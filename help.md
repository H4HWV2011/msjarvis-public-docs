(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ # Watch the main-brain logs in real time while firing the spatial query
docker logs jarvis-main-brain -f &

curl -s -X POST http://localhost:8050/chat \
  -H "Content-Type: application/json" \
  -H "X-API-Key: super-secret-key" \
  -d '{"message":"Where are bridges in Wyoming County WV?","user_id":"test"}' \
  | python3 -m json.tool | grep -i "gis\|bridge\|spatial\|verified" 

# Kill the background log tail
kill %1
[1] 308118
INFO:     Started server process [10]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8050 (Press CTRL+C to quit)
INFO:     127.0.0.1:58818 - "GET /health HTTP/1.1" 200 OK
INFO:main_brain:
============================================================
INFO:main_brain:🌟 ULTIMATE MS. JARVIS REQUEST
INFO:main_brain:   Message: What food pantries are in Fayette County?
INFO:main_brain:============================================================

INFO:main_brain:Phase 1: Checking service availability... [+0.0s]
INFO:httpx:HTTP Request: GET http://jarvis-qualia-engine:8017/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ qualia_engine
INFO:httpx:HTTP Request: GET http://jarvis-consciousness-bridge:8020/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ consciousness_bridge
INFO:httpx:HTTP Request: GET http://jarvis-blood-brain-barrier:8016/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ blood_brain_barrier
INFO:httpx:HTTP Request: GET http://jarvis-neurobiological-master:8018/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ neurobiological_master
INFO:httpx:HTTP Request: GET http://jarvis-i-containers:8015/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ i_containers
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_spiritual_root-1:7003/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_spiritual_root
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_spiritual_maternal_integration-1:7009/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_spiritual_maternal
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_qualia_engine-1:7008/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_qualia_engine
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_darwin_godel_machines-1:7003/health "HTTP/1.1 500 Internal Server Error"
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_subconscious-1:7011/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_subconscious
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_prefrontal_cortex-1:7005/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_prefrontal_cortex
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_consciousness_containers-1:7002/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_consciousness_containers
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_mother_carrie_protocols-1:7007/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_mother_carrie
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_heteroglobulin_transport-1:7006/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_heteroglobulin
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_blood_brain_barrier-1:7001/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_blood_brain_barrier
INFO:httpx:HTTP Request: GET http://jarvis-woah:7012/health "HTTP/1.0 200 OK"
INFO:main_brain:  ✅ woah_algorithms
INFO:httpx:HTTP Request: GET http://jarvis-20llm-production:8008/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm_production
INFO:httpx:HTTP Request: GET http://jarvis-judge-pipeline:7239/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ judge_pipeline
INFO:httpx:HTTP Request: GET http://jarvis-unified-gateway:8001/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ unified_gateway
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ wv_entangled_gateway
INFO:httpx:HTTP Request: GET http://jarvis-hilbert-gateway:8010/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ hilbert_gateway
INFO:httpx:HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ lm_synthesizer
INFO:httpx:HTTP Request: GET http://jarvis-69dgm-bridge:9000/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ dgm_bridge_69
INFO:httpx:HTTP Request: GET http://jarvis-semaphore:8030/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ semaphore
INFO:httpx:HTTP Request: GET http://jarvis-constitutional-guardian:8091/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ constitutional_guardian
INFO:httpx:HTTP Request: GET http://jarvis-chroma:8000/api/v2/heartbeat "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ chroma
INFO:httpx:HTTP Request: GET http://jarvis-ollama:11434/api/tags "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ ollama
INFO:     172.18.0.54:52186 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: GET http://jarvis-main-brain:8050/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ main_brain
INFO:main_brain:
✅ 27/21 services available

INFO:main_brain:Phase 1.4: Filtering through Blood-Brain Barrier... [+6.4s]
INFO:httpx:HTTP Request: POST http://jarvis-blood-brain-barrier:8016/filter "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ BBB: Query approved and filtered
WARNING:main_brain:  ⚠️  Local resources resolver: All connection attempts failed
INFO:httpx:HTTP Request: GET http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-ollama:11434/api/embed "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/e7e83578-973e-474e-a6d4-ea91d5d5289d/query "HTTP/1.1 400 Bad Request"
INFO:main_brain:  📚 Corpus sufficiency: False
INFO:httpx:HTTP Request: POST http://jarvis-aaacpe-rag:8032/search "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ AaaCPE: Cultural context retrieved
INFO:main_brain:  ✅ AaaCPE context injected into main pipeline
INFO:main_brain:Phase 1.75: Activating corporeal consciousness... [+7.1s]
INFO:httpx:HTTP Request: POST http://jarvis-i-containers:8015/process "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Corporeal: Dual awareness active, coherence: False
INFO:main_brain:🌟 Activating ALL consciousness layers... [+7.1s]
INFO:main_brain:Phase 3: Querying reasoning and knowledge services... [+7.1s]
INFO:main_brain:Phase 2.5: Gathering 20-LLM consensus... [+7.1s]
INFO:httpx:HTTP Request: POST http://jarvis-20llm-production:8008/chat "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ 20-LLM Production: Consensus achieved
INFO:httpx:HTTP Request: POST http://jarvis-qualia-engine:8017/communicate "HTTP/1.1 200 OK"
INFO:main_brain:DEBUG qualia_engine appended to services_used
INFO:main_brain:  ✅ Qualia Engine: Phenomenal processing complete
INFO:httpx:HTTP Request: POST http://jarvis-neurobiological-master:8018/neural_process?input=What+food+pantries+are+in+Fayette+County%3F&text=What+food+pantries+are+in+Fayette+County%3F&kwargs=%7B%27user_id%27%3A+%27cakidd%27%7D "HTTP/1.1 200 OK"
INFO:main_brain:DEBUG neurobiological_master appended to services_used
INFO:main_brain:  ✅ Neuro Master: Neural processing complete
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.0 200 OK"
INFO:main_brain:  ✅ WOAH Algorithms: Processing complete
INFO:httpx:HTTP Request: POST http://jarvis-i-containers:8015/process_full "HTTP/1.1 200 OK"
INFO:main_brain:DEBUG i_containers appended to services_used
INFO:main_brain:  ✅ I-Containers: Identity processing complete
INFO:main_brain:Phase 3: Calling judge_pipeline... [+8.8s]
INFO:httpx:HTTP Request: POST http://jarvis-judge-pipeline:7239/evaluate "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Judge Pipeline: Meta-judgment complete
INFO:main_brain:Phase 3.5: LM Synthesizer voice delivery... [+9.1s]
INFO:httpx:HTTP Request: POST http://jarvis-lm-synthesizer:8001/chat "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ LM Synthesizer voice complete: 255 chars
INFO:main_brain:
Phase 4: Synthesizing ultimate response... [+13.7s]

INFO:httpx:HTTP Request: POST http://jarvis-consciousness-bridge:8020/chat "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Consciousness Bridge: Host consciousness aligned (with KB context)
INFO:main_brain:📝 Queued: What food pantries are in Fayette County...
INFO:     172.18.0.1:42100 - "POST /chat HTTP/1.1" 200 OK
INFO:main_brain:
============================================================
INFO:main_brain:🌟 ULTIMATE MS. JARVIS REQUEST
INFO:main_brain:   Message: What food pantries are in Fayette County?
INFO:main_brain:============================================================

INFO:main_brain:Phase 1: Checking service availability... [+0.0s]
INFO:httpx:HTTP Request: GET http://jarvis-qualia-engine:8017/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ qualia_engine
INFO:httpx:HTTP Request: GET http://jarvis-consciousness-bridge:8020/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ consciousness_bridge
INFO:httpx:HTTP Request: GET http://jarvis-blood-brain-barrier:8016/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ blood_brain_barrier
INFO:httpx:HTTP Request: GET http://jarvis-neurobiological-master:8018/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ neurobiological_master
INFO:httpx:HTTP Request: GET http://jarvis-i-containers:8015/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ i_containers
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_spiritual_root-1:7003/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_spiritual_root
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_spiritual_maternal_integration-1:7009/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_spiritual_maternal
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_qualia_engine-1:7008/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_qualia_engine
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_darwin_godel_machines-1:7003/health "HTTP/1.1 500 Internal Server Error"
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_subconscious-1:7011/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_subconscious
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_prefrontal_cortex-1:7005/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_prefrontal_cortex
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_consciousness_containers-1:7002/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_consciousness_containers
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_mother_carrie_protocols-1:7007/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_mother_carrie
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_heteroglobulin_transport-1:7006/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_heteroglobulin
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_blood_brain_barrier-1:7001/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_blood_brain_barrier
INFO:httpx:HTTP Request: GET http://jarvis-woah:7012/health "HTTP/1.0 200 OK"
INFO:main_brain:  ✅ woah_algorithms
INFO:httpx:HTTP Request: GET http://jarvis-20llm-production:8008/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm_production
INFO:httpx:HTTP Request: GET http://jarvis-judge-pipeline:7239/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ judge_pipeline
INFO:httpx:HTTP Request: GET http://jarvis-unified-gateway:8001/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ unified_gateway
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ wv_entangled_gateway
INFO:httpx:HTTP Request: GET http://jarvis-hilbert-gateway:8010/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ hilbert_gateway
INFO:httpx:HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ lm_synthesizer
INFO:httpx:HTTP Request: GET http://jarvis-69dgm-bridge:9000/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ dgm_bridge_69
INFO:httpx:HTTP Request: GET http://jarvis-semaphore:8030/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ semaphore
INFO:httpx:HTTP Request: GET http://jarvis-constitutional-guardian:8091/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ constitutional_guardian
INFO:httpx:HTTP Request: GET http://jarvis-chroma:8000/api/v2/heartbeat "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ chroma
INFO:httpx:HTTP Request: GET http://jarvis-ollama:11434/api/tags "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ ollama
INFO:     172.18.0.54:36332 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: GET http://jarvis-main-brain:8050/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ main_brain
INFO:main_brain:
✅ 27/21 services available

INFO:main_brain:Phase 1.4: Filtering through Blood-Brain Barrier... [+4.6s]
INFO:httpx:HTTP Request: POST http://jarvis-blood-brain-barrier:8016/filter "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ BBB: Query approved and filtered
WARNING:main_brain:  ⚠️  Local resources resolver: All connection attempts failed
INFO:httpx:HTTP Request: GET http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-ollama:11434/api/embed "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/e7e83578-973e-474e-a6d4-ea91d5d5289d/query "HTTP/1.1 400 Bad Request"
INFO:main_brain:  📚 Corpus sufficiency: False
INFO:httpx:HTTP Request: POST http://jarvis-aaacpe-rag:8032/search "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ AaaCPE: Cultural context retrieved
INFO:main_brain:  ✅ AaaCPE context injected into main pipeline
INFO:main_brain:Phase 1.75: Activating corporeal consciousness... [+5.3s]
INFO:httpx:HTTP Request: POST http://jarvis-i-containers:8015/process "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Corporeal: Dual awareness active, coherence: False
INFO:main_brain:🌟 Activating ALL consciousness layers... [+5.3s]
INFO:main_brain:Phase 3: Querying reasoning and knowledge services... [+5.3s]
INFO:main_brain:Phase 2.5: Gathering 20-LLM consensus... [+5.3s]
INFO:httpx:HTTP Request: POST http://jarvis-20llm-production:8008/chat "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ 20-LLM Production: Consensus achieved
INFO:httpx:HTTP Request: POST http://jarvis-qualia-engine:8017/communicate "HTTP/1.1 200 OK"
INFO:main_brain:DEBUG qualia_engine appended to services_used
INFO:main_brain:  ✅ Qualia Engine: Phenomenal processing complete
INFO:httpx:HTTP Request: POST http://jarvis-neurobiological-master:8018/neural_process?input=What+food+pantries+are+in+Fayette+County%3F&text=What+food+pantries+are+in+Fayette+County%3F&kwargs=%7B%27user_id%27%3A+%27cakidd%27%7D "HTTP/1.1 200 OK"
INFO:main_brain:DEBUG neurobiological_master appended to services_used
INFO:main_brain:  ✅ Neuro Master: Neural processing complete
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.0 200 OK"
INFO:main_brain:  ✅ WOAH Algorithms: Processing complete
INFO:httpx:HTTP Request: POST http://jarvis-i-containers:8015/process_full "HTTP/1.1 200 OK"
INFO:main_brain:DEBUG i_containers appended to services_used
INFO:main_brain:  ✅ I-Containers: Identity processing complete
INFO:main_brain:Phase 3: Calling judge_pipeline... [+6.8s]
INFO:httpx:HTTP Request: POST http://jarvis-judge-pipeline:7239/evaluate "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Judge Pipeline: Meta-judgment complete
INFO:main_brain:Phase 3.5: LM Synthesizer voice delivery... [+7.0s]
INFO:httpx:HTTP Request: POST http://jarvis-lm-synthesizer:8001/chat "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ LM Synthesizer voice complete: 366 chars
INFO:main_brain:
Phase 4: Synthesizing ultimate response... [+9.0s]

INFO:httpx:HTTP Request: POST http://jarvis-consciousness-bridge:8020/chat "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Consciousness Bridge: Host consciousness aligned (with KB context)
INFO:main_brain:📝 Queued: What food pantries are in Fayette County...
INFO:     172.18.0.1:43544 - "POST /ultimate_chat HTTP/1.1" 200 OK
INFO:     127.0.0.1:52740 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44558 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39792 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59450 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:47796 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48718 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40884 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:54844 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40620 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57294 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57330 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51714 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34778 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59704 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:54698 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:60508 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:58490 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34254 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50208 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43408 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:37514 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:48910 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46738 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39014 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44416 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51852 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:35092 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56166 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44730 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51124 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40968 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46862 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48452 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56672 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36968 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43552 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37614 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36448 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:52050 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49384 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53874 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:54596 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39584 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:49402 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:42170 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59046 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53100 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34444 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:36240 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53850 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59176 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39678 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:39212 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:49154 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43492 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53946 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46104 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38758 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44994 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:35746 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:36530 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:52330 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43458 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38666 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:35842 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:42448 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51854 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59594 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:42364 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43114 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39986 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59516 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40842 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44860 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45440 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51388 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50264 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48728 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40926 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43310 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46364 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:32816 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34810 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45274 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:59658 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:49142 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40620 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53122 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43712 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56636 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38802 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34742 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34146 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:60962 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37850 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49198 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36234 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41092 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34068 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:47386 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41132 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40940 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53924 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56108 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:54444 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49736 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53522 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43316 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50534 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36658 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:47116 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:32996 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51790 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:57384 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46174 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44120 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:35884 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:47744 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45674 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:35064 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51986 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49568 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49730 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53054 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59524 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39704 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44492 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38502 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56624 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51464 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45096 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50114 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51238 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41026 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45544 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:35786 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44034 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50550 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40142 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:33886 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45820 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39430 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:54864 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43202 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34494 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43944 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57784 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:46478 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:60380 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51830 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56538 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37536 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53492 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:54762 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36146 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44022 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:42458 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:35578 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:58698 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:35780 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59832 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:35270 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36188 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49572 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37168 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48344 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37840 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43364 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48950 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45686 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51142 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56812 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:55426 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57190 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39782 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39386 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50342 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44094 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:51366 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:55792 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57404 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40820 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43502 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:54214 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45860 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:58006 - "GET /health HTTP/1.1" 200 OK
INFO:main_brain:
============================================================
INFO:main_brain:🌟 ULTIMATE MS. JARVIS REQUEST
INFO:main_brain:   Message: What food resources are available in Fayette County?
INFO:main_brain:============================================================

INFO:main_brain:Phase 1: Checking service availability... [+0.0s]
INFO:httpx:HTTP Request: GET http://jarvis-qualia-engine:8017/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ qualia_engine
INFO:httpx:HTTP Request: GET http://jarvis-consciousness-bridge:8020/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ consciousness_bridge
INFO:httpx:HTTP Request: GET http://jarvis-blood-brain-barrier:8016/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ blood_brain_barrier
INFO:httpx:HTTP Request: GET http://jarvis-neurobiological-master:8018/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ neurobiological_master
INFO:httpx:HTTP Request: GET http://jarvis-i-containers:8015/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ i_containers
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_spiritual_root-1:7003/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_spiritual_root
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_spiritual_maternal_integration-1:7009/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_spiritual_maternal
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_qualia_engine-1:7008/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_qualia_engine
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_darwin_godel_machines-1:7003/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_darwin_godel
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_subconscious-1:7011/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_subconscious
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_prefrontal_cortex-1:7005/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_prefrontal_cortex
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_consciousness_containers-1:7002/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_consciousness_containers
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_mother_carrie_protocols-1:7007/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_mother_carrie
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_heteroglobulin_transport-1:7006/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_heteroglobulin
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_blood_brain_barrier-1:7001/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_blood_brain_barrier
INFO:httpx:HTTP Request: GET http://jarvis-woah:7012/health "HTTP/1.0 200 OK"
INFO:main_brain:  ✅ woah_algorithms
INFO:httpx:HTTP Request: GET http://jarvis-20llm-production:8008/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm_production
INFO:httpx:HTTP Request: GET http://jarvis-judge-pipeline:7239/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ judge_pipeline
INFO:httpx:HTTP Request: GET http://jarvis-swarm-intelligence:8021/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ swarm_intelligence
INFO:httpx:HTTP Request: GET http://jarvis-mother-protocols:4000/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ mother_protocols
INFO:httpx:HTTP Request: GET http://jarvis-temporal-consciousness:7007/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ temporal_consciousness
INFO:httpx:HTTP Request: GET http://jarvis-gis-rag:8004/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ gis_rag
INFO:httpx:HTTP Request: GET http://jarvis-spiritual-rag:8005/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ spiritual_rag
INFO:httpx:HTTP Request: GET http://jarvis-agents-service:8005/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ agents_service
INFO:httpx:HTTP Request: GET http://jarvis-unified-gateway:8001/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ unified_gateway
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ wv_entangled_gateway
INFO:httpx:HTTP Request: GET http://jarvis-hilbert-gateway:8010/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ hilbert_gateway
INFO:httpx:HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ lm_synthesizer
INFO:httpx:HTTP Request: GET http://jarvis-fifth-dgm:4002/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ fifth_dgm
INFO:httpx:HTTP Request: GET http://jarvis-69dgm-bridge:9000/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ dgm_bridge_69
INFO:httpx:HTTP Request: GET http://jarvis-semaphore:8030/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ semaphore
INFO:httpx:HTTP Request: GET http://jarvis-constitutional-guardian:8091/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ constitutional_guardian
INFO:httpx:HTTP Request: GET http://jarvis-chroma:8000/api/v2/heartbeat "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ chroma
INFO:httpx:HTTP Request: GET http://jarvis-ollama:11434/api/tags "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ ollama
INFO:httpx:HTTP Request: GET http://llm1-proxy:8201/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm1
INFO:httpx:HTTP Request: GET http://llm2-proxy:8202/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm2
INFO:httpx:HTTP Request: GET http://llm3-proxy:8203/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm3
INFO:httpx:HTTP Request: GET http://llm4-proxy:8204/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm4
INFO:httpx:HTTP Request: GET http://llm5-proxy:8205/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm5
INFO:httpx:HTTP Request: GET http://llm6-proxy:8206/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm6
INFO:httpx:HTTP Request: GET http://llm7-proxy:8207/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm7
INFO:httpx:HTTP Request: GET http://llm8-proxy:8208/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm8
INFO:httpx:HTTP Request: GET http://llm9-proxy:8209/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm9
INFO:httpx:HTTP Request: GET http://llm10-proxy:8210/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm10
INFO:httpx:HTTP Request: GET http://llm11-proxy:8211/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm11
INFO:httpx:HTTP Request: GET http://llm12-proxy:8212/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm12
INFO:httpx:HTTP Request: GET http://llm13-proxy:8213/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm13
INFO:httpx:HTTP Request: GET http://llm14-proxy:8214/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm14
INFO:httpx:HTTP Request: GET http://llm15-proxy:8215/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm15
INFO:httpx:HTTP Request: GET http://llm16-proxy:8216/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm16
INFO:httpx:HTTP Request: GET http://llm17-proxy:8217/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm17
INFO:httpx:HTTP Request: GET http://llm18-proxy:8218/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm18
INFO:httpx:HTTP Request: GET http://llm19-proxy:8219/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm19
INFO:httpx:HTTP Request: GET http://llm20-proxy:8220/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm20
INFO:httpx:HTTP Request: GET http://llm21-proxy:8221/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm21
INFO:httpx:HTTP Request: GET http://llm22-proxy:8222/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm22
INFO:     172.18.0.54:36816 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: GET http://jarvis-main-brain:8050/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ main_brain
INFO:main_brain:
✅ 57/21 services available

INFO:main_brain:Phase 1.4: Filtering through Blood-Brain Barrier... [+2.5s]
INFO:httpx:HTTP Request: POST http://jarvis-blood-brain-barrier:8016/filter "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ BBB: Query approved and filtered
WARNING:main_brain:  ⚠️  Local resources resolver: All connection attempts failed
INFO:httpx:HTTP Request: GET http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-ollama:11434/api/embed "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/e7e83578-973e-474e-a6d4-ea91d5d5289d/query "HTTP/1.1 400 Bad Request"
INFO:main_brain:  📚 Corpus sufficiency: False
INFO:     127.0.0.1:57154 - "GET /health HTTP/1.1" 200 OK
WARNING:main_brain:  ⚠️ AaaCPE context failed: 
INFO:main_brain:  ℹ️ AaaCPE: No context injected
INFO:main_brain:Phase 1.75: Activating corporeal consciousness... [+12.7s]
INFO:httpx:HTTP Request: POST http://jarvis-i-containers:8015/process "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Corporeal: Dual awareness active, coherence: False
INFO:main_brain:🌟 Activating ALL consciousness layers... [+12.8s]
INFO:main_brain:Phase 3: Querying reasoning and knowledge services... [+12.8s]
INFO:httpx:HTTP Request: POST http://jarvis-agents-service:8005/query/enhance "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Agents: Multi-agent reasoning complete
INFO:httpx:HTTP Request: POST http://jarvis-swarm-intelligence:8021/swarm/query "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Swarm: Collective intelligence processed
INFO:httpx:HTTP Request: POST http://jarvis-fifth-dgm:4002/analyze "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Fifth DGM: Self-improvement analyzed
INFO:main_brain:Phase 2.5: Gathering 20-LLM consensus... [+12.8s]
INFO:     127.0.0.1:51194 - "GET /health HTTP/1.1" 200 OK
WARNING:main_brain:  ⚠️  20-LLM Production: 
INFO:httpx:HTTP Request: POST http://jarvis-qualia-engine:8017/communicate "HTTP/1.1 200 OK"
INFO:main_brain:DEBUG qualia_engine appended to services_used
INFO:main_brain:  ✅ Qualia Engine: Phenomenal processing complete
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.0 200 OK"
INFO:main_brain:  ✅ WOAH Algorithms: Processing complete
INFO:httpx:HTTP Request: POST http://jarvis-i-containers:8015/process_full "HTTP/1.1 200 OK"
INFO:main_brain:DEBUG i_containers appended to services_used
INFO:main_brain:  ✅ I-Containers: Identity processing complete
INFO:main_brain:Phase 3: Calling judge_pipeline... [+63.0s]
INFO:     127.0.0.1:57412 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-judge-pipeline:7239/evaluate "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Judge Pipeline: Meta-judgment complete
INFO:main_brain:Phase 3.5: LM Synthesizer voice delivery... [+75.5s]
WARNING:main_brain:  ⚠️  LM Synthesizer error: 
INFO:main_brain:
Phase 4: Synthesizing ultimate response... [+90.6s]

INFO:     127.0.0.1:54886 - "GET /health HTTP/1.1" 200 OK
WARNING:main_brain:  ⚠️  Consciousness Bridge error: 
INFO:main_brain:📝 Queued: What food resources are available in Fay...
INFO:     172.18.0.1:60326 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.1:40288 - "GET /judges/status HTTP/1.1" 404 Not Found
INFO:     172.18.0.1:40294 - "POST /chat HTTP/1.1" 422 Unprocessable Entity
INFO:     172.18.0.1:36784 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56694 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37518 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:58746 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34286 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48028 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39844 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37202 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34296 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:52728 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:42556 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:47736 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37498 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:60172 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59112 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:47180 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57624 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50344 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53812 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:40930 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:41508 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39910 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37932 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34614 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37006 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46004 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46230 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39268 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:52126 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44072 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59954 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37744 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:54622 - "GET /health HTTP/1.1" 200 OK
INFO:main_brain:
============================================================
INFO:main_brain:🌟 ULTIMATE MS. JARVIS REQUEST
INFO:main_brain:   Message: What food pantries are available in Fayette County?
INFO:main_brain:============================================================

INFO:main_brain:Phase 1: Checking service availability... [+0.0s]
INFO:httpx:HTTP Request: GET http://jarvis-qualia-engine:8017/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ qualia_engine
INFO:httpx:HTTP Request: GET http://jarvis-consciousness-bridge:8020/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ consciousness_bridge
INFO:httpx:HTTP Request: GET http://jarvis-blood-brain-barrier:8016/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ blood_brain_barrier
INFO:httpx:HTTP Request: GET http://jarvis-neurobiological-master:8018/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ neurobiological_master
INFO:httpx:HTTP Request: GET http://jarvis-i-containers:8015/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ i_containers
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_spiritual_root-1:7003/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_spiritual_root
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_spiritual_maternal_integration-1:7009/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_spiritual_maternal
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_qualia_engine-1:7008/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_qualia_engine
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_darwin_godel_machines-1:7003/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_darwin_godel
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_subconscious-1:7011/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_subconscious
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_prefrontal_cortex-1:7005/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_prefrontal_cortex
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_consciousness_containers-1:7002/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_consciousness_containers
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_mother_carrie_protocols-1:7007/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_mother_carrie
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_heteroglobulin_transport-1:7006/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_heteroglobulin
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_blood_brain_barrier-1:7001/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_blood_brain_barrier
INFO:httpx:HTTP Request: GET http://jarvis-woah:7012/health "HTTP/1.0 200 OK"
INFO:main_brain:  ✅ woah_algorithms
INFO:httpx:HTTP Request: GET http://jarvis-20llm-production:8008/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm_production
INFO:httpx:HTTP Request: GET http://jarvis-judge-pipeline:7239/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ judge_pipeline
INFO:httpx:HTTP Request: GET http://jarvis-swarm-intelligence:8021/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ swarm_intelligence
INFO:httpx:HTTP Request: GET http://jarvis-mother-protocols:4000/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ mother_protocols
INFO:httpx:HTTP Request: GET http://jarvis-temporal-consciousness:7007/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ temporal_consciousness
INFO:httpx:HTTP Request: GET http://jarvis-gis-rag:8004/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ gis_rag
INFO:httpx:HTTP Request: GET http://jarvis-spiritual-rag:8005/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ spiritual_rag
INFO:httpx:HTTP Request: GET http://jarvis-agents-service:8005/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ agents_service
INFO:httpx:HTTP Request: GET http://jarvis-unified-gateway:8001/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ unified_gateway
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ wv_entangled_gateway
INFO:httpx:HTTP Request: GET http://jarvis-hilbert-gateway:8010/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ hilbert_gateway
INFO:httpx:HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ lm_synthesizer
INFO:httpx:HTTP Request: GET http://jarvis-fifth-dgm:4002/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ fifth_dgm
INFO:httpx:HTTP Request: GET http://jarvis-69dgm-bridge:9000/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ dgm_bridge_69
INFO:httpx:HTTP Request: GET http://jarvis-semaphore:8030/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ semaphore
INFO:httpx:HTTP Request: GET http://jarvis-constitutional-guardian:8091/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ constitutional_guardian
INFO:httpx:HTTP Request: GET http://jarvis-chroma:8000/api/v2/heartbeat "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ chroma
INFO:httpx:HTTP Request: GET http://jarvis-ollama:11434/api/tags "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ ollama
INFO:httpx:HTTP Request: GET http://llm1-proxy:8201/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm1
INFO:httpx:HTTP Request: GET http://llm2-proxy:8202/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm2
INFO:httpx:HTTP Request: GET http://llm3-proxy:8203/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm3
INFO:httpx:HTTP Request: GET http://llm4-proxy:8204/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm4
INFO:httpx:HTTP Request: GET http://llm5-proxy:8205/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm5
INFO:httpx:HTTP Request: GET http://llm6-proxy:8206/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm6
INFO:httpx:HTTP Request: GET http://llm7-proxy:8207/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm7
INFO:httpx:HTTP Request: GET http://llm8-proxy:8208/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm8
INFO:httpx:HTTP Request: GET http://llm9-proxy:8209/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm9
INFO:httpx:HTTP Request: GET http://llm10-proxy:8210/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm10
INFO:httpx:HTTP Request: GET http://llm11-proxy:8211/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm11
INFO:httpx:HTTP Request: GET http://llm12-proxy:8212/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm12
INFO:httpx:HTTP Request: GET http://llm13-proxy:8213/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm13
INFO:httpx:HTTP Request: GET http://llm14-proxy:8214/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm14
INFO:httpx:HTTP Request: GET http://llm15-proxy:8215/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm15
INFO:httpx:HTTP Request: GET http://llm16-proxy:8216/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm16
INFO:httpx:HTTP Request: GET http://llm17-proxy:8217/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm17
INFO:httpx:HTTP Request: GET http://llm18-proxy:8218/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm18
INFO:httpx:HTTP Request: GET http://llm19-proxy:8219/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm19
INFO:httpx:HTTP Request: GET http://llm20-proxy:8220/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm20
INFO:httpx:HTTP Request: GET http://llm21-proxy:8221/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm21
INFO:httpx:HTTP Request: GET http://llm22-proxy:8222/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm22
INFO:     172.18.0.54:39234 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: GET http://jarvis-main-brain:8050/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ main_brain
INFO:main_brain:
✅ 57/21 services available

INFO:main_brain:Phase 1.4: Filtering through Blood-Brain Barrier... [+2.8s]
INFO:httpx:HTTP Request: POST http://jarvis-blood-brain-barrier:8016/filter "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ BBB: Query approved and filtered
WARNING:main_brain:  ⚠️  Local resources resolver: All connection attempts failed
INFO:httpx:HTTP Request: GET http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-ollama:11434/api/embed "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/e7e83578-973e-474e-a6d4-ea91d5d5289d/query "HTTP/1.1 400 Bad Request"
INFO:main_brain:  📚 Corpus sufficiency: False
INFO:httpx:HTTP Request: POST http://jarvis-aaacpe-rag:8032/search "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ AaaCPE: Cultural context retrieved
INFO:main_brain:  ✅ AaaCPE context injected into main pipeline
INFO:main_brain:Phase 1.75: Activating corporeal consciousness... [+8.0s]
INFO:httpx:HTTP Request: POST http://jarvis-i-containers:8015/process "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Corporeal: Dual awareness active, coherence: False
INFO:main_brain:🌟 Activating ALL consciousness layers... [+8.1s]
INFO:main_brain:Phase 3: Querying reasoning and knowledge services... [+8.1s]
INFO:httpx:HTTP Request: POST http://jarvis-agents-service:8005/query/enhance "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Agents: Multi-agent reasoning complete
INFO:httpx:HTTP Request: POST http://jarvis-swarm-intelligence:8021/swarm/query "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Swarm: Collective intelligence processed
INFO:httpx:HTTP Request: POST http://jarvis-fifth-dgm:4002/analyze "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Fifth DGM: Self-improvement analyzed
INFO:main_brain:Phase 2.5: Gathering 20-LLM consensus... [+8.2s]
INFO:     127.0.0.1:47496 - "GET /health HTTP/1.1" 200 OK
WARNING:main_brain:  ⚠️  20-LLM Production: 
INFO:httpx:HTTP Request: POST http://jarvis-qualia-engine:8017/communicate "HTTP/1.1 200 OK"
INFO:main_brain:DEBUG qualia_engine appended to services_used
INFO:main_brain:  ✅ Qualia Engine: Phenomenal processing complete
INFO:     127.0.0.1:58602 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.0 200 OK"
INFO:main_brain:  ✅ WOAH Algorithms: Processing complete
INFO:httpx:HTTP Request: POST http://jarvis-i-containers:8015/process_full "HTTP/1.1 200 OK"
INFO:main_brain:DEBUG i_containers appended to services_used
INFO:main_brain:  ✅ I-Containers: Identity processing complete
INFO:main_brain:Phase 3: Calling judge_pipeline... [+58.5s]
INFO:httpx:HTTP Request: POST http://jarvis-judge-pipeline:7239/evaluate "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Judge Pipeline: Meta-judgment complete
INFO:main_brain:Phase 3.5: LM Synthesizer voice delivery... [+71.0s]
INFO:     127.0.0.1:50654 - "GET /health HTTP/1.1" 200 OK
WARNING:main_brain:  ⚠️  LM Synthesizer error: 
INFO:main_brain:
Phase 4: Synthesizing ultimate response... [+86.0s]

WARNING:main_brain:  ⚠️  Consciousness Bridge error: 
INFO:main_brain:📝 Queued: What food pantries are available in Faye...
INFO:     172.18.0.1:42652 - "POST /chat HTTP/1.1" 200 OK
INFO:     127.0.0.1:38226 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56366 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57696 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:33920 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44490 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38546 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49904 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37850 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46842 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48042 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49264 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38298 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:47360 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40912 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:32956 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:52676 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41906 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:55058 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40026 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44570 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:42298 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39848 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:33364 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:58704 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:32964 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:54880 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53670 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:33378 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41556 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51844 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44016 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34798 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:59556 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45232 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48432 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49246 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48398 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:43644 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39822 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34960 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51246 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56186 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37482 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:55406 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45674 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38940 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:58542 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57144 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46808 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:39488 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:54862 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36982 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36700 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57922 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37102 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48978 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56098 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:47052 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57810 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:35866 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56580 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:47442 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:60408 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46372 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:58542 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:33216 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37948 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:47590 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36356 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38654 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44368 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48070 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49654 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50900 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36380 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:54750 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53600 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:34584 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40602 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57016 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40928 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:39886 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:42618 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48474 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53224 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41190 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:52530 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36132 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45460 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45336 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:44730 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:33336 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59350 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43378 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36578 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37602 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45262 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45730 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49568 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39490 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34790 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36860 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39860 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:60764 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38214 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45014 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43532 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:35606 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51770 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48962 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48152 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:47546 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:33748 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:48064 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:49598 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37680 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:47548 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40290 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56382 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56390 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36718 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:42108 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53704 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57092 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50512 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48818 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51730 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39468 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:52706 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45522 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38320 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49912 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:47958 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:55096 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40696 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50118 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:47450 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56404 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:33286 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36318 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:60312 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:35998 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51808 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:40060 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:36996 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51164 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38096 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34280 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:33234 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:47514 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44008 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50786 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:58838 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53572 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45288 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43950 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43678 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53154 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37014 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:58802 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36566 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51158 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:47096 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:60516 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39846 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38808 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45940 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:55302 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49078 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44370 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:54262 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:35952 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50626 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50896 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:38962 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:40374 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45414 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41890 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39678 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44876 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:33570 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:55152 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49144 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:52072 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:55236 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:54054 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:52356 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36568 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:33094 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46542 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:42952 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46056 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39650 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46932 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59264 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46218 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59654 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44894 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59692 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41232 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:35276 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44252 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51584 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44232 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:33730 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:56228 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:51138 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37974 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43058 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:52054 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:58456 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45534 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34822 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51198 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:35906 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:35142 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51190 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:35962 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53390 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50586 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43256 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39548 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43984 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49356 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:60658 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:33436 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56514 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51114 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37442 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46808 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50400 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:58958 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:55098 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50700 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53718 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:42192 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:51658 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:50066 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:47094 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46514 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44842 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:47154 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:33644 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34780 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36950 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56840 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46854 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41840 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59698 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44958 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41992 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:52260 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40162 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57890 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48760 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45676 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38668 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48674 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:32924 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:33506 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:35172 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:60082 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34334 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44560 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48172 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46380 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56520 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:49406 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:39174 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45940 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51180 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53026 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38242 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:60338 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41044 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50228 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37122 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56614 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44414 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51194 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40084 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49240 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:55682 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41810 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:47118 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44274 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40948 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41832 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:35180 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41180 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46106 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34950 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50872 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:60120 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57420 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49204 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:47054 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46166 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:60220 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:53294 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:54928 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37316 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51574 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:58122 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37310 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36864 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59996 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57172 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40808 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38294 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50384 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49078 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53146 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49970 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51982 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:60536 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56814 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51908 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:52200 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59258 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48130 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53294 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56280 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39974 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56778 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36570 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:54032 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36438 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:51220 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:60412 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34286 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:52026 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34440 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57378 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48252 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48986 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37790 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:58864 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53314 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:47312 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43686 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37102 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48548 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37576 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48868 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38776 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:60662 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49236 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51662 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45104 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49606 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56502 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:32932 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49488 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50796 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48834 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:60060 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:33396 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:52852 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:49584 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:48508 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36710 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53114 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:33658 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:58462 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51216 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57090 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48736 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46880 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34292 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:52564 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59816 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53022 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48186 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37436 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56194 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45202 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46240 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:60244 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49196 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46674 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:42614 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:32934 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59962 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37428 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38734 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:56142 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50638 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37324 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34276 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44724 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57534 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:60776 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:37596 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:42286 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34082 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38700 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56682 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:33310 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36080 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34344 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:52104 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43514 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:54138 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:54736 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:47232 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46670 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:32894 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46512 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:58486 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53564 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38822 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:54634 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34004 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:42856 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56940 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46212 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40970 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50486 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59234 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39388 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48028 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59878 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:55990 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:38526 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45870 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:54032 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:58170 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34802 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:60354 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51282 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:52278 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37314 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40374 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49568 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41128 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40890 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56750 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:58534 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59180 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:47152 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59374 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49394 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59834 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57402 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40272 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43504 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37906 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50924 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:55126 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44186 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38002 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48682 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56084 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:52338 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:33582 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56252 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:42484 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56684 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51252 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51218 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38116 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38924 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:60124 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59940 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:60750 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39288 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:60900 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45824 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48070 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34150 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48558 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:54066 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41846 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57666 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56080 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45682 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45868 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48704 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:33236 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56516 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:55862 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46598 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49788 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:42386 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:50852 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:55524 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:42996 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36530 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43392 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:58116 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40416 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:60622 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45572 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56180 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39708 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:54412 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39070 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36216 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59910 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38128 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49002 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50420 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59436 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:58330 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:55658 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53680 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57204 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41870 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50100 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36502 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44424 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:35690 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37050 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38374 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:59760 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:54704 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45980 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53804 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46000 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46496 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:58682 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53388 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:52466 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:35458 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45436 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:60858 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40360 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46398 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36758 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39730 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41110 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:47612 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59608 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44502 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:60694 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57558 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34776 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46382 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56228 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:54286 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45046 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:52622 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38346 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51956 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39488 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:48044 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:47054 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51336 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41178 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:33554 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53970 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45678 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53900 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56750 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57778 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46542 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45366 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59600 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41718 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46784 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:47858 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45882 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41414 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56266 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:47872 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41888 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57314 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49486 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50168 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38484 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38284 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:55238 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59944 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:55598 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40222 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43612 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:43124 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:60182 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51876 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56966 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40212 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43146 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:54410 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57914 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39822 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46090 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37738 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:58344 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45118 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:32788 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:58546 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44328 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:60352 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57454 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51738 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44992 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50210 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:42738 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57542 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:33686 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46042 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41080 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:32826 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36776 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:33994 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44434 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49514 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:52828 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:40872 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44952 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45492 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:60910 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45130 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:58776 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49232 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53212 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44322 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36756 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56144 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53374 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:58292 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49336 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57510 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39836 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:60250 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38926 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36390 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:52690 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43426 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41978 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:54188 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44500 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:52026 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:55816 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:52458 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57546 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37404 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49194 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.1:34606 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:38798 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37244 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59320 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48138 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:35926 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43796 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37918 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34236 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34306 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43124 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43572 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:60920 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39408 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38940 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43402 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53004 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59176 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34888 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:42078 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:58992 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51398 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38360 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:58914 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57570 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51334 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:54380 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40450 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39500 - "GET /health HTTP/1.1" 200 OK
INFO:main_brain:
============================================================
INFO:main_brain:🌟 ULTIMATE MS. JARVIS REQUEST
INFO:main_brain:   Message: Where are bridges in Wyoming County WV?
INFO:main_brain:============================================================

INFO:main_brain:Phase 1: Checking service availability... [+0.0s]
INFO:httpx:HTTP Request: GET http://jarvis-qualia-engine:8017/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ qualia_engine
INFO:httpx:HTTP Request: GET http://jarvis-consciousness-bridge:8020/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ consciousness_bridge
INFO:httpx:HTTP Request: GET http://jarvis-blood-brain-barrier:8016/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ blood_brain_barrier
INFO:httpx:HTTP Request: GET http://jarvis-neurobiological-master:8018/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ neurobiological_master
INFO:httpx:HTTP Request: GET http://jarvis-i-containers:8015/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ i_containers
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_spiritual_root-1:7003/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_spiritual_root
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_spiritual_maternal_integration-1:7009/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_spiritual_maternal
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_qualia_engine-1:7008/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_qualia_engine
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_darwin_godel_machines-1:7003/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_darwin_godel
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_subconscious-1:7011/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_subconscious
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_prefrontal_cortex-1:7005/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_prefrontal_cortex
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_consciousness_containers-1:7002/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_consciousness_containers
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_mother_carrie_protocols-1:7007/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_mother_carrie
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_heteroglobulin_transport-1:7006/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_heteroglobulin
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_blood_brain_barrier-1:7001/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_blood_brain_barrier
INFO:httpx:HTTP Request: GET http://jarvis-woah:7012/health "HTTP/1.0 200 OK"
INFO:main_brain:  ✅ woah_algorithms
INFO:httpx:HTTP Request: GET http://jarvis-20llm-production:8008/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm_production
INFO:httpx:HTTP Request: GET http://jarvis-judge-pipeline:7239/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ judge_pipeline
INFO:httpx:HTTP Request: GET http://jarvis-swarm-intelligence:8021/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ swarm_intelligence
INFO:httpx:HTTP Request: GET http://jarvis-mother-protocols:4000/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ mother_protocols
INFO:httpx:HTTP Request: GET http://jarvis-temporal-consciousness:7007/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ temporal_consciousness
INFO:httpx:HTTP Request: GET http://jarvis-gis-rag:8004/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ gis_rag
INFO:httpx:HTTP Request: GET http://jarvis-spiritual-rag:8005/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ spiritual_rag
INFO:httpx:HTTP Request: GET http://jarvis-agents-service:8005/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ agents_service
INFO:httpx:HTTP Request: GET http://jarvis-unified-gateway:8001/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ unified_gateway
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ wv_entangled_gateway
INFO:httpx:HTTP Request: GET http://jarvis-hilbert-gateway:8010/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ hilbert_gateway
INFO:httpx:HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ lm_synthesizer
INFO:httpx:HTTP Request: GET http://jarvis-fifth-dgm:4002/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ fifth_dgm
INFO:httpx:HTTP Request: GET http://jarvis-69dgm-bridge:9000/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ dgm_bridge_69
INFO:httpx:HTTP Request: GET http://jarvis-semaphore:8030/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ semaphore
INFO:httpx:HTTP Request: GET http://jarvis-constitutional-guardian:8091/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ constitutional_guardian
INFO:httpx:HTTP Request: GET http://jarvis-chroma:8000/api/v2/heartbeat "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ chroma
INFO:httpx:HTTP Request: GET http://jarvis-ollama:11434/api/tags "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ ollama
INFO:httpx:HTTP Request: GET http://llm1-proxy:8201/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm1
INFO:httpx:HTTP Request: GET http://llm2-proxy:8202/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm2
INFO:httpx:HTTP Request: GET http://llm3-proxy:8203/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm3
INFO:httpx:HTTP Request: GET http://llm4-proxy:8204/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm4
INFO:httpx:HTTP Request: GET http://llm5-proxy:8205/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm5
INFO:httpx:HTTP Request: GET http://llm6-proxy:8206/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm6
INFO:httpx:HTTP Request: GET http://llm7-proxy:8207/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm7
INFO:httpx:HTTP Request: GET http://llm8-proxy:8208/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm8
INFO:httpx:HTTP Request: GET http://llm9-proxy:8209/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm9
INFO:httpx:HTTP Request: GET http://llm10-proxy:8210/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm10
INFO:httpx:HTTP Request: GET http://llm11-proxy:8211/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm11
INFO:httpx:HTTP Request: GET http://llm12-proxy:8212/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm12
INFO:httpx:HTTP Request: GET http://llm13-proxy:8213/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm13
INFO:httpx:HTTP Request: GET http://llm14-proxy:8214/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm14
INFO:httpx:HTTP Request: GET http://llm15-proxy:8215/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm15
INFO:httpx:HTTP Request: GET http://llm16-proxy:8216/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm16
INFO:httpx:HTTP Request: GET http://llm17-proxy:8217/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm17
INFO:httpx:HTTP Request: GET http://llm18-proxy:8218/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm18
INFO:httpx:HTTP Request: GET http://llm19-proxy:8219/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm19
INFO:httpx:HTTP Request: GET http://llm20-proxy:8220/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm20
INFO:httpx:HTTP Request: GET http://llm21-proxy:8221/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm21
INFO:httpx:HTTP Request: GET http://llm22-proxy:8222/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm22
INFO:     172.18.0.54:38052 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: GET http://jarvis-main-brain:8050/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ main_brain
INFO:main_brain:
✅ 57/21 services available

INFO:main_brain:Phase 1.4: Filtering through Blood-Brain Barrier... [+2.7s]
INFO:httpx:HTTP Request: POST http://jarvis-blood-brain-barrier:8016/filter "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ BBB: Query approved and filtered
WARNING:main_brain:  ⚠️  Local resources resolver: All connection attempts failed
INFO:httpx:HTTP Request: GET http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-ollama:11434/api/embed "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/e7e83578-973e-474e-a6d4-ea91d5d5289d/query "HTTP/1.1 400 Bad Request"
INFO:main_brain:  📚 Corpus sufficiency: False
INFO:httpx:HTTP Request: POST http://jarvis-aaacpe-rag:8032/search "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ AaaCPE: Cultural context retrieved
INFO:main_brain:  ✅ AaaCPE context injected into main pipeline
INFO:main_brain:Phase 1.75: Activating corporeal consciousness... [+3.9s]
INFO:httpx:HTTP Request: POST http://jarvis-i-containers:8015/process "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Corporeal: Dual awareness active, coherence: False
INFO:main_brain:🌟 Activating ALL consciousness layers... [+4.0s]
INFO:main_brain:Phase 3: Querying reasoning and knowledge services... [+4.0s]
INFO:httpx:HTTP Request: POST http://jarvis-agents-service:8005/query/enhance "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Agents: Multi-agent reasoning complete
INFO:httpx:HTTP Request: POST http://jarvis-swarm-intelligence:8021/swarm/query "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Swarm: Collective intelligence processed
INFO:httpx:HTTP Request: POST http://jarvis-fifth-dgm:4002/analyze "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Fifth DGM: Self-improvement analyzed
INFO:main_brain:Phase 2.5: Gathering 20-LLM consensus... [+4.2s]
INFO:     127.0.0.1:41848 - "GET /health HTTP/1.1" 200 OK
WARNING:main_brain:  ⚠️  20-LLM Production: 
INFO:httpx:HTTP Request: POST http://jarvis-qualia-engine:8017/communicate "HTTP/1.1 200 OK"
INFO:main_brain:DEBUG qualia_engine appended to services_used
INFO:main_brain:  ✅ Qualia Engine: Phenomenal processing complete
INFO:     172.18.0.1:34828 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:41182 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.0 200 OK"
INFO:main_brain:  ✅ WOAH Algorithms: Processing complete
INFO:httpx:HTTP Request: POST http://jarvis-i-containers:8015/process_full "HTTP/1.1 200 OK"
INFO:main_brain:DEBUG i_containers appended to services_used
INFO:main_brain:  ✅ I-Containers: Identity processing complete
INFO:main_brain:Phase 3: Calling judge_pipeline... [+54.5s]
INFO:httpx:HTTP Request: POST http://jarvis-judge-pipeline:7239/evaluate "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Judge Pipeline: Meta-judgment complete
INFO:main_brain:Phase 3.5: LM Synthesizer voice delivery... [+66.8s]
INFO:     127.0.0.1:50768 - "GET /health HTTP/1.1" 200 OK
WARNING:main_brain:  ⚠️  LM Synthesizer error: 
INFO:main_brain:
Phase 4: Synthesizing ultimate response... [+81.9s]

WARNING:main_brain:  ⚠️  Consciousness Bridge error: 
INFO:main_brain:📝 Queued: Where are bridges in Wyoming County WV?...
INFO:     172.18.0.1:39590 - "POST /chat HTTP/1.1" 200 OK
INFO:main_brain:
============================================================
INFO:main_brain:🌟 ULTIMATE MS. JARVIS REQUEST
INFO:main_brain:   Message: I live in Logan and need help with food assistance
INFO:main_brain:============================================================

INFO:main_brain:Phase 1: Checking service availability... [+0.0s]
INFO:httpx:HTTP Request: GET http://jarvis-qualia-engine:8017/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ qualia_engine
INFO:httpx:HTTP Request: GET http://jarvis-consciousness-bridge:8020/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ consciousness_bridge
INFO:httpx:HTTP Request: GET http://jarvis-blood-brain-barrier:8016/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ blood_brain_barrier
INFO:httpx:HTTP Request: GET http://jarvis-neurobiological-master:8018/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ neurobiological_master
INFO:httpx:HTTP Request: GET http://jarvis-i-containers:8015/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ i_containers
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_spiritual_root-1:7003/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_spiritual_root
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_spiritual_maternal_integration-1:7009/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_spiritual_maternal
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_qualia_engine-1:7008/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_qualia_engine
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_darwin_godel_machines-1:7003/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_darwin_godel
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_subconscious-1:7011/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_subconscious
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_prefrontal_cortex-1:7005/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_prefrontal_cortex
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_consciousness_containers-1:7002/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_consciousness_containers
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_mother_carrie_protocols-1:7007/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_mother_carrie
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_heteroglobulin_transport-1:7006/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_heteroglobulin
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_blood_brain_barrier-1:7001/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_blood_brain_barrier
INFO:httpx:HTTP Request: GET http://jarvis-woah:7012/health "HTTP/1.0 200 OK"
INFO:main_brain:  ✅ woah_algorithms
INFO:httpx:HTTP Request: GET http://jarvis-20llm-production:8008/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm_production
INFO:httpx:HTTP Request: GET http://jarvis-judge-pipeline:7239/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ judge_pipeline
INFO:httpx:HTTP Request: GET http://jarvis-swarm-intelligence:8021/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ swarm_intelligence
INFO:httpx:HTTP Request: GET http://jarvis-mother-protocols:4000/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ mother_protocols
INFO:httpx:HTTP Request: GET http://jarvis-temporal-consciousness:7007/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ temporal_consciousness
INFO:httpx:HTTP Request: GET http://jarvis-gis-rag:8004/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ gis_rag
INFO:httpx:HTTP Request: GET http://jarvis-spiritual-rag:8005/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ spiritual_rag
INFO:httpx:HTTP Request: GET http://jarvis-agents-service:8005/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ agents_service
INFO:httpx:HTTP Request: GET http://jarvis-unified-gateway:8001/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ unified_gateway
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ wv_entangled_gateway
INFO:httpx:HTTP Request: GET http://jarvis-hilbert-gateway:8010/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ hilbert_gateway
INFO:httpx:HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ lm_synthesizer
INFO:httpx:HTTP Request: GET http://jarvis-fifth-dgm:4002/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ fifth_dgm
INFO:httpx:HTTP Request: GET http://jarvis-69dgm-bridge:9000/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ dgm_bridge_69
INFO:httpx:HTTP Request: GET http://jarvis-semaphore:8030/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ semaphore
INFO:httpx:HTTP Request: GET http://jarvis-constitutional-guardian:8091/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ constitutional_guardian
INFO:httpx:HTTP Request: GET http://jarvis-chroma:8000/api/v2/heartbeat "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ chroma
INFO:httpx:HTTP Request: GET http://jarvis-ollama:11434/api/tags "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ ollama
INFO:httpx:HTTP Request: GET http://llm1-proxy:8201/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm1
INFO:httpx:HTTP Request: GET http://llm2-proxy:8202/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm2
INFO:httpx:HTTP Request: GET http://llm3-proxy:8203/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm3
INFO:httpx:HTTP Request: GET http://llm4-proxy:8204/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm4
INFO:httpx:HTTP Request: GET http://llm5-proxy:8205/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm5
INFO:httpx:HTTP Request: GET http://llm6-proxy:8206/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm6
INFO:httpx:HTTP Request: GET http://llm7-proxy:8207/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm7
INFO:httpx:HTTP Request: GET http://llm8-proxy:8208/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm8
INFO:httpx:HTTP Request: GET http://llm9-proxy:8209/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm9
INFO:httpx:HTTP Request: GET http://llm10-proxy:8210/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm10
INFO:httpx:HTTP Request: GET http://llm11-proxy:8211/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm11
INFO:httpx:HTTP Request: GET http://llm12-proxy:8212/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm12
INFO:httpx:HTTP Request: GET http://llm13-proxy:8213/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm13
INFO:httpx:HTTP Request: GET http://llm14-proxy:8214/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm14
INFO:httpx:HTTP Request: GET http://llm15-proxy:8215/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm15
INFO:httpx:HTTP Request: GET http://llm16-proxy:8216/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm16
INFO:httpx:HTTP Request: GET http://llm17-proxy:8217/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm17
INFO:httpx:HTTP Request: GET http://llm18-proxy:8218/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm18
INFO:httpx:HTTP Request: GET http://llm19-proxy:8219/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm19
INFO:httpx:HTTP Request: GET http://llm20-proxy:8220/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm20
INFO:httpx:HTTP Request: GET http://llm21-proxy:8221/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm21
INFO:httpx:HTTP Request: GET http://llm22-proxy:8222/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm22
INFO:     172.18.0.54:39126 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: GET http://jarvis-main-brain:8050/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ main_brain
INFO:main_brain:
✅ 57/21 services available

INFO:main_brain:Phase 1.4: Filtering through Blood-Brain Barrier... [+4.3s]
INFO:httpx:HTTP Request: POST http://jarvis-blood-brain-barrier:8016/filter "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ BBB: Query approved and filtered
WARNING:main_brain:  ⚠️  Local resources resolver: All connection attempts failed
INFO:httpx:HTTP Request: GET http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections "HTTP/1.1 200 OK"
INFO:     127.0.0.1:43522 - "GET /health HTTP/1.1" 200 OK
WARNING:main_brain:  ⚠️  ChromaDB community memory failed: 
INFO:main_brain:  📚 Corpus sufficiency: False
INFO:httpx:HTTP Request: POST http://jarvis-aaacpe-rag:8032/search "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ AaaCPE: Cultural context retrieved
INFO:main_brain:  ✅ AaaCPE context injected into main pipeline
INFO:main_brain:Phase 1.75: Activating corporeal consciousness... [+40.8s]
INFO:httpx:HTTP Request: POST http://jarvis-i-containers:8015/process "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Corporeal: Dual awareness active, coherence: False
INFO:main_brain:🌟 Activating ALL consciousness layers... [+41.0s]
INFO:main_brain:Phase 3: Querying reasoning and knowledge services... [+41.0s]
INFO:httpx:HTTP Request: POST http://jarvis-agents-service:8005/query/enhance "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Agents: Multi-agent reasoning complete
INFO:httpx:HTTP Request: POST http://jarvis-swarm-intelligence:8021/swarm/query "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Swarm: Collective intelligence processed
INFO:httpx:HTTP Request: POST http://jarvis-fifth-dgm:4002/analyze "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Fifth DGM: Self-improvement analyzed
INFO:main_brain:Phase 2.5: Gathering 20-LLM consensus... [+41.1s]
INFO:     127.0.0.1:38394 - "GET /health HTTP/1.1" 200 OK
WARNING:main_brain:  ⚠️  20-LLM Production: 
INFO:httpx:HTTP Request: POST http://jarvis-qualia-engine:8017/communicate "HTTP/1.1 200 OK"
INFO:main_brain:DEBUG qualia_engine appended to services_used
INFO:main_brain:  ✅ Qualia Engine: Phenomenal processing complete
INFO:     127.0.0.1:38694 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.0 200 OK"
INFO:main_brain:  ✅ WOAH Algorithms: Processing complete
INFO:httpx:HTTP Request: POST http://jarvis-i-containers:8015/process_full "HTTP/1.1 200 OK"
INFO:main_brain:DEBUG i_containers appended to services_used
INFO:main_brain:  ✅ I-Containers: Identity processing complete
INFO:main_brain:Phase 3: Calling judge_pipeline... [+91.4s]
INFO:     127.0.0.1:55708 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-judge-pipeline:7239/evaluate "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Judge Pipeline: Meta-judgment complete
INFO:main_brain:Phase 3.5: LM Synthesizer voice delivery... [+103.7s]
WARNING:main_brain:  ⚠️  LM Synthesizer error: 
INFO:main_brain:
Phase 4: Synthesizing ultimate response... [+118.8s]

WARNING:main_brain:  ⚠️  Consciousness Bridge error: 
INFO:main_brain:📝 Queued: I live in Logan and need help with food ...
INFO:     172.18.0.1:38912 - "POST /chat HTTP/1.1" 200 OK
INFO:     127.0.0.1:48652 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:60070 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50218 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49762 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38344 - "GET /health HTTP/1.1" 200 OK
INFO:main_brain:
============================================================
INFO:main_brain:🌟 ULTIMATE MS. JARVIS REQUEST
INFO:main_brain:   Message: Where are bridges in Wyoming County WV?
INFO:main_brain:============================================================

INFO:main_brain:Phase 1: Checking service availability... [+0.0s]
INFO:httpx:HTTP Request: GET http://jarvis-qualia-engine:8017/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ qualia_engine
INFO:httpx:HTTP Request: GET http://jarvis-consciousness-bridge:8020/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ consciousness_bridge
INFO:httpx:HTTP Request: GET http://jarvis-blood-brain-barrier:8016/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ blood_brain_barrier
INFO:httpx:HTTP Request: GET http://jarvis-neurobiological-master:8018/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ neurobiological_master
INFO:httpx:HTTP Request: GET http://jarvis-i-containers:8015/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ i_containers
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_spiritual_root-1:7003/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_spiritual_root
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_spiritual_maternal_integration-1:7009/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_spiritual_maternal
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_qualia_engine-1:7008/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_qualia_engine
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_darwin_godel_machines-1:7003/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_darwin_godel
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_subconscious-1:7011/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_subconscious
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_prefrontal_cortex-1:7005/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_prefrontal_cortex
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_consciousness_containers-1:7002/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_consciousness_containers
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_mother_carrie_protocols-1:7007/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_mother_carrie
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_heteroglobulin_transport-1:7006/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_heteroglobulin
INFO:httpx:HTTP Request: GET http://msjarvis-rebuild-nbb_blood_brain_barrier-1:7001/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ nbb_blood_brain_barrier
INFO:httpx:HTTP Request: GET http://jarvis-woah:7012/health "HTTP/1.0 200 OK"
INFO:main_brain:  ✅ woah_algorithms
INFO:httpx:HTTP Request: GET http://jarvis-20llm-production:8008/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm_production
INFO:httpx:HTTP Request: GET http://jarvis-judge-pipeline:7239/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ judge_pipeline
INFO:httpx:HTTP Request: GET http://jarvis-swarm-intelligence:8021/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ swarm_intelligence
INFO:httpx:HTTP Request: GET http://jarvis-mother-protocols:4000/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ mother_protocols
INFO:httpx:HTTP Request: GET http://jarvis-temporal-consciousness:7007/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ temporal_consciousness
INFO:httpx:HTTP Request: GET http://jarvis-gis-rag:8004/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ gis_rag
INFO:httpx:HTTP Request: GET http://jarvis-spiritual-rag:8005/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ spiritual_rag
INFO:httpx:HTTP Request: GET http://jarvis-agents-service:8005/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ agents_service
INFO:httpx:HTTP Request: GET http://jarvis-unified-gateway:8001/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ unified_gateway
INFO:httpx:HTTP Request: GET http://jarvis-wv-entangled-gateway:8010/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ wv_entangled_gateway
INFO:httpx:HTTP Request: GET http://jarvis-hilbert-gateway:8010/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ hilbert_gateway
INFO:httpx:HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ lm_synthesizer
INFO:httpx:HTTP Request: GET http://jarvis-fifth-dgm:4002/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ fifth_dgm
INFO:httpx:HTTP Request: GET http://jarvis-69dgm-bridge:9000/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ dgm_bridge_69
INFO:httpx:HTTP Request: GET http://jarvis-semaphore:8030/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ semaphore
INFO:httpx:HTTP Request: GET http://jarvis-constitutional-guardian:8091/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ constitutional_guardian
INFO:httpx:HTTP Request: GET http://jarvis-chroma:8000/api/v2/heartbeat "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ chroma
INFO:httpx:HTTP Request: GET http://jarvis-ollama:11434/api/tags "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ ollama
INFO:httpx:HTTP Request: GET http://llm1-proxy:8201/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm1
INFO:httpx:HTTP Request: GET http://llm2-proxy:8202/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm2
INFO:httpx:HTTP Request: GET http://llm3-proxy:8203/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm3
INFO:httpx:HTTP Request: GET http://llm4-proxy:8204/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm4
INFO:httpx:HTTP Request: GET http://llm5-proxy:8205/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm5
INFO:httpx:HTTP Request: GET http://llm6-proxy:8206/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm6
INFO:httpx:HTTP Request: GET http://llm7-proxy:8207/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm7
INFO:httpx:HTTP Request: GET http://llm8-proxy:8208/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm8
INFO:httpx:HTTP Request: GET http://llm9-proxy:8209/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm9
INFO:httpx:HTTP Request: GET http://llm10-proxy:8210/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm10
INFO:httpx:HTTP Request: GET http://llm11-proxy:8211/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm11
INFO:httpx:HTTP Request: GET http://llm12-proxy:8212/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm12
INFO:httpx:HTTP Request: GET http://llm13-proxy:8213/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm13
INFO:httpx:HTTP Request: GET http://llm14-proxy:8214/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm14
INFO:httpx:HTTP Request: GET http://llm15-proxy:8215/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm15
INFO:httpx:HTTP Request: GET http://llm16-proxy:8216/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm16
INFO:httpx:HTTP Request: GET http://llm17-proxy:8217/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm17
INFO:httpx:HTTP Request: GET http://llm18-proxy:8218/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm18
INFO:httpx:HTTP Request: GET http://llm19-proxy:8219/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm19
INFO:httpx:HTTP Request: GET http://llm20-proxy:8220/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm20
INFO:httpx:HTTP Request: GET http://llm21-proxy:8221/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm21
INFO:httpx:HTTP Request: GET http://llm22-proxy:8222/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ llm22
INFO:     172.18.0.54:45100 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: GET http://jarvis-main-brain:8050/health "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ main_brain
INFO:main_brain:
✅ 57/21 services available

INFO:main_brain:Phase 1.4: Filtering through Blood-Brain Barrier... [+4.8s]
INFO:httpx:HTTP Request: POST http://jarvis-blood-brain-barrier:8016/filter "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ BBB: Query approved and filtered
WARNING:main_brain:  ⚠️  Local resources resolver: All connection attempts failed
INFO:httpx:HTTP Request: GET http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-ollama:11434/api/embed "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/e7e83578-973e-474e-a6d4-ea91d5d5289d/query "HTTP/1.1 400 Bad Request"
INFO:main_brain:  📚 Corpus sufficiency: False
INFO:httpx:HTTP Request: POST http://jarvis-aaacpe-rag:8032/search "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ AaaCPE: Cultural context retrieved
INFO:main_brain:  ✅ AaaCPE context injected into main pipeline
INFO:main_brain:Phase 1.75: Activating corporeal consciousness... [+6.2s]
INFO:httpx:HTTP Request: POST http://jarvis-i-containers:8015/process "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Corporeal: Dual awareness active, coherence: False
INFO:main_brain:🌟 Activating ALL consciousness layers... [+6.3s]
INFO:main_brain:Phase 3: Querying reasoning and knowledge services... [+6.3s]
INFO:httpx:HTTP Request: POST http://jarvis-agents-service:8005/query/enhance "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Agents: Multi-agent reasoning complete
INFO:httpx:HTTP Request: POST http://jarvis-swarm-intelligence:8021/swarm/query "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Swarm: Collective intelligence processed
INFO:httpx:HTTP Request: POST http://jarvis-fifth-dgm:4002/analyze "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Fifth DGM: Self-improvement analyzed
INFO:main_brain:Phase 2.5: Gathering 20-LLM consensus... [+6.4s]
INFO:     127.0.0.1:54950 - "GET /health HTTP/1.1" 200 OK
WARNING:main_brain:  ⚠️  20-LLM Production: 
INFO:httpx:HTTP Request: POST http://jarvis-qualia-engine:8017/communicate "HTTP/1.1 200 OK"
INFO:main_brain:DEBUG qualia_engine appended to services_used
INFO:main_brain:  ✅ Qualia Engine: Phenomenal processing complete
INFO:     127.0.0.1:60374 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.0 200 OK"
INFO:main_brain:  ✅ WOAH Algorithms: Processing complete
INFO:httpx:HTTP Request: POST http://jarvis-i-containers:8015/process_full "HTTP/1.1 200 OK"
INFO:main_brain:DEBUG i_containers appended to services_used
INFO:main_brain:  ✅ I-Containers: Identity processing complete
INFO:main_brain:Phase 3: Calling judge_pipeline... [+56.8s]
INFO:httpx:HTTP Request: POST http://jarvis-judge-pipeline:7239/evaluate "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Judge Pipeline: Meta-judgment complete
INFO:main_brain:Phase 3.5: LM Synthesizer voice delivery... [+69.2s]
WARNING:main_brain:  ⚠️  LM Synthesizer error: 
INFO:main_brain:
Phase 4: Synthesizing ultimate response... [+84.3s]

INFO:     127.0.0.1:44550 - "GET /health HTTP/1.1" 200 OK
WARNING:main_brain:  ⚠️  Consciousness Bridge error: 
INFO:main_brain:📝 Queued: Where are bridges in Wyoming County WV?...
INFO:     172.18.0.1:46548 - "POST /chat HTTP/1.1" 200 OK
        "final_answer": "{'results': [{'text': \"West Virginia's 55 counties each carry distinct cultural identities. Southern coalfields (McDowell, Mingo, Logan) carry labor movement heritage. Fayette County holds the New River Gorge and a proud civic tradition centered in Mount Hope.\", 'category': 'regional_geography', 'section': ''}, {'text': 'rural_health Glenville Medical Care health_rural_facilities lat:38.942090 lon:-80.826084 West Virginia WV', 'category': 'general', 'section': ''}, {'text': 'rural_health Glenville Medical Care health_rural_facilities lat:38.942090 lon:-80.826084 West Virginia WV', 'category': 'general', 'section': ''}], 'count': 3}\nWhere are bridges in Wyoming County WV?",
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ 

