(.venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ # Is /opt/msjarvis-rebuild a symlink?
ls -la /opt/msjarvis-rebuild

# What does the running process actually have open?
PID=$(systemctl show -p MainPID jarvis-chat | cut -d= -f2)
echo "PID: $PID"
sudo ls -la /proc/$PID/exe
sudo cat /proc/$PID/cmdline | tr '\0' ' '

# What is the actual working directory of the running process?
sudo ls -la /proc/$PID/cwd

# Does the patched file match what's on nvme1?
diff /opt/msjarvis-rebuild/services/ms_jarvis_production_chat.py \
     /mnt/nvme1/msjarvis-rebuild/services/ms_jarvis_production_chat.py
total 710556
drwxrwxr-x 87 cakidd cakidd     57344 Jun 11 17:29  .
drwxr-xr-x  8 root   root        4096 Jun  2 11:56  ..
drwxr-xr-x  2 cakidd cakidd      4096 Jan  7 13:09  ...
-rw-rw-r--  1 cakidd cakidd         0 Jun  8 14:06 '='
-rw-rw-r--  1 cakidd cakidd        45 May  3 19:48 '\'
-rw-rw-r--  1 cakidd cakidd         0 Jan 11 22:23 '$IDX'
-rw-rw-r--  1 cakidd cakidd         0 May 29 20:22  0
-rw-rw-r--  1 cakidd cakidd      2859 May 27 09:44  00_provenance_migration.sql
-rw-rw-r--  1 cakidd cakidd         0 May 19 20:53 '=12.1'
-rw-rw-r--  1 cakidd cakidd     20906 Jun  7 09:52  20llm_backup_20260607_1005.py
-rw-rw-r--  1 cakidd cakidd        51 Jan 21 18:05  20llmFINAL.health.json
-rw-rw-r--  1 cakidd cakidd         0 May 19 20:53 '=470,driver'
-rw-rw-r--  1 cakidd cakidd         0 Jun  8 18:54  50
-rw-rw-r--  1 cakidd cakidd      6568 Jan  3 17:31  911centers_wvdem_032819_gcs84_attrs.csv
-rw-rw-r--  1 cakidd cakidd     27592 Apr 30 14:12  abis.contracts.json
-rw-r--r--  1 cakidd cakidd     15717 Jun  1 17:16  admin_cli.py
-rw-r--r--  1 cakidd cakidd     15362 Jun  1 17:16  admin_cli.py.bak.20260601-171658
drwxrwxrwx  2 cakidd cakidd      4096 Jun 11 18:06  admin-data
-rw-rw-r--  1 cakidd cakidd      1738 Mar 21 18:05  adversarial_results_20260321_180551.json
-rw-rw-r--  1 cakidd cakidd      8507 Mar 21 18:05  adversarial_results_20260321_180556.json
-rw-rw-r--  1 cakidd cakidd      1738 Mar 21 18:06  adversarial_results_20260321_180608.json
-rw-rw-r--  1 cakidd cakidd      8507 Mar 21 18:06  adversarial_results_20260321_180611.json
-rw-rw-r--  1 cakidd cakidd      1613 Mar 21 19:12  adversarial_results_20260321_191257.json
-rw-rw-r--  1 cakidd cakidd      1509 Mar 21 19:15  adversarial_results_20260321_191552.json
-rw-rw-r--  1 cakidd cakidd      1226 Mar 21 19:32  adversarial_results_20260321_193201.json
-rw-rw-r--  1 cakidd cakidd      1509 Mar 21 19:43  adversarial_results_20260321_194304.json
-rw-rw-r--  1 cakidd cakidd      1822 Mar 21 19:54  adversarial_results_20260321_195445.json
-rw-rw-r--  1 cakidd cakidd      2289 Mar 21 20:17  adversarial_results_20260321_201711.json
-rw-rw-r--  1 cakidd cakidd      1759 Mar 21 20:25  adversarial_results_20260321_202552.json
-rw-rw-r--  1 cakidd cakidd      1911 Mar 21 20:35  adversarial_results_20260321_203504.json
-rw-rw-r--  1 cakidd cakidd      1354 Mar 21 20:41  adversarial_results_20260321_204145.json
drwxrwxr-x  2 cakidd cakidd      4096 Jun  5 11:40  ai
drwxrwxr-x  3 cakidd cakidd      4096 Jun  5 11:40  ai-server
-rw-rw-r--  1 cakidd cakidd     25558 Jun  5 18:00  ai_server_20llm_PRODUCTION.py
-rw-rw-r--  1 cakidd cakidd     23034 Jun  5 17:40  ai_server_20llm_PRODUCTION.py.bak.20260605_174008
-rw-rw-r--  1 cakidd cakidd       386 Jan 11 22:14  all_gis_vectors_filtered.txt
-rw-rw-r--  1 cakidd cakidd       854 Jan 11 22:30  all_gis_vectors_full.txt
-rw-rw-r--  1 cakidd cakidd       854 Jan 11 22:31  all_gis_vectors_ingest.txt
-rw-rw-r--  1 cakidd cakidd      1023 Jan 11 22:14  all_gis_vectors.txt
-rw-rw-r--  1 cakidd cakidd       854 Jan 11 22:31  all_gis_vectors_unique.txt
-rw-rw-r--  1 cakidd cakidd       348 Jan  3 17:31  amtrackrails_federalrailroadadministration_200210_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd       347 Jan  3 17:31  amtrackrails_federalrailroadadministration_200210_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd       686 Feb  2 15:39  api_resources.py
-rw-rw-r--  1 cakidd cakidd      3577 Jun  5 17:42  apply_synthesis_patch.py
drwxr-xr-x  2 cakidd cakidd      4096 Jan  7 08:46  appservices
drwxrwxr-x  4 cakidd cakidd      4096 Apr 30 13:38  _archive
drwxrwxr-x  2 cakidd cakidd      4096 Feb 24 15:13  archives
-rwxrwxr-x  1 cakidd cakidd      1360 Jan 30 10:35  ask_gis_near_oakhill.py
-rwxrwxr-x  1 cakidd cakidd       873 Jan 30 10:33  ask_gis.py
-rw-rw-r--  1 cakidd cakidd       655 Jan 12 13:47  attrs_api.py
-rw-rw-r--  1 cakidd cakidd      3362 Jan 12 14:03  attrs_test.json
-rw-rw-r--  1 cakidd cakidd      2049 Jan 12 13:55  attrs_with_geom_api.py
-rw-rw-r--  1 cakidd cakidd         0 Mar 26 10:50  audit_20260326_1050.txt
-rw-rw-r--  1 cakidd cakidd      9083 Jun  1 17:32  auth_api.py
-rw-rw-r--  1 cakidd cakidd      8482 Apr 26 12:24  auth_api.py.bak_20260426-122443
-rw-rw-r--  1 cakidd cakidd      8905 Jun  1 17:32  auth_api.py.bak.20260601-173207
-rw-rw-r--  1 cakidd cakidd      8482 Apr 26 14:11  auth_api.py.bak-cors
-rw-rw-r--  1 cakidd cakidd       544 Jan 16 20:09  autonomouslearner.py
-rw-rw-r--  1 cakidd cakidd      1130 Feb  2 12:43  backfill_provenance_batch.sql
-rw-rw-r--  1 cakidd cakidd       956 Feb  2 10:08  backfill_provenance.sql
-rw-rw-r--  1 cakidd cakidd      1062 Apr 30 14:12  BACKLOG_ASPIRATIONAL.md
-rw-rw-r--  1 cakidd cakidd   4459920 Jan  7 13:13  backup_filename_index.txt
-rwxrwxr-x  1 cakidd cakidd       620 Mar 29 13:13  backup_judge_key_to_usb.sh
drwxrwxr-x  2 cakidd cakidd      4096 Jan  9 13:52  _backup_llm_proxy_dockerfiles
-rw-rw-r--  1 cakidd cakidd        94 Jan  7 13:11  backup_roots.txt
drwxrwxr-x  7 cakidd cakidd      4096 Jun  8 13:04  backups
-rw-rw-r--  1 cakidd cakidd       666 Mar 12 16:09  bbb-logs-20260312-160957.log
-rw-rw-r--  1 cakidd cakidd        43 Jan  8 18:53  bbb_requirements.txt
drwxrwxr-x  2 cakidd cakidd      4096 Mar 10 21:01  bin
-rw-rw-r--  1 cakidd cakidd    431248 Jan  3 17:31  blockgroups_census_2000_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd    429697 Jan  3 17:31  blockgroups_census_2000_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd    367446 Jan  3 17:31  blockgroups_census_201111_gcs83_attrs.csv
-rw-rw-r--  1 cakidd cakidd    544693 Jan  3 17:31  blockgroups_census_2020_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd    460763 Jan  3 17:31  blockgroups_census_2020_wma84_attrs.csv
-rw-rw-r--  1 cakidd cakidd      8709 Jan 25 14:42  bootstrap_gbim_beliefs_eq1.py
-rw-rw-r--  1 cakidd cakidd     90379 Jan  3 17:31  boundaryappalachianbasin_wvges_1996_utm83_attrs.csv
-rwxr-xr-x  1 cakidd cakidd      1282 Jan  9 12:02  brain_orchestrator.py
-rwxr-xr-x  1 cakidd cakidd      1273 Jan  7 13:18  brain_orchestrator.py.bak
drwxrwxr-x  3 cakidd cakidd      4096 Mar 30 20:57  build
-rw-rw-r--  1 cakidd cakidd      2105 Feb 22 14:42  bulk_ingest_attrs.py
-rw-rw-r--  1 cakidd cakidd     26015 Feb 22 15:06  bulk_ingest.log
-rwxrwxr-x  1 cakidd cakidd      1142 Feb 22 13:58  bulk_load_attrs.sh
-rw-rw-r--  1 cakidd cakidd         0 May 15 21:02 '^C'
-rwxrwxr-x  1 cakidd cakidd       474 Mar 29 13:13  cache_conversation_history_uuid.sh
-rw-rw-r--  1 cakidd cakidd         0 May 18 23:58  CACHED
-rw-rw-r--  1 cakidd cakidd      2435 Jan  3 17:31  calderl_reg_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd       531 Feb  6 22:12  call_rag_with_entanglement_example.py
-rwxrwxr-x  1 cakidd cakidd       543 Jan 12 07:51  capture_gdb_json.sh
-rw-rw-r--  1 cakidd cakidd       510 Mar 12 16:09  cb-logs-20260312-160957.log
-rw-rw-r--  1 cakidd cakidd        24 Jan 20 17:22  chat_light_current.py
-rw-rw-r--  1 cakidd cakidd     35036 Jun  7 10:26  ChatPanel_backup_20260607_1026.tsx
-rwxrwxr-x  1 cakidd cakidd       349 Jan 12 07:21  check_gbim_metadata.sh
drwxrwxr-x  6 cakidd cakidd      4096 Apr  5 17:41  chroma_data
drwxr-xr-x  8 cakidd cakidd      4096 Apr  5 17:41  chroma_db
drwxrwxr-x  2 cakidd cakidd      4096 Feb 16 10:09  chromadb
-rw-rw-r--  1 cakidd cakidd       633 Jan 10 15:59  chroma_ingestion_sources.txt
-rw-rw-r--  1 cakidd cakidd      3442 Jun  6 14:20  chroma_migrate.py
-rw-rw-r--  1 cakidd cakidd     12503 Jan 16 18:54  chroma_persistent_RAG_WORKING_20260116.tgz
-rw-r--r--  1 cakidd cakidd         0 Feb  5 11:15  chroma.sqlite3
-rw-rw-r--  1 cakidd cakidd     18960 Jan  3 17:31  citieswithpopulation_2500_census_201111_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      3795 Jan  3 17:31  citieswithpopulationover10k_census_201111_gcs83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      2330 Jan  3 17:31  citieswithpopulationover10k_uscensus_1990_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      2300 Jan  3 17:31  citieswithpopulationover10k_uscensus_1990_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     33496 Jan  3 17:31  citieswithpopulationover2500_uscensus_1990_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      4160 Jan  3 17:31  citieswithpopulationsover10k_census_2020_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      4174 Jan  3 17:31  citieswithpopulationsover10k_census_2020_wma84_attrs.csv
-rw-rw-r--  1 cakidd cakidd     18665 Jan  3 17:31  citieswithpopulationsover2500_census_2020_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     40121 Jan  3 17:31  citieswithpopulatoinover2500_uscensus_1990_utm83_attrs.csv
-rw-r--r--  1 cakidd cakidd       318 May 12 01:13  cloudflared.config.yml
-rw-rw-r--  1 cakidd cakidd  19308942 Apr 24 11:00  cloudflared.deb
-rw-rw-r--  1 cakidd cakidd      3981 Jan  3 17:31  coals2_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      3727 Jan  3 17:31  coals2_utm27_attrs.csv
-rw-rw-r--  1 cakidd cakidd      3871 Jan  3 17:31  coals2_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     79898 Jan  3 17:31  communityboundary_min_att_20250121_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      6910 Mar  7 11:23  complete_service_mapping.json
drwxrwxr-x  2 cakidd cakidd      4096 Jun  6 21:52  config
-rw-rw-r--  1 cakidd cakidd       124 Apr 25 12:17  conftest.py
-rw-r--r--  1 cakidd cakidd      7048 May 18 22:16  consciousness_unified_bridge_EDIT.py
-rw-r--r--  1 cakidd cakidd      7060 May 14 21:18  consciousness_unified_bridge.py.bak
-rw-rw-r--  1 cakidd cakidd       955 Jan 21 18:12  CONSENSUS_STATS_SNAPSHOT.json
-rw-rw-r--  1 cakidd cakidd     15819 Jun  7 09:22  constitutional_api.py
drwxrwxr-x  8 cakidd cakidd      4096 Jun  2 21:34  contracts
drwxrwxr-x  5 cakidd cakidd      4096 Jun  2 08:39  contracts.bad
drwxrwxr-x  5 cakidd cakidd      4096 Jun  2 08:37  contracts.broken.20260602-083929
-rw-rw-r--  1 cakidd cakidd        85 Mar 29 13:13  conversation_history_uuid.json
-rw-rw-r--  1 cakidd cakidd     18632 Jan  3 17:31  correctionalinstitutions_hsip_20091230_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     18770 Jan  3 17:31  correctionalinstitutions_hsip_20091230_wgs84_attrs.csv
-rw-rw-r--  1 cakidd cakidd    169708 Jan  3 17:31  countycityparkboundaries_20201104_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd         0 Jan 31 00:03  countyfp20
-rw-rw-r--  1 cakidd cakidd      6651 Jan  3 17:31  countyseats_usgs_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      6471 Jan  3 17:31  countyseats_usgs_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      8251 Jan  3 17:31  courthousescounty_manysources_200203_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      1540 Jan  3 17:31  courthousesfederal_manysources_200203_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      1512 Jan  3 17:31  courthousesfederal_manysources_200203_utm_attrs.csv
drwxrwxr-x  3 cakidd cakidd      4096 Apr  1 17:03  crypto
drwxrwxr-x  5 cakidd cakidd      4096 May  8 08:43  crypto-venv
-rw-rw-r--  1 cakidd cakidd         0 Jan  8 23:12  .current_commit.hash
-rw-rw-r--  1 cakidd cakidd       181 Jan 21 18:32  CURRENT_LLM_STACK_NOTES.txt
-rw-rw-r--  1 cakidd cakidd        93 Jan 22 17:35  CURRENTSTATUS.md
-rw-rw-r--  1 cakidd cakidd      1363 Jan  3 17:31  cvfault_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      1271 Jan  3 17:31  cvfault_utm27_attrs.csv
-rw-rw-r--  1 cakidd cakidd     10005 Jan  3 17:31  cvpoly_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      9330 Jan  3 17:31  cvpoly_utm27_attrs.csv
-rw-rw-r--  1 cakidd cakidd      9776 Jan  3 17:31  cvpoly_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     42060 Jan  3 17:31  damsnoncoal_usgs_2002_ll27_attrs.csv
-rw-rw-r--  1 cakidd cakidd     78275 Jan  3 17:31  dams_usarmycorpsofengineers_200010_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     77760 Jan  3 17:31  dams_usarmycropsofengineers_200010_ll83_attrs.csv
drwxr-xr-x  8 cakidd cakidd      4096 Jun  1 13:44  data
drwxrwxr-x  4 cakidd cakidd      4096 May  8 18:20  db
-rw-rw-r--  1 cakidd cakidd      1072 Jan 23 08:53  debug_consciousness_bridge.md
drwxrwxr-x  2 cakidd cakidd      4096 Jan 11 12:22  debug-logs
-rwxrwxr-x  1 cakidd cakidd      3069 Apr 30 14:12  debug_unified_gateway.sh
-rw-rw-r--  1 cakidd cakidd       503 Feb  2 15:43  demo_msjarvis_ranked.py
-rw-rw-r--  1 cakidd cakidd      1522 Feb  2 15:36  demo_msjarvis_resources.py
-rwxrwxr-x  1 cakidd cakidd       509 Apr 30 14:12  deploy-brain.sh
-rwxrwxr-x  1 cakidd cakidd     26191 Apr 30 14:12  deploy_gap_aware.sh
-rwxrwxr-x  1 cakidd cakidd       409 Apr 30 14:12  deploy-gbim.sh
-rwxrwxr-x  1 cakidd cakidd       497 Apr 30 14:12  deploy-memory.sh
-rwxrwxr-x  1 cakidd cakidd       422 Apr 30 14:12  deploy-orchestrator.sh
-rwxrwxr-x  1 cakidd cakidd      8340 May 27 09:44  deploy_provenance.sh
-rwxrwxr-x  1 cakidd cakidd      4680 Apr 30 14:12  deploy.sh
-rw-rw-r--  1 cakidd cakidd      5967 Jun  5 18:45  docker-compose-core.yml
-rw-rw-r--  1 cakidd cakidd      4327 Apr 30 12:02  docker-compose-core.yml.bak.20260430-120237
-rw-rw-r--  1 cakidd cakidd      5579 May  7 22:20  docker-compose-core.yml.bak.20260507-222001
-rw-rw-r--  1 cakidd cakidd      5579 May  7 22:22  docker-compose-core.yml.bak.20260507-222222
-rw-rw-r--  1 cakidd cakidd      4729 May 30 10:30  docker-compose.gateway-only.generated.yml
-rw-rw-r--  1 cakidd cakidd       354 May 23 17:08  docker-compose.gbim.yml
-rw-rw-r--  1 cakidd cakidd     23752 Jan 19 14:11  docker-compose.golden.bak_bbb_clean_proxy
-rw-rw-r--  1 cakidd cakidd     23424 Jan 19 14:51  docker-compose.golden.bak_bbb_proxy_cmd_fix
-rw-rw-r--  1 cakidd cakidd     23505 Jan 19 15:08  docker-compose.golden.bak_bbb_uvicorn_fix
-rw-rw-r--  1 cakidd cakidd     23765 Jan 19 14:10  docker-compose.golden.bak_before_bbb_proxy2
-rw-rw-r--  1 cakidd cakidd     23808 Jan 19 13:46  docker-compose.golden.bak_before_brain_ports_cleanup
-rw-rw-r--  1 cakidd cakidd     23771 Jan 19 14:06  docker-compose.golden.bak_before_python3_cmd_fix
-rw-rw-r--  1 cakidd cakidd     23506 Jan 19 19:32  docker-compose.golden.bak_nbb_base_final
-rw-rw-r--  1 cakidd cakidd     23547 Jan 19 15:29  docker-compose.golden.bak_python310_compose_all
-rw-rw-r--  1 cakidd cakidd     23427 Jan 19 14:13  docker-compose.golden.bak_services_mapping_fix
-rw-rw-r--  1 cakidd cakidd     23519 Jan 19 15:41  docker-compose.golden.bak_web_research_cmd
-rw-rw-r--  1 cakidd cakidd     25472 Jun  5 18:20  docker-compose.golden.yml
-rw-rw-r--  1 cakidd cakidd       144 Jun  9 11:28  docker-compose.ledger-override.yml
-rw-rw-r--  1 cakidd cakidd      5956 Jun  5 18:26  docker-compose.llm-proxies.yml
-rw-rw-r--  1 cakidd cakidd     30324 Feb 16 13:28  docker-compose.MOTHERCARRIE.BAK.20260216-132826
-rw-rw-r--  1 cakidd cakidd     30786 Feb 16 13:28  docker-compose.MOTHERCARRIE.BAK.20260216-132834
-rw-rw-r--  1 cakidd cakidd       173 May 10 17:43  docker-compose.ollama-override.yml.disabled
-rw-rw-r--  1 cakidd cakidd      1744 Jun  9 15:05  docker-compose.override.yml
-rw-rw-r--  1 cakidd cakidd       270 Apr 16 12:37  docker-compose.override.yml.bak
-rw-rw-r--  1 cakidd cakidd      4246 Apr 30 12:02  docker-compose.override.yml.bak.20260430-120221
-rw-rw-r--  1 cakidd cakidd       224 May 15 23:07  docker-compose.override.yml.bak.20260515-230700
-rw-rw-r--  1 cakidd cakidd       686 Jun  7 11:29  docker-compose.override.yml.bak-20260607-112910
-rw-rw-r--  1 cakidd cakidd       215 Mar 24 16:42  docker-compose.override.yml.bak_agents
-rw-rw-r--  1 cakidd cakidd       158 Mar 24 16:42  docker-compose.override.yml.bak_depends
-rw-rw-r--  1 cakidd cakidd       365 Mar 24 16:44  docker-compose.override.yml.bak_localdb
-rw-rw-r--  1 cakidd cakidd      4741 Apr  1 23:49  docker-compose.override.yml.disabled
-rw-rw-r--  1 cakidd cakidd       152 May 23 17:08  docker-compose-patch.yml
-rw-rw-r--  1 cakidd cakidd     28282 May 23 17:08  docker-compose.RAG_WORKING_20260116.yml
-rw-rw-r--  1 cakidd cakidd     28305 Jan 22 22:37  docker-compose.RAG_WORKING_20260116.yml.bak-20260122223705
-rw-rw-r--  1 cakidd cakidd     28282 Jan 22 23:32  docker-compose.RAG_WORKING_20260116.yml.bak_gateway8050
-rw-rw-r--  1 cakidd cakidd     28282 Jan 22 23:38  docker-compose.RAG_WORKING_20260116.yml.bak_mainbrain8058
-rw-rw-r--  1 cakidd cakidd     28295 Jan 22 22:47  docker-compose.RAG_WORKING_20260116.yml.bak-portfix-20260122224758
-rw-rw-r--  1 cakidd cakidd     28297 Jan 22 23:19  docker-compose.RAG_WORKING_20260116.yml.bak_python310_fix
-rw-rw-r--  1 cakidd cakidd       741 May 23 17:08  docker-compose.rag.yml
-rw-r--r--  1 cakidd cakidd         0 May 23 17:08  docker-compose.recovered.yml
-rw-rw-r--  1 cakidd cakidd      2858 May 23 17:08  docker-compose.restored.yml
-rw-rw-r--  1 cakidd cakidd      3107 Jan  9 21:52  docker-compose.restored.yml.pre-hilbert-fix-1768013541
-rw-rw-r--  1 cakidd cakidd      3008 Jan 10 05:15  docker-compose.restored.yml.safe-1768040125
-rw-rw-r--  1 cakidd cakidd     23808 May 23 17:08  docker-compose.working.20260118-235132.yml
-rw-rw-r--  1 cakidd cakidd     23808 May 23 17:08  docker-compose.working.20260119-000202.yml
-rw-rw-r--  1 cakidd cakidd     62416 Jun 11 17:30  docker-compose.yml
-rw-rw-r--  1 cakidd cakidd     24460 Jan  9 11:08  docker-compose.yml.20llm.bak
-rw-rw-r--  1 cakidd cakidd     24430 Jan  9 10:16  docker-compose.yml.after-bbb.bak
-rw-rw-r--  1 cakidd cakidd     31248 Feb 16 13:40  docker-compose.yml.backup
-rw-rw-r--  1 cakidd cakidd     25530 Jan 13 08:40  docker-compose.yml.backup.1768311648
-rw-rw-r--  1 cakidd cakidd     25475 Jan 13 09:07  docker-compose.yml.backup.1768313257
-rw-rw-r--  1 cakidd cakidd     25533 Jan 13 09:10  docker-compose.yml.backup.1768313407
-rw-rw-r--  1 cakidd cakidd     26513 Jan 18 20:40  docker-compose.yml.backup.1768786837
-rw-rw-r--  1 cakidd cakidd     26519 Jan 18 21:07  docker-compose.yml.backup.1768788421
-rw-rw-r--  1 cakidd cakidd     59992 May 30 07:36  docker-compose.yml.backup-1780140997
-rw-rw-r--  1 cakidd cakidd     59992 May 30 07:48  docker-compose.yml.backup-1780141699
-rw-rw-r--  1 cakidd cakidd     30747 Feb 15 23:29  docker-compose.yml.backup_20260215_232944
-rw-rw-r--  1 cakidd cakidd     33979 Feb 18 08:59  docker-compose.yml.backup_20260218_085941
-rw-------  1 cakidd cakidd     28919 Mar 18 10:21  docker-compose.yml.backup_20260318_102158
-rw-------  1 cakidd cakidd     29396 Mar 18 10:32  docker-compose.yml.backup_20260318_103245
-rw-------  1 cakidd cakidd     29471 Mar 18 10:38  docker-compose.yml.backup_20260318_103829
-rw-------  1 cakidd cakidd     29725 Mar 18 11:00  docker-compose.yml.backup_20260318_110053
-rw-------  1 cakidd cakidd     29637 Mar 18 11:02  docker-compose.yml.backup_20260318_110223
-rw-------  1 cakidd cakidd     29657 Mar 18 11:09  docker-compose.yml.backup_20260318_110927
-rw-rw-r--  1 cakidd cakidd     35648 Mar 23 20:57  docker-compose.yml.backup_20260323_205752
-rw-rw-r--  1 cakidd cakidd     35648 Mar 23 21:14  docker-compose.yml.backup_20260323_211407
-rw-rw-r--  1 cakidd cakidd     47973 Apr  6 11:54  docker-compose.yml.backup_20260406_newservices
-rw-rw-r--  1 cakidd cakidd     24516 Jan  9 07:40  docker-compose.yml.backup_autonomous_learner_20260109-074048
-rw-rw-r--  1 cakidd cakidd     24493 Jan  9 09:11  docker-compose.yml.backup_gateway_ports_20260109-091103
-rw-rw-r--  1 cakidd cakidd     25540 Jan 12 22:17  docker-compose.yml.backup_jan13_consciousness
-rw-rw-r--  1 cakidd cakidd     33979 Feb 18 15:36  docker-compose.yml.backup_nbb_ports
-rw-rw-r--  1 cakidd cakidd     34523 Feb 18 16:08  docker-compose.yml.backup_nbb_ports_fixed
-rw-rw-r--  1 cakidd cakidd     62635 Jun  5 11:34  docker-compose.yml.bak
-rw-rw-r--  1 cakidd cakidd     25879 Jan 15 13:14  docker-compose.yml.bak.1768500857
-rw-rw-r--  1 cakidd cakidd      1560 Jan 18 23:01  docker-compose.yml.bak_1768574001
-rw-rw-r--  1 cakidd cakidd     27809 Jan 18 19:15  docker-compose.yml.bak.1768781706
-rw-rw-r--  1 cakidd cakidd     26507 Jan 18 21:52  docker-compose.yml.bak-1768791131
-rw-rw-r--  1 cakidd cakidd     26543 Jan 18 21:53  docker-compose.yml.bak-1768791194
-rw-rw-r--  1 cakidd cakidd     26524 Jan 18 22:02  docker-compose.yml.bak-1768791760
-rw-rw-r--  1 cakidd cakidd     37230 May 10 18:53  docker-compose.yml.bak_1778453637
-rw-rw-r--  1 cakidd cakidd     60154 May 30 16:35  docker-compose.yml.bak2
-rw-rw-r--  1 cakidd cakidd      3037 Jan 10 16:10  docker-compose.yml.bak.20260110161005
-rw-rw-r--  1 cakidd cakidd     27123 Feb  6 14:23  docker-compose.yml.bak.20260206142334
-rw-rw-r--  1 cakidd cakidd     27123 Feb  6 14:26  docker-compose.yml.bak.20260206142646
-rw-rw-r--  1 cakidd cakidd     45635 Apr  7 22:14  docker-compose.yml.bak.20260407-221457
-rw-rw-r--  1 cakidd cakidd       715 Apr  7 22:16  docker-compose.yml.bak.20260407-221640
-rw-rw-r--  1 cakidd cakidd      1352 Apr  8 17:32  docker-compose.yml.bak.20260408-173239
-rw-rw-r--  1 cakidd cakidd      3162 Apr 14 21:04  docker-compose.yml.bak.20260414-210440
-rw-rw-r--  1 cakidd cakidd      3181 Apr 14 21:05  docker-compose.yml.bak.20260414-210516
-rw-rw-r--  1 cakidd cakidd      3181 Apr 14 21:07  docker-compose.yml.bak.20260414-210743
-rw-rw-r--  1 cakidd cakidd      3179 Apr 14 21:10  docker-compose.yml.bak.20260414-211038
-rw-rw-r--  1 cakidd cakidd      3179 Apr 14 21:12  docker-compose.yml.bak.20260414-211257
-rw-rw-r--  1 cakidd cakidd      3179 Apr 15 11:11  docker-compose.yml.bak_20260415-111118
-rw-rw-r--  1 cakidd cakidd      3216 Apr 15 11:12  docker-compose.yml.bak_20260415-111235
-rw-rw-r--  1 cakidd cakidd     42988 Apr 16 14:12  docker-compose.yml.bak.20260416-141203
-rw-rw-r--  1 cakidd cakidd     42988 Apr 16 14:12  docker-compose.yml.bak.20260416-141224
-rw-rw-r--  1 cakidd cakidd     42988 Apr 16 14:13  docker-compose.yml.bak.20260416-141309
-rw-rw-r--  1 cakidd cakidd     42988 Apr 16 14:13  docker-compose.yml.bak.20260416-141316
-rw-rw-r--  1 cakidd cakidd     42988 Apr 16 14:14  docker-compose.yml.bak.20260416-141425
-rw-rw-r--  1 cakidd cakidd     43184 Apr 16 14:16  docker-compose.yml.bak.20260416-141603
-rw-rw-r--  1 cakidd cakidd     43183 Apr 16 14:17  docker-compose.yml.bak.20260416-141709
-rw-rw-r--  1 cakidd cakidd     43193 Apr 16 14:44  docker-compose.yml.bak.20260416_144451
-rw-rw-r--  1 cakidd cakidd     43193 Apr 16 14:48  docker-compose.yml.bak.20260416_144808
-rw-rw-r--  1 cakidd cakidd     43193 Apr 16 14:53  docker-compose.yml.bak.20260416_145312
-rw-rw-r--  1 cakidd cakidd     57040 Apr 17 14:43  docker-compose.yml.bak-20260417-144354
-rw-rw-r--  1 cakidd cakidd     41431 Apr 22 20:46  docker-compose.yml.bak.20260422-204609
-rw-rw-r--  1 cakidd cakidd     41468 Apr 22 20:47  docker-compose.yml.bak.20260422-204722
-rw-rw-r--  1 cakidd cakidd     41684 Apr 22 22:07  docker-compose.yml.bak.20260422_220748
-rw-rw-r--  1 cakidd cakidd     41684 Apr 23 09:53  docker-compose.yml.bak.20260423_095331
-rw-rw-r--  1 cakidd cakidd     46101 Apr 30 11:54  docker-compose.yml.bak.20260430-115408
-rw-rw-r--  1 cakidd cakidd     53593 Apr 30 20:26  docker-compose.yml.bak.20260430-202630
-rw-rw-r--  1 cakidd cakidd     54391 May  1 08:25  docker-compose.yml.bak.20260501
-rw-rw-r--  1 cakidd cakidd     54511 May  1 14:09  docker-compose.yml.bak.20260501-200948
-rw-rw-r--  1 cakidd cakidd     37269 May 10 19:27  docker-compose.yml.bak.20260510-192741
-rw-rw-r--  1 cakidd cakidd     36475 May 10 19:44  docker-compose.yml.bak.20260510-194401
-rw-rw-r--  1 cakidd cakidd     36602 May 10 19:50  docker-compose.yml.bak.20260510-195030
-rw-rw-r--  1 cakidd cakidd     38975 May 17 16:26  docker-compose.yml.bak.20260517-162627
-rw-rw-r--  1 cakidd cakidd     38975 May 17 16:30  docker-compose.yml.bak.20260517-163017
-rw-rw-r--  1 cakidd cakidd     39102 May 18 21:50  docker-compose.yml.bak.20260518-215027
-rw-r--r--  1 root   root       39433 May 22 20:44  docker-compose.yml.bak.20260522_204447
-rw-rw-r--  1 cakidd cakidd     39433 May 22 21:35  docker-compose.yml.bak.20260522T193400Z
-rw-rw-r--  1 cakidd cakidd     60346 Jun  1 18:33  docker-compose.yml.bak.20260601-183350
-rw-rw-r--  1 cakidd cakidd     60453 Jun  1 18:49  docker-compose.yml.bak.20260601-184933
-rw-rw-r--  1 cakidd cakidd     61704 Jun  5 08:56  docker-compose.yml.bak.20260605_085627
-rw-rw-r--  1 cakidd cakidd     62549 Jun  5 09:36  docker-compose.yml.bak.20260605093602
-rw-rw-r--  1 cakidd cakidd     64361 Jun  7 13:40  docker-compose.yml.bak.20260607134059
-rw-rw-r--  1 cakidd cakidd     62549 Jun  8 19:14  docker-compose.yml.bak.20260608-191406
-rw-rw-r--  1 cakidd cakidd     62416 Jun 11 17:29  docker-compose.yml.bak.20260611_172936
-rw-rw-r--  1 cakidd cakidd     28614 Jan  7 13:54  docker-compose.yml.bak_add_clock
-rw-rw-r--  1 cakidd cakidd     24493 Jan 19 13:33  docker-compose.yml.bak_before_unified_fix
-rw-rw-r--  1 cakidd cakidd     28017 Jan  7 14:01  docker-compose.yml.bak_drop_images
-rw-rw-r--  1 cakidd cakidd     26248 Jan  7 14:09  docker-compose.yml.bak_drop_roche
-rw-rw-r--  1 cakidd cakidd      3216 Apr 15 14:21  docker-compose.yml.bak_hilbert_cmdfix_20260415-142151
-rw-rw-r--  1 cakidd cakidd      3146 Apr 15 14:23  docker-compose.yml.bak_hilbert_depsfix_20260415-142323
-rw-rw-r--  1 cakidd cakidd      3214 Apr 15 14:23  docker-compose.yml.bak_hilbert_depsfix_20260415-142332
-rw-rw-r--  1 cakidd cakidd      3214 Apr 15 14:23  docker-compose.yml.bak_hilbert_depsfix_20260415-142340
-rw-rw-r--  1 cakidd cakidd     62471 Jun  8 19:37  docker-compose.yml.bak-ledger
-rw-rw-r--  1 cakidd cakidd     62471 Jun  8 20:12  docker-compose.yml.bak-ledger-20260608-201202
-rw-rw-r--  1 cakidd cakidd     61704 Jun  5 01:55  docker-compose.yml.bak.port5002.20260605-015500
-rw-rw-r--  1 cakidd cakidd     27712 Jan 18 16:38  docker-compose.yml.bak_ports_20260118163828
-rw-rw-r--  1 cakidd cakidd     24054 Jan 23 14:30  docker-compose.yml.bak_redis_env_1769196600
-rw-rw-r--  1 cakidd cakidd     24054 Jan 23 14:05  docker-compose.yml.bak_redis_fix_1769195136
-rw-rw-r--  1 cakidd cakidd     24054 Jan 23 14:14  docker-compose.yml.bak_redis_fix_1769195657
-rw-rw-r--  1 cakidd cakidd     23700 Jan 19 13:35  docker-compose.yml.bak_unified_cycle_fix
-rw-rw-r--  1 cakidd cakidd     27712 Jan 18 16:34  docker-compose.yml.bak_woah_20260118163402
-rw-rw-r--  1 cakidd cakidd     24463 Jan  9 10:13  docker-compose.yml.bbb.bak
-rw-rw-r--  1 cakidd cakidd      2873 Jan 10 06:35  docker-compose.yml.before_8010_fix_1768044953
-rw-rw-r--  1 cakidd cakidd     30324 Feb 15 23:51  docker-compose.yml.before_fix
-rw-rw-r--  1 cakidd cakidd     23669 Jan 22 21:13  docker-compose.yml.before_fix_20260122
-rw-rw-r--  1 cakidd cakidd     24489 Jan  9 21:42  docker-compose.yml.before_neuro_fix_1768012948
-rw-rw-r--  1 cakidd cakidd      1830 Jan 15 23:45  docker-compose.yml.broken
-rw-rw-r--  1 cakidd cakidd     24557 Jan  9 21:51  docker-compose.yml.broken-1768013498
-rw-------  1 cakidd cakidd     24385 Mar 26 17:56  docker-compose.yml.broken-20260326-175632
-rw-rw-r--  1 cakidd cakidd     30701 Feb 15 23:33  docker-compose.yml.broken_backup
-rw-rw-r--  1 cakidd cakidd     26745 Jan 19 13:21  docker-compose.yml.BROKEN_BACKUP
-rw-rw-r--  1 cakidd cakidd     30701 Feb 15 23:48  docker-compose.yml.broken_spiritual
-rw-rw-r--  1 cakidd cakidd     25602 Jan 14 05:49  docker-compose.yml.chroma-backup-20260114054916
-rw-rw-r--  1 cakidd cakidd     25602 Jan 14 06:00  docker-compose.yml.chroma-backup-20260114060013
-rw-rw-r--  1 cakidd cakidd      2771 Apr 15 16:02  docker-compose.yml.corrupt.20260415-1601
-rw-rw-r--  1 cakidd cakidd     23695 Jan 22 21:26  docker-compose.yml.full_backup_20260122
-rw-rw-r--  1 cakidd cakidd      3160 Apr 15 16:38  docker-compose.yml.hilbert-experiment.20260415-163850
-rw-rw-r--  1 cakidd cakidd     24460 Jan  9 11:09  docker-compose.yml.nbb.bak
-rw-rw-r--  1 cakidd cakidd     42148 Apr 21 09:58  docker-compose.yml.pre_dsn_fix
-rw-rw-r--  1 cakidd cakidd      3107 Jan  9 21:52  docker-compose.yml.pre-hilbert-fix-1768013541
-rw-rw-r--  1 cakidd cakidd      3192 Apr 15 16:11  docker-compose.yml.pre-hilbert-image-20260415-161150
-rw-rw-r--  1 cakidd cakidd      3201 Apr 15 16:26  docker-compose.yml.pre-hilbert-noports.20260415-162654
-rw-rw-r--  1 cakidd cakidd      3191 Apr 15 16:25  docker-compose.yml.pre-hilbert-portfix.20260415-162529
-rw-rw-r--  1 cakidd cakidd     31012 Feb 16 21:37  docker-compose.yml.pre_judges
-rw-rw-r--  1 cakidd cakidd     37264 May 10 17:50  docker-compose.yml.pre_ollama_env_bak
-rw-rw-r--  1 cakidd cakidd     42246 Apr 22 23:43  docker-compose.yml.pre-secrets-fix
-rw-rw-r--  1 cakidd cakidd      3107 Jan 10 05:15  docker-compose.yml.safe-1768040125
-rw-rw-r--  1 cakidd cakidd       551 Jan 19 09:55  Dockerfile
-rw-rw-r--  1 cakidd cakidd       341 Jan 16 01:08  Dockerfile.20llm
-rw-rw-r--  1 cakidd cakidd       243 Jan  7 13:23  Dockerfile.agents
-rw-rw-r--  1 cakidd cakidd       432 Jun  1 17:04  Dockerfile.auth_api
-rw-rw-r--  1 cakidd cakidd       418 Jun  1 16:48  Dockerfile.auth_api.bak.20260601-164830
-rw-rw-r--  1 cakidd cakidd       425 Jun  1 16:48  Dockerfile.auth_api.bak.20260601-164835
drwxrwxr-x  2 cakidd cakidd      4096 Mar 10 13:38  dockerfile_backups_llm
-rw-rw-r--  1 cakidd cakidd       272 Jan 19 13:51  Dockerfile.bak_before_python3_fix
-rw-rw-r--  1 cakidd cakidd       594 May 28 19:39  Dockerfile.brain
-rw-rw-r--  1 cakidd cakidd       552 Mar  9 16:59  Dockerfile.brain.backup_20260309_165916
-rw-rw-r--  1 cakidd cakidd       606 Mar 18 10:35  Dockerfile.brain.backup_20260318_103552
-rw-rw-r--  1 cakidd cakidd       578 May 28 19:39  Dockerfile.brain.bak-20260528193952
-rw-rw-r--  1 cakidd cakidd       285 Jan  7 09:13  Dockerfile.consciousnessbridge
-rw-rw-r--  1 cakidd cakidd       386 Apr 30 14:04  Dockerfile.forge
-rw-rw-r--  1 cakidd cakidd       310 Jan 18 15:21  Dockerfile.full_neuro
-rw-rw-r--  1 cakidd cakidd       272 Jan 19 13:51  Dockerfile.gateway
-rw-rw-r--  1 cakidd cakidd       294 May 16 22:22  Dockerfile.gis_rag
-rw-rw-r--  1 cakidd cakidd       195 Jan  9 13:52  Dockerfile-llm10-proxy
-rw-rw-r--  1 cakidd cakidd       195 Jan  9 13:52  Dockerfile-llm11-proxy
-rw-rw-r--  1 cakidd cakidd       195 Jan  9 13:52  Dockerfile-llm12-proxy
-rw-rw-r--  1 cakidd cakidd       195 Jan  9 13:52  Dockerfile-llm13-proxy
-rw-rw-r--  1 cakidd cakidd       195 Jan  9 13:52  Dockerfile-llm14-proxy
-rw-rw-r--  1 cakidd cakidd       195 Jan  9 13:52  Dockerfile-llm15-proxy
-rw-rw-r--  1 cakidd cakidd       195 Jan  9 13:52  Dockerfile-llm16-proxy
-rw-rw-r--  1 cakidd cakidd       195 Jan  9 13:52  Dockerfile-llm17-proxy
-rw-rw-r--  1 cakidd cakidd       195 Jan  9 13:52  Dockerfile-llm18-proxy
-rw-rw-r--  1 cakidd cakidd       195 Jan  9 13:52  Dockerfile-llm19-proxy
-rw-rw-r--  1 cakidd cakidd       193 Jan  9 13:52  Dockerfile-llm1-proxy
-rw-rw-r--  1 cakidd cakidd       195 Jan  9 13:52  Dockerfile-llm20-proxy
-rw-rw-r--  1 cakidd cakidd       195 Jan  9 13:52  Dockerfile-llm21-proxy
-rw-rw-r--  1 cakidd cakidd       195 Jan  9 13:52  Dockerfile-llm22-proxy
-rw-rw-r--  1 cakidd cakidd       193 Jan  9 13:52  Dockerfile-llm2-proxy
-rw-rw-r--  1 cakidd cakidd       193 Jan  9 13:52  Dockerfile-llm3-proxy
-rw-rw-r--  1 cakidd cakidd       193 Jan  9 13:52  Dockerfile-llm4-proxy
-rw-rw-r--  1 cakidd cakidd       193 Jan  9 13:52  Dockerfile-llm5-proxy
-rw-rw-r--  1 cakidd cakidd       193 Jan  9 13:52  Dockerfile-llm6-proxy
-rw-rw-r--  1 cakidd cakidd       193 Jan  9 13:52  Dockerfile-llm7-proxy
-rw-rw-r--  1 cakidd cakidd       193 Jan  9 13:52  Dockerfile-llm8-proxy
-rw-rw-r--  1 cakidd cakidd       193 Jan  9 13:52  Dockerfile-llm9-proxy
-rw-rw-r--  1 cakidd cakidd       232 Mar 10 13:36  Dockerfile.lm_synthesizer.stub.bak
-rw-rw-r--  1 cakidd cakidd       281 Feb  3 17:00  Dockerfile.local_resources
-rw-rw-r--  1 cakidd cakidd       609 Feb 22 09:17  Dockerfile.nbb_icontainers_fastapi
-rw-rw-r--  1 cakidd cakidd       526 Jun  5 00:15  Dockerfile.neuro
-rw-rw-r--  1 cakidd cakidd       178 Jan 18 15:58  Dockerfile.neuro-prefrontal-patched
-rw-rw-r--  1 cakidd cakidd        30 Feb  8 22:56  Dockerfile.qualia
-rw-rw-r--  1 cakidd cakidd        30 Jan 15 14:00  Dockerfile.qualia.bak
-rw-rw-r--  1 cakidd cakidd       376 Jan  7 05:53  Dockerfile.rag
-rw-rw-r--  1 cakidd cakidd       314 Mar 10 17:52  Dockerfile_rag_real
-rw-rw-r--  1 cakidd cakidd       322 May 23 13:02  Dockerfile.rag_server
-rw-rw-r--  1 cakidd cakidd       440 Jan 18 22:02  Dockerfile.rag_server_main
-rw-rw-r--  1 cakidd cakidd       443 Jan 14 10:27  Dockerfile.ragservermain
-rw-rw-r--  1 cakidd cakidd       181 May  3 17:35  Dockerfile.session-sidecar
-rw-rw-r--  1 cakidd cakidd       168 Apr 21 16:41  Dockerfile.session-sidecar.bak
-rw-rw-r--  1 cakidd cakidd       247 Jan  7 13:23  Dockerfile.swarm
-rw-rw-r--  1 cakidd cakidd       229 May 27 12:06  Dockerfile.web_research
-rw-rw-r--  1 cakidd cakidd       342 Feb  7 17:13  Dockerfile.woah
-rw-rw-r--  1 cakidd cakidd      1555 Jun  3 22:39  .dockerignore
drwxrwxr-x  9 cakidd cakidd      4096 May  8 23:25  docs
-rwxrwxr-x  1 cakidd cakidd       504 Jan 12 07:49  dump_gdb_result.sh
-rw-rw-r--  1 cakidd cakidd       258 Jan 18 16:20  dynamic_port_service_no_flask.py
-rw-rw-r--  1 cakidd cakidd      3683 Mar 10 08:33  egeria-emergent.txt
-rw-rw-r--  1 cakidd cakidd    141117 Jan  3 17:31  empowermentzonesandenterprisecommunitiesbytract_uscens_30c72907_attrs.csv
-rw-rw-r--  1 cakidd cakidd      3700 Jan  3 17:31  empowermentzonesandenterprisecommunities_uscensus_2002_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     19122 Feb 22 21:59  enrich_from_attrs.log
-rw-rw-r--  1 cakidd cakidd     23042 Feb 22 21:42  enrich_from_attrs.py
-rw-rw-r--  1 cakidd cakidd     11134 Feb 22 21:14  enrich_where.log
-rw-rw-r--  1 cakidd cakidd      1689 Feb 22 20:59  enrich_where.py
-rw-rw-r--  1 cakidd cakidd      9020 Jun  9 14:38  .env
drwxrwxr-x  2 cakidd cakidd      4096 Jan 10 15:40  env
-rw-------  1 cakidd cakidd      8119 May  5 19:29  .env.backup-20260505
-rw-------  1 cakidd cakidd      6546 May 19 20:52  .env.bak
-rw-------  1 cakidd cakidd      6614 Jun  1 16:06  .env.bak.20260601-160603
-rw-r--r--  1 root   root        9099 Jun  8 11:08  .env.bak.2026-06-08-110803
-rw-rw-r--  1 cakidd cakidd      9053 Jun  8 19:14  .env.bak.20260608-191406
-rw-rw-r--  1 cakidd cakidd      9061 Jun  9 13:48  .env.bak.20260609T134810
-rw-------  1 cakidd cakidd      9170 Jun  5 01:38  .env.bak.gis_collection_20260605-013821
-rw-------  1 cakidd cakidd      8119 May  5 19:28  .env.complete
-rw-rw-r--  1 cakidd cakidd       336 May  3 00:38  .env.contracts.anvil
-rw-------  1 cakidd cakidd      1554 May  3 22:01  .env.example
-rw-------  1 cakidd cakidd       540 May  5 19:29  .env.stub.bak
-rw-rw-r--  1 cakidd cakidd     12259 Jan  9 17:39  error_summary.log
drwxrwxr-x  2 cakidd cakidd      4096 Feb  4 16:00  etl
-rw-rw-r--  1 cakidd cakidd     27965 May  8 20:12  eval_routed.csv
-rw-rw-r--  1 cakidd cakidd     30438 May  8 20:25  eval_routed_final.csv
-rw-rw-r--  1 cakidd cakidd     26262 May  8 20:12  eval_unrouted.csv
-rw-rw-r--  1 cakidd cakidd     30181 May  8 20:25  eval_unrouted_final.csv
-rw-rw-r--  1 cakidd cakidd       850 Feb  6 22:29  example_wv_entangled_request.json
-rw-rw-r--  1 cakidd cakidd      3968 Feb  6 22:47  example_wv_entangled_response.json
-rw-rw-r--  1 cakidd cakidd      2381 Jan  3 17:31  excursionpassengertrains_wvdof_200102_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      2325 Jan  3 17:31  excursionpassengertrains_wvdof_200102_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd       791 Jan 11 23:06  export_gbim_sample.py
-rw-rw-r--  1 cakidd cakidd         0 May 18 23:58  exporting
drwxrwxr-x  3 cakidd cakidd      4096 Jan 25 10:56  exports
-rw-rw-r--  1 cakidd cakidd    269289 Jan  3 17:31  facilities_epa_200203_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd    267986 Jan  3 17:31  facilities_epa_200203_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd  11728096 Jan  3 17:31  faultgl_reg_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     32998 Jan  3 17:31  fault_reg_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     32263 Jun  8 19:08  fayette_institutional_parcels.csv
-rw-rw-r--  1 cakidd cakidd     33223 Jun  8 19:13  fayette_network_full.csv
-rw-rw-r--  1 cakidd cakidd      5534 Jun  8 19:22  fayette_nuttall_parcels.csv
-rw-rw-r--  1 cakidd cakidd  23716905 Jan  3 17:31  features_attrs.csv
-rw-rw-r--  1 cakidd cakidd      5590 May 30 21:55  finding_001_response.json
-rw-rw-r--  1 cakidd cakidd      3013 May 30 21:58  FINDINGS.md
-rw-rw-r--  1 cakidd cakidd     63212 Jan  3 17:31  fire_departments_attrs.csv
-rw-rw-r--  1 cakidd cakidd     68568 Jan  3 17:31  fire_dept_wvdem_092017_utm83_attrs.csv
-rwxrwxr-x  1 cakidd cakidd       427 Jan 16 01:06  fix-20llm.sh
drwxrwxr-x  3 cakidd cakidd      4096 Jun  3 11:14  .fixbackups
-rw-rw-r--  1 cakidd cakidd      2310 Jun  5 17:55  fix_chat_handler.py
-rw-rw-r--  1 cakidd cakidd      3758 Apr 11 08:05  fix_jarvis.log
-rw-rw-r--  1 cakidd cakidd      1231 Jun  5 17:57  fix_persona_injection.py
-rw-rw-r--  1 cakidd cakidd      1523 Jun  5 18:00  fix_sandwich_prompt.py
-rw-rw-r--  1 cakidd cakidd  11703819 Jan  3 17:31  floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83_attrs.csv
drwxrwxr-x  5 cakidd cakidd      4096 Feb 14 11:47  .format-venv
-rwxrwxr-x  1 cakidd cakidd      1185 Jan  7 13:29  full_fs_indexer.sh
-rw-r--r--  1 cakidd cakidd      1135 Jan 21 21:21  gateway8050_inline.py
-rw-r--r--  1 cakidd cakidd     30814 Jun  6 22:10  gateway_backup_20260607_1003.py
-rw-rw-r--  1 cakidd cakidd      2856 Jan 19 11:33  gateway_chat_attempt.log
-rwxrwxr-x  1 cakidd cakidd       273 Jun  6 19:37  gateway-entrypoint.sh
-rw-rw-r--  1 cakidd cakidd         0 Feb 22 13:07  gbim_backbone_rich.dump.sql
-rw-rw-r--  1 cakidd cakidd       231 Jan 12 15:04  gbim_chroma.py
-rw-rw-r--  1 cakidd cakidd     58007 Jan 11 23:17  gbim_full_metadata.csv
drwxrwxr-x  3 cakidd cakidd      4096 May 31 21:44  gbim_ingest
-rw-rw-r--  1 cakidd cakidd      1387 Jan 12 16:20  gbim_orchestrator.py
-rw-rw-r--  1 cakidd cakidd      2868 Jan 11 23:16  gbim_sample_metadata.csv
-rw-rw-r--  1 cakidd cakidd         3 Feb  4 15:34  gbim_worldview_entity_clean.sql
-rw-rw-r--  1 cakidd cakidd         0 Feb 22 13:15  gbim_worldview_entity_data.sql
-rw-rw-r--  1 cakidd cakidd      1342 Feb 22 12:47  gbim_worldview_entity_fresh.sql
-rw-rw-r--  1 cakidd cakidd      1329 Jan 12 16:52  gdb_integration_service.log
-rw-rw-r--  1 cakidd cakidd      4041 Jan 12 07:51  gdb_result_snapshot.json
-rwxrwxr-x  1 cakidd cakidd      1724 Jan 26 14:49  generate_attrs_sql.sh
-rwxrwxr-x  1 cakidd cakidd      4820 Apr  4 06:51  generate_spiritual_inventories.py
-rw-rw-r--  1 cakidd cakidd      3811 Jan 17 23:23  geodb_collection_manifest.csv
-rw-rw-r--  1 cakidd cakidd       958 Jan 23 17:21  geodb_restore_plan.md
-rw-rw-r--  1 cakidd cakidd   5090366 Jan  3 17:31  geographicalnamesonusgstopomaps_usgs_200601_ll27_attrs.csv
-rw-rw-r--  1 cakidd cakidd   6693142 Jan  3 17:31  geographicalnamesonusgstopomaps_usgs_200601_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd   4916485 Jan  3 17:31  geographicnamesonusgstopomaps_current_usgs_20110801_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd   4942226 Jan  3 17:31  geographicnamesonusgstopomaps_current_usgs_20110801_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd    971906 Jan  3 17:31  geographicnamesonusgstopomaps_historical_usgs_20110801_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd   1230654 Jan  3 17:31  geographicnamesonusgstopomaps_historical_usgs_20110801_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd   5575035 Jan  3 17:31  geographicnamesonusgstopomaps_usgs_20110801_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd   5859524 Jan  3 17:31  geographicnamesonusgstopomaps_usgs_20110801_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd    485287 Jan  3 17:31  geolgyl_reg_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     51685 Jan  3 17:31  geolgyp_reg_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     29337 Jan  3 17:31  geotextl_reg_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      1252 Jan 11 22:45  gis_candidates_global.txt
-rw-rw-r--  1 cakidd cakidd       164 Jan 11 22:34  gis_candidates_stage2.txt
-rw-rw-r--  1 cakidd cakidd       952 Jan 12 18:07  gisgeodb_storage.py
-rw-rw-r--  1 cakidd cakidd      1693 Jan 16 20:11  gisgeodbstorage.py
drwxrwxr-x  2 cakidd cakidd      4096 Feb  3 13:27  gis_notes
-rw-rw-r--  1 cakidd cakidd       255 Jan 12 08:49  gis_pipeline_8819.log
-rw-rw-r--  1 cakidd cakidd      2044 Jan 30 10:28  gis_rag_query.py
-rw-rw-r--  1 cakidd cakidd      1269 Jan 30 15:28  gis_rag_server.py
-rw-rw-r--  1 cakidd cakidd      8297 May 31 22:47  gis_rag_service.py
-rw-rw-r--  1 cakidd cakidd      1410 Jun  1 11:28  gis_routes.py
drwxrwxr-x  3 cakidd cakidd      4096 May 16 22:22  gis_service
-rw-rw-r--  1 cakidd cakidd       317 Jan 12 08:42  gis_statewide_run.log
drwxrwxr-x  9 cakidd cakidd      4096 Jun 10 10:16  .git
-rw-rw-r--  1 cakidd cakidd      1798 Jun  6 21:48  .gitignore
-rwxrwxr-x  1 cakidd cakidd       746 Mar 29 13:44  go_no_go.sh
-rw-rw-r--  1 cakidd cakidd    836563 Jan  3 17:31  hazardmitigationbuyout_20250929_polygons_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd    873008 Jan  3 17:31  hazardmitigationbuyout_20250929_polygons_wma84_attrs.csv
-rw-rw-r--  1 cakidd cakidd      9254 Jan  3 17:31  healthruralfacilities_manysources_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      5456 Apr 12 11:26  healthy-state-20260412-1126.txt
-rw-rw-r--  1 cakidd cakidd      6038 Jan  3 17:31  highered_wvemd_072420_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      6136 Jan  3 17:31  highered_wvemd_072420_wgc84_attrs.csv
-rw-rw-r--  1 cakidd cakidd     13883 May  8 19:34  hilbert_audit_20260508_193423.log
-rw-rw-r--  1 cakidd cakidd        65 May  8 19:30  hilbert_audit_output.txt
-rwxrwxr-x  1 cakidd cakidd      6462 May  8 19:34  hilbert_paper_verification.sh
-rw-rw-r--  1 cakidd cakidd      4783 May  8 19:30  hilbert_verification_20260508_193018.log
-rw-rw-r--  1 cakidd cakidd       558 Jan  3 17:31  hospitals_attrs.csv
drwxrwxr-x  2 cakidd cakidd      4096 Jan 13 17:43  HOST_LEARNER_CHROMA_PATH
-rw-rw-r--  1 cakidd cakidd       290 Jan  3 17:31  impact_reg_ll83_attrs.csv
-rwxrwxr-x  1 cakidd cakidd      7002 Jan 30 15:25  index_gis_to_chroma.py
-rwxrwxr-x  1 cakidd cakidd      7209 Jan 30 10:31  index_gis_to_chroma.py.bak_20260130103111
-rw-rw-r--  1 cakidd cakidd     85529 Jan  3 17:31  indexgrid15minutequads_wvgistc_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd    184549 Jan  3 17:31  indexgrid15minutequads_wvgistc_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd    245526 Jan  3 17:31  indexgrid15minutewithcounties_wvgistc_utm27_attrs.csv
-rw-rw-r--  1 cakidd cakidd     14315 Jan  3 17:31  indexgrid1minutequads_wvgistc_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     18057 Jan  3 17:31  industrialbuildings_wvdo_200807_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     32321 Jan  3 17:31  industrialparks_wvdo_200078_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     53128 Jan  3 17:31  industrialsites_wvdo_200807_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     10439 Jan  3 17:31  inedexgrid1minutequads_wvgistc_utm83_attrs.csv
drwxrwxr-x  2 cakidd cakidd      4096 May 12 01:13  infra
drwxrwxr-x  5 cakidd cakidd      4096 Mar 18 16:18  ingest
-rw-rw-r--  1 cakidd cakidd      2988 Jan 23 20:55  ingest_attrs_to_chroma.py
-rw-rw-r--  1 cakidd cakidd      1173 Feb  1 14:18  ingest_gbimworldviewentities_from_csv.py
-rw-rw-r--  1 cakidd cakidd      2120 Feb  2 15:06  ingest_kanawha_images.py
-rw-rw-r--  1 cakidd cakidd      5174 Feb  2 14:44  ingest_kanawha_resources.py
-rw-rw-r--  1 cakidd cakidd       132 Jan 12 13:28  ingest.log
-rw-rw-r--  1 cakidd cakidd      1733 Jan 12 13:35  ingest_missing_attrs.py
-rw-rw-r--  1 cakidd cakidd     77199 Jan 12 13:36  ingest_missing.log
-rw-rw-r--  1 cakidd cakidd      1263 Jan 12 14:25  ingest_msjarvis_corpus.py
-rw-rw-r--  1 cakidd cakidd      1783 Jan 12 14:14  ingest_personal_pdfs.py
-rw-rw-r--  1 cakidd cakidd      3892 May  5 17:54  ingest_wvgistc_to_chroma.py
-rwxrwxr-x  1 cakidd cakidd      2604 Jan 31 20:26  ingest_wv_income_maintenance_manual.py
-rw-rw-r--  1 cakidd cakidd      1303 Apr 30 17:06  init_db.sql
drwxrwxr-x  2 cakidd cakidd      4096 Jan  5 02:02  integration_layer
-rw-rw-r--  1 cakidd cakidd     17840 Jan  3 17:31  intermodalterminalfacilities_usdot_1997_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     21472 Jan  3 17:31  intermodalterminalfacilities_usdot_1997_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd         0 May 18 23:58 '[internal]'
-rwxrwxr-x  1 cakidd cakidd       567 Jun  8 19:01  investigate_fayette.sh
drwxrwxr-x  2 cakidd cakidd      4096 Mar 18 16:18  itest-consciousness-bridge-logs
drwxrwxr-x  2 cakidd cakidd     12288 Mar 18 16:18  itest-i-containers-logs
-rw-r--r--  1 cakidd cakidd      5696 Feb 19 21:47 'itus_addr AS address, -- site address'
-rw-rw-r--  1 cakidd cakidd      2612 Mar  9 21:29  jarvis-20llm-openapi.json
drwxrwxr-x  2 cakidd cakidd      4096 Jan 18 23:03  jarvis-chroma
-rw-rw-r--  1 cakidd cakidd      8257 Apr 12 18:17  jarviscryptopolicy.py
-rw-rw-r--  1 cakidd cakidd   2276588 Apr 16 17:00  jarvis_eeg_delta_30s.log
-rw-rw-r--  1 cakidd cakidd       159 Jan 12 14:02  jarvis_env.sh
-rw-rw-r--  1 cakidd cakidd         0 May 18 23:58 '[jarvis-judge-alignment'
-rw-rw-r--  1 cakidd cakidd         0 May 18 23:58 '[jarvis-judge-alignment]'
-rw-rw-r--  1 cakidd cakidd         0 May 18 23:58 '[jarvis-judge-consistency'
-rw-rw-r--  1 cakidd cakidd         0 May 18 23:58 '[jarvis-judge-consistency]'
-rw-rw-r--  1 cakidd cakidd         0 May 18 23:58 '[jarvis-judge-ethics'
-rw-rw-r--  1 cakidd cakidd         0 May 18 23:58 '[jarvis-judge-ethics]'
-rw-rw-r--  1 cakidd cakidd         0 May 18 23:58 '[jarvis-judge-pipeline'
-rw-rw-r--  1 cakidd cakidd         0 May 18 23:58 '[jarvis-judge-pipeline]'
-rw-rw-r--  1 cakidd cakidd         0 May 18 23:58 '[jarvis-judge-truth]'
-rw-rw-r--  1 cakidd cakidd         0 May 18 23:58 '[jarvis-lm-synthesizer'
-rw-rw-r--  1 cakidd cakidd         0 May 18 23:58 '[jarvis-lm-synthesizer]'
-rw-rw-r--  1 cakidd cakidd      3504 Apr 30 14:12  judge_ethics_filter.py
drwxrwxr-x  2 cakidd cakidd      4096 Mar 20 22:07  judge-keys
-rw-rw-r--  1 cakidd cakidd     16006 Apr 30 14:12  judge_pipeline.py
-rw-rw-r--  1 cakidd cakidd      7194 Apr 30 14:12  judge_truth_filter.py
drwxrwxr-x  3 cakidd cakidd      4096 Mar 26 09:13  knowledge
drwxrwxr-x  3 cakidd cakidd      4096 Feb 16 09:17  knowledge_pdfs
-rw-rw-r--  1 cakidd cakidd      1122 Mar 24 11:06  KNOWN_ISSUES.md
-rw-rw-r--  1 cakidd cakidd       499 Jan 21 21:02  KNOWN_LIMITATIONS_20LLM_SEQUENTIAL.txt
-rw-rw-r--  1 cakidd cakidd      1594 May 19 22:10  kts_ledger_import.py
-rw-rw-r--  1 cakidd cakidd         1 Jun  2 11:31  kyc-registry-deploy.log
-rw-rw-r--  1 cakidd cakidd     22273 Mar 10 17:18  last-build-after-woah-llm22.log
-rw-rw-r--  1 cakidd cakidd     21418 Mar 10 17:16  last-build-final.log
-rw-rw-r--  1 cakidd cakidd     20916 Mar 10 17:14  last-build-full.log
-rw-rw-r--  1 cakidd cakidd     15022 Mar 10 17:10  last-build.log
-rw-rw-r--  1 cakidd cakidd     20867 Mar 10 17:11  last-build-no-llm12.log
-rw-rw-r--  1 cakidd cakidd       795 Feb 22 14:08  layer_manifest.csv
-rw-rw-r--  1 cakidd cakidd       221 Apr  1 15:11  LEARNER_STATUS.txt
-rw-rw-r--  1 cakidd cakidd     27936 Jan  3 17:31  libraries_manysources_2001_ll27_attrs.csv
-rw-rw-r--  1 cakidd cakidd     32934 Jan  3 17:31  libraries_manysources_2001_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd       612 Feb  2 15:59  list_due_for_verification.py
-rw-rw-r--  1 cakidd cakidd      1670 May 23 14:45  llm10_health_proxy.py
-rw-rw-r--  1 cakidd cakidd      1578 Mar 10 17:16  llm10_health_proxy.py.bak
-rw-rw-r--  1 cakidd cakidd      1479 May 23 14:45  llm11_health_proxy.py
-rw-rw-r--  1 cakidd cakidd      1519 May 23 14:45  llm12_health_proxy.py
-rw-rw-r--  1 cakidd cakidd      1427 Mar 10 17:14  llm12_health_proxy.py.bak
-rw-rw-r--  1 cakidd cakidd      1692 May 23 14:45  llm13_health_proxy.py
-rw-rw-r--  1 cakidd cakidd      1668 May 23 14:45  llm14_health_proxy.py
-rw-rw-r--  1 cakidd cakidd      1674 May 23 14:45  llm15_health_proxy.py
-rw-rw-r--  1 cakidd cakidd      1519 May 23 14:45  llm16_health_proxy.py
-rw-rw-r--  1 cakidd cakidd      1519 May 23 14:45  llm17_health_proxy.py
-rw-rw-r--  1 cakidd cakidd      1686 May 23 14:45  llm18_health_proxy.py
-rw-rw-r--  1 cakidd cakidd      1674 May 23 14:45  llm19_health_proxy.py
-rw-rw-r--  1 cakidd cakidd      1509 May 23 14:45  llm1_health_proxy.py
-rw-rw-r--  1 cakidd cakidd      1494 May 23 14:45  llm20_health_proxy.py
-rw-rw-r--  1 cakidd cakidd      1402 Mar 10 17:14  llm20_health_proxy.py.bak
-rw-rw-r--  1 cakidd cakidd      1680 May 23 14:45  llm21_health_proxy.py
-rw-rw-r--  1 cakidd cakidd      1495 May 23 14:45  llm22_health_proxy.py
-rw-rw-r--  1 cakidd cakidd      1403 Mar 10 17:17  llm22_health_proxy.py.bak
-rw-rw-r--  1 cakidd cakidd      1497 May 23 14:45  llm2_health_proxy.py
-rw-rw-r--  1 cakidd cakidd      1491 Mar 10 17:14  llm2_health_proxy.py.bak
-rw-rw-r--  1 cakidd cakidd      1692 May 23 14:45  llm3_health_proxy.py
-rw-rw-r--  1 cakidd cakidd      1509 May 23 14:45  llm4_health_proxy.py
-rw-rw-r--  1 cakidd cakidd      1668 May 23 14:45  llm5_health_proxy.py
-rw-rw-r--  1 cakidd cakidd      1504 May 23 14:45  llm6_health_proxy.py
-rw-rw-r--  1 cakidd cakidd      1514 May 23 14:45  llm7_health_proxy.py
-rw-rw-r--  1 cakidd cakidd      1509 May 23 14:45  llm8_health_proxy.py
-rw-rw-r--  1 cakidd cakidd      1534 May 23 14:45  llm9_health_proxy.py
-rw-r--r--  1 cakidd cakidd      7880 May 18 22:47  llm_consensus_20_FINAL_EDIT.py
-rw-r--r--  1 cakidd cakidd      8062 Jun  5 18:07  llm_consensus_20_FINAL.py
-rw-r--r--  1 cakidd cakidd      8177 May 14 21:42  llm_consensus_20_FINAL.py.bak
drwxrwxr-x  2 cakidd cakidd      4096 Jan 10 12:07  llm_health_proxies
drwxrwxr-x  2 cakidd cakidd      4096 Jan 10 12:11  llm_servers_from_backup
-rw-rw-r--  1 cakidd cakidd      2848 Apr 30 14:12  lm_judge_helper.py
-rw-rw-r--  1 cakidd cakidd      3021 Mar 20 05:29  load_all_attrs_csvs.py
-rw-rw-r--  1 cakidd cakidd         0 Jan 26 14:49  load_all_attrs.sql
-rw-rw-r--  1 cakidd cakidd       853 Jan 11 23:41  load_hospitals.sql
-rw-rw-r--  1 cakidd cakidd      4101 Feb 22 23:15  load_services_attrs_and_enrich.py
-rw-rw-r--  1 cakidd cakidd      2836 Feb  2 16:11  local_resources_export.csv
drwxrwxr-x  9 cakidd cakidd      4096 Jun  5 08:47  logs
drwxrwxr-x  2 cakidd cakidd     81920 Feb 16 22:12  logs-archive
-rw-rw-r--  1 cakidd cakidd       534 Jan 30 15:35  logs-gis_rag_server_8055.log
-rw-rw-r--  1 cakidd cakidd      3522 Jan 10 15:37  logs-rag_server_8003.log
-rw-rw-r--  1 cakidd cakidd      3305 Jan 10 16:00  logs-rag_server_dynamic.log
-rw-rw-r--  1 cakidd cakidd       245 Jan 10 12:34  logs-rag_server.log
-rw-rw-r--  1 cakidd cakidd         0 May 15 21:02  main
-rw-rw-r--  1 cakidd cakidd       300 Feb  8 10:53  mainbrain.log
-rw-rw-r--  1 cakidd cakidd     46742 Jun  3 13:35  main_brain.py
-rw-rw-r--  1 cakidd cakidd     46373 May 11 11:04  main_brain.py.bak.20260511-110458
-rw-rw-r--  1 cakidd cakidd     46369 Jun  3 13:13  main_brain.py.bak.20260603-131329
-rw-rw-r--  1 cakidd cakidd      1569 Feb  2 15:37  main.py
-rw-rw-r--  1 cakidd cakidd     16231 Jan  3 17:31  majorriversandlakesline_nhd_2002_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     15603 Jan  3 17:31  majorriversandlakesline_nhd_2002_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     26160 Jan  3 17:31  majorriversandlakespolygon_nhd_2002_poly_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd   1277432 Jan  3 17:31  manufacturingandbusiness_wvdo_200803_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      1623 Jan  3 17:31  metfacp_reg_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      4309 Jan  3 17:31  metropolitanandmicropolitanstatisticalareas_census_201111_gcs83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      5308 Jan  3 17:31  metropolitanandmicropolitanstatisticalareas_census_2020_wma84_attrs.csv
-rw-rw-r--  1 cakidd cakidd      3047 Jan  3 17:31  metropolitanstatisticalareas_uscensus_199901_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      3838 Jan  3 17:31  metropolitanstatisticalareas_uscensus_199901_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      1972 Jun  6 14:20  migration_20260606_142022.log
drwxrwxr-x  2 cakidd cakidd      4096 Apr 25 12:12  migrations
-rw-rw-r--  1 cakidd cakidd      7610 Jan  3 17:31  mineraloperations_usgs_200204_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      7586 Jan  3 17:31  mineraloperations_usgs_200204_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd   2399871 Jan  3 17:31  minesabandonedlandsline_wvdep_1996_noprojectoin_attrs.csv
-rw-rw-r--  1 cakidd cakidd     25145 Jan  3 17:31  minesabandonedlandspoint_wvdep_1996_noprojection_attrs.csv
-rw-rw-r--  1 cakidd cakidd    482548 Jan  3 17:31  minesabandonedlandspolygon_wvdep_1996_noprojection_attrs.csv
-rw-rw-r--  1 cakidd cakidd      4213 Jan 17 21:38  missing_collections.csv
-rw-rw-r--  1 cakidd cakidd      4752 Jan  7 13:23  missing_local_files.txt
-rw-rw-r--  1 cakidd cakidd      6375 Feb 22 18:01  missing_source_epochs.csv
-rw-r--r--  1 cakidd cakidd       464 May  4 11:43  Modelfile.egeria
drwxrwxr-x  3 cakidd cakidd      4096 May 23 16:07  models
-rw-rw-r--  1 cakidd cakidd       919 Feb  2 15:43  models.py
-rw-rw-r--  1 cakidd cakidd       513 Apr 30 14:12  mount_hope_data_template.json
drwxr-xr-x  5 cakidd cakidd      4096 Apr 26 12:16  ms-allis-auth-install
-rw-rw-r--  1 cakidd cakidd      6838 Apr 26 12:16  ms-allis-auth-install.tar.gz
drwxr-xr-x 12 cakidd cakidd      4096 Jun  7 19:36  ms-allis-frontend
-rw-rw-r--  1 cakidd cakidd         0 Mar 10 09:02  ms_jarvis_blood_brain_barrier
-rw-rw-r--  1 cakidd cakidd     12905 Apr 24 20:33  ms_jarvis_blood_brain_barrier.py
-rw-rw-r--  1 cakidd cakidd     11462 Mar 29 20:18  ms_jarvis_blood_brain_barrier.py.bak
-rw-rw-r--  1 cakidd cakidd       551 Jan 12 13:42  msjarvis_chroma_test.py
-rwxrwxr-x  1 cakidd cakidd      4065 Apr 24 19:10  msjarvisconsciousnessbridge.py.bak
-rw-rw-r--  1 cakidd cakidd     48538 May  3 00:31  ms_jarvis_contract_forge.py
-rw-rw-r--  1 cakidd cakidd      4423 May 31 22:20  msjarvis_embed_gbim.py
-rw-rw-r--  1 cakidd cakidd      1568 Feb 24 06:53  msjarvis_embed_gbim_resume_tail.py
-rwxrwxr-x  1 cakidd cakidd     14979 Mar 27 09:14  ms_jarvis_full_audit.sh
-rw-r--r--  1 cakidd cakidd      2890 May 11 11:53  ms_jarvis_psychology_services.py
-rw-rw-r--  1 cakidd cakidd      2955 Apr 30 14:12  ms_jarvis_rag_server.py
-rw-rw-r--  1 cakidd cakidd      2879 Apr 29 15:20  ms_jarvis_rag_server.py.bak.20260429-152039
-rw-rw-r--  1 cakidd cakidd      3464 Feb  6 22:42  msjarvisragserverwvpatch.py
drwxrwxr-x  6 cakidd cakidd      4096 Jun  1 11:41  msjarvis-rebuild
-rw-rw-r--  1 cakidd cakidd      1142 Feb  2 15:43  msjarvis_resources.py
-rw-rw-r--  1 cakidd cakidd       714 May 25 06:24  ms_jarvis_unified_gateway.py
-rw-rw-r--  1 cakidd cakidd     74450 May  1 01:56  ms_jarvis_unified_gateway.py.bak
-rw-rw-r--  1 cakidd cakidd       714 May 25 06:24  ms_jarvis_unified_gateway.py.bak.20260525_062445
-rw-r--r--  1 cakidd cakidd     30814 Jun  6 22:10  ms_jarvis_unified_gateway.py.working
-rw-rw-r--  1 cakidd cakidd      1112 Feb  7 18:01  msjarviswoahalgorithms.py
-rw-rw-r--  1 cakidd cakidd         0 May 18 23:58  naming
-rw-rw-r--  1 cakidd cakidd    377662 Jan  3 17:31  nationalatlasstreams_usgs_199903_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd    372396 Jan  3 17:31  nationalatlasstreams_usgs_199903_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd    102411 Jan  3 17:31  nationalregisterofhistoricplacespoints_natoinalpakrser_8d965955_attrs.csv
-rw-rw-r--  1 cakidd cakidd     60240 Jan  3 17:31  nationalregisterofhistoricplacespolygons_nationaparkse_b9d30a70_attrs.csv
-rw-rw-r--  1 cakidd cakidd     91542 Jan  3 17:31  nationalregister_point_20200923_attrs.csv
-rw-rw-r--  1 cakidd cakidd     96034 Jan  3 17:31  nationalregister_point_20200923_utm27_attrs.csv
-rw-rw-r--  1 cakidd cakidd       360 Jan  3 17:31  nationalwaterwaynetworkports_usarmycorpsofengineers_2001_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     27844 Jan  3 17:31  nationalwaterwaynetwork_usarmycorpsofengineers_2001_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     60271 Jan  3 17:31  nationaregisterofhistoricplacespolygons_nationalparkse_cab42150_attrs.csv
-rw-rw-r--  1 cakidd cakidd    102371 Jan  3 17:31  natoinalregisterofhistoricplacespoints_nationalparkser_ca43510e_attrs.csv
-rw-rw-r--  1 cakidd cakidd      2178 Jan  3 17:31  naviagablewaterways_usarmycropsofengineers_2006_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     70956 Jan  3 17:31  navigablewaterwaysrivermiles_usarmycropsofengineers_2006_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd   5228002 Jan  3 17:31  navigablewaterwaysstructures_usarmycorpsofengineers_2006_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd       397 Mar 10 08:22  nbb-prefrontal-full.json
-rw-rw-r--  1 cakidd cakidd         0 Jan 18 17:09  nbb_woah_algorithms_fix.patch
drwxrwxr-x 19 cakidd cakidd      4096 Apr 21 15:58  neurobiological_brain
drwxr-xr-x  3 cakidd cakidd      4096 Jan  7 08:40  neurobiologicalbrain
drwxrwxr-x  2 cakidd cakidd      4096 Apr 21 21:51  neurobiologicalbrainicontainersservice
drwxrwxr-x  2 cakidd cakidd      4096 Feb 16 13:28  neurobiologicalbrainmothercarrieprotocolsservice
-rw-r--r--  1 cakidd cakidd     20480 Jan 18 15:57  neuro-prefrontalcortex-patched.tar
-rwxrwxr-x  1 cakidd cakidd      3893 Mar 29 12:57  next_steps_local.sh
-rw-rw-r--  1 cakidd cakidd       301 Feb  4 00:37  nginx.conf
drwxrwxr-x 10 cakidd cakidd      4096 Jun  2 10:57  node_modules
-rw-------  1 cakidd cakidd       127 Feb 16 13:13  nohup.out
drwxrwxr-x  6 cakidd cakidd      4096 Apr 30 14:12  observability
-rw-rw-r--  1 cakidd cakidd     11029 Jan  3 17:31  officebuildings_wvdo_200807_utm83_attrs.csv
-rwxrwxr-x  1 cakidd cakidd      3376 Apr  3 21:28  oi36a-mitigation.sh
-rw-rw-r--  1 cakidd cakidd         0 Jan 11 22:50  old_drive_gis_candidates.txt
-rw-rw-r--  1 cakidd cakidd       408 Apr 30 14:12  OPEN_ITEMS.md
drwxrwxr-x  2 cakidd cakidd      4096 Apr 30 14:12  ops_history
drwxrwxr-x  4 cakidd cakidd      4096 May  8 23:21  output
-rw-rw-r--  1 cakidd cakidd       342 Jun  2 10:57  package.json
-rw-rw-r--  1 cakidd cakidd      4103 Jun  2 10:57  package-lock.json
-rw-rw-r--  1 cakidd cakidd      3061 Jan  3 17:31  paroleoffices_manysources_2008_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      2813 Jan  3 17:31  paroleoffices_manysources_2008_wgs84_attrs.csv
drwxrwxr-x  2 cakidd cakidd      4096 Jun  8 10:06  patches
-rw-rw-r--  1 cakidd cakidd      3798 Apr  3 08:34  patch_gate.py
-rw-rw-r--  1 cakidd cakidd      9403 Jun  1 13:49  patch_identity_layer.py
-rw-rw-r--  1 cakidd cakidd      5541 Apr 30 14:12  patch_judges.py
-rw-rw-r--  1 cakidd cakidd      7587 Jun  8 20:17  patch_learner_dedup_fanout.py
-rw-rw-r--  1 cakidd cakidd      5910 Jun  8 19:48  patch_learner_route_topics.py
-rwxrwxr-x  1 cakidd cakidd       491 Feb 16 22:29  patch_llm_health_endpoints.sh
-rwxrwxr-x  1 cakidd cakidd       593 Mar  9 20:57  patch_lm_synthesizer.sh
-rw-rw-r--  1 cakidd cakidd      4593 Jun  8 19:09 'patch_rag_store_collection(1).py'
-rw-rw-r--  1 cakidd cakidd      4593 Jun  8 19:07 'patch_rag_store_collection(2).py'
-rw-rw-r--  1 cakidd cakidd      4593 Jun  8 19:32  patch_rag_store_collection.py
-rw-rw-r--  1 cakidd cakidd       552 Jan 12 14:37  pdf_utils.py
drwxrwxr-x  6 cakidd cakidd      4096 May 15 18:42  persistent
lrwxrwxrwx  1 cakidd cakidd        50 Feb  4 16:27  persistent_chroma_old -> /home/ms-jarvis/msjarvis-rebuild/persistent/chroma
-rw-------  1 cakidd cakidd      4821 Jan 23 17:12  pg_hba.conf
-rw-rw-r--  1 cakidd cakidd      6918 Apr  7 22:28  pia-integration-check.log
-rw-rw-r--  1 cakidd cakidd      8716 May 15 22:51  pituitary_gland.py.bak
-rw-rw-r--  1 cakidd cakidd     10909 Jan  3 17:31  placesofworship_hsip_20080723_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     11029 Jan  3 17:31  placesofworship_hsip_20080723_wgs84_attrs.csv
-rw-rw-r--  1 cakidd cakidd     39924 Jan  3 17:31  policedept_wvdem_012319_gcs84_attrs.csv
-rw-rw-r--  1 cakidd cakidd     39224 Jan  3 17:31  policedept_wvdem_012319_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     52996 Jan  3 17:31  populatedplaces_census_201112_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     53215 Jan  3 17:31  populatedplaces_census_20112_gcs83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     57531 Jan  3 17:31  populatedplaces_census_2020_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     57594 Jan  3 17:31  populatedplaces_census_2020_wma84_attrs.csv
-rw-rw-r--  1 cakidd cakidd     36520 Jan  3 17:31  populatedplaces_uscensus_1990_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd    456656 Jan  3 17:31  populationdatablockgroups_uscensus_2000_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd    466702 Jan  3 17:31  populationdatablockgroups_uscensus_2000_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      3144 May  3 19:06  PORTING.md
-rwxrwxr-x  1 cakidd cakidd      3277 Jan 15 22:41  post-fix-automation.sh
-rw-rw-r--  1 cakidd cakidd      4077 Mar 10 10:21  post-patch-check.txt
-rw-rw-r--  1 cakidd cakidd    660837 Jan  3 17:31  pow_wvgistc_062919_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd    699923 Jan  3 17:31  pow_wvgistc_062919_wgs84_attrs.csv
-rwxrwxr-x  1 cakidd cakidd      4077 Apr 30 14:12  preflight_gate.sh
-rw-rw-r--  1 cakidd cakidd      1582 Mar 29 18:48  preflight_gate.sh.bak
-rwxrwxr-x  1 cakidd cakidd       442 Jan 12 07:47  probe_gdb_integration.sh
-rw-rw-r--  1 cakidd cakidd       741 Jan 12 08:50  processstatewidegisbulk_8819.log
-rw-rw-r--  1 cakidd cakidd       123 Jan 12 08:48  processstatewidegisbulk_.log
-rw-rw-r--  1 cakidd cakidd      1784 Jan 12 08:34  process_wv_layers.py
-rw-rw-r--  1 cakidd cakidd       832 Mar 21 18:06  prometheus.yml
drwxrwxr-x  2 cakidd cakidd      4096 Feb 24 15:15  proposals
-rw-rw-r--  1 cakidd cakidd      8235 Jan  3 17:31  publichealthdepts_hsip_20091229_utm83_attrs.csv
-rwxrwxr-x  1 cakidd cakidd       728 Jan 18 09:06  pull_jarvis_models.sh
drwxrwxr-x  2 cakidd cakidd      4096 Jun  4 12:55  __pycache__
drwxrwxr-x  3 cakidd cakidd      4096 Apr 25 12:11  .pytest_cache
-rw-rw-r--  1 cakidd cakidd        73 Apr 25 12:21  pytest.ini
drwxrwxr-x  2 cakidd cakidd      4096 Apr 30 14:12  qualia
-rw-rw-r--  1 cakidd cakidd      1053 Jan 12 15:09  query_msjarvis_corpus.py
-rw-rw-r--  1 cakidd cakidd       440 Jan 12 15:17  query_msjarvis_once.py
-rwxrwxr-x  1 cakidd cakidd       168 Jan 12 08:19  quick_gdb_probe.sh
-rw-rw-r--  1 cakidd cakidd       672 Jan 14 09:12  rag_insert_mountainshares.py
-rw-rw-r--  1 cakidd cakidd     11640 Feb  7 19:23  rag_integration_snapshot.tgz
-rw-rw-r--  1 cakidd cakidd      8001 Feb  2 17:06  rag_local_resources.py
-rw-rw-r--  1 cakidd cakidd       207 Jan 20 23:01  ragservermain.current.log
-rw-r--r--  1 cakidd cakidd     19564 Feb 24 12:00  rag_server_main.py
-rw-rw-r--  1 cakidd cakidd     12636 Feb  6 22:04  ragservermain.py
-rw-r--r--  1 cakidd cakidd     11788 Jan 11 20:14  rag_server_main.py.bak.1768180485
-rw-rw-r--  1 cakidd cakidd       107 Jan 20 23:00  ragsimple.current.log
-rw-rw-r--  1 cakidd cakidd   3544203 Jan  3 17:31  railnetworkregion_usdot_200203_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd   3496292 Jan  3 17:31  railnetworkregion_usdot_200203_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd    693208 Jan  3 17:31  railnetworkwv_usdot_200203_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd    683110 Jan  3 17:31  railnetworkwv_usdot_200203_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd    803922 Jan  3 17:31  railroads_rahalltransportationinstitute_2005_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      1693 Mar 30 19:46  randolph_matches.sql
-rw-rw-r--  1 cakidd cakidd         0 May 18 23:58  reading
-rw-r--r--  1 cakidd cakidd      4230 Apr 25 10:39  README-msallis-v1.md
-rw-rw-r--  1 cakidd cakidd     10794 Jan  3 17:31  realtimestreamflowstations_usgs_200012_ll27_attrs.csv
-rw-rw-r--  1 cakidd cakidd     10767 Jan  3 17:31  realtimestreamflowstations_usgs_200012_utm27_attrs.csv
-rw-rw-r--  1 cakidd cakidd     10759 Jan  3 17:31  realtimestreamflowstations_usgs_200012_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      2251 Jan 12 21:56  REBUILD_COMPLETE.md
-rw-rw-r--  1 cakidd cakidd      4393 May  5 18:54  rebuild_gis_chroma.py
-rwxrwxr-x  1 cakidd cakidd       220 Mar 25 11:58  redis-init.sh
drwxrwxr-x  3 cakidd cakidd      4096 Apr 30 14:12  redteam
-rw-rw-r--  1 cakidd cakidd     12307 Jan  3 17:31  regionalplanninganddevelopmentcouncil_wvdo_1971_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     16583 Jan  3 17:31  regionalplanninganddevelopmentcouncil_wvdo_1971_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      2160 Jan 12 14:43  reingest_msjarvis_chunks.py
-rwxrwxr-x  1 cakidd cakidd      1322 May  5 17:14  reload_and_ingest_gis.sh
-rwxrwxr-x  1 cakidd cakidd      1690 Jan 23 17:21  reload_geodb_bootstrap.sh
-rw-rw-r--  1 cakidd cakidd      2220 Mar 29 20:01  REMEDIATION_LOG_20260329.md
-rw-rw-r--  1 cakidd cakidd        16 May 24 18:49  requirements-69dgm.txt
-rw-rw-r--  1 cakidd cakidd       230 Jun  1 16:34  requirements-brain.txt
-rw-rw-r--  1 cakidd cakidd        88 May 17 11:05  requirements-gateway.txt
-rw-rw-r--  1 cakidd cakidd       490 Jun  3 19:25  requirements.txt
-rw-rw-r--  1 cakidd cakidd         0 May 18 23:58  resolve
-rw-rw-r--  1 cakidd cakidd         0 Feb 16 14:24  resolving
-rw-rw-r--  1 cakidd cakidd      1789 Feb  2 15:36  resource_assistant.py
-rw-rw-r--  1 cakidd cakidd      2281 Feb  2 15:50  resource_ranker.py
drwxrwxr-x  5 cakidd cakidd      4096 Feb 19 17:15  resources
-rwxrwxr-x  1 cakidd cakidd       350 Jan 21 18:32  RESTART_20LLM_FINAL.sh
-rwxrwxr-x  1 cakidd cakidd       724 Jan 18 14:43  restart_unified_msjarvis.sh
-rwxr-xr-x  1 cakidd cakidd     19818 Jan  7 13:13  restore_missing_files.sh
-rwxrwxr-x  1 cakidd cakidd       179 May 11 14:57  run_69dgm_orchestrator.sh
-rwxrwxr-x  1 cakidd cakidd       323 May 11 15:39  run_9000_69dgm_bridge.sh
-rwxrwxr-x  1 cakidd cakidd      1841 Jan 13 09:07  run_core_ops.sh
-rwxrwxr-x  1 cakidd cakidd       276 Jan 12 07:23  run_gbim_import.sh
-rwxrwxr-x  1 cakidd cakidd       617 Jan 12 07:20  run_gis_stack.sh
-rw-rw-r--  1 cakidd cakidd      2061 Mar 26 18:31  running_containers_20260326.txt
-rw-rw-r--  1 cakidd cakidd      2014 Mar 26 18:41  running_containers_93clean_20260326.txt
-rw-rw-r--  1 cakidd cakidd      2035 Mar 26 18:48  running_containers_GOLDEN_94_20260326.txt
-rwxrwxr-x  1 cakidd cakidd       253 Jan 12 07:21  run_sanctuary_import.sh
drwxrwxr-x  2 cakidd cakidd      4096 May 30 10:29  .scratch
drwxrwxr-x  4 cakidd cakidd      4096 Jun 11 15:42  scripts
drwxrwxr-x  2 cakidd cakidd      4096 Apr 30 14:20  .secrets
drwxrwxr-x  2 cakidd cakidd      4096 Jun  2 11:14  secrets
-rw-rw-r--  1 cakidd cakidd     16940 Feb 24 14:07  seed_full_knowledge.py
-rw-rw-r--  1 cakidd cakidd     10354 Feb 24 14:14  seed_gbim_catalog.py
-rw-rw-r--  1 cakidd cakidd      3267 Feb 24 13:58  seed_mountainshares.py
-rw-rw-r--  1 cakidd cakidd      5535 Jan  7 13:04  service_build_matrix.txt
-rw-rw-r--  1 cakidd cakidd       433 Jan 18 16:22  service_discovery_no_redis.py
-rw-r--r--  1 cakidd cakidd      9152 Mar 11 23:10  service_discovery.py
-rw-r--r--  1 cakidd cakidd      9152 Mar 10 17:10  service_discovery.py.bak
-rw-rw-r--  1 cakidd cakidd       166 Jan 18 16:20  service_registry_client_stub.py
drwxrwxrwx 57 cakidd cakidd    241664 Jun 11 18:07  services
-rw-rw-r--  1 cakidd cakidd      8933 Apr 19 15:08  session_2026-04-19.log
-rw-rw-r--  1 cakidd cakidd    173488 Jan  3 17:31  sewertreatmentplants_wvdep_200203_utm83_attrs.csv
drwxrwxr-x  3 cakidd cakidd      4096 Jun  7 11:26  shared
-rw-rw-r--  1 cakidd cakidd     10420 Jan  3 17:31  solidwastefacilities_wvdep_200202_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     10452 Jan  3 17:31  solidwastefacilities_wvdep_200202_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd        10 Feb 22 13:50  sourcetable
-rw-rw-r--  1 cakidd cakidd     18265 Feb 15 23:16  spiritual_nbb_backup_20260215_231630.tar.gz
-rw-rw-r--  1 cakidd cakidd      4662 Feb 15 23:20  spiritual_nbb_fix2_20260215_232031.tar.gz
-rw-rw-r--  1 cakidd cakidd     18767 Feb 15 23:27  spiritual_rag_deployment_20260215_232717.tar.gz
-rw-r--r--  1 cakidd cakidd      8707 Mar 31 19:59  spiritual_rag_domain.py.tmp
-rw-rw-r--  1 cakidd cakidd     30264 Jan  3 17:31  springs_wvges_1986_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     29901 Jan  3 17:31  springs_wvges_1986_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd       199 Mar 21 20:05  sprint3_full_20260321_200529.log
-rw-rw-r--  1 cakidd cakidd       314 Apr 30 14:12  sprint_backlog.md
-rw-rw-r--  1 cakidd cakidd       647 Jan 21 16:22  STABLE_MODE_NOTE.txt
-rwxrwxr-x  1 cakidd cakidd       321 Jan 21 17:54  START20LLMFINAL.sh
-rwxrwxr-x  1 cakidd cakidd       321 Jan 21 18:05  START20LLMFINAL.sh.backup.20260121180532
-rwxrwxr-x  1 cakidd cakidd       341 Jan 21 21:17  START20LLMPRODUCTION.sh
-rwxrwxr-x  1 cakidd cakidd       340 May 29 10:26  start_auth_router.sh
-rwxrwxr-x  1 cakidd cakidd       346 Jan 30 10:34  START_GIS_RAG.sh
-rwxrwxr-x  1 cakidd cakidd       427 Mar 26 18:52  start-jarvis.sh
-rwxrwxr-x  1 cakidd cakidd       427 Mar 26 18:53  start-jarvis.sh.bak_20260326
-rwxrwxr-x  1 cakidd cakidd       412 May  8 21:16  start_rag_router.sh
-rw-rw-r--  1 cakidd cakidd      2754 Apr 30 14:12  STARTUP.md
-rw-rw-r--  1 cakidd cakidd     15021 Jan  3 17:31  stateofwvhousedistricts_wvlegislativeservices_2010_attrs.csv
-rw-rw-r--  1 cakidd cakidd      3791 Jan  3 17:31  stateofwvsenatedistricts_wvlegislativeservices_2010_attrs.csv
-rw-rw-r--  1 cakidd cakidd     22015 Jan  3 17:31  states_region_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     10564 Mar 15 17:12  STATUS_MARCH15_2026_FINAL.md
-rw-rw-r--  1 cakidd cakidd   4398800 Jan  3 17:31  structurepolygons_samb_2003_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd    120913 Jan  3 17:31  summits_gistc_052012_utm83_shp_attrs.csv
-rw-rw-r--  1 cakidd cakidd    125235 Jan  3 17:31  summits_gistc_052012_wgs84_shp_attrs.csv
-rw-rw-r--  1 cakidd cakidd   1098946 Jan  3 17:31  surveycontrol_nationalgeodeticsurvey_102011_gcs83_attrs.csv
-rw-r--r--  1 cakidd cakidd     10589 May  2 18:07  swarm_intelligence.py
-rw-rw-r--  1 cakidd cakidd      4126 Mar 20 05:13  sync_chroma_metadata.py
-rw-rw-r--  1 cakidd cakidd      2821 Feb  2 13:11  sync_gbim_to_chroma.py
-rw-rw-r--  1 cakidd cakidd      1117 Apr 30 14:12  system_state_20260417.json
-rw-rw-r--  1 cakidd cakidd       392 Jan 16 19:23  test_autonomous_learner_store.py
-rwxrwxr-x  1 cakidd cakidd       659 Mar 29 18:55  test_bbb_output.sh
-rwxrwxr-x  1 cakidd cakidd       262 Feb 16 22:42  test_chatsync_gateway.sh
-rwxrwxr-x  1 cakidd cakidd       262 Feb 16 22:42  test_chatsync.sh
-rwxrwxr-x  1 cakidd cakidd      1423 Feb  7 17:20  test_end_to_end_woah_fifthdgm.py
-rwxrwxr-x  1 cakidd cakidd      1013 Mar 29 18:42  test_gateway_rbac.sh
-rwxrwxr-x  1 cakidd cakidd      1903 Jan 16 08:23  test_immediate.sh
-rwxrwxr-x  1 cakidd cakidd       115 Mar 12 13:42  test_jarvis_consciousness_bridge.sh
-rwxrwxr-x  1 cakidd cakidd      1009 Mar 12 13:36  test_jarvis_i_containers.sh
-rwxrwxr-x  1 cakidd cakidd       506 Jan 19 00:14  test_msjarvis.golden.sh
-rwxrwxr-x  1 cakidd cakidd       506 Jan 18 23:52  test_msjarvis.sh
-rwxrwxr-x  1 cakidd cakidd       506 Jan 19 00:02  test_msjarvis.working.20260119-000202.sh
-rw-rw-r--  1 cakidd cakidd       665 Feb  2 10:27  test_provenance_one.sql
-rw-rw-r--  1 cakidd cakidd       310 Mar 31 15:32  test_query.sh
-rwxrwxr-x  1 cakidd cakidd       661 Mar 29 13:44  test_rag_embedding_roundtrip.sh
-rw-rw-r--  1 cakidd cakidd       547 Feb  2 15:32  test_rag_image.py
-rwxrwxr-x  1 cakidd cakidd       379 Jun  3 12:55  test_rag_search.sh
-rw-rw-r--  1 cakidd cakidd       721 Feb  2 15:32  test_rag_text.py
drwxrwxr-x  2 cakidd cakidd      4096 May 16 17:21  tests
-rwxrwxr-x  1 cakidd cakidd       295 Jan 19 12:06  test-unified-gateway.sh
-rwxrwxr-x  1 cakidd cakidd       715 Mar 29 18:58  test_woah_optimizer.sh
drwxrwxr-x 12 cakidd cakidd      4096 May 16 21:51  tiger_downloads
-rwxrwxr-x  1 cakidd cakidd         5 Sep 26  2022  tl_2022_us_county.cpg
-rwxrwxr-x  1 cakidd cakidd    948433 Sep 26  2022  tl_2022_us_county.dbf
-rwxrwxr-x  1 cakidd cakidd       165 Sep 26  2022  tl_2022_us_county.prj
-rwxrwxr-x  1 cakidd cakidd 131238740 Sep 26  2022  tl_2022_us_county.shp
-rwxrwxr-x  1 cakidd cakidd     40489 Sep 29  2022  tl_2022_us_county.shp.ea.iso.xml
-rwxrwxr-x  1 cakidd cakidd     52545 Sep 29  2022  tl_2022_us_county.shp.iso.xml
-rwxrwxr-x  1 cakidd cakidd     25980 Sep 26  2022  tl_2022_us_county.shx
-rw-rw-r--  1 cakidd cakidd  83324165 Oct 31  2022  tl_2022_us_county.zip
drwxrwxr-x  2 cakidd cakidd      4096 Apr  7 17:21  tmp-aaacpe-patch
-rw-rw-r--  1 cakidd cakidd      5169 Feb  3 14:10  tmp_rag_slice.py
-rw-rw-r--  1 cakidd cakidd       482 Jan 12 16:53  TODO_enable_real_entanglement.md
drwxrwxr-x  4 cakidd cakidd      4096 Apr  7 20:59  tools
-rw-rw-r--  1 cakidd cakidd      7722 Jan  3 17:31  towersam_fcc_200202_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     67528 Jan  3 17:31  towersasr_fcc_200202_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     99648 Jan  3 17:31  towersasr_fcc_200202_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     21108 Jan  3 17:31  towerscellular_fcc_200202_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     30636 Jan  3 17:31  towerscellular_fcc_200202_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      8810 Jan  3 17:31  towersfm_fcc_200202_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd    189242 Jan  3 17:31  towersmicrowave_fcc_200202_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd    272567 Jan  3 17:31  towersmicrowave_fcc_200202_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     23150 Jan  3 17:31  towerspager_fcc_200202_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     33938 Jan  3 17:31  towerspager_fcc_200202_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      1914 Jan  3 17:31  towers_wvpublicbroadcasting_2002_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      1894 Jan  3 17:31  towers_wvpublicbroadcasting_2002_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd         0 May 18 23:58  transferring
drwxrwxr-x  2 cakidd cakidd      4096 Jun  6 22:45  ui
-rw-rw-r--  1 cakidd cakidd      6007 Jan 22 15:08  ultimate8050.log
-rw-------  1 cakidd cakidd       494 Apr 25 11:13  users.json
drwxrwxr-x  6 cakidd cakidd      4096 Apr 30 14:12  .venv
drwxrwxr-x  6 cakidd cakidd      4096 Jan 23 16:41  .venv-chroma
-rwxrwxr-x  1 cakidd cakidd     19471 May  8 10:52  VERIFYANDTEST.sh
-rwxrwxr-x  1 cakidd cakidd     19945 Apr 11 13:20  VERIFYANDTEST.sh.bak.20260411_132002
-rw-rw-r--  1 cakidd cakidd      2652 Jan  3 17:31  veteransaffairsfacilities_manysources_200503_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      2150 Jan  3 17:31  veteransaffairsfacilities_manysources_200503_wgs84_attrs.csv
-rw-rw-r--  1 cakidd cakidd    561014 Jan  3 17:31  votingdistrictswv_legislativeservices_2002_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd    397861 Jan  3 17:31  votingdistrictswv_uscensus_2000_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     18272 Jan  3 17:31  weatherstations_nationalclimatedatacenter_1999_gcs83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     24026 Jan  3 17:31  weatherstations_nationalclimatedatacenter_1999_utm27_attrs.csv
drwxrwxr-x  2 cakidd cakidd      4096 Feb 14 16:13  wheels
-rw-rw-r--  1 cakidd cakidd         0 May 11 11:09  when
-rw-rw-r--  1 cakidd cakidd  32508070 Jan  3 17:31  windenergyresource_nationalrenewableenergylab_200901_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd  33036666 Jan  3 17:31  windenergyresource_nationalrenewableenergylab_200901_wgs84_attrs.csv
-rw-rw-r--  1 cakidd cakidd        87 Feb  7 21:23  woah_health.json
-rw-rw-r--  1 cakidd cakidd        22 Feb  7 21:23  woah_metrics_example.json
-rw-rw-r--  1 cakidd cakidd      1655 Feb  7 21:21  woah_openapi.json
-rw-rw-r--  1 cakidd cakidd       319 Feb  7 21:23  woah_process_example.json
-rw-rw-r--  1 cakidd cakidd       711 Mar 25 12:04  woah_stub.py
drwxrwxr-x  5 cakidd cakidd      4096 Jan  9 20:50  .woah-venv
-rw-rw-r--  1 cakidd cakidd         0 May 18 23:58  writing
-rw-rw-r--  1 cakidd cakidd     16177 Jan  3 17:31  wv_county_boundaries_24k_topo_updated_2022_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd       744 Feb  6 22:25  wv_entangled_context_model.py
-rw-rw-r--  1 cakidd cakidd      2879 Feb  6 22:26  wv_entangled_context.schema.json
drwxrwxr-x  3 cakidd cakidd      4096 Feb  7 20:46  wv_gis_layers
-rw-rw-r--  1 cakidd cakidd    260368 Jan 12 08:34  wv_gis_layers_catalog.csv
-rw-rw-r--  1 cakidd cakidd    265495 Jan 12 08:39  wv_gis_layers_process_status.csv
-rw-rw-r--  1 cakidd cakidd     10249 Jan 11 22:46  wv_like_csv_candidates.txt
-rw-rw-r--  1 cakidd cakidd 289629049 Jan  3 17:31  wv_microsoft_20180207_utm17n83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      3000 Jan 11 22:48  wv_name_matches_current_pv.txt
-rw-rw-r--  1 cakidd cakidd       332 Jan  3 17:32  wvstatebounadary100k_usgs_200203_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd       252 Jan  3 17:32  wvstateboundary100k_usgs_200203_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd       330 Jan  3 17:32  wvstateboundary24k_usgs_200203_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     11956 Jan  3 17:32  wvstatehousedistricts_manysources_1992_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     16248 Jan  3 17:32  wvstatehousedistricts_manysources_1992_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     13692 Jan  3 17:32  wvstatehousedistricts_manysources_2002_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd     16856 Jan  3 17:32  wvstatehousedistricts_manysources_2002_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      3453 Jan  3 17:32  wvstatesenatedistricts_manysources_1992_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      4687 Jan  3 17:32  wvstatesenatedistricts_manysources_1992_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      3912 Jan  3 17:32  wvstatesenatedistricts_manysources_2002_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd      5144 Jan  3 17:32  wvstatesenatedistricts_wvlegislativeservices_2020_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd    164313 Jan  3 17:31  wv_tax_districts_ll83_attrs.csv
-rw-rw-r--  1 cakidd cakidd    164039 Jan  3 17:31  wv_tax_districts_wma84_attrs.csv
-rw-rw-r--  1 cakidd cakidd    215404 Jan  3 17:32  zipcodetabulationarea_census_2020_utm83_attrs.csv
-rw-rw-r--  1 cakidd cakidd    215071 Jan  3 17:32  zipcodetabulationarea_census_2020_wma84_attrs.csv
PID: 1893889
lrwxrwxrwx 1 cakidd cakidd 0 Jun 11 18:11 /proc/1893889/exe -> /usr/bin/python3.12
/opt/msjarvis-rebuild/.venv/bin/python3 services/ms_jarvis_production_chat.py lrwxrwxrwx 1 cakidd cakidd 0 Jun 11 18:15 /proc/1893889/cwd -> /opt/msjarvis-rebuild
1,10c1
< """
< ms_jarvis_production_chat.py — PATCHED 2026-06-07
< Fixes:
<   1. generate_response() now returns (text, expert_responses, minds_participated)
<   2. _compute_divergence() added — Jaccard 5-gram pairwise distance
<   3. /chat response includes pipeline.divergence_score + pipeline.divergence_flag
< """
< import asyncio
< import httpx
< import logging
---
> #!/usr/bin/env python3
12,14c3,5
< import re
< import time
< from typing import Any, Dict, List, Optional, Tuple
---
> import logging
> from datetime import datetime
> from typing import Optional, Dict, Any
16,18d6
< from fastapi import FastAPI, HTTPException
< from fastapi.middleware.cors import CORSMiddleware
< from pydantic import BaseModel
20,21c8
< logger = logging.getLogger("ms_jarvis_production_chat")
< logging.basicConfig(level=logging.INFO)
---
> import httpx
22a10,65
> async def call_truth_filter(text: str) -> dict:
>     """Call BBB truth filter on 8016 and return a slim verdict."""
>     try:
>         async with httpx.AsyncClient(timeout=10.0) as client:
>             resp = await client.post(
>                 "http://jarvis-blood-brain-barrier:8016/filter",
>                 json={"content": text},
>             )
>         if resp.status_code != 200:
>             return {
>                 "valid": False,
>                 "confidence": 0.5,
>                 "principal_reasons": [f"BBB unavailable (status {resp.status_code})"],
>             }
> 
>         bbb = resp.json()
>         approved = bbb.get("content_approved", False)
>         pass_rate = bbb.get("barrier_stats", {}).get("pass_rate", 0.9)
>         filters = bbb.get("filters", {}) or {}
> 
>         reasons = []
> 
>         eth = filters.get("ethical") or {}
>         if eth.get("ethical_status") != "approved":
>             reasons.append(f"Ethics: {eth.get('reason', 'issues detected')}")
> 
>         thr = filters.get("threat_detection") or {}
>         if not thr.get("community_safe", True):
>             r = thr.get("reasons") or []
>             if r:
>                 reasons.append(f"Threat: {', '.join(r)}")
>             else:
>                 reasons.append("Threat: community not safe")
> 
>         saf = filters.get("safety") or {}
>         if not saf.get("safe", True):
>             reasons.append(f"Safety: {saf.get('reason', 'unsafe')}")
> 
>         spr = filters.get("spiritual") or {}
>         if not spr.get("biblically_sound", True):
>             reasons.append(f"Spiritual: {spr.get('reason', 'not sound')}")
> 
>         if not reasons and approved:
>             reasons.append("All BBB filters passed.")
> 
>         return {
>             "valid": approved,
>             "confidence": pass_rate,
>             "principal_reasons": reasons,
>         }
>     except Exception as e:
>         return {
>             "valid": False,
>             "confidence": 0.5,
>             "principal_reasons": [f"Truth verdict error: {e}"],
>         }
24,27d66
< def _is_local_resource_query(message: str) -> bool:
<     if not message:
<         return False
<     text = message.lower()
29,62c68,70
<     geo_tokens = [
<         "county", "wv", "west virginia", "fayette", "fayetteville", "oak hill",
<         "beckley", "charleston", "appalachia", "appalachian", "mountainshares",
<     ]
<     service_tokens = [
<         "senior services", "senior center", "aging services", "area agency on aging",
<         "meals on wheels", "transportation", "home health", "caregiver",
<         "shelter", "food pantry", "clinic", "community resources", "local services",
<         "assistance", "nonprofit", "benefits", "housing assistance",
<     ]
< 
<     return any(g in text for g in geo_tokens) and any(t in text for t in service_tokens)
< 
< 
< def _downgrade_local_resource_answer(message: str) -> str:
<     return (
<         "[Safety note: for local services and programs in your area, this system does not "
<         "have authoritative, up-to-date listings for specific providers, addresses, phone "
<         "numbers, or hours. The guidance below is intentionally generic and should be "
<         "verified with official county or state sources before acting.]\n\n"
<         "For a question like this, the safest next steps are:\n\n"
<         "1. Contact the county government office and ask which department handles senior or aging services.\n"
<         "2. Check official West Virginia state aging or health-and-human-services directories for Fayette County listings.\n"
<         "3. Ask for these categories of help specifically: senior centers, home-delivered meals, transportation, caregiver support, in-home assistance, benefits counseling, and housing support.\n"
<         "4. Verify the legal name of the organization, service area, hours, eligibility, cost, and whether it appears on an official county or state resource list.\n\n"
<         "Common categories that may exist in a county like Fayette include:\n"
<         "- Area Agency on Aging or aging-resource office.\n"
<         "- Senior/community centers.\n"
<         "- Home-delivered meal or congregate meal programs.\n"
<         "- Transportation for appointments and errands.\n"
<         "- In-home support, respite, or caregiver assistance.\n"
<         "- Benefits navigation, case management, and housing referrals.\n\n"
<         "I am avoiding specific organization names or contact details here because high model disagreement and missing grounded retrieval make those details unsafe to present without verification."
<     )
---
> import httpx
> from fastapi import FastAPI, HTTPException
> from pydantic import BaseModel
63a72
> logger = logging.getLogger(__name__)
65,81c74,78
< app = FastAPI(title="Ms. Jarvis Production Chat", version="2.1.0-patched")
< app.add_middleware(
<     CORSMiddleware,
<     allow_origins=["*"],
<     allow_credentials=True,
<     allow_methods=["*"],
<     allow_headers=["*"],
< )
< 
< # ── Config ────────────────────────────────────────────────────────────────────
< CONSENSUS_URL  = os.getenv("CONSENSUS_URL",  "http://jarvis-20llm-production:8008")
< MEMORY_URL     = os.getenv("MEMORY_URL",     "http://jarvis-memory:8010")
< BBB_URL        = os.getenv("BBB_URL",        "http://jarvis-bbb:8012")
< RAG_URL        = os.getenv("RAG_URL",        "http://jarvis-rag:8011")
< RAG_API_KEY    = os.getenv("RAG_API_KEY",    "")
< HILBERT_URL    = os.getenv("HILBERT_URL",    "http://127.0.0.1:8081")
< DIVERGENCE_THRESHOLD = float(os.getenv("DIVERGENCE_THRESHOLD", "0.72"))
---
> """
> Ms. Egeria Jarvis - Production Chat Pipeline (stabilized minimal version)
> """
> 
> app = FastAPI(title="Ms. Jarvis Production Chat", version="1.0.0")
83,84c80,87
< HTTP_TIMEOUT = httpx.Timeout(None, connect=2.0, read=3.0, pool=2.0)
< CONSENSUS_TIMEOUT = httpx.Timeout(None, connect=5.0, read=None, write=None, pool=5.0)
---
> # Service URLs (host or container DNS; adjust later as you bring services online)
> UEID_URL = "http://jarvis-ueid-service:4030"              # currently stubbed in code
> RAG_URL = "http://127.0.0.1:8003"                 # RAG server (POST /search, /store_conversation)
> CONSENSUS_URL = "http://127.0.0.1:18018"      # consensus / LLM gateway (not yet wired)
> BBB_URL = "http://127.0.0.1:8016"                         # BBB proxy on host
> TRUTH_FILTER_URL = "http://jarvis-truth-filter:8054"      # truth filter (likely offline)
> TEMPORAL_URL = "http://jarvis-temporal-consciousness:7007"
> MOTHER_CARRIE_URL = "http://jarvis-mother-protocols:4000"
87d89
< # ── Pydantic models ───────────────────────────────────────────────────────────
90,101c92
<     user_id: str = "anonymous"
<     session_id: Optional[str] = None
<     context: Optional[List[Dict[str, Any]]] = None
<     use_rag: bool = True
< 
< 
< class PipelineInfo(BaseModel):
<     minds_participated: int = 0
<     divergence_score: float = 0.0
<     divergence_flag: bool = False
<     rag_used: bool = False
<     latency_ms: int = 0
---
>     user_id: str = "default_user"
106,109c97,169
<     user_id: str
<     session_id: Optional[str] = None
<     expert_responses: List[Dict[str, Any]] = []
<     pipeline: PipelineInfo = PipelineInfo()
---
>     source: str
>     verified: bool
>     processing_layers: Dict[str, Any]
> 
> 
> @app.get("/health")
> async def health():
>     return {"status": "healthy", "service": "production_chat_pipeline", "port": 8018}
> 
> 
> @app.get("/")
> async def root():
>     return {
>         "service": "Ms. Egeria Jarvis Production Chat",
>         "version": "1.0.0",
>         "creator": "Carrie Ann 'Mamma' Kidd",
>         "location": "Mount Hope, West Virginia",
>         "pipeline": [
>             "1. Check RAG for existing knowledge (simplified)",
>             "2. Prepare minimal context",
>             "3. Generate response (currently safe greeting fallback)",
>             "4. Filter through Blood-Brain Barrier",
>             "5. Verify with Truth Filter",
>             "6. Return safe, verified response",
>         ],
>     }
> 
> 
> async def check_chromadb_rag(message: str) -> Optional[str]:
>     """Step 1: Check RAG for existing knowledge (simplified schema)."""
>     try:
>         async with httpx.AsyncClient(timeout=10.0) as client:
>             resp = await client.post(
>                 f"{RAG_URL}/search",
>                 json={"query": message, "top_k": 5},
>             )
>         if resp.status_code != 200:
>             return None
>         data = resp.json()
>         results = data.get("results") or []
>         if isinstance(results, list) and results:
>             first = results[0]
>             if isinstance(first, dict):
>                 return first.get("content") or first.get("text") or str(first)
>             return str(first)
>         # ignore results_by_source for now; can be added later
>     except Exception as e:
>         logger.warning(f"RAG search failed: {e}")
>     return None
> 
> 
> async def store_conversation(user_id: str, query: str, response_text: str) -> bool:
>     """Store conversation in RAG with known-good schema."""
>     try:
>         async with httpx.AsyncClient(timeout=10.0) as client:
>             result = await client.post(
>                 f"{RAG_URL}/store_conversation",
>                 json={
>                     "user_message": query,
>                     "assistant_response": response_text,
>                     "user_id": user_id,
>                     "metadata": {
>                         "source": "production_chat",
>                         "type": "conversation",
>                         "location": "Mount Hope, WV",
>                         "timestamp": datetime.now().isoformat(),
>                     },
>                 },
>             )
>             return result.status_code == 200
>     except Exception as e:
>         logger.warning(f"Store conversation failed: {e}")
>         return False
112,116c172,194
< # ── Divergence scorer ─────────────────────────────────────────────────────────
< def _ngrams(text: str, n: int = 5) -> frozenset:
<     """Character n-grams of a normalised string."""
<     t = re.sub(r"\s+", " ", text.lower().strip())
<     return frozenset(t[i : i + n] for i in range(max(0, len(t) - n + 1)))
---
> async def get_recent_conversations(user_id: str, limit: int = 3) -> str:
>     """Get recent conversation history for context (best-effort)."""
>     try:
>         async with httpx.AsyncClient(timeout=10.0) as client:
>             resp = await client.get(
>                 f"{RAG_URL}/conversations/{user_id}",
>                 params={"limit": limit},
>             )
>         if resp.status_code != 200:
>             return ""
>         data = resp.json()
>         conversations = data.get("conversations", [])
>         if not conversations:
>             return ""
>         context = "Previous conversation context:\n"
>         for conv_list in conversations:
>             if isinstance(conv_list, list):
>                 for conv_text in conv_list:
>                     context += str(conv_text).replace("\n", " ") + "\n"
>         return context
>     except Exception as e:
>         logger.warning(f"Get conversations failed: {e}")
>         return ""
119c197
< def _compute_divergence(expert_responses: List[Dict[str, Any]]) -> float:
---
> async def generate_response(message: str, context: str = "") -> str:
121,123c199,200
<     Pairwise Jaccard distance averaged over all response pairs.
<     Returns 0.0 (all identical) → 1.0 (completely disjoint).
<     Falls back to 0.0 on any error.
---
>     Step 3: Generate response via unified gateway /chat at CONSENSUS_URL.
>     Falls back to safe greeting if the gateway returns empty or errors.
126,142c203,226
<         texts = [r.get("response", "") for r in expert_responses if r.get("response")]
<         if len(texts) < 2:
<             return 0.0
<         grams = [_ngrams(t) for t in texts]
<         distances: List[float] = []
<         for i in range(len(grams)):
<             for j in range(i + 1, len(grams)):
<                 union = grams[i] | grams[j]
<                 if not union:
<                     distances.append(0.0)
<                     continue
<                 inter = grams[i] & grams[j]
<                 distances.append(1.0 - len(inter) / len(union))
<         return round(sum(distances) / len(distances), 4) if distances else 0.0
<     except Exception as exc:  # noqa: BLE001
<         logger.warning("Divergence calculation failed: %s", exc)
<         return 0.0
---
>         async with httpx.AsyncClient(timeout=60.0) as client:
>             payload = {
>                 "message": message,
>                 "context": context,
>                 "user_id": "production_pipeline",
>             }
>             resp = await client.post(f"{CONSENSUS_URL}/chat", json=payload)
>         if resp.status_code == 200:
>             data = resp.json()
>             # Unified gateway schema: {"status": "...", "response": "...", "pipeline": {...}}
>             if isinstance(data, dict):
>                 text = data.get("response") or ""
>                 if text.strip():
>                     return str(text)
>                 # Fallback to any other plausible field if present
>                 for key in ("answer", "consensus", "text"):
>                     if key in data and data[key]:
>                         return str(data[key])
>             if isinstance(data, str) and data.strip():
>                 return data
>             # If we reach here, gateway returned empty/diagnostic only.
>     except Exception as e:
>         logger.warning(f"Consensus generation failed: {e}")
>     return "Hello! I'm Ms. Egeria Jarvis, serving Mount Hope, West Virginia."
145,146c229,230
< # ── BBB filter ────────────────────────────────────────────────────────────────
< async def _apply_bbb_filter(message: str) -> str:
---
> async def filter_through_bbb(response_text: str) -> Dict[str, Any]:
>     """Step 4: Filter through Blood-Brain Barrier for ethics."""
148,154c232,238
<         async with httpx.AsyncClient(timeout=httpx.Timeout(10.0)) as client:
<             r = await client.post(f"{BBB_URL}/filter", json={"text": message})
<             if r.status_code == 200:
<                 return r.json().get("filtered", message)
<     except Exception:
<         pass
<     return message
---
>         async with httpx.AsyncClient(timeout=5.0) as client:
>             resp = await client.get(f"{BBB_URL}/health")
>         if resp.status_code == 200:
>             return {"filtered": True, "safe": True, "status": "active"}
>     except Exception as e:
>         logger.warning(f"BBB filter check failed: {e}")
>     return {"filtered": False, "safe": True, "status": "bypassed"}
157,158c241,242
< # ── RAG context ───────────────────────────────────────────────────────────────
< async def _fetch_rag_context(message: str, user_id: str) -> str:
---
> async def verify_truth(response_text: str) -> bool:
>     """Step 5: Verify response through Truth Filter (best-effort; stub if offline)."""
160,168c244,247
<         async with httpx.AsyncClient(timeout=httpx.Timeout(15.0)) as client:
<             headers = {}
<             if RAG_API_KEY:
<                 headers["X-API-Key"] = RAG_API_KEY
<                 headers["Authorization"] = f"Bearer {RAG_API_KEY}"
<             r = await client.post(
<                 f"{RAG_URL}/search",
<                 json={"query": message, "user_id": user_id, "top_k": 5},
<                 headers=headers,
---
>         async with httpx.AsyncClient(timeout=5.0) as client:
>             resp = await client.post(
>                 f"{TRUTH_FILTER_URL}/verify",
>                 json={"content": response_text},
170,208c249,258
<             if r.status_code == 200:
<                 data = r.json()
<                 results = data.get("results") or []
<                 parts = []
< 
<                 for item in results:
<                     if isinstance(item, dict):
<                         text = (
<                             item.get("snippet")
<                             or item.get("text")
<                             or item.get("content")
<                             or ""
<                         )
<                         if isinstance(text, str) and text.strip():
<                             parts.append(text.strip())
<                     elif isinstance(item, str) and item.strip():
<                         parts.append(item.strip())
< 
<                 if parts:
<                     deduped = []
<                     seen = set()
<                     for part in parts:
<                         norm = part.strip()
<                         if norm and norm not in seen:
<                             seen.add(norm)
<                             deduped.append(norm)
<                     return "\n\n".join(deduped)
<     except Exception:
<         pass
<     return ""
< 
< 
< # ── Core generation — calls 8008 ensemble ─────────────────────────────────────
< async def generate_response(
<     message: str,
<     user_id: str,
<     context: Optional[List[Dict[str, Any]]] = None,
<     rag_context: str = "",
< ) -> Tuple[str, List[Dict[str, Any]], int]:
---
>         if resp.status_code == 200:
>             data = resp.json()
>             val = data.get("verified", True)
>             return bool(val) if val is not None else True
>     except Exception as e:
>         logger.warning(f"Truth verification failed: {e}")
>     return True
> 
> 
> async def add_consciousness_layers(message: str, user_id: str) -> Dict[str, Any]:
210,211c260,261
<     Returns (response_text, expert_responses, minds_participated).
<     Never raises — returns a graceful error string on failure.
---
>     Add temporal and maternal context.
>     CURRENTLY: stubbed as active; replace with real /health checks later.
213,216c263,265
<     payload: Dict[str, Any] = {
<         "message": message,
<         "user_id": user_id,
<         "context": context or [],
---
>     return {
>         "temporal": {"status": "active"},
>         "maternal": {"status": "active"},
218,219d266
<     if rag_context:
<         payload["rag_context"] = rag_context
221,237d267
<     try:
<         async with httpx.AsyncClient(timeout=CONSENSUS_TIMEOUT) as client:
<             r = await client.post(f"{CONSENSUS_URL}/chat", json=payload)
<             r.raise_for_status()
<             data = r.json()
< 
<         response_text       = data.get("response", "")
<         expert_responses    = data.get("expert_responses", [])
<         minds_participated  = int(data.get("minds_participated", len(expert_responses)))
<         return response_text, expert_responses, minds_participated
< 
<     except httpx.HTTPStatusError as exc:
<         logger.error("Ensemble HTTP error %s: %s", exc.response.status_code, exc)
<         return f"[Error {exc.response.status_code} from ensemble]", [], 0
<     except Exception as exc:
<         logger.exception("Ensemble call failed")
<         return "[Ensemble unavailable — please retry]", [], 0
238a269,275
> # In-memory session storage for active conversations
> active_conversations: Dict[str, str] = {}  # {user_id: conversation_id}
> 
> 
> async def get_or_create_ueid(user_id: str) -> str:
>     """Temporary stub UEID until real service is up."""
>     return f"UEID_STUB_{user_id}"
240,243c277,294
< # ── /health ───────────────────────────────────────────────────────────────────
< @app.get("/health")
< async def health():
<     return {"status": "ok", "service": "ms_jarvis_production_chat", "version": "2.1.0-patched"}
---
> 
> async def get_or_create_conversation(ueid: str, user_id: str) -> str:
>     """Get active conversation or create new one (local only)."""
>     if user_id in active_conversations:
>         return active_conversations[user_id]
> 
>     import uuid
> 
>     conv_id = f"CONV_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}"
>     active_conversations[user_id] = conv_id
>     return conv_id
> 
> 
> async def log_message_to_ueid(
>     conversation_id: str, ueid: str, message: str, response_text: str
> ) -> None:
>     """UEID logging stub (no-op until UEID service exists)."""
>     return None
246d296
< # ── /chat ─────────────────────────────────────────────────────────────────────
248,249c298,316
< async def chat(req: ChatRequest):
<     t0 = time.monotonic()
---
> async def chat(request: ChatRequest):
>     truth = await call_truth_filter(request.message)
> 
>     """Complete production chat pipeline (stabilized)."""
>     processing_layers: Dict[str, Any] = {}
> 
>     # Step 0: UEID + conversation (stubbed UEID)
>     ueid = await get_or_create_ueid(request.user_id)
>     conversation_id = await get_or_create_conversation(ueid, request.user_id)
>     processing_layers["ueid"] = ueid
>     processing_layers["conversation_id"] = conversation_id
> 
>     # Step 1: RAG knowledge check
>     # Step 1: RAG knowledge check (temporarily disabled while RAG collections are tuned)
>     existing_knowledge = None
>     processing_layers["knowledge_check"] = {
>         "found": False,
>         "note": "RAG /search currently returns results: [] for this query; using safe offline mode."
>     }
251,252c318
<     # BBB safety filter
<     filtered_message = await _apply_bbb_filter(req.message)
---
>     # Step 2: Minimal context
254,266c320,324
<     # RAG context (optional)
<     rag_context = ""
<     rag_used = False
<     if req.use_rag:
<         rag_context = await _fetch_rag_context(filtered_message, req.user_id)
<         rag_used = bool(rag_context)
< 
<     # Ensemble generation — returns full expert list now
<     response_text, expert_responses, minds_participated = await generate_response(
<         message=filtered_message,
<         user_id=req.user_id,
<         context=req.context,
<         rag_context=rag_context,
---
>     recent_context = await get_recent_conversations(request.user_id, limit=3)
>     context = (
>         f"{recent_context}\n{existing_knowledge}"
>         if existing_knowledge
>         else recent_context
267a326,329
>     processing_layers["web_search"] = {
>         "executed": not bool(existing_knowledge),
>         "reason": "knowledge_exists" if existing_knowledge else "will_store_after_response",
>     }
269,292c331,340
<     # Divergence scoring
<     divergence_score = _compute_divergence(expert_responses)
<     divergence_flag  = divergence_score > DIVERGENCE_THRESHOLD
< 
<     if divergence_flag:
<         logger.warning(
<             "HIGH DIVERGENCE user=%s score=%.4f minds=%d",
<             req.user_id, divergence_score, minds_participated,
<         )
<         response_text = (
<             "[Epistemic status: high ensemble divergence detected. "
<             "This response may contain low-consensus claims and should be treated as provisional.]\n\n"
<             + response_text
<         )
< 
<         # When we HAVE grounded retrieval but the minds still disagree,
<         # prepend a short verification reminder rather than downgrading.
<         if rag_used:
<             verify_note = (
<                 "Note: Even though this answer draws on Ms. Allis's internal documents, "
<                 "please verify organization names, locations, and contact details with "
<                 "official county/state sites and the organizations themselves before relying on them.\n\n"
<             )
<             response_text = verify_note + response_text
---
>     # Consciousness layers (stubbed as active)
>     consciousness = await add_consciousness_layers(request.message, request.user_id)
>     processing_layers["consciousness"] = consciousness
> 
>     # Step 3: Generation (safe greeting for now)
>     response_text = await generate_response(request.message, context)
>     processing_layers["generation"] = {
>         "completed": True,
>         "length": len(response_text),
>     }
294,301c342,352
<         # Hilbert mediation temporarily disabled:
<         # service at HILBERT_URL is reachable, but its live API exposes
<         # /embed, /state, /superposition, etc. — not /analyze.
<         # Keep high-divergence disclaimer, skip the bad side-call.
< 
<         # Strict downgrade for local-resource lookups when we lack grounded retrieval.
<         if not rag_used and _is_local_resource_query(req.message):
<             response_text = _downgrade_local_resource_answer(req.message)
---
>     # Step 4: BBB filter
>     bbb_result = await filter_through_bbb(response_text)
>     processing_layers["bbb_filter"] = bbb_result
> 
>     # Step 5: Truth verification
>     verified = await verify_truth(response_text)
>     processing_layers["truth_verification"] = {"verified": bool(verified)}
> 
>     # Step 6: Store conversation
>     stored = await store_conversation(request.user_id, request.message, response_text)
>     processing_layers["storage"] = {"stored": stored}
303c354,355
<     latency_ms = int((time.monotonic() - t0) * 1000)
---
>     # UEID logging stub
>     await log_message_to_ueid(conversation_id, ueid, request.message, response_text)
307,316c359,361
<         user_id=req.user_id,
<         session_id=req.session_id,
<         expert_responses=expert_responses,
<         pipeline=PipelineInfo(
<             minds_participated=minds_participated,
<             divergence_score=divergence_score,
<             divergence_flag=divergence_flag,
<             rag_used=rag_used,
<             latency_ms=latency_ms,
<         ),
---
>         source="chromadb_rag_web_consensus",
>         verified=bool(verified),
>         processing_layers=processing_layers,
320,331d364
< # ── /minds ────────────────────────────────────────────────────────────────────
< @app.get("/minds")
< async def minds_status():
<     """Proxy to ensemble roster."""
<     try:
<         async with httpx.AsyncClient(timeout=httpx.Timeout(10.0)) as client:
<             r = await client.get(f"{CONSENSUS_URL}/model_roster")
<             return r.json()
<     except Exception as exc:
<         raise HTTPException(502, f"Could not reach ensemble: {exc}")
< 
< 
334c367,368
<     uvicorn.run(app, host="0.0.0.0", port=8018, log_level="info")
---
> 
>     uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
(.venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ # Does ms_jarvis_production_chat.py import itself or get imported from somewhere?
head -20 /opt/msjarvis-rebuild/services/ms_jarvis_production_chat.py
# Is it a FastAPI app run directly, or is it imported by another file?
grep -rn "ms_jarvis_production_chat\|import.*production_chat" \
  /opt/msjarvis-rebuild/ --include="*.py" 2>/dev/null | grep -v __pycache__ | grep -v ".bak"
"""
ms_jarvis_production_chat.py — PATCHED 2026-06-07
Fixes:
  1. generate_response() now returns (text, expert_responses, minds_participated)
  2. _compute_divergence() added — Jaccard 5-gram pairwise distance
  3. /chat response includes pipeline.divergence_score + pipeline.divergence_flag
"""
import asyncio
import httpx
import logging
import os
import re
import time
from typing import Any, Dict, List, Optional, Tuple

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

logger = logging.getLogger("ms_jarvis_production_chat")
/opt/msjarvis-rebuild/_archive/generated_20260430/add_jarvis_personality.py:12:subprocess.run(["pkill", "-f", "ms_jarvis_production_chat.py"])
/opt/msjarvis-rebuild/_archive/generated_20260430/add_jarvis_personality.py:17:code = open("ms_jarvis_production_chat.py", "r").read()
/opt/msjarvis-rebuild/_archive/generated_20260430/add_jarvis_personality.py:26:with open("ms_jarvis_production_chat.py", "w") as f:
/opt/msjarvis-rebuild/_archive/generated_20260430/add_jarvis_personality.py:30:subprocess.Popen(["nohup", "python3", "ms_jarvis_production_chat.py"], 
/opt/msjarvis-rebuild/_archive/generated_20260430/add_conversation_context.py:8:subprocess.run(["pkill", "-f", "ms_jarvis_production_chat.py"])
/opt/msjarvis-rebuild/_archive/generated_20260430/add_conversation_context.py:10:with open("ms_jarvis_production_chat.py", "r") as f:
/opt/msjarvis-rebuild/_archive/generated_20260430/add_conversation_context.py:53:with open("ms_jarvis_production_chat.py", "w") as f:
/opt/msjarvis-rebuild/_archive/generated_20260430/add_conversation_context.py:57:    ["nohup", "python3", "ms_jarvis_production_chat.py"],
/opt/msjarvis-rebuild/_archive/generated_20260430/fix_creator_recognition.py:8:with open('ms_jarvis_production_chat.py', 'r') as f:
/opt/msjarvis-rebuild/_archive/generated_20260430/fix_creator_recognition.py:35:    with open('ms_jarvis_production_chat.py', 'w') as f:
/opt/msjarvis-rebuild/_archive/generated_20260430/fix_storage.py:6:with open("ms_jarvis_production_chat.py", "r") as f:
/opt/msjarvis-rebuild/_archive/generated_20260430/fix_storage.py:56:with open("ms_jarvis_production_chat.py", "w") as f:
/opt/msjarvis-rebuild/_archive/generated_20260430/update_production_to_v9.py:1:with open("ms_jarvis_production_chat.py", "r") as f:
/opt/msjarvis-rebuild/_archive/generated_20260430/update_production_to_v9.py:26:with open("ms_jarvis_production_chat.py", "w") as f:
/opt/msjarvis-rebuild/_archive/generated_20260430/fix_rag_store.py:9:subprocess.run(["pkill", "-f", "ms_jarvis_production_chat.py"])
/opt/msjarvis-rebuild/_archive/generated_20260430/fix_rag_store.py:12:with open("ms_jarvis_production_chat.py", "r") as f:
/opt/msjarvis-rebuild/_archive/generated_20260430/fix_rag_store.py:35:with open("ms_jarvis_production_chat.py", "w") as f:
/opt/msjarvis-rebuild/_archive/generated_20260430/fix_rag_store.py:40:    ["nohup", "python3", "ms_jarvis_production_chat.py"],
/opt/msjarvis-rebuild/_archive/generated_20260430/fix_prompt_leak.py:7:with open("ms_jarvis_production_chat.py", "r") as f:
/opt/msjarvis-rebuild/_archive/generated_20260430/fix_prompt_leak.py:66:with open("ms_jarvis_production_chat.py", "w") as f:
/opt/msjarvis-rebuild/services/ms_jarvis_production_chat.py:2:ms_jarvis_production_chat.py — PATCHED 2026-06-07
/opt/msjarvis-rebuild/services/ms_jarvis_production_chat.py:20:logger = logging.getLogger("ms_jarvis_production_chat")
/opt/msjarvis-rebuild/services/ms_jarvis_production_chat.py:243:    return {"status": "ok", "service": "ms_jarvis_production_chat", "version": "2.1.0-patched"}
/opt/msjarvis-rebuild/services/add_jarvis_personality.py:12:subprocess.run(["pkill", "-f", "ms_jarvis_production_chat.py"])
/opt/msjarvis-rebuild/services/add_jarvis_personality.py:17:code = open("ms_jarvis_production_chat.py", "r").read()
/opt/msjarvis-rebuild/services/add_jarvis_personality.py:26:with open("ms_jarvis_production_chat.py", "w") as f:
/opt/msjarvis-rebuild/services/add_jarvis_personality.py:30:subprocess.Popen(["nohup", "python3", "ms_jarvis_production_chat.py"], 
/opt/msjarvis-rebuild/services/add_conversation_context.py:8:subprocess.run(["pkill", "-f", "ms_jarvis_production_chat.py"])
/opt/msjarvis-rebuild/services/add_conversation_context.py:10:with open("ms_jarvis_production_chat.py", "r") as f:
/opt/msjarvis-rebuild/services/add_conversation_context.py:53:with open("ms_jarvis_production_chat.py", "w") as f:
/opt/msjarvis-rebuild/services/add_conversation_context.py:57:    ["nohup", "python3", "ms_jarvis_production_chat.py"],
/opt/msjarvis-rebuild/services/fix_creator_recognition.py:8:with open('ms_jarvis_production_chat.py', 'r') as f:
/opt/msjarvis-rebuild/services/fix_creator_recognition.py:35:    with open('ms_jarvis_production_chat.py', 'w') as f:
/opt/msjarvis-rebuild/services/fix_storage.py:6:with open("ms_jarvis_production_chat.py", "r") as f:
/opt/msjarvis-rebuild/services/fix_storage.py:56:with open("ms_jarvis_production_chat.py", "w") as f:
/opt/msjarvis-rebuild/services/update_production_to_v9.py:1:with open("ms_jarvis_production_chat.py", "r") as f:
/opt/msjarvis-rebuild/services/update_production_to_v9.py:26:with open("ms_jarvis_production_chat.py", "w") as f:
/opt/msjarvis-rebuild/services/fix_rag_store.py:9:subprocess.run(["pkill", "-f", "ms_jarvis_production_chat.py"])
/opt/msjarvis-rebuild/services/fix_rag_store.py:12:with open("ms_jarvis_production_chat.py", "r") as f:
/opt/msjarvis-rebuild/services/fix_rag_store.py:35:with open("ms_jarvis_production_chat.py", "w") as f:
/opt/msjarvis-rebuild/services/fix_rag_store.py:40:    ["nohup", "python3", "ms_jarvis_production_chat.py"],
/opt/msjarvis-rebuild/services/fix_prompt_leak.py:7:with open("ms_jarvis_production_chat.py", "r") as f:
/opt/msjarvis-rebuild/services/fix_prompt_leak.py:66:with open("ms_jarvis_production_chat.py", "w") as f:
/opt/msjarvis-rebuild/patches/ms_jarvis_production_chat_patched.py:2:ms_jarvis_production_chat.py — PATCHED 2026-06-07
/opt/msjarvis-rebuild/patches/ms_jarvis_production_chat_patched.py:20:logger = logging.getLogger("ms_jarvis_production_chat")
/opt/msjarvis-rebuild/patches/ms_jarvis_production_chat_patched.py:169:    return {"status": "ok", "service": "ms_jarvis_production_chat", "version": "2.1.0-patched"}
(.venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ 

