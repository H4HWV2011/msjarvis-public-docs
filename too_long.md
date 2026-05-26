(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ # Step 1 — discover real layout, container names, and compose services
echo "=== WORKING DIR ===" && ls /opt/msjarvis-rebuild/

echo ""
echo "=== DOCKER COMPOSE FILE ===" && cat /opt/msjarvis-rebuild/docker-compose.yml 2>/dev/null || \
  cat /opt/msjarvis-rebuild/docker-compose.yaml 2>/dev/null || echo "NOT FOUND"

echo ""
echo "=== RUNNING CONTAINERS ===" && docker ps --format "table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}"

echo ""
echo "=== BACKEND DIR CONTENTS ===" && find /opt/msjarvis-rebuild -name "main.py" 2>/dev/null
find /opt/msjarvis-rebuild -name "*.py" | head -30

echo ""
echo "=== POSTGRES CONTAINER NAME ===" && docker ps --format "{{.Names}}" | grep -i postgres
=== WORKING DIR ===
'='
'\'
'$IDX'
 0
'=12.1'
 20llmFINAL.health.json
'=470,driver'
 911centers_wvdem_032819_gcs84_attrs.csv
 abis.contracts.json
 admin_cli.py
 adversarial_results_20260321_180551.json
 adversarial_results_20260321_180556.json
 adversarial_results_20260321_180608.json
 adversarial_results_20260321_180611.json
 adversarial_results_20260321_191257.json
 adversarial_results_20260321_191552.json
 adversarial_results_20260321_193201.json
 adversarial_results_20260321_194304.json
 adversarial_results_20260321_195445.json
 adversarial_results_20260321_201711.json
 adversarial_results_20260321_202552.json
 adversarial_results_20260321_203504.json
 adversarial_results_20260321_204145.json
 ai
 ai-server
 all_gis_vectors_filtered.txt
 all_gis_vectors_full.txt
 all_gis_vectors_ingest.txt
 all_gis_vectors.txt
 all_gis_vectors_unique.txt
 amtrackrails_federalrailroadadministration_200210_ll83_attrs.csv
 amtrackrails_federalrailroadadministration_200210_utm83_attrs.csv
 api_resources.py
 appservices
 _archive
 archives
 ask_gis_near_oakhill.py
 ask_gis.py
 attrs_api.py
 attrs_test.json
 attrs_with_geom_api.py
 audit_20260326_1050.txt
 auth_api.py
 auth_api.py.bak_20260426-122443
 auth_api.py.bak-cors
 autonomouslearner.py
 backfill_provenance_batch.sql
 backfill_provenance.sql
 BACKLOG_ASPIRATIONAL.md
 backup_filename_index.txt
 backup_judge_key_to_usb.sh
 _backup_llm_proxy_dockerfiles
 backup_roots.txt
 backups
 bbb-logs-20260312-160957.log
 bbb_requirements.txt
 bin
 blockgroups_census_2000_ll83_attrs.csv
 blockgroups_census_2000_utm83_attrs.csv
 blockgroups_census_201111_gcs83_attrs.csv
 blockgroups_census_2020_utm83_attrs.csv
 blockgroups_census_2020_wma84_attrs.csv
 bootstrap_gbim_beliefs_eq1.py
 boundaryappalachianbasin_wvges_1996_utm83_attrs.csv
 brain_orchestrator.py
 brain_orchestrator.py.bak
 build
 bulk_ingest_attrs.py
 bulk_ingest.log
 bulk_load_attrs.sh
'^C'
 cache_conversation_history_uuid.sh
 CACHED
 calderl_reg_ll83_attrs.csv
 call_rag_with_entanglement_example.py
 capture_gdb_json.sh
 cb-logs-20260312-160957.log
 chat_light_current.py
 check_gbim_metadata.sh
 chroma_data
 chroma_db
 chromadb
 chroma_ingestion_sources.txt
 chroma_persistent_RAG_WORKING_20260116.tgz
 chroma.sqlite3
 citieswithpopulation_2500_census_201111_utm83_attrs.csv
 citieswithpopulationover10k_census_201111_gcs83_attrs.csv
 citieswithpopulationover10k_uscensus_1990_ll83_attrs.csv
 citieswithpopulationover10k_uscensus_1990_utm83_attrs.csv
 citieswithpopulationover2500_uscensus_1990_ll83_attrs.csv
 citieswithpopulationsover10k_census_2020_utm83_attrs.csv
 citieswithpopulationsover10k_census_2020_wma84_attrs.csv
 citieswithpopulationsover2500_census_2020_utm83_attrs.csv
 citieswithpopulatoinover2500_uscensus_1990_utm83_attrs.csv
 cloudflared.config.yml
 cloudflared.deb
 coals2_ll83_attrs.csv
 coals2_utm27_attrs.csv
 coals2_utm83_attrs.csv
 communityboundary_min_att_20250121_utm83_attrs.csv
 complete_service_mapping.json
 config
 conftest.py
 consciousness_unified_bridge_EDIT.py
 consciousness_unified_bridge.py.bak
 CONSENSUS_STATS_SNAPSHOT.json
 constitutional_api.py
 conversation_history_uuid.json
 correctionalinstitutions_hsip_20091230_utm83_attrs.csv
 correctionalinstitutions_hsip_20091230_wgs84_attrs.csv
 countycityparkboundaries_20201104_utm83_attrs.csv
 countyfp20
 countyseats_usgs_ll83_attrs.csv
 countyseats_usgs_utm83_attrs.csv
 courthousescounty_manysources_200203_utm83_attrs.csv
 courthousesfederal_manysources_200203_ll83_attrs.csv
 courthousesfederal_manysources_200203_utm_attrs.csv
 crypto
 crypto-venv
 CURRENT_LLM_STACK_NOTES.txt
 CURRENTSTATUS.md
 cvfault_ll83_attrs.csv
 cvfault_utm27_attrs.csv
 cvpoly_ll83_attrs.csv
 cvpoly_utm27_attrs.csv
 cvpoly_utm83_attrs.csv
 damsnoncoal_usgs_2002_ll27_attrs.csv
 dams_usarmycorpsofengineers_200010_utm83_attrs.csv
 dams_usarmycropsofengineers_200010_ll83_attrs.csv
 data
 db
 debug_consciousness_bridge.md
 debug-logs
 debug_unified_gateway.sh
 demo_msjarvis_ranked.py
 demo_msjarvis_resources.py
 deploy-brain.sh
 deploy_gap_aware.sh
 deploy-gbim.sh
 deploy-memory.sh
 deploy-orchestrator.sh
 deploy.sh
 docker-compose-core.yml
 docker-compose-core.yml.bak.20260430-120237
 docker-compose-core.yml.bak.20260507-222001
 docker-compose-core.yml.bak.20260507-222222
 docker-compose.gbim.yml
 docker-compose.golden.bak_bbb_clean_proxy
 docker-compose.golden.bak_bbb_proxy_cmd_fix
 docker-compose.golden.bak_bbb_uvicorn_fix
 docker-compose.golden.bak_before_bbb_proxy2
 docker-compose.golden.bak_before_brain_ports_cleanup
 docker-compose.golden.bak_before_python3_cmd_fix
 docker-compose.golden.bak_nbb_base_final
 docker-compose.golden.bak_python310_compose_all
 docker-compose.golden.bak_services_mapping_fix
 docker-compose.golden.bak_web_research_cmd
 docker-compose.golden.yml
 docker-compose.llm-proxies.yml
 docker-compose.MOTHERCARRIE.BAK.20260216-132826
 docker-compose.MOTHERCARRIE.BAK.20260216-132834
 docker-compose.ollama-override.yml.disabled
 docker-compose.override.yml
 docker-compose.override.yml.bak
 docker-compose.override.yml.bak.20260430-120221
 docker-compose.override.yml.bak.20260515-230700
 docker-compose.override.yml.bak_agents
 docker-compose.override.yml.bak_depends
 docker-compose.override.yml.bak_localdb
 docker-compose.override.yml.disabled
 docker-compose-patch.yml
 docker-compose.RAG_WORKING_20260116.yml
 docker-compose.RAG_WORKING_20260116.yml.bak-20260122223705
 docker-compose.RAG_WORKING_20260116.yml.bak_gateway8050
 docker-compose.RAG_WORKING_20260116.yml.bak_mainbrain8058
 docker-compose.RAG_WORKING_20260116.yml.bak-portfix-20260122224758
 docker-compose.RAG_WORKING_20260116.yml.bak_python310_fix
 docker-compose.rag.yml
 docker-compose.recovered.yml
 docker-compose.restored.yml
 docker-compose.restored.yml.pre-hilbert-fix-1768013541
 docker-compose.restored.yml.safe-1768040125
 docker-compose.working.20260118-235132.yml
 docker-compose.working.20260119-000202.yml
 docker-compose.yml
 docker-compose.yml.20llm.bak
 docker-compose.yml.after-bbb.bak
 docker-compose.yml.backup
 docker-compose.yml.backup.1768311648
 docker-compose.yml.backup.1768313257
 docker-compose.yml.backup.1768313407
 docker-compose.yml.backup.1768786837
 docker-compose.yml.backup.1768788421
 docker-compose.yml.backup_20260215_232944
 docker-compose.yml.backup_20260218_085941
 docker-compose.yml.backup_20260318_102158
 docker-compose.yml.backup_20260318_103245
 docker-compose.yml.backup_20260318_103829
 docker-compose.yml.backup_20260318_110053
 docker-compose.yml.backup_20260318_110223
 docker-compose.yml.backup_20260318_110927
 docker-compose.yml.backup_20260323_205752
 docker-compose.yml.backup_20260323_211407
 docker-compose.yml.backup_20260406_newservices
 docker-compose.yml.backup_autonomous_learner_20260109-074048
 docker-compose.yml.backup_gateway_ports_20260109-091103
 docker-compose.yml.backup_jan13_consciousness
 docker-compose.yml.backup_nbb_ports
 docker-compose.yml.backup_nbb_ports_fixed
 docker-compose.yml.bak
 docker-compose.yml.bak.1768500857
 docker-compose.yml.bak_1768574001
 docker-compose.yml.bak.1768781706
 docker-compose.yml.bak-1768791131
 docker-compose.yml.bak-1768791194
 docker-compose.yml.bak-1768791760
 docker-compose.yml.bak_1778453637
 docker-compose.yml.bak.20260110161005
 docker-compose.yml.bak.20260206142334
 docker-compose.yml.bak.20260206142646
 docker-compose.yml.bak.20260407-221457
 docker-compose.yml.bak.20260407-221640
 docker-compose.yml.bak.20260408-173239
 docker-compose.yml.bak.20260414-210440
 docker-compose.yml.bak.20260414-210516
 docker-compose.yml.bak.20260414-210743
 docker-compose.yml.bak.20260414-211038
 docker-compose.yml.bak.20260414-211257
 docker-compose.yml.bak_20260415-111118
 docker-compose.yml.bak_20260415-111235
 docker-compose.yml.bak.20260416-141203
 docker-compose.yml.bak.20260416-141224
 docker-compose.yml.bak.20260416-141309
 docker-compose.yml.bak.20260416-141316
 docker-compose.yml.bak.20260416-141425
 docker-compose.yml.bak.20260416-141603
 docker-compose.yml.bak.20260416-141709
 docker-compose.yml.bak.20260416_144451
 docker-compose.yml.bak.20260416_144808
 docker-compose.yml.bak.20260416_145312
 docker-compose.yml.bak-20260417-144354
 docker-compose.yml.bak.20260422-204609
 docker-compose.yml.bak.20260422-204722
 docker-compose.yml.bak.20260422_220748
 docker-compose.yml.bak.20260423_095331
 docker-compose.yml.bak.20260430-115408
 docker-compose.yml.bak.20260430-202630
 docker-compose.yml.bak.20260501
 docker-compose.yml.bak.20260501-200948
 docker-compose.yml.bak.20260510-192741
 docker-compose.yml.bak.20260510-194401
 docker-compose.yml.bak.20260510-195030
 docker-compose.yml.bak.20260517-162627
 docker-compose.yml.bak.20260517-163017
 docker-compose.yml.bak.20260518-215027
 docker-compose.yml.bak.20260522_204447
 docker-compose.yml.bak.20260522T193400Z
 docker-compose.yml.bak_add_clock
 docker-compose.yml.bak_before_unified_fix
 docker-compose.yml.bak_drop_images
 docker-compose.yml.bak_drop_roche
 docker-compose.yml.bak_hilbert_cmdfix_20260415-142151
 docker-compose.yml.bak_hilbert_depsfix_20260415-142323
 docker-compose.yml.bak_hilbert_depsfix_20260415-142332
 docker-compose.yml.bak_hilbert_depsfix_20260415-142340
 docker-compose.yml.bak_ports_20260118163828
 docker-compose.yml.bak_redis_env_1769196600
 docker-compose.yml.bak_redis_fix_1769195136
 docker-compose.yml.bak_redis_fix_1769195657
 docker-compose.yml.bak_unified_cycle_fix
 docker-compose.yml.bak_woah_20260118163402
 docker-compose.yml.bbb.bak
 docker-compose.yml.before_8010_fix_1768044953
 docker-compose.yml.before_fix
 docker-compose.yml.before_fix_20260122
 docker-compose.yml.before_neuro_fix_1768012948
 docker-compose.yml.broken
 docker-compose.yml.broken-1768013498
 docker-compose.yml.broken-20260326-175632
 docker-compose.yml.broken_backup
 docker-compose.yml.BROKEN_BACKUP
 docker-compose.yml.broken_spiritual
 docker-compose.yml.chroma-backup-20260114054916
 docker-compose.yml.chroma-backup-20260114060013
 docker-compose.yml.corrupt.20260415-1601
 docker-compose.yml.full_backup_20260122
 docker-compose.yml.hilbert-experiment.20260415-163850
 docker-compose.yml.nbb.bak
 docker-compose.yml.pre_dsn_fix
 docker-compose.yml.pre-hilbert-fix-1768013541
 docker-compose.yml.pre-hilbert-image-20260415-161150
 docker-compose.yml.pre-hilbert-noports.20260415-162654
 docker-compose.yml.pre-hilbert-portfix.20260415-162529
 docker-compose.yml.pre_judges
 docker-compose.yml.pre_ollama_env_bak
 docker-compose.yml.pre-secrets-fix
 docker-compose.yml.safe-1768040125
 Dockerfile
 Dockerfile.20llm
 Dockerfile.agents
 dockerfile_backups_llm
 Dockerfile.bak_before_python3_fix
 Dockerfile.brain
 Dockerfile.brain.backup_20260309_165916
 Dockerfile.brain.backup_20260318_103552
 Dockerfile.consciousnessbridge
 Dockerfile.forge
 Dockerfile.full_neuro
 Dockerfile.gateway
 Dockerfile.gis_rag
 Dockerfile-llm10-proxy
 Dockerfile-llm11-proxy
 Dockerfile-llm12-proxy
 Dockerfile-llm13-proxy
 Dockerfile-llm14-proxy
 Dockerfile-llm15-proxy
 Dockerfile-llm16-proxy
 Dockerfile-llm17-proxy
 Dockerfile-llm18-proxy
 Dockerfile-llm19-proxy
 Dockerfile-llm1-proxy
 Dockerfile-llm20-proxy
 Dockerfile-llm21-proxy
 Dockerfile-llm22-proxy
 Dockerfile-llm2-proxy
 Dockerfile-llm3-proxy
 Dockerfile-llm4-proxy
 Dockerfile-llm5-proxy
 Dockerfile-llm6-proxy
 Dockerfile-llm7-proxy
 Dockerfile-llm8-proxy
 Dockerfile-llm9-proxy
 Dockerfile.lm_synthesizer.stub.bak
 Dockerfile.local_resources
 Dockerfile.nbb_icontainers_fastapi
 Dockerfile.neuro
 Dockerfile.neuro-prefrontal-patched
 Dockerfile.qualia
 Dockerfile.qualia.bak
 Dockerfile.rag
 Dockerfile_rag_real
 Dockerfile.rag_server
 Dockerfile.rag_server_main
 Dockerfile.ragservermain
 Dockerfile.session-sidecar
 Dockerfile.session-sidecar.bak
 Dockerfile.swarm
 Dockerfile.web_research
 Dockerfile.woah
 docs
 dump_gdb_result.sh
 dynamic_port_service_no_flask.py
 egeria-emergent.txt
 empowermentzonesandenterprisecommunitiesbytract_uscens_30c72907_attrs.csv
 empowermentzonesandenterprisecommunities_uscensus_2002_utm83_attrs.csv
 enrich_from_attrs.log
 enrich_from_attrs.py
 enrich_where.log
 enrich_where.py
 env
 error_summary.log
 etl
 eval_routed.csv
 eval_routed_final.csv
 eval_unrouted.csv
 eval_unrouted_final.csv
 example_wv_entangled_request.json
 example_wv_entangled_response.json
 excursionpassengertrains_wvdof_200102_ll83_attrs.csv
 excursionpassengertrains_wvdof_200102_utm83_attrs.csv
 export_gbim_sample.py
 exporting
 exports
 facilities_epa_200203_ll83_attrs.csv
 facilities_epa_200203_utm83_attrs.csv
 faultgl_reg_ll83_attrs.csv
 fault_reg_ll83_attrs.csv
 features_attrs.csv
 fire_departments_attrs.csv
 fire_dept_wvdem_092017_utm83_attrs.csv
 fix-20llm.sh
 fix_jarvis.log
 floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83_attrs.csv
 full_fs_indexer.sh
 gateway8050_inline.py
 gateway_chat_attempt.log
 gateway-entrypoint.sh
 gbim_backbone_rich.dump.sql
 gbim_chroma.py
 gbim_full_metadata.csv
 gbim_orchestrator.py
 gbim_sample_metadata.csv
 gbim_worldview_entity_clean.sql
 gbim_worldview_entity_data.sql
 gbim_worldview_entity_fresh.sql
 gdb_integration_service.log
 gdb_result_snapshot.json
 generate_attrs_sql.sh
 generate_spiritual_inventories.py
 geodb_collection_manifest.csv
 geodb_restore_plan.md
 geographicalnamesonusgstopomaps_usgs_200601_ll27_attrs.csv
 geographicalnamesonusgstopomaps_usgs_200601_utm83_attrs.csv
 geographicnamesonusgstopomaps_current_usgs_20110801_ll83_attrs.csv
 geographicnamesonusgstopomaps_current_usgs_20110801_utm83_attrs.csv
 geographicnamesonusgstopomaps_historical_usgs_20110801_ll83_attrs.csv
 geographicnamesonusgstopomaps_historical_usgs_20110801_utm83_attrs.csv
 geographicnamesonusgstopomaps_usgs_20110801_ll83_attrs.csv
 geographicnamesonusgstopomaps_usgs_20110801_utm83_attrs.csv
 geolgyl_reg_ll83_attrs.csv
 geolgyp_reg_ll83_attrs.csv
 geotextl_reg_ll83_attrs.csv
 gis_candidates_global.txt
 gis_candidates_stage2.txt
 gisgeodb_storage.py
 gisgeodbstorage.py
 gis_notes
 gis_pipeline_8819.log
 gis_rag_query.py
 gis_rag_server.py
 gis_rag_service.py
 gis_service
 gis_statewide_run.log
 go_no_go.sh
 hazardmitigationbuyout_20250929_polygons_utm83_attrs.csv
 hazardmitigationbuyout_20250929_polygons_wma84_attrs.csv
 healthruralfacilities_manysources_utm83_attrs.csv
 healthy-state-20260412-1126.txt
 highered_wvemd_072420_utm83_attrs.csv
 highered_wvemd_072420_wgc84_attrs.csv
 hilbert_audit_20260508_193423.log
 hilbert_audit_output.txt
 hilbert_paper_verification.sh
 hilbert_verification_20260508_193018.log
 hospitals_attrs.csv
 HOST_LEARNER_CHROMA_PATH
 impact_reg_ll83_attrs.csv
 index_gis_to_chroma.py
 index_gis_to_chroma.py.bak_20260130103111
 indexgrid15minutequads_wvgistc_ll83_attrs.csv
 indexgrid15minutequads_wvgistc_utm83_attrs.csv
 indexgrid15minutewithcounties_wvgistc_utm27_attrs.csv
 indexgrid1minutequads_wvgistc_ll83_attrs.csv
 industrialbuildings_wvdo_200807_utm83_attrs.csv
 industrialparks_wvdo_200078_utm83_attrs.csv
 industrialsites_wvdo_200807_utm83_attrs.csv
 inedexgrid1minutequads_wvgistc_utm83_attrs.csv
 infra
 ingest
 ingest_attrs_to_chroma.py
 ingest_gbimworldviewentities_from_csv.py
 ingest_kanawha_images.py
 ingest_kanawha_resources.py
 ingest.log
 ingest_missing_attrs.py
 ingest_missing.log
 ingest_msjarvis_corpus.py
 ingest_personal_pdfs.py
 ingest_wvgistc_to_chroma.py
 ingest_wv_income_maintenance_manual.py
 init_db.sql
 integration_layer
 intermodalterminalfacilities_usdot_1997_ll83_attrs.csv
 intermodalterminalfacilities_usdot_1997_utm83_attrs.csv
'[internal]'
 itest-consciousness-bridge-logs
 itest-i-containers-logs
'itus_addr AS address, -- site address'
 jarvis-20llm-openapi.json
 jarvis-chroma
 jarviscryptopolicy.py
 jarvis_eeg_delta_30s.log
 jarvis_env.sh
'[jarvis-judge-alignment'
'[jarvis-judge-alignment]'
'[jarvis-judge-consistency'
'[jarvis-judge-consistency]'
'[jarvis-judge-ethics'
'[jarvis-judge-ethics]'
'[jarvis-judge-pipeline'
'[jarvis-judge-pipeline]'
'[jarvis-judge-truth]'
'[jarvis-lm-synthesizer'
'[jarvis-lm-synthesizer]'
 judge_ethics_filter.py
 judge-keys
 judge_pipeline.py
 judge_truth_filter.py
 knowledge
 knowledge_pdfs
 KNOWN_ISSUES.md
 KNOWN_LIMITATIONS_20LLM_SEQUENTIAL.txt
 kts_ledger_import.py
 last-build-after-woah-llm22.log
 last-build-final.log
 last-build-full.log
 last-build.log
 last-build-no-llm12.log
 layer_manifest.csv
 LEARNER_STATUS.txt
 libraries_manysources_2001_ll27_attrs.csv
 libraries_manysources_2001_utm83_attrs.csv
 list_due_for_verification.py
 llm10_health_proxy.py
 llm10_health_proxy.py.bak
 llm11_health_proxy.py
 llm12_health_proxy.py
 llm12_health_proxy.py.bak
 llm13_health_proxy.py
 llm14_health_proxy.py
 llm15_health_proxy.py
 llm16_health_proxy.py
 llm17_health_proxy.py
 llm18_health_proxy.py
 llm19_health_proxy.py
 llm1_health_proxy.py
 llm20_health_proxy.py
 llm20_health_proxy.py.bak
 llm21_health_proxy.py
 llm22_health_proxy.py
 llm22_health_proxy.py.bak
 llm2_health_proxy.py
 llm2_health_proxy.py.bak
 llm3_health_proxy.py
 llm4_health_proxy.py
 llm5_health_proxy.py
 llm6_health_proxy.py
 llm7_health_proxy.py
 llm8_health_proxy.py
 llm9_health_proxy.py
 llm_consensus_20_FINAL_EDIT.py
 llm_consensus_20_FINAL.py.bak
 llm_health_proxies
 llm_servers_from_backup
 lm_judge_helper.py
 load_all_attrs_csvs.py
 load_all_attrs.sql
 load_hospitals.sql
 load_services_attrs_and_enrich.py
 local_resources_export.csv
 logs
 logs-archive
 logs-gis_rag_server_8055.log
 logs-rag_server_8003.log
 logs-rag_server_dynamic.log
 logs-rag_server.log
 main
 mainbrain.log
 main_brain.py
 main_brain.py.bak.20260511-110458
 main.py
 majorriversandlakesline_nhd_2002_ll83_attrs.csv
 majorriversandlakesline_nhd_2002_utm83_attrs.csv
 majorriversandlakespolygon_nhd_2002_poly_ll83_attrs.csv
 manufacturingandbusiness_wvdo_200803_utm83_attrs.csv
 metfacp_reg_ll83_attrs.csv
 metropolitanandmicropolitanstatisticalareas_census_201111_gcs83_attrs.csv
 metropolitanandmicropolitanstatisticalareas_census_2020_wma84_attrs.csv
 metropolitanstatisticalareas_uscensus_199901_ll83_attrs.csv
 metropolitanstatisticalareas_uscensus_199901_utm83_attrs.csv
 migrations
 mineraloperations_usgs_200204_ll83_attrs.csv
 mineraloperations_usgs_200204_utm83_attrs.csv
 minesabandonedlandsline_wvdep_1996_noprojectoin_attrs.csv
 minesabandonedlandspoint_wvdep_1996_noprojection_attrs.csv
 minesabandonedlandspolygon_wvdep_1996_noprojection_attrs.csv
 missing_collections.csv
 missing_local_files.txt
 missing_source_epochs.csv
 Modelfile.egeria
 models
 models.py
 mount_hope_data_template.json
 ms-allis-auth-install
 ms-allis-auth-install.tar.gz
 ms-allis-frontend
 ms_jarvis_blood_brain_barrier
 ms_jarvis_blood_brain_barrier.py
 ms_jarvis_blood_brain_barrier.py.bak
 msjarvis_chroma_test.py
 msjarvisconsciousnessbridge.py.bak
 ms_jarvis_contract_forge.py
 msjarvis_embed_gbim.py
 msjarvis_embed_gbim_resume_tail.py
 ms_jarvis_full_audit.sh
 ms_jarvis_psychology_services.py
 ms_jarvis_rag_server.py
 ms_jarvis_rag_server.py.bak.20260429-152039
 msjarvisragserverwvpatch.py
 msjarvis-rebuild
 msjarvis_resources.py
 ms_jarvis_unified_gateway.py
 ms_jarvis_unified_gateway.py.bak
 ms_jarvis_unified_gateway.py.bak.20260525_062445
 msjarviswoahalgorithms.py
 naming
 nationalatlasstreams_usgs_199903_ll83_attrs.csv
 nationalatlasstreams_usgs_199903_utm83_attrs.csv
 nationalregisterofhistoricplacespoints_natoinalpakrser_8d965955_attrs.csv
 nationalregisterofhistoricplacespolygons_nationaparkse_b9d30a70_attrs.csv
 nationalregister_point_20200923_attrs.csv
 nationalregister_point_20200923_utm27_attrs.csv
 nationalwaterwaynetworkports_usarmycorpsofengineers_2001_ll83_attrs.csv
 nationalwaterwaynetwork_usarmycorpsofengineers_2001_utm83_attrs.csv
 nationaregisterofhistoricplacespolygons_nationalparkse_cab42150_attrs.csv
 natoinalregisterofhistoricplacespoints_nationalparkser_ca43510e_attrs.csv
 naviagablewaterways_usarmycropsofengineers_2006_utm83_attrs.csv
 navigablewaterwaysrivermiles_usarmycropsofengineers_2006_utm83_attrs.csv
 navigablewaterwaysstructures_usarmycorpsofengineers_2006_utm83_attrs.csv
 nbb-prefrontal-full.json
 nbb_woah_algorithms_fix.patch
 neurobiological_brain
 neurobiologicalbrain
 neurobiologicalbrainicontainersservice
 neurobiologicalbrainmothercarrieprotocolsservice
 neuro-prefrontalcortex-patched.tar
 next_steps_local.sh
 nginx.conf
 nohup.out
 observability
 officebuildings_wvdo_200807_utm83_attrs.csv
 oi36a-mitigation.sh
 old_drive_gis_candidates.txt
 OPEN_ITEMS.md
 ops_history
 output
 paroleoffices_manysources_2008_utm83_attrs.csv
 paroleoffices_manysources_2008_wgs84_attrs.csv
 patch_gate.py
 patch_judges.py
 patch_llm_health_endpoints.sh
 patch_lm_synthesizer.sh
 pdf_utils.py
 persistent
 persistent_chroma_old
 pg_hba.conf
 pia-integration-check.log
 pituitary_gland.py.bak
 placesofworship_hsip_20080723_utm83_attrs.csv
 placesofworship_hsip_20080723_wgs84_attrs.csv
 policedept_wvdem_012319_gcs84_attrs.csv
 policedept_wvdem_012319_utm83_attrs.csv
 populatedplaces_census_201112_utm83_attrs.csv
 populatedplaces_census_20112_gcs83_attrs.csv
 populatedplaces_census_2020_utm83_attrs.csv
 populatedplaces_census_2020_wma84_attrs.csv
 populatedplaces_uscensus_1990_utm83_attrs.csv
 populationdatablockgroups_uscensus_2000_ll83_attrs.csv
 populationdatablockgroups_uscensus_2000_utm83_attrs.csv
 PORTING.md
 post-fix-automation.sh
 post-patch-check.txt
 pow_wvgistc_062919_utm83_attrs.csv
 pow_wvgistc_062919_wgs84_attrs.csv
 preflight_gate.sh
 preflight_gate.sh.bak
 probe_gdb_integration.sh
 processstatewidegisbulk_8819.log
 processstatewidegisbulk_.log
 process_wv_layers.py
 prometheus.yml
 proposals
 publichealthdepts_hsip_20091229_utm83_attrs.csv
 pull_jarvis_models.sh
 __pycache__
 pytest.ini
 qualia
 query_msjarvis_corpus.py
 query_msjarvis_once.py
 quick_gdb_probe.sh
 rag_insert_mountainshares.py
 rag_integration_snapshot.tgz
 rag_local_resources.py
 ragservermain.current.log
 rag_server_main.py
 ragservermain.py
 rag_server_main.py.bak.1768180485
 ragsimple.current.log
 railnetworkregion_usdot_200203_ll83_attrs.csv
 railnetworkregion_usdot_200203_utm83_attrs.csv
 railnetworkwv_usdot_200203_ll83_attrs.csv
 railnetworkwv_usdot_200203_utm83_attrs.csv
 railroads_rahalltransportationinstitute_2005_utm83_attrs.csv
 randolph_matches.sql
 reading
 README-msallis-v1.md
 realtimestreamflowstations_usgs_200012_ll27_attrs.csv
 realtimestreamflowstations_usgs_200012_utm27_attrs.csv
 realtimestreamflowstations_usgs_200012_utm83_attrs.csv
 REBUILD_COMPLETE.md
 rebuild_gis_chroma.py
 redis-init.sh
 redteam
 regionalplanninganddevelopmentcouncil_wvdo_1971_ll83_attrs.csv
 regionalplanninganddevelopmentcouncil_wvdo_1971_utm83_attrs.csv
 reingest_msjarvis_chunks.py
 reload_and_ingest_gis.sh
 reload_geodb_bootstrap.sh
 REMEDIATION_LOG_20260329.md
 requirements-69dgm.txt
 requirements-brain.txt
 requirements-gateway.txt
 requirements.txt
 resolve
 resolving
 resource_assistant.py
 resource_ranker.py
 resources
 RESTART_20LLM_FINAL.sh
 restart_unified_msjarvis.sh
 restore_missing_files.sh
 run_69dgm_orchestrator.sh
 run_9000_69dgm_bridge.sh
 run_core_ops.sh
 run_gbim_import.sh
 run_gis_stack.sh
 running_containers_20260326.txt
 running_containers_93clean_20260326.txt
 running_containers_GOLDEN_94_20260326.txt
 run_sanctuary_import.sh
 scripts
 secrets
 seed_full_knowledge.py
 seed_gbim_catalog.py
 seed_mountainshares.py
 service_build_matrix.txt
 service_discovery_no_redis.py
 service_discovery.py
 service_discovery.py.bak
 service_registry_client_stub.py
 services
 session_2026-04-19.log
 sewertreatmentplants_wvdep_200203_utm83_attrs.csv
 solidwastefacilities_wvdep_200202_ll83_attrs.csv
 solidwastefacilities_wvdep_200202_utm83_attrs.csv
 sourcetable
 spiritual_nbb_backup_20260215_231630.tar.gz
 spiritual_nbb_fix2_20260215_232031.tar.gz
 spiritual_rag_deployment_20260215_232717.tar.gz
 spiritual_rag_domain.py.tmp
 springs_wvges_1986_ll83_attrs.csv
 springs_wvges_1986_utm83_attrs.csv
 sprint3_full_20260321_200529.log
 sprint_backlog.md
 STABLE_MODE_NOTE.txt
 START20LLMFINAL.sh
 START20LLMFINAL.sh.backup.20260121180532
 START20LLMPRODUCTION.sh
 START_GIS_RAG.sh
 start-jarvis.sh
 start-jarvis.sh.bak_20260326
 start_rag_router.sh
 STARTUP.md
 stateofwvhousedistricts_wvlegislativeservices_2010_attrs.csv
 stateofwvsenatedistricts_wvlegislativeservices_2010_attrs.csv
 states_region_ll83_attrs.csv
 STATUS_MARCH15_2026_FINAL.md
 structurepolygons_samb_2003_utm83_attrs.csv
 summits_gistc_052012_utm83_shp_attrs.csv
 summits_gistc_052012_wgs84_shp_attrs.csv
 surveycontrol_nationalgeodeticsurvey_102011_gcs83_attrs.csv
 swarm_intelligence.py
 sync_chroma_metadata.py
 sync_gbim_to_chroma.py
 system_state_20260417.json
 test_autonomous_learner_store.py
 test_bbb_output.sh
 test_chatsync_gateway.sh
 test_chatsync.sh
 test_end_to_end_woah_fifthdgm.py
 test_gateway_rbac.sh
 test_immediate.sh
 test_jarvis_consciousness_bridge.sh
 test_jarvis_i_containers.sh
 test_msjarvis.golden.sh
 test_msjarvis.sh
 test_msjarvis.working.20260119-000202.sh
 test_provenance_one.sql
 test_query.sh
 test_rag_embedding_roundtrip.sh
 test_rag_image.py
 test_rag_text.py
 tests
 test-unified-gateway.sh
 test_woah_optimizer.sh
 tiger_downloads
 tl_2022_us_county.cpg
 tl_2022_us_county.dbf
 tl_2022_us_county.prj
 tl_2022_us_county.shp
 tl_2022_us_county.shp.ea.iso.xml
 tl_2022_us_county.shp.iso.xml
 tl_2022_us_county.shx
 tl_2022_us_county.zip
 tmp-aaacpe-patch
 tmp_rag_slice.py
 TODO_enable_real_entanglement.md
 tools
 towersam_fcc_200202_utm83_attrs.csv
 towersasr_fcc_200202_ll83_attrs.csv
 towersasr_fcc_200202_utm83_attrs.csv
 towerscellular_fcc_200202_ll83_attrs.csv
 towerscellular_fcc_200202_utm83_attrs.csv
 towersfm_fcc_200202_utm83_attrs.csv
 towersmicrowave_fcc_200202_ll83_attrs.csv
 towersmicrowave_fcc_200202_utm83_attrs.csv
 towerspager_fcc_200202_ll83_attrs.csv
 towerspager_fcc_200202_utm83_attrs.csv
 towers_wvpublicbroadcasting_2002_ll83_attrs.csv
 towers_wvpublicbroadcasting_2002_utm83_attrs.csv
 transferring
 ui
 ultimate8050.log
 users.json
 VERIFYANDTEST.sh
 VERIFYANDTEST.sh.bak.20260411_132002
 veteransaffairsfacilities_manysources_200503_utm83_attrs.csv
 veteransaffairsfacilities_manysources_200503_wgs84_attrs.csv
 votingdistrictswv_legislativeservices_2002_utm83_attrs.csv
 votingdistrictswv_uscensus_2000_utm83_attrs.csv
 weatherstations_nationalclimatedatacenter_1999_gcs83_attrs.csv
 weatherstations_nationalclimatedatacenter_1999_utm27_attrs.csv
 wheels
 when
 windenergyresource_nationalrenewableenergylab_200901_utm83_attrs.csv
 windenergyresource_nationalrenewableenergylab_200901_wgs84_attrs.csv
 woah_health.json
 woah_metrics_example.json
 woah_openapi.json
 woah_process_example.json
 woah_stub.py
 writing
 wv_county_boundaries_24k_topo_updated_2022_utm83_attrs.csv
 wv_entangled_context_model.py
 wv_entangled_context.schema.json
 wv_gis_layers
 wv_gis_layers_catalog.csv
 wv_gis_layers_process_status.csv
 wv_like_csv_candidates.txt
 wv_microsoft_20180207_utm17n83_attrs.csv
 wv_name_matches_current_pv.txt
 wvstatebounadary100k_usgs_200203_utm83_attrs.csv
 wvstateboundary100k_usgs_200203_ll83_attrs.csv
 wvstateboundary24k_usgs_200203_utm83_attrs.csv
 wvstatehousedistricts_manysources_1992_ll83_attrs.csv
 wvstatehousedistricts_manysources_1992_utm83_attrs.csv
 wvstatehousedistricts_manysources_2002_ll83_attrs.csv
 wvstatehousedistricts_manysources_2002_utm83_attrs.csv
 wvstatesenatedistricts_manysources_1992_ll83_attrs.csv
 wvstatesenatedistricts_manysources_1992_utm83_attrs.csv
 wvstatesenatedistricts_manysources_2002_ll83_attrs.csv
 wvstatesenatedistricts_wvlegislativeservices_2020_utm83_attrs.csv
 wv_tax_districts_ll83_attrs.csv
 wv_tax_districts_wma84_attrs.csv
 zipcodetabulationarea_census_2020_utm83_attrs.csv
 zipcodetabulationarea_census_2020_wma84_attrs.csv

=== DOCKER COMPOSE FILE ===
services:
  jarvis-unified-gateway:
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
      - BBB_URL=http://jarvis-blood-brain-barrier:8016
      - WOAH_URL=http://jarvis-woah:7012
      - TOROIDAL_URL=http://jarvis-toroidal:8025
      - FRACTAL_URL=http://jarvis-fractal-consciousness:8027
      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
      - NEURO_MASTER_URL=http://jarvis-neurobiological-master:8018
      - JARVIS_API_KEY=65ad4816de9004910599e6313fddfc2cd372e1269c20d0d4f02efd2cbbcc1a56
      - JARVIS_API_KEY_FILE=/run/secrets/jarvisapikey
      - MAX_CONCURRENT_CHATS=4
      - SERVICE_PORT=8001
      - CLOCK_TS=1767812077
      - SERVICE_PORT=8018
      - JARVIS_API_KEY=65ad4816de9004910599e6313fddfc2cd372e1269c20d0d4f02efd2cbbcc1a56
      - SERVICE_NAME=ms_jarvis_consciousness_bridge
      - SERVICE_REDIS_HOST=jarvis-redis
      - SERVICE_REDIS_PORT=6379
      - FIFTH_DGM_URL=http://jarvis-fifth-dgm:4002
      - PSYCHOLOGY_SERVICES_URL=http://jarvis-psychology-services:8019
      - PSYCHOLOGICAL_RAG_URL=http://psychological_rag_domain:9006
      - CONSTITUTIONAL_GUARDIAN_URL=http://jarvis-constitutional-guardian:8091
    depends_on:
      - jarvis-redis
      - jarvis-chroma
      - jarvis-ollama
      - jarvis-brain-orchestrator
      - jarvis-lm-synthesizer
      - jarvis-20llm-production
      - jarvis-blood-brain-barrier
      - jarvis-woah
      - jarvis-consciousness-bridge
      - jarvis-fractal-consciousness
      - jarvis-qualia-engine
      - jarvis-i-containers
      - jarvis-neurobiological-master
      - nbb-i-containers
      - nbb_consciousness_containers
      - nbb_spiritual_root
      - nbb_woah_algorithms
      - nbb_prefrontal_cortex
      - nbb_heteroglobulin_transport
      - nbb_mother_carrie_protocols
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
    volumes:
      - ./services:/app/services
    healthcheck:
      test:
        - CMD
        - python3
        - -c
        - "import urllib.request, sys; r = urllib.request.urlopen('http://127.0.0.1:8001/health', timeout=5); sys.exit(0 if r.status == 200 else 1)"
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 20s
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: "5"
    deploy:
      resources:
        limits:
          cpus: "2.0"
          memory: 4g
    secrets:
      - jarvisapikey
  jarvis-20llm-production:
    build:
      context: .
      dockerfile: Dockerfile.brain
    container_name: jarvis-20llm-production
    working_dir: /app/services
    command:
      - python3
      - ai_server_20llm_PRODUCTION.py
    expose:
      - "8008"
    ports:
      - 127.0.0.1:8008:8008
    environment:
      - SERVICE_PORT=8008
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - CLOCK_TS=1767812077
    depends_on:
      - jarvis-ollama
    networks:
      - qualia-net
    restart: unless-stopped
    volumes:
      - ./services:/app/services
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: "3"
  jarvis-wv-entangled-gateway:
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
      - 0.0.0.0
      - --port
      - "8010"
      - --log-level
      - info
    expose:
      - "8010"
    ports:
      - 127.0.0.1:8010:8010
    extra_hosts:
      - "jarvis-ollama:172.18.0.18"
    environment:
      - SERVICE_PORT=8010
      - GIS_RAG_URL=http://jarvis-gis-rag:8004
      - OLLAMA_URL=http://jarvis-ollama:11434
      - OLLAMA_MODEL=llama3.1-split:latest
      - CLOCK_TS=1767812077
    depends_on:
      - jarvis-20llm-production
    networks:
      - qualia-net
    restart: unless-stopped
    volumes:
      - ./services:/app/services
      - hf-model-cache:/root/.cache/huggingface
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: "3"
  llm1-proxy:
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
    environment:
      CLOCK_TS: 1767812077
  llm2-proxy:
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
    environment:
      CLOCK_TS: 1767812077
  llm3-proxy:
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
    environment:
      CLOCK_TS: 1767812077
  llm4-proxy:
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
    environment:
      CLOCK_TS: 1767812077
  llm5-proxy:
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
    environment:
      CLOCK_TS: 1767812077
  llm6-proxy:
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
    environment:
      CLOCK_TS: 1767812077
  llm7-proxy:
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
    environment:
      CLOCK_TS: 1767812077
  llm8-proxy:
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
    environment:
      CLOCK_TS: 1767812077
  llm9-proxy:
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
    environment:
      CLOCK_TS: 1767812077
  llm10-proxy:
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
    environment:
      CLOCK_TS: 1767812077
  llm11-proxy:
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
    environment:
      CLOCK_TS: 1767812077
  llm12-proxy:
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
    environment:
      CLOCK_TS: 1767812077
  llm13-proxy:
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
    environment:
      CLOCK_TS: 1767812077
  llm14-proxy:
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
    environment:
      CLOCK_TS: 1767812077
  llm15-proxy:
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
    environment:
      CLOCK_TS: 1767812077
  llm16-proxy:
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
    environment:
      CLOCK_TS: 1767812077
  llm17-proxy:
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
    environment:
      CLOCK_TS: 1767812077
  llm18-proxy:
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
    environment:
      CLOCK_TS: 1767812077
  llm19-proxy:
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
    environment:
      CLOCK_TS: 1767812077
  llm20-proxy:
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
    environment:
      CLOCK_TS: 1767812077
  llm21-proxy:
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
    environment:
      CLOCK_TS: 1767812077
  llm22-proxy:
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
    environment:
      CLOCK_TS: 1767812077
  jarvis-lm-synthesizer:
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
      - SERVICE_PORT=8001
      - CLOCK_TS=1767812077
    networks:
      - qualia-net
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: "3"
  jarvis-hippocampus:
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
      - "8011"
    expose:
      - "8011"
    ports:
      - 127.0.0.1:8011:8011
    environment:
      - SERVICE_PORT=8011
      - CLOCK_TS=1767812077
      - GBIM_DSN=postgresql://postgres:postgres@jarvis-local-resources-db:5432/local_resources
      - CHROMA_HOST=jarvis-chroma
      - CHROMA_PORT=8000
      - HIPPOCAMPUS_COLLECTION=geospatialfeatures
    depends_on:
      - jarvis-local-resources-db
      - jarvis-chroma
    networks:
      - qualia-net
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: "3"
  jarvis-brain-orchestrator:
    build:
      context: .
      dockerfile: Dockerfile.brain
    container_name: jarvis-brain-orchestrator
    working_dir: /app/services
    environment:
      - SERVICE_PORT=7260
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - JARVIS_API_KEY=65ad4816de9004910599e6313fddfc2cd372e1269c20d0d4f02efd2cbbcc1a56
      - CLOCK_TS=1767812077
    command:
      - python3
      - brain_orchestrator.py
    ports:
      - 127.0.0.1:17260:7260
    depends_on:
      - jarvis-ollama
      - jarvis-main-brain
    networks:
      - qualia-net
    restart: unless-stopped
    volumes:
      - ./services:/app/services
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: "3"
    healthcheck:
      test:
        - CMD
        - python3
        - -c
        - import urllib.request, sys; r = urllib.request.urlopen('http://127.0.0.1:7260/health', timeout=5); sys.exit(0 if r.status == 200 else 1)
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 30s
  jarvis-agents-service:
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
      - SERVICE_PORT=8005
      - CLOCK_TS=1767812077
    networks:
      - qualia-net
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: "3"
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
    command:
      - python
      - /app/services/ms_jarvis_consciousness_bridge.py
    volumes:
      - ./services:/app/services
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
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - SERVICE_PORT=8021
      - CLOCK_TS=1767812077
    networks:
      - qualia-net
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: "3"
  jarvis-fifth-dgm:
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
      - CLOCK_TS=1767812077
      - FIFTH_DGM_WOAH_THRESHOLD=0.7
    networks:
      - qualia-net
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: "3"
    volumes:
      - ./services:/app
  jarvis-mother-protocols:
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
  jarvis-temporal-consciousness:
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
  jarvis-69dgm-bridge:
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
    environment:
      CLOCK_TS: 1767812077
  jarvis-blood-brain-barrier:
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
      - CONSTITUTIONAL_GUARDIAN_URL=http://jarvis-constitutional-guardian:8091
    volumes:
      - ./services:/app/services
    ports:
      - "127.0.0.1:8016:8016"
    networks:
      - qualia-net
    restart: unless-stopped
    depends_on:
      - jarvis-ollama
  jarvis-woah:
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
      - CLOCK_TS=1767812077
    depends_on:
      - jarvis-ollama
    networks:
      - qualia-net
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: "3"
    volumes:
      - ./services:/app
  jarvis-consciousness-bridge:
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
      - SERVICE_PORT=8018
      - JARVIS_API_KEY=65ad4816de9004910599e6313fddfc2cd372e1269c20d0d4f02efd2cbbcc1a56
      - SERVICE_NAME=ms_jarvis_consciousness_bridge
      - SERVICE_REDIS_HOST=jarvis-redis
      - SERVICE_REDIS_PORT=6379
    volumes:
      - ./services:/app/services
    depends_on:
      - jarvis-woah
    networks:
      - qualia-net
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: "3"
  jarvis-qualia-engine:
    build:
      context: ./services
      dockerfile: Dockerfile.qualia
    container_name: jarvis-qualia-engine
    expose:
      - "8017"
    environment:
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - CLOCK_TS=1767812077
    volumes:
      - ./services/ms_jarvis_qualia_engine.py:/app/services/ms_jarvis_qualia_engine.py:ro
    depends_on:
      - jarvis-ollama
    networks:
      - qualia-net
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: "3"
  jarvis-i-containers:
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
    volumes:
      - ./services/neurobiological_brain/i_containers/i_container_1/memory_self.py:/app/neurobiological_brain/i_containers/i_container_1/memory_self.py:ro
  jarvis-semaphore:
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
  jarvis-neurobiological-master:
    build:
      context: .
      dockerfile: Dockerfile.neuro
    container_name: jarvis-neurobiological-master
    working_dir: /app/services
    command:
      - python3
      - ms_jarvis_neurobiological_master.py
    expose:
      - "8018"
    environment:
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - QUALIA_URL=http://jarvis-qualia-engine:8017
      - I_CONTAINERS_URL=http://jarvis-i-containers:8015
      - CLOCK_TS=1767812077
    depends_on:
      - jarvis-blood-brain-barrier
      - jarvis-qualia-engine
      - jarvis-i-containers
    networks:
      - qualia-net
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: "3"
  jarvis-fractal-consciousness:
    build:
      context: ./services
    container_name: jarvis-fractal-consciousness
    expose:
      - "8027"
    environment:
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - CLOCK_TS=1767812077
    volumes:
      - ./services/msjarvis_fractal_consciousness.py:/app/msjarvis_fractal_consciousness.py:ro
    depends_on:
      - jarvis-ollama
    networks:
      - qualia-net
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: "3"
  jarvis-autonomous-learner:
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
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - CHROMA_HOST=jarvis-chroma
      - CHROMA_PORT=8000
      - SERVICE_PORT=8020
      - CLOCK_TS=1767812077
    volumes:
      - ./services:/app/services:rw
    depends_on:
      - jarvis-chroma
    networks:
      - qualia-net
    restart: unless-stopped
  jarvis-ollama:
    image: ollama/ollama:latest
    container_name: jarvis-ollama
    ports:
      - 127.0.0.1:11434:11434
    environment:
      - OLLAMA_MODELS=/root/.ollama/models
      - OLLAMA_KEEP_ALIVE=1m
      - OLLAMA_MAX_LOADED_MODELS=1
      - OLLAMA_NUM_PARALLEL=1
      - OLLAMA_FLASH_ATTENTION=1
      - CLOCK_TS=1767812077
    volumes:
      - /mnt/ssd2/msjarvis_secondary/models:/root/.ollama/models
    networks:
      - qualia-net
    restart: unless-stopped
    runtime: nvidia
    logging:
      driver: json-file
      options:
        max-size: 50m
        max-file: "5"
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
        limits:
          cpus: "8.0"
          memory: 28g
  jarvis-redis:
    image: redis:7-alpine
    container_name: jarvis-redis
    ports:
      - 127.0.0.1:6380:6379
    networks:
      - qualia-net
    restart: always
    healthcheck:
      test:
        - CMD
        - redis-cli
        - ping
      interval: 30s
      timeout: 10s
      retries: 3
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: "3"
    environment:
      CLOCK_TS: 1767812077
  jarvis-chroma:
    image: chromadb/chroma:latest
    container_name: jarvis-chroma
    ports:
      - 127.0.0.1:8002:8000
    environment:
      - ISPERSISTENT=TRUE
      - UVICORN_ACCESS_LOG=0
      - UVICORN_LOG_LEVEL=warning
      - PERSIST_DIRECTORY=/data
      - CLOCK_TS=1767812077
    volumes:
      - /mnt/nvme1/msjarvis-data/chroma-live:/data
    restart: always
    networks:
      - qualia-net
    healthcheck:
      test:
        - CMD
        - /bin/bash
        - -c
        - cat < /dev/null > /dev/tcp/localhost/8000
      interval: 30s
      timeout: 10s
      retries: 3
    logging:
      driver: json-file
      options:
        max-size: 20m
        max-file: "3"
  nbb-i-containers:
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
           - nbb_i-containers
    restart: "no"
    environment:
      CLOCK_TS: 1767812077
      NBB_ICONTAINERS_URL: http://nbb-i-containers:7005
  nbb_consciousness_containers:
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
      JARVIS_API_KEY: 65ad4816de9004910599e6313fddfc2cd372e1269c20d0d4f02efd2cbbcc1a56
      JARVIS_API_KEY_FILE: /run/secrets/jarvisapikey
  nbb_spiritual_root:
    build: ./neurobiological_brain/spiritual_root/service
    ports:
      - 127.0.0.1:8103:8010
    networks:
      - qualia-net
    restart: unless-stopped
    environment:
      SERVICE_PORT: "8010"
      JARVIS_API_KEY: 65ad4816de9004910599e6313fddfc2cd372e1269c20d0d4f02efd2cbbcc1a56
      JARVIS_API_KEY_FILE: /run/secrets/jarvisapikey
      CLOCK_TS: 1767812077
  nbb_woah_algorithms:
    build: ./neurobiological_brain/woah_algorithms/service
    ports:
      - 127.0.0.1:8104:8010
    networks:
      - qualia-net
    restart: unless-stopped
    environment:
      CLOCK_TS: 1767812077
      JARVIS_API_KEY: 65ad4816de9004910599e6313fddfc2cd372e1269c20d0d4f02efd2cbbcc1a56
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
      JARVIS_API_KEY: 65ad4816de9004910599e6313fddfc2cd372e1269c20d0d4f02efd2cbbcc1a56
      JARVIS_API_KEY_FILE: /run/secrets/jarvisapikey
      SERVICE_REDIS_ENABLED: "true"
  nbb_heteroglobulin_transport:
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
      JARVIS_API_KEY: 65ad4816de9004910599e6313fddfc2cd372e1269c20d0d4f02efd2cbbcc1a56
      JARVIS_API_KEY_FILE: /run/secrets/jarvisapikey
      SERVICE_REDIS_ENABLED: "true"
  nbb_mother_carrie_protocols:
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
      JARVIS_API_KEY: 65ad4816de9004910599e6313fddfc2cd372e1269c20d0d4f02efd2cbbcc1a56
      JARVIS_API_KEY_FILE: /run/secrets/jarvisapikey
      SERVICE_REDIS_ENABLED: "true"
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
      JARVIS_API_KEY: 65ad4816de9004910599e6313fddfc2cd372e1269c20d0d4f02efd2cbbcc1a56
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
      JARVIS_API_KEY: 65ad4816de9004910599e6313fddfc2cd372e1269c20d0d4f02efd2cbbcc1a56
      JARVIS_API_KEY_FILE: /run/secrets/jarvisapikey
      SERVICE_REDIS_ENABLED: "true"
  nbb_darwin_godel_machines:
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
      JARVIS_API_KEY: 65ad4816de9004910599e6313fddfc2cd372e1269c20d0d4f02efd2cbbcc1a56
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
      JARVIS_API_KEY: 65ad4816de9004910599e6313fddfc2cd372e1269c20d0d4f02efd2cbbcc1a56
      JARVIS_API_KEY_FILE: /run/secrets/jarvisapikey
  neo4j:
    image: neo4j:5.13-community
    container_name: neo4j
    ports:
      - 127.0.0.1:7687:7687
      - 127.0.0.1:7475:7474
    environment:
      - NEO4J_ACCEPT_LICENSE_AGREEMENT=yes
      - NEO4J_AUTH=neo4j/neo4jpassword
      - CLOCK_TS=1767812077
    restart: unless-stopped
    networks:
      - qualia-net
  mysql:
    image: mysql:8.2
    container_name: mysql
    environment:
      - MYSQL_ROOT_PASSWORD=my_secret_root_pw
      - MYSQL_DATABASE=quantum_ai
      - MYSQL_USER=msjarvis
      - MYSQL_PASSWORD=j4rv1sgeo!
      - CLOCK_TS=1767812077
    ports:
      - 127.0.0.1:3307:3306
    volumes:
      - ./data/mysql:/var/lib/mysql
    restart: always
    networks:
      - qualia-net
  ipfs:
    image: ipfs/kubo:latest
    container_name: ipfs
    ports:
      - 127.0.0.1:5001:5001
    volumes:
      - ./data/ipfs:/data/ipfs
    restart: unless-stopped
    networks:
      - qualia-net
    environment:
      CLOCK_TS: 1767812077
  jarvis-main-brain:
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
      - --host
      - 0.0.0.0
      - --port
      - "8050"
      - --proxy-headers
      - --forwarded-allow-ips=*
    env_file:
      - .env
    expose:
      - "8050"
    ports:
      - 127.0.0.1:8050:8050
    environment:
      - SERVICE_PORT=8050
      - JARVIS_API_KEY=65ad4816de9004910599e6313fddfc2cd372e1269c20d0d4f02efd2cbbcc1a56
      - JARVIS_API_KEY_FILE=/run/secrets/jarvisapikey
      - MAX_CONCURRENT_CHATS=4
      - CLOCK_TS=1767812077
      - CONSTITUTIONAL_GUARDIAN_URL=http://jarvis-constitutional-guardian:8091
    depends_on:
      - jarvis-redis
      - jarvis-chroma
      - jarvis-ollama
    networks:
      - qualia-net
    restart: unless-stopped
    volumes:
      - ./services:/app/services
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: "3"
    secrets:
      - jarvisapikey
  jarvis-local-resources:
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
      - CLOCK_TS=1767812077
      - LOCAL_RESOURCES_DSN=postgresql://msjarvis:Nathaniel1@jarvis-gis-db:5432/msjarvisgis
    depends_on:
      - jarvis-local-resources-db
    networks:
      - qualia-net
    restart: unless-stopped
    volumes:
      - ./services:/app/services
  jarvis-local-resources-db:
    image: postgis/postgis:15-3.4
    container_name: jarvis-local-resources-db
    environment:
      - POSTGRES_DB=msjarvisgis
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
    ports:
      - 127.0.0.1:5435:5432
    volumes:
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
      - CHROMA_HOST=jarvis-chroma
      - CHROMA_PORT=8000
      - GIS_RAG_CHROMA_URL=http://jarvis-chroma:8000
      - GIS_RAG_COLLECTION=geospatialfeatures
      - GIS_EMBED_MODEL=all-minilm
      - CLOCK_TS=1767812077
      - GIS_DATABASE_URL=postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
    volumes:
      - ./gis_service:/app/gis_service
    depends_on:
      - jarvis-chroma
      - jarvis-local-resources-db
    expose:
      - "8044"
    ports:
      - 127.0.0.1:8004:8004
    networks:
      - qualia-net
    restart: unless-stopped
  jarvis-toroidal:
    build:
      context: ./services
      dockerfile: Dockerfile.toroidal
    image: msjarvis-toroidal:latest
    container_name: jarvis-toroidal
    ports:
      - 127.0.0.1:8025:8025
    environment:
      - OLLAMA_HOST=http://jarvis-ollama:11434
      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
      - CLOCK_TS=1767812077
      - SERVICE_PORT=8018
      - JARVIS_API_KEY=65ad4816de9004910599e6313fddfc2cd372e1269c20d0d4f02efd2cbbcc1a56
      - SERVICE_NAME=ms_jarvis_consciousness_bridge
      - SERVICE_REDIS_HOST=jarvis-redis
      - SERVICE_REDIS_PORT=6379
    depends_on:
      - jarvis-consciousness-bridge
      - jarvis-ollama
    networks:
      - qualia-net
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: "3"
  psychological_rag_domain:
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
      - qualia-net
    restart: unless-stopped
    environment:
      CLOCK_TS: 1767812077
  jarvis-psychology-services:
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
      - SERVICE_PORT=8019
      - CLOCK_TS=1767812077
      - PSYCHOLOGICAL_RAG_URL=http://psychological_rag_domain:9006
    depends_on:
      - psychological_rag_domain
    networks:
      - qualia-net
    restart: unless-stopped
  jarvis-constitutional-guardian:
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
      - CLOCK_TS=1767812077
    depends_on:
      - jarvis-main-brain
      - jarvis-blood-brain-barrier
    networks:
      - qualia-net
    restart: unless-stopped
    volumes:
      - ./services/constitutional_principles.json:/app/constitutional_principles.json:ro
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: "3"
  jarvis-judge-truth:
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
    networks:
      - qualia-net
    restart: unless-stopped
  jarvis-judge-consistency:
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
    networks:
      - qualia-net
    restart: unless-stopped
  jarvis-judge-alignment:
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
    networks:
      - qualia-net
    restart: unless-stopped
  jarvis-judge-ethics:
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
    networks:
      - qualia-net
    restart: unless-stopped
  jarvis-judge-pipeline:
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
      - JUDGE_ALIGNMENT_URL=http://jarvis-judge-alignment:7232
      - JUDGE_ETHICS_URL=http://jarvis-judge-ethics:7233
      - LM_SYNTHESIZER_URL=http://jarvis-lm-synthesizer:8001
      - CLOCK_TS=1767812077
    networks:
      - qualia-net
    restart: unless-stopped
    depends_on:
      - jarvis-judge-truth
      - jarvis-judge-consistency
      - jarvis-judge-alignment
      - jarvis-judge-ethics
      - jarvis-lm-synthesizer
  jarvis-aaacpe-rag:
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
      - CHROMA_HOST=jarvis-chroma
      - CHROMA_PORT=8000
      - CLOCK_TS=1767812077
    depends_on:
      - jarvis-chroma
    volumes:
      - aaacpe-cultural-data:/data
    networks:
      - qualia-net
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: "3"
  jarvis-rag-server:
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
      - CHROMA_HOST=jarvis-chroma
      - CHROMA_PORT=8000
      - CLOCK_TS=1767812077
    depends_on:
      - jarvis-chroma
    volumes:
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
      - CHROMA_HOST=jarvis-chroma
      - CHROMA_PORT=8000
      - CLOCK_TS=1767812077
    depends_on:
      - jarvis-chroma
    volumes:
      - ./services:/app/services:rw
    networks:
      - qualia-net
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: "3"

  jarvis-eeg-delta:
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
      REDIS_HOST: jarvis-redis
    depends_on:
      - jarvis-redis

  jarvis-eeg-theta:
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
      REDIS_HOST: jarvis-redis
    depends_on:
      - jarvis-redis

  jarvis-eeg-beta:
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
      REDIS_HOST: jarvis-redis
    depends_on:
      - jarvis-redis


  # ── DGM Cross-Bridges 10001-10023 ──────────────────────────────────────────
  jarvis-dgm-bridge-01:
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
      - LLM_MODEL=mistral:7b-instruct-q4_K_M
    networks: [qualia-net]
    restart: unless-stopped
    depends_on: [jarvis-ollama, jarvis-fractal-consciousness, jarvis-swarm-intelligence]

  jarvis-dgm-bridge-02:
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
      - LLM_MODEL=llama3.1:8b
    networks: [qualia-net]
    restart: unless-stopped
    depends_on: [jarvis-ollama, jarvis-fractal-consciousness, jarvis-swarm-intelligence]

  jarvis-dgm-bridge-03:
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
      - LLM_MODEL=neural-chat:latest
    networks: [qualia-net]
    restart: unless-stopped
    depends_on: [jarvis-ollama, jarvis-fractal-consciousness, jarvis-swarm-intelligence]

  jarvis-dgm-bridge-04:
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
      - LLM_MODEL=phi3.5:latest
    networks: [qualia-net]
    restart: unless-stopped
    depends_on: [jarvis-ollama, jarvis-fractal-consciousness, jarvis-swarm-intelligence]

  jarvis-dgm-bridge-05:
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
      - LLM_MODEL=gemma:2b
    networks: [qualia-net]
    restart: unless-stopped
    depends_on: [jarvis-ollama, jarvis-fractal-consciousness, jarvis-swarm-intelligence]

  jarvis-dgm-bridge-06:
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
      - LLM_MODEL=zephyr:latest
    networks: [qualia-net]
    restart: unless-stopped
    depends_on: [jarvis-ollama, jarvis-fractal-consciousness, jarvis-swarm-intelligence]

  jarvis-dgm-bridge-07:
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
      - LLM_MODEL=openchat:latest
    networks: [qualia-net]
    restart: unless-stopped
    depends_on: [jarvis-ollama, jarvis-fractal-consciousness, jarvis-swarm-intelligence]

  jarvis-dgm-bridge-08:
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
      - LLM_MODEL=starling-lm:latest
    networks: [qualia-net]
    restart: unless-stopped
    depends_on: [jarvis-ollama, jarvis-fractal-consciousness, jarvis-swarm-intelligence]

  jarvis-dgm-bridge-09:
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
      - LLM_MODEL=phi:latest
    networks: [qualia-net]
    restart: unless-stopped
    depends_on: [jarvis-ollama, jarvis-fractal-consciousness, jarvis-swarm-intelligence]

  jarvis-dgm-bridge-10:
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
      - LLM_MODEL=qwen2:7b
    networks: [qualia-net]
    restart: unless-stopped
    depends_on: [jarvis-ollama, jarvis-fractal-consciousness, jarvis-swarm-intelligence]

  jarvis-dgm-bridge-11:
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
      - LLM_MODEL=vicuna:latest
    networks: [qualia-net]
    restart: unless-stopped
    depends_on: [jarvis-ollama, jarvis-fractal-consciousness, jarvis-swarm-intelligence]

  jarvis-dgm-bridge-12:
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
      - LLM_MODEL=dolphin-phi:latest
    networks: [qualia-net]
    restart: unless-stopped
    depends_on: [jarvis-ollama, jarvis-fractal-consciousness, jarvis-swarm-intelligence]

  jarvis-dgm-bridge-13:
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
      - LLM_MODEL=orca-mini:3b
    networks: [qualia-net]
    restart: unless-stopped
    depends_on: [jarvis-ollama, jarvis-fractal-consciousness, jarvis-swarm-intelligence]

  jarvis-dgm-bridge-14:
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
      - LLM_MODEL=llama3.1-split:latest
    networks: [qualia-net]
    restart: unless-stopped
    depends_on: [jarvis-ollama, jarvis-fractal-consciousness, jarvis-swarm-intelligence]

  jarvis-dgm-bridge-15:
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
      - LLM_MODEL=mistral-split:latest
    networks: [qualia-net]
    restart: unless-stopped
    depends_on: [jarvis-ollama, jarvis-fractal-consciousness, jarvis-swarm-intelligence]

  jarvis-dgm-bridge-16:
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
      - LLM_MODEL=llama3.1:8b-instruct-q4_K_M
    networks: [qualia-net]
    restart: unless-stopped
    depends_on: [jarvis-ollama, jarvis-fractal-consciousness, jarvis-swarm-intelligence]

  jarvis-dgm-bridge-17:
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
      - LLM_MODEL=deepseek-coder:latest
    networks: [qualia-net]
    restart: unless-stopped
    depends_on: [jarvis-ollama, jarvis-fractal-consciousness, jarvis-swarm-intelligence]

  jarvis-dgm-bridge-18:
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
      - LLM_MODEL=llama2:latest
    networks: [qualia-net]
    restart: unless-stopped
    depends_on: [jarvis-ollama, jarvis-fractal-consciousness, jarvis-swarm-intelligence]

  jarvis-dgm-bridge-19:
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
      - LLM_MODEL=medllama2:latest
    networks: [qualia-net]
    restart: unless-stopped
    depends_on: [jarvis-ollama, jarvis-fractal-consciousness, jarvis-swarm-intelligence]

  jarvis-dgm-bridge-20:
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
      - LLM_MODEL=qwen2:latest
    networks: [qualia-net]
    restart: unless-stopped
    depends_on: [jarvis-ollama, jarvis-fractal-consciousness, jarvis-swarm-intelligence]

  jarvis-dgm-bridge-21:
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
      - LLM_MODEL=starcoder2:latest
    networks: [qualia-net]
    restart: unless-stopped
    depends_on: [jarvis-ollama, jarvis-fractal-consciousness, jarvis-swarm-intelligence]

  jarvis-dgm-bridge-22:
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
      - LLM_MODEL=mistral:latest
    networks: [qualia-net]
    restart: unless-stopped
    depends_on: [jarvis-ollama, jarvis-fractal-consciousness, jarvis-swarm-intelligence]

  jarvis-dgm-bridge-23:
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
      - LLM_MODEL=llama3.1:latest
    networks: [qualia-net]
    restart: unless-stopped
    depends_on: [jarvis-ollama, jarvis-fractal-consciousness, jarvis-swarm-intelligence]

networks:
  qualia-net:
    external: true
volumes:
  chroma_data:
    external: true
  aaacpe-cultural-data:
    driver: local
  msjarvis-rebuild_jarvis-local-resources-db-data:
    external: true
  hf-model-cache:
    driver: local
secrets:
  jarvisapikey:
    file: .secrets/jarvisapikey.txt


=== RUNNING CONTAINERS ===
NAMES                                                   IMAGE                                                 STATUS                  PORTS
jarvis-constitutional-guardian                          msjarvis-rebuild-jarvis-constitutional-guardian       Up 11 hours             127.0.0.1:8091->8091/tcp
jarvis-wv-entangled-gateway                             msjarvis-rebuild-jarvis-wv-entangled-gateway          Up 12 hours             127.0.0.1:8010->8010/tcp
jarvis-dgm-bridge-03                                    msjarvis-rebuild-jarvis-dgm-bridge-03                 Up 12 hours             10003/tcp
jarvis-dgm-bridge-08                                    msjarvis-rebuild-jarvis-dgm-bridge-08                 Up 12 hours             10008/tcp
jarvis-dgm-bridge-01                                    msjarvis-rebuild-jarvis-dgm-bridge-01                 Up 12 hours             10001/tcp
jarvis-dgm-bridge-04                                    msjarvis-rebuild-jarvis-dgm-bridge-04                 Up 12 hours             10004/tcp
jarvis-dgm-bridge-07                                    msjarvis-rebuild-jarvis-dgm-bridge-07                 Up 12 hours             10007/tcp
jarvis-dgm-bridge-02                                    msjarvis-rebuild-jarvis-dgm-bridge-02                 Up 12 hours             10002/tcp
jarvis-dgm-bridge-09                                    msjarvis-rebuild-jarvis-dgm-bridge-09                 Up 12 hours             10009/tcp
jarvis-dgm-bridge-05                                    msjarvis-rebuild-jarvis-dgm-bridge-05                 Up 12 hours             10005/tcp
jarvis-dgm-bridge-06                                    msjarvis-rebuild-jarvis-dgm-bridge-06                 Up 12 hours             10006/tcp
jarvis-dgm-bridge-14                                    msjarvis-rebuild-jarvis-dgm-bridge-14                 Up 12 hours             10014/tcp
jarvis-dgm-bridge-20                                    msjarvis-rebuild-jarvis-dgm-bridge-20                 Up 12 hours             10020/tcp
jarvis-dgm-bridge-12                                    msjarvis-rebuild-jarvis-dgm-bridge-12                 Up 12 hours             10012/tcp
jarvis-dgm-bridge-22                                    msjarvis-rebuild-jarvis-dgm-bridge-22                 Up 12 hours             10022/tcp
jarvis-dgm-bridge-21                                    msjarvis-rebuild-jarvis-dgm-bridge-21                 Up 12 hours             10021/tcp
jarvis-dgm-bridge-11                                    msjarvis-rebuild-jarvis-dgm-bridge-11                 Up 12 hours             10011/tcp
jarvis-dgm-bridge-10                                    msjarvis-rebuild-jarvis-dgm-bridge-10                 Up 12 hours             10010/tcp
jarvis-dgm-bridge-13                                    msjarvis-rebuild-jarvis-dgm-bridge-13                 Up 12 hours             10013/tcp
jarvis-dgm-bridge-17                                    msjarvis-rebuild-jarvis-dgm-bridge-17                 Up 12 hours             10017/tcp
jarvis-dgm-bridge-23                                    msjarvis-rebuild-jarvis-dgm-bridge-23                 Up 12 hours             10023/tcp
jarvis-dgm-bridge-19                                    msjarvis-rebuild-jarvis-dgm-bridge-19                 Up 12 hours             10019/tcp
jarvis-dgm-bridge-15                                    msjarvis-rebuild-jarvis-dgm-bridge-15                 Up 12 hours             10015/tcp
jarvis-dgm-bridge-16                                    msjarvis-rebuild-jarvis-dgm-bridge-16                 Up 12 hours             10016/tcp
jarvis-dgm-bridge-18                                    msjarvis-rebuild-jarvis-dgm-bridge-18                 Up 12 hours             10018/tcp
jarvis-judge-pipeline                                   msjarvis-rebuild-jarvis-judge-pipeline                Up 12 hours             127.0.0.1:7239->7239/tcp
jarvis-rag-server                                       msjarvis-rebuild-jarvis-rag-server                    Up 12 hours             127.0.0.1:8003->8003/tcp
jarvis-judge-alignment                                  msjarvis-rebuild-jarvis-judge-alignment               Up 12 hours             127.0.0.1:7232->7232/tcp
jarvis-unified-gateway                                  msjarvis-rebuild-jarvis-unified-gateway               Up 13 hours (healthy)   127.0.0.1:8001->8001/tcp
jarvis-toroidal                                         msjarvis-toroidal:latest                              Up 13 hours             127.0.0.1:8025->8025/tcp
jarvis-neurobiological-master                           msjarvis-rebuild-jarvis-neurobiological-master        Up 13 hours             8018/tcp
jarvis-brain-orchestrator                               msjarvis-rebuild-jarvis-brain-orchestrator            Up 13 hours (healthy)   127.0.0.1:17260->7260/tcp
jarvis-consciousness-bridge                             msjarvis-rebuild-jarvis-consciousness-bridge          Up 13 hours             127.0.0.1:8020->8018/tcp
jarvis-main-brain                                       jarvis-main-brain:latest                              Up 13 hours             127.0.0.1:8050->8050/tcp
jarvis-20llm-production                                 msjarvis-rebuild-jarvis-20llm-production              Up 13 hours             127.0.0.1:8008->8008/tcp
jarvis-blood-brain-barrier                              msjarvis-rebuild-jarvis-blood-brain-barrier           Up 13 hours             127.0.0.1:8016->8016/tcp
jarvis-woah                                             msjarvis-rebuild-jarvis-woah                          Up 13 hours             127.0.0.1:7012->7012/tcp
jarvis-qualia-engine                                    msjarvis-rebuild-jarvis-qualia-engine                 Up 13 hours             8017/tcp
jarvis-fractal-consciousness                            msjarvis-rebuild-jarvis-fractal-consciousness         Up 13 hours             8002/tcp, 8027/tcp
jarvis-eeg-theta                                        msjarvis-rebuild-jarvis-eeg-theta                     Up 13 hours             127.0.0.1:8074->8074/tcp
jarvis-eeg-beta                                         msjarvis-rebuild-jarvis-eeg-beta                      Up 13 hours             127.0.0.1:8075->8075/tcp
jarvis-eeg-delta                                        msjarvis-rebuild-jarvis-eeg-delta                     Up 13 hours             127.0.0.1:8073->8073/tcp
jarvis-psychology-services                              msjarvis-rebuild-jarvis-psychology-services           Up 13 hours             127.0.0.1:8019->8019/tcp
jarvis-aaacpe-rag                                       msjarvis-rebuild-jarvis-aaacpe-rag                    Up 13 hours             127.0.0.1:8032->8032/tcp
jarvis-spiritual-rag                                    msjarvis-rebuild-jarvis-spiritual-rag                 Up 13 hours             127.0.0.1:8005->8005/tcp
jarvis-gis-rag                                          msjarvis-rebuild-jarvis-gis-rag                       Up 13 hours             127.0.0.1:8004->8004/tcp, 8044/tcp
jarvis-hippocampus                                      msjarvis-rebuild-jarvis-hippocampus                   Up 13 hours             127.0.0.1:8011->8011/tcp
jarvis-autonomous-learner                               msjarvis-rebuild-jarvis-rag-server:latest             Up 13 hours             8003/tcp, 127.0.0.1:8425->8425/tcp
jarvis-local-resources                                  msjarvis-rebuild-jarvis-local-resources               Up 13 hours             127.0.0.1:8006->8006/tcp, 8035/tcp
msjarvis-rebuild-nbb_darwin_godel_machines-1            msjarvis-rebuild-nbb_darwin_godel_machines            Up 13 hours             127.0.0.1:8302->8010/tcp
jarvis-local-resources-db                               postgis/postgis:15-3.4                                Up 13 hours             127.0.0.1:5435->5432/tcp
msjarvis-rebuild-nbb_mother_carrie_protocols-1          msjarvis-rebuild-nbb_mother_carrie_protocols          Up 13 hours             127.0.0.1:8107->8010/tcp
jarvis-fifth-dgm                                        msjarvis-rebuild-jarvis-fifth-dgm                     Up 13 hours             127.0.0.1:4002->4002/tcp
llm12-proxy                                             msjarvis-rebuild-llm12-proxy                          Up 13 hours             127.0.0.1:8212->8212/tcp
jarvis-judge-consistency                                msjarvis-rebuild-jarvis-judge-consistency             Up 13 hours             127.0.0.1:7231->7231/tcp
msjarvis-rebuild-nbb_woah_algorithms-1                  msjarvis-rebuild-nbb_woah_algorithms                  Up 13 hours             127.0.0.1:8104->8010/tcp
msjarvis-rebuild-nbb_pituitary_gland-1                  msjarvis-rebuild-nbb_pituitary_gland                  Up 13 hours             127.0.0.1:8108->80/tcp
jarvis-agents-service                                   msjarvis-rebuild-jarvis-agents-service                Up 13 hours             8005/tcp
msjarvis-rebuild-nbb_blood_brain_barrier-1              msjarvis-rebuild-nbb_blood_brain_barrier              Up 13 hours             127.0.0.1:8301->8010/tcp
msjarvis-rebuild-nbb_prefrontal_cortex-1                msjarvis-rebuild-nbb_prefrontal_cortex                Up 13 hours             127.0.0.1:8105->7005/tcp
llm18-proxy                                             msjarvis-rebuild-llm18-proxy                          Up 13 hours             127.0.0.1:8218->8218/tcp
jarvis-temporal-consciousness                           msjarvis-rebuild-jarvis-temporal-consciousness        Up 13 hours             7007/tcp
neo4j                                                   neo4j:5.13-community                                  Up 13 hours             7473/tcp, 127.0.0.1:7687->7687/tcp, 127.0.0.1:7475->7474/tcp
ipfs                                                    ipfs/kubo:latest                                      Up 13 hours (healthy)   4001/tcp, 8080-8081/tcp, 4001/udp, 127.0.0.1:5001->5001/tcp
llm19-proxy                                             msjarvis-rebuild-llm19-proxy                          Up 13 hours             127.0.0.1:8219->8219/tcp
llm21-proxy                                             msjarvis-rebuild-llm21-proxy                          Up 13 hours             127.0.0.1:8221->8221/tcp
llm15-proxy                                             msjarvis-rebuild-llm15-proxy                          Up 13 hours             127.0.0.1:8215->8215/tcp
msjarvis-rebuild-nbb_subconscious-1                     msjarvis-rebuild-nbb_subconscious                     Up 13 hours             127.0.0.1:8112->8010/tcp
llm6-proxy                                              msjarvis-rebuild-llm6-proxy                           Up 13 hours             127.0.0.1:8206->8206/tcp
llm7-proxy                                              msjarvis-rebuild-llm7-proxy                           Up 13 hours             127.0.0.1:8207->8207/tcp
llm13-proxy                                             msjarvis-rebuild-llm13-proxy                          Up 13 hours             127.0.0.1:8213->8213/tcp
jarvis-i-containers                                     msjarvis-rebuild-jarvis-i-containers                  Up 13 hours             8015/tcp
llm14-proxy                                             msjarvis-rebuild-llm14-proxy                          Up 13 hours             127.0.0.1:8214->8214/tcp
jarvis-semaphore                                        msjarvis-rebuild-jarvis-semaphore                     Up 13 hours             127.0.0.1:8030->8030/tcp
llm8-proxy                                              msjarvis-rebuild-llm8-proxy                           Up 13 hours             127.0.0.1:8208->8208/tcp
msjarvis-rebuild-nbb_spiritual_maternal_integration-1   msjarvis-rebuild-nbb_spiritual_maternal_integration   Up 13 hours             127.0.0.1:8109->8010/tcp
llm1-proxy                                              msjarvis-rebuild-llm1-proxy                           Up 13 hours             127.0.0.1:8201->8201/tcp
jarvis-mother-protocols                                 msjarvis-rebuild-jarvis-mother-protocols              Up 13 hours             4000/tcp
psychological_rag_domain                                msjarvis-rebuild-psychological_rag_domain             Up 13 hours             9006/tcp, 127.0.0.1:9006->8006/tcp
llm10-proxy                                             msjarvis-rebuild-llm10-proxy                          Up 13 hours             127.0.0.1:8210->8210/tcp
jarvis-swarm-intelligence                               msjarvis-rebuild-jarvis-swarm-intelligence            Up 13 hours             8021/tcp
llm17-proxy                                             msjarvis-rebuild-llm17-proxy                          Up 13 hours             127.0.0.1:8217->8217/tcp
jarvis-web-research                                     msjarvis-rebuild-jarvis-web-research                  Up 13 hours             8008/tcp
llm11-proxy                                             msjarvis-rebuild-llm11-proxy                          Up 13 hours             127.0.0.1:8211->8211/tcp
nbb-i-containers                                        msjarvis-rebuild-nbb-i-containers                     Up 13 hours             127.0.0.1:8101->7005/tcp
msjarvis-rebuild-nbb_spiritual_root-1                   msjarvis-rebuild-nbb_spiritual_root                   Up 13 hours             127.0.0.1:8103->8010/tcp
jarvis-69dgm-bridge                                     msjarvis-rebuild-jarvis-69dgm-bridge                  Up 13 hours             127.0.0.1:9000->9000/tcp
jarvis-lm-synthesizer                                   msjarvis-rebuild-jarvis-lm-synthesizer                Up 13 hours             8001/tcp
llm4-proxy                                              msjarvis-rebuild-llm4-proxy                           Up 13 hours             127.0.0.1:8204->8204/tcp
jarvis-judge-ethics                                     msjarvis-rebuild-jarvis-judge-ethics                  Up 13 hours             127.0.0.1:7233->7233/tcp
jarvis-redis                                            redis:7-alpine                                        Up 13 hours (healthy)   127.0.0.1:6380->6379/tcp
jarvis-chroma                                           chromadb/chroma:latest                                Up 13 hours (healthy)   127.0.0.1:8002->8000/tcp
llm16-proxy                                             msjarvis-rebuild-llm16-proxy                          Up 13 hours             127.0.0.1:8216->8216/tcp
llm3-proxy                                              msjarvis-rebuild-llm3-proxy                           Up 13 hours             127.0.0.1:8203->8203/tcp
llm5-proxy                                              msjarvis-rebuild-llm5-proxy                           Up 13 hours             127.0.0.1:8205->8205/tcp
msjarvis-rebuild-nbb_heteroglobulin_transport-1         msjarvis-rebuild-nbb_heteroglobulin_transport         Up 13 hours             127.0.0.1:8106->8010/tcp
jarvis-ollama                                           ollama/ollama:latest                                  Up 13 hours             127.0.0.1:11434->11434/tcp
mysql                                                   mysql:8.2                                             Up 13 hours             33060/tcp, 127.0.0.1:3307->3306/tcp
llm20-proxy                                             msjarvis-rebuild-llm20-proxy                          Up 13 hours             127.0.0.1:8220->8220/tcp
llm2-proxy                                              msjarvis-rebuild-llm2-proxy                           Up 13 hours             127.0.0.1:8202->8202/tcp
llm9-proxy                                              msjarvis-rebuild-llm9-proxy                           Up 13 hours             127.0.0.1:8209->8209/tcp
msjarvis-rebuild-nbb_qualia_engine-1                    msjarvis-rebuild-nbb_qualia_engine                    Up 13 hours             127.0.0.1:8303->8010/tcp
jarvis-judge-truth                                      msjarvis-rebuild-jarvis-judge-truth                   Up 13 hours             127.0.0.1:7230->7230/tcp
llm22-proxy                                             msjarvis-rebuild-llm22-proxy                          Up 13 hours             127.0.0.1:8222->8222/tcp
msjarvis-rebuild-nbb_consciousness_containers-1         msjarvis-rebuild-nbb_consciousness_containers         Up 13 hours             127.0.0.1:8102->8010/tcp
pg-recovery                                             postgis/postgis:15-3.4                                Up 20 hours             5432/tcp
jarvis-hilbert-state                                    msjarvis-rebuild-jarvis-hilbert-state:latest          Up 3 days               
jarvis-session-sidecar                                  jarvis-session-sidecar:latest                         Up 3 days               127.0.0.1:8060->8060/tcp, 8070/tcp
jarvis-gbim-temporal-indexer                            msjarvis-gbim-indexers:latest                         Up 3 days               127.0.0.1:7211->8000/tcp
jarvis-jaeger                                           jaegertracing/all-in-one:1.52                         Up 3 days               4317-4318/tcp, 5775/udp, 5778/tcp, 9411/tcp, 14250/tcp, 14268/tcp, 6831-6832/udp, 127.0.0.1:16686->16686/tcp

=== BACKEND DIR CONTENTS ===
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/scipy/_lib/cobyqa/main.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/markdown_it/main.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/typer/main.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/annotated_doc/main.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/pydantic_settings/main.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/open_clip_train/main.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/pydantic/v1/main.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/pydantic/main.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/uvicorn/main.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/dotenv/main.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/watchfiles/main.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/pip/_internal/cli/main.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/pip/_internal/main.py
/opt/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/markdown_it/main.py
/opt/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/typer/main.py
/opt/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/pydantic/v1/main.py
/opt/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/pydantic/main.py
/opt/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/uvicorn/main.py
/opt/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/dotenv/main.py
/opt/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/watchfiles/main.py
/opt/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/pip/_internal/cli/main.py
/opt/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/pip/_internal/main.py
/opt/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pip/_internal/cli/main.py
/opt/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pip/_internal/main.py
/opt/msjarvis-rebuild/services/jarvis_steward/main.py
/opt/msjarvis-rebuild/services/jarvis_rag_search/main.py
/opt/msjarvis-rebuild/services/_vendor/eth_hash/main.py
/opt/msjarvis-rebuild/services/_vendor/pydantic/v1/main.py
/opt/msjarvis-rebuild/services/_vendor/pydantic/main.py
/opt/msjarvis-rebuild/services/_vendor/eth_keys/backends/native/main.py
/opt/msjarvis-rebuild/services/_vendor/eth_keys/main.py
/opt/msjarvis-rebuild/services/_vendor/hexbytes/main.py
/opt/msjarvis-rebuild/services/_vendor/eth_rlp/main.py
/opt/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/scipy/_lib/cobyqa/main.py
/opt/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/markdown_it/main.py
/opt/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/typer/main.py
/opt/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/annotated_doc/main.py
/opt/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/pydantic/v1/main.py
/opt/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/pydantic/main.py
/opt/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/uvicorn/main.py
/opt/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/dotenv/main.py
/opt/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/watchfiles/main.py
/opt/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/pip/_internal/cli/main.py
/opt/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/pip/_internal/main.py
/opt/msjarvis-rebuild/services/main.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/markdown_it/main.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/typer/main.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/annotated_doc/main.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/pydantic_settings/main.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/eth_hash/main.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/pydantic/v1/main.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/pydantic/main.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/main.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/eth_keys/backends/native/main.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/eth_keys/main.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/dotenv/main.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/hexbytes/main.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/watchfiles/main.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/pip/_internal/cli/main.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/pip/_internal/main.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/eth_rlp/main.py
/opt/msjarvis-rebuild/neurobiologicalbrainmothercarrieprotocolsservice/main.py
/opt/msjarvis-rebuild/.format-venv/lib/python3.12/site-packages/pip/_internal/cli/main.py
/opt/msjarvis-rebuild/.format-venv/lib/python3.12/site-packages/pip/_internal/main.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/markdown_it/main.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/typer/main.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/pydantic/v1/main.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/pydantic/main.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/uvicorn/main.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/dotenv/main.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/watchfiles/main.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/pip/_internal/cli/main.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/pip/_internal/main.py
/opt/msjarvis-rebuild/.woah-venv/lib/python3.12/site-packages/annotated_doc/main.py
/opt/msjarvis-rebuild/.woah-venv/lib/python3.12/site-packages/pydantic/v1/main.py
/opt/msjarvis-rebuild/.woah-venv/lib/python3.12/site-packages/pydantic/main.py
/opt/msjarvis-rebuild/.woah-venv/lib/python3.12/site-packages/uvicorn/main.py
/opt/msjarvis-rebuild/.woah-venv/lib/python3.12/site-packages/pip/_internal/cli/main.py
/opt/msjarvis-rebuild/.woah-venv/lib/python3.12/site-packages/pip/_internal/main.py
/opt/msjarvis-rebuild/neurobiological_brain/mother_carrie_protocols/service/main.py
/opt/msjarvis-rebuild/main.py
/opt/msjarvis-rebuild/ms_jarvis_unified_gateway.py
/opt/msjarvis-rebuild/service_discovery.py
/opt/msjarvis-rebuild/enrich_where.py
/opt/msjarvis-rebuild/gisgeodb_storage.py
/opt/msjarvis-rebuild/load_all_attrs_csvs.py
/opt/msjarvis-rebuild/ms-allis-auth-install/backend/wallet_service.py
/opt/msjarvis-rebuild/ms-allis-auth-install/backend/auth_api_patch.py
/opt/msjarvis-rebuild/ms-allis-auth-install/backend/registration_pipeline.py
/opt/msjarvis-rebuild/llm21_health_proxy.py
/opt/msjarvis-rebuild/gis_service/router.py
/opt/msjarvis-rebuild/gis_service/spatial_queries.py
/opt/msjarvis-rebuild/gis_service/__init__.py
/opt/msjarvis-rebuild/resource_assistant.py
/opt/msjarvis-rebuild/woah_stub.py
/opt/msjarvis-rebuild/wv_entangled_context_model.py
/opt/msjarvis-rebuild/llm10_health_proxy.py
/opt/msjarvis-rebuild/service_discovery_no_redis.py
/opt/msjarvis-rebuild/test_rag_text.py
/opt/msjarvis-rebuild/seed_mountainshares.py
/opt/msjarvis-rebuild/swarm_intelligence.py
/opt/msjarvis-rebuild/api_resources.py
/opt/msjarvis-rebuild/llm1_health_proxy.py
/opt/msjarvis-rebuild/admin_cli.py
/opt/msjarvis-rebuild/gateway8050_inline.py
/opt/msjarvis-rebuild/ask_gis.py
/opt/msjarvis-rebuild/llm19_health_proxy.py
/opt/msjarvis-rebuild/ai-server/ai_server.py
/opt/msjarvis-rebuild/ai-server/ai_server_20llm_PRODUCTION.py
/opt/msjarvis-rebuild/service_registry_client_stub.py
/opt/msjarvis-rebuild/gbim_orchestrator.py

=== POSTGRES CONTAINER NAME ===
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ 

