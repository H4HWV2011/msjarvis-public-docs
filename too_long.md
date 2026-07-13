(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ psql -U postgres -p 5436 -d msjarvisgis_v2 <<'SQL'
-- Confirm feature table
SELECT COUNT(*) AS rows
FROM public.gbim_blockgroup_features;

SELECT bg_geoid,
       jsonb_pretty(attrs_json) AS attrs_pretty
FROM public.gbim_blockgroup_features
ORDER BY bg_geoid
LIMIT 3;

-- Confirm vector table
SELECT COUNT(*) AS rows
FROM public.gbim_blockgroup_vector;

SELECT bg_geoid, left(semantic_text, 1000) AS preview
FROM public.gbim_blockgroup_vector
ORDER BY bg_geoid
LIMIT 3;

ANALYZE public.gbim_blockgroup_features;
ANALYZE public.gbim_blockgroup_vector;
SQL
 rows 
------
 1639
(1 row)

   bg_geoid   |                                           attrs_pretty                                            
--------------+---------------------------------------------------------------------------------------------------
 540019655001 | {                                                                                                +
              |     "bg_geoid": "540019655001",                                                                  +
              |     "coverage": [                                                                                +
              |         {                                                                                        +
              |             "notes": "Blockgroup address-point coverage for Kanawha (v1, SRID-aligned)",         +
              |             "datasettype": "address_points_kanawha",                                             +
              |             "sourcetable": "public.wv_address_points_kanawha_part1 + part2",                     +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "unknown",                                                          +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T16:34:51.846304-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "Statewide county-unioned address-point coverage (v1)",                     +
              |             "datasettype": "address_points_statewide",                                           +
              |             "sourcetable": "public.wv_address_points_statewide_mv",                              +
              |             "featurecount": 445,                                                                 +
              |             "coveragestate": "present",                                                          +
              |             "coveragereason": "features_intersected",                                            +
              |             "calculationtime": "2026-07-12T16:50:27.968289-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for biodiversity priority areas",            +
              |             "datasettype": "public.wv_bio_biodiversity_rank",                                    +
              |             "sourcetable": "public.wv_bio_biodiversity_rank",                                    +
              |             "featurecount": 68,                                                                  +
              |             "coveragestate": "present",                                                          +
              |             "coveragereason": "features_intersected",                                            +
              |             "calculationtime": "2026-07-12T21:17:41.562932-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for EPA-regulated facilities",               +
              |             "datasettype": "public.wv_env_epa_facilities",                                       +
              |             "sourcetable": "public.wv_env_epa_facilities",                                       +
              |             "featurecount": 2,                                                                   +
              |             "coveragestate": "present",                                                          +
              |             "coveragereason": "features_intersected",                                            +
              |             "calculationtime": "2026-07-12T21:18:12.262701-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_env_wildfire_regions",         +
              |             "datasettype": "public.wv_env_wildfire_regions",                                     +
              |             "sourcetable": "public.wv_env_wildfire_regions",                                     +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_env_wind_energy_resources",    +
              |             "datasettype": "public.wv_env_wind_energy_resources",                                +
              |             "sourcetable": "public.wv_env_wind_energy_resources",                                +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_hlt_health_providers",         +
              |             "datasettype": "public.wv_hlt_health_providers",                                     +
              |             "sourcetable": "public.wv_hlt_health_providers",                                     +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_hlt_public_health_departments",+
              |             "datasettype": "public.wv_hlt_public_health_departments",                            +
              |             "sourcetable": "public.wv_hlt_public_health_departments",                            +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_hlt_rural_health_facilities",  +
              |             "datasettype": "public.wv_hlt_rural_health_facilities",                              +
              |             "sourcetable": "public.wv_hlt_rural_health_facilities",                              +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for floodplains",                            +
              |             "datasettype": "public.wv_hyd_hazus_floodplain_zones",                               +
              |             "sourcetable": "public.wv_hyd_hazus_floodplain_zones",                               +
              |             "featurecount": 3,                                                                   +
              |             "coveragestate": "present",                                                          +
              |             "coveragereason": "features_intersected",                                            +
              |             "calculationtime": "2026-07-12T20:49:55.705615-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for high-quality streams",                   +
              |             "datasettype": "public.wv_hyd_streams_high_quality",                                 +
              |             "sourcetable": "public.wv_hyd_streams_high_quality",                                 +
              |             "featurecount": 8,                                                                   +
              |             "coveragestate": "present",                                                          +
              |             "coveragereason": "features_intersected",                                            +
              |             "calculationtime": "2026-07-12T21:18:23.427246-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for fishing & boating access sites",         +
              |             "datasettype": "public.wv_rec_fishing_boating_access",                               +
              |             "sourcetable": "public.wv_rec_fishing_boating_access",                               +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:54.065318-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for fishing lakes",                          +
              |             "datasettype": "public.wv_rec_fishing_lakes",                                        +
              |             "sourcetable": "public.wv_rec_fishing_lakes",                                        +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:54.050938-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for national forest lands",                  +
              |             "datasettype": "public.wv_rec_national_forest",                                      +
              |             "sourcetable": "public.wv_rec_national_forest",                                      +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:53.989436-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for NPS units",                              +
              |             "datasettype": "public.wv_rec_nps_units",                                            +
              |             "sourcetable": "public.wv_rec_nps_units",                                            +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:54.000461-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for national wildlife refuges",              +
              |             "datasettype": "public.wv_rec_nwr_units",                                            +
              |             "sourcetable": "public.wv_rec_nwr_units",                                            +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:54.010841-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for state forests",                          +
              |             "datasettype": "public.wv_rec_state_forests",                                        +
              |             "sourcetable": "public.wv_rec_state_forests",                                        +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:53.95526-04:00",                                +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for state parks",                            +
              |             "datasettype": "public.wv_rec_state_parks",                                          +
              |             "sourcetable": "public.wv_rec_state_parks",                                          +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:54.036266-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for trail points",                           +
              |             "datasettype": "public.wv_rec_trail_points",                                         +
              |             "sourcetable": "public.wv_rec_trail_points",                                         +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:54.075949-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for trails",                                 +
              |             "datasettype": "public.wv_rec_trails",                                               +
              |             "sourcetable": "public.wv_rec_trails",                                               +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:54.086327-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for whitewater trails",                      +
              |             "datasettype": "public.wv_rec_whitewater_trails",                                    +
              |             "sourcetable": "public.wv_rec_whitewater_trails",                                    +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:54.103075-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for WVDNR managed lands",                    +
              |             "datasettype": "public.wv_rec_wvdnr_managed_lands",                                  +
              |             "sourcetable": "public.wv_rec_wvdnr_managed_lands",                                  +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:54.021343-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for hospitals",                              +
              |             "datasettype": "public.wv_soc_hospitals_wvdem",                                      +
              |             "sourcetable": "public.wv_soc_hospitals_wvdem",                                      +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T21:19:02.788746-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_soc_libraries",                +
              |             "datasettype": "public.wv_soc_libraries",                                            +
              |             "sourcetable": "public.wv_soc_libraries",                                            +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_soc_places_of_worship_wvgistc",+
              |             "datasettype": "public.wv_soc_places_of_worship_wvgistc",                            +
              |             "sourcetable": "public.wv_soc_places_of_worship_wvgistc",                            +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for K–12 schools",                           +
              |             "datasettype": "public.wv_soc_schools_k12",                                          +
              |             "sourcetable": "public.wv_soc_schools_k12",                                          +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T21:18:55.160838-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_str_bridges",                  +
              |             "datasettype": "public.wv_str_bridges",                                              +
              |             "sourcetable": "public.wv_str_bridges",                                              +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for airports",                               +
              |             "datasettype": "public.wv_trn_airports",                                             +
              |             "sourcetable": "public.wv_trn_airports",                                             +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T21:19:13.251108-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_trn_railroad_lines_rti",       +
              |             "datasettype": "public.wv_trn_railroad_lines_rti",                                   +
              |             "sourcetable": "public.wv_trn_railroad_lines_rti",                                   +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_trn_roads_interstate",         +
              |             "datasettype": "public.wv_trn_roads_interstate",                                     +
              |             "sourcetable": "public.wv_trn_roads_interstate",                                     +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_trn_roads_major_4800",         +
              |             "datasettype": "public.wv_trn_roads_major_4800",                                     +
              |             "sourcetable": "public.wv_trn_roads_major_4800",                                     +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_trn_roads_state_routes",       +
              |             "datasettype": "public.wv_trn_roads_state_routes",                                   +
              |             "sourcetable": "public.wv_trn_roads_state_routes",                                   +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_trn_roads_us_highways",        +
              |             "datasettype": "public.wv_trn_roads_us_highways",                                    +
              |             "sourcetable": "public.wv_trn_roads_us_highways",                                    +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_trn_roads_us_routes",          +
              |             "datasettype": "public.wv_trn_roads_us_routes",                                      +
              |             "sourcetable": "public.wv_trn_roads_us_routes",                                      +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for wastewater treatment plants",            +
              |             "datasettype": "public.wv_util_sewer_treatment_plants",                              +
              |             "sourcetable": "public.wv_util_sewer_treatment_plants",                              +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T21:19:22.973058-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_util_solid_waste_facilities",  +
              |             "datasettype": "public.wv_util_solid_waste_facilities",                              +
              |             "sourcetable": "public.wv_util_solid_waste_facilities",                              +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         }                                                                                        +
              |     ],                                                                                           +
              |     "identity": {                                                                                +
              |         "county_id": "54001",                                                                    +
              |         "created_at": "2026-07-12T16:21:02.317186-04:00",                                        +
              |         "county_geoid": "54001",                                                                 +
              |         "blockgroup_name": "Block Group 1"                                                       +
              |     }                                                                                            +
              | }
 540019655002 | {                                                                                                +
              |     "bg_geoid": "540019655002",                                                                  +
              |     "coverage": [                                                                                +
              |         {                                                                                        +
              |             "notes": "Blockgroup address-point coverage for Kanawha (v1, SRID-aligned)",         +
              |             "datasettype": "address_points_kanawha",                                             +
              |             "sourcetable": "public.wv_address_points_kanawha_part1 + part2",                     +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "unknown",                                                          +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T16:34:51.846304-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "Statewide county-unioned address-point coverage (v1)",                     +
              |             "datasettype": "address_points_statewide",                                           +
              |             "sourcetable": "public.wv_address_points_statewide_mv",                              +
              |             "featurecount": 701,                                                                 +
              |             "coveragestate": "present",                                                          +
              |             "coveragereason": "features_intersected",                                            +
              |             "calculationtime": "2026-07-12T16:50:27.968289-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for biodiversity priority areas",            +
              |             "datasettype": "public.wv_bio_biodiversity_rank",                                    +
              |             "sourcetable": "public.wv_bio_biodiversity_rank",                                    +
              |             "featurecount": 142,                                                                 +
              |             "coveragestate": "present",                                                          +
              |             "coveragereason": "features_intersected",                                            +
              |             "calculationtime": "2026-07-12T21:17:41.562932-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for EPA-regulated facilities",               +
              |             "datasettype": "public.wv_env_epa_facilities",                                       +
              |             "sourcetable": "public.wv_env_epa_facilities",                                       +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T21:18:12.262701-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_env_wildfire_regions",         +
              |             "datasettype": "public.wv_env_wildfire_regions",                                     +
              |             "sourcetable": "public.wv_env_wildfire_regions",                                     +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_env_wind_energy_resources",    +
              |             "datasettype": "public.wv_env_wind_energy_resources",                                +
              |             "sourcetable": "public.wv_env_wind_energy_resources",                                +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_hlt_health_providers",         +
              |             "datasettype": "public.wv_hlt_health_providers",                                     +
              |             "sourcetable": "public.wv_hlt_health_providers",                                     +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_hlt_public_health_departments",+
              |             "datasettype": "public.wv_hlt_public_health_departments",                            +
              |             "sourcetable": "public.wv_hlt_public_health_departments",                            +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_hlt_rural_health_facilities",  +
              |             "datasettype": "public.wv_hlt_rural_health_facilities",                              +
              |             "sourcetable": "public.wv_hlt_rural_health_facilities",                              +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for floodplains",                            +
              |             "datasettype": "public.wv_hyd_hazus_floodplain_zones",                               +
              |             "sourcetable": "public.wv_hyd_hazus_floodplain_zones",                               +
              |             "featurecount": 8,                                                                   +
              |             "coveragestate": "present",                                                          +
              |             "coveragereason": "features_intersected",                                            +
              |             "calculationtime": "2026-07-12T20:49:55.705615-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for high-quality streams",                   +
              |             "datasettype": "public.wv_hyd_streams_high_quality",                                 +
              |             "sourcetable": "public.wv_hyd_streams_high_quality",                                 +
              |             "featurecount": 33,                                                                  +
              |             "coveragestate": "present",                                                          +
              |             "coveragereason": "features_intersected",                                            +
              |             "calculationtime": "2026-07-12T21:18:23.427246-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for fishing & boating access sites",         +
              |             "datasettype": "public.wv_rec_fishing_boating_access",                               +
              |             "sourcetable": "public.wv_rec_fishing_boating_access",                               +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:54.065318-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for fishing lakes",                          +
              |             "datasettype": "public.wv_rec_fishing_lakes",                                        +
              |             "sourcetable": "public.wv_rec_fishing_lakes",                                        +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:54.050938-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for national forest lands",                  +
              |             "datasettype": "public.wv_rec_national_forest",                                      +
              |             "sourcetable": "public.wv_rec_national_forest",                                      +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:53.989436-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for NPS units",                              +
              |             "datasettype": "public.wv_rec_nps_units",                                            +
              |             "sourcetable": "public.wv_rec_nps_units",                                            +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:54.000461-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for national wildlife refuges",              +
              |             "datasettype": "public.wv_rec_nwr_units",                                            +
              |             "sourcetable": "public.wv_rec_nwr_units",                                            +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:54.010841-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for state forests",                          +
              |             "datasettype": "public.wv_rec_state_forests",                                        +
              |             "sourcetable": "public.wv_rec_state_forests",                                        +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:53.95526-04:00",                                +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for state parks",                            +
              |             "datasettype": "public.wv_rec_state_parks",                                          +
              |             "sourcetable": "public.wv_rec_state_parks",                                          +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:54.036266-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for trail points",                           +
              |             "datasettype": "public.wv_rec_trail_points",                                         +
              |             "sourcetable": "public.wv_rec_trail_points",                                         +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:54.075949-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for trails",                                 +
              |             "datasettype": "public.wv_rec_trails",                                               +
              |             "sourcetable": "public.wv_rec_trails",                                               +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:54.086327-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for whitewater trails",                      +
              |             "datasettype": "public.wv_rec_whitewater_trails",                                    +
              |             "sourcetable": "public.wv_rec_whitewater_trails",                                    +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:54.103075-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for WVDNR managed lands",                    +
              |             "datasettype": "public.wv_rec_wvdnr_managed_lands",                                  +
              |             "sourcetable": "public.wv_rec_wvdnr_managed_lands",                                  +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:54.021343-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for hospitals",                              +
              |             "datasettype": "public.wv_soc_hospitals_wvdem",                                      +
              |             "sourcetable": "public.wv_soc_hospitals_wvdem",                                      +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T21:19:02.788746-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_soc_libraries",                +
              |             "datasettype": "public.wv_soc_libraries",                                            +
              |             "sourcetable": "public.wv_soc_libraries",                                            +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_soc_places_of_worship_wvgistc",+
              |             "datasettype": "public.wv_soc_places_of_worship_wvgistc",                            +
              |             "sourcetable": "public.wv_soc_places_of_worship_wvgistc",                            +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for K–12 schools",                           +
              |             "datasettype": "public.wv_soc_schools_k12",                                          +
              |             "sourcetable": "public.wv_soc_schools_k12",                                          +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T21:18:55.160838-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_str_bridges",                  +
              |             "datasettype": "public.wv_str_bridges",                                              +
              |             "sourcetable": "public.wv_str_bridges",                                              +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for airports",                               +
              |             "datasettype": "public.wv_trn_airports",                                             +
              |             "sourcetable": "public.wv_trn_airports",                                             +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T21:19:13.251108-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_trn_railroad_lines_rti",       +
              |             "datasettype": "public.wv_trn_railroad_lines_rti",                                   +
              |             "sourcetable": "public.wv_trn_railroad_lines_rti",                                   +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_trn_roads_interstate",         +
              |             "datasettype": "public.wv_trn_roads_interstate",                                     +
              |             "sourcetable": "public.wv_trn_roads_interstate",                                     +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_trn_roads_major_4800",         +
              |             "datasettype": "public.wv_trn_roads_major_4800",                                     +
              |             "sourcetable": "public.wv_trn_roads_major_4800",                                     +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_trn_roads_state_routes",       +
              |             "datasettype": "public.wv_trn_roads_state_routes",                                   +
              |             "sourcetable": "public.wv_trn_roads_state_routes",                                   +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_trn_roads_us_highways",        +
              |             "datasettype": "public.wv_trn_roads_us_highways",                                    +
              |             "sourcetable": "public.wv_trn_roads_us_highways",                                    +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_trn_roads_us_routes",          +
              |             "datasettype": "public.wv_trn_roads_us_routes",                                      +
              |             "sourcetable": "public.wv_trn_roads_us_routes",                                      +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for wastewater treatment plants",            +
              |             "datasettype": "public.wv_util_sewer_treatment_plants",                              +
              |             "sourcetable": "public.wv_util_sewer_treatment_plants",                              +
              |             "featurecount": 2,                                                                   +
              |             "coveragestate": "present",                                                          +
              |             "coveragereason": "features_intersected",                                            +
              |             "calculationtime": "2026-07-12T21:19:22.973058-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_util_solid_waste_facilities",  +
              |             "datasettype": "public.wv_util_solid_waste_facilities",                              +
              |             "sourcetable": "public.wv_util_solid_waste_facilities",                              +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         }                                                                                        +
              |     ],                                                                                           +
              |     "identity": {                                                                                +
              |         "county_id": "54001",                                                                    +
              |         "created_at": "2026-07-12T16:21:02.317186-04:00",                                        +
              |         "county_geoid": "54001",                                                                 +
              |         "blockgroup_name": "Block Group 2"                                                       +
              |     }                                                                                            +
              | }
 540019655003 | {                                                                                                +
              |     "bg_geoid": "540019655003",                                                                  +
              |     "coverage": [                                                                                +
              |         {                                                                                        +
              |             "notes": "Blockgroup address-point coverage for Kanawha (v1, SRID-aligned)",         +
              |             "datasettype": "address_points_kanawha",                                             +
              |             "sourcetable": "public.wv_address_points_kanawha_part1 + part2",                     +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "unknown",                                                          +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T16:34:51.846304-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "Statewide county-unioned address-point coverage (v1)",                     +
              |             "datasettype": "address_points_statewide",                                           +
              |             "sourcetable": "public.wv_address_points_statewide_mv",                              +
              |             "featurecount": 966,                                                                 +
              |             "coveragestate": "present",                                                          +
              |             "coveragereason": "features_intersected",                                            +
              |             "calculationtime": "2026-07-12T16:50:27.968289-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for biodiversity priority areas",            +
              |             "datasettype": "public.wv_bio_biodiversity_rank",                                    +
              |             "sourcetable": "public.wv_bio_biodiversity_rank",                                    +
              |             "featurecount": 132,                                                                 +
              |             "coveragestate": "present",                                                          +
              |             "coveragereason": "features_intersected",                                            +
              |             "calculationtime": "2026-07-12T21:17:41.562932-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for EPA-regulated facilities",               +
              |             "datasettype": "public.wv_env_epa_facilities",                                       +
              |             "sourcetable": "public.wv_env_epa_facilities",                                       +
              |             "featurecount": 1,                                                                   +
              |             "coveragestate": "present",                                                          +
              |             "coveragereason": "features_intersected",                                            +
              |             "calculationtime": "2026-07-12T21:18:12.262701-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_env_wildfire_regions",         +
              |             "datasettype": "public.wv_env_wildfire_regions",                                     +
              |             "sourcetable": "public.wv_env_wildfire_regions",                                     +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_env_wind_energy_resources",    +
              |             "datasettype": "public.wv_env_wind_energy_resources",                                +
              |             "sourcetable": "public.wv_env_wind_energy_resources",                                +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_hlt_health_providers",         +
              |             "datasettype": "public.wv_hlt_health_providers",                                     +
              |             "sourcetable": "public.wv_hlt_health_providers",                                     +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_hlt_public_health_departments",+
              |             "datasettype": "public.wv_hlt_public_health_departments",                            +
              |             "sourcetable": "public.wv_hlt_public_health_departments",                            +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_hlt_rural_health_facilities",  +
              |             "datasettype": "public.wv_hlt_rural_health_facilities",                              +
              |             "sourcetable": "public.wv_hlt_rural_health_facilities",                              +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for floodplains",                            +
              |             "datasettype": "public.wv_hyd_hazus_floodplain_zones",                               +
              |             "sourcetable": "public.wv_hyd_hazus_floodplain_zones",                               +
              |             "featurecount": 12,                                                                  +
              |             "coveragestate": "present",                                                          +
              |             "coveragereason": "features_intersected",                                            +
              |             "calculationtime": "2026-07-12T20:49:55.705615-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for high-quality streams",                   +
              |             "datasettype": "public.wv_hyd_streams_high_quality",                                 +
              |             "sourcetable": "public.wv_hyd_streams_high_quality",                                 +
              |             "featurecount": 53,                                                                  +
              |             "coveragestate": "present",                                                          +
              |             "coveragereason": "features_intersected",                                            +
              |             "calculationtime": "2026-07-12T21:18:23.427246-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for fishing & boating access sites",         +
              |             "datasettype": "public.wv_rec_fishing_boating_access",                               +
              |             "sourcetable": "public.wv_rec_fishing_boating_access",                               +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:54.065318-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for fishing lakes",                          +
              |             "datasettype": "public.wv_rec_fishing_lakes",                                        +
              |             "sourcetable": "public.wv_rec_fishing_lakes",                                        +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:54.050938-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for national forest lands",                  +
              |             "datasettype": "public.wv_rec_national_forest",                                      +
              |             "sourcetable": "public.wv_rec_national_forest",                                      +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:53.989436-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for NPS units",                              +
              |             "datasettype": "public.wv_rec_nps_units",                                            +
              |             "sourcetable": "public.wv_rec_nps_units",                                            +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:54.000461-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for national wildlife refuges",              +
              |             "datasettype": "public.wv_rec_nwr_units",                                            +
              |             "sourcetable": "public.wv_rec_nwr_units",                                            +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:54.010841-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for state forests",                          +
              |             "datasettype": "public.wv_rec_state_forests",                                        +
              |             "sourcetable": "public.wv_rec_state_forests",                                        +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:53.95526-04:00",                                +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for state parks",                            +
              |             "datasettype": "public.wv_rec_state_parks",                                          +
              |             "sourcetable": "public.wv_rec_state_parks",                                          +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:54.036266-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for trail points",                           +
              |             "datasettype": "public.wv_rec_trail_points",                                         +
              |             "sourcetable": "public.wv_rec_trail_points",                                         +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:54.075949-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for trails",                                 +
              |             "datasettype": "public.wv_rec_trails",                                               +
              |             "sourcetable": "public.wv_rec_trails",                                               +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:54.086327-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for whitewater trails",                      +
              |             "datasettype": "public.wv_rec_whitewater_trails",                                    +
              |             "sourcetable": "public.wv_rec_whitewater_trails",                                    +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:54.103075-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for WVDNR managed lands",                    +
              |             "datasettype": "public.wv_rec_wvdnr_managed_lands",                                  +
              |             "sourcetable": "public.wv_rec_wvdnr_managed_lands",                                  +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-13T02:13:54.021343-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for hospitals",                              +
              |             "datasettype": "public.wv_soc_hospitals_wvdem",                                      +
              |             "sourcetable": "public.wv_soc_hospitals_wvdem",                                      +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T21:19:02.788746-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_soc_libraries",                +
              |             "datasettype": "public.wv_soc_libraries",                                            +
              |             "sourcetable": "public.wv_soc_libraries",                                            +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_soc_places_of_worship_wvgistc",+
              |             "datasettype": "public.wv_soc_places_of_worship_wvgistc",                            +
              |             "sourcetable": "public.wv_soc_places_of_worship_wvgistc",                            +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for K–12 schools",                           +
              |             "datasettype": "public.wv_soc_schools_k12",                                          +
              |             "sourcetable": "public.wv_soc_schools_k12",                                          +
              |             "featurecount": 1,                                                                   +
              |             "coveragestate": "present",                                                          +
              |             "coveragereason": "features_intersected",                                            +
              |             "calculationtime": "2026-07-12T21:18:55.160838-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_str_bridges",                  +
              |             "datasettype": "public.wv_str_bridges",                                              +
              |             "sourcetable": "public.wv_str_bridges",                                              +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for airports",                               +
              |             "datasettype": "public.wv_trn_airports",                                             +
              |             "sourcetable": "public.wv_trn_airports",                                             +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T21:19:13.251108-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_trn_railroad_lines_rti",       +
              |             "datasettype": "public.wv_trn_railroad_lines_rti",                                   +
              |             "sourcetable": "public.wv_trn_railroad_lines_rti",                                   +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_trn_roads_interstate",         +
              |             "datasettype": "public.wv_trn_roads_interstate",                                     +
              |             "sourcetable": "public.wv_trn_roads_interstate",                                     +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_trn_roads_major_4800",         +
              |             "datasettype": "public.wv_trn_roads_major_4800",                                     +
              |             "sourcetable": "public.wv_trn_roads_major_4800",                                     +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_trn_roads_state_routes",       +
              |             "datasettype": "public.wv_trn_roads_state_routes",                                   +
              |             "sourcetable": "public.wv_trn_roads_state_routes",                                   +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_trn_roads_us_highways",        +
              |             "datasettype": "public.wv_trn_roads_us_highways",                                    +
              |             "sourcetable": "public.wv_trn_roads_us_highways",                                    +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_trn_roads_us_routes",          +
              |             "datasettype": "public.wv_trn_roads_us_routes",                                      +
              |             "sourcetable": "public.wv_trn_roads_us_routes",                                      +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for wastewater treatment plants",            +
              |             "datasettype": "public.wv_util_sewer_treatment_plants",                              +
              |             "sourcetable": "public.wv_util_sewer_treatment_plants",                              +
              |             "featurecount": 1,                                                                   +
              |             "coveragestate": "present",                                                          +
              |             "coveragereason": "features_intersected",                                            +
              |             "calculationtime": "2026-07-12T21:19:22.973058-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         },                                                                                       +
              |         {                                                                                        +
              |             "notes": "GBIM blockgroup coverage load for public.wv_util_solid_waste_facilities",  +
              |             "datasettype": "public.wv_util_solid_waste_facilities",                              +
              |             "sourcetable": "public.wv_util_solid_waste_facilities",                              +
              |             "featurecount": 0,                                                                   +
              |             "coveragestate": "absent",                                                           +
              |             "coveragereason": "no_features_found_in_covered_area",                               +
              |             "calculationtime": "2026-07-12T20:28:35.867556-04:00",                               +
              |             "sourcelayerhash": null                                                              +
              |         }                                                                                        +
              |     ],                                                                                           +
              |     "identity": {                                                                                +
              |         "county_id": "54001",                                                                    +
              |         "created_at": "2026-07-12T16:21:02.317186-04:00",                                        +
              |         "county_geoid": "54001",                                                                 +
              |         "blockgroup_name": "Block Group 3"                                                       +
              |     }                                                                                            +
              | }
(3 rows)

 rows 
------
 1639
(1 row)

   bg_geoid   |                                                                         preview                                                                         
--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------
 540019655001 | Blockgroup: 540019655001                                                                                                                               +
              | Identity: {"county_id": "54001", "created_at": "2026-07-12T16:21:02.317186-04:00", "county_geoid": "54001", "blockgroup_name": "Block Group 1"}        +
              | Coverage layers:                                                                                                                                       +
              | layer=public.wv_address_points_kanawha_part1 + part2 | type=address_points_kanawha | count=0 | state=unknown | reason=no_features_found_in_covered_area+
              | layer=public.wv_address_points_statewide_mv | type=address_points_statewide | count=445 | state=present | reason=features_intersected                  +
              | layer=public.wv_bio_biodiversity_rank | type=public.wv_bio_biodiversity_rank | count=68 | state=present | reason=features_intersected                  +
              | layer=public.wv_env_epa_facilities | type=public.wv_env_epa_facilities | count=2 | state=present | reason=features_intersected                         +
              | layer=public.wv_env_wildfire_regions | type=public.wv_env_wildfire_regions | count=0 | state=absent | reason=no_features_found_in_covered_area         +
              | layer=public.wv_env_wind_energy_resources | type=public.wv_env_wind_energy_resources | count=0 | state=absent | reason=no_fe
 540019655002 | Blockgroup: 540019655002                                                                                                                               +
              | Identity: {"county_id": "54001", "created_at": "2026-07-12T16:21:02.317186-04:00", "county_geoid": "54001", "blockgroup_name": "Block Group 2"}        +
              | Coverage layers:                                                                                                                                       +
              | layer=public.wv_address_points_kanawha_part1 + part2 | type=address_points_kanawha | count=0 | state=unknown | reason=no_features_found_in_covered_area+
              | layer=public.wv_address_points_statewide_mv | type=address_points_statewide | count=701 | state=present | reason=features_intersected                  +
              | layer=public.wv_bio_biodiversity_rank | type=public.wv_bio_biodiversity_rank | count=142 | state=present | reason=features_intersected                 +
              | layer=public.wv_env_epa_facilities | type=public.wv_env_epa_facilities | count=0 | state=absent | reason=no_features_found_in_covered_area             +
              | layer=public.wv_env_wildfire_regions | type=public.wv_env_wildfire_regions | count=0 | state=absent | reason=no_features_found_in_covered_area         +
              | layer=public.wv_env_wind_energy_resources | type=public.wv_env_wind_energy_resources | count=0 | state=absent |
 540019655003 | Blockgroup: 540019655003                                                                                                                               +
              | Identity: {"county_id": "54001", "created_at": "2026-07-12T16:21:02.317186-04:00", "county_geoid": "54001", "blockgroup_name": "Block Group 3"}        +
              | Coverage layers:                                                                                                                                       +
              | layer=public.wv_address_points_kanawha_part1 + part2 | type=address_points_kanawha | count=0 | state=unknown | reason=no_features_found_in_covered_area+
              | layer=public.wv_address_points_statewide_mv | type=address_points_statewide | count=966 | state=present | reason=features_intersected                  +
              | layer=public.wv_bio_biodiversity_rank | type=public.wv_bio_biodiversity_rank | count=132 | state=present | reason=features_intersected                 +
              | layer=public.wv_env_epa_facilities | type=public.wv_env_epa_facilities | count=1 | state=present | reason=features_intersected                         +
              | layer=public.wv_env_wildfire_regions | type=public.wv_env_wildfire_regions | count=0 | state=absent | reason=no_features_found_in_covered_area         +
              | layer=public.wv_env_wind_energy_resources | type=public.wv_env_wind_energy_resources | count=0 | state=absent | reason=no_f
(3 rows)

ANALYZE
ANALYZE
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ 

