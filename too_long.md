crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ echo "=== msjarvisgis-recovery databases ==="
docker exec msjarvisgis-recovery psql -U postgres -c "\l"

echo ""
echo "=== jarvis-local-resources-db databases ==="
docker exec jarvis-local-resources-db psql -U postgres -c "\l"

echo ""
echo "=== msjarvis-db databases (if exists) ==="
docker exec msjarvis-db psql -U postgres -c "\l" 2>/dev/null || echo "msjarvis-db container not found or not running"
=== msjarvisgis-recovery databases ===
                                                 List of databases
    Name     |  Owner   | Encoding |  Collate   |   Ctype    | ICU Locale | Locale Provider |   Access privileges   
-------------+----------+----------+------------+------------+------------+-----------------+-----------------------
 msjarvisgis | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 postgres    | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 template0   | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/postgres          +
             |          |          |            |            |            |                 | postgres=CTc/postgres
 template1   | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/postgres          +
             |          |          |            |            |            |                 | postgres=CTc/postgres
(4 rows)


=== jarvis-local-resources-db databases ===
                                                    List of databases
       Name       |  Owner   | Encoding |  Collate   |   Ctype    | ICU Locale | Locale Provider |   Access privileges   
------------------+----------+----------+------------+------------+------------+-----------------+-----------------------
 local_resources  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =Tc/postgres         +
                  |          |          |            |            |            |                 | postgres=CTc/postgres+
                  |          |          |            |            |            |                 | msjarvis=CTc/postgres
 msjarvisgis      | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 postgres         | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 template0        | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/postgres          +
                  |          |          |            |            |            |                 | postgres=CTc/postgres
 template1        | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/postgres          +
                  |          |          |            |            |            |                 | postgres=CTc/postgres
 template_postgis | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
(6 rows)


=== msjarvis-db databases (if exists) ===
                                                 List of databases
    Name     |  Owner   | Encoding |  Collate   |   Ctype    | ICU Locale | Locale Provider |   Access privileges   
-------------+----------+----------+------------+------------+------------+-----------------+-----------------------
 msjarvisgis | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =Tc/postgres         +
             |          |          |            |            |            |                 | postgres=CTc/postgres+
             |          |          |            |            |            |                 | msjarvis=CTc/postgres
 postgres    | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 template0   | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/postgres          +
             |          |          |            |            |            |                 | postgres=CTc/postgres
 template1   | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/postgres          +
             |          |          |            |            |            |                 | postgres=CTc/postgres
(4 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ echo "=== msjarvisgis-recovery/msjarvisgis tables ==="
docker exec msjarvisgis-recovery psql -U postgres -d msjarvisgis -c "
SELECT schemaname, tablename, 
       pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) AS size,
       (SELECT count(*) FROM information_schema.columns WHERE table_schema=schemaname AND table_name=tablename) AS columns
FROM pg_tables 
WHERE schemaname NOT IN ('pg_catalog', 'information_schema')
ORDER BY schemaname, tablename;
"

echo ""
echo "=== jarvis-local-resources-db/msjarvisgis tables ==="
docker exec jarvis-local-resources-db psql -U postgres -d msjarvisgis -c "
SELECT schemaname, tablename, 
       pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) AS size,
       (SELECT count(*) FROM information_schema.columns WHERE table_schema=schemaname AND table_name=tablename) AS columns
FROM pg_tables 
WHERE schemaname NOT IN ('pg_catalog', 'information_schema')
ORDER BY schemaname, tablename;
"
=== msjarvisgis-recovery/msjarvisgis tables ===
   schemaname    |                            tablename                            |    size    | columns 
-----------------+-----------------------------------------------------------------+------------+---------
 cakidd          | bldg_join__flood_structures_at_risk                             | 8192 bytes |       9
 cakidd          | bldg_join__nearest_hospital                                     | 157 MB     |      10
 cakidd          | gbim_authorities                                                | 16 kB      |       5
 cakidd          | gbim_belief_relations                                           | 16 kB      |       7
 cakidd          | gbim_beliefs                                                    | 16 kB      |      12
 cakidd          | gbim_evidence                                                   | 16 kB      |      13
 cakidd          | gbim_graph_edges                                                | 3018 MB    |       9
 cakidd          | gbim_worldview_entity                                           | 48 kB      |       7
 cakidd          | gbim_worldviews                                                 | 48 kB      |       7
 cakidd          | geospatial_features                                             | 32 kB      |      12
 cakidd          | redetermination_tracker                                         | 64 kB      |      14
 cakidd          | user_benefit_profile                                            | 8192 bytes |      10
 gbim            | building_metrics                                                | 130 MB     |       2
 gbim            | entity_relationship                                             | 360 MB     |       7
 gbim            | gbim_attrs                                                      | 2041 MB    |       8
 gbim            | priority_layers                                                 | 32 kB      |       3
 gbim            | worldview_entity                                                | 1213 MB    |       9
 gbim_source_csv | amtrackrails_federalrailroadadministration_200210_utm83         | 24 kB      |       8
 gbim_source_csv | blockgroups_census_2000_utm83                                   | 616 kB     |       8
 gbim_source_csv | blockgroups_census_201111_utm83                                 | 640 kB     |       8
 gbim_source_csv | blockgroups_census_2020_utm83                                   | 752 kB     |       8
 gbim_source_csv | blocks_census_2020_utm83                                        | 31 MB      |       8
 gbim_source_csv | boundaryappalachianbasin_wvges_1996_utm83                       | 168 kB     |       8
 gbim_source_csv | citieswithpopulation_2500_census_201111_utm83                   | 64 kB      |       8
 gbim_source_csv | citieswithpopulationover10k_uscensus_1990_utm83                 | 24 kB      |       8
 gbim_source_csv | citieswithpopulationsover10k_census_2020_utm83                  | 24 kB      |       8
 gbim_source_csv | citieswithpopulationsover2500_census_2020_utm83                 | 64 kB      |       8
 gbim_source_csv | citieswithpopulatoinover2500_uscensus_1990_utm83                | 96 kB      |       8
 gbim_source_csv | coals2_utm83                                                    | 24 kB      |       8
 gbim_source_csv | communityboundary_min_att_20250121_utm83                        | 160 kB     |       8
 gbim_source_csv | communityhealthproviders_wvhealthcareauthority_200802_utm83     | 72 kB      |       8
 gbim_source_csv | correctionalinstitutions_hsip_20091230_utm83                    | 64 kB      |       8
 gbim_source_csv | countycityparkboundaries_20201104_utm83                         | 272 kB     |       8
 gbim_source_csv | countyseats_usgs_utm83                                          | 56 kB      |       8
 gbim_source_csv | courthousescounty_manysources_200203_utm83                      | 56 kB      |       8
 gbim_source_csv | cvfault_utm83                                                   | 24 kB      |       8
 gbim_source_csv | cvpoly_utm83                                                    | 56 kB      |       8
 gbim_source_csv | dams_usarmycorpsofengineers_200010_utm83                        | 184 kB     |       8
 gbim_source_csv | damsnoncoal_usgs_2002_utm83                                     | 144 kB     |       8
 gbim_source_csv | empowermentzonesandenterprisecommunities_uscensus_2002_utm83    | 24 kB      |       8
 gbim_source_csv | excursionpassengertrains_wvdof_200102_utm83                     | 24 kB      |       8
 gbim_source_csv | facilities_epa_200203_utm83                                     | 496 kB     |       8
 gbim_source_csv | fire_dept_wvdem_092017_utm83                                    | 152 kB     |       8
 gbim_source_csv | floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83  | 19 MB      |       8
 gbim_source_csv | geographicalnamesonusgstopomaps_usgs_200601_utm83               | 10 MB      |       8
 gbim_source_csv | geographicnamesonusgstopomaps_current_usgs_20110801_utm83       | 7544 kB    |       8
 gbim_source_csv | geographicnamesonusgstopomaps_historical_usgs_20110801_utm83    | 3016 kB    |       8
 gbim_source_csv | geographicnamesonusgstopomaps_usgs_20110801_utm83               | 8952 kB    |       8
 gbim_source_csv | hazardmitigationbuyout_20250929_polygons_utm83                  | 1168 kB    |       8
 gbim_source_csv | healthruralfacilities_manysources_utm83                         | 56 kB      |       8
 gbim_source_csv | highered_wvemd_072420_utm83                                     | 56 kB      |       8
 gbim_source_csv | historicalaerialphotographycountycoverage_wvgistc_utm83         | 64 kB      |       8
 gbim_source_csv | hospitals_wvdem_040519_utm83                                    | 56 kB      |       8
 gbim_source_csv | indexgrid15minutequads_wvgistc_utm83                            | 288 kB     |       8
 gbim_source_csv | industrialbuildings_wvdo_200807_utm83                           | 64 kB      |       8
 gbim_source_csv | industrialparks_wvdo_200078_utm83                               | 80 kB      |       8
 gbim_source_csv | industrialsites_wvdo_200807_utm83                               | 104 kB     |       8
 gbim_source_csv | inedexgrid1minutequads_wvgistc_utm83                            | 56 kB      |       8
 gbim_source_csv | intermodalterminalfacilities_usdot_1997_utm83                   | 72 kB      |       8
 gbim_source_csv | libraries_manysources_2001_utm83                                | 88 kB      |       8
 gbim_source_csv | majorriversandlakesline_nhd_2002_utm83                          | 64 kB      |       8
 gbim_source_csv | majorriversandlakespolygon_nhd_2002_utm83                       | 72 kB      |       8
 gbim_source_csv | manufacturingandbusiness_wvdo_200803_utm83                      | 2072 kB    |       8
 gbim_source_csv | metropolitanandmicropolitanstatisticalareas_census_201111_utm83 | 16 kB      |       8
 gbim_source_csv | metropolitanandmicropolitanstatisticalareas_census_2020_utm83   | 24 kB      |       8
 gbim_source_csv | metropolitanstatisticalareas_uscensus_199901_utm83              | 24 kB      |       8
 gbim_source_csv | mineraloperations_usgs_200204_utm83                             | 56 kB      |       8
 gbim_source_csv | nationalatlasstreams_usgs_199903_utm83                          | 552 kB     |       8
 gbim_source_csv | nationalwaterwaynetwork_usarmycorpsofengineers_2001_utm83       | 80 kB      |       8
 gbim_source_csv | nationalwaterwaynetworkports_usarmycorpsofengineers_2001_utm83  | 24 kB      |       8
 gbim_source_csv | naviagablewaterways_usarmycropsofengineers_2006_utm83           | 24 kB      |       8
 gbim_source_csv | navigablewaterwaysrivermiles_usarmycropsofengineers_2006_utm83  | 152 kB     |       8
 gbim_source_csv | navigablewaterwaysstructures_usarmycorpsofengineers_2006_utm83  | 8080 kB    |       8
 gbim_source_csv | nursinghomes_wvdem_041219_utm83                                 | 64 kB      |       8
 gbim_source_csv | officebuildings_wvdo_200807_utm83                               | 56 kB      |       8
 gbim_source_csv | paroleoffices_manysources_2008_utm83                            | 24 kB      |       8
 gbim_source_csv | placesofworship_hsip_20080723_utm83                             | 56 kB      |       8
 gbim_source_csv | policedept_wvdem_012319_utm83                                   | 112 kB     |       8
 gbim_source_csv | populatedplaces_census_201112_utm83                             | 128 kB     |       8
 gbim_source_csv | populatedplaces_census_2020_utm83                               | 136 kB     |       8
 gbim_source_csv | populatedplaces_uscensus_1990_utm83                             | 96 kB      |       8
 gbim_source_csv | populationdatablockgroups_uscensus_2000_utm83                   | 664 kB     |       8
 gbim_source_csv | pow_wvgistc_062919_utm83                                        | 1216 kB    |       8
 gbim_source_csv | publichealthdepts_hsip_20091229_utm83                           | 56 kB      |       8
 gbim_source_csv | railnetworkregion_usdot_200203_utm83                            | 4648 kB    |       8
 gbim_source_csv | railnetworkwv_usdot_200203_utm83                                | 976 kB     |       8
 gbim_source_csv | railroads_rahalltransportationinstitute_2005_utm83              | 1088 kB    |       8
 gbim_source_csv | realtimestreamflowstations_usgs_200012_utm83                    | 56 kB      |       8
 gbim_source_csv | recreationalwwtrails_ofwv_20151117_utm83                        | 136 kB     |       8
 gbim_source_csv | regionalplanninganddevelopmentcouncil_wvdo_1971_utm83           | 64 kB      |       8
 gbim_source_csv | sewertreatmentplants_wvdep_200203_utm83                         | 344 kB     |       8
 gbim_source_csv | solidwastefacilities_wvdep_200202_utm83                         | 56 kB      |       8
 gbim_source_csv | springs_wvges_1986_utm83                                        | 88 kB      |       8
 gbim_source_csv | structurepointsnorth_samb_2003_utm83                            | 138 MB     |       8
 gbim_source_csv | structurepointssouth_samb_2003_utm83                            | 165 MB     |       8
 gbim_source_csv | structurepolygons_samb_2003_utm83                               | 5856 kB    |       8
 gbim_source_csv | timberremovalvolume_usfs_1996_utm83                             | 64 kB      |       8
 gbim_source_csv | towers_wvpublicbroadcasting_2002_utm83                          | 24 kB      |       8
 gbim_source_csv | towersam_fcc_200202_utm83                                       | 56 kB      |       8
 gbim_source_csv | towersasr_fcc_200202_utm83                                      | 216 kB     |       8
 gbim_source_csv | towerscellular_fcc_200202_utm83                                 | 88 kB      |       8
 gbim_source_csv | towersfm_fcc_200202_utm83                                       | 56 kB      |       8
 gbim_source_csv | towersmicrowave_fcc_200202_utm83                                | 512 kB     |       8
 gbim_source_csv | towerspager_fcc_200202_utm83                                    | 88 kB      |       8
 gbim_source_csv | towersprivate_fcc_200202_utm83                                  | 1288 kB    |       8
 gbim_source_csv | veteransaffairsfacilities_manysources_200503_utm83              | 24 kB      |       8
 gbim_source_csv | votingdistrictswv_legislativeservices_2002_utm83                | 800 kB     |       8
 gbim_source_csv | votingdistrictswv_uscensus_2000_utm83                           | 608 kB     |       8
 gbim_source_csv | windenergyresource_nationalrenewableenergylab_200901_utm83      | 41 MB      |       8
 gbim_source_csv | wv_county_boundaries_24k_topo_updated_2022_utm83                | 64 kB      |       8
 gbim_source_csv | wv_tax_districts_utm83                                          | 256 kB     |       8
 gbim_source_csv | wvstatebounadary100k_usgs_200203_utm83                          | 24 kB      |       8
 gbim_source_csv | wvstateboundary24k_usgs_200203_utm83                            | 24 kB      |       8
 gbim_source_csv | wvstatehousedistricts_manysources_1992_utm83                    | 64 kB      |       8
 gbim_source_csv | wvstatehousedistricts_manysources_2002_utm83                    | 64 kB      |       8
 gbim_source_csv | wvstatehousedistricts_wvlegislativeservices_2020_utm83          | 80 kB      |       8
 gbim_source_csv | wvstatesenatedistricts_manysources_1992_utm83                   | 24 kB      |       8
 gbim_source_csv | wvstatesenatedistricts_manysources_2002_utm83                   | 24 kB      |       8
 gbim_source_csv | wvstatesenatedistricts_wvlegislativeservices_2020_utm83         | 24 kB      |       8
 gbim_source_csv | zipcodetabulationarea_census_2020_utm83                         | 336 kB     |       8
 public          | 911centers_wvdem_032819_gcs84                                   | 16 kB      |       5
 public          | 911centers_wvdem_032819_gcs84_attrs_raw                         | 16 kB      |       7
 public          | 911centers_wvdem_032819_utm83                                   | 16 kB      |       5
 public          | 911centers_wvdem_032819_utm83_attrs_raw                         | 16 kB      |       7
 public          | amtrackrails_federalrailroadadministration_200210_ll83          | 16 kB      |       5
 public          | amtrackrails_federalrailroadadministration_200210_ll83_attrs_ra | 16 kB      |       7
 public          | amtrackrails_federalrailroadadministration_200210_utm83         | 16 kB      |       5
 public          | amtrackrails_federalrailroadadministration_200210_utm83_attrs_r | 16 kB      |       7
 public          | amtrackrails_fra_200210_ll83_attrs_raw                          | 16 kB      |       7
 public          | amtrackrails_fra_200210_utm83_attrs_raw                         | 16 kB      |       7
 public          | attrs_files_list                                                | 104 kB     |       4
 public          | attrs_inventory_detailed                                        | 104 kB     |      10
 public          | authority_references                                            | 32 kB      |       7
 public          | benefit_case                                                    | 32 kB      |       6
 public          | benefit_county_daycare                                          | 24 kB      |       8
 public          | benefit_county_medicaid                                         | 24 kB      |       8
 public          | benefit_county_medicare                                         | 24 kB      |       8
 public          | benefit_county_section8                                         | 24 kB      |       8
 public          | benefit_county_snap                                             | 24 kB      |       8
 public          | benefit_county_ssi                                              | 24 kB      |       8
 public          | benefit_county_tanf                                             | 24 kB      |       8
 public          | benefit_county_utility20                                        | 40 kB      |       8
 public          | benefit_county_wic                                              | 24 kB      |       8
 public          | bldg_join__floodplainstructuresatrisk_usarmycorpsofengineers_20 | 8192 bytes |       9
 public          | bldg_join__hospitals                                            | 157 MB     |      10
 public          | blockgroups_census_2000_ll83                                    | 200 kB     |       5
 public          | blockgroups_census_2000_ll83_attrs_raw                          | 496 kB     |       7
 public          | blockgroups_census_2000_utm83                                   | 200 kB     |       5
 public          | blockgroups_census_2000_utm83_attrs_raw                         | 496 kB     |       7
 public          | blockgroups_census_201111_gcs83                                 | 216 kB     |       5
 public          | blockgroups_census_201111_gcs83_attrs_raw                       | 432 kB     |       7
 public          | blockgroups_census_201111_utm83                                 | 216 kB     |       5
 public          | blockgroups_census_201111_utm83_attrs_raw                       | 512 kB     |       7
 public          | blockgroups_census_2020_utm83                                   | 304 kB     |       5
 public          | blockgroups_census_2020_utm83_attrs_raw                         | 616 kB     |       7
 public          | blockgroups_census_2020_utm83_full                              | 25 MB      |      10
 public          | blockgroups_census_2020_wma84                                   | 216 kB     |       5
 public          | blockgroups_census_2020_wma84_attrs_raw                         | 528 kB     |       7
 public          | blocks_census_2020_utm83                                        | 12 MB      |       5
 public          | blocks_census_2020_utm83_attrs_raw                              | 25 MB      |       7
 public          | blocks_census_2020_utm83_full                                   | 172 MB     |      10
 public          | blocks_census_2020_wma84                                        | 7704 kB    |       5
 public          | blocks_census_2020_wma84_attrs_raw                              | 21 MB      |       7
 public          | boundaryappalachianbasin_wvges_1996_utm83                       | 72 kB      |       5
 public          | boundaryappalachianbasin_wvges_1996_utm83_attrs_raw             | 128 kB     |       7
 public          | boundaryappalachianbasin_wvges_1996_wma84                       | 72 kB      |       5
 public          | bridges                                                         | 648 kB     |       5
 public          | bridges_attrs_raw                                               | 928 kB     |       7
 public          | building_flood_risk                                             | 21 MB      |       7
 public          | building_metric_stage                                           | 32 kB      |       5
 public          | buildings                                                       | 448 MB     |       2
 public          | calderl_reg_ll83                                                | 16 kB      |       5
 public          | calderl_reg_ll83_attrs_raw                                      | 16 kB      |       7
 public          | citieswithpopulation_2500_census_201111_gcs83                   | 16 kB      |       5
 public          | citieswithpopulation_2500_census_201111_gcs83_attrs_raw         | 56 kB      |       7
 public          | citieswithpopulation_2500_census_201111_utm83                   | 16 kB      |       5
 public          | citieswithpopulation_2500_census_201111_utm83_attrs_raw         | 56 kB      |       7
 public          | citieswithpopulationover10k_census_201111_gcs83                 | 16 kB      |       5
 public          | citieswithpopulationover10k_census_201111_gcs83_attrs_raw       | 16 kB      |       7
 public          | citieswithpopulationover10k_uscensus_1990_ll83                  | 16 kB      |       5
 public          | citieswithpopulationover10k_uscensus_1990_ll83_attrs_raw        | 16 kB      |       7
 public          | citieswithpopulationover10k_uscensus_1990_utm83                 | 16 kB      |       5
 public          | citieswithpopulationover10k_uscensus_1990_utm83_attrs_raw       | 16 kB      |       7
 public          | citieswithpopulationover2500_uscensus_1990_ll83                 | 72 kB      |       5
 public          | citieswithpopulationover2500_uscensus_1990_ll83_attrs_raw       | 80 kB      |       7
 public          | citieswithpopulationsover10k_census_2020_utm83                  | 16 kB      |       5
 public          | citieswithpopulationsover10k_census_2020_utm83_attrs_raw        | 16 kB      |       7
 public          | citieswithpopulationsover10k_census_2020_wma84                  | 16 kB      |       5
 public          | citieswithpopulationsover10k_census_2020_wma84_attrs_raw        | 16 kB      |       7
 public          | citieswithpopulationsover2500_census_2020_utm83                 | 16 kB      |       5
 public          | citieswithpopulationsover2500_census_2020_utm83_attrs_raw       | 56 kB      |       7
 public          | citieswithpopulationsover2500_census_2020_wma84                 | 16 kB      |       5
 public          | citieswithpopulationsover2500_census_2020_wma84_attrs_raw       | 56 kB      |       7
 public          | citieswithpopulatoinover2500_uscensus_1990_utm83                | 72 kB      |       5
 public          | citieswithpopulatoinover2500_uscensus_1990_utm83_attrs_raw      | 80 kB      |       7
 public          | client_utility_account                                          | 32 kB      |       4
 public          | coals2_ll83                                                     | 16 kB      |       5
 public          | coals2_ll83_attrs_raw                                           | 16 kB      |       7
 public          | coals2_utm27                                                    | 16 kB      |       5
 public          | coals2_utm27_attrs_raw                                          | 16 kB      |       7
 public          | coals2_utm83                                                    | 16 kB      |       5
 public          | coals2_utm83_attrs_raw                                          | 16 kB      |       7
 public          | community_points                                                | 72 kB      |      11
 public          | communityboundary_min_att_20250121_utm83                        | 72 kB      |       5
 public          | communityboundary_min_att_20250121_utm83_attrs_raw              | 120 kB     |       7
 public          | communityboundary_min_att_20250121_wma84                        | 72 kB      |       5
 public          | communityboundary_min_att_20250121_wma84_attrs_raw              | 128 kB     |       7
 public          | communityhealthproviders_wvhealthcareauthority_200802_utm83     | 32 kB      |       5
 public          | communityhealthproviders_wvhealthcareauthority_200802_utm83_att | 104 kB     |       7
 public          | correctionalinstitutions_hsip_20091230_utm83                    | 48 kB      |       5
 public          | correctionalinstitutions_hsip_20091230_utm83_attrs_raw          | 56 kB      |       7
 public          | correctionalinstitutions_hsip_20091230_wgs84                    | 48 kB      |       5
 public          | correctionalinstitutions_hsip_20091230_wgs84_attrs_raw          | 56 kB      |       7
 public          | countycityparkboundaries_20201104_utm83                         | 104 kB     |       5
 public          | countycityparkboundaries_20201104_utm83_attrs_raw               | 216 kB     |       7
 public          | countyseats_usgs_ll83                                           | 16 kB      |       5
 public          | countyseats_usgs_ll83_attrs_raw                                 | 16 kB      |       7
 public          | countyseats_usgs_utm83                                          | 16 kB      |       5
 public          | countyseats_usgs_utm83_attrs_raw                                | 16 kB      |       7
 public          | courthousescounty_manysources_200203_ll83                       | 16 kB      |       5
 public          | courthousescounty_manysources_200203_ll83_attrs_raw             | 48 kB      |       7
 public          | courthousescounty_manysources_200203_utm83                      | 8192 bytes |       5
 public          | courthousescounty_manysources_200203_utm83_attrs_raw            | 8192 bytes |       7
 public          | courthousesfederal_manysources_200203_ll83                      | 8192 bytes |       5
 public          | courthousesfederal_manysources_200203_ll83_attrs_raw            | 8192 bytes |       7
 public          | courthousesfederal_manysources_200203_utm                       | 8192 bytes |       5
 public          | courthousesfederal_manysources_200203_utm_attrs_raw             | 8192 bytes |       7
 public          | cvfault_ll83                                                    | 16 kB      |       5
 public          | cvfault_ll83_attrs_raw                                          | 16 kB      |       7
 public          | cvfault_utm27                                                   | 16 kB      |       5
 public          | cvfault_utm27_attrs_raw                                         | 16 kB      |       7
 public          | cvfault_utm83                                                   | 16 kB      |       5
 public          | cvfault_utm83_attrs_raw                                         | 16 kB      |       7
 public          | cvpoly_ll83                                                     | 16 kB      |       5
 public          | cvpoly_ll83_attrs_raw                                           | 48 kB      |       7
 public          | cvpoly_utm27                                                    | 16 kB      |       5
 public          | cvpoly_utm27_attrs_raw                                          | 48 kB      |       7
 public          | cvpoly_utm83                                                    | 16 kB      |       5
 public          | cvpoly_utm83_attrs_raw                                          | 48 kB      |       7
 public          | dams_usarmycorpsofengineers_200010_utm83                        | 104 kB     |       5
 public          | dams_usarmycorpsofengineers_200010_utm83_attrs_raw              | 120 kB     |       7
 public          | dams_usarmycropsofengineers_200010_ll83                         | 104 kB     |       5
 public          | dams_usarmycropsofengineers_200010_ll83_attrs_raw               | 120 kB     |       7
 public          | damsnoncoal_usgs_2002_ll27                                      | 88 kB      |       5
 public          | damsnoncoal_usgs_2002_ll27_attrs_raw                            | 96 kB      |       7
 public          | damsnoncoal_usgs_2002_utm83                                     | 88 kB      |       5
 public          | damsnoncoal_usgs_2002_utm83_attrs_raw                           | 104 kB     |       7
 public          | empowermentzonesandenterprisecommunities_uscensus_2002_utm83    | 16 kB      |       5
 public          | empowermentzonesandenterprisecommunities_uscensus_2002_utm83_at | 16 kB      |       7
 public          | empowermentzonesandenterprisecommunitiesbytractuscens30c72907   | 96 kB      |       5
 public          | empowermentzonesandenterprisecommunitiesbytractuscens30c72907at | 184 kB     |       7
 public          | evidence_documents                                              | 32 kB      |       8
 public          | excursionpassengertrains_wvdof_200102_ll83                      | 16 kB      |       5
 public          | excursionpassengertrains_wvdof_200102_ll83_attrs_raw            | 16 kB      |       7
 public          | excursionpassengertrains_wvdof_200102_utm83                     | 16 kB      |       5
 public          | excursionpassengertrains_wvdof_200102_utm83_attrs_raw           | 16 kB      |       7
 public          | facilities_epa_200203_ll83                                      | 272 kB     |       5
 public          | facilities_epa_200203_ll83_attrs_raw                            | 336 kB     |       7
 public          | facilities_epa_200203_utm83                                     | 272 kB     |       5
 public          | facilities_epa_200203_utm83_attrs_raw                           | 336 kB     |       7
 public          | fault_reg_ll83                                                  | 48 kB      |       5
 public          | fault_reg_ll83_attrs_raw                                        | 72 kB      |       7
 public          | faultgl_reg_ll83                                                | 4224 kB    |       5
 public          | faultgl_reg_ll83_attrs_raw                                      | 12 MB      |       7
 public          | features                                                        | 11 MB      |       5
 public          | features_attrs_raw                                              | 24 MB      |       7
 public          | fire_departments                                                | 88 kB      |       5
 public          | fire_departments_attrs_raw                                      | 104 kB     |       7
 public          | fire_dept_wvdem_092017_utm83                                    | 96 kB      |       5
 public          | fire_dept_wvdem_092017_utm83_attrs_raw                          | 112 kB     |       7
 public          | floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83  | 11 MB      |       5
 public          | floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83_ | 13 MB      |       7
 public          | gbim_belief                                                     | 16 kB      |       8
 public          | gbim_belief_edges                                               | 24 kB      |       9
 public          | gbim_belief_evidence                                            | 231 MB     |       5
 public          | gbim_beliefs                                                    | 2531 MB    |      12
 public          | gbim_entities                                                   | 224 kB     |      10
 public          | gbim_entity_clusters                                            | 192 kB     |       6
 public          | gbim_entity_land_candidates                                     | 11 MB      |       5
 public          | gbim_evidence                                                   | 501 MB     |      10
 public          | gbim_full_points                                                | 299 MB     |       7
 public          | gbim_full_points_raw                                            | 132 MB     |       7
 public          | gbim_layer_catalog                                              | 72 kB      |       6
 public          | gbim_layer_config                                               | 32 kB      |       9
 public          | gbim_layer_manifest                                             | 88 kB      |       3
 public          | gbim_source_epochs                                              | 88 kB      |       3
 public          | gbim_source_tables_used                                         | 48 kB      |       1
 public          | gbim_worldview_entity                                           | 9219 MB    |      18
 public          | gbim_worldview_entity_backup_small                              | 160 kB     |       8
 public          | gbim_worldviews                                                 | 48 kB      |       9
 public          | gbimbeliefnormalized                                            | 12 GB      |      12
 public          | geographicalnamesonusgstopomaps_usgs_200601_ll27                | 5816 kB    |       5
 public          | geographicalnamesonusgstopomaps_usgs_200601_ll27_attrs_raw      | 6528 kB    |       7
 public          | geographicalnamesonusgstopomaps_usgs_200601_utm83               | 5888 kB    |       5
 public          | geographicalnamesonusgstopomaps_usgs_200601_utm83_attrs_raw     | 7336 kB    |       7
 public          | geographicnamesonusgstopomaps_current_usgs_20110801_ll83        | 4288 kB    |       5
 public          | geographicnamesonusgstopomaps_current_usgs_20110801_ll83_attrs_ | 5344 kB    |       7
 public          | geographicnamesonusgstopomaps_current_usgs_20110801_utm83       | 4352 kB    |       5
 public          | geographicnamesonusgstopomaps_current_usgs_20110801_utm83_attrs | 5368 kB    |       7
 public          | geographicnamesonusgstopomaps_historical_usgs_20110801_ll83     | 1048 kB    |       5
 public          | geographicnamesonusgstopomaps_historical_usgs_20110801_ll83_att | 1192 kB    |       7
 public          | geographicnamesonusgstopomaps_historical_usgs_20110801_utm83    | 1048 kB    |       5
 public          | geographicnamesonusgstopomaps_historical_usgs_20110801_utm83_at | 1328 kB    |       7
 public          | geographicnamesonusgstopomaps_usgs_20110801_ll83                | 5016 kB    |       5
 public          | geographicnamesonusgstopomaps_usgs_20110801_ll83_attrs_raw      | 6192 kB    |       7
 public          | geographicnamesonusgstopomaps_usgs_20110801_utm83               | 5088 kB    |       5
 public          | geographicnamesonusgstopomaps_usgs_20110801_utm83_attrs_raw     | 6352 kB    |       7
 public          | geolgyl_reg_ll83                                                | 208 kB     |       5
 public          | geolgyl_reg_ll83_attrs_raw                                      | 560 kB     |       7
 public          | geolgyp_reg_ll83                                                | 56 kB      |       5
 public          | geolgyp_reg_ll83_attrs_raw                                      | 88 kB      |       7
 public          | geospatial_features                                             | 7104 kB    |      24
 public          | geospatial_layers                                               | 32 kB      |       7
 public          | geotextl_reg_ll83                                               | 48 kB      |       5
 public          | geotextl_reg_ll83_attrs_raw                                     | 64 kB      |       7
 public          | glacagl_reg_ll83                                                | 48 kB      |       5
 public          | glacagl_reg_ll83_attrs_raw                                      | 72 kB      |       7
 public          | glacal_reg_ll83                                                 | 16 kB      |       5
 public          | glacal_reg_ll83_attrs_raw                                       | 16 kB      |       7
 public          | hazardmitigationbuyout_20250929_polygons_utm83                  | 400 kB     |       5
 public          | hazardmitigationbuyout_20250929_polygons_utm83_attrs_raw        | 920 kB     |       7
 public          | hazardmitigationbuyout_20250929_polygons_wma84                  | 400 kB     |       5
 public          | hazardmitigationbuyout_20250929_polygons_wma84_attrs_raw        | 968 kB     |       7
 public          | healthruralfacilities_manysources_utm83                         | 16 kB      |       5
 public          | healthruralfacilities_manysources_utm83_attrs_raw               | 56 kB      |       7
 public          | highered_wvemd_072420_utm83                                     | 16 kB      |       5
 public          | highered_wvemd_072420_utm83_attrs_raw                           | 16 kB      |       7
 public          | highered_wvemd_072420_wgc84                                     | 16 kB      |       5
 public          | highered_wvemd_072420_wgc84_attrs_raw                           | 16 kB      |       7
 public          | historicalaerialphotographycountycoverage_wvgistc_utm83         | 16 kB      |       5
 public          | historicalaerialphotographycountycoverage_wvgistc_utm83_attrs_r | 56 kB      |       7
 public          | hospitals                                                       | 24 kB      |       5
 public          | hospitals_attrs_raw                                             | 16 kB      |       7
 public          | hospitals_wvdem_040519_gcs84                                    | 16 kB      |       5
 public          | hospitals_wvdem_040519_gcs84_attrs_raw                          | 64 kB      |       7
 public          | hospitals_wvdem_040519_utm83                                    | 16 kB      |       5
 public          | hospitals_wvdem_040519_utm83_attrs_raw                          | 64 kB      |       7
 public          | hospitalswvdem040519utm83                                       | 8192 bytes |       5
 public          | hospitalswvdem040519utm83_attrs_raw                             | 8192 bytes |       7
 public          | impact_reg_ll83                                                 | 16 kB      |       5
 public          | impact_reg_ll83_attrs_raw                                       | 16 kB      |       7
 public          | indexgrid15minutequads_wvgistc_ll83                             | 128 kB     |       5
 public          | indexgrid15minutequads_wvgistc_ll83_attrs_raw                   | 152 kB     |       7
 public          | indexgrid15minutequads_wvgistc_utm83                            | 112 kB     |       5
 public          | indexgrid15minutequads_wvgistc_utm83_attrs_raw                  | 232 kB     |       7
 public          | indexgrid15minutewithcounties_wvgistc_utm27                     | 136 kB     |       5
 public          | indexgrid15minutewithcounties_wvgistc_utm27_attrs_raw           | 296 kB     |       7
 public          | indexgrid1minutequads_wvgistc_ll83                              | 16 kB      |       5
 public          | indexgrid1minutequads_wvgistc_ll83_attrs_raw                    | 48 kB      |       7
 public          | industrialbuildings_wvdo_200807_utm83                           | 48 kB      |       5
 public          | industrialbuildings_wvdo_200807_utm83_attrs_raw                 | 56 kB      |       7
 public          | industrialparks_wvdo_200078_utm83                               | 48 kB      |       5
 public          | industrialparks_wvdo_200078_utm83_attrs_raw                     | 72 kB      |       7
 public          | industrialsites_wvdo_200807_utm83                               | 56 kB      |       5
 public          | industrialsites_wvdo_200807_utm83_attrs_raw                     | 96 kB      |       7
 public          | inedexgrid1minutequads_wvgistc_utm83                            | 16 kB      |       5
 public          | inedexgrid1minutequads_wvgistc_utm83_attrs_raw                  | 48 kB      |       7
 public          | intake_submissions                                              | 16 kB      |      10
 public          | intermodalterminalfacilities_usdot_1997_ll83                    | 56 kB      |       5
 public          | intermodalterminalfacilities_usdot_1997_ll83_attrs_raw          | 56 kB      |       7
 public          | intermodalterminalfacilities_usdot_1997_utm83                   | 56 kB      |       5
 public          | intermodalterminalfacilities_usdot_1997_utm83_attrs_raw         | 56 kB      |       7
 public          | layer_config                                                    | 88 kB      |       6
 public          | libraries_manysources_2001_ll27                                 | 64 kB      |       5
 public          | libraries_manysources_2001_ll27_attrs_raw                       | 72 kB      |       7
 public          | libraries_manysources_2001_utm83                                | 64 kB      |       5
 public          | libraries_manysources_2001_utm83_attrs_raw                      | 72 kB      |       7
 public          | local_resources                                                 | 240 kB     |      35
 public          | majorriversandlakesline_nhd_2002_ll83                           | 16 kB      |       5
 public          | majorriversandlakesline_nhd_2002_ll83_attrs_raw                 | 56 kB      |       7
 public          | majorriversandlakesline_nhd_2002_utm83                          | 16 kB      |       5
 public          | majorriversandlakesline_nhd_2002_utm83_attrs_raw                | 56 kB      |       7
 public          | majorriversandlakespolygon_nhd_2002_poly_ll83                   | 48 kB      |       5
 public          | majorriversandlakespolygon_nhd_2002_poly_ll83_attrs_raw         | 64 kB      |       7
 public          | majorriversandlakespolygon_nhd_2002_utm83                       | 48 kB      |       5
 public          | majorriversandlakespolygon_nhd_2002_utm83_attrs_raw             | 64 kB      |       7
 public          | manufacturingandbusiness_wvdo_200803_utm83                      | 1144 kB    |       5
 public          | manufacturingandbusiness_wvdo_200803_utm83_attrs_raw            | 1424 kB    |       7
 public          | metfacp_reg_ll83                                                | 16 kB      |       5
 public          | metfacp_reg_ll83_attrs_raw                                      | 16 kB      |       7
 public          | metropolitanandmicropolitanstatisticalareas_census_2020_utm83   | 16 kB      |       5
 public          | metropolitanandmicropolitanstatisticalareas_census_2020_utm83_a | 16 kB      |       7
 public          | metropolitanandmicropolitanstatisticalareas_census_2020_wma84   | 16 kB      |       5
 public          | metropolitanandmicropolitanstatisticalareas_census_2020_wma84_a | 16 kB      |       7
 public          | metropolitanandmicropolitanstatisticalareascensus201111gcs83    | 16 kB      |       5
 public          | metropolitanandmicropolitanstatisticalareascensus201111gcs83att | 48 kB      |       7
 public          | metropolitanandmicropolitanstatisticalareascensus201111utm83    | 16 kB      |       5
 public          | metropolitanandmicropolitanstatisticalareascensus201111utm83att | 48 kB      |       7
 public          | metropolitanstatisticalareas_uscensus_199901_ll83               | 16 kB      |       5
 public          | metropolitanstatisticalareas_uscensus_199901_ll83_attrs_raw     | 16 kB      |       7
 public          | metropolitanstatisticalareas_uscensus_199901_utm83              | 16 kB      |       5
 public          | metropolitanstatisticalareas_uscensus_199901_utm83_attrs_raw    | 16 kB      |       7
 public          | mineraloperations_usgs_200204_ll83                              | 16 kB      |       5
 public          | mineraloperations_usgs_200204_ll83_attrs_raw                    | 48 kB      |       7
 public          | mineraloperations_usgs_200204_utm83                             | 16 kB      |       5
 public          | mineraloperations_usgs_200204_utm83_attrs_raw                   | 48 kB      |       7
 public          | minesabandonedlandsline_wvdep_1996_noprojectoin                 | 1376 kB    |       5
 public          | minesabandonedlandsline_wvdep_1996_noprojectoin_attrs_raw       | 2600 kB    |       7
 public          | minesabandonedlandspoint_wvdep_1996_noprojection                | 64 kB      |       5
 public          | minesabandonedlandspoint_wvdep_1996_noprojection_attrs_raw      | 64 kB      |       7
 public          | minesabandonedlandspolygon_wvdep_1996_noprojection              | 320 kB     |       5
 public          | minesabandonedlandspolygon_wvdep_1996_noprojection_attrs_raw    | 552 kB     |       7
 public          | ms_jarvis_learning_log                                          | 15 MB      |       5
 public          | nationalatlasstreams_usgs_199903_ll83                           | 200 kB     |       5
 public          | nationalatlasstreams_usgs_199903_ll83_attrs_raw                 | 440 kB     |       7
 public          | nationalatlasstreams_usgs_199903_utm83                          | 200 kB     |       5
 public          | nationalatlasstreams_usgs_199903_utm83_attrs_raw                | 432 kB     |       7
 public          | nationalregister_point_20200923                                 | 120 kB     |       5
 public          | nationalregister_point_20200923_attrs_raw                       | 144 kB     |       7
 public          | nationalregister_point_20200923_utm27                           | 120 kB     |       5
 public          | nationalregister_point_20200923_utm27_attrs_raw                 | 144 kB     |       7
 public          | nationalwaterwaynetwork_usarmycorpsofengineers_2001_ll83        | 48 kB      |       5
 public          | nationalwaterwaynetwork_usarmycorpsofengineers_2001_ll83_attrs_ | 64 kB      |       7
 public          | nationalwaterwaynetwork_usarmycorpsofengineers_2001_utm83       | 48 kB      |       5
 public          | nationalwaterwaynetwork_usarmycorpsofengineers_2001_utm83_attrs | 64 kB      |       7
 public          | nationalwaterwaynetworkports_usarmycorpsofengineers_2001_ll83   | 16 kB      |       5
 public          | nationalwaterwaynetworkports_usarmycorpsofengineers_2001_ll83_a | 16 kB      |       7
 public          | nationalwaterwaynetworkports_usarmycorpsofengineers_2001_utm83  | 16 kB      |       5
 public          | nationalwaterwaynetworkports_usarmycorpsofengineers_2001_utm83_ | 16 kB      |       7
 public          | naviagablewaterways_usarmycropsofengineers_2006_utm83           | 16 kB      |       5
 public          | naviagablewaterways_usarmycropsofengineers_2006_utm83_attrs_raw | 16 kB      |       7
 public          | navigablewaterwaysrivermiles_usarmycropsofengineers_2006_utm83  | 96 kB      |       5
 public          | navigablewaterwaysrivermiles_usarmycropsofengineers_2006_utm83_ | 112 kB     |       7
 public          | navigablewaterwaysstructures_usarmycorpsofengineers_2006_utm83  | 4472 kB    |       5
 public          | navigablewaterwaysstructures_usarmycorpsofengineers_2006_utm83_ | 5696 kB    |       7
 public          | nursinghomes_wvdem_041219_gcs84                                 | 24 kB      |       5
 public          | nursinghomes_wvdem_041219_gcs84_attrs_raw                       | 80 kB      |       7
 public          | nursinghomes_wvdem_041219_utm83                                 | 48 kB      |       5
 public          | nursinghomes_wvdem_041219_utm83_attrs_raw                       | 80 kB      |       7
 public          | officebuildings_wvdo_200807_utm83                               | 48 kB      |       5
 public          | officebuildings_wvdo_200807_utm83_attrs_raw                     | 48 kB      |       7
 public          | osm_clinics_wv                                                  | 232 kB     |       8
 public          | osm_clinics_wv_filtered                                         | 32 kB      |       8
 public          | osm_hospitals_wv                                                | 112 kB     |       8
 public          | osm_nursinghomes_wv                                             | 56 kB      |       8
 public          | osm_nursinghomes_wv_filtered                                    | 24 kB      |       8
 public          | paroleoffices_manysources_2008_utm83                            | 16 kB      |       5
 public          | paroleoffices_manysources_2008_utm83_attrs_raw                  | 16 kB      |       7
 public          | paroleoffices_manysources_2008_wgs84                            | 16 kB      |       5
 public          | paroleoffices_manysources_2008_wgs84_attrs_raw                  | 16 kB      |       7
 public          | placesofworship_hsip_20080723_utm83                             | 48 kB      |       5
 public          | placesofworship_hsip_20080723_utm83_attrs_raw                   | 48 kB      |       7
 public          | placesofworship_hsip_20080723_wgs84                             | 48 kB      |       5
 public          | placesofworship_hsip_20080723_wgs84_attrs_raw                   | 48 kB      |       7
 public          | policedept_wvdem_012319_gcs84                                   | 72 kB      |       5
 public          | policedept_wvdem_012319_gcs84_attrs_raw                         | 80 kB      |       7
 public          | policedept_wvdem_012319_utm83                                   | 72 kB      |       5
 public          | policedept_wvdem_012319_utm83_attrs_raw                         | 80 kB      |       7
 public          | populatedplaces_census_201112_utm83                             | 80 kB      |       5
 public          | populatedplaces_census_201112_utm83_attrs_raw                   | 96 kB      |       7
 public          | populatedplaces_census_20112_gcs83                              | 80 kB      |       5
 public          | populatedplaces_census_20112_gcs83_attrs_raw                    | 96 kB      |       7
 public          | populatedplaces_census_2020_utm83                               | 88 kB      |       5
 public          | populatedplaces_census_2020_utm83_attrs_raw                     | 96 kB      |       7
 public          | populatedplaces_census_2020_wma84                               | 80 kB      |       5
 public          | populatedplaces_census_2020_wma84_attrs_raw                     | 96 kB      |       7
 public          | populatedplaces_uscensus_1990_ll83                              | 64 kB      |       5
 public          | populatedplaces_uscensus_1990_ll83_attrs_raw                    | 80 kB      |       7
 public          | populatedplaces_uscensus_1990_utm83                             | 64 kB      |       5
 public          | populatedplaces_uscensus_1990_utm83_attrs_raw                   | 80 kB      |       7
 public          | populationdatablockgroups_uscensus_2000_ll83                    | 224 kB     |       5
 public          | populationdatablockgroups_uscensus_2000_ll83_attrs_raw          | 528 kB     |       7
 public          | populationdatablockgroups_uscensus_2000_utm83                   | 240 kB     |       5
 public          | populationdatablockgroups_uscensus_2000_utm83_attrs_raw         | 536 kB     |       7
 public          | pow_wvgistc_062919_utm83                                        | 600 kB     |       5
 public          | pow_wvgistc_062919_utm83_attrs_raw                              | 792 kB     |       7
 public          | pow_wvgistc_062919_wgs84                                        | 600 kB     |       5
 public          | pow_wvgistc_062919_wgs84_attrs_raw                              | 816 kB     |       7
 public          | program                                                         | 48 kB      |      43
 public          | program_authority_links                                         | 24 kB      |       4
 public          | program_catalog                                                 | 32 kB      |      10
 public          | program_eligibility                                             | 48 kB      |      11
 public          | program_entity_links                                            | 2800 kB    |       5
 public          | program_evidence_links                                          | 24 kB      |       4
 public          | program_income_limit_rules                                      | 24 kB      |       2
 public          | program_income_source_policy                                    | 24 kB      |      13
 public          | program_manual_rule_links                                       | 24 kB      |       2
 public          | program_name_crosswalk                                          | 32 kB      |       2
 public          | program_target_config                                           | 32 kB      |       3
 public          | publichealthdepts_hsip_20091229_gcs83                           | 16 kB      |       5
 public          | publichealthdepts_hsip_20091229_gcs83_attrs_raw                 | 48 kB      |       7
 public          | publichealthdepts_hsip_20091229_utm83                           | 16 kB      |       5
 public          | publichealthdepts_hsip_20091229_utm83_attrs_raw                 | 48 kB      |       7
 public          | railnetworkregion_usdot_200203_ll83                             | 1440 kB    |       5
 public          | railnetworkregion_usdot_200203_ll83_attrs_raw                   | 3784 kB    |       7
 public          | railnetworkregion_usdot_200203_utm83                            | 1440 kB    |       5
 public          | railnetworkregion_usdot_200203_utm83_attrs_raw                  | 3680 kB    |       7
 public          | railnetworkwv_usdot_200203_ll83                                 | 304 kB     |       5
 public          | railnetworkwv_usdot_200203_ll83_attrs_raw                       | 760 kB     |       7
 public          | railnetworkwv_usdot_200203_utm83                                | 304 kB     |       5
 public          | railnetworkwv_usdot_200203_utm83_attrs_raw                      | 760 kB     |       7
 public          | railroads_rahalltransportationinstitute_2005_utm83              | 392 kB     |       5
 public          | railroads_rahalltransportationinstitute_2005_utm83_attrs_raw    | 896 kB     |       7
 public          | realtimestreamflowstations_usgs_200012_ll27                     | 48 kB      |       5
 public          | realtimestreamflowstations_usgs_200012_ll27_attrs_raw           | 48 kB      |       7
 public          | realtimestreamflowstations_usgs_200012_utm27                    | 48 kB      |       5
 public          | realtimestreamflowstations_usgs_200012_utm27_attrs_raw          | 48 kB      |       7
 public          | realtimestreamflowstations_usgs_200012_utm83                    | 48 kB      |       5
 public          | realtimestreamflowstations_usgs_200012_utm83_attrs_raw          | 48 kB      |       7
 public          | recreationalwwtrails_ofwv_20151117_utm83                        | 64 kB      |       5
 public          | recreationalwwtrails_ofwv_20151117_utm83_attrs_raw              | 120 kB     |       7
 public          | regionalplanninganddevelopmentcouncil_wvdo_1971_ll83            | 16 kB      |       5
 public          | regionalplanninganddevelopmentcouncil_wvdo_1971_ll83_attrs_raw  | 48 kB      |       7
 public          | regionalplanninganddevelopmentcouncil_wvdo_1971_utm83           | 16 kB      |       5
 public          | regionalplanninganddevelopmentcouncil_wvdo_1971_utm83_attrs_raw | 56 kB      |       7
 public          | resource_county_coverage                                        | 32 kB      |       2
 public          | resource_eligibility                                            | 32 kB      |      11
 public          | rural_health_attrs_staging                                      | 48 kB      |       7
 public          | sewertreatmentplants_wvdep_200203_utm83                         | 192 kB     |       5
 public          | sewertreatmentplants_wvdep_200203_utm83_attrs_raw               | 232 kB     |       7
 public          | solidwastefacilities_wvdep_200202_ll83                          | 48 kB      |       5
 public          | solidwastefacilities_wvdep_200202_ll83_attrs_raw                | 48 kB      |       7
 public          | solidwastefacilities_wvdep_200202_utm83                         | 48 kB      |       5
 public          | solidwastefacilities_wvdep_200202_utm83_attrs_raw               | 48 kB      |       7
 public          | spatial_ref_sys                                                 | 7144 kB    |       5
 public          | springs_wvges_1986_ll83                                         | 64 kB      |       5
 public          | springs_wvges_1986_ll83_attrs_raw                               | 72 kB      |       7
 public          | springs_wvges_1986_utm83                                        | 64 kB      |       5
 public          | springs_wvges_1986_utm83_attrs_raw                              | 72 kB      |       7
 public          | stateofwvhousedistricts_wvlegislativeservices_2010              | 48 kB      |       5
 public          | stateofwvhousedistricts_wvlegislativeservices_2010_attrs_raw    | 48 kB      |       7
 public          | stateofwvsenatedistricts_wvlegislativeservices_2010             | 16 kB      |       5
 public          | stateofwvsenatedistricts_wvlegislativeservices_2010_attrs_raw   | 16 kB      |       7
 public          | states_region_ll83                                              | 16 kB      |       5
 public          | states_region_ll83_attrs_raw                                    | 56 kB      |       7
 public          | structurepointsnorth_samb_2003_utm83                            | 69 MB      |       5
 public          | structurepointsnorth_samb_2003_utm83_attrs_raw                  | 90 MB      |       7
 public          | structurepointssouth_samb_2003_utm83                            | 83 MB      |       5
 public          | structurepointssouth_samb_2003_utm83_attrs_raw                  | 109 MB     |       7
 public          | structurepolygons_samb_2003_utm83                               | 1808 kB    |       5
 public          | structurepolygons_samb_2003_utm83_attrs_raw                     | 4640 kB    |       7
 public          | summits_gistc_052012_utm83_shp                                  | 136 kB     |       5
 public          | summits_gistc_052012_utm83_shp_attrs_raw                        | 168 kB     |       7
 public          | summits_gistc_052012_wgs84_shp                                  | 136 kB     |       5
 public          | summits_gistc_052012_wgs84_shp_attrs_raw                        | 168 kB     |       7
 public          | surveycontrol_nationalgeodeticsurvey_102011_gcs83               | 1104 kB    |       5
 public          | surveycontrol_nationalgeodeticsurvey_102011_gcs83_attrs_raw     | 1312 kB    |       7
 public          | tiger_county_2022                                               | 131 MB     |      19
 public          | timberremovalvolume_usfs_1996_utm83                             | 16 kB      |       5
 public          | timberremovalvolume_usfs_1996_utm83_attrs_raw                   | 56 kB      |       7
 public          | tl_2020_54_bg                                                   | 25 MB      |      14
 public          | tl_2020_54_tabblock20                                           | 175 MB     |      19
 public          | tmp_building_block_nearest_sample                               | 288 kB     |       3
 public          | towers_wvpublicbroadcasting_2002_ll83                           | 16 kB      |       5
 public          | towers_wvpublicbroadcasting_2002_ll83_attrs_raw                 | 16 kB      |       7
 public          | towers_wvpublicbroadcasting_2002_utm83                          | 16 kB      |       5
 public          | towers_wvpublicbroadcasting_2002_utm83_attrs_raw                | 16 kB      |       7
 public          | towersam_fcc_200202_utm83                                       | 16 kB      |       5
 public          | towersam_fcc_200202_utm83_attrs_raw                             | 48 kB      |       7
 public          | towersasr_fcc_200202_ll83                                       | 112 kB     |       5
 public          | towersasr_fcc_200202_ll83_attrs_raw                             | 128 kB     |       7
 public          | towersasr_fcc_200202_utm83                                      | 120 kB     |       5
 public          | towersasr_fcc_200202_utm83_attrs_raw                            | 144 kB     |       7
 public          | towerscellular_fcc_200202_ll83                                  | 64 kB      |       5
 public          | towerscellular_fcc_200202_ll83_attrs_raw                        | 64 kB      |       7
 public          | towerscellular_fcc_200202_utm83                                 | 64 kB      |       5
 public          | towerscellular_fcc_200202_utm83_attrs_raw                       | 72 kB      |       7
 public          | towersfm_fcc_200202_utm83                                       | 16 kB      |       5
 public          | towersfm_fcc_200202_utm83_attrs_raw                             | 48 kB      |       7
 public          | towersmicrowave_fcc_200202_ll83                                 | 264 kB     |       5
 public          | towersmicrowave_fcc_200202_ll83_attrs_raw                       | 304 kB     |       7
 public          | towersmicrowave_fcc_200202_utm83                                | 264 kB     |       5
 public          | towersmicrowave_fcc_200202_utm83_attrs_raw                      | 344 kB     |       7
 public          | towerspager_fcc_200202_ll83                                     | 64 kB      |       5
 public          | towerspager_fcc_200202_ll83_attrs_raw                           | 72 kB      |       7
 public          | towerspager_fcc_200202_utm83                                    | 64 kB      |       5
 public          | towerspager_fcc_200202_utm83_attrs_raw                          | 72 kB      |       7
 public          | towersprivate_fcc_200202_ll83                                   | 648 kB     |       5
 public          | towersprivate_fcc_200202_ll83_attrs_raw                         | 744 kB     |       7
 public          | towersprivate_fcc_200202_utm83                                  | 648 kB     |       5
 public          | towersprivate_fcc_200202_utm83_attrs_raw                        | 840 kB     |       7
 public          | uei_registry                                                    | 48 kB      |      13
 public          | us_counties                                                     | 2608 kB    |       6
 public          | us_counties_tmp                                                 | 130 MB     |      19
 public          | us_zips                                                         | 864 MB     |       4
 public          | us_zips_tmp                                                     | 865 MB     |      11
 public          | user_compliance_task                                            | 32 kB      |      13
 public          | utility_discount_enrollment                                     | 48 kB      |      15
 public          | veteransaffairsfacilities_manysources_200503_utm83              | 16 kB      |       5
 public          | veteransaffairsfacilities_manysources_200503_utm83_attrs_raw    | 16 kB      |       7
 public          | veteransaffairsfacilities_manysources_200503_wgs84              | 16 kB      |       5
 public          | veteransaffairsfacilities_manysources_200503_wgs84_attrs_raw    | 16 kB      |       7
 public          | votingdistrictswv_legislativeservices_2002_ll83                 | 264 kB     |       5
 public          | votingdistrictswv_legislativeservices_2002_ll83_attrs_raw       | 512 kB     |       7
 public          | votingdistrictswv_legislativeservices_2002_utm83                | 272 kB     |       5
 public          | votingdistrictswv_legislativeservices_2002_utm83_attrs_raw      | 632 kB     |       7
 public          | votingdistrictswv_uscensus_2000_utm83                           | 248 kB     |       5
 public          | votingdistrictswv_uscensus_2000_utm83_attrs_raw                 | 464 kB     |       7
 public          | weatherstations_nationalclimatedatacenter_1999_gcs83            | 56 kB      |       5
 public          | weatherstations_nationalclimatedatacenter_1999_gcs83_attrs_raw  | 56 kB      |       7
 public          | weatherstations_nationalclimatedatacenter_1999_utm27            | 56 kB      |       5
 public          | weatherstations_nationalclimatedatacenter_1999_utm27_attrs_raw  | 64 kB      |       7
 public          | windenergyresource_nationalrenewableenergylab_200901_utm83      | 14 MB      |       5
 public          | windenergyresource_nationalrenewableenergylab_200901_utm83_attr | 33 MB      |       7
 public          | windenergyresource_nationalrenewableenergylab_200901_wgs84      | 14 MB      |       5
 public          | windenergyresource_nationalrenewableenergylab_200901_wgs84_attr | 34 MB      |       7
 public          | workforceinvestmentareas_wvgistc_200208_ll83                    | 16 kB      |       5
 public          | workforceinvestmentareas_wvgistc_200208_ll83_attrs_raw          | 56 kB      |       7
 public          | wv_county_bbox_geom                                             | 64 kB      |       3
 public          | wv_county_boundaries_24k_topo_updated_2022_utm83_attrs_raw      | 56 kB      |       7
 public          | wv_county_names                                                 | 32 kB      |       3
 public          | wv_hospitals                                                    | 96 kB      |       9
 public          | wv_income_manual_income_limits                                  | 32 kB      |      16
 public          | wv_income_manual_income_sources                                 | 32 kB      |       4
 public          | wv_income_manual_income_treatment                               | 32 kB      |       6
 public          | wv_income_manual_income_treatment_extended                      | 32 kB      |      10
 public          | wv_income_manual_rules                                          | 32 kB      |       9
 public          | wv_microsoft_20180207_utm17n83                                  | 106 MB     |       5
 public          | wv_microsoft_20180207_utm17n83_attrs_raw                        | 295 MB     |       7
 public          | wv_state_poly                                                   | 600 kB     |       1
 public          | wv_tax_districts_ll83                                           | 96 kB      |       5
 public          | wv_tax_districts_ll83_attrs_raw                                 | 208 kB     |       7
 public          | wv_tax_districts_utm83_attrs_raw                                | 200 kB     |       7
 public          | wv_tax_districts_wma84                                          | 96 kB      |       5
 public          | wv_tax_districts_wma84_attrs_raw                                | 208 kB     |       7
 public          | wvgistc_building_footprints                                     | 205 MB     |       5
 public          | wvgistc_building_footprints_attrs_raw                           | 557 MB     |       7
 public          | wvgistcbuildingfootprints                                       | 305 MB     |       5
 public          | wvgistcbuildingfootprints_attrs_raw                             | 575 MB     |       7
 public          | wvgistcbuildingfootprintsattrsraw                               | 575 MB     |       7
 public          | wvstatebounadary100k_usgs_200203_utm83                          | 16 kB      |       5
 public          | wvstatebounadary100k_usgs_200203_utm83_attrs_raw                | 16 kB      |       7
 public          | wvstateboundary100k_usgs_200203_ll83                            | 16 kB      |       5
 public          | wvstateboundary100k_usgs_200203_ll83_attrs_raw                  | 16 kB      |       7
 public          | wvstateboundary24k_usgs_200203_ll83                             | 16 kB      |       5
 public          | wvstateboundary24k_usgs_200203_ll83_attrs_raw                   | 16 kB      |       7
 public          | wvstateboundary24k_usgs_200203_utm83                            | 16 kB      |       5
 public          | wvstateboundary24k_usgs_200203_utm83_attrs_raw                  | 16 kB      |       7
 public          | wvstatehousedistricts_manysources_1992_ll83                     | 16 kB      |       5
 public          | wvstatehousedistricts_manysources_1992_ll83_attrs_raw           | 48 kB      |       7
 public          | wvstatehousedistricts_manysources_1992_utm83                    | 16 kB      |       5
 public          | wvstatehousedistricts_manysources_1992_utm83_attrs_raw          | 56 kB      |       7
 public          | wvstatehousedistricts_manysources_2002_ll83                     | 16 kB      |       5
 public          | wvstatehousedistricts_manysources_2002_ll83_attrs_raw           | 48 kB      |       7
 public          | wvstatehousedistricts_manysources_2002_utm83                    | 16 kB      |       5
 public          | wvstatehousedistricts_manysources_2002_utm83_attrs_raw          | 56 kB      |       7
 public          | wvstatehousedistricts_wvlegislativeservices_2020_utm83_attrs_ra | 64 kB      |       7
 public          | wvstatesenatedistricts_manysources_1992_ll83                    | 16 kB      |       5
 public          | wvstatesenatedistricts_manysources_1992_ll83_attrs_raw          | 16 kB      |       7
 public          | wvstatesenatedistricts_manysources_1992_utm83                   | 16 kB      |       5
 public          | wvstatesenatedistricts_manysources_1992_utm83_attrs_raw         | 16 kB      |       7
 public          | wvstatesenatedistricts_manysources_2002_ll83                    | 16 kB      |       5
 public          | wvstatesenatedistricts_manysources_2002_ll83_attrs_raw          | 16 kB      |       7
 public          | wvstatesenatedistricts_manysources_2002_utm83                   | 16 kB      |       5
 public          | wvstatesenatedistricts_manysources_2002_utm83_attrs_raw         | 16 kB      |       7
 public          | wvstatesenatedistricts_wvlegislativeservices_2020_utm83_attrs_r | 16 kB      |       7
 public          | zcta_county_rel                                                 | 9128 kB    |      18
 public          | zipcodetabulationarea_census_2020_raw                           | 865 MB     |      11
 public          | zipcodetabulationarea_census_2020_utm83_attrs_raw               | 264 kB     |       7
 public          | zipcodetabulationarea_census_2020_wma84                         | 829 MB     |      11
 public          | zipcodetabulationarea_census_2020_wma84_attrs_raw               | 264 kB     |       7
 raw             | boundaryappalachianbasin_wvges_1996_utm83_attrs                 | 80 kB      |       4
 raw             | boundaryappalachianbasin_wvges_1996_utm83_stage                 | 128 kB     |       7
 raw             | wv_tax_parcels_2025                                             | 1013 MB    |      21
 tiger           | addr                                                            | 24 kB      |      14
 tiger           | addrfeat                                                        | 48 kB      |      25
 tiger           | bg                                                              | 16 kB      |      14
 tiger           | county                                                          | 32 kB      |      19
 tiger           | county_lookup                                                   | 24 kB      |       4
 tiger           | countysub_lookup                                                | 24 kB      |       6
 tiger           | cousub                                                          | 32 kB      |      20
 tiger           | direction_lookup                                                | 40 kB      |       2
 tiger           | edges                                                           | 40 kB      |      33
 tiger           | faces                                                           | 40 kB      |      75
 tiger           | featnames                                                       | 32 kB      |      20
 tiger           | geocode_settings                                                | 16 kB      |       5
 tiger           | geocode_settings_default                                        | 32 kB      |       5
 tiger           | loader_lookuptables                                             | 64 kB      |      14
 tiger           | loader_platform                                                 | 32 kB      |      10
 tiger           | loader_variables                                                | 32 kB      |       5
 tiger           | pagc_gaz                                                        | 128 kB     |       6
 tiger           | pagc_lex                                                        | 336 kB     |       6
 tiger           | pagc_rules                                                      | 856 kB     |       3
 tiger           | place                                                           | 32 kB      |      19
 tiger           | place_lookup                                                    | 24 kB      |       4
 tiger           | secondary_unit_lookup                                           | 40 kB      |       2
 tiger           | state                                                           | 40 kB      |      15
 tiger           | state_lookup                                                    | 104 kB     |       4
 tiger           | street_type_lookup                                              | 128 kB     |       3
 tiger           | tabblock                                                        | 16 kB      |      16
 tiger           | tabblock20                                                      | 16 kB      |      18
 tiger           | tract                                                           | 16 kB      |      14
 tiger           | zcta5                                                           | 16 kB      |      12
 tiger           | zip_lookup                                                      | 8192 bytes |      10
 tiger           | zip_lookup_all                                                  | 0 bytes    |      10
 tiger           | zip_lookup_base                                                 | 8192 bytes |       5
 tiger           | zip_state                                                       | 8192 bytes |       3
 tiger           | zip_state_loc                                                   | 8192 bytes |       4
 topology        | layer                                                           | 24 kB      |       8
 topology        | topology                                                        | 24 kB      |       6
 trails          | historic_context                                                | 32 kB      |       9
 trails          | trail                                                           | 56 kB      |      10
 trails          | waypoint                                                        | 72 kB      |      12
(693 rows)


=== jarvis-local-resources-db/msjarvisgis tables ===
   schemaname    |                            tablename                            |    size    | columns 
-----------------+-----------------------------------------------------------------+------------+---------
 cakidd          | bldg_join__flood_structures_at_risk                             | 8192 bytes |       9
 cakidd          | bldg_join__nearest_hospital                                     | 315 MB     |      10
 cakidd          | gbim_authorities                                                | 16 kB      |       5
 cakidd          | gbim_belief_relations                                           | 16 kB      |       7
 cakidd          | gbim_beliefs                                                    | 16 kB      |      12
 cakidd          | gbim_evidence                                                   | 16 kB      |      13
 cakidd          | gbim_graph_edges                                                | 3018 MB    |       9
 cakidd          | gbim_worldview_entity                                           | 48 kB      |       7
 cakidd          | gbim_worldviews                                                 | 48 kB      |       7
 cakidd          | redetermination_tracker                                         | 64 kB      |      14
 cakidd          | user_benefit_profile                                            | 8192 bytes |      10
 gbim            | building_metrics                                                | 130 MB     |       2
 gbim            | entity_relationship                                             | 360 MB     |       7
 gbim            | gbim_attrs                                                      | 2041 MB    |       8
 gbim            | priority_layers                                                 | 64 kB      |       3
 gbim            | worldview_entity                                                | 1213 MB    |       9
 gbim_source_csv | amtrackrails_federalrailroadadministration_200210_utm83         | 16 kB      |       8
 gbim_source_csv | blockgroups_census_2000_utm83                                   | 552 kB     |       8
 gbim_source_csv | blockgroups_census_201111_utm83                                 | 576 kB     |       8
 gbim_source_csv | blockgroups_census_2020_utm83                                   | 672 kB     |       8
 gbim_source_csv | blocks_census_2020_utm83                                        | 28 MB      |       8
 gbim_source_csv | boundaryappalachianbasin_wvges_1996_utm83                       | 144 kB     |       8
 gbim_source_csv | citieswithpopulation_2500_census_201111_utm83                   | 56 kB      |       8
 gbim_source_csv | citieswithpopulationover10k_uscensus_1990_utm83                 | 16 kB      |       8
 gbim_source_csv | citieswithpopulationsover10k_census_2020_utm83                  | 16 kB      |       8
 gbim_source_csv | citieswithpopulationsover2500_census_2020_utm83                 | 56 kB      |       8
 gbim_source_csv | citieswithpopulatoinover2500_uscensus_1990_utm83                | 88 kB      |       8
 gbim_source_csv | coals2_utm83                                                    | 16 kB      |       8
 gbim_source_csv | communityboundary_min_att_20250121_utm83                        | 136 kB     |       8
 gbim_source_csv | communityhealthproviders_wvhealthcareauthority_200802_utm83     | 64 kB      |       8
 gbim_source_csv | correctionalinstitutions_hsip_20091230_utm83                    | 56 kB      |       8
 gbim_source_csv | countycityparkboundaries_20201104_utm83                         | 240 kB     |       8
 gbim_source_csv | countyseats_usgs_utm83                                          | 48 kB      |       8
 gbim_source_csv | courthousescounty_manysources_200203_utm83                      | 48 kB      |       8
 gbim_source_csv | cvfault_utm83                                                   | 16 kB      |       8
 gbim_source_csv | cvpoly_utm83                                                    | 48 kB      |       8
 gbim_source_csv | dams_usarmycorpsofengineers_200010_utm83                        | 144 kB     |       8
 gbim_source_csv | damsnoncoal_usgs_2002_utm83                                     | 112 kB     |       8
 gbim_source_csv | empowermentzonesandenterprisecommunities_uscensus_2002_utm83    | 16 kB      |       8
 gbim_source_csv | excursionpassengertrains_wvdof_200102_utm83                     | 16 kB      |       8
 gbim_source_csv | facilities_epa_200203_utm83                                     | 408 kB     |       8
 gbim_source_csv | fire_dept_wvdem_092017_utm83                                    | 128 kB     |       8
 gbim_source_csv | floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83  | 16 MB      |       8
 gbim_source_csv | geographicalnamesonusgstopomaps_usgs_200601_utm83               | 8760 kB    |       8
 gbim_source_csv | geographicnamesonusgstopomaps_current_usgs_20110801_utm83       | 6272 kB    |       8
 gbim_source_csv | geographicnamesonusgstopomaps_historical_usgs_20110801_utm83    | 2592 kB    |       8
 gbim_source_csv | geographicnamesonusgstopomaps_usgs_20110801_utm83               | 7424 kB    |       8
 gbim_source_csv | hazardmitigationbuyout_20250929_polygons_utm83                  | 1032 kB    |       8
 gbim_source_csv | healthruralfacilities_manysources_utm83                         | 48 kB      |       8
 gbim_source_csv | highered_wvemd_072420_utm83                                     | 48 kB      |       8
 gbim_source_csv | historicalaerialphotographycountycoverage_wvgistc_utm83         | 56 kB      |       8
 gbim_source_csv | hospitals_wvdem_040519_utm83                                    | 48 kB      |       8
 gbim_source_csv | indexgrid15minutequads_wvgistc_utm83                            | 256 kB     |       8
 gbim_source_csv | industrialbuildings_wvdo_200807_utm83                           | 56 kB      |       8
 gbim_source_csv | industrialparks_wvdo_200078_utm83                               | 72 kB      |       8
 gbim_source_csv | industrialsites_wvdo_200807_utm83                               | 96 kB      |       8
 gbim_source_csv | inedexgrid1minutequads_wvgistc_utm83                            | 48 kB      |       8
 gbim_source_csv | intermodalterminalfacilities_usdot_1997_utm83                   | 64 kB      |       8
 gbim_source_csv | libraries_manysources_2001_utm83                                | 80 kB      |       8
 gbim_source_csv | majorriversandlakesline_nhd_2002_utm83                          | 56 kB      |       8
 gbim_source_csv | majorriversandlakespolygon_nhd_2002_utm83                       | 64 kB      |       8
 gbim_source_csv | manufacturingandbusiness_wvdo_200803_utm83                      | 1720 kB    |       8
 gbim_source_csv | metropolitanandmicropolitanstatisticalareas_census_201111_utm83 | 16 kB      |       8
 gbim_source_csv | metropolitanandmicropolitanstatisticalareas_census_2020_utm83   | 16 kB      |       8
 gbim_source_csv | metropolitanstatisticalareas_uscensus_199901_utm83              | 16 kB      |       8
 gbim_source_csv | mineraloperations_usgs_200204_utm83                             | 48 kB      |       8
 gbim_source_csv | nationalatlasstreams_usgs_199903_utm83                          | 488 kB     |       8
 gbim_source_csv | nationalwaterwaynetwork_usarmycorpsofengineers_2001_utm83       | 72 kB      |       8
 gbim_source_csv | nationalwaterwaynetworkports_usarmycorpsofengineers_2001_utm83  | 16 kB      |       8
 gbim_source_csv | naviagablewaterways_usarmycropsofengineers_2006_utm83           | 16 kB      |       8
 gbim_source_csv | navigablewaterwaysrivermiles_usarmycropsofengineers_2006_utm83  | 128 kB     |       8
 gbim_source_csv | navigablewaterwaysstructures_usarmycorpsofengineers_2006_utm83  | 6808 kB    |       8
 gbim_source_csv | nursinghomes_wvdem_041219_utm83                                 | 56 kB      |       8
 gbim_source_csv | officebuildings_wvdo_200807_utm83                               | 48 kB      |       8
 gbim_source_csv | paroleoffices_manysources_2008_utm83                            | 16 kB      |       8
 gbim_source_csv | placesofworship_hsip_20080723_utm83                             | 48 kB      |       8
 gbim_source_csv | policedept_wvdem_012319_utm83                                   | 88 kB      |       8
 gbim_source_csv | populatedplaces_census_201112_utm83                             | 104 kB     |       8
 gbim_source_csv | populatedplaces_census_2020_utm83                               | 112 kB     |       8
 gbim_source_csv | populatedplaces_uscensus_1990_utm83                             | 88 kB      |       8
 gbim_source_csv | populationdatablockgroups_uscensus_2000_utm83                   | 600 kB     |       8
 gbim_source_csv | pow_wvgistc_062919_utm83                                        | 976 kB     |       8
 gbim_source_csv | publichealthdepts_hsip_20091229_utm83                           | 48 kB      |       8
 gbim_source_csv | railnetworkregion_usdot_200203_utm83                            | 4128 kB    |       8
 gbim_source_csv | railnetworkwv_usdot_200203_utm83                                | 856 kB     |       8
 gbim_source_csv | railroads_rahalltransportationinstitute_2005_utm83              | 976 kB     |       8
 gbim_source_csv | realtimestreamflowstations_usgs_200012_utm83                    | 48 kB      |       8
 gbim_source_csv | recreationalwwtrails_ofwv_20151117_utm83                        | 128 kB     |       8
 gbim_source_csv | regionalplanninganddevelopmentcouncil_wvdo_1971_utm83           | 56 kB      |       8
 gbim_source_csv | sewertreatmentplants_wvdep_200203_utm83                         | 280 kB     |       8
 gbim_source_csv | solidwastefacilities_wvdep_200202_utm83                         | 48 kB      |       8
 gbim_source_csv | springs_wvges_1986_utm83                                        | 80 kB      |       8
 gbim_source_csv | structurepointsnorth_samb_2003_utm83                            | 113 MB     |       8
 gbim_source_csv | structurepointssouth_samb_2003_utm83                            | 135 MB     |       8
 gbim_source_csv | structurepolygons_samb_2003_utm83                               | 5216 kB    |       8
 gbim_source_csv | timberremovalvolume_usfs_1996_utm83                             | 56 kB      |       8
 gbim_source_csv | towers_wvpublicbroadcasting_2002_utm83                          | 16 kB      |       8
 gbim_source_csv | towersam_fcc_200202_utm83                                       | 48 kB      |       8
 gbim_source_csv | towersasr_fcc_200202_utm83                                      | 176 kB     |       8
 gbim_source_csv | towerscellular_fcc_200202_utm83                                 | 80 kB      |       8
 gbim_source_csv | towersfm_fcc_200202_utm83                                       | 48 kB      |       8
 gbim_source_csv | towersmicrowave_fcc_200202_utm83                                | 416 kB     |       8
 gbim_source_csv | towerspager_fcc_200202_utm83                                    | 80 kB      |       8
 gbim_source_csv | towersprivate_fcc_200202_utm83                                  | 1056 kB    |       8
 gbim_source_csv | veteransaffairsfacilities_manysources_200503_utm83              | 16 kB      |       8
 gbim_source_csv | votingdistrictswv_legislativeservices_2002_utm83                | 704 kB     |       8
 gbim_source_csv | votingdistrictswv_uscensus_2000_utm83                           | 520 kB     |       8
 gbim_source_csv | windenergyresource_nationalrenewableenergylab_200901_utm83      | 37 MB      |       8
 gbim_source_csv | wv_county_boundaries_24k_topo_updated_2022_utm83                | 56 kB      |       8
 gbim_source_csv | wv_tax_districts_utm83                                          | 224 kB     |       8
 gbim_source_csv | wvstatebounadary100k_usgs_200203_utm83                          | 16 kB      |       8
 gbim_source_csv | wvstateboundary24k_usgs_200203_utm83                            | 16 kB      |       8
 gbim_source_csv | wvstatehousedistricts_manysources_1992_utm83                    | 56 kB      |       8
 gbim_source_csv | wvstatehousedistricts_manysources_2002_utm83                    | 56 kB      |       8
 gbim_source_csv | wvstatehousedistricts_wvlegislativeservices_2020_utm83          | 72 kB      |       8
 gbim_source_csv | wvstatesenatedistricts_manysources_1992_utm83                   | 16 kB      |       8
 gbim_source_csv | wvstatesenatedistricts_manysources_2002_utm83                   | 16 kB      |       8
 gbim_source_csv | wvstatesenatedistricts_wvlegislativeservices_2020_utm83         | 16 kB      |       8
 gbim_source_csv | zipcodetabulationarea_census_2020_utm83                         | 296 kB     |       8
 public          | 911centers_wvdem_032819_gcs84                                   | 48 kB      |       5
 public          | 911centers_wvdem_032819_gcs84_attrs_raw                         | 48 kB      |       7
 public          | 911centers_wvdem_032819_utm83                                   | 48 kB      |       5
 public          | 911centers_wvdem_032819_utm83_attrs_raw                         | 48 kB      |       7
 public          | amtrackrails_federalrailroadadministration_200210_ll83          | 16 kB      |       5
 public          | amtrackrails_federalrailroadadministration_200210_ll83_attrs_ra | 16 kB      |       7
 public          | amtrackrails_federalrailroadadministration_200210_utm83         | 16 kB      |       5
 public          | amtrackrails_federalrailroadadministration_200210_utm83_attrs_r | 16 kB      |       7
 public          | amtrackrails_fra_200210_ll83_attrs_raw                          | 16 kB      |       7
 public          | amtrackrails_fra_200210_utm83_attrs_raw                         | 16 kB      |       7
 public          | attrs_files_list                                                | 112 kB     |       4
 public          | attrs_inventory_detailed                                        | 112 kB     |      10
 public          | authority_references                                            | 32 kB      |       7
 public          | benefit_case                                                    | 32 kB      |       6
 public          | benefit_county_daycare                                          | 72 kB      |       8
 public          | benefit_county_medicaid                                         | 72 kB      |       8
 public          | benefit_county_medicare                                         | 72 kB      |       8
 public          | benefit_county_section8                                         | 72 kB      |       8
 public          | benefit_county_snap                                             | 72 kB      |       8
 public          | benefit_county_ssi                                              | 72 kB      |       8
 public          | benefit_county_tanf                                             | 72 kB      |       8
 public          | benefit_county_utility20                                        | 72 kB      |       8
 public          | benefit_county_wic                                              | 72 kB      |       8
 public          | bldg_join__floodplainstructuresatrisk_usarmycorpsofengineers_20 | 8192 bytes |       9
 public          | bldg_join__hospitals                                            | 315 MB     |      10
 public          | blockgroups_census_2000_ll83                                    | 360 kB     |       5
 public          | blockgroups_census_2000_ll83_attrs_raw                          | 944 kB     |       7
 public          | blockgroups_census_2000_utm83                                   | 360 kB     |       5
 public          | blockgroups_census_2000_utm83_attrs_raw                         | 952 kB     |       7
 public          | blockgroups_census_201111_gcs83                                 | 384 kB     |       5
 public          | blockgroups_census_201111_gcs83_attrs_raw                       | 816 kB     |       7
 public          | blockgroups_census_201111_utm83                                 | 384 kB     |       5
 public          | blockgroups_census_201111_utm83_attrs_raw                       | 984 kB     |       7
 public          | blockgroups_census_2020_utm83                                   | 568 kB     |       5
 public          | blockgroups_census_2020_utm83_attrs_raw                         | 1184 kB    |       7
 public          | blockgroups_census_2020_utm83_full                              | 49 MB      |      10
 public          | blockgroups_census_2020_wma84                                   | 392 kB     |       5
 public          | blockgroups_census_2020_wma84_attrs_raw                         | 1016 kB    |       7
 public          | blocks_census_2020_utm83                                        | 24 MB      |       5
 public          | blocks_census_2020_utm83_attrs_raw                              | 51 MB      |       7
 public          | blocks_census_2020_utm83_full                                   | 343 MB     |      10
 public          | blocks_census_2020_wma84                                        | 15 MB      |       5
 public          | blocks_census_2020_wma84_attrs_raw                              | 42 MB      |       7
 public          | boundaryappalachianbasin_wvges_1996_utm83                       | 112 kB     |       5
 public          | boundaryappalachianbasin_wvges_1996_utm83_attrs_raw             | 224 kB     |       7
 public          | boundaryappalachianbasin_wvges_1996_wma84                       | 112 kB     |       5
 public          | bridges                                                         | 1256 kB    |       5
 public          | bridges_attrs_raw                                               | 1816 kB    |       7
 public          | building_flood_risk                                             | 42 MB      |       7
 public          | building_metric_stage                                           | 32 kB      |       5
 public          | buildings                                                       | 448 MB     |       2
 public          | calderl_reg_ll83                                                | 16 kB      |       5
 public          | calderl_reg_ll83_attrs_raw                                      | 16 kB      |       7
 public          | canonical_layers                                                | 128 kB     |       9
 public          | citieswithpopulation_2500_census_201111_gcs83                   | 48 kB      |       5
 public          | citieswithpopulation_2500_census_201111_gcs83_attrs_raw         | 72 kB      |       7
 public          | citieswithpopulation_2500_census_201111_utm83                   | 48 kB      |       5
 public          | citieswithpopulation_2500_census_201111_utm83_attrs_raw         | 72 kB      |       7
 public          | citieswithpopulationover10k_census_201111_gcs83                 | 16 kB      |       5
 public          | citieswithpopulationover10k_census_201111_gcs83_attrs_raw       | 16 kB      |       7
 public          | citieswithpopulationover10k_uscensus_1990_ll83                  | 16 kB      |       5
 public          | citieswithpopulationover10k_uscensus_1990_ll83_attrs_raw        | 16 kB      |       7
 public          | citieswithpopulationover10k_uscensus_1990_utm83                 | 16 kB      |       5
 public          | citieswithpopulationover10k_uscensus_1990_utm83_attrs_raw       | 16 kB      |       7
 public          | citieswithpopulationover2500_uscensus_1990_ll83                 | 104 kB     |       5
 public          | citieswithpopulationover2500_uscensus_1990_ll83_attrs_raw       | 120 kB     |       7
 public          | citieswithpopulationsover10k_census_2020_utm83                  | 16 kB      |       5
 public          | citieswithpopulationsover10k_census_2020_utm83_attrs_raw        | 48 kB      |       7
 public          | citieswithpopulationsover10k_census_2020_wma84                  | 16 kB      |       5
 public          | citieswithpopulationsover10k_census_2020_wma84_attrs_raw        | 48 kB      |       7
 public          | citieswithpopulationsover2500_census_2020_utm83                 | 48 kB      |       5
 public          | citieswithpopulationsover2500_census_2020_utm83_attrs_raw       | 72 kB      |       7
 public          | citieswithpopulationsover2500_census_2020_wma84                 | 48 kB      |       5
 public          | citieswithpopulationsover2500_census_2020_wma84_attrs_raw       | 72 kB      |       7
 public          | citieswithpopulatoinover2500_uscensus_1990_utm83                | 104 kB     |       5
 public          | citieswithpopulatoinover2500_uscensus_1990_utm83_attrs_raw      | 128 kB     |       7
 public          | client_utility_account                                          | 32 kB      |       4
 public          | coals2_ll83                                                     | 16 kB      |       5
 public          | coals2_ll83_attrs_raw                                           | 48 kB      |       7
 public          | coals2_utm27                                                    | 16 kB      |       5
 public          | coals2_utm27_attrs_raw                                          | 16 kB      |       7
 public          | coals2_utm83                                                    | 16 kB      |       5
 public          | coals2_utm83_attrs_raw                                          | 48 kB      |       7
 public          | community_points                                                | 16 kB      |      11
 public          | communityboundary_min_att_20250121_utm83                        | 104 kB     |       5
 public          | communityboundary_min_att_20250121_utm83_attrs_raw              | 200 kB     |       7
 public          | communityboundary_min_att_20250121_wma84                        | 104 kB     |       5
 public          | communityboundary_min_att_20250121_wma84_attrs_raw              | 216 kB     |       7
 public          | communityhealthproviders_wvhealthcareauthority_200802_utm83     | 80 kB      |       5
 public          | communityhealthproviders_wvhealthcareauthority_200802_utm83_att | 88 kB      |       7
 public          | confidence_decay                                                | 24 kB      |       6
 public          | correctionalinstitutions_hsip_20091230_utm83                    | 64 kB      |       5
 public          | correctionalinstitutions_hsip_20091230_utm83_attrs_raw          | 72 kB      |       7
 public          | correctionalinstitutions_hsip_20091230_wgs84                    | 64 kB      |       5
 public          | correctionalinstitutions_hsip_20091230_wgs84_attrs_raw          | 72 kB      |       7
 public          | countycityparkboundaries_20201104_utm83                         | 184 kB     |       5
 public          | countycityparkboundaries_20201104_utm83_attrs_raw               | 400 kB     |       7
 public          | countyseats_usgs_ll83                                           | 48 kB      |       5
 public          | countyseats_usgs_ll83_attrs_raw                                 | 48 kB      |       7
 public          | countyseats_usgs_utm83                                          | 48 kB      |       5
 public          | countyseats_usgs_utm83_attrs_raw                                | 48 kB      |       7
 public          | courthousescounty_manysources_200203_ll83                       | 48 kB      |       5
 public          | courthousescounty_manysources_200203_ll83_attrs_raw             | 56 kB      |       7
 public          | courthousescounty_manysources_200203_utm83                      | 8192 bytes |       5
 public          | courthousescounty_manysources_200203_utm83_attrs_raw            | 8192 bytes |       7
 public          | courthousesfederal_manysources_200203_ll83                      | 8192 bytes |       5
 public          | courthousesfederal_manysources_200203_ll83_attrs_raw            | 8192 bytes |       7
 public          | courthousesfederal_manysources_200203_utm                       | 8192 bytes |       5
 public          | courthousesfederal_manysources_200203_utm_attrs_raw             | 8192 bytes |       7
 public          | cvfault_ll83                                                    | 16 kB      |       5
 public          | cvfault_ll83_attrs_raw                                          | 16 kB      |       7
 public          | cvfault_utm27                                                   | 16 kB      |       5
 public          | cvfault_utm27_attrs_raw                                         | 16 kB      |       7
 public          | cvfault_utm83                                                   | 16 kB      |       5
 public          | cvfault_utm83_attrs_raw                                         | 16 kB      |       7
 public          | cvpoly_ll83                                                     | 16 kB      |       5
 public          | cvpoly_ll83_attrs_raw                                           | 56 kB      |       7
 public          | cvpoly_utm27                                                    | 16 kB      |       5
 public          | cvpoly_utm27_attrs_raw                                          | 56 kB      |       7
 public          | cvpoly_utm83                                                    | 16 kB      |       5
 public          | cvpoly_utm83_attrs_raw                                          | 56 kB      |       7
 public          | dams_usarmycorpsofengineers_200010_utm83                        | 176 kB     |       5
 public          | dams_usarmycorpsofengineers_200010_utm83_attrs_raw              | 216 kB     |       7
 public          | dams_usarmycropsofengineers_200010_ll83                         | 176 kB     |       5
 public          | dams_usarmycropsofengineers_200010_ll83_attrs_raw               | 216 kB     |       7
 public          | damsnoncoal_usgs_2002_ll27                                      | 136 kB     |       5
 public          | damsnoncoal_usgs_2002_ll27_attrs_raw                            | 152 kB     |       7
 public          | damsnoncoal_usgs_2002_utm83                                     | 136 kB     |       5
 public          | damsnoncoal_usgs_2002_utm83_attrs_raw                           | 168 kB     |       7
 public          | empowermentzonesandenterprisecommunities_uscensus_2002_utm83    | 16 kB      |       5
 public          | empowermentzonesandenterprisecommunities_uscensus_2002_utm83_at | 16 kB      |       7
 public          | empowermentzonesandenterprisecommunitiesbytractuscens30c72907   | 160 kB     |       5
 public          | empowermentzonesandenterprisecommunitiesbytractuscens30c72907at | 336 kB     |       7
 public          | evidence_documents                                              | 32 kB      |       8
 public          | excursionpassengertrains_wvdof_200102_ll83                      | 16 kB      |       5
 public          | excursionpassengertrains_wvdof_200102_ll83_attrs_raw            | 16 kB      |       7
 public          | excursionpassengertrains_wvdof_200102_utm83                     | 16 kB      |       5
 public          | excursionpassengertrains_wvdof_200102_utm83_attrs_raw           | 16 kB      |       7
 public          | facilities_epa_200203_ll83                                      | 496 kB     |       5
 public          | facilities_epa_200203_ll83_attrs_raw                            | 632 kB     |       7
 public          | facilities_epa_200203_utm83                                     | 496 kB     |       5
 public          | facilities_epa_200203_utm83_attrs_raw                           | 632 kB     |       7
 public          | fault_reg_ll83                                                  | 56 kB      |       5
 public          | fault_reg_ll83_attrs_raw                                        | 104 kB     |       7
 public          | faultgl_reg_ll83                                                | 8400 kB    |       5
 public          | faultgl_reg_ll83_attrs_raw                                      | 24 MB      |       7
 public          | fayette_fire_stations                                           | 16 kB      |       5
 public          | fayette_parcels                                                 | 6088 kB    |       8
 public          | features                                                        | 21 MB      |       5
 public          | features_attrs_raw                                              | 47 MB      |       7
 public          | fire_departments                                                | 136 kB     |       5
 public          | fire_departments_attrs_raw                                      | 176 kB     |       7
 public          | fire_dept_wvdem_092017_utm83                                    | 160 kB     |       5
 public          | fire_dept_wvdem_092017_utm83_attrs_raw                          | 184 kB     |       7
 public          | floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83  | 22 MB      |       5
 public          | floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83_ | 26 MB      |       7
 public          | gbim_belief                                                     | 16 kB      |       8
 public          | gbim_belief_edges                                               | 24 kB      |       9
 public          | gbim_belief_evidence                                            | 231 MB     |       5
 public          | gbim_beliefs                                                    | 2413 MB    |      12
 public          | gbim_entities                                                   | 64 kB      |       7
 public          | gbim_entity_clusters                                            | 152 kB     |       6
 public          | gbim_entity_land_candidates                                     | 6672 kB    |       5
 public          | gbim_evidence                                                   | 501 MB     |      10
 public          | gbim_full_points                                                | 14 MB      |       6
 public          | gbim_full_points_raw                                            | 132 MB     |       7
 public          | gbim_layer_catalog                                              | 104 kB     |       6
 public          | gbim_layer_config                                               | 32 kB      |       9
 public          | gbim_layer_manifest                                             | 96 kB      |       3
 public          | gbim_source_epochs                                              | 96 kB      |       3
 public          | gbim_source_tables_used                                         | 64 kB      |       1
 public          | gbim_worldview_entity                                           | 9060 MB    |      12
 public          | gbim_worldview_entity_backup_small                              | 160 kB     |       8
 public          | gbim_worldviews                                                 | 48 kB      |       9
 public          | gbimbeliefnormalized                                            | 24 GB      |      12
 public          | geographicalnamesonusgstopomaps_usgs_200601_ll27                | 5816 kB    |       5
 public          | geographicalnamesonusgstopomaps_usgs_200601_ll27_attrs_raw      | 6528 kB    |       7
 public          | geographicalnamesonusgstopomaps_usgs_200601_utm83               | 5888 kB    |       5
 public          | geographicalnamesonusgstopomaps_usgs_200601_utm83_attrs_raw     | 7336 kB    |       7
 public          | geographicnamesonusgstopomaps_current_usgs_20110801_ll83        | 4288 kB    |       5
 public          | geographicnamesonusgstopomaps_current_usgs_20110801_ll83_attrs_ | 5344 kB    |       7
 public          | geographicnamesonusgstopomaps_current_usgs_20110801_utm83       | 4352 kB    |       5
 public          | geographicnamesonusgstopomaps_current_usgs_20110801_utm83_attrs | 5368 kB    |       7
 public          | geographicnamesonusgstopomaps_historical_usgs_20110801_ll83     | 1048 kB    |       5
 public          | geographicnamesonusgstopomaps_historical_usgs_20110801_ll83_att | 1192 kB    |       7
 public          | geographicnamesonusgstopomaps_historical_usgs_20110801_utm83    | 1048 kB    |       5
 public          | geographicnamesonusgstopomaps_historical_usgs_20110801_utm83_at | 1328 kB    |       7
 public          | geographicnamesonusgstopomaps_usgs_20110801_ll83                | 5016 kB    |       5
 public          | geographicnamesonusgstopomaps_usgs_20110801_ll83_attrs_raw      | 6192 kB    |       7
 public          | geographicnamesonusgstopomaps_usgs_20110801_utm83               | 5088 kB    |       5
 public          | geographicnamesonusgstopomaps_usgs_20110801_utm83_attrs_raw     | 6352 kB    |       7
 public          | geolgyl_reg_ll83                                                | 208 kB     |       5
 public          | geolgyl_reg_ll83_attrs_raw                                      | 560 kB     |       7
 public          | geolgyp_reg_ll83                                                | 56 kB      |       5
 public          | geolgyp_reg_ll83_attrs_raw                                      | 88 kB      |       7
 public          | geospatial_features                                             | 38 GB      |      24
 public          | geospatial_layers                                               | 32 kB      |       7
 public          | geotextl_reg_ll83                                               | 48 kB      |       5
 public          | geotextl_reg_ll83_attrs_raw                                     | 64 kB      |       7
 public          | glacagl_reg_ll83                                                | 48 kB      |       5
 public          | glacagl_reg_ll83_attrs_raw                                      | 72 kB      |       7
 public          | glacal_reg_ll83                                                 | 16 kB      |       5
 public          | glacal_reg_ll83_attrs_raw                                       | 16 kB      |       7
 public          | hazardmitigationbuyout_20250929_polygons_utm83                  | 400 kB     |       5
 public          | hazardmitigationbuyout_20250929_polygons_utm83_attrs_raw        | 920 kB     |       7
 public          | hazardmitigationbuyout_20250929_polygons_wma84                  | 504 kB     |       5
 public          | hazardmitigationbuyout_20250929_polygons_wma84_attrs_raw        | 968 kB     |       7
 public          | healthruralfacilities_manysources_utm83                         | 16 kB      |       5
 public          | healthruralfacilities_manysources_utm83_attrs_raw               | 48 kB      |       7
 public          | highered_wvemd_072420_utm83                                     | 16 kB      |       5
 public          | highered_wvemd_072420_utm83_attrs_raw                           | 16 kB      |       7
 public          | highered_wvemd_072420_wgc84                                     | 16 kB      |       5
 public          | highered_wvemd_072420_wgc84_attrs_raw                           | 16 kB      |       7
 public          | historicalaerialphotographycountycoverage_wvgistc_utm83         | 16 kB      |       5
 public          | historicalaerialphotographycountycoverage_wvgistc_utm83_attrs_r | 56 kB      |       7
 public          | hospitals                                                       | 16 kB      |       5
 public          | hospitals_attrs_raw                                             | 16 kB      |       7
 public          | hospitals_wvdem_040519_gcs84                                    | 16 kB      |       5
 public          | hospitals_wvdem_040519_gcs84_attrs_raw                          | 48 kB      |       7
 public          | hospitals_wvdem_040519_utm83                                    | 16 kB      |       5
 public          | hospitals_wvdem_040519_utm83_attrs_raw                          | 48 kB      |       7
 public          | hospitalswvdem040519utm83                                       | 8192 bytes |       5
 public          | hospitalswvdem040519utm83_attrs_raw                             | 8192 bytes |       7
 public          | impact_reg_ll83                                                 | 16 kB      |       5
 public          | impact_reg_ll83_attrs_raw                                       | 16 kB      |       7
 public          | indexgrid15minutequads_wvgistc_ll83                             | 128 kB     |       5
 public          | indexgrid15minutequads_wvgistc_ll83_attrs_raw                   | 152 kB     |       7
 public          | indexgrid15minutequads_wvgistc_utm83                            | 112 kB     |       5
 public          | indexgrid15minutequads_wvgistc_utm83_attrs_raw                  | 232 kB     |       7
 public          | indexgrid15minutewithcounties_wvgistc_utm27                     | 136 kB     |       5
 public          | indexgrid15minutewithcounties_wvgistc_utm27_attrs_raw           | 296 kB     |       7
 public          | indexgrid1minutequads_wvgistc_ll83                              | 16 kB      |       5
 public          | indexgrid1minutequads_wvgistc_ll83_attrs_raw                    | 48 kB      |       7
 public          | industrialbuildings_wvdo_200807_utm83                           | 48 kB      |       5
 public          | industrialbuildings_wvdo_200807_utm83_attrs_raw                 | 56 kB      |       7
 public          | industrialparks_wvdo_200078_utm83                               | 48 kB      |       5
 public          | industrialparks_wvdo_200078_utm83_attrs_raw                     | 72 kB      |       7
 public          | industrialsites_wvdo_200807_utm83                               | 56 kB      |       5
 public          | industrialsites_wvdo_200807_utm83_attrs_raw                     | 96 kB      |       7
 public          | inedexgrid1minutequads_wvgistc_utm83                            | 16 kB      |       5
 public          | inedexgrid1minutequads_wvgistc_utm83_attrs_raw                  | 48 kB      |       7
 public          | intake_submissions                                              | 8192 bytes |      10
 public          | intermodalterminalfacilities_usdot_1997_ll83                    | 56 kB      |       5
 public          | intermodalterminalfacilities_usdot_1997_ll83_attrs_raw          | 56 kB      |       7
 public          | intermodalterminalfacilities_usdot_1997_utm83                   | 56 kB      |       5
 public          | intermodalterminalfacilities_usdot_1997_utm83_attrs_raw         | 56 kB      |       7
 public          | layer_config                                                    | 88 kB      |       6
 public          | libraries_manysources_2001_ll27                                 | 64 kB      |       5
 public          | libraries_manysources_2001_ll27_attrs_raw                       | 72 kB      |       7
 public          | libraries_manysources_2001_utm83                                | 64 kB      |       5
 public          | libraries_manysources_2001_utm83_attrs_raw                      | 72 kB      |       7
 public          | local_resources                                                 | 32 kB      |      17
 public          | local_resources_index                                           | 32 kB      |      11
 public          | majorriversandlakesline_nhd_2002_ll83                           | 16 kB      |       5
 public          | majorriversandlakesline_nhd_2002_ll83_attrs_raw                 | 56 kB      |       7
 public          | majorriversandlakesline_nhd_2002_utm83                          | 16 kB      |       5
 public          | majorriversandlakesline_nhd_2002_utm83_attrs_raw                | 56 kB      |       7
 public          | majorriversandlakespolygon_nhd_2002_poly_ll83                   | 48 kB      |       5
 public          | majorriversandlakespolygon_nhd_2002_poly_ll83_attrs_raw         | 64 kB      |       7
 public          | majorriversandlakespolygon_nhd_2002_utm83                       | 48 kB      |       5
 public          | majorriversandlakespolygon_nhd_2002_utm83_attrs_raw             | 64 kB      |       7
 public          | manufacturingandbusiness_wvdo_200803_utm83                      | 1144 kB    |       5
 public          | manufacturingandbusiness_wvdo_200803_utm83_attrs_raw            | 1424 kB    |       7
 public          | memories                                                        | 80 kB      |      10
 public          | metfacp_reg_ll83                                                | 16 kB      |       5
 public          | metfacp_reg_ll83_attrs_raw                                      | 16 kB      |       7
 public          | metropolitanandmicropolitanstatisticalareas_census_2020_utm83   | 16 kB      |       5
 public          | metropolitanandmicropolitanstatisticalareas_census_2020_utm83_a | 16 kB      |       7
 public          | metropolitanandmicropolitanstatisticalareas_census_2020_wma84   | 16 kB      |       5
 public          | metropolitanandmicropolitanstatisticalareas_census_2020_wma84_a | 16 kB      |       7
 public          | metropolitanandmicropolitanstatisticalareascensus201111gcs83    | 16 kB      |       5
 public          | metropolitanandmicropolitanstatisticalareascensus201111gcs83att | 48 kB      |       7
 public          | metropolitanandmicropolitanstatisticalareascensus201111utm83    | 16 kB      |       5
 public          | metropolitanandmicropolitanstatisticalareascensus201111utm83att | 48 kB      |       7
 public          | metropolitanstatisticalareas_uscensus_199901_ll83               | 16 kB      |       5
 public          | metropolitanstatisticalareas_uscensus_199901_ll83_attrs_raw     | 16 kB      |       7
 public          | metropolitanstatisticalareas_uscensus_199901_utm83              | 16 kB      |       5
 public          | metropolitanstatisticalareas_uscensus_199901_utm83_attrs_raw    | 16 kB      |       7
 public          | mineraloperations_usgs_200204_ll83                              | 16 kB      |       5
 public          | mineraloperations_usgs_200204_ll83_attrs_raw                    | 48 kB      |       7
 public          | mineraloperations_usgs_200204_utm83                             | 16 kB      |       5
 public          | mineraloperations_usgs_200204_utm83_attrs_raw                   | 48 kB      |       7
 public          | minesabandonedlandsline_wvdep_1996_noprojectoin                 | 1376 kB    |       5
 public          | minesabandonedlandsline_wvdep_1996_noprojectoin_attrs_raw       | 2600 kB    |       7
 public          | minesabandonedlandspoint_wvdep_1996_noprojection                | 64 kB      |       5
 public          | minesabandonedlandspoint_wvdep_1996_noprojection_attrs_raw      | 64 kB      |       7
 public          | minesabandonedlandspolygon_wvdep_1996_noprojection              | 320 kB     |       5
 public          | minesabandonedlandspolygon_wvdep_1996_noprojection_attrs_raw    | 552 kB     |       7
 public          | nationalatlasstreams_usgs_199903_ll83                           | 200 kB     |       5
 public          | nationalatlasstreams_usgs_199903_ll83_attrs_raw                 | 440 kB     |       7
 public          | nationalatlasstreams_usgs_199903_utm83                          | 200 kB     |       5
 public          | nationalatlasstreams_usgs_199903_utm83_attrs_raw                | 432 kB     |       7
 public          | nationalregister_point_20200923                                 | 120 kB     |       5
 public          | nationalregister_point_20200923_attrs_raw                       | 144 kB     |       7
 public          | nationalregister_point_20200923_utm27                           | 120 kB     |       5
 public          | nationalregister_point_20200923_utm27_attrs_raw                 | 144 kB     |       7
 public          | nationalwaterwaynetwork_usarmycorpsofengineers_2001_ll83        | 48 kB      |       5
 public          | nationalwaterwaynetwork_usarmycorpsofengineers_2001_ll83_attrs_ | 64 kB      |       7
 public          | nationalwaterwaynetwork_usarmycorpsofengineers_2001_utm83       | 48 kB      |       5
 public          | nationalwaterwaynetwork_usarmycorpsofengineers_2001_utm83_attrs | 64 kB      |       7
 public          | nationalwaterwaynetworkports_usarmycorpsofengineers_2001_ll83   | 16 kB      |       5
 public          | nationalwaterwaynetworkports_usarmycorpsofengineers_2001_ll83_a | 16 kB      |       7
 public          | nationalwaterwaynetworkports_usarmycorpsofengineers_2001_utm83  | 16 kB      |       5
 public          | nationalwaterwaynetworkports_usarmycorpsofengineers_2001_utm83_ | 16 kB      |       7
 public          | naviagablewaterways_usarmycropsofengineers_2006_utm83           | 16 kB      |       5
 public          | naviagablewaterways_usarmycropsofengineers_2006_utm83_attrs_raw | 16 kB      |       7
 public          | navigablewaterwaysrivermiles_usarmycropsofengineers_2006_utm83  | 96 kB      |       5
 public          | navigablewaterwaysrivermiles_usarmycropsofengineers_2006_utm83_ | 112 kB     |       7
 public          | navigablewaterwaysstructures_usarmycorpsofengineers_2006_utm83  | 4472 kB    |       5
 public          | navigablewaterwaysstructures_usarmycorpsofengineers_2006_utm83_ | 5696 kB    |       7
 public          | nursinghomes_wvdem_041219_gcs84                                 | 24 kB      |       5
 public          | nursinghomes_wvdem_041219_gcs84_attrs_raw                       | 48 kB      |       7
 public          | nursinghomes_wvdem_041219_utm83                                 | 48 kB      |       5
 public          | nursinghomes_wvdem_041219_utm83_attrs_raw                       | 48 kB      |       7
 public          | officebuildings_wvdo_200807_utm83                               | 48 kB      |       5
 public          | officebuildings_wvdo_200807_utm83_attrs_raw                     | 48 kB      |       7
 public          | paroleoffices_manysources_2008_utm83                            | 16 kB      |       5
 public          | paroleoffices_manysources_2008_utm83_attrs_raw                  | 16 kB      |       7
 public          | paroleoffices_manysources_2008_wgs84                            | 16 kB      |       5
 public          | paroleoffices_manysources_2008_wgs84_attrs_raw                  | 16 kB      |       7
 public          | placesofworship_hsip_20080723_utm83                             | 48 kB      |       5
 public          | placesofworship_hsip_20080723_utm83_attrs_raw                   | 48 kB      |       7
 public          | placesofworship_hsip_20080723_wgs84                             | 48 kB      |       5
 public          | placesofworship_hsip_20080723_wgs84_attrs_raw                   | 48 kB      |       7
 public          | policedept_wvdem_012319_gcs84                                   | 48 kB      |       5
 public          | policedept_wvdem_012319_gcs84_attrs_raw                         | 80 kB      |       7
 public          | policedept_wvdem_012319_utm83                                   | 72 kB      |       5
 public          | policedept_wvdem_012319_utm83_attrs_raw                         | 80 kB      |       7
 public          | populatedplaces_census_201112_utm83                             | 80 kB      |       5
 public          | populatedplaces_census_201112_utm83_attrs_raw                   | 96 kB      |       7
 public          | populatedplaces_census_20112_gcs83                              | 80 kB      |       5
 public          | populatedplaces_census_20112_gcs83_attrs_raw                    | 96 kB      |       7
 public          | populatedplaces_census_2020_utm83                               | 88 kB      |       5
 public          | populatedplaces_census_2020_utm83_attrs_raw                     | 96 kB      |       7
 public          | populatedplaces_census_2020_wma84                               | 80 kB      |       5
 public          | populatedplaces_census_2020_wma84_attrs_raw                     | 96 kB      |       7
 public          | populatedplaces_uscensus_1990_ll83                              | 64 kB      |       5
 public          | populatedplaces_uscensus_1990_ll83_attrs_raw                    | 80 kB      |       7
 public          | populatedplaces_uscensus_1990_utm83                             | 64 kB      |       5
 public          | populatedplaces_uscensus_1990_utm83_attrs_raw                   | 80 kB      |       7
 public          | populationdatablockgroups_uscensus_2000_ll83                    | 224 kB     |       5
 public          | populationdatablockgroups_uscensus_2000_ll83_attrs_raw          | 528 kB     |       7
 public          | populationdatablockgroups_uscensus_2000_utm83                   | 240 kB     |       5
 public          | populationdatablockgroups_uscensus_2000_utm83_attrs_raw         | 536 kB     |       7
 public          | pow_wvgistc_062919_utm83                                        | 600 kB     |       5
 public          | pow_wvgistc_062919_utm83_attrs_raw                              | 792 kB     |       7
 public          | pow_wvgistc_062919_wgs84                                        | 600 kB     |       5
 public          | pow_wvgistc_062919_wgs84_attrs_raw                              | 816 kB     |       7
 public          | program                                                         | 48 kB      |      43
 public          | program_authority_links                                         | 24 kB      |       4
 public          | program_catalog                                                 | 32 kB      |      10
 public          | program_eligibility                                             | 8192 bytes |      11
 public          | program_entity_links                                            | 2800 kB    |       5
 public          | program_evidence_links                                          | 24 kB      |       4
 public          | program_income_limit_rules                                      | 24 kB      |       2
 public          | program_income_source_policy                                    | 24 kB      |      13
 public          | program_manual_rule_links                                       | 24 kB      |       2
 public          | program_name_crosswalk                                          | 8192 bytes |       2
 public          | program_target_config                                           | 32 kB      |       3
 public          | publichealthdepts_hsip_20091229_gcs83                           | 16 kB      |       5
 public          | publichealthdepts_hsip_20091229_gcs83_attrs_raw                 | 48 kB      |       7
 public          | publichealthdepts_hsip_20091229_utm83                           | 16 kB      |       5
 public          | publichealthdepts_hsip_20091229_utm83_attrs_raw                 | 48 kB      |       7
 public          | railnetworkregion_usdot_200203_ll83                             | 1440 kB    |       5
 public          | railnetworkregion_usdot_200203_ll83_attrs_raw                   | 3784 kB    |       7
 public          | railnetworkregion_usdot_200203_utm83                            | 1440 kB    |       5
 public          | railnetworkregion_usdot_200203_utm83_attrs_raw                  | 3680 kB    |       7
 public          | railnetworkwv_usdot_200203_ll83                                 | 304 kB     |       5
 public          | railnetworkwv_usdot_200203_ll83_attrs_raw                       | 760 kB     |       7
 public          | railnetworkwv_usdot_200203_utm83                                | 304 kB     |       5
 public          | railnetworkwv_usdot_200203_utm83_attrs_raw                      | 760 kB     |       7
 public          | railroads_rahalltransportationinstitute_2005_utm83              | 392 kB     |       5
 public          | railroads_rahalltransportationinstitute_2005_utm83_attrs_raw    | 896 kB     |       7
 public          | realtimestreamflowstations_usgs_200012_ll27                     | 48 kB      |       5
 public          | realtimestreamflowstations_usgs_200012_ll27_attrs_raw           | 48 kB      |       7
 public          | realtimestreamflowstations_usgs_200012_utm27                    | 48 kB      |       5
 public          | realtimestreamflowstations_usgs_200012_utm27_attrs_raw          | 48 kB      |       7
 public          | realtimestreamflowstations_usgs_200012_utm83                    | 48 kB      |       5
 public          | realtimestreamflowstations_usgs_200012_utm83_attrs_raw          | 48 kB      |       7
 public          | recreationalwwtrails_ofwv_20151117_utm83                        | 64 kB      |       5
 public          | recreationalwwtrails_ofwv_20151117_utm83_attrs_raw              | 120 kB     |       7
 public          | regionalplanninganddevelopmentcouncil_wvdo_1971_ll83            | 16 kB      |       5
 public          | regionalplanninganddevelopmentcouncil_wvdo_1971_ll83_attrs_raw  | 48 kB      |       7
 public          | regionalplanninganddevelopmentcouncil_wvdo_1971_utm83           | 16 kB      |       5
 public          | regionalplanninganddevelopmentcouncil_wvdo_1971_utm83_attrs_raw | 56 kB      |       7
 public          | resource_county_coverage                                        | 8192 bytes |       2
 public          | resource_eligibility                                            | 8192 bytes |      11
 public          | samhsa_provider_building_join                                   | 3296 kB    |      18
 public          | samhsa_provider_spatial_grounded                                | 3312 kB    |      20
 public          | samhsa_provider_stage                                           | 4720 kB    |      16
 public          | sewertreatmentplants_wvdep_200203_utm83                         | 192 kB     |       5
 public          | sewertreatmentplants_wvdep_200203_utm83_attrs_raw               | 232 kB     |       7
 public          | solidwastefacilities_wvdep_200202_ll83                          | 48 kB      |       5
 public          | solidwastefacilities_wvdep_200202_ll83_attrs_raw                | 48 kB      |       7
 public          | solidwastefacilities_wvdep_200202_utm83                         | 48 kB      |       5
 public          | solidwastefacilities_wvdep_200202_utm83_attrs_raw               | 48 kB      |       7
 public          | spatial_ref_sys                                                 | 7144 kB    |       5
 public          | spatial_role_scopes                                             | 40 kB      |       7
 public          | springs_wvges_1986_ll83                                         | 64 kB      |       5
 public          | springs_wvges_1986_ll83_attrs_raw                               | 72 kB      |       7
 public          | springs_wvges_1986_utm83                                        | 64 kB      |       5
 public          | springs_wvges_1986_utm83_attrs_raw                              | 72 kB      |       7
 public          | stateofwvhousedistricts_wvlegislativeservices_2010              | 48 kB      |       5
 public          | stateofwvhousedistricts_wvlegislativeservices_2010_attrs_raw    | 48 kB      |       7
 public          | stateofwvsenatedistricts_wvlegislativeservices_2010             | 16 kB      |       5
 public          | stateofwvsenatedistricts_wvlegislativeservices_2010_attrs_raw   | 16 kB      |       7
 public          | states_region_ll83                                              | 16 kB      |       5
 public          | states_region_ll83_attrs_raw                                    | 56 kB      |       7
 public          | structurepointsnorth_samb_2003_utm83                            | 69 MB      |       5
 public          | structurepointsnorth_samb_2003_utm83_attrs_raw                  | 90 MB      |       7
 public          | structurepointssouth_samb_2003_utm83                            | 83 MB      |       5
 public          | structurepointssouth_samb_2003_utm83_attrs_raw                  | 109 MB     |       7
 public          | structurepolygons_samb_2003_utm83                               | 1808 kB    |       5
 public          | structurepolygons_samb_2003_utm83_attrs_raw                     | 4640 kB    |       7
 public          | summits_gistc_052012_utm83_shp                                  | 136 kB     |       5
 public          | summits_gistc_052012_utm83_shp_attrs_raw                        | 168 kB     |       7
 public          | summits_gistc_052012_wgs84_shp                                  | 136 kB     |       5
 public          | summits_gistc_052012_wgs84_shp_attrs_raw                        | 168 kB     |       7
 public          | surveycontrol_nationalgeodeticsurvey_102011_gcs83               | 1104 kB    |       5
 public          | surveycontrol_nationalgeodeticsurvey_102011_gcs83_attrs_raw     | 1312 kB    |       7
 public          | tiger_county_2022                                               | 8192 bytes |      19
 public          | timberremovalvolume_usfs_1996_utm83                             | 16 kB      |       5
 public          | timberremovalvolume_usfs_1996_utm83_attrs_raw                   | 56 kB      |       7
 public          | tl_2020_54_bg                                                   | 25 MB      |      14
 public          | tl_2020_54_tabblock20                                           | 175 MB     |      19
 public          | tmp_building_block_nearest_sample                               | 288 kB     |       3
 public          | towers_wvpublicbroadcasting_2002_ll83                           | 16 kB      |       5
 public          | towers_wvpublicbroadcasting_2002_ll83_attrs_raw                 | 16 kB      |       7
 public          | towers_wvpublicbroadcasting_2002_utm83                          | 16 kB      |       5
 public          | towers_wvpublicbroadcasting_2002_utm83_attrs_raw                | 16 kB      |       7
 public          | towersam_fcc_200202_utm83                                       | 16 kB      |       5
 public          | towersam_fcc_200202_utm83_attrs_raw                             | 48 kB      |       7
 public          | towersasr_fcc_200202_ll83                                       | 112 kB     |       5
 public          | towersasr_fcc_200202_ll83_attrs_raw                             | 128 kB     |       7
 public          | towersasr_fcc_200202_utm83                                      | 120 kB     |       5
 public          | towersasr_fcc_200202_utm83_attrs_raw                            | 144 kB     |       7
 public          | towerscellular_fcc_200202_ll83                                  | 64 kB      |       5
 public          | towerscellular_fcc_200202_ll83_attrs_raw                        | 64 kB      |       7
 public          | towerscellular_fcc_200202_utm83                                 | 64 kB      |       5
 public          | towerscellular_fcc_200202_utm83_attrs_raw                       | 72 kB      |       7
 public          | towersfm_fcc_200202_utm83                                       | 16 kB      |       5
 public          | towersfm_fcc_200202_utm83_attrs_raw                             | 48 kB      |       7
 public          | towersmicrowave_fcc_200202_ll83                                 | 264 kB     |       5
 public          | towersmicrowave_fcc_200202_ll83_attrs_raw                       | 304 kB     |       7
 public          | towersmicrowave_fcc_200202_utm83                                | 264 kB     |       5
 public          | towersmicrowave_fcc_200202_utm83_attrs_raw                      | 344 kB     |       7
 public          | towerspager_fcc_200202_ll83                                     | 64 kB      |       5
 public          | towerspager_fcc_200202_ll83_attrs_raw                           | 72 kB      |       7
 public          | towerspager_fcc_200202_utm83                                    | 64 kB      |       5
 public          | towerspager_fcc_200202_utm83_attrs_raw                          | 72 kB      |       7
 public          | towersprivate_fcc_200202_ll83                                   | 648 kB     |       5
 public          | towersprivate_fcc_200202_ll83_attrs_raw                         | 744 kB     |       7
 public          | towersprivate_fcc_200202_utm83                                  | 648 kB     |       5
 public          | towersprivate_fcc_200202_utm83_attrs_raw                        | 840 kB     |       7
 public          | uei_registry                                                    | 8192 bytes |      13
 public          | us_counties                                                     | 2608 kB    |       6
 public          | us_counties_tmp                                                 | 130 MB     |      19
 public          | us_zips                                                         | 864 MB     |       4
 public          | us_zips_tmp                                                     | 865 MB     |      11
 public          | user_compliance_task                                            | 32 kB      |      13
 public          | utility_discount_enrollment                                     | 48 kB      |      15
 public          | veteransaffairsfacilities_manysources_200503_utm83              | 16 kB      |       5
 public          | veteransaffairsfacilities_manysources_200503_utm83_attrs_raw    | 16 kB      |       7
 public          | veteransaffairsfacilities_manysources_200503_wgs84              | 16 kB      |       5
 public          | veteransaffairsfacilities_manysources_200503_wgs84_attrs_raw    | 16 kB      |       7
 public          | votingdistrictswv_legislativeservices_2002_ll83                 | 264 kB     |       5
 public          | votingdistrictswv_legislativeservices_2002_ll83_attrs_raw       | 512 kB     |       7
 public          | votingdistrictswv_legislativeservices_2002_utm83                | 272 kB     |       5
 public          | votingdistrictswv_legislativeservices_2002_utm83_attrs_raw      | 632 kB     |       7
 public          | votingdistrictswv_uscensus_2000_utm83                           | 248 kB     |       5
 public          | votingdistrictswv_uscensus_2000_utm83_attrs_raw                 | 464 kB     |       7
 public          | weatherstations_nationalclimatedatacenter_1999_gcs83            | 56 kB      |       5
 public          | weatherstations_nationalclimatedatacenter_1999_gcs83_attrs_raw  | 56 kB      |       7
 public          | weatherstations_nationalclimatedatacenter_1999_utm27            | 56 kB      |       5
 public          | weatherstations_nationalclimatedatacenter_1999_utm27_attrs_raw  | 64 kB      |       7
 public          | windenergyresource_nationalrenewableenergylab_200901_utm83      | 14 MB      |       5
 public          | windenergyresource_nationalrenewableenergylab_200901_utm83_attr | 33 MB      |       7
 public          | windenergyresource_nationalrenewableenergylab_200901_wgs84      | 14 MB      |       5
 public          | windenergyresource_nationalrenewableenergylab_200901_wgs84_attr | 34 MB      |       7
 public          | workforceinvestmentareas_wvgistc_200208_ll83                    | 16 kB      |       5
 public          | workforceinvestmentareas_wvgistc_200208_ll83_attrs_raw          | 56 kB      |       7
 public          | wv_county_bbox_geom                                             | 8192 bytes |       3
 public          | wv_county_boundaries_24k_topo_updated_2022_utm83_attrs_raw      | 56 kB      |       7
 public          | wv_county_names                                                 | 8192 bytes |       3
 public          | wv_income_manual_income_limits                                  | 32 kB      |      16
 public          | wv_income_manual_income_sources                                 | 32 kB      |       4
 public          | wv_income_manual_income_treatment                               | 32 kB      |       6
 public          | wv_income_manual_income_treatment_extended                      | 32 kB      |      10
 public          | wv_income_manual_rules                                          | 32 kB      |       9
 public          | wv_microsoft_20180207_utm17n83                                  | 106 MB     |       5
 public          | wv_microsoft_20180207_utm17n83_attrs_raw                        | 295 MB     |       7
 public          | wv_tax_districts_ll83                                           | 96 kB      |       5
 public          | wv_tax_districts_ll83_attrs_raw                                 | 208 kB     |       7
 public          | wv_tax_districts_utm83_attrs_raw                                | 200 kB     |       7
 public          | wv_tax_districts_wma84                                          | 96 kB      |       5
 public          | wv_tax_districts_wma84_attrs_raw                                | 208 kB     |       7
 public          | wv_zip_zcta_raw                                                 | 480 kB     |      17
 public          | wvgistc_building_footprints                                     | 205 MB     |       5
 public          | wvgistc_building_footprints_attrs_raw                           | 557 MB     |       7
 public          | wvgistcbuildingfootprints                                       | 305 MB     |       5
 public          | wvgistcbuildingfootprints_attrs_raw                             | 575 MB     |       7
 public          | wvgistcbuildingfootprintsattrsraw                               | 575 MB     |       7
 public          | wvstatebounadary100k_usgs_200203_utm83                          | 16 kB      |       5
 public          | wvstatebounadary100k_usgs_200203_utm83_attrs_raw                | 16 kB      |       7
 public          | wvstateboundary100k_usgs_200203_ll83                            | 16 kB      |       5
 public          | wvstateboundary100k_usgs_200203_ll83_attrs_raw                  | 16 kB      |       7
 public          | wvstateboundary24k_usgs_200203_ll83                             | 16 kB      |       5
 public          | wvstateboundary24k_usgs_200203_ll83_attrs_raw                   | 16 kB      |       7
 public          | wvstateboundary24k_usgs_200203_utm83                            | 16 kB      |       5
 public          | wvstateboundary24k_usgs_200203_utm83_attrs_raw                  | 16 kB      |       7
 public          | wvstatehousedistricts_manysources_1992_ll83                     | 16 kB      |       5
 public          | wvstatehousedistricts_manysources_1992_ll83_attrs_raw           | 48 kB      |       7
 public          | wvstatehousedistricts_manysources_1992_utm83                    | 16 kB      |       5
 public          | wvstatehousedistricts_manysources_1992_utm83_attrs_raw          | 56 kB      |       7
 public          | wvstatehousedistricts_manysources_2002_ll83                     | 16 kB      |       5
 public          | wvstatehousedistricts_manysources_2002_ll83_attrs_raw           | 48 kB      |       7
 public          | wvstatehousedistricts_manysources_2002_utm83                    | 16 kB      |       5
 public          | wvstatehousedistricts_manysources_2002_utm83_attrs_raw          | 56 kB      |       7
 public          | wvstatehousedistricts_wvlegislativeservices_2020_utm83_attrs_ra | 64 kB      |       7
 public          | wvstatesenatedistricts_manysources_1992_ll83                    | 16 kB      |       5
 public          | wvstatesenatedistricts_manysources_1992_ll83_attrs_raw          | 16 kB      |       7
 public          | wvstatesenatedistricts_manysources_1992_utm83                   | 16 kB      |       5
 public          | wvstatesenatedistricts_manysources_1992_utm83_attrs_raw         | 16 kB      |       7
 public          | wvstatesenatedistricts_manysources_2002_ll83                    | 16 kB      |       5
 public          | wvstatesenatedistricts_manysources_2002_ll83_attrs_raw          | 16 kB      |       7
 public          | wvstatesenatedistricts_manysources_2002_utm83                   | 16 kB      |       5
 public          | wvstatesenatedistricts_manysources_2002_utm83_attrs_raw         | 16 kB      |       7
 public          | wvstatesenatedistricts_wvlegislativeservices_2020_utm83_attrs_r | 16 kB      |       7
 public          | zcta_county_rel                                                 | 6936 kB    |       6
 public          | zcta_polygons                                                   | 865 MB     |      11
 public          | zipcodetabulationarea_census_2020_raw                           | 865 MB     |      11
 public          | zipcodetabulationarea_census_2020_utm83_attrs_raw               | 264 kB     |       7
 public          | zipcodetabulationarea_census_2020_wma84                         | 120 kB     |       5
 public          | zipcodetabulationarea_census_2020_wma84_attrs_raw               | 264 kB     |       7
 raw             | boundaryappalachianbasin_wvges_1996_utm83_attrs                 | 80 kB      |       4
 raw             | boundaryappalachianbasin_wvges_1996_utm83_stage                 | 128 kB     |       7
 raw             | wv_tax_parcels_2025                                             | 1013 MB    |      21
 tiger           | addr                                                            | 24 kB      |      14
 tiger           | addrfeat                                                        | 48 kB      |      25
 tiger           | bg                                                              | 16 kB      |      14
 tiger           | county                                                          | 32 kB      |      19
 tiger           | county_lookup                                                   | 24 kB      |       4
 tiger           | countysub_lookup                                                | 24 kB      |       6
 tiger           | cousub                                                          | 32 kB      |      20
 tiger           | direction_lookup                                                | 40 kB      |       2
 tiger           | edges                                                           | 40 kB      |      33
 tiger           | faces                                                           | 40 kB      |      75
 tiger           | featnames                                                       | 32 kB      |      20
 tiger           | geocode_settings                                                | 16 kB      |       5
 tiger           | geocode_settings_default                                        | 32 kB      |       5
 tiger           | loader_lookuptables                                             | 64 kB      |      14
 tiger           | loader_platform                                                 | 32 kB      |      10
 tiger           | loader_variables                                                | 32 kB      |       5
 tiger           | pagc_gaz                                                        | 128 kB     |       6
 tiger           | pagc_lex                                                        | 336 kB     |       6
 tiger           | pagc_rules                                                      | 856 kB     |       3
 tiger           | place                                                           | 32 kB      |      19
 tiger           | place_lookup                                                    | 24 kB      |       4
 tiger           | secondary_unit_lookup                                           | 40 kB      |       2
 tiger           | state                                                           | 40 kB      |      15
 tiger           | state_lookup                                                    | 104 kB     |       4
 tiger           | street_type_lookup                                              | 128 kB     |       3
 tiger           | tabblock                                                        | 16 kB      |      16
 tiger           | tabblock20                                                      | 16 kB      |      18
 tiger           | tract                                                           | 16 kB      |      14
 tiger           | zcta5                                                           | 24 kB      |      12
 tiger           | zip_lookup                                                      | 8192 bytes |      10
 tiger           | zip_lookup_all                                                  | 0 bytes    |      10
 tiger           | zip_lookup_base                                                 | 8192 bytes |       5
 tiger           | zip_state                                                       | 8192 bytes |       3
 tiger           | zip_state_loc                                                   | 8192 bytes |       4
 topology        | layer                                                           | 24 kB      |       8
 topology        | topology                                                        | 24 kB      |       5
(692 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ echo "=== msjarvisgis-recovery geometry columns ==="
docker exec msjarvisgis-recovery psql -U postgres -d msjarvisgis -c "
SELECT f_table_schema, f_table_name, f_geometry_column, type, srid
FROM geometry_columns
ORDER BY f_table_schema, f_table_name;
" 2>/dev/null || echo "No PostGIS extension or no geometry columns"

echo ""
echo "=== jarvis-local-resources-db geometry columns ==="
docker exec jarvis-local-resources-db psql -U postgres -d msjarvisgis -c "
SELECT f_table_schema, f_table_name, f_geometry_column, type, srid
FROM geometry_columns
ORDER BY f_table_schema, f_table_name;
" 2>/dev/null || echo "No PostGIS extension or no geometry columns"
=== msjarvisgis-recovery geometry columns ===
 f_table_schema  |                          f_table_name                           | f_geometry_column |      type       | srid  
-----------------+-----------------------------------------------------------------+-------------------+-----------------+-------
 cakidd          | bldg_join__flood_structures_at_risk                             | geom              | POINT           | 26917
 cakidd          | bldg_join__nearest_hospital                                     | geom              | POINT           | 26917
 cakidd          | geospatial_features                                             | geom              | GEOMETRY        |  4326
 gbim            | gbim_attrs                                                      | bbox              | GEOMETRY        |     0
 gbim            | gbim_attrs                                                      | geom              | GEOMETRY        |     0
 gbim            | vw_blockgroup_infrastructure                                    | geom              | GEOMETRY        |     0
 gbim            | vw_city_emergency_coverage                                      | geom              | GEOMETRY        |     0
 gbim            | worldview_entity                                                | bbox              | GEOMETRY        |     0
 gbim            | worldview_entity                                                | geom              | GEOMETRY        |     0
 gbim_source_csv | amtrackrails_federalrailroadadministration_200210_utm83         | geom              | POINT           | 26917
 gbim_source_csv | blockgroups_census_2000_utm83                                   | geom              | POINT           | 26917
 gbim_source_csv | blockgroups_census_201111_utm83                                 | geom              | POINT           | 26917
 gbim_source_csv | blockgroups_census_2020_utm83                                   | geom              | POINT           | 26917
 gbim_source_csv | blocks_census_2020_utm83                                        | geom              | POINT           | 26917
 gbim_source_csv | boundaryappalachianbasin_wvges_1996_utm83                       | geom              | POINT           | 26917
 gbim_source_csv | citieswithpopulation_2500_census_201111_utm83                   | geom              | POINT           | 26917
 gbim_source_csv | citieswithpopulationover10k_uscensus_1990_utm83                 | geom              | POINT           | 26917
 gbim_source_csv | citieswithpopulationsover10k_census_2020_utm83                  | geom              | POINT           | 26917
 gbim_source_csv | citieswithpopulationsover2500_census_2020_utm83                 | geom              | POINT           | 26917
 gbim_source_csv | citieswithpopulatoinover2500_uscensus_1990_utm83                | geom              | POINT           | 26917
 gbim_source_csv | coals2_utm83                                                    | geom              | POINT           | 26917
 gbim_source_csv | communityboundary_min_att_20250121_utm83                        | geom              | POINT           | 26917
 gbim_source_csv | communityhealthproviders_wvhealthcareauthority_200802_utm83     | geom              | POINT           | 26917
 gbim_source_csv | correctionalinstitutions_hsip_20091230_utm83                    | geom              | POINT           | 26917
 gbim_source_csv | countycityparkboundaries_20201104_utm83                         | geom              | POINT           | 26917
 gbim_source_csv | countyseats_usgs_utm83                                          | geom              | POINT           | 26917
 gbim_source_csv | courthousescounty_manysources_200203_utm83                      | geom              | POINT           | 26917
 gbim_source_csv | cvfault_utm83                                                   | geom              | POINT           | 26917
 gbim_source_csv | cvpoly_utm83                                                    | geom              | POINT           | 26917
 gbim_source_csv | dams_usarmycorpsofengineers_200010_utm83                        | geom              | POINT           | 26917
 gbim_source_csv | damsnoncoal_usgs_2002_utm83                                     | geom              | POINT           | 26917
 gbim_source_csv | empowermentzonesandenterprisecommunities_uscensus_2002_utm83    | geom              | POINT           | 26917
 gbim_source_csv | excursionpassengertrains_wvdof_200102_utm83                     | geom              | POINT           | 26917
 gbim_source_csv | facilities_epa_200203_utm83                                     | geom              | POINT           | 26917
 gbim_source_csv | fire_dept_wvdem_092017_utm83                                    | geom              | POINT           | 26917
 gbim_source_csv | floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83  | geom              | POINT           | 26917
 gbim_source_csv | geographicalnamesonusgstopomaps_usgs_200601_utm83               | geom              | POINT           | 26917
 gbim_source_csv | geographicnamesonusgstopomaps_current_usgs_20110801_utm83       | geom              | POINT           | 26917
 gbim_source_csv | geographicnamesonusgstopomaps_historical_usgs_20110801_utm83    | geom              | POINT           | 26917
 gbim_source_csv | geographicnamesonusgstopomaps_usgs_20110801_utm83               | geom              | POINT           | 26917
 gbim_source_csv | hazardmitigationbuyout_20250929_polygons_utm83                  | geom              | POINT           | 26917
 gbim_source_csv | healthruralfacilities_manysources_utm83                         | geom              | POINT           | 26917
 gbim_source_csv | highered_wvemd_072420_utm83                                     | geom              | POINT           | 26917
 gbim_source_csv | historicalaerialphotographycountycoverage_wvgistc_utm83         | geom              | POINT           | 26917
 gbim_source_csv | hospitals_wvdem_040519_utm83                                    | geom              | POINT           | 26917
 gbim_source_csv | indexgrid15minutequads_wvgistc_utm83                            | geom              | POINT           | 26917
 gbim_source_csv | industrialbuildings_wvdo_200807_utm83                           | geom              | POINT           | 26917
 gbim_source_csv | industrialparks_wvdo_200078_utm83                               | geom              | POINT           | 26917
 gbim_source_csv | industrialsites_wvdo_200807_utm83                               | geom              | POINT           | 26917
 gbim_source_csv | inedexgrid1minutequads_wvgistc_utm83                            | geom              | POINT           | 26917
 gbim_source_csv | intermodalterminalfacilities_usdot_1997_utm83                   | geom              | POINT           | 26917
 gbim_source_csv | libraries_manysources_2001_utm83                                | geom              | POINT           | 26917
 gbim_source_csv | majorriversandlakesline_nhd_2002_utm83                          | geom              | POINT           | 26917
 gbim_source_csv | majorriversandlakespolygon_nhd_2002_utm83                       | geom              | POINT           | 26917
 gbim_source_csv | manufacturingandbusiness_wvdo_200803_utm83                      | geom              | POINT           | 26917
 gbim_source_csv | metropolitanandmicropolitanstatisticalareas_census_201111_utm83 | geom              | POINT           | 26917
 gbim_source_csv | metropolitanandmicropolitanstatisticalareas_census_2020_utm83   | geom              | POINT           | 26917
 gbim_source_csv | metropolitanstatisticalareas_uscensus_199901_utm83              | geom              | POINT           | 26917
 gbim_source_csv | mineraloperations_usgs_200204_utm83                             | geom              | POINT           | 26917
 gbim_source_csv | nationalatlasstreams_usgs_199903_utm83                          | geom              | POINT           | 26917
 gbim_source_csv | nationalwaterwaynetwork_usarmycorpsofengineers_2001_utm83       | geom              | POINT           | 26917
 gbim_source_csv | nationalwaterwaynetworkports_usarmycorpsofengineers_2001_utm83  | geom              | POINT           | 26917
 gbim_source_csv | naviagablewaterways_usarmycropsofengineers_2006_utm83           | geom              | POINT           | 26917
 gbim_source_csv | navigablewaterwaysrivermiles_usarmycropsofengineers_2006_utm83  | geom              | POINT           | 26917
 gbim_source_csv | navigablewaterwaysstructures_usarmycorpsofengineers_2006_utm83  | geom              | POINT           | 26917
 gbim_source_csv | nursinghomes_wvdem_041219_utm83                                 | geom              | POINT           | 26917
 gbim_source_csv | officebuildings_wvdo_200807_utm83                               | geom              | POINT           | 26917
 gbim_source_csv | paroleoffices_manysources_2008_utm83                            | geom              | POINT           | 26917
 gbim_source_csv | placesofworship_hsip_20080723_utm83                             | geom              | POINT           | 26917
 gbim_source_csv | policedept_wvdem_012319_utm83                                   | geom              | POINT           | 26917
 gbim_source_csv | populatedplaces_census_201112_utm83                             | geom              | POINT           | 26917
 gbim_source_csv | populatedplaces_census_2020_utm83                               | geom              | POINT           | 26917
 gbim_source_csv | populatedplaces_uscensus_1990_utm83                             | geom              | POINT           | 26917
 gbim_source_csv | populationdatablockgroups_uscensus_2000_utm83                   | geom              | POINT           | 26917
 gbim_source_csv | pow_wvgistc_062919_utm83                                        | geom              | POINT           | 26917
 gbim_source_csv | publichealthdepts_hsip_20091229_utm83                           | geom              | POINT           | 26917
 gbim_source_csv | railnetworkregion_usdot_200203_utm83                            | geom              | POINT           | 26917
 gbim_source_csv | railnetworkwv_usdot_200203_utm83                                | geom              | POINT           | 26917
 gbim_source_csv | railroads_rahalltransportationinstitute_2005_utm83              | geom              | POINT           | 26917
 gbim_source_csv | realtimestreamflowstations_usgs_200012_utm83                    | geom              | POINT           | 26917
 gbim_source_csv | recreationalwwtrails_ofwv_20151117_utm83                        | geom              | POINT           | 26917
 gbim_source_csv | regionalplanninganddevelopmentcouncil_wvdo_1971_utm83           | geom              | POINT           | 26917
 gbim_source_csv | sewertreatmentplants_wvdep_200203_utm83                         | geom              | POINT           | 26917
 gbim_source_csv | solidwastefacilities_wvdep_200202_utm83                         | geom              | POINT           | 26917
 gbim_source_csv | springs_wvges_1986_utm83                                        | geom              | POINT           | 26917
 gbim_source_csv | structurepointsnorth_samb_2003_utm83                            | geom              | POINT           | 26917
 gbim_source_csv | structurepointssouth_samb_2003_utm83                            | geom              | POINT           | 26917
 gbim_source_csv | structurepolygons_samb_2003_utm83                               | geom              | POINT           | 26917
 gbim_source_csv | timberremovalvolume_usfs_1996_utm83                             | geom              | POINT           | 26917
 gbim_source_csv | towers_wvpublicbroadcasting_2002_utm83                          | geom              | POINT           | 26917
 gbim_source_csv | towersam_fcc_200202_utm83                                       | geom              | POINT           | 26917
 gbim_source_csv | towersasr_fcc_200202_utm83                                      | geom              | POINT           | 26917
 gbim_source_csv | towerscellular_fcc_200202_utm83                                 | geom              | POINT           | 26917
 gbim_source_csv | towersfm_fcc_200202_utm83                                       | geom              | POINT           | 26917
 gbim_source_csv | towersmicrowave_fcc_200202_utm83                                | geom              | POINT           | 26917
 gbim_source_csv | towerspager_fcc_200202_utm83                                    | geom              | POINT           | 26917
 gbim_source_csv | towersprivate_fcc_200202_utm83                                  | geom              | POINT           | 26917
 gbim_source_csv | veteransaffairsfacilities_manysources_200503_utm83              | geom              | POINT           | 26917
 gbim_source_csv | votingdistrictswv_legislativeservices_2002_utm83                | geom              | POINT           | 26917
 gbim_source_csv | votingdistrictswv_uscensus_2000_utm83                           | geom              | POINT           | 26917
 gbim_source_csv | windenergyresource_nationalrenewableenergylab_200901_utm83      | geom              | POINT           | 26917
 gbim_source_csv | wv_county_boundaries_24k_topo_updated_2022_utm83                | geom              | POINT           | 26917
 gbim_source_csv | wv_tax_districts_utm83                                          | geom              | POINT           | 26917
 gbim_source_csv | wvstatebounadary100k_usgs_200203_utm83                          | geom              | POINT           | 26917
 gbim_source_csv | wvstateboundary24k_usgs_200203_utm83                            | geom              | POINT           | 26917
 gbim_source_csv | wvstatehousedistricts_manysources_1992_utm83                    | geom              | POINT           | 26917
 gbim_source_csv | wvstatehousedistricts_manysources_2002_utm83                    | geom              | POINT           | 26917
 gbim_source_csv | wvstatehousedistricts_wvlegislativeservices_2020_utm83          | geom              | POINT           | 26917
 gbim_source_csv | wvstatesenatedistricts_manysources_1992_utm83                   | geom              | POINT           | 26917
 gbim_source_csv | wvstatesenatedistricts_manysources_2002_utm83                   | geom              | POINT           | 26917
 gbim_source_csv | wvstatesenatedistricts_wvlegislativeservices_2020_utm83         | geom              | POINT           | 26917
 gbim_source_csv | zipcodetabulationarea_census_2020_utm83                         | geom              | POINT           | 26917
 public          | 911centers_wvdem_032819_gcs84                                   | geom              | GEOMETRY        |     0
 public          | 911centers_wvdem_032819_utm83                                   | geom              | GEOMETRY        |     0
 public          | amtrackrails_federalrailroadadministration_200210_ll83          | geom              | GEOMETRY        |     0
 public          | amtrackrails_federalrailroadadministration_200210_utm83         | geom              | GEOMETRY        |     0
 public          | benefit_county_daycare                                          | geom              | POINT           | 26917
 public          | benefit_county_medicaid                                         | geom              | POINT           | 26917
 public          | benefit_county_medicare                                         | geom              | POINT           | 26917
 public          | benefit_county_section8                                         | geom              | POINT           | 26917
 public          | benefit_county_snap                                             | geom              | POINT           | 26917
 public          | benefit_county_ssi                                              | geom              | POINT           | 26917
 public          | benefit_county_tanf                                             | geom              | POINT           | 26917
 public          | benefit_county_utility20                                        | geom              | POINT           | 26917
 public          | benefit_county_wic                                              | geom              | POINT           | 26917
 public          | bldg_join__floodplainstructuresatrisk_usarmycorpsofengineers_20 | geom              | POINT           | 26917
 public          | bldg_join__hospitals                                            | geom              | POINT           | 26917
 public          | blockgroups_census_2000_ll83                                    | geom              | GEOMETRY        |     0
 public          | blockgroups_census_2000_utm83                                   | geom              | GEOMETRY        |     0
 public          | blockgroups_census_201111_gcs83                                 | geom              | GEOMETRY        |     0
 public          | blockgroups_census_201111_utm83                                 | geom              | GEOMETRY        |     0
 public          | blockgroups_census_2020_utm83                                   | geom              | GEOMETRY        | 26917
 public          | blockgroups_census_2020_utm83_full                              | geom              | GEOMETRY        |     0
 public          | blockgroups_census_2020_wma84                                   | geom              | GEOMETRY        |     0
 public          | blocks_census_2020_utm83                                        | geom              | GEOMETRY        | 26917
 public          | blocks_census_2020_utm83_full                                   | geom              | GEOMETRY        |     0
 public          | blocks_census_2020_wma84                                        | geom              | GEOMETRY        |     0
 public          | boundaryappalachianbasin_wvges_1996_utm83                       | geom              | GEOMETRY        |     0
 public          | boundaryappalachianbasin_wvges_1996_wma84                       | geom              | GEOMETRY        |  3395
 public          | bridges                                                         | geom              | GEOMETRY        |     0
 public          | building_flood_risk                                             | building_geom     | POLYGON         | 26917
 public          | building_flood_risk                                             | floodpoint_geom   | POINT           | 26917
 public          | buildings                                                       | geom              | POLYGON         | 26917
 public          | calderl_reg_ll83                                                | geom              | GEOMETRY        |     0
 public          | citieswithpopulation_2500_census_201111_gcs83                   | geom              | GEOMETRY        |     0
 public          | citieswithpopulation_2500_census_201111_utm83                   | geom              | GEOMETRY        |     0
 public          | citieswithpopulationover10k_census_201111_gcs83                 | geom              | GEOMETRY        |     0
 public          | citieswithpopulationover10k_uscensus_1990_ll83                  | geom              | GEOMETRY        |     0
 public          | citieswithpopulationover10k_uscensus_1990_utm83                 | geom              | GEOMETRY        |     0
 public          | citieswithpopulationover2500_uscensus_1990_ll83                 | geom              | GEOMETRY        |     0
 public          | citieswithpopulationsover10k_census_2020_utm83                  | geom              | GEOMETRY        |     0
 public          | citieswithpopulationsover10k_census_2020_wma84                  | geom              | GEOMETRY        |     0
 public          | citieswithpopulationsover2500_census_2020_utm83                 | geom              | GEOMETRY        |     0
 public          | citieswithpopulationsover2500_census_2020_wma84                 | geom              | GEOMETRY        |     0
 public          | citieswithpopulatoinover2500_uscensus_1990_utm83                | geom              | GEOMETRY        |     0
 public          | coals2_ll83                                                     | geom              | GEOMETRY        |     0
 public          | coals2_utm27                                                    | geom              | GEOMETRY        |     0
 public          | coals2_utm83                                                    | geom              | GEOMETRY        |     0
 public          | community_points                                                | geom              | POINT           |  4326
 public          | communityboundary_min_att_20250121_utm83                        | geom              | GEOMETRY        |     0
 public          | communityboundary_min_att_20250121_wma84                        | geom              | GEOMETRY        |     0
 public          | communityhealthproviders_wvhealthcareauthority_200802_utm83     | geom              | GEOMETRY        | 26917
 public          | correctionalinstitutions_hsip_20091230_utm83                    | geom              | GEOMETRY        |     0
 public          | correctionalinstitutions_hsip_20091230_wgs84                    | geom              | GEOMETRY        |     0
 public          | countycityparkboundaries_20201104_utm83                         | geom              | GEOMETRY        |     0
 public          | countyseats_usgs_ll83                                           | geom              | GEOMETRY        |     0
 public          | countyseats_usgs_utm83                                          | geom              | GEOMETRY        |     0
 public          | courthousescounty_manysources_200203_ll83                       | geom              | GEOMETRY        |     0
 public          | courthousescounty_manysources_200203_utm83                      | geom              | GEOMETRY        |     0
 public          | courthousesfederal_manysources_200203_ll83                      | geom              | GEOMETRY        |     0
 public          | courthousesfederal_manysources_200203_utm                       | geom              | GEOMETRY        |     0
 public          | cvfault_ll83                                                    | geom              | GEOMETRY        |     0
 public          | cvfault_utm27                                                   | geom              | GEOMETRY        |     0
 public          | cvfault_utm83                                                   | geom              | GEOMETRY        |     0
 public          | cvpoly_ll83                                                     | geom              | GEOMETRY        |     0
 public          | cvpoly_utm27                                                    | geom              | GEOMETRY        |     0
 public          | cvpoly_utm83                                                    | geom              | GEOMETRY        |     0
 public          | dams_usarmycorpsofengineers_200010_utm83                        | geom              | GEOMETRY        |     0
 public          | dams_usarmycropsofengineers_200010_ll83                         | geom              | GEOMETRY        |     0
 public          | damsnoncoal_usgs_2002_ll27                                      | geom              | GEOMETRY        |     0
 public          | damsnoncoal_usgs_2002_utm83                                     | geom              | GEOMETRY        |     0
 public          | empowermentzonesandenterprisecommunities_uscensus_2002_utm83    | geom              | GEOMETRY        |     0
 public          | empowermentzonesandenterprisecommunitiesbytractuscens30c72907   | geom              | GEOMETRY        |     0
 public          | excursionpassengertrains_wvdof_200102_ll83                      | geom              | GEOMETRY        |     0
 public          | excursionpassengertrains_wvdof_200102_utm83                     | geom              | GEOMETRY        |     0
 public          | facilities_epa_200203_ll83                                      | geom              | GEOMETRY        |     0
 public          | facilities_epa_200203_utm83                                     | geom              | GEOMETRY        |     0
 public          | fault_reg_ll83                                                  | geom              | GEOMETRY        |     0
 public          | faultgl_reg_ll83                                                | geom              | GEOMETRY        |     0
 public          | features                                                        | geom              | GEOMETRY        |     0
 public          | fire_departments                                                | geom              | GEOMETRY        |     0
 public          | fire_dept_wvdem_092017_utm83                                    | geom              | GEOMETRY        |     0
 public          | floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83  | geom              | GEOMETRY        |     0
 public          | gbim_entities                                                   | geom              | POINT           |  4326
 public          | gbim_full_points                                                | geom              | POINT           |  4326
 public          | gbim_full_points                                                | geom_utm          | POINT           | 26917
 public          | gbim_worldview_entity                                           | centroid_geom     | POINT           | 26917
 public          | geographicalnamesonusgstopomaps_usgs_200601_ll27                | geom              | GEOMETRY        |     0
 public          | geographicalnamesonusgstopomaps_usgs_200601_utm83               | geom              | GEOMETRY        |     0
 public          | geographicnamesonusgstopomaps_current_usgs_20110801_ll83        | geom              | GEOMETRY        |     0
 public          | geographicnamesonusgstopomaps_current_usgs_20110801_utm83       | geom              | GEOMETRY        |     0
 public          | geographicnamesonusgstopomaps_historical_usgs_20110801_ll83     | geom              | GEOMETRY        |     0
 public          | geographicnamesonusgstopomaps_historical_usgs_20110801_utm83    | geom              | GEOMETRY        |     0
 public          | geographicnamesonusgstopomaps_usgs_20110801_ll83                | geom              | GEOMETRY        |     0
 public          | geographicnamesonusgstopomaps_usgs_20110801_utm83               | geom              | GEOMETRY        |     0
 public          | geolgyl_reg_ll83                                                | geom              | GEOMETRY        |     0
 public          | geolgyp_reg_ll83                                                | geom              | GEOMETRY        |     0
 public          | geospatial_census_tracts                                        | geom              | GEOMETRY        |     0
 public          | geospatial_counties                                             | geom              | GEOMETRY        |     0
 public          | geospatial_features                                             | geom              | GEOMETRY        |  4326
 public          | geospatial_utility_territories                                  | geom              | GEOMETRY        |     0
 public          | geospatial_zoning                                               | geom              | GEOMETRY        |     0
 public          | geotextl_reg_ll83                                               | geom              | GEOMETRY        |     0
 public          | glacagl_reg_ll83                                                | geom              | GEOMETRY        |     0
 public          | glacal_reg_ll83                                                 | geom              | GEOMETRY        |     0
 public          | hazardmitigationbuyout_20250929_polygons_utm83                  | geom              | GEOMETRY        |     0
 public          | hazardmitigationbuyout_20250929_polygons_wma84                  | geom              | GEOMETRY        |     0
 public          | healthruralfacilities_manysources_utm83                         | geom              | GEOMETRY        |     0
 public          | highered_wvemd_072420_utm83                                     | geom              | GEOMETRY        |     0
 public          | highered_wvemd_072420_wgc84                                     | geom              | GEOMETRY        |     0
 public          | historicalaerialphotographycountycoverage_wvgistc_utm83         | geom              | GEOMETRY        |     0
 public          | hospitals                                                       | geom              | GEOMETRY        |  4326
 public          | hospitals_wvdem_040519_gcs84                                    | geom              | GEOMETRY        |     0
 public          | hospitals_wvdem_040519_utm83                                    | geom              | GEOMETRY        |     0
 public          | hospitalswvdem040519utm83                                       | geom              | GEOMETRY        |     0
 public          | impact_reg_ll83                                                 | geom              | GEOMETRY        |     0
 public          | indexgrid15minutequads_wvgistc_ll83                             | geom              | GEOMETRY        |     0
 public          | indexgrid15minutequads_wvgistc_utm83                            | geom              | GEOMETRY        |     0
 public          | indexgrid15minutewithcounties_wvgistc_utm27                     | geom              | GEOMETRY        |     0
 public          | indexgrid1minutequads_wvgistc_ll83                              | geom              | GEOMETRY        |     0
 public          | industrialbuildings_wvdo_200807_utm83                           | geom              | GEOMETRY        |     0
 public          | industrialparks_wvdo_200078_utm83                               | geom              | GEOMETRY        |     0
 public          | industrialsites_wvdo_200807_utm83                               | geom              | GEOMETRY        |     0
 public          | inedexgrid1minutequads_wvgistc_utm83                            | geom              | GEOMETRY        |     0
 public          | intermodalterminalfacilities_usdot_1997_ll83                    | geom              | GEOMETRY        |     0
 public          | intermodalterminalfacilities_usdot_1997_utm83                   | geom              | GEOMETRY        |     0
 public          | libraries_manysources_2001_ll27                                 | geom              | GEOMETRY        |     0
 public          | libraries_manysources_2001_utm83                                | geom              | GEOMETRY        |     0
 public          | local_resources                                                 | geom              | POINT           | 26917
 public          | majorriversandlakesline_nhd_2002_ll83                           | geom              | GEOMETRY        |     0
 public          | majorriversandlakesline_nhd_2002_utm83                          | geom              | GEOMETRY        |     0
 public          | majorriversandlakespolygon_nhd_2002_poly_ll83                   | geom              | GEOMETRY        |     0
 public          | majorriversandlakespolygon_nhd_2002_utm83                       | geom              | GEOMETRY        |     0
 public          | manufacturingandbusiness_wvdo_200803_utm83                      | geom              | GEOMETRY        |     0
 public          | metfacp_reg_ll83                                                | geom              | GEOMETRY        |     0
 public          | metropolitanandmicropolitanstatisticalareas_census_2020_utm83   | geom              | GEOMETRY        |     0
 public          | metropolitanandmicropolitanstatisticalareas_census_2020_wma84   | geom              | GEOMETRY        |     0
 public          | metropolitanandmicropolitanstatisticalareascensus201111gcs83    | geom              | GEOMETRY        |     0
 public          | metropolitanandmicropolitanstatisticalareascensus201111utm83    | geom              | GEOMETRY        |     0
 public          | metropolitanstatisticalareas_uscensus_199901_ll83               | geom              | GEOMETRY        |     0
 public          | metropolitanstatisticalareas_uscensus_199901_utm83              | geom              | GEOMETRY        |     0
 public          | mineraloperations_usgs_200204_ll83                              | geom              | GEOMETRY        |     0
 public          | mineraloperations_usgs_200204_utm83                             | geom              | GEOMETRY        |     0
 public          | minesabandonedlandsline_wvdep_1996_noprojectoin                 | geom              | GEOMETRY        |     0
 public          | minesabandonedlandspoint_wvdep_1996_noprojection                | geom              | GEOMETRY        |     0
 public          | minesabandonedlandspolygon_wvdep_1996_noprojection              | geom              | GEOMETRY        |     0
 public          | mvw_gbim_landowner_spatial                                      | centroid          | GEOMETRY        |     0
 public          | mvw_gbim_landowner_spatial                                      | geom              | MULTIPOLYGON    | 26917
 public          | nationalatlasstreams_usgs_199903_ll83                           | geom              | GEOMETRY        |     0
 public          | nationalatlasstreams_usgs_199903_utm83                          | geom              | GEOMETRY        |     0
 public          | nationalregister_point_20200923                                 | geom              | GEOMETRY        |     0
 public          | nationalregister_point_20200923_utm27                           | geom              | GEOMETRY        |     0
 public          | nationalwaterwaynetwork_usarmycorpsofengineers_2001_ll83        | geom              | GEOMETRY        |     0
 public          | nationalwaterwaynetwork_usarmycorpsofengineers_2001_utm83       | geom              | GEOMETRY        |     0
 public          | nationalwaterwaynetworkports_usarmycorpsofengineers_2001_ll83   | geom              | GEOMETRY        |     0
 public          | nationalwaterwaynetworkports_usarmycorpsofengineers_2001_utm83  | geom              | GEOMETRY        |     0
 public          | naviagablewaterways_usarmycropsofengineers_2006_utm83           | geom              | GEOMETRY        |     0
 public          | navigablewaterwaysrivermiles_usarmycropsofengineers_2006_utm83  | geom              | GEOMETRY        |     0
 public          | navigablewaterwaysstructures_usarmycorpsofengineers_2006_utm83  | geom              | GEOMETRY        |     0
 public          | nursinghomes_wvdem_041219_gcs84                                 | geom              | GEOMETRY        |  4326
 public          | nursinghomes_wvdem_041219_utm83                                 | geom              | GEOMETRY        |     0
 public          | officebuildings_wvdo_200807_utm83                               | geom              | GEOMETRY        |     0
 public          | osm_clinics_wv                                                  | geom              | POINT           |  4326
 public          | osm_clinics_wv_filtered                                         | geom              | POINT           |  4326
 public          | osm_hospitals_wv                                                | geom              | POINT           |  4326
 public          | osm_nursinghomes_wv                                             | geom              | POINT           |  4326
 public          | osm_nursinghomes_wv_filtered                                    | geom              | POINT           |  4326
 public          | paroleoffices_manysources_2008_utm83                            | geom              | GEOMETRY        |     0
 public          | paroleoffices_manysources_2008_wgs84                            | geom              | GEOMETRY        |     0
 public          | placesofworship_hsip_20080723_utm83                             | geom              | GEOMETRY        |     0
 public          | placesofworship_hsip_20080723_wgs84                             | geom              | GEOMETRY        |     0
 public          | policedept_wvdem_012319_gcs84                                   | geom              | GEOMETRY        |     0
 public          | policedept_wvdem_012319_utm83                                   | geom              | GEOMETRY        |     0
 public          | populatedplaces_census_201112_utm83                             | geom              | GEOMETRY        |     0
 public          | populatedplaces_census_20112_gcs83                              | geom              | GEOMETRY        |     0
 public          | populatedplaces_census_2020_utm83                               | geom              | GEOMETRY        |     0
 public          | populatedplaces_census_2020_wma84                               | geom              | GEOMETRY        |     0
 public          | populatedplaces_uscensus_1990_ll83                              | geom              | GEOMETRY        |     0
 public          | populatedplaces_uscensus_1990_utm83                             | geom              | GEOMETRY        |     0
 public          | populationdatablockgroups_uscensus_2000_ll83                    | geom              | GEOMETRY        |     0
 public          | populationdatablockgroups_uscensus_2000_utm83                   | geom              | GEOMETRY        |     0
 public          | pow_wvgistc_062919_utm83                                        | geom              | GEOMETRY        |     0
 public          | pow_wvgistc_062919_wgs84                                        | geom              | GEOMETRY        |     0
 public          | publichealthdepts_hsip_20091229_gcs83                           | geom              | GEOMETRY        |     0
 public          | publichealthdepts_hsip_20091229_utm83                           | geom              | GEOMETRY        |     0
 public          | railnetworkregion_usdot_200203_ll83                             | geom              | GEOMETRY        |     0
 public          | railnetworkregion_usdot_200203_utm83                            | geom              | GEOMETRY        |     0
 public          | railnetworkwv_usdot_200203_ll83                                 | geom              | GEOMETRY        |     0
 public          | railnetworkwv_usdot_200203_utm83                                | geom              | GEOMETRY        |     0
 public          | railroads_rahalltransportationinstitute_2005_utm83              | geom              | GEOMETRY        |     0
 public          | realtimestreamflowstations_usgs_200012_ll27                     | geom              | GEOMETRY        |     0
 public          | realtimestreamflowstations_usgs_200012_utm27                    | geom              | GEOMETRY        |     0
 public          | realtimestreamflowstations_usgs_200012_utm83                    | geom              | GEOMETRY        |     0
 public          | recreationalwwtrails_ofwv_20151117_utm83                        | geom              | GEOMETRY        |     0
 public          | regionalplanninganddevelopmentcouncil_wvdo_1971_ll83            | geom              | GEOMETRY        |     0
 public          | regionalplanninganddevelopmentcouncil_wvdo_1971_utm83           | geom              | GEOMETRY        |     0
 public          | sewertreatmentplants_wvdep_200203_utm83                         | geom              | GEOMETRY        |     0
 public          | solidwastefacilities_wvdep_200202_ll83                          | geom              | GEOMETRY        |     0
 public          | solidwastefacilities_wvdep_200202_utm83                         | geom              | GEOMETRY        |     0
 public          | springs_wvges_1986_ll83                                         | geom              | GEOMETRY        |     0
 public          | springs_wvges_1986_utm83                                        | geom              | GEOMETRY        |     0
 public          | stateofwvhousedistricts_wvlegislativeservices_2010              | geom              | GEOMETRY        |     0
 public          | stateofwvsenatedistricts_wvlegislativeservices_2010             | geom              | GEOMETRY        |     0
 public          | states_region_ll83                                              | geom              | GEOMETRY        |     0
 public          | structurepointsnorth_samb_2003_utm83                            | geom              | GEOMETRY        |     0
 public          | structurepointssouth_samb_2003_utm83                            | geom              | GEOMETRY        |     0
 public          | structurepolygons_samb_2003_utm83                               | geom              | GEOMETRY        |     0
 public          | summits_gistc_052012_utm83_shp                                  | geom              | GEOMETRY        |     0
 public          | summits_gistc_052012_wgs84_shp                                  | geom              | GEOMETRY        |     0
 public          | surveycontrol_nationalgeodeticsurvey_102011_gcs83               | geom              | GEOMETRY        |     0
 public          | tiger_county_2022                                               | geom              | MULTIPOLYGON    |  4269
 public          | timberremovalvolume_usfs_1996_utm83                             | geom              | GEOMETRY        |     0
 public          | tl_2020_54_bg                                                   | geom              | MULTIPOLYGON    |  4269
 public          | tl_2020_54_tabblock20                                           | geom              | MULTIPOLYGON    |  4269
 public          | towers_wvpublicbroadcasting_2002_ll83                           | geom              | GEOMETRY        |     0
 public          | towers_wvpublicbroadcasting_2002_utm83                          | geom              | GEOMETRY        |     0
 public          | towersam_fcc_200202_utm83                                       | geom              | GEOMETRY        |     0
 public          | towersasr_fcc_200202_ll83                                       | geom              | GEOMETRY        |     0
 public          | towersasr_fcc_200202_utm83                                      | geom              | GEOMETRY        |     0
 public          | towerscellular_fcc_200202_ll83                                  | geom              | GEOMETRY        |     0
 public          | towerscellular_fcc_200202_utm83                                 | geom              | GEOMETRY        |     0
 public          | towersfm_fcc_200202_utm83                                       | geom              | GEOMETRY        |     0
 public          | towersmicrowave_fcc_200202_ll83                                 | geom              | GEOMETRY        |     0
 public          | towersmicrowave_fcc_200202_utm83                                | geom              | GEOMETRY        |     0
 public          | towerspager_fcc_200202_ll83                                     | geom              | GEOMETRY        |     0
 public          | towerspager_fcc_200202_utm83                                    | geom              | GEOMETRY        |     0
 public          | towersprivate_fcc_200202_ll83                                   | geom              | GEOMETRY        |     0
 public          | towersprivate_fcc_200202_utm83                                  | geom              | GEOMETRY        |     0
 public          | us_counties                                                     | geom              | MULTIPOLYGON    |  4269
 public          | us_counties_26917                                               | geom_26917        | GEOMETRY        |     0
 public          | us_counties_26917                                               | geom              | MULTIPOLYGON    |  4269
 public          | us_counties_tmp                                                 | geom              | MULTIPOLYGON    |  4269
 public          | us_zips                                                         | geom              | MULTIPOLYGON    |  4269
 public          | us_zips_26917                                                   | geom              | MULTIPOLYGON    |  4269
 public          | us_zips_26917                                                   | geom_26917        | GEOMETRY        |     0
 public          | us_zips_tmp                                                     | geom              | MULTIPOLYGON    |  4269
 public          | v_health_facilities_all                                         | geom              | GEOMETRY        |     0
 public          | v_hospitals_with_zip                                            | geom              | GEOMETRY        |  4326
 public          | veteransaffairsfacilities_manysources_200503_utm83              | geom              | GEOMETRY        |     0
 public          | veteransaffairsfacilities_manysources_200503_wgs84              | geom              | GEOMETRY        |     0
 public          | votingdistrictswv_legislativeservices_2002_ll83                 | geom              | GEOMETRY        |     0
 public          | votingdistrictswv_legislativeservices_2002_utm83                | geom              | GEOMETRY        |     0
 public          | votingdistrictswv_uscensus_2000_utm83                           | geom              | GEOMETRY        |     0
 public          | vw_appalachianbasin_from_blockgroups_wma84                      | basin_geom        | GEOMETRY        |  3395
 public          | vw_appalachianbasin_from_blocks_wma84                           | basin_geom        | GEOMETRY        |  3395
 public          | vw_appalachianbasin_services_wma84                              | geom              | GEOMETRY        |     0
 public          | vw_blockgroups2020_services_wma84                               | geom              | GEOMETRY        |     0
 public          | vw_blocks2020_services_wma84                                    | geom              | GEOMETRY        |     0
 public          | vw_building_beliefs                                             | geom              | GEOMETRY        |     0
 public          | vw_gbim_features                                                | geom              | GEOMETRY        |  4326
 public          | vw_gbim_landowner_spatial                                       | centroid          | GEOMETRY        |     0
 public          | vw_gbim_landowner_spatial                                       | geom              | MULTIPOLYGON    | 26917
 public          | vw_geospatial_features_point_centroids                          | geom              | GEOMETRY        |  4326
 public          | vw_geospatial_features_point_centroids                          | centroid_geom     | GEOMETRY        |     0
 public          | vw_local_resources                                              | geom              | POINT           | 26917
 public          | weatherstations_nationalclimatedatacenter_1999_gcs83            | geom              | GEOMETRY        |     0
 public          | weatherstations_nationalclimatedatacenter_1999_utm27            | geom              | GEOMETRY        |     0
 public          | windenergyresource_nationalrenewableenergylab_200901_utm83      | geom              | GEOMETRY        |     0
 public          | windenergyresource_nationalrenewableenergylab_200901_wgs84      | geom              | GEOMETRY        |     0
 public          | workforceinvestmentareas_wvgistc_200208_ll83                    | geom              | GEOMETRY        |     0
 public          | wv_county_bbox_geom                                             | geom_bbox         | GEOMETRY        |     0
 public          | wv_hospitals                                                    | geom              | POINT           |  4326
 public          | wv_microsoft_20180207_utm17n83                                  | geom              | GEOMETRY        |     0
 public          | wv_state_poly                                                   | geom              | GEOMETRY        |     0
 public          | wv_tax_districts_ll83                                           | geom              | GEOMETRY        |     0
 public          | wv_tax_districts_wma84                                          | geom              | GEOMETRY        |     0
 public          | wvgistc_building_footprints                                     | geom              | GEOMETRY        |     0
 public          | wvgistcbuildingfootprints                                       | geom              | GEOMETRY        |     0
 public          | wvstatebounadary100k_usgs_200203_utm83                          | geom              | GEOMETRY        |     0
 public          | wvstateboundary100k_usgs_200203_ll83                            | geom              | GEOMETRY        |     0
 public          | wvstateboundary24k_usgs_200203_ll83                             | geom              | GEOMETRY        |     0
 public          | wvstateboundary24k_usgs_200203_utm83                            | geom              | GEOMETRY        |     0
 public          | wvstatehousedistricts_manysources_1992_ll83                     | geom              | GEOMETRY        |     0
 public          | wvstatehousedistricts_manysources_1992_utm83                    | geom              | GEOMETRY        |     0
 public          | wvstatehousedistricts_manysources_2002_ll83                     | geom              | GEOMETRY        |     0
 public          | wvstatehousedistricts_manysources_2002_utm83                    | geom              | GEOMETRY        |     0
 public          | wvstatesenatedistricts_manysources_1992_ll83                    | geom              | GEOMETRY        |     0
 public          | wvstatesenatedistricts_manysources_1992_utm83                   | geom              | GEOMETRY        |     0
 public          | wvstatesenatedistricts_manysources_2002_ll83                    | geom              | GEOMETRY        |     0
 public          | wvstatesenatedistricts_manysources_2002_utm83                   | geom              | GEOMETRY        |     0
 public          | zipcodetabulationarea_census_2020_raw                           | geom              | MULTIPOLYGON    |  4269
 public          | zipcodetabulationarea_census_2020_wma84                         | geom              | MULTIPOLYGON    |  4269
 raw             | wv_tax_parcels_2025                                             | geom              | MULTIPOLYGON    | 26917
 tiger           | addrfeat                                                        | the_geom          | LINESTRING      |  4329
 tiger           | bg                                                              | the_geom          | MULTIPOLYGON    |  4269
 tiger           | county                                                          | the_geom          | MULTIPOLYGON    |  4269
 tiger           | cousub                                                          | the_geom          | MULTIPOLYGON    |  4269
 tiger           | edges                                                           | the_geom          | MULTILINESTRING |  4269
 tiger           | faces                                                           | the_geom          | MULTIPOLYGON    |  4269
 tiger           | place                                                           | the_geom          | MULTIPOLYGON    |  4269
 tiger           | state                                                           | the_geom          | MULTIPOLYGON    |  4269
 tiger           | tabblock                                                        | the_geom          | MULTIPOLYGON    |  4269
 tiger           | tabblock20                                                      | the_geom          | MULTIPOLYGON    |  4269
 tiger           | tract                                                           | the_geom          | MULTIPOLYGON    |  4269
 tiger           | zcta5                                                           | the_geom          | MULTIPOLYGON    |  4269
 trails          | trail                                                           | geom              | LINESTRING      |  4326
 trails          | waypoint                                                        | geom              | POINT           |  4326
(407 rows)


=== jarvis-local-resources-db geometry columns ===
 f_table_schema  |                          f_table_name                           | f_geometry_column |      type       | srid  
-----------------+-----------------------------------------------------------------+-------------------+-----------------+-------
 cakidd          | bldg_join__flood_structures_at_risk                             | geom              | POINT           | 26917
 cakidd          | bldg_join__nearest_hospital                                     | geom              | POINT           | 26917
 gbim            | gbim_attrs                                                      | geom              | GEOMETRY        |     0
 gbim            | gbim_attrs                                                      | bbox              | GEOMETRY        |     0
 gbim            | vw_blockgroup_infrastructure                                    | geom              | GEOMETRY        |     0
 gbim            | vw_city_emergency_coverage                                      | geom              | GEOMETRY        |     0
 gbim            | worldview_entity                                                | geom              | GEOMETRY        |     0
 gbim            | worldview_entity                                                | bbox              | GEOMETRY        |     0
 gbim_source_csv | amtrackrails_federalrailroadadministration_200210_utm83         | geom              | POINT           | 26917
 gbim_source_csv | blockgroups_census_2000_utm83                                   | geom              | POINT           | 26917
 gbim_source_csv | blockgroups_census_201111_utm83                                 | geom              | POINT           | 26917
 gbim_source_csv | blockgroups_census_2020_utm83                                   | geom              | POINT           | 26917
 gbim_source_csv | blocks_census_2020_utm83                                        | geom              | POINT           | 26917
 gbim_source_csv | boundaryappalachianbasin_wvges_1996_utm83                       | geom              | POINT           | 26917
 gbim_source_csv | citieswithpopulation_2500_census_201111_utm83                   | geom              | POINT           | 26917
 gbim_source_csv | citieswithpopulationover10k_uscensus_1990_utm83                 | geom              | POINT           | 26917
 gbim_source_csv | citieswithpopulationsover10k_census_2020_utm83                  | geom              | POINT           | 26917
 gbim_source_csv | citieswithpopulationsover2500_census_2020_utm83                 | geom              | POINT           | 26917
 gbim_source_csv | citieswithpopulatoinover2500_uscensus_1990_utm83                | geom              | POINT           | 26917
 gbim_source_csv | coals2_utm83                                                    | geom              | POINT           | 26917
 gbim_source_csv | communityboundary_min_att_20250121_utm83                        | geom              | POINT           | 26917
 gbim_source_csv | communityhealthproviders_wvhealthcareauthority_200802_utm83     | geom              | POINT           | 26917
 gbim_source_csv | correctionalinstitutions_hsip_20091230_utm83                    | geom              | POINT           | 26917
 gbim_source_csv | countycityparkboundaries_20201104_utm83                         | geom              | POINT           | 26917
 gbim_source_csv | countyseats_usgs_utm83                                          | geom              | POINT           | 26917
 gbim_source_csv | courthousescounty_manysources_200203_utm83                      | geom              | POINT           | 26917
 gbim_source_csv | cvfault_utm83                                                   | geom              | POINT           | 26917
 gbim_source_csv | cvpoly_utm83                                                    | geom              | POINT           | 26917
 gbim_source_csv | dams_usarmycorpsofengineers_200010_utm83                        | geom              | POINT           | 26917
 gbim_source_csv | damsnoncoal_usgs_2002_utm83                                     | geom              | POINT           | 26917
 gbim_source_csv | empowermentzonesandenterprisecommunities_uscensus_2002_utm83    | geom              | POINT           | 26917
 gbim_source_csv | excursionpassengertrains_wvdof_200102_utm83                     | geom              | POINT           | 26917
 gbim_source_csv | facilities_epa_200203_utm83                                     | geom              | POINT           | 26917
 gbim_source_csv | fire_dept_wvdem_092017_utm83                                    | geom              | POINT           | 26917
 gbim_source_csv | floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83  | geom              | POINT           | 26917
 gbim_source_csv | geographicalnamesonusgstopomaps_usgs_200601_utm83               | geom              | POINT           | 26917
 gbim_source_csv | geographicnamesonusgstopomaps_current_usgs_20110801_utm83       | geom              | POINT           | 26917
 gbim_source_csv | geographicnamesonusgstopomaps_historical_usgs_20110801_utm83    | geom              | POINT           | 26917
 gbim_source_csv | geographicnamesonusgstopomaps_usgs_20110801_utm83               | geom              | POINT           | 26917
 gbim_source_csv | hazardmitigationbuyout_20250929_polygons_utm83                  | geom              | POINT           | 26917
 gbim_source_csv | healthruralfacilities_manysources_utm83                         | geom              | POINT           | 26917
 gbim_source_csv | highered_wvemd_072420_utm83                                     | geom              | POINT           | 26917
 gbim_source_csv | historicalaerialphotographycountycoverage_wvgistc_utm83         | geom              | POINT           | 26917
 gbim_source_csv | hospitals_wvdem_040519_utm83                                    | geom              | POINT           | 26917
 gbim_source_csv | indexgrid15minutequads_wvgistc_utm83                            | geom              | POINT           | 26917
 gbim_source_csv | industrialbuildings_wvdo_200807_utm83                           | geom              | POINT           | 26917
 gbim_source_csv | industrialparks_wvdo_200078_utm83                               | geom              | POINT           | 26917
 gbim_source_csv | industrialsites_wvdo_200807_utm83                               | geom              | POINT           | 26917
 gbim_source_csv | inedexgrid1minutequads_wvgistc_utm83                            | geom              | POINT           | 26917
 gbim_source_csv | intermodalterminalfacilities_usdot_1997_utm83                   | geom              | POINT           | 26917
 gbim_source_csv | libraries_manysources_2001_utm83                                | geom              | POINT           | 26917
 gbim_source_csv | majorriversandlakesline_nhd_2002_utm83                          | geom              | POINT           | 26917
 gbim_source_csv | majorriversandlakespolygon_nhd_2002_utm83                       | geom              | POINT           | 26917
 gbim_source_csv | manufacturingandbusiness_wvdo_200803_utm83                      | geom              | POINT           | 26917
 gbim_source_csv | metropolitanandmicropolitanstatisticalareas_census_201111_utm83 | geom              | POINT           | 26917
 gbim_source_csv | metropolitanandmicropolitanstatisticalareas_census_2020_utm83   | geom              | POINT           | 26917
 gbim_source_csv | metropolitanstatisticalareas_uscensus_199901_utm83              | geom              | POINT           | 26917
 gbim_source_csv | mineraloperations_usgs_200204_utm83                             | geom              | POINT           | 26917
 gbim_source_csv | nationalatlasstreams_usgs_199903_utm83                          | geom              | POINT           | 26917
 gbim_source_csv | nationalwaterwaynetwork_usarmycorpsofengineers_2001_utm83       | geom              | POINT           | 26917
 gbim_source_csv | nationalwaterwaynetworkports_usarmycorpsofengineers_2001_utm83  | geom              | POINT           | 26917
 gbim_source_csv | naviagablewaterways_usarmycropsofengineers_2006_utm83           | geom              | POINT           | 26917
 gbim_source_csv | navigablewaterwaysrivermiles_usarmycropsofengineers_2006_utm83  | geom              | POINT           | 26917
 gbim_source_csv | navigablewaterwaysstructures_usarmycorpsofengineers_2006_utm83  | geom              | POINT           | 26917
 gbim_source_csv | nursinghomes_wvdem_041219_utm83                                 | geom              | POINT           | 26917
 gbim_source_csv | officebuildings_wvdo_200807_utm83                               | geom              | POINT           | 26917
 gbim_source_csv | paroleoffices_manysources_2008_utm83                            | geom              | POINT           | 26917
 gbim_source_csv | placesofworship_hsip_20080723_utm83                             | geom              | POINT           | 26917
 gbim_source_csv | policedept_wvdem_012319_utm83                                   | geom              | POINT           | 26917
 gbim_source_csv | populatedplaces_census_201112_utm83                             | geom              | POINT           | 26917
 gbim_source_csv | populatedplaces_census_2020_utm83                               | geom              | POINT           | 26917
 gbim_source_csv | populatedplaces_uscensus_1990_utm83                             | geom              | POINT           | 26917
 gbim_source_csv | populationdatablockgroups_uscensus_2000_utm83                   | geom              | POINT           | 26917
 gbim_source_csv | pow_wvgistc_062919_utm83                                        | geom              | POINT           | 26917
 gbim_source_csv | publichealthdepts_hsip_20091229_utm83                           | geom              | POINT           | 26917
 gbim_source_csv | railnetworkregion_usdot_200203_utm83                            | geom              | POINT           | 26917
 gbim_source_csv | railnetworkwv_usdot_200203_utm83                                | geom              | POINT           | 26917
 gbim_source_csv | railroads_rahalltransportationinstitute_2005_utm83              | geom              | POINT           | 26917
 gbim_source_csv | realtimestreamflowstations_usgs_200012_utm83                    | geom              | POINT           | 26917
 gbim_source_csv | recreationalwwtrails_ofwv_20151117_utm83                        | geom              | POINT           | 26917
 gbim_source_csv | regionalplanninganddevelopmentcouncil_wvdo_1971_utm83           | geom              | POINT           | 26917
 gbim_source_csv | sewertreatmentplants_wvdep_200203_utm83                         | geom              | POINT           | 26917
 gbim_source_csv | solidwastefacilities_wvdep_200202_utm83                         | geom              | POINT           | 26917
 gbim_source_csv | springs_wvges_1986_utm83                                        | geom              | POINT           | 26917
 gbim_source_csv | structurepointsnorth_samb_2003_utm83                            | geom              | POINT           | 26917
 gbim_source_csv | structurepointssouth_samb_2003_utm83                            | geom              | POINT           | 26917
 gbim_source_csv | structurepolygons_samb_2003_utm83                               | geom              | POINT           | 26917
 gbim_source_csv | timberremovalvolume_usfs_1996_utm83                             | geom              | POINT           | 26917
 gbim_source_csv | towers_wvpublicbroadcasting_2002_utm83                          | geom              | POINT           | 26917
 gbim_source_csv | towersam_fcc_200202_utm83                                       | geom              | POINT           | 26917
 gbim_source_csv | towersasr_fcc_200202_utm83                                      | geom              | POINT           | 26917
 gbim_source_csv | towerscellular_fcc_200202_utm83                                 | geom              | POINT           | 26917
 gbim_source_csv | towersfm_fcc_200202_utm83                                       | geom              | POINT           | 26917
 gbim_source_csv | towersmicrowave_fcc_200202_utm83                                | geom              | POINT           | 26917
 gbim_source_csv | towerspager_fcc_200202_utm83                                    | geom              | POINT           | 26917
 gbim_source_csv | towersprivate_fcc_200202_utm83                                  | geom              | POINT           | 26917
 gbim_source_csv | veteransaffairsfacilities_manysources_200503_utm83              | geom              | POINT           | 26917
 gbim_source_csv | votingdistrictswv_legislativeservices_2002_utm83                | geom              | POINT           | 26917
 gbim_source_csv | votingdistrictswv_uscensus_2000_utm83                           | geom              | POINT           | 26917
 gbim_source_csv | windenergyresource_nationalrenewableenergylab_200901_utm83      | geom              | POINT           | 26917
 gbim_source_csv | wv_county_boundaries_24k_topo_updated_2022_utm83                | geom              | POINT           | 26917
 gbim_source_csv | wv_tax_districts_utm83                                          | geom              | POINT           | 26917
 gbim_source_csv | wvstatebounadary100k_usgs_200203_utm83                          | geom              | POINT           | 26917
 gbim_source_csv | wvstateboundary24k_usgs_200203_utm83                            | geom              | POINT           | 26917
 gbim_source_csv | wvstatehousedistricts_manysources_1992_utm83                    | geom              | POINT           | 26917
 gbim_source_csv | wvstatehousedistricts_manysources_2002_utm83                    | geom              | POINT           | 26917
 gbim_source_csv | wvstatehousedistricts_wvlegislativeservices_2020_utm83          | geom              | POINT           | 26917
 gbim_source_csv | wvstatesenatedistricts_manysources_1992_utm83                   | geom              | POINT           | 26917
 gbim_source_csv | wvstatesenatedistricts_manysources_2002_utm83                   | geom              | POINT           | 26917
 gbim_source_csv | wvstatesenatedistricts_wvlegislativeservices_2020_utm83         | geom              | POINT           | 26917
 gbim_source_csv | zipcodetabulationarea_census_2020_utm83                         | geom              | POINT           | 26917
 public          | 911centers_wvdem_032819_gcs84                                   | geom              | GEOMETRY        |  4326
 public          | 911centers_wvdem_032819_utm83                                   | geom              | GEOMETRY        |     0
 public          | amtrackrails_federalrailroadadministration_200210_ll83          | geom              | GEOMETRY        |     0
 public          | amtrackrails_federalrailroadadministration_200210_utm83         | geom              | GEOMETRY        |     0
 public          | benefit_county_daycare                                          | geom              | POINT           | 26917
 public          | benefit_county_medicaid                                         | geom              | POINT           | 26917
 public          | benefit_county_medicare                                         | geom              | POINT           | 26917
 public          | benefit_county_section8                                         | geom              | POINT           | 26917
 public          | benefit_county_snap                                             | geom              | POINT           | 26917
 public          | benefit_county_ssi                                              | geom              | POINT           | 26917
 public          | benefit_county_tanf                                             | geom              | POINT           | 26917
 public          | benefit_county_utility20                                        | geom              | POINT           | 26917
 public          | benefit_county_wic                                              | geom              | POINT           | 26917
 public          | bldg_join__floodplainstructuresatrisk_usarmycorpsofengineers_20 | geom              | POINT           | 26917
 public          | bldg_join__hospitals                                            | geom              | POINT           | 26917
 public          | blockgroups_census_2000_ll83                                    | geom              | GEOMETRY        |     0
 public          | blockgroups_census_2000_utm83                                   | geom              | GEOMETRY        |     0
 public          | blockgroups_census_201111_gcs83                                 | geom              | GEOMETRY        |     0
 public          | blockgroups_census_201111_utm83                                 | geom              | GEOMETRY        |     0
 public          | blockgroups_census_2020_utm83                                   | geom              | GEOMETRY        | 26917
 public          | blockgroups_census_2020_utm83_full                              | geom              | GEOMETRY        |     0
 public          | blockgroups_census_2020_wma84                                   | geom              | GEOMETRY        |     0
 public          | blocks_census_2020_utm83                                        | geom              | GEOMETRY        | 26917
 public          | blocks_census_2020_utm83_full                                   | geom              | GEOMETRY        |     0
 public          | blocks_census_2020_wma84                                        | geom              | GEOMETRY        |     0
 public          | boundaryappalachianbasin_wvges_1996_utm83                       | geom              | GEOMETRY        |     0
 public          | boundaryappalachianbasin_wvges_1996_wma84                       | geom              | GEOMETRY        |  3395
 public          | bridges                                                         | geom              | GEOMETRY        |     0
 public          | building_flood_risk                                             | building_geom     | POLYGON         | 26917
 public          | building_flood_risk                                             | floodpoint_geom   | POINT           | 26917
 public          | buildings                                                       | geom              | POLYGON         | 26917
 public          | calderl_reg_ll83                                                | geom              | GEOMETRY        |     0
 public          | citieswithpopulation_2500_census_201111_gcs83                   | geom              | GEOMETRY        |     0
 public          | citieswithpopulation_2500_census_201111_utm83                   | geom              | GEOMETRY        |     0
 public          | citieswithpopulationover10k_census_201111_gcs83                 | geom              | GEOMETRY        |     0
 public          | citieswithpopulationover10k_uscensus_1990_ll83                  | geom              | GEOMETRY        |     0
 public          | citieswithpopulationover10k_uscensus_1990_utm83                 | geom              | GEOMETRY        |     0
 public          | citieswithpopulationover2500_uscensus_1990_ll83                 | geom              | GEOMETRY        |     0
 public          | citieswithpopulationsover10k_census_2020_utm83                  | geom              | GEOMETRY        |     0
 public          | citieswithpopulationsover10k_census_2020_wma84                  | geom              | GEOMETRY        |     0
 public          | citieswithpopulationsover2500_census_2020_utm83                 | geom              | GEOMETRY        |     0
 public          | citieswithpopulationsover2500_census_2020_wma84                 | geom              | GEOMETRY        |     0
 public          | citieswithpopulatoinover2500_uscensus_1990_utm83                | geom              | GEOMETRY        |     0
 public          | coals2_ll83                                                     | geom              | GEOMETRY        |     0
 public          | coals2_utm27                                                    | geom              | GEOMETRY        |     0
 public          | coals2_utm83                                                    | geom              | GEOMETRY        |     0
 public          | community_points                                                | geom              | POINT           |  4326
 public          | communityboundary_min_att_20250121_utm83                        | geom              | GEOMETRY        |     0
 public          | communityboundary_min_att_20250121_wma84                        | geom              | GEOMETRY        |     0
 public          | communityhealthproviders_wvhealthcareauthority_200802_utm83     | geom              | GEOMETRY        | 26917
 public          | correctionalinstitutions_hsip_20091230_utm83                    | geom              | GEOMETRY        |     0
 public          | correctionalinstitutions_hsip_20091230_wgs84                    | geom              | GEOMETRY        |     0
 public          | countycityparkboundaries_20201104_utm83                         | geom              | GEOMETRY        |     0
 public          | countyseats_usgs_ll83                                           | geom              | GEOMETRY        |     0
 public          | countyseats_usgs_utm83                                          | geom              | GEOMETRY        |     0
 public          | courthousescounty_manysources_200203_ll83                       | geom              | GEOMETRY        |     0
 public          | courthousescounty_manysources_200203_utm83                      | geom              | GEOMETRY        |     0
 public          | courthousesfederal_manysources_200203_ll83                      | geom              | GEOMETRY        |     0
 public          | courthousesfederal_manysources_200203_utm                       | geom              | GEOMETRY        |     0
 public          | cvfault_ll83                                                    | geom              | GEOMETRY        |     0
 public          | cvfault_utm27                                                   | geom              | GEOMETRY        |     0
 public          | cvfault_utm83                                                   | geom              | GEOMETRY        |     0
 public          | cvpoly_ll83                                                     | geom              | GEOMETRY        |     0
 public          | cvpoly_utm27                                                    | geom              | GEOMETRY        |     0
 public          | cvpoly_utm83                                                    | geom              | GEOMETRY        |     0
 public          | dams_usarmycorpsofengineers_200010_utm83                        | geom              | GEOMETRY        |     0
 public          | dams_usarmycropsofengineers_200010_ll83                         | geom              | GEOMETRY        |     0
 public          | damsnoncoal_usgs_2002_ll27                                      | geom              | GEOMETRY        |     0
 public          | damsnoncoal_usgs_2002_utm83                                     | geom              | GEOMETRY        |     0
 public          | empowermentzonesandenterprisecommunities_uscensus_2002_utm83    | geom              | GEOMETRY        |     0
 public          | empowermentzonesandenterprisecommunitiesbytractuscens30c72907   | geom              | GEOMETRY        |     0
 public          | excursionpassengertrains_wvdof_200102_ll83                      | geom              | GEOMETRY        |     0
 public          | excursionpassengertrains_wvdof_200102_utm83                     | geom              | GEOMETRY        |     0
 public          | facilities_epa_200203_ll83                                      | geom              | GEOMETRY        |     0
 public          | facilities_epa_200203_utm83                                     | geom              | GEOMETRY        |     0
 public          | fault_reg_ll83                                                  | geom              | GEOMETRY        |     0
 public          | faultgl_reg_ll83                                                | geom              | GEOMETRY        |     0
 public          | features                                                        | geom              | GEOMETRY        |     0
 public          | fire_departments                                                | geom              | GEOMETRY        |     0
 public          | fire_dept_wvdem_092017_utm83                                    | geom              | GEOMETRY        | 26917
 public          | floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83  | geom              | GEOMETRY        |     0
 public          | gbim_entities                                                   | geom              | POINT           |  4326
 public          | gbim_full_points                                                | geom              | POINT           |  4326
 public          | gbim_worldview_entity                                           | centroid_geom     | POINT           | 26917
 public          | geographicalnamesonusgstopomaps_usgs_200601_ll27                | geom              | GEOMETRY        |     0
 public          | geographicalnamesonusgstopomaps_usgs_200601_utm83               | geom              | GEOMETRY        |     0
 public          | geographicnamesonusgstopomaps_current_usgs_20110801_ll83        | geom              | GEOMETRY        |     0
 public          | geographicnamesonusgstopomaps_current_usgs_20110801_utm83       | geom              | GEOMETRY        |     0
 public          | geographicnamesonusgstopomaps_historical_usgs_20110801_ll83     | geom              | GEOMETRY        |     0
 public          | geographicnamesonusgstopomaps_historical_usgs_20110801_utm83    | geom              | GEOMETRY        |     0
 public          | geographicnamesonusgstopomaps_usgs_20110801_ll83                | geom              | GEOMETRY        |     0
 public          | geographicnamesonusgstopomaps_usgs_20110801_utm83               | geom              | GEOMETRY        |     0
 public          | geolgyl_reg_ll83                                                | geom              | GEOMETRY        |     0
 public          | geolgyp_reg_ll83                                                | geom              | GEOMETRY        |     0
 public          | geospatial_census_tracts                                        | geom              | GEOMETRY        |     0
 public          | geospatial_counties                                             | geom              | GEOMETRY        |     0
 public          | geospatial_features                                             | geom              | GEOMETRY        |  4326
 public          | geospatial_utility_territories                                  | geom              | GEOMETRY        |     0
 public          | geospatial_zoning                                               | geom              | GEOMETRY        |     0
 public          | geotextl_reg_ll83                                               | geom              | GEOMETRY        |     0
 public          | glacagl_reg_ll83                                                | geom              | GEOMETRY        |     0
 public          | glacal_reg_ll83                                                 | geom              | GEOMETRY        |     0
 public          | hazardmitigationbuyout_20250929_polygons_utm83                  | geom              | GEOMETRY        |     0
 public          | hazardmitigationbuyout_20250929_polygons_wma84                  | geom              | GEOMETRY        |  3857
 public          | healthruralfacilities_manysources_utm83                         | geom              | GEOMETRY        |     0
 public          | highered_wvemd_072420_utm83                                     | geom              | GEOMETRY        |     0
 public          | highered_wvemd_072420_wgc84                                     | geom              | GEOMETRY        |     0
 public          | historicalaerialphotographycountycoverage_wvgistc_utm83         | geom              | GEOMETRY        |     0
 public          | hospitals                                                       | geom              | GEOMETRY        |     0
 public          | hospitals_wvdem_040519_gcs84                                    | geom              | GEOMETRY        |  4326
 public          | hospitals_wvdem_040519_utm83                                    | geom              | GEOMETRY        |     0
 public          | hospitalswvdem040519utm83                                       | geom              | GEOMETRY        |     0
 public          | impact_reg_ll83                                                 | geom              | GEOMETRY        |     0
 public          | indexgrid15minutequads_wvgistc_ll83                             | geom              | GEOMETRY        |     0
 public          | indexgrid15minutequads_wvgistc_utm83                            | geom              | GEOMETRY        |     0
 public          | indexgrid15minutewithcounties_wvgistc_utm27                     | geom              | GEOMETRY        |     0
 public          | indexgrid1minutequads_wvgistc_ll83                              | geom              | GEOMETRY        |     0
 public          | industrialbuildings_wvdo_200807_utm83                           | geom              | GEOMETRY        |     0
 public          | industrialparks_wvdo_200078_utm83                               | geom              | GEOMETRY        |     0
 public          | industrialsites_wvdo_200807_utm83                               | geom              | GEOMETRY        |     0
 public          | inedexgrid1minutequads_wvgistc_utm83                            | geom              | GEOMETRY        |     0
 public          | intermodalterminalfacilities_usdot_1997_ll83                    | geom              | GEOMETRY        |     0
 public          | intermodalterminalfacilities_usdot_1997_utm83                   | geom              | GEOMETRY        |     0
 public          | libraries_manysources_2001_ll27                                 | geom              | GEOMETRY        |     0
 public          | libraries_manysources_2001_utm83                                | geom              | GEOMETRY        |     0
 public          | majorriversandlakesline_nhd_2002_ll83                           | geom              | GEOMETRY        |     0
 public          | majorriversandlakesline_nhd_2002_utm83                          | geom              | GEOMETRY        |     0
 public          | majorriversandlakespolygon_nhd_2002_poly_ll83                   | geom              | GEOMETRY        |     0
 public          | majorriversandlakespolygon_nhd_2002_utm83                       | geom              | GEOMETRY        |     0
 public          | manufacturingandbusiness_wvdo_200803_utm83                      | geom              | GEOMETRY        |     0
 public          | memories                                                        | spatial_ref       | POINT           |  4326
 public          | metfacp_reg_ll83                                                | geom              | GEOMETRY        |     0
 public          | metropolitanandmicropolitanstatisticalareas_census_2020_utm83   | geom              | GEOMETRY        |     0
 public          | metropolitanandmicropolitanstatisticalareas_census_2020_wma84   | geom              | GEOMETRY        |     0
 public          | metropolitanandmicropolitanstatisticalareascensus201111gcs83    | geom              | GEOMETRY        |     0
 public          | metropolitanandmicropolitanstatisticalareascensus201111utm83    | geom              | GEOMETRY        |     0
 public          | metropolitanstatisticalareas_uscensus_199901_ll83               | geom              | GEOMETRY        |     0
 public          | metropolitanstatisticalareas_uscensus_199901_utm83              | geom              | GEOMETRY        |     0
 public          | mineraloperations_usgs_200204_ll83                              | geom              | GEOMETRY        |     0
 public          | mineraloperations_usgs_200204_utm83                             | geom              | GEOMETRY        |     0
 public          | minesabandonedlandsline_wvdep_1996_noprojectoin                 | geom              | GEOMETRY        |     0
 public          | minesabandonedlandspoint_wvdep_1996_noprojection                | geom              | GEOMETRY        |     0
 public          | minesabandonedlandspolygon_wvdep_1996_noprojection              | geom              | GEOMETRY        |     0
 public          | mvw_gbim_landowner_spatial                                      | geom              | MULTIPOLYGON    | 26917
 public          | mvw_gbim_landowner_spatial                                      | centroid          | GEOMETRY        |     0
 public          | nationalatlasstreams_usgs_199903_ll83                           | geom              | GEOMETRY        |     0
 public          | nationalatlasstreams_usgs_199903_utm83                          | geom              | GEOMETRY        |     0
 public          | nationalregister_point_20200923                                 | geom              | GEOMETRY        |     0
 public          | nationalregister_point_20200923_utm27                           | geom              | GEOMETRY        |     0
 public          | nationalwaterwaynetwork_usarmycorpsofengineers_2001_ll83        | geom              | GEOMETRY        |     0
 public          | nationalwaterwaynetwork_usarmycorpsofengineers_2001_utm83       | geom              | GEOMETRY        |     0
 public          | nationalwaterwaynetworkports_usarmycorpsofengineers_2001_ll83   | geom              | GEOMETRY        |     0
 public          | nationalwaterwaynetworkports_usarmycorpsofengineers_2001_utm83  | geom              | GEOMETRY        |     0
 public          | naviagablewaterways_usarmycropsofengineers_2006_utm83           | geom              | GEOMETRY        |     0
 public          | navigablewaterwaysrivermiles_usarmycropsofengineers_2006_utm83  | geom              | GEOMETRY        |     0
 public          | navigablewaterwaysstructures_usarmycorpsofengineers_2006_utm83  | geom              | GEOMETRY        |     0
 public          | nursinghomes_wvdem_041219_gcs84                                 | geom              | GEOMETRY        |  4326
 public          | nursinghomes_wvdem_041219_utm83                                 | geom              | GEOMETRY        |     0
 public          | officebuildings_wvdo_200807_utm83                               | geom              | GEOMETRY        |     0
 public          | paroleoffices_manysources_2008_utm83                            | geom              | GEOMETRY        |     0
 public          | paroleoffices_manysources_2008_wgs84                            | geom              | GEOMETRY        |     0
 public          | placesofworship_hsip_20080723_utm83                             | geom              | GEOMETRY        |     0
 public          | placesofworship_hsip_20080723_wgs84                             | geom              | GEOMETRY        |     0
 public          | policedept_wvdem_012319_gcs84                                   | geom              | GEOMETRY        |  4326
 public          | policedept_wvdem_012319_utm83                                   | geom              | GEOMETRY        |     0
 public          | populatedplaces_census_201112_utm83                             | geom              | GEOMETRY        |     0
 public          | populatedplaces_census_20112_gcs83                              | geom              | GEOMETRY        |     0
 public          | populatedplaces_census_2020_utm83                               | geom              | GEOMETRY        |     0
 public          | populatedplaces_census_2020_wma84                               | geom              | GEOMETRY        |     0
 public          | populatedplaces_uscensus_1990_ll83                              | geom              | GEOMETRY        |     0
 public          | populatedplaces_uscensus_1990_utm83                             | geom              | GEOMETRY        |     0
 public          | populationdatablockgroups_uscensus_2000_ll83                    | geom              | GEOMETRY        |     0
 public          | populationdatablockgroups_uscensus_2000_utm83                   | geom              | GEOMETRY        |     0
 public          | pow_wvgistc_062919_utm83                                        | geom              | GEOMETRY        |     0
 public          | pow_wvgistc_062919_wgs84                                        | geom              | GEOMETRY        |     0
 public          | publichealthdepts_hsip_20091229_gcs83                           | geom              | GEOMETRY        |     0
 public          | publichealthdepts_hsip_20091229_utm83                           | geom              | GEOMETRY        |     0
 public          | railnetworkregion_usdot_200203_ll83                             | geom              | GEOMETRY        |     0
 public          | railnetworkregion_usdot_200203_utm83                            | geom              | GEOMETRY        |     0
 public          | railnetworkwv_usdot_200203_ll83                                 | geom              | GEOMETRY        |     0
 public          | railnetworkwv_usdot_200203_utm83                                | geom              | GEOMETRY        |     0
 public          | railroads_rahalltransportationinstitute_2005_utm83              | geom              | GEOMETRY        |     0
 public          | realtimestreamflowstations_usgs_200012_ll27                     | geom              | GEOMETRY        |     0
 public          | realtimestreamflowstations_usgs_200012_utm27                    | geom              | GEOMETRY        |     0
 public          | realtimestreamflowstations_usgs_200012_utm83                    | geom              | GEOMETRY        |     0
 public          | recreationalwwtrails_ofwv_20151117_utm83                        | geom              | GEOMETRY        |     0
 public          | regionalplanninganddevelopmentcouncil_wvdo_1971_ll83            | geom              | GEOMETRY        |     0
 public          | regionalplanninganddevelopmentcouncil_wvdo_1971_utm83           | geom              | GEOMETRY        |     0
 public          | samhsa_provider_building_join                                   | geom              | POINT           |  4326
 public          | samhsa_provider_spatial_grounded                                | geom              | POINT           |  4326
 public          | samhsa_provider_stage                                           | geom              | POINT           |  4326
 public          | sewertreatmentplants_wvdep_200203_utm83                         | geom              | GEOMETRY        |     0
 public          | solidwastefacilities_wvdep_200202_ll83                          | geom              | GEOMETRY        |     0
 public          | solidwastefacilities_wvdep_200202_utm83                         | geom              | GEOMETRY        |     0
 public          | springs_wvges_1986_ll83                                         | geom              | GEOMETRY        |     0
 public          | springs_wvges_1986_utm83                                        | geom              | GEOMETRY        |     0
 public          | stateofwvhousedistricts_wvlegislativeservices_2010              | geom              | GEOMETRY        |     0
 public          | stateofwvsenatedistricts_wvlegislativeservices_2010             | geom              | GEOMETRY        |     0
 public          | states_region_ll83                                              | geom              | GEOMETRY        |     0
 public          | structurepointsnorth_samb_2003_utm83                            | geom              | GEOMETRY        |     0
 public          | structurepointssouth_samb_2003_utm83                            | geom              | GEOMETRY        |     0
 public          | structurepolygons_samb_2003_utm83                               | geom              | GEOMETRY        |     0
 public          | summits_gistc_052012_utm83_shp                                  | geom              | GEOMETRY        |     0
 public          | summits_gistc_052012_wgs84_shp                                  | geom              | GEOMETRY        |     0
 public          | surveycontrol_nationalgeodeticsurvey_102011_gcs83               | geom              | GEOMETRY        |     0
 public          | tiger_county_2022                                               | geom              | MULTIPOLYGON    |  4269
 public          | timberremovalvolume_usfs_1996_utm83                             | geom              | GEOMETRY        |     0
 public          | tl_2020_54_bg                                                   | geom              | MULTIPOLYGON    |  4269
 public          | tl_2020_54_tabblock20                                           | geom              | MULTIPOLYGON    |  4269
 public          | towers_wvpublicbroadcasting_2002_ll83                           | geom              | GEOMETRY        |     0
 public          | towers_wvpublicbroadcasting_2002_utm83                          | geom              | GEOMETRY        |     0
 public          | towersam_fcc_200202_utm83                                       | geom              | GEOMETRY        |     0
 public          | towersasr_fcc_200202_ll83                                       | geom              | GEOMETRY        |     0
 public          | towersasr_fcc_200202_utm83                                      | geom              | GEOMETRY        |     0
 public          | towerscellular_fcc_200202_ll83                                  | geom              | GEOMETRY        |     0
 public          | towerscellular_fcc_200202_utm83                                 | geom              | GEOMETRY        |     0
 public          | towersfm_fcc_200202_utm83                                       | geom              | GEOMETRY        |     0
 public          | towersmicrowave_fcc_200202_ll83                                 | geom              | GEOMETRY        |     0
 public          | towersmicrowave_fcc_200202_utm83                                | geom              | GEOMETRY        |     0
 public          | towerspager_fcc_200202_ll83                                     | geom              | GEOMETRY        |     0
 public          | towerspager_fcc_200202_utm83                                    | geom              | GEOMETRY        |     0
 public          | towersprivate_fcc_200202_ll83                                   | geom              | GEOMETRY        |     0
 public          | towersprivate_fcc_200202_utm83                                  | geom              | GEOMETRY        |     0
 public          | us_counties                                                     | geom              | MULTIPOLYGON    |  4269
 public          | us_counties_26917                                               | geom              | MULTIPOLYGON    |  4269
 public          | us_counties_26917                                               | geom_26917        | GEOMETRY        |     0
 public          | us_counties_tmp                                                 | geom              | MULTIPOLYGON    |  4269
 public          | us_zips                                                         | geom              | MULTIPOLYGON    |  4269
 public          | us_zips_26917                                                   | geom              | MULTIPOLYGON    |  4269
 public          | us_zips_26917                                                   | geom_26917        | GEOMETRY        |     0
 public          | us_zips_tmp                                                     | geom              | MULTIPOLYGON    |  4269
 public          | veteransaffairsfacilities_manysources_200503_utm83              | geom              | GEOMETRY        |     0
 public          | veteransaffairsfacilities_manysources_200503_wgs84              | geom              | GEOMETRY        |     0
 public          | votingdistrictswv_legislativeservices_2002_ll83                 | geom              | GEOMETRY        |     0
 public          | votingdistrictswv_legislativeservices_2002_utm83                | geom              | GEOMETRY        |     0
 public          | votingdistrictswv_uscensus_2000_utm83                           | geom              | GEOMETRY        |     0
 public          | vw_appalachianbasin_from_blockgroups_wma84                      | basin_geom        | GEOMETRY        |  3395
 public          | vw_appalachianbasin_from_blocks_wma84                           | basin_geom        | GEOMETRY        |  3395
 public          | vw_appalachianbasin_services_wma84                              | geom              | GEOMETRY        |     0
 public          | vw_blockgroups2020_services_wma84                               | geom              | GEOMETRY        |     0
 public          | vw_blocks2020_services_wma84                                    | geom              | GEOMETRY        |     0
 public          | vw_building_beliefs                                             | geom              | GEOMETRY        |     0
 public          | vw_gbim_features                                                | geom              | GEOMETRY        |  4326
 public          | vw_gbim_landowner_spatial                                       | centroid          | GEOMETRY        |     0
 public          | vw_gbim_landowner_spatial                                       | geom              | MULTIPOLYGON    | 26917
 public          | vw_geospatial_features_point_centroids                          | geom              | GEOMETRY        |  4326
 public          | vw_geospatial_features_point_centroids                          | centroid_geom     | GEOMETRY        |     0
 public          | weatherstations_nationalclimatedatacenter_1999_gcs83            | geom              | GEOMETRY        |     0
 public          | weatherstations_nationalclimatedatacenter_1999_utm27            | geom              | GEOMETRY        |     0
 public          | windenergyresource_nationalrenewableenergylab_200901_utm83      | geom              | GEOMETRY        |     0
 public          | windenergyresource_nationalrenewableenergylab_200901_wgs84      | geom              | GEOMETRY        |     0
 public          | workforceinvestmentareas_wvgistc_200208_ll83                    | geom              | GEOMETRY        |     0
 public          | wv_county_bbox_geom                                             | geom_bbox         | GEOMETRY        |     0
 public          | wv_microsoft_20180207_utm17n83                                  | geom              | GEOMETRY        |     0
 public          | wv_tax_districts_ll83                                           | geom              | GEOMETRY        |     0
 public          | wv_tax_districts_wma84                                          | geom              | GEOMETRY        |     0
 public          | wvgistc_building_footprints                                     | geom              | GEOMETRY        |     0
 public          | wvgistcbuildingfootprints                                       | geom              | GEOMETRY        |     0
 public          | wvstatebounadary100k_usgs_200203_utm83                          | geom              | GEOMETRY        |     0
 public          | wvstateboundary100k_usgs_200203_ll83                            | geom              | GEOMETRY        |     0
 public          | wvstateboundary24k_usgs_200203_ll83                             | geom              | GEOMETRY        |     0
 public          | wvstateboundary24k_usgs_200203_utm83                            | geom              | GEOMETRY        |     0
 public          | wvstatehousedistricts_manysources_1992_ll83                     | geom              | GEOMETRY        |     0
 public          | wvstatehousedistricts_manysources_1992_utm83                    | geom              | GEOMETRY        |     0
 public          | wvstatehousedistricts_manysources_2002_ll83                     | geom              | GEOMETRY        |     0
 public          | wvstatehousedistricts_manysources_2002_utm83                    | geom              | GEOMETRY        |     0
 public          | wvstatesenatedistricts_manysources_1992_ll83                    | geom              | GEOMETRY        |     0
 public          | wvstatesenatedistricts_manysources_1992_utm83                   | geom              | GEOMETRY        |     0
 public          | wvstatesenatedistricts_manysources_2002_ll83                    | geom              | GEOMETRY        |     0
 public          | wvstatesenatedistricts_manysources_2002_utm83                   | geom              | GEOMETRY        |     0
 public          | zcta_centroids                                                  | centroid_geom     | GEOMETRY        |     0
 public          | zcta_polygons                                                   | geom              | MULTIPOLYGON    |  4269
 public          | zipcodetabulationarea_census_2020_raw                           | geom              | MULTIPOLYGON    |  4269
 public          | zipcodetabulationarea_census_2020_wma84                         | geom              | GEOMETRY        |     0
 raw             | wv_tax_parcels_2025                                             | geom              | MULTIPOLYGON    | 26917
 tiger           | addrfeat                                                        | the_geom          | LINESTRING      |  4269
 tiger           | bg                                                              | the_geom          | MULTIPOLYGON    |  4269
 tiger           | county                                                          | the_geom          | MULTIPOLYGON    |  4269
 tiger           | cousub                                                          | the_geom          | MULTIPOLYGON    |  4269
 tiger           | edges                                                           | the_geom          | MULTILINESTRING |  4269
 tiger           | faces                                                           | the_geom          | MULTIPOLYGON    |  4269
 tiger           | place                                                           | the_geom          | MULTIPOLYGON    |  4269
 tiger           | state                                                           | the_geom          | MULTIPOLYGON    |  4269
 tiger           | tabblock                                                        | the_geom          | MULTIPOLYGON    |  4269
 tiger           | tabblock20                                                      | the_geom          | MULTIPOLYGON    |  4269
 tiger           | tract                                                           | the_geom          | MULTIPOLYGON    |  4269
 tiger           | zcta5                                                           | the_geom          | MULTIPOLYGON    |  4269
(398 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ docker exec msjarvisgis-recovery psql -U postgres -d msjarvisgis -c "
SELECT 'local_resources' AS table_name, count(*) AS rows FROM local_resources
UNION ALL
SELECT 'resource_county_coverage', count(*) FROM resource_county_coverage
UNION ALL
SELECT 'resource_eligibility', count(*) FROM resource_eligibility
ORDER BY table_name;
"

docker exec jarvis-local-resources-db psql -U postgres -d msjarvisgis -c "
SELECT 'zcta_county_rel' AS table_name, count(*) AS rows FROM zcta_county_rel
UNION ALL
SELECT 'zcta_polygons', count(*) FROM zcta_polygons
UNION ALL
SELECT 'zcta_centroids', count(*) FROM zcta_centroids
UNION ALL
SELECT 'canonical_layers', count(*) FROM canonical_layers
ORDER BY table_name;
"
        table_name        | rows 
--------------------------+------
 local_resources          |   80
 resource_county_coverage |   20
 resource_eligibility     |   47
(3 rows)

    table_name    | rows  
------------------+-------
 canonical_layers |   338
 zcta_centroids   |   829
 zcta_county_rel  | 69934
 zcta_polygons    | 33144
(4 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ echo "=== Comparing us_zips schema between databases ==="
docker exec msjarvisgis-recovery psql -U postgres -d msjarvisgis -c "
SELECT column_name, data_type, character_maximum_length, is_nullable
FROM information_schema.columns
WHERE table_name = 'us_zips' AND table_schema = 'public'
ORDER BY ordinal_position;
"

docker exec jarvis-local-resources-db psql -U postgres -d msjarvisgis -c "
SELECT column_name, data_type, character_maximum_length, is_nullable
FROM information_schema.columns
WHERE table_name = 'us_zips' AND table_schema = 'public'
ORDER BY ordinal_position;
"
=== Comparing us_zips schema between databases ===
 column_name |  data_type   | character_maximum_length | is_nullable 
-------------+--------------+--------------------------+-------------
 gid         | integer      |                          | NO
 zip         | text         |                          | YES
 state_abbr  | text         |                          | YES
 geom        | USER-DEFINED |                          | YES
(4 rows)

 column_name |  data_type   | character_maximum_length | is_nullable 
-------------+--------------+--------------------------+-------------
 gid         | integer      |                          | NO
 zip         | text         |                          | YES
 state_abbr  | text         |                          | YES
 geom        | USER-DEFINED |                          | YES
(4 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ echo "=== Tables in msjarvisgis-recovery ==="
docker exec msjarvisgis-recovery psql -U postgres -d msjarvisgis -t -A -c "
SELECT tablename FROM pg_tables WHERE schemaname = 'public' ORDER BY tablename;
" > /tmp/tables_recovery.txt

echo "=== Tables in jarvis-local-resources-db ==="
docker exec jarvis-local-resources-db psql -U postgres -d msjarvisgis -t -A -c "
SELECT tablename FROM pg_tables WHERE schemaname = 'public' ORDER BY tablename;
" > /tmp/tables_geo.txt

echo ""
echo "=== Tables present in BOTH databases (potential duplicates) ==="
comm -12 /tmp/tables_recovery.txt /tmp/tables_geo.txt

echo ""
echo "=== Tables ONLY in msjarvisgis-recovery ==="
comm -23 /tmp/tables_recovery.txt /tmp/tables_geo.txt

echo ""
echo "=== Tables ONLY in jarvis-local-resources-db ==="
comm -13 /tmp/tables_recovery.txt /tmp/tables_geo.txt
=== Tables in msjarvisgis-recovery ===
=== Tables in jarvis-local-resources-db ===

=== Tables present in BOTH databases (potential duplicates) ===
911centers_wvdem_032819_gcs84
911centers_wvdem_032819_gcs84_attrs_raw
911centers_wvdem_032819_utm83
911centers_wvdem_032819_utm83_attrs_raw
amtrackrails_federalrailroadadministration_200210_ll83
amtrackrails_federalrailroadadministration_200210_ll83_attrs_ra
amtrackrails_federalrailroadadministration_200210_utm83
amtrackrails_federalrailroadadministration_200210_utm83_attrs_r
amtrackrails_fra_200210_ll83_attrs_raw
amtrackrails_fra_200210_utm83_attrs_raw
attrs_files_list
attrs_inventory_detailed
authority_references
benefit_case
benefit_county_daycare
benefit_county_medicaid
benefit_county_medicare
benefit_county_section8
benefit_county_snap
benefit_county_ssi
benefit_county_tanf
benefit_county_utility20
benefit_county_wic
bldg_join__floodplainstructuresatrisk_usarmycorpsofengineers_20
bldg_join__hospitals
blockgroups_census_2000_ll83
blockgroups_census_2000_ll83_attrs_raw
blockgroups_census_2000_utm83
blockgroups_census_2000_utm83_attrs_raw
blockgroups_census_201111_gcs83
blockgroups_census_201111_gcs83_attrs_raw
blockgroups_census_201111_utm83
blockgroups_census_201111_utm83_attrs_raw
blockgroups_census_2020_utm83
blockgroups_census_2020_utm83_attrs_raw
blockgroups_census_2020_utm83_full
blockgroups_census_2020_wma84
blockgroups_census_2020_wma84_attrs_raw
blocks_census_2020_utm83
blocks_census_2020_utm83_attrs_raw
blocks_census_2020_utm83_full
blocks_census_2020_wma84
blocks_census_2020_wma84_attrs_raw
boundaryappalachianbasin_wvges_1996_utm83
boundaryappalachianbasin_wvges_1996_utm83_attrs_raw
boundaryappalachianbasin_wvges_1996_wma84
bridges
bridges_attrs_raw
building_flood_risk
building_metric_stage
buildings
calderl_reg_ll83
calderl_reg_ll83_attrs_raw
citieswithpopulation_2500_census_201111_gcs83
citieswithpopulation_2500_census_201111_gcs83_attrs_raw
citieswithpopulation_2500_census_201111_utm83
citieswithpopulation_2500_census_201111_utm83_attrs_raw
citieswithpopulationover10k_census_201111_gcs83
citieswithpopulationover10k_census_201111_gcs83_attrs_raw
citieswithpopulationover10k_uscensus_1990_ll83
citieswithpopulationover10k_uscensus_1990_ll83_attrs_raw
citieswithpopulationover10k_uscensus_1990_utm83
citieswithpopulationover10k_uscensus_1990_utm83_attrs_raw
citieswithpopulationover2500_uscensus_1990_ll83
citieswithpopulationover2500_uscensus_1990_ll83_attrs_raw
citieswithpopulationsover10k_census_2020_utm83
citieswithpopulationsover10k_census_2020_utm83_attrs_raw
citieswithpopulationsover10k_census_2020_wma84
citieswithpopulationsover10k_census_2020_wma84_attrs_raw
citieswithpopulationsover2500_census_2020_utm83
citieswithpopulationsover2500_census_2020_utm83_attrs_raw
citieswithpopulationsover2500_census_2020_wma84
citieswithpopulationsover2500_census_2020_wma84_attrs_raw
citieswithpopulatoinover2500_uscensus_1990_utm83
citieswithpopulatoinover2500_uscensus_1990_utm83_attrs_raw
client_utility_account
coals2_ll83
coals2_ll83_attrs_raw
coals2_utm27
coals2_utm27_attrs_raw
coals2_utm83
coals2_utm83_attrs_raw
community_points
comm: file 1 is not in sorted order
comm: file 2 is not in sorted order
communityboundary_min_att_20250121_utm83
communityboundary_min_att_20250121_utm83_attrs_raw
communityboundary_min_att_20250121_wma84
communityboundary_min_att_20250121_wma84_attrs_raw
communityhealthproviders_wvhealthcareauthority_200802_utm83
communityhealthproviders_wvhealthcareauthority_200802_utm83_att
correctionalinstitutions_hsip_20091230_utm83
correctionalinstitutions_hsip_20091230_utm83_attrs_raw
correctionalinstitutions_hsip_20091230_wgs84
correctionalinstitutions_hsip_20091230_wgs84_attrs_raw
countycityparkboundaries_20201104_utm83
countycityparkboundaries_20201104_utm83_attrs_raw
countyseats_usgs_ll83
countyseats_usgs_ll83_attrs_raw
countyseats_usgs_utm83
countyseats_usgs_utm83_attrs_raw
courthousescounty_manysources_200203_ll83
courthousescounty_manysources_200203_ll83_attrs_raw
courthousescounty_manysources_200203_utm83
courthousescounty_manysources_200203_utm83_attrs_raw
courthousesfederal_manysources_200203_ll83
courthousesfederal_manysources_200203_ll83_attrs_raw
courthousesfederal_manysources_200203_utm
courthousesfederal_manysources_200203_utm_attrs_raw
cvfault_ll83
cvfault_ll83_attrs_raw
cvfault_utm27
cvfault_utm27_attrs_raw
cvfault_utm83
cvfault_utm83_attrs_raw
cvpoly_ll83
cvpoly_ll83_attrs_raw
cvpoly_utm27
cvpoly_utm27_attrs_raw
cvpoly_utm83
cvpoly_utm83_attrs_raw
dams_usarmycorpsofengineers_200010_utm83
dams_usarmycorpsofengineers_200010_utm83_attrs_raw
dams_usarmycropsofengineers_200010_ll83
dams_usarmycropsofengineers_200010_ll83_attrs_raw
damsnoncoal_usgs_2002_ll27
damsnoncoal_usgs_2002_ll27_attrs_raw
damsnoncoal_usgs_2002_utm83
damsnoncoal_usgs_2002_utm83_attrs_raw
empowermentzonesandenterprisecommunities_uscensus_2002_utm83
empowermentzonesandenterprisecommunities_uscensus_2002_utm83_at
empowermentzonesandenterprisecommunitiesbytractuscens30c72907
empowermentzonesandenterprisecommunitiesbytractuscens30c72907at
evidence_documents
excursionpassengertrains_wvdof_200102_ll83
excursionpassengertrains_wvdof_200102_ll83_attrs_raw
excursionpassengertrains_wvdof_200102_utm83
excursionpassengertrains_wvdof_200102_utm83_attrs_raw
facilities_epa_200203_ll83
facilities_epa_200203_ll83_attrs_raw
facilities_epa_200203_utm83
facilities_epa_200203_utm83_attrs_raw
fault_reg_ll83
fault_reg_ll83_attrs_raw
faultgl_reg_ll83
faultgl_reg_ll83_attrs_raw
features
features_attrs_raw
fire_departments
fire_departments_attrs_raw
fire_dept_wvdem_092017_utm83
fire_dept_wvdem_092017_utm83_attrs_raw
floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83
floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83_
gbim_belief
gbim_belief_edges
gbim_belief_evidence
gbim_beliefs
gbim_entities
gbim_entity_clusters
gbim_entity_land_candidates
gbim_evidence
gbim_full_points
gbim_full_points_raw
gbim_layer_catalog
gbim_layer_config
gbim_layer_manifest
gbim_source_epochs
gbim_source_tables_used
gbim_worldview_entity
gbim_worldview_entity_backup_small
gbim_worldviews
gbimbeliefnormalized
geographicalnamesonusgstopomaps_usgs_200601_ll27
geographicalnamesonusgstopomaps_usgs_200601_ll27_attrs_raw
geographicalnamesonusgstopomaps_usgs_200601_utm83
geographicalnamesonusgstopomaps_usgs_200601_utm83_attrs_raw
geographicnamesonusgstopomaps_current_usgs_20110801_ll83
geographicnamesonusgstopomaps_current_usgs_20110801_ll83_attrs_
geographicnamesonusgstopomaps_current_usgs_20110801_utm83
geographicnamesonusgstopomaps_current_usgs_20110801_utm83_attrs
geographicnamesonusgstopomaps_historical_usgs_20110801_ll83
geographicnamesonusgstopomaps_historical_usgs_20110801_ll83_att
geographicnamesonusgstopomaps_historical_usgs_20110801_utm83
geographicnamesonusgstopomaps_historical_usgs_20110801_utm83_at
geographicnamesonusgstopomaps_usgs_20110801_ll83
geographicnamesonusgstopomaps_usgs_20110801_ll83_attrs_raw
geographicnamesonusgstopomaps_usgs_20110801_utm83
geographicnamesonusgstopomaps_usgs_20110801_utm83_attrs_raw
geolgyl_reg_ll83
geolgyl_reg_ll83_attrs_raw
geolgyp_reg_ll83
geolgyp_reg_ll83_attrs_raw
geospatial_features
geospatial_layers
geotextl_reg_ll83
geotextl_reg_ll83_attrs_raw
glacagl_reg_ll83
glacagl_reg_ll83_attrs_raw
glacal_reg_ll83
glacal_reg_ll83_attrs_raw
hazardmitigationbuyout_20250929_polygons_utm83
hazardmitigationbuyout_20250929_polygons_utm83_attrs_raw
hazardmitigationbuyout_20250929_polygons_wma84
hazardmitigationbuyout_20250929_polygons_wma84_attrs_raw
healthruralfacilities_manysources_utm83
healthruralfacilities_manysources_utm83_attrs_raw
highered_wvemd_072420_utm83
highered_wvemd_072420_utm83_attrs_raw
highered_wvemd_072420_wgc84
highered_wvemd_072420_wgc84_attrs_raw
historicalaerialphotographycountycoverage_wvgistc_utm83
historicalaerialphotographycountycoverage_wvgistc_utm83_attrs_r
hospitals
hospitals_attrs_raw
hospitals_wvdem_040519_gcs84
hospitals_wvdem_040519_gcs84_attrs_raw
hospitals_wvdem_040519_utm83
hospitals_wvdem_040519_utm83_attrs_raw
hospitalswvdem040519utm83
hospitalswvdem040519utm83_attrs_raw
impact_reg_ll83
impact_reg_ll83_attrs_raw
indexgrid15minutequads_wvgistc_ll83
indexgrid15minutequads_wvgistc_ll83_attrs_raw
indexgrid15minutequads_wvgistc_utm83
indexgrid15minutequads_wvgistc_utm83_attrs_raw
indexgrid15minutewithcounties_wvgistc_utm27
indexgrid15minutewithcounties_wvgistc_utm27_attrs_raw
indexgrid1minutequads_wvgistc_ll83
indexgrid1minutequads_wvgistc_ll83_attrs_raw
industrialbuildings_wvdo_200807_utm83
industrialbuildings_wvdo_200807_utm83_attrs_raw
industrialparks_wvdo_200078_utm83
industrialparks_wvdo_200078_utm83_attrs_raw
industrialsites_wvdo_200807_utm83
industrialsites_wvdo_200807_utm83_attrs_raw
inedexgrid1minutequads_wvgistc_utm83
inedexgrid1minutequads_wvgistc_utm83_attrs_raw
intake_submissions
intermodalterminalfacilities_usdot_1997_ll83
intermodalterminalfacilities_usdot_1997_ll83_attrs_raw
intermodalterminalfacilities_usdot_1997_utm83
intermodalterminalfacilities_usdot_1997_utm83_attrs_raw
layer_config
libraries_manysources_2001_ll27
libraries_manysources_2001_ll27_attrs_raw
libraries_manysources_2001_utm83
libraries_manysources_2001_utm83_attrs_raw
local_resources
majorriversandlakesline_nhd_2002_ll83
majorriversandlakesline_nhd_2002_ll83_attrs_raw
majorriversandlakesline_nhd_2002_utm83
majorriversandlakesline_nhd_2002_utm83_attrs_raw
majorriversandlakespolygon_nhd_2002_poly_ll83
majorriversandlakespolygon_nhd_2002_poly_ll83_attrs_raw
majorriversandlakespolygon_nhd_2002_utm83
majorriversandlakespolygon_nhd_2002_utm83_attrs_raw
manufacturingandbusiness_wvdo_200803_utm83
manufacturingandbusiness_wvdo_200803_utm83_attrs_raw
metfacp_reg_ll83
metfacp_reg_ll83_attrs_raw
metropolitanandmicropolitanstatisticalareas_census_2020_utm83
metropolitanandmicropolitanstatisticalareas_census_2020_utm83_a
metropolitanandmicropolitanstatisticalareas_census_2020_wma84
metropolitanandmicropolitanstatisticalareas_census_2020_wma84_a
metropolitanandmicropolitanstatisticalareascensus201111gcs83
metropolitanandmicropolitanstatisticalareascensus201111gcs83att
metropolitanandmicropolitanstatisticalareascensus201111utm83
metropolitanandmicropolitanstatisticalareascensus201111utm83att
metropolitanstatisticalareas_uscensus_199901_ll83
metropolitanstatisticalareas_uscensus_199901_ll83_attrs_raw
metropolitanstatisticalareas_uscensus_199901_utm83
metropolitanstatisticalareas_uscensus_199901_utm83_attrs_raw
mineraloperations_usgs_200204_ll83
mineraloperations_usgs_200204_ll83_attrs_raw
mineraloperations_usgs_200204_utm83
mineraloperations_usgs_200204_utm83_attrs_raw
minesabandonedlandsline_wvdep_1996_noprojectoin
minesabandonedlandsline_wvdep_1996_noprojectoin_attrs_raw
minesabandonedlandspoint_wvdep_1996_noprojection
minesabandonedlandspoint_wvdep_1996_noprojection_attrs_raw
minesabandonedlandspolygon_wvdep_1996_noprojection
minesabandonedlandspolygon_wvdep_1996_noprojection_attrs_raw
nationalatlasstreams_usgs_199903_ll83
nationalatlasstreams_usgs_199903_ll83_attrs_raw
nationalatlasstreams_usgs_199903_utm83
nationalatlasstreams_usgs_199903_utm83_attrs_raw
nationalregister_point_20200923
nationalregister_point_20200923_attrs_raw
nationalregister_point_20200923_utm27
nationalregister_point_20200923_utm27_attrs_raw
nationalwaterwaynetwork_usarmycorpsofengineers_2001_ll83
nationalwaterwaynetwork_usarmycorpsofengineers_2001_ll83_attrs_
nationalwaterwaynetwork_usarmycorpsofengineers_2001_utm83
nationalwaterwaynetwork_usarmycorpsofengineers_2001_utm83_attrs
nationalwaterwaynetworkports_usarmycorpsofengineers_2001_ll83
nationalwaterwaynetworkports_usarmycorpsofengineers_2001_ll83_a
nationalwaterwaynetworkports_usarmycorpsofengineers_2001_utm83
nationalwaterwaynetworkports_usarmycorpsofengineers_2001_utm83_
naviagablewaterways_usarmycropsofengineers_2006_utm83
naviagablewaterways_usarmycropsofengineers_2006_utm83_attrs_raw
navigablewaterwaysrivermiles_usarmycropsofengineers_2006_utm83
navigablewaterwaysrivermiles_usarmycropsofengineers_2006_utm83_
navigablewaterwaysstructures_usarmycorpsofengineers_2006_utm83
navigablewaterwaysstructures_usarmycorpsofengineers_2006_utm83_
nursinghomes_wvdem_041219_gcs84
nursinghomes_wvdem_041219_gcs84_attrs_raw
nursinghomes_wvdem_041219_utm83
nursinghomes_wvdem_041219_utm83_attrs_raw
officebuildings_wvdo_200807_utm83
officebuildings_wvdo_200807_utm83_attrs_raw
paroleoffices_manysources_2008_utm83
paroleoffices_manysources_2008_utm83_attrs_raw
paroleoffices_manysources_2008_wgs84
paroleoffices_manysources_2008_wgs84_attrs_raw
placesofworship_hsip_20080723_utm83
placesofworship_hsip_20080723_utm83_attrs_raw
placesofworship_hsip_20080723_wgs84
placesofworship_hsip_20080723_wgs84_attrs_raw
policedept_wvdem_012319_gcs84
policedept_wvdem_012319_gcs84_attrs_raw
policedept_wvdem_012319_utm83
policedept_wvdem_012319_utm83_attrs_raw
populatedplaces_census_201112_utm83
populatedplaces_census_201112_utm83_attrs_raw
populatedplaces_census_20112_gcs83
populatedplaces_census_20112_gcs83_attrs_raw
populatedplaces_census_2020_utm83
populatedplaces_census_2020_utm83_attrs_raw
populatedplaces_census_2020_wma84
populatedplaces_census_2020_wma84_attrs_raw
populatedplaces_uscensus_1990_ll83
populatedplaces_uscensus_1990_ll83_attrs_raw
populatedplaces_uscensus_1990_utm83
populatedplaces_uscensus_1990_utm83_attrs_raw
populationdatablockgroups_uscensus_2000_ll83
populationdatablockgroups_uscensus_2000_ll83_attrs_raw
populationdatablockgroups_uscensus_2000_utm83
populationdatablockgroups_uscensus_2000_utm83_attrs_raw
pow_wvgistc_062919_utm83
pow_wvgistc_062919_utm83_attrs_raw
pow_wvgistc_062919_wgs84
pow_wvgistc_062919_wgs84_attrs_raw
program
program_authority_links
program_catalog
program_eligibility
program_entity_links
program_evidence_links
program_income_limit_rules
program_income_source_policy
program_manual_rule_links
program_name_crosswalk
program_target_config
publichealthdepts_hsip_20091229_gcs83
publichealthdepts_hsip_20091229_gcs83_attrs_raw
publichealthdepts_hsip_20091229_utm83
publichealthdepts_hsip_20091229_utm83_attrs_raw
railnetworkregion_usdot_200203_ll83
railnetworkregion_usdot_200203_ll83_attrs_raw
railnetworkregion_usdot_200203_utm83
railnetworkregion_usdot_200203_utm83_attrs_raw
railnetworkwv_usdot_200203_ll83
railnetworkwv_usdot_200203_ll83_attrs_raw
railnetworkwv_usdot_200203_utm83
railnetworkwv_usdot_200203_utm83_attrs_raw
railroads_rahalltransportationinstitute_2005_utm83
railroads_rahalltransportationinstitute_2005_utm83_attrs_raw
realtimestreamflowstations_usgs_200012_ll27
realtimestreamflowstations_usgs_200012_ll27_attrs_raw
realtimestreamflowstations_usgs_200012_utm27
realtimestreamflowstations_usgs_200012_utm27_attrs_raw
realtimestreamflowstations_usgs_200012_utm83
realtimestreamflowstations_usgs_200012_utm83_attrs_raw
recreationalwwtrails_ofwv_20151117_utm83
recreationalwwtrails_ofwv_20151117_utm83_attrs_raw
regionalplanninganddevelopmentcouncil_wvdo_1971_ll83
regionalplanninganddevelopmentcouncil_wvdo_1971_ll83_attrs_raw
regionalplanninganddevelopmentcouncil_wvdo_1971_utm83
regionalplanninganddevelopmentcouncil_wvdo_1971_utm83_attrs_raw
resource_county_coverage
resource_eligibility
sewertreatmentplants_wvdep_200203_utm83
sewertreatmentplants_wvdep_200203_utm83_attrs_raw
solidwastefacilities_wvdep_200202_ll83
solidwastefacilities_wvdep_200202_ll83_attrs_raw
solidwastefacilities_wvdep_200202_utm83
solidwastefacilities_wvdep_200202_utm83_attrs_raw
spatial_ref_sys
springs_wvges_1986_ll83
springs_wvges_1986_ll83_attrs_raw
springs_wvges_1986_utm83
springs_wvges_1986_utm83_attrs_raw
stateofwvhousedistricts_wvlegislativeservices_2010
stateofwvhousedistricts_wvlegislativeservices_2010_attrs_raw
stateofwvsenatedistricts_wvlegislativeservices_2010
stateofwvsenatedistricts_wvlegislativeservices_2010_attrs_raw
states_region_ll83
states_region_ll83_attrs_raw
structurepointsnorth_samb_2003_utm83
structurepointsnorth_samb_2003_utm83_attrs_raw
structurepointssouth_samb_2003_utm83
structurepointssouth_samb_2003_utm83_attrs_raw
structurepolygons_samb_2003_utm83
structurepolygons_samb_2003_utm83_attrs_raw
summits_gistc_052012_utm83_shp
summits_gistc_052012_utm83_shp_attrs_raw
summits_gistc_052012_wgs84_shp
summits_gistc_052012_wgs84_shp_attrs_raw
surveycontrol_nationalgeodeticsurvey_102011_gcs83
surveycontrol_nationalgeodeticsurvey_102011_gcs83_attrs_raw
tiger_county_2022
timberremovalvolume_usfs_1996_utm83
timberremovalvolume_usfs_1996_utm83_attrs_raw
tl_2020_54_bg
tl_2020_54_tabblock20
tmp_building_block_nearest_sample
towers_wvpublicbroadcasting_2002_ll83
towers_wvpublicbroadcasting_2002_ll83_attrs_raw
towers_wvpublicbroadcasting_2002_utm83
towers_wvpublicbroadcasting_2002_utm83_attrs_raw
towersam_fcc_200202_utm83
towersam_fcc_200202_utm83_attrs_raw
towersasr_fcc_200202_ll83
towersasr_fcc_200202_ll83_attrs_raw
towersasr_fcc_200202_utm83
towersasr_fcc_200202_utm83_attrs_raw
towerscellular_fcc_200202_ll83
towerscellular_fcc_200202_ll83_attrs_raw
towerscellular_fcc_200202_utm83
towerscellular_fcc_200202_utm83_attrs_raw
towersfm_fcc_200202_utm83
towersfm_fcc_200202_utm83_attrs_raw
towersmicrowave_fcc_200202_ll83
towersmicrowave_fcc_200202_ll83_attrs_raw
towersmicrowave_fcc_200202_utm83
towersmicrowave_fcc_200202_utm83_attrs_raw
towerspager_fcc_200202_ll83
towerspager_fcc_200202_ll83_attrs_raw
towerspager_fcc_200202_utm83
towerspager_fcc_200202_utm83_attrs_raw
towersprivate_fcc_200202_ll83
towersprivate_fcc_200202_ll83_attrs_raw
towersprivate_fcc_200202_utm83
towersprivate_fcc_200202_utm83_attrs_raw
uei_registry
us_counties
us_counties_tmp
us_zips
us_zips_tmp
user_compliance_task
utility_discount_enrollment
veteransaffairsfacilities_manysources_200503_utm83
veteransaffairsfacilities_manysources_200503_utm83_attrs_raw
veteransaffairsfacilities_manysources_200503_wgs84
veteransaffairsfacilities_manysources_200503_wgs84_attrs_raw
votingdistrictswv_legislativeservices_2002_ll83
votingdistrictswv_legislativeservices_2002_ll83_attrs_raw
votingdistrictswv_legislativeservices_2002_utm83
votingdistrictswv_legislativeservices_2002_utm83_attrs_raw
votingdistrictswv_uscensus_2000_utm83
votingdistrictswv_uscensus_2000_utm83_attrs_raw
weatherstations_nationalclimatedatacenter_1999_gcs83
weatherstations_nationalclimatedatacenter_1999_gcs83_attrs_raw
weatherstations_nationalclimatedatacenter_1999_utm27
weatherstations_nationalclimatedatacenter_1999_utm27_attrs_raw
windenergyresource_nationalrenewableenergylab_200901_utm83
windenergyresource_nationalrenewableenergylab_200901_utm83_attr
windenergyresource_nationalrenewableenergylab_200901_wgs84
windenergyresource_nationalrenewableenergylab_200901_wgs84_attr
workforceinvestmentareas_wvgistc_200208_ll83
workforceinvestmentareas_wvgistc_200208_ll83_attrs_raw
wv_county_bbox_geom
wv_county_boundaries_24k_topo_updated_2022_utm83_attrs_raw
wv_county_names
wv_income_manual_income_limits
wv_income_manual_income_sources
wv_income_manual_income_treatment
wv_income_manual_income_treatment_extended
wv_income_manual_rules
wv_microsoft_20180207_utm17n83
wv_microsoft_20180207_utm17n83_attrs_raw
wv_tax_districts_ll83
wv_tax_districts_ll83_attrs_raw
wv_tax_districts_utm83_attrs_raw
wv_tax_districts_wma84
wv_tax_districts_wma84_attrs_raw
zcta_county_rel
zipcodetabulationarea_census_2020_raw
zipcodetabulationarea_census_2020_utm83_attrs_raw
zipcodetabulationarea_census_2020_wma84
zipcodetabulationarea_census_2020_wma84_attrs_raw
comm: input is not in sorted order

=== Tables ONLY in msjarvisgis-recovery ===
comm: file 1 is not in sorted order
comm: file 2 is not in sorted order
ms_jarvis_learning_log
osm_clinics_wv
osm_clinics_wv_filtered
osm_hospitals_wv
osm_nursinghomes_wv
osm_nursinghomes_wv_filtered
rural_health_attrs_staging
wv_hospitals
wv_state_poly
wvgistc_building_footprints
wvgistc_building_footprints_attrs_raw
wvgistcbuildingfootprints
wvgistcbuildingfootprints_attrs_raw
wvgistcbuildingfootprintsattrsraw
wvstatebounadary100k_usgs_200203_utm83
wvstatebounadary100k_usgs_200203_utm83_attrs_raw
wvstateboundary100k_usgs_200203_ll83
wvstateboundary100k_usgs_200203_ll83_attrs_raw
wvstateboundary24k_usgs_200203_ll83
wvstateboundary24k_usgs_200203_ll83_attrs_raw
wvstateboundary24k_usgs_200203_utm83
wvstateboundary24k_usgs_200203_utm83_attrs_raw
wvstatehousedistricts_manysources_1992_ll83
wvstatehousedistricts_manysources_1992_ll83_attrs_raw
wvstatehousedistricts_manysources_1992_utm83
wvstatehousedistricts_manysources_1992_utm83_attrs_raw
wvstatehousedistricts_manysources_2002_ll83
wvstatehousedistricts_manysources_2002_ll83_attrs_raw
wvstatehousedistricts_manysources_2002_utm83
wvstatehousedistricts_manysources_2002_utm83_attrs_raw
wvstatehousedistricts_wvlegislativeservices_2020_utm83_attrs_ra
wvstatesenatedistricts_manysources_1992_ll83
wvstatesenatedistricts_manysources_1992_ll83_attrs_raw
wvstatesenatedistricts_manysources_1992_utm83
wvstatesenatedistricts_manysources_1992_utm83_attrs_raw
wvstatesenatedistricts_manysources_2002_ll83
wvstatesenatedistricts_manysources_2002_ll83_attrs_raw
wvstatesenatedistricts_manysources_2002_utm83
wvstatesenatedistricts_manysources_2002_utm83_attrs_raw
wvstatesenatedistricts_wvlegislativeservices_2020_utm83_attrs_r
comm: input is not in sorted order

=== Tables ONLY in jarvis-local-resources-db ===
canonical_layers
comm: file 1 is not in sorted order
comm: file 2 is not in sorted order
confidence_decay
fayette_fire_stations
fayette_parcels
local_resources_index
memories
samhsa_provider_building_join
samhsa_provider_spatial_grounded
samhsa_provider_stage
spatial_role_scopes
wv_zip_zcta_raw
wvgistc_building_footprints
wvgistc_building_footprints_attrs_raw
wvgistcbuildingfootprints
wvgistcbuildingfootprints_attrs_raw
wvgistcbuildingfootprintsattrsraw
wvstatebounadary100k_usgs_200203_utm83
wvstatebounadary100k_usgs_200203_utm83_attrs_raw
wvstateboundary100k_usgs_200203_ll83
wvstateboundary100k_usgs_200203_ll83_attrs_raw
wvstateboundary24k_usgs_200203_ll83
wvstateboundary24k_usgs_200203_ll83_attrs_raw
wvstateboundary24k_usgs_200203_utm83
wvstateboundary24k_usgs_200203_utm83_attrs_raw
wvstatehousedistricts_manysources_1992_ll83
wvstatehousedistricts_manysources_1992_ll83_attrs_raw
wvstatehousedistricts_manysources_1992_utm83
wvstatehousedistricts_manysources_1992_utm83_attrs_raw
wvstatehousedistricts_manysources_2002_ll83
wvstatehousedistricts_manysources_2002_ll83_attrs_raw
wvstatehousedistricts_manysources_2002_utm83
wvstatehousedistricts_manysources_2002_utm83_attrs_raw
wvstatehousedistricts_wvlegislativeservices_2020_utm83_attrs_ra
wvstatesenatedistricts_manysources_1992_ll83
wvstatesenatedistricts_manysources_1992_ll83_attrs_raw
wvstatesenatedistricts_manysources_1992_utm83
wvstatesenatedistricts_manysources_1992_utm83_attrs_raw
wvstatesenatedistricts_manysources_2002_ll83
wvstatesenatedistricts_manysources_2002_ll83_attrs_raw
wvstatesenatedistricts_manysources_2002_utm83
wvstatesenatedistricts_manysources_2002_utm83_attrs_raw
wvstatesenatedistricts_wvlegislativeservices_2020_utm83_attrs_r
zcta_polygons
comm: input is not in sorted order
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ echo "=== Foreign keys in msjarvisgis-recovery ==="
docker exec msjarvisgis-recovery psql -U postgres -d msjarvisgis -c "
SELECT
    tc.table_name, 
    kcu.column_name, 
    ccu.table_name AS foreign_table_name,
    ccu.column_name AS foreign_column_name 
FROM information_schema.table_constraints AS tc 
JOIN information_schema.key_column_usage AS kcu
  ON tc.constraint_name = kcu.constraint_name
JOIN information_schema.constraint_column_usage AS ccu
  ON ccu.constraint_name = tc.constraint_name
WHERE tc.constraint_type = 'FOREIGN KEY' AND tc.table_schema = 'public'
ORDER BY tc.table_name, kcu.column_name;
"

echo ""
echo "=== Foreign keys in jarvis-local-resources-db ==="
docker exec jarvis-local-resources-db psql -U postgres -d msjarvisgis -c "
SELECT
    tc.table_name, 
    kcu.column_name, 
    ccu.table_name AS foreign_table_name,
    ccu.column_name AS foreign_column_name 
FROM information_schema.table_constraints AS tc 
JOIN information_schema.key_column_usage AS kcu
  ON tc.constraint_name = kcu.constraint_name
"RDER BY tc.table_name, kcu.column_name; AND tc.table_schema = 'public'
=== Foreign keys in msjarvisgis-recovery ===
            table_name             |     column_name     |       foreign_table_name        | foreign_column_name 
-----------------------------------+---------------------+---------------------------------+---------------------
 gbim_belief                       | gbim_entity_id      | gbim_worldview_entity           | id
 gbim_belief_edges                 | source_belief_id    | gbim_beliefs                    | belief_id
 gbim_belief_edges                 | target_belief_id    | gbim_beliefs                    | belief_id
 gbim_belief_edges                 | target_worldview_id | gbim_worldviews                 | worldview_id
 gbim_belief_evidence              | belief_id           | gbim_beliefs                    | belief_id
 gbim_belief_evidence              | evidence_id         | gbim_evidence                   | evidence_id
 gbim_beliefs                      | worldview_id        | gbim_worldviews                 | worldview_id
 gbim_beliefs                      | worldview_id        | gbim_worldviews                 | worldview_id
 gbim_beliefs                      | worldview_id        | gbim_worldviews                 | worldview_id
 gbim_beliefs                      | worldview_id        | gbim_worldviews                 | worldview_id
 intake_submissions                | reviewed_by         | uei_registry                    | uei
 intake_submissions                | submitted_by        | uei_registry                    | uei
 program_authority_links           | authority_id        | authority_references            | authority_id
 program_authority_links           | program_id          | program_catalog                 | program_id
 program_entity_links              | entity_id           | gbim_worldview_entity           | id
 program_entity_links              | program_id          | program_catalog                 | program_id
 program_evidence_links            | doc_id              | evidence_documents              | doc_id
 program_evidence_links            | program_id          | program_catalog                 | program_id
 program_income_limit_rules        | income_rule_id      | wv_income_manual_income_limits  | rule_id
 program_income_limit_rules        | program_id          | program_catalog                 | program_id
 program_income_source_policy      | program_id          | program                         | program_id
 program_manual_rule_links         | program_id          | program_catalog                 | program_id
 program_manual_rule_links         | rule_id             | wv_income_manual_rules          | rule_id
 program_target_config             | program_id          | program_catalog                 | program_id
 resource_county_coverage          | resource_id         | local_resources                 | id
 resource_eligibility              | resource_id         | local_resources                 | id
 user_compliance_task              | enrollment_id       | utility_discount_enrollment     | enrollment_id
 utility_discount_enrollment       | program_id          | program                         | program_id
 wv_income_manual_income_treatment | source_code         | wv_income_manual_income_sources | source_code
(29 rows)


=== Foreign keys in jarvis-local-resources-db ===
            table_name             |     column_name     |       foreign_table_name        | foreign_column_name 
-----------------------------------+---------------------+---------------------------------+---------------------
 gbim_belief                       | gbim_entity_id      | gbim_worldview_entity           | id
 gbim_belief_edges                 | source_belief_id    | gbim_beliefs                    | belief_id
 gbim_belief_edges                 | target_belief_id    | gbim_beliefs                    | belief_id
 gbim_belief_edges                 | target_worldview_id | gbim_worldviews                 | worldview_id
 gbim_belief_evidence              | belief_id           | gbim_beliefs                    | belief_id
 gbim_belief_evidence              | evidence_id         | gbim_evidence                   | evidence_id
 gbim_beliefs                      | worldview_id        | gbim_worldviews                 | worldview_id
 gbim_beliefs                      | worldview_id        | gbim_worldviews                 | worldview_id
 gbim_beliefs                      | worldview_id        | gbim_worldviews                 | worldview_id
 gbim_beliefs                      | worldview_id        | gbim_worldviews                 | worldview_id
 program_authority_links           | authority_id        | authority_references            | authority_id
 program_authority_links           | program_id          | program_catalog                 | program_id
 program_entity_links              | entity_id           | gbim_worldview_entity           | id
 program_entity_links              | program_id          | program_catalog                 | program_id
 program_evidence_links            | doc_id              | evidence_documents              | doc_id
 program_evidence_links            | program_id          | program_catalog                 | program_id
 program_income_limit_rules        | income_rule_id      | wv_income_manual_income_limits  | rule_id
 program_income_limit_rules        | program_id          | program_catalog                 | program_id
 program_income_source_policy      | program_id          | program                         | program_id
 program_manual_rule_links         | program_id          | program_catalog                 | program_id
 program_manual_rule_links         | rule_id             | wv_income_manual_rules          | rule_id
 program_target_config             | program_id          | program_catalog                 | program_id
 user_compliance_task              | enrollment_id       | utility_discount_enrollment     | enrollment_id
 utility_discount_enrollment       | program_id          | program                         | program_id
 wv_income_manual_income_treatment | source_code         | wv_income_manual_income_sources | source_code
(25 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ docker exec msjarvisgis-recovery psql -U postgres -d msjarvisgis -c "
SELECT 
    count(*) AS total_rows,
    count(CASE WHEN county IS NULL THEN 1 END) AS null_county,
    count(CASE WHEN zip_coverage IS NULL THEN 1 END) AS null_zip_coverage,
    count(CASE WHEN name IS NULL THEN 1 END) AS null_name
FROM local_resources;
"

docker exec jarvis-local-resources-db psql -U postgres -d msjarvisgis -c "
SELECT 
    count(*) AS total_rows,
    count(CASE WHEN county_name IS NULL THEN 1 END) AS null_county_name,
    count(CASE WHEN geoid_zcta5 IS NULL THEN 1 END) AS null_geoid_zcta5,
    count(CASE WHEN statefp IS NULL THEN 1 END) AS null_statefp
FROM zcta_county_rel;
"
 total_rows | null_county | null_zip_coverage | null_name 
------------+-------------+-------------------+-----------
         80 |           0 |                 0 |         0
(1 row)

 total_rows | null_county_name | null_geoid_zcta5 | null_statefp 
------------+------------------+------------------+--------------
      69934 |                0 |                0 |            0
(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ echo "=== SRID usage in jarvis-local-resources-db ==="
docker exec jarvis-local-resources-db psql -U postgres -d msjarvisgis -c "
SELECT DISTINCT srid, count(*) AS tables_using_srid
FROM geometry_columns
GROUP BY srid
ORDER BY srid;
" 2>/dev/null || echo "No geometry columns found"
=== SRID usage in jarvis-local-resources-db ===
 srid  | tables_using_srid 
-------+-------------------
     0 |               230
  3395 |                 3
  3857 |                 1
  4269 |                23
  4326 |                14
 26917 |               127
(6 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ mkdir -p output/migration-validation

docker exec msjarvisgis-recovery psql -U postgres -d msjarvisgis -c "\copy (
  SELECT * FROM local_resources ORDER BY id LIMIT 5
) TO '/tmp/local_resources_sample.csv' WITH CSV HEADER"
docker cp msjarvisgis-recovery:/tmp/local_resources_sample.csv output/migration-validation/

docker exec jarvis-local-resources-db psql -U postgres -d msjarvisgis -c "\copy (
  SELECT * FROM zcta_county_rel WHERE statefp = '54' ORDER BY geoid_zcta5 LIMIT 5
) TO '/tmp/zcta_county_rel_sample.csv' WITH CSV HEADER"
docker cp jarvis-local-resources-db:/tmp/zcta_county_rel_sample.csv output/migration-validation/

ls -lh output/migration-validation/
COPY 5
Successfully copied 9.22kB to /home/cakidd/msjarvis-rebuild-working/msjarvis-rebuild/output/migration-validation/
COPY 5
Successfully copied 2.05kB to /home/cakidd/msjarvis-rebuild-working/msjarvis-rebuild/output/migration-validation/
total 12K
-rw-r--r-- 1 cakidd cakidd 7.4K May  3 13:34 local_resources_sample.csv
-rw-r--r-- 1 cakidd cakidd  214 May  3 13:34 zcta_county_rel_sample.csv
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ echo "=== Test query: ZIP to county lookup ==="
docker exec jarvis-local-resources-db psql -U postgres -d msjarvisgis -c "
SELECT geoid_zcta5, county_name, statefp, overlap_pct
FROM zcta_county_rel
WHERE geoid_zcta5 IN ('25840', '25901', '25177')
  AND statefp = '54'
ORDER BY geoid_zcta5, overlap_pct DESC;
"

echo ""
echo "=== Test query: Resources by county ==="
docker exec msjarvisgis-recovery psql -U postgres -d msjarvisgis -c "
SELECT county, count(*) AS resources
FROM local_resources
GROUP BY county
ORDER BY county;
"
=== Test query: ZIP to county lookup ===
 geoid_zcta5 | county_name | statefp |      overlap_pct      
-------------+-------------+---------+-----------------------
 25177       | Kanawha     | 54      |    0.9966391552859295
 25177       | Putnam      | 54      | 0.0033608447140705475
 25177       | Lincoln     | 54      |                     0
 25840       | Fayette     | 54      |    0.9999999999999997
 25901       | Fayette     | 54      |     0.999999999999997
 25901       | Raleigh     | 54      |                     0
(6 rows)


=== Test query: Resources by county ===
 county  | resources 
---------+-----------
 Fayette |        66
 Kanawha |        12
 Logan   |         2
(3 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ echo "=== Database sizes in msjarvisgis-recovery ==="
docker exec msjarvisgis-recovery psql -U postgres -c "
SELECT datname, pg_size_pretty(pg_database_size(datname)) AS size
FROM pg_database
WHERE datname NOT IN ('template0', 'template1')
ORDER BY pg_database_size(datname) DESC;
"

echo ""
echo "=== Database sizes in jarvis-local-resources-db ==="
docker exec jarvis-local-resources-db psql -U postgres -c "
SELECT datname, pg_size_pretty(pg_database_size(datname)) AS size
FROM pg_database
WHERE datname NOT IN ('template0', 'template1')
ORDER BY pg_database_size(datname) DESC;
"
=== Database sizes in msjarvisgis-recovery ===
   datname   |  size   
-------------+---------
 msjarvisgis | 45 GB
 postgres    | 7487 kB
(2 rows)


=== Database sizes in jarvis-local-resources-db ===
     datname      | size  
------------------+-------
 msjarvisgis      | 94 GB
 local_resources  | 13 GB
 postgres         | 19 MB
 template_postgis | 19 MB
(4 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ echo "=== Indexes in msjarvisgis-recovery ==="
docker exec msjarvisgis-recovery psql -U postgres -d msjarvisgis -c "
SELECT tablename, indexname, indexdef
FROM pg_indexes
WHERE schemaname = 'public'
ORDER BY tablename, indexname;
"

echo ""
echo "=== Indexes in jarvis-local-resources-db ==="
docker exec jarvis-local-resources-db psql -U postgres -d msjarvisgis -c "
SELECT tablename, indexname, indexdef
FROM pg_indexes
WHERE schemaname = 'public'
ORDER BY tablename, indexname;
"
=== Indexes in msjarvisgis-recovery ===
                 tablename                  |                            indexname                            |                                                                                         indexdef                                                                                         
--------------------------------------------+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 attrs_files_list                           | attrs_files_list_pkey                                           | CREATE UNIQUE INDEX attrs_files_list_pkey ON public.attrs_files_list USING btree (id)
 attrs_inventory_detailed                   | attrs_inventory_detailed_pkey                                   | CREATE UNIQUE INDEX attrs_inventory_detailed_pkey ON public.attrs_inventory_detailed USING btree (id)
 authority_references                       | authority_references_pkey                                       | CREATE UNIQUE INDEX authority_references_pkey ON public.authority_references USING btree (authority_id)
 benefit_case                               | benefit_case_pkey                                               | CREATE UNIQUE INDEX benefit_case_pkey ON public.benefit_case USING btree (case_id)
 benefit_county_daycare                     | benefit_county_daycare_geom_idx                                 | CREATE INDEX benefit_county_daycare_geom_idx ON public.benefit_county_daycare USING gist (geom)
 benefit_county_daycare                     | benefit_county_daycare_pkey                                     | CREATE UNIQUE INDEX benefit_county_daycare_pkey ON public.benefit_county_daycare USING btree (id)
 benefit_county_medicaid                    | benefit_county_medicaid_geom_idx                                | CREATE INDEX benefit_county_medicaid_geom_idx ON public.benefit_county_medicaid USING gist (geom)
 benefit_county_medicaid                    | benefit_county_medicaid_pkey                                    | CREATE UNIQUE INDEX benefit_county_medicaid_pkey ON public.benefit_county_medicaid USING btree (id)
 benefit_county_medicare                    | benefit_county_medicare_geom_idx                                | CREATE INDEX benefit_county_medicare_geom_idx ON public.benefit_county_medicare USING gist (geom)
 benefit_county_medicare                    | benefit_county_medicare_pkey                                    | CREATE UNIQUE INDEX benefit_county_medicare_pkey ON public.benefit_county_medicare USING btree (id)
 benefit_county_section8                    | benefit_county_section8_geom_idx                                | CREATE INDEX benefit_county_section8_geom_idx ON public.benefit_county_section8 USING gist (geom)
 benefit_county_section8                    | benefit_county_section8_pkey                                    | CREATE UNIQUE INDEX benefit_county_section8_pkey ON public.benefit_county_section8 USING btree (id)
 benefit_county_snap                        | benefit_county_snap_geom_idx                                    | CREATE INDEX benefit_county_snap_geom_idx ON public.benefit_county_snap USING gist (geom)
 benefit_county_snap                        | benefit_county_snap_pkey                                        | CREATE UNIQUE INDEX benefit_county_snap_pkey ON public.benefit_county_snap USING btree (id)
 benefit_county_ssi                         | benefit_county_ssi_geom_idx                                     | CREATE INDEX benefit_county_ssi_geom_idx ON public.benefit_county_ssi USING gist (geom)
 benefit_county_ssi                         | benefit_county_ssi_pkey                                         | CREATE UNIQUE INDEX benefit_county_ssi_pkey ON public.benefit_county_ssi USING btree (id)
 benefit_county_tanf                        | benefit_county_tanf_geom_idx                                    | CREATE INDEX benefit_county_tanf_geom_idx ON public.benefit_county_tanf USING gist (geom)
 benefit_county_tanf                        | benefit_county_tanf_pkey                                        | CREATE UNIQUE INDEX benefit_county_tanf_pkey ON public.benefit_county_tanf USING btree (id)
 benefit_county_utility20                   | benefit_county_utility20_geom_idx                               | CREATE INDEX benefit_county_utility20_geom_idx ON public.benefit_county_utility20 USING gist (geom)
 benefit_county_utility20                   | benefit_county_utility20_pkey                                   | CREATE UNIQUE INDEX benefit_county_utility20_pkey ON public.benefit_county_utility20 USING btree (id)
 benefit_county_wic                         | benefit_county_wic_geom_idx                                     | CREATE INDEX benefit_county_wic_geom_idx ON public.benefit_county_wic USING gist (geom)
 benefit_county_wic                         | benefit_county_wic_pkey                                         | CREATE UNIQUE INDEX benefit_county_wic_pkey ON public.benefit_county_wic USING btree (id)
 blockgroups_census_2020_utm83_full         | blockgroups_2020_full_geom_gix                                  | CREATE INDEX blockgroups_2020_full_geom_gix ON public.blockgroups_census_2020_utm83_full USING gist (geom)
 blocks_census_2020_utm83_full              | blocks_2020_full_geom_gix                                       | CREATE INDEX blocks_2020_full_geom_gix ON public.blocks_census_2020_utm83_full USING gist (geom)
 building_metric_stage                      | building_metric_stage_pkey                                      | CREATE UNIQUE INDEX building_metric_stage_pkey ON public.building_metric_stage USING btree (geodb_id)
 buildings                                  | buildings_geom_idx                                              | CREATE INDEX buildings_geom_idx ON public.buildings USING gist (geom)
 buildings                                  | buildings_pkey                                                  | CREATE UNIQUE INDEX buildings_pkey ON public.buildings USING btree (building_id)
 client_utility_account                     | client_utility_account_pkey                                     | CREATE UNIQUE INDEX client_utility_account_pkey ON public.client_utility_account USING btree (client_id, utility_account_number, utility_type)
 community_points                           | community_points_pkey                                           | CREATE UNIQUE INDEX community_points_pkey ON public.community_points USING btree (point_id)
 community_points                           | community_points_program_id_key                                 | CREATE UNIQUE INDEX community_points_program_id_key ON public.community_points USING btree (program_id)
 community_points                           | idx_cpts_geom                                                   | CREATE INDEX idx_cpts_geom ON public.community_points USING gist (geom)
 community_points                           | idx_cpts_zip                                                    | CREATE INDEX idx_cpts_zip ON public.community_points USING btree (zip_code)
 evidence_documents                         | evidence_documents_pkey                                         | CREATE UNIQUE INDEX evidence_documents_pkey ON public.evidence_documents USING btree (doc_id)
 gbim_belief                                | gbim_belief_pkey                                                | CREATE UNIQUE INDEX gbim_belief_pkey ON public.gbim_belief USING btree (id)
 gbim_belief_edges                          | gbim_belief_edges_pkey                                          | CREATE UNIQUE INDEX gbim_belief_edges_pkey ON public.gbim_belief_edges USING btree (edge_id)
 gbim_belief_edges                          | gbim_belief_edges_source_idx                                    | CREATE INDEX gbim_belief_edges_source_idx ON public.gbim_belief_edges USING btree (source_belief_id, relation_type)
 gbim_belief_evidence                       | gbim_belief_evidence_evidence_idx                               | CREATE INDEX gbim_belief_evidence_evidence_idx ON public.gbim_belief_evidence USING btree (evidence_id)
 gbim_belief_evidence                       | gbim_belief_evidence_pkey                                       | CREATE UNIQUE INDEX gbim_belief_evidence_pkey ON public.gbim_belief_evidence USING btree (belief_id, evidence_id)
 gbim_beliefs                               | gbim_beliefs_feature_ref_idx                                    | CREATE INDEX gbim_beliefs_feature_ref_idx ON public.gbim_beliefs USING btree (feature_ref)
 gbim_beliefs                               | gbim_beliefs_pkey                                               | CREATE UNIQUE INDEX gbim_beliefs_pkey ON public.gbim_beliefs USING btree (belief_id)
 gbim_beliefs                               | gbim_beliefs_worldview_idx                                      | CREATE INDEX gbim_beliefs_worldview_idx ON public.gbim_beliefs USING btree (worldview_id)
 gbim_beliefs                               | idx_gbim_beliefs_feature_ref                                    | CREATE INDEX idx_gbim_beliefs_feature_ref ON public.gbim_beliefs USING btree (feature_ref)
 gbim_beliefs                               | idx_gbim_beliefs_proposition_code                               | CREATE INDEX idx_gbim_beliefs_proposition_code ON public.gbim_beliefs USING btree (proposition_code)
 gbim_entities                              | gbim_entities_pkey                                              | CREATE UNIQUE INDEX gbim_entities_pkey ON public.gbim_entities USING btree (id)
 gbim_entities                              | idx_gbim_confidence_decay                                       | CREATE INDEX idx_gbim_confidence_decay ON public.gbim_entities USING btree (confidence_decay)
 gbim_entities                              | idx_gbim_last_validated                                         | CREATE INDEX idx_gbim_last_validated ON public.gbim_entities USING btree (last_validated_at)
 gbim_entity_clusters                       | gbim_entity_clusters_pkey                                       | CREATE UNIQUE INDEX gbim_entity_clusters_pkey ON public.gbim_entity_clusters USING btree (canonical_name)
 gbim_entity_land_candidates                | idx_entity_candidates_trgm                                      | CREATE INDEX idx_entity_candidates_trgm ON public.gbim_entity_land_candidates USING gin (fullownername gin_trgm_ops)
 gbim_evidence                              | gbim_evidence_pkey                                              | CREATE UNIQUE INDEX gbim_evidence_pkey ON public.gbim_evidence USING btree (evidence_id)
 gbim_evidence                              | gbim_evidence_source_idx                                        | CREATE INDEX gbim_evidence_source_idx ON public.gbim_evidence USING btree (source_system, source_table, source_pk)
 gbim_full_points                           | idx_gbim_full_points_geom                                       | CREATE INDEX idx_gbim_full_points_geom ON public.gbim_full_points USING gist (geom)
 gbim_full_points                           | idx_gbim_full_points_geom_utm                                   | CREATE INDEX idx_gbim_full_points_geom_utm ON public.gbim_full_points USING gist (geom_utm)
 gbim_layer_config                          | gbim_layer_config_pkey                                          | CREATE UNIQUE INDEX gbim_layer_config_pkey ON public.gbim_layer_config USING btree (sourcetable)
 gbim_layer_manifest                        | gbim_layer_manifest_pkey                                        | CREATE UNIQUE INDEX gbim_layer_manifest_pkey ON public.gbim_layer_manifest USING btree (sourcetable)
 gbim_source_epochs                         | gbim_source_epochs_pkey                                         | CREATE UNIQUE INDEX gbim_source_epochs_pkey ON public.gbim_source_epochs USING btree (sourcetable)
 gbim_worldview_entity                      | gbim_worldview_entity_pkey                                      | CREATE UNIQUE INDEX gbim_worldview_entity_pkey ON public.gbim_worldview_entity USING btree (id)
 gbim_worldview_entity                      | gbim_worldview_entity_unique_feature                            | CREATE UNIQUE INDEX gbim_worldview_entity_unique_feature ON public.gbim_worldview_entity USING btree (source_table, source_pk)
 gbim_worldview_entity                      | idx_gbim_worldview_data_age                                     | CREATE INDEX idx_gbim_worldview_data_age ON public.gbim_worldview_entity USING btree (data_age_months)
 gbim_worldview_entity                      | idx_gbim_worldview_last_verified                                | CREATE INDEX idx_gbim_worldview_last_verified ON public.gbim_worldview_entity USING btree (last_verified)
 gbim_worldview_entity                      | idx_gbim_worldview_needs_verification                           | CREATE INDEX idx_gbim_worldview_needs_verification ON public.gbim_worldview_entity USING btree (needs_verification, data_age_months) WHERE (needs_verification = true)
 gbim_worldviews                            | gbim_worldviews_name_version_idx                                | CREATE UNIQUE INDEX gbim_worldviews_name_version_idx ON public.gbim_worldviews USING btree (name, COALESCE(version_tag, ''::text))
 gbim_worldviews                            | gbim_worldviews_pkey                                            | CREATE UNIQUE INDEX gbim_worldviews_pkey ON public.gbim_worldviews USING btree (worldview_id)
 gbimbeliefnormalized                       | gbim_belief_normalized_pkey                                     | CREATE UNIQUE INDEX gbim_belief_normalized_pkey ON public.gbimbeliefnormalized USING btree (gbim_entity_id)
 gbimbeliefnormalized                       | idx_gbimbelief_epoch                                            | CREATE INDEX idx_gbimbelief_epoch ON public.gbimbeliefnormalized USING btree ((("when" ->> 'epoch'::text)))
 gbimbeliefnormalized                       | idx_gbimbelief_vintage                                          | CREATE INDEX idx_gbimbelief_vintage ON public.gbimbeliefnormalized USING btree ((("when" ->> 'vintage'::text)))
 gbimbeliefnormalized                       | idx_gbimbelief_when_gin                                         | CREATE INDEX idx_gbimbelief_when_gin ON public.gbimbeliefnormalized USING gin ("when")
 geospatial_features                        | geospatial_features_pkey                                        | CREATE UNIQUE INDEX geospatial_features_pkey ON public.geospatial_features USING btree (id)
 geospatial_features                        | geospatial_features_unique                                      | CREATE UNIQUE INDEX geospatial_features_unique ON public.geospatial_features USING btree (layer_name, feature_id)
 geospatial_layers                          | geospatial_layers_pkey                                          | CREATE UNIQUE INDEX geospatial_layers_pkey ON public.geospatial_layers USING btree (layer_name)
 hospitals                                  | hospitals_geom_idx                                              | CREATE INDEX hospitals_geom_idx ON public.hospitals USING gist (geom)
 intake_submissions                         | intake_submissions_pkey                                         | CREATE UNIQUE INDEX intake_submissions_pkey ON public.intake_submissions USING btree (id)
 layer_config                               | layer_config_pkey                                               | CREATE UNIQUE INDEX layer_config_pkey ON public.layer_config USING btree (source_table)
 local_resources                            | idx_local_resources_county                                      | CREATE INDEX idx_local_resources_county ON public.local_resources USING btree (lower(county))
 local_resources                            | idx_local_resources_geom                                        | CREATE INDEX idx_local_resources_geom ON public.local_resources USING gist (geom)
 local_resources                            | local_resources_pkey                                            | CREATE UNIQUE INDEX local_resources_pkey ON public.local_resources USING btree (id)
 ms_jarvis_learning_log                     | idx_mll_action                                                  | CREATE INDEX idx_mll_action ON public.ms_jarvis_learning_log USING btree (learning_action)
 ms_jarvis_learning_log                     | idx_mll_ts                                                      | CREATE INDEX idx_mll_ts ON public.ms_jarvis_learning_log USING btree (created_at DESC)
 ms_jarvis_learning_log                     | idx_mll_ueid                                                    | CREATE INDEX idx_mll_ueid ON public.ms_jarvis_learning_log USING btree (ueid)
 ms_jarvis_learning_log                     | ms_jarvis_learning_log_pkey                                     | CREATE UNIQUE INDEX ms_jarvis_learning_log_pkey ON public.ms_jarvis_learning_log USING btree (id)
 mvw_gbim_landowner_spatial                 | idx_mvw_gbim_landowner_county                                   | CREATE INDEX idx_mvw_gbim_landowner_county ON public.mvw_gbim_landowner_spatial USING btree (county_id)
 mvw_gbim_landowner_spatial                 | idx_mvw_gbim_landowner_geom                                     | CREATE INDEX idx_mvw_gbim_landowner_geom ON public.mvw_gbim_landowner_spatial USING gist (geom)
 mvw_gbim_landowner_spatial                 | idx_mvw_gbim_landowner_uniq                                     | CREATE UNIQUE INDEX idx_mvw_gbim_landowner_uniq ON public.mvw_gbim_landowner_spatial USING btree (belief_id, worldview_id)
 mvw_gbim_landowner_spatial                 | idx_mvw_landowner_county                                        | CREATE INDEX idx_mvw_landowner_county ON public.mvw_gbim_landowner_spatial USING btree (county_id)
 mvw_gbim_landowner_spatial                 | idx_mvw_landowner_entity                                        | CREATE INDEX idx_mvw_landowner_entity ON public.mvw_gbim_landowner_spatial USING btree (entity_name)
 mvw_gbim_landowner_spatial                 | idx_mvw_landowner_geom                                          | CREATE INDEX idx_mvw_landowner_geom ON public.mvw_gbim_landowner_spatial USING gist (geom)
 osm_clinics_wv                             | idx_osm_clinics_geom                                            | CREATE INDEX idx_osm_clinics_geom ON public.osm_clinics_wv USING gist (geom)
 osm_clinics_wv_filtered                    | idx_osm_clinics_filt_geom                                       | CREATE INDEX idx_osm_clinics_filt_geom ON public.osm_clinics_wv_filtered USING gist (geom)
 osm_hospitals_wv                           | idx_osm_hospitals_geom                                          | CREATE INDEX idx_osm_hospitals_geom ON public.osm_hospitals_wv USING gist (geom)
 osm_nursinghomes_wv                        | idx_osm_nh_geom                                                 | CREATE INDEX idx_osm_nh_geom ON public.osm_nursinghomes_wv USING gist (geom)
 osm_nursinghomes_wv_filtered               | idx_osm_nh_filt_geom                                            | CREATE INDEX idx_osm_nh_filt_geom ON public.osm_nursinghomes_wv_filtered USING gist (geom)
 program                                    | program_pkey                                                    | CREATE UNIQUE INDEX program_pkey ON public.program USING btree (program_id)
 program                                    | program_program_code_key                                        | CREATE UNIQUE INDEX program_program_code_key ON public.program USING btree (program_code)
 program_authority_links                    | program_authority_links_pkey                                    | CREATE UNIQUE INDEX program_authority_links_pkey ON public.program_authority_links USING btree (link_id)
 program_catalog                            | program_catalog_pkey                                            | CREATE UNIQUE INDEX program_catalog_pkey ON public.program_catalog USING btree (program_id)
 program_eligibility                        | idx_prog_elig_unique                                            | CREATE UNIQUE INDEX idx_prog_elig_unique ON public.program_eligibility USING btree (program_name, household_size)
 program_eligibility                        | program_eligibility_pkey                                        | CREATE UNIQUE INDEX program_eligibility_pkey ON public.program_eligibility USING btree (id)
 program_entity_links                       | program_entity_links_pkey                                       | CREATE UNIQUE INDEX program_entity_links_pkey ON public.program_entity_links USING btree (link_id)
 program_entity_links                       | program_entity_links_unique_pair                                | CREATE UNIQUE INDEX program_entity_links_unique_pair ON public.program_entity_links USING btree (entity_id, program_id)
 program_evidence_links                     | program_evidence_links_pkey                                     | CREATE UNIQUE INDEX program_evidence_links_pkey ON public.program_evidence_links USING btree (link_id)
 program_income_limit_rules                 | program_income_limit_rules_pkey                                 | CREATE UNIQUE INDEX program_income_limit_rules_pkey ON public.program_income_limit_rules USING btree (program_id, income_rule_id)
 program_income_source_policy               | program_income_source_policy_pkey                               | CREATE UNIQUE INDEX program_income_source_policy_pkey ON public.program_income_source_policy USING btree (policy_id)
 program_income_source_policy               | program_income_source_policy_program_id_source_code_key         | CREATE UNIQUE INDEX program_income_source_policy_program_id_source_code_key ON public.program_income_source_policy USING btree (program_id, source_code)
 program_manual_rule_links                  | program_manual_rule_links_pkey                                  | CREATE UNIQUE INDEX program_manual_rule_links_pkey ON public.program_manual_rule_links USING btree (program_id, rule_id)
 program_name_crosswalk                     | program_name_crosswalk_pkey                                     | CREATE UNIQUE INDEX program_name_crosswalk_pkey ON public.program_name_crosswalk USING btree (local_program_label)
 program_target_config                      | program_target_config_pkey                                      | CREATE UNIQUE INDEX program_target_config_pkey ON public.program_target_config USING btree (program_id, target_layer)
 resource_county_coverage                   | resource_county_coverage_pkey                                   | CREATE UNIQUE INDEX resource_county_coverage_pkey ON public.resource_county_coverage USING btree (resource_id, county_name)
 resource_eligibility                       | resource_eligibility_pkey                                       | CREATE UNIQUE INDEX resource_eligibility_pkey ON public.resource_eligibility USING btree (resource_id, household_size)
 spatial_ref_sys                            | spatial_ref_sys_pkey                                            | CREATE UNIQUE INDEX spatial_ref_sys_pkey ON public.spatial_ref_sys USING btree (srid)
 tiger_county_2022                          | tiger_county_2022_pkey                                          | CREATE UNIQUE INDEX tiger_county_2022_pkey ON public.tiger_county_2022 USING btree (gid)
 tl_2020_54_bg                              | tl_2020_54_bg_geom_idx                                          | CREATE INDEX tl_2020_54_bg_geom_idx ON public.tl_2020_54_bg USING gist (geom)
 tl_2020_54_bg                              | tl_2020_54_bg_pkey                                              | CREATE UNIQUE INDEX tl_2020_54_bg_pkey ON public.tl_2020_54_bg USING btree (gid)
 tl_2020_54_tabblock20                      | tl_2020_54_tabblock20_geom_idx                                  | CREATE INDEX tl_2020_54_tabblock20_geom_idx ON public.tl_2020_54_tabblock20 USING gist (geom)
 tl_2020_54_tabblock20                      | tl_2020_54_tabblock20_pkey                                      | CREATE UNIQUE INDEX tl_2020_54_tabblock20_pkey ON public.tl_2020_54_tabblock20 USING btree (gid)
 uei_registry                               | uei_registry_pkey                                               | CREATE UNIQUE INDEX uei_registry_pkey ON public.uei_registry USING btree (uei)
 uei_registry                               | uei_registry_wallet_address_key                                 | CREATE UNIQUE INDEX uei_registry_wallet_address_key ON public.uei_registry USING btree (wallet_address)
 us_counties                                | us_counties_geom_gix                                            | CREATE INDEX us_counties_geom_gix ON public.us_counties USING gist (geom)
 us_counties                                | us_counties_pkey                                                | CREATE UNIQUE INDEX us_counties_pkey ON public.us_counties USING btree (gid)
 us_counties_26917                          | us_counties_26917_gix                                           | CREATE INDEX us_counties_26917_gix ON public.us_counties_26917 USING gist (geom_26917)
 us_counties_tmp                            | us_counties_tmp_geom_idx                                        | CREATE INDEX us_counties_tmp_geom_idx ON public.us_counties_tmp USING gist (geom)
 us_counties_tmp                            | us_counties_tmp_pkey                                            | CREATE UNIQUE INDEX us_counties_tmp_pkey ON public.us_counties_tmp USING btree (gid)
 us_zips                                    | us_zips_geom_gix                                                | CREATE INDEX us_zips_geom_gix ON public.us_zips USING gist (geom)
 us_zips                                    | us_zips_pkey                                                    | CREATE UNIQUE INDEX us_zips_pkey ON public.us_zips USING btree (gid)
 us_zips_26917                              | us_zips_26917_gix                                               | CREATE INDEX us_zips_26917_gix ON public.us_zips_26917 USING gist (geom_26917)
 us_zips_tmp                                | us_zips_tmp_geom_idx                                            | CREATE INDEX us_zips_tmp_geom_idx ON public.us_zips_tmp USING gist (geom)
 us_zips_tmp                                | us_zips_tmp_pkey                                                | CREATE UNIQUE INDEX us_zips_tmp_pkey ON public.us_zips_tmp USING btree (gid)
 user_compliance_task                       | utility_vendor_notification_pkey                                | CREATE UNIQUE INDEX utility_vendor_notification_pkey ON public.user_compliance_task USING btree (notification_id)
 utility_discount_enrollment                | utility_discount_enrollment_pkey                                | CREATE UNIQUE INDEX utility_discount_enrollment_pkey ON public.utility_discount_enrollment USING btree (enrollment_id)
 utility_discount_enrollment                | utility_discount_enrollment_program_id_utility_account_numb_key | CREATE UNIQUE INDEX utility_discount_enrollment_program_id_utility_account_numb_key ON public.utility_discount_enrollment USING btree (program_id, utility_account_number, utility_type)
 wv_county_bbox_geom                        | idx_wv_county_bbox_geom                                         | CREATE INDEX idx_wv_county_bbox_geom ON public.wv_county_bbox_geom USING gist (geom_bbox)
 wv_county_names                            | wv_county_names_pkey                                            | CREATE UNIQUE INDEX wv_county_names_pkey ON public.wv_county_names USING btree (geodb_id)
 wv_hospitals                               | wv_hospitals_pkey                                               | CREATE UNIQUE INDEX wv_hospitals_pkey ON public.wv_hospitals USING btree (id)
 wv_income_manual_income_limits             | wv_income_manual_income_limits_pkey                             | CREATE UNIQUE INDEX wv_income_manual_income_limits_pkey ON public.wv_income_manual_income_limits USING btree (rule_id)
 wv_income_manual_income_sources            | wv_income_manual_income_sources_pkey                            | CREATE UNIQUE INDEX wv_income_manual_income_sources_pkey ON public.wv_income_manual_income_sources USING btree (source_code)
 wv_income_manual_income_treatment          | wv_income_manual_income_treatment_pkey                          | CREATE UNIQUE INDEX wv_income_manual_income_treatment_pkey ON public.wv_income_manual_income_treatment USING btree (program_code, source_code)
 wv_income_manual_income_treatment_extended | wv_income_manual_income_treatment_extended_pkey                 | CREATE UNIQUE INDEX wv_income_manual_income_treatment_extended_pkey ON public.wv_income_manual_income_treatment_extended USING btree (treatment_id)
 wv_income_manual_rules                     | wv_income_manual_rules_pkey                                     | CREATE UNIQUE INDEX wv_income_manual_rules_pkey ON public.wv_income_manual_rules USING btree (rule_id)
 wv_state_poly                              | idx_wv_state_poly                                               | CREATE INDEX idx_wv_state_poly ON public.wv_state_poly USING gist (geom)
 wvgistcbuildingfootprints                  | wvgistcbuildingfootprints_geom_gix                              | CREATE INDEX wvgistcbuildingfootprints_geom_gix ON public.wvgistcbuildingfootprints USING gist (geom)
 zcta_county_rel                            | idx_zcta_county_zcta5                                           | CREATE INDEX idx_zcta_county_zcta5 ON public.zcta_county_rel USING btree (geoid_zcta5)
 zipcodetabulationarea_census_2020_raw      | zipcodetabulationarea_census_2020_raw_geom_geom_idx             | CREATE INDEX zipcodetabulationarea_census_2020_raw_geom_geom_idx ON public.zipcodetabulationarea_census_2020_raw USING gist (geom)
 zipcodetabulationarea_census_2020_raw      | zipcodetabulationarea_census_2020_raw_pkey                      | CREATE UNIQUE INDEX zipcodetabulationarea_census_2020_raw_pkey ON public.zipcodetabulationarea_census_2020_raw USING btree (ogc_fid)
 zipcodetabulationarea_census_2020_wma84    | zipcodetabulationarea_census_2020_wma84_pkey                    | CREATE UNIQUE INDEX zipcodetabulationarea_census_2020_wma84_pkey ON public.zipcodetabulationarea_census_2020_wma84 USING btree (gid)
(142 rows)


=== Indexes in jarvis-local-resources-db ===
                   tablename                    |                            indexname                            |                                                                                         indexdef                                                                                         
------------------------------------------------+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 attrs_files_list                               | attrs_files_list_pkey                                           | CREATE UNIQUE INDEX attrs_files_list_pkey ON public.attrs_files_list USING btree (id)
 attrs_inventory_detailed                       | attrs_inventory_detailed_pkey                                   | CREATE UNIQUE INDEX attrs_inventory_detailed_pkey ON public.attrs_inventory_detailed USING btree (id)
 authority_references                           | authority_references_pkey                                       | CREATE UNIQUE INDEX authority_references_pkey ON public.authority_references USING btree (authority_id)
 benefit_case                                   | benefit_case_pkey                                               | CREATE UNIQUE INDEX benefit_case_pkey ON public.benefit_case USING btree (case_id)
 benefit_county_daycare                         | benefit_county_daycare_geom_idx                                 | CREATE INDEX benefit_county_daycare_geom_idx ON public.benefit_county_daycare USING gist (geom)
 benefit_county_daycare                         | benefit_county_daycare_pkey                                     | CREATE UNIQUE INDEX benefit_county_daycare_pkey ON public.benefit_county_daycare USING btree (id)
 benefit_county_medicaid                        | benefit_county_medicaid_geom_idx                                | CREATE INDEX benefit_county_medicaid_geom_idx ON public.benefit_county_medicaid USING gist (geom)
 benefit_county_medicaid                        | benefit_county_medicaid_pkey                                    | CREATE UNIQUE INDEX benefit_county_medicaid_pkey ON public.benefit_county_medicaid USING btree (id)
 benefit_county_medicare                        | benefit_county_medicare_geom_idx                                | CREATE INDEX benefit_county_medicare_geom_idx ON public.benefit_county_medicare USING gist (geom)
 benefit_county_medicare                        | benefit_county_medicare_pkey                                    | CREATE UNIQUE INDEX benefit_county_medicare_pkey ON public.benefit_county_medicare USING btree (id)
 benefit_county_section8                        | benefit_county_section8_geom_idx                                | CREATE INDEX benefit_county_section8_geom_idx ON public.benefit_county_section8 USING gist (geom)
 benefit_county_section8                        | benefit_county_section8_pkey                                    | CREATE UNIQUE INDEX benefit_county_section8_pkey ON public.benefit_county_section8 USING btree (id)
 benefit_county_snap                            | benefit_county_snap_geom_idx                                    | CREATE INDEX benefit_county_snap_geom_idx ON public.benefit_county_snap USING gist (geom)
 benefit_county_snap                            | benefit_county_snap_pkey                                        | CREATE UNIQUE INDEX benefit_county_snap_pkey ON public.benefit_county_snap USING btree (id)
 benefit_county_ssi                             | benefit_county_ssi_geom_idx                                     | CREATE INDEX benefit_county_ssi_geom_idx ON public.benefit_county_ssi USING gist (geom)
 benefit_county_ssi                             | benefit_county_ssi_pkey                                         | CREATE UNIQUE INDEX benefit_county_ssi_pkey ON public.benefit_county_ssi USING btree (id)
 benefit_county_tanf                            | benefit_county_tanf_geom_idx                                    | CREATE INDEX benefit_county_tanf_geom_idx ON public.benefit_county_tanf USING gist (geom)
 benefit_county_tanf                            | benefit_county_tanf_pkey                                        | CREATE UNIQUE INDEX benefit_county_tanf_pkey ON public.benefit_county_tanf USING btree (id)
 benefit_county_utility20                       | benefit_county_utility20_geom_idx                               | CREATE INDEX benefit_county_utility20_geom_idx ON public.benefit_county_utility20 USING gist (geom)
 benefit_county_utility20                       | benefit_county_utility20_pkey                                   | CREATE UNIQUE INDEX benefit_county_utility20_pkey ON public.benefit_county_utility20 USING btree (id)
 benefit_county_wic                             | benefit_county_wic_geom_idx                                     | CREATE INDEX benefit_county_wic_geom_idx ON public.benefit_county_wic USING gist (geom)
 benefit_county_wic                             | benefit_county_wic_pkey                                         | CREATE UNIQUE INDEX benefit_county_wic_pkey ON public.benefit_county_wic USING btree (id)
 blockgroups_census_2020_utm83_full             | blockgroups_2020_full_geom_gix                                  | CREATE INDEX blockgroups_2020_full_geom_gix ON public.blockgroups_census_2020_utm83_full USING gist (geom)
 blocks_census_2020_utm83_full                  | blocks_2020_full_geom_gix                                       | CREATE INDEX blocks_2020_full_geom_gix ON public.blocks_census_2020_utm83_full USING gist (geom)
 building_metric_stage                          | building_metric_stage_pkey                                      | CREATE UNIQUE INDEX building_metric_stage_pkey ON public.building_metric_stage USING btree (geodb_id)
 buildings                                      | buildings_geom_idx                                              | CREATE INDEX buildings_geom_idx ON public.buildings USING gist (geom)
 buildings                                      | buildings_pkey                                                  | CREATE UNIQUE INDEX buildings_pkey ON public.buildings USING btree (building_id)
 canonical_layers                               | canonical_layers_pkey                                           | CREATE UNIQUE INDEX canonical_layers_pkey ON public.canonical_layers USING btree (layer_name)
 client_utility_account                         | client_utility_account_pkey                                     | CREATE UNIQUE INDEX client_utility_account_pkey ON public.client_utility_account USING btree (client_id, utility_account_number, utility_type)
 confidence_decay                               | confidence_decay_pkey                                           | CREATE UNIQUE INDEX confidence_decay_pkey ON public.confidence_decay USING btree (id)
 confidence_decay                               | idx_confidence_decay_user                                       | CREATE INDEX idx_confidence_decay_user ON public.confidence_decay USING btree (user_id)
 evidence_documents                             | evidence_documents_pkey                                         | CREATE UNIQUE INDEX evidence_documents_pkey ON public.evidence_documents USING btree (doc_id)
 gbim_belief                                    | gbim_belief_pkey                                                | CREATE UNIQUE INDEX gbim_belief_pkey ON public.gbim_belief USING btree (id)
 gbim_belief_edges                              | gbim_belief_edges_pkey                                          | CREATE UNIQUE INDEX gbim_belief_edges_pkey ON public.gbim_belief_edges USING btree (edge_id)
 gbim_belief_edges                              | gbim_belief_edges_source_idx                                    | CREATE INDEX gbim_belief_edges_source_idx ON public.gbim_belief_edges USING btree (source_belief_id, relation_type)
 gbim_belief_evidence                           | gbim_belief_evidence_evidence_idx                               | CREATE INDEX gbim_belief_evidence_evidence_idx ON public.gbim_belief_evidence USING btree (evidence_id)
 gbim_belief_evidence                           | gbim_belief_evidence_pkey                                       | CREATE UNIQUE INDEX gbim_belief_evidence_pkey ON public.gbim_belief_evidence USING btree (belief_id, evidence_id)
 gbim_beliefs                                   | gbim_beliefs_feature_ref_idx                                    | CREATE INDEX gbim_beliefs_feature_ref_idx ON public.gbim_beliefs USING btree (feature_ref)
 gbim_beliefs                                   | gbim_beliefs_pkey                                               | CREATE UNIQUE INDEX gbim_beliefs_pkey ON public.gbim_beliefs USING btree (belief_id)
 gbim_beliefs                                   | gbim_beliefs_w3_uniq                                            | CREATE UNIQUE INDEX gbim_beliefs_w3_uniq ON public.gbim_beliefs USING btree (worldview_id, feature_ref, proposition_code) WHERE (worldview_id = 3)
 gbim_beliefs                                   | gbim_beliefs_worldview_idx                                      | CREATE INDEX gbim_beliefs_worldview_idx ON public.gbim_beliefs USING btree (worldview_id)
 gbim_entities                                  | gbim_entities_pkey                                              | CREATE UNIQUE INDEX gbim_entities_pkey ON public.gbim_entities USING btree (id)
 gbim_evidence                                  | gbim_evidence_pkey                                              | CREATE UNIQUE INDEX gbim_evidence_pkey ON public.gbim_evidence USING btree (evidence_id)
 gbim_evidence                                  | gbim_evidence_source_idx                                        | CREATE INDEX gbim_evidence_source_idx ON public.gbim_evidence USING btree (source_system, source_table, source_pk)
 gbim_full_points                               | idx_gbim_full_points_geom                                       | CREATE INDEX idx_gbim_full_points_geom ON public.gbim_full_points USING gist (geom)
 gbim_layer_config                              | gbim_layer_config_pkey                                          | CREATE UNIQUE INDEX gbim_layer_config_pkey ON public.gbim_layer_config USING btree (sourcetable)
 gbim_layer_manifest                            | gbim_layer_manifest_pkey                                        | CREATE UNIQUE INDEX gbim_layer_manifest_pkey ON public.gbim_layer_manifest USING btree (sourcetable)
 gbim_source_epochs                             | gbim_source_epochs_pkey                                         | CREATE UNIQUE INDEX gbim_source_epochs_pkey ON public.gbim_source_epochs USING btree (sourcetable)
 gbim_worldview_entity                          | gbim_worldview_entity_pkey                                      | CREATE UNIQUE INDEX gbim_worldview_entity_pkey ON public.gbim_worldview_entity USING btree (id)
 gbim_worldview_entity                          | gbim_worldview_entity_unique_feature                            | CREATE UNIQUE INDEX gbim_worldview_entity_unique_feature ON public.gbim_worldview_entity USING btree (source_table, source_pk)
 gbim_worldviews                                | gbim_worldviews_name_version_idx                                | CREATE UNIQUE INDEX gbim_worldviews_name_version_idx ON public.gbim_worldviews USING btree (name, COALESCE(version_tag, ''::text))
 gbim_worldviews                                | gbim_worldviews_pkey                                            | CREATE UNIQUE INDEX gbim_worldviews_pkey ON public.gbim_worldviews USING btree (worldview_id)
 gbimbeliefnormalized                           | gbim_belief_normalized_pkey                                     | CREATE UNIQUE INDEX gbim_belief_normalized_pkey ON public.gbimbeliefnormalized USING btree (gbim_entity_id)
 gbimbeliefnormalized                           | idx_gbimbelief_epoch                                            | CREATE INDEX idx_gbimbelief_epoch ON public.gbimbeliefnormalized USING btree ((("when" ->> 'epoch'::text)))
 gbimbeliefnormalized                           | idx_gbimbelief_vintage                                          | CREATE INDEX idx_gbimbelief_vintage ON public.gbimbeliefnormalized USING btree ((("when" ->> 'vintage'::text)))
 gbimbeliefnormalized                           | idx_gbimbelief_when_gin                                         | CREATE INDEX idx_gbimbelief_when_gin ON public.gbimbeliefnormalized USING gin ("when")
 geospatial_features                            | geospatial_features_pkey                                        | CREATE UNIQUE INDEX geospatial_features_pkey ON public.geospatial_features USING btree (id)
 geospatial_features                            | geospatial_features_unique                                      | CREATE UNIQUE INDEX geospatial_features_unique ON public.geospatial_features USING btree (layer_name, feature_id)
 geospatial_features                            | idx_geospatial_features_geom                                    | CREATE INDEX idx_geospatial_features_geom ON public.geospatial_features USING gist (geom)
 geospatial_features                            | idx_gf_import_batch                                             | CREATE INDEX idx_gf_import_batch ON public.geospatial_features USING btree (import_batch_id)
 geospatial_features                            | idx_gf_layer_name                                               | CREATE INDEX idx_gf_layer_name ON public.geospatial_features USING btree (layer_name)
 geospatial_features                            | idx_gf_lon_lat                                                  | CREATE INDEX idx_gf_lon_lat ON public.geospatial_features USING btree (lon, lat)
 geospatial_features                            | idx_gf_name                                                     | CREATE INDEX idx_gf_name ON public.geospatial_features USING btree (name) WHERE (name IS NOT NULL)
 geospatial_features                            | idx_gf_source_id                                                | CREATE INDEX idx_gf_source_id ON public.geospatial_features USING btree (source_id)
 geospatial_layers                              | geospatial_layers_pkey                                          | CREATE UNIQUE INDEX geospatial_layers_pkey ON public.geospatial_layers USING btree (layer_name)
 hazardmitigationbuyout_20250929_polygons_wma84 | idx_hazard_buyout_geom                                          | CREATE INDEX idx_hazard_buyout_geom ON public.hazardmitigationbuyout_20250929_polygons_wma84 USING gist (geom)
 layer_config                                   | layer_config_pkey                                               | CREATE UNIQUE INDEX layer_config_pkey ON public.layer_config USING btree (source_table)
 local_resources                                | local_resources_pkey                                            | CREATE UNIQUE INDEX local_resources_pkey ON public.local_resources USING btree (id)
 local_resources_index                          | idx_lri_county                                                  | CREATE INDEX idx_lri_county ON public.local_resources_index USING btree (county)
 local_resources_index                          | idx_lri_zip                                                     | CREATE INDEX idx_lri_zip ON public.local_resources_index USING btree (zip)
 local_resources_index                          | local_resources_index_pkey                                      | CREATE UNIQUE INDEX local_resources_index_pkey ON public.local_resources_index USING btree (id)
 memories                                       | idx_memories_gbim                                               | CREATE INDEX idx_memories_gbim ON public.memories USING btree (gbim_entity_id)
 memories                                       | idx_memories_promoted                                           | CREATE INDEX idx_memories_promoted ON public.memories USING btree (promoted) WHERE (promoted = true)
 memories                                       | idx_memories_spatial                                            | CREATE INDEX idx_memories_spatial ON public.memories USING gist (spatial_ref)
 memories                                       | idx_memories_unreviewed                                         | CREATE INDEX idx_memories_unreviewed ON public.memories USING btree (reviewed) WHERE (reviewed = false)
 memories                                       | memories_pkey                                                   | CREATE UNIQUE INDEX memories_pkey ON public.memories USING btree (id)
 mvw_gbim_landowner_spatial                     | idx_mvw_gbim_landowner_county                                   | CREATE INDEX idx_mvw_gbim_landowner_county ON public.mvw_gbim_landowner_spatial USING btree (county_id)
 mvw_gbim_landowner_spatial                     | idx_mvw_gbim_landowner_geom                                     | CREATE INDEX idx_mvw_gbim_landowner_geom ON public.mvw_gbim_landowner_spatial USING gist (geom)
 mvw_gbim_landowner_spatial                     | idx_mvw_landowner_county                                        | CREATE INDEX idx_mvw_landowner_county ON public.mvw_gbim_landowner_spatial USING btree (county_id)
 mvw_gbim_landowner_spatial                     | idx_mvw_landowner_entity                                        | CREATE INDEX idx_mvw_landowner_entity ON public.mvw_gbim_landowner_spatial USING btree (entity_name)
 mvw_gbim_landowner_spatial                     | idx_mvw_landowner_geom                                          | CREATE INDEX idx_mvw_landowner_geom ON public.mvw_gbim_landowner_spatial USING gist (geom)
 program                                        | program_pkey                                                    | CREATE UNIQUE INDEX program_pkey ON public.program USING btree (program_id)
 program                                        | program_program_code_key                                        | CREATE UNIQUE INDEX program_program_code_key ON public.program USING btree (program_code)
 program_authority_links                        | program_authority_links_pkey                                    | CREATE UNIQUE INDEX program_authority_links_pkey ON public.program_authority_links USING btree (link_id)
 program_catalog                                | program_catalog_pkey                                            | CREATE UNIQUE INDEX program_catalog_pkey ON public.program_catalog USING btree (program_id)
 program_entity_links                           | program_entity_links_pkey                                       | CREATE UNIQUE INDEX program_entity_links_pkey ON public.program_entity_links USING btree (link_id)
 program_entity_links                           | program_entity_links_unique_pair                                | CREATE UNIQUE INDEX program_entity_links_unique_pair ON public.program_entity_links USING btree (entity_id, program_id)
 program_evidence_links                         | program_evidence_links_pkey                                     | CREATE UNIQUE INDEX program_evidence_links_pkey ON public.program_evidence_links USING btree (link_id)
 program_income_limit_rules                     | program_income_limit_rules_pkey                                 | CREATE UNIQUE INDEX program_income_limit_rules_pkey ON public.program_income_limit_rules USING btree (program_id, income_rule_id)
 program_income_source_policy                   | program_income_source_policy_pkey                               | CREATE UNIQUE INDEX program_income_source_policy_pkey ON public.program_income_source_policy USING btree (policy_id)
 program_income_source_policy                   | program_income_source_policy_program_id_source_code_key         | CREATE UNIQUE INDEX program_income_source_policy_program_id_source_code_key ON public.program_income_source_policy USING btree (program_id, source_code)
 program_manual_rule_links                      | program_manual_rule_links_pkey                                  | CREATE UNIQUE INDEX program_manual_rule_links_pkey ON public.program_manual_rule_links USING btree (program_id, rule_id)
 program_target_config                          | program_target_config_pkey                                      | CREATE UNIQUE INDEX program_target_config_pkey ON public.program_target_config USING btree (program_id, target_layer)
 samhsa_provider_stage                          | idx_samhsa_provider_stage_geom                                  | CREATE INDEX idx_samhsa_provider_stage_geom ON public.samhsa_provider_stage USING gist (geom)
 spatial_ref_sys                                | spatial_ref_sys_pkey                                            | CREATE UNIQUE INDEX spatial_ref_sys_pkey ON public.spatial_ref_sys USING btree (srid)
 spatial_role_scopes                            | idx_srs_role                                                    | CREATE INDEX idx_srs_role ON public.spatial_role_scopes USING btree (role_name)
 spatial_role_scopes                            | idx_srs_zcta                                                    | CREATE INDEX idx_srs_zcta ON public.spatial_role_scopes USING btree (zcta_zip)
 spatial_role_scopes                            | spatial_role_scopes_pkey                                        | CREATE UNIQUE INDEX spatial_role_scopes_pkey ON public.spatial_role_scopes USING btree (scope_id)
 spatial_role_scopes                            | spatial_role_scopes_role_name_zcta_zip_key                      | CREATE UNIQUE INDEX spatial_role_scopes_role_name_zcta_zip_key ON public.spatial_role_scopes USING btree (role_name, zcta_zip)
 tl_2020_54_bg                                  | tl_2020_54_bg_geom_idx                                          | CREATE INDEX tl_2020_54_bg_geom_idx ON public.tl_2020_54_bg USING gist (geom)
 tl_2020_54_bg                                  | tl_2020_54_bg_pkey                                              | CREATE UNIQUE INDEX tl_2020_54_bg_pkey ON public.tl_2020_54_bg USING btree (gid)
 tl_2020_54_tabblock20                          | tl_2020_54_tabblock20_geom_idx                                  | CREATE INDEX tl_2020_54_tabblock20_geom_idx ON public.tl_2020_54_tabblock20 USING gist (geom)
 tl_2020_54_tabblock20                          | tl_2020_54_tabblock20_pkey                                      | CREATE UNIQUE INDEX tl_2020_54_tabblock20_pkey ON public.tl_2020_54_tabblock20 USING btree (gid)
 us_counties                                    | us_counties_geom_gix                                            | CREATE INDEX us_counties_geom_gix ON public.us_counties USING gist (geom)
 us_counties                                    | us_counties_pkey                                                | CREATE UNIQUE INDEX us_counties_pkey ON public.us_counties USING btree (gid)
 us_counties_26917                              | us_counties_26917_gix                                           | CREATE INDEX us_counties_26917_gix ON public.us_counties_26917 USING gist (geom_26917)
 us_counties_tmp                                | us_counties_tmp_geom_idx                                        | CREATE INDEX us_counties_tmp_geom_idx ON public.us_counties_tmp USING gist (geom)
 us_counties_tmp                                | us_counties_tmp_pkey                                            | CREATE UNIQUE INDEX us_counties_tmp_pkey ON public.us_counties_tmp USING btree (gid)
 us_zips                                        | us_zips_geom_gix                                                | CREATE INDEX us_zips_geom_gix ON public.us_zips USING gist (geom)
 us_zips                                        | us_zips_pkey                                                    | CREATE UNIQUE INDEX us_zips_pkey ON public.us_zips USING btree (gid)
 us_zips_26917                                  | us_zips_26917_gix                                               | CREATE INDEX us_zips_26917_gix ON public.us_zips_26917 USING gist (geom_26917)
 us_zips_tmp                                    | us_zips_tmp_geom_idx                                            | CREATE INDEX us_zips_tmp_geom_idx ON public.us_zips_tmp USING gist (geom)
 us_zips_tmp                                    | us_zips_tmp_pkey                                                | CREATE UNIQUE INDEX us_zips_tmp_pkey ON public.us_zips_tmp USING btree (gid)
 user_compliance_task                           | utility_vendor_notification_pkey                                | CREATE UNIQUE INDEX utility_vendor_notification_pkey ON public.user_compliance_task USING btree (notification_id)
 utility_discount_enrollment                    | utility_discount_enrollment_pkey                                | CREATE UNIQUE INDEX utility_discount_enrollment_pkey ON public.utility_discount_enrollment USING btree (enrollment_id)
 utility_discount_enrollment                    | utility_discount_enrollment_program_id_utility_account_numb_key | CREATE UNIQUE INDEX utility_discount_enrollment_program_id_utility_account_numb_key ON public.utility_discount_enrollment USING btree (program_id, utility_account_number, utility_type)
 wv_income_manual_income_limits                 | wv_income_manual_income_limits_pkey                             | CREATE UNIQUE INDEX wv_income_manual_income_limits_pkey ON public.wv_income_manual_income_limits USING btree (rule_id)
 wv_income_manual_income_sources                | wv_income_manual_income_sources_pkey                            | CREATE UNIQUE INDEX wv_income_manual_income_sources_pkey ON public.wv_income_manual_income_sources USING btree (source_code)
 wv_income_manual_income_treatment              | wv_income_manual_income_treatment_pkey                          | CREATE UNIQUE INDEX wv_income_manual_income_treatment_pkey ON public.wv_income_manual_income_treatment USING btree (program_code, source_code)
 wv_income_manual_income_treatment_extended     | wv_income_manual_income_treatment_extended_pkey                 | CREATE UNIQUE INDEX wv_income_manual_income_treatment_extended_pkey ON public.wv_income_manual_income_treatment_extended USING btree (treatment_id)
 wv_income_manual_rules                         | wv_income_manual_rules_pkey                                     | CREATE UNIQUE INDEX wv_income_manual_rules_pkey ON public.wv_income_manual_rules USING btree (rule_id)
 wv_zip_zcta_raw                                | idx_wv_zip                                                      | CREATE INDEX idx_wv_zip ON public.wv_zip_zcta_raw USING btree (zip)
 wv_zip_zcta_raw                                | wv_zip_zcta_raw_pkey                                            | CREATE UNIQUE INDEX wv_zip_zcta_raw_pkey ON public.wv_zip_zcta_raw USING btree (geodb_id)
 wvgistcbuildingfootprints                      | wvgistcbuildingfootprints_geom_gix                              | CREATE INDEX wvgistcbuildingfootprints_geom_gix ON public.wvgistcbuildingfootprints USING gist (geom)
 zcta_county_rel                                | zcta_county_rel_county_geoid_idx                                | CREATE INDEX zcta_county_rel_county_geoid_idx ON public.zcta_county_rel USING btree (county_geoid)
 zcta_county_rel                                | zcta_county_rel_geoid_zcta5_idx                                 | CREATE INDEX zcta_county_rel_geoid_zcta5_idx ON public.zcta_county_rel USING btree (geoid_zcta5)
 zcta_county_rel                                | zcta_county_rel_statefp_idx                                     | CREATE INDEX zcta_county_rel_statefp_idx ON public.zcta_county_rel USING btree (statefp)
 zcta_polygons                                  | zcta_polygons_geom_idx                                          | CREATE INDEX zcta_polygons_geom_idx ON public.zcta_polygons USING gist (geom)
 zcta_polygons                                  | zcta_polygons_pkey                                              | CREATE UNIQUE INDEX zcta_polygons_pkey ON public.zcta_polygons USING btree (gid)
 zipcodetabulationarea_census_2020_raw          | zipcodetabulationarea_census_2020_raw_geom_geom_idx             | CREATE INDEX zipcodetabulationarea_census_2020_raw_geom_geom_idx ON public.zipcodetabulationarea_census_2020_raw USING gist (geom)
 zipcodetabulationarea_census_2020_raw          | zipcodetabulationarea_census_2020_raw_pkey                      | CREATE UNIQUE INDEX zipcodetabulationarea_census_2020_raw_pkey ON public.zipcodetabulationarea_census_2020_raw USING btree (ogc_fid)
(131 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ 

