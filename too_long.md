(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/Downloads/files$ psql "postgresql://postgres@localhost:5436/msjarvisgis_v2" -c "
CREATE OR REPLACE VIEW public.wv_county_belief_vector_ready_with_chroma_hashes AS
SELECT
  v.*,
  r.collection_hash,
  f.collection_feature_hash
FROM public.wv_county_belief_vector_ready v
LEFT JOIN public.gbim_chroma_collection_registry r
  ON r.collection_name = 'gbimwvcountiesv2'
LEFT JOIN public.gbim_chroma_collection_feature_registry f
  ON f.collection_name = 'gbimwvcountiesv2'
 AND f.document_id = v.document_id;
"
CREATE VIEW
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/Downloads/files$ psql "postgresql://postgres@localhost:5436/msjarvisgis_v2" -c "
SELECT document_id, collection_hash, collection_feature_hash
FROM public.wv_tract_belief_vector_ready_with_chroma_hashes
LIMIT 5;
"
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/Downloads/files$ psql "postgresql://postgres@localhost:5436/msjarvisgis_v2" -c "
SELECT document_id, collection_hash, collection_feature_hash
FROM public.wv_county_belief_vector_ready_with_chroma_hashes
LIMIT 5;
"
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/Downloads/files$ psql "postgresql://postgres@localhost:5436/msjarvisgis_v2" -c "
SELECT document_id, collection_hash, collection_feature_hash
FROM public.wv_blockgroup_belief_vector_ready_with_chroma_hashes
LIMIT 5;
"
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/Downloads/files$ docker ps --format 'table {{.Names}}\t{{.Image}}\t{{.Ports}}\t{{.Status}}'
NAMES                                        IMAGE                                             PORTS                                                                                                          STATUS
jarvis-ollama                                ollama/ollama:latest                              0.0.0.0:11435->11434/tcp, [::]:11435->11434/tcp                                                                Up About an hour
jarvis-gis-rag                               msjarvis-rebuild-jarvis-gis-rag                   127.0.0.1:8004->8004/tcp, 8044/tcp                                                                             Up 29 hours
jarvis-consciousness-bridge                  msjarvis-rebuild-jarvis-consciousness-bridge      8002/tcp, 127.0.0.1:8020->8020/tcp                                                                             Up 2 days
ms-allis-internal-sandbox                    msjarvis-rebuild-ms-allis-internal-sandbox        127.0.0.1:8042->8042/tcp                                                                                       Up 2 days
jarvis-i-containers                          msjarvis-rebuild-jarvis-i-containers              8015/tcp                                                                                                       Up 2 days
jarvis-msjarvis-db                           postgis/postgis:16-3.4                            127.0.0.1:5433->5432/tcp                                                                                       Up 44 hours (healthy)
jarvis-fractal-consciousness                 msjarvis-rebuild-jarvis-fractal-consciousness     0.0.0.0:8027->8027/tcp, [::]:8027->8027/tcp                                                                    Up 2 days
jarvis-consciousness-scheduler               msjarvis-rebuild-jarvis-consciousness-scheduler   8019/tcp                                                                                                       Up 2 days
jarvis-neurobiological-master                msjarvis-rebuild-jarvis-neurobiological-master    8018/tcp                                                                                                       Up 2 days
jarvis-main-brain                            jarvis-main-brain:latest                          127.0.0.1:8050->8050/tcp                                                                                       Up 2 days
jarvis-unified-gateway                       msjarvis-rebuild-jarvis-unified-gateway           127.0.0.1:8093->8001/tcp                                                                                       Up 2 days (healthy)
jarvis-brain-orchestrator                    msjarvis-rebuild-jarvis-brain-orchestrator        127.0.0.1:17260->7260/tcp                                                                                      Up 2 days (healthy)
jarvis-intake-service                        jarvis-main-brain:latest                          127.0.0.1:8007->8007/tcp                                                                                       Up 2 days
4d2a4c3cc2b3_jarvis-woah                     msjarvis-rebuild-jarvis-woah                      127.0.0.1:7012->7012/tcp                                                                                       Up 2 days
7555461d0e3c_jarvis-fifth-dgm                msjarvis-rebuild-jarvis-fifth-dgm                 127.0.0.1:4002->4002/tcp                                                                                       Up 2 days
neo4j                                        neo4j:5.13-community                              7473/tcp, 127.0.0.1:7687->7687/tcp, 127.0.0.1:7475->7474/tcp                                                   Up 2 days
jarvis-blood-brain-barrier                   msjarvis-rebuild-jarvis-blood-brain-barrier       127.0.0.1:8016->8016/tcp                                                                                       Up 2 days
jarvis-wv-entangled-gateway                  msjarvis-rebuild-jarvis-wv-entangled-gateway      127.0.0.1:8010->8010/tcp                                                                                       Up 2 days
jarvis-20llm-production                      msjarvis-rebuild-jarvis-20llm-production                                                                                                                         Up 2 days
qualia-orchestrator-69dgm-real               qualia-orchestrator:real                          127.0.0.1:9998->9998/tcp                                                                                       Up 2 days (healthy)
jarvis-civic-intake                          jarvis-main-brain:latest                          127.0.0.1:18093->8100/tcp                                                                                      Up 2 days
jarvis-hp-sidecar                            jarvis-hp-sidecar:local                           127.0.0.1:8094->8094/tcp                                                                                       Up 2 days
jarvis-hilbert-state                         jarvis-main-brain:latest                          127.0.0.1:18092->8081/tcp                                                                                      Up 2 days
fa51c5ec3ec9_jarvis-gbim-query-router        jarvis-main-brain:latest                          127.0.0.1:7205->7205/tcp                                                                                       Up 2 days
hp-local-db                                  postgis/postgis:15-3.4                            5432/tcp                                                                                                       Up 2 days
jarvis-kyc-vault                             msjarvis-rebuild-jarvis-kyc-vault                                                                                                                                Restarting (3) 1 second ago
jarvis-redis                                 redis:7-alpine                                    127.0.0.1:6380->6379/tcp                                                                                       Up 2 days (healthy)
e665651c00d5_llm2-proxy                      msjarvis-rebuild-llm2-proxy                       127.0.0.1:8202->8202/tcp                                                                                       Up 2 days
2d6c035dc9fe_llm20-proxy                     msjarvis-rebuild-llm20-proxy                      127.0.0.1:8220->8220/tcp                                                                                       Up 2 days
b91b3c2adba5_llm17-proxy                     msjarvis-rebuild-llm17-proxy                      127.0.0.1:8217->8217/tcp                                                                                       Up 2 days
b5a2b182f1b7_llm19-proxy                     msjarvis-rebuild-llm19-proxy                      127.0.0.1:8219->8219/tcp                                                                                       Up 2 days
c68db82137f8_llm9-proxy                      msjarvis-rebuild-llm9-proxy                       127.0.0.1:8209->8209/tcp                                                                                       Up 2 days
05cbdb9d8b63_llm18-proxy                     msjarvis-rebuild-llm18-proxy                      127.0.0.1:8218->8218/tcp                                                                                       Up 2 days
07868f87c30f_llm10-proxy                     msjarvis-rebuild-llm10-proxy                      127.0.0.1:8210->8210/tcp                                                                                       Up 2 days
f970d6243de9_llm1-proxy                      msjarvis-rebuild-llm1-proxy                       127.0.0.1:8201->8201/tcp                                                                                       Up 2 days
1e1783a0cae3_jarvis-temporal-consciousness   msjarvis-rebuild-jarvis-temporal-consciousness    7007/tcp                                                                                                       Up 2 days
bbd55aa39149_llm13-proxy                     msjarvis-rebuild-llm13-proxy                      127.0.0.1:8213->8213/tcp                                                                                       Up 2 days
cdb1cfcf3615_llm15-proxy                     msjarvis-rebuild-llm15-proxy                      127.0.0.1:8215->8215/tcp                                                                                       Up 2 days
03da3490dbba_llm12-proxy                     msjarvis-rebuild-llm12-proxy                      127.0.0.1:8212->8212/tcp                                                                                       Up 2 days
b9f25945034e_llm6-proxy                      msjarvis-rebuild-llm6-proxy                       127.0.0.1:8206->8206/tcp                                                                                       Up 2 days
6c076127418c_llm4-proxy                      msjarvis-rebuild-llm4-proxy                       127.0.0.1:8204->8204/tcp                                                                                       Up 2 days
6dd05bcbf535_llm5-proxy                      msjarvis-rebuild-llm5-proxy                       127.0.0.1:8205->8205/tcp                                                                                       Up 2 days
f49af6a3d696_llm7-proxy                      msjarvis-rebuild-llm7-proxy                       127.0.0.1:8207->8207/tcp                                                                                       Up 2 days
687596ae0eb1_llm22-proxy                     msjarvis-rebuild-llm22-proxy                      127.0.0.1:8222->8222/tcp                                                                                       Up 2 days
a40eece620f3_nbb_woah_algorithms             msjarvis-rebuild-nbb_woah_algorithms              127.0.0.1:8104->8010/tcp                                                                                       Up 2 days
eeb98757a243_llm21-proxy                     msjarvis-rebuild-llm21-proxy                      127.0.0.1:8221->8221/tcp                                                                                       Up 2 days
8dffd2f7b142_llm3-proxy                      msjarvis-rebuild-llm3-proxy                       127.0.0.1:8203->8203/tcp                                                                                       Up 2 days
22cb4468dbd5_llm8-proxy                      msjarvis-rebuild-llm8-proxy                       127.0.0.1:8208->8208/tcp                                                                                       Up 2 days
675f8bd43968_llm11-proxy                     msjarvis-rebuild-llm11-proxy                      127.0.0.1:8211->8211/tcp                                                                                       Up 2 days
be5c6613bca3_llm14-proxy                     msjarvis-rebuild-llm14-proxy                      127.0.0.1:8214->8214/tcp                                                                                       Up 2 days
69ee8c1dadfb_llm16-proxy                     msjarvis-rebuild-llm16-proxy                      127.0.0.1:8216->8216/tcp                                                                                       Up 2 days
nbb_pituitary_gland                          msjarvis-rebuild-nbb_pituitary_gland              127.0.0.1:8108->80/tcp                                                                                         Up 2 days
jarvis-lm-synthesizer                        msjarvis-rebuild-jarvis-lm-synthesizer            8001/tcp                                                                                                       Up 2 days
jarvis-rag-server                            msjarvis-rebuild-jarvis-rag-server                127.0.0.1:8003->8003/tcp                                                                                       Up 2 days
jarvis-chroma                                chromadb/chroma:0.6.3                             127.0.0.1:8002->8000/tcp                                                                                       Up 2 days (healthy)
jarvis-constitutional-guardian               msjarvis-rebuild-jarvis-constitutional-guardian   127.0.0.1:8091->8091/tcp                                                                                       Up 2 days
jarvis-judge-pipeline                        msjarvis-rebuild-jarvis-judge-pipeline            7239/tcp                                                                                                       Up 2 days
jarvis-semaphore                             msjarvis-rebuild-jarvis-semaphore                 127.0.0.1:8030->8030/tcp                                                                                       Up 2 days
jarvis-web-research                          msjarvis-rebuild-jarvis-web-research              8008/tcp                                                                                                       Up 2 days
jarvis-pia-sampler                           python:3.11-slim                                  8076/tcp                                                                                                       Up 2 days
jarvis-judge-alignment                       msjarvis-rebuild-jarvis-judge-alignment           7232/tcp                                                                                                       Up 2 days
jarvis-spiritual-rag                         msjarvis-rebuild-jarvis-spiritual-rag             127.0.0.1:8005->8005/tcp                                                                                       Up 2 days
jarvis-eeg-theta                             msjarvis-rebuild-jarvis-eeg-theta                 127.0.0.1:8074->8074/tcp                                                                                       Up 2 days
jarvis-eeg-delta                             msjarvis-rebuild-jarvis-eeg-delta                 127.0.0.1:8073->8073/tcp                                                                                       Up 2 days
jarvis-swarm-intelligence                    msjarvis-rebuild-jarvis-swarm-intelligence        8021/tcp                                                                                                       Up 2 days
jarvis-provenance                            msjarvis-rebuild-jarvis-provenance                127.0.0.1:8046->8046/tcp                                                                                       Up 2 days
jarvis-phi-probe                             msjarvis-rebuild-jarvis-phi-probe                 127.0.0.1:8026->8025/tcp                                                                                       Up 2 days
jarvis-ingest-api                            python:3.11-slim                                                                                                                                                 Up 4 hours
jarvis-eeg-beta                              msjarvis-rebuild-jarvis-eeg-beta                  127.0.0.1:8075->8075/tcp                                                                                       Up 2 days
jarvis-rag-router                            msjarvis-rebuild-jarvis-rag-router                8003/tcp, 127.0.0.1:5015->5001/tcp                                                                             Up 2 days
jarvis-nbb-i-containers-2                    msjarvis-rebuild-nbb_i_containers                 127.0.0.1:8015->8015/tcp                                                                                       Up 2 days
jarvis-aaacpe-rag                            msjarvis-rebuild-jarvis-aaacpe-rag                127.0.0.1:8032->8032/tcp                                                                                       Up 2 days
jarvis-judge-truth                           msjarvis-rebuild-jarvis-judge-truth               7230/tcp                                                                                                       Up 2 days
jarvis-aaacpe-scraper                        msjarvis-rebuild-jarvis-aaacpe-scraper            127.0.0.1:8033->8033/tcp                                                                                       Up 2 days
jarvis-judge-ethics                          msjarvis-rebuild-jarvis-judge-ethics              7233/tcp                                                                                                       Up 2 days
jarvis-contracts                             msjarvis-rebuild-jarvis-contracts                                                                                                                                Up 2 days
jarvis-agents-service                        msjarvis-rebuild-jarvis-agents-service            8005/tcp                                                                                                       Up 2 days
jarvis-judge-consistency                     msjarvis-rebuild-jarvis-judge-consistency         7231/tcp                                                                                                       Up 2 days
jarvis-jaeger                                jaegertracing/all-in-one:1.52                     4317-4318/tcp, 5775/udp, 5778/tcp, 9411/tcp, 14250/tcp, 14268/tcp, 6831-6832/udp, 127.0.0.1:16686->16686/tcp   Up 2 days
jarvis-toroidal                              msjarvis-toroidal:latest                          127.0.0.1:8025->8025/tcp                                                                                       Up 2 days
jarvis-psychology-services                   msjarvis-rebuild-jarvis-psychology-services       127.0.0.1:8019->8019/tcp                                                                                       Up 2 days
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/Downloads/files$ docker logs --tail 120 jarvis-chroma
  File "/usr/local/lib/python3.11/site-packages/starlette/middleware/base.py", line 187, in __call__
    response = await self.dispatch_func(request, call_next)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/chroma/chromadb/server/fastapi/__init__.py", line 144, in check_http_version_middleware
    return await call_next(request)
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/starlette/middleware/base.py", line 163, in call_next
    raise app_exc
  File "/usr/local/lib/python3.11/site-packages/starlette/middleware/base.py", line 149, in coro
    await self.app(scope, receive_or_disconnect, send_no_error)
  File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 62, in __call__
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
  File "/usr/local/lib/python3.11/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    raise exc
  File "/usr/local/lib/python3.11/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 715, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 735, in app
    await route.handle(scope, receive, send)
  File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 288, in handle
    await self.app(scope, receive, send)
  File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 76, in app
    await wrap_app_handling_exceptions(app, request)(scope, receive, send)
  File "/usr/local/lib/python3.11/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    raise exc
  File "/usr/local/lib/python3.11/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 73, in app
    response = await f(request)
               ^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 301, in app
    raw_response = await run_endpoint_function(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 212, in run_endpoint_function
    return await dependant.call(**values)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/chroma/chromadb/telemetry/opentelemetry/__init__.py", line 134, in async_wrapper
    return await f(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/chroma/chromadb/server/fastapi/__init__.py", line 719, in list_collections
    await to_thread.run_sync(
  File "/usr/local/lib/python3.11/site-packages/anyio/to_thread.py", line 56, in run_sync
    return await get_async_backend().run_sync_in_worker_thread(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/anyio/_backends/_asyncio.py", line 2461, in run_sync_in_worker_thread
    return await future
           ^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/anyio/_backends/_asyncio.py", line 962, in run
    result = context.run(func, *args)
             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/chroma/chromadb/server/fastapi/__init__.py", line 713, in process_list_collections
    return self._api.list_collections(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/chroma/chromadb/telemetry/opentelemetry/__init__.py", line 150, in wrapper
    return f(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^
  File "/chroma/chromadb/api/segment.py", line 103, in wrapper
    return self._rate_limit_enforcer.rate_limit(func)(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/chroma/chromadb/rate_limit/simple_rate_limit/__init__.py", line 24, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/chroma/chromadb/api/segment.py", line 334, in list_collections
    return self._sysdb.get_collections(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/chroma/chromadb/telemetry/opentelemetry/__init__.py", line 150, in wrapper
    return f(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^
  File "/chroma/chromadb/db/mixins/sysdb.py", line 511, in get_collections
    rows = cur.execute(sql, params).fetchall()
           ^^^^^^^^^^^^^^^^^^^^^^^^
sqlite3.OperationalError: database is locked
DEBUG:    [11-07-2026 15:18:42] Stopping component System
DEBUG:    [11-07-2026 15:18:42] Stopping component SegmentAPI
DEBUG:    [11-07-2026 15:18:42] Stopping component LocalExecutor
DEBUG:    [11-07-2026 15:18:42] Stopping component PersistentLocalHnswSegment
DEBUG:    [11-07-2026 15:18:42] Stopping component PersistentLocalHnswSegment
DEBUG:    [11-07-2026 15:18:42] Stopping component LocalSegmentManager
DEBUG:    [11-07-2026 15:18:42] Stopping component SimpleAsyncRateLimitEnforcer
DEBUG:    [11-07-2026 15:18:42] Stopping component SimpleRateLimitEnforcer
DEBUG:    [11-07-2026 15:18:42] Stopping component Posthog
DEBUG:    [11-07-2026 15:18:42] Stopping component SimpleQuotaEnforcer
DEBUG:    [11-07-2026 15:18:42] Stopping component SqliteDB
DEBUG:    [11-07-2026 15:18:42] Stopping component OpenTelemetryClient
Starting 'uvicorn chromadb.app:app' with args: --workers 1 --host 0.0.0.0 --port 8000 --proxy-headers --log-config chromadb/log_config.yml --timeout-keep-alive 30
INFO:     [11-07-2026 15:19:36] Set chroma_server_nofile to 65536
DEBUG:    [11-07-2026 15:19:36] Starting component System
DEBUG:    [11-07-2026 15:19:36] Starting component OpenTelemetryClient
DEBUG:    [11-07-2026 15:19:36] Starting component SqliteDB
DEBUG:    [11-07-2026 15:19:36] Starting component SimpleQuotaEnforcer
DEBUG:    [11-07-2026 15:19:36] Starting component Posthog
DEBUG:    [11-07-2026 15:19:36] Starting component SimpleRateLimitEnforcer
DEBUG:    [11-07-2026 15:19:36] Starting component LocalSegmentManager
DEBUG:    [11-07-2026 15:19:36] Starting component LocalExecutor
DEBUG:    [11-07-2026 15:19:36] Starting component SegmentAPI
DEBUG:    [11-07-2026 15:19:36] Starting component SimpleAsyncRateLimitEnforcer
DEBUG:    [11-07-2026 15:19:44] Collection ms_jarvis_memory already exists, returning existing collection.
DEBUG:    [11-07-2026 15:19:44] Starting component PersistentLocalHnswSegment
DEBUG:    [11-07-2026 15:19:55] Starting component PersistentLocalHnswSegment
DEBUG:    [11-07-2026 15:19:55] Starting component PersistentLocalHnswSegment
DEBUG:    [11-07-2026 15:20:10] Starting component PersistentLocalHnswSegment
DEBUG:    [11-07-2026 15:20:11] Starting component PersistentLocalHnswSegment
DEBUG:    [11-07-2026 15:20:11] Starting component PersistentLocalHnswSegment
DEBUG:    [11-07-2026 15:20:11] Starting component PersistentLocalHnswSegment
DEBUG:    [11-07-2026 15:20:11] Starting component PersistentLocalHnswSegment
DEBUG:    [11-07-2026 15:20:45] Starting component PersistentLocalHnswSegment
/usr/local/lib/python3.11/site-packages/anyio/_backends/_asyncio.py:958: RuntimeWarning: coroutine 'FastAPI.auth_and_get_tenant_and_database_for_request' was never awaited
  result = None
RuntimeWarning: Enable tracemalloc to get the object allocation traceback
DEBUG:    [11-07-2026 18:42:07] Starting component PersistentLocalHnswSegment
DEBUG:    [11-07-2026 19:03:13] Starting component PersistentLocalHnswSegment
DEBUG:    [11-07-2026 19:12:22] Starting component PersistentLocalHnswSegment
DEBUG:    [11-07-2026 19:20:24] Starting component PersistentLocalHnswSegment
DEBUG:    [12-07-2026 03:04:51] Starting component PersistentLocalHnswSegment
DEBUG:    [12-07-2026 03:04:53] Starting component PersistentLocalHnswSegment
DEBUG:    [13-07-2026 19:01:15] Starting component PersistentLocalHnswSegment
DEBUG:    [13-07-2026 19:03:19] Starting component PersistentLocalHnswSegment
DEBUG:    [13-07-2026 19:19:00] Starting component PersistentLocalHnswSegment
DEBUG:    [13-07-2026 19:20:57] Starting component PersistentLocalHnswSegment
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/Downloads/files$ docker logs --tail 120 jarvis-ollama
slot launch_slot_: id  0 | task 1162 | processing task, is_child = 0
slot   operator(): id  0 | task 1162 | new prompt, n_ctx_slot = 256, n_keep = 0, task.n_tokens = 98
slot   operator(): id  0 | task 1162 | cached n_tokens = 0, memory_seq_rm [0, end)
slot      release: id  0 | task 1162 | stop processing: n_tokens = 98, truncated = 0
srv  update_slots: all slots are idle
slot get_availabl: id  0 | task -1 | selected slot by LRU, t_last = 187298835980
slot launch_slot_: id  0 | task 1164 | processing task, is_child = 0
slot   operator(): id  0 | task 1164 | new prompt, n_ctx_slot = 256, n_keep = 0, task.n_tokens = 107
slot   operator(): id  0 | task 1164 | cached n_tokens = 0, memory_seq_rm [0, end)
slot      release: id  0 | task 1164 | stop processing: n_tokens = 107, truncated = 0
srv  update_slots: all slots are idle
slot get_availabl: id  0 | task -1 | selected slot by LRU, t_last = 187298838572
slot launch_slot_: id  0 | task 1166 | processing task, is_child = 0
slot   operator(): id  0 | task 1166 | new prompt, n_ctx_slot = 256, n_keep = 0, task.n_tokens = 98
slot   operator(): id  0 | task 1166 | cached n_tokens = 0, memory_seq_rm [0, end)
slot      release: id  0 | task 1166 | stop processing: n_tokens = 98, truncated = 0
srv  update_slots: all slots are idle
slot get_availabl: id  0 | task -1 | selected slot by LRU, t_last = 187298841018
slot launch_slot_: id  0 | task 1168 | processing task, is_child = 0
slot   operator(): id  0 | task 1168 | new prompt, n_ctx_slot = 256, n_keep = 0, task.n_tokens = 97
slot   operator(): id  0 | task 1168 | cached n_tokens = 0, memory_seq_rm [0, end)
slot      release: id  0 | task 1168 | stop processing: n_tokens = 97, truncated = 0
srv  update_slots: all slots are idle
slot get_availabl: id  0 | task -1 | selected slot by LRU, t_last = 187298843547
slot launch_slot_: id  0 | task 1170 | processing task, is_child = 0
slot   operator(): id  0 | task 1170 | new prompt, n_ctx_slot = 256, n_keep = 0, task.n_tokens = 89
slot   operator(): id  0 | task 1170 | cached n_tokens = 0, memory_seq_rm [0, end)
slot      release: id  0 | task 1170 | stop processing: n_tokens = 89, truncated = 0
srv  update_slots: all slots are idle
slot get_availabl: id  0 | task -1 | selected slot by LRU, t_last = 187298846045
slot launch_slot_: id  0 | task 1172 | processing task, is_child = 0
slot   operator(): id  0 | task 1172 | new prompt, n_ctx_slot = 256, n_keep = 0, task.n_tokens = 98
slot   operator(): id  0 | task 1172 | cached n_tokens = 0, memory_seq_rm [0, end)
slot      release: id  0 | task 1172 | stop processing: n_tokens = 98, truncated = 0
srv  update_slots: all slots are idle
slot get_availabl: id  0 | task -1 | selected slot by LRU, t_last = 187298848674
slot launch_slot_: id  0 | task 1174 | processing task, is_child = 0
slot   operator(): id  0 | task 1174 | new prompt, n_ctx_slot = 256, n_keep = 0, task.n_tokens = 98
slot   operator(): id  0 | task 1174 | cached n_tokens = 0, memory_seq_rm [0, end)
slot      release: id  0 | task 1174 | stop processing: n_tokens = 98, truncated = 0
srv  update_slots: all slots are idle
slot get_availabl: id  0 | task -1 | selected slot by LRU, t_last = 187298851827
slot launch_slot_: id  0 | task 1176 | processing task, is_child = 0
slot   operator(): id  0 | task 1176 | new prompt, n_ctx_slot = 256, n_keep = 0, task.n_tokens = 98
slot   operator(): id  0 | task 1176 | cached n_tokens = 0, memory_seq_rm [0, end)
slot      release: id  0 | task 1176 | stop processing: n_tokens = 98, truncated = 0
srv  update_slots: all slots are idle
slot get_availabl: id  0 | task -1 | selected slot by LRU, t_last = 187298854476
slot launch_slot_: id  0 | task 1178 | processing task, is_child = 0
slot   operator(): id  0 | task 1178 | new prompt, n_ctx_slot = 256, n_keep = 0, task.n_tokens = 107
slot   operator(): id  0 | task 1178 | cached n_tokens = 0, memory_seq_rm [0, end)
slot      release: id  0 | task 1178 | stop processing: n_tokens = 107, truncated = 0
srv  update_slots: all slots are idle
slot get_availabl: id  0 | task -1 | selected slot by LRU, t_last = 187298857214
slot launch_slot_: id  0 | task 1180 | processing task, is_child = 0
slot   operator(): id  0 | task 1180 | new prompt, n_ctx_slot = 256, n_keep = 0, task.n_tokens = 100
slot   operator(): id  0 | task 1180 | cached n_tokens = 0, memory_seq_rm [0, end)
slot      release: id  0 | task 1180 | stop processing: n_tokens = 100, truncated = 0
srv  update_slots: all slots are idle
slot get_availabl: id  0 | task -1 | selected slot by LRU, t_last = 187298859716
slot launch_slot_: id  0 | task 1182 | processing task, is_child = 0
slot   operator(): id  0 | task 1182 | new prompt, n_ctx_slot = 256, n_keep = 0, task.n_tokens = 88
slot   operator(): id  0 | task 1182 | cached n_tokens = 0, memory_seq_rm [0, end)
slot      release: id  0 | task 1182 | stop processing: n_tokens = 88, truncated = 0
srv  update_slots: all slots are idle
slot get_availabl: id  0 | task -1 | selected slot by LRU, t_last = 187298862499
slot launch_slot_: id  0 | task 1184 | processing task, is_child = 0
slot   operator(): id  0 | task 1184 | new prompt, n_ctx_slot = 256, n_keep = 0, task.n_tokens = 107
slot   operator(): id  0 | task 1184 | cached n_tokens = 0, memory_seq_rm [0, end)
slot      release: id  0 | task 1184 | stop processing: n_tokens = 107, truncated = 0
srv  update_slots: all slots are idle
slot get_availabl: id  0 | task -1 | selected slot by LRU, t_last = 187298865326
slot launch_slot_: id  0 | task 1186 | processing task, is_child = 0
slot   operator(): id  0 | task 1186 | new prompt, n_ctx_slot = 256, n_keep = 0, task.n_tokens = 109
slot   operator(): id  0 | task 1186 | cached n_tokens = 0, memory_seq_rm [0, end)
slot      release: id  0 | task 1186 | stop processing: n_tokens = 109, truncated = 0
srv  update_slots: all slots are idle
slot get_availabl: id  0 | task -1 | selected slot by LRU, t_last = 187298867962
slot launch_slot_: id  0 | task 1188 | processing task, is_child = 0
slot   operator(): id  0 | task 1188 | new prompt, n_ctx_slot = 256, n_keep = 0, task.n_tokens = 100
slot   operator(): id  0 | task 1188 | cached n_tokens = 0, memory_seq_rm [0, end)
slot      release: id  0 | task 1188 | stop processing: n_tokens = 100, truncated = 0
srv  update_slots: all slots are idle
slot get_availabl: id  0 | task -1 | selected slot by LRU, t_last = 187298870694
slot launch_slot_: id  0 | task 1190 | processing task, is_child = 0
slot   operator(): id  0 | task 1190 | new prompt, n_ctx_slot = 256, n_keep = 0, task.n_tokens = 109
slot   operator(): id  0 | task 1190 | cached n_tokens = 0, memory_seq_rm [0, end)
slot      release: id  0 | task 1190 | stop processing: n_tokens = 109, truncated = 0
srv  update_slots: all slots are idle
slot get_availabl: id  0 | task -1 | selected slot by LRU, t_last = 187298873354
slot launch_slot_: id  0 | task 1192 | processing task, is_child = 0
slot   operator(): id  0 | task 1192 | new prompt, n_ctx_slot = 256, n_keep = 0, task.n_tokens = 98
slot   operator(): id  0 | task 1192 | cached n_tokens = 0, memory_seq_rm [0, end)
slot      release: id  0 | task 1192 | stop processing: n_tokens = 98, truncated = 0
srv  update_slots: all slots are idle
slot get_availabl: id  0 | task -1 | selected slot by LRU, t_last = 187298876087
slot launch_slot_: id  0 | task 1194 | processing task, is_child = 0
slot   operator(): id  0 | task 1194 | new prompt, n_ctx_slot = 256, n_keep = 0, task.n_tokens = 97
slot   operator(): id  0 | task 1194 | cached n_tokens = 0, memory_seq_rm [0, end)
slot      release: id  0 | task 1194 | stop processing: n_tokens = 97, truncated = 0
srv  update_slots: all slots are idle
slot get_availabl: id  0 | task -1 | selected slot by LRU, t_last = 187298878689
slot launch_slot_: id  0 | task 1196 | processing task, is_child = 0
slot   operator(): id  0 | task 1196 | new prompt, n_ctx_slot = 256, n_keep = 0, task.n_tokens = 99
slot   operator(): id  0 | task 1196 | cached n_tokens = 0, memory_seq_rm [0, end)
slot      release: id  0 | task 1196 | stop processing: n_tokens = 99, truncated = 0
srv  update_slots: all slots are idle
slot get_availabl: id  0 | task -1 | selected slot by LRU, t_last = 187298881270
slot launch_slot_: id  0 | task 1198 | processing task, is_child = 0
slot   operator(): id  0 | task 1198 | new prompt, n_ctx_slot = 256, n_keep = 0, task.n_tokens = 97
slot   operator(): id  0 | task 1198 | cached n_tokens = 0, memory_seq_rm [0, end)
slot      release: id  0 | task 1198 | stop processing: n_tokens = 97, truncated = 0
srv  update_slots: all slots are idle
slot get_availabl: id  0 | task -1 | selected slot by LRU, t_last = 187298883704
slot launch_slot_: id  0 | task 1200 | processing task, is_child = 0
slot   operator(): id  0 | task 1200 | new prompt, n_ctx_slot = 256, n_keep = 0, task.n_tokens = 99
slot   operator(): id  0 | task 1200 | cached n_tokens = 0, memory_seq_rm [0, end)
slot      release: id  0 | task 1200 | stop processing: n_tokens = 99, truncated = 0
srv  update_slots: all slots are idle
[GIN] 2026/07/13 - 19:20:55 | 200 |  248.177471ms |      172.17.0.1 | POST     "/api/embed"
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/Downloads/files$ python - << 'PY'
import json, chromadb, os

print("LOCAL CHROMA")
local = chromadb.PersistentClient(path=os.path.expanduser("~/chroma"))
for c in local.list_collections():
    try:
        col = local.get_collection(c.name)
        print(json.dumps({
            "name": c.name,
            "count": col.count(),
            "metadata": getattr(col, "metadata", None)
        }, default=str))
    except Exception as e:
        print(json.dumps({"name": c.name, "error": str(e)}))

print("\nREMOTE CHROMA")
remote = chromadb.HttpClient(host="127.0.0.1", port=8002)
for c in remote.list_collections():
    try:
        col = remote.get_collection(c.name)
        print(json.dumps({
            "name": c.name,
            "count": col.count(),
PY      print(json.dumps({"name": c.name, "error": str(e)}))
LOCAL CHROMA
Traceback (most recent call last):
  File "<stdin>", line 7, in <module>
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/models/Collection.py", line 418, in __getattr__
    raise NotImplementedError(
NotImplementedError: In Chroma v0.6.0, list_collections only returns collection names. Use Client.get_collection(gbimwvtractsv2) to access name. See https://docs.trychroma.com/deployment/migration for more information.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 14, in <module>
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/models/Collection.py", line 418, in __getattr__
    raise NotImplementedError(
NotImplementedError: In Chroma v0.6.0, list_collections only returns collection names. Use Client.get_collection(gbimwvtractsv2) to access name. See https://docs.trychroma.com/deployment/migration for more information.
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/Downloads/files$ python - << 'PY'
import os, json, chromadb

def short(x, n=500):
    s = str(x)
    return s if len(s) <= n else s[:n] + "...<truncated>"

def inspect_client(label, client):
    print(f"\n===== {label} =====")
    for c in client.list_collections():
        name = c.name
        print(f"\n--- COLLECTION: {name} ---")
        col = client.get_collection(name)
        print("count:", col.count())
        print("collection_metadata:", json.dumps(getattr(col, "metadata", None), default=str, indent=2))
        sample = col.get(include=["documents", "metadatas"], limit=3)
        for i, rid in enumerate(sample["ids"]):
            print(f"record_{i+1}_id:", rid)
            print("metadata:", json.dumps(sample["metadatas"][i], default=str, indent=2))
            print("document:", short(sample["documents"][i], 800))

local = chromadb.PersistentClient(path=os.path.expanduser("~/chroma"))
PYspect_client("REMOTE", remote)t="127.0.0.1", port=8002)

===== LOCAL =====
Traceback (most recent call last):
  File "<stdin>", line 22, in <module>
  File "<stdin>", line 10, in inspect_client
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/models/Collection.py", line 418, in __getattr__
    raise NotImplementedError(
NotImplementedError: In Chroma v0.6.0, list_collections only returns collection names. Use Client.get_collection(gbimwvtractsv2) to access name. See https://docs.trychroma.com/deployment/migration for more information.
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/Downloads/files$ find ~ -type f \
  \( -iname '*.py' -o -iname '*.sql' -o -iname '*.sh' -o -iname '*.md' -o -iname '*.txt' \) \
  | grep -Ei 'person|people|time|temporal|hilbert|publish|chroma|belief|snapshot|manifest|registry' \
  | sort
find: ‘/home/cakidd/msjarvis-rebuild-working/msjarvis-rebuild/data/local_resources’: Permission denied
find: ‘/home/cakidd/msjarvisgis_cluster_recovery_copy’: Permission denied
/home/cakidd/46a-69DGM-Consciousness-Bridge-Implementation-Snapshot.md
/home/cakidd/audit-snapshots/audit_20260628_132144/00_meta.txt
/home/cakidd/audit-snapshots/audit_20260628_132144/01_counts.txt
/home/cakidd/audit-snapshots/audit_20260628_132144/01_docker_ps_full.txt
/home/cakidd/audit-snapshots/audit_20260628_132144/01_running_count.txt
/home/cakidd/audit-snapshots/audit_20260628_132144/02_nonloopback_bindings.txt
/home/cakidd/audit-snapshots/audit_20260628_132144/03_health.txt
/home/cakidd/audit-snapshots/audit_20260628_132144/04_images.txt
/home/cakidd/audit-snapshots/audit_20260628_132144/05_ollama_models.txt
/home/cakidd/audit-snapshots/audit_20260628_132144/06_chroma_summary.txt
/home/cakidd/audit-snapshots/audit_20260628_132144/06_chroma.txt
/home/cakidd/audit-snapshots/audit_20260628_132144/07_postgres.txt
/home/cakidd/audit-snapshots/audit_20260628_132144/08_naming.txt
/home/cakidd/audit-snapshots/audit_20260628_132144/09_public_endpoint.txt
/home/cakidd/audit-snapshots/audit_20260628_132144/SNAPSHOT.md
/home/cakidd/audit-snapshots/chromaverify_20260628_134458/VERIFY.md
/home/cakidd/audit-snapshots/portaudit_20260628_133930/00_meta.txt
/home/cakidd/audit-snapshots/portaudit_20260628_133930/01_counts.txt
/home/cakidd/audit-snapshots/portaudit_20260628_133930/04_host_listeners.txt
/home/cakidd/audit-snapshots/portaudit_20260628_133930/05_host_listeners_external.txt
/home/cakidd/audit-snapshots/portaudit_20260628_133930/06_firewall.txt
/home/cakidd/audit-snapshots/portaudit_20260628_133930/07_doc_reconcile.txt
/home/cakidd/audit-snapshots/portaudit_20260628_133930/08_port_map_canonical.txt
/home/cakidd/audit-snapshots/portaudit_20260628_133930/09_nmap_localhost_full.txt
/home/cakidd/audit-snapshots/portaudit_20260628_133930/SUMMARY.md
/home/cakidd/.cache/chroma/onnx_models/all-MiniLM-L6-v2/onnx/vocab.txt
/home/cakidd/calliope/docs/advanced/time.md
/home/cakidd/calliope/src/calliope/preprocess/time.py
/home/cakidd/calliope/src/calliope/schemas/runtime_attrs_schema.py
/home/cakidd/calliope/tests/preprocess/time_test.py
/home/cakidd/Downloads/beyond_euclidean_slam_toroidal_hilbert_world_models.md
/home/cakidd/Downloads/COMPLETE_CHROMA_FIX.sh
/home/cakidd/Downloads/EMERGENCY_CHROMA_DIAGNOSIS.sh
/home/cakidd/Downloads/files(9)/generate-timesheet.py
/home/cakidd/Downloads/fix-ledger-localtime.py
/home/cakidd/Downloads/fix_persona_v6.py
/home/cakidd/Downloads/fix_persona_v7.py
/home/cakidd/Downloads/generate-timesheet(1).py
/home/cakidd/Downloads/generate-timesheet.py
/home/cakidd/Downloads/Hilbert People Space — Person-in-Context Without Surveillance(1).md
/home/cakidd/Downloads/Hilbert People Space — Person-in-Context Without Surveillance.md
/home/cakidd/Downloads/ingest_gis_to_chroma(1).py
/home/cakidd/Downloads/ingest_gis_to_chroma(2).py
/home/cakidd/Downloads/ingest_gis_to_chroma.py
/home/cakidd/Downloads/inspect-timesheet2.py
/home/cakidd/Downloads/inspect-timesheet3(1).py
/home/cakidd/Downloads/inspect-timesheet3.py
/home/cakidd/Downloads/inspect-timesheet.py
/home/cakidd/Downloads/KTS-detailed_timesheet_2025-2026(1).md
/home/cakidd/Downloads/KTS-detailed_timesheet_2025-2026.md
/home/cakidd/Downloads/KTS_Timesheet_2025_2026.md
/home/cakidd/Downloads/KTS_Timesheet_Corrected_v1.1.md
/home/cakidd/Downloads/KTS_Timesheet_v1.2_Final.md
/home/cakidd/Downloads/msjarvis_audit_snapshot.sh
/home/cakidd/Downloads/msjarvis_chroma_backup_verify.sh
/home/cakidd/Downloads/seed_chromadb(1).py
/home/cakidd/Downloads/seed_chromadb.py
/home/cakidd/Downloads/timesheet_import.sql
/home/cakidd/fix_chroma.sh
/home/cakidd/gbim-investigation-20260712T192124Z/14-manifest-dir.txt
/home/cakidd/gbim-investigation-20260712T192124Z/15-manifest-hashes.txt
/home/cakidd/gbim-investigation-20260712T192124Z/16-header-wv_source_manifest_layers.txt
/home/cakidd/gbim-investigation-20260712T192124Z/17-live-tables-not-in-any-manifest.txt
/home/cakidd/gbim-investigation-20260712T192124Z/18-manifest-tables-not-in-database.txt
/home/cakidd/gbim-investigation-20260712T192124Z/20-chroma.txt
/home/cakidd/gbim-investigation-20260712T192124Z/23-gates-and-chroma.txt
/home/cakidd/hilbert_people_audit_20260629_012202/compose_files.txt
/home/cakidd/hilbert_people_audit_20260629_012202/container_env.txt
/home/cakidd/hilbert_people_audit_20260629_012202/docker_ps.txt
/home/cakidd/hilbert_people_audit_20260629_012202/MountainShares-Commons_risk_grep.txt
/home/cakidd/hilbert_people_audit_20260629_012202/msjarvis-rebuild_risk_grep.txt
/home/cakidd/hilbert_people_audit_20260629_012317/chroma_collections.txt
/home/cakidd/hilbert_people_audit_20260629_012317/compose_files.txt
/home/cakidd/hilbert_people_audit_20260629_012317/container_env.txt
/home/cakidd/hilbert_people_audit_20260629_012317/docker_ps.txt
/home/cakidd/hilbert_people_audit_20260629_012921/chroma_collections.txt
/home/cakidd/hilbert_people_audit_20260629_012921/chroma_faces_only.txt
/home/cakidd/hilbert_people_audit_20260629_012921/chroma_faces_probe.txt
/home/cakidd/hilbert_people_audit_20260629_012921/chroma_userish_collections.txt
/home/cakidd/hilbert_people_audit_20260629_012921/compose_files.txt
/home/cakidd/hilbert_people_audit_20260629_012921/container_env.txt
/home/cakidd/hilbert_people_audit_20260629_012921/container_networks.txt
/home/cakidd/hilbert_people_audit_20260629_012921/docker_networks.txt
/home/cakidd/hilbert_people_audit_20260629_012921/docker_ps.txt
/home/cakidd/hilbert_people_audit_20260629_012921/faces_callers.txt
/home/cakidd/hilbert_people_audit_20260629_012921/MountainShares-Commons_identity_vectors_paths_clean.txt
/home/cakidd/hilbert_people_audit_20260629_012921/MountainShares-Commons_identity_vectors_paths.txt
/home/cakidd/hilbert_people_audit_20260629_012921/msjarvisgis_risky_columns.txt
/home/cakidd/hilbert_people_audit_20260629_012921/msjarvisgis_risky_routines.txt
/home/cakidd/hilbert_people_audit_20260629_012921/msjarvisgis_risky_table_ddl.sql
/home/cakidd/hilbert_people_audit_20260629_012921/msjarvisgis_risky_tables.txt
/home/cakidd/hilbert_people_audit_20260629_012921/msjarvisgis_schemas.txt
/home/cakidd/hilbert_people_audit_20260629_012921/msjarvis-rebuild_identity_vectors_paths_clean.txt
/home/cakidd/hilbert_people_audit_20260629_012921/msjarvis-rebuild_identity_vectors_paths.txt
/home/cakidd/hilbert_people_audit_20260629_012921/openapi_capture_log.txt
/home/cakidd/hilbert_people_audit_20260629_012921/openapi_people_paths.txt
/home/cakidd/hilbert_people_audit_20260629_012921/prohibited_tables_present.txt
/home/cakidd/hilbert_people_audit_20260629_012921/prohibited_tables_status.txt
/home/cakidd/hilbert-proof/empirical_data_20260506_105219.txt
/home/cakidd/hp-antisurveillance-build-20260629-014619/artifacts/chroma-risk-summary.txt
/home/cakidd/hp-antisurveillance-build-20260629-014743/artifacts/chroma-risk-summary.txt
/home/cakidd/hp-antisurveillance-build-20260629-014830/artifacts/chroma-risk-summary.txt
/home/cakidd/hp-antisurveillance-next-20260629-015308/artifacts/chroma-options-faces.txt
/home/cakidd/inspect_chroma.py
/home/cakidd/jarvis_audit/scripts/pg_topology_snapshot.sh
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/AaaCPE_Appalachian_Dialect_Knowledge.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/aaacpe_initial_ingest.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/aaacpe_rag_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/aaacpe_scraper/aaacpe_scraper_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/aaacpe_scraper_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/aacpe_ingest_community.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/aacpe_prepare_metadata.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/aapcappe_ingest.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/academic_research_gateway_8062_cors.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/academic_research_gateway_8062.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/academic_whitebox_api.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/activate_dgm_enhanced.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/activate_dgm.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/activate_egeria_persona.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/add_auto_store.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/add_background_call.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/add_background_storage.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/add_conversation_context.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/add_conversation_endpoint.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/add_conversation_storage.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/add_dynamic_context.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/add_fast_layer.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/add_fifth_dgm_to_chat.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/add_full_brain_class.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/add_gpu_cleanup_correct.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/add_gpu_cleanup_every_3.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/add_identity_context.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ADDITIONAL_SERVICES_FINAL.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ADDITIONAL_SERVICES.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/add_jarvis_personality.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/add_learning_suggestion.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/add_mamma_greeting_simple.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/add_messenger_to_gateway.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/add_new_consciousness_services.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/add_ready_endpoint.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/add_security_to_chat.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/add_semaphore.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/add_simple_gpu_cleanup.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/add_swagger_to_ports.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/add_swagger_to_rag.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/add_to_consciousness_engine.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/add_to_main_consciousness.psychology_patched.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/add_to_main_consciousness.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/add_user_memory_attribute.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/add_user_memory.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/add_web_research_storage.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/add_working_search.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/advanced_service_dashboard.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/agents_main.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ai_server_11llm_OPTIMIZED.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ai_server_19llm_CONSCIOUS.backup_20251013_082519.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ai_server_19llm_CONSCIOUS.backup_20251013_083103.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ai_server_19llm_CONSCIOUS.backup_20251026_200122.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ai_server_19llm_CONSCIOUS.backup_20251110_135425.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ai_server_19llm_CONSCIOUS.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ai_server_19llm_PRODUCTION.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ai_server_19llm_PRODUCTION_WITH_HEALTH.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ai_server_20llm_FINAL.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ai_server_20llm_PRODUCTION.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ai_server_22llm_FIXED.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ai_server_22llm.psychology_patched_FIXED.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ai_server_22llm.psychology_patched.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ai_server_22llm.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ai_server_22llm_SEQUENTIAL_OPTIMIZED_ORDER.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ai_server_22llm_SEQUENTIAL.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ai_server_22llm_SMALL_TO_LARGE.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ai_server_4llm.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ai_server_integrated.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ai_server_original_backup.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ai_server.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ai_server_restored.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ai_teams_config.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/all_actual_py.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/all_actual_services.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/all_build_dirs.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/all_service_ports.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/all_services_compose_blocks_dynamic.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/all_services_compose_blocks.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/all_services.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/apk-list.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/apply_ollama_fix.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/apt-list.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/async_polling_architecture.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/attention_multimodal_fuser.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/attention_pipeline.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/attention_priority_scheduler.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/attention_router.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/audit_attrs.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/audit_local_state.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/auth.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/auto_fix_gateway.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/autonomous_learner_gisgeodb_wrapper.psychology_patched.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/autonomous_learner_gisgeodb_wrapper.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/autonomous_learner.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/autonomous_learner_topic_source.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/auto_rag_builder.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/available_models.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/backfill_gbim_worldview_metadata.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/backfill_gbim_worldview_metadata_v2.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/background_curator.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/batch_normalize_beliefs.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/batch_patch_services.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bbb_ethics_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bbb_requirements.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bbb_signature_verifier.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bbb_validator.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/belief_integrator.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/belief_revision_engine.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/belief_state_schema.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/benefits_chat.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/brain_orchestrator_main.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/brain_orchestrator.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_69dgm.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_autonomous_to_i_container_dgm_woah.psychology_patched.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_autonomous_to_i_container_dgm_woah.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_autonomous_to_i_container_fixed.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10001.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10002.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10003.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10004.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10005.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10006.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10007.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10008.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10009.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10010.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10011.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10012.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10013.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10014.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10015.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10016.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10017.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10018.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10019.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10020.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10021.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10022.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10023.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10024.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10025.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10026.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10027.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10028.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10029.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10030.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10031.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10032.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10033.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10034.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10035.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10036.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10037.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10038.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10039.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10040.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10041.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10042.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10043.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10044.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10045.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10046.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10047.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10048.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10049.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10050.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10051.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10052.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10053.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10054.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10055.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10056.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10057.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10058.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10059.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10060.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10061.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10062.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10063.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10064.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10065.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10066.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10067.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10068.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm_10069.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bridge_cross_dgm.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/build_additional_services.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/build_dir_audit.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/build_entityid_to_chromaid_map.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/build_project_impact_graph.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bulk_build_beliefs.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bulk_compose_rewrite.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bulk_load_knowledge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bulk_load_MAXIMUM.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/bulk_sync_gis_to_chromadb.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/chain_listener.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/chat_endpoint_universal.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/chat_server.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/chat_worker.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/chroma_client_old.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/chroma_client.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/chroma_config.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/chromadb_client.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/chromadb_main.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/chromadb_rag_helper.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/chromadb_rest_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/chromadb_v2_to_gis_sync.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/chroma_health_monitor.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/chroma_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/chroma_health_utils.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/chroma_python_test.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/chroma_test.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/chunked_ingest_gbim_to_chroma.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/clean_compose.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/clean_integration.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/clean_service_candidates.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/cleanup_manifest.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/cloudflare_domain_integration.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/commons_gamification.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/community_stake_registry.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/complete_fix.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/complete_memory_fix.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/complete_system_audit.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/complete_system_audit_with_swagger.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/comprehensive_gisgeodb_audit_FIXED.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/comprehensive_gisgeodb_audit.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/COMPREHENSIVE_PORT_AUDIT_20251009_234234.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/comprehensive_storage_fix.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/comprehensive_url_fix.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ConfigLoader.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/config_spiritual.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/configure_facebook_webhook.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/connection_pooling.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/consciousness_coordinator.psychology_patched.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/consciousness_coordinator.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/consciousness_feed_integration.psychology_patched.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/consciousness_feed_integration.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/consciousness_gateway.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/consciousness_with_egeria_voice.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/consciousness_working.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/consensus_4010_stub.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/consolidate_to_chroma_db.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/constitutional_api_fixed.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/constitutional_api.PROD_BACKUP.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/constitutional_api.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/constitutional_guardian.PROD_BACKUP.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/constitutional_guardian.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/CONSTITUTIONAL_SCHEDULER_ENTRY.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/context_manager.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/contract_generator.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/conversation_memory_endpoints.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/conversion_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/count_collections_local.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/count_collections.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/cpu_optimization.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/create_autonomous_learner_tables.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/create_consciousness_data_integration.psychology_patched.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/create_consciousness_data_integration.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/create_dual_consciousness_i_containers.psychology_patched.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/create_dual_consciousness_i_containers.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/create_geodb_nodes.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/create_immutable_security_layer.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/create_i_statement_feedback_loop.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/create_perpetual_storage_layer.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/create_tile_index.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/create_ueid_identity_layer.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/crypto_client.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/dao_governance.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/data_inventory_endpoint.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/dedupe_compose.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/DEPLOYMENT_ORDER.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/designed_ports.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/dgm_adoption_worker.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/dgm_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/dgm_connector_registry.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/dgm_orchestrator_fake.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/dgm_orchestrator.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/dgm_rag_integration.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/dgm_rag_integration_v2.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/dgm_supervisor_woah_fixed.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/dgm_supervisor_woah.psychology_patched.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/dgm_supervisor_woah.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/dgm_supervisor_woah_simple.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/dgm_worker.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/dir_endpoints.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/disable_aggressive_cleaning.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/domain_service_router.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/download_nltk_data.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/dpkg-list.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/dynamic_app.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/dynamic_port_scheduler.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/dynamic_port_service_enhanced.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/dynamic_port_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/egeria_active_heartbeat.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/EGERIA_AGI_TEST_RESULTS_SUMMARY.md
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/egeria_api_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/egeria_autonomous_inquiry_active.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/egeria_autonomous_inquiry.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/egeria_code_execution_engine.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/egeria_core_identity.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/egeria_facebook_perpetual_scheduler.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/EGERIA_IDENTITY.md
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/egeria_multi_mode_system.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/egeria_safe_self_correction.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/egeria_status_poller.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/egeria_system_prompt.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/egeria_true_identity.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/egeria_web_ui_dynamic.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/egeria_web_ui_final_biological.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/egeria_web_ui_FIXED.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/egeria_web_ui_fixed_simple.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/egeria_web_ui_plain_authentic.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/egeria_web_ui.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/egeria_web_ui_v3_consciousness.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/egeria_web_ui_with_execution.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/egeria_web_ui_working.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/email_auto_checker.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/email_gis_geolocation_extractor.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/email_rag_integration.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/email_strategy.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/embed_and_add.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/embed_and_query.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/embed_gbim.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/embed_geodb.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/enable_22llm_routing.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/enhance_agent_prompts.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/enhance_cleaner.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/enhanced_learner_concept.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/enhance_pituitary_warmth.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/enhance_rag_first.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/enhance_rag_knowledge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/enrich_geodb_collections.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/enrich_geodb_layers.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ethical_filter.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/etl_from_csv_template.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/etl_from_manifest.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/etl_template_layer.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/export_attributes_to_gis.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/export_chroma_manifest.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/export_geodb_attrs.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/export_metadata_csv.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/extract_all_chromadbs_to_gis.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/extract_all_chromadb_to_gis.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/extract_binder4_text.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/extract_chroma_sqlite_to_gis.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/extract_real_knowledge_to_gis.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/extract_shapefile_features_to_csv.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/facebook_chat_unified.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/facebook_consciousness_daemon.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/facebook_daemon_polling.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/facebook_messenger_integration.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/facebook_poster_autonomous.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/facebook_poster_fast.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/facebook_poster.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/facebook_poster_working.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/facebook_voice_orchestrator_egeria.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fifth_dgm_integration.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fifth_dgm_main.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fifth_dgm.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/file_metadata_matching_algorithm.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fill_null_coordinates_mount_hope.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/final_model_optimization.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_agent_prompts.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_all_consciousness_services.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_autonomous_learner_endpoint.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_autonomous_learner_indent.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_autonomous.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_background_storage.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_chat_server.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_chroma_url.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_consciousness_endpoints.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_context_flow.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_creator_recognition.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_fastapi_lifespan.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_gpu_and_retry.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_import.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_indentation.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_judge_and_memory.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_judge_authentic.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_judge_response.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_judge_synthesis.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_main_brain_endpoints.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_model_names.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_model_unloading.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_multi_rag_chromadb.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_new_service_endpoints.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_orchestrator_init.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_orchestrator_scope.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_persona_hang.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_persona.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_port_8001_clean.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_port_8051_handler.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_prompt_leak.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_query_service_endpoints.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_rag_store.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_response_parsing.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_semaphore.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_storage.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_swagger.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_timeouts_add_22llm.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_web_research.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fix_woah_discovery.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fractal_adapter.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/fraud_detection_ai.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/FULL_DEPLOYMENT_MANIFEST.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gateway8050_simple.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gateway_messenger_integration.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gateway_verify_fixed.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gateway_wv_entanglement.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gbim_api.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gbim_benefit_indexer.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gbim_chroma_fixed.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gbim_chroma.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gbim_core.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gbim_dashboard.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gbim_entangled_summary.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gbim_entanglement.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gbim_explain.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gbim_gis_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gbim_metadata_loader.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gbim_msjarvis.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gbim_query_router.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gbim_reingest_placeholder.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gbim-router/app/assertion_client.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gbim-router/app/hilbert_writer.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gbim-router/app/__init__.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gbim-router/app/integration_patch.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gbim-router/nearest_hospitals.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gbim-router/requirements.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gbim_semantic_indexer.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gbim_spatial_indexer.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gbim_temporal_indexer.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gbim_v0_retrieval.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gdb_integration_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/generate_services.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/geobim_health_shim_8051.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/geobim_integrated.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/geobim_mysql.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/geobim_mysql_v2.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/geodb_adapter.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/geodb_core.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/geo_rag_debug_app.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/geo_rag_debug.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/geospatial_resolver.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gis_chat_integration.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gis_command_module.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gisgeodbdirectaccess.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gisgeodb_learner_hook.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gisgeodb_storage.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gis-rag/ingest_gis_tables.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gis_rag_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gpu_accelerated_rag_fixed.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/gpu_accelerated_rag.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/guards_api_module.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/guards.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/hardware_optimization_analyzer.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/harmony4hope_deployment_manager.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/health_access_api.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/health_access_gbim_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/health_access_query.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/health_check_cache.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/hello.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/hierarchical_coordinator_autonomous.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/hierarchical_coordinator_deep_mode.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/hierarchical_integration.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/hierarchical_method.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/hilbert/chroma_policy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/hilbert/civic_intake.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/hilbert/civic_projector.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/hilbert/civic_query.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/hilbert_commons/commons_aggregator.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/hilbert_commons/_gen_seeds.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/hilbert_commons/kanon.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/hilbert_commons/projector.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/hilbert/ingest_worker.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/hilbert/__init__.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/hilbert/jarvis_hilbert_state.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/hilbert/layer3_opt_in.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/hilbert/migrations/001_hp_appearance_schema.sql
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/hilbert/pipeline/__init__.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/hilbert/query_guard.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/hilbert_spatial_chat.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/hilbert/test_hilbert_state.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/hilbert/write_pipeline.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/hilbert/wv_civic_infrastructure.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/hippocampus_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/host_bulk_loader.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/hp_antisurveillance_guardian_client.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/hp_sidecar.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/i_container_interest_algorithm.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/icontainers_fastapi.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/immutable_core_enforcement.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/implement_judge_pituitary_fixed.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/implement_safe_optimizations.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/import_gbim_assets.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/import_gis_geodata_to_gbim.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/import_gisgeodata_to_gbim.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/index_all_extracted_gis.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/infrastructure_endpoints.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ingest_additional_kbs.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ingest_api.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ingest_benefit_programs.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ingest_benefit_programs_to_chroma.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ingest_compliance_tasks_to_chroma.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ingest_csv_to_gisgeodb.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ingestcsvtogisgeodb.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ingest_documents_to_chromadb.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ingest_full_attributed_docs.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ingest_gbim_to_chroma_fast.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ingest_gbim_to_chroma.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ingest_gbim_to_chroma_resume.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ingest_gbim_to_chroma_ultrafast.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ingest_gis_features_to_chromadb.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ingest_h4h_cultural_heritage.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ingest_hospitals.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ingest_imm_to_chroma.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ingest_knowledge_simple.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ingest_mrsid_imagery.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ingest_utility_enrollments_to_chroma.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ingest_watcher.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/__init__.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/inject_egeria_persona.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/inject_gisgeodb_into_learner.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/inspect_geodb_collection.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/intake_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/integrate_all_services.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/integrate_complete_architecture.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/integrate_consciousness_into_swarm.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/integrate_fifth_dgm_autonomous_learner.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/integrate_full_brain.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/integrate_full_neural_architecture.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/integrate_i_container_interests.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/integrate_i_container_to_schedulers.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/integrate_orchestrator_flow.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/integrate_spatial_temporal.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/INTEGRATION_IMPLEMENTATION.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/interaction_logger.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/internet_tunnel_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-69dgm-bridge_jarvis-fractal-consciousness_baseline.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-aaacpe-rag_aaacpe_rag_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-adoption-worker_dgm_adoption_worker.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-agents-service_ms_jarvis_consciousness_unified_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvisarchiveapi.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-assertion-gateway/app/claims.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-assertion-gateway/app/__init__.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-assertion-gateway/app/kyc_reader.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-assertion-gateway/app/main.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-assertion-gateway/app/minimization.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-assertion-gateway/app/policy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-assertion-gateway/requirements.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis_authentic_persona.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-constitutional-guardian_constitutional_api.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarviscryptopolicy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis_ensemble.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-fifth-dgm_service_discovery.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-gis-rag_gis_rag_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis_hilbert_semantic.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis_hilbert_state.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis_hilbert_time.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-hippocampus_hippocampus_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-i-containers_icontainers_fastapi.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-judge-alignment_lm_synthesizer.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-judge-consistency_lm_synthesizer.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-judge-ethics_lm_synthesizer.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-judge-pipeline_judge_pipeline.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-judge-truth_lm_synthesizer.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis_llm1.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-lm-synthesizer_lm_synthesizer.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-local-resources_local_resources_resolver.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-mother-protocols_mother_protocols.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-neurobiological-master_ms_jarvis_consciousness_unified_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-psychology-services_psychology_integration_adapter.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-qualia-engine_ms_jarvis_qualia_engine.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-rag-server_ms_jarvis_consciousness_unified_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-semaphore_msjarvis_semaphore.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-spiritual-rag_spiritual_rag_domain.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis_steward.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis_stewardship_scheduler.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-swarm-intelligence_ms_jarvis_consciousness_unified_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis_synth_llm.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-temporal-consciousness_temporal_consciousness.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-toroidal_toroidal_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-woah_dgm_supervisor_woah_fixed.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10070.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10071.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10072.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10073.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10074.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10075.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10076.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10077.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10078.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10079.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10080.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10081.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10082.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10083.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10084.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10085.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10086.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10087.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10088.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10089.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10090.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10091.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10092.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10093.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10094.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10095.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10096.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10097.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10098.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10099.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10100.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10101.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10102.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10103.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10104.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10105.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10106.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10107.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10108.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10109.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10110.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10111.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10112.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10113.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10114.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10115.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10116.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10117.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10118.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10119.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10120.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10121.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10122.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10123.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10124.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10125.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10126.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10127.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10128.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10129.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10130.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10131.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10132.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10133.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10134.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_10135.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_alignment_filter.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_consistency_engine.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_ethics_filter.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_pipeline.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judgesigner.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_to_pituitary_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/judge_truth_filter.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/knowledge_growth_endpoint.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/layer2_port9000_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/link_gisgeodb_to_files.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/list_geodb_collections.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/live_ports.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm10_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm10-proxy_llm10_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm11_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm11-proxy_llm11_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm12_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm12-proxy_llm12_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm13_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm13-proxy_llm13_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm14_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm14-proxy_llm14_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm15_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm15-proxy_llm15_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm16_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm16-proxy_llm16_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm17_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm17-proxy_llm17_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm18_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm18-proxy_llm18_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm19_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm19-proxy_llm19_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm1_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm1-proxy_llm1_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm20_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm20-proxy_llm20_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm21_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm21-proxy_llm21_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm22_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm22-proxy_llm22_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm2_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm2-proxy_llm2_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm3_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm3-proxy_llm3_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm4_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm4-proxy_llm4_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm5_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm5-proxy_llm5_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm6_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm6-proxy_llm6_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm7_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm7-proxy_llm7_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm8_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm8-proxy_llm8_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm9_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm9-proxy_llm9_health_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm_belief_utils.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm_bridge_main.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm_conscious_OPTIMIZED.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm_consensus_19_PRODUCTION.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm_consensus_20_FINAL.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm_consensus_22_OPTIMIZED_ORDER.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm_consensus_22.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm_consensus_22_SMALL_TO_LARGE.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm_ensemble_router.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/llm_judge_v3.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/lm_synthesizer.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/load_backbone_places_from_geodb.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/load_complete_knowledge_base.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/load_feature_geometries_to_chromadb.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/load_geodb_health_providers_to_neo4j.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/load_geodb_hospitals_to_neo4j.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/load_geodb_layer_to_neo4j.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/load_gis_to_chroma.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/load_pdfs_spiritual.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/load_rag_data.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/load_rag_knowledge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/load_shapefile_features_to_chromadb.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/load_spiritual_library.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/local_resources_resolver.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/logging_conf.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/main_brain_legacy_backup.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/main_brain_psychology_patch.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/main_brain.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/main_brian.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/main.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/main_qualia.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/main_with_rag.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/mamma_kidd_auth.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/MAMMA_KIDD_QUICK_REFERENCE.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/manifest_endpoints.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/manual_storage_patch.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/master_chat_orchestrator_dynamic.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/master_chat_orchestrator.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/master_chat_orchestrator_v5_consciousness.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/master_chat_orchestrator_v6_biologics.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/master_chat_orchestrator_v7_complete.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/master_chat_orchestrator_v7_dynamic.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/master_chat_orchestrator_v8_spiritual_complete.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/master_chat_orchestrator_v9_dgm_complete.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/master_chat_orchestrator_v9_gpu_optimized.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/master_chat_orchestrator_v9_optimized.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/master_unified_consciousness_scheduler_ENRICHED.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/master_unified_consciousness_scheduler.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/memory_dgm_engine.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/memory_dgm_gateway.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/memory_manager.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/mesh_coordinator_interface.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/messenger_service_fixed.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/METHOD_AUDIT_RAW.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/method_tracker_decorator.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/method_tracking_helper.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/method_tracking_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/metrics_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/migrate_blood_brain_barrier.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/migrate_chromadb_collections.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/migrate_gis2chroma.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/migrate_neurobiological_master.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/modify_autonomous_learning_cycle.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/mother_carrie_logging.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/mother_protocols.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/mountainshares_award.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/mountainshares_chain_monitor.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/mountainshares_gbim_suggester.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/mountainshares_ingest.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/mountainshares_quest_api.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/mountainshares_registry.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/move_huggingface_to_cpu.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_egeria_facebook_autopost.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_agents_ollama.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_agents_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_alerting_manager.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_api_docs.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_attribute_table_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_attribute_table_sync_continuous.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_authentic_multi_llm.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvis_autolearner_minimal.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_autonomous_learner_FIXED.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_autonomous_learner_optimized.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_autonomous_learner.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_autonomous_learner_WITH_FIFTH_DGM.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_auto_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_bbb_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvis_bbb_proxy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvis_benefit_rag.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_blockchain_deployment.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_blood_brain_barrier.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_brain_orchestrator_advanced.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_brain.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_chromadb_query.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_cleanup_manager.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvis_client.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_command_orchestrator_FINAL.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_command_orchestrator.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_command_orchestrator_v5.0_preachy.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_command_orchestrator_v5_backup.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_complete_knowledge_ingestion.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_conscious_collective.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_consciousness_bridge_enhanced.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_consciousness_bridge_parallel_woah.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_consciousness_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvisconsciousnessbridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_consciousness_bridge_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_consciousness_bridge_woah.psychology_patched.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_consciousness_bridge_woah.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_consciousness_complete.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_consciousness_enhancement_production.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_consciousness_final.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_consciousness_poster_FIXED.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_consciousness_poster.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_consciousness_unified_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_consensus_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_contract_builder.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_contract_builder_v2.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_conversational_chat.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_conversational_gateway_4022.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_daily_backup.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_darwin_godel_machine.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_dynamic_model_selector.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_easyocr_processor_old.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_easyocr_processor.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_email_identity_verifier.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_email_monitor.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_email_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_eternal_watchdog.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_exclusive_training_layer.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_expiration_monitor.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_facebook_async.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_facebook_autonomous_social.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_facebook_brain_integrated.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_facebook_CONSCIOUSNESS_FIXED.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_facebook_CONSCIOUSNESS.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_facebook_DGM.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_facebook_dgm_woah.psychology_patched.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_facebook_dgm_woah.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_facebook_full.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_facebook_intelligent.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_facebook_poster_8040.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_facebook_poster_FIXED.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_facebook_poster.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_facebook_poster_temp.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_facebook_poster_v3.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_facebook_PRODUCTION.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_facebook_rag.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_facebook_webhook.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_facebook_webhooks.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_fact_filter.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_feed_reader_PRODUCTION.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_feed_reader_WORKING.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_fifth_dgm_orchestrator.psychology_patched.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_fifth_dgm_orchestrator.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_fractal_consciousness_FIXED.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_fractal_consciousness.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvisfractalconsciousness.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_fractal_dgm_woah.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_full_neurobio_chat.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_fully_autonomous_coordinator.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvis_gateway_v2_final.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvis_gateway_with_judge_filtering.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_generate_frontend.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_geo_tracker_simple.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_geo_ueid_integration.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_gis_enhanced_chat.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_gis_georeferencing_sync_FIXED.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_gis_georeferencing_sync_FIXED_V2.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_gis_georeferencing_sync.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_gis_query_service_backup.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_gis_query_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_gis_query_with_bbb_gisgeodb.psychology_patched.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_gis_query_with_bbb_gisgeodb.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_i_containers_FIXED.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvis_icontainers.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_i_containers_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvisicontainersservice.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_id_ocr_processor.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_integration_hub.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_layer2_dgm.psychology_patched.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_layer2_dgm.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_layer2_woah.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_link_reader_scheduled_FIXED.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_link_reader_scheduled.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_llm_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_llm_bridge_simple.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_local_resources_api.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_location_services.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_main_gateway_8000.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_main_gateway.backup_1762220815.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_main_gateway.backup_error.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_main_gateway.backup_test.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_main_gateway.broken_final.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_main_gateway.error_final.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_main_gateway.pre_fix.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_main_gateway.proxy_backup.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_main_gateway.proxy_final.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_main_gateway.proxy_still_broken.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_main_gateway.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvismaingateway.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_main_gateway.py.30endpoints_backup.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_main_gateway.py.full_backup_1762223304.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_memory_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_messenger_ui_final.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_messenger_ui_fixed.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_messenger_ui.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_metadata_aware_learner.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_microsoft_integration_FIXED.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_microsoft_integration.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_mother_carrie_protocols.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_mountainshares_integration.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_neurobiological_master.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_paddleocr_processor.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_phi_probe.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvis_ports_runtime.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvis_processes_runtime.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_production_chat_BACKUP.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_production_chat_BEFORE_GIS.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_production_chat.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_psychology_services.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_qualia_engine.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_rag_server.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvisragserver_wvpatch.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvisragserverwvpatch.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_ram_watchdog.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvis-rebuild-nbb_blood_brain_barrier-1_ms_jarvis_consciousness_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvis-rebuild-nbb_consciousness_containers-1_main.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvis-rebuild-nbb_heteroglobulin_transport-1_main.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvis-rebuild-nbb_i_containers-1_ms_jarvis_consciousness_unified_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvis-rebuild-nbb_mother_carrie_protocols-1_main.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvis-rebuild-nbb_pituitary_gland-1_main.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvis-rebuild-nbb_prefrontal_cortex-1_main.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvis-rebuild-nbb_qualia_engine-1_ms_jarvis_consciousness_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvis-rebuild-nbb_spiritual_maternal_integration-1_main.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvis-rebuild-nbb_spiritual_root-1_main.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvis-rebuild-nbb_subconscious-1_main.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvis-rebuild-nbb_woah_algorithms-1_service_discovery.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_seamless_monitor.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvis_semaphore.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_service_factory.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_showcase_api.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_silent_geo_tracker.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_simple_web_ui.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_spiritual_services.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_substack_reader.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_swap_memory_manager.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_swarm_intelligence.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_sync_monitor.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_temporal_consciousness.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_theological_integration.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_toroidal_consciousness.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvistoroidalconsciousness.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_truth_filter_gisgeodb.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_ueid_system.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_ueid_wallet_integration.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/MS_JARVIS_ULTIMATE_AUDIT_20251010_002719.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_unified_gateway.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvis_unified_gateway.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvisunifiedgateway.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_unified_gateway_v4.3.20251124.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_unified_gateway_v4.3.backup.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_unified_gateway_v4.3.pre_manifest.backup.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_unified_gateway_v4.3.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_unified_rag_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_unified_swagger_gateway_BACKUP.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_unified_swagger_gateway_CLEAN.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_unified_swagger_gateway_COMPLETE.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_unified_swagger_gateway_FINAL.psychology_patched.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_unified_swagger_gateway_FINAL.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvisunifiedswaggergatewayFINAL.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_unified_swagger_gateway_FIXED.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvisunifiedswaggergatewayFIXED.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_unified_swagger_gateway_PROD.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_unified_swagger_gateway.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvisunifiedswaggergateway.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_unified_swagger_gateway_SECURED.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_venv_scheduler_FIXED.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_venv_scheduler.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_venv_scheduler_SIMPLE.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_web_deployer_old.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_web_deployer.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_web_research_aggregate.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_web_research_aggregate.safe.20260119-094221.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_web_research_fixed.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_web_research.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_web_research_simple.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_web_research_v2.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_woah_algorithms_enhanced.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_jarvis_woah_algorithms.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvis_woah_algorithms.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvis_woah_algorithms_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvis_woah_runner.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/msjarvis_wv_entangled_gateway.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_mountainshares_analytics.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_mountainshares_coordinator.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ms_mountainshares_indexer.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/multi_model_consensus.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/multi_rag_dgm_system.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/my_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/nbb_darwin_godel_machines_msjarvis-rebuild-nbb_spiritual_root-1_main.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/nbb_darwin_godel_machines.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neuro_adapter.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/blood_brain_barrier/ethical_filter.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/blood_brain_barrier/__init__.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/blood_brain_barrier/safety_monitor.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/blood_brain_barrier/spiritual_filter.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/consciousness_bridge/service/consciousness_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/consciousness_containers/service/consciousness_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/consciousness_containers/service/dynamic_port_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/consciousness_containers/service/requirements.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/heteroglobulin_transport/service/consciousness_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/heteroglobulin_transport/service/dynamic_port_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/heteroglobulin_transport/service/requirements.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/i_containers/i_container_1/ego_boundaries/core.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/i_containers/i_container_1/ego_boundaries/__init__.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/i_containers/i_container_1/ego_boundaries.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/i_containers/i_container_1/identity_core.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/i_containers/i_container_1/__init__.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/i_containers/i_container_1/memory_self.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/i_containers/i_container_1/personal_narrative.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/i_containers/i_container_1/self_recognition.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/i_containers/i_container_2/__init__.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/i_containers/i_container_2/introspection_engine.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/i_containers/i_container_2/metacognitive_awareness.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/i_containers/i_container_2/observer_self.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/i_containers/i_container_2/reflection_system.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/i_containers/i_container_2/witness_consciousness.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/i_containers/__init__.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/i_containers/service/consciousness_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/i_containers/service/dynamic_port_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/i_containers/service/requirements.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/i_containers/service/service_discovery.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/i_containers/service/service_registry_client.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/__init__.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/mother_carrie_protocols/service/bootstrap_with_flask.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/mother_carrie_protocols/service/consciousness_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/mother_carrie_protocols/service/dynamic_port_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/mother_carrie_protocols/service/entrypoint_with_flask.sh
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/mother_carrie_protocols/service/requirements.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/neurobiological_brain/__init__.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/neurobiological_brain/qualia_engine/emotional_resonance/emotional_resonance.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/neurobiological_brain/qualia_engine/emotional_resonance/__init__.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/neurobiological_brain/qualia_engine/experience_generator/experience_generator.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/neurobiological_brain/qualia_engine/experience_generator/__init__.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/neurobiological_brain/qualia_engine/__init__.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/neurobiological_brain/qualia_engine/meaning_maker/__init__.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/neurobiological_brain/qualia_engine/meaning_maker/meaning_maker.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/pituitary_gland/service/consciousness_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/pituitary_gland/service/dynamic_port_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/pituitary_gland/service/requirements.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/prefrontal_cortex/service/consciousness_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/prefrontal_cortex/service/dynamic_port_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/prefrontal_cortex/service/requirements.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/prefrontal_cortex/service/service_discovery.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/prefrontal_cortex/service/service_registry_client.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/requirements.nbb.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/spiritual_maternal_integration/service/consciousness_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/spiritual_maternal_integration/service/dynamic_port_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/spiritual_maternal_integration/service/requirements.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/spiritual_root/service/consciousness_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/spiritual_root/service/dynamic_port_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/spiritual_root/service/requirements.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/subconscious/service/consciousness_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/subconscious/service/dynamic_port_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/subconscious/service/requirements.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/woah_algorithms/service/consciousness_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/woah_algorithms/service/dynamic_port_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiologicalbrain/woah_algorithms/service/requirements.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neurobiological_integration.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neuro_blood_brain_barrier.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neuro_consciousness_containers.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neuro_i_containers.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neuro_master_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neuro_prefrontal_cortex.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neuro_qualia_engine.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/neuro_subconscious.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/npm-packages.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/oauth2_callback.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/oauth2_handler.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ollama_fix.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/open_ports_full.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/open_ports.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/optimized_timeouts.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/optimize_egeria_complete.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/optimize_models_for_vram.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/override_launcher.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/paired_services.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/parallel_processing.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/parse_world_files.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/patch_agent_identity.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/patch_autonomous_learner_gisgeodb.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/patch_fractal.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/patch_learner_clean.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/patch_mother_persona.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/patch_neuro.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/patch_qualia.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/performance_optimization_analyzer.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/persona_fix.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/phase1_integration.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/phase2_integration.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/phase3_integration.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/phase4_5_integration.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/phase6_integration.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/phase7_integration.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/pia_sampler/pia_sampler_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/pid_code_backtrace.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/pid_dir_map.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/pid_port_map.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/pituitary_gland.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/polling_client.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/populate_redetermination_tracker.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/populate_security_layers_test.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/port_9000_69dgm_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/port_9000_academic_extension.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/port_9000_chat_wrapper_69dgm.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/port_9001_ARCHITECTURE_CORRECT.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/port_9001_FINAL_FIX.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/port_9001_FINAL_WORKING.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/port_9001_proxy_simple.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/port_9001_ui_DIRECT.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/port_9001_ui_FIXED.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/port_9001_ui_MYSQL_PROD.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/port_9001_ui_MYSQL.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/port_9001_ui_WITH_CONVERSATIONS.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/port_9001_ui_WORKING.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/port_9001_ui_wrapper.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/PORT_AUDIT_RAW.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/port_manager_fixed.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/port_manager.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ports_diff_msjarvis.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/port_service_audit.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/PORTS_REGISTRY_RAW.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/probe_services.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/process_comprehensive_gis.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/process_gis_shapefiles.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/process_statewide_gis_bulk.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/PRODUCTION_STATUS_REPORT.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/profile_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/pronoun_fixer.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/proxy_8060.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/psychological_rag_domain_psychological_rag_domain.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/psychological_rag_domain.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/psychology_integration_adapter.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/psychology_loop_closer.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/public_form_simplified.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/python_commands.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/python_ports.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/qualia_adapter.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/qualia_email_registration_orchestrator_69dgm.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/qualia_unified_orchestrator_69dgm_ACTIVE.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/qualia_unified_orchestrator_69dgm.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/qualia_unified_orchestrator_69dgm_REAL.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/qualia_unified_write_orchestrator_69dgm.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/quantum_dashboard.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/quantum_insight_llm.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/quantum_state_engine.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/query_benefits_system.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/query_imm_and_programs.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/quick_optimizations.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/rag_5100_ensemble_fast.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/rag_5100_ensemble.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/rag_5100_final.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/rag_client.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/rag_command_module.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/rag_direct_debug.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/rag_evidence_aggregator.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/rag_first_workflow.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/rag_general.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/rag_geospatial_context.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/rag_geospatial.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/rag_grounded_v2.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/rag_heartbeat_monitor.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/rag_local_resources.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/rag_query_router.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/rag_server_main.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/rag_server_min.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/rag_server.psychology_patched.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/rag_server.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/rag_simple.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/rag_temporal_heartbeat.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/rag_temporal.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/rag_to_gis_sync.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/rag_topic_router.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/rag_workflow.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/real_services_clean.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/real_services_detected.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/real_services_final.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/real_services_prod.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/real_services.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/rebuild_query_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/recover_160_queries.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/recover_chromadb_FIXED.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/recover_chromadb_to_gisgeodb.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/redirect_4015_to_4020.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/REFERENCE_windows_swarm.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/register_agents_from_csv.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/register_agents_from_csv_strict.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/register_hilbert_services.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/register_services.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/register_to_hilbert_chromadb.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/registration_biometric_production_final.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/registration_service_clean.backup_1762220206.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/registration_service_clean.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/reload_all_knowledge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/remaining_services.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/remove_duplicate_inits.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/replace_dolphin_phi.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/requirements-freeze.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/requirements_gbim.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/requirements-list.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/requirements-rag.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/requirements_semaphore.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/requirements_temporal.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/requirements_toroidal.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/requirements.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/response_filter.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/response_sanitizer.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/rest_endpoints.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/RESTORATION_CERTIFICATE_CORRECTED.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/RESTORATION_CERTIFICATE.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/restore_pia_wiring.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/resume_ingest_gbim_to_chroma.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/resume_sync_wvgistc_buildings.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/retrieval_router.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/retrieval_spiritual.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/roche_llm.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/roche_llm.stub.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/route_declarations_clean.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/route_declarations_raw.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/rpm-list.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/run_autonomous_learner_once.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/run_gateway_with_guards.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/running_python_services.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/safe_ingest_gbim_to_chroma.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/safe_integration.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/safety_monitor.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/sanctuary_construction_monitor_gateway.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/sanctuary_construction_monitor.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/schema_aware_topic_planner.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/schema_registry.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/search_metadata.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/seed_spatial_identity.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/service_api_check.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/service_api_report.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/service_discovery_glassbox.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/service_discovery.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/service_http_check.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/service_pid_directory_map.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/service_registry_client.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/services_list.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/services_msjarvisunifiedgatewayv4_3.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/set_intelligent_accuracy_scores.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/settings_snippet.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/silence_memory_errors.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/simple_orchestrator_fix.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/simple_prompt_fix.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/smart_auto_store.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/spiritual_filter.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/spiritual_rag_domain.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/stage2_biometric_backup.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/stage2_biometric.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/stakeholder_health_access_tests.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/stakeholder_health_access_tests_v2.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/start_facebook_4021.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/start_gateway_with_guards.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/substack_rss_reader.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/summarize_docs.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/swagger_chat_integration.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/swagger_gateway_FIXED.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/swagger_gateway.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/swarm_intelligence_main.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/swarm_watchdog.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/switch_to_small_models.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/sync_geodb_to_chromadb.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/sync_health_access_to_chromadb.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/SYSTEM_AUDIT_20251009_233918.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/system_dashboard.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/tag_quantum_gbim.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/talk_to_jarvis.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/temporal_consciousness.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/test_aacpe_features.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/test_aapcappe_corpus.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/test_aapcappe_retrieval.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/test_chroma_client.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/test_chromadb_heartbeat.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/test_chromadb_v2_heartbeat.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/test_ddg_verbose.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/test_end_to_end_woah_fifthdgm.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/test_fifth_dgm_integration.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/test_full_brain_integration.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/test_gbim_llm_summary.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/test_gbim_semantic_query.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/test_geodb_llm_summary.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/test_gis_chat.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/test_health_access_gbim.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/test_imm_query.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/test_knowledge_base.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/test_method_tracking.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/test_multi_collection_query.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/test.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/test_rag.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/test_retrieval_endpoint.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/test_spatial_awareness.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/threat_detection.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/topic_entanglement.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/toroidal_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/trigger_entangled_assets.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/truly_unpaired_services.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/truth_filter_bbb_verification.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/truth_filter_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ultimate_chat_current.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ULTIMATE_PORT_AUDIT_20251010_094847.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/ultimate_web_orchestrator.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/unified_consciousness_gateway_PRODUCTION.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/unifiedconsciousnessgatewayPRODUCTION.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/unified_orchestrator.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/update_carrie_keywords.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/update_facebook_poster.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/update_gisgeodb_schema.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/update_production_to_v9.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/update_services_to_use_port_manager.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/update_theological_boundaries.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/update_web_chat.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/update_web_research_package.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/use_existing_models.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/user_auth_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/user_dashboard.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/use_reliable_models_only.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/vatican_scraper_service.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/vectorize_gis_to_chromadb.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/verify_and_document_system.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/verify_benefit_chroma_sync.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/WATCHDOG_LOG.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/web_chat_server.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/web_connectivity_analyzer.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/webhook_notifications.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/web_page_ingest.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/web_research_fail_tracker.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/web_research_main.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/web_research_proxy_8007.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/web_research.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/web_research_requirements.txt
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/website_deployment_manager.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/wire_layers_into_chat.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/wire_learner_to_gisgeodb.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/wire_qualia_to_port8001.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/woah_command_module.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/woah_metrics_router.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/woah_optimizer.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/woah_policy_update.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/woah_population_state.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/woah_qualia_bridge.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/working_full_pipeline_FINAL_CONSCIOUSNESS.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/working_full_pipeline.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/working_full_pipeline_WITH_SPATIAL_TEMPORAL.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/wv_gis_mass_downloader.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/wvu_ldap_auth.py
/home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/yarn-packages.txt
/home/cakidd/.local/lib/python3.12/site-packages/chromadb-1.5.5.dist-info/entry_points.txt
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/api/async_api.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/api/async_client.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/api/async_fastapi.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/api/base_http_client.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/api/client.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/api/collection_configuration.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/api/configuration.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/api/fastapi.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/api/functions.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/api/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/api/models/AsyncCollection.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/api/models/AttachedFunction.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/api/models/CollectionCommon.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/api/models/Collection.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/api/rust.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/api/segment.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/api/shared_system_client.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/api/types.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/app.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/auth/basic_authn/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/auth/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/auth/simple_rbac_authz/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/auth/utils/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/base_types.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/cli/cli.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/cli/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/cli/utils.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/config.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/db/base.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/db/impl/grpc/client.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/db/impl/grpc/server.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/db/impl/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/db/impl/sqlite_pool.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/db/impl/sqlite.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/db/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/db/migrations.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/db/mixins/embeddings_queue.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/db/mixins/sysdb.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/db/system.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/errors.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/execution/executor/abstract.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/execution/executor/distributed.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/execution/executor/local.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/execution/expression/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/execution/expression/operator.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/execution/expression/plan.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/execution/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/ingest/impl/utils.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/ingest/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/logservice/logservice.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/migrations/embeddings_queue/00001-embeddings.sqlite.sql
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/migrations/embeddings_queue/00002-embeddings-queue-config.sqlite.sql
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/migrations/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/migrations/metadb/00001-embedding-metadata.sqlite.sql
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/migrations/metadb/00002-embedding-metadata.sqlite.sql
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/migrations/metadb/00003-full-text-tokenize.sqlite.sql
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/migrations/metadb/00004-metadata-indices.sqlite.sql
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/migrations/metadb/00005-max-seq-id-int.sqlite.sql
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/migrations/sysdb/00001-collections.sqlite.sql
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/migrations/sysdb/00002-segments.sqlite.sql
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/migrations/sysdb/00003-collection-dimension.sqlite.sql
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/migrations/sysdb/00004-tenants-databases.sqlite.sql
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/migrations/sysdb/00005-remove-topic.sqlite.sql
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/migrations/sysdb/00006-collection-segment-metadata.sqlite.sql
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/migrations/sysdb/00007-collection-config.sqlite.sql
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/migrations/sysdb/00008-maintenance-log.sqlite.sql
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/migrations/sysdb/00009-segment-collection-not-null.sqlite.sql
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/proto/convert.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/proto/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/proto/utils.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/quota/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/quota/simple_quota_enforcer/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/rate_limit/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/rate_limit/simple_rate_limit/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb_rust_bindings/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/segment/distributed/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/segment/impl/distributed/segment_directory.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/segment/impl/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/segment/impl/manager/cache/cache.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/segment/impl/manager/cache/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/segment/impl/manager/distributed.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/segment/impl/manager/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/segment/impl/manager/local.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/segment/impl/metadata/sqlite.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/segment/impl/vector/batch.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/segment/impl/vector/brute_force_index.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/segment/impl/vector/hnsw_params.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/segment/impl/vector/local_hnsw.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/segment/impl/vector/local_persistent_hnsw.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/segment/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/serde.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/server/fastapi/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/server/fastapi/types.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/server/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/telemetry/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/telemetry/opentelemetry/fastapi.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/telemetry/opentelemetry/grpc.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/telemetry/opentelemetry/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/telemetry/product/events.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/telemetry/product/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/telemetry/product/posthog.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/telemetry/README.md
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/api/test_collection.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/api/test_count_api.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/api/test_delete_database.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/api/test_get_database.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/api/test_indexing_status.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/api/test_invalid_update.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/api/test_limit_offset.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/api/test_list_databases.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/api/test_numpy_list_inputs.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/api/test_schema_e2e.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/api/test_schema.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/api/test_search_api.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/api/test_shared_system_client.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/api/test_types.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/auth/test_auth_utils.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/auth/test_rbac_authz.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/client/create_http_client_with_basic_auth.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/client/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/client/test_create_http_client.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/client/test_database_tenant_auth.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/client/test_database_tenant.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/client/test_multiple_clients_concurrency.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/configurations/test_collection_configuration.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/configurations/test_configurations.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/conftest.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/data_loader/test_data_loader.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/db/test_log_purge.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/distributed/README.md
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/distributed/test_log_backpressure.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/distributed/test_repair_collection_log_offset.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/distributed/test_reroute.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/distributed/test_sanity.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/distributed/test_statistics_wrapper.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/distributed/test_task_api.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/ef/test_chroma_bm25_embedding_function.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/ef/test_custom_ef.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/ef/test_default_ef.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/ef/test_ef.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/ef/test_morph_ef.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/ef/test_multimodal_ef.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/ef/test_ollama_ef.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/ef/test_onnx_mini_lm_l6_v2.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/ef/test_openai_ef.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/ef/test_voyageai_ef.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/property/invariants.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/property/strategies.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/property/test_add.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/property/test_base64_conversion.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/property/test_client_url.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/property/test_collections.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/property/test_collections_with_database_tenant_overwrite.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/property/test_collections_with_database_tenant.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/property/test_cross_version_persist.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/property/test_embeddings.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/property/test_filtering.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/property/test_fork.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/property/test_persist.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/property/test_restart_persist.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/property/test_schema.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/segment/distributed/test_memberlist_provider.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/segment/distributed/test_rendezvous_hash.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/stress/test_many_collections.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/test_api.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/test_chroma.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/test_client.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/test_cli.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/test_config.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/test_multithreaded.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/utils/cross_version.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/utils/distance_functions.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/utils/test_embedding_function_schemas.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/utils/test_result_df_transform.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/test/utils/wait_for_version_increase.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/types.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/async_to_sync.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/batch_utils.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/data_loaders.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/delete_file.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/directory.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/distance_functions.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/amazon_bedrock_embedding_function.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/baseten_embedding_function.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/bm25_embedding_function.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_bm25_embedding_function.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_cloud_qwen_embedding_function.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_cloud_splade_embedding_function.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_langchain_embedding_function.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/cloudflare_workers_ai_embedding_function.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/cohere_embedding_function.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/fastembed_sparse_embedding_function.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/google_embedding_function.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/huggingface_embedding_function.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/huggingface_sparse_embedding_function.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/instructor_embedding_function.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/jina_embedding_function.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/mistral_embedding_function.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/morph_embedding_function.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/nomic_embedding_function.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/ollama_embedding_function.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/onnx_mini_lm_l6_v2.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/openai_embedding_function.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/open_clip_embedding_function.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/perplexity_embedding_function.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/roboflow_embedding_function.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/schemas/bm25_tokenizer.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/schemas/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/schemas/README.md
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/schemas/registry.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/schemas/schema_utils.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/sentence_transformer_embedding_function.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/text2vec_embedding_function.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/together_ai_embedding_function.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/utils.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/embedding_functions/voyageai_embedding_function.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/fastapi.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/lru_cache.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/messageid.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/read_write_lock.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/rendezvous_hash.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/results.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/sparse_embedding_utils.py
/home/cakidd/.local/lib/python3.12/site-packages/chromadb/utils/statistics.py
/home/cakidd/.local/lib/python3.12/site-packages/cuda/bindings/_lib/cyruntime/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/fsspec/registry.py
/home/cakidd/.local/lib/python3.12/site-packages/google/protobuf/runtime_version.py
/home/cakidd/.local/lib/python3.12/site-packages/google/protobuf/timestamp_pb2.py
/home/cakidd/.local/lib/python3.12/site-packages/google/protobuf/timestamp.py
/home/cakidd/.local/lib/python3.12/site-packages/google/type/datetime_pb2.py
/home/cakidd/.local/lib/python3.12/site-packages/google/type/timeofday_pb2.py
/home/cakidd/.local/lib/python3.12/site-packages/grpc/_runtime_protos.py
/home/cakidd/.local/lib/python3.12/site-packages/huggingface_hub/_snapshot_download.py
/home/cakidd/.local/lib/python3.12/site-packages/huggingface_hub/utils/_datetime.py
/home/cakidd/.local/lib/python3.12/site-packages/huggingface_hub/utils/_runtime.py
/home/cakidd/.local/lib/python3.12/site-packages/jsonschema/benchmarks/unused_registry.py
/home/cakidd/.local/lib/python3.12/site-packages/kubernetes/client/models/v1_node_runtime_handler_features.py
/home/cakidd/.local/lib/python3.12/site-packages/kubernetes/client/models/v1_node_runtime_handler.py
/home/cakidd/.local/lib/python3.12/site-packages/kubernetes/client/models/v1_runtime_class_list.py
/home/cakidd/.local/lib/python3.12/site-packages/kubernetes/client/models/v1_runtime_class.py
/home/cakidd/.local/lib/python3.12/site-packages/networkx/algorithms/isomorphism/temporalisomorphvf2.py
/home/cakidd/.local/lib/python3.12/site-packages/networkx/algorithms/isomorphism/tests/test_temporalisomorphvf2.py
/home/cakidd/.local/lib/python3.12/site-packages/networkx/algorithms/tests/test_time_dependent.py
/home/cakidd/.local/lib/python3.12/site-packages/networkx/algorithms/time_dependent.py
/home/cakidd/.local/lib/python3.12/site-packages/networkx/generators/tests/test_time_series.py
/home/cakidd/.local/lib/python3.12/site-packages/networkx/generators/time_series.py
/home/cakidd/.local/lib/python3.12/site-packages/nvidia_cuda_runtime_cu12-12.8.90.dist-info/License.txt
/home/cakidd/.local/lib/python3.12/site-packages/nvidia_cuda_runtime_cu12-12.8.90.dist-info/top_level.txt
/home/cakidd/.local/lib/python3.12/site-packages/nvidia/cuda_runtime/include/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/nvidia/cuda_runtime/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/nvidia/cuda_runtime/lib/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime-1.24.4.dist-info/entry_points.txt
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime-1.24.4.dist-info/top_level.txt
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/backend/backend.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/backend/backend_rep.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/backend/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/capi/build_and_package_info.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/capi/convert_npz_to_onnx_adapter.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/capi/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/capi/_ld_preload.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/capi/onnxruntime_collect_build_info.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/capi/onnxruntime_inference_collection.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/capi/onnxruntime_validation.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/capi/_pybind_state.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/datasets/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/Privacy.md
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/base_quantizer.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/calibrate.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/CalTableFlatBuffers/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/CalTableFlatBuffers/KeyValue.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/CalTableFlatBuffers/TrtTable.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/execution_providers/qnn/fusion_lpnorm.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/execution_providers/qnn/fusion_spacetodepth.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/execution_providers/qnn/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/execution_providers/qnn/mixed_precision_overrides_utils.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/execution_providers/qnn/preprocess.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/execution_providers/qnn/quant_config.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/fusions/fusion_gelu.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/fusions/fusion_layernorm.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/fusions/fusion.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/fusions/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/fusions/replace_upsample_with_resize.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/matmul_bnb4_quantizer.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/matmul_nbits_quantizer.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/neural_compressor/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/neural_compressor/onnx_model.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/neural_compressor/util.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/neural_compressor/weight_only.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/onnx_model.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/onnx_quantizer.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/operators/activation.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/operators/argmax.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/operators/attention.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/operators/base_operator.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/operators/binary_op.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/operators/concat.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/operators/conv.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/operators/direct_q8.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/operators/embed_layernorm.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/operators/gather.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/operators/gavgpool.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/operators/gemm.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/operators/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/operators/lstm.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/operators/matmul.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/operators/maxpool.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/operators/norm.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/operators/pad.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/operators/pooling.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/operators/qdq_base_operator.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/operators/resize.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/operators/softmax.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/operators/split.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/operators/where.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/preprocess.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/qdq_loss_debug.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/qdq_quantizer.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/quantize.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/quant_utils.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/registry.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/shape_inference.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/static_quantize_runner.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/quantization/tensor_quant_overrides.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/ThirdPartyNotices.txt
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/check_onnx_model_mobile_usability.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/convert_onnx_models_to_ort.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/file_utils.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/logger.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/make_dynamic_shape_fixed.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/mobile_helpers/coreml_supported_mlprogram_ops.md
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/mobile_helpers/coreml_supported_neuralnetwork_ops.md
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/mobile_helpers/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/mobile_helpers/nnapi_supported_ops.md
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/mobile_helpers/usability_checker.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/offline_tuning.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/onnx_model_utils.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/onnx_randomizer.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/onnxruntime_test.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/optimize_onnx_model.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/operator_type_usage_processors.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/ArgTypeAndIndex.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/ArgType.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/Attribute.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/AttributeType.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/Checkpoint.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/DeprecatedKernelCreateInfos.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/DeprecatedNodeIndexAndKernelDefHash.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/DeprecatedSessionState.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/DeprecatedSubGraphSessionState.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/Dimension.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/DimensionValue.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/DimensionValueType.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/EdgeEnd.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/FloatProperty.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/Graph.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/InferenceSession.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/IntProperty.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/KernelTypeStrArgsEntry.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/KernelTypeStrResolver.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/MapType.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/Model.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/ModuleState.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/NodeEdge.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/Node.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/NodesToOptimizeIndices.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/NodeType.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/OperatorSetId.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/OpIdKernelTypeStrArgsEntry.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/OptimizerGroup.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/ParameterOptimizerState.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/PropertyBag.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/RuntimeOptimizationRecordContainerEntry.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/RuntimeOptimizationRecord.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/RuntimeOptimizations.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/SequenceType.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/Shape.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/SparseTensor.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/StringProperty.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/StringStringEntry.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/TensorDataType.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/Tensor.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/TensorTypeAndShape.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/TypeInfo.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/TypeInfoValue.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/ValueInfo.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_model_processor.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/types.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/utils.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/pytorch_export_contrib_ops.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/pytorch_export_helpers.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/qdq_helpers/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/qdq_helpers/optimize_qdq_model.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/qnn/add_trans_cast.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/qnn/gen_qnn_ctx_onnx_model.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/qnn/preprocess.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/reduced_build_config_parser.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/remove_initializer_from_input.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/symbolic_shape_infer.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/tools/update_onnx_opset.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/affinity_helper.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/benchmark_helper.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/benchmark.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/bert_perf_test.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/bert_test_data.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/compare_bert_results.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/constants.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/convert_generation.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/convert_tf_models_to_pytorch.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/convert_to_packing_mode.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/dynamo_onnx_helper.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/float16.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_attention_clip.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_attention.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_attention_sam2.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_attention_unet.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_attention_vae.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_bart_attention.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_base.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_bias_add.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_biasgelu.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_biassplitgelu.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_conformer_attention.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_constant_fold.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_embedlayer.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_fastgelu.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_gelu_approximation.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_gelu.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_gemmfastgelu.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_gpt_attention_megatron.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_gpt_attention_no_past.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_gpt_attention.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_group_norm.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_layernorm.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_mha_mmdit.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_nhwc_conv.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_options.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_qordered_attention.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_qordered_gelu.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_qordered_layernorm.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_qordered_matmul.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_quickgelu.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_reshape.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_rotary_attention.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_shape.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_simplified_layernorm.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_skip_group_norm.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_skiplayernorm.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_transpose.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/fusion_utils.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/huggingface_models.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/import_utils.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/io_binding_helper.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/large_model_exporter.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/machine_info.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/metrics.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/bart/export.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/bart/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/bert/eval_squad.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/bert/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/gpt2/benchmark_gpt2.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/gpt2/convert_to_onnx.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/gpt2/gpt2_helper.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/gpt2/gpt2_parity.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/gpt2/gpt2_tester.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/gpt2/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/gpt2/parity_check_helper.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/llama/benchmark_all.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/llama/benchmark_e2e.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/llama/benchmark.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/llama/convert_to_onnx.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/llama/dist_settings.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/llama/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/llama/llama_inputs.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/llama/llama_parity.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/llama/llama_torch.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/llama/quant_kv_dataloader.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/longformer/benchmark_longformer.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/longformer/convert_to_onnx.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/longformer/generate_test_data.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/longformer/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/longformer/longformer_helper.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/phi2/convert_to_onnx.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/phi2/inference_example.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/phi2/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/sam2/benchmark_sam2.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/sam2/convert_to_onnx.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/sam2/image_decoder.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/sam2/image_encoder.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/sam2/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/sam2/mask_decoder.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/sam2/nvtx_helper.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/sam2/prompt_encoder.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/sam2/sam2_demo.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/sam2/sam2_image_onnx_predictor.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/sam2/sam2_utils.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/benchmark_controlnet.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/benchmark.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/demo_txt2img.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/demo_txt2img_xl.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/demo_utils.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/diffusion_models.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/diffusion_schedulers.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/engine_builder_ort_cuda.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/engine_builder_ort_trt.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/engine_builder.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/engine_builder_tensorrt.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/engine_builder_torch.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/optimize_pipeline.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/ort_optimizer.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/pipeline_stable_diffusion.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/trt_utilities.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/t5/convert_to_onnx.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/t5/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/t5/t5_decoder.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/t5/t5_encoder_decoder_init.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/t5/t5_encoder.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/t5/t5_helper.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/whisper/benchmark_all.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/whisper/benchmark.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/whisper/convert_to_onnx.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/whisper/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/whisper/whisper_chain.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/whisper/whisper_decoder.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/whisper/whisper_encoder_decoder_init.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/whisper/whisper_encoder.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/whisper/whisper_helper.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/whisper/whisper_inputs.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/models/whisper/whisper_jump_times.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/onnx_exporter.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/onnx_model_bart.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/onnx_model_bert_keras.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/onnx_model_bert.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/onnx_model_bert_tf.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/onnx_model_clip.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/onnx_model_conformer.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/onnx_model_gpt2.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/onnx_model_mmdit.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/onnx_model_phi.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/onnx_model.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/onnx_model_sam2.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/onnx_model_t5.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/onnx_model_tnlr.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/onnx_model_unet.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/onnx_model_vae.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/onnx_utils.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/optimizer.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/past_helper.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/profile_result_processor.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/profiler.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/quantize_helper.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/shape_infer_helper.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/shape_optimizer.py
/home/cakidd/.local/lib/python3.12/site-packages/onnxruntime/transformers/torch_onnx_export_helper.py
/home/cakidd/.local/lib/python3.12/site-packages/pydantic/datetime_parse.py
/home/cakidd/.local/lib/python3.12/site-packages/pydantic/v1/datetime_parse.py
/home/cakidd/.local/lib/python3.12/site-packages/pypika/clickhouse/dates_and_times.py
/home/cakidd/.local/lib/python3.12/site-packages/redis/commands/timeseries/commands.py
/home/cakidd/.local/lib/python3.12/site-packages/redis/commands/timeseries/info.py
/home/cakidd/.local/lib/python3.12/site-packages/redis/commands/timeseries/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/redis/commands/timeseries/utils.py
/home/cakidd/.local/lib/python3.12/site-packages/redis/observability/registry.py
/home/cakidd/.local/lib/python3.12/site-packages/scipy/datasets/_registry.py
/home/cakidd/.local/lib/python3.12/site-packages/scipy/signal/_short_time_fft.py
/home/cakidd/.local/lib/python3.12/site-packages/scipy/signal/tests/test_short_time_fft.py
/home/cakidd/.local/lib/python3.12/site-packages/sympy/physics/quantum/hilbert.py
/home/cakidd/.local/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_hilbert.py
/home/cakidd/.local/lib/python3.12/site-packages/sympy/physics/units/systems/length_weight_time.py
/home/cakidd/.local/lib/python3.12/site-packages/sympy/utilities/tests/test_timeutils.py
/home/cakidd/.local/lib/python3.12/site-packages/sympy/utilities/timeutils.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/distributed/elastic/rendezvous/registry.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/distributed/elastic/timer/api.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/distributed/elastic/timer/debug_info_logging.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/distributed/elastic/timer/file_based_local_timer.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/distributed/elastic/timer/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/distributed/elastic/timer/local_timer.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/distributed/fsdp/_runtime_utils.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/distributed/rpc/backend_registry.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/distributed/rpc/_testing/faulty_agent_backend_registry.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/distributed/_shard/op_registry_utils.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/distributed/_tools/runtime_estimator.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/distributions/constraint_registry.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_dynamo/backends/registry.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_dynamo/comptime.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_export/passes/add_runtime_assertions_for_constraints_pass.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_export/passes/remove_runtime_assertions.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_functorch/_aot_autograd/runtime_wrappers.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/fx/passes/runtime_assert.py
/home/cakidd/.local/lib/python3.12/site-packages/torchgen/static_runtime/config.py
/home/cakidd/.local/lib/python3.12/site-packages/torchgen/static_runtime/generator.py
/home/cakidd/.local/lib/python3.12/site-packages/torchgen/static_runtime/gen_static_runtime_ops.py
/home/cakidd/.local/lib/python3.12/site-packages/torchgen/static_runtime/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_inductor/compile_worker/timer.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_inductor/fx_passes/node_runtime_estimation.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_inductor/runtime/autotune_cache.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_inductor/runtime/benchmarking.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_inductor/runtime/cache_dir_utils.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_inductor/runtime/caching/config.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_inductor/runtime/caching/context.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_inductor/runtime/caching/exceptions.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_inductor/runtime/caching/implementations.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_inductor/runtime/caching/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_inductor/runtime/caching/interfaces.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_inductor/runtime/caching/locks.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_inductor/runtime/caching/utils.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_inductor/runtime/compile_tasks.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_inductor/runtime/coordinate_descent_tuner.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_inductor/runtime/debug_utils.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_inductor/runtime/halide_helpers.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_inductor/runtime/hints.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_inductor/runtime/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_inductor/runtime/runtime_utils.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_inductor/runtime/static_cuda_launcher.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_inductor/runtime/triton_compat.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_inductor/runtime/triton_helpers.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_inductor/runtime/triton_heuristics.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_inductor/template_heuristics/registry.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_library/fake_class_registry.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_library/simple_registry.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/nn/attention/_registry.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/onnx/_internal/exporter/_torchlib/_torchlib_registry.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/_strobelight/compile_time_profiler.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/utils/benchmark/examples/simple_timeit.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/utils/benchmark/utils/timer.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/utils/benchmark/utils/valgrind_wrapper/timer_interface.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/utils/data/datapipes/utils/snapshot.py
/home/cakidd/.local/lib/python3.12/site-packages/torch/utils/_runtime_estimation.py
/home/cakidd/.local/lib/python3.12/site-packages/transformers/models/time_series_transformer/configuration_time_series_transformer.py
/home/cakidd/.local/lib/python3.12/site-packages/transformers/models/time_series_transformer/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/transformers/models/time_series_transformer/modeling_time_series_transformer.py
/home/cakidd/.local/lib/python3.12/site-packages/transformers/models/timesfm/configuration_timesfm.py
/home/cakidd/.local/lib/python3.12/site-packages/transformers/models/timesfm/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/transformers/models/timesfm/modeling_timesfm.py
/home/cakidd/.local/lib/python3.12/site-packages/transformers/models/timesfm/modular_timesfm.py
/home/cakidd/.local/lib/python3.12/site-packages/transformers/models/timesformer/configuration_timesformer.py
/home/cakidd/.local/lib/python3.12/site-packages/transformers/models/timesformer/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/transformers/models/timesformer/modeling_timesformer.py
/home/cakidd/.local/lib/python3.12/site-packages/transformers/models/voxtral_realtime/configuration_voxtral_realtime.py
/home/cakidd/.local/lib/python3.12/site-packages/transformers/models/voxtral_realtime/feature_extraction_voxtral_realtime.py
/home/cakidd/.local/lib/python3.12/site-packages/transformers/models/voxtral_realtime/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/transformers/models/voxtral_realtime/modeling_voxtral_realtime.py
/home/cakidd/.local/lib/python3.12/site-packages/transformers/models/voxtral_realtime/modular_voxtral_realtime.py
/home/cakidd/.local/lib/python3.12/site-packages/transformers/models/voxtral_realtime/processing_voxtral_realtime.py
/home/cakidd/.local/lib/python3.12/site-packages/transformers/time_series_utils.py
/home/cakidd/.local/lib/python3.12/site-packages/triton/experimental/gluon/_runtime.py
/home/cakidd/.local/lib/python3.12/site-packages/triton/runtime/_allocation.py
/home/cakidd/.local/lib/python3.12/site-packages/triton/runtime/_async_compile.py
/home/cakidd/.local/lib/python3.12/site-packages/triton/runtime/autotuner.py
/home/cakidd/.local/lib/python3.12/site-packages/triton/runtime/build.py
/home/cakidd/.local/lib/python3.12/site-packages/triton/runtime/cache.py
/home/cakidd/.local/lib/python3.12/site-packages/triton/runtime/driver.py
/home/cakidd/.local/lib/python3.12/site-packages/triton/runtime/errors.py
/home/cakidd/.local/lib/python3.12/site-packages/triton/runtime/__init__.py
/home/cakidd/.local/lib/python3.12/site-packages/triton/runtime/interpreter.py
/home/cakidd/.local/lib/python3.12/site-packages/triton/runtime/jit.py
/home/cakidd/.local/lib/python3.12/site-packages/websockets/asyncio/async_timeout.py
/home/cakidd/.local/share/Trash/files/timesheet_import(1).sql
/home/cakidd/.local/share/Trash/files/timesheet_import(2).sql
/home/cakidd/MountainShares-Commons/04-evidence/INFRASTRUCTURE_SNAPSHOT.md
/home/cakidd/MountainShares-Commons/04-evidence/scripts/msjarvis_audit_snapshot.sh
/home/cakidd/MountainShares-Commons/04-evidence/scripts/msjarvis_chroma_backup_verify.sh
/home/cakidd/MountainShares-Commons/04-evidence/snapshots/latest/port_map_canonical.txt
/home/cakidd/MountainShares-Commons/04-evidence/snapshots/README.md
/home/cakidd/msallis-chroma-collection-names.txt
/home/cakidd/msallis-focus/live-persona-hits.txt
/home/cakidd/msallis-focus/opt-persona-files.txt
/home/cakidd/msallis-focus/opt-persona-hits.txt
/home/cakidd/msallis-focus/opt-repo-persona-hits.txt
/home/cakidd/msallis-focus/patch_persona_opt.py
/home/cakidd/msallis-focus/persona_patch_confirmed.py
/home/cakidd/msallis-focus/persona_patch_exact.py
/home/cakidd/msjarvis-public-docs/discipline/Polymathmatic Geography: A Manifesto.md
/home/cakidd/msjarvis-public-docs/discipline/Polymathmatic Geography and the GeoBelief Information Model (GBIM.md
/home/cakidd/msjarvis-public-docs/docs/kidd_technical_services_detailed_timesheet_2025-2026.md
/home/cakidd/msjarvis-public-docs/docs/stack-snapshot-20260322-1447.md
/home/cakidd/msjarvis-public-docs/mountainshares-dao/smart-contracts-registry.md
/home/cakidd/msjarvis-public-docs/thesis/04-hilbert-space-state.md
/home/cakidd/msjarvis-public-docs/thesis/05-chromadb-semantic-memory.md
/home/cakidd/msjarvis-public-docs/thesis/26-temporal-toroidal-semaphore-structure.md
/home/cakidd/msjarvis-public-docs/thesis/46a-69DGM-Consciousness-Bridge-Implementation-Snapshot.md
/home/cakidd/msjarvis-public-docs/thesis/Hilbert People Space — Person-in-Context Without Surveillance.md
/home/cakidd/msjarvis-rebuild-working/msjarvis-rebuild/services/hilbert_spatial_chat.py
/home/cakidd/.nvm/versions/node/v22.23.1/lib/node_modules/npm/docs/content/commands/npm-publish.md
/home/cakidd/.nvm/versions/node/v22.23.1/lib/node_modules/npm/docs/content/commands/npm-unpublish.md
/home/cakidd/.nvm/versions/node/v22.23.1/lib/node_modules/npm/docs/content/using-npm/registry.md
/home/cakidd/.nvm/versions/node/v22.23.1/lib/node_modules/npm/node_modules/libnpmpublish/README.md
/home/cakidd/.nvm/versions/node/v22.23.1/lib/node_modules/npm/node_modules/npm-pick-manifest/LICENSE.md
/home/cakidd/.nvm/versions/node/v22.23.1/lib/node_modules/npm/node_modules/npm-registry-fetch/LICENSE.md
/home/cakidd/publish_wv_blockgroups_v1.py
/home/cakidd/publish_wv_counties_v2.py
/home/cakidd/publish_wv_tracts_v2.py
/home/cakidd/publish_wv_tracts_v3.py
/home/cakidd/repos/normalization_work/output/chroma_collection_counts_after_hash_dedup.txt
/home/cakidd/repos/normalization_work/output/chroma_collection_counts.txt
/home/cakidd/repos/normalization_work/output/chroma_collection_names.txt
/home/cakidd/repos/normalization_work/output/redis_hilbert_keys_full.txt
/home/cakidd/repos/normalization_work/output/redis_hilbert_keys.txt
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/asgiref/timeout.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb-0.6.3.dist-info/entry_points.txt
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb-0.6.3.dist-info/top_level.txt
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/api/async_api.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/api/async_client.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/api/async_fastapi.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/api/base_http_client.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/api/client.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/api/configuration.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/api/fastapi.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/api/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/api/models/AsyncCollection.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/api/models/CollectionCommon.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/api/models/Collection.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/api/segment.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/api/shared_system_client.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/api/types.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/app.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/auth/basic_authn/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/auth/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/auth/simple_rbac_authz/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/auth/utils/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/cli/cli.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/cli/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/cli/utils.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/config.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/db/base.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/db/impl/grpc/client.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/db/impl/grpc/server.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/db/impl/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/db/impl/sqlite_pool.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/db/impl/sqlite.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/db/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/db/migrations.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/db/mixins/embeddings_queue.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/db/mixins/sysdb.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/db/system.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/errors.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/execution/executor/abstract.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/execution/executor/distributed.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/execution/executor/local.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/execution/expression/operator.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/execution/expression/plan.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/execution/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/ingest/impl/utils.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/ingest/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/logservice/logservice.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/migrations/embeddings_queue/00001-embeddings.sqlite.sql
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/migrations/embeddings_queue/00002-embeddings-queue-config.sqlite.sql
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/migrations/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/migrations/metadb/00001-embedding-metadata.sqlite.sql
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/migrations/metadb/00002-embedding-metadata.sqlite.sql
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/migrations/metadb/00003-full-text-tokenize.sqlite.sql
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/migrations/metadb/00004-metadata-indices.sqlite.sql
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/migrations/sysdb/00001-collections.sqlite.sql
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/migrations/sysdb/00002-segments.sqlite.sql
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/migrations/sysdb/00003-collection-dimension.sqlite.sql
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/migrations/sysdb/00004-tenants-databases.sqlite.sql
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/migrations/sysdb/00005-remove-topic.sqlite.sql
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/migrations/sysdb/00006-collection-segment-metadata.sqlite.sql
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/migrations/sysdb/00007-collection-config.sqlite.sql
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/migrations/sysdb/00008-maintenance-log.sqlite.sql
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/migrations/sysdb/00009-segment-collection-not-null.sqlite.sql
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/proto/convert.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/proto/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/proto/utils.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/quota/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/quota/simple_quota_enforcer/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/rate_limit/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/rate_limit/simple_rate_limit/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/segment/distributed/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/segment/impl/distributed/segment_directory.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/segment/impl/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/segment/impl/manager/cache/cache.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/segment/impl/manager/cache/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/segment/impl/manager/distributed.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/segment/impl/manager/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/segment/impl/manager/local.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/segment/impl/metadata/sqlite.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/segment/impl/vector/batch.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/segment/impl/vector/brute_force_index.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/segment/impl/vector/hnsw_params.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/segment/impl/vector/local_hnsw.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/segment/impl/vector/local_persistent_hnsw.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/segment/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/serde.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/server/fastapi/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/server/fastapi/types.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/server/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/telemetry/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/telemetry/opentelemetry/fastapi.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/telemetry/opentelemetry/grpc.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/telemetry/opentelemetry/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/telemetry/product/events.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/telemetry/product/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/telemetry/product/posthog.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/telemetry/README.md
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/api/test_collection.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/api/test_delete_database.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/api/test_get_database.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/api/test_limit_offset.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/api/test_list_databases.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/api/test_types.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/auth/rbac_test_executors.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/auth/strategies.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/auth/test_auth_utils.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/auth/test_base_class_behavior.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/auth/test_basic_authn.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/auth/test_simple_rbac_authz.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/auth/test_token_authn.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/cache/test_cache.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/client/create_http_client_with_basic_auth.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/client/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/client/test_create_http_client.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/client/test_database_tenant_auth.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/client/test_database_tenant.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/client/test_http_client_v1_compatability.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/client/test_multiple_clients_concurrency.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/configurations/test_configurations.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/conftest.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/data_loader/test_data_loader.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/db/migrations/00001-migration-1.psql.sql
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/db/migrations/00001-migration-1.sqlite.sql
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/db/migrations/00002-migration-2.psql.sql
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/db/migrations/00002-migration-2.sqlite.sql
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/db/migrations/00003-migration-3.psql.sql
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/db/migrations/00003-migration-3.sqlite.sql
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/db/migrations/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/db/test_base.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/db/test_hash.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/db/test_log_purge.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/db/test_migrations.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/db/test_system.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/distributed/README.md
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/distributed/test_reroute.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/distributed/test_sanity.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/ef/test_default_ef.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/ef/test_ef.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/ef/test_multimodal_ef.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/ef/test_ollama_ef.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/ef/test_openai_ef.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/ingest/test_producer_consumer.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/property/invariants.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/property/strategies.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/property/test_add.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/property/test_client_url.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/property/test_collections.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/property/test_collections_with_database_tenant_overwrite.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/property/test_collections_with_database_tenant.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/property/test_cross_version_persist.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/property/test_embeddings.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/property/test_filtering.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/property/test_persist.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/property/test_restart_persist.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/property/test_segment_manager.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/property/test_sysdb.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/proto/test_utils.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/segment/distributed/test_memberlist_provider.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/segment/distributed/test_protobuf_translation.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/segment/distributed/test_rendezvous_hash.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/segment/test_metadata.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/segment/test_vector.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/stress/test_many_collections.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/test_api.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/test_chroma.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/test_client.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/test_cli.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/test_config.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/test_logservice.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/test_multithreaded.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/utils/cross_version.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/utils/distance_functions.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/utils/test_messagid.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/test/utils/wait_for_version_increase.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/types.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/utils/async_to_sync.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/utils/batch_utils.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/utils/data_loaders.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/utils/delete_file.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/utils/directory.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/utils/distance_functions.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/utils/embedding_functions/amazon_bedrock_embedding_function.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_langchain_embedding_function.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/utils/embedding_functions/cohere_embedding_function.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/utils/embedding_functions/google_embedding_function.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/utils/embedding_functions/huggingface_embedding_function.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/utils/embedding_functions/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/utils/embedding_functions/instructor_embedding_function.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/utils/embedding_functions/jina_embedding_function.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/utils/embedding_functions/ollama_embedding_function.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/utils/embedding_functions/onnx_mini_lm_l6_v2.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/utils/embedding_functions/openai_embedding_function.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/utils/embedding_functions/open_clip_embedding_function.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/utils/embedding_functions/roboflow_embedding_function.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/utils/embedding_functions/sentence_transformer_embedding_function.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/utils/embedding_functions/text2vec_embedding_function.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/utils/embedding_functions/voyageai_embedding_function.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/utils/fastapi.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/utils/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/utils/lru_cache.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/utils/messageid.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/utils/read_write_lock.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chromadb/utils/rendezvous_hash.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/chroma_hnswlib-0.7.6.dist-info/top_level.txt
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/fsspec/registry.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/google/protobuf/runtime_version.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/google/protobuf/timestamp_pb2.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/google/protobuf/timestamp.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/google/type/datetime_pb2.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/google/type/timeofday_pb2.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/grpc/_runtime_protos.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/huggingface_hub/_snapshot_download.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/huggingface_hub/utils/_datetime.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/huggingface_hub/utils/_runtime.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/itsdangerous/timed.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/jinja2/runtime.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/kubernetes/aio/client/models/v1_node_runtime_handler_features.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/kubernetes/aio/client/models/v1_node_runtime_handler.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/kubernetes/aio/client/models/v1_runtime_class_list.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/kubernetes/aio/client/models/v1_runtime_class.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/kubernetes/client/models/v1_node_runtime_handler_features.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/kubernetes/client/models/v1_node_runtime_handler.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/kubernetes/client/models/v1_runtime_class_list.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/kubernetes/client/models/v1_runtime_class.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/networkx/algorithms/isomorphism/temporalisomorphvf2.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/networkx/algorithms/isomorphism/tests/test_temporalisomorphvf2.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/networkx/algorithms/tests/test_time_dependent.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/networkx/algorithms/time_dependent.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/networkx/generators/tests/test_time_series.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/networkx/generators/time_series.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/nltk/sentiment/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/nltk/sentiment/sentiment_analyzer.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/nltk/sentiment/util.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/nltk/sentiment/vader.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/numpy/_core/tests/test_datetime.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/numpy/typing/tests/test_runtime.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime-1.27.0.dist-info/entry_points.txt
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime-1.27.0.dist-info/top_level.txt
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/backend/backend.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/backend/backend_rep.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/backend/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/capi/build_and_package_info.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/capi/convert_npz_to_onnx_adapter.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/capi/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/capi/_ld_preload.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/capi/onnxruntime_collect_build_info.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/capi/onnxruntime_inference_collection.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/capi/onnxruntime_validation.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/capi/_pybind_state.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/datasets/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/Privacy.md
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/base_quantizer.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/calibrate.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/CalTableFlatBuffers/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/CalTableFlatBuffers/KeyValue.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/CalTableFlatBuffers/TrtTable.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/execution_providers/qnn/fusion_lpnorm.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/execution_providers/qnn/fusion_spacetodepth.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/execution_providers/qnn/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/execution_providers/qnn/mixed_precision_overrides_utils.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/execution_providers/qnn/preprocess.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/execution_providers/qnn/quant_config.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/fusions/fusion_gelu.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/fusions/fusion_layernorm.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/fusions/fusion.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/fusions/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/fusions/replace_upsample_with_resize.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/matmul_bnb4_quantizer.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/matmul_nbits_quantizer.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/neural_compressor/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/neural_compressor/onnx_model.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/neural_compressor/util.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/neural_compressor/weight_only.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/onnx_model.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/onnx_quantizer.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/operators/activation.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/operators/argmax.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/operators/attention.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/operators/base_operator.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/operators/binary_op.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/operators/concat.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/operators/conv.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/operators/direct_q8.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/operators/embed_layernorm.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/operators/gather.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/operators/gavgpool.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/operators/gemm.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/operators/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/operators/lstm.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/operators/matmul.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/operators/maxpool.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/operators/norm.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/operators/pad.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/operators/pooling.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/operators/qdq_base_operator.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/operators/resize.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/operators/softmax.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/operators/split.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/operators/where.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/preprocess.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/qdq_loss_debug.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/qdq_quantizer.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/quantize.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/quant_utils.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/registry.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/shape_inference.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/static_quantize_runner.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/quantization/tensor_quant_overrides.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/ThirdPartyNotices.txt
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/check_onnx_model_mobile_usability.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/convert_onnx_models_to_ort.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/file_utils.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/logger.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/make_dynamic_shape_fixed.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/mobile_helpers/coreml_supported_mlprogram_ops.md
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/mobile_helpers/coreml_supported_neuralnetwork_ops.md
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/mobile_helpers/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/mobile_helpers/nnapi_supported_ops.md
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/mobile_helpers/usability_checker.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/offline_tuning.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/onnx_model_utils.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/onnx_randomizer.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/onnxruntime_test.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/optimize_onnx_model.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/operator_type_usage_processors.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/ArgTypeAndIndex.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/ArgType.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/Attribute.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/AttributeType.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/Checkpoint.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/DeprecatedKernelCreateInfos.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/DeprecatedNodeIndexAndKernelDefHash.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/DeprecatedSessionState.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/DeprecatedSubGraphSessionState.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/Dimension.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/DimensionValue.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/DimensionValueType.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/EdgeEnd.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/FloatProperty.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/Graph.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/InferenceSession.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/IntProperty.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/KernelTypeStrArgsEntry.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/KernelTypeStrResolver.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/MapType.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/Model.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/ModuleState.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/NodeEdge.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/Node.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/NodesToOptimizeIndices.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/NodeType.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/OperatorSetId.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/OpIdKernelTypeStrArgsEntry.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/OptimizerGroup.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/ParameterOptimizerState.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/PropertyBag.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/RuntimeOptimizationRecordContainerEntry.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/RuntimeOptimizationRecord.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/RuntimeOptimizations.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/SequenceType.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/Shape.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/SparseTensor.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/StringProperty.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/StringStringEntry.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/TensorDataType.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/Tensor.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/TensorTypeAndShape.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/TypeInfo.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/TypeInfoValue.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/fbs/ValueInfo.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_flatbuffers_py/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/ort_model_processor.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/types.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/ort_format_model/utils.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/pytorch_export_contrib_ops.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/pytorch_export_helpers.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/qdq_helpers/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/qdq_helpers/optimize_qdq_model.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/qnn/add_trans_cast.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/qnn/gen_qnn_ctx_onnx_model.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/qnn/preprocess.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/reduced_build_config_parser.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/remove_initializer_from_input.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/symbolic_shape_infer.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/tools/update_onnx_opset.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/affinity_helper.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/benchmark_helper.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/benchmark.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/bert_perf_test.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/bert_test_data.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/compare_bert_results.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/constants.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/convert_generation.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/convert_tf_models_to_pytorch.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/convert_to_packing_mode.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/dynamo_onnx_helper.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/float16.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_attention_clip.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_attention.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_attention_sam2.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_attention_unet.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_attention_vae.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_bart_attention.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_base.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_bias_add.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_biasgelu.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_biassplitgelu.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_conformer_attention.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_constant_fold.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_embedlayer.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_fastgelu.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_gelu_approximation.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_gelu.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_gemmfastgelu.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_gpt_attention_megatron.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_gpt_attention_no_past.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_gpt_attention.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_group_norm.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_layernorm.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_mha_dit.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_mha_mmdit.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_nhwc_conv.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_options.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_qordered_attention.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_qordered_gelu.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_qordered_layernorm.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_qordered_matmul.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_quickgelu.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_reshape.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_rotary_attention.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_shape.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_simplified_layernorm.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_skip_group_norm.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_skiplayernorm.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_transpose.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/fusion_utils.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/huggingface_models.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/import_utils.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/io_binding_helper.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/large_model_exporter.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/machine_info.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/metrics.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/bart/export.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/bart/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/bert/eval_squad.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/bert/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/gpt2/benchmark_gpt2.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/gpt2/convert_to_onnx.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/gpt2/gpt2_helper.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/gpt2/gpt2_parity.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/gpt2/gpt2_tester.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/gpt2/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/gpt2/parity_check_helper.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/llama/benchmark_all.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/llama/benchmark_e2e.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/llama/benchmark.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/llama/convert_to_onnx.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/llama/dist_settings.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/llama/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/llama/llama_inputs.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/llama/llama_parity.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/llama/llama_torch.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/llama/quant_kv_dataloader.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/longformer/benchmark_longformer.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/longformer/convert_to_onnx.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/longformer/generate_test_data.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/longformer/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/longformer/longformer_helper.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/phi2/convert_to_onnx.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/phi2/inference_example.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/phi2/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/sam2/benchmark_sam2.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/sam2/convert_to_onnx.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/sam2/image_decoder.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/sam2/image_encoder.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/sam2/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/sam2/mask_decoder.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/sam2/nvtx_helper.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/sam2/prompt_encoder.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/sam2/sam2_demo.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/sam2/sam2_image_onnx_predictor.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/sam2/sam2_utils.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/benchmark_controlnet.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/benchmark.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/demo_txt2img.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/demo_txt2img_xl.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/demo_utils.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/diffusion_models.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/diffusion_schedulers.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/engine_builder_ort_cuda.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/engine_builder_ort_trt.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/engine_builder.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/engine_builder_tensorrt.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/engine_builder_torch.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/optimize_pipeline.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/ort_optimizer.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/pipeline_stable_diffusion.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/stable_diffusion/trt_utilities.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/t5/convert_to_onnx.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/t5/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/t5/t5_decoder.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/t5/t5_encoder_decoder_init.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/t5/t5_encoder.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/t5/t5_helper.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/whisper/benchmark_all.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/whisper/benchmark.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/whisper/convert_to_onnx.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/whisper/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/whisper/whisper_chain.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/whisper/whisper_decoder.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/whisper/whisper_encoder_decoder_init.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/whisper/whisper_encoder.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/whisper/whisper_helper.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/whisper/whisper_inputs.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/models/whisper/whisper_jump_times.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/onnx_exporter.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/onnx_model_bart.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/onnx_model_bert_keras.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/onnx_model_bert.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/onnx_model_bert_tf.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/onnx_model_clip.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/onnx_model_conformer.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/onnx_model_gpt2.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/onnx_model_mmdit.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/onnx_model_phi.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/onnx_model.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/onnx_model_sam2.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/onnx_model_t5.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/onnx_model_tnlr.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/onnx_model_unet.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/onnx_model_vae.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/onnx_utils.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/optimizer.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/past_helper.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/profile_result_processor.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/profiler.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/quantize_helper.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/shape_infer_helper.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/shape_optimizer.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/onnxruntime/transformers/torch_onnx_export_helper.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/pip/_internal/utils/datetime.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/pip/_vendor/rich/_timer.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/pip/_vendor/urllib3/util/timeout.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/pydantic/datetime_parse.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/pydantic/v1/datetime_parse.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/pypika/clickhouse/dates_and_times.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/redis/commands/timeseries/commands.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/redis/commands/timeseries/info.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/redis/commands/timeseries/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/redis/commands/timeseries/utils.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/redis/observability/registry.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/rich/_timer.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/scipy/datasets/_registry.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/scipy/signal/_short_time_fft.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/scipy/signal/tests/test_short_time_fft.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/sympy/physics/quantum/hilbert.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_hilbert.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/sympy/physics/units/systems/length_weight_time.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/sympy/utilities/tests/test_timeutils.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/sympy/utilities/timeutils.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/textblob/en/sentiments.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/textblob/sentiments.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/distributed/elastic/rendezvous/registry.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/distributed/elastic/timer/api.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/distributed/elastic/timer/debug_info_logging.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/distributed/elastic/timer/file_based_local_timer.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/distributed/elastic/timer/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/distributed/elastic/timer/local_timer.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/distributed/fsdp/_runtime_utils.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/distributed/rpc/backend_registry.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/distributed/rpc/_testing/faulty_agent_backend_registry.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/distributed/_shard/op_registry_utils.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/distributed/_tools/runtime_estimator.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/distributions/constraint_registry.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_dynamo/backends/registry.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_dynamo/comptime.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_export/passes/add_runtime_assertions_for_constraints_pass.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_export/passes/remove_runtime_assertions.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_functorch/_aot_autograd/runtime_wrappers.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/fx/passes/runtime_assert.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torchgen/static_runtime/config.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torchgen/static_runtime/generator.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torchgen/static_runtime/gen_static_runtime_ops.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torchgen/static_runtime/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_inductor/compile_worker/timer.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_inductor/fx_passes/node_runtime_estimation.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_inductor/runtime/autotune_cache.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_inductor/runtime/benchmarking.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_inductor/runtime/cache_dir_utils.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_inductor/runtime/caching/config.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_inductor/runtime/caching/context.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_inductor/runtime/caching/encoders.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_inductor/runtime/caching/exceptions.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_inductor/runtime/caching/implementations.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_inductor/runtime/caching/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_inductor/runtime/caching/interfaces.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_inductor/runtime/caching/locks.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_inductor/runtime/caching/memoizers.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_inductor/runtime/caching/utils.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_inductor/runtime/compile_tasks.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_inductor/runtime/coordinate_descent_tuner.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_inductor/runtime/debug_utils.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_inductor/runtime/halide_helpers.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_inductor/runtime/hints.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_inductor/runtime/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_inductor/runtime/proton_utils.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_inductor/runtime/runtime_utils.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_inductor/runtime/static_triton_launcher.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_inductor/runtime/triton_compat.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_inductor/runtime/triton_helpers.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_inductor/runtime/triton_heuristics.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_inductor/runtime/triton_lazy_compile.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_inductor/template_heuristics/registry.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_library/fake_class_registry.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_library/simple_registry.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_native/dsl_registry.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_native/registry.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/nn/attention/_registry.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/onnx/_internal/exporter/_torchlib/_torchlib_registry.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/_strobelight/compile_time_profiler.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/utils/benchmark/examples/simple_timeit.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/utils/benchmark/utils/timer.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/utils/benchmark/utils/valgrind_wrapper/timer_interface.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/utils/data/datapipes/utils/snapshot.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/torch/utils/_runtime_estimation.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/transformers/models/time_series_transformer/configuration_time_series_transformer.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/transformers/models/time_series_transformer/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/transformers/models/time_series_transformer/modeling_time_series_transformer.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/transformers/models/timesfm2_5/configuration_timesfm2_5.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/transformers/models/timesfm2_5/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/transformers/models/timesfm2_5/modeling_timesfm2_5.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/transformers/models/timesfm2_5/modular_timesfm2_5.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/transformers/models/timesfm/configuration_timesfm.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/transformers/models/timesfm/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/transformers/models/timesfm/modeling_timesfm.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/transformers/models/timesfm/modular_timesfm.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/transformers/models/timesformer/configuration_timesformer.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/transformers/models/timesformer/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/transformers/models/timesformer/modeling_timesformer.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/transformers/models/timesformer/video_processing_timesformer.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/transformers/models/voxtral_realtime/configuration_voxtral_realtime.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/transformers/models/voxtral_realtime/feature_extraction_voxtral_realtime.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/transformers/models/voxtral_realtime/__init__.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/transformers/models/voxtral_realtime/modeling_voxtral_realtime.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/transformers/models/voxtral_realtime/modular_voxtral_realtime.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/transformers/models/voxtral_realtime/processing_voxtral_realtime.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/transformers/time_series_utils.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/urllib3/util/timeout.py
/home/cakidd/repos/normalization_work/output/venv_similarity/lib/python3.12/site-packages/websockets/asyncio/async_timeout.py
/home/cakidd/sync_gbimwvblockgroupsv1_to_remote_chroma.py
/home/cakidd/sync_worldview_to_chroma.py
/home/cakidd/sync_wv_counties_v2_to_remote_chroma.py
/home/cakidd/sync_wv_tracts_v2_to_remote_chroma.py
/home/cakidd/sync_wv_tracts_v3_to_remote_chroma.py
/home/cakidd/wv_blockgroup_belief_vector_ready.sql
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/Downloads/files$ grep -RniE 'gbimperson|person_belief|people space|Hilbert People|temporal|Ht|snapshot_version|collection_hash|feature_hash|publication_manifest' ~ 2>/dev/null | head -n 300
/home/cakidd/jarvis_audit/policy/hp_kyc_mapping.yaml:32:      - Light recovery copy in jarvis-msjarvis-db container.
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:14:./docker-compose.yml:555:    - HILBERT_TIME_URL=http://jarvis-hilbert-time:8092
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:20:./docker-compose.yml:1703:    - HILBERT_TIME_URL=http://jarvis-hilbert-time:8092
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:53:services/jarvis_hilbert_state.py:20:HILBERT_TIME_URL = os.getenv("HILBERT_TIME_URL", "http://jarvis-hilbert-time:8092")
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:100:./scratch_edits/civic_projector_edit.py:2:Civic Projector — reads hp.* (Hilbert People) ONLY.
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:121:./services/jarvis_hilbert_state.py:20:HILBERT_TIME_URL = os.getenv("HILBERT_TIME_URL", "http://jarvis-hilbert-time:8092")
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:176:services/msjarvisunifiedswaggergatewayFIXED.py:58:HILBERT_URL = "http://jarvis-hilbert-spatial:8235"         # /hilbert-space
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:200:services/jarvis-hippocampus_hippocampus_service.py:71:HILBERT_URL       = os.getenv("HILBERT_URL", "http://localhost:18092")
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:378:services/hp_sidecar.py:13:HILBERT_URL = os.environ.get("HILBERT_STATE_URL", "http://jarvis-hilbert-state:8081")
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:385:services/jarvis_hilbert_semantic.py:18:HILBERT_TIME_URL = os.getenv("HILBERT_TIME_URL", "http://jarvis-hilbert-time:8092")
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:386:services/jarvis_hilbert_semantic.py:19:HILBERT_STATE_URL = os.getenv("HILBERT_STATE_URL", "http://jarvis-hilbert-state:8081")
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:412:services/hilbert/civic_intake.py:30:        raise HTTPException(status_code=403, detail="Invalid X-Hilbert-Key")
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:422:services/hilbert/migrations/001_hp_appearance_schema.sql:139:-- hilbert_app role has NO connect rights to kycvault DB (enforced at pg_hba)
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:439:services/quantum_insight_llm.py:97:        "You see a Hilbert-space state over current concepts, with inner-product couplings.\n\n"
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:442:./services/msjarvisunifiedswaggergatewayFIXED.py:58:HILBERT_URL = "http://jarvis-hilbert-spatial:8235"         # /hilbert-space
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:467:services/hilbert/civic_projector.py:2:Civic Projector — reads hp.* (Hilbert People) ONLY.
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:478:services/hilbert_commons/projector.py:41:def _subspace_weight(meta: dict, keys: frozenset) -> float:
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:481:services/hilbert_commons/projector.py:60:    w_app  = _subspace_weight(meta, _APP_KEYS)
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:482:services/hilbert_commons/projector.py:61:    w_geo  = _subspace_weight(meta, _GEO_KEYS)
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:483:services/hilbert_commons/projector.py:62:    w_time = _subspace_weight(meta, _TIME_KEYS)
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:500:./services/jarvis-hippocampus_hippocampus_service.py:71:HILBERT_URL       = os.getenv("HILBERT_URL", "http://localhost:18092")
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:510:services/hilbert/jarvis_hilbert_state.py:20:HILBERT_TIME_URL = os.getenv("HILBERT_TIME_URL", "http://jarvis-hilbert-time:8092")
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:570:./services/jarvis_hilbert_semantic.py:18:HILBERT_TIME_URL = os.getenv("HILBERT_TIME_URL", "http://jarvis-hilbert-time:8092")
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:571:./services/jarvis_hilbert_semantic.py:19:HILBERT_STATE_URL = os.getenv("HILBERT_STATE_URL", "http://jarvis-hilbert-state:8081")
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:589:services/intake_service.py:32:HILBERT_TIME_URL= os.getenv("HILBERT_TIME_URL","http://jarvis-hilbert-time:8092")
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:597:./services/hilbert/civic_intake.py:30:        raise HTTPException(status_code=403, detail="Invalid X-Hilbert-Key")
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:605:./services/hilbert/migrations/001_hp_appearance_schema.sql:139:-- hilbert_app role has NO connect rights to kycvault DB (enforced at pg_hba)
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:615:./services/quantum_insight_llm.py:97:        "You see a Hilbert-space state over current concepts, with inner-product couplings.\n\n"
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:623:./services/hp_sidecar.py:13:HILBERT_URL = os.environ.get("HILBERT_STATE_URL", "http://jarvis-hilbert-state:8081")
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:627:services/PORTS_REGISTRY_RAW.txt:125:/home/ms-jarvis/msjarvis-rebuild/services/hilbert_spatial_chat.py:        _chromadb_client = chromadb.HttpClient(host="localhost", port=8018)
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:631:./services/hilbert/civic_projector.py:2:Civic Projector — reads hp.* (Hilbert People) ONLY.
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:637:services/PORT_AUDIT_RAW.txt:140:/home/ms-jarvis/msjarvis-rebuild/services/hilbert_spatial_chat.py:88:        _chromadb_client = chromadb.HttpClient(host="localhost", port=8018)
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:654:./services/hilbert/jarvis_hilbert_state.py:20:HILBERT_TIME_URL = os.getenv("HILBERT_TIME_URL", "http://jarvis-hilbert-time:8092")
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:689:services/msjarvisconsciousnessbridge.py:35:            "hilbert": "http://jarvis-hilbert-gateway:8081",
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:728:./services/intake_service.py:32:HILBERT_TIME_URL= os.getenv("HILBERT_TIME_URL","http://jarvis-hilbert-time:8092")
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:745:./services/hilbert_commons/projector.py:41:def _subspace_weight(meta: dict, keys: frozenset) -> float:
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:748:./services/hilbert_commons/projector.py:60:    w_app  = _subspace_weight(meta, _APP_KEYS)
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:749:./services/hilbert_commons/projector.py:61:    w_geo  = _subspace_weight(meta, _GEO_KEYS)
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:750:./services/hilbert_commons/projector.py:62:    w_time = _subspace_weight(meta, _TIME_KEYS)
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:792:./services/PORTS_REGISTRY_RAW.txt:125:/home/ms-jarvis/msjarvis-rebuild/services/hilbert_spatial_chat.py:        _chromadb_client = chromadb.HttpClient(host="localhost", port=8018)
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:805:./services/msjarvisconsciousnessbridge.py:35:            "hilbert": "http://jarvis-hilbert-gateway:8081",
/home/cakidd/jarvis_audit/extracts/code_theory_refs.log:810:./services/PORT_AUDIT_RAW.txt:140:/home/ms-jarvis/msjarvis-rebuild/services/hilbert_spatial_chat.py:88:        _chromadb_client = chromadb.HttpClient(host="localhost", port=8018)
/home/cakidd/jarvis_audit/extracts/critical_service_code_context.log:10:import httpx
/home/cakidd/jarvis_audit/extracts/critical_service_code_context.log:14:from fastapi import FastAPI, HTTPException
/home/cakidd/jarvis_audit/extracts/critical_service_code_context.log:41:FIFTH_DGM_URL = os.getenv("FIFTH_DGM_URL", "http://msjarvisfifthdgmorchestrator:4002")
/home/cakidd/jarvis_audit/extracts/critical_service_code_context.log:42:PSYCHOLOGY_SERVICES_URL = os.getenv("PSYCHOLOGY_SERVICES_URL", "http://jarvis-psychology-services:8019")
/home/cakidd/jarvis_audit/extracts/critical_service_code_context.log:43:CONSTITUTIONAL_GUARDIAN_URL = os.getenv("CONSTITUTIONAL_GUARDIAN_URL", "http://jarvis-constitutional-guardian:8091")
/home/cakidd/jarvis_audit/extracts/critical_service_code_context.log:52:            "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
/home/cakidd/jarvis_audit/extracts/critical_service_code_context.log:53:            "neurobiological_master": "http://jarvis-neurobiological-master:8018",
/home/cakidd/jarvis_audit/extracts/critical_service_code_context.log:54:            "i_containers": "http://jarvis-i-containers:8015",
/home/cakidd/jarvis_audit/extracts/critical_service_code_context.log:55:            "blood_brain_barrier": "http://jarvis-blood-brain-barrier:8016",
/home/cakidd/jarvis_audit/extracts/critical_service_code_context.log:56:            "qualia_engine": "http://jarvis-qualia-engine:8017",
/home/cakidd/jarvis_audit/extracts/critical_service_code_context.log:58:            "wv_ensemble": "http://jarvis-wv-entangled-gateway:8010",
/home/cakidd/jarvis_audit/extracts/critical_service_code_context.log:76:            async with httpx.AsyncClient(timeout=None) as client:
/home/cakidd/jarvis_audit/extracts/critical_service_code_context.log:105:        async with httpx.AsyncClient(timeout=None) as client:
/home/cakidd/jarvis_audit/extracts/critical_service_code_context.log:133:        async with httpx.AsyncClient(timeout=None) as client:
/home/cakidd/jarvis_audit/extracts/critical_service_code_context.log:193:            # WV Ensemble — thought production (WV-first architecture)
/home/cakidd/jarvis_audit/extracts/critical_service_code_context.log:271:from fastapi import FastAPI, Header, HTTPException, status, Depends
/home/cakidd/jarvis_audit/extracts/critical_service_code_context.log:273:import httpx  # NEW: for forwarding to main_brain
/home/cakidd/jarvis_audit/extracts/critical_service_code_context.log:303:MAIN_BRAIN_URL = os.getenv("MAIN_BRAIN_URL", "http://jarvis-main-brain:8050")
/home/cakidd/jarvis_audit/extracts/critical_service_code_context.log:340:        raise HTTPException(
/home/cakidd/jarvis_audit/extracts/critical_service_code_context.log:341:            status_code=status.HTTP_401_UNAUTHORIZED,
/home/cakidd/jarvis_audit/extracts/critical_service_code_context.log:371:        async with httpx.AsyncClient(timeout=None) as client:
/home/cakidd/jarvis_audit/extracts/critical_service_code_context.log:379:        raise HTTPException(status_code=502, detail="Main brain unreachable")
/home/cakidd/jarvis_audit/extracts/critical_service_code_context.log:386:        raise HTTPException(status_code=502, detail="Main brain error")
/home/cakidd/jarvis_audit/extracts/critical_service_code_context.log:463:    import httpx
/home/cakidd/jarvis_audit/extracts/critical_service_code_context.log:464:    async with httpx.AsyncClient(timeout=5.0) as client:
/home/cakidd/jarvis_audit/extracts/critical_service_code_context.log:465:        r = await client.post("http://jarvis-fifth-dgm:4002/filter_consciousness", json=payload)
/home/cakidd/jarvis_audit/extracts/critical_service_code_context.log:492:from fastapi import FastAPI, HTTPException
/home/cakidd/jarvis_audit/extracts/critical_service_code_context.log:496:import httpx
/home/cakidd/jarvis_audit/extracts/critical_service_code_context.log:522:GUARDIAN_URL = os.getenv("CONSTITUTIONAL_GUARDIAN_URL", "http://jarvis-constitutional-guardian:8091")
/home/cakidd/jarvis_audit/extracts/critical_service_code_context.log:550:            async with httpx.AsyncClient(timeout=5.0) as client:
/home/cakidd/jarvis_audit/extracts/critical_service_code_context.log:564:        except httpx.TimeoutException:
/home/cakidd/jarvis_audit/extracts/critical_service_code_context.log:709:        raise HTTPException(status_code=500, detail=str(e))
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:2072:newfstatat(AT_FDCWD, "/usr/lib/python3.12/http/__init__.cpython-312-x86_64-linux-gnu.so", 0x7ffe3a092520, 0) = -1 ENOENT (No such file or directory)
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:2073:newfstatat(AT_FDCWD, "/usr/lib/python3.12/http/__init__.abi3.so", 0x7ffe3a092520, 0) = -1 ENOENT (No such file or directory)
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:2074:newfstatat(AT_FDCWD, "/usr/lib/python3.12/http/__init__.so", 0x7ffe3a092520, 0) = -1 ENOENT (No such file or directory)
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:2075:newfstatat(AT_FDCWD, "/usr/lib/python3.12/http/__init__.py", {st_mode=S_IFREG|0644, st_size=8308, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:2076:newfstatat(AT_FDCWD, "/usr/lib/python3.12/http/__init__.py", {st_mode=S_IFREG|0644, st_size=8308, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:2077:openat(AT_FDCWD, "/usr/lib/python3.12/http/__pycache__/__init__.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 3
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:2083:read(3, "\313\r\r\n\0\0\0\0\300\216\301it \0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\5\0\0\0\0\0\0\0\363t\0\0\0\227\0d\0d\1l\0m\1Z\1m\2Z\2m\3Z\3\1\0d\2d\3g\2Z\4\2\0e\3e\2\253\1\0\0\0\0\0\0\2\0G\0d\4\204\0d\2\253\2\0\0\0\0\0\0\253\0\0\0\0\0\0\0Z\5\2\0e\3e\1\253\1\0\0\0\0\0\0\2\0G\0d\5\204\0d\3\253\2\0\0\0\0\0\0\253\0\0\0\0\0\0\0Z\6y\6)\7\351\0\0\0\0)\3\332\7StrEnum\332\7IntEnum\332\f_simple_enum\332\nHTTPStatus\332\nHTTPMethodc\0\0\0\0\0\0\0\0\0\0\0\0\2\0\0\0\0\0\0\0\363`\1\0\0\227\0e\0Z\1d"..., 9488) = 9487
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3535:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/protocols/http/__init__.cpython-312-x86_64-linux-gnu.so", 0x7ffe3a092870, 0) = -1 ENOENT (No such file or directory)
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3536:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/protocols/http/__init__.abi3.so", 0x7ffe3a092870, 0) = -1 ENOENT (No such file or directory)
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3537:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/protocols/http/__init__.so", 0x7ffe3a092870, 0) = -1 ENOENT (No such file or directory)
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3538:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/protocols/http/__init__.py", {st_mode=S_IFREG|0664, st_size=0, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3539:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/protocols/http/__init__.py", {st_mode=S_IFREG|0664, st_size=0, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3540:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/protocols/http/__pycache__/__init__.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3546:read(13, "\313\r\r\n\0\0\0\0\177\4Cj\0\0\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\363\4\0\0\0\227\0y\0)\1N\251\0r\2\0\0\0\363\0\0\0\0\372q/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/protocols/http/__init__.py\372\10<module>r\5\0\0\0\1\0\0\0s\5\0\0\0\361\3\1\1\1r\3\0\0\0", 211) = 210
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3549:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/protocols/http", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3550:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/protocols/http", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3551:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/protocols/http", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3552:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/protocols/http", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3557:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/protocols/http/auto.py", {st_mode=S_IFREG|0664, st_size=403, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3558:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/protocols/http/auto.py", {st_mode=S_IFREG|0664, st_size=403, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3559:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/protocols/http/__pycache__/auto.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3565:read(13, "\313\r\r\n\0\0\0\0\177\4Cj\223\1\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\4\0\0\0\0\0\0\1\363d\0\0\0\227\0U\0d\0d\1l\0m\1Z\1\1\0d\0d\2l\2Z\2d\3e\3d\4<\0\0\0\t\0d\0d\2l\4Z\4d\0d\5l\5m\6Z\6\1\0e\6Z\7y\2#\0e\10$\0r\v\1\0d\0d\6l\tm\nZ\n\1\0e\nZ\7Y\0y\2w\0x\3Y\0w\1)\7\351\0\0\0\0)\1\332\vannotationsNz\26type[asyncio.Protocol]\332\20AutoHTTPProtocol)\1\332\21HttpToolsProtocol)\1\332\vH11Protocol)\v\332\n__future_"..., 622) = 621
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3574:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/__init__.cpython-312-x86_64-linux-gnu.so", 0x7ffe3a092200, 0) = -1 ENOENT (No such file or directory)
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3575:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/__init__.abi3.so", 0x7ffe3a092200, 0) = -1 ENOENT (No such file or directory)
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3576:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/__init__.so", 0x7ffe3a092200, 0) = -1 ENOENT (No such file or directory)
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3577:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/__init__.py", {st_mode=S_IFREG|0664, st_size=147, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3578:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/__init__.py", {st_mode=S_IFREG|0664, st_size=147, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3579:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/__pycache__/__init__.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3588:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3589:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3590:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3591:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3596:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/parser/__init__.cpython-312-x86_64-linux-gnu.so", 0x7ffe3a091720, 0) = -1 ENOENT (No such file or directory)
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3597:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/parser/__init__.abi3.so", 0x7ffe3a091720, 0) = -1 ENOENT (No such file or directory)
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3598:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/parser/__init__.so", 0x7ffe3a091720, 0) = -1 ENOENT (No such file or directory)
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3599:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/parser/__init__.py", {st_mode=S_IFREG|0664, st_size=201, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3600:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/parser/__init__.py", {st_mode=S_IFREG|0664, st_size=201, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3601:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/parser/__pycache__/__init__.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3607:read(13, "\313\r\r\n\0\0\0\0\342\223\301i\311\0\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\2\0\0\0\0\0\0\0\363z\0\0\0\227\0d\0d\1l\0m\1Z\1\1\0d\0d\2l\2\255\2\1\0d\0d\2l\3\255\2\1\0d\0d\2l\4\255\2\1\0e\2j\n\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0e\3j\n\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0z\0\0\0e\4j\n\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0z\0\0\0Z\5y\3)\4\351\1\0\0\0)\1\332\fHTTPProtocol)\1\332\1*N)\6\332\10protocolr\3\0\0\0\332\6parser\332\6errors\332\nurl_parser\332\7__all__\251\0\363\0\0\0\0\372k"..., 439) = 438
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3610:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/parser", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3611:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/parser", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3612:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/parser", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3613:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/parser", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3618:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/parser/protocol.py", {st_mode=S_IFREG|0664, st_size=542, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3619:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/parser/protocol.py", {st_mode=S_IFREG|0664, st_size=542, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3620:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/parser/__pycache__/protocol.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3626:read(13, "\313\r\r\n\0\0\0\0\342\223\301i\36\2\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\5\0\0\0\0\0\0\0\363&\0\0\0\227\0d\0d\1l\0m\1Z\1\1\0\2\0G\0d\2\204\0d\3e\1\253\3\0\0\0\0\0\0Z\2y\4)\5\351\0\0\0\0)\1\332\10Protocolc\0\0\0\0\0\0\0\0\0\0\0\0\6\0\0\0\0\0\0\0\363|\0\0\0\227\0e\0Z\1d\0Z\2d\1Z\3d\22d\4\204\4Z\4d\5e\5d\2d\3f\4d\6\204\4Z\6d\7e\5d\10e\5d\2d\3f\6d\t\204\4Z\7d\22d\n\204\4Z\10d\ve\5d\2d\3f\4d\f\204\4Z\td\22d\r\204\4Z\nd\22d\16\204\4Z\vd\22d\17\204\4Z\fd\20e\5d\2d\3f\4d\21\204\4Z\ry\3)\23\332\fHTT"..., 1827) = 1826
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3629:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/parser", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3630:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/parser/parser.cpython-312-x86_64-linux-gnu.so", {st_mode=S_IFREG|0775, st_size=1264464, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3631:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/parser/parser.cpython-312-x86_64-linux-gnu.so", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3640:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/parser", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3641:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/parser/errors.py", {st_mode=S_IFREG|0664, st_size=566, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3642:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/parser/errors.py", {st_mode=S_IFREG|0664, st_size=566, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3643:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/parser/__pycache__/errors.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3649:read(13, "\313\r\r\n\0\0\0\0\342\223\301i6\2\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\5\0\0\0\0\0\0\0\363\214\0\0\0\227\0d\0Z\0\2\0G\0d\1\204\0d\2e\1\253\3\0\0\0\0\0\0Z\2\2\0G\0d\3\204\0d\4e\2\253\3\0\0\0\0\0\0Z\3\2\0G\0d\5\204\0d\6e\2\253\3\0\0\0\0\0\0Z\4\2\0G\0d\7\204\0d\10e\2\253\3\0\0\0\0\0\0Z\5\2\0G\0d\t\204\0d\ne\2\253\3\0\0\0\0\0\0Z\6\2\0G\0d\v\204\0d\fe\1\253\3\0\0\0\0\0\0Z\7y\r)\16)\6\332\17HttpParserError\332\27HttpParserCallbackError\332\34HttpParserInvalidStatusErr"..., 1223) = 1222
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3652:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/parser", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3653:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/parser/url_parser.cpython-312-x86_64-linux-gnu.so", {st_mode=S_IFREG|0775, st_size=483328, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3654:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/parser/url_parser.cpython-312-x86_64-linux-gnu.so", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3664:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3665:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/_version.py", {st_mode=S_IFREG|0664, st_size=575, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3666:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/_version.py", {st_mode=S_IFREG|0664, st_size=575, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3667:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/__pycache__/_version.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3673:read(13, "\313\r\r\n\0\0\0\0\342\223\301i?\2\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\1\0\0\0\0\0\0\0\363\10\0\0\0\227\0d\0Z\0y\1)\2z\0050.7.1N)\1\332\v__version__\251\0\363\0\0\0\0\372d/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httptools/_version.py\372\10<module>r\6\0\0\0\1\0\0\0s\f\0\0\0\360\3\1\1\1\360\32\0\17\26\201\vr\4\0\0\0", 226) = 225
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3676:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/protocols/http", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3677:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/protocols/http/httptools_impl.py", {st_mode=S_IFREG|0664, st_size=21462, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3678:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/protocols/http/httptools_impl.py", {st_mode=S_IFREG|0664, st_size=21462, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3679:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/protocols/http/__pycache__/httptools_impl.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3689:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/protocols/http", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3690:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/protocols/http/flow_control.py", {st_mode=S_IFREG|0664, st_size=1771, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3691:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/protocols/http/flow_control.py", {st_mode=S_IFREG|0664, st_size=1771, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3692:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/protocols/http/__pycache__/flow_control.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3698:read(13, "\313\r\r\n\0\0\0\0\177\4Cj\353\6\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\4\0\0\0\0\0\0\0\363L\0\0\0\227\0d\0d\1l\0Z\0d\0d\2l\1m\2Z\2m\3Z\3m\4Z\4m\5Z\5m\6Z\6\1\0d\3Z\7d\4Z\10\2\0G\0d\5\204\0d\6\253\2\0\0\0\0\0\0Z\td\10d\7\204\4Z\ny\1)\t\351\0\0\0\0N)\5\332\23ASGIReceiveCallable\332\20ASGISendCallable\332\25HTTPResponseBodyEvent\332\26HTTPResponseStartEvent\332\5Scope\251\2s\n\0\0\0connections\5\0\0\0closei\0\0\1\0c\0\0"..., 3113) = 3112
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3980:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/websockets/http11.py", {st_mode=S_IFREG|0664, st_size=12569, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3981:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/websockets/http11.py", {st_mode=S_IFREG|0664, st_size=12569, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:3982:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/websockets/__pycache__/http11.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4098:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/websockets/http.py", {st_mode=S_IFREG|0664, st_size=644, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4099:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/websockets/http.py", {st_mode=S_IFREG|0664, st_size=644, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4100:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/websockets/__pycache__/http.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4146:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/websockets/legacy/http.py", {st_mode=S_IFREG|0664, st_size=6930, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4147:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/websockets/legacy/http.py", {st_mode=S_IFREG|0664, st_size=6930, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4148:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/websockets/legacy/__pycache__/http.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4247:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/__init__.cpython-312-x86_64-linux-gnu.so", 0x7ffe3a092200, 0) = -1 ENOENT (No such file or directory)
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4248:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/__init__.abi3.so", 0x7ffe3a092200, 0) = -1 ENOENT (No such file or directory)
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4249:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/__init__.so", 0x7ffe3a092200, 0) = -1 ENOENT (No such file or directory)
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4250:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/__init__.py", {st_mode=S_IFREG|0664, st_size=3210, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4251:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/__init__.py", {st_mode=S_IFREG|0664, st_size=3210, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4252:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/__pycache__/__init__.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4261:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4262:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4263:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4264:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4269:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/__version__.py", {st_mode=S_IFREG|0664, st_size=108, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4270:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/__version__.py", {st_mode=S_IFREG|0664, st_size=108, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4271:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/__pycache__/__version__.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4277:read(13, "\313\r\r\n\0\0\0\0\200\4Cjl\0\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\1\0\0\0\0\0\0\0\363\20\0\0\0\227\0d\0Z\0d\1Z\1d\2Z\2y\3)\4\332\5httpxz,A next generation HTTP client, for Python 3.z\0060.27.0N)\3\332\t__title__\332\17__description__\332\v__version__\251\0\363\0\0\0\0\372c/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/htt"..., 323) = 322
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4280:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4281:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_api.py", {st_mode=S_IFREG|0664, st_size=12928, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4282:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_api.py", {st_mode=S_IFREG|0664, st_size=12928, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4283:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/__pycache__/_api.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4292:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4293:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_client.py", {st_mode=S_IFREG|0664, st_size=67490, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4294:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_client.py", {st_mode=S_IFREG|0664, st_size=67490, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4295:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/__pycache__/_client.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4304:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4305:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_auth.py", {st_mode=S_IFREG|0664, st_size=11830, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4306:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_auth.py", {st_mode=S_IFREG|0664, st_size=11830, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4307:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/__pycache__/_auth.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4330:newfstatat(AT_FDCWD, "/usr/lib/python3.12/http", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4331:newfstatat(AT_FDCWD, "/usr/lib/python3.12/http", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4332:newfstatat(AT_FDCWD, "/usr/lib/python3.12/http", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4333:openat(AT_FDCWD, "/usr/lib/python3.12/http", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4338:newfstatat(AT_FDCWD, "/usr/lib/python3.12/http/client.py", {st_mode=S_IFREG|0644, st_size=57965, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4339:newfstatat(AT_FDCWD, "/usr/lib/python3.12/http/client.py", {st_mode=S_IFREG|0644, st_size=57965, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4340:openat(AT_FDCWD, "/usr/lib/python3.12/http/__pycache__/client.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4457:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4458:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_exceptions.py", {st_mode=S_IFREG|0664, st_size=7922, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4459:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_exceptions.py", {st_mode=S_IFREG|0664, st_size=7922, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4460:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/__pycache__/_exceptions.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4469:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4470:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_models.py", {st_mode=S_IFREG|0664, st_size=42303, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4471:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_models.py", {st_mode=S_IFREG|0664, st_size=42303, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4472:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/__pycache__/_models.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4482:newfstatat(AT_FDCWD, "/usr/lib/python3.12/http", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4483:newfstatat(AT_FDCWD, "/usr/lib/python3.12/http/cookiejar.py", {st_mode=S_IFREG|0644, st_size=77438, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4484:newfstatat(AT_FDCWD, "/usr/lib/python3.12/http/cookiejar.py", {st_mode=S_IFREG|0644, st_size=77438, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4485:openat(AT_FDCWD, "/usr/lib/python3.12/http/__pycache__/cookiejar.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4494:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4495:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_content.py", {st_mode=S_IFREG|0664, st_size=8047, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4496:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_content.py", {st_mode=S_IFREG|0664, st_size=8047, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4497:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/__pycache__/_content.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4506:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4507:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_multipart.py", {st_mode=S_IFREG|0664, st_size=8885, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4508:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_multipart.py", {st_mode=S_IFREG|0664, st_size=8885, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4509:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/__pycache__/_multipart.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4518:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4519:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_types.py", {st_mode=S_IFREG|0664, st_size=3391, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4520:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_types.py", {st_mode=S_IFREG|0664, st_size=3391, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4521:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/__pycache__/_types.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4530:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4531:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_utils.py", {st_mode=S_IFREG|0664, st_size=13858, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4532:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_utils.py", {st_mode=S_IFREG|0664, st_size=13858, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4533:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/__pycache__/_utils.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4571:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4572:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_decoders.py", {st_mode=S_IFREG|0664, st_size=9904, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4573:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_decoders.py", {st_mode=S_IFREG|0664, st_size=9904, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4574:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/__pycache__/_decoders.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4583:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4584:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_compat.py", {st_mode=S_IFREG|0664, st_size=1563, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4585:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_compat.py", {st_mode=S_IFREG|0664, st_size=1563, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4586:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/__pycache__/_compat.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4609:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4610:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_status_codes.py", {st_mode=S_IFREG|0664, st_size=5618, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4611:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_status_codes.py", {st_mode=S_IFREG|0664, st_size=5618, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4612:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/__pycache__/_status_codes.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4622:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4623:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_urls.py", {st_mode=S_IFREG|0664, st_size=21783, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4624:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_urls.py", {st_mode=S_IFREG|0664, st_size=21783, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4625:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/__pycache__/_urls.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4713:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4714:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_urlparse.py", {st_mode=S_IFREG|0664, st_size=17720, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4715:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_urlparse.py", {st_mode=S_IFREG|0664, st_size=17720, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4716:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/__pycache__/_urlparse.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4725:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4726:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_config.py", {st_mode=S_IFREG|0664, st_size=12204, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4727:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_config.py", {st_mode=S_IFREG|0664, st_size=12204, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4728:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/__pycache__/_config.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4941:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4942:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_transports/__init__.cpython-312-x86_64-linux-gnu.so", 0x7ffe3a090a40, 0) = -1 ENOENT (No such file or directory)
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4943:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_transports/__init__.abi3.so", 0x7ffe3a090a40, 0) = -1 ENOENT (No such file or directory)
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4944:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_transports/__init__.so", 0x7ffe3a090a40, 0) = -1 ENOENT (No such file or directory)
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4945:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_transports/__init__.py", {st_mode=S_IFREG|0664, st_size=0, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4946:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_transports/__init__.py", {st_mode=S_IFREG|0664, st_size=0, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4947:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_transports/__pycache__/__init__.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4953:read(13, "\313\r\r\n\0\0\0\0\200\4Cj\0\0\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\363\4\0\0\0\227\0y\0)\1N\251\0r\2\0\0\0\363\0\0\0\0\372l/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_transports/__init__.py\372\10<module>r\5\0\0\0\1\0\0\0s\5\0\0\0\361\3\1\1\1r\3\0\0\0", 206) = 205
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4956:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_transports", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4957:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_transports", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4958:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_transports", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4959:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_transports", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4964:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_transports/asgi.py", {st_mode=S_IFREG|0664, st_size=5490, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4965:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_transports/asgi.py", {st_mode=S_IFREG|0664, st_size=5490, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4966:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_transports/__pycache__/asgi.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4975:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_transports", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4976:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_transports/base.py", {st_mode=S_IFREG|0664, st_size=2472, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4977:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_transports/base.py", {st_mode=S_IFREG|0664, st_size=2472, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4978:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_transports/__pycache__/base.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4987:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_transports", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4988:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_transports/default.py", {st_mode=S_IFREG|0664, st_size=13290, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4989:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_transports/default.py", {st_mode=S_IFREG|0664, st_size=13290, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:4990:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_transports/__pycache__/default.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5005:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore/__init__.cpython-312-x86_64-linux-gnu.so", 0x7ffe3a090840, 0) = -1 ENOENT (No such file or directory)
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5006:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore/__init__.abi3.so", 0x7ffe3a090840, 0) = -1 ENOENT (No such file or directory)
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5007:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore/__init__.so", 0x7ffe3a090840, 0) = -1 ENOENT (No such file or directory)
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5008:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore/__init__.py", {st_mode=S_IFREG|0664, st_size=3445, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5009:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore/__init__.py", {st_mode=S_IFREG|0664, st_size=3445, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5010:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore/__pycache__/__init__.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5019:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5020:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5021:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5022:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5027:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore/_api.py", {st_mode=S_IFREG|0664, st_size=3146, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5028:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore/_api.py", {st_mode=S_IFREG|0664, st_size=3146, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5029:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore/__pycache__/_api.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5038:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5039:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore/_models.py", {st_mode=S_IFREG|0664, st_size=17623, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5040:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore/_models.py", {st_mode=S_IFREG|0664, st_size=17623, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5041:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore/__pycache__/_models.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5050:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5051:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore/_sync/__init__.cpython-312-x86_64-linux-gnu.so", 0x7ffe3a08f6f0, 0) = -1 ENOENT (No such file or directory)
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5052:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore/_sync/__init__.abi3.so", 0x7ffe3a08f6f0, 0) = -1 ENOENT (No such file or directory)
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5053:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore/_sync/__init__.so", 0x7ffe3a08f6f0, 0) = -1 ENOENT (No such file or directory)
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5054:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore/_sync/__init__.py", {st_mode=S_IFREG|0664, st_size=1141, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5055:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore/_sync/__init__.py", {st_mode=S_IFREG|0664, st_size=1141, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5056:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore/_sync/__pycache__/__init__.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5062:read(13, "\313\r\r\n\0\0\0\0\262\rBju\4\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\5\0\0\0\0\0\0\0\363\270\0\0\0\227\0d\0d\1l\0m\1Z\1\1\0d\0d\2l\2m\3Z\3\1\0d\0d\3l\4m\5Z\5\1\0d\0d\4l\6m\7Z\7\1\0d\0d\5l\10m\tZ\t\1\0\t\0d\0d\6l\nm\vZ\v\1\0\t\0d\0d\tl\rm\16Z\16\1\0g\0d\f\242\1Z\17y\r#\0e\f$\0r\r\1\0\2\0G\0d\7\204\0d\10\253\2\0\0\0\0\0\0Z\vY\0\214\35w\0x\3Y\0w\1#\0e\f$\0r\r\1\0\2\0G\0d\n\204\0d\v\253\2\0\0\0\0\0\0Z\16Y\0\214+w\0x\3Y\0w\1)\16\351\1\0\0\0)\1\332\16HTTPConnection)\1\332\16C"..., 1585) = 1584
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5065:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore/_sync", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5066:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore/_sync", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5067:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore/_sync", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5068:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore/_sync", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5073:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore/_sync/connection.py", {st_mode=S_IFREG|0664, st_size=8238, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5074:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore/_sync/connection.py", {st_mode=S_IFREG|0664, st_size=8238, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5075:openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore/_sync/__pycache__/connection.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5084:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5085:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore/_backends/__init__.cpython-312-x86_64-linux-gnu.so", 0x7ffe3a08e5a0, 0) = -1 ENOENT (No such file or directory)
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5086:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore/_backends/__init__.abi3.so", 0x7ffe3a08e5a0, 0) = -1 ENOENT (No such file or directory)
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5087:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore/_backends/__init__.so", 0x7ffe3a08e5a0, 0) = -1 ENOENT (No such file or directory)
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653:5088:newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpcore/_backends/__init__.py", {st_mode=S_IFREG|0664, st_size=0, ...}, 0) = 0
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/Downloads/files$ psql "postgresql://postgres@localhost:5436/msjarvisgis_v2" -c "
SELECT table_schema, table_name
FROM information_schema.tables
WHERE table_schema NOT IN ('pg_catalog','information_schema')
ORDER BY table_schema, table_name;
"
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/Downloads/files$ psql "postgresql://postgres@localhost:5436/msjarvisgis_v2" -c "
SELECT table_schema, table_name, column_name, data_type
FROM information_schema.columns
WHERE table_schema NOT IN ('pg_catalog','information_schema')
  AND (
    table_name ILIKE '%person%' OR
    table_name ILIKE '%people%' OR
    table_name ILIKE '%time%' OR
    table_name ILIKE '%temporal%' OR
    table_name ILIKE '%belief%' OR
    table_name ILIKE '%manifest%' OR
    table_name ILIKE '%registry%' OR
    column_name ILIKE '%person%' OR
    column_name ILIKE '%time%' OR
    column_name ILIKE '%snapshot%' OR
    column_name ILIKE '%hash%'
  )
ORDER BY table_schema, table_name, ordinal_position;
"
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/Downloads/files$ psql "postgresql://postgres@localhost:5436/msjarvisgis_v2" -c "
SELECT schemaname, viewname
FROM pg_views
WHERE schemaname NOT IN ('pg_catalog','information_schema')
ORDER BY schemaname, viewname;
"
 schemaname |                       viewname                       
------------+------------------------------------------------------
 public     | gbim_blockgroup_belief_render_v2
 public     | gbim_blockgroup_coverage_semantic
 public     | gbim_blockgroup_embedding_source
 public     | gbim_blockgroup_numeric_features
 public     | gbim_tract_layer_rollup
 public     | geography_columns
 public     | geometry_columns
 public     | wv_blockgroup_belief_vector_ready
 public     | wv_blockgroup_belief_vector_ready_v1
 public     | wv_blockgroup_belief_vector_ready_with_chroma_hashes
 public     | wv_blockgroup_hazus_floodplains
 public     | wv_blockgroup_hazus_tax_summary
 public     | wv_county_belief_vector_ready
 public     | wv_county_belief_vector_ready_with_chroma_hashes
 public     | wv_county_hazus_floodplain_summary
 public     | wv_tract_address_points_coverage_statewide
 public     | wv_tract_belief_vector_ready
 public     | wv_tract_belief_vector_ready_with_chroma_hashes
(18 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/Downloads/files$ psql "postgresql://postgres@localhost:5436/msjarvisgis_v2" -c "
SELECT *
FROM public.gbim_chroma_collection_registry
ORDER BY collection_name;
"
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/Downloads/files$ psql "postgresql://postgres@localhost:5436/msjarvisgis_v2" -c "
SELECT collection_name, count(*) AS feature_rows
FROM public.gbim_chroma_collection_feature_registry
GROUP BY collection_name
ORDER BY collection_name;
"
   collection_name   | feature_rows 
---------------------+--------------
 gbimwvblockgroupsv1 |         1639
 gbimwvcountiesv2    |           55
 gbimwvtractsv2      |          546
(3 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/Downloads/files$ psql "postgresql://postgres@localhost:5436/msjarvisgis_v2" -c "
SELECT *
FROM public.gbim_chroma_publication_manifest
ORDER BY logical_collection_name;
"
ERROR:  relation "public.gbim_chroma_publication_manifest" does not exist
LINE 3: FROM public.gbim_chroma_publication_manifest
             ^
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/Downloads/files$ psql "postgresql://postgres@localhost:5436/msjarvisgis_v2" -c "
SELECT *
FROM public.gbim_vertical_slice_acceptance_tests
ORDER BY logical_collection_name, test_name;
"
ERROR:  relation "public.gbim_vertical_slice_acceptance_tests" does not exist
LINE 3: FROM public.gbim_vertical_slice_acceptance_tests
             ^
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/Downloads/files$ psql "postgresql://postgres@localhost:5436/msjarvisgis_v2" -c "
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_schema = 'public'
  AND table_name IN (
    'wv_county_belief_vector_ready',
    'wv_tract_belief_vector_ready',
    'wv_blockgroup_belief_vector_ready_v1',
    'wv_county_belief_vector_ready_with_chroma_hashes',
    'wv_tract_belief_vector_ready_with_chroma_hashes',
    'wv_blockgroup_belief_vector_ready_with_chroma_hashes'
  )
ORDER BY table_name, ordinal_position;
"
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/Downloads/files$ psql "postgresql://postgres@localhost:5436/msjarvisgis_v2" -c "
SELECT
  'county' AS entity_type,
  snapshot_version,
  min(generated_at) AS min_generated_at,
  max(generated_at) AS max_generated_at,
  count(*) AS row_count
FROM public.wv_county_belief_vector_ready
GROUP BY snapshot_version

UNION ALL

SELECT
  'tract' AS entity_type,
  snapshot_version,
  min(generated_at) AS min_generated_at,
  max(generated_at) AS max_generated_at,
  count(*) AS row_count
FROM public.wv_tract_belief_vector_ready
GROUP BY snapshot_version

UNION ALL

"RDER BY entity_type, snapshot_version;_ready_v1
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/Downloads/files$ python - << 'PY'
import os, json, chromadb, psycopg

PG_DSN = "postgresql://postgres@localhost:5436/msjarvisgis_v2"
report = {
    "local_chroma": [],
    "remote_chroma": [],
    "postgres": {}
}

local = chromadb.PersistentClient(path=os.path.expanduser("~/chroma"))
for c in local.list_collections():
    col = local.get_collection(c.name)
    report["local_chroma"].append({
        "name": c.name,
        "count": col.count(),
        "metadata": getattr(col, "metadata", None)
    })

remote = chromadb.HttpClient(host="127.0.0.1", port=8002)
for c in remote.list_collections():
    col = remote.get_collection(c.name)
    report["remote_chroma"].append({
        "name": c.name,
PYint(out)ump(report, f, indent=2, default=str))tack_report.json"))record_count, colle
Traceback (most recent call last):
  File "<stdin>", line 12, in <module>
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/models/Collection.py", line 418, in __getattr__
    raise NotImplementedError(
NotImplementedError: In Chroma v0.6.0, list_collections only returns collection names. Use Client.get_collection(gbimwvtractsv2) to access name. See https://docs.trychroma.com/deployment/migration for more information.
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/Downloads/files$ 

