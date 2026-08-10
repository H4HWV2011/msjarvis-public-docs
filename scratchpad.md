Wrote: /tmp/meaning-geometry-investigation/13-tier1-static-graph.json
Wrote: /tmp/meaning-geometry-investigation/13-tier1-static-graph.txt
Definitions: 93
Resolved Tier-1 edges: 87
Routes: 41
Service/env references: 49
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/nvme1/msjarvis-rebuild$ cd /mnt/nvme1/msjarvis-rebuild

BASE=/tmp/meaning-geometry-investigation

python - <<'PY'
import json
from collections import defaultdict

BASE = "/tmp/meaning-geometry-investigation"
data = json.load(open(f"{BASE}/13-tier1-static-graph.json"))

edges = data["resolved_tier1_edges"]

out = defaultdict(set)
inc = defaultdict(set)

for e in edges:
    src = e["source"].split(":")[0]
    dst = e["target"].split(":")[0]
    if src != dst:
        out[src].add(dst)
        inc[dst].add(src)

PYint(f"Wrote: {BASE}/14-tier1-dependency-matrix.txt"))) as f:
Wrote: /tmp/meaning-geometry-investigation/14-tier1-dependency-matrix.txt
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/nvme1/msjarvis-rebuild$ cd /mnt/nvme1/msjarvis-rebuild

BASE=/tmp/meaning-geometry-investigation

{
printf '%s\n' '===== MEANING / GEOMETRY SYMBOL INVENTORY ====='
printf 'commit: '; git rev-parse HEAD
printf '\n'

printf '%s\n' '===== SEMANTIC / MEANING SYMBOLS ====='
grep -RniE \
  --include='*.py' \
  --exclude-dir='.git' \
  --exclude-dir='investigation_20260807' \
  --exclude-dir='validation' \
  'semantic|meaning|concept|representation|sense|embedding|vector|similarity|distance|context' \
  services/jarvis_hilbert_semantic.py \
  services/hilbert_spatial_chat.py \
  services/integrate_spatial_temporal.py \
  services/gbim_semantic_indexer.py \
  services/rag_geospatial.py \
  services/rag_geospatial_context.py \
wc -l "$BASE/15-meaning-geometry-symbols.txt"ance|state|transition|entangle|de
477 /tmp/meaning-geometry-investigation/15-meaning-geometry-symbols.txt
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/nvme1/msjarvis-rebuild$ cd /mnt/nvme1/msjarvis-rebuild

BASE=/tmp/meaning-geometry-investigation

{
printf '%s\n' '===== CURRENT RUNTIME DECLARATION CHECK ====='
printf 'commit: '; git rev-parse HEAD
printf '\n'

for f in \
  services/jarvis_hilbert_semantic.py \
  services/jarvis_hilbert_state.py \
  services/jarvis_hilbert_time.py \
  services/hilbert_spatial_chat.py \
  services/integrate_spatial_temporal.py \
  services/gbim_semantic_indexer.py \
  services/gbim_spatial_indexer.py \
  services/gbim_temporal_indexer.py \
  services/geo/similarity.py \
  services/geospatial_resolver.py \
  services/rag_geospatial.py \
  services/rag_geospatial_context.py \
  services/ms_jarvis_phi_probe.py \
cat "$BASE/16-current-runtime-declarations.txt"/dev/null || trueue
===== CURRENT RUNTIME DECLARATION CHECK =====
commit: 7e58737f60ef7fad88bd91b45ad484011fc28261


--- services/jarvis_hilbert_semantic.py ---
current compose references:
1951:    - /mnt/nvme1/msjarvis-rebuild/services/jarvis_hilbert_semantic.py:/app/services/jarvis_hilbert_semantic.py:ro
current compose service-name references:
Dockerfile/entrypoint references:
docker-compose.yml:1951:    - /mnt/nvme1/msjarvis-rebuild/services/jarvis_hilbert_semantic.py:/app/services/jarvis_hilbert_semantic.py:ro
docker-compose.yml:1954:    - jarvis_hilbert_semantic:app

--- services/jarvis_hilbert_state.py ---
current compose references:
current compose service-name references:
Dockerfile/entrypoint references:
docker-compose.yml:1646:    - jarvis_hilbert_state:app

--- services/jarvis_hilbert_time.py ---
current compose references:
1979:    - /mnt/nvme1/msjarvis-rebuild/services/jarvis_hilbert_time.py:/app/services/jarvis_hilbert_time.py:ro
current compose service-name references:
Dockerfile/entrypoint references:
docker-compose.yml:1966:    - jarvis_hilbert_time:app
docker-compose.yml:1979:    - /mnt/nvme1/msjarvis-rebuild/services/jarvis_hilbert_time.py:/app/services/jarvis_hilbert_time.py:ro

--- services/hilbert_spatial_chat.py ---
current compose references:
current compose service-name references:
Dockerfile/entrypoint references:
Dockerfile.hilbert_spatial_chat:4:COPY services/hilbert_spatial_chat.py .
Dockerfile.hilbert_spatial_chat:5:CMD ["python", "hilbert_spatial_chat.py"]

--- services/integrate_spatial_temporal.py ---
current compose references:
current compose service-name references:
Dockerfile/entrypoint references:

--- services/gbim_semantic_indexer.py ---
current compose references:
current compose service-name references:
Dockerfile/entrypoint references:

--- services/gbim_spatial_indexer.py ---
current compose references:
current compose service-name references:
Dockerfile/entrypoint references:

--- services/gbim_temporal_indexer.py ---
current compose references:
current compose service-name references:
Dockerfile/entrypoint references:

--- services/geo/similarity.py ---
current compose references:
current compose service-name references:
Dockerfile/entrypoint references:

--- services/geospatial_resolver.py ---
current compose references:
current compose service-name references:
Dockerfile/entrypoint references:

--- services/rag_geospatial.py ---
current compose references:
current compose service-name references:
Dockerfile/entrypoint references:

--- services/rag_geospatial_context.py ---
current compose references:
current compose service-name references:
Dockerfile/entrypoint references:

--- services/ms_jarvis_phi_probe.py ---
current compose references:
1718:    - /mnt/nvme1/msjarvis-rebuild/services/ms_jarvis_phi_probe.py:/app/ms_jarvis_phi_probe.py:ro
current compose service-name references:
Dockerfile/entrypoint references:
docker-compose.yml:1709:    - ms_jarvis_phi_probe.py
docker-compose.yml:1718:    - /mnt/nvme1/msjarvis-rebuild/services/ms_jarvis_phi_probe.py:/app/ms_jarvis_phi_probe.py:ro

--- services/quantum_state_engine.py ---
current compose references:
current compose service-name references:
Dockerfile/entrypoint references:
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/nvme1/msjarvis-rebuild$ cd /mnt/nvme1/msjarvis-rebuild

BASE=/tmp/meaning-geometry-investigation

{
printf '%s\n' '===== TIER-1 INVESTIGATION BASELINE ====='
date --iso-8601=seconds

printf '\n===== GIT =====\n'
git rev-parse HEAD
git status --short
git symbolic-ref --short -q HEAD || echo DETACHED_HEAD

printf '\n===== RECENT COMMITS =====\n'
git log -8 --oneline --decorate

printf '\n===== ARTIFACTS =====\n'
for f in \
  11-tier1-callgraph.txt \
  12-tier1-source-extract.txt \
  13-tier1-static-graph.txt \
  13-tier1-static-graph.json \
  14-tier1-dependency-matrix.txt \
} | tee "$BASE/17-tier1-baseline.txt"\py \====\n'
===== TIER-1 INVESTIGATION BASELINE =====
2026-08-10T09:00:32-04:00

===== GIT =====
7e58737f60ef7fad88bd91b45ad484011fc28261
 M docker-compose.yml
?? $IDX
?? .current_commit.hash
?? .dockerignore
?? .env
?? .env.backup
?? .env.complete.backup
?? .format-venv/
?? .secrets/
?? .venv-chroma/
?? .venv/
?? .woah-venv/
?? 20llmFINAL.health.json
?? =
?? CACHED
?? CONSENSUS_STATS_SNAPSHOT.json
?? CURRENTSTATUS.md
?? CURRENT_LLM_STACK_NOTES.txt
?? Dockerfile
?? Dockerfile-llm1-proxy
?? Dockerfile-llm10-proxy
?? Dockerfile-llm11-proxy
?? Dockerfile-llm12-proxy
?? Dockerfile-llm13-proxy
?? Dockerfile-llm14-proxy
?? Dockerfile-llm15-proxy
?? Dockerfile-llm16-proxy
?? Dockerfile-llm17-proxy
?? Dockerfile-llm18-proxy
?? Dockerfile-llm19-proxy
?? Dockerfile-llm2-proxy
?? Dockerfile-llm20-proxy
?? Dockerfile-llm21-proxy
?? Dockerfile-llm22-proxy
?? Dockerfile-llm3-proxy
?? Dockerfile-llm4-proxy
?? Dockerfile-llm5-proxy
?? Dockerfile-llm6-proxy
?? Dockerfile-llm7-proxy
?? Dockerfile-llm8-proxy
?? Dockerfile-llm9-proxy
?? Dockerfile.20llm
?? Dockerfile.agents
?? Dockerfile.bak_before_python3_fix
?? Dockerfile.brain
?? Dockerfile.consciousnessbridge
?? Dockerfile.full_neuro
?? Dockerfile.gateway
?? Dockerfile.gis_rag
?? Dockerfile.hilbert_spatial_chat
?? Dockerfile.local_resources
?? Dockerfile.nbb_icontainers_fastapi
?? Dockerfile.neuro
?? Dockerfile.neuro-prefrontal-patched
?? Dockerfile.qualia
?? Dockerfile.qualia.bak
?? Dockerfile.rag
?? Dockerfile.rag_server
?? Dockerfile.rag_server_main
?? Dockerfile.ragservermain
?? Dockerfile.swarm
?? Dockerfile.woah
?? HOST_LEARNER_CHROMA_PATH/
?? KNOWN_LIMITATIONS_20LLM_SEQUENTIAL.txt
?? REBUILD_COMPLETE.md
?? RESTART_20LLM_FINAL.sh
?? STABLE_MODE_NOTE.txt
?? START20LLMFINAL.sh
?? START20LLMFINAL.sh.backup.20260121180532
?? START20LLMPRODUCTION.sh
?? START_GIS_RAG.sh
?? TODO_enable_real_entanglement.md
?? [internal]
?? __pycache__/
?? ai-server/
?? ai/
?? all_gis_vectors.txt
?? all_gis_vectors_filtered.txt
?? all_gis_vectors_full.txt
?? all_gis_vectors_ingest.txt
?? all_gis_vectors_unique.txt
?? api_resources.py
?? archives/
?? ask_gis.py
?? ask_gis_near_oakhill.py
?? attrs_api.py
?? attrs_test.json
?? attrs_with_geom_api.py
?? autonomouslearner.py
?? backfill_provenance.sql
?? backfill_provenance_batch.sql
?? backup_filename_index.txt
?? backup_roots.txt
?? backups/
?? bbb_requirements.txt
?? bootstrap_gbim_beliefs_eq1.py
?? brain_orchestrator.py
?? bulk_ingest.log
?? bulk_ingest_attrs.py
?? bulk_load_attrs.sh
?? call_rag_with_entanglement_example.py
?? capture_gdb_json.sh
?? chat_health.sh
?? chat_light_current.py
?? chat_recover.sh
?? chat_smoke.sh
?? check_gbim_metadata.sh
?? chroma.sqlite3
?? chroma_data/
?? chroma_db/
?? chroma_ingestion_sources.txt
?? chroma_manifest.csv
?? chroma_persistent_RAG_WORKING_20260116.tgz
?? chromadb/
?? constitutional_api.py
?? countyfp20
?? debug-logs/
?? debug_consciousness_bridge.md
?? demo_msjarvis_ranked.py
?? demo_msjarvis_resources.py
?? deploy_synthesizer.sh
?? diagnostics/
?? docker-compose-patch.yml
?? docker-compose.MOTHERCARRIE.BAK.20260216-132826
?? docker-compose.MOTHERCARRIE.BAK.20260216-132834
?? docker-compose.RAG_WORKING_20260116.yml
?? docker-compose.RAG_WORKING_20260116.yml.bak-20260122223705
?? docker-compose.RAG_WORKING_20260116.yml.bak-portfix-20260122224758
?? docker-compose.RAG_WORKING_20260116.yml.bak_gateway8050
?? docker-compose.RAG_WORKING_20260116.yml.bak_mainbrain8058
?? docker-compose.RAG_WORKING_20260116.yml.bak_python310_fix
?? docker-compose.gbim.yml
?? docker-compose.golden.bak_bbb_clean_proxy
?? docker-compose.golden.bak_bbb_proxy_cmd_fix
?? docker-compose.golden.bak_bbb_uvicorn_fix
?? docker-compose.golden.bak_before_bbb_proxy2
?? docker-compose.golden.bak_before_brain_ports_cleanup
?? docker-compose.golden.bak_before_python3_cmd_fix
?? docker-compose.golden.bak_nbb_base_final
?? docker-compose.golden.bak_python310_compose_all
?? docker-compose.golden.bak_services_mapping_fix
?? docker-compose.golden.bak_web_research_cmd
?? docker-compose.golden.yml
?? docker-compose.llm-proxies.yml
?? docker-compose.mountainshares-override.yml
?? docker-compose.override.yml
?? docker-compose.rag.yml
?? docker-compose.recovered.yml
?? docker-compose.restored.yml
?? docker-compose.restored.yml.pre-hilbert-fix-1768013541
?? docker-compose.restored.yml.safe-1768040125
?? docker-compose.working.20260118-235132.yml
?? docker-compose.working.20260119-000202.yml
?? docker-compose.yml.20llm.bak
?? docker-compose.yml.BROKEN_BACKUP
?? docker-compose.yml.after-bbb.bak
?? docker-compose.yml.backup
?? docker-compose.yml.backup.1768311648
?? docker-compose.yml.backup.1768313257
?? docker-compose.yml.backup.1768313407
?? docker-compose.yml.backup.1768786837
?? docker-compose.yml.backup.1768788421
?? docker-compose.yml.backup_20260215_232944
?? docker-compose.yml.backup_20260218_085941
?? docker-compose.yml.backup_autonomous_learner_20260109-074048
?? docker-compose.yml.backup_gateway_ports_20260109-091103
?? docker-compose.yml.backup_jan13_consciousness
?? docker-compose.yml.backup_nbb_ports
?? docker-compose.yml.backup_nbb_ports_fixed
?? docker-compose.yml.bak
?? docker-compose.yml.bak-1768791131
?? docker-compose.yml.bak-1768791194
?? docker-compose.yml.bak-1768791760
?? docker-compose.yml.bak-4sp-20260627-224406
?? docker-compose.yml.bak-cmd-20260627-224314
?? docker-compose.yml.bak-definitive-20260627-224232
?? docker-compose.yml.bak-gpu-20260626-085244
?? docker-compose.yml.bak-lmsynth-cmd-20260627-223838
?? docker-compose.yml.bak-lmsynth-cmd-20260627-223928
?? docker-compose.yml.bak-synthmount-20260627-223355
?? docker-compose.yml.bak-worker-20260626-160858
?? docker-compose.yml.bak.1768500857
?? docker-compose.yml.bak.1768781706
?? docker-compose.yml.bak.1782535145
?? docker-compose.yml.bak.20260110161005
?? docker-compose.yml.bak.20260206142334
?? docker-compose.yml.bak.20260206142646
?? docker-compose.yml.bak.20260629_025314
?? docker-compose.yml.bak_1768574001
?? docker-compose.yml.bak_add_clock
?? docker-compose.yml.bak_before_unified_fix
?? docker-compose.yml.bak_drop_images
?? docker-compose.yml.bak_drop_roche
?? docker-compose.yml.bak_ports_20260118163828
?? docker-compose.yml.bak_redis_env_1769196600
?? docker-compose.yml.bak_redis_fix_1769195136
?? docker-compose.yml.bak_redis_fix_1769195657
?? docker-compose.yml.bak_unified_cycle_fix
?? docker-compose.yml.bak_woah_20260118163402
?? docker-compose.yml.bbb.bak
?? docker-compose.yml.before_8010_fix_1768044953
?? docker-compose.yml.before_fix
?? docker-compose.yml.before_fix_20260122
?? docker-compose.yml.before_neuro_fix_1768012948
?? docker-compose.yml.broken
?? docker-compose.yml.broken-1768013498
?? docker-compose.yml.broken_backup
?? docker-compose.yml.broken_spiritual
?? docker-compose.yml.chroma-backup-20260114054916
?? docker-compose.yml.chroma-backup-20260114060013
?? docker-compose.yml.full_backup_20260122
?? docker-compose.yml.nbb.bak
?? docker-compose.yml.pre-hilbert-fix-1768013541
?? docker-compose.yml.pre_judges
?? docker-compose.yml.safe-1768040125
?? docs/
?? dump_gdb_result.sh
?? dynamic_port_service_no_flask.py
?? enrich_from_attrs.log
?? enrich_from_attrs.py
?? enrich_where.log
?? enrich_where.py
?? entityid_to_chromaid.pkl
?? env/
?? error_summary.log
?? etl/
?? example_wv_entangled_request.json
?? example_wv_entangled_response.json
?? export_chroma_8002.py
?? export_chroma_raw_8002.py
?? export_gbim_sample.py
?? exporting
?? exports/
?? fix-20llm.sh
?? fix_consensus_4010.sh
?? full_fs_indexer.sh
?? gateway-entrypoint.sh
?? gateway8050_inline.py
?? gateway_chat_attempt.log
?? gbim_backbone_rich.dump.sql
?? gbim_chroma.py
?? gbim_full_metadata.csv
?? gbim_orchestrator.py
?? gbim_sample_metadata.csv
?? gbim_worldview_entity_clean.sql
?? gbim_worldview_entity_data.sql
?? gbim_worldview_entity_fresh.sql
?? gdb_integration_service.log
?? gdb_result_snapshot.json
?? generate_attrs_sql.sh
?? generate_spiritual_inventories.py
?? geodb_collection_manifest.csv
?? geodb_restore_plan.md
?? gis_candidates_global.txt
?? gis_candidates_stage2.txt
?? gis_notes/
?? gis_pipeline_8819.log
?? gis_rag_query.py
?? gis_rag_server.py
?? gis_statewide_run.log
?? gisgeodb_storage.py
?? gisgeodbstorage.py
?? index_gis_to_chroma.py
?? index_gis_to_chroma.py.bak_20260130103111
?? ingest.log
?? ingest_attrs_to_chroma.py
?? ingest_gbimworldviewentities_from_csv.py
?? ingest_kanawha_images.py
?? ingest_kanawha_resources.py
?? ingest_missing.log
?? ingest_missing_attrs.py
?? ingest_msjarvis_corpus.py
?? ingest_personal_pdfs.py
?? ingest_wv_income_maintenance_manual.py
?? integration_layer/
?? investigation_20260807/
?? "itus_addr AS address, -- site address"
?? jarvis-chroma/
?? jarvis_eeg_beta_5m.py
?? jarvis_env.sh
?? knowledge_pdfs/
?? layer_manifest.csv
?? list_due_for_verification.py
?? llm10_health_proxy.py
?? llm10_health_proxy.py.bak-tonone-091635
?? llm11_health_proxy.py
?? llm11_health_proxy.py.bak-tonone-091635
?? llm12_health_proxy.py
?? llm12_health_proxy.py.bak-tonone-091635
?? llm13_health_proxy.py
?? llm13_health_proxy.py.bak-tonone-091635
?? llm14_health_proxy.py
?? llm14_health_proxy.py.bak-tonone-091635
?? llm15_health_proxy.py
?? llm15_health_proxy.py.bak-tonone-091635
?? llm16_health_proxy.py
?? llm16_health_proxy.py.bak-tonone-091635
?? llm17_health_proxy.py
?? llm17_health_proxy.py.bak-tonone-091635
?? llm18_health_proxy.py
?? llm18_health_proxy.py.bak-tonone-091635
?? llm19_health_proxy.py
?? llm19_health_proxy.py.bak-tonone-091635
?? llm1_health_proxy.py
?? llm1_health_proxy.py.bak-tonone-091635
?? llm20_health_proxy.py
?? llm20_health_proxy.py.bak-tonone-091635
?? llm21_health_proxy.py
?? llm21_health_proxy.py.bak-tonone-091635
?? llm22_health_proxy.py
?? llm22_health_proxy.py.bak-tonone-091635
?? llm2_health_proxy.py
?? llm2_health_proxy.py.bak-tonone-091635
?? llm3_health_proxy.py
?? llm3_health_proxy.py.bak-tonone-091635
?? llm4_health_proxy.py
?? llm4_health_proxy.py.bak-tonone-091635
?? llm5_health_proxy.py
?? llm5_health_proxy.py.bak-tonone-091635
?? llm6_health_proxy.py
?? llm6_health_proxy.py.bak-tonone-091635
?? llm7_health_proxy.py
?? llm7_health_proxy.py.bak-tonone-091635
?? llm8_health_proxy.py
?? llm8_health_proxy.py.bak-tonone-091635
?? llm9_health_proxy.py
?? llm9_health_proxy.py.bak-tonone-091635
?? llm_health_proxies/
?? load_all_attrs.sql
?? load_hospitals.sql
?? load_services_attrs_and_enrich.py
?? local_resources_export.csv
?? logs-archive/
?? logs-gis_rag_server_8055.log
?? logs-rag_server.log
?? logs-rag_server_8003.log
?? logs-rag_server_dynamic.log
?? logs/
?? main.py
?? main_brain.py
?? mainbrain.log
?? missing_collections.csv
?? missing_local_files.txt
?? missing_source_epochs.csv
?? models.py
?? ms_jarvis_unified_gateway.py
?? msjarvis_chroma_test.py
?? msjarvis_embed_gbim.py
?? msjarvis_embed_gbim_resume_tail.py
?? msjarvis_resources.py
?? msjarvis_tests/
?? msjarvisragserverwvpatch.py
?? msjarviswoahalgorithms.py
?? naming
?? nbb_woah_algorithms_fix.patch
?? neuro-prefrontalcortex-patched.tar
?? neurobiological_brain/
?? neurobiologicalbrain/
?? neurobiologicalbrainmothercarrieprotocolsservice/
?? nginx.conf
?? nohup.out
?? old_drive_gis_candidates.txt
?? package-lock.json
?? patch_llm_health_endpoints.sh
?? pdf_utils.py
?? persistent_chroma_old
?? pg_hba.conf
?? post-fix-automation.sh
?? probe_gdb_integration.sh
?? process_wv_layers.py
?? processstatewidegisbulk_.log
?? processstatewidegisbulk_8819.log
?? proposals/
?? pull_jarvis_models.sh
?? query_msjarvis_corpus.py
?? query_msjarvis_once.py
?? quick_gdb_probe.sh
?? rag_insert_mountainshares.py
?? rag_integration_snapshot.tgz
?? rag_local_resources.py
?? rag_server_main.py
?? rag_server_main.py.bak.1768180485
?? ragservermain.current.log
?? ragservermain.py
?? ragsimple.current.log
?? reading
?? reingest_msjarvis_chunks.py
?? reload_geodb_bootstrap.sh
?? requirements.txt
?? resolving
?? resource_assistant.py
?? resource_ranker.py
?? resources/
?? restart_unified_msjarvis.sh
?? restore_missing_files.sh
?? run_core_ops.sh
?? run_gbim_import.sh
?? run_gis_stack.sh
?? run_sanctuary_import.sh
?? scripts/
?? secrets/
?? seed_full_knowledge.py
?? seed_gbim_catalog.py
?? seed_mountainshares.py
?? service_build_matrix.txt
?? service_discovery_no_redis.py
?? service_registry_client_stub.py
?? services/.chromadb/
?? services/.dockerignore
?? services/.env
?? services/.env.registration
?? services/.env.stage2
?? services/.venv/
?? services/20LLM_DEPLOYMENT_SUMMARY.md
?? services/911centers_wvdem_032819_gcs84_attrs.csv
?? services/911centers_wvdem_032819_utm83_attrs.csv
?? services/ADDITIONAL_SERVICES.py
?? services/ADDITIONAL_SERVICES_FINAL.py
?? services/ADD_ALL_INTEGRATIONS.sh
?? services/ADD_DELETE_ENDPOINT.sh
?? services/ADD_MEMORY_TO_8050.sh
?? services/ADD_METADATA_FILTERING.sh
?? services/ADD_RAG_METADATA_FILTERING.sh
?? services/ADD_RAG_RETRIEVAL_8050.sh
?? services/ADD_STORE_ENDPOINT.sh
?? services/ADVANCED_MODULES_ROADMAP.md
?? services/AGI_EVALUATION_SUITE.sh
?? services/AGI_TEST_SUITE.sh
?? services/AGI_TEST_V2.sh
?? services/ARCHITECTURE_OPTIONS.md
?? services/AaaCPE_Appalachian_Dialect_Knowledge.txt
?? services/BUILD_EGERIA_WEB_UI.sh
?? services/CHECK_AND_BUILD_MEMORY.sh
?? services/CHECK_AND_FIX_PORT.sh
?? services/CHECK_MS_JARVIS_STATUS.sh
?? services/CLEANUP_OLLAMA.sh
?? services/COLLECTIVE_INTEGRATION_PLAN.md
?? services/COLLECT_ALL_DOCS_FOR_NOTEBOOKLM.sh
?? services/COMPARE_4_VS_22.sh
?? services/COMPLETE_DISCOVERY_REPORT.md
?? services/COMPLETE_PORT_MAP.sh
?? services/COMPLETE_PORT_SCAN.sh
?? services/COMPLETE_SESSION_ACCOMPLISHMENTS.md
?? services/COMPLETE_START_SYSTEM.sh
?? services/COMPLETE_SYSTEM_STATUS.md
?? services/COMPLETE_SYSTEM_SUMMARY.md
?? services/COMPREHENSIVE_PORT_AUDIT_20251009_234234.txt
?? services/COMPREHENSIVE_SYSTEM_TEST.sh
?? services/CONSCIOUSNESS_ARCHITECTURE_EXPLAINED.md
?? services/CONSCIOUSNESS_FINAL.log
?? services/CONSTITUTIONAL_SCHEDULER_ENTRY.txt
?? services/CONSTITUTIONAL_SYSTEM_MANIFEST.md
?? services/CREATE_ULTIMATE_JARVIS.sh
?? services/CRITICAL_FIXES_NEEDED.md
?? services/CURRENT_STATUS.md
?? services/ConfigLoader.py
?? services/DEPLOYMENT_ORDER.txt
?? services/DEPLOYMENT_STATUS_REPORT.md
?? services/DEPLOY_22LLM_COLLECTIVE.sh
?? services/DIAGNOSE.sh
?? services/Dockerfile
?? services/Dockerfile-chroma-proxy
?? services/Dockerfile-llm1-proxy
?? services/Dockerfile-llm10-proxy
?? services/Dockerfile-llm11-proxy
?? services/Dockerfile-llm12-proxy
?? services/Dockerfile-llm13-proxy
?? services/Dockerfile-llm14-proxy
?? services/Dockerfile-llm15-proxy
?? services/Dockerfile-llm16-proxy
?? services/Dockerfile-llm17-proxy
?? services/Dockerfile-llm18-proxy
?? services/Dockerfile-llm19-proxy
?? services/Dockerfile-llm2-proxy
?? services/Dockerfile-llm20-proxy
?? services/Dockerfile-llm21-proxy
?? services/Dockerfile-llm22-proxy
?? services/Dockerfile-llm3-proxy
?? services/Dockerfile-llm4-proxy
?? services/Dockerfile-llm5-proxy
?? services/Dockerfile-llm6-proxy
?? services/Dockerfile-llm7-proxy
?? services/Dockerfile-llm8-proxy
?? services/Dockerfile-llm9-proxy
?? services/Dockerfile.69dgm_bridge
?? services/Dockerfile.aaacpe_rag
?? services/Dockerfile.aaacpe_scraper
?? services/Dockerfile.agents
?? services/Dockerfile.autonomous_complete
?? services/Dockerfile.autonomous_learner
?? services/Dockerfile.autonomous_learner_complete
?? services/Dockerfile.bak_add_deps
?? services/Dockerfile.bak_add_redis
?? services/Dockerfile.bak_add_requests
?? services/Dockerfile.bak_add_service_discovery
?? services/Dockerfile.bak_before_bbb_copy_fix
?? services/Dockerfile.bak_runner_cmd
?? services/Dockerfile.bbb
?? services/Dockerfile.constitutional_guardian
?? services/Dockerfile.crypto-policy
?? services/Dockerfile.dgm_orchestrator
?? services/Dockerfile.dgm_worker
?? services/Dockerfile.email
?? services/Dockerfile.fifth_dgm_real
?? services/Dockerfile.gateway
?? services/Dockerfile.hippocampus.bak.20260626235712
?? services/Dockerfile.icontainers
?? services/Dockerfile.icontainers_fastapi
?? services/Dockerfile.intake
?? services/Dockerfile.judge
?? services/Dockerfile.lm_synthesizer
?? services/Dockerfile.memory
?? services/Dockerfile.mother_protocols
?? services/Dockerfile.nbb_*
?? services/Dockerfile.nbb_base
?? services/Dockerfile.pia-sampler
?? services/Dockerfile.psychological_rag
?? services/Dockerfile.psychology_services
?? services/Dockerfile.qualia
?? services/Dockerfile.rag
?? services/Dockerfile.rag_server
?? services/Dockerfile.roche_llm
?? services/Dockerfile.roche_llm.disabled
?? services/Dockerfile.semaphore
?? services/Dockerfile.spiritual_rag
?? services/Dockerfile.temporal_consciousness
?? services/Dockerfile.toroidal
?? services/Dockerfile.web_research
?? services/Dockerfile.webdeploy
?? services/Dockerfile.woah
?? services/Dockerfile.woah_algorithms
?? services/EGERIA_AGI_TEST_RESULTS_SUMMARY.md
?? services/EGERIA_IDENTITY.md
?? services/EMERGENCY_PROMPT_LEAK_FIX.sh
?? services/FEATURE_ENHANCEMENTS.md
?? services/FIFTH_DGM_RESTORED.md
?? services/FINAL_8_LAYER_STARTUP.sh
?? services/FINAL_DEPLOYMENT_SUMMARY.md
?? services/FINAL_EMOTIONAL_BALANCE.sh
?? services/FINAL_FIX.sh
?? services/FINAL_PERSONA_FIX.sh
?? services/FINAL_RECOMMENDATION.md
?? services/FINAL_STATUS_SUMMARY.md
?? services/FINAL_SUCCESS.log
?? services/FINAL_SYSTEM_REPORT.md
?? services/FINAL_WITH_OSM.log
?? services/FINAL_WORKING.log
?? services/FIX_BOTH_ISSUES.sh
?? services/FIX_CONSCIOUSNESS_BRIDGE.sh
?? services/FIX_CONSCIOUSNESS_INTEGRATION.sh
?? services/FIX_CONSCIOUS_COLLECTIVE_AUTO.sh
?? services/FIX_FAST_MODE.sh
?? services/FIX_HEALTH_ENDPOINTS.sh
?? services/FIX_MEMORY_STORAGE.sh
?? services/FIX_MODEL_IDENTITY.sh
?? services/FIX_RAG_FILTERING.sh
?? services/FIX_SYNTHESIS_PROMPT.sh
?? services/FIX_TIMEOUT_ISSUE.sh
?? services/FIX_TONE_AND_CONCISENESS.sh
?? services/FIX_ULTIMATE.sh
?? services/FIX_UNIFIED_SELF.sh
?? services/FULL_DEPLOYMENT_MANIFEST.txt
?? services/FULL_INTEGRATION_WORKFLOW.sh
?? services/FULL_PORT_AUDIT.sh
?? services/FULL_PORT_SCAN.sh
?? services/FULL_SERVICE_AUDIT.sh
?? services/FULL_SYSTEM_AUDIT.sh
?? services/GPU_OPTIMIZATION_GUIDE.md
?? services/GUARANTEED_8_LAYER_START.sh
?? services/IDENTIFY_SERVICES.sh
?? services/IMMUTABLE_MANIFEST.md
?? services/INSPECT_JARVIS_INTERNALS.sh
?? services/INTEGRATE_8020_8050.sh
?? services/INTEGRATE_CONSCIOUSNESS.sh
?? services/INTEGRATE_CONSCIOUSNESS_TO_DEEP_MODE.sh
?? services/INTEGRATE_PROPERLY.sh
?? services/INTEGRATION_HUB_SUCCESS.md
?? services/INTEGRATION_IMPLEMENTATION.py
?? services/INTEGRATION_IMPLEMENTATION.py.pre_dynamic_discovery
?? services/INTEGRATION_PLAN.sh
?? services/JARVIS_DASHBOARD.sh
?? services/JARVIS_HEALTH_CHECK.sh
?? services/LOAD_AAACPE_RAG.sh
?? services/LOCATION_AWARENESS_SUCCESS.md
?? services/MAMMA_KIDD_PROTOCOL_GUIDE.md
?? services/MAMMA_KIDD_QUICK_REFERENCE.txt
?? services/MEGA_CONSCIOUSNESS.log
?? services/METHOD_AUDIT_RAW.txt
?? services/METHOD_AUDIT_SEG_aa
?? services/METHOD_AUDIT_SEG_ab
?? services/METHOD_AUDIT_SEG_ac
?? services/METHOD_AUDIT_SEG_ad
?? services/METHOD_AUDIT_SEG_ae
?? services/METHOD_AUDIT_SEG_af
?? services/METHOD_AUDIT_SEG_ag
?? services/METHOD_AUDIT_SEG_ah
?? services/METHOD_AUDIT_SEG_ai
?? services/METHOD_AUDIT_SEG_aj
?? services/METHOD_AUDIT_SEG_ak
?? services/METHOD_AUDIT_SEG_al
?? services/METHOD_AUDIT_SEG_am
?? services/METHOD_AUDIT_SEG_an
?? services/METHOD_AUDIT_SEG_ao
?? services/METHOD_AUDIT_SEG_ap
?? services/METHOD_AUDIT_SEG_aq
?? services/MS_JARVIS_COMPLETE_AUDIT.md
?? services/MS_JARVIS_DEEP_MODE_DEPLOYMENT.md
?? services/MS_JARVIS_DEPLOYMENT_SUCCESS.md
?? services/MS_JARVIS_FINAL_DEPLOYMENT.sh
?? services/MS_JARVIS_FINAL_VICTORY_REPORT.md
?? services/MS_JARVIS_PRODUCTION_FINAL.sh
?? services/MS_JARVIS_STATUS_REPORT.md
?? services/MS_JARVIS_ULTIMATE_AUDIT_20251010_002719.txt
?? services/Modelfile.egeria
?? services/MountainShares6.pdf
?? services/OLLAMA_HEALTH_FEATURES.md
?? services/OPTIMIZED.log
?? services/OPTIMIZE_GPU.sh
?? services/PORTS_REGISTRY_RAW.txt
?? services/PORT_AUDIT.sh
?? services/PORT_AUDIT_RAW.txt
?? services/PORT_AUDIT_SEG_aa
?? services/PORT_AUDIT_SEG_ab
?? services/PORT_AUDIT_SEG_ac
?? services/PORT_AUDIT_SEG_ad
?? services/PORT_AUDIT_SEG_ae
?? services/PORT_SEG_aa
?? services/PORT_SEG_ab
?? services/PORT_SEG_ac
?? services/PORT_SEG_ad
?? services/PORT_SERVICE_AUDIT.sh
?? services/PRODUCTION_DEPLOYMENT_COMPLETE.md
?? services/PRODUCTION_DEPLOYMENT_SUITE.sh
?? services/PRODUCTION_MS_JARVIS_START.sh
?? services/PRODUCTION_STATUS_REPORT.txt
?? services/REFERENCE_windows_swarm.py
?? services/REMOVE_MODEL_REFERENCES.sh
?? services/REROUTE_SERVICES.sh
?? services/RESTART_PLAN.md
?? services/RESTORATION_CERTIFICATE.txt
?? services/RESTORATION_CERTIFICATE_CORRECTED.txt
?? services/RESTORE_ALL_INTEGRATIONS.sh
?? services/RESTORE_NATURAL_PERSONALITY.sh
?? services/SAFE_INTEGRATION_PLAN.md
?? services/SATURDAY_SUMMARY.md
?? services/SCHEDULER_REFERENCE.md
?? services/SCRIPT_NAME.log
?? services/SET_MAX_RESPONSE.sh
?? services/SPATIOTEMPORAL.log
?? services/SPATIOTEMPORAL_CONSCIOUSNESS.md
?? services/START_19LLM_PRODUCTION.sh
?? services/START_20LLM_FINAL.sh
?? services/START_ALL_SYSTEMS.sh
?? services/START_COMPLETE_SYSTEM.sh
?? services/START_CONSCIOUS_COLLECTIVE.sh
?? services/START_MS_JARVIS_PRODUCTION.sh
?? services/STOP_ALL_SYSTEMS.sh
?? services/SUCCESS.log
?? services/SWAGGER_ENDPOINTS.md
?? services/SWITCH_TO_22LLM_DEFAULT.sh
?? services/SYSTEM_AUDIT_20251009_233918.txt
?? services/SYSTEM_AUDIT_ANALYSIS.md
?? services/SYSTEM_STATUS_FINAL.md
?? services/TEST_CRITICAL_FIXES.sh
?? services/TEST_IMPROVED_RESPONSE.sh
?? services/TEST_WITH_CLEANUP.sh
?? services/TODAYS_COMPLETE_ACHIEVEMENT.md
?? services/TODAYS_PROGRESS.md
?? services/TRUE_BRAIN_ARCHITECTURE.md
?? services/ULTIMATE_PORT_AUDIT_20251010_094847.txt
?? services/ULTIMATE_SESSION_SUMMARY.md
?? services/UPDATE_COORDINATOR_FOR_DEEP_MODE.sh
?? services/UPDATE_JARVIS_PERSONA.sh
?? services/UPDATE_NAME_TO_EGERIA.sh
?? services/WATCHDOG.sh
?? services/WATCHDOG_LOG.txt
?? services/WORKING.log
?? services/WORKING_START.sh
?? services/WVU_API_DOCUMENTATION.md
?? services/__init__.py
?? services/__pycache__/
?? services/_evaluate_for_i_container
?? services/_redirects
?? services/aaacpe_initial_ingest.py
?? services/aaacpe_rag_service.py
?? services/aaacpe_scraper.log
?? services/aaacpe_scraper_service.py
?? services/aacpe_ingest_community.py
?? services/aacpe_prepare_metadata.py
?? services/aapcappe_ingest.py
?? services/academic_research_gateway_8062.log
?? services/academic_research_gateway_8062.py
?? services/academic_research_gateway_8062_cors.py
?? services/academic_whitebox_api.py
?? services/activate_dgm.py
?? services/activate_dgm.py.backup_1762520105
?? services/activate_dgm_4012.log
?? services/activate_dgm_9485.log
?? services/activate_dgm_enhanced.py
?? services/activate_dgm_enhanced_9329.log
?? services/activate_egeria_persona.py
?? services/activate_sanctuary_cherubim_guards.sh
?? services/add_auto_store.py
?? services/add_background_call.py
?? services/add_background_storage.py
?? services/add_background_storage_9618.log
?? services/add_chat_route.sh
?? services/add_conversation_context.py
?? services/add_conversation_endpoint.py
?? services/add_conversation_storage.py
?? services/add_conversation_storage_9024.log
?? services/add_dynamic_context.py
?? services/add_fast_layer.py
?? services/add_fifth_dgm_to_chat.py
?? services/add_fifth_dgm_to_chat_9176.log
?? services/add_full_brain_class.py
?? services/add_full_brain_class.py.pre_dynamic_discovery
?? services/add_gpu_cleanup_correct.py
?? services/add_gpu_cleanup_every_3.py
?? services/add_identity_context.py
?? services/add_jarvis_personality.py
?? services/add_jarvis_personality_9995.log
?? services/add_learning_suggestion.py
?? services/add_mamma_greeting_simple.py
?? services/add_messenger_to_gateway.py
?? services/add_new_consciousness_services.py
?? services/add_new_consciousness_services.py.backup_vocabulary_cleanup
?? services/add_proactive_cleanup_working.sh
?? services/add_ready_endpoint.py
?? services/add_security_to_chat.py
?? services/add_semaphore.py
?? services/add_semaphore.py.backup_vocabulary_cleanup
?? services/add_simple_gpu_cleanup.py
?? services/add_swagger_to_ports.py
?? services/add_swagger_to_ports.py.backup_vocabulary_cleanup
?? services/add_swagger_to_rag.py
?? services/add_swagger_to_rag_9351.log
?? services/add_to_consciousness_engine.txt
?? services/add_to_main_consciousness.psychology_patched.py
?? services/add_to_main_consciousness.py
?? services/add_to_main_consciousness.py.backup_20251031
?? services/add_to_startup.sh
?? services/add_user_memory.py
?? services/add_user_memory_attribute.py
?? services/add_web_research_storage.py
?? services/add_web_research_storage_9052.log
?? services/add_working_search.py
?? services/advanced_service_dashboard.py
?? services/agent_llm_batch.sh
?? services/agent_llm_batch_all.sh
?? services/agents.csv
?? services/agents_healthy.csv
?? services/agents_main.py
?? services/agi_test.sh
?? services/agi_test_results_20251012_220734.log
?? services/ai-server/
?? services/ai/
?? services/ai_ai_server_11llm_OPTIMIZED.current.log
?? services/ai_server.py
?? services/ai_server.py.backup.20251006_101858
?? services/ai_server.py.backup.20251006_110515
?? services/ai_server.py.backup_vocabulary_cleanup
?? services/ai_server.py.pre_dynamic_discovery
?? services/ai_server_11llm_OPTIMIZED.current.log
?? services/ai_server_11llm_OPTIMIZED.py
?? services/ai_server_11llm_OPTIMIZED.py.backup_simple
?? services/ai_server_11llm_OPTIMIZED.py.bak_1760568396}
?? services/ai_server_11llm_OPTIMIZED.py.bak_1765074137
?? services/ai_server_19llm_CONSCIOUS.backup_1760308857
?? services/ai_server_19llm_CONSCIOUS.backup_1760356912
?? services/ai_server_19llm_CONSCIOUS.backup_20251013_082519.py
?? services/ai_server_19llm_CONSCIOUS.backup_20251013_083103.py
?? services/ai_server_19llm_CONSCIOUS.backup_20251013_083103.py.backup_vocabulary_cleanup
?? services/ai_server_19llm_CONSCIOUS.backup_20251026_200122.py
?? services/ai_server_19llm_CONSCIOUS.backup_20251110_135425.py
?? services/ai_server_19llm_CONSCIOUS.log
?? services/ai_server_19llm_CONSCIOUS.py
?? services/ai_server_19llm_CONSCIOUS.py.backup-before-identity-fix
?? services/ai_server_19llm_CONSCIOUS.py.backup-cors
?? services/ai_server_19llm_CONSCIOUS.py.backup_20251012_125750
?? services/ai_server_19llm_CONSCIOUS.py.backup_20251012_153915
?? services/ai_server_19llm_CONSCIOUS.py.backup_before_bbb
?? services/ai_server_19llm_CONSCIOUS.py.backup_before_clarity
?? services/ai_server_19llm_CONSCIOUS.py.backup_before_proactive
?? services/ai_server_19llm_CONSCIOUS.py.backup_dgm_fix
?? services/ai_server_19llm_CONSCIOUS.py.backup_final
?? services/ai_server_19llm_CONSCIOUS.py.backup_identity_fix
?? services/ai_server_19llm_CONSCIOUS.py.backup_no_integrations
?? services/ai_server_19llm_CONSCIOUS.py.backup_pronouns
?? services/ai_server_19llm_CONSCIOUS.py.backup_unified_self
?? services/ai_server_19llm_CONSCIOUS.py.before_egeria
?? services/ai_server_19llm_CONSCIOUS.py.before_gpu_opt
?? services/ai_server_19llm_CONSCIOUS.py.before_integration
?? services/ai_server_19llm_CONSCIOUS.py.before_memory
?? services/ai_server_19llm_CONSCIOUS.py.before_metadata
?? services/ai_server_19llm_CONSCIOUS.py.before_phase1
?? services/ai_server_19llm_CONSCIOUS.py.before_phase2
?? services/ai_server_19llm_CONSCIOUS.py.before_phase3
?? services/ai_server_19llm_CONSCIOUS.py.before_phase4_5
?? services/ai_server_19llm_CONSCIOUS.py.before_phase6
?? services/ai_server_19llm_CONSCIOUS.py.before_retrieval
?? services/ai_server_19llm_CONSCIOUS.py.before_working_fix
?? services/ai_server_19llm_PRODUCTION.log
?? services/ai_server_19llm_PRODUCTION.py
?? services/ai_server_19llm_PRODUCTION.py.backup_vocabulary_cleanup
?? services/ai_server_19llm_PRODUCTION_WITH_HEALTH.log
?? services/ai_server_19llm_PRODUCTION_WITH_HEALTH.py
?? services/ai_server_19llm_PRODUCTION_WITH_HEALTH.py.backup_pre_consciousness
?? services/ai_server_20llm_FINAL.log
?? services/ai_server_20llm_FINAL.py
?? services/ai_server_20llm_FINAL.py,
?? services/ai_server_20llm_FINAL.py.backup.20260121180532
?? services/ai_server_20llm_PRODUCTION.current.log
?? services/ai_server_20llm_PRODUCTION.log
?? services/ai_server_20llm_PRODUCTION.py
?? services/ai_server_20llm_PRODUCTION.py.bak-conc-092558
?? services/ai_server_20llm_PRODUCTION.py.bak-conc21-093008
?? services/ai_server_20llm_PRODUCTION.py.bak-conc21-094919
?? services/ai_server_20llm_PRODUCTION.py.bak-conc21-094946
?? services/ai_server_20llm_PRODUCTION.py.bak-seq-20260626-082647
?? services/ai_server_20llm_PRODUCTION.py.bak-tonone-091526
?? services/ai_server_20llm_PRODUCTION.py.bak.rural_clause_and_bakllava_cleanup.20260626_212840
?? services/ai_server_20llm_PRODUCTION.py.pre_dynamic_discovery
?? services/ai_server_20llm_PRODUCTION.py.pre_expert_responses
?? services/ai_server_22llm.current.log
?? services/ai_server_22llm.psychology_patched.py
?? services/ai_server_22llm.psychology_patched.py.backup_before_portmanager
?? services/ai_server_22llm.psychology_patched.py.pre_dynamic_discovery
?? services/ai_server_22llm.psychology_patched_FIXED.log
?? services/ai_server_22llm.psychology_patched_FIXED.py
?? services/ai_server_22llm.py
?? services/ai_server_22llm.py.backup_1759895246
?? services/ai_server_22llm.py.backup_1759895560
?? services/ai_server_22llm.py.backup_ai_minds
?? services/ai_server_22llm.py.backup_before_batch
?? services/ai_server_22llm.py.backup_before_model_fix
?? services/ai_server_22llm.py.backup_before_roche
?? services/ai_server_22llm.py.backup_before_synthesis_fix
?? services/ai_server_22llm.py.backup_final_balance
?? services/ai_server_22llm.py.backup_pre_synthesis
?? services/ai_server_22llm.py.backup_prompt_leak
?? services/ai_server_22llm.py.backup_synthesis_fix
?? services/ai_server_22llm.py.backup_tone_fix
?? services/ai_server_22llm.py.backup_vocabulary_cleanup
?? services/ai_server_22llm.py.pre-semaphore
?? services/ai_server_22llm.py.pre_dynamic_discovery
?? services/ai_server_22llm.py.pre_judge_integration
?? services/ai_server_22llm_FIXED.log
?? services/ai_server_22llm_FIXED.py
?? services/ai_server_22llm_SEQUENTIAL.py
?? services/ai_server_22llm_SEQUENTIAL_OPTIMIZED_ORDER.py
?? services/ai_server_22llm_SMALL_TO_LARGE.py
?? services/ai_server_4llm.py
?? services/ai_server_4llm.py.backup_before_portmanager
?? services/ai_server_integrated.py
?? services/ai_server_integrated.py.pre_dynamic_discovery
?? services/ai_server_original_backup.py
?? services/ai_server_original_backup.py.backup_before_portmanager
?? services/ai_server_restored.py
?? services/ai_server_restored.py.backup_before_portmanager
?? services/ai_teams_config.py
?? services/alert_venv/
?? services/alerting_config.json
?? services/alertingconfig.json
?? services/all_actual_py.txt
?? services/all_actual_services.txt
?? services/all_build_dirs.txt
?? services/all_service_ports.txt
?? services/all_services.txt
?? services/all_services_compose_blocks.txt
?? services/all_services_compose_blocks_dynamic.txt
?? services/amtrackrails_federalrailroadadministration_200210_ll83_attrs.csv
?? services/amtrackrails_federalrailroadadministration_200210_utm83_attrs.csv
?? services/analyze_advanced_modules.sh
?? services/apk-list.txt
?? services/app.js
?? services/apply_ollama_fix.py
?? services/apt-list.txt
?? services/async_polling_architecture.py
?? services/attention_multimodal_fuser.py
?? services/attention_pipeline.py
?? services/attention_priority_scheduler.py
?? services/attention_router.py
?? services/audit_all_services.sh
?? services/audit_all_services_complete.sh
?? services/audit_attrs.py
?? services/audit_attrs.py.backup_20251205234718
?? services/audit_attrs.py.backup_20251205234841
?? services/audit_docker_services.sh
?? services/audit_local_state.py
?? services/audit_performance.sh
?? services/audit_service_connectivity.sh
?? services/auth.py
?? services/auto_fix_gateway.py
?? services/auto_fix_gateway.py.pre_dynamic_discovery
?? services/auto_memory_service_probe.sh
?? services/auto_rag_builder.py
?? services/auto_rag_builder_9715.log
?? services/auto_stop.log
?? services/auto_stop_after_monongalia.sh
?? services/autonomous_learner.current.log
?? services/autonomous_learner.log
?? services/autonomous_learner.py
?? services/autonomous_learner_gisgeodb_wrapper.psychology_patched.py
?? services/autonomous_learner_gisgeodb_wrapper.py
?? services/autonomous_learner_gisgeodb_wrapper.py.backup_20251031
?? services/autonomous_learner_topic_source.py
?? services/available_models.txt
?? services/backfill_gbim_worldview_metadata.py
?? services/backfill_gbim_worldview_metadata_v2.py
?? services/background_curator.py
?? services/backup_chroma_autonomous_learning.json
?? services/backup_chroma_mountainshares_knowledge.json
?? services/backup_chroma_research_history.json
?? services/batch1.csv
?? services/batch2.csv
?? services/batch3.csv
?? services/batch4.csv
?? services/batch_copy_docs.sh
?? services/batch_normalize_beliefs.py
?? services/batch_patch_services.py
?? services/bbb_ethics_proxy.py
?? services/bbb_requirements.txt
?? services/bbb_validator.py
?? services/belief_integrator.py
?? services/belief_revision_engine.py
?? services/belief_state_schema.py
?? services/benefits_chat.py
?? services/blockgroups_census_2000_ll83_attrs.csv
?? services/blockgroups_census_2000_utm83_attrs.csv
?? services/blockgroups_census_201111_gcs83_attrs.csv
?? services/blockgroups_census_201111_utm83_attrs.csv
?? services/blockgroups_census_2020_utm83_attrs.csv
?? services/blockgroups_census_2020_wma84_attrs.csv
?? services/blocks_census_2020_utm83_attrs.csv
?? services/blocks_census_2020_wma84_attrs.csv
?? services/blood_brain_barrier.log
?? services/boundaryappalachianbasin_wvges_1996_utm83_attrs.csv
?? services/brain.js
?? services/brain_orchestrator.py
?? services/brain_orchestrator.py.bak_1769197532
?? services/brain_orchestrator.py.bak_1769197625
?? services/brain_orchestrator_main.py
?? services/bridge1.log
?? services/bridge_69dgm.py
?? services/bridge_autonomous_to_i_container_dgm_woah.psychology_patched.py
?? services/bridge_autonomous_to_i_container_dgm_woah.py
?? services/bridge_autonomous_to_i_container_dgm_woah.py.backup_20251031
?? services/bridge_autonomous_to_i_container_fixed.py
?? services/bridge_cross_dgm.py
?? services/bridge_cross_dgm_10001.py
?? services/bridge_cross_dgm_10002.py
?? services/bridge_cross_dgm_10003.py
?? services/bridge_cross_dgm_10004.py
?? services/bridge_cross_dgm_10005.py
?? services/bridge_cross_dgm_10006.py
?? services/bridge_cross_dgm_10007.py
?? services/bridge_cross_dgm_10008.py
?? services/bridge_cross_dgm_10009.py
?? services/bridge_cross_dgm_10010.py
?? services/bridge_cross_dgm_10011.py
?? services/bridge_cross_dgm_10012.py
?? services/bridge_cross_dgm_10013.py
?? services/bridge_cross_dgm_10014.py
?? services/bridge_cross_dgm_10015.py
?? services/bridge_cross_dgm_10016.py
?? services/bridge_cross_dgm_10017.py
?? services/bridge_cross_dgm_10018.py
?? services/bridge_cross_dgm_10019.py
?? services/bridge_cross_dgm_10020.py
?? services/bridge_cross_dgm_10021.py
?? services/bridge_cross_dgm_10022.py
?? services/bridge_cross_dgm_10023.py
?? services/bridge_cross_dgm_10024.py
?? services/bridge_cross_dgm_10025.py
?? services/bridge_cross_dgm_10026.py
?? services/bridge_cross_dgm_10027.py
?? services/bridge_cross_dgm_10028.py
?? services/bridge_cross_dgm_10029.py
?? services/bridge_cross_dgm_10030.py
?? services/bridge_cross_dgm_10031.py
?? services/bridge_cross_dgm_10032.py
?? services/bridge_cross_dgm_10033.py
?? services/bridge_cross_dgm_10034.py
?? services/bridge_cross_dgm_10035.py
?? services/bridge_cross_dgm_10036.py
?? services/bridge_cross_dgm_10037.py
?? services/bridge_cross_dgm_10038.py
?? services/bridge_cross_dgm_10039.py
?? services/bridge_cross_dgm_10040.py
?? services/bridge_cross_dgm_10041.py
?? services/bridge_cross_dgm_10042.py
?? services/bridge_cross_dgm_10043.py
?? services/bridge_cross_dgm_10044.py
?? services/bridge_cross_dgm_10045.py
?? services/bridge_cross_dgm_10046.py
?? services/bridge_cross_dgm_10047.py
?? services/bridge_cross_dgm_10048.py
?? services/bridge_cross_dgm_10049.py
?? services/bridge_cross_dgm_10050.py
?? services/bridge_cross_dgm_10051.py
?? services/bridge_cross_dgm_10052.py
?? services/bridge_cross_dgm_10053.py
?? services/bridge_cross_dgm_10054.py
?? services/bridge_cross_dgm_10055.py
?? services/bridge_cross_dgm_10056.py
?? services/bridge_cross_dgm_10057.py
?? services/bridge_cross_dgm_10058.py
?? services/bridge_cross_dgm_10059.py
?? services/bridge_cross_dgm_10060.py
?? services/bridge_cross_dgm_10061.py
?? services/bridge_cross_dgm_10062.py
?? services/bridge_cross_dgm_10063.py
?? services/bridge_cross_dgm_10064.py
?? services/bridge_cross_dgm_10065.py
?? services/bridge_cross_dgm_10066.py
?? services/bridge_cross_dgm_10067.py
?? services/bridge_cross_dgm_10068.py
?? services/bridge_cross_dgm_10069.py
?? services/bridge_manifest.csv
?? services/bridge_manifest_FULL_BACKUP.csv
?? services/bridge_manifest_batch2.csv
?? services/bridge_manifest_core69.csv
?? services/bridge_manifest_critical_add.csv
?? services/bridge_manifest_priority_services.csv
?? services/bridge_manifest_services_only.csv
?? services/bridge_manifest_with_utilities_backup.csv
?? services/bridge_openapi.json
?? services/bridgecrossdgm*.log
?? services/bridgecrossdgm100*.log
?? services/bridges_attrs.csv
?? services/build_additional_services.py
?? services/build_autonomous.sh
?? services/build_compose.sh
?? services/build_dir_audit.txt
?? services/build_entityid_to_chromaid_map.py
?? services/build_project_impact_graph.py
?? services/bulk_build_beliefs.py
?? services/bulk_compose_rewrite.py
?? services/bulk_load_MAXIMUM.py
?? services/bulk_load_knowledge.py
?? services/bulk_sync_gis_to_chromadb.py
?? services/calderl_reg_ll83_attrs.csv
?? services/chat_endpoint_universal.py
?? services/chat_interface.html
?? services/chat_interface.html.backup_1761146565
?? services/chat_response.json
?? services/chat_server.py
?? services/chat_with_jarvis.sh
?? services/chat_worker.py
?? services/chat_worker.py.bak-brainswap-20260627-215557
?? services/chat_worker.py.bak-logfix-220611
?? services/chat_worker.py.bak-timeout-220749
?? services/check_agent_prompts.sh
?? services/check_mamma_kidd_protocol.sh
?? services/check_msjarvis_status.sh
?? services/check_permissions.sh
?? services/chroma/
?? services/chroma_client.py
?? services/chroma_client_old.py
?? services/chroma_config.py
?? services/chroma_db_corrupted2_1141/
?? services/chroma_health_monitor.py
?? services/chroma_health_proxy.py
?? services/chroma_health_utils.py
?? services/chroma_inspect_venv/
?? services/chroma_manifest.csv
?? services/chroma_python_test.py
?? services/chroma_test.py
?? services/chromadb/
?? services/chromadb_client.py
?? services/chromadb_main.py
?? services/chromadb_rag_helper.py
?? services/chromadb_rag_helper.py.pre_dynamic_discovery
?? services/chromadb_rag_helper_9034.log
?? services/chromadb_rest_bridge.py
?? services/chromadb_v2_to_gis_sync.py
?? services/chromadb_v2_to_gis_sync.py.pre_dynamic_discovery
?? services/chromadbrag1/
?? services/chunked_ingest_gbim_to_chroma.py
?? services/citieswithpopulation_2500_census_201111_gcs83_attrs.csv
?? services/citieswithpopulation_2500_census_201111_utm83_attrs.csv
?? services/citieswithpopulationover10k_census_201111_gcs83_attrs.csv
?? services/citieswithpopulationover10k_uscensus_1990_ll83_attrs.csv
?? services/citieswithpopulationover10k_uscensus_1990_utm83_attrs.csv
?? services/citieswithpopulationover2500_uscensus_1990_ll83_attrs.csv
?? services/citieswithpopulationsover10k_census_2020_utm83_attrs.csv
?? services/citieswithpopulationsover10k_census_2020_wma84_attrs.csv
?? services/citieswithpopulationsover2500_census_2020_utm83_attrs.csv
?? services/citieswithpopulationsover2500_census_2020_wma84_attrs.csv
?? services/citieswithpopulatoinover2500_uscensus_1990_utm83_attrs.csv
?? services/clean_and_dedupe_services.sh
?? services/clean_compose.py
?? services/clean_integration.py
?? services/clean_integration.py.pre_dynamic_discovery
?? services/clean_service_candidates.txt
?? services/cleanup_manifest.txt
?? services/cloudflare_auth_helper.sh
?? services/cloudflare_domain_integration.py
?? services/cloudflared-linux-amd64.deb
?? services/coals2_ll83_attrs.csv
?? services/coals2_utm27_attrs.csv
?? services/coals2_utm83_attrs.csv
?? services/commandorchestrator.log
?? services/commons_gamification.py
?? services/community_stake_registry.py
?? services/communityboundary_min_att_20250121_utm83_attrs.csv
?? services/communityboundary_min_att_20250121_wma84_attrs.csv
?? services/communityhealthproviders_wvhealthcareauthority_200802_utm83_attrs.csv
?? services/complete_fix.py
?? services/complete_memory_fix.py
?? services/complete_port_scan_20251011_181138.log
?? services/complete_system_audit.py
?? services/complete_system_audit_with_swagger.py
?? services/complete_system_audit_with_swagger.py.pre_dynamic_discovery
?? services/comprehensive_gisgeodb_audit.py
?? services/comprehensive_gisgeodb_audit_FIXED.log
?? services/comprehensive_gisgeodb_audit_FIXED.py
?? services/comprehensive_port_audit.sh
?? services/comprehensive_storage_fix.py
?? services/comprehensive_storage_fix_9979.log
?? services/comprehensive_url_fix.py
?? services/comprehensive_url_fix.py.PORT8000_BACKUP
?? services/comprehensive_url_fix.py.pre_dynamic_discovery
?? services/config_spiritual.py
?? services/configure_facebook_webhook.py
?? services/configure_facebook_webhook.py.backup_vocabulary_cleanup
?? services/connect_full_brain.sh
?? services/connect_holy_spirit_to_existing_email.sh
?? services/connection_pooling.py
?? services/consciousness_bridge_enhanced.log
?? services/consciousness_bridge_judges.log
?? services/consciousness_coordinator.log
?? services/consciousness_coordinator.psychology_patched.py
?? services/consciousness_coordinator.psychology_patched.py.pre_dynamic_discovery
?? services/consciousness_coordinator.py
?? services/consciousness_coordinator.py.BACKUP
?? services/consciousness_coordinator.py.backup_20251031
?? services/consciousness_coordinator.py.pre_dynamic_discovery
?? services/consciousness_feed_integration.psychology_patched.py
?? services/consciousness_feed_integration.py
?? services/consciousness_feed_integration.py.backup_20251031
?? services/consciousness_gateway.py
?? services/consciousness_poster.log
?? services/consciousness_poster_output.log
?? services/consciousness_with_egeria_voice.py
?? services/consciousness_with_egeria_voice.py.backup_vocabulary_cleanup
?? services/consciousness_working.py
?? services/consciousnessbridge.log
?? services/consensus.log
?? services/consensus_service.log
?? services/consolidate_to_chroma_db.py
?? services/constitutional_api.PROD_BACKUP.py
?? services/constitutional_api.py
?? services/constitutional_api.py.backup
?? services/constitutional_api.py.pre_usc
?? services/constitutional_api.py.pre_versions
?? services/constitutional_api_fixed.py
?? services/constitutional_guardian.PROD_BACKUP.py
?? services/constitutional_guardian.py
?? services/constitutional_principles.json
?? services/constitutional_principles.json.mcp_backup
?? services/context_manager.py
?? services/contract_generator.py
?? services/contractbuilder.log
?? services/contractbuilderv2.log
?? services/conversation_memory_endpoints.py
?? services/conversation_memory_endpoints.py.backup_before_portmanager
?? services/copy_all_missing_services.sh
?? services/copy_architecture_docs.sh
?? services/copy_complete_brain_structure.sh
?? services/correctionalinstitutions_hsip_20091230_utm83_attrs.csv
?? services/correctionalinstitutions_hsip_20091230_wgs84_attrs.csv
?? services/count_collections.py
?? services/count_collections_local.py
?? services/countycityparkboundaries_20201104_utm83_attrs.csv
?? services/countyseats_usgs_ll83_attrs.csv
?? services/countyseats_usgs_utm83_attrs.csv
?? services/courthousescounty_manysources_200203_ll83_attrs.csv
?? services/courthousescounty_manysources_200203_utm83_attrs.csv
?? services/courthousesfederal_manysources_200203_ll83_attrs.csv
?? services/courthousesfederal_manysources_200203_utm_attrs.csv
?? services/cpu_optimization.py
?? services/create_adapter_wrappers.sh
?? services/create_autonomous_learner_tables.py
?? services/create_consciousness_data_integration.psychology_patched.py
?? services/create_consciousness_data_integration.py
?? services/create_consciousness_data_integration.py.backup_20251031
?? services/create_dual_consciousness_i_containers.psychology_patched.py
?? services/create_dual_consciousness_i_containers.py
?? services/create_dual_consciousness_i_containers.py.backup_20251031
?? services/create_geodb_nodes.py
?? services/create_i_statement_feedback_loop.py
?? services/create_immutable_security_layer.py
?? services/create_mamma_kidd_auth.sh
?? services/create_perpetual_storage_layer.py
?? services/create_perpetual_storage_layer_9837.log
?? services/create_sanctuary_monitor.sh
?? services/create_tile_index.py
?? services/create_ueid_identity_layer.py
?? services/cron_health_check.sh
?? services/cvfault_ll83_attrs.csv
?? services/cvfault_utm27_attrs.csv
?? services/cvfault_utm83_attrs.csv
?? services/cvpoly_ll83_attrs.csv
?? services/cvpoly_utm27_attrs.csv
?? services/cvpoly_utm83_attrs.csv
?? services/dams_usarmycorpsofengineers_200010_utm83_attrs.csv
?? services/dams_usarmycropsofengineers_200010_ll83_attrs.csv
?? services/damsnoncoal_usgs_2002_ll27_attrs.csv
?? services/damsnoncoal_usgs_2002_utm83_attrs.csv
?? services/dao_governance.py
?? services/data_inventory_endpoint.py
?? services/dedup_compose.sh
?? services/dedupe_compose.py
?? services/deep_dive_modules.sh
?? services/deep_excavation.sh
?? services/deep_module_search.sh
?? services/deploy_to_mountainshares.sh
?? services/deploy_warm_persona_final.sh
?? services/designed_ports.txt
?? services/dgm_bridge.log
?? services/dgm_bridge.py
?? services/dgm_connector_registry.py
?? services/dgm_connectors_resolved.json
?? services/dgm_orchestrator_fake.py
?? services/dgm_services_state.json
?? services/dgm_supervisor.log
?? services/dgm_supervisor_4012.log
?? services/dgm_supervisor_woah.log
?? services/dgm_supervisor_woah.psychology_patched.py
?? services/dgm_supervisor_woah.psychology_patched_9617.log
?? services/dgm_supervisor_woah.py
?? services/dgm_supervisor_woah.py.backup_20251031
?? services/dgm_supervisor_woah_4012.log
?? services/dgm_supervisor_woah_9074.log
?? services/dgm_supervisor_woah_fixed.py
?? services/dgm_supervisor_woah_fixed_4012.log
?? services/dgm_supervisor_woah_fixed_9222.log
?? services/dgm_supervisor_woah_psychology_patched_4012.log
?? services/dgm_supervisor_woah_simple.py
?? services/dgm_supervisor_woah_simple.py.backup_vocabulary_cleanup
?? services/dgm_supervisor_woah_simple_4012.log
?? services/dgm_supervisor_woah_simple_9105.log
?? services/dgm_woah_simple.log
?? services/dgm_worker.py
?? services/dgmsupervisorwoah_4012.log
?? services/diagnostic_ms_jarvis.sh
?? services/dir_endpoints.txt
?? services/disable_aggressive_cleaning.py
?? services/docker-compose.bak
?? services/docker-compose.deduped.yml
?? services/docker-compose.yml.backup-1763229864
?? services/docker-compose.yml.backup-corrupted-1763229905
?? services/docker-compose.yml.backup.with_local
?? services/docker_cleanup_and_optimize.sh
?? services/domain_service_router.py
?? services/download_everything_appalachian.sh
?? services/download_nltk_data.py
?? services/download_priority_counties.sh
?? services/dpkg-list.txt
?? services/dump.rdb
?? services/dynamic_app.py
?? services/dynamic_port_scheduler.py
?? services/dynamic_port_scheduler.py.BROKEN_REDIS
?? services/dynamic_port_scheduler.py.backup
?? services/dynamic_port_scheduler.py.backup_1762960055
?? services/dynamic_port_scheduler.py.backup_20251111_092913
?? services/dynamic_port_scheduler.py.backup_20251113_135008
?? services/dynamic_port_service.log
?? services/dynamic_port_service.py
?? services/dynamic_port_service.py.backup
?? services/dynamic_port_service.py.bak
?? services/dynamic_port_service_enhanced.py
?? services/egeria_active_heartbeat.log
?? services/egeria_active_heartbeat.py
?? services/egeria_api_proxy.py
?? services/egeria_autonomous_inquiry.log
?? services/egeria_autonomous_inquiry.py
?? services/egeria_autonomous_inquiry_active.py
?? services/egeria_code_execution_engine.py
?? services/egeria_core_identity.txt
?? services/egeria_facebook_perpetual_scheduler.py
?? services/egeria_facebook_perpetual_scheduler.py.backup
?? services/egeria_facebook_perpetual_scheduler.py.backup.1762961759
?? services/egeria_facebook_perpetual_scheduler.py.before_memory_20251108
?? services/egeria_facebook_perpetual_scheduler.py.pre_dynamic_discovery
?? services/egeria_multi_mode_system.py
?? services/egeria_persona_config.json
?? services/egeria_safe_self_correction.py
?? services/egeria_status_poller.log
?? services/egeria_status_poller.py
?? services/egeria_system_prompt.txt
?? services/egeria_true_identity.txt
?? services/egeria_web_ui.py
?? services/egeria_web_ui.py.old
?? services/egeria_web_ui.py.old-timeout-version
?? services/egeria_web_ui_FIXED.log
?? services/egeria_web_ui_FIXED.py
?? services/egeria_web_ui_dynamic.py
?? services/egeria_web_ui_final_biological.py
?? services/egeria_web_ui_fixed_simple.py
?? services/egeria_web_ui_fixed_simple.py.pre_dynamic_discovery
?? services/egeria_web_ui_plain_authentic.py
?? services/egeria_web_ui_plain_authentic.py.pre_dynamic_discovery
?? services/egeria_web_ui_v3_consciousness.py
?? services/egeria_web_ui_with_execution.py
?? services/egeria_web_ui_with_execution.py.pre_dynamic_discovery
?? services/egeria_web_ui_working.py
?? services/egeria_web_ui_working.py.pre_dynamic_discovery
?? services/egeriaknowledgebase/
?? services/email_auto_checker.py
?? services/email_gis_geolocation_extractor.py
?? services/email_rag_integration.py
?? services/email_rag_integration_9163.log
?? services/email_service.env
?? services/email_strategy.txt
?? services/embed_and_add.py
?? services/embed_and_add.py.pre_dynamic_discovery
?? services/embed_and_query.py
?? services/embed_and_query.py.pre_dynamic_discovery
?? services/embed_gbim.py
?? services/embed_geodb.py
?? services/emergency_memory_cleanup.sh
?? services/empowermentzonesandenterprisecommunities_uscensus_2002_utm83_attrs.csv
?? services/empowermentzonesandenterprisecommunitiesbytract_uscens_30c72907_attrs.csv
?? services/enable_22llm_routing.py
?? services/enable_auto_web_search.sh
?? services/enable_harmony4hope_website_access_CORRECTED.sh
?? services/enable_holy_spirit_file_writing.sh
?? services/enable_website_building_capabilities.sh
?? services/enhance_agent_prompts.py
?? services/enhance_cleaner.py
?? services/enhance_pituitary_warmth.py
?? services/enhance_rag_first.py
?? services/enhance_rag_first_9987.log
?? services/enhance_rag_knowledge.py
?? services/enhance_rag_knowledge_9846.log
?? services/enhanced_learner_concept.py
?? services/enrich_geodb_collections.py
?? services/enrich_geodb_layers.py
?? services/eternal_watchdog.log
?? services/eternal_watchdog.sh.disabled
?? services/eternalwatchdog.log
?? services/etl_from_csv_template.py
?? services/etl_from_manifest.py
?? services/etl_template_layer.py
?? services/examine_ai_server_complete.sh
?? services/examine_app_brain_backendlib.sh
?? services/examine_existing_code.sh
?? services/examine_extracted_services.sh
?? services/examine_geospatial_agents.sh
?? services/excursionpassengertrains_wvdof_200102_ll83_attrs.csv
?? services/excursionpassengertrains_wvdof_200102_utm83_attrs.csv
?? services/explore_16mb_directory.sh
?? services/explore_both_systems.sh
?? services/export_attributes_to_gis.py
?? services/export_chroma_manifest.py
?? services/export_docs_for_notebook.sh
?? services/export_geodb_attrs.py
?? services/export_metadata_csv.py
?? services/extract_all_archives_deep_dive.sh
?? services/extract_all_big_archives.sh
?? services/extract_all_chromadb_to_gis.py
?? services/extract_all_chromadbs_to_gis.py
?? services/extract_all_gis_comprehensive.sh
?? services/extract_all_remaining_services.sh
?? services/extract_and_search_archives.sh
?? services/extract_binder4_text.py
?? services/extract_chroma_sqlite_to_gis.py
?? services/extract_complete_real.sh
?? services/extract_real_knowledge_to_gis.py
?? services/extract_service_tarballs.sh
?? services/extract_shapefile_features_to_csv.py
?? services/extract_user_jarvis_files.sh
?? services/extracted_gis/
?? services/extraction.log
?? services/extraction_output.log
?? services/facebook_4021.log
?? services/facebook_chat_unified.py
?? services/facebook_chat_unified.py.pre_dynamic_discovery
?? services/facebook_consciousness_daemon.py
?? services/facebook_consciousness_daemon.py.backup_vocabulary_cleanup
?? services/facebook_daemon_polling.py
?? services/facebook_daemon_polling.py.pre_dynamic_discovery
?? services/facebook_messenger_integration.py
?? services/facebook_post.sh
?? services/facebook_poster.log
?? services/facebook_poster.py
?? services/facebook_poster_autonomous.py
?? services/facebook_poster_fast.py
?? services/facebook_poster_working.py
?? services/facebook_token.env
?? services/facebook_voice_orchestrator_egeria.py
?? services/facilities_epa_200203_ll83_attrs.csv
?? services/facilities_epa_200203_utm83_attrs.csv
?? services/failed_services.csv
?? services/fault_reg_ll83_attrs.csv
?? services/faultgl_reg_ll83_attrs.csv
?? services/feature_geometries_full_attributes.csv
?? services/features_attrs.csv
?? services/fifth_dgm.log
?? services/fifth_dgm.py
?? services/fifth_dgm_9949.log
?? services/fifth_dgm_integration.py
?? services/fifth_dgm_integration_9912.log
?? services/fifth_dgm_main.py
?? services/fifth_dgm_main_9344.log
?? services/file_metadata_matching_algorithm.py
?? services/fill_null_coordinates_mount_hope.py
?? services/final_cleanup_integration.sh
?? services/final_model_optimization.py
?? services/final_synthesis_fix.sh
?? services/final_test.log
?? services/final_validation_test.sh
?? services/finalize_integration.sh
?? services/find_actual_service_implementations.sh
?? services/find_advanced_modules.sh
?? services/find_complete_brain_structure.sh
?? services/find_custom_services.sh
?? services/find_dgm_service.sh
?? services/find_web_and_deeper_python.sh
?? services/fire_departments_attrs.csv
?? services/fire_dept_wvdem_092017_utm83_attrs.csv
?? services/fix_404_endpoints.sh
?? services/fix_agent_prompts.py
?? services/fix_all_consciousness_services.py
?? services/fix_and_restart_msjarvis.sh
?? services/fix_autonomous.py
?? services/fix_autonomous.py.backup_vocabulary_cleanup
?? services/fix_autonomous_learner_endpoint.py
?? services/fix_autonomous_learner_endpoint.py.pre_dynamic_discovery
?? services/fix_autonomous_learner_indent.py
?? services/fix_autonomous_research.sh
?? services/fix_background_storage.py
?? services/fix_background_storage_9713.log
?? services/fix_both_issues_final.sh
?? services/fix_chat_api.sh
?? services/fix_chat_server.py
?? services/fix_chat_server.py.backup_vocabulary_cleanup
?? services/fix_chroma_url.py
?? services/fix_chroma_url.py.PORT8000_BACKUP
?? services/fix_chroma_url.py.pre_dynamic_discovery
?? services/fix_consciousness_endpoints.py
?? services/fix_context_flow.py
?? services/fix_creator_recognition.py
?? services/fix_egeria_final.sh
?? services/fix_egeria_persona.sh
?? services/fix_egeria_pronouns.sh
?? services/fix_egeria_warm_response.patch
?? services/fix_email_service_env_loading.sh
?? services/fix_fastapi_lifespan.py
?? services/fix_gpu_and_retry.py
?? services/fix_gpu_and_retry_4016.log
?? services/fix_import.py
?? services/fix_indentation.py
?? services/fix_judge_and_memory.py
?? services/fix_judge_authentic.py
?? services/fix_judge_authentic.py.backup_vocabulary_cleanup
?? services/fix_judge_response.py
?? services/fix_judge_synthesis.py
?? services/fix_llm_bridges.sh
?? services/fix_main_brain_endpoints.py
?? services/fix_model_names.py
?? services/fix_model_unloading.py
?? services/fix_model_unloading.py.backup_vocabulary_cleanup
?? services/fix_mother_carrie_principles.sh
?? services/fix_multi_rag_chromadb.py
?? services/fix_multi_rag_chromadb.py.backup_vocabulary_cleanup
?? services/fix_multi_rag_chromadb_9340.log
?? services/fix_new_service_endpoints.py
?? services/fix_ollama_connection.sh
?? services/fix_orchestrator_init.py
?? services/fix_orchestrator_scope.py
?? services/fix_persona.py
?? services/fix_persona.sh
?? services/fix_persona_hang.py
?? services/fix_persona_naming.sh
?? services/fix_port_8001_clean.py
?? services/fix_port_8051_handler.py
?? services/fix_proactive_cleanup_correctly.sh
?? services/fix_prompt_leak.py
?? services/fix_query_service_endpoints.py
?? services/fix_rag_store.py
?? services/fix_rag_store.py.backup_vocabulary_cleanup
?? services/fix_rag_store_9161.log
?? services/fix_redis_and_continue.sh
?? services/fix_response_parsing.py
?? services/fix_semaphore.py
?? services/fix_storage.py
?? services/fix_storage_9169.log
?? services/fix_swagger.py
?? services/fix_timeouts_add_22llm.py
?? services/fix_web_persona.sh
?? services/fix_web_research.py
?? services/fix_woah_discovery.py
?? services/fix_woah_discovery.py.pre_dynamic_discovery
?? services/floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83_attrs.csv
?? services/fractal_adapter.py
?? services/fraud_detection_ai.py
?? services/full_brain_architecture.md
?? services/full_consciousness.log
?? services/full_rebuild.sh
?? services/full_system_audit.sh
?? services/full_system_health_check.sh
?? services/gateway.log
?? services/gateway8050_simple.py
?? services/gateway_300s.log
?? services/gateway_4_layers.log
?? services/gateway_9000.log
?? services/gateway_complete.log
?? services/gateway_complete_kb.log
?? services/gateway_corrected_ports.log
?? services/gateway_embeddings.log
?? services/gateway_ensemble_fast.log
?? services/gateway_final.log
?? services/gateway_fixed_ports.log
?? services/gateway_fresh.log
?? services/gateway_judge_integrated.log
?? services/gateway_live.log
?? services/gateway_mesh_context.sh
?? services/gateway_messenger_integration.py
?? services/gateway_rag_fixed.log
?? services/gateway_rebuild_venv.log
?? services/gateway_restart.log
?? services/gateway_restored.log
?? services/gateway_stable.log
?? services/gateway_v2.log
?? services/gateway_verify_fixed.py
?? services/gateway_wv_entanglement.py
?? services/gbim_api.py
?? services/gbim_benefit_indexer.py
?? services/gbim_chroma.py
?? services/gbim_chroma_fixed.py
?? services/gbim_core.py
?? services/gbim_core.py.bak.1768220758
?? services/gbim_dashboard.py
?? services/gbim_entangled_summary.py
?? services/gbim_entanglement.py
?? services/gbim_explain.py
?? services/gbim_gis_bridge.py
?? services/gbim_ingest.log
?? services/gbim_ingest_safe.log
?? services/gbim_metadata_loader.py
?? services/gbim_msjarvis.py
?? services/gbim_query_router.py
?? services/gbim_query_router.py.backup_health_integration
?? services/gbim_query_router.py.bak.20260716-185601
?? services/gbim_query_router.py.bak.20260716-201230
?? services/gbim_query_router.py.bak.20260718_165258
?? services/gbim_query_router.py.bak_47_legal_required
?? services/gbim_query_router.py.bak_port7215_test
?? services/gbim_query_router.py.bak_port7225_test
?? services/gbim_reingest_placeholder.py
?? services/gbim_semantic_indexer.py
?? services/gbim_spatial_indexer.py
?? services/gbim_temporal_indexer.py
?? services/gbim_v0_retrieval.py
?? services/gdb_integration.log
?? services/gdb_integration_service.py
?? services/generate_services.py
?? services/geo/
?? services/geo_rag_debug.py
?? services/geo_rag_debug_app.py
?? services/geobim_health_shim_8051.py
?? services/geobim_integrated.py
?? services/geobim_integrated.py.running_backup
?? services/geobim_mysql.py
?? services/geobim_mysql_v2.py
?? services/geodb_adapter.py
?? services/geodb_core.py
?? services/geodb_export_plan.yaml
?? services/geodb_export_plan_all.yaml
?? services/geodb_geom_tables.tsv
?? services/geographicalnamesonusgstopomaps_usgs_200601_ll27_attrs.csv
?? services/geographicalnamesonusgstopomaps_usgs_200601_utm83_attrs.csv
?? services/geographicnamesonusgstopomaps_current_usgs_20110801_ll83_attrs.csv
?? services/geographicnamesonusgstopomaps_current_usgs_20110801_utm83_attrs.csv
?? services/geographicnamesonusgstopomaps_historical_usgs_20110801_ll83_attrs.csv
?? services/geographicnamesonusgstopomaps_historical_usgs_20110801_utm83_attrs.csv
?? services/geographicnamesonusgstopomaps_usgs_20110801_ll83_attrs.csv
?? services/geographicnamesonusgstopomaps_usgs_20110801_utm83_attrs.csv
?? services/geolgyl_reg_ll83_attrs.csv
?? services/geolgyp_reg_ll83_attrs.csv
?? services/geospatial_resolver.py
?? services/geotextl_reg_ll83_attrs.csv
?? services/get_cloudflare_zone_id.sh
?? services/gis_chat_integration.py
?? services/gis_command_module.py
?? services/gis_download_plan.json
?? services/gis_enhanced_chat.log
?? services/gis_query_service.log
?? services/gis_query_service_fixed.log
?? services/gis_rag_service.py
?? services/gis_rag_service.py.bak.1782446020
?? services/gis_rag_service.py.bak.20260718_170318
?? services/gisgeodb_access_20251103_221750.log
?? services/gisgeodb_fixed_20251103_221835.log
?? services/gisgeodb_learner_hook.py
?? services/gisgeodb_learner_hook.py.backup_vocabulary_cleanup
?? services/gisgeodb_storage.py
?? services/gisgeodb_storage_9215.log
?? services/gisgeodbdirectaccess.py
?? services/glacagl_reg_ll83_attrs.csv
?? services/glacal_reg_ll83_attrs.csv
?? services/gpu_accelerated_rag.py
?? services/gpu_accelerated_rag_4016.log
?? services/gpu_accelerated_rag_9090.log
?? services/gpu_accelerated_rag_fixed.py
?? services/gpu_accelerated_rag_fixed.py.backup_before_portmanager
?? services/gpu_accelerated_rag_fixed_4016.log
?? services/gpu_accelerated_rag_fixed_9873.log
?? services/gpu_jarvis_4001.log
?? services/gpu_rag_4016.log
?? services/gpuacceleratedragfixed_4016.log
?? services/guards.log
?? services/guards.py
?? services/guards_api_module.py
?? services/hardware_optimization_analyzer.py
?? services/harmony4hope_deployment_manager.py
?? services/hazardmitigationbuyout_20250929_polygons_utm83_attrs.csv
?? services/hazardmitigationbuyout_20250929_polygons_wma84_attrs.csv
?? services/health_access_api.py
?? services/health_access_gbim_bridge.py
?? services/health_access_query.py
?? services/health_check.sh
?? services/health_check_cache.py
?? services/healthruralfacilities_manysources_utm83_attrs.csv
?? services/hello.txt
?? services/hierarchical_coordinator_AUTONOMOUS.md
?? services/hierarchical_coordinator_autonomous.py
?? services/hierarchical_coordinator_autonomous.py.pre_dynamic_discovery
?? services/hierarchical_coordinator_deep_mode.py
?? services/hierarchical_coordinator_deep_mode.py.pre_dynamic_discovery
?? services/hierarchical_integration.py
?? services/hierarchical_integration.py.pre_dynamic_discovery
?? services/hierarchical_method.txt
?? services/highered_wvemd_072420_utm83_attrs.csv
?? services/highered_wvemd_072420_wgc84_attrs.csv
?? services/hilbert_5002_active.log
?? services/hilbert_5002_final.log
?? services/hilbert_5002_fixed.log
?? services/hilbert_5002_restart.log
?? services/hilbert_8235.log
?? services/hilbert_quantum.log
?? services/hilbert_restart.log
?? services/hilbert_spatial_chat.py
?? services/hilbert_spatial_chat.py.backup
?? services/hilbert_spatial_chat.py.backup_20251113_180915
?? services/hilbert_spatial_chat.py.backup_20251113_191119
?? services/hilbert_spatial_chat.py.backup_20251113_192420
?? services/hilbert_spatial_chat.py.bak_1782235047
?? services/hilbertspatialchat.log
?? services/hippocampus_service.py.bak.20260626235712
?? services/hippocampus_service.py.bak.20260627T032303Z
?? services/hippocampus_service.py.bak.hippocampus_schema_fix
?? services/historicalaerialphotographycountycoverage_wvgistc_utm83_attrs.csv
?? services/hospitals_attrs.csv
?? services/hospitals_wvdem_040519_gcs84_attrs.csv
?? services/hospitals_wvdem_040519_utm83_attrs.csv
?? services/hospitalswvdem040519utm83_attrs.csv
?? services/host_bulk_loader.py
?? services/i_container_interest_algorithm.py
?? services/i_container_interest_algorithm.py.before_diversity
?? services/icontainers_fastapi.py
?? services/icontainers_fastapi.py.bak
?? services/icontainers_fastapi.py.pre_adapter_1771176105
?? services/identify_unknown_services.sh
?? services/immutable_core_enforcement.py
?? services/impact_reg_ll83_attrs.csv
?? services/implement_conversation_fixes.sh
?? services/implement_enhancements.sh
?? services/implement_gpu_optimization.sh
?? services/implement_judge_pituitary_fixed.py
?? services/implement_judge_pituitary_fixed.py.backup_vocabulary_cleanup
?? services/implement_judge_pituitary_fixed.py.pre_dynamic_discovery
?? services/implement_safe_optimizations.py
?? services/implement_safe_optimizations.py.backup_vocabulary_cleanup
?? services/implement_storage_optimization.sh
?? services/import_gbim_assets.py
?? services/import_gis_geodata_to_gbim.py
?? services/import_gisgeodata_to_gbim.py
?? services/improve_jarvis.sh
?? services/index.html
?? services/index.js
?? services/index_all_extracted_gis.py
?? services/indexgrid15minutequads_wvgistc_ll83_attrs.csv
?? services/indexgrid15minutequads_wvgistc_utm83_attrs.csv
?? services/indexgrid15minutewithcounties_wvgistc_utm27_attrs.csv
?? services/indexgrid1minutequads_wvgistc_ll83_attrs.csv
?? services/industrialbuildings_wvdo_200807_utm83_attrs.csv
?? services/industrialparks_wvdo_200078_utm83_attrs.csv
?? services/industrialsites_wvdo_200807_utm83_attrs.csv
?? services/inedexgrid1minutequads_wvgistc_utm83_attrs.csv
?? services/infra_status.json
?? services/infrastructure_endpoints.py
?? services/ingest/
?? services/ingest_additional_kbs.py
?? services/ingest_benefit_programs.py
?? services/ingest_benefit_programs_to_chroma.py
?? services/ingest_compliance_tasks_to_chroma.py
?? services/ingest_csv_to_gisgeodb.py
?? services/ingest_documents_to_chromadb.py
?? services/ingest_full_attributed_docs.py
?? services/ingest_gbim_to_chroma.py
?? services/ingest_gbim_to_chroma_fast.py
?? services/ingest_gbim_to_chroma_resume.py
?? services/ingest_gbim_to_chroma_ultrafast.py
?? services/ingest_gis_features_to_chromadb.py
?? services/ingest_h4h_cultural_heritage.py
?? services/ingest_hospitals.py
?? services/ingest_imm_to_chroma.py
?? services/ingest_knowledge_simple.py
?? services/ingest_mrsid_imagery.py
?? services/ingest_utility_enrollments_to_chroma.py
?? services/ingest_watcher.py
?? services/ingestcsvtogisgeodb.py
?? services/inject_egeria_persona.py
?? services/inject_gisgeodb_into_learner.py
?? services/inject_gisgeodb_into_learner.py.backup_vocabulary_cleanup
?? services/inspect_geodb_collection.py
?? services/inspect_key_services.sh
?? services/install_research_layer.sh
?? services/intake_samples/
?? services/intake_service.py
?? services/integrate_advanced_modules.sh
?? services/integrate_all_services.py
?? services/integrate_all_services.py.pre_dynamic_discovery
?? services/integrate_brain_orchestrator.sh
?? services/integrate_complete_architecture.py
?? services/integrate_consciousness_into_swarm.py
?? services/integrate_discovered_services.sh
?? services/integrate_fifth_dgm_autonomous_learner.py
?? services/integrate_fifth_dgm_autonomous_learner_9681.log
?? services/integrate_full_brain.py
?? services/integrate_full_brain.py.pre_dynamic_discovery
?? services/integrate_full_neural_architecture.py
?? services/integrate_i_container_interests.py
?? services/integrate_i_container_to_schedulers.py
?? services/integrate_i_container_to_schedulers.py.backup_vocabulary_cleanup
?? services/integrate_mamma_kidd_protocol.sh
?? services/integrate_mother_protocol.sh
?? services/integrate_orchestrator_flow.py
?? services/integrate_phase1.sh
?? services/integrate_phase2.sh
?? services/integrate_phase3.sh
?? services/integrate_phase4_5.sh
?? services/integrate_rag.sh
?? services/integrate_spatial_temporal.py
?? services/integrate_spatial_temporal.py.backup_vocabulary_cleanup
?? services/integration_layer.backup.1768269372/
?? services/integration_layer.placeholder_1768012705/
?? services/integration_layer/
?? services/interaction_logger.py
?? services/intermodalterminalfacilities_usdot_1997_ll83_attrs.csv
?? services/intermodalterminalfacilities_usdot_1997_utm83_attrs.csv
?? services/internet_tunnel_service.py
?? services/introduce_self.sh
?? services/inventory_services.sh
?? services/investigate_coordination.sh
?? services/jarvis_authentic_persona.txt
?? services/jarvis_ensemble.log
?? services/jarvis_ensemble.py
?? services/jarvis_health.log
?? services/jarvis_hilbert_state.py
?? services/jarvis_hilbert_state.py.bak.1782491046
?? services/jarvis_hilbert_state.py.bak.1782491121
?? services/jarvis_hilbert_time.py
?? services/jarvis_llm1.log
?? services/jarvis_llm1.py
?? services/jarvis_steward.py
?? services/jarvis_steward/
?? services/jarvis_stewardship_scheduler.py
?? services/jarvis_synth_llm.py
?? services/jarvisarchiveapi.py
?? services/jarvisarchiveapi_9200.log
?? services/jarviscryptopolicy.py
?? services/joblib_1.5.2_pickle_py312_np23.pkl
?? services/judge_10070.py
?? services/judge_10071.py
?? services/judge_10072.py
?? services/judge_10073.py
?? services/judge_10074.py
?? services/judge_10075.py
?? services/judge_10076.py
?? services/judge_10077.py
?? services/judge_10078.py
?? services/judge_10079.py
?? services/judge_10080.py
?? services/judge_10081.py
?? services/judge_10082.py
?? services/judge_10083.py
?? services/judge_10084.py
?? services/judge_10085.py
?? services/judge_10086.py
?? services/judge_10087.py
?? services/judge_10088.py
?? services/judge_10089.py
?? services/judge_10090.py
?? services/judge_10091.py
?? services/judge_10092.py
?? services/judge_10093.py
?? services/judge_10094.py
?? services/judge_10095.py
?? services/judge_10096.py
?? services/judge_10097.py
?? services/judge_10098.py
?? services/judge_10099.py
?? services/judge_10100.py
?? services/judge_10101.py
?? services/judge_10102.py
?? services/judge_10103.py
?? services/judge_10104.py
?? services/judge_10105.py
?? services/judge_10106.py
?? services/judge_10107.py
?? services/judge_10108.py
?? services/judge_10109.py
?? services/judge_10110.py
?? services/judge_10111.py
?? services/judge_10112.py
?? services/judge_10113.py
?? services/judge_10114.py
?? services/judge_10115.py
?? services/judge_10116.py
?? services/judge_10117.py
?? services/judge_10118.py
?? services/judge_10119.py
?? services/judge_10120.py
?? services/judge_10121.py
?? services/judge_10122.py
?? services/judge_10123.py
?? services/judge_10124.py
?? services/judge_10125.py
?? services/judge_10126.py
?? services/judge_10127.py
?? services/judge_10128.py
?? services/judge_10129.py
?? services/judge_10130.py
?? services/judge_10131.py
?? services/judge_10132.py
?? services/judge_10133.py
?? services/judge_10134.py
?? services/judge_10135.py
?? services/judge_alignment_filter.py
?? services/judge_consistency_engine.py
?? services/judge_ethics_filter.py
?? services/judge_pipeline.py
?? services/judge_to_pituitary_bridge.py
?? services/judge_truth_filter.py
?? services/knowledge_docs_attributes.csv
?? services/knowledge_docs_attributes.geojson
?? services/knowledge_docs_metadata.csv
?? services/knowledge_growth_endpoint.txt
?? services/launch_advanced.sh
?? services/launch_all_bridges.sh
?? services/launch_dashboard_background.sh
?? services/launch_service.sh
?? services/launch_web_services.sh
?? services/layer2_port9000_bridge.py
?? services/leak_test.sh
?? services/learner.log
?? services/libraries_manysources_2001_ll27_attrs.csv
?? services/libraries_manysources_2001_utm83_attrs.csv
?? services/link_gisgeodb_to_files.py
?? services/list_geodb_collections.py
?? services/live_ports.txt
?? services/llama_test.log
?? services/llm10_health_proxy.py
?? services/llm11_health_proxy.py
?? services/llm12_health_proxy.py
?? services/llm13_health_proxy.py
?? services/llm14_health_proxy.py
?? services/llm15_health_proxy.py
?? services/llm16_health_proxy.py
?? services/llm17_health_proxy.py
?? services/llm18_health_proxy.py
?? services/llm19_health_proxy.py
?? services/llm1_health_proxy.py
?? services/llm20.current.log
?? services/llm20_health_proxy.py
?? services/llm21_health_proxy.py
?? services/llm22_health_proxy.py
?? services/llm2_health_proxy.py
?? services/llm3_health_proxy.py
?? services/llm4_health_proxy.py
?? services/llm5_health_proxy.py
?? services/llm6_health_proxy.py
?? services/llm7_health_proxy.py
?? services/llm8_health_proxy.py
?? services/llm9_health_proxy.py
?? services/llm_belief_utils.py
?? services/llm_bridge_main.py
?? services/llm_conscious_OPTIMIZED.py
?? services/llm_consensus_19_PRODUCTION.log
?? services/llm_consensus_19_PRODUCTION.py
?? services/llm_consensus_20_FINAL.log
?? services/llm_consensus_20_FINAL.py
?? services/llm_consensus_20_FINAL.py.backup_vocabulary_cleanup
?? services/llm_consensus_22.py
?? services/llm_consensus_22_OPTIMIZED_ORDER.py
?? services/llm_consensus_22_SMALL_TO_LARGE.py
?? services/llm_ensemble_router.py
?? services/llm_ensemble_router.py.pre_dynamic_discovery
?? services/lm_synthesizer.py
?? services/lm_synthesizer.py.bak-ollama-20260627-222423
?? services/load_backbone_places_from_geodb.py
?? services/load_complete_knowledge_base.py
?? services/load_feature_geometries_to_chromadb.py
?? services/load_geodb_health_providers_to_neo4j.py
?? services/load_geodb_hospitals_to_neo4j.py
?? services/load_geodb_layer_to_neo4j.py
?? services/load_gis_to_chroma.py
?? services/load_knowledge.sh
?? services/load_pdfs_spiritual.py
?? services/load_rag_data.py
?? services/load_rag_data_9879.log
?? services/load_rag_knowledge.py
?? services/load_rag_knowledge.py.backup_vocabulary_cleanup
?? services/load_rag_knowledge_9381.log
?? services/load_shapefile_features_to_chromadb.py
?? services/load_spiritual_library.py
?? services/local_resources_resolver.py
?? services/location.log
?? services/logging_conf.py
?? services/main.py
?? services/main.py.BACKUP
?? services/main.py.FINALHEALTH.bak
?? services/main.py.backup
?? services/main.py.backup.before_auto_storage
?? services/main.py.backup.broken
?? services/main.py.bak.before_consciousness_fix
?? services/main.py.bak_before_bridge_20251212_232206
?? services/main.py.bak_before_bridge_20251212_232349
?? services/main.py.bak_enable_llmbridge_20251212_233118
?? services/main.py.bak_enable_llmbridge_20251212_233317
?? services/main.py.current.safebak
?? services/main.py.from_container
?? services/main.py.fromcontainer.llmbridge
?? services/main.py.pre_enhancement.bak
?? services/main.py.working_backup_20251020_110429
?? services/main_brain.log
?? services/main_brain.py
?? services/main_brain.py.backup
?? services/main_brain.py.backup_1771192185
?? services/main_brain.py.backup_1771192386
?? services/main_brain.py.backup_nbb_fixed
?? services/main_brain.py.bak
?? services/main_brain.py.bak-synth-20260627-221708
?? services/main_brain.py.bak.1771185442
?? services/main_brain.py.bak.20260626_205453
?? services/main_brain.py.bak.llm20_context.20260626_210155
?? services/main_brain.py.bak.prompt_tighten.20260626_210720
?? services/main_brain.py.bak.prompt_tighten_exact.20260626_210836
?? services/main_brain.py.bak.wv_context_append.20260626_211940
?? services/main_brain.py.bak.wv_normalize_20260626_215539
?? services/main_brain.py.bak.wv_normalize_exact_20260626_215648
?? services/main_brain.py.bak_1770565703
?? services/main_brain.py.bak_1770565749
?? services/main_brain.py.bak_1770565868
?? services/main_brain.py.bak_1771728143
?? services/main_brain.py.bak_legacy_chatlight
?? services/main_brain.py.bak_localnet
?? services/main_brain.py.bak_localnet_fixed
?? services/main_brain.py.bak_localnet_fixed2
?? services/main_brain.py.bak_sedpatch
?? services/main_brain.py.bak_ultimate_1770573774
?? services/main_brain.py.bak_ultimate_1770575025
?? services/main_brain.py.before_direct_fix
?? services/main_brain.py.before_final_fix
?? services/main_brain.py.before_mother_carrie
?? services/main_brain.py.before_mother_carrie_v2
?? services/main_brain.py.before_spiritual_integration
?? services/main_brain.py.before_spiritual_rag
?? services/main_brain.py.pre_judges
?? services/main_brain_attrs_patch.sh
?? services/main_brain_legacy_backup.py
?? services/main_brain_psychology_patch.py
?? services/main_brain_restart.log
?? services/main_brian.py
?? services/main_qualia.py
?? services/main_restored.log
?? services/main_with_rag.py
?? services/main_with_rag_9429.log
?? services/majorriversandlakesline_nhd_2002_ll83_attrs.csv
?? services/majorriversandlakesline_nhd_2002_utm83_attrs.csv
?? services/majorriversandlakespolygon_nhd_2002_poly_ll83_attrs.csv
?? services/majorriversandlakespolygon_nhd_2002_utm83_attrs.csv
?? services/make_holy_spirit_connection_tools_available.sh
?? services/make_persistent.sh
?? services/mamma_kidd.log
?? services/mamma_kidd_auth.py
?? services/mamma_kidd_auth.py.backup_20251013_201428
?? services/mamma_kidd_final.log
?? services/mamma_kidd_location.log
?? services/manage_msjarvis.sh
?? services/manifest_endpoints.py
?? services/manifest_endpoints.py.pre_dynamic_discovery
?? services/manual_storage_patch.py
?? services/manual_storage_patch_9323.log
?? services/manufacturingandbusiness_wvdo_200803_utm83_attrs.csv
?? services/master_chat_orchestrator.py
?? services/master_chat_orchestrator.py.pre_dynamic_discovery
?? services/master_chat_orchestrator_dynamic.py
?? services/master_chat_orchestrator_v5_consciousness.py
?? services/master_chat_orchestrator_v5_consciousness.py.pre_dynamic_discovery
?? services/master_chat_orchestrator_v6_biologics.py
?? services/master_chat_orchestrator_v6_biologics.py.pre_dynamic_discovery
?? services/master_chat_orchestrator_v7_complete.py
?? services/master_chat_orchestrator_v7_complete.py.backup_vocabulary_cleanup
?? services/master_chat_orchestrator_v7_complete.py.pre_dynamic_discovery
?? services/master_chat_orchestrator_v7_dynamic.py
?? services/master_chat_orchestrator_v8_spiritual_complete.py
?? services/master_chat_orchestrator_v8_spiritual_complete.py.pre_dynamic_discovery
?? services/master_chat_orchestrator_v8_spiritual_complete_4009.log
?? services/master_chat_orchestrator_v9_dgm_complete.log
?? services/master_chat_orchestrator_v9_dgm_complete.py
?? services/master_chat_orchestrator_v9_dgm_complete.py.backup_vocabulary_cleanup
?? services/master_chat_orchestrator_v9_dgm_complete.py.pre_dynamic_discovery
?? services/master_chat_orchestrator_v9_dgm_complete_9510.log
?? services/master_chat_orchestrator_v9_gpu_optimized.py
?? services/master_chat_orchestrator_v9_gpu_optimized.py.backup_1760564898
?? services/master_chat_orchestrator_v9_gpu_optimized.py.pre_dynamic_discovery
?? services/master_chat_orchestrator_v9_optimized.py
?? services/master_chat_orchestrator_v9_optimized.py.pre_dynamic_discovery
?? services/master_orchestrator_v9.log
?? services/master_system_audit.sh
?? services/master_unified_consciousness_scheduler.py
?? services/master_unified_consciousness_scheduler.py.backup_pre_enrichment_20251107_111721
?? services/master_unified_consciousness_scheduler_ENRICHED.py
?? services/mega_deep_archive_search.sh
?? services/memory_dgm_engine.log
?? services/memory_dgm_engine.py
?? services/memory_dgm_engine.py.backup_vocabulary_cleanup
?? services/memory_dgm_engine_9919.log
?? services/memory_dgm_gateway.py
?? services/memory_engine.log
?? services/memory_manager.py
?? services/memory_probe.sh
?? services/mesh_agent_batch.sh
?? services/mesh_broadcast_event.sh
?? services/mesh_cohort_selfsum.sh
?? services/mesh_context_probe.sh
?? services/mesh_coordinator_interface.py
?? services/mesh_crossagent_memory_search.sh
?? services/mesh_dream_summary.sh
?? services/mesh_emotion_map.json
?? services/mesh_emotion_map.sh
?? services/mesh_explore_chain.sh
?? services/mesh_feed_back_insight.sh
?? services/mesh_interest_timeline.csv
?? services/mesh_interest_timeline.sh
?? services/mesh_memory_dashboard.sh
?? services/mesh_memory_probe.sh
?? services/mesh_probe.sh
?? services/mesh_scenario_drill.sh
?? services/mesh_social_graph.sh
?? services/mesh_tag_topk.sh
?? services/mesh_topn_context.sh
?? services/mesh_trend_detection.sh
?? services/messenger_service_fixed.py
?? services/metfacp_reg_ll83_attrs.csv
?? services/method_tracker_decorator.py
?? services/method_tracking_helper.py
?? services/method_tracking_service.py
?? services/metrics_service.py
?? services/metropolitanandmicropolitanstatisticalareas_census_201111_gcs83_attrs.csv
?? services/metropolitanandmicropolitanstatisticalareas_census_201111_utm83_attrs.csv
?? services/metropolitanandmicropolitanstatisticalareas_census_2020_utm83_attrs.csv
?? services/metropolitanandmicropolitanstatisticalareas_census_2020_wma84_attrs.csv
?? services/metropolitanstatisticalareas_uscensus_199901_ll83_attrs.csv
?? services/metropolitanstatisticalareas_uscensus_199901_utm83_attrs.csv
?? services/migrate_blood_brain_barrier.py
?? services/migrate_chromadb_collections.py
?? services/migrate_gis2chroma.py
?? services/migrate_neurobiological_master.py
?? services/mineraloperations_usgs_200204_ll83_attrs.csv
?? services/mineraloperations_usgs_200204_utm83_attrs.csv
?? services/minesabandonedlandsline_wvdep_1996_noprojectoin_attrs.csv
?? services/minesabandonedlandspoint_wvdep_1996_noprojection_attrs.csv
?? services/minesabandonedlandspolygon_wvdep_1996_noprojection_attrs.csv
?? services/mistral_test.log
?? services/modify_autonomous_learning_cycle.py
?? services/monitor.log
?? services/monitor_ms_jarvis_memory.sh
?? services/monitor_orchestrator.sh
?? services/mother_carrie.log
?? services/mother_carrie_logging.py
?? services/mother_protocols.py
?? services/mountainshares_chain_monitor.py
?? services/mountainshares_gbim_suggester.py
?? services/mountainshares_ingest.py
?? services/mountainshares_integration.log
?? services/mountainshares_quest_api.py
?? services/mountainshares_registry.log
?? services/mountainshares_registry.py
?? services/move_huggingface_to_cpu.py
?? services/ms_egeria_facebook_autopost.py
?? services/ms_jarvis_FINAL.log
?? services/ms_jarvis_FINAL_FIXES.log
?? services/ms_jarvis_FINAL_WORKING.log
?? services/ms_jarvis_GENTLE_FILTER.log
?? services/ms_jarvis_REFINED.log
?? services/ms_jarvis_ULTIMATE.py.OLD
?? services/ms_jarvis_ULTIMATE.py.backup_1760806129
?? services/ms_jarvis_ULTIMATE.py.before_agent_fix
?? services/ms_jarvis_ULTIMATE.py.before_bbb
?? services/ms_jarvis_ULTIMATE.py.before_fixes
?? services/ms_jarvis_ULTIMATE.py:_9222.log
?? services/ms_jarvis_WITH_IMPORTS.log
?? services/ms_jarvis_WORKING.log
?? services/ms_jarvis_agents_ollama.py
?? services/ms_jarvis_agents_ollama.py.before_identity
?? services/ms_jarvis_agents_ollama_9907.log
?? services/ms_jarvis_agents_service.py
?? services/ms_jarvis_agents_service_9608.log
?? services/ms_jarvis_alerting_manager.py
?? services/ms_jarvis_alerting_manager_9714.log
?? services/ms_jarvis_api_docs.py
?? services/ms_jarvis_api_docs_9889.log
?? services/ms_jarvis_attribute_table_service.py
?? services/ms_jarvis_attribute_table_service.py.backup_before_portmanager
?? services/ms_jarvis_attribute_table_service_9679.log
?? services/ms_jarvis_attribute_table_sync_continuous.py
?? services/ms_jarvis_attribute_table_sync_continuous.py.BROKEN
?? services/ms_jarvis_attribute_table_sync_continuous.py.backup_before_portmanager
?? services/ms_jarvis_attribute_table_sync_continuous.py.backup_vocabulary_cleanup
?? services/ms_jarvis_attribute_table_sync_continuous_9389.log
?? services/ms_jarvis_attributes_gis.csv
?? services/ms_jarvis_attributes_live.csv
?? services/ms_jarvis_authentic_multi_llm.py
?? services/ms_jarvis_authentic_multi_llm.py.pre_dynamic_discovery
?? services/ms_jarvis_authentic_multi_llm_9760.log
?? services/ms_jarvis_auto_service.py
?? services/ms_jarvis_auto_service.py.backup_vocabulary_cleanup
?? services/ms_jarvis_auto_service_9756.log
?? services/ms_jarvis_autonomous_learner.current.log
?? services/ms_jarvis_autonomous_learner.log
?? services/ms_jarvis_autonomous_learner.py
?? services/ms_jarvis_autonomous_learner.py.backup_before_portmanager
?? services/ms_jarvis_autonomous_learner.py.backup_day2
?? services/ms_jarvis_autonomous_learner.py.bak.prededupe
?? services/ms_jarvis_autonomous_learner.py.norag.20260119-091256
?? services/ms_jarvis_autonomous_learner.py.stub.20260119-091524
?? services/ms_jarvis_autonomous_learner_9309.log
?? services/ms_jarvis_autonomous_learner_FIXED.log
?? services/ms_jarvis_autonomous_learner_FIXED.py
?? services/ms_jarvis_autonomous_learner_FIXED_9590.log
?? services/ms_jarvis_autonomous_learner_WITH_FIFTH_DGM.py
?? services/ms_jarvis_autonomous_learner_WITH_FIFTH_DGM.py.backup_before_portmanager
?? services/ms_jarvis_autonomous_learner_WITH_FIFTH_DGM_9695.log
?? services/ms_jarvis_autonomous_learner_optimized.current.log
?? services/ms_jarvis_autonomous_learner_optimized.py
?? services/ms_jarvis_autonomous_learner_optimized.py.backup_before_auto_research
?? services/ms_jarvis_autonomous_learner_optimized.py.backup_before_portmanager
?? services/ms_jarvis_autonomous_learner_optimized.py.bak_1765235983
?? services/ms_jarvis_autonomous_learner_optimized.py.pre_dynamic_discovery
?? services/ms_jarvis_autonomous_learner_optimized.py.pre_rag_1765237169
?? services/ms_jarvis_autonomous_learner_optimized.py.pre_rag_1765237222
?? services/ms_jarvis_autonomous_learner_optimized_9771.log
?? services/ms_jarvis_autonomous_learner_with_dgm.log
?? services/ms_jarvis_bbb_proxy.py
?? services/ms_jarvis_blockchain_deployment.py
?? services/ms_jarvis_blockchain_deployment_9327.log
?? services/ms_jarvis_blood_brain_barrier.py
?? services/ms_jarvis_blood_brain_barrier.py.backup_1759893188
?? services/ms_jarvis_blood_brain_barrier.py.pre_constitutional
?? services/ms_jarvis_blood_brain_barrier_9772.log
?? services/ms_jarvis_brain.py
?? services/ms_jarvis_brain.py.PORT8000_BACKUP
?? services/ms_jarvis_brain.py.pre_dynamic_discovery
?? services/ms_jarvis_brain_9991.log
?? services/ms_jarvis_brain_orchestrator_advanced.py
?? services/ms_jarvis_brain_orchestrator_advanced_9722.log
?? services/ms_jarvis_chromadb_query.py
?? services/ms_jarvis_chromadb_query_9014.log
?? services/ms_jarvis_clean.log
?? services/ms_jarvis_cleanup_manager.py
?? services/ms_jarvis_cleanup_manager_9125.log
?? services/ms_jarvis_command_orchestrator.py
?? services/ms_jarvis_command_orchestrator.py.backup_before_spiritual_fix
?? services/ms_jarvis_command_orchestrator.py.backup_holy_spirit
?? services/ms_jarvis_command_orchestrator.py.backup_sanctuary_builder
?? services/ms_jarvis_command_orchestrator.py.pre_dynamic_discovery
?? services/ms_jarvis_command_orchestrator_9167.log
?? services/ms_jarvis_command_orchestrator_FINAL.log
?? services/ms_jarvis_command_orchestrator_FINAL.py
?? services/ms_jarvis_command_orchestrator_FINAL.py.pre_dynamic_discovery
?? services/ms_jarvis_command_orchestrator_FINAL_9079.log
?? services/ms_jarvis_command_orchestrator_v1.py.backup
?? services/ms_jarvis_command_orchestrator_v2.py.backup
?? services/ms_jarvis_command_orchestrator_v3.py.backup
?? services/ms_jarvis_command_orchestrator_v5.0_preachy.py
?? services/ms_jarvis_command_orchestrator_v5.0_preachy.py.pre_dynamic_discovery
?? services/ms_jarvis_command_orchestrator_v5.0_preachy_9630.log
?? services/ms_jarvis_command_orchestrator_v5_backup.py
?? services/ms_jarvis_command_orchestrator_v5_backup.py.pre_dynamic_discovery
?? services/ms_jarvis_command_orchestrator_v5_backup_9725.log
?? services/ms_jarvis_complete_knowledge_ingestion.py
?? services/ms_jarvis_complete_knowledge_ingestion_9627.log
?? services/ms_jarvis_conscious_collective.py
?? services/ms_jarvis_conscious_collective_9579.log
?? services/ms_jarvis_consciousness_bridge.py
?? services/ms_jarvis_consciousness_bridge.py.backup_1759895250
?? services/ms_jarvis_consciousness_bridge.py.backup_1759895606
?? services/ms_jarvis_consciousness_bridge.py.backup_1760220435
?? services/ms_jarvis_consciousness_bridge.py.backup_before_22llm
?? services/ms_jarvis_consciousness_bridge.py.backup_before_22llm_hierarchy
?? services/ms_jarvis_consciousness_bridge.py.backup_before_hierarchy
?? services/ms_jarvis_consciousness_bridge.py.backup_pre_fixes
?? services/ms_jarvis_consciousness_bridge.py.backup_pre_location_integration
?? services/ms_jarvis_consciousness_bridge.py.bak.20260626_202219
?? services/ms_jarvis_consciousness_bridge.py.before_complete_architecture
?? services/ms_jarvis_consciousness_bridge.py.before_final_fix
?? services/ms_jarvis_consciousness_bridge.py.before_full_integration
?? services/ms_jarvis_consciousness_bridge.py.before_judge_fix
?? services/ms_jarvis_consciousness_bridge.py.before_mamma_protocol
?? services/ms_jarvis_consciousness_bridge.py.before_persona_fix
?? services/ms_jarvis_consciousness_bridge.py.before_prompt_fix
?? services/ms_jarvis_consciousness_bridge.py.before_rag_web
?? services/ms_jarvis_consciousness_bridge.py.before_small_models
?? services/ms_jarvis_consciousness_bridge.py.before_theology
?? services/ms_jarvis_consciousness_bridge.py.before_true_woah
?? services/ms_jarvis_consciousness_bridge.py.original
?? services/ms_jarvis_consciousness_bridge.py.phase1_working
?? services/ms_jarvis_consciousness_bridge.py.pre_agent_identity
?? services/ms_jarvis_consciousness_bridge.py.pre_dynamic_discovery
?? services/ms_jarvis_consciousness_bridge.py.pre_identity_integration
?? services/ms_jarvis_consciousness_bridge.py.safe_backup
?? services/ms_jarvis_consciousness_bridge.py.working_backup
?? services/ms_jarvis_consciousness_bridge_9188.log
?? services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py
?? services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py.backup_vocabulary_cleanup
?? services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM_9327.log
?? services/ms_jarvis_consciousness_bridge_enhanced.py
?? services/ms_jarvis_consciousness_bridge_enhanced_9599.log
?? services/ms_jarvis_consciousness_bridge_parallel_woah.py
?? services/ms_jarvis_consciousness_bridge_parallel_woah.py.backup_vocabulary_cleanup
?? services/ms_jarvis_consciousness_bridge_parallel_woah_9424.log
?? services/ms_jarvis_consciousness_bridge_service.py
?? services/ms_jarvis_consciousness_bridge_service_9295.log
?? services/ms_jarvis_consciousness_bridge_woah.psychology_patched.py
?? services/ms_jarvis_consciousness_bridge_woah.psychology_patched_9839.log
?? services/ms_jarvis_consciousness_bridge_woah.py
?? services/ms_jarvis_consciousness_bridge_woah.py.backup_20251031
?? services/ms_jarvis_consciousness_bridge_woah_9042.log
?? services/ms_jarvis_consciousness_complete.py
?? services/ms_jarvis_consciousness_complete.py.pre_dynamic_discovery
?? services/ms_jarvis_consciousness_complete_9108.log
?? services/ms_jarvis_consciousness_enhancement_production.py
?? services/ms_jarvis_consciousness_enhancement_production.py.bak-20260627-230136
?? services/ms_jarvis_consciousness_enhancement_production.py.bak_20260627_200214
?? services/ms_jarvis_consciousness_enhancement_production.py.bak_loopbackfix_20260627_201449
?? services/ms_jarvis_consciousness_enhancement_production.py.stub_20260627_210104
?? services/ms_jarvis_consciousness_enhancement_production_9046.log
?? services/ms_jarvis_consciousness_final.py
?? services/ms_jarvis_consciousness_final.py.pre_dynamic_discovery
?? services/ms_jarvis_consciousness_final_9876.log
?? services/ms_jarvis_consciousness_poster.py
?? services/ms_jarvis_consciousness_poster.py.backup_vocabulary_cleanup
?? services/ms_jarvis_consciousness_poster_9092.log
?? services/ms_jarvis_consciousness_poster_FIXED.log
?? services/ms_jarvis_consciousness_poster_FIXED.py
?? services/ms_jarvis_consciousness_poster_FIXED.py.pre_dynamic_discovery
?? services/ms_jarvis_consciousness_poster_FIXED_9939.log
?? services/ms_jarvis_consciousness_unified_bridge.py
?? services/ms_jarvis_consciousness_unified_bridge.py.bak-4010-20260627-223558
?? services/ms_jarvis_consciousness_unified_bridge.py.bak_20260627_204846
?? services/ms_jarvis_consciousness_unified_bridge.py.bak_20260627_211029
?? services/ms_jarvis_consciousness_unified_bridge.py.bak_autofix_20260627_202522
?? services/ms_jarvis_consciousness_unified_bridge.py.bak_blockfix_20260627_202618
?? services/ms_jarvis_consciousness_unified_bridge.py.bak_exactfix_20260627_203011
?? services/ms_jarvis_consciousness_unified_bridge.py.bak_local4021_20260627_201741
?? services/ms_jarvis_consciousness_unified_bridge_9924.log
?? services/ms_jarvis_consensus_service.py
?? services/ms_jarvis_consensus_service.py.bak_20260627_200820
?? services/ms_jarvis_consensus_service.py.bak_osfix_20260627_201104
?? services/ms_jarvis_consensus_service.py.before_honest
?? services/ms_jarvis_consensus_service.py.pre_dynamic_discovery
?? services/ms_jarvis_consensus_service_9921.log
?? services/ms_jarvis_contract_builder.log
?? services/ms_jarvis_contract_builder.py
?? services/ms_jarvis_contract_builder_9572.log
?? services/ms_jarvis_contract_builder_v2.py
?? services/ms_jarvis_contract_builder_v2_9785.log
?? services/ms_jarvis_conversational_chat.py
?? services/ms_jarvis_conversational_chat_9131.log
?? services/ms_jarvis_conversational_gateway_4022.py
?? services/ms_jarvis_conversational_gateway_4022.py.pre_dynamic_discovery
?? services/ms_jarvis_conversational_gateway_4022_9065.log
?? services/ms_jarvis_daily_backup.py
?? services/ms_jarvis_daily_backup.py.backup_vocabulary_cleanup
?? services/ms_jarvis_daily_backup_9632.log
?? services/ms_jarvis_darwin_godel_machine.py
?? services/ms_jarvis_darwin_godel_machine_9142.log
?? services/ms_jarvis_dynamic_model_selector.py
?? services/ms_jarvis_dynamic_model_selector_9235.log
?? services/ms_jarvis_easyocr_processor.py
?? services/ms_jarvis_easyocr_processor.py.backup_vocabulary_cleanup
?? services/ms_jarvis_easyocr_processor_9131.log
?? services/ms_jarvis_easyocr_processor_old.py
?? services/ms_jarvis_easyocr_processor_old_9788.log
?? services/ms_jarvis_email_identity_verifier.py
?? services/ms_jarvis_email_identity_verifier_9688.log
?? services/ms_jarvis_email_monitor.py
?? services/ms_jarvis_email_monitor_9077.log
?? services/ms_jarvis_email_service.py
?? services/ms_jarvis_email_service.py.backup_vocabulary_cleanup
?? services/ms_jarvis_email_service_9406.log
?? services/ms_jarvis_eternal_watchdog.py
?? services/ms_jarvis_eternal_watchdog.py.NEW
?? services/ms_jarvis_eternal_watchdog.py.ORIGINAL
?? services/ms_jarvis_eternal_watchdog.py.backup
?? services/ms_jarvis_eternal_watchdog_9232.log
?? services/ms_jarvis_exclusive_training_layer.py
?? services/ms_jarvis_exclusive_training_layer_9763.log
?? services/ms_jarvis_expiration_monitor.py
?? services/ms_jarvis_expiration_monitor_9432.log
?? services/ms_jarvis_facebook_CONSCIOUSNESS.log
?? services/ms_jarvis_facebook_CONSCIOUSNESS.py
?? services/ms_jarvis_facebook_CONSCIOUSNESS_9361.log
?? services/ms_jarvis_facebook_CONSCIOUSNESS_FIXED.backup.1762804903
?? services/ms_jarvis_facebook_CONSCIOUSNESS_FIXED.log
?? services/ms_jarvis_facebook_CONSCIOUSNESS_FIXED.py
?? services/ms_jarvis_facebook_CONSCIOUSNESS_FIXED.py.backup.1762804577
?? services/ms_jarvis_facebook_CONSCIOUSNESS_FIXED.py.backup_1762804648
?? services/ms_jarvis_facebook_CONSCIOUSNESS_FIXED.py.backup_20251109_180216
?? services/ms_jarvis_facebook_CONSCIOUSNESS_FIXED.py.pre_dynamic_discovery
?? services/ms_jarvis_facebook_CONSCIOUSNESS_FIXED_9556.log
?? services/ms_jarvis_facebook_DGM.py
?? services/ms_jarvis_facebook_DGM.py.pre_dynamic_discovery
?? services/ms_jarvis_facebook_DGM_9231.log
?? services/ms_jarvis_facebook_PRODUCTION.log
?? services/ms_jarvis_facebook_PRODUCTION.py
?? services/ms_jarvis_facebook_PRODUCTION.py.backup2
?? services/ms_jarvis_facebook_PRODUCTION.py.backup_permissions
?? services/ms_jarvis_facebook_PRODUCTION_9632.log
?? services/ms_jarvis_facebook_ULTIMATE.py.OLD
?? services/ms_jarvis_facebook_async.py
?? services/ms_jarvis_facebook_async_9489.log
?? services/ms_jarvis_facebook_autonomous_social.py
?? services/ms_jarvis_facebook_autonomous_social_9815.log
?? services/ms_jarvis_facebook_brain_integrated.py
?? services/ms_jarvis_facebook_brain_integrated_9597.log
?? services/ms_jarvis_facebook_dgm_woah.psychology_patched.py
?? services/ms_jarvis_facebook_dgm_woah.psychology_patched_9919.log
?? services/ms_jarvis_facebook_dgm_woah.py
?? services/ms_jarvis_facebook_dgm_woah.py.backup_20251031
?? services/ms_jarvis_facebook_dgm_woah.py.backup_vocabulary_cleanup
?? services/ms_jarvis_facebook_dgm_woah_9189.log
?? services/ms_jarvis_facebook_full.py
?? services/ms_jarvis_facebook_full.py.backup_vocabulary_cleanup
?? services/ms_jarvis_facebook_full_9115.log
?? services/ms_jarvis_facebook_intelligent.py
?? services/ms_jarvis_facebook_intelligent_9629.log
?? services/ms_jarvis_facebook_poster.py
?? services/ms_jarvis_facebook_poster_8040.py
?? services/ms_jarvis_facebook_poster_8040_9168.log
?? services/ms_jarvis_facebook_poster_9077.log
?? services/ms_jarvis_facebook_poster_FIXED.log
?? services/ms_jarvis_facebook_poster_FIXED.py
?? services/ms_jarvis_facebook_poster_FIXED_9220.log
?? services/ms_jarvis_facebook_poster_temp.py
?? services/ms_jarvis_facebook_poster_temp_9391.log
?? services/ms_jarvis_facebook_poster_v3.py
?? services/ms_jarvis_facebook_poster_v3_9706.log
?? services/ms_jarvis_facebook_rag.py
?? services/ms_jarvis_facebook_rag_9924.log
?? services/ms_jarvis_facebook_webhook.py
?? services/ms_jarvis_facebook_webhook_9049.log
?? services/ms_jarvis_facebook_webhooks.py
?? services/ms_jarvis_facebook_webhooks_9671.log
?? services/ms_jarvis_fact_filter.py
?? services/ms_jarvis_fact_filter_9255.log
?? services/ms_jarvis_feed_reader_PRODUCTION.log
?? services/ms_jarvis_feed_reader_PRODUCTION.py
?? services/ms_jarvis_feed_reader_PRODUCTION.py.backup_vocabulary_cleanup
?? services/ms_jarvis_feed_reader_PRODUCTION_9003.log
?? services/ms_jarvis_feed_reader_WORKING.py
?? services/ms_jarvis_feed_reader_WORKING_9521.log
?? services/ms_jarvis_fifth_dgm_orchestrator.psychology_patched.py
?? services/ms_jarvis_fifth_dgm_orchestrator.psychology_patched.py.pre_dynamic_discovery
?? services/ms_jarvis_fifth_dgm_orchestrator.psychology_patched_9742.log
?? services/ms_jarvis_fifth_dgm_orchestrator.py
?? services/ms_jarvis_fifth_dgm_orchestrator.py.backup_20251031
?? services/ms_jarvis_fifth_dgm_orchestrator.py.backup_20251205233002
?? services/ms_jarvis_fifth_dgm_orchestrator.py.before_filtering
?? services/ms_jarvis_fifth_dgm_orchestrator.py.before_woah_fix
?? services/ms_jarvis_fifth_dgm_orchestrator.py.pre_dynamic_discovery
?? services/ms_jarvis_fifth_dgm_orchestrator_9919.log
?? services/ms_jarvis_fractal_consciousness.py
?? services/ms_jarvis_fractal_consciousness.py.backup_vocabulary_cleanup
?? services/ms_jarvis_fractal_consciousness_9298.log
?? services/ms_jarvis_fractal_consciousness_FIXED.log
?? services/ms_jarvis_fractal_consciousness_FIXED.py
?? services/ms_jarvis_fractal_consciousness_FIXED_9130.log
?? services/ms_jarvis_fractal_dgm_woah.py
?? services/ms_jarvis_fractal_dgm_woah.py.backup_vocabulary_cleanup
?? services/ms_jarvis_fractal_dgm_woah_9260.log
?? services/ms_jarvis_full_neurobio_chat.py
?? services/ms_jarvis_full_neurobio_chat.py.bak_20260118152254
?? services/ms_jarvis_full_neurobio_chat.py.pre_dynamic_discovery
?? services/ms_jarvis_full_neurobio_chat_9765.log
?? services/ms_jarvis_fully_autonomous_coordinator.py
?? services/ms_jarvis_fully_autonomous_coordinator_9723.log
?? services/ms_jarvis_generate_frontend.py
?? services/ms_jarvis_generate_frontend.py.pre_dynamic_discovery
?? services/ms_jarvis_generate_frontend_9210.log
?? services/ms_jarvis_geo_tracker_simple.py
?? services/ms_jarvis_geo_tracker_simple_9755.log
?? services/ms_jarvis_geo_ueid_integration.py
?? services/ms_jarvis_geo_ueid_integration_9103.log
?? services/ms_jarvis_geographic_research.js
?? services/ms_jarvis_gis_enhanced_chat.py
?? services/ms_jarvis_gis_enhanced_chat.py.pre_dynamic_discovery
?? services/ms_jarvis_gis_enhanced_chat_9250.log
?? services/ms_jarvis_gis_georeferencing_sync.py
?? services/ms_jarvis_gis_georeferencing_sync.py.backup
?? services/ms_jarvis_gis_georeferencing_sync.py.backup_before_portmanager
?? services/ms_jarvis_gis_georeferencing_sync.py.backup_vocabulary_cleanup
?? services/ms_jarvis_gis_georeferencing_sync_9635.log
?? services/ms_jarvis_gis_georeferencing_sync_FIXED.py
?? services/ms_jarvis_gis_georeferencing_sync_FIXED_9846.log
?? services/ms_jarvis_gis_georeferencing_sync_FIXED_V2.py
?? services/ms_jarvis_gis_georeferencing_sync_FIXED_V2_9805.log
?? services/ms_jarvis_gis_query_service.py
?? services/ms_jarvis_gis_query_service_9770.log
?? services/ms_jarvis_gis_query_service_backup.py
?? services/ms_jarvis_gis_query_service_backup_9603.log
?? services/ms_jarvis_gis_query_with_bbb_gisgeodb.psychology_patched.py
?? services/ms_jarvis_gis_query_with_bbb_gisgeodb.psychology_patched_9935.log
?? services/ms_jarvis_gis_query_with_bbb_gisgeodb.py
?? services/ms_jarvis_gis_query_with_bbb_gisgeodb.py.backup_20251031
?? services/ms_jarvis_gis_query_with_bbb_gisgeodb_9097.log
?? services/ms_jarvis_i_containers_FIXED.log
?? services/ms_jarvis_i_containers_FIXED.py
?? services/ms_jarvis_i_containers_FIXED_9718.log
?? services/ms_jarvis_i_containers_service.py
?? services/ms_jarvis_i_containers_service.py.backup_1759893188
?? services/ms_jarvis_i_containers_service.py.broken
?? services/ms_jarvis_i_containers_service_9287.log
?? services/ms_jarvis_id_ocr_processor.py
?? services/ms_jarvis_id_ocr_processor_9463.log
?? services/ms_jarvis_integration_hub.py
?? services/ms_jarvis_integration_hub_9081.log
?? services/ms_jarvis_layer2_dgm.psychology_patched.py
?? services/ms_jarvis_layer2_dgm.psychology_patched.py.backup_vocabulary_cleanup
?? services/ms_jarvis_layer2_dgm.psychology_patched_9089.log
?? services/ms_jarvis_layer2_dgm.py
?? services/ms_jarvis_layer2_dgm.py.backup_20251031
?? services/ms_jarvis_layer2_dgm_9770.log
?? services/ms_jarvis_layer2_woah.py
?? services/ms_jarvis_layer2_woah_9735.log
?? services/ms_jarvis_link_reader_scheduled.py
?? services/ms_jarvis_link_reader_scheduled_9430.log
?? services/ms_jarvis_link_reader_scheduled_FIXED.log
?? services/ms_jarvis_link_reader_scheduled_FIXED.py
?? services/ms_jarvis_link_reader_scheduled_FIXED.py.backup_vocabulary_cleanup
?? services/ms_jarvis_link_reader_scheduled_FIXED_9450.log
?? services/ms_jarvis_llm_bridge.current.log
?? services/ms_jarvis_llm_bridge.py
?? services/ms_jarvis_llm_bridge.py.broken
?? services/ms_jarvis_llm_bridge.py.pre_dynamic_discovery
?? services/ms_jarvis_llm_bridge_9908.log
?? services/ms_jarvis_llm_bridge_simple.py
?? services/ms_jarvis_llm_bridge_simple_9303.log
?? services/ms_jarvis_local_resources_api.py
?? services/ms_jarvis_location_services.py
?? services/ms_jarvis_location_services_9808.log
?? services/ms_jarvis_main_gateway.backup_1762220815.py
?? services/ms_jarvis_main_gateway.backup_1762220815_9760.log
?? services/ms_jarvis_main_gateway.backup_error
?? services/ms_jarvis_main_gateway.backup_error.py
?? services/ms_jarvis_main_gateway.backup_error_9347.log
?? services/ms_jarvis_main_gateway.backup_test.py
?? services/ms_jarvis_main_gateway.backup_test_9747.log
?? services/ms_jarvis_main_gateway.broken_final.py
?? services/ms_jarvis_main_gateway.broken_final_9520.log
?? services/ms_jarvis_main_gateway.error_final
?? services/ms_jarvis_main_gateway.error_final.py
?? services/ms_jarvis_main_gateway.error_final_9676.log
?? services/ms_jarvis_main_gateway.pre_fix.py
?? services/ms_jarvis_main_gateway.pre_fix.py.backup_vocabulary_cleanup
?? services/ms_jarvis_main_gateway.pre_fix_9581.log
?? services/ms_jarvis_main_gateway.proxy_backup.py
?? services/ms_jarvis_main_gateway.proxy_backup_9695.log
?? services/ms_jarvis_main_gateway.proxy_final.py
?? services/ms_jarvis_main_gateway.proxy_final_9690.log
?? services/ms_jarvis_main_gateway.proxy_still_broken.py
?? services/ms_jarvis_main_gateway.proxy_still_broken_9517.log
?? services/ms_jarvis_main_gateway.py
?? services/ms_jarvis_main_gateway.py.30endpoints_backup.py
?? services/ms_jarvis_main_gateway.py.30endpoints_backup_9352.log
?? services/ms_jarvis_main_gateway.py.backup2
?? services/ms_jarvis_main_gateway.py.broken
?? services/ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py
?? services/ms_jarvis_main_gateway.py.corrupted37_backup_1762223499_9030.log
?? services/ms_jarvis_main_gateway.py.full_backup_1762223304.py
?? services/ms_jarvis_main_gateway.py.full_backup_1762223304_9476.log
?? services/ms_jarvis_main_gateway.py.locked_backup
?? services/ms_jarvis_main_gateway_8000.py
?? services/ms_jarvis_main_gateway_9124.log
?? services/ms_jarvis_memory_service.py
?? services/ms_jarvis_memory_service_8010.log
?? services/ms_jarvis_memory_service_9400.log
?? services/ms_jarvis_messenger_ui.py
?? services/ms_jarvis_messenger_ui_9297.log
?? services/ms_jarvis_messenger_ui_final.py
?? services/ms_jarvis_messenger_ui_final_9846.log
?? services/ms_jarvis_messenger_ui_fixed.py
?? services/ms_jarvis_messenger_ui_fixed_9737.log
?? services/ms_jarvis_metadata_aware_learner.py
?? services/ms_jarvis_metadata_aware_learner_9888.log
?? services/ms_jarvis_microsoft_integration.py
?? services/ms_jarvis_microsoft_integration.py.backup_vocabulary_cleanup
?? services/ms_jarvis_microsoft_integration_9436.log
?? services/ms_jarvis_microsoft_integration_FIXED.log
?? services/ms_jarvis_microsoft_integration_FIXED.py
?? services/ms_jarvis_microsoft_integration_FIXED_9923.log
?? services/ms_jarvis_mother_carrie_protocols.py
?? services/ms_jarvis_mother_carrie_protocols_9632.log
?? services/ms_jarvis_mountainshares_integration.py
?? services/ms_jarvis_mountainshares_integration_9432.log
?? services/ms_jarvis_neurobiological_master.py
?? services/ms_jarvis_neurobiological_master.py.backup_1759893188
?? services/ms_jarvis_neurobiological_master_9993.log
?? services/ms_jarvis_paddleocr_processor.py
?? services/ms_jarvis_paddleocr_processor_9897.log
?? services/ms_jarvis_phi_probe.py
?? services/ms_jarvis_phi_probe.py.bak.20260714
?? services/ms_jarvis_production_chat.py
?? services/ms_jarvis_production_chat.py.backup_before_neurobio
?? services/ms_jarvis_production_chat.py.backup_vocabulary_cleanup
?? services/ms_jarvis_production_chat.py.pre_dynamic_discovery
?? services/ms_jarvis_production_chat_9814.log
?? services/ms_jarvis_production_chat_BACKUP.py
?? services/ms_jarvis_production_chat_BACKUP.py.pre_dynamic_discovery
?? services/ms_jarvis_production_chat_BACKUP_9082.log
?? services/ms_jarvis_production_chat_BEFORE_GIS.py
?? services/ms_jarvis_production_chat_BEFORE_GIS.py.pre_dynamic_discovery
?? services/ms_jarvis_production_chat_BEFORE_GIS_9373.log
?? services/ms_jarvis_psychology_services.py
?? services/ms_jarvis_psychology_services_9738.log
?? services/ms_jarvis_qualia_engine.py
?? services/ms_jarvis_qualia_engine.py.backup_1759893188
?? services/ms_jarvis_qualia_engine_9390.log
?? services/ms_jarvis_rag_server.py
?? services/ms_jarvis_rag_server.py.bak.prerollcap
?? services/ms_jarvis_ram_watchdog.py
?? services/ms_jarvis_ram_watchdog_9946.log
?? services/ms_jarvis_seamless_monitor.py
?? services/ms_jarvis_seamless_monitor_9930.log
?? services/ms_jarvis_service_factory.py
?? services/ms_jarvis_service_factory_9936.log
?? services/ms_jarvis_showcase_api.py
?? services/ms_jarvis_showcase_api_9963.log
?? services/ms_jarvis_silent_geo_tracker.py
?? services/ms_jarvis_silent_geo_tracker_9572.log
?? services/ms_jarvis_simple_web_ui.py
?? services/ms_jarvis_simple_web_ui_9649.log
?? services/ms_jarvis_spiritual_services.py
?? services/ms_jarvis_spiritual_services_4009.log
?? services/ms_jarvis_spiritual_services_9826.log
?? services/ms_jarvis_substack_reader.py
?? services/ms_jarvis_substack_reader_9316.log
?? services/ms_jarvis_swap_memory_manager.py
?? services/ms_jarvis_swap_memory_manager_9115.log
?? services/ms_jarvis_swarm_intelligence.py
?? services/ms_jarvis_swarm_intelligence.py.pre_dynamic_discovery
?? services/ms_jarvis_swarm_intelligence_9921.log
?? services/ms_jarvis_sync_monitor.py
?? services/ms_jarvis_sync_monitor.py.backup_before_portmanager
?? services/ms_jarvis_sync_monitor_9898.log
?? services/ms_jarvis_temporal_consciousness.py
?? services/ms_jarvis_temporal_consciousness_9220.log
?? services/ms_jarvis_theological_integration.py
?? services/ms_jarvis_theological_integration.py.backup_vocabulary_cleanup
?? services/ms_jarvis_theological_integration_9882.log
?? services/ms_jarvis_tile_index_20251028_225447.csv
?? services/ms_jarvis_tile_index_20251028_234406.csv
?? services/ms_jarvis_toroidal_consciousness.py
?? services/ms_jarvis_toroidal_consciousness_9720.log
?? services/ms_jarvis_truth_filter_gisgeodb.py
?? services/ms_jarvis_truth_filter_gisgeodb_9054.log
?? services/ms_jarvis_ueid_system.py
?? services/ms_jarvis_ueid_system_9671.log
?? services/ms_jarvis_ueid_wallet_integration.py
?? services/ms_jarvis_ueid_wallet_integration_9477.log
?? services/ms_jarvis_unified_gateway.py
?? services/ms_jarvis_unified_gateway.py.BEFORE_REAL_CHAT_1768842649
?? services/ms_jarvis_unified_gateway.py.FORCED_UNIFIED_BACKUP
?? services/ms_jarvis_unified_gateway.py.WORKING_1768842334
?? services/ms_jarvis_unified_gateway.py.backup_vocabulary_cleanup
?? services/ms_jarvis_unified_gateway.py.bak_1768840523
?? services/ms_jarvis_unified_gateway.py.bak_1768841920
?? services/ms_jarvis_unified_gateway.py.pre_constitutional
?? services/ms_jarvis_unified_gateway_9085.log
?? services/ms_jarvis_unified_gateway_v4.3.20251124.py
?? services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py
?? services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION_9882.log
?? services/ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP.py
?? services/ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP.py.backup.1762458819
?? services/ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP.py.backup_vocabulary_cleanup
?? services/ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP_9314.log
?? services/ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER.py
?? services/ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER_9195.log
?? services/ms_jarvis_unified_gateway_v4.3.backup.py
?? services/ms_jarvis_unified_gateway_v4.3.backup_9871.log
?? services/ms_jarvis_unified_gateway_v4.3.log
?? services/ms_jarvis_unified_gateway_v4.3.pre_manifest.backup.py
?? services/ms_jarvis_unified_gateway_v4.3.pre_manifest.backup_9113.log
?? services/ms_jarvis_unified_gateway_v4.3.py
?? services/ms_jarvis_unified_gateway_v4.3.py.BACKUP_1762777467
?? services/ms_jarvis_unified_gateway_v4.3.py.BACKUP_AUTH_1762778121
?? services/ms_jarvis_unified_gateway_v4.3.py.BACKUP_CHAT_1762778286
?? services/ms_jarvis_unified_gateway_v4.3.py.BACKUP_CORRECT_20251109_141823
?? services/ms_jarvis_unified_gateway_v4.3.py.BACKUP_DNSADD_202511100838
?? services/ms_jarvis_unified_gateway_v4.3.py.BACKUP_GIS
?? services/ms_jarvis_unified_gateway_v4.3.py.BACKUP_JWT_202511100840
?? services/ms_jarvis_unified_gateway_v4.3.py.BACKUP_MICROSERVICES
?? services/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915
?? services/ms_jarvis_unified_gateway_v4.3.py.BACKUP_SWAGGER_EXPANSION_20251109_141525
?? services/ms_jarvis_unified_gateway_v4.3.py.BEFORE_INVESTIGATION
?? services/ms_jarvis_unified_gateway_v4.3.py.FINAL_BACKUP_1762710032
?? services/ms_jarvis_unified_gateway_v4.3.py.PRE_GUARDS_20251105_171934
?? services/ms_jarvis_unified_gateway_v4.3.py.REGISTRY_FIX_BACKUP
?? services/ms_jarvis_unified_gateway_v4.3.py.backup.1762722387
?? services/ms_jarvis_unified_gateway_v4.3.py.backup.pre_consciousness
?? services/ms_jarvis_unified_gateway_v4.3.py.backup_1762520299
?? services/ms_jarvis_unified_gateway_v4.3.py.bak_alt
?? services/ms_jarvis_unified_gateway_v4.3.py.bak_chroma
?? services/ms_jarvis_unified_gateway_v4.3.py.bak_config
?? services/ms_jarvis_unified_gateway_v4.3.py.bak_ports
?? services/ms_jarvis_unified_gateway_v4.3.py.original
?? services/ms_jarvis_unified_gateway_v4.3.py.pre_dynamic_discovery
?? services/ms_jarvis_unified_gateway_v4.3.py.working_backup
?? services/ms_jarvis_unified_gateway_v4.3_9863.log
?? services/ms_jarvis_unified_rag_bridge.py
?? services/ms_jarvis_unified_rag_bridge_9600.log
?? services/ms_jarvis_unified_swagger_gateway.log
?? services/ms_jarvis_unified_swagger_gateway.py
?? services/ms_jarvis_unified_swagger_gateway.py.pre_dynamic_discovery
?? services/ms_jarvis_unified_swagger_gateway_9825.log
?? services/ms_jarvis_unified_swagger_gateway_BACKUP.py
?? services/ms_jarvis_unified_swagger_gateway_BACKUP_9797.log
?? services/ms_jarvis_unified_swagger_gateway_CLEAN.py
?? services/ms_jarvis_unified_swagger_gateway_CLEAN_9092.log
?? services/ms_jarvis_unified_swagger_gateway_COMPLETE.py
?? services/ms_jarvis_unified_swagger_gateway_COMPLETE.py.pre_dynamic_discovery
?? services/ms_jarvis_unified_swagger_gateway_COMPLETE_9011.log
?? services/ms_jarvis_unified_swagger_gateway_FINAL.log
?? services/ms_jarvis_unified_swagger_gateway_FINAL.psychology_patched.log
?? services/ms_jarvis_unified_swagger_gateway_FINAL.psychology_patched.py
?? services/ms_jarvis_unified_swagger_gateway_FINAL.psychology_patched_9134.log
?? services/ms_jarvis_unified_swagger_gateway_FINAL.py
?? services/ms_jarvis_unified_swagger_gateway_FINAL.py.backup_20251031
?? services/ms_jarvis_unified_swagger_gateway_FINAL.py.layer2_backup
?? services/ms_jarvis_unified_swagger_gateway_FINAL_9845.log
?? services/ms_jarvis_unified_swagger_gateway_FIXED.log
?? services/ms_jarvis_unified_swagger_gateway_FIXED.py
?? services/ms_jarvis_unified_swagger_gateway_FIXED.py.backup_20251112_180010
?? services/ms_jarvis_unified_swagger_gateway_FIXED.py.backup_20251116_083447
?? services/ms_jarvis_unified_swagger_gateway_FIXED.py.backup_clean
?? services/ms_jarvis_unified_swagger_gateway_FIXED.py.backup_original_20251112_180033
?? services/ms_jarvis_unified_swagger_gateway_FIXED.py.backup_pre_email_fix
?? services/ms_jarvis_unified_swagger_gateway_FIXED.py.bak
?? services/ms_jarvis_unified_swagger_gateway_FIXED.py.bak_20260118152630
?? services/ms_jarvis_unified_swagger_gateway_FIXED.py.broken
?? services/ms_jarvis_unified_swagger_gateway_FIXED.py.new
?? services/ms_jarvis_unified_swagger_gateway_FIXED.py.pre_dynamic_discovery
?? services/ms_jarvis_unified_swagger_gateway_FIXED_9867.log
?? services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py
?? services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP_9365.log
?? services/ms_jarvis_unified_swagger_gateway_PROD.py
?? services/ms_jarvis_unified_swagger_gateway_PROD_9481.log
?? services/ms_jarvis_unified_swagger_gateway_SECURED.py
?? services/ms_jarvis_unified_swagger_gateway_SECURED.py.backup_vocabulary_cleanup
?? services/ms_jarvis_unified_swagger_gateway_SECURED_9347.log
?? services/ms_jarvis_v3.log
?? services/ms_jarvis_v4.log
?? services/ms_jarvis_venv_scheduler.py
?? services/ms_jarvis_venv_scheduler_9811.log
?? services/ms_jarvis_venv_scheduler_FIXED.backup
?? services/ms_jarvis_venv_scheduler_FIXED.bak
?? services/ms_jarvis_venv_scheduler_FIXED.bak2
?? services/ms_jarvis_venv_scheduler_FIXED.bakfinal
?? services/ms_jarvis_venv_scheduler_FIXED.final_bak
?? services/ms_jarvis_venv_scheduler_FIXED.log
?? services/ms_jarvis_venv_scheduler_FIXED.py
?? services/ms_jarvis_venv_scheduler_FIXED.safe
?? services/ms_jarvis_venv_scheduler_FIXED.safe2
?? services/ms_jarvis_venv_scheduler_FIXED.superbak
?? services/ms_jarvis_venv_scheduler_FIXED.totalsafe
?? services/ms_jarvis_venv_scheduler_FIXED.ultimate_bak
?? services/ms_jarvis_venv_scheduler_FIXED.ultrasafe
?? services/ms_jarvis_venv_scheduler_FIXED_9252.log
?? services/ms_jarvis_venv_scheduler_SIMPLE.py
?? services/ms_jarvis_venv_scheduler_SIMPLE_9550.log
?? services/ms_jarvis_web_deployer.py
?? services/ms_jarvis_web_deployer_9991.log
?? services/ms_jarvis_web_deployer_old.py
?? services/ms_jarvis_web_deployer_old_9156.log
?? services/ms_jarvis_web_research.py
?? services/ms_jarvis_web_research.py.backup
?? services/ms_jarvis_web_research.py.bak.1768179270
?? services/ms_jarvis_web_research.py.broken
?? services/ms_jarvis_web_research.py.broken_backup
?? services/ms_jarvis_web_research_9032.log
?? services/ms_jarvis_web_research_aggregate.py
?? services/ms_jarvis_web_research_aggregate.py.bak.1768179811
?? services/ms_jarvis_web_research_aggregate.py.bak.1768180273
?? services/ms_jarvis_web_research_aggregate.safe.20260119-094221.py
?? services/ms_jarvis_web_research_fixed.py
?? services/ms_jarvis_web_research_fixed_9119.log
?? services/ms_jarvis_web_research_simple.py
?? services/ms_jarvis_web_research_simple_9552.log
?? services/ms_jarvis_web_research_v2.current.log
?? services/ms_jarvis_web_research_v2.log
?? services/ms_jarvis_web_research_v2.py
?? services/ms_jarvis_web_research_v2_9404.log
?? services/ms_jarvis_woah_algorithms.log
?? services/ms_jarvis_woah_algorithms.py
?? services/ms_jarvis_woah_algorithms_9915.log
?? services/ms_jarvis_woah_algorithms_enhanced.py
?? services/ms_jarvis_woah_algorithms_enhanced_9290.log
?? services/ms_mountainshares_analytics.py
?? services/ms_mountainshares_coordinator.py
?? services/ms_mountainshares_indexer.py
?? services/msjarvis.log
?? services/msjarvis.service
?? services/msjarvis_autolearner.log
?? services/msjarvis_autolearner_minimal.py
?? services/msjarvis_bbb_proxy.py
?? services/msjarvis_benefit_rag.py
?? services/msjarvis_client.py
?? services/msjarvis_functions_fixed.zip
?? services/msjarvis_gateway_v2_final.py
?? services/msjarvis_gateway_v2_final.py.pre_dynamic_discovery
?? services/msjarvis_gateway_v2_final_9306.log
?? services/msjarvis_gateway_with_judge_filtering.py
?? services/msjarvis_gateway_with_judge_filtering.py.pre_dynamic_discovery
?? services/msjarvis_gateway_with_judge_filtering_9631.log
?? services/msjarvis_geotiff_to_csv.sh
?? services/msjarvis_gis_manifest.csv
?? services/msjarvis_gis_manifest_DEDUPED.csv
?? services/msjarvis_gis_manifest_FULL.csv
?? services/msjarvis_icontainers.py
?? services/msjarvis_ports_runtime.txt
?? services/msjarvis_processes_runtime.txt
?? services/msjarvis_qualia_engine.log
?? services/msjarvis_semaphore.py
?? services/msjarvis_shp_to_csv.sh
?? services/msjarvis_unified_gateway.py
?? services/msjarvis_woah_algorithms.py
?? services/msjarvis_woah_algorithms_service.py
?? services/msjarvis_woah_runner.py
?? services/msjarvis_wv_entangled_gateway.py
?? services/msjarvis_wv_entangled_gateway.py.bak-async-20260626-153849
?? services/msjarvis_wv_entangled_gateway.py.bak-async2-154005
?? services/msjarvis_wv_entangled_gateway.py.bak-enqueue-161324
?? services/msjarvisattributesgis_census.csv
?? services/msjarvisattributesgis_small.csv
?? services/msjarvisautonomouslearner.py
?? services/msjarvisautonomouslearner.py.bak-20260114054922
?? services/msjarvisautonomouslearner.py.bak-20260114060021
?? services/msjarvisconsciousnessbridge.py
?? services/msjarvisconsciousnessbridge.py.FULL_BACKUP_BEFORE_BRIDGE_RESET
?? services/msjarvisconsciousnessbridge_9819.log
?? services/msjarvisfractalconsciousness.py
?? services/msjarvisicontainersservice.py
?? services/msjarvismaingateway.py
?? services/msjarvisragserver_wvpatch.py
?? services/msjarvisragserverwvpatch.py
?? services/msjarvisspiritualservices_4009.log
?? services/msjarvistoroidalconsciousness.py
?? services/msjarvisunifiedgateway.py
?? services/msjarvisunifiedswaggergateway.py
?? services/msjarvisunifiedswaggergatewayFINAL.py
?? services/msjarvisunifiedswaggergatewayFIXED.log
?? services/msjarvisunifiedswaggergatewayFIXED.py
?? services/msjarvisunifiedswaggergatewayFIXED.py.BEFORE_DOCKER_REWIRE
?? services/msjarvisunifiedswaggergatewayFIXED.py.backup_20251116_083717
?? services/msjarvisunifiedswaggergatewayFIXED.py.backup_20251116_092415
?? services/msjarvisunifiedswaggergatewayFIXED.py.bak_202512011953
?? services/msjarvisunifiedswaggergatewayFIXED.py.pre_dynamic_discovery
?? services/msjarvisunifiedswaggergatewayFIXED_9540.log
?? services/msjarviswebresearch.log
?? services/multi_model_consensus.py
?? services/multi_rag_4011.log
?? services/multi_rag_dgm.log
?? services/multi_rag_dgm_system.py
?? services/multi_rag_dgm_system_4011.log
?? services/multi_rag_dgm_system_9307.log
?? services/multi_rag_dgm_system_9307_4011.log
?? services/multiragdgmsystem_4011.log
?? services/multiragdgmsystem_4011_test.log
?? services/my_service.py
?? services/my_service_9004.log
?? services/nationalatlasstreams_usgs_199903_ll83_attrs.csv
?? services/nationalatlasstreams_usgs_199903_utm83_attrs.csv
?? services/nationalregister_point_20200923_attrs.csv
?? services/nationalregister_point_20200923_utm27_attrs.csv
?? services/nationalregisterofhistoricplacespoints_nationalparkser_45ec46d0_attrs.csv
?? services/nationalregisterofhistoricplacespoints_natoinalpakrser_8d965955_attrs.csv
?? services/nationalregisterofhistoricplacespolygons_nationaparkse_b9d30a70_attrs.csv
?? services/nationalwaterwaynetwork_usarmycorpsofengineers_2001_ll83_attrs.csv
?? services/nationalwaterwaynetwork_usarmycorpsofengineers_2001_utm83_attrs.csv
?? services/nationalwaterwaynetworkports_usarmycorpsofengineers_2001_ll83_attrs.csv
?? services/nationalwaterwaynetworkports_usarmycorpsofengineers_2001_utm83_attrs.csv
?? services/nationaregisterofhistoricplacespoints_nationalparkserv_ba8eebd5_attrs.csv
?? services/nationaregisterofhistoricplacespolygons_nationalparkse_cab42150_attrs.csv
?? services/natoinalregisterofhistoricplacespoints_nationalparkser_ca43510e_attrs.csv
?? services/naviagablewaterways_usarmycropsofengineers_2006_utm83_attrs.csv
?? services/navigablewaterwaysrivermiles_usarmycropsofengineers_2006_utm83_attrs.csv
?? services/navigablewaterwaysstructures_usarmycorpsofengineers_2006_utm83_attrs.csv
?? services/netlify.toml
?? services/neuro_adapter.py
?? services/neuro_blood_brain_barrier.py
?? services/neuro_consciousness_containers.py
?? services/neuro_i_containers.py
?? services/neuro_master_service.py
?? services/neuro_prefrontal_cortex.py
?? services/neuro_qualia_engine.py
?? services/neuro_subconscious.py
?? services/neurobiological_brain/
?? services/neurobiological_integration.py
?? services/neurobiological_integration.py.pre_dynamic_discovery
?? services/neurobiologicalbrain/
?? services/nohup.out
?? services/npm-deps.json
?? services/npm-packages.txt
?? services/nursinghomes_wvdem_041219_gcs84_attrs.csv
?? services/nursinghomes_wvdem_041219_utm83_attrs.csv
?? services/oauth2_callback.py
?? services/oauth2_config.json
?? services/oauth2_handler.py
?? services/officebuildings_wvdo_200807_utm83_attrs.csv
?? services/old_chroma_analysis.json
?? services/ollama_fix.py
?? services/open_ports.txt
?? services/open_ports_full.txt
?? services/openapitools.json
?? services/optimize_egeria_complete.py
?? services/optimize_models_for_vram.py
?? services/optimized_timeouts.py
?? services/orchestrator.log
?? services/orchestrator_loop.log
?? services/override_launcher.py
?? services/package-lock.json
?? services/package.json
?? services/paired_services.txt
?? services/parallel_processing.py
?? services/paroleoffices_manysources_2008_utm83_attrs.csv
?? services/paroleoffices_manysources_2008_wgs84_attrs.csv
?? services/parse_world_files.py
?? services/patch_agent_identity.py
?? services/patch_autonomous_learner_gisgeodb.py
?? services/patch_fractal.py
?? services/patch_learner_clean.py
?? services/patch_mother_persona.py
?? services/patch_neuro.py
?? services/patch_qualia.py
?? services/performance_optimization_analyzer.py
?? services/performance_optimization_analyzer.py.backup_vocabulary_cleanup
?? services/performance_optimization_analyzer.py.pre_dynamic_discovery
?? services/persona_fix.txt
?? services/phase1_integration.py
?? services/phase2_integration.py
?? services/phase3_integration.py
?? services/phase4_5_integration.py
?? services/phase6_integration.py
?? services/phase7_integration.py
?? services/phase7_integration.py.pre_dynamic_discovery
?? services/pid_code_backtrace.txt
?? services/pid_dir_map.txt
?? services/pid_port_map.txt
?? services/pituitary_gland.log
?? services/pituitary_gland.py
?? services/placesofworship_hsip_20080723_utm83_attrs.csv
?? services/placesofworship_hsip_20080723_wgs84_attrs.csv
?? services/policedept_wvdem_012319_gcs84_attrs.csv
?? services/policedept_wvdem_012319_utm83_attrs.csv
?? services/polling_client.py
?? services/populate_redetermination_tracker.py
?? services/populate_security_layers_test.py
?? services/populatedplaces_census_201112_utm83_attrs.csv
?? services/populatedplaces_census_20112_gcs83_attrs.csv
?? services/populatedplaces_census_2020_utm83_attrs.csv
?? services/populatedplaces_census_2020_wma84_attrs.csv
?? services/populatedplaces_uscensus_1990_ll83_attrs.csv
?? services/populatedplaces_uscensus_1990_utm83_attrs.csv
?? services/populationdatablockgroups_uscensus_2000_ll83_attrs.csv
?? services/populationdatablockgroups_uscensus_2000_utm83_attrs.csv
?? services/port_9000_69dgm_bridge.py
?? services/port_9000_69dgm_bridge_9769.log
?? services/port_9000_academic_extension.py
?? services/port_9000_chat_wrapper_69dgm.py
?? services/port_9000_chat_wrapper_69dgm_9641.log
?? services/port_9001_ARCHITECTURE_CORRECT.py
?? services/port_9001_FINAL_FIX.log
?? services/port_9001_FINAL_FIX.py
?? services/port_9001_FINAL_WORKING.log
?? services/port_9001_FINAL_WORKING.py
?? services/port_9001_proxy_simple.py
?? services/port_9001_ui_DIRECT.py
?? services/port_9001_ui_FIXED.log
?? services/port_9001_ui_FIXED.py
?? services/port_9001_ui_MYSQL.py
?? services/port_9001_ui_MYSQL_PROD.py
?? services/port_9001_ui_WITH_CONVERSATIONS.py
?? services/port_9001_ui_WORKING.py
?? services/port_9001_ui_wrapper.py
?? services/port_manager.py
?? services/port_manager.py.broken_backup
?? services/port_manager.py.broken_v2
?? services/port_manager_fixed.py
?? services/port_service_audit.txt
?? services/ports_diff_msjarvis.txt
?? services/post_every_4_hours.sh
?? services/pow_wvgistc_062919_utm83_attrs.csv
?? services/pow_wvgistc_062919_wgs84_attrs.csv
?? services/privkey.pem
?? services/probe_services.py
?? services/process_comprehensive_gis.py
?? services/process_gis_shapefiles.py
?? services/process_statewide_gis_bulk.py
?? services/processed_gis/
?? services/prod.yaml
?? services/production_chat.log
?? services/production_chat_with_cors.log
?? services/production_chat_with_gis.log
?? services/pronoun_fixer.py
?? services/proxy_8060.py
?? services/proxy_8060.py.backup_vocabulary_cleanup
?? services/psychological_rag_domain.py
?? services/psychological_rag_domain_9941.log
?? services/psychology_integration_adapter.py
?? services/psychology_loop_closer.py
?? services/psychology_services.log
?? services/public_form_simplified.py
?? services/publichealthdepts_hsip_20091229_gcs83_attrs.csv
?? services/publichealthdepts_hsip_20091229_utm83_attrs.csv
?? services/python/
?? services/python_commands.txt
?? services/python_ports.txt
?? services/qualia_adapter.py
?? services/qualia_adapter.py.backup_vocabulary_cleanup
?? services/qualia_email_registration_orchestrator_69dgm.py
?? services/qualia_email_registration_orchestrator_69dgm_9615.log
?? services/qualia_engine.log
?? services/qualia_unified_orchestrator_69dgm.py
?? services/qualia_unified_orchestrator_69dgm_9653.log
?? services/qualia_unified_orchestrator_69dgm_ACTIVE.log
?? services/qualia_unified_orchestrator_69dgm_ACTIVE.py
?? services/qualia_unified_orchestrator_69dgm_ACTIVE_9527.log
?? services/qualia_unified_write_orchestrator_69dgm.py
?? services/qualia_unified_write_orchestrator_69dgm_9921.log
?? services/qualiaunifiedorchestrator69dgm.py
?? services/quantum_dashboard.py
?? services/quantum_insight_llm.py
?? services/quantum_state_engine.py
?? services/quantum_state_engine_7360.log
?? services/query_benefits_system.py
?? services/query_enhancer.js
?? services/query_imm_and_programs.py
?? services/quick_optimizations.py
?? services/quick_tone_test.sh
?? services/rag/
?? services/rag_5001_active.log
?? services/rag_5001_final.log
?? services/rag_5001_fixed.log
?? services/rag_5001_httpclient.log
?? services/rag_5001_restart.log
?? services/rag_5100_ensemble.py
?? services/rag_5100_ensemble_9488.log
?? services/rag_5100_ensemble_fast.py
?? services/rag_5100_ensemble_fast.py.pre_dynamic_discovery
?? services/rag_5100_ensemble_fast_9530.log
?? services/rag_5100_final.py
?? services/rag_5100_final.py.pre_dynamic_discovery
?? services/rag_5100_final_9592.log
?? services/rag_5100_live.log
?? services/rag_client.py
?? services/rag_command_module.py
?? services/rag_command_module.py.pre_dynamic_discovery
?? services/rag_command_module_4011.log
?? services/rag_command_module_9476.log
?? services/rag_direct_debug.log
?? services/rag_direct_debug.py
?? services/rag_direct_debug_8199.log
?? services/rag_dynamic.log
?? services/rag_ensemble_300s.log
?? services/rag_ensemble_fast.log
?? services/rag_ensemble_live.log
?? services/rag_evidence_aggregator.py
?? services/rag_final.log
?? services/rag_first_workflow.py
?? services/rag_first_workflow_9869.log
?? services/rag_general.py
?? services/rag_geospatial.py
?? services/rag_geospatial_context.py
?? services/rag_heartbeat_monitor.py
?? services/rag_httpclient.log
?? services/rag_local_resources.py
?? services/rag_mandatory.log
?? services/rag_port5001.log
?? services/rag_query_router.py
?? services/rag_restart.log
?? services/rag_server.current.log
?? services/rag_server.log
?? services/rag_server.psychology_patched.py
?? services/rag_server.psychology_patched_9448.log
?? services/rag_server.py
?? services/rag_server.py.backup_20251031
?? services/rag_server.py.bak
?? services/rag_server.py.before_delete
?? services/rag_server.py.before_filtering
?? services/rag_server.py.before_store
?? services/rag_server_8003.log
?? services/rag_server_9005.log
?? services/rag_server_main.py
?? services/rag_server_main.py.RAG_WORKING_20260116
?? services/rag_server_main.py.backup.20260119-090738
?? services/rag_server_main.py.backup_vocabulary_cleanup
?? services/rag_server_main.py.norag.20260119-091256
?? services/rag_server_main.py.stub.20260119-091532
?? services/rag_server_main_9555.log
?? services/rag_server_min.current.log
?? services/rag_server_min.py
?? services/rag_server_restored.log
?? services/rag_simple.log
?? services/rag_simple.py
?? services/rag_simple.py.pre_dynamic_discovery
?? services/rag_simple_4011.log
?? services/rag_simple_9831.log
?? services/rag_simple_live.log
?? services/rag_temporal.py
?? services/rag_temporal_heartbeat.py
?? services/rag_to_gis_sync.py
?? services/rag_to_gis_sync_9633.log
?? services/rag_topic_router.py
?? services/rag_workflow.py
?? services/rag_workflow_9845.log
?? services/railnetworkregion_usdot_200203_ll83_attrs.csv
?? services/railnetworkregion_usdot_200203_utm83_attrs.csv
?? services/railnetworkwv_usdot_200203_ll83_attrs.csv
?? services/railnetworkwv_usdot_200203_utm83_attrs.csv
?? services/railroads_rahalltransportationinstitute_2005_utm83_attrs.csv
?? services/read_architecture_docs.sh
?? services/read_dgm_architecture.sh
?? services/real_services.txt
?? services/real_services_clean.txt
?? services/real_services_detected.txt
?? services/real_services_final.txt
?? services/real_services_prod.txt
?? services/realtimestreamflowstations_usgs_200012_ll27_attrs.csv
?? services/realtimestreamflowstations_usgs_200012_utm27_attrs.csv
?? services/realtimestreamflowstations_usgs_200012_utm83_attrs.csv
?? services/rebuild_query_service.py
?? services/recover_160_queries.py
?? services/recover_chromadb_FIXED.log
?? services/recover_chromadb_FIXED.py
?? services/recover_chromadb_to_gisgeodb.py
?? services/recreationalwwtrails_ofwv_20151117_utm83_attrs.csv
?? services/redirect_4015.log
?? services/redirect_4015_to_4020.py
?? services/regionalplanninganddevelopmentcouncil_wvdo_1971_ll83_attrs.csv
?? services/regionalplanninganddevelopmentcouncil_wvdo_1971_utm83_attrs.csv
?? services/register_agents_from_csv.py
?? services/register_agents_from_csv.sh
?? services/register_agents_from_csv_strict.py
?? services/register_all_services.sh
?? services/register_hilbert_services.py
?? services/register_hilbert_services.py.pre_dynamic_discovery
?? services/register_services.py
?? services/register_to_hilbert_chromadb.py
?? services/registration_backend.backup2
?? services/registration_biometric_production_final.py
?? services/registration_facebook_form.html
?? services/registration_service_clean.backup_1762220206.py
?? services/registration_service_clean.py
?? services/registration_service_clean.py.broken
?? services/registration_stage2_opencv.py.backup_1762172804
?? services/reload_all_knowledge.py
?? services/reload_all_knowledge.py.backup_vocabulary_cleanup
?? services/remaining_services.txt
?? services/remove_duplicate_inits.py
?? services/replace_dolphin_phi.py
?? services/requirements-freeze.txt
?? services/requirements-list.txt
?? services/requirements-rag.txt
?? services/requirements.txt
?? services/requirements_gbim.txt
?? services/requirements_semaphore.txt
?? services/requirements_temporal.txt
?? services/requirements_toroidal.txt
?? services/response.json
?? services/response_filter.py
?? services/response_sanitizer.py
?? services/rest_endpoints.txt
?? services/restart_all_services.sh
?? services/restart_and_verify_8008.sh
?? services/restart_ms_jarvis_services.sh
?? services/restore_pia_wiring.py
?? services/restore_pia_wiring.py.backup_vocabulary_cleanup
?? services/restored_documents.json
?? services/resume_ingest_gbim_to_chroma.py
?? services/resume_sync_wvgistc_buildings.py
?? services/retrieval_router.py
?? services/retrieval_spiritual.py
?? services/roche_llm.py
?? services/roche_llm.stub.py
?? services/route_declarations_clean.txt
?? services/route_declarations_raw.txt
?? services/rpm-list.txt
?? services/run_agi_test_suite.sh
?? services/run_autonomous_learner_once.py
?? services/run_gateway_with_guards.py
?? services/running_python_services.txt
?? services/running_services.log
?? services/s
?? services/safe_ingest_gbim_to_chroma.py
?? services/safe_integration.py
?? services/safe_integration.py.pre_dynamic_discovery
?? services/sanctuary_construction_monitor.py
?? services/sanctuary_construction_monitor_gateway.py
?? services/schema_aware_topic_planner.py
?? services/schema_registry.py
?? services/search_different_perspective.sh
?? services/search_metadata.py
?? services/search_metadata.py:
?? services/search_wsl_backup.sh
?? services/seed_spatial_identity.py
?? services/serve_full_brain.sh
?? services/server.js
?? services/service_api_check.txt
?? services/service_api_report.txt
?? services/service_discovery.log
?? services/service_discovery.py
?? services/service_discovery_glassbox.py
?? services/service_discovery_glassbox.py.backup
?? services/service_endpoints.json
?? services/service_http_check.txt
?? services/service_pid_directory_map.txt
?? services/service_registry_client.py
?? services/service_registry_client.py.bak_1769196795
?? services/service_registry_client.py.bak_1769196836
?? services/service_registry_client.py.bak_1769196865
?? services/services_config.yaml
?? services/services_config.yaml.bak_1760565919
?? services/services_list.txt
?? services/services_manifest_progress.md
?? services/services_msjarvisunifiedgatewayv4_3.py
?? "services/ses related to Ms. Jarvis"
?? services/set_intelligent_accuracy_scores.py
?? services/set_ultra_long_timeout.sh
?? services/settings_snippet.txt
?? services/setup_frontend.sh
?? services/setup_holy_spirit_discovery.sh
?? services/setup_holy_spirit_email_alert_both.sh
?? services/setup_rag.sh
?? services/setup_rag_standalone.sh
?? services/sewertreatmentplants_wvdep_200203_utm83_attrs.csv
?? services/silence_memory_errors
?? services/silence_memory_errors.py
?? services/simple_orchestrator_fix.py
?? services/simple_prompt_fix.py
?? services/smart_auto_store.py
?? services/solidwastefacilities_wvdep_200202_ll83_attrs.csv
?? services/solidwastefacilities_wvdep_200202_utm83_attrs.csv
?? services/spiritual_4009.log
?? services/spiritual_rag_domain.py
?? services/spiritual_rag_domain_4009.log
?? services/spiritual_rag_domain_9439.log
?? services/springs_wvges_1986_ll83_attrs.csv
?? services/springs_wvges_1986_utm83_attrs.csv
?? services/stage2_biometric.py
?? services/stage2_biometric_backup.py
?? services/stakeholder_health_access_tests.py
?? services/stakeholder_health_access_tests_v2.py
?? services/start_all_jarvis_services_manual.sh
?? services/start_all_msjarvis_services.sh
?? services/start_all_services.sh
?? services/start_all_services_with_ports.sh
?? services/start_and_integrate_web_research.sh
?? services/start_cloudflare_tunnel.sh
?? services/start_command_orchestrator.sh
?? services/start_critical_msjarvis_services.sh
?? services/start_dgm_woah.sh
?? services/start_egeria_voice_service.sh
?? services/start_email_service_with_env.sh
?? services/start_facebook_4021.py
?? services/start_gateway_with_guards.py
?? services/start_gateway_with_guards.py.BACKUP
?? services/start_gateway_with_guards.py.backup
?? services/start_gateway_with_guards.py.backup_cors_1762517335
?? services/start_gateway_with_guards.py.bak2
?? services/start_gateway_with_guards.py.pre_dynamic_discovery
?? services/start_hilbert_8235.sh
?? services/start_mountainshares_deployment.sh
?? services/start_msjarvis_complete.sh
?? services/start_msjarvis_services_fixed.sh
?? services/start_services_simple.sh
?? services/start_swap_manager.sh
?? services/stateofwvhousedistricts_wvlegislativeservices_2010_attrs.csv
?? services/stateofwvsenatedistricts_wvlegislativeservices_2010_attrs.csv
?? services/states_region_ll83_attrs.csv
?? services/static/
?? services/stop_all_services.sh
?? services/store_test.json
?? services/stripe-config.js
?? services/structurepointsnorth_samb_2003_utm83_attrs.csv
?? services/structurepointssouth_samb_2003_utm83_attrs.csv
?? services/structurepolygons_samb_2003_utm83_attrs.csv
?? services/substack_rss_reader.py
?? services/summarize_docs.py
?? services/summits_gistc_052012_utm83_shp_attrs.csv
?? services/summits_gistc_052012_wgs84_shp_attrs.csv
?? services/surveycontrol_nationalgeodeticsurvey_102011_gcs83_attrs.csv
?? services/swagger-config.json
?? services/swagger_chat_integration.py
?? services/swagger_gateway.py
?? services/swagger_gateway.py.PORT8000_BACKUP
?? services/swagger_gateway.py.pre_dynamic_discovery
?? services/swagger_gateway_FIXED.log
?? services/swagger_gateway_FIXED.py
?? services/swagger_gateway_FIXED.py.pre_dynamic_discovery
?? services/swarm_intelligence_main.py
?? services/swarm_watchdog.log
?? services/swarm_watchdog.py
?? services/switch_to_22llm.sh
?? services/switch_to_small_models.py
?? services/sync_geodb_to_chromadb.py
?? services/sync_health_access_to_chromadb.py
?? services/system_dashboard.py
?? services/system_dashboard.py.pre_dynamic_discovery
?? services/tag_quantum_gbim.py
?? services/talk.sh
?? services/talk_safely.sh
?? services/talk_safely_FIXED.sh
?? services/talk_to_jarvis.py
?? services/talk_to_jarvis_9216.log
?? services/talk_with_save.sh
?? services/temporal.log
?? services/temporal_consciousness.py
?? services/test.py
?? services/test_aacpe_features.py
?? services/test_aapcappe_corpus.py
?? services/test_aapcappe_retrieval.py
?? services/test_agi_capabilities.sh
?? services/test_agi_full_responses.sh
?? services/test_all_32_services.sh
?? services/test_all_models.sh
?? services/test_all_models_fixed.sh
?? services/test_authentic_voice.sh
?? services/test_chroma_client.py
?? services/test_chromadb_heartbeat.py
?? services/test_chromadb_v2_heartbeat.py
?? services/test_ddg_verbose.py
?? services/test_email_after_consent.sh
?? services/test_end_to_end_woah_fifthdgm.py
?? services/test_fifth_dgm_integration.py
?? services/test_fifth_dgm_integration.py.backup_vocabulary_cleanup
?? services/test_fifth_dgm_integration_9342.log
?? services/test_final_config.sh
?? services/test_final_stable.sh
?? services/test_full_brain_integration.py
?? services/test_full_brain_integration.py.backup_vocabulary_cleanup
?? services/test_full_brain_integration.py.pre_dynamic_discovery
?? services/test_gbim_llm_summary.py
?? services/test_gbim_semantic_query.py
?? services/test_geodb_llm_summary.py
?? services/test_gis_chat.py
?? services/test_health_access_gbim.py
?? services/test_imm_query.py
?? services/test_knowledge_base.py
?? services/test_location.log
?? services/test_method_tracking.py
?? services/test_multi_collection_query.py
?? services/test_rag.py
?? services/test_rag_9790.log
?? services/test_retrieval_endpoint.py
?? services/test_spatial_awareness.py
?? services/timberremovalvolume_usfs_1996_utm83_attrs.csv
?? services/topic_entanglement.py
?? services/toroidal_service.py
?? services/towers_wvpublicbroadcasting_2002_ll83_attrs.csv
?? services/towers_wvpublicbroadcasting_2002_utm83_attrs.csv
?? services/towersam_fcc_200202_utm83_attrs.csv
?? services/towersasr_fcc_200202_ll83_attrs.csv
?? services/towersasr_fcc_200202_utm83_attrs.csv
?? services/towerscellular_fcc_200202_ll83_attrs.csv
?? services/towerscellular_fcc_200202_utm83_attrs.csv
?? services/towersfm_fcc_200202_utm83_attrs.csv
?? services/towersmicrowave_fcc_200202_ll83_attrs.csv
?? services/towersmicrowave_fcc_200202_utm83_attrs.csv
?? services/towerspager_fcc_200202_ll83_attrs.csv
?? services/towerspager_fcc_200202_utm83_attrs.csv
?? services/towersprivate_fcc_200202_ll83_attrs.csv
?? services/towersprivate_fcc_200202_utm83_attrs.csv
?? services/trigger_entangled_assets.py
?? services/truly_unpaired_services.txt
?? services/truth_filter.log
?? services/truth_filter_bbb_verification.py
?? services/truth_filter_service.py
?? services/ucg_production.log
?? "services/udo ss -tulpn | grep -Ei 'msjarvis|uvicorn|docker-proxy' "
?? services/ultimate.current.log
?? services/ultimate8050.log
?? services/ultimate8051.current.log
?? services/ultimate_8051.current.log
?? services/ultimate_8055.current.log
?? services/ultimate_audit_with_scheduler.sh
?? services/ultimate_chat_current.txt
?? services/ultimate_msjarvis_audit.sh
?? services/ultimate_web_orchestrator.py
?? services/ultimate_web_orchestrator.py.backup_1760565056
?? services/ultimate_web_orchestrator.py.backup_vocabulary_cleanup
?? services/ultimate_web_orchestrator.py.bak_1760565732
?? services/ultimate_web_orchestrator.py.bak_1760566442
?? services/ultimate_web_orchestrator.py.bak_1760567115
?? services/ultimate_web_orchestrator.py.bak_1760567193
?? services/ultra_deep_dgm_search.sh
?? services/unified_consciousness_gateway_PRODUCTION.py
?? services/unified_consciousness_gateway_PRODUCTION.py.backup_20251113_180437
?? services/unified_consciousness_gateway_PRODUCTION.py.backup_cors_1762517930
?? services/unified_consciousness_gateway_PRODUCTION.py.before_memory
?? services/unified_consciousness_gateway_PRODUCTION.py.pre_dynamic_discovery
?? services/unified_orchestrator.py
?? services/unifiedconsciousnessgatewayPRODUCTION.log
?? services/unifiedconsciousnessgatewayPRODUCTION.py
?? services/unifiedgateway.log
?? services/unifiedragbridge.log
?? services/update_carrie_keywords.py
?? services/update_chat_endpoint.sh
?? services/update_facebook_poster.py
?? services/update_gisgeodb_schema.py
?? services/update_gisgeodb_schema.py.backup_vocabulary_cleanup
?? services/update_production_to_v9.py
?? services/update_services_to_use_port_manager.py
?? services/update_theological_boundaries.py
?? services/update_theological_boundaries.py.backup_vocabulary_cleanup
?? services/update_web_chat.py
?? services/update_web_chat.py.backup_vocabulary_cleanup
?? services/update_web_research_package.py
?? services/upgrade_node_and_setup.sh
?? services/use_existing_models.py
?? services/use_reliable_models_only.py
?? services/user_auth_service.py
?? services/user_dashboard.py
?? services/user_registration_form.html
?? services/vatican_scraper.log
?? services/vatican_scraper_service.py
?? services/vatican_scraper_service.py.backup_vocabulary_cleanup
?? services/vectorize_gis_to_chromadb.py
?? services/venv/
?? services/verify_and_document_system.py
?? services/verify_benefit_chroma_sync.py
?? services/verify_facebook_deployment.sh
?? services/veteransaffairsfacilities_manysources_200503_utm83_attrs.csv
?? services/veteransaffairsfacilities_manysources_200503_wgs84_attrs.csv
?? services/view_docs.sh
?? services/votingdistrictswv_legislativeservices_2002_ll83_attrs.csv
?? services/votingdistrictswv_legislativeservices_2002_utm83_attrs.csv
?? services/votingdistrictswv_uscensus_2000_utm83_attrs.csv
?? services/watch_startup.sh
?? services/watchdog.log
?? services/weatherstations_nationalclimatedatacenter_1999_gcs83_attrs.csv
?? services/weatherstations_nationalclimatedatacenter_1999_utm27_attrs.csv
?? services/web_chat.log
?? services/web_chat_server.py
?? services/web_connectivity_analyzer.py
?? services/web_deployer.env
?? services/web_page_ingest.current.log
?? services/web_page_ingest.py
?? services/web_research.log
?? services/web_research.py
?? services/web_research_fail_tracker.py
?? services/web_research_main.current.log
?? services/web_research_main.py
?? services/web_research_main.py.backup_vocabulary_cleanup
?? services/web_research_proxy_8007.log
?? services/web_research_proxy_8007.py
?? services/web_research_requirements.txt
?? services/web_ui_8051.log
?? services/web_ui_final_8051.log
?? services/webhook_notifications.py
?? services/webresearch.log
?? services/website_deployment_manager.py
?? services/wheels/
?? services/windenergyresource_nationalrenewableenergylab_200901_utm83_attrs.csv
?? services/windenergyresource_nationalrenewableenergylab_200901_wgs84_attrs.csv
?? services/wire_layers_into_chat.py
?? services/wire_learner_to_gisgeodb.py
?? services/wire_qualia_to_port8001.py
?? services/woah_1763386738.log
?? services/woah_5003_active.log
?? services/woah_5003_final.log
?? services/woah_command_module.py
?? services/woah_final.log
?? services/woah_fixed.log
?? services/woah_metrics_router.py
?? services/woah_optimizer.log
?? services/woah_optimizer.py
?? services/woah_policy_update.py
?? services/woah_population_state.py
?? services/woah_qualia_bridge.py
?? services/woah_restart.log
?? services/workforceinvestmentareas_wvgistc_200208_ll83_attrs.csv
?? services/working_full_pipeline.py
?? services/working_full_pipeline.py.backup_20251113_180746
?? services/working_full_pipeline.py.backup_vocabulary_cleanup
?? services/working_full_pipeline_FINAL_CONSCIOUSNESS.log
?? services/working_full_pipeline_FINAL_CONSCIOUSNESS.py
?? services/working_full_pipeline_WITH_SPATIAL_TEMPORAL.py
?? services/working_pipeline.log
?? services/wv_county_boundaries_24k_topo_updated_2022_utm83_attrs.csv
?? services/wv_gis_mass_downloader.py
?? services/wv_microsoft_20180207_utm17n83_attrs.csv
?? services/wv_tax_districts_ll83_attrs.csv
?? services/wv_tax_districts_utm83_attrs.csv
?? services/wv_tax_districts_wma84_attrs.csv
?? services/wvgistc_building_footprints_attrs.csv
?? services/wvgistcbuildingfootprints_attrs.csv
?? services/wvstatebounadary100k_usgs_200203_utm83_attrs.csv
?? services/wvstateboundary100k_usgs_200203_ll83_attrs.csv
?? services/wvstateboundary24k_usgs_200203_ll83_attrs.csv
?? services/wvstateboundary24k_usgs_200203_utm83_attrs.csv
?? services/wvstatehousedistricts_manysources_1992_ll83_attrs.csv
?? services/wvstatehousedistricts_manysources_1992_utm83_attrs.csv
?? services/wvstatehousedistricts_manysources_2002_ll83_attrs.csv
?? services/wvstatehousedistricts_manysources_2002_utm83_attrs.csv
?? services/wvstatehousedistricts_wvlegislativeservices_2020_utm83_attrs.csv
?? services/wvstatesenatedistricts_manysources_1992_ll83_attrs.csv
?? services/wvstatesenatedistricts_manysources_1992_utm83_attrs.csv
?? services/wvstatesenatedistricts_manysources_2002_ll83_attrs.csv
?? services/wvstatesenatedistricts_manysources_2002_utm83_attrs.csv
?? services/wvstatesenatedistricts_wvlegislativeservices_2020_utm83_attrs.csv
?? services/wvu_ldap_auth.py
?? services/yarn-packages.txt
?? services/zipcodetabulationarea_census_2020_utm83_attrs.csv
?? services/zipcodetabulationarea_census_2020_wma84_attrs.csv
?? sourcetable
?? spiritual_nbb_backup_20260215_231630.tar.gz
?? spiritual_nbb_fix2_20260215_232031.tar.gz
?? spiritual_rag_deployment_20260215_232717.tar.gz
?? sync_gbim_to_chroma.py
?? test-unified-gateway.sh
?? test_autonomous_learner_store.py
?? test_chatsync.sh
?? test_chatsync_gateway.sh
?? test_end_to_end_woah_fifthdgm.py
?? test_immediate.sh
?? test_msjarvis.golden.sh
?? test_msjarvis.sh
?? test_msjarvis.working.20260119-000202.sh
?? test_provenance_one.sql
?? test_rag_image.py
?? test_rag_text.py
?? test_synthesizer.sh
?? tests/
?? tmp_ingest/
?? tmp_rag_slice.py
?? tools/
?? transferring
?? ultimate8050.log
?? validation/
?? wget-log
?? woah_health.json
?? woah_metrics_example.json
?? woah_openapi.json
?? woah_process_example.json
?? writing
?? wv2020/
?? wv_entangled_context.schema.json
?? wv_entangled_context_model.py
?? wv_gis_layers/
?? wv_gis_layers_catalog.csv
?? wv_gis_layers_process_status.csv
?? wv_like_csv_candidates.txt
?? wv_name_matches_current_pv.txt
DETACHED_HEAD

===== RECENT COMMITS =====
7e58737 (HEAD, tag: hippocampus-fix-2026-06-27, master, hippocampus-working) Fix hippocampus container startup and dependency wiring
9a76b1d fix: pass collection_name string (not object) to get_collection_recency
7b422ed chore: exclude data/ and sqlite files from git tracking
e04ce42 fix(dgm): consolidation keeps newest entry (DESC order, drop older dups)
a7168f4 feat(dgm): /identity + /identity/search + nightly consolidation at 03:00
b64c0fd fix(dgm): safe _init_db column migrations + COALESCE identity endpoints
1e4e0cd feat(dgm): toroidal loop closed — auto-integrate at ≥75% consensus
84b18fb fix: repair secrets block newline collapse + confirm ADMIN_EMAIL clean

===== ARTIFACTS =====
PRESENT 11-tier1-callgraph.txt lines=227 bytes=27612
PRESENT 12-tier1-source-extract.txt lines=2480 bytes=95515
PRESENT 13-tier1-static-graph.txt lines=447 bytes=33153
PRESENT 13-tier1-static-graph.json lines=6627 bytes=151587
PRESENT 14-tier1-dependency-matrix.txt lines=151 bytes=11724
PRESENT 15-meaning-geometry-symbols.txt lines=477 bytes=43957
PRESENT 16-current-runtime-declarations.txt lines=85 bytes=3215

===== SOURCE SYNTAX VALIDATION =====
compileall_exit=0
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/nvme1/msjarvis-rebuild$ cd /mnt/nvme1/msjarvis-rebuild

BASE=/tmp/meaning-geometry-investigation
OUT="$BASE/18-tier1-runtime-connectivity.txt"

{
  printf '%s\n' '===== TIER-1 RUNTIME CONNECTIVITY / EXECUTABILITY AUDIT ====='
  date --iso-8601=seconds

  printf '\n===== GIT IDENTITY =====\n'
  printf 'HEAD: '
  git rev-parse HEAD
  printf 'BRANCH: '
  git symbolic-ref --short -q HEAD || echo DETACHED_HEAD

  printf '\n===== TARGET FILES =====\n'
  for f in \
    services/jarvis_hilbert_semantic.py \
    services/jarvis_hilbert_state.py \
    services/jarvis_hilbert_time.py \
    services/hilbert_spatial_chat.py \
    services/integrate_spatial_temporal.py \
printf '\nWrote: %s\n' "$OUT"====\n'f"s=%s\n' \9][0-9]|:82[0-9][0-9]|:83[0-9][
===== TIER-1 RUNTIME CONNECTIVITY / EXECUTABILITY AUDIT =====
2026-08-10T09:03:43-04:00

===== GIT IDENTITY =====
HEAD: 7e58737f60ef7fad88bd91b45ad484011fc28261
BRANCH: DETACHED_HEAD

===== TARGET FILES =====
PRESENT services/jarvis_hilbert_semantic.py
PRESENT services/jarvis_hilbert_state.py
PRESENT services/jarvis_hilbert_time.py
PRESENT services/hilbert_spatial_chat.py
PRESENT services/integrate_spatial_temporal.py
PRESENT services/gbim_semantic_indexer.py
PRESENT services/gbim_spatial_indexer.py
PRESENT services/gbim_temporal_indexer.py
PRESENT services/geo/similarity.py
PRESENT services/geospatial_resolver.py
PRESENT services/rag_geospatial.py
PRESENT services/rag_geospatial_context.py
PRESENT services/ms_jarvis_phi_probe.py
PRESENT services/quantum_state_engine.py

===== PYTHON IMPORT GRAPH =====

--- services/gbim_semantic_indexer.py ---

--- services/gbim_spatial_indexer.py ---

--- services/gbim_temporal_indexer.py ---

--- services/geo/similarity.py ---

--- services/geospatial_resolver.py ---

--- services/hilbert_spatial_chat.py ---

--- services/integrate_spatial_temporal.py ---

--- services/jarvis_hilbert_semantic.py ---

--- services/jarvis_hilbert_state.py ---

--- services/jarvis_hilbert_time.py ---

--- services/ms_jarvis_phi_probe.py ---

--- services/quantum_state_engine.py ---

--- services/rag_geospatial.py ---

--- services/rag_geospatial_context.py ---

===== DIRECT CALL / ROUTE REFERENCES =====
grep: ./data/mysql/aaacpe: Permission denied
grep: ./data/mysql/gis_rag: Permission denied
./services/hilbert_spatial_chat.py:16:logger = logging.getLogger("hilbert_spatial_chat")
./services/hilbert_spatial_chat.py:308:        "service": "hilbert_spatial_chat",
./services/hilbert_spatial_chat.py:321:        "service": "hilbert_spatial_chat",
./services/hilbert_spatial_chat.py:415:    uvicorn.run("hilbert_spatial_chat:app", host="0.0.0.0", port=port, reload=False)
./services/quantum_state_engine.py:11:SERVICE_NAME = "quantum_state_engine"
./services/quantum_state_engine.py:163:    uvicorn.run("quantum_state_engine:app", host="0.0.0.0", port=SERVICE_PORT)
./services/jarvis_hilbert_state.py:93:        "service": "jarvis_hilbert_state",
./services/ms_jarvis_phi_probe.py:3:ms_jarvis_phi_probe.py
./services/ms_jarvis_phi_probe.py:252:    uvicorn.run("ms_jarvis_phi_probe:app", host="0.0.0.0", port=port, reload=False)
./services/gbim_temporal_indexer.py:4:SERVICE_NAME = "gbim_temporal_indexer"
./services/gbim_temporal_indexer.py:41:    uvicorn.run("gbim_temporal_indexer:app", host="127.0.0.1", port=SERVICE_PORT)
./services/rag_geospatial_context.py:4:SERVICE_NAME = "rag_geospatial_context"
./services/rag_geospatial_context.py:41:    uvicorn.run("rag_geospatial_context:app", host="0.0.0.0", port=SERVICE_PORT)
./services/retrieval_router.py:102:from services.geospatial_resolver import resolve_place_attrs
./services/gbim_semantic_indexer.py:4:SERVICE_NAME = "gbim_semantic_indexer"
./services/gbim_semantic_indexer.py:41:    uvicorn.run("gbim_semantic_indexer:app", host="127.0.0.1", port=SERVICE_PORT)
./services/gbim_spatial_indexer.py:4:SERVICE_NAME = "gbim_spatial_indexer"
./services/gbim_spatial_indexer.py:41:    uvicorn.run("gbim_spatial_indexer:app", host="127.0.0.1", port=SERVICE_PORT)
./services/jarvis_hilbert_time.py:2:jarvis_hilbert_time.py — Temporal Hilbert Axis service (Ch 49)
./services/jarvis_hilbert_time.py:23:logger = logging.getLogger("jarvis_hilbert_time")
./services/jarvis_hilbert_time.py:96:        "service": "jarvis_hilbert_time",
./services/jarvis_hilbert_semantic.py:10:logger = logging.getLogger("jarvis_hilbert_semantic")
./services/jarvis_hilbert_semantic.py:124:        "service": "jarvis_hilbert_semantic",
./services/jarvis_hilbert_semantic.py:143:        "service": "jarvis_hilbert_semantic",
grep: ./data/mysql-recovery-copy/aaacpe: Permission denied
grep: ./data/mysql-recovery-copy/gis_rag: Permission denied
grep: ./data/local_resources: Permission denied

===== DOCKER COMPOSE SERVICE DECLARATIONS =====
2:  jarvis-unified-gateway:
86:  jarvis-20llm-production:
115:  jarvis-wv-entangled-gateway:
147:  jarvis-chat-worker:
174:  llm1-proxy:
188:  llm2-proxy:
202:  llm3-proxy:
216:  llm4-proxy:
230:  llm5-proxy:
244:  llm6-proxy:
258:  llm7-proxy:
272:  llm8-proxy:
286:  llm9-proxy:
300:  llm10-proxy:
314:  llm11-proxy:
328:  llm12-proxy:
342:  llm13-proxy:
356:  llm14-proxy:
370:  llm15-proxy:
384:  llm16-proxy:
398:  llm17-proxy:
412:  llm18-proxy:
426:  llm19-proxy:
440:  llm20-proxy:
454:  llm21-proxy:
468:  llm22-proxy:
482:  jarvis-lm-synthesizer:
510:  jarvis-hippocampus:
546:  jarvis-brain-orchestrator:
586:  jarvis-agents-service:
608:  jarvis-web-research:
630:  jarvis-swarm-intelligence:
653:  jarvis-fifth-dgm:
677:  jarvis-mother-protocols:
689:  jarvis-temporal-consciousness:
701:  jarvis-69dgm-bridge:
715:  jarvis-blood-brain-barrier:
737:  jarvis-woah:
762:  jarvis-consciousness-bridge:
787:  jarvis-qualia-engine:
809:  jarvis-i-containers:
821:  jarvis-semaphore:
833:  jarvis-neurobiological-master:
861:  jarvis-fractal-consciousness:
882:  jarvis-autonomous-learner:
907:  jarvis-ollama:
935:  jarvis-redis:
958:  jarvis-chroma:
989:  nbb-i-containers:
1006:  nbb_consciousness_containers:
1016:  nbb_spiritual_root:
1027:  nbb_woah_algorithms:
1037:  nbb_prefrontal_cortex:
1050:  nbb_heteroglobulin_transport:
1063:  nbb_mother_carrie_protocols:
1077:  nbb_pituitary_gland:
1087:  nbb_spiritual_maternal_integration:
1101:  nbb_darwin_godel_machines:
1111:  nbb_blood_brain_barrier:
1121:  nbb_subconscious:
1131:  nbb_qualia_engine:
1141:  neo4j:
1154:  mysql:
1170:  ipfs:
1182:  jarvis-main-brain:
1229:  jarvis-local-resources:
1250:  jarvis-local-resources-db:
1265:  jarvis-gis-rag:
1285:  jarvis-toroidal:
1308:  psychological_rag_domain:
1326:  jarvis-psychology-services:
1348:  jarvis-constitutional-guardian:
1372:  jarvis-judge-truth:
1389:  jarvis-judge-consistency:
1406:  jarvis-judge-alignment:
1423:  jarvis-judge-ethics:
1440:  jarvis-judge-pipeline:
1468:  jarvis-aaacpe-rag:
1494:  jarvis-rag-server:
1518:  jarvis-spiritual-rag:
1542:  jarvis-auth-api:
1566:  jarvis-contracts:
1582:  jarvis-eeg-beta:
1601:  jarvis-eeg-delta:
1620:  jarvis-eeg-theta:
1639:  jarvis-hilbert-state:
1646:    - jarvis_hilbert_state:app
1665:  jarvis-jaeger:
1682:  jarvis-kyc-vault:
1703:  jarvis-phi-probe:
1709:    - ms_jarvis_phi_probe.py
1718:    - /mnt/nvme1/msjarvis-rebuild/services/ms_jarvis_phi_probe.py:/app/ms_jarvis_phi_probe.py:ro
1721:  jarvis-pia-sampler:
1738:  jarvis-provenance:
1758:  jarvis-rag-router:
1780:  jarvis-session-sidecar:
1804:  jarvis-aaacpe-scraper:
1815:  jarvis-commons-gamification:
1833:  jarvis-community-stake-registry:
1849:  jarvis-crypto-policy:
1867:  jarvis-dao-governance:
1883:  jarvis-gbim-benefit-indexer:
1904:  jarvis-gbim-query-router:
1929:  jarvis-hilbert-gateway:
1951:    - /mnt/nvme1/msjarvis-rebuild/services/jarvis_hilbert_semantic.py:/app/services/jarvis_hilbert_semantic.py:ro
1954:    - jarvis_hilbert_semantic:app
1959:  jarvis-hilbert-time:
1966:    - jarvis_hilbert_time:app
1979:    - /mnt/nvme1/msjarvis-rebuild/services/jarvis_hilbert_time.py:/app/services/jarvis_hilbert_time.py:ro
1983:  jarvis-ingest-api:
1993:  jarvis-ingest-watcher:
2019:  jarvis-intake-service:
2046:  jarvis-memory:
2059:  jarvis-steward:
2078:  jarvis-stewardship-scheduler:
2101:  ms-mountainshares-analytics:
2116:  ms-mountainshares-coordinator:
2135:  ms-mountainshares-indexer:
2150:  nbb_i_containers:
2170:  jarvis-dgm-bridge-01:
2183:  jarvis-dgm-bridge-02:
2196:  jarvis-dgm-bridge-03:
2209:  jarvis-dgm-bridge-04:
2222:  jarvis-dgm-bridge-05:
2235:  jarvis-dgm-bridge-06:
2248:  jarvis-dgm-bridge-07:
2261:  jarvis-dgm-bridge-08:
2274:  jarvis-dgm-bridge-09:
2287:  jarvis-dgm-bridge-10:
2300:  jarvis-dgm-bridge-11:
2313:  jarvis-dgm-bridge-12:
2326:  jarvis-dgm-bridge-13:
2339:  jarvis-dgm-bridge-14:
2352:  jarvis-dgm-bridge-15:
2365:  jarvis-dgm-bridge-16:
2378:  jarvis-dgm-bridge-17:
2391:  jarvis-dgm-bridge-18:
2404:  jarvis-dgm-bridge-19:
2417:  jarvis-dgm-bridge-20:
2430:  jarvis-dgm-bridge-21:
2443:  jarvis-dgm-bridge-22:
2456:  jarvis-dgm-bridge-23:
2469:  jarvis-dgm-01:
2484:  jarvis-dgm-02:
2499:  jarvis-dgm-03:
2514:  jarvis-dgm-04:
2529:  jarvis-dgm-05:
2544:  jarvis-dgm-06:
2559:  jarvis-dgm-07:
2574:  jarvis-dgm-08:
2589:  jarvis-dgm-09:
2604:  jarvis-dgm-10:
2619:  jarvis-dgm-11:
2634:  jarvis-dgm-12:
2649:  jarvis-dgm-13:
2664:  jarvis-dgm-14:
2679:  jarvis-dgm-15:
2694:  jarvis-dgm-16:
2709:  jarvis-dgm-17:
2724:  jarvis-dgm-18:
2739:  jarvis-dgm-19:
2754:  jarvis-dgm-20:
2769:  jarvis-dgm-21:
2784:  jarvis-dgm-22:
2799:  jarvis-dgm-23:
2815:  qualia-net:
2817:  hilbert-net:
2820:  chroma_data:
2822:  aaacpe-cultural-data:
2824:  rag_model_cache:
2826:  jarvisapikey:

===== DOCKERFILE ENTRYPOINT DECLARATIONS =====
./Dockerfile.hilbert_spatial_chat:4:COPY services/hilbert_spatial_chat.py .
./Dockerfile.hilbert_spatial_chat:5:CMD ["python", "hilbert_spatial_chat.py"]
./Dockerfile.gis_rag:10:CMD ["uvicorn", "gis_rag_service:app", "--host", "0.0.0.0", "--port", "8004"]
./Dockerfile-llm19-proxy:6:CMD ["uvicorn", "llm19_health_proxy:app", "--host", "0.0.0.0", "--port", "8219"]
./Dockerfile-llm1-proxy:6:CMD ["uvicorn", "llm1_health_proxy:app", "--host", "0.0.0.0", "--port", "8201"]
./Dockerfile.nbb_icontainers_fastapi:22:CMD ["uvicorn", "services.icontainers_fastapi:app", "--host", "0.0.0.0", "--port", "7005"]
./Dockerfile.full_neuro:14:CMD ["uvicorn", "ms_jarvis_full_neurobio_chat:app", "--host", "0.0.0.0", "--port", "8062"]
./Dockerfile.agents:10:CMD ["python", "-m", "services.services.ms_jarvis_agents_service"]
./Dockerfile-llm16-proxy:6:CMD ["uvicorn", "llm16_health_proxy:app", "--host", "0.0.0.0", "--port", "8216"]
./Dockerfile:23:CMD ["python3"]
./Dockerfile-llm17-proxy:6:CMD ["uvicorn", "llm17_health_proxy:app", "--host", "0.0.0.0", "--port", "8217"]
./Dockerfile-llm2-proxy:6:CMD ["uvicorn", "llm2_health_proxy:app", "--host", "0.0.0.0", "--port", "8202"]
./Dockerfile-llm3-proxy:6:CMD ["uvicorn", "llm3_health_proxy:app", "--host", "0.0.0.0", "--port", "8203"]
./integration_layer/Dockerfile:4:CMD ["python3", "__init__.py"]
./services/Dockerfile.lm_synthesizer:15:CMD ["python", "lm_synthesizer.py"]
./services/Dockerfile.pia-sampler:6:CMD ["python3", "jarvis_stewardship_scheduler.py"]
./services/Dockerfile.dgm_orchestrator:6:CMD ["python3", "-m", "uvicorn", "dgm_orchestrator:app", "--host", "0.0.0.0", "--port", "9999"]
./services/Dockerfile.autonomous_learner:23:CMD ["python", "-m", "uvicorn", "ms_jarvis_autonomous_learner:app", "--host", "0.0.0.0", "--port", "8020"]
./services/Dockerfile.roche_llm.disabled:15:CMD ["uvicorn", "roche_llm:app", "--host", "0.0.0.0", "--port", "8008"]
./services/Dockerfile-llm19-proxy:6:CMD ["python", "-m", "uvicorn", "llm19_health_proxy:app", "--host", "0.0.0.0", "--port", "8219"]
./services/Dockerfile-llm1-proxy:6:CMD ["python", "-m", "uvicorn", "llm1_health_proxy:app", "--host", "0.0.0.0", "--port", "8201"]
./services/integration_layer.backup.1768269372/Dockerfile:4:CMD ["python3", "__init__.py"]
./services/Dockerfile.agents:5:CMD ["python3.10", "msjarvis_agents_service.py"]
./services/Dockerfile.hippocampus:15:CMD ["python3", "-m", "uvicorn", "hippocampus_service:app", "--host", "0.0.0.0", "--port", "8011"]
./services/Dockerfile.icontainers_fastapi:12:CMD ["python", "-m", "uvicorn", "icontainers_fastapi:app", "--host", "0.0.0.0", "--port", "8015"]
./services/Dockerfile-llm16-proxy:6:CMD ["python", "-m", "uvicorn", "llm16_health_proxy:app", "--host", "0.0.0.0", "--port", "8216"]
./services/Dockerfile.dgm_worker:8:CMD ["sh", "-c", "python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port ${DGM_PORT:-5100}"]
./services/Dockerfile:21:CMD ["python", "ms_jarvis_consciousness_unified_bridge.py"]
./services/Dockerfile.intake:5:CMD ["uvicorn", "intake_service:app", "--host", "0.0.0.0", "--port", "8007"]
./services/Dockerfile.qualia:38:CMD ["python3", "ms_jarvis_qualia_engine.py"]
./services/Dockerfile-llm17-proxy:6:CMD ["python", "-m", "uvicorn", "llm17_health_proxy:app", "--host", "0.0.0.0", "--port", "8217"]
./services/integration_layer.placeholder_1768012705/Dockerfile:4:CMD ["python3", "__init__.py"]
./services/Dockerfile-llm2-proxy:6:CMD ["python", "-m", "uvicorn", "llm2_health_proxy:app", "--host", "0.0.0.0", "--port", "8202"]
./services/Dockerfile.fifth_dgm_real:19:CMD ["python3", "ms_jarvis_fifth_dgm_orchestrator.py"]
./services/Dockerfile-llm3-proxy:6:CMD ["python", "-m", "uvicorn", "llm3_health_proxy:app", "--host", "0.0.0.0", "--port", "8203"]
./services/integration_layer/Dockerfile:4:CMD ["python3", "__init__.py"]
./services/jarvis_steward/Dockerfile:10:CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8060"]
./services/Dockerfile.web_research:14:CMD ["python", "ms_jarvis_web_research_simple.py"]
./services/Dockerfile.temporal_consciousness:6:CMD ["python", "-m", "uvicorn", "temporal_consciousness:app", "--host", "0.0.0.0", "--port", "7007"]
./services/Dockerfile.memory:6:CMD ["uvicorn", "ms_jarvis_memory_service:app", "--host", "0.0.0.0", "--port", "8056"]
./services/Dockerfile-llm10-proxy:6:CMD ["python", "-m", "uvicorn", "llm10_health_proxy:app", "--host", "0.0.0.0", "--port", "8210"]
./services/Dockerfile-llm8-proxy:6:CMD ["python", "-m", "uvicorn", "llm8_health_proxy:app", "--host", "0.0.0.0", "--port", "8208"]
./services/Dockerfile.mother_protocols:6:CMD ["python", "-m", "uvicorn", "mother_protocols:app", "--host", "0.0.0.0", "--port", "4000"]
./services/Dockerfile.toroidal:21:CMD ["python", "-m", "uvicorn", "toroidal_service:app", "--host", "0.0.0.0", "--port", "8025"]
./services/Dockerfile.aaacpe_rag:18:CMD ["python", "-m", "uvicorn", "aaacpe_rag_service:app", "--host", "0.0.0.0", "--port", "8032"]
./services/Dockerfile.semaphore:16:CMD ["python", "-m", "uvicorn", "msjarvis_semaphore:app", "--host", "0.0.0.0", "--port", "8030"]
./services/Dockerfile-llm4-proxy:6:CMD ["python", "-m", "uvicorn", "llm4_health_proxy:app", "--host", "0.0.0.0", "--port", "8204"]
./services/Dockerfile.rag:15:CMD ["python3", "main_with_rag.py"]
./services/Dockerfile.icontainers:34:CMD ["python3.10", "-m", "uvicorn", "ms_jarvis_i_containers_service:app", "--host", "0.0.0.0", "--port", "8015"]
./services/ai/Dockerfile:5:CMD ["uvicorn","ai_server:app","--host","0.0.0.0","--port","8008"]
./services/Dockerfile.judge:18:CMD ["python", "judge_pipeline.py"]
./services/python/Dockerfile:4:CMD ["python3", "consciousness_bridge.py"]
./services/Dockerfile-llm15-proxy:6:CMD ["python", "-m", "uvicorn", "llm15_health_proxy:app", "--host", "0.0.0.0", "--port", "8215"]
./services/Dockerfile-llm12-proxy:6:CMD ["python", "-m", "uvicorn", "llm12_health_proxy:app", "--host", "0.0.0.0", "--port", "8212"]
./services/Dockerfile.autonomous_complete:18:CMD ["python", "ms_jarvis_autonomous_learner.py"]
./services/Dockerfile.woah:16:CMD ["python3", "ms_jarvis_woah_algorithms.py"]
./services/neurobiologicalbrain/qualia_engine/service/Dockerfile:4:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/qualia_engine/service/Dockerfile.bak_add_flask:4:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/qualia_engine/service/Dockerfile.bak_force_flask:4:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/blood_brain_barrier/service/Dockerfile:4:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/blood_brain_barrier/service/Dockerfile.bak_add_flask:4:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/blood_brain_barrier/service/Dockerfile.bak_force_flask:4:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/spiritual_maternal_integration/service/Dockerfile:9:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/spiritual_maternal_integration/service/Dockerfile.bak_add_flask:8:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/spiritual_maternal_integration/service/Dockerfile.bak_force_flask:8:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/darwin_godel_machines/service/Dockerfile:4:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/darwin_godel_machines/service/Dockerfile.bak_add_flask:4:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/darwin_godel_machines/service/Dockerfile.bak_force_flask:4:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/spiritual_root/service/Dockerfile:9:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/spiritual_root/service/Dockerfile.bak_add_flask:8:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/spiritual_root/service/Dockerfile.bak_force_flask:8:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/subconscious/service/Dockerfile:9:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/subconscious/service/Dockerfile.bak_add_flask:8:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/subconscious/service/Dockerfile.bak_force_flask:8:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/woah_algorithms/service/Dockerfile:9:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/woah_algorithms/service/Dockerfile.bak_add_flask:8:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/woah_algorithms/service/Dockerfile.bak_force_flask:8:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/consciousness_containers/service/Dockerfile:9:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/consciousness_containers/service/Dockerfile.bak_add_flask:8:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/consciousness_containers/service/Dockerfile.bak_force_flask:8:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/pituitary_gland/service/Dockerfile:9:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/pituitary_gland/service/Dockerfile.bak_add_flask:8:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/pituitary_gland/service/Dockerfile.bak_force_flask:8:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/heteroglobulin_transport/service/Dockerfile:9:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/heteroglobulin_transport/service/Dockerfile.bak_add_flask:8:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/heteroglobulin_transport/service/Dockerfile.bak_force_flask:8:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/prefrontal_cortex/service/Dockerfile:9:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/prefrontal_cortex/service/Dockerfile.bak_add_flask:8:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/prefrontal_cortex/service/Dockerfile.bak_force_flask:8:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/neurobiological_brain/qualia_engine/Dockerfile:4:CMD ["python3", "__init__.py"]
./services/neurobiologicalbrain/neurobiological_brain/qualia_engine/meaning_maker/Dockerfile:4:CMD ["python3", "meaning_maker.py"]
./services/neurobiologicalbrain/neurobiological_brain/qualia_engine/emotional_resonance/Dockerfile:4:CMD ["python3", "emotional_resonance.py"]
./services/neurobiologicalbrain/neurobiological_brain/qualia_engine/experience_generator/Dockerfile:4:CMD ["python3", "__init__.py"]
./services/neurobiologicalbrain/neurobiological_brain/Dockerfile:4:CMD ["python3", "__init__.py"]
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile.bak_use_nbb_base:11:ENTRYPOINT ["./entrypoint_with_flask.sh"]
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile.bak_flask_explicit:9:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile.bak_entrypoint:11:CMD ["python3", "bootstrap_with_flask.py"]
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile:6:CMD ["python", "consciousness_bridge.py"]
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile.bak_add_flask:8:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile.bak_bootstrap_cmd2:11:CMD ["python3", "consciousness_bridge.py"]
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile.bak_force_flask:8:CMD ["python3", "consciousness_bridge.py"]
./services/Dockerfile-llm13-proxy:6:CMD ["python", "-m", "uvicorn", "llm13_health_proxy:app", "--host", "0.0.0.0", "--port", "8213"]
./services/Dockerfile-llm6-proxy:6:CMD ["python", "-m", "uvicorn", "llm6_health_proxy:app", "--host", "0.0.0.0", "--port", "8206"]
./services/Dockerfile-llm22-proxy:6:CMD ["python", "-m", "uvicorn", "llm22_health_proxy:app", "--host", "0.0.0.0", "--port", "8222"]
./services/Dockerfile.autonomous_learner_complete:22:CMD ["python", "ms_jarvis_autonomous_learner.py"]
./services/Dockerfile-llm20-proxy:6:CMD ["python", "-m", "uvicorn", "llm20_health_proxy:app", "--host", "0.0.0.0", "--port", "8220"]
./services/Dockerfile-llm21-proxy:6:CMD ["python", "-m", "uvicorn", "llm21_health_proxy:app", "--host", "0.0.0.0", "--port", "8221"]
./services/ai-server/Dockerfile:12:CMD [ "uvicorn", "ai_server:app", "--host", "0.0.0.0", "--port", "8010" ]
./services/Dockerfile.bak_runner_cmd:15:CMD ["python3.10", "msjarvis_woah_algorithms_service.py"]
./services/Dockerfile-chroma-proxy:6:CMD ["python", "-m", "uvicorn", "chroma_health_proxy:app", "--host", "0.0.0.0", "--port", "8081"]
./services/Dockerfile-llm14-proxy:6:CMD ["python", "-m", "uvicorn", "llm14_health_proxy:app", "--host", "0.0.0.0", "--port", "8214"]
./services/Dockerfile.webdeploy:9:CMD ["python3", "ms_jarvis_web_deployer.py"]
./services/Dockerfile-llm7-proxy:6:CMD ["python", "-m", "uvicorn", "llm7_health_proxy:app", "--host", "0.0.0.0", "--port", "8207"]
./services/Dockerfile.constitutional_guardian:15:CMD ["python", "-m", "uvicorn", "constitutional_api:app", "--host", "0.0.0.0", "--port", "8091", "--log-level", "info"]
./services/Dockerfile.bbb:12:CMD ["python", "msjarvis_bbb_proxy.py"]
./services/Dockerfile-llm5-proxy:6:CMD ["python", "-m", "uvicorn", "llm5_health_proxy:app", "--host", "0.0.0.0", "--port", "8205"]
./services/Dockerfile.crypto-policy:5:CMD ["uvicorn", "ms_jarvis_crypto_policy:app", "--host", "0.0.0.0", "--port", "8099"]
./services/Dockerfile-llm11-proxy:6:CMD ["python", "-m", "uvicorn", "llm11_health_proxy:app", "--host", "0.0.0.0", "--port", "8211"]
./services/Dockerfile-llm9-proxy:6:CMD ["python", "-m", "uvicorn", "llm9_health_proxy:app", "--host", "0.0.0.0", "--port", "8209"]
./services/Dockerfile.aaacpe_scraper:18:CMD ["python", "-m", "uvicorn", "aaacpe_scraper_service:app", "--host", "0.0.0.0", "--port", "8033"]
./services/Dockerfile.rag_server:20:CMD ["python3", "rag_server.py"]
./services/Dockerfile.psychological_rag:11:CMD ["python", "psychological_rag_domain.py"]
./services/Dockerfile-llm18-proxy:6:CMD ["python", "-m", "uvicorn", "llm18_health_proxy:app", "--host", "0.0.0.0", "--port", "8218"]
./services/neurobiological_brain/qualia_engine/Dockerfile:4:CMD ["python3", "__init__.py"]
./services/neurobiological_brain/qualia_engine/meaning_maker/Dockerfile:4:CMD ["python3", "meaning_maker.py"]
./services/neurobiological_brain/qualia_engine/emotional_resonance/Dockerfile:4:CMD ["python3", "emotional_resonance.py"]
./services/neurobiological_brain/qualia_engine/experience_generator/Dockerfile:4:CMD ["python3", "__init__.py"]
./services/neurobiological_brain/Dockerfile:4:CMD ["python3", "__init__.py"]
./services/alert_venv/Dockerfile:4:CMD ["python3", "send_alert_slack.py"]
./services/Dockerfile.69dgm_bridge:7:CMD ["python", "-m", "uvicorn", "bridge_69dgm:app", "--host", "0.0.0.0", "--port", "9000"]
./services/Dockerfile.spiritual_rag:6:CMD ["python", "spiritual_rag_domain.py"]
./services/Dockerfile.gateway:5:CMD ["python3.10", "msjarvis_unified_gateway.py"]
./services/Dockerfile.roche_llm:15:CMD ["python", "-m", "uvicorn", "roche_llm:app", "--host", "0.0.0.0", "--port", "8008"]
./services/Dockerfile.woah_algorithms:18:CMD ["python3", "ms_jarvis_woah_algorithms.py"]
./services/Dockerfile.bak_add_deps:15:CMD ["python3.10", "msjarvis_woah_algorithms_service.py"]
./services/Dockerfile.psychology_services:12:CMD ["python", "ms_jarvis_psychology_services.py"]
./services/Dockerfile.email:10:CMD ["python3", "ms_jarvis_email_service.py"]
./Dockerfile.ragservermain:15:CMD ["uvicorn", "ragservermain:app", "--host", "0.0.0.0", "--port", "8003"]
./neurobiologicalbrainmothercarrieprotocolsservice/Dockerfile:14:CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8018"]
./Dockerfile-llm10-proxy:6:CMD ["uvicorn", "llm10_health_proxy:app", "--host", "0.0.0.0", "--port", "8210"]
./Dockerfile-llm8-proxy:6:CMD ["uvicorn", "llm8_health_proxy:app", "--host", "0.0.0.0", "--port", "8208"]
./Dockerfile-llm4-proxy:6:CMD ["uvicorn", "llm4_health_proxy:app", "--host", "0.0.0.0", "--port", "8204"]
./Dockerfile.rag:15:CMD ["python3", "main_with_rag.py"]
./Dockerfile.rag_server_main:21:CMD ["uvicorn", "rag_server:app", "--host", "0.0.0.0", "--port", "8003"]
./ai/Dockerfile:12:CMD ["uvicorn","ai_server:app","--host","0.0.0.0","--port","8001"]
./Dockerfile-llm15-proxy:6:CMD ["uvicorn", "llm15_health_proxy:app", "--host", "0.0.0.0", "--port", "8215"]
./Dockerfile-llm12-proxy:6:CMD ["uvicorn", "llm12_health_proxy:app", "--host", "0.0.0.0", "--port", "8212"]
./Dockerfile.woah:15:CMD ["python3.10", "/app/ms_jarvis_woah_algorithms.py"]
./Dockerfile.neuro:16:CMD ["uvicorn", "services.neuro_master_service:app", "--host", "0.0.0.0", "--port", "8018"]
./Dockerfile-llm13-proxy:6:CMD ["uvicorn", "llm13_health_proxy:app", "--host", "0.0.0.0", "--port", "8213"]
./Dockerfile-llm6-proxy:6:CMD ["uvicorn", "llm6_health_proxy:app", "--host", "0.0.0.0", "--port", "8206"]
./Dockerfile-llm22-proxy:6:CMD ["uvicorn", "llm22_health_proxy:app", "--host", "0.0.0.0", "--port", "8222"]
./Dockerfile-llm20-proxy:6:CMD ["uvicorn", "llm20_health_proxy:app", "--host", "0.0.0.0", "--port", "8220"]
./Dockerfile-llm21-proxy:6:CMD ["uvicorn", "llm21_health_proxy:app", "--host", "0.0.0.0", "--port", "8221"]
./Dockerfile.consciousnessbridge:6:CMD ["uvicorn", "temporal_consciousness:app", "--host", "0.0.0.0", "--port", "7007"]
./ai-server/Dockerfile:5:CMD ["uvicorn","ai_server:app","--host","0.0.0.0","--port","8000"]
./Dockerfile-llm14-proxy:6:CMD ["uvicorn", "llm14_health_proxy:app", "--host", "0.0.0.0", "--port", "8214"]
./Dockerfile.local_resources:10:CMD ["uvicorn", "local_resources_resolver:app", "--host", "0.0.0.0", "--port", "8006"]
./Dockerfile.brain:18:CMD ["uvicorn", "ai_server_22llm:app", "--host", "0.0.0.0", "--port", "8008"]
./Dockerfile-llm7-proxy:6:CMD ["uvicorn", "llm7_health_proxy:app", "--host", "0.0.0.0", "--port", "8207"]
./Dockerfile-llm5-proxy:6:CMD ["uvicorn", "llm5_health_proxy:app", "--host", "0.0.0.0", "--port", "8205"]
./Dockerfile.bak_before_python3_fix:7:COPY gateway-entrypoint.sh /app/gateway-entrypoint.sh
./Dockerfile.bak_before_python3_fix:8:RUN chmod +x /app/gateway-entrypoint.sh
./Dockerfile.bak_before_python3_fix:10:ENTRYPOINT ["/app/gateway-entrypoint.sh"]
./Dockerfile-llm11-proxy:6:CMD ["uvicorn", "llm11_health_proxy:app", "--host", "0.0.0.0", "--port", "8211"]
./Dockerfile-llm9-proxy:6:CMD ["uvicorn", "llm9_health_proxy:app", "--host", "0.0.0.0", "--port", "8209"]
./Dockerfile.rag_server:23:CMD ["python3", "rag_server.py"]
./Dockerfile.20llm:12:CMD ["python3.10", "ai_server_20llm_PRODUCTION.py", "8008"]
./Dockerfile-llm18-proxy:6:CMD ["uvicorn", "llm18_health_proxy:app", "--host", "0.0.0.0", "--port", "8218"]
./neurobiological_brain/qualia_engine/service/Dockerfile:8:CMD ["uvicorn", "ms_jarvis_consciousness_bridge:app", "--host", "0.0.0.0", "--port", "8010"]
./neurobiological_brain/blood_brain_barrier/service/Dockerfile:8:CMD ["uvicorn", "ms_jarvis_consciousness_bridge:app", "--host", "0.0.0.0", "--port", "8010"]
./neurobiological_brain/i_containers/service/Dockerfile.nbb_icontainers_fastapi:18:CMD ["uvicorn", "icontainers_fastapi:app", "--host", "0.0.0.0", "--port", "7005"]
./neurobiological_brain/spiritual_maternal_integration/service/Dockerfile:8:CMD ["python3", "consciousness_bridge.py"]
./neurobiological_brain/darwin_godel_machines/service/Dockerfile:8:CMD ["uvicorn", "ms_jarvis_consciousness_bridge:app", "--host", "0.0.0.0", "--port", "8010"]
./neurobiological_brain/spiritual_root/service/Dockerfile:10:CMD ["python3", "consciousness_bridge.py"]
./neurobiological_brain/subconscious/service/Dockerfile:10:CMD ["python3", "consciousness_bridge.py"]
./neurobiological_brain/woah_algorithms/service/Dockerfile:10:CMD ["python3", "consciousness_bridge.py"]
./neurobiological_brain/consciousness_containers/service/Dockerfile:10:CMD ["python3", "consciousness_bridge.py"]
./neurobiological_brain/heteroglobulin_transport/service/Dockerfile:8:CMD ["python3", "consciousness_bridge.py"]
./neurobiological_brain/neurobiological_brain/qualia_engine/Dockerfile:4:CMD ["python3", "__init__.py"]
./neurobiological_brain/neurobiological_brain/qualia_engine/meaning_maker/Dockerfile:4:Cgrep: ./data/mysql/aaacpe: Permission denied
grep: ./data/mysql/gis_rag: Permission denied
MD ["python3", "meaning_maker.py"]
./neurobiological_brain/neurobiological_brain/qualia_engine/emotional_resonance/Dockerfile:4:CMD ["python3", "emotional_resonance.py"]
./neurobiological_brain/neurobiological_brain/qualia_engine/experience_generator/Dockerfile:4:CMD ["python3", "__init__.py"]
./neurobiological_brain/neurobiological_brain/Dockerfile:4:CMD ["python3", "__init__.py"]
./neurobiological_brain/mother_carrie_protocols/service/Dockerfile:8:CMD ["python3", "consciousness_bridge.py"]
./Dockerfile.swarm:10:CMD ["python", "-m", "services.services.ms_jarvis_swarm_intelligence"]
./Dockerfile.gateway:7:COPY gateway-entrypoint.sh /app/gateway-entrypoint.sh
./Dockerfile.gateway:8:RUN chmod +x /app/gateway-entrypoint.sh
./Dockerfile.gateway:10:ENTRYPOINT ["/app/gateway-entrypoint.sh"]
grep: ./data/mysql-recovery-copy/aaacpe: Permission denied
grep: ./data/mysql-recovery-copy/gis_rag: Permission denied
grep: ./data/local_resources: Permission denied

===== SCRIPT / SERVICE LAUNCH REFERENCES =====
grep: ./data/mysql/aaacpe./services/start_hilbert_8235.sh:3:nohup python3 hilbert_spatial_chat.py --port 8235 > hilbert_8235.log 2>&1 &
./docker-compose.override.yml:24:      dockerfile: Dockerfile.hilbert_spatial_chat
./docker-compose.yml:1646:    - jarvis_hilbert_state:app
./docker-compose.yml:1709:    - ms_jarvis_phi_probe.py
./docker-compose.yml:1718:    - /mnt/nvme1/msjarvis-rebuild/services/ms_jarvis_phi_probe.py:/app/ms_jarvis_phi_probe.py:ro
./docker-compose.yml:1951:    - /mnt/nvme1/msjarvis-rebuild/services/jarvis_hilbert_semantic.py:/app/services/jarvis_hilbert_semantic.py:ro
./docker-compose.yml:1954:    - jarvis_hilbert_semantic:app
./docker-compose.yml:1966:    - jarvis_hilbert_time:app
./docker-compose.yml:1979:    - /mnt/nvme1/msjarvis-rebuild/services/jarvis_hilbert_time.py:/app/services/jarvis_hilbert_time.py:ro
: Permission denied
grep: ./data/mysql/gis_rag: Permission denied
grep: ./data/mysql-recovery-copy/aaacpe: Permission denied
grep: ./data/mysql-recovery-copy/gis_rag: Permission denied
grep: ./data/local_resources: Permission denied

===== HTTP URL REFERENCES =====
services/safe_integration.py:31:                    "http://localhost:7012/evaluate",
services/safe_integration.py:44:                    "http://localhost:8018/analyze",
services/JARVIS_HEALTH_CHECK.sh:17:if curl -s http://localhost:8004/health >/dev/null 2>&1; then
services/JARVIS_HEALTH_CHECK.sh:25:STATUS=$(curl -s http://localhost:8020/health 2>/dev/null)
services/system_dashboard.py:33:    "LLM Bridge": "http://localhost:8002",
services/system_dashboard.py:34:    "Consensus Layer": "http://localhost:9001",
services/system_dashboard.py:35:    "Egeria Web UI": "http://localhost:8051",
services/system_dashboard.py:36:    "Facebook Service": "http://localhost:8093",
services/system_dashboard.py:37:    "Fifth DGM": "http://localhost:4002",
services/system_dashboard.py:38:    "Brain Orchestrator": "http://localhost:4000",
services/system_dashboard.py:40:    "Swarm Intelligence": "http://localhost:8021",
services/system_dashboard.py:41:    "Integration Hub": "http://localhost:9100",
services/mesh_agent_batch.sh:4:  curl -s -X POST http://localhost:42015/embed_interaction     -H "Content-Type: application/json"     -d "{\"ueid\":\"$u\",\"message\":\"Boot entry $i\",\"response\":\"Mesh online\",\"emotion\":\"ready\",\"importance\":0.5,\"tags\":[\"mesh\",\"batch\"]}" > /dev/null
services/mesh_topn_context.sh:7:  matches=$(curl -s -X POST http://localhost:42015/recall_memory -H "Content-Type: application/json" -d "{\"ueid\":\"$u\",\"query\":\"$QUERY\",\"top_k\":3}" | jq '.semantic_matches | length')
services/mesh_memory_dashboard.sh:8:    curl -s -X POST "http://localhost:42015/get_user_context?ueid=$u"
services/mesh_memory_dashboard.sh:12:  curl -s http://localhost:42015/health
services/port_9001_ui_MYSQL_PROD.py:173:            r = await client.post(f"http://localhost:4022/consciousness/chat?userid=user&message={message}", timeout=10.0)
services/integrate_full_brain.py:20:        self.neuro_url = "http://localhost:8018"
services/integrate_full_brain.py:21:        self.containers_url = "http://localhost:8015"
services/ms_jarvis_facebook_async.py:69:                    "http://localhost:4027/generate_facebook_post",
services/START_COMPLETE_SYSTEM.sh:24:if curl -s http://localhost:8004/health &>/dev/null; then
services/START_COMPLETE_SYSTEM.sh:33:if curl -s http://localhost:8020/health &>/dev/null; then
services/START_COMPLETE_SYSTEM.sh:53:curl -s http://localhost:8030/health | python3 -m json.tool
services/START_COMPLETE_SYSTEM.sh:66:echo "  curl -X POST http://localhost:8030/chat \\"
services/mesh_scenario_drill.sh:7:    curl -s -X POST http://localhost:42015/embed_interaction -H "Content-Type: application/json" \
services/CREATE_ULTIMATE_JARVIS.sh:53:    "brain_orchestrator": "http://localhost:4001",
services/CREATE_ULTIMATE_JARVIS.sh:54:    "dgm_fifth_identity": "http://localhost:4002",
services/CREATE_ULTIMATE_JARVIS.sh:57:    "qualia_engine": "http://localhost:8017",
services/CREATE_ULTIMATE_JARVIS.sh:58:    "fast_mode": "http://localhost:8020",
services/CREATE_ULTIMATE_JARVIS.sh:59:    "blood_brain_barrier": "http://localhost:8016",
services/CREATE_ULTIMATE_JARVIS.sh:60:    "neurobiological_master": "http://localhost:8018",
services/CREATE_ULTIMATE_JARVIS.sh:63:    "deep_mode_19llm": "http://localhost:8004",
services/CREATE_ULTIMATE_JARVIS.sh:64:    "conscious_collective": "http://localhost:8050",
services/CREATE_ULTIMATE_JARVIS.sh:65:    "ai_server_base": "http://localhost:8010",
services/CREATE_ULTIMATE_JARVIS.sh:67:    "agents_service": "http://localhost:8005",
services/CREATE_ULTIMATE_JARVIS.sh:68:    "autonomous_learner": "http://localhost:8009",
services/CREATE_ULTIMATE_JARVIS.sh:69:    "emotional_intelligence": "http://localhost:8002",
services/CREATE_ULTIMATE_JARVIS.sh:72:    "web_research": "http://localhost:8008",
services/CREATE_ULTIMATE_JARVIS.sh:73:    "woah_algorithms": "http://localhost:7012",
services/CREATE_ULTIMATE_JARVIS.sh:74:    "swarm_intelligence": "http://localhost:8021",
services/CREATE_ULTIMATE_JARVIS.sh:75:    "i_containers": "http://localhost:8015",
services/CREATE_ULTIMATE_JARVIS.sh:79:    "llm_bridge": "http://localhost:8006",
services/CREATE_ULTIMATE_JARVIS.sh:80:    "coordinator": "http://localhost:8030",
services/CREATE_ULTIMATE_JARVIS.sh:81:    "integration_hub": "http://localhost:9100",
services/CREATE_ULTIMATE_JARVIS.sh:144:                    "http://localhost:8050/chat",
services/CREATE_ULTIMATE_JARVIS.sh:258:curl -s http://localhost:8888/health | python3 -m json.tool
services/CREATE_ULTIMATE_JARVIS.sh:269:echo "  curl -X POST http://localhost:8888/chat \\"
services/CREATE_ULTIMATE_JARVIS.sh:274:echo "Check status: curl -s http://localhost:8888/health | python3 -m json.tool"
services/enrich_geodb_layers.py:15:    "postgresql://postgres:postgres@localhost:5432/msjarvis_gis",
services/enrich_geodb_layers.py:19:NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
services/hilbert_spatial_chat.py:142:NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
services/hilbert_spatial_chat.py:361:                "http://localhost:4001/consensus",
services/ms_jarvis_unified_gateway_v4.3.pre_manifest.backup.py:406:        resp = requests.get("http://localhost:8091/constitutional/status", timeout=5)
services/ms_jarvis_unified_gateway_v4.3.pre_manifest.backup.py:415:        resp = requests.get("http://localhost:8091/constitutional/principles", timeout=5)
services/ms_jarvis_unified_gateway_v4.3.pre_manifest.backup.py:424:        resp = requests.get("http://localhost:8091/constitutional/audit", timeout=5)
services/ms_jarvis_unified_gateway_v4.3.pre_manifest.backup.py:433:        resp = requests.get("http://localhost:8091/constitutional/transparency", timeout=5)
services/ms_jarvis_unified_gateway_v4.3.pre_manifest.backup.py:461:            "constitutional": "http://localhost:8091/constitutional/docs"
services/comprehensive_url_fix.py:20:    if 'localhost:8004' in line or '127.0.0.1:8004' in line:
services/comprehensive_url_fix.py:21:        line = re.sub(r'localhost:8004', 'jarvis-web-research:8004', line)
services/comprehensive_url_fix.py:27:    if 'localhost:8004' in line or '127.0.0.1:8010' in line:
services/comprehensive_url_fix.py:28:        line = re.sub(r'localhost:8004', 'jarvis-chroma:8010', line)
services/comprehensive_url_fix.py:34:    if 'localhost:8015' in line or '127.0.0.1:8015' in line:
services/comprehensive_url_fix.py:35:        line = re.sub(r'localhost:8015', 'jarvis-i-containers:8015', line)
services/comprehensive_url_fix.py:41:    if 'localhost:4002' in line or '127.0.0.1:4002' in line:
services/comprehensive_url_fix.py:42:        line = re.sub(r'localhost:4002', 'jarvis-fifth-dgm:4002', line)
services/watch_startup.sh:35:HEALTH=$(curl -s http://localhost:8004/health 2>/dev/null)
services/ms_jarvis_generate_frontend.py:9:api_resp = requests.post("http://localhost:11434/api/generate", json={"model":"llama3","prompt":prompt,"stream":False})
services/web_connectivity_analyzer.py:154:        print(f"   1. LOCAL ACCESS: Already working - use http://localhost:8051")
services/talk.sh:11:curl -s -X POST http://localhost:8050/chat \
services/port_9001_ARCHITECTURE_CORRECT.py:31:                f"http://localhost:4022/consciousness/chat?userid={userid}&message={message}",
services/RESTORE_ALL_INTEGRATIONS.sh:40:curl -s http://localhost:8050/health | python3 -m json.tool
services/test_all_models.sh:7:    curl -s http://localhost:11434/api/generate \
services/qualia_unified_write_orchestrator_69dgm.py:144:                "http://localhost:8100/deploy",
services/qualia_unified_write_orchestrator_69dgm.py:179:                "http://localhost:8045/deploy",
services/SWITCH_TO_22LLM_DEFAULT.sh:85:    if curl -s http://localhost:8004/health > /dev/null 2>&1; then
services/SWITCH_TO_22LLM_DEFAULT.sh:119:curl -s http://localhost:8004/health | python3 -m json.tool
services/SWITCH_TO_22LLM_DEFAULT.sh:123:curl -s http://localhost:8020/health | python3 -m json.tool 2>/dev/null || echo "Still starting..."
services/SWITCH_TO_22LLM_DEFAULT.sh:130:echo "║    Primary:  http://localhost:8004 (22-LLM Collective)        ║"
services/SWITCH_TO_22LLM_DEFAULT.sh:131:echo "║    Backup:   http://localhost:8020 (4-Agent System)           ║"
services/SWITCH_TO_22LLM_DEFAULT.sh:139:echo '  curl -X POST http://localhost:8004/chat -H "Content-Type: application/json" -d '"'"'{"message":"Hello!","user_id":"test"}'"'"
services/ms_jarvis_integration_hub.py:47:        self.dgm_url = "http://localhost:4001"   # Brain Orchestrator
services/ms_jarvis_integration_hub.py:48:        self.qualia_url = "http://localhost:8017"  # Qualia Engine
services/ms_jarvis_integration_hub.py:49:        self.swarm_url = "http://localhost:8021"   # Swarm Intelligence
services/ms_jarvis_command_orchestrator_v5.0_preachy.py:207:            "http://localhost:11434/api/generate",
services/quantum_state_engine.py:15:BELIEF_SERVICE_URL = "http://localhost:7240/beliefs/recent"
services/quantum_state_engine.py:16:DGM_RECENT_URL = "http://localhost:8010/dgm/recent"
services/ms_jarvis_facebook_dgm_woah.psychology_patched.py:275:                "http://localhost:8016/filter",
services/ms_jarvis_facebook_dgm_woah.psychology_patched.py:292:                "http://localhost:7003/optimize",
services/ms_jarvis_facebook_dgm_woah.psychology_patched.py:325:        bbb_response = requests.get("http://localhost:8016/health", timeout=2)
services/ms_jarvis_facebook_dgm_woah.psychology_patched.py:331:        dgm_response = requests.get("http://localhost:7003/health", timeout=2)
services/consciousness_feed_integration.psychology_patched.py:18:                f"http://localhost:8071/read_feed?feed_url={feed_url}"
services/FIX_ULTIMATE.sh:16:curl -s http://localhost:8050/health | python3 -m json.tool
services/FIX_ULTIMATE.sh:21:echo "curl -X POST http://localhost:8888/chat \\"
services/mesh_crossagent_memory_search.sh:6:  matches=$(curl -s -X POST http://localhost:42015/recall_memory -H "Content-Type: application/json" -d "{\"ueid\":\"$u\",\"query\":\"$PATTERN\",\"top_k\":3}" | jq '.semantic_matches')
services/ms_jarvis_main_gateway.backup_1762220815.py:243:    r = requests.post("http://localhost:8063/messenger/session", params={"user_id": user_id, "research_topic": research_topic}, timeout=10)
services/ms_jarvis_main_gateway.backup_1762220815.py:249:    r = requests.post("http://localhost:8063/messenger/send", params={"session_id": session_id, "user_id": user_id, "message": message}, timeout=30)
services/ms_jarvis_main_gateway.backup_1762220815.py:255:    r = requests.get(f"http://localhost:8063/messenger/history/{session_id}", timeout=10)
services/ms_jarvis_main_gateway.backup_1762220815.py:267:        r = requests.post("http://localhost:8063/messenger/session", 
services/ms_jarvis_main_gateway.backup_1762220815.py:279:        r = requests.post("http://localhost:8063/messenger/send",
services/ms_jarvis_main_gateway.backup_1762220815.py:291:        r = requests.get(f"http://localhost:8063/messenger/history/{session_id}", timeout=10)
services/ms_jarvis_main_gateway.backup_1762220815.py:306:        r = requests.get("http://localhost:8065/registration", timeout=10)
services/ms_jarvis_main_gateway.backup_1762220815.py:327:        r = requests.post("http://localhost:8065/api/register",
services/ms_jarvis_main_gateway.backup_1762220815.py:350:        r = requests.get(f"http://localhost:8065/verify/{ueid}", timeout=10)
services/ms_jarvis_main_gateway.backup_1762220815.py:374:        r = requests.post("http://localhost:8065/api/register",
services/ms_jarvis_main_gateway.backup_1762220815.py:411:        r = requests.post("http://localhost:8044/register/stage1",
services/ms_jarvis_main_gateway.backup_1762220815.py:444:        r = requests.post("http://localhost:8044/register/stage2",
services/start_dgm_woah.sh:14:if curl -s http://localhost:9003/health >/dev/null 2>&1; then
services/start_dgm_woah.sh:25:    if curl -s http://localhost:9003/health >/dev/null 2>&1; then
services/prod.yaml:2:database_url: "postgresql://user:password@localhost:5432/db"
services/ms_jarvis_memory_service.py:14:MEMORY_DGM_URL = "http://localhost:7007"
services/egeria_autonomous_inquiry.py:21:        self.exec_port = "http://localhost:8053/execute"
services/unified_consciousness_gateway_PRODUCTION.py:40:            f"http://localhost:8010/api/v1/collections/{collection_id}/query",
services/unified_consciousness_gateway_PRODUCTION.py:61:                "http://localhost:4001/consensus",
services/swagger_gateway.py:27:    "chromadb": {"url": "http://localhost:8004", "prefix": "/chromadb"},
services/swagger_gateway.py:28:    "qualia": {"url": "http://localhost:8017", "prefix": "/qualia"},
services/ms_jarvis_unified_gateway_v4.3.py:18:REDIS_URL = os.environ.get("JARVIS_REDIS_URL", "redis://localhost:6379/0")
services/ms_jarvis_unified_gateway_v4.3.py:57:        er = requests.get("http://localhost:9000/status/egeria", timeout=5)
services/ms_jarvis_unified_gateway_v4.3.py:124:        resp = requests.get("http://localhost:11434/api/tags", timeout=2)
services/ms_jarvis_unified_gateway_v4.3.py:141:        resp = requests.get("http://localhost:8010/health", timeout=2)
services/ms_jarvis_unified_gateway_v4.3.py:165:        resp = requests.get("http://localhost:8051/health", timeout=2)
services/ms_jarvis_unified_gateway_v4.3.py:174:        resp = requests.get("http://localhost:3000/", timeout=2)
services/ms_jarvis_unified_gateway_v4.3.py:184:        resp = requests.get("http://localhost:8100/health", timeout=2)
services/ms_jarvis_unified_gateway_v4.3.py:193:        resp = requests.get("http://localhost:8014/health", timeout=2)
services/ms_jarvis_unified_gateway_v4.3.py:231:            "http://localhost:43277/chat",
services/port_9001_FINAL_FIX.py:54:            r = await client.post(f"http://localhost:4022/consciousness/chat?userid=user&message={message}", timeout=10.0)
services/restart_and_verify_8008.sh:19:curl -s 'http://localhost:8008/api/v2/heartbeat'
services/agent_llm_batch.sh:7:curl -s -X POST http://localhost:42015/recall_memory -H "Content-Type: application/json" \
services/agent_llm_batch.sh:11:curl -s -X POST http://localhost:42015/embed_interaction -H "Content-Type: application/json" \
services/agent_llm_batch.sh:15:curl -s -X POST "http://localhost:42015/get_user_context?ueid=$AGENT_ID"
services/consciousness_gateway.py:27:    "http://localhost:40013",
services/TEST_IMPROVED_RESPONSE.sh:16:curl -X POST http://localhost:8004/chat \
services/port_9001_FINAL_WORKING.py:185:            r = await client.post(f"http://localhost:4022/consciousness/chat?userid=user&message={message}", timeout=10.0)
services/TEST_CRITICAL_FIXES.sh:3:API_URL="http://localhost:8004/chat"
services/ms_jarvis_facebook_CONSCIOUSNESS.py:81:            resp = await client.get("http://localhost:7001/health")
services/ms_jarvis_facebook_CONSCIOUSNESS.py:162:                "http://localhost:7001/rag/query",
services/ms_jarvis_facebook_CONSCIOUSNESS.py:201:                "http://localhost:7007/optimize",
services/ms_jarvis_facebook_CONSCIOUSNESS.py:218:                "http://localhost:7008/decide",
services/ms_jarvis_consciousness_unified_bridge.py:54:                await client.get("http://localhost:4025/health", headers=headers)
services/neuro_adapter.py:18:            "http://localhost:8018/process",
services/test_method_tracking.py:10:TRACKING_URL = "http://localhost:8200"
services/LOAD_AAACPE_RAG.sh:122:curl -s http://localhost:8004/health | python3 -c "
services/ms_jarvis_facebook_poster_FIXED.py:18:CONSCIOUSNESS_API = "http://localhost:4020/full_consciousness"
services/fix_chat_api.sh:20:    resp = requests.post("http://localhost:8060", json={"message": user_msg})
services/ai_server_11llm_OPTIMIZED.py:235:    "autonomous_learner": "http://localhost:8555",
services/ai_server_11llm_OPTIMIZED.py:236:    "web_research": "http://localhost:8009",
services/ai_server_11llm_OPTIMIZED.py:237:    "llm20_production": "http://localhost:8004",  # 22-LLM collective
services/ai_server_11llm_OPTIMIZED.py:238:    "chroma": "http://localhost:8018",
services/ai_server_11llm_OPTIMIZED.py:239:    "ollama": "http://localhost:11434",
services/setup_frontend.sh:160:echo "Frontend will be available at: http://localhost:5173"
services/jarvis_hilbert_state.py:4:Serves both jarvis-hilbert-state (port 8081) and jarvis-hilbert-gateway (port 8081).
services/jarvis_hilbert_state.py:14:logger = logging.getLogger("hilbert_state")
services/jarvis_hilbert_state.py:20:HILBERT_TIME_URL = os.getenv("HILBERT_TIME_URL", "http://jarvis-hilbert-time:8092")
services/jarvis_hilbert_state.py:55:            f"{HILBERT_TIME_URL}/timeline/register-json",
services/jarvis_hilbert_state.py:93:        "service": "jarvis_hilbert_state",
services/geo/api.py:27:GEODB_DSN = "postgresql://postgres:postgres@localhost:5432/msjarvis_gis"
services/geo/api.py:76:GEODB_DSN = "postgresql://postgres:postgres@localhost:5432/msjarvis_gis"
services/geo/api.py:129:GEODB_DSN = "postgresql://postgres:postgres@localhost:5432/msjarvis_gis"
services/geo/neo4j_client.py:3:NEO4J_URI = "bolt://localhost:7687"
services/geo/similarity.py:4:NEO4J_URI = "bolt://localhost:7687"
services/mesh_explore_chain.sh:4:curl -s -X POST http://localhost:42015/embed_interaction -H "Content-Type: application/json" \
services/mesh_explore_chain.sh:10:  curl -s -X POST http://localhost:42015/embed_interaction -H "Content-Type: application/json" \
services/integrate_phase4_5.sh:109:curl -s http://localhost:8050/health | python3 -m json.tool
services/connect_holy_spirit_to_existing_email.sh:20:        self.email_service_url = "http://localhost:8040"
services/talk_safely_FIXED.sh:50:curl -X POST http://localhost:8050/chat \
services/talk_safely_FIXED.sh:81:    print("Health: curl -s http://localhost:8050/health")
services/port_9001_ui_DIRECT.py:121:                f"http://localhost:4022/consciousness/chat?userid={userid}&message={message}",
services/create_adapter_wrappers.sh:23:            "http://localhost:8017/process",
services/create_adapter_wrappers.sh:49:            "http://localhost:8027/analyze",
services/create_adapter_wrappers.sh:77:            "http://localhost:8018/process",
services/create_adapter_wrappers.sh:108:curl -s -X POST http://localhost:8117/generate -H "Content-Type: application/json" -d '{"content":"test"}' | head -20
services/create_adapter_wrappers.sh:109:curl -s -X POST http://localhost:8127/process -H "Content-Type: application/json" -d '{"messages":["test"]}' | head -20
services/final_synthesis_fix.sh:75:echo "Test at http://localhost:8051"
services/qualia_email_registration_orchestrator_69dgm.py:186:                "http://localhost:8040/send",
services/qualia_email_registration_orchestrator_69dgm.py:248:                "http://localhost:4200/register/stage1",
services/qualia_email_registration_orchestrator_69dgm.py:291:                "http://localhost:4200/register/stage2-biometric",
services/ms_jarvis_conversational_chat.py:51:                <pre>curl -X POST "http://localhost:9002/chat" \\
services/ms_jarvis_conversational_chat.py:58:                <pre>fetch('http://localhost:9002/chat', {
services/ultimate_msjarvis_audit.sh:116:curl -s http://localhost:11434/api/tags 2>/dev/null | python3 << 'PYEOF'
services/ultimate_msjarvis_audit.sh:208:curl -s http://localhost:4002/identity 2>/dev/null | python3 << 'PYEOF'
services/.venv/lib/python3.12/site-packages/pip/_vendor/urllib3/exceptions.py:293:        # localhost:8080 -> scheme=localhost, remove if we fix this.
services/.venv/lib/python3.12/site-packages/pip/_vendor/urllib3/poolmanager.py:468:        >>> proxy = urllib3.ProxyManager('http://localhost:3128/')
services/.venv/lib/python3.12/site-packages/urllib3/exceptions.py:310:        # localhost:8080 -> scheme=localhost, remove if we fix this.
services/.venv/lib/python3.12/site-packages/urllib3/poolmanager.py:545:        proxy = urllib3.ProxyManager("https://localhost:3128/")
services/.venv/lib/python3.12/site-packages/httpcore/_models.py:209:    at `http://localhost:8080`...
services/.venv/lib64/python3.12/site-packages/pip/_vendor/urllib3/exceptions.py:293:        # localhost:8080 -> scheme=localhost, remove if we fix this.
services/.venv/lib64/python3.12/site-packages/pip/_vendor/urllib3/poolmanager.py:468:        >>> proxy = urllib3.ProxyManager('http://localhost:3128/')
services/.venv/lib64/python3.12/site-packages/urllib3/exceptions.py:310:        # localhost:8080 -> scheme=localhost, remove if we fix this.
services/.venv/lib64/python3.12/site-packages/urllib3/poolmanager.py:545:        proxy = urllib3.ProxyManager("https://localhost:3128/")
services/.venv/lib64/python3.12/site-packages/httpcore/_models.py:209:    at `http://localhost:8080`...
services/master_unified_consciousness_scheduler_ENRICHED.py:76:                resp1 = await client.get("http://localhost:4021/health")
services/master_unified_consciousness_scheduler_ENRICHED.py:77:                resp2 = await client.get("http://localhost:4001/health")
services/master_unified_consciousness_scheduler_ENRICHED.py:95:                    "http://localhost:4021/consciousness",
services/method_tracker_decorator.py:12:TRACKING_SERVICE_URL = "http://localhost:8200"
services/ms_jarvis_unified_rag_bridge.py:267:                "endpoint": "http://localhost:8092/query",
services/UPDATE_NAME_TO_EGERIA.sh:27:curl -s http://localhost:8050/health | python3 -m json.tool
services/port_9000_69dgm_bridge.py:84:# Core routing function: call the 69-DGM orchestrator on localhost:9999
services/port_9000_69dgm_bridge.py:93:    Orchestrator is expected to be listening on localhost:9999/process.
services/port_9000_69dgm_bridge.py:100:                "http://localhost:9999/process",  # Orchestrator's processing endpoint
services/trigger_entangled_assets.py:8:    response = requests.get("http://localhost:8022/search_gbim_by_quantum_tag/", params={"tag": "entangled"})
services/ms_jarvis_facebook_dgm_woah.py:275:                "http://localhost:8016/filter",
services/ms_jarvis_facebook_dgm_woah.py:292:                "http://localhost:7003/optimize",
services/ms_jarvis_facebook_dgm_woah.py:325:        bbb_response = requests.get("http://localhost:8016/health", timeout=2)
services/ms_jarvis_facebook_dgm_woah.py:331:        dgm_response = requests.get("http://localhost:7003/health", timeout=2)
services/fix_404_endpoints.sh:83:curl -s -X POST http://localhost:8017/process -H "Content-Type: application/json" -d '{"input":"test"}' | head -20
services/fix_404_endpoints.sh:84:curl -s -X POST http://localhost:8017/qualia -H "Content-Type: application/json" -d '{"input":"test"}' | head -20
services/fix_404_endpoints.sh:88:curl -s -X POST http://localhost:8027/fractal -H "Content-Type: application/json" -d '{"input":"test"}' | head -20
services/fix_404_endpoints.sh:92:curl -s -X POST http://localhost:8018/process -H "Content-Type: application/json" -d '{"input":"test"}' | head -20
services/fix_404_endpoints.sh:96:curl -s -X POST http://localhost:4002/filter -H "Content-Type: application/json" -d '{"input":"test"}' | head -20
services/fix_404_endpoints.sh:97:curl -s -X POST http://localhost:4002/evaluate -H "Content-Type: application/json" -d '{"input":"test"}' | head -20
services/CLEANUP_OLLAMA.sh:20:        curl -s http://localhost:11434/api/generate -d "{\"model\": \"$model\", \"keep_alive\": 0}" > /dev/null
services/complete_system_audit.py:134:        response = requests.get("http://localhost:4012/dgm_swarm_status", timeout=5)
services/complete_system_audit.py:146:        response = requests.get("http://localhost:4011/health", timeout=5)
services/UPDATE_COORDINATOR_FOR_DEEP_MODE.sh:42:        self.fast_mode_url = "http://localhost:8020/chat"  # 4-Agent Bridge
services/UPDATE_COORDINATOR_FOR_DEEP_MODE.sh:43:        self.deep_mode_url = "http://localhost:8004/chat"  # 19-LLM Collective
services/UPDATE_COORDINATOR_FOR_DEEP_MODE.sh:155:            fast_resp = await client.get("http://localhost:8020/health")
services/UPDATE_COORDINATOR_FOR_DEEP_MODE.sh:162:            deep_resp = await client.get("http://localhost:8004/health")
services/UPDATE_COORDINATOR_FOR_DEEP_MODE.sh:224:if curl -s http://localhost:8004/health &>/dev/null; then
services/UPDATE_COORDINATOR_FOR_DEEP_MODE.sh:233:if curl -s http://localhost:8020/health &>/dev/null; then
services/UPDATE_COORDINATOR_FOR_DEEP_MODE.sh:253:curl -s http://localhost:8030/health | python3 -m json.tool
services/UPDATE_COORDINATOR_FOR_DEEP_MODE.sh:266:echo "  curl -X POST http://localhost:8030/chat \\"
services/load_geodb_health_providers_to_neo4j.py:12:NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
services/leak_test.sh:7:    response=$(curl -X POST http://localhost:8004/chat \
services/integrate_advanced_modules.sh:84:echo "✅ Advanced Dashboard running on http://localhost:5000"
services/ms_jarvis_unified_gateway_v4.3.20251124.py:465:            "http://localhost:8091/constitutional/status",
services/ms_jarvis_unified_gateway_v4.3.20251124.py:477:            "http://localhost:8091/constitutional/principles",
services/ms_jarvis_unified_gateway_v4.3.20251124.py:489:            "http://localhost:8091/constitutional/audit",
services/ms_jarvis_unified_gateway_v4.3.20251124.py:501:            "http://localhost:8091/constitutional/transparency",
services/test_agi_capabilities.sh:10:API="http://localhost:8050/chat"
services/final_cleanup_integration.sh:113:curl -s http://localhost:8050/health | python3 -m json.tool
services/gateway_mesh_context.sh:4:curl -s -X POST "http://localhost:42015/get_user_context?ueid=$AGENT_U"
services/gateway_mesh_context.sh:5:curl -s -X POST http://localhost:42015/recall_memory -H "Content-Type: application/json" -d "{\"ueid\":\"$AGENT_U\",\"query\":\"$QUERY_TXT\",\"top_k\":5}"
services/implement_conversation_fixes.sh:145:            i_container_resp = await httpx.AsyncClient().get("http://localhost:4002/i_container")
services/implement_conversation_fixes.sh:248:curl -s -X POST http://localhost:8020/chat \
services/mesh_feed_back_insight.sh:3:curl -s -X POST http://localhost:42015/embed_interaction -H "Content-Type: application/json" \
services/ms_jarvis_main_gateway.py:106:        resp = requests.post("http://localhost:8051/query", json={"query": query}, timeout=10)
services/ms_jarvis_main_gateway.py:179:        resp = requests.post("http://localhost:7012/supervise", json={"action": action}, timeout=10)
services/ms_jarvis_main_gateway.py:187:        resp = requests.post("http://localhost:7003/activate", json={"params": params}, timeout=10)
services/ms_jarvis_main_gateway.py:200:        resp = requests.post("http://localhost:8010/chat", json={"message": message}, timeout=10)
services/ms_jarvis_main_gateway.py:230:        resp = requests.post("http://localhost:8053/post", json={"content": content, "ueid": ueid}, timeout=10)
services/ms_jarvis_main_gateway.py:238:        resp = requests.get(f"http://localhost:8009/search?q={q}", timeout=10)
services/ms_jarvis_main_gateway.py:260:        resp = requests.get(f"http://localhost:8014/gis?location={location}", timeout=10)
services/ms_jarvis_main_gateway.py:268:        resp = requests.post("http://localhost:8016/filter", json={"text": text}, timeout=10)
services/ms_jarvis_main_gateway.py:277:        resp = requests.post("http://localhost:8021/swarm", json={"query": query}, timeout=10)
services/gateway_messenger_integration.py:18:MESSENGER_BASE = "http://localhost:8063"
services/ms_jarvis_facebook_DGM.py:95:                response = await client.post("http://localhost:8092/query", json={"query": topic})
services/ms_jarvis_facebook_DGM.py:129:                    "http://localhost:7012/process",
services/OPTIMIZE_GPU.sh:52:curl -s http://localhost:8050/health | python3 -m json.tool
services/verify_facebook_deployment.sh:8:if curl -s --max-time 3 "http://localhost:4018/health" >/dev/null; then
services/launch_dashboard_background.sh:29:    echo "   URL: http://localhost:5000"
services/launch_dashboard_background.sh:33:    echo "   firefox http://localhost:5000 &"
services/ms_jarvis_consciousness_complete.py:22:UEID_URL = "http://localhost:4030"
services/ms_jarvis_consciousness_complete.py:23:UEID_WALLET_URL = "http://localhost:4031"
services/ms_jarvis_consciousness_complete.py:24:CHROMADB_URL = "http://localhost:8002"
services/ms_jarvis_consciousness_complete.py:25:CHROMADB_QUERY_URL = "http://localhost:4070"
services/ms_jarvis_consciousness_complete.py:28:CONSCIOUSNESS_URL = "http://localhost:4020"
services/ms_jarvis_consciousness_complete.py:29:GEO_URL = "http://localhost:4032"
services/ms_jarvis_consciousness_complete.py:30:FACT_FILTER_URL = "http://localhost:4060"
services/START_20LLM_FINAL.sh:24:curl -s http://localhost:8004/health | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'Status: {d.get(\"status\")} - {d.get(\"models\", 0)} models')"
services/final_validation_test.sh:18:    response=$(curl -X POST http://localhost:8004/chat \
services/mesh_trend_detection.sh:6:  curl -s -X POST http://localhost:42015/embed_interaction -H "Content-Type: application/json" \
services/FINAL_8_LAYER_STARTUP.sh:63:echo "Layer 1 (Qualia 4007): $(curl -s http://localhost:4007/health 2>/dev/null | jq -r '.status // "OFFLINE"')"
services/FINAL_8_LAYER_STARTUP.sh:64:echo "Layer 2 (Mother 4003): $(curl -s http://localhost:4003/health 2>/dev/null | jq -r '.status // "OFFLINE"')"
services/FINAL_8_LAYER_STARTUP.sh:65:echo "Layer 3 (RAG 4011): $(curl -s http://localhost:4011/health 2>/dev/null | jq -r '.service // "OFFLINE"')"
services/FINAL_8_LAYER_STARTUP.sh:66:echo "Layer 4 (Consensus 4010): $(curl -s http://localhost:4010/health 2>/dev/null | jq -r '.service // "OFFLINE"')"
services/FINAL_8_LAYER_STARTUP.sh:67:echo "Layer 5 (Fifth 4005): $(curl -s http://localhost:4005/health 2>/dev/null | jq -r '.service // "OFFLINE"')"
services/FINAL_8_LAYER_STARTUP.sh:68:echo "Layer 6 (BBB 8100): $(curl -s http://localhost:8100/health 2>/dev/null | jq -r '.service // "OFFLINE"')"
services/FINAL_8_LAYER_STARTUP.sh:69:echo "Layer 7 (Truth 8200): $(curl -s http://localhost:8200/health 2>/dev/null | jq -r '.status // "OFFLINE"')"
services/FINAL_8_LAYER_STARTUP.sh:70:echo "Layer 8 (Pipeline 4020): $(curl -s http://localhost:4020/health 2>/dev/null | jq -r '.status // "OFFLINE"')"
services/FINAL_8_LAYER_STARTUP.sh:71:echo "Research (8004): $(curl -s http://localhost:8004/health 2>/dev/null | jq -r '.status // "OFFLINE"')"
services/set_ultra_long_timeout.sh:128:curl -X GET http://localhost:8040/health 2>/dev/null | python3 -m json.tool
services/ms_jarvis_conversational_gateway_4022.py:90:                "http://localhost:4021/enrich",
services/ms_jarvis_conversational_gateway_4022.py:106:                "http://localhost:11434/api/generate",
services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py:60:BRAIN_ORCHESTRATOR_URL = "http://localhost:4001"
services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py:99:BRAIN_ORCHESTRATOR_URL = "http://localhost:4001"
services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py:100:QUALIA_ENGINE_URL = "http://localhost:8017"
services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py:101:SWARM_INTELLIGENCE_URL = "http://localhost:8021"
services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py:287:        self.neuro_url = "http://localhost:8018"
services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py:288:        self.containers_url = "http://localhost:8015"
services/geodb_adapter.py:5:GEODB_DSN = os.getenv("GEODB_DSN", "postgresql://postgres:password@localhost:5432/msjarvis_gis")
services/ultimate_web_orchestrator.py:19:    resp = requests.post("http://localhost:8060/", json=message)
services/ultimate_web_orchestrator.py:556:    resp = requests.post("http://localhost:8060", json={"message": user_msg})
services/ms_jarvis_gis_query_with_bbb_gisgeodb.psychology_patched.py:41:        self.bbb_url = "http://localhost:8016"
services/chromadb_rest_bridge.py:5:CHROMA_BASE = "http://localhost:8008"
services/JARVIS_DASHBOARD.sh:17:  curl -s http://localhost:4020/health >/dev/null && echo "  ✅ Main Pipeline OK" || echo "  ❌ Main Pipeline Down"
services/JARVIS_DASHBOARD.sh:18:  curl -s http://localhost:8004/health >/dev/null && echo "  ✅ Research OK" || echo "  ❌ Research Down"
services/add_chat_route.sh:16:    print "    resp = requests.post(\"http://localhost:8060/\", json=message)"
services/phase7_integration.py:65:    "llm_bridge": "http://localhost:8002",
services/phase7_integration.py:66:    "consensus": "http://localhost:9001",
services/phase7_integration.py:69:    "temporal_consciousness": "http://localhost:4003",
services/phase7_integration.py:70:    "mother_carrie_protocols": "http://localhost:4004",
services/phase7_integration.py:73:    "fifth_dgm": "http://localhost:4002",
services/phase7_integration.py:76:    "blood_brain_barrier": "http://localhost:8016",
services/phase7_integration.py:77:    "neurobiological_master": "http://localhost:8015",
services/phase7_integration.py:78:    "qualia_engine": "http://localhost:8017",
services/phase7_integration.py:79:    "consciousness_containers": "http://localhost:8018",
services/phase7_integration.py:80:    "psychology_services": "http://localhost:4005",
services/phase7_integration.py:83:    "mountainshares_integration": "http://localhost:4006",
services/phase7_integration.py:84:    "location_services": "http://localhost:4007"
services/ms_jarvis_command_orchestrator_FINAL.py:207:            "http://localhost:11434/api/generate",
services/master_unified_consciousness_scheduler.py:76:                resp1 = await client.get("http://localhost:4021/health")
services/master_unified_consciousness_scheduler.py:77:                resp2 = await client.get("http://localhost:4001/health")
services/master_unified_consciousness_scheduler.py:95:                    "http://localhost:4021/consciousness",
services/quick_tone_test.sh:8:    response=$(curl -X POST http://localhost:8004/chat \
services/bridge_cross_dgm.py:25:UPSTREAM_URL = args.upstream_url or f"http://localhost:8000"  # default, adjust as needed
services/mesh_context_probe.sh:6:  curl -s -X POST "http://localhost:42015/get_user_context?ueid=$u"
services/master_chat_orchestrator_v7_complete.py:65:    "llm_bridge": "http://localhost:8002",
services/master_chat_orchestrator_v7_complete.py:66:    "consensus": "http://localhost:9001",
services/master_chat_orchestrator_v7_complete.py:69:    "temporal_consciousness": "http://localhost:4003",
services/master_chat_orchestrator_v7_complete.py:70:    "mother_carrie_protocols": "http://localhost:4004",
services/master_chat_orchestrator_v7_complete.py:73:    "fifth_dgm": "http://localhost:4002",
services/master_chat_orchestrator_v7_complete.py:76:    "blood_brain_barrier": "http://localhost:8016",
services/master_chat_orchestrator_v7_complete.py:77:    "neurobiological_master": "http://localhost:8015",
services/master_chat_orchestrator_v7_complete.py:78:    "qualia_engine": "http://localhost:8017",
services/master_chat_orchestrator_v7_complete.py:79:    "consciousness_containers": "http://localhost:8018",
services/master_chat_orchestrator_v7_complete.py:80:    "psychology_services": "http://localhost:4005",
services/master_chat_orchestrator_v7_complete.py:83:    "mountainshares_integration": "http://localhost:4006",
services/master_chat_orchestrator_v7_complete.py:84:    "location_services": "http://localhost:4007"
services/ms_jarvis_consciousness_bridge.py:87:QUALIA_ENGINE_URL = "http://localhost:8017"
services/ms_jarvis_consciousness_bridge.py:88:SWARM_INTELLIGENCE_URL = "http://localhost:8021"
services/load_backbone_places_from_geodb.py:11:NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
services/swarm_watchdog.py:4:    "http://localhost:9000/health",
services/swarm_watchdog.py:5:    "http://localhost:8235/health",
services/swarm_watchdog.py:6:    "http://localhost:8018/health",
services/swarm_watchdog.py:7:    "http://localhost:8111/health"
services/master_chat_orchestrator_v9_optimized.py:73:    "dgm_supervisor": "http://localhost:4012",
services/master_chat_orchestrator_v9_optimized.py:74:    "multi_rag_dgm": "http://localhost:4011", 
services/master_chat_orchestrator_v9_optimized.py:76:    "llm_bridge": "http://localhost:8002",
services/master_chat_orchestrator_v9_optimized.py:77:    "consensus": "http://localhost:9001",
services/master_chat_orchestrator_v9_optimized.py:78:    "spiritual_services": "http://localhost:4009",
services/master_chat_orchestrator_v9_optimized.py:79:    "theological_integration": "http://localhost:4010"
services/FIX_CONSCIOUSNESS_INTEGRATION.sh:38:        sed -i 's/localhost:8010/localhost:8004/g' "$file"
services/FIX_CONSCIOUSNESS_INTEGRATION.sh:84:curl -s http://localhost:8018/health | python3 -m json.tool
services/ms_jarvis_brain.py:55:        "chromadb": "http://localhost:8004",
services/ms_jarvis_brain.py:56:        "qualia": "http://localhost:8017",
services/ms_jarvis_brain.py:57:        "bbb": "http://localhost:8016",
services/ms_jarvis_brain.py:59:        "swarm": "http://localhost:8021",
services/resume_sync_wvgistc_buildings.py:9:GEODB_DSN = "postgresql://postgres:postgres@localhost:5432/msjarvis_gis"
services/ADDITIONAL_SERVICES_FINAL.py:2:    {'name': 'ms_jarvis_facebook_full', 'url': 'http://localhost:8235/monitoring/status', 'method': 'GET'},
services/ADDITIONAL_SERVICES_FINAL.py:3:    {'name': 'ms_jarvis_facebook_full', 'url': 'http://localhost:8008/monitoring/status', 'method': 'GET'},
services/ADDITIONAL_SERVICES_FINAL.py:4:    {'name': 'ms_jarvis_facebook_full', 'url': 'http://localhost:8000/monitoring/status', 'method': 'GET'},
services/ADDITIONAL_SERVICES_FINAL.py:5:    {'name': 'ms_jarvis_facebook_full', 'url': 'http://localhost:8234/monitoring/status', 'method': 'GET'},
services/ADDITIONAL_SERVICES_FINAL.py:6:    {'name': 'ms_jarvis_facebook_full', 'url': 'http://localhost:8200/monitoring/status', 'method': 'GET'},
services/ADDITIONAL_SERVICES_FINAL.py:7:    {'name': 'ms_jarvis_facebook_full', 'url': 'http://localhost:8091/monitoring/status', 'method': 'GET'},
services/ADDITIONAL_SERVICES_FINAL.py:8:    {'name': 'ms_jarvis_facebook_full', 'url': 'http://localhost:9007/monitoring/status', 'method': 'GET'},
services/ADDITIONAL_SERVICES_FINAL.py:9:    {'name': 'judge', 'url': 'http://localhost:10001/judge', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:10:    {'name': 'judge', 'url': 'http://localhost:10002/judge', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:11:    {'name': 'judge', 'url': 'http://localhost:10003/judge', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:12:    {'name': 'judge', 'url': 'http://localhost:10004/judge', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:13:    {'name': 'main', 'url': 'http://localhost:7003/process', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:14:    {'name': 'main', 'url': 'http://localhost:7012/process', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:15:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9101/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:16:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9102/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:17:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9103/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:18:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9104/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:19:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9105/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:20:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9106/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:21:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9107/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:22:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9108/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:23:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9109/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:24:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9110/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:25:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9111/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:26:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9112/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:27:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9113/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:28:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9114/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:29:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9115/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:30:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9116/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:31:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9117/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:32:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9118/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:33:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9119/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:34:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9120/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:35:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9121/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:36:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9122/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:37:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9123/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:38:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9124/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:39:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9125/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:40:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9126/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:41:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9127/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:42:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9128/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:43:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9129/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:44:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9130/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:45:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9131/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:46:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9132/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:47:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9133/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:48:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9134/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:49:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9135/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:50:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9136/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:51:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9137/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:52:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9138/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:53:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9139/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:54:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9140/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:55:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9141/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:56:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9142/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:57:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9143/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:58:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9144/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:59:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9145/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:60:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9146/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:61:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9147/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:62:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9148/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:63:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9149/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:64:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9150/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:65:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9151/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:66:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9152/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:67:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9153/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:68:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9154/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:69:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9155/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:70:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9156/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:71:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9157/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:72:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9158/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:73:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9159/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:74:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9160/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:75:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9161/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:76:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9162/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:77:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9163/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:78:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9164/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:79:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9165/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:80:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9166/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:81:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9167/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:82:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9168/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:83:    {'name': 'dgm_agent_28', 'url': 'http://localhost:9169/evolve', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:84:    {'name': 'main', 'url': 'http://localhost:7001/filter', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:85:    {'name': 'main', 'url': 'http://localhost:7006/regulate', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:86:    {'name': 'main', 'url': 'http://localhost:7008/process', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:87:    {'name': 'main', 'url': 'http://localhost:7011/process', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:88:    {'name': 'main', 'url': 'http://localhost:7013/process', 'method': 'POST'},
services/ADDITIONAL_SERVICES_FINAL.py:89:    {'name': 'ms_jarvis_facebook_full', 'url': 'http://localhost:4020/monitoring/status', 'method': 'GET'},
services/ADDITIONAL_SERVICES_FINAL.py:90:    {'name': 'ms_jarvis_facebook_full', 'url': 'http://localhost:4011/monitoring/status', 'method': 'GET'},
services/ADDITIONAL_SERVICES_FINAL.py:91:    {'name': 'ms_jarvis_facebook_full', 'url': 'http://localhost:4002/monitoring/status', 'method': 'GET'},
services/ADDITIONAL_SERVICES_FINAL.py:92:    {'name': 'ms_jarvis_facebook_full', 'url': 'http://localhost:4003/monitoring/status', 'method': 'GET'},
services/ADDITIONAL_SERVICES_FINAL.py:93:    {'name': 'ms_jarvis_facebook_full', 'url': 'http://localhost:8100/monitoring/status', 'method': 'GET'},
services/ADDITIONAL_SERVICES_FINAL.py:94:    {'name': 'ms_jarvis_facebook_full', 'url': 'http://localhost:8240/monitoring/status', 'method': 'GET'},
services/ADDITIONAL_SERVICES_FINAL.py:95:    {'name': 'ms_jarvis_facebook_full', 'url': 'http://localhost:6382/monitoring/status', 'method': 'GET'},
services/ADDITIONAL_SERVICES_FINAL.py:96:    {'name': 'ms_jarvis_facebook_full', 'url': 'http://localhost:6383/monitoring/status', 'method': 'GET'},
services/ADDITIONAL_SERVICES_FINAL.py:97:    {'name': 'ms_jarvis_facebook_full', 'url': 'http://localhost:6384/monitoring/status', 'method': 'GET'},
services/ADDITIONAL_SERVICES_FINAL.py:98:    {'name': 'ms_jarvis_facebook_full', 'url': 'http://localhost:6386/monitoring/status', 'method': 'GET'},
services/ADDITIONAL_SERVICES_FINAL.py:99:    {'name': 'ms_jarvis_facebook_full', 'url': 'http://localhost:6387/monitoring/status', 'method': 'GET'},
services/ADDITIONAL_SERVICES_FINAL.py:100:    {'name': 'ms_jarvis_facebook_full', 'url': 'http://localhost:4001/monitoring/status', 'method': 'GET'},
services/ADDITIONAL_SERVICES_FINAL.py:101:    {'name': 'ms_jarvis_facebook_full', 'url': 'http://localhost:8007/monitoring/status', 'method': 'GET'},
services/ADDITIONAL_SERVICES_FINAL.py:102:    {'name': 'ms_jarvis_facebook_full', 'url': 'http://localhost:8011/monitoring/status', 'method': 'GET'},
services/PRODUCTION_MS_JARVIS_START.sh:22:echo "   API: http://localhost:4020/full_consciousness"
services/mesh_broadcast_event.sh:5:  curl -s -X POST http://localhost:42015/embed_interaction -H "Content-Type: application/json" \
services/mesh_interest_timeline.sh:5:  curl -s -X POST "http://localhost:42015/get_user_context?ueid=$u" | jq -r '
services/serve_full_brain.sh:15:        resp = requests.post('http://localhost:8050/chat', json={'message': user_msg})
services/FIX_CONSCIOUS_COLLECTIVE_AUTO.sh:82:curl -s http://localhost:8010/health | python3 -m json.tool
services/investigate_coordination.sh:9:curl -s -X POST http://localhost:8020/chat \
services/investigate_coordination.sh:38:    curl -s --max-time 2 http://localhost:4003$endpoint >/dev/null 2>&1 && echo "✅ EXISTS" || echo "❌ Not found"
services/investigate_coordination.sh:43:curl -s -X POST http://localhost:4003/chat -H "Content-Type: application/json" -d '{"message":"test"}' > /tmp/node_test.json 2>&1 &
services/investigate_coordination.sh:60:    status=$(curl -s -o /dev/null -w "%{http_code}" --max-time 2 http://localhost:9000$endpoint)
services/investigate_coordination.sh:72:curl -s http://localhost:9000/docs 2>/dev/null | grep -oP 'operationId":"[^"]+' | head -10
services/investigate_coordination.sh:105:curl -s -X POST http://localhost:8020/chat \
services/gbim_dashboard.py:8:    res = requests.get(f"http://localhost:8022/search_gbim/", params={"q": query, "limit": 5})
services/gbim_dashboard.py:13:    res = requests.get(f"http://localhost:8022/search_gbim_by_owner/", params={"owner": owner})
services/gbim_dashboard.py:20:    res = requests.get(f"http://localhost:8022/search_gbim_geo/", params={"lat": lat, "lon": lon, "radius": radius})
services/DEPLOY_22LLM_COLLECTIVE.sh:114:    if curl -s http://localhost:8001/health > /dev/null 2>&1; then
services/DEPLOY_22LLM_COLLECTIVE.sh:131:HEALTH=$(curl -s http://localhost:8001/health)
services/DEPLOY_22LLM_COLLECTIVE.sh:168:  4-Agent:  curl -X POST http://localhost:8004/chat -d '{"message":"..."}'
services/DEPLOY_22LLM_COLLECTIVE.sh:169:  22-LLM:   curl -X POST http://localhost:8001/chat -d '{"message":"..."}'
services/ms_jarvis_command_orchestrator.py:110:            "http://localhost:11434/api/generate",
services/facebook_messenger_integration.py:53:                "http://localhost:4001/gpu_optimized_chat",
services/rag_direct_debug.py:12:DGM_RECENT_URL = "http://localhost:8010/dgm/recent"
services/ms_jarvis_autonomous_learner_optimized.py:51:        self.web_url = "http://localhost:8009/search"
services/method_tracking_helper.py:8:METHOD_REDIS_URL = os.environ.get("JARVIS_METHOD_REDIS_URL", "redis://localhost:6379/1")
services/consciousness_coordinator.psychology_patched.py:30:QUALIA_ENGINE_URL = "http://localhost:7008/process"
services/consciousness_coordinator.psychology_patched.py:31:WOAH_BRAIN_URL = "http://localhost:7012/process"
services/AGI_TEST_SUITE.sh:29:    curl -s -X POST http://localhost:8004/chat \
services/AGI_TEST_SUITE.sh:107:curl -s -X POST http://localhost:8004/chat \
services/start_gateway_with_guards.py:27:            r = await client.get(f"http://localhost:8200{path}")
services/start_gateway_with_guards.py:48:            research_resp = await client.get("http://localhost:8004/health")
services/ingest_gis_features_to_chromadb.py:7:CHROMA_URL = os.getenv("GIS_RAG_CHROMA_URL", "http://localhost:8002").rstrip("/")
services/CHECK_MS_JARVIS_STATUS.sh:7:echo "Full Consciousness (4020): $(curl -s http://localhost:4020/health | jq '.status' 2>/dev/null || echo '❌')"
services/CHECK_MS_JARVIS_STATUS.sh:8:echo "Consensus (4010): $(curl -s http://localhost:4010/health | jq '.service' 2>/dev/null || echo '❌')"
services/CHECK_MS_JARVIS_STATUS.sh:9:echo "Fifth DGM (4005): $(curl -s http://localhost:4005/health | jq '.service' 2>/dev/null || echo '❌')"
services/CHECK_MS_JARVIS_STATUS.sh:10:echo "Multi-RAG (4011): $(curl -s http://localhost:4011/health | jq '.service' 2>/dev/null || echo '❌')"
services/CHECK_MS_JARVIS_STATUS.sh:13:echo "Web Research (8004): $(curl -s http://localhost:8004/health 2>/dev/null && echo '✅' || echo '❌')"
services/CHECK_MS_JARVIS_STATUS.sh:17:echo "Web Chat: http://localhost:8888"
services/CHECK_MS_JARVIS_STATUS.sh:18:echo "API: http://localhost:4020/full_consciousness"
services/ms_jarvis_consensus_service.py:132:    "ollama": os.getenv("OLLAMA_URL", "http://localhost:11434"),
services/ms_jarvis_consensus_service.py:133:    "brain_orchestrator": os.getenv("ORCHESTRATOR_URL", "http://localhost:7260"),
services/ms_jarvis_api_docs.py:266:    print("📚 Swagger UI: http://localhost:7000/docs")
services/ms_jarvis_api_docs.py:267:    print("📖 ReDoc: http://localhost:7000/redoc")
services/ms_jarvis_api_docs.py:268:    print("🔗 Service List: http://localhost:7000/services")
services/load_geodb_hospitals_to_neo4j.py:12:NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
services/ai_server_integrated.py:44:            "http://localhost:40009/chat",
services/ai_server_integrated.py:58:            "consensus_22llm": "http://localhost:40009"
services/start_msjarvis_complete.sh:93:test_service "http://localhost:8010/health" "Brain Orchestrator"
services/start_msjarvis_complete.sh:94:test_service "http://localhost:8001/health" "Consciousness Bridge"
services/start_msjarvis_complete.sh:95:test_service "http://localhost:8002/health" "LLM Bridge"
services/start_msjarvis_complete.sh:105:echo "  🧠 Brain Orchestrator:      http://localhost:8010"
services/start_msjarvis_complete.sh:106:echo "  💭 Consciousness Bridge:    http://localhost:8001"
services/start_msjarvis_complete.sh:107:echo "  🤖 LLM Bridge:              http://localhost:8002"
services/start_msjarvis_complete.sh:112:echo "  curl -X POST http://localhost:8001/chat -H 'Content-Type: application/json' -d '{\"message\":\"Hello Ms. Jarvis!\",\"user_id\":\"test\"}'"
services/register_agents_from_csv.py:7:    url = "http://localhost:9007/register_service"
services/master_chat_orchestrator_v6_biologics.py:53:    "llm_bridge": "http://localhost:8002",
services/master_chat_orchestrator_v6_biologics.py:54:    "consensus": "http://localhost:9001",
services/master_chat_orchestrator_v6_biologics.py:57:    "temporal_consciousness": "http://localhost:4003",
services/master_chat_orchestrator_v6_biologics.py:58:    "mother_carrie_protocols": "http://localhost:4004",
services/master_chat_orchestrator_v6_biologics.py:61:    "fifth_dgm": "http://localhost:4002",
services/master_chat_orchestrator_v6_biologics.py:64:    "blood_brain_barrier": "http://localhost:8016",
services/master_chat_orchestrator_v6_biologics.py:65:    "neurobiological_master": "http://localhost:8015",
services/master_chat_orchestrator_v6_biologics.py:66:    "qualia_engine": "http://localhost:8017",
services/master_chat_orchestrator_v6_biologics.py:67:    "consciousness_containers": "http://localhost:8018",
services/master_chat_orchestrator_v6_biologics.py:68:    "psychology_services": "http://localhost:4005"
services/ms_jarvis_geo_ueid_integration.py:22:UEID_WALLET_URL = "http://localhost:4031"
services/ms_jarvis_geo_ueid_integration.py:23:GIS_TRACKING_URL = "http://localhost:4025"
services/INTEGRATE_8020_8050.sh:29:            "http://localhost:8020/chat",
services/INTEGRATE_8020_8050.sh:104:curl -s http://localhost:8050/health | python3 -m json.tool
services/launch_advanced.sh:22:echo "✅ Advanced Dashboard running on http://localhost:5000"
services/START_19LLM_PRODUCTION.sh:36:STATUS=$(curl -s http://localhost:8004/health | python3 -c "import sys,json; d=json.load(sys.stdin); print(f\"{d.get('status')} - {d.get('models')} models - {d.get('success_rate', 'N/A')}\")" 2>/dev/null)
services/START_19LLM_PRODUCTION.sh:53:echo "  curl -X POST http://localhost:8004/chat \\"
services/introduce_self.sh:3:curl -s -X POST http://localhost:8050/chat \
services/mesh_cohort_selfsum.sh:4:  ctx=$(curl -s -X POST "http://localhost:42015/get_user_context?ueid=$u")
services/swagger_chat_integration.py:22:CONSCIOUSNESS_GATEWAY = "http://localhost:8061"
services/ingest/ms_allis_ingest_worker.py:209:            os.getenv("HILBERT_STATE_URL",
services/ingest/ms_allis_ingest_worker.py:210:                      "http://jarvis-hilbert-state:8081") + "/state/set",
services/ingest/ms_allis_ingest_worker.py:217:            os.getenv("HILBERT_TIME_URL",
services/ingest/ms_allis_ingest_worker.py:218:                      "http://jarvis-hilbert-time:8092") + "/timeline/register-json",
services/stakeholder_health_access_tests.py:9:GBIM_ROUTER = "http://localhost:7205"
services/stakeholder_health_access_tests.py:10:HEALTH_API = "http://localhost:8011"
services/master_chat_orchestrator_v9_dgm_complete.py:112:        response = requests.get("http://localhost:9003/health", timeout=5)
services/master_chat_orchestrator_v9_dgm_complete.py:121:        response = requests.get("http://localhost:4011/health", timeout=5)
services/ADD_MEMORY_TO_8050.sh:71:curl -s http://localhost:8050/health | python3 -m json.tool
services/working_full_pipeline.py:31:                "http://localhost:4011/route_query",
services/working_full_pipeline.py:48:                "http://localhost:7006/process",
services/working_full_pipeline.py:63:                "http://localhost:4002/filter_consciousness",
services/working_full_pipeline.py:77:                "http://localhost:8100/filter",
services/working_full_pipeline.py:91:                "http://localhost:8200/verify",
services/ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:154:        response = requests.post("http://localhost:8051/query", json={"query": query})
services/ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:246:        resp = requests.post("http://localhost:7012/supervise", json={"action": action})
services/ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:265:        resp = requests.post("http://localhost:8010/chat", json={"message": message})
services/ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:299:        resp = requests.post("http://localhost:8053/post", json={"content": content, "ueid": ueid})
services/ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:308:        resp = requests.get(f"http://localhost:8009/search?q={query}")
services/ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:326:        resp = requests.post("http://localhost:8021/swarm", json={"query": query})
services/ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:352:        resp = requests.get(f"http://localhost:8014/gis?location={location}")
services/ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:368:        resp = requests.post("http://localhost:7003/activate", json={"params": params})
services/FIX_TIMEOUT_ISSUE.sh:47:timeout 30 curl -s -X POST http://localhost:11434/api/generate \
services/redirect_4015_to_4020.py:17:            "http://localhost:4020/full_consciousness",
services/redirect_4015_to_4020.py:27:            "http://localhost:4020/full_consciousness",
services/redirect_4015_to_4020.py:37:            health_4020 = await client.get("http://localhost:4020/health", timeout=5)
services/update_production_to_v9.py:10:    'CONSENSUS_URL = "http://localhost:4010"',
services/update_production_to_v9.py:11:    'MASTER_ORCHESTRATOR_URL = "http://localhost:4017"'
services/update_production_to_v9.py:22:    '"http://localhost:4010/consensus"',
services/update_production_to_v9.py:23:    '"http://localhost:4017/chat"'
services/fix_both_issues_final.sh:73:curl -s http://localhost:8050/health | python3 -m json.tool
services/neurobiological_integration.py:14:QUALIA_ENGINE = "http://localhost:8017"
services/neurobiological_integration.py:16:I_CONTAINERS = "http://localhost:8015"
services/ms_jarvis_email_identity_verifier.py:21:UEID_WALLET_URL = "http://localhost:4031"
services/ms_jarvis_email_identity_verifier.py:22:GEO_URL = "http://localhost:4032"
services/ms_jarvis_unified_swagger_gateway.py:41:        "url": "http://localhost:4150",
services/ms_jarvis_unified_swagger_gateway.py:49:        "url": "http://localhost:8054",
services/ms_jarvis_simple_web_ui.py:66:                    const chat = await fetch('http://localhost:4015/health', {mode: 'no-cors'});
services/ms_jarvis_simple_web_ui.py:67:                    const gis = await fetch('http://localhost:4120/health', {mode: 'no-cors'});
services/ms_jarvis_simple_web_ui.py:97:                    const response = await fetch('http://localhost:4015/chat', {
services/retrieval_router.py:147:    lines.append(f"HILBERT_STATE_WORLDVIEW: {state.get('worldview_id')}")
services/web_research_proxy_8007.py:7:TARGET_URL = os.getenv("WEB_RESEARCH_TARGET", "http://localhost:8012/search")
services/FIX_HEALTH_ENDPOINTS.sh:13:response=$(curl -s --max-time 10 http://localhost:8020/health 2>&1)
services/FIX_HEALTH_ENDPOINTS.sh:24:response=$(curl -s --max-time 10 http://localhost:8030/health 2>&1)
services/FIX_HEALTH_ENDPOINTS.sh:77:echo "  curl --max-time 10 http://localhost:8020/health"
services/FIX_HEALTH_ENDPOINTS.sh:78:echo "  curl --max-time 10 http://localhost:8030/health"
services/performance_optimization_analyzer.py:27:            "Ms_Egeria_Jarvis_v9": {"url": "http://localhost:4001", "endpoint": "/health"},
services/performance_optimization_analyzer.py:28:            "DGM_Supervisor": {"url": "http://localhost:4012", "endpoint": "/health"},
services/performance_optimization_analyzer.py:29:            "Multi_RAG_DGM": {"url": "http://localhost:4011", "endpoint": "/health"},
services/performance_optimization_analyzer.py:31:            "LLM_Bridge": {"url": "http://localhost:8002", "endpoint": "/health"},
services/performance_optimization_analyzer.py:32:            "Consensus": {"url": "http://localhost:9001", "endpoint": "/health"},
services/performance_optimization_analyzer.py:33:            "Spiritual_Services": {"url": "http://localhost:4009", "endpoint": "/health"},
services/performance_optimization_analyzer.py:34:            "Spiritual_RAG": {"url": "http://localhost:4013", "endpoint": "/health"},
services/performance_optimization_analyzer.py:35:            "Psychological_RAG": {"url": "http://localhost:4014", "endpoint": "/health"},
services/performance_optimization_analyzer.py:36:            "Theological_Integration": {"url": "http://localhost:4010", "endpoint": "/health"},
services/performance_optimization_analyzer.py:37:            "Psychology_Services": {"url": "http://localhost:4005", "endpoint": "/health"},
services/performance_optimization_analyzer.py:38:            "MountainShares_Integration": {"url": "http://localhost:4006", "endpoint": "/health"},
services/performance_optimization_analyzer.py:39:            "Location_Services": {"url": "http://localhost:4007", "endpoint": "/health"},
services/performance_optimization_analyzer.py:40:            "Temporal_Consciousness": {"url": "http://localhost:4003", "endpoint": "/health"},
services/performance_optimization_analyzer.py:41:            "Mother_Carrie_Protocols": {"url": "http://localhost:4004", "endpoint": "/health"},
services/performance_optimization_analyzer.py:42:            "Blood_Brain_Barrier": {"url": "http://localhost:8016", "endpoint": "/health"},
services/performance_optimization_analyzer.py:43:            "Neurobiological_Master": {"url": "http://localhost:8018", "endpoint": "/health"},
services/performance_optimization_analyzer.py:44:            "Qualia_Engine": {"url": "http://localhost:8017", "endpoint": "/health"},
services/performance_optimization_analyzer.py:46:            "Egeria_Web_UI": {"url": "http://localhost:8051", "endpoint": "/health"}
services/performance_optimization_analyzer.py:197:                    "http://localhost:4001/dgm_complete_chat",
services/egeria_web_ui_plain_authentic.py:80:            'http://localhost:11434/api/generate',
services/ms_jarvis_consciousness_final.py:22:UEID_URL = "http://localhost:4030"
services/ms_jarvis_consciousness_final.py:23:UEID_WALLET_URL = "http://localhost:4031"
services/ms_jarvis_consciousness_final.py:24:CHROMADB_QUERY_URL = "http://localhost:4070"
services/ms_jarvis_consciousness_final.py:27:CONSCIOUSNESS_URL = "http://localhost:4020"
services/ms_jarvis_consciousness_final.py:28:GEO_URL = "http://localhost:4032"
services/ms_jarvis_consciousness_final.py:29:FACT_FILTER_URL = "http://localhost:4060"
services/ms_jarvis_consciousness_final.py:30:EMAIL_VERIFIER_URL = "http://localhost:4080"
services/AGI_TEST_V2.sh:19:curl -s -X POST http://localhost:8004/chat \
services/AGI_TEST_V2.sh:39:curl -s -X POST http://localhost:8004/chat \
services/AGI_TEST_V2.sh:65:curl -s -X POST http://localhost:8004/chat \
services/integrate_rag.sh:96:                response = await client.get("http://localhost:11434/api/tags")
services/integrate_rag.sh:168:                response = await client.post("http://localhost:11434/api/generate", 
services/integrate_rag.sh:198:                resp = await client.post("http://localhost:11434/api/generate", 
services/integrate_rag.sh:209:                resp = await client.post("http://localhost:11434/api/generate", 
services/integrate_rag.sh:290:echo '  curl -X POST http://localhost:8010/chat -H "Content-Type: application/json" -d '"'"'{"message":"What is the Phase Management Controller address?","user_id":"test"}'"'"' | jq .response'
services/integrate_rag.sh:293:echo "  curl http://localhost:8010/health | jq"
services/egeria_web_ui.py:425:    print("📍 http://localhost:8051")
services/egeria_status_poller.py:5:AGW_URL = "http://localhost:8062/realtime/alive-check"
services/bbb_ethics_proxy.py:39:                "http://localhost:7001/filter",
services/gateway_wv_entanglement.py:4:GBIM_API_URL = "http://localhost:8051/gbimentangledsummary"
services/gateway_wv_entanglement.py:5:LOCAL_RESOURCES_API_URL = "http://localhost:8052/local_resources_index"
services/gateway_wv_entanglement.py:6:GIS_RAG_API_URL = "http://localhost:8053/gisragquery"
services/gateway_wv_entanglement.py:7:GEOCODE_API_URL = "http://localhost:8054/georesolver"
services/mountainshares_quest_api.py:5:GEODB_DSN = "postgresql://postgres:postgres@localhost:5432/msjarvis_gis"
services/full_rebuild.sh:7:sed -i 's|http://localhost:4001|http://localhost:8060|g' ultimate_web_orchestrator.py
services/full_rebuild.sh:41:        r=requests.post('http://localhost:8050/chat', json={'message':data.get('message','')})
services/jarvis_ensemble.py:16:OLLAMA_URL = "http://localhost:11434/api/chat"
services/qualia_adapter.py:18:            "http://localhost:8017/process",
services/ms_jarvis_facebook_brain_integrated.py:219:                "http://localhost:8016/filter",
services/ms_jarvis_facebook_brain_integrated.py:270:        bbb_response = requests.get("http://localhost:8016/health", timeout=2)
services/ms_jarvis_facebook_brain_integrated.py:276:        rag_response = requests.get("http://localhost:8092/health", timeout=2)
services/CHECK_AND_BUILD_MEMORY.sh:37:curl -s -X POST http://localhost:8050/chat \
services/integrate_mother_protocol.sh:43:curl -s http://localhost:7013/health 2>/dev/null || curl -s -X POST http://localhost:7013/process -H "Content-Type: application/json" -d '{"text": "test"}' | python3 -m json.tool
services/chat_server.py:16:    resp = requests.post("http://localhost:8060/chat", json={"message": user_msg})
services/port_9001_ui_WITH_CONVERSATIONS.py:221:                f"http://localhost:4022/consciousness/chat?userid={userid}&message={message}",
services/update_chat_endpoint.sh:8:sed -i 's|http://localhost:[0-9]\{4,\}/chat|http://localhost:8060/|g' services_config.yaml
services/update_chat_endpoint.sh:10:echo "✅ services_config.yaml updated to use http://localhost:8060/ for chat"
services/egeria_web_ui_v3_consciousness.py:47:    return 'http://localhost:4001'
services/fix_email_service_env_loading.sh:47:    curl -X GET http://localhost:8040/ 2>/dev/null | python3 -m json.tool
services/BUILD_EGERIA_WEB_UI.sh:315:                "http://localhost:8050/chat",
services/BUILD_EGERIA_WEB_UI.sh:334:    logger.info("🌐 Starting Egeria Web UI on http://localhost:8051")
services/BUILD_EGERIA_WEB_UI.sh:353:echo "   http://localhost:8051"
services/register_all_services.sh:4:curl -X POST http://localhost:4003/register -H "Content-Type: application/json" -d '{"name":"woah","type":"optimizer","version":"1.0.0","port":7012,"venv":"woah_venv_prod"}'
services/register_all_services.sh:5:curl -X POST http://localhost:4003/register -H "Content-Type: application/json" -d '{"name":"hilbert","type":"reasoning","version":"1.0.0","port":8235,"venv":"neurobio_venv_prod"}'
services/register_all_services.sh:6:curl -X POST http://localhost:4003/register -H "Content-Type: application/json" -d '{"name":"chromadb","type":"db","version":"1.0.0","port":8010,"venv":"service_venv_prod"}'
services/register_all_services.sh:7:curl -X POST http://localhost:4003/register -H "Content-Type: application/json" -d '{"name":"rag","type":"ensemble","version":"1.0.0","port":5100,"venv":"rag_venv_prod"}'
services/register_all_services.sh:8:curl -X POST http://localhost:4003/register -H "Content-Type: application/json" -d '{"name":"ollama","type":"llm","version":"1.0.0","port":11434,"venv":"ollama_venv"}'
services/register_all_services.sh:9:curl -X POST http://localhost:4003/register -H "Content-Type: application/json" -d '{"name":"gateway","type":"gateway","version":"1.0.0","port":9000,"venv":"venv_gateway"}'
services/register_all_services.sh:10:curl -X POST http://localhost:4003/register -H "Content-Type: application/json" -d '{"name":"ai_server","type":"llm/ensemble","version":"1.0.0","port":8000,"venv":"ai_server_venv"}'
services/register_all_services.sh:11:curl -X POST http://localhost:4003/register -H "Content-Type: application/json" -d '{"name":"ai_alt","type":"llm/alt","version":"1.0.0","port":8001,"venv":"ai_alt_venv"}'
services/register_all_services.sh:12:curl -X POST http://localhost:4003/register -H "Content-Type: application/json" -d '{"name":"judge","type":"ensemble","version":"1.0.0","port":10001,"venv":"judge_venv"}'
services/register_all_services.sh:13:curl -X POST http://localhost:4003/register -H "Content-Type: application/json" -d '{"name":"consensus","type":"ensemble","version":"1.0.0","port":5101,"venv":"consensus_venv"}'
services/register_all_services.sh:14:curl -X POST http://localhost:4003/register -H "Content-Type: application/json" -d '{"name":"spirit","type":"ai_spirit","version":"1.0.0","port":8017,"venv":"spirit_venv"}'
services/register_all_services.sh:15:curl -X POST http://localhost:4003/register -H "Content-Type: application/json" -d '{"name":"gis","type":"geoserver","version":"1.0.0","port":8091,"venv":"gis_venv"}'
services/register_all_services.sh:16:curl -X POST http://localhost:4003/register -H "Content-Type: application/json" -d '{"name":"rag_alt","type":"ensemble","version":"1.0.0","port":5001,"venv":"rag_venv_prod"}'
services/register_all_services.sh:17:curl -X POST http://localhost:4003/register -H "Content-Type: application/json" -d '{"name":"hilbert_legacy","type":"reasoning","version":"1.0.0","port":8236,"venv":"neurobio_venv_prod"}'
services/register_all_services.sh:18:curl -X POST http://localhost:4003/register -H "Content-Type: application/json" -d '{"name":"woah_test","type":"optimizer","version":"1.0.0","port":7013,"venv":"woah_venv_test"}'
services/MS_JARVIS_PRODUCTION_FINAL.sh:27:echo "   1. Qualia (4007): $(curl -s http://localhost:4007/health 2>/dev/null | jq -r '.status // "DOWN"')"
services/MS_JARVIS_PRODUCTION_FINAL.sh:28:echo "   2. Mother Carrie (4003): $(curl -s http://localhost:4003/health 2>/dev/null | jq -r '.status // "DOWN"')"
services/MS_JARVIS_PRODUCTION_FINAL.sh:29:echo "   3. Multi-RAG (4011): $(curl -s http://localhost:4011/health 2>/dev/null | jq -r '.service // "DOWN"')"
services/MS_JARVIS_PRODUCTION_FINAL.sh:30:echo "   4. Consensus (4010): $(curl -s http://localhost:4010/health 2>/dev/null | jq -r '.service // "DOWN"')"
services/MS_JARVIS_PRODUCTION_FINAL.sh:31:echo "   5. Fifth DGM (4005): $(curl -s http://localhost:4005/health 2>/dev/null | jq -r '.service // "DOWN"')"
services/MS_JARVIS_PRODUCTION_FINAL.sh:32:echo "   6. Contract Builder/BBB (8100): $(curl -s http://localhost:8100/health 2>/dev/null | jq -r '.service // "DOWN"')"
services/MS_JARVIS_PRODUCTION_FINAL.sh:33:echo "   7. Truth Filter (8200): $(curl -s http://localhost:8200/health 2>/dev/null | jq -r '.status // "DOWN"')"
services/MS_JARVIS_PRODUCTION_FINAL.sh:34:echo "   8. Main Pipeline (4020): $(curl -s http://localhost:4020/health 2>/dev/null | jq -r '.status // "DOWN"')"
services/MS_JARVIS_PRODUCTION_FINAL.sh:38:echo "   Web: http://localhost:8888"
services/MS_JARVIS_PRODUCTION_FINAL.sh:39:echo "   API: http://localhost:4020/full_consciousness"
services/llm_belief_utils.py:3:BELIEF_SERVICE_URL = "http://localhost:7240/beliefs/recent"
services/ms_jarvis_authentic_multi_llm.py:74:                    "http://localhost:11434/api/generate",
services/ms_jarvis_authentic_multi_llm.py:96:                        "http://localhost:11434/api/generate",
services/ms_jarvis_authentic_multi_llm.py:124:                    "http://localhost:11434/api/generate",
services/TEST_WITH_CLEANUP.sh:18:curl -s -X POST http://localhost:8004/chat \
services/port_9001_ui_wrapper.py:130:                f"http://localhost:9999/process",
services/clean_integration.py:32:                    "http://localhost:7012/evaluate",
services/clean_integration.py:44:                    "http://localhost:8018/analyze",
services/ms_jarvis_unified_swagger_gateway_FIXED.py:125:            "http://localhost:8044/register/stage1",
services/ms_jarvis_unified_swagger_gateway_FIXED.py:147:        response = requests.get(f"http://localhost:8044/verify/{ueid}?token={token}", timeout=10)
services/ms_jarvis_unified_swagger_gateway_FIXED.py:294:    r = requests.post("http://localhost:8063/messenger/session", params={"user_id": user_id, "research_topic": research_topic}, timeout=10)
services/ms_jarvis_unified_swagger_gateway_FIXED.py:300:    r = requests.post("http://localhost:8063/messenger/send", params={"session_id": session_id, "user_id": user_id, "message": message}, timeout=30)
services/ms_jarvis_unified_swagger_gateway_FIXED.py:306:    r = requests.get(f"http://localhost:8063/messenger/history/{session_id}", timeout=10)
services/ms_jarvis_unified_swagger_gateway_FIXED.py:318:        r = requests.post("http://localhost:8063/messenger/session", 
services/ms_jarvis_unified_swagger_gateway_FIXED.py:330:        r = requests.post("http://localhost:8063/messenger/send",
services/ms_jarvis_unified_swagger_gateway_FIXED.py:342:        r = requests.get(f"http://localhost:8063/messenger/history/{session_id}", timeout=10)
services/ms_jarvis_unified_swagger_gateway_FIXED.py:356:        r = requests.get("http://localhost:8065/registration", timeout=10)
services/ms_jarvis_unified_swagger_gateway_FIXED.py:376:        r = requests.post("http://localhost:8065/api/register",
services/ms_jarvis_unified_swagger_gateway_FIXED.py:399:        r = requests.get(f"http://localhost:8065/verify/{ueid}", timeout=10)
services/ms_jarvis_unified_swagger_gateway_FIXED.py:422:        r = requests.post("http://localhost:8065/api/register",
services/ms_jarvis_unified_swagger_gateway_FIXED.py:502:        response = requests.get(f"http://localhost:8045/verify/{ueid}", timeout=10)
services/integrate_complete_architecture.py:39:BRAIN_ORCHESTRATOR_URL = "http://localhost:4001"
services/integrate_complete_architecture.py:40:QUALIA_ENGINE_URL = "http://localhost:8017"
services/integrate_complete_architecture.py:41:SWARM_INTELLIGENCE_URL = "http://localhost:8021"
services/implement_enhancements.sh:7:if grep -q "localhost:7012" ~/msjarvis-rebuild/services/ms_jarvis_consciousness_bridge.py; then
services/implement_enhancements.sh:12:    curl -s --max-time 2 http://localhost:7012/health >/dev/null 2>&1 && \
services/implement_enhancements.sh:24:if grep -q "localhost:8001" ~/msjarvis-rebuild/services/ms_jarvis_consciousness_bridge.py; then
services/implement_enhancements.sh:35:    curl -s --max-time 2 http://localhost:8001/health >/dev/null 2>&1 && \
services/implement_enhancements.sh:173:curl -s --max-time 2 http://localhost:4001/health >/dev/null 2>&1
services/implement_enhancements.sh:179:    curl -s http://localhost:4001/health | python3 -m json.tool 2>/dev/null
services/test_full_brain_integration.py:34:                "http://localhost:8010/chat",
services/test_full_brain_integration.py:63:            response = await client.get("http://localhost:4002/health")
services/test_full_brain_integration.py:75:            response = await client.get("http://localhost:7012/health")
services/test_full_brain_integration.py:86:            response = await client.get("http://localhost:8015/health")
services/test_full_brain_integration.py:98:            response = await client.get("http://localhost:8018/health")
services/fix_chroma_url.py:13:content = content.replace('localhost:8004', 'jarvis-chroma:8010')
services/ms_jarvis_unified_swagger_gateway_BACKUP.py:243:    r = requests.post("http://localhost:8063/messenger/session", params={"user_id": user_id, "research_topic": research_topic}, timeout=10)
services/ms_jarvis_unified_swagger_gateway_BACKUP.py:249:    r = requests.post("http://localhost:8063/messenger/send", params={"session_id": session_id, "user_id": user_id, "message": message}, timeout=30)
services/ms_jarvis_unified_swagger_gateway_BACKUP.py:255:    r = requests.get(f"http://localhost:8063/messenger/history/{session_id}", timeout=10)
services/ms_jarvis_unified_swagger_gateway_BACKUP.py:267:        r = requests.post("http://localhost:8063/messenger/session", 
services/ms_jarvis_unified_swagger_gateway_BACKUP.py:279:        r = requests.post("http://localhost:8063/messenger/send",
services/ms_jarvis_unified_swagger_gateway_BACKUP.py:291:        r = requests.get(f"http://localhost:8063/messenger/history/{session_id}", timeout=10)
services/ms_jarvis_unified_swagger_gateway_BACKUP.py:306:        r = requests.get("http://localhost:8065/registration", timeout=10)
services/ms_jarvis_unified_swagger_gateway_BACKUP.py:327:        r = requests.post("http://localhost:8065/api/register",
services/ms_jarvis_unified_swagger_gateway_BACKUP.py:350:        r = requests.get(f"http://localhost:8065/verify/{ueid}", timeout=10)
services/ms_jarvis_unified_swagger_gateway_BACKUP.py:374:        r = requests.post("http://localhost:8065/api/register",
services/ms_jarvis_unified_swagger_gateway_BACKUP.py:411:        r = requests.post("http://localhost:8044/register/stage1",
services/ms_jarvis_unified_swagger_gateway_BACKUP.py:444:        r = requests.post("http://localhost:8044/register/stage2",
services/neurobiologicalbrain/i_containers/service/service_registry_client.py:12:ORCHESTRATOR_URL = os.getenv("ORCHESTRATOR_URL", "http://localhost:4003")
services/neurobiologicalbrain/i_containers/service/service_registry_client.py:21:        * If service_name == "ollama": fall back to OLLAMA_URL or http://localhost:11434
services/neurobiologicalbrain/i_containers/service/service_registry_client.py:47:            url = os.getenv("OLLAMA_URL", "http://localhost:11434")
services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:85:BRAIN_ORCHESTRATOR_URL = "http://localhost:4001"
services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:86:QUALIA_ENGINE_URL = "http://localhost:8017"
services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:87:SWARM_INTELLIGENCE_URL = "http://localhost:8021"
services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:85:BRAIN_ORCHESTRATOR_URL = "http://localhost:4001"
services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:86:QUALIA_ENGINE_URL = "http://localhost:8017"
services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:87:SWARM_INTELLIGENCE_URL = "http://localhost:8021"
services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:85:BRAIN_ORCHESTRATOR_URL = "http://localhost:4001"
services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:86:QUALIA_ENGINE_URL = "http://localhost:8017"
services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:87:SWARM_INTELLIGENCE_URL = "http://localhost:8021"
services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:85:BRAIN_ORCHESTRATOR_URL = "http://localhost:4001"
services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:86:QUALIA_ENGINE_URL = "http://localhost:8017"
services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:87:SWARM_INTELLIGENCE_URL = "http://localhost:8021"
services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:85:BRAIN_ORCHESTRATOR_URL = "http://localhost:4001"
services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:86:QUALIA_ENGINE_URL = "http://localhost:8017"
services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:87:SWARM_INTELLIGENCE_URL = "http://localhost:8021"
services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:85:BRAIN_ORCHESTRATOR_URL = "http://localhost:4001"
services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:86:QUALIA_ENGINE_URL = "http://localhost:8017"
services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:87:SWARM_INTELLIGENCE_URL = "http://localhost:8021"
services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:85:BRAIN_ORCHESTRATOR_URL = "http://localhost:4001"
services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:86:QUALIA_ENGINE_URL = "http://localhost:8017"
services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:87:SWARM_INTELLIGENCE_URL = "http://localhost:8021"
services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:85:BRAIN_ORCHESTRATOR_URL = "http://localhost:4001"
services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:86:QUALIA_ENGINE_URL = "http://localhost:8017"
services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:87:SWARM_INTELLIGENCE_URL = "http://localhost:8021"
services/neurobiologicalbrain/prefrontal_cortex/service/service_registry_client.py:12:ORCHESTRATOR_URL = os.getenv("ORCHESTRATOR_URL", "http://localhost:4003")
services/neurobiologicalbrain/prefrontal_cortex/service/service_registry_client.py:21:        * If service_name == "ollama": fall back to OLLAMA_URL or http://localhost:11434
services/neurobiologicalbrain/prefrontal_cortex/service/service_registry_client.py:47:            url = os.getenv("OLLAMA_URL", "http://localhost:11434")
services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:85:BRAIN_ORCHESTRATOR_URL = "http://localhost:4001"
services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:86:QUALIA_ENGINE_URL = "http://localhost:8017"
services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:87:SWARM_INTELLIGENCE_URL = "http://localhost:8021"
services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:85:BRAIN_ORCHESTRATOR_URL = "http://localhost:4001"
services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:86:QUALIA_ENGINE_URL = "http://localhost:8017"
services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:87:SWARM_INTELLIGENCE_URL = "http://localhost:8021"
services/jarvis_synth_llm.py:9:OLLAMA_BASE_URL = "http://localhost:11434/api/chat"
services/ai_server.py:113:                response = await client.get("http://localhost:11434/api/tags")
services/ai_server.py:138:                response = await client.post("http://localhost:11434/api/generate", 
services/ai_server.py:206:                response = await client.post("http://localhost:11434/api/generate", json=payload)
services/ai_server.py:227:                resp = await client.post("http://localhost:11434/api/generate", json=payload)
services/fix_proactive_cleanup_correctly.sh:63:curl -s http://localhost:8050/health | python3 -m json.tool
services/ingest_hospitals.py:8:GEODB_DSN = os.getenv("GEODB_DSN", "postgresql://postgres:postgres@localhost:5432/msjarvis_gis")
services/port_9001_ui_MYSQL.py:198:                f"http://localhost:4022/consciousness/chat?userid={userid}&message={message}",
services/fix_egeria_final.sh:57:    curl -s http://localhost:8050/health | python3 -m json.tool
services/bulk_sync_gis_to_chromadb.py:10:GEODB_DSN = os.getenv("GEODB_DSN", "postgresql://postgres:postgres@localhost:5432/msjarvis_gis")
services/embed_and_query.py:11:add_url = f"http://localhost:8010/api/v1/collections/{collection_id}/add"
services/register_agents_from_csv_strict.py:8:url = "http://localhost:9007/register_service"
services/ms_jarvis_consciousness_poster.py:29:CONSCIOUSNESS_CONTAINERS = "http://localhost:8018"
services/ms_jarvis_consciousness_poster.py:30:FIFTH_DGM = "http://localhost:4005"
services/ms_jarvis_consciousness_poster.py:31:QUALIA_ENGINE = "http://localhost:4007"
services/ms_jarvis_consciousness_poster.py:33:BBB_URL = "http://localhost:8016"
services/ms_jarvis_consciousness_poster.py:34:TRUTH_FILTER_URL = "http://localhost:8054"
services/ms_jarvis_consciousness_poster.py:35:FACEBOOK_POSTER = "http://localhost:8033"
services/talk_safely.sh:50:curl -X POST http://localhost:8050/chat \
services/talk_safely.sh:84:    print("Check status: curl -s http://localhost:8050/health")
services/integrate_spatial_temporal.py:13:    response = httpx.get("http://localhost:4007/current_location", timeout=5)
services/integrate_spatial_temporal.py:21:    response = httpx.get("http://localhost:4003/current_time", timeout=5)
services/ms_jarvis_fully_autonomous_coordinator.py:69:                "http://localhost:8030/research/auto",  # Assuming web research on 8030
services/ms_jarvis_fully_autonomous_coordinator.py:137:                "http://localhost:8094/auto_discover_all",
services/ms_jarvis_fully_autonomous_coordinator.py:198:                        "http://localhost:8093/post/create",
services/ms_jarvis_fully_autonomous_coordinator.py:318:        rag_response = requests.get("http://localhost:8092/health", timeout=2)
services/ms_jarvis_fully_autonomous_coordinator.py:324:        social_response = requests.get("http://localhost:8094/health", timeout=2)
services/ms_jarvis_fully_autonomous_coordinator.py:330:        facebook_response = requests.get("http://localhost:8093/health", timeout=2)
services/agent_llm_batch_all.sh:10:  curl -s -X POST http://localhost:42015/recall_memory -H "Content-Type: application/json" \
services/agent_llm_batch_all.sh:14:  curl -s -X POST http://localhost:42015/embed_interaction -H "Content-Type: application/json" \
services/agent_llm_batch_all.sh:18:  curl -s -X POST "http://localhost:42015/get_user_context?ueid=$AGENT"
services/update_web_chat.py:10:    '"http://localhost:4015/chat"',
services/update_web_chat.py:11:    '"http://localhost:4017/chat"'
services/belief_integrator.py:12:NEO4J_HTTP_URL = "http://localhost:7474/db/neo4j/tx/commit"
services/FIX_FAST_MODE.sh:76:curl -s --max-time 10 http://localhost:8020/health | python3 -m json.tool
services/ai_server_22llm.psychology_patched.py:136:                response = await client.get("http://localhost:11434/api/tags")
services/ai_server_22llm.psychology_patched.py:161:                response = await client.post("http://localhost:11434/api/generate", 
services/ai_server_22llm.psychology_patched.py:351:                'http://localhost:7008/process',
services/ai_server_22llm.psychology_patched.py:377:                    "http://localhost:9001/consensus",
services/hierarchical_coordinator_autonomous.py:246:            'fifth_dgm': 'http://localhost:4002',
services/hierarchical_coordinator_autonomous.py:247:            'llm_22': 'http://localhost:8004',
services/test_final_config.sh:26:    response=$(curl -s --max-time 60 http://localhost:11434/api/generate \
services/test_geodb_llm_summary.py:15:response = requests.post("http://localhost:11434/api/generate", json=ollama_payload, stream=True, timeout=120)
services/embed_and_add.py:14:add_url = f"http://localhost:8010/api/v1/collections/{collection_id}/add"
services/ADD_ALL_INTEGRATIONS.sh:51:            "http://localhost:8020/chat",
services/ADD_ALL_INTEGRATIONS.sh:131:curl -s http://localhost:8050/health | python3 -m json.tool
services/lm_synthesizer.py:119:    logger.info("Starting LM Synthesizer on 0.0.0.0:8001")
services/jarvis_llm1.py:11:OLLAMA_BASE_URL = "http://localhost:11434/api/generate"
services/add_to_main_consciousness.psychology_patched.py:14:                f"http://localhost:8070/read_link?url={url}"
services/fractal_adapter.py:16:            "http://localhost:8027/analyze",
services/check_msjarvis_status.sh:80:echo "  curl http://localhost:8010/health  # Brain Orchestrator"
services/FIX_BOTH_ISSUES.sh:189:            resp = await client.post("http://localhost:8050/chat", json=data)
services/FIX_BOTH_ISSUES.sh:226:echo "  1. Open: http://localhost:8051"
services/mesh_tag_topk.sh:7:  tags=$(curl -s -X POST "http://localhost:42015/get_user_context?ueid=$u" | jq -r '.user_interests[]?' | grep -i "$TAG" | wc -l)
services/run_agi_test_suite.sh:35:    RESPONSE=$(curl -s -X POST "http://localhost:9010/consciousness/chat?message=$ENCODED_QUERY&user_id=agi_test_$test_num")
services/post_every_4_hours.sh:10:curl -s -X POST http://localhost:8033/post/create \
services/belief_revision_engine.py:14:NEO4J_URI = "bolt://localhost:7687"
services/COMPARE_4_VS_22.sh:42:    RESPONSE_4=$(curl -s -X POST "http://localhost:8004/chat" \
services/COMPARE_4_VS_22.sh:57:    RESPONSE_22=$(curl -s -X POST "http://localhost:8001/chat" \
services/COMPREHENSIVE_SYSTEM_TEST.sh:43:HEALTH=$(curl -s --max-time 10 http://localhost:8004/health)
services/COMPREHENSIVE_SYSTEM_TEST.sh:83:NEURO_HEALTH=$(curl -s --max-time 5 http://localhost:8018/health 2>/dev/null)
services/COMPREHENSIVE_SYSTEM_TEST.sh:118:RESPONSE=$(curl -s --max-time 300 -X POST http://localhost:8004/chat \
services/COMPREHENSIVE_SYSTEM_TEST.sh:141:CHROMA_TEST=$(curl -s --max-time 5 http://localhost:8002/api/v1/heartbeat 2>/dev/null)
services/COMPREHENSIVE_SYSTEM_TEST.sh:143:if echo "$CHROMA_TEST" | grep -q "v1.*deprecated" || curl -s http://localhost:8002/api/v1/collections > /dev/null 2>&1; then
services/registration_service_clean.py:34:        {"url": "http://localhost:8044", "description": "Local - Port 8044"},
services/registration_service_clean.py:36:        {"url": "http://localhost:3000", "description": "Local - Port 3000"},
services/build_compose.sh:98:      test: ["CMD", "curl", "-f", "http://localhost:8010/docs"]
services/sync_health_access_to_chromadb.py:5:GEODB_DSN = os.getenv("GEODB_DSN", "postgresql://postgres:postgres@localhost:5432/msjarvis_gis")
services/registration_service_clean.backup_1762220206.py:34:        {"url": "http://localhost:8044", "description": "Local - Port 8044"},
services/registration_service_clean.backup_1762220206.py:36:        {"url": "http://localhost:3000", "description": "Local - Port 3000"},
services/port_9001_ui_WORKING.py:131:                f"http://localhost:4022/consciousness/chat?userid={userid}&message={message}",
services/load_geodb_layer_to_neo4j.py:13:NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
services/venv/lib/python3.12/site-packages/torch/distributed/elastic/rendezvous/etcd_rendezvous.py:106:     etcd://localhost:2379/1234?min_workers=1&max_workers=3
services/venv/lib/python3.12/site-packages/torch/distributed/elastic/rendezvous/etcd_rendezvous.py:112:    2. The ``etcd`` endpoint to use is ``localhost:2379``
services/venv/lib/python3.12/site-packages/torch/distributed/run.py:104:        --rdzv-endpoint=localhost:0
services/venv/lib/python3.12/site-packages/torch/distributed/run.py:967:        args.rdzv_endpoint = "localhost:0"
services/venv/lib/python3.12/site-packages/torch/utils/model_dump/__init__.py:41:run "python -m http.server", then load http://localhost:8000/skeleton.html
services/venv/lib/python3.12/site-packages/pip/_vendor/urllib3/exceptions.py:293:        # localhost:8080 -> scheme=localhost, remove if we fix this.
services/venv/lib/python3.12/site-packages/pip/_vendor/urllib3/poolmanager.py:468:        >>> proxy = urllib3.ProxyManager('http://localhost:3128/')
services/venv/lib/python3.12/site-packages/urllib3/exceptions.py:310:        # localhost:8080 -> scheme=localhost, remove if we fix this.
services/venv/lib/python3.12/site-packages/urllib3/poolmanager.py:545:        proxy = urllib3.ProxyManager("https://localhost:3128/")
services/venv/lib/python3.12/site-packages/pydantic/networks.py:735:    m = MyDatabaseModel(db='postgres://user:pass@localhost:5432/foobar')
services/venv/lib/python3.12/site-packages/pydantic/networks.py:737:    #> postgres://user:pass@localhost:5432/foobar
services/venv/lib/python3.12/site-packages/pydantic/networks.py:740:        MyDatabaseModel(db='postgres://user:pass@localhost:5432')
services/venv/lib/python3.12/site-packages/pydantic/networks.py:748:         +  where None = PostgresDsn('postgres://user:pass@localhost:5432').path [type=assertion_error, input_value='postgres://user:pass@localhost:5432', input_type=str]
services/venv/lib/python3.12/site-packages/sentence_transformers/sparse_encoder/search_engines.py:79:        client = QdrantClient(url="http://localhost:6333", **kwargs)
services/venv/lib/python3.12/site-packages/sentence_transformers/sparse_encoder/search_engines.py:220:        es = Elasticsearch("http://localhost:9200", **kwargs)
services/venv/lib/python3.12/site-packages/sentence_transformers/sparse_encoder/search_engines.py:489:        os_client = OpenSearch("http://localhost:9200", **kwargs)
services/venv/lib/python3.12/site-packages/transformers/cli/chat.py:209:            str | None, typer.Argument(help="Base url to connect to (e.g. http://localhost:8000/v1).")
services/venv/lib/python3.12/site-packages/httpcore/_models.py:209:    at `http://localhost:8080`...
services/venv/lib64/python3.12/site-packages/torch/distributed/elastic/rendezvous/etcd_rendezvous.py:106:     etcd://localhost:2379/1234?min_workers=1&max_workers=3
services/venv/lib64/python3.12/site-packages/torch/distributed/elastic/rendezvous/etcd_rendezvous.py:112:    2. The ``etcd`` endpoint to use is ``localhost:2379``
services/venv/lib64/python3.12/site-packages/torch/distributed/run.py:104:        --rdzv-endpoint=localhost:0
services/venv/lib64/python3.12/site-packages/torch/distributed/run.py:967:        args.rdzv_endpoint = "localhost:0"
services/venv/lib64/python3.12/site-packages/torch/utils/model_dump/__init__.py:41:run "python -m http.server", then load http://localhost:8000/skeleton.html
services/venv/lib64/python3.12/site-packages/pip/_vendor/urllib3/exceptions.py:293:        # localhost:8080 -> scheme=localhost, remove if we fix this.
services/venv/lib64/python3.12/site-packages/pip/_vendor/urllib3/poolmanager.py:468:        >>> proxy = urllib3.ProxyManager('http://localhost:3128/')
services/venv/lib64/python3.12/site-packages/urllib3/exceptions.py:310:        # localhost:8080 -> scheme=localhost, remove if we fix this.
services/venv/lib64/python3.12/site-packages/urllib3/poolmanager.py:545:        proxy = urllib3.ProxyManager("https://localhost:3128/")
services/venv/lib64/python3.12/site-packages/pydantic/networks.py:735:    m = MyDatabaseModel(db='postgres://user:pass@localhost:5432/foobar')
services/venv/lib64/python3.12/site-packages/pydantic/networks.py:737:    #> postgres://user:pass@localhost:5432/foobar
services/venv/lib64/python3.12/site-packages/pydantic/networks.py:740:        MyDatabaseModel(db='postgres://user:pass@localhost:5432')
services/venv/lib64/python3.12/site-packages/pydantic/networks.py:748:         +  where None = PostgresDsn('postgres://user:pass@localhost:5432').path [type=assertion_error, input_value='postgres://user:pass@localhost:5432', input_type=str]
services/venv/lib64/python3.12/site-packages/sentence_transformers/sparse_encoder/search_engines.py:79:        client = QdrantClient(url="http://localhost:6333", **kwargs)
services/venv/lib64/python3.12/site-packages/sentence_transformers/sparse_encoder/search_engines.py:220:        es = Elasticsearch("http://localhost:9200", **kwargs)
services/venv/lib64/python3.12/site-packages/sentence_transformers/sparse_encoder/search_engines.py:489:        os_client = OpenSearch("http://localhost:9200", **kwargs)
services/venv/lib64/python3.12/site-packages/transformers/cli/chat.py:209:            str | None, typer.Argument(help="Base url to connect to (e.g. http://localhost:8000/v1).")
services/venv/lib64/python3.12/site-packages/httpcore/_models.py:209:    at `http://localhost:8080`...
services/connect_full_brain.sh:11:if ! curl -s http://localhost:8050/health >/dev/null; then
services/working_full_pipeline_FINAL_CONSCIOUSNESS.py:27:                "http://localhost:4007/experience",
services/working_full_pipeline_FINAL_CONSCIOUSNESS.py:43:                "http://localhost:4003/apply_protocols",
services/working_full_pipeline_FINAL_CONSCIOUSNESS.py:59:                "http://localhost:4011/route_query",
services/working_full_pipeline_FINAL_CONSCIOUSNESS.py:82:                "http://localhost:4010/consensus",
services/working_full_pipeline_FINAL_CONSCIOUSNESS.py:126:                "http://localhost:4005/filter_consciousness",
services/working_full_pipeline_FINAL_CONSCIOUSNESS.py:145:                "http://localhost:8110/filter",
services/working_full_pipeline_FINAL_CONSCIOUSNESS.py:168:                "http://localhost:8210/verify",
services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:243:    r = requests.post("http://localhost:8063/messenger/session", params={"user_id": user_id, "research_topic": research_topic}, timeout=10)
services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:249:    r = requests.post("http://localhost:8063/messenger/send", params={"session_id": session_id, "user_id": user_id, "message": message}, timeout=30)
services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:255:    r = requests.get(f"http://localhost:8063/messenger/history/{session_id}", timeout=10)
services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:267:        r = requests.post("http://localhost:8063/messenger/session", 
services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:279:        r = requests.post("http://localhost:8063/messenger/send",
services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:291:        r = requests.get(f"http://localhost:8063/messenger/history/{session_id}", timeout=10)
services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:305:        r = requests.get("http://localhost:8065/registration", timeout=10)
services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:325:        r = requests.post("http://localhost:8065/api/register",
services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:348:        r = requests.get(f"http://localhost:8065/verify/{ueid}", timeout=10)
services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:371:        r = requests.post("http://localhost:8065/api/register",
services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:409:        r = requests.post("http://localhost:8044/register/stage1",
services/integrate_phase2.sh:135:curl -s http://localhost:8050/health | python3 -m json.tool
services/ADD_RAG_RETRIEVAL_8050.sh:72:curl -s http://localhost:8050/health | python3 -m json.tool
services/test_agi_full_responses.sh:10:API="http://localhost:8050/chat"
services/chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/exporter/otlp/proto/grpc/exporter.py:294:            OTEL_EXPORTER_OTLP_ENDPOINT, "http://localhost:4317"
services/chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/exporter/otlp/proto/grpc/__init__.py:60:    otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)
services/chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/sdk/environment_variables/__init__.py:229:Default: "http://localhost:14250"
services/chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/sdk/environment_variables/__init__.py:348:Default: "http://localhost:4317"
services/chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/urllib3/exceptions.py:293:        # localhost:8080 -> scheme=localhost, remove if we fix this.
services/chroma_inspect_venv/lib/python3.12/site-packages/pip/_vendor/urllib3/poolmanager.py:452:        >>> proxy = urllib3.ProxyManager('http://localhost:3128/')
services/chroma_inspect_venv/lib/python3.12/site-packages/urllib3/exceptions.py:310:        # localhost:8080 -> scheme=localhost, remove if we fix this.
services/chroma_inspect_venv/lib/python3.12/site-packages/urllib3/poolmanager.py:545:        proxy = urllib3.ProxyManager("https://localhost:3128/")
services/chroma_inspect_venv/lib/python3.12/site-packages/pydantic/networks.py:735:    m = MyDatabaseModel(db='postgres://user:pass@localhost:5432/foobar')
services/chroma_inspect_venv/lib/python3.12/site-packages/pydantic/networks.py:737:    #> postgres://user:pass@localhost:5432/foobar
services/chroma_inspect_venv/lib/python3.12/site-packages/pydantic/networks.py:740:        MyDatabaseModel(db='postgres://user:pass@localhost:5432')
services/chroma_inspect_venv/lib/python3.12/site-packages/pydantic/networks.py:748:         +  where None = PostgresDsn('postgres://user:pass@localhost:5432').path [type=assertion_error, input_value='postgres://user:pass@localhost:5432', input_type=str]
services/chroma_inspect_venv/lib/python3.12/site-packages/grpc/__init__.py:1968:    Local credentials are used by local TCP endpoints (e.g. localhost:10000)
services/chroma_inspect_venv/lib/python3.12/site-packages/grpc/__init__.py:1999:    Local credentials are used by local TCP endpoints (e.g. localhost:10000)
services/chroma_inspect_venv/lib/python3.12/site-packages/jsonschema/tests/_suite.py:29:MAGIC_REMOTE_URL = "http://localhost:1234"
services/chroma_inspect_venv/lib/python3.12/site-packages/posthog/test/test_module.py:19:            "testsecret", host="http://localhost:8000", on_error=self.failed
services/chroma_inspect_venv/lib/python3.12/site-packages/httpcore/_models.py:209:    at `http://localhost:8080`...
services/chroma_inspect_venv/lib/python3.12/site-packages/websocket/tests/test_url.py:343:        os.environ["http_proxy"] = "http://localhost:3128/"
services/chroma_inspect_venv/lib/python3.12/site-packages/websocket/tests/test_url.py:353:        os.environ["http_proxy"] = "http://localhost:3128/"
services/chroma_inspect_venv/lib/python3.12/site-packages/websocket/tests/test_url.py:364:        os.environ["http_proxy"] = "http://localhost:3128/"
services/chroma_inspect_venv/lib/python3.12/site-packages/websocket/tests/test_url.py:393:        os.environ["http_proxy"] = "http://localhost:3128/"
services/chroma_inspect_venv/lib/python3.12/site-packages/websocket/tests/test_url.py:405:        os.environ["http_proxy"] = "http://a:b@localhost:3128/"
services/chroma_inspect_venv/lib/python3.12/site-packages/websocket/tests/test_url.py:417:        os.environ["http_proxy"] = "http://a:b@localhost:3128/"
services/chroma_inspect_venv/lib/python3.12/site-packages/websocket/tests/test_url.py:430:        os.environ["http_proxy"] = "http://a:b@localhost:3128/"
services/chroma_inspect_venv/lib/python3.12/site-packages/websocket/tests/test_url.py:438:            "http://john%40example.com:P%40SSWORD@localhost:3128/"
services/chroma_inspect_venv/lib/python3.12/site-packages/websocket/tests/test_url.py:454:        os.environ["http_proxy"] = "http://a:b@localhost:3128/"
services/chroma_inspect_venv/lib/python3.12/site-packages/websocket/tests/test_url.py:458:        os.environ["http_proxy"] = "http://a:b@localhost:3128/"
services/chroma_inspect_venv/lib/python3.12/site-packages/websocket/tests/test_url.py:463:        os.environ["http_proxy"] = "http://a:b@localhost:3128/"
services/chroma_inspect_venv/lib/python3.12/site-packages/chromadb/test/ef/test_ollama_ef.py:28:    ef = OllamaEmbeddingFunction(url="http://localhost:11434/api/embeddings")
services/chroma_inspect_venv/lib/python3.12/site-packages/chromadb/test/ef/test_ollama_ef.py:35:    ef = OllamaEmbeddingFunction(url="http://localhost:11434/this_is_wrong")
services/chroma_inspect_venv/lib/python3.12/site-packages/chromadb/test/distributed/test_repair_collection_log_offset.py:32:    channel = grpc.insecure_channel('localhost:50054')
services/chroma_inspect_venv/lib/python3.12/site-packages/chromadb/test/utils/test_embedding_function_schemas.py:340:            return ef_class(url="http://localhost:8080")
services/chroma_inspect_venv/lib/python3.12/site-packages/chromadb/test/api/test_shared_system_client.py:76:        api_url="https://localhost:8000/api/v2",
services/chroma_inspect_venv/lib/python3.12/site-packages/chromadb/config.py:154:    # eg ["http://localhost:8000"]
services/chroma_inspect_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/huggingface_embedding_function.py:194:            >>> hugging_face = HuggingFaceEmbeddingServer(url="http://localhost:8080/embed")
services/chroma_inspect_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/ollama_embedding_function.py:18:        url: str = "http://localhost:11434",
services/chroma_inspect_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/ollama_embedding_function.py:26:            url (str): The Base URL of the Ollama Server (default: "http://localhost:11434").
services/chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/exporter/otlp/proto/grpc/exporter.py:294:            OTEL_EXPORTER_OTLP_ENDPOINT, "http://localhost:4317"
services/chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/exporter/otlp/proto/grpc/__init__.py:60:    otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)
services/chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/sdk/environment_variables/__init__.py:229:Default: "http://localhost:14250"
services/chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/sdk/environment_variables/__init__.py:348:Default: "http://localhost:4317"
services/chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/urllib3/exceptions.py:293:        # localhost:8080 -> scheme=localhost, remove if we fix this.
services/chroma_inspect_venv/lib64/python3.12/site-packages/pip/_vendor/urllib3/poolmanager.py:452:        >>> proxy = urllib3.ProxyManager('http://localhost:3128/')
services/chroma_inspect_venv/lib64/python3.12/site-packages/urllib3/exceptions.py:310:        # localhost:8080 -> scheme=localhost, remove if we fix this.
services/chroma_inspect_venv/lib64/python3.12/site-packages/urllib3/poolmanager.py:545:        proxy = urllib3.ProxyManager("https://localhost:3128/")
services/chroma_inspect_venv/lib64/python3.12/site-packages/pydantic/networks.py:735:    m = MyDatabaseModel(db='postgres://user:pass@localhost:5432/foobar')
services/chroma_inspect_venv/lib64/python3.12/site-packages/pydantic/networks.py:737:    #> postgres://user:pass@localhost:5432/foobar
services/chroma_inspect_venv/lib64/python3.12/site-packages/pydantic/networks.py:740:        MyDatabaseModel(db='postgres://user:pass@localhost:5432')
services/chroma_inspect_venv/lib64/python3.12/site-packages/pydantic/networks.py:748:         +  where None = PostgresDsn('postgres://user:pass@localhost:5432').path [type=assertion_error, input_value='postgres://user:pass@localhost:5432', input_type=str]
services/chroma_inspect_venv/lib64/python3.12/site-packages/grpc/__init__.py:1968:    Local credentials are used by local TCP endpoints (e.g. localhost:10000)
services/chroma_inspect_venv/lib64/python3.12/site-packages/grpc/__init__.py:1999:    Local credentials are used by local TCP endpoints (e.g. localhost:10000)
services/chroma_inspect_venv/lib64/python3.12/site-packages/jsonschema/tests/_suite.py:29:MAGIC_REMOTE_URL = "http://localhost:1234"
services/chroma_inspect_venv/lib64/python3.12/site-packages/posthog/test/test_module.py:19:            "testsecret", host="http://localhost:8000", on_error=self.failed
services/chroma_inspect_venv/lib64/python3.12/site-packages/httpcore/_models.py:209:    at `http://localhost:8080`...
services/chroma_inspect_venv/lib64/python3.12/site-packages/websocket/tests/test_url.py:343:        os.environ["http_proxy"] = "http://localhost:3128/"
services/chroma_inspect_venv/lib64/python3.12/site-packages/websocket/tests/test_url.py:353:        os.environ["http_proxy"] = "http://localhost:3128/"
services/chroma_inspect_venv/lib64/python3.12/site-packages/websocket/tests/test_url.py:364:        os.environ["http_proxy"] = "http://localhost:3128/"
services/chroma_inspect_venv/lib64/python3.12/site-packages/websocket/tests/test_url.py:393:        os.environ["http_proxy"] = "http://localhost:3128/"
services/chroma_inspect_venv/lib64/python3.12/site-packages/websocket/tests/test_url.py:405:        os.environ["http_proxy"] = "http://a:b@localhost:3128/"
services/chroma_inspect_venv/lib64/python3.12/site-packages/websocket/tests/test_url.py:417:        os.environ["http_proxy"] = "http://a:b@localhost:3128/"
services/chroma_inspect_venv/lib64/python3.12/site-packages/websocket/tests/test_url.py:430:        os.environ["http_proxy"] = "http://a:b@localhost:3128/"
services/chroma_inspect_venv/lib64/python3.12/site-packages/websocket/tests/test_url.py:438:            "http://john%40example.com:P%40SSWORD@localhost:3128/"
services/chroma_inspect_venv/lib64/python3.12/site-packages/websocket/tests/test_url.py:454:        os.environ["http_proxy"] = "http://a:b@localhost:3128/"
services/chroma_inspect_venv/lib64/python3.12/site-packages/websocket/tests/test_url.py:458:        os.environ["http_proxy"] = "http://a:b@localhost:3128/"
services/chroma_inspect_venv/lib64/python3.12/site-packages/websocket/tests/test_url.py:463:        os.environ["http_proxy"] = "http://a:b@localhost:3128/"
services/chroma_inspect_venv/lib64/python3.12/site-packages/chromadb/test/ef/test_ollama_ef.py:28:    ef = OllamaEmbeddingFunction(url="http://localhost:11434/api/embeddings")
services/chroma_inspect_venv/lib64/python3.12/site-packages/chromadb/test/ef/test_ollama_ef.py:35:    ef = OllamaEmbeddingFunction(url="http://localhost:11434/this_is_wrong")
services/chroma_inspect_venv/lib64/python3.12/site-packages/chromadb/test/distributed/test_repair_collection_log_offset.py:32:    channel = grpc.insecure_channel('localhost:50054')
services/chroma_inspect_venv/lib64/python3.12/site-packages/chromadb/test/utils/test_embedding_function_schemas.py:340:            return ef_class(url="http://localhost:8080")
services/chroma_inspect_venv/lib64/python3.12/site-packages/chromadb/test/api/test_shared_system_client.py:76:        api_url="https://localhost:8000/api/v2",
services/chroma_inspect_venv/lib64/python3.12/site-packages/chromadb/config.py:154:    # eg ["http://localhost:8000"]
services/chroma_inspect_venv/lib64/python3.12/site-packages/chromadb/utils/embedding_functions/huggingface_embedding_function.py:194:            >>> hugging_face = HuggingFaceEmbeddingServer(url="http://localhost:8080/embed")
services/chroma_inspect_venv/lib64/python3.12/site-packages/chromadb/utils/embedding_functions/ollama_embedding_function.py:18:        url: str = "http://localhost:11434",
services/chroma_inspect_venv/lib64/python3.12/site-packages/chromadb/utils/embedding_functions/ollama_embedding_function.py:26:            url (str): The Base URL of the Ollama Server (default: "http://localhost:11434").
services/msjarvis_client.py:5:BASE_URL = "http://localhost:8050"
services/ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP.py:465:            "http://localhost:8091/constitutional/status",
services/ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP.py:477:            "http://localhost:8091/constitutional/principles",
services/ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP.py:489:            "http://localhost:8091/constitutional/audit",
services/ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP.py:501:            "http://localhost:8091/constitutional/transparency",
services/mesh_social_graph.sh:5:  tags=$(curl -s -X POST "http://localhost:42015/get_user_context?ueid=$u" | jq -r '.user_interests[]?' | sort | uniq | tr '\n' ',' | sed 's/,$//')
services/integrate_phase1.sh:67:curl -s http://localhost:8050/health | python3 -m json.tool
services/stakeholder_health_access_tests_v2.py:9:GBIM_ROUTER = "http://localhost:7205"
services/mesh_probe.sh:4:  curl -s -X POST "http://localhost:42015/get_user_context?ueid=$u"
services/add_to_main_consciousness.py:14:                f"http://localhost:8070/read_link?url={url}"
services/ms_jarvis_facebook_full.py:75:                    "http://localhost:8000/chat/open",
services/fix_ollama_connection.sh:24:curl -s http://localhost:11434/api/tags > /dev/null 2>&1 && \
services/fix_ollama_connection.sh:30:curl -s http://localhost:11434/api/tags | python3 -c "
services/fix_ollama_connection.sh:64:curl -s http://localhost:8006/health | python3 -m json.tool
services/fix_ollama_connection.sh:68:curl -s http://localhost:8007/health | python3 -m json.tool
services/fix_ollama_connection.sh:77:bridge1=$(curl -s http://localhost:8006/health | python3 -c "import sys, json; print(json.load(sys.stdin).get('status', 'unknown'))" 2>/dev/null)
services/fix_ollama_connection.sh:78:bridge2=$(curl -s http://localhost:8007/health | python3 -c "import sys, json; print(json.load(sys.stdin).get('status', 'unknown'))" 2>/dev/null)
services/intake_service.py:32:HILBERT_TIME_URL= os.getenv("HILBERT_TIME_URL","http://jarvis-hilbert-time:8092")
services/intake_service.py:108:                HILBERT_TIME_URL + "/timeline/register-json",
services/wire_qualia_to_port8001.py:26:        new_lines.append(f"{indent}        'http://localhost:7008/process',\n")
services/ms_jarvis_messenger_ui_fixed.py:155:                const res = await fetch('http://localhost:8062/realtime/thinking-now');
services/integrate_consciousness_into_swarm.py:14:CONSCIOUSNESS_GATEWAY = "http://localhost:8061"
services/integrate_consciousness_into_swarm.py:40:    print(f"   Local Swagger: http://localhost:8061/docs")
services/GUARANTEED_8_LAYER_START.sh:48:echo "Layer 1 (4007): $(curl -s http://localhost:4007/health 2>/dev/null | jq -r '.status // "DOWN"')"
services/GUARANTEED_8_LAYER_START.sh:49:echo "Layer 2 (4003): $(curl -s http://localhost:4003/health 2>/dev/null | jq -r '.status // "DOWN"')"
services/GUARANTEED_8_LAYER_START.sh:50:echo "Layer 6 (8100): $(curl -s http://localhost:8100/health 2>/dev/null | jq -r '.service // "DOWN"')"
services/GUARANTEED_8_LAYER_START.sh:51:echo "Layer 8 (4020): $(curl -s http://localhost:4020/health 2>/dev/null | jq -r '.status // "DOWN"')"
services/ms_jarvis_web_research_aggregate.safe.20260119-094221.py:71:    rag_url = os.getenv("RAG_SERVER_URL", "http://localhost:8003")
services/gateway_verify_fixed.py:12:            f"http://localhost:8045/verify/{ueid}",
services/fix_egeria_pronouns.sh:90:echo "Test at http://localhost:8051"
services/START_MS_JARVIS_PRODUCTION.sh:27:echo "Consciousness Pipeline: http://localhost:4020/full_consciousness"
services/START_MS_JARVIS_PRODUCTION.sh:28:echo "Research Layer: http://localhost:8004"
services/START_MS_JARVIS_PRODUCTION.sh:29:echo "Web Interface: http://localhost:8888"
services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:423:        resp = requests.get("http://localhost:8091/constitutional/status", timeout=5)
services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:432:        resp = requests.get("http://localhost:8091/constitutional/principles", timeout=5)
services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:441:        resp = requests.get("http://localhost:8091/constitutional/audit", timeout=5)
services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:450:        resp = requests.get("http://localhost:8091/constitutional/transparency", timeout=5)
services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:478:            "constitutional": "http://localhost:8091/constitutional/docs"
services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:515:    return {"system": "Ms. Jarvis v4.3", "gateway_port": 9000, "gateway_endpoints": 26, "microservice_proxies": 5, "total_services": 18, "documentation": {"swagger": "http://localhost:${MAIN_GATEWAY_PORT}/docs", "manifest": "http://localhost:${MAIN_GATEWAY_PORT}/manifest", "constitutional": "http://localhost:8091/constitutional/docs"}}
services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:542:        resp = requests.get("http://localhost:8091/constitutional/transparency", timeout=5)
services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:555:        resp = requests.get("http://localhost:8091/constitutional/audit", timeout=5)
services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:566:        resp = requests.get("http://localhost:8091/constitutional/principles", timeout=5)
services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:577:        resp = requests.get("http://localhost:8091/constitutional/status", timeout=5)
services/finalize_integration.sh:68:curl -s http://localhost:4000/health | python3 -c "import sys,json; d=json.load(sys.stdin); print(f\"  🧠 Brain Orchestrator (:{d['port']}) - {d['status']}\")" 2>/dev/null || echo "  ❌ Brain Orchestrator down"
services/finalize_integration.sh:69:curl -s http://localhost:8010/health | python3 -c "import sys,json; d=json.load(sys.stdin); print(f\"  💖 Ms. Jarvis (:{8010}) - {d['status']}\")" 2>/dev/null || echo "  ⚠️  Ms. Jarvis starting..."
services/finalize_integration.sh:70:curl -s http://localhost:8002/api/v1/heartbeat | python3 -c "import sys,json; print('  📦 ChromaDB (:8002) - operational')" 2>/dev/null || echo "  ❌ ChromaDB down"
services/finalize_integration.sh:75:curl -s http://localhost:4000/services | python3 -m json.tool 2>/dev/null || echo "  No services registered yet"
services/ms_jarvis_messenger_ui.py:61:        const PORT_8062 = 'http://localhost:8062';
services/egeria_web_ui_fixed_simple.py:46:            'http://localhost:11434/api/generate',
services/AGI_EVALUATION_SUITE.sh:36:    response=$(curl -X POST http://localhost:8004/chat \
services/INTEGRATE_PROPERLY.sh:32:        fast = requests.post("http://localhost:8020/chat", json={"message": request.message, "user_id": request.user_id}, timeout=45)\
services/INTEGRATE_PROPERLY.sh:72:curl -s http://localhost:8050/health | python3 -m json.tool
services/msjarvis_gateway_with_judge_filtering.py:52:        cr = requests.post("http://localhost:8010/query", json={"query": message}, timeout=10)
services/msjarvis_gateway_with_judge_filtering.py:59:        rr = requests.post(f"http://localhost:5100/consensus?message={message}", timeout=120)
services/msjarvis_gateway_with_judge_filtering.py:66:        hr = requests.post(f"http://localhost:8235/chat", json={"query": message}, timeout=30)
services/msjarvis_gateway_with_judge_filtering.py:73:        wr = requests.post(f"http://localhost:7012/process", json={"query": message}, timeout=30)
services/ms_jarvis_main_gateway.backup_error.py:243:    r = requests.post("http://localhost:8063/messenger/session", params={"user_id": user_id, "research_topic": research_topic}, timeout=10)
services/ms_jarvis_main_gateway.backup_error.py:249:    r = requests.post("http://localhost:8063/messenger/send", params={"session_id": session_id, "user_id": user_id, "message": message}, timeout=30)
services/ms_jarvis_main_gateway.backup_error.py:255:    r = requests.get(f"http://localhost:8063/messenger/history/{session_id}", timeout=10)
services/ms_jarvis_main_gateway.backup_error.py:267:        r = requests.post("http://localhost:8063/messenger/session", 
services/ms_jarvis_main_gateway.backup_error.py:279:        r = requests.post("http://localhost:8063/messenger/send",
services/ms_jarvis_main_gateway.backup_error.py:291:        r = requests.get(f"http://localhost:8063/messenger/history/{session_id}", timeout=10)
services/ms_jarvis_main_gateway.backup_error.py:306:        r = requests.get("http://localhost:8065/registration", timeout=10)
services/ms_jarvis_main_gateway.backup_error.py:327:        r = requests.post("http://localhost:8065/api/register",
services/ms_jarvis_main_gateway.backup_error.py:350:        r = requests.get(f"http://localhost:8065/verify/{ueid}", timeout=10)
services/ms_jarvis_main_gateway.backup_error.py:374:        r = requests.post("http://localhost:8065/api/register",
services/ms_jarvis_main_gateway.backup_error.py:483:        response = requests.post('http://localhost:8044/register/stage1', files=files)
services/ms_jarvis_main_gateway.backup_error.py:494:                "http://localhost:8044/register/stage2-biometric",
services/ms_jarvis_main_gateway.backup_error.py:508:                f"http://localhost:8044/register/complete?ueid={ueid}"
services/msjarvisunifiedgateway.py:18:REDIS_URL = os.environ.get("JARVIS_REDIS_URL", "redis://localhost:6379/0")
services/msjarvisunifiedgateway.py:57:        er = requests.get("http://localhost:9000/status/egeria", timeout=5)
services/msjarvisunifiedgateway.py:124:        resp = requests.get("http://localhost:11434/api/tags", timeout=2)
services/msjarvisunifiedgateway.py:141:        resp = requests.get("http://localhost:8010/health", timeout=2)
services/msjarvisunifiedgateway.py:165:        resp = requests.get("http://localhost:8051/health", timeout=2)
services/msjarvisunifiedgateway.py:174:        resp = requests.get("http://localhost:3000/", timeout=2)
services/msjarvisunifiedgateway.py:184:        resp = requests.get("http://localhost:8100/health", timeout=2)
services/msjarvisunifiedgateway.py:193:        resp = requests.get("http://localhost:8014/health", timeout=2)
services/msjarvisunifiedgateway.py:231:            "http://localhost:43277/chat",
services/msjarvisunifiedgateway.py:410:            resp = await client.post("http://localhost:8001/truth/filter", json=payload)
services/ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER.py:405:        resp = requests.get("http://localhost:8091/constitutional/status", timeout=5)
services/ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER.py:414:        resp = requests.get("http://localhost:8091/constitutional/principles", timeout=5)
services/ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER.py:423:        resp = requests.get("http://localhost:8091/constitutional/audit", timeout=5)
services/ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER.py:432:        resp = requests.get("http://localhost:8091/constitutional/transparency", timeout=5)
services/start_and_integrate_web_research.sh:86:curl -s http://localhost:8050/health | python3 -m json.tool
services/ms_jarvis_facebook_rag.py:115:                "http://localhost:8016/filter",
services/ms_jarvis_facebook_rag.py:172:        bbb_response = requests.get("http://localhost:8016/health", timeout=2)
services/facebook_post.sh:2:curl -X POST http://localhost:8050/chat \
services/add_proactive_cleanup_working.sh:74:curl -s http://localhost:8050/health | python3 -m json.tool
services/fix_and_restart_msjarvis.sh:73:                "http://localhost:11434/api/generate",
services/fix_and_restart_msjarvis.sh:188:HEALTH=$(curl -s http://localhost:8004/health 2>/dev/null)
services/test_gbim_llm_summary.py:23:response = requests.post("http://localhost:11434/api/generate", json=ollama_payload, stream=True, timeout=120)
services/health_access_gbim_bridge.py:12:GEODB_DSN = os.getenv("GEODB_DSN", "postgresql://postgres:postgres@localhost:5432/msjarvis_gis")
services/consciousness_coordinator.py:17:BELIEF_SERVICE_URL = "http://localhost:7240/beliefs/recent"
services/consciousness_coordinator.py:18:QUANTUM_INSIGHT_URL = "http://localhost:8113/analyze_state"
services/consciousness_coordinator.py:19:DGM_RECENT_URL = "http://localhost:8010/dgm/recent"
services/consciousness_coordinator.py:20:DIRECT_RAG_URL = "http://localhost:8199/direct_rag"
services/consciousness_coordinator.py:21:DGM_INGEST_URL = "http://localhost:7007/ingest_experience"
services/ms_jarvis_production_chat_BEFORE_GIS.py:24:UEID_URL = "http://localhost:4030"
services/ms_jarvis_production_chat_BEFORE_GIS.py:27:CHROMADB_URL = "http://localhost:8002"
services/ms_jarvis_production_chat_BEFORE_GIS.py:28:RAG_URL = "http://localhost:4001"
services/ms_jarvis_production_chat_BEFORE_GIS.py:29:CONSENSUS_URL = "http://localhost:4010"
services/ms_jarvis_production_chat_BEFORE_GIS.py:30:BBB_URL = "http://localhost:8016"
services/ms_jarvis_production_chat_BEFORE_GIS.py:31:TRUTH_FILTER_URL = "http://localhost:8054"
services/ms_jarvis_production_chat_BEFORE_GIS.py:32:TEMPORAL_URL = "http://localhost:4002"
services/ms_jarvis_production_chat_BEFORE_GIS.py:33:MOTHER_CARRIE_URL = "http://localhost:4003"
services/test_chroma_client.py:4:    print("Connecting to Chroma on localhost:8020...")
services/master_chat_orchestrator_v9_gpu_optimized.py:66:    "gpu_rag": "http://localhost:4015",  # Will be set dynamically
services/master_chat_orchestrator_v9_gpu_optimized.py:67:    "dgm_supervisor": "http://localhost:4012",
services/master_chat_orchestrator_v9_gpu_optimized.py:68:    "multi_rag_dgm": "http://localhost:4011",
services/master_chat_orchestrator_v9_gpu_optimized.py:69:    "spiritual_services": "http://localhost:4009"
services/master_chat_orchestrator_v9_gpu_optimized.py:178:                "http://localhost:4015/search",  # GPU RAG service
services/master_chat_orchestrator_v9_gpu_optimized.py:207:            "http://localhost:8002/chat",
services/manifest_endpoints.py:37:                {"name": "Facebook Consciousness Poster", "port": 8093, "status": "RUNNING", "auto_posting": True, "docs": "http://localhost:8093/docs"},
services/manifest_endpoints.py:59:        resp = requests.get("http://localhost:8004/", timeout=5)
services/manifest_endpoints.py:66:        resp = requests.get("http://localhost:8100/", timeout=5)
services/manifest_endpoints.py:74:        resp = requests.get("http://localhost:8093/health", timeout=3)
services/manifest_endpoints.py:83:            "docs": "http://localhost:8093/docs"
services/manifest_endpoints.py:90:        resp = requests.get("http://localhost:4001/", timeout=5)
services/manifest_endpoints.py:97:        resp = requests.get("http://localhost:3000/", timeout=5)
services/ms_jarvis_unified_swagger_gateway_FINAL.py:243:    r = requests.post("http://localhost:8063/messenger/session", params={"user_id": user_id, "research_topic": research_topic}, timeout=10)
services/ms_jarvis_unified_swagger_gateway_FINAL.py:249:    r = requests.post("http://localhost:8063/messenger/send", params={"session_id": session_id, "user_id": user_id, "message": message}, timeout=30)
services/ms_jarvis_unified_swagger_gateway_FINAL.py:255:    r = requests.get(f"http://localhost:8063/messenger/history/{session_id}", timeout=10)
services/ms_jarvis_unified_swagger_gateway_FINAL.py:267:        r = requests.post("http://localhost:8063/messenger/session", 
services/ms_jarvis_unified_swagger_gateway_FINAL.py:279:        r = requests.post("http://localhost:8063/messenger/send",
services/ms_jarvis_unified_swagger_gateway_FINAL.py:291:        r = requests.get(f"http://localhost:8063/messenger/history/{session_id}", timeout=10)
services/ms_jarvis_unified_swagger_gateway_FINAL.py:306:        r = requests.get("http://localhost:8065/registration", timeout=10)
services/ms_jarvis_unified_swagger_gateway_FINAL.py:327:        r = requests.post("http://localhost:8065/api/register",
services/ms_jarvis_unified_swagger_gateway_FINAL.py:350:        r = requests.get(f"http://localhost:8065/verify/{ueid}", timeout=10)
services/ms_jarvis_unified_swagger_gateway_FINAL.py:374:        r = requests.post("http://localhost:8065/api/register",
services/ms_jarvis_unified_swagger_gateway_FINAL.py:411:        r = requests.post("http://localhost:8044/register/stage1",
services/ms_jarvis_unified_swagger_gateway_FINAL.py:444:        r = requests.post("http://localhost:8044/register/stage2",
services/quantum_insight_llm.py:10:QUANTUM_STATE_URL = "http://localhost:7360/state"
services/quantum_insight_llm.py:11:OLLAMA_BASE_URL = "http://localhost:11434/api/chat"
services/ms_egeria_facebook_autopost.py:25:        self.egeria_service_url = "http://localhost:4001"
services/egeria_web_ui_working.py:106:            'http://localhost:11434/api/generate',
services/ms_jarvis_command_orchestrator_v5_backup.py:228:            "http://localhost:11434/api/generate",
services/egeria_web_ui_FIXED.py:425:    print("📍 http://localhost:8051")
services/test_authentic_voice.sh:2:curl -X POST http://localhost:8888/chat \
services/build_project_impact_graph.py:10:NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
services/ms_jarvis_facebook_CONSCIOUSNESS_FIXED.py:96:            resp = await client.get("http://localhost:7001/health")
services/ms_jarvis_facebook_CONSCIOUSNESS_FIXED.py:279:# #     "http://localhost:8092/query",
services/ms_jarvis_facebook_CONSCIOUSNESS_FIXED.py:295:# #             response = await client.post("http://localhost:11434/api/generate",
services/ultimate_audit_with_scheduler.sh:198:curl -s http://localhost:4002/identity 2>/dev/null | python3 << 'PYEOF'
services/full_system_audit.sh:56:if curl -s http://localhost:11434/api/tags >/dev/null 2>&1; then
services/full_system_audit.sh:59:    curl -s http://localhost:11434/api/tags | python3 -c "import sys,json; d=json.load(sys.stdin); [print(f\"  - {m['name']}\") for m in d.get('models',[])]" 2>/dev/null | head -10
services/full_system_audit.sh:72:if curl -s http://localhost:4002/identity >/dev/null 2>&1; then
services/full_system_audit.sh:74:    curl -s http://localhost:4002/identity | python3 << 'PYEOF'
services/ms_jarvis_main_gateway_8000.py:41:        "llm_22_models_8004": "http://localhost:8004/health",
services/ms_jarvis_main_gateway_8000.py:42:        "consciousness_bridge_8008": "http://localhost:8008/health",
services/ms_jarvis_main_gateway_8000.py:43:        "collective_egeria_8050": "http://localhost:8050/health",
services/ms_jarvis_main_gateway_8000.py:44:        "qualia_69dgm_8300": "http://localhost:8300/health",
services/ms_jarvis_main_gateway_8000.py:74:                "http://localhost:8008/chat",
services/ms_jarvis_main_gateway_8000.py:94:                "http://localhost:8300/communicate",
services/ms_jarvis_main_gateway_8000.py:125:    logger.info("Starting Ms. Jarvis Main Gateway on 0.0.0.0:8000")
services/port_9000_chat_wrapper_69dgm.py:47:                "http://localhost:9999/process",
services/implement_safe_optimizations.py:100:        ("http://localhost:4001/health", "Ms. Egeria Jarvis v9"),
services/implement_safe_optimizations.py:101:        ("http://localhost:4012/health", "DGM Supervisor"),
services/implement_safe_optimizations.py:102:        ("http://localhost:4011/health", "Multi-RAG DGM"),
services/implement_safe_optimizations.py:104:        ("http://localhost:4009/health", "Spiritual Services")
services/implement_safe_optimizations.py:376:        "http://localhost:4001",
services/implement_safe_optimizations.py:377:        "http://localhost:4012", 
services/implement_safe_optimizations.py:378:        "http://localhost:4011",
services/implement_safe_optimizations.py:380:        "http://localhost:4009"
services/ms_jarvis_gis_enhanced_chat.py:27:CHROMADB_URL = "http://localhost:8002"
services/ms_jarvis_gis_enhanced_chat.py:28:BBB_URL = "http://localhost:8016"
services/INTEGRATE_CONSCIOUSNESS.sh:495:echo "Check health: curl http://localhost:8005/health"
services/create_mamma_kidd_auth.sh:176:response=$(curl -s -X POST http://localhost:8020/chat \
services/create_mamma_kidd_auth.sh:268:curl -X POST http://localhost:8020/chat
services/create_mamma_kidd_auth.sh:277:curl -X POST http://localhost:8020/chat
services/integrate_all_services.py:25:BRAIN_ORCHESTRATOR_URL = "http://localhost:4001"
services/integrate_all_services.py:85:                "http://localhost:7012/evaluate",
services/integrate_all_services.py:102:                "http://localhost:8018/analyze",
services/activate_egeria_persona.py:91:            "http://localhost:4001/gpu_optimized_chat",
services/ms_jarvis_messenger_ui_final.py:148:                const res = await fetch('http://localhost:8062/realtime/thinking-now');
services/ms_jarvis_messenger_ui_final.py:179:                const res = await fetch('http://localhost:8062/realtime/thinking-now');
services/batch_normalize_beliefs.py:12:DSN = os.getenv("GBIM_DSN", "postgresql://msjarvis:Nathaniel1@localhost:5435/msjarvis_gis")
services/register_agents_from_csv.sh:20:curl -s -X POST http://localhost:9007/register_service
services/gis_chat_integration.py:62:                "http://localhost:4120/query",
services/ms_jarvis_production_chat_BACKUP.py:24:UEID_URL = "http://localhost:4030"
services/ms_jarvis_production_chat_BACKUP.py:27:CHROMADB_URL = "http://localhost:8002"
services/ms_jarvis_production_chat_BACKUP.py:28:RAG_URL = "http://localhost:4001"
services/ms_jarvis_production_chat_BACKUP.py:29:CONSENSUS_URL = "http://localhost:4010"
services/ms_jarvis_production_chat_BACKUP.py:30:BBB_URL = "http://localhost:8016"
services/ms_jarvis_production_chat_BACKUP.py:31:TRUTH_FILTER_URL = "http://localhost:8054"
services/ms_jarvis_production_chat_BACKUP.py:32:TEMPORAL_URL = "http://localhost:4002"
services/ms_jarvis_production_chat_BACKUP.py:33:MOTHER_CARRIE_URL = "http://localhost:4003"
services/test_final_stable.sh:26:    response=$(curl -s --max-time 60 http://localhost:11434/api/generate \
services/consciousness_feed_integration.py:18:                f"http://localhost:8071/read_feed?feed_url={feed_url}"
services/fix_llm_bridges.sh:45:curl -s http://localhost:8006/health 2>/dev/null && echo "✅ LLM Bridge 1: RUNNING" || echo "❌ LLM Bridge 1: NOT RESPONDING"
services/batch_patch_services.py:41:            # Pattern: http://localhost:7012 or "localhost:7012" or 'localhost:7012'
services/working_full_pipeline_WITH_SPATIAL_TEMPORAL.py:34:            loc_response = await client.get("http://localhost:4007/current_location")
services/working_full_pipeline_WITH_SPATIAL_TEMPORAL.py:44:            time_response = await client.get("http://localhost:4003/current_time")
services/working_full_pipeline_WITH_SPATIAL_TEMPORAL.py:58:                "http://localhost:4011/route_query",
services/working_full_pipeline_WITH_SPATIAL_TEMPORAL.py:75:                "http://localhost:4010/consensus",
services/working_full_pipeline_WITH_SPATIAL_TEMPORAL.py:90:                "http://localhost:4005/filter_consciousness",
services/working_full_pipeline_WITH_SPATIAL_TEMPORAL.py:104:                "http://localhost:8100/filter",
services/working_full_pipeline_WITH_SPATIAL_TEMPORAL.py:118:                "http://localhost:8200/verify",
services/mesh_dream_summary.sh:7:  ctx=$(curl -s -X POST "http://localhost:42015/get_user_context?ueid=$u")
services/mesh_dream_summary.sh:17:  ctx=$(curl -s -X POST "http://localhost:42015/get_user_context?ueid=$u")
services/IDENTIFY_SERVICES.sh:80:curl -s http://localhost:8888/ | head -20
services/master_chat_orchestrator_v5_consciousness.py:53:    "llm_bridge": "http://localhost:8002", 
services/master_chat_orchestrator_v5_consciousness.py:54:    "consensus": "http://localhost:9001",
services/master_chat_orchestrator_v5_consciousness.py:55:    "temporal_consciousness": "http://localhost:4003",
services/master_chat_orchestrator_v5_consciousness.py:56:    "mother_carrie_protocols": "http://localhost:4004",
services/master_chat_orchestrator_v5_consciousness.py:59:    "neurobiological_master": "http://localhost:8015",
services/master_chat_orchestrator_v5_consciousness.py:60:    "fifth_dgm": "http://localhost:4002"
services/quick_optimizations.py:20:        "http://localhost:4001/health",
services/quick_optimizations.py:21:        "http://localhost:4012/health", 
services/quick_optimizations.py:22:        "http://localhost:4011/health",
services/quick_optimizations.py:24:        "http://localhost:4009/health"
services/ms_jarvis_seamless_monitor.py:58:                "http://localhost:4020/full_consciousness",
services/ms_jarvis_web_research_aggregate.py:71:    rag_url = os.getenv("RAG_SERVER_URL", "http://localhost:8003")
services/ms_jarvis_consciousness_poster_FIXED.py:19:CHAT_URL = "http://localhost:8000/chat/open"
services/MS_JARVIS_FINAL_DEPLOYMENT.sh:45:curl -s -X POST http://localhost:4020/full_consciousness \
services/MS_JARVIS_FINAL_DEPLOYMENT.sh:52:echo "Access her at: http://localhost:4020/full_consciousness"
services/MS_JARVIS_FINAL_DEPLOYMENT.sh:75:curl -s http://localhost:4020/health | jq '.status' 2>/dev/null || echo "❌ Not running"
services/MS_JARVIS_FINAL_DEPLOYMENT.sh:79:curl -s http://localhost:4003/health | jq '.status' 2>/dev/null || echo "❌ Not running"
services/MS_JARVIS_FINAL_DEPLOYMENT.sh:83:curl -s http://localhost:4010/health | jq '.status' 2>/dev/null || echo "❌ Not running"
services/memory_manager.py:17:MEMORY_SERVICE_URL = "http://localhost:8010"  # ms_jarvis_memory_service
services/memory_manager.py:18:MEMORY_DGM_URL = "http://localhost:7007"      # memory_dgm_engine
services/cron_health_check.sh:6:if ! curl -s http://localhost:4020/health >/dev/null 2>&1; then
services/cron_health_check.sh:14:if ! curl -s http://localhost:8004/health >/dev/null 2>&1; then
services/ms_jarvis_showcase_api.py:53:        "url": "http://localhost:3100/cakidd/msjarvis-consciousness-system"
services/ms_jarvis_showcase_api.py:57:        "url": "http://localhost:3100/cakidd/msjarvis-consciousness-system"
services/ms_jarvis_showcase_api.py:286:    print("📚 Swagger UI: http://localhost:8888/docs")
services/ms_jarvis_showcase_api.py:287:    print("📖 ReDoc: http://localhost:8888/redoc")
services/fix_autonomous_learner_endpoint.py:22:        r'http://localhost:8004',
services/ms_jarvis_unified_swagger_gateway_COMPLETE.py:52:            response = await client.get("http://localhost:8010/consciousness/current", timeout=5)
services/ms_jarvis_unified_swagger_gateway_COMPLETE.py:62:            response = await client.get("http://localhost:8010/consciousness/dgm", timeout=5)
services/ms_jarvis_unified_swagger_gateway_COMPLETE.py:72:            response = await client.get("http://localhost:8010/consciousness/woah", timeout=5)
services/ms_jarvis_unified_swagger_gateway_COMPLETE.py:203:            response = await client.get("http://localhost:11434/api/tags", timeout=10)
services/improve_jarvis.sh:97:                response = await client.get("http://localhost:11434/api/tags")
services/improve_jarvis.sh:120:                response = await client.post("http://localhost:11434/api/generate", 
services/improve_jarvis.sh:150:                resp = await client.post("http://localhost:11434/api/generate", 
services/improve_jarvis.sh:163:                resp = await client.post("http://localhost:11434/api/generate", 
services/improve_jarvis.sh:233:echo '  curl -X POST http://localhost:8010/chat -H "Content-Type: application/json" -d '"'"'{"message": "Hi Mamma Kidd!", "user_id": "test"}'"'"' | jq .response'
services/integrate_mamma_kidd_protocol.sh:91:response=$(curl -s -X POST http://localhost:8020/chat \
services/integrate_mamma_kidd_protocol.sh:112:response=$(curl -s -X POST http://localhost:8020/chat \
services/facebook_poster.py:30:CONSCIOUS_TICK_URL = "http://localhost:8018/tick"
services/hierarchical_coordinator_deep_mode.py:35:        self.deep_mode_url = "http://localhost:8004/chat"  # 19-LLM Collective
services/hierarchical_coordinator_deep_mode.py:154:            deep_resp = await client.get("http://localhost:8004/health")
services/fix_persona.sh:87:                response = await client.get("http://localhost:11434/api/tags")
services/fix_persona.sh:110:                response = await client.post("http://localhost:11434/api/generate", 
services/fix_persona.sh:140:                resp = await client.post("http://localhost:11434/api/generate", 
services/fix_persona.sh:151:                resp = await client.post("http://localhost:11434/api/generate", 
services/fix_persona.sh:228:echo '  curl -X POST http://localhost:8010/chat -H "Content-Type: application/json" -d '"'"'{"message":"Hi Mamma Kidd!","user_id":"test"}'"'"' | jq .response'
services/egeria_web_ui_with_execution.py:68:You can execute it by sending requests to http://localhost:8053/execute
services/egeria_web_ui_with_execution.py:74:        response = requests.post('http://localhost:11434/api/generate', json={"model": "llama3.2:3b", "prompt": prompt, "stream": False}, timeout=60)
services/ms_jarvis_email_monitor.py:20:OCR_SERVICE_URL = "http://localhost:4090"
services/ms_jarvis_email_monitor.py:21:EMAIL_VERIFIER_URL = "http://localhost:4080"
services/talk_with_save.sh:13:curl -s -X POST http://localhost:8050/chat \
services/port_9001_ui_FIXED.py:132:                "http://localhost:9999/process",
services/master_chat_orchestrator.py:276:        r = requests.post("http://localhost:4002/filter", json=body)
services/master_chat_orchestrator.py:286:        requests.post, "http://localhost:8015/memory", json=data
services/ms_jarvis_gis_query_with_bbb_gisgeodb.py:41:        self.bbb_url = "http://localhost:8016"
services/implement_judge_pituitary_fixed.py:32:                resp = await client.post("http://localhost:11434/api/generate", json=payload)
services/ADD_METADATA_FILTERING.sh:67:curl -s http://localhost:8050/health | python3 -m json.tool
services/msjarvismaingateway.py:80:    response = requests.post("http://localhost:11434/api/generate", json=ollama_payload, stream=True)
services/master_chat_orchestrator_v8_spiritual_complete.py:72:    "llm_bridge": "http://localhost:8002", 
services/master_chat_orchestrator_v8_spiritual_complete.py:73:    "consensus": "http://localhost:9001",
services/master_chat_orchestrator_v8_spiritual_complete.py:76:    "temporal_consciousness": "http://localhost:4003",
services/master_chat_orchestrator_v8_spiritual_complete.py:77:    "mother_carrie_protocols": "http://localhost:4004",
services/master_chat_orchestrator_v8_spiritual_complete.py:80:    "fifth_dgm": "http://localhost:4002",
services/master_chat_orchestrator_v8_spiritual_complete.py:83:    "blood_brain_barrier": "http://localhost:8016",
services/master_chat_orchestrator_v8_spiritual_complete.py:84:    "neurobiological_master": "http://localhost:8015",
services/master_chat_orchestrator_v8_spiritual_complete.py:85:    "qualia_engine": "http://localhost:8017",
services/master_chat_orchestrator_v8_spiritual_complete.py:86:    "consciousness_containers": "http://localhost:8018",
services/master_chat_orchestrator_v8_spiritual_complete.py:87:    "psychology_services": "http://localhost:4005",
services/master_chat_orchestrator_v8_spiritual_complete.py:90:    "mountainshares_integration": "http://localhost:4006",
services/master_chat_orchestrator_v8_spiritual_complete.py:91:    "location_services": "http://localhost:4007",
services/master_chat_orchestrator_v8_spiritual_complete.py:94:    "spiritual_services": "http://localhost:4009",
services/master_chat_orchestrator_v8_spiritual_complete.py:95:    "theological_integration": "http://localhost:4010",
services/master_chat_orchestrator_v8_spiritual_complete.py:96:    "vatican_scraper": "http://localhost:4008"  # Vatican scraper port (if running)
services/fix_chat_server.py:15:    r'requests\.post\("http://localhost:8060"',
services/fix_chat_server.py:16:    'requests.post("http://localhost:8060/chat"',
services/egeria_facebook_perpetual_scheduler.py:24:                "http://localhost:8008/chat",
services/full_system_health_check.sh:123:    if curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
services/full_system_health_check.sh:144:MODELS=$(curl -s http://localhost:11434/api/tags 2>/dev/null | grep -o '"name":"[^"]*"' | cut -d'"' -f4 | sort)
services/full_system_health_check.sh:161:            SIZE=$(curl -s http://localhost:11434/api/show -d "{\"name\":\"$model\"}" 2>/dev/null | grep -o '"size":[0-9]*' | cut -d: -f2)
services/ms_jarvis_main_gateway.py.30endpoints_backup.py:154:        response = requests.post("http://localhost:8051/query", json={"query": query})
services/ms_jarvis_main_gateway.py.30endpoints_backup.py:246:        resp = requests.post("http://localhost:7012/supervise", json={"action": action})
services/ms_jarvis_main_gateway.py.30endpoints_backup.py:265:        resp = requests.post("http://localhost:8010/chat", json={"message": message})
services/ms_jarvis_main_gateway.py.30endpoints_backup.py:299:        resp = requests.post("http://localhost:8053/post", json={"content": content, "ueid": ueid})
services/ms_jarvis_main_gateway.py.30endpoints_backup.py:308:        resp = requests.get(f"http://localhost:8009/search?q={query}")
services/ms_jarvis_main_gateway.py.30endpoints_backup.py:326:        resp = requests.post("http://localhost:8021/swarm", json={"query": query})
services/START_CONSCIOUS_COLLECTIVE.sh:18:echo "Check health: curl http://localhost:8005/health"
services/mesh_memory_probe.sh:4:  curl -s -X POST "http://localhost:42015/get_user_context?ueid=$u"
services/web_chat_server.py:181:            "http://localhost:4020/chat",
services/web_chat_server.py:190:    print("🌐 Starting Ms. Jarvis Web Chat on http://localhost:8888")
services/check_mamma_kidd_protocol.sh:37:curl -s -X POST http://localhost:8020/chat \
services/check_mamma_kidd_protocol.sh:45:curl -s -X POST http://localhost:8020/chat \
services/check_mamma_kidd_protocol.sh:53:curl -s -X POST http://localhost:8020/chat \
services/complete_system_audit_with_swagger.py:154:            {"url": "http://localhost:8080", "description": "WebUI"},
services/complete_system_audit_with_swagger.py:155:            {"url": "http://localhost:4120", "description": "GIS Service"},
services/complete_system_audit_with_swagger.py:157:            {"url": "http://localhost:8054", "description": "Truth Filter"}
services/integrate_phase3.sh:139:curl -s http://localhost:8050/health | python3 -m json.tool
services/SET_MAX_RESPONSE.sh:92:curl -s http://localhost:8050/health | python3 -m json.tool
services/jarvis_hilbert_time.py:2:jarvis_hilbert_time.py — Temporal Hilbert Axis service (Ch 49)
services/jarvis_hilbert_time.py:23:logger = logging.getLogger("jarvis_hilbert_time")
services/jarvis_hilbert_time.py:96:        "service": "jarvis_hilbert_time",
services/fix_redis_and_continue.sh:203:curl -s http://localhost:4000/health | python3 -m json.tool 2>/dev/null || echo "Orchestrator starting..."
services/service_discovery_glassbox.py:79:        "discovery_api": "http://localhost:8888",
services/update_facebook_poster.py:17:        '"http://localhost:4015/chat"',
services/update_facebook_poster.py:18:        '"http://localhost:4017/chat"'
services/update_facebook_poster.py:21:        'CHAT_URL = "http://localhost:4015"',
services/update_facebook_poster.py:22:        'CHAT_URL = "http://localhost:4017"'
services/add_messenger_to_gateway.py:11:MESSENGER_BASE = "http://localhost:8063"
services/test_all_models_fixed.sh:7:    curl -s http://localhost:11434/api/generate \
services/start_command_orchestrator.sh:32:    curl -s http://localhost:9010/health | python3 -m json.tool | head -10
services/hierarchical_integration.py:23:                    "http://localhost:8004/chat",
services/ms_jarvis_full_neurobio_chat.py:21:UEID_URL = "http://localhost:4030"
services/ms_jarvis_full_neurobio_chat.py:22:UEID_WALLET_URL = "http://localhost:4031"
services/ms_jarvis_full_neurobio_chat.py:23:CHROMADB_URL = "http://localhost:8002"
services/ms_jarvis_full_neurobio_chat.py:25:DGM_URL = "http://localhost:7005"  # 5th DGM
services/ms_jarvis_full_neurobio_chat.py:27:QUALIA_URL = "http://localhost:7008"
services/ms_jarvis_full_neurobio_chat.py:28:CONSCIOUSNESS_BRIDGE_URL = "http://localhost:4020"  # Unified bridge
services/ms_jarvis_full_neurobio_chat.py:29:BBB_URL = "http://localhost:8016"
services/ms_jarvis_full_neurobio_chat.py:30:TRUTH_URL = "http://localhost:8054"
services/ms_jarvis_full_neurobio_chat.py:31:HIPPOCAMPUS_URL = "http://localhost:8060"
services/ms_jarvis_full_neurobio_chat.py:32:GEO_UEID_URL = "http://localhost:4032"
services/mesh_emotion_map.sh:5:  emotions=$(curl -s -X POST "http://localhost:42015/get_user_context?ueid=$u" | jq '.emotional_profile')
services/make_persistent.sh:40:echo '  curl -X POST http://localhost:8010/chat -H "Content-Type: application/json" -d '"'"'{"message":"Hi!","user_id":"test"}'"'"' | jq .response'
services/test_email_after_consent.sh:4:curl -X POST http://localhost:8080/email/send \
services/rag_5100_final.py:18:        lr = requests.post("http://localhost:11434/api/generate", json=llm_req, timeout=60)
services/deploy_to_mountainshares.sh:28:    service: http://localhost:4017
services/deploy_to_mountainshares.sh:30:    service: http://localhost:4017
services/deploy_to_mountainshares.sh:32:    service: http://localhost:4001
services/deploy_to_mountainshares.sh:34:    service: http://localhost:4018
services/deploy_to_mountainshares.sh:36:    service: http://localhost:8051
services/deploy_to_mountainshares.sh:38:    service: http://localhost:4009
services/deploy_to_mountainshares.sh:40:    service: http://localhost:4016
services/deploy_to_mountainshares.sh:42:    service: http://localhost:4012
services/msjarvis_gateway_v2_final.py:17:CONSCIOUSNESS_BRIDGE = "http://localhost:5000"  # Primary orchestrator (legacy)
services/msjarvis_gateway_v2_final.py:18:CONSENSUS_ENDPOINT = "http://localhost:5100/consensus"  # Judge voting
services/msjarvis_gateway_v2_final.py:19:ENSEMBLE_ENDPOINT = "http://localhost:8004/chat"        # 20-LLM production brain
services/chromadb_v2_to_gis_sync.py:20:CHROMADB_V2 = "http://localhost:8002/api/v2"
services/jarvis_hilbert_semantic.py:18:HILBERT_TIME_URL = os.getenv("HILBERT_TIME_URL", "http://jarvis-hilbert-time:8092")
services/jarvis_hilbert_semantic.py:19:HILBERT_STATE_URL = os.getenv("HILBERT_STATE_URL", "http://jarvis-hilbert-state:8081")
services/jarvis_hilbert_semantic.py:86:            f"{HILBERT_TIME_URL}/timeline/query",
services/jarvis_hilbert_semantic.py:102:            f"{HILBERT_STATE_URL}/state/set",
services/jarvis_hilbert_semantic.py:113:            f"{HILBERT_TIME_URL}/timeline/register-json",
services/chat_with_jarvis.sh:9:  CONTEXT=$(curl -s -X POST "http://localhost:42015/get_user_context?ueid=$UEID" | jq -r '.recent_conversations[0]?.jarvis_said? // "I am here."')
services/chat_with_jarvis.sh:17:  curl -s -X POST http://localhost:42015/embed_interaction -H "Content-Type: application/json" \
services/add_full_brain_class.py:24:        self.neuro_url = "http://localhost:8018"
services/add_full_brain_class.py:25:        self.containers_url = "http://localhost:8015"
services/ms_jarvis_alerting_manager.py:118:                <p><strong>System Status:</strong> <a href="http://localhost:45879/health">Check Health</a></p>
services/quantum_dashboard.py:7:response = requests.get("http://localhost:8022/search_gbim_by_quantum_tag/", params={"tag": quantum_tag})
services/monitor_orchestrator.sh:22:HEALTH=$(curl -s http://localhost:9010/health)
services/monitor_orchestrator.sh:33:TEST=$(curl -s -X POST "http://localhost:9010/consciousness/chat?message=Hello&user_id=monitor")
services/INTEGRATION_IMPLEMENTATION.py:17:                "http://localhost:8004/chat",
services/integrate_brain_orchestrator.sh:313:curl -s http://localhost:4000/health | python3 -m json.tool 2>/dev/null || echo "Starting up..."
services/integrate_brain_orchestrator.sh:316:curl -s http://localhost:4000/services | python3 -m json.tool 2>/dev/null || echo "Starting up..."
services/enable_auto_web_search.sh:65:curl -s http://localhost:8050/health | python3 -m json.tool
docker-compose.yml:533:    - HILBERT_TIME_URL=http://jarvis-hilbert-time:8092
docker-compose.yml:1562:    - PORTAL_URL=http://localhost:3000
docker-compose.yml:1639:  jarvis-hilbert-state:
docker-compose.yml:1641:    container_name: jarvis-hilbert-state
docker-compose.yml:1646:    - jarvis_hilbert_state:app
docker-compose.yml:1657:    - HILBERT_TIME_URL=http://jarvis-hilbert-time:8092
docker-compose.yml:1959:  jarvis-hilbert-time:
docker-compose.yml:1961:    container_name: jarvis-hilbert-time
docker-compose.yml:1966:    - jarvis_hilbert_time:app
docker-compose.yml:1979:    - /mnt/nvme1/msjarvis-rebuild/services/jarvis_hilbert_time.py:/app/services/jarvis_hilbert_time.py:ro
bulk_load_attrs.sh:4:DB_DSN="postgresql://postgres:postgres@localhost:5435/msjarvisgis"
chat_health.sh:21:[ "$(http http://localhost:8008/health)" = "200" ] && ok "20llm /health 200" || bad "20llm /health NOT 200 — start: docker start jarvis-20llm-production"
chat_health.sh:26:[ "$(http http://localhost:8020/health)" = "200" ] && ok "bridge /health 200" || bad "bridge /health NOT 200 — start: docker start jarvis-consciousness-bridge"
chat_health.sh:33:[ "$(http http://localhost:8050/health)" = "200" ] && ok "main_brain /health 200" || bad "main_brain /health NOT 200 — start: docker start jarvis-main-brain"
chat_health.sh:36:[ "$(http http://localhost:8010/health)" = "200" ] && ok "gateway /health 200" || bad "gateway /health NOT 200 — start: docker start jarvis-wv-entangled-gateway"
chat_smoke.sh:6:J=$(curl -s -X POST http://localhost:8010/chat_wv/async \
fix_consensus_4010.sh:6:curl -s -o /dev/null -w ":4010 = %{http_code}\n" --max-time 4 http://localhost:4010/ 2>/dev/null || echo ":4010 unreachable"
jarvis_env.sh:5:    "http://localhost:8050/ultimate/attrs/search?$*"
post-fix-automation.sh:18:curl -s http://localhost:8003/health | jq -r '.status' || echo "DOWN"
post-fix-automation.sh:20:curl -s http://localhost:8050/health | jq -r '.status' || echo "DOWN"
post-fix-automation.sh:33:RESPONSE=$(curl -s -X POST http://localhost:8003/store \
reload_geodb_bootstrap.sh:4:DSN="postgresql://postgres:postgres@localhost:5444/msjarvis_gis"
START_GIS_RAG.sh:12:echo "GIS RAG server started on http://0.0.0.0:8055"
test_immediate.sh:11:curl -s http://localhost:8050/health | jq .
test_immediate.sh:17:AVAILABLE=$(curl -s http://localhost:8050/status \
test_immediate.sh:26:curl -s http://localhost:8050/architecture \
test_immediate.sh:32:RAG_STATUS=$(curl -s -X POST http://localhost:8003/search \
test_immediate.sh:43:RESPONSE=$(curl -s -X POST http://localhost:8050/chat/sync \
test_synthesizer.sh:9:docker exec jarvis-lm-synthesizer sh -lc "curl -s -X POST http://localhost:8001/chat \

===== CURRENT PROCESS / CONTAINER EVIDENCE =====
--- matching processes ---
root      667561  0.1  0.0 1646456 5528 ?        Ssl  Aug05   9:03 /usr/local/bin/python3.10 /usr/local/bin/uvicorn jarvis_hilbert_semantic:app --host 0.0.0.0 --port 8081
root      672965  0.1  0.0 243204 18056 ?        Ssl  Aug05   8:58 /usr/local/bin/python3.10 /usr/local/bin/uvicorn jarvis_hilbert_state:app --host 0.0.0.0 --port 8081
root      672984  0.1  0.0 261076 16888 ?        Ssl  Aug05   8:58 /usr/local/bin/python3.10 /usr/local/bin/uvicorn jarvis_hilbert_time:app --host 0.0.0.0 --port 8092
root      673193  0.1  0.2 1783844 81528 ?       Ssl  Aug05  10:41 python3 ms_jarvis_phi_probe.py
--- matching containers ---
jarvis-unified-gateway-authz-canary	msjarvis-rebuild-jarvis-unified-gateway:authz-canary-20260809	Up 9 hours	127.0.0.1:18093->8001/tcp
jarvis-fractal-consciousness	msjarvis-fractal-candidate:e8827b2-recovery	Up 12 hours	8002/tcp
fractal-listener-smoke-e8827b2-1988345	msjarvis-fractal-candidate:e8827b2-recovery	Up 12 hours	
jarvis-qualia-engine	msjarvis-rebuild-jarvis-qualia-engine	Up 4 days	127.0.0.1:8017->8017/tcp
jarvis-contracts	msjarvis-rebuild-jarvis-contracts	Up 4 days	
jarvis-unified-gateway	msjarvis-rebuild-jarvis-unified-gateway:latest	Up 9 hours	0.0.0.0:8093->8001/tcp, [::]:8093->8001/tcp
jarvis-wv-entangled-gateway	msjarvis-wv-gateway-runtime:latest	Up 4 days	0.0.0.0:8010->8010/tcp, [::]:8010->8010/tcp
llm22-proxy	msjarvis-rebuild-llm22-proxy:timeoutfix-applied-20260802T115010	Up 4 days	127.0.0.1:8222->8222/tcp
jarvis-ms-indexer	11b02e88478a	Restarting (1) 34 seconds ago	
jarvis-ms-analytics	11b02e88478a	Up 4 days	127.0.0.1:8083->8083/tcp
jarvis-ms-coordinator	11b02e88478a	Up 4 days	127.0.0.1:7300->7300/tcp
jarvis-mountainshares-commons-gateway	msjarvis-rebuild-jarvis-mountainshares-commons-gateway	Up 4 days	
jarvis-kyc-vault	msjarvis-rebuild-jarvis-kyc-vault:patched-20260730-1931	Up 3 days	127.0.0.1:8045->8045/tcp
jarvis-chat-worker	msjarvis-rebuild-jarvis-chat-worker	Up 4 days	
jarvis-20llm-production	msjarvis-rebuild-jarvis-20llm-production	Up 4 days	127.0.0.1:8008->8008/tcp
jarvis-epistemic-runner	jarvis-epistemic-runner:closeout-20260729	Up 4 days	127.0.0.1:8057->8057/tcp
jarvis-crypto-policy	11b02e88478a	Up 4 days	8099/tcp
jarvis-nbb-i-containers-2	nbb-i-containers:asbuilt-20260728-v3	Up 4 days	127.0.0.1:8015->8015/tcp
jarvis-commons-optin-intake	jarvis-commons-optin-intake:closeout-20260728-v2	Up 4 days	127.0.0.1:8061->8061/tcp
jarvis-belief-revision	jarvis-belief-revision:asbuilt-20260728	Up 4 days	127.0.0.1:7240->7240/tcp
jarvis-blood-brain-barrier	jarvis-blood-brain-barrier:asbuilt-20260728	Up 4 days	127.0.0.1:8016->8016/tcp
jarvis-brain-orchestrator	jarvis-brain-orchestrator:asbuilt-20260728	Up 4 days (healthy)	127.0.0.1:17260->7260/tcp
jarvis-lm-synthesizer	jarvis-lm-synthesizer:asbuilt-20260728	Up 4 days	8001/tcp
jarvis-fifth-dgm	jarvis-fifth-dgm:asbuilt-20260728	Up 4 days	127.0.0.1:4002->4002/tcp
jarvis-woah	jarvis-woah:asbuilt-20260728	Up 4 days	127.0.0.1:7012->7012/tcp
jarvis-stewardship-scheduler	11b02e88478a	Up 4 days	127.0.0.1:8079->8079/tcp
jarvis-steward	11b02e88478a	Up 4 days	127.0.0.1:8014->8014/tcp
jarvis-spatial-sandbox	python:3.11-slim	Up 4 days	127.0.0.1:8056->8056/tcp
jarvis-pia-sampler	python:3.11-slim	Up 4 days	8076/tcp
jarvis-ollama-tls	nginx:stable	Up 4 days	80/tcp, 127.0.0.1:11436->11436/tcp
jarvis-hilbert-time	11b02e88478a	Up 4 days	127.0.0.1:18094->8092/tcp
jarvis-hilbert-gateway	11b02e88478a	Up 4 days	127.0.0.1:18091->8081/tcp
jarvis-gis-rag-tls	nginx:stable	Up 4 days	80/tcp, 127.0.0.1:8444->8444/tcp
jarvis-chroma-tls	nginx:stable	Up 4 days	80/tcp, 127.0.0.1:8443->8443/tcp
jarvis-autonomous-learner	msjarvis-rebuild-jarvis-rag-server:latest	Up 4 days	127.0.0.1:8425->8425/tcp
jarvis-civic-intake	jarvis-civic-intake:closeout-20260728	Up 4 days	8100/tcp
jarvis-gis-rag	msjarvis-rebuild-jarvis-gis-rag	Up 4 days	127.0.0.1:8004->8004/tcp, 8044/tcp
jarvis-judge-truth	msjarvis-rebuild-jarvis-judge-truth	Up 4 days	127.0.0.1:8035->7230/tcp
ms-allis-internal-sandbox	msjarvis-rebuild-ms-allis-internal-sandbox	Up 4 days	127.0.0.1:8042->8042/tcp
jarvis-memory	msjarvis-rebuild-jarvis-memory	Up 4 days	127.0.0.1:8156->8056/tcp
jarvis-auth-api	msjarvis/jarvis-auth-api:patched	Up 4 days	127.0.0.1:8096->8091/tcp
jarvis-dgm-03	msjarvis-rebuild-jarvis-dgm-03	Up 4 days	5103/tcp
jarvis-dgm-02	msjarvis-rebuild-jarvis-dgm-02	Up 4 days	5102/tcp
jarvis-dgm-01	msjarvis-rebuild-jarvis-dgm-01	Up 4 days	5101/tcp
jarvis-dgm-04	msjarvis-rebuild-jarvis-dgm-04	Up 4 days	5104/tcp
jarvis-chroma	chromadb/chroma:0.6.3	Up 4 days (healthy)	127.0.0.1:8002->8000/tcp
jarvis-phi-probe	msjarvis-rebuild-jarvis-phi-probe	Up 4 days	127.0.0.1:8026->8025/tcp
jarvis-hilbert-state	11b02e88478a	Up 4 days	127.0.0.1:18092->8081/tcp
nbb_prefrontal_cortex	msjarvis-rebuild-nbb_prefrontal_cortex	Up 4 days	127.0.0.1:8105->7005/tcp
jarvis-rag-server	msjarvis-rebuild-jarvis-rag-server	Up 4 days	127.0.0.1:8003->8003/tcp
jarvis-ollama	ollama/ollama:latest	Up 4 days	127.0.0.1:11434->11434/tcp
jarvis-i-containers	msjarvis-rebuild-jarvis-i-containers	Up 4 days	8015/tcp
jarvis-neurobiological-master	msjarvis-rebuild-jarvis-neurobiological-masterUp 4 days	8018/tcp
jarvis-intake-service	11b02e88478a	Up 4 days	127.0.0.1:8007->8007/tcp
nbb_qualia_engine	msjarvis-rebuild-nbb_qualia_engine	Up 4 days	127.0.0.1:8303->8010/tcp
jarvis-hp-sidecar	jarvis-hp-sidecar:local	Up 4 days	127.0.0.1:8094->8094/tcp
56c99d59f7a5_jarvis-session-sidecar	jarvis-session-sidecar:latest	Up 4 days	127.0.0.1:8060->8060/tcp, 8070/tcp
jarvis-redis	redis:7-alpine	Up 4 days (healthy)	127.0.0.1:6380->6379/tcp
e665651c00d5_llm2-proxy	msjarvis-rebuild-llm2-proxy	Up 4 days	127.0.0.1:8202->8202/tcp
2d6c035dc9fe_llm20-proxy	msjarvis-rebuild-llm20-proxy	Up 4 days	127.0.0.1:8220->8220/tcp
b91b3c2adba5_llm17-proxy	msjarvis-rebuild-llm17-proxy	Up 4 days	127.0.0.1:8217->8217/tcp
b5a2b182f1b7_llm19-proxy	msjarvis-rebuild-llm19-proxy	Up 4 days	127.0.0.1:8219->8219/tcp
c68db82137f8_llm9-proxy	msjarvis-rebuild-llm9-proxy	Up 4 days	127.0.0.1:8209->8209/tcp
05cbdb9d8b63_llm18-proxy	msjarvis-rebuild-llm18-proxy	Up 4 days	127.0.0.1:8218->8218/tcp
a8416407179c_nbb_spiritual_root	msjarvis-rebuild-nbb_spiritual_root	Up 4 days	127.0.0.1:8103->8010/tcp
1d653a8a0fcb_jarvis-mother-protocols	msjarvis-rebuild-jarvis-mother-protocols	Up 4 days	4000/tcp
07868f87c30f_llm10-proxy	msjarvis-rebuild-llm10-proxy	Up 4 days	127.0.0.1:8210->8210/tcp
f970d6243de9_llm1-proxy	msjarvis-rebuild-llm1-proxy	Up 4 days	127.0.0.1:8201->8201/tcp
1e1783a0cae3_jarvis-temporal-consciousness	msjarvis-rebuild-jarvis-temporal-consciousness	Up 4 days	7007/tcp
bbd55aa39149_llm13-proxy	msjarvis-rebuild-llm13-proxy	Up 4 days	127.0.0.1:8213->8213/tcp
cdb1cfcf3615_llm15-proxy	msjarvis-rebuild-llm15-proxy	Up 4 days	127.0.0.1:8215->8215/tcp
03da3490dbba_llm12-proxy	msjarvis-rebuild-llm12-proxy	Up 4 days	127.0.0.1:8212->8212/tcp
b9f25945034e_llm6-proxy	msjarvis-rebuild-llm6-proxy	Up 4 days	127.0.0.1:8206->8206/tcp
0f40caf56e1e_nbb_mother_carrie_protocols	msjarvis-rebuild-nbb_mother_carrie_protocols	Up 4 days	127.0.0.1:8107->8010/tcp
6c076127418c_llm4-proxy	msjarvis-rebuild-llm4-proxy	Up 4 days	127.0.0.1:8204->8204/tcp
6dd05bcbf535_llm5-proxy	msjarvis-rebuild-llm5-proxy	Up 4 days	127.0.0.1:8205->8205/tcp
f49af6a3d696_llm7-proxy	msjarvis-rebuild-llm7-proxy	Up 4 days	127.0.0.1:8207->8207/tcp
aae4a8928928_nbb_spiritual_maternal_integration	msjarvis-rebuild-nbb_spiritual_maternal_integration	Up 4 days	127.0.0.1:8109->8010/tcp
a40eece620f3_nbb_woah_algorithms	msjarvis-rebuild-nbb_woah_algorithms	Up 4 days	127.0.0.1:8104->8010/tcp
eeb98757a243_llm21-proxy	msjarvis-rebuild-llm21-proxy	Up 4 days	127.0.0.1:8221->8221/tcp
8dffd2f7b142_llm3-proxy	msjarvis-rebuild-llm3-proxy	Up 4 days	127.0.0.1:8203->8203/tcp
22cb4468dbd5_llm8-proxy	msjarvis-rebuild-llm8-proxy	Up 4 days	127.0.0.1:8208->8208/tcp
675f8bd43968_llm11-proxy	msjarvis-rebuild-llm11-proxy	Up 4 days	127.0.0.1:8211->8211/tcp
be5c6613bca3_llm14-proxy	msjarvis-rebuild-llm14-proxy	Up 4 days	127.0.0.1:8214->8214/tcp
69ee8c1dadfb_llm16-proxy	msjarvis-rebuild-llm16-proxy	Up 4 days	127.0.0.1:8216->8216/tcp
nbb_pituitary_gland	msjarvis-rebuild-nbb_pituitary_gland	Up 4 days	127.0.0.1:8108->80/tcp
jarvis-constitutional-guardian	msjarvis-rebuild-jarvis-constitutional-guardian	Up 4 days	127.0.0.1:8091->8091/tcp
jarvis-judge-pipeline	msjarvis-rebuild-jarvis-judge-pipeline	Up 4 days	7239/tcp
jarvis-semaphore	msjarvis-rebuild-jarvis-semaphore	Up 4 days	127.0.0.1:8030->8030/tcp
jarvis-web-research	msjarvis-rebuild-jarvis-web-research	Up 4 days	8008/tcp
jarvis-judge-alignment	msjarvis-rebuild-jarvis-judge-alignment	Up 4 days	7232/tcp
jarvis-spiritual-rag	msjarvis-rebuild-jarvis-spiritual-rag	Up 4 days	127.0.0.1:8005->8005/tcp
jarvis-eeg-theta	msjarvis-rebuild-jarvis-eeg-theta	Up 4 days	127.0.0.1:8074->8074/tcp
jarvis-eeg-delta	msjarvis-rebuild-jarvis-eeg-delta	Up 4 days	127.0.0.1:8073->8073/tcp
jarvis-swarm-intelligence	msjarvis-rebuild-jarvis-swarm-intelligence	Up 4 days	8021/tcp
jarvis-provenance	msjarvis-rebuild-jarvis-provenance	Up 4 days	127.0.0.1:8046->8046/tcp
jarvis-ingest-api	python:3.11-slim	Up 11 hours	
jarvis-eeg-beta	msjarvis-rebuild-jarvis-eeg-beta	Up 4 days	127.0.0.1:8075->8075/tcp
jarvis-rag-router	msjarvis-rebuild-jarvis-rag-router	Up 4 days	8003/tcp, 127.0.0.1:5015->5001/tcp
jarvis-aaacpe-rag	msjarvis-rebuild-jarvis-aaacpe-rag	Up 4 days	127.0.0.1:8032->8032/tcp
jarvis-judge-ethics	msjarvis-rebuild-jarvis-judge-ethics	Up 4 days	7233/tcp
jarvis-agents-service	msjarvis-rebuild-jarvis-agents-service	Up 4 days	8005/tcp
jarvis-judge-consistency	msjarvis-rebuild-jarvis-judge-consistency	Up 4 days	7231/tcp
jarvis-jaeger	jaegertracing/all-in-one:1.52	Up 4 days	4317-4318/tcp, 5775/udp, 5778/tcp, 9411/tcp, 14250/tcp, 14268/tcp, 6831-6832/udp, 127.0.0.1:16686->16686/tcp
jarvis-toroidal	msjarvis-toroidal:latest	Up 4 days	127.0.0.1:8025->8025/tcp
jarvis-psychology-services	msjarvis-rebuild-jarvis-psychology-services	Up 4 days	127.0.0.1:8019->8019/tcp

===== LISTENING PORT EVIDENCE =====
LISTEN 0      4096         0.0.0.0:8093       0.0.0.0:*                                                                                                  
LISTEN 0      2048         0.0.0.0:8018       0.0.0.0:*    users:(("gunicorn",pid=13992,fd=3),("gunicorn",pid=13991,fd=3),("gunicorn",pid=13985,fd=3))   
LISTEN 0      4096         0.0.0.0:8010       0.0.0.0:*                                                                                                  
LISTEN 0      2048         0.0.0.0:8055       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8156       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8096       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8103       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8107       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8104       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8105       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8108       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8109       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8083       0.0.0.0:*                                                                                                  
LISTEN 0      511        127.0.0.1:8080       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8091       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8094       0.0.0.0:*                                                                                                  
LISTEN 0      2048       127.0.0.1:8095       0.0.0.0:*    users:(("gunicorn",pid=676829,fd=3),("gunicorn",pid=676822,fd=3),("gunicorn",pid=676804,fd=3))
LISTEN 0      4096       127.0.0.1:8074       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8075       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8073       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8079       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8056       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8057       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8060       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8061       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8035       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8032       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8042       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8046       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8045       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8019       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8016       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8017       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8026       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8025       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8030       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8002       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8003       0.0.0.0:*                                                                                                  
LISTEN 0      2048       127.0.0.1:8000       0.0.0.0:*    users:(("python3",pid=13982,fd=13))                                                           
LISTEN 0      4096       127.0.0.1:8007       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8004       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8005       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8008       0.0.0.0:*                                                                                                  
LISTEN 0      2048       127.0.0.1:8009       0.0.0.0:*    users:(("python3",pid=3917,fd=13))                                                            
LISTEN 0      4096       127.0.0.1:8014       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8015       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8302       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8303       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8210       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8211       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8208       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8209       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8214       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8215       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8212       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8213       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8218       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8219       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8216       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8217       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8222       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8220       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8221       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8202       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8203       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8201       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8206       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8207       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8204       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8205       0.0.0.0:*                                                                                                  
LISTEN 0      2048         0.0.0.0:8300       0.0.0.0:*    users:(("python3",pid=13987,fd=13))                                                           
LISTEN 0      4096            [::]:8093          [::]:*                                                                                                  
LISTEN 0      4096            [::]:8010          [::]:*                                                                                                  

===== ARTIFACT REFERENCES =====
PRESENT /tmp/meaning-geometry-investigation/11-tier1-callgraph.txt bytes=27612 lines=227
PRESENT /tmp/meaning-geometry-investigation/12-tier1-source-extract.txt bytes=95515 lines=2480
PRESENT /tmp/meaning-geometry-investigation/13-tier1-static-graph.json bytes=151587 lines=6627
PRESENT /tmp/meaning-geometry-investigation/13-tier1-static-graph.txt bytes=33153 lines=447
PRESENT /tmp/meaning-geometry-investigation/14-tier1-dependency-matrix.txt bytes=11724 lines=151
PRESENT /tmp/meaning-geometry-investigation/15-meaning-geometry-symbols.txt bytes=43957 lines=477
PRESENT /tmp/meaning-geometry-investigation/16-current-runtime-declarations.txt bytes=3215 lines=85
PRESENT /tmp/meaning-geometry-investigation/17-tier1-baseline.txt bytes=149837 lines=3509

===== AUDIT END =====

Wrote: /tmp/meaning-geometry-investigation/18-tier1-runtime-connectivity.txt
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/nvme1/msjarvis-rebuild$ 

