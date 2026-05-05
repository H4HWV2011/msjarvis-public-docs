(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ # Find the actual running postgres containers
docker ps --format "table {{.Names}}\t{{.Image}}\t{{.Status}}" | grep -iE "postgres|db|data"
jarvis-gis-db                                           postgis/postgis:15-3.4                                Up 4 hours
jarvis-chroma                                           chromadb/chroma:latest                                Up 8 hours (healthy)
chromadb                                                chromadb/chroma:latest                                Up 11 days
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ docker ps --format "table {{.Names}}\t{{.Image}}\t{{.Ports}}"
NAMES                                                   IMAGE                                                 PORTS
jarvis-gis-db                                           postgis/postgis:15-3.4                                127.0.0.1:5435->5432/tcp
jarvis-local-resources                                  msjarvis-rebuild-jarvis-local-resources               127.0.0.1:8006->8006/tcp, 8035/tcp
jarvis-gis-rag                                          msjarvis-rebuild-jarvis-gis-rag                       127.0.0.1:8004->8004/tcp, 8044/tcp
jarvis-chroma                                           chromadb/chroma:latest                                127.0.0.1:8002->8000/tcp
jarvis-stewardship-scheduler                            msjarvis-rebuild-jarvis-stewardship-scheduler         127.0.0.1:8079->8079/tcp
jarvis-steward                                          msjarvis-rebuild-jarvis-steward                       127.0.0.1:8051->8060/tcp
jarvis-unified-gateway                                  msjarvis-rebuild-jarvis-unified-gateway               127.0.0.1:18018->8001/tcp
jarvis-confidence-decay                                 msjarvis-rebuild-jarvis-confidence-decay              
jarvis-main-brain                                       msjarvis-rebuild-jarvis-main-brain                    127.0.0.1:8050->8050/tcp
jarvis-qualia-engine                                    msjarvis-rebuild-jarvis-qualia-engine                 127.0.0.1:8017->8017/tcp
jarvis-memory                                           msjarvis-rebuild-jarvis-memory                        127.0.0.1:8056->8056/tcp
jarvis-auth-api                                         msjarvis-rebuild-jarvis-auth-api                      127.0.0.1:8092->8091/tcp
jarvis-hilbert-state                                    msjarvis-rebuild-jarvis-hilbert-state                 
jarvis-anvil                                            ghcr.io/foundry-rs/foundry:latest                     127.0.0.1:8545->8545/tcp
jarvis-judge-pipeline                                   msjarvis-rebuild-jarvis-judge-pipeline                
jarvis-session-sidecar                                  msjarvis-rebuild-jarvis-session-sidecar               127.0.0.1:8060->8060/tcp
competent_elion                                         msjarvis-rebuild-jarvis-session-sidecar               
jarvis-gbim-spatial-indexer                             msjarvis-gbim-indexers:latest                         127.0.0.1:7210->8000/tcp
jarvis-pia-sampler                                      msjarvis-rebuild-jarvis-pia-sampler                   127.0.0.1:8076->8050/tcp
jarvis-community-stake-registry                         msjarvis-rebuild-jarvis-main-brain:latest             127.0.0.1:8084->8084/tcp
jarvis-dao-governance                                   msjarvis-rebuild-jarvis-main-brain:latest             127.0.0.1:8082->8082/tcp
jarvis-mountainshares-coordinator                       msjarvis-rebuild-jarvis-main-brain:latest             127.0.0.1:8080->8080/tcp
jarvis-gbim-verifier                                    msjarvis-rebuild-jarvis-gbim-verifier                 
jarvis-decay-escalation-consumer                        msjarvis-rebuild-jarvis-decay-escalation-consumer     
mysql                                                   mysql:8.2                                             33060/tcp, 127.0.0.1:3307->3306/tcp
neo4j                                                   neo4j:5.13-community                                  7473/tcp, 127.0.0.1:7687->7687/tcp, 127.0.0.1:7475->7474/tcp
jarvis-crypto-policy                                    msjarvis-rebuild-jarvis-crypto-policy                 127.0.0.1:8099->8099/tcp
jarvis-gbim-query-router                                msjarvis-rebuild-jarvis-gbim-query-router             127.0.0.1:7205->7205/tcp
jarvis-ms-token-service                                 msjarvis-rebuild-jarvis-main-brain:latest             127.0.0.1:8088->8083/tcp
jarvis-judge-ethics                                     msjarvis-rebuild-jarvis-judge-ethics                  
jarvis-judge-alignment                                  msjarvis-rebuild-jarvis-judge-alignment               
nbb_woah_algorithms                                     msjarvis-rebuild-jarvis-main-brain:latest             127.0.0.1:8104->8104/tcp
jarvis-contract-forge                                   msjarvis-rebuild-jarvis-contract-forge                127.0.0.1:8093->8091/tcp
jarvis-brain-orchestrator                               msjarvis-rebuild-jarvis-brain-orchestrator            127.0.0.1:17260->7260/tcp
jarvis-judge-truth                                      msjarvis-rebuild-jarvis-judge-truth                   7230/tcp
jarvis-judge-consistency                                msjarvis-rebuild-jarvis-judge-consistency             
jarvis-blood-brain-barrier                              msjarvis-rebuild-jarvis-blood-brain-barrier           127.0.0.1:8016->8016/tcp
jarvis-redis                                            redis:7-alpine                                        127.0.0.1:6380->6379/tcp
jarvis-neurobiological-master                           msjarvis-rebuild-jarvis-neurobiological-master        8018/tcp
jarvis-rag-server                                       msjarvis-rebuild-jarvis-rag-server                    127.0.0.1:8003->8003/tcp
jarvis-autonomous-learner                               msjarvis-rebuild-jarvis-autonomous-learner            127.0.0.1:8020->8020/tcp
jarvis-ingest-watcher                                   msjarvis-rebuild_jarvis-ingest-watcher                
msjarvis-rebuild-nbb_prefrontal_cortex-1                msjarvis-rebuild-nbb_prefrontal_cortex                127.0.0.1:8105->7005/tcp
llm22-proxy                                             msjarvis-rebuild-llm22-proxy:latest                   127.0.0.1:8222->8222/tcp
llm14-proxy                                             msjarvis-rebuild-llm14-proxy:latest                   127.0.0.1:8214->8214/tcp
llm2-proxy                                              msjarvis-rebuild-llm2-proxy:latest                    127.0.0.1:8202->8202/tcp
llm18-proxy                                             msjarvis-rebuild-llm18-proxy:latest                   127.0.0.1:8218->8218/tcp
llm7-proxy                                              msjarvis-rebuild-llm7-proxy:latest                    127.0.0.1:8207->8207/tcp
jarvis-20llm-production                                 msjarvis-rebuild-jarvis-20llm-production              127.0.0.1:8008->8008/tcp
llm17-proxy                                             msjarvis-rebuild-llm17-proxy:latest                   127.0.0.1:8217->8217/tcp
llm12-proxy                                             msjarvis-rebuild-llm12-proxy:latest                   127.0.0.1:8212->8212/tcp
jarvis-fractal-consciousness                            msjarvis-rebuild-jarvis-fractal-consciousness         8027/tcp
jarvis-constitutional-guardian                          msjarvis-rebuild-jarvis-constitutional-guardian       127.0.0.1:8091->8091/tcp
llm20-proxy                                             msjarvis-rebuild-llm20-proxy:latest                   127.0.0.1:8220->8220/tcp
jarvis-fifth-dgm                                        msjarvis-rebuild-jarvis-fifth-dgm                     127.0.0.1:4002->4002/tcp
llm11-proxy                                             msjarvis-rebuild-llm11-proxy:latest                   127.0.0.1:8211->8211/tcp
llm6-proxy                                              msjarvis-rebuild-llm6-proxy:latest                    127.0.0.1:8206->8206/tcp
llm9-proxy                                              msjarvis-rebuild-llm9-proxy:latest                    127.0.0.1:8209->8209/tcp
msjarvis-rebuild-nbb_darwin_godel_machines-1            msjarvis-rebuild-nbb_darwin_godel_machines            127.0.0.1:8302->7003/tcp
llm21-proxy                                             msjarvis-rebuild-llm21-proxy:latest                   127.0.0.1:8221->8221/tcp
msjarvis-rebuild-nbb_pituitary_gland-1                  msjarvis-rebuild-nbb_pituitary_gland                  127.0.0.1:8108->80/tcp
llm16-proxy                                             msjarvis-rebuild-llm16-proxy:latest                   127.0.0.1:8216->8216/tcp
llm15-proxy                                             msjarvis-rebuild-llm15-proxy:latest                   127.0.0.1:8215->8215/tcp
jarvis-spiritual-rag                                    msjarvis-rebuild-jarvis-spiritual-rag                 8005/tcp, 127.0.0.1:8046->8046/tcp
msjarvis-rebuild-nbb_blood_brain_barrier-1              msjarvis-rebuild-nbb_blood_brain_barrier              127.0.0.1:8301->7001/tcp
llm8-proxy                                              msjarvis-rebuild-llm8-proxy:latest                    127.0.0.1:8208->8208/tcp
llm4-proxy                                              msjarvis-rebuild-llm4-proxy:latest                    127.0.0.1:8204->8204/tcp
jarvis-aaacpe-rag                                       msjarvis-rebuild-jarvis-aaacpe-rag                    127.0.0.1:8032->8032/tcp
jarvis-semaphore                                        msjarvis-rebuild-jarvis-semaphore                     127.0.0.1:8030->8030/tcp
llm10-proxy                                             msjarvis-rebuild-llm10-proxy:latest                   127.0.0.1:8210->8210/tcp
msjarvis-rebuild-nbb_heteroglobulin_transport-1         msjarvis-rebuild-nbb_heteroglobulin_transport         127.0.0.1:8106->7006/tcp
jarvis-woah                                             msjarvis-rebuild-jarvis-woah                          7012/tcp
msjarvis-rebuild-nbb_spiritual_root-1                   msjarvis-rebuild-nbb_spiritual_root                   127.0.0.1:8103->7003/tcp
jarvis-swarm-intelligence                               msjarvis-rebuild-jarvis-swarm-intelligence            8021/tcp, 8300/tcp
msjarvis-rebuild-nbb_i_containers-1                     msjarvis-rebuild-nbb_i_containers                     127.0.0.1:8101->7005/tcp
msjarvis-rebuild-nbb_spiritual_maternal_integration-1   msjarvis-rebuild-nbb_spiritual_maternal_integration   127.0.0.1:8109->7009/tcp
llm1-proxy                                              msjarvis-rebuild-llm1-proxy:latest                    127.0.0.1:8201->8201/tcp
ipfs                                                    ipfs/kubo:latest                                      4001/tcp, 8080-8081/tcp, 4001/udp, 127.0.0.1:5001->5001/tcp
llm19-proxy                                             msjarvis-rebuild-llm19-proxy:latest                   127.0.0.1:8219->8219/tcp
llm13-proxy                                             msjarvis-rebuild-llm13-proxy:latest                   127.0.0.1:8213->8213/tcp
jarvis-web-research                                     msjarvis-rebuild-jarvis-web-research                  8090/tcp
jarvis-69dgm-bridge                                     msjarvis-rebuild-jarvis-69dgm-bridge                  127.0.0.1:19000->9000/tcp
llm5-proxy                                              msjarvis-rebuild-llm5-proxy:latest                    127.0.0.1:8205->8205/tcp
msjarvis-rebuild-nbb_mother_carrie_protocols-1          msjarvis-rebuild-nbb_mother_carrie_protocols          127.0.0.1:8107->7007/tcp
jarvis-temporal-consciousness                           msjarvis-rebuild-jarvis-temporal-consciousness        7007/tcp
msjarvis-rebuild-nbb_consciousness_containers-1         msjarvis-rebuild-nbb_consciousness_containers         127.0.0.1:8102->7002/tcp
llm3-proxy                                              msjarvis-rebuild-llm3-proxy:latest                    127.0.0.1:8203->8203/tcp
jarvis-i-containers                                     msjarvis-rebuild-jarvis-i-containers                  127.0.0.1:8015->8015/tcp
jarvis-consciousness-bridge                             msjarvis-rebuild-jarvis-consciousness-bridge          8020/tcp
jarvis-ollama                                           ollama/ollama:latest                                  127.0.0.1:11434->11434/tcp
jarvis-lm-synthesizer                                   msjarvis-rebuild-jarvis-lm-synthesizer                8001/tcp
jarvis-gbim-temporal-indexer                            msjarvis-gbim-indexers:latest                         127.0.0.1:7211->8000/tcp
jarvis-gbim-benefit-indexer                             msjarvis-gbim-benefit-indexer:latest                  127.0.0.1:7206->7206/tcp
jarvis-aaacpe-scraper                                   msjarvis-rebuild-jarvis-aaacpe-scraper                127.0.0.1:8033->8033/tcp
jarvis-mother-protocols                                 msjarvis-rebuild-jarvis-mother-protocols              4000/tcp
jarvis-ingest-api                                       python:3.11-slim                                      
jarvis-gbim-semantic-indexer                            msjarvis-gbim-indexers:latest                         127.0.0.1:7212->8000/tcp
chromadb                                                chromadb/chroma:latest                                127.0.0.1:8001->8000/tcp
jarvis-grafana                                          grafana/grafana:10.2.3                                127.0.0.1:3000->3000/tcp
jarvis-jaeger                                           jaegertracing/all-in-one:1.52                         4317-4318/tcp, 5775/udp, 5778/tcp, 9411/tcp, 14250/tcp, 14268/tcp, 6831-6832/udp, 127.0.0.1:16686->16686/tcp
jarvis-prometheus                                       prom/prometheus:v2.48.0                               127.0.0.1:9090->9090/tcp
jarvis-otel-collector                                   otel/opentelemetry-collector-contrib:0.93.0           127.0.0.1:4317-4318->4317-4318/tcp, 127.0.0.1:8888->8888/tcp, 127.0.0.1:13133->13133/tcp, 55678-55679/tcp
jarvis-llm-judge-v3                                     msjarvis-rebuild-jarvis-llm-judge-v3                  127.0.0.1:7240->7240/tcp
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ # Check if there's a separate compose file for the GIS/data stack
ls /opt/msjarvis-rebuild/
docker compose -f /opt/msjarvis-rebuild/docker-compose.yml ps 2>/dev/null || \
docker compose ps
'='                                                                   gateway8050_inline.py
'$IDX'                                                                gateway_chat_attempt.log
 20llmFINAL.health.json                                               gateway-entrypoint.sh
 ai                                                                   gbim_backbone_rich.dump.sql
 ai-server                                                            gbim_chroma.py
 all_gis_vectors_filtered.txt                                         gbim_full_metadata.csv
 all_gis_vectors_full.txt                                             gbim_orchestrator.py
 all_gis_vectors_ingest.txt                                           gbim_sample_metadata.csv
 all_gis_vectors.txt                                                  gbim_worldview_entity_clean.sql
 all_gis_vectors_unique.txt                                           gbim_worldview_entity_data.sql
 api_resources.py                                                     gbim_worldview_entity_fresh.sql
 appservices                                                          gdb_integration_service.log
 archives                                                             gdb_result_snapshot.json
 ask_gis_near_oakhill.py                                              generate_attrs_sql.sh
 ask_gis.py                                                           generate_spiritual_inventories.py
 attrs_api.py                                                         geodb_collection_manifest.csv
 attrs_test.json                                                      geodb_restore_plan.md
 attrs_with_geom_api.py                                               gis_candidates_global.txt
 autonomouslearner.py                                                 gis_candidates_stage2.txt
 backfill_provenance_batch.sql                                        gisgeodb_storage.py
 backfill_provenance.sql                                              gisgeodbstorage.py
 backup_filename_index.txt                                            gis_notes
 _backup_llm_proxy_dockerfiles                                        gis_pipeline_8819.log
 backup_roots.txt                                                     gis_rag_query.py
 bbb_requirements.txt                                                 gis_rag_server.py
 bin                                                                  gis_statewide_run.log
 bootstrap_gbim_beliefs_eq1.py                                        HOST_LEARNER_CHROMA_PATH
 brain_orchestrator.py                                                index_gis_to_chroma.py
 bulk_ingest_attrs.py                                                 index_gis_to_chroma.py.bak_20260130103111
 bulk_ingest.log                                                      ingest_attrs_to_chroma.py
 bulk_load_attrs.sh                                                   ingest_gbimworldviewentities_from_csv.py
 CACHED                                                               ingest_kanawha_images.py
 call_rag_with_entanglement_example.py                                ingest_kanawha_resources.py
 capture_gdb_json.sh                                                  ingest.log
 chat_light_current.py                                                ingest_missing_attrs.py
 check_gbim_metadata.sh                                               ingest_missing.log
 chroma_data                                                          ingest_msjarvis_corpus.py
 chroma_db                                                            ingest_personal_pdfs.py
 chromadb                                                             ingest_wv_income_maintenance_manual.py
 chroma_ingestion_sources.txt                                         integration_layer
 chroma_persistent_RAG_WORKING_20260116.tgz                          '[internal]'
 chroma.sqlite3                                                      'itus_addr AS address, -- site address'
 CONSENSUS_STATS_SNAPSHOT.json                                        jarvis-chroma
 constitutional_api.py                                                jarvis_env.sh
 countyfp20                                                           knowledge_pdfs
 CURRENT_LLM_STACK_NOTES.txt                                          KNOWN_LIMITATIONS_20LLM_SEQUENTIAL.txt
 CURRENTSTATUS.md                                                     layer_manifest.csv
 data                                                                 list_due_for_verification.py
 debug_consciousness_bridge.md                                        llm10_health_proxy.py
 debug-logs                                                           llm11_health_proxy.py
 demo_msjarvis_ranked.py                                              llm12_health_proxy.py
 demo_msjarvis_resources.py                                           llm13_health_proxy.py
 docker-compose.gbim.yml                                              llm14_health_proxy.py
 docker-compose.golden.bak_bbb_clean_proxy                            llm15_health_proxy.py
 docker-compose.golden.bak_bbb_proxy_cmd_fix                          llm16_health_proxy.py
 docker-compose.golden.bak_bbb_uvicorn_fix                            llm17_health_proxy.py
 docker-compose.golden.bak_before_bbb_proxy2                          llm18_health_proxy.py
 docker-compose.golden.bak_before_brain_ports_cleanup                 llm19_health_proxy.py
 docker-compose.golden.bak_before_python3_cmd_fix                     llm1_health_proxy.py
 docker-compose.golden.bak_nbb_base_final                             llm20_health_proxy.py
 docker-compose.golden.bak_python310_compose_all                      llm21_health_proxy.py
 docker-compose.golden.bak_services_mapping_fix                       llm22_health_proxy.py
 docker-compose.golden.bak_web_research_cmd                           llm2_health_proxy.py
 docker-compose.golden.yml                                            llm3_health_proxy.py
 docker-compose.llm-proxies.yml                                       llm4_health_proxy.py
 docker-compose.MOTHERCARRIE.BAK.20260216-132826                      llm5_health_proxy.py
 docker-compose.MOTHERCARRIE.BAK.20260216-132834                      llm6_health_proxy.py
 docker-compose.override.yml                                          llm7_health_proxy.py
 docker-compose-patch.yml                                             llm8_health_proxy.py
 docker-compose.RAG_WORKING_20260116.yml                              llm9_health_proxy.py
 docker-compose.RAG_WORKING_20260116.yml.bak-20260122223705           llm_health_proxies
 docker-compose.RAG_WORKING_20260116.yml.bak_gateway8050              llm_servers_from_backup
 docker-compose.RAG_WORKING_20260116.yml.bak_mainbrain8058            load_all_attrs.sql
 docker-compose.RAG_WORKING_20260116.yml.bak-portfix-20260122224758   load_hospitals.sql
 docker-compose.RAG_WORKING_20260116.yml.bak_python310_fix            load_services_attrs_and_enrich.py
 docker-compose.rag.yml                                               local_resources_export.csv
 docker-compose.recovered.yml                                         logs
 docker-compose.restored.yml                                          logs-archive
 docker-compose.restored.yml.pre-hilbert-fix-1768013541               logs-gis_rag_server_8055.log
 docker-compose.restored.yml.safe-1768040125                          logs-rag_server_8003.log
 docker-compose.working.20260118-235132.yml                           logs-rag_server_dynamic.log
 docker-compose.working.20260119-000202.yml                           logs-rag_server.log
 docker-compose.yml                                                   mainbrain.log
 docker-compose.yml.20llm.bak                                         main_brain.py
 docker-compose.yml.after-bbb.bak                                     main.py
 docker-compose.yml.backup                                            missing_collections.csv
 docker-compose.yml.backup.1768311648                                 missing_local_files.txt
 docker-compose.yml.backup.1768313257                                 missing_source_epochs.csv
 docker-compose.yml.backup.1768313407                                 models.py
 docker-compose.yml.backup.1768786837                                 msjarvis_chroma_test.py
 docker-compose.yml.backup.1768788421                                 msjarvis_embed_gbim.py
 docker-compose.yml.backup_20260215_232944                            msjarvis_embed_gbim_resume_tail.py
 docker-compose.yml.backup_20260218_085941                            msjarvisragserverwvpatch.py
 docker-compose.yml.backup_autonomous_learner_20260109-074048         msjarvis_resources.py
 docker-compose.yml.backup_gateway_ports_20260109-091103              ms_jarvis_unified_gateway.py
 docker-compose.yml.backup_jan13_consciousness                        msjarviswoahalgorithms.py
 docker-compose.yml.backup_nbb_ports                                  naming
 docker-compose.yml.backup_nbb_ports_fixed                            nbb_woah_algorithms_fix.patch
 docker-compose.yml.bak                                               neurobiological_brain
 docker-compose.yml.bak.1768500857                                    neurobiologicalbrain
 docker-compose.yml.bak_1768574001                                    neurobiologicalbrainmothercarrieprotocolsservice
 docker-compose.yml.bak.1768781706                                    neuro-prefrontalcortex-patched.tar
 docker-compose.yml.bak-1768791131                                    nginx.conf
 docker-compose.yml.bak-1768791194                                    nohup.out
 docker-compose.yml.bak-1768791760                                    old_drive_gis_candidates.txt
 docker-compose.yml.bak.20260110161005                                patch_llm_health_endpoints.sh
 docker-compose.yml.bak.20260206142334                                pdf_utils.py
 docker-compose.yml.bak.20260206142646                                persistent_chroma_old
 docker-compose.yml.bak_add_clock                                     pg_hba.conf
 docker-compose.yml.bak_before_unified_fix                            post-fix-automation.sh
 docker-compose.yml.bak_drop_images                                   probe_gdb_integration.sh
 docker-compose.yml.bak_drop_roche                                    processstatewidegisbulk_8819.log
 docker-compose.yml.bak_ports_20260118163828                          processstatewidegisbulk_.log
 docker-compose.yml.bak_redis_env_1769196600                          process_wv_layers.py
 docker-compose.yml.bak_redis_fix_1769195136                          proposals
 docker-compose.yml.bak_redis_fix_1769195657                          pull_jarvis_models.sh
 docker-compose.yml.bak_unified_cycle_fix                             __pycache__
 docker-compose.yml.bak_woah_20260118163402                           query_msjarvis_corpus.py
 docker-compose.yml.bbb.bak                                           query_msjarvis_once.py
 docker-compose.yml.before_8010_fix_1768044953                        quick_gdb_probe.sh
 docker-compose.yml.before_fix                                        rag_insert_mountainshares.py
 docker-compose.yml.before_fix_20260122                               rag_integration_snapshot.tgz
 docker-compose.yml.before_neuro_fix_1768012948                       rag_local_resources.py
 docker-compose.yml.broken                                            ragservermain.current.log
 docker-compose.yml.broken-1768013498                                 rag_server_main.py
 docker-compose.yml.broken_backup                                     ragservermain.py
 docker-compose.yml.BROKEN_BACKUP                                     rag_server_main.py.bak.1768180485
 docker-compose.yml.broken_spiritual                                  ragsimple.current.log
 docker-compose.yml.chroma-backup-20260114054916                      reading
 docker-compose.yml.chroma-backup-20260114060013                      REBUILD_COMPLETE.md
 docker-compose.yml.full_backup_20260122                              reingest_msjarvis_chunks.py
 docker-compose.yml.nbb.bak                                           reload_and_ingest_gis.sh
 docker-compose.yml.pre-hilbert-fix-1768013541                        reload_geodb_bootstrap.sh
 docker-compose.yml.pre_judges                                        requirements.txt
 docker-compose.yml.safe-1768040125                                   resolving
 Dockerfile                                                           resource_assistant.py
 Dockerfile.20llm                                                     resource_ranker.py
 Dockerfile.agents                                                    resources
 Dockerfile.bak_before_python3_fix                                    RESTART_20LLM_FINAL.sh
 Dockerfile.brain                                                     restart_unified_msjarvis.sh
 Dockerfile.consciousnessbridge                                       restore_missing_files.sh
 Dockerfile.full_neuro                                                run_core_ops.sh
 Dockerfile.gateway                                                   run_gbim_import.sh
 Dockerfile.gis_rag                                                   run_gis_stack.sh
 Dockerfile-llm10-proxy                                               run_sanctuary_import.sh
 Dockerfile-llm11-proxy                                               scripts
 Dockerfile-llm12-proxy                                               secrets
 Dockerfile-llm13-proxy                                               seed_full_knowledge.py
 Dockerfile-llm14-proxy                                               seed_gbim_catalog.py
 Dockerfile-llm15-proxy                                               seed_mountainshares.py
 Dockerfile-llm16-proxy                                               service_build_matrix.txt
 Dockerfile-llm17-proxy                                               service_discovery_no_redis.py
 Dockerfile-llm18-proxy                                               service_registry_client_stub.py
 Dockerfile-llm19-proxy                                               services
 Dockerfile-llm1-proxy                                                sourcetable
 Dockerfile-llm20-proxy                                               spiritual_nbb_backup_20260215_231630.tar.gz
 Dockerfile-llm21-proxy                                               spiritual_nbb_fix2_20260215_232031.tar.gz
 Dockerfile-llm22-proxy                                               spiritual_rag_deployment_20260215_232717.tar.gz
 Dockerfile-llm2-proxy                                                STABLE_MODE_NOTE.txt
 Dockerfile-llm3-proxy                                                START20LLMFINAL.sh
 Dockerfile-llm4-proxy                                                START20LLMFINAL.sh.backup.20260121180532
 Dockerfile-llm5-proxy                                                START20LLMPRODUCTION.sh
 Dockerfile-llm6-proxy                                                START_GIS_RAG.sh
 Dockerfile-llm7-proxy                                                STATUS_MARCH15_2026_FINAL.md
 Dockerfile-llm8-proxy                                                sync_gbim_to_chroma.py
 Dockerfile-llm9-proxy                                                test_autonomous_learner_store.py
 Dockerfile.local_resources                                           test_chatsync_gateway.sh
 Dockerfile.nbb_icontainers_fastapi                                   test_chatsync.sh
 Dockerfile.neuro                                                     test_end_to_end_woah_fifthdgm.py
 Dockerfile.neuro-prefrontal-patched                                  test_immediate.sh
 Dockerfile.qualia                                                    test_msjarvis.golden.sh
 Dockerfile.qualia.bak                                                test_msjarvis.sh
 Dockerfile.rag                                                       test_msjarvis.working.20260119-000202.sh
 Dockerfile.rag_server                                                test_provenance_one.sql
 Dockerfile.rag_server_main                                           test_rag_image.py
 Dockerfile.ragservermain                                             test_rag_text.py
 Dockerfile.swarm                                                     test-unified-gateway.sh
 Dockerfile.woah                                                      tmp_rag_slice.py
 docs                                                                 TODO_enable_real_entanglement.md
 dump_gdb_result.sh                                                   tools
 dynamic_port_service_no_flask.py                                     transferring
 enrich_from_attrs.log                                                ultimate8050.log
 enrich_from_attrs.py                                                 wheels
 enrich_where.log                                                     woah_health.json
 enrich_where.py                                                      woah_metrics_example.json
 env                                                                  woah_openapi.json
 error_summary.log                                                    woah_process_example.json
 etl                                                                  writing
 example_wv_entangled_request.json                                    wv_entangled_context_model.py
 example_wv_entangled_response.json                                   wv_entangled_context.schema.json
 export_gbim_sample.py                                                wv_gis_layers
 exporting                                                            wv_gis_layers_catalog.csv
 exports                                                              wv_gis_layers_process_status.csv
 fix-20llm.sh                                                         wv_like_csv_candidates.txt
 full_fs_indexer.sh                                                   wv_name_matches_current_pv.txt
NAME                                                    IMAGE                                                 COMMAND                  SERVICE                              CREATED        STATUS                  PORTS
ipfs                                                    ipfs/kubo:latest                                      "/sbin/tini -- /usr/…"   ipfs                                 5 days ago     Up 5 days (healthy)     4001/tcp, 8080-8081/tcp, 4001/udp, 127.0.0.1:5001->5001/tcp
jarvis-20llm-production                                 msjarvis-rebuild-jarvis-20llm-production              "python3 ai_server_2…"   jarvis-20llm-production              5 days ago     Up 2 days               127.0.0.1:8008->8008/tcp
jarvis-69dgm-bridge                                     msjarvis-rebuild-jarvis-69dgm-bridge                  "python3 port_9000_6…"   jarvis-69dgm-bridge                  5 days ago     Up 5 days               127.0.0.1:19000->9000/tcp
jarvis-aaacpe-rag                                       msjarvis-rebuild-jarvis-aaacpe-rag                    "uvicorn aaacpe_rag_…"   jarvis-aaacpe-rag                    5 days ago     Up 5 days               127.0.0.1:8032->8032/tcp
jarvis-aaacpe-scraper                                   msjarvis-rebuild-jarvis-aaacpe-scraper                "uvicorn aaacpe_scra…"   jarvis-aaacpe-scraper                12 days ago    Up 12 days              127.0.0.1:8033->8033/tcp
jarvis-anvil                                            ghcr.io/foundry-rs/foundry:latest                     "sh -c 'anvil --host…"   jarvis-anvil                         2 days ago     Up 2 days               127.0.0.1:8545->8545/tcp
jarvis-auth-api                                         msjarvis-rebuild-jarvis-auth-api                      "sh -lc 'cd /app/ser…"   jarvis-auth-api                      44 hours ago   Up 44 hours (healthy)   127.0.0.1:8092->8091/tcp
jarvis-autonomous-learner                               msjarvis-rebuild-jarvis-autonomous-learner            "uvicorn ms_jarvis_a…"   jarvis-autonomous-learner            5 days ago     Up 5 days               127.0.0.1:8020->8020/tcp
jarvis-blood-brain-barrier                              msjarvis-rebuild-jarvis-blood-brain-barrier           "python3 ms_jarvis_b…"   jarvis-blood-brain-barrier           4 days ago     Up 4 days               127.0.0.1:8016->8016/tcp
jarvis-brain-orchestrator                               msjarvis-rebuild-jarvis-brain-orchestrator            "python3 brain_orche…"   jarvis-brain-orchestrator            3 days ago     Up 3 days (healthy)     127.0.0.1:17260->7260/tcp
jarvis-chroma                                           chromadb/chroma:latest                                "dumb-init -- chroma…"   jarvis-chroma                        8 hours ago    Up 8 hours (healthy)    127.0.0.1:8002->8000/tcp
jarvis-community-stake-registry                         msjarvis-rebuild-jarvis-main-brain:latest             "uvicorn community_s…"   jarvis-community-stake-registry      2 days ago     Up 2 days               127.0.0.1:8084->8084/tcp
jarvis-confidence-decay                                 msjarvis-rebuild-jarvis-confidence-decay              "python3 services/co…"   jarvis-confidence-decay              44 hours ago   Up 44 hours (healthy)   
jarvis-consciousness-bridge                             msjarvis-rebuild-jarvis-consciousness-bridge          "python3 /app/servic…"   jarvis-consciousness-bridge          10 days ago    Up 5 days               8020/tcp
jarvis-constitutional-guardian                          msjarvis-rebuild-jarvis-constitutional-guardian       "python3 jarvis-cons…"   jarvis-constitutional-guardian       5 days ago     Up 5 days               127.0.0.1:8091->8091/tcp
jarvis-contract-forge                                   msjarvis-rebuild-jarvis-contract-forge                "uvicorn ms_jarvis_c…"   jarvis-contract-forge                2 days ago     Up 2 days               127.0.0.1:8093->8091/tcp
jarvis-crypto-policy                                    msjarvis-rebuild-jarvis-crypto-policy                 "uvicorn jarviscrypt…"   jarvis-crypto-policy                 2 days ago     Up 2 days               127.0.0.1:8099->8099/tcp
jarvis-dao-governance                                   msjarvis-rebuild-jarvis-main-brain:latest             "uvicorn dao_governa…"   jarvis-dao-governance                2 days ago     Up 2 days               127.0.0.1:8082->8082/tcp
jarvis-decay-escalation-consumer                        msjarvis-rebuild-jarvis-decay-escalation-consumer     "python -u jarvis_de…"   jarvis-decay-escalation-consumer     2 days ago     Up 2 days               
jarvis-fifth-dgm                                        msjarvis-rebuild-jarvis-fifth-dgm                     "python -m uvicorn m…"   jarvis-fifth-dgm                     5 days ago     Up 5 days               127.0.0.1:4002->4002/tcp
jarvis-fractal-consciousness                            msjarvis-rebuild-jarvis-fractal-consciousness         "python3 /app/servic…"   jarvis-fractal-consciousness         5 days ago     Up 5 days               8027/tcp
jarvis-gbim-query-router                                msjarvis-rebuild-jarvis-gbim-query-router             "python3 gbim_query_…"   jarvis-gbim-query-router             2 days ago     Up 2 days               127.0.0.1:7205->7205/tcp
jarvis-gbim-spatial-indexer                             msjarvis-gbim-indexers:latest                         "python3 -m uvicorn …"   jarvis-gbim-spatial-indexer          2 days ago     Up 2 days               127.0.0.1:7210->8000/tcp
jarvis-gbim-verifier                                    msjarvis-rebuild-jarvis-gbim-verifier                 "python3 gbim_verifi…"   jarvis-gbim-verifier                 2 days ago     Up 2 days               
jarvis-gis-db                                           postgis/postgis:15-3.4                                "docker-entrypoint.s…"   jarvis-local-resources-db            4 hours ago    Up 4 hours              127.0.0.1:5435->5432/tcp
jarvis-gis-rag                                          msjarvis-rebuild-jarvis-gis-rag                       "uvicorn gis_rag_ser…"   jarvis-gis-rag                       4 hours ago    Up 14 minutes           127.0.0.1:8004->8004/tcp, 8044/tcp
jarvis-hilbert-state                                    msjarvis-rebuild-jarvis-hilbert-state                 "python3 -m uvicorn …"   jarvis-hilbert-state                 47 hours ago   Up 47 hours             
jarvis-i-containers                                     msjarvis-rebuild-jarvis-i-containers                  "/opt/nvidia/nvidia_…"   jarvis-i-containers                  5 days ago     Up 4 days               127.0.0.1:8015->8015/tcp
jarvis-ingest-api                                       python:3.11-slim                                      "python3 -c 'import …"   jarvis-ingest-api                    12 days ago    Up 20 hours             
jarvis-ingest-watcher                                   msjarvis-rebuild_jarvis-ingest-watcher                "python -m ingest_wa…"   jarvis-ingest-watcher                5 days ago     Up 5 days               
jarvis-judge-alignment                                  msjarvis-rebuild-jarvis-judge-alignment               "python3 judge_align…"   jarvis-judge-alignment               2 days ago     Up 2 days               
jarvis-judge-consistency                                msjarvis-rebuild-jarvis-judge-consistency             "python3 judge_consi…"   jarvis-judge-consistency             4 days ago     Up 4 days               
jarvis-judge-ethics                                     msjarvis-rebuild-jarvis-judge-ethics                  "python3 judge_ethic…"   jarvis-judge-ethics                  2 days ago     Up 2 days               
jarvis-judge-pipeline                                   msjarvis-rebuild-jarvis-judge-pipeline                "python3 judge_pipel…"   jarvis-judge-pipeline                2 days ago     Up 2 days               
jarvis-judge-truth                                      msjarvis-rebuild-jarvis-judge-truth                   "python3 judge_truth…"   jarvis-judge-truth                   4 days ago     Up 4 days               7230/tcp
jarvis-lm-synthesizer                                   msjarvis-rebuild-jarvis-lm-synthesizer                "python lm_synthesiz…"   jarvis-lm-synthesizer                10 days ago    Up 10 days              8001/tcp
jarvis-local-resources                                  msjarvis-rebuild-jarvis-local-resources               "uvicorn local_resou…"   jarvis-local-resources               4 hours ago    Up 4 hours              127.0.0.1:8006->8006/tcp, 8035/tcp
jarvis-main-brain                                       msjarvis-rebuild-jarvis-main-brain                    "sh -lc 'cd /app/ser…"   jarvis-main-brain                    44 hours ago   Up 44 hours (healthy)   127.0.0.1:8050->8050/tcp
jarvis-memory                                           msjarvis-rebuild-jarvis-memory                        "uvicorn ms_jarvis_m…"   jarvis-memory                        44 hours ago   Up 44 hours             127.0.0.1:8056->8056/tcp
jarvis-mother-protocols                                 msjarvis-rebuild-jarvis-mother-protocols              "python -m uvicorn m…"   jarvis-mother-protocols              12 days ago    Up 12 days              4000/tcp
jarvis-mountainshares-coordinator                       msjarvis-rebuild-jarvis-main-brain:latest             "uvicorn mountainsha…"   jarvis-mountainshares-coordinator    2 days ago     Up 2 days               127.0.0.1:8080->8080/tcp
jarvis-ms-token-service                                 msjarvis-rebuild-jarvis-main-brain:latest             "uvicorn token_servi…"   jarvis-ms-token-service              2 days ago     Up 2 days               127.0.0.1:8088->8083/tcp
jarvis-neurobiological-master                           msjarvis-rebuild-jarvis-neurobiological-master        "python3 ms_jarvis_n…"   jarvis-neurobiological-master        4 days ago     Up 4 days               8018/tcp
jarvis-ollama                                           ollama/ollama:latest                                  "/bin/ollama serve"      jarvis-ollama                        10 days ago    Up 10 days              127.0.0.1:11434->11434/tcp
jarvis-pia-sampler                                      msjarvis-rebuild-jarvis-pia-sampler                   "sh -lc 'cd /app/ser…"   jarvis-pia-sampler                   2 days ago     Up 2 days               127.0.0.1:8076->8050/tcp
jarvis-qualia-engine                                    msjarvis-rebuild-jarvis-qualia-engine                 "python3 -m uvicorn …"   jarvis-qualia-engine                 44 hours ago   Up 44 hours             127.0.0.1:8017->8017/tcp
jarvis-rag-server                                       msjarvis-rebuild-jarvis-rag-server                    "uvicorn ms_jarvis_r…"   jarvis-rag-server                    4 days ago     Up 4 days               127.0.0.1:8003->8003/tcp
jarvis-redis                                            redis:7-alpine                                        "docker-entrypoint.s…"   jarvis-redis                         4 days ago     Up 4 days (healthy)     127.0.0.1:6380->6379/tcp
jarvis-semaphore                                        msjarvis-rebuild-jarvis-semaphore                     "uvicorn jarvis-sema…"   jarvis-semaphore                     5 days ago     Up 5 days               127.0.0.1:8030->8030/tcp
jarvis-session-sidecar                                  msjarvis-rebuild-jarvis-session-sidecar               "uvicorn services.se…"   jarvis-session-sidecar               2 days ago     Up 2 days               127.0.0.1:8060->8060/tcp
jarvis-spiritual-rag                                    msjarvis-rebuild-jarvis-spiritual-rag                 "python3 jarvis-spir…"   jarvis-spiritual-rag                 5 days ago     Up 5 days               8005/tcp, 127.0.0.1:8046->8046/tcp
jarvis-steward                                          msjarvis-rebuild-jarvis-steward                       "uvicorn jarvis_stew…"   jarvis-steward                       29 hours ago   Up 29 hours             127.0.0.1:8051->8060/tcp
jarvis-stewardship-scheduler                            msjarvis-rebuild-jarvis-stewardship-scheduler         "python3 jarvis_stew…"   jarvis-stewardship-scheduler         26 hours ago   Up 26 hours             127.0.0.1:8079->8079/tcp
jarvis-swarm-intelligence                               msjarvis-rebuild-jarvis-swarm-intelligence            "python3 ms_jarvis_s…"   jarvis-swarm-intelligence            5 days ago     Up 5 days               8021/tcp, 8300/tcp
jarvis-temporal-consciousness                           msjarvis-rebuild-jarvis-temporal-consciousness        "sh -c 'echo 'Tempor…"   jarvis-temporal-consciousness        5 days ago     Up 11 minutes           7007/tcp
jarvis-unified-gateway                                  msjarvis-rebuild-jarvis-unified-gateway               "/bin/sh -c 'pip ins…"   jarvis-unified-gateway               42 hours ago   Up 42 hours             127.0.0.1:18018->8001/tcp
jarvis-web-research                                     msjarvis-rebuild-jarvis-web-research                  "python ms_jarvis_we…"   jarvis-web-research                  5 days ago     Up 5 days               8090/tcp
jarvis-woah                                             msjarvis-rebuild-jarvis-woah                          "uvicorn woah_servic…"   jarvis-woah                          5 days ago     Up 5 days               7012/tcp
llm1-proxy                                              msjarvis-rebuild-llm1-proxy:latest                    "uvicorn llm1_health…"   llm1-proxy                           5 days ago     Up 2 days               127.0.0.1:8201->8201/tcp
llm10-proxy                                             msjarvis-rebuild-llm10-proxy:latest                   "uvicorn llm10_healt…"   llm10-proxy                          5 days ago     Up 2 days               127.0.0.1:8210->8210/tcp
llm11-proxy                                             msjarvis-rebuild-llm11-proxy:latest                   "uvicorn llm11_healt…"   llm11-proxy                          5 days ago     Up 2 days               127.0.0.1:8211->8211/tcp
llm12-proxy                                             msjarvis-rebuild-llm12-proxy:latest                   "uvicorn llm12_healt…"   llm12-proxy                          5 days ago     Up 2 days               127.0.0.1:8212->8212/tcp
llm13-proxy                                             msjarvis-rebuild-llm13-proxy:latest                   "uvicorn llm13_healt…"   llm13-proxy                          5 days ago     Up 2 days               127.0.0.1:8213->8213/tcp
llm14-proxy                                             msjarvis-rebuild-llm14-proxy:latest                   "uvicorn llm14_healt…"   llm14-proxy                          5 days ago     Up 2 days               127.0.0.1:8214->8214/tcp
llm15-proxy                                             msjarvis-rebuild-llm15-proxy:latest                   "uvicorn llm15_healt…"   llm15-proxy                          5 days ago     Up 2 days               127.0.0.1:8215->8215/tcp
llm16-proxy                                             msjarvis-rebuild-llm16-proxy:latest                   "uvicorn llm16_healt…"   llm16-proxy                          5 days ago     Up 2 days               127.0.0.1:8216->8216/tcp
llm17-proxy                                             msjarvis-rebuild-llm17-proxy:latest                   "uvicorn llm17_healt…"   llm17-proxy                          5 days ago     Up 2 days               127.0.0.1:8217->8217/tcp
llm18-proxy                                             msjarvis-rebuild-llm18-proxy:latest                   "uvicorn llm18_healt…"   llm18-proxy                          5 days ago     Up 2 days               127.0.0.1:8218->8218/tcp
llm19-proxy                                             msjarvis-rebuild-llm19-proxy:latest                   "uvicorn llm19_healt…"   llm19-proxy                          5 days ago     Up 2 days               127.0.0.1:8219->8219/tcp
llm2-proxy                                              msjarvis-rebuild-llm2-proxy:latest                    "uvicorn llm2_health…"   llm2-proxy                           5 days ago     Up 2 days               127.0.0.1:8202->8202/tcp
llm20-proxy                                             msjarvis-rebuild-llm20-proxy:latest                   "uvicorn llm20_healt…"   llm20-proxy                          5 days ago     Up 2 days               127.0.0.1:8220->8220/tcp
llm21-proxy                                             msjarvis-rebuild-llm21-proxy:latest                   "uvicorn llm21_healt…"   llm21-proxy                          5 days ago     Up 2 days               127.0.0.1:8221->8221/tcp
llm22-proxy                                             msjarvis-rebuild-llm22-proxy:latest                   "uvicorn llm22_healt…"   llm22-proxy                          5 days ago     Up 2 days               127.0.0.1:8222->8222/tcp
llm3-proxy                                              msjarvis-rebuild-llm3-proxy:latest                    "uvicorn llm3_health…"   llm3-proxy                           5 days ago     Up 2 days               127.0.0.1:8203->8203/tcp
llm4-proxy                                              msjarvis-rebuild-llm4-proxy:latest                    "uvicorn llm4_health…"   llm4-proxy                           5 days ago     Up 2 days               127.0.0.1:8204->8204/tcp
llm5-proxy                                              msjarvis-rebuild-llm5-proxy:latest                    "uvicorn llm5_health…"   llm5-proxy                           5 days ago     Up 2 days               127.0.0.1:8205->8205/tcp
llm6-proxy                                              msjarvis-rebuild-llm6-proxy:latest                    "uvicorn llm6_health…"   llm6-proxy                           5 days ago     Up 2 days               127.0.0.1:8206->8206/tcp
llm7-proxy                                              msjarvis-rebuild-llm7-proxy:latest                    "uvicorn llm7_health…"   llm7-proxy                           5 days ago     Up 2 days               127.0.0.1:8207->8207/tcp
llm8-proxy                                              msjarvis-rebuild-llm8-proxy:latest                    "uvicorn llm8_health…"   llm8-proxy                           5 days ago     Up 2 days               127.0.0.1:8208->8208/tcp
llm9-proxy                                              msjarvis-rebuild-llm9-proxy:latest                    "uvicorn llm9_health…"   llm9-proxy                           5 days ago     Up 2 days               127.0.0.1:8209->8209/tcp
msjarvis-rebuild-nbb_blood_brain_barrier-1              msjarvis-rebuild-nbb_blood_brain_barrier              "uvicorn blood_brain…"   nbb_blood_brain_barrier              5 days ago     Up 5 days               127.0.0.1:8301->7001/tcp
msjarvis-rebuild-nbb_consciousness_containers-1         msjarvis-rebuild-nbb_consciousness_containers         "uvicorn consciousne…"   nbb_consciousness_containers         5 days ago     Up 5 days               127.0.0.1:8102->7002/tcp
msjarvis-rebuild-nbb_darwin_godel_machines-1            msjarvis-rebuild-nbb_darwin_godel_machines            "uvicorn nbb_darwin_…"   nbb_darwin_godel_machines            5 days ago     Up 5 days               127.0.0.1:8302->7003/tcp
msjarvis-rebuild-nbb_heteroglobulin_transport-1         msjarvis-rebuild-nbb_heteroglobulin_transport         "uvicorn heteroglobu…"   nbb_heteroglobulin_transport         5 days ago     Up 5 days               127.0.0.1:8106->7006/tcp
msjarvis-rebuild-nbb_i_containers-1                     msjarvis-rebuild-nbb_i_containers                     "uvicorn i_container…"   nbb_i_containers                     5 days ago     Up 4 days               127.0.0.1:8101->7005/tcp
msjarvis-rebuild-nbb_mother_carrie_protocols-1          msjarvis-rebuild-nbb_mother_carrie_protocols          "uvicorn main:app --…"   nbb_mother_carrie_protocols          5 days ago     Up 5 days               127.0.0.1:8107->7007/tcp
msjarvis-rebuild-nbb_pituitary_gland-1                  msjarvis-rebuild-nbb_pituitary_gland                  "uvicorn pituitary_g…"   nbb_pituitary_gland                  5 days ago     Up 5 days               127.0.0.1:8108->80/tcp
msjarvis-rebuild-nbb_prefrontal_cortex-1                msjarvis-rebuild-nbb_prefrontal_cortex                "uvicorn prefrontal_…"   nbb_prefrontal_cortex                5 days ago     Up 5 days               127.0.0.1:8105->7005/tcp
msjarvis-rebuild-nbb_spiritual_maternal_integration-1   msjarvis-rebuild-nbb_spiritual_maternal_integration   "uvicorn spiritual_m…"   nbb_spiritual_maternal_integration   5 days ago     Up 5 days               127.0.0.1:8109->7009/tcp
msjarvis-rebuild-nbb_spiritual_root-1                   msjarvis-rebuild-nbb_spiritual_root                   "uvicorn spiritual_r…"   nbb_spiritual_root                   5 days ago     Up 5 days               127.0.0.1:8103->7003/tcp
mysql                                                   mysql:8.2                                             "docker-entrypoint.s…"   mysql                                2 days ago     Up 2 days (healthy)     33060/tcp, 127.0.0.1:3307->3306/tcp
nbb_woah_algorithms                                     msjarvis-rebuild-jarvis-main-brain:latest             "uvicorn ms_jarvis_w…"   nbb_woah_algorithms                  2 days ago     Up 2 days               127.0.0.1:8104->8104/tcp
neo4j                                                   neo4j:5.13-community                                  "tini -g -- /startup…"   neo4j                                2 days ago     Up 2 days (healthy)     7473/tcp, 127.0.0.1:7687->7687/tcp, 127.0.0.1:7475->7474/tcp
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ 

