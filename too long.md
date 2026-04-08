
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ cd ~/msjarvis-rebuild-working/msjarvis-rebuild || exit 1

grep -Rni "FastAPI" services | grep -i memory
grep -Rni "jarvis-memory" services
grep -Rni "ms-jarvis-memory" services
ls -1 services | grep -i memory
grep: services/__pycache__/main_brain.cpython-312.pyc: binary file matches
grep: services/__pycache__/dao_governance.cpython-310.pyc: binary file matches
grep: services/__pycache__/jarvis_eeg_beta_5m.cpython-312.pyc: binary file matches
grep: services/__pycache__/main_brain.cpython-310.pyc: binary file matches
grep: services/__pycache__/commons_gamification.cpython-310.pyc: binary file matches
grep: services/__pycache__/jarvis_pia_status.cpython-312.pyc: binary file matches
grep: services/__pycache__/dao_governance.cpython-312.pyc: binary file matches
grep: services/__pycache__/gbim_benefit_indexer.cpython-311.pyc: binary file matches
grep: services/__pycache__/jarvis_eeg_theta_60s.cpython-312.pyc: binary file matches
grep: services/__pycache__/gbim_query_router.cpython-311.pyc: binary file matches
grep: services/__pycache__/jarvis_eeg_delta_30s.cpython-312.pyc: binary file matches
grep: services/__pycache__/community_stake_registry.cpython-310.pyc: binary file matches
grep: services/__pycache__/dgm_adoption_worker.cpython-312.pyc: binary file matches
grep: services/__pycache__/jarvis-semaphore_msjarvis_semaphore.cpython-311.pyc: binary file matches
services/Dockerfile.memory:3:RUN pip install --no-cache-dir fastapi uvicorn httpx psycopg2-binary asyncpg pydantic redis
services/ms_jarvis_memory.py:6:from fastapi import FastAPI, HTTPException, Header
services/ms_jarvis_memory.py:7:from fastapi.responses import JSONResponse
services/ms_jarvis_memory.py:12:app = FastAPI(title="Ms. Jarvis Memory Service", version="2.0.0")
grep: services/session_sidecar/__pycache__/app.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/industrialbuildings_wvdo_200807_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/geographicalnamesonusgstopomaps_usgs_200601_ll27_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/blockgroups_census_2020_wma84_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/cvpoly_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/indexgrid15minutequads_wvgistc_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/railnetworkwv_usdot_200203_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/mineraloperations_usgs_200204_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/towersprivate_fcc_200202_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/citieswithpopulationover10k_uscensus_1990_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/citieswithpopulation_2500_census_201111_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/metfacp_reg_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/wvgistcbuildingfootprints_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/bridges_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/inedexgrid1minutequads_wvgistc_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/towers_wvpublicbroadcasting_2002_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/hospitals_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/policedept_wvdem_012319_gcs84_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/wv_tax_districts_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/mineraloperations_usgs_200204_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/fault_reg_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/coals2_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/towersasr_fcc_200202_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/placesofworship_hsip_20080723_wgs84_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/regionalplanninganddevelopmentcouncil_wvdo_1971_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/coals2_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/cvfault_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/amtrackrails_federalrailroadadministration_200210_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/veteransaffairsfacilities_manysources_200503_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/realtimestreamflowstations_usgs_200012_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/citieswithpopulationover2500_uscensus_1990_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/blockgroups_census_201111_gcs83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/blocks_census_2020_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/publichealthdepts_hsip_20091229_gcs83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/metropolitanstatisticalareas_uscensus_199901_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/votingdistrictswv_legislativeservices_2002_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/wvstatesenatedistricts_manysources_2002_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/paroleoffices_manysources_2008_wgs84_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/cvpoly_utm27_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/recreationalwwtrails_ofwv_20151117_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/geolgyp_reg_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/workforceinvestmentareas_wvgistc_200208_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/nationalwaterwaynetworkports_usarmycorpsofengineers_2001_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/towersam_fcc_200202_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/glacal_reg_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/springs_wvges_1986_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/wvstatesenatedistricts_manysources_1992_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/nationalatlasstreams_usgs_199903_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/towerspager_fcc_200202_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/surveycontrol_nationalgeodeticsurvey_102011_gcs83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/cvfault_utm27_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/excursionpassengertrains_wvdof_200102_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/wvstatesenatedistricts_manysources_2002_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/citieswithpopulationsover2500_census_2020_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/wvstatehousedistricts_manysources_2002_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/towerspager_fcc_200202_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/blockgroups_census_2020_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/glacagl_reg_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/majorriversandlakesline_nhd_2002_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/communityboundary_min_att_20250121_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/publichealthdepts_hsip_20091229_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/correctionalinstitutions_hsip_20091230_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/manufacturingandbusiness_wvdo_200803_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/solidwastefacilities_wvdep_200202_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/states_region_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/windenergyresource_nationalrenewableenergylab_200901_wgs84_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/votingdistrictswv_uscensus_2000_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/railroads_rahalltransportationinstitute_2005_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/navigablewaterwaysrivermiles_usarmycropsofengineers_2006_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/citieswithpopulatoinover2500_uscensus_1990_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/wvstatehousedistricts_manysources_1992_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/nationalwaterwaynetworkports_usarmycorpsofengineers_2001_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/towerscellular_fcc_200202_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/blocks_census_2020_utm83_full_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/libraries_manysources_2001_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/geographicnamesonusgstopomaps_current_usgs_20110801_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/blockgroups_census_2020_utm83_full_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/citieswithpopulationsover10k_census_2020_wma84_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/geographicnamesonusgstopomaps_usgs_20110801_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/wvstateboundary24k_usgs_200203_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/pow_wvgistc_062919_wgs84_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/pow_wvgistc_062919_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/blockgroups_census_201111_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/wvstatebounadary100k_usgs_200203_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/citieswithpopulationover10k_uscensus_1990_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/towerscellular_fcc_200202_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/industrialparks_wvdo_200078_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/wvstatesenatedistricts_manysources_1992_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/towersfm_fcc_200202_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/wvstateboundary24k_usgs_200203_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/911centers_wvdem_032819_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/metropolitanandmicropolitanstatisticalareas_census_2020_wma84_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/structurepolygons_samb_2003_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/empowermentzonesandenterprisecommunitiesbytractuscens30c72907_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/citieswithpopulationover10k_census_201111_gcs83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/nationalregister_point_20200923_utm27_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/countycityparkboundaries_20201104_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/intermodalterminalfacilities_usdot_1997_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/paroleoffices_manysources_2008_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/realtimestreamflowstations_usgs_200012_ll27_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/summits_gistc_052012_utm83_shp_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/facilities_epa_200203_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/wvstateboundary100k_usgs_200203_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/towersasr_fcc_200202_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/populatedplaces_census_2020_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/amtrackrails_federalrailroadadministration_200210_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/nursinghomes_wvdem_041219_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/nationalwaterwaynetwork_usarmycorpsofengineers_2001_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/zipcodetabulationarea_census_2020_wma84_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/metropolitanandmicropolitanstatisticalareascensus201111gcs83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/majorriversandlakespolygon_nhd_2002_poly_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/majorriversandlakespolygon_nhd_2002_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/metropolitanandmicropolitanstatisticalareascensus201111utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/nationalwaterwaynetwork_usarmycorpsofengineers_2001_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/realtimestreamflowstations_usgs_200012_utm27_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/populatedplaces_census_201112_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/fire_dept_wvdem_092017_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/highered_wvemd_072420_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/impact_reg_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/naviagablewaterways_usarmycropsofengineers_2006_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/populatedplaces_census_20112_gcs83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/fire_departments_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/stateofwvhousedistricts_wvlegislativeservices_2010_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/libraries_manysources_2001_ll27_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/populatedplaces_uscensus_1990_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/citieswithpopulation_2500_census_201111_gcs83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/wv_microsoft_20180207_utm17n83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/communityboundary_min_att_20250121_wma84_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/coals2_utm27_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/indexgrid1minutequads_wvgistc_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/correctionalinstitutions_hsip_20091230_wgs84_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/wvstatehousedistricts_manysources_2002_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/geolgyl_reg_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/structurepointsnorth_samb_2003_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/railnetworkregion_usdot_200203_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/911centers_wvdem_032819_gcs84_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/highered_wvemd_072420_wgc84_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/populatedplaces_census_2020_wma84_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/towersprivate_fcc_200202_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/summits_gistc_052012_wgs84_shp_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/hospitals_wvdem_040519_gcs84_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/votingdistrictswv_legislativeservices_2002_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/communityhealthproviders_wvhealthcareauthority_200802_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/cvpoly_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/countyseats_usgs_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/structurepointssouth_samb_2003_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/excursionpassengertrains_wvdof_200102_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/cvfault_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/veteransaffairsfacilities_manysources_200503_wgs84_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/empowermentzonesandenterprisecommunities_uscensus_2002_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/boundaryappalachianbasin_wvges_1996_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/indexgrid15minutequads_wvgistc_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/railnetworkregion_usdot_200203_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/stateofwvsenatedistricts_wvlegislativeservices_2010_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/blocks_census_2020_wma84_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/navigablewaterwaysstructures_usarmycorpsofengineers_2006_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/geographicnamesonusgstopomaps_historical_usgs_20110801_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/officebuildings_wvdo_200807_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/geographicalnamesonusgstopomaps_usgs_200601_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/metropolitanandmicropolitanstatisticalareas_census_2020_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/intermodalterminalfacilities_usdot_1997_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/metropolitanstatisticalareas_uscensus_199901_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/hazardmitigationbuyout_20250929_polygons_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/majorriversandlakesline_nhd_2002_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/placesofworship_hsip_20080723_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/nursinghomes_wvdem_041219_gcs84_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/springs_wvges_1986_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/wvstatehousedistricts_manysources_1992_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/weatherstations_nationalclimatedatacenter_1999_gcs83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/towersmicrowave_fcc_200202_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/hazardmitigationbuyout_20250929_polygons_wma84_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/towers_wvpublicbroadcasting_2002_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/countyseats_usgs_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/solidwastefacilities_wvdep_200202_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/hospitals_wvdem_040519_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/policedept_wvdem_012319_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/geotextl_reg_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/citieswithpopulationsover2500_census_2020_wma84_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/dams_usarmycorpsofengineers_200010_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/weatherstations_nationalclimatedatacenter_1999_utm27_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/wv_tax_districts_wma84_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/courthousescounty_manysources_200203_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/historicalaerialphotographycountycoverage_wvgistc_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/healthruralfacilities_manysources_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/damsnoncoal_usgs_2002_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/citieswithpopulationsover10k_census_2020_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/sewertreatmentplants_wvdep_200203_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/blockgroups_census_2000_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/faultgl_reg_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/timberremovalvolume_usfs_1996_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/industrialsites_wvdo_200807_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/nationalatlasstreams_usgs_199903_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/windenergyresource_nationalrenewableenergylab_200901_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/regionalplanninganddevelopmentcouncil_wvdo_1971_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/calderl_reg_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/facilities_epa_200203_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/dams_usarmycropsofengineers_200010_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/populatedplaces_uscensus_1990_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/towersmicrowave_fcc_200202_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/railnetworkwv_usdot_200203_utm83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/blockgroups_census_2000_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/indexgrid15minutewithcounties_wvgistc_utm27_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/populationdatablockgroups_uscensus_2000_ll83_service.cpython-312.pyc: binary file matches
grep: services/gis_dataset_services/__pycache__/populationdatablockgroups_uscensus_2000_utm83_service.cpython-312.pyc: binary file matches
grep: services/neurobiological_brain/blood_brain_barrier/__pycache__/spiritual_filter.cpython-312.pyc: binary file matches
services/ms_jarvis_unified_gateway.py:638:    target = f"http://jarvis-memory:8056/memory/{path}"
services/ms_jarvis_unified_gateway.py:1119:            _hx.post('http://jarvis-memory:8056/memory/turn',
services/constitutional_principles.json:224:    "admin": "ADMINISTRATIVE — logged, gate decisions durable at jarvis-memory:8056",
services/constitutional_principles.json:225:    "carrie_admin": "ADMINISTRATIVE — logged, gate decisions durable at jarvis-memory:8056",
services/constitutional_principles.json:226:    "system": "LOGGED — generally allowed, gate decisions durable at jarvis-memory:8056"
services/ms_jarvis_unified_gateway.py.checkpoint.20260329_214153:535:    target = f"http://jarvis-memory:8056/memory/{path}"
grep: services/__pycache__/jarvis_pia_status.cpython-312.pyc: binary file matches
services/ms_jarvis_unified_gateway.py.checkpoint.20260329_213555:535:    target = f"http://jarvis-memory:8056/memory/{path}"
services/main_brain.py.bak.1774448411:1317:    # Item 6 — Store turn in jarvis-memory (Redis conversation store)
services/main_brain.py.bak.1774448411:1323:                "http://jarvis-memory:8056/memory/turn",
services/ms_jarvis_unified_gateway.py.checkpoint.20260329_212043:535:    target = f"http://jarvis-memory:8056/memory/{path}"
services/jarvis-woah_dgm_supervisor_woah_fixed.py:112:        ("memory",                  "jarvis-memory",                     8056, ["memory","storage"]),
services/jarvis_pia_status.py:10:JARVIS_MEMORY_URL = os.getenv("JARVIS_MEMORY_URL", "http://jarvis-memory:8056")
services/jarvis_pia_status.py:38:    """Query jarvis-memory for recent PIA-relevant events in the last window_minutes.
services/jarvis_pia_status.py:40:    Expected jarvis-memory endpoint:
services/ms_jarvis_memory.py:63:        return {"status": "healthy", "service": "ms-jarvis-memory", "redis": "connected"}
services/ms_jarvis_blood_brain_barrier.py:31:    """Ch32 — durable BBB gate audit to jarvis-memory:8056."""
services/ms_jarvis_blood_brain_barrier.py:37:                "http://jarvis-memory:8056/memory/turn",
services/woah_service.py:112:        ("memory",                  "jarvis-memory",                     8056, ["memory","storage"]),
services/main_brain_LEGACY_32svc.py:1345:    # Item 6 — Store turn in jarvis-memory (Redis conversation store)
services/main_brain_LEGACY_32svc.py:1350:                "http://jarvis-memory:8056/memory/turn",
services/ms_jarvis_unified_gateway.py.checkpoint.20260329_211609:535:    target = f"http://jarvis-memory:8056/memory/{path}"
services/ms_jarvis_memory.py:63:        return {"status": "healthy", "service": "ms-jarvis-memory", "redis": "connected"}
Dockerfile.memory
ms_jarvis_memory.py
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ sed -n '1,260p' services/ms_jarvis_memory.py
"""
Ms. Jarvis Conversation Memory Service
Sprint 2 item 5 (turns) + Sprint 4 A-10/A-18 (quest context)
Port: 8056
"""
from fastapi import FastAPI, HTTPException, Header
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
import redis, os, json, time, uuid

app = FastAPI(title="Ms. Jarvis Memory Service", version="2.0.0")

REDIS_HOST  = os.getenv("REDIS_HOST", "jarvis-redis")
REDIS_PORT  = int(os.getenv("REDIS_PORT", 6379))
MAX_TURNS   = int(os.getenv("MAX_TURNS", 50))
TTL_SECONDS = int(os.getenv("CONV_TTL", 86400 * 7))
QUEST_TTL   = int(os.getenv("QUEST_TTL", 86400 * 30))  # 30 days

def get_redis():
    return redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def _auth(x_api_key: str = "", authorization: str = "") -> str:
    token = x_api_key or (authorization[7:] if authorization.lower().startswith("bearer ") else "")
    if not token:
        raise HTTPException(status_code=401, detail="Authentication required")
    internal_key = os.getenv("JARVIS_API_KEY", "")
    if token == "internal" or (internal_key and token == internal_key):
        return "internal"
    r = get_redis()
    td = r.hgetall(f"redteam:token:{token}")
    if td and td.get("active") == "true":
        return td.get("userid", "unknown")
    raise HTTPException(status_code=401, detail="Invalid or expired token")

# ── Models ────────────────────────────────────────────────────────────────────

class TurnIn(BaseModel):
    session_id: Optional[str] = None
    user_message: str
    assistant_response: str
    quest_id: Optional[str] = None       # A-18 — link turn to active quest
    metadata: Optional[dict] = {}

class SessionQuery(BaseModel):
    session_id: str
    limit: Optional[int] = 20

class QuestStateIn(BaseModel):           # A-18 quest state storage
    quest_id: str
    user_id: str
    quest_type: str                      # e.g. "onboarding", "benefits_lookup", "proposal"
    status: str = "active"               # active | completed | abandoned
    step: int = 0
    context: dict = {}

# ── Routes ────────────────────────────────────────────────────────────────────

@app.get("/health")
def health():
    try:
        get_redis().ping()
        return {"status": "healthy", "service": "ms-jarvis-memory", "redis": "connected"}
    except Exception as e:
        return JSONResponse({"status": "degraded", "redis": str(e)}, status_code=503)

@app.post("/memory/turn")
def store_turn(
    body: TurnIn,
    x_api_key: str = Header(""),
    authorization: str = Header("")
):
    userid = _auth(x_api_key, authorization)
    session_id = body.session_id or str(uuid.uuid4())
    r = get_redis()

    turn = {
        "turn_id":   str(uuid.uuid4()),
        "timestamp": time.time(),
        "user":      body.user_message,
        "assistant": body.assistant_response,
        "quest_id":  body.quest_id,
        "metadata":  json.dumps(body.metadata or {})
    }

    key = f"conv:{userid}:{session_id}"
    pipe = r.pipeline()
    pipe.rpush(key, json.dumps(turn))
    pipe.ltrim(key, -MAX_TURNS, -1)
    pipe.expire(key, TTL_SECONDS)
    pipe.execute()

    r.sadd(f"conv:sessions:{userid}", session_id)
    r.expire(f"conv:sessions:{userid}", TTL_SECONDS)

    # if turn is part of a quest, index it
    if body.quest_id:
        r.sadd(f"quest:turns:{body.quest_id}", turn["turn_id"])
        r.expire(f"quest:turns:{body.quest_id}", QUEST_TTL)

    return {"stored": True, "session_id": session_id, "userid": userid}

@app.post("/memory/get")
def get_history(
    body: SessionQuery,
    x_api_key: str = Header(""),
    authorization: str = Header("")
):
    userid = _auth(x_api_key, authorization)
    r = get_redis()
    raw = r.lrange(f"conv:{userid}:{body.session_id}", -body.limit, -1)
    turns = [json.loads(t) for t in raw]
    return {"session_id": body.session_id, "userid": userid, "turns": turns, "count": len(turns)}

@app.get("/memory/sessions")
def list_sessions(
    x_api_key: str = Header(""),
    authorization: str = Header("")
):
    userid = _auth(x_api_key, authorization)
    sessions = list(get_redis().smembers(f"conv:sessions:{userid}"))
    return {"userid": userid, "sessions": sessions, "count": len(sessions)}

@app.delete("/memory/session/{session_id}")
def delete_session(
    session_id: str,
    x_api_key: str = Header(""),
    authorization: str = Header("")
):
    userid = _auth(x_api_key, authorization)
    r = get_redis()
    r.delete(f"conv:{userid}:{session_id}")
    r.srem(f"conv:sessions:{userid}", session_id)
    return {"deleted": True, "session_id": session_id}

# ── Quest state (A-18) ────────────────────────────────────────────────────────

@app.post("/memory/quest")
def store_quest(
    body: QuestStateIn,
    x_api_key: str = Header(""),
    authorization: str = Header("")
):
    """Store or update quest state for a user."""
    _auth(x_api_key, authorization)
    r = get_redis()
    payload = {
        "quest_id":   body.quest_id,
        "user_id":    body.user_id,
        "quest_type": body.quest_type,
        "status":     body.status,
        "step":       body.step,
        "context":    json.dumps(body.context),
        "updated_at": time.time(),
    }
    key = f"quest:state:{body.user_id}:{body.quest_id}"
    r.hset(key, mapping=payload)
    r.expire(key, QUEST_TTL)
    r.sadd(f"quest:index:{body.user_id}", body.quest_id)
    r.expire(f"quest:index:{body.user_id}", QUEST_TTL)
    return {"stored": True, "quest_id": body.quest_id}

@app.get("/memory/quest/{user_id}/{quest_id}")
def get_quest(
    user_id: str,
    quest_id: str,
    x_api_key: str = Header(""),
    authorization: str = Header("")
):
    """Retrieve quest state."""
    _auth(x_api_key, authorization)
    r = get_redis()
    data = r.hgetall(f"quest:state:{user_id}:{quest_id}")
    if not data:
        raise HTTPException(status_code=404, detail="Quest not found")
    data["context"] = json.loads(data.get("context", "{}"))
    return data

@app.get("/memory/quests/{user_id}")
def list_quests(
    user_id: str,
    x_api_key: str = Header(""),
    authorization: str = Header("")
):
    """List all quest IDs for a user."""
    _auth(x_api_key, authorization)
    r = get_redis()
    quest_ids = list(r.smembers(f"quest:index:{user_id}"))
    return {"user_id": user_id, "quest_ids": quest_ids, "count": len(quest_ids)}

# ── A-10: Per-user episodic memory consolidation ──────────────────────────────

class ConsolidateIn(BaseModel):
    user_id: str
    max_sessions: int = 10        # sessions to consolidate across
    turns_per_session: int = 5    # most recent turns per session to include

@app.post("/memory/consolidate/{user_id}")
def consolidate_episodic(
    user_id: str,
    body: ConsolidateIn = ConsolidateIn(user_id="default"),
    x_api_key: str = Header(""),
    authorization: str = Header("")
):
    """
    A-10: Episodic memory consolidation.
    Pulls recent turns across all sessions for a user,
    produces a structured episodic summary stored in Redis.
    """
    _auth(x_api_key, authorization)
    r = get_redis()

    session_ids = list(r.smembers(f"conv:sessions:{user_id}"))[:body.max_sessions]
    if not session_ids:
        return {"status": "no_sessions", "user_id": user_id, "episodes": []}

    episodes = []
    for sid in session_ids:
        raw = r.lrange(f"conv:{user_id}:{sid}", -body.turns_per_session, -1)
        turns = [json.loads(t) for t in raw]
        if not turns:
            continue
        # Build a compact episodic summary per session
        episode = {
            "session_id": sid,
            "turn_count": len(turns),
            "first_ts": turns[0].get("timestamp"),
            "last_ts": turns[-1].get("timestamp"),
            "topics": list({t.get("metadata", {}) and
                           json.loads(t["metadata"]).get("topic", "general")
                           if isinstance(t.get("metadata"), str)
                           else t.get("metadata", {}).get("topic", "general")
                           for t in turns}),
            "sample_exchange": {
                "user": turns[-1].get("user", "")[:120],
                "assistant": turns[-1].get("assistant", "")[:200],
            },
            "quest_ids": list({t.get("quest_id") for t in turns if t.get("quest_id")}),
        }
        episodes.append(episode)

    # Store consolidated episodic memory
    consolidated = {
        "user_id": user_id,
        "consolidated_at": time.time(),
        "session_count": len(episodes),
        "episodes": json.dumps(episodes),
    }
    r.hset(f"episodic:{user_id}", mapping=consolidated)
    r.expire(f"episodic:{user_id}", TTL_SECONDS)

    return {
        "status": "consolidated",
        "user_id": user_id,
        "session_count": len(episodes),
        "episodes": episodes,
    }

@app.get("/memory/episodic/{user_id}")
def get_episodic(
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ 

