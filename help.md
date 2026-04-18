(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ # Check all heritage data files — sizes and real column counts
echo "=== All data files ==="
ls -lh /mnt/nvme1/msjarvis-rebuild/data/*.csv 2>/dev/null
ls -lh /mnt/nvme1/msjarvis-rebuild/data/*.shp 2>/dev/null
ls -lh /mnt/nvme1/msjarvis-rebuild/data/*.gpkg 2>/dev/null
ls -lh /mnt/nvme1/msjarvis-rebuild/data/*.geojson 2>/dev/null

echo ""
echo "=== Row counts ==="
for f in /mnt/nvme1/msjarvis-rebuild/data/*.csv; do
    echo "$(wc -l < $f) rows — $(basename $f)"
done

echo ""
echo "=== Full headers (first 200 chars) ==="
for f in /mnt/nvme1/msjarvis-rebuild/data/*.csv; do
    echo "--- $(basename $f) ---"
    head -1 $f | cut -c1-200
done
=== All data files ===
-rw-rw-r-- 1 cakidd cakidd   15K Jan 25 18:04 /mnt/nvme1/msjarvis-rebuild/data/attrs_inventory_basic.csv
-rw-rw-r-- 1 cakidd cakidd   33K Jan 25 19:17 /mnt/nvme1/msjarvis-rebuild/data/attrs_inventory_detailed.csv
-rw-rw-r-- 1 cakidd cakidd  1.9K Jan 25 20:13 /mnt/nvme1/msjarvis-rebuild/data/gbim_layer_config.csv
-rw-rw-r-- 1 cakidd cakidd  7.4K Jan 17 23:26 /mnt/nvme1/msjarvis-rebuild/data/geodb_collection_manifest_extended.csv
-rw-rw-r-- 1 cakidd cakidd  3.8K Jan 17 23:26 /mnt/nvme1/msjarvis-rebuild/data/geodb_collection_manifest_v1.csv
-rw-rw-r-- 1 cakidd cakidd   385 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_911centers_wvdem_032819_gcs84_features.csv
-rw-rw-r-- 1 cakidd cakidd   385 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_911centers_wvdem_032819_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd    23 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_amtrackrails_federalrailroadadministration_200210_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd    23 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_amtrackrails_federalrailroadadministration_200210_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   15M Jan 25 10:19 /mnt/nvme1/msjarvis-rebuild/data/h_app_block_features.csv
-rw-rw-r-- 1 cakidd cakidd  345K Jan 25 10:23 /mnt/nvme1/msjarvis-rebuild/data/h_app_blockgroup_features.csv
-rw-rw-r-- 1 cakidd cakidd  448K Jan 25 10:28 /mnt/nvme1/msjarvis-rebuild/data/h_app_blockgroup_features_with_attrs.csv
-rw-rw-r-- 1 cakidd cakidd   13K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_blockgroups_census_2000_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   13K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_blockgroups_census_2000_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   13K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_blockgroups_census_201111_gcs83_features.csv
-rw-rw-r-- 1 cakidd cakidd   13K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_blockgroups_census_201111_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   14K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_blockgroups_census_2020_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   14K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_blockgroups_census_2020_wma84_features.csv
-rw-rw-r-- 1 cakidd cakidd  698K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_blocks_census_2020_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  698K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_blocks_census_2020_wma84_features.csv
-rw-rw-r-- 1 cakidd cakidd  2.4K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_boundaryappalachianbasin_wvges_1996_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   64K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_bridges_features.csv
-rw-rw-r-- 1 cakidd cakidd    71 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_calderl_reg_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd  3.5K Jan 25 10:24 /mnt/nvme1/msjarvis-rebuild/data/h_app_cbsa_features.csv
-rw-rw-r-- 1 cakidd cakidd  8.8K Jan 25 10:29 /mnt/nvme1/msjarvis-rebuild/data/h_app_cbsa_features_with_attrs.csv
-rw-rw-r-- 1 cakidd cakidd   462 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_citieswithpopulation_2500_census_201111_gcs83_features.csv
-rw-rw-r-- 1 cakidd cakidd   462 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_citieswithpopulation_2500_census_201111_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   112 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_citieswithpopulationover10k_census_201111_gcs83_features.csv
-rw-rw-r-- 1 cakidd cakidd   119 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_citieswithpopulationover10k_uscensus_1990_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   119 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_citieswithpopulationover10k_uscensus_1990_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  2.1K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_citieswithpopulationover2500_uscensus_1990_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   105 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_citieswithpopulationsover10k_census_2020_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   105 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_citieswithpopulationsover10k_census_2020_wma84_features.csv
-rw-rw-r-- 1 cakidd cakidd   448 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_citieswithpopulationsover2500_census_2020_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   448 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_citieswithpopulationsover2500_census_2020_wma84_features.csv
-rw-rw-r-- 1 cakidd cakidd  2.1K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_citieswithpopulatoinover2500_uscensus_1990_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   112 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_coals2_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   112 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_coals2_utm27_features.csv
-rw-rw-r-- 1 cakidd cakidd   112 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_coals2_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  2.2K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_communityboundary_min_att_20250121_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  2.2K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_communityboundary_min_att_20250121_wma84_features.csv
-rw-rw-r-- 1 cakidd cakidd  1.1K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_communityhealthproviders_wvhealthcareauthority_200802_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   771 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_correctionalinstitutions_hsip_20091230_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   771 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_correctionalinstitutions_hsip_20091230_wgs84_features.csv
-rw-rw-r-- 1 cakidd cakidd  4.6K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_countycityparkboundaries_20201104_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   392 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_countyseats_usgs_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   392 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_countyseats_usgs_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   392 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_courthousescounty_manysources_200203_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   392 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_courthousescounty_manysources_200203_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd    77 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_courthousesfederal_manysources_200203_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd    77 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_courthousesfederal_manysources_200203_utm_features.csv
-rw-rw-r-- 1 cakidd cakidd    47 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_cvfault_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd    47 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_cvfault_utm27_features.csv
-rw-rw-r-- 1 cakidd cakidd    47 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_cvfault_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   273 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_cvpoly_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   273 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_cvpoly_utm27_features.csv
-rw-rw-r-- 1 cakidd cakidd   273 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_cvpoly_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  3.6K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_damsnoncoal_usgs_2002_ll27_features.csv
-rw-rw-r-- 1 cakidd cakidd  3.6K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_damsnoncoal_usgs_2002_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  4.5K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_dams_usarmycorpsofengineers_200010_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  4.5K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_dams_usarmycropsofengineers_200010_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd  3.5K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_empowermentzonesandenterprisecommunitiesbytract_uscens_30c72907_features.csv
-rw-rw-r-- 1 cakidd cakidd    84 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_empowermentzonesandenterprisecommunities_uscensus_2002_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd    65 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_excursionpassengertrains_wvdof_200102_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd    65 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_excursionpassengertrains_wvdof_200102_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   18K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_facilities_epa_200203_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   18K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_facilities_epa_200203_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  410K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_faultgl_reg_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   899 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_fault_reg_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd  698K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_features_features.csv
-rw-rw-r-- 1 cakidd cakidd  4.2K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_fire_departments_features.csv
-rw-rw-r-- 1 cakidd cakidd  4.2K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_fire_dept_wvdem_092017_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  781K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  426K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_geographicalnamesonusgstopomaps_usgs_200601_ll27_features.csv
-rw-rw-r-- 1 cakidd cakidd  426K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_geographicalnamesonusgstopomaps_usgs_200601_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  295K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_geographicnamesonusgstopomaps_current_usgs_20110801_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd  295K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_geographicnamesonusgstopomaps_current_usgs_20110801_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   63K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_geographicnamesonusgstopomaps_historical_usgs_20110801_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   63K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_geographicnamesonusgstopomaps_historical_usgs_20110801_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  366K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_geographicnamesonusgstopomaps_usgs_20110801_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd  366K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_geographicnamesonusgstopomaps_usgs_20110801_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   15K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_geolgyl_reg_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd  1.5K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_geolgyp_reg_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   779 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_geotextl_reg_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   947 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_glacagl_reg_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd    47 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_glacal_reg_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   25K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_hazardmitigationbuyout_20250929_polygons_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   25K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_hazardmitigationbuyout_20250929_polygons_wma84_features.csv
-rw-rw-r-- 1 cakidd cakidd   427 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_healthruralfacilities_manysources_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   350 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_highered_wvemd_072420_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   350 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_highered_wvemd_072420_wgc84_features.csv
-rw-rw-r-- 1 cakidd cakidd   392 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_historicalaerialphotographycountycoverage_wvgistc_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   176 Jan 25 10:34 /mnt/nvme1/msjarvis-rebuild/data/h_app_horn_summary.csv
-rw-rw-r-- 1 cakidd cakidd    53 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_hospitals_features.csv
-rw-rw-r-- 1 cakidd cakidd   476 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_hospitals_wvdem_040519_gcs84_features.csv
-rw-rw-r-- 1 cakidd cakidd   476 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_hospitals_wvdem_040519_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd    29 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_impact_reg_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd  6.5K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_indexgrid15minutequads_wvgistc_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd  5.2K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_indexgrid15minutequads_wvgistc_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  6.6K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_indexgrid15minutewithcounties_wvgistc_utm27_features.csv
-rw-rw-r-- 1 cakidd cakidd   385 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_indexgrid1minutequads_wvgistc_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   851 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_industrialbuildings_wvdo_200807_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   763 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_industrialparks_wvdo_200078_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  1.4K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_industrialsites_wvdo_200807_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   385 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_inedexgrid1minutequads_wvgistc_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  1.1K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_intermodalterminalfacilities_usdot_1997_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd  1.1K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_intermodalterminalfacilities_usdot_1997_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  2.0K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_libraries_manysources_2001_ll27_features.csv
-rw-rw-r-- 1 cakidd cakidd  2.0K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_libraries_manysources_2001_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   392 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_majorriversandlakesline_nhd_2002_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   392 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_majorriversandlakesline_nhd_2002_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   609 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_majorriversandlakespolygon_nhd_2002_poly_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   609 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_majorriversandlakespolygon_nhd_2002_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   73K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_manufacturingandbusiness_wvdo_200803_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd    53 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_metfacp_reg_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   119 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_metropolitanandmicropolitanstatisticalareas_census_201111_gcs83_features.csv
-rw-rw-r-- 1 cakidd cakidd   119 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_metropolitanandmicropolitanstatisticalareas_census_201111_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   126 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_metropolitanandmicropolitanstatisticalareas_census_2020_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   126 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_metropolitanandmicropolitanstatisticalareas_census_2020_wma84_features.csv
-rw-rw-r-- 1 cakidd cakidd    91 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_metropolitanstatisticalareas_uscensus_199901_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd    91 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_metropolitanstatisticalareas_uscensus_199901_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   413 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_mineraloperations_usgs_200204_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   413 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_mineraloperations_usgs_200204_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   95K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_minesabandonedlandsline_wvdep_1996_noprojectoin_features.csv
-rw-rw-r-- 1 cakidd cakidd  1.7K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_minesabandonedlandspoint_wvdep_1996_noprojection_features.csv
-rw-rw-r-- 1 cakidd cakidd   18K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_minesabandonedlandspolygon_wvdep_1996_noprojection_features.csv
-rw-rw-r-- 1 cakidd cakidd   11K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_nationalatlasstreams_usgs_199903_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   11K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_nationalatlasstreams_usgs_199903_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  5.1K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_nationalregisterofhistoricplacespoints_nationalparkser_45ec46d0_features.csv
-rw-rw-r-- 1 cakidd cakidd  5.1K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_nationalregisterofhistoricplacespoints_natoinalpakrser_8d965955_features.csv
-rw-rw-r-- 1 cakidd cakidd  1.5K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_nationalregisterofhistoricplacespolygons_nationaparkse_b9d30a70_features.csv
-rw-rw-r-- 1 cakidd cakidd  5.8K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_nationalregister_point_20200923_features.csv
-rw-rw-r-- 1 cakidd cakidd  5.8K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_nationalregister_point_20200923_utm27_features.csv
-rw-rw-r-- 1 cakidd cakidd    29 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_nationalwaterwaynetworkports_usarmycorpsofengineers_2001_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd    29 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_nationalwaterwaynetworkports_usarmycorpsofengineers_2001_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   651 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_nationalwaterwaynetwork_usarmycorpsofengineers_2001_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   651 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_nationalwaterwaynetwork_usarmycorpsofengineers_2001_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  5.1K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_nationaregisterofhistoricplacespoints_nationalparkserv_ba8eebd5_features.csv
-rw-rw-r-- 1 cakidd cakidd  1.5K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_nationaregisterofhistoricplacespolygons_nationalparkse_cab42150_features.csv
-rw-rw-r-- 1 cakidd cakidd  5.1K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_natoinalregisterofhistoricplacespoints_nationalparkser_ca43510e_features.csv
-rw-rw-r-- 1 cakidd cakidd    59 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_naviagablewaterways_usarmycropsofengineers_2006_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  3.4K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_navigablewaterwaysrivermiles_usarmycropsofengineers_2006_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  303K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_navigablewaterwaysstructures_usarmycorpsofengineers_2006_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   795 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_nursinghomes_wvdem_041219_gcs84_features.csv
-rw-rw-r-- 1 cakidd cakidd   795 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_nursinghomes_wvdem_041219_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   532 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_officebuildings_wvdo_200807_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   168 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_paroleoffices_manysources_2008_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   168 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_paroleoffices_manysources_2008_wgs84_features.csv
-rw-rw-r-- 1 cakidd cakidd   497 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_placesofworship_hsip_20080723_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   497 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_placesofworship_hsip_20080723_wgs84_features.csv
-rw-rw-r-- 1 cakidd cakidd  2.4K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_policedept_wvdem_012319_gcs84_features.csv
-rw-rw-r-- 1 cakidd cakidd  2.4K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_policedept_wvdem_012319_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  3.1K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_populatedplaces_census_201112_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  3.1K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_populatedplaces_census_20112_gcs83_features.csv
-rw-rw-r-- 1 cakidd cakidd  3.4K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_populatedplaces_census_2020_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  3.4K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_populatedplaces_census_2020_wma84_features.csv
-rw-rw-r-- 1 cakidd cakidd  2.1K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_populatedplaces_uscensus_1990_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd  2.1K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_populatedplaces_uscensus_1990_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   13K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_populationdatablockgroups_uscensus_2000_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   13K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_populationdatablockgroups_uscensus_2000_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   49K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_pow_wvgistc_062919_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   49K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_pow_wvgistc_062919_wgs84_features.csv
-rw-rw-r-- 1 cakidd cakidd   357 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_publichealthdepts_hsip_20091229_gcs83_features.csv
-rw-rw-r-- 1 cakidd cakidd   357 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_publichealthdepts_hsip_20091229_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  109K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_railnetworkregion_usdot_200203_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd  109K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_railnetworkregion_usdot_200203_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   21K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_railnetworkwv_usdot_200203_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   21K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_railnetworkwv_usdot_200203_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   23K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_railroads_rahalltransportationinstitute_2005_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   546 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_realtimestreamflowstations_usgs_200012_ll27_features.csv
-rw-rw-r-- 1 cakidd cakidd   546 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_realtimestreamflowstations_usgs_200012_utm27_features.csv
-rw-rw-r-- 1 cakidd cakidd   546 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_realtimestreamflowstations_usgs_200012_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  2.1K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_recreationalwwtrails_ofwv_20151117_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   399 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_regionalplanninganddevelopmentcouncil_wvdo_1971_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   399 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_regionalplanninganddevelopmentcouncil_wvdo_1971_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   11K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_sewertreatmentplants_wvdep_200203_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   553 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_solidwastefacilities_wvdep_200202_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   553 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_solidwastefacilities_wvdep_200202_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  1.9K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_springs_wvges_1986_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd  1.9K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_springs_wvges_1986_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   476 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_stateofwvhousedistricts_wvlegislativeservices_2010_features.csv
-rw-rw-r-- 1 cakidd cakidd   126 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_stateofwvsenatedistricts_wvlegislativeservices_2010_features.csv
-rw-rw-r-- 1 cakidd cakidd   581 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_states_region_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd  6.5M Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_structurepointsnorth_samb_2003_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  7.8M Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_structurepointssouth_samb_2003_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  141K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_structurepolygons_samb_2003_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  7.5K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_summits_gistc_052012_utm83_shp_features.csv
-rw-rw-r-- 1 cakidd cakidd  7.5K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_summits_gistc_052012_wgs84_shp_features.csv
-rw-rw-r-- 1 cakidd cakidd   75K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_surveycontrol_nationalgeodeticsurvey_102011_gcs83_features.csv
-rw-rw-r-- 1 cakidd cakidd   392 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_timberremovalvolume_usfs_1996_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   455 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_towersam_fcc_200202_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  6.3K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_towersasr_fcc_200202_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd  6.3K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_towersasr_fcc_200202_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  1.8K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_towerscellular_fcc_200202_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd  1.8K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_towerscellular_fcc_200202_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   518 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_towersfm_fcc_200202_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   18K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_towersmicrowave_fcc_200202_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   18K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_towersmicrowave_fcc_200202_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  2.1K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_towerspager_fcc_200202_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd  2.1K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_towerspager_fcc_200202_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   49K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_towersprivate_fcc_200202_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   49K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_towersprivate_fcc_200202_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   105 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_towers_wvpublicbroadcasting_2002_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   105 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_towers_wvpublicbroadcasting_2002_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   119 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_veteransaffairsfacilities_manysources_200503_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   119 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_veteransaffairsfacilities_manysources_200503_wgs84_features.csv
-rw-rw-r-- 1 cakidd cakidd   16K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_votingdistrictswv_legislativeservices_2002_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   16K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_votingdistrictswv_legislativeservices_2002_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   16K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_votingdistrictswv_uscensus_2000_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  1.2K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_weatherstations_nationalclimatedatacenter_1999_gcs83_features.csv
-rw-rw-r-- 1 cakidd cakidd  1.2K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_weatherstations_nationalclimatedatacenter_1999_utm27_features.csv
-rw-rw-r-- 1 cakidd cakidd 1018K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_windenergyresource_nationalrenewableenergylab_200901_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd 1018K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_windenergyresource_nationalrenewableenergylab_200901_wgs84_features.csv
-rw-rw-r-- 1 cakidd cakidd   399 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_workforceinvestmentareas_wvgistc_200208_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   392 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_wv_county_boundaries_24k_topo_updated_2022_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   24M Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_wvgistc_building_footprints_features.csv
-rw-rw-r-- 1 cakidd cakidd   24M Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_wvgistcbuildingfootprints_features.csv
-rw-rw-r-- 1 cakidd cakidd   11M Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_wv_microsoft_20180207_utm17n83_features.csv
-rw-rw-r-- 1 cakidd cakidd    23 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_wvstatebounadary100k_usgs_200203_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd    23 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_wvstateboundary100k_usgs_200203_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd    23 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_wvstateboundary24k_usgs_200203_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd    23 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_wvstateboundary24k_usgs_200203_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   399 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_wvstatehousedistricts_manysources_1992_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   399 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_wvstatehousedistricts_manysources_1992_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   413 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_wvstatehousedistricts_manysources_2002_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   413 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_wvstatehousedistricts_manysources_2002_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   707 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_wvstatehousedistricts_wvlegislativeservices_2020_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   119 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_wvstatesenatedistricts_manysources_1992_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   119 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_wvstatesenatedistricts_manysources_1992_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   119 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_wvstatesenatedistricts_manysources_2002_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd   119 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_wvstatesenatedistricts_manysources_2002_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd   126 Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_wvstatesenatedistricts_wvlegislativeservices_2020_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  4.6K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_wv_tax_districts_ll83_features.csv
-rw-rw-r-- 1 cakidd cakidd  4.6K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_wv_tax_districts_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  4.6K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_wv_tax_districts_wma84_features.csv
-rw-rw-r-- 1 cakidd cakidd  152K Jan 25 10:23 /mnt/nvme1/msjarvis-rebuild/data/h_app_zcta_features.csv
-rw-rw-r-- 1 cakidd cakidd  359K Jan 25 10:29 /mnt/nvme1/msjarvis-rebuild/data/h_app_zcta_features_with_attrs.csv
-rw-rw-r-- 1 cakidd cakidd  5.7K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_zipcodetabulationarea_census_2020_utm83_features.csv
-rw-rw-r-- 1 cakidd cakidd  5.7K Jan 25 10:47 /mnt/nvme1/msjarvis-rebuild/data/h_app_zipcodetabulationarea_census_2020_wma84_features.csv
-rw-rw-r-- 1 cakidd cakidd     2 Jan 23 18:20 /mnt/nvme1/msjarvis-rebuild/data/ms_jarvis_attributes_gis.csv

=== Row counts ===
228 rows — attrs_inventory_basic.csv
227 rows — attrs_inventory_detailed.csv
11 rows — gbim_layer_config.csv
123 rows — geodb_collection_manifest_extended.csv
123 rows — geodb_collection_manifest_v1.csv
55 rows — h_app_911centers_wvdem_032819_gcs84_features.csv
55 rows — h_app_911centers_wvdem_032819_utm83_features.csv
2 rows — h_app_amtrackrails_federalrailroadadministration_200210_ll83_features.csv
2 rows — h_app_amtrackrails_federalrailroadadministration_200210_utm83_features.csv
72559 rows — h_app_block_features.csv
1640 rows — h_app_blockgroup_features.csv
1640 rows — h_app_blockgroup_features_with_attrs.csv
1589 rows — h_app_blockgroups_census_2000_ll83_features.csv
1589 rows — h_app_blockgroups_census_2000_utm83_features.csv
1593 rows — h_app_blockgroups_census_201111_gcs83_features.csv
1593 rows — h_app_blockgroups_census_201111_utm83_features.csv
1640 rows — h_app_blockgroups_census_2020_utm83_features.csv
1640 rows — h_app_blockgroups_census_2020_wma84_features.csv
72559 rows — h_app_blocks_census_2020_utm83_features.csv
72559 rows — h_app_blocks_census_2020_wma84_features.csv
314 rows — h_app_boundaryappalachianbasin_wvges_1996_utm83_features.csv
7358 rows — h_app_bridges_features.csv
10 rows — h_app_calderl_reg_ll83_features.csv
18 rows — h_app_cbsa_features.csv
18 rows — h_app_cbsa_features_with_attrs.csv
66 rows — h_app_citieswithpopulation_2500_census_201111_gcs83_features.csv
66 rows — h_app_citieswithpopulation_2500_census_201111_utm83_features.csv
16 rows — h_app_citieswithpopulationover10k_census_201111_gcs83_features.csv
17 rows — h_app_citieswithpopulationover10k_uscensus_1990_ll83_features.csv
17 rows — h_app_citieswithpopulationover10k_uscensus_1990_utm83_features.csv
278 rows — h_app_citieswithpopulationover2500_uscensus_1990_ll83_features.csv
15 rows — h_app_citieswithpopulationsover10k_census_2020_utm83_features.csv
15 rows — h_app_citieswithpopulationsover10k_census_2020_wma84_features.csv
64 rows — h_app_citieswithpopulationsover2500_census_2020_utm83_features.csv
64 rows — h_app_citieswithpopulationsover2500_census_2020_wma84_features.csv
278 rows — h_app_citieswithpopulatoinover2500_uscensus_1990_utm83_features.csv
16 rows — h_app_coals2_ll83_features.csv
16 rows — h_app_coals2_utm27_features.csv
16 rows — h_app_coals2_utm83_features.csv
293 rows — h_app_communityboundary_min_att_20250121_utm83_features.csv
293 rows — h_app_communityboundary_min_att_20250121_wma84_features.csv
151 rows — h_app_communityhealthproviders_wvhealthcareauthority_200802_utm83_features.csv
109 rows — h_app_correctionalinstitutions_hsip_20091230_utm83_features.csv
109 rows — h_app_correctionalinstitutions_hsip_20091230_wgs84_features.csv
597 rows — h_app_countycityparkboundaries_20201104_utm83_features.csv
56 rows — h_app_countyseats_usgs_ll83_features.csv
56 rows — h_app_countyseats_usgs_utm83_features.csv
56 rows — h_app_courthousescounty_manysources_200203_ll83_features.csv
56 rows — h_app_courthousescounty_manysources_200203_utm83_features.csv
11 rows — h_app_courthousesfederal_manysources_200203_ll83_features.csv
11 rows — h_app_courthousesfederal_manysources_200203_utm_features.csv
6 rows — h_app_cvfault_ll83_features.csv
6 rows — h_app_cvfault_utm27_features.csv
6 rows — h_app_cvfault_utm83_features.csv
39 rows — h_app_cvpoly_ll83_features.csv
39 rows — h_app_cvpoly_utm27_features.csv
39 rows — h_app_cvpoly_utm83_features.csv
469 rows — h_app_damsnoncoal_usgs_2002_ll27_features.csv
469 rows — h_app_damsnoncoal_usgs_2002_utm83_features.csv
576 rows — h_app_dams_usarmycorpsofengineers_200010_utm83_features.csv
576 rows — h_app_dams_usarmycropsofengineers_200010_ll83_features.csv
460 rows — h_app_empowermentzonesandenterprisecommunitiesbytract_uscens_30c72907_features.csv
12 rows — h_app_empowermentzonesandenterprisecommunities_uscensus_2002_utm83_features.csv
9 rows — h_app_excursionpassengertrains_wvdof_200102_ll83_features.csv
9 rows — h_app_excursionpassengertrains_wvdof_200102_utm83_features.csv
2138 rows — h_app_facilities_epa_200203_ll83_features.csv
2138 rows — h_app_facilities_epa_200203_utm83_features.csv
43085 rows — h_app_faultgl_reg_ll83_features.csv
125 rows — h_app_fault_reg_ll83_features.csv
72559 rows — h_app_features_features.csv
549 rows — h_app_fire_departments_features.csv
549 rows — h_app_fire_dept_wvdem_092017_utm83_features.csv
81055 rows — h_app_floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83_features.csv
44651 rows — h_app_geographicalnamesonusgstopomaps_usgs_200601_ll27_features.csv
44651 rows — h_app_geographicalnamesonusgstopomaps_usgs_200601_utm83_features.csv
31258 rows — h_app_geographicnamesonusgstopomaps_current_usgs_20110801_ll83_features.csv
31258 rows — h_app_geographicnamesonusgstopomaps_current_usgs_20110801_utm83_features.csv
7275 rows — h_app_geographicnamesonusgstopomaps_historical_usgs_20110801_ll83_features.csv
7275 rows — h_app_geographicnamesonusgstopomaps_historical_usgs_20110801_utm83_features.csv
38532 rows — h_app_geographicnamesonusgstopomaps_usgs_20110801_ll83_features.csv
38532 rows — h_app_geographicnamesonusgstopomaps_usgs_20110801_utm83_features.csv
1797 rows — h_app_geolgyl_reg_ll83_features.csv
193 rows — h_app_geolgyp_reg_ll83_features.csv
110 rows — h_app_geotextl_reg_ll83_features.csv
131 rows — h_app_glacagl_reg_ll83_features.csv
6 rows — h_app_glacal_reg_ll83_features.csv
2924 rows — h_app_hazardmitigationbuyout_20250929_polygons_utm83_features.csv
2924 rows — h_app_hazardmitigationbuyout_20250929_polygons_wma84_features.csv
61 rows — h_app_healthruralfacilities_manysources_utm83_features.csv
50 rows — h_app_highered_wvemd_072420_utm83_features.csv
50 rows — h_app_highered_wvemd_072420_wgc84_features.csv
56 rows — h_app_historicalaerialphotographycountycoverage_wvgistc_utm83_features.csv
4 rows — h_app_horn_summary.csv
7 rows — h_app_hospitals_features.csv
68 rows — h_app_hospitals_wvdem_040519_gcs84_features.csv
68 rows — h_app_hospitals_wvdem_040519_utm83_features.csv
3 rows — h_app_impact_reg_ll83_features.csv
842 rows — h_app_indexgrid15minutequads_wvgistc_ll83_features.csv
667 rows — h_app_indexgrid15minutequads_wvgistc_utm83_features.csv
846 rows — h_app_indexgrid15minutewithcounties_wvgistc_utm27_features.csv
55 rows — h_app_indexgrid1minutequads_wvgistc_ll83_features.csv
119 rows — h_app_industrialbuildings_wvdo_200807_utm83_features.csv
108 rows — h_app_industrialparks_wvdo_200078_utm83_features.csv
184 rows — h_app_industrialsites_wvdo_200807_utm83_features.csv
55 rows — h_app_inedexgrid1minutequads_wvgistc_utm83_features.csv
153 rows — h_app_intermodalterminalfacilities_usdot_1997_ll83_features.csv
153 rows — h_app_intermodalterminalfacilities_usdot_1997_utm83_features.csv
257 rows — h_app_libraries_manysources_2001_ll27_features.csv
257 rows — h_app_libraries_manysources_2001_utm83_features.csv
56 rows — h_app_majorriversandlakesline_nhd_2002_ll83_features.csv
56 rows — h_app_majorriversandlakesline_nhd_2002_utm83_features.csv
87 rows — h_app_majorriversandlakespolygon_nhd_2002_poly_ll83_features.csv
87 rows — h_app_majorriversandlakespolygon_nhd_2002_utm83_features.csv
8318 rows — h_app_manufacturingandbusiness_wvdo_200803_utm83_features.csv
7 rows — h_app_metfacp_reg_ll83_features.csv
17 rows — h_app_metropolitanandmicropolitanstatisticalareas_census_201111_gcs83_features.csv
17 rows — h_app_metropolitanandmicropolitanstatisticalareas_census_201111_utm83_features.csv
18 rows — h_app_metropolitanandmicropolitanstatisticalareas_census_2020_utm83_features.csv
18 rows — h_app_metropolitanandmicropolitanstatisticalareas_census_2020_wma84_features.csv
13 rows — h_app_metropolitanstatisticalareas_uscensus_199901_ll83_features.csv
13 rows — h_app_metropolitanstatisticalareas_uscensus_199901_utm83_features.csv
59 rows — h_app_mineraloperations_usgs_200204_ll83_features.csv
59 rows — h_app_mineraloperations_usgs_200204_utm83_features.csv
10797 rows — h_app_minesabandonedlandsline_wvdep_1996_noprojectoin_features.csv
220 rows — h_app_minesabandonedlandspoint_wvdep_1996_noprojection_features.csv
2121 rows — h_app_minesabandonedlandspolygon_wvdep_1996_noprojection_features.csv
1276 rows — h_app_nationalatlasstreams_usgs_199903_ll83_features.csv
1276 rows — h_app_nationalatlasstreams_usgs_199903_utm83_features.csv
663 rows — h_app_nationalregisterofhistoricplacespoints_nationalparkser_45ec46d0_features.csv
662 rows — h_app_nationalregisterofhistoricplacespoints_natoinalpakrser_8d965955_features.csv
196 rows — h_app_nationalregisterofhistoricplacespolygons_nationaparkse_b9d30a70_features.csv
753 rows — h_app_nationalregister_point_20200923_features.csv
753 rows — h_app_nationalregister_point_20200923_utm27_features.csv
3 rows — h_app_nationalwaterwaynetworkports_usarmycorpsofengineers_2001_ll83_features.csv
3 rows — h_app_nationalwaterwaynetworkports_usarmycorpsofengineers_2001_utm83_features.csv
93 rows — h_app_nationalwaterwaynetwork_usarmycorpsofengineers_2001_ll83_features.csv
93 rows — h_app_nationalwaterwaynetwork_usarmycorpsofengineers_2001_utm83_features.csv
663 rows — h_app_nationaregisterofhistoricplacespoints_nationalparkserv_ba8eebd5_features.csv
196 rows — h_app_nationaregisterofhistoricplacespolygons_nationalparkse_cab42150_features.csv
662 rows — h_app_natoinalregisterofhistoricplacespoints_nationalparkser_ca43510e_features.csv
8 rows — h_app_naviagablewaterways_usarmycropsofengineers_2006_utm83_features.csv
447 rows — h_app_navigablewaterwaysrivermiles_usarmycropsofengineers_2006_utm83_features.csv
32117 rows — h_app_navigablewaterwaysstructures_usarmycorpsofengineers_2006_utm83_features.csv
112 rows — h_app_nursinghomes_wvdem_041219_gcs84_features.csv
112 rows — h_app_nursinghomes_wvdem_041219_utm83_features.csv
76 rows — h_app_officebuildings_wvdo_200807_utm83_features.csv
24 rows — h_app_paroleoffices_manysources_2008_utm83_features.csv
24 rows — h_app_paroleoffices_manysources_2008_wgs84_features.csv
71 rows — h_app_placesofworship_hsip_20080723_utm83_features.csv
71 rows — h_app_placesofworship_hsip_20080723_wgs84_features.csv
313 rows — h_app_policedept_wvdem_012319_gcs84_features.csv
313 rows — h_app_policedept_wvdem_012319_utm83_features.csv
402 rows — h_app_populatedplaces_census_201112_utm83_features.csv
402 rows — h_app_populatedplaces_census_20112_gcs83_features.csv
440 rows — h_app_populatedplaces_census_2020_utm83_features.csv
440 rows — h_app_populatedplaces_census_2020_wma84_features.csv
278 rows — h_app_populatedplaces_uscensus_1990_ll83_features.csv
278 rows — h_app_populatedplaces_uscensus_1990_utm83_features.csv
1589 rows — h_app_populationdatablockgroups_uscensus_2000_ll83_features.csv
1589 rows — h_app_populationdatablockgroups_uscensus_2000_utm83_features.csv
5614 rows — h_app_pow_wvgistc_062919_utm83_features.csv
5614 rows — h_app_pow_wvgistc_062919_wgs84_features.csv
51 rows — h_app_publichealthdepts_hsip_20091229_gcs83_features.csv
51 rows — h_app_publichealthdepts_hsip_20091229_utm83_features.csv
12218 rows — h_app_railnetworkregion_usdot_200203_ll83_features.csv
12218 rows — h_app_railnetworkregion_usdot_200203_utm83_features.csv
2429 rows — h_app_railnetworkwv_usdot_200203_ll83_features.csv
2429 rows — h_app_railnetworkwv_usdot_200203_utm83_features.csv
2683 rows — h_app_railroads_rahalltransportationinstitute_2005_utm83_features.csv
78 rows — h_app_realtimestreamflowstations_usgs_200012_ll27_features.csv
78 rows — h_app_realtimestreamflowstations_usgs_200012_utm27_features.csv
78 rows — h_app_realtimestreamflowstations_usgs_200012_utm83_features.csv
277 rows — h_app_recreationalwwtrails_ofwv_20151117_utm83_features.csv
57 rows — h_app_regionalplanninganddevelopmentcouncil_wvdo_1971_ll83_features.csv
57 rows — h_app_regionalplanninganddevelopmentcouncil_wvdo_1971_utm83_features.csv
1270 rows — h_app_sewertreatmentplants_wvdep_200203_utm83_features.csv
79 rows — h_app_solidwastefacilities_wvdep_200202_ll83_features.csv
79 rows — h_app_solidwastefacilities_wvdep_200202_utm83_features.csv
250 rows — h_app_springs_wvges_1986_ll83_features.csv
250 rows — h_app_springs_wvges_1986_utm83_features.csv
68 rows — h_app_stateofwvhousedistricts_wvlegislativeservices_2010_features.csv
18 rows — h_app_stateofwvsenatedistricts_wvlegislativeservices_2010_features.csv
83 rows — h_app_states_region_ll83_features.csv
621928 rows — h_app_structurepointsnorth_samb_2003_utm83_features.csv
745033 rows — h_app_structurepointssouth_samb_2003_utm83_features.csv
15506 rows — h_app_structurepolygons_samb_2003_utm83_features.csv
972 rows — h_app_summits_gistc_052012_utm83_shp_features.csv
972 rows — h_app_summits_gistc_052012_wgs84_shp_features.csv
8560 rows — h_app_surveycontrol_nationalgeodeticsurvey_102011_gcs83_features.csv
56 rows — h_app_timberremovalvolume_usfs_1996_utm83_features.csv
65 rows — h_app_towersam_fcc_200202_utm83_features.csv
811 rows — h_app_towersasr_fcc_200202_ll83_features.csv
811 rows — h_app_towersasr_fcc_200202_utm83_features.csv
241 rows — h_app_towerscellular_fcc_200202_ll83_features.csv
241 rows — h_app_towerscellular_fcc_200202_utm83_features.csv
74 rows — h_app_towersfm_fcc_200202_utm83_features.csv
2090 rows — h_app_towersmicrowave_fcc_200202_ll83_features.csv
2090 rows — h_app_towersmicrowave_fcc_200202_utm83_features.csv
273 rows — h_app_towerspager_fcc_200202_ll83_features.csv
273 rows — h_app_towerspager_fcc_200202_utm83_features.csv
5688 rows — h_app_towersprivate_fcc_200202_ll83_features.csv
5688 rows — h_app_towersprivate_fcc_200202_utm83_features.csv
15 rows — h_app_towers_wvpublicbroadcasting_2002_ll83_features.csv
15 rows — h_app_towers_wvpublicbroadcasting_2002_utm83_features.csv
17 rows — h_app_veteransaffairsfacilities_manysources_200503_utm83_features.csv
17 rows — h_app_veteransaffairsfacilities_manysources_200503_wgs84_features.csv
1910 rows — h_app_votingdistrictswv_legislativeservices_2002_ll83_features.csv
1910 rows — h_app_votingdistrictswv_legislativeservices_2002_utm83_features.csv
1927 rows — h_app_votingdistrictswv_uscensus_2000_utm83_features.csv
163 rows — h_app_weatherstations_nationalclimatedatacenter_1999_gcs83_features.csv
163 rows — h_app_weatherstations_nationalclimatedatacenter_1999_utm27_features.csv
104813 rows — h_app_windenergyresource_nationalrenewableenergylab_200901_utm83_features.csv
104813 rows — h_app_windenergyresource_nationalrenewableenergylab_200901_wgs84_features.csv
57 rows — h_app_workforceinvestmentareas_wvgistc_200208_ll83_features.csv
56 rows — h_app_wv_county_boundaries_24k_topo_updated_2022_utm83_features.csv
2121131 rows — h_app_wvgistc_building_footprints_features.csv
2121131 rows — h_app_wvgistcbuildingfootprints_features.csv
1020049 rows — h_app_wv_microsoft_20180207_utm17n83_features.csv
2 rows — h_app_wvstatebounadary100k_usgs_200203_utm83_features.csv
2 rows — h_app_wvstateboundary100k_usgs_200203_ll83_features.csv
2 rows — h_app_wvstateboundary24k_usgs_200203_ll83_features.csv
2 rows — h_app_wvstateboundary24k_usgs_200203_utm83_features.csv
57 rows — h_app_wvstatehousedistricts_manysources_1992_ll83_features.csv
57 rows — h_app_wvstatehousedistricts_manysources_1992_utm83_features.csv
59 rows — h_app_wvstatehousedistricts_manysources_2002_ll83_features.csv
59 rows — h_app_wvstatehousedistricts_manysources_2002_utm83_features.csv
101 rows — h_app_wvstatehousedistricts_wvlegislativeservices_2020_utm83_features.csv
17 rows — h_app_wvstatesenatedistricts_manysources_1992_ll83_features.csv
17 rows — h_app_wvstatesenatedistricts_manysources_1992_utm83_features.csv
17 rows — h_app_wvstatesenatedistricts_manysources_2002_ll83_features.csv
17 rows — h_app_wvstatesenatedistricts_manysources_2002_utm83_features.csv
18 rows — h_app_wvstatesenatedistricts_wvlegislativeservices_2020_utm83_features.csv
601 rows — h_app_wv_tax_districts_ll83_features.csv
601 rows — h_app_wv_tax_districts_utm83_features.csv
601 rows — h_app_wv_tax_districts_wma84_features.csv
742 rows — h_app_zcta_features.csv
742 rows — h_app_zcta_features_with_attrs.csv
742 rows — h_app_zipcodetabulationarea_census_2020_utm83_features.csv
742 rows — h_app_zipcodetabulationarea_census_2020_wma84_features.csv
1 rows — ms_jarvis_attributes_gis.csv

=== Full headers (first 200 chars) ===
--- attrs_inventory_basic.csv ---
id,file_path
--- attrs_inventory_detailed.csv ---
id,file_path,can_join_to_buildings,join_strategy,priority,notes
--- gbim_layer_config.csv ---
sourcetable,geom_table,geom_column,join_mode,search_radius_m,proposition_code,proposition,tags
--- geodb_collection_manifest_extended.csv ---
collection_name,doc_count,priority,theme,geometry_type,gbim_table,notes
--- geodb_collection_manifest_v1.csv ---
collection_name,doc_count
--- h_app_911centers_wvdem_032819_gcs84_features.csv ---
unit_id,pop_2020
--- h_app_911centers_wvdem_032819_utm83_features.csv ---
unit_id,pop_2020
--- h_app_amtrackrails_federalrailroadadministration_200210_ll83_features.csv ---
unit_id,pop_2020
--- h_app_amtrackrails_federalrailroadadministration_200210_utm83_features.csv ---
unit_id,pop_2020
--- h_app_block_features.csv ---
unit_id,unit_type,geom
--- h_app_blockgroup_features.csv ---
unit_id,unit_type,geom
--- h_app_blockgroup_features_with_attrs.csv ---
unit_id,unit_type,geom,label
--- h_app_blockgroups_census_2000_ll83_features.csv ---
unit_id,pop_2020
--- h_app_blockgroups_census_2000_utm83_features.csv ---
unit_id,pop_2020
--- h_app_blockgroups_census_201111_gcs83_features.csv ---
unit_id,pop_2020
--- h_app_blockgroups_census_201111_utm83_features.csv ---
unit_id,pop_2020
--- h_app_blockgroups_census_2020_utm83_features.csv ---
unit_id,pop_2020
--- h_app_blockgroups_census_2020_wma84_features.csv ---
unit_id,pop_2020
--- h_app_blocks_census_2020_utm83_features.csv ---
unit_id,pop_2020
--- h_app_blocks_census_2020_wma84_features.csv ---
unit_id,pop_2020
--- h_app_boundaryappalachianbasin_wvges_1996_utm83_features.csv ---
unit_id,pop_2020
--- h_app_bridges_features.csv ---
unit_id,pop_2020
--- h_app_calderl_reg_ll83_features.csv ---
unit_id,pop_2020
--- h_app_cbsa_features.csv ---
unit_id,unit_type,geom
--- h_app_cbsa_features_with_attrs.csv ---
unit_id,unit_type,geom,lat,lon,bbox,label,sourcetable,country
--- h_app_citieswithpopulation_2500_census_201111_gcs83_features.csv ---
unit_id,pop_2020
--- h_app_citieswithpopulation_2500_census_201111_utm83_features.csv ---
unit_id,pop_2020
--- h_app_citieswithpopulationover10k_census_201111_gcs83_features.csv ---
unit_id,pop_2020
--- h_app_citieswithpopulationover10k_uscensus_1990_ll83_features.csv ---
unit_id,pop_2020
--- h_app_citieswithpopulationover10k_uscensus_1990_utm83_features.csv ---
unit_id,pop_2020
--- h_app_citieswithpopulationover2500_uscensus_1990_ll83_features.csv ---
unit_id,pop_2020
--- h_app_citieswithpopulationsover10k_census_2020_utm83_features.csv ---
unit_id,pop_2020
--- h_app_citieswithpopulationsover10k_census_2020_wma84_features.csv ---
unit_id,pop_2020
--- h_app_citieswithpopulationsover2500_census_2020_utm83_features.csv ---
unit_id,pop_2020
--- h_app_citieswithpopulationsover2500_census_2020_wma84_features.csv ---
unit_id,pop_2020
--- h_app_citieswithpopulatoinover2500_uscensus_1990_utm83_features.csv ---
unit_id,pop_2020
--- h_app_coals2_ll83_features.csv ---
unit_id,pop_2020
--- h_app_coals2_utm27_features.csv ---
unit_id,pop_2020
--- h_app_coals2_utm83_features.csv ---
unit_id,pop_2020
--- h_app_communityboundary_min_att_20250121_utm83_features.csv ---
unit_id,pop_2020
--- h_app_communityboundary_min_att_20250121_wma84_features.csv ---
unit_id,pop_2020
--- h_app_communityhealthproviders_wvhealthcareauthority_200802_utm83_features.csv ---
unit_id,pop_2020
--- h_app_correctionalinstitutions_hsip_20091230_utm83_features.csv ---
unit_id,pop_2020
--- h_app_correctionalinstitutions_hsip_20091230_wgs84_features.csv ---
unit_id,pop_2020
--- h_app_countycityparkboundaries_20201104_utm83_features.csv ---
unit_id,pop_2020
--- h_app_countyseats_usgs_ll83_features.csv ---
unit_id,pop_2020
--- h_app_countyseats_usgs_utm83_features.csv ---
unit_id,pop_2020
--- h_app_courthousescounty_manysources_200203_ll83_features.csv ---
unit_id,pop_2020
--- h_app_courthousescounty_manysources_200203_utm83_features.csv ---
unit_id,pop_2020
--- h_app_courthousesfederal_manysources_200203_ll83_features.csv ---
unit_id,pop_2020
--- h_app_courthousesfederal_manysources_200203_utm_features.csv ---
unit_id,pop_2020
--- h_app_cvfault_ll83_features.csv ---
unit_id,pop_2020
--- h_app_cvfault_utm27_features.csv ---
unit_id,pop_2020
--- h_app_cvfault_utm83_features.csv ---
unit_id,pop_2020
--- h_app_cvpoly_ll83_features.csv ---
unit_id,pop_2020
--- h_app_cvpoly_utm27_features.csv ---
unit_id,pop_2020
--- h_app_cvpoly_utm83_features.csv ---
unit_id,pop_2020
--- h_app_damsnoncoal_usgs_2002_ll27_features.csv ---
unit_id,pop_2020
--- h_app_damsnoncoal_usgs_2002_utm83_features.csv ---
unit_id,pop_2020
--- h_app_dams_usarmycorpsofengineers_200010_utm83_features.csv ---
unit_id,pop_2020
--- h_app_dams_usarmycropsofengineers_200010_ll83_features.csv ---
unit_id,pop_2020
--- h_app_empowermentzonesandenterprisecommunitiesbytract_uscens_30c72907_features.csv ---
unit_id,pop_2020
--- h_app_empowermentzonesandenterprisecommunities_uscensus_2002_utm83_features.csv ---
unit_id,pop_2020
--- h_app_excursionpassengertrains_wvdof_200102_ll83_features.csv ---
unit_id,pop_2020
--- h_app_excursionpassengertrains_wvdof_200102_utm83_features.csv ---
unit_id,pop_2020
--- h_app_facilities_epa_200203_ll83_features.csv ---
unit_id,pop_2020
--- h_app_facilities_epa_200203_utm83_features.csv ---
unit_id,pop_2020
--- h_app_faultgl_reg_ll83_features.csv ---
unit_id,pop_2020
--- h_app_fault_reg_ll83_features.csv ---
unit_id,pop_2020
--- h_app_features_features.csv ---
unit_id,pop_2020
--- h_app_fire_departments_features.csv ---
unit_id,pop_2020
--- h_app_fire_dept_wvdem_092017_utm83_features.csv ---
unit_id,pop_2020
--- h_app_floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83_features.csv ---
unit_id,pop_2020
--- h_app_geographicalnamesonusgstopomaps_usgs_200601_ll27_features.csv ---
unit_id,pop_2020
--- h_app_geographicalnamesonusgstopomaps_usgs_200601_utm83_features.csv ---
unit_id,pop_2020
--- h_app_geographicnamesonusgstopomaps_current_usgs_20110801_ll83_features.csv ---
unit_id,pop_2020
--- h_app_geographicnamesonusgstopomaps_current_usgs_20110801_utm83_features.csv ---
unit_id,pop_2020
--- h_app_geographicnamesonusgstopomaps_historical_usgs_20110801_ll83_features.csv ---
unit_id,pop_2020
--- h_app_geographicnamesonusgstopomaps_historical_usgs_20110801_utm83_features.csv ---
unit_id,pop_2020
--- h_app_geographicnamesonusgstopomaps_usgs_20110801_ll83_features.csv ---
unit_id,pop_2020
--- h_app_geographicnamesonusgstopomaps_usgs_20110801_utm83_features.csv ---
unit_id,pop_2020
--- h_app_geolgyl_reg_ll83_features.csv ---
unit_id,pop_2020
--- h_app_geolgyp_reg_ll83_features.csv ---
unit_id,pop_2020
--- h_app_geotextl_reg_ll83_features.csv ---
unit_id,pop_2020
--- h_app_glacagl_reg_ll83_features.csv ---
unit_id,pop_2020
--- h_app_glacal_reg_ll83_features.csv ---
unit_id,pop_2020
--- h_app_hazardmitigationbuyout_20250929_polygons_utm83_features.csv ---
unit_id,pop_2020
--- h_app_hazardmitigationbuyout_20250929_polygons_wma84_features.csv ---
unit_id,pop_2020
--- h_app_healthruralfacilities_manysources_utm83_features.csv ---
unit_id,pop_2020
--- h_app_highered_wvemd_072420_utm83_features.csv ---
unit_id,pop_2020
--- h_app_highered_wvemd_072420_wgc84_features.csv ---
unit_id,pop_2020
--- h_app_historicalaerialphotographycountycoverage_wvgistc_utm83_features.csv ---
unit_id,pop_2020
--- h_app_horn_summary.csv ---
scale,pop_frac,cum_pop_at_frac,cum_k_at_frac,avg_k_per_person_at_frac,total_pop,total_k
--- h_app_hospitals_features.csv ---
unit_id,pop_2020
--- h_app_hospitals_wvdem_040519_gcs84_features.csv ---
unit_id,pop_2020
--- h_app_hospitals_wvdem_040519_utm83_features.csv ---
unit_id,pop_2020
--- h_app_impact_reg_ll83_features.csv ---
unit_id,pop_2020
--- h_app_indexgrid15minutequads_wvgistc_ll83_features.csv ---
unit_id,pop_2020
--- h_app_indexgrid15minutequads_wvgistc_utm83_features.csv ---
unit_id,pop_2020
--- h_app_indexgrid15minutewithcounties_wvgistc_utm27_features.csv ---
unit_id,pop_2020
--- h_app_indexgrid1minutequads_wvgistc_ll83_features.csv ---
unit_id,pop_2020
--- h_app_industrialbuildings_wvdo_200807_utm83_features.csv ---
unit_id,pop_2020
--- h_app_industrialparks_wvdo_200078_utm83_features.csv ---
unit_id,pop_2020
--- h_app_industrialsites_wvdo_200807_utm83_features.csv ---
unit_id,pop_2020
--- h_app_inedexgrid1minutequads_wvgistc_utm83_features.csv ---
unit_id,pop_2020
--- h_app_intermodalterminalfacilities_usdot_1997_ll83_features.csv ---
unit_id,pop_2020
--- h_app_intermodalterminalfacilities_usdot_1997_utm83_features.csv ---
unit_id,pop_2020
--- h_app_libraries_manysources_2001_ll27_features.csv ---
unit_id,pop_2020
--- h_app_libraries_manysources_2001_utm83_features.csv ---
unit_id,pop_2020
--- h_app_majorriversandlakesline_nhd_2002_ll83_features.csv ---
unit_id,pop_2020
--- h_app_majorriversandlakesline_nhd_2002_utm83_features.csv ---
unit_id,pop_2020
--- h_app_majorriversandlakespolygon_nhd_2002_poly_ll83_features.csv ---
unit_id,pop_2020
--- h_app_majorriversandlakespolygon_nhd_2002_utm83_features.csv ---
unit_id,pop_2020
--- h_app_manufacturingandbusiness_wvdo_200803_utm83_features.csv ---
unit_id,pop_2020
--- h_app_metfacp_reg_ll83_features.csv ---
unit_id,pop_2020
--- h_app_metropolitanandmicropolitanstatisticalareas_census_201111_gcs83_features.csv ---
unit_id,pop_2020
--- h_app_metropolitanandmicropolitanstatisticalareas_census_201111_utm83_features.csv ---
unit_id,pop_2020
--- h_app_metropolitanandmicropolitanstatisticalareas_census_2020_utm83_features.csv ---
unit_id,pop_2020
--- h_app_metropolitanandmicropolitanstatisticalareas_census_2020_wma84_features.csv ---
unit_id,pop_2020
--- h_app_metropolitanstatisticalareas_uscensus_199901_ll83_features.csv ---
unit_id,pop_2020
--- h_app_metropolitanstatisticalareas_uscensus_199901_utm83_features.csv ---
unit_id,pop_2020
--- h_app_mineraloperations_usgs_200204_ll83_features.csv ---
unit_id,pop_2020
--- h_app_mineraloperations_usgs_200204_utm83_features.csv ---
unit_id,pop_2020
--- h_app_minesabandonedlandsline_wvdep_1996_noprojectoin_features.csv ---
unit_id,pop_2020
--- h_app_minesabandonedlandspoint_wvdep_1996_noprojection_features.csv ---
unit_id,pop_2020
--- h_app_minesabandonedlandspolygon_wvdep_1996_noprojection_features.csv ---
unit_id,pop_2020
--- h_app_nationalatlasstreams_usgs_199903_ll83_features.csv ---
unit_id,pop_2020
--- h_app_nationalatlasstreams_usgs_199903_utm83_features.csv ---
unit_id,pop_2020
--- h_app_nationalregisterofhistoricplacespoints_nationalparkser_45ec46d0_features.csv ---
unit_id,pop_2020
--- h_app_nationalregisterofhistoricplacespoints_natoinalpakrser_8d965955_features.csv ---
unit_id,pop_2020
--- h_app_nationalregisterofhistoricplacespolygons_nationaparkse_b9d30a70_features.csv ---
unit_id,pop_2020
--- h_app_nationalregister_point_20200923_features.csv ---
unit_id,pop_2020
--- h_app_nationalregister_point_20200923_utm27_features.csv ---
unit_id,pop_2020
--- h_app_nationalwaterwaynetworkports_usarmycorpsofengineers_2001_ll83_features.csv ---
unit_id,pop_2020
--- h_app_nationalwaterwaynetworkports_usarmycorpsofengineers_2001_utm83_features.csv ---
unit_id,pop_2020
--- h_app_nationalwaterwaynetwork_usarmycorpsofengineers_2001_ll83_features.csv ---
unit_id,pop_2020
--- h_app_nationalwaterwaynetwork_usarmycorpsofengineers_2001_utm83_features.csv ---
unit_id,pop_2020
--- h_app_nationaregisterofhistoricplacespoints_nationalparkserv_ba8eebd5_features.csv ---
unit_id,pop_2020
--- h_app_nationaregisterofhistoricplacespolygons_nationalparkse_cab42150_features.csv ---
unit_id,pop_2020
--- h_app_natoinalregisterofhistoricplacespoints_nationalparkser_ca43510e_features.csv ---
unit_id,pop_2020
--- h_app_naviagablewaterways_usarmycropsofengineers_2006_utm83_features.csv ---
unit_id,pop_2020
--- h_app_navigablewaterwaysrivermiles_usarmycropsofengineers_2006_utm83_features.csv ---
unit_id,pop_2020
--- h_app_navigablewaterwaysstructures_usarmycorpsofengineers_2006_utm83_features.csv ---
unit_id,pop_2020
--- h_app_nursinghomes_wvdem_041219_gcs84_features.csv ---
unit_id,pop_2020
--- h_app_nursinghomes_wvdem_041219_utm83_features.csv ---
unit_id,pop_2020
--- h_app_officebuildings_wvdo_200807_utm83_features.csv ---
unit_id,pop_2020
--- h_app_paroleoffices_manysources_2008_utm83_features.csv ---
unit_id,pop_2020
--- h_app_paroleoffices_manysources_2008_wgs84_features.csv ---
unit_id,pop_2020
--- h_app_placesofworship_hsip_20080723_utm83_features.csv ---
unit_id,pop_2020
--- h_app_placesofworship_hsip_20080723_wgs84_features.csv ---
unit_id,pop_2020
--- h_app_policedept_wvdem_012319_gcs84_features.csv ---
unit_id,pop_2020
--- h_app_policedept_wvdem_012319_utm83_features.csv ---
unit_id,pop_2020
--- h_app_populatedplaces_census_201112_utm83_features.csv ---
unit_id,pop_2020
--- h_app_populatedplaces_census_20112_gcs83_features.csv ---
unit_id,pop_2020
--- h_app_populatedplaces_census_2020_utm83_features.csv ---
unit_id,pop_2020
--- h_app_populatedplaces_census_2020_wma84_features.csv ---
unit_id,pop_2020
--- h_app_populatedplaces_uscensus_1990_ll83_features.csv ---
unit_id,pop_2020
--- h_app_populatedplaces_uscensus_1990_utm83_features.csv ---
unit_id,pop_2020
--- h_app_populationdatablockgroups_uscensus_2000_ll83_features.csv ---
unit_id,pop_2020
--- h_app_populationdatablockgroups_uscensus_2000_utm83_features.csv ---
unit_id,pop_2020
--- h_app_pow_wvgistc_062919_utm83_features.csv ---
unit_id,pop_2020
--- h_app_pow_wvgistc_062919_wgs84_features.csv ---
unit_id,pop_2020
--- h_app_publichealthdepts_hsip_20091229_gcs83_features.csv ---
unit_id,pop_2020
--- h_app_publichealthdepts_hsip_20091229_utm83_features.csv ---
unit_id,pop_2020
--- h_app_railnetworkregion_usdot_200203_ll83_features.csv ---
unit_id,pop_2020
--- h_app_railnetworkregion_usdot_200203_utm83_features.csv ---
unit_id,pop_2020
--- h_app_railnetworkwv_usdot_200203_ll83_features.csv ---
unit_id,pop_2020
--- h_app_railnetworkwv_usdot_200203_utm83_features.csv ---
unit_id,pop_2020
--- h_app_railroads_rahalltransportationinstitute_2005_utm83_features.csv ---
unit_id,pop_2020
--- h_app_realtimestreamflowstations_usgs_200012_ll27_features.csv ---
unit_id,pop_2020
--- h_app_realtimestreamflowstations_usgs_200012_utm27_features.csv ---
unit_id,pop_2020
--- h_app_realtimestreamflowstations_usgs_200012_utm83_features.csv ---
unit_id,pop_2020
--- h_app_recreationalwwtrails_ofwv_20151117_utm83_features.csv ---
unit_id,pop_2020
--- h_app_regionalplanninganddevelopmentcouncil_wvdo_1971_ll83_features.csv ---
unit_id,pop_2020
--- h_app_regionalplanninganddevelopmentcouncil_wvdo_1971_utm83_features.csv ---
unit_id,pop_2020
--- h_app_sewertreatmentplants_wvdep_200203_utm83_features.csv ---
unit_id,pop_2020
--- h_app_solidwastefacilities_wvdep_200202_ll83_features.csv ---
unit_id,pop_2020
--- h_app_solidwastefacilities_wvdep_200202_utm83_features.csv ---
unit_id,pop_2020
--- h_app_springs_wvges_1986_ll83_features.csv ---
unit_id,pop_2020
--- h_app_springs_wvges_1986_utm83_features.csv ---
unit_id,pop_2020
--- h_app_stateofwvhousedistricts_wvlegislativeservices_2010_features.csv ---
unit_id,pop_2020
--- h_app_stateofwvsenatedistricts_wvlegislativeservices_2010_features.csv ---
unit_id,pop_2020
--- h_app_states_region_ll83_features.csv ---
unit_id,pop_2020
--- h_app_structurepointsnorth_samb_2003_utm83_features.csv ---
unit_id,pop_2020
--- h_app_structurepointssouth_samb_2003_utm83_features.csv ---
unit_id,pop_2020
--- h_app_structurepolygons_samb_2003_utm83_features.csv ---
unit_id,pop_2020
--- h_app_summits_gistc_052012_utm83_shp_features.csv ---
unit_id,pop_2020
--- h_app_summits_gistc_052012_wgs84_shp_features.csv ---
unit_id,pop_2020
--- h_app_surveycontrol_nationalgeodeticsurvey_102011_gcs83_features.csv ---
unit_id,pop_2020
--- h_app_timberremovalvolume_usfs_1996_utm83_features.csv ---
unit_id,pop_2020
--- h_app_towersam_fcc_200202_utm83_features.csv ---
unit_id,pop_2020
--- h_app_towersasr_fcc_200202_ll83_features.csv ---
unit_id,pop_2020
--- h_app_towersasr_fcc_200202_utm83_features.csv ---
unit_id,pop_2020
--- h_app_towerscellular_fcc_200202_ll83_features.csv ---
unit_id,pop_2020
--- h_app_towerscellular_fcc_200202_utm83_features.csv ---
unit_id,pop_2020
--- h_app_towersfm_fcc_200202_utm83_features.csv ---
unit_id,pop_2020
--- h_app_towersmicrowave_fcc_200202_ll83_features.csv ---
unit_id,pop_2020
--- h_app_towersmicrowave_fcc_200202_utm83_features.csv ---
unit_id,pop_2020
--- h_app_towerspager_fcc_200202_ll83_features.csv ---
unit_id,pop_2020
--- h_app_towerspager_fcc_200202_utm83_features.csv ---
unit_id,pop_2020
--- h_app_towersprivate_fcc_200202_ll83_features.csv ---
unit_id,pop_2020
--- h_app_towersprivate_fcc_200202_utm83_features.csv ---
unit_id,pop_2020
--- h_app_towers_wvpublicbroadcasting_2002_ll83_features.csv ---
unit_id,pop_2020
--- h_app_towers_wvpublicbroadcasting_2002_utm83_features.csv ---
unit_id,pop_2020
--- h_app_veteransaffairsfacilities_manysources_200503_utm83_features.csv ---
unit_id,pop_2020
--- h_app_veteransaffairsfacilities_manysources_200503_wgs84_features.csv ---
unit_id,pop_2020
--- h_app_votingdistrictswv_legislativeservices_2002_ll83_features.csv ---
unit_id,pop_2020
--- h_app_votingdistrictswv_legislativeservices_2002_utm83_features.csv ---
unit_id,pop_2020
--- h_app_votingdistrictswv_uscensus_2000_utm83_features.csv ---
unit_id,pop_2020
--- h_app_weatherstations_nationalclimatedatacenter_1999_gcs83_features.csv ---
unit_id,pop_2020
--- h_app_weatherstations_nationalclimatedatacenter_1999_utm27_features.csv ---
unit_id,pop_2020
--- h_app_windenergyresource_nationalrenewableenergylab_200901_utm83_features.csv ---
unit_id,pop_2020
--- h_app_windenergyresource_nationalrenewableenergylab_200901_wgs84_features.csv ---
unit_id,pop_2020
--- h_app_workforceinvestmentareas_wvgistc_200208_ll83_features.csv ---
unit_id,pop_2020
--- h_app_wv_county_boundaries_24k_topo_updated_2022_utm83_features.csv ---
unit_id,pop_2020
--- h_app_wvgistc_building_footprints_features.csv ---
unit_id,pop_2020
--- h_app_wvgistcbuildingfootprints_features.csv ---
unit_id,pop_2020
--- h_app_wv_microsoft_20180207_utm17n83_features.csv ---
unit_id,pop_2020
--- h_app_wvstatebounadary100k_usgs_200203_utm83_features.csv ---
unit_id,pop_2020
--- h_app_wvstateboundary100k_usgs_200203_ll83_features.csv ---
unit_id,pop_2020
--- h_app_wvstateboundary24k_usgs_200203_ll83_features.csv ---
unit_id,pop_2020
--- h_app_wvstateboundary24k_usgs_200203_utm83_features.csv ---
unit_id,pop_2020
--- h_app_wvstatehousedistricts_manysources_1992_ll83_features.csv ---
unit_id,pop_2020
--- h_app_wvstatehousedistricts_manysources_1992_utm83_features.csv ---
unit_id,pop_2020
--- h_app_wvstatehousedistricts_manysources_2002_ll83_features.csv ---
unit_id,pop_2020
--- h_app_wvstatehousedistricts_manysources_2002_utm83_features.csv ---
unit_id,pop_2020
--- h_app_wvstatehousedistricts_wvlegislativeservices_2020_utm83_features.csv ---
unit_id,pop_2020
--- h_app_wvstatesenatedistricts_manysources_1992_ll83_features.csv ---
unit_id,pop_2020
--- h_app_wvstatesenatedistricts_manysources_1992_utm83_features.csv ---
unit_id,pop_2020
--- h_app_wvstatesenatedistricts_manysources_2002_ll83_features.csv ---
unit_id,pop_2020
--- h_app_wvstatesenatedistricts_manysources_2002_utm83_features.csv ---
unit_id,pop_2020
--- h_app_wvstatesenatedistricts_wvlegislativeservices_2020_utm83_features.csv ---
unit_id,pop_2020
--- h_app_wv_tax_districts_ll83_features.csv ---
unit_id,pop_2020
--- h_app_wv_tax_districts_utm83_features.csv ---
unit_id,pop_2020
--- h_app_wv_tax_districts_wma84_features.csv ---
unit_id,pop_2020
--- h_app_zcta_features.csv ---
unit_id,unit_type,geom
--- h_app_zcta_features_with_attrs.csv ---
unit_id,unit_type,geom,lat,lon,bbox,label,sourcetable,country
--- h_app_zipcodetabulationarea_census_2020_utm83_features.csv ---
unit_id,pop_2020
--- h_app_zipcodetabulationarea_census_2020_wma84_features.csv ---
unit_id,pop_2020
--- ms_jarvis_attributes_gis.csv ---

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ 

