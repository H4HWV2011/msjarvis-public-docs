(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild/formal/commons_proofs$ CLOSEOUT=~/msjarvis-rebuild/production-closeout-20260729
DUMP=/mnt/spiritual_drive/msjarvis-rebuild/production_closeout_20260728/backups/wv_gis_20260728_001859.dump

# 1. What objects are in the production dump (runtime_governance + key public tables)
echo "=== DUMP TOC: all runtime_governance + public non-wv tables ===" \
  | tee "$CLOSEOUT/blocker2-gap-analysis-20260729.log"

pg_restore --list "$DUMP" \
  | grep -vE "^;" \
  | grep -vE "TABLE DATA public wv_" \
  | grep -E "runtime_governance|TABLE public [^w]|FUNCTION|PROCEDURE|VIEW|MATERIALIZED|SEQUENCE|INDEX|TRIGGER" \
  | tee -a "$CLOSEOUT/blocker2-gap-analysis-20260729.log"

echo "" | tee -a "$CLOSEOUT/blocker2-gap-analysis-20260729.log"

# 2. What runtime_governance objects currently exist in msjarvisgis_v2
echo "=== CURRENT runtime_governance objects in msjarvisgis_v2 ===" \
  | tee -a "$CLOSEOUT/blocker2-gap-analysis-20260729.log"

docker exec -i jarvis-msjarvis-db psql -U postgres -d msjarvisgis_v2 -X -P pager=off << 'SQL' \
  | tee -a "$CLOSEOUT/blocker2-gap-analysis-20260729.log"ents(p.oid) || ')'D,
=== DUMP TOC: all runtime_governance + public non-wv tables ===
24; 2615 4134489 SCHEMA - runtime_governance postgres
8925; 0 0 ACL - SCHEMA runtime_governance postgres
1137; 1255 4134912 FUNCTION identity biometric_enrollment_allowed(bigint) postgres
1337; 1255 4134861 FUNCTION identity prune_expired_identities() postgres
1304; 1255 4120149 FUNCTION private get_hilbert_person_governed(text, text, text, text, text, text) postgres
8929; 0 0 ACL private FUNCTION get_hilbert_person_governed(p_requester_role text, p_requester_subject text, p_request_purpose text, p_legal_basis text, p_case_id text, p_subject_lookup text) postgres
1451; 1255 4120113 FUNCTION public enforce_gbim_active_collection_gate() msjarvis
1344; 1255 4120118 FUNCTION public evaluate_gbim_manifest_coherence(text, text) postgres
8930; 0 0 ACL public FUNCTION evaluate_gbim_manifest_coherence(p_collection_name text, p_collection_version text) postgres
1212; 1255 772032 PROCEDURE public gbim_bg_coverage_all() postgres
1072; 1255 1117103 PROCEDURE public gbim_bg_coverage_v2() postgres
931; 1259 4134366 TABLE public gbim_record postgres
1237; 1255 4134443 FUNCTION public gbim_feature_hash(public.gbim_record) postgres
1339; 1255 4134423 PROCEDURE public gbim_load_bg_table(text) postgres
1825; 1255 756427 PROCEDURE public gbim_load_blockgroup_coverage(text) postgres
1200; 1255 4134403 FUNCTION public gbim_promote(uuid) postgres
1341; 1255 4120117 FUNCTION public promote_gbim_collection(text, text) postgres
8932; 0 0 ACL public FUNCTION promote_gbim_collection(p_collection_name text, p_collection_version text) postgres
1330; 1255 4134488 FUNCTION public refresh_gbim_degradation_status() postgres
1488; 1255 4120115 FUNCTION public sync_gbim_publication_manifest_promoted_at() msjarvis
1104; 1255 771885 FUNCTION public transform_safe(public.geometry, integer) postgres
1256; 1255 4134503 FUNCTION runtime_governance apply_runtime_lifecycle() postgres
1463; 1255 4135002 FUNCTION runtime_governance commons_attempt_reconstruction(text, text, text) postgres
1028; 1255 4134933 FUNCTION runtime_governance commons_can_aggregate(text, text) postgres
1150; 1255 4134968 FUNCTION runtime_governance commons_reconstruction_allowed() postgres
1796; 1255 4134934 FUNCTION runtime_governance commons_scalar_average(text, text, text) postgres
1255; 1255 4134959 FUNCTION runtime_governance commons_scalar_average_with_provenance(text, text, text) postgres
1559; 1255 4134946 FUNCTION runtime_governance commons_vector_mean(text, text, integer) postgres
1223; 1255 4134637 PROCEDURE runtime_governance gbim_bg_expansion_lifecycle() postgres
8933; 0 0 ACL runtime_governance PROCEDURE gbim_bg_expansion_lifecycle() postgres
1713; 1255 4134799 FUNCTION runtime_governance import_policy_set_audit(jsonb, text) postgres
1083; 1255 4134798 FUNCTION runtime_governance log_candidate_revision(text, text, text, text, text) postgres
1290; 1255 4134502 FUNCTION runtime_governance log_lifecycle_counts() postgres
1321; 1255 4134636 FUNCTION runtime_governance public_answer_packet(text, text) postgres
8934; 0 0 ACL runtime_governance FUNCTION public_answer_packet(p_geoid text, p_metric_name text) postgres
1112; 1255 4134640 FUNCTION runtime_governance public_geoid_panel(text) postgres
8935; 0 0 ACL runtime_governance FUNCTION public_geoid_panel(p_geoid text) postgres
1753; 1255 4134840 FUNCTION runtime_governance refresh_phi_domain_metrics() postgres
1264; 1255 4134501 FUNCTION runtime_governance refresh_public_admissible_gbim_mv() postgres
1027; 1255 4134852 FUNCTION runtime_governance run_recursive_self_assessment() postgres
749; 1259 4120139 SEQUENCE audit person_plane_access_log_id_seq postgres
8937; 0 0 SEQUENCE OWNED BY audit person_plane_access_log_id_seq postgres
8938; 0 0 ACL audit SEQUENCE person_plane_access_log_id_seq postgres
747; 1259 4120125 SEQUENCE governance person_plane_purpose_map_id_seq postgres
8940; 0 0 SEQUENCE OWNED BY governance person_plane_purpose_map_id_seq postgres
970; 1259 4134889 SEQUENCE identity biometric_audit_log_audit_id_seq postgres
8941; 0 0 SEQUENCE OWNED BY identity biometric_audit_log_audit_id_seq postgres
968; 1259 4134878 SEQUENCE identity biometric_consent_consent_id_seq postgres
8942; 0 0 SEQUENCE OWNED BY identity biometric_consent_consent_id_seq postgres
972; 1259 4134900 SEQUENCE identity biometric_template_template_id_seq postgres
8943; 0 0 SEQUENCE OWNED BY identity biometric_template_template_id_seq postgres
243; 1259 744110 SEQUENCE normalization geoanchor_record_id_seq2 postgres
245; 1259 744118 TABLE public gbim_active_collection msjarvis_admin
753; 1259 4120243 TABLE public gbim_active_collection_repoint_backup_20260721_203253 postgres
575; 1259 765899 TABLE public gbim_bg_coverage_area postgres
577; 1259 765917 TABLE public gbim_bg_coverage_counts postgres
576; 1259 765908 TABLE public gbim_bg_coverage_length postgres
593; 1259 910427 TABLE public gbim_bg_coverage_progress postgres
595; 1259 1123025 TABLE public gbim_bg_layer_role postgres
596; 1259 1123030 VIEW public gbim_blockgroup_belief_render_v2 postgres
579; 1259 765974 TABLE public gbim_blockgroup_coverage_bridge postgres
591; 1259 771886 VIEW public gbim_blockgroup_coverage_semantic postgres
582; 1259 767664 TABLE public gbim_blockgroup_vector postgres
583; 1259 769332 VIEW public gbim_blockgroup_embedding_source postgres
581; 1259 766017 TABLE public gbim_blockgroup_features postgres
585; 1259 769347 VIEW public gbim_blockgroup_numeric_features postgres
584; 1259 769341 TABLE public gbim_blockgroup_recreation_flags postgres
580; 1259 765981 TABLE public gbim_blockgroup_semantic_payload postgres
534; 1259 756428 TABLE public gbim_blockgroup_text_fragments postgres
741; 1259 1877595 TABLE public gbim_chroma_collection_feature_registry postgres
740; 1259 1877587 TABLE public gbim_chroma_collection_registry postgres
745; 1259 1877622 TABLE public gbim_chroma_publication_manifest postgres
752; 1259 4120238 TABLE public gbim_chroma_publication_manifest_repoint_backup_20260721_203253 postgres
246; 1259 744124 TABLE public gbim_collection_manifest msjarvis_admin
754; 1259 4120248 TABLE public gbim_collection_manifest_repoint_backup_20260721_203253 postgres
578; 1259 765959 TABLE public gbim_dataset_map postgres
594; 1259 910435 TABLE public gbim_layer_projection postgres
532; 1259 756414 TABLE public gbim_layer_registry postgres
932; 1259 4134386 TABLE public gbim_provenance postgres
574; 1259 765853 TABLE public gbim_registry postgres
573; 1259 765852 SEQUENCE public gbim_registry_gbim_id_seq postgres
8952; 0 0 SEQUENCE OWNED BY public gbim_registry_gbim_id_seq postgres
933; 1259 4134414 VIEW public gbim_response postgres
934; 1259 4134424 VIEW public gbim_response_envelope postgres
533; 1259 756423 VIEW public gbim_tract_layer_rollup postgres
746; 1259 1877630 TABLE public gbim_vertical_slice_acceptance_tests postgres
937; 1259 4134549 VIEW public public_admissible_gbim postgres
938; 1259 4134554 MATERIALIZED VIEW public public_admissible_gbim_mv postgres
248; 1259 744136 SEQUENCE public wv_atm_weather_stations_gid_seq postgres
8954; 0 0 SEQUENCE OWNED BY public wv_atm_weather_stations_gid_seq postgres
757; 1259 4123197 VIEW public wv_bg_base postgres
538; 1259 758444 SEQUENCE public wv_bio_biodiversity_rank_gid_seq msjarvis
8955; 0 0 SEQUENCE OWNED BY public wv_bio_biodiversity_rank_gid_seq msjarvis
587; 1259 769381 SEQUENCE public wv_bio_ecoregions_gid_seq postgres
8956; 0 0 SEQUENCE OWNED BY public wv_bio_ecoregions_gid_seq postgres
250; 1259 744154 SEQUENCE public wv_bio_red_spruce_cover_gid_seq postgres
8957; 0 0 SEQUENCE OWNED BY public wv_bio_red_spruce_cover_gid_seq postgres
597; 1259 1123044 VIEW public wv_blockgroup_belief_vector_ready postgres
739; 1259 1877576 VIEW public wv_blockgroup_belief_vector_ready_v1 postgres
8958; 0 0 COMMENT public VIEW wv_blockgroup_belief_vector_ready_v1 postgres
742; 1259 1877607 VIEW public wv_blockgroup_belief_vector_ready_with_chroma_hashes postgres
720; 1259 1127117 VIEW public wv_blockgroup_hazus_floodplains postgres
735; 1259 1876103 VIEW public wv_blockgroup_hazus_tax_summary postgres
252; 1259 744160 SEQUENCE public wv_bnd_appalachian_basin_boundary_gid_seq postgres
8959; 0 0 SEQUENCE OWNED BY public wv_bnd_appalachian_basin_boundary_gid_seq postgres
254; 1259 744166 SEQUENCE public wv_bnd_arc_counties_gid_seq postgres
8960; 0 0 SEQUENCE OWNED BY public wv_bnd_arc_counties_gid_seq postgres
256; 1259 744172 SEQUENCE public wv_bnd_canaan_valley_nwr_gid_seq postgres
8961; 0 0 SEQUENCE OWNED BY public wv_bnd_canaan_valley_nwr_gid_seq postgres
258; 1259 744178 SEQUENCE public wv_bnd_census_designated_places_gid_seq postgres
8962; 0 0 SEQUENCE OWNED BY public wv_bnd_census_designated_places_gid_seq postgres
260; 1259 744184 SEQUENCE public wv_bnd_county_24k_gid_seq postgres
8963; 0 0 SEQUENCE OWNED BY public wv_bnd_county_24k_gid_seq postgres
262; 1259 744190 SEQUENCE public wv_bnd_county_municipal_dlg_gid_seq postgres
8964; 0 0 SEQUENCE OWNED BY public wv_bnd_county_municipal_dlg_gid_seq postgres
264; 1259 744196 SEQUENCE public wv_bnd_mnf_basic_ownership_gid_seq postgres
8965; 0 0 SEQUENCE OWNED BY public wv_bnd_mnf_basic_ownership_gid_seq postgres
266; 1259 744202 SEQUENCE public wv_bnd_mnf_management_prescriptions_gid_seq postgres
8966; 0 0 SEQUENCE OWNED BY public wv_bnd_mnf_management_prescriptions_gid_seq postgres
268; 1259 744208 SEQUENCE public wv_bnd_mnf_ranger_districts_gid_seq postgres
8967; 0 0 SEQUENCE OWNED BY public wv_bnd_mnf_ranger_districts_gid_seq postgres
270; 1259 744214 SEQUENCE public wv_bnd_mnf_recreation_gid_seq postgres
8968; 0 0 SEQUENCE OWNED BY public wv_bnd_mnf_recreation_gid_seq postgres
272; 1259 744220 SEQUENCE public wv_bnd_mnf_recreation_sites_gid_seq postgres
8969; 0 0 SEQUENCE OWNED BY public wv_bnd_mnf_recreation_sites_gid_seq postgres
274; 1259 744226 SEQUENCE public wv_bnd_mnf_wilderness_gid_seq postgres
8970; 0 0 SEQUENCE OWNED BY public wv_bnd_mnf_wilderness_gid_seq postgres
276; 1259 744232 SEQUENCE public wv_bnd_morgantown_wards_gid_seq postgres
8971; 0 0 SEQUENCE OWNED BY public wv_bnd_morgantown_wards_gid_seq postgres
278; 1259 744238 SEQUENCE public wv_bnd_nhd_mussel_streams_gid_seq postgres
8972; 0 0 SEQUENCE OWNED BY public wv_bnd_nhd_mussel_streams_gid_seq postgres
280; 1259 744244 SEQUENCE public wv_bnd_public_lands_county_city_parks_gid_seq postgres
8973; 0 0 SEQUENCE OWNED BY public wv_bnd_public_lands_county_city_parks_gid_seq postgres
282; 1259 744250 SEQUENCE public wv_bnd_public_lands_national_forest_gid_seq postgres
8974; 0 0 SEQUENCE OWNED BY public wv_bnd_public_lands_national_forest_gid_seq postgres
284; 1259 744256 SEQUENCE public wv_bnd_public_lands_national_park_gid_seq postgres
8975; 0 0 SEQUENCE OWNED BY public wv_bnd_public_lands_national_park_gid_seq postgres
286; 1259 744262 SEQUENCE public wv_bnd_public_lands_nwr_gid_seq postgres
8976; 0 0 SEQUENCE OWNED BY public wv_bnd_public_lands_nwr_gid_seq postgres
288; 1259 744268 SEQUENCE public wv_bnd_public_lands_state_forests_gid_seq postgres
8977; 0 0 SEQUENCE OWNED BY public wv_bnd_public_lands_state_forests_gid_seq postgres
290; 1259 744274 SEQUENCE public wv_bnd_public_lands_state_parks_gid_seq postgres
8978; 0 0 SEQUENCE OWNED BY public wv_bnd_public_lands_state_parks_gid_seq postgres
292; 1259 744280 SEQUENCE public wv_bnd_public_lands_wildlife_resources_gid_seq postgres
8979; 0 0 SEQUENCE OWNED BY public wv_bnd_public_lands_wildlife_resources_gid_seq postgres
294; 1259 744286 SEQUENCE public wv_bnd_state_boundary_100k_gid_seq postgres
8980; 0 0 SEQUENCE OWNED BY public wv_bnd_state_boundary_100k_gid_seq postgres
296; 1259 744292 SEQUENCE public wv_bnd_voting_districts_2000_gid_seq postgres
8981; 0 0 SEQUENCE OWNED BY public wv_bnd_voting_districts_2000_gid_seq postgres
298; 1259 744298 SEQUENCE public wv_bnd_voting_districts_2002_gid_seq postgres
8982; 0 0 SEQUENCE OWNED BY public wv_bnd_voting_districts_2002_gid_seq postgres
300; 1259 744304 SEQUENCE public wv_bnd_workforce_investment_areas_gid_seq postgres
8983; 0 0 SEQUENCE OWNED BY public wv_bnd_workforce_investment_areas_gid_seq postgres
302; 1259 744310 SEQUENCE public wv_censustracts_census_2020_utm83_gid_seq postgres
8984; 0 0 SEQUENCE OWNED BY public wv_censustracts_census_2020_utm83_gid_seq postgres
308; 1259 744354 VIEW public wv_county_belief_vector_ready postgres
744; 1259 1877617 VIEW public wv_county_belief_vector_ready_with_chroma_hashes postgres
310; 1259 744364 SEQUENCE public wv_county_boundaries_24k_topo_updated_2026_utm83_gdb_gid_seq postgres
8985; 0 0 SEQUENCE OWNED BY public wv_county_boundaries_24k_topo_updated_2026_utm83_gdb_gid_seq postgres
312; 1259 744370 SEQUENCE public wv_county_boundaries_24k_topo_updated_2026_wma84_gdb_gid_seq postgres
8986; 0 0 SEQUENCE OWNED BY public wv_county_boundaries_24k_topo_updated_2026_wma84_gdb_gid_seq postgres
721; 1259 1127122 VIEW public wv_county_hazus_floodplain_summary postgres
315; 1259 744381 SEQUENCE public wv_eco_abandoned_mine_lands_line_gid_seq postgres
8987; 0 0 SEQUENCE OWNED BY public wv_eco_abandoned_mine_lands_line_gid_seq postgres
317; 1259 744387 SEQUENCE public wv_eco_abandoned_mine_lands_point_gid_seq postgres
8988; 0 0 SEQUENCE OWNED BY public wv_eco_abandoned_mine_lands_point_gid_seq postgres
319; 1259 744393 SEQUENCE public wv_eco_abandoned_mine_lands_polygon_gid_seq postgres
8989; 0 0 SEQUENCE OWNED BY public wv_eco_abandoned_mine_lands_polygon_gid_seq postgres
321; 1259 744399 SEQUENCE public wv_eco_coal_fields_gid_seq postgres
8990; 0 0 SEQUENCE OWNED BY public wv_eco_coal_fields_gid_seq postgres
323; 1259 744405 SEQUENCE public wv_eco_ezec_communities_gid_seq postgres
8991; 0 0 SEQUENCE OWNED BY public wv_eco_ezec_communities_gid_seq postgres
325; 1259 744411 SEQUENCE public wv_eco_industrial_sites_gid_seq postgres
8992; 0 0 SEQUENCE OWNED BY public wv_eco_industrial_sites_gid_seq postgres
327; 1259 744417 SEQUENCE public wv_eco_manufacturing_directory_gid_seq postgres
8993; 0 0 SEQUENCE OWNED BY public wv_eco_manufacturing_directory_gid_seq postgres
329; 1259 744423 SEQUENCE public wv_eco_mineral_operations_gid_seq postgres
8994; 0 0 SEQUENCE OWNED BY public wv_eco_mineral_operations_gid_seq postgres
331; 1259 744429 SEQUENCE public wv_eco_mountaintop_removal_gid_seq postgres
8995; 0 0 SEQUENCE OWNED BY public wv_eco_mountaintop_removal_gid_seq postgres
333; 1259 744435 SEQUENCE public wv_elv_summit_names_gid_seq postgres
8996; 0 0 SEQUENCE OWNED BY public wv_elv_summit_names_gid_seq postgres
336; 1259 744446 SEQUENCE public wv_env_air_nonattainment_gid_seq postgres
8997; 0 0 SEQUENCE OWNED BY public wv_env_air_nonattainment_gid_seq postgres
540; 1259 758450 SEQUENCE public wv_env_epa_facilities_gid_seq msjarvis
8998; 0 0 SEQUENCE OWNED BY public wv_env_epa_facilities_gid_seq msjarvis
338; 1259 744458 SEQUENCE public wv_env_timber_removal_volume_gid_seq postgres
8999; 0 0 SEQUENCE OWNED BY public wv_env_timber_removal_volume_gid_seq postgres
340; 1259 744464 SEQUENCE public wv_env_wildfire_regions_gid_seq postgres
9000; 0 0 SEQUENCE OWNED BY public wv_env_wildfire_regions_gid_seq postgres
342; 1259 744470 SEQUENCE public wv_env_wind_energy_resources_gid_seq postgres
9001; 0 0 SEQUENCE OWNED BY public wv_env_wind_energy_resources_gid_seq postgres
344; 1259 744476 SEQUENCE public wv_geo_coal_beds_gid_seq postgres
9002; 0 0 SEQUENCE OWNED BY public wv_geo_coal_beds_gid_seq postgres
346; 1259 744482 SEQUENCE public wv_geo_geological_map_generalized_gid_seq postgres
9003; 0 0 SEQUENCE OWNED BY public wv_geo_geological_map_generalized_gid_seq postgres
348; 1259 744488 SEQUENCE public wv_geo_karst_gid_seq postgres
9004; 0 0 SEQUENCE OWNED BY public wv_geo_karst_gid_seq postgres
350; 1259 744494 SEQUENCE public wv_hlt_health_providers_gid_seq postgres
9005; 0 0 SEQUENCE OWNED BY public wv_hlt_health_providers_gid_seq postgres
352; 1259 744500 SEQUENCE public wv_hlt_public_health_departments_gid_seq postgres
9006; 0 0 SEQUENCE OWNED BY public wv_hlt_public_health_departments_gid_seq postgres
354; 1259 744506 SEQUENCE public wv_hlt_rural_health_facilities_gid_seq postgres
9007; 0 0 SEQUENCE OWNED BY public wv_hlt_rural_health_facilities_gid_seq postgres
356; 1259 744512 SEQUENCE public wv_hyd_dams_dmr_gid_seq postgres
9008; 0 0 SEQUENCE OWNED BY public wv_hyd_dams_dmr_gid_seq postgres
358; 1259 744518 SEQUENCE public wv_hyd_dams_nid_gid_seq postgres
9009; 0 0 SEQUENCE OWNED BY public wv_hyd_dams_nid_gid_seq postgres
360; 1259 744524 SEQUENCE public wv_hyd_dams_noncoal_gid_seq postgres
9010; 0 0 SEQUENCE OWNED BY public wv_hyd_dams_noncoal_gid_seq postgres
536; 1259 757979 SEQUENCE public wv_hyd_hazus_floodplain_zones_gid_seq msjarvis
9011; 0 0 SEQUENCE OWNED BY public wv_hyd_hazus_floodplain_zones_gid_seq msjarvis
362; 1259 744536 SEQUENCE public wv_hyd_high_water_marks_gid_seq postgres
9012; 0 0 SEQUENCE OWNED BY public wv_hyd_high_water_marks_gid_seq postgres
364; 1259 744542 SEQUENCE public wv_hyd_navigable_waterways_gid_seq postgres
9013; 0 0 SEQUENCE OWNED BY public wv_hyd_navigable_waterways_gid_seq postgres
366; 1259 744548 SEQUENCE public wv_hyd_navigable_waterways_river_miles_gid_seq postgres
9014; 0 0 SEQUENCE OWNED BY public wv_hyd_navigable_waterways_river_miles_gid_seq postgres
368; 1259 744554 SEQUENCE public wv_hyd_navigable_waterways_structures_gid_seq postgres
9015; 0 0 SEQUENCE OWNED BY public wv_hyd_navigable_waterways_structures_gid_seq postgres
370; 1259 744560 SEQUENCE public wv_hyd_springs_100gpm_gid_seq postgres
9016; 0 0 SEQUENCE OWNED BY public wv_hyd_springs_100gpm_gid_seq postgres
372; 1259 744566 SEQUENCE public wv_hyd_streamflow_stations_gid_seq postgres
9017; 0 0 SEQUENCE OWNED BY public wv_hyd_streamflow_stations_gid_seq postgres
542; 1259 758456 SEQUENCE public wv_hyd_streams_high_quality_gid_seq msjarvis
9018; 0 0 SEQUENCE OWNED BY public wv_hyd_streams_high_quality_gid_seq msjarvis
374; 1259 744578 SEQUENCE public wv_hyd_streams_national_atlas_gid_seq postgres
9019; 0 0 SEQUENCE OWNED BY public wv_hyd_streams_national_atlas_gid_seq postgres
376; 1259 744584 SEQUENCE public wv_hyd_streams_tiger_gid_seq postgres
9020; 0 0 SEQUENCE OWNED BY public wv_hyd_streams_tiger_gid_seq postgres
378; 1259 744590 SEQUENCE public wv_hyd_watershed_boundary_11digit_gid_seq postgres
9021; 0 0 SEQUENCE OWNED BY public wv_hyd_watershed_boundary_11digit_gid_seq postgres
380; 1259 744596 SEQUENCE public wv_hyd_watershed_boundary_12digit_hu_gid_seq postgres
9022; 0 0 SEQUENCE OWNED BY public wv_hyd_watershed_boundary_12digit_hu_gid_seq postgres
382; 1259 744602 SEQUENCE public wv_hyd_watershed_boundary_8_10_12_gid_seq postgres
9023; 0 0 SEQUENCE OWNED BY public wv_hyd_watershed_boundary_8_10_12_gid_seq postgres
385; 1259 744614 SEQUENCE public wv_loc_census_urbanized_areas_gid_seq postgres
9024; 0 0 SEQUENCE OWNED BY public wv_loc_census_urbanized_areas_gid_seq postgres
387; 1259 744620 SEQUENCE public wv_loc_county_seats_gid_seq postgres
9025; 0 0 SEQUENCE OWNED BY public wv_loc_county_seats_gid_seq postgres
389; 1259 744626 SEQUENCE public wv_loc_geodetic_control_points_gid_seq postgres
9026; 0 0 SEQUENCE OWNED BY public wv_loc_geodetic_control_points_gid_seq postgres
391; 1259 744632 SEQUENCE public wv_loc_populated_places_census_gid_seq postgres
9027; 0 0 SEQUENCE OWNED BY public wv_loc_populated_places_census_gid_seq postgres
393; 1259 744638 SEQUENCE public wv_loc_sams2_address_road_centerlines_gid_seq postgres
9028; 0 0 SEQUENCE OWNED BY public wv_loc_sams2_address_road_centerlines_gid_seq postgres
395; 1259 744644 SEQUENCE public wv_mil_army_reserve_facilities_gid_seq postgres
9029; 0 0 SEQUENCE OWNED BY public wv_mil_army_reserve_facilities_gid_seq postgres
397; 1259 744650 SEQUENCE public wv_mil_national_guard_armories_gid_seq postgres
9030; 0 0 SEQUENCE OWNED BY public wv_mil_national_guard_armories_gid_seq postgres
399; 1259 744656 SEQUENCE public wv_plc_hazus_level1_gid_seq postgres
9031; 0 0 SEQUENCE OWNED BY public wv_plc_hazus_level1_gid_seq postgres
401; 1259 744662 SEQUENCE public wv_plc_regional_planning_councils_gid_seq postgres
9032; 0 0 SEQUENCE OWNED BY public wv_plc_regional_planning_councils_gid_seq postgres
403; 1259 744668 SEQUENCE public wv_plc_tax_district_boundaries_gid_seq postgres
9033; 0 0 SEQUENCE OWNED BY public wv_plc_tax_district_boundaries_gid_seq postgres
405; 1259 744674 SEQUENCE public wv_plc_tax_parcels_surface_mineral_gid_seq postgres
9034; 0 0 SEQUENCE OWNED BY public wv_plc_tax_parcels_surface_mineral_gid_seq postgres
569; 1259 764344 SEQUENCE public wv_rec_fishing_boating_access_ogc_fid_seq postgres
9035; 0 0 SEQUENCE OWNED BY public wv_rec_fishing_boating_access_ogc_fid_seq postgres
553; 1259 760284 SEQUENCE public wv_rec_fishing_lakes_ogc_fid_seq postgres
9036; 0 0 SEQUENCE OWNED BY public wv_rec_fishing_lakes_ogc_fid_seq postgres
557; 1259 760856 SEQUENCE public wv_rec_national_forest_ogc_fid_seq postgres
9037; 0 0 SEQUENCE OWNED BY public wv_rec_national_forest_ogc_fid_seq postgres
559; 1259 760898 SEQUENCE public wv_rec_nps_units_ogc_fid_seq postgres
9038; 0 0 SEQUENCE OWNED BY public wv_rec_nps_units_ogc_fid_seq postgres
561; 1259 760943 SEQUENCE public wv_rec_nwr_units_ogc_fid_seq postgres
9039; 0 0 SEQUENCE OWNED BY public wv_rec_nwr_units_ogc_fid_seq postgres
555; 1259 760807 SEQUENCE public wv_rec_state_forests_ogc_fid_seq postgres
9040; 0 0 SEQUENCE OWNED BY public wv_rec_state_forests_ogc_fid_seq postgres
551; 1259 760081 SEQUENCE public wv_rec_state_parks_ogc_fid_seq postgres
9041; 0 0 SEQUENCE OWNED BY public wv_rec_state_parks_ogc_fid_seq postgres
565; 1259 763982 SEQUENCE public wv_rec_trail_points_ogc_fid_seq postgres
9042; 0 0 SEQUENCE OWNED BY public wv_rec_trail_points_ogc_fid_seq postgres
563; 1259 760975 SEQUENCE public wv_rec_trails_ogc_fid_seq postgres
9043; 0 0 SEQUENCE OWNED BY public wv_rec_trails_ogc_fid_seq postgres
567; 1259 763992 SEQUENCE public wv_rec_whitewater_trails_ogc_fid_seq postgres
9044; 0 0 SEQUENCE OWNED BY public wv_rec_whitewater_trails_ogc_fid_seq postgres
571; 1259 764719 SEQUENCE public wv_rec_wvdnr_managed_lands_ogc_fid_seq postgres
9045; 0 0 SEQUENCE OWNED BY public wv_rec_wvdnr_managed_lands_ogc_fid_seq postgres
407; 1259 744680 SEQUENCE public wv_soc_911_centers_gid_seq postgres
9046; 0 0 SEQUENCE OWNED BY public wv_soc_911_centers_gid_seq postgres
409; 1259 744686 SEQUENCE public wv_soc_census_blockgroups_2020_gid_seq postgres
9047; 0 0 SEQUENCE OWNED BY public wv_soc_census_blockgroups_2020_gid_seq postgres
589; 1259 769407 SEQUENCE public wv_soc_census_blockgroups_2020_utm17_gid_seq postgres
9048; 0 0 SEQUENCE OWNED BY public wv_soc_census_blockgroups_2020_utm17_gid_seq postgres
411; 1259 744692 SEQUENCE public wv_soc_census_tracts_2020_gid_seq postgres
9049; 0 0 SEQUENCE OWNED BY public wv_soc_census_tracts_2020_gid_seq postgres
413; 1259 744698 SEQUENCE public wv_soc_cities_pop10k_gid_seq postgres
9050; 0 0 SEQUENCE OWNED BY public wv_soc_cities_pop10k_gid_seq postgres
415; 1259 744704 SEQUENCE public wv_soc_cities_pop2500_gid_seq postgres
9051; 0 0 SEQUENCE OWNED BY public wv_soc_cities_pop2500_gid_seq postgres
417; 1259 744710 SEQUENCE public wv_soc_communities_pop_change_gid_seq postgres
9052; 0 0 SEQUENCE OWNED BY public wv_soc_communities_pop_change_gid_seq postgres
419; 1259 744716 SEQUENCE public wv_soc_courthouses_county_gid_seq postgres
9053; 0 0 SEQUENCE OWNED BY public wv_soc_courthouses_county_gid_seq postgres
421; 1259 744722 SEQUENCE public wv_soc_courthouses_federal_gid_seq postgres
9054; 0 0 SEQUENCE OWNED BY public wv_soc_courthouses_federal_gid_seq postgres
423; 1259 744728 SEQUENCE public wv_soc_fish_hatcheries_gid_seq postgres
9055; 0 0 SEQUENCE OWNED BY public wv_soc_fish_hatcheries_gid_seq postgres
425; 1259 744734 SEQUENCE public wv_soc_fishing_boating_access_gid_seq postgres
9056; 0 0 SEQUENCE OWNED BY public wv_soc_fishing_boating_access_gid_seq postgres
427; 1259 744740 SEQUENCE public wv_soc_fishing_lakes_gid_seq postgres
9057; 0 0 SEQUENCE OWNED BY public wv_soc_fishing_lakes_gid_seq postgres
429; 1259 744746 SEQUENCE public wv_soc_higher_ed_facilities_gid_seq postgres
9058; 0 0 SEQUENCE OWNED BY public wv_soc_higher_ed_facilities_gid_seq postgres
544; 1259 758462 SEQUENCE public wv_soc_hospitals_wvdem_gid_seq msjarvis
9059; 0 0 SEQUENCE OWNED BY public wv_soc_hospitals_wvdem_gid_seq msjarvis
431; 1259 744758 SEQUENCE public wv_soc_libraries_gid_seq postgres
9060; 0 0 SEQUENCE OWNED BY public wv_soc_libraries_gid_seq postgres
433; 1259 744764 SEQUENCE public wv_soc_national_register_historic_points_gid_seq postgres
9061; 0 0 SEQUENCE OWNED BY public wv_soc_national_register_historic_points_gid_seq postgres
435; 1259 744770 SEQUENCE public wv_soc_national_register_historic_polygons_gid_seq postgres
9062; 0 0 SEQUENCE OWNED BY public wv_soc_national_register_historic_polygons_gid_seq postgres
437; 1259 744776 SEQUENCE public wv_soc_nursing_homes_gid_seq postgres
9063; 0 0 SEQUENCE OWNED BY public wv_soc_nursing_homes_gid_seq postgres
439; 1259 744782 SEQUENCE public wv_soc_places_of_worship_wvgistc_gid_seq postgres
9064; 0 0 SEQUENCE OWNED BY public wv_soc_places_of_worship_wvgistc_gid_seq postgres
441; 1259 744788 SEQUENCE public wv_soc_population_by_decade_gid_seq postgres
9065; 0 0 SEQUENCE OWNED BY public wv_soc_population_by_decade_gid_seq postgres
546; 1259 758469 SEQUENCE public wv_soc_schools_k12_gid_seq msjarvis
9066; 0 0 SEQUENCE OWNED BY public wv_soc_schools_k12_gid_seq msjarvis
443; 1259 744801 SEQUENCE public wv_soc_towers_am_gid_seq postgres
9067; 0 0 SEQUENCE OWNED BY public wv_soc_towers_am_gid_seq postgres
445; 1259 744807 SEQUENCE public wv_soc_towers_asr_gid_seq postgres
9068; 0 0 SEQUENCE OWNED BY public wv_soc_towers_asr_gid_seq postgres
447; 1259 744813 SEQUENCE public wv_soc_towers_cellular_gid_seq postgres
9069; 0 0 SEQUENCE OWNED BY public wv_soc_towers_cellular_gid_seq postgres
449; 1259 744819 SEQUENCE public wv_soc_towers_fm_gid_seq postgres
9070; 0 0 SEQUENCE OWNED BY public wv_soc_towers_fm_gid_seq postgres
451; 1259 744825 SEQUENCE public wv_soc_towers_microwave_gid_seq postgres
9071; 0 0 SEQUENCE OWNED BY public wv_soc_towers_microwave_gid_seq postgres
453; 1259 744831 SEQUENCE public wv_soc_towers_pager_gid_seq postgres
9072; 0 0 SEQUENCE OWNED BY public wv_soc_towers_pager_gid_seq postgres
455; 1259 744837 SEQUENCE public wv_soc_towers_private_gid_seq postgres
9073; 0 0 SEQUENCE OWNED BY public wv_soc_towers_private_gid_seq postgres
457; 1259 744843 SEQUENCE public wv_soc_towers_tv_gid_seq postgres
9074; 0 0 SEQUENCE OWNED BY public wv_soc_towers_tv_gid_seq postgres
459; 1259 744849 SEQUENCE public wv_soc_va_facilities_gid_seq postgres
9075; 0 0 SEQUENCE OWNED BY public wv_soc_va_facilities_gid_seq postgres
461; 1259 744855 SEQUENCE public wv_soc_zcta_2020_gid_seq postgres
9076; 0 0 SEQUENCE OWNED BY public wv_soc_zcta_2020_gid_seq postgres
463; 1259 744861 SEQUENCE public wv_str_bridges_gid_seq postgres
9077; 0 0 SEQUENCE OWNED BY public wv_str_bridges_gid_seq postgres
465; 1259 744867 SEQUENCE public wv_str_correctional_institutions_gid_seq postgres
9078; 0 0 SEQUENCE OWNED BY public wv_str_correctional_institutions_gid_seq postgres
467; 1259 744873 SEQUENCE public wv_str_flood_atrisk_structures_gid_seq postgres
9079; 0 0 SEQUENCE OWNED BY public wv_str_flood_atrisk_structures_gid_seq postgres
469; 1259 744879 SEQUENCE public wv_str_parole_offices_gid_seq postgres
9080; 0 0 SEQUENCE OWNED BY public wv_str_parole_offices_gid_seq postgres
471; 1259 744885 SEQUENCE public wv_str_places_of_worship_hsip_gid_seq postgres
9081; 0 0 SEQUENCE OWNED BY public wv_str_places_of_worship_hsip_gid_seq postgres
473; 1259 744891 SEQUENCE public wv_str_samb_building_points_gid_seq postgres
9082; 0 0 SEQUENCE OWNED BY public wv_str_samb_building_points_gid_seq postgres
475; 1259 744897 SEQUENCE public wv_str_samb_building_polygons_gid_seq postgres
9083; 0 0 SEQUENCE OWNED BY public wv_str_samb_building_polygons_gid_seq postgres
531; 1259 756398 VIEW public wv_tract_address_points_coverage_statewide postgres
480; 1259 744926 VIEW public wv_tract_belief_vector_ready postgres
743; 1259 1877612 VIEW public wv_tract_belief_vector_ready_with_chroma_hashes postgres
483; 1259 744941 SEQUENCE public wv_trn_airport_facilities_gid_seq postgres
9084; 0 0 SEQUENCE OWNED BY public wv_trn_airport_facilities_gid_seq postgres
485; 1259 744947 SEQUENCE public wv_trn_airport_proposed_gid_seq postgres
9085; 0 0 SEQUENCE OWNED BY public wv_trn_airport_proposed_gid_seq postgres
487; 1259 744953 SEQUENCE public wv_trn_airport_runways_gid_seq postgres
9086; 0 0 SEQUENCE OWNED BY public wv_trn_airport_runways_gid_seq postgres
548; 1259 758475 SEQUENCE public wv_trn_airports_gid_seq msjarvis
9087; 0 0 SEQUENCE OWNED BY public wv_trn_airports_gid_seq msjarvis
489; 1259 744965 SEQUENCE public wv_trn_intermodal_terminals_gid_seq postgres
9088; 0 0 SEQUENCE OWNED BY public wv_trn_intermodal_terminals_gid_seq postgres
491; 1259 744971 SEQUENCE public wv_trn_mnf_recreation_trails_gid_seq postgres
9089; 0 0 SEQUENCE OWNED BY public wv_trn_mnf_recreation_trails_gid_seq postgres
493; 1259 744977 SEQUENCE public wv_trn_mnf_roads_gid_seq postgres
9090; 0 0 SEQUENCE OWNED BY public wv_trn_mnf_roads_gid_seq postgres
495; 1259 744983 SEQUENCE public wv_trn_railroad_lines_rti_gid_seq postgres
9091; 0 0 SEQUENCE OWNED BY public wv_trn_railroad_lines_rti_gid_seq postgres
497; 1259 744989 SEQUENCE public wv_trn_railroads_amtrak_gid_seq postgres
9092; 0 0 SEQUENCE OWNED BY public wv_trn_railroads_amtrak_gid_seq postgres
499; 1259 744995 SEQUENCE public wv_trn_railroads_excursion_gid_seq postgres
9093; 0 0 SEQUENCE OWNED BY public wv_trn_railroads_excursion_gid_seq postgres
501; 1259 745001 SEQUENCE public wv_trn_railroads_national_network_gid_seq postgres
9094; 0 0 SEQUENCE OWNED BY public wv_trn_railroads_national_network_gid_seq postgres
503; 1259 745007 SEQUENCE public wv_trn_recreational_trails_gid_seq postgres
9095; 0 0 SEQUENCE OWNED BY public wv_trn_recreational_trails_gid_seq postgres
505; 1259 745013 SEQUENCE public wv_trn_roads_interstate_gid_seq postgres
9096; 0 0 SEQUENCE OWNED BY public wv_trn_roads_interstate_gid_seq postgres
507; 1259 745019 SEQUENCE public wv_trn_roads_major_4800_gid_seq postgres
9097; 0 0 SEQUENCE OWNED BY public wv_trn_roads_major_4800_gid_seq postgres
509; 1259 745025 SEQUENCE public wv_trn_roads_state_routes_gid_seq postgres
9098; 0 0 SEQUENCE OWNED BY public wv_trn_roads_state_routes_gid_seq postgres
511; 1259 745031 SEQUENCE public wv_trn_roads_us_highways_gid_seq postgres
9099; 0 0 SEQUENCE OWNED BY public wv_trn_roads_us_highways_gid_seq postgres
513; 1259 745037 SEQUENCE public wv_trn_roads_us_routes_gid_seq postgres
9100; 0 0 SEQUENCE OWNED BY public wv_trn_roads_us_routes_gid_seq postgres
515; 1259 745043 SEQUENCE public wv_trn_whitewater_trails_gid_seq postgres
9101; 0 0 SEQUENCE OWNED BY public wv_trn_whitewater_trails_gid_seq postgres
550; 1259 758481 SEQUENCE public wv_util_sewer_treatment_plants_gid_seq msjarvis
9102; 0 0 SEQUENCE OWNED BY public wv_util_sewer_treatment_plants_gid_seq msjarvis
517; 1259 745055 SEQUENCE public wv_util_solid_waste_facilities_gid_seq postgres
9103; 0 0 SEQUENCE OWNED BY public wv_util_solid_waste_facilities_gid_seq postgres
518; 1259 745056 SEQUENCE public wv_wv_county_boundaries_24k_topo_updated_2026_utm83_gid_seq postgres
9104; 0 0 SEQUENCE OWNED BY public wv_wv_county_boundaries_24k_topo_updated_2026_utm83_gid_seq postgres
520; 1259 745062 SEQUENCE public wv_wv_county_boundaries_24k_topo_updated_2026_wma84_gid_seq postgres
9105; 0 0 SEQUENCE OWNED BY public wv_wv_county_boundaries_24k_topo_updated_2026_wma84_gid_seq postgres
944; 1259 4134651 TABLE runtime_governance civic_policy_audit postgres
943; 1259 4134642 TABLE runtime_governance civic_policy_fact postgres
945; 1259 4134660 VIEW runtime_governance civic_policy_fact_current postgres
976; 1259 4134923 TABLE runtime_governance commons_contribution postgres
975; 1259 4134922 SEQUENCE runtime_governance commons_contribution_contribution_id_seq postgres
9106; 0 0 SEQUENCE OWNED BY runtime_governance commons_contribution_contribution_id_seq postgres
974; 1259 4134914 TABLE runtime_governance commons_k_threshold_policy postgres
981; 1259 4134960 TABLE runtime_governance commons_noninvertibility_policy postgres
957; 1259 4134790 TABLE runtime_governance commons_phase_status postgres
980; 1259 4134948 TABLE runtime_governance commons_provenance_certificate postgres
979; 1259 4134947 SEQUENCE runtime_governance commons_provenance_certificate_certificate_id_seq postgres
9107; 0 0 SEQUENCE OWNED BY runtime_governance commons_provenance_certificate_certificate_id_seq postgres
985; 1259 4134992 TABLE runtime_governance commons_reconstruction_attempt postgres
984; 1259 4134991 SEQUENCE runtime_governance commons_reconstruction_attempt_attempt_id_seq postgres
9108; 0 0 SEQUENCE OWNED BY runtime_governance commons_reconstruction_attempt_attempt_id_seq postgres
978; 1259 4134936 TABLE runtime_governance commons_vector_contribution postgres
977; 1259 4134935 SEQUENCE runtime_governance commons_vector_contribution_vector_id_seq postgres
9109; 0 0 SEQUENCE OWNED BY runtime_governance commons_vector_contribution_vector_id_seq postgres
947; 1259 4134673 TABLE runtime_governance epistemic_loop_metrics postgres
946; 1259 4134664 TABLE runtime_governance epistemic_revision_log postgres
964; 1259 4134842 TABLE runtime_governance epistemic_self_assessment postgres
963; 1259 4134841 SEQUENCE runtime_governance epistemic_self_assessment_assessment_id_seq postgres
9110; 0 0 SEQUENCE OWNED BY runtime_governance epistemic_self_assessment_assessment_id_seq postgres
956; 1259 4134760 TABLE runtime_governance geo_guard_city postgres
960; 1259 4134810 TABLE runtime_governance geo_guard_config postgres
948; 1259 4134681 TABLE runtime_governance out_of_state_city postgres
959; 1259 4134801 TABLE runtime_governance phi_baseline_metrics postgres
958; 1259 4134800 SEQUENCE runtime_governance phi_baseline_metrics_metrics_id_seq postgres
9111; 0 0 SEQUENCE OWNED BY runtime_governance phi_baseline_metrics_metrics_id_seq postgres
962; 1259 4134830 TABLE runtime_governance phi_domain_metrics postgres
961; 1259 4134829 SEQUENCE runtime_governance phi_domain_metrics_metrics_id_seq postgres
9112; 0 0 SEQUENCE OWNED BY runtime_governance phi_domain_metrics_metrics_id_seq postgres
955; 1259 4134751 TABLE runtime_governance policy_set_audit postgres
954; 1259 4134750 SEQUENCE runtime_governance policy_set_audit_audit_id_seq postgres
9113; 0 0 SEQUENCE OWNED BY runtime_governance policy_set_audit_audit_id_seq postgres
936; 1259 4134491 TABLE runtime_governance public_answer_audit postgres
9114; 0 0 ACL runtime_governance TABLE public_answer_audit postgres
935; 1259 4134490 SEQUENCE runtime_governance public_answer_audit_audit_id_seq postgres
9115; 0 0 SEQUENCE OWNED BY runtime_governance public_answer_audit_audit_id_seq postgres
983; 1259 4134971 TABLE runtime_governance user_partition_registry postgres
982; 1259 4134970 SEQUENCE runtime_governance user_partition_registry_partition_id_seq postgres
9116; 0 0 SEQUENCE OWNED BY runtime_governance user_partition_registry_partition_id_seq postgres
598; 1259 1125550 SEQUENCE staging_hazus barbour_objectid_seq postgres
9117; 0 0 SEQUENCE OWNED BY staging_hazus barbour_objectid_seq postgres
602; 1259 1125577 SEQUENCE staging_hazus berkeley_objectid_seq postgres
9118; 0 0 SEQUENCE OWNED BY staging_hazus berkeley_objectid_seq postgres
600; 1259 1125560 SEQUENCE staging_hazus boone_objectid_seq postgres
9119; 0 0 SEQUENCE OWNED BY staging_hazus boone_objectid_seq postgres
604; 1259 1125587 SEQUENCE staging_hazus braxton_objectid_seq postgres
9120; 0 0 SEQUENCE OWNED BY staging_hazus braxton_objectid_seq postgres
606; 1259 1125597 SEQUENCE staging_hazus brooke_objectid_seq postgres
9121; 0 0 SEQUENCE OWNED BY staging_hazus brooke_objectid_seq postgres
608; 1259 1125607 SEQUENCE staging_hazus cabell_objectid_seq postgres
9122; 0 0 SEQUENCE OWNED BY staging_hazus cabell_objectid_seq postgres
610; 1259 1125617 SEQUENCE staging_hazus calhoun_objectid_seq postgres
9123; 0 0 SEQUENCE OWNED BY staging_hazus calhoun_objectid_seq postgres
612; 1259 1125627 SEQUENCE staging_hazus clay_objectid_seq postgres
9124; 0 0 SEQUENCE OWNED BY staging_hazus clay_objectid_seq postgres
614; 1259 1125638 SEQUENCE staging_hazus doddridge_objectid_seq postgres
9125; 0 0 SEQUENCE OWNED BY staging_hazus doddridge_objectid_seq postgres
616; 1259 1125648 SEQUENCE staging_hazus fayette_objectid_seq postgres
9126; 0 0 SEQUENCE OWNED BY staging_hazus fayette_objectid_seq postgres
710; 1259 1126263 SEQUENCE staging_hazus floodplain_100year_objectid_seq postgres
9127; 0 0 SEQUENCE OWNED BY staging_hazus floodplain_100year_objectid_seq postgres
708; 1259 1126198 SEQUENCE staging_hazus floodplain_10year_objectid_seq postgres
9128; 0 0 SEQUENCE OWNED BY staging_hazus floodplain_10year_objectid_seq postgres
712; 1259 1126328 SEQUENCE staging_hazus floodplain_25year_objectid_seq postgres
9129; 0 0 SEQUENCE OWNED BY staging_hazus floodplain_25year_objectid_seq postgres
714; 1259 1126393 SEQUENCE staging_hazus floodplain_50year_objectid_seq postgres
9130; 0 0 SEQUENCE OWNED BY staging_hazus floodplain_50year_objectid_seq postgres
618; 1259 1125663 SEQUENCE staging_hazus gilmer_objectid_seq postgres
9131; 0 0 SEQUENCE OWNED BY staging_hazus gilmer_objectid_seq postgres
620; 1259 1125673 SEQUENCE staging_hazus grant_objectid_seq postgres
9132; 0 0 SEQUENCE OWNED BY staging_hazus grant_objectid_seq postgres
622; 1259 1125683 SEQUENCE staging_hazus greenbrier_objectid_seq postgres
9133; 0 0 SEQUENCE OWNED BY staging_hazus greenbrier_objectid_seq postgres
696; 1259 1126137 SEQUENCE staging_hazus hampshire_objectid_seq postgres
9134; 0 0 SEQUENCE OWNED BY staging_hazus hampshire_objectid_seq postgres
624; 1259 1125700 SEQUENCE staging_hazus hancock_objectid_seq postgres
9135; 0 0 SEQUENCE OWNED BY staging_hazus hancock_objectid_seq postgres
626; 1259 1125710 SEQUENCE staging_hazus hardy_objectid_seq postgres
9136; 0 0 SEQUENCE OWNED BY staging_hazus hardy_objectid_seq postgres
628; 1259 1125723 SEQUENCE staging_hazus harrison_objectid_seq postgres
9137; 0 0 SEQUENCE OWNED BY staging_hazus harrison_objectid_seq postgres
630; 1259 1125733 SEQUENCE staging_hazus jackson_objectid_seq postgres
9138; 0 0 SEQUENCE OWNED BY staging_hazus jackson_objectid_seq postgres
632; 1259 1125743 SEQUENCE staging_hazus jefferson_objectid_seq postgres
9139; 0 0 SEQUENCE OWNED BY staging_hazus jefferson_objectid_seq postgres
634; 1259 1125753 SEQUENCE staging_hazus kanawha_objectid_seq postgres
9140; 0 0 SEQUENCE OWNED BY staging_hazus kanawha_objectid_seq postgres
636; 1259 1125765 SEQUENCE staging_hazus lewis_objectid_seq postgres
9141; 0 0 SEQUENCE OWNED BY staging_hazus lewis_objectid_seq postgres
638; 1259 1125775 SEQUENCE staging_hazus lincoln_objectid_seq postgres
9142; 0 0 SEQUENCE OWNED BY staging_hazus lincoln_objectid_seq postgres
640; 1259 1125785 SEQUENCE staging_hazus logan_objectid_seq postgres
9143; 0 0 SEQUENCE OWNED BY staging_hazus logan_objectid_seq postgres
698; 1259 1126148 SEQUENCE staging_hazus marion_objectid_seq postgres
9144; 0 0 SEQUENCE OWNED BY staging_hazus marion_objectid_seq postgres
642; 1259 1125798 SEQUENCE staging_hazus marshall_objectid_seq postgres
9145; 0 0 SEQUENCE OWNED BY staging_hazus marshall_objectid_seq postgres
644; 1259 1125808 SEQUENCE staging_hazus mason_objectid_seq postgres
9146; 0 0 SEQUENCE OWNED BY staging_hazus mason_objectid_seq postgres
646; 1259 1125818 SEQUENCE staging_hazus mcdowell_objectid_seq postgres
9147; 0 0 SEQUENCE OWNED BY staging_hazus mcdowell_objectid_seq postgres
648; 1259 1125834 SEQUENCE staging_hazus mercer_objectid_seq postgres
9148; 0 0 SEQUENCE OWNED BY staging_hazus mercer_objectid_seq postgres
700; 1259 1126158 SEQUENCE staging_hazus mineral_objectid_seq postgres
9149; 0 0 SEQUENCE OWNED BY staging_hazus mineral_objectid_seq postgres
650; 1259 1125844 SEQUENCE staging_hazus mingo_objectid_seq postgres
9150; 0 0 SEQUENCE OWNED BY staging_hazus mingo_objectid_seq postgres
702; 1259 1126168 SEQUENCE staging_hazus monongalia_objectid_seq postgres
9151; 0 0 SEQUENCE OWNED BY staging_hazus monongalia_objectid_seq postgres
652; 1259 1125858 SEQUENCE staging_hazus monroe_objectid_seq postgres
9152; 0 0 SEQUENCE OWNED BY staging_hazus monroe_objectid_seq postgres
654; 1259 1125868 SEQUENCE staging_hazus morgan_objectid_seq postgres
9153; 0 0 SEQUENCE OWNED BY staging_hazus morgan_objectid_seq postgres
656; 1259 1125878 SEQUENCE staging_hazus nicholas_objectid_seq postgres
9154; 0 0 SEQUENCE OWNED BY staging_hazus nicholas_objectid_seq postgres
658; 1259 1125889 SEQUENCE staging_hazus ohio_objectid_seq postgres
9155; 0 0 SEQUENCE OWNED BY staging_hazus ohio_objectid_seq postgres
660; 1259 1125899 SEQUENCE staging_hazus pendleton_objectid_seq postgres
9156; 0 0 SEQUENCE OWNED BY staging_hazus pendleton_objectid_seq postgres
662; 1259 1125917 SEQUENCE staging_hazus pleasants_objectid_seq postgres
9157; 0 0 SEQUENCE OWNED BY staging_hazus pleasants_objectid_seq postgres
664; 1259 1125927 SEQUENCE staging_hazus pocahontas_objectid_seq postgres
9158; 0 0 SEQUENCE OWNED BY staging_hazus pocahontas_objectid_seq postgres
704; 1259 1126178 SEQUENCE staging_hazus preston_objectid_seq postgres
9159; 0 0 SEQUENCE OWNED BY staging_hazus preston_objectid_seq postgres
666; 1259 1125949 SEQUENCE staging_hazus putnam_objectid_seq postgres
9160; 0 0 SEQUENCE OWNED BY staging_hazus putnam_objectid_seq postgres
668; 1259 1125960 SEQUENCE staging_hazus raleigh_objectid_seq postgres
9161; 0 0 SEQUENCE OWNED BY staging_hazus raleigh_objectid_seq postgres
670; 1259 1125988 SEQUENCE staging_hazus randolph_objectid_seq postgres
9162; 0 0 SEQUENCE OWNED BY staging_hazus randolph_objectid_seq postgres
672; 1259 1126003 SEQUENCE staging_hazus ritchie_objectid_seq postgres
9163; 0 0 SEQUENCE OWNED BY staging_hazus ritchie_objectid_seq postgres
674; 1259 1126013 SEQUENCE staging_hazus roane_objectid_seq postgres
9164; 0 0 SEQUENCE OWNED BY staging_hazus roane_objectid_seq postgres
676; 1259 1126023 SEQUENCE staging_hazus summers_objectid_seq postgres
9165; 0 0 SEQUENCE OWNED BY staging_hazus summers_objectid_seq postgres
678; 1259 1126035 SEQUENCE staging_hazus taylor_objectid_seq postgres
9166; 0 0 SEQUENCE OWNED BY staging_hazus taylor_objectid_seq postgres
680; 1259 1126045 SEQUENCE staging_hazus tucker_objectid_seq postgres
9167; 0 0 SEQUENCE OWNED BY staging_hazus tucker_objectid_seq postgres
682; 1259 1126057 SEQUENCE staging_hazus tyler_objectid_seq postgres
9168; 0 0 SEQUENCE OWNED BY staging_hazus tyler_objectid_seq postgres
684; 1259 1126067 SEQUENCE staging_hazus upshur_objectid_seq postgres
9169; 0 0 SEQUENCE OWNED BY staging_hazus upshur_objectid_seq postgres
686; 1259 1126077 SEQUENCE staging_hazus wayne_objectid_seq postgres
9170; 0 0 SEQUENCE OWNED BY staging_hazus wayne_objectid_seq postgres
688; 1259 1126088 SEQUENCE staging_hazus webster_objectid_seq postgres
9171; 0 0 SEQUENCE OWNED BY staging_hazus webster_objectid_seq postgres
706; 1259 1126188 SEQUENCE staging_hazus wetzel_objectid_seq postgres
9172; 0 0 SEQUENCE OWNED BY staging_hazus wetzel_objectid_seq postgres
690; 1259 1126101 SEQUENCE staging_hazus wirt_objectid_seq postgres
9173; 0 0 SEQUENCE OWNED BY staging_hazus wirt_objectid_seq postgres
692; 1259 1126111 SEQUENCE staging_hazus wood_objectid_seq postgres
9174; 0 0 SEQUENCE OWNED BY staging_hazus wood_objectid_seq postgres
694; 1259 1126121 SEQUENCE staging_hazus wyoming_objectid_seq postgres
9175; 0 0 SEQUENCE OWNED BY staging_hazus wyoming_objectid_seq postgres
722; 1259 1127128 SEQUENCE staging_tax_2025 mastersurfwv_2025_objectid_seq postgres
9176; 0 0 SEQUENCE OWNED BY staging_tax_2025 mastersurfwv_2025_objectid_seq postgres
724; 1259 1405238 SEQUENCE staging_tax_2025 parcelsummary_ogc_fid_seq postgres
9177; 0 0 SEQUENCE OWNED BY staging_tax_2025 parcelsummary_ogc_fid_seq postgres
729; 1259 1872962 SEQUENCE staging_tax_districts wv_tax_districts_ll83_objectid_1_seq postgres
9178; 0 0 SEQUENCE OWNED BY staging_tax_districts wv_tax_districts_ll83_objectid_1_seq postgres
727; 1259 1872093 SEQUENCE staging_tax_districts wv_tax_districts_utm83_objectid_1_seq postgres
9179; 0 0 SEQUENCE OWNED BY staging_tax_districts wv_tax_districts_utm83_objectid_1_seq postgres
731; 1259 1873831 SEQUENCE staging_tax_districts wv_tax_districts_wma84_objectid_1_seq postgres
9180; 0 0 SEQUENCE OWNED BY staging_tax_districts wv_tax_districts_wma84_objectid_1_seq postgres
6842; 2604 4134926 DEFAULT runtime_governance commons_contribution contribution_id postgres
6846; 2604 4134951 DEFAULT runtime_governance commons_provenance_certificate certificate_id postgres
6851; 2604 4134995 DEFAULT runtime_governance commons_reconstruction_attempt attempt_id postgres
6844; 2604 4134939 DEFAULT runtime_governance commons_vector_contribution vector_id postgres
6829; 2604 4134845 DEFAULT runtime_governance epistemic_self_assessment assessment_id postgres
6824; 2604 4134804 DEFAULT runtime_governance phi_baseline_metrics metrics_id postgres
6827; 2604 4134833 DEFAULT runtime_governance phi_domain_metrics metrics_id postgres
6821; 2604 4134754 DEFAULT runtime_governance policy_set_audit audit_id postgres
6794; 2604 4134494 DEFAULT runtime_governance public_answer_audit audit_id postgres
6849; 2604 4134974 DEFAULT runtime_governance user_partition_registry partition_id postgres
8873; 0 4134651 TABLE DATA runtime_governance civic_policy_audit postgres
8872; 0 4134642 TABLE DATA runtime_governance civic_policy_fact postgres
8904; 0 4134923 TABLE DATA runtime_governance commons_contribution postgres
8902; 0 4134914 TABLE DATA runtime_governance commons_k_threshold_policy postgres
8909; 0 4134960 TABLE DATA runtime_governance commons_noninvertibility_policy postgres
8885; 0 4134790 TABLE DATA runtime_governance commons_phase_status postgres
8908; 0 4134948 TABLE DATA runtime_governance commons_provenance_certificate postgres
8913; 0 4134992 TABLE DATA runtime_governance commons_reconstruction_attempt postgres
8906; 0 4134936 TABLE DATA runtime_governance commons_vector_contribution postgres
8875; 0 4134673 TABLE DATA runtime_governance epistemic_loop_metrics postgres
8874; 0 4134664 TABLE DATA runtime_governance epistemic_revision_log postgres
8892; 0 4134842 TABLE DATA runtime_governance epistemic_self_assessment postgres
8884; 0 4134760 TABLE DATA runtime_governance geo_guard_city postgres
8888; 0 4134810 TABLE DATA runtime_governance geo_guard_config postgres
8876; 0 4134681 TABLE DATA runtime_governance out_of_state_city postgres
8887; 0 4134801 TABLE DATA runtime_governance phi_baseline_metrics postgres
8890; 0 4134830 TABLE DATA runtime_governance phi_domain_metrics postgres
8883; 0 4134751 TABLE DATA runtime_governance policy_set_audit postgres
8870; 0 4134491 TABLE DATA runtime_governance public_answer_audit postgres
8911; 0 4134971 TABLE DATA runtime_governance user_partition_registry postgres
9181; 0 0 SEQUENCE SET audit person_plane_access_log_id_seq postgres
9182; 0 0 SEQUENCE SET cron jobid_seq postgres
9183; 0 0 SEQUENCE SET cron runid_seq postgres
9184; 0 0 SEQUENCE SET governance person_plane_purpose_map_id_seq postgres
9185; 0 0 SEQUENCE SET identity biometric_audit_log_audit_id_seq postgres
9186; 0 0 SEQUENCE SET identity biometric_consent_consent_id_seq postgres
9187; 0 0 SEQUENCE SET identity biometric_template_template_id_seq postgres
9188; 0 0 SEQUENCE SET normalization geoanchor_record_id_seq2 postgres
9189; 0 0 SEQUENCE SET public gbim_registry_gbim_id_seq postgres
9190; 0 0 SEQUENCE SET public wv_atm_weather_stations_gid_seq postgres
9191; 0 0 SEQUENCE SET public wv_bio_biodiversity_rank_gid_seq msjarvis
9192; 0 0 SEQUENCE SET public wv_bio_ecoregions_gid_seq postgres
9193; 0 0 SEQUENCE SET public wv_bio_red_spruce_cover_gid_seq postgres
9194; 0 0 SEQUENCE SET public wv_bnd_appalachian_basin_boundary_gid_seq postgres
9195; 0 0 SEQUENCE SET public wv_bnd_arc_counties_gid_seq postgres
9196; 0 0 SEQUENCE SET public wv_bnd_canaan_valley_nwr_gid_seq postgres
9197; 0 0 SEQUENCE SET public wv_bnd_census_designated_places_gid_seq postgres
9198; 0 0 SEQUENCE SET public wv_bnd_county_24k_gid_seq postgres
9199; 0 0 SEQUENCE SET public wv_bnd_county_municipal_dlg_gid_seq postgres
9200; 0 0 SEQUENCE SET public wv_bnd_mnf_basic_ownership_gid_seq postgres
9201; 0 0 SEQUENCE SET public wv_bnd_mnf_management_prescriptions_gid_seq postgres
9202; 0 0 SEQUENCE SET public wv_bnd_mnf_ranger_districts_gid_seq postgres
9203; 0 0 SEQUENCE SET public wv_bnd_mnf_recreation_gid_seq postgres
9204; 0 0 SEQUENCE SET public wv_bnd_mnf_recreation_sites_gid_seq postgres
9205; 0 0 SEQUENCE SET public wv_bnd_mnf_wilderness_gid_seq postgres
9206; 0 0 SEQUENCE SET public wv_bnd_morgantown_wards_gid_seq postgres
9207; 0 0 SEQUENCE SET public wv_bnd_nhd_mussel_streams_gid_seq postgres
9208; 0 0 SEQUENCE SET public wv_bnd_public_lands_county_city_parks_gid_seq postgres
9209; 0 0 SEQUENCE SET public wv_bnd_public_lands_national_forest_gid_seq postgres
9210; 0 0 SEQUENCE SET public wv_bnd_public_lands_national_park_gid_seq postgres
9211; 0 0 SEQUENCE SET public wv_bnd_public_lands_nwr_gid_seq postgres
9212; 0 0 SEQUENCE SET public wv_bnd_public_lands_state_forests_gid_seq postgres
9213; 0 0 SEQUENCE SET public wv_bnd_public_lands_state_parks_gid_seq postgres
9214; 0 0 SEQUENCE SET public wv_bnd_public_lands_wildlife_resources_gid_seq postgres
9215; 0 0 SEQUENCE SET public wv_bnd_state_boundary_100k_gid_seq postgres
9216; 0 0 SEQUENCE SET public wv_bnd_voting_districts_2000_gid_seq postgres
9217; 0 0 SEQUENCE SET public wv_bnd_voting_districts_2002_gid_seq postgres
9218; 0 0 SEQUENCE SET public wv_bnd_workforce_investment_areas_gid_seq postgres
9219; 0 0 SEQUENCE SET public wv_censustracts_census_2020_utm83_gid_seq postgres
9220; 0 0 SEQUENCE SET public wv_county_boundaries_24k_topo_updated_2026_utm83_gdb_gid_seq postgres
9221; 0 0 SEQUENCE SET public wv_county_boundaries_24k_topo_updated_2026_wma84_gdb_gid_seq postgres
9222; 0 0 SEQUENCE SET public wv_eco_abandoned_mine_lands_line_gid_seq postgres
9223; 0 0 SEQUENCE SET public wv_eco_abandoned_mine_lands_point_gid_seq postgres
9224; 0 0 SEQUENCE SET public wv_eco_abandoned_mine_lands_polygon_gid_seq postgres
9225; 0 0 SEQUENCE SET public wv_eco_coal_fields_gid_seq postgres
9226; 0 0 SEQUENCE SET public wv_eco_ezec_communities_gid_seq postgres
9227; 0 0 SEQUENCE SET public wv_eco_industrial_sites_gid_seq postgres
9228; 0 0 SEQUENCE SET public wv_eco_manufacturing_directory_gid_seq postgres
9229; 0 0 SEQUENCE SET public wv_eco_mineral_operations_gid_seq postgres
9230; 0 0 SEQUENCE SET public wv_eco_mountaintop_removal_gid_seq postgres
9231; 0 0 SEQUENCE SET public wv_elv_summit_names_gid_seq postgres
9232; 0 0 SEQUENCE SET public wv_env_air_nonattainment_gid_seq postgres
9233; 0 0 SEQUENCE SET public wv_env_epa_facilities_gid_seq msjarvis
9234; 0 0 SEQUENCE SET public wv_env_timber_removal_volume_gid_seq postgres
9235; 0 0 SEQUENCE SET public wv_env_wildfire_regions_gid_seq postgres
9236; 0 0 SEQUENCE SET public wv_env_wind_energy_resources_gid_seq postgres
9237; 0 0 SEQUENCE SET public wv_geo_coal_beds_gid_seq postgres
9238; 0 0 SEQUENCE SET public wv_geo_geological_map_generalized_gid_seq postgres
9239; 0 0 SEQUENCE SET public wv_geo_karst_gid_seq postgres
9240; 0 0 SEQUENCE SET public wv_hlt_health_providers_gid_seq postgres
9241; 0 0 SEQUENCE SET public wv_hlt_public_health_departments_gid_seq postgres
9242; 0 0 SEQUENCE SET public wv_hlt_rural_health_facilities_gid_seq postgres
9243; 0 0 SEQUENCE SET public wv_hyd_dams_dmr_gid_seq postgres
9244; 0 0 SEQUENCE SET public wv_hyd_dams_nid_gid_seq postgres
9245; 0 0 SEQUENCE SET public wv_hyd_dams_noncoal_gid_seq postgres
9246; 0 0 SEQUENCE SET public wv_hyd_hazus_floodplain_zones_gid_seq msjarvis
9247; 0 0 SEQUENCE SET public wv_hyd_high_water_marks_gid_seq postgres
9248; 0 0 SEQUENCE SET public wv_hyd_navigable_waterways_gid_seq postgres
9249; 0 0 SEQUENCE SET public wv_hyd_navigable_waterways_river_miles_gid_seq postgres
9250; 0 0 SEQUENCE SET public wv_hyd_navigable_waterways_structures_gid_seq postgres
9251; 0 0 SEQUENCE SET public wv_hyd_springs_100gpm_gid_seq postgres
9252; 0 0 SEQUENCE SET public wv_hyd_streamflow_stations_gid_seq postgres
9253; 0 0 SEQUENCE SET public wv_hyd_streams_high_quality_gid_seq msjarvis
9254; 0 0 SEQUENCE SET public wv_hyd_streams_national_atlas_gid_seq postgres
9255; 0 0 SEQUENCE SET public wv_hyd_streams_tiger_gid_seq postgres
9256; 0 0 SEQUENCE SET public wv_hyd_watershed_boundary_11digit_gid_seq postgres
9257; 0 0 SEQUENCE SET public wv_hyd_watershed_boundary_12digit_hu_gid_seq postgres
9258; 0 0 SEQUENCE SET public wv_hyd_watershed_boundary_8_10_12_gid_seq postgres
9259; 0 0 SEQUENCE SET public wv_loc_census_urbanized_areas_gid_seq postgres
9260; 0 0 SEQUENCE SET public wv_loc_county_seats_gid_seq postgres
9261; 0 0 SEQUENCE SET public wv_loc_geodetic_control_points_gid_seq postgres
9262; 0 0 SEQUENCE SET public wv_loc_populated_places_census_gid_seq postgres
9263; 0 0 SEQUENCE SET public wv_loc_sams2_address_road_centerlines_gid_seq postgres
9264; 0 0 SEQUENCE SET public wv_mil_army_reserve_facilities_gid_seq postgres
9265; 0 0 SEQUENCE SET public wv_mil_national_guard_armories_gid_seq postgres
9266; 0 0 SEQUENCE SET public wv_plc_hazus_level1_gid_seq postgres
9267; 0 0 SEQUENCE SET public wv_plc_regional_planning_councils_gid_seq postgres
9268; 0 0 SEQUENCE SET public wv_plc_tax_district_boundaries_gid_seq postgres
9269; 0 0 SEQUENCE SET public wv_plc_tax_parcels_surface_mineral_gid_seq postgres
9270; 0 0 SEQUENCE SET public wv_rec_fishing_boating_access_ogc_fid_seq postgres
9271; 0 0 SEQUENCE SET public wv_rec_fishing_lakes_ogc_fid_seq postgres
9272; 0 0 SEQUENCE SET public wv_rec_national_forest_ogc_fid_seq postgres
9273; 0 0 SEQUENCE SET public wv_rec_nps_units_ogc_fid_seq postgres
9274; 0 0 SEQUENCE SET public wv_rec_nwr_units_ogc_fid_seq postgres
9275; 0 0 SEQUENCE SET public wv_rec_state_forests_ogc_fid_seq postgres
9276; 0 0 SEQUENCE SET public wv_rec_state_parks_ogc_fid_seq postgres
9277; 0 0 SEQUENCE SET public wv_rec_trail_points_ogc_fid_seq postgres
9278; 0 0 SEQUENCE SET public wv_rec_trails_ogc_fid_seq postgres
9279; 0 0 SEQUENCE SET public wv_rec_whitewater_trails_ogc_fid_seq postgres
9280; 0 0 SEQUENCE SET public wv_rec_wvdnr_managed_lands_ogc_fid_seq postgres
9281; 0 0 SEQUENCE SET public wv_soc_911_centers_gid_seq postgres
9282; 0 0 SEQUENCE SET public wv_soc_census_blockgroups_2020_gid_seq postgres
9283; 0 0 SEQUENCE SET public wv_soc_census_blockgroups_2020_utm17_gid_seq postgres
9284; 0 0 SEQUENCE SET public wv_soc_census_tracts_2020_gid_seq postgres
9285; 0 0 SEQUENCE SET public wv_soc_cities_pop10k_gid_seq postgres
9286; 0 0 SEQUENCE SET public wv_soc_cities_pop2500_gid_seq postgres
9287; 0 0 SEQUENCE SET public wv_soc_communities_pop_change_gid_seq postgres
9288; 0 0 SEQUENCE SET public wv_soc_courthouses_county_gid_seq postgres
9289; 0 0 SEQUENCE SET public wv_soc_courthouses_federal_gid_seq postgres
9290; 0 0 SEQUENCE SET public wv_soc_fish_hatcheries_gid_seq postgres
9291; 0 0 SEQUENCE SET public wv_soc_fishing_boating_access_gid_seq postgres
9292; 0 0 SEQUENCE SET public wv_soc_fishing_lakes_gid_seq postgres
9293; 0 0 SEQUENCE SET public wv_soc_higher_ed_facilities_gid_seq postgres
9294; 0 0 SEQUENCE SET public wv_soc_hospitals_wvdem_gid_seq msjarvis
9295; 0 0 SEQUENCE SET public wv_soc_libraries_gid_seq postgres
9296; 0 0 SEQUENCE SET public wv_soc_national_register_historic_points_gid_seq postgres
9297; 0 0 SEQUENCE SET public wv_soc_national_register_historic_polygons_gid_seq postgres
9298; 0 0 SEQUENCE SET public wv_soc_nursing_homes_gid_seq postgres
9299; 0 0 SEQUENCE SET public wv_soc_places_of_worship_wvgistc_gid_seq postgres
9300; 0 0 SEQUENCE SET public wv_soc_population_by_decade_gid_seq postgres
9301; 0 0 SEQUENCE SET public wv_soc_schools_k12_gid_seq msjarvis
9302; 0 0 SEQUENCE SET public wv_soc_towers_am_gid_seq postgres
9303; 0 0 SEQUENCE SET public wv_soc_towers_asr_gid_seq postgres
9304; 0 0 SEQUENCE SET public wv_soc_towers_cellular_gid_seq postgres
9305; 0 0 SEQUENCE SET public wv_soc_towers_fm_gid_seq postgres
9306; 0 0 SEQUENCE SET public wv_soc_towers_microwave_gid_seq postgres
9307; 0 0 SEQUENCE SET public wv_soc_towers_pager_gid_seq postgres
9308; 0 0 SEQUENCE SET public wv_soc_towers_private_gid_seq postgres
9309; 0 0 SEQUENCE SET public wv_soc_towers_tv_gid_seq postgres
9310; 0 0 SEQUENCE SET public wv_soc_va_facilities_gid_seq postgres
9311; 0 0 SEQUENCE SET public wv_soc_zcta_2020_gid_seq postgres
9312; 0 0 SEQUENCE SET public wv_str_bridges_gid_seq postgres
9313; 0 0 SEQUENCE SET public wv_str_correctional_institutions_gid_seq postgres
9314; 0 0 SEQUENCE SET public wv_str_flood_atrisk_structures_gid_seq postgres
9315; 0 0 SEQUENCE SET public wv_str_parole_offices_gid_seq postgres
9316; 0 0 SEQUENCE SET public wv_str_places_of_worship_hsip_gid_seq postgres
9317; 0 0 SEQUENCE SET public wv_str_samb_building_points_gid_seq postgres
9318; 0 0 SEQUENCE SET public wv_str_samb_building_polygons_gid_seq postgres
9319; 0 0 SEQUENCE SET public wv_trn_airport_facilities_gid_seq postgres
9320; 0 0 SEQUENCE SET public wv_trn_airport_proposed_gid_seq postgres
9321; 0 0 SEQUENCE SET public wv_trn_airport_runways_gid_seq postgres
9322; 0 0 SEQUENCE SET public wv_trn_airports_gid_seq msjarvis
9323; 0 0 SEQUENCE SET public wv_trn_intermodal_terminals_gid_seq postgres
9324; 0 0 SEQUENCE SET public wv_trn_mnf_recreation_trails_gid_seq postgres
9325; 0 0 SEQUENCE SET public wv_trn_mnf_roads_gid_seq postgres
9326; 0 0 SEQUENCE SET public wv_trn_railroad_lines_rti_gid_seq postgres
9327; 0 0 SEQUENCE SET public wv_trn_railroads_amtrak_gid_seq postgres
9328; 0 0 SEQUENCE SET public wv_trn_railroads_excursion_gid_seq postgres
9329; 0 0 SEQUENCE SET public wv_trn_railroads_national_network_gid_seq postgres
9330; 0 0 SEQUENCE SET public wv_trn_recreational_trails_gid_seq postgres
9331; 0 0 SEQUENCE SET public wv_trn_roads_interstate_gid_seq postgres
9332; 0 0 SEQUENCE SET public wv_trn_roads_major_4800_gid_seq postgres
9333; 0 0 SEQUENCE SET public wv_trn_roads_state_routes_gid_seq postgres
9334; 0 0 SEQUENCE SET public wv_trn_roads_us_highways_gid_seq postgres
9335; 0 0 SEQUENCE SET public wv_trn_roads_us_routes_gid_seq postgres
9336; 0 0 SEQUENCE SET public wv_trn_whitewater_trails_gid_seq postgres
9337; 0 0 SEQUENCE SET public wv_util_sewer_treatment_plants_gid_seq msjarvis
9338; 0 0 SEQUENCE SET public wv_util_solid_waste_facilities_gid_seq postgres
9339; 0 0 SEQUENCE SET public wv_wv_county_boundaries_24k_topo_updated_2026_utm83_gid_seq postgres
9340; 0 0 SEQUENCE SET public wv_wv_county_boundaries_24k_topo_updated_2026_wma84_gid_seq postgres
9341; 0 0 SEQUENCE SET runtime_governance commons_contribution_contribution_id_seq postgres
9342; 0 0 SEQUENCE SET runtime_governance commons_provenance_certificate_certificate_id_seq postgres
9343; 0 0 SEQUENCE SET runtime_governance commons_reconstruction_attempt_attempt_id_seq postgres
9344; 0 0 SEQUENCE SET runtime_governance commons_vector_contribution_vector_id_seq postgres
9345; 0 0 SEQUENCE SET runtime_governance epistemic_self_assessment_assessment_id_seq postgres
9346; 0 0 SEQUENCE SET runtime_governance phi_baseline_metrics_metrics_id_seq postgres
9347; 0 0 SEQUENCE SET runtime_governance phi_domain_metrics_metrics_id_seq postgres
9348; 0 0 SEQUENCE SET runtime_governance policy_set_audit_audit_id_seq postgres
9349; 0 0 SEQUENCE SET runtime_governance public_answer_audit_audit_id_seq postgres
9350; 0 0 SEQUENCE SET runtime_governance user_partition_registry_partition_id_seq postgres
9351; 0 0 SEQUENCE SET staging_hazus barbour_objectid_seq postgres
9352; 0 0 SEQUENCE SET staging_hazus berkeley_objectid_seq postgres
9353; 0 0 SEQUENCE SET staging_hazus boone_objectid_seq postgres
9354; 0 0 SEQUENCE SET staging_hazus braxton_objectid_seq postgres
9355; 0 0 SEQUENCE SET staging_hazus brooke_objectid_seq postgres
9356; 0 0 SEQUENCE SET staging_hazus cabell_objectid_seq postgres
9357; 0 0 SEQUENCE SET staging_hazus calhoun_objectid_seq postgres
9358; 0 0 SEQUENCE SET staging_hazus clay_objectid_seq postgres
9359; 0 0 SEQUENCE SET staging_hazus doddridge_objectid_seq postgres
9360; 0 0 SEQUENCE SET staging_hazus fayette_objectid_seq postgres
9361; 0 0 SEQUENCE SET staging_hazus floodplain_100year_objectid_seq postgres
9362; 0 0 SEQUENCE SET staging_hazus floodplain_10year_objectid_seq postgres
9363; 0 0 SEQUENCE SET staging_hazus floodplain_25year_objectid_seq postgres
9364; 0 0 SEQUENCE SET staging_hazus floodplain_50year_objectid_seq postgres
9365; 0 0 SEQUENCE SET staging_hazus gilmer_objectid_seq postgres
9366; 0 0 SEQUENCE SET staging_hazus grant_objectid_seq postgres
9367; 0 0 SEQUENCE SET staging_hazus greenbrier_objectid_seq postgres
9368; 0 0 SEQUENCE SET staging_hazus hampshire_objectid_seq postgres
9369; 0 0 SEQUENCE SET staging_hazus hancock_objectid_seq postgres
9370; 0 0 SEQUENCE SET staging_hazus hardy_objectid_seq postgres
9371; 0 0 SEQUENCE SET staging_hazus harrison_objectid_seq postgres
9372; 0 0 SEQUENCE SET staging_hazus jackson_objectid_seq postgres
9373; 0 0 SEQUENCE SET staging_hazus jefferson_objectid_seq postgres
9374; 0 0 SEQUENCE SET staging_hazus kanawha_objectid_seq postgres
9375; 0 0 SEQUENCE SET staging_hazus lewis_objectid_seq postgres
9376; 0 0 SEQUENCE SET staging_hazus lincoln_objectid_seq postgres
9377; 0 0 SEQUENCE SET staging_hazus logan_objectid_seq postgres
9378; 0 0 SEQUENCE SET staging_hazus marion_objectid_seq postgres
9379; 0 0 SEQUENCE SET staging_hazus marshall_objectid_seq postgres
9380; 0 0 SEQUENCE SET staging_hazus mason_objectid_seq postgres
9381; 0 0 SEQUENCE SET staging_hazus mcdowell_objectid_seq postgres
9382; 0 0 SEQUENCE SET staging_hazus mercer_objectid_seq postgres
9383; 0 0 SEQUENCE SET staging_hazus mineral_objectid_seq postgres
9384; 0 0 SEQUENCE SET staging_hazus mingo_objectid_seq postgres
9385; 0 0 SEQUENCE SET staging_hazus monongalia_objectid_seq postgres
9386; 0 0 SEQUENCE SET staging_hazus monroe_objectid_seq postgres
9387; 0 0 SEQUENCE SET staging_hazus morgan_objectid_seq postgres
9388; 0 0 SEQUENCE SET staging_hazus nicholas_objectid_seq postgres
9389; 0 0 SEQUENCE SET staging_hazus ohio_objectid_seq postgres
9390; 0 0 SEQUENCE SET staging_hazus pendleton_objectid_seq postgres
9391; 0 0 SEQUENCE SET staging_hazus pleasants_objectid_seq postgres
9392; 0 0 SEQUENCE SET staging_hazus pocahontas_objectid_seq postgres
9393; 0 0 SEQUENCE SET staging_hazus preston_objectid_seq postgres
9394; 0 0 SEQUENCE SET staging_hazus putnam_objectid_seq postgres
9395; 0 0 SEQUENCE SET staging_hazus raleigh_objectid_seq postgres
9396; 0 0 SEQUENCE SET staging_hazus randolph_objectid_seq postgres
9397; 0 0 SEQUENCE SET staging_hazus ritchie_objectid_seq postgres
9398; 0 0 SEQUENCE SET staging_hazus roane_objectid_seq postgres
9399; 0 0 SEQUENCE SET staging_hazus summers_objectid_seq postgres
9400; 0 0 SEQUENCE SET staging_hazus taylor_objectid_seq postgres
9401; 0 0 SEQUENCE SET staging_hazus tucker_objectid_seq postgres
9402; 0 0 SEQUENCE SET staging_hazus tyler_objectid_seq postgres
9403; 0 0 SEQUENCE SET staging_hazus upshur_objectid_seq postgres
9404; 0 0 SEQUENCE SET staging_hazus wayne_objectid_seq postgres
9405; 0 0 SEQUENCE SET staging_hazus webster_objectid_seq postgres
9406; 0 0 SEQUENCE SET staging_hazus wetzel_objectid_seq postgres
9407; 0 0 SEQUENCE SET staging_hazus wirt_objectid_seq postgres
9408; 0 0 SEQUENCE SET staging_hazus wood_objectid_seq postgres
9409; 0 0 SEQUENCE SET staging_hazus wyoming_objectid_seq postgres
9410; 0 0 SEQUENCE SET staging_tax_2025 mastersurfwv_2025_objectid_seq postgres
9411; 0 0 SEQUENCE SET staging_tax_2025 parcelsummary_ogc_fid_seq postgres
9412; 0 0 SEQUENCE SET staging_tax_districts wv_tax_districts_ll83_objectid_1_seq postgres
9413; 0 0 SEQUENCE SET staging_tax_districts wv_tax_districts_utm83_objectid_1_seq postgres
9414; 0 0 SEQUENCE SET staging_tax_districts wv_tax_districts_wma84_objectid_1_seq postgres
7946; 2606 4134659 CONSTRAINT runtime_governance civic_policy_audit civic_policy_audit_pkey postgres
7944; 2606 4134649 CONSTRAINT runtime_governance civic_policy_fact civic_policy_fact_pkey postgres
7994; 2606 4134931 CONSTRAINT runtime_governance commons_contribution commons_contribution_pkey postgres
7992; 2606 4134921 CONSTRAINT runtime_governance commons_k_threshold_policy commons_k_threshold_policy_pkey postgres
8003; 2606 4134967 CONSTRAINT runtime_governance commons_noninvertibility_policy commons_noninvertibility_policy_pkey postgres
7965; 2606 4134797 CONSTRAINT runtime_governance commons_phase_status commons_phase_status_pkey postgres
8000; 2606 4134956 CONSTRAINT runtime_governance commons_provenance_certificate commons_provenance_certificate_pkey postgres
8008; 2606 4135000 CONSTRAINT runtime_governance commons_reconstruction_attempt commons_reconstruction_attempt_pkey postgres
7997; 2606 4134944 CONSTRAINT runtime_governance commons_vector_contribution commons_vector_contribution_pkey postgres
7950; 2606 4134680 CONSTRAINT runtime_governance epistemic_loop_metrics epistemic_loop_metrics_pkey postgres
7948; 2606 4134672 CONSTRAINT runtime_governance epistemic_revision_log epistemic_revision_log_pkey postgres
7974; 2606 4134850 CONSTRAINT runtime_governance epistemic_self_assessment epistemic_self_assessment_pkey postgres
7963; 2606 4134766 CONSTRAINT runtime_governance geo_guard_city geo_guard_city_pkey postgres
7969; 2606 4134817 CONSTRAINT runtime_governance geo_guard_config geo_guard_config_pkey postgres
7967; 2606 4134809 CONSTRAINT runtime_governance phi_baseline_metrics phi_baseline_metrics_pkey postgres
7972; 2606 4134838 CONSTRAINT runtime_governance phi_domain_metrics phi_domain_metrics_pkey postgres
7961; 2606 4134759 CONSTRAINT runtime_governance policy_set_audit policy_set_audit_pkey postgres
7933; 2606 4134500 CONSTRAINT runtime_governance public_answer_audit public_answer_audit_pkey postgres
8006; 2606 4134979 CONSTRAINT runtime_governance user_partition_registry user_partition_registry_pkey postgres
7740; 1259 4120138 INDEX governance idx_person_plane_purpose_map_lookup postgres
7953; 1259 4134712 INDEX hilbert commons_provenance_commons_idx postgres
7987; 1259 4134899 INDEX identity idx_biometric_audit_log_identity_time postgres
7984; 1259 4134888 INDEX identity idx_biometric_consent_identity postgres
7990; 1259 4134911 INDEX identity idx_biometric_template_identity_modality_active postgres
6867; 1259 746668 INDEX normalization geoanchor_pkey postgres
7749; 1259 4120157 INDEX private idx_hilbert_person_external_subject_id postgres
7491; 1259 765907 INDEX public gbim_bg_coverage_area_bg_geoid_idx postgres
7492; 1259 765906 INDEX public gbim_bg_coverage_area_gbim_id_idx postgres
7499; 1259 765925 INDEX public gbim_bg_coverage_counts_bg_geoid_idx postgres
7500; 1259 765924 INDEX public gbim_bg_coverage_counts_gbim_id_idx postgres
7495; 1259 765916 INDEX public gbim_bg_coverage_length_bg_geoid_idx postgres
7496; 1259 765915 INDEX public gbim_bg_coverage_length_gbim_id_idx postgres
7505; 1259 765979 INDEX public gbim_blockgroup_coverage_bridge_bg_idx postgres
7506; 1259 765980 INDEX public gbim_blockgroup_coverage_bridge_gbim_idx postgres
7508; 1259 767663 INDEX public gbim_blockgroup_features_attrs_json_idx postgres
7514; 1259 769346 INDEX public gbim_blockgroup_recreation_flags_bg_idx postgres
7507; 1259 765986 INDEX public gbim_blockgroup_semantic_payload_bg_idx postgres
7511; 1259 769310 INDEX public gbim_blockgroup_vector_json_idx postgres
6874; 1259 4120119 INDEX public gbim_one_active_manifest_per_collection msjarvis_admin
7931; 1259 4134422 INDEX public gbim_provenance_tracker_idx postgres
7923; 1259 4134421 INDEX public gbim_record_claim_idx postgres
7924; 1259 4134420 INDEX public gbim_record_lookup_idx postgres
6875; 1259 910443 INDEX public gix_wv_atm_weather_stations_26917 postgres
7515; 1259 910446 INDEX public gix_wv_bio_ecoregions_26917 postgres
6879; 1259 912978 INDEX public gix_wv_bio_red_spruce_cover_26917 postgres
7420; 1259 1122999 INDEX public gix_wv_blockgroup_representation_geom postgres
6883; 1259 912985 INDEX public gix_wv_bnd_appalachian_basin_boundary_26917 postgres
6887; 1259 913076 INDEX public gix_wv_bnd_arc_counties_26917 postgres
6891; 1259 913085 INDEX public gix_wv_bnd_canaan_valley_nwr_26917 postgres
6895; 1259 913171 INDEX public gix_wv_bnd_census_designated_places_26917 postgres
6899; 1259 913231 INDEX public gix_wv_bnd_county_24k_26917 postgres
6903; 1259 913291 INDEX public gix_wv_bnd_county_municipal_dlg_26917 postgres
6907; 1259 913298 INDEX public gix_wv_bnd_mnf_basic_ownership_26917 postgres
6911; 1259 913348 INDEX public gix_wv_bnd_mnf_management_prescriptions_26917 postgres
6915; 1259 913361 INDEX public gix_wv_bnd_mnf_ranger_districts_26917 postgres
6919; 1259 913362 INDEX public gix_wv_bnd_mnf_recreation_campgrounds_26917 postgres
6923; 1259 913363 INDEX public gix_wv_bnd_mnf_recreation_sites_26917 postgres
6927; 1259 913372 INDEX public gix_wv_bnd_mnf_wilderness_26917 postgres
6931; 1259 913379 INDEX public gix_wv_bnd_morgantown_wards_26917 postgres
6935; 1259 915794 INDEX public gix_wv_bnd_nhd_mussel_streams_26917 postgres
6939; 1259 916062 INDEX public gix_wv_bnd_public_lands_county_city_parks_26917 postgres
6943; 1259 916080 INDEX public gix_wv_bnd_public_lands_national_forest_26917 postgres
6947; 1259 916086 INDEX public gix_wv_bnd_public_lands_national_park_26917 postgres
6951; 1259 916089 INDEX public gix_wv_bnd_public_lands_nwr_26917 postgres
6955; 1259 916100 INDEX public gix_wv_bnd_public_lands_state_forests_26917 postgres
6959; 1259 916198 INDEX public gix_wv_bnd_public_lands_state_parks_26917 postgres
6963; 1259 916420 INDEX public gix_wv_bnd_public_lands_wildlife_resources_26917 postgres
6967; 1259 916428 INDEX public gix_wv_bnd_state_boundary_100k_26917 postgres
6971; 1259 916435 INDEX public gix_wv_bnd_voting_districts_2000_26917 postgres
6975; 1259 917549 INDEX public gix_wv_bnd_voting_districts_2002_26917 postgres
6979; 1259 917610 INDEX public gix_wv_bnd_workforce_investment_areas_26917 postgres
7004; 1259 917670 INDEX public gix_wv_county_boundaries_24k_topo_updated_2026_wma84_gdb_26917 postgres
7008; 1259 917678 INDEX public gix_wv_eco_abandoned_mine_lands_line_26917 postgres
7012; 1259 917685 INDEX public gix_wv_eco_abandoned_mine_lands_point_26917 postgres
7016; 1259 917690 INDEX public gix_wv_eco_abandoned_mine_lands_polygon_26917 postgres
7020; 1259 917697 INDEX public gix_wv_eco_coal_fields_26917 postgres
7024; 1259 917707 INDEX public gix_wv_eco_ezec_communities_26917 postgres
7028; 1259 917766 INDEX public gix_wv_eco_industrial_sites_26917 postgres
7032; 1259 917769 INDEX public gix_wv_eco_manufacturing_directory_26917 postgres
7036; 1259 917814 INDEX public gix_wv_eco_mineral_operations_26917 postgres
7040; 1259 917815 INDEX public gix_wv_eco_mountaintop_removal_26917 postgres
7044; 1259 917816 INDEX public gix_wv_elv_summit_names_26917 postgres
7050; 1259 917876 INDEX public gix_wv_env_air_nonattainment_26917 postgres
7054; 1259 917884 INDEX public gix_wv_env_timber_removal_volume_26917 postgres
7058; 1259 917946 INDEX public gix_wv_env_wildfire_regions_26917 postgres
7062; 1259 918010 INDEX public gix_wv_env_wind_energy_resources_26917 postgres
7066; 1259 918017 INDEX public gix_wv_geo_coal_beds_26917 postgres
7070; 1259 918020 INDEX public gix_wv_geo_geological_map_generalized_26917 postgres
7074; 1259 918023 INDEX public gix_wv_geo_karst_26917 postgres
7705; 1259 1126747 INDEX public gix_wv_hazus_floodplain_100year_26917 postgres
7706; 1259 1126867 INDEX public gix_wv_hazus_floodplain_10year_26917 postgres
7707; 1259 1126987 INDEX public gix_wv_hazus_floodplain_25year_26917 postgres
7708; 1259 1127107 INDEX public gix_wv_hazus_floodplain_50year_26917 postgres
7078; 1259 918026 INDEX public gix_wv_hlt_health_providers_26917 postgres
7082; 1259 918030 INDEX public gix_wv_hlt_public_health_departments_26917 postgres
7086; 1259 918031 INDEX public gix_wv_hlt_rural_health_facilities_26917 postgres
7090; 1259 918032 INDEX public gix_wv_hyd_dams_dmr_26917 postgres
7094; 1259 918041 INDEX public gix_wv_hyd_dams_nid_26917 postgres
7098; 1259 918050 INDEX public gix_wv_hyd_dams_noncoal_26917 postgres
7102; 1259 918056 INDEX public gix_wv_hyd_high_water_marks_26917 postgres
7106; 1259 918068 INDEX public gix_wv_hyd_navigable_waterways_26917 postgres
7110; 1259 918069 INDEX public gix_wv_hyd_navigable_waterways_river_miles_26917 postgres
7114; 1259 918072 INDEX public gix_wv_hyd_navigable_waterways_structures_26917 postgres
7118; 1259 918077 INDEX public gix_wv_hyd_springs_100gpm_26917 postgres
7122; 1259 918080 INDEX public gix_wv_hyd_streamflow_stations_26917 postgres
7126; 1259 918110 INDEX public gix_wv_hyd_streams_national_atlas_26917 postgres
7130; 1259 920630 INDEX public gix_wv_hyd_streams_tiger_26917 postgres
7134; 1259 920960 INDEX public gix_wv_hyd_watershed_boundary_11digit_26917 postgres
7138; 1259 922218 INDEX public gix_wv_hyd_watershed_boundary_12digit_hu_26917 postgres
7142; 1259 922258 INDEX public gix_wv_hyd_watershed_boundary_8_10_12_26917 postgres
7148; 1259 922289 INDEX public gix_wv_loc_census_urbanized_areas_26917 postgres
7152; 1259 922290 INDEX public gix_wv_loc_county_seats_26917 postgres
7156; 1259 922291 INDEX public gix_wv_loc_geodetic_control_points_26917 postgres
7160; 1259 922301 INDEX public gix_wv_loc_populated_places_census_26917 postgres
7164; 1259 922306 INDEX public gix_wv_loc_sams2_address_road_centerlines_26917 postgres
7168; 1259 922318 INDEX public gix_wv_mil_army_reserve_facilities_26917 postgres
7172; 1259 922319 INDEX public gix_wv_mil_national_guard_armories_26917 postgres
7176; 1259 923352 INDEX public gix_wv_plc_hazus_level1_26917 postgres
7180; 1259 923413 INDEX public gix_wv_plc_regional_planning_councils_26917 postgres
7184; 1259 923923 INDEX public gix_wv_plc_tax_district_boundaries_26917 postgres
7188; 1259 1102918 INDEX public gix_wv_plc_tax_parcels_surface_mineral_26917 postgres
7479; 1259 1103105 INDEX public gix_wv_rec_whitewater_trails_26917 postgres
7192; 1259 1103110 INDEX public gix_wv_soc_911_centers_26917 postgres
7196; 1259 1104462 INDEX public gix_wv_soc_census_blockgroups_2020_26917 postgres
7200; 1259 1104966 INDEX public gix_wv_soc_census_tracts_2020_26917 postgres
7204; 1259 1104985 INDEX public gix_wv_soc_cities_pop10k_26917 postgres
7208; 1259 1105047 INDEX public gix_wv_soc_cities_pop2500_26917 postgres
7212; 1259 1105197 INDEX public gix_wv_soc_communities_pop_change_26917 postgres
7216; 1259 1105204 INDEX public gix_wv_soc_courthouses_county_26917 postgres
7220; 1259 1105205 INDEX public gix_wv_soc_courthouses_federal_26917 postgres
7224; 1259 1105206 INDEX public gix_wv_soc_fish_hatcheries_26917 postgres
7228; 1259 1105207 INDEX public gix_wv_soc_fishing_boating_access_26917 postgres
7232; 1259 1105285 INDEX public gix_wv_soc_fishing_lakes_26917 postgres
7236; 1259 1105288 INDEX public gix_wv_soc_higher_ed_facilities_26917 postgres
7240; 1259 1105289 INDEX public gix_wv_soc_libraries_26917 postgres
7244; 1259 1105293 INDEX public gix_wv_soc_national_register_historic_points_26917 postgres
7248; 1259 1105543 INDEX public gix_wv_soc_national_register_historic_polygons_26917 postgres
7252; 1259 1105551 INDEX public gix_wv_soc_nursing_homes_26917 postgres
7256; 1259 1105556 INDEX public gix_wv_soc_places_of_worship_wvgistc_26917 postgres
7260; 1259 1105621 INDEX public gix_wv_soc_population_by_decade_26917 postgres
7264; 1259 1105626 INDEX public gix_wv_soc_towers_am_26917 postgres
7268; 1259 1105627 INDEX public gix_wv_soc_towers_asr_26917 postgres
7272; 1259 1105639 INDEX public gix_wv_soc_towers_cellular_26917 postgres
7276; 1259 1105644 INDEX public gix_wv_soc_towers_fm_26917 postgres
7280; 1259 1105647 INDEX public gix_wv_soc_towers_microwave_26917 postgres
7284; 1259 1105659 INDEX public gix_wv_soc_towers_pager_26917 postgres
7288; 1259 1105665 INDEX public gix_wv_soc_towers_private_26917 postgres
7292; 1259 1105677 INDEX public gix_wv_soc_towers_tv_26917 postgres
7296; 1259 1105678 INDEX public gix_wv_soc_va_facilities_26917 postgres
7300; 1259 1106373 INDEX public gix_wv_soc_zcta_2020_26917 postgres
7304; 1259 1106380 INDEX public gix_wv_str_bridges_26917 postgres
7308; 1259 1106390 INDEX public gix_wv_str_correctional_institutions_26917 postgres
7312; 1259 1106394 INDEX public gix_wv_str_flood_atrisk_structures_26917 postgres
7316; 1259 1106402 INDEX public gix_wv_str_parole_offices_26917 postgres
7320; 1259 1106403 INDEX public gix_wv_str_places_of_worship_hsip_26917 postgres
7324; 1259 1106404 INDEX public gix_wv_str_samb_building_points_26917 postgres
7328; 1259 1106414 INDEX public gix_wv_str_samb_building_polygons_26917 postgres
7724; 1259 1876070 INDEX public gix_wv_tax_districts_2023_26917 postgres
7714; 1259 1872080 INDEX public gix_wv_tax_master_surf_2025_26917 postgres
7725; 1259 1876102 INDEX public gix_wv_tax_parcel_summary_2025_26917 postgres
7342; 1259 1106434 INDEX public gix_wv_trn_airport_facilities_26917 postgres
7346; 1259 1106437 INDEX public gix_wv_trn_airport_proposed_26917 postgres
7350; 1259 1106442 INDEX public gix_wv_trn_airport_runways_26917 postgres
7354; 1259 1106443 INDEX public gix_wv_trn_intermodal_terminals_26917 postgres
7358; 1259 1106639 INDEX public gix_wv_trn_mnf_recreation_trails_26917 postgres
7362; 1259 1107578 INDEX public gix_wv_trn_mnf_roads_26917 postgres
7366; 1259 1107814 INDEX public gix_wv_trn_railroad_lines_rti_26917 postgres
7370; 1259 1107823 INDEX public gix_wv_trn_railroads_amtrak_26917 postgres
7374; 1259 1107825 INDEX public gix_wv_trn_railroads_excursion_26917 postgres
7378; 1259 1107984 INDEX public gix_wv_trn_railroads_national_network_26917 postgres
7382; 1259 1107991 INDEX public gix_wv_trn_recreational_trails_26917 postgres
7386; 1259 1108055 INDEX public gix_wv_trn_roads_interstate_26917 postgres
7390; 1259 1116276 INDEX public gix_wv_trn_roads_major_4800_26917 postgres
7394; 1259 1116527 INDEX public gix_wv_trn_roads_state_routes_26917 postgres
7398; 1259 1116690 INDEX public gix_wv_trn_roads_us_highways_26917 postgres
7402; 1259 1116853 INDEX public gix_wv_trn_roads_us_routes_26917 postgres
7406; 1259 1117035 INDEX public gix_wv_trn_whitewater_trails_26917 postgres
7410; 1259 1117040 INDEX public gix_wv_util_solid_waste_facilities_26917 postgres
7414; 1259 1117098 INDEX public gix_wv_wv_county_boundaries_24k_topo_updated_2026_wma84_26917 postgres
7934; 1259 4134561 INDEX public public_admissible_gbim_mv_gbim_id_idx postgres
7935; 1259 4134562 INDEX public public_admissible_gbim_mv_spacetime_idx postgres
7781; 1259 4133509 INDEX public public_wv_bg_atm_weather_stations_geoid_idx postgres
7778; 1259 4133491 INDEX public public_wv_bg_bio_biodiversity_rank_geoid_idx postgres
7779; 1259 4133497 INDEX public public_wv_bg_bio_ecoregions_geoid_idx postgres
7780; 1259 4133503 INDEX public public_wv_bg_bio_red_spruce_cover_geoid_idx postgres
7786; 1259 4133539 INDEX public public_wv_bg_blockgroup_representation_geoid_idx postgres
7782; 1259 4133515 INDEX public public_wv_bg_bnd_appalachian_basin_boundary_geoid_idx postgres
7783; 1259 4133521 INDEX public public_wv_bg_bnd_arc_counties_geoid_idx postgres
7784; 1259 4133527 INDEX public public_wv_bg_bnd_canaan_valley_nwr_geoid_idx postgres
7785; 1259 4133533 INDEX public public_wv_bg_bnd_census_designated_places_geoid_idx postgres
7787; 1259 4133545 INDEX public public_wv_bg_bnd_county_24k_geoid_idx postgres
7788; 1259 4133551 INDEX public public_wv_bg_bnd_county_municipal_dlg_geoid_idx postgres
7789; 1259 4133557 INDEX public public_wv_bg_bnd_mnf_basic_ownership_geoid_idx postgres
7790; 1259 4133563 INDEX public public_wv_bg_bnd_mnf_management_prescriptions_geoid_idx postgres
7791; 1259 4133569 INDEX public public_wv_bg_bnd_mnf_ranger_districts_geoid_idx postgres
7792; 1259 4133575 INDEX public public_wv_bg_bnd_mnf_recreation_campgrounds_geoid_idx postgres
7793; 1259 4133581 INDEX public public_wv_bg_bnd_mnf_recreation_sites_geoid_idx postgres
7794; 1259 4133587 INDEX public public_wv_bg_bnd_mnf_wilderness_geoid_idx postgres
7795; 1259 4133593 INDEX public public_wv_bg_bnd_morgantown_wards_geoid_idx postgres
7796; 1259 4133599 INDEX public public_wv_bg_bnd_nhd_mussel_streams_geoid_idx postgres
7797; 1259 4133605 INDEX public public_wv_bg_bnd_public_lands_county_city_parks_geoid_idx postgres
7798; 1259 4133611 INDEX public public_wv_bg_bnd_public_lands_national_forest_geoid_idx postgres
7799; 1259 4133617 INDEX public public_wv_bg_bnd_public_lands_national_park_geoid_idx postgres
7800; 1259 4133623 INDEX public public_wv_bg_bnd_public_lands_nwr_geoid_idx postgres
7801; 1259 4133629 INDEX public public_wv_bg_bnd_public_lands_state_forests_geoid_idx postgres
7802; 1259 4133635 INDEX public public_wv_bg_bnd_public_lands_state_parks_geoid_idx postgres
7803; 1259 4133641 INDEX public public_wv_bg_bnd_public_lands_wildlife_resources_geoid_idx postgres
7804; 1259 4133647 INDEX public public_wv_bg_bnd_state_boundary_100k_geoid_idx postgres
7805; 1259 4133653 INDEX public public_wv_bg_bnd_voting_districts_2000_geoid_idx postgres
7806; 1259 4133659 INDEX public public_wv_bg_bnd_voting_districts_2002_geoid_idx postgres
7807; 1259 4133665 INDEX public public_wv_bg_bnd_workforce_investment_areas_geoid_idx postgres
7808; 1259 4133671 INDEX public public_wv_bg_censustracts_census_2020_utm83_geoid_idx postgres
7809; 1259 4133677 INDEX public public_wv_bg_county_boundaries_24k_topo_updated_2026_utm83_gdb_ postgres
7810; 1259 4133683 INDEX public public_wv_bg_county_boundaries_24k_topo_updated_2026_wma84_gdb_ postgres
7811; 1259 4133689 INDEX public public_wv_bg_eco_abandoned_mine_lands_line_geoid_idx postgres
7812; 1259 4133695 INDEX public public_wv_bg_eco_abandoned_mine_lands_point_geoid_idx postgres
7813; 1259 4133701 INDEX public public_wv_bg_eco_abandoned_mine_lands_polygon_geoid_idx postgres
7755; 1259 4125825 INDEX public public_wv_bg_eco_aml_geoid_idx postgres
7814; 1259 4133707 INDEX public public_wv_bg_eco_coal_fields_geoid_idx postgres
7815; 1259 4133713 INDEX public public_wv_bg_eco_ezec_communities_geoid_idx postgres
7816; 1259 4133719 INDEX public public_wv_bg_eco_industrial_sites_geoid_idx postgres
7817; 1259 4133725 INDEX public public_wv_bg_eco_manufacturing_directory_geoid_idx postgres
7818; 1259 4133731 INDEX public public_wv_bg_eco_mineral_operations_geoid_idx postgres
7819; 1259 4133737 INDEX public public_wv_bg_eco_mountaintop_removal_geoid_idx postgres
7754; 1259 4125819 INDEX public public_wv_bg_eco_mtr_geoid_idx postgres
7751; 1259 4120316 INDEX public public_wv_bg_education_access_geoid_idx postgres
7820; 1259 4133743 INDEX public public_wv_bg_elv_summit_names_geoid_idx postgres
7763; 1259 4132681 INDEX public public_wv_bg_enriched_geoid_idx postgres
7821; 1259 4133749 INDEX public public_wv_bg_env_air_nonattainment_geoid_idx postgres
7922; 1259 4134365 INDEX public public_wv_bg_env_epa_facilities_geoid_idx postgres
7822; 1259 4133761 INDEX public public_wv_bg_env_timber_removal_volume_geoid_idx postgres
7823; 1259 4133767 INDEX public public_wv_bg_env_wildfire_regions_geoid_idx postgres
7824; 1259 4133773 INDEX public public_wv_bg_env_wind_energy_resources_geoid_idx postgres
7825; 1259 4133779 INDEX public public_wv_bg_geo_coal_beds_geoid_idx postgres
7826; 1259 4133785 INDEX public public_wv_bg_geo_geological_map_generalized_geoid_idx postgres
7827; 1259 4133791 INDEX public public_wv_bg_geo_karst_geoid_idx postgres
7753; 1259 4124849 INDEX public public_wv_bg_governance_geoid_idx postgres
7752; 1259 4123212 INDEX public public_wv_bg_hazard_flags_geoid_idx postgres
7828; 1259 4133797 INDEX public public_wv_bg_hazus_floodplain_100year_geoid_idx postgres
7829; 1259 4133803 INDEX public public_wv_bg_hazus_floodplain_10year_geoid_idx postgres
7830; 1259 4133809 INDEX public public_wv_bg_hazus_floodplain_25year_geoid_idx postgres
7831; 1259 4133815 INDEX public public_wv_bg_hazus_floodplain_50year_geoid_idx postgres
7750; 1259 4120310 INDEX public public_wv_bg_health_access_geoid_idx postgres
7832; 1259 4133821 INDEX public public_wv_bg_hlt_health_providers_geoid_idx postgres
7833; 1259 4133827 INDEX public public_wv_bg_hlt_rural_health_facilities_geoid_idx postgres
7775; 1259 4132816 INDEX public public_wv_bg_hyd_dams_dmr_geoid_idx postgres
7834; 1259 4133833 INDEX public public_wv_bg_hyd_dams_nid_geoid_idx postgres
7835; 1259 4133839 INDEX public public_wv_bg_hyd_dams_noncoal_geoid_idx postgres
7836; 1259 4133845 INDEX public public_wv_bg_hyd_hazus_floodplain_zones_geoid_idx postgres
7837; 1259 4133851 INDEX public public_wv_bg_hyd_high_water_marks_geoid_idx postgres
7838; 1259 4133857 INDEX public public_wv_bg_hyd_navigable_waterways_geoid_idx postgres
7839; 1259 4133863 INDEX public public_wv_bg_hyd_navigable_waterways_river_miles_geoid_idx postgres
7840; 1259 4133869 INDEX public public_wv_bg_hyd_navigable_waterways_structures_geoid_idx postgres
7841; 1259 4133875 INDEX public public_wv_bg_hyd_springs_100gpm_geoid_idx postgres
7842; 1259 4133881 INDEX public public_wv_bg_hyd_streamflow_stations_geoid_idx postgres
7843; 1259 4133887 INDEX public public_wv_bg_hyd_streams_high_quality_geoid_idx postgres
7844; 1259 4133893 INDEX public public_wv_bg_hyd_streams_national_atlas_geoid_idx postgres
7845; 1259 4133899 INDEX public public_wv_bg_hyd_streams_tiger_geoid_idx postgres
7846; 1259 4133905 INDEX public public_wv_bg_hyd_watershed_boundary_11digit_geoid_idx postgres
7847; 1259 4133911 INDEX public public_wv_bg_hyd_watershed_boundary_12digit_hu_geoid_idx postgres
7848; 1259 4133917 INDEX public public_wv_bg_hyd_watershed_boundary_8_10_12_geoid_idx postgres
7849; 1259 4133923 INDEX public public_wv_bg_loc_census_urbanized_areas_geoid_idx postgres
7850; 1259 4133929 INDEX public public_wv_bg_loc_county_seats_geoid_idx postgres
7851; 1259 4133935 INDEX public public_wv_bg_loc_geodetic_control_points_geoid_idx postgres
7852; 1259 4133941 INDEX public public_wv_bg_loc_populated_places_census_geoid_idx postgres
7853; 1259 4133947 INDEX public public_wv_bg_loc_sams2_address_road_centerlines_geoid_idx postgres
7854; 1259 4133953 INDEX public public_wv_bg_mil_army_reserve_facilities_geoid_idx postgres
7855; 1259 4133959 INDEX public public_wv_bg_mil_national_guard_armories_geoid_idx postgres
7856; 1259 4133965 INDEX public public_wv_bg_plc_hazus_level1_geoid_idx postgres
7857; 1259 4133971 INDEX public public_wv_bg_plc_regional_planning_councils_geoid_idx postgres
7858; 1259 4133977 INDEX public public_wv_bg_plc_tax_district_boundaries_geoid_idx postgres
7859; 1259 4133983 INDEX public public_wv_bg_plc_tax_parcels_surface_mineral_geoid_idx postgres
7773; 1259 4132785 INDEX public public_wv_bg_rec_fishing_access_geoid_idx postgres
7860; 1259 4133989 INDEX public public_wv_bg_rec_fishing_lakes_geoid_idx postgres
7762; 1259 4126872 INDEX public public_wv_bg_rec_libraries_geoid_idx postgres
7776; 1259 4132822 INDEX public public_wv_bg_rec_national_forest_geoid_idx postgres
7861; 1259 4133995 INDEX public public_wv_bg_rec_nps_units_geoid_idx postgres
7862; 1259 4134001 INDEX public public_wv_bg_rec_nwr_units_geoid_idx postgres
7863; 1259 4134007 INDEX public public_wv_bg_rec_state_forests_geoid_idx postgres
7864; 1259 4134013 INDEX public public_wv_bg_rec_state_parks_geoid_idx postgres
7865; 1259 4134019 INDEX public public_wv_bg_rec_trail_points_geoid_idx postgres
7767; 1259 4132730 INDEX public public_wv_bg_rec_trails_geoid_idx postgres
7866; 1259 4134025 INDEX public public_wv_bg_rec_whitewater_trails_geoid_idx postgres
7867; 1259 4134031 INDEX public public_wv_bg_rec_wvdnr_managed_lands_geoid_idx postgres
7868; 1259 4134037 INDEX public public_wv_bg_soc_911_centers_geoid_idx postgres
7869; 1259 4134043 INDEX public public_wv_bg_soc_census_blockgroups_2020_geoid_idx postgres
7870; 1259 4134049 INDEX public public_wv_bg_soc_census_blockgroups_2020_utm17_geoid_idx postgres
7871; 1259 4134055 INDEX public public_wv_bg_soc_census_tracts_2020_geoid_idx postgres
7872; 1259 4134061 INDEX public public_wv_bg_soc_cities_pop10k_geoid_idx postgres
7873; 1259 4134067 INDEX public public_wv_bg_soc_cities_pop2500_geoid_idx postgres
7874; 1259 4134073 INDEX public public_wv_bg_soc_communities_pop_change_geoid_idx postgres
7875; 1259 4134079 INDEX public public_wv_bg_soc_courthouses_county_geoid_idx postgres
7876; 1259 4134085 INDEX public public_wv_bg_soc_courthouses_federal_geoid_idx postgres
7877; 1259 4134091 INDEX public public_wv_bg_soc_fish_hatcheries_geoid_idx postgres
7878; 1259 4134097 INDEX public public_wv_bg_soc_fishing_boating_access_geoid_idx postgres
7879; 1259 4134103 INDEX public public_wv_bg_soc_fishing_lakes_geoid_idx postgres
7880; 1259 4134109 INDEX public public_wv_bg_soc_higher_ed_facilities_geoid_idx postgres
7881; 1259 4134115 INDEX public public_wv_bg_soc_national_register_historic_points_geoid_idx postgres
7882; 1259 4134121 INDEX public public_wv_bg_soc_national_register_historic_polygons_geoid_idx postgres
7777; 1259 4132828 INDEX public public_wv_bg_soc_nursing_homes_geoid_idx postgres
7883; 1259 4134127 INDEX public public_wv_bg_soc_places_of_worship_wvgistc_geoid_idx postgres
7884; 1259 4134133 INDEX public public_wv_bg_soc_population_by_decade_geoid_idx postgres
7774; 1259 4132791 INDEX public public_wv_bg_soc_schools_k12_geoid_idx postgres
7885; 1259 4134139 INDEX public public_wv_bg_soc_towers_am_geoid_idx postgres
7886; 1259 4134145 INDEX public public_wv_bg_soc_towers_asr_geoid_idx postgres
7887; 1259 4134151 INDEX public public_wv_bg_soc_towers_cellular_geoid_idx postgres
7888; 1259 4134157 INDEX public public_wv_bg_soc_towers_fm_geoid_idx postgres
7889; 1259 4134163 INDEX public public_wv_bg_soc_towers_microwave_geoid_idx postgres
7890; 1259 4134169 INDEX public public_wv_bg_soc_towers_pager_geoid_idx postgres
7891; 1259 4134175 INDEX public public_wv_bg_soc_towers_private_geoid_idx postgres
7892; 1259 4134181 INDEX public public_wv_bg_soc_towers_tv_geoid_idx postgres
7769; 1259 4132743 INDEX public public_wv_bg_soc_va_facilities_geoid_idx postgres
7893; 1259 4134187 INDEX public public_wv_bg_soc_zcta_2020_geoid_idx postgres
7761; 1259 4125903 INDEX public public_wv_bg_social_911_geoid_idx postgres
7760; 1259 4125897 INDEX public public_wv_bg_social_higher_ed_geoid_idx postgres
7768; 1259 4132737 INDEX public public_wv_bg_social_hospitals_geoid_idx postgres
7766; 1259 4132714 INDEX public public_wv_bg_social_libraries_geoid_idx postgres
7894; 1259 4134193 INDEX public public_wv_bg_str_bridges_geoid_idx postgres
7772; 1259 4132779 INDEX public public_wv_bg_str_correctional_institutions_geoid_idx postgres
7895; 1259 4134199 INDEX public public_wv_bg_str_flood_atrisk_structures_geoid_idx postgres
7896; 1259 4134205 INDEX public public_wv_bg_str_parole_offices_geoid_idx postgres
7897; 1259 4134211 INDEX public public_wv_bg_str_places_of_worship_hsip_geoid_idx postgres
7898; 1259 4134217 INDEX public public_wv_bg_str_samb_building_points_geoid_idx postgres
7899; 1259 4134223 INDEX public public_wv_bg_str_samb_building_polygons_geoid_idx postgres
7900; 1259 4134229 INDEX public public_wv_bg_tax_districts_2023_geoid_idx postgres
7901; 1259 4134235 INDEX public public_wv_bg_tax_master_surf_2025_geoid_idx postgres
7757; 1259 4125873 INDEX public public_wv_bg_transport_airports_geoid_idx postgres
7756; 1259 4125867 INDEX public public_wv_bg_transport_roads_geoid_idx postgres
7902; 1259 4134241 INDEX public public_wv_bg_trn_airport_facilities_geoid_idx postgres
7903; 1259 4134247 INDEX public public_wv_bg_trn_airport_proposed_geoid_idx postgres
7904; 1259 4134253 INDEX public public_wv_bg_trn_airport_runways_geoid_idx postgres
7905; 1259 4134259 INDEX public public_wv_bg_trn_airports_geoid_idx postgres
7906; 1259 4134265 INDEX public public_wv_bg_trn_intermodal_terminals_geoid_idx postgres
7907; 1259 4134271 INDEX public public_wv_bg_trn_mnf_recreation_trails_geoid_idx postgres
7908; 1259 4134277 INDEX public public_wv_bg_trn_mnf_roads_geoid_idx postgres
7909; 1259 4134283 INDEX public public_wv_bg_trn_railroad_lines_rti_geoid_idx postgres
7910; 1259 4134289 INDEX public public_wv_bg_trn_railroads_amtrak_geoid_idx postgres
7911; 1259 4134295 INDEX public public_wv_bg_trn_railroads_excursion_geoid_idx postgres
7912; 1259 4134301 INDEX public public_wv_bg_trn_railroads_national_network_geoid_idx postgres
7913; 1259 4134307 INDEX public public_wv_bg_trn_recreational_trails_geoid_idx postgres
7914; 1259 4134313 INDEX public public_wv_bg_trn_roads_interstate_geoid_idx postgres
7915; 1259 4134319 INDEX public public_wv_bg_trn_roads_major_4800_geoid_idx postgres
7916; 1259 4134325 INDEX public public_wv_bg_trn_roads_state_routes_geoid_idx postgres
7917; 1259 4134331 INDEX public public_wv_bg_trn_roads_us_highways_geoid_idx postgres
7918; 1259 4134337 INDEX public public_wv_bg_trn_roads_us_routes_geoid_idx postgres
7919; 1259 4134343 INDEX public public_wv_bg_trn_whitewater_trails_geoid_idx postgres
7758; 1259 4125879 INDEX public public_wv_bg_util_sewer_geoid_idx postgres
7770; 1259 4132749 INDEX public public_wv_bg_util_sewer_plants_geoid_idx postgres
7771; 1259 4132773 INDEX public public_wv_bg_util_solid_waste_facilities_geoid_idx postgres
7759; 1259 4125885 INDEX public public_wv_bg_util_solid_waste_geoid_idx postgres
7920; 1259 4134349 INDEX public public_wv_bg_wv_county_boundaries_24k_topo_updated_2026_utm83_g postgres
7921; 1259 4134355 INDEX public public_wv_bg_wv_county_boundaries_24k_topo_updated_2026_wma84_g postgres
6876; 1259 746669 INDEX public wv_atm_weather_stations_geom_geom_idx postgres
7434; 1259 759068 INDEX public wv_bio_biodiversity_rank_geom_geom_idx msjarvis
7516; 1259 1117570 INDEX public wv_bio_ecoregions_geom_idx postgres
6880; 1259 746672 INDEX public wv_bio_red_spruce_cover_geom_geom_idx postgres
6884; 1259 746673 INDEX public wv_bnd_appalachian_basin_boundary_geom_geom_idx postgres
6888; 1259 746674 INDEX public wv_bnd_arc_counties_geom_geom_idx postgres
6892; 1259 746675 INDEX public wv_bnd_canaan_valley_nwr_geom_geom_idx postgres
6896; 1259 746676 INDEX public wv_bnd_census_designated_places_geom_geom_idx postgres
6900; 1259 746677 INDEX public wv_bnd_county_24k_geom_geom_idx postgres
6904; 1259 746678 INDEX public wv_bnd_county_municipal_dlg_geom_geom_idx postgres
6908; 1259 746679 INDEX public wv_bnd_mnf_basic_ownership_geom_geom_idx postgres
6912; 1259 746680 INDEX public wv_bnd_mnf_management_prescriptions_geom_geom_idx postgres
6916; 1259 746681 INDEX public wv_bnd_mnf_ranger_districts_geom_geom_idx postgres
6920; 1259 746682 INDEX public wv_bnd_mnf_recreation_geom_geom_idx postgres
6924; 1259 746683 INDEX public wv_bnd_mnf_recreation_sites_geom_geom_idx postgres
6928; 1259 746684 INDEX public wv_bnd_mnf_wilderness_geom_geom_idx postgres
6932; 1259 746685 INDEX public wv_bnd_morgantown_wards_geom_geom_idx postgres
6936; 1259 746686 INDEX public wv_bnd_nhd_mussel_streams_geom_geom_idx postgres
6940; 1259 746687 INDEX public wv_bnd_public_lands_county_city_parks_geom_geom_idx postgres
6944; 1259 746688 INDEX public wv_bnd_public_lands_national_forest_geom_geom_idx postgres
6948; 1259 746689 INDEX public wv_bnd_public_lands_national_park_geom_geom_idx postgres
6952; 1259 746690 INDEX public wv_bnd_public_lands_nwr_geom_geom_idx postgres
6956; 1259 746691 INDEX public wv_bnd_public_lands_state_forests_geom_geom_idx postgres
6960; 1259 746692 INDEX public wv_bnd_public_lands_state_parks_geom_geom_idx postgres
6964; 1259 746693 INDEX public wv_bnd_public_lands_wildlife_resources_geom_geom_idx postgres
6968; 1259 746694 INDEX public wv_bnd_state_boundary_100k_geom_geom_idx postgres
6972; 1259 746695 INDEX public wv_bnd_voting_districts_2000_geom_geom_idx postgres
6976; 1259 746696 INDEX public wv_bnd_voting_districts_2002_geom_geom_idx postgres
6980; 1259 746697 INDEX public wv_bnd_workforce_investment_areas_geom_geom_idx postgres
6983; 1259 746698 INDEX public wv_censustracts_census_2020_utm83_geom_geom_idx postgres
7001; 1259 746699 INDEX public wv_county_boundaries_24k_topo_updated_2026_utm83__geom_geom_idx postgres
7005; 1259 746700 INDEX public wv_county_boundaries_24k_topo_updated_2026_wma84__geom_geom_idx postgres
7009; 1259 746701 INDEX public wv_eco_abandoned_mine_lands_line_geom_geom_idx postgres
7013; 1259 746702 INDEX public wv_eco_abandoned_mine_lands_point_geom_geom_idx postgres
7017; 1259 746703 INDEX public wv_eco_abandoned_mine_lands_polygon_geom_geom_idx postgres
7021; 1259 746704 INDEX public wv_eco_coal_fields_geom_geom_idx postgres
7025; 1259 746705 INDEX public wv_eco_ezec_communities_geom_geom_idx postgres
7029; 1259 746706 INDEX public wv_eco_industrial_sites_geom_geom_idx postgres
7033; 1259 746707 INDEX public wv_eco_manufacturing_directory_geom_geom_idx postgres
7037; 1259 746708 INDEX public wv_eco_mineral_operations_geom_geom_idx postgres
7041; 1259 746709 INDEX public wv_eco_mountaintop_removal_geom_geom_idx postgres
7045; 1259 746710 INDEX public wv_elv_summit_names_geom_geom_idx postgres
7051; 1259 746711 INDEX public wv_env_air_nonattainment_geom_geom_idx postgres
7437; 1259 759069 INDEX public wv_env_epa_facilities_geom_geom_idx msjarvis
7055; 1259 746713 INDEX public wv_env_timber_removal_volume_geom_geom_idx postgres
7059; 1259 746714 INDEX public wv_env_wildfire_regions_geom_geom_idx postgres
7063; 1259 746715 INDEX public wv_env_wind_energy_resources_geom_geom_idx postgres
7067; 1259 746716 INDEX public wv_geo_coal_beds_geom_geom_idx postgres
7071; 1259 746717 INDEX public wv_geo_geological_map_generalized_geom_geom_idx postgres
7075; 1259 746718 INDEX public wv_geo_karst_geom_geom_idx postgres
7079; 1259 746719 INDEX public wv_hlt_health_providers_geom_geom_idx postgres
7083; 1259 746720 INDEX public wv_hlt_public_health_departments_geom_geom_idx postgres
7087; 1259 746721 INDEX public wv_hlt_rural_health_facilities_geom_geom_idx postgres
7091; 1259 746722 INDEX public wv_hyd_dams_dmr_geom_geom_idx postgres
7095; 1259 746723 INDEX public wv_hyd_dams_nid_geom_geom_idx postgres
7099; 1259 746724 INDEX public wv_hyd_dams_noncoal_geom_geom_idx postgres
7431; 1259 758203 INDEX public wv_hyd_hazus_floodplain_zones_geom_geom_idx msjarvis
7103; 1259 746726 INDEX public wv_hyd_high_water_marks_geom_geom_idx postgres
7107; 1259 746727 INDEX public wv_hyd_navigable_waterways_geom_geom_idx postgres
7111; 1259 746728 INDEX public wv_hyd_navigable_waterways_river_miles_geom_geom_idx postgres
7115; 1259 746729 INDEX public wv_hyd_navigable_waterways_structures_geom_geom_idx postgres
7119; 1259 746730 INDEX public wv_hyd_springs_100gpm_geom_geom_idx postgres
7123; 1259 746731 INDEX public wv_hyd_streamflow_stations_geom_geom_idx postgres
7440; 1259 759070 INDEX public wv_hyd_streams_high_quality_geom_geom_idx msjarvis
7127; 1259 746733 INDEX public wv_hyd_streams_national_atlas_geom_geom_idx postgres
7131; 1259 746734 INDEX public wv_hyd_streams_tiger_geom_geom_idx postgres
7135; 1259 746735 INDEX public wv_hyd_watershed_boundary_11digit_geom_geom_idx postgres
7139; 1259 746736 INDEX public wv_hyd_watershed_boundary_12digit_hu_geom_geom_idx postgres
7143; 1259 746737 INDEX public wv_hyd_watershed_boundary_8_10_12_geom_geom_idx postgres
7149; 1259 746738 INDEX public wv_loc_census_urbanized_areas_geom_geom_idx postgres
7153; 1259 746739 INDEX public wv_loc_county_seats_geom_geom_idx postgres
7157; 1259 746740 INDEX public wv_loc_geodetic_control_points_geom_geom_idx postgres
7161; 1259 746741 INDEX public wv_loc_populated_places_census_geom_geom_idx postgres
7165; 1259 746742 INDEX public wv_loc_sams2_address_road_centerlines_geom_geom_idx postgres
7169; 1259 746743 INDEX public wv_mil_army_reserve_facilities_geom_geom_idx postgres
7173; 1259 746744 INDEX public wv_mil_national_guard_armories_geom_geom_idx postgres
7177; 1259 746745 INDEX public wv_plc_hazus_level1_geom_geom_idx postgres
7181; 1259 746746 INDEX public wv_plc_regional_planning_councils_geom_geom_idx postgres
7185; 1259 746747 INDEX public wv_plc_tax_district_boundaries_geom_geom_idx postgres
7189; 1259 746748 INDEX public wv_plc_tax_parcels_surface_mineral_geom_geom_idx postgres
7483; 1259 764353 INDEX public wv_rec_fishing_boating_access_geom_geom_idx postgres
7458; 1259 760293 INDEX public wv_rec_fishing_lakes_geom_geom_idx postgres
7464; 1259 760865 INDEX public wv_rec_national_forest_geom_geom_idx postgres
7467; 1259 760907 INDEX public wv_rec_nps_units_geom_geom_idx postgres
7470; 1259 760952 INDEX public wv_rec_nwr_units_geom_geom_idx postgres
7461; 1259 760816 INDEX public wv_rec_state_forests_geom_geom_idx postgres
7455; 1259 760090 INDEX public wv_rec_state_parks_geom_geom_idx postgres
7476; 1259 763991 INDEX public wv_rec_trail_points_geom_geom_idx postgres
7473; 1259 760984 INDEX public wv_rec_trails_geom_geom_idx postgres
7480; 1259 764001 INDEX public wv_rec_whitewater_trails_geom_geom_idx postgres
7486; 1259 764728 INDEX public wv_rec_wvdnr_managed_lands_geom_geom_idx postgres
7193; 1259 746749 INDEX public wv_soc_911_centers_geom_geom_idx postgres
7197; 1259 746750 INDEX public wv_soc_census_blockgroups_2020_geom_geom_idx postgres
7519; 1259 771881 INDEX public wv_soc_census_blockgroups_2020_utm17_geom_idx postgres
7201; 1259 746751 INDEX public wv_soc_census_tracts_2020_geom_geom_idx postgres
7205; 1259 746752 INDEX public wv_soc_cities_pop10k_geom_geom_idx postgres
7209; 1259 746753 INDEX public wv_soc_cities_pop2500_geom_geom_idx postgres
7213; 1259 746754 INDEX public wv_soc_communities_pop_change_geom_geom_idx postgres
7217; 1259 746755 INDEX public wv_soc_courthouses_county_geom_geom_idx postgres
7221; 1259 746756 INDEX public wv_soc_courthouses_federal_geom_geom_idx postgres
7225; 1259 746757 INDEX public wv_soc_fish_hatcheries_geom_geom_idx postgres
7229; 1259 746758 INDEX public wv_soc_fishing_boating_access_geom_geom_idx postgres
7233; 1259 746759 INDEX public wv_soc_fishing_lakes_geom_geom_idx postgres
7237; 1259 746760 INDEX public wv_soc_higher_ed_facilities_geom_geom_idx postgres
7443; 1259 759071 INDEX public wv_soc_hospitals_wvdem_geom_geom_idx msjarvis
7241; 1259 746762 INDEX public wv_soc_libraries_geom_geom_idx postgres
7245; 1259 746763 INDEX public wv_soc_national_register_historic_points_geom_geom_idx postgres
7249; 1259 746764 INDEX public wv_soc_national_register_historic_polygons_geom_geom_idx postgres
7253; 1259 746765 INDEX public wv_soc_nursing_homes_geom_geom_idx postgres
7257; 1259 746766 INDEX public wv_soc_places_of_worship_wvgistc_geom_geom_idx postgres
7261; 1259 746767 INDEX public wv_soc_population_by_decade_geom_geom_idx postgres
7446; 1259 759072 INDEX public wv_soc_schools_k12_geom_geom_idx msjarvis
7265; 1259 746769 INDEX public wv_soc_towers_am_geom_geom_idx postgres
7269; 1259 746770 INDEX public wv_soc_towers_asr_geom_geom_idx postgres
7273; 1259 746771 INDEX public wv_soc_towers_cellular_geom_geom_idx postgres
7277; 1259 746772 INDEX public wv_soc_towers_fm_geom_geom_idx postgres
7281; 1259 746773 INDEX public wv_soc_towers_microwave_geom_geom_idx postgres
7285; 1259 746774 INDEX public wv_soc_towers_pager_geom_geom_idx postgres
7289; 1259 746775 INDEX public wv_soc_towers_private_geom_geom_idx postgres
7293; 1259 746776 INDEX public wv_soc_towers_tv_geom_geom_idx postgres
7297; 1259 746777 INDEX public wv_soc_va_facilities_geom_geom_idx postgres
7301; 1259 746778 INDEX public wv_soc_zcta_2020_geom_geom_idx postgres
7305; 1259 746779 INDEX public wv_str_bridges_geom_geom_idx postgres
7309; 1259 746780 INDEX public wv_str_correctional_institutions_geom_geom_idx postgres
7313; 1259 746781 INDEX public wv_str_flood_atrisk_structures_geom_geom_idx postgres
7317; 1259 746782 INDEX public wv_str_parole_offices_geom_geom_idx postgres
7321; 1259 746783 INDEX public wv_str_places_of_worship_hsip_geom_geom_idx postgres
7325; 1259 746784 INDEX public wv_str_samb_building_points_geom_geom_idx postgres
7329; 1259 746785 INDEX public wv_str_samb_building_polygons_geom_geom_idx postgres
7343; 1259 746786 INDEX public wv_trn_airport_facilities_geom_geom_idx postgres
7347; 1259 746787 INDEX public wv_trn_airport_proposed_geom_geom_idx postgres
7351; 1259 746788 INDEX public wv_trn_airport_runways_geom_geom_idx postgres
7449; 1259 759073 INDEX public wv_trn_airports_geom_geom_idx msjarvis
7355; 1259 746790 INDEX public wv_trn_intermodal_terminals_geom_geom_idx postgres
7359; 1259 746791 INDEX public wv_trn_mnf_recreation_trails_geom_geom_idx postgres
7363; 1259 746792 INDEX public wv_trn_mnf_roads_geom_geom_idx postgres
7367; 1259 746793 INDEX public wv_trn_railroad_lines_rti_geom_geom_idx postgres
7371; 1259 746794 INDEX public wv_trn_railroads_amtrak_geom_geom_idx postgres
7375; 1259 746795 INDEX public wv_trn_railroads_excursion_geom_geom_idx postgres
7379; 1259 746796 INDEX public wv_trn_railroads_national_network_geom_geom_idx postgres
7383; 1259 746797 INDEX public wv_trn_recreational_trails_geom_geom_idx postgres
7387; 1259 746798 INDEX public wv_trn_roads_interstate_geom_geom_idx postgres
7391; 1259 746799 INDEX public wv_trn_roads_major_4800_geom_geom_idx postgres
7395; 1259 746800 INDEX public wv_trn_roads_state_routes_geom_geom_idx postgres
7399; 1259 746801 INDEX public wv_trn_roads_us_highways_geom_geom_idx postgres
7403; 1259 746802 INDEX public wv_trn_roads_us_routes_geom_geom_idx postgres
7407; 1259 746803 INDEX public wv_trn_whitewater_trails_geom_geom_idx postgres
7452; 1259 759074 INDEX public wv_util_sewer_treatment_plants_geom_geom_idx msjarvis
7411; 1259 746805 INDEX public wv_util_solid_waste_facilities_geom_geom_idx postgres
7000; 1259 746806 INDEX public wv_wv_county_boundaries_24k_topo_updated_2026_utm_geom_geom_idx postgres
7417; 1259 746807 INDEX public wv_wv_county_boundaries_24k_topo_updated_2026_wma_geom_geom_idx postgres
7942; 1259 4134650 INDEX runtime_governance civic_policy_fact_jurisdiction_subject_idx postgres
7995; 1259 4134932 INDEX runtime_governance idx_commons_contribution_group postgres
8001; 1259 4134957 INDEX runtime_governance idx_commons_provenance_domain_key postgres
8009; 1259 4135001 INDEX runtime_governance idx_commons_reconstruction_attempt postgres
7998; 1259 4134945 INDEX runtime_governance idx_commons_vector_group postgres
7970; 1259 4134839 INDEX runtime_governance idx_phi_domain_metrics_domain_time postgres
7975; 1259 4134851 INDEX runtime_governance idx_self_assessment_time postgres
8004; 1259 4134980 INDEX runtime_governance idx_user_partition_user_domain postgres
7528; 1259 1125559 INDEX staging_hazus barbour_geom_geom_idx postgres
7534; 1259 1125586 INDEX staging_hazus berkeley_geom_geom_idx postgres
7531; 1259 1125569 INDEX staging_hazus boone_geom_geom_idx postgres
7537; 1259 1125596 INDEX staging_hazus braxton_geom_geom_idx postgres
7540; 1259 1125606 INDEX staging_hazus brooke_geom_geom_idx postgres
7543; 1259 1125616 INDEX staging_hazus cabell_geom_geom_idx postgres
7546; 1259 1125626 INDEX staging_hazus calhoun_geom_geom_idx postgres
7549; 1259 1125636 INDEX staging_hazus clay_geom_geom_idx postgres
7552; 1259 1125647 INDEX staging_hazus doddridge_geom_geom_idx postgres
7555; 1259 1125657 INDEX staging_hazus fayette_geom_geom_idx postgres
7696; 1259 1126272 INDEX staging_hazus floodplain_100year_geom_geom_idx postgres
7693; 1259 1126207 INDEX staging_hazus floodplain_10year_geom_geom_idx postgres
7699; 1259 1126337 INDEX staging_hazus floodplain_25year_geom_geom_idx postgres
7702; 1259 1126402 INDEX staging_hazus floodplain_50year_geom_geom_idx postgres
7558; 1259 1125672 INDEX staging_hazus gilmer_geom_geom_idx postgres
7561; 1259 1125682 INDEX staging_hazus grant_geom_geom_idx postgres
7564; 1259 1125692 INDEX staging_hazus greenbrier_geom_geom_idx postgres
7675; 1259 1126146 INDEX staging_hazus hampshire_geom_geom_idx postgres
7567; 1259 1125709 INDEX staging_hazus hancock_geom_geom_idx postgres
7570; 1259 1125719 INDEX staging_hazus hardy_geom_geom_idx postgres
7573; 1259 1125732 INDEX staging_hazus harrison_geom_geom_idx postgres
7576; 1259 1125742 INDEX staging_hazus jackson_geom_geom_idx postgres
7579; 1259 1125752 INDEX staging_hazus jefferson_geom_geom_idx postgres
7582; 1259 1125762 INDEX staging_hazus kanawha_geom_geom_idx postgres
7585; 1259 1125774 INDEX staging_hazus lewis_geom_geom_idx postgres
7588; 1259 1125784 INDEX staging_hazus lincoln_geom_geom_idx postgres
7591; 1259 1125794 INDEX staging_hazus logan_geom_geom_idx postgres
7678; 1259 1126157 INDEX staging_hazus marion_geom_geom_idx postgres
7594; 1259 1125807 INDEX staging_hazus marshall_geom_geom_idx postgres
7597; 1259 1125817 INDEX staging_hazus mason_geom_geom_idx postgres
7600; 1259 1125827 INDEX staging_hazus mcdowell_geom_geom_idx postgres
7603; 1259 1125843 INDEX staging_hazus mercer_geom_geom_idx postgres
7681; 1259 1126167 INDEX staging_hazus mineral_geom_geom_idx postgres
7606; 1259 1125853 INDEX staging_hazus mingo_geom_geom_idx postgres
7684; 1259 1126177 INDEX staging_hazus monongalia_geom_geom_idx postgres
7609; 1259 1125867 INDEX staging_hazus monroe_geom_geom_idx postgres
7612; 1259 1125877 INDEX staging_hazus morgan_geom_geom_idx postgres
7615; 1259 1125887 INDEX staging_hazus nicholas_geom_geom_idx postgres
7618; 1259 1125898 INDEX staging_hazus ohio_geom_geom_idx postgres
7621; 1259 1125908 INDEX staging_hazus pendleton_geom_geom_idx postgres
7624; 1259 1125926 INDEX staging_hazus pleasants_geom_geom_idx postgres
7627; 1259 1125936 INDEX staging_hazus pocahontas_geom_geom_idx postgres
7687; 1259 1126187 INDEX staging_hazus preston_geom_geom_idx postgres
7630; 1259 1125958 INDEX staging_hazus putnam_geom_geom_idx postgres
7633; 1259 1125969 INDEX staging_hazus raleigh_geom_geom_idx postgres
7636; 1259 1125997 INDEX staging_hazus randolph_geom_geom_idx postgres
7639; 1259 1126012 INDEX staging_hazus ritchie_geom_geom_idx postgres
7642; 1259 1126022 INDEX staging_hazus roane_geom_geom_idx postgres
7645; 1259 1126032 INDEX staging_hazus summers_geom_geom_idx postgres
7648; 1259 1126044 INDEX staging_hazus taylor_geom_geom_idx postgres
7651; 1259 1126054 INDEX staging_hazus tucker_geom_geom_idx postgres
7654; 1259 1126066 INDEX staging_hazus tyler_geom_geom_idx postgres
7657; 1259 1126076 INDEX staging_hazus upshur_geom_geom_idx postgres
7660; 1259 1126086 INDEX staging_hazus wayne_geom_geom_idx postgres
7663; 1259 1126097 INDEX staging_hazus webster_geom_geom_idx postgres
7690; 1259 1126197 INDEX staging_hazus wetzel_geom_geom_idx postgres
7666; 1259 1126110 INDEX staging_hazus wirt_geom_geom_idx postgres
7669; 1259 1126120 INDEX staging_hazus wood_geom_geom_idx postgres
7672; 1259 1126130 INDEX staging_hazus wyoming_geom_geom_idx postgres
7709; 1259 1127137 INDEX staging_tax_2025 mastersurfwv_2025_geom_geom_idx postgres
7718; 1259 1872971 INDEX staging_tax_districts wv_tax_districts_ll83_geom_geom_idx postgres
7715; 1259 1872102 INDEX staging_tax_districts wv_tax_districts_utm83_geom_geom_idx postgres
7721; 1259 1873840 INDEX staging_tax_districts wv_tax_districts_wma84_geom_geom_idx postgres
8023; 2620 4120114 TRIGGER public gbim_active_collection gbim_active_collection_gate msjarvis_admin
8024; 2620 4120116 TRIGGER public gbim_active_collection gbim_publication_manifest_sync msjarvis_admin
8021; 2606 4134981 FK CONSTRAINT runtime_governance commons_contribution commons_contribution_partition_fk postgres
8022; 2606 4134986 FK CONSTRAINT runtime_governance commons_vector_contribution commons_vector_partition_fk postgres
8871; 0 4134554 MATERIALIZED VIEW DATA public public_admissible_gbim_mv postgres

=== CURRENT runtime_governance objects in msjarvisgis_v2 ===
   kind   |                          name                          
----------+--------------------------------------------------------
 FUNCTION | public_answer_packet(p_geoid text, p_metric_name text)
 FUNCTION | public_geoid_panel(p_geoid text)
 m        | public_admissible_gbim_mv
 TABLE    | commons_phase_status
 TABLE    | commons_provenance_certificate
 TABLE    | commons_release_authorization
 TABLE    | commons_vector_contribution
 TABLE    | public_answer_audit
 v        | public_admissible_gbim
(9 rows)

 indexname | indexdef 
-----------+----------
(0 rows)

 trigger_name | event_manipulation | action_statement 
--------------+--------------------+------------------
(0 rows)

ERROR:  column "phase" does not exist
LINE 1: SELECT phase, status, updated_at
               ^
=== GAP ANALYSIS COMPLETE ===
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild/formal/commons_proofs$ 

