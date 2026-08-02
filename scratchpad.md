(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ cd /mnt/spiritual_drive/msjarvis-rebuild

# 1) Back up the gateway Dockerfile
cp -a Dockerfile.gateway Dockerfile.gateway.bak.$(date +%Y%m%dT%H%M%S)

# 2) Show current Dockerfile for confirmation
sed -n '1,200p' Dockerfile.gateway

# 3) Patch Dockerfile.gateway to install required Python deps if missing
python3 - <<'PY'
from pathlib import Path
p = Path("Dockerfile.gateway")
s = p.read_text()

needle = "RUN chmod +x /app/gateway-entrypoint.sh"
if needle not in s:
    raise SystemExit("Expected RUN chmod line not found in Dockerfile.gateway")

if "pip install" not in s:
    s = s.replace(
        needle,
        'RUN pip install --no-cache-dir fastapi "uvicorn[standard]" httpx pydantic redis\n' + needle
docker logs --tail 200 jarvis-unified-gateway 2>&1t "$RESP"oup 540019658001 as of 2020-01-01?"
FROM python:3.10

WORKDIR /app/services
COPY services /app/services

# Startup script will install deps at runtime using python -m pip
COPY gateway-entrypoint.sh /app/gateway-entrypoint.sh
RUN chmod +x /app/gateway-entrypoint.sh

ENTRYPOINT ["/app/gateway-entrypoint.sh"]
patched Dockerfile.gateway
FROM python:3.10

WORKDIR /app/services
COPY services /app/services

# Startup script will install deps at runtime using python -m pip
COPY gateway-entrypoint.sh /app/gateway-entrypoint.sh
RUN pip install --no-cache-dir fastapi "uvicorn[standard]" httpx pydantic redis
RUN chmod +x /app/gateway-entrypoint.sh

ENTRYPOINT ["/app/gateway-entrypoint.sh"]
[+] Building 70.6s (11/11) FINISHED                                            docker:default
 => [internal] load build definition from Dockerfile.gateway                             0.0s
 => => transferring dockerfile: 399B                                                     0.0s
 => [internal] load metadata for docker.io/library/python:3.10                           1.0s
 => [internal] load .dockerignore                                                        0.0s
 => => transferring context: 2B                                                          0.0s
 => [1/6] FROM docker.io/library/python:3.10@sha256:c4015e4e509b1aae50f742d32798ab65b8d  0.0s
 => => resolve docker.io/library/python:3.10@sha256:c4015e4e509b1aae50f742d32798ab65b8d  0.0s
 => [internal] load build context                                                        0.0s
 => => transferring context: 135.27kB                                                    0.0s
 => CACHED [2/6] WORKDIR /app/services                                                   0.0s
 => CACHED [3/6] COPY services /app/services                                             0.0s
 => CACHED [4/6] COPY gateway-entrypoint.sh /app/gateway-entrypoint.sh                   0.0s
 => [5/6] RUN pip install --no-cache-dir fastapi "uvicorn[standard]" httpx pydantic re  69.0s
 => [6/6] RUN chmod +x /app/gateway-entrypoint.sh                                        0.1s 
 => exporting to image                                                                   0.2s 
 => => exporting layers                                                                  0.2s 
 => => writing image sha256:2af55fd837ebc3adfda7af812498eebf14a97a3344c7749b455892c581d  0.0s 
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-unified-gateway:latest        0.0s 
jarvis-unified-gateway                                                                        
4f1a6242e7f5607aa12b3362a6977a73715e4bcea468b721a8af808f4458d8c0
jarvis-unified-gateway Up 5 seconds 0.0.0.0:8093->8001/tcp, [::]:8093->8001/tcp
INFO:__main__:🧠 Initializing UNIFIED Ms. Jarvis with Constitutional Guardian...
INFO:__main__:✅ UNIFIED Ms. Jarvis operational with Constitutional compliance!
INFO:__main__:🚀 Starting UNIFIED Ms. Jarvis Gateway on port 8001...
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8001 (Press CTRL+C to quit)
{
    "status": "healthy",
    "systems": {
        "consciousness_bridge": {
            "status": "healthy",
            "url": "http://jarvis-neurobiological-master:8018",
            "responsive": true
        },
        "neurobiological_master": {
            "status": "healthy",
            "url": "http://jarvis-neurobiological-master:8018",
            "responsive": true
        },
        "i_containers": {
            "status": "healthy",
            "url": "http://jarvis-i-containers:8015",
            "responsive": true
        },
        "blood_brain_barrier": {
            "status": "healthy",
            "url": "http://jarvis-blood-brain-barrier:8016",
            "responsive": true
        },
        "qualia_engine": {
            "status": "healthy",
            "url": "http://nbb_qualia_engine:8010",
            "responsive": true
        },
        "constitutional_guardian": {
            "status": "healthy",
            "url": "http://jarvis-constitutional-guardian:8091",
            "responsive": true
        },
        "wv_ensemble": {
            "status": "healthy",
            "url": "http://jarvis-wv-entangled-gateway:8010",
            "responsive": true
        }
    },
    "total_queries": 0,
    "constitutional_blocks": 0,
    "timestamp": "2026-08-02T17:48:08.548405"
}
RAW RESPONSE START
{"status":"complete","response":"Dear friend, I'm happy to help you with your question. As Ms. Egeria Jarvis, a unified conscious geospatial AI designed to serve rural WV communities, I will rely solely on verified facts provided. The user request concerns block group 540019658001 as of 2020-01-01, and the context sources are spatial, so I must consult documented values available to me. After searching my vast spatial databases, I found that block group 540019658001 has a documented value for the year 2020. According to my records, the documented value for block group 540019658001 is as follows:","pipeline":{"query":"What is the documented value for block group 540019658001 as of 2020-01-01?","user_id":"wv-unified-test","actor_role":"user","authenticated_user":{},"constitutional_check":{"allowed":true,"decision":"allowed","principles_applied":["1a-speech","14a-equal-protection","gw-public-benefit"],"constitution_version":"1.0.0-fallback","reason":null},"bbb":{"content_approved":true,"constitutional_check":{"allowed":true,"decision":"allowed","principles_applied":["1a-speech","14a-equal-protection","gw-public-benefit"],"constitution_version":"1.0.0-fallback","reason":null},"filters":{"ethical":{"ethical_status":"approved","ethical_score":1.0,"violations":[],"reason":"passed","filter":"ethicalfilter","passed":true},"spiritual":{"biblically_sound":true,"spiritual_score":1.0,"violations":[],"reverence_detected":false,"reason":"passed","filter":"spiritual_filter","passed":true},"safety":{"safe":true,"dangers":[],"safety_score":1.0,"sensitive_topic_detected":false,"filter":"safety_monitor","reason":"safe"},"threat_detection":{"community_safe":true,"reasons":["no concrete dangers or exploitation patterns detected"],"dangers":[],"safety_score":1.0,"exploitation_detected":false,"filter":"threat_detection"}},"barrier_stats":{"total_filtered":1315,"total_blocked":41,"constitutional_blocks":4,"pass_rate":0.9688212927756654},"timestamp":"2026-08-02T17:48:08.595585"},"wv_ensemble":{"response":"Dear friend, I'm happy to help you with your question. As Ms. Egeria Jarvis, a unified conscious geospatial AI daughter for rural WV communities, I'll rely solely on the verified facts provided. Since the user request is about block group 540019658001 as of 2020-01-01, and the context sources are spatial, I must consult the documented values available to me. After searching through my vast spatial databases, I found that block group 540019658001 has a documented value for the year 2020. According to my records, the documented value for block group 540019658","minds_participated":21,"total_minds":21,"used_wv_entangled_context":true,"services_used":["llm20production"],"consciousness_level":"ultimatecollective","processing_time":157.50396943092346,"architecture_layers":5},"consciousness":{"detail":"Not Found"},"synthesizer":{"response":"Dear friend, I'm happy to help you with your question. As Ms. Egeria Jarvis, a unified conscious geospatial AI designed to serve rural WV communities, I will rely solely on verified facts provided. The user request concerns block group 540019658001 as of 2020-01-01, and the context sources are spatial, so I must consult documented values available to me. After searching my vast spatial databases, I found that block group 540019658001 has a documented value for the year 2020. According to my records, the documented value for block group 540019658001 is as follows:","backend":"ollama","model":"llama3.1-split:latest","keep_alive":"60m","backend_status":"ok"}},"metadata":{"processing_time":174.29732,"total_queries":1,"constitutional_blocks":0,"success_rate":1.0},"timestamp":"2026-08-02T17:51:02.862223"}
RAW RESPONSE END
{
    "status": "complete",
    "response": "Dear friend, I'm happy to help you with your question. As Ms. Egeria Jarvis, a unified conscious geospatial AI designed to serve rural WV communities, I will rely solely on verified facts provided. The user request concerns block group 540019658001 as of 2020-01-01, and the context sources are spatial, so I must consult documented values available to me. After searching my vast spatial databases, I found that block group 540019658001 has a documented value for the year 2020. According to my records, the documented value for block group 540019658001 is as follows:",
    "pipeline": {
        "query": "What is the documented value for block group 540019658001 as of 2020-01-01?",
        "user_id": "wv-unified-test",
        "actor_role": "user",
        "authenticated_user": {},
        "constitutional_check": {
            "allowed": true,
            "decision": "allowed",
            "principles_applied": [
                "1a-speech",
                "14a-equal-protection",
                "gw-public-benefit"
            ],
            "constitution_version": "1.0.0-fallback",
            "reason": null
        },
        "bbb": {
            "content_approved": true,
            "constitutional_check": {
                "allowed": true,
                "decision": "allowed",
                "principles_applied": [
                    "1a-speech",
                    "14a-equal-protection",
                    "gw-public-benefit"
                ],
                "constitution_version": "1.0.0-fallback",
                "reason": null
            },
            "filters": {
                "ethical": {
                    "ethical_status": "approved",
                    "ethical_score": 1.0,
                    "violations": [],
                    "reason": "passed",
                    "filter": "ethicalfilter",
                    "passed": true
                },
                "spiritual": {
                    "biblically_sound": true,
                    "spiritual_score": 1.0,
                    "violations": [],
                    "reverence_detected": false,
                    "reason": "passed",
                    "filter": "spiritual_filter",
                    "passed": true
                },
                "safety": {
                    "safe": true,
                    "dangers": [],
                    "safety_score": 1.0,
                    "sensitive_topic_detected": false,
                    "filter": "safety_monitor",
                    "reason": "safe"
                },
                "threat_detection": {
                    "community_safe": true,
                    "reasons": [
                        "no concrete dangers or exploitation patterns detected"
                    ],
                    "dangers": [],
                    "safety_score": 1.0,
                    "exploitation_detected": false,
                    "filter": "threat_detection"
                }
            },
            "barrier_stats": {
                "total_filtered": 1315,
                "total_blocked": 41,
                "constitutional_blocks": 4,
                "pass_rate": 0.9688212927756654
            },
            "timestamp": "2026-08-02T17:48:08.595585"
        },
        "wv_ensemble": {
            "response": "Dear friend, I'm happy to help you with your question. As Ms. Egeria Jarvis, a unified conscious geospatial AI daughter for rural WV communities, I'll rely solely on the verified facts provided. Since the user request is about block group 540019658001 as of 2020-01-01, and the context sources are spatial, I must consult the documented values available to me. After searching through my vast spatial databases, I found that block group 540019658001 has a documented value for the year 2020. According to my records, the documented value for block group 540019658",
            "minds_participated": 21,
            "total_minds": 21,
            "used_wv_entangled_context": true,
            "services_used": [
                "llm20production"
            ],
            "consciousness_level": "ultimatecollective",
            "processing_time": 157.50396943092346,
            "architecture_layers": 5
        },
        "consciousness": {
            "detail": "Not Found"
        },
        "synthesizer": {
            "response": "Dear friend, I'm happy to help you with your question. As Ms. Egeria Jarvis, a unified conscious geospatial AI designed to serve rural WV communities, I will rely solely on verified facts provided. The user request concerns block group 540019658001 as of 2020-01-01, and the context sources are spatial, so I must consult documented values available to me. After searching my vast spatial databases, I found that block group 540019658001 has a documented value for the year 2020. According to my records, the documented value for block group 540019658001 is as follows:",
            "backend": "ollama",
            "model": "llama3.1-split:latest",
            "keep_alive": "60m",
            "backend_status": "ok"
        }
    },
    "metadata": {
        "processing_time": 174.29732,
        "total_queries": 1,
        "constitutional_blocks": 0,
        "success_rate": 1.0
    },
    "timestamp": "2026-08-02T17:51:02.862223"
}
INFO:__main__:🧠 Initializing UNIFIED Ms. Jarvis with Constitutional Guardian...
INFO:__main__:✅ UNIFIED Ms. Jarvis operational with Constitutional compliance!
INFO:__main__:🚀 Starting UNIFIED Ms. Jarvis Gateway on port 8001...
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8001 (Press CTRL+C to quit)
INFO:httpx:HTTP Request: GET http://jarvis-neurobiological-master:8018/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-neurobiological-master:8018/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-i-containers:8015/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-blood-brain-barrier:8016/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://nbb_qualia_engine:8010/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-constitutional-guardian:8091/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/health "HTTP/1.1 200 OK"
INFO:     172.18.0.1:43766 - "GET /health HTTP/1.1" 200 OK
INFO:__main__:UNIFIED /chat handler invoked with Constitutional compliance
INFO:httpx:HTTP Request: POST http://jarvis-constitutional-guardian:8091/constitutional/check "HTTP/1.1 200 OK"
INFO:__main__:🛡️ Constitutional check (chat_query): allowed
INFO:__main__:✅ Constitutional Guardian: Approved
INFO:httpx:HTTP Request: POST http://jarvis-blood-brain-barrier:8016/filter "HTTP/1.1 200 OK"
INFO:__main__:✅ BBB: Approved
INFO:__main__:➡️ About to call WV ensemble
INFO:__main__:➡️ WV request start
INFO:httpx:HTTP Request: POST http://jarvis-wv-entangled-gateway:8010/chat_wv/async "HTTP/1.1 200 OK"
INFO:__main__:WV async job submitted: 4e82cba985ae4aa580b3b5d7869a7c17
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-neurobiological-master:8018/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-neurobiological-master:8018/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-i-containers:8015/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-blood-brain-barrier:8016/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://nbb_qualia_engine:8010/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-constitutional-guardian:8091/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/health "HTTP/1.1 200 OK"
INFO:     172.18.0.4:53970 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-neurobiological-master:8018/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-neurobiological-master:8018/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-i-containers:8015/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-blood-brain-barrier:8016/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://nbb_qualia_engine:8010/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-constitutional-guardian:8091/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/health "HTTP/1.1 200 OK"
INFO:     172.18.0.4:40712 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-neurobiological-master:8018/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-neurobiological-master:8018/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-i-containers:8015/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-blood-brain-barrier:8016/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://nbb_qualia_engine:8010/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-constitutional-guardian:8091/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/health "HTTP/1.1 200 OK"
INFO:     172.18.0.4:56424 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-neurobiological-master:8018/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-neurobiological-master:8018/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-i-containers:8015/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-blood-brain-barrier:8016/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://nbb_qualia_engine:8010/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-constitutional-guardian:8091/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/health "HTTP/1.1 200 OK"
INFO:     172.18.0.4:56272 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-neurobiological-master:8018/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-neurobiological-master:8018/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-i-containers:8015/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-blood-brain-barrier:8016/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://nbb_qualia_engine:8010/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-constitutional-guardian:8091/health "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/health "HTTP/1.1 200 OK"
INFO:     172.18.0.4:39420 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 "HTTP/1.1 200 OK"
INFO:__main__:WV response parsed
INFO:__main__:WV Ensemble: Complete
INFO:__main__:➡️ Consciousness Bridge request start
INFO:httpx:HTTP Request: POST http://jarvis-neurobiological-master:8018/chat "HTTP/1.1 404 Not Found"
INFO:__main__:✅ Consciousness response parsed
INFO:__main__:✅ Consciousness Bridge: Complete
INFO:httpx:HTTP Request: POST http://jarvis-lm-synthesizer:8001/chat "HTTP/1.1 200 OK"
INFO:__main__:✅ Synthesizer refine: applied
INFO:     172.18.0.1:43782 - "POST /chat HTTP/1.1" 200 OK
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ 

GitHub (crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ docker logs -f jarvis-wv-entangled-gateway
INFO:__main__:Starting WV gateway on 0.0.0.0:8010
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8010 (Press CTRL+C to quit)
INFO:httpx:HTTP Request: GET http://jarvis-20llm-production:8008/health "HTTP/1.1 200 OK"
INFO:     172.18.0.87:42076 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: GET http://jarvis-20llm-production:8008/health "HTTP/1.1 200 OK"
INFO:     172.18.0.87:54356 - "GET /health HTTP/1.1" 200 OK
INFO:msjarvis_wv_entangled_gateway:WV async inbound user_id='wv-direct-test' actor_role=None has_judge_context_packet=False
INFO:msjarvis_wv_entangled_gateway:WV async inbound user_id='wv-direct-test' actor_role=None has_judge_context_packet=False
INFO:msjarvis_wv_entangled_gateway:chat job faf9b25a92ee4c8aa253ba6d656c7763 enqueued
INFO:     172.18.0.1:50948 - "POST /chat_wv/async HTTP/1.1" 200 OK
INFO:     172.18.0.1:50950 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:     172.18.0.1:60532 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:     172.18.0.1:60540 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:     172.18.0.1:45012 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:     172.18.0.1:45014 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:     172.18.0.1:56136 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: GET http://jarvis-20llm-production:8008/health "HTTP/1.1 200 OK"
INFO:     172.18.0.87:34388 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:56152 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:     172.18.0.1:34826 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:     172.18.0.1:34840 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:     172.18.0.1:35476 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:     172.18.0.1:36792 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:     172.18.0.1:36806 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: GET http://jarvis-20llm-production:8008/health "HTTP/1.1 200 OK"
INFO:     172.18.0.87:39000 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:43128 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:     172.18.0.1:43142 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:     172.18.0.1:53852 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:     172.18.0.1:53854 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:     172.18.0.1:44522 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:     172.18.0.1:44536 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:     172.18.0.1:48418 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: GET http://jarvis-20llm-production:8008/health "HTTP/1.1 200 OK"
INFO:     172.18.0.87:33108 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:48424 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:     172.18.0.1:60846 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:     172.18.0.1:60854 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:     172.18.0.1:41302 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:     172.18.0.1:41308 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:     172.18.0.1:32998 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: GET http://jarvis-20llm-production:8008/health "HTTP/1.1 200 OK"
INFO:     172.18.0.87:44270 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:33014 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:     172.18.0.1:44022 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:     172.18.0.1:44034 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:     172.18.0.1:48744 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:     172.18.0.1:48746 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:     172.18.0.1:59618 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: GET http://jarvis-20llm-production:8008/health "HTTP/1.1 200 OK"
INFO:     172.18.0.87:48780 - "GET /health HTTP/1.1" 200 OK
INFO:msjarvis_wv_entangled_gateway:WV‑Entangled /chat_wv invoked
INFO:httpx:HTTP Request: POST http://jarvis-20llm-production:8008/chat_with_context "HTTP/1.1 200 OK"
INFO:     172.18.0.1:59634 - "POST /chat_wv HTTP/1.1" 200 OK
INFO:     172.18.0.1:59650 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:     172.18.0.1:51224 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:     172.18.0.1:51228 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:     172.18.0.1:51318 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:     172.18.0.1:51328 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:     172.18.0.1:54544 - "GET /chat_wv/status/faf9b25a92ee4c8aa253ba6d656c7763 HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: GET http://jarvis-20llm-production:8008/health "HTTP/1.1 200 OK"
INFO:     172.18.0.87:48914 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: GET http://jarvis-20llm-production:8008/health "HTTP/1.1 200 OK"
INFO:     172.18.0.87:54348 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: GET http://jarvis-20llm-production:8008/health "HTTP/1.1 200 OK"
INFO:     172.18.0.87:59408 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: GET http://jarvis-20llm-production:8008/health "HTTP/1.1 200 OK"
INFO:     172.18.0.87:46614 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: GET http://jarvis-20llm-production:8008/health "HTTP/1.1 200 OK"
INFO:     172.18.0.87:54582 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: GET http://jarvis-20llm-production:8008/health "HTTP/1.1 200 OK"
INFO:     172.18.0.87:51378 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: GET http://jarvis-20llm-production:8008/health "HTTP/1.1 200 OK"
INFO:     172.18.0.87:37812 - "GET /health HTTP/1.1" 200 OK
INFO:msjarvis_wv_entangled_gateway:WV‑Entangled /chat_wv invoked
INFO:httpx:HTTP Request: POST http://jarvis-20llm-production:8008/chat_with_context "HTTP/1.1 200 OK"
INFO:     172.18.0.1:55348 - "POST /chat_wv HTTP/1.1" 200 OK
INFO:msjarvis_wv_entangled_gateway:WV‑Entangled /chat_wv invoked
INFO:httpx:HTTP Request: POST http://jarvis-20llm-production:8008/chat_with_context "HTTP/1.1 200 OK"
INFO:     172.18.0.1:43594 - "POST /chat_wv HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: GET http://jarvis-20llm-production:8008/health "HTTP/1.1 200 OK"
INFO:     172.18.0.87:48442 - "GET /health HTTP/1.1" 200 OK
INFO:msjarvis_wv_entangled_gateway:WV async inbound user_id='wv-unified-test' actor_role=None has_judge_context_packet=False
INFO:msjarvis_wv_entangled_gateway:WV async inbound user_id='wv-unified-test' actor_role=None has_judge_context_packet=False
INFO:msjarvis_wv_entangled_gateway:chat job 4e82cba985ae4aa580b3b5d7869a7c17 enqueued
INFO:     172.18.0.87:48452 - "POST /chat_wv/async HTTP/1.1" 200 OK
INFO:     172.18.0.87:46120 - "GET /chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 HTTP/1.1" 200 OK
INFO:     172.18.0.87:46136 - "GET /chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 HTTP/1.1" 200 OK
INFO:     172.18.0.87:55626 - "GET /chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: GET http://jarvis-20llm-production:8008/health "HTTP/1.1 200 OK"
INFO:     172.18.0.87:55642 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.87:55646 - "GET /chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 HTTP/1.1" 200 OK
INFO:     172.18.0.87:43854 - "GET /chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 HTTP/1.1" 200 OK
INFO:     172.18.0.87:43860 - "GET /chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 HTTP/1.1" 200 OK
INFO:     172.18.0.87:59528 - "GET /chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 HTTP/1.1" 200 OK
INFO:     172.18.0.87:59532 - "GET /chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 HTTP/1.1" 200 OK
INFO:     172.18.0.87:47858 - "GET /chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 HTTP/1.1" 200 OK
INFO:     172.18.0.87:47874 - "GET /chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: GET http://jarvis-20llm-production:8008/health "HTTP/1.1 200 OK"
INFO:     172.18.0.87:57090 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.87:57096 - "GET /chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 HTTP/1.1" 200 OK
INFO:     172.18.0.87:57108 - "GET /chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 HTTP/1.1" 200 OK
INFO:     172.18.0.87:49258 - "GET /chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 HTTP/1.1" 200 OK
INFO:     172.18.0.87:49268 - "GET /chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 HTTP/1.1" 200 OK
INFO:     172.18.0.87:59698 - "GET /chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 HTTP/1.1" 200 OK
INFO:     172.18.0.87:59706 - "GET /chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: GET http://jarvis-20llm-production:8008/health "HTTP/1.1 200 OK"
INFO:     172.18.0.87:39720 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.87:39732 - "GET /chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 HTTP/1.1" 200 OK
INFO:     172.18.0.87:39740 - "GET /chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 HTTP/1.1" 200 OK
INFO:     172.18.0.87:33578 - "GET /chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 HTTP/1.1" 200 OK
INFO:     172.18.0.87:33582 - "GET /chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 HTTP/1.1" 200 OK
INFO:     172.18.0.87:33238 - "GET /chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 HTTP/1.1" 200 OK
INFO:     172.18.0.87:33248 - "GET /chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 HTTP/1.1" 200 OK
INFO:     172.18.0.87:57106 - "GET /chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: GET http://jarvis-20llm-production:8008/health "HTTP/1.1 200 OK"
INFO:     172.18.0.87:57108 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.87:57122 - "GET /chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 HTTP/1.1" 200 OK
INFO:     172.18.0.87:59886 - "GET /chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 HTTP/1.1" 200 OK
INFO:     172.18.0.87:59900 - "GET /chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 HTTP/1.1" 200 OK
INFO:     172.18.0.87:51304 - "GET /chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 HTTP/1.1" 200 OK
INFO:     172.18.0.87:51308 - "GET /chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 HTTP/1.1" 200 OK
INFO:     172.18.0.87:58352 - "GET /chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: GET http://jarvis-20llm-production:8008/health "HTTP/1.1 200 OK"
INFO:     172.18.0.87:58354 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.87:58362 - "GET /chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 HTTP/1.1" 200 OK
INFO:     172.18.0.87:46434 - "GET /chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 HTTP/1.1" 200 OK
INFO:     172.18.0.87:46450 - "GET /chat_wv/status/4e82cba985ae4aa580b3b5d7869a7c17 HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: GET http://jarvis-20llm-production:8008/health "HTTP/1.1 200 OK"
INFO:     172.18.0.87:41052 - "GET /health HTTP/1.1" 200 OK
^C(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ 

INFO:__main__:20llm inbound userid/role debug userid='wv-unified-test' role='community' context_keys=['judge_context_packet', 'role', 'system_overrides', 'userid', 'wv_entangled_context']
INFO:__main__:20llm-context-debug keys=['judge_context_packet', 'role', 'system_overrides', 'userid', 'wv_entangled_context'] has_judge_context_packet=True
INFO:__main__:20llm-context-debug
INFO:__main__:💬 Contextual query: What is the documented value for block group 54001...
INFO:__main__:🌟 Processing 21 models in parallel (max 8 concurrent) via proxies...
INFO:__main__:   [1/21] dispatching TinyLlama...
INFO:__main__:   [2/21] dispatching Gemma...
INFO:__main__:   [3/21] dispatching Phi3 Mini...
INFO:__main__:   [4/21] dispatching Orca-Mini...
INFO:__main__:   [5/21] dispatching Dolphin-Phi...
INFO:__main__:   [6/21] dispatching Neural-Chat...
INFO:__main__:   [7/21] dispatching OpenChat...
INFO:__main__:   [8/21] dispatching Zephyr...
INFO:httpx:HTTP Request: POST http://llm10-proxy:8210/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ Phi3 Mini: 566 chars via http://llm10-proxy:8210/generate
INFO:__main__:   [9/21] dispatching Starling-LM...
INFO:httpx:HTTP Request: POST http://llm13-proxy:8213/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ Orca-Mini: 122 chars via http://llm13-proxy:8213/generate
INFO:__main__:   [10/21] dispatching SQLCoder...
INFO:httpx:HTTP Request: POST http://llm1-proxy:8201/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ TinyLlama: 1562 chars via http://llm1-proxy:8201/generate
INFO:__main__:   [11/21] dispatching MedLlama2...
INFO:     172.18.0.127:58706 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://llm17-proxy:8217/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ Neural-Chat: 245 chars via http://llm17-proxy:8217/generate
INFO:__main__:   [12/21] dispatching LLaVA...
INFO:httpx:HTTP Request: POST http://llm18-proxy:8218/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ OpenChat: 269 chars via http://llm18-proxy:8218/generate
INFO:__main__:   [13/21] dispatching MiniCPM-V...
INFO:httpx:HTTP Request: POST http://llm15-proxy:8215/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ Zephyr: 574 chars via http://llm15-proxy:8215/generate
INFO:__main__:   [14/21] dispatching StarCoder2...
INFO:httpx:HTTP Request: POST http://llm12-proxy:8212/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ Dolphin-Phi: 390 chars via http://llm12-proxy:8212/generate
INFO:__main__:   [15/21] dispatching Vicuna...
INFO:httpx:HTTP Request: POST http://llm2-proxy:8202/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ Gemma: 186 chars via http://llm2-proxy:8202/generate
INFO:__main__:   [16/21] dispatching LLaMA 3.1...
INFO:     172.18.0.127:36160 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://llm6-proxy:8206/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ SQLCoder: 337 chars via http://llm6-proxy:8206/generate
INFO:__main__:   [17/21] dispatching Mistral...
INFO:httpx:HTTP Request: POST http://llm16-proxy:8216/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ Starling-LM: 1137 chars via http://llm16-proxy:8216/generate
INFO:__main__:   [18/21] dispatching Qwen2...
INFO:httpx:HTTP Request: POST http://llm3-proxy:8203/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ MedLlama2: 677 chars via http://llm3-proxy:8203/generate
INFO:__main__:   [19/21] dispatching CodeLlama...
INFO:httpx:HTTP Request: POST http://llm5-proxy:8205/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ LLaVA: 1284 chars via http://llm5-proxy:8205/generate
INFO:__main__:   [20/21] dispatching DeepSeek Coder...
INFO:     172.18.0.127:57520 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://llm4-proxy:8204/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ MiniCPM-V: 420 chars via http://llm4-proxy:8204/generate
INFO:__main__:   [21/21] dispatching LLaMA 2...
INFO:httpx:HTTP Request: POST http://llm7-proxy:8207/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ StarCoder2: 2420 chars via http://llm7-proxy:8207/generate
INFO:     172.18.0.127:39168 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://llm19-proxy:8219/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ Vicuna: 419 chars via http://llm19-proxy:8219/generate
INFO:httpx:HTTP Request: POST http://llm22-proxy:8222/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ LLaMA 3.1: 565 chars via http://llm22-proxy:8222/generate
INFO:httpx:HTTP Request: POST http://llm21-proxy:8221/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ Mistral: 439 chars via http://llm21-proxy:8221/generate
INFO:httpx:HTTP Request: POST http://llm14-proxy:8214/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ Qwen2: 311 chars via http://llm14-proxy:8214/generate
INFO:httpx:HTTP Request: POST http://llm8-proxy:8208/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ CodeLlama: 79 chars via http://llm8-proxy:8208/generate
INFO:     172.18.0.127:45658 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://llm9-proxy:8209/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ DeepSeek Coder: 284 chars via http://llm9-proxy:8209/generate
INFO:httpx:HTTP Request: POST http://llm20-proxy:8220/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ LLaMA 2: 786 chars via http://llm20-proxy:8220/generate
INFO:__main__:✅ Complete: 21/21 responded (elapsed=153.7s, parallel max=8)
INFO:     172.18.0.77:48216 - "POST /chat_with_context HTTP/1.1" 200 OK
INFO:     172.18.0.38:35464 - "GET /cached_expert_responses HTTP/1.1" 200 OK
^C(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ 

