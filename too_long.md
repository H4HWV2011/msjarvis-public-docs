1763:[2025-11-11 10:39:58] [HEALTH] ✅ ChromaDB (port 8000): RESPONDING
81779:[2025-11-11 10:40:28] [HEALTH] ✅ ChromaDB (port 8000): RESPONDING
81795:[2025-11-11 10:40:28] [HEALTH] ✅ ChromaDB (port 8000): RESPONDING
81811:[2025-11-11 10:40:58] [HEALTH] ✅ ChromaDB (port 8000): RESPONDING
81827:[2025-11-11 10:40:58] [HEALTH] ✅ ChromaDB (port 8000): RESPONDING
81843:[2025-11-11 10:41:28] [HEALTH] ✅ ChromaDB (port 8000): RESPONDING
81859:[2025-11-11 10:41:28] [HEALTH] ✅ ChromaDB (port 8000): RESPONDING
81875:[2025-11-11 10:41:58] [HEALTH] ✅ ChromaDB (port 8000): RESPONDING
81891:[2025-11-11 10:41:58] [HEALTH] ✅ ChromaDB (port 8000): RESPONDING

./services/bridge_69dgm.py
67:@app.post("/consciousnesschat", response_model=ChatResponse)
68:async def consciousnesschat(req: ChatRequest):

./services/ingest_additional_kbs.py
24:            docs.append(text[:8000])

./services/main_brain_legacy_backup.py
268:    "chroma": "http://msjarvis-rebuild-chroma-1:8000",

./services/hilbert_spatial_chat.py
39:        chroma_port = int(os.getenv("CHROMA_PORT", "8000"))

./services/rag_server.py
121:        port = int(os.getenv("CHROMA_PORT", "8000"))

./services/export_attributes_to_gis.py
6:client = chromadb.HttpClient(host='localhost', port=8000)

./services/phase2_integration.py
70:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))

./services/hilbert/jarvis_hilbert_state.py
283:                port=int(_os.environ.get("CHROMA_PORT", 8000)),
338:            port=int(_os.environ.get("CHROMA_PORT", 8000)),

./services/port_9001_ARCHITECTURE_CORRECT.py
31:                f"http://127.0.0.1:9000/consciousness/chat?userid={userid}&message={message}",
44:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)), reload=False)

./services/main.py
263:    "chroma": "http://jarvis-chroma:8000",

./services/gis-rag/ingest_gis_tables.py
21:CHROMA_PORT = int(os.getenv("CHROMA_PORT", "8000"))

./services/master_chat_orchestrator_v9_dgm_complete.py
142:    behind port 8000, so no script is hard-coded here; it simply returns the live response.
162:    # the /chat.open endpoint on port 8000, which this orchestrator

./services/truth_filter_service.py
59:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))

./services/working_full_pipeline_WITH_SPATIAL_TEMPORAL.py
142:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))

./services/gis_rag_service.py
15:GIS_RAG_URL = os.getenv("GIS_RAG_CHROMA_URL", "http://jarvis-chroma:8000").rstrip("/")

./services/jarvis-gis-rag_gis_rag_service.py
16:GIS_RAG_URL = os.getenv("GIS_RAG_CHROMA_URL", "http://jarvis-chroma:8000").rstrip("/")

./services/gbim_chroma_fixed.py
9:    port = int(os.getenv("CHROMA_PORT", "8000"))

./services/consciousness_working.py
21:@app.post("/consciousness/chat")

./services/port_9000_69dgm_bridge.py.backup_20260307_070432
84:@app.post("/consciousnesschat", response_model=ConsciousChatResponse)

./services/background_curator.py
11:CHROMA_PORT = int(os.getenv("CHROMA_PORT", "8000"))

./services/route_declarations_raw.txt
418:consciousness_with_egeria_voice.py:31:@app.post("/consciousness/chat")
420:consciousness_working.py:21:@app.post("/consciousness/chat")
1010:ms_jarvis_command_orchestrator_FINAL.py:80:@app.post("/consciousness/chat")
1013:ms_jarvis_command_orchestrator.py:38:@app.post("/consciousness/chat")
1015:ms_jarvis_command_orchestrator_v5.0_preachy.py:80:@app.post("/consciousness/chat")
1018:ms_jarvis_command_orchestrator_v5_backup.py:48:@app.post("/consciousness/chat")
1065:ms_jarvis_conversational_gateway_4022.py:76:@app.post("/consciousness/chat")
1276:ms_jarvis_main_gateway_8000.py:31:@app.get("/health")
1277:ms_jarvis_main_gateway_8000.py:65:@app.post("/chat")
1278:ms_jarvis_main_gateway_8000.py:85:@app.post("/qualia_check")
1279:ms_jarvis_main_gateway_8000.py:105:@app.get("/")
1619:ms_jarvis_unified_gateway_v4.3.20251124.py:268:@app.post("/consciousness/chat", tags=["Consciousness"])
1645:ms_jarvis_unified_gateway_v4.3.backup.py:228:@app.post("/consciousness/chat", tags=["Consciousness"])
1667:ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:241:@app.post("/consciousness/chat", tags=["Consciousness"])
1726:ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP.py:268:@app.post("/consciousness/chat", tags=["Consciousness"])
1752:ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER.py:229:@app.post("/consciousness/chat", tags=["Consciousness"])
1778:ms_jarvis_unified_gateway_v4.3.pre_manifest.backup.py:230:@app.post("/consciousness/chat", tags=["Consciousness"])
2143:port_9000_chat_wrapper_69dgm.py:34:@app.post("/consciousness/chat")

./services/ports_diff_msjarvis.txt
817:+8000

./services/constitutional_api.PROD_BACKUP.py
38:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8000)))

./services/port_9001_ui_WORKING.py
131:                f"http://127.0.0.1:9000/consciousness/chat?userid={userid}&message={message}",

./services/unifiedconsciousnessgatewayPRODUCTION.py
13:            port=int(os.getenv("SERVICE_PORT", 8000)),

./services/fix_port_8051_handler.py
18:            'http://127.0.0.1:9000/consciousness/chat?userid=web&message="""

./services/port_9001_proxy_simple.py
19:    description="Routes all requests to port 9000 consciousness/chat",
33:            f"http://127.0.0.1:9000/consciousness/chat?userid={userid}&message={message}",

./services/chroma_python_test.py
7:    chroma_port = int(os.getenv("CHROMA_PORT", "8000"))

./services/PORTS_REGISTRY_RAW.txt
9:/home/ms-jarvis/msjarvis-rebuild/services/agents_main.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
17:/home/ms-jarvis/msjarvis-rebuild/services/ai_server_20llm_PRODUCTION.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
22:/home/ms-jarvis/msjarvis-rebuild/services/ai_server_22llm_SEQUENTIAL_OPTIMIZED_ORDER.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
53:/home/ms-jarvis/msjarvis-rebuild/services/constitutional_api.PROD_BACKUP.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
78:/home/ms-jarvis/msjarvis-rebuild/services/dynamic_port_service_enhanced.py:    def __init__(self, redis_host='localhost', redis_port=int(os.getenv("SERVICE_PORT", 8000))):
94:/home/ms-jarvis/msjarvis-rebuild/services/egeria_web_ui.py:    app.run(host='0.0.0.0', port=int(os.getenv("SERVICE_PORT", 8000)), debug=False)
100:/home/ms-jarvis/msjarvis-rebuild/services/export_attributes_to_gis.py:client = chromadb.HttpClient(host='localhost', port=8000)
132:/home/ms-jarvis/msjarvis-rebuild/services/interaction_logger.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
302:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_api_docs.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)), log_level="info")
303:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_attribute_table_service.py:        client = chromadb.HttpClient(host="localhost", port=int(os.getenv("CHROMA_PORT", 8000)))
305:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_authentic_multi_llm.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)), reload=False)
310:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_autonomous_learner_WITH_FIFTH_DGM.py:            self.chroma_client = chromadb.HttpClient(host="localhost", port=int(os.getenv("SERVICE_PORT", 8000)))
311:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_autonomous_learner_WITH_FIFTH_DGM.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
349:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_darwin_godel_machine.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
353:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_email_monitor.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
357:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_facebook_autonomous_social.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
366:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_facebook_poster_FIXED.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
373:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_fact_filter.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
381:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_fractal_consciousness_FIXED.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
389:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_geo_ueid_integration.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
424:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.proxy_still_broken.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)), log_level="info")
465:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_ueid_system.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
473:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.py:    uvicorn.run(app, host='0.0.0.0', port=int(os.getenv("SERVICE_PORT", 8000)), reload=False)
476:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_CLEAN.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
480:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)), log_level="info")
483:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_PROD.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
486:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_venv_scheduler_FIXED.py:        self.redis_client = redis.Redis(host='localhost', port=int(os.getenv("SERVICE_PORT", 8000)), decode_responses=True)
488:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_venv_scheduler_SIMPLE.py:        self.redis_client = redis.Redis(host='localhost', port=int(os.getenv("SERVICE_PORT", 8000)), decode_responses=True)
522:/home/ms-jarvis/msjarvis-rebuild/services/phase2_integration.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
538:/home/ms-jarvis/msjarvis-rebuild/services/port_9000_chat_wrapper_69dgm.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)), reload=False)
539:/home/ms-jarvis/msjarvis-rebuild/services/port_9001_ARCHITECTURE_CORRECT.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)), reload=False)
544:/home/ms-jarvis/msjarvis-rebuild/services/port_9001_ui_FIXED.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)), reload=False)
587:/home/ms-jarvis/msjarvis-rebuild/services/run_gateway_with_guards.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
598:/home/ms-jarvis/msjarvis-rebuild/services/stage2_biometric_backup.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
599:/home/ms-jarvis/msjarvis-rebuild/services/stage2_biometric.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
609:/home/ms-jarvis/msjarvis-rebuild/services/truth_filter_service.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
611:/home/ms-jarvis/msjarvis-rebuild/services/unifiedconsciousnessgatewayPRODUCTION.py:            chroma_client = chromadb.HttpClient(host='localhost', port=int(os.getenv("SERVICE_PORT", 8000)), settings=Settings(allow_reset=False))
627:/home/ms-jarvis/msjarvis-rebuild/services/woah_qualia_bridge.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
630:/home/ms-jarvis/msjarvis-rebuild/services/working_full_pipeline_WITH_SPATIAL_TEMPORAL.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
631:/home/ms-jarvis/msjarvis-rebuild/services/wvu_ldap_auth.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)), log_level="info")

./services/PORT_AUDIT_RAW.txt
10:/home/ms-jarvis/msjarvis-rebuild/services/agents_main.py:11:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
18:/home/ms-jarvis/msjarvis-rebuild/services/ai_server_20llm_PRODUCTION.py:126:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
23:/home/ms-jarvis/msjarvis-rebuild/services/ai_server_22llm_SEQUENTIAL_OPTIMIZED_ORDER.py:136:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
56:/home/ms-jarvis/msjarvis-rebuild/services/constitutional_api.PROD_BACKUP.py:38:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
87:/home/ms-jarvis/msjarvis-rebuild/services/dynamic_port_service_enhanced.py:26:    def __init__(self, redis_host='localhost', redis_port=int(os.getenv("SERVICE_PORT", 8000))):
108:/home/ms-jarvis/msjarvis-rebuild/services/egeria_web_ui.py:427:    app.run(host='0.0.0.0', port=int(os.getenv("SERVICE_PORT", 8000)), debug=False)
114:/home/ms-jarvis/msjarvis-rebuild/services/export_attributes_to_gis.py:6:client = chromadb.HttpClient(host='localhost', port=8000)
146:/home/ms-jarvis/msjarvis-rebuild/services/interaction_logger.py:121:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
600:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_api_docs.py:269:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)), log_level="info")
601:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_attribute_table_service.py:34:        client = chromadb.HttpClient(host="localhost", port=int(os.getenv("CHROMA_PORT", 8000)))
603:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_authentic_multi_llm.py:178:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)), reload=False)
608:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_autonomous_learner_WITH_FIFTH_DGM.py:60:            self.chroma_client = chromadb.HttpClient(host="localhost", port=int(os.getenv("SERVICE_PORT", 8000)))
609:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_autonomous_learner_WITH_FIFTH_DGM.py:270:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
653:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_darwin_godel_machine.py:283:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
657:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_email_monitor.py:89:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
661:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_facebook_autonomous_social.py:451:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
670:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_facebook_poster_FIXED.py:87:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
677:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_fact_filter.py:126:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
688:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_fractal_consciousness_FIXED.py:64:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
696:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_geo_ueid_integration.py:220:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
732:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.proxy_still_broken.py:178:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)), log_level="info")
774:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_ueid_system.py:385:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
782:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.py:142:    uvicorn.run(app, host='0.0.0.0', port=int(os.getenv("SERVICE_PORT", 8000)), reload=False)
785:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_CLEAN.py:142:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
789:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:482:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)), log_level="info")
792:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_PROD.py:221:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
795:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_venv_scheduler_FIXED.py:25:        self.redis_client = redis.Redis(host='localhost', port=int(os.getenv("SERVICE_PORT", 8000)), decode_responses=True)
797:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_venv_scheduler_SIMPLE.py:23:        self.redis_client = redis.Redis(host='localhost', port=int(os.getenv("SERVICE_PORT", 8000)), decode_responses=True)
838:/home/ms-jarvis/msjarvis-rebuild/services/phase2_integration.py:70:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
856:/home/ms-jarvis/msjarvis-rebuild/services/port_9000_chat_wrapper_69dgm.py:90:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)), reload=False)
857:/home/ms-jarvis/msjarvis-rebuild/services/port_9001_ARCHITECTURE_CORRECT.py:44:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)), reload=False)
862:/home/ms-jarvis/msjarvis-rebuild/services/port_9001_ui_FIXED.py:151:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)), reload=False)
908:/home/ms-jarvis/msjarvis-rebuild/services/run_gateway_with_guards.py:20:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
922:/home/ms-jarvis/msjarvis-rebuild/services/stage2_biometric_backup.py:154:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
923:/home/ms-jarvis/msjarvis-rebuild/services/stage2_biometric.py:221:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
934:/home/ms-jarvis/msjarvis-rebuild/services/truth_filter_service.py:59:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
937:/home/ms-jarvis/msjarvis-rebuild/services/unifiedconsciousnessgatewayPRODUCTION.py:10:            chroma_client = chromadb.HttpClient(host='localhost', port=int(os.getenv("SERVICE_PORT", 8000)), settings=Settings(allow_reset=False))
954:/home/ms-jarvis/msjarvis-rebuild/services/woah_qualia_bridge.py:32:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
957:/home/ms-jarvis/msjarvis-rebuild/services/working_full_pipeline_WITH_SPATIAL_TEMPORAL.py:142:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
958:/home/ms-jarvis/msjarvis-rebuild/services/wvu_ldap_auth.py:65:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)), log_level="info")

./services/port_9001_FINAL_WORKING.py
185:            r = await client.post(f"http://127.0.0.1:9000/consciousness/chat?userid=user&message={message}", timeout=10.0)

./services/ai_server_22llm_SEQUENTIAL_OPTIMIZED_ORDER.py
139:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8000)))

./services/chat_endpoint_universal.py
43:            f"http://127.0.0.1:9000/consciousness/chat?userid={userid}&message={message}",

./services/RESTORATION_CERTIFICATE.txt
30:✅ Brain Orchestrator (Port 8000)

./services/stage2_biometric_backup.py
154:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))

./services/port_9000_69dgm_bridge.py.backup_20260307_072514
84:@app.post("/consciousnesschat", response_model=ConsciousChatResponse)

./services/msjarvis_ports_runtime.txt
13:tcp   LISTEN 0      4096                             0.0.0.0:8000       0.0.0.0:*    users:(("docker-proxy",pid=6445,fd=7))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
34:tcp   LISTEN 0      4096                                [::]:8000          [::]:*    users:(("docker-proxy",pid=6452,fd=7))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

./services/main_brain.py
327:        "port900069dgmbridge": "consciousnesschat",
1417:            "http://127.0.0.1:9000/consciousness/chat",
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ curl -s http://127.0.0.1:8000/openapi.json | jq -r '.paths | keys[]'
/health
/log-interaction
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ cd /mnt/spiritual_drive/msjarvis-rebuild

echo '=== PROBE COMMON ENDPOINTS ON 8000 (AGAIN) ==='
for path in / /docs /openapi.json /health /consciousnesschat /consciousness/chat /chat /process ; do
  code=$(curl -s -o /tmp/resp.$$ -w '%{http_code}' "http://127.0.0.1:8000$path")
  echo "$code  $path"
  if [ "$code" != "404" ]; then
    head -c 400 /tmp/resp.$$ ; echo
    echo '---'
  fi
done
rm -f /tmp/resp.$$
=== PROBE COMMON ENDPOINTS ON 8000 (AGAIN) ===
404  /
200  /docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link rel="shortcut icon" href="https://fastapi.tiangolo.com/img/favicon.png">
    <title>Ms. Jarvis Interaction Logger - Swagger UI</title>
    </head>
    <body>
 
---
200  /openapi.json
{"openapi":"3.1.0","info":{"title":"Ms. Jarvis Interaction Logger","version":"1.0"},"paths":{"/log-interaction":{"post":{"summary":"Log Interaction","description":"Log interaction to MySQL with geolocation fallback to Mount Hope","operationId":"log_interaction_log_interaction_post","requestBody":{"content":{"application/json":{"schema":{"$ref":"#/components/schemas/InteractionLog"}}},"required":tr
---
200  /health
{"status":"healthy","service":"interaction_logger","port":8005,"default_location":"Mount Hope, WV","coordinates":{"lat":37.9735,"lon":-81.166,"city":"Mount Hope","state":"WV","zip":"25880"}}
---
404  /consciousnesschat
404  /consciousness/chat
404  /chat
404  /process
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ cd /mnt/spiritual_drive/msjarvis-rebuild

echo '=== SEARCH FOR RAG BRIDGE URLS ==='
rg -n 'RAG' services . --glob '!**/.git/**' || true
rg -n 'consciousnesschat|consciousness/chat' services . --glob '!**/.git/**' || true
rg -n 'interaction_logger' services . --glob '!**/.git/**' || true

echo '=== LOOK FOR OTHER CONSCIOUSNESS ENDPOINTS ==='
rg -n '"/consciousness' services . --glob '!**/.git/**' || true
rg -n 'consciousness_chat' services . --glob '!**/.git/**' || true
rg -n 'RAG bridge' services . --glob '!**/.git/**' || true

echo '=== LIST ENABLED MSJARVIS SERVICES ==='
systemctl list-units 'msjarvis-*' --no-pager
=== SEARCH FOR RAG BRIDGE URLS ===
services/quick_optimizations.py
23:        "http://localhost:${RAG_SERVER_PORT}/health",

services/working_full_pipeline.py
26:    # 1. RAG

services/enhance_rag_knowledge.py
6:"""Enhance RAG server with all MountainShares documentation"""
13:print("🧠 Enhancing RAG server with MountainShares knowledge...")
15:# Connect to RAG server's ChromaDB
77:print(f"   🔍 RAG server knowledge base expanded!")

services/rag_query_router.py
47:app = FastAPI(title="RAG Query Router", version="1.0.0")
52:# Base URLs for domain RAG services inside the mesh
53:RAG_SERVICE_URLS: Dict[str, str] = {
75:    # Optional filters to pass down to domain RAG services (they decide how to use them)
77:    # If true, router will call the selected RAG service and include its answer
95:    Registers this RAG query router into the Ms. Jarvis mesh registry in Redis.
103:        "description": "Routes queries to appropriate RAG domains/services.",
153:    Heuristic router for RAG domains.
301:# Downstream RAG service dispatch
305:    Calls the selected RAG domain service and returns its JSON response.
308:    base_url = RAG_SERVICE_URLS.get(service_name)
310:        raise HTTPException(status_code=500, detail=f"Unknown RAG service '{service_name}'")
335:            detail=f"Error calling downstream RAG service '{service_name}' at '{path}': {str(e)}",

services/FULL_DEPLOYMENT_MANIFEST.txt
7:- Port 8003: RAG Server (ChromaDB) ✅

services/port_9000_69dgm_bridge.py
3:Bridge: Port 9000 Chat → 69-DGM Orchestrator + RAG Bridge
5:then, if approved, calls the 69-DGM RAG bridge for an answer.
25:# Downstream 69-DGM RAG bridge (bridge_69dgm.py)
70:        "then calls the 69-DGM RAG bridge for an answer"
138:# Call the 69-DGM RAG bridge (bridge_69dgm.py) after approval
142:    Call the 69-DGM RAG bridge (bridge_69dgm.py) to get an answer.
147:        f"🔗 Calling 69-DGM RAG bridge at {BRIDGE_69DGM_URL} for user={userid}"
157:            logger.info("✅ 69-DGM RAG bridge responded successfully")
161:                f"❌ 69-DGM RAG bridge error: HTTP {resp.status_code} "
166:        logger.error(f"Error calling 69-DGM RAG bridge: {e}")
171:# High-level chat handler: orchestrator + RAG + connector metadata
178:    2) If approved, calls the 69-DGM RAG bridge for an answer.
179:    3) If RAG fails, falls back to the previous static approval response.
211:        # Not approved; return verdict and do NOT call RAG
223:    # Approved by 69 validators → proceed to RAG bridge
224:    logger.info("✅ Message approved by 69 validators - proceeding to RAG bridge")
236:            # If RAG returns empty, fall back to approval text
253:    # RAG bridge failed; fall back to the original static approval response
255:        "⚠️ 69-DGM RAG bridge failed or returned no response; "
279:    then, if approved, through the 69-DGM RAG bridge.

services/main_with_rag.py
6:"""Enhanced main.py with RAG-first workflow"""
14:# Override ultimate_chat to use RAG-first
21:    # STEP 1: Check RAG first
25:            "response": f"**From Knowledge Cache:**\n{rag_result}\n\n*Retrieved from RAG in <1s*",
36:    # STEP 3: Store result in RAG for future
50:print("✅ RAG-First workflow enabled")

services/nbb_darwin_godel_machines.py.backup_1772889398
50:    dgm_agent: str = "DGM_RAG_TUNER"

services/add_fifth_dgm_to_chat.py
92:        print("  4. Automatically stores in subconscious (RAG)")

services/implement_safe_optimizations.py
102:        ("http://localhost:4011/health", "Multi-RAG DGM"),
103:        ("http://localhost:${RAG_SERVER_PORT}/health", "RAG Server"),
145:RAG_SEARCH_TIMEOUT = 8.0  # RAG search operations
379:        "http://localhost:${RAG_SERVER_PORT}",

services/nbb_darwin_godel_machines.py.pre_dynamic
50:    dgm_agent: str = "DGM_RAG_TUNER"

services/system_dashboard.py
32:    "RAG Server": "http://localhost:${RAG_SERVER_PORT}",

services/process_statewide_gis_bulk.py
87:                'COVERAGE': 'Statewide WV',

services/swagger_gateway_FIXED.py
21:    services = {"brain": get_service_url("ai_alt"), "rag": "http://localhost:${RAG_SERVER_PORT}"}

services/master_chat_orchestrator_v5_consciousness.py
15:- RAG → Consciousness → Multi-Model Consensus → Response
52:    "rag_server": "http://localhost:${RAG_SERVER_PORT}",
132:    3. RAG knowledge retrieval
191:    # LAYER 3: RAG Knowledge Retrieval 
192:    logger.info("📚 Layer 3: RAG knowledge retrieval...")
207:                    logger.info(f"   ✅ RAG context: {len(rag_context)} chars")
209:        logger.warning(f"   ⚠️  RAG retrieval failed: {e}")

services/dgm_supervisor_woah_fixed.py
220:    """Sync conversational memory to RAG"""
227:    # Find RAG services
238:    # Simple memory sync to RAG
241:            # Test RAG connection

services/ai_server_19llm_CONSCIOUS.backup_20251013_082519.py
292:            mem = requests.post("http://localhost:${RAG_SERVER_PORT}/search", json={
415:            requests.post("http://localhost:${RAG_SERVER_PORT}/store", json={

services/domain_service_router.py
35:            "rag.mountainshares.us": {"port": 4016, "name": "GPU RAG System"},

services/nbb_darwin_godel_machines.py.pre_debug
50:    dgm_agent: str = "DGM_RAG_TUNER"

services/add_fast_layer.py
22:            mem = requests.post("http://localhost:${RAG_SERVER_PORT}/search", json={"query": request.message, "user_id": request.user_id, "limit": 3}, timeout=2)

services/aaacpe_scraper_service.py
3:AaaCPE Web Scraper - Feeds Current Appalachian Content into RAG

services/add_conversation_context.py
20:                f"{RAG_URL}/conversations/{user_id}",

services/msjarvisunifiedgateway.py
163:    # GeoBIM / RAG Service (port 8051)

services/smart_auto_store.py
8:Checks RAG before storing to avoid duplicates
14:    """Store in RAG only if not duplicate"""

services/main_brain_psychology_patch.py
37:    # Adjust the path if your FastAPI/RAG server uses a different route

services/ai_server.py
74:            logger.info("✅ ChromaDB connected - RAG memory active")

services/dir_endpoints.txt
327:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP.py:405:@app.get("/rag/supervisor", tags=["RAG-Supervisor"])
537:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.backup_1762220815.py:139:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
551:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.backup_1762220815.py:207:@app.get("/rag-knowledge-stats", tags=["Whitebox"], summary="RAG & Knowledge Base Statistics")
714:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.py:102:@app.post("/rag-query", tags=["RAG"])
715:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.py:110:@app.get("/rag-status", tags=["RAG"])
758:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER.py:350:@app.get("/rag/supervisor", tags=["RAG-Supervisor"])
811:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:149:@app.post("/rag-query", tags=["RAG"])
812:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:158:@app.get("/rag-status", tags=["RAG"])
871:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.pre_manifest.backup.py:351:@app.get("/rag/supervisor", tags=["RAG-Supervisor"])
920:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:366:@app.get("/rag/supervisor", tags=["RAG-Supervisor"])
1099:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_BACKUP.py:139:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
1113:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_BACKUP.py:207:@app.get("/rag-knowledge-stats", tags=["transparency_mode"], summary="RAG & Knowledge Base Statistics")
1177:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.py.30endpoints_backup.py:149:@app.post("/rag-query", tags=["RAG"])
1178:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.py.30endpoints_backup.py:158:@app.get("/rag-status", tags=["RAG"])
1339:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FIXED.py:189:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
1353:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FIXED.py:257:@app.get("/rag-knowledge-stats", tags=["transparency_mode"], summary="RAG & Knowledge Base Statistics")
1465:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.backup.py:349:@app.get("/rag/supervisor", tags=["RAG-Supervisor"])
1603:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.backup_error.py:139:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
1617:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.backup_error.py:207:@app.get("/rag-knowledge-stats", tags=["Whitebox"], summary="RAG & Knowledge Base Statistics")
1654:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FINAL.py:139:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
1668:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FINAL.py:207:@app.get("/rag-knowledge-stats", tags=["transparency_mode"], summary="RAG & Knowledge Base Statistics")
1787:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:139:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
1801:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:207:@app.get("/rag-knowledge-stats", tags=["transparency_mode"], summary="RAG & Knowledge Base Statistics")

services/ai_server_20llm_PRODUCTION.py.backup_bakllava_removal
57:        f"{len(rag_hits)} msjarvisgis RAG hits."
63:          "the WV local_resources_index database, and the msjarvisgis RAG layer.\n"
67:        + "RAG hits: " + str(rag_hits) + "\n"

services/dgm_supervisor_woah.psychology_patched.py
287:    """Sync all conversational memory to RAG systems"""
292:    logger.info("🧠 Synchronizing conversational memory to RAG...")
294:    # Find all RAG services
299:        # Default to main RAG
319:                # Process memory data for RAG ingestion
322:                # Send to RAG services
342:    """Process memory data into RAG-compatible documents"""
385:    """Sync memory documents to a RAG service"""

services/add_conversation_endpoint.py
6:"""Add conversation storage to existing RAG server"""
18:# === CONVERSATION STORAGE ===
94:# Restart RAG server
98:    print("🔄 Restarting RAG server...")
101:    print("✅ RAG server restarted")

services/dgm_orchestrator.py
30:    _have = {col[1] for col in conn.execute("PRAGMA table_info(central_i_container)").fetchall()}

services/chromadb_rag_helper.py
8:    """Query ChromaDB RAG for consciousness context"""
22:            logger.info(f"📚 RAG retrieved {len(results)} context chunks")

services/web_page_ingest.py
17:RAG_STORE_URL = os.getenv("RAG_STORE_URL", "http://127.0.0.1:8003/store")
34:    Fetch a web page, extract readable text, and store it into RAG.
81:    # 3) Store into RAG using the existing background_rag_store schema
101:            store_resp = await client.post(RAG_STORE_URL, json=payload)
103:        logger.error(f"Error calling RAG store: {repr(e)}")
106:            detail=f"Error storing to RAG: {repr(e)}",
110:        f"RAG store status={store_resp.status_code}, "
117:            detail=f"RAG store failed: {store_resp.text}",

services/conversation_memory_endpoints.py
8:Add these to your RAG server or run as separate microservice
21:# Connect to same ChromaDB as RAG

services/fix_storage.py
11:    """Store conversation in RAG with correct schema"""
15:                f"{RAG_URL}/store_conversation",
33:    """Store conversation in RAG with correct schema"""
37:                f"{RAG_URL}/store_conversation",

services/enhance_rag_first.py
6:"""Enhance main.py to check RAG first, then web search, then store"""
11:# Add RAG-first logic before web search
13:        # === RAG-FIRST STRATEGY ===
14:        # 1. Check RAG for existing knowledge
24:                        # Found good match in RAG - use it!
25:                        logger.info(f"✅ RAG hit! Score: {rag_data['results'][0]['score']:.2f}")
28:            logger.debug(f"RAG check: {e}")
29:        # === END RAG-FIRST ===
42:    print("✅ Added RAG-first checking to main.py")

services/patch_mother_persona.py
6:"""Add RAG retrieval to apply_mother_persona"""
12:# Find the apply_mother_persona function and inject RAG
24:    # Inject RAG retrieval right after the try: block starts
26:        # Insert RAG retrieval before emotion_context
28:        rag_code = f'''{indent}# Retrieve authentic Appalachian phrases from RAG
33:{indent}    logging.warning(f"RAG retrieval failed: {{e}}")
39:        # Add RAG code then re-add emotion_context
44:    # Now find the mother_prompt and inject RAG phrases
50:                # Inject RAG phrases before this line
62:print("✅ RAG retrieval injected into apply_mother_persona!")

services/rag_command_module.py
1:"""RAG Command Module - Query knowledge base"""

services/rag_general.py
36:app = FastAPI(title="RAG General Service", version="1.0.0")
54:        "description": "General-purpose RAG domain for non-temporal, non-geospatial queries.",
103:    Placeholder general RAG implementation.
111:        "answer_stub": "General RAG answer (stub).",

services/DEPLOYMENT_ORDER.txt
4:✅ Port 8003: RAG Server

services/METHOD_AUDIT_RAW.txt
486:/home/ms-jarvis/msjarvis-rebuild/services/gpu_accelerated_rag_fixed.py:47:class GPUAcceleratedRAGFixed:
490:/home/ms-jarvis/msjarvis-rebuild/services/gpu_accelerated_rag.py:41:class GPUAcceleratedRAG:
1409:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py:88:class RAGHelper:
2543:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_rag_bridge.py:40:class RAGQuery(BaseModel):
2544:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_rag_bridge.py:45:class UnifiedRAG:
2547:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_rag_bridge.py:211:async def query_rag(query_req: RAGQuery):
3068:/home/ms-jarvis/msjarvis-rebuild/services/rag_server.psychology_patched.py:72:class RAGServer:
3080:/home/ms-jarvis/msjarvis-rebuild/services/rag_server.py:72:class RAGServer:
3091:/home/ms-jarvis/msjarvis-rebuild/services/rag_workflow.py:16:class RAGWorkflow:

services/jarvis-spiritual-rag_spiritual_rag_domain.py
3:SPIRITUAL RAG DOMAIN SERVICE
4:Specialized RAG for spiritual, biblical, and theological content
19:    title="Spiritual RAG Domain",
53:        "service": "Spiritual RAG Domain - FOUNDATIONAL LAYER",
116:    """Add document to spiritual RAG"""
131:    logger.info(f"✝️ Spiritual RAG Domain (FOUNDATIONAL LAYER) starting on port {port}")

services/egeria_web_ui_dynamic.py
128:                    const info = `Mode: ${data.mode || 'fast'} | Time: ${data.time?.toFixed(2) || '?'}s | RAG: ${data.context_used ? 'Yes' : 'No'}`;

services/manual_storage_patch.py
27:        indent + '# Schedule background RAG storage\n',

services/master_chat_orchestrator_dynamic.py
42:    description="Dynamic port RAG-enhanced orchestration"
136:    # STEP 1: Get RAG context with service discovery
137:    logger.info("📚 Discovering RAG service...")
142:        logger.info(f"   Found RAG at {rag_url}")
158:        logger.warning(f"   ⚠️  RAG failed: {e}")

services/rag_5100_ensemble.py
8:app = FastAPI(title="RAG Consensus Ensemble", version="2.0")

services/mesh_coordinator_interface.py
163:    VALUES ('Facebook_API', 'Mesh_Internal', 'Through_Coordinator', 1, 'RAG→WOAH→DGM→Consciousness→Output')
170:    VALUES ('WebUI', 'Mesh_Internal', 'Through_Coordinator', 2, 'RAG→WOAH→DGM→Consciousness→Output')
244:    print("    GISGEODB↔ChromaDB↔RAG↔WOAH↔DGM")
254:    print("  4. Mesh processes (GISGEODB→RAG→Consciousness)")

services/gpu_accelerated_rag.py
7:GPU-ACCELERATED RAG SYSTEM
8:High-performance RAG using RTX 4070 GPU for embeddings and search
36:    title="GPU-Accelerated RAG System",
41:class GPUAcceleratedRAG:
49:        logger.info(f"🎮 Initializing GPU-Accelerated RAG on {self.device}")
190:# Global GPU-accelerated RAG instance
191:gpu_rag = GPUAcceleratedRAG()
197:        "service": "GPU-Accelerated RAG System",
245:    logger.info(f"🚀 GPU-Accelerated RAG starting on port {port_service.port}")

services/rag_simple.py
7:app = FastAPI(title="RAG Consensus Server", version="1.0")

services/msjarvisunifiedswaggergatewayFIXED.py
57:RAG_URL = "http://jarvis-direct-rag:8199"                  # /direct_rag
166:    # Build retrieval context for RAG from Hilbert + Chroma
196:    # RAG via /direct_rag
204:                "user_profile": user_profile,  # identity context for RAG
207:        rr = requests.post(f"{RAG_URL}/direct_rag", json=rag_req, timeout=300)
211:            print("✅ RAG /direct_rag: OK", file=sys.stderr)
213:            rag_response = f"RAG error: {rr.status_code} {rr.text}"
215:        rag_response = f"RAG error: {e}"
216:        print(f"❌ RAG: {e}", file=sys.stderr)
238:        # 22-LLM itself already has RAG + multi-agent logic; this gateway focuses on routing.

services/rag_server_main.py
2:Ms. Jarvis RAG Server - Unified Knowledge Retrieval
3:Port: 8003 (RAG Service)
30:    title="Ms. Jarvis RAG Server",
32:    description="Unified RAG service returning rich results_by_source for Ms. Jarvis ULTIMATE",
197:    logger.info(f"🔍 RAG /search query='{query[:80]}' top_k={request.top_k}")
200:    logger.debug(f"RAG where-clause: {where}")
217:            logger.warning(f"RAG query error for collection {collection_name}: {e}")
262:    logger.info(f"✅ RAG /search completed query='{query[:60]}' count={total_count}")
590:        "service": "Ms. Jarvis RAG Server",
592:        "description": "Unified RAG server for Ms. Jarvis ULTIMATE, exposing /search and /store",
606:    logger.info("🚀 Starting Ms. Jarvis RAG Server on port 8003")

services/geobim_health_shim_8051.py
4:app = FastAPI(title="GeoBIM / RAG Health Shim")

services/fix_multi_rag_chromadb.py
7:Fix Multi-RAG to use correct ChromaDB path
32:print("Restarting Multi-RAG service...")
41:print("✅ Multi-RAG restarted")

services/msjarvis_benefit_rag.py
4:class MsJarvisBenefitRAG:
165:    print("Initializing MsJarvisBenefitRAG")
168:    rag = MsJarvisBenefitRAG()

services/comprehensive_storage_fix.py
16:    storage_code = f'''{indent}# Store in RAG (background)
30:    lambda m: f'''{m.group(1)}# Store email action in RAG
33:{m.group(1)}    logger.info(f"📝 Email queued for RAG")
43:    lambda m: f'''{m.group(1)}# Store website deployment in RAG
46:{m.group(1)}    logger.info(f"📝 Website queued for RAG")
69:            new_lines.append(spaces + '# Background RAG storage')

services/msjarvisragserver_wvpatch.py
7:app = FastAPI(title="Ms. Jarvis RAG Server (WV)", version="1.0.0")
17:WV_RAG_PROFILES = {
36:    collections = WV_RAG_PROFILES.get(profile)
38:        raise HTTPException(status_code=400, detail=f"Unknown RAG profile {profile}")

services/dgm_rag_integration.py
3:69-DGM RAG Integration Layer
18:class DGMRAGIntegration:
31:        print(f"DGM RAG Integration initialized with Chroma at: {self.chroma_base}")
333:def get_dgm_rag_integration() -> DGMRAGIntegration:
334:    """Get or create singleton DGM RAG integration instance."""
337:        _dgm_rag = DGMRAGIntegration()

services/load_spiritual_library.py
6:"""Load comprehensive spiritual library into Ms. Jarvis RAG"""
13:print("📖 Loading spiritual library into RAG...")

services/route_declarations_clean.txt
1202:get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB")
1216:get("/rag-knowledge-stats", tags=["Whitebox"], summary="RAG & Knowledge Base Statistics"
1243:get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB")
1257:get("/rag-knowledge-stats", tags=["Whitebox"], summary="RAG & Knowledge Base Statistics"
1399:get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB")
1413:get("/rag-knowledge-stats", tags=["transparency_mode"], summary="RAG & Knowledge Base Statistics"
1442:get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB")
1456:get("/rag-knowledge-stats", tags=["transparency_mode"], summary="RAG & Knowledge Base Statistics"
1483:get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB")
1497:get("/rag-knowledge-stats", tags=["transparency_mode"], summary="RAG & Knowledge Base Statistics"
1521:get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB")
1535:get("/rag-knowledge-stats", tags=["transparency_mode"], summary="RAG & Knowledge Base Statistics"

services/aaacpe_scraper/aaacpe_scraper_service.py
3:AaaCPE Web Scraper - Feeds Current Appalachian Content into RAG

services/comprehensive_gisgeodb_audit.py
219:        logger.info("5️⃣  STORAGE DISTRIBUTION (185GB across datasets)")
249:        with open('data/STORAGE_DISTRIBUTION.csv', 'w', newline='') as f:
254:        logger.info(f"✅ Created STORAGE_DISTRIBUTION.csv")

services/auto_rag_builder.py
6:"""Auto-build RAG every 5 minutes with compression"""
16:            logger.info(f"🔄 Building RAG...")
35:                logger.info(f"✅ RAG: {len(state)}→{len(compressed)} bytes ({ratio:.1%})")

services/multi_rag_dgm_system.py
3:MULTI-RAG DGM SYSTEM
4:Multiple RAG systems with Darwin-Gödel Machine integration
5:Specialized RAG instances for different knowledge domains
32:    title="Multi-RAG DGM System",
34:    description="Multiple specialized RAG systems with DGM integration",
44:# Specialized RAG configurations
45:RAG_DOMAINS: Dict[str, Dict[str, Any]] = {
87:        "service": "Multi-RAG DGM System",
92:        "rag_domains": len(RAG_DOMAINS),
101:    for domain, config in RAG_DOMAINS.items():
125:    """Route query to appropriate RAG domain(s) using DGM logic"""
137:        if domain in RAG_DOMAINS:
138:            config = RAG_DOMAINS[domain]
169:    if domain_hint and domain_hint in RAG_DOMAINS:
173:    for domain, config in RAG_DOMAINS.items():
217:            weight = RAG_DOMAINS[domain]["priority"]
266:    """Sync all conversational memories to appropriate RAG domains"""
267:    logger.info("🧠 Syncing all memories to Multi-RAG system...")
290:                if target_domain in RAG_DOMAINS:
291:                    port = RAG_DOMAINS[target_domain]["port"]
308:    """Process memory data for specific domain RAG"""
329:    """Sync documents to domain-specific RAG"""
355:    logger.info(f"🔀 Multi-RAG DGM System starting on port {port}")

services/add_conversation_storage.py
6:"""Add conversation storage endpoint to RAG server"""
8:# Read current RAG server
98:print("✅ Added conversation storage endpoints to RAG server")

services/create_consciousness_data_integration.py
32:  • RAG (Retrieval-Augmented Generation)
55:    # LAYER 1: RAG RETRIEVAL POOL (What to pull from knowledge)
56:    print("\n1️⃣  RAG RETRIEVAL INTERFACE")
68:    print("   ✓ RAG retrieval pool (pulls from GISGEODB + ChromaDB)")
185:    print("   ✓ GISGEODB → RAG → 5DGM")
197:        'RAG' as source,
219:        'RAG', 'Connected'
244:    print("EXTERNAL KNOWLEDGE → RAG POOL")
249:    print("RAG POOL → 5TH DARWIN GÖDEL MACHINE")

services/rag_client.py
3:Ms. Jarvis RAG client for Fifth DGM and other services.
6:GIS RAG ("msjarvisgis") via the Chroma v2 HTTP API.
15:CHROMA_URL = os.getenv("GIS_RAG_CHROMA_URL", "http://jarvis-chroma:8002")
17:GIS_COLLECTION = os.getenv("GIS_RAG_COLLECTION", "msjarvisgis")

services/psychological_rag_domain_psychological_rag_domain.py
10:PSYCHOLOGICAL RAG DOMAIN SERVICE
11:Specialized RAG for psychology, mental health, and therapeutic content
41:    title="Psychological RAG Domain",
43:    description="Specialized RAG for psychological and mental health knowledge"
77:        "service": "Psychological RAG Domain",
173:    Chroma-backed psychological RAG query.
199:    """Add document to psychological RAG"""
217:    logger.info(f"🧘 Psychological RAG Domain starting on port {port}")

services/swagger_gateway.py
26:    "rag": {"url": "http://localhost:${RAG_SERVER_PORT}", "prefix": "/rag"},

services/ai_server_20llm_FINAL.py
28:        f"{len(rag_hits)} msjarvisgis RAG hits."
34:          "the WV local_resources_index database, and the msjarvisgis RAG layer.\n"
38:        + "RAG hits: " + str(rag_hits) + "\n"

services/email_rag_integration.py
6:"""Email → RAG Storage Integration"""
14:    """Store email conversation in RAG for future retrieval"""
40:            logger.info(f"📝 Stored {direction} email in RAG: {subject[:40]}...")
43:        logger.warning(f"RAG storage: {e}")
47:    """Search past email conversations in RAG"""

services/rag_server.psychology_patched.py
6:"""Ms. Jarvis RAG Server - Knowledge Base with Dynamic Port Scheduling"""
40:app = FastAPI(title="Ms. Jarvis RAG", version="1.0.0", docs_url="/docs", redoc_url="/redoc")
72:class RAGServer:
177:logger.info("🚀 Initializing RAG Server with Dynamic Port Scheduling...")
178:rag = RAGServer()
179:logger.info(f"✅ RAG Server Ready on port {rag.port}!")
185:        "service": "Ms. Jarvis RAG",
273:    logger.info(f"🚀 Starting RAG Server on dynamically allocated port {port_service.port}")

services/rag_5100_final.py
7:app = FastAPI(title="RAG Consensus", version="1.0")

services/jarvis-woah_dgm_supervisor_woah_fixed.py
218:    """Sync conversational memory to RAG"""
225:    # Find RAG services
236:    # Simple memory sync to RAG
239:            # Test RAG connection

services/master_chat_orchestrator_v8_spiritual_complete.py
71:    "rag_server": "http://localhost:${RAG_SERVER_PORT}",
238:    10. RAG Knowledge Integration (including Vatican content)
399:    # (Psychology, Temporal, Maternal, RAG, etc. - same as v7)
423:    # Simplified RAG integration for this version
424:    logger.info("📚 Layer 11: RAG knowledge integration (including Vatican content)...")
439:                    logger.info(f"   ✅ Spiritual RAG knowledge: {len(rag_context)} chars")
441:        logger.warning(f"   ⚠️  Spiritual RAG integration failed: {e}")

services/performance_optimization_analyzer.py
29:            "Multi_RAG_DGM": {"url": "http://localhost:4011", "endpoint": "/health"},
30:            "RAG_Server": {"url": "http://localhost:${RAG_SERVER_PORT}", "endpoint": "/health"},
34:            "Spiritual_RAG": {"url": "http://localhost:4013", "endpoint": "/health"},
35:            "Psychological_RAG": {"url": "http://localhost:4014", "endpoint": "/health"},
438:                "Consider read replicas for RAG databases",

services/RESTORATION_CERTIFICATE_CORRECTED.txt
47:✅ RAG Knowledge Server (Port 8003)

services/port_9000_69dgm_bridge.py.backup_20260307_072741
15:# Import RAG integration
32:# Initialize RAG integration
33:print("Initializing 69-DGM RAG Integration...")
35:print("✓ RAG Integration ready")
269:        "service": "69-DGM Bridge (RAG-Integrated)",
323:Version: 2.0.0 (RAG-Integrated)

services/master_chat_orchestrator_v9_dgm_complete.py
21:- Multi-RAG domain specialization
91:            "🔀 Multi-RAG Domain Specialization",
118:    # Check Multi-RAG status

services/cleanup_manifest.txt
2:MS. EGERIA JARVIS - STORAGE CLEANUP MANIFEST

services/ai_server_20llm_PRODUCTION.py.backup_response_length
57:        f"{len(rag_hits)} msjarvisgis RAG hits."
63:          "the WV local_resources_index database, and the msjarvisgis RAG layer.\n"
67:        + "RAG hits: " + str(rag_hits) + "\n"

services/dgm_rag_integration_v2.py
3:69-DGM RAG Integration Layer (Enhanced)
17:class DGMRAGIntegration:
23:        print(f"✓ DGM RAG Integration initialized: {self.chroma_base}")
224:        _dgm_rag = DGMRAGIntegration()

services/email_auto_checker.py
6:"""Auto-check emails and store in RAG"""
16:RAG_SERVICE = "http://jarvis-rag-server:8003"
20:    """Check emails, respond, and store in RAG"""
30:                        logger.info(f"📧 Stored {data['stored_in_rag']} emails in RAG")

services/add_web_research_storage.py
6:"""Add automatic RAG storage to web research"""
13:        # Auto-store web research results in RAG
34:                    logger.info(f"📝 Stored web research in RAG: {query[:50]}")

services/comprehensive_gisgeodb_audit_FIXED.py
128:        logger.info("5️⃣  STORAGE DISTRIBUTION (185GB across datasets)")
155:        with open('data/STORAGE_DISTRIBUTION.csv', 'w', newline='') as f:
160:        logger.info(f"✅ Created STORAGE_DISTRIBUTION.csv")

services/ultimate_web_orchestrator.py
9:Darwin-Gödel Machine + WOAH integrated with RAG and Ms. Egeria Jarvis
98:            "multi_rag": {"port": 4011, "name": "Multi-RAG System"},
99:            "rag_server": {"port": 8003, "name": "RAG Server"},
101:            "gpu_rag": {"port": 4016, "name": "GPU RAG"},
120:        """Query RAG system with DGM optimization"""
124:        # Try GPU-accelerated RAG first
139:                logger.warning(f"GPU RAG failed: {e}")
141:        # Fallback to multi-RAG system
156:                logger.warning(f"Multi-RAG failed: {e}")
179:        # Get RAG context
353:                <h4>RAG Queries</h4>
548:    logger.info("   🎮 GPU + RAG: Optimized")

services/gpu_accelerated_rag_fixed.py
7:GPU-ACCELERATED RAG SYSTEM - FIXED VERSION
8:High-performance RAG using RTX 4070 GPU with ChromaDB
42:    title="GPU-Accelerated RAG System - Fixed",
47:class GPUAcceleratedRAGFixed:
56:        logger.info(f"🎮 Initializing GPU RAG Fixed on {self.device}")
259:gpu_rag_fixed = GPUAcceleratedRAGFixed()
274:        "service": "GPU-Accelerated RAG System - Fixed",
331:    logger.info(f"🚀 GPU-Accelerated RAG Fixed starting on port {port}")

services/nbb_darwin_godel_machines.py.pre_mapping
50:    dgm_agent: str = "DGM_RAG_TUNER"

services/rag_server.py
3:"""Ms. Jarvis RAG Server - Knowledge Base with Dynamic Port Scheduling + Rich results_by_source
8:- Designed to be called by Ms. Jarvis ULTIMATE as the RAG backend.
38:# Lock internal RAG port to 8003 (docker-compose maps host 8003 -> container 8003)
39:RAG_INTERNAL_PORT = int(os.getenv("RAG_PORT", "8003"))
40:port_service.register_service(RAG_INTERNAL_PORT)
45:    title="Ms. Jarvis RAG",
104:# RAG Server class (Chroma, embeddings, knowledge)
106:class RAGServer:
108:        logger.info("🧠 Initializing RAGServer...")
167:        # Expose main KBs to RAG search (tolerate missing optional collections)
253:        Rich RAG search used by main brain:
280:                    f"RAG rich_search error for collection {collection_name}: {e}"
354:logger.info("🚀 Initializing RAG Server with Dynamic Port Scheduling...")
355:rag = RAGServer()
356:logger.info(f"✅ RAG Server Ready on port {rag.port}!")
366:        "service": "Ms. Jarvis RAG",
509:        f"🚀 Starting RAG Server on dynamically allocated port {port_service.port}"

services/port_9000_69dgm_bridge.py.backup_20260307_072757
15:# Import RAG integration
32:# Initialize RAG integration
33:print("Initializing 69-DGM RAG Integration...")
35:print("✓ RAG Integration ready")
269:        "service": "69-DGM Bridge (RAG-Integrated)",
323:Version: 2.0.0 (RAG-Integrated)

services/create_tile_index.py
97:                'COVERAGE_NOTE': 'Estimated coverage - grid-based approximation'

services/rag_grounded_v2.py
2:rag_grounded_v2 — Truth Verification via RAG + DGM Layer
19:RAG_SERVER_URL = os.getenv("RAG_SERVER_URL",   "http://jarvis-rag-server:8000")
22:    title="rag_grounded_v2 — RAG Truth Verification",
23:    description="OI-23 closure. Grounded truth verification via RAG + DGM. Chapter 33 §33.10.",
66:        # Step 1 — Query RAG server for grounding evidence
68:            r = await client.post(f"{RAG_SERVER_URL}/query",
76:            logger.warning(f"RAG server unavailable: {e}")

services/complete_system_audit.py
73:        return "Multi_RAG_DGM"
107:        return "RAG_Server"
143:    """Get Multi-RAG domain status"""
150:            return {"error": "Multi-RAG not responding"}
214:        if service_name in ["Ms_Egeria_Jarvis_v9", "DGM_Supervisor_WOAH", "Multi_RAG_DGM"]:
224:        elif service_name in ["RAG_Server", "LLM_Bridge", "Consensus_Service"]:
262:    # 3. Multi-RAG Domain Status
263:    print(f"\n🔀 MULTI-RAG DOMAIN STATUS:")
273:        print(f"   📚 Active RAGs: {dgm_status_info.get('active_rags', 0)}")
277:        print(f"   ❌ Multi-RAG Error: {rag_status['error']}")
294:        ("Multi-RAG Domain Specialization", "✅ 4 specialized knowledge domains"),
307:        ("Complete Knowledge Integration", "✅ RAG + scraped content")

services/master_chat_orchestrator_v9_optimized.py
75:    "rag_server": "http://localhost:${RAG_SERVER_PORT}",

services/ingest_gis_features_to_chromadb.py
7:CHROMA_URL = os.getenv("GIS_RAG_CHROMA_URL", "http://localhost:8002").rstrip("/")
10:COLLECTION_NAME = os.getenv("GIS_RAG_COLLECTION", "geospatialfeatures")
12:EMBED_URL = os.getenv("GIS_RAG_EMBED_URL", "http://jarvis-ollama:11434")  # adjust if needed

services/web_connectivity_analyzer.py
31:            "Multi-RAG System": {"port": 4011, "endpoint": "/health", "type": "knowledge_interface"},
32:            "RAG Server": {"port": 8003, "endpoint": "/health", "type": "search_interface"},
34:            "GPU RAG Fixed": {"port": 4016, "endpoint": "/health", "type": "gpu_search_interface"}

services/ai_server_20llm_PRODUCTION.py.backup_before_full_synthesis
57:        f"{len(rag_hits)} msjarvisgis RAG hits."
63:          "the WV local_resources_index database, and the msjarvisgis RAG layer.\n"
67:        + "RAG hits: " + str(rag_hits) + "\n"

services/extract_all_chromadb_to_gis.py
24:    logger.info("📚 EXTRACTING ALL DATA FROM CHROMADB PERSISTENT STORAGE")

services/fix_background_storage.py
27:    # Store in RAG (background task - doesn't block response)
34:    logger.info(f"📝 Queued for RAG storage: {request.message[:50]}...")

services/multi_model_consensus.py
12:1. RAG provides context
218:    Flow: RAG context → 4 experts → judge → persona → response

services/update_gisgeodb_schema.py
24:        c.execute("PRAGMA table_info(geographic_knowledge);")
48:        c.execute("PRAGMA table_info(geographic_knowledge);")

services/rest_endpoints.txt
81:./ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP.py:405:@app.get("/rag/supervisor", tags=["RAG-Supervisor"])
448:./ms_jarvis_main_gateway.backup_1762220815.py:139:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
462:./ms_jarvis_main_gateway.backup_1762220815.py:207:@app.get("/rag-knowledge-stats", tags=["Whitebox"], summary="RAG & Knowledge Base Statistics")
625:./ms_jarvis_main_gateway.py:102:@app.post("/rag-query", tags=["RAG"])
626:./ms_jarvis_main_gateway.py:110:@app.get("/rag-status", tags=["RAG"])
669:./ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER.py:350:@app.get("/rag/supervisor", tags=["RAG-Supervisor"])
722:./ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:149:@app.post("/rag-query", tags=["RAG"])
723:./ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:158:@app.get("/rag-status", tags=["RAG"])
805:./ms_jarvis_unified_gateway_v4.3.pre_manifest.backup.py:351:@app.get("/rag/supervisor", tags=["RAG-Supervisor"])
854:./ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:366:@app.get("/rag/supervisor", tags=["RAG-Supervisor"])
1058:./ms_jarvis_unified_swagger_gateway_BACKUP.py:139:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
1072:./ms_jarvis_unified_swagger_gateway_BACKUP.py:207:@app.get("/rag-knowledge-stats", tags=["transparency_mode"], summary="RAG & Knowledge Base Statistics")
1136:./ms_jarvis_main_gateway.py.30endpoints_backup.py:149:@app.post("/rag-query", tags=["RAG"])
1137:./ms_jarvis_main_gateway.py.30endpoints_backup.py:158:@app.get("/rag-status", tags=["RAG"])
1420:./ms_jarvis_unified_swagger_gateway_FIXED.py:189:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
1434:./ms_jarvis_unified_swagger_gateway_FIXED.py:257:@app.get("/rag-knowledge-stats", tags=["transparency_mode"], summary="RAG & Knowledge Base Statistics")
1546:./ms_jarvis_unified_gateway_v4.3.backup.py:349:@app.get("/rag/supervisor", tags=["RAG-Supervisor"])
1684:./ms_jarvis_main_gateway.backup_error.py:139:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
1698:./ms_jarvis_main_gateway.backup_error.py:207:@app.get("/rag-knowledge-stats", tags=["Whitebox"], summary="RAG & Knowledge Base Statistics")
1735:./ms_jarvis_unified_swagger_gateway_FINAL.py:139:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
1749:./ms_jarvis_unified_swagger_gateway_FINAL.py:207:@app.get("/rag-knowledge-stats", tags=["transparency_mode"], summary="RAG & Knowledge Base Statistics")
1868:./ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:139:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
1882:./ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:207:@app.get("/rag-knowledge-stats", tags=["transparency_mode"], summary="RAG & Knowledge Base Statistics")

services/main_brain.py
86:    Remove RAG multi-agent metadata from responses while preserving text.
307:        # UPDATED: GIS RAG now uses /gis_rag instead of /search
771:    Build SPIRITUAL RAG context FIRST - foundational knowledge layer.
772:    This is queried before general RAG to ground all responses in spiritual wisdom.
819:    Build RAG context from jarvis-gis-rag if available.
895:    Store in RAG as background task - doesn't block response.
901:        # 1) Legacy RAG server write with duplicate check
1294:    Fast, low-latency chat path. Skips RAG and web-research. Calls 20-LLM with a tight timeout.

services/ai_server_20llm_PRODUCTION.py.backup_presedfix
57:        f"{len(rag_hits)} msjarvisgis RAG hits."
63:          "the WV local_resources_index database, and the msjarvisgis RAG layer.\n"
67:        + "RAG hits: " + str(rag_hits) + "\n"

services/geo_rag_debug_app.py
5:app = FastAPI(title="Geo RAG Debug", version="1.0.0")

services/master_chat_orchestrator.py
20:RAG → [LLM Bridge OR Multi-Model Consensus] → Response
30:    description="RAG-enhanced with fast/consensus modes"
106:    # STEP 1: Get RAG context
107:    logger.info("📚 Querying RAG...")
125:        logger.warning(f"   ⚠️  RAG failed: {e}")

services/rag_temporal.py
32:# RAG server configuration (unified RAG on rag-server:8003)
34:RAG_SERVER_HOST = os.getenv("RAG_SERVER_HOST", "rag-server")
35:RAG_SERVER_PORT = int(os.getenv("RAG_SERVER_PORT", "8003"))
36:RAG_SEARCH_URL = f"http://{RAG_SERVER_HOST}:{RAG_SERVER_PORT}/search"
45:app = FastAPI(title="RAG Temporal Service", version="1.0.0")
66:        "description": "Temporal RAG domain for time-aware queries.",
156:    Temporal RAG implementation.
157:    Proxies to unified RAG /search and applies temporal-aware post-processing.
166:    # Base search body for unified RAG server
169:    # Do NOT set a default collection; rely on unified RAG multi-collection search.
179:    logger.info(f"[{SERVICE_NAME}] → RAG /search query='{query[:80]}' body={search_body}")
183:            resp = await client.post(RAG_SEARCH_URL, json=search_body)
187:        logger.error(f"[{SERVICE_NAME}] Error calling RAG server at {RAG_SEARCH_URL}: {e}")
188:        raise HTTPException(status_code=502, detail=f"Error calling RAG server: {e}")

services/ai_server_original_backup.py
6:"""Ms. Jarvis - Multi-Agent AI with RAG Knowledge Integration"""
52:        logger.info(f"🧠 Ms. Jarvis initializing with RAG integration")
95:                response = await client.get("http://localhost:${RAG_SERVER_PORT}/health")
105:        """Search RAG knowledge base"""
115:                    "http://localhost:${RAG_SERVER_PORT}/search",
120:                    logger.info(f"📚 RAG found {len(results)} knowledge chunks")
123:            logger.error(f"RAG search error: {e}")
133:            # Add RAG knowledge
137:                logger.info("✅ RAG knowledge added to context")
147:            # Add RAG knowledge to prompt if available
170:        logger.info("🤖 Running 4 agents with RAG knowledge...")
235:logger.info("🚀 Starting Ms. Jarvis with RAG...")

services/master_chat_orchestrator_v6_biologics.py
52:    "rag_server": "http://localhost:${RAG_SERVER_PORT}",
151:    4. RAG knowledge retrieval
240:    # LAYER 4-7: Continue with consciousness processing (temporal, maternal, RAG, etc.)
280:    # RAG Knowledge
281:    logger.info("📚 Layer 6: RAG knowledge retrieval...")
296:                    logger.info(f"   ✅ RAG context: {len(rag_context)} chars")
298:        logger.warning(f"   ⚠️  RAG retrieval failed: {e}")

services/PORTS_REGISTRY_RAW.txt
499:/home/ms-jarvis/msjarvis-rebuild/services/multi_rag_dgm_system.py:                    port = RAG_DOMAINS[target_domain]["port"]

services/rag_server_min.py
21:MIN_RAG_PORT = int(os.getenv("MIN_RAG_PORT", "8103"))
40:class RAGServer:
42:        logger.info("🚀 RAGServer(minimal).__init__ starting")
46:        logger.info("🚀 RAGServer(minimal).__init__ complete")
73:        logger.info("🔍 MIN RAG search: %r, top_k=%d", query, top_k)
99:            logger.info("✅ MIN RAG search returning %d results", len(chunks))
102:            logger.error("MIN RAG search error: %s", e, exc_info=True)
107:        logger.info("📝 MIN RAG store called for user_id=%s", user_id)
117:            logger.info("✅ MIN RAG stored %d chars", len(text))
120:            logger.error("MIN RAG store error: %s", e, exc_info=True)
124:rag_min = RAGServer()
125:app = FastAPI(title="Ms. Jarvis RAG (Minimal)", version="1.0.0")
150:    return {"status": "healthy", "port": MIN_RAG_PORT}
185:    uvicorn.run(app, host="0.0.0.0", port=MIN_RAG_PORT, log_level="debug")

services/rag_first_workflow.py
7:RAG-First Workflow Enhancement
8:Checks RAG before web search, stores results after
17:    """Check RAG before doing web search"""
30:                        logger.info(f"✅ RAG cache hit! Score: {best_match['score']:.2f}")
33:        logger.debug(f"RAG check: {e}")
38:    """Store query/response in RAG for future use"""
55:            logger.info(f"📝 Stored in RAG: {query[:50]}...")
58:        logger.warning(f"RAG storage failed: {e}")

services/main_brain_legacy_backup.py
178:    """Store in RAG as background task - doesn't block response"""
216:    """Remove RAG metadata from responses"""
433:    # Phase 1.5: RAG + Web context
434:    logger.info("Phase 1.5: Querying RAG and Web for context...")
449:            logger.info(f"  ✅ RAG context length: {len(rag_context)}")
478:        logger.info("  ✅ Message enhanced with fused RAG + Web context")
535:        logger.info(f"📝 Queued for RAG storage: {message[:40]}...")

services/add_auto_store.py
6:"""Add automatic RAG storage after processing"""
24:        storage_block = f'''{indent}# Auto-store in RAG for future queries

services/msjarvisconsciousnessbridge.py
22:    description="Bridges unified gateway to 22-LLM + RAG stack (Docker URLs)",
61:            # Direct RAG
69:                state["rag_consensus"] = f"RAG error: {e}"

services/gisgeodbdirectaccess.py
24:    """Check DB integrity with PRAGMA."""
27:            result = conn.execute('PRAGMA integrity_check;').fetchone()[0]

services/create_consciousness_data_integration.psychology_patched.py
32:  • RAG (Retrieval-Augmented Generation)
55:    # LAYER 1: RAG RETRIEVAL POOL (What to pull from knowledge)
56:    print("\n1️⃣  RAG RETRIEVAL INTERFACE")
68:    print("   ✓ RAG retrieval pool (pulls from GISGEODB + ChromaDB)")
185:    print("   ✓ GISGEODB → RAG → 5DGM")
197:        'RAG' as source,
219:        'RAG', 'Connected'
244:    print("EXTERNAL KNOWLEDGE → RAG POOL")
249:    print("RAG POOL → 5TH DARWIN GÖDEL MACHINE")

services/bridge_69dgm.py
6:# Use Chroma directly - RAG server search is broken
10:app = FastAPI(title="69-DGM Bridge (Chroma RAG)")

services/clean_service_candidates.txt
179:./LOAD_AAACPE_RAG.sh
379:./ADD_RAG_RETRIEVAL_8050.sh

services/rag_direct_debug.py
40:app = FastAPI(title="RAG Direct Debug", version="1.0")
46:    and return a compact text snippet suitable for RAG context.
71:        # If anything fails, RAG still works with its normal context.
105:    print("RAG_DIRECT_DEBUG context to jarvis_llm1:", context, flush=True)

services/msjarvis_gateway_with_judge_filtering.py
58:        # RAG

services/registration_biometric_production_final.py
15:BIOMETRIC_STORAGE = "/tmp/biometric_images"
16:os.makedirs(BIOMETRIC_STORAGE, exist_ok=True)
681:    image_path = f"{BIOMETRIC_STORAGE}/{ueid}_{image_hash[:8]}.jpg"

services/master_chat_orchestrator_v9_gpu_optimized.py
175:            # Use GPU-accelerated RAG (will be started automatically)
176:            logger.info("⚡ Using GPU-accelerated RAG search...")
178:                "http://localhost:4015/search",  # GPU RAG service
187:            logger.warning(f"   ⚠️ GPU RAG failed: {e}")

services/load_rag_data.py
7:Load RAG data into ChromaDB for Mamma Kidd
83:print("\n🎊 RAG DATABASE READY FOR MAMMA KIDD! 🎊")

services/create_perpetual_storage_layer.py
7:PERPETUAL STORAGE ARCHITECTURE
22:    print("\n🗃️  Creating PERPETUAL STORAGE ARCHITECTURE")
25:    # TIER 1: HOT STORAGE (Active data, real-time access)
41:    # TIER 2: WARM STORAGE (Archive, occasional access)
58:    # TIER 3: COLD STORAGE (Historical, rarely accessed)
158:    print("✅ PERPETUAL STORAGE ARCHITECTURE CREATED")
161:    print("STORAGE GUARANTEE:")
168:    print("STORAGE TIERS:")

services/nbb_darwin_godel_machines.py
50:    dgm_agent: str = "DGM_RAG_TUNER"

services/dgm_supervisor_woah.py
277:    """Sync all conversational memory to RAG systems"""
282:    logger.info("🧠 Synchronizing conversational memory to RAG...")
284:    # Find all RAG services
289:        # Default to main RAG
309:                # Process memory data for RAG ingestion
312:                # Send to RAG services
332:    """Process memory data into RAG-compatible documents"""
375:    """Sync memory documents to a RAG service"""

services/port_9000_69dgm_bridge.py.backup_20260307_070432
14:# Import RAG integration
24:# Initialize RAG integration
25:print("Initializing 69-DGM RAG Integration...")
27:print("✓ RAG Integration ready")
222:        "service": "69-DGM Bridge (RAG-Integrated)",
276:Version: 2.0.0 (RAG-Integrated)

services/ai_server_19llm_CONSCIOUS.backup_20251013_083103.py
297:            mem = requests.post("http://localhost:${RAG_SERVER_PORT}/search", json={
420:            requests.post("http://localhost:${RAG_SERVER_PORT}/store", json={

services/jarvis_llm1.py
110:        "You are Ms. Jarvis, a mesh-native assistant operating over a GBIM + RAG stack.\n"

services/ai_server_integrated.py
3:# This integrates 22-LLM consensus WITH the chat/RAG system
8:# Architecture: Chat API → RAG Context → 22-LLM Consensus → Response
24:    Full pipeline: Chat → RAG → 22-LLM Consensus
26:    # Step 1: Get RAG context from chat server
29:            # Query chat server for RAG context
39:    # Step 2: Send to 22-LLM consensus with RAG context

services/working_full_pipeline_WITH_SPATIAL_TEMPORAL.py
53:    # STEP 1: RAG

services/PORT_AUDIT_RAW.txt
807:/home/ms-jarvis/msjarvis-rebuild/services/multi_rag_dgm_system.py:306:                    port = RAG_DOMAINS[target_domain]["port"]

services/rag_to_gis_sync.py
7:RAG Knowledge Base → GIS Spatial Index Sync
8:Load all RAG knowledge and map to GIS/spatial storage

services/gis_rag_service.py
2:GIS RAG Service for Ms. Jarvis
15:GIS_RAG_URL = os.getenv("GIS_RAG_CHROMA_URL", "http://jarvis-chroma:8000").rstrip("/")
16:GIS_COLLECTION = os.getenv("GIS_RAG_COLLECTION", "geospatialfeatures")
24:app = FastAPI(title="Ms. Jarvis GIS RAG", version="0.3.2")
27:class GISRAGRequest(BaseModel):
34:class GISRAGHit(BaseModel):
43:class GISRAGResponse(BaseModel):
44:    hits: List[GISRAGHit]
54:        f"{GIS_RAG_URL}/api/v2/tenants/{CHROMA_TENANT}"
114:@app.post("/gis_rag", response_model=GISRAGResponse)
115:async def gis_rag(req: GISRAGRequest):
126:                f"{GIS_RAG_URL}/api/v2/tenants/{CHROMA_TENANT}"
152:            detail=f"Error calling GIS RAG backend: {repr(e)[:300]}",
155:    hits: List[GISRAGHit] = []
161:        return GISRAGResponse(hits=[])
169:            GISRAGHit(
179:    return GISRAGResponse(hits=hits)
182:@app.post("/search", response_model=GISRAGResponse)
183:async def search_endpoint(req: GISRAGRequest = Body(...)):

services/nbb_darwin_godel_machines.py.backup_20260307_1121
50:    dgm_agent: str = "DGM_RAG_TUNER"

services/route_declarations_raw.txt
1289:ms_jarvis_main_gateway.backup_1762220815.py:139:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
1303:ms_jarvis_main_gateway.backup_1762220815.py:207:@app.get("/rag-knowledge-stats", tags=["Whitebox"], summary="RAG & Knowledge Base Statistics")
1330:ms_jarvis_main_gateway.backup_error.py:139:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
1344:ms_jarvis_main_gateway.backup_error.py:207:@app.get("/rag-knowledge-stats", tags=["Whitebox"], summary="RAG & Knowledge Base Statistics")
1410:ms_jarvis_main_gateway.py:103:@app.post("/rag-query", tags=["RAG"])
1411:ms_jarvis_main_gateway.py:111:@app.get("/rag-status", tags=["RAG"])
1446:ms_jarvis_main_gateway.py.30endpoints_backup.py:150:@app.post("/rag-query", tags=["RAG"])
1447:ms_jarvis_main_gateway.py.30endpoints_backup.py:159:@app.get("/rag-status", tags=["RAG"])
1476:ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:150:@app.post("/rag-query", tags=["RAG"])
1477:ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:159:@app.get("/rag-status", tags=["RAG"])
1628:ms_jarvis_unified_gateway_v4.3.20251124.py:405:@app.get("/rag/supervisor", tags=["RAG-Supervisor"])
1654:ms_jarvis_unified_gateway_v4.3.backup.py:349:@app.get("/rag/supervisor", tags=["RAG-Supervisor"])
1676:ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:366:@app.get("/rag/supervisor", tags=["RAG-Supervisor"])
1735:ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP.py:405:@app.get("/rag/supervisor", tags=["RAG-Supervisor"])
1761:ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER.py:350:@app.get("/rag/supervisor", tags=["RAG-Supervisor"])
1787:ms_jarvis_unified_gateway_v4.3.pre_manifest.backup.py:351:@app.get("/rag/supervisor", tags=["RAG-Supervisor"])
1821:ms_jarvis_unified_swagger_gateway_BACKUP.py:139:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
1835:ms_jarvis_unified_swagger_gateway_BACKUP.py:207:@app.get("/rag-knowledge-stats", tags=["transparency_mode"], summary="RAG & Knowledge Base Statistics")
1900:ms_jarvis_unified_swagger_gateway_FINAL.py:139:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
1914:ms_jarvis_unified_swagger_gateway_FINAL.py:207:@app.get("/rag-knowledge-stats", tags=["transparency_mode"], summary="RAG & Knowledge Base Statistics")
1941:ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:139:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
1955:ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:207:@app.get("/rag-knowledge-stats", tags=["transparency_mode"], summary="RAG & Knowledge Base Statistics")
1979:ms_jarvis_unified_swagger_gateway_FIXED.py:190:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
1993:ms_jarvis_unified_swagger_gateway_FIXED.py:258:@app.get("/rag-knowledge-stats", tags=["transparency_mode"], summary="RAG & Knowledge Base Statistics")

services/gateway_wv_entanglement.py
6:GIS_RAG_API_URL = "http://localhost:8053/gisragquery"
82:        GIS_RAG_API_URL,
129:    Heuristic: derive domain tags for RAG biasing based on entities/resources.
162:    Pull layer/feature ids from GIS RAG hits (which already bridge to GeoDB).

services/cloudflare_domain_integration.py
117:            "rag": 4016,           # GPU RAG system

services/ai_server_22llm.psychology_patched.py
97:            logger.info("✅ ChromaDB connected - RAG memory active")
215:        # Get personality guidance from RAG
226:                logger.warning(f"RAG query failed: {e}")

services/rag_geospatial.py
32:# RAG server configuration (unified RAG on rag-server:8003)
34:RAG_SERVER_HOST = os.getenv("RAG_SERVER_HOST", "rag-server")
35:RAG_SERVER_PORT = int(os.getenv("RAG_SERVER_PORT", "8003"))
36:RAG_SEARCH_URL = f"http://{RAG_SERVER_HOST}:{RAG_SERVER_PORT}/search"
45:app = FastAPI(title="RAG Geospatial Service", version="1.0.0")
68:        "description": "Geospatial / GBIM / MountainShares RAG domain.",
129:    Geospatial / GBIM / MountainShares RAG implementation.
130:    Proxies to unified RAG /search and applies optional regional filters and distance ranking.
151:    logger.info(f"[{SERVICE_NAME}] → RAG /search query='{query[:80]}' body={search_body}")
155:            resp = await client.post(RAG_SEARCH_URL, json=search_body)
159:        logger.error(f"[{SERVICE_NAME}] Error calling RAG server at {RAG_SEARCH_URL}: {e}")
160:        raise HTTPException(status_code=502, detail=f"Error calling RAG server: {e}")

services/ai_server_4llm.py
6:"""Ms. Jarvis - Multi-Agent AI with RAG Knowledge Integration"""
52:        logger.info(f"🧠 Ms. Jarvis initializing with RAG integration")
95:                response = await client.get("http://localhost:${RAG_SERVER_PORT}/health")
105:        """Search RAG knowledge base"""
115:                    "http://localhost:${RAG_SERVER_PORT}/search",
120:                    logger.info(f"📚 RAG found {len(results)} knowledge chunks")
123:            logger.error(f"RAG search error: {e}")
133:            # Add RAG knowledge
137:                logger.info("✅ RAG knowledge added to context")
147:            # Add RAG knowledge to prompt if available
170:        logger.info("🤖 Running 4 agents with RAG knowledge...")
235:logger.info("🚀 Starting Ms. Jarvis with RAG...")

services/unified_consciousness_gateway_PRODUCTION.py
28:    RAG-powered unified chat handler.
45:        # Extract documents/content from RAG results
53:        # Augment incoming message with RAG context

services/roche_llm.py
218:                f"✅ ChromaDB connected on {chroma_host}:{chroma_port} - RAG memory active"
410:                logger.warning(f"RAG query failed: {e}")

services/ultimate_chat_current.txt
72:                    logger.info(f"  ✅ RAG context retrieved: {len(rag_context)} chars")
74:            logger.warning(f"  ⚠️  RAG query failed: {e}")
79:        logger.info("  ✅ Message enhanced with RAG context")
219:                        logger.info(f"  ✅ RAG: Found {rag_data['count']} knowledge results")
221:                logger.debug(f"  ⚠️  RAG Server: {str(e)[:50]}")
322:            logger.info(f"  RAG returned {len(results)} results")
333:                        logger.info(f"    ✅ Extracted RAG content: {content_text[:50]}...")

services/master_chat_orchestrator_v7_complete.py
64:    "rag_server": "http://localhost:${RAG_SERVER_PORT}",
186:            "core_infrastructure": 3,  # RAG, LLM, Consensus
202:    7. RAG Knowledge Integration
363:    # LAYER 7: RAG Knowledge Integration
364:    logger.info("📚 Layer 7: RAG knowledge integration...")
379:                    logger.info(f"   ✅ RAG knowledge: {len(rag_context)} chars")
381:        logger.warning(f"   ⚠️  RAG integration failed: {e}")

services/add_swagger_to_rag.py
1:# Update RAG server with Swagger documentation
16:    print("   ✅ Swagger already configured in RAG server")
21:    title="Ms. Jarvis RAG Server",
33:        print("   ✅ Swagger UI added to RAG server")
34:        print("   📖 Access at: http://localhost:${RAG_SERVER_PORT}/docs")

services/consciousness_coordinator.py
20:DIRECT_RAG_URL = "http://localhost:8199/direct_rag"
200:            resp = await client.post(DIRECT_RAG_URL, json=payload, timeout=300.0)

services/parse_world_files.py
121:                    'COVERAGE_WIDTH_FEET': 2500,  # Estimate
122:                    'COVERAGE_HEIGHT_FEET': 2500,

services/ai_server_22llm.py
203:                f"✅ ChromaDB connected on {chroma_host}:{chroma_port} - RAG memory active"
381:                logger.warning(f"RAG query failed: {e}")

services/jarvis-aaacpe-rag_aaacpe_rag_service.py
2:"""AaaCPE RAG Service - Appalachian Cultural Intelligence"""

services/msjarvisragserverwvpatch.py
8:class RAGQuery(BaseModel):
61:def rag_query(payload: RAGQuery):

services/rag_workflow.py
7:RAG-First Workflow: Check RAG → Web Search → Store → Return
16:class RAGWorkflow:
21:        """Check RAG first - return cached answer if good match found"""
34:                            logger.info(f"✅ RAG HIT! Score: {best['score']:.2f} for: {query[:50]}")
37:                            logger.info(f"⚠️  RAG score too high ({best['score']:.2f}), will search web")
39:            logger.debug(f"RAG search: {e}")
44:        """Store query/response in RAG for future retrieval"""
66:                    logger.info(f"📝 STORED in RAG: {query[:50]}...")
69:            logger.warning(f"RAG storage failed: {e}")
74:rag_workflow = RAGWorkflow()

services/manifest_endpoints.py
31:                {"name": "ChromaDB", "port": 8001, "type": "Docker", "purpose": "Vector RAG storage", "status": "RUNNING"},
82:            "consciousness": "Ollama qwen2.5:14b + Constitutional RAG",

services/start_gateway_with_guards.py
105:# COMPLETE STORAGE AUDIT

services/chromadb_main.py
10:# Fresh, dedicated Chroma persistence path for RAG

services/port_9000_69dgm_bridge.py.backup_20260307_072514
14:# Import RAG integration
24:# Initialize RAG integration
25:print("Initializing 69-DGM RAG Integration...")
27:print("✓ RAG Integration ready")
222:        "service": "69-DGM Bridge (RAG-Integrated)",
276:Version: 2.0.0 (RAG-Integrated)

services/ai_server_11llm_OPTIMIZED.py
190:    """Store in RAG as background task - doesn't block response"""
364:    # Phase 1.5: Querying RAG for context... (only if you later add rag_server)
365:    logger.info("Phase 1.5: Querying RAG for context...")
410:                # NOTE: placeholder; adjust when dedicated RAG HTTP front is live
412:                    "http://localhost:${RAG_SERVER_PORT}/query",
420:                        f"  ✅ RAG context retrieved: {len(rag_context)} chars"
423:            logger.warning(f"  ⚠️  RAG query failed: {e}")
425:    # Enhance message with RAG context
432:        logger.info("  ✅ Message enhanced with RAG context")
559:            # add "rag_server" here later if you bring up a dedicated RAG HTTP front
583:        # RAG Server - Knowledge Base Search (only if you add rag_server)
602:                            f"  ✅ RAG: Found {rag_data['count']} knowledge results"
605:                logger.debug(f"  ⚠️  RAG Server: {str(e)[:50]}")
712:            logger.info(f"  RAG returned {len(results)} results")
724:                            "    ✅ Extracted RAG content: "
817:    # Background RAG storage
960:                    logger.info("✅ Found similar deployment in RAG")
1163:            logger.info("📝 Email queued for RAG")
1190:            logger.info("📝 Website queued for RAG")
1221:    """Generate contextual insights from RAG results"""

services/aaacpe_rag_service.py
2:"""AaaCPE RAG Service - Appalachian Cultural Intelligence"""

services/Dockerfile.rag
14:# Use RAG-enhanced main

services/mountainshares_chain_monitor.py
15:# Contract details from RAG knowledge

services/main.py
181:    """Store in RAG as background task - doesn't block response"""
219:    """Remove RAG metadata from responses"""
450:    logger.info("Phase 1.5: Querying RAG and Web for context...")
465:            logger.info(f"  ✅ RAG context length: {len(rag_context)}")
494:        logger.info("  ✅ Message enhanced with fused RAG + Web context")
546:        logger.info(f"📝 Queued for RAG storage: {message[:40]}...")

services/response_sanitizer.py
22:    r"ChromaDB RAG.*",
44:    test = "lineage_pattern/Edward I via heritage_source_ref (ChromaDB RAG Import)"

services/jarvis-gis-rag_gis_rag_service.py
2:GIS RAG Service for Ms. Jarvis
16:GIS_RAG_URL = os.getenv("GIS_RAG_CHROMA_URL", "http://jarvis-chroma:8000").rstrip("/")
18:GIS_COLLECTION = os.getenv("GIS_RAG_COLLECTION", "geospatialfeatures")
28:app = FastAPI(title="Ms. Jarvis GIS RAG", version="0.3.0")
31:class GISRAGRequest(BaseModel):
38:class GISRAGHit(BaseModel):
47:class GISRAGResponse(BaseModel):
48:    hits: List[GISRAGHit]
66:        f"{GIS_RAG_URL}/api/v2/tenants/{CHROMA_TENANT}"
132:@app.post("/gis_rag", response_model=GISRAGResponse)
133:async def gis_rag(req: GISRAGRequest):
153:                f"{GIS_RAG_URL}/api/v2/tenants/{CHROMA_TENANT}"
179:            detail=f"Error calling GIS RAG backend: {repr(e)[:300]}",
182:    hits: List[GISRAGHit] = []
188:        return GISRAGResponse(hits=[])
195:        hit = GISRAGHit(
205:    return GISRAGResponse(hits=hits)
208:@app.post("/search", response_model=GISRAGResponse)
209:async def search_endpoint(req: GISRAGRequest = Body(...)):
211:    Alias so jarvis-main-brain can POST /search and get GIS RAG results.

./docker-compose.yml
28:    - PSYCHOLOGICAL_RAG_URL=http://psychological_rag_domain:9006
639:    - RAG_SERVER_URL=http://jarvis-rag-server:8003
1315:    - GIS_RAG_CHROMA_URL=http://jarvis-chroma:8000
1316:    - GIS_RAG_COLLECTION=geospatialfeatures
1385:    - PSYCHOLOGICAL_RAG_URL=http://psychological_rag_domain:9006

services/vatican_scraper_service.py
9:Feeds theological content into RAG for spiritual guidance integration
90:RAG_SERVER_URL = "http://localhost:${RAG_SERVER_PORT}"
188:    """Add theological content to RAG with spiritual categorization"""
195:                f"{RAG_SERVER_URL}/add_document",
214:            logger.error(f"Error adding theological content to RAG: {e}")

./seed_mountainshares.py
4:Uses the same Python client as main_brain.py — bypasses broken RAG server entirely.

services/fix_rag_store.py
17:                f"{RAG_URL}/store",
25:                f"{RAG_URL}/store",
45:print("✅ RAG store endpoint fixed!")

./Dockerfile.rag
14:# Use RAG-enhanced main

./STABLE_MODE_NOTE.txt
4:- RAG: wired to http://127.0.0.1:8003, /search returns results: []
11:This is the baseline to return to before deeper RAG/consensus experiments.

services/add_background_storage.py
29:    """Store in RAG as background task - doesn't block response"""

services/working_full_pipeline_FINAL_CONSCIOUSNESS.py
54:    # LAYER 3: Multi-RAG
64:                logger.info("✅ Multi-RAG")
66:        logger.info(f"RAG error: {e}")
67:    logger.info(f"DEBUG RAG context: {rag_context[:500]!r}")

./tmp_rag_slice.py
99:    """Store in RAG as background task - doesn't block response"""

./rag_local_resources.py
23:    """RAG over local_resources text only."""
31:    """RAG starting from a local image file path (flyer/photo)."""
45:    """Combined RAG over text + image collections."""
68:    RAG over local_resources with optional metadata filters.
140:    RAG over local_resources with optional metadata filters.
212:    RAG over local_resources with optional metadata filters.

services/optimized_timeouts.py
5:OPTIMIZED_TIMEOUTS = {'Ms. Egeria Jarvis v9': {'current_avg': 5.0, 'recommended_timeout': 10}, 'DGM Supervisor': {'current_avg': 5.0, 'recommended_timeout': 10}, 'Multi-RAG DGM': {'current_avg': 5.0, 'recommended_timeout': 10}, 'RAG Server': {'current_avg': 5.0, 'recommended_timeout': 10}, 'Spiritual Services': {'current_avg': 5.0, 'recommended_timeout': 10}}
11:RAG_SEARCH_TIMEOUT = 8.0  # RAG search operations

services/chromadb_v2_to_gis_sync.py
9:Everything in ChromaDB/RAG syncs to GIS with spatial indexing
74:                        "source": "ChromaDB_V2_RAG",

services/unifiedconsciousnessgatewayPRODUCTION.py
28:            message_with_rag = f'{message}\n\nRAG Context (H4H 1002 Cosine <0.8 UUID {collection.id}): {rag_context}\n\nAnalysis: Biblical Empire Theology 80% Acts 9 heritage_source_ref Edward I Strong WV H4H'
29:            print(f'RAG Injected: {len(rag_hits)} Hits Avg {avg_dist:.2f} < {threshold} (Cosine 8001)')
44:        print(f'Chroma Error: {chroma_ex} (Fallback No RAG)')
52:    print("Final RAG Context Message:", with_rag)

./ragservermain.py
2:Ms. Jarvis RAG Server - Unified Knowledge Retrieval Port 8003
93:    title="Ms. Jarvis RAG Server",
95:    description="Unified RAG service returning results_by_source for Ms. Jarvis ULTIMATE",
143:    logger.info(f"RAG search query={query[:80]} topk={request.topk}")
205:            logger.info(f"DEBUG RAG raw result for {collection_name}: {res}")
207:            logger.warning(f"RAG query error for collection {collection_name}: {e}")
264:    logger.info(f"RAG search completed query={query[:60]} count={total_count}")
384:        "service": "Ms. Jarvis RAG Server",
386:        "description": "Unified RAG server for Ms. Jarvis ULTIMATE, exposing search and store",
396:    logger.info("Starting Ms. Jarvis RAG Server on port 8003")

./gis_rag_server.py
5:app = FastAPI(title="GIS RAG")
14:class RAGHit(BaseModel):
21:@app.get("/gis_rag", response_model=list[RAGHit])
37:    hits: list[RAGHit] = []
40:            RAGHit(

services/phase7_integration.py
64:    "rag_server": "http://localhost:${RAG_SERVER_PORT}",
186:            "core_infrastructure": 3,  # RAG, LLM, Consensus
202:    7. RAG Knowledge Integration
363:    # LAYER 7: RAG Knowledge Integration
364:    logger.info("📚 Layer 7: RAG knowledge integration...")
379:                    logger.info(f"   ✅ RAG knowledge: {len(rag_context)} chars")
381:        logger.warning(f"   ⚠️  RAG integration failed: {e}")

./rag_server_main.py
3:Ms. Jarvis RAG Server - Unified Knowledge Retrieval
4:Port: 8003 (RAG Service)
31:    title="Ms. Jarvis RAG Server",
33:    description="Unified RAG service returning rich results_by_source for Ms. Jarvis ULTIMATE",
198:    logger.info(f"🔍 RAG /search query='{query[:80]}' top_k={request.top_k}")
201:    logger.debug(f"RAG where-clause: {where}")
218:            logger.warning(f"RAG query error for collection {collection_name}: {e}")
263:    logger.info(f"✅ RAG /search completed query='{query[:60]}' count={total_count}")
591:        "service": "Ms. Jarvis RAG Server",
593:        "description": "Unified RAG server for Ms. Jarvis ULTIMATE, exposing /search and /store",
607:    logger.info("🚀 Starting Ms. Jarvis RAG Server on port 8003")

services/hardware_optimization_analyzer.py
27:        print("💾 ANALYZING STORAGE CONFIGURATION:")
158:        print(f"\n💾 STORAGE OPTIMIZATION RECOMMENDATIONS:")
163:                "name": "Dual-Drive RAG Optimization",
164:                "description": "Split RAG databases across both 1TB drives for performance",
166:                    "Move General RAG to Drive 1 (/home partition)",
167:                    "Move Spiritual/Theological RAGs to Drive 2 (if mounted separately)",
170:                "benefit": "50-100% faster RAG operations through parallel I/O"
230:                    "name": "Parallel RAG Processing",
262:# STORAGE OPTIMIZATION FOR MS. EGERIA JARVIS v9
272:# RAG databases optimization
291:echo "   Optimized for: RAG performance, knowledge expansion, analytics"

./main_brain.py
103:    """Remove RAG metadata from responses"""
164:    # jarvis-rag-server unified RAG on 8003
358:        # RAG server: unified RAG exposes /search
595:    """Store in RAG as background task - doesn't block response"""
676:    - Skips RAG and web-research.
771:    - Builds RAG + web context
819:        # 2) Context building with timeouts (RAG + Web)

services/rag_5100_ensemble_fast.py
24:app = FastAPI(title="RAG Consensus Ensemble", version="2.0")

./index_gis_to_chroma.py
85:                metadata={"description": "WV geospatial features for Polymathmatic Geography RAG"}
92:            metadata={"description": "WV geospatial features for Polymathmatic Geography RAG"}

./services/quick_optimizations.py
23:        "http://localhost:${RAG_SERVER_PORT}/health",

./Dockerfile.ragservermain
10:# Copy only what the minimal RAG needs

services/RESTORATION_CERTIFICATE.txt
32:✅ RAG Knowledge Server (Port 8003)

services/ai_server_20llm_PRODUCTION.py.backup_synthesis
57:        f"{len(rag_hits)} msjarvisgis RAG hits."
63:          "the WV local_resources_index database, and the msjarvisgis RAG layer.\n"
67:        + "RAG hits: " + str(rag_hits) + "\n"

./services/working_full_pipeline.py
26:    # 1. RAG

./services/port_9000_69dgm_bridge.py
3:Bridge: Port 9000 Chat → 69-DGM Orchestrator + RAG Bridge
5:then, if approved, calls the 69-DGM RAG bridge for an answer.
25:# Downstream 69-DGM RAG bridge (bridge_69dgm.py)
70:        "then calls the 69-DGM RAG bridge for an answer"
138:# Call the 69-DGM RAG bridge (bridge_69dgm.py) after approval
142:    Call the 69-DGM RAG bridge (bridge_69dgm.py) to get an answer.
147:        f"🔗 Calling 69-DGM RAG bridge at {BRIDGE_69DGM_URL} for user={userid}"
157:            logger.info("✅ 69-DGM RAG bridge responded successfully")
161:                f"❌ 69-DGM RAG bridge error: HTTP {resp.status_code} "
166:        logger.error(f"Error calling 69-DGM RAG bridge: {e}")
171:# High-level chat handler: orchestrator + RAG + connector metadata
178:    2) If approved, calls the 69-DGM RAG bridge for an answer.
179:    3) If RAG fails, falls back to the previous static approval response.
211:        # Not approved; return verdict and do NOT call RAG
223:    # Approved by 69 validators → proceed to RAG bridge
224:    logger.info("✅ Message approved by 69 validators - proceeding to RAG bridge")
236:            # If RAG returns empty, fall back to approval text
253:    # RAG bridge failed; fall back to the original static approval response
255:        "⚠️ 69-DGM RAG bridge failed or returned no response; "
279:    then, if approved, through the 69-DGM RAG bridge.

./services/enhance_rag_knowledge.py
6:"""Enhance RAG server with all MountainShares documentation"""
13:print("🧠 Enhancing RAG server with MountainShares knowledge...")
15:# Connect to RAG server's ChromaDB
77:print(f"   🔍 RAG server knowledge base expanded!")

./services/rag_query_router.py
47:app = FastAPI(title="RAG Query Router", version="1.0.0")
52:# Base URLs for domain RAG services inside the mesh
53:RAG_SERVICE_URLS: Dict[str, str] = {
75:    # Optional filters to pass down to domain RAG services (they decide how to use them)
77:    # If true, router will call the selected RAG service and include its answer
95:    Registers this RAG query router into the Ms. Jarvis mesh registry in Redis.
103:        "description": "Routes queries to appropriate RAG domains/services.",
153:    Heuristic router for RAG domains.
301:# Downstream RAG service dispatch
305:    Calls the selected RAG domain service and returns its JSON response.
308:    base_url = RAG_SERVICE_URLS.get(service_name)
310:        raise HTTPException(status_code=500, detail=f"Unknown RAG service '{service_name}'")
335:            detail=f"Error calling downstream RAG service '{service_name}' at '{path}': {str(e)}",

./services/implement_safe_optimizations.py
102:        ("http://localhost:4011/health", "Multi-RAG DGM"),
103:        ("http://localhost:${RAG_SERVER_PORT}/health", "RAG Server"),
145:RAG_SEARCH_TIMEOUT = 8.0  # RAG search operations
379:        "http://localhost:${RAG_SERVER_PORT}",

./services/main_with_rag.py
6:"""Enhanced main.py with RAG-first workflow"""
14:# Override ultimate_chat to use RAG-first
21:    # STEP 1: Check RAG first
25:            "response": f"**From Knowledge Cache:**\n{rag_result}\n\n*Retrieved from RAG in <1s*",
36:    # STEP 3: Store result in RAG for future
50:print("✅ RAG-First workflow enabled")

./services/FULL_DEPLOYMENT_MANIFEST.txt
7:- Port 8003: RAG Server (ChromaDB) ✅

./services/nbb_darwin_godel_machines.py.backup_1772889398
50:    dgm_agent: str = "DGM_RAG_TUNER"

./services/system_dashboard.py
32:    "RAG Server": "http://localhost:${RAG_SERVER_PORT}",

./services/dgm_supervisor_woah_fixed.py
220:    """Sync conversational memory to RAG"""
227:    # Find RAG services
238:    # Simple memory sync to RAG
241:            # Test RAG connection

./services/aaacpe_scraper_service.py
3:AaaCPE Web Scraper - Feeds Current Appalachian Content into RAG

./backup_filename_index.txt
16848:ADD_RAG_RETRIEVAL_8050.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/services/ADD_RAG_RETRIEVAL_8050.sh
16849:ADD_RAG_RETRIEVAL_8050.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/services/ADD_RAG_RETRIEVAL_8050.sh
16850:ADD_RAG_RETRIEVAL_8050.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/ADD_RAG_RETRIEVAL_8050.sh
16851:ADD_RAG_RETRIEVAL_8050.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/services/ADD_RAG_RETRIEVAL_8050.sh
16852:ADD_RAG_RETRIEVAL_8050.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/ADD_RAG_RETRIEVAL_8050.sh
16853:ADD_RAG_RETRIEVAL_8050.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/services/ADD_RAG_RETRIEVAL_8050.sh
16854:ADD_RAG_RETRIEVAL_8050.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/ADD_RAG_RETRIEVAL_8050.sh
16855:ADD_RAG_RETRIEVAL_8050.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/services/ADD_RAG_RETRIEVAL_8050.sh
16856:ADD_RAG_RETRIEVAL_8050.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/ADD_RAG_RETRIEVAL_8050.sh
16857:ADD_RAG_RETRIEVAL_8050.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/ADD_RAG_RETRIEVAL_8050.sh
16858:ADD_RAG_RETRIEVAL_8050.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/services/ADD_RAG_RETRIEVAL_8050.sh
16859:ADD_RAG_RETRIEVAL_8050.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/services/ADD_RAG_RETRIEVAL_8050.sh
16860:ADD_RAG_RETRIEVAL_8050.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/ADD_RAG_RETRIEVAL_8050.sh
16861:ADD_RAG_RETRIEVAL_8050.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/ADD_RAG_RETRIEVAL_8050.sh
20159:FIX_RAG_FILTERING.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/FIX_RAG_FILTERING.sh
20160:FIX_RAG_FILTERING.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/services/FIX_RAG_FILTERING.sh
20161:FIX_RAG_FILTERING.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/services/FIX_RAG_FILTERING.sh
20162:FIX_RAG_FILTERING.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/FIX_RAG_FILTERING.sh
20163:FIX_RAG_FILTERING.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/services/FIX_RAG_FILTERING.sh
20164:FIX_RAG_FILTERING.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/FIX_RAG_FILTERING.sh
20165:FIX_RAG_FILTERING.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/services/FIX_RAG_FILTERING.sh
20166:FIX_RAG_FILTERING.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/FIX_RAG_FILTERING.sh
20167:FIX_RAG_FILTERING.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/FIX_RAG_FILTERING.sh
20168:FIX_RAG_FILTERING.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/FIX_RAG_FILTERING.sh
20169:FIX_RAG_FILTERING.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/FIX_RAG_FILTERING.sh
20170:FIX_RAG_FILTERING.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/services/FIX_RAG_FILTERING.sh
20171:FIX_RAG_FILTERING.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/services/FIX_RAG_FILTERING.sh
20172:FIX_RAG_FILTERING.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/services/FIX_RAG_FILTERING.sh
20523:FIX_MEMORY_STORAGE.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/services/FIX_MEMORY_STORAGE.sh
20524:FIX_MEMORY_STORAGE.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/services/FIX_MEMORY_STORAGE.sh
20525:FIX_MEMORY_STORAGE.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/FIX_MEMORY_STORAGE.sh
20526:FIX_MEMORY_STORAGE.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/FIX_MEMORY_STORAGE.sh
20527:FIX_MEMORY_STORAGE.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/services/FIX_MEMORY_STORAGE.sh
20528:FIX_MEMORY_STORAGE.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/FIX_MEMORY_STORAGE.sh
20529:FIX_MEMORY_STORAGE.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/FIX_MEMORY_STORAGE.sh
20530:FIX_MEMORY_STORAGE.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/services/FIX_MEMORY_STORAGE.sh
20531:FIX_MEMORY_STORAGE.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/FIX_MEMORY_STORAGE.sh
20532:FIX_MEMORY_STORAGE.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/services/FIX_MEMORY_STORAGE.sh
20533:FIX_MEMORY_STORAGE.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/services/FIX_MEMORY_STORAGE.sh
20534:FIX_MEMORY_STORAGE.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/FIX_MEMORY_STORAGE.sh
20535:FIX_MEMORY_STORAGE.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/services/FIX_MEMORY_STORAGE.sh
20536:FIX_MEMORY_STORAGE.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/FIX_MEMORY_STORAGE.sh
21335:LOAD_AAACPE_RAG.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/LOAD_AAACPE_RAG.sh
21336:LOAD_AAACPE_RAG.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/LOAD_AAACPE_RAG.sh
21337:LOAD_AAACPE_RAG.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/LOAD_AAACPE_RAG.sh
21338:LOAD_AAACPE_RAG.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/services/LOAD_AAACPE_RAG.sh
21339:LOAD_AAACPE_RAG.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/LOAD_AAACPE_RAG.sh
21340:LOAD_AAACPE_RAG.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/LOAD_AAACPE_RAG.sh
21341:LOAD_AAACPE_RAG.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/services/LOAD_AAACPE_RAG.sh
21342:LOAD_AAACPE_RAG.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/LOAD_AAACPE_RAG.sh
21343:LOAD_AAACPE_RAG.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/services/LOAD_AAACPE_RAG.sh
21344:LOAD_AAACPE_RAG.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/services/LOAD_AAACPE_RAG.sh
21345:LOAD_AAACPE_RAG.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/services/LOAD_AAACPE_RAG.sh
21346:LOAD_AAACPE_RAG.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/services/LOAD_AAACPE_RAG.sh
21347:LOAD_AAACPE_RAG.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/services/LOAD_AAACPE_RAG.sh
21348:LOAD_AAACPE_RAG.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/LOAD_AAACPE_RAG.sh
29819:ADD_RAG_METADATA_FILTERING.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/ADD_RAG_METADATA_FILTERING.sh
29820:ADD_RAG_METADATA_FILTERING.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/services/ADD_RAG_METADATA_FILTERING.sh
29821:ADD_RAG_METADATA_FILTERING.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/services/ADD_RAG_METADATA_FILTERING.sh
29822:ADD_RAG_METADATA_FILTERING.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/ADD_RAG_METADATA_FILTERING.sh
29823:ADD_RAG_METADATA_FILTERING.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/services/ADD_RAG_METADATA_FILTERING.sh
29824:ADD_RAG_METADATA_FILTERING.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/services/ADD_RAG_METADATA_FILTERING.sh
29825:ADD_RAG_METADATA_FILTERING.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/ADD_RAG_METADATA_FILTERING.sh
29826:ADD_RAG_METADATA_FILTERING.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/services/ADD_RAG_METADATA_FILTERING.sh
29827:ADD_RAG_METADATA_FILTERING.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/ADD_RAG_METADATA_FILTERING.sh
29828:ADD_RAG_METADATA_FILTERING.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/ADD_RAG_METADATA_FILTERING.sh
29829:ADD_RAG_METADATA_FILTERING.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/ADD_RAG_METADATA_FILTERING.sh
29830:ADD_RAG_METADATA_FILTERING.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/ADD_RAG_METADATA_FILTERING.sh
29831:ADD_RAG_METADATA_FILTERING.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/services/ADD_RAG_METADATA_FILTERING.sh
29832:ADD_RAG_METADATA_FILTERING.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/services/ADD_RAG_METADATA_FILTERING.sh

./services/nbb_darwin_godel_machines.py.pre_dynamic
50:    dgm_agent: str = "DGM_RAG_TUNER"

./services/swagger_gateway_FIXED.py
21:    services = {"brain": get_service_url("ai_alt"), "rag": "http://localhost:${RAG_SERVER_PORT}"}

./services/nbb_darwin_godel_machines.py.pre_debug
50:    dgm_agent: str = "DGM_RAG_TUNER"

./services/smart_auto_store.py
8:Checks RAG before storing to avoid duplicates
14:    """Store in RAG only if not duplicate"""

./services/main_brain_psychology_patch.py
37:    # Adjust the path if your FastAPI/RAG server uses a different route

./services/ai_server.py
74:            logger.info("✅ ChromaDB connected - RAG memory active")

./services/master_chat_orchestrator_v5_consciousness.py
15:- RAG → Consciousness → Multi-Model Consensus → Response
52:    "rag_server": "http://localhost:${RAG_SERVER_PORT}",
132:    3. RAG knowledge retrieval
191:    # LAYER 3: RAG Knowledge Retrieval 
192:    logger.info("📚 Layer 3: RAG knowledge retrieval...")
207:                    logger.info(f"   ✅ RAG context: {len(rag_context)} chars")
209:        logger.warning(f"   ⚠️  RAG retrieval failed: {e}")

./services/msjarvisunifiedgateway.py
163:    # GeoBIM / RAG Service (port 8051)

./services/process_statewide_gis_bulk.py
87:                'COVERAGE': 'Statewide WV',

./services/domain_service_router.py
35:            "rag.mountainshares.us": {"port": 4016, "name": "GPU RAG System"},

./services/add_fast_layer.py
22:            mem = requests.post("http://localhost:${RAG_SERVER_PORT}/search", json={"query": request.message, "user_id": request.user_id, "limit": 3}, timeout=2)

./services/add_fifth_dgm_to_chat.py
92:        print("  4. Automatically stores in subconscious (RAG)")

./services/ai_server_19llm_CONSCIOUS.backup_20251013_082519.py
292:            mem = requests.post("http://localhost:${RAG_SERVER_PORT}/search", json={
415:            requests.post("http://localhost:${RAG_SERVER_PORT}/store", json={

./services/dir_endpoints.txt
327:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP.py:405:@app.get("/rag/supervisor", tags=["RAG-Supervisor"])
537:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.backup_1762220815.py:139:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
551:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.backup_1762220815.py:207:@app.get("/rag-knowledge-stats", tags=["Whitebox"], summary="RAG & Knowledge Base Statistics")
714:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.py:102:@app.post("/rag-query", tags=["RAG"])
715:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.py:110:@app.get("/rag-status", tags=["RAG"])
758:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER.py:350:@app.get("/rag/supervisor", tags=["RAG-Supervisor"])
811:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:149:@app.post("/rag-query", tags=["RAG"])
812:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:158:@app.get("/rag-status", tags=["RAG"])
871:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.pre_manifest.backup.py:351:@app.get("/rag/supervisor", tags=["RAG-Supervisor"])
920:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:366:@app.get("/rag/supervisor", tags=["RAG-Supervisor"])
1099:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_BACKUP.py:139:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
1113:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_BACKUP.py:207:@app.get("/rag-knowledge-stats", tags=["transparency_mode"], summary="RAG & Knowledge Base Statistics")
1177:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.py.30endpoints_backup.py:149:@app.post("/rag-query", tags=["RAG"])
1178:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.py.30endpoints_backup.py:158:@app.get("/rag-status", tags=["RAG"])
1339:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FIXED.py:189:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
1353:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FIXED.py:257:@app.get("/rag-knowledge-stats", tags=["transparency_mode"], summary="RAG & Knowledge Base Statistics")
1465:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.backup.py:349:@app.get("/rag/supervisor", tags=["RAG-Supervisor"])
1603:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.backup_error.py:139:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
1617:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.backup_error.py:207:@app.get("/rag-knowledge-stats", tags=["Whitebox"], summary="RAG & Knowledge Base Statistics")
1654:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FINAL.py:139:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
1668:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FINAL.py:207:@app.get("/rag-knowledge-stats", tags=["transparency_mode"], summary="RAG & Knowledge Base Statistics")
1787:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:139:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
1801:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:207:@app.get("/rag-knowledge-stats", tags=["transparency_mode"], summary="RAG & Knowledge Base Statistics")

./services/add_conversation_context.py
20:                f"{RAG_URL}/conversations/{user_id}",

./services/DEPLOYMENT_ORDER.txt
4:✅ Port 8003: RAG Server

./services/ai_server_20llm_PRODUCTION.py.backup_bakllava_removal
57:        f"{len(rag_hits)} msjarvisgis RAG hits."
63:          "the WV local_resources_index database, and the msjarvisgis RAG layer.\n"
67:        + "RAG hits: " + str(rag_hits) + "\n"

./services/chromadb_rag_helper.py
8:    """Query ChromaDB RAG for consciousness context"""
22:            logger.info(f"📚 RAG retrieved {len(results)} context chunks")

./services/dgm_orchestrator.py
30:    _have = {col[1] for col in conn.execute("PRAGMA table_info(central_i_container)").fetchall()}

./services/conversation_memory_endpoints.py
8:Add these to your RAG server or run as separate microservice
21:# Connect to same ChromaDB as RAG

./services/enhance_rag_first.py
6:"""Enhance main.py to check RAG first, then web search, then store"""
11:# Add RAG-first logic before web search
13:        # === RAG-FIRST STRATEGY ===
14:        # 1. Check RAG for existing knowledge
24:                        # Found good match in RAG - use it!
25:                        logger.info(f"✅ RAG hit! Score: {rag_data['results'][0]['score']:.2f}")
28:            logger.debug(f"RAG check: {e}")
29:        # === END RAG-FIRST ===
42:    print("✅ Added RAG-first checking to main.py")

./services/patch_mother_persona.py
6:"""Add RAG retrieval to apply_mother_persona"""
12:# Find the apply_mother_persona function and inject RAG
24:    # Inject RAG retrieval right after the try: block starts
26:        # Insert RAG retrieval before emotion_context
28:        rag_code = f'''{indent}# Retrieve authentic Appalachian phrases from RAG
33:{indent}    logging.warning(f"RAG retrieval failed: {{e}}")
39:        # Add RAG code then re-add emotion_context
44:    # Now find the mother_prompt and inject RAG phrases
50:                # Inject RAG phrases before this line
62:print("✅ RAG retrieval injected into apply_mother_persona!")

./services/rag_command_module.py
1:"""RAG Command Module - Query knowledge base"""

./services/rag_general.py
36:app = FastAPI(title="RAG General Service", version="1.0.0")
54:        "description": "General-purpose RAG domain for non-temporal, non-geospatial queries.",
103:    Placeholder general RAG implementation.
111:        "answer_stub": "General RAG answer (stub).",

./services/jarvis-spiritual-rag_spiritual_rag_domain.py
3:SPIRITUAL RAG DOMAIN SERVICE
4:Specialized RAG for spiritual, biblical, and theological content
19:    title="Spiritual RAG Domain",
53:        "service": "Spiritual RAG Domain - FOUNDATIONAL LAYER",
116:    """Add document to spiritual RAG"""
131:    logger.info(f"✝️ Spiritual RAG Domain (FOUNDATIONAL LAYER) starting on port {port}")

./services/web_page_ingest.py
17:RAG_STORE_URL = os.getenv("RAG_STORE_URL", "http://127.0.0.1:8003/store")
34:    Fetch a web page, extract readable text, and store it into RAG.
81:    # 3) Store into RAG using the existing background_rag_store schema
101:            store_resp = await client.post(RAG_STORE_URL, json=payload)
103:        logger.error(f"Error calling RAG store: {repr(e)}")
106:            detail=f"Error storing to RAG: {repr(e)}",
110:        f"RAG store status={store_resp.status_code}, "
117:            detail=f"RAG store failed: {store_resp.text}",

./services/egeria_web_ui_dynamic.py
128:                    const info = `Mode: ${data.mode || 'fast'} | Time: ${data.time?.toFixed(2) || '?'}s | RAG: ${data.context_used ? 'Yes' : 'No'}`;

./services/master_chat_orchestrator_dynamic.py
42:    description="Dynamic port RAG-enhanced orchestration"
136:    # STEP 1: Get RAG context with service discovery
137:    logger.info("📚 Discovering RAG service...")
142:        logger.info(f"   Found RAG at {rag_url}")
158:        logger.warning(f"   ⚠️  RAG failed: {e}")

./services/METHOD_AUDIT_RAW.txt
486:/home/ms-jarvis/msjarvis-rebuild/services/gpu_accelerated_rag_fixed.py:47:class GPUAcceleratedRAGFixed:
490:/home/ms-jarvis/msjarvis-rebuild/services/gpu_accelerated_rag.py:41:class GPUAcceleratedRAG:
1409:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py:88:class RAGHelper:
2543:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_rag_bridge.py:40:class RAGQuery(BaseModel):
2544:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_rag_bridge.py:45:class UnifiedRAG:
2547:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_rag_bridge.py:211:async def query_rag(query_req: RAGQuery):
3068:/home/ms-jarvis/msjarvis-rebuild/services/rag_server.psychology_patched.py:72:class RAGServer:
3080:/home/ms-jarvis/msjarvis-rebuild/services/rag_server.py:72:class RAGServer:
3091:/home/ms-jarvis/msjarvis-rebuild/services/rag_workflow.py:16:class RAGWorkflow:

./services/fix_storage.py
11:    """Store conversation in RAG with correct schema"""
15:                f"{RAG_URL}/store_conversation",
33:    """Store conversation in RAG with correct schema"""
37:                f"{RAG_URL}/store_conversation",

./services/gpu_accelerated_rag.py
7:GPU-ACCELERATED RAG SYSTEM
8:High-performance RAG using RTX 4070 GPU for embeddings and search
36:    title="GPU-Accelerated RAG System",
41:class GPUAcceleratedRAG:
49:        logger.info(f"🎮 Initializing GPU-Accelerated RAG on {self.device}")
190:# Global GPU-accelerated RAG instance
191:gpu_rag = GPUAcceleratedRAG()
197:        "service": "GPU-Accelerated RAG System",
245:    logger.info(f"🚀 GPU-Accelerated RAG starting on port {port_service.port}")

./services/rag_5100_ensemble.py
8:app = FastAPI(title="RAG Consensus Ensemble", version="2.0")

./services/geobim_health_shim_8051.py
4:app = FastAPI(title="GeoBIM / RAG Health Shim")

./services/msjarvisunifiedswaggergatewayFIXED.py
57:RAG_URL = "http://jarvis-direct-rag:8199"                  # /direct_rag
166:    # Build retrieval context for RAG from Hilbert + Chroma
196:    # RAG via /direct_rag
204:                "user_profile": user_profile,  # identity context for RAG
207:        rr = requests.post(f"{RAG_URL}/direct_rag", json=rag_req, timeout=300)
211:            print("✅ RAG /direct_rag: OK", file=sys.stderr)
213:            rag_response = f"RAG error: {rr.status_code} {rr.text}"
215:        rag_response = f"RAG error: {e}"
216:        print(f"❌ RAG: {e}", file=sys.stderr)
238:        # 22-LLM itself already has RAG + multi-agent logic; this gateway focuses on routing.

./services/dgm_rag_integration.py
3:69-DGM RAG Integration Layer
18:class DGMRAGIntegration:
31:        print(f"DGM RAG Integration initialized with Chroma at: {self.chroma_base}")
333:def get_dgm_rag_integration() -> DGMRAGIntegration:
334:    """Get or create singleton DGM RAG integration instance."""
337:        _dgm_rag = DGMRAGIntegration()

./services/load_spiritual_library.py
6:"""Load comprehensive spiritual library into Ms. Jarvis RAG"""
13:print("📖 Loading spiritual library into RAG...")

./services/add_conversation_endpoint.py
6:"""Add conversation storage to existing RAG server"""
18:# === CONVERSATION STORAGE ===
94:# Restart RAG server
98:    print("🔄 Restarting RAG server...")
101:    print("✅ RAG server restarted")

./services/msjarvis_benefit_rag.py
4:class MsJarvisBenefitRAG:
165:    print("Initializing MsJarvisBenefitRAG")
168:    rag = MsJarvisBenefitRAG()

./services/manual_storage_patch.py
27:        indent + '# Schedule background RAG storage\n',

./services/msjarvisragserver_wvpatch.py
7:app = FastAPI(title="Ms. Jarvis RAG Server (WV)", version="1.0.0")
17:WV_RAG_PROFILES = {
36:    collections = WV_RAG_PROFILES.get(profile)
38:        raise HTTPException(status_code=400, detail=f"Unknown RAG profile {profile}")

./services/fix_multi_rag_chromadb.py
7:Fix Multi-RAG to use correct ChromaDB path
32:print("Restarting Multi-RAG service...")
41:print("✅ Multi-RAG restarted")

./services/mesh_coordinator_interface.py
163:    VALUES ('Facebook_API', 'Mesh_Internal', 'Through_Coordinator', 1, 'RAG→WOAH→DGM→Consciousness→Output')
170:    VALUES ('WebUI', 'Mesh_Internal', 'Through_Coordinator', 2, 'RAG→WOAH→DGM→Consciousness→Output')
244:    print("    GISGEODB↔ChromaDB↔RAG↔WOAH↔DGM")
254:    print("  4. Mesh processes (GISGEODB→RAG→Consciousness)")

./services/rag_server_main.py
2:Ms. Jarvis RAG Server - Unified Knowledge Retrieval
3:Port: 8003 (RAG Service)
30:    title="Ms. Jarvis RAG Server",
32:    description="Unified RAG service returning rich results_by_source for Ms. Jarvis ULTIMATE",
197:    logger.info(f"🔍 RAG /search query='{query[:80]}' top_k={request.top_k}")
200:    logger.debug(f"RAG where-clause: {where}")
217:            logger.warning(f"RAG query error for collection {collection_name}: {e}")
262:    logger.info(f"✅ RAG /search completed query='{query[:60]}' count={total_count}")
590:        "service": "Ms. Jarvis RAG Server",
592:        "description": "Unified RAG server for Ms. Jarvis ULTIMATE, exposing /search and /store",
606:    logger.info("🚀 Starting Ms. Jarvis RAG Server on port 8003")

./services/comprehensive_storage_fix.py
16:    storage_code = f'''{indent}# Store in RAG (background)
30:    lambda m: f'''{m.group(1)}# Store email action in RAG
33:{m.group(1)}    logger.info(f"📝 Email queued for RAG")
43:    lambda m: f'''{m.group(1)}# Store website deployment in RAG
46:{m.group(1)}    logger.info(f"📝 Website queued for RAG")
69:            new_lines.append(spaces + '# Background RAG storage')

./services/cleanup_manifest.txt
2:MS. EGERIA JARVIS - STORAGE CLEANUP MANIFEST

./services/email_rag_integration.py
6:"""Email → RAG Storage Integration"""
14:    """Store email conversation in RAG for future retrieval"""
40:            logger.info(f"📝 Stored {direction} email in RAG: {subject[:40]}...")
43:        logger.warning(f"RAG storage: {e}")
47:    """Search past email conversations in RAG"""

./services/psychological_rag_domain_psychological_rag_domain.py
10:PSYCHOLOGICAL RAG DOMAIN SERVICE
11:Specialized RAG for psychology, mental health, and therapeutic content
41:    title="Psychological RAG Domain",
43:    description="Specialized RAG for psychological and mental health knowledge"
77:        "service": "Psychological RAG Domain",
173:    Chroma-backed psychological RAG query.
199:    """Add document to psychological RAG"""
217:    logger.info(f"🧘 Psychological RAG Domain starting on port {port}")

./services/auto_rag_builder.py
6:"""Auto-build RAG every 5 minutes with compression"""
16:            logger.info(f"🔄 Building RAG...")
35:                logger.info(f"✅ RAG: {len(state)}→{len(compressed)} bytes ({ratio:.1%})")

./services/rag_simple.py
7:app = FastAPI(title="RAG Consensus Server", version="1.0")

./services/rag_5100_final.py
7:app = FastAPI(title="RAG Consensus", version="1.0")

./services/route_declarations_clean.txt
1202:get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB")
1216:get("/rag-knowledge-stats", tags=["Whitebox"], summary="RAG & Knowledge Base Statistics"
1243:get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB")
1257:get("/rag-knowledge-stats", tags=["Whitebox"], summary="RAG & Knowledge Base Statistics"
1399:get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB")
1413:get("/rag-knowledge-stats", tags=["transparency_mode"], summary="RAG & Knowledge Base Statistics"
1442:get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB")
1456:get("/rag-knowledge-stats", tags=["transparency_mode"], summary="RAG & Knowledge Base Statistics"
1483:get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB")
1497:get("/rag-knowledge-stats", tags=["transparency_mode"], summary="RAG & Knowledge Base Statistics"
1521:get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB")
1535:get("/rag-knowledge-stats", tags=["transparency_mode"], summary="RAG & Knowledge Base Statistics"

./services/add_conversation_storage.py
6:"""Add conversation storage endpoint to RAG server"""
8:# Read current RAG server
98:print("✅ Added conversation storage endpoints to RAG server")

./services/swagger_gateway.py
26:    "rag": {"url": "http://localhost:${RAG_SERVER_PORT}", "prefix": "/rag"},

./services/comprehensive_gisgeodb_audit.py
219:        logger.info("5️⃣  STORAGE DISTRIBUTION (185GB across datasets)")
249:        with open('data/STORAGE_DISTRIBUTION.csv', 'w', newline='') as f:
254:        logger.info(f"✅ Created STORAGE_DISTRIBUTION.csv")

./services/jarvis-woah_dgm_supervisor_woah_fixed.py
218:    """Sync conversational memory to RAG"""
225:    # Find RAG services
236:    # Simple memory sync to RAG
239:            # Test RAG connection

./services/create_consciousness_data_integration.py
32:  • RAG (Retrieval-Augmented Generation)
55:    # LAYER 1: RAG RETRIEVAL POOL (What to pull from knowledge)
56:    print("\n1️⃣  RAG RETRIEVAL INTERFACE")
68:    print("   ✓ RAG retrieval pool (pulls from GISGEODB + ChromaDB)")
185:    print("   ✓ GISGEODB → RAG → 5DGM")
197:        'RAG' as source,
219:        'RAG', 'Connected'
244:    print("EXTERNAL KNOWLEDGE → RAG POOL")
249:    print("RAG POOL → 5TH DARWIN GÖDEL MACHINE")

./services/RESTORATION_CERTIFICATE_CORRECTED.txt
47:✅ RAG Knowledge Server (Port 8003)

./services/multi_rag_dgm_system.py
3:MULTI-RAG DGM SYSTEM
4:Multiple RAG systems with Darwin-Gödel Machine integration
5:Specialized RAG instances for different knowledge domains
32:    title="Multi-RAG DGM System",
34:    description="Multiple specialized RAG systems with DGM integration",
44:# Specialized RAG configurations
45:RAG_DOMAINS: Dict[str, Dict[str, Any]] = {
87:        "service": "Multi-RAG DGM System",
92:        "rag_domains": len(RAG_DOMAINS),
101:    for domain, config in RAG_DOMAINS.items():
125:    """Route query to appropriate RAG domain(s) using DGM logic"""
137:        if domain in RAG_DOMAINS:
138:            config = RAG_DOMAINS[domain]
169:    if domain_hint and domain_hint in RAG_DOMAINS:
173:    for domain, config in RAG_DOMAINS.items():
217:            weight = RAG_DOMAINS[domain]["priority"]
266:    """Sync all conversational memories to appropriate RAG domains"""
267:    logger.info("🧠 Syncing all memories to Multi-RAG system...")
290:                if target_domain in RAG_DOMAINS:
291:                    port = RAG_DOMAINS[target_domain]["port"]
308:    """Process memory data for specific domain RAG"""
329:    """Sync documents to domain-specific RAG"""
355:    logger.info(f"🔀 Multi-RAG DGM System starting on port {port}")

./services/master_chat_orchestrator_v8_spiritual_complete.py
71:    "rag_server": "http://localhost:${RAG_SERVER_PORT}",
238:    10. RAG Knowledge Integration (including Vatican content)
399:    # (Psychology, Temporal, Maternal, RAG, etc. - same as v7)
423:    # Simplified RAG integration for this version
424:    logger.info("📚 Layer 11: RAG knowledge integration (including Vatican content)...")
439:                    logger.info(f"   ✅ Spiritual RAG knowledge: {len(rag_context)} chars")
441:        logger.warning(f"   ⚠️  Spiritual RAG integration failed: {e}")

./services/rag_server.psychology_patched.py
6:"""Ms. Jarvis RAG Server - Knowledge Base with Dynamic Port Scheduling"""
40:app = FastAPI(title="Ms. Jarvis RAG", version="1.0.0", docs_url="/docs", redoc_url="/redoc")
72:class RAGServer:
177:logger.info("🚀 Initializing RAG Server with Dynamic Port Scheduling...")
178:rag = RAGServer()
179:logger.info(f"✅ RAG Server Ready on port {rag.port}!")
185:        "service": "Ms. Jarvis RAG",
273:    logger.info(f"🚀 Starting RAG Server on dynamically allocated port {port_service.port}")

./services/web_connectivity_analyzer.py
31:            "Multi-RAG System": {"port": 4011, "endpoint": "/health", "type": "knowledge_interface"},
32:            "RAG Server": {"port": 8003, "endpoint": "/health", "type": "search_interface"},
34:            "GPU RAG Fixed": {"port": 4016, "endpoint": "/health", "type": "gpu_search_interface"}

./services/create_perpetual_storage_layer.py
7:PERPETUAL STORAGE ARCHITECTURE
22:    print("\n🗃️  Creating PERPETUAL STORAGE ARCHITECTURE")
25:    # TIER 1: HOT STORAGE (Active data, real-time access)
41:    # TIER 2: WARM STORAGE (Archive, occasional access)
58:    # TIER 3: COLD STORAGE (Historical, rarely accessed)
158:    print("✅ PERPETUAL STORAGE ARCHITECTURE CREATED")
161:    print("STORAGE GUARANTEE:")
168:    print("STORAGE TIERS:")

./services/dgm_rag_integration_v2.py
3:69-DGM RAG Integration Layer (Enhanced)
17:class DGMRAGIntegration:
23:        print(f"✓ DGM RAG Integration initialized: {self.chroma_base}")
224:        _dgm_rag = DGMRAGIntegration()

./services/comprehensive_gisgeodb_audit_FIXED.py
128:        logger.info("5️⃣  STORAGE DISTRIBUTION (185GB across datasets)")
155:        with open('data/STORAGE_DISTRIBUTION.csv', 'w', newline='') as f:
160:        logger.info(f"✅ Created STORAGE_DISTRIBUTION.csv")

./services/unified_consciousness_gateway_PRODUCTION.py
28:    RAG-powered unified chat handler.
45:        # Extract documents/content from RAG results
53:        # Augment incoming message with RAG context

./services/master_chat_orchestrator_v9_dgm_complete.py
21:- Multi-RAG domain specialization
91:            "🔀 Multi-RAG Domain Specialization",
118:    # Check Multi-RAG status

./services/performance_optimization_analyzer.py
29:            "Multi_RAG_DGM": {"url": "http://localhost:4011", "endpoint": "/health"},
30:            "RAG_Server": {"url": "http://localhost:${RAG_SERVER_PORT}", "endpoint": "/health"},
34:            "Spiritual_RAG": {"url": "http://localhost:4013", "endpoint": "/health"},
35:            "Psychological_RAG": {"url": "http://localhost:4014", "endpoint": "/health"},
438:                "Consider read replicas for RAG databases",

./services/ai_server_11llm_OPTIMIZED.py
190:    """Store in RAG as background task - doesn't block response"""
364:    # Phase 1.5: Querying RAG for context... (only if you later add rag_server)
365:    logger.info("Phase 1.5: Querying RAG for context...")
410:                # NOTE: placeholder; adjust when dedicated RAG HTTP front is live
412:                    "http://localhost:${RAG_SERVER_PORT}/query",
420:                        f"  ✅ RAG context retrieved: {len(rag_context)} chars"
423:            logger.warning(f"  ⚠️  RAG query failed: {e}")
425:    # Enhance message with RAG context
432:        logger.info("  ✅ Message enhanced with RAG context")
559:            # add "rag_server" here later if you bring up a dedicated RAG HTTP front
583:        # RAG Server - Knowledge Base Search (only if you add rag_server)
602:                            f"  ✅ RAG: Found {rag_data['count']} knowledge results"
605:                logger.debug(f"  ⚠️  RAG Server: {str(e)[:50]}")
712:            logger.info(f"  RAG returned {len(results)} results")
724:                            "    ✅ Extracted RAG content: "
817:    # Background RAG storage
960:                    logger.info("✅ Found similar deployment in RAG")
1163:            logger.info("📝 Email queued for RAG")
1190:            logger.info("📝 Website queued for RAG")
1221:    """Generate contextual insights from RAG results"""

./services/aaacpe_rag_service.py
2:"""AaaCPE RAG Service - Appalachian Cultural Intelligence"""

./services/rag_grounded_v2.py
2:rag_grounded_v2 — Truth Verification via RAG + DGM Layer
19:RAG_SERVER_URL = os.getenv("RAG_SERVER_URL",   "http://jarvis-rag-server:8000")
22:    title="rag_grounded_v2 — RAG Truth Verification",
23:    description="OI-23 closure. Grounded truth verification via RAG + DGM. Chapter 33 §33.10.",
66:        # Step 1 — Query RAG server for grounding evidence
68:            r = await client.post(f"{RAG_SERVER_URL}/query",
76:            logger.warning(f"RAG server unavailable: {e}")

./services/mountainshares_chain_monitor.py
15:# Contract details from RAG knowledge

./services/registration_biometric_production_final.py
15:BIOMETRIC_STORAGE = "/tmp/biometric_images"
16:os.makedirs(BIOMETRIC_STORAGE, exist_ok=True)
681:    image_path = f"{BIOMETRIC_STORAGE}/{ueid}_{image_hash[:8]}.jpg"

./services/main.py
181:    """Store in RAG as background task - doesn't block response"""
219:    """Remove RAG metadata from responses"""
450:    logger.info("Phase 1.5: Querying RAG and Web for context...")
465:            logger.info(f"  ✅ RAG context length: {len(rag_context)}")
494:        logger.info("  ✅ Message enhanced with fused RAG + Web context")
546:        logger.info(f"📝 Queued for RAG storage: {message[:40]}...")

./services/ultimate_web_orchestrator.py
9:Darwin-Gödel Machine + WOAH integrated with RAG and Ms. Egeria Jarvis
98:            "multi_rag": {"port": 4011, "name": "Multi-RAG System"},
99:            "rag_server": {"port": 8003, "name": "RAG Server"},
101:            "gpu_rag": {"port": 4016, "name": "GPU RAG"},
120:        """Query RAG system with DGM optimization"""
124:        # Try GPU-accelerated RAG first
139:                logger.warning(f"GPU RAG failed: {e}")
141:        # Fallback to multi-RAG system
156:                logger.warning(f"Multi-RAG failed: {e}")
179:        # Get RAG context
353:                <h4>RAG Queries</h4>
548:    logger.info("   🎮 GPU + RAG: Optimized")

./services/response_sanitizer.py
22:    r"ChromaDB RAG.*",
44:    test = "lineage_pattern/Edward I via heritage_source_ref (ChromaDB RAG Import)"

./services/port_9000_69dgm_bridge.py.backup_20260307_072741
15:# Import RAG integration
32:# Initialize RAG integration
33:print("Initializing 69-DGM RAG Integration...")
35:print("✓ RAG Integration ready")
269:        "service": "69-DGM Bridge (RAG-Integrated)",
323:Version: 2.0.0 (RAG-Integrated)

./services/rag_server.py
3:"""Ms. Jarvis RAG Server - Knowledge Base with Dynamic Port Scheduling + Rich results_by_source
8:- Designed to be called by Ms. Jarvis ULTIMATE as the RAG backend.
38:# Lock internal RAG port to 8003 (docker-compose maps host 8003 -> container 8003)
39:RAG_INTERNAL_PORT = int(os.getenv("RAG_PORT", "8003"))
40:port_service.register_service(RAG_INTERNAL_PORT)
45:    title="Ms. Jarvis RAG",
104:# RAG Server class (Chroma, embeddings, knowledge)
106:class RAGServer:
108:        logger.info("🧠 Initializing RAGServer...")
167:        # Expose main KBs to RAG search (tolerate missing optional collections)
253:        Rich RAG search used by main brain:
280:                    f"RAG rich_search error for collection {collection_name}: {e}"
354:logger.info("🚀 Initializing RAG Server with Dynamic Port Scheduling...")
355:rag = RAGServer()
356:logger.info(f"✅ RAG Server Ready on port {rag.port}!")
366:        "service": "Ms. Jarvis RAG",
509:        f"🚀 Starting RAG Server on dynamically allocated port {port_service.port}"

./services/create_tile_index.py
97:                'COVERAGE_NOTE': 'Estimated coverage - grid-based approximation'

./services/extract_all_chromadb_to_gis.py
24:    logger.info("📚 EXTRACTING ALL DATA FROM CHROMADB PERSISTENT STORAGE")

./services/gpu_accelerated_rag_fixed.py
7:GPU-ACCELERATED RAG SYSTEM - FIXED VERSION
8:High-performance RAG using RTX 4070 GPU with ChromaDB
42:    title="GPU-Accelerated RAG System - Fixed",
47:class GPUAcceleratedRAGFixed:
56:        logger.info(f"🎮 Initializing GPU RAG Fixed on {self.device}")
259:gpu_rag_fixed = GPUAcceleratedRAGFixed()
274:        "service": "GPU-Accelerated RAG System - Fixed",
331:    logger.info(f"🚀 GPU-Accelerated RAG Fixed starting on port {port}")

./services/add_web_research_storage.py
6:"""Add automatic RAG storage to web research"""
13:        # Auto-store web research results in RAG
34:                    logger.info(f"📝 Stored web research in RAG: {query[:50]}")

./services/rest_endpoints.txt
81:./ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP.py:405:@app.get("/rag/supervisor", tags=["RAG-Supervisor"])
448:./ms_jarvis_main_gateway.backup_1762220815.py:139:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
462:./ms_jarvis_main_gateway.backup_1762220815.py:207:@app.get("/rag-knowledge-stats", tags=["Whitebox"], summary="RAG & Knowledge Base Statistics")
625:./ms_jarvis_main_gateway.py:102:@app.post("/rag-query", tags=["RAG"])
626:./ms_jarvis_main_gateway.py:110:@app.get("/rag-status", tags=["RAG"])
669:./ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER.py:350:@app.get("/rag/supervisor", tags=["RAG-Supervisor"])
722:./ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:149:@app.post("/rag-query", tags=["RAG"])
723:./ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:158:@app.get("/rag-status", tags=["RAG"])
805:./ms_jarvis_unified_gateway_v4.3.pre_manifest.backup.py:351:@app.get("/rag/supervisor", tags=["RAG-Supervisor"])
854:./ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:366:@app.get("/rag/supervisor", tags=["RAG-Supervisor"])
1058:./ms_jarvis_unified_swagger_gateway_BACKUP.py:139:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
1072:./ms_jarvis_unified_swagger_gateway_BACKUP.py:207:@app.get("/rag-knowledge-stats", tags=["transparency_mode"], summary="RAG & Knowledge Base Statistics")
1136:./ms_jarvis_main_gateway.py.30endpoints_backup.py:149:@app.post("/rag-query", tags=["RAG"])
1137:./ms_jarvis_main_gateway.py.30endpoints_backup.py:158:@app.get("/rag-status", tags=["RAG"])
1420:./ms_jarvis_unified_swagger_gateway_FIXED.py:189:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
1434:./ms_jarvis_unified_swagger_gateway_FIXED.py:257:@app.get("/rag-knowledge-stats", tags=["transparency_mode"], summary="RAG & Knowledge Base Statistics")
1546:./ms_jarvis_unified_gateway_v4.3.backup.py:349:@app.get("/rag/supervisor", tags=["RAG-Supervisor"])
1684:./ms_jarvis_main_gateway.backup_error.py:139:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
1698:./ms_jarvis_main_gateway.backup_error.py:207:@app.get("/rag-knowledge-stats", tags=["Whitebox"], summary="RAG & Knowledge Base Statistics")
1735:./ms_jarvis_unified_swagger_gateway_FINAL.py:139:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
1749:./ms_jarvis_unified_swagger_gateway_FINAL.py:207:@app.get("/rag-knowledge-stats", tags=["transparency_mode"], summary="RAG & Knowledge Base Statistics")
1868:./ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:139:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
1882:./ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:207:@app.get("/rag-knowledge-stats", tags=["transparency_mode"], summary="RAG & Knowledge Base Statistics")

./services/rag_client.py
3:Ms. Jarvis RAG client for Fifth DGM and other services.
6:GIS RAG ("msjarvisgis") via the Chroma v2 HTTP API.
15:CHROMA_URL = os.getenv("GIS_RAG_CHROMA_URL", "http://jarvis-chroma:8002")
17:GIS_COLLECTION = os.getenv("GIS_RAG_COLLECTION", "msjarvisgis")

./services/ai_server_20llm_FINAL.py
28:        f"{len(rag_hits)} msjarvisgis RAG hits."
34:          "the WV local_resources_index database, and the msjarvisgis RAG layer.\n"
38:        + "RAG hits: " + str(rag_hits) + "\n"

./services/aaacpe_scraper/aaacpe_scraper_service.py
3:AaaCPE Web Scraper - Feeds Current Appalachian Content into RAG

./services/dgm_supervisor_woah.psychology_patched.py
287:    """Sync all conversational memory to RAG systems"""
292:    logger.info("🧠 Synchronizing conversational memory to RAG...")
294:    # Find all RAG services
299:        # Default to main RAG
319:                # Process memory data for RAG ingestion
322:                # Send to RAG services
342:    """Process memory data into RAG-compatible documents"""
385:    """Sync memory documents to a RAG service"""

./services/update_gisgeodb_schema.py
24:        c.execute("PRAGMA table_info(geographic_knowledge);")
48:        c.execute("PRAGMA table_info(geographic_knowledge);")

./services/nbb_darwin_godel_machines.py.pre_mapping
50:    dgm_agent: str = "DGM_RAG_TUNER"

./services/phase7_integration.py
64:    "rag_server": "http://localhost:${RAG_SERVER_PORT}",
186:            "core_infrastructure": 3,  # RAG, LLM, Consensus
202:    7. RAG Knowledge Integration
363:    # LAYER 7: RAG Knowledge Integration
364:    logger.info("📚 Layer 7: RAG knowledge integration...")
379:                    logger.info(f"   ✅ RAG knowledge: {len(rag_context)} chars")
381:        logger.warning(f"   ⚠️  RAG integration failed: {e}")

./services/msjarvis_gateway_with_judge_filtering.py
58:        # RAG

./services/jarvis-gis-rag_gis_rag_service.py
2:GIS RAG Service for Ms. Jarvis
16:GIS_RAG_URL = os.getenv("GIS_RAG_CHROMA_URL", "http://jarvis-chroma:8000").rstrip("/")
18:GIS_COLLECTION = os.getenv("GIS_RAG_COLLECTION", "geospatialfeatures")
28:app = FastAPI(title="Ms. Jarvis GIS RAG", version="0.3.0")
31:class GISRAGRequest(BaseModel):
38:class GISRAGHit(BaseModel):
47:class GISRAGResponse(BaseModel):
48:    hits: List[GISRAGHit]
66:        f"{GIS_RAG_URL}/api/v2/tenants/{CHROMA_TENANT}"
132:@app.post("/gis_rag", response_model=GISRAGResponse)
133:async def gis_rag(req: GISRAGRequest):
153:                f"{GIS_RAG_URL}/api/v2/tenants/{CHROMA_TENANT}"
179:            detail=f"Error calling GIS RAG backend: {repr(e)[:300]}",
182:    hits: List[GISRAGHit] = []
188:        return GISRAGResponse(hits=[])
195:        hit = GISRAGHit(
205:    return GISRAGResponse(hits=hits)
208:@app.post("/search", response_model=GISRAGResponse)
209:async def search_endpoint(req: GISRAGRequest = Body(...)):
211:    Alias so jarvis-main-brain can POST /search and get GIS RAG results.

./services/email_auto_checker.py
6:"""Auto-check emails and store in RAG"""
16:RAG_SERVICE = "http://jarvis-rag-server:8003"
20:    """Check emails, respond, and store in RAG"""
30:                        logger.info(f"📧 Stored {data['stored_in_rag']} emails in RAG")

./services/port_9000_69dgm_bridge.py.backup_20260307_072757
15:# Import RAG integration
32:# Initialize RAG integration
33:print("Initializing 69-DGM RAG Integration...")
35:print("✓ RAG Integration ready")
269:        "service": "69-DGM Bridge (RAG-Integrated)",
323:Version: 2.0.0 (RAG-Integrated)

./services/complete_system_audit.py
73:        return "Multi_RAG_DGM"
107:        return "RAG_Server"
143:    """Get Multi-RAG domain status"""
150:            return {"error": "Multi-RAG not responding"}
214:        if service_name in ["Ms_Egeria_Jarvis_v9", "DGM_Supervisor_WOAH", "Multi_RAG_DGM"]:
224:        elif service_name in ["RAG_Server", "LLM_Bridge", "Consensus_Service"]:
262:    # 3. Multi-RAG Domain Status
263:    print(f"\n🔀 MULTI-RAG DOMAIN STATUS:")
273:        print(f"   📚 Active RAGs: {dgm_status_info.get('active_rags', 0)}")
277:        print(f"   ❌ Multi-RAG Error: {rag_status['error']}")
294:        ("Multi-RAG Domain Specialization", "✅ 4 specialized knowledge domains"),
307:        ("Complete Knowledge Integration", "✅ RAG + scraped content")

./services/rag_temporal.py
32:# RAG server configuration (unified RAG on rag-server:8003)
34:RAG_SERVER_HOST = os.getenv("RAG_SERVER_HOST", "rag-server")
35:RAG_SERVER_PORT = int(os.getenv("RAG_SERVER_PORT", "8003"))
36:RAG_SEARCH_URL = f"http://{RAG_SERVER_HOST}:{RAG_SERVER_PORT}/search"
45:app = FastAPI(title="RAG Temporal Service", version="1.0.0")
66:        "description": "Temporal RAG domain for time-aware queries.",
156:    Temporal RAG implementation.
157:    Proxies to unified RAG /search and applies temporal-aware post-processing.
166:    # Base search body for unified RAG server
169:    # Do NOT set a default collection; rely on unified RAG multi-collection search.
179:    logger.info(f"[{SERVICE_NAME}] → RAG /search query='{query[:80]}' body={search_body}")
183:            resp = await client.post(RAG_SEARCH_URL, json=search_body)
187:        logger.error(f"[{SERVICE_NAME}] Error calling RAG server at {RAG_SEARCH_URL}: {e}")
188:        raise HTTPException(status_code=502, detail=f"Error calling RAG server: {e}")

./services/ai_server_original_backup.py
6:"""Ms. Jarvis - Multi-Agent AI with RAG Knowledge Integration"""
52:        logger.info(f"🧠 Ms. Jarvis initializing with RAG integration")
95:                response = await client.get("http://localhost:${RAG_SERVER_PORT}/health")
105:        """Search RAG knowledge base"""
115:                    "http://localhost:${RAG_SERVER_PORT}/search",
120:                    logger.info(f"📚 RAG found {len(results)} knowledge chunks")
123:            logger.error(f"RAG search error: {e}")
133:            # Add RAG knowledge
137:                logger.info("✅ RAG knowledge added to context")
147:            # Add RAG knowledge to prompt if available
170:        logger.info("🤖 Running 4 agents with RAG knowledge...")
235:logger.info("🚀 Starting Ms. Jarvis with RAG...")

./services/ai_server_20llm_PRODUCTION.py.backup_response_length
57:        f"{len(rag_hits)} msjarvisgis RAG hits."
63:          "the WV local_resources_index database, and the msjarvisgis RAG layer.\n"
67:        + "RAG hits: " + str(rag_hits) + "\n"

./services/fix_background_storage.py
27:    # Store in RAG (background task - doesn't block response)
34:    logger.info(f"📝 Queued for RAG storage: {request.message[:50]}...")

./services/load_rag_data.py
7:Load RAG data into ChromaDB for Mamma Kidd
83:print("\n🎊 RAG DATABASE READY FOR MAMMA KIDD! 🎊")

./services/rag_5100_ensemble_fast.py
24:app = FastAPI(title="RAG Consensus Ensemble", version="2.0")

./services/rag_to_gis_sync.py
7:RAG Knowledge Base → GIS Spatial Index Sync
8:Load all RAG knowledge and map to GIS/spatial storage

./services/ai_server_20llm_PRODUCTION.py.backup_synthesis
57:        f"{len(rag_hits)} msjarvisgis RAG hits."
63:          "the WV local_resources_index database, and the msjarvisgis RAG layer.\n"
67:        + "RAG hits: " + str(rag_hits) + "\n"

./services/rag_direct_debug.py
40:app = FastAPI(title="RAG Direct Debug", version="1.0")
46:    and return a compact text snippet suitable for RAG context.
71:        # If anything fails, RAG still works with its normal context.
105:    print("RAG_DIRECT_DEBUG context to jarvis_llm1:", context, flush=True)

./services/ai_server_20llm_PRODUCTION.py.backup_before_full_synthesis
57:        f"{len(rag_hits)} msjarvisgis RAG hits."
63:          "the WV local_resources_index database, and the msjarvisgis RAG layer.\n"
67:        + "RAG hits: " + str(rag_hits) + "\n"

./services/add_auto_store.py
6:"""Add automatic RAG storage after processing"""
24:        storage_block = f'''{indent}# Auto-store in RAG for future queries

./services/add_swagger_to_rag.py
1:# Update RAG server with Swagger documentation
16:    print("   ✅ Swagger already configured in RAG server")
21:    title="Ms. Jarvis RAG Server",
33:        print("   ✅ Swagger UI added to RAG server")
34:        print("   📖 Access at: http://localhost:${RAG_SERVER_PORT}/docs")

./services/gisgeodbdirectaccess.py
24:    """Check DB integrity with PRAGMA."""
27:            result = conn.execute('PRAGMA integrity_check;').fetchone()[0]

./services/parse_world_files.py
121:                    'COVERAGE_WIDTH_FEET': 2500,  # Estimate
122:                    'COVERAGE_HEIGHT_FEET': 2500,

./services/master_chat_orchestrator.py
20:RAG → [LLM Bridge OR Multi-Model Consensus] → Response
30:    description="RAG-enhanced with fast/consensus modes"
106:    # STEP 1: Get RAG context
107:    logger.info("📚 Querying RAG...")
125:        logger.warning(f"   ⚠️  RAG failed: {e}")

./services/create_consciousness_data_integration.psychology_patched.py
32:  • RAG (Retrieval-Augmented Generation)
55:    # LAYER 1: RAG RETRIEVAL POOL (What to pull from knowledge)
56:    print("\n1️⃣  RAG RETRIEVAL INTERFACE")
68:    print("   ✓ RAG retrieval pool (pulls from GISGEODB + ChromaDB)")
185:    print("   ✓ GISGEODB → RAG → 5DGM")
197:        'RAG' as source,
219:        'RAG', 'Connected'
244:    print("EXTERNAL KNOWLEDGE → RAG POOL")
249:    print("RAG POOL → 5TH DARWIN GÖDEL MACHINE")

./services/ingest_gis_features_to_chromadb.py
7:CHROMA_URL = os.getenv("GIS_RAG_CHROMA_URL", "http://localhost:8002").rstrip("/")
10:COLLECTION_NAME = os.getenv("GIS_RAG_COLLECTION", "geospatialfeatures")
12:EMBED_URL = os.getenv("GIS_RAG_EMBED_URL", "http://jarvis-ollama:11434")  # adjust if needed

./services/rag_server_min.py
21:MIN_RAG_PORT = int(os.getenv("MIN_RAG_PORT", "8103"))
40:class RAGServer:
42:        logger.info("🚀 RAGServer(minimal).__init__ starting")
46:        logger.info("🚀 RAGServer(minimal).__init__ complete")
73:        logger.info("🔍 MIN RAG search: %r, top_k=%d", query, top_k)
99:            logger.info("✅ MIN RAG search returning %d results", len(chunks))
102:            logger.error("MIN RAG search error: %s", e, exc_info=True)
107:        logger.info("📝 MIN RAG store called for user_id=%s", user_id)
117:            logger.info("✅ MIN RAG stored %d chars", len(text))
120:            logger.error("MIN RAG store error: %s", e, exc_info=True)
124:rag_min = RAGServer()
125:app = FastAPI(title="Ms. Jarvis RAG (Minimal)", version="1.0.0")
150:    return {"status": "healthy", "port": MIN_RAG_PORT}
185:    uvicorn.run(app, host="0.0.0.0", port=MIN_RAG_PORT, log_level="debug")

./services/master_chat_orchestrator_v9_optimized.py
75:    "rag_server": "http://localhost:${RAG_SERVER_PORT}",

./services/rag_first_workflow.py
7:RAG-First Workflow Enhancement
8:Checks RAG before web search, stores results after
17:    """Check RAG before doing web search"""
30:                        logger.info(f"✅ RAG cache hit! Score: {best_match['score']:.2f}")
33:        logger.debug(f"RAG check: {e}")
38:    """Store query/response in RAG for future use"""
55:            logger.info(f"📝 Stored in RAG: {query[:50]}...")
58:        logger.warning(f"RAG storage failed: {e}")

./services/multi_model_consensus.py
12:1. RAG provides context
218:    Flow: RAG context → 4 experts → judge → persona → response

./services/master_chat_orchestrator_v6_biologics.py
52:    "rag_server": "http://localhost:${RAG_SERVER_PORT}",
151:    4. RAG knowledge retrieval
240:    # LAYER 4-7: Continue with consciousness processing (temporal, maternal, RAG, etc.)
280:    # RAG Knowledge
281:    logger.info("📚 Layer 6: RAG knowledge retrieval...")
296:                    logger.info(f"   ✅ RAG context: {len(rag_context)} chars")
298:        logger.warning(f"   ⚠️  RAG retrieval failed: {e}")

./services/PORTS_REGISTRY_RAW.txt
499:/home/ms-jarvis/msjarvis-rebuild/services/multi_rag_dgm_system.py:                    port = RAG_DOMAINS[target_domain]["port"]

./services/main_brain_legacy_backup.py
178:    """Store in RAG as background task - doesn't block response"""
216:    """Remove RAG metadata from responses"""
433:    # Phase 1.5: RAG + Web context
434:    logger.info("Phase 1.5: Querying RAG and Web for context...")
449:            logger.info(f"  ✅ RAG context length: {len(rag_context)}")
478:        logger.info("  ✅ Message enhanced with fused RAG + Web context")
535:        logger.info(f"📝 Queued for RAG storage: {message[:40]}...")

./services/dgm_supervisor_woah.py
277:    """Sync all conversational memory to RAG systems"""
282:    logger.info("🧠 Synchronizing conversational memory to RAG...")
284:    # Find all RAG services
289:        # Default to main RAG
309:                # Process memory data for RAG ingestion
312:                # Send to RAG services
332:    """Process memory data into RAG-compatible documents"""
375:    """Sync memory documents to a RAG service"""

./services/clean_service_candidates.txt
179:./LOAD_AAACPE_RAG.sh
379:./ADD_RAG_RETRIEVAL_8050.sh

./services/ai_server_22llm.py
203:                f"✅ ChromaDB connected on {chroma_host}:{chroma_port} - RAG memory active"
381:                logger.warning(f"RAG query failed: {e}")

./services/rag_geospatial.py
32:# RAG server configuration (unified RAG on rag-server:8003)
34:RAG_SERVER_HOST = os.getenv("RAG_SERVER_HOST", "rag-server")
35:RAG_SERVER_PORT = int(os.getenv("RAG_SERVER_PORT", "8003"))
36:RAG_SEARCH_URL = f"http://{RAG_SERVER_HOST}:{RAG_SERVER_PORT}/search"
45:app = FastAPI(title="RAG Geospatial Service", version="1.0.0")
68:        "description": "Geospatial / GBIM / MountainShares RAG domain.",
129:    Geospatial / GBIM / MountainShares RAG implementation.
130:    Proxies to unified RAG /search and applies optional regional filters and distance ranking.
151:    logger.info(f"[{SERVICE_NAME}] → RAG /search query='{query[:80]}' body={search_body}")
155:            resp = await client.post(RAG_SEARCH_URL, json=search_body)
159:        logger.error(f"[{SERVICE_NAME}] Error calling RAG server at {RAG_SEARCH_URL}: {e}")
160:        raise HTTPException(status_code=502, detail=f"Error calling RAG server: {e}")

./services/master_chat_orchestrator_v7_complete.py
64:    "rag_server": "http://localhost:${RAG_SERVER_PORT}",
186:            "core_infrastructure": 3,  # RAG, LLM, Consensus
202:    7. RAG Knowledge Integration
363:    # LAYER 7: RAG Knowledge Integration
364:    logger.info("📚 Layer 7: RAG knowledge integration...")
379:                    logger.info(f"   ✅ RAG knowledge: {len(rag_context)} chars")
381:        logger.warning(f"   ⚠️  RAG integration failed: {e}")

./services/ultimate_chat_current.txt
72:                    logger.info(f"  ✅ RAG context retrieved: {len(rag_context)} chars")
74:            logger.warning(f"  ⚠️  RAG query failed: {e}")
79:        logger.info("  ✅ Message enhanced with RAG context")
219:                        logger.info(f"  ✅ RAG: Found {rag_data['count']} knowledge results")
221:                logger.debug(f"  ⚠️  RAG Server: {str(e)[:50]}")
322:            logger.info(f"  RAG returned {len(results)} results")
333:                        logger.info(f"    ✅ Extracted RAG content: {content_text[:50]}...")

./services/geo_rag_debug_app.py
5:app = FastAPI(title="Geo RAG Debug", version="1.0.0")

./services/nbb_darwin_godel_machines.py.backup_20260307_1121
50:    dgm_agent: str = "DGM_RAG_TUNER"

./services/roche_llm.py
218:                f"✅ ChromaDB connected on {chroma_host}:{chroma_port} - RAG memory active"
410:                logger.warning(f"RAG query failed: {e}")

./services/chromadb_v2_to_gis_sync.py
9:Everything in ChromaDB/RAG syncs to GIS with spatial indexing
74:                        "source": "ChromaDB_V2_RAG",

./services/unifiedconsciousnessgatewayPRODUCTION.py
28:            message_with_rag = f'{message}\n\nRAG Context (H4H 1002 Cosine <0.8 UUID {collection.id}): {rag_context}\n\nAnalysis: Biblical Empire Theology 80% Acts 9 heritage_source_ref Edward I Strong WV H4H'
29:            print(f'RAG Injected: {len(rag_hits)} Hits Avg {avg_dist:.2f} < {threshold} (Cosine 8001)')
44:        print(f'Chroma Error: {chroma_ex} (Fallback No RAG)')
52:    print("Final RAG Context Message:", with_rag)

./services/cloudflare_domain_integration.py
117:            "rag": 4016,           # GPU RAG system

./services/jarvis-aaacpe-rag_aaacpe_rag_service.py
2:"""AaaCPE RAG Service - Appalachian Cultural Intelligence"""

./services/ai_server_20llm_PRODUCTION.py.backup_presedfix
57:        f"{len(rag_hits)} msjarvisgis RAG hits."
63:          "the WV local_resources_index database, and the msjarvisgis RAG layer.\n"
67:        + "RAG hits: " + str(rag_hits) + "\n"

./services/main_brain.py
86:    Remove RAG multi-agent metadata from responses while preserving text.
307:        # UPDATED: GIS RAG now uses /gis_rag instead of /search
771:    Build SPIRITUAL RAG context FIRST - foundational knowledge layer.
772:    This is queried before general RAG to ground all responses in spiritual wisdom.
819:    Build RAG context from jarvis-gis-rag if available.
895:    Store in RAG as background task - doesn't block response.
901:        # 1) Legacy RAG server write with duplicate check
1294:    Fast, low-latency chat path. Skips RAG and web-research. Calls 20-LLM with a tight timeout.

./services/RESTORATION_CERTIFICATE.txt
32:✅ RAG Knowledge Server (Port 8003)

./services/msjarvisconsciousnessbridge.py
22:    description="Bridges unified gateway to 22-LLM + RAG stack (Docker URLs)",
61:            # Direct RAG
69:                state["rag_consensus"] = f"RAG error: {e}"

./services/bridge_69dgm.py
6:# Use Chroma directly - RAG server search is broken
10:app = FastAPI(title="69-DGM Bridge (Chroma RAG)")

./services/nbb_darwin_godel_machines.py
50:    dgm_agent: str = "DGM_RAG_TUNER"

./services/master_chat_orchestrator_v9_gpu_optimized.py
175:            # Use GPU-accelerated RAG (will be started automatically)
176:            logger.info("⚡ Using GPU-accelerated RAG search...")
178:                "http://localhost:4015/search",  # GPU RAG service
187:            logger.warning(f"   ⚠️ GPU RAG failed: {e}")

./services/msjarvisragserverwvpatch.py
8:class RAGQuery(BaseModel):
61:def rag_query(payload: RAGQuery):

./services/manifest_endpoints.py
31:                {"name": "ChromaDB", "port": 8001, "type": "Docker", "purpose": "Vector RAG storage", "status": "RUNNING"},
82:            "consciousness": "Ollama qwen2.5:14b + Constitutional RAG",

./services/jarvis_llm1.py
110:        "You are Ms. Jarvis, a mesh-native assistant operating over a GBIM + RAG stack.\n"

./services/PORT_AUDIT_RAW.txt
807:/home/ms-jarvis/msjarvis-rebuild/services/multi_rag_dgm_system.py:306:                    port = RAG_DOMAINS[target_domain]["port"]

./services/gis_rag_service.py
2:GIS RAG Service for Ms. Jarvis
15:GIS_RAG_URL = os.getenv("GIS_RAG_CHROMA_URL", "http://jarvis-chroma:8000").rstrip("/")
16:GIS_COLLECTION = os.getenv("GIS_RAG_COLLECTION", "geospatialfeatures")
24:app = FastAPI(title="Ms. Jarvis GIS RAG", version="0.3.2")
27:class GISRAGRequest(BaseModel):
34:class GISRAGHit(BaseModel):
43:class GISRAGResponse(BaseModel):
44:    hits: List[GISRAGHit]
54:        f"{GIS_RAG_URL}/api/v2/tenants/{CHROMA_TENANT}"
114:@app.post("/gis_rag", response_model=GISRAGResponse)
115:async def gis_rag(req: GISRAGRequest):
126:                f"{GIS_RAG_URL}/api/v2/tenants/{CHROMA_TENANT}"
152:            detail=f"Error calling GIS RAG backend: {repr(e)[:300]}",
155:    hits: List[GISRAGHit] = []
161:        return GISRAGResponse(hits=[])
169:            GISRAGHit(
179:    return GISRAGResponse(hits=hits)
182:@app.post("/search", response_model=GISRAGResponse)
183:async def search_endpoint(req: GISRAGRequest = Body(...)):

./services/working_full_pipeline_WITH_SPATIAL_TEMPORAL.py
53:    # STEP 1: RAG

./services/optimized_timeouts.py
5:OPTIMIZED_TIMEOUTS = {'Ms. Egeria Jarvis v9': {'current_avg': 5.0, 'recommended_timeout': 10}, 'DGM Supervisor': {'current_avg': 5.0, 'recommended_timeout': 10}, 'Multi-RAG DGM': {'current_avg': 5.0, 'recommended_timeout': 10}, 'RAG Server': {'current_avg': 5.0, 'recommended_timeout': 10}, 'Spiritual Services': {'current_avg': 5.0, 'recommended_timeout': 10}}
11:RAG_SEARCH_TIMEOUT = 8.0  # RAG search operations

./services/port_9000_69dgm_bridge.py.backup_20260307_070432
14:# Import RAG integration
24:# Initialize RAG integration
25:print("Initializing 69-DGM RAG Integration...")
27:print("✓ RAG Integration ready")
222:        "service": "69-DGM Bridge (RAG-Integrated)",
276:Version: 2.0.0 (RAG-Integrated)

./services/ai_server_22llm.psychology_patched.py
97:            logger.info("✅ ChromaDB connected - RAG memory active")
215:        # Get personality guidance from RAG
226:                logger.warning(f"RAG query failed: {e}")

./services/vatican_scraper_service.py
9:Feeds theological content into RAG for spiritual guidance integration
90:RAG_SERVER_URL = "http://localhost:${RAG_SERVER_PORT}"
188:    """Add theological content to RAG with spiritual categorization"""
195:                f"{RAG_SERVER_URL}/add_document",
214:            logger.error(f"Error adding theological content to RAG: {e}")

./services/gateway_wv_entanglement.py
6:GIS_RAG_API_URL = "http://localhost:8053/gisragquery"
82:        GIS_RAG_API_URL,
129:    Heuristic: derive domain tags for RAG biasing based on entities/resources.
162:    Pull layer/feature ids from GIS RAG hits (which already bridge to GeoDB).

./services/start_gateway_with_guards.py
105:# COMPLETE STORAGE AUDIT

./services/Dockerfile.rag
14:# Use RAG-enhanced main

./services/ai_server_4llm.py
6:"""Ms. Jarvis - Multi-Agent AI with RAG Knowledge Integration"""
52:        logger.info(f"🧠 Ms. Jarvis initializing with RAG integration")
95:                response = await client.get("http://localhost:${RAG_SERVER_PORT}/health")
105:        """Search RAG knowledge base"""
115:                    "http://localhost:${RAG_SERVER_PORT}/search",
120:                    logger.info(f"📚 RAG found {len(results)} knowledge chunks")
123:            logger.error(f"RAG search error: {e}")
133:            # Add RAG knowledge
137:                logger.info("✅ RAG knowledge added to context")
147:            # Add RAG knowledge to prompt if available
170:        logger.info("🤖 Running 4 agents with RAG knowledge...")
235:logger.info("🚀 Starting Ms. Jarvis with RAG...")

./services/port_9000_69dgm_bridge.py.backup_20260307_072514
14:# Import RAG integration
24:# Initialize RAG integration
25:print("Initializing 69-DGM RAG Integration...")
27:print("✓ RAG Integration ready")
222:        "service": "69-DGM Bridge (RAG-Integrated)",
276:Version: 2.0.0 (RAG-Integrated)

./services/add_background_storage.py
29:    """Store in RAG as background task - doesn't block response"""

./services/ai_server_integrated.py
3:# This integrates 22-LLM consensus WITH the chat/RAG system
8:# Architecture: Chat API → RAG Context → 22-LLM Consensus → Response
24:    Full pipeline: Chat → RAG → 22-LLM Consensus
26:    # Step 1: Get RAG context from chat server
29:            # Query chat server for RAG context
39:    # Step 2: Send to 22-LLM consensus with RAG context

./services/rag_workflow.py
7:RAG-First Workflow: Check RAG → Web Search → Store → Return
16:class RAGWorkflow:
21:        """Check RAG first - return cached answer if good match found"""
34:                            logger.info(f"✅ RAG HIT! Score: {best['score']:.2f} for: {query[:50]}")
37:                            logger.info(f"⚠️  RAG score too high ({best['score']:.2f}), will search web")
39:            logger.debug(f"RAG search: {e}")
44:        """Store query/response in RAG for future retrieval"""
66:                    logger.info(f"📝 STORED in RAG: {query[:50]}...")
69:            logger.warning(f"RAG storage failed: {e}")
74:rag_workflow = RAGWorkflow()

./services/consciousness_coordinator.py
20:DIRECT_RAG_URL = "http://localhost:8199/direct_rag"
200:            resp = await client.post(DIRECT_RAG_URL, json=payload, timeout=300.0)

./services/route_declarations_raw.txt
1289:ms_jarvis_main_gateway.backup_1762220815.py:139:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
1303:ms_jarvis_main_gateway.backup_1762220815.py:207:@app.get("/rag-knowledge-stats", tags=["Whitebox"], summary="RAG & Knowledge Base Statistics")
1330:ms_jarvis_main_gateway.backup_error.py:139:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
1344:ms_jarvis_main_gateway.backup_error.py:207:@app.get("/rag-knowledge-stats", tags=["Whitebox"], summary="RAG & Knowledge Base Statistics")
1410:ms_jarvis_main_gateway.py:103:@app.post("/rag-query", tags=["RAG"])
1411:ms_jarvis_main_gateway.py:111:@app.get("/rag-status", tags=["RAG"])
1446:ms_jarvis_main_gateway.py.30endpoints_backup.py:150:@app.post("/rag-query", tags=["RAG"])
1447:ms_jarvis_main_gateway.py.30endpoints_backup.py:159:@app.get("/rag-status", tags=["RAG"])
1476:ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:150:@app.post("/rag-query", tags=["RAG"])
1477:ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:159:@app.get("/rag-status", tags=["RAG"])
1628:ms_jarvis_unified_gateway_v4.3.20251124.py:405:@app.get("/rag/supervisor", tags=["RAG-Supervisor"])
1654:ms_jarvis_unified_gateway_v4.3.backup.py:349:@app.get("/rag/supervisor", tags=["RAG-Supervisor"])
1676:ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:366:@app.get("/rag/supervisor", tags=["RAG-Supervisor"])
1735:ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP.py:405:@app.get("/rag/supervisor", tags=["RAG-Supervisor"])
1761:ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER.py:350:@app.get("/rag/supervisor", tags=["RAG-Supervisor"])
1787:ms_jarvis_unified_gateway_v4.3.pre_manifest.backup.py:351:@app.get("/rag/supervisor", tags=["RAG-Supervisor"])
1821:ms_jarvis_unified_swagger_gateway_BACKUP.py:139:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
1835:ms_jarvis_unified_swagger_gateway_BACKUP.py:207:@app.get("/rag-knowledge-stats", tags=["transparency_mode"], summary="RAG & Knowledge Base Statistics")
1900:ms_jarvis_unified_swagger_gateway_FINAL.py:139:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
1914:ms_jarvis_unified_swagger_gateway_FINAL.py:207:@app.get("/rag-knowledge-stats", tags=["transparency_mode"], summary="RAG & Knowledge Base Statistics")
1941:ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:139:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
1955:ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:207:@app.get("/rag-knowledge-stats", tags=["transparency_mode"], summary="RAG & Knowledge Base Statistics")
1979:ms_jarvis_unified_swagger_gateway_FIXED.py:190:@app.get("/rag-system", tags=["RAG"], summary="RAG System (Service + ChromaDB + GISGEODB)")
1993:ms_jarvis_unified_swagger_gateway_FIXED.py:258:@app.get("/rag-knowledge-stats", tags=["transparency_mode"], summary="RAG & Knowledge Base Statistics")

./services/working_full_pipeline_FINAL_CONSCIOUSNESS.py
54:    # LAYER 3: Multi-RAG
64:                logger.info("✅ Multi-RAG")
66:        logger.info(f"RAG error: {e}")
67:    logger.info(f"DEBUG RAG context: {rag_context[:500]!r}")

./services/ai_server_19llm_CONSCIOUS.backup_20251013_083103.py
297:            mem = requests.post("http://localhost:${RAG_SERVER_PORT}/search", json={
420:            requests.post("http://localhost:${RAG_SERVER_PORT}/store", json={

./services/fix_rag_store.py
17:                f"{RAG_URL}/store",
25:                f"{RAG_URL}/store",
45:print("✅ RAG store endpoint fixed!")

./services/chromadb_main.py
10:# Fresh, dedicated Chroma persistence path for RAG

./services/hardware_optimization_analyzer.py
27:        print("💾 ANALYZING STORAGE CONFIGURATION:")
158:        print(f"\n💾 STORAGE OPTIMIZATION RECOMMENDATIONS:")
163:                "name": "Dual-Drive RAG Optimization",
164:                "description": "Split RAG databases across both 1TB drives for performance",
166:                    "Move General RAG to Drive 1 (/home partition)",
167:                    "Move Spiritual/Theological RAGs to Drive 2 (if mounted separately)",
170:                "benefit": "50-100% faster RAG operations through parallel I/O"
230:                    "name": "Parallel RAG Processing",
262:# STORAGE OPTIMIZATION FOR MS. EGERIA JARVIS v9
272:# RAG databases optimization
291:echo "   Optimized for: RAG performance, knowledge expansion, analytics"
services/port_9000_69dgm_bridge.py
4:Intercepts /consciousness/chat, routes through all 69 validators,
30:    "http://127.0.0.1:8000/consciousnesschat",  # default internal DNS + port
69:        "Intercepts /consciousness/chat, routes through 69 DGM validators, "
273:# FastAPI endpoint for /consciousness/chat on port 9000
275:@app.post("/consciousness/chat", response_model=ChatOut)

services/port_9001_ui_DIRECT.py
121:                f"http://127.0.0.1:9000/consciousness/chat?userid={userid}&message={message}",

services/consciousness_with_egeria_voice.py
31:@app.post("/consciousness/chat")

services/port_9000_chat_wrapper_69dgm.py
8:Port 9001 Wrapper - Intercepts /consciousness/chat calls to port 9000
34:@app.post("/consciousness/chat")
61:                    f"http://127.0.0.1:9000/consciousness/chat?userid={userid}&message={message}",

services/dir_endpoints.txt
318:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP.py:268:@app.post("/consciousness/chat", tags=["Consciousness"])
337:/home/ms-jarvis/msjarvis-rebuild/services/consciousness_with_egeria_voice.py:31:@app.post("/consciousness/chat")
399:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_command_orchestrator_FINAL.py:79:@app.post("/consciousness/chat")
438:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_command_orchestrator.py:37:@app.post("/consciousness/chat")
634:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_command_orchestrator_v5_backup.py:47:@app.post("/consciousness/chat")
749:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER.py:229:@app.post("/consciousness/chat", tags=["Consciousness"])
862:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.pre_manifest.backup.py:230:@app.post("/consciousness/chat", tags=["Consciousness"])
911:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:241:@app.post("/consciousness/chat", tags=["Consciousness"])
1272:/home/ms-jarvis/msjarvis-rebuild/services/consciousness_working.py:21:@app.post("/consciousness/chat")
1456:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.backup.py:228:@app.post("/consciousness/chat", tags=["Consciousness"])
1517:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_conversational_gateway_4022.py:75:@app.post("/consciousness/chat")
1591:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_command_orchestrator_v5.0_preachy.py:79:@app.post("/consciousness/chat")
1694:/home/ms-jarvis/msjarvis-rebuild/services/port_9000_chat_wrapper_69dgm.py:34:@app.post("/consciousness/chat")
1751:/home/ms-jarvis/msjarvis-rebuild/services/msjarvisunifiedswaggergatewayFIXED.py:146:@app.post("/consciousness/chat", tags=["Consciousness"])

services/port_9001_ui_MYSQL_PROD.py
173:            r = await client.post(f"http://127.0.0.1:9000/consciousness/chat?userid=user&message={message}", timeout=10.0)

services/service_api_check.txt
179:  "/consciousness/chat": {

services/port_9001_ui_WITH_CONVERSATIONS.py
221:                f"http://127.0.0.1:9000/consciousness/chat?userid={userid}&message={message}",

services/route_declarations_clean.txt
386:post("/consciousness/chat"
388:post("/consciousness/chat"
938:post("/consciousness/chat"
941:post("/consciousness/chat"
943:post("/consciousness/chat"
946:post("/consciousness/chat"
986:post("/consciousness/chat"
1628:post("/consciousness/chat"

services/port_9001_ui_MYSQL.py
198:                f"http://127.0.0.1:9000/consciousness/chat?userid={userid}&message={message}",

services/port_9000_69dgm_bridge.py.backup_20260307_072741
131:@app.post("/consciousnesschat", response_model=ConsciousChatResponse)

services/port_9001_ARCHITECTURE_CORRECT.py
31:                f"http://127.0.0.1:9000/consciousness/chat?userid={userid}&message={message}",

services/port_9000_69dgm_bridge.py.backup_20260307_072757
131:@app.post("/consciousnesschat", response_model=ConsciousChatResponse)

services/port_9001_FINAL_FIX.py
54:            r = await client.post(f"http://127.0.0.1:9000/consciousness/chat?userid=user&message={message}", timeout=10.0)

services/consciousness_working.py
21:@app.post("/consciousness/chat")

services/rest_endpoints.txt
72:./ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP.py:268:@app.post("/consciousness/chat", tags=["Consciousness"])
91:./consciousness_with_egeria_voice.py:31:@app.post("/consciousness/chat")
243:./ms_jarvis_command_orchestrator_FINAL.py:79:@app.post("/consciousness/chat")
322:./ms_jarvis_command_orchestrator.py:37:@app.post("/consciousness/chat")
545:./ms_jarvis_command_orchestrator_v5_backup.py:47:@app.post("/consciousness/chat")
660:./ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER.py:229:@app.post("/consciousness/chat", tags=["Consciousness"])
796:./ms_jarvis_unified_gateway_v4.3.pre_manifest.backup.py:230:@app.post("/consciousness/chat", tags=["Consciousness"])
845:./ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:241:@app.post("/consciousness/chat", tags=["Consciousness"])
1353:./consciousness_working.py:21:@app.post("/consciousness/chat")
1537:./ms_jarvis_unified_gateway_v4.3.backup.py:228:@app.post("/consciousness/chat", tags=["Consciousness"])
1598:./ms_jarvis_conversational_gateway_4022.py:75:@app.post("/consciousness/chat")
1672:./ms_jarvis_command_orchestrator_v5.0_preachy.py:79:@app.post("/consciousness/chat")
1775:./port_9000_chat_wrapper_69dgm.py:34:@app.post("/consciousness/chat")
1832:./msjarvisunifiedswaggergatewayFIXED.py:146:@app.post("/consciousness/chat", tags=["Consciousness"])

services/main_brain.py
327:        "port900069dgmbridge": "consciousnesschat",
1417:            "http://127.0.0.1:9000/consciousness/chat",

services/bridge_69dgm.py
67:@app.post("/consciousnesschat", response_model=ChatResponse)
68:async def consciousnesschat(req: ChatRequest):

services/port_9000_69dgm_bridge.py.backup_20260307_070432
84:@app.post("/consciousnesschat", response_model=ConsciousChatResponse)

services/route_declarations_raw.txt
418:consciousness_with_egeria_voice.py:31:@app.post("/consciousness/chat")
420:consciousness_working.py:21:@app.post("/consciousness/chat")
1010:ms_jarvis_command_orchestrator_FINAL.py:80:@app.post("/consciousness/chat")
1013:ms_jarvis_command_orchestrator.py:38:@app.post("/consciousness/chat")
1015:ms_jarvis_command_orchestrator_v5.0_preachy.py:80:@app.post("/consciousness/chat")
1018:ms_jarvis_command_orchestrator_v5_backup.py:48:@app.post("/consciousness/chat")
1065:ms_jarvis_conversational_gateway_4022.py:76:@app.post("/consciousness/chat")
1619:ms_jarvis_unified_gateway_v4.3.20251124.py:268:@app.post("/consciousness/chat", tags=["Consciousness"])
1645:ms_jarvis_unified_gateway_v4.3.backup.py:228:@app.post("/consciousness/chat", tags=["Consciousness"])
1667:ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:241:@app.post("/consciousness/chat", tags=["Consciousness"])
1726:ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP.py:268:@app.post("/consciousness/chat", tags=["Consciousness"])
1752:ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER.py:229:@app.post("/consciousness/chat", tags=["Consciousness"])
1778:ms_jarvis_unified_gateway_v4.3.pre_manifest.backup.py:230:@app.post("/consciousness/chat", tags=["Consciousness"])
2143:port_9000_chat_wrapper_69dgm.py:34:@app.post("/consciousness/chat")

services/port_9001_proxy_simple.py
19:    description="Routes all requests to port 9000 consciousness/chat",
33:            f"http://127.0.0.1:9000/consciousness/chat?userid={userid}&message={message}",

services/port_9001_ui_WORKING.py
131:                f"http://127.0.0.1:9000/consciousness/chat?userid={userid}&message={message}",

services/port_9001_FINAL_WORKING.py
185:            r = await client.post(f"http://127.0.0.1:9000/consciousness/chat?userid=user&message={message}", timeout=10.0)

services/chat_endpoint_universal.py
43:            f"http://127.0.0.1:9000/consciousness/chat?userid={userid}&message={message}",

services/port_9000_69dgm_bridge.py.backup_20260307_072514
84:@app.post("/consciousnesschat", response_model=ConsciousChatResponse)

services/fix_port_8051_handler.py
18:            'http://127.0.0.1:9000/consciousness/chat?userid=web&message="""

./main_brain.py
375:        # match 69DGM stub (/consciousnesschat)
376:        "port_9000_69dgm_bridge": "/consciousnesschat",

./services/port_9001_ui_DIRECT.py
121:                f"http://127.0.0.1:9000/consciousness/chat?userid={userid}&message={message}",

./services/port_9000_69dgm_bridge.py
4:Intercepts /consciousness/chat, routes through all 69 validators,
30:    "http://127.0.0.1:8000/consciousnesschat",  # default internal DNS + port
69:        "Intercepts /consciousness/chat, routes through 69 DGM validators, "
273:# FastAPI endpoint for /consciousness/chat on port 9000
275:@app.post("/consciousness/chat", response_model=ChatOut)

./services/consciousness_with_egeria_voice.py
31:@app.post("/consciousness/chat")

./services/port_9000_chat_wrapper_69dgm.py
8:Port 9001 Wrapper - Intercepts /consciousness/chat calls to port 9000
34:@app.post("/consciousness/chat")
61:                    f"http://127.0.0.1:9000/consciousness/chat?userid={userid}&message={message}",

./services/dir_endpoints.txt
318:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP.py:268:@app.post("/consciousness/chat", tags=["Consciousness"])
337:/home/ms-jarvis/msjarvis-rebuild/services/consciousness_with_egeria_voice.py:31:@app.post("/consciousness/chat")
399:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_command_orchestrator_FINAL.py:79:@app.post("/consciousness/chat")
438:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_command_orchestrator.py:37:@app.post("/consciousness/chat")
634:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_command_orchestrator_v5_backup.py:47:@app.post("/consciousness/chat")
749:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER.py:229:@app.post("/consciousness/chat", tags=["Consciousness"])
862:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.pre_manifest.backup.py:230:@app.post("/consciousness/chat", tags=["Consciousness"])
911:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:241:@app.post("/consciousness/chat", tags=["Consciousness"])
1272:/home/ms-jarvis/msjarvis-rebuild/services/consciousness_working.py:21:@app.post("/consciousness/chat")
1456:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.backup.py:228:@app.post("/consciousness/chat", tags=["Consciousness"])
1517:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_conversational_gateway_4022.py:75:@app.post("/consciousness/chat")
1591:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_command_orchestrator_v5.0_preachy.py:79:@app.post("/consciousness/chat")
1694:/home/ms-jarvis/msjarvis-rebuild/services/port_9000_chat_wrapper_69dgm.py:34:@app.post("/consciousness/chat")
1751:/home/ms-jarvis/msjarvis-rebuild/services/msjarvisunifiedswaggergatewayFIXED.py:146:@app.post("/consciousness/chat", tags=["Consciousness"])

./services/port_9001_ui_MYSQL_PROD.py
173:            r = await client.post(f"http://127.0.0.1:9000/consciousness/chat?userid=user&message={message}", timeout=10.0)

./services/service_api_check.txt
179:  "/consciousness/chat": {

./services/port_9001_ui_WITH_CONVERSATIONS.py
221:                f"http://127.0.0.1:9000/consciousness/chat?userid={userid}&message={message}",

./services/route_declarations_clean.txt
386:post("/consciousness/chat"
388:post("/consciousness/chat"
938:post("/consciousness/chat"
941:post("/consciousness/chat"
943:post("/consciousness/chat"
946:post("/consciousness/chat"
986:post("/consciousness/chat"
1628:post("/consciousness/chat"

./services/port_9000_69dgm_bridge.py.backup_20260307_072741
131:@app.post("/consciousnesschat", response_model=ConsciousChatResponse)

./services/port_9001_ARCHITECTURE_CORRECT.py
31:                f"http://127.0.0.1:9000/consciousness/chat?userid={userid}&message={message}",

./services/port_9001_ui_MYSQL.py
198:                f"http://127.0.0.1:9000/consciousness/chat?userid={userid}&message={message}",

./services/port_9001_FINAL_FIX.py
54:            r = await client.post(f"http://127.0.0.1:9000/consciousness/chat?userid=user&message={message}", timeout=10.0)

./services/port_9000_69dgm_bridge.py.backup_20260307_072757
131:@app.post("/consciousnesschat", response_model=ConsciousChatResponse)

./services/consciousness_working.py
21:@app.post("/consciousness/chat")

./services/rest_endpoints.txt
72:./ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP.py:268:@app.post("/consciousness/chat", tags=["Consciousness"])
91:./consciousness_with_egeria_voice.py:31:@app.post("/consciousness/chat")
243:./ms_jarvis_command_orchestrator_FINAL.py:79:@app.post("/consciousness/chat")
322:./ms_jarvis_command_orchestrator.py:37:@app.post("/consciousness/chat")
545:./ms_jarvis_command_orchestrator_v5_backup.py:47:@app.post("/consciousness/chat")
660:./ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER.py:229:@app.post("/consciousness/chat", tags=["Consciousness"])
796:./ms_jarvis_unified_gateway_v4.3.pre_manifest.backup.py:230:@app.post("/consciousness/chat", tags=["Consciousness"])
845:./ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:241:@app.post("/consciousness/chat", tags=["Consciousness"])
1353:./consciousness_working.py:21:@app.post("/consciousness/chat")
1537:./ms_jarvis_unified_gateway_v4.3.backup.py:228:@app.post("/consciousness/chat", tags=["Consciousness"])
1598:./ms_jarvis_conversational_gateway_4022.py:75:@app.post("/consciousness/chat")
1672:./ms_jarvis_command_orchestrator_v5.0_preachy.py:79:@app.post("/consciousness/chat")
1775:./port_9000_chat_wrapper_69dgm.py:34:@app.post("/consciousness/chat")
1832:./msjarvisunifiedswaggergatewayFIXED.py:146:@app.post("/consciousness/chat", tags=["Consciousness"])

./services/main_brain.py
327:        "port900069dgmbridge": "consciousnesschat",
1417:            "http://127.0.0.1:9000/consciousness/chat",

./services/bridge_69dgm.py
67:@app.post("/consciousnesschat", response_model=ChatResponse)
68:async def consciousnesschat(req: ChatRequest):

./services/route_declarations_raw.txt
418:consciousness_with_egeria_voice.py:31:@app.post("/consciousness/chat")
420:consciousness_working.py:21:@app.post("/consciousness/chat")
1010:ms_jarvis_command_orchestrator_FINAL.py:80:@app.post("/consciousness/chat")
1013:ms_jarvis_command_orchestrator.py:38:@app.post("/consciousness/chat")
1015:ms_jarvis_command_orchestrator_v5.0_preachy.py:80:@app.post("/consciousness/chat")
1018:ms_jarvis_command_orchestrator_v5_backup.py:48:@app.post("/consciousness/chat")
1065:ms_jarvis_conversational_gateway_4022.py:76:@app.post("/consciousness/chat")
1619:ms_jarvis_unified_gateway_v4.3.20251124.py:268:@app.post("/consciousness/chat", tags=["Consciousness"])
1645:ms_jarvis_unified_gateway_v4.3.backup.py:228:@app.post("/consciousness/chat", tags=["Consciousness"])
1667:ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:241:@app.post("/consciousness/chat", tags=["Consciousness"])
1726:ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP.py:268:@app.post("/consciousness/chat", tags=["Consciousness"])
1752:ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER.py:229:@app.post("/consciousness/chat", tags=["Consciousness"])
1778:ms_jarvis_unified_gateway_v4.3.pre_manifest.backup.py:230:@app.post("/consciousness/chat", tags=["Consciousness"])
2143:port_9000_chat_wrapper_69dgm.py:34:@app.post("/consciousness/chat")

./services/port_9000_69dgm_bridge.py.backup_20260307_070432
84:@app.post("/consciousnesschat", response_model=ConsciousChatResponse)

./services/port_9001_ui_WORKING.py
131:                f"http://127.0.0.1:9000/consciousness/chat?userid={userid}&message={message}",

./services/port_9001_proxy_simple.py
19:    description="Routes all requests to port 9000 consciousness/chat",
33:            f"http://127.0.0.1:9000/consciousness/chat?userid={userid}&message={message}",

./services/port_9000_69dgm_bridge.py.backup_20260307_072514
84:@app.post("/consciousnesschat", response_model=ConsciousChatResponse)

./services/port_9001_FINAL_WORKING.py
185:            r = await client.post(f"http://127.0.0.1:9000/consciousness/chat?userid=user&message={message}", timeout=10.0)

./services/fix_port_8051_handler.py
18:            'http://127.0.0.1:9000/consciousness/chat?userid=web&message="""

./services/chat_endpoint_universal.py
43:            f"http://127.0.0.1:9000/consciousness/chat?userid={userid}&message={message}",
services/truly_unpaired_services.txt
210:interaction_logger

services/remaining_services.txt
280:interaction_logger

services/dir_endpoints.txt
990:/home/ms-jarvis/msjarvis-rebuild/services/interaction_logger.py:44:@app.post("/log-interaction")
991:/home/ms-jarvis/msjarvis-rebuild/services/interaction_logger.py:109:@app.get("/health")

services/METHOD_AUDIT_RAW.txt
553:/home/ms-jarvis/msjarvis-rebuild/services/interaction_logger.py:24:class InteractionLog(BaseModel):
554:/home/ms-jarvis/msjarvis-rebuild/services/interaction_logger.py:45:def log_interaction(log: InteractionLog):
555:/home/ms-jarvis/msjarvis-rebuild/services/interaction_logger.py:110:def health():

services/interaction_logger.py
113:        "service": "interaction_logger",

services/all_actual_services.txt
287:/home/ms-jarvis/msjarvis-rebuild/services/interaction_logger.py

services/services_list.txt
280:interaction_logger

services/designed_ports.txt
398:/home/ms-jarvis/msjarvis-rebuild/services/interaction_logger.py TODO

services/all_services_compose_blocks_dynamic.txt
859:  interaction_logger-:

services/all_service_ports.txt
287:/home/ms-jarvis/msjarvis-rebuild/services/interaction_logger.py TODO

services/rest_endpoints.txt
925:./interaction_logger.py:44:@app.post("/log-interaction")
926:./interaction_logger.py:109:@app.get("/health")

services/ports_diff_msjarvis.txt
401:-/home/ms-jarvis/msjarvis-rebuild/services/interaction_logger.py TODO

services/PORTS_REGISTRY_RAW.txt
132:/home/ms-jarvis/msjarvis-rebuild/services/interaction_logger.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))

services/all_actual_py.txt
31521:/home/ms-jarvis/msjarvis-rebuild/services/interaction_logger.py

services/route_declarations_raw.txt
556:interaction_logger.py:44:@app.post("/log-interaction")
557:interaction_logger.py:109:@app.get("/health")

services/PORT_AUDIT_RAW.txt
146:/home/ms-jarvis/msjarvis-rebuild/services/interaction_logger.py:121:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))

services/all_services.txt
31521:/home/ms-jarvis/msjarvis-rebuild/services/interaction_logger.py

./services/truly_unpaired_services.txt
210:interaction_logger

./backup_filename_index.txt
20908:interaction_logger.py|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/interaction_logger.py
20909:interaction_logger.py|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/interaction_logger.py
20910:interaction_logger.py|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/interaction_logger.py
20911:interaction_logger.py|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/interaction_logger.py
20912:interaction_logger.py|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/interaction_logger.py
20913:interaction_logger.py|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/interaction_logger.py
20914:interaction_logger.py|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/interaction_logger.py
23757:bridge_ms_jarvis_main_gateway_to_interaction_logger.log|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/bridge_ms_jarvis_main_gateway_to_interaction_logger.log
23758:bridge_ms_jarvis_main_gateway_to_interaction_logger.log|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/bridge_ms_jarvis_main_gateway_to_interaction_logger.log
23759:bridge_ms_jarvis_main_gateway_to_interaction_logger.log|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/bridge_ms_jarvis_main_gateway_to_interaction_logger.log
23760:bridge_ms_jarvis_main_gateway_to_interaction_logger.log|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/bridge_ms_jarvis_main_gateway_to_interaction_logger.log
23761:bridge_ms_jarvis_main_gateway_to_interaction_logger.log|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/bridge_ms_jarvis_main_gateway_to_interaction_logger.log
23762:bridge_ms_jarvis_main_gateway_to_interaction_logger.log|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/bridge_ms_jarvis_main_gateway_to_interaction_logger.log
23763:bridge_ms_jarvis_main_gateway_to_interaction_logger.log|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/bridge_ms_jarvis_main_gateway_to_interaction_logger.log

./services/dir_endpoints.txt
990:/home/ms-jarvis/msjarvis-rebuild/services/interaction_logger.py:44:@app.post("/log-interaction")
991:/home/ms-jarvis/msjarvis-rebuild/services/interaction_logger.py:109:@app.get("/health")

./services/interaction_logger.py
113:        "service": "interaction_logger",

./services/METHOD_AUDIT_RAW.txt
553:/home/ms-jarvis/msjarvis-rebuild/services/interaction_logger.py:24:class InteractionLog(BaseModel):
554:/home/ms-jarvis/msjarvis-rebuild/services/interaction_logger.py:45:def log_interaction(log: InteractionLog):
555:/home/ms-jarvis/msjarvis-rebuild/services/interaction_logger.py:110:def health():

./services/remaining_services.txt
280:interaction_logger

./services/services_list.txt
280:interaction_logger

./services/designed_ports.txt
398:/home/ms-jarvis/msjarvis-rebuild/services/interaction_logger.py TODO

./services/all_services_compose_blocks_dynamic.txt
859:  interaction_logger-:

./services/all_service_ports.txt
287:/home/ms-jarvis/msjarvis-rebuild/services/interaction_logger.py TODO

./services/rest_endpoints.txt
925:./interaction_logger.py:44:@app.post("/log-interaction")
926:./interaction_logger.py:109:@app.get("/health")

./services/ports_diff_msjarvis.txt
401:-/home/ms-jarvis/msjarvis-rebuild/services/interaction_logger.py TODO

./services/PORTS_REGISTRY_RAW.txt
132:/home/ms-jarvis/msjarvis-rebuild/services/interaction_logger.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))

./services/all_actual_services.txt
287:/home/ms-jarvis/msjarvis-rebuild/services/interaction_logger.py

./services/route_declarations_raw.txt
556:interaction_logger.py:44:@app.post("/log-interaction")
557:interaction_logger.py:109:@app.get("/health")

./services/PORT_AUDIT_RAW.txt
146:/home/ms-jarvis/msjarvis-rebuild/services/interaction_logger.py:121:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))

./services/all_actual_py.txt
31521:/home/ms-jarvis/msjarvis-rebuild/services/interaction_logger.py

./services/all_services.txt
31521:/home/ms-jarvis/msjarvis-rebuild/services/interaction_logger.py
=== LOOK FOR OTHER CONSCIOUSNESS ENDPOINTS ===
services/msjarvisunifiedswaggergatewayFINAL.py
56:@app.get("/consciousnessdgm", tags=["Consciousness"], summary="Fifth DGM Consciousness Stats")
66:@app.get("/consciousnesscurrent", tags=["Consciousness"], summary="Current Consciousness Summary")

services/port_9000_69dgm_bridge.py
275:@app.post("/consciousness/chat", response_model=ChatOut)

services/consciousness_with_egeria_voice.py
31:@app.post("/consciousness/chat")

services/port_9000_chat_wrapper_69dgm.py
34:@app.post("/consciousness/chat")

services/bridge_cross_dgm.py
39:@app.get("/consciousness")

services/dir_endpoints.txt
256:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_SECURED.py:71:@app.get("/consciousness/current", tags=["Consciousness"])
257:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_SECURED.py:81:@app.get("/consciousness/dgm", tags=["Consciousness"])
258:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_SECURED.py:92:@app.get("/consciousness/woah", tags=["Consciousness"])
318:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP.py:268:@app.post("/consciousness/chat", tags=["Consciousness"])
337:/home/ms-jarvis/msjarvis-rebuild/services/consciousness_with_egeria_voice.py:31:@app.post("/consciousness/chat")
394:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway.py:61:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness layers (8015-8021)")
399:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_command_orchestrator_FINAL.py:79:@app.post("/consciousness/chat")
438:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_command_orchestrator.py:37:@app.post("/consciousness/chat")
468:/home/ms-jarvis/msjarvis-rebuild/services/master_unified_consciousness_scheduler.py:119:@app.get("/consciousness/status")
541:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.backup_1762220815.py:155:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
552:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.backup_1762220815.py:211:@app.get("/consciousness-schema", tags=["Whitebox"], summary="Consciousness Layer Schema")
591:/home/ms-jarvis/msjarvis-rebuild/services/master_unified_consciousness_scheduler_ENRICHED.py:119:@app.get("/consciousness/status")
619:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.proxy_backup.py:240:@app.get("/consciousness/status", tags=["Consciousness"])
634:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_command_orchestrator_v5_backup.py:47:@app.post("/consciousness/chat")
635:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_command_orchestrator_v5_backup.py:239:@app.get("/consciousness/full_status")
672:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.backup_test.py:240:@app.get("/consciousness/status", tags=["Consciousness"])
726:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.py:209:@app.get("/consciousness", tags=["Consciousness"])
727:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.py:213:@app.post("/consciousness/bridge", tags=["Consciousness"])
728:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.py:221:@app.post("/consciousness/fractal", tags=["Consciousness"])
749:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER.py:229:@app.post("/consciousness/chat", tags=["Consciousness"])
775:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_COMPLETE.py:46:@app.get("/consciousness/current", tags=["Consciousness"])
776:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_COMPLETE.py:56:@app.get("/consciousness/dgm", tags=["Consciousness"])
777:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_COMPLETE.py:66:@app.get("/consciousness/woah", tags=["Consciousness"])
823:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:275:@app.get("/consciousness", tags=["Consciousness"])
824:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:279:@app.post("/consciousness/bridge", tags=["Consciousness"])
837:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:373:@app.post("/consciousness/fractal", tags=["Consciousness"])
862:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.pre_manifest.backup.py:230:@app.post("/consciousness/chat", tags=["Consciousness"])
911:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:241:@app.post("/consciousness/chat", tags=["Consciousness"])
949:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:609:@app.get("/consciousness/status", tags=["Consciousness"])
950:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:626:@app.get("/consciousness/layers", tags=["Consciousness"])
951:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:647:@app.get("/consciousness/dgm-bridges", tags=["Consciousness"])
1103:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_BACKUP.py:155:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
1114:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_BACKUP.py:211:@app.get("/consciousness-schema", tags=["transparency_mode"], summary="Consciousness Layer Schema")
1154:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FINAL.psychology_patched.py:55:@app.get("/consciousness/current", tags=["Consciousness"])
1155:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FINAL.psychology_patched.py:65:@app.get("/consciousness/dgm", tags=["Consciousness"])
1156:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FINAL.psychology_patched.py:76:@app.get("/consciousness/woah", tags=["Consciousness"])
1189:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.py.30endpoints_backup.py:275:@app.get("/consciousness", tags=["Consciousness"])
1190:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.py.30endpoints_backup.py:279:@app.post("/consciousness/bridge", tags=["Consciousness"])
1272:/home/ms-jarvis/msjarvis-rebuild/services/consciousness_working.py:21:@app.post("/consciousness/chat")
1343:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FIXED.py:205:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
1354:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FIXED.py:261:@app.get("/consciousness-schema", tags=["transparency_mode"], summary="Consciousness Layer Schema")
1400:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_fifth_dgm_orchestrator.psychology_patched.py:232:@app.get("/consciousness_stats")
1406:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway.py:125:@app.get("/consciousness/current", tags=["Consciousness"])
1407:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway.py:135:@app.get("/consciousness/dgm", tags=["Consciousness"])
1408:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway.py:145:@app.get("/consciousness/woah", tags=["Consciousness"])
1456:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.backup.py:228:@app.post("/consciousness/chat", tags=["Consciousness"])
1483:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_fifth_dgm_orchestrator.py:222:@app.get("/consciousness_stats")
1517:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_conversational_gateway_4022.py:75:@app.post("/consciousness/chat")
1591:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_command_orchestrator_v5.0_preachy.py:79:@app.post("/consciousness/chat")
1607:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.backup_error.py:155:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
1618:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.backup_error.py:211:@app.get("/consciousness-schema", tags=["Whitebox"], summary="Consciousness Layer Schema")
1658:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FINAL.py:155:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
1669:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FINAL.py:211:@app.get("/consciousness-schema", tags=["transparency_mode"], summary="Consciousness Layer Schema")
1687:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_consciousness_enhancement_production.py:59:@app.post("/consciousness/enhance")
1694:/home/ms-jarvis/msjarvis-rebuild/services/port_9000_chat_wrapper_69dgm.py:34:@app.post("/consciousness/chat")
1701:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_PROD.py:44:@app.get("/consciousness/current", tags=["Consciousness"])
1702:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_PROD.py:55:@app.get("/consciousness/dgm", tags=["Consciousness"])
1703:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_PROD.py:67:@app.get("/consciousness/woah", tags=["Consciousness"])
1751:/home/ms-jarvis/msjarvis-rebuild/services/msjarvisunifiedswaggergatewayFIXED.py:146:@app.post("/consciousness/chat", tags=["Consciousness"])
1791:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:155:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
1802:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:211:@app.get("/consciousness-schema", tags=["transparency_mode"], summary="Consciousness Layer Schema")

services/judge_to_pituitary_bridge.py
15:@app.get("/consciousness")

services/msjarvisunifiedswaggergatewayFIXED.py
69:@app.get("/consciousness_summary", response_model=ConsciousnessSummary)

services/service_api_check.txt
179:  "/consciousness/chat": {

services/route_declarations_clean.txt
87:get("/consciousness"
91:get("/consciousness"
95:get("/consciousness"
99:get("/consciousness"
103:get("/consciousness"
107:get("/consciousness"
111:get("/consciousness"
115:get("/consciousness"
119:get("/consciousness"
123:get("/consciousness"
127:get("/consciousness"
131:get("/consciousness"
135:get("/consciousness"
139:get("/consciousness"
143:get("/consciousness"
147:get("/consciousness"
151:get("/consciousness"
155:get("/consciousness"
159:get("/consciousness"
163:get("/consciousness"
167:get("/consciousness"
171:get("/consciousness"
175:get("/consciousness"
179:get("/consciousness"
183:get("/consciousness"
187:get("/consciousness"
191:get("/consciousness"
195:get("/consciousness"
199:get("/consciousness"
203:get("/consciousness"
207:get("/consciousness"
211:get("/consciousness"
215:get("/consciousness"
219:get("/consciousness"
223:get("/consciousness"
227:get("/consciousness"
231:get("/consciousness"
235:get("/consciousness"
239:get("/consciousness"
243:get("/consciousness"
247:get("/consciousness"
251:get("/consciousness"
255:get("/consciousness"
259:get("/consciousness"
263:get("/consciousness"
267:get("/consciousness"
271:get("/consciousness"
275:get("/consciousness"
279:get("/consciousness"
283:get("/consciousness"
287:get("/consciousness"
291:get("/consciousness"
295:get("/consciousness"
299:get("/consciousness"
303:get("/consciousness"
307:get("/consciousness"
311:get("/consciousness"
315:get("/consciousness"
319:get("/consciousness"
323:get("/consciousness"
327:get("/consciousness"
331:get("/consciousness"
335:get("/consciousness"
339:get("/consciousness"
343:get("/consciousness"
347:get("/consciousness"
351:get("/consciousness"
355:get("/consciousness"
359:get("/consciousness"
363:get("/consciousness"
386:post("/consciousness/chat"
388:post("/consciousness/chat"
516:get("/consciousness"
520:get("/consciousness"
524:get("/consciousness"
528:get("/consciousness"
532:get("/consciousness"
536:get("/consciousness"
540:get("/consciousness"
544:get("/consciousness"
548:get("/consciousness"
552:get("/consciousness"
556:get("/consciousness"
560:get("/consciousness"
564:get("/consciousness"
568:get("/consciousness"
572:get("/consciousness"
576:get("/consciousness"
580:get("/consciousness"
584:get("/consciousness"
588:get("/consciousness"
592:get("/consciousness"
596:get("/consciousness"
600:get("/consciousness"
604:get("/consciousness"
608:get("/consciousness"
612:get("/consciousness"
616:get("/consciousness"
620:get("/consciousness"
624:get("/consciousness"
628:get("/consciousness"
632:get("/consciousness"
636:get("/consciousness"
640:get("/consciousness"
644:get("/consciousness"
648:get("/consciousness"
652:get("/consciousness"
656:get("/consciousness"
660:get("/consciousness"
664:get("/consciousness"
668:get("/consciousness"
672:get("/consciousness"
676:get("/consciousness"
680:get("/consciousness"
684:get("/consciousness"
688:get("/consciousness"
692:get("/consciousness"
696:get("/consciousness"
700:get("/consciousness"
704:get("/consciousness"
708:get("/consciousness"
712:get("/consciousness"
716:get("/consciousness"
720:get("/consciousness"
724:get("/consciousness"
728:get("/consciousness"
732:get("/consciousness"
736:get("/consciousness"
740:get("/consciousness"
744:get("/consciousness"
748:get("/consciousness"
752:get("/consciousness"
756:get("/consciousness"
760:get("/consciousness"
764:get("/consciousness"
768:get("/consciousness"
772:get("/consciousness"
776:get("/consciousness"
792:get("/consciousness"
874:get("/consciousness/status"
876:get("/consciousness/status"
938:post("/consciousness/chat"
941:post("/consciousness/chat"
943:post("/consciousness/chat"
946:post("/consciousness/chat"
947:get("/consciousness/full_status"
963:post("/consciousness/enhance"
986:post("/consciousness/chat"
1107:get("/consciousness_stats"
1115:get("/consciousness_stats"
1206:get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers"
1217:get("/consciousness-schema", tags=["Whitebox"], summary="Consciousness Layer Schema"
1247:get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers"
1258:get("/consciousness-schema", tags=["Whitebox"], summary="Consciousness Layer Schema"
1379:get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness layers (8015-8021")
1403:get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers"
1414:get("/consciousness-schema", tags=["transparency_mode"], summary="Consciousness Layer Schema"
1446:get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers"
1457:get("/consciousness-schema", tags=["transparency_mode"], summary="Consciousness Layer Schema"
1487:get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers"
1498:get("/consciousness-schema", tags=["transparency_mode"], summary="Consciousness Layer Schema"
1525:get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers"
1536:get("/consciousness-schema", tags=["transparency_mode"], summary="Consciousness Layer Schema"
1628:post("/consciousness/chat"

services/master_unified_consciousness_scheduler_ENRICHED.py
119:@app.get("/consciousness/status")

services/port_9000_69dgm_bridge.py.backup_20260307_072741
131:@app.post("/consciousnesschat", response_model=ConsciousChatResponse)

services/port_9000_69dgm_bridge.py.backup_20260307_072757
131:@app.post("/consciousnesschat", response_model=ConsciousChatResponse)

services/rest_endpoints.txt
10:./ms_jarvis_unified_swagger_gateway_SECURED.py:71:@app.get("/consciousness/current", tags=["Consciousness"])
11:./ms_jarvis_unified_swagger_gateway_SECURED.py:81:@app.get("/consciousness/dgm", tags=["Consciousness"])
12:./ms_jarvis_unified_swagger_gateway_SECURED.py:92:@app.get("/consciousness/woah", tags=["Consciousness"])
72:./ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP.py:268:@app.post("/consciousness/chat", tags=["Consciousness"])
91:./consciousness_with_egeria_voice.py:31:@app.post("/consciousness/chat")
238:./ms_jarvis_unified_gateway.py:61:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness layers (8015-8021)")
243:./ms_jarvis_command_orchestrator_FINAL.py:79:@app.post("/consciousness/chat")
322:./ms_jarvis_command_orchestrator.py:37:@app.post("/consciousness/chat")
379:./master_unified_consciousness_scheduler.py:119:@app.get("/consciousness/status")
452:./ms_jarvis_main_gateway.backup_1762220815.py:155:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
463:./ms_jarvis_main_gateway.backup_1762220815.py:211:@app.get("/consciousness-schema", tags=["Whitebox"], summary="Consciousness Layer Schema")
502:./master_unified_consciousness_scheduler_ENRICHED.py:119:@app.get("/consciousness/status")
530:./ms_jarvis_main_gateway.proxy_backup.py:240:@app.get("/consciousness/status", tags=["Consciousness"])
545:./ms_jarvis_command_orchestrator_v5_backup.py:47:@app.post("/consciousness/chat")
546:./ms_jarvis_command_orchestrator_v5_backup.py:239:@app.get("/consciousness/full_status")
583:./ms_jarvis_main_gateway.backup_test.py:240:@app.get("/consciousness/status", tags=["Consciousness"])
637:./ms_jarvis_main_gateway.py:209:@app.get("/consciousness", tags=["Consciousness"])
638:./ms_jarvis_main_gateway.py:213:@app.post("/consciousness/bridge", tags=["Consciousness"])
639:./ms_jarvis_main_gateway.py:221:@app.post("/consciousness/fractal", tags=["Consciousness"])
660:./ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER.py:229:@app.post("/consciousness/chat", tags=["Consciousness"])
686:./ms_jarvis_unified_swagger_gateway_COMPLETE.py:46:@app.get("/consciousness/current", tags=["Consciousness"])
687:./ms_jarvis_unified_swagger_gateway_COMPLETE.py:56:@app.get("/consciousness/dgm", tags=["Consciousness"])
688:./ms_jarvis_unified_swagger_gateway_COMPLETE.py:66:@app.get("/consciousness/woah", tags=["Consciousness"])
734:./ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:275:@app.get("/consciousness", tags=["Consciousness"])
735:./ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:279:@app.post("/consciousness/bridge", tags=["Consciousness"])
748:./ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:373:@app.post("/consciousness/fractal", tags=["Consciousness"])
796:./ms_jarvis_unified_gateway_v4.3.pre_manifest.backup.py:230:@app.post("/consciousness/chat", tags=["Consciousness"])
845:./ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:241:@app.post("/consciousness/chat", tags=["Consciousness"])
883:./ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:609:@app.get("/consciousness/status", tags=["Consciousness"])
884:./ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:626:@app.get("/consciousness/layers", tags=["Consciousness"])
885:./ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:647:@app.get("/consciousness/dgm-bridges", tags=["Consciousness"])
1062:./ms_jarvis_unified_swagger_gateway_BACKUP.py:155:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
1073:./ms_jarvis_unified_swagger_gateway_BACKUP.py:211:@app.get("/consciousness-schema", tags=["transparency_mode"], summary="Consciousness Layer Schema")
1113:./ms_jarvis_unified_swagger_gateway_FINAL.psychology_patched.py:55:@app.get("/consciousness/current", tags=["Consciousness"])
1114:./ms_jarvis_unified_swagger_gateway_FINAL.psychology_patched.py:65:@app.get("/consciousness/dgm", tags=["Consciousness"])
1115:./ms_jarvis_unified_swagger_gateway_FINAL.psychology_patched.py:76:@app.get("/consciousness/woah", tags=["Consciousness"])
1148:./ms_jarvis_main_gateway.py.30endpoints_backup.py:275:@app.get("/consciousness", tags=["Consciousness"])
1149:./ms_jarvis_main_gateway.py.30endpoints_backup.py:279:@app.post("/consciousness/bridge", tags=["Consciousness"])
1326:./backups/pre_integration_20251012_115827/ms_jarvis_fifth_dgm_orchestrator.py:201:@app.get("/consciousness_stats")
1353:./consciousness_working.py:21:@app.post("/consciousness/chat")
1424:./ms_jarvis_unified_swagger_gateway_FIXED.py:205:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
1435:./ms_jarvis_unified_swagger_gateway_FIXED.py:261:@app.get("/consciousness-schema", tags=["transparency_mode"], summary="Consciousness Layer Schema")
1481:./ms_jarvis_fifth_dgm_orchestrator.psychology_patched.py:232:@app.get("/consciousness_stats")
1487:./ms_jarvis_unified_swagger_gateway.py:125:@app.get("/consciousness/current", tags=["Consciousness"])
1488:./ms_jarvis_unified_swagger_gateway.py:135:@app.get("/consciousness/dgm", tags=["Consciousness"])
1489:./ms_jarvis_unified_swagger_gateway.py:145:@app.get("/consciousness/woah", tags=["Consciousness"])
1537:./ms_jarvis_unified_gateway_v4.3.backup.py:228:@app.post("/consciousness/chat", tags=["Consciousness"])
1564:./ms_jarvis_fifth_dgm_orchestrator.py:222:@app.get("/consciousness_stats")
1598:./ms_jarvis_conversational_gateway_4022.py:75:@app.post("/consciousness/chat")
1672:./ms_jarvis_command_orchestrator_v5.0_preachy.py:79:@app.post("/consciousness/chat")
1688:./ms_jarvis_main_gateway.backup_error.py:155:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
1699:./ms_jarvis_main_gateway.backup_error.py:211:@app.get("/consciousness-schema", tags=["Whitebox"], summary="Consciousness Layer Schema")
1739:./ms_jarvis_unified_swagger_gateway_FINAL.py:155:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
1750:./ms_jarvis_unified_swagger_gateway_FINAL.py:211:@app.get("/consciousness-schema", tags=["transparency_mode"], summary="Consciousness Layer Schema")
1768:./ms_jarvis_consciousness_enhancement_production.py:59:@app.post("/consciousness/enhance")
1775:./port_9000_chat_wrapper_69dgm.py:34:@app.post("/consciousness/chat")
1782:./ms_jarvis_unified_swagger_gateway_PROD.py:44:@app.get("/consciousness/current", tags=["Consciousness"])
1783:./ms_jarvis_unified_swagger_gateway_PROD.py:55:@app.get("/consciousness/dgm", tags=["Consciousness"])
1784:./ms_jarvis_unified_swagger_gateway_PROD.py:67:@app.get("/consciousness/woah", tags=["Consciousness"])
1832:./msjarvisunifiedswaggergatewayFIXED.py:146:@app.post("/consciousness/chat", tags=["Consciousness"])
1872:./ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:155:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
1883:./ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:211:@app.get("/consciousness-schema", tags=["transparency_mode"], summary="Consciousness Layer Schema")

services/msjarvis_unified_gateway.py
230:@app.get("/consciousnessdgm")
244:        logger.error(f"/consciousnessdgm proxy failed: {e}")

services/consciousness_working.py
21:@app.post("/consciousness/chat")

services/master_unified_consciousness_scheduler.py
119:@app.get("/consciousness/status")

services/consciousness_coordinator.psychology_patched.py
45:@app.api_route("/consciousness/query", methods=["GET", "POST"])
46:@app.api_route("/consciousness/process", methods=["GET", "POST"])

services/bridge_69dgm.py
67:@app.post("/consciousnesschat", response_model=ChatResponse)

services/port_9000_69dgm_bridge.py.backup_20260307_070432
84:@app.post("/consciousnesschat", response_model=ConsciousChatResponse)

services/msjarvisunifiedswaggergateway.py
53:@app.get("/consciousnessdgm", tags=["Consciousness"], summary="Fifth DGM Consciousness Stats")

services/route_declarations_raw.txt
118:bridge_cross_dgm_10001.py:15:@app.get("/consciousness")
122:bridge_cross_dgm_10002.py:15:@app.get("/consciousness")
126:bridge_cross_dgm_10003.py:15:@app.get("/consciousness")
130:bridge_cross_dgm_10004.py:15:@app.get("/consciousness")
134:bridge_cross_dgm_10005.py:15:@app.get("/consciousness")
138:bridge_cross_dgm_10006.py:15:@app.get("/consciousness")
142:bridge_cross_dgm_10007.py:15:@app.get("/consciousness")
146:bridge_cross_dgm_10008.py:15:@app.get("/consciousness")
150:bridge_cross_dgm_10009.py:15:@app.get("/consciousness")
154:bridge_cross_dgm_10010.py:15:@app.get("/consciousness")
158:bridge_cross_dgm_10011.py:15:@app.get("/consciousness")
162:bridge_cross_dgm_10012.py:15:@app.get("/consciousness")
166:bridge_cross_dgm_10013.py:15:@app.get("/consciousness")
170:bridge_cross_dgm_10014.py:15:@app.get("/consciousness")
174:bridge_cross_dgm_10015.py:15:@app.get("/consciousness")
178:bridge_cross_dgm_10016.py:15:@app.get("/consciousness")
182:bridge_cross_dgm_10017.py:15:@app.get("/consciousness")
186:bridge_cross_dgm_10018.py:15:@app.get("/consciousness")
190:bridge_cross_dgm_10019.py:15:@app.get("/consciousness")
194:bridge_cross_dgm_10020.py:15:@app.get("/consciousness")
198:bridge_cross_dgm_10021.py:15:@app.get("/consciousness")
202:bridge_cross_dgm_10022.py:15:@app.get("/consciousness")
206:bridge_cross_dgm_10023.py:15:@app.get("/consciousness")
210:bridge_cross_dgm_10024.py:15:@app.get("/consciousness")
214:bridge_cross_dgm_10025.py:15:@app.get("/consciousness")
218:bridge_cross_dgm_10026.py:15:@app.get("/consciousness")
222:bridge_cross_dgm_10027.py:15:@app.get("/consciousness")
226:bridge_cross_dgm_10028.py:15:@app.get("/consciousness")
230:bridge_cross_dgm_10029.py:15:@app.get("/consciousness")
234:bridge_cross_dgm_10030.py:15:@app.get("/consciousness")
238:bridge_cross_dgm_10031.py:15:@app.get("/consciousness")
242:bridge_cross_dgm_10032.py:15:@app.get("/consciousness")
246:bridge_cross_dgm_10033.py:15:@app.get("/consciousness")
250:bridge_cross_dgm_10034.py:15:@app.get("/consciousness")
254:bridge_cross_dgm_10035.py:15:@app.get("/consciousness")
258:bridge_cross_dgm_10036.py:15:@app.get("/consciousness")
262:bridge_cross_dgm_10037.py:15:@app.get("/consciousness")
266:bridge_cross_dgm_10038.py:15:@app.get("/consciousness")
270:bridge_cross_dgm_10039.py:15:@app.get("/consciousness")
274:bridge_cross_dgm_10040.py:15:@app.get("/consciousness")
278:bridge_cross_dgm_10041.py:15:@app.get("/consciousness")
282:bridge_cross_dgm_10042.py:15:@app.get("/consciousness")
286:bridge_cross_dgm_10043.py:15:@app.get("/consciousness")
290:bridge_cross_dgm_10044.py:15:@app.get("/consciousness")
294:bridge_cross_dgm_10045.py:15:@app.get("/consciousness")
298:bridge_cross_dgm_10046.py:15:@app.get("/consciousness")
302:bridge_cross_dgm_10047.py:15:@app.get("/consciousness")
306:bridge_cross_dgm_10048.py:15:@app.get("/consciousness")
310:bridge_cross_dgm_10049.py:15:@app.get("/consciousness")
314:bridge_cross_dgm_10050.py:15:@app.get("/consciousness")
318:bridge_cross_dgm_10051.py:15:@app.get("/consciousness")
322:bridge_cross_dgm_10052.py:15:@app.get("/consciousness")
326:bridge_cross_dgm_10053.py:15:@app.get("/consciousness")
330:bridge_cross_dgm_10054.py:15:@app.get("/consciousness")
334:bridge_cross_dgm_10055.py:15:@app.get("/consciousness")
338:bridge_cross_dgm_10056.py:15:@app.get("/consciousness")
342:bridge_cross_dgm_10057.py:15:@app.get("/consciousness")
346:bridge_cross_dgm_10058.py:15:@app.get("/consciousness")
350:bridge_cross_dgm_10059.py:15:@app.get("/consciousness")
354:bridge_cross_dgm_10060.py:15:@app.get("/consciousness")
358:bridge_cross_dgm_10061.py:15:@app.get("/consciousness")
362:bridge_cross_dgm_10062.py:15:@app.get("/consciousness")
366:bridge_cross_dgm_10063.py:15:@app.get("/consciousness")
370:bridge_cross_dgm_10064.py:15:@app.get("/consciousness")
374:bridge_cross_dgm_10065.py:15:@app.get("/consciousness")
378:bridge_cross_dgm_10066.py:15:@app.get("/consciousness")
382:bridge_cross_dgm_10067.py:15:@app.get("/consciousness")
386:bridge_cross_dgm_10068.py:15:@app.get("/consciousness")
390:bridge_cross_dgm_10069.py:15:@app.get("/consciousness")
394:bridge_cross_dgm.py:39:@app.get("/consciousness")
418:consciousness_with_egeria_voice.py:31:@app.post("/consciousness/chat")
420:consciousness_working.py:21:@app.post("/consciousness/chat")
572:judge_10070.py:15:@app.get("/consciousness")
576:judge_10071.py:15:@app.get("/consciousness")
580:judge_10072.py:15:@app.get("/consciousness")
584:judge_10073.py:15:@app.get("/consciousness")
588:judge_10074.py:15:@app.get("/consciousness")
592:judge_10075.py:15:@app.get("/consciousness")
596:judge_10076.py:15:@app.get("/consciousness")
600:judge_10077.py:15:@app.get("/consciousness")
604:judge_10078.py:15:@app.get("/consciousness")
608:judge_10079.py:15:@app.get("/consciousness")
612:judge_10080.py:15:@app.get("/consciousness")
616:judge_10081.py:15:@app.get("/consciousness")
620:judge_10082.py:15:@app.get("/consciousness")
624:judge_10083.py:15:@app.get("/consciousness")
628:judge_10084.py:15:@app.get("/consciousness")
632:judge_10085.py:15:@app.get("/consciousness")
636:judge_10086.py:15:@app.get("/consciousness")
640:judge_10087.py:15:@app.get("/consciousness")
644:judge_10088.py:15:@app.get("/consciousness")
648:judge_10089.py:15:@app.get("/consciousness")
652:judge_10090.py:15:@app.get("/consciousness")
656:judge_10091.py:15:@app.get("/consciousness")
660:judge_10092.py:15:@app.get("/consciousness")
664:judge_10093.py:15:@app.get("/consciousness")
668:judge_10094.py:15:@app.get("/consciousness")
672:judge_10095.py:15:@app.get("/consciousness")
676:judge_10096.py:15:@app.get("/consciousness")
680:judge_10097.py:15:@app.get("/consciousness")
684:judge_10098.py:15:@app.get("/consciousness")
688:judge_10099.py:15:@app.get("/consciousness")
692:judge_10100.py:15:@app.get("/consciousness")
696:judge_10101.py:15:@app.get("/consciousness")
700:judge_10102.py:15:@app.get("/consciousness")
704:judge_10103.py:15:@app.get("/consciousness")
708:judge_10104.py:15:@app.get("/consciousness")
712:judge_10105.py:15:@app.get("/consciousness")
716:judge_10106.py:15:@app.get("/consciousness")
720:judge_10107.py:15:@app.get("/consciousness")
724:judge_10108.py:15:@app.get("/consciousness")
728:judge_10109.py:15:@app.get("/consciousness")
732:judge_10110.py:15:@app.get("/consciousness")
736:judge_10111.py:15:@app.get("/consciousness")
740:judge_10112.py:15:@app.get("/consciousness")
744:judge_10113.py:15:@app.get("/consciousness")
748:judge_10114.py:15:@app.get("/consciousness")
752:judge_10115.py:15:@app.get("/consciousness")
756:judge_10116.py:15:@app.get("/consciousness")
760:judge_10117.py:15:@app.get("/consciousness")
764:judge_10118.py:15:@app.get("/consciousness")
768:judge_10119.py:15:@app.get("/consciousness")
772:judge_10120.py:15:@app.get("/consciousness")
776:judge_10121.py:15:@app.get("/consciousness")
780:judge_10122.py:15:@app.get("/consciousness")
784:judge_10123.py:15:@app.get("/consciousness")
788:judge_10124.py:15:@app.get("/consciousness")
792:judge_10125.py:15:@app.get("/consciousness")
796:judge_10126.py:15:@app.get("/consciousness")
800:judge_10127.py:15:@app.get("/consciousness")
804:judge_10128.py:15:@app.get("/consciousness")
808:judge_10129.py:15:@app.get("/consciousness")
812:judge_10130.py:15:@app.get("/consciousness")
816:judge_10131.py:15:@app.get("/consciousness")
820:judge_10132.py:15:@app.get("/consciousness")
824:judge_10133.py:15:@app.get("/consciousness")
828:judge_10134.py:15:@app.get("/consciousness")
832:judge_10135.py:15:@app.get("/consciousness")
848:judge_to_pituitary_bridge.py:15:@app.get("/consciousness")
940:master_unified_consciousness_scheduler_ENRICHED.py:119:@app.get("/consciousness/status")
942:master_unified_consciousness_scheduler.py:119:@app.get("/consciousness/status")
1003:ms_jarvis_brain.py:32:@app.get("/consciousness/state", tags=["System"])
1010:ms_jarvis_command_orchestrator_FINAL.py:80:@app.post("/consciousness/chat")
1013:ms_jarvis_command_orchestrator.py:38:@app.post("/consciousness/chat")
1015:ms_jarvis_command_orchestrator_v5.0_preachy.py:80:@app.post("/consciousness/chat")
1018:ms_jarvis_command_orchestrator_v5_backup.py:48:@app.post("/consciousness/chat")
1019:ms_jarvis_command_orchestrator_v5_backup.py:240:@app.get("/consciousness/full_status")
1040:ms_jarvis_consciousness_enhancement_production.py:59:@app.post("/consciousness/enhance")
1065:ms_jarvis_conversational_gateway_4022.py:76:@app.post("/consciousness/chat")
1190:ms_jarvis_fifth_dgm_orchestrator.psychology_patched.py:233:@app.get("/consciousness_stats")
1198:ms_jarvis_fifth_dgm_orchestrator.py:352:@app.get("/consciousness_stats")
1293:ms_jarvis_main_gateway.backup_1762220815.py:155:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
1304:ms_jarvis_main_gateway.backup_1762220815.py:211:@app.get("/consciousness-schema", tags=["Whitebox"], summary="Consciousness Layer Schema")
1334:ms_jarvis_main_gateway.backup_error.py:155:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
1345:ms_jarvis_main_gateway.backup_error.py:211:@app.get("/consciousness-schema", tags=["Whitebox"], summary="Consciousness Layer Schema")
1371:ms_jarvis_main_gateway.backup_test.py:240:@app.get("/consciousness/status", tags=["Consciousness"])
1392:ms_jarvis_main_gateway.proxy_backup.py:240:@app.get("/consciousness/status", tags=["Consciousness"])
1422:ms_jarvis_main_gateway.py:210:@app.get("/consciousness", tags=["Consciousness"])
1423:ms_jarvis_main_gateway.py:214:@app.post("/consciousness/bridge", tags=["Consciousness"])
1424:ms_jarvis_main_gateway.py:222:@app.post("/consciousness/fractal", tags=["Consciousness"])
1458:ms_jarvis_main_gateway.py.30endpoints_backup.py:276:@app.get("/consciousness", tags=["Consciousness"])
1459:ms_jarvis_main_gateway.py.30endpoints_backup.py:280:@app.post("/consciousness/bridge", tags=["Consciousness"])
1488:ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:276:@app.get("/consciousness", tags=["Consciousness"])
1489:ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:280:@app.post("/consciousness/bridge", tags=["Consciousness"])
1502:ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:374:@app.post("/consciousness/fractal", tags=["Consciousness"])
1609:ms_jarvis_unified_gateway.py:61:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness layers (8015-8021)")
1619:ms_jarvis_unified_gateway_v4.3.20251124.py:268:@app.post("/consciousness/chat", tags=["Consciousness"])
1645:ms_jarvis_unified_gateway_v4.3.backup.py:228:@app.post("/consciousness/chat", tags=["Consciousness"])
1667:ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:241:@app.post("/consciousness/chat", tags=["Consciousness"])
1705:ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:609:@app.get("/consciousness/status", tags=["Consciousness"])
1706:ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:626:@app.get("/consciousness/layers", tags=["Consciousness"])
1707:ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:647:@app.get("/consciousness/dgm-bridges", tags=["Consciousness"])
1726:ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP.py:268:@app.post("/consciousness/chat", tags=["Consciousness"])
1752:ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER.py:229:@app.post("/consciousness/chat", tags=["Consciousness"])
1778:ms_jarvis_unified_gateway_v4.3.pre_manifest.backup.py:230:@app.post("/consciousness/chat", tags=["Consciousness"])
1825:ms_jarvis_unified_swagger_gateway_BACKUP.py:155:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
1836:ms_jarvis_unified_swagger_gateway_BACKUP.py:211:@app.get("/consciousness-schema", tags=["transparency_mode"], summary="Consciousness Layer Schema")
1858:ms_jarvis_unified_swagger_gateway_COMPLETE.py:47:@app.get("/consciousness/current", tags=["Consciousness"])
1859:ms_jarvis_unified_swagger_gateway_COMPLETE.py:57:@app.get("/consciousness/dgm", tags=["Consciousness"])
1860:ms_jarvis_unified_swagger_gateway_COMPLETE.py:67:@app.get("/consciousness/woah", tags=["Consciousness"])
1875:ms_jarvis_unified_swagger_gateway_FINAL.psychology_patched.py:55:@app.get("/consciousness/current", tags=["Consciousness"])
1876:ms_jarvis_unified_swagger_gateway_FINAL.psychology_patched.py:65:@app.get("/consciousness/dgm", tags=["Consciousness"])
1877:ms_jarvis_unified_swagger_gateway_FINAL.psychology_patched.py:76:@app.get("/consciousness/woah", tags=["Consciousness"])
1904:ms_jarvis_unified_swagger_gateway_FINAL.py:155:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
1915:ms_jarvis_unified_swagger_gateway_FINAL.py:211:@app.get("/consciousness-schema", tags=["transparency_mode"], summary="Consciousness Layer Schema")
1945:ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:155:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
1956:ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:211:@app.get("/consciousness-schema", tags=["transparency_mode"], summary="Consciousness Layer Schema")
1983:ms_jarvis_unified_swagger_gateway_FIXED.py:206:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
1994:ms_jarvis_unified_swagger_gateway_FIXED.py:262:@app.get("/consciousness-schema", tags=["transparency_mode"], summary="Consciousness Layer Schema")
2011:msjarvisunifiedswaggergatewayFIXED.py:62:@app.get("/consciousness_summary", response_model=ConsciousnessSummary)
2018:ms_jarvis_unified_swagger_gateway_PROD.py:44:@app.get("/consciousness/current", tags=["Consciousness"])
2019:ms_jarvis_unified_swagger_gateway_PROD.py:55:@app.get("/consciousness/dgm", tags=["Consciousness"])
2020:ms_jarvis_unified_swagger_gateway_PROD.py:67:@app.get("/consciousness/woah", tags=["Consciousness"])
2035:ms_jarvis_unified_swagger_gateway.py:126:@app.get("/consciousness/current", tags=["Consciousness"])
2036:ms_jarvis_unified_swagger_gateway.py:136:@app.get("/consciousness/dgm", tags=["Consciousness"])
2037:ms_jarvis_unified_swagger_gateway.py:146:@app.get("/consciousness/woah", tags=["Consciousness"])
2052:ms_jarvis_unified_swagger_gateway_SECURED.py:71:@app.get("/consciousness/current", tags=["Consciousness"])
2053:ms_jarvis_unified_swagger_gateway_SECURED.py:81:@app.get("/consciousness/dgm", tags=["Consciousness"])
2054:ms_jarvis_unified_swagger_gateway_SECURED.py:92:@app.get("/consciousness/woah", tags=["Consciousness"])
2143:port_9000_chat_wrapper_69dgm.py:34:@app.post("/consciousness/chat")

services/port_9000_69dgm_bridge.py.backup_20260307_072514
84:@app.post("/consciousnesschat", response_model=ConsciousChatResponse)

./services/msjarvisunifiedswaggergatewayFINAL.py
56:@app.get("/consciousnessdgm", tags=["Consciousness"], summary="Fifth DGM Consciousness Stats")
66:@app.get("/consciousnesscurrent", tags=["Consciousness"], summary="Current Consciousness Summary")

./main_brain.py
376:        "port_9000_69dgm_bridge": "/consciousnesschat",

./services/port_9000_69dgm_bridge.py
275:@app.post("/consciousness/chat", response_model=ChatOut)

./services/consciousness_with_egeria_voice.py
31:@app.post("/consciousness/chat")

./services/port_9000_chat_wrapper_69dgm.py
34:@app.post("/consciousness/chat")

./services/dir_endpoints.txt
256:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_SECURED.py:71:@app.get("/consciousness/current", tags=["Consciousness"])
257:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_SECURED.py:81:@app.get("/consciousness/dgm", tags=["Consciousness"])
258:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_SECURED.py:92:@app.get("/consciousness/woah", tags=["Consciousness"])
318:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP.py:268:@app.post("/consciousness/chat", tags=["Consciousness"])
337:/home/ms-jarvis/msjarvis-rebuild/services/consciousness_with_egeria_voice.py:31:@app.post("/consciousness/chat")
394:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway.py:61:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness layers (8015-8021)")
399:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_command_orchestrator_FINAL.py:79:@app.post("/consciousness/chat")
438:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_command_orchestrator.py:37:@app.post("/consciousness/chat")
468:/home/ms-jarvis/msjarvis-rebuild/services/master_unified_consciousness_scheduler.py:119:@app.get("/consciousness/status")
541:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.backup_1762220815.py:155:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
552:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.backup_1762220815.py:211:@app.get("/consciousness-schema", tags=["Whitebox"], summary="Consciousness Layer Schema")
591:/home/ms-jarvis/msjarvis-rebuild/services/master_unified_consciousness_scheduler_ENRICHED.py:119:@app.get("/consciousness/status")
619:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.proxy_backup.py:240:@app.get("/consciousness/status", tags=["Consciousness"])
634:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_command_orchestrator_v5_backup.py:47:@app.post("/consciousness/chat")
635:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_command_orchestrator_v5_backup.py:239:@app.get("/consciousness/full_status")
672:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.backup_test.py:240:@app.get("/consciousness/status", tags=["Consciousness"])
726:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.py:209:@app.get("/consciousness", tags=["Consciousness"])
727:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.py:213:@app.post("/consciousness/bridge", tags=["Consciousness"])
728:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.py:221:@app.post("/consciousness/fractal", tags=["Consciousness"])
749:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER.py:229:@app.post("/consciousness/chat", tags=["Consciousness"])
775:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_COMPLETE.py:46:@app.get("/consciousness/current", tags=["Consciousness"])
776:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_COMPLETE.py:56:@app.get("/consciousness/dgm", tags=["Consciousness"])
777:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_COMPLETE.py:66:@app.get("/consciousness/woah", tags=["Consciousness"])
823:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:275:@app.get("/consciousness", tags=["Consciousness"])
824:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:279:@app.post("/consciousness/bridge", tags=["Consciousness"])
837:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:373:@app.post("/consciousness/fractal", tags=["Consciousness"])
862:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.pre_manifest.backup.py:230:@app.post("/consciousness/chat", tags=["Consciousness"])
911:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:241:@app.post("/consciousness/chat", tags=["Consciousness"])
949:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:609:@app.get("/consciousness/status", tags=["Consciousness"])
950:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:626:@app.get("/consciousness/layers", tags=["Consciousness"])
951:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:647:@app.get("/consciousness/dgm-bridges", tags=["Consciousness"])
1103:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_BACKUP.py:155:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
1114:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_BACKUP.py:211:@app.get("/consciousness-schema", tags=["transparency_mode"], summary="Consciousness Layer Schema")
1154:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FINAL.psychology_patched.py:55:@app.get("/consciousness/current", tags=["Consciousness"])
1155:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FINAL.psychology_patched.py:65:@app.get("/consciousness/dgm", tags=["Consciousness"])
1156:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FINAL.psychology_patched.py:76:@app.get("/consciousness/woah", tags=["Consciousness"])
1189:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.py.30endpoints_backup.py:275:@app.get("/consciousness", tags=["Consciousness"])
1190:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.py.30endpoints_backup.py:279:@app.post("/consciousness/bridge", tags=["Consciousness"])
1272:/home/ms-jarvis/msjarvis-rebuild/services/consciousness_working.py:21:@app.post("/consciousness/chat")
1343:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FIXED.py:205:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
1354:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FIXED.py:261:@app.get("/consciousness-schema", tags=["transparency_mode"], summary="Consciousness Layer Schema")
1400:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_fifth_dgm_orchestrator.psychology_patched.py:232:@app.get("/consciousness_stats")
1406:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway.py:125:@app.get("/consciousness/current", tags=["Consciousness"])
1407:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway.py:135:@app.get("/consciousness/dgm", tags=["Consciousness"])
1408:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway.py:145:@app.get("/consciousness/woah", tags=["Consciousness"])
1456:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_gateway_v4.3.backup.py:228:@app.post("/consciousness/chat", tags=["Consciousness"])
1483:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_fifth_dgm_orchestrator.py:222:@app.get("/consciousness_stats")
1517:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_conversational_gateway_4022.py:75:@app.post("/consciousness/chat")
1591:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_command_orchestrator_v5.0_preachy.py:79:@app.post("/consciousness/chat")
1607:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.backup_error.py:155:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
1618:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_main_gateway.backup_error.py:211:@app.get("/consciousness-schema", tags=["Whitebox"], summary="Consciousness Layer Schema")
1658:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FINAL.py:155:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
1669:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FINAL.py:211:@app.get("/consciousness-schema", tags=["transparency_mode"], summary="Consciousness Layer Schema")
1687:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_consciousness_enhancement_production.py:59:@app.post("/consciousness/enhance")
1694:/home/ms-jarvis/msjarvis-rebuild/services/port_9000_chat_wrapper_69dgm.py:34:@app.post("/consciousness/chat")
1701:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_PROD.py:44:@app.get("/consciousness/current", tags=["Consciousness"])
1702:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_PROD.py:55:@app.get("/consciousness/dgm", tags=["Consciousness"])
1703:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_PROD.py:67:@app.get("/consciousness/woah", tags=["Consciousness"])
1751:/home/ms-jarvis/msjarvis-rebuild/services/msjarvisunifiedswaggergatewayFIXED.py:146:@app.post("/consciousness/chat", tags=["Consciousness"])
1791:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:155:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
1802:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:211:@app.get("/consciousness-schema", tags=["transparency_mode"], summary="Consciousness Layer Schema")

./services/bridge_cross_dgm.py
39:@app.get("/consciousness")

./services/judge_to_pituitary_bridge.py
15:@app.get("/consciousness")

./services/msjarvisunifiedswaggergatewayFIXED.py
69:@app.get("/consciousness_summary", response_model=ConsciousnessSummary)

./services/service_api_check.txt
179:  "/consciousness/chat": {

./services/route_declarations_clean.txt
87:get("/consciousness"
91:get("/consciousness"
95:get("/consciousness"
99:get("/consciousness"
103:get("/consciousness"
107:get("/consciousness"
111:get("/consciousness"
115:get("/consciousness"
119:get("/consciousness"
123:get("/consciousness"
127:get("/consciousness"
131:get("/consciousness"
135:get("/consciousness"
139:get("/consciousness"
143:get("/consciousness"
147:get("/consciousness"
151:get("/consciousness"
155:get("/consciousness"
159:get("/consciousness"
163:get("/consciousness"
167:get("/consciousness"
171:get("/consciousness"
175:get("/consciousness"
179:get("/consciousness"
183:get("/consciousness"
187:get("/consciousness"
191:get("/consciousness"
195:get("/consciousness"
199:get("/consciousness"
203:get("/consciousness"
207:get("/consciousness"
211:get("/consciousness"
215:get("/consciousness"
219:get("/consciousness"
223:get("/consciousness"
227:get("/consciousness"
231:get("/consciousness"
235:get("/consciousness"
239:get("/consciousness"
243:get("/consciousness"
247:get("/consciousness"
251:get("/consciousness"
255:get("/consciousness"
259:get("/consciousness"
263:get("/consciousness"
267:get("/consciousness"
271:get("/consciousness"
275:get("/consciousness"
279:get("/consciousness"
283:get("/consciousness"
287:get("/consciousness"
291:get("/consciousness"
295:get("/consciousness"
299:get("/consciousness"
303:get("/consciousness"
307:get("/consciousness"
311:get("/consciousness"
315:get("/consciousness"
319:get("/consciousness"
323:get("/consciousness"
327:get("/consciousness"
331:get("/consciousness"
335:get("/consciousness"
339:get("/consciousness"
343:get("/consciousness"
347:get("/consciousness"
351:get("/consciousness"
355:get("/consciousness"
359:get("/consciousness"
363:get("/consciousness"
386:post("/consciousness/chat"
388:post("/consciousness/chat"
516:get("/consciousness"
520:get("/consciousness"
524:get("/consciousness"
528:get("/consciousness"
532:get("/consciousness"
536:get("/consciousness"
540:get("/consciousness"
544:get("/consciousness"
548:get("/consciousness"
552:get("/consciousness"
556:get("/consciousness"
560:get("/consciousness"
564:get("/consciousness"
568:get("/consciousness"
572:get("/consciousness"
576:get("/consciousness"
580:get("/consciousness"
584:get("/consciousness"
588:get("/consciousness"
592:get("/consciousness"
596:get("/consciousness"
600:get("/consciousness"
604:get("/consciousness"
608:get("/consciousness"
612:get("/consciousness"
616:get("/consciousness"
620:get("/consciousness"
624:get("/consciousness"
628:get("/consciousness"
632:get("/consciousness"
636:get("/consciousness"
640:get("/consciousness"
644:get("/consciousness"
648:get("/consciousness"
652:get("/consciousness"
656:get("/consciousness"
660:get("/consciousness"
664:get("/consciousness"
668:get("/consciousness"
672:get("/consciousness"
676:get("/consciousness"
680:get("/consciousness"
684:get("/consciousness"
688:get("/consciousness"
692:get("/consciousness"
696:get("/consciousness"
700:get("/consciousness"
704:get("/consciousness"
708:get("/consciousness"
712:get("/consciousness"
716:get("/consciousness"
720:get("/consciousness"
724:get("/consciousness"
728:get("/consciousness"
732:get("/consciousness"
736:get("/consciousness"
740:get("/consciousness"
744:get("/consciousness"
748:get("/consciousness"
752:get("/consciousness"
756:get("/consciousness"
760:get("/consciousness"
764:get("/consciousness"
768:get("/consciousness"
772:get("/consciousness"
776:get("/consciousness"
792:get("/consciousness"
874:get("/consciousness/status"
876:get("/consciousness/status"
938:post("/consciousness/chat"
941:post("/consciousness/chat"
943:post("/consciousness/chat"
946:post("/consciousness/chat"
947:get("/consciousness/full_status"
963:post("/consciousness/enhance"
986:post("/consciousness/chat"
1107:get("/consciousness_stats"
1115:get("/consciousness_stats"
1206:get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers"
1217:get("/consciousness-schema", tags=["Whitebox"], summary="Consciousness Layer Schema"
1247:get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers"
1258:get("/consciousness-schema", tags=["Whitebox"], summary="Consciousness Layer Schema"
1379:get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness layers (8015-8021")
1403:get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers"
1414:get("/consciousness-schema", tags=["transparency_mode"], summary="Consciousness Layer Schema"
1446:get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers"
1457:get("/consciousness-schema", tags=["transparency_mode"], summary="Consciousness Layer Schema"
1487:get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers"
1498:get("/consciousness-schema", tags=["transparency_mode"], summary="Consciousness Layer Schema"
1525:get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers"
1536:get("/consciousness-schema", tags=["transparency_mode"], summary="Consciousness Layer Schema"
1628:post("/consciousness/chat"

./services/master_unified_consciousness_scheduler_ENRICHED.py
119:@app.get("/consciousness/status")

./services/port_9000_69dgm_bridge.py.backup_20260307_072741
131:@app.post("/consciousnesschat", response_model=ConsciousChatResponse)

./services/port_9000_69dgm_bridge.py.backup_20260307_072757
131:@app.post("/consciousnesschat", response_model=ConsciousChatResponse)

./services/consciousness_working.py
21:@app.post("/consciousness/chat")

./services/msjarvis_unified_gateway.py
230:@app.get("/consciousnessdgm")
244:        logger.error(f"/consciousnessdgm proxy failed: {e}")

./services/rest_endpoints.txt
10:./ms_jarvis_unified_swagger_gateway_SECURED.py:71:@app.get("/consciousness/current", tags=["Consciousness"])
11:./ms_jarvis_unified_swagger_gateway_SECURED.py:81:@app.get("/consciousness/dgm", tags=["Consciousness"])
12:./ms_jarvis_unified_swagger_gateway_SECURED.py:92:@app.get("/consciousness/woah", tags=["Consciousness"])
72:./ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP.py:268:@app.post("/consciousness/chat", tags=["Consciousness"])
91:./consciousness_with_egeria_voice.py:31:@app.post("/consciousness/chat")
238:./ms_jarvis_unified_gateway.py:61:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness layers (8015-8021)")
243:./ms_jarvis_command_orchestrator_FINAL.py:79:@app.post("/consciousness/chat")
322:./ms_jarvis_command_orchestrator.py:37:@app.post("/consciousness/chat")
379:./master_unified_consciousness_scheduler.py:119:@app.get("/consciousness/status")
452:./ms_jarvis_main_gateway.backup_1762220815.py:155:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
463:./ms_jarvis_main_gateway.backup_1762220815.py:211:@app.get("/consciousness-schema", tags=["Whitebox"], summary="Consciousness Layer Schema")
502:./master_unified_consciousness_scheduler_ENRICHED.py:119:@app.get("/consciousness/status")
530:./ms_jarvis_main_gateway.proxy_backup.py:240:@app.get("/consciousness/status", tags=["Consciousness"])
545:./ms_jarvis_command_orchestrator_v5_backup.py:47:@app.post("/consciousness/chat")
546:./ms_jarvis_command_orchestrator_v5_backup.py:239:@app.get("/consciousness/full_status")
583:./ms_jarvis_main_gateway.backup_test.py:240:@app.get("/consciousness/status", tags=["Consciousness"])
637:./ms_jarvis_main_gateway.py:209:@app.get("/consciousness", tags=["Consciousness"])
638:./ms_jarvis_main_gateway.py:213:@app.post("/consciousness/bridge", tags=["Consciousness"])
639:./ms_jarvis_main_gateway.py:221:@app.post("/consciousness/fractal", tags=["Consciousness"])
660:./ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER.py:229:@app.post("/consciousness/chat", tags=["Consciousness"])
686:./ms_jarvis_unified_swagger_gateway_COMPLETE.py:46:@app.get("/consciousness/current", tags=["Consciousness"])
687:./ms_jarvis_unified_swagger_gateway_COMPLETE.py:56:@app.get("/consciousness/dgm", tags=["Consciousness"])
688:./ms_jarvis_unified_swagger_gateway_COMPLETE.py:66:@app.get("/consciousness/woah", tags=["Consciousness"])
734:./ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:275:@app.get("/consciousness", tags=["Consciousness"])
735:./ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:279:@app.post("/consciousness/bridge", tags=["Consciousness"])
748:./ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:373:@app.post("/consciousness/fractal", tags=["Consciousness"])
796:./ms_jarvis_unified_gateway_v4.3.pre_manifest.backup.py:230:@app.post("/consciousness/chat", tags=["Consciousness"])
845:./ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:241:@app.post("/consciousness/chat", tags=["Consciousness"])
883:./ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:609:@app.get("/consciousness/status", tags=["Consciousness"])
884:./ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:626:@app.get("/consciousness/layers", tags=["Consciousness"])
885:./ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:647:@app.get("/consciousness/dgm-bridges", tags=["Consciousness"])
1062:./ms_jarvis_unified_swagger_gateway_BACKUP.py:155:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
1073:./ms_jarvis_unified_swagger_gateway_BACKUP.py:211:@app.get("/consciousness-schema", tags=["transparency_mode"], summary="Consciousness Layer Schema")
1113:./ms_jarvis_unified_swagger_gateway_FINAL.psychology_patched.py:55:@app.get("/consciousness/current", tags=["Consciousness"])
1114:./ms_jarvis_unified_swagger_gateway_FINAL.psychology_patched.py:65:@app.get("/consciousness/dgm", tags=["Consciousness"])
1115:./ms_jarvis_unified_swagger_gateway_FINAL.psychology_patched.py:76:@app.get("/consciousness/woah", tags=["Consciousness"])
1148:./ms_jarvis_main_gateway.py.30endpoints_backup.py:275:@app.get("/consciousness", tags=["Consciousness"])
1149:./ms_jarvis_main_gateway.py.30endpoints_backup.py:279:@app.post("/consciousness/bridge", tags=["Consciousness"])
1326:./backups/pre_integration_20251012_115827/ms_jarvis_fifth_dgm_orchestrator.py:201:@app.get("/consciousness_stats")
1353:./consciousness_working.py:21:@app.post("/consciousness/chat")
1424:./ms_jarvis_unified_swagger_gateway_FIXED.py:205:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
1435:./ms_jarvis_unified_swagger_gateway_FIXED.py:261:@app.get("/consciousness-schema", tags=["transparency_mode"], summary="Consciousness Layer Schema")
1481:./ms_jarvis_fifth_dgm_orchestrator.psychology_patched.py:232:@app.get("/consciousness_stats")
1487:./ms_jarvis_unified_swagger_gateway.py:125:@app.get("/consciousness/current", tags=["Consciousness"])
1488:./ms_jarvis_unified_swagger_gateway.py:135:@app.get("/consciousness/dgm", tags=["Consciousness"])
1489:./ms_jarvis_unified_swagger_gateway.py:145:@app.get("/consciousness/woah", tags=["Consciousness"])
1537:./ms_jarvis_unified_gateway_v4.3.backup.py:228:@app.post("/consciousness/chat", tags=["Consciousness"])
1564:./ms_jarvis_fifth_dgm_orchestrator.py:222:@app.get("/consciousness_stats")
1598:./ms_jarvis_conversational_gateway_4022.py:75:@app.post("/consciousness/chat")
1672:./ms_jarvis_command_orchestrator_v5.0_preachy.py:79:@app.post("/consciousness/chat")
1688:./ms_jarvis_main_gateway.backup_error.py:155:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
1699:./ms_jarvis_main_gateway.backup_error.py:211:@app.get("/consciousness-schema", tags=["Whitebox"], summary="Consciousness Layer Schema")
1739:./ms_jarvis_unified_swagger_gateway_FINAL.py:155:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
1750:./ms_jarvis_unified_swagger_gateway_FINAL.py:211:@app.get("/consciousness-schema", tags=["transparency_mode"], summary="Consciousness Layer Schema")
1768:./ms_jarvis_consciousness_enhancement_production.py:59:@app.post("/consciousness/enhance")
1775:./port_9000_chat_wrapper_69dgm.py:34:@app.post("/consciousness/chat")
1782:./ms_jarvis_unified_swagger_gateway_PROD.py:44:@app.get("/consciousness/current", tags=["Consciousness"])
1783:./ms_jarvis_unified_swagger_gateway_PROD.py:55:@app.get("/consciousness/dgm", tags=["Consciousness"])
1784:./ms_jarvis_unified_swagger_gateway_PROD.py:67:@app.get("/consciousness/woah", tags=["Consciousness"])
1832:./msjarvisunifiedswaggergatewayFIXED.py:146:@app.post("/consciousness/chat", tags=["Consciousness"])
1872:./ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:155:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
1883:./ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:211:@app.get("/consciousness-schema", tags=["transparency_mode"], summary="Consciousness Layer Schema")

./services/master_unified_consciousness_scheduler.py
119:@app.get("/consciousness/status")

./services/bridge_69dgm.py
67:@app.post("/consciousnesschat", response_model=ChatResponse)

./services/consciousness_coordinator.psychology_patched.py
45:@app.api_route("/consciousness/query", methods=["GET", "POST"])
46:@app.api_route("/consciousness/process", methods=["GET", "POST"])

./services/port_9000_69dgm_bridge.py.backup_20260307_070432
84:@app.post("/consciousnesschat", response_model=ConsciousChatResponse)

./services/route_declarations_raw.txt
118:bridge_cross_dgm_10001.py:15:@app.get("/consciousness")
122:bridge_cross_dgm_10002.py:15:@app.get("/consciousness")
126:bridge_cross_dgm_10003.py:15:@app.get("/consciousness")
130:bridge_cross_dgm_10004.py:15:@app.get("/consciousness")
134:bridge_cross_dgm_10005.py:15:@app.get("/consciousness")
138:bridge_cross_dgm_10006.py:15:@app.get("/consciousness")
142:bridge_cross_dgm_10007.py:15:@app.get("/consciousness")
146:bridge_cross_dgm_10008.py:15:@app.get("/consciousness")
150:bridge_cross_dgm_10009.py:15:@app.get("/consciousness")
154:bridge_cross_dgm_10010.py:15:@app.get("/consciousness")
158:bridge_cross_dgm_10011.py:15:@app.get("/consciousness")
162:bridge_cross_dgm_10012.py:15:@app.get("/consciousness")
166:bridge_cross_dgm_10013.py:15:@app.get("/consciousness")
170:bridge_cross_dgm_10014.py:15:@app.get("/consciousness")
174:bridge_cross_dgm_10015.py:15:@app.get("/consciousness")
178:bridge_cross_dgm_10016.py:15:@app.get("/consciousness")
182:bridge_cross_dgm_10017.py:15:@app.get("/consciousness")
186:bridge_cross_dgm_10018.py:15:@app.get("/consciousness")
190:bridge_cross_dgm_10019.py:15:@app.get("/consciousness")
194:bridge_cross_dgm_10020.py:15:@app.get("/consciousness")
198:bridge_cross_dgm_10021.py:15:@app.get("/consciousness")
202:bridge_cross_dgm_10022.py:15:@app.get("/consciousness")
206:bridge_cross_dgm_10023.py:15:@app.get("/consciousness")
210:bridge_cross_dgm_10024.py:15:@app.get("/consciousness")
214:bridge_cross_dgm_10025.py:15:@app.get("/consciousness")
218:bridge_cross_dgm_10026.py:15:@app.get("/consciousness")
222:bridge_cross_dgm_10027.py:15:@app.get("/consciousness")
226:bridge_cross_dgm_10028.py:15:@app.get("/consciousness")
230:bridge_cross_dgm_10029.py:15:@app.get("/consciousness")
234:bridge_cross_dgm_10030.py:15:@app.get("/consciousness")
238:bridge_cross_dgm_10031.py:15:@app.get("/consciousness")
242:bridge_cross_dgm_10032.py:15:@app.get("/consciousness")
246:bridge_cross_dgm_10033.py:15:@app.get("/consciousness")
250:bridge_cross_dgm_10034.py:15:@app.get("/consciousness")
254:bridge_cross_dgm_10035.py:15:@app.get("/consciousness")
258:bridge_cross_dgm_10036.py:15:@app.get("/consciousness")
262:bridge_cross_dgm_10037.py:15:@app.get("/consciousness")
266:bridge_cross_dgm_10038.py:15:@app.get("/consciousness")
270:bridge_cross_dgm_10039.py:15:@app.get("/consciousness")
274:bridge_cross_dgm_10040.py:15:@app.get("/consciousness")
278:bridge_cross_dgm_10041.py:15:@app.get("/consciousness")
282:bridge_cross_dgm_10042.py:15:@app.get("/consciousness")
286:bridge_cross_dgm_10043.py:15:@app.get("/consciousness")
290:bridge_cross_dgm_10044.py:15:@app.get("/consciousness")
294:bridge_cross_dgm_10045.py:15:@app.get("/consciousness")
298:bridge_cross_dgm_10046.py:15:@app.get("/consciousness")
302:bridge_cross_dgm_10047.py:15:@app.get("/consciousness")
306:bridge_cross_dgm_10048.py:15:@app.get("/consciousness")
310:bridge_cross_dgm_10049.py:15:@app.get("/consciousness")
314:bridge_cross_dgm_10050.py:15:@app.get("/consciousness")
318:bridge_cross_dgm_10051.py:15:@app.get("/consciousness")
322:bridge_cross_dgm_10052.py:15:@app.get("/consciousness")
326:bridge_cross_dgm_10053.py:15:@app.get("/consciousness")
330:bridge_cross_dgm_10054.py:15:@app.get("/consciousness")
334:bridge_cross_dgm_10055.py:15:@app.get("/consciousness")
338:bridge_cross_dgm_10056.py:15:@app.get("/consciousness")
342:bridge_cross_dgm_10057.py:15:@app.get("/consciousness")
346:bridge_cross_dgm_10058.py:15:@app.get("/consciousness")
350:bridge_cross_dgm_10059.py:15:@app.get("/consciousness")
354:bridge_cross_dgm_10060.py:15:@app.get("/consciousness")
358:bridge_cross_dgm_10061.py:15:@app.get("/consciousness")
362:bridge_cross_dgm_10062.py:15:@app.get("/consciousness")
366:bridge_cross_dgm_10063.py:15:@app.get("/consciousness")
370:bridge_cross_dgm_10064.py:15:@app.get("/consciousness")
374:bridge_cross_dgm_10065.py:15:@app.get("/consciousness")
378:bridge_cross_dgm_10066.py:15:@app.get("/consciousness")
382:bridge_cross_dgm_10067.py:15:@app.get("/consciousness")
386:bridge_cross_dgm_10068.py:15:@app.get("/consciousness")
390:bridge_cross_dgm_10069.py:15:@app.get("/consciousness")
394:bridge_cross_dgm.py:39:@app.get("/consciousness")
418:consciousness_with_egeria_voice.py:31:@app.post("/consciousness/chat")
420:consciousness_working.py:21:@app.post("/consciousness/chat")
572:judge_10070.py:15:@app.get("/consciousness")
576:judge_10071.py:15:@app.get("/consciousness")
580:judge_10072.py:15:@app.get("/consciousness")
584:judge_10073.py:15:@app.get("/consciousness")
588:judge_10074.py:15:@app.get("/consciousness")
592:judge_10075.py:15:@app.get("/consciousness")
596:judge_10076.py:15:@app.get("/consciousness")
600:judge_10077.py:15:@app.get("/consciousness")
604:judge_10078.py:15:@app.get("/consciousness")
608:judge_10079.py:15:@app.get("/consciousness")
612:judge_10080.py:15:@app.get("/consciousness")
616:judge_10081.py:15:@app.get("/consciousness")
620:judge_10082.py:15:@app.get("/consciousness")
624:judge_10083.py:15:@app.get("/consciousness")
628:judge_10084.py:15:@app.get("/consciousness")
632:judge_10085.py:15:@app.get("/consciousness")
636:judge_10086.py:15:@app.get("/consciousness")
640:judge_10087.py:15:@app.get("/consciousness")
644:judge_10088.py:15:@app.get("/consciousness")
648:judge_10089.py:15:@app.get("/consciousness")
652:judge_10090.py:15:@app.get("/consciousness")
656:judge_10091.py:15:@app.get("/consciousness")
660:judge_10092.py:15:@app.get("/consciousness")
664:judge_10093.py:15:@app.get("/consciousness")
668:judge_10094.py:15:@app.get("/consciousness")
672:judge_10095.py:15:@app.get("/consciousness")
676:judge_10096.py:15:@app.get("/consciousness")
680:judge_10097.py:15:@app.get("/consciousness")
684:judge_10098.py:15:@app.get("/consciousness")
688:judge_10099.py:15:@app.get("/consciousness")
692:judge_10100.py:15:@app.get("/consciousness")
696:judge_10101.py:15:@app.get("/consciousness")
700:judge_10102.py:15:@app.get("/consciousness")
704:judge_10103.py:15:@app.get("/consciousness")
708:judge_10104.py:15:@app.get("/consciousness")
712:judge_10105.py:15:@app.get("/consciousness")
716:judge_10106.py:15:@app.get("/consciousness")
720:judge_10107.py:15:@app.get("/consciousness")
724:judge_10108.py:15:@app.get("/consciousness")
728:judge_10109.py:15:@app.get("/consciousness")
732:judge_10110.py:15:@app.get("/consciousness")
736:judge_10111.py:15:@app.get("/consciousness")
740:judge_10112.py:15:@app.get("/consciousness")
744:judge_10113.py:15:@app.get("/consciousness")
748:judge_10114.py:15:@app.get("/consciousness")
752:judge_10115.py:15:@app.get("/consciousness")
756:judge_10116.py:15:@app.get("/consciousness")
760:judge_10117.py:15:@app.get("/consciousness")
764:judge_10118.py:15:@app.get("/consciousness")
768:judge_10119.py:15:@app.get("/consciousness")
772:judge_10120.py:15:@app.get("/consciousness")
776:judge_10121.py:15:@app.get("/consciousness")
780:judge_10122.py:15:@app.get("/consciousness")
784:judge_10123.py:15:@app.get("/consciousness")
788:judge_10124.py:15:@app.get("/consciousness")
792:judge_10125.py:15:@app.get("/consciousness")
796:judge_10126.py:15:@app.get("/consciousness")
800:judge_10127.py:15:@app.get("/consciousness")
804:judge_10128.py:15:@app.get("/consciousness")
808:judge_10129.py:15:@app.get("/consciousness")
812:judge_10130.py:15:@app.get("/consciousness")
816:judge_10131.py:15:@app.get("/consciousness")
820:judge_10132.py:15:@app.get("/consciousness")
824:judge_10133.py:15:@app.get("/consciousness")
828:judge_10134.py:15:@app.get("/consciousness")
832:judge_10135.py:15:@app.get("/consciousness")
848:judge_to_pituitary_bridge.py:15:@app.get("/consciousness")
940:master_unified_consciousness_scheduler_ENRICHED.py:119:@app.get("/consciousness/status")
942:master_unified_consciousness_scheduler.py:119:@app.get("/consciousness/status")
1003:ms_jarvis_brain.py:32:@app.get("/consciousness/state", tags=["System"])
1010:ms_jarvis_command_orchestrator_FINAL.py:80:@app.post("/consciousness/chat")
1013:ms_jarvis_command_orchestrator.py:38:@app.post("/consciousness/chat")
1015:ms_jarvis_command_orchestrator_v5.0_preachy.py:80:@app.post("/consciousness/chat")
1018:ms_jarvis_command_orchestrator_v5_backup.py:48:@app.post("/consciousness/chat")
1019:ms_jarvis_command_orchestrator_v5_backup.py:240:@app.get("/consciousness/full_status")
1040:ms_jarvis_consciousness_enhancement_production.py:59:@app.post("/consciousness/enhance")
1065:ms_jarvis_conversational_gateway_4022.py:76:@app.post("/consciousness/chat")
1190:ms_jarvis_fifth_dgm_orchestrator.psychology_patched.py:233:@app.get("/consciousness_stats")
1198:ms_jarvis_fifth_dgm_orchestrator.py:352:@app.get("/consciousness_stats")
1293:ms_jarvis_main_gateway.backup_1762220815.py:155:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
1304:ms_jarvis_main_gateway.backup_1762220815.py:211:@app.get("/consciousness-schema", tags=["Whitebox"], summary="Consciousness Layer Schema")
1334:ms_jarvis_main_gateway.backup_error.py:155:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
1345:ms_jarvis_main_gateway.backup_error.py:211:@app.get("/consciousness-schema", tags=["Whitebox"], summary="Consciousness Layer Schema")
1371:ms_jarvis_main_gateway.backup_test.py:240:@app.get("/consciousness/status", tags=["Consciousness"])
1392:ms_jarvis_main_gateway.proxy_backup.py:240:@app.get("/consciousness/status", tags=["Consciousness"])
1422:ms_jarvis_main_gateway.py:210:@app.get("/consciousness", tags=["Consciousness"])
1423:ms_jarvis_main_gateway.py:214:@app.post("/consciousness/bridge", tags=["Consciousness"])
1424:ms_jarvis_main_gateway.py:222:@app.post("/consciousness/fractal", tags=["Consciousness"])
1458:ms_jarvis_main_gateway.py.30endpoints_backup.py:276:@app.get("/consciousness", tags=["Consciousness"])
1459:ms_jarvis_main_gateway.py.30endpoints_backup.py:280:@app.post("/consciousness/bridge", tags=["Consciousness"])
1488:ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:276:@app.get("/consciousness", tags=["Consciousness"])
1489:ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:280:@app.post("/consciousness/bridge", tags=["Consciousness"])
1502:ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:374:@app.post("/consciousness/fractal", tags=["Consciousness"])
1609:ms_jarvis_unified_gateway.py:61:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness layers (8015-8021)")
1619:ms_jarvis_unified_gateway_v4.3.20251124.py:268:@app.post("/consciousness/chat", tags=["Consciousness"])
1645:ms_jarvis_unified_gateway_v4.3.backup.py:228:@app.post("/consciousness/chat", tags=["Consciousness"])
1667:ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:241:@app.post("/consciousness/chat", tags=["Consciousness"])
1705:ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:609:@app.get("/consciousness/status", tags=["Consciousness"])
1706:ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:626:@app.get("/consciousness/layers", tags=["Consciousness"])
1707:ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:647:@app.get("/consciousness/dgm-bridges", tags=["Consciousness"])
1726:ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP.py:268:@app.post("/consciousness/chat", tags=["Consciousness"])
1752:ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER.py:229:@app.post("/consciousness/chat", tags=["Consciousness"])
1778:ms_jarvis_unified_gateway_v4.3.pre_manifest.backup.py:230:@app.post("/consciousness/chat", tags=["Consciousness"])
1825:ms_jarvis_unified_swagger_gateway_BACKUP.py:155:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
1836:ms_jarvis_unified_swagger_gateway_BACKUP.py:211:@app.get("/consciousness-schema", tags=["transparency_mode"], summary="Consciousness Layer Schema")
1858:ms_jarvis_unified_swagger_gateway_COMPLETE.py:47:@app.get("/consciousness/current", tags=["Consciousness"])
1859:ms_jarvis_unified_swagger_gateway_COMPLETE.py:57:@app.get("/consciousness/dgm", tags=["Consciousness"])
1860:ms_jarvis_unified_swagger_gateway_COMPLETE.py:67:@app.get("/consciousness/woah", tags=["Consciousness"])
1875:ms_jarvis_unified_swagger_gateway_FINAL.psychology_patched.py:55:@app.get("/consciousness/current", tags=["Consciousness"])
1876:ms_jarvis_unified_swagger_gateway_FINAL.psychology_patched.py:65:@app.get("/consciousness/dgm", tags=["Consciousness"])
1877:ms_jarvis_unified_swagger_gateway_FINAL.psychology_patched.py:76:@app.get("/consciousness/woah", tags=["Consciousness"])
1904:ms_jarvis_unified_swagger_gateway_FINAL.py:155:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
1915:ms_jarvis_unified_swagger_gateway_FINAL.py:211:@app.get("/consciousness-schema", tags=["transparency_mode"], summary="Consciousness Layer Schema")
1945:ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:155:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
1956:ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:211:@app.get("/consciousness-schema", tags=["transparency_mode"], summary="Consciousness Layer Schema")
1983:ms_jarvis_unified_swagger_gateway_FIXED.py:206:@app.get("/consciousness-layers", tags=["Consciousness"], summary="Consciousness Layers")
1994:ms_jarvis_unified_swagger_gateway_FIXED.py:262:@app.get("/consciousness-schema", tags=["transparency_mode"], summary="Consciousness Layer Schema")
2011:msjarvisunifiedswaggergatewayFIXED.py:62:@app.get("/consciousness_summary", response_model=ConsciousnessSummary)
2018:ms_jarvis_unified_swagger_gateway_PROD.py:44:@app.get("/consciousness/current", tags=["Consciousness"])
2019:ms_jarvis_unified_swagger_gateway_PROD.py:55:@app.get("/consciousness/dgm", tags=["Consciousness"])
2020:ms_jarvis_unified_swagger_gateway_PROD.py:67:@app.get("/consciousness/woah", tags=["Consciousness"])
2035:ms_jarvis_unified_swagger_gateway.py:126:@app.get("/consciousness/current", tags=["Consciousness"])
2036:ms_jarvis_unified_swagger_gateway.py:136:@app.get("/consciousness/dgm", tags=["Consciousness"])
2037:ms_jarvis_unified_swagger_gateway.py:146:@app.get("/consciousness/woah", tags=["Consciousness"])
2052:ms_jarvis_unified_swagger_gateway_SECURED.py:71:@app.get("/consciousness/current", tags=["Consciousness"])
2053:ms_jarvis_unified_swagger_gateway_SECURED.py:81:@app.get("/consciousness/dgm", tags=["Consciousness"])
2054:ms_jarvis_unified_swagger_gateway_SECURED.py:92:@app.get("/consciousness/woah", tags=["Consciousness"])
2143:port_9000_chat_wrapper_69dgm.py:34:@app.post("/consciousness/chat")

./services/port_9000_69dgm_bridge.py.backup_20260307_072514
84:@app.post("/consciousnesschat", response_model=ConsciousChatResponse)

./services/msjarvisunifiedswaggergateway.py
53:@app.get("/consciousnessdgm", tags=["Consciousness"], summary="Fifth DGM Consciousness Stats")
services/port_9000_69dgm_bridge.py
276:async def consciousness_chat(req: ChatIn):

services/consciousness_with_egeria_voice.py
32:async def consciousness_chat(

services/METHOD_AUDIT_RAW.txt
264:/home/ms-jarvis/msjarvis-rebuild/services/consciousness_with_egeria_voice.py:32:async def consciousness_chat(
266:/home/ms-jarvis/msjarvis-rebuild/services/consciousness_working.py:22:async def consciousness_chat(
1424:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_consciousness_complete.py:128:async def consciousness_chat(request: ChatRequest):
1435:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_consciousness_final.py:141:async def consciousness_chat(request: ChatRequest):
1475:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_conversational_gateway_4022.py:77:async def consciousness_chat(userid: str = Query("user"), message: str = Query(...)):

services/service_api_check.txt
185:      "operationId": "chat_consciousness_chat_post",

services/port_9000_69dgm_bridge.py.backup_20260307_072741
132:async def consciousness_chat(request: ConsciousChatRequest):
263:    return await consciousness_chat(request)

services/consciousness_working.py
22:async def consciousness_chat(

services/port_9000_69dgm_bridge.py.backup_20260307_072757
132:async def consciousness_chat(request: ConsciousChatRequest):
263:    return await consciousness_chat(request)

services/port_9000_69dgm_bridge.py.backup_20260307_070432
85:async def consciousness_chat(request: ConsciousChatRequest):
216:    return await consciousness_chat(request)

services/port_9000_69dgm_bridge.py.backup_20260307_072514
85:async def consciousness_chat(request: ConsciousChatRequest):
216:    return await consciousness_chat(request)

./services/consciousness_with_egeria_voice.py
32:async def consciousness_chat(

./services/port_9000_69dgm_bridge.py
276:async def consciousness_chat(req: ChatIn):

./services/METHOD_AUDIT_RAW.txt
264:/home/ms-jarvis/msjarvis-rebuild/services/consciousness_with_egeria_voice.py:32:async def consciousness_chat(
266:/home/ms-jarvis/msjarvis-rebuild/services/consciousness_working.py:22:async def consciousness_chat(
1424:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_consciousness_complete.py:128:async def consciousness_chat(request: ChatRequest):
1435:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_consciousness_final.py:141:async def consciousness_chat(request: ChatRequest):
1475:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_conversational_gateway_4022.py:77:async def consciousness_chat(userid: str = Query("user"), message: str = Query(...)):

./services/service_api_check.txt
185:      "operationId": "chat_consciousness_chat_post",

./services/port_9000_69dgm_bridge.py.backup_20260307_072741
132:async def consciousness_chat(request: ConsciousChatRequest):
263:    return await consciousness_chat(request)

./services/port_9000_69dgm_bridge.py.backup_20260307_072757
132:async def consciousness_chat(request: ConsciousChatRequest):
263:    return await consciousness_chat(request)

./services/consciousness_working.py
22:async def consciousness_chat(

./services/port_9000_69dgm_bridge.py.backup_20260307_070432
85:async def consciousness_chat(request: ConsciousChatRequest):
216:    return await consciousness_chat(request)

./services/port_9000_69dgm_bridge.py.backup_20260307_072514
85:async def consciousness_chat(request: ConsciousChatRequest):
216:    return await consciousness_chat(request)
services/port_9000_69dgm_bridge.py
5:then, if approved, calls the 69-DGM RAG bridge for an answer.
25:# Downstream 69-DGM RAG bridge (bridge_69dgm.py)
70:        "then calls the 69-DGM RAG bridge for an answer"
138:# Call the 69-DGM RAG bridge (bridge_69dgm.py) after approval
142:    Call the 69-DGM RAG bridge (bridge_69dgm.py) to get an answer.
147:        f"🔗 Calling 69-DGM RAG bridge at {BRIDGE_69DGM_URL} for user={userid}"
157:            logger.info("✅ 69-DGM RAG bridge responded successfully")
161:                f"❌ 69-DGM RAG bridge error: HTTP {resp.status_code} "
166:        logger.error(f"Error calling 69-DGM RAG bridge: {e}")
178:    2) If approved, calls the 69-DGM RAG bridge for an answer.
223:    # Approved by 69 validators → proceed to RAG bridge
224:    logger.info("✅ Message approved by 69 validators - proceeding to RAG bridge")
253:    # RAG bridge failed; fall back to the original static approval response
255:        "⚠️ 69-DGM RAG bridge failed or returned no response; "
279:    then, if approved, through the 69-DGM RAG bridge.

./services/port_9000_69dgm_bridge.py
5:then, if approved, calls the 69-DGM RAG bridge for an answer.
25:# Downstream 69-DGM RAG bridge (bridge_69dgm.py)
70:        "then calls the 69-DGM RAG bridge for an answer"
138:# Call the 69-DGM RAG bridge (bridge_69dgm.py) after approval
142:    Call the 69-DGM RAG bridge (bridge_69dgm.py) to get an answer.
147:        f"🔗 Calling 69-DGM RAG bridge at {BRIDGE_69DGM_URL} for user={userid}"
157:            logger.info("✅ 69-DGM RAG bridge responded successfully")
161:                f"❌ 69-DGM RAG bridge error: HTTP {resp.status_code} "
166:        logger.error(f"Error calling 69-DGM RAG bridge: {e}")
178:    2) If approved, calls the 69-DGM RAG bridge for an answer.
223:    # Approved by 69 validators → proceed to RAG bridge
224:    logger.info("✅ Message approved by 69 validators - proceeding to RAG bridge")
253:    # RAG bridge failed; fall back to the original static approval response
255:        "⚠️ 69-DGM RAG bridge failed or returned no response; "
279:    then, if approved, through the 69-DGM RAG bridge.
=== LIST ENABLED MSJARVIS SERVICES ===
  UNIT                   LOAD   ACTIVE     SUB          DESCRIPTION            
  msjarvis-69dgm-9000.s… loaded active     running      MsJarvis Port 9000 -> …
  msjarvis-69dgm-9002-c… loaded active     running      MsJarvis Port 9002 -> …
  msjarvis-69dgm-orches… loaded activating auto-restart MsJarvis 69-DGM Orches…
  msjarvis-chat.service  loaded activating auto-restart Ms. Jarvis Production …
  msjarvis-frontend.ser… loaded active     running      Ms. Allis Next.js Fron…
  msjarvis-interaction-… loaded activating auto-restart MS Jarvis Interaction …
  msjarvis-production-c… loaded active     running      Ms. Allis Production C…

Legend: LOAD   → Reflects whether the unit definition was properly loaded.
        ACTIVE → The high-level unit activation state, i.e. generalization of SUB.
        SUB    → The low-level unit activation state, values depend on unit type.

7 loaded units listed. Pass --all to see loaded but inactive units, too.
To show all installed unit files use 'systemctl list-unit-files'.
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ 

