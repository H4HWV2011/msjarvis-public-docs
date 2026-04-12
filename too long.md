   - 127.0.0.1:8221:8221
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild/msjarvis-rebuild$ # Commit all the fixed Dockerfiles
git add services/Dockerfile-llm*
git commit -m "fix: replace stub Dockerfiles for llm1,4,7,13,21-proxy with real Python proxies

llm13-proxy: was alpine placeholder, now python:3.12-slim + gemma:2b
llm1,4,7,21-proxy: were alpine sleep stubs, now proper uvicorn proxies
All ports verified against docker-compose.yml (8201,8204,8207,8213,8221)"

# Now rebuild llm13 (the one we actually need right now)
docker compose up -d --no-deps --build llm13-proxy
sleep 10
docker exec llm13-proxy grep -n "gemma\\|orca" /app/llm13_health_proxy.py
fatal: pathspec 'services/Dockerfile-llm10-proxy' is beyond a symbolic link
On branch chore/ch29-closeout-rbac-pia-2026-04-07
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   ../Dockerfile.brain
	modified:   ../Dockerfile.gateway
	modified:   ../VERIFYANDTEST.sh
	modified:   ../config/Caddyfile
	modified:   ../docker-compose-core.yml
	deleted:    ../docker-compose.override.yml
	modified:   ../docker-compose.yml
	deleted:    ../docker-compose.yml.bak
	deleted:    ../docker-compose.yml.bak.20260312-002553
	deleted:    ../docker-compose.yml.bak.20260312-002755
	deleted:    ../docker-compose.yml.bak.20260312-002852
	deleted:    ../docker-compose.yml.bak_20260310-184927
	modified:   ../ms_jarvis_rag_server.py
	modified:   docker-compose.yml
	modified:   ../neurobiological_brain/i_containers/service/neurobiologicalbrain/subconscious/service/consciousness_bridge.py
	modified:   ../neurobiological_brain/spiritual_root/service/spiritual_root.py
	modified:   ../requirements.txt
	modified:   ../scripts/audit_36.sh
	modified:   ../scripts/jarvis_auth_service.py
	modified:   ../scripts/preflight_gate.sh
	modified:   ../scripts/sprint3_adversarial_tests.py
	modified:   ../services-safe/docker-compose.yml
	modified:   ../services-safe/egeria_autonomous_inquiry.py
	modified:   ../services-safe/ms_jarvis_autonomous_learner_optimized.py
	modified:   ../services-safe/ms_jarvis_rag_server.py
	modified:   ../services-safe/requirements.txt
	modified:   ../services/Dockerfile
	modified:   ../services/Dockerfile-llm1-proxy
	modified:   ../services/Dockerfile-llm13-proxy
	modified:   ../services/Dockerfile-llm21-proxy
	modified:   ../services/Dockerfile-llm4-proxy
	modified:   ../services/Dockerfile-llm7-proxy
	modified:   ../services/Dockerfile.aaacpe_rag
	modified:   ../services/Dockerfile.aaacpe_scraper
	modified:   ../services/Dockerfile.crypto-policy
	modified:   ../services/Dockerfile.hippocampus
	modified:   ../services/Dockerfile.icontainers
	modified:   ../services/Dockerfile.judge
	modified:   ../services/Dockerfile.local-resources
	deleted:    ../services/Dockerfile.policy
	modified:   ../services/Dockerfile.spiritual_rag
	deleted:    ../services/Dockerfile.steward
	modified:   ../services/Dockerfile.woah
	modified:   ../services/aaacpe_scraper_service.py
	modified:   ../services/ai_server_11llm_OPTIMIZED.py
	modified:   ../services/ai_server_20llm_PRODUCTION.py
	modified:   ../services/brain_orchestrator.py
	modified:   ../services/dao_governance.py
	modified:   ../services/egeria_autonomous_inquiry.py
	modified:   ../services/jarvis-aaacpe-rag_aaacpe_rag_service.py
	modified:   ../services/jarvis-constitutional-guardian_constitutional_api.py
	modified:   ../services/jarvis-gis-rag_gis_rag_service.py
	modified:   ../services/jarvis-hippocampus_hippocampus_service.py
	modified:   ../services/jarvis-semaphore_msjarvis_semaphore.py
	modified:   ../services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py
	modified:   ../services/jarvis_eeg_beta_5m.py
	modified:   ../services/jarvis_eeg_delta_30s.py
	modified:   ../services/jarvis_eeg_theta_60s.py
	modified:   ../services/jarviscryptopolicy.py
	modified:   ../services/judge_pipeline.py
	modified:   ../services/judgesigner.py
	modified:   ../services/llm13-proxy_llm13_health_proxy.py
	modified:   ../services/llm_consensus_20_FINAL.py
	modified:   ../services/main_brain.py
	modified:   ../services/ms_jarvis_autonomous_learner_optimized.py
	modified:   ../services/ms_jarvis_blood_brain_barrier.py
	modified:   ../services/ms_jarvis_memory.py
	typechange: ../services/ms_jarvis_qualia_engine.py
	modified:   ../services/ms_jarvis_rag_server.py
	modified:   ../services/ms_jarvis_unified_gateway.py
	modified:   ../services/ms_jarvis_web_research_aggregate.py
	typechange: ../services/msjarvis_fractal_consciousness.py
	modified:   ../services/msjarvisconsciousnessbridge_ACTUAL.py
	modified:   ../services/neurobiological_brain/blood_brain_barrier/safety_monitor.py
	modified:   ../services/neurobiological_brain/blood_brain_barrier/threat_detection.py
	modified:   ../services/neurobiological_brain/blood_brain_barrier/truth_verification.py
	modified:   ../services/requirements.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	../.dockerignore
	../26.0.1
	../911centers_wvdem_032819_gcs84_attrs.csv
	../=
	../Accept:
	../Dockerfile.neuro
	../GET
	../HTTP
	../Host:
	../User-Agent:
	../amtrackrails_federalrailroadadministration_200210_ll83_attrs.csv
	../amtrackrails_federalrailroadadministration_200210_utm83_attrs.csv
	../blockgroups_census_2000_ll83_attrs.csv
	../blockgroups_census_2000_utm83_attrs.csv
	../blockgroups_census_201111_gcs83_attrs.csv
	../blockgroups_census_2020_utm83_attrs.csv
	../blockgroups_census_2020_wma84_attrs.csv
	../boundaryappalachianbasin_wvges_1996_utm83_attrs.csv
	../calderl_reg_ll83_attrs.csv
	../citieswithpopulation_2500_census_201111_utm83_attrs.csv
	../citieswithpopulationover10k_census_201111_gcs83_attrs.csv
	../citieswithpopulationover10k_uscensus_1990_ll83_attrs.csv
	../citieswithpopulationover10k_uscensus_1990_utm83_attrs.csv
	../citieswithpopulationover2500_uscensus_1990_ll83_attrs.csv
	../citieswithpopulationsover10k_census_2020_utm83_attrs.csv
	../citieswithpopulationsover10k_census_2020_wma84_attrs.csv
	../citieswithpopulationsover2500_census_2020_utm83_attrs.csv
	../citieswithpopulatoinover2500_uscensus_1990_utm83_attrs.csv
	../coals2_ll83_attrs.csv
	../coals2_utm27_attrs.csv
	../coals2_utm83_attrs.csv
	../communityboundary_min_att_20250121_utm83_attrs.csv
	../correctionalinstitutions_hsip_20091230_utm83_attrs.csv
	../correctionalinstitutions_hsip_20091230_wgs84_attrs.csv
	../countycityparkboundaries_20201104_utm83_attrs.csv
	../countyseats_usgs_ll83_attrs.csv
	../countyseats_usgs_utm83_attrs.csv
	../courthousescounty_manysources_200203_utm83_attrs.csv
	../courthousesfederal_manysources_200203_ll83_attrs.csv
	../courthousesfederal_manysources_200203_utm_attrs.csv
	../cvfault_ll83_attrs.csv
	../cvfault_utm27_attrs.csv
	../cvpoly_ll83_attrs.csv
	../cvpoly_utm27_attrs.csv
	../cvpoly_utm83_attrs.csv
	../dams_usarmycorpsofengineers_200010_utm83_attrs.csv
	../dams_usarmycropsofengineers_200010_ll83_attrs.csv
	../damsnoncoal_usgs_2002_ll27_attrs.csv
	../db/schema/
	../deploy-brain.sh
	../deploy-gbim.sh
	../deploy-memory.sh
	../deploy-orchestrator.sh
	../deploy_gap_aware.sh
	../docker-compose.override.yml.disabled
	../docs/confidence_decay_baseline_20260402.txt
	../docs/mysql_schema.sql
	../docs/mysql_schema_dump_20260402.sql
	../docs/sprints/
	../empowermentzonesandenterprisecommunities_uscensus_2002_utm83_attrs.csv
	../empowermentzonesandenterprisecommunitiesbytract_uscens_30c72907_attrs.csv
	../excursionpassengertrains_wvdof_200102_ll83_attrs.csv
	../excursionpassengertrains_wvdof_200102_utm83_attrs.csv
	../facilities_epa_200203_ll83_attrs.csv
	../facilities_epa_200203_utm83_attrs.csv
	../fault_reg_ll83_attrs.csv
	../faultgl_reg_ll83_attrs.csv
	../features_attrs.csv
	../fire_departments_attrs.csv
	../fire_dept_wvdem_092017_utm83_attrs.csv
	../floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83_attrs.csv
	../geographicalnamesonusgstopomaps_usgs_200601_ll27_attrs.csv
	../geographicalnamesonusgstopomaps_usgs_200601_utm83_attrs.csv
	../geographicnamesonusgstopomaps_current_usgs_20110801_ll83_attrs.csv
	../geographicnamesonusgstopomaps_current_usgs_20110801_utm83_attrs.csv
	../geographicnamesonusgstopomaps_historical_usgs_20110801_ll83_attrs.csv
	../geographicnamesonusgstopomaps_historical_usgs_20110801_utm83_attrs.csv
	../geographicnamesonusgstopomaps_usgs_20110801_ll83_attrs.csv
	../geographicnamesonusgstopomaps_usgs_20110801_utm83_attrs.csv
	../geolgyl_reg_ll83_attrs.csv
	../geolgyp_reg_ll83_attrs.csv
	../geotextl_reg_ll83_attrs.csv
	../hazardmitigationbuyout_20250929_polygons_utm83_attrs.csv
	../hazardmitigationbuyout_20250929_polygons_wma84_attrs.csv
	../healthruralfacilities_manysources_utm83_attrs.csv
	../highered_wvemd_072420_utm83_attrs.csv
	../highered_wvemd_072420_wgc84_attrs.csv
	../hospitals_attrs.csv
	../impact_reg_ll83_attrs.csv
	../indexgrid15minutequads_wvgistc_ll83_attrs.csv
	../indexgrid15minutequads_wvgistc_utm83_attrs.csv
	../indexgrid15minutewithcounties_wvgistc_utm27_attrs.csv
	../indexgrid1minutequads_wvgistc_ll83_attrs.csv
	../industrialbuildings_wvdo_200807_utm83_attrs.csv
	../industrialparks_wvdo_200078_utm83_attrs.csv
	../industrialsites_wvdo_200807_utm83_attrs.csv
	../inedexgrid1minutequads_wvgistc_utm83_attrs.csv
	../intermodalterminalfacilities_usdot_1997_ll83_attrs.csv
	../intermodalterminalfacilities_usdot_1997_utm83_attrs.csv
	../jarviscryptopolicy.py
	../libraries_manysources_2001_ll27_attrs.csv
	../libraries_manysources_2001_utm83_attrs.csv
	../logs/ops_history/
	../logs/qualia_woah/
	../logs/redteam_bbb/
	../majorriversandlakesline_nhd_2002_ll83_attrs.csv
	../majorriversandlakesline_nhd_2002_utm83_attrs.csv
	../majorriversandlakespolygon_nhd_2002_poly_ll83_attrs.csv
	../manufacturingandbusiness_wvdo_200803_utm83_attrs.csv
	../metfacp_reg_ll83_attrs.csv
	../metropolitanandmicropolitanstatisticalareas_census_201111_gcs83_attrs.csv
	../metropolitanandmicropolitanstatisticalareas_census_2020_wma84_attrs.csv
	../metropolitanstatisticalareas_uscensus_199901_ll83_attrs.csv
	../metropolitanstatisticalareas_uscensus_199901_utm83_attrs.csv
	../mineraloperations_usgs_200204_ll83_attrs.csv
	../mineraloperations_usgs_200204_utm83_attrs.csv
	../minesabandonedlandsline_wvdep_1996_noprojectoin_attrs.csv
	../minesabandonedlandspoint_wvdep_1996_noprojection_attrs.csv
	../minesabandonedlandspolygon_wvdep_1996_noprojection_attrs.csv
	../ms_jarvis_blood_brain_barrier.py
	Dockerfile.fractal
	Dockerfile.woah
	gbim_query_router.py
	services
	../nationalatlasstreams_usgs_199903_ll83_attrs.csv
	../nationalatlasstreams_usgs_199903_utm83_attrs.csv
	../nationalregister_point_20200923_attrs.csv
	../nationalregister_point_20200923_utm27_attrs.csv
	../nationalregisterofhistoricplacespoints_natoinalpakrser_8d965955_attrs.csv
	../nationalregisterofhistoricplacespolygons_nationaparkse_b9d30a70_attrs.csv
	../nationalwaterwaynetwork_usarmycorpsofengineers_2001_utm83_attrs.csv
	../nationalwaterwaynetworkports_usarmycorpsofengineers_2001_ll83_attrs.csv
	../nationaregisterofhistoricplacespolygons_nationalparkse_cab42150_attrs.csv
	../natoinalregisterofhistoricplacespoints_nationalparkser_ca43510e_attrs.csv
	../naviagablewaterways_usarmycropsofengineers_2006_utm83_attrs.csv
	../navigablewaterwaysrivermiles_usarmycropsofengineers_2006_utm83_attrs.csv
	../navigablewaterwaysstructures_usarmycorpsofengineers_2006_utm83_attrs.csv
	../observability/docker-compose.yml
	../observability/grafana/
	../observability/otel/config.yaml
	../observability/prometheus/prometheus.yml
	../observability/scripts/
	../officebuildings_wvdo_200807_utm83_attrs.csv
	../oi36a-mitigation.sh
	../output/
	../paroleoffices_manysources_2008_utm83_attrs.csv
	../paroleoffices_manysources_2008_wgs84_attrs.csv
	../patch_gate.py
	../placesofworship_hsip_20080723_utm83_attrs.csv
	../placesofworship_hsip_20080723_wgs84_attrs.csv
	../policedept_wvdem_012319_gcs84_attrs.csv
	../policedept_wvdem_012319_utm83_attrs.csv
	../populatedplaces_census_201112_utm83_attrs.csv
	../populatedplaces_census_20112_gcs83_attrs.csv
	../populatedplaces_census_2020_utm83_attrs.csv
	../populatedplaces_census_2020_wma84_attrs.csv
	../populatedplaces_uscensus_1990_utm83_attrs.csv
	../populationdatablockgroups_uscensus_2000_ll83_attrs.csv
	../populationdatablockgroups_uscensus_2000_utm83_attrs.csv
	../pow_wvgistc_062919_utm83_attrs.csv
	../pow_wvgistc_062919_wgs84_attrs.csv
	../publichealthdepts_hsip_20091229_utm83_attrs.csv
	../railnetworkregion_usdot_200203_ll83_attrs.csv
	../railnetworkregion_usdot_200203_utm83_attrs.csv
	../railnetworkwv_usdot_200203_ll83_attrs.csv
	../railnetworkwv_usdot_200203_utm83_attrs.csv
	../railroads_rahalltransportationinstitute_2005_utm83_attrs.csv
	../realtimestreamflowstations_usgs_200012_ll27_attrs.csv
	../realtimestreamflowstations_usgs_200012_utm27_attrs.csv
	../realtimestreamflowstations_usgs_200012_utm83_attrs.csv
	../regionalplanninganddevelopmentcouncil_wvdo_1971_ll83_attrs.csv
	../regionalplanninganddevelopmentcouncil_wvdo_1971_utm83_attrs.csv
	../scripts/aaacpe_scraper.py
	../scripts/check-constitutional-health.sh
	../scripts/close_chapter_26.sh
	../scripts/gbim_axis_loader.sql
	../scripts/gbim_decay_refresh.sh
	../scripts/oi38_seed_collections.py
	../scripts/refresh_gbim_spatial.sh
	../scripts/run_aaacpe_scraper.sh
	../scripts/system_audit.sh
	../scripts/test_session_sidecar.sh
	../services-576-recovered/
	../services-nvme1-recovered/
	../services-safe/auth-proxy/
	../services-safe/gbim_recovered/
	../services-safe/session_buffer_minimal.py
	../services/Dockerfile.bbb
	../services/archived-dockerfiles/
	../services/constitutional_principles.json
	../services/eeg_shared/
	../services/entityid_to_chromaid.pkl
	../services/gbim_benefit_indexer/
	../services/gbim_query_router/
	../services/gis_dataset_services/
	../services/identity_promotion.py
	../services/jarvis_data_ingest.py
	../services/jarvis_gis_rag/
	../services/jarvis_pia_status.py
	../services/jarvis_rag_search/
	../services/llm13_health_proxy.py
	../services/llm_judge_v3.py
	../services/main_brain.py.manualbak
	../services/main_brain.py.manualbak3
	../services/main_brain.py.manualbak4
	../services/main_brain.py.manualbak5
	../services/main_brain.py.pre_aaacpe_patch
	../services/otel_tracing.py
	../services/rag_grounded_v2.py
	../services/requirements-ingest.txt
	../services/rotate_judge_keys.sh
	../services/spiritual_origins.geojson
	../sewertreatmentplants_wvdep_200203_utm83_attrs.csv
	../solidwastefacilities_wvdep_200202_ll83_attrs.csv
	../solidwastefacilities_wvdep_200202_utm83_attrs.csv
	../springs_wvges_1986_ll83_attrs.csv
	../springs_wvges_1986_utm83_attrs.csv
	../stateofwvhousedistricts_wvlegislativeservices_2010_attrs.csv
	../stateofwvsenatedistricts_wvlegislativeservices_2010_attrs.csv
	../states_region_ll83_attrs.csv
	../structurepolygons_samb_2003_utm83_attrs.csv
	../summits_gistc_052012_utm83_shp_attrs.csv
	../summits_gistc_052012_wgs84_shp_attrs.csv
	../surveycontrol_nationalgeodeticsurvey_102011_gcs83_attrs.csv
	../test_query.sh
	../tmp-aaacpe-patch/
	../tools/
	../towers_wvpublicbroadcasting_2002_ll83_attrs.csv
	../towers_wvpublicbroadcasting_2002_utm83_attrs.csv
	../towersam_fcc_200202_utm83_attrs.csv
	../towersasr_fcc_200202_ll83_attrs.csv
	../towersasr_fcc_200202_utm83_attrs.csv
	../towerscellular_fcc_200202_ll83_attrs.csv
	../towerscellular_fcc_200202_utm83_attrs.csv
	../towersfm_fcc_200202_utm83_attrs.csv
	../towersmicrowave_fcc_200202_ll83_attrs.csv
	../towersmicrowave_fcc_200202_utm83_attrs.csv
	../towerspager_fcc_200202_ll83_attrs.csv
	../towerspager_fcc_200202_utm83_attrs.csv
	../veteransaffairsfacilities_manysources_200503_utm83_attrs.csv
	../veteransaffairsfacilities_manysources_200503_wgs84_attrs.csv
	../votingdistrictswv_legislativeservices_2002_utm83_attrs.csv
	../votingdistrictswv_uscensus_2000_utm83_attrs.csv
	../weatherstations_nationalclimatedatacenter_1999_gcs83_attrs.csv
	../weatherstations_nationalclimatedatacenter_1999_utm27_attrs.csv
	../windenergyresource_nationalrenewableenergylab_200901_utm83_attrs.csv
	../windenergyresource_nationalrenewableenergylab_200901_wgs84_attrs.csv
	../wv_county_boundaries_24k_topo_updated_2022_utm83_attrs.csv
	../wv_microsoft_20180207_utm17n83_attrs.csv
	../wv_tax_districts_ll83_attrs.csv
	../wv_tax_districts_wma84_attrs.csv
	../wvstatebounadary100k_usgs_200203_utm83_attrs.csv
	../wvstateboundary100k_usgs_200203_ll83_attrs.csv
	../wvstateboundary24k_usgs_200203_utm83_attrs.csv
	../wvstatehousedistricts_manysources_1992_ll83_attrs.csv
	../wvstatehousedistricts_manysources_1992_utm83_attrs.csv
	../wvstatehousedistricts_manysources_2002_ll83_attrs.csv
	../wvstatehousedistricts_manysources_2002_utm83_attrs.csv
	../wvstatesenatedistricts_manysources_1992_ll83_attrs.csv
	../wvstatesenatedistricts_manysources_1992_utm83_attrs.csv
	../wvstatesenatedistricts_manysources_2002_ll83_attrs.csv
	../wvstatesenatedistricts_wvlegislativeservices_2020_utm83_attrs.csv
	../zipcodetabulationarea_census_2020_utm83_attrs.csv
	../zipcodetabulationarea_census_2020_wma84_attrs.csv

no changes added to commit (use "git add" and/or "git commit -a")
[+] Building 0.9s (11/11) FINISHED                                                  
 => [internal] load local bake definitions                                     0.0s
 => => reading from stdin 645B                                                 0.0s
 => [internal] load build definition from Dockerfile-llm13-proxy               0.0s
 => => transferring dockerfile: 246B                                           0.0s
 => [internal] load metadata for docker.io/library/python:3.12-slim            0.7s
 => [internal] load .dockerignore                                              0.0s
 => => transferring context: 2B                                                0.0s
 => [1/4] FROM docker.io/library/python:3.12-slim@sha256:804ddf3251a60bbf9c92  0.0s
 => => resolve docker.io/library/python:3.12-slim@sha256:804ddf3251a60bbf9c92  0.0s
 => [internal] load build context                                              0.0s
 => => transferring context: 43B                                               0.0s
 => CACHED [2/4] WORKDIR /app                                                  0.0s
 => CACHED [3/4] COPY llm13_health_proxy.py .                                  0.0s
 => CACHED [4/4] RUN pip install fastapi uvicorn httpx                         0.0s
 => exporting to image                                                         0.0s
 => => exporting layers                                                        0.0s
 => => writing image sha256:2beec03cf2b86e3a1f1ab994d9c72d859187f5aab4aa1a73f  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-llm13-proxy                0.0s
 => resolving provenance for metadata file                                     0.0s
WARN[0001] Found orphan containers ([msjarvis-rebuild-jarvis-rag-search-1 jarvis-gis-rag jarvis-hilbert-state jarvis-data-ingest jarvis-redis-local]) for this project. If you removed or renamed this service in your compose file, you can run this command with the --remove-orphans flag to clean it up. 
[+] up 2/2
 ✔ Image msjarvis-rebuild-llm13-proxy Built                                     1.0s
 ✔ Container llm13-proxy              Started                                   0.0s
Error response from daemon: Container a450458e4e3574db121cbeba9893914f38662b6e06f743782ad506a68912fd50 is restarting, wait until the container is running
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild/msjarvis-rebuild$ 

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild/msjarvis-rebuild$ docker ps --format "table {{.Names}}\\t{{.Status}}\\t{{.Ports}}" | grep llm | sort
jarvis-20llm-production                                 Up 13 minutes                   127.0.0.1:8008->8008/tcp
jarvis-llm-judge-v3                                     Up 2 days                       127.0.0.1:7240->7240/tcp
llm10-proxy                                             Up 2 days                       127.0.0.1:8210->8210/tcp
llm11-proxy                                             Up 2 days                       127.0.0.1:8211->8211/tcp
llm12-proxy                                             Up 2 days                       127.0.0.1:8212->8212/tcp
llm13-proxy                                             Restarting (1) 24 seconds ago   
llm14-proxy                                             Up 2 days                       127.0.0.1:8214->8214/tcp
llm15-proxy                                             Up 2 days                       127.0.0.1:8215->8215/tcp
llm16-proxy                                             Up 2 days                       127.0.0.1:8216->8216/tcp
llm17-proxy                                             Up 2 days                       127.0.0.1:8217->8217/tcp
llm18-proxy                                             Up 2 days                       127.0.0.1:8218->8218/tcp
llm19-proxy                                             Up 2 days                       127.0.0.1:8219->8219/tcp
llm1-proxy                                              Up 2 days                       127.0.0.1:8201->8201/tcp
llm20-proxy                                             Up 2 days                       127.0.0.1:8220->8220/tcp
llm21-proxy                                             Up 2 days                       127.0.0.1:8221->8221/tcp
llm22-proxy                                             Up 2 days                       127.0.0.1:8222->8222/tcp
llm2-proxy                                              Up 2 days                       127.0.0.1:8202->8202/tcp
llm3-proxy                                              Up 2 days                       127.0.0.1:8203->8203/tcp
llm4-proxy                                              Up 2 days                       127.0.0.1:8204->8204/tcp
llm5-proxy                                              Up 2 days                       127.0.0.1:8205->8205/tcp
llm6-proxy                                              Up 2 days                       127.0.0.1:8206->8206/tcp
llm7-proxy                                              Up 2 days                       127.0.0.1:8207->8207/tcp
llm8-proxy                                              Up 2 days                       127.0.0.1:8208->8208/tcp
llm9-proxy                                              Up 2 days                       127.0.0.1:8209->8209/tcp
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild/msjarvis-rebuild$ 

    127.0.0.1:8209->8209/tcp
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild/msjarvis-rebuild$ docker ps
CONTAINER ID   IMAGE                                                 COMMAND                  CREATED              STATUS                          PORTS                                                                                                          NAMES
a450458e4e35   msjarvis-rebuild-llm13-proxy                          "uvicorn llm13_healt…"   About a minute ago   Restarting (1) 38 seconds ago                                                                                                                  llm13-proxy
8cd24a1b2569   ollama/ollama:latest                                  "/bin/ollama serve"      16 minutes ago       Up 16 minutes                   127.0.0.1:11434->11434/tcp                                                                                     jarvis-ollama
3408ed865618   msjarvis-rebuild-jarvis-semaphore                     "uvicorn msjarvis_se…"   2 hours ago          Up 2 hours                      127.0.0.1:8030->8030/tcp                                                                                       jarvis-semaphore
b9ee5e2bc9a1   msjarvis-rebuild-jarvis-main-brain                    "sh -lc 'cd /app/ser…"   3 hours ago          Up 3 hours                      127.0.0.1:8050->8050/tcp                                                                                       jarvis-main-brain
564fcf722aa8   msjarvis-rebuild-jarvis-memory                        "uvicorn ms_jarvis_m…"   5 hours ago          Up 5 hours                      127.0.0.1:8056->8056/tcp                                                                                       jarvis-memory
65a37d26268f   python:3.11-slim                                      "sh -c 'pip install …"   6 hours ago          Up 6 hours                      127.0.0.1:8029->8029/tcp                                                                                       jarvis-pia-status
b745a8580f0f   msjarvis-rebuild_psychological_rag_domain             "python psychologica…"   6 hours ago          Up 6 hours                      9006/tcp, 127.0.0.1:9006->8006/tcp                                                                             psychological_rag_domain
26b9ca22a972   msjarvis-rebuild-jarvis-psychology-services:latest    "python ms_jarvis_ps…"   6 hours ago          Up 6 hours                      127.0.0.1:8019->8019/tcp                                                                                       jarvis-psychology-services
4bc748ffff8b   chromadb/chroma:0.5.20                                "/docker_entrypoint.…"   7 hours ago          Up 6 hours                      127.0.0.1:8002->8000/tcp                                                                                       jarvis-chroma
4301d0e621e8   msjarvis-rebuild-jarvis-rag-server                    "uvicorn ms_jarvis_r…"   17 hours ago         Up 17 hours (healthy)           127.0.0.1:8003->8003/tcp                                                                                       jarvis-rag-server
ecfa5bcb7f65   services-safe-jarvis-auth-proxy                       "uvicorn main:app --…"   24 hours ago         Up 24 hours                     127.0.0.1:8080->8080/tcp                                                                                       jarvis-auth-proxy
86c59bc806d0   chromadb/chroma:latest                                "dumb-init -- chroma…"   25 hours ago         Up 25 hours                     127.0.0.1:8001->8000/tcp                                                                                       chromadb
c2bc04943db9   msjarvis-rebuild-jarvis-rag-search                    "uvicorn main:app --…"   25 hours ago         Up 25 hours                     127.0.0.1:8095->8095/tcp                                                                                       msjarvis-rebuild-jarvis-rag-search-1
beb2191686a5   grafana/grafana:10.2.3                                "/run.sh"                25 hours ago         Up 25 hours                     127.0.0.1:3000->3000/tcp                                                                                       jarvis-grafana
f374c61cf1e7   jaegertracing/all-in-one:1.52                         "/go/bin/all-in-one-…"   25 hours ago         Up 25 hours                     4317-4318/tcp, 5775/udp, 5778/tcp, 9411/tcp, 14250/tcp, 14268/tcp, 6831-6832/udp, 127.0.0.1:16686->16686/tcp   jarvis-jaeger
f87a27c72ae6   prom/prometheus:v2.48.0                               "/bin/prometheus --c…"   25 hours ago         Up 25 hours                     127.0.0.1:9090->9090/tcp                                                                                       jarvis-prometheus
812c37fa7bd6   otel/opentelemetry-collector-contrib:0.93.0           "/otelcol-contrib --…"   25 hours ago         Up 25 hours                     127.0.0.1:4317-4318->4317-4318/tcp, 127.0.0.1:8888->8888/tcp, 127.0.0.1:13133->13133/tcp, 55678-55679/tcp      jarvis-otel-collector
829abf189295   msjarvis-rebuild-jarvis-i-containers                  "/opt/nvidia/nvidia_…"   25 hours ago         Up 25 hours                     127.0.0.1:8015->8015/tcp                                                                                       jarvis-i-containers
99009d894838   msjarvis-rebuild-jarvis-judge-consistency             "python3 judge_consi…"   25 hours ago         Up 25 hours                     127.0.0.1:8042->8042/tcp                                                                                       jarvis-judge-consistency
3f8c87865eb4   msjarvis-rebuild-jarvis-judge-truth                   "python3 judge_truth…"   25 hours ago         Up 25 hours                     127.0.0.1:8041->8041/tcp                                                                                       jarvis-judge-truth
727d01bdea37   msjarvis-rebuild-jarvis-judge-alignment               "python3 judge_align…"   25 hours ago         Up 25 hours                     127.0.0.1:8043->8043/tcp                                                                                       jarvis-judge-alignment
6d47f0e0b874   msjarvis-rebuild-jarvis-judge-ethics                  "python3 judge_ethic…"   25 hours ago         Up 25 hours                     127.0.0.1:8044->8044/tcp                                                                                       jarvis-judge-ethics
f01d0e7e57be   msjarvis-rebuild-jarvis-judge-pipeline                "python3 judge_pipel…"   25 hours ago         Up 25 hours                     127.0.0.1:8040->8040/tcp                                                                                       jarvis-judge-pipeline
107a0a630d3c   msjarvis-rebuild-jarvis-gbim-query-router             "python3 gbim_query_…"   25 hours ago         Up 25 hours                     127.0.0.1:7205->7205/tcp                                                                                       jarvis-gbim-query-router
e9317b62c269   msjarvis-rebuild-jarvis-gis-rag:latest                "uvicorn gis_rag_ser…"   26 hours ago         Up 26 hours                     127.0.0.1:8004->8004/tcp                                                                                       jarvis-gis-rag
b9b7327ebc3e   msjarvis-crypto-policy:latest                         "uvicorn jarviscrypt…"   26 hours ago         Up 26 hours (healthy)           127.0.0.1:8099->8099/tcp                                                                                       369b2f771ae5_jarvis-crypto-policy
c5d34cfddca2   python:3.11-slim                                      "sh -c 'pip install …"   26 hours ago         Up 26 hours                     127.0.0.1:18092->8081/tcp                                                                                      jarvis-hilbert-state
3b65c66bb935   msjarvis-rebuild-jarvis-woah                          "uvicorn woah_servic…"   28 hours ago         Up 28 hours                     7012/tcp                                                                                                       jarvis-woah
ab1e7a71afb1   msjarvis-rebuild-jarvis-aaacpe-scraper                "uvicorn aaacpe_scra…"   29 hours ago         Up 29 hours                     127.0.0.1:8048->8033/tcp                                                                                       jarvis-aaacpe-scraper
a4982178f046   msjarvis-rebuild-jarvis-aaacpe-rag                    "uvicorn aaacpe_rag_…"   29 hours ago         Up 29 hours                     127.0.0.1:8047->8032/tcp                                                                                       jarvis-aaacpe-rag
fd8a1d138e3a   msjarvis-rebuild-jarvis-brain-orchestrator            "python3 services/ma…"   32 hours ago         Up 32 hours (unhealthy)         127.0.0.1:17260->7260/tcp                                                                                      jarvis-brain-orchestrator
ce08b82a37a0   msjarvis-rebuild-jarvis-unified-gateway               "python3 ms_jarvis_u…"   33 hours ago         Up 33 hours                     127.0.0.1:18018->8001/tcp                                                                                      jarvis-unified-gateway
542110c0a9d1   msjarvis-rebuild-jarvis-consciousness-bridge          "python3 services/ms…"   41 hours ago         Up 17 hours                                                                                                                                    jarvis-consciousness-bridge
5e6cdd931abd   redis:7-alpine                                        "docker-entrypoint.s…"   45 hours ago         Up 45 hours                     127.0.0.1:6380->6379/tcp                                                                                       jarvis-redis
255af9b6f5a6   msjarvis-rebuild-jarvis-20llm-production              "python3 ai_server_2…"   45 hours ago         Up 14 minutes                   127.0.0.1:8008->8008/tcp                                                                                       jarvis-20llm-production
5560763f8fcf   msjarvis-rebuild-jarvis-blood-brain-barrier           "python3 ms_jarvis_b…"   45 hours ago         Up 6 hours                      127.0.0.1:8016->8016/tcp                                                                                       jarvis-blood-brain-barrier
966fc10adfb7   python:3.11-slim                                      "sh -c 'pip install …"   45 hours ago         Up 45 hours                     127.0.0.1:8077->8077/tcp                                                                                       jarvis-data-ingest
f032ac069508   msjarvis-rebuild-jarvis-hippocampus                   "uvicorn hippocampus…"   45 hours ago         Up 45 hours                     127.0.0.1:8045->8045/tcp                                                                                       jarvis-hippocampus
b177b2f1d3d2   msjarvis-rebuild-jarvis-local-resources               "uvicorn local_resou…"   46 hours ago         Up 46 hours                     127.0.0.1:8058->8055/tcp                                                                                       jarvis-local-resources
c536f0fd71be   postgis/postgis:15-3.3                                "docker-entrypoint.s…"   47 hours ago         Up 47 hours                     127.0.0.1:5435->5432/tcp                                                                                       jarvis-local-resources-db
e1756749a660   msjarvis-rebuild-jarvis-spiritual-rag                 "python3 jarvis-spir…"   47 hours ago         Up 47 hours                     8005/tcp, 127.0.0.1:8046->8046/tcp                                                                             jarvis-spiritual-rag
c82b9d4c5503   redis:7-alpine                                        "docker-entrypoint.s…"   2 days ago           Up 2 days                       127.0.0.1:16380->6379/tcp                                                                                      jarvis-redis-local
f6e20b8ad945   msjarvis-rebuild-jarvis-llm-judge-v3                  "python judge_pipeli…"   2 days ago           Up 2 days                       127.0.0.1:7240->7240/tcp                                                                                       jarvis-llm-judge-v3
366c4d4e1c95   msjarvis-rebuild-jarvis-fractal-consciousness         "sh -c 'pip install …"   2 days ago           Up 2 days                       8027/tcp                                                                                                       jarvis-fractal-consciousness
7cdc995b109a   msjarvis-rebuild-jarvis-qualia-engine                 "python3 /app/ms_jar…"   2 days ago           Up 2 days                       8017/tcp                                                                                                       jarvis-qualia-engine
e0d3718f0056   msjarvis-rebuild-jarvis-neurobiological-master        "python3 ms_jarvis_n…"   2 days ago           Up 6 hours                      8018/tcp                                                                                                       jarvis-neurobiological-master
40a4745990bc   msjarvis-rebuild-llm7-proxy                           "python -m uvicorn l…"   2 days ago           Up 2 days                       127.0.0.1:8207->8207/tcp                                                                                       llm7-proxy
6d1946a88162   msjarvis-rebuild-llm5-proxy                           "python -m uvicorn l…"   2 days ago           Up 2 days                       127.0.0.1:8205->8205/tcp                                                                                       llm5-proxy
ab7625acb841   msjarvis-rebuild-llm6-proxy                           "python -m uvicorn l…"   2 days ago           Up 2 days                       127.0.0.1:8206->8206/tcp                                                                                       llm6-proxy
1b939e859ba7   msjarvis-rebuild-llm15-proxy                          "python -m uvicorn l…"   2 days ago           Up 2 days                       127.0.0.1:8215->8215/tcp                                                                                       llm15-proxy
4ca62b712813   msjarvis-rebuild-llm2-proxy                           "python -m uvicorn l…"   2 days ago           Up 2 days                       127.0.0.1:8202->8202/tcp                                                                                       llm2-proxy
66301a593a90   msjarvis-rebuild-nbb_darwin_godel_machines            "uvicorn nbb_darwin_…"   2 days ago           Up 2 days                       127.0.0.1:8302->7003/tcp                                                                                       msjarvis-rebuild-nbb_darwin_godel_machines-1
78969ce82df4   msjarvis-rebuild-llm19-proxy                          "python -m uvicorn l…"   2 days ago           Up 2 days                       127.0.0.1:8219->8219/tcp                                                                                       llm19-proxy
b59f34c2a811   msjarvis-rebuild-llm17-proxy                          "python -m uvicorn l…"   2 days ago           Up 2 days                       127.0.0.1:8217->8217/tcp                                                                                       llm17-proxy
9b3609863ab8   msjarvis-rebuild-llm14-proxy                          "python -m uvicorn l…"   2 days ago           Up 2 days                       127.0.0.1:8214->8214/tcp                                                                                       llm14-proxy
79ec87160f06   msjarvis-rebuild-llm9-proxy                           "python -m uvicorn l…"   2 days ago           Up 2 days                       127.0.0.1:8209->8209/tcp                                                                                       llm9-proxy
3a391d3827d4   msjarvis-rebuild-llm16-proxy                          "python -m uvicorn l…"   2 days ago           Up 2 days                       127.0.0.1:8216->8216/tcp                                                                                       llm16-proxy
c07b0d8212cf   msjarvis-rebuild-llm3-proxy                           "python -m uvicorn l…"   2 days ago           Up 2 days                       127.0.0.1:8203->8203/tcp                                                                                       llm3-proxy
8a94bdf9249b   msjarvis-rebuild-llm1-proxy                           "python -m uvicorn l…"   2 days ago           Up 2 days                       127.0.0.1:8201->8201/tcp                                                                                       llm1-proxy
8778fe56ac5c   msjarvis-rebuild-jarvis-fifth-dgm                     "python3 /app/ms_jar…"   2 days ago           Up 2 days                       4002/tcp                                                                                                       jarvis-fifth-dgm
52a034d62fc8   msjarvis-rebuild-llm21-proxy                          "python -m uvicorn l…"   2 days ago           Up 2 days                       127.0.0.1:8221->8221/tcp                                                                                       llm21-proxy
149929b8e9c2   msjarvis-rebuild-llm20-proxy                          "python -m uvicorn l…"   2 days ago           Up 2 days                       127.0.0.1:8220->8220/tcp                                                                                       llm20-proxy
dc4cf0732dae   msjarvis-rebuild-llm11-proxy                          "python -m uvicorn l…"   2 days ago           Up 2 days                       127.0.0.1:8211->8211/tcp                                                                                       llm11-proxy
6f6d5b05caf6   msjarvis-rebuild-jarvis-agents-service                "python3 ms_jarvis_a…"   2 days ago           Up 2 days                       8005/tcp                                                                                                       jarvis-agents-service
a8fd95cf540f   ipfs/kubo:latest                                      "/sbin/tini -- /usr/…"   2 days ago           Up 2 days (healthy)             4001/tcp, 8080-8081/tcp, 4001/udp, 127.0.0.1:5001->5001/tcp                                                    ipfs
dc7d52473f2d   msjarvis-rebuild-llm22-proxy                          "python -m uvicorn l…"   2 days ago           Up 2 days                       127.0.0.1:8222->8222/tcp                                                                                       llm22-proxy
7311ec13e507   msjarvis-rebuild-llm12-proxy                          "python -m uvicorn l…"   2 days ago           Up 2 days                       127.0.0.1:8212->8212/tcp                                                                                       llm12-proxy
dca36eb7290e   msjarvis-rebuild-llm8-proxy                           "python -m uvicorn l…"   2 days ago           Up 2 days                       127.0.0.1:8208->8208/tcp                                                                                       llm8-proxy
3d8bdea1a018   msjarvis-rebuild-llm18-proxy                          "python -m uvicorn l…"   2 days ago           Up 2 days                       127.0.0.1:8218->8218/tcp                                                                                       llm18-proxy
da2b8e9b9486   msjarvis-rebuild-jarvis-autonomous-learner            "uvicorn ms_jarvis_a…"   2 days ago           Up 2 days                       8020/tcp                                                                                                       ab536e7f8e27_jarvis-autonomous-learner
e76f91d80275   msjarvis-rebuild-llm4-proxy                           "python -m uvicorn l…"   2 days ago           Up 2 days                       127.0.0.1:8204->8204/tcp                                                                                       llm4-proxy
1b2e67983209   neo4j:5.13-community                                  "tini -g -- /startup…"   2 days ago           Up 2 days                       7473/tcp, 127.0.0.1:7687->7687/tcp, 127.0.0.1:7475->7474/tcp                                                   neo4j
dd9495ac5962   msjarvis-rebuild-llm10-proxy                          "python -m uvicorn l…"   2 days ago           Up 2 days                       127.0.0.1:8210->8210/tcp                                                                                       llm10-proxy
e4079d80b9c3   mysql:8.2                                             "docker-entrypoint.s…"   2 days ago           Up 2 days                       33060/tcp, 127.0.0.1:3307->3306/tcp                                                                            mysql
36a582a9327f   msjarvis-rebuild-jarvis-web-research                  "python ms_jarvis_we…"   2 days ago           Up 2 days                       8008/tcp                                                                                                       jarvis-web-research
7f25779766f6   msjarvis-rebuild-nbb_pituitary_gland                  "uvicorn pituitary_g…"   2 days ago           Up 6 hours                      127.0.0.1:8108->7008/tcp                                                                                       msjarvis-rebuild-nbb_pituitary_gland-1
282867d66a03   msjarvis-rebuild-jarvis-69dgm-bridge                  "python3 port_9000_6…"   2 days ago           Up 2 days                       9000/tcp                                                                                                       jarvis-69dgm-bridge
01908c423693   msjarvis-rebuild-jarvis-temporal-consciousness        "python -m uvicorn t…"   2 days ago           Up 2 days                       7007/tcp                                                                                                       jarvis-temporal-consciousness
697587e2b9ad   msjarvis-rebuild-jarvis-lm-synthesizer                "python lm_synthesiz…"   2 days ago           Up 2 days                       8001/tcp                                                                                                       jarvis-lm-synthesizer
fe2057569d92   msjarvis-rebuild-jarvis-swarm-intelligence            "python3 ms_jarvis_s…"   2 days ago           Up 2 days                       8021/tcp                                                                                                       jarvis-swarm-intelligence
d4937da44329   msjarvis-rebuild-nbb_qualia_engine                    "uvicorn qualia_engi…"   6 days ago           Up 2 days                       127.0.0.1:8303->7008/tcp                                                                                       msjarvis-rebuild-nbb_qualia_engine-1
8254b8e1b476   alpine:3.18                                           "sh -c 'echo 'nbb_wo…"   6 days ago           Up 40 minutes                                                                                                                                  nbb_woah_algorithms
59438e1d5868   msjarvis-rebuild-nbb_subconscious                     "uvicorn consciousne…"   6 days ago           Up 2 days                       127.0.0.1:8112->7011/tcp                                                                                       msjarvis-rebuild-nbb_subconscious-1
aa64d696e557   msjarvis-rebuild-nbb_prefrontal_cortex                "/start.sh"              6 days ago           Up 2 days                       127.0.0.1:8105->7005/tcp                                                                                       msjarvis-rebuild-nbb_prefrontal_cortex-1
0a7ac1b1617e   msjarvis-rebuild-nbb_mother_carrie_protocols          "uvicorn main:app --…"   6 days ago           Up 2 days                       127.0.0.1:8107->7007/tcp                                                                                       msjarvis-rebuild-nbb_mother_carrie_protocols-1
066c7920ee64   msjarvis-rebuild-nbb_spiritual_root                   "uvicorn spiritual_r…"   6 days ago           Up 2 days                       127.0.0.1:8103->7003/tcp                                                                                       msjarvis-rebuild-nbb_spiritual_root-1
062fb67a82f4   msjarvis-rebuild-jarvis-mother-protocols              "python -m uvicorn m…"   6 days ago           Up 2 days                       4000/tcp                                                                                                       jarvis-mother-protocols
9576658f69a7   msjarvis-rebuild-nbb_blood_brain_barrier              "uvicorn blood_brain…"   6 days ago           Up 2 days                       127.0.0.1:8301->7001/tcp                                                                                       msjarvis-rebuild-nbb_blood_brain_barrier-1
f12397aedddb   msjarvis-rebuild-nbb_i_containers                     "uvicorn i_container…"   6 days ago           Up 2 days                       127.0.0.1:8101->7005/tcp                                                                                       msjarvis-rebuild-nbb_i_containers-1
b69b5f51ce3a   msjarvis-rebuild-nbb_heteroglobulin_transport         "uvicorn heteroglobu…"   6 days ago           Up 2 days                       127.0.0.1:8106->7006/tcp                                                                                       msjarvis-rebuild-nbb_heteroglobulin_transport-1
5f7ac820970d   msjarvis-rebuild-nbb_spiritual_maternal_integration   "uvicorn spiritual_m…"   6 days ago           Up 2 days                       127.0.0.1:8109->7009/tcp                                                                                       msjarvis-rebuild-nbb_spiritual_maternal_integration-1
5d7927d91519   msjarvis-rebuild-nbb_consciousness_containers         "uvicorn consciousne…"   6 days ago           Up 2 days                       127.0.0.1:8102->7002/tcp                                                                                       msjarvis-rebuild-nbb_consciousness_containers-1
7cd232c9a08a   postgis/postgis:16-3.4                                "docker-entrypoint.s…"   8 days ago           Up 2 days                       5432/tcp                                                                                                       postgis-forensic
6d09f3247e66   postgres:16-alpine                                    "docker-entrypoint.s…"   10 days ago          Up 2 days                       127.0.0.1:5433->5432/tcp                                                                                       msjarvis-pgdata-rescue
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild/msjarvis-rebuild$ 

