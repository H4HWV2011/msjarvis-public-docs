^C
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ # Check how many docs are in that collection
curl -s "http://127.0.0.1:8000/api/v2/tenants/default_tenant/databases/default_database/collections/e7e83578-973e-474e-a6d4-ea91d5d5289d" \
  | python3 -m json.tool

# Also check what main_brain sends to Chroma — find the query builder
grep -n "n_results\|query_embeddings\|chroma\|corpus" \
  ~/msjarvis-rebuild-working/msjarvis-rebuild/services/main_brain.py | head -20
Expecting value: line 1 column 1 (char 0)
526:    "chroma": "http://jarvis-chroma:8000",
564:    "chroma": "http://jarvis-chroma:8000/api/v2/heartbeat",
836:        CHROMA_BASE = "http://jarvis-chroma:8000"
838:        async with httpx.AsyncClient(timeout=10.0) as chroma_client:
840:            cols_resp = await chroma_client.get(f"{CHROMA_BASE}{CHROMA_V2}/collections")
848:                    embed_resp = await chroma_client.post(
861:                    mem_resp = await chroma_client.post(
864:                            'query_embeddings': [embedding],
865:                            'n_results': 5,
894:    # Decide if corpus is sufficient (we have verified local resources or RAG docs)
895:    corpus_sufficient = bool(local_resources_context or rag_context)
896:    logger.info(f"  📚 Corpus sufficiency: {corpus_sufficient}")
959:    # Only use agents_service when verified corpus is sparse
960:    if "agents_service" in available_services and not corpus_sufficient:
979:    # Only use web_research when verified corpus is sparse
980:    if "web_research" in available_services and not corpus_sufficient:
1519:async def unified_governance_query(q: str, n_results: int = 5):
1523:            params={"q": q, "n_results": n_results},
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ grep -n "local resources resolver\|local_resources\|connection attempts" \
  ~/msjarvis-rebuild-working/msjarvis-rebuild/services/main_brain.py | head -10
761:    local_resources_context = ""
790:                    local_resources_context = "\n".join(lr_snippets)
813:    if local_resources_context:
815:            f"VERIFIED LOCAL COMMUNITY RESOURCES (status: good, human-validated):\n{local_resources_context}"
895:    corpus_sufficient = bool(local_resources_context or rag_context)
1064:            if local_resources_context:
1065:                first_lines = local_resources_context.split("\n")[:5]
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ INFO:     (crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ # Add to your uvicorn startup or main_brain logging config:ng config:
# Filter out the /health GET 200 noise
grep -v '"GET /health HTTP' <(docker logs jarvis-main-brain --follow 2>&1)
INFO:     Started server process [10]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8050 (Press CTRL+C to quit)
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
INFO:     172.18.0.1:37514 - "GET / HTTP/1.1" 200 OK
INFO:     172.18.0.1:39212 - "GET / HTTP/1.1" 200 OK
INFO:     172.18.0.1:59658 - "GET / HTTP/1.1" 200 OK
INFO:     172.18.0.1:35884 - "GET / HTTP/1.1" 200 OK
INFO:     172.18.0.1:46478 - "GET / HTTP/1.1" 200 OK
INFO:     172.18.0.1:51366 - "GET / HTTP/1.1" 200 OK
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
INFO:httpx:HTTP Request: POST http://jarvis-judge-pipeline:7239/evaluate "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Judge Pipeline: Meta-judgment complete
INFO:main_brain:Phase 3.5: LM Synthesizer voice delivery... [+75.5s]
WARNING:main_brain:  ⚠️  LM Synthesizer error: 
INFO:main_brain:
Phase 4: Synthesizing ultimate response... [+90.6s]

WARNING:main_brain:  ⚠️  Consciousness Bridge error: 
INFO:main_brain:📝 Queued: What food resources are available in Fay...
INFO:     172.18.0.1:60326 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.1:40288 - "GET /judges/status HTTP/1.1" 404 Not Found
INFO:     172.18.0.1:40294 - "POST /chat HTTP/1.1" 422 Unprocessable Entity
INFO:     172.18.0.1:40930 - "GET / HTTP/1.1" 200 OK
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
WARNING:main_brain:  ⚠️  20-LLM Production: 
INFO:httpx:HTTP Request: POST http://jarvis-qualia-engine:8017/communicate "HTTP/1.1 200 OK"
INFO:main_brain:DEBUG qualia_engine appended to services_used
INFO:main_brain:  ✅ Qualia Engine: Phenomenal processing complete
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.0 200 OK"
INFO:main_brain:  ✅ WOAH Algorithms: Processing complete
INFO:httpx:HTTP Request: POST http://jarvis-i-containers:8015/process_full "HTTP/1.1 200 OK"
INFO:main_brain:DEBUG i_containers appended to services_used
INFO:main_brain:  ✅ I-Containers: Identity processing complete
INFO:main_brain:Phase 3: Calling judge_pipeline... [+58.5s]
INFO:httpx:HTTP Request: POST http://jarvis-judge-pipeline:7239/evaluate "HTTP/1.1 200 OK"
INFO:main_brain:  ✅ Judge Pipeline: Meta-judgment complete
INFO:main_brain:Phase 3.5: LM Synthesizer voice delivery... [+71.0s]
WARNING:main_brain:  ⚠️  LM Synthesizer error: 
INFO:main_brain:
Phase 4: Synthesizing ultimate response... [+86.0s]

WARNING:main_brain:  ⚠️  Consciousness Bridge error: 
INFO:main_brain:📝 Queued: What food pantries are available in Faye...
INFO:     172.18.0.1:42652 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.1:32956 - "GET / HTTP/1.1" 200 OK
INFO:     172.18.0.1:39488 - "GET / HTTP/1.1" 200 OK
INFO:     172.18.0.1:39886 - "GET / HTTP/1.1" 200 OK
INFO:     172.18.0.1:48064 - "GET / HTTP/1.1" 200 OK
INFO:     172.18.0.1:40060 - "GET / HTTP/1.1" 200 OK
INFO:     172.18.0.1:38962 - "GET / HTTP/1.1" 200 OK
INFO:     172.18.0.1:56228 - "GET / HTTP/1.1" 200 OK
INFO:     172.18.0.1:51658 - "GET / HTTP/1.1" 200 OK
INFO:     172.18.0.1:49406 - "GET / HTTP/1.1" 200 OK
INFO:     172.18.0.1:60220 - "GET / HTTP/1.1" 200 OK
INFO:     172.18.0.1:51220 - "GET / HTTP/1.1" 200 OK
INFO:     172.18.0.1:49584 - "GET / HTTP/1.1" 200 OK
INFO:     172.18.0.1:60776 - "GET / HTTP/1.1" 200 OK
INFO:     172.18.0.1:55990 - "GET / HTTP/1.1" 200 OK
INFO:     172.18.0.1:52338 - "GET / HTTP/1.1" 200 OK
INFO:     172.18.0.1:42386 - "GET / HTTP/1.1" 200 OK
INFO:     172.18.0.1:59760 - "GET / HTTP/1.1" 200 OK
INFO:     172.18.0.1:48044 - "GET / HTTP/1.1" 200 OK
INFO:     172.18.0.1:43124 - "GET / HTTP/1.1" 200 OK
INFO:     172.18.0.1:52828 - "GET / HTTP/1.1" 200 OK
INFO:     172.18.0.1:34606 - "GET / HTTP/1.1" 200 OK
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
