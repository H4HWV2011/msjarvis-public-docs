crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/nvme1/msjarvis-rebuild$ cd /mnt/nvme1/msjarvis-rebuild

echo "=== backup compose ==="
cp docker-compose.yml docker-compose.yml.bak-lmsynth-cmd-$(date +%Y%m%d-%H%M%S)

echo "=== inspect current service block ==="
docker compose config | sed -n '/jarvis-lm-synthesizer:/,/^[^[:space:]]/p'

echo "=== patch command to mounted path /appservices/lm_synthesizer.py ==="
python3 - <<'PY'
from pathlib import Path
import re

p = Path("docker-compose.yml")
s = p.read_text()

m = re.search(r'(\n  jarvis-lm-synthesizer:\n(?:.*\n)*?)(?=\n  [A-Za-z0-9_-]+:\n|\Z)', s)
if not m:
    print("✗ jarvis-lm-synthesizer service block not found")
    raise SystemExit(1)

block = m.group(1)
docker inspect jarvis-lm-synthesizer --format '{{json .Config.Cmd}}' | python3 -m json.toolappse
=== backup compose ===
=== inspect current service block ===
      jarvis-lm-synthesizer:
        condition: service_started
        required: true
    environment:
      CLOCK_TS: "1767812077"
      JUDGE_ALIGNMENT_URL: http://jarvis-judge-alignment:7232
      JUDGE_CONSISTENCY_URL: http://jarvis-judge-consistency:7231
      JUDGE_ETHICS_URL: http://jarvis-judge-ethics:7233
      JUDGE_TRUTH_URL: http://jarvis-judge-truth:7230
      LM_SYNTHESIZER_URL: http://jarvis-lm-synthesizer:8001
      SERVICE_NAME: judge_pipeline
      SERVICE_PORT: "7239"
    expose:
      - "7239"
    networks:
      qualia-net: null
    restart: unless-stopped
  jarvis-judge-truth:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile.judge
    command:
      - python
      - judge_truth_filter.py
    container_name: jarvis-judge-truth
    environment:
      CLOCK_TS: "1767812077"
      SERVICE_NAME: judge_truth_filter
      SERVICE_PORT: "7230"
    expose:
      - "7230"
    networks:
      qualia-net: null
    restart: unless-stopped
  jarvis-kyc-vault:
    command:
      - uvicorn
      - app:app
      - --host
      - 0.0.0.0
      - --port
      - "8045"
    container_name: jarvis-kyc-vault
    environment:
      KYC_PG_DSN: postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
      KYC_RETENTION_DAYS: "90"
      PROVENANCE_URL: http://jarvis-provenance:8046
    expose:
      - "8045"
    image: msjarvis-rebuild-jarvis-kyc-vault
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8045
        published: "8045"
        protocol: tcp
    restart: unless-stopped
  jarvis-lm-synthesizer:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile.lm_synthesizer
    command:
      - python
      - lm_synthesizer.py
    container_name: jarvis-lm-synthesizer
    environment:
      CLOCK_TS: "1767812077"
      OLLAMA_HOST: http://jarvis-ollama:11434
      SERVICE_PORT: "8001"
    expose:
      - "8001"
    logging:
      driver: json-file
      options:
        max-file: "3"
        max-size: 10m
    networks:
      qualia-net: null
    restart: unless-stopped
  jarvis-local-resources:
    build:
      context: /mnt/nvme1/msjarvis-rebuild
      dockerfile: Dockerfile.local_resources
    container_name: jarvis-local-resources
    depends_on:
      jarvis-local-resources-db:
        condition: service_started
        required: true
    environment:
      CLOCK_TS: "1767812077"
      LOCAL_RESOURCES_DSN: postgresql://msjarvis:Nathaniel1@jarvis-local-resources-db:5432/local_resources
      PYTHONPATH: /app/services
    expose:
      - "8035"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8006
        published: "8006"
        protocol: tcp
    restart: unless-stopped
    volumes:
      - type: bind
        source: /mnt/nvme1/msjarvis-rebuild/services
        target: /app/services
        bind: {}
    working_dir: /app/services
  jarvis-local-resources-db:
    container_name: jarvis-local-resources-db
    environment:
      POSTGRES_DB: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_USER: postgres
    image: postgis/postgis:15-3.4
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 5432
        published: "5435"
        protocol: tcp
    restart: unless-stopped
    volumes:
      - type: bind
        source: /mnt/nvme1/msjarvis-rebuild/data/local_resources
        target: /var/lib/postgresql/data
        bind: {}
  jarvis-main-brain:
    build:
      context: /mnt/nvme1/msjarvis-rebuild
      dockerfile: Dockerfile
    command:
      - python
      - -m
      - uvicorn
      - main_brain:app
      - --host
      - 0.0.0.0
      - --port
      - "8050"
      - --proxy-headers
      - --forwarded-allow-ips=*
    container_name: jarvis-main-brain
    depends_on:
      jarvis-chroma:
        condition: service_started
        required: true
      jarvis-ollama:
        condition: service_started
        required: true
      jarvis-redis:
        condition: service_started
        required: true
    environment:
      CLOCK_TS: "1767812077"
      CONSTITUTIONAL_GUARDIAN_URL: http://jarvis-constitutional-guardian:8091
      JARVIS_API_KEY: super-secret-key
      JARVIS_API_KEY_FILE: /run/secrets/jarvisapikey
      MAX_CONCURRENT_CHATS: "4"
      RAG_SERVER_URL: http://jarvis-rag-server:8003
      RAG_URL: http://jarvis-rag-server:8003
      SERVICE_PORT: "8050"
    expose:
      - "8050"
    image: jarvis-main-brain:latest
    logging:
      driver: json-file
      options:
        max-file: "3"
        max-size: 10m
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8050
        published: "8050"
        protocol: tcp
    restart: unless-stopped
    secrets:
      - source: jarvisapikey
        target: /run/secrets/jarvisapikey
    volumes:
      - type: bind
        source: /mnt/nvme1/msjarvis-rebuild/services
        target: /app/services
        bind: {}
    working_dir: /app/services
  jarvis-memory:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile.memory
    container_name: jarvis-memory
    environment:
      JARVIS_API_KEY: c0ecca01f56b152430ee63967757a84386c0b8b022cbc6f5a27c5c9ee98ce267
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8056
        published: "8056"
        protocol: tcp
    restart: unless-stopped
  jarvis-mother-protocols:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile.mother_protocols
    container_name: jarvis-mother-protocols
    environment:
      CLOCK_TS: "1767812077"
    expose:
      - "4000"
    networks:
      qualia-net: null
    restart: unless-stopped
  jarvis-neurobiological-master:
    build:
      context: /mnt/nvme1/msjarvis-rebuild
      dockerfile: Dockerfile.neuro
    command:
      - python3
      - ms_jarvis_neurobiological_master.py
    container_name: jarvis-neurobiological-master
    depends_on:
      jarvis-blood-brain-barrier:
        condition: service_started
        required: true
      jarvis-i-containers:
        condition: service_started
        required: true
      jarvis-qualia-engine:
        condition: service_started
        required: true
    environment:
      CLOCK_TS: "1767812077"
      I_CONTAINERS_URL: http://jarvis-i-containers:8015
      OLLAMA_HOST: http://jarvis-ollama:11434
      QUALIA_URL: http://jarvis-qualia-engine:8017
    expose:
      - "8018"
    logging:
      driver: json-file
      options:
        max-file: "3"
        max-size: 10m
    networks:
      qualia-net: null
    restart: unless-stopped
    working_dir: /app/services
  jarvis-ollama:
    container_name: jarvis-ollama
    deploy:
      resources:
        limits:
          cpus: 8
          memory: "25769803776"
        reservations:
          devices:
            - capabilities:
                - gpu
              driver: nvidia
              count: -1
    environment:
      CLOCK_TS: "1767812077"
      OLLAMA_MODELS: /root/.ollama/models
    image: ollama/ollama:latest
    logging:
      driver: json-file
      options:
        max-file: "5"
        max-size: 50m
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 11434
        published: "11434"
        protocol: tcp
    restart: unless-stopped
    volumes:
      - type: bind
        source: /mnt/ssd2/msjarvis_secondary/models
        target: /root/.ollama/models
        bind: {}
  jarvis-phi-probe:
    command:
      - python3
      - ms_jarvis_phi_probe.py
    container_name: jarvis-phi-probe
    environment:
      CHROMA_URL: http://jarvis-chroma:8000
      REDIS_URL: redis://jarvis-redis:6379
    expose:
      - "8025"
    image: msjarvis-rebuild-jarvis-phi-probe
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8025
        published: "8026"
        protocol: tcp
    restart: unless-stopped
    volumes:
      - type: bind
        source: /mnt/nvme1/msjarvis-rebuild/services/ms_jarvis_phi_probe.py
        target: /app/ms_jarvis_phi_probe.py
        read_only: true
        bind: {}
  jarvis-pia-sampler:
    command:
      - sh
      - -c
      - pip install fastapi uvicorn redis -q && python3 pia_sampler_service.py
    container_name: jarvis-pia-sampler
    environment:
      REDIS_URL: redis://jarvis-redis:6379/0
    expose:
      - "8076"
    image: python:3.11-slim
    networks:
      qualia-net: null
    restart: unless-stopped
    volumes:
      - type: bind
        source: /mnt/spiritual_drive/msjarvis-rebuild/services/pia_sampler/pia_sampler_service.py
        target: /app/pia_sampler_service.py
        read_only: true
        bind: {}
    working_dir: /app
  jarvis-provenance:
    command:
      - uvicorn
      - app:app
      - --host
      - 0.0.0.0
      - --port
      - "8046"
    container_name: jarvis-provenance
    environment:
      IPFS_API_URL: http://ipfs:5001
      PROVENANCE_SIGNING_KEY: msjarvis-provenance-key-change-in-prod
    expose:
      - "8046"
    image: msjarvis-rebuild-jarvis-provenance
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8046
        published: "8046"
        protocol: tcp
    restart: unless-stopped
  jarvis-psychology-services:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile.psychology_services
    command:
      - python
      - ms_jarvis_psychology_services.py
    container_name: jarvis-psychology-services
    depends_on:
      psychological_rag_domain:
        condition: service_started
        required: true
    environment:
      CLOCK_TS: "1767812077"
      PSYCHOLOGICAL_RAG_URL: http://psychological_rag_domain:9006
      SERVICE_PORT: "8019"
    expose:
      - "8019"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8019
        published: "8019"
        protocol: tcp
    restart: unless-stopped
    working_dir: /app
  jarvis-qualia-engine:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile.qualia
    container_name: jarvis-qualia-engine
    depends_on:
      jarvis-ollama:
        condition: service_started
        required: true
    environment:
      CLOCK_TS: "1767812077"
      OLLAMA_HOST: http://jarvis-ollama:11434
    expose:
      - "8017"
    logging:
      driver: json-file
      options:
        max-file: "3"
        max-size: 10m
    networks:
      qualia-net: null
    restart: unless-stopped
    volumes:
      - type: bind
        source: /mnt/nvme1/msjarvis-rebuild/services/ms_jarvis_qualia_engine.py
        target: /app/services/ms_jarvis_qualia_engine.py
        read_only: true
        bind: {}
  jarvis-rag-router:
    command:
      - uvicorn
      - rag_query_router:app
      - --host
      - 0.0.0.0
      - --port
      - "5001"
    container_name: jarvis-rag-router
    environment:
      CHROMA_HOST: jarvis-chroma
      CHROMA_PORT: "8000"
      SERVICE_PORT: "5001"
    expose:
      - "5001"
      - "8003"
    image: msjarvis-rebuild-jarvis-rag-router
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 5001
        published: "5015"
        protocol: tcp
    restart: unless-stopped
  jarvis-rag-server:
    build:
      context: /mnt/nvme1/msjarvis-rebuild
      dockerfile: Dockerfile.rag_server
    command:
      - uvicorn
      - rag_server_main:app
      - --host
      - 0.0.0.0
      - --port
      - "8003"
    container_name: jarvis-rag-server
    depends_on:
      jarvis-chroma:
        condition: service_started
        required: true
      jarvis-local-resources-db:
        condition: service_started
        required: true
    environment:
      CHROMA_HOST: jarvis-chroma
      CHROMA_PORT: "8000"
      CHROMA_URL: http://jarvis-chroma:8000
      CLOCK_TS: "1767812077"
      EPISODIC_DSN: dbname=postgres user=postgres password=postgres host=jarvis-local-resources-db
      SERVICE_PORT: "8003"
    expose:
      - "8003"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8003
        published: "8003"
        protocol: tcp
    restart: unless-stopped
    volumes:
      - type: bind
        source: /home/cakidd/msjarvis-rebuild/data/mountainshares
        target: /app/mountainshares_docs
        read_only: true
        bind: {}
      - type: bind
        source: /mnt/nvme1/msjarvis-rebuild/services/backup_chroma_mountainshares_knowledge.json
        target: /app/backup_mountainshares.json
        read_only: true
        bind: {}
      - type: volume
        source: rag_model_cache
        target: /root/.cache/chroma
        volume: {}
    working_dir: /app/services
  jarvis-redis:
    container_name: jarvis-redis
    environment:
      CLOCK_TS: "1767812077"
    healthcheck:
      test:
        - CMD
        - redis-cli
        - ping
      timeout: 10s
      interval: 30s
      retries: 3
    image: redis:7-alpine
    logging:
      driver: json-file
      options:
        max-file: "3"
        max-size: 10m
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 6379
        published: "6380"
        protocol: tcp
    restart: always
  jarvis-semaphore:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile.semaphore
    container_name: jarvis-semaphore
    expose:
      - "8030"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8030
        published: "8030"
        protocol: tcp
    restart: unless-stopped
  jarvis-session-sidecar:
    command:
      - uvicorn
      - app:app
      - --host
      - 0.0.0.0
      - --port
      - "8060"
    container_name: jarvis-session-sidecar
    environment:
      LOCAL_RESOURCES_DSN: postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
      SESSION_REDIS_HOST: jarvis-redis
      SESSION_REDIS_MAX_ITEMS: "20"
      SESSION_REDIS_PORT: "6379"
      SESSION_REDIS_TTL: "1800"
    expose:
      - "8060"
      - "8070"
    image: jarvis-session-sidecar:latest
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8060
        published: "8060"
        protocol: tcp
    restart: unless-stopped
  jarvis-spiritual-rag:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile.spiritual_rag
    container_name: jarvis-spiritual-rag
    depends_on:
      jarvis-chroma:
        condition: service_started
        required: true
    environment:
      CHROMA_HOST: jarvis-chroma
      CHROMA_PORT: "8000"
      CLOCK_TS: "1767812077"
      SERVICE_PORT: "8005"
    expose:
      - "8005"
    logging:
      driver: json-file
      options:
        max-file: "3"
        max-size: 10m
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8005
        published: "8005"
        protocol: tcp
    restart: unless-stopped
  jarvis-steward:
    command:
      - python3
      - jarvis_steward.py
    container_name: jarvis-steward
    environment:
      REDIS_HOST: jarvis-redis
      REDIS_PORT: "6379"
      REDIS_URL: redis://jarvis-redis:6379/0
      SERVICE_PORT: "8014"
    image: jarvis-main-brain:latest
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8014
        published: "8014"
        protocol: tcp
    restart: unless-stopped
    volumes:
      - type: bind
        source: /mnt/nvme1/msjarvis-rebuild/services/jarvis_steward.py
        target: /app/services/jarvis_steward.py
        read_only: true
        bind: {}
    working_dir: /app/services
  jarvis-stewardship-scheduler:
    command:
      - python3
      - jarvis_stewardship_scheduler.py
    container_name: jarvis-stewardship-scheduler
    depends_on:
      jarvis-local-resources-db:
        condition: service_started
        required: true
      jarvis-redis:
        condition: service_started
        required: true
    environment:
      DB_DSN: postgresql://postgres:postgres@jarvis-local-resources-db:5432/local_resources
      REDIS_URL: redis://jarvis-redis:6379/0
      SERVICE_PORT: "8079"
    expose:
      - "8079"
    image: jarvis-main-brain:latest
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8079
        published: "8079"
        protocol: tcp
    restart: unless-stopped
    volumes:
      - type: bind
        source: /mnt/nvme1/msjarvis-rebuild/services
        target: /app/services
        read_only: true
        bind: {}
    working_dir: /app/services
  jarvis-swarm-intelligence:
    build:
      context: /mnt/nvme1/msjarvis-rebuild
      dockerfile: Dockerfile.swarm
    command:
      - python3
      - ms_jarvis_swarm_intelligence.py
    container_name: jarvis-swarm-intelligence
    environment:
      CLOCK_TS: "1767812077"
      OLLAMA_HOST: http://jarvis-ollama:11434
      SERVICE_PORT: "8021"
    expose:
      - "8021"
    logging:
      driver: json-file
      options:
        max-file: "3"
        max-size: 10m
    networks:
      qualia-net: null
    restart: unless-stopped
    working_dir: /app/services
  jarvis-temporal-consciousness:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile.temporal_consciousness
    container_name: jarvis-temporal-consciousness
    environment:
      CLOCK_TS: "1767812077"
    expose:
      - "7007"
    networks:
      qualia-net: null
    restart: unless-stopped
  jarvis-toroidal:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile.toroidal
    container_name: jarvis-toroidal
    depends_on:
      jarvis-consciousness-bridge:
        condition: service_started
        required: true
      jarvis-ollama:
        condition: service_started
        required: true
    environment:
      CLOCK_TS: "1767812077"
      CONSCIOUSNESS_BRIDGE_URL: http://jarvis-consciousness-bridge:8020
      OLLAMA_HOST: http://jarvis-ollama:11434
    image: msjarvis-toroidal:latest
    logging:
      driver: json-file
      options:
        max-file: "3"
        max-size: 10m
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8025
        published: "8025"
        protocol: tcp
    restart: unless-stopped
  jarvis-unified-gateway:
    build:
      context: /mnt/nvme1/msjarvis-rebuild
      dockerfile: Dockerfile.gateway
    command:
      - python3
      - ms_jarvis_unified_gateway.py
    container_name: jarvis-unified-gateway
    depends_on:
      jarvis-20llm-production:
        condition: service_started
        required: true
      jarvis-blood-brain-barrier:
        condition: service_started
        required: true
      jarvis-brain-orchestrator:
        condition: service_started
        required: true
      jarvis-chroma:
        condition: service_started
        required: true
      jarvis-consciousness-bridge:
        condition: service_started
        required: true
      jarvis-constitutional-guardian:
        condition: service_started
        required: true
      jarvis-fifth-dgm:
        condition: service_started
        required: true
      jarvis-fractal-consciousness:
        condition: service_started
        required: true
      jarvis-i-containers:
        condition: service_started
        required: true
      jarvis-lm-synthesizer:
        condition: service_started
        required: true
      jarvis-neurobiological-master:
        condition: service_started
        required: true
      jarvis-ollama:
        condition: service_started
        required: true
      jarvis-psychology-services:
        condition: service_started
        required: true
      jarvis-qualia-engine:
        condition: service_started
        required: true
      jarvis-redis:
        condition: service_started
        required: true
      jarvis-toroidal:
        condition: service_started
        required: true
      jarvis-woah:
        condition: service_started
        required: true
      nbb-i-containers:
        condition: service_started
        required: true
      nbb_consciousness_containers:
        condition: service_started
        required: true
      nbb_heteroglobulin_transport:
        condition: service_started
        required: true
      nbb_mother_carrie_protocols:
        condition: service_started
        required: true
      nbb_pituitary_gland:
        condition: service_started
        required: true
      nbb_prefrontal_cortex:
        condition: service_started
        required: true
      nbb_spiritual_maternal_integration:
        condition: service_started
        required: true
      nbb_spiritual_root:
        condition: service_started
        required: true
      nbb_subconscious:
        condition: service_started
        required: true
      nbb_woah_algorithms:
        condition: service_started
        required: true
      psychological_rag_domain:
        condition: service_started
        required: true
    deploy:
      resources:
        limits:
          cpus: 2
          memory: "4294967296"
    environment:
      BBB_URL: http://jarvis-blood-brain-barrier:8016
      CLOCK_TS: "1767812077"
      CONSCIOUSNESS_BRIDGE_URL: http://jarvis-consciousness-bridge:8020
      CONSTITUTIONAL_GUARDIAN_URL: http://jarvis-constitutional-guardian:8091
      FIFTH_DGM_URL: http://jarvis-fifth-dgm:4002
      FRACTAL_URL: http://jarvis-fractal-consciousness:8027
      JARVIS_API_KEY: super-secret-key
      JARVIS_API_KEY_FILE: /run/secrets/jarvisapikey
      MAX_CONCURRENT_CHATS: "4"
      NEURO_MASTER_URL: http://jarvis-neurobiological-master:8018
      PSYCHOLOGICAL_RAG_URL: http://psychological_rag_domain:9006
      PSYCHOLOGY_SERVICES_URL: http://jarvis-psychology-services:8019
      SERVICE_PORT: "8001"
      TOROIDAL_URL: http://jarvis-toroidal:8025
      WOAH_URL: http://jarvis-woah:7012
    healthcheck:
      test:
        - CMD
        - python3
        - -c
        - import urllib.request, sys; r = urllib.request.urlopen('http://127.0.0.1:8001/health', timeout=5); sys.exit(0 if r.status == 200 else 1)
      timeout: 10s
      interval: 30s
      retries: 3
      start_period: 20s
    logging:
      driver: json-file
      options:
        max-file: "5"
        max-size: 10m
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8001
        published: "8001"
        protocol: tcp
    restart: unless-stopped
    secrets:
      - source: jarvisapikey
        target: /run/secrets/jarvisapikey
    volumes:
      - type: bind
        source: /mnt/nvme1/msjarvis-rebuild/services
        target: /app/services
        bind: {}
    working_dir: /app/services
  jarvis-web-research:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile.web_research
    command:
      - python
      - ms_jarvis_web_research_simple.py
    container_name: jarvis-web-research
    environment:
      CLOCK_TS: "1767812077"
      RAG_SERVER_URL: http://jarvis-rag-server:8003
      SERVICE_PORT: "8008"
    expose:
      - "8008"
    logging:
      driver: json-file
      options:
        max-file: "3"
        max-size: 10m
    networks:
      qualia-net: null
    restart: unless-stopped
  jarvis-woah:
    build:
      context: /mnt/nvme1/msjarvis-rebuild
      dockerfile: Dockerfile.woah
    container_name: jarvis-woah
    depends_on:
      jarvis-ollama:
        condition: service_started
        required: true
    environment:
      CLOCK_TS: "1767812077"
      OLLAMA_HOST: http://jarvis-ollama:11434
      SERVICE_PORT: "7012"
    expose:
      - "7012"
    logging:
      driver: json-file
      options:
        max-file: "3"
        max-size: 10m
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 7012
        published: "7012"
        protocol: tcp
    restart: unless-stopped
    volumes:
      - type: bind
        source: /mnt/nvme1/msjarvis-rebuild/services
        target: /app
        bind: {}
  jarvis-wv-entangled-gateway:
    build:
      context: /mnt/nvme1/msjarvis-rebuild
      dockerfile: Dockerfile
    command:
      - python
      - -m
      - uvicorn
      - msjarvis_wv_entangled_gateway:app
      - --host
      - 0.0.0.0
      - --port
      - "8010"
      - --log-level
      - info
    container_name: jarvis-wv-entangled-gateway
    depends_on:
      jarvis-20llm-production:
        condition: service_started
        required: true
    environment:
      CLOCK_TS: "1767812077"
      SERVICE_PORT: "8010"
    expose:
      - "8010"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8010
        published: "8010"
        protocol: tcp
    restart: unless-stopped
    volumes:
      - type: bind
        source: /mnt/nvme1/msjarvis-rebuild/services
        target: /app/services
        bind: {}
    working_dir: /app/services
  llm1-proxy:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile-llm1-proxy
    container_name: llm1-proxy
    environment:
      CLOCK_TS: "1767812077"
    expose:
      - "8201"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8201
        published: "8201"
        protocol: tcp
    restart: unless-stopped
  llm2-proxy:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile-llm2-proxy
    container_name: llm2-proxy
    environment:
      CLOCK_TS: "1767812077"
    expose:
      - "8202"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8202
        published: "8202"
        protocol: tcp
    restart: unless-stopped
  llm3-proxy:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile-llm3-proxy
    container_name: llm3-proxy
    environment:
      CLOCK_TS: "1767812077"
    expose:
      - "8203"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8203
        published: "8203"
        protocol: tcp
    restart: unless-stopped
  llm4-proxy:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile-llm4-proxy
    container_name: llm4-proxy
    environment:
      CLOCK_TS: "1767812077"
    expose:
      - "8204"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8204
        published: "8204"
        protocol: tcp
    restart: unless-stopped
  llm5-proxy:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile-llm5-proxy
    container_name: llm5-proxy
    environment:
      CLOCK_TS: "1767812077"
    expose:
      - "8205"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8205
        published: "8205"
        protocol: tcp
    restart: unless-stopped
  llm6-proxy:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile-llm6-proxy
    container_name: llm6-proxy
    environment:
      CLOCK_TS: "1767812077"
    expose:
      - "8206"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8206
        published: "8206"
        protocol: tcp
    restart: unless-stopped
  llm7-proxy:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile-llm7-proxy
    container_name: llm7-proxy
    environment:
      CLOCK_TS: "1767812077"
    expose:
      - "8207"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8207
        published: "8207"
        protocol: tcp
    restart: unless-stopped
  llm8-proxy:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile-llm8-proxy
    container_name: llm8-proxy
    environment:
      CLOCK_TS: "1767812077"
    expose:
      - "8208"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8208
        published: "8208"
        protocol: tcp
    restart: unless-stopped
  llm9-proxy:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile-llm9-proxy
    container_name: llm9-proxy
    environment:
      CLOCK_TS: "1767812077"
    expose:
      - "8209"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8209
        published: "8209"
        protocol: tcp
    restart: unless-stopped
  llm10-proxy:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile-llm10-proxy
    container_name: llm10-proxy
    environment:
      CLOCK_TS: "1767812077"
    expose:
      - "8210"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8210
        published: "8210"
        protocol: tcp
    restart: unless-stopped
  llm11-proxy:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile-llm11-proxy
    container_name: llm11-proxy
    environment:
      CLOCK_TS: "1767812077"
    expose:
      - "8211"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8211
        published: "8211"
        protocol: tcp
    restart: unless-stopped
  llm12-proxy:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile-llm12-proxy
    container_name: llm12-proxy
    environment:
      CLOCK_TS: "1767812077"
    expose:
      - "8212"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8212
        published: "8212"
        protocol: tcp
    restart: unless-stopped
  llm13-proxy:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile-llm13-proxy
    container_name: llm13-proxy
    environment:
      CLOCK_TS: "1767812077"
    expose:
      - "8213"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8213
        published: "8213"
        protocol: tcp
    restart: unless-stopped
  llm14-proxy:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile-llm14-proxy
    container_name: llm14-proxy
    environment:
      CLOCK_TS: "1767812077"
    expose:
      - "8214"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8214
        published: "8214"
        protocol: tcp
    restart: unless-stopped
  llm15-proxy:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile-llm15-proxy
    container_name: llm15-proxy
    environment:
      CLOCK_TS: "1767812077"
    expose:
      - "8215"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8215
        published: "8215"
        protocol: tcp
    restart: unless-stopped
  llm16-proxy:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile-llm16-proxy
    container_name: llm16-proxy
    environment:
      CLOCK_TS: "1767812077"
    expose:
      - "8216"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8216
        published: "8216"
        protocol: tcp
    restart: unless-stopped
  llm17-proxy:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile-llm17-proxy
    container_name: llm17-proxy
    environment:
      CLOCK_TS: "1767812077"
    expose:
      - "8217"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8217
        published: "8217"
        protocol: tcp
    restart: unless-stopped
  llm18-proxy:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile-llm18-proxy
    container_name: llm18-proxy
    environment:
      CLOCK_TS: "1767812077"
    expose:
      - "8218"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8218
        published: "8218"
        protocol: tcp
    restart: unless-stopped
  llm19-proxy:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile-llm19-proxy
    container_name: llm19-proxy
    environment:
      CLOCK_TS: "1767812077"
    expose:
      - "8219"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8219
        published: "8219"
        protocol: tcp
    restart: unless-stopped
  llm20-proxy:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile-llm20-proxy
    container_name: llm20-proxy
    environment:
      CLOCK_TS: "1767812077"
    expose:
      - "8220"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8220
        published: "8220"
        protocol: tcp
    restart: unless-stopped
  llm21-proxy:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile-llm21-proxy
    container_name: llm21-proxy
    environment:
      CLOCK_TS: "1767812077"
    expose:
      - "8221"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8221
        published: "8221"
        protocol: tcp
    restart: unless-stopped
  llm22-proxy:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile-llm22-proxy
    container_name: llm22-proxy
    environment:
      CLOCK_TS: "1767812077"
    expose:
      - "8222"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8222
        published: "8222"
        protocol: tcp
    restart: unless-stopped
  ms-mountainshares-analytics:
    command:
      - sh
      - -c
      - cd /app/services && python3 ms_mountainshares_analytics.py
    container_name: jarvis-ms-analytics
    depends_on:
      ms-mountainshares-coordinator:
        condition: service_started
        required: true
    environment:
      PORT: "8083"
      ROLE: analytics
    image: jarvis-main-brain:latest
    networks:
      default: null
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8083
        published: "8083"
        protocol: tcp
    restart: unless-stopped
  ms-mountainshares-coordinator:
    command:
      - sh
      - -c
      - cd /app/services && python3 ms_mountainshares_coordinator.py
    container_name: jarvis-ms-coordinator
    depends_on:
      jarvis-local-resources-db:
        condition: service_started
        required: true
      jarvis-redis:
        condition: service_started
        required: true
    environment:
      DB_DSN: postgresql://postgres:postgres@jarvis-local-resources-db:5432/local_resources
      REDIS_URL: redis://jarvis-redis:6379
      SERVICE_PORT: "7300"
    expose:
      - "7300"
    image: jarvis-main-brain:latest
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 7300
        published: "7300"
        protocol: tcp
    restart: unless-stopped
    working_dir: /app/services
  ms-mountainshares-indexer:
    command:
      - sh
      - -c
      - cd /app/services && python3 ms_mountainshares_indexer.py
    container_name: jarvis-ms-indexer
    depends_on:
      ms-mountainshares-coordinator:
        condition: service_started
        required: true
    environment:
      PORT: "8080"
      ROLE: indexer
    image: jarvis-main-brain:latest
    networks:
      default: null
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8080
        published: "8080"
        protocol: tcp
    restart: unless-stopped
  mysql:
    container_name: mysql
    environment:
      CLOCK_TS: "1767812077"
      MYSQL_DATABASE: quantum_ai
      MYSQL_PASSWORD: j4rv1sgeo!
      MYSQL_ROOT_PASSWORD: my_secret_root_pw
      MYSQL_USER: msjarvis
    image: mysql:8.2
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 3306
        published: "3307"
        protocol: tcp
    restart: always
    volumes:
      - type: bind
        source: /mnt/nvme1/msjarvis-rebuild/data/mysql
        target: /var/lib/mysql
        bind: {}
  nbb-i-containers:
    build:
      context: /mnt/nvme1/msjarvis-rebuild
      dockerfile: Dockerfile.nbb_icontainers_fastapi
    container_name: nbb-i-containers
    environment:
      CLOCK_TS: "1767812077"
      NBB_ICONTAINERS_URL: http://nbb_i-containers:7005
    expose:
      - "7005"
    networks:
      qualia-net:
        aliases:
          - nbb_i-containers
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 7005
        published: "8101"
        protocol: tcp
    restart: "no"
  nbb_blood_brain_barrier:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/neurobiological_brain/blood_brain_barrier/service
      dockerfile: Dockerfile
    container_name: nbb_blood_brain_barrier
    environment:
      CLOCK_TS: "1767812077"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8010
        published: "8301"
        protocol: tcp
    restart: unless-stopped
  nbb_consciousness_containers:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/neurobiological_brain/consciousness_containers/service
      dockerfile: Dockerfile
    container_name: nbb_consciousness_containers
    environment:
      CLOCK_TS: "1767812077"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8010
        published: "8102"
        protocol: tcp
    restart: unless-stopped
  nbb_darwin_godel_machines:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/neurobiological_brain/darwin_godel_machines/service
      dockerfile: Dockerfile
    container_name: nbb_darwin_godel_machines
    environment:
      CLOCK_TS: "1767812077"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8010
        published: "8302"
        protocol: tcp
    restart: unless-stopped
  nbb_heteroglobulin_transport:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/neurobiological_brain/heteroglobulin_transport/service
      dockerfile: Dockerfile
    container_name: nbb_heteroglobulin_transport
    environment:
      CLOCK_TS: "1767812077"
      SERVICE_REDIS_ENABLED: "true"
      SERVICE_REDIS_HOST: jarvis-redis
      SERVICE_REDIS_PORT: "6379"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8010
        published: "8106"
        protocol: tcp
    restart: unless-stopped
  nbb_i_containers:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/neurobiological_brain/i_containers/service
      dockerfile: Dockerfile
    command:
      - sh
      - -c
      - ln -sfn /app/neurobiological_brain/i_containers /app/neurobiological_brain/neurobiologicalbrain/i_containers 2>/dev/null; python3 ms_jarvis_i_containers_service.py
    container_name: jarvis-nbb-i-containers-2
    environment:
      CLOCK_TS: null
      PYTHONPATH: /app:/app/services:/app/neurobiological_brain
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8015
        published: "8015"
        protocol: tcp
    restart: unless-stopped
    volumes:
      - type: bind
        source: /mnt/nvme1/msjarvis-rebuild/neurobiological_brain
        target: /app/neurobiological_brain
        bind: {}
      - type: bind
        source: /home/cakidd/i-containers-overlay/integration_layer
        target: /app/integration_layer
        read_only: true
        bind: {}
    working_dir: /app
  nbb_mother_carrie_protocols:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/neurobiological_brain/mother_carrie_protocols/service
      dockerfile: Dockerfile
    container_name: nbb_mother_carrie_protocols
    environment:
      CLOCK_TS: "1767812077"
      SERVICE_PORT: "8010"
      SERVICE_REDIS_ENABLED: "true"
      SERVICE_REDIS_HOST: jarvis-redis
      SERVICE_REDIS_PORT: "6379"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8010
        published: "8107"
        protocol: tcp
    restart: unless-stopped
  nbb_pituitary_gland:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/neurobiological_brain/pituitary_gland/service
      dockerfile: Dockerfile
    container_name: nbb_pituitary_gland
    environment:
      CLOCK_TS: "1767812077"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 80
        published: "8108"
        protocol: tcp
    restart: unless-stopped
  nbb_prefrontal_cortex:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/neurobiological_brain/prefrontal_cortex/service
      dockerfile: Dockerfile
    container_name: nbb_prefrontal_cortex
    environment:
      CLOCK_TS: "1767812077"
      SERVICE_REDIS_ENABLED: "true"
      SERVICE_REDIS_HOST: jarvis-redis
      SERVICE_REDIS_PORT: "6379"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8010
        published: "8105"
        protocol: tcp
    restart: unless-stopped
  nbb_qualia_engine:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/neurobiological_brain/qualia_engine/service
      dockerfile: Dockerfile
    container_name: nbb_qualia_engine
    environment:
      CLOCK_TS: "1767812077"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8010
        published: "8303"
        protocol: tcp
    restart: unless-stopped
  nbb_spiritual_maternal_integration:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/neurobiological_brain/spiritual_maternal_integration/service
      dockerfile: Dockerfile
    container_name: nbb_spiritual_maternal_integration
    environment:
      CLOCK_TS: "1767812077"
      SERVICE_PORT: "8010"
      SERVICE_REDIS_ENABLED: "true"
      SERVICE_REDIS_HOST: jarvis-redis
      SERVICE_REDIS_PORT: "6379"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8010
        published: "8109"
        protocol: tcp
    restart: unless-stopped
  nbb_spiritual_root:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/neurobiological_brain/spiritual_root/service
      dockerfile: Dockerfile
    container_name: nbb_spiritual_root
    environment:
      CLOCK_TS: "1767812077"
      SERVICE_PORT: "8010"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8010
        published: "8103"
        protocol: tcp
    restart: unless-stopped
  nbb_subconscious:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/neurobiological_brain/subconscious/service
      dockerfile: Dockerfile
    container_name: nbb_subconscious
    environment:
      CLOCK_TS: "1767812077"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8010
        published: "8112"
        protocol: tcp
    restart: unless-stopped
  nbb_woah_algorithms:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/neurobiological_brain/woah_algorithms/service
      dockerfile: Dockerfile
    container_name: nbb_woah_algorithms
    environment:
      CLOCK_TS: "1767812077"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8010
        published: "8104"
        protocol: tcp
    restart: unless-stopped
  neo4j:
    container_name: neo4j
    environment:
      CLOCK_TS: "1767812077"
      NEO4J_ACCEPT_LICENSE_AGREEMENT: "yes"
      NEO4J_AUTH: neo4j/neo4jpassword
    image: neo4j:5.13-community
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 7687
        published: "7687"
        protocol: tcp
      - mode: ingress
        host_ip: 127.0.0.1
        target: 7474
        published: "7475"
        protocol: tcp
    restart: unless-stopped
  psychological_rag_domain:
    build:
      context: /mnt/nvme1/msjarvis-rebuild/services
      dockerfile: Dockerfile.psychological_rag
    command:
      - python
      - psychological_rag_domain.py
    container_name: psychological_rag_domain
    environment:
      CLOCK_TS: "1767812077"
    expose:
      - "8006"
    networks:
      qualia-net: null
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8006
        published: "9006"
        protocol: tcp
    restart: unless-stopped
    working_dir: /app
networks:
=== patch command to mounted path /appservices/lm_synthesizer.py ===
✗ no matching command stanza found; inspect the service block manually
=== validate compose ===
✓ compose valid
=== recreate synthesizer ===
[+] up 1/1
 ✔ Container jarvis-lm-synthesizer Started                                                  0.6s
=== verify mounted rewrite exists ===
ls: cannot access '/appservices/lm_synthesizer.py': No such file or directory
grep: /appservices/lm_synthesizer.py: No such file or directory
=== verify running command ===
[
    "python",
    "lm_synthesizer.py"
]
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/nvme1/msjarvis-rebuild$ 

