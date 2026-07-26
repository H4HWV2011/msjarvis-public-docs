wv_gis=# CREATE OR REPLACE PROCEDURE public.gbim_load_bg_table(p_bg_table text)
LANGUAGE plpgsql
AS $$
DECLARE
  v_driver RECORD;
  v_sql text;
BEGIN
  SELECT
    d.table_name,
    d.bg_table_name,
    d.pk_column,
    d.geom_column,
    d.metric_column_name
  INTO v_driver
  FROM public.wv_bg_driver AS d
  WHERE d.bg_table_name = replace(p_bg_table, 'public.', '');

  IF NOT FOUND THEN
    RAISE EXCEPTION 'No matching row in public.wv_bg_driver for %', p_bg_table;
  END IF;

  v_sql := format($f$
    WITH src AS (
      SELECT
$$;;ERE r.bg_table = p_bg_table;gbim_id) OR r.company_name IS NULL);geoid',
CREATE PROCEDURE
wv_gis=# CALL public.gbim_load_bg_table('public.wv_bg_env_epa_facilities');

SELECT
  COUNT(*) AS gbim_rows_loaded,
  SUM(CASE WHEN promotion_state = 'authorized' THEN 1 ELSE 0 END) AS authorized_rows,
  SUM(CASE WHEN public_claim_allowed THEN 1 ELSE 0 END) AS public_claim_rows
FROM public.gbim_record
WHERE bg_table = 'public.wv_bg_env_epa_facilities';
ERROR:  relation "public.wv_bg_env_epa_facilities" does not exist
LINE 14:       FROM "public.wv_bg_env_epa_facilities" AS bg
                    ^
QUERY:  
    WITH src AS (
      SELECT
        'public.wv_env_epa_facilities'::text AS source_table,
        'public.wv_bg_env_epa_facilities'::text AS bg_table,
        bg.geoid::text AS geoid,
        'env_epa_facilities_count'::text AS metric_name,
        bg.env_epa_facilities_count::numeric AS metric_value,
        'count'::text AS units,
        'COUNT(DISTINCT gid)'::text AS aggregation,
        'geoid'::text AS join_key,
        to_jsonb(bg) AS record_payload,
        encode(digest(to_jsonb(bg)::text, 'sha256'), 'hex') AS record_hash
      FROM "public.wv_bg_env_epa_facilities" AS bg
    ),
    upsert_record AS (
      INSERT INTO public.gbim_record (
        source_table,
        bg_table,
        geoid,
        metric_name,
        metric_value,
        units,
        aggregation,
        join_key,
        record_payload,
        record_hash,
        observed_date,
        temporal_coverage_label,
        temporal_status,
        ingested_at,
        degradation_status,
        degradation_checked_at,
        updated_at
      )
      SELECT
        s.source_table,
        s.bg_table,
        s.geoid,
        s.metric_name,
        s.metric_value,
        s.units,
        s.aggregation,
        s.join_key,
        s.record_payload,
        s.record_hash,
        NULL::timestamptz AS observed_date,
        CASE
          WHEN t.temporal_date_scraped THEN 'dataset-attested'
          ELSE 'temporal-missing'
        END AS temporal_coverage_label,
        CASE
          WHEN t.temporal_date_scraped THEN 'grounded'
          ELSE 'ungrounded'
        END AS temporal_status,
        now() AS ingested_at,
        'fresh'::text AS degradation_status,
        now() AS degradation_checked_at,
        now() AS updated_at
      FROM src AS s
      JOIN public.wv_table_completion_tracker AS t
        ON t.table_name = 'wv_env_epa_facilities'
      ON CONFLICT (source_table, bg_table, geoid, metric_name)
      DO UPDATE SET
        metric_value = EXCLUDED.metric_value,
        units = EXCLUDED.units,
        aggregation = EXCLUDED.aggregation,
        join_key = EXCLUDED.join_key,
        record_payload = EXCLUDED.record_payload,
        record_hash = EXCLUDED.record_hash,
        temporal_coverage_label = EXCLUDED.temporal_coverage_label,
        temporal_status = EXCLUDED.temporal_status,
        ingested_at = now(),
        degradation_status = 'fresh',
        degradation_checked_at = now(),
        updated_at = now()
      RETURNING gbim_id, geoid
    )
    INSERT INTO public.gbim_provenance (
      gbim_id,
      tracker_table_name,
      bg_join_expanded,
      temporal_date_scraped,
      chroma_ready,
      source_pk_column,
      source_geom_column,
      source_kind,
      derivation_method,
      srid_target,
      sql_pattern,
      provenance_note,
      metadata_company_scraped,
      authority_source
    )
    SELECT
      r.gbim_id,
      t.table_name AS tracker_table_name,
      t.bg_join_expanded,
      t.temporal_date_scraped,
      t.chroma_ready,
      'gid'::text AS source_pk_column,
      'geom_utm17'::text AS source_geom_column,
      'public_postgis_layer'::text AS source_kind,
      'ST_Intersects'::text AS derivation_method,
      26917 AS srid_target,
      'COUNT(DISTINCT src.gid) grouped by bg.geoid'::text AS sql_pattern,
      COALESCE(t.notes, '')::text AS provenance_note,
      false AS metadata_company_scraped,
      'WVGIS Technical Center'::text AS authority_source
    FROM upsert_record AS r
    JOIN public.wv_table_completion_tracker AS t
      ON t.table_name = 'wv_env_epa_facilities'
    ON CONFLICT (gbim_id)
    DO UPDATE SET
      tracker_table_name = EXCLUDED.tracker_table_name,
      bg_join_expanded = EXCLUDED.bg_join_expanded,
      temporal_date_scraped = EXCLUDED.temporal_date_scraped,
      chroma_ready = EXCLUDED.chroma_ready,
      source_pk_column = EXCLUDED.source_pk_column,
      source_geom_column = EXCLUDED.source_geom_column,
      source_kind = EXCLUDED.source_kind,
      derivation_method = EXCLUDED.derivation_method,
      srid_target = EXCLUDED.srid_target,
      sql_pattern = EXCLUDED.sql_pattern,
      provenance_note = EXCLUDED.provenance_note,
      metadata_company_scraped = EXCLUDED.metadata_company_scraped,
      authority_source = EXCLUDED.authority_source;
  
CONTEXT:  PL/pgSQL function gbim_load_bg_table(text) line 161 at EXECUTE
 gbim_rows_loaded | authorized_rows | public_claim_rows 
------------------+-----------------+-------------------
                1 |               1 |                 1
(1 row)

wv_gis=# DO $$
DECLARE
  r RECORD;
BEGIN
  FOR r IN
    SELECT 'public.' || bg_table_name AS bg_table
    FROM public.wv_bg_driver
    ORDER BY bg_table_name
  LOOP
    BEGIN
      CALL public.gbim_load_bg_table(r.bg_table);
      RAISE NOTICE 'GBIM loaded: %', r.bg_table;
    EXCEPTION WHEN OTHERS THEN
      RAISE NOTICE 'GBIM load failed: % -> %', r.bg_table, SQLERRM;
    END;
  END LOOP;
END $$;
NOTICE:  GBIM load failed: public.wv_bg_atm_weather_stations -> relation "public.wv_bg_atm_weather_stations" does not exist
NOTICE:  GBIM load failed: public.wv_bg_bio_biodiversity_rank -> relation "public.wv_bg_bio_biodiversity_rank" does not exist
NOTICE:  GBIM load failed: public.wv_bg_bio_ecoregions -> relation "public.wv_bg_bio_ecoregions" does not exist
NOTICE:  GBIM load failed: public.wv_bg_bio_red_spruce_cover -> relation "public.wv_bg_bio_red_spruce_cover" does not exist
NOTICE:  GBIM load failed: public.wv_bg_blockgroup_representation -> relation "public.wv_bg_blockgroup_representation" does not exist
NOTICE:  GBIM load failed: public.wv_bg_bnd_appalachian_basin_boundary -> relation "public.wv_bg_bnd_appalachian_basin_boundary" does not exist
NOTICE:  GBIM load failed: public.wv_bg_bnd_arc_counties -> relation "public.wv_bg_bnd_arc_counties" does not exist
NOTICE:  GBIM load failed: public.wv_bg_bnd_canaan_valley_nwr -> relation "public.wv_bg_bnd_canaan_valley_nwr" does not exist
NOTICE:  GBIM load failed: public.wv_bg_bnd_census_designated_places -> relation "public.wv_bg_bnd_census_designated_places" does not exist
NOTICE:  GBIM load failed: public.wv_bg_bnd_county_24k -> relation "public.wv_bg_bnd_county_24k" does not exist
NOTICE:  GBIM load failed: public.wv_bg_bnd_county_municipal_dlg -> relation "public.wv_bg_bnd_county_municipal_dlg" does not exist
NOTICE:  GBIM load failed: public.wv_bg_bnd_mnf_basic_ownership -> relation "public.wv_bg_bnd_mnf_basic_ownership" does not exist
NOTICE:  GBIM load failed: public.wv_bg_bnd_mnf_management_prescriptions -> relation "public.wv_bg_bnd_mnf_management_prescriptions" does not exist
NOTICE:  GBIM load failed: public.wv_bg_bnd_mnf_ranger_districts -> relation "public.wv_bg_bnd_mnf_ranger_districts" does not exist
NOTICE:  GBIM load failed: public.wv_bg_bnd_mnf_recreation_campgrounds -> relation "public.wv_bg_bnd_mnf_recreation_campgrounds" does not exist
NOTICE:  GBIM load failed: public.wv_bg_bnd_mnf_recreation_sites -> relation "public.wv_bg_bnd_mnf_recreation_sites" does not exist
NOTICE:  GBIM load failed: public.wv_bg_bnd_mnf_wilderness -> relation "public.wv_bg_bnd_mnf_wilderness" does not exist
NOTICE:  GBIM load failed: public.wv_bg_bnd_morgantown_wards -> relation "public.wv_bg_bnd_morgantown_wards" does not exist
NOTICE:  GBIM load failed: public.wv_bg_bnd_nhd_mussel_streams -> relation "public.wv_bg_bnd_nhd_mussel_streams" does not exist
NOTICE:  GBIM load failed: public.wv_bg_bnd_public_lands_county_city_parks -> relation "public.wv_bg_bnd_public_lands_county_city_parks" does not exist
NOTICE:  GBIM load failed: public.wv_bg_bnd_public_lands_national_forest -> relation "public.wv_bg_bnd_public_lands_national_forest" does not exist
NOTICE:  GBIM load failed: public.wv_bg_bnd_public_lands_national_park -> relation "public.wv_bg_bnd_public_lands_national_park" does not exist
NOTICE:  GBIM load failed: public.wv_bg_bnd_public_lands_nwr -> relation "public.wv_bg_bnd_public_lands_nwr" does not exist
NOTICE:  GBIM load failed: public.wv_bg_bnd_public_lands_state_forests -> relation "public.wv_bg_bnd_public_lands_state_forests" does not exist
NOTICE:  GBIM load failed: public.wv_bg_bnd_public_lands_state_parks -> relation "public.wv_bg_bnd_public_lands_state_parks" does not exist
NOTICE:  GBIM load failed: public.wv_bg_bnd_public_lands_wildlife_resources -> relation "public.wv_bg_bnd_public_lands_wildlife_resources" does not exist
NOTICE:  GBIM load failed: public.wv_bg_bnd_state_boundary_100k -> relation "public.wv_bg_bnd_state_boundary_100k" does not exist
NOTICE:  GBIM load failed: public.wv_bg_bnd_voting_districts_2000 -> relation "public.wv_bg_bnd_voting_districts_2000" does not exist
NOTICE:  GBIM load failed: public.wv_bg_bnd_voting_districts_2002 -> relation "public.wv_bg_bnd_voting_districts_2002" does not exist
NOTICE:  GBIM load failed: public.wv_bg_bnd_workforce_investment_areas -> relation "public.wv_bg_bnd_workforce_investment_areas" does not exist
NOTICE:  GBIM load failed: public.wv_bg_censustracts_census_2020_utm83 -> relation "public.wv_bg_censustracts_census_2020_utm83" does not exist
NOTICE:  GBIM load failed: public.wv_bg_county_boundaries_24k_topo_updated_2026_utm83_gdb -> relation "public.wv_bg_county_boundaries_24k_topo_updated_2026_utm83_gdb" does not exist
NOTICE:  GBIM load failed: public.wv_bg_county_boundaries_24k_topo_updated_2026_wma84_gdb -> relation "public.wv_bg_county_boundaries_24k_topo_updated_2026_wma84_gdb" does not exist
NOTICE:  GBIM load failed: public.wv_bg_eco_abandoned_mine_lands_line -> relation "public.wv_bg_eco_abandoned_mine_lands_line" does not exist
NOTICE:  GBIM load failed: public.wv_bg_eco_abandoned_mine_lands_point -> relation "public.wv_bg_eco_abandoned_mine_lands_point" does not exist
NOTICE:  GBIM load failed: public.wv_bg_eco_abandoned_mine_lands_polygon -> relation "public.wv_bg_eco_abandoned_mine_lands_polygon" does not exist
NOTICE:  GBIM load failed: public.wv_bg_eco_coal_fields -> relation "public.wv_bg_eco_coal_fields" does not exist
NOTICE:  GBIM load failed: public.wv_bg_eco_ezec_communities -> relation "public.wv_bg_eco_ezec_communities" does not exist
NOTICE:  GBIM load failed: public.wv_bg_eco_industrial_sites -> relation "public.wv_bg_eco_industrial_sites" does not exist
NOTICE:  GBIM load failed: public.wv_bg_eco_manufacturing_directory -> relation "public.wv_bg_eco_manufacturing_directory" does not exist
NOTICE:  GBIM load failed: public.wv_bg_eco_mineral_operations -> relation "public.wv_bg_eco_mineral_operations" does not exist
NOTICE:  GBIM load failed: public.wv_bg_eco_mountaintop_removal -> relation "public.wv_bg_eco_mountaintop_removal" does not exist
NOTICE:  GBIM load failed: public.wv_bg_elv_summit_names -> relation "public.wv_bg_elv_summit_names" does not exist
NOTICE:  GBIM load failed: public.wv_bg_env_air_nonattainment -> relation "public.wv_bg_env_air_nonattainment" does not exist
NOTICE:  GBIM load failed: public.wv_bg_env_epa_facilities -> relation "public.wv_bg_env_epa_facilities" does not exist
NOTICE:  GBIM load failed: public.wv_bg_env_timber_removal_volume -> relation "public.wv_bg_env_timber_removal_volume" does not exist
NOTICE:  GBIM load failed: public.wv_bg_env_wildfire_regions -> relation "public.wv_bg_env_wildfire_regions" does not exist
NOTICE:  GBIM load failed: public.wv_bg_env_wind_energy_resources -> relation "public.wv_bg_env_wind_energy_resources" does not exist
NOTICE:  GBIM load failed: public.wv_bg_geo_coal_beds -> relation "public.wv_bg_geo_coal_beds" does not exist
NOTICE:  GBIM load failed: public.wv_bg_geo_geological_map_generalized -> relation "public.wv_bg_geo_geological_map_generalized" does not exist
NOTICE:  GBIM load failed: public.wv_bg_geo_karst -> relation "public.wv_bg_geo_karst" does not exist
NOTICE:  GBIM load failed: public.wv_bg_hazus_floodplain_100year -> relation "public.wv_bg_hazus_floodplain_100year" does not exist
NOTICE:  GBIM load failed: public.wv_bg_hazus_floodplain_10year -> relation "public.wv_bg_hazus_floodplain_10year" does not exist
NOTICE:  GBIM load failed: public.wv_bg_hazus_floodplain_25year -> relation "public.wv_bg_hazus_floodplain_25year" does not exist
NOTICE:  GBIM load failed: public.wv_bg_hazus_floodplain_50year -> relation "public.wv_bg_hazus_floodplain_50year" does not exist
NOTICE:  GBIM load failed: public.wv_bg_hlt_health_providers -> relation "public.wv_bg_hlt_health_providers" does not exist
NOTICE:  GBIM load failed: public.wv_bg_hlt_rural_health_facilities -> relation "public.wv_bg_hlt_rural_health_facilities" does not exist
NOTICE:  GBIM load failed: public.wv_bg_hyd_dams_nid -> relation "public.wv_bg_hyd_dams_nid" does not exist
NOTICE:  GBIM load failed: public.wv_bg_hyd_dams_noncoal -> relation "public.wv_bg_hyd_dams_noncoal" does not exist
NOTICE:  GBIM load failed: public.wv_bg_hyd_hazus_floodplain_zones -> relation "public.wv_bg_hyd_hazus_floodplain_zones" does not exist
NOTICE:  GBIM load failed: public.wv_bg_hyd_high_water_marks -> relation "public.wv_bg_hyd_high_water_marks" does not exist
NOTICE:  GBIM load failed: public.wv_bg_hyd_navigable_waterways -> relation "public.wv_bg_hyd_navigable_waterways" does not exist
NOTICE:  GBIM load failed: public.wv_bg_hyd_navigable_waterways_river_miles -> relation "public.wv_bg_hyd_navigable_waterways_river_miles" does not exist
NOTICE:  GBIM load failed: public.wv_bg_hyd_navigable_waterways_structures -> relation "public.wv_bg_hyd_navigable_waterways_structures" does not exist
NOTICE:  GBIM load failed: public.wv_bg_hyd_springs_100gpm -> relation "public.wv_bg_hyd_springs_100gpm" does not exist
NOTICE:  GBIM load failed: public.wv_bg_hyd_streamflow_stations -> relation "public.wv_bg_hyd_streamflow_stations" does not exist
NOTICE:  GBIM load failed: public.wv_bg_hyd_streams_high_quality -> relation "public.wv_bg_hyd_streams_high_quality" does not exist
NOTICE:  GBIM load failed: public.wv_bg_hyd_streams_national_atlas -> relation "public.wv_bg_hyd_streams_national_atlas" does not exist
NOTICE:  GBIM load failed: public.wv_bg_hyd_streams_tiger -> relation "public.wv_bg_hyd_streams_tiger" does not exist
NOTICE:  GBIM load failed: public.wv_bg_hyd_watershed_boundary_11digit -> relation "public.wv_bg_hyd_watershed_boundary_11digit" does not exist
NOTICE:  GBIM load failed: public.wv_bg_hyd_watershed_boundary_12digit_hu -> relation "public.wv_bg_hyd_watershed_boundary_12digit_hu" does not exist
NOTICE:  GBIM load failed: public.wv_bg_hyd_watershed_boundary_8_10_12 -> relation "public.wv_bg_hyd_watershed_boundary_8_10_12" does not exist
NOTICE:  GBIM load failed: public.wv_bg_loc_census_urbanized_areas -> relation "public.wv_bg_loc_census_urbanized_areas" does not exist
NOTICE:  GBIM load failed: public.wv_bg_loc_county_seats -> relation "public.wv_bg_loc_county_seats" does not exist
NOTICE:  GBIM load failed: public.wv_bg_loc_geodetic_control_points -> relation "public.wv_bg_loc_geodetic_control_points" does not exist
NOTICE:  GBIM load failed: public.wv_bg_loc_populated_places_census -> relation "public.wv_bg_loc_populated_places_census" does not exist
NOTICE:  GBIM load failed: public.wv_bg_loc_sams2_address_road_centerlines -> relation "public.wv_bg_loc_sams2_address_road_centerlines" does not exist
NOTICE:  GBIM load failed: public.wv_bg_mil_army_reserve_facilities -> relation "public.wv_bg_mil_army_reserve_facilities" does not exist
NOTICE:  GBIM load failed: public.wv_bg_mil_national_guard_armories -> relation "public.wv_bg_mil_national_guard_armories" does not exist
NOTICE:  GBIM load failed: public.wv_bg_plc_hazus_level1 -> relation "public.wv_bg_plc_hazus_level1" does not exist
NOTICE:  GBIM load failed: public.wv_bg_plc_regional_planning_councils -> relation "public.wv_bg_plc_regional_planning_councils" does not exist
NOTICE:  GBIM load failed: public.wv_bg_plc_tax_district_boundaries -> relation "public.wv_bg_plc_tax_district_boundaries" does not exist
NOTICE:  GBIM load failed: public.wv_bg_plc_tax_parcels_surface_mineral -> relation "public.wv_bg_plc_tax_parcels_surface_mineral" does not exist
NOTICE:  GBIM load failed: public.wv_bg_rec_fishing_lakes -> relation "public.wv_bg_rec_fishing_lakes" does not exist
NOTICE:  GBIM load failed: public.wv_bg_rec_nps_units -> relation "public.wv_bg_rec_nps_units" does not exist
NOTICE:  GBIM load failed: public.wv_bg_rec_nwr_units -> relation "public.wv_bg_rec_nwr_units" does not exist
NOTICE:  GBIM load failed: public.wv_bg_rec_state_forests -> relation "public.wv_bg_rec_state_forests" does not exist
NOTICE:  GBIM load failed: public.wv_bg_rec_state_parks -> relation "public.wv_bg_rec_state_parks" does not exist
NOTICE:  GBIM load failed: public.wv_bg_rec_trail_points -> relation "public.wv_bg_rec_trail_points" does not exist
NOTICE:  GBIM load failed: public.wv_bg_rec_whitewater_trails -> relation "public.wv_bg_rec_whitewater_trails" does not exist
NOTICE:  GBIM load failed: public.wv_bg_rec_wvdnr_managed_lands -> relation "public.wv_bg_rec_wvdnr_managed_lands" does not exist
NOTICE:  GBIM load failed: public.wv_bg_soc_911_centers -> relation "public.wv_bg_soc_911_centers" does not exist
NOTICE:  GBIM load failed: public.wv_bg_soc_census_blockgroups_2020 -> relation "public.wv_bg_soc_census_blockgroups_2020" does not exist
NOTICE:  GBIM load failed: public.wv_bg_soc_census_blockgroups_2020_utm17 -> relation "public.wv_bg_soc_census_blockgroups_2020_utm17" does not exist
NOTICE:  GBIM load failed: public.wv_bg_soc_census_tracts_2020 -> relation "public.wv_bg_soc_census_tracts_2020" does not exist
NOTICE:  GBIM load failed: public.wv_bg_soc_cities_pop10k -> relation "public.wv_bg_soc_cities_pop10k" does not exist
NOTICE:  GBIM load failed: public.wv_bg_soc_cities_pop2500 -> relation "public.wv_bg_soc_cities_pop2500" does not exist
NOTICE:  GBIM load failed: public.wv_bg_soc_communities_pop_change -> relation "public.wv_bg_soc_communities_pop_change" does not exist
NOTICE:  GBIM load failed: public.wv_bg_soc_courthouses_county -> relation "public.wv_bg_soc_courthouses_county" does not exist
NOTICE:  GBIM load failed: public.wv_bg_soc_courthouses_federal -> relation "public.wv_bg_soc_courthouses_federal" does not exist
NOTICE:  GBIM load failed: public.wv_bg_soc_fish_hatcheries -> relation "public.wv_bg_soc_fish_hatcheries" does not exist
NOTICE:  GBIM load failed: public.wv_bg_soc_fishing_boating_access -> relation "public.wv_bg_soc_fishing_boating_access" does not exist
NOTICE:  GBIM load failed: public.wv_bg_soc_fishing_lakes -> relation "public.wv_bg_soc_fishing_lakes" does not exist
NOTICE:  GBIM load failed: public.wv_bg_soc_higher_ed_facilities -> relation "public.wv_bg_soc_higher_ed_facilities" does not exist
NOTICE:  GBIM load failed: public.wv_bg_soc_national_register_historic_points -> relation "public.wv_bg_soc_national_register_historic_points" does not exist
NOTICE:  GBIM load failed: public.wv_bg_soc_national_register_historic_polygons -> relation "public.wv_bg_soc_national_register_historic_polygons" does not exist
NOTICE:  GBIM load failed: public.wv_bg_soc_places_of_worship_wvgistc -> relation "public.wv_bg_soc_places_of_worship_wvgistc" does not exist
NOTICE:  GBIM load failed: public.wv_bg_soc_population_by_decade -> relation "public.wv_bg_soc_population_by_decade" does not exist
NOTICE:  GBIM load failed: public.wv_bg_soc_towers_am -> relation "public.wv_bg_soc_towers_am" does not exist
NOTICE:  GBIM load failed: public.wv_bg_soc_towers_asr -> relation "public.wv_bg_soc_towers_asr" does not exist
NOTICE:  GBIM load failed: public.wv_bg_soc_towers_cellular -> relation "public.wv_bg_soc_towers_cellular" does not exist
NOTICE:  GBIM load failed: public.wv_bg_soc_towers_fm -> relation "public.wv_bg_soc_towers_fm" does not exist
NOTICE:  GBIM load failed: public.wv_bg_soc_towers_microwave -> relation "public.wv_bg_soc_towers_microwave" does not exist
NOTICE:  GBIM load failed: public.wv_bg_soc_towers_pager -> relation "public.wv_bg_soc_towers_pager" does not exist
NOTICE:  GBIM load failed: public.wv_bg_soc_towers_private -> relation "public.wv_bg_soc_towers_private" does not exist
NOTICE:  GBIM load failed: public.wv_bg_soc_towers_tv -> relation "public.wv_bg_soc_towers_tv" does not exist
NOTICE:  GBIM load failed: public.wv_bg_soc_zcta_2020 -> relation "public.wv_bg_soc_zcta_2020" does not exist
NOTICE:  GBIM load failed: public.wv_bg_str_bridges -> relation "public.wv_bg_str_bridges" does not exist
NOTICE:  GBIM load failed: public.wv_bg_str_flood_atrisk_structures -> relation "public.wv_bg_str_flood_atrisk_structures" does not exist
NOTICE:  GBIM load failed: public.wv_bg_str_parole_offices -> relation "public.wv_bg_str_parole_offices" does not exist
NOTICE:  GBIM load failed: public.wv_bg_str_places_of_worship_hsip -> relation "public.wv_bg_str_places_of_worship_hsip" does not exist
NOTICE:  GBIM load failed: public.wv_bg_str_samb_building_points -> relation "public.wv_bg_str_samb_building_points" does not exist
NOTICE:  GBIM load failed: public.wv_bg_str_samb_building_polygons -> relation "public.wv_bg_str_samb_building_polygons" does not exist
NOTICE:  GBIM load failed: public.wv_bg_tax_districts_2023 -> relation "public.wv_bg_tax_districts_2023" does not exist
NOTICE:  GBIM load failed: public.wv_bg_tax_master_surf_2025 -> relation "public.wv_bg_tax_master_surf_2025" does not exist
NOTICE:  GBIM load failed: public.wv_bg_trn_airport_facilities -> relation "public.wv_bg_trn_airport_facilities" does not exist
NOTICE:  GBIM load failed: public.wv_bg_trn_airport_proposed -> relation "public.wv_bg_trn_airport_proposed" does not exist
NOTICE:  GBIM load failed: public.wv_bg_trn_airport_runways -> relation "public.wv_bg_trn_airport_runways" does not exist
NOTICE:  GBIM load failed: public.wv_bg_trn_airports -> relation "public.wv_bg_trn_airports" does not exist
NOTICE:  GBIM load failed: public.wv_bg_trn_intermodal_terminals -> relation "public.wv_bg_trn_intermodal_terminals" does not exist
NOTICE:  GBIM load failed: public.wv_bg_trn_mnf_recreation_trails -> relation "public.wv_bg_trn_mnf_recreation_trails" does not exist
NOTICE:  GBIM load failed: public.wv_bg_trn_mnf_roads -> relation "public.wv_bg_trn_mnf_roads" does not exist
NOTICE:  GBIM load failed: public.wv_bg_trn_railroad_lines_rti -> relation "public.wv_bg_trn_railroad_lines_rti" does not exist
NOTICE:  GBIM load failed: public.wv_bg_trn_railroads_amtrak -> relation "public.wv_bg_trn_railroads_amtrak" does not exist
NOTICE:  GBIM load failed: public.wv_bg_trn_railroads_excursion -> relation "public.wv_bg_trn_railroads_excursion" does not exist
NOTICE:  GBIM load failed: public.wv_bg_trn_railroads_national_network -> relation "public.wv_bg_trn_railroads_national_network" does not exist
NOTICE:  GBIM load failed: public.wv_bg_trn_recreational_trails -> relation "public.wv_bg_trn_recreational_trails" does not exist
NOTICE:  GBIM load failed: public.wv_bg_trn_roads_interstate -> relation "public.wv_bg_trn_roads_interstate" does not exist
NOTICE:  GBIM load failed: public.wv_bg_trn_roads_major_4800 -> relation "public.wv_bg_trn_roads_major_4800" does not exist
NOTICE:  GBIM load failed: public.wv_bg_trn_roads_state_routes -> relation "public.wv_bg_trn_roads_state_routes" does not exist
NOTICE:  GBIM load failed: public.wv_bg_trn_roads_us_highways -> relation "public.wv_bg_trn_roads_us_highways" does not exist
NOTICE:  GBIM load failed: public.wv_bg_trn_roads_us_routes -> relation "public.wv_bg_trn_roads_us_routes" does not exist
NOTICE:  GBIM load failed: public.wv_bg_trn_whitewater_trails -> relation "public.wv_bg_trn_whitewater_trails" does not exist
NOTICE:  GBIM load failed: public.wv_bg_wv_county_boundaries_24k_topo_updated_2026_utm83 -> relation "public.wv_bg_wv_county_boundaries_24k_topo_updated_2026_utm83" does not exist
NOTICE:  GBIM load failed: public.wv_bg_wv_county_boundaries_24k_topo_updated_2026_wma84 -> relation "public.wv_bg_wv_county_boundaries_24k_topo_updated_2026_wma84" does not exist
DO
wv_gis=# SELECT
  COUNT(*) AS total_gbim_records,
  SUM(CASE WHEN promotion_state = 'authorized' THEN 1 ELSE 0 END) AS authorized_records,
  SUM(CASE WHEN public_claim_allowed THEN 1 ELSE 0 END) AS public_claim_records
FROM public.gbim_record;

SELECT
  bg_table,
  COUNT(*) AS rows_per_bg_table,
  SUM(CASE WHEN promotion_state = 'authorized' THEN 1 ELSE 0 END) AS authorized_rows
FROM public.gbim_record
GROUP BY bg_table
ORDER BY bg_table;

SELECT *
FROM public.gbim_response
WHERE bg_table = 'public.wv_bg_env_epa_facilities'
ORDER BY geoid
LIMIT 10;
 total_gbim_records | authorized_records | public_claim_records 
--------------------+--------------------+----------------------
                  1 |                  1 |                    1
(1 row)

            bg_table             | rows_per_bg_table | authorized_rows 
---------------------------------+-------------------+-----------------
 public.wv_bg_env_epa_facilities |                 1 |               1
(1 row)

               gbim_id                | gbim_version |         source_table         |            bg_table             |    geoid     |       metric_name        | metric_value | units |     aggregation     | join_key |                      record_payload                      |                           record_hash                            | chroma_collections_has | chroma_collections_feature_hash | promotion_state | public_claim_allowed | under_whose_authority  |      company_name      | observed_date | temporal_coverage_label | temporal_status |          ingested_at          | degradation_status |    degradation_checked_at     |          created_at           |          updated_at           |  tracker_table_name   | bg_join_expanded | temporal_date_scraped | chroma_ready | source_pk_column | source_geom_column |     source_kind      | derivation_method | srid_target |                 sql_pattern                 |                                                              provenance_note                                                              | metadata_company_scraped |    authority_source    
--------------------------------------+--------------+------------------------------+---------------------------------+--------------+--------------------------+--------------+-------+---------------------+----------+----------------------------------------------------------+------------------------------------------------------------------+------------------------+---------------------------------+-----------------+----------------------+------------------------+------------------------+---------------+-------------------------+-----------------+-------------------------------+--------------------+-------------------------------+-------------------------------+-------------------------------+-----------------------+------------------+-----------------------+--------------+------------------+--------------------+----------------------+-------------------+-------------+---------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+------------------------
 ca9612dc-d306-4818-a7fc-47fe6d8e7ac2 | 1.0          | public.wv_env_epa_facilities | public.wv_bg_env_epa_facilities | 540019655001 | env_epa_facilities_count |            2 | count | COUNT(DISTINCT gid) | geoid    | {"geoid": "540019655001", "env_epa_facilities_count": 2} | 67a193a7b8b198ea5de9336cac39158753d1ce3aa837eeaef4abffb0a3851155 | f                      |                                 | authorized      | t                    | WVGIS Technical Center | WVGIS Technical Center |               |                         |                 | 2026-07-26 17:13:13.311113-04 | fresh              | 2026-07-26 17:13:13.311113-04 | 2026-07-26 17:13:13.311113-04 | 2026-07-26 17:13:13.334642-04 | wv_env_epa_facilities | t                | t                     | t            | gid              | geom_utm17         | public_postgis_layer | ST_Intersects     |       26917 | COUNT(DISTINCT src.gid) grouped by bg.geoid | Temporal/date columns detected via information_schema scan; Temporal attributes present in schema; BG expansion: wv_bg_env_epa_facilities | f                        | WVGIS Technical Center
(1 row)

wv_gis=# DROP VIEW IF EXISTS public.gbim_response_envelope;

CREATE OR REPLACE VIEW public.gbim_response_envelope AS
SELECT
  r.gbim_id,
  jsonb_build_object(
    'gbim_version', r.gbim_version,
    'request', jsonb_build_object(
      'request_id', 'gbim_' || replace(r.gbim_id::text, '-', ''),
      'query_text', 'What is ' || r.metric_name || ' for blockgroup ' || r.geoid || '?',
      'requested_at', to_char(now() AT TIME ZONE 'UTC', 'YYYY-MM-DD"T"HH24:MI:SS"Z"'),
      'actor', 'public_ui',
      'scope', jsonb_build_object(
        'jurisdiction', 'wv',
        'place_text', 'Blockgroup ' || r.geoid,
        'topic', split_part(replace(r.source_table, 'public.wv_', ''), '_', 1)
      )
    ),
    'answer', jsonb_build_object(
      'status', CASE
        WHEN r.public_claim_allowed THEN 'authorized'
        ELSE 'candidate'
      END,
      'mode', 'grounded_fact',
      'headline', 'Blockgroup ' || r.geoid || ' has ' || COALESCE(r.metric_value::text, 'nullFROM public.gbim_response AS r;.public_claim_allowedscraped::text,aset-attested'),m ' || r.bg
NOTICE:  view "gbim_response_envelope" does not exist, skipping
DROP VIEW
CREATE VIEW
wv_gis=# SELECT envelope
FROM public.gbim_response_envelope
WHERE gbim_id IN (
  SELECT gbim_id
  FROM public.gbim_record
  WHERE bg_table = 'public.wv_bg_env_epa_facilities'
    AND geoid = '540019655001'
    AND metric_name = 'env_epa_facilities_count'
);
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    envelope                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 {"data": {"units": "count", "bg_table": "public.wv_bg_env_epa_facilities", "join_key": "geoid", "aggregation": "COUNT(DISTINCT gid)", "metric_name": "env_epa_facilities_count", "metric_value": 2, "source_table": "public.wv_env_epa_facilities"}, "answer": {"mode": "grounded_fact", "status": "authorized", "headline": "Blockgroup 540019655001 has 2 for env_epa_facilities_count.", "narrative": "GBIM read 2 from public.wv_bg_env_epa_facilities for blockgroup 540019655001.", "confidence": {"basis": "authorized_tracker_state", "value": 0.99}}, "request": {"actor": "public_ui", "scope": {"topic": "env", "place_text": "Blockgroup 540019655001", "jurisdiction": "wv"}, "query_text": "What is env_epa_facilities_count for blockgroup 540019655001?", "request_id": "gbim_ca9612dcd3064818a7fc47fe6d8e7ac2", "requested_at": "2026-07-26T21:18:54Z"}, "spacetime": {"when": {"derived_from": "table temporal metadata", "observed_date": null, "coverage_label": "dataset-attested", "temporal_status": "grounded"}, "where": {"geoid": "540019655001", "jurisdiction": "WV", "geography_type": "blockgroup", "source_geometry_table": "public.wv_bg_base"}}, "provenance": {"sources": [{"table": "public.wv_env_epa_facilities", "pk_column": "gid", "geom_column": "geom_utm17", "source_kind": "public_postgis_layer"}, {"table": "public.wv_bg_env_epa_facilities", "derivation": "blockgroup spatial intersection"}], "tracker": {"table_name": "wv_env_epa_facilities", "chroma_ready": true, "bg_join_expanded": true, "temporal_date_scraped": true}, "derivation": {"method": "ST_Intersects", "sql_pattern": "COUNT(DISTINCT src.gid) grouped by bg.geoid", "srid_target": 26917}}, "gbim_version": "1.0", "admissibility": {"reasons": ["bg_join_expanded=true", "temporal_date_scraped=true", "chroma_ready=true"], "promotion_state": "authorized", "sandbox_bypassed": false, "public_claim_allowed": true}}
(1 row)

wv_gis=# SELECT envelope
FROM public.gbim_response_envelope
WHERE gbim_id IN (
  SELECT gbim_id
  FROM public.gbim_record
  WHERE bg_table = 'public.wv_bg_env_epa_facilities'
)
ORDER BY gbim_id;
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    envelope                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 {"data": {"units": "count", "bg_table": "public.wv_bg_env_epa_facilities", "join_key": "geoid", "aggregation": "COUNT(DISTINCT gid)", "metric_name": "env_epa_facilities_count", "metric_value": 2, "source_table": "public.wv_env_epa_facilities"}, "answer": {"mode": "grounded_fact", "status": "authorized", "headline": "Blockgroup 540019655001 has 2 for env_epa_facilities_count.", "narrative": "GBIM read 2 from public.wv_bg_env_epa_facilities for blockgroup 540019655001.", "confidence": {"basis": "authorized_tracker_state", "value": 0.99}}, "request": {"actor": "public_ui", "scope": {"topic": "env", "place_text": "Blockgroup 540019655001", "jurisdiction": "wv"}, "query_text": "What is env_epa_facilities_count for blockgroup 540019655001?", "request_id": "gbim_ca9612dcd3064818a7fc47fe6d8e7ac2", "requested_at": "2026-07-26T21:19:01Z"}, "spacetime": {"when": {"derived_from": "table temporal metadata", "observed_date": null, "coverage_label": "dataset-attested", "temporal_status": "grounded"}, "where": {"geoid": "540019655001", "jurisdiction": "WV", "geography_type": "blockgroup", "source_geometry_table": "public.wv_bg_base"}}, "provenance": {"sources": [{"table": "public.wv_env_epa_facilities", "pk_column": "gid", "geom_column": "geom_utm17", "source_kind": "public_postgis_layer"}, {"table": "public.wv_bg_env_epa_facilities", "derivation": "blockgroup spatial intersection"}], "tracker": {"table_name": "wv_env_epa_facilities", "chroma_ready": true, "bg_join_expanded": true, "temporal_date_scraped": true}, "derivation": {"method": "ST_Intersects", "sql_pattern": "COUNT(DISTINCT src.gid) grouped by bg.geoid", "srid_target": 26917}}, "gbim_version": "1.0", "admissibility": {"reasons": ["bg_join_expanded=true", "temporal_date_scraped=true", "chroma_ready=true"], "promotion_state": "authorized", "sandbox_bypassed": false, "public_claim_allowed": true}}
(1 row)

wv_gis=# SELECT envelope
FROM public.gbim_response_envelope
WHERE gbim_id IN (
  SELECT gbim_id
  FROM public.gbim_record
  WHERE public_claim_allowed = true
)
ORDER BY gbim_id;
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    envelope                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 {"data": {"units": "count", "bg_table": "public.wv_bg_env_epa_facilities", "join_key": "geoid", "aggregation": "COUNT(DISTINCT gid)", "metric_name": "env_epa_facilities_count", "metric_value": 2, "source_table": "public.wv_env_epa_facilities"}, "answer": {"mode": "grounded_fact", "status": "authorized", "headline": "Blockgroup 540019655001 has 2 for env_epa_facilities_count.", "narrative": "GBIM read 2 from public.wv_bg_env_epa_facilities for blockgroup 540019655001.", "confidence": {"basis": "authorized_tracker_state", "value": 0.99}}, "request": {"actor": "public_ui", "scope": {"topic": "env", "place_text": "Blockgroup 540019655001", "jurisdiction": "wv"}, "query_text": "What is env_epa_facilities_count for blockgroup 540019655001?", "request_id": "gbim_ca9612dcd3064818a7fc47fe6d8e7ac2", "requested_at": "2026-07-26T21:19:07Z"}, "spacetime": {"when": {"derived_from": "table temporal metadata", "observed_date": null, "coverage_label": "dataset-attested", "temporal_status": "grounded"}, "where": {"geoid": "540019655001", "jurisdiction": "WV", "geography_type": "blockgroup", "source_geometry_table": "public.wv_bg_base"}}, "provenance": {"sources": [{"table": "public.wv_env_epa_facilities", "pk_column": "gid", "geom_column": "geom_utm17", "source_kind": "public_postgis_layer"}, {"table": "public.wv_bg_env_epa_facilities", "derivation": "blockgroup spatial intersection"}], "tracker": {"table_name": "wv_env_epa_facilities", "chroma_ready": true, "bg_join_expanded": true, "temporal_date_scraped": true}, "derivation": {"method": "ST_Intersects", "sql_pattern": "COUNT(DISTINCT src.gid) grouped by bg.geoid", "srid_target": 26917}}, "gbim_version": "1.0", "admissibility": {"reasons": ["bg_join_expanded=true", "temporal_date_scraped=true", "chroma_ready=true"], "promotion_state": "authorized", "sandbox_bypassed": false, "public_claim_allowed": true}}
(1 row)

wv_gis=# 

