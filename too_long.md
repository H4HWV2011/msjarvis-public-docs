
(.venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ # 1. See the raw auth error
curl -s -X POST http://localhost:8096/auth/login \
  --data-urlencode "username=cakidd" \
  --data-urlencode "password=REAL_PASSWORD_HERE"

# 2. Find what DB the auth API uses
docker ps | grep -E "postgres|db|auth"

# 3. Check geospatialfeatures count
curl -s "http://localhost:8002/api/v2/tenants/default_tenant/databases/default_database/collections/5d72dd26-f19c-42d1-bdfc-3820efc2436d/count"

# 4. Test embedding directly
curl -s http://localhost:11434/api/embeddings \
  -H "Content-Type: application/json" \
  -d '{"model":"all-minilm","prompt":"Fayette County hospital"}' | jq '{len: (.embedding | length)}'
{"detail":"Invalid username or password"}35f3812c7409   msjarvis-rebuild-jarvis-auth-api                      "python -m uvicorn a…"   13 minutes ago   Up 13 minutes           127.0.0.1:8096->8091/tcp                                                                                       jarvis-auth-api
4da0fedbc4b2   msjarvis-rebuild-jarvis-rag-router                    "uvicorn rag_query_r…"   31 hours ago     Up 22 hours             8003/tcp, 127.0.0.1:5015->5001/tcp                                                                             jarvis-rag-router
14fe811db8dd   jarvis-main-brain:latest                              "python -m uvicorn m…"   31 hours ago     Up 22 hours             127.0.0.1:8050->8050/tcp                                                                                       jarvis-main-brain
2cb6c465159e   chromadb/chroma:latest                                "dumb-init -- chroma…"   31 hours ago     Up 22 hours (healthy)   127.0.0.1:8002->8000/tcp                                                                                       jarvis-chroma
823b7f10db0d   msjarvis-rebuild-llm7-proxy                           "python -m uvicorn l…"   31 hours ago     Up 22 hours             127.0.0.1:8207->8207/tcp                                                                                       llm7-proxy
0ad75f6db901   msjarvis-rebuild-llm9-proxy                           "python -m uvicorn l…"   31 hours ago     Up 22 hours             127.0.0.1:8209->8209/tcp                                                                                       llm9-proxy
a6a83e45cc73   postgis/postgis:15-3.4                                "docker-entrypoint.s…"   31 hours ago     Up 22 hours             127.0.0.1:5435->5432/tcp                                                                                       jarvis-local-resources-db
ce1087b5db06   msjarvis-rebuild-llm10-proxy                          "python -m uvicorn l…"   31 hours ago     Up 22 hours             127.0.0.1:8210->8210/tcp                                                                                       llm10-proxy
0{
  "len": 384
}
(.venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ # 1. See what DB connection string auth_api actually uses
docker exec jarvis-auth-api env | grep -i "db\|postgres\|database\|dsn\|conn"

# 2. Check ALL tables in local_resources to find where users might be stored
docker exec jarvis-local-resources-db psql -U postgres -d local_resources \
  -c "\dt"

# 3. Also check msjarvisgis — it's owner 'msjarvis', not postgres
docker exec jarvis-local-resources-db psql -U postgres -d msjarvisgis \
  -c "\dt"
DATABASE_URL=postgresql://postgres:postgres@jarvis-local-resources-db:5432/local_resources
POSTGRES_DSN=postgresql://postgres@jarvis-local-resources-db:5432/msjarvisgis
                     List of relations
 Schema |              Name              | Type  |  Owner   
--------+--------------------------------+-------+----------
 public | building_parcel_county_tax_mat | table | postgres
 public | building_profile               | table | postgres
 public | building_samb_link             | table | postgres
 public | building_zip6_to_zip5          | table | postgres
 public | building_zip6_to_zip6poly      | table | postgres
 public | community_resources            | table | postgres
 public | conversation_beliefs           | table | postgres
 public | county_lookup                  | table | postgres
 public | enriched_buildings_with_samb   | table | postgres
 public | equity_timesheet               | table | postgres
 public | equity_timesheet_ctx_backup    | table | postgres
 public | founder_tokens                 | table | postgres
 public | gbim_belief_normalized         | table | postgres
 public | gbim_worldview_entity          | table | postgres
 public | gbim_zcta_2020                 | table | postgres
 public | imm_binder4_raw                | table | postgres
 public | local_resources                | table | postgres
 public | local_resources_index          | table | postgres
 public | mountainshares_balances        | table | postgres
 public | mountainshares_ledger          | table | postgres
 public | mountainshares_participation   | table | postgres
 public | ms_governance_log              | table | postgres
 public | ms_participation               | table | postgres
 public | ms_reserve_bands               | table | postgres
 public | ms_treasury                    | table | postgres
 public | ms_user_profile                | table | postgres
 public | spatial_ref_sys                | table | postgres
 public | spatial_role_scopes            | table | postgres
 public | travel_regions                 | table | postgres
 public | ueid_immutable_security        | table | postgres
 public | us_counties                    | table | postgres
 public | us_zips                        | table | postgres
 public | user_longterm_memory           | table | postgres
 public | wv_address_aliases             | table | postgres
 public | wv_address_dual                | table | postgres
 public | wv_address_points_raw          | table | postgres
 public | wv_address_zones               | table | postgres
 public | wv_aml_lines                   | table | postgres
 public | wv_aml_points                  | table | postgres
 public | wv_aml_polygons                | table | postgres
 public | wv_buildings                   | table | postgres
 public | wv_counties                    | table | postgres
 public | wv_county_boundaries_raw       | table | postgres
 public | wv_county_lookup               | table | postgres
 public | wv_ems_stations                | table | postgres
 public | wv_fire_stations               | table | postgres
 public | wv_fire_stations_clean         | table | postgres
 public | wv_floodplain_structures       | table | postgres
 public | wv_gis_features                | table | postgres
 public | wv_hazard_buyouts              | table | postgres
 public | wv_hospitals                   | table | postgres
 public | wv_industrial_buildings        | table | postgres
 public | wv_industrial_buildings_raw    | table | postgres
 public | wv_mineral_operations          | table | postgres
 public | wv_municipalities              | table | postgres
 public | wv_office_buildings            | table | postgres
 public | wv_office_buildings_raw        | table | postgres
 public | wv_parcels                     | table | postgres
 public | wv_samb_north                  | table | postgres
 public | wv_samb_north_raw              | table | postgres
 public | wv_samb_poly_raw               | table | postgres
 public | wv_samb_south                  | table | postgres
 public | wv_samb_south_raw              | table | postgres
 public | wv_tax_districts               | table | postgres
 public | wv_tax_districts_poly          | table | postgres
 public | wv_tax_districts_raw           | table | postgres
 public | wv_wvgistc_buildings           | table | postgres
 public | wv_wvgistc_buildings_raw       | table | postgres
 public | wv_zip_codes                   | table | postgres
 public | wv_zip_zcta_raw                | table | postgres
 public | zcta_county_rel                | table | postgres
 public | zip6_regions                   | table | postgres
(72 rows)

                                       List of relations
  Schema  |                              Name                               | Type  |  Owner   
----------+-----------------------------------------------------------------+-------+----------
 public   | 911centers_wvdem_032819_gcs84                                   | table | msjarvis
 public   | 911centers_wvdem_032819_utm83                                   | table | msjarvis
 public   | addrfeat                                                        | table | msjarvis
 public   | amtrackrails_federalrailroadadministration_200210_ll83          | table | msjarvis
 public   | bg                                                              | table | msjarvis
 public   | blockgroups_census_2000_ll83                                    | table | msjarvis
 public   | blockgroups_census_2000_utm83                                   | table | msjarvis
 public   | blockgroups_census_201111_gcs83                                 | table | msjarvis
 public   | blockgroups_census_201111_utm83                                 | table | msjarvis
 public   | blockgroups_census_2020_utm83                                   | table | msjarvis
 public   | blockgroups_census_2020_wma84                                   | table | msjarvis
 public   | blocks_census_2020_utm83                                        | table | msjarvis
 public   | blocks_census_2020_wma84                                        | table | msjarvis
 public   | boundaryappalachianbasin_wvges_1996_utm83                       | table | msjarvis
 public   | bridges                                                         | table | msjarvis
 public   | calderl_reg_ll83                                                | table | msjarvis
 public   | census_block_groups_2020_utm83                                  | table | msjarvis
 public   | census_blocks_2020_utm83                                        | table | msjarvis
 public   | census_cities_over10k_2020_utm83                                | table | msjarvis
 public   | census_cities_over2500_2020_utm83                               | table | msjarvis
 public   | census_county_boundaries_2021_utm83                             | table | postgres
 public   | census_designated_places_2021_utm83                             | table | msjarvis
 public   | census_empowerment_zones_2002_utm83                             | table | postgres
 public   | census_historical_pop_by_county_2006_utm83                      | table | postgres
 public   | census_incorporated_places_2021_utm83                           | table | postgres
 public   | census_metro_micro_areas_2020_utm83                             | table | postgres
 public   | census_minor_civil_divisions_2020_utm83                         | table | postgres
 public   | census_misc_transportation_2000_utm83                           | table | postgres
 public   | census_pop_change_communities_2020_utm83                        | table | postgres
 public   | census_pop_change_counties_2020_utm83                           | table | postgres
 public   | census_populated_places_2020_utm83                              | table | postgres
 public   | census_railroads_2023_utm83                                     | table | postgres
 public   | census_roads_2023_utm83                                         | table | postgres
 public   | census_streams_waterbodies_2023_utm83                           | table | postgres
 public   | census_tl_2020_54_bg                                            | table | msjarvis
 public   | census_tl_2020_54_tabblock20                                    | table | msjarvis
 public   | census_tl_2020_us_county                                        | table | msjarvis
 public   | census_tl_2020_us_zcta510                                       | table | msjarvis
 public   | census_tl_2020_us_zcta520                                       | table | msjarvis
 public   | census_tracts_2020_utm83                                        | table | msjarvis
 public   | census_urban_areas_100k_2020_utm83                              | table | postgres
 public   | census_zcta_2020_utm83                                          | table | postgres
 public   | citieswithpopulation_2500_census_201111_gcs83                   | table | msjarvis
 public   | citieswithpopulation_2500_census_201111_utm83                   | table | msjarvis
 public   | citieswithpopulationover10k_census_201111_gcs83                 | table | msjarvis
 public   | citieswithpopulationover10k_uscensus_1990_ll83                  | table | msjarvis
 public   | citieswithpopulationover2500_uscensus_1990_ll83                 | table | msjarvis
 public   | citieswithpopulationsover10k_census_2020_utm83                  | table | msjarvis
 public   | citieswithpopulationsover2500_census_2020_utm83                 | table | msjarvis
 public   | citieswithpopulatoinover2500_uscensus_1990_utm83                | table | msjarvis
 public   | coals2_ll83                                                     | table | msjarvis
 public   | coals2_utm27                                                    | table | msjarvis
 public   | coals2_utm83                                                    | table | msjarvis
 public   | communityboundary_min_att_20250121_utm83                        | table | msjarvis
 public   | communityboundary_min_att_20250121_wma84                        | table | msjarvis
 public   | communityhealthproviders_wvhealthcareauthority_200802_utm83     | table | msjarvis
 public   | conversation_history                                            | table | msjarvis
 public   | correctionalinstitutions_hsip_20091230_utm83                    | table | msjarvis
 public   | correctionalinstitutions_hsip_20091230_wgs84                    | table | msjarvis
 public   | county                                                          | table | msjarvis
 public   | countycityparkboundaries_20201104_utm83                         | table | msjarvis
 public   | countyseats_usgs_ll83                                           | table | msjarvis
 public   | countyseats_usgs_utm83                                          | table | msjarvis
 public   | courthousescounty_manysources_200203_ll83                       | table | msjarvis
 public   | courthousescounty_manysources_200203_utm83                      | table | msjarvis
 public   | courthousesfederal_manysources_200203_ll83                      | table | msjarvis
 public   | courthousesfederal_manysources_200203_utm                       | table | msjarvis
 public   | cousub                                                          | table | msjarvis
 public   | cvfault_ll83                                                    | table | msjarvis
 public   | cvfault_utm27                                                   | table | msjarvis
 public   | cvfault_utm83                                                   | table | msjarvis
 public   | cvpoly_ll83                                                     | table | msjarvis
 public   | cvpoly_utm27                                                    | table | msjarvis
 public   | cvpoly_utm83                                                    | table | msjarvis
 public   | dams_usarmycorpsofengineers_200010_utm83                        | table | msjarvis
 public   | dams_usarmycropsofengineers_200010_ll83                         | table | msjarvis
 public   | damsnoncoal_usgs_2002_ll27                                      | table | msjarvis
 public   | edges                                                           | table | msjarvis
 public   | empowermentzonesandenterprisecommunities_uscensus_2002_utm83    | table | msjarvis
 public   | empowermentzonesandenterprisecommunitiesbytract_uscens_30c72907 | table | msjarvis
 public   | equity_timesheet                                                | table | postgres
 public   | excursionpassengertrains_wvdof_200102_ll83                      | table | msjarvis
 public   | excursionpassengertrains_wvdof_200102_utm83                     | table | msjarvis
 public   | faces                                                           | table | msjarvis
 public   | facilities_epa_200203_ll83                                      | table | msjarvis
 public   | facilities_epa_200203_utm83                                     | table | msjarvis
 public   | fault_reg_ll83                                                  | table | msjarvis
 public   | faultgl_reg_ll83                                                | table | msjarvis
 public   | fayette_parcels                                                 | table | msjarvis
 public   | features                                                        | table | msjarvis
 public   | fire_departments                                                | table | msjarvis
 public   | fire_dept_wvdem_092017_utm83                                    | table | msjarvis
 public   | floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83  | table | msjarvis
 public   | founder_tokens                                                  | table | postgres
 public   | gbim_entities                                                   | table | msjarvis
 public   | geographicalnamesonusgstopomaps_usgs_200601_ll27                | table | msjarvis
 public   | geographicnamesonusgstopomaps_current_usgs_20110801_ll83        | table | msjarvis
 public   | geographicnamesonusgstopomaps_historical_usgs_20110801_ll83     | table | msjarvis
 public   | geographicnamesonusgstopomaps_usgs_20110801_ll83                | table | msjarvis
 public   | geolgyl_reg_ll83                                                | table | msjarvis
 public   | geolgyp_reg_ll83                                                | table | msjarvis
 public   | geospatial_features                                             | table | postgres
 public   | geotextl_reg_ll83                                               | table | msjarvis
 public   | glacagl_reg_ll83                                                | table | msjarvis
 public   | glacal_reg_ll83                                                 | table | msjarvis
 public   | hazardmitigationbuyout_20250929_polygons_utm83                  | table | msjarvis
 public   | healthruralfacilities_manysources_utm83                         | table | msjarvis
 public   | highered_wvemd_072420_utm83                                     | table | msjarvis
 public   | highered_wvemd_072420_wgc84                                     | table | msjarvis
 public   | historicalaerialphotographycountycoverage_wvgistc_utm83         | table | msjarvis
 public   | hospitals                                                       | table | msjarvis
 public   | hospitals_wvdem_040519_gcs84                                    | table | msjarvis
 public   | hospitals_wvdem_040519_utm83                                    | table | msjarvis
 public   | impact_reg_ll83                                                 | table | msjarvis
 public   | indexgrid15minutequads_wvgistc_ll83                             | table | msjarvis
 public   | indexgrid15minutequads_wvgistc_utm83                            | table | msjarvis
 public   | indexgrid15minutewithcounties_wvgistc_utm27                     | table | msjarvis
 public   | indexgrid1minutequads_wvgistc_ll83                              | table | msjarvis
 public   | industrialbuildings_wvdo_200807_utm83                           | table | msjarvis
 public   | industrialparks_wvdo_200078_utm83                               | table | msjarvis
 public   | industrialsites_wvdo_200807_utm83                               | table | msjarvis
 public   | inedexgrid1minutequads_wvgistc_utm83                            | table | msjarvis
 public   | interaction_provenance_immutable                                | table | postgres
 public   | interactions                                                    | table | postgres
 public   | intermodalterminalfacilities_usdot_1997_ll83                    | table | msjarvis
 public   | intermodalterminalfacilities_usdot_1997_utm83                   | table | msjarvis
 public   | libraries_manysources_2001_ll27                                 | table | msjarvis
 public   | libraries_manysources_2001_utm83                                | table | msjarvis
 public   | majorriversandlakesline_nhd_2002_ll83                           | table | msjarvis
 public   | majorriversandlakesline_nhd_2002_utm83                          | table | msjarvis
 public   | majorriversandlakespolygon_nhd_2002_poly_ll83                   | table | msjarvis
 public   | majorriversandlakespolygon_nhd_2002_utm83                       | table | msjarvis
 public   | manufacturingandbusiness_wvdo_200803_utm83                      | table | msjarvis
 public   | metfacp_reg_ll83                                                | table | msjarvis
 public   | metropolitanandmicropolitanstatisticalareas_census_201111_gcs83 | table | msjarvis
 public   | metropolitanstatisticalareas_uscensus_199901_ll83               | table | msjarvis
 public   | mineraloperations_usgs_200204_ll83                              | table | msjarvis
 public   | mineraloperations_usgs_200204_utm83                             | table | msjarvis
 public   | minesabandonedlandsline_wvdep_1996_noprojectoin                 | table | msjarvis
 public   | minesabandonedlandspoint_wvdep_1996_noprojection                | table | msjarvis
 public   | minesabandonedlandspolygon_wvdep_1996_noprojection              | table | msjarvis
 public   | mountainshares_balances                                         | table | postgres
 public   | mountainshares_participants                                     | table | postgres
 public   | nationalatlasstreams_usgs_199903_ll83                           | table | msjarvis
 public   | nationalatlasstreams_usgs_199903_utm83                          | table | msjarvis
 public   | nationalregister_point_20200923                                 | table | msjarvis
 public   | nationalregister_point_20200923_utm27                           | table | msjarvis
 public   | nationalregisterofhistoricplacespoints_nationalparkser_45ec46d0 | table | msjarvis
 public   | nationalregisterofhistoricplacespolygons_nationaparkse_b9d30a70 | table | msjarvis
 public   | nationalwaterwaynetwork_usarmycorpsofengineers_2001_ll83        | table | msjarvis
 public   | nationalwaterwaynetworkports_usarmycorpsofengineers_2001_ll83   | table | msjarvis
 public   | nationaregisterofhistoricplacespoints_nationalparkserv_ba8eebd5 | table | msjarvis
 public   | nationaregisterofhistoricplacespolygons_nationalparkse_cab42150 | table | msjarvis
 public   | natoinalregisterofhistoricplacespoints_nationalparkser_ca43510e | table | msjarvis
 public   | naviagablewaterways_usarmycropsofengineers_2006_utm83           | table | msjarvis
 public   | navigablewaterwaysrivermiles_usarmycropsofengineers_2006_utm83  | table | msjarvis
 public   | navigablewaterwaysstructures_usarmycorpsofengineers_2006_utm83  | table | msjarvis
 public   | nursinghomes_wvdem_041219_gcs84                                 | table | msjarvis
 public   | nursinghomes_wvdem_041219_utm83                                 | table | msjarvis
 public   | officebuildings_wvdo_200807_utm83                               | table | msjarvis
 public   | paroleoffices_manysources_2008_utm83                            | table | msjarvis
 public   | paroleoffices_manysources_2008_wgs84                            | table | msjarvis
 public   | place                                                           | table | msjarvis
 public   | placesofworship_hsip_20080723_utm83                             | table | msjarvis
 public   | placesofworship_hsip_20080723_wgs84                             | table | msjarvis
 public   | policedept_wvdem_012319_gcs84                                   | table | msjarvis
 public   | policedept_wvdem_012319_utm83                                   | table | msjarvis
 public   | populatedplaces_census_201112_utm83                             | table | msjarvis
 public   | populatedplaces_census_20112_gcs83                              | table | msjarvis
 public   | populatedplaces_census_2020_utm83                               | table | msjarvis
 public   | populatedplaces_census_2020_wma84                               | table | msjarvis
 public   | populatedplaces_uscensus_1990_ll83                              | table | msjarvis
 public   | populatedplaces_uscensus_1990_utm83                             | table | msjarvis
 public   | populationdatablockgroups_uscensus_2000_ll83                    | table | msjarvis
 public   | populationdatablockgroups_uscensus_2000_utm83                   | table | msjarvis
 public   | pow_wvgistc_062919_utm83                                        | table | msjarvis
 public   | pow_wvgistc_062919_wgs84                                        | table | msjarvis
 public   | publichealthdepts_hsip_20091229_gcs83                           | table | msjarvis
 public   | publichealthdepts_hsip_20091229_utm83                           | table | msjarvis
 public   | railnetworkregion_usdot_200203_ll83                             | table | msjarvis
 public   | railnetworkregion_usdot_200203_utm83                            | table | msjarvis
 public   | railnetworkwv_usdot_200203_ll83                                 | table | msjarvis
 public   | railnetworkwv_usdot_200203_utm83                                | table | msjarvis
 public   | railroads_rahalltransportationinstitute_2005_utm83              | table | msjarvis
 public   | realtimestreamflowstations_usgs_200012_ll27                     | table | msjarvis
 public   | realtimestreamflowstations_usgs_200012_utm27                    | table | msjarvis
 public   | recreationalwwtrails_ofwv_20151117_utm83                        | table | msjarvis
 public   | regionalplanninganddevelopmentcouncil_wvdo_1971_ll83            | table | msjarvis
 public   | sewertreatmentplants_wvdep_200203_utm83                         | table | msjarvis
 public   | solidwastefacilities_wvdep_200202_ll83                          | table | msjarvis
 public   | solidwastefacilities_wvdep_200202_utm83                         | table | msjarvis
 public   | spatial_ref_sys                                                 | table | postgres
 public   | springs_wvges_1986_ll83                                         | table | msjarvis
 public   | springs_wvges_1986_utm83                                        | table | msjarvis
 public   | state                                                           | table | msjarvis
 public   | stateofwvhousedistricts_wvlegislativeservices_2010              | table | msjarvis
 public   | stateofwvsenatedistricts_wvlegislativeservices_2010             | table | msjarvis
 public   | states_region_ll83                                              | table | msjarvis
 public   | structurepointsnorth_samb_2003_utm83                            | table | msjarvis
 public   | structurepointssouth_samb_2003_utm83                            | table | msjarvis
 public   | structurepolygons_samb_2003_utm83                               | table | msjarvis
 public   | summits_gistc_052012_utm83_shp                                  | table | msjarvis
 public   | summits_gistc_052012_wgs84_shp                                  | table | msjarvis
 public   | surveycontrol_nationalgeodeticsurvey_102011_gcs83               | table | msjarvis
 public   | tabblock20                                                      | table | msjarvis
 public   | timberremovalvolume_usfs_1996_utm83                             | table | msjarvis
 public   | towers_wvpublicbroadcasting_2002_ll83                           | table | msjarvis
 public   | towers_wvpublicbroadcasting_2002_utm83                          | table | msjarvis
 public   | towersam_fcc_200202_utm83                                       | table | msjarvis
 public   | towersasr_fcc_200202_ll83                                       | table | msjarvis
 public   | towersasr_fcc_200202_utm83                                      | table | msjarvis
 public   | towerscellular_fcc_200202_ll83                                  | table | msjarvis
 public   | towerscellular_fcc_200202_utm83                                 | table | msjarvis
 public   | towersfm_fcc_200202_utm83                                       | table | msjarvis
 public   | towersmicrowave_fcc_200202_ll83                                 | table | msjarvis
 public   | towersmicrowave_fcc_200202_utm83                                | table | msjarvis
 public   | towerspager_fcc_200202_ll83                                     | table | msjarvis
 public   | towerspager_fcc_200202_utm83                                    | table | msjarvis
 public   | towersprivate_fcc_200202_ll83                                   | table | msjarvis
 public   | towersprivate_fcc_200202_utm83                                  | table | msjarvis
 public   | tract                                                           | table | msjarvis
 public   | veteransaffairsfacilities_manysources_200503_utm83              | table | msjarvis
 public   | votingdistrictswv_legislativeservices_2002_ll83                 | table | msjarvis
 public   | votingdistrictswv_uscensus_2000_utm83                           | table | msjarvis
 public   | weatherstations_nationalclimatedatacenter_1999_gcs83            | table | msjarvis
 public   | windenergyresource_nationalrenewableenergylab_200901_utm83      | table | msjarvis
 public   | workforceinvestmentareas_wvgistc_200208_ll83                    | table | msjarvis
 public   | wv_buildings                                                    | table | msjarvis
 public   | wv_congressional_districts_118th_utm83                          | table | postgres
 public   | wv_county_boundaries_24k_topo_updated_2022_utm83                | table | msjarvis
 public   | wv_county_polygons                                              | table | postgres
 public   | wv_layer_registry                                               | table | msjarvis
 public   | wv_microsoft_20180207_utm17n83                                  | table | msjarvis
 public   | wv_precincts_2024_utm83                                         | table | postgres
 public   | wv_state_house_districts_2020_utm83                             | table | postgres
 public   | wv_state_senate_districts_2020_utm83                            | table | postgres
 public   | wv_tax_districts_ll83                                           | table | msjarvis
 public   | wv_tax_districts_utm83                                          | table | msjarvis
 public   | wv_tax_districts_wma84                                          | table | msjarvis
 public   | wv_voting_districts_2020_utm83                                  | table | postgres
 public   | wvdnr_electricity_infrastructure_2003_utm83                     | table | postgres
 public   | wvdnr_public_fishing_areas_2002_utm83                           | table | postgres
 public   | wvdnr_red_spruce_cover_2013_utm83                               | table | postgres
 public   | wvdnr_state_park_boundaries_2022_utm83                          | table | postgres
 public   | wvdnr_stocked_trout_ponds_utm83                                 | table | postgres
 public   | wvdnr_stocked_trout_streams_utm83                               | table | postgres
 public   | wvdnr_trails_state_forests_2001_utm83                           | table | postgres
 public   | wvdnr_trails_wma_2005_utm83                                     | table | postgres
 public   | wvdnr_wildlife_center_2022_utm83                                | table | postgres
 public   | wvdnr_wildlife_mgmt_areas_2022_utm83                            | table | postgres
 public   | wvdnr_wildlife_sanctuary_2022_utm83                             | table | postgres
 public   | wvdof_state_forest_boundaries_2022_utm83                        | table | postgres
 public   | wvdof_wildfire_regions_2008_utm83                               | table | postgres
 public   | wvges_geological_map_1968_utm83                                 | table | postgres
 public   | wvges_geology_bedrock_1999_utm83                                | table | postgres
 public   | wvges_geology_karst_1968_utm83                                  | table | postgres
 public   | wvges_mines_mountaintop_removal_1998_utm83                      | table | postgres
 public   | wvges_springs_1986_utm83                                        | table | postgres
 public   | wvgistc_911centers_wvdem_032819_gcs84                           | table | postgres
 public   | wvgistc_air_nonattainment_wvdep_200802_utm83                    | table | msjarvis
 public   | wvgistc_airport_facilities_dhsem_200807_utm83                   | table | msjarvis
 public   | wvgistc_airport_runways_faa_200202_utm83                        | table | msjarvis
 public   | wvgistc_airports_wvdot_1998_utm83                               | table | msjarvis
 public   | wvgistc_amtrak_rails_fra_200210_utm83                           | table | msjarvis
 public   | wvgistc_boat_launches_dnr_200410_utm83                          | table | msjarvis
 public   | wvgistc_boundaries_appalachian_states_1996_utm83                | table | msjarvis
 public   | wvgistc_building_footprints                                     | table | msjarvis
 public   | wvgistc_buildings_usgs_201006_utm83                             | table | msjarvis
 public   | wvgistc_canaan_valley_nwr_2009_utm83                            | table | postgres
 public   | wvgistc_cemeteries_usgs_201006_utm83                            | table | msjarvis
 public   | wvgistc_churches_usgs_2010                                      | table | postgres
 public   | wvgistc_churches_usgs_201006_utm83                              | table | msjarvis
 public   | wvgistc_community_boundary_2025_utm83                           | table | msjarvis
 public   | wvgistc_community_health_providers_200802_utm83                 | table | msjarvis
 public   | wvgistc_correctional_institutions_hsip_200912_utm83             | table | msjarvis
 public   | wvgistc_correctionalinstitutions_hsip_20091230_utm83            | table | msjarvis
 public   | wvgistc_counties_appalachia_arc_utm83                           | table | postgres
 public   | wvgistc_county_city_park_boundaries_2020_utm83                  | table | postgres
 public   | wvgistc_county_city_parks_2020_utm83                            | table | postgres
 public   | wvgistc_county_courthouses_200203_utm83                         | table | postgres
 public   | wvgistc_county_seats_usgs_utm83                                 | table | postgres
 public   | wvgistc_dams_noncoal_usgs_2002_utm83                            | table | postgres
 public   | wvgistc_dams_samb_2003_utm83                                    | table | postgres
 public   | wvgistc_dams_usace_200010_utm83                                 | table | postgres
 public   | wvgistc_ecoregions_usfs_2000_utm83                              | table | postgres
 public   | wvgistc_emergency_ops_centers_200807_utm83                      | table | postgres
 public   | wvgistc_ems_hsip_200809_utm83                                   | table | postgres
 public   | wvgistc_epa_facilities_200203_utm83                             | table | postgres
 public   | wvgistc_excursion_trains_200102_utm83                           | table | postgres
 public   | wvgistc_fire_departments                                        | table | postgres
 public   | wvgistc_fire_departments_200809_utm83                           | table | postgres
 public   | wvgistc_fire_dept_wvdem_092017_utm83                            | table | msjarvis
 public   | wvgistc_flood_tool_political_2023_utm83                         | table | postgres
 public   | wvgistc_floodplain_q3_utm83                                     | table | postgres
 public   | wvgistc_floodplain_structures_risk_2003_utm83                   | table | postgres
 public   | wvgistc_geonames_usgs_current_2013_utm83                        | table | postgres
 public   | wvgistc_geonames_usgs_historical_2013_utm83                     | table | postgres
 public   | wvgistc_hatfield_mccoy_trail_2006_utm83                         | table | postgres
 public   | wvgistc_health_rural_facilities_utm83                           | table | postgres
 public   | wvgistc_high_water_marks_2025_utm83                             | table | postgres
 public   | wvgistc_higher_ed_2020_utm83                                    | table | postgres
 public   | wvgistc_highered_wvemd_072420_utm83                             | table | msjarvis
 public   | wvgistc_hospitals_hsip_200809_utm83                             | table | postgres
 public   | wvgistc_hospitals_usgs_1981_utm83                               | table | postgres
 public   | wvgistc_hospitals_wvdem_040519_gcs84                            | table | postgres
 public   | wvgistc_hospitals_wvdem_040519_utm83                            | table | msjarvis
 public   | wvgistc_hospitals_wvhca_200802_utm83                            | table | postgres
 public   | wvgistc_hydrography_4800_utm83                                  | table | postgres
 public   | wvgistc_index_grid_24k_quads_utm83                              | table | postgres
 public   | wvgistc_intermodal_terminals_1997_utm83                         | table | postgres
 public   | wvgistc_law_enforcement_hsip_2009_utm83                         | table | postgres
 public   | wvgistc_lawenforcement_hsip_20091230_utm83                      | table | postgres
 public   | wvgistc_libraries_2001_utm83                                    | table | postgres
 public   | wvgistc_libraries_manysources_2001_utm83                        | table | postgres
 public   | wvgistc_locales_usgs_1981_utm83                                 | table | postgres
 public   | wvgistc_locks_2003_utm83                                        | table | postgres
 public   | wvgistc_major_rivers_lakes_line_2002_utm83                      | table | postgres
 public   | wvgistc_major_rivers_lakes_poly_2002_utm83                      | table | postgres
 public   | wvgistc_manufacturing_business_200803_utm83                     | table | postgres
 public   | wvgistc_mineral_operations_2002_utm83                           | table | postgres
 public   | wvgistc_national_forest_2024_utm83                              | table | postgres
 public   | wvgistc_national_guard_armories_200204_utm83                    | table | postgres
 public   | wvgistc_national_park_boundaries_2003_utm83                     | table | postgres
 public   | wvgistc_national_park_service_2024_utm83                        | table | postgres
 public   | wvgistc_national_wildlife_refuge_2024_utm83                     | table | postgres
 public   | wvgistc_navigable_waterways_2006_utm83                          | table | postgres
 public   | wvgistc_nursing_homes_hsip_2010_utm83                           | table | postgres
 public   | wvgistc_nursing_homes_wvhca_200802_utm83                        | table | postgres
 public   | wvgistc_nursinghomes_wvdem_041219_gcs84                         | table | postgres
 public   | wvgistc_nursinghomes_wvdem_041219_utm83                         | table | msjarvis
 public   | wvgistc_nursinghomes_wvhca_200802_utm83                         | table | postgres
 public   | wvgistc_parolefacilities_technigraphics_200711_utm83            | table | postgres
 public   | wvgistc_places_of_worship_hsip_2008_utm83                       | table | postgres
 public   | wvgistc_policedept_wvdem_012319_gcs84                           | table | postgres
 public   | wvgistc_populated_places_usgs_1981_utm83                        | table | postgres
 public   | wvgistc_pow_2019_utm83                                          | table | postgres
 public   | wvgistc_public_health_depts_hsip_2009_utm83                     | table | postgres
 public   | wvgistc_railroad_bridges_2003_utm83                             | table | postgres
 public   | wvgistc_railroads_rti_2005_utm83                                | table | postgres
 public   | wvgistc_recreational_trails_2019_utm83                          | table | postgres
 public   | wvgistc_regional_planning_councils_1971_utm83                   | table | postgres
 public   | wvgistc_riparian_areas_2020_utm83                               | table | postgres
 public   | wvgistc_road_bridges_2003_utm83                                 | table | postgres
 public   | wvgistc_roadless_areas_usfs_2000_utm83                          | table | postgres
 public   | wvgistc_roads_county_200810_utm83                               | table | postgres
 public   | wvgistc_roads_interstates_200910_utm83                          | table | postgres
 public   | wvgistc_roads_scenic_byways_200101_utm83                        | table | postgres
 public   | wvgistc_roads_state_routes_200910_utm83                         | table | postgres
 public   | wvgistc_roads_us_routes_200910_utm83                            | table | postgres
 public   | wvgistc_schools_wvde_2021                                       | table | postgres
 public   | wvgistc_sewer_treatment_plants_200203_utm83                     | table | postgres
 public   | wvgistc_sites_buildings_parks_200807_utm83                      | table | postgres
 public   | wvgistc_solid_waste_facilities_200202_utm83                     | table | postgres
 public   | wvgistc_spillways_2003_utm83                                    | table | postgres
 public   | wvgistc_state_govt_buildings_2008_utm83                         | table | postgres
 public   | wvgistc_statewide_hydro_lr_utm83                                | table | postgres
 public   | wvgistc_streamflow_stations_usgs_2000_utm83                     | table | postgres
 public   | wvgistc_structure_polygons_2003_utm83                           | table | postgres
 public   | wvgistc_structures_at_risk_fema_2003_utm83                      | table | postgres
 public   | wvgistc_summits_usgs_1981_utm83                                 | table | postgres
 public   | wvgistc_timber_removal_volume_1996_utm83                        | table | postgres
 public   | wvgistc_towers_am_fcc_200202_utm83                              | table | postgres
 public   | wvgistc_towers_asr_fcc_200202_utm83                             | table | postgres
 public   | wvgistc_towers_cellular_fcc_200202_utm83                        | table | postgres
 public   | wvgistc_towers_fm_fcc_200202_utm83                              | table | postgres
 public   | wvgistc_towers_microwave_fcc_200202_utm83                       | table | postgres
 public   | wvgistc_towers_pager_fcc_200202_utm83                           | table | postgres
 public   | wvgistc_towers_private_fcc_200202_utm83                         | table | postgres
 public   | wvgistc_towers_public_broadcasting_2002_utm83                   | table | postgres
 public   | wvgistc_towers_tv_fcc_200202_utm83                              | table | postgres
 public   | wvgistc_trails_bluestone_river_2007_utm83                       | table | postgres
 public   | wvgistc_trails_canaan_valley_nwr_2006_utm83                     | table | postgres
 public   | wvgistc_trails_hatfield_mccoy_2006_utm83                        | table | postgres
 public   | wvgistc_trails_new_river_gorge_2007_utm83                       | table | postgres
 public   | wvgistc_trails_tucker_county_2007_utm83                         | table | postgres
 public   | wvgistc_tunnels_2003_utm83                                      | table | postgres
 public   | wvgistc_veterans_affairs_200503_utm83                           | table | postgres
 public   | wvgistc_veteransaffairsfacilities_manysources_200503_utm83      | table | postgres
 public   | wvgistc_watershed_8digit_2002_utm83                             | table | postgres
 public   | wvgistc_watershed_hu12_nrcs_2009_utm83                          | table | postgres
 public   | wvgistc_waterway_river_miles_2006_utm83                         | table | postgres
 public   | wvgistc_waterway_structures_2006_utm83                          | table | postgres
 public   | wvgistc_weather_stations_1999_utm83                             | table | postgres
 public   | wvgistc_wind_energy_resource_2009_utm83                         | table | postgres
 public   | wvgistc_workforce_investment_areas_200208_utm83                 | table | postgres
 public   | wvgistcbuildingfootprints                                       | table | msjarvis
 public   | wvstatebounadary100k_usgs_200203_utm83                          | table | msjarvis
 public   | wvstateboundary100k_usgs_200203_ll83                            | table | msjarvis
 public   | wvstateboundary24k_usgs_200203_ll83                             | table | msjarvis
 public   | wvstateboundary24k_usgs_200203_utm83                            | table | msjarvis
 public   | wvstatehousedistricts_manysources_1992_ll83                     | table | msjarvis
 public   | wvstatehousedistricts_manysources_1992_utm83                    | table | msjarvis
 public   | wvstatehousedistricts_manysources_2002_ll83                     | table | msjarvis
 public   | wvstatehousedistricts_manysources_2002_utm83                    | table | msjarvis
 public   | wvstatehousedistricts_wvlegislativeservices_2020_utm83          | table | msjarvis
 public   | wvstatesenatedistricts_manysources_1992_ll83                    | table | msjarvis
 public   | wvstatesenatedistricts_manysources_1992_utm83                   | table | msjarvis
 public   | wvstatesenatedistricts_manysources_2002_ll83                    | table | msjarvis
 public   | wvstatesenatedistricts_manysources_2002_utm83                   | table | msjarvis
 public   | wvstatesenatedistricts_wvlegislativeservices_2020_utm83         | table | msjarvis
 public   | zcta5                                                           | table | msjarvis
 public   | zipcodetabulationarea_census_2020_utm83                         | table | msjarvis
 public   | zipcodetabulationarea_census_2020_wma84                         | table | msjarvis
 tiger    | addr                                                            | table | postgres
 tiger    | county_lookup                                                   | table | postgres
 tiger    | countysub_lookup                                                | table | postgres
 tiger    | direction_lookup                                                | table | postgres
 tiger    | featnames                                                       | table | postgres
 tiger    | geocode_settings                                                | table | postgres
 tiger    | geocode_settings_default                                        | table | postgres
 tiger    | loader_lookuptables                                             | table | postgres
 tiger    | loader_platform                                                 | table | postgres
 tiger    | loader_variables                                                | table | postgres
 tiger    | pagc_gaz                                                        | table | postgres
 tiger    | pagc_lex                                                        | table | postgres
 tiger    | pagc_rules                                                      | table | postgres
 tiger    | place_lookup                                                    | table | postgres
 tiger    | secondary_unit_lookup                                           | table | postgres
 tiger    | state_lookup                                                    | table | postgres
 tiger    | street_type_lookup                                              | table | postgres
 tiger    | tabblock                                                        | table | postgres
 tiger    | zip_lookup                                                      | table | postgres
 tiger    | zip_lookup_all                                                  | table | postgres
 tiger    | zip_lookup_base                                                 | table | postgres
 tiger    | zip_state                                                       | table | postgres
 tiger    | zip_state_loc                                                   | table | postgres
 topology | layer                                                           | table | postgres
 topology | topology                                                        | table | postgres
(428 rows)

(.venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ # Find the users table — search all databases
docker exec jarvis-local-resources-db psql -U postgres \
  -c "SELECT table_catalog, table_name FROM information_schema.tables WHERE table_name LIKE '%user%' OR table_name LIKE '%member%' OR table_name LIKE '%account%';"
 table_catalog |         table_name          
---------------+-----------------------------
 postgres      | pg_user_mapping
 postgres      | pg_auth_members
 postgres      | pg_user
 postgres      | pg_stat_user_tables
 postgres      | pg_stat_xact_user_tables
 postgres      | pg_statio_user_tables
 postgres      | pg_stat_user_indexes
 postgres      | pg_statio_user_indexes
 postgres      | pg_statio_user_sequences
 postgres      | pg_stat_user_functions
 postgres      | pg_stat_xact_user_functions
 postgres      | pg_user_mappings
 postgres      | user_defined_types
 postgres      | _pg_user_mappings
 postgres      | user_mapping_options
 postgres      | user_mappings
(16 rows)

(.venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ # What tables exist in the GIS database?
docker exec jarvis-local-resources-db psql -U postgres -d msjarvisgis \
  -c "\dt"

# Count rows in likely feature tables
docker exec jarvis-local-resources-db psql -U postgres -d msjarvisgis \
  -c "SELECT schemaname, tablename, n_live_tup FROM pg_stat_user_tables ORDER BY n_live_tup DESC LIMIT 15;"
                                       List of relations
  Schema  |                              Name                               | Type  |  Owner   
----------+-----------------------------------------------------------------+-------+----------
 public   | 911centers_wvdem_032819_gcs84                                   | table | msjarvis
 public   | 911centers_wvdem_032819_utm83                                   | table | msjarvis
 public   | addrfeat                                                        | table | msjarvis
 public   | amtrackrails_federalrailroadadministration_200210_ll83          | table | msjarvis
 public   | bg                                                              | table | msjarvis
 public   | blockgroups_census_2000_ll83                                    | table | msjarvis
 public   | blockgroups_census_2000_utm83                                   | table | msjarvis
 public   | blockgroups_census_201111_gcs83                                 | table | msjarvis
 public   | blockgroups_census_201111_utm83                                 | table | msjarvis
 public   | blockgroups_census_2020_utm83                                   | table | msjarvis
 public   | blockgroups_census_2020_wma84                                   | table | msjarvis
 public   | blocks_census_2020_utm83                                        | table | msjarvis
 public   | blocks_census_2020_wma84                                        | table | msjarvis
 public   | boundaryappalachianbasin_wvges_1996_utm83                       | table | msjarvis
 public   | bridges                                                         | table | msjarvis
 public   | calderl_reg_ll83                                                | table | msjarvis
 public   | census_block_groups_2020_utm83                                  | table | msjarvis
 public   | census_blocks_2020_utm83                                        | table | msjarvis
 public   | census_cities_over10k_2020_utm83                                | table | msjarvis
 public   | census_cities_over2500_2020_utm83                               | table | msjarvis
 public   | census_county_boundaries_2021_utm83                             | table | postgres
 public   | census_designated_places_2021_utm83                             | table | msjarvis
 public   | census_empowerment_zones_2002_utm83                             | table | postgres
 public   | census_historical_pop_by_county_2006_utm83                      | table | postgres
 public   | census_incorporated_places_2021_utm83                           | table | postgres
 public   | census_metro_micro_areas_2020_utm83                             | table | postgres
 public   | census_minor_civil_divisions_2020_utm83                         | table | postgres
 public   | census_misc_transportation_2000_utm83                           | table | postgres
 public   | census_pop_change_communities_2020_utm83                        | table | postgres
 public   | census_pop_change_counties_2020_utm83                           | table | postgres
 public   | census_populated_places_2020_utm83                              | table | postgres
 public   | census_railroads_2023_utm83                                     | table | postgres
 public   | census_roads_2023_utm83                                         | table | postgres
 public   | census_streams_waterbodies_2023_utm83                           | table | postgres
 public   | census_tl_2020_54_bg                                            | table | msjarvis
 public   | census_tl_2020_54_tabblock20                                    | table | msjarvis
 public   | census_tl_2020_us_county                                        | table | msjarvis
 public   | census_tl_2020_us_zcta510                                       | table | msjarvis
 public   | census_tl_2020_us_zcta520                                       | table | msjarvis
 public   | census_tracts_2020_utm83                                        | table | msjarvis
 public   | census_urban_areas_100k_2020_utm83                              | table | postgres
 public   | census_zcta_2020_utm83                                          | table | postgres
 public   | citieswithpopulation_2500_census_201111_gcs83                   | table | msjarvis
 public   | citieswithpopulation_2500_census_201111_utm83                   | table | msjarvis
 public   | citieswithpopulationover10k_census_201111_gcs83                 | table | msjarvis
 public   | citieswithpopulationover10k_uscensus_1990_ll83                  | table | msjarvis
 public   | citieswithpopulationover2500_uscensus_1990_ll83                 | table | msjarvis
 public   | citieswithpopulationsover10k_census_2020_utm83                  | table | msjarvis
 public   | citieswithpopulationsover2500_census_2020_utm83                 | table | msjarvis
 public   | citieswithpopulatoinover2500_uscensus_1990_utm83                | table | msjarvis
 public   | coals2_ll83                                                     | table | msjarvis
 public   | coals2_utm27                                                    | table | msjarvis
 public   | coals2_utm83                                                    | table | msjarvis
 public   | communityboundary_min_att_20250121_utm83                        | table | msjarvis
 public   | communityboundary_min_att_20250121_wma84                        | table | msjarvis
 public   | communityhealthproviders_wvhealthcareauthority_200802_utm83     | table | msjarvis
 public   | conversation_history                                            | table | msjarvis
 public   | correctionalinstitutions_hsip_20091230_utm83                    | table | msjarvis
 public   | correctionalinstitutions_hsip_20091230_wgs84                    | table | msjarvis
 public   | county                                                          | table | msjarvis
 public   | countycityparkboundaries_20201104_utm83                         | table | msjarvis
 public   | countyseats_usgs_ll83                                           | table | msjarvis
 public   | countyseats_usgs_utm83                                          | table | msjarvis
 public   | courthousescounty_manysources_200203_ll83                       | table | msjarvis
 public   | courthousescounty_manysources_200203_utm83                      | table | msjarvis
 public   | courthousesfederal_manysources_200203_ll83                      | table | msjarvis
 public   | courthousesfederal_manysources_200203_utm                       | table | msjarvis
 public   | cousub                                                          | table | msjarvis
 public   | cvfault_ll83                                                    | table | msjarvis
 public   | cvfault_utm27                                                   | table | msjarvis
 public   | cvfault_utm83                                                   | table | msjarvis
 public   | cvpoly_ll83                                                     | table | msjarvis
 public   | cvpoly_utm27                                                    | table | msjarvis
 public   | cvpoly_utm83                                                    | table | msjarvis
 public   | dams_usarmycorpsofengineers_200010_utm83                        | table | msjarvis
 public   | dams_usarmycropsofengineers_200010_ll83                         | table | msjarvis
 public   | damsnoncoal_usgs_2002_ll27                                      | table | msjarvis
 public   | edges                                                           | table | msjarvis
 public   | empowermentzonesandenterprisecommunities_uscensus_2002_utm83    | table | msjarvis
 public   | empowermentzonesandenterprisecommunitiesbytract_uscens_30c72907 | table | msjarvis
 public   | equity_timesheet                                                | table | postgres
 public   | excursionpassengertrains_wvdof_200102_ll83                      | table | msjarvis
 public   | excursionpassengertrains_wvdof_200102_utm83                     | table | msjarvis
 public   | faces                                                           | table | msjarvis
 public   | facilities_epa_200203_ll83                                      | table | msjarvis
 public   | facilities_epa_200203_utm83                                     | table | msjarvis
 public   | fault_reg_ll83                                                  | table | msjarvis
 public   | faultgl_reg_ll83                                                | table | msjarvis
 public   | fayette_parcels                                                 | table | msjarvis
 public   | features                                                        | table | msjarvis
 public   | fire_departments                                                | table | msjarvis
 public   | fire_dept_wvdem_092017_utm83                                    | table | msjarvis
 public   | floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83  | table | msjarvis
 public   | founder_tokens                                                  | table | postgres
 public   | gbim_entities                                                   | table | msjarvis
 public   | geographicalnamesonusgstopomaps_usgs_200601_ll27                | table | msjarvis
 public   | geographicnamesonusgstopomaps_current_usgs_20110801_ll83        | table | msjarvis
 public   | geographicnamesonusgstopomaps_historical_usgs_20110801_ll83     | table | msjarvis
 public   | geographicnamesonusgstopomaps_usgs_20110801_ll83                | table | msjarvis
 public   | geolgyl_reg_ll83                                                | table | msjarvis
 public   | geolgyp_reg_ll83                                                | table | msjarvis
 public   | geospatial_features                                             | table | postgres
 public   | geotextl_reg_ll83                                               | table | msjarvis
 public   | glacagl_reg_ll83                                                | table | msjarvis
 public   | glacal_reg_ll83                                                 | table | msjarvis
 public   | hazardmitigationbuyout_20250929_polygons_utm83                  | table | msjarvis
 public   | healthruralfacilities_manysources_utm83                         | table | msjarvis
 public   | highered_wvemd_072420_utm83                                     | table | msjarvis
 public   | highered_wvemd_072420_wgc84                                     | table | msjarvis
 public   | historicalaerialphotographycountycoverage_wvgistc_utm83         | table | msjarvis
 public   | hospitals                                                       | table | msjarvis
 public   | hospitals_wvdem_040519_gcs84                                    | table | msjarvis
 public   | hospitals_wvdem_040519_utm83                                    | table | msjarvis
 public   | impact_reg_ll83                                                 | table | msjarvis
 public   | indexgrid15minutequads_wvgistc_ll83                             | table | msjarvis
 public   | indexgrid15minutequads_wvgistc_utm83                            | table | msjarvis
 public   | indexgrid15minutewithcounties_wvgistc_utm27                     | table | msjarvis
 public   | indexgrid1minutequads_wvgistc_ll83                              | table | msjarvis
 public   | industrialbuildings_wvdo_200807_utm83                           | table | msjarvis
 public   | industrialparks_wvdo_200078_utm83                               | table | msjarvis
 public   | industrialsites_wvdo_200807_utm83                               | table | msjarvis
 public   | inedexgrid1minutequads_wvgistc_utm83                            | table | msjarvis
 public   | interaction_provenance_immutable                                | table | postgres
 public   | interactions                                                    | table | postgres
 public   | intermodalterminalfacilities_usdot_1997_ll83                    | table | msjarvis
 public   | intermodalterminalfacilities_usdot_1997_utm83                   | table | msjarvis
 public   | libraries_manysources_2001_ll27                                 | table | msjarvis
 public   | libraries_manysources_2001_utm83                                | table | msjarvis
 public   | majorriversandlakesline_nhd_2002_ll83                           | table | msjarvis
 public   | majorriversandlakesline_nhd_2002_utm83                          | table | msjarvis
 public   | majorriversandlakespolygon_nhd_2002_poly_ll83                   | table | msjarvis
 public   | majorriversandlakespolygon_nhd_2002_utm83                       | table | msjarvis
 public   | manufacturingandbusiness_wvdo_200803_utm83                      | table | msjarvis
 public   | metfacp_reg_ll83                                                | table | msjarvis
 public   | metropolitanandmicropolitanstatisticalareas_census_201111_gcs83 | table | msjarvis
 public   | metropolitanstatisticalareas_uscensus_199901_ll83               | table | msjarvis
 public   | mineraloperations_usgs_200204_ll83                              | table | msjarvis
 public   | mineraloperations_usgs_200204_utm83                             | table | msjarvis
 public   | minesabandonedlandsline_wvdep_1996_noprojectoin                 | table | msjarvis
 public   | minesabandonedlandspoint_wvdep_1996_noprojection                | table | msjarvis
 public   | minesabandonedlandspolygon_wvdep_1996_noprojection              | table | msjarvis
 public   | mountainshares_balances                                         | table | postgres
 public   | mountainshares_participants                                     | table | postgres
 public   | nationalatlasstreams_usgs_199903_ll83                           | table | msjarvis
 public   | nationalatlasstreams_usgs_199903_utm83                          | table | msjarvis
 public   | nationalregister_point_20200923                                 | table | msjarvis
 public   | nationalregister_point_20200923_utm27                           | table | msjarvis
 public   | nationalregisterofhistoricplacespoints_nationalparkser_45ec46d0 | table | msjarvis
 public   | nationalregisterofhistoricplacespolygons_nationaparkse_b9d30a70 | table | msjarvis
 public   | nationalwaterwaynetwork_usarmycorpsofengineers_2001_ll83        | table | msjarvis
 public   | nationalwaterwaynetworkports_usarmycorpsofengineers_2001_ll83   | table | msjarvis
 public   | nationaregisterofhistoricplacespoints_nationalparkserv_ba8eebd5 | table | msjarvis
 public   | nationaregisterofhistoricplacespolygons_nationalparkse_cab42150 | table | msjarvis
 public   | natoinalregisterofhistoricplacespoints_nationalparkser_ca43510e | table | msjarvis
 public   | naviagablewaterways_usarmycropsofengineers_2006_utm83           | table | msjarvis
 public   | navigablewaterwaysrivermiles_usarmycropsofengineers_2006_utm83  | table | msjarvis
 public   | navigablewaterwaysstructures_usarmycorpsofengineers_2006_utm83  | table | msjarvis
 public   | nursinghomes_wvdem_041219_gcs84                                 | table | msjarvis
 public   | nursinghomes_wvdem_041219_utm83                                 | table | msjarvis
 public   | officebuildings_wvdo_200807_utm83                               | table | msjarvis
 public   | paroleoffices_manysources_2008_utm83                            | table | msjarvis
 public   | paroleoffices_manysources_2008_wgs84                            | table | msjarvis
 public   | place                                                           | table | msjarvis
 public   | placesofworship_hsip_20080723_utm83                             | table | msjarvis
 public   | placesofworship_hsip_20080723_wgs84                             | table | msjarvis
 public   | policedept_wvdem_012319_gcs84                                   | table | msjarvis
 public   | policedept_wvdem_012319_utm83                                   | table | msjarvis
 public   | populatedplaces_census_201112_utm83                             | table | msjarvis
 public   | populatedplaces_census_20112_gcs83                              | table | msjarvis
 public   | populatedplaces_census_2020_utm83                               | table | msjarvis
 public   | populatedplaces_census_2020_wma84                               | table | msjarvis
 public   | populatedplaces_uscensus_1990_ll83                              | table | msjarvis
 public   | populatedplaces_uscensus_1990_utm83                             | table | msjarvis
 public   | populationdatablockgroups_uscensus_2000_ll83                    | table | msjarvis
 public   | populationdatablockgroups_uscensus_2000_utm83                   | table | msjarvis
 public   | pow_wvgistc_062919_utm83                                        | table | msjarvis
 public   | pow_wvgistc_062919_wgs84                                        | table | msjarvis
 public   | publichealthdepts_hsip_20091229_gcs83                           | table | msjarvis
 public   | publichealthdepts_hsip_20091229_utm83                           | table | msjarvis
 public   | railnetworkregion_usdot_200203_ll83                             | table | msjarvis
 public   | railnetworkregion_usdot_200203_utm83                            | table | msjarvis
 public   | railnetworkwv_usdot_200203_ll83                                 | table | msjarvis
 public   | railnetworkwv_usdot_200203_utm83                                | table | msjarvis
 public   | railroads_rahalltransportationinstitute_2005_utm83              | table | msjarvis
 public   | realtimestreamflowstations_usgs_200012_ll27                     | table | msjarvis
 public   | realtimestreamflowstations_usgs_200012_utm27                    | table | msjarvis
 public   | recreationalwwtrails_ofwv_20151117_utm83                        | table | msjarvis
 public   | regionalplanninganddevelopmentcouncil_wvdo_1971_ll83            | table | msjarvis
 public   | sewertreatmentplants_wvdep_200203_utm83                         | table | msjarvis
 public   | solidwastefacilities_wvdep_200202_ll83                          | table | msjarvis
 public   | solidwastefacilities_wvdep_200202_utm83                         | table | msjarvis
 public   | spatial_ref_sys                                                 | table | postgres
 public   | springs_wvges_1986_ll83                                         | table | msjarvis
 public   | springs_wvges_1986_utm83                                        | table | msjarvis
 public   | state                                                           | table | msjarvis
 public   | stateofwvhousedistricts_wvlegislativeservices_2010              | table | msjarvis
 public   | stateofwvsenatedistricts_wvlegislativeservices_2010             | table | msjarvis
 public   | states_region_ll83                                              | table | msjarvis
 public   | structurepointsnorth_samb_2003_utm83                            | table | msjarvis
 public   | structurepointssouth_samb_2003_utm83                            | table | msjarvis
 public   | structurepolygons_samb_2003_utm83                               | table | msjarvis
 public   | summits_gistc_052012_utm83_shp                                  | table | msjarvis
 public   | summits_gistc_052012_wgs84_shp                                  | table | msjarvis
 public   | surveycontrol_nationalgeodeticsurvey_102011_gcs83               | table | msjarvis
 public   | tabblock20                                                      | table | msjarvis
 public   | timberremovalvolume_usfs_1996_utm83                             | table | msjarvis
 public   | towers_wvpublicbroadcasting_2002_ll83                           | table | msjarvis
 public   | towers_wvpublicbroadcasting_2002_utm83                          | table | msjarvis
 public   | towersam_fcc_200202_utm83                                       | table | msjarvis
 public   | towersasr_fcc_200202_ll83                                       | table | msjarvis
 public   | towersasr_fcc_200202_utm83                                      | table | msjarvis
 public   | towerscellular_fcc_200202_ll83                                  | table | msjarvis
 public   | towerscellular_fcc_200202_utm83                                 | table | msjarvis
 public   | towersfm_fcc_200202_utm83                                       | table | msjarvis
 public   | towersmicrowave_fcc_200202_ll83                                 | table | msjarvis
 public   | towersmicrowave_fcc_200202_utm83                                | table | msjarvis
 public   | towerspager_fcc_200202_ll83                                     | table | msjarvis
 public   | towerspager_fcc_200202_utm83                                    | table | msjarvis
 public   | towersprivate_fcc_200202_ll83                                   | table | msjarvis
 public   | towersprivate_fcc_200202_utm83                                  | table | msjarvis
 public   | tract                                                           | table | msjarvis
 public   | veteransaffairsfacilities_manysources_200503_utm83              | table | msjarvis
 public   | votingdistrictswv_legislativeservices_2002_ll83                 | table | msjarvis
 public   | votingdistrictswv_uscensus_2000_utm83                           | table | msjarvis
 public   | weatherstations_nationalclimatedatacenter_1999_gcs83            | table | msjarvis
 public   | windenergyresource_nationalrenewableenergylab_200901_utm83      | table | msjarvis
 public   | workforceinvestmentareas_wvgistc_200208_ll83                    | table | msjarvis
 public   | wv_buildings                                                    | table | msjarvis
 public   | wv_congressional_districts_118th_utm83                          | table | postgres
 public   | wv_county_boundaries_24k_topo_updated_2022_utm83                | table | msjarvis
 public   | wv_county_polygons                                              | table | postgres
 public   | wv_layer_registry                                               | table | msjarvis
 public   | wv_microsoft_20180207_utm17n83                                  | table | msjarvis
 public   | wv_precincts_2024_utm83                                         | table | postgres
 public   | wv_state_house_districts_2020_utm83                             | table | postgres
 public   | wv_state_senate_districts_2020_utm83                            | table | postgres
 public   | wv_tax_districts_ll83                                           | table | msjarvis
 public   | wv_tax_districts_utm83                                          | table | msjarvis
 public   | wv_tax_districts_wma84                                          | table | msjarvis
 public   | wv_voting_districts_2020_utm83                                  | table | postgres
 public   | wvdnr_electricity_infrastructure_2003_utm83                     | table | postgres
 public   | wvdnr_public_fishing_areas_2002_utm83                           | table | postgres
 public   | wvdnr_red_spruce_cover_2013_utm83                               | table | postgres
 public   | wvdnr_state_park_boundaries_2022_utm83                          | table | postgres
 public   | wvdnr_stocked_trout_ponds_utm83                                 | table | postgres
 public   | wvdnr_stocked_trout_streams_utm83                               | table | postgres
 public   | wvdnr_trails_state_forests_2001_utm83                           | table | postgres
 public   | wvdnr_trails_wma_2005_utm83                                     | table | postgres
 public   | wvdnr_wildlife_center_2022_utm83                                | table | postgres
 public   | wvdnr_wildlife_mgmt_areas_2022_utm83                            | table | postgres
 public   | wvdnr_wildlife_sanctuary_2022_utm83                             | table | postgres
 public   | wvdof_state_forest_boundaries_2022_utm83                        | table | postgres
 public   | wvdof_wildfire_regions_2008_utm83                               | table | postgres
 public   | wvges_geological_map_1968_utm83                                 | table | postgres
 public   | wvges_geology_bedrock_1999_utm83                                | table | postgres
 public   | wvges_geology_karst_1968_utm83                                  | table | postgres
 public   | wvges_mines_mountaintop_removal_1998_utm83                      | table | postgres
 public   | wvges_springs_1986_utm83                                        | table | postgres
 public   | wvgistc_911centers_wvdem_032819_gcs84                           | table | postgres
 public   | wvgistc_air_nonattainment_wvdep_200802_utm83                    | table | msjarvis
 public   | wvgistc_airport_facilities_dhsem_200807_utm83                   | table | msjarvis
 public   | wvgistc_airport_runways_faa_200202_utm83                        | table | msjarvis
 public   | wvgistc_airports_wvdot_1998_utm83                               | table | msjarvis
 public   | wvgistc_amtrak_rails_fra_200210_utm83                           | table | msjarvis
 public   | wvgistc_boat_launches_dnr_200410_utm83                          | table | msjarvis
 public   | wvgistc_boundaries_appalachian_states_1996_utm83                | table | msjarvis
 public   | wvgistc_building_footprints                                     | table | msjarvis
 public   | wvgistc_buildings_usgs_201006_utm83                             | table | msjarvis
 public   | wvgistc_canaan_valley_nwr_2009_utm83                            | table | postgres
 public   | wvgistc_cemeteries_usgs_201006_utm83                            | table | msjarvis
 public   | wvgistc_churches_usgs_2010                                      | table | postgres
 public   | wvgistc_churches_usgs_201006_utm83                              | table | msjarvis
 public   | wvgistc_community_boundary_2025_utm83                           | table | msjarvis
 public   | wvgistc_community_health_providers_200802_utm83                 | table | msjarvis
 public   | wvgistc_correctional_institutions_hsip_200912_utm83             | table | msjarvis
 public   | wvgistc_correctionalinstitutions_hsip_20091230_utm83            | table | msjarvis
 public   | wvgistc_counties_appalachia_arc_utm83                           | table | postgres
 public   | wvgistc_county_city_park_boundaries_2020_utm83                  | table | postgres
 public   | wvgistc_county_city_parks_2020_utm83                            | table | postgres
 public   | wvgistc_county_courthouses_200203_utm83                         | table | postgres
 public   | wvgistc_county_seats_usgs_utm83                                 | table | postgres
 public   | wvgistc_dams_noncoal_usgs_2002_utm83                            | table | postgres
 public   | wvgistc_dams_samb_2003_utm83                                    | table | postgres
 public   | wvgistc_dams_usace_200010_utm83                                 | table | postgres
 public   | wvgistc_ecoregions_usfs_2000_utm83                              | table | postgres
 public   | wvgistc_emergency_ops_centers_200807_utm83                      | table | postgres
 public   | wvgistc_ems_hsip_200809_utm83                                   | table | postgres
 public   | wvgistc_epa_facilities_200203_utm83                             | table | postgres
 public   | wvgistc_excursion_trains_200102_utm83                           | table | postgres
 public   | wvgistc_fire_departments                                        | table | postgres
 public   | wvgistc_fire_departments_200809_utm83                           | table | postgres
 public   | wvgistc_fire_dept_wvdem_092017_utm83                            | table | msjarvis
 public   | wvgistc_flood_tool_political_2023_utm83                         | table | postgres
 public   | wvgistc_floodplain_q3_utm83                                     | table | postgres
 public   | wvgistc_floodplain_structures_risk_2003_utm83                   | table | postgres
 public   | wvgistc_geonames_usgs_current_2013_utm83                        | table | postgres
 public   | wvgistc_geonames_usgs_historical_2013_utm83                     | table | postgres
 public   | wvgistc_hatfield_mccoy_trail_2006_utm83                         | table | postgres
 public   | wvgistc_health_rural_facilities_utm83                           | table | postgres
 public   | wvgistc_high_water_marks_2025_utm83                             | table | postgres
 public   | wvgistc_higher_ed_2020_utm83                                    | table | postgres
 public   | wvgistc_highered_wvemd_072420_utm83                             | table | msjarvis
 public   | wvgistc_hospitals_hsip_200809_utm83                             | table | postgres
 public   | wvgistc_hospitals_usgs_1981_utm83                               | table | postgres
 public   | wvgistc_hospitals_wvdem_040519_gcs84                            | table | postgres
 public   | wvgistc_hospitals_wvdem_040519_utm83                            | table | msjarvis
 public   | wvgistc_hospitals_wvhca_200802_utm83                            | table | postgres
 public   | wvgistc_hydrography_4800_utm83                                  | table | postgres
 public   | wvgistc_index_grid_24k_quads_utm83                              | table | postgres
 public   | wvgistc_intermodal_terminals_1997_utm83                         | table | postgres
 public   | wvgistc_law_enforcement_hsip_2009_utm83                         | table | postgres
 public   | wvgistc_lawenforcement_hsip_20091230_utm83                      | table | postgres
 public   | wvgistc_libraries_2001_utm83                                    | table | postgres
 public   | wvgistc_libraries_manysources_2001_utm83                        | table | postgres
 public   | wvgistc_locales_usgs_1981_utm83                                 | table | postgres
 public   | wvgistc_locks_2003_utm83                                        | table | postgres
 public   | wvgistc_major_rivers_lakes_line_2002_utm83                      | table | postgres
 public   | wvgistc_major_rivers_lakes_poly_2002_utm83                      | table | postgres
 public   | wvgistc_manufacturing_business_200803_utm83                     | table | postgres
 public   | wvgistc_mineral_operations_2002_utm83                           | table | postgres
 public   | wvgistc_national_forest_2024_utm83                              | table | postgres
 public   | wvgistc_national_guard_armories_200204_utm83                    | table | postgres
 public   | wvgistc_national_park_boundaries_2003_utm83                     | table | postgres
 public   | wvgistc_national_park_service_2024_utm83                        | table | postgres
 public   | wvgistc_national_wildlife_refuge_2024_utm83                     | table | postgres
 public   | wvgistc_navigable_waterways_2006_utm83                          | table | postgres
 public   | wvgistc_nursing_homes_hsip_2010_utm83                           | table | postgres
 public   | wvgistc_nursing_homes_wvhca_200802_utm83                        | table | postgres
 public   | wvgistc_nursinghomes_wvdem_041219_gcs84                         | table | postgres
 public   | wvgistc_nursinghomes_wvdem_041219_utm83                         | table | msjarvis
 public   | wvgistc_nursinghomes_wvhca_200802_utm83                         | table | postgres
 public   | wvgistc_parolefacilities_technigraphics_200711_utm83            | table | postgres
 public   | wvgistc_places_of_worship_hsip_2008_utm83                       | table | postgres
 public   | wvgistc_policedept_wvdem_012319_gcs84                           | table | postgres
 public   | wvgistc_populated_places_usgs_1981_utm83                        | table | postgres
 public   | wvgistc_pow_2019_utm83                                          | table | postgres
 public   | wvgistc_public_health_depts_hsip_2009_utm83                     | table | postgres
 public   | wvgistc_railroad_bridges_2003_utm83                             | table | postgres
 public   | wvgistc_railroads_rti_2005_utm83                                | table | postgres
 public   | wvgistc_recreational_trails_2019_utm83                          | table | postgres
 public   | wvgistc_regional_planning_councils_1971_utm83                   | table | postgres
 public   | wvgistc_riparian_areas_2020_utm83                               | table | postgres
 public   | wvgistc_road_bridges_2003_utm83                                 | table | postgres
 public   | wvgistc_roadless_areas_usfs_2000_utm83                          | table | postgres
 public   | wvgistc_roads_county_200810_utm83                               | table | postgres
 public   | wvgistc_roads_interstates_200910_utm83                          | table | postgres
 public   | wvgistc_roads_scenic_byways_200101_utm83                        | table | postgres
 public   | wvgistc_roads_state_routes_200910_utm83                         | table | postgres
 public   | wvgistc_roads_us_routes_200910_utm83                            | table | postgres
 public   | wvgistc_schools_wvde_2021                                       | table | postgres
 public   | wvgistc_sewer_treatment_plants_200203_utm83                     | table | postgres
 public   | wvgistc_sites_buildings_parks_200807_utm83                      | table | postgres
 public   | wvgistc_solid_waste_facilities_200202_utm83                     | table | postgres
 public   | wvgistc_spillways_2003_utm83                                    | table | postgres
 public   | wvgistc_state_govt_buildings_2008_utm83                         | table | postgres
 public   | wvgistc_statewide_hydro_lr_utm83                                | table | postgres
 public   | wvgistc_streamflow_stations_usgs_2000_utm83                     | table | postgres
 public   | wvgistc_structure_polygons_2003_utm83                           | table | postgres
 public   | wvgistc_structures_at_risk_fema_2003_utm83                      | table | postgres
 public   | wvgistc_summits_usgs_1981_utm83                                 | table | postgres
 public   | wvgistc_timber_removal_volume_1996_utm83                        | table | postgres
 public   | wvgistc_towers_am_fcc_200202_utm83                              | table | postgres
 public   | wvgistc_towers_asr_fcc_200202_utm83                             | table | postgres
 public   | wvgistc_towers_cellular_fcc_200202_utm83                        | table | postgres
 public   | wvgistc_towers_fm_fcc_200202_utm83                              | table | postgres
 public   | wvgistc_towers_microwave_fcc_200202_utm83                       | table | postgres
 public   | wvgistc_towers_pager_fcc_200202_utm83                           | table | postgres
 public   | wvgistc_towers_private_fcc_200202_utm83                         | table | postgres
 public   | wvgistc_towers_public_broadcasting_2002_utm83                   | table | postgres
 public   | wvgistc_towers_tv_fcc_200202_utm83                              | table | postgres
 public   | wvgistc_trails_bluestone_river_2007_utm83                       | table | postgres
 public   | wvgistc_trails_canaan_valley_nwr_2006_utm83                     | table | postgres
 public   | wvgistc_trails_hatfield_mccoy_2006_utm83                        | table | postgres
 public   | wvgistc_trails_new_river_gorge_2007_utm83                       | table | postgres
 public   | wvgistc_trails_tucker_county_2007_utm83                         | table | postgres
 public   | wvgistc_tunnels_2003_utm83                                      | table | postgres
 public   | wvgistc_veterans_affairs_200503_utm83                           | table | postgres
 public   | wvgistc_veteransaffairsfacilities_manysources_200503_utm83      | table | postgres
 public   | wvgistc_watershed_8digit_2002_utm83                             | table | postgres
 public   | wvgistc_watershed_hu12_nrcs_2009_utm83                          | table | postgres
 public   | wvgistc_waterway_river_miles_2006_utm83                         | table | postgres
 public   | wvgistc_waterway_structures_2006_utm83                          | table | postgres
 public   | wvgistc_weather_stations_1999_utm83                             | table | postgres
 public   | wvgistc_wind_energy_resource_2009_utm83                         | table | postgres
 public   | wvgistc_workforce_investment_areas_200208_utm83                 | table | postgres
 public   | wvgistcbuildingfootprints                                       | table | msjarvis
 public   | wvstatebounadary100k_usgs_200203_utm83                          | table | msjarvis
 public   | wvstateboundary100k_usgs_200203_ll83                            | table | msjarvis
 public   | wvstateboundary24k_usgs_200203_ll83                             | table | msjarvis
 public   | wvstateboundary24k_usgs_200203_utm83                            | table | msjarvis
 public   | wvstatehousedistricts_manysources_1992_ll83                     | table | msjarvis
 public   | wvstatehousedistricts_manysources_1992_utm83                    | table | msjarvis
 public   | wvstatehousedistricts_manysources_2002_ll83                     | table | msjarvis
 public   | wvstatehousedistricts_manysources_2002_utm83                    | table | msjarvis
 public   | wvstatehousedistricts_wvlegislativeservices_2020_utm83          | table | msjarvis
 public   | wvstatesenatedistricts_manysources_1992_ll83                    | table | msjarvis
 public   | wvstatesenatedistricts_manysources_1992_utm83                   | table | msjarvis
 public   | wvstatesenatedistricts_manysources_2002_ll83                    | table | msjarvis
 public   | wvstatesenatedistricts_manysources_2002_utm83                   | table | msjarvis
 public   | wvstatesenatedistricts_wvlegislativeservices_2020_utm83         | table | msjarvis
 public   | zcta5                                                           | table | msjarvis
 public   | zipcodetabulationarea_census_2020_utm83                         | table | msjarvis
 public   | zipcodetabulationarea_census_2020_wma84                         | table | msjarvis
 tiger    | addr                                                            | table | postgres
 tiger    | county_lookup                                                   | table | postgres
 tiger    | countysub_lookup                                                | table | postgres
 tiger    | direction_lookup                                                | table | postgres
 tiger    | featnames                                                       | table | postgres
 tiger    | geocode_settings                                                | table | postgres
 tiger    | geocode_settings_default                                        | table | postgres
 tiger    | loader_lookuptables                                             | table | postgres
 tiger    | loader_platform                                                 | table | postgres
 tiger    | loader_variables                                                | table | postgres
 tiger    | pagc_gaz                                                        | table | postgres
 tiger    | pagc_lex                                                        | table | postgres
 tiger    | pagc_rules                                                      | table | postgres
 tiger    | place_lookup                                                    | table | postgres
 tiger    | secondary_unit_lookup                                           | table | postgres
 tiger    | state_lookup                                                    | table | postgres
 tiger    | street_type_lookup                                              | table | postgres
 tiger    | tabblock                                                        | table | postgres
 tiger    | zip_lookup                                                      | table | postgres
 tiger    | zip_lookup_all                                                  | table | postgres
 tiger    | zip_lookup_base                                                 | table | postgres
 tiger    | zip_state                                                       | table | postgres
 tiger    | zip_state_loc                                                   | table | postgres
 topology | layer                                                           | table | postgres
 topology | topology                                                        | table | postgres
(428 rows)

ERROR:  column "tablename" does not exist
LINE 1: SELECT schemaname, tablename, n_live_tup FROM pg_stat_user_t...
                           ^
(.venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ # geospatial_features (different from geospatialfeatures)
curl -s "http://localhost:8002/api/v2/tenants/default_tenant/databases/default_database/collections/77393847-dfe0-4b74-a2a6-3e23c4fb7ab9/count"

# address_points
curl -s "http://localhost:8002/api/v2/tenants/default_tenant/databases/default_database/collections/83e5ae3a-de6f-4511-8c4f-b55d894b050e/count"

# zcta_centroids
curl -s "http://localhost:8002/api/v2/tenants/default_tenant/databases/default_database/collections/b25f29af-9860-4523-a958-fa10d882f5d2/count"

# gis_wv_benefits
curl -s "http://localhost:8002/api/v2/tenants/default_tenant/databases/default_database/collections/39a7f546-c952-4b31-acd4-d29067a2162b/count"
(.venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ # Find what table name and DB the login function usesion uses
grep -n "users\|login\|password\|SELECT\|postgres\|DATABASE" /opt/msjarvis-rebuild/auth_api.py | head -40

# Find the DB connection setup
grep -n "asyncpg\|psycopg\|DATABASE_URL\|PG_\|POSTGRES" /opt/msjarvis-rebuild/auth_api.py | head -20
5:  GET  /login          — magic link token handler → sets cookie → redirect
187:@app.get("/login")
188:def login(token: str, response: Response):
(.venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ # Auth DB investigation
docker exec jarvis-auth-api env | grep -i "db\|postgres\|database\|redis"
grep -n "SELECT\|users\|DATABASE_URL\|login" /opt/msjarvis-rebuild/auth_api.py | head -30

# GIS collection counts (all 4)
for id in 77393847-dfe0-4b74-a2a6-3e23c4fb7ab9 83e5ae3a-de6f-4511-8c4f-b55d894b050e b25f29af-9860-4523-a958-fa10d882f5d2 39a7f546-c952-4b31-acd4-d29067a2162b; do
  echo -n "$id: "
  curl -s "http://localhost:8002/api/v2/tenants/default_tenant/databases/default_database/collections/$id/count"
  echo
done

# PostGIS table row counts
docker exec jarvis-local-resources-db psql -U postgres -d msjarvisgis \
  -c "SELECT tablename, n_live_tup FROM pg_stat_user_tables ORDER BY n_live_tup DESC LIMIT 10;"
DATABASE_URL=postgresql://postgres:postgres@jarvis-local-resources-db:5432/local_resources
REDIS_URL=redis://jarvis-redis:6379
POSTGRES_DSN=postgresql://postgres@jarvis-local-resources-db:5432/msjarvisgis
5:  GET  /login          — magic link token handler → sets cookie → redirect
187:@app.get("/login")
188:def login(token: str, response: Response):
77393847-dfe0-4b74-a2a6-3e23c4fb7ab9: 270
83e5ae3a-de6f-4511-8c4f-b55d894b050e: 0
b25f29af-9860-4523-a958-fa10d882f5d2: 829
39a7f546-c952-4b31-acd4-d29067a2162b: 0
ERROR:  column "tablename" does not exist
LINE 1: SELECT tablename, n_live_tup FROM pg_stat_user_tables ORDER ...
               ^
(.venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ 

