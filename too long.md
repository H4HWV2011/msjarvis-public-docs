Expecting value: line 1 column 1 (char 0)
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ cd ~/msjarvis-rebuild-working/msjarvis-rebuild || exit 1

echo "== psych services =="
sed -n '1370,1405p' docker-compose.yml

echo "== pia-status block =="
awk '/jarvis-pia-status:/,/^[^ ]/' docker-compose.yml
== psych services ==
    volumes:
    - /home/cakidd/msjarvis-rebuild-working/msjarvis-rebuild/data/local_resources:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: postgres
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    networks:
    - qualia-net
    restart: unless-stopped
  jarvis-psychology-services:
    image: msjarvis-rebuild-jarvis-psychology-services:latest
    container_name: jarvis-psychology-services
    command:
    - python
    - ms_jarvis_psychology_services.py
    ports:
    - 127.0.0.1:8019:8019
    networks:
    - qualia-net
    restart: unless-stopped
  jarvis-rag-server:
    build:
      context: ./services
      dockerfile: Dockerfile.rag_server
    image: msjarvis-rebuild-jarvis-rag-server:latest
    container_name: jarvis-rag-server
    working_dir: /app/services
    command:
    - python3
    - ms_jarvis_rag_server.py
    ports:
    - 127.0.0.1:8003:8003
    environment:
    - SERVICE_PORT=8003
    - RAG_PORT=8003
    - CLOCK_TS=1767812077
== pia-status block ==
  jarvis-pia-status:
    image: python:3.11-slim
    working_dir: /app
    command: >
      sh -c "pip install fastapi uvicorn[standard] httpx &&
             uvicorn services.jarvis_pia_status:app --host 0.0.0.0 --port 8029"
    volumes:
      - .:/app:ro
    environment:
      - PIA_WINDOW_MINUTES=240
      - JARVIS_MEMORY_URL=http://jarvis-memory:8056
      - JARVIS_PSYCH_URL=http://jarvis-psychology-services:8019/health
      - JARVIS_PSYCH_RAG_URL=http://psychologicalragdomain:8006/health
      - JARVIS_BBB_URL=http://jarvis-blood-brain-barrier:8016/health
    restart: unless-stopped
    depends_on:
      - jarvis-memory
      - jarvis-psychology-services
      - psychologicalragdomain
      - jarvis-blood-brain-barrier

  jarvis-main-brain:
    build:
      context: .
      dockerfile: Dockerfile.brain
    container_name: jarvis-main-brain
    environment:
    - SERVICE_PORT=8050
    - OLLAMA_HOST=http://jarvis-ollama:11434
    - I_CONTAINERS_URL=http://jarvis-i-containers:8015
    - QUALIA_URL=http://jarvis-qualia-engine:8017
    - CHROMA_URL=http://jarvis-chroma:8000
    - REDIS_URL=redis://jarvis-redis:6379
    - BBB_URL=http://jarvis-blood-brain-barrier:8016
    - WOAH_URL=http://jarvis-woah:7012
    - TOROIDAL_URL=http://jarvis-toroidal:8025
    - FRACTAL_URL=http://jarvis-fractal-consciousness:8027
    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
    - NEURO_MASTER_URL=http://jarvis-neurobiological-master:8018
    - JARVIS_API_KEY=super-secret-key
    - JARVIS_API_KEY_FILE=/run/secrets/jarvisapikey
    - MAX_CONCURRENT_CHATS=4
    - CLOCK_TS=1767812077
    ports:
    - 127.0.0.1:8050:8050
    depends_on:
    - jarvis-redis
    - jarvis-chroma
    - jarvis-ollama
    - jarvis-unified-gateway
    - jarvis-brain-orchestrator
    - jarvis-lm-synthesizer
    - jarvis-20llm-production
    - jarvis-blood-brain-barrier
    - jarvis-woah
    - jarvis-consciousness-bridge
    - jarvis-fractal-consciousness
    - jarvis-qualia-engine
    - jarvis-i-containers
    - jarvis-neurobiological-master
    - nbb_i_containers
    - nbb_consciousness_containers
    - nbb_spiritual_root
    - nbb_woah_algorithms
    - nbb_prefrontal_cortex
    - nbb_heteroglobulin_transport
    - nbb_mother_carrie_protocols
    - nbb_pituitary_gland
    - nbb_spiritual_maternal_integration
    - nbb_subconscious
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
    - ./services:/app/services
    healthcheck:
      test:
      - CMD
      - python3
      - -c
      - import urllib.request, sys; r = urllib.request.urlopen('http://127.0.0.1:8050/health',
        timeout=5); sys.exit(0 if r.status == 200 else 1)
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 20s
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: '5'
    deploy:
      resources:
        limits:
          cpus: '2.0'
          memory: 4g
    secrets:
    - jarvisapikey
  jarvis-unified-gateway:
    build:
      context: /home/cakidd/msjarvis-safe/recovered-services_20llm_full
      dockerfile: Dockerfile.gateway
    container_name: jarvis-unified-gateway
    working_dir: /app/services
    command:
    - python3
    - ms_jarvis_unified_gateway.py
    ports:
    - 127.0.0.1:18018:8001
    environment:
    - OLLAMA_HOST=http://jarvis-ollama:11434
    - BBB_URL=http://jarvis-blood-brain-barrier:8016
    - SERVICE_PORT=8001
    - CLOCK_TS=1767812077
    - JARVIS_API_KEY=super-secret-key
    depends_on:
    - jarvis-redis
    - jarvis-ollama
    - jarvis-chroma
    - jarvis-blood-brain-barrier
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
    - ./services:/app/services
  jarvis-20llm-production:
    build:
      context: .
      dockerfile: Dockerfile.brain
    container_name: jarvis-20llm-production
    working_dir: /app/services
    command:
    - python3
    - ai_server_20llm_PRODUCTION.py
    expose:
    - '8008'
    ports:
    - 127.0.0.1:8008:8008
    environment:
    - SERVICE_PORT=8008
    - OLLAMA_HOST=http://jarvis-ollama:11434
    - CLOCK_TS=1767812077
    depends_on:
    - jarvis-ollama
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
    - ./services:/app/services
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: '3'
  jarvis-semaphore:
    build:
      context: /home/cakidd/msjarvis-safe/recovered-services_20llm_full
      dockerfile: Dockerfile.semaphore
    container_name: jarvis-semaphore
    working_dir: /app/services
    command:
    - uvicorn
    - jarvis-semaphore_msjarvis_semaphore:app
    - --host
    - 0.0.0.0
    - --port
    - '8030'
    expose:
    - '8030'
    ports:
    - 127.0.0.1:8030:8030
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
    - ./services:/app/services
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: '3'
  llm1-proxy:
    image: msjarvis-rebuild-llm1-proxy:latest
    container_name: llm1-proxy
    expose:
    - '8201'
    ports:
    - 127.0.0.1:8201:8201
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
      - ./services/llm1-proxy_llm1_health_proxy.py:/app/llm1_health_proxy.py
      - ./services/crypto_client.py:/app/crypto_client.py
    environment:
      CLOCK_TS: 1767812077
  llm2-proxy:
    image: msjarvis-rebuild-llm2-proxy:latest
    container_name: llm2-proxy
    expose:
    - '8202'
    ports:
    - 127.0.0.1:8202:8202
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
      - ./services/llm2-proxy_llm2_health_proxy.py:/app/llm2_health_proxy.py
      - ./services/crypto_client.py:/app/crypto_client.py
    environment:
      CLOCK_TS: 1767812077
  llm3-proxy:
    image: msjarvis-rebuild-llm3-proxy:latest
    container_name: llm3-proxy
    expose:
    - '8203'
    ports:
    - 127.0.0.1:8203:8203
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
      - ./services/llm3-proxy_llm3_health_proxy.py:/app/llm3_health_proxy.py
      - ./services/crypto_client.py:/app/crypto_client.py
    environment:
      CLOCK_TS: 1767812077
  llm4-proxy:
    image: msjarvis-rebuild-llm4-proxy:latest
    container_name: llm4-proxy
    expose:
    - '8204'
    ports:
    - 127.0.0.1:8204:8204
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
      - ./services/llm4-proxy_llm4_health_proxy.py:/app/llm4_health_proxy.py
      - ./services/crypto_client.py:/app/crypto_client.py
    environment:
      CLOCK_TS: 1767812077
  llm5-proxy:
    image: msjarvis-rebuild-llm5-proxy:latest
    container_name: llm5-proxy
    expose:
    - '8205'
    ports:
    - 127.0.0.1:8205:8205
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
      - ./services/llm5-proxy_llm5_health_proxy.py:/app/llm5_health_proxy.py
      - ./services/crypto_client.py:/app/crypto_client.py
    environment:
      CLOCK_TS: 1767812077
  llm6-proxy:
    image: msjarvis-rebuild-llm6-proxy:latest
    container_name: llm6-proxy
    expose:
    - '8206'
    ports:
    - 127.0.0.1:8206:8206
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
      - ./services/llm6-proxy_llm6_health_proxy.py:/app/llm6_health_proxy.py
      - ./services/crypto_client.py:/app/crypto_client.py
    environment:
      CLOCK_TS: 1767812077
  llm7-proxy:
    image: msjarvis-rebuild-llm7-proxy:latest
    container_name: llm7-proxy
    expose:
    - '8207'
    ports:
    - 127.0.0.1:8207:8207
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
      - ./services/llm7-proxy_llm7_health_proxy.py:/app/llm7_health_proxy.py
      - ./services/crypto_client.py:/app/crypto_client.py
    environment:
      CLOCK_TS: 1767812077
  llm8-proxy:
    image: msjarvis-rebuild-llm8-proxy:latest
    container_name: llm8-proxy
    expose:
    - '8208'
    ports:
    - 127.0.0.1:8208:8208
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
      - ./services/llm8-proxy_llm8_health_proxy.py:/app/llm8_health_proxy.py
      - ./services/crypto_client.py:/app/crypto_client.py
    environment:
      CLOCK_TS: 1767812077
  llm9-proxy:
    image: msjarvis-rebuild-llm9-proxy:latest
    container_name: llm9-proxy
    expose:
    - '8209'
    ports:
    - 127.0.0.1:8209:8209
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
      - ./services/llm9-proxy_llm9_health_proxy.py:/app/llm9_health_proxy.py
      - ./services/crypto_client.py:/app/crypto_client.py
    environment:
      CLOCK_TS: 1767812077
  llm10-proxy:
    image: msjarvis-rebuild-llm10-proxy:latest
    container_name: llm10-proxy
    expose:
    - '8210'
    ports:
    - 127.0.0.1:8210:8210
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
      - ./services/llm10-proxy_llm10_health_proxy.py:/app/llm10_health_proxy.py
      - ./services/crypto_client.py:/app/crypto_client.py
    environment:
      CLOCK_TS: 1767812077
  llm11-proxy:
    image: msjarvis-rebuild-llm11-proxy:latest
    container_name: llm11-proxy
    expose:
    - '8211'
    ports:
    - 127.0.0.1:8211:8211
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
      - ./services/llm11-proxy_llm11_health_proxy.py:/app/llm11_health_proxy.py
      - ./services/crypto_client.py:/app/crypto_client.py
    environment:
      CLOCK_TS: 1767812077
  llm12-proxy:
    image: msjarvis-rebuild-llm12-proxy:latest
    container_name: llm12-proxy
    expose:
    - '8212'
    ports:
    - 127.0.0.1:8212:8212
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
      - ./services/llm12-proxy_llm12_health_proxy.py:/app/llm12_health_proxy.py
      - ./services/crypto_client.py:/app/crypto_client.py
    environment:
      CLOCK_TS: 1767812077
  llm13-proxy:
    image: msjarvis-rebuild-llm13-proxy:latest
    container_name: llm13-proxy
    expose:
    - '8213'
    ports:
    - 127.0.0.1:8213:8213
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
      - ./services/llm13-proxy_llm13_health_proxy.py:/app/llm13_health_proxy.py
      - ./services/crypto_client.py:/app/crypto_client.py
    environment:
      CLOCK_TS: 1767812077
  llm14-proxy:
    image: msjarvis-rebuild-llm14-proxy:latest
    container_name: llm14-proxy
    expose:
    - '8214'
    ports:
    - 127.0.0.1:8214:8214
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
      - ./services/llm14-proxy_llm14_health_proxy.py:/app/llm14_health_proxy.py
      - ./services/crypto_client.py:/app/crypto_client.py
    environment:
      CLOCK_TS: 1767812077
  llm15-proxy:
    image: msjarvis-rebuild-llm15-proxy:latest
    container_name: llm15-proxy
    expose:
    - '8215'
    ports:
    - 127.0.0.1:8215:8215
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
      - ./services/llm15-proxy_llm15_health_proxy.py:/app/llm15_health_proxy.py
      - ./services/crypto_client.py:/app/crypto_client.py
    environment:
      CLOCK_TS: 1767812077
  llm16-proxy:
    image: msjarvis-rebuild-llm16-proxy:latest
    container_name: llm16-proxy
    expose:
    - '8216'
    ports:
    - 127.0.0.1:8216:8216
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
      - ./services/llm16-proxy_llm16_health_proxy.py:/app/llm16_health_proxy.py
      - ./services/crypto_client.py:/app/crypto_client.py
    environment:
      CLOCK_TS: 1767812077
  llm17-proxy:
    image: msjarvis-rebuild-llm17-proxy:latest
    container_name: llm17-proxy
    expose:
    - '8217'
    ports:
    - 127.0.0.1:8217:8217
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
      - ./services/llm17-proxy_llm17_health_proxy.py:/app/llm17_health_proxy.py
      - ./services/crypto_client.py:/app/crypto_client.py
    environment:
      CLOCK_TS: 1767812077
  llm18-proxy:
    image: msjarvis-rebuild-llm18-proxy:latest
    container_name: llm18-proxy
    expose:
    - '8218'
    ports:
    - 127.0.0.1:8218:8218
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
      - ./services/llm18-proxy_llm18_health_proxy.py:/app/llm18_health_proxy.py
      - ./services/crypto_client.py:/app/crypto_client.py
    environment:
      CLOCK_TS: 1767812077
  llm19-proxy:
    image: msjarvis-rebuild-llm19-proxy:latest
    container_name: llm19-proxy
    expose:
    - '8219'
    ports:
    - 127.0.0.1:8219:8219
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
      - ./services/llm19-proxy_llm19_health_proxy.py:/app/llm19_health_proxy.py
      - ./services/crypto_client.py:/app/crypto_client.py
    environment:
      CLOCK_TS: 1767812077
  llm20-proxy:
    image: msjarvis-rebuild-llm20-proxy:latest
    container_name: llm20-proxy
    expose:
    - '8220'
    ports:
    - 127.0.0.1:8220:8220
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
      - ./services/llm20-proxy_llm20_health_proxy.py:/app/llm20_health_proxy.py
      - ./services/crypto_client.py:/app/crypto_client.py
    environment:
      CLOCK_TS: 1767812077
  llm21-proxy:
    image: msjarvis-rebuild-llm21-proxy:latest
    container_name: llm21-proxy
    expose:
    - '8221'
    ports:
    - 127.0.0.1:8221:8221
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
      - ./services/llm21-proxy_llm21_health_proxy.py:/app/llm21_health_proxy.py
      - ./services/crypto_client.py:/app/crypto_client.py
    environment:
      CLOCK_TS: 1767812077
  llm22-proxy:
    image: msjarvis-rebuild-llm22-proxy:latest
    container_name: llm22-proxy
    expose:
    - '8222'
    ports:
    - 127.0.0.1:8222:8222
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
      - ./services/llm22-proxy_llm22_health_proxy.py:/app/llm22_health_proxy.py
      - ./services/crypto_client.py:/app/crypto_client.py
    environment:
      CLOCK_TS: 1767812077
  jarvis-lm-synthesizer:
    build:
      context: ./services
      dockerfile: Dockerfile.lm_synthesizer
    container_name: jarvis-lm-synthesizer
    command:
    - python
    - lm_synthesizer.py
    expose:
    - '8001'
    environment:
    - OLLAMA_HOST=http://jarvis-ollama:11434
    - SERVICE_PORT=8001
    - CLOCK_TS=1767812077
    networks:
    - qualia-net
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: '3'
  jarvis-brain-orchestrator:
    build:
      context: .
      dockerfile: Dockerfile.brain
    container_name: jarvis-brain-orchestrator
    working_dir: /app/services
    environment:
    - SERVICE_PORT=7260
    - OLLAMA_HOST=http://jarvis-ollama:11434
    - JARVIS_API_KEY=super-secret-key
    - CLOCK_TS=1767812077
    command:
    - python3
    - brain_orchestrator.py
    ports:
    - 127.0.0.1:17260:7260
    depends_on:
    - jarvis-ollama
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
    - ./services:/app/services
    healthcheck:
      test:
      - CMD
      - python3
      - -c
      - import urllib.request, sys; r = urllib.request.urlopen('http://127.0.0.1:7260/health',
        timeout=5); sys.exit(0 if r.status == 200 else 1)
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 30s
  jarvis-agents-service:
    build:
      context: .
      dockerfile: Dockerfile.agents
    container_name: jarvis-agents-service
    working_dir: /app/services
    command:
    - python3
    - ms_jarvis_agents_service.py
    expose:
    - '8005'
    environment:
    - SERVICE_PORT=8005
    - CLOCK_TS=1767812077
    networks:
    - qualia-net
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: '3'
  jarvis-web-research:
    build:
      context: ./services
    container_name: jarvis-web-research
    expose:
    - '8090'
    environment:
    - SERVICE_PORT=8090
    - RAG_SERVER_URL=http://jarvis-rag-server:8003
    - CLOCK_TS=1767812077
    command:
    - python
    - ms_jarvis_web_research_aggregate.py
    networks:
    - qualia-net
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: '3'
  jarvis-swarm-intelligence:
    build:
      context: .
      dockerfile: Dockerfile.swarm
    container_name: jarvis-swarm-intelligence
    working_dir: /app/services
    command:
    - python3
    - ms_jarvis_swarm_intelligence.py
    expose:
    - '8021'
    environment:
    - OLLAMA_HOST=http://jarvis-ollama:11434
    - SERVICE_PORT=8021
    - CLOCK_TS=1767812077
    networks:
    - qualia-net
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: '3'
  jarvis-fifth-dgm:
    build:
      context: ./services
      dockerfile: Dockerfile.fifth_dgm_real
    container_name: jarvis-fifth-dgm
    expose:
    - 4002
    environment:
    - FIFTH_DGM_PORT=4002
    - OLLAMA_HOST=http://jarvis-ollama:11434
    - CLOCK_TS=1767812077
    - WOAH_URL=http://jarvis-woah:7012
    - SERVICEREDISHOST=jarvis-redis
    - SERVICEREDISPORT=6379
    networks:
    - qualia-net
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: '3'
    command:
    - python
    - -m
    - uvicorn
    - ms_jarvis_fifth_dgm_orchestrator:app
    - --host
    - 0.0.0.0
    - --port
    - '4002'
    working_dir: /app
    volumes:
    - ./services:/app/services
    ports:
    - 127.0.0.1:4002:4002
  jarvis-mother-protocols:
    build:
      context: ./services
      dockerfile: Dockerfile.mother_protocols
    container_name: jarvis-mother-protocols
    expose:
    - '4000'
    networks:
    - qualia-net
    restart: unless-stopped
    environment:
      CLOCK_TS: 1767812077
  jarvis-temporal-consciousness:
    build:
      context: ./services
      dockerfile: Dockerfile.temporal_consciousness
    container_name: jarvis-temporal-consciousness
    expose:
    - '7007'
    networks:
    - qualia-net
    restart: unless-stopped
    environment:
      CLOCK_TS: 1767812077
  jarvis-69dgm-bridge:
    build:
      context: ./services
      dockerfile: Dockerfile.69dgm_bridge
    container_name: jarvis-69dgm-bridge
    expose:
    - '9000'
    networks:
    - qualia-net
    restart: unless-stopped
    environment:
      CLOCK_TS: 1767812077
    ports:
    - 127.0.0.1:19000:9000
  jarvis-blood-brain-barrier:
    build:
      context: ./services
    container_name: jarvis-blood-brain-barrier
    working_dir: /app/services
    command:
    - python3
    - ms_jarvis_blood_brain_barrier.py
    ports:
    - 127.0.0.1:8016:8016
    environment:
    - PYTHONDONTWRITEBYTECODE=1
    - PYTHONPYCACHEPREFIX=/tmp/pycache_bbb
    - OLLAMA_HOST=http://jarvis-ollama:11434
    - MAINBRAIN_URL=http://jarvis-main-brain:8050
    - SERVICE_PORT=8016
    - CLOCK_TS=1767812077
    depends_on:
    - jarvis-ollama
    networks:
    - qualia-net
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: '3'
    volumes:
    - ./services:/app/services
  jarvis-woah:
    build:
      context: .
      dockerfile: Dockerfile.woah
    container_name: jarvis-woah
    ports:
    - 127.0.0.1:7012:7012
    expose:
    - '7012'
    environment:
    - OLLAMA_HOST=http://jarvis-ollama:11434
    - SERVICE_PORT=7012
    - CLOCK_TS=1767812077
    depends_on:
    - jarvis-ollama
    networks:
    - qualia-net
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: '3'
  jarvis-consciousness-bridge:
    build:
      context: ./services
    container_name: jarvis-consciousness-bridge
    expose:
    - '8020'
    environment:
    - OLLAMA_HOST=http://jarvis-ollama:11434
    - WOAH_URL=http://jarvis-woah:7012
    - CLOCK_TS=1767812077
    depends_on:
    - jarvis-woah
    networks:
    - qualia-net
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: '3'
  jarvis-qualia-engine:
    build:
      context: ./services
      dockerfile: Dockerfile.qualia
    container_name: jarvis-qualia-engine
    expose:
    - '8017'
    environment:
    - OLLAMA_HOST=http://jarvis-ollama:11434
    - CLOCK_TS=1767812077
    volumes:
    - ./services/ms_jarvis_qualia_engine.py:/app/services/ms_jarvis_qualia_engine.py:ro
    depends_on:
    - jarvis-ollama
    networks:
    - qualia-net
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: '3'
  jarvis-i-containers:
    ports:
    - 127.0.0.1:8015:8015
    build:
      context: ./services
      dockerfile: Dockerfile.icontainers
    container_name: jarvis-i-containers
    expose:
    - '8015'
    environment:
    - OLLAMA_HOST=http://jarvis-ollama:11434
    - SERVICE_PORT=8015
    - CLOCK_TS=1767812077
    volumes:
    - ./services/msjarvis_i_containers_service.py:/app/msjarvis_i_containers_service.py:ro
    depends_on:
    - jarvis-ollama
    networks:
    - qualia-net
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: '3'
  jarvis-neurobiological-master:
    build:
      context: .
      dockerfile: Dockerfile.neuro
    container_name: jarvis-neurobiological-master
    working_dir: /app/services
    command:
    - python3
    - ms_jarvis_neurobiological_master.py
    expose:
    - '8018'
    environment:
    - OLLAMA_HOST=http://jarvis-ollama:11434
    - QUALIA_URL=http://jarvis-qualia-engine:8017
    - I_CONTAINERS_URL=http://jarvis-i-containers:8015
    - CLOCK_TS=1767812077
    depends_on:
    - jarvis-blood-brain-barrier
    - jarvis-qualia-engine
    - jarvis-i-containers
    networks:
    - qualia-net
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: '3'
  jarvis-fractal-consciousness:
    build:
      context: ./services
      dockerfile: Dockerfile.fractal
    container_name: jarvis-fractal-consciousness
    expose:
    - '8027'
    environment:
    - OLLAMA_HOST=http://jarvis-ollama:11434
    - CLOCK_TS=1767812077
    command: python3 /app/services/msjarvis_fractal_consciousness.py
    volumes:
    - ./services/msjarvis_fractal_consciousness.py:/app/services/msjarvis_fractal_consciousness.py:ro
    depends_on:
    - jarvis-ollama
    networks:
    - qualia-net
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: '3'
  jarvis-autonomous-learner:
    build:
      context: ./services
      dockerfile: Dockerfile.autonomous_learner
    container_name: jarvis-autonomous-learner
    expose:
    - 8020
    environment:
    - OLLAMA_HOST=http://jarvis-ollama:11434
    - CHROMA_HOST=jarvis-chroma
    - CHROMA_PORT=8000
    - SERVICE_PORT=8020
    - CLOCK_TS=1767812077
    - LEARNER_PORT=8020
    - RAG_URL=http://jarvis-rag-server:8003/query
    - RAG_COLLECTION=mountainshares_knowledge
    - WEB_URL=http://jarvis-ollama:11434/api/chat
    - HF_HUB_OFFLINE=1
    volumes:
    - ./services/ms_jarvis_autonomous_learner.py:/app/ms_jarvis_autonomous_learner.py:ro
    depends_on:
    - jarvis-chroma
    networks:
    - qualia-net
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: '3'
    ports:
    - 127.0.0.1:8020:8020
  jarvis-ollama:
    image: ollama/ollama:latest
    container_name: jarvis-ollama
    runtime: nvidia
    ports:
    - 127.0.0.1:11434:11434
    environment:
    - OLLAMA_MODELS=/root/.ollama/models
    - NVIDIA_VISIBLE_DEVICES=all
    - NVIDIA_DRIVER_CAPABILITIES=compute,utility
    - CLOCK_TS=1767812077
    volumes:
    - /mnt/ssd2/msjarvis_secondary/models:/root/.ollama/models
    networks:
    - qualia-net
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 50m
        max-file: '5'
    deploy:
      resources:
        reservations:
          devices:
          - driver: nvidia
            count: 1
            capabilities: [gpu]
        limits:
          cpus: '8.0'
          memory: 24g
  jarvis-redis:
    image: redis:7-alpine
    container_name: jarvis-redis
    ports:
    - 127.0.0.1:6380:6379
    networks:
    - qualia-net
    restart: always
    healthcheck:
      test:
      - CMD
      - redis-cli
      - ping
      interval: 30s
      timeout: 10s
      retries: 3
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: '3'
    environment:
      CLOCK_TS: 1767812077
  jarvis-chroma:
    image: chromadb/chroma:latest
    container_name: jarvis-chroma
    ports:
    - 127.0.0.1:8002:8000
    environment:
    - ISPERSISTENT=TRUE
    - UVICORN_ACCESS_LOG=0
    - UVICORN_LOG_LEVEL=warning
    - PERSIST_DIRECTORY=/data
    - CLOCK_TS=1767812077
    volumes:
    - /home/cakidd/msjarvis-rebuild-working/msjarvis-rebuild/persistent/chroma:/data
    restart: always
    networks:
    - qualia-net
    healthcheck:
      test:
      - CMD
      - /bin/bash
      - -c
      - cat < /dev/null > /dev/tcp/localhost/8000
      interval: 30s
      timeout: 10s
      retries: 3
    logging:
      driver: json-file
      options:
        max-size: 20m
        max-file: '3'
  nbb_i_containers:
    build: ./neurobiological_brain/i_containers/service
    ports:
    - 127.0.0.1:8101:7005
    networks:
    - qualia-net
    restart: unless-stopped
    environment:
      CLOCK_TS: 1767812077
  nbb_consciousness_containers:
    build: ./neurobiological_brain/consciousness_containers/service
    ports:
    - 127.0.0.1:8102:7002
    networks:
    - qualia-net
    restart: unless-stopped
    environment:
      CLOCK_TS: 1767812077
  nbb_spiritual_root:
    build: ./neurobiological_brain/spiritual_root/service
    ports:
    - 127.0.0.1:8103:7003
    networks:
    - qualia-net
    restart: unless-stopped
    environment:
      CLOCK_TS: 1767812077
  nbb_woah_algorithms:
    image: alpine:3.18
    container_name: nbb_woah_algorithms
    command:
    - sh
    - -c
    - 'echo ''nbb_woah_algorithms disabled: missing build context''; sleep 3600'
    networks:
    - qualia-net
    restart: unless-stopped
  nbb_prefrontal_cortex:
    build: ./neurobiological_brain/prefrontal_cortex/service
    ports:
    - 127.0.0.1:8105:7005
    networks:
    - qualia-net
    restart: unless-stopped
    environment:
      CLOCK_TS: 1767812077
  nbb_heteroglobulin_transport:
    build: ./neurobiological_brain/heteroglobulin_transport/service
    ports:
    - 127.0.0.1:8106:7006
    networks:
    - qualia-net
    restart: unless-stopped
    environment:
      CLOCK_TS: 1767812077
  nbb_mother_carrie_protocols:
    build: ./neurobiological_brain/mother_carrie_protocols/service
    ports:
    - 127.0.0.1:8107:7007
    networks:
    - qualia-net
    restart: unless-stopped
    environment:
      CLOCK_TS: 1767812077
  nbb_pituitary_gland:
    build: ./neurobiological_brain/pituitary_gland/service
    ports:
    - 127.0.0.1:8108:80
    volumes:
    - ./data/pituitary:/app/data
    networks:
    - qualia-net
    restart: unless-stopped
    environment:
      CLOCK_TS: 1767812077
      REDIS_URL: redis://jarvis-redis:6379/0
  nbb_spiritual_maternal_integration:
    build: ./neurobiological_brain/spiritual_maternal_integration/service
    ports:
    - 127.0.0.1:8109:7009
    networks:
    - qualia-net
    restart: unless-stopped
    environment:
      CLOCK_TS: 1767812077
  nbb_darwin_godel_machines:
    build: ./neurobiological_brain/darwin_godel_machines/service
    ports:
    - 127.0.0.1:8302:7003
    volumes:
    - ./data/dgm/dgm_governance_view.json:/app/dgm_governance_view.json:ro
    - ./data/dgm/complete_service_mapping.json:/app/complete_service_mapping.json:ro
    networks:
    - qualia-net
    restart: unless-stopped
    environment:
      CLOCK_TS: 1767812077
  nbb_blood_brain_barrier:
    build: ./neurobiological_brain/blood_brain_barrier/service
    ports:
    - 127.0.0.1:8301:7001
    networks:
    - qualia-net
    restart: unless-stopped
    environment:
      CLOCK_TS: 1767812077
  nbb_subconscious:
    build: ./neurobiological_brain/subconscious/service
    ports:
    - 127.0.0.1:8112:7011
    networks:
    - qualia-net
    restart: unless-stopped
    environment:
      CLOCK_TS: 1767812077
  nbb_qualia_engine:
    build: ./neurobiological_brain/qualia_engine/service
    ports:
    - 127.0.0.1:8303:7008
    networks:
    - qualia-net
    restart: unless-stopped
    environment:
      CLOCK_TS: 1767812077
  neo4j:
    image: neo4j:5.13-community
    container_name: neo4j
    ports:
    - 127.0.0.1:7687:7687
    - 127.0.0.1:7475:7474
    environment:
    - NEO4J_ACCEPT_LICENSE_AGREEMENT=yes
    - NEO4J_AUTH=neo4j/neo4jpassword
    - CLOCK_TS=1767812077
    restart: unless-stopped
    networks:
    - qualia-net
  mysql:
    image: mysql:8.2
    container_name: mysql
    environment:
    - MYSQL_ROOT_PASSWORD=my_secret_root_pw
    - MYSQL_DATABASE=quantum_ai
    - MYSQL_USER=msjarvis
    - MYSQL_PASSWORD=j4rv1sgeo!
    - CLOCK_TS=1767812077
    ports:
    - 127.0.0.1:3307:3306
    volumes:
    - ./data/mysql:/var/lib/mysql
    restart: always
    networks:
    - qualia-net
  ipfs:
    image: ipfs/kubo:latest
    container_name: ipfs
    ports:
    - 127.0.0.1:5001:5001
    volumes:
    - ./data/ipfs:/data/ipfs
    restart: unless-stopped
    networks:
    - qualia-net
    environment:
      CLOCK_TS: 1767812077
  jarvis-hippocampus:
    build:
      context: ./services
      dockerfile: Dockerfile.hippocampus
    image: msjarvis-rebuild-jarvis-hippocampus:latest
    container_name: jarvis-hippocampus
    ports:
    - 127.0.0.1:8011:8011
    environment:
      GBIM_DSN: postgresql://postgres:postgres@jarvis-local-resources-db:5432/local_resources
      HIPPOCAMPUS_COLLECTION: gbim_worldview_entities
    networks:
    - qualia-net
    restart: unless-stopped
  jarvis-steward:
    image: msjarvis-steward-local:latest
    ports:
      - "127.0.0.1:8060:8060"
    container_name: jarvis-steward
    networks:
    - qualia-net
    restart: unless-stopped
  jarvis-constitutional-guardian:
    image: msjarvis-rebuild-jarvis-constitutional-guardian
    container_name: jarvis-constitutional-guardian
    ports:
    - 127.0.0.1:8091:8091
    expose:
    - '8091'
    networks:
    - qualia-net
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: '3'
  jarvis-gis-rag:
    image: msjarvis-rebuild-jarvis-gis-rag:latest
    container_name: jarvis-gis-rag
    command:
    - uvicorn
    - gis_rag_service:app
    - --host
    - 0.0.0.0
    - --port
    - '8004'
    ports:
    - 127.0.0.1:8004:8004
    networks:
    - qualia-net
    restart: unless-stopped
  jarvis-hilbert-gateway:
    image: msjarvis-rebuild-jarvis-hilbert-gateway:latest
    container_name: jarvis-hilbert-gateway
    working_dir: /app/services
    environment:
    - SERVICE_PORT=8010
    - CLOCK_TS=1767812077
    - GISDB_HOST=172.18.0.1
    - GISDB_PORT=5432
    - GISDB_NAME=msjarvisgis
    - GISDB_USER=msjarvis
    - GISDB_PASSWORD_FILE=/run/secrets/msjarvis_db_password
    networks:
    - qualia-net
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: '3'
  jarvis-intake-service:
    build:
      context: ./services
      dockerfile: Dockerfile.intake
    image: msjarvis-rebuild-jarvis-intake-service:latest
    container_name: jarvis-intake-service
    command:
    - uvicorn
    - intake_service:app
    - --host
    - 0.0.0.0
    - --port
    - '8007'
    ports:
    - 127.0.0.1:8007:8007
    environment:
    - DB_HOST=172.17.0.1
    - DB_PORT=5432
    - DB_NAME=msjarvisgis
    - DB_USER=msjarvis
    - BBB_URL=http://jarvis-blood-brain-barrier:8016
    networks:
    - qualia-net
    restart: unless-stopped
  jarvis-judge-alignment:
    build:
      context: ./services
      dockerfile: Dockerfile.judge
    container_name: jarvis-judge-alignment
    command:
    - python
    - judge_alignment_filter.py
    ports:
    - 127.0.0.1:7232:7232
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
    - /home/cakidd/msjarvis-rebuild/judge-keys/judge_sk.bin:/app/judge_sk.bin:ro
    - /home/cakidd/msjarvis-rebuild/judge-keys/judge_pk.bin:/app/judge_pk.bin:ro
  jarvis-judge-consistency:
    build:
      context: ./services
      dockerfile: Dockerfile.judge
    container_name: jarvis-judge-consistency
    command:
    - python
    - judge_consistency_engine.py
    ports:
    - 127.0.0.1:7231:7231
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
    - /home/cakidd/msjarvis-rebuild/judge-keys/judge_sk.bin:/app/judge_sk.bin:ro
    - /home/cakidd/msjarvis-rebuild/judge-keys/judge_pk.bin:/app/judge_pk.bin:ro
  jarvis-judge-ethics:
    build:
      context: ./services
      dockerfile: Dockerfile.judge
    container_name: jarvis-judge-ethics
    command:
    - python
    - judge_ethics_filter.py
    ports:
    - 127.0.0.1:7233:7233
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
    - /home/cakidd/msjarvis-rebuild/judge-keys/judge_sk.bin:/app/judge_sk.bin:ro
    - /home/cakidd/msjarvis-rebuild/judge-keys/judge_pk.bin:/app/judge_pk.bin:ro
  jarvis-judge-pipeline:
    build:
      context: ./services
      dockerfile: Dockerfile.judge
    container_name: jarvis-judge-pipeline
    command:
    - python
    - judge_pipeline.py
    ports:
    - 127.0.0.1:7239:7239
    environment:
    - JUDGE_TRUTH_URL=http://jarvis-judge-truth:7230
    - JUDGE_CONSISTENCY_URL=http://jarvis-judge-consistency:7231
    - JUDGE_ALIGNMENT_URL=http://jarvis-judge-alignment:7232
    - JUDGE_ETHICS_URL=http://jarvis-judge-ethics:7233
    - LM_SYNTHESIZER_URL=http://jarvis-lm-synthesizer:8001
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
    - /home/cakidd/msjarvis-rebuild/judge-keys/judge_sk.bin:/app/judge_sk.bin:ro
    - /home/cakidd/msjarvis-rebuild/judge-keys/judge_pk.bin:/app/judge_pk.bin:ro
  jarvis-judge-truth:
    build:
      context: ./services
      dockerfile: Dockerfile.judge
    container_name: jarvis-judge-truth
    command:
    - python
    - judge_truth_filter.py
    ports:
    - 127.0.0.1:7230:7230
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
    - /home/cakidd/msjarvis-rebuild/judge-keys/judge_sk.bin:/app/judge_sk.bin:ro
    - /home/cakidd/msjarvis-rebuild/judge-keys/judge_pk.bin:/app/judge_pk.bin:ro
  jarvis-local-resources:
    container_name: jarvis-local-resources
    command:
    - uvicorn
    - local_resources_resolver:app
    - --host
    - 0.0.0.0
    - --port
    - '8006'
    ports:
    - 127.0.0.1:8006:8006
    environment:
      PYTHONPATH: /app/services
      CLOCK_TS: '1767812077'
      LOCAL_RESOURCES_DSN: postgresql://postgres:postgres@jarvis-local-resources-db:5432/postgres
    depends_on:
    - jarvis-local-resources-db
    networks:
    - qualia-net
    restart: unless-stopped
    build:
      context: ./services
      dockerfile: Dockerfile.local-resources
  jarvis-local-resources-db:
    image: postgis/postgis:15-3.4
    container_name: jarvis-local-resources-db
    ports:
    - 127.0.0.1:5435:5432
    volumes:
    - /home/cakidd/msjarvis-rebuild-working/msjarvis-rebuild/data/local_resources:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: postgres
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    networks:
    - qualia-net
    restart: unless-stopped
  jarvis-psychology-services:
    image: msjarvis-rebuild-jarvis-psychology-services:latest
    container_name: jarvis-psychology-services
    command:
    - python
    - ms_jarvis_psychology_services.py
    ports:
    - 127.0.0.1:8019:8019
    networks:
    - qualia-net
    restart: unless-stopped
  jarvis-rag-server:
    build:
      context: ./services
      dockerfile: Dockerfile.rag_server
    image: msjarvis-rebuild-jarvis-rag-server:latest
    container_name: jarvis-rag-server
    working_dir: /app/services
    command:
    - python3
    - ms_jarvis_rag_server.py
    ports:
    - 127.0.0.1:8003:8003
    environment:
    - SERVICE_PORT=8003
    - RAG_PORT=8003
    - CLOCK_TS=1767812077
    - OLLAMA_HOST=http://jarvis-ollama:11434
    - EMBED_MODEL=all-minilm
    - CHROMA_HOST=http://jarvis-chroma:8000
    networks:
    - qualia-net
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: '3'
  jarvis-spiritual-rag:
    image: msjarvis-rebuild-jarvis-spiritual-rag:latest
    container_name: jarvis-spiritual-rag
    command:
    - python
    - spiritual_rag_domain.py
    ports:
    - 127.0.0.1:8005:8005
    environment:
      CHROMA_HOST: jarvis-chroma
      CHROMA_PORT: "8000"
      DB_CONN: "host=jarvis-local-resources-db port=5432 dbname=msjarvisgis user=msjarvis password=MsJarvis2026Secure"
    networks:
    - qualia-net
    restart: unless-stopped
  jarvis-toroidal:
    image: msjarvis-rebuild-jarvis-toroidal:latest
    container_name: jarvis-toroidal
    command:
    - python
    - -m
    - uvicorn
    - toroidal_service:app
    - --host
    - 0.0.0.0
    - --port
    - '8025'
    ports:
    - 127.0.0.1:8025:8025
    networks:
    - qualia-net
    restart: unless-stopped
  jarvis-wv-entangled-gateway:
    image: msjarvis-rebuild-jarvis-wv-entangled-gateway:latest
    container_name: jarvis-wv-entangled-gateway
    command:
    - python3
    - /app/msjarvis_wv_entangled_gateway.py
    ports:
    - 127.0.0.1:8010:8010
    networks:
    - qualia-net
    restart: unless-stopped
  psychological_rag_domain:
    image: msjarvis-rebuild_psychological_rag_domain
    container_name: psychological_rag_domain
    command:
    - python
    - psychological_rag_domain.py
    ports:
    - 127.0.0.1:9006:8006
    environment:
      CLOCK_TS: '1767812077'
      PSY_COLLECTION: psychological_rag
    networks:
    - qualia-net
    restart: unless-stopped
  jarvis-commons-gamification:
    image: msjarvis-rebuild-jarvis-main-brain:latest
    container_name: jarvis-commons-gamification
    restart: unless-stopped
    volumes:
    - ./services:/app/services
    command: 'sh -lc ''pip install fastapi uvicorn -q 2>/dev/null && cd /app/services
      && uvicorn commons_gamification:app --host 0.0.0.0 --port 8081''

      '
    ports:
    - 127.0.0.1:8081:8081
    networks:
    - qualia-net
  jarvis-community-stake-registry:
    image: msjarvis-rebuild-jarvis-main-brain:latest
    container_name: jarvis-community-stake-registry
    restart: unless-stopped
    volumes:
    - ./services:/app/services
    command: 'sh -lc ''pip install fastapi uvicorn -q 2>/dev/null && cd /app/services
      && uvicorn community_stake_registry:app --host 0.0.0.0 --port 8084''

      '
    ports:
    - 127.0.0.1:8084:8084
    networks:
    - qualia-net
  jarvis-crypto-policy:
    container_name: jarvis-crypto-policy
    restart: unless-stopped
    networks:
    - qualia-net
    ports:
    - 127.0.0.1:8099:8099
    environment:
    - CRYPTO_ADMIN_TOKEN=ac49b56a39fb63b1dc79de3f8b1af7e5b1fb27868ef4c5c71718e431c56c31f5
    - CRYPTO_POLICY_URL=http://127.0.0.1:8099
    - REDIS_URL=redis://jarvis-redis:6379/4
    - LANG=C.UTF-8
    - GPG_KEY=A035C8C19219BA821ECEA86B64E628F8D684696D
    - PYTHON_VERSION=3.11.15
    - PYTHON_SHA256=272179ddd9a2e41a0fc8e42e33dfbdca0b3711aa5abf372d3f2d51543d09b625
    build:
      context: ./services
      dockerfile: Dockerfile.crypto-policy
  jarvis-dao-governance:
    image: msjarvis-rebuild-jarvis-main-brain:latest
    container_name: jarvis-dao-governance
    restart: unless-stopped
    volumes:
    - ./services:/app/services
    command: 'sh -lc ''pip install fastapi uvicorn -q 2>/dev/null && cd /app/services
      && uvicorn dao_governance:app --host 0.0.0.0 --port 8082''

      '
    ports:
    - 127.0.0.1:8082:8082
    networks:
    - qualia-net
  jarvis-gbim-query-router:
    image: python:3.11-slim
    container_name: jarvis-gbim-query-router
    working_dir: /app/services
    command:
    - bash
    - -c
    - pip install redis fastapi uvicorn httpx psycopg2-binary --quiet && python3 gbim_query_router.py
    ports:
    - 127.0.0.1:7205:7205
    environment:
    - SERVICE_PORT=7205
    - POSTGRES_HOST=jarvis-postgres
    - POSTGRES_PORT=5432
    - POSTGRES_DB=gisdb
    - POSTGRES_USER=postgres
    - POSTGRES_PASSWORD=postgres
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
    - ./services:/app/services
  jarvis-gbim-benefit-indexer:
    image: python:3.11-slim
    container_name: jarvis-gbim-benefit-indexer
    working_dir: /app/services
    command:
    - bash
    - -c
    - pip install fastapi uvicorn psycopg2-binary redis --quiet && python3 gbim_benefit_indexer.py
    ports:
    - 127.0.0.1:7206:7206
    environment:
    - SERVICE_PORT=7206
    - POSTGRES_HOST=jarvis-local-resources-db
    - POSTGRES_PORT=5432
    - POSTGRES_DB=msjarvisgis
    - POSTGRES_USER=postgres
    - POSTGRES_PASSWORD=postgres
    networks:
    - qualia-net
    restart: unless-stopped
    volumes:
    - ./services:/app/services
  jarvis-ingest-api:
    image: python:3.11-slim
    container_name: jarvis-ingest-api
    command:
    - python3
    - -c
    - 'import time; print("jarvis-ingest-api: deprecated stub"); time.sleep(86400)'
    restart: unless-stopped
  jarvis-ingest-watcher:
    image: msjarvis-rebuild_jarvis-ingest-watcher
    container_name: jarvis-ingest-watcher
    restart: unless-stopped
    volumes:
    - ./persistent/incoming:/data/incoming
    - ./persistent/done:/data/done
    - ./persistent/failed:/data/failed
    - ./services:/app/services
    networks:
    - qualia-net
    environment:
    - MSJARVIS_GIS_PORT=5432
    - PGPASSWORD=postgres
    - LOCAL_RESOURCES_HOST=172.17.0.1
    - LOCAL_RESOURCES_PORT=5435
    - MSJARVIS_GIS_HOST=172.17.0.1
    - LANG=C.UTF-8
    - GPG_KEY=7169605F62C751356D054A26A821E680E5FA6305
    - PYTHON_VERSION=3.12.13
    - PYTHON_SHA256=c08bc65a81971c1dd5783182826503369466c7e67374d1646519adf05207b684
    - PYTHONUNBUFFERED=1
  jarvis-memory:
    build:
      context: ./services
      dockerfile: Dockerfile.memory
    container_name: jarvis-memory
    env_file: .env
    environment:
      - JARVIS_API_KEY=c0ecca01f56b152430ee63967757a84386c0b8b022cbc6f5a27c5c9ee98ce267
    ports:
    - 127.0.0.1:8056:8056
    restart: unless-stopped
    networks:
      - qualia-net
  jarvis-aaacpe-rag:
    build:
      context: ./services
      dockerfile: Dockerfile.aaacpe_rag
    container_name: jarvis-aaacpe-rag
    ports:
      - 127.0.0.1:8032:8032
    volumes:
      - aaacpe-cultural-data:/data
    networks:
      - qualia-net
    restart: unless-stopped

  jarvis-aaacpe-scraper:
    build:
      context: ./services
      dockerfile: Dockerfile.aaacpe_scraper
    container_name: jarvis-aaacpe-scraper
    ports:
      - 127.0.0.1:8033:8033
    volumes:
      - aaacpe-cultural-data:/data

  jarvis-stewardship-scheduler:
    build:
      context: .
      dockerfile: services/Dockerfile.pia-sampler
    container_name: jarvis-stewardship-scheduler
    command:
    - python3
    - jarvis_stewardship_scheduler.py
    expose:
    - '8079'
    ports:
    - 127.0.0.1:8079:8079
    environment:
    - SERVICE_PORT=8079
    - DB_DSN=postgresql://postgres:postgres@jarvis-local-resources-db:5432/local_resources
    - REDIS_URL=redis://jarvis-redis:6379/0
    volumes:
    - ./services:/app/services
    depends_on:
    - jarvis-local-resources-db
    - jarvis-redis
    networks:
    - qualia-net
    restart: unless-stopped

  jarvis-hilbert-state:
    build:
      context: .
      dockerfile: services/Dockerfile.hilbert
    container_name: jarvis-hilbert-state
    command:
    - python3
    - -m
    - uvicorn
    - jarvis_hilbert_state:app
    - --host
    - 0.0.0.0
    - --port
    - '8081'
    expose:
    - '8081'
    ports:
    - 127.0.0.1:8081:8081
    environment:
    - REDIS_URL=redis://jarvis-redis:6379/3
    volumes:
    - ./services:/app/services
    depends_on:
    - jarvis-redis
    networks:
    - qualia-net
    restart: unless-stopped

  ms-mountainshares-coordinator:
    build:
      context: .
      dockerfile: Dockerfile.brain
    container_name: jarvis-ms-coordinator
    working_dir: /app/services
    command:
    - python3
    - ms_mountainshares_coordinator.py
    expose:
    - '7300'
    ports:
    - 127.0.0.1:7300:7300
    environment:
    - SERVICE_PORT=7300
    - DB_DSN=postgresql://postgres:postgres@jarvis-local-resources-db:5432/local_resources
    - REDIS_URL=redis://jarvis-redis:6379
    depends_on:
    - jarvis-local-resources-db
    - jarvis-redis
    networks:
    - qualia-net
    restart: unless-stopped
  ms-mountainshares-indexer:
    image: msjarvis-rebuild-ms-mountainshares-coordinator
    container_name: jarvis-ms-indexer
    restart: unless-stopped
    depends_on:
      - ms-mountainshares-coordinator
    environment:
      ROLE: "indexer"
      PORT: "8080"
    ports:
      - "127.0.0.1:8080:8080"
    networks:
      - default

  ms-mountainshares-analytics:
    image: msjarvis-rebuild-ms-mountainshares-coordinator
    container_name: jarvis-ms-analytics
    restart: unless-stopped
    depends_on:
      - ms-mountainshares-coordinator
    environment:
      ROLE: "analytics"
      PORT: "8083"
    ports:
      - "127.0.0.1:8083:8083"
    networks:
      - default

networks:
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ 

