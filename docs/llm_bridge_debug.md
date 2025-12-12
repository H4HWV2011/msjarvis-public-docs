# llm_bridge debug and troubleshooting

This document describes the llm_bridge debug endpoints, how main_brain uses the bridge, and how to troubleshoot common Ollama connectivity issues.

## Endpoints and JSON shapes

### Health check

- URL (host): http://localhost:18006/health
- URL (inside docker network): http://jarvis-llm-bridge:8006/health
- Method: GET
- Response (example shape):
  {
    "status": "healthy",
    "role": "llm_bridge_ollama"
  }

### Debug echo

- URL (host): http://localhost:18006/debug/echo
- URL (inside docker network): http://jarvis-llm-bridge:8006/debug/echo
- Method: GET
- Query params:
  - prompt (optional): text to send through the bridge to the default model.
- Response (example shape):
  {
    "info": "Ms. Jarvis llm_bridge debug endpoint",
    "model": "llama3.1:8b",
    "ollama_url": "http://ollama:11434/api/generate",
    "prompt": "test from llm_bridge",
    "response": "..."
  }

These endpoints are intended for manual testing with curl and for automated smoke checks from other services.

## How main_brain calls llm_bridge

When main_brain receives a ULTIMATE request, it orchestrates several phases, including health checks, context gathering, and model generation through llm_bridge.

### Call sequence

1. Phase 1 – Service availability

   main_brain checks health of:
   - http://jarvis-blood-brain-barrier:8016/health
   - http://jarvis-autonomous-learner:8053/health
   - http://jarvis-ollama:11434/api/tags
   - http://jarvis-llm-bridge:8006/health
   - http://jarvis-web-research:8009/health
   - http://jarvis-main-brain:8050/health

2. Phase 1.4 – Blood-Brain Barrier filtering

   - POST http://jarvis-blood-brain-barrier:8016/filter

3. Phase 1.5 – RAG and web context

   - POST http://jarvis-web-research:8009/search

4. Generation via llm_bridge

   - POST http://jarvis-llm-bridge:8006/process

The llm_bridge call returns the model’s generated text, which main_brain then queues for RAG storage.

## Troubleshooting Ollama 404 and /api/tags issues

### 1. Container not running or not exposed

Check running containers and ports:

  docker ps --format "table {{.Names}}\t{{.Image}}\t{{.Ports}}"
  sudo ss -tulnp | grep 11434

If jarvis-ollama is missing or 11434 is not listening, start or restart:

  docker start jarvis-ollama
  # or
  docker restart jarvis-ollama

### 2. Wrong hostname or path inside the network

Ollama should be reachable as http://ollama:11434 inside the Docker network.

From host:

  curl -s http://localhost:11434/api/tags

From a container:

  docker exec -it jarvis-llm-bridge curl -s http://ollama:11434/api/tags

If these fail, fix the hostname (ollama, not localhost) and paths (/api/generate, /api/tags) in llm_bridge config.

### 3. No models returned from /api/tags

Check tags:

  curl -s http://localhost:11434/api/tags

If the expected model (for example llama3.1:8b) is missing, pull it:

  ollama pull llama3.1:8b

Then restart jarvis-ollama and re-check /api/tags.

### 4. Bridging and health debug checklist

From the host:

  curl -s http://localhost:8051/health || echo "main-brain unreachable"
  curl -s http://localhost:18006/health || echo "llmbridge host-port unreachable"
  curl -s http://localhost:8016/health || echo "BBB host-port unreachable"
  curl -s http://localhost:18009/health || echo "webresearch host-port unreachable"
  curl -s http://localhost:11434/api/tags || echo "ollama host-port unreachable"

Exercise llm_bridge debug:

  curl -s "http://localhost:18006/debug/echo"
  curl -s "http://localhost:18006/debug/echo?prompt=test+from+llm_bridge"

If these succeed but main_brain still has issues, inspect:

  docker logs -f jarvis-main-brain

to see which phase and service is failing.
