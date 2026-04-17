crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ # Full database inventory
docker exec postgis-forensic psql -U msjarvis -d msjarvis -c "\l"

# See what's actually in there
docker exec postgis-forensic psql -U msjarvis -d msjarvis -c "\dt"
                                                       List of databases
       Name       | Owner  | Encoding | Locale Provider |  Collate   |   Ctype    | ICU Locale | ICU Rules | Access privileges 
------------------+--------+----------+-----------------+------------+------------+------------+-----------+-------------------
 msjarvis         | jarvis | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 msjarvisgis      | jarvis | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 postgres         | jarvis | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 template0        | jarvis | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | =c/jarvis        +
                  |        |          |                 |            |            |            |           | jarvis=CTc/jarvis
 template1        | jarvis | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | =c/jarvis        +
                  |        |          |                 |            |            |            |           | jarvis=CTc/jarvis
 template_postgis | jarvis | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
(6 rows)

              List of relations
  Schema  |      Name       | Type  | Owner  
----------+-----------------+-------+--------
 public   | spatial_ref_sys | table | jarvis
 public   | wv_locations    | table | jarvis
 topology | layer           | table | jarvis
 topology | topology        | table | jarvis
(4 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ docker compose -f ~/msjarvis-rebuild-working/msjarvis-rebuild/msjarvis-rebuild/docker-compose.yml <command>
bash: syntax error near unexpected token `newline'
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ # See full schema of postgis-forensic msjarvisgis
docker exec postgis-forensic psql -U msjarvis -d msjarvisgis -c "\dt"

# See what wv_locations contains
docker exec postgis-forensic psql -U msjarvis -d msjarvisgis -c "\d wv_locations"

# See the msjarvis database tables (core state)
docker exec postgis-forensic psql -U msjarvis -d msjarvis -c "\dt"
                                     List of relations
 Schema |                              Name                               | Type  | Owner  
--------+-----------------------------------------------------------------+-------+--------
 public | 911centers_wvdem_032819_gcs84_attrs_raw                         | table | jarvis
 public | 911centers_wvdem_032819_utm83_attrs_raw                         | table | jarvis
 public | amtrackrails_federalrailroadadministration_200210_ll83_attrs_ra | table | jarvis
 public | amtrackrails_federalrailroadadministration_200210_utm83_attrs_r | table | jarvis
 public | amtrackrails_fra_200210_ll83_attrs_raw                          | table | jarvis
 public | amtrackrails_fra_200210_utm83_attrs_raw                         | table | jarvis
 public | attrs_files_list                                                | table | jarvis
 public | attrs_inventory_detailed                                        | table | jarvis
 public | authority_references                                            | table | jarvis
 public | benefit_case                                                    | table | jarvis
 public | blockgroups_census_2000_ll83_attrs_raw                          | table | jarvis
 public | blockgroups_census_2000_utm83_attrs_raw                         | table | jarvis
 public | blockgroups_census_201111_gcs83_attrs_raw                       | table | jarvis
 public | blockgroups_census_201111_utm83_attrs_raw                       | table | jarvis
 public | blockgroups_census_2020_utm83_attrs_raw                         | table | jarvis
 public | blockgroups_census_2020_wma84_attrs_raw                         | table | jarvis
 public | blocks_census_2020_utm83_attrs_raw                              | table | jarvis
 public | blocks_census_2020_wma84_attrs_raw                              | table | jarvis
 public | boundaryappalachianbasin_wvges_1996_utm83_attrs_raw             | table | jarvis
 public | bridges_attrs_raw                                               | table | jarvis
 public | building_metric_stage                                           | table | jarvis
 public | calderl_reg_ll83_attrs_raw                                      | table | jarvis
 public | citieswithpopulation_2500_census_201111_gcs83_attrs_raw         | table | jarvis
 public | citieswithpopulation_2500_census_201111_utm83_attrs_raw         | table | jarvis
 public | citieswithpopulationover10k_census_201111_gcs83_attrs_raw       | table | jarvis
 public | citieswithpopulationover10k_uscensus_1990_ll83_attrs_raw        | table | jarvis
 public | citieswithpopulationover10k_uscensus_1990_utm83_attrs_raw       | table | jarvis
 public | citieswithpopulationover2500_uscensus_1990_ll83_attrs_raw       | table | jarvis
 public | citieswithpopulationsover10k_census_2020_utm83_attrs_raw        | table | jarvis
 public | citieswithpopulationsover10k_census_2020_wma84_attrs_raw        | table | jarvis
 public | citieswithpopulationsover2500_census_2020_utm83_attrs_raw       | table | jarvis
 public | citieswithpopulationsover2500_census_2020_wma84_attrs_raw       | table | jarvis
 public | citieswithpopulatoinover2500_uscensus_1990_utm83_attrs_raw      | table | jarvis
 public | client_utility_account                                          | table | jarvis
 public | coals2_ll83_attrs_raw                                           | table | jarvis
 public | coals2_utm27_attrs_raw                                          | table | jarvis
 public | coals2_utm83_attrs_raw                                          | table | jarvis
 public | communityboundary_min_att_20250121_utm83_attrs_raw              | table | jarvis
 public | communityboundary_min_att_20250121_wma84_attrs_raw              | table | jarvis
 public | communityhealthproviders_wvhealthcareauthority_200802_u_attrs_r | table | jarvis
 public | communityhealthproviders_wvhealthcareauthority_200802_utm83_att | table | jarvis
 public | correctionalinstitutions_hsip_20091230_utm83_attrs_raw          | table | jarvis
 public | correctionalinstitutions_hsip_20091230_wgs84_attrs_raw          | table | jarvis
 public | countycityparkboundaries_20201104_utm83_attrs_raw               | table | jarvis
 public | countyseats_usgs_ll83_attrs_raw                                 | table | jarvis
 public | countyseats_usgs_utm83_attrs_raw                                | table | jarvis
 public | courthousescounty_manysources_200203_ll83_attrs_raw             | table | jarvis
 public | courthousescounty_manysources_200203_utm83_attrs_raw            | table | jarvis
 public | courthousesfederal_manysources_200203_ll83_attrs_raw            | table | jarvis
 public | courthousesfederal_manysources_200203_utm_attrs_raw             | table | jarvis
 public | cvfault_ll83_attrs_raw                                          | table | jarvis
 public | cvfault_utm27_attrs_raw                                         | table | jarvis
 public | cvfault_utm83_attrs_raw                                         | table | jarvis
 public | cvpoly_ll83_attrs_raw                                           | table | jarvis
 public | cvpoly_utm27_attrs_raw                                          | table | jarvis
 public | cvpoly_utm83_attrs_raw                                          | table | jarvis
 public | dams_usarmycorpsofengineers_200010_utm83_attrs_raw              | table | jarvis
 public | dams_usarmycropsofengineers_200010_ll83_attrs_raw               | table | jarvis
 public | damsnoncoal_usgs_2002_ll27_attrs_raw                            | table | jarvis
 public | damsnoncoal_usgs_2002_utm83_attrs_raw                           | table | jarvis
 public | empowermentzonesandenterprisecommunities_uscensus_2002__attrs_r | table | jarvis
 public | empowermentzonesandenterprisecommunities_uscensus_2002_utm83_at | table | jarvis
 public | empowermentzonesandenterprisecommunitiesbytract_uscens__attrs_r | table | jarvis
 public | empowermentzonesandenterprisecommunitiesbytractuscens30c72907at | table | jarvis
 public | evidence_documents                                              | table | jarvis
 public | excursionpassengertrains_wvdof_200102_ll83_attrs_raw            | table | jarvis
 public | excursionpassengertrains_wvdof_200102_utm83_attrs_raw           | table | jarvis
 public | facilities_epa_200203_ll83_attrs_raw                            | table | jarvis
 public | facilities_epa_200203_utm83_attrs_raw                           | table | jarvis
 public | fault_reg_ll83_attrs_raw                                        | table | jarvis
 public | faultgl_reg_ll83_attrs_raw                                      | table | jarvis
 public | features_attrs_raw                                              | table | jarvis
 public | fire_departments_attrs_raw                                      | table | jarvis
 public | fire_dept_wvdem_092017_utm83_attrs_raw                          | table | jarvis
 public | floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83_ | table | jarvis
 public | floodplainstructuresatrisk_usarmycorpsofengineers_20030_attrs_r | table | jarvis
 public | gbim_belief                                                     | table | jarvis
 public | gbim_belief_edges                                               | table | jarvis
 public | gbim_belief_evidence                                            | table | jarvis
 public | gbim_beliefs                                                    | table | jarvis
 public | gbim_entity_clusters                                            | table | jarvis
 public | gbim_entity_land_candidates                                     | table | jarvis
 public | gbim_evidence                                                   | table | jarvis
 public | gbim_full_points_raw                                            | table | jarvis
 public | gbim_layer_catalog                                              | table | jarvis
 public | gbim_layer_config                                               | table | jarvis
 public | gbim_layer_manifest                                             | table | jarvis
 public | gbim_source_epochs                                              | table | jarvis
 public | gbim_source_tables_used                                         | table | jarvis
 public | gbim_worldview_entity_backup_small                              | table | jarvis
 public | gbim_worldviews                                                 | table | jarvis
 public | gbimbeliefnormalized                                            | table | jarvis
 public | geographicalnamesonusgstopomaps_usgs_200601_ll27_attrs_raw      | table | jarvis
 public | geographicalnamesonusgstopomaps_usgs_200601_utm83_attrs_raw     | table | jarvis
 public | geographicnamesonusgstopomaps_current_usgs_20110801_ll83_attrs_ | table | jarvis
 public | geographicnamesonusgstopomaps_current_usgs_20110801_ll8_attrs_r | table | jarvis
 public | geographicnamesonusgstopomaps_current_usgs_20110801_utm83_attrs | table | jarvis
 public | geographicnamesonusgstopomaps_current_usgs_20110801_utm_attrs_r | table | jarvis
 public | geographicnamesonusgstopomaps_historical_usgs_20110801__attrs_r | table | jarvis
 public | geographicnamesonusgstopomaps_historical_usgs_20110801_ll83_att | table | jarvis
 public | geographicnamesonusgstopomaps_historical_usgs_20110801_utm83_at | table | jarvis
 public | geographicnamesonusgstopomaps_usgs_20110801_ll83_attrs_raw      | table | jarvis
 public | geographicnamesonusgstopomaps_usgs_20110801_utm83_attrs_raw     | table | jarvis
 public | geolgyl_reg_ll83_attrs_raw                                      | table | jarvis
 public | geolgyp_reg_ll83_attrs_raw                                      | table | jarvis
 public | geospatial_layers                                               | table | jarvis
 public | geotextl_reg_ll83_attrs_raw                                     | table | jarvis
 public | glacagl_reg_ll83_attrs_raw                                      | table | jarvis
 public | glacal_reg_ll83_attrs_raw                                       | table | jarvis
 public | hazardmitigationbuyout_20250929_polygons_utm83_attrs_raw        | table | jarvis
 public | hazardmitigationbuyout_20250929_polygons_wma84_attrs_raw        | table | jarvis
 public | healthruralfacilities_manysources_utm83_attrs_raw               | table | jarvis
 public | highered_wvemd_072420_utm83_attrs_raw                           | table | jarvis
 public | highered_wvemd_072420_wgc84_attrs_raw                           | table | jarvis
 public | historicalaerialphotographycountycoverage_wvgistc_utm83_attrs_r | table | jarvis
 public | hospitals_attrs_raw                                             | table | jarvis
 public | hospitals_wvdem_040519_gcs84_attrs_raw                          | table | jarvis
 public | hospitals_wvdem_040519_utm83_attrs_raw                          | table | jarvis
 public | hospitalswvdem040519utm83_attrs_raw                             | table | jarvis
 public | impact_reg_ll83_attrs_raw                                       | table | jarvis
 public | indexgrid15minutequads_wvgistc_ll83_attrs_raw                   | table | jarvis
 public | indexgrid15minutequads_wvgistc_utm83_attrs_raw                  | table | jarvis
 public | indexgrid15minutewithcounties_wvgistc_utm27_attrs_raw           | table | jarvis
 public | indexgrid1minutequads_wvgistc_ll83_attrs_raw                    | table | jarvis
 public | industrialbuildings_wvdo_200807_utm83_attrs_raw                 | table | jarvis
 public | industrialparks_wvdo_200078_utm83_attrs_raw                     | table | jarvis
 public | industrialsites_wvdo_200807_utm83_attrs_raw                     | table | jarvis
 public | inedexgrid1minutequads_wvgistc_utm83_attrs_raw                  | table | jarvis
 public | intake_submissions                                              | table | jarvis
 public | intermodalterminalfacilities_usdot_1997_ll83_attrs_raw          | table | jarvis
 public | intermodalterminalfacilities_usdot_1997_utm83_attrs_raw         | table | jarvis
 public | layer_config                                                    | table | jarvis
 public | libraries_manysources_2001_ll27_attrs_raw                       | table | jarvis
 public | libraries_manysources_2001_utm83_attrs_raw                      | table | jarvis
 public | majorriversandlakesline_nhd_2002_ll83_attrs_raw                 | table | jarvis
 public | majorriversandlakesline_nhd_2002_utm83_attrs_raw                | table | jarvis
 public | majorriversandlakespolygon_nhd_2002_poly_ll83_attrs_raw         | table | jarvis
 public | majorriversandlakespolygon_nhd_2002_utm83_attrs_raw             | table | jarvis
 public | manufacturingandbusiness_wvdo_200803_utm83_attrs_raw            | table | jarvis
 public | metfacp_reg_ll83_attrs_raw                                      | table | jarvis
 public | metropolitanandmicropolitanstatisticalareas_census_2011_attrs_r | table | jarvis
 public | metropolitanandmicropolitanstatisticalareas_census_2020_attrs_r | table | jarvis
 public | metropolitanandmicropolitanstatisticalareas_census_2020_utm83_a | table | jarvis
 public | metropolitanandmicropolitanstatisticalareas_census_2020_wma84_a | table | jarvis
 public | metropolitanandmicropolitanstatisticalareascensus201111gcs83att | table | jarvis
 public | metropolitanandmicropolitanstatisticalareascensus201111utm83att | table | jarvis
 public | metropolitanstatisticalareas_uscensus_199901_ll83_attrs_raw     | table | jarvis
 public | metropolitanstatisticalareas_uscensus_199901_utm83_attrs_raw    | table | jarvis
 public | mineraloperations_usgs_200204_ll83_attrs_raw                    | table | jarvis
 public | mineraloperations_usgs_200204_utm83_attrs_raw                   | table | jarvis
 public | minesabandonedlandsline_wvdep_1996_noprojectoin_attrs_raw       | table | jarvis
 public | minesabandonedlandspoint_wvdep_1996_noprojection_attrs_raw      | table | jarvis
 public | minesabandonedlandspolygon_wvdep_1996_noprojection_attrs_raw    | table | jarvis
 public | ms_jarvis_learning_log                                          | table | jarvis
 public | nationalatlasstreams_usgs_199903_ll83_attrs_raw                 | table | jarvis
 public | nationalatlasstreams_usgs_199903_utm83_attrs_raw                | table | jarvis
 public | nationalregister_point_20200923_attrs_raw                       | table | jarvis
 public | nationalregister_point_20200923_utm27_attrs_raw                 | table | jarvis
 public | nationalregisterofhistoricplacespoints_nationalparkser__attrs_r | table | jarvis
 public | nationalregisterofhistoricplacespoints_natoinalpakrser__attrs_r | table | jarvis
 public | nationalregisterofhistoricplacespolygons_nationaparkse__attrs_r | table | jarvis
 public | nationalwaterwaynetwork_usarmycorpsofengineers_2001_ll83_attrs_ | table | jarvis
 public | nationalwaterwaynetwork_usarmycorpsofengineers_2001_ll8_attrs_r | table | jarvis
 public | nationalwaterwaynetwork_usarmycorpsofengineers_2001_utm83_attrs | table | jarvis
 public | nationalwaterwaynetwork_usarmycorpsofengineers_2001_utm_attrs_r | table | jarvis
 public | nationalwaterwaynetworkports_usarmycorpsofengineers_2001_ll83_a | table | jarvis
 public | nationalwaterwaynetworkports_usarmycorpsofengineers_2001_utm83_ | table | jarvis
 public | nationalwaterwaynetworkports_usarmycorpsofengineers_200_attrs_r | table | jarvis
 public | nationaregisterofhistoricplacespoints_nationalparkserv__attrs_r | table | jarvis
 public | nationaregisterofhistoricplacespolygons_nationalparkse__attrs_r | table | jarvis
 public | natoinalregisterofhistoricplacespoints_nationalparkser__attrs_r | table | jarvis
 public | naviagablewaterways_usarmycropsofengineers_2006_utm83_attrs_raw | table | jarvis
 public | navigablewaterwaysrivermiles_usarmycropsofengineers_2006_utm83_ | table | jarvis
 public | navigablewaterwaysrivermiles_usarmycropsofengineers_200_attrs_r | table | jarvis
 public | navigablewaterwaysstructures_usarmycorpsofengineers_2006_utm83_ | table | jarvis
 public | navigablewaterwaysstructures_usarmycorpsofengineers_200_attrs_r | table | jarvis
 public | nursinghomes_wvdem_041219_gcs84_attrs_raw                       | table | jarvis
 public | nursinghomes_wvdem_041219_utm83_attrs_raw                       | table | jarvis
 public | officebuildings_wvdo_200807_utm83_attrs_raw                     | table | jarvis
 public | paroleoffices_manysources_2008_utm83_attrs_raw                  | table | jarvis
 public | paroleoffices_manysources_2008_wgs84_attrs_raw                  | table | jarvis
 public | placesofworship_hsip_20080723_utm83_attrs_raw                   | table | jarvis
 public | placesofworship_hsip_20080723_wgs84_attrs_raw                   | table | jarvis
 public | policedept_wvdem_012319_gcs84_attrs_raw                         | table | jarvis
 public | policedept_wvdem_012319_utm83_attrs_raw                         | table | jarvis
 public | populatedplaces_census_201112_utm83_attrs_raw                   | table | jarvis
 public | populatedplaces_census_20112_gcs83_attrs_raw                    | table | jarvis
 public | populatedplaces_census_2020_utm83_attrs_raw                     | table | jarvis
 public | populatedplaces_census_2020_wma84_attrs_raw                     | table | jarvis
 public | populatedplaces_uscensus_1990_ll83_attrs_raw                    | table | jarvis
 public | populatedplaces_uscensus_1990_utm83_attrs_raw                   | table | jarvis
 public | populationdatablockgroups_uscensus_2000_ll83_attrs_raw          | table | jarvis
 public | populationdatablockgroups_uscensus_2000_utm83_attrs_raw         | table | jarvis
 public | pow_wvgistc_062919_utm83_attrs_raw                              | table | jarvis
 public | pow_wvgistc_062919_wgs84_attrs_raw                              | table | jarvis
 public | program                                                         | table | jarvis
 public | program_authority_links                                         | table | jarvis
 public | program_catalog                                                 | table | jarvis
 public | program_eligibility                                             | table | jarvis
 public | program_entity_links                                            | table | jarvis
 public | program_evidence_links                                          | table | jarvis
 public | program_income_limit_rules                                      | table | jarvis
 public | program_income_source_policy                                    | table | jarvis
 public | program_manual_rule_links                                       | table | jarvis
 public | program_name_crosswalk                                          | table | jarvis
 public | program_target_config                                           | table | jarvis
 public | publichealthdepts_hsip_20091229_gcs83_attrs_raw                 | table | jarvis
 public | publichealthdepts_hsip_20091229_utm83_attrs_raw                 | table | jarvis
 public | railnetworkregion_usdot_200203_ll83_attrs_raw                   | table | jarvis
 public | railnetworkregion_usdot_200203_utm83_attrs_raw                  | table | jarvis
 public | railnetworkwv_usdot_200203_ll83_attrs_raw                       | table | jarvis
 public | railnetworkwv_usdot_200203_utm83_attrs_raw                      | table | jarvis
 public | railroads_rahalltransportationinstitute_2005_utm83_attrs_raw    | table | jarvis
 public | realtimestreamflowstations_usgs_200012_ll27_attrs_raw           | table | jarvis
 public | realtimestreamflowstations_usgs_200012_utm27_attrs_raw          | table | jarvis
 public | realtimestreamflowstations_usgs_200012_utm83_attrs_raw          | table | jarvis
 public | recreationalwwtrails_ofwv_20151117_utm83_attrs_raw              | table | jarvis
 public | regionalplanninganddevelopmentcouncil_wvdo_1971_ll83_attrs_raw  | table | jarvis
 public | regionalplanninganddevelopmentcouncil_wvdo_1971_utm83_attrs_raw | table | jarvis
 public | resource_county_coverage                                        | table | jarvis
 public | resource_eligibility                                            | table | jarvis
 public | sewertreatmentplants_wvdep_200203_utm83_attrs_raw               | table | jarvis
 public | solidwastefacilities_wvdep_200202_ll83_attrs_raw                | table | jarvis
 public | solidwastefacilities_wvdep_200202_utm83_attrs_raw               | table | jarvis
 public | springs_wvges_1986_ll83_attrs_raw                               | table | jarvis
 public | springs_wvges_1986_utm83_attrs_raw                              | table | jarvis
 public | stateofwvhousedistricts_wvlegislativeservices_2010_attrs_raw    | table | jarvis
 public | stateofwvsenatedistricts_wvlegislativeservices_2010_attrs_raw   | table | jarvis
 public | states_region_ll83_attrs_raw                                    | table | jarvis
 public | structurepointsnorth_samb_2003_utm83_attrs_raw                  | table | jarvis
 public | structurepointssouth_samb_2003_utm83_attrs_raw                  | table | jarvis
 public | structurepolygons_samb_2003_utm83_attrs_raw                     | table | jarvis
 public | summits_gistc_052012_utm83_shp_attrs_raw                        | table | jarvis
 public | summits_gistc_052012_wgs84_shp_attrs_raw                        | table | jarvis
 public | surveycontrol_nationalgeodeticsurvey_102011_gcs83_attrs_raw     | table | jarvis
 public | timberremovalvolume_usfs_1996_utm83_attrs_raw                   | table | jarvis
 public | tmp_building_block_nearest_sample                               | table | jarvis
 public | towers_wvpublicbroadcasting_2002_ll83_attrs_raw                 | table | jarvis
 public | towers_wvpublicbroadcasting_2002_utm83_attrs_raw                | table | jarvis
 public | towersam_fcc_200202_utm83_attrs_raw                             | table | jarvis
 public | towersasr_fcc_200202_ll83_attrs_raw                             | table | jarvis
 public | towersasr_fcc_200202_utm83_attrs_raw                            | table | jarvis
 public | towerscellular_fcc_200202_ll83_attrs_raw                        | table | jarvis
 public | towerscellular_fcc_200202_utm83_attrs_raw                       | table | jarvis
 public | towersfm_fcc_200202_utm83_attrs_raw                             | table | jarvis
 public | towersmicrowave_fcc_200202_ll83_attrs_raw                       | table | jarvis
 public | towersmicrowave_fcc_200202_utm83_attrs_raw                      | table | jarvis
 public | towerspager_fcc_200202_ll83_attrs_raw                           | table | jarvis
 public | towerspager_fcc_200202_utm83_attrs_raw                          | table | jarvis
 public | towersprivate_fcc_200202_ll83_attrs_raw                         | table | jarvis
 public | towersprivate_fcc_200202_utm83_attrs_raw                        | table | jarvis
 public | uei_registry                                                    | table | jarvis
 public | user_compliance_task                                            | table | jarvis
 public | utility_discount_enrollment                                     | table | jarvis
 public | veteransaffairsfacilities_manysources_200503_utm83_attrs_raw    | table | jarvis
 public | veteransaffairsfacilities_manysources_200503_wgs84_attrs_raw    | table | jarvis
 public | votingdistrictswv_legislativeservices_2002_ll83_attrs_raw       | table | jarvis
 public | votingdistrictswv_legislativeservices_2002_utm83_attrs_raw      | table | jarvis
 public | votingdistrictswv_uscensus_2000_utm83_attrs_raw                 | table | jarvis
 public | weatherstations_nationalclimatedatacenter_1999_gcs83_attrs_raw  | table | jarvis
 public | weatherstations_nationalclimatedatacenter_1999_utm27_attrs_raw  | table | jarvis
 public | windenergyresource_nationalrenewableenergylab_200901_ut_attrs_r | table | jarvis
 public | windenergyresource_nationalrenewableenergylab_200901_utm83_attr | table | jarvis
 public | windenergyresource_nationalrenewableenergylab_200901_wg_attrs_r | table | jarvis
 public | windenergyresource_nationalrenewableenergylab_200901_wgs84_attr | table | jarvis
 public | workforceinvestmentareas_wvgistc_200208_ll83_attrs_raw          | table | jarvis
 public | wv_county_boundaries_24k_topo_updated_2022_utm83_attrs_raw      | table | jarvis
 public | wv_county_names                                                 | table | jarvis
 public | wv_income_manual_income_limits                                  | table | jarvis
 public | wv_income_manual_income_sources                                 | table | jarvis
 public | wv_income_manual_income_treatment                               | table | jarvis
 public | wv_income_manual_income_treatment_extended                      | table | jarvis
 public | wv_income_manual_rules                                          | table | jarvis
 public | wv_microsoft_20180207_utm17n83_attrs_raw                        | table | jarvis
 public | wv_tax_districts_ll83_attrs_raw                                 | table | jarvis
 public | wv_tax_districts_utm83_attrs_raw                                | table | jarvis
 public | wv_tax_districts_wma84_attrs_raw                                | table | jarvis
 public | wvgistc_building_footprints_attrs_raw                           | table | jarvis
 public | wvgistcbuildingfootprints_attrs_raw                             | table | jarvis
 public | wvgistcbuildingfootprintsattrsraw                               | table | jarvis
 public | wvstatebounadary100k_usgs_200203_utm83_attrs_raw                | table | jarvis
 public | wvstateboundary100k_usgs_200203_ll83_attrs_raw                  | table | jarvis
 public | wvstateboundary24k_usgs_200203_ll83_attrs_raw                   | table | jarvis
 public | wvstateboundary24k_usgs_200203_utm83_attrs_raw                  | table | jarvis
 public | wvstatehousedistricts_manysources_1992_ll83_attrs_raw           | table | jarvis
 public | wvstatehousedistricts_manysources_1992_utm83_attrs_raw          | table | jarvis
 public | wvstatehousedistricts_manysources_2002_ll83_attrs_raw           | table | jarvis
 public | wvstatehousedistricts_manysources_2002_utm83_attrs_raw          | table | jarvis
 public | wvstatehousedistricts_wvlegislativeservices_2020_utm83_attrs_ra | table | jarvis
 public | wvstatesenatedistricts_manysources_1992_ll83_attrs_raw          | table | jarvis
 public | wvstatesenatedistricts_manysources_1992_utm83_attrs_raw         | table | jarvis
 public | wvstatesenatedistricts_manysources_2002_ll83_attrs_raw          | table | jarvis
 public | wvstatesenatedistricts_manysources_2002_utm83_attrs_raw         | table | jarvis
 public | wvstatesenatedistricts_wvlegislativeservices_2020_utm83_attrs_r | table | jarvis
 public | zcta_county_rel                                                 | table | jarvis
 public | zipcodetabulationarea_census_2020_utm83_attrs_raw               | table | jarvis
 public | zipcodetabulationarea_census_2020_wma84_attrs_raw               | table | jarvis
(297 rows)

Did not find any relation named "wv_locations".
              List of relations
  Schema  |      Name       | Type  | Owner  
----------+-----------------+-------+--------
 public   | spatial_ref_sys | table | jarvis
 public   | wv_locations    | table | jarvis
 topology | layer           | table | jarvis
 topology | topology        | table | jarvis
(4 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ # List all services managed by the inner compose file
docker compose -f ~/msjarvis-rebuild-working/msjarvis-rebuild/msjarvis-rebuild/docker-compose.yml ps

# Check which orphan services are actually running
docker compose -f ~/msjarvis-rebuild-working/msjarvis-rebuild/msjarvis-rebuild/docker-compose.yml ps --format "table {{.Name}}\t{{.Status}}\t{{.Ports}}"
NAME                                                    IMAGE                                                 COMMAND                  SERVICE                              CREATED         STATUS                  PORTS
ipfs                                                    ipfs/kubo:latest                                      "/sbin/tini -- /usr/…"   ipfs                                 5 hours ago     Up 5 hours (healthy)    4001/tcp, 8080-8081/tcp, 4001/udp, 127.0.0.1:5001->5001/tcp
jarvis-20llm-production                                 msjarvis-rebuild-jarvis-20llm-production              "python3 ai_server_2…"   jarvis-20llm-production              11 hours ago    Up 11 hours             127.0.0.1:8008->8008/tcp
jarvis-69dgm-bridge                                     msjarvis-rebuild-jarvis-69dgm-bridge                  "python3 port_9000_6…"   jarvis-69dgm-bridge                  7 hours ago     Up 7 hours              127.0.0.1:19000->9000/tcp
jarvis-aaacpe-rag                                       msjarvis-rebuild-jarvis-aaacpe-rag                    "uvicorn aaacpe_rag_…"   jarvis-aaacpe-rag                    5 hours ago     Up 5 hours              127.0.0.1:8032->8032/tcp
jarvis-agents-service                                   msjarvis-rebuild-jarvis-agents-service                "python3 ms_jarvis_a…"   jarvis-agents-service                5 hours ago     Up 5 hours              8005/tcp
jarvis-autonomous-learner                               msjarvis-rebuild-jarvis-autonomous-learner            "uvicorn ms_jarvis_a…"   jarvis-autonomous-learner            5 hours ago     Up 5 hours              127.0.0.1:8020->8020/tcp
jarvis-bbb-output-filter                                msjarvis-rebuild-bbb-output-filter                    "uvicorn app:app --h…"   bbb-output-filter                    7 hours ago     Up 7 hours              127.0.0.1:8017->8017/tcp
jarvis-blood-brain-barrier                              msjarvis-rebuild-jarvis-blood-brain-barrier           "python3 ms_jarvis_b…"   jarvis-blood-brain-barrier           31 hours ago    Up 31 hours             127.0.0.1:8016->8016/tcp
jarvis-brain-orchestrator                               msjarvis-rebuild-jarvis-brain-orchestrator            "python3 brain_orche…"   jarvis-brain-orchestrator            32 hours ago    Up 32 hours (healthy)   127.0.0.1:17260->7260/tcp
jarvis-chroma                                           chromadb/chroma:latest                                "dumb-init -- chroma…"   jarvis-chroma                        31 hours ago    Up 4 hours (healthy)    127.0.0.1:8002->8000/tcp
jarvis-commons-gamification                             msjarvis-rebuild-jarvis-main-brain:latest             "sh -lc 'pip install…"   jarvis-commons-gamification          5 hours ago     Up 5 hours              127.0.0.1:8081->8081/tcp
jarvis-community-stake-registry                         msjarvis-rebuild-jarvis-main-brain:latest             "sh -lc 'pip install…"   jarvis-community-stake-registry      5 hours ago     Up 5 hours              127.0.0.1:8084->8084/tcp
jarvis-consciousness-bridge                             msjarvis-rebuild-jarvis-consciousness-bridge          "python3 /app/servic…"   jarvis-consciousness-bridge          26 hours ago    Up 26 hours             8020/tcp
jarvis-constitutional-guardian                          msjarvis-rebuild-jarvis-constitutional-guardian       "python3 jarvis-cons…"   jarvis-constitutional-guardian       4 days ago      Up 4 days               127.0.0.1:8091->8091/tcp
jarvis-crypto-policy                                    msjarvis-rebuild-jarvis-crypto-policy                 "uvicorn jarviscrypt…"   jarvis-crypto-policy                 5 hours ago     Up 5 hours              127.0.0.1:8099->8099/tcp
jarvis-dao-governance                                   msjarvis-rebuild-jarvis-main-brain:latest             "sh -lc 'pip install…"   jarvis-dao-governance                5 hours ago     Up 5 hours              127.0.0.1:8082->8082/tcp
jarvis-data-ingest                                      msjarvis-rebuild-jarvis-data-ingest                   "uvicorn jarvis_data…"   jarvis-data-ingest                   4 days ago      Up 4 days               127.0.0.1:8077->8077/tcp
jarvis-eeg-beta                                         msjarvis-rebuild-jarvis-eeg-beta                      "uvicorn jarvis_eeg_…"   jarvis-eeg-beta                      3 hours ago     Up 3 hours              127.0.0.1:8075->8075/tcp
jarvis-eeg-delta                                        msjarvis-rebuild-jarvis-eeg-delta                     "uvicorn jarvis_eeg_…"   jarvis-eeg-delta                     3 hours ago     Up 3 hours              127.0.0.1:8073->8073/tcp
jarvis-eeg-theta                                        msjarvis-rebuild-jarvis-eeg-theta                     "uvicorn jarvis_eeg_…"   jarvis-eeg-theta                     3 hours ago     Up 3 hours              127.0.0.1:8074->8074/tcp
jarvis-fifth-dgm                                        msjarvis-rebuild-jarvis-fifth-dgm                     "python -m uvicorn m…"   jarvis-fifth-dgm                     5 hours ago     Up 5 hours              127.0.0.1:4002->4002/tcp
jarvis-fractal-consciousness                            msjarvis-rebuild-jarvis-fractal-consciousness         "python3 /app/servic…"   jarvis-fractal-consciousness         6 hours ago     Up 6 hours              8027/tcp
jarvis-gbim-benefit-indexer                             python:3.11-slim                                      "bash -c 'pip instal…"   jarvis-gbim-benefit-indexer          4 days ago      Up 4 days               127.0.0.1:7206->7206/tcp
jarvis-gbim-query-router                                python:3.11-slim                                      "bash -c 'pip instal…"   jarvis-gbim-query-router             30 hours ago    Up 30 hours             127.0.0.1:7205->7205/tcp
jarvis-gis-rag                                          msjarvis-rebuild-jarvis-gis-rag:latest                "uvicorn gis_rag_ser…"   jarvis-gis-rag                       5 hours ago     Up 5 hours              127.0.0.1:8004->8004/tcp, 8008/tcp
jarvis-hilbert-gateway                                  msjarvis-rebuild-jarvis-hilbert-gateway:latest        "uvicorn jarvis-wv-e…"   jarvis-hilbert-gateway               4 days ago      Up 4 days               
jarvis-hilbert-state                                    msjarvis-rebuild-jarvis-hilbert-state                 "python3 -m uvicorn …"   jarvis-hilbert-state                 27 hours ago    Up 27 hours             
jarvis-hippocampus                                      msjarvis-rebuild-jarvis-hippocampus:latest            "uvicorn hippocampus…"   jarvis-hippocampus                   11 hours ago    Up 11 hours             127.0.0.1:8011->8011/tcp
jarvis-i-containers                                     msjarvis-rebuild-jarvis-i-containers                  "/opt/nvidia/nvidia_…"   jarvis-i-containers                  11 hours ago    Up 11 hours             127.0.0.1:8015->8015/tcp
jarvis-ingest-api                                       python:3.11-slim                                      "python3 -c 'import …"   jarvis-ingest-api                    4 days ago      Up 2 hours              
jarvis-ingest-watcher                                   msjarvis-rebuild_jarvis-ingest-watcher                "python3 /app/ingest…"   jarvis-ingest-watcher                5 hours ago     Up 5 hours              
jarvis-intake-service                                   msjarvis-rebuild-jarvis-intake-service:latest         "uvicorn intake_serv…"   jarvis-intake-service                4 days ago      Up 4 days               127.0.0.1:8007->8007/tcp
jarvis-judge-alignment                                  msjarvis-rebuild-jarvis-judge-alignment               "python judge_alignm…"   jarvis-judge-alignment               11 hours ago    Up 11 hours             127.0.0.1:7232->7232/tcp
jarvis-judge-consistency                                msjarvis-rebuild-jarvis-judge-consistency             "python judge_consis…"   jarvis-judge-consistency             11 hours ago    Up 11 hours             127.0.0.1:7231->7231/tcp
jarvis-judge-ethics                                     msjarvis-rebuild-jarvis-judge-ethics                  "python judge_ethics…"   jarvis-judge-ethics                  11 hours ago    Up 11 hours             127.0.0.1:7233->7233/tcp
jarvis-judge-pipeline                                   msjarvis-rebuild-jarvis-judge-pipeline                "python judge_pipeli…"   jarvis-judge-pipeline                3 hours ago     Up 3 hours              127.0.0.1:7239->7239/tcp
jarvis-judge-truth                                      msjarvis-rebuild-jarvis-judge-truth                   "python judge_truth_…"   jarvis-judge-truth                   11 hours ago    Up 11 hours             127.0.0.1:7230->7230/tcp
jarvis-lm-synthesizer                                   msjarvis-rebuild-jarvis-lm-synthesizer                "python lm_synthesiz…"   jarvis-lm-synthesizer                11 hours ago    Up 11 hours             8001/tcp
jarvis-local-resources                                  msjarvis-rebuild-jarvis-local-resources               "uvicorn local_resou…"   jarvis-local-resources               11 hours ago    Up 11 hours             127.0.0.1:8006->8006/tcp
jarvis-local-resources-db                               postgis/postgis:15-3.4                                "docker-entrypoint.s…"   jarvis-local-resources-db            5 hours ago     Up 5 hours              127.0.0.1:5435->5432/tcp
jarvis-main-brain                                       msjarvis-rebuild-jarvis-main-brain                    "sh -lc 'cd /app/ser…"   jarvis-main-brain                    6 hours ago     Up 6 hours (healthy)    127.0.0.1:8050->8050/tcp
jarvis-memory                                           msjarvis-rebuild-jarvis-memory                        "uvicorn ms_jarvis_m…"   jarvis-memory                        5 hours ago     Up 5 hours              127.0.0.1:8056->8056/tcp
jarvis-mother-protocols                                 msjarvis-rebuild-jarvis-mother-protocols              "python -m uvicorn m…"   jarvis-mother-protocols              5 hours ago     Up 5 hours              4000/tcp
jarvis-ms-analytics                                     msjarvis-rebuild-ms-mountainshares-coordinator        "uvicorn ms_mountain…"   ms-mountainshares-analytics          6 hours ago     Up 6 hours              127.0.0.1:8083->8083/tcp
jarvis-ms-coordinator                                   msjarvis-rebuild-ms-mountainshares-coordinator        "python3 ms_mountain…"   ms-mountainshares-coordinator        6 hours ago     Up 6 hours              127.0.0.1:7300->7300/tcp
jarvis-ms-indexer                                       msjarvis-rebuild-ms-mountainshares-coordinator        "uvicorn ms_mountain…"   ms-mountainshares-indexer            6 hours ago     Up 6 hours              127.0.0.1:8086->8080/tcp
jarvis-ms-token-service                                 msjarvis-rebuild-jarvis-main-brain:latest             "sh -lc 'pip install…"   jarvis-ms-token-service              4 minutes ago   Up 4 minutes            127.0.0.1:8088->8083/tcp
jarvis-neurobiological-master                           msjarvis-rebuild-jarvis-neurobiological-master        "python3 ms_jarvis_n…"   jarvis-neurobiological-master        9 hours ago     Up 9 hours              8018/tcp
jarvis-ollama                                           ollama/ollama:latest                                  "/bin/ollama serve"      jarvis-ollama                        7 hours ago     Up 7 hours              127.0.0.1:11434->11434/tcp
jarvis-psychology-services                              msjarvis-rebuild-jarvis-psychology-services:latest    "python ms_jarvis_ps…"   jarvis-psychology-services           3 days ago      Up 47 hours             127.0.0.1:8019->8019/tcp
jarvis-qualia-engine                                    msjarvis-rebuild-jarvis-qualia-engine                 "python3 ms_jarvis_q…"   jarvis-qualia-engine                 11 hours ago    Up 11 hours             8017/tcp
jarvis-rag-server                                       msjarvis-rebuild-jarvis-rag-server:latest             "python3 ms_jarvis_r…"   jarvis-rag-server                    5 hours ago     Up 5 hours              127.0.0.1:8003->8003/tcp
jarvis-redis                                            redis:7-alpine                                        "docker-entrypoint.s…"   jarvis-redis                         6 hours ago     Up 6 hours (healthy)    127.0.0.1:6380->6379/tcp
jarvis-redis-local                                      redis:7-alpine                                        "docker-entrypoint.s…"   jarvis-redis-local                   6 days ago      Up 6 days               127.0.0.1:16380->6379/tcp
jarvis-semaphore                                        msjarvis-rebuild-jarvis-semaphore                     "uvicorn jarvis-sema…"   jarvis-semaphore                     11 hours ago    Up 11 hours             127.0.0.1:8030->8030/tcp
jarvis-spiritual-rag                                    msjarvis-rebuild-jarvis-spiritual-rag:latest          "python spiritual_ra…"   jarvis-spiritual-rag                 5 hours ago     Up 5 hours              127.0.0.1:8005->8005/tcp
jarvis-steward                                          msjarvis-steward-local:latest                         "sh -c 'PYTHONPATH=/…"   jarvis-steward                       22 hours ago    Up 22 hours             127.0.0.1:8060->8060/tcp
jarvis-stewardship-scheduler                            msjarvis-rebuild-jarvis-stewardship-scheduler         "python3 jarvis_stew…"   jarvis-stewardship-scheduler         4 days ago      Up 4 days               127.0.0.1:8079->8079/tcp
jarvis-swarm-intelligence                               msjarvis-rebuild-jarvis-swarm-intelligence            "python3 ms_jarvis_s…"   jarvis-swarm-intelligence            5 hours ago     Up 5 hours              8021/tcp
jarvis-temporal-consciousness                           msjarvis-rebuild-jarvis-temporal-consciousness        "python -m uvicorn t…"   jarvis-temporal-consciousness        5 hours ago     Up 5 hours              7007/tcp
jarvis-toroidal                                         msjarvis-rebuild-jarvis-toroidal:latest               "python -m uvicorn t…"   jarvis-toroidal                      4 days ago      Up 4 days               127.0.0.1:8025->8025/tcp
jarvis-unified-gateway                                  msjarvis-rebuild-jarvis-unified-gateway               "python3 ms_jarvis_u…"   jarvis-unified-gateway               10 hours ago    Up 9 hours              127.0.0.1:18018->8001/tcp
jarvis-web-research                                     msjarvis-rebuild-jarvis-web-research                  "python ms_jarvis_we…"   jarvis-web-research                  5 hours ago     Up 5 hours              8090/tcp
jarvis-woah                                             msjarvis-rebuild-jarvis-woah                          "uvicorn woah_servic…"   jarvis-woah                          31 hours ago    Up 31 hours             7012/tcp
jarvis-wv-entangled-gateway                             msjarvis-rebuild-jarvis-wv-entangled-gateway:latest   "python3 /app/msjarv…"   jarvis-wv-entangled-gateway          4 days ago      Up 4 days               127.0.0.1:8010->8010/tcp
llm1-proxy                                              msjarvis-rebuild-llm1-proxy:latest                    "python -m uvicorn l…"   llm1-proxy                           5 hours ago     Up 5 hours              127.0.0.1:8201->8201/tcp
llm10-proxy                                             msjarvis-rebuild-llm10-proxy:latest                   "python -m uvicorn l…"   llm10-proxy                          5 hours ago     Up 5 hours              127.0.0.1:8210->8210/tcp
llm11-proxy                                             msjarvis-rebuild-llm11-proxy:latest                   "python -m uvicorn l…"   llm11-proxy                          5 hours ago     Up 5 hours              127.0.0.1:8211->8211/tcp
llm12-proxy                                             msjarvis-rebuild-llm12-proxy:latest                   "python -m uvicorn l…"   llm12-proxy                          5 hours ago     Up 5 hours              127.0.0.1:8212->8212/tcp
llm13-proxy                                             msjarvis-rebuild-llm13-proxy:latest                   "uvicorn llm13_healt…"   llm13-proxy                          5 hours ago     Up 5 hours              127.0.0.1:8213->8213/tcp
llm14-proxy                                             msjarvis-rebuild-llm14-proxy:latest                   "python -m uvicorn l…"   llm14-proxy                          5 hours ago     Up 5 hours              127.0.0.1:8214->8214/tcp
llm15-proxy                                             msjarvis-rebuild-llm15-proxy:latest                   "python -m uvicorn l…"   llm15-proxy                          5 hours ago     Up 5 hours              127.0.0.1:8215->8215/tcp
llm16-proxy                                             msjarvis-rebuild-llm16-proxy:latest                   "python -m uvicorn l…"   llm16-proxy                          5 hours ago     Up 5 hours              127.0.0.1:8216->8216/tcp
llm17-proxy                                             msjarvis-rebuild-llm17-proxy:latest                   "python -m uvicorn l…"   llm17-proxy                          5 hours ago     Up 5 hours              127.0.0.1:8217->8217/tcp
llm18-proxy                                             msjarvis-rebuild-llm18-proxy:latest                   "python -m uvicorn l…"   llm18-proxy                          5 hours ago     Up 5 hours              127.0.0.1:8218->8218/tcp
llm19-proxy                                             msjarvis-rebuild-llm19-proxy:latest                   "python -m uvicorn l…"   llm19-proxy                          5 hours ago     Up 5 hours              127.0.0.1:8219->8219/tcp
llm2-proxy                                              msjarvis-rebuild-llm2-proxy:latest                    "python -m uvicorn l…"   llm2-proxy                           5 hours ago     Up 5 hours              127.0.0.1:8202->8202/tcp
llm20-proxy                                             msjarvis-rebuild-llm20-proxy:latest                   "python -m uvicorn l…"   llm20-proxy                          5 hours ago     Up 5 hours              127.0.0.1:8220->8220/tcp
llm21-proxy                                             msjarvis-rebuild-llm21-proxy:latest                   "python -m uvicorn l…"   llm21-proxy                          5 hours ago     Up 5 hours              127.0.0.1:8221->8221/tcp
llm22-proxy                                             msjarvis-rebuild-llm22-proxy:latest                   "python -m uvicorn l…"   llm22-proxy                          5 hours ago     Up 5 hours              127.0.0.1:8222->8222/tcp
llm3-proxy                                              msjarvis-rebuild-llm3-proxy:latest                    "python -m uvicorn l…"   llm3-proxy                           5 hours ago     Up 5 hours              127.0.0.1:8203->8203/tcp
llm4-proxy                                              msjarvis-rebuild-llm4-proxy:latest                    "python -m uvicorn l…"   llm4-proxy                           5 hours ago     Up 5 hours              127.0.0.1:8204->8204/tcp
llm5-proxy                                              msjarvis-rebuild-llm5-proxy:latest                    "python -m uvicorn l…"   llm5-proxy                           5 hours ago     Up 5 hours              127.0.0.1:8205->8205/tcp
llm6-proxy                                              msjarvis-rebuild-llm6-proxy:latest                    "python -m uvicorn l…"   llm6-proxy                           5 hours ago     Up 5 hours              127.0.0.1:8206->8206/tcp
llm7-proxy                                              msjarvis-rebuild-llm7-proxy:latest                    "python -m uvicorn l…"   llm7-proxy                           5 hours ago     Up 5 hours              127.0.0.1:8207->8207/tcp
llm8-proxy                                              msjarvis-rebuild-llm8-proxy:latest                    "python -m uvicorn l…"   llm8-proxy                           5 hours ago     Up 5 hours              127.0.0.1:8208->8208/tcp
llm9-proxy                                              msjarvis-rebuild-llm9-proxy:latest                    "python -m uvicorn l…"   llm9-proxy                           5 hours ago     Up 5 hours              127.0.0.1:8209->8209/tcp
msjarvis-rebuild-jarvis-pia-status-1                    python:3.11-slim                                      "sh -c 'pip install …"   jarvis-pia-status                    33 hours ago    Up 3 hours              127.0.0.1:8029->8029/tcp
msjarvis-rebuild-nbb_blood_brain_barrier-1              msjarvis-rebuild-nbb_blood_brain_barrier              "uvicorn blood_brain…"   nbb_blood_brain_barrier              11 days ago     Up 6 days               127.0.0.1:8301->7001/tcp
msjarvis-rebuild-nbb_consciousness_containers-1         msjarvis-rebuild-nbb_consciousness_containers         "uvicorn consciousne…"   nbb_consciousness_containers         11 days ago     Up 6 days               127.0.0.1:8102->7002/tcp
msjarvis-rebuild-nbb_darwin_godel_machines-1            msjarvis-rebuild-nbb_darwin_godel_machines            "uvicorn nbb_darwin_…"   nbb_darwin_godel_machines            5 hours ago     Up 5 hours              127.0.0.1:8302->7003/tcp
msjarvis-rebuild-nbb_heteroglobulin_transport-1         msjarvis-rebuild-nbb_heteroglobulin_transport         "uvicorn heteroglobu…"   nbb_heteroglobulin_transport         11 days ago     Up 6 days               127.0.0.1:8106->7006/tcp
msjarvis-rebuild-nbb_i_containers-1                     msjarvis-rebuild-nbb_i_containers                     "uvicorn i_container…"   nbb_i_containers                     11 days ago     Up 6 days               127.0.0.1:8101->7005/tcp
msjarvis-rebuild-nbb_mother_carrie_protocols-1          msjarvis-rebuild-nbb_mother_carrie_protocols          "uvicorn main:app --…"   nbb_mother_carrie_protocols          11 days ago     Up 6 days               127.0.0.1:8107->7007/tcp
msjarvis-rebuild-nbb_pituitary_gland-1                  msjarvis-rebuild-nbb_pituitary_gland                  "uvicorn pituitary_g…"   nbb_pituitary_gland                  11 hours ago    Up 11 hours             127.0.0.1:8108->80/tcp
msjarvis-rebuild-nbb_prefrontal_cortex-1                msjarvis-rebuild-nbb_prefrontal_cortex                "/start.sh"              nbb_prefrontal_cortex                11 days ago     Up 6 days               127.0.0.1:8105->7005/tcp
msjarvis-rebuild-nbb_qualia_engine-1                    msjarvis-rebuild-nbb_qualia_engine                    "uvicorn qualia_engi…"   nbb_qualia_engine                    11 days ago     Up 6 days               127.0.0.1:8303->7008/tcp
msjarvis-rebuild-nbb_spiritual_maternal_integration-1   msjarvis-rebuild-nbb_spiritual_maternal_integration   "uvicorn spiritual_m…"   nbb_spiritual_maternal_integration   11 days ago     Up 6 days               127.0.0.1:8109->7009/tcp
msjarvis-rebuild-nbb_spiritual_root-1                   msjarvis-rebuild-nbb_spiritual_root                   "uvicorn spiritual_r…"   nbb_spiritual_root                   11 days ago     Up 6 days               127.0.0.1:8103->7003/tcp
msjarvis-rebuild-nbb_subconscious-1                     msjarvis-rebuild-nbb_subconscious                     "uvicorn consciousne…"   nbb_subconscious                     11 days ago     Up 6 days               127.0.0.1:8112->7011/tcp
mysql                                                   mysql:8.2                                             "docker-entrypoint.s…"   mysql                                5 hours ago     Up 5 hours              33060/tcp, 127.0.0.1:3307->3306/tcp
nbb_woah_algorithms                                     msjarvis-rebuild-jarvis-main-brain:latest             "sh -lc 'pip install…"   nbb_woah_algorithms                  6 hours ago     Up 6 hours              127.0.0.1:8104->8104/tcp
neo4j                                                   neo4j:5.13-community                                  "tini -g -- /startup…"   neo4j                                5 hours ago     Up 5 hours              7473/tcp, 127.0.0.1:7687->7687/tcp, 127.0.0.1:7475->7474/tcp
psychological_rag_domain                                msjarvis-rebuild_psychological_rag_domain             "python psychologica…"   psychological_rag_domain             3 days ago      Up 47 hours             9006/tcp, 127.0.0.1:9006->8006/tcp
NAME                                                    STATUS                  PORTS
ipfs                                                    Up 5 hours (healthy)    4001/tcp, 8080-8081/tcp, 4001/udp, 127.0.0.1:5001->5001/tcp
jarvis-20llm-production                                 Up 11 hours             127.0.0.1:8008->8008/tcp
jarvis-69dgm-bridge                                     Up 7 hours              127.0.0.1:19000->9000/tcp
jarvis-aaacpe-rag                                       Up 5 hours              127.0.0.1:8032->8032/tcp
jarvis-agents-service                                   Up 5 hours              8005/tcp
jarvis-autonomous-learner                               Up 5 hours              127.0.0.1:8020->8020/tcp
jarvis-bbb-output-filter                                Up 7 hours              127.0.0.1:8017->8017/tcp
jarvis-blood-brain-barrier                              Up 31 hours             127.0.0.1:8016->8016/tcp
jarvis-brain-orchestrator                               Up 32 hours (healthy)   127.0.0.1:17260->7260/tcp
jarvis-chroma                                           Up 4 hours (healthy)    127.0.0.1:8002->8000/tcp
jarvis-commons-gamification                             Up 5 hours              127.0.0.1:8081->8081/tcp
jarvis-community-stake-registry                         Up 5 hours              127.0.0.1:8084->8084/tcp
jarvis-consciousness-bridge                             Up 26 hours             8020/tcp
jarvis-constitutional-guardian                          Up 4 days               127.0.0.1:8091->8091/tcp
jarvis-crypto-policy                                    Up 5 hours              127.0.0.1:8099->8099/tcp
jarvis-dao-governance                                   Up 5 hours              127.0.0.1:8082->8082/tcp
jarvis-data-ingest                                      Up 4 days               127.0.0.1:8077->8077/tcp
jarvis-eeg-beta                                         Up 3 hours              127.0.0.1:8075->8075/tcp
jarvis-eeg-delta                                        Up 3 hours              127.0.0.1:8073->8073/tcp
jarvis-eeg-theta                                        Up 3 hours              127.0.0.1:8074->8074/tcp
jarvis-fifth-dgm                                        Up 5 hours              127.0.0.1:4002->4002/tcp
jarvis-fractal-consciousness                            Up 6 hours              8027/tcp
jarvis-gbim-benefit-indexer                             Up 4 days               127.0.0.1:7206->7206/tcp
jarvis-gbim-query-router                                Up 30 hours             127.0.0.1:7205->7205/tcp
jarvis-gis-rag                                          Up 5 hours              127.0.0.1:8004->8004/tcp, 8008/tcp
jarvis-hilbert-gateway                                  Up 4 days               
jarvis-hilbert-state                                    Up 27 hours             
jarvis-hippocampus                                      Up 11 hours             127.0.0.1:8011->8011/tcp
jarvis-i-containers                                     Up 11 hours             127.0.0.1:8015->8015/tcp
jarvis-ingest-api                                       Up 2 hours              
jarvis-ingest-watcher                                   Up 5 hours              
jarvis-intake-service                                   Up 4 days               127.0.0.1:8007->8007/tcp
jarvis-judge-alignment                                  Up 11 hours             127.0.0.1:7232->7232/tcp
jarvis-judge-consistency                                Up 11 hours             127.0.0.1:7231->7231/tcp
jarvis-judge-ethics                                     Up 11 hours             127.0.0.1:7233->7233/tcp
jarvis-judge-pipeline                                   Up 3 hours              127.0.0.1:7239->7239/tcp
jarvis-judge-truth                                      Up 11 hours             127.0.0.1:7230->7230/tcp
jarvis-lm-synthesizer                                   Up 11 hours             8001/tcp
jarvis-local-resources                                  Up 11 hours             127.0.0.1:8006->8006/tcp
jarvis-local-resources-db                               Up 5 hours              127.0.0.1:5435->5432/tcp
jarvis-main-brain                                       Up 6 hours (healthy)    127.0.0.1:8050->8050/tcp
jarvis-memory                                           Up 5 hours              127.0.0.1:8056->8056/tcp
jarvis-mother-protocols                                 Up 5 hours              4000/tcp
jarvis-ms-analytics                                     Up 6 hours              127.0.0.1:8083->8083/tcp
jarvis-ms-coordinator                                   Up 6 hours              127.0.0.1:7300->7300/tcp
jarvis-ms-indexer                                       Up 6 hours              127.0.0.1:8086->8080/tcp
jarvis-ms-token-service                                 Up 4 minutes            127.0.0.1:8088->8083/tcp
jarvis-neurobiological-master                           Up 9 hours              8018/tcp
jarvis-ollama                                           Up 7 hours              127.0.0.1:11434->11434/tcp
jarvis-psychology-services                              Up 47 hours             127.0.0.1:8019->8019/tcp
jarvis-qualia-engine                                    Up 11 hours             8017/tcp
jarvis-rag-server                                       Up 5 hours              127.0.0.1:8003->8003/tcp
jarvis-redis                                            Up 6 hours (healthy)    127.0.0.1:6380->6379/tcp
jarvis-redis-local                                      Up 6 days               127.0.0.1:16380->6379/tcp
jarvis-semaphore                                        Up 11 hours             127.0.0.1:8030->8030/tcp
jarvis-spiritual-rag                                    Up 5 hours              127.0.0.1:8005->8005/tcp
jarvis-steward                                          Up 22 hours             127.0.0.1:8060->8060/tcp
jarvis-stewardship-scheduler                            Up 4 days               127.0.0.1:8079->8079/tcp
jarvis-swarm-intelligence                               Up 5 hours              8021/tcp
jarvis-temporal-consciousness                           Up 5 hours              7007/tcp
jarvis-toroidal                                         Up 4 days               127.0.0.1:8025->8025/tcp
jarvis-unified-gateway                                  Up 9 hours              127.0.0.1:18018->8001/tcp
jarvis-web-research                                     Up 5 hours              8090/tcp
jarvis-woah                                             Up 31 hours             7012/tcp
jarvis-wv-entangled-gateway                             Up 4 days               127.0.0.1:8010->8010/tcp
llm1-proxy                                              Up 5 hours              127.0.0.1:8201->8201/tcp
llm10-proxy                                             Up 5 hours              127.0.0.1:8210->8210/tcp
llm11-proxy                                             Up 5 hours              127.0.0.1:8211->8211/tcp
llm12-proxy                                             Up 5 hours              127.0.0.1:8212->8212/tcp
llm13-proxy                                             Up 5 hours              127.0.0.1:8213->8213/tcp
llm14-proxy                                             Up 5 hours              127.0.0.1:8214->8214/tcp
llm15-proxy                                             Up 5 hours              127.0.0.1:8215->8215/tcp
llm16-proxy                                             Up 5 hours              127.0.0.1:8216->8216/tcp
llm17-proxy                                             Up 5 hours              127.0.0.1:8217->8217/tcp
llm18-proxy                                             Up 5 hours              127.0.0.1:8218->8218/tcp
llm19-proxy                                             Up 5 hours              127.0.0.1:8219->8219/tcp
llm2-proxy                                              Up 5 hours              127.0.0.1:8202->8202/tcp
llm20-proxy                                             Up 5 hours              127.0.0.1:8220->8220/tcp
llm21-proxy                                             Up 5 hours              127.0.0.1:8221->8221/tcp
llm22-proxy                                             Up 5 hours              127.0.0.1:8222->8222/tcp
llm3-proxy                                              Up 5 hours              127.0.0.1:8203->8203/tcp
llm4-proxy                                              Up 5 hours              127.0.0.1:8204->8204/tcp
llm5-proxy                                              Up 5 hours              127.0.0.1:8205->8205/tcp
llm6-proxy                                              Up 5 hours              127.0.0.1:8206->8206/tcp
llm7-proxy                                              Up 5 hours              127.0.0.1:8207->8207/tcp
llm8-proxy                                              Up 5 hours              127.0.0.1:8208->8208/tcp
llm9-proxy                                              Up 5 hours              127.0.0.1:8209->8209/tcp
msjarvis-rebuild-jarvis-pia-status-1                    Up 3 hours              127.0.0.1:8029->8029/tcp
msjarvis-rebuild-nbb_blood_brain_barrier-1              Up 6 days               127.0.0.1:8301->7001/tcp
msjarvis-rebuild-nbb_consciousness_containers-1         Up 6 days               127.0.0.1:8102->7002/tcp
msjarvis-rebuild-nbb_darwin_godel_machines-1            Up 5 hours              127.0.0.1:8302->7003/tcp
msjarvis-rebuild-nbb_heteroglobulin_transport-1         Up 6 days               127.0.0.1:8106->7006/tcp
msjarvis-rebuild-nbb_i_containers-1                     Up 6 days               127.0.0.1:8101->7005/tcp
msjarvis-rebuild-nbb_mother_carrie_protocols-1          Up 6 days               127.0.0.1:8107->7007/tcp
msjarvis-rebuild-nbb_pituitary_gland-1                  Up 11 hours             127.0.0.1:8108->80/tcp
msjarvis-rebuild-nbb_prefrontal_cortex-1                Up 6 days               127.0.0.1:8105->7005/tcp
msjarvis-rebuild-nbb_qualia_engine-1                    Up 6 days               127.0.0.1:8303->7008/tcp
msjarvis-rebuild-nbb_spiritual_maternal_integration-1   Up 6 days               127.0.0.1:8109->7009/tcp
msjarvis-rebuild-nbb_spiritual_root-1                   Up 6 days               127.0.0.1:8103->7003/tcp
msjarvis-rebuild-nbb_subconscious-1                     Up 6 days               127.0.0.1:8112->7011/tcp
mysql                                                   Up 5 hours              33060/tcp, 127.0.0.1:3307->3306/tcp
nbb_woah_algorithms                                     Up 6 hours              127.0.0.1:8104->8104/tcp
neo4j                                                   Up 5 hours              7473/tcp, 127.0.0.1:7687->7687/tcp, 127.0.0.1:7475->7474/tcp
psychological_rag_domain                                Up 47 hours             9006/tcp, 127.0.0.1:9006->8006/tcp
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ # 1. Inventory postgis-forensic fully (5 min)
docker exec postgis-forensic psql -U msjarvis -d msjarvis -c "\dt"
docker exec postgis-forensic psql -U msjarvis -d msjarvisgis -c "\dt"

# 2. Verify token-service can actually serve tokens (not just /health)
curl -s http://127.0.0.1:8088/token/generate \
  -H "Content-Type: application/json" \
  -d '{"user_id":"test","action":"test"}' | python3 -m json.tool

# 3. Check what the ms-coordinator and ms-indexer orphans actually do
curl -s http://127.0.0.1:$(docker inspect jarvis-ms-coordinator \
  --format '{{(index (index .HostConfig.PortBindings) "7260/tcp") 0}.HostPort}')/health \
  | python3 -m json.tool
              List of relations
  Schema  |      Name       | Type  | Owner  
----------+-----------------+-------+--------
 public   | spatial_ref_sys | table | jarvis
 public   | wv_locations    | table | jarvis
 topology | layer           | table | jarvis
 topology | topology        | table | jarvis
(4 rows)

                                     List of relations
 Schema |                              Name                               | Type  | Owner  
--------+-----------------------------------------------------------------+-------+--------
 public | 911centers_wvdem_032819_gcs84_attrs_raw                         | table | jarvis
 public | 911centers_wvdem_032819_utm83_attrs_raw                         | table | jarvis
 public | amtrackrails_federalrailroadadministration_200210_ll83_attrs_ra | table | jarvis
 public | amtrackrails_federalrailroadadministration_200210_utm83_attrs_r | table | jarvis
 public | amtrackrails_fra_200210_ll83_attrs_raw                          | table | jarvis
 public | amtrackrails_fra_200210_utm83_attrs_raw                         | table | jarvis
 public | attrs_files_list                                                | table | jarvis
 public | attrs_inventory_detailed                                        | table | jarvis
 public | authority_references                                            | table | jarvis
 public | benefit_case                                                    | table | jarvis
 public | blockgroups_census_2000_ll83_attrs_raw                          | table | jarvis
 public | blockgroups_census_2000_utm83_attrs_raw                         | table | jarvis
 public | blockgroups_census_201111_gcs83_attrs_raw                       | table | jarvis
 public | blockgroups_census_201111_utm83_attrs_raw                       | table | jarvis
 public | blockgroups_census_2020_utm83_attrs_raw                         | table | jarvis
 public | blockgroups_census_2020_wma84_attrs_raw                         | table | jarvis
 public | blocks_census_2020_utm83_attrs_raw                              | table | jarvis
 public | blocks_census_2020_wma84_attrs_raw                              | table | jarvis
 public | boundaryappalachianbasin_wvges_1996_utm83_attrs_raw             | table | jarvis
 public | bridges_attrs_raw                                               | table | jarvis
 public | building_metric_stage                                           | table | jarvis
 public | calderl_reg_ll83_attrs_raw                                      | table | jarvis
 public | citieswithpopulation_2500_census_201111_gcs83_attrs_raw         | table | jarvis
 public | citieswithpopulation_2500_census_201111_utm83_attrs_raw         | table | jarvis
 public | citieswithpopulationover10k_census_201111_gcs83_attrs_raw       | table | jarvis
 public | citieswithpopulationover10k_uscensus_1990_ll83_attrs_raw        | table | jarvis
 public | citieswithpopulationover10k_uscensus_1990_utm83_attrs_raw       | table | jarvis
 public | citieswithpopulationover2500_uscensus_1990_ll83_attrs_raw       | table | jarvis
 public | citieswithpopulationsover10k_census_2020_utm83_attrs_raw        | table | jarvis
 public | citieswithpopulationsover10k_census_2020_wma84_attrs_raw        | table | jarvis
 public | citieswithpopulationsover2500_census_2020_utm83_attrs_raw       | table | jarvis
 public | citieswithpopulationsover2500_census_2020_wma84_attrs_raw       | table | jarvis
 public | citieswithpopulatoinover2500_uscensus_1990_utm83_attrs_raw      | table | jarvis
 public | client_utility_account                                          | table | jarvis
 public | coals2_ll83_attrs_raw                                           | table | jarvis
 public | coals2_utm27_attrs_raw                                          | table | jarvis
 public | coals2_utm83_attrs_raw                                          | table | jarvis
 public | communityboundary_min_att_20250121_utm83_attrs_raw              | table | jarvis
 public | communityboundary_min_att_20250121_wma84_attrs_raw              | table | jarvis
 public | communityhealthproviders_wvhealthcareauthority_200802_u_attrs_r | table | jarvis
 public | communityhealthproviders_wvhealthcareauthority_200802_utm83_att | table | jarvis
 public | correctionalinstitutions_hsip_20091230_utm83_attrs_raw          | table | jarvis
 public | correctionalinstitutions_hsip_20091230_wgs84_attrs_raw          | table | jarvis
 public | countycityparkboundaries_20201104_utm83_attrs_raw               | table | jarvis
 public | countyseats_usgs_ll83_attrs_raw                                 | table | jarvis
 public | countyseats_usgs_utm83_attrs_raw                                | table | jarvis
 public | courthousescounty_manysources_200203_ll83_attrs_raw             | table | jarvis
 public | courthousescounty_manysources_200203_utm83_attrs_raw            | table | jarvis
 public | courthousesfederal_manysources_200203_ll83_attrs_raw            | table | jarvis
 public | courthousesfederal_manysources_200203_utm_attrs_raw             | table | jarvis
 public | cvfault_ll83_attrs_raw                                          | table | jarvis
 public | cvfault_utm27_attrs_raw                                         | table | jarvis
 public | cvfault_utm83_attrs_raw                                         | table | jarvis
 public | cvpoly_ll83_attrs_raw                                           | table | jarvis
 public | cvpoly_utm27_attrs_raw                                          | table | jarvis
 public | cvpoly_utm83_attrs_raw                                          | table | jarvis
 public | dams_usarmycorpsofengineers_200010_utm83_attrs_raw              | table | jarvis
 public | dams_usarmycropsofengineers_200010_ll83_attrs_raw               | table | jarvis
 public | damsnoncoal_usgs_2002_ll27_attrs_raw                            | table | jarvis
 public | damsnoncoal_usgs_2002_utm83_attrs_raw                           | table | jarvis
 public | empowermentzonesandenterprisecommunities_uscensus_2002__attrs_r | table | jarvis
 public | empowermentzonesandenterprisecommunities_uscensus_2002_utm83_at | table | jarvis
 public | empowermentzonesandenterprisecommunitiesbytract_uscens__attrs_r | table | jarvis
 public | empowermentzonesandenterprisecommunitiesbytractuscens30c72907at | table | jarvis
 public | evidence_documents                                              | table | jarvis
 public | excursionpassengertrains_wvdof_200102_ll83_attrs_raw            | table | jarvis
 public | excursionpassengertrains_wvdof_200102_utm83_attrs_raw           | table | jarvis
 public | facilities_epa_200203_ll83_attrs_raw                            | table | jarvis
 public | facilities_epa_200203_utm83_attrs_raw                           | table | jarvis
 public | fault_reg_ll83_attrs_raw                                        | table | jarvis
 public | faultgl_reg_ll83_attrs_raw                                      | table | jarvis
 public | features_attrs_raw                                              | table | jarvis
 public | fire_departments_attrs_raw                                      | table | jarvis
 public | fire_dept_wvdem_092017_utm83_attrs_raw                          | table | jarvis
 public | floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83_ | table | jarvis
 public | floodplainstructuresatrisk_usarmycorpsofengineers_20030_attrs_r | table | jarvis
 public | gbim_belief                                                     | table | jarvis
 public | gbim_belief_edges                                               | table | jarvis
 public | gbim_belief_evidence                                            | table | jarvis
 public | gbim_beliefs                                                    | table | jarvis
 public | gbim_entity_clusters                                            | table | jarvis
 public | gbim_entity_land_candidates                                     | table | jarvis
 public | gbim_evidence                                                   | table | jarvis
 public | gbim_full_points_raw                                            | table | jarvis
 public | gbim_layer_catalog                                              | table | jarvis
 public | gbim_layer_config                                               | table | jarvis
 public | gbim_layer_manifest                                             | table | jarvis
 public | gbim_source_epochs                                              | table | jarvis
 public | gbim_source_tables_used                                         | table | jarvis
 public | gbim_worldview_entity_backup_small                              | table | jarvis
 public | gbim_worldviews                                                 | table | jarvis
 public | gbimbeliefnormalized                                            | table | jarvis
 public | geographicalnamesonusgstopomaps_usgs_200601_ll27_attrs_raw      | table | jarvis
 public | geographicalnamesonusgstopomaps_usgs_200601_utm83_attrs_raw     | table | jarvis
 public | geographicnamesonusgstopomaps_current_usgs_20110801_ll83_attrs_ | table | jarvis
 public | geographicnamesonusgstopomaps_current_usgs_20110801_ll8_attrs_r | table | jarvis
 public | geographicnamesonusgstopomaps_current_usgs_20110801_utm83_attrs | table | jarvis
 public | geographicnamesonusgstopomaps_current_usgs_20110801_utm_attrs_r | table | jarvis
 public | geographicnamesonusgstopomaps_historical_usgs_20110801__attrs_r | table | jarvis
 public | geographicnamesonusgstopomaps_historical_usgs_20110801_ll83_att | table | jarvis
 public | geographicnamesonusgstopomaps_historical_usgs_20110801_utm83_at | table | jarvis
 public | geographicnamesonusgstopomaps_usgs_20110801_ll83_attrs_raw      | table | jarvis
 public | geographicnamesonusgstopomaps_usgs_20110801_utm83_attrs_raw     | table | jarvis
 public | geolgyl_reg_ll83_attrs_raw                                      | table | jarvis
 public | geolgyp_reg_ll83_attrs_raw                                      | table | jarvis
 public | geospatial_layers                                               | table | jarvis
 public | geotextl_reg_ll83_attrs_raw                                     | table | jarvis
 public | glacagl_reg_ll83_attrs_raw                                      | table | jarvis
 public | glacal_reg_ll83_attrs_raw                                       | table | jarvis
 public | hazardmitigationbuyout_20250929_polygons_utm83_attrs_raw        | table | jarvis
 public | hazardmitigationbuyout_20250929_polygons_wma84_attrs_raw        | table | jarvis
 public | healthruralfacilities_manysources_utm83_attrs_raw               | table | jarvis
 public | highered_wvemd_072420_utm83_attrs_raw                           | table | jarvis
 public | highered_wvemd_072420_wgc84_attrs_raw                           | table | jarvis
 public | historicalaerialphotographycountycoverage_wvgistc_utm83_attrs_r | table | jarvis
 public | hospitals_attrs_raw                                             | table | jarvis
 public | hospitals_wvdem_040519_gcs84_attrs_raw                          | table | jarvis
 public | hospitals_wvdem_040519_utm83_attrs_raw                          | table | jarvis
 public | hospitalswvdem040519utm83_attrs_raw                             | table | jarvis
 public | impact_reg_ll83_attrs_raw                                       | table | jarvis
 public | indexgrid15minutequads_wvgistc_ll83_attrs_raw                   | table | jarvis
 public | indexgrid15minutequads_wvgistc_utm83_attrs_raw                  | table | jarvis
 public | indexgrid15minutewithcounties_wvgistc_utm27_attrs_raw           | table | jarvis
 public | indexgrid1minutequads_wvgistc_ll83_attrs_raw                    | table | jarvis
 public | industrialbuildings_wvdo_200807_utm83_attrs_raw                 | table | jarvis
 public | industrialparks_wvdo_200078_utm83_attrs_raw                     | table | jarvis
 public | industrialsites_wvdo_200807_utm83_attrs_raw                     | table | jarvis
 public | inedexgrid1minutequads_wvgistc_utm83_attrs_raw                  | table | jarvis
 public | intake_submissions                                              | table | jarvis
 public | intermodalterminalfacilities_usdot_1997_ll83_attrs_raw          | table | jarvis
 public | intermodalterminalfacilities_usdot_1997_utm83_attrs_raw         | table | jarvis
 public | layer_config                                                    | table | jarvis
 public | libraries_manysources_2001_ll27_attrs_raw                       | table | jarvis
 public | libraries_manysources_2001_utm83_attrs_raw                      | table | jarvis
 public | majorriversandlakesline_nhd_2002_ll83_attrs_raw                 | table | jarvis
 public | majorriversandlakesline_nhd_2002_utm83_attrs_raw                | table | jarvis
 public | majorriversandlakespolygon_nhd_2002_poly_ll83_attrs_raw         | table | jarvis
 public | majorriversandlakespolygon_nhd_2002_utm83_attrs_raw             | table | jarvis
 public | manufacturingandbusiness_wvdo_200803_utm83_attrs_raw            | table | jarvis
 public | metfacp_reg_ll83_attrs_raw                                      | table | jarvis
 public | metropolitanandmicropolitanstatisticalareas_census_2011_attrs_r | table | jarvis
 public | metropolitanandmicropolitanstatisticalareas_census_2020_attrs_r | table | jarvis
 public | metropolitanandmicropolitanstatisticalareas_census_2020_utm83_a | table | jarvis
 public | metropolitanandmicropolitanstatisticalareas_census_2020_wma84_a | table | jarvis
 public | metropolitanandmicropolitanstatisticalareascensus201111gcs83att | table | jarvis
 public | metropolitanandmicropolitanstatisticalareascensus201111utm83att | table | jarvis
 public | metropolitanstatisticalareas_uscensus_199901_ll83_attrs_raw     | table | jarvis
 public | metropolitanstatisticalareas_uscensus_199901_utm83_attrs_raw    | table | jarvis
 public | mineraloperations_usgs_200204_ll83_attrs_raw                    | table | jarvis
 public | mineraloperations_usgs_200204_utm83_attrs_raw                   | table | jarvis
 public | minesabandonedlandsline_wvdep_1996_noprojectoin_attrs_raw       | table | jarvis
 public | minesabandonedlandspoint_wvdep_1996_noprojection_attrs_raw      | table | jarvis
 public | minesabandonedlandspolygon_wvdep_1996_noprojection_attrs_raw    | table | jarvis
 public | ms_jarvis_learning_log                                          | table | jarvis
 public | nationalatlasstreams_usgs_199903_ll83_attrs_raw                 | table | jarvis
 public | nationalatlasstreams_usgs_199903_utm83_attrs_raw                | table | jarvis
 public | nationalregister_point_20200923_attrs_raw                       | table | jarvis
 public | nationalregister_point_20200923_utm27_attrs_raw                 | table | jarvis
 public | nationalregisterofhistoricplacespoints_nationalparkser__attrs_r | table | jarvis
 public | nationalregisterofhistoricplacespoints_natoinalpakrser__attrs_r | table | jarvis
 public | nationalregisterofhistoricplacespolygons_nationaparkse__attrs_r | table | jarvis
 public | nationalwaterwaynetwork_usarmycorpsofengineers_2001_ll83_attrs_ | table | jarvis
 public | nationalwaterwaynetwork_usarmycorpsofengineers_2001_ll8_attrs_r | table | jarvis
 public | nationalwaterwaynetwork_usarmycorpsofengineers_2001_utm83_attrs | table | jarvis
 public | nationalwaterwaynetwork_usarmycorpsofengineers_2001_utm_attrs_r | table | jarvis
 public | nationalwaterwaynetworkports_usarmycorpsofengineers_2001_ll83_a | table | jarvis
 public | nationalwaterwaynetworkports_usarmycorpsofengineers_2001_utm83_ | table | jarvis
 public | nationalwaterwaynetworkports_usarmycorpsofengineers_200_attrs_r | table | jarvis
 public | nationaregisterofhistoricplacespoints_nationalparkserv__attrs_r | table | jarvis
 public | nationaregisterofhistoricplacespolygons_nationalparkse__attrs_r | table | jarvis
 public | natoinalregisterofhistoricplacespoints_nationalparkser__attrs_r | table | jarvis
 public | naviagablewaterways_usarmycropsofengineers_2006_utm83_attrs_raw | table | jarvis
 public | navigablewaterwaysrivermiles_usarmycropsofengineers_2006_utm83_ | table | jarvis
 public | navigablewaterwaysrivermiles_usarmycropsofengineers_200_attrs_r | table | jarvis
 public | navigablewaterwaysstructures_usarmycorpsofengineers_2006_utm83_ | table | jarvis
 public | navigablewaterwaysstructures_usarmycorpsofengineers_200_attrs_r | table | jarvis
 public | nursinghomes_wvdem_041219_gcs84_attrs_raw                       | table | jarvis
 public | nursinghomes_wvdem_041219_utm83_attrs_raw                       | table | jarvis
 public | officebuildings_wvdo_200807_utm83_attrs_raw                     | table | jarvis
 public | paroleoffices_manysources_2008_utm83_attrs_raw                  | table | jarvis
 public | paroleoffices_manysources_2008_wgs84_attrs_raw                  | table | jarvis
 public | placesofworship_hsip_20080723_utm83_attrs_raw                   | table | jarvis
 public | placesofworship_hsip_20080723_wgs84_attrs_raw                   | table | jarvis
 public | policedept_wvdem_012319_gcs84_attrs_raw                         | table | jarvis
 public | policedept_wvdem_012319_utm83_attrs_raw                         | table | jarvis
 public | populatedplaces_census_201112_utm83_attrs_raw                   | table | jarvis
 public | populatedplaces_census_20112_gcs83_attrs_raw                    | table | jarvis
 public | populatedplaces_census_2020_utm83_attrs_raw                     | table | jarvis
 public | populatedplaces_census_2020_wma84_attrs_raw                     | table | jarvis
 public | populatedplaces_uscensus_1990_ll83_attrs_raw                    | table | jarvis
 public | populatedplaces_uscensus_1990_utm83_attrs_raw                   | table | jarvis
 public | populationdatablockgroups_uscensus_2000_ll83_attrs_raw          | table | jarvis
 public | populationdatablockgroups_uscensus_2000_utm83_attrs_raw         | table | jarvis
 public | pow_wvgistc_062919_utm83_attrs_raw                              | table | jarvis
 public | pow_wvgistc_062919_wgs84_attrs_raw                              | table | jarvis
 public | program                                                         | table | jarvis
 public | program_authority_links                                         | table | jarvis
 public | program_catalog                                                 | table | jarvis
 public | program_eligibility                                             | table | jarvis
 public | program_entity_links                                            | table | jarvis
 public | program_evidence_links                                          | table | jarvis
 public | program_income_limit_rules                                      | table | jarvis
 public | program_income_source_policy                                    | table | jarvis
 public | program_manual_rule_links                                       | table | jarvis
 public | program_name_crosswalk                                          | table | jarvis
 public | program_target_config                                           | table | jarvis
 public | publichealthdepts_hsip_20091229_gcs83_attrs_raw                 | table | jarvis
 public | publichealthdepts_hsip_20091229_utm83_attrs_raw                 | table | jarvis
 public | railnetworkregion_usdot_200203_ll83_attrs_raw                   | table | jarvis
 public | railnetworkregion_usdot_200203_utm83_attrs_raw                  | table | jarvis
 public | railnetworkwv_usdot_200203_ll83_attrs_raw                       | table | jarvis
 public | railnetworkwv_usdot_200203_utm83_attrs_raw                      | table | jarvis
 public | railroads_rahalltransportationinstitute_2005_utm83_attrs_raw    | table | jarvis
 public | realtimestreamflowstations_usgs_200012_ll27_attrs_raw           | table | jarvis
 public | realtimestreamflowstations_usgs_200012_utm27_attrs_raw          | table | jarvis
 public | realtimestreamflowstations_usgs_200012_utm83_attrs_raw          | table | jarvis
 public | recreationalwwtrails_ofwv_20151117_utm83_attrs_raw              | table | jarvis
 public | regionalplanninganddevelopmentcouncil_wvdo_1971_ll83_attrs_raw  | table | jarvis
 public | regionalplanninganddevelopmentcouncil_wvdo_1971_utm83_attrs_raw | table | jarvis
 public | resource_county_coverage                                        | table | jarvis
 public | resource_eligibility                                            | table | jarvis
 public | sewertreatmentplants_wvdep_200203_utm83_attrs_raw               | table | jarvis
 public | solidwastefacilities_wvdep_200202_ll83_attrs_raw                | table | jarvis
 public | solidwastefacilities_wvdep_200202_utm83_attrs_raw               | table | jarvis
 public | springs_wvges_1986_ll83_attrs_raw                               | table | jarvis
 public | springs_wvges_1986_utm83_attrs_raw                              | table | jarvis
 public | stateofwvhousedistricts_wvlegislativeservices_2010_attrs_raw    | table | jarvis
 public | stateofwvsenatedistricts_wvlegislativeservices_2010_attrs_raw   | table | jarvis
 public | states_region_ll83_attrs_raw                                    | table | jarvis
 public | structurepointsnorth_samb_2003_utm83_attrs_raw                  | table | jarvis
 public | structurepointssouth_samb_2003_utm83_attrs_raw                  | table | jarvis
 public | structurepolygons_samb_2003_utm83_attrs_raw                     | table | jarvis
 public | summits_gistc_052012_utm83_shp_attrs_raw                        | table | jarvis
 public | summits_gistc_052012_wgs84_shp_attrs_raw                        | table | jarvis
 public | surveycontrol_nationalgeodeticsurvey_102011_gcs83_attrs_raw     | table | jarvis
 public | timberremovalvolume_usfs_1996_utm83_attrs_raw                   | table | jarvis
 public | tmp_building_block_nearest_sample                               | table | jarvis
 public | towers_wvpublicbroadcasting_2002_ll83_attrs_raw                 | table | jarvis
 public | towers_wvpublicbroadcasting_2002_utm83_attrs_raw                | table | jarvis
 public | towersam_fcc_200202_utm83_attrs_raw                             | table | jarvis
 public | towersasr_fcc_200202_ll83_attrs_raw                             | table | jarvis
 public | towersasr_fcc_200202_utm83_attrs_raw                            | table | jarvis
 public | towerscellular_fcc_200202_ll83_attrs_raw                        | table | jarvis
 public | towerscellular_fcc_200202_utm83_attrs_raw                       | table | jarvis
 public | towersfm_fcc_200202_utm83_attrs_raw                             | table | jarvis
 public | towersmicrowave_fcc_200202_ll83_attrs_raw                       | table | jarvis
 public | towersmicrowave_fcc_200202_utm83_attrs_raw                      | table | jarvis
 public | towerspager_fcc_200202_ll83_attrs_raw                           | table | jarvis
 public | towerspager_fcc_200202_utm83_attrs_raw                          | table | jarvis
 public | towersprivate_fcc_200202_ll83_attrs_raw                         | table | jarvis
 public | towersprivate_fcc_200202_utm83_attrs_raw                        | table | jarvis
 public | uei_registry                                                    | table | jarvis
 public | user_compliance_task                                            | table | jarvis
 public | utility_discount_enrollment                                     | table | jarvis
 public | veteransaffairsfacilities_manysources_200503_utm83_attrs_raw    | table | jarvis
 public | veteransaffairsfacilities_manysources_200503_wgs84_attrs_raw    | table | jarvis
 public | votingdistrictswv_legislativeservices_2002_ll83_attrs_raw       | table | jarvis
 public | votingdistrictswv_legislativeservices_2002_utm83_attrs_raw      | table | jarvis
 public | votingdistrictswv_uscensus_2000_utm83_attrs_raw                 | table | jarvis
 public | weatherstations_nationalclimatedatacenter_1999_gcs83_attrs_raw  | table | jarvis
 public | weatherstations_nationalclimatedatacenter_1999_utm27_attrs_raw  | table | jarvis
 public | windenergyresource_nationalrenewableenergylab_200901_ut_attrs_r | table | jarvis
 public | windenergyresource_nationalrenewableenergylab_200901_utm83_attr | table | jarvis
 public | windenergyresource_nationalrenewableenergylab_200901_wg_attrs_r | table | jarvis
 public | windenergyresource_nationalrenewableenergylab_200901_wgs84_attr | table | jarvis
 public | workforceinvestmentareas_wvgistc_200208_ll83_attrs_raw          | table | jarvis
 public | wv_county_boundaries_24k_topo_updated_2022_utm83_attrs_raw      | table | jarvis
 public | wv_county_names                                                 | table | jarvis
 public | wv_income_manual_income_limits                                  | table | jarvis
 public | wv_income_manual_income_sources                                 | table | jarvis
 public | wv_income_manual_income_treatment                               | table | jarvis
 public | wv_income_manual_income_treatment_extended                      | table | jarvis
 public | wv_income_manual_rules                                          | table | jarvis
 public | wv_microsoft_20180207_utm17n83_attrs_raw                        | table | jarvis
 public | wv_tax_districts_ll83_attrs_raw                                 | table | jarvis
 public | wv_tax_districts_utm83_attrs_raw                                | table | jarvis
 public | wv_tax_districts_wma84_attrs_raw                                | table | jarvis
 public | wvgistc_building_footprints_attrs_raw                           | table | jarvis
 public | wvgistcbuildingfootprints_attrs_raw                             | table | jarvis
 public | wvgistcbuildingfootprintsattrsraw                               | table | jarvis
 public | wvstatebounadary100k_usgs_200203_utm83_attrs_raw                | table | jarvis
 public | wvstateboundary100k_usgs_200203_ll83_attrs_raw                  | table | jarvis
 public | wvstateboundary24k_usgs_200203_ll83_attrs_raw                   | table | jarvis
 public | wvstateboundary24k_usgs_200203_utm83_attrs_raw                  | table | jarvis
 public | wvstatehousedistricts_manysources_1992_ll83_attrs_raw           | table | jarvis
 public | wvstatehousedistricts_manysources_1992_utm83_attrs_raw          | table | jarvis
 public | wvstatehousedistricts_manysources_2002_ll83_attrs_raw           | table | jarvis
 public | wvstatehousedistricts_manysources_2002_utm83_attrs_raw          | table | jarvis
 public | wvstatehousedistricts_wvlegislativeservices_2020_utm83_attrs_ra | table | jarvis
 public | wvstatesenatedistricts_manysources_1992_ll83_attrs_raw          | table | jarvis
 public | wvstatesenatedistricts_manysources_1992_utm83_attrs_raw         | table | jarvis
 public | wvstatesenatedistricts_manysources_2002_ll83_attrs_raw          | table | jarvis
 public | wvstatesenatedistricts_manysources_2002_utm83_attrs_raw         | table | jarvis
 public | wvstatesenatedistricts_wvlegislativeservices_2020_utm83_attrs_r | table | jarvis
 public | zcta_county_rel                                                 | table | jarvis
 public | zipcodetabulationarea_census_2020_utm83_attrs_raw               | table | jarvis
 public | zipcodetabulationarea_census_2020_wma84_attrs_raw               | table | jarvis
(297 rows)

{
    "detail": "Not Found"
}
template parsing error: template: :1: unexpected "}" in operand
Expecting value: line 1 column 1 (char 0)
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ 

