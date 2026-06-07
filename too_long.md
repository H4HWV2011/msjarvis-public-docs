crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild$ # What frontend-related containers/services already exist?
docker ps --format '{{.Names}}\t{{.Ports}}' | grep -iv "llm\|chroma\|nbb\|jarvis-[0-9]\|ollama\|redis\|postgres"
jarvis-swarm-intelligence	8021/tcp
jarvis-neurobiological-master	8018/tcp
jarvis-agents-service	8005/tcp
jarvis-unified-gateway	127.0.0.1:8001->8001/tcp
jarvis-toroidal	127.0.0.1:8025->8025/tcp
jarvis-woah	127.0.0.1:7012->7012/tcp
jarvis-constitutional-guardian	127.0.0.1:8091->8091/tcp
jarvis-fifth-dgm	127.0.0.1:4002->4002/tcp
jarvis-i-containers	8015/tcp
jarvis-psychology-services	127.0.0.1:8019->8019/tcp
jarvis-lm-synthesizer	8001/tcp
jarvis-main-brain	127.0.0.1:8050->8050/tcp
jarvis-hilbert-state	127.0.0.1:8081->8081/tcp
jarvis-qualia-engine	8017/tcp
jarvis-eeg-delta	127.0.0.1:8073->8073/tcp
jarvis-eeg-theta	127.0.0.1:8074->8074/tcp
jarvis-autonomous-learner	8003/tcp, 127.0.0.1:8425->8425/tcp
jarvis-rag-server	127.0.0.1:8003->8003/tcp
jarvis-blood-brain-barrier	127.0.0.1:8016->8016/tcp
jarvis-dgm-bridge-23	10023/tcp
jarvis-dgm-bridge-22	10022/tcp
jarvis-dgm-bridge-21	10021/tcp
jarvis-dgm-bridge-19	10019/tcp
jarvis-dgm-bridge-18	10018/tcp
jarvis-dgm-bridge-17	10017/tcp
jarvis-dgm-bridge-16	10016/tcp
jarvis-dgm-bridge-13	10013/tcp
jarvis-dgm-bridge-12	10012/tcp
jarvis-dgm-bridge-11	10011/tcp
jarvis-dgm-bridge-09	10009/tcp
jarvis-dgm-bridge-08	10008/tcp
jarvis-dgm-bridge-07	10007/tcp
jarvis-dgm-bridge-05	10005/tcp
jarvis-dgm-bridge-04	10004/tcp
jarvis-dgm-bridge-03	10003/tcp
jarvis-dgm-bridge-02	10002/tcp
jarvis-dgm-bridge-01	10001/tcp
jarvis-dgm-bridge-06	10006/tcp
jarvis-dgm-bridge-10	10010/tcp
jarvis-dgm-bridge-20	10020/tcp
jarvis-fractal-consciousness	8002/tcp, 127.0.0.1:8027->8008/tcp
jarvis-local-resources	127.0.0.1:8006->8006/tcp, 8035/tcp
jarvis-judge-pipeline	127.0.0.1:7239->7239/tcp
jarvis-hippocampus	127.0.0.1:8011->8011/tcp
jarvis-gis-rag	127.0.0.1:8004->8004/tcp, 8044/tcp
jarvis-wv-entangled-gateway	127.0.0.1:8010->8010/tcp
jarvis-consciousness-bridge	127.0.0.1:8020->8018/tcp
jarvis-brain-orchestrator	127.0.0.1:17260->7260/tcp
jarvis-spiritual-rag	127.0.0.1:8005->8005/tcp
jarvis-rag-router	8003/tcp, 127.0.0.1:5012->5001/tcp
a273a1b67360_jarvis-aaacpe-rag	127.0.0.1:8032->8032/tcp
1f9572f759ac_jarvis-auth-api	127.0.0.1:8096->8091/tcp
36ed251382b5_ipfs	4001/tcp, 8080-8081/tcp, 4001/udp, 127.0.0.1:5002->5001/tcp
jarvis-contracts	
jarvis-phi-probe	127.0.0.1:8026->8025/tcp
jarvis-web-research	8008/tcp
jarvis-dgm-bridge-14	10014/tcp
jarvis-dgm-bridge-15	10015/tcp
jarvis-eeg-beta	127.0.0.1:8075->8075/tcp
jarvis-local-resources-db	127.0.0.1:5435->5432/tcp
jarvis-judge-ethics	127.0.0.1:7233->7233/tcp
jarvis-judge-truth	127.0.0.1:7230->7230/tcp
jarvis-judge-consistency	127.0.0.1:7231->7231/tcp
mysql	33060/tcp, 127.0.0.1:3307->3306/tcp
jarvis-judge-alignment	127.0.0.1:7232->7232/tcp
neo4j	7473/tcp, 127.0.0.1:7687->7687/tcp, 127.0.0.1:7475->7474/tcp
jarvis-mother-protocols	4000/tcp
jarvis-semaphore	127.0.0.1:8030->8030/tcp
psychological_rag_domain	9006/tcp, 127.0.0.1:9006->8006/tcp
jarvis-temporal-consciousness	7007/tcp
jarvis-session-sidecar	127.0.0.1:8060->8060/tcp, 8070/tcp
jarvis-gbim-temporal-indexer	127.0.0.1:7211->8000/tcp
jarvis-jaeger	4317-4318/tcp, 5775/udp, 5778/tcp, 9411/tcp, 14250/tcp, 14268/tcp, 6831-6832/udp, 127.0.0.1:16686->16686/tcp
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild$ # What does the Caddy config currently route?
docker exec $(docker ps -qf name=caddy) cat /etc/caddy/Caddyfile 2>/dev/null || \
  find /opt/msjarvis-rebuild -name "Caddyfile" -o -name "caddy.conf" 2>/dev/null | xargs cat
{
	https_port 8443
	auto_https off
}

:80, :8443 {
	header {
		Access-Control-Allow-Origin "*"
		Access-Control-Allow-Methods "GET, POST, OPTIONS, DELETE, PUT"
		Access-Control-Allow-Headers "Authorization, Content-Type, X-API-Key"
		Access-Control-Max-Age "3600"
	}

	@chat_rate path /chat* /chat_wv*
	rate_limit @chat_rate {
		zone chat_zone {
			key {remote_host}
			events 60
			window 1m
		}
	}

	encode gzip

	log {
		output file /home/cakidd/msjarvis-rebuild-working/msjarvis-rebuild/logs/caddy_access.log
		format json
	}
}

dashboard.mountainshares.us {
	reverse_proxy 127.0.0.1:3000
}

egeria.mountainshares.us:80, egeria.mountainshares.us:8443 {

	@hastoken {
		header Authorization *
	}
	@notoken {
		not header Authorization *
	}

	# ── Portal API routes → 8095 ─────────────────────────────────────
	handle /auth/portal/me* {
		reverse_proxy 127.0.0.1:8095 {
			header_up Authorization {http.request.header.Authorization}
			header_up X-API-Key {http.request.header.X-API-Key}
			header_up X-Session-Token {http.request.header.X-Session-Token}
		}
	}

		route /portal* {
		handle @notoken {
			respond `{"detail":"Not authenticated"}` 401
		}
		reverse_proxy 127.0.0.1:3001 {
			header_up Authorization {http.request.header.Authorization}
		}
	}

	route /admin* {
		handle @notoken {
			respond `{"detail":"Not authenticated"}` 401
		}
		reverse_proxy 127.0.0.1:3001 {
			header_up Authorization {http.request.header.Authorization}
		}
	}

	route /systems* {
		handle @notoken {
			respond `{"detail":"Not authenticated"}` 401
		}
		reverse_proxy 127.0.0.1:8010 {
			header_up Authorization {http.request.header.Authorization}
			header_up X-API-Key {http.request.header.X-API-Key}
		}
	}

	route /bbb-audit* {
		handle @notoken {
			respond `{"detail":"Not authenticated"}` 401
		}
		reverse_proxy 127.0.0.1:8010 {
			header_up Authorization {http.request.header.Authorization}
			header_up X-API-Key {http.request.header.X-API-Key}
		}
	}

	route /constitutional* {
		handle @notoken {
			respond `{"detail":"Not authenticated"}` 401
		}
		reverse_proxy 127.0.0.1:8010 {
			header_up Authorization {http.request.header.Authorization}
			header_up X-API-Key {http.request.header.X-API-Key}
		}
	}


	# Primary async chat endpoint → jarvis-main-brain
	handle /api/chat/async {
		handle @notoken {
			respond `{"detail":"Not authenticated"}` 401
		}
		rewrite * /chat/async
		reverse_proxy 127.0.0.1:8050 {
			header_up Authorization {http.request.header.Authorization}
			header_up X-Api-Key {env.JARVIS_API_KEY}
			transport http {
				read_buffer 16384
				response_header_timeout 300s
				dial_timeout 10s
			}
		}
	}

	handle /api/chat/status/* {
		handle @notoken {
			respond `{"detail":"Not authenticated"}` 401
		}
		rewrite * /chat/status/{path.3}
		reverse_proxy 127.0.0.1:8050 {
			header_up Authorization {http.request.header.Authorization}
			header_up X-Api-Key {env.JARVIS_API_KEY}
		}
	}

	# /chat is not a real 8018 endpoint
	handle /chat {
		respond `{"detail":"Not found"}` 404
	}

	# Primary AI chat endpoint
	handle /chat_wv* {
		handle @notoken {
			respond `{"detail":"Not authenticated"}` 401
		}
		reverse_proxy 127.0.0.1:8010 {
			header_up Authorization {http.request.header.Authorization}
			header_up X-Api-Key {env.JARVIS_API_KEY}
			transport http {
				read_buffer 16384
				response_header_timeout 300s
				dial_timeout 10s
			}
		}
	}


	handle /auth/apply* {
		reverse_proxy 127.0.0.1:8095 {
			header_up Authorization {http.request.header.Authorization}
			header_up X-API-Key {http.request.header.X-API-Key}
		}
	}

	handle /auth/approve* {
		reverse_proxy 127.0.0.1:8095 {
			header_up Authorization {http.request.header.Authorization}
			header_up X-API-Key {http.request.header.X-API-Key}
		}
	}

	handle /auth/deny* {
		reverse_proxy 127.0.0.1:8095 {
			header_up Authorization {http.request.header.Authorization}
			header_up X-API-Key {http.request.header.X-API-Key}
		}
	}

	handle /auth/portal* {
		reverse_proxy 127.0.0.1:8095 {
			header_up Authorization {http.request.header.Authorization}
			header_up X-API-Key {http.request.header.X-API-Key}
		}
	}

	handle /auth/applications* {
		reverse_proxy 127.0.0.1:8095 {
			header_up Authorization {http.request.header.Authorization}
			header_up X-API-Key {http.request.header.X-API-Key}
		}
	}

	handle /auth/first-login* {
		reverse_proxy 127.0.0.1:8095 {
			header_up Authorization {http.request.header.Authorization}
			header_up X-API-Key {http.request.header.X-API-Key}
		}
	}

	handle /auth/register* {
		reverse_proxy 127.0.0.1:8095 {
			header_up Authorization {http.request.header.Authorization}
			header_up X-API-Key {http.request.header.X-API-Key}
		}
	}

	handle /auth/login* {
		reverse_proxy 127.0.0.1:8095 {
			header_up Authorization {http.request.header.Authorization}
			header_up X-API-Key {http.request.header.X-API-Key}
		}
	}

	handle /auth/logout* {
		reverse_proxy 127.0.0.1:8095 {
			header_up Authorization {http.request.header.Authorization}
			header_up X-API-Key {http.request.header.X-API-Key}
		}
	}

	handle /auth/me* {
		reverse_proxy 127.0.0.1:8095 {
			header_up Authorization {http.request.header.Authorization}
			header_up X-API-Key {http.request.header.X-API-Key}
		}
	}

	handle /auth* {
		reverse_proxy 127.0.0.1:8092 {
			header_up Authorization {http.request.header.Authorization}
		}
	}

	handle {
		reverse_proxy 127.0.0.1:3001
	}

	encode gzip

	log {
		output file /var/log/caddy/caddy_allis.log
		format json
	}
}
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild$ # Is there a frontend service defined in docker-compose already?
grep -A 10 -i "frontend\|ui\|web\|react\|next\|static" \
  /opt/msjarvis-rebuild/docker-compose.yml
    build:
      context: ./contracts
      dockerfile: Dockerfile
    container_name: jarvis-contracts
    working_dir: /workspace
    volumes:
      - ./contracts:/workspace
      - ./secrets/contracts.env:/workspace/.env:ro
    environment:
      - NODE_ENV=development
    command: ["sleep", "infinity"]
--
    build:
      context: .
      dockerfile: Dockerfile.gateway
    container_name: jarvis-unified-gateway
    working_dir: /app/services
    command:
      - python3
      - ms_jarvis_unified_gateway.py
    ports:
      - 127.0.0.1:8001:8001
    environment:
--
      - nbb_pituitary_gland
      - nbb_spiritual_maternal_integration
      - nbb_subconscious
      - jarvis-fifth-dgm
      - jarvis-toroidal
      - jarvis-psychology-services
      - psychological_rag_domain
      - jarvis-constitutional-guardian
    networks:
      - qualia-net
    restart: unless-stopped
--
    build:
      context: .
      dockerfile: Dockerfile.brain
    container_name: jarvis-20llm-production
    extra_hosts:
      - "host.docker.internal:host-gateway"
    working_dir: /app/services
    command:
      - python3
      - ai_server_20llm_PRODUCTION.py
    expose:
--
    build:
      context: .
      dockerfile: Dockerfile
    container_name: jarvis-wv-entangled-gateway
    working_dir: /app/services
    command:
      - python
      - -m
      - uvicorn
      - msjarvis_wv_entangled_gateway:app
      - --host
--
    build:
      context: ./services
      dockerfile: Dockerfile-llm1-proxy
    container_name: llm1-proxy
    expose:
      - "8201"
    ports:
      - 127.0.0.1:8201:8201
    networks:
      - qualia-net
    restart: unless-stopped
--
    build:
      context: ./services
      dockerfile: Dockerfile-llm2-proxy
    container_name: llm2-proxy
    expose:
      - "8202"
    ports:
      - 127.0.0.1:8202:8202
    networks:
      - qualia-net
    restart: unless-stopped
--
    build:
      context: ./services
      dockerfile: Dockerfile-llm3-proxy
    container_name: llm3-proxy
    expose:
      - "8203"
    ports:
      - 127.0.0.1:8203:8203
    networks:
      - qualia-net
    restart: unless-stopped
--
    build:
      context: ./services
      dockerfile: Dockerfile-llm4-proxy
    container_name: llm4-proxy
    expose:
      - "8204"
    ports:
      - 127.0.0.1:8204:8204
    networks:
      - qualia-net
    restart: unless-stopped
--
    build:
      context: ./services
      dockerfile: Dockerfile-llm5-proxy
    container_name: llm5-proxy
    expose:
      - "8205"
    ports:
      - 127.0.0.1:8205:8205
    networks:
      - qualia-net
    restart: unless-stopped
--
    build:
      context: ./services
      dockerfile: Dockerfile-llm6-proxy
    container_name: llm6-proxy
    expose:
      - "8206"
    ports:
      - 127.0.0.1:8206:8206
    networks:
      - qualia-net
    restart: unless-stopped
--
    build:
      context: ./services
      dockerfile: Dockerfile-llm7-proxy
    container_name: llm7-proxy
    expose:
      - "8207"
    ports:
      - 127.0.0.1:8207:8207
    networks:
      - qualia-net
    restart: unless-stopped
--
    build:
      context: ./services
      dockerfile: Dockerfile-llm8-proxy
    container_name: llm8-proxy
    expose:
      - "8208"
    ports:
      - 127.0.0.1:8208:8208
    networks:
      - qualia-net
    restart: unless-stopped
--
    build:
      context: ./services
      dockerfile: Dockerfile-llm9-proxy
    container_name: llm9-proxy
    expose:
      - "8209"
    ports:
      - 127.0.0.1:8209:8209
    networks:
      - qualia-net
    restart: unless-stopped
--
    build:
      context: ./services
      dockerfile: Dockerfile-llm10-proxy
    container_name: llm10-proxy
    expose:
      - "8210"
    ports:
      - 127.0.0.1:8210:8210
    networks:
      - qualia-net
    restart: unless-stopped
--
    build:
      context: ./services
      dockerfile: Dockerfile-llm11-proxy
    container_name: llm11-proxy
    expose:
      - "8211"
    ports:
      - 127.0.0.1:8211:8211
    networks:
      - qualia-net
    restart: unless-stopped
--
    build:
      context: ./services
      dockerfile: Dockerfile-llm12-proxy
    container_name: llm12-proxy
    expose:
      - "8212"
    ports:
      - 127.0.0.1:8212:8212
    networks:
      - qualia-net
    restart: unless-stopped
--
    build:
      context: ./services
      dockerfile: Dockerfile-llm13-proxy
    container_name: llm13-proxy
    expose:
      - "8213"
    ports:
      - 127.0.0.1:8213:8213
    networks:
      - qualia-net
    restart: unless-stopped
--
    build:
      context: ./services
      dockerfile: Dockerfile-llm14-proxy
    container_name: llm14-proxy
    expose:
      - "8214"
    ports:
      - 127.0.0.1:8214:8214
    networks:
      - qualia-net
    restart: unless-stopped
--
    build:
      context: ./services
      dockerfile: Dockerfile-llm15-proxy
    container_name: llm15-proxy
    expose:
      - "8215"
    ports:
      - 127.0.0.1:8215:8215
    networks:
      - qualia-net
    restart: unless-stopped
--
    build:
      context: ./services
      dockerfile: Dockerfile-llm16-proxy
    container_name: llm16-proxy
    expose:
      - "8216"
    ports:
      - 127.0.0.1:8216:8216
    networks:
      - qualia-net
    restart: unless-stopped
--
    build:
      context: ./services
      dockerfile: Dockerfile-llm17-proxy
    container_name: llm17-proxy
    expose:
      - "8217"
    ports:
      - 127.0.0.1:8217:8217
    networks:
      - qualia-net
    restart: unless-stopped
--
    build:
      context: ./services
      dockerfile: Dockerfile-llm18-proxy
    container_name: llm18-proxy
    expose:
      - "8218"
    ports:
      - 127.0.0.1:8218:8218
    networks:
      - qualia-net
    restart: unless-stopped
--
    build:
      context: ./services
      dockerfile: Dockerfile-llm19-proxy
    container_name: llm19-proxy
    expose:
      - "8219"
    ports:
      - 127.0.0.1:8219:8219
    networks:
      - qualia-net
    restart: unless-stopped
--
    build:
      context: ./services
      dockerfile: Dockerfile-llm20-proxy
    container_name: llm20-proxy
    expose:
      - "8220"
    ports:
      - 127.0.0.1:8220:8220
    networks:
      - qualia-net
    restart: unless-stopped
--
    build:
      context: ./services
      dockerfile: Dockerfile-llm21-proxy
    container_name: llm21-proxy
    expose:
      - "8221"
    ports:
      - 127.0.0.1:8221:8221
    networks:
      - qualia-net
    restart: unless-stopped
--
    build:
      context: ./services
      dockerfile: Dockerfile-llm22-proxy
    container_name: llm22-proxy
    expose:
      - "8222"
    ports:
      - 127.0.0.1:8222:8222
    networks:
      - qualia-net
    restart: unless-stopped
--
    build:
      context: ./services
      dockerfile: Dockerfile.lm_synthesizer
    container_name: jarvis-lm-synthesizer
    command:
      - python
      - lm_synthesizer.py
    expose:
      - "8001"
    environment:
      - OLLAMA_HOST=http://jarvis-ollama:11434
--
    build:
      context: ./services
      dockerfile: Dockerfile.hippocampus
    container_name: jarvis-hippocampus
    working_dir: /app
    command:
      - uvicorn
      - hippocampus_service:app
      - --host
      - 0.0.0.0
      - --port
--
    build:
      context: .
      dockerfile: Dockerfile.brain
    container_name: jarvis-brain-orchestrator
    working_dir: /app/services
    environment:
      - SERVICE_PORT=7260
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - CLOCK_TS=1767812077
      - HF_HUB_OFFLINE=1
    command:
--
    build:
      context: .
      dockerfile: Dockerfile.agents
    container_name: jarvis-agents-service
    working_dir: /app/services
    command:
      - python3
      - ms_jarvis_agents_service.py
    expose:
      - "8005"
    environment:
--
  jarvis-web-research:
    build:
      context: ./services
      dockerfile: Dockerfile.web_research
    container_name: jarvis-web-research
    expose:
      - "8008"
    environment:
      - SERVICE_PORT=8008
      - RAG_SERVER_URL=http://jarvis-rag-server:8003
      - CLOCK_TS=1767812077
      - HF_HUB_OFFLINE=1
    command:
      - python
      - /app/services/ms_jarvis_web_research_simple.py
    volumes:
      - ./services/ms_jarvis_web_research_simple.py:/app/services/ms_jarvis_web_research_simple.py:ro
    networks:
      - qualia-net
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: "3"
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
      - "8021"
    environment:
--
    build:
      context: ./services
      dockerfile: Dockerfile.fifth_dgm_real
    container_name: jarvis-fifth-dgm
    expose:
      - "4002"
    ports:
      - 127.0.0.1:4002:4002
    environment:
      - FIFTH_DGM_PORT=4002
      - OLLAMA_HOST=http://jarvis-ollama:11434
--
    build:
      context: ./services
      dockerfile: Dockerfile.mother_protocols
    container_name: jarvis-mother-protocols
    expose:
      - "4000"
    networks:
      - qualia-net
    restart: unless-stopped
    environment:
      CLOCK_TS: 1767812077
--
    build:
      context: ./services
      dockerfile: Dockerfile.temporal_consciousness
    container_name: jarvis-temporal-consciousness
    expose:
      - "7007"
    networks:
      - qualia-net
    restart: unless-stopped
    environment:
      CLOCK_TS: 1767812077
--
    build:
      context: ./services
      dockerfile: Dockerfile.69dgm_bridge
    container_name: jarvis-69dgm-bridge
    expose:
      - "9000"
    ports:
      - "127.0.0.1:9000:9000"
    networks:
      - qualia-net
    restart: unless-stopped
--
    build:
      context: ./services
      dockerfile: Dockerfile.bbb
    container_name: jarvis-blood-brain-barrier
    working_dir: /app/services
    command:
      - python3
      - ms_jarvis_blood_brain_barrier.py
    environment:
      - CLOCK_TS=1767812077
      - HF_HUB_OFFLINE=1
--
    build:
      context: .
      dockerfile: Dockerfile.woah
    container_name: jarvis-woah
    expose:
      - "7012"
    ports:
      - 127.0.0.1:7012:7012
    environment:
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - SERVICE_PORT=7012
--
    build:
      context: ./services
      dockerfile: Dockerfile.consciousness_bridge
    container_name: jarvis-consciousness-bridge
    command: python3 /app/services/ms_jarvis_consciousness_bridge.py
    ports:
      - "127.0.0.1:8020:8018"
    environment:
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - WOAH_URL=http://jarvis-woah:7012
      - CLOCK_TS=1767812077
--
    build:
      context: ./services
      dockerfile: Dockerfile.qualia
    container_name: jarvis-qualia-engine
    expose:
      - "8017"
    environment:
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - CLOCK_TS=1767812077
      - HF_HUB_OFFLINE=1
    volumes:
--
    build:
      context: ./services
      dockerfile: Dockerfile.icontainers_fastapi
    container_name: jarvis-i-containers
    expose:
      - "8015"
    environment:
      - NBB_ICONTAINERS_URL=http://nbb-i-containers:7005
    networks:
      - qualia-net
    restart: unless-stopped
--
    build:
      context: ./services
      dockerfile: Dockerfile.semaphore
    container_name: jarvis-semaphore
    expose:
      - "8030"
    ports:
      - 127.0.0.1:8030:8030
    networks:
      - qualia-net
    restart: unless-stopped
--
    build:
      context: .
      dockerfile: Dockerfile.neuro
    container_name: jarvis-neurobiological-master
    command:
      - uvicorn
      - services.ms_jarvis_neurobiological_master:app
      - --host
      - 0.0.0.0
      - --port
      - "8018" 
--
    build:
      context: ./services
    container_name: jarvis-fractal-consciousness
    ports:
      - "127.0.0.1:8027:8008"
    environment:
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - CLOCK_TS=1767812077
      - HF_HUB_OFFLINE=1
    volumes:
      - ./services/msjarvis_fractal_consciousness.py:/app/msjarvis_fractal_consciousness.py:ro
--
    image: msjarvis-rebuild-jarvis-rag-server:latest
    container_name: jarvis-autonomous-learner
    command:
      - /bin/sh
      - -c
      - cd /app/services && python3 -m uvicorn ms_jarvis_autonomous_learner:app --host 0.0.0.0 --port 8425
    ports:
      - "127.0.0.1:8425:8425"
    expose:
      - "8425"
    environment:
--
    build:
      context: .
      dockerfile: Dockerfile.nbb_icontainers_fastapi
    container_name: nbb-i-containers
    expose:
      - "7005"
    ports:
      - 127.0.0.1:8101:7005
    networks:
       qualia-net:
         aliases:
--
    build: ./neurobiological_brain/consciousness_containers/service
    ports:
      - 127.0.0.1:8102:8010
    networks:
      - qualia-net
    restart: unless-stopped
    volumes:
      - ./services/neurobiological_brain/i_containers/i_container_1/memory_self.py:/app/services/neurobiological_brain/i_containers/i_container_1/memory_self.py:ro
    environment:
      CLOCK_TS: 1767812077
      JARVIS_API_KEY: 250d77bc696f043ffe1ffc69a49d1ec3899b9a6bd37263bc11daa9a2bd4e7735
--
    build: ./neurobiological_brain/spiritual_root/service
    ports:
      - 127.0.0.1:8103:8010
    networks:
      - qualia-net
    restart: unless-stopped
    environment:
      SERVICE_PORT: "8010"
      JARVIS_API_KEY: 250d77bc696f043ffe1ffc69a49d1ec3899b9a6bd37263bc11daa9a2bd4e7735
      JARVIS_API_KEY_FILE: /run/secrets/jarvisapikey
      CLOCK_TS: 1767812077
--
    build: ./neurobiological_brain/woah_algorithms/service
    ports:
      - 127.0.0.1:8104:8010
    networks:
      - qualia-net
    restart: unless-stopped
    environment:
      CLOCK_TS: 1767812077
      JARVIS_API_KEY: 250d77bc696f043ffe1ffc69a49d1ec3899b9a6bd37263bc11daa9a2bd4e7735
      JARVIS_API_KEY_FILE: /run/secrets/jarvisapikey
  nbb_prefrontal_cortex:
    build: ./neurobiological_brain/prefrontal_cortex/service
    ports:
      - 127.0.0.1:8105:7005
    networks:
      - qualia-net
    restart: unless-stopped
    environment:
      CLOCK_TS: 1767812077
      SERVICE_REDIS_HOST: jarvis-redis
      SERVICE_REDIS_PORT: 6379
      JARVIS_API_KEY: 250d77bc696f043ffe1ffc69a49d1ec3899b9a6bd37263bc11daa9a2bd4e7735
--
    build: ./neurobiological_brain/heteroglobulin_transport/service
    ports:
      - 127.0.0.1:8106:8010
    networks:
      - qualia-net
    restart: unless-stopped
    environment:
      CLOCK_TS: 1767812077
      SERVICE_REDIS_HOST: jarvis-redis
      SERVICE_REDIS_PORT: 6379
      JARVIS_API_KEY: 250d77bc696f043ffe1ffc69a49d1ec3899b9a6bd37263bc11daa9a2bd4e7735
--
    build: ./neurobiological_brain/mother_carrie_protocols/service
    ports:
      - 127.0.0.1:8107:8010
    networks:
      - qualia-net
    restart: unless-stopped
    environment:
      SERVICE_PORT: "8010"
      CLOCK_TS: 1767812077
      SERVICE_REDIS_HOST: jarvis-redis
      SERVICE_REDIS_PORT: 6379
--
  nbb_pituitary_gland:
    build: ./neurobiological_brain/pituitary_gland/service
    ports:
      - 127.0.0.1:8108:80
    networks:
      - qualia-net
    restart: unless-stopped
    environment:
      CLOCK_TS: 1767812077
      WEB_CONCURRENCY: "1"
      MAX_WORKERS: "1"
      REDIS_URL: "redis://jarvis-redis:6379/0"
      JARVIS_API_KEY: 250d77bc696f043ffe1ffc69a49d1ec3899b9a6bd37263bc11daa9a2bd4e7735
      JARVIS_API_KEY_FILE: /run/secrets/jarvisapikey
      APP_MODULE: "pituitary_gland:app"
  nbb_spiritual_maternal_integration:
    build: ./neurobiological_brain/spiritual_maternal_integration/service
    ports:
      - 127.0.0.1:8109:8010
    networks:
      - qualia-net
    restart: unless-stopped
    environment:
      SERVICE_PORT: "8010"
      CLOCK_TS: 1767812077
      SERVICE_REDIS_HOST: jarvis-redis
      SERVICE_REDIS_PORT: 6379
--
    build: ./neurobiological_brain/darwin_godel_machines/service
    ports:
      - 127.0.0.1:8302:8010
    networks:
      - qualia-net
    restart: unless-stopped
    volumes:
      - /opt/msjarvis-rebuild/services:/opt/msjarvis-rebuild/services
      - ./neurobiological_brain/darwin_godel_machines/service/dgm_governance_view.json:/app/dgm_governance_view.json:ro
      - /var/run/docker.sock:/var/run/docker.sock
    environment:
      CLOCK_TS: 1767812077
  nbb_blood_brain_barrier:
    build: ./neurobiological_brain/blood_brain_barrier/service
    ports:
      - 127.0.0.1:8301:8010
    networks:
      - qualia-net
    restart: unless-stopped
    environment:
      CLOCK_TS: 1767812077
  nbb_subconscious:
    build: ./neurobiological_brain/subconscious/service
    ports:
      - 127.0.0.1:8112:8010
    networks:
      - qualia-net
    restart: unless-stopped
    environment:
      CLOCK_TS: 1767812077
      JARVIS_API_KEY: 250d77bc696f043ffe1ffc69a49d1ec3899b9a6bd37263bc11daa9a2bd4e7735
      JARVIS_API_KEY_FILE: /run/secrets/jarvisapikey
  nbb_qualia_engine:
    build: ./neurobiological_brain/qualia_engine/service
    ports:
      - 127.0.0.1:8303:8010
    networks:
      - qualia-net
    restart: unless-stopped
    environment:
      CLOCK_TS: 1767812077
      JARVIS_API_KEY: 250d77bc696f043ffe1ffc69a49d1ec3899b9a6bd37263bc11daa9a2bd4e7735
      JARVIS_API_KEY_FILE: /run/secrets/jarvisapikey
  neo4j:
--
    build:
      context: .
      dockerfile: Dockerfile
    image: jarvis-main-brain:latest
    container_name: jarvis-main-brain
    working_dir: /app/services
    command:
      - python
      - -m
      - uvicorn
      - main_brain:app
--
    build:
      context: .
      dockerfile: Dockerfile.local_resources
    container_name: jarvis-local-resources
    working_dir: /app/services
    expose:
      - "8035"
    ports:
      - 127.0.0.1:8006:8006
    environment:
      - PYTHONPATH=/app/services
--
      - msjarvis-rebuild_jarvis-local-resources-db-data:/var/lib/postgresql/data
    networks:
      - qualia-net
    restart: unless-stopped
  jarvis-gis-rag:
    build:
      context: .
      dockerfile: Dockerfile.gis_rag
    container_name: jarvis-gis-rag
    environment:
      - CHROMA_HOST=172.18.0.2
      - CHROMA_PORT=8000
      - GIS_RAG_CHROMA_URL=http://jarvis-chroma:8000
      - GIS_RAG_COLLECTION=geospatial_features
      - GIS_EMBED_MODEL=all-minilm
      - CLOCK_TS=1767812077
--
    build:
      context: ./services
      dockerfile: Dockerfile.toroidal
    image: msjarvis-toroidal:latest
    container_name: jarvis-toroidal
    ports:
      - 127.0.0.1:8025:8025
    environment:
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
      - CLOCK_TS=1767812077
--
    build:
      context: ./services
      dockerfile: Dockerfile.psychological_rag
    container_name: psychological_rag_domain
    working_dir: /app
    command: ["python", "psychological_rag_domain.py"]
    expose:
      - "8006"
    ports:
      - 127.0.0.1:9006:8006
    networks:
--
    build:
      context: ./services
      dockerfile: Dockerfile.psychology_services
    container_name: jarvis-psychology-services
    working_dir: /app
    command: ["uvicorn", "psychology_server:app", "--host", "0.0.0.0", "--port", "8019"]
    expose:
      - "8019"
    ports:
      - 127.0.0.1:8019:8019
    environment:
--
    build:
      context: ./services
      dockerfile: Dockerfile.constitutional_guardian
    container_name: jarvis-constitutional-guardian
    working_dir: /app
    expose:
      - "8091"
    ports:
      - 127.0.0.1:8091:8091
    environment:
      - SERVICE_PORT=8091
--
    build:
      context: ./services
      dockerfile: Dockerfile.judge
    container_name: jarvis-judge-truth
    ports:
      - "127.0.0.1:7230:7230"
    volumes:
      - /opt/msjarvis-rebuild/judge-keys/judge_sk.bin:/app/judge_sk.bin:ro
      - /opt/msjarvis-rebuild/judge-keys/judge_pk.bin:/app/judge_pk.bin:ro
    command:
      - python
      - judge_truth_filter.py
    expose:
      - "7230"
    environment:
      - SERVICE_NAME=judge_truth_filter
      - SERVICE_PORT=7230
      - CLOCK_TS=1767812077
      - HF_HUB_OFFLINE=1
--
    build:
      context: ./services
      dockerfile: Dockerfile.judge
    container_name: jarvis-judge-consistency
    ports:
      - "127.0.0.1:7231:7231"
    volumes:
      - /opt/msjarvis-rebuild/judge-keys/judge_sk.bin:/app/judge_sk.bin:ro
      - /opt/msjarvis-rebuild/judge-keys/judge_pk.bin:/app/judge_pk.bin:ro
    command:
      - python
      - judge_consistency_engine.py
    expose:
      - "7231"
    environment:
      - SERVICE_NAME=judge_consistency_engine
      - SERVICE_PORT=7231
      - CLOCK_TS=1767812077
      - HF_HUB_OFFLINE=1
--
    build:
      context: ./services
      dockerfile: Dockerfile.judge
    container_name: jarvis-judge-alignment
    ports:
      - "127.0.0.1:7232:7232"
    volumes:
      - /opt/msjarvis-rebuild/judge-keys/judge_sk.bin:/app/judge_sk.bin:ro
      - /opt/msjarvis-rebuild/judge-keys/judge_pk.bin:/app/judge_pk.bin:ro
    command:
      - python
      - judge_alignment_filter.py
    expose:
      - "7232"
    environment:
      - SERVICE_NAME=judge_alignment_filter
      - SERVICE_PORT=7232
      - CLOCK_TS=1767812077
      - HF_HUB_OFFLINE=1
--
    build:
      context: ./services
      dockerfile: Dockerfile.judge
    container_name: jarvis-judge-ethics
    ports:
      - "127.0.0.1:7233:7233"
    volumes:
      - /opt/msjarvis-rebuild/judge-keys/judge_sk.bin:/app/judge_sk.bin:ro
      - /opt/msjarvis-rebuild/judge-keys/judge_pk.bin:/app/judge_pk.bin:ro
    command:
      - python
      - judge_ethics_filter.py
    expose:
      - "7233"
    environment:
      - SERVICE_NAME=judge_ethics_filter
      - SERVICE_PORT=7233
      - CLOCK_TS=1767812077
      - HF_HUB_OFFLINE=1
--
    build:
      context: ./services
      dockerfile: Dockerfile.judge
    container_name: jarvis-judge-pipeline
    ports:
      - "127.0.0.1:7239:7239"
    volumes:
      - /opt/msjarvis-rebuild/judge-keys/judge_sk.bin:/app/judge_sk.bin:ro
      - /opt/msjarvis-rebuild/judge-keys/judge_pk.bin:/app/judge_pk.bin:ro
    command:
      - python
      - judge_pipeline.py
    expose:
      - "7239"
    environment:
      - SERVICE_NAME=judge_pipeline
      - SERVICE_PORT=7239
      - JUDGE_TRUTH_URL=http://jarvis-judge-truth:7230
      - JUDGE_CONSISTENCY_URL=http://jarvis-judge-consistency:7231
--
    build:
      context: ./services
      dockerfile: Dockerfile.aaacpe_rag
    container_name: jarvis-aaacpe-rag
    expose:
      - "8032"
    ports:
      - 127.0.0.1:8032:8032
    environment:
      - SERVICE_PORT=8032
      - CHROMA_HOST=172.18.0.2
--
    build:
      context: ./services
      dockerfile: Dockerfile.rag_server
    container_name: jarvis-rag-server
    ports:
      - "127.0.0.1:8003:8003"
    expose:
      - "8003"
    environment:
      - SERVICE_PORT=8003
      - CHROMA_HOST=172.18.0.2
--
      - /home/cakidd/msjarvis-rebuild/data/mountainshares:/app/mountainshares_docs:ro
      - /home/cakidd/msjarvis-rebuild/services/backup_chroma_mountainshares_knowledge.json:/app/backup_mountainshares.json:ro
      - /opt/msjarvis-rebuild/services:/app/services
    networks:
      - qualia-net
    restart: unless-stopped
  jarvis-spiritual-rag:
    build:
      context: ./services
      dockerfile: Dockerfile.spiritual_rag
    container_name: jarvis-spiritual-rag
    expose:
      - "8005"
    ports:
      - 127.0.0.1:8005:8005
    environment:
      - SERVICE_PORT=8005
      - CHROMA_HOST=172.18.0.2
--
    build:
      context: ./services
      dockerfile: Dockerfile.eeg
    command: uvicorn jarvis_eeg_delta_30s:app --host 0.0.0.0 --port 8073
    container_name: jarvis-eeg-delta
    restart: unless-stopped
    ports:
      - "127.0.0.1:8073:8073/tcp"
    networks:
      - qualia-net
    environment:
--
    build:
      context: ./services
      dockerfile: Dockerfile.eeg
    command: uvicorn jarvis_eeg_theta_60s:app --host 0.0.0.0 --port 8074
    container_name: jarvis-eeg-theta
    restart: unless-stopped
    ports:
      - "127.0.0.1:8074:8074/tcp"
    networks:
      - qualia-net
    environment:
--
    build:
      context: ./services
      dockerfile: Dockerfile.eeg
    command: uvicorn jarvis_eeg_beta_5m:app --host 0.0.0.0 --port 8075
    container_name: jarvis-eeg-beta
    restart: unless-stopped
    ports:
      - "127.0.0.1:8075:8075/tcp"
    networks:
      - qualia-net
    environment:
--
    build: { context: ./services, dockerfile: Dockerfile.bridge }
    container_name: jarvis-dgm-bridge-01
    command: python3 bridge_cross_dgm_10001.py
    expose: ["10001"]
    environment:
      - SERVICE_PORT=10001
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - FRACTAL_URL=http://jarvis-fractal-consciousness:8027
      - SWARM_URL=http://jarvis-swarm-intelligence:8021
      - UPSTREAM_URL=http://jarvis-judge-pipeline:7239
      - DOWNSTREAM_URL=http://jarvis-neurobiological-master:8018
--
    build: { context: ./services, dockerfile: Dockerfile.bridge }
    container_name: jarvis-dgm-bridge-02
    command: python3 bridge_cross_dgm_10002.py
    expose: ["10002"]
    environment:
      - SERVICE_PORT=10002
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - FRACTAL_URL=http://jarvis-fractal-consciousness:8027
      - SWARM_URL=http://jarvis-swarm-intelligence:8021
      - UPSTREAM_URL=http://jarvis-qualia-engine:8017
      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
--
    build: { context: ./services, dockerfile: Dockerfile.bridge }
    container_name: jarvis-dgm-bridge-03
    command: python3 bridge_cross_dgm_10003.py
    expose: ["10003"]
    environment:
      - SERVICE_PORT=10003
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - FRACTAL_URL=http://jarvis-fractal-consciousness:8027
      - SWARM_URL=http://jarvis-swarm-intelligence:8021
      - UPSTREAM_URL=http://jarvis-consciousness-bridge:8018
      - DOWNSTREAM_URL=http://jarvis-swarm-intelligence:8021
--
    build: { context: ./services, dockerfile: Dockerfile.bridge }
    container_name: jarvis-dgm-bridge-04
    command: python3 bridge_cross_dgm_10004.py
    expose: ["10004"]
    environment:
      - SERVICE_PORT=10004
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - FRACTAL_URL=http://jarvis-fractal-consciousness:8027
      - SWARM_URL=http://jarvis-swarm-intelligence:8021
      - UPSTREAM_URL=http://jarvis-swarm-intelligence:8021
      - DOWNSTREAM_URL=http://jarvis-fractal-consciousness:8027
--
    build: { context: ./services, dockerfile: Dockerfile.bridge }
    container_name: jarvis-dgm-bridge-05
    command: python3 bridge_cross_dgm_10005.py
    expose: ["10005"]
    environment:
      - SERVICE_PORT=10005
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - FRACTAL_URL=http://jarvis-fractal-consciousness:8027
      - SWARM_URL=http://jarvis-swarm-intelligence:8021
      - UPSTREAM_URL=http://jarvis-fractal-consciousness:8027
      - DOWNSTREAM_URL=http://jarvis-blood-brain-barrier:8016
--
    build: { context: ./services, dockerfile: Dockerfile.bridge }
    container_name: jarvis-dgm-bridge-06
    command: python3 bridge_cross_dgm_10006.py
    expose: ["10006"]
    environment:
      - SERVICE_PORT=10006
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - FRACTAL_URL=http://jarvis-fractal-consciousness:8027
      - SWARM_URL=http://jarvis-swarm-intelligence:8021
      - UPSTREAM_URL=http://jarvis-blood-brain-barrier:8016
      - DOWNSTREAM_URL=http://jarvis-constitutional-guardian:8091
--
    build: { context: ./services, dockerfile: Dockerfile.bridge }
    container_name: jarvis-dgm-bridge-07
    command: python3 bridge_cross_dgm_10007.py
    expose: ["10007"]
    environment:
      - SERVICE_PORT=10007
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - FRACTAL_URL=http://jarvis-fractal-consciousness:8027
      - SWARM_URL=http://jarvis-swarm-intelligence:8021
      - UPSTREAM_URL=http://jarvis-constitutional-guardian:8091
      - DOWNSTREAM_URL=http://jarvis-judge-pipeline:7239
--
    build: { context: ./services, dockerfile: Dockerfile.bridge }
    container_name: jarvis-dgm-bridge-08
    command: python3 bridge_cross_dgm_10008.py
    expose: ["10008"]
    environment:
      - SERVICE_PORT=10008
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - FRACTAL_URL=http://jarvis-fractal-consciousness:8027
      - SWARM_URL=http://jarvis-swarm-intelligence:8021
      - UPSTREAM_URL=http://jarvis-neurobiological-master:8018
      - DOWNSTREAM_URL=http://jarvis-qualia-engine:8017
--
    build: { context: ./services, dockerfile: Dockerfile.bridge }
    container_name: jarvis-dgm-bridge-09
    command: python3 bridge_cross_dgm_10009.py
    expose: ["10009"]
    environment:
      - SERVICE_PORT=10009
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - FRACTAL_URL=http://jarvis-fractal-consciousness:8027
      - SWARM_URL=http://jarvis-swarm-intelligence:8021
      - UPSTREAM_URL=http://jarvis-eeg-beta:8030
      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
--
    build: { context: ./services, dockerfile: Dockerfile.bridge }
    container_name: jarvis-dgm-bridge-10
    command: python3 bridge_cross_dgm_10010.py
    expose: ["10010"]
    environment:
      - SERVICE_PORT=10010
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - FRACTAL_URL=http://jarvis-fractal-consciousness:8027
      - SWARM_URL=http://jarvis-swarm-intelligence:8021
      - UPSTREAM_URL=http://jarvis-temporal-consciousness:8029
      - DOWNSTREAM_URL=http://jarvis-fractal-consciousness:8027
--
    build: { context: ./services, dockerfile: Dockerfile.bridge }
    container_name: jarvis-dgm-bridge-11
    command: python3 bridge_cross_dgm_10011.py
    expose: ["10011"]
    environment:
      - SERVICE_PORT=10011
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - FRACTAL_URL=http://jarvis-fractal-consciousness:8027
      - SWARM_URL=http://jarvis-swarm-intelligence:8021
      - UPSTREAM_URL=http://jarvis-woah:8025
      - DOWNSTREAM_URL=http://jarvis-swarm-intelligence:8021
--
    build: { context: ./services, dockerfile: Dockerfile.bridge }
    container_name: jarvis-dgm-bridge-12
    command: python3 bridge_cross_dgm_10012.py
    expose: ["10012"]
    environment:
      - SERVICE_PORT=10012
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - FRACTAL_URL=http://jarvis-fractal-consciousness:8027
      - SWARM_URL=http://jarvis-swarm-intelligence:8021
      - UPSTREAM_URL=http://jarvis-mother-protocols:8090
      - DOWNSTREAM_URL=http://jarvis-constitutional-guardian:8091
--
    build: { context: ./services, dockerfile: Dockerfile.bridge }
    container_name: jarvis-dgm-bridge-13
    command: python3 bridge_cross_dgm_10013.py
    expose: ["10013"]
    environment:
      - SERVICE_PORT=10013
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - FRACTAL_URL=http://jarvis-fractal-consciousness:8027
      - SWARM_URL=http://jarvis-swarm-intelligence:8021
      - UPSTREAM_URL=http://jarvis-toroidal:8026
      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
--
    build: { context: ./services, dockerfile: Dockerfile.bridge }
    container_name: jarvis-dgm-bridge-14
    command: python3 bridge_cross_dgm_10014.py
    expose: ["10014"]
    environment:
      - SERVICE_PORT=10014
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - FRACTAL_URL=http://jarvis-fractal-consciousness:8027
      - SWARM_URL=http://jarvis-swarm-intelligence:8021
      - UPSTREAM_URL=http://jarvis-hippocampus:8023
      - DOWNSTREAM_URL=http://jarvis-qualia-engine:8017
--
    build: { context: ./services, dockerfile: Dockerfile.bridge }
    container_name: jarvis-dgm-bridge-15
    command: python3 bridge_cross_dgm_10015.py
    expose: ["10015"]
    environment:
      - SERVICE_PORT=10015
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - FRACTAL_URL=http://jarvis-fractal-consciousness:8027
      - SWARM_URL=http://jarvis-swarm-intelligence:8021
      - UPSTREAM_URL=http://jarvis-semaphore:8022
      - DOWNSTREAM_URL=http://jarvis-blood-brain-barrier:8016
--
    build: { context: ./services, dockerfile: Dockerfile.bridge }
    container_name: jarvis-dgm-bridge-16
    command: python3 bridge_cross_dgm_10016.py
    expose: ["10016"]
    environment:
      - SERVICE_PORT=10016
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - FRACTAL_URL=http://jarvis-fractal-consciousness:8027
      - SWARM_URL=http://jarvis-swarm-intelligence:8021
      - UPSTREAM_URL=http://jarvis-fifth-dgm:4002
      - DOWNSTREAM_URL=http://jarvis-judge-pipeline:7239
--
    build: { context: ./services, dockerfile: Dockerfile.bridge }
    container_name: jarvis-dgm-bridge-17
    command: python3 bridge_cross_dgm_10017.py
    expose: ["10017"]
    environment:
      - SERVICE_PORT=10017
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - FRACTAL_URL=http://jarvis-fractal-consciousness:8027
      - SWARM_URL=http://jarvis-swarm-intelligence:8021
      - UPSTREAM_URL=http://jarvis-swarm-intelligence:8021
      - DOWNSTREAM_URL=http://jarvis-constitutional-guardian:8091
--
    build: { context: ./services, dockerfile: Dockerfile.bridge }
    container_name: jarvis-dgm-bridge-18
    command: python3 bridge_cross_dgm_10018.py
    expose: ["10018"]
    environment:
      - SERVICE_PORT=10018
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - FRACTAL_URL=http://jarvis-fractal-consciousness:8027
      - SWARM_URL=http://jarvis-swarm-intelligence:8021
      - UPSTREAM_URL=http://jarvis-fractal-consciousness:8027
      - DOWNSTREAM_URL=http://jarvis-qualia-engine:8017
--
    build: { context: ./services, dockerfile: Dockerfile.bridge }
    container_name: jarvis-dgm-bridge-19
    command: python3 bridge_cross_dgm_10019.py
    expose: ["10019"]
    environment:
      - SERVICE_PORT=10019
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - FRACTAL_URL=http://jarvis-fractal-consciousness:8027
      - SWARM_URL=http://jarvis-swarm-intelligence:8021
      - UPSTREAM_URL=http://jarvis-judge-pipeline:7239
      - DOWNSTREAM_URL=http://jarvis-swarm-intelligence:8021
--
    build: { context: ./services, dockerfile: Dockerfile.bridge }
    container_name: jarvis-dgm-bridge-20
    command: python3 bridge_cross_dgm_10020.py
    expose: ["10020"]
    environment:
      - SERVICE_PORT=10020
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - FRACTAL_URL=http://jarvis-fractal-consciousness:8027
      - SWARM_URL=http://jarvis-swarm-intelligence:8021
      - UPSTREAM_URL=http://jarvis-consciousness-bridge:8018
      - DOWNSTREAM_URL=http://jarvis-fractal-consciousness:8027
--
    build: { context: ./services, dockerfile: Dockerfile.bridge }
    container_name: jarvis-dgm-bridge-21
    command: python3 bridge_cross_dgm_10021.py
    expose: ["10021"]
    environment:
      - SERVICE_PORT=10021
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - FRACTAL_URL=http://jarvis-fractal-consciousness:8027
      - SWARM_URL=http://jarvis-swarm-intelligence:8021
      - UPSTREAM_URL=http://jarvis-constitutional-guardian:8091
      - DOWNSTREAM_URL=http://jarvis-swarm-intelligence:8021
--
    build: { context: ./services, dockerfile: Dockerfile.bridge }
    container_name: jarvis-dgm-bridge-22
    command: python3 bridge_cross_dgm_10022.py
    expose: ["10022"]
    environment:
      - SERVICE_PORT=10022
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - FRACTAL_URL=http://jarvis-fractal-consciousness:8027
      - SWARM_URL=http://jarvis-swarm-intelligence:8021
      - UPSTREAM_URL=http://jarvis-blood-brain-barrier:8016
      - DOWNSTREAM_URL=http://jarvis-fractal-consciousness:8027
--
    build: { context: ./services, dockerfile: Dockerfile.bridge }
    container_name: jarvis-dgm-bridge-23
    command: python3 bridge_cross_dgm_10023.py
    expose: ["10023"]
    environment:
      - SERVICE_PORT=10023
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - FRACTAL_URL=http://jarvis-fractal-consciousness:8027
      - SWARM_URL=http://jarvis-swarm-intelligence:8021
      - UPSTREAM_URL=http://jarvis-qualia-engine:8017
      - DOWNSTREAM_URL=http://jarvis-swarm-intelligence:8021
--
    build:
      context: .
      dockerfile: Dockerfile.auth_api
    container_name: jarvis-auth-api
    ports:
      - "127.0.0.1:8096:8091"
    expose:
      - "8091"
    environment:
      - SERVICE_PORT=8091
      - REDIS_URL=redis://jarvis-redis:6379
--
    build:
      context: ./services
      dockerfile: Dockerfile.phiprobe
    container_name: jarvis-phi-probe
    ports:
      - "127.0.0.1:8026:8025"
    networks:
      - qualia-net
    volumes:
      - ./services/ms_jarvis_phi_probe.py:/app/ms_jarvis_phi_probe.py:ro
    environment:
--
    build:
      context: ./services
      dockerfile: Dockerfile.rag_server
    container_name: jarvis-rag-router
    command: ["uvicorn", "rag_query_router:app", "--host", "0.0.0.0", "--port", "5001"]
    environment:
      - SERVICE_PORT=5001
      - CHROMA_HOST=172.18.0.2
      - CHROMA_PORT=8000
    ports:
      - "127.0.0.1:5012:5001"
--
  msjarvis-rebuild_jarvis-local-resources-db-data:
    external: true
  hf-model-cache:
    driver: local
secrets:
  jarvisapikey:
    file: .secrets/jarvisapikey.txt

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild$ 

