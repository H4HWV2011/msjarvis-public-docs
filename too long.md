(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ cd ~/msjarvis-rebuild-working/msjarvis-rebuild

# Check for any /chat_with_context or jarvis-20llm-production references
grep -n "chat_with_context" services/ms_jarvis_autonomous_learner_optimized.py || echo "no chat_with_context in learner"
grep -n "jarvis-20llm-production" services/ms_jarvis_autonomous_learner_optimized.py || echo "no 20llm in learner"

# Confirm WEB_URL env is Ollama chat
grep -n "WEB_URL" docker-compose.yml
no chat_with_context in learner
no 20llm in learner
800:    - WEB_URL=http://jarvis-ollama:11434/api/chat
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ docker compose build jarvis-autonomous-learner
docker compose up -d jarvis-autonomous-learner

sleep 5
docker compose ps jarvis-autonomous-learner
[+] Building 0.5s (14/14) FINISHED                                             
 => [internal] load local bake definitions                                0.0s
 => => reading from stdin 691B                                            0.0s
 => [internal] load build definition from Dockerfile.autonomous_learner   0.0s
 => => transferring dockerfile: 726B                                      0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim       0.0s
 => [internal] load .dockerignore                                         0.0s
 => => transferring context: 2B                                           0.0s
 => [1/7] FROM docker.io/library/python:3.11-slim                         0.0s
 => [internal] load build context                                         0.0s
 => => transferring context: 105B                                         0.0s
 => CACHED [2/7] WORKDIR /app                                             0.0s
 => CACHED [3/7] RUN apt-get update && apt-get install -y build-essentia  0.0s
 => CACHED [4/7] RUN pip install --no-cache-dir     fastapi uvicorn http  0.0s
 => CACHED [5/7] RUN python3 -c "from sentence_transformers import Sente  0.0s
 => CACHED [6/7] COPY topic_entanglement.py topic_entanglement.py         0.0s
 => CACHED [7/7] COPY ms_jarvis_autonomous_learner_optimized.py ms_jarvi  0.0s
 => exporting to image                                                    0.0s
 => => exporting layers                                                   0.0s
 => => writing image sha256:2c8818b6cf86db1dfac93a3f41ff0b53d7d67ed1dde4  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-autonomous-le  0.0s
 => resolving provenance for metadata file                                0.0s
[+] build 1/1
 ✔ Image msjarvis-rebuild-jarvis-autonomous-learner Built                  0.6s
[+] up 2/2
 ✔ Container jarvis-chroma             Running                             0.0s
 ✔ Container jarvis-autonomous-learner Running                             0.0s
NAME                        IMAGE                                        COMMAND                  SERVICE                     CREATED         STATUS         PORTS
jarvis-autonomous-learner   msjarvis-rebuild-jarvis-autonomous-learner   "uvicorn ms_jarvis_a…"   jarvis-autonomous-learner   5 minutes ago   Up 5 minutes   127.0.0.1:8020->8020/tcp
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ docker logs jarvis-autonomous-learner | tail -n 40
docker logs jarvis-ollama | tail -n 20
docker logs jarvis-20llm-production | tail -n 20
2026-03-27 00:55:27,326 - INFO - Use pytorch device_name: cpu
2026-03-27 00:55:27,326 - INFO - Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Loading weights: 100%|██████████| 103/103 [00:00<00:00, 3005.21it/s]
BertModel LOAD REPORT from: sentence-transformers/all-MiniLM-L6-v2
Key                     | Status     |  | 
------------------------+------------+--+-
embeddings.position_ids | UNEXPECTED |  | 

Notes:
- UNEXPECTED	:can be ignored when loading from different task/architecture; not ok if you expect identical arch.
2026-03-27 00:55:27,844 - INFO - HTTP Request: GET http://jarvis-chroma:8000/api/v2/auth/identity "HTTP/1.1 200 OK"
2026-03-27 00:55:27,872 - INFO - HTTP Request: GET http://jarvis-chroma:8000/api/v2/tenants/default_tenant "HTTP/1.1 200 OK"
2026-03-27 00:55:27,875 - INFO - HTTP Request: GET http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database "HTTP/1.1 200 OK"
2026-03-27 00:55:27,877 - INFO - HTTP Request: GET http://jarvis-chroma:8000/api/v2/heartbeat "HTTP/1.1 200 OK"
2026-03-27 00:55:27,885 - INFO - HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections "HTTP/1.1 200 OK"
2026-03-27 00:55:27,890 - INFO - HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections "HTTP/1.1 200 OK"
2026-03-27 00:55:27,891 - INFO - ✅ ChromaDB connected - Optimized learning storage ready
INFO:     Started server process [1]
INFO:     Waiting for application startup.
2026-03-27 00:55:27,894 - INFO - 🧠 Optimized Autonomous Learning STARTED
2026-03-27 00:55:27,894 - INFO -    ✅ Semantic deduplication enabled
2026-03-27 00:55:27,894 - INFO -    ✅ Automatic summarization enabled
2026-03-27 00:55:27,894 - INFO -    ✅ Periodic cleanup enabled (every 24h)
2026-03-27 00:55:27,894 - INFO - 🧠 LEARNING CYCLE #1 - Uptime: 0d 0h 0m
2026-03-27 00:55:27,894 - INFO -    Topic: MountainShares smart contract security best practices
2026-03-27 00:55:27,894 - INFO -    Stats: Stored=0, Deduped=0
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8020 (Press CTRL+C to quit)
2026-03-27 00:55:28,928 - INFO - HTTP Request: POST http://jarvis-rag-server:8003/query "HTTP/1.1 200 OK"
2026-03-27 00:56:28,936 - ERROR - ❌ Web research error: 
2026-03-27 00:56:28,936 - INFO - 🔍 Researched: MountainShares smart contract security best practices - RAG=0 results, Web=0 results
2026-03-27 00:56:28,936 - INFO - 💡 Cycle complete - Next in 5 minutes
[DEBUG] WEB_URL in learner: http://jarvis-ollama:11434/api/chat
time=2026-03-26T22:59:47.546Z level=INFO source=routes.go:1663 msg="server config" env="map[CUDA_VISIBLE_DEVICES: GGML_VK_VISIBLE_DEVICES: GPU_DEVICE_ORDINAL: HIP_VISIBLE_DEVICES: HSA_OVERRIDE_GFX_VERSION: HTTPS_PROXY: HTTP_PROXY: NO_PROXY: OLLAMA_CONTEXT_LENGTH:0 OLLAMA_DEBUG:INFO OLLAMA_EDITOR: OLLAMA_FLASH_ATTENTION:false OLLAMA_GPU_OVERHEAD:0 OLLAMA_HOST:http://0.0.0.0:11434 OLLAMA_KEEP_ALIVE:5m0s OLLAMA_KV_CACHE_TYPE: OLLAMA_LLM_LIBRARY: OLLAMA_LOAD_TIMEOUT:5m0s OLLAMA_MAX_LOADED_MODELS:0 OLLAMA_MAX_QUEUE:512 OLLAMA_MODELS:/root/.ollama/models OLLAMA_MULTIUSER_CACHE:false OLLAMA_NEW_ENGINE:false OLLAMA_NOHISTORY:false OLLAMA_NOPRUNE:false OLLAMA_NO_CLOUD:false OLLAMA_NUM_PARALLEL:1 OLLAMA_ORIGINS:[http://localhost https://localhost http://localhost:* https://localhost:* http://127.0.0.1 https://127.0.0.1 http://127.0.0.1:* https://127.0.0.1:* http://0.0.0.0 https://0.0.0.0 http://0.0.0.0:* https://0.0.0.0:* app://* file://* tauri://* vscode-webview://* vscode-file://*] OLLAMA_REMOTES:[ollama.com] OLLAMA_SCHED_SPREAD:false OLLAMA_VULKAN:false ROCR_VISIBLE_DEVICES: http_proxy: https_proxy: no_proxy:]"
time=2026-03-26T22:59:47.546Z level=INFO source=routes.go:1665 msg="Ollama cloud disabled: false"
time=2026-03-26T22:59:47.557Z level=INFO source=images.go:473 msg="total blobs: 120"
time=2026-03-26T22:59:47.561Z level=INFO source=images.go:480 msg="total unused blobs removed: 0"
time=2026-03-26T22:59:47.563Z level=INFO source=routes.go:1718 msg="Listening on [::]:11434 (version 0.16.3)"
time=2026-03-26T22:59:47.564Z level=INFO source=runner.go:67 msg="discovering available GPUs..."
time=2026-03-26T22:59:47.565Z level=INFO source=server.go:431 msg="starting runner" cmd="/usr/bin/ollama runner --ollama-engine --port 39505"
time=2026-03-26T22:59:47.627Z level=INFO source=server.go:431 msg="starting runner" cmd="/usr/bin/ollama runner --ollama-engine --port 37483"
time=2026-03-26T22:59:47.677Z level=INFO source=runner.go:106 msg="experimental Vulkan support disabled.  To enable, set OLLAMA_VULKAN=1"
time=2026-03-26T22:59:47.678Z level=INFO source=types.go:60 msg="inference compute" id=cpu library=cpu compute="" name=cpu description=cpu libdirs=ollama driver="" pci_id="" type="" total="24.0 GiB" available="24.0 GiB"
time=2026-03-26T22:59:47.678Z level=INFO source=routes.go:1768 msg="vram-based default context" total_vram="0 B" default_num_ctx=4096
time=2026-03-26T23:40:07.844Z level=WARN source=server.go:209 msg="flash attention enabled but not supported by model"
time=2026-03-26T23:40:07.844Z level=INFO source=server.go:431 msg="starting runner" cmd="/usr/bin/ollama runner --ollama-engine --model /root/.ollama/models/blobs/sha256-797b70c4edf85907fe0a49eb85811256f65fa0f7bf52166b147fd16be2be4662 --port 45233"
time=2026-03-26T23:40:07.845Z level=INFO source=sched.go:491 msg="system memory" total="24.0 GiB" free="24.0 GiB" free_swap="8.0 GiB"
time=2026-03-26T23:40:07.845Z level=INFO source=server.go:757 msg="loading model" "model layers"=7 requested=-1
time=2026-03-26T23:40:07.870Z level=INFO source=runner.go:1411 msg="starting ollama engine"
time=2026-03-26T23:40:07.871Z level=INFO source=runner.go:1446 msg="Server listening on 127.0.0.1:45233"
time=2026-03-26T23:40:07.879Z level=INFO source=runner.go:1284 msg=load request="{Operation:fit LoraPath:[] Parallel:1 BatchSize:256 FlashAttention:Disabled KvSize:256 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-26T23:40:07.891Z level=INFO source=ggml.go:136 msg="" architecture=bert file_type=F16 name=all-MiniLM-L6-v2 description="" num_tensors=101 num_key_values=24
load_backend: loaded CPU backend from /usr/lib/ollama/libggml-cpu-alderlake.so
time=2026-03-26T23:40:07.904Z level=INFO source=ggml.go:104 msg=system CPU.0.SSE3=1 CPU.0.SSSE3=1 CPU.0.AVX=1 CPU.0.AVX_VNNI=1 CPU.0.AVX2=1 CPU.0.F16C=1 CPU.0.FMA=1 CPU.0.BMI2=1 CPU.0.LLAMAFILE=1 CPU.1.LLAMAFILE=1 compiler=cgo(gcc)
time=2026-03-26T23:40:07.910Z level=INFO source=runner.go:1284 msg=load request="{Operation:alloc LoraPath:[] Parallel:1 BatchSize:256 FlashAttention:Disabled KvSize:256 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-26T23:40:07.926Z level=INFO source=runner.go:1284 msg=load request="{Operation:commit LoraPath:[] Parallel:1 BatchSize:256 FlashAttention:Disabled KvSize:256 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-26T23:40:07.926Z level=INFO source=ggml.go:482 msg="offloading 0 repeating layers to GPU"
time=2026-03-26T23:40:07.926Z level=INFO source=ggml.go:486 msg="offloading output layer to CPU"
time=2026-03-26T23:40:07.926Z level=INFO source=ggml.go:494 msg="offloaded 0/7 layers to GPU"
time=2026-03-26T23:40:07.926Z level=INFO source=device.go:245 msg="model weights" device=CPU size="65.5 MiB"
time=2026-03-26T23:40:07.926Z level=INFO source=device.go:267 msg="compute graph" device=CPU size="4.9 MiB"
time=2026-03-26T23:40:07.926Z level=INFO source=device.go:272 msg="total memory" size="70.3 MiB"
time=2026-03-26T23:40:07.927Z level=INFO source=sched.go:566 msg="loaded runners" count=1
time=2026-03-26T23:40:07.927Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-26T23:40:07.930Z level=INFO source=server.go:1384 msg="waiting for server to become available" status="llm server loading model"
time=2026-03-26T23:40:08.182Z level=INFO source=server.go:1388 msg="llama runner started in 0.34 seconds"
time=2026-03-27T00:19:25.238Z level=WARN source=server.go:209 msg="flash attention enabled but not supported by model"
time=2026-03-27T00:19:25.239Z level=INFO source=server.go:431 msg="starting runner" cmd="/usr/bin/ollama runner --ollama-engine --model /root/.ollama/models/blobs/sha256-797b70c4edf85907fe0a49eb85811256f65fa0f7bf52166b147fd16be2be4662 --port 40751"
time=2026-03-27T00:19:25.239Z level=INFO source=sched.go:491 msg="system memory" total="24.0 GiB" free="23.9 GiB" free_swap="8.0 GiB"
time=2026-03-27T00:19:25.239Z level=INFO source=server.go:757 msg="loading model" "model layers"=7 requested=-1
time=2026-03-27T00:19:25.268Z level=INFO source=runner.go:1411 msg="starting ollama engine"
time=2026-03-27T00:19:25.269Z level=INFO source=runner.go:1446 msg="Server listening on 127.0.0.1:40751"
time=2026-03-27T00:19:25.273Z level=INFO source=runner.go:1284 msg=load request="{Operation:fit LoraPath:[] Parallel:1 BatchSize:256 FlashAttention:Disabled KvSize:256 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:19:25.286Z level=INFO source=ggml.go:136 msg="" architecture=bert file_type=F16 name=all-MiniLM-L6-v2 description="" num_tensors=101 num_key_values=24
load_backend: loaded CPU backend from /usr/lib/ollama/libggml-cpu-alderlake.so
time=2026-03-27T00:19:25.298Z level=INFO source=ggml.go:104 msg=system CPU.0.SSE3=1 CPU.0.SSSE3=1 CPU.0.AVX=1 CPU.0.AVX_VNNI=1 CPU.0.AVX2=1 CPU.0.F16C=1 CPU.0.FMA=1 CPU.0.BMI2=1 CPU.0.LLAMAFILE=1 CPU.1.LLAMAFILE=1 compiler=cgo(gcc)
time=2026-03-27T00:19:25.303Z level=INFO source=runner.go:1284 msg=load request="{Operation:alloc LoraPath:[] Parallel:1 BatchSize:256 FlashAttention:Disabled KvSize:256 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:19:25.321Z level=INFO source=runner.go:1284 msg=load request="{Operation:commit LoraPath:[] Parallel:1 BatchSize:256 FlashAttention:Disabled KvSize:256 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:19:25.321Z level=INFO source=device.go:245 msg="model weights" device=CPU size="65.5 MiB"
time=2026-03-27T00:19:25.321Z level=INFO source=device.go:267 msg="compute graph" device=CPU size="4.9 MiB"
time=2026-03-27T00:19:25.321Z level=INFO source=ggml.go:482 msg="offloading 0 repeating layers to GPU"
time=2026-03-27T00:19:25.321Z level=INFO source=ggml.go:486 msg="offloading output layer to CPU"
time=2026-03-27T00:19:25.321Z level=INFO source=ggml.go:494 msg="offloaded 0/7 layers to GPU"
time=2026-03-27T00:19:25.321Z level=INFO source=device.go:272 msg="total memory" size="70.3 MiB"
time=2026-03-27T00:19:25.321Z level=INFO source=sched.go:566 msg="loaded runners" count=1
time=2026-03-27T00:19:25.321Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:19:25.322Z level=INFO source=server.go:1384 msg="waiting for server to become available" status="llm server loading model"
time=2026-03-27T00:19:25.573Z level=INFO source=server.go:1388 msg="llama runner started in 0.33 seconds"
time=2026-03-27T00:34:54.421Z level=WARN source=server.go:209 msg="flash attention enabled but not supported by model"
time=2026-03-27T00:34:54.422Z level=INFO source=server.go:431 msg="starting runner" cmd="/usr/bin/ollama runner --ollama-engine --model /root/.ollama/models/blobs/sha256-797b70c4edf85907fe0a49eb85811256f65fa0f7bf52166b147fd16be2be4662 --port 38721"
time=2026-03-27T00:34:54.422Z level=INFO source=sched.go:491 msg="system memory" total="24.0 GiB" free="23.9 GiB" free_swap="8.0 GiB"
time=2026-03-27T00:34:54.422Z level=INFO source=server.go:757 msg="loading model" "model layers"=7 requested=-1
time=2026-03-27T00:34:54.449Z level=INFO source=runner.go:1411 msg="starting ollama engine"
time=2026-03-27T00:34:54.450Z level=INFO source=runner.go:1446 msg="Server listening on 127.0.0.1:38721"
time=2026-03-27T00:34:54.457Z level=INFO source=runner.go:1284 msg=load request="{Operation:fit LoraPath:[] Parallel:1 BatchSize:256 FlashAttention:Disabled KvSize:256 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:34:54.471Z level=INFO source=ggml.go:136 msg="" architecture=bert file_type=F16 name=all-MiniLM-L6-v2 description="" num_tensors=101 num_key_values=24
load_backend: loaded CPU backend from /usr/lib/ollama/libggml-cpu-alderlake.so
time=2026-03-27T00:34:54.483Z level=INFO source=ggml.go:104 msg=system CPU.0.SSE3=1 CPU.0.SSSE3=1 CPU.0.AVX=1 CPU.0.AVX_VNNI=1 CPU.0.AVX2=1 CPU.0.F16C=1 CPU.0.FMA=1 CPU.0.BMI2=1 CPU.0.LLAMAFILE=1 CPU.1.LLAMAFILE=1 compiler=cgo(gcc)
time=2026-03-27T00:34:54.488Z level=INFO source=runner.go:1284 msg=load request="{Operation:alloc LoraPath:[] Parallel:1 BatchSize:256 FlashAttention:Disabled KvSize:256 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:34:54.504Z level=INFO source=runner.go:1284 msg=load request="{Operation:commit LoraPath:[] Parallel:1 BatchSize:256 FlashAttention:Disabled KvSize:256 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:34:54.505Z level=INFO source=device.go:245 msg="model weights" device=CPU size="65.5 MiB"
time=2026-03-27T00:34:54.505Z level=INFO source=device.go:267 msg="compute graph" device=CPU size="4.9 MiB"
time=2026-03-27T00:34:54.505Z level=INFO source=device.go:272 msg="total memory" size="70.3 MiB"
time=2026-03-27T00:34:54.505Z level=INFO source=sched.go:566 msg="loaded runners" count=1
time=2026-03-27T00:34:54.505Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:34:54.505Z level=INFO source=ggml.go:482 msg="offloading 0 repeating layers to GPU"
time=2026-03-27T00:34:54.505Z level=INFO source=ggml.go:486 msg="offloading output layer to CPU"
time=2026-03-27T00:34:54.505Z level=INFO source=ggml.go:494 msg="offloaded 0/7 layers to GPU"
time=2026-03-27T00:34:54.505Z level=INFO source=server.go:1384 msg="waiting for server to become available" status="llm server loading model"
time=2026-03-27T00:34:54.757Z level=INFO source=server.go:1388 msg="llama runner started in 0.33 seconds"
llama_model_loader: loaded meta data with 23 key-value pairs and 201 tensors from /root/.ollama/models/blobs/sha256-2af3b81862c6be03c769683af18efdadb2c33f60ff32ab6f83e42c043d6c7816 (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = TinyLlama
llama_model_loader: - kv   2:                       llama.context_length u32              = 2048
llama_model_loader: - kv   3:                     llama.embedding_length u32              = 2048
llama_model_loader: - kv   4:                          llama.block_count u32              = 22
llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 5632
llama_model_loader: - kv   6:                 llama.rope.dimension_count u32              = 64
llama_model_loader: - kv   7:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv   8:              llama.attention.head_count_kv u32              = 4
llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  10:                       llama.rope.freq_base f32              = 10000.000000
llama_model_loader: - kv  11:                          general.file_type u32              = 2
llama_model_loader: - kv  12:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  13:                      tokenizer.ggml.tokens arr[str,32000]   = ["<unk>", "<s>", "</s>", "<0x00>", "<...
llama_model_loader: - kv  14:                      tokenizer.ggml.scores arr[f32,32000]   = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  15:                  tokenizer.ggml.token_type arr[i32,32000]   = [2, 3, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, ...
llama_model_loader: - kv  16:                      tokenizer.ggml.merges arr[str,61249]   = ["▁ t", "e r", "i n", "▁ a", "e n...
llama_model_loader: - kv  17:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  18:                tokenizer.ggml.eos_token_id u32              = 2
llama_model_loader: - kv  19:            tokenizer.ggml.unknown_token_id u32              = 0
llama_model_loader: - kv  20:            tokenizer.ggml.padding_token_id u32              = 2
llama_model_loader: - kv  21:                    tokenizer.chat_template str              = {% for message in messages %}\n{% if m...
llama_model_loader: - kv  22:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   45 tensors
llama_model_loader: - type q4_0:  155 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 606.53 MiB (4.63 BPW) 
load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
load: printing all EOG tokens:
load:   - 2 ('</s>')
load: special tokens cache size = 3
load: token to piece cache size = 0.1684 MB
print_info: arch             = llama
print_info: vocab_only       = 1
print_info: no_alloc         = 0
print_info: model type       = ?B
print_info: model params     = 1.10 B
print_info: general.name     = TinyLlama
print_info: vocab type       = SPM
print_info: n_vocab          = 32000
print_info: n_merges         = 0
print_info: BOS token        = 1 '<s>'
print_info: EOS token        = 2 '</s>'
print_info: UNK token        = 0 '<unk>'
print_info: PAD token        = 2 '</s>'
print_info: LF token         = 13 '<0x0A>'
print_info: EOG token        = 2 '</s>'
print_info: max token length = 48
llama_model_load: vocab only - skipping tensors
time=2026-03-27T00:42:11.008Z level=WARN source=server.go:169 msg="requested context size too large for model" num_ctx=4096 n_ctx_train=2048
time=2026-03-27T00:42:11.009Z level=INFO source=server.go:431 msg="starting runner" cmd="/usr/bin/ollama runner --model /root/.ollama/models/blobs/sha256-2af3b81862c6be03c769683af18efdadb2c33f60ff32ab6f83e42c043d6c7816 --port 46861"
time=2026-03-27T00:42:11.009Z level=INFO source=sched.go:491 msg="system memory" total="24.0 GiB" free="23.8 GiB" free_swap="8.0 GiB"
time=2026-03-27T00:42:11.009Z level=INFO source=server.go:498 msg="loading model" "model layers"=23 requested=-1
time=2026-03-27T00:42:11.010Z level=INFO source=device.go:245 msg="model weights" device=CPU size="571.4 MiB"
time=2026-03-27T00:42:11.010Z level=INFO source=device.go:256 msg="kv cache" device=CPU size="44.0 MiB"
time=2026-03-27T00:42:11.010Z level=INFO source=device.go:272 msg="total memory" size="615.4 MiB"
time=2026-03-27T00:42:11.034Z level=INFO source=runner.go:965 msg="starting go runner"
load_backend: loaded CPU backend from /usr/lib/ollama/libggml-cpu-alderlake.so
time=2026-03-27T00:42:11.047Z level=INFO source=ggml.go:104 msg=system CPU.0.SSE3=1 CPU.0.SSSE3=1 CPU.0.AVX=1 CPU.0.AVX_VNNI=1 CPU.0.AVX2=1 CPU.0.F16C=1 CPU.0.FMA=1 CPU.0.BMI2=1 CPU.0.LLAMAFILE=1 CPU.1.LLAMAFILE=1 compiler=cgo(gcc)
time=2026-03-27T00:42:11.048Z level=INFO source=runner.go:1001 msg="Server listening on 127.0.0.1:46861"
time=2026-03-27T00:42:11.055Z level=INFO source=runner.go:895 msg=load request="{Operation:commit LoraPath:[] Parallel:1 BatchSize:512 FlashAttention:Auto KvSize:2048 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:42:11.055Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:42:11.055Z level=INFO source=server.go:1384 msg="waiting for server to become available" status="llm server loading model"
llama_model_loader: loaded meta data with 23 key-value pairs and 201 tensors from /root/.ollama/models/blobs/sha256-2af3b81862c6be03c769683af18efdadb2c33f60ff32ab6f83e42c043d6c7816 (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = TinyLlama
llama_model_loader: - kv   2:                       llama.context_length u32              = 2048
llama_model_loader: - kv   3:                     llama.embedding_length u32              = 2048
llama_model_loader: - kv   4:                          llama.block_count u32              = 22
llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 5632
llama_model_loader: - kv   6:                 llama.rope.dimension_count u32              = 64
llama_model_loader: - kv   7:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv   8:              llama.attention.head_count_kv u32              = 4
llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  10:                       llama.rope.freq_base f32              = 10000.000000
llama_model_loader: - kv  11:                          general.file_type u32              = 2
llama_model_loader: - kv  12:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  13:                      tokenizer.ggml.tokens arr[str,32000]   = ["<unk>", "<s>", "</s>", "<0x00>", "<...
llama_model_loader: - kv  14:                      tokenizer.ggml.scores arr[f32,32000]   = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  15:                  tokenizer.ggml.token_type arr[i32,32000]   = [2, 3, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, ...
llama_model_loader: - kv  16:                      tokenizer.ggml.merges arr[str,61249]   = ["▁ t", "e r", "i n", "▁ a", "e n...
llama_model_loader: - kv  17:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  18:                tokenizer.ggml.eos_token_id u32              = 2
llama_model_loader: - kv  19:            tokenizer.ggml.unknown_token_id u32              = 0
llama_model_loader: - kv  20:            tokenizer.ggml.padding_token_id u32              = 2
llama_model_loader: - kv  21:                    tokenizer.chat_template str              = {% for message in messages %}\n{% if m...
llama_model_loader: - kv  22:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   45 tensors
llama_model_loader: - type q4_0:  155 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 606.53 MiB (4.63 BPW) 
load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
load: printing all EOG tokens:
load:   - 2 ('</s>')
load: special tokens cache size = 3
load: token to piece cache size = 0.1684 MB
print_info: arch             = llama
print_info: vocab_only       = 0
print_info: no_alloc         = 0
print_info: n_ctx_train      = 2048
print_info: n_embd           = 2048
print_info: n_embd_inp       = 2048
print_info: n_layer          = 22
print_info: n_head           = 32
print_info: n_head_kv        = 4
print_info: n_rot            = 64
print_info: n_swa            = 0
print_info: is_swa_any       = 0
print_info: n_embd_head_k    = 64
print_info: n_embd_head_v    = 64
print_info: n_gqa            = 8
print_info: n_embd_k_gqa     = 256
print_info: n_embd_v_gqa     = 256
print_info: f_norm_eps       = 0.0e+00
print_info: f_norm_rms_eps   = 1.0e-05
print_info: f_clamp_kqv      = 0.0e+00
print_info: f_max_alibi_bias = 0.0e+00
print_info: f_logit_scale    = 0.0e+00
print_info: f_attn_scale     = 0.0e+00
print_info: n_ff             = 5632
print_info: n_expert         = 0
print_info: n_expert_used    = 0
print_info: n_expert_groups  = 0
print_info: n_group_used     = 0
print_info: causal attn      = 1
print_info: pooling type     = 0
print_info: rope type        = 0
print_info: rope scaling     = linear
print_info: freq_base_train  = 10000.0
print_info: freq_scale_train = 1
print_info: n_ctx_orig_yarn  = 2048
print_info: rope_yarn_log_mul= 0.0000
print_info: rope_finetuned   = unknown
print_info: model type       = 1B
print_info: model params     = 1.10 B
print_info: general.name     = TinyLlama
print_info: vocab type       = SPM
print_info: n_vocab          = 32000
print_info: n_merges         = 0
print_info: BOS token        = 1 '<s>'
print_info: EOS token        = 2 '</s>'
print_info: UNK token        = 0 '<unk>'
print_info: PAD token        = 2 '</s>'
print_info: LF token         = 13 '<0x0A>'
print_info: EOG token        = 2 '</s>'
print_info: max token length = 48
load_tensors: loading model tensors, this can take a while... (mmap = false)
load_tensors:          CPU model buffer size =   606.53 MiB
llama_context: constructing llama_context
llama_context: n_seq_max     = 1
llama_context: n_ctx         = 2048
llama_context: n_ctx_seq     = 2048
llama_context: n_batch       = 512
llama_context: n_ubatch      = 512
llama_context: causal_attn   = 1
llama_context: flash_attn    = auto
llama_context: kv_unified    = false
llama_context: freq_base     = 10000.0
llama_context: freq_scale    = 1
llama_context:        CPU  output buffer size =     0.13 MiB
llama_kv_cache:        CPU KV buffer size =    44.00 MiB
llama_kv_cache: size =   44.00 MiB (  2048 cells,  22 layers,  1/1 seqs), K (f16):   22.00 MiB, V (f16):   22.00 MiB
llama_context: Flash Attention was auto, set to enabled
llama_context:        CPU compute buffer size =    66.50 MiB
llama_context: graph nodes  = 689
llama_context: graph splits = 1
time=2026-03-27T00:42:12.060Z level=INFO source=server.go:1388 msg="llama runner started in 1.05 seconds"
time=2026-03-27T00:42:12.060Z level=INFO source=sched.go:566 msg="loaded runners" count=2
time=2026-03-27T00:42:12.060Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:42:12.060Z level=INFO source=server.go:1388 msg="llama runner started in 1.05 seconds"
llama_model_loader: loaded meta data with 21 key-value pairs and 164 tensors from /root/.ollama/models/blobs/sha256-c1864a5eb19305c40519da12cc543519e48a0697ecd30e15d5ac228644957d12 (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = gemma
llama_model_loader: - kv   1:                               general.name str              = gemma-2b-it
llama_model_loader: - kv   2:                       gemma.context_length u32              = 8192
llama_model_loader: - kv   3:                          gemma.block_count u32              = 18
llama_model_loader: - kv   4:                     gemma.embedding_length u32              = 2048
llama_model_loader: - kv   5:                  gemma.feed_forward_length u32              = 16384
llama_model_loader: - kv   6:                 gemma.attention.head_count u32              = 8
llama_model_loader: - kv   7:              gemma.attention.head_count_kv u32              = 1
llama_model_loader: - kv   8:                 gemma.attention.key_length u32              = 256
llama_model_loader: - kv   9:               gemma.attention.value_length u32              = 256
llama_model_loader: - kv  10:     gemma.attention.layer_norm_rms_epsilon f32              = 0.000001
llama_model_loader: - kv  11:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  12:                tokenizer.ggml.bos_token_id u32              = 2
llama_model_loader: - kv  13:                tokenizer.ggml.eos_token_id u32              = 1
llama_model_loader: - kv  14:            tokenizer.ggml.padding_token_id u32              = 0
llama_model_loader: - kv  15:            tokenizer.ggml.unknown_token_id u32              = 3
llama_model_loader: - kv  16:                      tokenizer.ggml.tokens arr[str,256128]  = ["<pad>", "<eos>", "<bos>", "<unk>", ...
llama_model_loader: - kv  17:                      tokenizer.ggml.scores arr[f32,256128]  = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  18:                  tokenizer.ggml.token_type arr[i32,256128]  = [3, 3, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, ...
llama_model_loader: - kv  19:               general.quantization_version u32              = 2
llama_model_loader: - kv  20:                          general.file_type u32              = 2
llama_model_loader: - type  f32:   37 tensors
llama_model_loader: - type q4_0:  126 tensors
llama_model_loader: - type q8_0:    1 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 1.56 GiB (5.34 BPW) 
load: control-looking token:    107 '<end_of_turn>' was not control-type; this is probably a bug in the model. its type will be overridden
load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
load: printing all EOG tokens:
load:   - 1 ('<eos>')
load:   - 107 ('<end_of_turn>')
load: special tokens cache size = 5
load: token to piece cache size = 1.6014 MB
print_info: arch             = gemma
print_info: vocab_only       = 1
print_info: no_alloc         = 0
print_info: model type       = ?B
print_info: model params     = 2.51 B
print_info: general.name     = gemma-2b-it
print_info: vocab type       = SPM
print_info: n_vocab          = 256128
print_info: n_merges         = 0
print_info: BOS token        = 2 '<bos>'
print_info: EOS token        = 1 '<eos>'
print_info: EOT token        = 107 '<end_of_turn>'
print_info: UNK token        = 3 '<unk>'
print_info: PAD token        = 0 '<pad>'
print_info: LF token         = 227 '<0x0A>'
print_info: EOG token        = 1 '<eos>'
print_info: EOG token        = 107 '<end_of_turn>'
print_info: max token length = 93
llama_model_load: vocab only - skipping tensors
time=2026-03-27T00:42:21.373Z level=INFO source=server.go:431 msg="starting runner" cmd="/usr/bin/ollama runner --model /root/.ollama/models/blobs/sha256-c1864a5eb19305c40519da12cc543519e48a0697ecd30e15d5ac228644957d12 --port 33697"
time=2026-03-27T00:42:21.375Z level=INFO source=sched.go:491 msg="system memory" total="24.0 GiB" free="22.6 GiB" free_swap="8.0 GiB"
time=2026-03-27T00:42:21.375Z level=INFO source=server.go:498 msg="loading model" "model layers"=19 requested=-1
time=2026-03-27T00:42:21.376Z level=INFO source=device.go:245 msg="model weights" device=CPU size="1.6 GiB"
time=2026-03-27T00:42:21.376Z level=INFO source=device.go:256 msg="kv cache" device=CPU size="72.0 MiB"
time=2026-03-27T00:42:21.376Z level=INFO source=device.go:272 msg="total memory" size="1.6 GiB"
time=2026-03-27T00:42:21.396Z level=INFO source=runner.go:965 msg="starting go runner"
load_backend: loaded CPU backend from /usr/lib/ollama/libggml-cpu-alderlake.so
time=2026-03-27T00:42:21.406Z level=INFO source=ggml.go:104 msg=system CPU.0.SSE3=1 CPU.0.SSSE3=1 CPU.0.AVX=1 CPU.0.AVX_VNNI=1 CPU.0.AVX2=1 CPU.0.F16C=1 CPU.0.FMA=1 CPU.0.BMI2=1 CPU.0.LLAMAFILE=1 CPU.1.LLAMAFILE=1 compiler=cgo(gcc)
time=2026-03-27T00:42:21.407Z level=INFO source=runner.go:1001 msg="Server listening on 127.0.0.1:33697"
time=2026-03-27T00:42:21.410Z level=INFO source=runner.go:895 msg=load request="{Operation:commit LoraPath:[] Parallel:1 BatchSize:512 FlashAttention:Auto KvSize:4096 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:42:21.411Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:42:21.411Z level=INFO source=server.go:1384 msg="waiting for server to become available" status="llm server loading model"
llama_model_loader: loaded meta data with 21 key-value pairs and 164 tensors from /root/.ollama/models/blobs/sha256-c1864a5eb19305c40519da12cc543519e48a0697ecd30e15d5ac228644957d12 (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = gemma
llama_model_loader: - kv   1:                               general.name str              = gemma-2b-it
llama_model_loader: - kv   2:                       gemma.context_length u32              = 8192
llama_model_loader: - kv   3:                          gemma.block_count u32              = 18
llama_model_loader: - kv   4:                     gemma.embedding_length u32              = 2048
llama_model_loader: - kv   5:                  gemma.feed_forward_length u32              = 16384
llama_model_loader: - kv   6:                 gemma.attention.head_count u32              = 8
llama_model_loader: - kv   7:              gemma.attention.head_count_kv u32              = 1
llama_model_loader: - kv   8:                 gemma.attention.key_length u32              = 256
llama_model_loader: - kv   9:               gemma.attention.value_length u32              = 256
llama_model_loader: - kv  10:     gemma.attention.layer_norm_rms_epsilon f32              = 0.000001
llama_model_loader: - kv  11:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  12:                tokenizer.ggml.bos_token_id u32              = 2
llama_model_loader: - kv  13:                tokenizer.ggml.eos_token_id u32              = 1
llama_model_loader: - kv  14:            tokenizer.ggml.padding_token_id u32              = 0
llama_model_loader: - kv  15:            tokenizer.ggml.unknown_token_id u32              = 3
llama_model_loader: - kv  16:                      tokenizer.ggml.tokens arr[str,256128]  = ["<pad>", "<eos>", "<bos>", "<unk>", ...
llama_model_loader: - kv  17:                      tokenizer.ggml.scores arr[f32,256128]  = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  18:                  tokenizer.ggml.token_type arr[i32,256128]  = [3, 3, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, ...
llama_model_loader: - kv  19:               general.quantization_version u32              = 2
llama_model_loader: - kv  20:                          general.file_type u32              = 2
llama_model_loader: - type  f32:   37 tensors
llama_model_loader: - type q4_0:  126 tensors
llama_model_loader: - type q8_0:    1 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 1.56 GiB (5.34 BPW) 
load: control-looking token:    107 '<end_of_turn>' was not control-type; this is probably a bug in the model. its type will be overridden
load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
load: printing all EOG tokens:
load:   - 1 ('<eos>')
load:   - 107 ('<end_of_turn>')
load: special tokens cache size = 5
load: token to piece cache size = 1.6014 MB
print_info: arch             = gemma
print_info: vocab_only       = 0
print_info: no_alloc         = 0
print_info: n_ctx_train      = 8192
print_info: n_embd           = 2048
print_info: n_embd_inp       = 2048
print_info: n_layer          = 18
print_info: n_head           = 8
print_info: n_head_kv        = 1
print_info: n_rot            = 256
print_info: n_swa            = 0
print_info: is_swa_any       = 0
print_info: n_embd_head_k    = 256
print_info: n_embd_head_v    = 256
print_info: n_gqa            = 8
print_info: n_embd_k_gqa     = 256
print_info: n_embd_v_gqa     = 256
print_info: f_norm_eps       = 0.0e+00
print_info: f_norm_rms_eps   = 1.0e-06
print_info: f_clamp_kqv      = 0.0e+00
print_info: f_max_alibi_bias = 0.0e+00
print_info: f_logit_scale    = 0.0e+00
print_info: f_attn_scale     = 0.0e+00
print_info: n_ff             = 16384
print_info: n_expert         = 0
print_info: n_expert_used    = 0
print_info: n_expert_groups  = 0
print_info: n_group_used     = 0
print_info: causal attn      = 1
print_info: pooling type     = 0
print_info: rope type        = 2
print_info: rope scaling     = linear
print_info: freq_base_train  = 10000.0
print_info: freq_scale_train = 1
print_info: n_ctx_orig_yarn  = 8192
print_info: rope_yarn_log_mul= 0.0000
print_info: rope_finetuned   = unknown
print_info: model type       = 2B
print_info: model params     = 2.51 B
print_info: general.name     = gemma-2b-it
print_info: vocab type       = SPM
print_info: n_vocab          = 256128
print_info: n_merges         = 0
print_info: BOS token        = 2 '<bos>'
print_info: EOS token        = 1 '<eos>'
print_info: EOT token        = 107 '<end_of_turn>'
print_info: UNK token        = 3 '<unk>'
print_info: PAD token        = 0 '<pad>'
print_info: LF token         = 227 '<0x0A>'
print_info: EOG token        = 1 '<eos>'
print_info: EOG token        = 107 '<end_of_turn>'
print_info: max token length = 93
load_tensors: loading model tensors, this can take a while... (mmap = false)
load_tensors:          CPU model buffer size =  1594.93 MiB
llama_context: constructing llama_context
llama_context: n_seq_max     = 1
llama_context: n_ctx         = 4096
llama_context: n_ctx_seq     = 4096
llama_context: n_batch       = 512
llama_context: n_ubatch      = 512
llama_context: causal_attn   = 1
llama_context: flash_attn    = auto
llama_context: kv_unified    = false
llama_context: freq_base     = 10000.0
llama_context: freq_scale    = 1
llama_context: n_ctx_seq (4096) < n_ctx_train (8192) -- the full capacity of the model will not be utilized
llama_context:        CPU  output buffer size =     0.98 MiB
llama_kv_cache:        CPU KV buffer size =    72.00 MiB
llama_kv_cache: size =   72.00 MiB (  4096 cells,  18 layers,  1/1 seqs), K (f16):   36.00 MiB, V (f16):   36.00 MiB
llama_context: Flash Attention was auto, set to enabled
llama_context:        CPU compute buffer size =   508.25 MiB
llama_context: graph nodes  = 584
llama_context: graph splits = 1
time=2026-03-27T00:42:23.924Z level=INFO source=server.go:1388 msg="llama runner started in 2.55 seconds"
time=2026-03-27T00:42:23.925Z level=INFO source=sched.go:566 msg="loaded runners" count=3
time=2026-03-27T00:42:23.925Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:42:23.925Z level=INFO source=server.go:1388 msg="llama runner started in 2.55 seconds"
llama_model_loader: loaded meta data with 36 key-value pairs and 197 tensors from /root/.ollama/models/blobs/sha256-633fc5be925f9a484b61d6f9b9a78021eeb462100bd557309f01ba84cac26adf (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = phi3
llama_model_loader: - kv   1:                               general.type str              = model
llama_model_loader: - kv   2:                               general.name str              = Phi 3 Mini 128k Instruct
llama_model_loader: - kv   3:                           general.finetune str              = 128k-instruct
llama_model_loader: - kv   4:                           general.basename str              = Phi-3
llama_model_loader: - kv   5:                         general.size_label str              = mini
llama_model_loader: - kv   6:                            general.license str              = mit
llama_model_loader: - kv   7:                       general.license.link str              = https://huggingface.co/microsoft/Phi-...
llama_model_loader: - kv   8:                               general.tags arr[str,3]       = ["nlp", "code", "text-generation"]
llama_model_loader: - kv   9:                          general.languages arr[str,1]       = ["en"]
llama_model_loader: - kv  10:                        phi3.context_length u32              = 131072
llama_model_loader: - kv  11:  phi3.rope.scaling.original_context_length u32              = 4096
llama_model_loader: - kv  12:                      phi3.embedding_length u32              = 3072
llama_model_loader: - kv  13:                   phi3.feed_forward_length u32              = 8192
llama_model_loader: - kv  14:                           phi3.block_count u32              = 32
llama_model_loader: - kv  15:                  phi3.attention.head_count u32              = 32
llama_model_loader: - kv  16:               phi3.attention.head_count_kv u32              = 32
llama_model_loader: - kv  17:      phi3.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  18:                  phi3.rope.dimension_count u32              = 96
llama_model_loader: - kv  19:                        phi3.rope.freq_base f32              = 10000.000000
llama_model_loader: - kv  20:                          general.file_type u32              = 2
llama_model_loader: - kv  21:              phi3.attention.sliding_window u32              = 262144
llama_model_loader: - kv  22:              phi3.rope.scaling.attn_factor f32              = 1.190238
llama_model_loader: - kv  23:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  24:                         tokenizer.ggml.pre str              = default
llama_model_loader: - kv  25:                      tokenizer.ggml.tokens arr[str,32064]   = ["<unk>", "<s>", "</s>", "<0x00>", "<...
llama_model_loader: - kv  26:                      tokenizer.ggml.scores arr[f32,32064]   = [-1000.000000, -1000.000000, -1000.00...
llama_model_loader: - kv  27:                  tokenizer.ggml.token_type arr[i32,32064]   = [3, 3, 4, 6, 6, 6, 6, 6, 6, 6, 6, 6, ...
llama_model_loader: - kv  28:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  29:                tokenizer.ggml.eos_token_id u32              = 32000
llama_model_loader: - kv  30:            tokenizer.ggml.unknown_token_id u32              = 0
llama_model_loader: - kv  31:            tokenizer.ggml.padding_token_id u32              = 32000
llama_model_loader: - kv  32:               tokenizer.ggml.add_bos_token bool             = false
llama_model_loader: - kv  33:               tokenizer.ggml.add_eos_token bool             = false
llama_model_loader: - kv  34:                    tokenizer.chat_template str              = {% for message in messages %}{% if me...
llama_model_loader: - kv  35:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   67 tensors
llama_model_loader: - type q4_0:  129 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 2.03 GiB (4.55 BPW) 
load: printing all EOG tokens:
load:   - 32000 ('<|endoftext|>')
load:   - 32007 ('<|end|>')
load: special tokens cache size = 14
load: token to piece cache size = 0.1685 MB
print_info: arch             = phi3
print_info: vocab_only       = 1
print_info: no_alloc         = 0
print_info: model type       = ?B
print_info: model params     = 3.82 B
print_info: general.name     = Phi 3 Mini 128k Instruct
print_info: vocab type       = SPM
print_info: n_vocab          = 32064
print_info: n_merges         = 0
print_info: BOS token        = 1 '<s>'
print_info: EOS token        = 32000 '<|endoftext|>'
print_info: EOT token        = 32007 '<|end|>'
print_info: UNK token        = 0 '<unk>'
print_info: PAD token        = 32000 '<|endoftext|>'
print_info: LF token         = 13 '<0x0A>'
print_info: EOG token        = 32000 '<|endoftext|>'
print_info: EOG token        = 32007 '<|end|>'
print_info: max token length = 48
llama_model_load: vocab only - skipping tensors
time=2026-03-27T00:42:39.362Z level=INFO source=server.go:431 msg="starting runner" cmd="/usr/bin/ollama runner --model /root/.ollama/models/blobs/sha256-633fc5be925f9a484b61d6f9b9a78021eeb462100bd557309f01ba84cac26adf --port 45099"
time=2026-03-27T00:42:39.363Z level=INFO source=sched.go:491 msg="system memory" total="24.0 GiB" free="19.9 GiB" free_swap="8.0 GiB"
time=2026-03-27T00:42:39.363Z level=INFO source=server.go:498 msg="loading model" "model layers"=33 requested=-1
time=2026-03-27T00:42:39.363Z level=INFO source=device.go:245 msg="model weights" device=CPU size="2.0 GiB"
time=2026-03-27T00:42:39.363Z level=INFO source=device.go:256 msg="kv cache" device=CPU size="1.5 GiB"
time=2026-03-27T00:42:39.363Z level=INFO source=device.go:272 msg="total memory" size="3.5 GiB"
time=2026-03-27T00:42:39.382Z level=INFO source=runner.go:965 msg="starting go runner"
load_backend: loaded CPU backend from /usr/lib/ollama/libggml-cpu-alderlake.so
time=2026-03-27T00:42:39.392Z level=INFO source=ggml.go:104 msg=system CPU.0.SSE3=1 CPU.0.SSSE3=1 CPU.0.AVX=1 CPU.0.AVX_VNNI=1 CPU.0.AVX2=1 CPU.0.F16C=1 CPU.0.FMA=1 CPU.0.BMI2=1 CPU.0.LLAMAFILE=1 CPU.1.LLAMAFILE=1 compiler=cgo(gcc)
time=2026-03-27T00:42:39.392Z level=INFO source=runner.go:1001 msg="Server listening on 127.0.0.1:45099"
time=2026-03-27T00:42:39.397Z level=INFO source=runner.go:895 msg=load request="{Operation:commit LoraPath:[] Parallel:1 BatchSize:512 FlashAttention:Auto KvSize:4096 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:42:39.397Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:42:39.397Z level=INFO source=server.go:1384 msg="waiting for server to become available" status="llm server loading model"
llama_model_loader: loaded meta data with 36 key-value pairs and 197 tensors from /root/.ollama/models/blobs/sha256-633fc5be925f9a484b61d6f9b9a78021eeb462100bd557309f01ba84cac26adf (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = phi3
llama_model_loader: - kv   1:                               general.type str              = model
llama_model_loader: - kv   2:                               general.name str              = Phi 3 Mini 128k Instruct
llama_model_loader: - kv   3:                           general.finetune str              = 128k-instruct
llama_model_loader: - kv   4:                           general.basename str              = Phi-3
llama_model_loader: - kv   5:                         general.size_label str              = mini
llama_model_loader: - kv   6:                            general.license str              = mit
llama_model_loader: - kv   7:                       general.license.link str              = https://huggingface.co/microsoft/Phi-...
llama_model_loader: - kv   8:                               general.tags arr[str,3]       = ["nlp", "code", "text-generation"]
llama_model_loader: - kv   9:                          general.languages arr[str,1]       = ["en"]
llama_model_loader: - kv  10:                        phi3.context_length u32              = 131072
llama_model_loader: - kv  11:  phi3.rope.scaling.original_context_length u32              = 4096
llama_model_loader: - kv  12:                      phi3.embedding_length u32              = 3072
llama_model_loader: - kv  13:                   phi3.feed_forward_length u32              = 8192
llama_model_loader: - kv  14:                           phi3.block_count u32              = 32
llama_model_loader: - kv  15:                  phi3.attention.head_count u32              = 32
llama_model_loader: - kv  16:               phi3.attention.head_count_kv u32              = 32
llama_model_loader: - kv  17:      phi3.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  18:                  phi3.rope.dimension_count u32              = 96
llama_model_loader: - kv  19:                        phi3.rope.freq_base f32              = 10000.000000
llama_model_loader: - kv  20:                          general.file_type u32              = 2
llama_model_loader: - kv  21:              phi3.attention.sliding_window u32              = 262144
llama_model_loader: - kv  22:              phi3.rope.scaling.attn_factor f32              = 1.190238
llama_model_loader: - kv  23:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  24:                         tokenizer.ggml.pre str              = default
llama_model_loader: - kv  25:                      tokenizer.ggml.tokens arr[str,32064]   = ["<unk>", "<s>", "</s>", "<0x00>", "<...
llama_model_loader: - kv  26:                      tokenizer.ggml.scores arr[f32,32064]   = [-1000.000000, -1000.000000, -1000.00...
llama_model_loader: - kv  27:                  tokenizer.ggml.token_type arr[i32,32064]   = [3, 3, 4, 6, 6, 6, 6, 6, 6, 6, 6, 6, ...
llama_model_loader: - kv  28:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  29:                tokenizer.ggml.eos_token_id u32              = 32000
llama_model_loader: - kv  30:            tokenizer.ggml.unknown_token_id u32              = 0
llama_model_loader: - kv  31:            tokenizer.ggml.padding_token_id u32              = 32000
llama_model_loader: - kv  32:               tokenizer.ggml.add_bos_token bool             = false
llama_model_loader: - kv  33:               tokenizer.ggml.add_eos_token bool             = false
llama_model_loader: - kv  34:                    tokenizer.chat_template str              = {% for message in messages %}{% if me...
llama_model_loader: - kv  35:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   67 tensors
llama_model_loader: - type q4_0:  129 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 2.03 GiB (4.55 BPW) 
load_hparams: Phi SWA is currently disabled - results might be suboptimal for some models (see https://github.com/ggml-org/llama.cpp/pull/13676)
load: printing all EOG tokens:
load:   - 32000 ('<|endoftext|>')
load:   - 32007 ('<|end|>')
load: special tokens cache size = 14
load: token to piece cache size = 0.1685 MB
print_info: arch             = phi3
print_info: vocab_only       = 0
print_info: no_alloc         = 0
print_info: n_ctx_train      = 131072
print_info: n_embd           = 3072
print_info: n_embd_inp       = 3072
print_info: n_layer          = 32
print_info: n_head           = 32
print_info: n_head_kv        = 32
print_info: n_rot            = 96
print_info: n_swa            = 0
print_info: is_swa_any       = 0
print_info: n_embd_head_k    = 96
print_info: n_embd_head_v    = 96
print_info: n_gqa            = 1
print_info: n_embd_k_gqa     = 3072
print_info: n_embd_v_gqa     = 3072
print_info: f_norm_eps       = 0.0e+00
print_info: f_norm_rms_eps   = 1.0e-05
print_info: f_clamp_kqv      = 0.0e+00
print_info: f_max_alibi_bias = 0.0e+00
print_info: f_logit_scale    = 0.0e+00
print_info: f_attn_scale     = 0.0e+00
print_info: n_ff             = 8192
print_info: n_expert         = 0
print_info: n_expert_used    = 0
print_info: n_expert_groups  = 0
print_info: n_group_used     = 0
print_info: causal attn      = 1
print_info: pooling type     = 0
print_info: rope type        = 2
print_info: rope scaling     = linear
print_info: freq_base_train  = 10000.0
print_info: freq_scale_train = 1
print_info: n_ctx_orig_yarn  = 4096
print_info: rope_yarn_log_mul= 0.0000
print_info: rope_finetuned   = unknown
print_info: model type       = 3B
print_info: model params     = 3.82 B
print_info: general.name     = Phi 3 Mini 128k Instruct
print_info: vocab type       = SPM
print_info: n_vocab          = 32064
print_info: n_merges         = 0
print_info: BOS token        = 1 '<s>'
print_info: EOS token        = 32000 '<|endoftext|>'
print_info: EOT token        = 32007 '<|end|>'
print_info: UNK token        = 0 '<unk>'
print_info: PAD token        = 32000 '<|endoftext|>'
print_info: LF token         = 13 '<0x0A>'
print_info: EOG token        = 32000 '<|endoftext|>'
print_info: EOG token        = 32007 '<|end|>'
print_info: max token length = 48
load_tensors: loading model tensors, this can take a while... (mmap = false)
load_tensors:          CPU model buffer size =  2074.66 MiB
llama_context: constructing llama_context
llama_context: n_seq_max     = 1
llama_context: n_ctx         = 4096
llama_context: n_ctx_seq     = 4096
llama_context: n_batch       = 512
llama_context: n_ubatch      = 512
llama_context: causal_attn   = 1
llama_context: flash_attn    = auto
llama_context: kv_unified    = false
llama_context: freq_base     = 10000.0
llama_context: freq_scale    = 1
llama_context: n_ctx_seq (4096) < n_ctx_train (131072) -- the full capacity of the model will not be utilized
llama_context:        CPU  output buffer size =     0.13 MiB
llama_kv_cache:        CPU KV buffer size =  1536.00 MiB
llama_kv_cache: size = 1536.00 MiB (  4096 cells,  32 layers,  1/1 seqs), K (f16):  768.00 MiB, V (f16):  768.00 MiB
llama_context: Flash Attention was auto, set to enabled
llama_context:        CPU compute buffer size =    72.01 MiB
llama_context: graph nodes  = 935
llama_context: graph splits = 1
time=2026-03-27T00:42:42.663Z level=INFO source=server.go:1388 msg="llama runner started in 3.30 seconds"
time=2026-03-27T00:42:42.663Z level=INFO source=sched.go:566 msg="loaded runners" count=3
time=2026-03-27T00:42:42.664Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:42:42.664Z level=INFO source=server.go:1388 msg="llama runner started in 3.30 seconds"
llama_model_loader: loaded meta data with 19 key-value pairs and 237 tensors from /root/.ollama/models/blobs/sha256-66002b78c70a22ab25e16cc9a1736c6cc6335398c7312e3eb33db202350afe66 (version GGUF V2)
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = pankajmathur
llama_model_loader: - kv   2:                       llama.context_length u32              = 2048
llama_model_loader: - kv   3:                     llama.embedding_length u32              = 3200
llama_model_loader: - kv   4:                          llama.block_count u32              = 26
llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 8640
llama_model_loader: - kv   6:                 llama.rope.dimension_count u32              = 100
llama_model_loader: - kv   7:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv   8:              llama.attention.head_count_kv u32              = 32
llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000001
llama_model_loader: - kv  10:                          general.file_type u32              = 2
llama_model_loader: - kv  11:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  12:                      tokenizer.ggml.tokens arr[str,32000]   = ["<unk>", "<s>", "</s>", "<0x00>", "<...
llama_model_loader: - kv  13:                      tokenizer.ggml.scores arr[f32,32000]   = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  14:                  tokenizer.ggml.token_type arr[i32,32000]   = [2, 3, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, ...
llama_model_loader: - kv  15:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  16:                tokenizer.ggml.eos_token_id u32              = 2
llama_model_loader: - kv  17:            tokenizer.ggml.padding_token_id u32              = 0
llama_model_loader: - kv  18:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   53 tensors
llama_model_loader: - type q4_0:  183 tensors
llama_model_loader: - type q8_0:    1 tensors
print_info: file format = GGUF V2
print_info: file type   = Q4_0
print_info: file size   = 1.84 GiB (4.62 BPW) 
load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
load: printing all EOG tokens:
load:   - 2 ('</s>')
load: special tokens cache size = 3
load: token to piece cache size = 0.1914 MB
print_info: arch             = llama
print_info: vocab_only       = 1
print_info: no_alloc         = 0
print_info: model type       = ?B
print_info: model params     = 3.43 B
print_info: general.name     = pankajmathur
print_info: vocab type       = SPM
print_info: n_vocab          = 32000
print_info: n_merges         = 0
print_info: BOS token        = 1 '<s>'
print_info: EOS token        = 2 '</s>'
print_info: UNK token        = 0 '<unk>'
print_info: PAD token        = 0 '<unk>'
print_info: LF token         = 13 '<0x0A>'
print_info: EOG token        = 2 '</s>'
print_info: max token length = 18
llama_model_load: vocab only - skipping tensors
time=2026-03-27T00:43:04.422Z level=WARN source=server.go:169 msg="requested context size too large for model" num_ctx=4096 n_ctx_train=2048
time=2026-03-27T00:43:04.422Z level=INFO source=server.go:431 msg="starting runner" cmd="/usr/bin/ollama runner --model /root/.ollama/models/blobs/sha256-66002b78c70a22ab25e16cc9a1736c6cc6335398c7312e3eb33db202350afe66 --port 39099"
time=2026-03-27T00:43:04.423Z level=INFO source=sched.go:491 msg="system memory" total="24.0 GiB" free="17.9 GiB" free_swap="8.0 GiB"
time=2026-03-27T00:43:04.423Z level=INFO source=server.go:498 msg="loading model" "model layers"=27 requested=-1
time=2026-03-27T00:43:04.423Z level=INFO source=device.go:245 msg="model weights" device=CPU size="1.8 GiB"
time=2026-03-27T00:43:04.423Z level=INFO source=device.go:256 msg="kv cache" device=CPU size="650.0 MiB"
time=2026-03-27T00:43:04.423Z level=INFO source=device.go:272 msg="total memory" size="2.4 GiB"
time=2026-03-27T00:43:04.441Z level=INFO source=runner.go:965 msg="starting go runner"
load_backend: loaded CPU backend from /usr/lib/ollama/libggml-cpu-alderlake.so
time=2026-03-27T00:43:04.451Z level=INFO source=ggml.go:104 msg=system CPU.0.SSE3=1 CPU.0.SSSE3=1 CPU.0.AVX=1 CPU.0.AVX_VNNI=1 CPU.0.AVX2=1 CPU.0.F16C=1 CPU.0.FMA=1 CPU.0.BMI2=1 CPU.0.LLAMAFILE=1 CPU.1.LLAMAFILE=1 compiler=cgo(gcc)
time=2026-03-27T00:43:04.451Z level=INFO source=runner.go:1001 msg="Server listening on 127.0.0.1:39099"
time=2026-03-27T00:43:04.458Z level=INFO source=runner.go:895 msg=load request="{Operation:commit LoraPath:[] Parallel:1 BatchSize:512 FlashAttention:Auto KvSize:2048 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:43:04.459Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:43:04.459Z level=INFO source=server.go:1384 msg="waiting for server to become available" status="llm server loading model"
llama_model_loader: loaded meta data with 19 key-value pairs and 237 tensors from /root/.ollama/models/blobs/sha256-66002b78c70a22ab25e16cc9a1736c6cc6335398c7312e3eb33db202350afe66 (version GGUF V2)
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = pankajmathur
llama_model_loader: - kv   2:                       llama.context_length u32              = 2048
llama_model_loader: - kv   3:                     llama.embedding_length u32              = 3200
llama_model_loader: - kv   4:                          llama.block_count u32              = 26
llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 8640
llama_model_loader: - kv   6:                 llama.rope.dimension_count u32              = 100
llama_model_loader: - kv   7:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv   8:              llama.attention.head_count_kv u32              = 32
llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000001
llama_model_loader: - kv  10:                          general.file_type u32              = 2
llama_model_loader: - kv  11:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  12:                      tokenizer.ggml.tokens arr[str,32000]   = ["<unk>", "<s>", "</s>", "<0x00>", "<...
llama_model_loader: - kv  13:                      tokenizer.ggml.scores arr[f32,32000]   = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  14:                  tokenizer.ggml.token_type arr[i32,32000]   = [2, 3, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, ...
llama_model_loader: - kv  15:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  16:                tokenizer.ggml.eos_token_id u32              = 2
llama_model_loader: - kv  17:            tokenizer.ggml.padding_token_id u32              = 0
llama_model_loader: - kv  18:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   53 tensors
llama_model_loader: - type q4_0:  183 tensors
llama_model_loader: - type q8_0:    1 tensors
print_info: file format = GGUF V2
print_info: file type   = Q4_0
print_info: file size   = 1.84 GiB (4.62 BPW) 
load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
load: printing all EOG tokens:
load:   - 2 ('</s>')
load: special tokens cache size = 3
load: token to piece cache size = 0.1914 MB
print_info: arch             = llama
print_info: vocab_only       = 0
print_info: no_alloc         = 0
print_info: n_ctx_train      = 2048
print_info: n_embd           = 3200
print_info: n_embd_inp       = 3200
print_info: n_layer          = 26
print_info: n_head           = 32
print_info: n_head_kv        = 32
print_info: n_rot            = 100
print_info: n_swa            = 0
print_info: is_swa_any       = 0
print_info: n_embd_head_k    = 100
print_info: n_embd_head_v    = 100
print_info: n_gqa            = 1
print_info: n_embd_k_gqa     = 3200
print_info: n_embd_v_gqa     = 3200
print_info: f_norm_eps       = 0.0e+00
print_info: f_norm_rms_eps   = 1.0e-06
print_info: f_clamp_kqv      = 0.0e+00
print_info: f_max_alibi_bias = 0.0e+00
print_info: f_logit_scale    = 0.0e+00
print_info: f_attn_scale     = 0.0e+00
print_info: n_ff             = 8640
print_info: n_expert         = 0
print_info: n_expert_used    = 0
print_info: n_expert_groups  = 0
print_info: n_group_used     = 0
print_info: causal attn      = 1
print_info: pooling type     = 0
print_info: rope type        = 0
print_info: rope scaling     = linear
print_info: freq_base_train  = 10000.0
print_info: freq_scale_train = 1
print_info: n_ctx_orig_yarn  = 2048
print_info: rope_yarn_log_mul= 0.0000
print_info: rope_finetuned   = unknown
print_info: model type       = 3B
print_info: model params     = 3.43 B
print_info: general.name     = pankajmathur
print_info: vocab type       = SPM
print_info: n_vocab          = 32000
print_info: n_merges         = 0
print_info: BOS token        = 1 '<s>'
print_info: EOS token        = 2 '</s>'
print_info: UNK token        = 0 '<unk>'
print_info: PAD token        = 0 '<unk>'
print_info: LF token         = 13 '<0x0A>'
print_info: EOG token        = 2 '</s>'
print_info: max token length = 18
load_tensors: loading model tensors, this can take a while... (mmap = false)
load_tensors:          CPU model buffer size =  1887.49 MiB
llama_context: constructing llama_context
llama_context: n_seq_max     = 1
llama_context: n_ctx         = 2048
llama_context: n_ctx_seq     = 2048
llama_context: n_batch       = 512
llama_context: n_ubatch      = 512
llama_context: causal_attn   = 1
llama_context: flash_attn    = auto
llama_context: kv_unified    = false
llama_context: freq_base     = 10000.0
llama_context: freq_scale    = 1
llama_context:        CPU  output buffer size =     0.13 MiB
llama_kv_cache:        CPU KV buffer size =   650.00 MiB
llama_kv_cache: size =  650.00 MiB (  2048 cells,  26 layers,  1/1 seqs), K (f16):  325.00 MiB, V (f16):  325.00 MiB
llama_context: Flash Attention was auto, set to enabled
llama_context:        CPU compute buffer size =    93.51 MiB
llama_context: graph nodes  = 813
llama_context: graph splits = 1
time=2026-03-27T00:43:06.971Z level=INFO source=server.go:1388 msg="llama runner started in 2.55 seconds"
time=2026-03-27T00:43:06.972Z level=INFO source=sched.go:566 msg="loaded runners" count=3
time=2026-03-27T00:43:06.972Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:43:06.972Z level=INFO source=server.go:1388 msg="llama runner started in 2.55 seconds"
llama_model_loader: loaded meta data with 22 key-value pairs and 325 tensors from /root/.ollama/models/blobs/sha256-4eca7304a07a42c48887f159ef5ad82ed5a5bd30fe52db4aadae1dd938e26f70 (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = phi2
llama_model_loader: - kv   1:                               general.name str              = Phi2
llama_model_loader: - kv   2:                        phi2.context_length u32              = 2048
llama_model_loader: - kv   3:                      phi2.embedding_length u32              = 2560
llama_model_loader: - kv   4:                   phi2.feed_forward_length u32              = 10240
llama_model_loader: - kv   5:                           phi2.block_count u32              = 32
llama_model_loader: - kv   6:                  phi2.attention.head_count u32              = 32
llama_model_loader: - kv   7:               phi2.attention.head_count_kv u32              = 32
llama_model_loader: - kv   8:          phi2.attention.layer_norm_epsilon f32              = 0.000010
llama_model_loader: - kv   9:                  phi2.rope.dimension_count u32              = 32
llama_model_loader: - kv  10:                          general.file_type u32              = 2
llama_model_loader: - kv  11:               tokenizer.ggml.add_bos_token bool             = false
llama_model_loader: - kv  12:                       tokenizer.ggml.model str              = gpt2
llama_model_loader: - kv  13:                      tokenizer.ggml.tokens arr[str,51200]   = ["!", "\"", "#", "$", "%", "&", "'", ...
llama_model_loader: - kv  14:                  tokenizer.ggml.token_type arr[i32,51200]   = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...
llama_model_loader: - kv  15:                      tokenizer.ggml.merges arr[str,50000]   = ["Ġ t", "Ġ a", "h e", "i n", "r e",...
llama_model_loader: - kv  16:                tokenizer.ggml.bos_token_id u32              = 50256
llama_model_loader: - kv  17:                tokenizer.ggml.eos_token_id u32              = 50295
llama_model_loader: - kv  18:            tokenizer.ggml.unknown_token_id u32              = 50256
llama_model_loader: - kv  19:            tokenizer.ggml.padding_token_id u32              = 50256
llama_model_loader: - kv  20:                    tokenizer.chat_template str              = {{ bos_token }}{%- set ns = namespace...
llama_model_loader: - kv  21:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:  195 tensors
llama_model_loader: - type q4_0:  129 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 1.49 GiB (4.61 BPW) 
load: missing or unrecognized pre-tokenizer type, using: 'default'
load: printing all EOG tokens:
load:   - 50256 ('<|endoftext|>')
load:   - 50295 ('<|im_end|>')
load: special tokens cache size = 944
load: token to piece cache size = 0.3151 MB
print_info: arch             = phi2
print_info: vocab_only       = 1
print_info: no_alloc         = 0
print_info: model type       = ?B
print_info: model params     = 2.78 B
print_info: general.name     = Phi2
print_info: vocab type       = BPE
print_info: n_vocab          = 51200
print_info: n_merges         = 50000
print_info: BOS token        = 50256 '<|endoftext|>'
print_info: EOS token        = 50295 '<|im_end|>'
print_info: EOT token        = 50256 '<|endoftext|>'
print_info: UNK token        = 50256 '<|endoftext|>'
print_info: PAD token        = 50256 '<|endoftext|>'
print_info: LF token         = 198 'Ċ'
print_info: EOG token        = 50256 '<|endoftext|>'
print_info: EOG token        = 50295 '<|im_end|>'
print_info: max token length = 256
llama_model_load: vocab only - skipping tensors
time=2026-03-27T00:43:29.819Z level=WARN source=server.go:169 msg="requested context size too large for model" num_ctx=4096 n_ctx_train=2048
time=2026-03-27T00:43:29.820Z level=INFO source=server.go:431 msg="starting runner" cmd="/usr/bin/ollama runner --model /root/.ollama/models/blobs/sha256-4eca7304a07a42c48887f159ef5ad82ed5a5bd30fe52db4aadae1dd938e26f70 --port 34067"
time=2026-03-27T00:43:29.820Z level=INFO source=sched.go:491 msg="system memory" total="24.0 GiB" free="16.2 GiB" free_swap="8.0 GiB"
time=2026-03-27T00:43:29.820Z level=INFO source=server.go:498 msg="loading model" "model layers"=33 requested=-1
time=2026-03-27T00:43:29.821Z level=INFO source=device.go:245 msg="model weights" device=CPU size="1.4 GiB"
time=2026-03-27T00:43:29.821Z level=INFO source=device.go:256 msg="kv cache" device=CPU size="640.0 MiB"
time=2026-03-27T00:43:29.821Z level=INFO source=device.go:272 msg="total memory" size="2.0 GiB"
time=2026-03-27T00:43:29.846Z level=INFO source=runner.go:965 msg="starting go runner"
load_backend: loaded CPU backend from /usr/lib/ollama/libggml-cpu-alderlake.so
time=2026-03-27T00:43:29.859Z level=INFO source=ggml.go:104 msg=system CPU.0.SSE3=1 CPU.0.SSSE3=1 CPU.0.AVX=1 CPU.0.AVX_VNNI=1 CPU.0.AVX2=1 CPU.0.F16C=1 CPU.0.FMA=1 CPU.0.BMI2=1 CPU.0.LLAMAFILE=1 CPU.1.LLAMAFILE=1 compiler=cgo(gcc)
time=2026-03-27T00:43:29.860Z level=INFO source=runner.go:1001 msg="Server listening on 127.0.0.1:34067"
time=2026-03-27T00:43:29.865Z level=INFO source=runner.go:895 msg=load request="{Operation:commit LoraPath:[] Parallel:1 BatchSize:512 FlashAttention:Auto KvSize:2048 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:43:29.866Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:43:29.866Z level=INFO source=server.go:1384 msg="waiting for server to become available" status="llm server loading model"
llama_model_loader: loaded meta data with 22 key-value pairs and 325 tensors from /root/.ollama/models/blobs/sha256-4eca7304a07a42c48887f159ef5ad82ed5a5bd30fe52db4aadae1dd938e26f70 (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = phi2
llama_model_loader: - kv   1:                               general.name str              = Phi2
llama_model_loader: - kv   2:                        phi2.context_length u32              = 2048
llama_model_loader: - kv   3:                      phi2.embedding_length u32              = 2560
llama_model_loader: - kv   4:                   phi2.feed_forward_length u32              = 10240
llama_model_loader: - kv   5:                           phi2.block_count u32              = 32
llama_model_loader: - kv   6:                  phi2.attention.head_count u32              = 32
llama_model_loader: - kv   7:               phi2.attention.head_count_kv u32              = 32
llama_model_loader: - kv   8:          phi2.attention.layer_norm_epsilon f32              = 0.000010
llama_model_loader: - kv   9:                  phi2.rope.dimension_count u32              = 32
llama_model_loader: - kv  10:                          general.file_type u32              = 2
llama_model_loader: - kv  11:               tokenizer.ggml.add_bos_token bool             = false
llama_model_loader: - kv  12:                       tokenizer.ggml.model str              = gpt2
llama_model_loader: - kv  13:                      tokenizer.ggml.tokens arr[str,51200]   = ["!", "\"", "#", "$", "%", "&", "'", ...
llama_model_loader: - kv  14:                  tokenizer.ggml.token_type arr[i32,51200]   = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...
llama_model_loader: - kv  15:                      tokenizer.ggml.merges arr[str,50000]   = ["Ġ t", "Ġ a", "h e", "i n", "r e",...
llama_model_loader: - kv  16:                tokenizer.ggml.bos_token_id u32              = 50256
llama_model_loader: - kv  17:                tokenizer.ggml.eos_token_id u32              = 50295
llama_model_loader: - kv  18:            tokenizer.ggml.unknown_token_id u32              = 50256
llama_model_loader: - kv  19:            tokenizer.ggml.padding_token_id u32              = 50256
llama_model_loader: - kv  20:                    tokenizer.chat_template str              = {{ bos_token }}{%- set ns = namespace...
llama_model_loader: - kv  21:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:  195 tensors
llama_model_loader: - type q4_0:  129 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 1.49 GiB (4.61 BPW) 
load: missing or unrecognized pre-tokenizer type, using: 'default'
load: printing all EOG tokens:
load:   - 50256 ('<|endoftext|>')
load:   - 50295 ('<|im_end|>')
load: special tokens cache size = 944
load: token to piece cache size = 0.3151 MB
print_info: arch             = phi2
print_info: vocab_only       = 0
print_info: no_alloc         = 0
print_info: n_ctx_train      = 2048
print_info: n_embd           = 2560
print_info: n_embd_inp       = 2560
print_info: n_layer          = 32
print_info: n_head           = 32
print_info: n_head_kv        = 32
print_info: n_rot            = 32
print_info: n_swa            = 0
print_info: is_swa_any       = 0
print_info: n_embd_head_k    = 80
print_info: n_embd_head_v    = 80
print_info: n_gqa            = 1
print_info: n_embd_k_gqa     = 2560
print_info: n_embd_v_gqa     = 2560
print_info: f_norm_eps       = 1.0e-05
print_info: f_norm_rms_eps   = 0.0e+00
print_info: f_clamp_kqv      = 0.0e+00
print_info: f_max_alibi_bias = 0.0e+00
print_info: f_logit_scale    = 0.0e+00
print_info: f_attn_scale     = 0.0e+00
print_info: n_ff             = 10240
print_info: n_expert         = 0
print_info: n_expert_used    = 0
print_info: n_expert_groups  = 0
print_info: n_group_used     = 0
print_info: causal attn      = 1
print_info: pooling type     = 0
print_info: rope type        = 2
print_info: rope scaling     = linear
print_info: freq_base_train  = 10000.0
print_info: freq_scale_train = 1
print_info: n_ctx_orig_yarn  = 2048
print_info: rope_yarn_log_mul= 0.0000
print_info: rope_finetuned   = unknown
print_info: model type       = 3B
print_info: model params     = 2.78 B
print_info: general.name     = Phi2
print_info: vocab type       = BPE
print_info: n_vocab          = 51200
print_info: n_merges         = 50000
print_info: BOS token        = 50256 '<|endoftext|>'
print_info: EOS token        = 50295 '<|im_end|>'
print_info: EOT token        = 50256 '<|endoftext|>'
print_info: UNK token        = 50256 '<|endoftext|>'
print_info: PAD token        = 50256 '<|endoftext|>'
print_info: LF token         = 198 'Ċ'
print_info: EOG token        = 50256 '<|endoftext|>'
print_info: EOG token        = 50295 '<|im_end|>'
print_info: max token length = 256
load_tensors: loading model tensors, this can take a while... (mmap = false)
load_tensors:          CPU model buffer size =  1526.50 MiB
llama_context: constructing llama_context
llama_context: n_seq_max     = 1
llama_context: n_ctx         = 2048
llama_context: n_ctx_seq     = 2048
llama_context: n_batch       = 512
llama_context: n_ubatch      = 512
llama_context: causal_attn   = 1
llama_context: flash_attn    = auto
llama_context: kv_unified    = false
llama_context: freq_base     = 10000.0
llama_context: freq_scale    = 1
llama_context:        CPU  output buffer size =     0.21 MiB
llama_kv_cache:        CPU KV buffer size =   640.00 MiB
llama_kv_cache: size =  640.00 MiB (  2048 cells,  32 layers,  1/1 seqs), K (f16):  320.00 MiB, V (f16):  320.00 MiB
llama_context: Flash Attention was auto, set to enabled
llama_context:        CPU compute buffer size =   105.00 MiB
llama_context: graph nodes  = 1034
llama_context: graph splits = 1
time=2026-03-27T00:43:32.127Z level=INFO source=server.go:1388 msg="llama runner started in 2.31 seconds"
time=2026-03-27T00:43:32.127Z level=INFO source=sched.go:566 msg="loaded runners" count=3
time=2026-03-27T00:43:32.127Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:43:32.127Z level=INFO source=server.go:1388 msg="llama runner started in 2.31 seconds"
llama_model_loader: loaded meta data with 21 key-value pairs and 291 tensors from /root/.ollama/models/blobs/sha256-5768750fc96e296081ba7531933c7eb5c5bacfafbd06b81d1bb495e97f6a4b20 (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = Intel
llama_model_loader: - kv   2:                       llama.context_length u32              = 32768
llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
llama_model_loader: - kv   4:                          llama.block_count u32              = 32
llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 14336
llama_model_loader: - kv   6:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv   7:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv   8:              llama.attention.head_count_kv u32              = 8
llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  10:                       llama.rope.freq_base f32              = 10000.000000
llama_model_loader: - kv  11:                          general.file_type u32              = 2
llama_model_loader: - kv  12:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  13:                      tokenizer.ggml.tokens arr[str,32000]   = ["<unk>", "<s>", "</s>", "<0x00>", "<...
llama_model_loader: - kv  14:                      tokenizer.ggml.scores arr[f32,32000]   = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  15:                  tokenizer.ggml.token_type arr[i32,32000]   = [2, 3, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, ...
llama_model_loader: - kv  16:                      tokenizer.ggml.merges arr[str,58980]   = ["▁ t", "i n", "e r", "▁ a", "h e...
llama_model_loader: - kv  17:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  18:                tokenizer.ggml.eos_token_id u32              = 2
llama_model_loader: - kv  19:            tokenizer.ggml.unknown_token_id u32              = 0
llama_model_loader: - kv  20:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   65 tensors
llama_model_loader: - type q4_0:  225 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 3.83 GiB (4.54 BPW) 
load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
load: printing all EOG tokens:
load:   - 2 ('</s>')
load: special tokens cache size = 3
load: token to piece cache size = 0.1637 MB
print_info: arch             = llama
print_info: vocab_only       = 1
print_info: no_alloc         = 0
print_info: model type       = ?B
print_info: model params     = 7.24 B
print_info: general.name     = Intel
print_info: vocab type       = SPM
print_info: n_vocab          = 32000
print_info: n_merges         = 0
print_info: BOS token        = 1 '<s>'
print_info: EOS token        = 2 '</s>'
print_info: UNK token        = 0 '<unk>'
print_info: LF token         = 13 '<0x0A>'
print_info: EOG token        = 2 '</s>'
print_info: max token length = 48
llama_model_load: vocab only - skipping tensors
time=2026-03-27T00:43:49.939Z level=INFO source=server.go:431 msg="starting runner" cmd="/usr/bin/ollama runner --model /root/.ollama/models/blobs/sha256-5768750fc96e296081ba7531933c7eb5c5bacfafbd06b81d1bb495e97f6a4b20 --port 41047"
time=2026-03-27T00:43:49.940Z level=INFO source=sched.go:491 msg="system memory" total="24.0 GiB" free="15.0 GiB" free_swap="8.0 GiB"
time=2026-03-27T00:43:49.940Z level=INFO source=server.go:498 msg="loading model" "model layers"=33 requested=-1
time=2026-03-27T00:43:49.941Z level=INFO source=device.go:245 msg="model weights" device=CPU size="3.8 GiB"
time=2026-03-27T00:43:49.941Z level=INFO source=device.go:256 msg="kv cache" device=CPU size="512.0 MiB"
time=2026-03-27T00:43:49.941Z level=INFO source=device.go:272 msg="total memory" size="4.3 GiB"
time=2026-03-27T00:43:49.959Z level=INFO source=runner.go:965 msg="starting go runner"
load_backend: loaded CPU backend from /usr/lib/ollama/libggml-cpu-alderlake.so
time=2026-03-27T00:43:49.968Z level=INFO source=ggml.go:104 msg=system CPU.0.SSE3=1 CPU.0.SSSE3=1 CPU.0.AVX=1 CPU.0.AVX_VNNI=1 CPU.0.AVX2=1 CPU.0.F16C=1 CPU.0.FMA=1 CPU.0.BMI2=1 CPU.0.LLAMAFILE=1 CPU.1.LLAMAFILE=1 compiler=cgo(gcc)
time=2026-03-27T00:43:49.969Z level=INFO source=runner.go:1001 msg="Server listening on 127.0.0.1:41047"
time=2026-03-27T00:43:49.975Z level=INFO source=runner.go:895 msg=load request="{Operation:commit LoraPath:[] Parallel:1 BatchSize:512 FlashAttention:Auto KvSize:4096 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:43:49.975Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:43:49.976Z level=INFO source=server.go:1384 msg="waiting for server to become available" status="llm server loading model"
llama_model_loader: loaded meta data with 21 key-value pairs and 291 tensors from /root/.ollama/models/blobs/sha256-5768750fc96e296081ba7531933c7eb5c5bacfafbd06b81d1bb495e97f6a4b20 (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = Intel
llama_model_loader: - kv   2:                       llama.context_length u32              = 32768
llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
llama_model_loader: - kv   4:                          llama.block_count u32              = 32
llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 14336
llama_model_loader: - kv   6:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv   7:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv   8:              llama.attention.head_count_kv u32              = 8
llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  10:                       llama.rope.freq_base f32              = 10000.000000
llama_model_loader: - kv  11:                          general.file_type u32              = 2
llama_model_loader: - kv  12:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  13:                      tokenizer.ggml.tokens arr[str,32000]   = ["<unk>", "<s>", "</s>", "<0x00>", "<...
llama_model_loader: - kv  14:                      tokenizer.ggml.scores arr[f32,32000]   = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  15:                  tokenizer.ggml.token_type arr[i32,32000]   = [2, 3, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, ...
llama_model_loader: - kv  16:                      tokenizer.ggml.merges arr[str,58980]   = ["▁ t", "i n", "e r", "▁ a", "h e...
llama_model_loader: - kv  17:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  18:                tokenizer.ggml.eos_token_id u32              = 2
llama_model_loader: - kv  19:            tokenizer.ggml.unknown_token_id u32              = 0
llama_model_loader: - kv  20:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   65 tensors
llama_model_loader: - type q4_0:  225 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 3.83 GiB (4.54 BPW) 
load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
load: printing all EOG tokens:
load:   - 2 ('</s>')
load: special tokens cache size = 3
load: token to piece cache size = 0.1637 MB
print_info: arch             = llama
print_info: vocab_only       = 0
print_info: no_alloc         = 0
print_info: n_ctx_train      = 32768
print_info: n_embd           = 4096
print_info: n_embd_inp       = 4096
print_info: n_layer          = 32
print_info: n_head           = 32
print_info: n_head_kv        = 8
print_info: n_rot            = 128
print_info: n_swa            = 0
print_info: is_swa_any       = 0
print_info: n_embd_head_k    = 128
print_info: n_embd_head_v    = 128
print_info: n_gqa            = 4
print_info: n_embd_k_gqa     = 1024
print_info: n_embd_v_gqa     = 1024
print_info: f_norm_eps       = 0.0e+00
print_info: f_norm_rms_eps   = 1.0e-05
print_info: f_clamp_kqv      = 0.0e+00
print_info: f_max_alibi_bias = 0.0e+00
print_info: f_logit_scale    = 0.0e+00
print_info: f_attn_scale     = 0.0e+00
print_info: n_ff             = 14336
print_info: n_expert         = 0
print_info: n_expert_used    = 0
print_info: n_expert_groups  = 0
print_info: n_group_used     = 0
print_info: causal attn      = 1
print_info: pooling type     = 0
print_info: rope type        = 0
print_info: rope scaling     = linear
print_info: freq_base_train  = 10000.0
print_info: freq_scale_train = 1
print_info: n_ctx_orig_yarn  = 32768
print_info: rope_yarn_log_mul= 0.0000
print_info: rope_finetuned   = unknown
print_info: model type       = 7B
print_info: model params     = 7.24 B
print_info: general.name     = Intel
print_info: vocab type       = SPM
print_info: n_vocab          = 32000
print_info: n_merges         = 0
print_info: BOS token        = 1 '<s>'
print_info: EOS token        = 2 '</s>'
print_info: UNK token        = 0 '<unk>'
print_info: LF token         = 13 '<0x0A>'
print_info: EOG token        = 2 '</s>'
print_info: max token length = 48
load_tensors: loading model tensors, this can take a while... (mmap = false)
load_tensors:          CPU model buffer size =  3917.87 MiB
llama_context: constructing llama_context
llama_context: n_seq_max     = 1
llama_context: n_ctx         = 4096
llama_context: n_ctx_seq     = 4096
llama_context: n_batch       = 512
llama_context: n_ubatch      = 512
llama_context: causal_attn   = 1
llama_context: flash_attn    = auto
llama_context: kv_unified    = false
llama_context: freq_base     = 10000.0
llama_context: freq_scale    = 1
llama_context: n_ctx_seq (4096) < n_ctx_train (32768) -- the full capacity of the model will not be utilized
llama_context:        CPU  output buffer size =     0.14 MiB
llama_kv_cache:        CPU KV buffer size =   512.00 MiB
llama_kv_cache: size =  512.00 MiB (  4096 cells,  32 layers,  1/1 seqs), K (f16):  256.00 MiB, V (f16):  256.00 MiB
llama_context: Flash Attention was auto, set to enabled
llama_context:        CPU compute buffer size =   112.01 MiB
llama_context: graph nodes  = 999
llama_context: graph splits = 1
time=2026-03-27T00:43:54.750Z level=INFO source=server.go:1388 msg="llama runner started in 4.81 seconds"
time=2026-03-27T00:43:54.750Z level=INFO source=sched.go:566 msg="loaded runners" count=3
time=2026-03-27T00:43:54.750Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:43:54.751Z level=INFO source=server.go:1388 msg="llama runner started in 4.81 seconds"
llama_model_loader: loaded meta data with 24 key-value pairs and 291 tensors from /root/.ollama/models/blobs/sha256-1cecc26325a197571a1961bfacf64dc6e35e0f05faf57d3c6941a982e1eb2e1d (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = openchat
llama_model_loader: - kv   2:                       llama.context_length u32              = 8192
llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
llama_model_loader: - kv   4:                          llama.block_count u32              = 32
llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 14336
llama_model_loader: - kv   6:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv   7:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv   8:              llama.attention.head_count_kv u32              = 8
llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  10:                       llama.rope.freq_base f32              = 10000.000000
llama_model_loader: - kv  11:                          general.file_type u32              = 2
llama_model_loader: - kv  12:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  13:                      tokenizer.ggml.tokens arr[str,32002]   = ["<unk>", "<s>", "</s>", "<0x00>", "<...
llama_model_loader: - kv  14:                      tokenizer.ggml.scores arr[f32,32002]   = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  15:                  tokenizer.ggml.token_type arr[i32,32002]   = [2, 3, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, ...
llama_model_loader: - kv  16:                      tokenizer.ggml.merges arr[str,58980]   = ["▁ t", "i n", "e r", "▁ a", "h e...
llama_model_loader: - kv  17:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  18:                tokenizer.ggml.eos_token_id u32              = 32000
llama_model_loader: - kv  19:            tokenizer.ggml.unknown_token_id u32              = 0
llama_model_loader: - kv  20:               tokenizer.ggml.add_bos_token bool             = true
llama_model_loader: - kv  21:               tokenizer.ggml.add_eos_token bool             = false
llama_model_loader: - kv  22:                    tokenizer.chat_template str              = {{ bos_token }}{% for message in mess...
llama_model_loader: - kv  23:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   65 tensors
llama_model_loader: - type q4_0:  225 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 3.83 GiB (4.54 BPW) 
load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
load: printing all EOG tokens:
load:   - 32000 ('<|end_of_turn|>')
load: special tokens cache size = 5
load: token to piece cache size = 0.1637 MB
print_info: arch             = llama
print_info: vocab_only       = 1
print_info: no_alloc         = 0
print_info: model type       = ?B
print_info: model params     = 7.24 B
print_info: general.name     = openchat
print_info: vocab type       = SPM
print_info: n_vocab          = 32002
print_info: n_merges         = 0
print_info: BOS token        = 1 '<s>'
print_info: EOS token        = 32000 '<|end_of_turn|>'
print_info: UNK token        = 0 '<unk>'
print_info: LF token         = 13 '<0x0A>'
print_info: EOG token        = 32000 '<|end_of_turn|>'
print_info: max token length = 48
llama_model_load: vocab only - skipping tensors
time=2026-03-27T00:44:37.613Z level=INFO source=server.go:431 msg="starting runner" cmd="/usr/bin/ollama runner --model /root/.ollama/models/blobs/sha256-1cecc26325a197571a1961bfacf64dc6e35e0f05faf57d3c6941a982e1eb2e1d --port 39247"
time=2026-03-27T00:44:37.613Z level=INFO source=sched.go:491 msg="system memory" total="24.0 GiB" free="16.6 GiB" free_swap="8.0 GiB"
time=2026-03-27T00:44:37.613Z level=INFO source=server.go:498 msg="loading model" "model layers"=33 requested=-1
time=2026-03-27T00:44:37.614Z level=INFO source=device.go:245 msg="model weights" device=CPU size="3.8 GiB"
time=2026-03-27T00:44:37.614Z level=INFO source=device.go:256 msg="kv cache" device=CPU size="512.0 MiB"
time=2026-03-27T00:44:37.614Z level=INFO source=device.go:272 msg="total memory" size="4.3 GiB"
time=2026-03-27T00:44:37.641Z level=INFO source=runner.go:965 msg="starting go runner"
load_backend: loaded CPU backend from /usr/lib/ollama/libggml-cpu-alderlake.so
time=2026-03-27T00:44:37.655Z level=INFO source=ggml.go:104 msg=system CPU.0.SSE3=1 CPU.0.SSSE3=1 CPU.0.AVX=1 CPU.0.AVX_VNNI=1 CPU.0.AVX2=1 CPU.0.F16C=1 CPU.0.FMA=1 CPU.0.BMI2=1 CPU.0.LLAMAFILE=1 CPU.1.LLAMAFILE=1 compiler=cgo(gcc)
time=2026-03-27T00:44:37.656Z level=INFO source=runner.go:1001 msg="Server listening on 127.0.0.1:39247"
time=2026-03-27T00:44:37.660Z level=INFO source=runner.go:895 msg=load request="{Operation:commit LoraPath:[] Parallel:1 BatchSize:512 FlashAttention:Auto KvSize:4096 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:44:37.662Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:44:37.662Z level=INFO source=server.go:1384 msg="waiting for server to become available" status="llm server loading model"
llama_model_loader: loaded meta data with 24 key-value pairs and 291 tensors from /root/.ollama/models/blobs/sha256-1cecc26325a197571a1961bfacf64dc6e35e0f05faf57d3c6941a982e1eb2e1d (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = openchat
llama_model_loader: - kv   2:                       llama.context_length u32              = 8192
llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
llama_model_loader: - kv   4:                          llama.block_count u32              = 32
llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 14336
llama_model_loader: - kv   6:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv   7:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv   8:              llama.attention.head_count_kv u32              = 8
llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  10:                       llama.rope.freq_base f32              = 10000.000000
llama_model_loader: - kv  11:                          general.file_type u32              = 2
llama_model_loader: - kv  12:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  13:                      tokenizer.ggml.tokens arr[str,32002]   = ["<unk>", "<s>", "</s>", "<0x00>", "<...
llama_model_loader: - kv  14:                      tokenizer.ggml.scores arr[f32,32002]   = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  15:                  tokenizer.ggml.token_type arr[i32,32002]   = [2, 3, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, ...
llama_model_loader: - kv  16:                      tokenizer.ggml.merges arr[str,58980]   = ["▁ t", "i n", "e r", "▁ a", "h e...
llama_model_loader: - kv  17:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  18:                tokenizer.ggml.eos_token_id u32              = 32000
llama_model_loader: - kv  19:            tokenizer.ggml.unknown_token_id u32              = 0
llama_model_loader: - kv  20:               tokenizer.ggml.add_bos_token bool             = true
llama_model_loader: - kv  21:               tokenizer.ggml.add_eos_token bool             = false
llama_model_loader: - kv  22:                    tokenizer.chat_template str              = {{ bos_token }}{% for message in mess...
llama_model_loader: - kv  23:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   65 tensors
llama_model_loader: - type q4_0:  225 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 3.83 GiB (4.54 BPW) 
load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
load: printing all EOG tokens:
load:   - 32000 ('<|end_of_turn|>')
load: special tokens cache size = 5
load: token to piece cache size = 0.1637 MB
print_info: arch             = llama
print_info: vocab_only       = 0
print_info: no_alloc         = 0
print_info: n_ctx_train      = 8192
print_info: n_embd           = 4096
print_info: n_embd_inp       = 4096
print_info: n_layer          = 32
print_info: n_head           = 32
print_info: n_head_kv        = 8
print_info: n_rot            = 128
print_info: n_swa            = 0
print_info: is_swa_any       = 0
print_info: n_embd_head_k    = 128
print_info: n_embd_head_v    = 128
print_info: n_gqa            = 4
print_info: n_embd_k_gqa     = 1024
print_info: n_embd_v_gqa     = 1024
print_info: f_norm_eps       = 0.0e+00
print_info: f_norm_rms_eps   = 1.0e-05
print_info: f_clamp_kqv      = 0.0e+00
print_info: f_max_alibi_bias = 0.0e+00
print_info: f_logit_scale    = 0.0e+00
print_info: f_attn_scale     = 0.0e+00
print_info: n_ff             = 14336
print_info: n_expert         = 0
print_info: n_expert_used    = 0
print_info: n_expert_groups  = 0
print_info: n_group_used     = 0
print_info: causal attn      = 1
print_info: pooling type     = 0
print_info: rope type        = 0
print_info: rope scaling     = linear
print_info: freq_base_train  = 10000.0
print_info: freq_scale_train = 1
print_info: n_ctx_orig_yarn  = 8192
print_info: rope_yarn_log_mul= 0.0000
print_info: rope_finetuned   = unknown
print_info: model type       = 7B
print_info: model params     = 7.24 B
print_info: general.name     = openchat
print_info: vocab type       = SPM
print_info: n_vocab          = 32002
print_info: n_merges         = 0
print_info: BOS token        = 1 '<s>'
print_info: EOS token        = 32000 '<|end_of_turn|>'
print_info: UNK token        = 0 '<unk>'
print_info: LF token         = 13 '<0x0A>'
print_info: EOG token        = 32000 '<|end_of_turn|>'
print_info: max token length = 48
load_tensors: loading model tensors, this can take a while... (mmap = false)
load_tensors:          CPU model buffer size =  3917.88 MiB
llama_context: constructing llama_context
llama_context: n_seq_max     = 1
llama_context: n_ctx         = 4096
llama_context: n_ctx_seq     = 4096
llama_context: n_batch       = 512
llama_context: n_ubatch      = 512
llama_context: causal_attn   = 1
llama_context: flash_attn    = auto
llama_context: kv_unified    = false
llama_context: freq_base     = 10000.0
llama_context: freq_scale    = 1
llama_context: n_ctx_seq (4096) < n_ctx_train (8192) -- the full capacity of the model will not be utilized
llama_context:        CPU  output buffer size =     0.14 MiB
llama_kv_cache:        CPU KV buffer size =   512.00 MiB
llama_kv_cache: size =  512.00 MiB (  4096 cells,  32 layers,  1/1 seqs), K (f16):  256.00 MiB, V (f16):  256.00 MiB
llama_context: Flash Attention was auto, set to enabled
llama_context:        CPU compute buffer size =   112.01 MiB
llama_context: graph nodes  = 999
llama_context: graph splits = 1
time=2026-03-27T00:44:42.942Z level=INFO source=server.go:1388 msg="llama runner started in 5.33 seconds"
time=2026-03-27T00:44:42.942Z level=INFO source=sched.go:566 msg="loaded runners" count=3
time=2026-03-27T00:44:42.942Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:44:42.943Z level=INFO source=server.go:1388 msg="llama runner started in 5.33 seconds"
llama_model_loader: loaded meta data with 23 key-value pairs and 291 tensors from /root/.ollama/models/blobs/sha256-730ebed2578e5be3e25c3ba155b06cb46690426682a38127cb72a9697e4443b4 (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = HuggingFaceH4
llama_model_loader: - kv   2:                       llama.context_length u32              = 32768
llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
llama_model_loader: - kv   4:                          llama.block_count u32              = 32
llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 14336
llama_model_loader: - kv   6:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv   7:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv   8:              llama.attention.head_count_kv u32              = 8
llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  10:                       llama.rope.freq_base f32              = 10000.000000
llama_model_loader: - kv  11:                          general.file_type u32              = 2
llama_model_loader: - kv  12:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  13:                      tokenizer.ggml.tokens arr[str,32000]   = ["<unk>", "<s>", "</s>", "<0x00>", "<...
llama_model_loader: - kv  14:                      tokenizer.ggml.scores arr[f32,32000]   = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  15:                  tokenizer.ggml.token_type arr[i32,32000]   = [2, 3, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, ...
llama_model_loader: - kv  16:                      tokenizer.ggml.merges arr[str,58980]   = ["▁ t", "i n", "e r", "▁ a", "h e...
llama_model_loader: - kv  17:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  18:                tokenizer.ggml.eos_token_id u32              = 2
llama_model_loader: - kv  19:            tokenizer.ggml.unknown_token_id u32              = 0
llama_model_loader: - kv  20:            tokenizer.ggml.padding_token_id u32              = 2
llama_model_loader: - kv  21:                    tokenizer.chat_template str              = {% for message in messages %}\n{% if m...
llama_model_loader: - kv  22:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   65 tensors
llama_model_loader: - type q4_0:  225 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 3.83 GiB (4.54 BPW) 
load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
load: printing all EOG tokens:
load:   - 2 ('</s>')
load: special tokens cache size = 3
load: token to piece cache size = 0.1637 MB
print_info: arch             = llama
print_info: vocab_only       = 1
print_info: no_alloc         = 0
print_info: model type       = ?B
print_info: model params     = 7.24 B
print_info: general.name     = HuggingFaceH4
print_info: vocab type       = SPM
print_info: n_vocab          = 32000
print_info: n_merges         = 0
print_info: BOS token        = 1 '<s>'
print_info: EOS token        = 2 '</s>'
print_info: UNK token        = 0 '<unk>'
print_info: PAD token        = 2 '</s>'
print_info: LF token         = 13 '<0x0A>'
print_info: EOG token        = 2 '</s>'
print_info: max token length = 48
llama_model_load: vocab only - skipping tensors
time=2026-03-27T00:45:28.198Z level=INFO source=server.go:431 msg="starting runner" cmd="/usr/bin/ollama runner --model /root/.ollama/models/blobs/sha256-730ebed2578e5be3e25c3ba155b06cb46690426682a38127cb72a9697e4443b4 --port 36089"
time=2026-03-27T00:45:28.198Z level=INFO source=sched.go:491 msg="system memory" total="24.0 GiB" free="16.2 GiB" free_swap="8.0 GiB"
time=2026-03-27T00:45:28.198Z level=INFO source=server.go:498 msg="loading model" "model layers"=33 requested=-1
time=2026-03-27T00:45:28.199Z level=INFO source=device.go:245 msg="model weights" device=CPU size="3.8 GiB"
time=2026-03-27T00:45:28.199Z level=INFO source=device.go:256 msg="kv cache" device=CPU size="512.0 MiB"
time=2026-03-27T00:45:28.199Z level=INFO source=device.go:272 msg="total memory" size="4.3 GiB"
time=2026-03-27T00:45:28.223Z level=INFO source=runner.go:965 msg="starting go runner"
load_backend: loaded CPU backend from /usr/lib/ollama/libggml-cpu-alderlake.so
time=2026-03-27T00:45:28.236Z level=INFO source=ggml.go:104 msg=system CPU.0.SSE3=1 CPU.0.SSSE3=1 CPU.0.AVX=1 CPU.0.AVX_VNNI=1 CPU.0.AVX2=1 CPU.0.F16C=1 CPU.0.FMA=1 CPU.0.BMI2=1 CPU.0.LLAMAFILE=1 CPU.1.LLAMAFILE=1 compiler=cgo(gcc)
time=2026-03-27T00:45:28.237Z level=INFO source=runner.go:1001 msg="Server listening on 127.0.0.1:36089"
time=2026-03-27T00:45:28.245Z level=INFO source=runner.go:895 msg=load request="{Operation:commit LoraPath:[] Parallel:1 BatchSize:512 FlashAttention:Auto KvSize:4096 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:45:28.246Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:45:28.246Z level=INFO source=server.go:1384 msg="waiting for server to become available" status="llm server loading model"
llama_model_loader: loaded meta data with 23 key-value pairs and 291 tensors from /root/.ollama/models/blobs/sha256-730ebed2578e5be3e25c3ba155b06cb46690426682a38127cb72a9697e4443b4 (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = HuggingFaceH4
llama_model_loader: - kv   2:                       llama.context_length u32              = 32768
llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
llama_model_loader: - kv   4:                          llama.block_count u32              = 32
llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 14336
llama_model_loader: - kv   6:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv   7:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv   8:              llama.attention.head_count_kv u32              = 8
llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  10:                       llama.rope.freq_base f32              = 10000.000000
llama_model_loader: - kv  11:                          general.file_type u32              = 2
llama_model_loader: - kv  12:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  13:                      tokenizer.ggml.tokens arr[str,32000]   = ["<unk>", "<s>", "</s>", "<0x00>", "<...
llama_model_loader: - kv  14:                      tokenizer.ggml.scores arr[f32,32000]   = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  15:                  tokenizer.ggml.token_type arr[i32,32000]   = [2, 3, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, ...
llama_model_loader: - kv  16:                      tokenizer.ggml.merges arr[str,58980]   = ["▁ t", "i n", "e r", "▁ a", "h e...
llama_model_loader: - kv  17:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  18:                tokenizer.ggml.eos_token_id u32              = 2
llama_model_loader: - kv  19:            tokenizer.ggml.unknown_token_id u32              = 0
llama_model_loader: - kv  20:            tokenizer.ggml.padding_token_id u32              = 2
llama_model_loader: - kv  21:                    tokenizer.chat_template str              = {% for message in messages %}\n{% if m...
llama_model_loader: - kv  22:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   65 tensors
llama_model_loader: - type q4_0:  225 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 3.83 GiB (4.54 BPW) 
load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
load: printing all EOG tokens:
load:   - 2 ('</s>')
load: special tokens cache size = 3
load: token to piece cache size = 0.1637 MB
print_info: arch             = llama
print_info: vocab_only       = 0
print_info: no_alloc         = 0
print_info: n_ctx_train      = 32768
print_info: n_embd           = 4096
print_info: n_embd_inp       = 4096
print_info: n_layer          = 32
print_info: n_head           = 32
print_info: n_head_kv        = 8
print_info: n_rot            = 128
print_info: n_swa            = 0
print_info: is_swa_any       = 0
print_info: n_embd_head_k    = 128
print_info: n_embd_head_v    = 128
print_info: n_gqa            = 4
print_info: n_embd_k_gqa     = 1024
print_info: n_embd_v_gqa     = 1024
print_info: f_norm_eps       = 0.0e+00
print_info: f_norm_rms_eps   = 1.0e-05
print_info: f_clamp_kqv      = 0.0e+00
print_info: f_max_alibi_bias = 0.0e+00
print_info: f_logit_scale    = 0.0e+00
print_info: f_attn_scale     = 0.0e+00
print_info: n_ff             = 14336
print_info: n_expert         = 0
print_info: n_expert_used    = 0
print_info: n_expert_groups  = 0
print_info: n_group_used     = 0
print_info: causal attn      = 1
print_info: pooling type     = 0
print_info: rope type        = 0
print_info: rope scaling     = linear
print_info: freq_base_train  = 10000.0
print_info: freq_scale_train = 1
print_info: n_ctx_orig_yarn  = 32768
print_info: rope_yarn_log_mul= 0.0000
print_info: rope_finetuned   = unknown
print_info: model type       = 7B
print_info: model params     = 7.24 B
print_info: general.name     = HuggingFaceH4
print_info: vocab type       = SPM
print_info: n_vocab          = 32000
print_info: n_merges         = 0
print_info: BOS token        = 1 '<s>'
print_info: EOS token        = 2 '</s>'
print_info: UNK token        = 0 '<unk>'
print_info: PAD token        = 2 '</s>'
print_info: LF token         = 13 '<0x0A>'
print_info: EOG token        = 2 '</s>'
print_info: max token length = 48
load_tensors: loading model tensors, this can take a while... (mmap = false)
load_tensors:          CPU model buffer size =  3917.87 MiB
llama_context: constructing llama_context
llama_context: n_seq_max     = 1
llama_context: n_ctx         = 4096
llama_context: n_ctx_seq     = 4096
llama_context: n_batch       = 512
llama_context: n_ubatch      = 512
llama_context: causal_attn   = 1
llama_context: flash_attn    = auto
llama_context: kv_unified    = false
llama_context: freq_base     = 10000.0
llama_context: freq_scale    = 1
llama_context: n_ctx_seq (4096) < n_ctx_train (32768) -- the full capacity of the model will not be utilized
llama_context:        CPU  output buffer size =     0.14 MiB
llama_kv_cache:        CPU KV buffer size =   512.00 MiB
llama_kv_cache: size =  512.00 MiB (  4096 cells,  32 layers,  1/1 seqs), K (f16):  256.00 MiB, V (f16):  256.00 MiB
llama_context: Flash Attention was auto, set to enabled
llama_context:        CPU compute buffer size =   112.01 MiB
llama_context: graph nodes  = 999
llama_context: graph splits = 1
time=2026-03-27T00:45:33.274Z level=INFO source=server.go:1388 msg="llama runner started in 5.08 seconds"
time=2026-03-27T00:45:33.274Z level=INFO source=sched.go:566 msg="loaded runners" count=3
time=2026-03-27T00:45:33.274Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:45:33.274Z level=INFO source=server.go:1388 msg="llama runner started in 5.08 seconds"
llama_model_loader: loaded meta data with 25 key-value pairs and 291 tensors from /root/.ollama/models/blobs/sha256-77bf5506c1e863c73d1f7ed41ecbf27929a04144d19a2688148fabb127d2e692 (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = Nexusflow
llama_model_loader: - kv   2:                           llama.vocab_size u32              = 32002
llama_model_loader: - kv   3:                       llama.context_length u32              = 8192
llama_model_loader: - kv   4:                     llama.embedding_length u32              = 4096
llama_model_loader: - kv   5:                          llama.block_count u32              = 32
llama_model_loader: - kv   6:                  llama.feed_forward_length u32              = 14336
llama_model_loader: - kv   7:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv   8:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv   9:              llama.attention.head_count_kv u32              = 8
llama_model_loader: - kv  10:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  11:                       llama.rope.freq_base f32              = 10000.000000
llama_model_loader: - kv  12:                          general.file_type u32              = 2
llama_model_loader: - kv  13:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  14:                      tokenizer.ggml.tokens arr[str,32002]   = ["<unk>", "<s>", "</s>", "<0x00>", "<...
llama_model_loader: - kv  15:                      tokenizer.ggml.scores arr[f32,32002]   = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  16:                  tokenizer.ggml.token_type arr[i32,32002]   = [2, 3, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, ...
llama_model_loader: - kv  17:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  18:                tokenizer.ggml.eos_token_id u32              = 32000
llama_model_loader: - kv  19:            tokenizer.ggml.unknown_token_id u32              = 0
llama_model_loader: - kv  20:            tokenizer.ggml.padding_token_id u32              = 32000
llama_model_loader: - kv  21:               tokenizer.ggml.add_bos_token bool             = true
llama_model_loader: - kv  22:               tokenizer.ggml.add_eos_token bool             = false
llama_model_loader: - kv  23:                    tokenizer.chat_template str              = {{ bos_token }}{% for message in mess...
llama_model_loader: - kv  24:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   65 tensors
llama_model_loader: - type q4_0:  225 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 3.83 GiB (4.54 BPW) 
load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
load: printing all EOG tokens:
load:   - 32000 ('<|end_of_turn|>')
load: special tokens cache size = 5
load: token to piece cache size = 0.1637 MB
print_info: arch             = llama
print_info: vocab_only       = 1
print_info: no_alloc         = 0
print_info: model type       = ?B
print_info: model params     = 7.24 B
print_info: general.name     = Nexusflow
print_info: vocab type       = SPM
print_info: n_vocab          = 32002
print_info: n_merges         = 0
print_info: BOS token        = 1 '<s>'
print_info: EOS token        = 32000 '<|end_of_turn|>'
print_info: UNK token        = 0 '<unk>'
print_info: PAD token        = 32000 '<|end_of_turn|>'
print_info: LF token         = 13 '<0x0A>'
print_info: EOG token        = 32000 '<|end_of_turn|>'
print_info: max token length = 48
llama_model_load: vocab only - skipping tensors
time=2026-03-27T00:46:15.411Z level=INFO source=server.go:431 msg="starting runner" cmd="/usr/bin/ollama runner --model /root/.ollama/models/blobs/sha256-77bf5506c1e863c73d1f7ed41ecbf27929a04144d19a2688148fabb127d2e692 --port 44123"
time=2026-03-27T00:46:15.412Z level=INFO source=sched.go:491 msg="system memory" total="24.0 GiB" free="16.2 GiB" free_swap="8.0 GiB"
time=2026-03-27T00:46:15.412Z level=INFO source=server.go:498 msg="loading model" "model layers"=33 requested=-1
time=2026-03-27T00:46:15.413Z level=INFO source=device.go:245 msg="model weights" device=CPU size="3.8 GiB"
time=2026-03-27T00:46:15.413Z level=INFO source=device.go:256 msg="kv cache" device=CPU size="512.0 MiB"
time=2026-03-27T00:46:15.413Z level=INFO source=device.go:272 msg="total memory" size="4.3 GiB"
time=2026-03-27T00:46:15.432Z level=INFO source=runner.go:965 msg="starting go runner"
load_backend: loaded CPU backend from /usr/lib/ollama/libggml-cpu-alderlake.so
time=2026-03-27T00:46:15.444Z level=INFO source=ggml.go:104 msg=system CPU.0.SSE3=1 CPU.0.SSSE3=1 CPU.0.AVX=1 CPU.0.AVX_VNNI=1 CPU.0.AVX2=1 CPU.0.F16C=1 CPU.0.FMA=1 CPU.0.BMI2=1 CPU.0.LLAMAFILE=1 CPU.1.LLAMAFILE=1 compiler=cgo(gcc)
time=2026-03-27T00:46:15.445Z level=INFO source=runner.go:1001 msg="Server listening on 127.0.0.1:44123"
time=2026-03-27T00:46:15.457Z level=INFO source=runner.go:895 msg=load request="{Operation:commit LoraPath:[] Parallel:1 BatchSize:512 FlashAttention:Auto KvSize:4096 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:46:15.457Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:46:15.458Z level=INFO source=server.go:1384 msg="waiting for server to become available" status="llm server loading model"
llama_model_loader: loaded meta data with 25 key-value pairs and 291 tensors from /root/.ollama/models/blobs/sha256-77bf5506c1e863c73d1f7ed41ecbf27929a04144d19a2688148fabb127d2e692 (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = Nexusflow
llama_model_loader: - kv   2:                           llama.vocab_size u32              = 32002
llama_model_loader: - kv   3:                       llama.context_length u32              = 8192
llama_model_loader: - kv   4:                     llama.embedding_length u32              = 4096
llama_model_loader: - kv   5:                          llama.block_count u32              = 32
llama_model_loader: - kv   6:                  llama.feed_forward_length u32              = 14336
llama_model_loader: - kv   7:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv   8:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv   9:              llama.attention.head_count_kv u32              = 8
llama_model_loader: - kv  10:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  11:                       llama.rope.freq_base f32              = 10000.000000
llama_model_loader: - kv  12:                          general.file_type u32              = 2
llama_model_loader: - kv  13:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  14:                      tokenizer.ggml.tokens arr[str,32002]   = ["<unk>", "<s>", "</s>", "<0x00>", "<...
llama_model_loader: - kv  15:                      tokenizer.ggml.scores arr[f32,32002]   = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  16:                  tokenizer.ggml.token_type arr[i32,32002]   = [2, 3, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, ...
llama_model_loader: - kv  17:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  18:                tokenizer.ggml.eos_token_id u32              = 32000
llama_model_loader: - kv  19:            tokenizer.ggml.unknown_token_id u32              = 0
llama_model_loader: - kv  20:            tokenizer.ggml.padding_token_id u32              = 32000
llama_model_loader: - kv  21:               tokenizer.ggml.add_bos_token bool             = true
llama_model_loader: - kv  22:               tokenizer.ggml.add_eos_token bool             = false
llama_model_loader: - kv  23:                    tokenizer.chat_template str              = {{ bos_token }}{% for message in mess...
llama_model_loader: - kv  24:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   65 tensors
llama_model_loader: - type q4_0:  225 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 3.83 GiB (4.54 BPW) 
load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
load: printing all EOG tokens:
load:   - 32000 ('<|end_of_turn|>')
load: special tokens cache size = 5
load: token to piece cache size = 0.1637 MB
print_info: arch             = llama
print_info: vocab_only       = 0
print_info: no_alloc         = 0
print_info: n_ctx_train      = 8192
print_info: n_embd           = 4096
print_info: n_embd_inp       = 4096
print_info: n_layer          = 32
print_info: n_head           = 32
print_info: n_head_kv        = 8
print_info: n_rot            = 128
print_info: n_swa            = 0
print_info: is_swa_any       = 0
print_info: n_embd_head_k    = 128
print_info: n_embd_head_v    = 128
print_info: n_gqa            = 4
print_info: n_embd_k_gqa     = 1024
print_info: n_embd_v_gqa     = 1024
print_info: f_norm_eps       = 0.0e+00
print_info: f_norm_rms_eps   = 1.0e-05
print_info: f_clamp_kqv      = 0.0e+00
print_info: f_max_alibi_bias = 0.0e+00
print_info: f_logit_scale    = 0.0e+00
print_info: f_attn_scale     = 0.0e+00
print_info: n_ff             = 14336
print_info: n_expert         = 0
print_info: n_expert_used    = 0
print_info: n_expert_groups  = 0
print_info: n_group_used     = 0
print_info: causal attn      = 1
print_info: pooling type     = 0
print_info: rope type        = 0
print_info: rope scaling     = linear
print_info: freq_base_train  = 10000.0
print_info: freq_scale_train = 1
print_info: n_ctx_orig_yarn  = 8192
print_info: rope_yarn_log_mul= 0.0000
print_info: rope_finetuned   = unknown
print_info: model type       = 7B
print_info: model params     = 7.24 B
print_info: general.name     = Nexusflow
print_info: vocab type       = SPM
print_info: n_vocab          = 32002
print_info: n_merges         = 0
print_info: BOS token        = 1 '<s>'
print_info: EOS token        = 32000 '<|end_of_turn|>'
print_info: UNK token        = 0 '<unk>'
print_info: PAD token        = 32000 '<|end_of_turn|>'
print_info: LF token         = 13 '<0x0A>'
print_info: EOG token        = 32000 '<|end_of_turn|>'
print_info: max token length = 48
load_tensors: loading model tensors, this can take a while... (mmap = false)
load_tensors:          CPU model buffer size =  3917.88 MiB
llama_context: constructing llama_context
llama_context: n_seq_max     = 1
llama_context: n_ctx         = 4096
llama_context: n_ctx_seq     = 4096
llama_context: n_batch       = 512
llama_context: n_ubatch      = 512
llama_context: causal_attn   = 1
llama_context: flash_attn    = auto
llama_context: kv_unified    = false
llama_context: freq_base     = 10000.0
llama_context: freq_scale    = 1
llama_context: n_ctx_seq (4096) < n_ctx_train (8192) -- the full capacity of the model will not be utilized
llama_context:        CPU  output buffer size =     0.14 MiB
llama_kv_cache:        CPU KV buffer size =   512.00 MiB
llama_kv_cache: size =  512.00 MiB (  4096 cells,  32 layers,  1/1 seqs), K (f16):  256.00 MiB, V (f16):  256.00 MiB
llama_context: Flash Attention was auto, set to enabled
llama_context:        CPU compute buffer size =   112.01 MiB
llama_context: graph nodes  = 999
llama_context: graph splits = 1
time=2026-03-27T00:46:19.982Z level=INFO source=server.go:1388 msg="llama runner started in 4.57 seconds"
time=2026-03-27T00:46:19.982Z level=INFO source=sched.go:566 msg="loaded runners" count=3
time=2026-03-27T00:46:19.982Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:46:19.982Z level=INFO source=server.go:1388 msg="llama runner started in 4.57 seconds"
llama_model_loader: loaded meta data with 20 key-value pairs and 291 tensors from /root/.ollama/models/blobs/sha256-bd9d5f911cb214dba65cc678b115d022b042da77507429bd24c5082262209a20 (version GGUF V2)
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = defog
llama_model_loader: - kv   2:                       llama.context_length u32              = 32768
llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
llama_model_loader: - kv   4:                          llama.block_count u32              = 32
llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 14336
llama_model_loader: - kv   6:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv   7:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv   8:              llama.attention.head_count_kv u32              = 8
llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  10:                       llama.rope.freq_base f32              = 10000.000000
llama_model_loader: - kv  11:                          general.file_type u32              = 2
llama_model_loader: - kv  12:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  13:                      tokenizer.ggml.tokens arr[str,32000]   = ["<unk>", "<s>", "</s>", "<0x00>", "<...
llama_model_loader: - kv  14:                      tokenizer.ggml.scores arr[f32,32000]   = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  15:                  tokenizer.ggml.token_type arr[i32,32000]   = [2, 3, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, ...
llama_model_loader: - kv  16:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  17:                tokenizer.ggml.eos_token_id u32              = 2
llama_model_loader: - kv  18:            tokenizer.ggml.unknown_token_id u32              = 0
llama_model_loader: - kv  19:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   65 tensors
llama_model_loader: - type q4_0:  225 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V2
print_info: file type   = Q4_0
print_info: file size   = 3.83 GiB (4.54 BPW) 
load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
load: printing all EOG tokens:
load:   - 2 ('</s>')
load: special tokens cache size = 3
load: token to piece cache size = 0.1637 MB
print_info: arch             = llama
print_info: vocab_only       = 1
print_info: no_alloc         = 0
print_info: model type       = ?B
print_info: model params     = 7.24 B
print_info: general.name     = defog
print_info: vocab type       = SPM
print_info: n_vocab          = 32000
print_info: n_merges         = 0
print_info: BOS token        = 1 '<s>'
print_info: EOS token        = 2 '</s>'
print_info: UNK token        = 0 '<unk>'
print_info: LF token         = 13 '<0x0A>'
print_info: EOG token        = 2 '</s>'
print_info: max token length = 48
llama_model_load: vocab only - skipping tensors
time=2026-03-27T00:46:59.250Z level=INFO source=server.go:431 msg="starting runner" cmd="/usr/bin/ollama runner --model /root/.ollama/models/blobs/sha256-bd9d5f911cb214dba65cc678b115d022b042da77507429bd24c5082262209a20 --port 34469"
time=2026-03-27T00:46:59.250Z level=INFO source=sched.go:491 msg="system memory" total="24.0 GiB" free="16.7 GiB" free_swap="8.0 GiB"
time=2026-03-27T00:46:59.250Z level=INFO source=server.go:498 msg="loading model" "model layers"=33 requested=-1
time=2026-03-27T00:46:59.251Z level=INFO source=device.go:245 msg="model weights" device=CPU size="3.8 GiB"
time=2026-03-27T00:46:59.251Z level=INFO source=device.go:256 msg="kv cache" device=CPU size="512.0 MiB"
time=2026-03-27T00:46:59.251Z level=INFO source=device.go:272 msg="total memory" size="4.3 GiB"
time=2026-03-27T00:46:59.276Z level=INFO source=runner.go:965 msg="starting go runner"
load_backend: loaded CPU backend from /usr/lib/ollama/libggml-cpu-alderlake.so
time=2026-03-27T00:46:59.287Z level=INFO source=ggml.go:104 msg=system CPU.0.SSE3=1 CPU.0.SSSE3=1 CPU.0.AVX=1 CPU.0.AVX_VNNI=1 CPU.0.AVX2=1 CPU.0.F16C=1 CPU.0.FMA=1 CPU.0.BMI2=1 CPU.0.LLAMAFILE=1 CPU.1.LLAMAFILE=1 compiler=cgo(gcc)
time=2026-03-27T00:46:59.288Z level=INFO source=runner.go:1001 msg="Server listening on 127.0.0.1:34469"
time=2026-03-27T00:46:59.295Z level=INFO source=runner.go:895 msg=load request="{Operation:commit LoraPath:[] Parallel:1 BatchSize:512 FlashAttention:Auto KvSize:4096 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:46:59.296Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:46:59.296Z level=INFO source=server.go:1384 msg="waiting for server to become available" status="llm server loading model"
llama_model_loader: loaded meta data with 20 key-value pairs and 291 tensors from /root/.ollama/models/blobs/sha256-bd9d5f911cb214dba65cc678b115d022b042da77507429bd24c5082262209a20 (version GGUF V2)
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = defog
llama_model_loader: - kv   2:                       llama.context_length u32              = 32768
llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
llama_model_loader: - kv   4:                          llama.block_count u32              = 32
llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 14336
llama_model_loader: - kv   6:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv   7:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv   8:              llama.attention.head_count_kv u32              = 8
llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  10:                       llama.rope.freq_base f32              = 10000.000000
llama_model_loader: - kv  11:                          general.file_type u32              = 2
llama_model_loader: - kv  12:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  13:                      tokenizer.ggml.tokens arr[str,32000]   = ["<unk>", "<s>", "</s>", "<0x00>", "<...
llama_model_loader: - kv  14:                      tokenizer.ggml.scores arr[f32,32000]   = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  15:                  tokenizer.ggml.token_type arr[i32,32000]   = [2, 3, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, ...
llama_model_loader: - kv  16:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  17:                tokenizer.ggml.eos_token_id u32              = 2
llama_model_loader: - kv  18:            tokenizer.ggml.unknown_token_id u32              = 0
llama_model_loader: - kv  19:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   65 tensors
llama_model_loader: - type q4_0:  225 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V2
print_info: file type   = Q4_0
print_info: file size   = 3.83 GiB (4.54 BPW) 
load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
load: printing all EOG tokens:
load:   - 2 ('</s>')
load: special tokens cache size = 3
load: token to piece cache size = 0.1637 MB
print_info: arch             = llama
print_info: vocab_only       = 0
print_info: no_alloc         = 0
print_info: n_ctx_train      = 32768
print_info: n_embd           = 4096
print_info: n_embd_inp       = 4096
print_info: n_layer          = 32
print_info: n_head           = 32
print_info: n_head_kv        = 8
print_info: n_rot            = 128
print_info: n_swa            = 0
print_info: is_swa_any       = 0
print_info: n_embd_head_k    = 128
print_info: n_embd_head_v    = 128
print_info: n_gqa            = 4
print_info: n_embd_k_gqa     = 1024
print_info: n_embd_v_gqa     = 1024
print_info: f_norm_eps       = 0.0e+00
print_info: f_norm_rms_eps   = 1.0e-05
print_info: f_clamp_kqv      = 0.0e+00
print_info: f_max_alibi_bias = 0.0e+00
print_info: f_logit_scale    = 0.0e+00
print_info: f_attn_scale     = 0.0e+00
print_info: n_ff             = 14336
print_info: n_expert         = 0
print_info: n_expert_used    = 0
print_info: n_expert_groups  = 0
print_info: n_group_used     = 0
print_info: causal attn      = 1
print_info: pooling type     = 0
print_info: rope type        = 0
print_info: rope scaling     = linear
print_info: freq_base_train  = 10000.0
print_info: freq_scale_train = 1
print_info: n_ctx_orig_yarn  = 32768
print_info: rope_yarn_log_mul= 0.0000
print_info: rope_finetuned   = unknown
print_info: model type       = 7B
print_info: model params     = 7.24 B
print_info: general.name     = defog
print_info: vocab type       = SPM
print_info: n_vocab          = 32000
print_info: n_merges         = 0
print_info: BOS token        = 1 '<s>'
print_info: EOS token        = 2 '</s>'
print_info: UNK token        = 0 '<unk>'
print_info: LF token         = 13 '<0x0A>'
print_info: EOG token        = 2 '</s>'
print_info: max token length = 48
load_tensors: loading model tensors, this can take a while... (mmap = false)
load_tensors:          CPU model buffer size =  3917.87 MiB
llama_context: constructing llama_context
llama_context: n_seq_max     = 1
llama_context: n_ctx         = 4096
llama_context: n_ctx_seq     = 4096
llama_context: n_batch       = 512
llama_context: n_ubatch      = 512
llama_context: causal_attn   = 1
llama_context: flash_attn    = auto
llama_context: kv_unified    = false
llama_context: freq_base     = 10000.0
llama_context: freq_scale    = 1
llama_context: n_ctx_seq (4096) < n_ctx_train (32768) -- the full capacity of the model will not be utilized
llama_context:        CPU  output buffer size =     0.14 MiB
llama_kv_cache:        CPU KV buffer size =   512.00 MiB
llama_kv_cache: size =  512.00 MiB (  4096 cells,  32 layers,  1/1 seqs), K (f16):  256.00 MiB, V (f16):  256.00 MiB
llama_context: Flash Attention was auto, set to enabled
llama_context:        CPU compute buffer size =   112.01 MiB
llama_context: graph nodes  = 999
llama_context: graph splits = 1
time=2026-03-27T00:47:04.577Z level=INFO source=server.go:1388 msg="llama runner started in 5.33 seconds"
time=2026-03-27T00:47:04.577Z level=INFO source=sched.go:566 msg="loaded runners" count=3
time=2026-03-27T00:47:04.577Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:47:04.577Z level=INFO source=server.go:1388 msg="llama runner started in 5.33 seconds"
llama_model_loader: loaded meta data with 19 key-value pairs and 291 tensors from /root/.ollama/models/blobs/sha256-f050c123dbd6006182412343ad6185c2d01316887e9cd77531d2aaf0060d6756 (version GGUF V2)
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = LLaMA v2
llama_model_loader: - kv   2:                       llama.context_length u32              = 4096
llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
llama_model_loader: - kv   4:                          llama.block_count u32              = 32
llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 11008
llama_model_loader: - kv   6:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv   7:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv   8:              llama.attention.head_count_kv u32              = 32
llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  10:                          general.file_type u32              = 2
llama_model_loader: - kv  11:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  12:                      tokenizer.ggml.tokens arr[str,32000]   = ["<unk>", "<s>", "</s>", "<0x00>", "<...
llama_model_loader: - kv  13:                      tokenizer.ggml.scores arr[f32,32000]   = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  14:                  tokenizer.ggml.token_type arr[i32,32000]   = [2, 3, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, ...
llama_model_loader: - kv  15:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  16:                tokenizer.ggml.eos_token_id u32              = 2
llama_model_loader: - kv  17:            tokenizer.ggml.unknown_token_id u32              = 0
llama_model_loader: - kv  18:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   65 tensors
llama_model_loader: - type q4_0:  225 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V2
print_info: file type   = Q4_0
print_info: file size   = 3.56 GiB (4.54 BPW) 
load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
load: printing all EOG tokens:
load:   - 2 ('</s>')
load: special tokens cache size = 3
load: token to piece cache size = 0.1684 MB
print_info: arch             = llama
print_info: vocab_only       = 1
print_info: no_alloc         = 0
print_info: model type       = ?B
print_info: model params     = 6.74 B
print_info: general.name     = LLaMA v2
print_info: vocab type       = SPM
print_info: n_vocab          = 32000
print_info: n_merges         = 0
print_info: BOS token        = 1 '<s>'
print_info: EOS token        = 2 '</s>'
print_info: UNK token        = 0 '<unk>'
print_info: LF token         = 13 '<0x0A>'
print_info: EOG token        = 2 '</s>'
print_info: max token length = 48
llama_model_load: vocab only - skipping tensors
time=2026-03-27T00:47:12.766Z level=INFO source=server.go:431 msg="starting runner" cmd="/usr/bin/ollama runner --model /root/.ollama/models/blobs/sha256-f050c123dbd6006182412343ad6185c2d01316887e9cd77531d2aaf0060d6756 --port 45175"
time=2026-03-27T00:47:12.766Z level=INFO source=sched.go:491 msg="system memory" total="24.0 GiB" free="11.8 GiB" free_swap="8.0 GiB"
time=2026-03-27T00:47:12.766Z level=INFO source=server.go:498 msg="loading model" "model layers"=33 requested=-1
time=2026-03-27T00:47:12.767Z level=INFO source=device.go:245 msg="model weights" device=CPU size="3.5 GiB"
time=2026-03-27T00:47:12.767Z level=INFO source=device.go:256 msg="kv cache" device=CPU size="2.0 GiB"
time=2026-03-27T00:47:12.767Z level=INFO source=device.go:272 msg="total memory" size="5.5 GiB"
time=2026-03-27T00:47:12.793Z level=INFO source=runner.go:965 msg="starting go runner"
load_backend: loaded CPU backend from /usr/lib/ollama/libggml-cpu-alderlake.so
time=2026-03-27T00:47:12.806Z level=INFO source=ggml.go:104 msg=system CPU.0.SSE3=1 CPU.0.SSSE3=1 CPU.0.AVX=1 CPU.0.AVX_VNNI=1 CPU.0.AVX2=1 CPU.0.F16C=1 CPU.0.FMA=1 CPU.0.BMI2=1 CPU.0.LLAMAFILE=1 CPU.1.LLAMAFILE=1 compiler=cgo(gcc)
time=2026-03-27T00:47:12.806Z level=INFO source=runner.go:1001 msg="Server listening on 127.0.0.1:45175"
time=2026-03-27T00:47:12.812Z level=INFO source=runner.go:895 msg=load request="{Operation:commit LoraPath:[] Parallel:1 BatchSize:512 FlashAttention:Auto KvSize:4096 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:47:12.813Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:47:12.813Z level=INFO source=server.go:1384 msg="waiting for server to become available" status="llm server loading model"
llama_model_loader: loaded meta data with 19 key-value pairs and 291 tensors from /root/.ollama/models/blobs/sha256-f050c123dbd6006182412343ad6185c2d01316887e9cd77531d2aaf0060d6756 (version GGUF V2)
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = LLaMA v2
llama_model_loader: - kv   2:                       llama.context_length u32              = 4096
llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
llama_model_loader: - kv   4:                          llama.block_count u32              = 32
llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 11008
llama_model_loader: - kv   6:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv   7:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv   8:              llama.attention.head_count_kv u32              = 32
llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  10:                          general.file_type u32              = 2
llama_model_loader: - kv  11:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  12:                      tokenizer.ggml.tokens arr[str,32000]   = ["<unk>", "<s>", "</s>", "<0x00>", "<...
llama_model_loader: - kv  13:                      tokenizer.ggml.scores arr[f32,32000]   = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  14:                  tokenizer.ggml.token_type arr[i32,32000]   = [2, 3, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, ...
llama_model_loader: - kv  15:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  16:                tokenizer.ggml.eos_token_id u32              = 2
llama_model_loader: - kv  17:            tokenizer.ggml.unknown_token_id u32              = 0
llama_model_loader: - kv  18:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   65 tensors
llama_model_loader: - type q4_0:  225 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V2
print_info: file type   = Q4_0
print_info: file size   = 3.56 GiB (4.54 BPW) 
load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
load: printing all EOG tokens:
load:   - 2 ('</s>')
load: special tokens cache size = 3
load: token to piece cache size = 0.1684 MB
print_info: arch             = llama
print_info: vocab_only       = 0
print_info: no_alloc         = 0
print_info: n_ctx_train      = 4096
print_info: n_embd           = 4096
print_info: n_embd_inp       = 4096
print_info: n_layer          = 32
print_info: n_head           = 32
print_info: n_head_kv        = 32
print_info: n_rot            = 128
print_info: n_swa            = 0
print_info: is_swa_any       = 0
print_info: n_embd_head_k    = 128
print_info: n_embd_head_v    = 128
print_info: n_gqa            = 1
print_info: n_embd_k_gqa     = 4096
print_info: n_embd_v_gqa     = 4096
print_info: f_norm_eps       = 0.0e+00
print_info: f_norm_rms_eps   = 1.0e-05
print_info: f_clamp_kqv      = 0.0e+00
print_info: f_max_alibi_bias = 0.0e+00
print_info: f_logit_scale    = 0.0e+00
print_info: f_attn_scale     = 0.0e+00
print_info: n_ff             = 11008
print_info: n_expert         = 0
print_info: n_expert_used    = 0
print_info: n_expert_groups  = 0
print_info: n_group_used     = 0
print_info: causal attn      = 1
print_info: pooling type     = 0
print_info: rope type        = 0
print_info: rope scaling     = linear
print_info: freq_base_train  = 10000.0
print_info: freq_scale_train = 1
print_info: n_ctx_orig_yarn  = 4096
print_info: rope_yarn_log_mul= 0.0000
print_info: rope_finetuned   = unknown
print_info: model type       = 7B
print_info: model params     = 6.74 B
print_info: general.name     = LLaMA v2
print_info: vocab type       = SPM
print_info: n_vocab          = 32000
print_info: n_merges         = 0
print_info: BOS token        = 1 '<s>'
print_info: EOS token        = 2 '</s>'
print_info: UNK token        = 0 '<unk>'
print_info: LF token         = 13 '<0x0A>'
print_info: EOG token        = 2 '</s>'
print_info: max token length = 48
load_tensors: loading model tensors, this can take a while... (mmap = false)
load_tensors:          CPU model buffer size =  3647.87 MiB
llama_context: constructing llama_context
llama_context: n_seq_max     = 1
llama_context: n_ctx         = 4096
llama_context: n_ctx_seq     = 4096
llama_context: n_batch       = 512
llama_context: n_ubatch      = 512
llama_context: causal_attn   = 1
llama_context: flash_attn    = auto
llama_context: kv_unified    = false
llama_context: freq_base     = 10000.0
llama_context: freq_scale    = 1
llama_context:        CPU  output buffer size =     0.14 MiB
llama_kv_cache:        CPU KV buffer size =  2048.00 MiB
llama_kv_cache: size = 2048.00 MiB (  4096 cells,  32 layers,  1/1 seqs), K (f16): 1024.00 MiB, V (f16): 1024.00 MiB
llama_context: Flash Attention was auto, set to enabled
llama_context:        CPU compute buffer size =    92.51 MiB
llama_context: graph nodes  = 999
llama_context: graph splits = 1
time=2026-03-27T00:47:19.099Z level=INFO source=server.go:1388 msg="llama runner started in 6.33 seconds"
time=2026-03-27T00:47:19.099Z level=INFO source=sched.go:566 msg="loaded runners" count=3
time=2026-03-27T00:47:19.099Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:47:19.100Z level=INFO source=server.go:1388 msg="llama runner started in 6.33 seconds"
time=2026-03-27T00:47:38.399Z level=WARN source=server.go:209 msg="flash attention enabled but not supported by model"
time=2026-03-27T00:47:38.400Z level=INFO source=server.go:431 msg="starting runner" cmd="/usr/bin/ollama runner --ollama-engine --model /root/.ollama/models/blobs/sha256-797b70c4edf85907fe0a49eb85811256f65fa0f7bf52166b147fd16be2be4662 --port 46515"
time=2026-03-27T00:47:38.400Z level=INFO source=sched.go:491 msg="system memory" total="24.0 GiB" free="16.2 GiB" free_swap="8.0 GiB"
time=2026-03-27T00:47:38.400Z level=INFO source=server.go:757 msg="loading model" "model layers"=7 requested=-1
time=2026-03-27T00:47:38.426Z level=INFO source=runner.go:1411 msg="starting ollama engine"
time=2026-03-27T00:47:38.426Z level=INFO source=runner.go:1446 msg="Server listening on 127.0.0.1:46515"
time=2026-03-27T00:47:38.434Z level=INFO source=runner.go:1284 msg=load request="{Operation:fit LoraPath:[] Parallel:1 BatchSize:256 FlashAttention:Disabled KvSize:256 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:47:38.450Z level=INFO source=ggml.go:136 msg="" architecture=bert file_type=F16 name=all-MiniLM-L6-v2 description="" num_tensors=101 num_key_values=24
load_backend: loaded CPU backend from /usr/lib/ollama/libggml-cpu-alderlake.so
time=2026-03-27T00:47:38.474Z level=INFO source=ggml.go:104 msg=system CPU.0.SSE3=1 CPU.0.SSSE3=1 CPU.0.AVX=1 CPU.0.AVX_VNNI=1 CPU.0.AVX2=1 CPU.0.F16C=1 CPU.0.FMA=1 CPU.0.BMI2=1 CPU.0.LLAMAFILE=1 CPU.1.LLAMAFILE=1 compiler=cgo(gcc)
time=2026-03-27T00:47:38.479Z level=INFO source=runner.go:1284 msg=load request="{Operation:alloc LoraPath:[] Parallel:1 BatchSize:256 FlashAttention:Disabled KvSize:256 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:47:38.496Z level=INFO source=runner.go:1284 msg=load request="{Operation:commit LoraPath:[] Parallel:1 BatchSize:256 FlashAttention:Disabled KvSize:256 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:47:38.496Z level=INFO source=device.go:245 msg="model weights" device=CPU size="65.5 MiB"
time=2026-03-27T00:47:38.496Z level=INFO source=ggml.go:482 msg="offloading 0 repeating layers to GPU"
time=2026-03-27T00:47:38.497Z level=INFO source=ggml.go:486 msg="offloading output layer to CPU"
time=2026-03-27T00:47:38.497Z level=INFO source=ggml.go:494 msg="offloaded 0/7 layers to GPU"
time=2026-03-27T00:47:38.497Z level=INFO source=device.go:267 msg="compute graph" device=CPU size="4.9 MiB"
time=2026-03-27T00:47:38.497Z level=INFO source=device.go:272 msg="total memory" size="70.3 MiB"
time=2026-03-27T00:47:38.497Z level=INFO source=sched.go:566 msg="loaded runners" count=3
time=2026-03-27T00:47:38.497Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:47:38.497Z level=INFO source=server.go:1384 msg="waiting for server to become available" status="llm server loading model"
time=2026-03-27T00:47:38.749Z level=INFO source=server.go:1388 msg="llama runner started in 0.35 seconds"
llama_model_loader: loaded meta data with 24 key-value pairs and 291 tensors from /root/.ollama/models/blobs/sha256-170370233dd5c5415250a2ecd5c71586352850729062ccef1496385647293868 (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = liuhaotian
llama_model_loader: - kv   2:                       llama.context_length u32              = 32768
llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
llama_model_loader: - kv   4:                          llama.block_count u32              = 32
llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 14336
llama_model_loader: - kv   6:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv   7:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv   8:              llama.attention.head_count_kv u32              = 8
llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  10:                       llama.rope.freq_base f32              = 1000000.000000
llama_model_loader: - kv  11:                          general.file_type u32              = 2
llama_model_loader: - kv  12:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  13:                      tokenizer.ggml.tokens arr[str,32000]   = ["<unk>", "<s>", "</s>", "<0x00>", "<...
llama_model_loader: - kv  14:                      tokenizer.ggml.scores arr[f32,32000]   = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  15:                  tokenizer.ggml.token_type arr[i32,32000]   = [2, 3, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, ...
llama_model_loader: - kv  16:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  17:                tokenizer.ggml.eos_token_id u32              = 2
llama_model_loader: - kv  18:            tokenizer.ggml.unknown_token_id u32              = 0
llama_model_loader: - kv  19:            tokenizer.ggml.padding_token_id u32              = 0
llama_model_loader: - kv  20:               tokenizer.ggml.add_bos_token bool             = true
llama_model_loader: - kv  21:               tokenizer.ggml.add_eos_token bool             = false
llama_model_loader: - kv  22:                    tokenizer.chat_template str              = {{ bos_token }}{% for message in mess...
llama_model_loader: - kv  23:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   65 tensors
llama_model_loader: - type q4_0:  225 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 3.83 GiB (4.54 BPW) 
load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
load: printing all EOG tokens:
load:   - 2 ('</s>')
load: special tokens cache size = 3
load: token to piece cache size = 0.1637 MB
print_info: arch             = llama
print_info: vocab_only       = 1
print_info: no_alloc         = 0
print_info: model type       = ?B
print_info: model params     = 7.24 B
print_info: general.name     = liuhaotian
print_info: vocab type       = SPM
print_info: n_vocab          = 32000
print_info: n_merges         = 0
print_info: BOS token        = 1 '<s>'
print_info: EOS token        = 2 '</s>'
print_info: UNK token        = 0 '<unk>'
print_info: PAD token        = 0 '<unk>'
print_info: LF token         = 13 '<0x0A>'
print_info: EOG token        = 2 '</s>'
print_info: max token length = 48
llama_model_load: vocab only - skipping tensors
time=2026-03-27T00:48:00.231Z level=INFO source=server.go:431 msg="starting runner" cmd="/usr/bin/ollama runner --model /root/.ollama/models/blobs/sha256-170370233dd5c5415250a2ecd5c71586352850729062ccef1496385647293868 --port 44677"
time=2026-03-27T00:48:00.232Z level=INFO source=sched.go:491 msg="system memory" total="24.0 GiB" free="17.8 GiB" free_swap="8.0 GiB"
time=2026-03-27T00:48:00.232Z level=INFO source=server.go:498 msg="loading model" "model layers"=33 requested=-1
time=2026-03-27T00:48:00.232Z level=INFO source=device.go:245 msg="model weights" device=CPU size="3.8 GiB"
time=2026-03-27T00:48:00.232Z level=INFO source=device.go:256 msg="kv cache" device=CPU size="512.0 MiB"
time=2026-03-27T00:48:00.232Z level=INFO source=device.go:272 msg="total memory" size="4.3 GiB"
time=2026-03-27T00:48:00.257Z level=INFO source=runner.go:965 msg="starting go runner"
load_backend: loaded CPU backend from /usr/lib/ollama/libggml-cpu-alderlake.so
time=2026-03-27T00:48:00.270Z level=INFO source=ggml.go:104 msg=system CPU.0.SSE3=1 CPU.0.SSSE3=1 CPU.0.AVX=1 CPU.0.AVX_VNNI=1 CPU.0.AVX2=1 CPU.0.F16C=1 CPU.0.FMA=1 CPU.0.BMI2=1 CPU.0.LLAMAFILE=1 CPU.1.LLAMAFILE=1 compiler=cgo(gcc)
time=2026-03-27T00:48:00.271Z level=INFO source=runner.go:1001 msg="Server listening on 127.0.0.1:44677"
time=2026-03-27T00:48:00.278Z level=INFO source=runner.go:895 msg=load request="{Operation:commit LoraPath:[] Parallel:1 BatchSize:512 FlashAttention:Auto KvSize:4096 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath:/root/.ollama/models/blobs/sha256-72d6f08a42f656d36b356dbe0920675899a99ce21192fd66266fb7d82ed07539 MainGPU:0 UseMmap:false}"
time=2026-03-27T00:48:00.278Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:48:00.279Z level=INFO source=server.go:1384 msg="waiting for server to become available" status="llm server loading model"
llama_model_loader: loaded meta data with 24 key-value pairs and 291 tensors from /root/.ollama/models/blobs/sha256-170370233dd5c5415250a2ecd5c71586352850729062ccef1496385647293868 (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = liuhaotian
llama_model_loader: - kv   2:                       llama.context_length u32              = 32768
llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
llama_model_loader: - kv   4:                          llama.block_count u32              = 32
llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 14336
llama_model_loader: - kv   6:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv   7:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv   8:              llama.attention.head_count_kv u32              = 8
llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  10:                       llama.rope.freq_base f32              = 1000000.000000
llama_model_loader: - kv  11:                          general.file_type u32              = 2
llama_model_loader: - kv  12:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  13:                      tokenizer.ggml.tokens arr[str,32000]   = ["<unk>", "<s>", "</s>", "<0x00>", "<...
llama_model_loader: - kv  14:                      tokenizer.ggml.scores arr[f32,32000]   = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  15:                  tokenizer.ggml.token_type arr[i32,32000]   = [2, 3, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, ...
llama_model_loader: - kv  16:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  17:                tokenizer.ggml.eos_token_id u32              = 2
llama_model_loader: - kv  18:            tokenizer.ggml.unknown_token_id u32              = 0
llama_model_loader: - kv  19:            tokenizer.ggml.padding_token_id u32              = 0
llama_model_loader: - kv  20:               tokenizer.ggml.add_bos_token bool             = true
llama_model_loader: - kv  21:               tokenizer.ggml.add_eos_token bool             = false
llama_model_loader: - kv  22:                    tokenizer.chat_template str              = {{ bos_token }}{% for message in mess...
llama_model_loader: - kv  23:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   65 tensors
llama_model_loader: - type q4_0:  225 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 3.83 GiB (4.54 BPW) 
load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
load: printing all EOG tokens:
load:   - 2 ('</s>')
load: special tokens cache size = 3
load: token to piece cache size = 0.1637 MB
print_info: arch             = llama
print_info: vocab_only       = 0
print_info: no_alloc         = 0
print_info: n_ctx_train      = 32768
print_info: n_embd           = 4096
print_info: n_embd_inp       = 4096
print_info: n_layer          = 32
print_info: n_head           = 32
print_info: n_head_kv        = 8
print_info: n_rot            = 128
print_info: n_swa            = 0
print_info: is_swa_any       = 0
print_info: n_embd_head_k    = 128
print_info: n_embd_head_v    = 128
print_info: n_gqa            = 4
print_info: n_embd_k_gqa     = 1024
print_info: n_embd_v_gqa     = 1024
print_info: f_norm_eps       = 0.0e+00
print_info: f_norm_rms_eps   = 1.0e-05
print_info: f_clamp_kqv      = 0.0e+00
print_info: f_max_alibi_bias = 0.0e+00
print_info: f_logit_scale    = 0.0e+00
print_info: f_attn_scale     = 0.0e+00
print_info: n_ff             = 14336
print_info: n_expert         = 0
print_info: n_expert_used    = 0
print_info: n_expert_groups  = 0
print_info: n_group_used     = 0
print_info: causal attn      = 1
print_info: pooling type     = 0
print_info: rope type        = 0
print_info: rope scaling     = linear
print_info: freq_base_train  = 1000000.0
print_info: freq_scale_train = 1
print_info: n_ctx_orig_yarn  = 32768
print_info: rope_yarn_log_mul= 0.0000
print_info: rope_finetuned   = unknown
print_info: model type       = 7B
print_info: model params     = 7.24 B
print_info: general.name     = liuhaotian
print_info: vocab type       = SPM
print_info: n_vocab          = 32000
print_info: n_merges         = 0
print_info: BOS token        = 1 '<s>'
print_info: EOS token        = 2 '</s>'
print_info: UNK token        = 0 '<unk>'
print_info: PAD token        = 0 '<unk>'
print_info: LF token         = 13 '<0x0A>'
print_info: EOG token        = 2 '</s>'
print_info: max token length = 48
load_tensors: loading model tensors, this can take a while... (mmap = false)
load_tensors:          CPU model buffer size =  3917.87 MiB
llama_context: constructing llama_context
llama_context: n_seq_max     = 1
llama_context: n_ctx         = 4096
llama_context: n_ctx_seq     = 4096
llama_context: n_batch       = 512
llama_context: n_ubatch      = 512
llama_context: causal_attn   = 1
llama_context: flash_attn    = auto
llama_context: kv_unified    = false
llama_context: freq_base     = 1000000.0
llama_context: freq_scale    = 1
llama_context: n_ctx_seq (4096) < n_ctx_train (32768) -- the full capacity of the model will not be utilized
llama_context:        CPU  output buffer size =     0.14 MiB
llama_kv_cache:        CPU KV buffer size =   512.00 MiB
llama_kv_cache: size =  512.00 MiB (  4096 cells,  32 layers,  1/1 seqs), K (f16):  256.00 MiB, V (f16):  256.00 MiB
llama_context: Flash Attention was auto, set to enabled
llama_context:        CPU compute buffer size =   112.01 MiB
llama_context: graph nodes  = 999
llama_context: graph splits = 1
clip_model_loader: model name:   openai/clip-vit-large-patch14-336
clip_model_loader: description:  image encoder for LLaVA
clip_model_loader: GGUF version: 3
clip_model_loader: alignment:    32
clip_model_loader: n_tensors:    377
clip_model_loader: n_kv:         19

clip_model_loader: has vision encoder
clip_model_loader: tensor[0]: n_dims = 1, name = mm.0.bias, tensor_size=16384, offset=0, shape:[4096, 1, 1, 1], type = f32
clip_model_loader: tensor[1]: n_dims = 2, name = mm.0.weight, tensor_size=8388608, offset=16384, shape:[1024, 4096, 1, 1], type = f16
clip_model_loader: tensor[2]: n_dims = 1, name = mm.2.bias, tensor_size=16384, offset=8404992, shape:[4096, 1, 1, 1], type = f32
clip_model_loader: tensor[3]: n_dims = 2, name = mm.2.weight, tensor_size=33554432, offset=8421376, shape:[4096, 4096, 1, 1], type = f16
clip_model_loader: tensor[4]: n_dims = 1, name = v.class_embd, tensor_size=4096, offset=41975808, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[5]: n_dims = 4, name = v.patch_embd.weight, tensor_size=1204224, offset=41979904, shape:[14, 14, 3, 1024], type = f16
clip_model_loader: tensor[6]: n_dims = 2, name = v.position_embd.weight, tensor_size=1181696, offset=43184128, shape:[1024, 577, 1, 1], type = f16
clip_model_loader: tensor[7]: n_dims = 1, name = v.pre_ln.weight, tensor_size=4096, offset=44365824, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[8]: n_dims = 1, name = v.pre_ln.bias, tensor_size=4096, offset=44369920, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[9]: n_dims = 2, name = v.blk.0.attn_k.weight, tensor_size=2097152, offset=44374016, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[10]: n_dims = 1, name = v.blk.0.attn_k.bias, tensor_size=4096, offset=46471168, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[11]: n_dims = 2, name = v.blk.0.attn_v.weight, tensor_size=2097152, offset=46475264, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[12]: n_dims = 1, name = v.blk.0.attn_v.bias, tensor_size=4096, offset=48572416, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[13]: n_dims = 2, name = v.blk.0.attn_q.weight, tensor_size=2097152, offset=48576512, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[14]: n_dims = 1, name = v.blk.0.attn_q.bias, tensor_size=4096, offset=50673664, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[15]: n_dims = 2, name = v.blk.0.attn_out.weight, tensor_size=2097152, offset=50677760, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[16]: n_dims = 1, name = v.blk.0.attn_out.bias, tensor_size=4096, offset=52774912, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[17]: n_dims = 1, name = v.blk.0.ln1.weight, tensor_size=4096, offset=52779008, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[18]: n_dims = 1, name = v.blk.0.ln1.bias, tensor_size=4096, offset=52783104, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[19]: n_dims = 2, name = v.blk.0.ffn_down.weight, tensor_size=8388608, offset=52787200, shape:[1024, 4096, 1, 1], type = f16
clip_model_loader: tensor[20]: n_dims = 1, name = v.blk.0.ffn_down.bias, tensor_size=16384, offset=61175808, shape:[4096, 1, 1, 1], type = f32
clip_model_loader: tensor[21]: n_dims = 2, name = v.blk.0.ffn_up.weight, tensor_size=8388608, offset=61192192, shape:[4096, 1024, 1, 1], type = f16
clip_model_loader: tensor[22]: n_dims = 1, name = v.blk.0.ffn_up.bias, tensor_size=4096, offset=69580800, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[23]: n_dims = 1, name = v.blk.0.ln2.weight, tensor_size=4096, offset=69584896, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[24]: n_dims = 1, name = v.blk.0.ln2.bias, tensor_size=4096, offset=69588992, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[25]: n_dims = 2, name = v.blk.1.attn_k.weight, tensor_size=2097152, offset=69593088, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[26]: n_dims = 1, name = v.blk.1.attn_k.bias, tensor_size=4096, offset=71690240, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[27]: n_dims = 2, name = v.blk.1.attn_v.weight, tensor_size=2097152, offset=71694336, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[28]: n_dims = 1, name = v.blk.1.attn_v.bias, tensor_size=4096, offset=73791488, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[29]: n_dims = 2, name = v.blk.1.attn_q.weight, tensor_size=2097152, offset=73795584, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[30]: n_dims = 1, name = v.blk.1.attn_q.bias, tensor_size=4096, offset=75892736, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[31]: n_dims = 2, name = v.blk.1.attn_out.weight, tensor_size=2097152, offset=75896832, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[32]: n_dims = 1, name = v.blk.1.attn_out.bias, tensor_size=4096, offset=77993984, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[33]: n_dims = 1, name = v.blk.1.ln1.weight, tensor_size=4096, offset=77998080, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[34]: n_dims = 1, name = v.blk.1.ln1.bias, tensor_size=4096, offset=78002176, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[35]: n_dims = 2, name = v.blk.1.ffn_down.weight, tensor_size=8388608, offset=78006272, shape:[1024, 4096, 1, 1], type = f16
clip_model_loader: tensor[36]: n_dims = 1, name = v.blk.1.ffn_down.bias, tensor_size=16384, offset=86394880, shape:[4096, 1, 1, 1], type = f32
clip_model_loader: tensor[37]: n_dims = 2, name = v.blk.1.ffn_up.weight, tensor_size=8388608, offset=86411264, shape:[4096, 1024, 1, 1], type = f16
clip_model_loader: tensor[38]: n_dims = 1, name = v.blk.1.ffn_up.bias, tensor_size=4096, offset=94799872, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[39]: n_dims = 1, name = v.blk.1.ln2.weight, tensor_size=4096, offset=94803968, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[40]: n_dims = 1, name = v.blk.1.ln2.bias, tensor_size=4096, offset=94808064, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[41]: n_dims = 2, name = v.blk.2.attn_k.weight, tensor_size=2097152, offset=94812160, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[42]: n_dims = 1, name = v.blk.2.attn_k.bias, tensor_size=4096, offset=96909312, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[43]: n_dims = 2, name = v.blk.2.attn_v.weight, tensor_size=2097152, offset=96913408, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[44]: n_dims = 1, name = v.blk.2.attn_v.bias, tensor_size=4096, offset=99010560, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[45]: n_dims = 2, name = v.blk.2.attn_q.weight, tensor_size=2097152, offset=99014656, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[46]: n_dims = 1, name = v.blk.2.attn_q.bias, tensor_size=4096, offset=101111808, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[47]: n_dims = 2, name = v.blk.2.attn_out.weight, tensor_size=2097152, offset=101115904, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[48]: n_dims = 1, name = v.blk.2.attn_out.bias, tensor_size=4096, offset=103213056, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[49]: n_dims = 1, name = v.blk.2.ln1.weight, tensor_size=4096, offset=103217152, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[50]: n_dims = 1, name = v.blk.2.ln1.bias, tensor_size=4096, offset=103221248, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[51]: n_dims = 2, name = v.blk.2.ffn_down.weight, tensor_size=8388608, offset=103225344, shape:[1024, 4096, 1, 1], type = f16
clip_model_loader: tensor[52]: n_dims = 1, name = v.blk.2.ffn_down.bias, tensor_size=16384, offset=111613952, shape:[4096, 1, 1, 1], type = f32
clip_model_loader: tensor[53]: n_dims = 2, name = v.blk.2.ffn_up.weight, tensor_size=8388608, offset=111630336, shape:[4096, 1024, 1, 1], type = f16
clip_model_loader: tensor[54]: n_dims = 1, name = v.blk.2.ffn_up.bias, tensor_size=4096, offset=120018944, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[55]: n_dims = 1, name = v.blk.2.ln2.weight, tensor_size=4096, offset=120023040, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[56]: n_dims = 1, name = v.blk.2.ln2.bias, tensor_size=4096, offset=120027136, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[57]: n_dims = 2, name = v.blk.3.attn_k.weight, tensor_size=2097152, offset=120031232, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[58]: n_dims = 1, name = v.blk.3.attn_k.bias, tensor_size=4096, offset=122128384, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[59]: n_dims = 2, name = v.blk.3.attn_v.weight, tensor_size=2097152, offset=122132480, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[60]: n_dims = 1, name = v.blk.3.attn_v.bias, tensor_size=4096, offset=124229632, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[61]: n_dims = 2, name = v.blk.3.attn_q.weight, tensor_size=2097152, offset=124233728, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[62]: n_dims = 1, name = v.blk.3.attn_q.bias, tensor_size=4096, offset=126330880, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[63]: n_dims = 2, name = v.blk.3.attn_out.weight, tensor_size=2097152, offset=126334976, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[64]: n_dims = 1, name = v.blk.3.attn_out.bias, tensor_size=4096, offset=128432128, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[65]: n_dims = 1, name = v.blk.3.ln1.weight, tensor_size=4096, offset=128436224, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[66]: n_dims = 1, name = v.blk.3.ln1.bias, tensor_size=4096, offset=128440320, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[67]: n_dims = 2, name = v.blk.3.ffn_down.weight, tensor_size=8388608, offset=128444416, shape:[1024, 4096, 1, 1], type = f16
clip_model_loader: tensor[68]: n_dims = 1, name = v.blk.3.ffn_down.bias, tensor_size=16384, offset=136833024, shape:[4096, 1, 1, 1], type = f32
clip_model_loader: tensor[69]: n_dims = 2, name = v.blk.3.ffn_up.weight, tensor_size=8388608, offset=136849408, shape:[4096, 1024, 1, 1], type = f16
clip_model_loader: tensor[70]: n_dims = 1, name = v.blk.3.ffn_up.bias, tensor_size=4096, offset=145238016, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[71]: n_dims = 1, name = v.blk.3.ln2.weight, tensor_size=4096, offset=145242112, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[72]: n_dims = 1, name = v.blk.3.ln2.bias, tensor_size=4096, offset=145246208, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[73]: n_dims = 2, name = v.blk.4.attn_k.weight, tensor_size=2097152, offset=145250304, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[74]: n_dims = 1, name = v.blk.4.attn_k.bias, tensor_size=4096, offset=147347456, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[75]: n_dims = 2, name = v.blk.4.attn_v.weight, tensor_size=2097152, offset=147351552, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[76]: n_dims = 1, name = v.blk.4.attn_v.bias, tensor_size=4096, offset=149448704, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[77]: n_dims = 2, name = v.blk.4.attn_q.weight, tensor_size=2097152, offset=149452800, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[78]: n_dims = 1, name = v.blk.4.attn_q.bias, tensor_size=4096, offset=151549952, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[79]: n_dims = 2, name = v.blk.4.attn_out.weight, tensor_size=2097152, offset=151554048, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[80]: n_dims = 1, name = v.blk.4.attn_out.bias, tensor_size=4096, offset=153651200, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[81]: n_dims = 1, name = v.blk.4.ln1.weight, tensor_size=4096, offset=153655296, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[82]: n_dims = 1, name = v.blk.4.ln1.bias, tensor_size=4096, offset=153659392, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[83]: n_dims = 2, name = v.blk.4.ffn_down.weight, tensor_size=8388608, offset=153663488, shape:[1024, 4096, 1, 1], type = f16
clip_model_loader: tensor[84]: n_dims = 1, name = v.blk.4.ffn_down.bias, tensor_size=16384, offset=162052096, shape:[4096, 1, 1, 1], type = f32
clip_model_loader: tensor[85]: n_dims = 2, name = v.blk.4.ffn_up.weight, tensor_size=8388608, offset=162068480, shape:[4096, 1024, 1, 1], type = f16
clip_model_loader: tensor[86]: n_dims = 1, name = v.blk.4.ffn_up.bias, tensor_size=4096, offset=170457088, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[87]: n_dims = 1, name = v.blk.4.ln2.weight, tensor_size=4096, offset=170461184, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[88]: n_dims = 1, name = v.blk.4.ln2.bias, tensor_size=4096, offset=170465280, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[89]: n_dims = 2, name = v.blk.5.attn_k.weight, tensor_size=2097152, offset=170469376, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[90]: n_dims = 1, name = v.blk.5.attn_k.bias, tensor_size=4096, offset=172566528, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[91]: n_dims = 2, name = v.blk.5.attn_v.weight, tensor_size=2097152, offset=172570624, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[92]: n_dims = 1, name = v.blk.5.attn_v.bias, tensor_size=4096, offset=174667776, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[93]: n_dims = 2, name = v.blk.5.attn_q.weight, tensor_size=2097152, offset=174671872, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[94]: n_dims = 1, name = v.blk.5.attn_q.bias, tensor_size=4096, offset=176769024, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[95]: n_dims = 2, name = v.blk.5.attn_out.weight, tensor_size=2097152, offset=176773120, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[96]: n_dims = 1, name = v.blk.5.attn_out.bias, tensor_size=4096, offset=178870272, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[97]: n_dims = 1, name = v.blk.5.ln1.weight, tensor_size=4096, offset=178874368, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[98]: n_dims = 1, name = v.blk.5.ln1.bias, tensor_size=4096, offset=178878464, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[99]: n_dims = 2, name = v.blk.5.ffn_down.weight, tensor_size=8388608, offset=178882560, shape:[1024, 4096, 1, 1], type = f16
clip_model_loader: tensor[100]: n_dims = 1, name = v.blk.5.ffn_down.bias, tensor_size=16384, offset=187271168, shape:[4096, 1, 1, 1], type = f32
clip_model_loader: tensor[101]: n_dims = 2, name = v.blk.5.ffn_up.weight, tensor_size=8388608, offset=187287552, shape:[4096, 1024, 1, 1], type = f16
clip_model_loader: tensor[102]: n_dims = 1, name = v.blk.5.ffn_up.bias, tensor_size=4096, offset=195676160, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[103]: n_dims = 1, name = v.blk.5.ln2.weight, tensor_size=4096, offset=195680256, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[104]: n_dims = 1, name = v.blk.5.ln2.bias, tensor_size=4096, offset=195684352, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[105]: n_dims = 2, name = v.blk.6.attn_k.weight, tensor_size=2097152, offset=195688448, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[106]: n_dims = 1, name = v.blk.6.attn_k.bias, tensor_size=4096, offset=197785600, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[107]: n_dims = 2, name = v.blk.6.attn_v.weight, tensor_size=2097152, offset=197789696, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[108]: n_dims = 1, name = v.blk.6.attn_v.bias, tensor_size=4096, offset=199886848, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[109]: n_dims = 2, name = v.blk.6.attn_q.weight, tensor_size=2097152, offset=199890944, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[110]: n_dims = 1, name = v.blk.6.attn_q.bias, tensor_size=4096, offset=201988096, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[111]: n_dims = 2, name = v.blk.6.attn_out.weight, tensor_size=2097152, offset=201992192, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[112]: n_dims = 1, name = v.blk.6.attn_out.bias, tensor_size=4096, offset=204089344, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[113]: n_dims = 1, name = v.blk.6.ln1.weight, tensor_size=4096, offset=204093440, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[114]: n_dims = 1, name = v.blk.6.ln1.bias, tensor_size=4096, offset=204097536, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[115]: n_dims = 2, name = v.blk.6.ffn_down.weight, tensor_size=8388608, offset=204101632, shape:[1024, 4096, 1, 1], type = f16
clip_model_loader: tensor[116]: n_dims = 1, name = v.blk.6.ffn_down.bias, tensor_size=16384, offset=212490240, shape:[4096, 1, 1, 1], type = f32
clip_model_loader: tensor[117]: n_dims = 2, name = v.blk.6.ffn_up.weight, tensor_size=8388608, offset=212506624, shape:[4096, 1024, 1, 1], type = f16
clip_model_loader: tensor[118]: n_dims = 1, name = v.blk.6.ffn_up.bias, tensor_size=4096, offset=220895232, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[119]: n_dims = 1, name = v.blk.6.ln2.weight, tensor_size=4096, offset=220899328, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[120]: n_dims = 1, name = v.blk.6.ln2.bias, tensor_size=4096, offset=220903424, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[121]: n_dims = 2, name = v.blk.7.attn_k.weight, tensor_size=2097152, offset=220907520, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[122]: n_dims = 1, name = v.blk.7.attn_k.bias, tensor_size=4096, offset=223004672, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[123]: n_dims = 2, name = v.blk.7.attn_v.weight, tensor_size=2097152, offset=223008768, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[124]: n_dims = 1, name = v.blk.7.attn_v.bias, tensor_size=4096, offset=225105920, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[125]: n_dims = 2, name = v.blk.7.attn_q.weight, tensor_size=2097152, offset=225110016, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[126]: n_dims = 1, name = v.blk.7.attn_q.bias, tensor_size=4096, offset=227207168, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[127]: n_dims = 2, name = v.blk.7.attn_out.weight, tensor_size=2097152, offset=227211264, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[128]: n_dims = 1, name = v.blk.7.attn_out.bias, tensor_size=4096, offset=229308416, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[129]: n_dims = 1, name = v.blk.7.ln1.weight, tensor_size=4096, offset=229312512, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[130]: n_dims = 1, name = v.blk.7.ln1.bias, tensor_size=4096, offset=229316608, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[131]: n_dims = 2, name = v.blk.7.ffn_down.weight, tensor_size=8388608, offset=229320704, shape:[1024, 4096, 1, 1], type = f16
clip_model_loader: tensor[132]: n_dims = 1, name = v.blk.7.ffn_down.bias, tensor_size=16384, offset=237709312, shape:[4096, 1, 1, 1], type = f32
clip_model_loader: tensor[133]: n_dims = 2, name = v.blk.7.ffn_up.weight, tensor_size=8388608, offset=237725696, shape:[4096, 1024, 1, 1], type = f16
clip_model_loader: tensor[134]: n_dims = 1, name = v.blk.7.ffn_up.bias, tensor_size=4096, offset=246114304, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[135]: n_dims = 1, name = v.blk.7.ln2.weight, tensor_size=4096, offset=246118400, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[136]: n_dims = 1, name = v.blk.7.ln2.bias, tensor_size=4096, offset=246122496, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[137]: n_dims = 2, name = v.blk.8.attn_k.weight, tensor_size=2097152, offset=246126592, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[138]: n_dims = 1, name = v.blk.8.attn_k.bias, tensor_size=4096, offset=248223744, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[139]: n_dims = 2, name = v.blk.8.attn_v.weight, tensor_size=2097152, offset=248227840, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[140]: n_dims = 1, name = v.blk.8.attn_v.bias, tensor_size=4096, offset=250324992, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[141]: n_dims = 2, name = v.blk.8.attn_q.weight, tensor_size=2097152, offset=250329088, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[142]: n_dims = 1, name = v.blk.8.attn_q.bias, tensor_size=4096, offset=252426240, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[143]: n_dims = 2, name = v.blk.8.attn_out.weight, tensor_size=2097152, offset=252430336, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[144]: n_dims = 1, name = v.blk.8.attn_out.bias, tensor_size=4096, offset=254527488, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[145]: n_dims = 1, name = v.blk.8.ln1.weight, tensor_size=4096, offset=254531584, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[146]: n_dims = 1, name = v.blk.8.ln1.bias, tensor_size=4096, offset=254535680, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[147]: n_dims = 2, name = v.blk.8.ffn_down.weight, tensor_size=8388608, offset=254539776, shape:[1024, 4096, 1, 1], type = f16
clip_model_loader: tensor[148]: n_dims = 1, name = v.blk.8.ffn_down.bias, tensor_size=16384, offset=262928384, shape:[4096, 1, 1, 1], type = f32
clip_model_loader: tensor[149]: n_dims = 2, name = v.blk.8.ffn_up.weight, tensor_size=8388608, offset=262944768, shape:[4096, 1024, 1, 1], type = f16
clip_model_loader: tensor[150]: n_dims = 1, name = v.blk.8.ffn_up.bias, tensor_size=4096, offset=271333376, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[151]: n_dims = 1, name = v.blk.8.ln2.weight, tensor_size=4096, offset=271337472, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[152]: n_dims = 1, name = v.blk.8.ln2.bias, tensor_size=4096, offset=271341568, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[153]: n_dims = 2, name = v.blk.9.attn_k.weight, tensor_size=2097152, offset=271345664, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[154]: n_dims = 1, name = v.blk.9.attn_k.bias, tensor_size=4096, offset=273442816, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[155]: n_dims = 2, name = v.blk.9.attn_v.weight, tensor_size=2097152, offset=273446912, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[156]: n_dims = 1, name = v.blk.9.attn_v.bias, tensor_size=4096, offset=275544064, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[157]: n_dims = 2, name = v.blk.9.attn_q.weight, tensor_size=2097152, offset=275548160, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[158]: n_dims = 1, name = v.blk.9.attn_q.bias, tensor_size=4096, offset=277645312, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[159]: n_dims = 2, name = v.blk.9.attn_out.weight, tensor_size=2097152, offset=277649408, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[160]: n_dims = 1, name = v.blk.9.attn_out.bias, tensor_size=4096, offset=279746560, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[161]: n_dims = 1, name = v.blk.9.ln1.weight, tensor_size=4096, offset=279750656, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[162]: n_dims = 1, name = v.blk.9.ln1.bias, tensor_size=4096, offset=279754752, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[163]: n_dims = 2, name = v.blk.9.ffn_down.weight, tensor_size=8388608, offset=279758848, shape:[1024, 4096, 1, 1], type = f16
clip_model_loader: tensor[164]: n_dims = 1, name = v.blk.9.ffn_down.bias, tensor_size=16384, offset=288147456, shape:[4096, 1, 1, 1], type = f32
clip_model_loader: tensor[165]: n_dims = 2, name = v.blk.9.ffn_up.weight, tensor_size=8388608, offset=288163840, shape:[4096, 1024, 1, 1], type = f16
clip_model_loader: tensor[166]: n_dims = 1, name = v.blk.9.ffn_up.bias, tensor_size=4096, offset=296552448, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[167]: n_dims = 1, name = v.blk.9.ln2.weight, tensor_size=4096, offset=296556544, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[168]: n_dims = 1, name = v.blk.9.ln2.bias, tensor_size=4096, offset=296560640, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[169]: n_dims = 2, name = v.blk.10.attn_k.weight, tensor_size=2097152, offset=296564736, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[170]: n_dims = 1, name = v.blk.10.attn_k.bias, tensor_size=4096, offset=298661888, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[171]: n_dims = 2, name = v.blk.10.attn_v.weight, tensor_size=2097152, offset=298665984, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[172]: n_dims = 1, name = v.blk.10.attn_v.bias, tensor_size=4096, offset=300763136, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[173]: n_dims = 2, name = v.blk.10.attn_q.weight, tensor_size=2097152, offset=300767232, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[174]: n_dims = 1, name = v.blk.10.attn_q.bias, tensor_size=4096, offset=302864384, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[175]: n_dims = 2, name = v.blk.10.attn_out.weight, tensor_size=2097152, offset=302868480, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[176]: n_dims = 1, name = v.blk.10.attn_out.bias, tensor_size=4096, offset=304965632, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[177]: n_dims = 1, name = v.blk.10.ln1.weight, tensor_size=4096, offset=304969728, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[178]: n_dims = 1, name = v.blk.10.ln1.bias, tensor_size=4096, offset=304973824, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[179]: n_dims = 2, name = v.blk.10.ffn_down.weight, tensor_size=8388608, offset=304977920, shape:[1024, 4096, 1, 1], type = f16
clip_model_loader: tensor[180]: n_dims = 1, name = v.blk.10.ffn_down.bias, tensor_size=16384, offset=313366528, shape:[4096, 1, 1, 1], type = f32
clip_model_loader: tensor[181]: n_dims = 2, name = v.blk.10.ffn_up.weight, tensor_size=8388608, offset=313382912, shape:[4096, 1024, 1, 1], type = f16
clip_model_loader: tensor[182]: n_dims = 1, name = v.blk.10.ffn_up.bias, tensor_size=4096, offset=321771520, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[183]: n_dims = 1, name = v.blk.10.ln2.weight, tensor_size=4096, offset=321775616, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[184]: n_dims = 1, name = v.blk.10.ln2.bias, tensor_size=4096, offset=321779712, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[185]: n_dims = 2, name = v.blk.11.attn_k.weight, tensor_size=2097152, offset=321783808, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[186]: n_dims = 1, name = v.blk.11.attn_k.bias, tensor_size=4096, offset=323880960, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[187]: n_dims = 2, name = v.blk.11.attn_v.weight, tensor_size=2097152, offset=323885056, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[188]: n_dims = 1, name = v.blk.11.attn_v.bias, tensor_size=4096, offset=325982208, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[189]: n_dims = 2, name = v.blk.11.attn_q.weight, tensor_size=2097152, offset=325986304, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[190]: n_dims = 1, name = v.blk.11.attn_q.bias, tensor_size=4096, offset=328083456, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[191]: n_dims = 2, name = v.blk.11.attn_out.weight, tensor_size=2097152, offset=328087552, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[192]: n_dims = 1, name = v.blk.11.attn_out.bias, tensor_size=4096, offset=330184704, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[193]: n_dims = 1, name = v.blk.11.ln1.weight, tensor_size=4096, offset=330188800, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[194]: n_dims = 1, name = v.blk.11.ln1.bias, tensor_size=4096, offset=330192896, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[195]: n_dims = 2, name = v.blk.11.ffn_down.weight, tensor_size=8388608, offset=330196992, shape:[1024, 4096, 1, 1], type = f16
clip_model_loader: tensor[196]: n_dims = 1, name = v.blk.11.ffn_down.bias, tensor_size=16384, offset=338585600, shape:[4096, 1, 1, 1], type = f32
clip_model_loader: tensor[197]: n_dims = 2, name = v.blk.11.ffn_up.weight, tensor_size=8388608, offset=338601984, shape:[4096, 1024, 1, 1], type = f16
clip_model_loader: tensor[198]: n_dims = 1, name = v.blk.11.ffn_up.bias, tensor_size=4096, offset=346990592, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[199]: n_dims = 1, name = v.blk.11.ln2.weight, tensor_size=4096, offset=346994688, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[200]: n_dims = 1, name = v.blk.11.ln2.bias, tensor_size=4096, offset=346998784, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[201]: n_dims = 2, name = v.blk.12.attn_k.weight, tensor_size=2097152, offset=347002880, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[202]: n_dims = 1, name = v.blk.12.attn_k.bias, tensor_size=4096, offset=349100032, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[203]: n_dims = 2, name = v.blk.12.attn_v.weight, tensor_size=2097152, offset=349104128, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[204]: n_dims = 1, name = v.blk.12.attn_v.bias, tensor_size=4096, offset=351201280, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[205]: n_dims = 2, name = v.blk.12.attn_q.weight, tensor_size=2097152, offset=351205376, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[206]: n_dims = 1, name = v.blk.12.attn_q.bias, tensor_size=4096, offset=353302528, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[207]: n_dims = 2, name = v.blk.12.attn_out.weight, tensor_size=2097152, offset=353306624, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[208]: n_dims = 1, name = v.blk.12.attn_out.bias, tensor_size=4096, offset=355403776, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[209]: n_dims = 1, name = v.blk.12.ln1.weight, tensor_size=4096, offset=355407872, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[210]: n_dims = 1, name = v.blk.12.ln1.bias, tensor_size=4096, offset=355411968, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[211]: n_dims = 2, name = v.blk.12.ffn_down.weight, tensor_size=8388608, offset=355416064, shape:[1024, 4096, 1, 1], type = f16
clip_model_loader: tensor[212]: n_dims = 1, name = v.blk.12.ffn_down.bias, tensor_size=16384, offset=363804672, shape:[4096, 1, 1, 1], type = f32
clip_model_loader: tensor[213]: n_dims = 2, name = v.blk.12.ffn_up.weight, tensor_size=8388608, offset=363821056, shape:[4096, 1024, 1, 1], type = f16
clip_model_loader: tensor[214]: n_dims = 1, name = v.blk.12.ffn_up.bias, tensor_size=4096, offset=372209664, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[215]: n_dims = 1, name = v.blk.12.ln2.weight, tensor_size=4096, offset=372213760, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[216]: n_dims = 1, name = v.blk.12.ln2.bias, tensor_size=4096, offset=372217856, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[217]: n_dims = 2, name = v.blk.13.attn_k.weight, tensor_size=2097152, offset=372221952, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[218]: n_dims = 1, name = v.blk.13.attn_k.bias, tensor_size=4096, offset=374319104, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[219]: n_dims = 2, name = v.blk.13.attn_v.weight, tensor_size=2097152, offset=374323200, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[220]: n_dims = 1, name = v.blk.13.attn_v.bias, tensor_size=4096, offset=376420352, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[221]: n_dims = 2, name = v.blk.13.attn_q.weight, tensor_size=2097152, offset=376424448, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[222]: n_dims = 1, name = v.blk.13.attn_q.bias, tensor_size=4096, offset=378521600, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[223]: n_dims = 2, name = v.blk.13.attn_out.weight, tensor_size=2097152, offset=378525696, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[224]: n_dims = 1, name = v.blk.13.attn_out.bias, tensor_size=4096, offset=380622848, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[225]: n_dims = 1, name = v.blk.13.ln1.weight, tensor_size=4096, offset=380626944, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[226]: n_dims = 1, name = v.blk.13.ln1.bias, tensor_size=4096, offset=380631040, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[227]: n_dims = 2, name = v.blk.13.ffn_down.weight, tensor_size=8388608, offset=380635136, shape:[1024, 4096, 1, 1], type = f16
clip_model_loader: tensor[228]: n_dims = 1, name = v.blk.13.ffn_down.bias, tensor_size=16384, offset=389023744, shape:[4096, 1, 1, 1], type = f32
clip_model_loader: tensor[229]: n_dims = 2, name = v.blk.13.ffn_up.weight, tensor_size=8388608, offset=389040128, shape:[4096, 1024, 1, 1], type = f16
clip_model_loader: tensor[230]: n_dims = 1, name = v.blk.13.ffn_up.bias, tensor_size=4096, offset=397428736, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[231]: n_dims = 1, name = v.blk.13.ln2.weight, tensor_size=4096, offset=397432832, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[232]: n_dims = 1, name = v.blk.13.ln2.bias, tensor_size=4096, offset=397436928, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[233]: n_dims = 2, name = v.blk.14.attn_k.weight, tensor_size=2097152, offset=397441024, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[234]: n_dims = 1, name = v.blk.14.attn_k.bias, tensor_size=4096, offset=399538176, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[235]: n_dims = 2, name = v.blk.14.attn_v.weight, tensor_size=2097152, offset=399542272, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[236]: n_dims = 1, name = v.blk.14.attn_v.bias, tensor_size=4096, offset=401639424, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[237]: n_dims = 2, name = v.blk.14.attn_q.weight, tensor_size=2097152, offset=401643520, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[238]: n_dims = 1, name = v.blk.14.attn_q.bias, tensor_size=4096, offset=403740672, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[239]: n_dims = 2, name = v.blk.14.attn_out.weight, tensor_size=2097152, offset=403744768, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[240]: n_dims = 1, name = v.blk.14.attn_out.bias, tensor_size=4096, offset=405841920, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[241]: n_dims = 1, name = v.blk.14.ln1.weight, tensor_size=4096, offset=405846016, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[242]: n_dims = 1, name = v.blk.14.ln1.bias, tensor_size=4096, offset=405850112, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[243]: n_dims = 2, name = v.blk.14.ffn_down.weight, tensor_size=8388608, offset=405854208, shape:[1024, 4096, 1, 1], type = f16
clip_model_loader: tensor[244]: n_dims = 1, name = v.blk.14.ffn_down.bias, tensor_size=16384, offset=414242816, shape:[4096, 1, 1, 1], type = f32
clip_model_loader: tensor[245]: n_dims = 2, name = v.blk.14.ffn_up.weight, tensor_size=8388608, offset=414259200, shape:[4096, 1024, 1, 1], type = f16
clip_model_loader: tensor[246]: n_dims = 1, name = v.blk.14.ffn_up.bias, tensor_size=4096, offset=422647808, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[247]: n_dims = 1, name = v.blk.14.ln2.weight, tensor_size=4096, offset=422651904, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[248]: n_dims = 1, name = v.blk.14.ln2.bias, tensor_size=4096, offset=422656000, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[249]: n_dims = 2, name = v.blk.15.attn_k.weight, tensor_size=2097152, offset=422660096, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[250]: n_dims = 1, name = v.blk.15.attn_k.bias, tensor_size=4096, offset=424757248, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[251]: n_dims = 2, name = v.blk.15.attn_v.weight, tensor_size=2097152, offset=424761344, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[252]: n_dims = 1, name = v.blk.15.attn_v.bias, tensor_size=4096, offset=426858496, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[253]: n_dims = 2, name = v.blk.15.attn_q.weight, tensor_size=2097152, offset=426862592, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[254]: n_dims = 1, name = v.blk.15.attn_q.bias, tensor_size=4096, offset=428959744, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[255]: n_dims = 2, name = v.blk.15.attn_out.weight, tensor_size=2097152, offset=428963840, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[256]: n_dims = 1, name = v.blk.15.attn_out.bias, tensor_size=4096, offset=431060992, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[257]: n_dims = 1, name = v.blk.15.ln1.weight, tensor_size=4096, offset=431065088, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[258]: n_dims = 1, name = v.blk.15.ln1.bias, tensor_size=4096, offset=431069184, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[259]: n_dims = 2, name = v.blk.15.ffn_down.weight, tensor_size=8388608, offset=431073280, shape:[1024, 4096, 1, 1], type = f16
clip_model_loader: tensor[260]: n_dims = 1, name = v.blk.15.ffn_down.bias, tensor_size=16384, offset=439461888, shape:[4096, 1, 1, 1], type = f32
clip_model_loader: tensor[261]: n_dims = 2, name = v.blk.15.ffn_up.weight, tensor_size=8388608, offset=439478272, shape:[4096, 1024, 1, 1], type = f16
clip_model_loader: tensor[262]: n_dims = 1, name = v.blk.15.ffn_up.bias, tensor_size=4096, offset=447866880, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[263]: n_dims = 1, name = v.blk.15.ln2.weight, tensor_size=4096, offset=447870976, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[264]: n_dims = 1, name = v.blk.15.ln2.bias, tensor_size=4096, offset=447875072, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[265]: n_dims = 2, name = v.blk.16.attn_k.weight, tensor_size=2097152, offset=447879168, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[266]: n_dims = 1, name = v.blk.16.attn_k.bias, tensor_size=4096, offset=449976320, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[267]: n_dims = 2, name = v.blk.16.attn_v.weight, tensor_size=2097152, offset=449980416, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[268]: n_dims = 1, name = v.blk.16.attn_v.bias, tensor_size=4096, offset=452077568, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[269]: n_dims = 2, name = v.blk.16.attn_q.weight, tensor_size=2097152, offset=452081664, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[270]: n_dims = 1, name = v.blk.16.attn_q.bias, tensor_size=4096, offset=454178816, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[271]: n_dims = 2, name = v.blk.16.attn_out.weight, tensor_size=2097152, offset=454182912, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[272]: n_dims = 1, name = v.blk.16.attn_out.bias, tensor_size=4096, offset=456280064, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[273]: n_dims = 1, name = v.blk.16.ln1.weight, tensor_size=4096, offset=456284160, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[274]: n_dims = 1, name = v.blk.16.ln1.bias, tensor_size=4096, offset=456288256, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[275]: n_dims = 2, name = v.blk.16.ffn_down.weight, tensor_size=8388608, offset=456292352, shape:[1024, 4096, 1, 1], type = f16
clip_model_loader: tensor[276]: n_dims = 1, name = v.blk.16.ffn_down.bias, tensor_size=16384, offset=464680960, shape:[4096, 1, 1, 1], type = f32
clip_model_loader: tensor[277]: n_dims = 2, name = v.blk.16.ffn_up.weight, tensor_size=8388608, offset=464697344, shape:[4096, 1024, 1, 1], type = f16
clip_model_loader: tensor[278]: n_dims = 1, name = v.blk.16.ffn_up.bias, tensor_size=4096, offset=473085952, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[279]: n_dims = 1, name = v.blk.16.ln2.weight, tensor_size=4096, offset=473090048, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[280]: n_dims = 1, name = v.blk.16.ln2.bias, tensor_size=4096, offset=473094144, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[281]: n_dims = 2, name = v.blk.17.attn_k.weight, tensor_size=2097152, offset=473098240, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[282]: n_dims = 1, name = v.blk.17.attn_k.bias, tensor_size=4096, offset=475195392, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[283]: n_dims = 2, name = v.blk.17.attn_v.weight, tensor_size=2097152, offset=475199488, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[284]: n_dims = 1, name = v.blk.17.attn_v.bias, tensor_size=4096, offset=477296640, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[285]: n_dims = 2, name = v.blk.17.attn_q.weight, tensor_size=2097152, offset=477300736, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[286]: n_dims = 1, name = v.blk.17.attn_q.bias, tensor_size=4096, offset=479397888, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[287]: n_dims = 2, name = v.blk.17.attn_out.weight, tensor_size=2097152, offset=479401984, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[288]: n_dims = 1, name = v.blk.17.attn_out.bias, tensor_size=4096, offset=481499136, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[289]: n_dims = 1, name = v.blk.17.ln1.weight, tensor_size=4096, offset=481503232, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[290]: n_dims = 1, name = v.blk.17.ln1.bias, tensor_size=4096, offset=481507328, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[291]: n_dims = 2, name = v.blk.17.ffn_down.weight, tensor_size=8388608, offset=481511424, shape:[1024, 4096, 1, 1], type = f16
clip_model_loader: tensor[292]: n_dims = 1, name = v.blk.17.ffn_down.bias, tensor_size=16384, offset=489900032, shape:[4096, 1, 1, 1], type = f32
clip_model_loader: tensor[293]: n_dims = 2, name = v.blk.17.ffn_up.weight, tensor_size=8388608, offset=489916416, shape:[4096, 1024, 1, 1], type = f16
clip_model_loader: tensor[294]: n_dims = 1, name = v.blk.17.ffn_up.bias, tensor_size=4096, offset=498305024, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[295]: n_dims = 1, name = v.blk.17.ln2.weight, tensor_size=4096, offset=498309120, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[296]: n_dims = 1, name = v.blk.17.ln2.bias, tensor_size=4096, offset=498313216, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[297]: n_dims = 2, name = v.blk.18.attn_k.weight, tensor_size=2097152, offset=498317312, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[298]: n_dims = 1, name = v.blk.18.attn_k.bias, tensor_size=4096, offset=500414464, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[299]: n_dims = 2, name = v.blk.18.attn_v.weight, tensor_size=2097152, offset=500418560, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[300]: n_dims = 1, name = v.blk.18.attn_v.bias, tensor_size=4096, offset=502515712, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[301]: n_dims = 2, name = v.blk.18.attn_q.weight, tensor_size=2097152, offset=502519808, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[302]: n_dims = 1, name = v.blk.18.attn_q.bias, tensor_size=4096, offset=504616960, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[303]: n_dims = 2, name = v.blk.18.attn_out.weight, tensor_size=2097152, offset=504621056, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[304]: n_dims = 1, name = v.blk.18.attn_out.bias, tensor_size=4096, offset=506718208, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[305]: n_dims = 1, name = v.blk.18.ln1.weight, tensor_size=4096, offset=506722304, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[306]: n_dims = 1, name = v.blk.18.ln1.bias, tensor_size=4096, offset=506726400, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[307]: n_dims = 2, name = v.blk.18.ffn_down.weight, tensor_size=8388608, offset=506730496, shape:[1024, 4096, 1, 1], type = f16
clip_model_loader: tensor[308]: n_dims = 1, name = v.blk.18.ffn_down.bias, tensor_size=16384, offset=515119104, shape:[4096, 1, 1, 1], type = f32
clip_model_loader: tensor[309]: n_dims = 2, name = v.blk.18.ffn_up.weight, tensor_size=8388608, offset=515135488, shape:[4096, 1024, 1, 1], type = f16
clip_model_loader: tensor[310]: n_dims = 1, name = v.blk.18.ffn_up.bias, tensor_size=4096, offset=523524096, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[311]: n_dims = 1, name = v.blk.18.ln2.weight, tensor_size=4096, offset=523528192, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[312]: n_dims = 1, name = v.blk.18.ln2.bias, tensor_size=4096, offset=523532288, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[313]: n_dims = 2, name = v.blk.19.attn_k.weight, tensor_size=2097152, offset=523536384, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[314]: n_dims = 1, name = v.blk.19.attn_k.bias, tensor_size=4096, offset=525633536, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[315]: n_dims = 2, name = v.blk.19.attn_v.weight, tensor_size=2097152, offset=525637632, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[316]: n_dims = 1, name = v.blk.19.attn_v.bias, tensor_size=4096, offset=527734784, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[317]: n_dims = 2, name = v.blk.19.attn_q.weight, tensor_size=2097152, offset=527738880, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[318]: n_dims = 1, name = v.blk.19.attn_q.bias, tensor_size=4096, offset=529836032, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[319]: n_dims = 2, name = v.blk.19.attn_out.weight, tensor_size=2097152, offset=529840128, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[320]: n_dims = 1, name = v.blk.19.attn_out.bias, tensor_size=4096, offset=531937280, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[321]: n_dims = 1, name = v.blk.19.ln1.weight, tensor_size=4096, offset=531941376, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[322]: n_dims = 1, name = v.blk.19.ln1.bias, tensor_size=4096, offset=531945472, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[323]: n_dims = 2, name = v.blk.19.ffn_down.weight, tensor_size=8388608, offset=531949568, shape:[1024, 4096, 1, 1], type = f16
clip_model_loader: tensor[324]: n_dims = 1, name = v.blk.19.ffn_down.bias, tensor_size=16384, offset=540338176, shape:[4096, 1, 1, 1], type = f32
clip_model_loader: tensor[325]: n_dims = 2, name = v.blk.19.ffn_up.weight, tensor_size=8388608, offset=540354560, shape:[4096, 1024, 1, 1], type = f16
clip_model_loader: tensor[326]: n_dims = 1, name = v.blk.19.ffn_up.bias, tensor_size=4096, offset=548743168, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[327]: n_dims = 1, name = v.blk.19.ln2.weight, tensor_size=4096, offset=548747264, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[328]: n_dims = 1, name = v.blk.19.ln2.bias, tensor_size=4096, offset=548751360, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[329]: n_dims = 2, name = v.blk.20.attn_k.weight, tensor_size=2097152, offset=548755456, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[330]: n_dims = 1, name = v.blk.20.attn_k.bias, tensor_size=4096, offset=550852608, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[331]: n_dims = 2, name = v.blk.20.attn_v.weight, tensor_size=2097152, offset=550856704, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[332]: n_dims = 1, name = v.blk.20.attn_v.bias, tensor_size=4096, offset=552953856, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[333]: n_dims = 2, name = v.blk.20.attn_q.weight, tensor_size=2097152, offset=552957952, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[334]: n_dims = 1, name = v.blk.20.attn_q.bias, tensor_size=4096, offset=555055104, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[335]: n_dims = 2, name = v.blk.20.attn_out.weight, tensor_size=2097152, offset=555059200, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[336]: n_dims = 1, name = v.blk.20.attn_out.bias, tensor_size=4096, offset=557156352, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[337]: n_dims = 1, name = v.blk.20.ln1.weight, tensor_size=4096, offset=557160448, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[338]: n_dims = 1, name = v.blk.20.ln1.bias, tensor_size=4096, offset=557164544, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[339]: n_dims = 2, name = v.blk.20.ffn_down.weight, tensor_size=8388608, offset=557168640, shape:[1024, 4096, 1, 1], type = f16
clip_model_loader: tensor[340]: n_dims = 1, name = v.blk.20.ffn_down.bias, tensor_size=16384, offset=565557248, shape:[4096, 1, 1, 1], type = f32
clip_model_loader: tensor[341]: n_dims = 2, name = v.blk.20.ffn_up.weight, tensor_size=8388608, offset=565573632, shape:[4096, 1024, 1, 1], type = f16
clip_model_loader: tensor[342]: n_dims = 1, name = v.blk.20.ffn_up.bias, tensor_size=4096, offset=573962240, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[343]: n_dims = 1, name = v.blk.20.ln2.weight, tensor_size=4096, offset=573966336, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[344]: n_dims = 1, name = v.blk.20.ln2.bias, tensor_size=4096, offset=573970432, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[345]: n_dims = 2, name = v.blk.21.attn_k.weight, tensor_size=2097152, offset=573974528, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[346]: n_dims = 1, name = v.blk.21.attn_k.bias, tensor_size=4096, offset=576071680, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[347]: n_dims = 2, name = v.blk.21.attn_v.weight, tensor_size=2097152, offset=576075776, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[348]: n_dims = 1, name = v.blk.21.attn_v.bias, tensor_size=4096, offset=578172928, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[349]: n_dims = 2, name = v.blk.21.attn_q.weight, tensor_size=2097152, offset=578177024, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[350]: n_dims = 1, name = v.blk.21.attn_q.bias, tensor_size=4096, offset=580274176, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[351]: n_dims = 2, name = v.blk.21.attn_out.weight, tensor_size=2097152, offset=580278272, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[352]: n_dims = 1, name = v.blk.21.attn_out.bias, tensor_size=4096, offset=582375424, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[353]: n_dims = 1, name = v.blk.21.ln1.weight, tensor_size=4096, offset=582379520, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[354]: n_dims = 1, name = v.blk.21.ln1.bias, tensor_size=4096, offset=582383616, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[355]: n_dims = 2, name = v.blk.21.ffn_down.weight, tensor_size=8388608, offset=582387712, shape:[1024, 4096, 1, 1], type = f16
clip_model_loader: tensor[356]: n_dims = 1, name = v.blk.21.ffn_down.bias, tensor_size=16384, offset=590776320, shape:[4096, 1, 1, 1], type = f32
clip_model_loader: tensor[357]: n_dims = 2, name = v.blk.21.ffn_up.weight, tensor_size=8388608, offset=590792704, shape:[4096, 1024, 1, 1], type = f16
clip_model_loader: tensor[358]: n_dims = 1, name = v.blk.21.ffn_up.bias, tensor_size=4096, offset=599181312, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[359]: n_dims = 1, name = v.blk.21.ln2.weight, tensor_size=4096, offset=599185408, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[360]: n_dims = 1, name = v.blk.21.ln2.bias, tensor_size=4096, offset=599189504, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[361]: n_dims = 2, name = v.blk.22.attn_k.weight, tensor_size=2097152, offset=599193600, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[362]: n_dims = 1, name = v.blk.22.attn_k.bias, tensor_size=4096, offset=601290752, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[363]: n_dims = 2, name = v.blk.22.attn_v.weight, tensor_size=2097152, offset=601294848, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[364]: n_dims = 1, name = v.blk.22.attn_v.bias, tensor_size=4096, offset=603392000, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[365]: n_dims = 2, name = v.blk.22.attn_q.weight, tensor_size=2097152, offset=603396096, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[366]: n_dims = 1, name = v.blk.22.attn_q.bias, tensor_size=4096, offset=605493248, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[367]: n_dims = 2, name = v.blk.22.attn_out.weight, tensor_size=2097152, offset=605497344, shape:[1024, 1024, 1, 1], type = f16
clip_model_loader: tensor[368]: n_dims = 1, name = v.blk.22.attn_out.bias, tensor_size=4096, offset=607594496, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[369]: n_dims = 1, name = v.blk.22.ln1.weight, tensor_size=4096, offset=607598592, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[370]: n_dims = 1, name = v.blk.22.ln1.bias, tensor_size=4096, offset=607602688, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[371]: n_dims = 2, name = v.blk.22.ffn_down.weight, tensor_size=8388608, offset=607606784, shape:[1024, 4096, 1, 1], type = f16
clip_model_loader: tensor[372]: n_dims = 1, name = v.blk.22.ffn_down.bias, tensor_size=16384, offset=615995392, shape:[4096, 1, 1, 1], type = f32
clip_model_loader: tensor[373]: n_dims = 2, name = v.blk.22.ffn_up.weight, tensor_size=8388608, offset=616011776, shape:[4096, 1024, 1, 1], type = f16
clip_model_loader: tensor[374]: n_dims = 1, name = v.blk.22.ffn_up.bias, tensor_size=4096, offset=624400384, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[375]: n_dims = 1, name = v.blk.22.ln2.weight, tensor_size=4096, offset=624404480, shape:[1024, 1, 1, 1], type = f32
clip_model_loader: tensor[376]: n_dims = 1, name = v.blk.22.ln2.bias, tensor_size=4096, offset=624408576, shape:[1024, 1, 1, 1], type = f32
clip_ctx: CLIP using CPU backend
load_hparams: projector:          mlp
load_hparams: n_embd:             1024
load_hparams: n_head:             16
load_hparams: n_ff:               4096
load_hparams: n_layer:            23
load_hparams: ffn_op:             gelu_quick
load_hparams: projection_dim:     768

--- vision hparams ---
load_hparams: image_size:         336
load_hparams: patch_size:         14
load_hparams: has_llava_proj:     1
load_hparams: minicpmv_version:   0
load_hparams: n_merge:            0
load_hparams: n_wa_pattern:       0

load_hparams: model size:         595.49 MiB
load_hparams: metadata size:      0.13 MiB
load_tensors: ffn up/down are swapped
load_tensors: loaded 377 tensors from /root/.ollama/models/blobs/sha256-72d6f08a42f656d36b356dbe0920675899a99ce21192fd66266fb7d82ed07539
warmup: warmup with image size = 336 x 336
alloc_compute_meta:        CPU compute buffer size =    21.55 MiB
alloc_compute_meta: graph splits = 1, nodes = 705
warmup: flash attention is enabled
time=2026-03-27T00:48:06.563Z level=INFO source=server.go:1388 msg="llama runner started in 6.33 seconds"
time=2026-03-27T00:48:06.563Z level=INFO source=sched.go:566 msg="loaded runners" count=3
time=2026-03-27T00:48:06.563Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:48:06.564Z level=INFO source=server.go:1388 msg="llama runner started in 6.33 seconds"
llama_model_loader: loaded meta data with 22 key-value pairs and 339 tensors from /root/.ollama/models/blobs/sha256-262843d4806aeb402336980badd414a72576b20b1e5d537647da15f16c4a4df0 (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = qwen2
llama_model_loader: - kv   1:                               general.name str              = model
llama_model_loader: - kv   2:                          qwen2.block_count u32              = 28
llama_model_loader: - kv   3:                       qwen2.context_length u32              = 32768
llama_model_loader: - kv   4:                     qwen2.embedding_length u32              = 3584
llama_model_loader: - kv   5:                  qwen2.feed_forward_length u32              = 18944
llama_model_loader: - kv   6:                 qwen2.attention.head_count u32              = 28
llama_model_loader: - kv   7:              qwen2.attention.head_count_kv u32              = 4
llama_model_loader: - kv   8:                       qwen2.rope.freq_base f32              = 1000000.000000
llama_model_loader: - kv   9:     qwen2.attention.layer_norm_rms_epsilon f32              = 0.000001
llama_model_loader: - kv  10:                          general.file_type u32              = 2
llama_model_loader: - kv  11:                       tokenizer.ggml.model str              = gpt2
llama_model_loader: - kv  12:                         tokenizer.ggml.pre str              = qwen2
llama_model_loader: - kv  13:                      tokenizer.ggml.tokens arr[str,151666]  = ["!", "\"", "#", "$", "%", "&", "'", ...
llama_model_loader: - kv  14:                  tokenizer.ggml.token_type arr[i32,151666]  = [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...
llama_model_loader: - kv  15:                      tokenizer.ggml.merges arr[str,151387]  = ["Ġ Ġ", "ĠĠ ĠĠ", "i n", "Ġ t",...
llama_model_loader: - kv  16:                tokenizer.ggml.bos_token_id u32              = 151644
llama_model_loader: - kv  17:                tokenizer.ggml.eos_token_id u32              = 151645
llama_model_loader: - kv  18:            tokenizer.ggml.unknown_token_id u32              = 128244
llama_model_loader: - kv  19:            tokenizer.ggml.padding_token_id u32              = 0
llama_model_loader: - kv  20:                    tokenizer.chat_template str              = {% for message in messages %}{% if lo...
llama_model_loader: - kv  21:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:  141 tensors
llama_model_loader: - type q4_0:  197 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 4.12 GiB (4.65 BPW) 
load: printing all EOG tokens:
load:   - 151643 ('<|endoftext|>')
load:   - 151645 ('<|im_end|>')
load: special tokens cache size = 25
load: token to piece cache size = 0.9309 MB
print_info: arch             = qwen2
print_info: vocab_only       = 1
print_info: no_alloc         = 0
print_info: model type       = ?B
print_info: model params     = 7.61 B
print_info: general.name     = model
print_info: vocab type       = BPE
print_info: n_vocab          = 151666
print_info: n_merges         = 151387
print_info: BOS token        = 151644 '<|im_start|>'
print_info: EOS token        = 151645 '<|im_end|>'
print_info: EOT token        = 151645 '<|im_end|>'
print_info: UNK token        = 128244 '<unk>'
print_info: PAD token        = 0 '!'
print_info: LF token         = 198 'Ċ'
print_info: EOG token        = 151643 '<|endoftext|>'
print_info: EOG token        = 151645 '<|im_end|>'
print_info: max token length = 256
llama_model_load: vocab only - skipping tensors
time=2026-03-27T00:48:51.648Z level=INFO source=server.go:431 msg="starting runner" cmd="/usr/bin/ollama runner --model /root/.ollama/models/blobs/sha256-262843d4806aeb402336980badd414a72576b20b1e5d537647da15f16c4a4df0 --port 32783"
time=2026-03-27T00:48:51.649Z level=INFO source=sched.go:491 msg="system memory" total="24.0 GiB" free="16.8 GiB" free_swap="8.0 GiB"
time=2026-03-27T00:48:51.649Z level=INFO source=server.go:498 msg="loading model" "model layers"=29 requested=-1
time=2026-03-27T00:48:51.651Z level=INFO source=device.go:245 msg="model weights" device=CPU size="3.8 GiB"
time=2026-03-27T00:48:51.651Z level=INFO source=device.go:256 msg="kv cache" device=CPU size="224.0 MiB"
time=2026-03-27T00:48:51.651Z level=INFO source=device.go:272 msg="total memory" size="4.1 GiB"
time=2026-03-27T00:48:51.676Z level=INFO source=runner.go:965 msg="starting go runner"
load_backend: loaded CPU backend from /usr/lib/ollama/libggml-cpu-alderlake.so
time=2026-03-27T00:48:51.691Z level=INFO source=ggml.go:104 msg=system CPU.0.SSE3=1 CPU.0.SSSE3=1 CPU.0.AVX=1 CPU.0.AVX_VNNI=1 CPU.0.AVX2=1 CPU.0.F16C=1 CPU.0.FMA=1 CPU.0.BMI2=1 CPU.0.LLAMAFILE=1 CPU.1.LLAMAFILE=1 compiler=cgo(gcc)
time=2026-03-27T00:48:51.692Z level=INFO source=runner.go:1001 msg="Server listening on 127.0.0.1:32783"
time=2026-03-27T00:48:51.697Z level=INFO source=runner.go:895 msg=load request="{Operation:commit LoraPath:[] Parallel:1 BatchSize:512 FlashAttention:Auto KvSize:4096 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath:/root/.ollama/models/blobs/sha256-f8a805e9e62085805c69c427287acefc284932eb4abfe6e1b1ce431d27e2f4e0 MainGPU:0 UseMmap:false}"
time=2026-03-27T00:48:51.697Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:48:51.698Z level=INFO source=server.go:1384 msg="waiting for server to become available" status="llm server loading model"
llama_model_loader: loaded meta data with 22 key-value pairs and 339 tensors from /root/.ollama/models/blobs/sha256-262843d4806aeb402336980badd414a72576b20b1e5d537647da15f16c4a4df0 (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = qwen2
llama_model_loader: - kv   1:                               general.name str              = model
llama_model_loader: - kv   2:                          qwen2.block_count u32              = 28
llama_model_loader: - kv   3:                       qwen2.context_length u32              = 32768
llama_model_loader: - kv   4:                     qwen2.embedding_length u32              = 3584
llama_model_loader: - kv   5:                  qwen2.feed_forward_length u32              = 18944
llama_model_loader: - kv   6:                 qwen2.attention.head_count u32              = 28
llama_model_loader: - kv   7:              qwen2.attention.head_count_kv u32              = 4
llama_model_loader: - kv   8:                       qwen2.rope.freq_base f32              = 1000000.000000
llama_model_loader: - kv   9:     qwen2.attention.layer_norm_rms_epsilon f32              = 0.000001
llama_model_loader: - kv  10:                          general.file_type u32              = 2
llama_model_loader: - kv  11:                       tokenizer.ggml.model str              = gpt2
llama_model_loader: - kv  12:                         tokenizer.ggml.pre str              = qwen2
llama_model_loader: - kv  13:                      tokenizer.ggml.tokens arr[str,151666]  = ["!", "\"", "#", "$", "%", "&", "'", ...
llama_model_loader: - kv  14:                  tokenizer.ggml.token_type arr[i32,151666]  = [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...
llama_model_loader: - kv  15:                      tokenizer.ggml.merges arr[str,151387]  = ["Ġ Ġ", "ĠĠ ĠĠ", "i n", "Ġ t",...
llama_model_loader: - kv  16:                tokenizer.ggml.bos_token_id u32              = 151644
llama_model_loader: - kv  17:                tokenizer.ggml.eos_token_id u32              = 151645
llama_model_loader: - kv  18:            tokenizer.ggml.unknown_token_id u32              = 128244
llama_model_loader: - kv  19:            tokenizer.ggml.padding_token_id u32              = 0
llama_model_loader: - kv  20:                    tokenizer.chat_template str              = {% for message in messages %}{% if lo...
llama_model_loader: - kv  21:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:  141 tensors
llama_model_loader: - type q4_0:  197 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 4.12 GiB (4.65 BPW) 
load: printing all EOG tokens:
load:   - 151643 ('<|endoftext|>')
load:   - 151645 ('<|im_end|>')
load: special tokens cache size = 25
load: token to piece cache size = 0.9309 MB
print_info: arch             = qwen2
print_info: vocab_only       = 0
print_info: no_alloc         = 0
print_info: n_ctx_train      = 32768
print_info: n_embd           = 3584
print_info: n_embd_inp       = 3584
print_info: n_layer          = 28
print_info: n_head           = 28
print_info: n_head_kv        = 4
print_info: n_rot            = 128
print_info: n_swa            = 0
print_info: is_swa_any       = 0
print_info: n_embd_head_k    = 128
print_info: n_embd_head_v    = 128
print_info: n_gqa            = 7
print_info: n_embd_k_gqa     = 512
print_info: n_embd_v_gqa     = 512
print_info: f_norm_eps       = 0.0e+00
print_info: f_norm_rms_eps   = 1.0e-06
print_info: f_clamp_kqv      = 0.0e+00
print_info: f_max_alibi_bias = 0.0e+00
print_info: f_logit_scale    = 0.0e+00
print_info: f_attn_scale     = 0.0e+00
print_info: n_ff             = 18944
print_info: n_expert         = 0
print_info: n_expert_used    = 0
print_info: n_expert_groups  = 0
print_info: n_group_used     = 0
print_info: causal attn      = 1
print_info: pooling type     = -1
print_info: rope type        = 2
print_info: rope scaling     = linear
print_info: freq_base_train  = 1000000.0
print_info: freq_scale_train = 1
print_info: n_ctx_orig_yarn  = 32768
print_info: rope_yarn_log_mul= 0.0000
print_info: rope_finetuned   = unknown
print_info: model type       = 7B
print_info: model params     = 7.61 B
print_info: general.name     = model
print_info: vocab type       = BPE
print_info: n_vocab          = 151666
print_info: n_merges         = 151387
print_info: BOS token        = 151644 '<|im_start|>'
print_info: EOS token        = 151645 '<|im_end|>'
print_info: EOT token        = 151645 '<|im_end|>'
print_info: UNK token        = 128244 '<unk>'
print_info: PAD token        = 0 '!'
print_info: LF token         = 198 'Ċ'
print_info: EOG token        = 151643 '<|endoftext|>'
print_info: EOG token        = 151645 '<|im_end|>'
print_info: max token length = 256
load_tensors: loading model tensors, this can take a while... (mmap = false)
load_tensors:          CPU model buffer size =  4218.54 MiB
llama_context: constructing llama_context
llama_context: n_seq_max     = 1
llama_context: n_ctx         = 4096
llama_context: n_ctx_seq     = 4096
llama_context: n_batch       = 512
llama_context: n_ubatch      = 512
llama_context: causal_attn   = 1
llama_context: flash_attn    = auto
llama_context: kv_unified    = false
llama_context: freq_base     = 1000000.0
llama_context: freq_scale    = 1
llama_context: n_ctx_seq (4096) < n_ctx_train (32768) -- the full capacity of the model will not be utilized
llama_context:        CPU  output buffer size =     0.59 MiB
llama_kv_cache:        CPU KV buffer size =   224.00 MiB
llama_kv_cache: size =  224.00 MiB (  4096 cells,  28 layers,  1/1 seqs), K (f16):  112.00 MiB, V (f16):  112.00 MiB
llama_context: Flash Attention was auto, set to enabled
llama_context:        CPU compute buffer size =   303.22 MiB
llama_context: graph nodes  = 959
llama_context: graph splits = 1
clip_model_loader: model name:   
clip_model_loader: description:  image encoder for MiniCPM-V
clip_model_loader: GGUF version: 3
clip_model_loader: alignment:    32
clip_model_loader: n_tensors:    455
clip_model_loader: n_kv:         19

clip_model_loader: has vision encoder
clip_model_loader: tensor[0]: n_dims = 2, name = resampler.query, tensor_size=917504, offset=0, shape:[3584, 64, 1, 1], type = f32
clip_model_loader: tensor[1]: n_dims = 2, name = resampler.pos_embed_k, tensor_size=70246400, offset=917504, shape:[3584, 4900, 1, 1], type = f32
clip_model_loader: tensor[2]: n_dims = 2, name = resampler.proj.weight, tensor_size=25690112, offset=71163904, shape:[3584, 3584, 1, 1], type = f16
clip_model_loader: tensor[3]: n_dims = 2, name = resampler.kv.weight, tensor_size=8257536, offset=96854016, shape:[1152, 3584, 1, 1], type = f16
clip_model_loader: tensor[4]: n_dims = 2, name = resampler.attn.q.weight, tensor_size=25690112, offset=105111552, shape:[3584, 3584, 1, 1], type = f16
clip_model_loader: tensor[5]: n_dims = 2, name = resampler.attn.k.weight, tensor_size=25690112, offset=130801664, shape:[3584, 3584, 1, 1], type = f16
clip_model_loader: tensor[6]: n_dims = 2, name = resampler.attn.v.weight, tensor_size=25690112, offset=156491776, shape:[3584, 3584, 1, 1], type = f16
clip_model_loader: tensor[7]: n_dims = 1, name = resampler.attn.q.bias, tensor_size=14336, offset=182181888, shape:[3584, 1, 1, 1], type = f32
clip_model_loader: tensor[8]: n_dims = 1, name = resampler.attn.k.bias, tensor_size=14336, offset=182196224, shape:[3584, 1, 1, 1], type = f32
clip_model_loader: tensor[9]: n_dims = 1, name = resampler.attn.v.bias, tensor_size=14336, offset=182210560, shape:[3584, 1, 1, 1], type = f32
clip_model_loader: tensor[10]: n_dims = 2, name = resampler.attn.out.weight, tensor_size=25690112, offset=182224896, shape:[3584, 3584, 1, 1], type = f16
clip_model_loader: tensor[11]: n_dims = 1, name = resampler.attn.out.bias, tensor_size=14336, offset=207915008, shape:[3584, 1, 1, 1], type = f32
clip_model_loader: tensor[12]: n_dims = 1, name = resampler.ln_q.weight, tensor_size=14336, offset=207929344, shape:[3584, 1, 1, 1], type = f32
clip_model_loader: tensor[13]: n_dims = 1, name = resampler.ln_q.bias, tensor_size=14336, offset=207943680, shape:[3584, 1, 1, 1], type = f32
clip_model_loader: tensor[14]: n_dims = 1, name = resampler.ln_kv.weight, tensor_size=14336, offset=207958016, shape:[3584, 1, 1, 1], type = f32
clip_model_loader: tensor[15]: n_dims = 1, name = resampler.ln_kv.bias, tensor_size=14336, offset=207972352, shape:[3584, 1, 1, 1], type = f32
clip_model_loader: tensor[16]: n_dims = 1, name = resampler.ln_post.weight, tensor_size=14336, offset=207986688, shape:[3584, 1, 1, 1], type = f32
clip_model_loader: tensor[17]: n_dims = 1, name = resampler.ln_post.bias, tensor_size=14336, offset=208001024, shape:[3584, 1, 1, 1], type = f32
clip_model_loader: tensor[18]: n_dims = 4, name = v.patch_embd.weight, tensor_size=1354752, offset=208015360, shape:[14, 14, 3, 1152], type = f16
clip_model_loader: tensor[19]: n_dims = 1, name = v.patch_embd.bias, tensor_size=4608, offset=209370112, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[20]: n_dims = 2, name = v.position_embd.weight, tensor_size=11289600, offset=209374720, shape:[1152, 4900, 1, 1], type = f16
clip_model_loader: tensor[21]: n_dims = 2, name = v.blk.0.attn_k.weight, tensor_size=2654208, offset=220664320, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[22]: n_dims = 1, name = v.blk.0.attn_k.bias, tensor_size=4608, offset=223318528, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[23]: n_dims = 2, name = v.blk.0.attn_v.weight, tensor_size=2654208, offset=223323136, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[24]: n_dims = 1, name = v.blk.0.attn_v.bias, tensor_size=4608, offset=225977344, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[25]: n_dims = 2, name = v.blk.0.attn_q.weight, tensor_size=2654208, offset=225981952, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[26]: n_dims = 1, name = v.blk.0.attn_q.bias, tensor_size=4608, offset=228636160, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[27]: n_dims = 2, name = v.blk.0.attn_out.weight, tensor_size=2654208, offset=228640768, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[28]: n_dims = 1, name = v.blk.0.attn_out.bias, tensor_size=4608, offset=231294976, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[29]: n_dims = 1, name = v.blk.0.ln1.weight, tensor_size=4608, offset=231299584, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[30]: n_dims = 1, name = v.blk.0.ln1.bias, tensor_size=4608, offset=231304192, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[31]: n_dims = 2, name = v.blk.0.ffn_down.weight, tensor_size=9916416, offset=231308800, shape:[1152, 4304, 1, 1], type = f16
clip_model_loader: tensor[32]: n_dims = 1, name = v.blk.0.ffn_down.bias, tensor_size=17216, offset=241225216, shape:[4304, 1, 1, 1], type = f32
clip_model_loader: tensor[33]: n_dims = 2, name = v.blk.0.ffn_up.weight, tensor_size=9916416, offset=241242432, shape:[4304, 1152, 1, 1], type = f16
clip_model_loader: tensor[34]: n_dims = 1, name = v.blk.0.ffn_up.bias, tensor_size=4608, offset=251158848, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[35]: n_dims = 1, name = v.blk.0.ln2.weight, tensor_size=4608, offset=251163456, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[36]: n_dims = 1, name = v.blk.0.ln2.bias, tensor_size=4608, offset=251168064, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[37]: n_dims = 2, name = v.blk.1.attn_k.weight, tensor_size=2654208, offset=251172672, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[38]: n_dims = 1, name = v.blk.1.attn_k.bias, tensor_size=4608, offset=253826880, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[39]: n_dims = 2, name = v.blk.1.attn_v.weight, tensor_size=2654208, offset=253831488, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[40]: n_dims = 1, name = v.blk.1.attn_v.bias, tensor_size=4608, offset=256485696, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[41]: n_dims = 2, name = v.blk.1.attn_q.weight, tensor_size=2654208, offset=256490304, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[42]: n_dims = 1, name = v.blk.1.attn_q.bias, tensor_size=4608, offset=259144512, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[43]: n_dims = 2, name = v.blk.1.attn_out.weight, tensor_size=2654208, offset=259149120, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[44]: n_dims = 1, name = v.blk.1.attn_out.bias, tensor_size=4608, offset=261803328, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[45]: n_dims = 1, name = v.blk.1.ln1.weight, tensor_size=4608, offset=261807936, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[46]: n_dims = 1, name = v.blk.1.ln1.bias, tensor_size=4608, offset=261812544, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[47]: n_dims = 2, name = v.blk.1.ffn_down.weight, tensor_size=9916416, offset=261817152, shape:[1152, 4304, 1, 1], type = f16
clip_model_loader: tensor[48]: n_dims = 1, name = v.blk.1.ffn_down.bias, tensor_size=17216, offset=271733568, shape:[4304, 1, 1, 1], type = f32
clip_model_loader: tensor[49]: n_dims = 2, name = v.blk.1.ffn_up.weight, tensor_size=9916416, offset=271750784, shape:[4304, 1152, 1, 1], type = f16
clip_model_loader: tensor[50]: n_dims = 1, name = v.blk.1.ffn_up.bias, tensor_size=4608, offset=281667200, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[51]: n_dims = 1, name = v.blk.1.ln2.weight, tensor_size=4608, offset=281671808, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[52]: n_dims = 1, name = v.blk.1.ln2.bias, tensor_size=4608, offset=281676416, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[53]: n_dims = 2, name = v.blk.2.attn_k.weight, tensor_size=2654208, offset=281681024, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[54]: n_dims = 1, name = v.blk.2.attn_k.bias, tensor_size=4608, offset=284335232, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[55]: n_dims = 2, name = v.blk.2.attn_v.weight, tensor_size=2654208, offset=284339840, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[56]: n_dims = 1, name = v.blk.2.attn_v.bias, tensor_size=4608, offset=286994048, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[57]: n_dims = 2, name = v.blk.2.attn_q.weight, tensor_size=2654208, offset=286998656, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[58]: n_dims = 1, name = v.blk.2.attn_q.bias, tensor_size=4608, offset=289652864, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[59]: n_dims = 2, name = v.blk.2.attn_out.weight, tensor_size=2654208, offset=289657472, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[60]: n_dims = 1, name = v.blk.2.attn_out.bias, tensor_size=4608, offset=292311680, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[61]: n_dims = 1, name = v.blk.2.ln1.weight, tensor_size=4608, offset=292316288, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[62]: n_dims = 1, name = v.blk.2.ln1.bias, tensor_size=4608, offset=292320896, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[63]: n_dims = 2, name = v.blk.2.ffn_down.weight, tensor_size=9916416, offset=292325504, shape:[1152, 4304, 1, 1], type = f16
clip_model_loader: tensor[64]: n_dims = 1, name = v.blk.2.ffn_down.bias, tensor_size=17216, offset=302241920, shape:[4304, 1, 1, 1], type = f32
clip_model_loader: tensor[65]: n_dims = 2, name = v.blk.2.ffn_up.weight, tensor_size=9916416, offset=302259136, shape:[4304, 1152, 1, 1], type = f16
clip_model_loader: tensor[66]: n_dims = 1, name = v.blk.2.ffn_up.bias, tensor_size=4608, offset=312175552, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[67]: n_dims = 1, name = v.blk.2.ln2.weight, tensor_size=4608, offset=312180160, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[68]: n_dims = 1, name = v.blk.2.ln2.bias, tensor_size=4608, offset=312184768, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[69]: n_dims = 2, name = v.blk.3.attn_k.weight, tensor_size=2654208, offset=312189376, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[70]: n_dims = 1, name = v.blk.3.attn_k.bias, tensor_size=4608, offset=314843584, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[71]: n_dims = 2, name = v.blk.3.attn_v.weight, tensor_size=2654208, offset=314848192, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[72]: n_dims = 1, name = v.blk.3.attn_v.bias, tensor_size=4608, offset=317502400, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[73]: n_dims = 2, name = v.blk.3.attn_q.weight, tensor_size=2654208, offset=317507008, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[74]: n_dims = 1, name = v.blk.3.attn_q.bias, tensor_size=4608, offset=320161216, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[75]: n_dims = 2, name = v.blk.3.attn_out.weight, tensor_size=2654208, offset=320165824, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[76]: n_dims = 1, name = v.blk.3.attn_out.bias, tensor_size=4608, offset=322820032, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[77]: n_dims = 1, name = v.blk.3.ln1.weight, tensor_size=4608, offset=322824640, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[78]: n_dims = 1, name = v.blk.3.ln1.bias, tensor_size=4608, offset=322829248, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[79]: n_dims = 2, name = v.blk.3.ffn_down.weight, tensor_size=9916416, offset=322833856, shape:[1152, 4304, 1, 1], type = f16
clip_model_loader: tensor[80]: n_dims = 1, name = v.blk.3.ffn_down.bias, tensor_size=17216, offset=332750272, shape:[4304, 1, 1, 1], type = f32
clip_model_loader: tensor[81]: n_dims = 2, name = v.blk.3.ffn_up.weight, tensor_size=9916416, offset=332767488, shape:[4304, 1152, 1, 1], type = f16
clip_model_loader: tensor[82]: n_dims = 1, name = v.blk.3.ffn_up.bias, tensor_size=4608, offset=342683904, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[83]: n_dims = 1, name = v.blk.3.ln2.weight, tensor_size=4608, offset=342688512, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[84]: n_dims = 1, name = v.blk.3.ln2.bias, tensor_size=4608, offset=342693120, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[85]: n_dims = 2, name = v.blk.4.attn_k.weight, tensor_size=2654208, offset=342697728, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[86]: n_dims = 1, name = v.blk.4.attn_k.bias, tensor_size=4608, offset=345351936, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[87]: n_dims = 2, name = v.blk.4.attn_v.weight, tensor_size=2654208, offset=345356544, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[88]: n_dims = 1, name = v.blk.4.attn_v.bias, tensor_size=4608, offset=348010752, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[89]: n_dims = 2, name = v.blk.4.attn_q.weight, tensor_size=2654208, offset=348015360, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[90]: n_dims = 1, name = v.blk.4.attn_q.bias, tensor_size=4608, offset=350669568, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[91]: n_dims = 2, name = v.blk.4.attn_out.weight, tensor_size=2654208, offset=350674176, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[92]: n_dims = 1, name = v.blk.4.attn_out.bias, tensor_size=4608, offset=353328384, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[93]: n_dims = 1, name = v.blk.4.ln1.weight, tensor_size=4608, offset=353332992, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[94]: n_dims = 1, name = v.blk.4.ln1.bias, tensor_size=4608, offset=353337600, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[95]: n_dims = 2, name = v.blk.4.ffn_down.weight, tensor_size=9916416, offset=353342208, shape:[1152, 4304, 1, 1], type = f16
clip_model_loader: tensor[96]: n_dims = 1, name = v.blk.4.ffn_down.bias, tensor_size=17216, offset=363258624, shape:[4304, 1, 1, 1], type = f32
clip_model_loader: tensor[97]: n_dims = 2, name = v.blk.4.ffn_up.weight, tensor_size=9916416, offset=363275840, shape:[4304, 1152, 1, 1], type = f16
clip_model_loader: tensor[98]: n_dims = 1, name = v.blk.4.ffn_up.bias, tensor_size=4608, offset=373192256, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[99]: n_dims = 1, name = v.blk.4.ln2.weight, tensor_size=4608, offset=373196864, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[100]: n_dims = 1, name = v.blk.4.ln2.bias, tensor_size=4608, offset=373201472, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[101]: n_dims = 2, name = v.blk.5.attn_k.weight, tensor_size=2654208, offset=373206080, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[102]: n_dims = 1, name = v.blk.5.attn_k.bias, tensor_size=4608, offset=375860288, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[103]: n_dims = 2, name = v.blk.5.attn_v.weight, tensor_size=2654208, offset=375864896, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[104]: n_dims = 1, name = v.blk.5.attn_v.bias, tensor_size=4608, offset=378519104, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[105]: n_dims = 2, name = v.blk.5.attn_q.weight, tensor_size=2654208, offset=378523712, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[106]: n_dims = 1, name = v.blk.5.attn_q.bias, tensor_size=4608, offset=381177920, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[107]: n_dims = 2, name = v.blk.5.attn_out.weight, tensor_size=2654208, offset=381182528, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[108]: n_dims = 1, name = v.blk.5.attn_out.bias, tensor_size=4608, offset=383836736, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[109]: n_dims = 1, name = v.blk.5.ln1.weight, tensor_size=4608, offset=383841344, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[110]: n_dims = 1, name = v.blk.5.ln1.bias, tensor_size=4608, offset=383845952, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[111]: n_dims = 2, name = v.blk.5.ffn_down.weight, tensor_size=9916416, offset=383850560, shape:[1152, 4304, 1, 1], type = f16
clip_model_loader: tensor[112]: n_dims = 1, name = v.blk.5.ffn_down.bias, tensor_size=17216, offset=393766976, shape:[4304, 1, 1, 1], type = f32
clip_model_loader: tensor[113]: n_dims = 2, name = v.blk.5.ffn_up.weight, tensor_size=9916416, offset=393784192, shape:[4304, 1152, 1, 1], type = f16
clip_model_loader: tensor[114]: n_dims = 1, name = v.blk.5.ffn_up.bias, tensor_size=4608, offset=403700608, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[115]: n_dims = 1, name = v.blk.5.ln2.weight, tensor_size=4608, offset=403705216, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[116]: n_dims = 1, name = v.blk.5.ln2.bias, tensor_size=4608, offset=403709824, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[117]: n_dims = 2, name = v.blk.6.attn_k.weight, tensor_size=2654208, offset=403714432, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[118]: n_dims = 1, name = v.blk.6.attn_k.bias, tensor_size=4608, offset=406368640, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[119]: n_dims = 2, name = v.blk.6.attn_v.weight, tensor_size=2654208, offset=406373248, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[120]: n_dims = 1, name = v.blk.6.attn_v.bias, tensor_size=4608, offset=409027456, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[121]: n_dims = 2, name = v.blk.6.attn_q.weight, tensor_size=2654208, offset=409032064, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[122]: n_dims = 1, name = v.blk.6.attn_q.bias, tensor_size=4608, offset=411686272, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[123]: n_dims = 2, name = v.blk.6.attn_out.weight, tensor_size=2654208, offset=411690880, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[124]: n_dims = 1, name = v.blk.6.attn_out.bias, tensor_size=4608, offset=414345088, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[125]: n_dims = 1, name = v.blk.6.ln1.weight, tensor_size=4608, offset=414349696, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[126]: n_dims = 1, name = v.blk.6.ln1.bias, tensor_size=4608, offset=414354304, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[127]: n_dims = 2, name = v.blk.6.ffn_down.weight, tensor_size=9916416, offset=414358912, shape:[1152, 4304, 1, 1], type = f16
clip_model_loader: tensor[128]: n_dims = 1, name = v.blk.6.ffn_down.bias, tensor_size=17216, offset=424275328, shape:[4304, 1, 1, 1], type = f32
clip_model_loader: tensor[129]: n_dims = 2, name = v.blk.6.ffn_up.weight, tensor_size=9916416, offset=424292544, shape:[4304, 1152, 1, 1], type = f16
clip_model_loader: tensor[130]: n_dims = 1, name = v.blk.6.ffn_up.bias, tensor_size=4608, offset=434208960, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[131]: n_dims = 1, name = v.blk.6.ln2.weight, tensor_size=4608, offset=434213568, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[132]: n_dims = 1, name = v.blk.6.ln2.bias, tensor_size=4608, offset=434218176, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[133]: n_dims = 2, name = v.blk.7.attn_k.weight, tensor_size=2654208, offset=434222784, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[134]: n_dims = 1, name = v.blk.7.attn_k.bias, tensor_size=4608, offset=436876992, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[135]: n_dims = 2, name = v.blk.7.attn_v.weight, tensor_size=2654208, offset=436881600, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[136]: n_dims = 1, name = v.blk.7.attn_v.bias, tensor_size=4608, offset=439535808, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[137]: n_dims = 2, name = v.blk.7.attn_q.weight, tensor_size=2654208, offset=439540416, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[138]: n_dims = 1, name = v.blk.7.attn_q.bias, tensor_size=4608, offset=442194624, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[139]: n_dims = 2, name = v.blk.7.attn_out.weight, tensor_size=2654208, offset=442199232, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[140]: n_dims = 1, name = v.blk.7.attn_out.bias, tensor_size=4608, offset=444853440, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[141]: n_dims = 1, name = v.blk.7.ln1.weight, tensor_size=4608, offset=444858048, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[142]: n_dims = 1, name = v.blk.7.ln1.bias, tensor_size=4608, offset=444862656, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[143]: n_dims = 2, name = v.blk.7.ffn_down.weight, tensor_size=9916416, offset=444867264, shape:[1152, 4304, 1, 1], type = f16
clip_model_loader: tensor[144]: n_dims = 1, name = v.blk.7.ffn_down.bias, tensor_size=17216, offset=454783680, shape:[4304, 1, 1, 1], type = f32
clip_model_loader: tensor[145]: n_dims = 2, name = v.blk.7.ffn_up.weight, tensor_size=9916416, offset=454800896, shape:[4304, 1152, 1, 1], type = f16
clip_model_loader: tensor[146]: n_dims = 1, name = v.blk.7.ffn_up.bias, tensor_size=4608, offset=464717312, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[147]: n_dims = 1, name = v.blk.7.ln2.weight, tensor_size=4608, offset=464721920, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[148]: n_dims = 1, name = v.blk.7.ln2.bias, tensor_size=4608, offset=464726528, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[149]: n_dims = 2, name = v.blk.8.attn_k.weight, tensor_size=2654208, offset=464731136, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[150]: n_dims = 1, name = v.blk.8.attn_k.bias, tensor_size=4608, offset=467385344, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[151]: n_dims = 2, name = v.blk.8.attn_v.weight, tensor_size=2654208, offset=467389952, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[152]: n_dims = 1, name = v.blk.8.attn_v.bias, tensor_size=4608, offset=470044160, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[153]: n_dims = 2, name = v.blk.8.attn_q.weight, tensor_size=2654208, offset=470048768, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[154]: n_dims = 1, name = v.blk.8.attn_q.bias, tensor_size=4608, offset=472702976, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[155]: n_dims = 2, name = v.blk.8.attn_out.weight, tensor_size=2654208, offset=472707584, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[156]: n_dims = 1, name = v.blk.8.attn_out.bias, tensor_size=4608, offset=475361792, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[157]: n_dims = 1, name = v.blk.8.ln1.weight, tensor_size=4608, offset=475366400, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[158]: n_dims = 1, name = v.blk.8.ln1.bias, tensor_size=4608, offset=475371008, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[159]: n_dims = 2, name = v.blk.8.ffn_down.weight, tensor_size=9916416, offset=475375616, shape:[1152, 4304, 1, 1], type = f16
clip_model_loader: tensor[160]: n_dims = 1, name = v.blk.8.ffn_down.bias, tensor_size=17216, offset=485292032, shape:[4304, 1, 1, 1], type = f32
clip_model_loader: tensor[161]: n_dims = 2, name = v.blk.8.ffn_up.weight, tensor_size=9916416, offset=485309248, shape:[4304, 1152, 1, 1], type = f16
clip_model_loader: tensor[162]: n_dims = 1, name = v.blk.8.ffn_up.bias, tensor_size=4608, offset=495225664, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[163]: n_dims = 1, name = v.blk.8.ln2.weight, tensor_size=4608, offset=495230272, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[164]: n_dims = 1, name = v.blk.8.ln2.bias, tensor_size=4608, offset=495234880, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[165]: n_dims = 2, name = v.blk.9.attn_k.weight, tensor_size=2654208, offset=495239488, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[166]: n_dims = 1, name = v.blk.9.attn_k.bias, tensor_size=4608, offset=497893696, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[167]: n_dims = 2, name = v.blk.9.attn_v.weight, tensor_size=2654208, offset=497898304, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[168]: n_dims = 1, name = v.blk.9.attn_v.bias, tensor_size=4608, offset=500552512, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[169]: n_dims = 2, name = v.blk.9.attn_q.weight, tensor_size=2654208, offset=500557120, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[170]: n_dims = 1, name = v.blk.9.attn_q.bias, tensor_size=4608, offset=503211328, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[171]: n_dims = 2, name = v.blk.9.attn_out.weight, tensor_size=2654208, offset=503215936, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[172]: n_dims = 1, name = v.blk.9.attn_out.bias, tensor_size=4608, offset=505870144, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[173]: n_dims = 1, name = v.blk.9.ln1.weight, tensor_size=4608, offset=505874752, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[174]: n_dims = 1, name = v.blk.9.ln1.bias, tensor_size=4608, offset=505879360, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[175]: n_dims = 2, name = v.blk.9.ffn_down.weight, tensor_size=9916416, offset=505883968, shape:[1152, 4304, 1, 1], type = f16
clip_model_loader: tensor[176]: n_dims = 1, name = v.blk.9.ffn_down.bias, tensor_size=17216, offset=515800384, shape:[4304, 1, 1, 1], type = f32
clip_model_loader: tensor[177]: n_dims = 2, name = v.blk.9.ffn_up.weight, tensor_size=9916416, offset=515817600, shape:[4304, 1152, 1, 1], type = f16
clip_model_loader: tensor[178]: n_dims = 1, name = v.blk.9.ffn_up.bias, tensor_size=4608, offset=525734016, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[179]: n_dims = 1, name = v.blk.9.ln2.weight, tensor_size=4608, offset=525738624, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[180]: n_dims = 1, name = v.blk.9.ln2.bias, tensor_size=4608, offset=525743232, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[181]: n_dims = 2, name = v.blk.10.attn_k.weight, tensor_size=2654208, offset=525747840, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[182]: n_dims = 1, name = v.blk.10.attn_k.bias, tensor_size=4608, offset=528402048, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[183]: n_dims = 2, name = v.blk.10.attn_v.weight, tensor_size=2654208, offset=528406656, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[184]: n_dims = 1, name = v.blk.10.attn_v.bias, tensor_size=4608, offset=531060864, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[185]: n_dims = 2, name = v.blk.10.attn_q.weight, tensor_size=2654208, offset=531065472, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[186]: n_dims = 1, name = v.blk.10.attn_q.bias, tensor_size=4608, offset=533719680, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[187]: n_dims = 2, name = v.blk.10.attn_out.weight, tensor_size=2654208, offset=533724288, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[188]: n_dims = 1, name = v.blk.10.attn_out.bias, tensor_size=4608, offset=536378496, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[189]: n_dims = 1, name = v.blk.10.ln1.weight, tensor_size=4608, offset=536383104, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[190]: n_dims = 1, name = v.blk.10.ln1.bias, tensor_size=4608, offset=536387712, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[191]: n_dims = 2, name = v.blk.10.ffn_down.weight, tensor_size=9916416, offset=536392320, shape:[1152, 4304, 1, 1], type = f16
clip_model_loader: tensor[192]: n_dims = 1, name = v.blk.10.ffn_down.bias, tensor_size=17216, offset=546308736, shape:[4304, 1, 1, 1], type = f32
clip_model_loader: tensor[193]: n_dims = 2, name = v.blk.10.ffn_up.weight, tensor_size=9916416, offset=546325952, shape:[4304, 1152, 1, 1], type = f16
clip_model_loader: tensor[194]: n_dims = 1, name = v.blk.10.ffn_up.bias, tensor_size=4608, offset=556242368, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[195]: n_dims = 1, name = v.blk.10.ln2.weight, tensor_size=4608, offset=556246976, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[196]: n_dims = 1, name = v.blk.10.ln2.bias, tensor_size=4608, offset=556251584, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[197]: n_dims = 2, name = v.blk.11.attn_k.weight, tensor_size=2654208, offset=556256192, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[198]: n_dims = 1, name = v.blk.11.attn_k.bias, tensor_size=4608, offset=558910400, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[199]: n_dims = 2, name = v.blk.11.attn_v.weight, tensor_size=2654208, offset=558915008, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[200]: n_dims = 1, name = v.blk.11.attn_v.bias, tensor_size=4608, offset=561569216, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[201]: n_dims = 2, name = v.blk.11.attn_q.weight, tensor_size=2654208, offset=561573824, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[202]: n_dims = 1, name = v.blk.11.attn_q.bias, tensor_size=4608, offset=564228032, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[203]: n_dims = 2, name = v.blk.11.attn_out.weight, tensor_size=2654208, offset=564232640, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[204]: n_dims = 1, name = v.blk.11.attn_out.bias, tensor_size=4608, offset=566886848, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[205]: n_dims = 1, name = v.blk.11.ln1.weight, tensor_size=4608, offset=566891456, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[206]: n_dims = 1, name = v.blk.11.ln1.bias, tensor_size=4608, offset=566896064, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[207]: n_dims = 2, name = v.blk.11.ffn_down.weight, tensor_size=9916416, offset=566900672, shape:[1152, 4304, 1, 1], type = f16
clip_model_loader: tensor[208]: n_dims = 1, name = v.blk.11.ffn_down.bias, tensor_size=17216, offset=576817088, shape:[4304, 1, 1, 1], type = f32
clip_model_loader: tensor[209]: n_dims = 2, name = v.blk.11.ffn_up.weight, tensor_size=9916416, offset=576834304, shape:[4304, 1152, 1, 1], type = f16
clip_model_loader: tensor[210]: n_dims = 1, name = v.blk.11.ffn_up.bias, tensor_size=4608, offset=586750720, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[211]: n_dims = 1, name = v.blk.11.ln2.weight, tensor_size=4608, offset=586755328, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[212]: n_dims = 1, name = v.blk.11.ln2.bias, tensor_size=4608, offset=586759936, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[213]: n_dims = 2, name = v.blk.12.attn_k.weight, tensor_size=2654208, offset=586764544, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[214]: n_dims = 1, name = v.blk.12.attn_k.bias, tensor_size=4608, offset=589418752, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[215]: n_dims = 2, name = v.blk.12.attn_v.weight, tensor_size=2654208, offset=589423360, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[216]: n_dims = 1, name = v.blk.12.attn_v.bias, tensor_size=4608, offset=592077568, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[217]: n_dims = 2, name = v.blk.12.attn_q.weight, tensor_size=2654208, offset=592082176, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[218]: n_dims = 1, name = v.blk.12.attn_q.bias, tensor_size=4608, offset=594736384, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[219]: n_dims = 2, name = v.blk.12.attn_out.weight, tensor_size=2654208, offset=594740992, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[220]: n_dims = 1, name = v.blk.12.attn_out.bias, tensor_size=4608, offset=597395200, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[221]: n_dims = 1, name = v.blk.12.ln1.weight, tensor_size=4608, offset=597399808, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[222]: n_dims = 1, name = v.blk.12.ln1.bias, tensor_size=4608, offset=597404416, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[223]: n_dims = 2, name = v.blk.12.ffn_down.weight, tensor_size=9916416, offset=597409024, shape:[1152, 4304, 1, 1], type = f16
clip_model_loader: tensor[224]: n_dims = 1, name = v.blk.12.ffn_down.bias, tensor_size=17216, offset=607325440, shape:[4304, 1, 1, 1], type = f32
clip_model_loader: tensor[225]: n_dims = 2, name = v.blk.12.ffn_up.weight, tensor_size=9916416, offset=607342656, shape:[4304, 1152, 1, 1], type = f16
clip_model_loader: tensor[226]: n_dims = 1, name = v.blk.12.ffn_up.bias, tensor_size=4608, offset=617259072, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[227]: n_dims = 1, name = v.blk.12.ln2.weight, tensor_size=4608, offset=617263680, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[228]: n_dims = 1, name = v.blk.12.ln2.bias, tensor_size=4608, offset=617268288, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[229]: n_dims = 2, name = v.blk.13.attn_k.weight, tensor_size=2654208, offset=617272896, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[230]: n_dims = 1, name = v.blk.13.attn_k.bias, tensor_size=4608, offset=619927104, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[231]: n_dims = 2, name = v.blk.13.attn_v.weight, tensor_size=2654208, offset=619931712, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[232]: n_dims = 1, name = v.blk.13.attn_v.bias, tensor_size=4608, offset=622585920, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[233]: n_dims = 2, name = v.blk.13.attn_q.weight, tensor_size=2654208, offset=622590528, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[234]: n_dims = 1, name = v.blk.13.attn_q.bias, tensor_size=4608, offset=625244736, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[235]: n_dims = 2, name = v.blk.13.attn_out.weight, tensor_size=2654208, offset=625249344, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[236]: n_dims = 1, name = v.blk.13.attn_out.bias, tensor_size=4608, offset=627903552, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[237]: n_dims = 1, name = v.blk.13.ln1.weight, tensor_size=4608, offset=627908160, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[238]: n_dims = 1, name = v.blk.13.ln1.bias, tensor_size=4608, offset=627912768, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[239]: n_dims = 2, name = v.blk.13.ffn_down.weight, tensor_size=9916416, offset=627917376, shape:[1152, 4304, 1, 1], type = f16
clip_model_loader: tensor[240]: n_dims = 1, name = v.blk.13.ffn_down.bias, tensor_size=17216, offset=637833792, shape:[4304, 1, 1, 1], type = f32
clip_model_loader: tensor[241]: n_dims = 2, name = v.blk.13.ffn_up.weight, tensor_size=9916416, offset=637851008, shape:[4304, 1152, 1, 1], type = f16
clip_model_loader: tensor[242]: n_dims = 1, name = v.blk.13.ffn_up.bias, tensor_size=4608, offset=647767424, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[243]: n_dims = 1, name = v.blk.13.ln2.weight, tensor_size=4608, offset=647772032, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[244]: n_dims = 1, name = v.blk.13.ln2.bias, tensor_size=4608, offset=647776640, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[245]: n_dims = 2, name = v.blk.14.attn_k.weight, tensor_size=2654208, offset=647781248, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[246]: n_dims = 1, name = v.blk.14.attn_k.bias, tensor_size=4608, offset=650435456, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[247]: n_dims = 2, name = v.blk.14.attn_v.weight, tensor_size=2654208, offset=650440064, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[248]: n_dims = 1, name = v.blk.14.attn_v.bias, tensor_size=4608, offset=653094272, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[249]: n_dims = 2, name = v.blk.14.attn_q.weight, tensor_size=2654208, offset=653098880, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[250]: n_dims = 1, name = v.blk.14.attn_q.bias, tensor_size=4608, offset=655753088, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[251]: n_dims = 2, name = v.blk.14.attn_out.weight, tensor_size=2654208, offset=655757696, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[252]: n_dims = 1, name = v.blk.14.attn_out.bias, tensor_size=4608, offset=658411904, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[253]: n_dims = 1, name = v.blk.14.ln1.weight, tensor_size=4608, offset=658416512, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[254]: n_dims = 1, name = v.blk.14.ln1.bias, tensor_size=4608, offset=658421120, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[255]: n_dims = 2, name = v.blk.14.ffn_down.weight, tensor_size=9916416, offset=658425728, shape:[1152, 4304, 1, 1], type = f16
clip_model_loader: tensor[256]: n_dims = 1, name = v.blk.14.ffn_down.bias, tensor_size=17216, offset=668342144, shape:[4304, 1, 1, 1], type = f32
clip_model_loader: tensor[257]: n_dims = 2, name = v.blk.14.ffn_up.weight, tensor_size=9916416, offset=668359360, shape:[4304, 1152, 1, 1], type = f16
clip_model_loader: tensor[258]: n_dims = 1, name = v.blk.14.ffn_up.bias, tensor_size=4608, offset=678275776, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[259]: n_dims = 1, name = v.blk.14.ln2.weight, tensor_size=4608, offset=678280384, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[260]: n_dims = 1, name = v.blk.14.ln2.bias, tensor_size=4608, offset=678284992, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[261]: n_dims = 2, name = v.blk.15.attn_k.weight, tensor_size=2654208, offset=678289600, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[262]: n_dims = 1, name = v.blk.15.attn_k.bias, tensor_size=4608, offset=680943808, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[263]: n_dims = 2, name = v.blk.15.attn_v.weight, tensor_size=2654208, offset=680948416, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[264]: n_dims = 1, name = v.blk.15.attn_v.bias, tensor_size=4608, offset=683602624, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[265]: n_dims = 2, name = v.blk.15.attn_q.weight, tensor_size=2654208, offset=683607232, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[266]: n_dims = 1, name = v.blk.15.attn_q.bias, tensor_size=4608, offset=686261440, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[267]: n_dims = 2, name = v.blk.15.attn_out.weight, tensor_size=2654208, offset=686266048, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[268]: n_dims = 1, name = v.blk.15.attn_out.bias, tensor_size=4608, offset=688920256, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[269]: n_dims = 1, name = v.blk.15.ln1.weight, tensor_size=4608, offset=688924864, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[270]: n_dims = 1, name = v.blk.15.ln1.bias, tensor_size=4608, offset=688929472, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[271]: n_dims = 2, name = v.blk.15.ffn_down.weight, tensor_size=9916416, offset=688934080, shape:[1152, 4304, 1, 1], type = f16
clip_model_loader: tensor[272]: n_dims = 1, name = v.blk.15.ffn_down.bias, tensor_size=17216, offset=698850496, shape:[4304, 1, 1, 1], type = f32
clip_model_loader: tensor[273]: n_dims = 2, name = v.blk.15.ffn_up.weight, tensor_size=9916416, offset=698867712, shape:[4304, 1152, 1, 1], type = f16
clip_model_loader: tensor[274]: n_dims = 1, name = v.blk.15.ffn_up.bias, tensor_size=4608, offset=708784128, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[275]: n_dims = 1, name = v.blk.15.ln2.weight, tensor_size=4608, offset=708788736, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[276]: n_dims = 1, name = v.blk.15.ln2.bias, tensor_size=4608, offset=708793344, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[277]: n_dims = 2, name = v.blk.16.attn_k.weight, tensor_size=2654208, offset=708797952, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[278]: n_dims = 1, name = v.blk.16.attn_k.bias, tensor_size=4608, offset=711452160, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[279]: n_dims = 2, name = v.blk.16.attn_v.weight, tensor_size=2654208, offset=711456768, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[280]: n_dims = 1, name = v.blk.16.attn_v.bias, tensor_size=4608, offset=714110976, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[281]: n_dims = 2, name = v.blk.16.attn_q.weight, tensor_size=2654208, offset=714115584, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[282]: n_dims = 1, name = v.blk.16.attn_q.bias, tensor_size=4608, offset=716769792, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[283]: n_dims = 2, name = v.blk.16.attn_out.weight, tensor_size=2654208, offset=716774400, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[284]: n_dims = 1, name = v.blk.16.attn_out.bias, tensor_size=4608, offset=719428608, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[285]: n_dims = 1, name = v.blk.16.ln1.weight, tensor_size=4608, offset=719433216, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[286]: n_dims = 1, name = v.blk.16.ln1.bias, tensor_size=4608, offset=719437824, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[287]: n_dims = 2, name = v.blk.16.ffn_down.weight, tensor_size=9916416, offset=719442432, shape:[1152, 4304, 1, 1], type = f16
clip_model_loader: tensor[288]: n_dims = 1, name = v.blk.16.ffn_down.bias, tensor_size=17216, offset=729358848, shape:[4304, 1, 1, 1], type = f32
clip_model_loader: tensor[289]: n_dims = 2, name = v.blk.16.ffn_up.weight, tensor_size=9916416, offset=729376064, shape:[4304, 1152, 1, 1], type = f16
clip_model_loader: tensor[290]: n_dims = 1, name = v.blk.16.ffn_up.bias, tensor_size=4608, offset=739292480, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[291]: n_dims = 1, name = v.blk.16.ln2.weight, tensor_size=4608, offset=739297088, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[292]: n_dims = 1, name = v.blk.16.ln2.bias, tensor_size=4608, offset=739301696, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[293]: n_dims = 2, name = v.blk.17.attn_k.weight, tensor_size=2654208, offset=739306304, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[294]: n_dims = 1, name = v.blk.17.attn_k.bias, tensor_size=4608, offset=741960512, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[295]: n_dims = 2, name = v.blk.17.attn_v.weight, tensor_size=2654208, offset=741965120, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[296]: n_dims = 1, name = v.blk.17.attn_v.bias, tensor_size=4608, offset=744619328, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[297]: n_dims = 2, name = v.blk.17.attn_q.weight, tensor_size=2654208, offset=744623936, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[298]: n_dims = 1, name = v.blk.17.attn_q.bias, tensor_size=4608, offset=747278144, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[299]: n_dims = 2, name = v.blk.17.attn_out.weight, tensor_size=2654208, offset=747282752, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[300]: n_dims = 1, name = v.blk.17.attn_out.bias, tensor_size=4608, offset=749936960, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[301]: n_dims = 1, name = v.blk.17.ln1.weight, tensor_size=4608, offset=749941568, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[302]: n_dims = 1, name = v.blk.17.ln1.bias, tensor_size=4608, offset=749946176, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[303]: n_dims = 2, name = v.blk.17.ffn_down.weight, tensor_size=9916416, offset=749950784, shape:[1152, 4304, 1, 1], type = f16
clip_model_loader: tensor[304]: n_dims = 1, name = v.blk.17.ffn_down.bias, tensor_size=17216, offset=759867200, shape:[4304, 1, 1, 1], type = f32
clip_model_loader: tensor[305]: n_dims = 2, name = v.blk.17.ffn_up.weight, tensor_size=9916416, offset=759884416, shape:[4304, 1152, 1, 1], type = f16
clip_model_loader: tensor[306]: n_dims = 1, name = v.blk.17.ffn_up.bias, tensor_size=4608, offset=769800832, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[307]: n_dims = 1, name = v.blk.17.ln2.weight, tensor_size=4608, offset=769805440, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[308]: n_dims = 1, name = v.blk.17.ln2.bias, tensor_size=4608, offset=769810048, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[309]: n_dims = 2, name = v.blk.18.attn_k.weight, tensor_size=2654208, offset=769814656, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[310]: n_dims = 1, name = v.blk.18.attn_k.bias, tensor_size=4608, offset=772468864, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[311]: n_dims = 2, name = v.blk.18.attn_v.weight, tensor_size=2654208, offset=772473472, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[312]: n_dims = 1, name = v.blk.18.attn_v.bias, tensor_size=4608, offset=775127680, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[313]: n_dims = 2, name = v.blk.18.attn_q.weight, tensor_size=2654208, offset=775132288, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[314]: n_dims = 1, name = v.blk.18.attn_q.bias, tensor_size=4608, offset=777786496, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[315]: n_dims = 2, name = v.blk.18.attn_out.weight, tensor_size=2654208, offset=777791104, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[316]: n_dims = 1, name = v.blk.18.attn_out.bias, tensor_size=4608, offset=780445312, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[317]: n_dims = 1, name = v.blk.18.ln1.weight, tensor_size=4608, offset=780449920, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[318]: n_dims = 1, name = v.blk.18.ln1.bias, tensor_size=4608, offset=780454528, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[319]: n_dims = 2, name = v.blk.18.ffn_down.weight, tensor_size=9916416, offset=780459136, shape:[1152, 4304, 1, 1], type = f16
clip_model_loader: tensor[320]: n_dims = 1, name = v.blk.18.ffn_down.bias, tensor_size=17216, offset=790375552, shape:[4304, 1, 1, 1], type = f32
clip_model_loader: tensor[321]: n_dims = 2, name = v.blk.18.ffn_up.weight, tensor_size=9916416, offset=790392768, shape:[4304, 1152, 1, 1], type = f16
clip_model_loader: tensor[322]: n_dims = 1, name = v.blk.18.ffn_up.bias, tensor_size=4608, offset=800309184, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[323]: n_dims = 1, name = v.blk.18.ln2.weight, tensor_size=4608, offset=800313792, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[324]: n_dims = 1, name = v.blk.18.ln2.bias, tensor_size=4608, offset=800318400, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[325]: n_dims = 2, name = v.blk.19.attn_k.weight, tensor_size=2654208, offset=800323008, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[326]: n_dims = 1, name = v.blk.19.attn_k.bias, tensor_size=4608, offset=802977216, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[327]: n_dims = 2, name = v.blk.19.attn_v.weight, tensor_size=2654208, offset=802981824, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[328]: n_dims = 1, name = v.blk.19.attn_v.bias, tensor_size=4608, offset=805636032, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[329]: n_dims = 2, name = v.blk.19.attn_q.weight, tensor_size=2654208, offset=805640640, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[330]: n_dims = 1, name = v.blk.19.attn_q.bias, tensor_size=4608, offset=808294848, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[331]: n_dims = 2, name = v.blk.19.attn_out.weight, tensor_size=2654208, offset=808299456, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[332]: n_dims = 1, name = v.blk.19.attn_out.bias, tensor_size=4608, offset=810953664, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[333]: n_dims = 1, name = v.blk.19.ln1.weight, tensor_size=4608, offset=810958272, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[334]: n_dims = 1, name = v.blk.19.ln1.bias, tensor_size=4608, offset=810962880, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[335]: n_dims = 2, name = v.blk.19.ffn_down.weight, tensor_size=9916416, offset=810967488, shape:[1152, 4304, 1, 1], type = f16
clip_model_loader: tensor[336]: n_dims = 1, name = v.blk.19.ffn_down.bias, tensor_size=17216, offset=820883904, shape:[4304, 1, 1, 1], type = f32
clip_model_loader: tensor[337]: n_dims = 2, name = v.blk.19.ffn_up.weight, tensor_size=9916416, offset=820901120, shape:[4304, 1152, 1, 1], type = f16
clip_model_loader: tensor[338]: n_dims = 1, name = v.blk.19.ffn_up.bias, tensor_size=4608, offset=830817536, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[339]: n_dims = 1, name = v.blk.19.ln2.weight, tensor_size=4608, offset=830822144, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[340]: n_dims = 1, name = v.blk.19.ln2.bias, tensor_size=4608, offset=830826752, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[341]: n_dims = 2, name = v.blk.20.attn_k.weight, tensor_size=2654208, offset=830831360, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[342]: n_dims = 1, name = v.blk.20.attn_k.bias, tensor_size=4608, offset=833485568, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[343]: n_dims = 2, name = v.blk.20.attn_v.weight, tensor_size=2654208, offset=833490176, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[344]: n_dims = 1, name = v.blk.20.attn_v.bias, tensor_size=4608, offset=836144384, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[345]: n_dims = 2, name = v.blk.20.attn_q.weight, tensor_size=2654208, offset=836148992, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[346]: n_dims = 1, name = v.blk.20.attn_q.bias, tensor_size=4608, offset=838803200, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[347]: n_dims = 2, name = v.blk.20.attn_out.weight, tensor_size=2654208, offset=838807808, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[348]: n_dims = 1, name = v.blk.20.attn_out.bias, tensor_size=4608, offset=841462016, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[349]: n_dims = 1, name = v.blk.20.ln1.weight, tensor_size=4608, offset=841466624, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[350]: n_dims = 1, name = v.blk.20.ln1.bias, tensor_size=4608, offset=841471232, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[351]: n_dims = 2, name = v.blk.20.ffn_down.weight, tensor_size=9916416, offset=841475840, shape:[1152, 4304, 1, 1], type = f16
clip_model_loader: tensor[352]: n_dims = 1, name = v.blk.20.ffn_down.bias, tensor_size=17216, offset=851392256, shape:[4304, 1, 1, 1], type = f32
clip_model_loader: tensor[353]: n_dims = 2, name = v.blk.20.ffn_up.weight, tensor_size=9916416, offset=851409472, shape:[4304, 1152, 1, 1], type = f16
clip_model_loader: tensor[354]: n_dims = 1, name = v.blk.20.ffn_up.bias, tensor_size=4608, offset=861325888, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[355]: n_dims = 1, name = v.blk.20.ln2.weight, tensor_size=4608, offset=861330496, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[356]: n_dims = 1, name = v.blk.20.ln2.bias, tensor_size=4608, offset=861335104, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[357]: n_dims = 2, name = v.blk.21.attn_k.weight, tensor_size=2654208, offset=861339712, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[358]: n_dims = 1, name = v.blk.21.attn_k.bias, tensor_size=4608, offset=863993920, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[359]: n_dims = 2, name = v.blk.21.attn_v.weight, tensor_size=2654208, offset=863998528, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[360]: n_dims = 1, name = v.blk.21.attn_v.bias, tensor_size=4608, offset=866652736, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[361]: n_dims = 2, name = v.blk.21.attn_q.weight, tensor_size=2654208, offset=866657344, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[362]: n_dims = 1, name = v.blk.21.attn_q.bias, tensor_size=4608, offset=869311552, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[363]: n_dims = 2, name = v.blk.21.attn_out.weight, tensor_size=2654208, offset=869316160, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[364]: n_dims = 1, name = v.blk.21.attn_out.bias, tensor_size=4608, offset=871970368, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[365]: n_dims = 1, name = v.blk.21.ln1.weight, tensor_size=4608, offset=871974976, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[366]: n_dims = 1, name = v.blk.21.ln1.bias, tensor_size=4608, offset=871979584, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[367]: n_dims = 2, name = v.blk.21.ffn_down.weight, tensor_size=9916416, offset=871984192, shape:[1152, 4304, 1, 1], type = f16
clip_model_loader: tensor[368]: n_dims = 1, name = v.blk.21.ffn_down.bias, tensor_size=17216, offset=881900608, shape:[4304, 1, 1, 1], type = f32
clip_model_loader: tensor[369]: n_dims = 2, name = v.blk.21.ffn_up.weight, tensor_size=9916416, offset=881917824, shape:[4304, 1152, 1, 1], type = f16
clip_model_loader: tensor[370]: n_dims = 1, name = v.blk.21.ffn_up.bias, tensor_size=4608, offset=891834240, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[371]: n_dims = 1, name = v.blk.21.ln2.weight, tensor_size=4608, offset=891838848, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[372]: n_dims = 1, name = v.blk.21.ln2.bias, tensor_size=4608, offset=891843456, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[373]: n_dims = 2, name = v.blk.22.attn_k.weight, tensor_size=2654208, offset=891848064, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[374]: n_dims = 1, name = v.blk.22.attn_k.bias, tensor_size=4608, offset=894502272, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[375]: n_dims = 2, name = v.blk.22.attn_v.weight, tensor_size=2654208, offset=894506880, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[376]: n_dims = 1, name = v.blk.22.attn_v.bias, tensor_size=4608, offset=897161088, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[377]: n_dims = 2, name = v.blk.22.attn_q.weight, tensor_size=2654208, offset=897165696, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[378]: n_dims = 1, name = v.blk.22.attn_q.bias, tensor_size=4608, offset=899819904, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[379]: n_dims = 2, name = v.blk.22.attn_out.weight, tensor_size=2654208, offset=899824512, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[380]: n_dims = 1, name = v.blk.22.attn_out.bias, tensor_size=4608, offset=902478720, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[381]: n_dims = 1, name = v.blk.22.ln1.weight, tensor_size=4608, offset=902483328, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[382]: n_dims = 1, name = v.blk.22.ln1.bias, tensor_size=4608, offset=902487936, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[383]: n_dims = 2, name = v.blk.22.ffn_down.weight, tensor_size=9916416, offset=902492544, shape:[1152, 4304, 1, 1], type = f16
clip_model_loader: tensor[384]: n_dims = 1, name = v.blk.22.ffn_down.bias, tensor_size=17216, offset=912408960, shape:[4304, 1, 1, 1], type = f32
clip_model_loader: tensor[385]: n_dims = 2, name = v.blk.22.ffn_up.weight, tensor_size=9916416, offset=912426176, shape:[4304, 1152, 1, 1], type = f16
clip_model_loader: tensor[386]: n_dims = 1, name = v.blk.22.ffn_up.bias, tensor_size=4608, offset=922342592, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[387]: n_dims = 1, name = v.blk.22.ln2.weight, tensor_size=4608, offset=922347200, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[388]: n_dims = 1, name = v.blk.22.ln2.bias, tensor_size=4608, offset=922351808, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[389]: n_dims = 2, name = v.blk.23.attn_k.weight, tensor_size=2654208, offset=922356416, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[390]: n_dims = 1, name = v.blk.23.attn_k.bias, tensor_size=4608, offset=925010624, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[391]: n_dims = 2, name = v.blk.23.attn_v.weight, tensor_size=2654208, offset=925015232, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[392]: n_dims = 1, name = v.blk.23.attn_v.bias, tensor_size=4608, offset=927669440, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[393]: n_dims = 2, name = v.blk.23.attn_q.weight, tensor_size=2654208, offset=927674048, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[394]: n_dims = 1, name = v.blk.23.attn_q.bias, tensor_size=4608, offset=930328256, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[395]: n_dims = 2, name = v.blk.23.attn_out.weight, tensor_size=2654208, offset=930332864, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[396]: n_dims = 1, name = v.blk.23.attn_out.bias, tensor_size=4608, offset=932987072, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[397]: n_dims = 1, name = v.blk.23.ln1.weight, tensor_size=4608, offset=932991680, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[398]: n_dims = 1, name = v.blk.23.ln1.bias, tensor_size=4608, offset=932996288, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[399]: n_dims = 2, name = v.blk.23.ffn_down.weight, tensor_size=9916416, offset=933000896, shape:[1152, 4304, 1, 1], type = f16
clip_model_loader: tensor[400]: n_dims = 1, name = v.blk.23.ffn_down.bias, tensor_size=17216, offset=942917312, shape:[4304, 1, 1, 1], type = f32
clip_model_loader: tensor[401]: n_dims = 2, name = v.blk.23.ffn_up.weight, tensor_size=9916416, offset=942934528, shape:[4304, 1152, 1, 1], type = f16
clip_model_loader: tensor[402]: n_dims = 1, name = v.blk.23.ffn_up.bias, tensor_size=4608, offset=952850944, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[403]: n_dims = 1, name = v.blk.23.ln2.weight, tensor_size=4608, offset=952855552, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[404]: n_dims = 1, name = v.blk.23.ln2.bias, tensor_size=4608, offset=952860160, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[405]: n_dims = 2, name = v.blk.24.attn_k.weight, tensor_size=2654208, offset=952864768, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[406]: n_dims = 1, name = v.blk.24.attn_k.bias, tensor_size=4608, offset=955518976, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[407]: n_dims = 2, name = v.blk.24.attn_v.weight, tensor_size=2654208, offset=955523584, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[408]: n_dims = 1, name = v.blk.24.attn_v.bias, tensor_size=4608, offset=958177792, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[409]: n_dims = 2, name = v.blk.24.attn_q.weight, tensor_size=2654208, offset=958182400, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[410]: n_dims = 1, name = v.blk.24.attn_q.bias, tensor_size=4608, offset=960836608, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[411]: n_dims = 2, name = v.blk.24.attn_out.weight, tensor_size=2654208, offset=960841216, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[412]: n_dims = 1, name = v.blk.24.attn_out.bias, tensor_size=4608, offset=963495424, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[413]: n_dims = 1, name = v.blk.24.ln1.weight, tensor_size=4608, offset=963500032, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[414]: n_dims = 1, name = v.blk.24.ln1.bias, tensor_size=4608, offset=963504640, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[415]: n_dims = 2, name = v.blk.24.ffn_down.weight, tensor_size=9916416, offset=963509248, shape:[1152, 4304, 1, 1], type = f16
clip_model_loader: tensor[416]: n_dims = 1, name = v.blk.24.ffn_down.bias, tensor_size=17216, offset=973425664, shape:[4304, 1, 1, 1], type = f32
clip_model_loader: tensor[417]: n_dims = 2, name = v.blk.24.ffn_up.weight, tensor_size=9916416, offset=973442880, shape:[4304, 1152, 1, 1], type = f16
clip_model_loader: tensor[418]: n_dims = 1, name = v.blk.24.ffn_up.bias, tensor_size=4608, offset=983359296, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[419]: n_dims = 1, name = v.blk.24.ln2.weight, tensor_size=4608, offset=983363904, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[420]: n_dims = 1, name = v.blk.24.ln2.bias, tensor_size=4608, offset=983368512, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[421]: n_dims = 2, name = v.blk.25.attn_k.weight, tensor_size=2654208, offset=983373120, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[422]: n_dims = 1, name = v.blk.25.attn_k.bias, tensor_size=4608, offset=986027328, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[423]: n_dims = 2, name = v.blk.25.attn_v.weight, tensor_size=2654208, offset=986031936, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[424]: n_dims = 1, name = v.blk.25.attn_v.bias, tensor_size=4608, offset=988686144, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[425]: n_dims = 2, name = v.blk.25.attn_q.weight, tensor_size=2654208, offset=988690752, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[426]: n_dims = 1, name = v.blk.25.attn_q.bias, tensor_size=4608, offset=991344960, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[427]: n_dims = 2, name = v.blk.25.attn_out.weight, tensor_size=2654208, offset=991349568, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[428]: n_dims = 1, name = v.blk.25.attn_out.bias, tensor_size=4608, offset=994003776, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[429]: n_dims = 1, name = v.blk.25.ln1.weight, tensor_size=4608, offset=994008384, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[430]: n_dims = 1, name = v.blk.25.ln1.bias, tensor_size=4608, offset=994012992, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[431]: n_dims = 2, name = v.blk.25.ffn_down.weight, tensor_size=9916416, offset=994017600, shape:[1152, 4304, 1, 1], type = f16
clip_model_loader: tensor[432]: n_dims = 1, name = v.blk.25.ffn_down.bias, tensor_size=17216, offset=1003934016, shape:[4304, 1, 1, 1], type = f32
clip_model_loader: tensor[433]: n_dims = 2, name = v.blk.25.ffn_up.weight, tensor_size=9916416, offset=1003951232, shape:[4304, 1152, 1, 1], type = f16
clip_model_loader: tensor[434]: n_dims = 1, name = v.blk.25.ffn_up.bias, tensor_size=4608, offset=1013867648, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[435]: n_dims = 1, name = v.blk.25.ln2.weight, tensor_size=4608, offset=1013872256, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[436]: n_dims = 1, name = v.blk.25.ln2.bias, tensor_size=4608, offset=1013876864, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[437]: n_dims = 2, name = v.blk.26.attn_k.weight, tensor_size=2654208, offset=1013881472, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[438]: n_dims = 1, name = v.blk.26.attn_k.bias, tensor_size=4608, offset=1016535680, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[439]: n_dims = 2, name = v.blk.26.attn_v.weight, tensor_size=2654208, offset=1016540288, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[440]: n_dims = 1, name = v.blk.26.attn_v.bias, tensor_size=4608, offset=1019194496, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[441]: n_dims = 2, name = v.blk.26.attn_q.weight, tensor_size=2654208, offset=1019199104, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[442]: n_dims = 1, name = v.blk.26.attn_q.bias, tensor_size=4608, offset=1021853312, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[443]: n_dims = 2, name = v.blk.26.attn_out.weight, tensor_size=2654208, offset=1021857920, shape:[1152, 1152, 1, 1], type = f16
clip_model_loader: tensor[444]: n_dims = 1, name = v.blk.26.attn_out.bias, tensor_size=4608, offset=1024512128, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[445]: n_dims = 1, name = v.blk.26.ln1.weight, tensor_size=4608, offset=1024516736, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[446]: n_dims = 1, name = v.blk.26.ln1.bias, tensor_size=4608, offset=1024521344, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[447]: n_dims = 2, name = v.blk.26.ffn_down.weight, tensor_size=9916416, offset=1024525952, shape:[1152, 4304, 1, 1], type = f16
clip_model_loader: tensor[448]: n_dims = 1, name = v.blk.26.ffn_down.bias, tensor_size=17216, offset=1034442368, shape:[4304, 1, 1, 1], type = f32
clip_model_loader: tensor[449]: n_dims = 2, name = v.blk.26.ffn_up.weight, tensor_size=9916416, offset=1034459584, shape:[4304, 1152, 1, 1], type = f16
clip_model_loader: tensor[450]: n_dims = 1, name = v.blk.26.ffn_up.bias, tensor_size=4608, offset=1044376000, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[451]: n_dims = 1, name = v.blk.26.ln2.weight, tensor_size=4608, offset=1044380608, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[452]: n_dims = 1, name = v.blk.26.ln2.bias, tensor_size=4608, offset=1044385216, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[453]: n_dims = 1, name = v.post_ln.weight, tensor_size=4608, offset=1044389824, shape:[1152, 1, 1, 1], type = f32
clip_model_loader: tensor[454]: n_dims = 1, name = v.post_ln.bias, tensor_size=4608, offset=1044394432, shape:[1152, 1, 1, 1], type = f32
clip_ctx: CLIP using CPU backend
load_hparams: projector:          resampler
load_hparams: n_embd:             1152
load_hparams: n_head:             16
load_hparams: n_ff:               4304
load_hparams: n_layer:            26
load_hparams: ffn_op:             gelu
load_hparams: projection_dim:     0

--- vision hparams ---
load_hparams: image_size:         448
load_hparams: patch_size:         14
load_hparams: has_llava_proj:     0
load_hparams: minicpmv_version:   3
load_hparams: n_merge:            0
load_hparams: n_wa_pattern:       0

load_hparams: model size:         996.02 MiB
load_hparams: metadata size:      0.16 MiB
load_tensors: ffn up/down are swapped
load_tensors: loaded 439 tensors from /root/.ollama/models/blobs/sha256-f8a805e9e62085805c69c427287acefc284932eb4abfe6e1b1ce431d27e2f4e0
warmup: warmup with image size = 448 x 448
alloc_compute_meta:        CPU compute buffer size =    53.31 MiB
alloc_compute_meta: graph splits = 1, nodes = 862
warmup: flash attention is enabled
time=2026-03-27T00:48:57.984Z level=INFO source=server.go:1388 msg="llama runner started in 6.34 seconds"
time=2026-03-27T00:48:57.984Z level=INFO source=sched.go:566 msg="loaded runners" count=3
time=2026-03-27T00:48:57.984Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:48:57.984Z level=INFO source=server.go:1388 msg="llama runner started in 6.34 seconds"
llama_model_loader: loaded meta data with 19 key-value pairs and 483 tensors from /root/.ollama/models/blobs/sha256-28bfdfaeba9f51611c00ed322ba684ce6db076756dbc46643f98a8a748c5199e (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = starcoder2
llama_model_loader: - kv   1:                               general.name str              = starcoder2-3b
llama_model_loader: - kv   2:                     starcoder2.block_count u32              = 30
llama_model_loader: - kv   3:                  starcoder2.context_length u32              = 16384
llama_model_loader: - kv   4:                starcoder2.embedding_length u32              = 3072
llama_model_loader: - kv   5:             starcoder2.feed_forward_length u32              = 12288
llama_model_loader: - kv   6:            starcoder2.attention.head_count u32              = 24
llama_model_loader: - kv   7:         starcoder2.attention.head_count_kv u32              = 2
llama_model_loader: - kv   8:                  starcoder2.rope.freq_base f32              = 999999.437500
llama_model_loader: - kv   9:    starcoder2.attention.layer_norm_epsilon f32              = 0.000010
llama_model_loader: - kv  10:                          general.file_type u32              = 2
llama_model_loader: - kv  11:                       tokenizer.ggml.model str              = gpt2
llama_model_loader: - kv  12:                      tokenizer.ggml.tokens arr[str,49152]   = ["<|endoftext|>", "<fim_prefix>", "<f...
llama_model_loader: - kv  13:                  tokenizer.ggml.token_type arr[i32,49152]   = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, ...
llama_model_loader: - kv  14:                      tokenizer.ggml.merges arr[str,48872]   = ["Ġ Ġ", "ĠĠ ĠĠ", "ĠĠĠĠ ĠĠ...
llama_model_loader: - kv  15:                tokenizer.ggml.bos_token_id u32              = 0
llama_model_loader: - kv  16:                tokenizer.ggml.eos_token_id u32              = 0
llama_model_loader: - kv  17:            tokenizer.ggml.unknown_token_id u32              = 0
llama_model_loader: - kv  18:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:  302 tensors
llama_model_loader: - type q4_0:  181 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 1.59 GiB (4.51 BPW) 
load: missing or unrecognized pre-tokenizer type, using: 'default'
load: printing all EOG tokens:
load:   - 0 ('<|endoftext|>')
load:   - 4 ('<fim_pad>')
load: special tokens cache size = 38
load: token to piece cache size = 0.2828 MB
print_info: arch             = starcoder2
print_info: vocab_only       = 1
print_info: no_alloc         = 0
print_info: model type       = ?B
print_info: model params     = 3.03 B
print_info: general.name     = starcoder2-3b
print_info: vocab type       = BPE
print_info: n_vocab          = 49152
print_info: n_merges         = 48872
print_info: BOS token        = 0 '<|endoftext|>'
print_info: EOS token        = 0 '<|endoftext|>'
print_info: EOT token        = 0 '<|endoftext|>'
print_info: UNK token        = 0 '<|endoftext|>'
print_info: LF token         = 222 'Ċ'
print_info: FIM PRE token    = 1 '<fim_prefix>'
print_info: FIM SUF token    = 3 '<fim_suffix>'
print_info: FIM MID token    = 2 '<fim_middle>'
print_info: FIM PAD token    = 4 '<fim_pad>'
print_info: EOG token        = 0 '<|endoftext|>'
print_info: EOG token        = 4 '<fim_pad>'
print_info: max token length = 512
llama_model_load: vocab only - skipping tensors
time=2026-03-27T00:49:35.779Z level=INFO source=server.go:431 msg="starting runner" cmd="/usr/bin/ollama runner --model /root/.ollama/models/blobs/sha256-28bfdfaeba9f51611c00ed322ba684ce6db076756dbc46643f98a8a748c5199e --port 42385"
time=2026-03-27T00:49:35.779Z level=INFO source=sched.go:491 msg="system memory" total="24.0 GiB" free="17.3 GiB" free_swap="8.0 GiB"
time=2026-03-27T00:49:35.779Z level=INFO source=server.go:498 msg="loading model" "model layers"=31 requested=-1
time=2026-03-27T00:49:35.780Z level=INFO source=device.go:245 msg="model weights" device=CPU size="1.6 GiB"
time=2026-03-27T00:49:35.780Z level=INFO source=device.go:256 msg="kv cache" device=CPU size="120.0 MiB"
time=2026-03-27T00:49:35.780Z level=INFO source=device.go:272 msg="total memory" size="1.7 GiB"
time=2026-03-27T00:49:35.798Z level=INFO source=runner.go:965 msg="starting go runner"
load_backend: loaded CPU backend from /usr/lib/ollama/libggml-cpu-alderlake.so
time=2026-03-27T00:49:35.809Z level=INFO source=ggml.go:104 msg=system CPU.0.SSE3=1 CPU.0.SSSE3=1 CPU.0.AVX=1 CPU.0.AVX_VNNI=1 CPU.0.AVX2=1 CPU.0.F16C=1 CPU.0.FMA=1 CPU.0.BMI2=1 CPU.0.LLAMAFILE=1 CPU.1.LLAMAFILE=1 compiler=cgo(gcc)
time=2026-03-27T00:49:35.809Z level=INFO source=runner.go:1001 msg="Server listening on 127.0.0.1:42385"
time=2026-03-27T00:49:35.814Z level=INFO source=runner.go:895 msg=load request="{Operation:commit LoraPath:[] Parallel:1 BatchSize:512 FlashAttention:Auto KvSize:4096 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:49:35.814Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:49:35.815Z level=INFO source=server.go:1384 msg="waiting for server to become available" status="llm server loading model"
llama_model_loader: loaded meta data with 19 key-value pairs and 483 tensors from /root/.ollama/models/blobs/sha256-28bfdfaeba9f51611c00ed322ba684ce6db076756dbc46643f98a8a748c5199e (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = starcoder2
llama_model_loader: - kv   1:                               general.name str              = starcoder2-3b
llama_model_loader: - kv   2:                     starcoder2.block_count u32              = 30
llama_model_loader: - kv   3:                  starcoder2.context_length u32              = 16384
llama_model_loader: - kv   4:                starcoder2.embedding_length u32              = 3072
llama_model_loader: - kv   5:             starcoder2.feed_forward_length u32              = 12288
llama_model_loader: - kv   6:            starcoder2.attention.head_count u32              = 24
llama_model_loader: - kv   7:         starcoder2.attention.head_count_kv u32              = 2
llama_model_loader: - kv   8:                  starcoder2.rope.freq_base f32              = 999999.437500
llama_model_loader: - kv   9:    starcoder2.attention.layer_norm_epsilon f32              = 0.000010
llama_model_loader: - kv  10:                          general.file_type u32              = 2
llama_model_loader: - kv  11:                       tokenizer.ggml.model str              = gpt2
llama_model_loader: - kv  12:                      tokenizer.ggml.tokens arr[str,49152]   = ["<|endoftext|>", "<fim_prefix>", "<f...
llama_model_loader: - kv  13:                  tokenizer.ggml.token_type arr[i32,49152]   = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, ...
llama_model_loader: - kv  14:                      tokenizer.ggml.merges arr[str,48872]   = ["Ġ Ġ", "ĠĠ ĠĠ", "ĠĠĠĠ ĠĠ...
llama_model_loader: - kv  15:                tokenizer.ggml.bos_token_id u32              = 0
llama_model_loader: - kv  16:                tokenizer.ggml.eos_token_id u32              = 0
llama_model_loader: - kv  17:            tokenizer.ggml.unknown_token_id u32              = 0
llama_model_loader: - kv  18:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:  302 tensors
llama_model_loader: - type q4_0:  181 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 1.59 GiB (4.51 BPW) 
load: missing or unrecognized pre-tokenizer type, using: 'default'
load: printing all EOG tokens:
load:   - 0 ('<|endoftext|>')
load:   - 4 ('<fim_pad>')
load: special tokens cache size = 38
load: token to piece cache size = 0.2828 MB
print_info: arch             = starcoder2
print_info: vocab_only       = 0
print_info: no_alloc         = 0
print_info: n_ctx_train      = 16384
print_info: n_embd           = 3072
print_info: n_embd_inp       = 3072
print_info: n_layer          = 30
print_info: n_head           = 24
print_info: n_head_kv        = 2
print_info: n_rot            = 128
print_info: n_swa            = 0
print_info: is_swa_any       = 0
print_info: n_embd_head_k    = 128
print_info: n_embd_head_v    = 128
print_info: n_gqa            = 12
print_info: n_embd_k_gqa     = 256
print_info: n_embd_v_gqa     = 256
print_info: f_norm_eps       = 1.0e-05
print_info: f_norm_rms_eps   = 0.0e+00
print_info: f_clamp_kqv      = 0.0e+00
print_info: f_max_alibi_bias = 0.0e+00
print_info: f_logit_scale    = 0.0e+00
print_info: f_attn_scale     = 0.0e+00
print_info: n_ff             = 12288
print_info: n_expert         = 0
print_info: n_expert_used    = 0
print_info: n_expert_groups  = 0
print_info: n_group_used     = 0
print_info: causal attn      = 1
print_info: pooling type     = 0
print_info: rope type        = 2
print_info: rope scaling     = linear
print_info: freq_base_train  = 999999.4
print_info: freq_scale_train = 1
print_info: n_ctx_orig_yarn  = 16384
print_info: rope_yarn_log_mul= 0.0000
print_info: rope_finetuned   = unknown
print_info: model type       = 3B
print_info: model params     = 3.03 B
print_info: general.name     = starcoder2-3b
print_info: vocab type       = BPE
print_info: n_vocab          = 49152
print_info: n_merges         = 48872
print_info: BOS token        = 0 '<|endoftext|>'
print_info: EOS token        = 0 '<|endoftext|>'
print_info: EOT token        = 0 '<|endoftext|>'
print_info: UNK token        = 0 '<|endoftext|>'
print_info: LF token         = 222 'Ċ'
print_info: FIM PRE token    = 1 '<fim_prefix>'
print_info: FIM SUF token    = 3 '<fim_suffix>'
print_info: FIM MID token    = 2 '<fim_middle>'
print_info: FIM PAD token    = 4 '<fim_pad>'
print_info: EOG token        = 0 '<|endoftext|>'
print_info: EOG token        = 4 '<fim_pad>'
print_info: max token length = 512
load_tensors: loading model tensors, this can take a while... (mmap = false)
load_tensors:          CPU model buffer size =  1629.01 MiB
llama_context: constructing llama_context
llama_context: n_seq_max     = 1
llama_context: n_ctx         = 4096
llama_context: n_ctx_seq     = 4096
llama_context: n_batch       = 512
llama_context: n_ubatch      = 512
llama_context: causal_attn   = 1
llama_context: flash_attn    = auto
llama_context: kv_unified    = false
llama_context: freq_base     = 999999.4
llama_context: freq_scale    = 1
llama_context: n_ctx_seq (4096) < n_ctx_train (16384) -- the full capacity of the model will not be utilized
llama_context:        CPU  output buffer size =     0.20 MiB
llama_kv_cache:        CPU KV buffer size =   120.00 MiB
llama_kv_cache: size =  120.00 MiB (  4096 cells,  30 layers,  1/1 seqs), K (f16):   60.00 MiB, V (f16):   60.00 MiB
llama_context: Flash Attention was auto, set to enabled
llama_context:        CPU compute buffer size =   108.00 MiB
llama_context: graph nodes  = 1148
llama_context: graph splits = 1
time=2026-03-27T00:49:37.826Z level=INFO source=server.go:1388 msg="llama runner started in 2.05 seconds"
time=2026-03-27T00:49:37.826Z level=INFO source=sched.go:566 msg="loaded runners" count=3
time=2026-03-27T00:49:37.826Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:49:37.826Z level=INFO source=server.go:1388 msg="llama runner started in 2.05 seconds"
llama_model_loader: loaded meta data with 19 key-value pairs and 291 tensors from /root/.ollama/models/blobs/sha256-0577f52a4edfd5e48bb59c296bb4f40328161ecc3d0aa4398b3cb6b2b7367cac (version GGUF V2)
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = LLaMA v2
llama_model_loader: - kv   2:                       llama.context_length u32              = 4096
llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
llama_model_loader: - kv   4:                          llama.block_count u32              = 32
llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 11008
llama_model_loader: - kv   6:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv   7:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv   8:              llama.attention.head_count_kv u32              = 32
llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  10:                          general.file_type u32              = 2
llama_model_loader: - kv  11:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  12:                      tokenizer.ggml.tokens arr[str,32000]   = ["<unk>", "<s>", "</s>", "<0x00>", "<...
llama_model_loader: - kv  13:                      tokenizer.ggml.scores arr[f32,32000]   = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  14:                  tokenizer.ggml.token_type arr[i32,32000]   = [2, 3, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, ...
llama_model_loader: - kv  15:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  16:                tokenizer.ggml.eos_token_id u32              = 2
llama_model_loader: - kv  17:            tokenizer.ggml.padding_token_id u32              = 0
llama_model_loader: - kv  18:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   65 tensors
llama_model_loader: - type q4_0:  225 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V2
print_info: file type   = Q4_0
print_info: file size   = 3.56 GiB (4.54 BPW) 
load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
load: printing all EOG tokens:
load:   - 2 ('</s>')
load: special tokens cache size = 3
load: token to piece cache size = 0.1684 MB
print_info: arch             = llama
print_info: vocab_only       = 1
print_info: no_alloc         = 0
print_info: model type       = ?B
print_info: model params     = 6.74 B
print_info: general.name     = LLaMA v2
print_info: vocab type       = SPM
print_info: n_vocab          = 32000
print_info: n_merges         = 0
print_info: BOS token        = 1 '<s>'
print_info: EOS token        = 2 '</s>'
print_info: UNK token        = 0 '<unk>'
print_info: PAD token        = 0 '<unk>'
print_info: LF token         = 13 '<0x0A>'
print_info: EOG token        = 2 '</s>'
print_info: max token length = 48
llama_model_load: vocab only - skipping tensors
time=2026-03-27T00:49:56.045Z level=INFO source=server.go:431 msg="starting runner" cmd="/usr/bin/ollama runner --model /root/.ollama/models/blobs/sha256-0577f52a4edfd5e48bb59c296bb4f40328161ecc3d0aa4398b3cb6b2b7367cac --port 44073"
time=2026-03-27T00:49:56.045Z level=INFO source=sched.go:491 msg="system memory" total="24.0 GiB" free="15.7 GiB" free_swap="8.0 GiB"
time=2026-03-27T00:49:56.045Z level=INFO source=server.go:498 msg="loading model" "model layers"=33 requested=-1
time=2026-03-27T00:49:56.046Z level=INFO source=device.go:245 msg="model weights" device=CPU size="3.5 GiB"
time=2026-03-27T00:49:56.046Z level=INFO source=device.go:256 msg="kv cache" device=CPU size="2.0 GiB"
time=2026-03-27T00:49:56.046Z level=INFO source=device.go:272 msg="total memory" size="5.5 GiB"
time=2026-03-27T00:49:56.069Z level=INFO source=runner.go:965 msg="starting go runner"
load_backend: loaded CPU backend from /usr/lib/ollama/libggml-cpu-alderlake.so
time=2026-03-27T00:49:56.079Z level=INFO source=ggml.go:104 msg=system CPU.0.SSE3=1 CPU.0.SSSE3=1 CPU.0.AVX=1 CPU.0.AVX_VNNI=1 CPU.0.AVX2=1 CPU.0.F16C=1 CPU.0.FMA=1 CPU.0.BMI2=1 CPU.0.LLAMAFILE=1 CPU.1.LLAMAFILE=1 compiler=cgo(gcc)
time=2026-03-27T00:49:56.079Z level=INFO source=runner.go:1001 msg="Server listening on 127.0.0.1:44073"
time=2026-03-27T00:49:56.090Z level=INFO source=runner.go:895 msg=load request="{Operation:commit LoraPath:[] Parallel:1 BatchSize:512 FlashAttention:Auto KvSize:4096 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:49:56.090Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:49:56.091Z level=INFO source=server.go:1384 msg="waiting for server to become available" status="llm server loading model"
llama_model_loader: loaded meta data with 19 key-value pairs and 291 tensors from /root/.ollama/models/blobs/sha256-0577f52a4edfd5e48bb59c296bb4f40328161ecc3d0aa4398b3cb6b2b7367cac (version GGUF V2)
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = LLaMA v2
llama_model_loader: - kv   2:                       llama.context_length u32              = 4096
llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
llama_model_loader: - kv   4:                          llama.block_count u32              = 32
llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 11008
llama_model_loader: - kv   6:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv   7:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv   8:              llama.attention.head_count_kv u32              = 32
llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  10:                          general.file_type u32              = 2
llama_model_loader: - kv  11:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  12:                      tokenizer.ggml.tokens arr[str,32000]   = ["<unk>", "<s>", "</s>", "<0x00>", "<...
llama_model_loader: - kv  13:                      tokenizer.ggml.scores arr[f32,32000]   = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  14:                  tokenizer.ggml.token_type arr[i32,32000]   = [2, 3, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, ...
llama_model_loader: - kv  15:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  16:                tokenizer.ggml.eos_token_id u32              = 2
llama_model_loader: - kv  17:            tokenizer.ggml.padding_token_id u32              = 0
llama_model_loader: - kv  18:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   65 tensors
llama_model_loader: - type q4_0:  225 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V2
print_info: file type   = Q4_0
print_info: file size   = 3.56 GiB (4.54 BPW) 
load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
load: printing all EOG tokens:
load:   - 2 ('</s>')
load: special tokens cache size = 3
load: token to piece cache size = 0.1684 MB
print_info: arch             = llama
print_info: vocab_only       = 0
print_info: no_alloc         = 0
print_info: n_ctx_train      = 4096
print_info: n_embd           = 4096
print_info: n_embd_inp       = 4096
print_info: n_layer          = 32
print_info: n_head           = 32
print_info: n_head_kv        = 32
print_info: n_rot            = 128
print_info: n_swa            = 0
print_info: is_swa_any       = 0
print_info: n_embd_head_k    = 128
print_info: n_embd_head_v    = 128
print_info: n_gqa            = 1
print_info: n_embd_k_gqa     = 4096
print_info: n_embd_v_gqa     = 4096
print_info: f_norm_eps       = 0.0e+00
print_info: f_norm_rms_eps   = 1.0e-05
print_info: f_clamp_kqv      = 0.0e+00
print_info: f_max_alibi_bias = 0.0e+00
print_info: f_logit_scale    = 0.0e+00
print_info: f_attn_scale     = 0.0e+00
print_info: n_ff             = 11008
print_info: n_expert         = 0
print_info: n_expert_used    = 0
print_info: n_expert_groups  = 0
print_info: n_group_used     = 0
print_info: causal attn      = 1
print_info: pooling type     = 0
print_info: rope type        = 0
print_info: rope scaling     = linear
print_info: freq_base_train  = 10000.0
print_info: freq_scale_train = 1
print_info: n_ctx_orig_yarn  = 4096
print_info: rope_yarn_log_mul= 0.0000
print_info: rope_finetuned   = unknown
print_info: model type       = 7B
print_info: model params     = 6.74 B
print_info: general.name     = LLaMA v2
print_info: vocab type       = SPM
print_info: n_vocab          = 32000
print_info: n_merges         = 0
print_info: BOS token        = 1 '<s>'
print_info: EOS token        = 2 '</s>'
print_info: UNK token        = 0 '<unk>'
print_info: PAD token        = 0 '<unk>'
print_info: LF token         = 13 '<0x0A>'
print_info: EOG token        = 2 '</s>'
print_info: max token length = 48
load_tensors: loading model tensors, this can take a while... (mmap = false)
load_tensors:          CPU model buffer size =  3647.87 MiB
llama_context: constructing llama_context
llama_context: n_seq_max     = 1
llama_context: n_ctx         = 4096
llama_context: n_ctx_seq     = 4096
llama_context: n_batch       = 512
llama_context: n_ubatch      = 512
llama_context: causal_attn   = 1
llama_context: flash_attn    = auto
llama_context: kv_unified    = false
llama_context: freq_base     = 10000.0
llama_context: freq_scale    = 1
llama_context:        CPU  output buffer size =     0.14 MiB
llama_kv_cache:        CPU KV buffer size =  2048.00 MiB
llama_kv_cache: size = 2048.00 MiB (  4096 cells,  32 layers,  1/1 seqs), K (f16): 1024.00 MiB, V (f16): 1024.00 MiB
llama_context: Flash Attention was auto, set to enabled
llama_context:        CPU compute buffer size =    92.51 MiB
llama_context: graph nodes  = 999
llama_context: graph splits = 1
time=2026-03-27T00:50:01.116Z level=INFO source=server.go:1388 msg="llama runner started in 5.07 seconds"
time=2026-03-27T00:50:01.116Z level=INFO source=sched.go:566 msg="loaded runners" count=3
time=2026-03-27T00:50:01.116Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:50:01.117Z level=INFO source=server.go:1388 msg="llama runner started in 5.07 seconds"
llama_model_loader: loaded meta data with 22 key-value pairs and 291 tensors from /root/.ollama/models/blobs/sha256-6a0746a1ec1aef3e7ec53868f220ff6e389f6f8ef87a01d77c96807de94ca2aa (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = Meta-Llama-3-8B-Instruct
llama_model_loader: - kv   2:                          llama.block_count u32              = 32
llama_model_loader: - kv   3:                       llama.context_length u32              = 8192
llama_model_loader: - kv   4:                     llama.embedding_length u32              = 4096
llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 14336
llama_model_loader: - kv   6:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv   7:              llama.attention.head_count_kv u32              = 8
llama_model_loader: - kv   8:                       llama.rope.freq_base f32              = 500000.000000
llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  10:                          general.file_type u32              = 2
llama_model_loader: - kv  11:                           llama.vocab_size u32              = 128256
llama_model_loader: - kv  12:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv  13:                       tokenizer.ggml.model str              = gpt2
llama_model_loader: - kv  14:                         tokenizer.ggml.pre str              = llama-bpe
llama_model_loader: - kv  15:                      tokenizer.ggml.tokens arr[str,128256]  = ["!", "\"", "#", "$", "%", "&", "'", ...
llama_model_loader: - kv  16:                  tokenizer.ggml.token_type arr[i32,128256]  = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...
llama_model_loader: - kv  17:                      tokenizer.ggml.merges arr[str,280147]  = ["Ġ Ġ", "Ġ ĠĠĠ", "ĠĠ ĠĠ", "...
llama_model_loader: - kv  18:                tokenizer.ggml.bos_token_id u32              = 128000
llama_model_loader: - kv  19:                tokenizer.ggml.eos_token_id u32              = 128009
llama_model_loader: - kv  20:                    tokenizer.chat_template str              = {% set loop_messages = messages %}{% ...
llama_model_loader: - kv  21:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   65 tensors
llama_model_loader: - type q4_0:  225 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 4.33 GiB (4.64 BPW) 
load: printing all EOG tokens:
load:   - 128001 ('<|end_of_text|>')
load:   - 128009 ('<|eot_id|>')
load: special tokens cache size = 256
load: token to piece cache size = 0.8000 MB
print_info: arch             = llama
print_info: vocab_only       = 1
print_info: no_alloc         = 0
print_info: model type       = ?B
print_info: model params     = 8.03 B
print_info: general.name     = Meta-Llama-3-8B-Instruct
print_info: vocab type       = BPE
print_info: n_vocab          = 128256
print_info: n_merges         = 280147
print_info: BOS token        = 128000 '<|begin_of_text|>'
print_info: EOS token        = 128009 '<|eot_id|>'
print_info: EOT token        = 128009 '<|eot_id|>'
print_info: LF token         = 198 'Ċ'
print_info: EOG token        = 128001 '<|end_of_text|>'
print_info: EOG token        = 128009 '<|eot_id|>'
print_info: max token length = 256
llama_model_load: vocab only - skipping tensors
time=2026-03-27T00:50:15.908Z level=INFO source=server.go:431 msg="starting runner" cmd="/usr/bin/ollama runner --model /root/.ollama/models/blobs/sha256-6a0746a1ec1aef3e7ec53868f220ff6e389f6f8ef87a01d77c96807de94ca2aa --port 46799"
time=2026-03-27T00:50:15.909Z level=INFO source=sched.go:491 msg="system memory" total="24.0 GiB" free="17.6 GiB" free_swap="8.0 GiB"
time=2026-03-27T00:50:15.909Z level=INFO source=server.go:498 msg="loading model" "model layers"=33 requested=-1
time=2026-03-27T00:50:15.909Z level=INFO source=device.go:245 msg="model weights" device=CPU size="4.1 GiB"
time=2026-03-27T00:50:15.909Z level=INFO source=device.go:256 msg="kv cache" device=CPU size="512.0 MiB"
time=2026-03-27T00:50:15.909Z level=INFO source=device.go:272 msg="total memory" size="4.6 GiB"
time=2026-03-27T00:50:15.938Z level=INFO source=runner.go:965 msg="starting go runner"
load_backend: loaded CPU backend from /usr/lib/ollama/libggml-cpu-alderlake.so
time=2026-03-27T00:50:15.950Z level=INFO source=ggml.go:104 msg=system CPU.0.SSE3=1 CPU.0.SSSE3=1 CPU.0.AVX=1 CPU.0.AVX_VNNI=1 CPU.0.AVX2=1 CPU.0.F16C=1 CPU.0.FMA=1 CPU.0.BMI2=1 CPU.0.LLAMAFILE=1 CPU.1.LLAMAFILE=1 compiler=cgo(gcc)
time=2026-03-27T00:50:15.951Z level=INFO source=runner.go:1001 msg="Server listening on 127.0.0.1:46799"
time=2026-03-27T00:50:15.955Z level=INFO source=runner.go:895 msg=load request="{Operation:commit LoraPath:[] Parallel:1 BatchSize:512 FlashAttention:Auto KvSize:4096 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:50:15.955Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:50:15.956Z level=INFO source=server.go:1384 msg="waiting for server to become available" status="llm server loading model"
llama_model_loader: loaded meta data with 22 key-value pairs and 291 tensors from /root/.ollama/models/blobs/sha256-6a0746a1ec1aef3e7ec53868f220ff6e389f6f8ef87a01d77c96807de94ca2aa (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = Meta-Llama-3-8B-Instruct
llama_model_loader: - kv   2:                          llama.block_count u32              = 32
llama_model_loader: - kv   3:                       llama.context_length u32              = 8192
llama_model_loader: - kv   4:                     llama.embedding_length u32              = 4096
llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 14336
llama_model_loader: - kv   6:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv   7:              llama.attention.head_count_kv u32              = 8
llama_model_loader: - kv   8:                       llama.rope.freq_base f32              = 500000.000000
llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  10:                          general.file_type u32              = 2
llama_model_loader: - kv  11:                           llama.vocab_size u32              = 128256
llama_model_loader: - kv  12:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv  13:                       tokenizer.ggml.model str              = gpt2
llama_model_loader: - kv  14:                         tokenizer.ggml.pre str              = llama-bpe
llama_model_loader: - kv  15:                      tokenizer.ggml.tokens arr[str,128256]  = ["!", "\"", "#", "$", "%", "&", "'", ...
llama_model_loader: - kv  16:                  tokenizer.ggml.token_type arr[i32,128256]  = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...
llama_model_loader: - kv  17:                      tokenizer.ggml.merges arr[str,280147]  = ["Ġ Ġ", "Ġ ĠĠĠ", "ĠĠ ĠĠ", "...
llama_model_loader: - kv  18:                tokenizer.ggml.bos_token_id u32              = 128000
llama_model_loader: - kv  19:                tokenizer.ggml.eos_token_id u32              = 128009
llama_model_loader: - kv  20:                    tokenizer.chat_template str              = {% set loop_messages = messages %}{% ...
llama_model_loader: - kv  21:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   65 tensors
llama_model_loader: - type q4_0:  225 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 4.33 GiB (4.64 BPW) 
load: printing all EOG tokens:
load:   - 128001 ('<|end_of_text|>')
load:   - 128009 ('<|eot_id|>')
load: special tokens cache size = 256
load: token to piece cache size = 0.8000 MB
print_info: arch             = llama
print_info: vocab_only       = 0
print_info: no_alloc         = 0
print_info: n_ctx_train      = 8192
print_info: n_embd           = 4096
print_info: n_embd_inp       = 4096
print_info: n_layer          = 32
print_info: n_head           = 32
print_info: n_head_kv        = 8
print_info: n_rot            = 128
print_info: n_swa            = 0
print_info: is_swa_any       = 0
print_info: n_embd_head_k    = 128
print_info: n_embd_head_v    = 128
print_info: n_gqa            = 4
print_info: n_embd_k_gqa     = 1024
print_info: n_embd_v_gqa     = 1024
print_info: f_norm_eps       = 0.0e+00
print_info: f_norm_rms_eps   = 1.0e-05
print_info: f_clamp_kqv      = 0.0e+00
print_info: f_max_alibi_bias = 0.0e+00
print_info: f_logit_scale    = 0.0e+00
print_info: f_attn_scale     = 0.0e+00
print_info: n_ff             = 14336
print_info: n_expert         = 0
print_info: n_expert_used    = 0
print_info: n_expert_groups  = 0
print_info: n_group_used     = 0
print_info: causal attn      = 1
print_info: pooling type     = 0
print_info: rope type        = 0
print_info: rope scaling     = linear
print_info: freq_base_train  = 500000.0
print_info: freq_scale_train = 1
print_info: n_ctx_orig_yarn  = 8192
print_info: rope_yarn_log_mul= 0.0000
print_info: rope_finetuned   = unknown
print_info: model type       = 8B
print_info: model params     = 8.03 B
print_info: general.name     = Meta-Llama-3-8B-Instruct
print_info: vocab type       = BPE
print_info: n_vocab          = 128256
print_info: n_merges         = 280147
print_info: BOS token        = 128000 '<|begin_of_text|>'
print_info: EOS token        = 128009 '<|eot_id|>'
print_info: EOT token        = 128009 '<|eot_id|>'
print_info: LF token         = 198 'Ċ'
print_info: EOG token        = 128001 '<|end_of_text|>'
print_info: EOG token        = 128009 '<|eot_id|>'
print_info: max token length = 256
load_tensors: loading model tensors, this can take a while... (mmap = false)
load_tensors:          CPU model buffer size =  4437.80 MiB
llama_context: constructing llama_context
llama_context: n_seq_max     = 1
llama_context: n_ctx         = 4096
llama_context: n_ctx_seq     = 4096
llama_context: n_batch       = 512
llama_context: n_ubatch      = 512
llama_context: causal_attn   = 1
llama_context: flash_attn    = auto
llama_context: kv_unified    = false
llama_context: freq_base     = 500000.0
llama_context: freq_scale    = 1
llama_context: n_ctx_seq (4096) < n_ctx_train (8192) -- the full capacity of the model will not be utilized
llama_context:        CPU  output buffer size =     0.50 MiB
llama_kv_cache:        CPU KV buffer size =   512.00 MiB
llama_kv_cache: size =  512.00 MiB (  4096 cells,  32 layers,  1/1 seqs), K (f16):  256.00 MiB, V (f16):  256.00 MiB
llama_context: Flash Attention was auto, set to enabled
llama_context:        CPU compute buffer size =   258.50 MiB
llama_context: graph nodes  = 999
llama_context: graph splits = 1
time=2026-03-27T00:50:21.488Z level=INFO source=server.go:1388 msg="llama runner started in 5.58 seconds"
time=2026-03-27T00:50:21.488Z level=INFO source=sched.go:566 msg="loaded runners" count=3
time=2026-03-27T00:50:21.488Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:50:21.488Z level=INFO source=server.go:1388 msg="llama runner started in 5.58 seconds"
llama_model_loader: loaded meta data with 25 key-value pairs and 291 tensors from /root/.ollama/models/blobs/sha256-f5074b1221da0f5a2910d33b642efa5b9eb58cfdddca1c79e16d7ad28aa2b31f (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = Mistral-7B-Instruct-v0.3
llama_model_loader: - kv   2:                          llama.block_count u32              = 32
llama_model_loader: - kv   3:                       llama.context_length u32              = 32768
llama_model_loader: - kv   4:                     llama.embedding_length u32              = 4096
llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 14336
llama_model_loader: - kv   6:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv   7:              llama.attention.head_count_kv u32              = 8
llama_model_loader: - kv   8:                       llama.rope.freq_base f32              = 1000000.000000
llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  10:                          general.file_type u32              = 15
llama_model_loader: - kv  11:                           llama.vocab_size u32              = 32768
llama_model_loader: - kv  12:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv  13:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  14:                         tokenizer.ggml.pre str              = default
llama_model_loader: - kv  15:                      tokenizer.ggml.tokens arr[str,32768]   = ["<unk>", "<s>", "</s>", "[INST]", "[...
llama_model_loader: - kv  16:                      tokenizer.ggml.scores arr[f32,32768]   = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  17:                  tokenizer.ggml.token_type arr[i32,32768]   = [2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, ...
llama_model_loader: - kv  18:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  19:                tokenizer.ggml.eos_token_id u32              = 2
llama_model_loader: - kv  20:            tokenizer.ggml.unknown_token_id u32              = 0
llama_model_loader: - kv  21:               tokenizer.ggml.add_bos_token bool             = true
llama_model_loader: - kv  22:               tokenizer.ggml.add_eos_token bool             = false
llama_model_loader: - kv  23:                    tokenizer.chat_template str              = {{ bos_token }}{% for message in mess...
llama_model_loader: - kv  24:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   65 tensors
llama_model_loader: - type q4_K:  193 tensors
llama_model_loader: - type q6_K:   33 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_K - Medium
print_info: file size   = 4.07 GiB (4.83 BPW) 
load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
load: printing all EOG tokens:
load:   - 2 ('</s>')
load: special tokens cache size = 771
load: token to piece cache size = 0.1731 MB
print_info: arch             = llama
print_info: vocab_only       = 1
print_info: no_alloc         = 0
print_info: model type       = ?B
print_info: model params     = 7.25 B
print_info: general.name     = Mistral-7B-Instruct-v0.3
print_info: vocab type       = SPM
print_info: n_vocab          = 32768
print_info: n_merges         = 0
print_info: BOS token        = 1 '<s>'
print_info: EOS token        = 2 '</s>'
print_info: UNK token        = 0 '<unk>'
print_info: LF token         = 781 '<0x0A>'
print_info: EOG token        = 2 '</s>'
print_info: max token length = 48
llama_model_load: vocab only - skipping tensors
time=2026-03-27T00:51:02.815Z level=INFO source=server.go:431 msg="starting runner" cmd="/usr/bin/ollama runner --model /root/.ollama/models/blobs/sha256-f5074b1221da0f5a2910d33b642efa5b9eb58cfdddca1c79e16d7ad28aa2b31f --port 46703"
time=2026-03-27T00:51:02.816Z level=INFO source=sched.go:491 msg="system memory" total="24.0 GiB" free="17.0 GiB" free_swap="8.0 GiB"
time=2026-03-27T00:51:02.816Z level=INFO source=server.go:498 msg="loading model" "model layers"=33 requested=-1
time=2026-03-27T00:51:02.816Z level=INFO source=device.go:245 msg="model weights" device=CPU size="4.0 GiB"
time=2026-03-27T00:51:02.816Z level=INFO source=device.go:256 msg="kv cache" device=CPU size="512.0 MiB"
time=2026-03-27T00:51:02.816Z level=INFO source=device.go:272 msg="total memory" size="4.5 GiB"
time=2026-03-27T00:51:02.836Z level=INFO source=runner.go:965 msg="starting go runner"
load_backend: loaded CPU backend from /usr/lib/ollama/libggml-cpu-alderlake.so
time=2026-03-27T00:51:02.847Z level=INFO source=ggml.go:104 msg=system CPU.0.SSE3=1 CPU.0.SSSE3=1 CPU.0.AVX=1 CPU.0.AVX_VNNI=1 CPU.0.AVX2=1 CPU.0.F16C=1 CPU.0.FMA=1 CPU.0.BMI2=1 CPU.0.LLAMAFILE=1 CPU.1.LLAMAFILE=1 compiler=cgo(gcc)
time=2026-03-27T00:51:02.847Z level=INFO source=runner.go:1001 msg="Server listening on 127.0.0.1:46703"
time=2026-03-27T00:51:02.850Z level=INFO source=runner.go:895 msg=load request="{Operation:commit LoraPath:[] Parallel:1 BatchSize:512 FlashAttention:Auto KvSize:4096 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:51:02.850Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:51:02.850Z level=INFO source=server.go:1384 msg="waiting for server to become available" status="llm server loading model"
llama_model_loader: loaded meta data with 25 key-value pairs and 291 tensors from /root/.ollama/models/blobs/sha256-f5074b1221da0f5a2910d33b642efa5b9eb58cfdddca1c79e16d7ad28aa2b31f (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = Mistral-7B-Instruct-v0.3
llama_model_loader: - kv   2:                          llama.block_count u32              = 32
llama_model_loader: - kv   3:                       llama.context_length u32              = 32768
llama_model_loader: - kv   4:                     llama.embedding_length u32              = 4096
llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 14336
llama_model_loader: - kv   6:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv   7:              llama.attention.head_count_kv u32              = 8
llama_model_loader: - kv   8:                       llama.rope.freq_base f32              = 1000000.000000
llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  10:                          general.file_type u32              = 15
llama_model_loader: - kv  11:                           llama.vocab_size u32              = 32768
llama_model_loader: - kv  12:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv  13:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  14:                         tokenizer.ggml.pre str              = default
llama_model_loader: - kv  15:                      tokenizer.ggml.tokens arr[str,32768]   = ["<unk>", "<s>", "</s>", "[INST]", "[...
llama_model_loader: - kv  16:                      tokenizer.ggml.scores arr[f32,32768]   = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  17:                  tokenizer.ggml.token_type arr[i32,32768]   = [2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, ...
llama_model_loader: - kv  18:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  19:                tokenizer.ggml.eos_token_id u32              = 2
llama_model_loader: - kv  20:            tokenizer.ggml.unknown_token_id u32              = 0
llama_model_loader: - kv  21:               tokenizer.ggml.add_bos_token bool             = true
llama_model_loader: - kv  22:               tokenizer.ggml.add_eos_token bool             = false
llama_model_loader: - kv  23:                    tokenizer.chat_template str              = {{ bos_token }}{% for message in mess...
llama_model_loader: - kv  24:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   65 tensors
llama_model_loader: - type q4_K:  193 tensors
llama_model_loader: - type q6_K:   33 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_K - Medium
print_info: file size   = 4.07 GiB (4.83 BPW) 
load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
load: printing all EOG tokens:
load:   - 2 ('</s>')
load: special tokens cache size = 771
load: token to piece cache size = 0.1731 MB
print_info: arch             = llama
print_info: vocab_only       = 0
print_info: no_alloc         = 0
print_info: n_ctx_train      = 32768
print_info: n_embd           = 4096
print_info: n_embd_inp       = 4096
print_info: n_layer          = 32
print_info: n_head           = 32
print_info: n_head_kv        = 8
print_info: n_rot            = 128
print_info: n_swa            = 0
print_info: is_swa_any       = 0
print_info: n_embd_head_k    = 128
print_info: n_embd_head_v    = 128
print_info: n_gqa            = 4
print_info: n_embd_k_gqa     = 1024
print_info: n_embd_v_gqa     = 1024
print_info: f_norm_eps       = 0.0e+00
print_info: f_norm_rms_eps   = 1.0e-05
print_info: f_clamp_kqv      = 0.0e+00
print_info: f_max_alibi_bias = 0.0e+00
print_info: f_logit_scale    = 0.0e+00
print_info: f_attn_scale     = 0.0e+00
print_info: n_ff             = 14336
print_info: n_expert         = 0
print_info: n_expert_used    = 0
print_info: n_expert_groups  = 0
print_info: n_group_used     = 0
print_info: causal attn      = 1
print_info: pooling type     = 0
print_info: rope type        = 0
print_info: rope scaling     = linear
print_info: freq_base_train  = 1000000.0
print_info: freq_scale_train = 1
print_info: n_ctx_orig_yarn  = 32768
print_info: rope_yarn_log_mul= 0.0000
print_info: rope_finetuned   = unknown
print_info: model type       = 7B
print_info: model params     = 7.25 B
print_info: general.name     = Mistral-7B-Instruct-v0.3
print_info: vocab type       = SPM
print_info: n_vocab          = 32768
print_info: n_merges         = 0
print_info: BOS token        = 1 '<s>'
print_info: EOS token        = 2 '</s>'
print_info: UNK token        = 0 '<unk>'
print_info: LF token         = 781 '<0x0A>'
print_info: EOG token        = 2 '</s>'
print_info: max token length = 48
load_tensors: loading model tensors, this can take a while... (mmap = false)
load_tensors:          CPU model buffer size =  4169.52 MiB
llama_context: constructing llama_context
llama_context: n_seq_max     = 1
llama_context: n_ctx         = 4096
llama_context: n_ctx_seq     = 4096
llama_context: n_batch       = 512
llama_context: n_ubatch      = 512
llama_context: causal_attn   = 1
llama_context: flash_attn    = auto
llama_context: kv_unified    = false
llama_context: freq_base     = 1000000.0
llama_context: freq_scale    = 1
llama_context: n_ctx_seq (4096) < n_ctx_train (32768) -- the full capacity of the model will not be utilized
llama_context:        CPU  output buffer size =     0.14 MiB
llama_kv_cache:        CPU KV buffer size =   512.00 MiB
llama_kv_cache: size =  512.00 MiB (  4096 cells,  32 layers,  1/1 seqs), K (f16):  256.00 MiB, V (f16):  256.00 MiB
llama_context: Flash Attention was auto, set to enabled
llama_context:        CPU compute buffer size =   112.01 MiB
llama_context: graph nodes  = 999
llama_context: graph splits = 1
time=2026-03-27T00:51:07.877Z level=INFO source=server.go:1388 msg="llama runner started in 5.06 seconds"
time=2026-03-27T00:51:07.877Z level=INFO source=sched.go:566 msg="loaded runners" count=3
time=2026-03-27T00:51:07.877Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:51:07.878Z level=INFO source=server.go:1388 msg="llama runner started in 5.06 seconds"
llama_model_loader: loaded meta data with 21 key-value pairs and 339 tensors from /root/.ollama/models/blobs/sha256-43f7a214e5329f672bb05404cfba1913cbb70fdaa1a17497224e1925046b0ed5 (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = qwen2
llama_model_loader: - kv   1:                               general.name str              = Qwen2-7B-Instruct
llama_model_loader: - kv   2:                          qwen2.block_count u32              = 28
llama_model_loader: - kv   3:                       qwen2.context_length u32              = 32768
llama_model_loader: - kv   4:                     qwen2.embedding_length u32              = 3584
llama_model_loader: - kv   5:                  qwen2.feed_forward_length u32              = 18944
llama_model_loader: - kv   6:                 qwen2.attention.head_count u32              = 28
llama_model_loader: - kv   7:              qwen2.attention.head_count_kv u32              = 4
llama_model_loader: - kv   8:                       qwen2.rope.freq_base f32              = 1000000.000000
llama_model_loader: - kv   9:     qwen2.attention.layer_norm_rms_epsilon f32              = 0.000001
llama_model_loader: - kv  10:                          general.file_type u32              = 2
llama_model_loader: - kv  11:                       tokenizer.ggml.model str              = gpt2
llama_model_loader: - kv  12:                         tokenizer.ggml.pre str              = qwen2
llama_model_loader: - kv  13:                      tokenizer.ggml.tokens arr[str,152064]  = ["!", "\"", "#", "$", "%", "&", "'", ...
llama_model_loader: - kv  14:                  tokenizer.ggml.token_type arr[i32,152064]  = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...
llama_model_loader: - kv  15:                      tokenizer.ggml.merges arr[str,151387]  = ["Ġ Ġ", "ĠĠ ĠĠ", "i n", "Ġ t",...
llama_model_loader: - kv  16:                tokenizer.ggml.eos_token_id u32              = 151645
llama_model_loader: - kv  17:            tokenizer.ggml.padding_token_id u32              = 151643
llama_model_loader: - kv  18:                tokenizer.ggml.bos_token_id u32              = 151643
llama_model_loader: - kv  19:                    tokenizer.chat_template str              = {% for message in messages %}{% if lo...
llama_model_loader: - kv  20:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:  141 tensors
llama_model_loader: - type q4_0:  197 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 4.12 GiB (4.65 BPW) 
load: printing all EOG tokens:
load:   - 151643 ('<|endoftext|>')
load:   - 151645 ('<|im_end|>')
load: special tokens cache size = 421
load: token to piece cache size = 0.9352 MB
print_info: arch             = qwen2
print_info: vocab_only       = 1
print_info: no_alloc         = 0
print_info: model type       = ?B
print_info: model params     = 7.62 B
print_info: general.name     = Qwen2-7B-Instruct
print_info: vocab type       = BPE
print_info: n_vocab          = 152064
print_info: n_merges         = 151387
print_info: BOS token        = 151643 '<|endoftext|>'
print_info: EOS token        = 151645 '<|im_end|>'
print_info: EOT token        = 151645 '<|im_end|>'
print_info: PAD token        = 151643 '<|endoftext|>'
print_info: LF token         = 198 'Ċ'
print_info: EOG token        = 151643 '<|endoftext|>'
print_info: EOG token        = 151645 '<|im_end|>'
print_info: max token length = 256
llama_model_load: vocab only - skipping tensors
time=2026-03-27T00:51:45.748Z level=INFO source=server.go:431 msg="starting runner" cmd="/usr/bin/ollama runner --model /root/.ollama/models/blobs/sha256-43f7a214e5329f672bb05404cfba1913cbb70fdaa1a17497224e1925046b0ed5 --port 36823"
time=2026-03-27T00:51:45.749Z level=INFO source=sched.go:491 msg="system memory" total="24.0 GiB" free="12.7 GiB" free_swap="8.0 GiB"
time=2026-03-27T00:51:45.749Z level=INFO source=server.go:498 msg="loading model" "model layers"=29 requested=-1
time=2026-03-27T00:51:45.750Z level=INFO source=device.go:245 msg="model weights" device=CPU size="3.8 GiB"
time=2026-03-27T00:51:45.750Z level=INFO source=device.go:256 msg="kv cache" device=CPU size="224.0 MiB"
time=2026-03-27T00:51:45.750Z level=INFO source=device.go:272 msg="total memory" size="4.1 GiB"
time=2026-03-27T00:51:45.774Z level=INFO source=runner.go:965 msg="starting go runner"
load_backend: loaded CPU backend from /usr/lib/ollama/libggml-cpu-alderlake.so
time=2026-03-27T00:51:45.786Z level=INFO source=ggml.go:104 msg=system CPU.0.SSE3=1 CPU.0.SSSE3=1 CPU.0.AVX=1 CPU.0.AVX_VNNI=1 CPU.0.AVX2=1 CPU.0.F16C=1 CPU.0.FMA=1 CPU.0.BMI2=1 CPU.0.LLAMAFILE=1 CPU.1.LLAMAFILE=1 compiler=cgo(gcc)
time=2026-03-27T00:51:45.787Z level=INFO source=runner.go:1001 msg="Server listening on 127.0.0.1:36823"
time=2026-03-27T00:51:45.795Z level=INFO source=runner.go:895 msg=load request="{Operation:commit LoraPath:[] Parallel:1 BatchSize:512 FlashAttention:Auto KvSize:4096 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:51:45.795Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:51:45.796Z level=INFO source=server.go:1384 msg="waiting for server to become available" status="llm server loading model"
llama_model_loader: loaded meta data with 21 key-value pairs and 339 tensors from /root/.ollama/models/blobs/sha256-43f7a214e5329f672bb05404cfba1913cbb70fdaa1a17497224e1925046b0ed5 (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = qwen2
llama_model_loader: - kv   1:                               general.name str              = Qwen2-7B-Instruct
llama_model_loader: - kv   2:                          qwen2.block_count u32              = 28
llama_model_loader: - kv   3:                       qwen2.context_length u32              = 32768
llama_model_loader: - kv   4:                     qwen2.embedding_length u32              = 3584
llama_model_loader: - kv   5:                  qwen2.feed_forward_length u32              = 18944
llama_model_loader: - kv   6:                 qwen2.attention.head_count u32              = 28
llama_model_loader: - kv   7:              qwen2.attention.head_count_kv u32              = 4
llama_model_loader: - kv   8:                       qwen2.rope.freq_base f32              = 1000000.000000
llama_model_loader: - kv   9:     qwen2.attention.layer_norm_rms_epsilon f32              = 0.000001
llama_model_loader: - kv  10:                          general.file_type u32              = 2
llama_model_loader: - kv  11:                       tokenizer.ggml.model str              = gpt2
llama_model_loader: - kv  12:                         tokenizer.ggml.pre str              = qwen2
llama_model_loader: - kv  13:                      tokenizer.ggml.tokens arr[str,152064]  = ["!", "\"", "#", "$", "%", "&", "'", ...
llama_model_loader: - kv  14:                  tokenizer.ggml.token_type arr[i32,152064]  = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...
llama_model_loader: - kv  15:                      tokenizer.ggml.merges arr[str,151387]  = ["Ġ Ġ", "ĠĠ ĠĠ", "i n", "Ġ t",...
llama_model_loader: - kv  16:                tokenizer.ggml.eos_token_id u32              = 151645
llama_model_loader: - kv  17:            tokenizer.ggml.padding_token_id u32              = 151643
llama_model_loader: - kv  18:                tokenizer.ggml.bos_token_id u32              = 151643
llama_model_loader: - kv  19:                    tokenizer.chat_template str              = {% for message in messages %}{% if lo...
llama_model_loader: - kv  20:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:  141 tensors
llama_model_loader: - type q4_0:  197 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 4.12 GiB (4.65 BPW) 
load: printing all EOG tokens:
load:   - 151643 ('<|endoftext|>')
load:   - 151645 ('<|im_end|>')
load: special tokens cache size = 421
load: token to piece cache size = 0.9352 MB
print_info: arch             = qwen2
print_info: vocab_only       = 0
print_info: no_alloc         = 0
print_info: n_ctx_train      = 32768
print_info: n_embd           = 3584
print_info: n_embd_inp       = 3584
print_info: n_layer          = 28
print_info: n_head           = 28
print_info: n_head_kv        = 4
print_info: n_rot            = 128
print_info: n_swa            = 0
print_info: is_swa_any       = 0
print_info: n_embd_head_k    = 128
print_info: n_embd_head_v    = 128
print_info: n_gqa            = 7
print_info: n_embd_k_gqa     = 512
print_info: n_embd_v_gqa     = 512
print_info: f_norm_eps       = 0.0e+00
print_info: f_norm_rms_eps   = 1.0e-06
print_info: f_clamp_kqv      = 0.0e+00
print_info: f_max_alibi_bias = 0.0e+00
print_info: f_logit_scale    = 0.0e+00
print_info: f_attn_scale     = 0.0e+00
print_info: n_ff             = 18944
print_info: n_expert         = 0
print_info: n_expert_used    = 0
print_info: n_expert_groups  = 0
print_info: n_group_used     = 0
print_info: causal attn      = 1
print_info: pooling type     = -1
print_info: rope type        = 2
print_info: rope scaling     = linear
print_info: freq_base_train  = 1000000.0
print_info: freq_scale_train = 1
print_info: n_ctx_orig_yarn  = 32768
print_info: rope_yarn_log_mul= 0.0000
print_info: rope_finetuned   = unknown
print_info: model type       = 7B
print_info: model params     = 7.62 B
print_info: general.name     = Qwen2-7B-Instruct
print_info: vocab type       = BPE
print_info: n_vocab          = 152064
print_info: n_merges         = 151387
print_info: BOS token        = 151643 '<|endoftext|>'
print_info: EOS token        = 151645 '<|im_end|>'
print_info: EOT token        = 151645 '<|im_end|>'
print_info: PAD token        = 151643 '<|endoftext|>'
print_info: LF token         = 198 'Ċ'
print_info: EOG token        = 151643 '<|endoftext|>'
print_info: EOG token        = 151645 '<|im_end|>'
print_info: max token length = 256
load_tensors: loading model tensors, this can take a while... (mmap = false)
load_tensors:          CPU model buffer size =  4220.43 MiB
llama_context: constructing llama_context
llama_context: n_seq_max     = 1
llama_context: n_ctx         = 4096
llama_context: n_ctx_seq     = 4096
llama_context: n_batch       = 512
llama_context: n_ubatch      = 512
llama_context: causal_attn   = 1
llama_context: flash_attn    = auto
llama_context: kv_unified    = false
llama_context: freq_base     = 1000000.0
llama_context: freq_scale    = 1
llama_context: n_ctx_seq (4096) < n_ctx_train (32768) -- the full capacity of the model will not be utilized
llama_context:        CPU  output buffer size =     0.59 MiB
llama_kv_cache:        CPU KV buffer size =   224.00 MiB
llama_kv_cache: size =  224.00 MiB (  4096 cells,  28 layers,  1/1 seqs), K (f16):  112.00 MiB, V (f16):  112.00 MiB
llama_context: Flash Attention was auto, set to enabled
llama_context:        CPU compute buffer size =   304.00 MiB
llama_context: graph nodes  = 959
llama_context: graph splits = 1
time=2026-03-27T00:51:54.347Z level=INFO source=server.go:1388 msg="llama runner started in 8.60 seconds"
time=2026-03-27T00:51:54.354Z level=INFO source=sched.go:566 msg="loaded runners" count=3
time=2026-03-27T00:51:54.356Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:51:54.358Z level=INFO source=server.go:1388 msg="llama runner started in 8.61 seconds"
time=2026-03-27T00:52:34.049Z level=WARN source=types.go:976 msg="invalid option provided" option=rope_frequency_base
llama_model_loader: loaded meta data with 20 key-value pairs and 291 tensors from /root/.ollama/models/blobs/sha256-3a43f93b78ec50f7c4e4dc8bd1cb3fff5a900e7d574c51a6f7495e48486e0dac (version GGUF V2)
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = codellama
llama_model_loader: - kv   2:                       llama.context_length u32              = 16384
llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
llama_model_loader: - kv   4:                          llama.block_count u32              = 32
llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 11008
llama_model_loader: - kv   6:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv   7:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv   8:              llama.attention.head_count_kv u32              = 32
llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  10:                       llama.rope.freq_base f32              = 1000000.000000
llama_model_loader: - kv  11:                          general.file_type u32              = 2
llama_model_loader: - kv  12:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  13:                      tokenizer.ggml.tokens arr[str,32016]   = ["<unk>", "<s>", "</s>", "<0x00>", "<...
llama_model_loader: - kv  14:                      tokenizer.ggml.scores arr[f32,32016]   = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  15:                  tokenizer.ggml.token_type arr[i32,32016]   = [2, 3, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, ...
llama_model_loader: - kv  16:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  17:                tokenizer.ggml.eos_token_id u32              = 2
llama_model_loader: - kv  18:            tokenizer.ggml.unknown_token_id u32              = 0
llama_model_loader: - kv  19:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   65 tensors
llama_model_loader: - type q4_0:  225 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V2
print_info: file type   = Q4_0
print_info: file size   = 3.56 GiB (4.54 BPW) 
load: control-looking token:  32007 '▁<PRE>' was not control-type; this is probably a bug in the model. its type will be overridden
load: control-looking token:  32009 '▁<MID>' was not control-type; this is probably a bug in the model. its type will be overridden
load: control-looking token:  32008 '▁<SUF>' was not control-type; this is probably a bug in the model. its type will be overridden
load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
load: printing all EOG tokens:
load:   - 2 ('</s>')
load: special tokens cache size = 6
load: token to piece cache size = 0.1686 MB
print_info: arch             = llama
print_info: vocab_only       = 1
print_info: no_alloc         = 0
print_info: model type       = ?B
print_info: model params     = 6.74 B
print_info: general.name     = codellama
print_info: vocab type       = SPM
print_info: n_vocab          = 32016
print_info: n_merges         = 0
print_info: BOS token        = 1 '<s>'
print_info: EOS token        = 2 '</s>'
print_info: UNK token        = 0 '<unk>'
print_info: LF token         = 13 '<0x0A>'
print_info: FIM PRE token    = 32007 '▁<PRE>'
print_info: FIM SUF token    = 32008 '▁<SUF>'
print_info: FIM MID token    = 32009 '▁<MID>'
print_info: EOG token        = 2 '</s>'
print_info: max token length = 48
llama_model_load: vocab only - skipping tensors
time=2026-03-27T00:52:34.546Z level=INFO source=server.go:431 msg="starting runner" cmd="/usr/bin/ollama runner --model /root/.ollama/models/blobs/sha256-3a43f93b78ec50f7c4e4dc8bd1cb3fff5a900e7d574c51a6f7495e48486e0dac --port 35095"
time=2026-03-27T00:52:34.548Z level=INFO source=sched.go:491 msg="system memory" total="24.0 GiB" free="13.8 GiB" free_swap="6.3 GiB"
time=2026-03-27T00:52:34.548Z level=INFO source=server.go:498 msg="loading model" "model layers"=33 requested=-1
time=2026-03-27T00:52:34.548Z level=INFO source=device.go:245 msg="model weights" device=CPU size="3.5 GiB"
time=2026-03-27T00:52:34.548Z level=INFO source=device.go:256 msg="kv cache" device=CPU size="2.0 GiB"
time=2026-03-27T00:52:34.548Z level=INFO source=device.go:272 msg="total memory" size="5.5 GiB"
time=2026-03-27T00:52:34.589Z level=INFO source=runner.go:965 msg="starting go runner"
load_backend: loaded CPU backend from /usr/lib/ollama/libggml-cpu-alderlake.so
time=2026-03-27T00:52:34.602Z level=INFO source=ggml.go:104 msg=system CPU.0.SSE3=1 CPU.0.SSSE3=1 CPU.0.AVX=1 CPU.0.AVX_VNNI=1 CPU.0.AVX2=1 CPU.0.F16C=1 CPU.0.FMA=1 CPU.0.BMI2=1 CPU.0.LLAMAFILE=1 CPU.1.LLAMAFILE=1 compiler=cgo(gcc)
time=2026-03-27T00:52:34.603Z level=INFO source=runner.go:1001 msg="Server listening on 127.0.0.1:35095"
time=2026-03-27T00:52:34.604Z level=INFO source=runner.go:895 msg=load request="{Operation:commit LoraPath:[] Parallel:1 BatchSize:512 FlashAttention:Auto KvSize:4096 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:52:34.605Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:52:34.605Z level=INFO source=server.go:1384 msg="waiting for server to become available" status="llm server loading model"
llama_model_loader: loaded meta data with 20 key-value pairs and 291 tensors from /root/.ollama/models/blobs/sha256-3a43f93b78ec50f7c4e4dc8bd1cb3fff5a900e7d574c51a6f7495e48486e0dac (version GGUF V2)
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = codellama
llama_model_loader: - kv   2:                       llama.context_length u32              = 16384
llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
llama_model_loader: - kv   4:                          llama.block_count u32              = 32
llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 11008
llama_model_loader: - kv   6:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv   7:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv   8:              llama.attention.head_count_kv u32              = 32
llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  10:                       llama.rope.freq_base f32              = 1000000.000000
llama_model_loader: - kv  11:                          general.file_type u32              = 2
llama_model_loader: - kv  12:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  13:                      tokenizer.ggml.tokens arr[str,32016]   = ["<unk>", "<s>", "</s>", "<0x00>", "<...
llama_model_loader: - kv  14:                      tokenizer.ggml.scores arr[f32,32016]   = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  15:                  tokenizer.ggml.token_type arr[i32,32016]   = [2, 3, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, ...
llama_model_loader: - kv  16:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  17:                tokenizer.ggml.eos_token_id u32              = 2
llama_model_loader: - kv  18:            tokenizer.ggml.unknown_token_id u32              = 0
llama_model_loader: - kv  19:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   65 tensors
llama_model_loader: - type q4_0:  225 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V2
print_info: file type   = Q4_0
print_info: file size   = 3.56 GiB (4.54 BPW) 
load: control-looking token:  32007 '▁<PRE>' was not control-type; this is probably a bug in the model. its type will be overridden
load: control-looking token:  32009 '▁<MID>' was not control-type; this is probably a bug in the model. its type will be overridden
load: control-looking token:  32008 '▁<SUF>' was not control-type; this is probably a bug in the model. its type will be overridden
load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
load: printing all EOG tokens:
load:   - 2 ('</s>')
load: special tokens cache size = 6
load: token to piece cache size = 0.1686 MB
print_info: arch             = llama
print_info: vocab_only       = 0
print_info: no_alloc         = 0
print_info: n_ctx_train      = 16384
print_info: n_embd           = 4096
print_info: n_embd_inp       = 4096
print_info: n_layer          = 32
print_info: n_head           = 32
print_info: n_head_kv        = 32
print_info: n_rot            = 128
print_info: n_swa            = 0
print_info: is_swa_any       = 0
print_info: n_embd_head_k    = 128
print_info: n_embd_head_v    = 128
print_info: n_gqa            = 1
print_info: n_embd_k_gqa     = 4096
print_info: n_embd_v_gqa     = 4096
print_info: f_norm_eps       = 0.0e+00
print_info: f_norm_rms_eps   = 1.0e-05
print_info: f_clamp_kqv      = 0.0e+00
print_info: f_max_alibi_bias = 0.0e+00
print_info: f_logit_scale    = 0.0e+00
print_info: f_attn_scale     = 0.0e+00
print_info: n_ff             = 11008
print_info: n_expert         = 0
print_info: n_expert_used    = 0
print_info: n_expert_groups  = 0
print_info: n_group_used     = 0
print_info: causal attn      = 1
print_info: pooling type     = 0
print_info: rope type        = 0
print_info: rope scaling     = linear
print_info: freq_base_train  = 1000000.0
print_info: freq_scale_train = 1
print_info: n_ctx_orig_yarn  = 16384
print_info: rope_yarn_log_mul= 0.0000
print_info: rope_finetuned   = unknown
print_info: model type       = 7B
print_info: model params     = 6.74 B
print_info: general.name     = codellama
print_info: vocab type       = SPM
print_info: n_vocab          = 32016
print_info: n_merges         = 0
print_info: BOS token        = 1 '<s>'
print_info: EOS token        = 2 '</s>'
print_info: UNK token        = 0 '<unk>'
print_info: LF token         = 13 '<0x0A>'
print_info: FIM PRE token    = 32007 '▁<PRE>'
print_info: FIM SUF token    = 32008 '▁<SUF>'
print_info: FIM MID token    = 32009 '▁<MID>'
print_info: EOG token        = 2 '</s>'
print_info: max token length = 48
load_tensors: loading model tensors, this can take a while... (mmap = false)
load_tensors:          CPU model buffer size =  3647.95 MiB
llama_context: constructing llama_context
llama_context: n_seq_max     = 1
llama_context: n_ctx         = 4096
llama_context: n_ctx_seq     = 4096
llama_context: n_batch       = 512
llama_context: n_ubatch      = 512
llama_context: causal_attn   = 1
llama_context: flash_attn    = auto
llama_context: kv_unified    = false
llama_context: freq_base     = 1000000.0
llama_context: freq_scale    = 1
llama_context: n_ctx_seq (4096) < n_ctx_train (16384) -- the full capacity of the model will not be utilized
llama_context:        CPU  output buffer size =     0.14 MiB
llama_kv_cache:        CPU KV buffer size =  2048.00 MiB
llama_kv_cache: size = 2048.00 MiB (  4096 cells,  32 layers,  1/1 seqs), K (f16): 1024.00 MiB, V (f16): 1024.00 MiB
llama_context: Flash Attention was auto, set to enabled
llama_context:        CPU compute buffer size =    92.51 MiB
llama_context: graph nodes  = 999
llama_context: graph splits = 1
time=2026-03-27T00:52:41.905Z level=INFO source=server.go:1388 msg="llama runner started in 7.36 seconds"
time=2026-03-27T00:52:41.905Z level=INFO source=sched.go:566 msg="loaded runners" count=3
time=2026-03-27T00:52:41.906Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:52:41.906Z level=INFO source=server.go:1388 msg="llama runner started in 7.36 seconds"
time=2026-03-27T00:52:42.375Z level=WARN source=server.go:209 msg="flash attention enabled but not supported by model"
time=2026-03-27T00:52:42.375Z level=INFO source=server.go:431 msg="starting runner" cmd="/usr/bin/ollama runner --ollama-engine --model /root/.ollama/models/blobs/sha256-797b70c4edf85907fe0a49eb85811256f65fa0f7bf52166b147fd16be2be4662 --port 42629"
time=2026-03-27T00:52:42.376Z level=INFO source=sched.go:491 msg="system memory" total="24.0 GiB" free="13.0 GiB" free_swap="5.8 GiB"
time=2026-03-27T00:52:42.376Z level=INFO source=server.go:757 msg="loading model" "model layers"=7 requested=-1
time=2026-03-27T00:52:42.403Z level=INFO source=runner.go:1411 msg="starting ollama engine"
time=2026-03-27T00:52:42.403Z level=INFO source=runner.go:1446 msg="Server listening on 127.0.0.1:42629"
time=2026-03-27T00:52:42.410Z level=INFO source=runner.go:1284 msg=load request="{Operation:fit LoraPath:[] Parallel:1 BatchSize:256 FlashAttention:Disabled KvSize:256 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:52:42.422Z level=INFO source=ggml.go:136 msg="" architecture=bert file_type=F16 name=all-MiniLM-L6-v2 description="" num_tensors=101 num_key_values=24
load_backend: loaded CPU backend from /usr/lib/ollama/libggml-cpu-alderlake.so
time=2026-03-27T00:52:42.433Z level=INFO source=ggml.go:104 msg=system CPU.0.SSE3=1 CPU.0.SSSE3=1 CPU.0.AVX=1 CPU.0.AVX_VNNI=1 CPU.0.AVX2=1 CPU.0.F16C=1 CPU.0.FMA=1 CPU.0.BMI2=1 CPU.0.LLAMAFILE=1 CPU.1.LLAMAFILE=1 compiler=cgo(gcc)
time=2026-03-27T00:52:42.438Z level=INFO source=runner.go:1284 msg=load request="{Operation:alloc LoraPath:[] Parallel:1 BatchSize:256 FlashAttention:Disabled KvSize:256 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:52:42.454Z level=INFO source=runner.go:1284 msg=load request="{Operation:commit LoraPath:[] Parallel:1 BatchSize:256 FlashAttention:Disabled KvSize:256 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:52:42.455Z level=INFO source=device.go:245 msg="model weights" device=CPU size="65.5 MiB"
time=2026-03-27T00:52:42.455Z level=INFO source=ggml.go:482 msg="offloading 0 repeating layers to GPU"
time=2026-03-27T00:52:42.455Z level=INFO source=ggml.go:486 msg="offloading output layer to CPU"
time=2026-03-27T00:52:42.455Z level=INFO source=ggml.go:494 msg="offloaded 0/7 layers to GPU"
time=2026-03-27T00:52:42.455Z level=INFO source=device.go:267 msg="compute graph" device=CPU size="4.9 MiB"
time=2026-03-27T00:52:42.455Z level=INFO source=device.go:272 msg="total memory" size="70.3 MiB"
time=2026-03-27T00:52:42.455Z level=INFO source=sched.go:566 msg="loaded runners" count=3
time=2026-03-27T00:52:42.455Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:52:42.455Z level=INFO source=server.go:1384 msg="waiting for server to become available" status="llm server loading model"
time=2026-03-27T00:52:42.707Z level=INFO source=server.go:1388 msg="llama runner started in 0.33 seconds"
llama_model_loader: loaded meta data with 26 key-value pairs and 219 tensors from /root/.ollama/models/blobs/sha256-d040cc18521592f70c199396aeaa44cdc40224079156dc09d4283d745d9dc5fd (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = deepseek-ai
llama_model_loader: - kv   2:                       llama.context_length u32              = 16384
llama_model_loader: - kv   3:                     llama.embedding_length u32              = 2048
llama_model_loader: - kv   4:                          llama.block_count u32              = 24
llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 5504
llama_model_loader: - kv   6:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv   7:                 llama.attention.head_count u32              = 16
llama_model_loader: - kv   8:              llama.attention.head_count_kv u32              = 16
llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000001
llama_model_loader: - kv  10:                       llama.rope.freq_base f32              = 100000.000000
llama_model_loader: - kv  11:                    llama.rope.scaling.type str              = linear
llama_model_loader: - kv  12:                  llama.rope.scaling.factor f32              = 4.000000
llama_model_loader: - kv  13:                          general.file_type u32              = 2
llama_model_loader: - kv  14:                       tokenizer.ggml.model str              = gpt2
llama_model_loader: - kv  15:                      tokenizer.ggml.tokens arr[str,32256]   = ["!", "\"", "#", "$", "%", "&", "'", ...
llama_model_loader: - kv  16:                      tokenizer.ggml.scores arr[f32,32256]   = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  17:                  tokenizer.ggml.token_type arr[i32,32256]   = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...
llama_model_loader: - kv  18:                      tokenizer.ggml.merges arr[str,31757]   = ["Ġ Ġ", "Ġ t", "Ġ a", "i n", "h e...
llama_model_loader: - kv  19:                tokenizer.ggml.bos_token_id u32              = 32013
llama_model_loader: - kv  20:                tokenizer.ggml.eos_token_id u32              = 32021
llama_model_loader: - kv  21:            tokenizer.ggml.padding_token_id u32              = 32014
llama_model_loader: - kv  22:               tokenizer.ggml.add_bos_token bool             = true
llama_model_loader: - kv  23:               tokenizer.ggml.add_eos_token bool             = false
llama_model_loader: - kv  24:                    tokenizer.chat_template str              = {% if not add_generation_prompt is de...
llama_model_loader: - kv  25:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   49 tensors
llama_model_loader: - type q4_0:  169 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 738.88 MiB (4.60 BPW) 
load: missing or unrecognized pre-tokenizer type, using: 'default'
load: control-looking token:  32015 '<｜fim▁hole｜>' was not control-type; this is probably a bug in the model. its type will be overridden
load: control-looking token:  32017 '<｜fim▁end｜>' was not control-type; this is probably a bug in the model. its type will be overridden
load: control-looking token:  32016 '<｜fim▁begin｜>' was not control-type; this is probably a bug in the model. its type will be overridden
load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
load: special_eot_id is not in special_eog_ids - the tokenizer config may be incorrect
load: printing all EOG tokens:
load:   - 32014 ('<｜end▁of▁sentence｜>')
load:   - 32021 ('<|EOT|>')
load: special tokens cache size = 256
load: token to piece cache size = 0.1792 MB
print_info: arch             = llama
print_info: vocab_only       = 1
print_info: no_alloc         = 0
print_info: model type       = ?B
print_info: model params     = 1.35 B
print_info: general.name     = deepseek-ai
print_info: vocab type       = BPE
print_info: n_vocab          = 32256
print_info: n_merges         = 31757
print_info: BOS token        = 32013 '<｜begin▁of▁sentence｜>'
print_info: EOS token        = 32021 '<|EOT|>'
print_info: EOT token        = 32014 '<｜end▁of▁sentence｜>'
print_info: PAD token        = 32014 '<｜end▁of▁sentence｜>'
print_info: LF token         = 185 'Ċ'
print_info: FIM PRE token    = 32016 '<｜fim▁begin｜>'
print_info: FIM SUF token    = 32015 '<｜fim▁hole｜>'
print_info: FIM MID token    = 32017 '<｜fim▁end｜>'
print_info: EOG token        = 32014 '<｜end▁of▁sentence｜>'
print_info: EOG token        = 32021 '<|EOT|>'
print_info: max token length = 128
llama_model_load: vocab only - skipping tensors
time=2026-03-27T00:53:18.831Z level=INFO source=server.go:431 msg="starting runner" cmd="/usr/bin/ollama runner --model /root/.ollama/models/blobs/sha256-d040cc18521592f70c199396aeaa44cdc40224079156dc09d4283d745d9dc5fd --port 43771"
time=2026-03-27T00:53:18.832Z level=INFO source=sched.go:491 msg="system memory" total="24.0 GiB" free="18.5 GiB" free_swap="5.8 GiB"
time=2026-03-27T00:53:18.832Z level=INFO source=server.go:498 msg="loading model" "model layers"=25 requested=-1
time=2026-03-27T00:53:18.832Z level=INFO source=device.go:245 msg="model weights" device=CPU size="703.4 MiB"
time=2026-03-27T00:53:18.832Z level=INFO source=device.go:256 msg="kv cache" device=CPU size="768.0 MiB"
time=2026-03-27T00:53:18.832Z level=INFO source=device.go:272 msg="total memory" size="1.4 GiB"
time=2026-03-27T00:53:18.853Z level=INFO source=runner.go:965 msg="starting go runner"
load_backend: loaded CPU backend from /usr/lib/ollama/libggml-cpu-alderlake.so
time=2026-03-27T00:53:18.862Z level=INFO source=ggml.go:104 msg=system CPU.0.SSE3=1 CPU.0.SSSE3=1 CPU.0.AVX=1 CPU.0.AVX_VNNI=1 CPU.0.AVX2=1 CPU.0.F16C=1 CPU.0.FMA=1 CPU.0.BMI2=1 CPU.0.LLAMAFILE=1 CPU.1.LLAMAFILE=1 compiler=cgo(gcc)
time=2026-03-27T00:53:18.862Z level=INFO source=runner.go:1001 msg="Server listening on 127.0.0.1:43771"
time=2026-03-27T00:53:18.865Z level=INFO source=runner.go:895 msg=load request="{Operation:commit LoraPath:[] Parallel:1 BatchSize:512 FlashAttention:Auto KvSize:4096 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:53:18.865Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:53:18.866Z level=INFO source=server.go:1384 msg="waiting for server to become available" status="llm server loading model"
llama_model_loader: loaded meta data with 26 key-value pairs and 219 tensors from /root/.ollama/models/blobs/sha256-d040cc18521592f70c199396aeaa44cdc40224079156dc09d4283d745d9dc5fd (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = deepseek-ai
llama_model_loader: - kv   2:                       llama.context_length u32              = 16384
llama_model_loader: - kv   3:                     llama.embedding_length u32              = 2048
llama_model_loader: - kv   4:                          llama.block_count u32              = 24
llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 5504
llama_model_loader: - kv   6:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv   7:                 llama.attention.head_count u32              = 16
llama_model_loader: - kv   8:              llama.attention.head_count_kv u32              = 16
llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000001
llama_model_loader: - kv  10:                       llama.rope.freq_base f32              = 100000.000000
llama_model_loader: - kv  11:                    llama.rope.scaling.type str              = linear
llama_model_loader: - kv  12:                  llama.rope.scaling.factor f32              = 4.000000
llama_model_loader: - kv  13:                          general.file_type u32              = 2
llama_model_loader: - kv  14:                       tokenizer.ggml.model str              = gpt2
llama_model_loader: - kv  15:                      tokenizer.ggml.tokens arr[str,32256]   = ["!", "\"", "#", "$", "%", "&", "'", ...
llama_model_loader: - kv  16:                      tokenizer.ggml.scores arr[f32,32256]   = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  17:                  tokenizer.ggml.token_type arr[i32,32256]   = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...
llama_model_loader: - kv  18:                      tokenizer.ggml.merges arr[str,31757]   = ["Ġ Ġ", "Ġ t", "Ġ a", "i n", "h e...
llama_model_loader: - kv  19:                tokenizer.ggml.bos_token_id u32              = 32013
llama_model_loader: - kv  20:                tokenizer.ggml.eos_token_id u32              = 32021
llama_model_loader: - kv  21:            tokenizer.ggml.padding_token_id u32              = 32014
llama_model_loader: - kv  22:               tokenizer.ggml.add_bos_token bool             = true
llama_model_loader: - kv  23:               tokenizer.ggml.add_eos_token bool             = false
llama_model_loader: - kv  24:                    tokenizer.chat_template str              = {% if not add_generation_prompt is de...
llama_model_loader: - kv  25:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   49 tensors
llama_model_loader: - type q4_0:  169 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 738.88 MiB (4.60 BPW) 
load: missing or unrecognized pre-tokenizer type, using: 'default'
load: control-looking token:  32015 '<｜fim▁hole｜>' was not control-type; this is probably a bug in the model. its type will be overridden
load: control-looking token:  32017 '<｜fim▁end｜>' was not control-type; this is probably a bug in the model. its type will be overridden
load: control-looking token:  32016 '<｜fim▁begin｜>' was not control-type; this is probably a bug in the model. its type will be overridden
load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
load: special_eot_id is not in special_eog_ids - the tokenizer config may be incorrect
load: printing all EOG tokens:
load:   - 32014 ('<｜end▁of▁sentence｜>')
load:   - 32021 ('<|EOT|>')
load: special tokens cache size = 256
load: token to piece cache size = 0.1792 MB
print_info: arch             = llama
print_info: vocab_only       = 0
print_info: no_alloc         = 0
print_info: n_ctx_train      = 16384
print_info: n_embd           = 2048
print_info: n_embd_inp       = 2048
print_info: n_layer          = 24
print_info: n_head           = 16
print_info: n_head_kv        = 16
print_info: n_rot            = 128
print_info: n_swa            = 0
print_info: is_swa_any       = 0
print_info: n_embd_head_k    = 128
print_info: n_embd_head_v    = 128
print_info: n_gqa            = 1
print_info: n_embd_k_gqa     = 2048
print_info: n_embd_v_gqa     = 2048
print_info: f_norm_eps       = 0.0e+00
print_info: f_norm_rms_eps   = 1.0e-06
print_info: f_clamp_kqv      = 0.0e+00
print_info: f_max_alibi_bias = 0.0e+00
print_info: f_logit_scale    = 0.0e+00
print_info: f_attn_scale     = 0.0e+00
print_info: n_ff             = 5504
print_info: n_expert         = 0
print_info: n_expert_used    = 0
print_info: n_expert_groups  = 0
print_info: n_group_used     = 0
print_info: causal attn      = 1
print_info: pooling type     = 0
print_info: rope type        = 0
print_info: rope scaling     = linear
print_info: freq_base_train  = 100000.0
print_info: freq_scale_train = 0.25
print_info: n_ctx_orig_yarn  = 16384
print_info: rope_yarn_log_mul= 0.0000
print_info: rope_finetuned   = unknown
print_info: model type       = ?B
print_info: model params     = 1.35 B
print_info: general.name     = deepseek-ai
print_info: vocab type       = BPE
print_info: n_vocab          = 32256
print_info: n_merges         = 31757
print_info: BOS token        = 32013 '<｜begin▁of▁sentence｜>'
print_info: EOS token        = 32021 '<|EOT|>'
print_info: EOT token        = 32014 '<｜end▁of▁sentence｜>'
print_info: PAD token        = 32014 '<｜end▁of▁sentence｜>'
print_info: LF token         = 185 'Ċ'
print_info: FIM PRE token    = 32016 '<｜fim▁begin｜>'
print_info: FIM SUF token    = 32015 '<｜fim▁hole｜>'
print_info: FIM MID token    = 32017 '<｜fim▁end｜>'
print_info: EOG token        = 32014 '<｜end▁of▁sentence｜>'
print_info: EOG token        = 32021 '<|EOT|>'
print_info: max token length = 128
load_tensors: loading model tensors, this can take a while... (mmap = false)
load_tensors:          CPU model buffer size =   738.88 MiB
llama_context: constructing llama_context
llama_context: n_seq_max     = 1
llama_context: n_ctx         = 4096
llama_context: n_ctx_seq     = 4096
llama_context: n_batch       = 512
llama_context: n_ubatch      = 512
llama_context: causal_attn   = 1
llama_context: flash_attn    = auto
llama_context: kv_unified    = false
llama_context: freq_base     = 100000.0
llama_context: freq_scale    = 0.25
llama_context: n_ctx_seq (4096) < n_ctx_train (16384) -- the full capacity of the model will not be utilized
llama_context:        CPU  output buffer size =     0.13 MiB
llama_kv_cache:        CPU KV buffer size =   768.00 MiB
llama_kv_cache: size =  768.00 MiB (  4096 cells,  24 layers,  1/1 seqs), K (f16):  384.00 MiB, V (f16):  384.00 MiB
llama_context: Flash Attention was auto, set to enabled
llama_context:        CPU compute buffer size =    71.00 MiB
llama_context: graph nodes  = 751
llama_context: graph splits = 1
time=2026-03-27T00:53:20.625Z level=INFO source=server.go:1388 msg="llama runner started in 1.79 seconds"
time=2026-03-27T00:53:20.626Z level=INFO source=sched.go:566 msg="loaded runners" count=3
time=2026-03-27T00:53:20.626Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:53:20.626Z level=INFO source=server.go:1388 msg="llama runner started in 1.79 seconds"
llama_model_loader: loaded meta data with 23 key-value pairs and 291 tensors from /root/.ollama/models/blobs/sha256-8934d96d3f08982e95922b2b7a2c626a1fe873d7c3b06e8e56d7bc0a1fef9246 (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = LLaMA v2
llama_model_loader: - kv   2:                       llama.context_length u32              = 4096
llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
llama_model_loader: - kv   4:                          llama.block_count u32              = 32
llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 11008
llama_model_loader: - kv   6:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv   7:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv   8:              llama.attention.head_count_kv u32              = 32
llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  10:                          general.file_type u32              = 2
llama_model_loader: - kv  11:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  12:                      tokenizer.ggml.tokens arr[str,32000]   = ["<unk>", "<s>", "</s>", "<0x00>", "<...
llama_model_loader: - kv  13:                      tokenizer.ggml.scores arr[f32,32000]   = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  14:                  tokenizer.ggml.token_type arr[i32,32000]   = [2, 3, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, ...
llama_model_loader: - kv  15:                      tokenizer.ggml.merges arr[str,61249]   = ["▁ t", "e r", "i n", "▁ a", "e n...
llama_model_loader: - kv  16:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  17:                tokenizer.ggml.eos_token_id u32              = 2
llama_model_loader: - kv  18:            tokenizer.ggml.unknown_token_id u32              = 0
llama_model_loader: - kv  19:               tokenizer.ggml.add_bos_token bool             = true
llama_model_loader: - kv  20:               tokenizer.ggml.add_eos_token bool             = false
llama_model_loader: - kv  21:                    tokenizer.chat_template str              = {% if messages[0]['role'] == 'system'...
llama_model_loader: - kv  22:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   65 tensors
llama_model_loader: - type q4_0:  225 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 3.56 GiB (4.54 BPW) 
load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
load: printing all EOG tokens:
load:   - 2 ('</s>')
load: special tokens cache size = 3
load: token to piece cache size = 0.1684 MB
print_info: arch             = llama
print_info: vocab_only       = 1
print_info: no_alloc         = 0
print_info: model type       = ?B
print_info: model params     = 6.74 B
print_info: general.name     = LLaMA v2
print_info: vocab type       = SPM
print_info: n_vocab          = 32000
print_info: n_merges         = 0
print_info: BOS token        = 1 '<s>'
print_info: EOS token        = 2 '</s>'
print_info: UNK token        = 0 '<unk>'
print_info: LF token         = 13 '<0x0A>'
print_info: EOG token        = 2 '</s>'
print_info: max token length = 48
llama_model_load: vocab only - skipping tensors
time=2026-03-27T00:53:30.806Z level=INFO source=server.go:431 msg="starting runner" cmd="/usr/bin/ollama runner --model /root/.ollama/models/blobs/sha256-8934d96d3f08982e95922b2b7a2c626a1fe873d7c3b06e8e56d7bc0a1fef9246 --port 36579"
time=2026-03-27T00:53:30.807Z level=INFO source=sched.go:491 msg="system memory" total="24.0 GiB" free="16.4 GiB" free_swap="5.8 GiB"
time=2026-03-27T00:53:30.807Z level=INFO source=server.go:498 msg="loading model" "model layers"=33 requested=-1
time=2026-03-27T00:53:30.807Z level=INFO source=device.go:245 msg="model weights" device=CPU size="3.5 GiB"
time=2026-03-27T00:53:30.807Z level=INFO source=device.go:256 msg="kv cache" device=CPU size="2.0 GiB"
time=2026-03-27T00:53:30.807Z level=INFO source=device.go:272 msg="total memory" size="5.5 GiB"
time=2026-03-27T00:53:30.825Z level=INFO source=runner.go:965 msg="starting go runner"
load_backend: loaded CPU backend from /usr/lib/ollama/libggml-cpu-alderlake.so
time=2026-03-27T00:53:30.833Z level=INFO source=ggml.go:104 msg=system CPU.0.SSE3=1 CPU.0.SSSE3=1 CPU.0.AVX=1 CPU.0.AVX_VNNI=1 CPU.0.AVX2=1 CPU.0.F16C=1 CPU.0.FMA=1 CPU.0.BMI2=1 CPU.0.LLAMAFILE=1 CPU.1.LLAMAFILE=1 compiler=cgo(gcc)
time=2026-03-27T00:53:30.834Z level=INFO source=runner.go:1001 msg="Server listening on 127.0.0.1:36579"
time=2026-03-27T00:53:30.841Z level=INFO source=runner.go:895 msg=load request="{Operation:commit LoraPath:[] Parallel:1 BatchSize:512 FlashAttention:Auto KvSize:4096 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:53:30.842Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:53:30.842Z level=INFO source=server.go:1384 msg="waiting for server to become available" status="llm server loading model"
llama_model_loader: loaded meta data with 23 key-value pairs and 291 tensors from /root/.ollama/models/blobs/sha256-8934d96d3f08982e95922b2b7a2c626a1fe873d7c3b06e8e56d7bc0a1fef9246 (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = LLaMA v2
llama_model_loader: - kv   2:                       llama.context_length u32              = 4096
llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
llama_model_loader: - kv   4:                          llama.block_count u32              = 32
llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 11008
llama_model_loader: - kv   6:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv   7:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv   8:              llama.attention.head_count_kv u32              = 32
llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  10:                          general.file_type u32              = 2
llama_model_loader: - kv  11:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  12:                      tokenizer.ggml.tokens arr[str,32000]   = ["<unk>", "<s>", "</s>", "<0x00>", "<...
llama_model_loader: - kv  13:                      tokenizer.ggml.scores arr[f32,32000]   = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  14:                  tokenizer.ggml.token_type arr[i32,32000]   = [2, 3, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, ...
llama_model_loader: - kv  15:                      tokenizer.ggml.merges arr[str,61249]   = ["▁ t", "e r", "i n", "▁ a", "e n...
llama_model_loader: - kv  16:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  17:                tokenizer.ggml.eos_token_id u32              = 2
llama_model_loader: - kv  18:            tokenizer.ggml.unknown_token_id u32              = 0
llama_model_loader: - kv  19:               tokenizer.ggml.add_bos_token bool             = true
llama_model_loader: - kv  20:               tokenizer.ggml.add_eos_token bool             = false
llama_model_loader: - kv  21:                    tokenizer.chat_template str              = {% if messages[0]['role'] == 'system'...
llama_model_loader: - kv  22:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   65 tensors
llama_model_loader: - type q4_0:  225 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 3.56 GiB (4.54 BPW) 
load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
load: printing all EOG tokens:
load:   - 2 ('</s>')
load: special tokens cache size = 3
load: token to piece cache size = 0.1684 MB
print_info: arch             = llama
print_info: vocab_only       = 0
print_info: no_alloc         = 0
print_info: n_ctx_train      = 4096
print_info: n_embd           = 4096
print_info: n_embd_inp       = 4096
print_info: n_layer          = 32
print_info: n_head           = 32
print_info: n_head_kv        = 32
print_info: n_rot            = 128
print_info: n_swa            = 0
print_info: is_swa_any       = 0
print_info: n_embd_head_k    = 128
print_info: n_embd_head_v    = 128
print_info: n_gqa            = 1
print_info: n_embd_k_gqa     = 4096
print_info: n_embd_v_gqa     = 4096
print_info: f_norm_eps       = 0.0e+00
print_info: f_norm_rms_eps   = 1.0e-05
print_info: f_clamp_kqv      = 0.0e+00
print_info: f_max_alibi_bias = 0.0e+00
print_info: f_logit_scale    = 0.0e+00
print_info: f_attn_scale     = 0.0e+00
print_info: n_ff             = 11008
print_info: n_expert         = 0
print_info: n_expert_used    = 0
print_info: n_expert_groups  = 0
print_info: n_group_used     = 0
print_info: causal attn      = 1
print_info: pooling type     = 0
print_info: rope type        = 0
print_info: rope scaling     = linear
print_info: freq_base_train  = 10000.0
print_info: freq_scale_train = 1
print_info: n_ctx_orig_yarn  = 4096
print_info: rope_yarn_log_mul= 0.0000
print_info: rope_finetuned   = unknown
print_info: model type       = 7B
print_info: model params     = 6.74 B
print_info: general.name     = LLaMA v2
print_info: vocab type       = SPM
print_info: n_vocab          = 32000
print_info: n_merges         = 0
print_info: BOS token        = 1 '<s>'
print_info: EOS token        = 2 '</s>'
print_info: UNK token        = 0 '<unk>'
print_info: LF token         = 13 '<0x0A>'
print_info: EOG token        = 2 '</s>'
print_info: max token length = 48
load_tensors: loading model tensors, this can take a while... (mmap = false)
load_tensors:          CPU model buffer size =  3647.87 MiB
llama_context: constructing llama_context
llama_context: n_seq_max     = 1
llama_context: n_ctx         = 4096
llama_context: n_ctx_seq     = 4096
llama_context: n_batch       = 512
llama_context: n_ubatch      = 512
llama_context: causal_attn   = 1
llama_context: flash_attn    = auto
llama_context: kv_unified    = false
llama_context: freq_base     = 10000.0
llama_context: freq_scale    = 1
llama_context:        CPU  output buffer size =     0.14 MiB
llama_kv_cache:        CPU KV buffer size =  2048.00 MiB
llama_kv_cache: size = 2048.00 MiB (  4096 cells,  32 layers,  1/1 seqs), K (f16): 1024.00 MiB, V (f16): 1024.00 MiB
llama_context: Flash Attention was auto, set to enabled
llama_context:        CPU compute buffer size =    92.51 MiB
llama_context: graph nodes  = 999
llama_context: graph splits = 1
time=2026-03-27T00:53:37.379Z level=INFO source=server.go:1388 msg="llama runner started in 6.57 seconds"
time=2026-03-27T00:53:37.379Z level=INFO source=sched.go:566 msg="loaded runners" count=3
time=2026-03-27T00:53:37.379Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:53:37.380Z level=INFO source=server.go:1388 msg="llama runner started in 6.57 seconds"
time=2026-03-27T00:55:28.524Z level=WARN source=server.go:209 msg="flash attention enabled but not supported by model"
time=2026-03-27T00:55:28.525Z level=INFO source=server.go:431 msg="starting runner" cmd="/usr/bin/ollama runner --ollama-engine --model /root/.ollama/models/blobs/sha256-797b70c4edf85907fe0a49eb85811256f65fa0f7bf52166b147fd16be2be4662 --port 41589"
time=2026-03-27T00:55:28.525Z level=INFO source=sched.go:491 msg="system memory" total="24.0 GiB" free="14.8 GiB" free_swap="5.9 GiB"
time=2026-03-27T00:55:28.525Z level=INFO source=server.go:757 msg="loading model" "model layers"=7 requested=-1
time=2026-03-27T00:55:28.549Z level=INFO source=runner.go:1411 msg="starting ollama engine"
time=2026-03-27T00:55:28.550Z level=INFO source=runner.go:1446 msg="Server listening on 127.0.0.1:41589"
time=2026-03-27T00:55:28.560Z level=INFO source=runner.go:1284 msg=load request="{Operation:fit LoraPath:[] Parallel:1 BatchSize:256 FlashAttention:Disabled KvSize:256 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:55:28.574Z level=INFO source=ggml.go:136 msg="" architecture=bert file_type=F16 name=all-MiniLM-L6-v2 description="" num_tensors=101 num_key_values=24
load_backend: loaded CPU backend from /usr/lib/ollama/libggml-cpu-alderlake.so
time=2026-03-27T00:55:28.587Z level=INFO source=ggml.go:104 msg=system CPU.0.SSE3=1 CPU.0.SSSE3=1 CPU.0.AVX=1 CPU.0.AVX_VNNI=1 CPU.0.AVX2=1 CPU.0.F16C=1 CPU.0.FMA=1 CPU.0.BMI2=1 CPU.0.LLAMAFILE=1 CPU.1.LLAMAFILE=1 compiler=cgo(gcc)
time=2026-03-27T00:55:28.591Z level=INFO source=runner.go:1284 msg=load request="{Operation:alloc LoraPath:[] Parallel:1 BatchSize:256 FlashAttention:Disabled KvSize:256 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:55:28.607Z level=INFO source=runner.go:1284 msg=load request="{Operation:commit LoraPath:[] Parallel:1 BatchSize:256 FlashAttention:Disabled KvSize:256 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:55:28.607Z level=INFO source=ggml.go:482 msg="offloading 0 repeating layers to GPU"
time=2026-03-27T00:55:28.607Z level=INFO source=ggml.go:486 msg="offloading output layer to CPU"
time=2026-03-27T00:55:28.607Z level=INFO source=ggml.go:494 msg="offloaded 0/7 layers to GPU"
time=2026-03-27T00:55:28.607Z level=INFO source=device.go:245 msg="model weights" device=CPU size="65.5 MiB"
time=2026-03-27T00:55:28.607Z level=INFO source=device.go:267 msg="compute graph" device=CPU size="4.9 MiB"
time=2026-03-27T00:55:28.607Z level=INFO source=device.go:272 msg="total memory" size="70.3 MiB"
time=2026-03-27T00:55:28.607Z level=INFO source=sched.go:566 msg="loaded runners" count=3
time=2026-03-27T00:55:28.607Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:55:28.608Z level=INFO source=server.go:1384 msg="waiting for server to become available" status="llm server loading model"
time=2026-03-27T00:55:28.859Z level=INFO source=server.go:1388 msg="llama runner started in 0.33 seconds"
llama_model_loader: loaded meta data with 29 key-value pairs and 292 tensors from /root/.ollama/models/blobs/sha256-667b0c1932bc6ffc593ed1d03f895bf2dc8dc6df21db3042284a6f4416b06a29 (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.type str              = model
llama_model_loader: - kv   2:                               general.name str              = Meta Llama 3.1 8B Instruct
llama_model_loader: - kv   3:                           general.finetune str              = Instruct
llama_model_loader: - kv   4:                           general.basename str              = Meta-Llama-3.1
llama_model_loader: - kv   5:                         general.size_label str              = 8B
llama_model_loader: - kv   6:                            general.license str              = llama3.1
llama_model_loader: - kv   7:                               general.tags arr[str,6]       = ["facebook", "meta", "pytorch", "llam...
llama_model_loader: - kv   8:                          general.languages arr[str,8]       = ["en", "de", "fr", "it", "pt", "hi", ...
llama_model_loader: - kv   9:                          llama.block_count u32              = 32
llama_model_loader: - kv  10:                       llama.context_length u32              = 131072
llama_model_loader: - kv  11:                     llama.embedding_length u32              = 4096
llama_model_loader: - kv  12:                  llama.feed_forward_length u32              = 14336
llama_model_loader: - kv  13:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv  14:              llama.attention.head_count_kv u32              = 8
llama_model_loader: - kv  15:                       llama.rope.freq_base f32              = 500000.000000
llama_model_loader: - kv  16:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  17:                          general.file_type u32              = 15
llama_model_loader: - kv  18:                           llama.vocab_size u32              = 128256
llama_model_loader: - kv  19:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv  20:                       tokenizer.ggml.model str              = gpt2
llama_model_loader: - kv  21:                         tokenizer.ggml.pre str              = llama-bpe
llama_model_loader: - kv  22:                      tokenizer.ggml.tokens arr[str,128256]  = ["!", "\"", "#", "$", "%", "&", "'", ...
llama_model_loader: - kv  23:                  tokenizer.ggml.token_type arr[i32,128256]  = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...
llama_model_loader: - kv  24:                      tokenizer.ggml.merges arr[str,280147]  = ["Ġ Ġ", "Ġ ĠĠĠ", "ĠĠ ĠĠ", "...
llama_model_loader: - kv  25:                tokenizer.ggml.bos_token_id u32              = 128000
llama_model_loader: - kv  26:                tokenizer.ggml.eos_token_id u32              = 128009
llama_model_loader: - kv  27:                    tokenizer.chat_template str              = {{- bos_token }}\n{%- if custom_tools ...
llama_model_loader: - kv  28:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   66 tensors
llama_model_loader: - type q4_K:  193 tensors
llama_model_loader: - type q6_K:   33 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_K - Medium
print_info: file size   = 4.58 GiB (4.89 BPW) 
load: printing all EOG tokens:
load:   - 128001 ('<|end_of_text|>')
load:   - 128008 ('<|eom_id|>')
load:   - 128009 ('<|eot_id|>')
load: special tokens cache size = 256
load: token to piece cache size = 0.7999 MB
print_info: arch             = llama
print_info: vocab_only       = 1
print_info: no_alloc         = 0
print_info: model type       = ?B
print_info: model params     = 8.03 B
print_info: general.name     = Meta Llama 3.1 8B Instruct
print_info: vocab type       = BPE
print_info: n_vocab          = 128256
print_info: n_merges         = 280147
print_info: BOS token        = 128000 '<|begin_of_text|>'
print_info: EOS token        = 128009 '<|eot_id|>'
print_info: EOT token        = 128009 '<|eot_id|>'
print_info: EOM token        = 128008 '<|eom_id|>'
print_info: LF token         = 198 'Ċ'
print_info: EOG token        = 128001 '<|end_of_text|>'
print_info: EOG token        = 128008 '<|eom_id|>'
print_info: EOG token        = 128009 '<|eot_id|>'
print_info: max token length = 256
llama_model_load: vocab only - skipping tensors
time=2026-03-27T00:55:30.104Z level=INFO source=server.go:431 msg="starting runner" cmd="/usr/bin/ollama runner --model /root/.ollama/models/blobs/sha256-667b0c1932bc6ffc593ed1d03f895bf2dc8dc6df21db3042284a6f4416b06a29 --port 43711"
time=2026-03-27T00:55:30.105Z level=INFO source=sched.go:491 msg="system memory" total="24.0 GiB" free="14.7 GiB" free_swap="5.9 GiB"
time=2026-03-27T00:55:30.105Z level=INFO source=server.go:498 msg="loading model" "model layers"=33 requested=-1
time=2026-03-27T00:55:30.106Z level=INFO source=device.go:245 msg="model weights" device=CPU size="4.3 GiB"
time=2026-03-27T00:55:30.106Z level=INFO source=device.go:256 msg="kv cache" device=CPU size="512.0 MiB"
time=2026-03-27T00:55:30.106Z level=INFO source=device.go:272 msg="total memory" size="4.8 GiB"
time=2026-03-27T00:55:30.133Z level=INFO source=runner.go:965 msg="starting go runner"
load_backend: loaded CPU backend from /usr/lib/ollama/libggml-cpu-alderlake.so
time=2026-03-27T00:55:30.146Z level=INFO source=ggml.go:104 msg=system CPU.0.SSE3=1 CPU.0.SSSE3=1 CPU.0.AVX=1 CPU.0.AVX_VNNI=1 CPU.0.AVX2=1 CPU.0.F16C=1 CPU.0.FMA=1 CPU.0.BMI2=1 CPU.0.LLAMAFILE=1 CPU.1.LLAMAFILE=1 compiler=cgo(gcc)
time=2026-03-27T00:55:30.146Z level=INFO source=runner.go:1001 msg="Server listening on 127.0.0.1:43711"
time=2026-03-27T00:55:30.150Z level=INFO source=runner.go:895 msg=load request="{Operation:commit LoraPath:[] Parallel:1 BatchSize:512 FlashAttention:Auto KvSize:4096 KvCacheType: NumThreads:0 GPULayers:[] MultiUserCache:false ProjectorPath: MainGPU:0 UseMmap:false}"
time=2026-03-27T00:55:30.151Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:55:30.151Z level=INFO source=server.go:1384 msg="waiting for server to become available" status="llm server loading model"
llama_model_loader: loaded meta data with 29 key-value pairs and 292 tensors from /root/.ollama/models/blobs/sha256-667b0c1932bc6ffc593ed1d03f895bf2dc8dc6df21db3042284a6f4416b06a29 (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.type str              = model
llama_model_loader: - kv   2:                               general.name str              = Meta Llama 3.1 8B Instruct
llama_model_loader: - kv   3:                           general.finetune str              = Instruct
llama_model_loader: - kv   4:                           general.basename str              = Meta-Llama-3.1
llama_model_loader: - kv   5:                         general.size_label str              = 8B
llama_model_loader: - kv   6:                            general.license str              = llama3.1
llama_model_loader: - kv   7:                               general.tags arr[str,6]       = ["facebook", "meta", "pytorch", "llam...
llama_model_loader: - kv   8:                          general.languages arr[str,8]       = ["en", "de", "fr", "it", "pt", "hi", ...
llama_model_loader: - kv   9:                          llama.block_count u32              = 32
llama_model_loader: - kv  10:                       llama.context_length u32              = 131072
llama_model_loader: - kv  11:                     llama.embedding_length u32              = 4096
llama_model_loader: - kv  12:                  llama.feed_forward_length u32              = 14336
llama_model_loader: - kv  13:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv  14:              llama.attention.head_count_kv u32              = 8
llama_model_loader: - kv  15:                       llama.rope.freq_base f32              = 500000.000000
llama_model_loader: - kv  16:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  17:                          general.file_type u32              = 15
llama_model_loader: - kv  18:                           llama.vocab_size u32              = 128256
llama_model_loader: - kv  19:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv  20:                       tokenizer.ggml.model str              = gpt2
llama_model_loader: - kv  21:                         tokenizer.ggml.pre str              = llama-bpe
llama_model_loader: - kv  22:                      tokenizer.ggml.tokens arr[str,128256]  = ["!", "\"", "#", "$", "%", "&", "'", ...
llama_model_loader: - kv  23:                  tokenizer.ggml.token_type arr[i32,128256]  = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...
llama_model_loader: - kv  24:                      tokenizer.ggml.merges arr[str,280147]  = ["Ġ Ġ", "Ġ ĠĠĠ", "ĠĠ ĠĠ", "...
llama_model_loader: - kv  25:                tokenizer.ggml.bos_token_id u32              = 128000
llama_model_loader: - kv  26:                tokenizer.ggml.eos_token_id u32              = 128009
llama_model_loader: - kv  27:                    tokenizer.chat_template str              = {{- bos_token }}\n{%- if custom_tools ...
llama_model_loader: - kv  28:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   66 tensors
llama_model_loader: - type q4_K:  193 tensors
llama_model_loader: - type q6_K:   33 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_K - Medium
print_info: file size   = 4.58 GiB (4.89 BPW) 
load: printing all EOG tokens:
load:   - 128001 ('<|end_of_text|>')
load:   - 128008 ('<|eom_id|>')
load:   - 128009 ('<|eot_id|>')
load: special tokens cache size = 256
load: token to piece cache size = 0.7999 MB
print_info: arch             = llama
print_info: vocab_only       = 0
print_info: no_alloc         = 0
print_info: n_ctx_train      = 131072
print_info: n_embd           = 4096
print_info: n_embd_inp       = 4096
print_info: n_layer          = 32
print_info: n_head           = 32
print_info: n_head_kv        = 8
print_info: n_rot            = 128
print_info: n_swa            = 0
print_info: is_swa_any       = 0
print_info: n_embd_head_k    = 128
print_info: n_embd_head_v    = 128
print_info: n_gqa            = 4
print_info: n_embd_k_gqa     = 1024
print_info: n_embd_v_gqa     = 1024
print_info: f_norm_eps       = 0.0e+00
print_info: f_norm_rms_eps   = 1.0e-05
print_info: f_clamp_kqv      = 0.0e+00
print_info: f_max_alibi_bias = 0.0e+00
print_info: f_logit_scale    = 0.0e+00
print_info: f_attn_scale     = 0.0e+00
print_info: n_ff             = 14336
print_info: n_expert         = 0
print_info: n_expert_used    = 0
print_info: n_expert_groups  = 0
print_info: n_group_used     = 0
print_info: causal attn      = 1
print_info: pooling type     = 0
print_info: rope type        = 0
print_info: rope scaling     = linear
print_info: freq_base_train  = 500000.0
print_info: freq_scale_train = 1
print_info: n_ctx_orig_yarn  = 131072
print_info: rope_yarn_log_mul= 0.0000
print_info: rope_finetuned   = unknown
print_info: model type       = 8B
print_info: model params     = 8.03 B
print_info: general.name     = Meta Llama 3.1 8B Instruct
print_info: vocab type       = BPE
print_info: n_vocab          = 128256
print_info: n_merges         = 280147
print_info: BOS token        = 128000 '<|begin_of_text|>'
print_info: EOS token        = 128009 '<|eot_id|>'
print_info: EOT token        = 128009 '<|eot_id|>'
print_info: EOM token        = 128008 '<|eom_id|>'
print_info: LF token         = 198 'Ċ'
print_info: EOG token        = 128001 '<|end_of_text|>'
print_info: EOG token        = 128008 '<|eom_id|>'
print_info: EOG token        = 128009 '<|eot_id|>'
print_info: max token length = 256
load_tensors: loading model tensors, this can take a while... (mmap = false)
load_tensors:          CPU model buffer size =  4685.30 MiB
llama_context: constructing llama_context
llama_context: n_seq_max     = 1
llama_context: n_ctx         = 4096
llama_context: n_ctx_seq     = 4096
llama_context: n_batch       = 512
llama_context: n_ubatch      = 512
llama_context: causal_attn   = 1
llama_context: flash_attn    = auto
llama_context: kv_unified    = false
llama_context: freq_base     = 500000.0
llama_context: freq_scale    = 1
llama_context: n_ctx_seq (4096) < n_ctx_train (131072) -- the full capacity of the model will not be utilized
llama_context:        CPU  output buffer size =     0.50 MiB
llama_kv_cache:        CPU KV buffer size =   512.00 MiB
llama_kv_cache: size =  512.00 MiB (  4096 cells,  32 layers,  1/1 seqs), K (f16):  256.00 MiB, V (f16):  256.00 MiB
llama_context: Flash Attention was auto, set to enabled
llama_context:        CPU compute buffer size =   258.50 MiB
llama_context: graph nodes  = 999
llama_context: graph splits = 1
time=2026-03-27T00:55:38.191Z level=INFO source=server.go:1388 msg="llama runner started in 8.09 seconds"
time=2026-03-27T00:55:38.191Z level=INFO source=sched.go:566 msg="loaded runners" count=3
time=2026-03-27T00:55:38.191Z level=INFO source=server.go:1350 msg="waiting for llama runner to start responding"
time=2026-03-27T00:55:38.192Z level=INFO source=server.go:1388 msg="llama runner started in 8.09 seconds"
[GIN] 2026/03/27 - 00:44:47 | 200 |    40.14716ms |     172.18.0.85 | POST     "/api/embeddings"
[GIN] 2026/03/27 - 00:45:27 | 200 | 50.517223952s |     172.18.0.92 | POST     "/api/generate"
[GIN] 2026/03/27 - 00:46:14 | 200 | 47.332022913s |     172.18.0.44 | POST     "/api/generate"
[GIN] 2026/03/27 - 00:46:58 | 200 | 43.659393972s |     172.18.0.26 | POST     "/api/generate"
[GIN] 2026/03/27 - 00:47:12 | 200 | 13.761122126s |     172.18.0.58 | POST     "/api/generate"
[GIN] 2026/03/27 - 00:47:38 | 200 |  861.046237ms |     172.18.0.85 | POST     "/api/embeddings"
[GIN] 2026/03/27 - 00:47:59 | 200 | 47.365980396s |     172.18.0.57 | POST     "/api/generate"
[GIN] 2026/03/27 - 00:48:50 | 200 | 50.014256871s |     172.18.0.32 | POST     "/api/generate"
[GIN] 2026/03/27 - 00:49:35 | 200 | 44.894987798s |     172.18.0.43 | POST     "/api/generate"
[GIN] 2026/03/27 - 00:49:55 | 200 | 20.523233198s |     172.18.0.42 | POST     "/api/generate"
[GIN] 2026/03/27 - 00:50:14 | 200 | 18.303518103s |      172.18.0.7 | POST     "/api/generate"
[GIN] 2026/03/27 - 00:51:02 | 200 | 47.974440403s |     172.18.0.48 | POST     "/api/generate"
[GIN] 2026/03/27 - 00:51:44 | 200 | 42.359385274s |     172.18.0.20 | POST     "/api/generate"
[GIN] 2026/03/27 - 00:52:33 | 200 | 49.184686136s |     172.18.0.41 | POST     "/api/generate"
[GIN] 2026/03/27 - 00:52:42 | 200 |  3.624272513s |     172.18.0.85 | POST     "/api/embeddings"
[GIN] 2026/03/27 - 00:53:18 | 200 | 44.091613548s |     172.18.0.30 | POST     "/api/generate"
[GIN] 2026/03/27 - 00:53:30 | 200 | 12.193421656s |      172.18.0.4 | POST     "/api/generate"
[GIN] 2026/03/27 - 00:54:16 | 200 | 45.755147716s |     172.18.0.70 | POST     "/api/generate"
[GIN] 2026/03/27 - 00:55:28 | 200 |  930.618291ms |     172.18.0.85 | POST     "/api/embeddings"
[GIN] 2026/03/27 - 00:56:28 | 500 |          1m0s |     172.18.0.52 | POST     "/api/chat"
INFO:__main__:🧠 Production Brain: 22 models loaded
INFO:__main__:   • TinyLlama -> model=tinyllama:latest endpoint=http://llm1-proxy:8201/generate weight=0.7 specialty=Quick responses active=True
INFO:__main__:   • Gemma -> model=gemma:2b endpoint=http://llm2-proxy:8202/generate weight=0.8 specialty=Synthesis active=True
INFO:__main__:   • Phi3 Mini -> model=phi3:mini endpoint=http://llm10-proxy:8210/generate weight=0.85 specialty=Fast reasoning active=True
INFO:__main__:   • Orca-Mini -> model=orca-mini:latest endpoint=http://llm13-proxy:8213/generate weight=0.8 specialty=Reasoning active=True
INFO:__main__:   • Dolphin-Phi -> model=dolphin-phi:latest endpoint=http://llm12-proxy:8212/generate weight=0.8 specialty=Dialogue active=True
INFO:__main__:   • Neural-Chat -> model=neural-chat:latest endpoint=http://llm17-proxy:8217/generate weight=0.85 specialty=Conversation active=True
INFO:__main__:   • OpenChat -> model=openchat:latest endpoint=http://llm18-proxy:8218/generate weight=0.85 specialty=Dialogue active=True
INFO:__main__:   • Zephyr -> model=zephyr:latest endpoint=http://llm15-proxy:8215/generate weight=0.85 specialty=Helpful responses active=True
INFO:__main__:   • Starling-LM -> model=starling-lm:latest endpoint=http://llm16-proxy:8216/generate weight=0.85 specialty=Communication active=True
INFO:__main__:   • SQLCoder -> model=sqlcoder:latest endpoint=http://llm6-proxy:8206/generate weight=0.75 specialty=SQL active=True
INFO:__main__:   • MedLlama2 -> model=medllama2:latest endpoint=http://llm3-proxy:8203/generate weight=0.75 specialty=Medical knowledge active=True
INFO:__main__:   • LLaVA -> model=llava:latest endpoint=http://llm5-proxy:8205/generate weight=0.8 specialty=Vision understanding active=True
INFO:__main__:   • MiniCPM-V -> model=minicpm-v:latest endpoint=http://llm4-proxy:8204/generate weight=0.8 specialty=Vision-language reasoning active=True
INFO:__main__:   • BakLLaVA -> model=bakllava:latest endpoint=http://llmXX-bakllava-disabled/generate weight=0.8 specialty=Visual reasoning active=False
INFO:__main__:   • StarCoder2 -> model=starcoder2:latest endpoint=http://llm7-proxy:8207/generate weight=0.85 specialty=Code analysis active=True
INFO:__main__:   • Vicuna -> model=vicuna:latest endpoint=http://llm19-proxy:8219/generate weight=0.85 specialty=Instruction following active=True
INFO:__main__:   • LLaMA 3.1 -> model=llama3:latest endpoint=http://llm22-proxy:8222/generate weight=1.0 specialty=General reasoning active=True
INFO:__main__:   • Mistral -> model=mistral:latest endpoint=http://llm21-proxy:8221/generate weight=0.95 specialty=Logic and reasoning active=True
INFO:__main__:   • Qwen2 -> model=qwen2:latest endpoint=http://llm14-proxy:8214/generate weight=0.9 specialty=Multilingual understanding active=True
INFO:__main__:   • CodeLlama -> model=codellama:latest endpoint=http://llm8-proxy:8208/generate weight=0.9 specialty=Code understanding active=True
INFO:__main__:   • DeepSeek Coder -> model=deepseek-coder:latest endpoint=http://llm9-proxy:8209/generate weight=0.9 specialty=Code generation active=True
INFO:__main__:   • LLaMA 2 -> model=llama2:latest endpoint=http://llm20-proxy:8220/generate weight=0.9 specialty=General reasoning active=True
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8008 (Press CTRL+C to quit)
INFO:__main__:💬 Contextual query: MountainShares smart contract security best practi...
INFO:__main__:🌟 Processing 21 models sequentially via proxies...
INFO:__main__:   [1/21] Processing TinyLlama...
INFO:httpx:HTTP Request: POST http://llm1-proxy:8201/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ TinyLlama: 626 chars via http://llm1-proxy:8201/generate
INFO:__main__:   [2/21] Processing Gemma...
INFO:httpx:HTTP Request: POST http://llm2-proxy:8202/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ Gemma: 738 chars via http://llm2-proxy:8202/generate
INFO:__main__:   [3/21] Processing Phi3 Mini...
INFO:httpx:HTTP Request: POST http://llm10-proxy:8210/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ Phi3 Mini: 578 chars via http://llm10-proxy:8210/generate
INFO:__main__:   [4/21] Processing Orca-Mini...
INFO:httpx:HTTP Request: POST http://llm13-proxy:8213/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ Orca-Mini: 569 chars via http://llm13-proxy:8213/generate
INFO:__main__:   [5/21] Processing Dolphin-Phi...
INFO:httpx:HTTP Request: POST http://llm12-proxy:8212/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ Dolphin-Phi: 621 chars via http://llm12-proxy:8212/generate
INFO:__main__:   [6/21] Processing Neural-Chat...
INFO:httpx:HTTP Request: POST http://llm17-proxy:8217/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ Neural-Chat: 630 chars via http://llm17-proxy:8217/generate
INFO:__main__:   [7/21] Processing OpenChat...
INFO:httpx:HTTP Request: POST http://llm18-proxy:8218/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ OpenChat: 701 chars via http://llm18-proxy:8218/generate
INFO:__main__:   [8/21] Processing Zephyr...
INFO:httpx:HTTP Request: POST http://llm15-proxy:8215/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ Zephyr: 691 chars via http://llm15-proxy:8215/generate
INFO:__main__:   [9/21] Processing Starling-LM...
INFO:httpx:HTTP Request: POST http://llm16-proxy:8216/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ Starling-LM: 631 chars via http://llm16-proxy:8216/generate
INFO:__main__:   [10/21] Processing SQLCoder...
INFO:httpx:HTTP Request: POST http://llm6-proxy:8206/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ SQLCoder: 8 chars via http://llm6-proxy:8206/generate
INFO:__main__:   [11/21] Processing MedLlama2...
INFO:httpx:HTTP Request: POST http://llm3-proxy:8203/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ MedLlama2: 667 chars via http://llm3-proxy:8203/generate
INFO:__main__:   [12/21] Processing LLaVA...
INFO:httpx:HTTP Request: POST http://llm5-proxy:8205/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ LLaVA: 631 chars via http://llm5-proxy:8205/generate
INFO:__main__:   [13/21] Processing MiniCPM-V...
INFO:httpx:HTTP Request: POST http://llm4-proxy:8204/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ MiniCPM-V: 745 chars via http://llm4-proxy:8204/generate
INFO:__main__:   [14/21] Processing StarCoder2...
INFO:httpx:HTTP Request: POST http://llm7-proxy:8207/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ StarCoder2: 682 chars via http://llm7-proxy:8207/generate
INFO:__main__:   [15/21] Processing Vicuna...
INFO:httpx:HTTP Request: POST http://llm19-proxy:8219/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ Vicuna: 7 chars via http://llm19-proxy:8219/generate
INFO:__main__:   [16/21] Processing LLaMA 3.1...
INFO:httpx:HTTP Request: POST http://llm22-proxy:8222/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ LLaMA 3.1: 608 chars via http://llm22-proxy:8222/generate
INFO:__main__:   [17/21] Processing Mistral...
INFO:httpx:HTTP Request: POST http://llm21-proxy:8221/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ Mistral: 618 chars via http://llm21-proxy:8221/generate
INFO:__main__:   [18/21] Processing Qwen2...
INFO:httpx:HTTP Request: POST http://llm14-proxy:8214/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ Qwen2: 708 chars via http://llm14-proxy:8214/generate
INFO:__main__:   [19/21] Processing CodeLlama...
INFO:httpx:HTTP Request: POST http://llm8-proxy:8208/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ CodeLlama: 596 chars via http://llm8-proxy:8208/generate
INFO:__main__:   [20/21] Processing DeepSeek Coder...
INFO:httpx:HTTP Request: POST http://llm9-proxy:8209/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ DeepSeek Coder: 636 chars via http://llm9-proxy:8209/generate
INFO:__main__:   [21/21] Processing LLaMA 2...
INFO:httpx:HTTP Request: POST http://llm20-proxy:8220/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ LLaMA 2: 557 chars via http://llm20-proxy:8220/generate
INFO:__main__:✅ Complete: 21/21 responded within budget (elapsed=725.8s)
INFO:     172.18.0.1:54252 - "GET / HTTP/1.1" 404 Not Found
INFO:     172.18.0.1:35598 - "GET / HTTP/1.1" 404 Not Found
INFO:     172.18.0.1:53686 - "GET / HTTP/1.1" 404 Not Found
INFO:     172.18.0.1:44660 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:40750 - "GET / HTTP/1.1" 404 Not Found
INFO:     172.18.0.1:36028 - "GET / HTTP/1.1" 404 Not Found
INFO:     172.18.0.1:33946 - "GET / HTTP/1.1" 404 Not Found
INFO:     172.18.0.1:56154 - "GET /docs HTTP/1.1" 200 OK
INFO:     172.18.0.1:56162 - "GET /openapi.json HTTP/1.1" 200 OK
INFO:     172.18.0.1:45576 - "GET /docs HTTP/1.1" 200 OK
INFO:     172.18.0.1:45588 - "GET /openapi.json HTTP/1.1" 200 OK
INFO:     172.18.0.1:54080 - "GET /openapi.json HTTP/1.1" 200 OK
INFO:     172.18.0.1:54104 - "GET / HTTP/1.1" 404 Not Found
INFO:     172.18.0.52:51856 - "POST /chat_with_context HTTP/1.1" 422 Unprocessable Entity
INFO:     172.18.0.52:42242 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:37008 - "GET / HTTP/1.1" 404 Not Found
INFO:     172.18.0.1:36384 - "GET / HTTP/1.1" 404 Not Found
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ 

