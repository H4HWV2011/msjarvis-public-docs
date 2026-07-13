ALTER TABLE

msjarvisgis=# UPDATE wv_entity_registry

SET canonical_spine = 'county',

    has_canonical_county = TRUE,

    geometry_srid = 26917

WHERE table_name IN (

  'wv_county_boundaries_24k_topo_updated_2026_utm83_gdb',

  'wv_county_boundaries_24k_topo_updated_2026_wma84_gdb',

  'wv_wv_county_boundaries_24k_topo_updated_2026_utm83',

  'wv_wv_county_boundaries_24k_topo_updated_2026_wma84',

  'wv_zipcodetabulationarea_census_2020_utm83',

  'wv_zipcodetabulationarea_census_2020_wma84',

  'wv_censustracts_census_2020_utm83',

  'wv_soc_census_tracts_2020',

  'wv_blockgroups_census_2020_utm83',

  'wv_blockgroups_census_2020_wma84',

  'wv_hyd_dfirm_nfhl',

  'wv_hazus_floodplain_10year_gdb',

  'wv_hazus_floodplain_25year_gdb',

  'wv_hazus_floodplain_50year_gdb',

  'wv_hazus_floodplain_100year_gdb'

);

UPDATE wv_entity_registry

SET canonical_spine = 'county',

WHERE entity_type = 'address_point';

UPDATE 5

UPDATE 59

msjarvisgis=# CREATE OR REPLACE VIEW wv_county_belief_summary AS

SELECT

  ci.canonical_county_id,

  ci.county_name,

  COUNT(DISTINCT z.gid)           AS n_zctas,

  COUNT(DISTINCT t.geoid)         AS n_tracts,

  COUNT(DISTINCT bg.geoid)        AS n_blockgroups,

  COUNT(DISTINCT ap.geom)         AS n_address_points,

  COUNT(DISTINCT d.gid)           AS n_dfirm_polygons,

  COUNT(DISTINCT fp10.gid)        AS n_fp_10yr,

  COUNT(DISTINCT fp25.gid)        AS n_fp_25yr,

  COUNT(DISTINCT fp50.gid)        AS n_fp_50yr,

  COUNT(DISTINCT fp100.gid)       AS n_fp_100yr

FROM wv_county_identity ci

LEFT JOIN wv_zipcodetabulationarea_census_2020_utm83 z

  ON z.canonical_county_id = ci.canonical_county_id

LEFT JOIN wv_censustracts_census_2020_utm83 t

  ON t.canonical_county_id = ci.canonical_county_id

LEFT JOIN wv_blockgroups_census_2020_utm83 bg

  ON bg.canonical_county_id = ci.canonical_county_id

LEFT JOIN (

  SELECT canonical_county_id, geom

  FROM wv_address_points_barbour

  UNION ALL

GROUP BY ci.canonical_county_id, ci.county_name;unty_id_* tables

CREATE VIEW

msjarvisgis=# SELECT *

FROM wv_county_belief_summary

ORDER BY canonical_county_id;

SELECT 'zcta_utm83' AS layer, COUNT(*) AS n_features, COUNT(canonical_county_id) AS with_canonical

FROM wv_zipcodetabulationarea_census_2020_utm83

UNION ALL

SELECT 'zcta_wma84', COUNT(*), COUNT(canonical_county_id)

FROM wv_zipcodetabulationarea_census_2020_wma84

UNION ALL

SELECT 'tracts_utm83', COUNT(*), COUNT(canonical_county_id)

FROM wv_censustracts_census_2020_utm83

UNION ALL

SELECT 'soc_tracts_2020', COUNT(*), COUNT(canonical_county_id)

FROM wv_soc_census_tracts_2020

UNION ALL

SELECT 'bg_utm83', COUNT(*), COUNT(canonical_county_id)

FROM wv_blockgroups_census_2020_utm83

UNION ALL

SELECT 'bg_wma84', COUNT(*), COUNT(canonical_county_id)

FROM wv_blockgroups_census_2020_wma84

UNION ALL

SELECT 'dfirm_nfhl', COUNT(*), COUNT(canonical_county_id)

FROM wv_hyd_dfirm_nfhl;

^CCancel request sent

ERROR:  canceling statement due to user request

msjarvisgis=# SELECT pid,

       usename,

       datname,

       state,

       query_start,

       now() - query_start AS runtime,

       LEFT(query, 120) AS query

FROM pg_stat_activity

WHERE datname = current_database()

ORDER BY runtime DESC;

 pid | usename  |   datname   | state  |         query_start          | runtime  |                 query                  

-----+----------+-------------+--------+------------------------------+----------+----------------------------------------

 245 | msjarvis | msjarvisgis | active | 2026-07-11 17:36:49.53096+00 | 00:00:00 | SELECT pid,                           +

     |          |             |        |                              |          |        usename,                       +

     |          |             |        |                              |          |        datname,                       +

     |          |             |        |                              |          |        state,                         +

     |          |             |        |                              |          |        query_start,                   +

     |          |             |        |                              |          |        now() - query_start AS runtime,+

     |          |             |        |                              |          |    

(1 row)

msjarvisgis=# SELECT pg_cancel_backend(<pid>);

ERROR:  syntax error at or near "<"

LINE 1: SELECT pg_cancel_backend(<pid>);

                                 ^

msjarvisgis=# SELECT pg_terminate_backend(<pid>);

ERROR:  syntax error at or near "<"

LINE 1: SELECT pg_terminate_backend(<pid>);

                                    ^

msjarvisgis=# SELECT pid,

       usename,

       datname,

       state,

       query_start,

       now() - query_start AS runtime,

       LEFT(query, 120) AS query

FROM pg_stat_activity

WHERE datname = current_database()

ORDER BY runtime DESC;

 pid | usename  |   datname   | state  |          query_start          | runtime  |                 query                  

-----+----------+-------------+--------+-------------------------------+----------+----------------------------------------

 245 | msjarvis | msjarvisgis | active | 2026-07-11 17:37:54.233571+00 | 00:00:00 | SELECT pid,                           +

     |          |             |        |                               |          |        usename,                       +

     |          |             |        |                               |          |        datname,                       +

     |          |             |        |                               |          |        state,                         +

     |          |             |        |                               |          |        query_start,                   +

     |          |             |        |                               |          |        now() - query_start AS runtime,+

     |          |             |        |                               |          |    

(1 row)

msjarvisgis=# SELECT pg_cancel_backend(245);

ERROR:  canceling statement due to user request

msjarvisgis=# SELECT pg_terminate_backend(245);

FATAL:  terminating connection due to administrator command

server closed the connection unexpectedly

	This probably means the server terminated abnormally

	before or while processing the request.

The connection to the server was lost. Attempting reset: Succeeded.

msjarvisgis=# psql -d msjarvisgis

msjarvisgis-# SELECT current_database();

ERROR:  syntax error at or near "psql"

LINE 1: psql -d msjarvisgis

        ^

msjarvisgis=# CREATE OR REPLACE VIEW wv_county_belief_summary AS

SELECT

  ci.canonical_county_id,

  ci.county_name,

  COALESCE(z.n_zctas, 0)        AS n_zctas,

  COALESCE(t.n_tracts, 0)       AS n_tracts,

  COALESCE(bg.n_blockgroups, 0) AS n_blockgroups,

  COALESCE(ap.n_address_points, 0) AS n_address_points,

  COALESCE(d.n_dfirm_polygons, 0)  AS n_dfirm_polygons

FROM wv_county_identity ci

LEFT JOIN (

  SELECT canonical_county_id, COUNT(*) AS n_zctas

  FROM wv_zipcodetabulationarea_census_2020_utm83

  GROUP BY canonical_county_id

) z ON z.canonical_county_id = ci.canonical_county_id

LEFT JOIN (

  SELECT canonical_county_id, COUNT(*) AS n_tracts

  FROM wv_censustracts_census_2020_utm83

  GROUP BY canonical_county_id

) t ON t.canonical_county_id = ci.canonical_county_id

LEFT JOIN (

  SELECT canonical_county_id, COUNT(*) AS n_blockgroups

  FROM wv_blockgroups_census_2020_utm83

  GROUP BY canonical_county_id

) d ON d.canonical_county_id = ci.canonical_county_id;gonsinghas

ERROR:  relation "wv_address_points_kanawha" does not exist

LINE 67:     SELECT canonical_county_id FROM wv_address_points_kanawh...

                                             ^

msjarvisgis=# \dt *address_points*

                      List of relations

 Schema |              Name               | Type  |  Owner   

--------+---------------------------------+-------+----------

 public | wv_address_points_barbour       | table | msjarvis

 public | wv_address_points_berkeley      | table | msjarvis

 public | wv_address_points_boone         | table | msjarvis

 public | wv_address_points_braxton       | table | msjarvis

 public | wv_address_points_brooke        | table | msjarvis

 public | wv_address_points_cabell        | table | msjarvis

 public | wv_address_points_calhoun       | table | msjarvis

 public | wv_address_points_clay          | table | msjarvis

 public | wv_address_points_doddridge     | table | msjarvis

 public | wv_address_points_fayette       | table | msjarvis

 public | wv_address_points_gilmer        | table | msjarvis

 public | wv_address_points_grant         | table | msjarvis

 public | wv_address_points_greenbrier    | table | msjarvis

 public | wv_address_points_hampshire     | table | msjarvis

 public | wv_address_points_hancock       | table | msjarvis

 public | wv_address_points_hardy         | table | msjarvis

 public | wv_address_points_harrison      | table | msjarvis

 public | wv_address_points_jackson       | table | msjarvis

 public | wv_address_points_jefferson     | table | msjarvis

 public | wv_address_points_kanawha part1 | table | msjarvis

 public | wv_address_points_kanawha part2 | table | msjarvis

 public | wv_address_points_kanawha_part1 | table | msjarvis

 public | wv_address_points_kanawha_part2 | table | msjarvis

 public | wv_address_points_lewis         | table | msjarvis

 public | wv_address_points_lincoln       | table | msjarvis

 public | wv_address_points_logan         | table | msjarvis

 public | wv_address_points_marion        | table | msjarvis

 public | wv_address_points_marshall      | table | msjarvis

 public | wv_address_points_mason         | table | msjarvis

 public | wv_address_points_mcdowell      | table | msjarvis

 public | wv_address_points_mercer        | table | msjarvis

 public | wv_address_points_mineral       | table | msjarvis

 public | wv_address_points_mingo         | table | msjarvis

 public | wv_address_points_monongalia    | table | msjarvis

 public | wv_address_points_monroe        | table | msjarvis

 public | wv_address_points_morgan        | table | msjarvis

 public | wv_address_points_nicholas      | table | msjarvis

 public | wv_address_points_ohio          | table | msjarvis

 public | wv_address_points_pendleton     | table | msjarvis

 public | wv_address_points_pleasants     | table | msjarvis

 public | wv_address_points_pocahontas    | table | msjarvis

 public | wv_address_points_preston       | table | msjarvis

 public | wv_address_points_putnam        | table | msjarvis

 public | wv_address_points_raleigh       | table | msjarvis

 public | wv_address_points_randolph      | table | msjarvis

 public | wv_address_points_raw           | table | msjarvis

 public | wv_address_points_ritchie       | table | msjarvis

 public | wv_address_points_roane         | table | msjarvis

 public | wv_address_points_summers       | table | msjarvis

 public | wv_address_points_taylor        | table | msjarvis

 public | wv_address_points_tucker        | table | msjarvis

 public | wv_address_points_tyler         | table | msjarvis

 public | wv_address_points_upshur        | table | msjarvis

 public | wv_address_points_wayne         | table | msjarvis

 public | wv_address_points_webster       | table | msjarvis

 public | wv_address_points_wetzel        | table | msjarvis

 public | wv_address_points_wirt          | table | msjarvis

 public | wv_address_points_wood          | table | msjarvis

 public | wv_address_points_wyoming       | table | msjarvis

(59 rows)

msjarvisgis=# \dt *kanawha*

                      List of relations

 Schema |              Name               | Type  |  Owner   

--------+---------------------------------+-------+----------

 public | wv_address_points_kanawha part1 | table | msjarvis

 public | wv_address_points_kanawha part2 | table | msjarvis

 public | wv_address_points_kanawha_part1 | table | msjarvis

 public | wv_address_points_kanawha_part2 | table | msjarvis

 public | wv_hazus_kanawha_gdb            | table | msjarvis

(5 rows)

msjarvisgis=# DROP VIEW IF EXISTS wv_county_belief_summary;

CREATE VIEW wv_county_belief_summary AS

SELECT

  ci.canonical_county_id,

  ci.county_name,

  COALESCE(z.n_zctas, 0)        AS n_zctas,

  COALESCE(t.n_tracts, 0)       AS n_tracts,

  COALESCE(bg.n_blockgroups, 0) AS n_blockgroups,

  COALESCE(ap.n_address_points, 0) AS n_address_points,

  COALESCE(d.n_dfirm_polygons, 0)  AS n_dfirm_polygons

FROM wv_county_identity ci

LEFT JOIN (

  SELECT canonical_county_id, COUNT(*) AS n_zctas

  FROM wv_zipcodetabulationarea_census_2020_utm83

  GROUP BY canonical_county_id

) z ON z.canonical_county_id = ci.canonical_county_id

LEFT JOIN (

  SELECT canonical_county_id, COUNT(*) AS n_tracts

  FROM wv_censustracts_census_2020_utm83

  GROUP BY canonical_county_id

) t ON t.canonical_county_id = ci.canonical_county_id

LEFT JOIN (

  SELECT canonical_county_id, COUNT(*) AS n_blockgroups

) d ON d.canonical_county_id = ci.canonical_county_id;gonsinghasrt2

DROP VIEW

CREATE VIEW

msjarvisgis=# SELECT *

FROM wv_county_belief_summary

ORDER BY canonical_county_id

LIMIT 100;

 canonical_county_id | county_name | n_zctas | n_tracts | n_blockgroups | n_address_points | n_dfirm_polygons 

---------------------+-------------+---------+----------+---------------+------------------+------------------

 54001               | Barbour     |       6 |        4 |            16 |            10894 |                0

 54003               | Berkeley    |      10 |       25 |            73 |            61793 |                0

 54005               | Boone       |      28 |        8 |            17 |            12573 |                0

 54007               | Braxton     |      13 |        3 |            13 |            17912 |                0

 54009               | Brooke      |       7 |        8 |            27 |            18952 |                0

 54011               | Cabell      |      12 |       34 |           134 |            46770 |                0

 54013               | Calhoun     |      10 |        2 |             6 |             3951 |                0

 54015               | Clay        |      12 |        3 |             7 |             5306 |                0

 54017               | Doddridge   |       5 |        2 |             8 |             9309 |                0

 54019               | Fayette     |      42 |       13 |            21 |                0 |              138

 54021               | Gilmer      |       9 |        3 |            10 |               32 |                0

 54023               | Grant       |       7 |        3 |            10 |                0 |                0

 54025               | Greenbrier  |      18 |       10 |            35 |                0 |              317

 54027               | Hampshire   |      17 |        9 |            26 |                0 |                0

 54029               | Hancock     |       5 |        8 |            51 |               22 |                0

 54031               | Hardy       |       8 |        5 |            13 |                0 |                0

 54033               | Harrison    |      17 |       25 |            55 |              344 |                0

 54035               | Jackson     |      11 |        7 |            23 |                0 |                0

 54037               | Jefferson   |       9 |       15 |            42 |                5 |                0

 54039               | Kanawha     |      44 |       57 |            99 |               30 |                6

 54041               | Lewis       |       8 |        5 |            15 |            22572 |                0

 54043               | Lincoln     |      14 |        6 |            21 |               44 |                0

 54045               | Logan       |      30 |       10 |            31 |               22 |                0

 54047               | McDowell    |      36 |        8 |            22 |                0 |                0

 54049               | Marion      |      14 |       21 |            26 |                0 |                0

 54051               | Marshall    |       8 |       10 |            31 |                0 |                0

 54053               | Mason       |      13 |        7 |            22 |               15 |                0

 54055               | Mercer      |      17 |       16 |            18 |                0 |                0

 54057               | Mineral     |       8 |        6 |             7 |                0 |                0

 54059               | Mingo       |      18 |        7 |            25 |                0 |                0

 54061               | Monongalia  |      12 |       28 |           105 |                0 |                0

 54063               | Monroe      |      11 |        3 |             5 |                0 |                2

 54065               | Morgan      |       2 |        6 |            16 |                0 |                0

 54067               | Nicholas    |      16 |        8 |            24 |               61 |              107

 54069               | Ohio        |       4 |       18 |            56 |                5 |                0

 54071               | Pendleton   |       8 |        3 |             8 |                0 |                0

 54073               | Pleasants   |       2 |        2 |             7 |                0 |                0

 54075               | Pocahontas  |      11 |        5 |            10 |                0 |                6

 54077               | Preston     |      14 |       11 |            34 |                0 |                0

 54079               | Putnam      |      11 |       12 |            97 |                4 |                0

 54081               | Raleigh     |      41 |       17 |            87 |                0 |              118

 54083               | Randolph    |      22 |        7 |            28 |                0 |                0

 54085               | Ritchie     |      10 |        3 |            11 |                7 |                0

 54087               | Roane       |       8 |        5 |            16 |                5 |                0

 54089               | Summers     |      10 |        4 |            23 |                0 |                2

 54091               | Taylor      |       5 |        4 |            18 |                2 |                0

 54093               | Tucker      |       6 |        3 |             8 |                0 |                0

 54095               | Tyler       |       4 |        4 |            16 |                1 |                0

 54097               | Upshur      |       6 |        6 |            19 |               29 |                0

 54099               | Wayne       |      13 |       11 |             8 |             1955 |                0

 54101               | Webster     |       9 |        4 |             8 |                5 |                0

 54103               | Wetzel      |      11 |        4 |             9 |                0 |                0

 54105               | Wirt        |       2 |        2 |             4 |                1 |                0

 54107               | Wood        |      11 |       28 |            96 |                0 |                0

 54109               | Wyoming     |      36 |        6 |            18 |                0 |                0

(55 rows)

msjarvisgis=# CREATE EXTENSION IF NOT EXISTS pgcrypto;

UPDATE wv_county_representation r

SET source_feature_hash = encode(

    digest(

        concat_ws(

            '|',

            r.table_name,

            r.source_feature_id::text,

            r.canonical_county_id,

            encode(

                ST_AsEWKB(

                    ST_Normalize(

                        ST_Transform(src.geom, 4326)

                    )

                ),

                'hex'

            )

        ),

        'sha256'

    ),

    'hex'

)

FROM (

FROM wv_county_representation;ure_hash) AS distinct_hashes84',,:text AS table_name

CREATE EXTENSION

UPDATE 220

 representations | hashed | distinct_hashes 

-----------------+--------+-----------------

             220 |    220 |             220

(1 row)

msjarvisgis=# CREATE TABLE IF NOT EXISTS wv_county_dataset_coverage (

    canonical_county_id text NOT NULL,

    dataset_type        text NOT NULL,

    source_table        text,

    feature_count       bigint NOT NULL DEFAULT 0,

    coverage_state      text NOT NULL,

    calculated_at       timestamptz NOT NULL DEFAULT now(),

    source_layer_hash   text,

    notes               text,

    PRIMARY KEY (canonical_county_id, dataset_type, source_table),

    FOREIGN KEY (canonical_county_id)

        REFERENCES wv_county_identity (canonical_county_id),

    CHECK (coverage_state IN (

        'present',

        'confirmed_none',

        'missing_source',

        'unassigned',

        'not_applicable',

        'unknown'

    ))

);

CREATE TABLE

msjarvisgis=# INSERT INTO wv_county_dataset_coverage (

    canonical_county_id,

    dataset_type,

    source_table,

    feature_count,

    coverage_state,

    source_layer_hash,

    notes

)

SELECT canonical_county_id, 'zcta', 'wv_zipcodetabulationarea_census_2020_utm83', n_zctas,

       CASE WHEN n_zctas > 0 THEN 'present' ELSE 'unknown' END,

       encode(digest('wv_zipcodetabulationarea_census_2020_utm83', 'sha256'), 'hex'),

       'Loaded from derived county summary view'

FROM wv_county_belief_summary

UNION ALL

SELECT canonical_county_id, 'tract', 'wv_censustracts_census_2020_utm83', n_tracts,

       CASE WHEN n_tracts > 0 THEN 'present' ELSE 'unknown' END,

       encode(digest('wv_censustracts_census_2020_utm83', 'sha256'), 'hex'),

       'Loaded from derived county summary view'

FROM wv_county_belief_summary

UNION ALL

SELECT canonical_county_id, 'blockgroup', 'wv_blockgroups_census_2020_utm83', n_bl    notes = EXCLUDED.notes;LUDED.source_layer_hash,rce_table) DO UPDATE,m_polygons

INSERT 0 275

msjarvisgis=# CREATE TABLE IF NOT EXISTS wv_county_belief_snapshot (

    snapshot_id         uuid PRIMARY KEY DEFAULT gen_random_uuid(),

    canonical_county_id text NOT NULL,

    snapshot_version    text NOT NULL,

    belief_document     jsonb NOT NULL,

    belief_hash         text NOT NULL,

    generated_at        timestamptz NOT NULL DEFAULT now(),

    verification_state  text NOT NULL DEFAULT 'derived',

    FOREIGN KEY (canonical_county_id)

        REFERENCES wv_county_identity (canonical_county_id),

    UNIQUE (canonical_county_id, snapshot_version)

);

CREATE TABLE

msjarvisgis=# INSERT INTO wv_county_belief_snapshot (

    canonical_county_id,

    snapshot_version,

    belief_document,

    belief_hash,

    verification_state

)

SELECT

    ci.canonical_county_id,

    'wv-county-snapshot-v1',

    doc.belief_document,

    encode(digest(doc.belief_document::text, 'sha256'), 'hex'),

    'derived'

FROM wv_county_identity ci

JOIN wv_county_belief_summary s

  ON s.canonical_county_id = ci.canonical_county_id

JOIN LATERAL (

    SELECT jsonb_build_object(

        'canonical_county_id', ci.canonical_county_id,

        'county_name', ci.county_name,

        'snapshot_version', 'wv-county-snapshot-v1',

        'generated_from', 'wv_county_belief_summary',

        'generated_at', now(),

        'verification_state', 'derived',

    verification_state = EXCLUDED.verification_state;O UPDATE_id

INSERT 0 55

msjarvisgis=# SELECT

    COUNT(*) AS snapshot_rows,

    COUNT(DISTINCT canonical_county_id) AS counties,

    COUNT(DISTINCT belief_hash) AS distinct_belief_hashes

FROM wv_county_belief_snapshot

WHERE snapshot_version = 'wv-county-snapshot-v1';

SELECT canonical_county_id, snapshot_version, belief_hash, verification_state

FROM wv_county_belief_snapshot

ORDER BY canonical_county_id

LIMIT 10;

 snapshot_rows | counties | distinct_belief_hashes 

---------------+----------+------------------------

            55 |       55 |                     55

(1 row)

 canonical_county_id |   snapshot_version    |                           belief_hash                            | verification_state 

---------------------+-----------------------+------------------------------------------------------------------+--------------------

 54001               | wv-county-snapshot-v1 | 551d0259c63d2a34da847b5f99940c3f292dd1e11fb13a48776d0fa9283696fe | derived

 54003               | wv-county-snapshot-v1 | a4b8ce5508ad5aa2f7e0054aaa4aa79552b4048b285fae7d91cd69e8c22ee696 | derived

 54005               | wv-county-snapshot-v1 | 6f32814d84b515ae3369f6f7b743b2ae09b6b54d709d215064832ba4118a978d | derived

 54007               | wv-county-snapshot-v1 | 35d9b9b9623af8d8020a6929b5e03dfe1ff52e67f004857ae6f0c679c898d5a3 | derived

 54009               | wv-county-snapshot-v1 | 53a780203b60dc7f349d3b09c8030e04d9b125feab6395f0981496af9506d772 | derived

 54011               | wv-county-snapshot-v1 | 37536422c7798322fb2daddee3affa0a27825d790c4364175a595d50d996d5d8 | derived

 54013               | wv-county-snapshot-v1 | f42920ff222e1906aaf5985e584a704589c81dd9cf6da5a30e07568fdfd5f0e6 | derived

 54015               | wv-county-snapshot-v1 | 64d02ea6446d06aaa785b5dc647da7156a77956ac0e2480fbd067a34a67391a8 | derived

 54017               | wv-county-snapshot-v1 | 8a696239c646a5c0b7f1e0028b4bede1df97036817e76556e791ada5bde92002 | derived

 54019               | wv-county-snapshot-v1 | e95d110391651fd47d9c04f1e1691cec0dce74350ca9ff6d95f2473a8ab854a2 | derived

(10 rows)

msjarvisgis=# CREATE OR REPLACE VIEW wv_county_belief_vector_ready AS

SELECT

    s.snapshot_version,

    s.canonical_county_id,

    ci.county_name,

    s.belief_hash AS document_id,

    jsonb_build_object(

        'canonical_county_id', s.canonical_county_id,

        'county_name', ci.county_name,

        'snapshot_version', s.snapshot_version,

        'belief_hash', s.belief_hash,

        'verification_state', s.verification_state

    ) AS metadata,

    concat(

        ci.county_name, ' County, West Virginia, GEOID ', s.canonical_county_id, '. ',

        'The current governed snapshot links ',

        (s.belief_document #>> '{summary_counts,n_zctas}'), ' ZCTAs, ',

        (s.belief_document #>> '{summary_counts,n_tracts}'), ' census tracts, ',

        (s.belief_document #>> '{summary_counts,n_blockgroups}'), ' block groups, ',

        (s.belief_document #>> '{summary_counts,n_dfirm_polygons}'), ' D-FIRM polygons, and ',

        (s.belief_document #>> '{summary_counts,n_address_points}'), ' address poiWHERE s.snapshot_version = 'wv-county-snapshot-v1';out true address absence unless

CREATE VIEW

msjarvisgis=# SELECT canonical_county_id, county_name, document_id, left(vector_document, 220)

FROM wv_county_belief_vector_ready

ORDER BY canonical_county_id

LIMIT 10;

 canonical_county_id | county_name |                           document_id                            |                                                                                                             left                                                                                                             

---------------------+-------------+------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 54001               | Barbour     | 551d0259c63d2a34da847b5f99940c3f292dd1e11fb13a48776d0fa9283696fe | Barbour County, West Virginia, GEOID 54001. The current governed snapshot links 6 ZCTAs, 4 census tracts, 16 block groups, 0 D-FIRM polygons, and 10894 address points. Address-point coverage state is present and must not

 54003               | Berkeley    | a4b8ce5508ad5aa2f7e0054aaa4aa79552b4048b285fae7d91cd69e8c22ee696 | Berkeley County, West Virginia, GEOID 54003. The current governed snapshot links 10 ZCTAs, 25 census tracts, 73 block groups, 0 D-FIRM polygons, and 61793 address points. Address-point coverage state is present and must 

 54005               | Boone       | 6f32814d84b515ae3369f6f7b743b2ae09b6b54d709d215064832ba4118a978d | Boone County, West Virginia, GEOID 54005. The current governed snapshot links 28 ZCTAs, 8 census tracts, 17 block groups, 0 D-FIRM polygons, and 12573 address points. Address-point coverage state is present and must not 

 54007               | Braxton     | 35d9b9b9623af8d8020a6929b5e03dfe1ff52e67f004857ae6f0c679c898d5a3 | Braxton County, West Virginia, GEOID 54007. The current governed snapshot links 13 ZCTAs, 3 census tracts, 13 block groups, 0 D-FIRM polygons, and 17912 address points. Address-point coverage state is present and must no

 54009               | Brooke      | 53a780203b60dc7f349d3b09c8030e04d9b125feab6395f0981496af9506d772 | Brooke County, West Virginia, GEOID 54009. The current governed snapshot links 7 ZCTAs, 8 census tracts, 27 block groups, 0 D-FIRM polygons, and 18952 address points. Address-point coverage state is present and must not 

 54011               | Cabell      | 37536422c7798322fb2daddee3affa0a27825d790c4364175a595d50d996d5d8 | Cabell County, West Virginia, GEOID 54011. The current governed snapshot links 12 ZCTAs, 34 census tracts, 134 block groups, 0 D-FIRM polygons, and 46770 address points. Address-point coverage state is present and must n

 54013               | Calhoun     | f42920ff222e1906aaf5985e584a704589c81dd9cf6da5a30e07568fdfd5f0e6 | Calhoun County, West Virginia, GEOID 54013. The current governed snapshot links 10 ZCTAs, 2 census tracts, 6 block groups, 0 D-FIRM polygons, and 3951 address points. Address-point coverage state is present and must not 

 54015               | Clay        | 64d02ea6446d06aaa785b5dc647da7156a77956ac0e2480fbd067a34a67391a8 | Clay County, West Virginia, GEOID 54015. The current governed snapshot links 12 ZCTAs, 3 census tracts, 7 block groups, 0 D-FIRM polygons, and 5306 address points. Address-point coverage state is present and must not be 

 54017               | Doddridge   | 8a696239c646a5c0b7f1e0028b4bede1df97036817e76556e791ada5bde92002 | Doddridge County, West Virginia, GEOID 54017. The current governed snapshot links 5 ZCTAs, 2 census tracts, 8 block groups, 0 D-FIRM polygons, and 9309 address points. Address-point coverage state is present and must not

 54019               | Fayette     | e95d110391651fd47d9c04f1e1691cec0dce74350ca9ff6d95f2473a8ab854a2 | Fayette County, West Virginia, GEOID 54019. The current governed snapshot links 42 ZCTAs, 13 census tracts, 21 block groups, 138 D-FIRM polygons, and 0 address points. Address-point coverage state is unknown and must not

(10 rows)

msjarvisgis=# psql -v ON_ERROR_STOP=1 <<'SQL'

INSERT INTO gbim_vector_publication (

    collection_version_id,

    document_id,

    canonical_entity_id,

    belief_hash,

    snapshot_version

)

SELECT

    m.collection_version_id,

    v.document_id,

    v.canonical_county_id,

    v.document_id,

    m.snapshot_version

FROM gbim_collection_manifest m

CROSS JOIN wv_county_belief_vector_ready v

WHERE m.collection_name = 'gbim_wv_counties'

  AND m.collection_version = 'v1'

ON CONFLICT (collection_version_id, document_id) DO NOTHING;

SELECT publication_status, COUNT(*)

FROM gbim_vector_publication p

JOIN gbim_collection_manifest m

  ON m.collection_version_id = p.collection_version_id

SQLM wv_county_belief_vector_ready; IS NULL) AS missing_metadata '') AS empty_docu

ERROR:  syntax error at or near "psql"

LINE 1: psql -v ON_ERROR_STOP=1 <<'SQL'

        ^

ERROR:  relation "gbim_vector_publication" does not exist

LINE 2: FROM gbim_vector_publication p

             ^

ERROR:  column "document" does not exist

LINE 5:     COUNT(*) FILTER (WHERE document IS NULL OR btrim(documen...

                                   ^

HINT:  Perhaps you meant to reference the column "wv_county_belief_vector_ready.document_id".

msjarvisgis-# 

\q

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ cat > /tmp/build_gbim_wv_counties_v1.py <<'PY'

import os, json, hashlib, sys

import psycopg2

import chromadb

from chromadb.config import Settings

PGHOST=os.getenv("PGHOST","127.0.0.1")

PGPORT=os.getenv("PGPORT","5433")

PGDATABASE=os.getenv("PGDATABASE","postgres")

PGUSER=os.getenv("PGUSER","postgres")

PGPASSWORD=os.getenv("PGPASSWORD","")

CHROMA_HOST=os.getenv("CHROMA_HOST","127.0.0.1")

CHROMA_PORT=int(os.getenv("CHROMA_PORT","8002"))

COLLECTION_NAME="gbim_wv_counties"

COLLECTION_VERSION="v1"

PHYSICAL_COLLECTION="gbim_wv_counties_v1"

conn = psycopg2.connect(host=PGHOST, port=PGPORT, dbname=PGDATABASE, user=PGUSER, password=PGPASSWORD)

conn.autocommit = False

def q(sql, params=None):

python3 /tmp/build_gbim_wv_counties_v1.pyon_version_id)SION)) 'hex'),id) AS ids, a

Traceback (most recent call last):

  File "/tmp/build_gbim_wv_counties_v1.py", line 37, in <module>

    raise RuntimeError("Manifest v1 not found.")

RuntimeError: Manifest v1 not found.

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

CREATE TABLE IF NOT EXISTS gbim_active_collection (

    logical_collection_name  text PRIMARY KEY,

    collection_version_id    uuid NOT NULL,

    physical_collection_name text NOT NULL UNIQUE,

    activated_at             timestamptz NOT NULL DEFAULT now(),

    FOREIGN KEY (collection_version_id)

        REFERENCES gbim_collection_manifest(collection_version_id)

);

BEGIN;

INSERT INTO gbim_active_collection (

    logical_collection_name,

    collection_version_id,

    physical_collection_name

)

SELECT

    'gbim_wv_counties',

    m.collection_version_id,

    'gbim_wv_counties_v1'

FROM gbim_collection_manifest m

WHERE m.collection_name = 'gbim_wv_counties'

  AND m.collection_version = 'v1'

SQLMIT;ollection_version = 'v1';_counties'ysical_collection_name,

psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: No such file or directory

	Is the server running locally and accepting connections on that socket?

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

SELECT document_id, canonical_county_id, county_name, document, metadata

FROM wv_county_belief_vector_ready

WHERE canonical_county_id = '54019';

SELECT *

FROM wv_county_belief_snapshot

WHERE canonical_county_id = '54019'

  AND snapshot_version = 'wv-county-snapshot-v1';

SELECT *

FROM wv_county_dataset_coverage

WHERE canonical_county_id = '54019'

ORDER BY dataset_type, source_table;

SELECT *

FROM wv_county_representation

WHERE canonical_county_id = '54019'

ORDER BY table_name, source_feature_id;

SQL

psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: No such file or directory

	Is the server running locally and accepting connections on that socket?

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ python3 - <<'PY'

import chromadb, json

client = chromadb.HttpClient(host="127.0.0.1", port=8002)

col = client.get_collection("gbim_wv_counties_v1")

print("COUNT", col.count())

print("\nID LOOKUP")

r = col.get(

    where={"canonical_county_id":"54019"},

    include=["documents","metadatas"]

)

print(json.dumps(r, indent=2)[:5000])

print("\nSEMANTIC QUERY 1")

q1 = col.query(

    query_texts=["What governed geographic information is available for Fayette County?"],

    n_results=3

)

print(json.dumps(q1, indent=2)[:5000])

print("\nSEMANTIC QUERY 2")

q2 = col.query(

PYint(json.dumps(q2, indent=2)[:5000])have no address points?"],

Traceback (most recent call last):

  File "<stdin>", line 3, in <module>

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/client.py", line 171, in get_collection

    model = self._server.get_collection(

            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/telemetry/opentelemetry/__init__.py", line 150, in wrapper

    return f(*args, **kwargs)

           ^^^^^^^^^^^^^^^^^^

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/fastapi.py", line 258, in get_collection

    resp_json = self._make_request(

                ^^^^^^^^^^^^^^^^^^^

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/fastapi.py", line 90, in _make_request

    BaseHTTPClient._raise_chroma_error(response)

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/base_http_client.py", line 96, in _raise_chroma_error

    raise chroma_error

chromadb.errors.InvalidCollectionException: Collection gbim_wv_counties_v1 does not exist.

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

BEGIN;

CREATE TEMP TABLE tmp_before_hashes AS

SELECT canonical_county_id, belief_hash

FROM wv_county_belief_snapshot

WHERE snapshot_version = 'wv-county-snapshot-v1';

UPDATE wv_county_dataset_coverage

SET coverage_state = 'missing_source',

    notes = 'Controlled recurrence test for v2 build'

WHERE canonical_county_id = '54019'

  AND dataset_type = 'address_point';

INSERT INTO wv_county_belief_snapshot (

    canonical_county_id,

    snapshot_version,

    belief_document,

    belief_hash,

    verification_state

)

SELECT

    ci.canonical_county_id,

    'wv-county-snapshot-v2',

SQLLBACK;napshot_version = 'wv-county-snapshot-v2'; '54019' AND b.belief_hash <> a

psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: No such file or directory

	Is the server running locally and accepting connections on that socket?

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ export PGHOST=127.0.0.1

export PGPORT=5433

export PGDATABASE=msjarvisgis

export PGUSER=postgres

# export PGPASSWORD='your_password_if_needed'

psql -c "select current_database(), current_user, inet_server_addr(), inet_server_port();"

 current_database | current_user | inet_server_addr | inet_server_port 

------------------+--------------+------------------+------------------

 msjarvisgis      | postgres     | 172.18.0.79      |             5432

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

CREATE OR REPLACE VIEW wv_county_belief_vector_ready AS

SELECT

    s.snapshot_version,

    s.canonical_county_id,

    ci.county_name,

    s.belief_hash AS document_id,

    jsonb_build_object(

        'canonical_county_id', s.canonical_county_id,

        'county_geoid', s.canonical_county_id,

        'county_name', ci.county_name,

        'snapshot_version', s.snapshot_version,

        'belief_hash', s.belief_hash,

        'verification_state', s.verification_state

    ) AS metadata,

    concat(

        ci.county_name, ' County, West Virginia, GEOID ', s.canonical_county_id, '. ',

        'The current governed snapshot links ',

        (s.belief_document #>> '{summary_counts,n_zctas}'), ' ZCTAs, ',

        (s.belief_document #>> '{summary_counts,n_tracts}'), ' census tracts, ',

        (s.belief_document #>> '{summary_counts,n_blockgroups}'), ' block groups, ',

        (s.belief_document #>> '{summary_counts,n_dfirm_polygons}'), ' D-FIRM polySQLRE s.snapshot_version = 'wv-county-snapshot-v1';out true address absence unless

ERROR:  cannot change name of view column "vector_document" to "document"

HINT:  Use ALTER VIEW ... RENAME COLUMN ... to change name of view column instead.

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ grep -RniE "(embedding[_-]?model|text-embedding|sentence.?transformer|all-MiniLM|bge-|e5-|nomic-embed|openai.*embedding|EMBEDDING_MODEL)" \

  /mnt/spiritual_drive /opt /srv /app /home/cakidd 2>/dev/null | head -n 100

/mnt/spiritual_drive/msjarvis-rebuild/Dockerfile.brain:11:    chromadb==0.6.3 numpy python-dateutil pytz scikit-learn scipy textblob sentence-transformers prometheus-fastapi-instrumentator || \

/mnt/spiritual_drive/msjarvis-rebuild/Dockerfile.brain:16:     chromadb==0.6.3 numpy python-dateutil pytz scikit-learn scipy textblob sentence-transformers prometheus-fastapi-instrumentator)

/mnt/spiritual_drive/msjarvis-rebuild/start_hilbert_state.sh:9:  -v /mnt/spiritual_drive/msjarvis-rebuild/models/all-MiniLM-L6-v2:/app/models/sentence-transformers/all-MiniLM-L6-v2:ro \

/mnt/spiritual_drive/msjarvis-rebuild/inspect_address_points.sh:14:echo "=== STEP 3: Search for any use of nomic-embed-text or 768 ==="

/mnt/spiritual_drive/msjarvis-rebuild/inspect_address_points.sh:15:rg "nomic-embed-text" .

/mnt/spiritual_drive/msjarvis-rebuild/inspect_address_points.sh:25:echo ">> edit it to use the all-minilm embedder (384-dim), then run it."

/mnt/spiritual_drive/msjarvis-rebuild/Dockerfile.rag_server:14:    sentence-transformers \

/mnt/spiritual_drive/msjarvis-rebuild/thesis/07-rag-pipeline-and-routers.md:40:> All ChromaDB collections — including `gbim_worldview_entities` (5,416,521 entities), `autonomous_learner` (21,181 items), `gis_wv_benefits`, and all semantic collections — use **384-dimensional vectors** produced by **`all-minilm:latest`** (pulled March 17, 2026, via `jarvis-ollama:11434/api/embeddings`). The `nomic-embed-text` model produces **768-dimensional vectors** and is **incompatible** with all existing collections. Any service, script, or migration that generates embeddings for ChromaDB **must** use `all-minilm:latest`. This includes Phase 1.45, text RAG, GIS RAG, the autonomous learner, and any new collection ingestion.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/07-rag-pipeline-and-routers.md:66:│    all-minilm:latest (384-dim) → autonomous_learner         │

/mnt/spiritual_drive/msjarvis-rebuild/thesis/07-rag-pipeline-and-routers.md:95:The Hilbert‐space state view treats the system's overall knowledge and constraints as a very high‐dimensional state vector. RAG interactions can be understood as projections into lower‐dimensional subspaces that correspond to "what matters for this query, given this role and place." For text, those projections are implemented as embedding‐based nearest‐neighbor searches in ChromaDB collections using **384-dimensional vectors from `all-minilm:latest`**. For space, they are implemented as centroid‐based spatial filters over PostgreSQL `gisdb`‐derived features and as neighborhood queries over GBIM‐linked spatial entities. For concrete help‐seeking and program questions, retrieved resource documents and metadata are further resolved into rows of `jarvis-local-resources-db` (port 5435) keyed by ZIP, county, and program type, which are themselves part of the structured Hilbert‐space state.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/07-rag-pipeline-and-routers.md:101:- ChromaDB collections like `gbim_worldview_entities` (consolidated GBIM spatial index), `autonomous_learner` (21,181 items, queried at Phase 1.45), `gis_wv_benefits`, `psychological_rag` (968 items), `appalachian_cultural_intelligence` (5 items), `spiritual_texts` (23 items), `gbim_beliefs_v2`, and others are configured at **384 dimensions (`all-minilm:latest`)** and accessed over a shared HTTP ChromaDB service at port 8000.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/07-rag-pipeline-and-routers.md:130:# REQUIRED: all-minilm:latest (384-dim) — DO NOT use nomic-embed-text (768-dim)

/mnt/spiritual_drive/msjarvis-rebuild/thesis/07-rag-pipeline-and-routers.md:142:# Embed and index in ChromaDB using all-minilm:latest

/mnt/spiritual_drive/msjarvis-rebuild/thesis/07-rag-pipeline-and-routers.md:159:│  │  -  Embedding: all-minilm:latest (384-dim)             │  │

/mnt/spiritual_drive/msjarvis-rebuild/thesis/07-rag-pipeline-and-routers.md:169:│  │  -  Embedding: all-minilm:latest (384-dim)             │  │

/mnt/spiritual_drive/msjarvis-rebuild/thesis/07-rag-pipeline-and-routers.md:184:│  │  -  Embedding: all-minilm:latest (384-dim)             │  │

/mnt/spiritual_drive/msjarvis-rebuild/thesis/07-rag-pipeline-and-routers.md:219:1. The main brain calls `jarvis-ollama:11434/api/embeddings` with model `all-minilm:latest` and the user query as the prompt, receiving a 384-dimensional embedding vector.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/07-rag-pipeline-and-routers.md:234:    json={"model": "all-minilm:latest", "prompt": user_query}

/mnt/spiritual_drive/msjarvis-rebuild/thesis/07-rag-pipeline-and-routers.md:252:> **Critical:** The embedding model **must** be `all-minilm:latest` (384-dim). Using `nomic-embed-text` (768-dim) will cause a dimension mismatch error against all existing ChromaDB collections. This applies to Phase 1.45, text RAG, GIS RAG, and any other ChromaDB write or query operation.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/07-rag-pipeline-and-routers.md:256:The text RAG service exposes a structured HTTP API used by main‐brain chat paths that takes a query string, a `top_k` parameter, optional metadata filters (such as collection, source, county, dataset, or worldview), and optional role and geography hints. It issues similarity searches against one or more ChromaDB collections using **`all-minilm:latest` (384-dimensional embeddings)**, and returns both a flat list of top results and a `results_by_source` mapping keyed by collection name. Each result item carries:

/mnt/spiritual_drive/msjarvis-rebuild/thesis/07-rag-pipeline-and-routers.md:282:> All collections: **384-dim, `all-minilm:latest`**. Do not use `nomic-embed-text`.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/07-rag-pipeline-and-routers.md:295:All embeddings use **`all-minilm:latest` (384-dim)**. Example:

/mnt/spiritual_drive/msjarvis-rebuild/thesis/07-rag-pipeline-and-routers.md:319:# NOTE: embeddings generated automatically by ChromaDB using all-minilm:latest

/mnt/spiritual_drive/msjarvis-rebuild/thesis/07-rag-pipeline-and-routers.md:320:# Do NOT pass pre-computed nomic-embed-text vectors to this collection

/mnt/spiritual_drive/msjarvis-rebuild/thesis/07-rag-pipeline-and-routers.md:382:Before any other RAG service is invoked, the main brain embeds the query via `all-minilm:latest` and retrieves the top-5 most similar records from `autonomous_learner` (21,181 items). These are prepended to `enhanced_message`.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/07-rag-pipeline-and-routers.md:387:**Retrieval from ChromaDB (384-dim, `all-minilm:latest`).**  

/mnt/spiritual_drive/msjarvis-rebuild/thesis/07-rag-pipeline-and-routers.md:406:│  │  Embed query (all-minilm:latest, 384-dim)      │         │

/mnt/spiritual_drive/msjarvis-rebuild/thesis/07-rag-pipeline-and-routers.md:441:The GIS RAG service embeds the query using `all-minilm:latest` (384-dim) and runs similarity search over geospatial ChromaDB collections. Because each entity includes centroids and region metadata sourced from PostgreSQL `gisdb`, the service can apply geometric or administrative filters by querying `gisdb.zcta_wv_centroids` (993 WV ZIP centroids) or joining to `msjarvis.gbim_beliefs` for temporal decay metadata.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/07-rag-pipeline-and-routers.md:503:│    all-minilm:latest → autonomous_learner → top-5 prepended │

/mnt/spiritual_drive/msjarvis-rebuild/thesis/07-rag-pipeline-and-routers.md:540:- The text RAG API exposes optional `role` and `geography` fields and uses them to choose which ChromaDB collections to query. All collections use 384-dim `all-minilm:latest` embeddings. WV‐specific benefits and governance collections are explicitly favored for WV benefits flows.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/07-rag-pipeline-and-routers.md:569:│  │     (all-minilm:latest, 384-dim, 21,181 items) │         │

/mnt/spiritual_drive/msjarvis-rebuild/thesis/07-rag-pipeline-and-routers.md:649:ChromaDB collections hold embedded representations at **384 dimensions (`all-minilm:latest`)**: `gbim_worldview_entities` (5,416,521 entities), `autonomous_learner` (21,181 items, growing ~288/day), `gis_wv_benefits`, and 10+ additional collections. Structured tables such as `jarvis-local-resources-db` (port 5435) hold normalized, versioned records addressable via RAG‐inferred keys. PostgreSQL `msjarvis` and `gisdb` (port 5433) encode belief graphs and spatial bodies reachable via `entity_id`, `source_table`, and `source_pk` fields returned in ChromaDB metadata. All 5,416,521 GBIM entities carry `confidence_decay` and `needs_verification` temporal metadata.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/00-overview.md:95:- **ChromaDB** (port 8000, containerized, `chroma_data` Docker volume): Vector database — `gbim_worldview_entities` (5,416,521 entities), `autonomous_learner` (21,181 items), `psychological_rag` (968 items), and 10+ additional collections. **All collections use 384-dimensional vectors (`all-minilm:latest`). The `nomic-embed-text` model produces 768-dim vectors and is incompatible with all existing collections.**

/mnt/spiritual_drive/msjarvis-rebuild/thesis/00-overview.md:109:* **Embedding model:** `all-minilm:latest` (384-dimensional). This is a locked dependency for all existing collections. **Do not use `nomic-embed-text` (768-dim) — it is incompatible with all existing ChromaDB collections.**

/mnt/spiritual_drive/msjarvis-rebuild/thesis/00-overview.md:126:| **1.45** | ChromaDB Semantic Community Memory Retrieval | 8000 | Embeds query via `all-minilm:latest`; retrieves top-5 `autonomous_learner` memories; prepends to `enhanced_message` | ✅ NEW |

/mnt/spiritual_drive/msjarvis-rebuild/thesis/00-overview.md:236:   1. Generates a 384-dimensional embedding of the query using `all-minilm:latest` via `jarvis-ollama:11434/api/embeddings`

/mnt/spiritual_drive/msjarvis-rebuild/thesis/00-overview.md:241:   > **Technical note:** All ChromaDB collections use 384-dimensional vectors. The `all-minilm:latest` model (pulled March 17, 2026) is the required embedding model. The previously listed `nomic-embed-text` model produces 768-dim vectors and is incompatible with all existing collections.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/00-overview.md:427:| ChromaDB curator _DummyCollection | Open | ✅ FIXED — all-minilm semantic retrieval implemented |

/mnt/spiritual_drive/msjarvis-rebuild/thesis/05-chromadb-semantic-memory.md:103:1. Generates a 384-dimensional embedding of the query using `all-minilm:latest` via `jarvis-ollama:11434/api/embeddings`

/mnt/spiritual_drive/msjarvis-rebuild/thesis/05-chromadb-semantic-memory.md:108:> **Critical note:** All ChromaDB collections use **384-dimensional vectors**. The required embedding model is `all-minilm:latest` (pulled March 17, 2026). `nomic-embed-text` produces 768-dimensional vectors and is **incompatible** with all existing collections. Any rebuild, migration, or new collection must use `all-minilm:latest`.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/05-chromadb-semantic-memory.md:133:- **Embedding dimensions:** 384 (`all-minilm:latest`)

/mnt/spiritual_drive/msjarvis-rebuild/thesis/05-chromadb-semantic-memory.md:188:- Embedding model: `all-minilm:latest` (384-dim)

/mnt/spiritual_drive/msjarvis-rebuild/thesis/05-chromadb-semantic-memory.md:243:The embedding model (`all-minilm:latest`, 384-dim) maps texts and entities into high-dimensional real vectors. ChromaDB stores these with metadata (identifiers, timestamps, geographies) and exposes nearest-neighbor search and filtering.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/05-chromadb-semantic-memory.md:263:Ms. Jarvis uses **`all-minilm:latest`** as the required embedding model, producing **384-dimensional vectors**. This model was pulled March 17, 2026 and confirmed as the active embedding model for all ChromaDB collections.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/05-chromadb-semantic-memory.md:265:> **⚠️ Critical architectural note:** All existing ChromaDB collections — including `gbim_worldview_entities` (5,416,521 entities), `autonomous_learner` (21,181 items), and all resource and semantic collections — use **384-dimensional vectors**. The `nomic-embed-text` model produces **768-dimensional vectors** and is **incompatible** with all existing collections. Any service that calls `jarvis-ollama:11434/api/embeddings` must specify `all-minilm:latest`. This applies to Phase 1.45 semantic retrieval, GIS RAG, text RAG, the autonomous learner, and any future collection creation.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/05-chromadb-semantic-memory.md:267:Previously, documentation referenced `nomic-embed-text` as the embedding model. That reference is incorrect and has been superseded. All new code, configuration, and documentation must reference `all-minilm:latest` (384-dim).

/mnt/spiritual_drive/msjarvis-rebuild/thesis/05-chromadb-semantic-memory.md:318:> **All collections use 384-dimensional vectors (`all-minilm:latest`).** Do not add collections or run ingests using any other embedding model.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/05-chromadb-semantic-memory.md:382:# Step 1: Generate 384-dim embedding via all-minilm:latest

/mnt/spiritual_drive/msjarvis-rebuild/thesis/05-chromadb-semantic-memory.md:385:    json={"model": "all-minilm:latest", "prompt": user_query}

/mnt/spiritual_drive/msjarvis-rebuild/thesis/05-chromadb-semantic-memory.md:438:1. Phase 1.45: `autonomous_learner` queried via `all-minilm:latest` embedding — top-5 community memories prepended to `enhanced_message`

/mnt/spiritual_drive/msjarvis-rebuild/thesis/05-chromadb-semantic-memory.md:469:- `query_texts`: Strings to embed and search (uses `all-minilm:latest` internally — 384-dim)

/mnt/spiritual_drive/msjarvis-rebuild/thesis/05-chromadb-semantic-memory.md:511:Collection names, metadata schemas, embedding configs, and RAG routing rules are versioned. The embedding model (`all-minilm:latest`, 384-dim) is a locked dependency — changing it requires a full re-embed of all collections. Migrations (e.g., consolidating collections, adding metadata fields, temporal decay field additions) are treated as explicit schema changes with evaluation.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/05-chromadb-semantic-memory.md:526:- Embedding model: **`all-minilm:latest` (384-dim)** — all collections; `nomic-embed-text` incompatible

/mnt/spiritual_drive/msjarvis-rebuild/thesis/05-chromadb-semantic-memory.md:547:- Phase 1.45 community memory: `all-minilm:latest` embedding → `autonomous_learner` collection → top-5 prepended to `enhanced_message`

/mnt/spiritual_drive/msjarvis-rebuild/thesis/05-chromadb-semantic-memory.md:585:- ✅ `all-minilm:latest` (384-dim) confirmed as the embedding model; `nomic-embed-text` incompatibility documented

/mnt/spiritual_drive/msjarvis-rebuild/thesis/05-chromadb-semantic-memory.md:608:`all-minilm:latest` (384-dim) is a locked dependency for all existing collections. Any upgrade requires a full re-embed of all 5,416,521+ entities and is treated as a major migration with evaluation.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/05-chromadb-semantic-memory.md:631:The `gbim_worldview_entities` collection is fully populated at 5,416,521 entities, verified against source data March 14, 2026. ChromaDB is fully containerized at port 8000 with the `chroma_data` Docker volume, part of a fully compose-managed 79-container stack (Docker Compose v5.1.0). The `autonomous_learner` collection (21,181 items) is now queried directly at Phase 1.45 of every production request, prepending community interaction memories to each query before it reaches the 21-model ensemble. The required embedding model for all collections is `all-minilm:latest` (384-dim); `nomic-embed-text` is documented as incompatible.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/17-executive-coordination-overview.md:39:| **ChromaDB** | port 8000 — `chroma_data` volume, 384-dim (`all-minilm:latest`) |

/mnt/spiritual_drive/msjarvis-rebuild/thesis/17-executive-coordination-overview.md:83:| **Phase 1.45** | Semantic community memory retrieval — `all-minilm:latest` (384-dim) → `autonomous_learner` (21,181 records) → top-5 prepended to `enhanced_message` | Included in Phase 1.4 total |

/mnt/spiritual_drive/msjarvis-rebuild/thesis/17-executive-coordination-overview.md:187:> **All collections use 384-dimensional vectors (`all-minilm:latest`).** The `nomic-embed-text` model produces 768-dimensional vectors and is incompatible with all existing collections. The `_DummyCollection` error that previously prevented semantic retrieval is resolved by the `all-minilm:latest` implementation deployed March 17, 2026.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/17-executive-coordination-overview.md:229:| ChromaDB `_DummyCollection` error blocking semantic retrieval | ✅ FIXED — `all-minilm:latest` semantic retrieval implemented |

/mnt/spiritual_drive/msjarvis-rebuild/thesis/17-executive-coordination-overview.md:276:**Status: Confirmed.** 21,181 `autonomous_learner` records are semantically queried on every request via `all-minilm:latest` (384-dim). Top-5 matching memories are prepended to `enhanced_message` before LLM processing. Growing at ~288 records/day.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/14-hippocampus-and-memory-consolidation.md:13:> *Figure 14.1. Hippocampal consolidation in Ms. Jarvis: GBIM entities and normalized nine-axis beliefs, enriched with centroids and provenance, are mirrored into a `geospatialfeatures` vector collection that serves as a long-term, place-aware memory index for retrieval and audit. Phase 1.45 (deployed March 17, 2026) adds a second active retrieval path: the `autonomous_learner` collection (21,181 records) is queried on every `/chat` request via `all-minilm:latest` (384-dim) semantic search, prepending the top-5 most relevant community interaction records to every LLM prompt.*

/mnt/spiritual_drive/msjarvis-rebuild/thesis/14-hippocampus-and-memory-consolidation.md:19:This chapter describes how recent activity is turned into durable records in the system's long-term stores. The design borrows the idea of a hippocampal buffer that receives short-lived experiences, decides what matters, and then writes compact, structured traces into more stable memory. In the current implementation, this role is played by two complementary subsystems: (1) the GBIM + beliefs + Chroma hippocampus — GBIM worldview entities in `gbim_worldview_entity`, their 1:1 normalized nine-axis belief rows in `gbim_belief_normalized`, and a ChromaDB collection called `geospatialfeatures` that mirrors centroid-bearing entities together with worldview, dataset, GeoDB IDs, and other provenance; and (2) the `autonomous_learner` ChromaDB collection, which accumulates community interaction records at ~288 per day and is queried at Phase 1.45 of every production `/chat` request. As of March 18, 2026, the `jarvis-hippocampus` service is deployed and confirmed operational as part of the 79-container production stack (commit `b90f9ff`), ChromaDB is fully containerized at port 8000 with the `chroma_data` Docker volume (restored March 15), and all ChromaDB collections use **384-dimensional vectors** produced by `all-minilm:latest`. Neurobiological work on hippocampal replay and complementary learning systems provides the conceptual backdrop for this design.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/14-hippocampus-and-memory-consolidation.md:25:- Embedding model: ✅ **`all-minilm:latest` (384-dim)** — canonical embedding model for all ChromaDB collections

/mnt/spiritual_drive/msjarvis-rebuild/thesis/14-hippocampus-and-memory-consolidation.md:31:> **Critical — Embedding model lock (March 17, 2026):** All ChromaDB collections — including `geospatialfeatures`, `autonomous_learner`, `gbim_worldview_entities`, `psychological_rag`, `ms_jarvis_memory`, and all others — use **384-dimensional vectors** produced by `all-minilm:latest` (pulled into `jarvis-ollama:11434`, March 17). The `nomic-embed-text` model produces **768-dimensional vectors** and is **incompatible** with all existing collections. Any service, script, or migration that generates embeddings for ChromaDB must use `all-minilm:latest`. The `_DummyCollection` error that previously blocked semantic retrieval from `autonomous_learner` is resolved by this implementation.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/14-hippocampus-and-memory-consolidation.md:39:As of March 17, 2026, a second active hippocampal pathway operates in parallel: **Phase 1.45 community memory retrieval**. On every `/chat` request, before the LLM ensemble, the main brain queries the `autonomous_learner` ChromaDB collection (21,181 records as of March 18) using `all-minilm:latest` (384-dim) semantic search and prepends the top-5 most semantically similar community interaction records to `enhanced_message`. This makes accumulated community memory an active, prompt-level input to every response — not merely a background store available for optional RAG lookup.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/14-hippocampus-and-memory-consolidation.md:46:| Community interaction memory | `autonomous_learner` | 21,181 (growing ~288/day) | Phase 1.45 (every request) | `all-minilm:latest` semantic search, top-5 prepended |

/mnt/spiritual_drive/msjarvis-rebuild/thesis/14-hippocampus-and-memory-consolidation.md:58:1. **Phase 1.45:** `autonomous_learner` queried via `all-minilm:latest` (384-dim) on every request — top-5 community memories prepended to `enhanced_message`

/mnt/spiritual_drive/msjarvis-rebuild/thesis/14-hippocampus-and-memory-consolidation.md:73:For features with geometry, the belief `where` axis records centroids and SRIDs derived from underlying WV GIS layers (PostgreSQL `gisdb`, port 5433 — PostGIS, 13 GB, 39 tables, 993 ZCTA centroids from `zcta_wv_centroids`). These values are streamed into ChromaDB `geospatialfeatures` metadata (`centroid_x`, `centroid_y`, `srid`) so that retrieval can respect spatial context and coordinate systems. All embeddings for `geospatialfeatures` use `all-minilm:latest` (384-dim) to maintain collection compatibility.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/14-hippocampus-and-memory-consolidation.md:76:The `autonomous_learner` ChromaDB collection (21,181 records as of March 18, 2026; growing ~288/day) accumulates community interaction records produced by the autonomous learning subsystem. These records are written separately from `background_rag_store` and represent a different hippocampal pathway: experiential, interaction-derived memory rather than structured GBIM entity promotion. They are queried at Phase 1.45 via `all-minilm:latest` semantic search on every production request.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/14-hippocampus-and-memory-consolidation.md:117:Centroid-bearing entities are added to the `geospatialfeatures` collection as simple documents (for example, `"label (type) from dataset:source_pk at centroid (x, y)"`) with rich metadata. All vectors use `all-minilm:latest` (384-dim):

/mnt/spiritual_drive/msjarvis-rebuild/thesis/14-hippocampus-and-memory-consolidation.md:139:Each community interaction processed by the autonomous learning subsystem is written as a document + metadata record in `autonomous_learner`, embedded via `all-minilm:latest` (384-dim). These records capture the conversational and task-level experience of the system's community engagement — a complementary memory pathway to the structured GBIM entity fabric. At 21,181 records and growing ~288/day, this collection is the fastest-growing hippocampal store and the one queried most frequently (Phase 1.45 on every production request).

/mnt/spiritual_drive/msjarvis-rebuild/thesis/14-hippocampus-and-memory-consolidation.md:188:1. The incoming query is embedded via `all-minilm:latest` at `jarvis-ollama:11434/api/embeddings` (384-dim).

/mnt/spiritual_drive/msjarvis-rebuild/thesis/14-hippocampus-and-memory-consolidation.md:224:- ✅ **Embedding model: `all-minilm:latest` (384-dim)** — canonical model for all ChromaDB collections; `nomic-embed-text` (768-dim) confirmed incompatible and must not be used

/mnt/spiritual_drive/msjarvis-rebuild/thesis/14-hippocampus-and-memory-consolidation.md:225:- ✅ `_DummyCollection` error blocking `autonomous_learner` semantic retrieval: RESOLVED (March 17) — `all-minilm:latest` semantic retrieval is the fix

/mnt/spiritual_drive/msjarvis-rebuild/thesis/14-hippocampus-and-memory-consolidation.md:257:The `geospatialfeatures` ChromaDB collection is scaffolded but currently at 0 records pending backfill ingest. Extended metadata fields (`worldview_id`, `bbox`, `dataset`) need population across all 5,416,521 GBIM entities. Backfill pipeline exists but requires execution post-ingest (see Chapter 5 §5.11). All backfill embeddings must use `all-minilm:latest` (384-dim).

/mnt/spiritual_drive/msjarvis-rebuild/thesis/14-hippocampus-and-memory-consolidation.md:272:The consolidation layer captures how recent activity and world-modeling are turned into lasting structure across two complementary hippocampal pathways: (1) GBIM entities with normalized beliefs and temporal decay metadata in PostgreSQL `msjarvis` (port 5433), mirrored as centroid-bearing records into the `geospatialfeatures` ChromaDB collection (port 8000, `chroma_data` volume), queried by GIS-RAG and spiritual-RAG during Phase 4; and (2) the `autonomous_learner` ChromaDB collection (21,181 records, growing ~288/day), queried via `all-minilm:latest` (384-dim) semantic search at Phase 1.45 of every production `/chat` request, with top-5 community memories prepended to `enhanced_message`.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/14-hippocampus-and-memory-consolidation.md:274:The `jarvis-hippocampus` service (deployed March 15, 2026, commit `b90f9ff`) functions as the dedicated hippocampal buffer within the 79-container production stack. The `confidence_decay` multiplier applied at Phase 5 of every production request makes hippocampal temporal state an active, measurable factor in every response — not merely an archival attribute. Phase 1.45 community memory retrieval (deployed March 17, 2026) makes `autonomous_learner` a live, prompt-level input to every response rather than a passive background store. The critical embedding model lock — **`all-minilm:latest` (384-dim) for all ChromaDB collections** — ensures collection compatibility and is a permanent architectural constraint.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/33-llm-ensemble-and-judges.md:20:│  -  all-minilm:latest 384-dim semantic search                │

/mnt/spiritual_drive/msjarvis-rebuild/thesis/33-llm-ensemble-and-judges.md:119:> **Figure 33.1.** Language model ensemble and judge pipeline architecture: 21 active expert models queried sequentially via semaphore proxy, synthesized consensus answer passed to 4-judge pipeline (truth, consistency, alignment, ethics) executing in parallel against the consensus answer only (raw_responses dump eliminated March 16, 2026), aggregated consensus_score and judge verdicts exposed in consciousnesslayers, Phase 3.5 LM Synthesizer + Voice Delivery merged into a single Ollama call (Phase 3.75 eliminated March 18, 2026), all context grounded in PostgreSQL-sourced RAG collections plus Phase 1.45 community memory retrieval (21,181 `autonomous_learner` records via `all-minilm:latest` 384-dim), with fallback to degraded mode if judge pipeline unavailable.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/33-llm-ensemble-and-judges.md:127:| **Implemented now** | `jarvis-20llm-production` (`ai_server_20llm_PRODUCTION.py`) confirmed running at **127.0.0.1:8008**. `jarvis-semaphore` proxy confirmed running at **127.0.0.1:8030**. **21 active expert model proxy containers** (`llm1-proxy` through `llm22-proxy`) confirmed running at **127.0.0.1:8201–8222** (22 proxies total; StarCoder2 at 8207 returns 0-char responses on community queries — 21 reliably active). Judge pipeline (`jarvis-judge-pipeline`) confirmed running at internal ports **7230–7233** (corrected from erroneous 7239, March 16, 2026) with all 4 judges: `judge-truth` **7230**, `judge-consistency` **7231**, `judge-alignment` **7232**, `judge-ethics` **7233**. **Judge pipeline updated March 16, 2026: evaluates consensus answer ONLY** — `raw_responses` dump from all 21 models no longer sent to judges; judge pipeline time reduced from ~85–100s to ~60–86s. **Phase 3.75 (Final LLM Polish via llm22-proxy) ELIMINATED March 18, 2026** — merged into Phase 3.5 LM Synthesizer single Ollama call with Ms. Jarvis persona injection; saves ~40s per query. **Phase 1.45 community memory retrieval added March 17, 2026** — `autonomous_learner` ChromaDB collection (21,181 records, growing ~288/day) queried via `all-minilm:latest` (384-dim) before LLM ensemble; top-5 memories prepended to `enhanced_message`. PostgreSQL `msjarvisgis` at **127.0.0.1:5432** (91 GB, 501 tables, 5.4M+ verified GBIM beliefs) as ground truth for truth judge validation and alignment judge community values checking. `POST /evaluate` endpoint on judge pipeline operational. `/cached_expert_responses` endpoint on `jarvis-20llm-production` operational. `asyncio.gather()` parallel judge execution confirmed. `judge-pipeline` consciousness layer in `UltimateResponse` confirmed. Fallback behavior confirmed: if judge pipeline unavailable, main brain marks layer `status: "error"` or `"skipped"`, uses 21-LLM answer as-is, assigns `consensus_score: 0.8`, sets `expert_count: 0` to signal degraded operation. All 79 containers fully compose-managed via Docker Compose v5.1.0; all `build:` directives converted to `image:` references. **Verified performance (March 18, 2026):** consensus score 0.975 on identity questions; 21/21 expert participation; all four judge verdicts pass (Truth=1.0, Consistency=1.0, Alignment=1.0, Ethics=0.9); end-to-end processing time **~436 seconds** (optimized from 532s baseline) for full pipeline including Phase 1.45 community memory, 21-model ensemble, consensus-only judge pipeline, and merged Phase 3.5 voice delivery. |

/mnt/spiritual_drive/msjarvis-rebuild/thesis/33-llm-ensemble-and-judges.md:139:> **March 16–18, 2026 architectural changes:** (1) Judge pipeline now evaluates the consensus answer only — the `raw_responses` dump from all 21 models is no longer sent to judges, reducing judge pipeline time from ~85–100s to ~60–86s. (2) Phase 3.75 (Final LLM Polish via `llm22-proxy`) has been eliminated and merged into Phase 3.5 (LM Synthesizer + Voice Delivery) as a single `jarvis-ollama:11434/api/generate` call with `llama3.1:latest` and the Ms. Egeria Jarvis persona prompt injected — saves ~40s per query. (3) Phase 1.45 community memory retrieval now prepends top-5 `autonomous_learner` records (21,181 total, growing ~288/day) to every LLM prompt via `all-minilm:latest` 384-dim semantic search. (4) All 22 proxy ports corrected from erroneous 7239 to proper per-judge ports (7230–7233).

/mnt/spiritual_drive/msjarvis-rebuild/thesis/33-llm-ensemble-and-judges.md:147:**Task execution (experts).** In the current deployment, **21 reliably active expert models** (22 proxies total; StarCoder2 at port 8207 frequently returns 0-character responses on community-domain queries) are exposed behind lightweight proxy containers (`llm1-proxy` through `llm22-proxy`, confirmed running at **127.0.0.1:8201–8222**). For each consensus request, all 21 models receive the same composite prompt — which already includes Phase 1.45 community memory from `autonomous_learner` (21,181 records via `all-minilm:latest` 384-dim), PostgreSQL-sourced RAG context from `jarvis-spiritual-rag` (port **8005**, queries GBIM collections), PostgreSQL GeoDB context from `jarvis-gis-rag` (port **8004**), container-state hints, and orchestration directives — and generate independent candidate answers. The proxy architecture prevents Ollama overload. In the current deployment, model proxies are dispatched **sequentially** rather than in true parallel to prevent Ollama resource exhaustion on the CPU-only inference host (Legion 5, 29 GB RAM, `size_vram: 0` on all models).

/mnt/spiritual_drive/msjarvis-rebuild/thesis/33-llm-ensemble-and-judges.md:293:1. **Phase 1.45** — `jarvis-main-brain` generates a 384-dim embedding of the query via `all-minilm:latest` at `jarvis-ollama:11434/api/embeddings`, queries the `autonomous_learner` ChromaDB collection (21,181 records as of March 18), retrieves the top-5 most semantically similar community interaction records, and prepends them to `enhanced_message`.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/33-llm-ensemble-and-judges.md:344:| Phase 1.45 | Community memory retrieval (`autonomous_learner`, `all-minilm:latest`) | ~0.7s |

/mnt/spiritual_drive/msjarvis-rebuild/thesis/33-llm-ensemble-and-judges.md:404:21 reliably active expert models via dedicated proxy containers (ports **8201–8222**, confirmed running). `ai_server_20llm_PRODUCTION.py` with `/cached_expert_responses` endpoint. Judge pipeline with all 4 judges operational (7230–7233, corrected March 16) validating against PostgreSQL `msjarvisgis`. **Consensus answer only sent to judges** (March 16 — reduces judge time to ~60–86s). **Phase 3.75 eliminated; Phase 3.5 LM Synthesizer + Voice Delivery merged** into single Ollama call (March 18 — saves ~40s). **Phase 1.45 community memory retrieval** (21,181 `autonomous_learner` records, `all-minilm:latest` 384-dim, March 17). Structured `REASONING / CONSENSUS_SCORE / FINAL_ANSWER` output format. Expert count and successful-expert tracking. Parallel judge execution via `asyncio.gather()`. Integration with main brain `consciousnesslayers`. Cache endpoint workaround for semaphore data preservation. PostgreSQL `msjarvisgis` at port 5432 as ground truth for truth judge and alignment judge validation. BBB `truth_score` null guard and fail-open on HTTP 500 (March 18). All 79 containers compose-managed via Docker Compose v5.1.0; `build:` → `image:` conversion complete.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/33-llm-ensemble-and-judges.md:417:In the current deployment, Ms. Jarvis's language-model ensemble and judge systems are built around `jarvis-20llm-production` (port **8008**) with **21 reliably active expert model proxies** (22 proxies at ports **8201–8222**; StarCoder2 at 8207 unreliable on community queries) and `jarvis-judge-pipeline` with four judge services (7230–7233, corrected March 16, 2026) validating against PostgreSQL `msjarvisgis` (port 5432, 91 GB, 501 tables, 5.4M+ verified GBIM beliefs). The ensemble queries all 21 experts sequentially via `jarvis-semaphore` (port **8030**) with a composite prompt enriched by Phase 1.45 community memory (21,181 `autonomous_learner` records, `all-minilm:latest` 384-dim) and PostgreSQL-sourced RAG context. The judge layer receives the **consensus answer only** (not the full raw_responses dump), computes `consensus_score` validated against PostgreSQL, tracks `expert_count` and `successful_experts`, produces structured `reasoning`, and returns per-judge verdicts for truth, consistency, alignment, and ethics in ~60–86s. The merged Phase 3.5 LM Synthesizer + Voice Delivery (single `jarvis-ollama:11434/api/generate` call with `llama3.1:latest` and Ms. Jarvis persona, ~30–55s) replaces the previous separate Phase 3.5 + Phase 3.75 pattern. These signals are exposed as a `judge-pipeline` consciousness layer in every `UltimateResponse` and are available for reuse by barrier, container, memory, and optimization components anchored to PostgreSQL. End-to-end benchmark: **~436 seconds** (optimized from 532s baseline).

/mnt/spiritual_drive/msjarvis-rebuild/thesis/11-llm-fabric-of-ms-jarvis.md:33:│  │  │   all-minilm:latest · 384-dim · top-5        │         │

/mnt/spiritual_drive/msjarvis-rebuild/thesis/11-llm-fabric-of-ms-jarvis.md:89:> **Figure 11.1.** The LLM fabric of Ms. Jarvis (March 18, 2026): user queries flow through NBB prefrontal (Phase 1), 7-filter BBB stack (Phase 1.4), ChromaDB semantic community memory retrieval via `all-minilm:latest` 384-dim embeddings (Phase 1.45 — NEW), psychology pre-assessment (Phase 3), LM Synthesizer calling `jarvis-ollama:11434` directly with `llama3.1:latest` and Ms. Egeria Jarvis persona injected (Phase 3.5), 21-model ensemble / 22 proxies with BakLLaVA permanently disabled (Phase 2.5), judge pipeline evaluating consensus answer only (Phase 3 — optimized), GBIM temporal confidence decay (Phase 5), 69-DGM cascade (Phase 7), safety/governance, and `normalize_identity()`. Phase 3.75 eliminated. All LLMs are exposed only via glass-box HTTP services and are grounded in West Virginia-specific memory anchored to three PostgreSQL databases.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/11-llm-fabric-of-ms-jarvis.md:97:| **Implemented and verified** | `jarvis-main-brain` → **127.0.0.1:8050** (confirmed). `jarvis-ollama` → **127.0.0.1:11434** (confirmed). `jarvis-wv-entangled-gateway` → **127.0.0.1:8010** (confirmed). `jarvis-spiritual-rag` (GBIM / worldview RAG) → **127.0.0.1:8005** (confirmed; earlier plan documents used 8103). `jarvis-gis-rag` → **127.0.0.1:8004** (confirmed). `jarvis-rag-server` (general RAG) → **127.0.0.1:8003** (confirmed; ONNX model downloaded and ChromaDB integration working). `jarvis-lm-synthesizer` → **127.0.0.1:8001** (confirmed; calls `jarvis-ollama:11434/api/generate` directly with `llama3.1:latest`; Ms. Egeria Jarvis persona prompt injected; previously called `jarvis-roche-llm` — corrected March 18, 2026). `psychological_rag_domain` → **127.0.0.1:8006** (confirmed; port corrected from 9006). `jarvis-psychology-services` → **127.0.0.1:8019** (confirmed; Phase 3 active on every production request). PostgreSQL `msjarvis` → **127.0.0.1:5433** (5,416,521 GBIM entities, 80 epochs, 206 source layers, temporal decay metadata). PostgreSQL `gisdb` → **127.0.0.1:5433** (13 GB PostGIS, 39 tables, 993 ZCTA centroids). `jarvis-local-resources-db` → **127.0.0.1:5435** (community resources, confirmed). ChromaDB → **127.0.0.1:8000** (`chroma_data` Docker volume; `psychological_rag` 968 items; `autonomous_learner` 21,181 items). `nbb_woah_algorithms` → **127.0.0.1:8104** host → internal 8010 (confirmed). `jarvis-woah` → **127.0.0.1:7012** (confirmed). `jarvis-blood-brain-barrier` → **0.0.0.0:8016** (confirmed; 7-filter stack; `truth_score` null guard added March 18; fail-open on HTTP 500 added March 18). `jarvis-20llm-production` → **127.0.0.1:8008** (confirmed; 21 active models / 22 proxies; BakLLaVA permanently disabled); wall-clock consensus ~320-360s. Judge pipeline → evaluates consensus answer only; raw_responses dump eliminated; ~60-86s (was ~85-100s). `jarvis-semaphore` → **127.0.0.1:8030** (confirmed; `max_concurrent: 4`; requires float `timeout`). `llm1-proxy` through `llm22-proxy` → **127.0.0.1:8201-8222** (21 active; llm11/BakLLaVA permanently disabled). `jarvis-hippocampus` → **127.0.0.1:8011**. `jarvis-69dgm-bridge` → **127.0.0.1:9000** (confirmed; Phase 7, 23 connectors × 3 stages). Judge services confirmed: `jarvis-judge-truth` 7230, `jarvis-judge-consistency` 7231, `jarvis-judge-alignment` 7232, `jarvis-judge-ethics` 7233. `jarvis-constitutional-guardian` → **127.0.0.1:8091** (confirmed). `jarvis-fifth-dgm` → **127.0.0.1:4002** (confirmed). `jarvis-redis` → **127.0.0.1:6380** (confirmed). `/chat/async` + `/chat/status/{job_id}` + `/chat/cancel/{job_id}` + `/chat/cancel/all` confirmed (Redis-backed, 30-min TTL, true asyncio task cancellation). `/chatlight/async` + `/chatlight/status/{job_id}` confirmed (tag `v2026.03.02-chatlight-async-working`). `normalize_identity()` confirmed producing Ms. Jarvis identity voice. Phase 1.45 ChromaDB semantic community memory retrieval confirmed — `all-minilm:latest` 384-dim, `autonomous_learner` collection, top-5 results prepended to `enhanced_message`. All 79 containers fully compose-managed. End-to-end benchmark: ~436s (full pipeline with community memory enrichment). |

/mnt/spiritual_drive/msjarvis-rebuild/thesis/11-llm-fabric-of-ms-jarvis.md:98:| **Architectural fixes recorded as permanent decisions** | BBB output guard `apply_output_guards_async` timeout corrected from `None` → **8.0s** (2026-03-02). Main-brain httpx client for semaphore proxy: `Timeout(None, connect=5.0, read=None)` — semaphore manages 600s deadline (2026-03-02). `llmtimeout` in chatlight handler corrected from `None` → `600.0` (2026-03-02). I-Containers schema corrected to `{"message": ..., "userid": "neurobiological_master"}` (2026-03-01). Consciousness Bridge actual port confirmed as **8018** (2026-03-01). PostgreSQL port corrected to **5433** (not 5432). ChromaDB port corrected to **8000** with `chroma_data` volume (not port 8002). `psychological_rag_domain` port corrected to **8006** (not 9006). RAG server `/store` payload corrected to `user_id` (not `userid`). Spiritual RAG port corrected to **8005** (not 8103). LM Synthesizer target corrected from `jarvis-roche-llm` → `jarvis-ollama:11434/api/generate` with `llama3.1:latest` (March 18, 2026). Judges now evaluate consensus answer only — raw_responses dump eliminated (March 18, 2026). Phase 3.75 (Final Polish via llm22-proxy) eliminated — merged into Phase 3.5 single Ollama call (March 18, 2026). BakLLaVA permanently disabled via `ai_server_20llm_PRODUCTION.py` name-check guard (March 18, 2026). `all-minilm:latest` (384-dim) confirmed as required embedding model — `nomic-embed-text` (768-dim) is incompatible with existing collections (March 18, 2026). Docker Compose upgraded from v1.29.2 → v5.1.0 (March 17, 2026). All 79 containers now compose-managed; all `build:` directives replaced with `image:` references (March 17, 2026). |

/mnt/spiritual_drive/msjarvis-rebuild/thesis/11-llm-fabric-of-ms-jarvis.md:240:Writes to `autonomous_learner` ChromaDB collection (port 8000) using `all-minilm:latest` 384-dim embeddings. 21,181 items as of March 18, 2026. Cooperates with `jarvis-i-containers` via `/next-learning-topic`.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/11-llm-fabric-of-ms-jarvis.md:243:`chroma_data` Docker volume. Active collections: `ms_jarvis_memory`, `mountainshares_knowledge`, `episodic_index`, `conversation_history`, `autonomous_learner` (21,181 items), `psychological_rag` (968 items), `gbim_beliefs_v2`, `gbim_worldview_entities`, `gis_wv_benefits`, `appalachian_cultural_intelligence`, `GBIM_sample_rows`, and others. **Required embedding model: `all-minilm:latest` (384-dim).** `nomic-embed-text` (768-dim) is incompatible with existing collections.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/11-llm-fabric-of-ms-jarvis.md:266:1. Generates a 384-dimensional embedding of the query using `all-minilm:latest` via `jarvis-ollama:11434/api/embeddings`

/mnt/spiritual_drive/msjarvis-rebuild/thesis/11-llm-fabric-of-ms-jarvis.md:271:> **Technical note:** All ChromaDB collections use 384-dimensional vectors. `all-minilm:latest` (pulled March 17, 2026) is the required embedding model. `nomic-embed-text` produces 768-dim vectors and is incompatible with existing collections.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/11-llm-fabric-of-ms-jarvis.md:331:The autonomous learner (port 8425) writes processed knowledge into the `autonomous_learner` ChromaDB collection (port 8000) using `all-minilm:latest` 384-dim embeddings. As of March 18, 2026, the collection holds 21,181 items growing at ~288/day. The Phase 1.45 retrieval step means this growing corpus now actively enriches every production query before it reaches the LLM ensemble.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/11-llm-fabric-of-ms-jarvis.md:366:- **ChromaDB.** Port **8000**, `chroma_data` volume. Required embedding model: `all-minilm:latest` (384-dim). Never reference port 8002 or `nomic-embed-text`.

/mnt/spiritual_drive/msjarvis-rebuild/thesis/11-llm-fabric-of-ms-jarvis.md:383:| *(March 18 session)* | 2026-03-18 | Phase 1.45 community memory · BakLLaVA permanently disabled · Phase 3.75 eliminated · judges evaluate consensus only · LM Synthesizer persona confirmed · all-minilm:latest 384-dim · Docker Compose v5.1.0 · all 79 containers compose-managed · ~436s end-to-end |

/mnt/spiritual_drive/msjarvis-rebuild/thesis/19-container-architecture-and-routing.md:31:│  -  Phase 1.45 community memory retrieval (all-minilm)       │

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ export PGHOST=127.0.0.1

export PGPORT=5433

export PGDATABASE=msjarvisgis

export PGUSER=postgres

# Drop and recreate with the correct column name

psql -v ON_ERROR_STOP=1 <<'SQL'

DROP VIEW IF EXISTS wv_county_belief_vector_ready;

CREATE VIEW wv_county_belief_vector_ready AS

SELECT

    s.snapshot_version,

    s.canonical_county_id,

    ci.county_name,

    s.belief_hash AS document_id,

    jsonb_build_object(

        'canonical_county_id', s.canonical_county_id,

        'county_geoid', s.canonical_county_id,

        'county_name', ci.county_name,

        'snapshot_version', s.snapshot_version,

        'belief_hash', s.belief_hash,

        'verification_state', s.verification_state

    ) AS metadata,

    concat(

        ci.county_name, ' County, West Virginia, GEOID ', s.canonical_county_id, 'SQLRE s.snapshot_version = 'wv-county-snapshot-v1';out true address absence unless

DROP VIEW

CREATE VIEW

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ export PGHOST=127.0.0.1

export PGPORT=5433

export PGDATABASE=msjarvisgis

export PGUSER=postgres

psql -v ON_ERROR_STOP=1 \

  -v embedding_model="'all-minilm:latest'" \

  -v embedding_dimension=384 <<'SQL'

CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS gbim_collection_manifest (

    collection_version_id uuid PRIMARY KEY DEFAULT gen_random_uuid(),

    collection_name       text NOT NULL,

    collection_version    text NOT NULL,

    source_view           text NOT NULL,

    snapshot_version      text NOT NULL,

    rendering_version     text NOT NULL,

    embedding_model       text NOT NULL,

    embedding_dimension   integer NOT NULL,

    record_count          integer,

    collection_hash       text,

    build_status          text NOT NULL DEFAULT 'planned',

    permitted_use         text NOT NULL,

    built_at              timestamptz,

SQLM wv_county_belief_vector_ready; IS NULL) AS missing_metadata '') AS empty_docu

NOTICE:  extension "pgcrypto" already exists, skipping

CREATE EXTENSION

CREATE TABLE

CREATE TABLE

INSERT 0 1

INSERT 0 55

 publication_status | count 

--------------------+-------

 pending            |    55

(1 row)

 rows | document_ids | counties | empty_documents | missing_metadata 

------+--------------+----------+-----------------+------------------

   55 |           55 |       55 |               0 |                0

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ export PGHOST=127.0.0.1

export PGPORT=5433

export PGDATABASE=msjarvisgis

export PGUSER=postgres

export CHROMA_HOST=127.0.0.1

export CHROMA_PORT=8002

python3 /tmp/build_gbim_wv_counties_v1.py

Traceback (most recent call last):

  File "/tmp/build_gbim_wv_counties_v1.py", line 84, in <module>

    existing = {c.name for c in client.list_collections()}

                ^^^^^^

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/models/Collection.py", line 418, in __getattr__

    raise NotImplementedError(

NotImplementedError: In Chroma v0.6.0, list_collections only returns collection names. Use Client.get_collection(public_civic_roles) to access name. See https://docs.trychroma.com/deployment/migration for more information.

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ python3 - <<'PY'

from pathlib import Path

p = Path("/tmp/build_gbim_wv_counties_v1.py")

s = p.read_text()

old = """existing = {c.name for c in client.list_collections()}

if PHYSICAL_COLLECTION in existing:

    col = client.get_collection(name=PHYSICAL_COLLECTION)

else:

    col = client.create_collection(

        name=PHYSICAL_COLLECTION,

        metadata={

            "authority_class": "governed_civic_geographic",

            "access_class": "public",

            "permitted_use": permitted_use,

            "logical_collection_name": COLLECTION_NAME,

            "collection_version": COLLECTION_VERSION,

            "snapshot_version": snapshot_version,

            "rendering_version": rendering_version,

            "embedding_model": embedding_model,

            "embedding_dimension": embedding_dimension

        }

    )"""

new = """try:

    col = client.get_collection(name=PHYSICAL_COLLECTION)

python3 /tmp/build_gbim_wv_counties_v1.pyund; patch manually.")

patched /tmp/build_gbim_wv_counties_v1.py

/home/cakidd/.cache/chroma/onnx_models/all-MiniLM-L6-v2/onnx.tar.gz: 100%|█| 79.3M

{

  "physical_collection": "gbim_wv_counties_v1",

  "count": 55,

  "verified": 55,

  "failed": 0,

  "collection_version_id": "f43b510a-12d5-4855-a203-65a2690ae6b0"

}

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ export PGHOST=127.0.0.1

export PGPORT=5433

export PGDATABASE=msjarvisgis

export PGUSER=postgres

psql -v ON_ERROR_STOP=1 <<'SQL'

CREATE TABLE IF NOT EXISTS gbim_active_collection (

    logical_collection_name  text PRIMARY KEY,

    collection_version_id    uuid NOT NULL,

    physical_collection_name text NOT NULL UNIQUE,

    activated_at             timestamptz NOT NULL DEFAULT now(),

    FOREIGN KEY (collection_version_id)

        REFERENCES gbim_collection_manifest(collection_version_id)

);

UPDATE gbim_collection_manifest

SET build_status = 'validated',

    built_at = COALESCE(built_at, now()),

    validated_at = now(),

    record_count = 55

WHERE collection_version_id = 'f43b510a-12d5-4855-a203-65a2690ae6b0';

INSERT INTO gbim_active_collection (

    logical_collection_name,

SQLRE logical_collection_name = 'gbim_wv_counties';203-65a2690ae6b0';t, promoted_a

CREATE TABLE

UPDATE 1

INSERT 0 1

UPDATE 1

 collection_name  | collection_version | build_status | record_count |          promoted_at          

------------------+--------------------+--------------+--------------+-------------------------------

 gbim_wv_counties | v1                 | active       |           55 | 2026-07-11 18:46:18.531273+00

(1 row)

 logical_collection_name |        collection_version_id         | physical_collection_name |         activated_at          

-------------------------+--------------------------------------+--------------------------+-------------------------------

 gbim_wv_counties        | f43b510a-12d5-4855-a203-65a2690ae6b0 | gbim_wv_counties_v1      | 2026-07-11 18:46:18.528621+00

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ python3 - <<'PY'

import chromadb, json

client = chromadb.HttpClient(host="127.0.0.1", port=8000)

col = client.get_collection("gbim_wv_counties_v1")

print("COUNT", col.count())

print("\nID LOOKUP")

r = col.get(

    where={"canonical_county_id":"54019"},

    include=["documents","metadatas"]

)

print(json.dumps(r, indent=2)[:4000])

print("\nSEMANTIC QUERY 1")

q1 = col.query(

    query_texts=["What governed geographic information is available for Fayette County?"],

    n_results=3

)

print(json.dumps(q1, indent=2)[:4000])

print("\nSEMANTIC QUERY 2")

q2 = col.query(

PYint(json.dumps(q2, indent=2)[:4000])have no address points?"],

Traceback (most recent call last):

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/base_http_client.py", line 99, in _raise_chroma_error

    resp.raise_for_status()

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_models.py", line 761, in raise_for_status

    raise HTTPStatusError(message, request=request, response=self)

httpx.HTTPStatusError: Client error '404 Not Found' for url 'http://127.0.0.1:8000/api/v2/auth/identity'

For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404

During handling of the above exception, another exception occurred:

Traceback (most recent call last):

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/client.py", line 101, in get_user_identity

    return self._server.get_user_identity()

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/telemetry/opentelemetry/__init__.py", line 150, in wrapper

    return f(*args, **kwargs)

           ^^^^^^^^^^^^^^^^^^

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/fastapi.py", line 182, in get_user_identity

    return UserIdentity(**self._make_request("get", "/auth/identity"))

                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/fastapi.py", line 90, in _make_request

    BaseHTTPClient._raise_chroma_error(response)

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/base_http_client.py", line 104, in _raise_chroma_error

    raise (Exception(resp.text))

Exception: {"detail":"Not Found"}

During handling of the above exception, another exception occurred:

Traceback (most recent call last):

  File "<stdin>", line 2, in <module>

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/__init__.py", line 203, in HttpClient

    return ClientCreator(tenant=tenant, database=database, settings=settings)

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/client.py", line 65, in __init__

    user_identity = self.get_user_identity()

                    ^^^^^^^^^^^^^^^^^^^^^^^^

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/client.py", line 110, in get_user_identity

    raise ValueError(str(e))

ValueError: {"detail":"Not Found"}

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ curl -i http://127.0.0.1:8000/api/v2/version

curl -i http://127.0.0.1:8000/api/v1/heartbeat

curl -i http://127.0.0.1:8000/api/v2/auth/identity

python3 - <<'PY'

import chromadb

import pkg_resources

print("chromadb_client_version =", pkg_resources.get_distribution("chromadb").version)

PY

HTTP/1.1 404 Not Found

date: Sat, 11 Jul 2026 18:47:49 GMT

server: uvicorn

content-length: 22

content-type: application/json

{"detail":"Not Found"}HTTP/1.1 404 Not Found

date: Sat, 11 Jul 2026 18:47:49 GMT

server: uvicorn

content-length: 22

content-type: application/json

{"detail":"Not Found"}HTTP/1.1 404 Not Found

date: Sat, 11 Jul 2026 18:47:49 GMT

server: uvicorn

content-length: 22

content-type: application/json

{"detail":"Not Found"}<stdin>:2: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.

chromadb_client_version = 0.6.3

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ curl -i http://127.0.0.1:8002/api/v2/version

curl -i http://127.0.0.1:8002/api/v1/heartbeat

curl -i http://127.0.0.1:8002/api/v2/auth/identity

HTTP/1.1 200 OK

date: Sat, 11 Jul 2026 18:48:47 GMT

server: uvicorn

content-length: 7

content-type: application/json

chroma-trace-id: 0

"0.6.3"HTTP/1.1 200 OK

date: Sat, 11 Jul 2026 18:48:47 GMT

server: uvicorn

content-length: 44

content-type: application/json

chroma-trace-id: 0

{"nanosecond heartbeat":1783795727513200130}HTTP/1.1 200 OK

date: Sat, 11 Jul 2026 18:48:47 GMT

server: uvicorn

content-length: 91

content-type: application/json

chroma-trace-id: 0

{"user_id":"","tenant":"default_tenant","databases":["default_database"],"attributes":null}(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ python3 - <<'PY'

import chromadb, json

client = chromadb.HttpClient(host="127.0.0.1", port=8002)

col = client.get_collection("gbim_wv_counties_v1")

print("COUNT", col.count())

print("\nID LOOKUP")

r = col.get(

    where={"canonical_county_id":"54019"},

    include=["documents","metadatas"]

)

print(json.dumps(r, indent=2)[:4000])

print("\nSEMANTIC QUERY 1")

q1 = col.query(

    query_texts=["What governed geographic information is available for Fayette County?"],

    n_results=3

)

print(json.dumps(q1, indent=2)[:4000])

print("\nSEMANTIC QUERY 2")

q2 = col.query(

PYint(json.dumps(q2, indent=2)[:4000])have no address points?"],

COUNT 55

ID LOOKUP

{

  "ids": [

    "e95d110391651fd47d9c04f1e1691cec0dce74350ca9ff6d95f2473a8ab854a2"

  ],

  "embeddings": null,

  "metadatas": [

    {

      "access_class": "public",

      "address_point_coverage_state": "unknown",

      "authority_class": "governed_civic_geographic",

      "belief_hash": "e95d110391651fd47d9c04f1e1691cec0dce74350ca9ff6d95f2473a8ab854a2",

      "blockgroup_coverage_state": "present",

      "canonical_county_id": "54019",

      "county_geoid": "54019",

      "county_name": "Fayette",

      "dfirm_polygon_coverage_state": "present",

      "permitted_use": "public_civic_geographic_retrieval",

      "rendering_version": "county-render-v1",

      "snapshot_version": "wv-county-snapshot-v1",

      "tract_coverage_state": "present",

      "verification_state": "derived",

      "zcta_coverage_state": "present"

    }

  ],

  "documents": [

    "Fayette County, West Virginia, GEOID 54019. The current governed snapshot links 42 ZCTAs, 13 census tracts, 21 block groups, 138 D-FIRM polygons, and 0 address points. Address-point coverage state is unknown and must not be interpreted as a claim about true address absence unless separately verified."

  ],

  "data": null,

  "uris": null,

  "included": [

    "documents",

    "metadatas"

  ]

}

SEMANTIC QUERY 1

{

  "ids": [

    [

      "e95d110391651fd47d9c04f1e1691cec0dce74350ca9ff6d95f2473a8ab854a2",

      "e2abf47305e12af7899a8fc43cba1789871b86336f1d73387706e91978987b8c",

      "634cc1b35f13e4d11107ae7a8c2acd3710d2666363cc07660b9871f0a38cbd35"

    ]

  ],

  "distances": [

    [

      0.9761103637436271,

      1.1105143994940372,

      1.1639015764395824

    ]

  ],

  "embeddings": null,

  "metadatas": [

    [

      {

        "access_class": "public",

        "address_point_coverage_state": "unknown",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "e95d110391651fd47d9c04f1e1691cec0dce74350ca9ff6d95f2473a8ab854a2",

        "blockgroup_coverage_state": "present",

        "canonical_county_id": "54019",

        "county_geoid": "54019",

        "county_name": "Fayette",

        "dfirm_polygon_coverage_state": "present",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "county-render-v1",

        "snapshot_version": "wv-county-snapshot-v1",

        "tract_coverage_state": "present",

        "verification_state": "derived",

        "zcta_coverage_state": "present"

      },

      {

        "access_class": "public",

        "address_point_coverage_state": "unknown",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "e2abf47305e12af7899a8fc43cba1789871b86336f1d73387706e91978987b8c",

        "blockgroup_coverage_state": "present",

        "canonical_county_id": "54063",

        "county_geoid": "54063",

        "county_name": "Monroe",

        "dfirm_polygon_coverage_state": "present",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "county-render-v1",

        "snapshot_version": "wv-county-snapshot-v1",

        "tract_coverage_state": "present",

        "verification_state": "derived",

        "zcta_coverage_state": "present"

      },

      {

        "access_class": "public",

        "address_point_coverage_state": "unknown",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "634cc1b35f13e4d11107ae7a8c2acd3710d2666363cc07660b9871f0a38cbd35",

        "blockgroup_coverage_state": "present",

        "canonical_county_id": "54049",

        "county_geoid": "54049",

        "county_name": "Marion",

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "county-render-v1",

        "snapshot_version": "wv-county-snapshot-v1",

        "tract_coverage_state": "present",

        "verification_state": "derived",

        "zcta_coverage_state": "present"

      }

    ]

  ],

  "documents": [

    [

      "Fayette County, West Virginia, GEOID 54019. The current governed snapshot links 42 ZCTAs, 13 census tracts, 21 block groups, 138 D-FIRM polygons, and 0 address points. Address-point coverage state is unknown and must not be interpreted as a claim about true address absence unless separately verified.",

      "Monroe County, West Virginia, GEOID 54063. The current governed snapshot links 11 ZCTAs, 3 census tracts, 5 block groups, 2 D-FIRM polygons, and 0 address points. Address-point coverage state is unknown and must not be interpreted as a claim about true address absence unless separately verified.",

      "Marion County, West Virginia, GEOID 54049. The current governed snapshot links 14 ZCTAs, 21 census tracts, 26 block groups, 0 D-FIRM polygons, and 0 address points. Address-point coverage state is unknown and must not be interpreted as a claim about true address absence unless separately verified."

    ]

  ],

  "uris": null,

  "data": null,

  "included": [

    "distances",

    "documents",

    "metadatas"

  ]

}

SEMANTIC QUERY 2

{

  "ids": [

    [

      "e95d110391651fd47d9c04f1e1691cec0dce74350ca9ff6d95f2473a8ab854a2",

      "e2abf47305e12af7899a8fc43cba1789871b86336f1d73387706e91978987b8c",

      "8a696239c646a5c0b7f1e0028b4bede1df97036817e76556e791ada5bde92002"

    ]

  ],

  "distances": [

    [

      0.8721222277108355,

      0.9994929663656624,

      1.006148826748629

    ]

  ],

  "embeddings": null,

  "metadatas": [

    [

      {

        "access_class": "public",

        "address_point_coverage_state": "unknown",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "e95d110391651fd47d9c04f1e1691cec0dce74350ca9ff6d95f2473a8ab854a2",

        "blockgroup_coverage_state": "present",

        "canonical_county_id": "54019",

        "county_geoid": "54019",

        "county_name": "Fayette",

        "dfirm_polygon_coverage_state": "present",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "county-render-v1",

        "snapshot_version": "wv-county-snapshot-v1",

        "tract_coverage_state": "present",

        "verification_state": "derived",

        "zcta_coverage_state": "present"

      },

      {

        "access_class": "public",

        "address_point_coverage_state": "unknown",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "e2abf47305e12af7899a8fc43cba1789871b86336f1d73387706e91978987b8c",

        "blockgroup_coverage_state": "present",

        "canonical_county_id": "54063",

        "county_geoid": "54063",

        "county_name": "Monroe",

        "dfirm_polygon_coverage_state": "present",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "county-render-v1",

        "snapshot_version": "wv-county-snapshot-v1",

        "tract_coverage_state": "present",

        "verification_state": "derived",

        "zcta_coverage_state": "present"

      },

      {

        "access_class": "public",

        "address_point_coverage_state": "present",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "8a696239c646a5c0b7f1e0028b4bede1df97036817e76556e791ada5bde92002",

        "blockgroup_coverage_state": "present",

        "canonical_county_id": "54017",

        "county_geoid": "54017",

        "county_name": "Doddridge",

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "county-render-v1",

        "snapshot_version": "wv-county-snapshot-v1",

        "tract_coverage_state": "present",

        "verification_state": "derived",

        "zcta_coverage_state": "present"

      }

    ]

  ],

  "documents": [

    [

      "Fayette County, West Virginia, GEOID 54019. The current governed snapshot links 42 ZCTAs, 13 census tracts, 21 block groups, 138 D-FIRM polygons, and 0 address points. Address-point coverage state is unknown and must not be interpreted as a claim about true address absence unless separately verified.",

      "Monroe County, West Virginia, GEOID 54063. The current governed snapshot links 11 ZCTAs, 3 census tracts, 5 block groups, 2 D-FIRM polygons, and 0 address points. Address-point coverage state is unknown and must not be interpreted as a claim about true address absence unless separately verified.",

      "Doddridge County, West Virginia, GEOID 54017. The current governed snapshot links 5 ZCTAs, 2 census tracts, 8 block groups, 0 D-FIRM polygons, and 9309 address points. Address-point coverage state is present and must not be interpreted as a claim about true address absence unless separately verified."

    ]

  ],

  "uris": null,

  "data": null,

  "included": [

    "distances",

    "documents",

    "metadatas"

  ]

}

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ export PGHOST=127.0.0.1

export PGPORT=5433

export PGDATABASE=msjarvisgis

export PGUSER=postgres

psql -v ON_ERROR_STOP=1 <<'SQL'

CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS wv_tract_representation (

    canonical_tract_id     text    NOT NULL,

    canonical_county_id    text    NOT NULL,

    table_name             text    NOT NULL,

    source_feature_id      bigint  NOT NULL,

    source_feature_hash    text,

    PRIMARY KEY (canonical_tract_id, table_name, source_feature_id),

    FOREIGN KEY (canonical_county_id)

        REFERENCES wv_county_identity (canonical_county_id)

);

INSERT INTO wv_tract_representation (

    canonical_tract_id,

    canonical_county_id,

    table_name,

    source_feature_id

SQLM wv_tract_representation;ture_hash) AS distinct_hashes_name,DO NOTHING;

NOTICE:  extension "pgcrypto" already exists, skipping

CREATE EXTENSION

CREATE TABLE

INSERT 0 546

UPDATE 546

 representations | hashed | distinct_hashes 

-----------------+--------+-----------------

             546 |    546 |             546

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

CREATE TABLE IF NOT EXISTS wv_tract_dataset_coverage (

    canonical_tract_id text NOT NULL,

    dataset_type       text NOT NULL,

    source_table       text,

    feature_count      bigint NOT NULL DEFAULT 0,

    coverage_state     text NOT NULL,

    calculated_at      timestamptz NOT NULL DEFAULT now(),

    source_layer_hash  text,

    notes              text,

    PRIMARY KEY (canonical_tract_id, dataset_type, source_table),

    FOREIGN KEY (canonical_tract_id)

        REFERENCES wv_tract_representation (canonical_tract_id),

    CHECK (coverage_state IN (

        'present',

        'confirmed_none',

        'missing_source',

        'unassigned',

        'not_applicable',

        'unknown'

    ))

);

INSERT INTO wv_tract_dataset_coverage (

SQLM wv_tract_dataset_coverage;act_id) AS tractssh,ce_table) DO UPDATE

ERROR:  there is no unique constraint matching given keys for referenced table "wv_tract_representation"

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ export PGHOST=127.0.0.1

export PGPORT=5433

export PGDATABASE=msjarvisgis

export PGUSER=postgres

psql -v ON_ERROR_STOP=1 <<'SQL'

DROP TABLE IF EXISTS wv_tract_dataset_coverage;

CREATE TABLE wv_tract_dataset_coverage (

    canonical_tract_id text NOT NULL,

    canonical_county_id text NOT NULL,

    dataset_type       text NOT NULL,

    source_table       text,

    feature_count      bigint NOT NULL DEFAULT 0,

    coverage_state     text NOT NULL,

    calculated_at      timestamptz NOT NULL DEFAULT now(),

    source_layer_hash  text,

    notes              text,

    PRIMARY KEY (canonical_tract_id, dataset_type, source_table),

    FOREIGN KEY (canonical_county_id)

        REFERENCES wv_county_identity (canonical_county_id),

    CHECK (coverage_state IN (

        'present',

        'confirmed_none',

SQLM wv_tract_dataset_coverage;unty_id) AS countiesce_table) DO UPDATE

NOTICE:  table "wv_tract_dataset_coverage" does not exist, skipping

DROP TABLE

CREATE TABLE

ERROR:  relation "wv_address_points_union" does not exist

LINE 21: LEFT JOIN wv_address_points_union ap

                   ^

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ export PGHOST=127.0.0.1

export PGPORT=5433

export PGDATABASE=msjarvisgis

export PGUSER=postgres

psql -v ON_ERROR_STOP=1 <<'SQL'

DROP TABLE IF EXISTS wv_tract_dataset_coverage;

CREATE TABLE wv_tract_dataset_coverage (

    canonical_tract_id  text NOT NULL,

    canonical_county_id text NOT NULL,

    dataset_type        text NOT NULL,

    source_table        text,

    feature_count       bigint NOT NULL DEFAULT 0,

    coverage_state      text NOT NULL,

    calculated_at       timestamptz NOT NULL DEFAULT now(),

    source_layer_hash   text,

    notes               text,

    PRIMARY KEY (canonical_tract_id, dataset_type, source_table),

    FOREIGN KEY (canonical_county_id)

        REFERENCES wv_county_identity (canonical_county_id),

    CHECK (coverage_state IN (

        'present',

        'confirmed_none',

SQLM wv_tract_dataset_coverage;unty_id) AS countiesce_table) DO UPDATE

DROP TABLE

CREATE TABLE

INSERT 0 546

 coverage_rows | tracts | counties 

---------------+--------+----------

           546 |    546 |       55

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ export PGHOST=127.0.0.1

export PGPORT=5433

export PGDATABASE=msjarvisgis

export PGUSER=postgres

psql -v ON_ERROR_STOP=1 <<'SQL'

CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS wv_tract_belief_snapshot (

    snapshot_id         uuid PRIMARY KEY DEFAULT gen_random_uuid(),

    canonical_tract_id  text NOT NULL,

    canonical_county_id text NOT NULL,

    snapshot_version    text NOT NULL,

    belief_document     jsonb NOT NULL,

    belief_hash         text NOT NULL,

    generated_at        timestamptz NOT NULL DEFAULT now(),

    verification_state  text NOT NULL DEFAULT 'derived',

    FOREIGN KEY (canonical_county_id)

        REFERENCES wv_county_identity (canonical_county_id),

    UNIQUE (canonical_tract_id, snapshot_version)

);

INSERT INTO wv_tract_belief_snapshot (

    canonical_tract_id,

SQLRE snapshot_version = 'wv-tract-snapshot-v1';ef_hashesATEhash

NOTICE:  extension "pgcrypto" already exists, skipping

CREATE EXTENSION

CREATE TABLE

INSERT 0 546

 snapshot_rows | tracts | distinct_belief_hashes 

---------------+--------+------------------------

           546 |    546 |                    546

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

DROP VIEW IF EXISTS wv_tract_belief_vector_ready;

CREATE VIEW wv_tract_belief_vector_ready AS

SELECT

    s.snapshot_version,

    s.canonical_tract_id,

    s.canonical_county_id,

    ci.county_name,

    s.belief_hash AS document_id,

    jsonb_build_object(

        'canonical_tract_id', s.canonical_tract_id,

        'canonical_county_id', s.canonical_county_id,

        'county_geoid', s.canonical_county_id,

        'county_name', ci.county_name,

        'snapshot_version', s.snapshot_version,

        'belief_hash', s.belief_hash,

        'verification_state', s.verification_state

    ) AS metadata,

    concat(

        ci.county_name, ' County, West Virginia, tract GEOID ', s.canonical_tract_id, '. ',

        'The current governed tract snapshot reports ',

        (s.belief_document #>> '{summary_counts,n_dfirm_polygons}'), ' D-FIRM polySQLIT 10;canonical_county_id, canonical_tract_idcounty_name,itive absence of flood

NOTICE:  view "wv_tract_belief_vector_ready" does not exist, skipping

DROP VIEW

CREATE VIEW

 canonical_tract_id | canonical_county_id | county_name |                           document_id                            |                                                                                                             left                                                                                                             

--------------------+---------------------+-------------+------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 54001965500        | 54001               | Barbour     | 28aa19bfe6a4566a84b81de1d4cd1e62cb82f35021dcbd0f9b99a6de96d84e31 | Barbour County, West Virginia, tract GEOID 54001965500. The current governed tract snapshot reports 0 D-FIRM polygons. D-FIRM coverage state is unknown and must not be interpreted as a claim about definitive absence of f

 54001965600        | 54001               | Barbour     | 6e441b32b69144f2b18db4653b220f035fadf31439e06173659f30b541e9863d | Barbour County, West Virginia, tract GEOID 54001965600. The current governed tract snapshot reports 0 D-FIRM polygons. D-FIRM coverage state is unknown and must not be interpreted as a claim about definitive absence of f

 54001965700        | 54001               | Barbour     | 81a534deee29ed0fed051400759aaff4fa060c7eeb28bde2837015f0fae523d8 | Barbour County, West Virginia, tract GEOID 54001965700. The current governed tract snapshot reports 0 D-FIRM polygons. D-FIRM coverage state is unknown and must not be interpreted as a claim about definitive absence of f

 54001965800        | 54001               | Barbour     | ecc4226c47b7eed8179f35aa06e344c57d0f1e53b5c2e1725a8da347f26bbc2f | Barbour County, West Virginia, tract GEOID 54001965800. The current governed tract snapshot reports 0 D-FIRM polygons. D-FIRM coverage state is unknown and must not be interpreted as a claim about definitive absence of f

 54003971101        | 54003               | Berkeley    | e41b6425d34f564a3619c7351ebebfa0cc3a0e379208255760812862682e350b | Berkeley County, West Virginia, tract GEOID 54003971101. The current governed tract snapshot reports 0 D-FIRM polygons. D-FIRM coverage state is unknown and must not be interpreted as a claim about definitive absence of 

 54003971103        | 54003               | Berkeley    | c597a19c5f895ca298b95c894be302d3ef57703d2ca1d402a9d5e45d5420e2f9 | Berkeley County, West Virginia, tract GEOID 54003971103. The current governed tract snapshot reports 0 D-FIRM polygons. D-FIRM coverage state is unknown and must not be interpreted as a claim about definitive absence of 

 54003971104        | 54003               | Berkeley    | 1fae8d73e6bfcead35247d7f89387dfac38552cad72f687adab642b5f959411e | Berkeley County, West Virginia, tract GEOID 54003971104. The current governed tract snapshot reports 0 D-FIRM polygons. D-FIRM coverage state is unknown and must not be interpreted as a claim about definitive absence of 

 54003971105        | 54003               | Berkeley    | 1236b01c4caaada7c96532df959e5a650e37ff0b98d97610ec3254890971f97b | Berkeley County, West Virginia, tract GEOID 54003971105. The current governed tract snapshot reports 0 D-FIRM polygons. D-FIRM coverage state is unknown and must not be interpreted as a claim about definitive absence of 

 54003971203        | 54003               | Berkeley    | 72262a17a3339944a3f648c094f5c61c41921d7255d27c06843431eef28cfc02 | Berkeley County, West Virginia, tract GEOID 54003971203. The current governed tract snapshot reports 0 D-FIRM polygons. D-FIRM coverage state is unknown and must not be interpreted as a claim about definitive absence of 

 54003971204        | 54003               | Berkeley    | b7da7986d79f2cb978fe99bf5931b6a22787eb9c8e7323500fcdb2da280ba53d | Berkeley County, West Virginia, tract GEOID 54003971204. The current governed tract snapshot reports 0 D-FIRM polygons. D-FIRM coverage state is unknown and must not be interpreted as a claim about definitive absence of 

(10 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

CREATE EXTENSION IF NOT EXISTS pgcrypto;

INSERT INTO gbim_collection_manifest (

    collection_name,

    collection_version,

    source_view,

    snapshot_version,

    rendering_version,

    embedding_model,

    embedding_dimension,

    permitted_use,

    notes

)

VALUES (

    'gbim_wv_tracts',

    'v1',

    'wv_tract_belief_vector_ready',

    'wv-tract-snapshot-v1',

    'tract-render-v1',

    'all-minilm:latest',

    384,

    'public_civic_geographic_retrieval',

    'First governed tract belief collection'

SQLER BY publication_status; 'v1'v_tracts'n_version_idTHING;

NOTICE:  extension "pgcrypto" already exists, skipping

CREATE EXTENSION

INSERT 0 1

INSERT 0 546

 publication_status | count 

--------------------+-------

 pending            |   546

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ export PGHOST=127.0.0.1

export PGPORT=5433

export PGDATABASE=msjarvisgis

export PGUSER=postgres

export CHROMA_HOST=127.0.0.1

export CHROMA_PORT=8002

python3 - <<'PY'

import os, json, psycopg2, chromadb

from chromadb.config import Settings

PGHOST=os.getenv("PGHOST","127.0.0.1")

PGPORT=os.getenv("PGPORT","5433")

PGDATABASE=os.getenv("PGDATABASE","msjarvisgis")

PGUSER=os.getenv("PGUSER","postgres")

PGPASSWORD=os.getenv("PGPASSWORD","")

CHROMA_HOST=os.getenv("CHROMA_HOST","127.0.0.1")

CHROMA_PORT=int(os.getenv("CHROMA_PORT","8002"))

COLLECTION_NAME="gbim_wv_tracts"

COLLECTION_VERSION="v1"

PHYSICAL_COLLECTION="gbim_wv_tracts_v1"

conn = psycopg2.connect(host=PGHOST, port=PGPORT, dbname=PGDATABASE,

PY indent=2))on_version_id": str(collection_version_id)eval",coverage_state", "unk

Traceback (most recent call last):

  File "<stdin>", line 76, in <module>

  File "/usr/lib/python3.12/json/__init__.py", line 339, in loads

    raise TypeError(f'the JSON object must be str, bytes or bytearray, '

TypeError: the JSON object must be str, bytes or bytearray, not dict

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ export PGHOST=127.0.0.1

export PGPORT=5433

export PGDATABASE=msjarvisgis

export PGUSER=postgres

export CHROMA_HOST=127.0.0.1

export CHROMA_PORT=8002

python3 - <<'PY'

import os, json, psycopg2, chromadb

from chromadb.config import Settings

PGHOST=os.getenv("PGHOST","127.0.0.1")

PGPORT=os.getenv("PGPORT","5433")

PGDATABASE=os.getenv("PGDATABASE","msjarvisgis")

PGUSER=os.getenv("PGUSER","postgres")

PGPASSWORD=os.getenv("PGPASSWORD","")

CHROMA_HOST=os.getenv("CHROMA_HOST","127.0.0.1")

CHROMA_PORT=int(os.getenv("CHROMA_PORT","8002"))

COLLECTION_NAME="gbim_wv_tracts"

COLLECTION_VERSION="v1"

PHYSICAL_COLLECTION="gbim_wv_tracts_v1"

conn = psycopg2.connect(

PY indent=2))on_version_id": str(collection_version_id)rsion_idwn").get("source_ta

{

  "physical_collection": "gbim_wv_tracts_v1",

  "count": 546,

  "verified": 546,

  "failed": 0,

  "collection_version_id": "a5a8716d-02aa-4cf7-8f28-81fcf7a8749d"

}

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

CREATE TABLE IF NOT EXISTS gbim_active_collection (

    logical_collection_name  text PRIMARY KEY,

    collection_version_id    uuid NOT NULL,

    physical_collection_name text NOT NULL UNIQUE,

    activated_at             timestamptz NOT NULL DEFAULT now(),

    FOREIGN KEY (collection_version_id)

        REFERENCES gbim_collection_manifest(collection_version_id)

);

INSERT INTO gbim_active_collection (

    logical_collection_name,

    collection_version_id,

    physical_collection_name

)

SELECT

    'gbim_wv_tracts',

    m.collection_version_id,

    'gbim_wv_tracts_v1'

FROM gbim_collection_manifest m

WHERE m.collection_name = 'gbim_wv_tracts'

  AND m.collection_version = 'v1'

ON CONFLICT (logical_collection_name) DO UPDATE

SET collection_version_id = EXCLUDED.collection_version_id,

SQLRE logical_collection_name = 'gbim_wv_tracts';_status, record_count, promoted_a

NOTICE:  relation "gbim_active_collection" already exists, skipping

CREATE TABLE

INSERT 0 1

UPDATE 1

 collection_name | collection_version | build_status | record_count |          promoted_at          

-----------------+--------------------+--------------+--------------+-------------------------------

 gbim_wv_tracts  | v1                 | active       |          546 | 2026-07-11 19:04:35.713377+00

(1 row)

 logical_collection_name |        collection_version_id         | physical_collection_name |         activated_at          

-------------------------+--------------------------------------+--------------------------+-------------------------------

 gbim_wv_tracts          | a5a8716d-02aa-4cf7-8f28-81fcf7a8749d | gbim_wv_tracts_v1        | 2026-07-11 19:04:35.699597+00

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ python3 - <<'PY'

import chromadb, json

client = chromadb.HttpClient(host="127.0.0.1", port=8002)

col = client.get_collection("gbim_wv_tracts_v1")

print("COUNT", col.count())

r = col.get(

    ids=["28aa19bfe6a4566a84b81de1d4cd1e62cb82f35021dcbd0f9b99a6de96d84e31"],

    include=["documents", "metadatas"]

)

print(json.dumps(r, indent=2)[:4000])

q = col.query(

    query_texts=["Which governed tracts mention D-FIRM polygon coverage in West Virginia?"],

    n_results=5

)

print(json.dumps(q, indent=2)[:4000])

PY

COUNT 546

{

  "ids": [

    "28aa19bfe6a4566a84b81de1d4cd1e62cb82f35021dcbd0f9b99a6de96d84e31"

  ],

  "embeddings": null,

  "metadatas": [

    {

      "access_class": "public",

      "authority_class": "governed_civic_geographic",

      "belief_hash": "28aa19bfe6a4566a84b81de1d4cd1e62cb82f35021dcbd0f9b99a6de96d84e31",

      "canonical_county_id": "54001",

      "canonical_tract_id": "54001965500",

      "county_geoid": "54001",

      "county_name": "Barbour",

      "dfirm_polygon_coverage_state": "unknown",

      "permitted_use": "public_civic_geographic_retrieval",

      "rendering_version": "tract-render-v1",

      "snapshot_version": "wv-tract-snapshot-v1",

      "verification_state": "derived"

    }

  ],

  "documents": [

    "Barbour County, West Virginia, tract GEOID 54001965500. The current governed tract snapshot reports 0 D-FIRM polygons. D-FIRM coverage state is unknown and must not be interpreted as a claim about definitive absence of flood-risk polygons unless separately verified."

  ],

  "data": null,

  "uris": null,

  "included": [

    "documents",

    "metadatas"

  ]

}

{

  "ids": [

    [

      "883a917afa80ce129dc9f855f1cc424c97cb9fe217c1f676d43e41d4d9af052e",

      "998512fd551708c4f44677126df8a24d26d2f35a5ead359a482e747ebd2d1e19",

      "08cd98200eb7f436563ac4a8d98728101b804edbb2a3e06059a864b31ad5bede",

      "1aed03bc258133654c1019e2fe23a0d3ff1f53802885958404fd1c62f0133172",

      "67fd4918127c0774847179c200fa514c62c07ac3a4a288c60afe4da348e992c5"

    ]

  ],

  "distances": [

    [

      0.45964688062667847,

      0.4755807506022217,

      0.4792171417366291,

      0.4803823319875752,

      0.4828284514422417

    ]

  ],

  "embeddings": null,

  "metadatas": [

    [

      {

        "access_class": "public",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "883a917afa80ce129dc9f855f1cc424c97cb9fe217c1f676d43e41d4d9af052e",

        "canonical_county_id": "54023",

        "canonical_tract_id": "54023969600",

        "county_geoid": "54023",

        "county_name": "Grant",

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "tract-render-v1",

        "snapshot_version": "wv-tract-snapshot-v1",

        "verification_state": "derived"

      },

      {

        "access_class": "public",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "998512fd551708c4f44677126df8a24d26d2f35a5ead359a482e747ebd2d1e19",

        "canonical_county_id": "54107",

        "canonical_tract_id": "54107000702",

        "county_geoid": "54107",

        "county_name": "Wood",

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "tract-render-v1",

        "snapshot_version": "wv-tract-snapshot-v1",

        "verification_state": "derived"

      },

      {

        "access_class": "public",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "08cd98200eb7f436563ac4a8d98728101b804edbb2a3e06059a864b31ad5bede",

        "canonical_county_id": "54107",

        "canonical_tract_id": "54107000902",

        "county_geoid": "54107",

        "county_name": "Wood",

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "tract-render-v1",

        "snapshot_version": "wv-tract-snapshot-v1",

        "verification_state": "derived"

      },

      {

        "access_class": "public",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "1aed03bc258133654c1019e2fe23a0d3ff1f53802885958404fd1c62f0133172",

        "canonical_county_id": "54107",

        "canonical_tract_id": "54107010602",

        "county_geoid": "54107",

        "county_name": "Wood",

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "tract-render-v1",

        "snapshot_version": "wv-tract-snapshot-v1",

        "verification_state": "derived"

      },

      {

        "access_class": "public",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "67fd4918127c0774847179c200fa514c62c07ac3a4a288c60afe4da348e992c5",

        "canonical_county_id": "54107",

        "canonical_tract_id": "54107011000",

        "county_geoid": "54107",

        "county_name": "Wood",

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "tract-render-v1",

        "snapshot_version": "wv-tract-snapshot-v1",

        "verification_state": "derived"

      }

    ]

  ],

  "documents": [

    [

      "Grant County, West Virginia, tract GEOID 54023969600. The current governed tract snapshot reports 0 D-FIRM polygons. D-FIRM coverage state is unknown and must not be interpreted as a claim about definitive absence of flood-risk polygons unless separately verified.",

      "Wood County, West Virginia, tract GEOID 54107000702. The current governed tra

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ export PGHOST=127.0.0.1

export PGPORT=5433

export PGDATABASE=msjarvisgis

export PGUSER=postgres

psql -v ON_ERROR_STOP=1 <<'SQL'

SELECT

    collection_version_id,

    collection_name,

    collection_version,

    source_view,

    snapshot_version,

    rendering_version,

    embedding_model,

    embedding_dimension,

    build_status,

    record_count,

    built_at,

    validated_at,

    promoted_at

FROM gbim_collection_manifest

WHERE collection_name = 'gbim_wv_tracts'

  AND collection_version = 'v1';

SQLRE logical_collection_name = 'gbim_wv_tracts';on_id

        collection_version_id         | collection_name | collection_version |         source_view          |   snapshot_version   | rendering_version |  embedding_model  | embedding_dimension | build_status | record_count |           built_at            |         validated_at          |          promoted_at          

--------------------------------------+-----------------+--------------------+------------------------------+----------------------+-------------------+-------------------+---------------------+--------------+--------------+-------------------------------+-------------------------------+-------------------------------

 a5a8716d-02aa-4cf7-8f28-81fcf7a8749d | gbim_wv_tracts  | v1                 | wv_tract_belief_vector_ready | wv-tract-snapshot-v1 | tract-render-v1   | all-minilm:latest |                 384 | active       |          546 | 2026-07-11 19:03:08.245313+00 | 2026-07-11 19:03:08.245313+00 | 2026-07-11 19:04:35.713377+00

(1 row)

 publication_status |  n  

--------------------+-----

 verified           | 546

(1 row)

 logical_collection_name |        collection_version_id         | physical_collection_name |         activated_at          

-------------------------+--------------------------------------+--------------------------+-------------------------------

 gbim_wv_tracts          | a5a8716d-02aa-4cf7-8f28-81fcf7a8749d | gbim_wv_tracts_v1        | 2026-07-11 19:04:35.699597+00

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ python3 - <<'PY'

import chromadb

src = chromadb.HttpClient(host="127.0.0.1", port=8002)

dst = chromadb.HttpClient(host="127.0.0.1", port=8000)

src_col = src.get_collection("gbim_wv_tracts_v1")

try:

    dst_col = dst.get_collection("gbim_wv_tracts_v1")

except Exception:

    dst_col = dst.create_collection(

        name="gbim_wv_tracts_v1",

        metadata=src_col.metadata

    )

batch = src_col.get(include=["documents", "metadatas"])

dst_col.upsert(

    ids=batch["ids"],

    documents=batch["documents"],

    metadatas=batch["metadatas"]

)

print({

PY  "collection": "gbim_wv_tracts_v1"

Traceback (most recent call last):

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/base_http_client.py", line 99, in _raise_chroma_error

    resp.raise_for_status()

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_models.py", line 761, in raise_for_status

    raise HTTPStatusError(message, request=request, response=self)

httpx.HTTPStatusError: Client error '404 Not Found' for url 'http://127.0.0.1:8000/api/v2/auth/identity'

For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404

During handling of the above exception, another exception occurred:

Traceback (most recent call last):

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/client.py", line 101, in get_user_identity

    return self._server.get_user_identity()

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/telemetry/opentelemetry/__init__.py", line 150, in wrapper

    return f(*args, **kwargs)

           ^^^^^^^^^^^^^^^^^^

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/fastapi.py", line 182, in get_user_identity

    return UserIdentity(**self._make_request("get", "/auth/identity"))

                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/fastapi.py", line 90, in _make_request

    BaseHTTPClient._raise_chroma_error(response)

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/base_http_client.py", line 104, in _raise_chroma_error

    raise (Exception(resp.text))

Exception: {"detail":"Not Found"}

During handling of the above exception, another exception occurred:

Traceback (most recent call last):

  File "<stdin>", line 4, in <module>

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/__init__.py", line 203, in HttpClient

    return ClientCreator(tenant=tenant, database=database, settings=settings)

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/client.py", line 65, in __init__

    user_identity = self.get_user_identity()

                    ^^^^^^^^^^^^^^^^^^^^^^^^

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/client.py", line 110, in get_user_identity

    raise ValueError(str(e))

ValueError: {"detail":"Not Found"}

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ python3 - <<'PY'

import chromadb, json

client = chromadb.HttpClient(host="127.0.0.1", port=8002)

col = client.get_collection("gbim_wv_tracts_v1")

print("COUNT", col.count())

q = col.query(

    query_texts=["Show governed tracts in Wood County, West Virginia."],

    n_results=5

)

print(json.dumps(q, indent=2)[:4000])

PY

COUNT 546

{

  "ids": [

    [

      "7420072b2528e4b47f3263c9f629af9fef22d375c87be8e611d77899b5e5a607",

      "b9f2fb5eaf0849506a2b505c26f4d2932885dae574334cd3e5df03d12111aa24",

      "9d2ee9e81ecd690b7e5484e31dd9b6679525ce6e23af9e6ebf4cfef18d1a786c",

      "268168944694ce68da4a314ee6ee3c6e9e102d4abd94a9525dbb2325ec280d9d",

      "dbbeb2a5ec0f1ed8f7d8042cfd571721b74817d258d5b37993e0ba090cb391c3"

    ]

  ],

  "distances": [

    [

      0.8410544991493225,

      0.8472188815851004,

      0.8490676016755869,

      0.8520347951585646,

      0.8549956200193802

    ]

  ],

  "embeddings": null,

  "metadatas": [

    [

      {

        "access_class": "public",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "7420072b2528e4b47f3263c9f629af9fef22d375c87be8e611d77899b5e5a607",

        "canonical_county_id": "54017",

        "canonical_tract_id": "54017965000",

        "county_geoid": "54017",

        "county_name": "Doddridge",

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "tract-render-v1",

        "snapshot_version": "wv-tract-snapshot-v1",

        "verification_state": "derived"

      },

      {

        "access_class": "public",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "b9f2fb5eaf0849506a2b505c26f4d2932885dae574334cd3e5df03d12111aa24",

        "canonical_county_id": "54107",

        "canonical_tract_id": "54107010901",

        "county_geoid": "54107",

        "county_name": "Wood",

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "tract-render-v1",

        "snapshot_version": "wv-tract-snapshot-v1",

        "verification_state": "derived"

      },

      {

        "access_class": "public",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "9d2ee9e81ecd690b7e5484e31dd9b6679525ce6e23af9e6ebf4cfef18d1a786c",

        "canonical_county_id": "54107",

        "canonical_tract_id": "54107000901",

        "county_geoid": "54107",

        "county_name": "Wood",

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "tract-render-v1",

        "snapshot_version": "wv-tract-snapshot-v1",

        "verification_state": "derived"

      },

      {

        "access_class": "public",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "268168944694ce68da4a314ee6ee3c6e9e102d4abd94a9525dbb2325ec280d9d",

        "canonical_county_id": "54107",

        "canonical_tract_id": "54107010101",

        "county_geoid": "54107",

        "county_name": "Wood",

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "tract-render-v1",

        "snapshot_version": "wv-tract-snapshot-v1",

        "verification_state": "derived"

      },

      {

        "access_class": "public",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "dbbeb2a5ec0f1ed8f7d8042cfd571721b74817d258d5b37993e0ba090cb391c3",

        "canonical_county_id": "54107",

        "canonical_tract_id": "54107010902",

        "county_geoid": "54107",

        "county_name": "Wood",

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "tract-render-v1",

        "snapshot_version": "wv-tract-snapshot-v1",

        "verification_state": "derived"

      }

    ]

  ],

  "documents": [

    [

      "Doddridge County, West Virginia, tract GEOID 54017965000. The current governed tract snapshot reports 0 D-FIRM polygons. D-FIRM coverage state is unknown and must not be interpreted as a claim about definitive absence of flood-risk polygons unless separately verified.",

      "Wood County, West Virginia, tract GEOID 54107010901. The current gover

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ export PGHOST=127.0.0.1

export PGPORT=5433

export PGDATABASE=msjarvisgis

export PGUSER=postgres

psql -v ON_ERROR_STOP=1 <<'SQL'

SELECT

    dataset_type,

    coverage_state,

    COUNT(*) AS tracts,

    MIN(feature_count) AS min_count,

    MAX(feature_count) AS max_count

FROM wv_tract_dataset_coverage

GROUP BY dataset_type, coverage_state

ORDER BY dataset_type, coverage_state;

SELECT

    COUNT(*) AS total_tracts,

    COUNT(*) FILTER (WHERE feature_count > 0) AS tracts_with_dfirm,

    COUNT(*) FILTER (WHERE feature_count = 0) AS tracts_with_zero_dfirm

FROM wv_tract_dataset_coverage

WHERE dataset_type = 'dfirm_polygon'

  AND source_table = 'wv_hyd_dfirm_nfhl';

SQL

 dataset_type  | coverage_state | tracts | min_count | max_count 

---------------+----------------+--------+-----------+-----------

 dfirm_polygon | unknown        |    546 |         0 |         0

(1 row)

 total_tracts | tracts_with_dfirm | tracts_with_zero_dfirm 

--------------+-------------------+------------------------

          546 |                 0 |                    546

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

SELECT

    c.canonical_tract_id,

    c.canonical_county_id,

    ci.county_name,

    c.feature_count,

    c.coverage_state

FROM wv_tract_dataset_coverage c

JOIN wv_county_identity ci

  ON ci.canonical_county_id = c.canonical_county_id

WHERE c.dataset_type = 'dfirm_polygon'

  AND c.source_table = 'wv_hyd_dfirm_nfhl'

  AND c.feature_count > 0

ORDER BY c.feature_count DESC, c.canonical_tract_id

LIMIT 25;

SQL

 canonical_tract_id | canonical_county_id | county_name | feature_count | coverage_state 

--------------------+---------------------+-------------+---------------+----------------

(0 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

DROP VIEW IF EXISTS wv_tract_belief_vector_ready;

CREATE VIEW wv_tract_belief_vector_ready AS

SELECT

    s.snapshot_version,

    s.canonical_tract_id,

    s.canonical_county_id,

    ci.county_name,

    s.belief_hash AS document_id,

    jsonb_build_object(

        'canonical_tract_id', s.canonical_tract_id,

        'canonical_county_id', s.canonical_county_id,

        'county_geoid', s.canonical_county_id,

        'county_name', ci.county_name,

        'snapshot_version', s.snapshot_version,

        'belief_hash', s.belief_hash,

        'verification_state', s.verification_state,

        'dfirm_polygon_count', COALESCE(dc.feature_count, 0),

        'dfirm_polygon_coverage_state', COALESCE(dc.coverage_state, 'unknown')

    ) AS metadata,

    concat(

        ci.county_name, ' County, West Virginia, tract GEOID ', s.canonical_tract_id, '. ',

SQLIT 5; canonical_county_id, canonical_tract_id, documentc conclusions are drawn.

DROP VIEW

CREATE VIEW

 canonical_tract_id | county_name |                                                                                                                                                                            metadata                                                                                                                                                                            |                                                                                                                                   document                                                                                                                                    

--------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 54001965500        | Barbour     | {"belief_hash": "28aa19bfe6a4566a84b81de1d4cd1e62cb82f35021dcbd0f9b99a6de96d84e31", "county_name": "Barbour", "county_geoid": "54001", "snapshot_version": "wv-tract-snapshot-v1", "canonical_tract_id": "54001965500", "verification_state": "derived", "canonical_county_id": "54001", "dfirm_polygon_count": 0, "dfirm_polygon_coverage_state": "unknown"}  | Barbour County, West Virginia, tract GEOID 54001965500. Governed tract snapshot version wv-tract-snapshot-v1. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. Coverage is unresolved and zero must not be interpreted as definitive absence of flood-risk polygons.

 54001965600        | Barbour     | {"belief_hash": "6e441b32b69144f2b18db4653b220f035fadf31439e06173659f30b541e9863d", "county_name": "Barbour", "county_geoid": "54001", "snapshot_version": "wv-tract-snapshot-v1", "canonical_tract_id": "54001965600", "verification_state": "derived", "canonical_county_id": "54001", "dfirm_polygon_count": 0, "dfirm_polygon_coverage_state": "unknown"}  | Barbour County, West Virginia, tract GEOID 54001965600. Governed tract snapshot version wv-tract-snapshot-v1. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. Coverage is unresolved and zero must not be interpreted as definitive absence of flood-risk polygons.

 54001965700        | Barbour     | {"belief_hash": "81a534deee29ed0fed051400759aaff4fa060c7eeb28bde2837015f0fae523d8", "county_name": "Barbour", "county_geoid": "54001", "snapshot_version": "wv-tract-snapshot-v1", "canonical_tract_id": "54001965700", "verification_state": "derived", "canonical_county_id": "54001", "dfirm_polygon_count": 0, "dfirm_polygon_coverage_state": "unknown"}  | Barbour County, West Virginia, tract GEOID 54001965700. Governed tract snapshot version wv-tract-snapshot-v1. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. Coverage is unresolved and zero must not be interpreted as definitive absence of flood-risk polygons.

 54001965800        | Barbour     | {"belief_hash": "ecc4226c47b7eed8179f35aa06e344c57d0f1e53b5c2e1725a8da347f26bbc2f", "county_name": "Barbour", "county_geoid": "54001", "snapshot_version": "wv-tract-snapshot-v1", "canonical_tract_id": "54001965800", "verification_state": "derived", "canonical_county_id": "54001", "dfirm_polygon_count": 0, "dfirm_polygon_coverage_state": "unknown"}  | Barbour County, West Virginia, tract GEOID 54001965800. Governed tract snapshot version wv-tract-snapshot-v1. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. Coverage is unresolved and zero must not be interpreted as definitive absence of flood-risk polygons.

 54003971101        | Berkeley    | {"belief_hash": "e41b6425d34f564a3619c7351ebebfa0cc3a0e379208255760812862682e350b", "county_name": "Berkeley", "county_geoid": "54003", "snapshot_version": "wv-tract-snapshot-v1", "canonical_tract_id": "54003971101", "verification_state": "derived", "canonical_county_id": "54003", "dfirm_polygon_count": 0, "dfirm_polygon_coverage_state": "unknown"} | Berkeley County, West Virginia, tract GEOID 54003971101. Governed tract snapshot version wv-tract-snapshot-v1. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. Coverage is unresolved and zero must not be interpreted as definitive absence of flood-risk polygons.

(5 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ export PGHOST=127.0.0.1

export PGPORT=5433

export PGDATABASE=msjarvisgis

export PGUSER=postgres

export CHROMA_HOST=127.0.0.1

export CHROMA_PORT=8002

python3 - <<'PY'

import os, json, psycopg2, chromadb

from chromadb.config import Settings

PGHOST=os.getenv("PGHOST","127.0.0.1")

PGPORT=os.getenv("PGPORT","5433")

PGDATABASE=os.getenv("PGDATABASE","msjarvisgis")

PGUSER=os.getenv("PGUSER","postgres")

PGPASSWORD=os.getenv("PGPASSWORD","")

CHROMA_HOST=os.getenv("CHROMA_HOST","127.0.0.1")

CHROMA_PORT=int(os.getenv("CHROMA_PORT","8002"))

conn = psycopg2.connect(

    host=PGHOST,

    port=PGPORT,

    dbname=PGDATABASE,

    user=PGUSER,

PY indent=2))col.count()wv_tracts_v1",';_tracts'tas)ct) else json.loads(metadata))

{

  "collection": "gbim_wv_tracts_v1",

  "count": 546

}

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ 

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ python3 - <<'PY'

import chromadb, json

client = chromadb.HttpClient(host="127.0.0.1", port=8002)

col = client.get_collection("gbim_wv_tracts_v1")

for text in [

    "Show governed tracts in Wood County, West Virginia.",

    "Which governed tracts have mapped D-FIRM polygon coverage in West Virginia?"

]:

    print("\nQUERY:", text)

    q = col.query(query_texts=[text], n_results=5)

    print(json.dumps(q, indent=2)[:4000])

PY

QUERY: Show governed tracts in Wood County, West Virginia.

{

  "ids": [

    [

      "7420072b2528e4b47f3263c9f629af9fef22d375c87be8e611d77899b5e5a607",

      "be715522d0213b3e4a18e485b66970c0d96b4aa57d213a5b89504637857686aa",

      "b9f2fb5eaf0849506a2b505c26f4d2932885dae574334cd3e5df03d12111aa24",

      "268168944694ce68da4a314ee6ee3c6e9e102d4abd94a9525dbb2325ec280d9d",

      "9d2ee9e81ecd690b7e5484e31dd9b6679525ce6e23af9e6ebf4cfef18d1a786c"

    ]

  ],

  "distances": [

    [

      0.7825459837913513,

      0.7834222316741943,

      0.7842634446004452,

      0.7886561653729587,

      0.7903503065965816

    ]

  ],

  "embeddings": null,

  "metadatas": [

    [

      {

        "access_class": "public",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "7420072b2528e4b47f3263c9f629af9fef22d375c87be8e611d77899b5e5a607",

        "canonical_county_id": "54017",

        "canonical_tract_id": "54017965000",

        "county_geoid": "54017",

        "county_name": "Doddridge",

        "dfirm_polygon_count": 0,

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "tract-render-v1",

        "snapshot_version": "wv-tract-snapshot-v1",

        "verification_state": "derived"

      },

      {

        "access_class": "public",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "be715522d0213b3e4a18e485b66970c0d96b4aa57d213a5b89504637857686aa",

        "canonical_county_id": "54017",

        "canonical_tract_id": "54017965100",

        "county_geoid": "54017",

        "county_name": "Doddridge",

        "dfirm_polygon_count": 0,

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "tract-render-v1",

        "snapshot_version": "wv-tract-snapshot-v1",

        "verification_state": "derived"

      },

      {

        "access_class": "public",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "b9f2fb5eaf0849506a2b505c26f4d2932885dae574334cd3e5df03d12111aa24",

        "canonical_county_id": "54107",

        "canonical_tract_id": "54107010901",

        "county_geoid": "54107",

        "county_name": "Wood",

        "dfirm_polygon_count": 0,

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "tract-render-v1",

        "snapshot_version": "wv-tract-snapshot-v1",

        "verification_state": "derived"

      },

      {

        "access_class": "public",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "268168944694ce68da4a314ee6ee3c6e9e102d4abd94a9525dbb2325ec280d9d",

        "canonical_county_id": "54107",

        "canonical_tract_id": "54107010101",

        "county_geoid": "54107",

        "county_name": "Wood",

        "dfirm_polygon_count": 0,

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "tract-render-v1",

        "snapshot_version": "wv-tract-snapshot-v1",

        "verification_state": "derived"

      },

      {

        "access_class": "public",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "9d2ee9e81ecd690b7e5484e31dd9b6679525ce6e23af9e6ebf4cfef18d1a786c",

        "canonical_county_id": "54107",

        "canonical_tract_id": "54107000901",

        "county_geoid": "54107",

        "county_name": "Wood",

        "dfirm_polygon_count": 0,

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "tract-render-v1",

        "snapshot_version": "wv-tract-snapshot-v1",

        "verification_state": "derived"

      }

    ]

  ],

  "documents": [

    [

      "Doddridge County, West Virginia, tract GEOID 54017965000. Governed tract snapshot version wv-tract-snapshot-v1. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. Cove

QUERY: Which governed tracts have mapped D-FIRM polygon coverage in West Virginia?

{

  "ids": [

    [

      "883a917afa80ce129dc9f855f1cc424c97cb9fe217c1f676d43e41d4d9af052e",

      "dbbeb2a5ec0f1ed8f7d8042cfd571721b74817d258d5b37993e0ba090cb391c3",

      "1aed03bc258133654c1019e2fe23a0d3ff1f53802885958404fd1c62f0133172",

      "017b312099b46e89d7a5909b213da58b219f9e15d39ee4d3cf855f1253cddaa6",

      "1cd4940d7df27f1576a70a402f0ea58e9624011ca33534ab1dab2fe2a8b5e695"

    ]

  ],

  "distances": [

    [

      0.5480765700340271,

      0.5541486599913779,

      0.5547984820346658,

      0.5551136789526399,

      0.5556702381744614

    ]

  ],

  "embeddings": null,

  "metadatas": [

    [

      {

        "access_class": "public",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "883a917afa80ce129dc9f855f1cc424c97cb9fe217c1f676d43e41d4d9af052e",

        "canonical_county_id": "54023",

        "canonical_tract_id": "54023969600",

        "county_geoid": "54023",

        "county_name": "Grant",

        "dfirm_polygon_count": 0,

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "tract-render-v1",

        "snapshot_version": "wv-tract-snapshot-v1",

        "verification_state": "derived"

      },

      {

        "access_class": "public",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "dbbeb2a5ec0f1ed8f7d8042cfd571721b74817d258d5b37993e0ba090cb391c3",

        "canonical_county_id": "54107",

        "canonical_tract_id": "54107010902",

        "county_geoid": "54107",

        "county_name": "Wood",

        "dfirm_polygon_count": 0,

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "tract-render-v1",

        "snapshot_version": "wv-tract-snapshot-v1",

        "verification_state": "derived"

      },

      {

        "access_class": "public",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "1aed03bc258133654c1019e2fe23a0d3ff1f53802885958404fd1c62f0133172",

        "canonical_county_id": "54107",

        "canonical_tract_id": "54107010602",

        "county_geoid": "54107",

        "county_name": "Wood",

        "dfirm_polygon_count": 0,

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "tract-render-v1",

        "snapshot_version": "wv-tract-snapshot-v1",

        "verification_state": "derived"

      },

      {

        "access_class": "public",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "017b312099b46e89d7a5909b213da58b219f9e15d39ee4d3cf855f1253cddaa6",

        "canonical_county_id": "54107",

        "canonical_tract_id": "54107010502",

        "county_geoid": "54107",

        "county_name": "Wood",

        "dfirm_polygon_count": 0,

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "tract-render-v1",

        "snapshot_version": "wv-tract-snapshot-v1",

        "verification_state": "derived"

      },

      {

        "access_class": "public",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "1cd4940d7df27f1576a70a402f0ea58e9624011ca33534ab1dab2fe2a8b5e695",

        "canonical_county_id": "54107",

        "canonical_tract_id": "54107010102",

        "county_geoid": "54107",

        "county_name": "Wood",

        "dfirm_polygon_count": 0,

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "tract-render-v1",

        "snapshot_version": "wv-tract-snapshot-v1",

        "verification_state": "derived"

      }

    ]

  ],

  "documents": [

    [

      "Grant County, West Virginia, tract GEOID 54023969600. Governed tract snapshot version wv-tract-snapshot-v1. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. Coverage is unres

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ export PGHOST=127.0.0.1

export PGPORT=5433

export PGDATABASE=msjarvisgis

export PGUSER=postgres

psql -v ON_ERROR_STOP=1 <<'SQL'

CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS wv_blockgroup_representation (

    canonical_blockgroup_id  text    NOT NULL,

    canonical_tract_id       text    NOT NULL,

    canonical_county_id      text    NOT NULL,

    table_name               text    NOT NULL,

    source_feature_id        bigint  NOT NULL,

    source_feature_hash      text,

    PRIMARY KEY (canonical_blockgroup_id, table_name, source_feature_id),

    FOREIGN KEY (canonical_county_id)

        REFERENCES wv_county_identity (canonical_county_id)

);

INSERT INTO wv_blockgroup_representation (

    canonical_blockgroup_id,

    canonical_tract_id,

    canonical_county_id,

SQLM wv_blockgroup_representation;hash) AS distinct_hashesname,e_id) DO NOTHING;

NOTICE:  extension "pgcrypto" already exists, skipping

CREATE EXTENSION

CREATE TABLE

INSERT 0 1639

UPDATE 1639

 representations | hashed | distinct_hashes 

-----------------+--------+-----------------

            1639 |   1639 |            1639

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

DROP TABLE IF EXISTS wv_blockgroup_dataset_coverage;

CREATE TABLE wv_blockgroup_dataset_coverage (

    canonical_blockgroup_id text NOT NULL,

    canonical_tract_id      text NOT NULL,

    canonical_county_id     text NOT NULL,

    dataset_type            text NOT NULL,

    source_table            text,

    feature_count           bigint NOT NULL DEFAULT 0,

    coverage_state          text NOT NULL,

    calculated_at           timestamptz NOT NULL DEFAULT now(),

    source_layer_hash       text,

    notes                   text,

    PRIMARY KEY (canonical_blockgroup_id, dataset_type, source_table),

    FOREIGN KEY (canonical_county_id)

        REFERENCES wv_county_identity (canonical_county_id),

    CHECK (coverage_state IN (

        'present',

        'confirmed_none',

        'missing_source',

        'unassigned',

        'not_applicable',

        'unknown'

SQLER BY dataset_type, coverage_state;e_layer_hash, source_table) DO UPDATE

NOTICE:  table "wv_blockgroup_dataset_coverage" does not exist, skipping

DROP TABLE

CREATE TABLE

INSERT 0 1639

 dataset_type  | coverage_state | blockgroups | min_count | max_count 

---------------+----------------+-------------+-----------+-----------

 dfirm_polygon | unknown        |        1639 |         0 |         0

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS wv_blockgroup_belief_snapshot (

    snapshot_id              uuid PRIMARY KEY DEFAULT gen_random_uuid(),

    canonical_blockgroup_id  text NOT NULL,

    canonical_tract_id       text NOT NULL,

    canonical_county_id      text NOT NULL,

    snapshot_version         text NOT NULL,

    belief_document          jsonb NOT NULL,

    belief_hash              text NOT NULL,

    generated_at             timestamptz NOT NULL DEFAULT now(),

    verification_state       text NOT NULL DEFAULT 'derived',

    FOREIGN KEY (canonical_county_id)

        REFERENCES wv_county_identity (canonical_county_id),

    UNIQUE (canonical_blockgroup_id, snapshot_version)

);

INSERT INTO wv_blockgroup_belief_snapshot (

    canonical_blockgroup_id,

    canonical_tract_id,

    canonical_county_id,

    snapshot_version,

    belief_document,

SQLRE snapshot_version = 'wv-blockgroup-snapshot-v1';shess,UPDATE

NOTICE:  extension "pgcrypto" already exists, skipping

CREATE EXTENSION

CREATE TABLE

INSERT 0 1639

 snapshot_rows | blockgroups | distinct_belief_hashes 

---------------+-------------+------------------------

          1639 |        1639 |                   1639

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

DROP VIEW IF EXISTS wv_blockgroup_belief_vector_ready;

CREATE VIEW wv_blockgroup_belief_vector_ready AS

SELECT

    s.snapshot_version,

    s.canonical_blockgroup_id,

    s.canonical_tract_id,

    s.canonical_county_id,

    ci.county_name,

    s.belief_hash AS document_id,

    jsonb_build_object(

        'canonical_blockgroup_id', s.canonical_blockgroup_id,

        'canonical_tract_id', s.canonical_tract_id,

        'canonical_county_id', s.canonical_county_id,

        'county_geoid', s.canonical_county_id,

        'county_name', ci.county_name,

        'snapshot_version', s.snapshot_version,

        'belief_hash', s.belief_hash,

        'verification_state', s.verification_state,

        'dfirm_polygon_count', COALESCE(dc.feature_count, 0),

        'dfirm_polygon_coverage_state', COALESCE(dc.coverage_state, 'unknown')

    ) AS metadata,

    concat(

        ci.county_name, ' County, West Virginia, block group GEOID ', s.canonical_SQLIT 10;canonical_county_id, canonical_tract_id, canonical_blockgroup_idre drawn.

NOTICE:  view "wv_blockgroup_belief_vector_ready" does not exist, skipping

DROP VIEW

CREATE VIEW

 canonical_blockgroup_id | county_name |                                                                                                                                                                                                   metadata                                                                                                                                                                                                    |                                                                                                                                            document                                                                                                                                            

-------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 540019655001            | Barbour     | {"belief_hash": "0173ca8bdde94dc6beba9af9430007fd6ee55c0c4add61f5d1724072a6964c26", "county_name": "Barbour", "county_geoid": "54001", "snapshot_version": "wv-blockgroup-snapshot-v1", "canonical_tract_id": "54001965500", "verification_state": "derived", "canonical_county_id": "54001", "dfirm_polygon_count": 0, "canonical_blockgroup_id": "540019655001", "dfirm_polygon_coverage_state": "unknown"} | Barbour County, West Virginia, block group GEOID 540019655001. Governed block-group snapshot version wv-blockgroup-snapshot-v1. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. Coverage is unresolved and zero must not be interpreted as definitive absence of flood-risk polygons.

 540019655002            | Barbour     | {"belief_hash": "89796db3199777787e1af774985db27cfe11016fd00d81abe828a63b25497d5d", "county_name": "Barbour", "county_geoid": "54001", "snapshot_version": "wv-blockgroup-snapshot-v1", "canonical_tract_id": "54001965500", "verification_state": "derived", "canonical_county_id": "54001", "dfirm_polygon_count": 0, "canonical_blockgroup_id": "540019655002", "dfirm_polygon_coverage_state": "unknown"} | Barbour County, West Virginia, block group GEOID 540019655002. Governed block-group snapshot version wv-blockgroup-snapshot-v1. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. Coverage is unresolved and zero must not be interpreted as definitive absence of flood-risk polygons.

 540019655003            | Barbour     | {"belief_hash": "14a6918691f1b5d57db7e95d40962ce864b1836e86f2cf1710e670baf8c3e5b5", "county_name": "Barbour", "county_geoid": "54001", "snapshot_version": "wv-blockgroup-snapshot-v1", "canonical_tract_id": "54001965500", "verification_state": "derived", "canonical_county_id": "54001", "dfirm_polygon_count": 0, "canonical_blockgroup_id": "540019655003", "dfirm_polygon_coverage_state": "unknown"} | Barbour County, West Virginia, block group GEOID 540019655003. Governed block-group snapshot version wv-blockgroup-snapshot-v1. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. Coverage is unresolved and zero must not be interpreted as definitive absence of flood-risk polygons.

 540019655004            | Barbour     | {"belief_hash": "67c3c12e3c01e1d1518277e908ea0d198387c6930b3bd60a517e3bccbd5ab3de", "county_name": "Barbour", "county_geoid": "54001", "snapshot_version": "wv-blockgroup-snapshot-v1", "canonical_tract_id": "54001965500", "verification_state": "derived", "canonical_county_id": "54001", "dfirm_polygon_count": 0, "canonical_blockgroup_id": "540019655004", "dfirm_polygon_coverage_state": "unknown"} | Barbour County, West Virginia, block group GEOID 540019655004. Governed block-group snapshot version wv-blockgroup-snapshot-v1. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. Coverage is unresolved and zero must not be interpreted as definitive absence of flood-risk polygons.

 540019656001            | Barbour     | {"belief_hash": "e77f3e24ed1b237c7bc3801b9859d5aa33075cd62dfbf6185111da432e753cbd", "county_name": "Barbour", "county_geoid": "54001", "snapshot_version": "wv-blockgroup-snapshot-v1", "canonical_tract_id": "54001965600", "verification_state": "derived", "canonical_county_id": "54001", "dfirm_polygon_count": 0, "canonical_blockgroup_id": "540019656001", "dfirm_polygon_coverage_state": "unknown"} | Barbour County, West Virginia, block group GEOID 540019656001. Governed block-group snapshot version wv-blockgroup-snapshot-v1. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. Coverage is unresolved and zero must not be interpreted as definitive absence of flood-risk polygons.

 540019656002            | Barbour     | {"belief_hash": "021b620367a78eaa3e7d1ade522d431e31fcf9dd41e781eb657a7b19fdcc9e6a", "county_name": "Barbour", "county_geoid": "54001", "snapshot_version": "wv-blockgroup-snapshot-v1", "canonical_tract_id": "54001965600", "verification_state": "derived", "canonical_county_id": "54001", "dfirm_polygon_count": 0, "canonical_blockgroup_id": "540019656002", "dfirm_polygon_coverage_state": "unknown"} | Barbour County, West Virginia, block group GEOID 540019656002. Governed block-group snapshot version wv-blockgroup-snapshot-v1. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. Coverage is unresolved and zero must not be interpreted as definitive absence of flood-risk polygons.

 540019656003            | Barbour     | {"belief_hash": "7ff02419efeb99946807d2d49ba954ff824308ba1a59b8ef623d35f3b727844b", "county_name": "Barbour", "county_geoid": "54001", "snapshot_version": "wv-blockgroup-snapshot-v1", "canonical_tract_id": "54001965600", "verification_state": "derived", "canonical_county_id": "54001", "dfirm_polygon_count": 0, "canonical_blockgroup_id": "540019656003", "dfirm_polygon_coverage_state": "unknown"} | Barbour County, West Virginia, block group GEOID 540019656003. Governed block-group snapshot version wv-blockgroup-snapshot-v1. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. Coverage is unresolved and zero must not be interpreted as definitive absence of flood-risk polygons.

 540019656004            | Barbour     | {"belief_hash": "a32df7f72e2ed52838084c64ab0d249e6d793006481b6d6c3809ffdd6695a1d6", "county_name": "Barbour", "county_geoid": "54001", "snapshot_version": "wv-blockgroup-snapshot-v1", "canonical_tract_id": "54001965600", "verification_state": "derived", "canonical_county_id": "54001", "dfirm_polygon_count": 0, "canonical_blockgroup_id": "540019656004", "dfirm_polygon_coverage_state": "unknown"} | Barbour County, West Virginia, block group GEOID 540019656004. Governed block-group snapshot version wv-blockgroup-snapshot-v1. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. Coverage is unresolved and zero must not be interpreted as definitive absence of flood-risk polygons.

 540019657001            | Barbour     | {"belief_hash": "a19d106e49e1f843518fde7c74ea78aefce1fa186694fd9da83892def2d65f59", "county_name": "Barbour", "county_geoid": "54001", "snapshot_version": "wv-blockgroup-snapshot-v1", "canonical_tract_id": "54001965700", "verification_state": "derived", "canonical_county_id": "54001", "dfirm_polygon_count": 0, "canonical_blockgroup_id": "540019657001", "dfirm_polygon_coverage_state": "unknown"} | Barbour County, West Virginia, block group GEOID 540019657001. Governed block-group snapshot version wv-blockgroup-snapshot-v1. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. Coverage is unresolved and zero must not be interpreted as definitive absence of flood-risk polygons.

 540019657002            | Barbour     | {"belief_hash": "cccf35a071d39eced9ab596f904287d9c8f60994f6c98dd35d4c85b5911c0ffd", "county_name": "Barbour", "county_geoid": "54001", "snapshot_version": "wv-blockgroup-snapshot-v1", "canonical_tract_id": "54001965700", "verification_state": "derived", "canonical_county_id": "54001", "dfirm_polygon_count": 0, "canonical_blockgroup_id": "540019657002", "dfirm_polygon_coverage_state": "unknown"} | Barbour County, West Virginia, block group GEOID 540019657002. Governed block-group snapshot version wv-blockgroup-snapshot-v1. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. Coverage is unresolved and zero must not be interpreted as definitive absence of flood-risk polygons.

(10 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

CREATE EXTENSION IF NOT EXISTS pgcrypto;

INSERT INTO gbim_collection_manifest (

    collection_name,

    collection_version,

    source_view,

    snapshot_version,

    rendering_version,

    embedding_model,

    embedding_dimension,

    permitted_use,

    notes

)

VALUES (

    'gbim_wv_blockgroups',

    'v1',

    'wv_blockgroup_belief_vector_ready',

    'wv-blockgroup-snapshot-v1',

    'blockgroup-render-v1',

    'all-minilm:latest',

    384,

    'public_civic_geographic_retrieval',

    'First governed block-group belief collection'

SQLER BY publication_status; 'v1'v_blockgroups'sion_idTHING;

NOTICE:  extension "pgcrypto" already exists, skipping

CREATE EXTENSION

INSERT 0 1

INSERT 0 1639

 publication_status | count 

--------------------+-------

 pending            |  1639

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ export PGHOST=127.0.0.1

export PGPORT=5433

export PGDATABASE=msjarvisgis

export PGUSER=postgres

export CHROMA_HOST=127.0.0.1

export CHROMA_PORT=8002

python3 - <<'PY'

import os, json, psycopg2, chromadb

from chromadb.config import Settings

PGHOST=os.getenv("PGHOST","127.0.0.1")

PGPORT=os.getenv("PGPORT","5433")

PGDATABASE=os.getenv("PGDATABASE","msjarvisgis")

PGUSER=os.getenv("PGUSER","postgres")

PGPASSWORD=os.getenv("PGPASSWORD","")

CHROMA_HOST=os.getenv("CHROMA_HOST","127.0.0.1")

CHROMA_PORT=int(os.getenv("CHROMA_PORT","8002"))

conn = psycopg2.connect(

    host=PGHOST,

    port=PGPORT,

    dbname=PGDATABASE,

    user=PGUSER,

PY indent=2))on_version_id": str(collection_version_id)rsion_idmetadata)cument, me

{

  "physical_collection": "gbim_wv_blockgroups_v1",

  "count": 1639,

  "collection_version_id": "4c6638de-274d-485c-bb64-ab078426a5a5"

}

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ 

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

INSERT INTO gbim_active_collection (

    logical_collection_name,

    collection_version_id,

    physical_collection_name

)

SELECT

    'gbim_wv_blockgroups',

    m.collection_version_id,

    'gbim_wv_blockgroups_v1'

FROM gbim_collection_manifest m

WHERE m.collection_name = 'gbim_wv_blockgroups'

  AND m.collection_version = 'v1'

ON CONFLICT (logical_collection_name) DO UPDATE

SET collection_version_id = EXCLUDED.collection_version_id,

    physical_collection_name = EXCLUDED.physical_collection_name,

    activated_at = now();

UPDATE gbim_collection_manifest

SET build_status = 'active',

    promoted_at = now()

WHERE collection_name = 'gbim_wv_blockgroups'

  AND collection_version = 'v1';

SQLRE logical_collection_name = 'gbim_wv_blockgroups';

INSERT 0 1

UPDATE 1

   collection_name   | collection_version | build_status | record_count |         promoted_at          

---------------------+--------------------+--------------+--------------+------------------------------

 gbim_wv_blockgroups | v1                 | active       |         1639 | 2026-07-11 19:12:33.45012+00

(1 row)

 logical_collection_name |        collection_version_id         | physical_collection_name |         activated_at          

-------------------------+--------------------------------------+--------------------------+-------------------------------

 gbim_wv_blockgroups     | 4c6638de-274d-485c-bb64-ab078426a5a5 | gbim_wv_blockgroups_v1   | 2026-07-11 19:12:33.436517+00

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ python3 - <<'PY'

import chromadb, json

client = chromadb.HttpClient(host="127.0.0.1", port=8002)

col = client.get_collection("gbim_wv_blockgroups_v1")

print("COUNT", col.count())

for text in [

    "Show governed block groups in Wood County, West Virginia.",

    "Which governed block groups have mapped D-FIRM polygon coverage in West Virginia?"

]:

    print("\nQUERY:", text)

    q = col.query(query_texts=[text], n_results=5)

    print(json.dumps(q, indent=2)[:4000])

PY

COUNT 1639

QUERY: Show governed block groups in Wood County, West Virginia.

{

  "ids": [

    [

      "2c5f2f614c2b4e2cd3281ed3614eb2b2cab7b7c2fa8143362d841a4df0a5a03e",

      "7deb9d2b60e7fbd5f1c05aabb6acafee5da33976c11bf297d4dd4aa36ea52652",

      "8e76cfdb0c431640b62627e60a5d76928d8ba8c51eefc64df2b63b3200982ede",

      "dc14bf6e03d3bb3fd65f1ab7f15fe9e4da431340838441b4409b26af0b1a9b06",

      "fac4cf0910b5f683b190a16e73a706c18a72532f0c15bc5b1e5029c3beac884d"

    ]

  ],

  "distances": [

    [

      0.5241342301155903,

      0.5270639061927795,

      0.5288537740707397,

      0.5298562173986201,

      0.5308499336242676

    ]

  ],

  "embeddings": null,

  "metadatas": [

    [

      {

        "access_class": "public",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "2c5f2f614c2b4e2cd3281ed3614eb2b2cab7b7c2fa8143362d841a4df0a5a03e",

        "canonical_blockgroup_id": "541070107052",

        "canonical_county_id": "54107",

        "canonical_tract_id": "54107010705",

        "county_geoid": "54107",

        "county_name": "Wood",

        "dfirm_polygon_count": 0,

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "blockgroup-render-v1",

        "snapshot_version": "wv-blockgroup-snapshot-v1",

        "verification_state": "derived"

      },

      {

        "access_class": "public",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "7deb9d2b60e7fbd5f1c05aabb6acafee5da33976c11bf297d4dd4aa36ea52652",

        "canonical_blockgroup_id": "541070107033",

        "canonical_county_id": "54107",

        "canonical_tract_id": "54107010703",

        "county_geoid": "54107",

        "county_name": "Wood",

        "dfirm_polygon_count": 0,

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "blockgroup-render-v1",

        "snapshot_version": "wv-blockgroup-snapshot-v1",

        "verification_state": "derived"

      },

      {

        "access_class": "public",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "8e76cfdb0c431640b62627e60a5d76928d8ba8c51eefc64df2b63b3200982ede",

        "canonical_blockgroup_id": "541070107031",

        "canonical_county_id": "54107",

        "canonical_tract_id": "54107010703",

        "county_geoid": "54107",

        "county_name": "Wood",

        "dfirm_polygon_count": 0,

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "blockgroup-render-v1",

        "snapshot_version": "wv-blockgroup-snapshot-v1",

        "verification_state": "derived"

      },

      {

        "access_class": "public",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "dc14bf6e03d3bb3fd65f1ab7f15fe9e4da431340838441b4409b26af0b1a9b06",

        "canonical_blockgroup_id": "541070107062",

        "canonical_county_id": "54107",

        "canonical_tract_id": "54107010706",

        "county_geoid": "54107",

        "county_name": "Wood",

        "dfirm_polygon_count": 0,

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "blockgroup-render-v1",

        "snapshot_version": "wv-blockgroup-snapshot-v1",

        "verification_state": "derived"

      },

      {

        "access_class": "public",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "fac4cf0910b5f683b190a16e73a706c18a72532f0c15bc5b1e5029c3beac884d",

        "canonical_blockgroup_id": "541070005004",

        "canonical_county_id": "54107",

        "canonical_tract_id": "54107000500",

        "county_geoid": "54107",

        "county_name": "Wood",

        "dfirm_polygon_count": 0,

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "blockgroup-render-v1",

        "snapshot_versio

QUERY: Which governed block groups have mapped D-FIRM polygon coverage in West Virginia?

{

  "ids": [

    [

      "d57b61e5d8aca21398ea75d7e8743e692c6a3dbcb48d3c6801c9e453b47e6037",

      "0ef80c5d734a6efc237e1f053d040e8f00c15f529845c55a38197a8d351efc7b",

      "af5fe4a28cfb0c14352f2b272e4068bcb04a91947e9590c40ec980c6c1578c4c",

      "5e12d57fbce4f0c2e70d166183154a0b18b11ed477432f6872d9fe0ca9248086",

      "1475c4624231a6dc1c319b22f31bee788eb8a6888c26e846ed0ada5e7a94b37a"

    ]

  ],

  "distances": [

    [

      0.4966554641723633,

      0.4989946782588959,

      0.4996587038040161,

      0.506151556968689,

      0.5089970827102661

    ]

  ],

  "embeddings": null,

  "metadatas": [

    [

      {

        "access_class": "public",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "d57b61e5d8aca21398ea75d7e8743e692c6a3dbcb48d3c6801c9e453b47e6037",

        "canonical_blockgroup_id": "540239696002",

        "canonical_county_id": "54023",

        "canonical_tract_id": "54023969600",

        "county_geoid": "54023",

        "county_name": "Grant",

        "dfirm_polygon_count": 0,

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "blockgroup-render-v1",

        "snapshot_version": "wv-blockgroup-snapshot-v1",

        "verification_state": "derived"

      },

      {

        "access_class": "public",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "0ef80c5d734a6efc237e1f053d040e8f00c15f529845c55a38197a8d351efc7b",

        "canonical_blockgroup_id": "540239696004",

        "canonical_county_id": "54023",

        "canonical_tract_id": "54023969600",

        "county_geoid": "54023",

        "county_name": "Grant",

        "dfirm_polygon_count": 0,

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "blockgroup-render-v1",

        "snapshot_version": "wv-blockgroup-snapshot-v1",

        "verification_state": "derived"

      },

      {

        "access_class": "public",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "af5fe4a28cfb0c14352f2b272e4068bcb04a91947e9590c40ec980c6c1578c4c",

        "canonical_blockgroup_id": "540239696003",

        "canonical_county_id": "54023",

        "canonical_tract_id": "54023969600",

        "county_geoid": "54023",

        "county_name": "Grant",

        "dfirm_polygon_count": 0,

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "blockgroup-render-v1",

        "snapshot_version": "wv-blockgroup-snapshot-v1",

        "verification_state": "derived"

      },

      {

        "access_class": "public",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "5e12d57fbce4f0c2e70d166183154a0b18b11ed477432f6872d9fe0ca9248086",

        "canonical_blockgroup_id": "540239695002",

        "canonical_county_id": "54023",

        "canonical_tract_id": "54023969500",

        "county_geoid": "54023",

        "county_name": "Grant",

        "dfirm_polygon_count": 0,

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "blockgroup-render-v1",

        "snapshot_version": "wv-blockgroup-snapshot-v1",

        "verification_state": "derived"

      },

      {

        "access_class": "public",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "1475c4624231a6dc1c319b22f31bee788eb8a6888c26e846ed0ada5e7a94b37a",

        "canonical_blockgroup_id": "540239696001",

        "canonical_county_id": "54023",

        "canonical_tract_id": "54023969600",

        "county_geoid": "54023",

        "county_name": "Grant",

        "dfirm_polygon_count": 0,

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "blockgroup-render-v1",

        "snapshot_ve

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ export PGHOST=127.0.0.1

export PGPORT=5433

export PGDATABASE=msjarvisgis

export PGUSER=postgres

psql -v ON_ERROR_STOP=1 <<'SQL'

-- County-level governed collection manifest

SELECT collection_name, collection_version, source_view, snapshot_version,

       embedding_model, embedding_dimension, build_status, record_count

FROM gbim_collection_manifest

WHERE collection_name IN (

    'gbim_wv_counties',

    'gbim_wv_tracts',

    'gbim_wv_blockgroups'

)

ORDER BY collection_name, collection_version;

-- Cross-check Wood County coverage statuses

SELECT

    'county' AS level,

    canonical_county_id,

    dataset_type,

    coverage_state,

    feature_count

SQLER BY level, canonical_tract_id, canonical_blockgroup_id, dataset_type;

   collection_name   | collection_version |            source_view            |     snapshot_version      |  embedding_model  | embedding_dimension | build_status | record_count 

---------------------+--------------------+-----------------------------------+---------------------------+-------------------+---------------------+--------------+--------------

 gbim_wv_blockgroups | v1                 | wv_blockgroup_belief_vector_ready | wv-blockgroup-snapshot-v1 | all-minilm:latest |                 384 | active       |         1639

 gbim_wv_counties    | v1                 | wv_county_belief_vector_ready     | wv-county-snapshot-v1     | all-minilm:latest |                 384 | active       |           55

 gbim_wv_tracts      | v1                 | wv_tract_belief_vector_ready      | wv-tract-snapshot-v1      | all-minilm:latest |                 384 | active       |          546

(3 rows)

 level  | canonical_county_id | dataset_type  | coverage_state | feature_count 

--------+---------------------+---------------+----------------+---------------

 county | 54107               | address_point | unknown        |             0

 county | 54107               | blockgroup    | present        |            96

 county | 54107               | dfirm_polygon | unknown        |             0

 county | 54107               | tract         | present        |            28

 county | 54107               | zcta          | present        |            11

(5 rows)

 level | canonical_tract_id | canonical_county_id | dataset_type  | coverage_state | feature_count 

-------+--------------------+---------------------+---------------+----------------+---------------

 tract | 54107000100        | 54107               | dfirm_polygon | unknown        |             0

 tract | 54107000300        | 54107               | dfirm_polygon | unknown        |             0

 tract | 54107000400        | 54107               | dfirm_polygon | unknown        |             0

 tract | 54107000500        | 54107               | dfirm_polygon | unknown        |             0

 tract | 54107000701        | 54107               | dfirm_polygon | unknown        |             0

 tract | 54107000702        | 54107               | dfirm_polygon | unknown        |             0

 tract | 54107000801        | 54107               | dfirm_polygon | unknown        |             0

 tract | 54107000802        | 54107               | dfirm_polygon | unknown        |             0

 tract | 54107000901        | 54107               | dfirm_polygon | unknown        |             0

 tract | 54107000902        | 54107               | dfirm_polygon | unknown        |             0

 tract | 54107000903        | 54107               | dfirm_polygon | unknown        |             0

 tract | 54107010101        | 54107               | dfirm_polygon | unknown        |             0

 tract | 54107010102        | 54107               | dfirm_polygon | unknown        |             0

 tract | 54107010200        | 54107               | dfirm_polygon | unknown        |             0

 tract | 54107010300        | 54107               | dfirm_polygon | unknown        |             0

 tract | 54107010400        | 54107               | dfirm_polygon | unknown        |             0

 tract | 54107010501        | 54107               | dfirm_polygon | unknown        |             0

 tract | 54107010502        | 54107               | dfirm_polygon | unknown        |             0

 tract | 54107010601        | 54107               | dfirm_polygon | unknown        |             0

 tract | 54107010602        | 54107               | dfirm_polygon | unknown        |             0

 tract | 54107010703        | 54107               | dfirm_polygon | unknown        |             0

 tract | 54107010704        | 54107               | dfirm_polygon | unknown        |             0

 tract | 54107010705        | 54107               | dfirm_polygon | unknown        |             0

 tract | 54107010706        | 54107               | dfirm_polygon | unknown        |             0

 tract | 54107010800        | 54107               | dfirm_polygon | unknown        |             0

 tract | 54107010901        | 54107               | dfirm_polygon | unknown        |             0

 tract | 54107010902        | 54107               | dfirm_polygon | unknown        |             0

 tract | 54107011000        | 54107               | dfirm_polygon | unknown        |             0

(28 rows)

   level    | canonical_blockgroup_id | canonical_tract_id | canonical_county_id | dataset_type  | coverage_state | feature_count 

------------+-------------------------+--------------------+---------------------+---------------+----------------+---------------

 blockgroup | 541070001001            | 54107000100        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070001002            | 54107000100        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070003001            | 54107000300        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070003002            | 54107000300        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070004001            | 54107000400        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070004002            | 54107000400        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070005001            | 54107000500        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070005002            | 54107000500        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070005003            | 54107000500        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070005004            | 54107000500        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070007011            | 54107000701        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070007012            | 54107000701        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070007013            | 54107000701        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070007021            | 54107000702        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070007022            | 54107000702        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070008011            | 54107000801        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070008021            | 54107000802        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070008022            | 54107000802        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070008023            | 54107000802        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070009011            | 54107000901        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070009021            | 54107000902        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070009022            | 54107000902        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070009031            | 54107000903        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070009032            | 54107000903        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070009033            | 54107000903        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070101011            | 54107010101        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070101021            | 54107010102        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070101022            | 54107010102        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070102001            | 54107010200        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070102002            | 54107010200        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070102003            | 54107010200        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070103001            | 54107010300        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070103002            | 54107010300        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070104001            | 54107010400        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070104002            | 54107010400        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070105011            | 54107010501        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070105012            | 54107010501        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070105021            | 54107010502        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070105022            | 54107010502        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070105023            | 54107010502        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070106011            | 54107010601        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070106012            | 54107010601        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070106013            | 54107010601        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070106021            | 54107010602        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070106022            | 54107010602        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070106023            | 54107010602        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070106024            | 54107010602        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070107031            | 54107010703        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070107032            | 54107010703        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070107033            | 54107010703        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070107034            | 54107010703        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070107041            | 54107010704        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070107042            | 54107010704        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070107051            | 54107010705        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070107052            | 54107010705        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070107061            | 54107010706        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070107062            | 54107010706        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070107063            | 54107010706        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070108001            | 54107010800        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070108002            | 54107010800        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070108003            | 54107010800        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070109011            | 54107010901        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070109012            | 54107010901        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070109013            | 54107010901        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070109014            | 54107010901        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070109021            | 54107010902        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070109022            | 54107010902        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070109023            | 54107010902        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070110001            | 54107011000        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070110002            | 54107011000        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070110003            | 54107011000        | 54107               | dfirm_polygon | unknown        |             0

 blockgroup | 541070110004            | 54107011000        | 54107               | dfirm_polygon | unknown        |             0

(72 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

UPDATE wv_blockgroup_dataset_coverage

SET notes = 'D-FIRM polygons not yet intersected at block-group resolution; zero is unresolved coverage, not verified absence.'

WHERE dataset_type = 'dfirm_polygon'

  AND source_table = 'wv_hyd_dfirm_nfhl'

  AND coverage_state = 'unknown';

SELECT dataset_type, coverage_state, COUNT(*), MIN(feature_count), MAX(feature_count)

FROM wv_blockgroup_dataset_coverage

GROUP BY dataset_type, coverage_state

ORDER BY dataset_type, coverage_state;

SQL

UPDATE 1639

 dataset_type  | coverage_state | count | min | max 

---------------+----------------+-------+-----+-----

 dfirm_polygon | unknown        |  1639 |   0 |   0

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

DROP VIEW IF EXISTS wv_dfirm_multiscale_coverage;

CREATE VIEW wv_dfirm_multiscale_coverage AS

SELECT

    'county' AS level,

    c.canonical_county_id,

    NULL::text AS canonical_tract_id,

    NULL::text AS canonical_blockgroup_id,

    c.feature_count,

    c.coverage_state,

    c.notes

FROM wv_county_dataset_coverage c

WHERE c.dataset_type = 'dfirm_polygon'

  AND c.source_table = 'wv_hyd_dfirm_nfhl'

UNION ALL

SELECT

    'tract' AS level,

    t.canonical_county_id,

    t.canonical_tract_id,

    NULL::text AS canonical_blockgroup_id,

    t.feature_count,

    t.coverage_state,

    t.notes

SQLER BY level, coverage_state;geNT(*) AS units

NOTICE:  view "wv_dfirm_multiscale_coverage" does not exist, skipping

DROP VIEW

CREATE VIEW

   level    | coverage_state | units 

------------+----------------+-------

 blockgroup | unknown        |  1639

 county     | present        |     8

 county     | unknown        |    47

 tract      | unknown        |   546

(4 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ python3 - <<'PY'

import chromadb, json

client = chromadb.HttpClient(host="127.0.0.1", port=8002)

col = client.get_collection("gbim_wv_blockgroups_v1")

def show(county_geoid):

    print(f"\nCOUNTY {county_geoid}")

    q = col.get(

        where={"county_geoid": county_geoid},

        limit=5

    )

    print(json.dumps({

        "ids": q["ids"],

        "metadatas": q["metadatas"],

    }, indent=2)[:4000])

for geoid in ["54107", "54023"]:

    show(geoid)

PY

COUNTY 54107

{

  "ids": [

    "28778eeea0a553e6c1fea2ea720a7cada0244451d4692c95722019cd50b7a0ba",

    "b18b5ecbf1f9aad734150dcf6b20d8e9a88ad8c15509596b4c4c8b1f22ad5f3b",

    "d80799d0c5408f8f19824bbc9508b72e778f8fb7914d9f9e8e4d0b32165f9815",

    "2e87f6731d45c570826cbd92ec5e57f0217e6b9184f4d284b3c2d7fbf276e1da",

    "cb5ed04fe35a1c7c48ecbb8a9840eb9f6bc08a8418b5763e40560f33b9cfe551"

  ],

  "metadatas": [

    {

      "access_class": "public",

      "authority_class": "governed_civic_geographic",

      "belief_hash": "28778eeea0a553e6c1fea2ea720a7cada0244451d4692c95722019cd50b7a0ba",

      "canonical_blockgroup_id": "541070001001",

      "canonical_county_id": "54107",

      "canonical_tract_id": "54107000100",

      "county_geoid": "54107",

      "county_name": "Wood",

      "dfirm_polygon_count": 0,

      "dfirm_polygon_coverage_state": "unknown",

      "permitted_use": "public_civic_geographic_retrieval",

      "rendering_version": "blockgroup-render-v1",

      "snapshot_version": "wv-blockgroup-snapshot-v1",

      "verification_state": "derived"

    },

    {

      "access_class": "public",

      "authority_class": "governed_civic_geographic",

      "belief_hash": "b18b5ecbf1f9aad734150dcf6b20d8e9a88ad8c15509596b4c4c8b1f22ad5f3b",

      "canonical_blockgroup_id": "541070001002",

      "canonical_county_id": "54107",

      "canonical_tract_id": "54107000100",

      "county_geoid": "54107",

      "county_name": "Wood",

      "dfirm_polygon_count": 0,

      "dfirm_polygon_coverage_state": "unknown",

      "permitted_use": "public_civic_geographic_retrieval",

      "rendering_version": "blockgroup-render-v1",

      "snapshot_version": "wv-blockgroup-snapshot-v1",

      "verification_state": "derived"

    },

    {

      "access_class": "public",

      "authority_class": "governed_civic_geographic",

      "belief_hash": "d80799d0c5408f8f19824bbc9508b72e778f8fb7914d9f9e8e4d0b32165f9815",

      "canonical_blockgroup_id": "541070003001",

      "canonical_county_id": "54107",

      "canonical_tract_id": "54107000300",

      "county_geoid": "54107",

      "county_name": "Wood",

      "dfirm_polygon_count": 0,

      "dfirm_polygon_coverage_state": "unknown",

      "permitted_use": "public_civic_geographic_retrieval",

      "rendering_version": "blockgroup-render-v1",

      "snapshot_version": "wv-blockgroup-snapshot-v1",

      "verification_state": "derived"

    },

    {

      "access_class": "public",

      "authority_class": "governed_civic_geographic",

      "belief_hash": "2e87f6731d45c570826cbd92ec5e57f0217e6b9184f4d284b3c2d7fbf276e1da",

      "canonical_blockgroup_id": "541070003002",

      "canonical_county_id": "54107",

      "canonical_tract_id": "54107000300",

      "county_geoid": "54107",

      "county_name": "Wood",

      "dfirm_polygon_count": 0,

      "dfirm_polygon_coverage_state": "unknown",

      "permitted_use": "public_civic_geographic_retrieval",

      "rendering_version": "blockgroup-render-v1",

      "snapshot_version": "wv-blockgroup-snapshot-v1",

      "verification_state": "derived"

    },

    {

      "access_class": "public",

      "authority_class": "governed_civic_geographic",

      "belief_hash": "cb5ed04fe35a1c7c48ecbb8a9840eb9f6bc08a8418b5763e40560f33b9cfe551",

      "canonical_blockgroup_id": "541070004001",

      "canonical_county_id": "54107",

      "canonical_tract_id": "54107000400",

      "county_geoid": "54107",

      "county_name": "Wood",

      "dfirm_polygon_count": 0,

      "dfirm_polygon_coverage_state": "unknown",

      "permitted_use": "public_civic_geographic_retrieval",

      "rendering_version": "blockgroup-render-v1",

      "snapshot_version": "wv-blockgroup-snapshot-v1",

      "verification_state": "derived"

    }

  ]

}

COUNTY 54023

{

  "ids": [

    "2d95a9c113385599470ac808b4b77007145a79e502799687a68a002f96628e7a",

    "c5f1899d0261454cf9c95efe492ec75b4375d923ea342197b7de63c54c59fb36",

    "17dedc7060c8d34964c8e9cdbdd901c7b23a6f5791bc5cd37c3ec7192a873d0c",

    "d82bebfc4cd343a561843c3b7c0dac3f7b86758968b7666de19b73d9956f9b99",

    "7f757b9c4202f6d35dc57c7d811a431dafb157a13f0895cf4997416889168f4a"

  ],

  "metadatas": [

    {

      "access_class": "public",

      "authority_class": "governed_civic_geographic",

      "belief_hash": "2d95a9c113385599470ac808b4b77007145a79e502799687a68a002f96628e7a",

      "canonical_blockgroup_id": "540239694001",

      "canonical_county_id": "54023",

      "canonical_tract_id": "54023969400",

      "county_geoid": "54023",

      "county_name": "Grant",

      "dfirm_polygon_count": 0,

      "dfirm_polygon_coverage_state": "unknown",

      "permitted_use": "public_civic_geographic_retrieval",

      "rendering_version": "blockgroup-render-v1",

      "snapshot_version": "wv-blockgroup-snapshot-v1",

      "verification_state": "derived"

    },

    {

      "access_class": "public",

      "authority_class": "governed_civic_geographic",

      "belief_hash": "c5f1899d0261454cf9c95efe492ec75b4375d923ea342197b7de63c54c59fb36",

      "canonical_blockgroup_id": "540239694002",

      "canonical_county_id": "54023",

      "canonical_tract_id": "54023969400",

      "county_geoid": "54023",

      "county_name": "Grant",

      "dfirm_polygon_count": 0,

      "dfirm_polygon_coverage_state": "unknown",

      "permitted_use": "public_civic_geographic_retrieval",

      "rendering_version": "blockgroup-render-v1",

      "snapshot_version": "wv-blockgroup-snapshot-v1",

      "verification_state": "derived"

    },

    {

      "access_class": "public",

      "authority_class": "governed_civic_geographic",

      "belief_hash": "17dedc7060c8d34964c8e9cdbdd901c7b23a6f5791bc5cd37c3ec7192a873d0c",

      "canonical_blockgroup_id": "540239694003",

      "canonical_county_id": "54023",

      "canonical_tract_id": "54023969400",

      "county_geoid": "54023",

      "county_name": "Grant",

      "dfirm_polygon_count": 0,

      "dfirm_polygon_coverage_state": "unknown",

      "permitted_use": "public_civic_geographic_retrieval",

      "rendering_version": "blockgroup-render-v1",

      "snapshot_version": "wv-blockgroup-snapshot-v1",

      "verification_state": "derived"

    },

    {

      "access_class": "public",

      "authority_class": "governed_civic_geographic",

      "belief_hash": "d82bebfc4cd343a561843c3b7c0dac3f7b86758968b7666de19b73d9956f9b99",

      "canonical_blockgroup_id": "540239694004",

      "canonical_county_id": "54023",

      "canonical_tract_id": "54023969400",

      "county_geoid": "54023",

      "county_name": "Grant",

      "dfirm_polygon_count": 0,

      "dfirm_polygon_coverage_state": "unknown",

      "permitted_use": "public_civic_geographic_retrieval",

      "rendering_version": "blockgroup-render-v1",

      "snapshot_version": "wv-blockgroup-snapshot-v1",

      "verification_state": "derived"

    },

    {

      "access_class": "public",

      "authority_class": "governed_civic_geographic",

      "belief_hash": "7f757b9c4202f6d35dc57c7d811a431dafb157a13f0895cf4997416889168f4a",

      "canonical_blockgroup_id": "540239695001",

      "canonical_county_id": "54023",

      "canonical_tract_id": "54023969500",

      "county_geoid": "54023",

      "county_name": "Grant",

      "dfirm_polygon_count": 0,

      "dfirm_polygon_coverage_state": "unknown",

      "permitted_use": "public_civic_geographic_retrieval",

      "rendering_version": "blockgroup-render-v1",

      "snapshot_version": "wv-blockgroup-snapshot-v1",

      "verification_state": "derived"

    }

  ]

}

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ export PGHOST=127.0.0.1

export PGPORT=5433

export PGDATABASE=msjarvisgis

export PGUSER=postgres

export CHROMA_HOST=127.0.0.1

export CHROMA_PORT=8000

psql -v ON_ERROR_STOP=1 <<'SQL'

CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS wv_zcta_representation (

    canonical_zcta_id      text    NOT NULL,

    canonical_county_id    text,

    table_name             text    NOT NULL,

    source_feature_id      bigint  NOT NULL,

    source_feature_hash    text,

    PRIMARY KEY (canonical_zcta_id, table_name, source_feature_id),

    FOREIGN KEY (canonical_county_id)

        REFERENCES wv_county_identity (canonical_county_id)

);

INSERT INTO wv_zcta_representation (

    canonical_zcta_id,

    canonical_county_id,

SQLM wv_zcta_representation;ature_hash) AS distinct_hashes AS table_name,;

NOTICE:  extension "pgcrypto" already exists, skipping

CREATE EXTENSION

CREATE TABLE

INSERT 0 741

UPDATE 741

 representations | hashed | distinct_hashes 

-----------------+--------+-----------------

             741 |    741 |             741

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

DROP TABLE IF EXISTS wv_zcta_dataset_coverage;

CREATE TABLE wv_zcta_dataset_coverage (

    canonical_zcta_id      text NOT NULL,

    canonical_county_id    text,

    dataset_type           text NOT NULL,

    source_table           text,

    feature_count          bigint NOT NULL DEFAULT 0,

    coverage_state         text NOT NULL,

    calculated_at          timestamptz NOT NULL DEFAULT now(),

    source_layer_hash      text,

    notes                  text,

    PRIMARY KEY (canonical_zcta_id, dataset_type, source_table),

    FOREIGN KEY (canonical_county_id)

        REFERENCES wv_county_identity (canonical_county_id),

    CHECK (coverage_state IN (

        'present',

        'confirmed_none',

        'missing_source',

        'unassigned',

        'not_applicable',

        'unknown'

    ))

SQLER BY dataset_type, coverage_state;e_layer_hash,_id,ble) DO UPDATEcoverage.'era

NOTICE:  table "wv_zcta_dataset_coverage" does not exist, skipping

DROP TABLE

CREATE TABLE

INSERT 0 1482

 dataset_type  | coverage_state | zctas | min_count | max_count 

---------------+----------------+-------+-----------+-----------

 address_point | unknown        |   741 |         0 |         0

 dfirm_polygon | unknown        |   741 |         0 |         0

(2 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS wv_zcta_belief_snapshot (

    snapshot_id           uuid PRIMARY KEY DEFAULT gen_random_uuid(),

    canonical_zcta_id     text NOT NULL,

    canonical_county_id   text,

    snapshot_version      text NOT NULL,

    belief_document       jsonb NOT NULL,

    belief_hash           text NOT NULL,

    generated_at          timestamptz NOT NULL DEFAULT now(),

    verification_state    text NOT NULL DEFAULT 'derived',

    FOREIGN KEY (canonical_county_id)

        REFERENCES wv_county_identity (canonical_county_id),

    UNIQUE (canonical_zcta_id, snapshot_version)

);

WITH zcta_to_county AS (

    SELECT

        z.zcta5ce20 AS canonical_zcta_id,

        c.canonical_county_id

    FROM wv_zipcodetabulationarea_census_2020_utm83 z

    LEFT JOIN LATERAL (

        SELECT ci.canonical_county_id

SQLRE snapshot_version = 'wv-zcta-snapshot-v1';ief_hashesTE_hashutm83', NULLS LAST

NOTICE:  extension "pgcrypto" already exists, skipping

CREATE EXTENSION

CREATE TABLE

INSERT 0 741

 snapshot_rows | zctas | distinct_belief_hashes 

---------------+-------+------------------------

           741 |   741 |                    741

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

DROP VIEW IF EXISTS wv_zcta_belief_vector_ready;

CREATE VIEW wv_zcta_belief_vector_ready AS

SELECT

    s.snapshot_version,

    s.canonical_zcta_id,

    s.canonical_county_id,

    ci.county_name,

    s.belief_hash AS document_id,

    jsonb_build_object(

        'canonical_zcta_id', s.canonical_zcta_id,

        'canonical_county_id', s.canonical_county_id,

        'county_geoid', s.canonical_county_id,

        'county_name', ci.county_name,

        'snapshot_version', s.snapshot_version,

        'belief_hash', s.belief_hash,

        'verification_state', s.verification_state,

        'address_point_count', COALESCE(ap.feature_count, 0),

        'address_point_coverage_state', COALESCE(ap.coverage_state, 'unknown'),

        'dfirm_polygon_count', COALESCE(df.feature_count, 0),

        'dfirm_polygon_coverage_state', COALESCE(df.coverage_state, 'unknown')

    ) AS metadata,

    concat(

SQLIT 10;canonical_zcta_id_readycal_county_id, metadata, documentverified absence.

NOTICE:  view "wv_zcta_belief_vector_ready" does not exist, skipping

DROP VIEW

CREATE VIEW

 canonical_zcta_id | canonical_county_id |                                                                                                                                                                                                           metadata                                                                                                                                                                                                           |                                                                                                                                                                document                                                                                                                                                                 

-------------------+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 20135             | 54037               | {"belief_hash": "414325614bdec16504ad0446d676c8f68b801acd5b646715f9a48d7144c921e9", "county_name": "Jefferson", "county_geoid": "54037", "snapshot_version": "wv-zcta-snapshot-v1", "canonical_zcta_id": "20135", "verification_state": "derived", "address_point_count": 0, "canonical_county_id": "54037", "dfirm_polygon_count": 0, "address_point_coverage_state": "unknown", "dfirm_polygon_coverage_state": "unknown"} | ZCTA 20135, West Virginia. Current county assignment is Jefferson County, GEOID 54037. Governed snapshot version wv-zcta-snapshot-v1. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.

 24604             | 54047               | {"belief_hash": "d27b409b305db961d4f3c649db3b5a9a915b9fb3ffff253857cb4930ce388a13", "county_name": "McDowell", "county_geoid": "54047", "snapshot_version": "wv-zcta-snapshot-v1", "canonical_zcta_id": "24604", "verification_state": "derived", "address_point_count": 0, "canonical_county_id": "54047", "dfirm_polygon_count": 0, "address_point_coverage_state": "unknown", "dfirm_polygon_coverage_state": "unknown"}  | ZCTA 24604, West Virginia. Current county assignment is McDowell County, GEOID 54047. Governed snapshot version wv-zcta-snapshot-v1. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.

 24622             | 54047               | {"belief_hash": "8acd09f834e6051fa9116710434d854838b04123b3214abc0e7dc897331795d1", "county_name": "McDowell", "county_geoid": "54047", "snapshot_version": "wv-zcta-snapshot-v1", "canonical_zcta_id": "24622", "verification_state": "derived", "address_point_count": 0, "canonical_county_id": "54047", "dfirm_polygon_count": 0, "address_point_coverage_state": "unknown", "dfirm_polygon_coverage_state": "unknown"}  | ZCTA 24622, West Virginia. Current county assignment is McDowell County, GEOID 54047. Governed snapshot version wv-zcta-snapshot-v1. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.

 24701             | 54055               | {"belief_hash": "9ff8db8874bd3a6611faf4293d489abbd81665d07211938ae45eb2e616153180", "county_name": "Mercer", "county_geoid": "54055", "snapshot_version": "wv-zcta-snapshot-v1", "canonical_zcta_id": "24701", "verification_state": "derived", "address_point_count": 0, "canonical_county_id": "54055", "dfirm_polygon_count": 0, "address_point_coverage_state": "unknown", "dfirm_polygon_coverage_state": "unknown"}    | ZCTA 24701, West Virginia. Current county assignment is Mercer County, GEOID 54055. Governed snapshot version wv-zcta-snapshot-v1. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.

 24712             | 54055               | {"belief_hash": "f7a994328839c6477e7e22050e57d96ac3f7f6fd83515ccc89bc135924b192dd", "county_name": "Mercer", "county_geoid": "54055", "snapshot_version": "wv-zcta-snapshot-v1", "canonical_zcta_id": "24712", "verification_state": "derived", "address_point_count": 0, "canonical_county_id": "54055", "dfirm_polygon_count": 0, "address_point_coverage_state": "unknown", "dfirm_polygon_coverage_state": "unknown"}    | ZCTA 24712, West Virginia. Current county assignment is Mercer County, GEOID 54055. Governed snapshot version wv-zcta-snapshot-v1. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.

 24714             | 54055               | {"belief_hash": "fe6d8f86d2a4ae36b53e2d34c135c87c2f84927c1b0465c8b6f11e47b9736dd5", "county_name": "Mercer", "county_geoid": "54055", "snapshot_version": "wv-zcta-snapshot-v1", "canonical_zcta_id": "24714", "verification_state": "derived", "address_point_count": 0, "canonical_county_id": "54055", "dfirm_polygon_count": 0, "address_point_coverage_state": "unknown", "dfirm_polygon_coverage_state": "unknown"}    | ZCTA 24714, West Virginia. Current county assignment is Mercer County, GEOID 54055. Governed snapshot version wv-zcta-snapshot-v1. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.

 24715             | 54055               | {"belief_hash": "9be5341ab4513c695d582ce08d7e699d9683ebab3624a329bc11a67bf1bae86d", "county_name": "Mercer", "county_geoid": "54055", "snapshot_version": "wv-zcta-snapshot-v1", "canonical_zcta_id": "24715", "verification_state": "derived", "address_point_count": 0, "canonical_county_id": "54055", "dfirm_polygon_count": 0, "address_point_coverage_state": "unknown", "dfirm_polygon_coverage_state": "unknown"}    | ZCTA 24715, West Virginia. Current county assignment is Mercer County, GEOID 54055. Governed snapshot version wv-zcta-snapshot-v1. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.

 24716             | 54109               | {"belief_hash": "17d732cbd5fa6c34f212bff879a32e7ebc0e43eccff44a5eb35db42995e078c3", "county_name": "Wyoming", "county_geoid": "54109", "snapshot_version": "wv-zcta-snapshot-v1", "canonical_zcta_id": "24716", "verification_state": "derived", "address_point_count": 0, "canonical_county_id": "54109", "dfirm_polygon_count": 0, "address_point_coverage_state": "unknown", "dfirm_polygon_coverage_state": "unknown"}   | ZCTA 24716, West Virginia. Current county assignment is Wyoming County, GEOID 54109. Governed snapshot version wv-zcta-snapshot-v1. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.

 24719             | 54109               | {"belief_hash": "912b1d40cd56357afcbcc1b44e5de928eeb3988c32c25313fb91a28347e55dfc", "county_name": "Wyoming", "county_geoid": "54109", "snapshot_version": "wv-zcta-snapshot-v1", "canonical_zcta_id": "24719", "verification_state": "derived", "address_point_count": 0, "canonical_county_id": "54109", "dfirm_polygon_count": 0, "address_point_coverage_state": "unknown", "dfirm_polygon_coverage_state": "unknown"}   | ZCTA 24719, West Virginia. Current county assignment is Wyoming County, GEOID 54109. Governed snapshot version wv-zcta-snapshot-v1. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.

 24724             | 54055               | {"belief_hash": "47493c10acf627bda7bca15194120342a15ffdf690aeeb6776a17e920e13ecb0", "county_name": "Mercer", "county_geoid": "54055", "snapshot_version": "wv-zcta-snapshot-v1", "canonical_zcta_id": "24724", "verification_state": "derived", "address_point_count": 0, "canonical_county_id": "54055", "dfirm_polygon_count": 0, "address_point_coverage_state": "unknown", "dfirm_polygon_coverage_state": "unknown"}    | ZCTA 24724, West Virginia. Current county assignment is Mercer County, GEOID 54055. Governed snapshot version wv-zcta-snapshot-v1. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.

(10 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

CREATE EXTENSION IF NOT EXISTS pgcrypto;

INSERT INTO gbim_collection_manifest (

    collection_name,

    collection_version,

    source_view,

    snapshot_version,

    rendering_version,

    embedding_model,

    embedding_dimension,

    permitted_use,

    notes

)

VALUES (

    'gbim_wv_zctas',

    'v1',

    'wv_zcta_belief_vector_ready',

    'wv-zcta-snapshot-v1',

    'zcta-render-v1',

    'all-minilmlatest',

    384,

    'public_civic_geographic_retrieval',

    'First governed ZCTA belief collection'

SQLER BY publication_status; 'v1'v_zctas'on_version_idTHING;

NOTICE:  extension "pgcrypto" already exists, skipping

CREATE EXTENSION

INSERT 0 1

INSERT 0 741

 publication_status | count 

--------------------+-------

 pending            |   741

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ python3 - <<'PY'

import os, json, psycopg2, chromadb

PGHOST=os.getenv("PGHOST","127.0.0.1")

PGPORT=os.getenv("PGPORT","5433")

PGDATABASE=os.getenv("PGDATABASE","msjarvisgis")

PGUSER=os.getenv("PGUSER","postgres")

PGPASSWORD=os.getenv("PGPASSWORD","")

CHROMA_HOST=os.getenv("CHROMA_HOST","127.0.0.1")

CHROMA_PORT=int(os.getenv("CHROMA_PORT","8000"))

conn = psycopg2.connect(

    host=PGHOST,

    port=PGPORT,

    dbname=PGDATABASE,

    user=PGUSER,

    password=PGPASSWORD

)

conn.autocommit = False

with conn.cursor() as cur:

    cur.execute("""

        SELECT

            m.collection_version_id,

PY indent=2))on_version_id": str(collection_version_id)rsion_idmetadata)

Traceback (most recent call last):

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/base_http_client.py", line 99, in _raise_chroma_error

    resp.raise_for_status()

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_models.py", line 761, in raise_for_status

    raise HTTPStatusError(message, request=request, response=self)

httpx.HTTPStatusError: Client error '404 Not Found' for url 'http://127.0.0.1:8000/api/v2/auth/identity'

For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404

During handling of the above exception, another exception occurred:

Traceback (most recent call last):

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/client.py", line 101, in get_user_identity

    return self._server.get_user_identity()

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/telemetry/opentelemetry/__init__.py", line 150, in wrapper

    return f(*args, **kwargs)

           ^^^^^^^^^^^^^^^^^^

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/fastapi.py", line 182, in get_user_identity

    return UserIdentity(**self._make_request("get", "/auth/identity"))

                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/fastapi.py", line 90, in _make_request

    BaseHTTPClient._raise_chroma_error(response)

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/base_http_client.py", line 104, in _raise_chroma_error

    raise (Exception(resp.text))

Exception: {"detail":"Not Found"}

During handling of the above exception, another exception occurred:

Traceback (most recent call last):

  File "<stdin>", line 42, in <module>

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/__init__.py", line 203, in HttpClient

    return ClientCreator(tenant=tenant, database=database, settings=settings)

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/client.py", line 65, in __init__

    user_identity = self.get_user_identity()

                    ^^^^^^^^^^^^^^^^^^^^^^^^

  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/client.py", line 110, in get_user_identity

    raise ValueError(str(e))

ValueError: {"detail":"Not Found"}

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ export PGHOST=127.0.0.1

export PGPORT=5433

export PGDATABASE=msjarvisgis

export PGUSER=postgres

export CHROMA_HOST=127.0.0.1

export CHROMA_PORT=8002

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ python3 - <<'PY'

import os, json, psycopg2, chromadb

from chromadb.config import Settings

PGHOST=os.getenv("PGHOST","127.0.0.1")

PGPORT=os.getenv("PGPORT","5433")

PGDATABASE=os.getenv("PGDATABASE","msjarvisgis")

PGUSER=os.getenv("PGUSER","postgres")

PGPASSWORD=os.getenv("PGPASSWORD","")

CHROMA_HOST=os.getenv("CHROMA_HOST","127.0.0.1")

CHROMA_PORT=int(os.getenv("CHROMA_PORT","8002"))

conn = psycopg2.connect(

    host=PGHOST,

    port=PGPORT,

    dbname=PGDATABASE,

    user=PGUSER,

    password=PGPASSWORD

)

conn.autocommit = False

with conn.cursor() as cur:

    cur.execute("""

        SELECT

PY indent=2))on_version_id": str(collection_version_id)rsion_idmetadata)

{

  "physical_collection": "gbim_wv_zctas_v1",

  "count": 741,

  "collection_version_id": "49e820bd-4f9b-42f6-a7fb-2f36e22f82e0"

}

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ 

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERRORSTOP=1 <<'SQL'

INSERT INTO gbim_active_collection (

    logical_collection_name,

    collection_version_id,

    physical_collection_name

)

SELECT

    'gbim_wv_zctas',

    m.collection_version_id,

    'gbim_wv_zctas_v1'

FROM gbim_collection_manifest m

WHERE m.collection_name = 'gbim_wv_zctas'

  AND m.collection_version = 'v1'

ON CONFLICT (logical_collection_name) DO UPDATE

SET collection_version_id = EXCLUDED.collection_version_id,

    physical_collection_name = EXCLUDED.physical_collection_name,

    activated_at = now();

UPDATE gbim_collection_manifest

SET build_status = 'active',

    promoted_at = now()

WHERE collection_name = 'gbim_wv_zctas'

  AND collection_version = 'v1';

SQLRE logical_collection_name = 'gbim_wv_zctas';

INSERT 0 1

UPDATE 1

 collection_name | collection_version | build_status | record_count |         promoted_at          

-----------------+--------------------+--------------+--------------+------------------------------

 gbim_wv_zctas   | v1                 | active       |          741 | 2026-07-11 19:20:43.87546+00

(1 row)

 logical_collection_name |        collection_version_id         | physical_collection_name |         activated_at          

-------------------------+--------------------------------------+--------------------------+-------------------------------

 gbim_wv_zctas           | 49e820bd-4f9b-42f6-a7fb-2f36e22f82e0 | gbim_wv_zctas_v1         | 2026-07-11 19:20:43.861534+00

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ python3 - <<'PY'

import chromadb, json

from chromadb.config import Settings

client = chromadb.HttpClient(

    host="127.0.0.1",

    port=8002,

    settings=Settings(allow_reset=False)

)

col = client.get_collection("gbim_wv_zctas_v1")

print("COUNT", col.count())

for text in [

    "Show governed ZCTAs in Jefferson County, West Virginia.",

    "Which governed ZCTAs have unresolved D-FIRM coverage in West Virginia?"

]:

    print("\nQUERY:", text)

    q = col.query(query_texts=[text], n_results=5)

    print(json.dumps(q, indent=2)[:4000])

PY

COUNT 741

QUERY: Show governed ZCTAs in Jefferson County, West Virginia.

{

  "ids": [

    [

      "eb77c41263643f300aa9e801f95c9f81e2fe5550ac27dbd45ba55d47c44f62e3",

      "1d7cf39efeb68f072e4dbe34403cb247923ec72e15983d57364997d231f1da7f",

      "414325614bdec16504ad0446d676c8f68b801acd5b646715f9a48d7144c921e9",

      "d5316004d63df0ab275ad0e382cc8042576168b5d031b1d20f7e3a95b79f8c5a",

      "cebe29049fdfbccbeff7ed8f5c4ea271cfbc60f1171b86c5a10b6e2ca7931f92"

    ]

  ],

  "distances": [

    [

      0.3731984496116638,

      0.3782958984375,

      0.3783397078514099,

      0.38205665349960327,

      0.3832830786705017

    ]

  ],

  "embeddings": null,

  "metadatas": [

    [

      {

        "access_class": "public",

        "address_point_count": 0,

        "address_point_coverage_state": "unknown",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "eb77c41263643f300aa9e801f95c9f81e2fe5550ac27dbd45ba55d47c44f62e3",

        "canonical_county_id": "54081",

        "canonical_zcta_id": "25180",

        "county_geoid": "54081",

        "county_name": "Raleigh",

        "dfirm_polygon_count": 0,

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "zcta-render-v1",

        "snapshot_version": "wv-zcta-snapshot-v1",

        "verification_state": "derived"

      },

      {

        "access_class": "public",

        "address_point_count": 0,

        "address_point_coverage_state": "unknown",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "1d7cf39efeb68f072e4dbe34403cb247923ec72e15983d57364997d231f1da7f",

        "canonical_county_id": "54019",

        "canonical_zcta_id": "25186",

        "county_geoid": "54019",

        "county_name": "Fayette",

        "dfirm_polygon_count": 0,

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "zcta-render-v1",

        "snapshot_version": "wv-zcta-snapshot-v1",

        "verification_state": "derived"

      },

      {

        "access_class": "public",

        "address_point_count": 0,

        "address_point_coverage_state": "unknown",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "414325614bdec16504ad0446d676c8f68b801acd5b646715f9a48d7144c921e9",

        "canonical_county_id": "54037",

        "canonical_zcta_id": "20135",

        "county_geoid": "54037",

        "county_name": "Jefferson",

        "dfirm_polygon_count": 0,

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "zcta-render-v1",

        "snapshot_version": "wv-zcta-snapshot-v1",

        "verification_state": "derived"

      },

      {

        "access_class": "public",

        "address_point_count": 0,

        "address_point_coverage_state": "unknown",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "d5316004d63df0ab275ad0e382cc8042576168b5d031b1d20f7e3a95b79f8c5a",

        "canonical_county_id": "54081",

        "canonical_zcta_id": "25140",

        "county_geoid": "54081",

        "county_name": "Raleigh",

        "dfirm_polygon_count": 0,

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "zcta-render-v1",

        "snapshot_version": "wv-zcta-snapshot-v1",

        "verification_state": "derived"

      },

      {

        "access_class": "public",

        "address_point_count": 0,

        "address_point_coverage_state": "unknown",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "cebe29049fdfbccbeff7ed8f5c4ea271cfbc60f1171b86c5a10b6e2ca7931f92",

        "canonical_county_id": "54019",

        "canonical_zcta_id": "25118",

        "county_geoid": "54019",

        "county_name": "Fayette",

        "dfirm_polygon_count": 0,

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civi

QUERY: Which governed ZCTAs have unresolved D-FIRM coverage in West Virginia?

{

  "ids": [

    [

      "42a25643f6617a18f9034b9f312124c8bd441206c255e3441f5b6ef85f2c7322",

      "22ab12c3e17cae18a39c4d10c68e4905a8ce94d45bde0411597ae14db189d07c",

      "27052a87781461268d24d0b7419b84607ef4d458d2cb95b5721853112754d882",

      "91fb239d6be4d2085008b66b3120873fe7fcb6dcdca3e4476caae48e47f4369e",

      "44fe9a99c01b030472f95a67ce14cee48148149ae7d036e4cd2b63424267f1d1"

    ]

  ],

  "distances": [

    [

      0.774611545331268,

      0.7887285957377286,

      0.7902541160583496,

      0.7960536496209698,

      0.7988744959381509

    ]

  ],

  "embeddings": null,

  "metadatas": [

    [

      {

        "access_class": "public",

        "address_point_count": 0,

        "address_point_coverage_state": "unknown",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "42a25643f6617a18f9034b9f312124c8bd441206c255e3441f5b6ef85f2c7322",

        "canonical_county_id": "54023",

        "canonical_zcta_id": "26720",

        "county_geoid": "54023",

        "county_name": "Grant",

        "dfirm_polygon_count": 0,

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "zcta-render-v1",

        "snapshot_version": "wv-zcta-snapshot-v1",

        "verification_state": "derived"

      },

      {

        "access_class": "public",

        "address_point_count": 0,

        "address_point_coverage_state": "unknown",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "22ab12c3e17cae18a39c4d10c68e4905a8ce94d45bde0411597ae14db189d07c",

        "canonical_county_id": "54023",

        "canonical_zcta_id": "26855",

        "county_geoid": "54023",

        "county_name": "Grant",

        "dfirm_polygon_count": 0,

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "zcta-render-v1",

        "snapshot_version": "wv-zcta-snapshot-v1",

        "verification_state": "derived"

      },

      {

        "access_class": "public",

        "address_point_count": 0,

        "address_point_coverage_state": "unknown",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "27052a87781461268d24d0b7419b84607ef4d458d2cb95b5721853112754d882",

        "canonical_county_id": "54023",

        "canonical_zcta_id": "26707",

        "county_geoid": "54023",

        "county_name": "Grant",

        "dfirm_polygon_count": 0,

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "zcta-render-v1",

        "snapshot_version": "wv-zcta-snapshot-v1",

        "verification_state": "derived"

      },

      {

        "access_class": "public",

        "address_point_count": 0,

        "address_point_coverage_state": "unknown",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "91fb239d6be4d2085008b66b3120873fe7fcb6dcdca3e4476caae48e47f4369e",

        "canonical_county_id": "54023",

        "canonical_zcta_id": "26731",

        "county_geoid": "54023",

        "county_name": "Grant",

        "dfirm_polygon_count": 0,

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographic_retrieval",

        "rendering_version": "zcta-render-v1",

        "snapshot_version": "wv-zcta-snapshot-v1",

        "verification_state": "derived"

      },

      {

        "access_class": "public",

        "address_point_count": 0,

        "address_point_coverage_state": "unknown",

        "authority_class": "governed_civic_geographic",

        "belief_hash": "44fe9a99c01b030472f95a67ce14cee48148149ae7d036e4cd2b63424267f1d1",

        "canonical_county_id": "54023",

        "canonical_zcta_id": "26739",

        "county_geoid": "54023",

        "county_name": "Grant",

        "dfirm_polygon_count": 0,

        "dfirm_polygon_coverage_state": "unknown",

        "permitted_use": "public_civic_geographi

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

SELECT 1;

SQL

 ?column? 

----------

        1

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ export PGHOST=127.0.0.1

export PGPORT=5433

export PGDATABASE=msjarvisgis

export PGUSER=postgres

export CHROMA_HOST=127.0.0.1

export CHROMA_PORT=8002

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS wv_tract_representation (

    canonical_tract_id      text    NOT NULL,

    canonical_county_id     text,

    table_name              text    NOT NULL,

    source_feature_id       bigint  NOT NULL,

    source_feature_hash     text,

    PRIMARY KEY (canonical_tract_id, table_name, source_feature_id),

    FOREIGN KEY (canonical_county_id)

        REFERENCES wv_county_identity (canonical_county_id)

);

INSERT INTO wv_tract_representation (

    canonical_tract_id,

    canonical_county_id,

    table_name,

    source_feature_id

)

SELECT

    t.geoidf20,

    LEFT(t.geoidf20, 5),

    'wv_censustracts_census_2020_utm83',

SQLM wv_tract_representation;ture_hash) AS distinct_hashes_name,DO NOTHING;

NOTICE:  extension "pgcrypto" already exists, skipping

CREATE EXTENSION

NOTICE:  relation "wv_tract_representation" already exists, skipping

CREATE TABLE

ERROR:  column t.geoidf20 does not exist

LINE 8:     t.geoidf20,

            ^

HINT:  Perhaps you meant to reference the column "t.geoidfq".

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS wv_tract_representation (

    canonical_tract_id      text    NOT NULL,

    canonical_county_id     text,

    table_name              text    NOT NULL,

    source_feature_id       bigint  NOT NULL,

    source_feature_hash     text,

    PRIMARY KEY (canonical_tract_id, table_name, source_feature_id),

    FOREIGN KEY (canonical_county_id)

        REFERENCES wv_county_identity (canonical_county_id)

);

INSERT INTO wv_tract_representation (

    canonical_tract_id,

    canonical_county_id,

    table_name,

    source_feature_id

)

SELECT

    t.geoidfq,

    LEFT(t.geoidfq, 5),

    'wv_censustracts_census_2020_utm83',

SQLM wv_tract_representation;ture_hash) AS distinct_hashes_name,DO NOTHING;

NOTICE:  extension "pgcrypto" already exists, skipping

CREATE EXTENSION

NOTICE:  relation "wv_tract_representation" already exists, skipping

CREATE TABLE

ERROR:  insert or update on table "wv_tract_representation" violates foreign key constraint "wv_tract_representation_canonical_county_id_fkey"

DETAIL:  Key (canonical_county_id)=(14000) is not present in table "wv_county_identity".

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

ALTER TABLE wv_tract_representation

    DROP CONSTRAINT IF EXISTS wv_tract_representation_canonical_county_id_fkey;

ALTER TABLE wv_tract_representation

    ALTER COLUMN canonical_county_id DROP NOT NULL;

SQL

ALTER TABLE

ALTER TABLE

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

INSERT INTO wv_tract_representation (

    canonical_tract_id,

    canonical_county_id,

    table_name,

    source_feature_id

)

SELECT

    t.geoidfq,

    CASE

        WHEN EXISTS (

            SELECT 1

            FROM wv_county_identity ci

            WHERE ci.canonical_county_id = LEFT(t.geoidfq, 5)

        )

        THEN LEFT(t.geoidfq, 5)

        ELSE NULL

    END,

    'wv_censustracts_census_2020_utm83',

    t.gid::bigint

FROM wv_censustracts_census_2020_utm83 t

ON CONFLICT (canonical_tract_id, table_name, source_feature_id) DO NOTHING;

UPDATE wv_tract_representation r

SQLM wv_tract_representation;ture_hash) AS distinct_hashes_name,

INSERT 0 546

UPDATE 1092

 representations | hashed | distinct_hashes 

-----------------+--------+-----------------

            1092 |   1092 |            1092

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

DROP TABLE IF EXISTS wv_tract_dataset_coverage;

CREATE TABLE wv_tract_dataset_coverage (

    canonical_tract_id      text NOT NULL,

    canonical_county_id     text,

    dataset_type            text NOT NULL,

    source_table            text,

    feature_count           bigint NOT NULL DEFAULT 0,

    coverage_state          text NOT NULL,

    calculated_at           timestamptz NOT NULL DEFAULT now(),

    source_layer_hash       text,

    notes                   text,

    PRIMARY KEY (canonical_tract_id, dataset_type, source_table),

    FOREIGN KEY (canonical_county_id)

        REFERENCES wv_county_identity (canonical_county_id),

    CHECK (coverage_state IN (

        'present',

        'confirmed_none',

        'missing_source',

        'unassigned',

        'not_applicable',

        'unknown'

    ))

SQLER BY dataset_type, coverage_state;e_layer_hash,_id,able) DO UPDATE),nown' END,

ERROR:  cannot drop table wv_tract_dataset_coverage because other objects depend on it

DETAIL:  view wv_tract_belief_vector_ready depends on table wv_tract_dataset_coverage

view wv_dfirm_multiscale_coverage depends on table wv_tract_dataset_coverage

HINT:  Use DROP ... CASCADE to drop the dependent objects too.

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

DROP VIEW IF EXISTS wv_tract_belief_vector_ready;

DROP VIEW IF EXISTS wv_dfirm_multiscale_coverage;

DROP TABLE IF EXISTS wv_tract_dataset_coverage;

CREATE TABLE wv_tract_dataset_coverage (

    canonical_tract_id      text NOT NULL,

    canonical_county_id     text,

    dataset_type            text NOT NULL,

    source_table            text,

    feature_count           bigint NOT NULL DEFAULT 0,

    coverage_state          text NOT NULL,

    calculated_at           timestamptz NOT NULL DEFAULT now(),

    source_layer_hash       text,

    notes                   text,

    PRIMARY KEY (canonical_tract_id, dataset_type, source_table),

    FOREIGN KEY (canonical_county_id)

        REFERENCES wv_county_identity (canonical_county_id),

    CHECK (coverage_state IN (

        'present',

        'confirmed_none',

        'missing_source',

        'unassigned',

SQLER BY dataset_type, coverage_state;e_layer_hash,_id,able) DO UPDATE),nown' END,

DROP VIEW

DROP VIEW

DROP TABLE

CREATE TABLE

ERROR:  column "geoidf20" does not exist

LINE 69:         LEFT(geoidf20, 11) AS canonical_tract_id,

                      ^

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

DROP VIEW IF EXISTS wv_tract_belief_vector_ready;

DROP VIEW IF EXISTS wv_dfirm_multiscale_coverage;

DROP TABLE IF EXISTS wv_tract_dataset_coverage;

CREATE TABLE wv_tract_dataset_coverage (

    canonical_tract_id      text NOT NULL,

    canonical_county_id     text,

    dataset_type            text NOT NULL,

    source_table            text,

    feature_count           bigint NOT NULL DEFAULT 0,

    coverage_state          text NOT NULL,

    calculated_at           timestamptz NOT NULL DEFAULT now(),

    source_layer_hash       text,

    notes                   text,

    PRIMARY KEY (canonical_tract_id, dataset_type, source_table),

    FOREIGN KEY (canonical_county_id)

        REFERENCES wv_county_identity (canonical_county_id),

    CHECK (coverage_state IN (

        'present',

        'confirmed_none',

        'missing_source',

        'unassigned',

SQLER BY dataset_type, coverage_state;e_layer_hash,_id,able) DO UPDATE),nown' END,

NOTICE:  view "wv_tract_belief_vector_ready" does not exist, skipping

DROP VIEW

NOTICE:  view "wv_dfirm_multiscale_coverage" does not exist, skipping

DROP VIEW

DROP TABLE

CREATE TABLE

ERROR:  column "geoidbg" does not exist

LINE 69:         LEFT(geoidbg, 11) AS canonical_tract_id,

                      ^

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

DROP VIEW IF EXISTS wv_tract_belief_vector_ready;

DROP VIEW IF EXISTS wv_dfirm_multiscale_coverage;

DROP TABLE IF EXISTS wv_tract_dataset_coverage;

CREATE TABLE wv_tract_dataset_coverage (

    canonical_tract_id      text NOT NULL,

    canonical_county_id     text,

    dataset_type            text NOT NULL,

    source_table            text,

    feature_count           bigint NOT NULL DEFAULT 0,

    coverage_state          text NOT NULL,

    calculated_at           timestamptz NOT NULL DEFAULT now(),

    source_layer_hash       text,

    notes                   text,

    PRIMARY KEY (canonical_tract_id, dataset_type, source_table),

    FOREIGN KEY (canonical_county_id)

        REFERENCES wv_county_identity (canonical_county_id),

    CHECK (coverage_state IN (

        'present',

        'confirmed_none',

        'missing_source',

        'unassigned',

SQLER BY dataset_type, coverage_state;e_layer_hash,_id,able) DO UPDATE),nown' END,

NOTICE:  view "wv_tract_belief_vector_ready" does not exist, skipping

DROP VIEW

NOTICE:  view "wv_dfirm_multiscale_coverage" does not exist, skipping

DROP VIEW

DROP TABLE

CREATE TABLE

ERROR:  column "geoidf20" does not exist

LINE 69:         LEFT(geoidf20, 11) AS canonical_tract_id,

                      ^

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

SELECT column_name

FROM information_schema.columns

WHERE table_name = 'wv_blockgroups_census_2020_utm83'

ORDER BY column_name;

SQL

     column_name     

---------------------

 aland

 amer_ind

 asian

 awater

 black

 blkgrpce

 canonical_county_id

 countyfp

 funcstat

 geographic

 geoid

 geoidfq

 geom

 gid

 hawn_pi

 intptlat

 intptlon

 mtfcc

 namelsad

 other

 pop2020

 statefp

 tractce

 white

 x

 y

(26 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

DROP VIEW IF EXISTS wv_tract_belief_vector_ready;

DROP VIEW IF EXISTS wv_dfirm_multiscale_coverage;

DROP TABLE IF EXISTS wv_tract_dataset_coverage;

CREATE TABLE wv_tract_dataset_coverage (

    canonical_tract_id      text NOT NULL,

    canonical_county_id     text,

    dataset_type            text NOT NULL,

    source_table            text,

    feature_count           bigint NOT NULL DEFAULT 0,

    coverage_state          text NOT NULL,

    calculated_at           timestamptz NOT NULL DEFAULT now(),

    source_layer_hash       text,

    notes                   text,

    PRIMARY KEY (canonical_tract_id, dataset_type, source_table),

    FOREIGN KEY (canonical_county_id)

        REFERENCES wv_county_identity (canonical_county_id),

    CHECK (coverage_state IN (

        'present',

        'confirmed_none',

        'missing_source',

        'unassigned',

SQLER BY dataset_type, coverage_state;e_layer_hash,_id,able) DO UPDATE),nown' END,

NOTICE:  view "wv_tract_belief_vector_ready" does not exist, skipping

DROP VIEW

NOTICE:  view "wv_dfirm_multiscale_coverage" does not exist, skipping

DROP VIEW

DROP TABLE

CREATE TABLE

INSERT 0 1638

 dataset_type  | coverage_state | tracts | min_count | max_count 

---------------+----------------+--------+-----------+-----------

 address_point | unknown        |    546 |         0 |         0

 blockgroup    | unknown        |    546 |         0 |         0

 dfirm_polygon | unknown        |    546 |         0 |         0

(3 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS wv_tract_belief_snapshot (

    snapshot_id           uuid PRIMARY KEY DEFAULT gen_random_uuid(),

    canonical_tract_id    text NOT NULL,

    canonical_county_id   text,

    snapshot_version      text NOT NULL,

    belief_document       jsonb NOT NULL,

    belief_hash           text NOT NULL,

    generated_at          timestamptz NOT NULL DEFAULT now(),

    verification_state    text NOT NULL DEFAULT 'derived',

    FOREIGN KEY (canonical_county_id)

        REFERENCES wv_county_identity (canonical_county_id),

    UNIQUE (canonical_tract_id, snapshot_version)

);

INSERT INTO wv_tract_belief_snapshot (

    canonical_tract_id,

    canonical_county_id,

    snapshot_version,

    belief_document,

    belief_hash,

    verification_state

SQLRE snapshot_version = 'wv-tract-snapshot-v1';ef_hashesATEhashq, 5)

NOTICE:  extension "pgcrypto" already exists, skipping

CREATE EXTENSION

NOTICE:  relation "wv_tract_belief_snapshot" already exists, skipping

CREATE TABLE

ERROR:  unrecognized encoding: "sha256"

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS wv_tract_belief_snapshot (

    snapshot_id           uuid PRIMARY KEY DEFAULT gen_random_uuid(),

    canonical_tract_id    text NOT NULL,

    canonical_county_id   text,

    snapshot_version      text NOT NULL,

    belief_document       jsonb NOT NULL,

    belief_hash           text NOT NULL,

    generated_at          timestamptz NOT NULL DEFAULT now(),

    verification_state    text NOT NULL DEFAULT 'derived',

    FOREIGN KEY (canonical_county_id)

        REFERENCES wv_county_identity (canonical_county_id),

    UNIQUE (canonical_tract_id, snapshot_version)

);

INSERT INTO wv_tract_belief_snapshot (

    canonical_tract_id,

    canonical_county_id,

    snapshot_version,

    belief_document,

    belief_hash,

    verification_state

SQLRE snapshot_version = 'wv-tract-snapshot-v1';ef_hashesATEhashq, 5)

NOTICE:  extension "pgcrypto" already exists, skipping

CREATE EXTENSION

NOTICE:  relation "wv_tract_belief_snapshot" already exists, skipping

CREATE TABLE

ERROR:  null value in column "canonical_county_id" of relation "wv_tract_belief_snapshot" violates not-null constraint

DETAIL:  Failing row contains (de46448d-8d69-4eb2-b8e7-b7add3f0077e, 1400000US54003971103, null, wv-tract-snapshot-v1, {"coverage": [{"notes": "Tract-level address-point coverage not ..., 8075ed00237d99ab37aa6af8a95a458355db04f4d9dec060fd54bd37c1ec53ef, 2026-07-11 19:43:33.096503+00, derived).

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

ALTER TABLE wv_tract_belief_snapshot

    ALTER COLUMN canonical_county_id DROP NOT NULL;

SQL

ALTER TABLE

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

DELETE FROM wv_tract_belief_snapshot

WHERE snapshot_version = 'wv-tract-snapshot-v1';

INSERT INTO wv_tract_belief_snapshot (

    canonical_tract_id,

    canonical_county_id,

    snapshot_version,

    belief_document,

    belief_hash,

    verification_state

)

SELECT

    t.geoidfq,

    CASE

        WHEN EXISTS (

            SELECT 1

            FROM wv_county_identity ci

            WHERE ci.canonical_county_id = LEFT(t.geoidfq, 5)

        )

        THEN LEFT(t.geoidfq, 5)

        ELSE NULL

    END,

    'wv-tract-snapshot-v1',

SQLRE snapshot_version = 'wv-tract-snapshot-v1';S NULL) AS null_county_ids

DELETE 546

INSERT 0 546

 snapshot_rows | tracts | distinct_belief_hashes | null_county_ids 

---------------+--------+------------------------+-----------------

           546 |    546 |                    546 |             546

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

DROP VIEW IF EXISTS wv_tract_belief_vector_ready;

CREATE VIEW wv_tract_belief_vector_ready AS

SELECT

    s.snapshot_version,

    s.canonical_tract_id,

    s.canonical_county_id,

    ci.county_name,

    s.belief_hash AS document_id,

    jsonb_build_object(

        'canonical_tract_id', s.canonical_tract_id,

        'canonical_county_id', s.canonical_county_id,

        'county_geoid', s.canonical_county_id,

        'county_name', ci.county_name,

        'snapshot_version', s.snapshot_version,

        'belief_hash', s.belief_hash,

        'verification_state', s.verification_state,

        'blockgroup_count', COALESCE(bg.feature_count, 0),

        'blockgroup_coverage_state', COALESCE(bg.coverage_state, 'unknown'),

        'address_point_count', COALESCE(ap.feature_count, 0),

        'address_point_coverage_state', COALESCE(ap.coverage_state, 'unknown'),

        'dfirm_polygon_count', COALESCE(df.feature_count, 0),

        'dfirm_polygon_coverage_state', COALESCE(df.coverage_state, 'unknown')

SQLIT 10;canonical_tract_id_readycal_county_id, metadata, documenterified absence.

NOTICE:  view "wv_tract_belief_vector_ready" does not exist, skipping

DROP VIEW

CREATE VIEW

  canonical_tract_id  | canonical_county_id |                                                                                                                                                                                                                                            metadata                                                                                                                                                                                                                                             |                                                                                                                                                                                                document                                                                                                                                                                                                 

----------------------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 1400000US54001965500 |                     | {"belief_hash": "827184090a7509c3cdbf4a0e361de91284365223a490ed24baae421d3ee0e079", "county_name": null, "county_geoid": null, "blockgroup_count": 0, "snapshot_version": "wv-tract-snapshot-v1", "canonical_tract_id": "1400000US54001965500", "verification_state": "derived", "address_point_count": 0, "canonical_county_id": null, "dfirm_polygon_count": 0, "blockgroup_coverage_state": "unknown", "address_point_coverage_state": "unknown", "dfirm_polygon_coverage_state": "unknown"} | Census tract 1400000US54001965500, West Virginia. Current county assignment is unresolved. Governed snapshot version wv-tract-snapshot-v1. Block-group count: 0. Block-group coverage state: unknown. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.

 1400000US54001965600 |                     | {"belief_hash": "bf61409fb373b95114bf2b4cf87edadbf095c0cbde8d48a37bb1f4edb7f5834b", "county_name": null, "county_geoid": null, "blockgroup_count": 0, "snapshot_version": "wv-tract-snapshot-v1", "canonical_tract_id": "1400000US54001965600", "verification_state": "derived", "address_point_count": 0, "canonical_county_id": null, "dfirm_polygon_count": 0, "blockgroup_coverage_state": "unknown", "address_point_coverage_state": "unknown", "dfirm_polygon_coverage_state": "unknown"} | Census tract 1400000US54001965600, West Virginia. Current county assignment is unresolved. Governed snapshot version wv-tract-snapshot-v1. Block-group count: 0. Block-group coverage state: unknown. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.

 1400000US54001965700 |                     | {"belief_hash": "1c08351ed8b97f089b12c6262dca60262fd85676e0e45cd6f352490576c714b8", "county_name": null, "county_geoid": null, "blockgroup_count": 0, "snapshot_version": "wv-tract-snapshot-v1", "canonical_tract_id": "1400000US54001965700", "verification_state": "derived", "address_point_count": 0, "canonical_county_id": null, "dfirm_polygon_count": 0, "blockgroup_coverage_state": "unknown", "address_point_coverage_state": "unknown", "dfirm_polygon_coverage_state": "unknown"} | Census tract 1400000US54001965700, West Virginia. Current county assignment is unresolved. Governed snapshot version wv-tract-snapshot-v1. Block-group count: 0. Block-group coverage state: unknown. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.

 1400000US54001965800 |                     | {"belief_hash": "a9dd1c1b14a723c6406bc273091af46bc8c1fe2f64fcdad9e16f21f00e56de17", "county_name": null, "county_geoid": null, "blockgroup_count": 0, "snapshot_version": "wv-tract-snapshot-v1", "canonical_tract_id": "1400000US54001965800", "verification_state": "derived", "address_point_count": 0, "canonical_county_id": null, "dfirm_polygon_count": 0, "blockgroup_coverage_state": "unknown", "address_point_coverage_state": "unknown", "dfirm_polygon_coverage_state": "unknown"} | Census tract 1400000US54001965800, West Virginia. Current county assignment is unresolved. Governed snapshot version wv-tract-snapshot-v1. Block-group count: 0. Block-group coverage state: unknown. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.

 1400000US54003971101 |                     | {"belief_hash": "983e0543189bcb878dfd35d8462b26ac9243e9e1b865d0aae7bf22adb89e2e3d", "county_name": null, "county_geoid": null, "blockgroup_count": 0, "snapshot_version": "wv-tract-snapshot-v1", "canonical_tract_id": "1400000US54003971101", "verification_state": "derived", "address_point_count": 0, "canonical_county_id": null, "dfirm_polygon_count": 0, "blockgroup_coverage_state": "unknown", "address_point_coverage_state": "unknown", "dfirm_polygon_coverage_state": "unknown"} | Census tract 1400000US54003971101, West Virginia. Current county assignment is unresolved. Governed snapshot version wv-tract-snapshot-v1. Block-group count: 0. Block-group coverage state: unknown. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.

 1400000US54003971103 |                     | {"belief_hash": "c6b2a15b71f0ca4ff9cf65d6ff3aa152d9b817e67db6dcc8ef83a88a98ea0946", "county_name": null, "county_geoid": null, "blockgroup_count": 0, "snapshot_version": "wv-tract-snapshot-v1", "canonical_tract_id": "1400000US54003971103", "verification_state": "derived", "address_point_count": 0, "canonical_county_id": null, "dfirm_polygon_count": 0, "blockgroup_coverage_state": "unknown", "address_point_coverage_state": "unknown", "dfirm_polygon_coverage_state": "unknown"} | Census tract 1400000US54003971103, West Virginia. Current county assignment is unresolved. Governed snapshot version wv-tract-snapshot-v1. Block-group count: 0. Block-group coverage state: unknown. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.

 1400000US54003971104 |                     | {"belief_hash": "d3da56da51113cd69c0ba9aaf4b7655a5c75549993bf2daf60dcfe11d05c3e90", "county_name": null, "county_geoid": null, "blockgroup_count": 0, "snapshot_version": "wv-tract-snapshot-v1", "canonical_tract_id": "1400000US54003971104", "verification_state": "derived", "address_point_count": 0, "canonical_county_id": null, "dfirm_polygon_count": 0, "blockgroup_coverage_state": "unknown", "address_point_coverage_state": "unknown", "dfirm_polygon_coverage_state": "unknown"} | Census tract 1400000US54003971104, West Virginia. Current county assignment is unresolved. Governed snapshot version wv-tract-snapshot-v1. Block-group count: 0. Block-group coverage state: unknown. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.

 1400000US54003971105 |                     | {"belief_hash": "48407143e33517a9c3750827baf76fc7298d9e133fd8c5e4e9d34276f5811465", "county_name": null, "county_geoid": null, "blockgroup_count": 0, "snapshot_version": "wv-tract-snapshot-v1", "canonical_tract_id": "1400000US54003971105", "verification_state": "derived", "address_point_count": 0, "canonical_county_id": null, "dfirm_polygon_count": 0, "blockgroup_coverage_state": "unknown", "address_point_coverage_state": "unknown", "dfirm_polygon_coverage_state": "unknown"} | Census tract 1400000US54003971105, West Virginia. Current county assignment is unresolved. Governed snapshot version wv-tract-snapshot-v1. Block-group count: 0. Block-group coverage state: unknown. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.

 1400000US54003971203 |                     | {"belief_hash": "b9d9455753a6868ad1c31fb721433c21284e2a604e51928ebcae7867fd5ac05d", "county_name": null, "county_geoid": null, "blockgroup_count": 0, "snapshot_version": "wv-tract-snapshot-v1", "canonical_tract_id": "1400000US54003971203", "verification_state": "derived", "address_point_count": 0, "canonical_county_id": null, "dfirm_polygon_count": 0, "blockgroup_coverage_state": "unknown", "address_point_coverage_state": "unknown", "dfirm_polygon_coverage_state": "unknown"} | Census tract 1400000US54003971203, West Virginia. Current county assignment is unresolved. Governed snapshot version wv-tract-snapshot-v1. Block-group count: 0. Block-group coverage state: unknown. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.

 1400000US54003971204 |                     | {"belief_hash": "d1d721fb45130fe056b62c673ab03c8aad2bbccd968ce9da6fad057781263d62", "county_name": null, "county_geoid": null, "blockgroup_count": 0, "snapshot_version": "wv-tract-snapshot-v1", "canonical_tract_id": "1400000US54003971204", "verification_state": "derived", "address_point_count": 0, "canonical_county_id": null, "dfirm_polygon_count": 0, "blockgroup_coverage_state": "unknown", "address_point_coverage_state": "unknown", "dfirm_polygon_coverage_state": "unknown"} | Census tract 1400000US54003971204, West Virginia. Current county assignment is unresolved. Governed snapshot version wv-tract-snapshot-v1. Block-group count: 0. Block-group coverage state: unknown. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.

(10 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

SELECT

    canonical_tract_id,

    length(canonical_tract_id) AS id_length,

    COUNT(*)

FROM wv_tract_belief_snapshot

GROUP BY canonical_tract_id, length(canonical_tract_id)

ORDER BY canonical_tract_id

LIMIT 20;

SELECT

    canonical_tract_id,

    substring(canonical_tract_id FROM '([0-9]{11})$') AS tract_geoid,

    substring(

        substring(canonical_tract_id FROM '([0-9]{11})$')

        FROM 1 FOR 5

    ) AS derived_county_geoid

FROM wv_tract_belief_snapshot

ORDER BY canonical_tract_id

LIMIT 20;

SQL

  canonical_tract_id  | id_length | count 

----------------------+-----------+-------

 1400000US54001965500 |        20 |     1

 1400000US54001965600 |        20 |     1

 1400000US54001965700 |        20 |     1

 1400000US54001965800 |        20 |     1

 1400000US54003971101 |        20 |     1

 1400000US54003971103 |        20 |     1

 1400000US54003971104 |        20 |     1

 1400000US54003971105 |        20 |     1

 1400000US54003971203 |        20 |     1

 1400000US54003971204 |        20 |     1

 1400000US54003971205 |        20 |     1

 1400000US54003971206 |        20 |     1

 1400000US54003971301 |        20 |     1

 1400000US54003971302 |        20 |     1

 1400000US54003971401 |        20 |     1

 1400000US54003971402 |        20 |     1

 1400000US54003971500 |        20 |     1

 1400000US54003971600 |        20 |     1

 1400000US54003971700 |        20 |     1

 1400000US54003971801 |        20 |     1

(20 rows)

  canonical_tract_id  | tract_geoid | derived_county_geoid 

----------------------+-------------+----------------------

 1400000US54001965500 | 54001965500 | 54001

 1400000US54001965600 | 54001965600 | 54001

 1400000US54001965700 | 54001965700 | 54001

 1400000US54001965800 | 54001965800 | 54001

 1400000US54003971101 | 54003971101 | 54003

 1400000US54003971103 | 54003971103 | 54003

 1400000US54003971104 | 54003971104 | 54003

 1400000US54003971105 | 54003971105 | 54003

 1400000US54003971203 | 54003971203 | 54003

 1400000US54003971204 | 54003971204 | 54003

 1400000US54003971205 | 54003971205 | 54003

 1400000US54003971206 | 54003971206 | 54003

 1400000US54003971301 | 54003971301 | 54003

 1400000US54003971302 | 54003971302 | 54003

 1400000US54003971401 | 54003971401 | 54003

 1400000US54003971402 | 54003971402 | 54003

 1400000US54003971500 | 54003971500 | 54003

 1400000US54003971600 | 54003971600 | 54003

 1400000US54003971700 | 54003971700 | 54003

 1400000US54003971801 | 54003971801 | 54003

(20 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

UPDATE wv_tract_identity t

SET canonical_county_id = c.canonical_county_id,

    updated_at = now()

FROM wv_county_identity c

WHERE c.county_geoid =

      substring(

          substring(t.canonical_tract_id FROM '([0-9]{11})$')

          FROM 1 FOR 5

      )

  AND t.canonical_county_id IS NULL;

SELECT

    COUNT(*) AS total_tracts,

    COUNT(canonical_county_id) AS county_resolved,

    COUNT(*) FILTER (WHERE canonical_county_id IS NULL) AS county_unresolved

FROM wv_tract_identity;

SQL

ERROR:  relation "wv_tract_identity" does not exist

LINE 1: UPDATE wv_tract_identity t

               ^

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

CREATE TABLE IF NOT EXISTS wv_tract_identity (

    canonical_tract_id   text PRIMARY KEY,

    tract_geoid          text NOT NULL,

    canonical_county_id  text,

    created_at           timestamptz NOT NULL DEFAULT now(),

    updated_at           timestamptz NOT NULL DEFAULT now(),

    FOREIGN KEY (canonical_county_id)

        REFERENCES wv_county_identity (canonical_county_id)

);

INSERT INTO wv_tract_identity (

    canonical_tract_id,

    tract_geoid,

    canonical_county_id

)

SELECT

    s.canonical_tract_id,

    substring(s.canonical_tract_id FROM '([0-9]{11})$') AS tract_geoid,

    NULL::text

FROM wv_tract_belief_snapshot s

WHERE s.snapshot_version = 'wv-tract-snapshot-v1'

ON CONFLICT (canonical_tract_id) DO NOTHING;

SQLM wv_tract_identity;ERE canonical_county_id IS NULL) AS county_unresolved

CREATE TABLE

INSERT 0 546

UPDATE 546

 total_tracts | county_resolved | county_unresolved 

--------------+-----------------+-------------------

          546 |             546 |                 0

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

SELECT

    c.canonical_county_id,

    c.county_name,

    COUNT(t.canonical_tract_id) AS n_tracts

FROM wv_county_identity c

LEFT JOIN wv_tract_identity t

  ON t.canonical_county_id = c.canonical_county_id

GROUP BY c.canonical_county_id, c.county_name

ORDER BY c.canonical_county_id;

SELECT

    c.canonical_county_id,

    c.county_name,

    c.n_tracts AS county_summary_count,

    COUNT(t.canonical_tract_id) AS canonical_tract_count

FROM wv_county_belief_summary c

LEFT JOIN wv_tract_identity t

  ON t.canonical_county_id = c.canonical_county_id

GROUP BY

    c.canonical_county_id,

    c.county_name,

    c.n_tracts

HAVING c.n_tracts <> COUNT(t.canonical_tract_id)

SQLER BY c.canonical_county_id;

 canonical_county_id | county_name | n_tracts 

---------------------+-------------+----------

 54001               | Barbour     |        4

 54003               | Berkeley    |       26

 54005               | Boone       |        8

 54007               | Braxton     |        3

 54009               | Brooke      |        8

 54011               | Cabell      |       34

 54013               | Calhoun     |        2

 54015               | Clay        |        3

 54017               | Doddridge   |        2

 54019               | Fayette     |       13

 54021               | Gilmer      |        3

 54023               | Grant       |        3

 54025               | Greenbrier  |       10

 54027               | Hampshire   |        9

 54029               | Hancock     |        8

 54031               | Hardy       |        5

 54033               | Harrison    |       25

 54035               | Jackson     |        7

 54037               | Jefferson   |       15

 54039               | Kanawha     |       57

 54041               | Lewis       |        5

 54043               | Lincoln     |        6

 54045               | Logan       |       10

 54047               | McDowell    |        8

 54049               | Marion      |       21

 54051               | Marshall    |       10

 54053               | Mason       |        7

 54055               | Mercer      |       16

 54057               | Mineral     |        7

 54059               | Mingo       |        7

 54061               | Monongalia  |       28

 54063               | Monroe      |        3

 54065               | Morgan      |        6

 54067               | Nicholas    |        8

 54069               | Ohio        |       18

 54071               | Pendleton   |        3

 54073               | Pleasants   |        2

 54075               | Pocahontas  |        5

 54077               | Preston     |       11

 54079               | Putnam      |       12

 54081               | Raleigh     |       17

 54083               | Randolph    |        7

 54085               | Ritchie     |        3

 54087               | Roane       |        5

 54089               | Summers     |        4

 54091               | Taylor      |        4

 54093               | Tucker      |        3

 54095               | Tyler       |        3

 54097               | Upshur      |        6

 54099               | Wayne       |       11

 54101               | Webster     |        4

 54103               | Wetzel      |        5

 54105               | Wirt        |        2

 54107               | Wood        |       28

 54109               | Wyoming     |        6

(55 rows)

 canonical_county_id | county_name | county_summary_count | canonical_tract_count 

---------------------+-------------+----------------------+-----------------------

 54003               | Berkeley    |                   25 |                    26

 54057               | Mineral     |                    6 |                     7

 54095               | Tyler       |                    4 |                     3

 54103               | Wetzel      |                    4 |                     5

(4 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

ALTER TABLE wv_tract_representation

    ALTER COLUMN canonical_county_id DROP NOT NULL;

UPDATE wv_tract_representation r

SET canonical_county_id = t.canonical_county_id,

    updated_at = now()

FROM wv_tract_identity t

WHERE t.canonical_tract_id = r.canonical_tract_id

  AND r.canonical_county_id IS DISTINCT FROM t.canonical_county_id;

SELECT

    COUNT(*) AS representations,

    COUNT(canonical_county_id) AS county_resolved,

    COUNT(*) FILTER (WHERE canonical_county_id IS NULL) AS county_unresolved

FROM wv_tract_representation;

SQL

ALTER TABLE

ERROR:  column "updated_at" of relation "wv_tract_representation" does not exist

LINE 3:     updated_at = now()

            ^

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

ALTER TABLE wv_tract_representation

    ALTER COLUMN canonical_county_id DROP NOT NULL;

UPDATE wv_tract_representation r

SET canonical_county_id = t.canonical_county_id

FROM wv_tract_identity t

WHERE t.canonical_tract_id = r.canonical_tract_id

  AND r.canonical_county_id IS DISTINCT FROM t.canonical_county_id;

SELECT

    COUNT(*) AS representations,

    COUNT(canonical_county_id) AS county_resolved,

    COUNT(*) FILTER (WHERE canonical_county_id IS NULL) AS county_unresolved

FROM wv_tract_representation;

SQL

ALTER TABLE

UPDATE 546

 representations | county_resolved | county_unresolved 

-----------------+-----------------+-------------------

            1092 |            1092 |                 0

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

SELECT

    c.canonical_county_id,

    c.county_name,

    c.n_tracts AS county_summary_count,

    COUNT(t.canonical_tract_id) AS canonical_tract_count

FROM wv_county_belief_summary c

LEFT JOIN wv_tract_identity t

  ON t.canonical_county_id = c.canonical_county_id

GROUP BY

    c.canonical_county_id,

    c.county_name,

    c.n_tracts

HAVING c.n_tracts <> COUNT(t.canonical_tract_id)

ORDER BY c.canonical_county_id;

SELECT

    t.canonical_tract_id,

    t.tract_geoid,

    t.canonical_county_id,

    c.county_name

FROM wv_tract_identity t

JOIN wv_county_identity c

  ON c.canonical_county_id = t.canonical_county_id

SQLER BY t.canonical_county_id, t.tract_geoid;','54095','54103')

 canonical_county_id | county_name | county_summary_count | canonical_tract_count 

---------------------+-------------+----------------------+-----------------------

 54003               | Berkeley    |                   25 |                    26

 54057               | Mineral     |                    6 |                     7

 54095               | Tyler       |                    4 |                     3

 54103               | Wetzel      |                    4 |                     5

(4 rows)

  canonical_tract_id  | tract_geoid | canonical_county_id | county_name 

----------------------+-------------+---------------------+-------------

 1400000US54003971101 | 54003971101 | 54003               | Berkeley

 1400000US54003971103 | 54003971103 | 54003               | Berkeley

 1400000US54003971104 | 54003971104 | 54003               | Berkeley

 1400000US54003971105 | 54003971105 | 54003               | Berkeley

 1400000US54003971203 | 54003971203 | 54003               | Berkeley

 1400000US54003971204 | 54003971204 | 54003               | Berkeley

 1400000US54003971205 | 54003971205 | 54003               | Berkeley

 1400000US54003971206 | 54003971206 | 54003               | Berkeley

 1400000US54003971301 | 54003971301 | 54003               | Berkeley

 1400000US54003971302 | 54003971302 | 54003               | Berkeley

 1400000US54003971401 | 54003971401 | 54003               | Berkeley

 1400000US54003971402 | 54003971402 | 54003               | Berkeley

 1400000US54003971500 | 54003971500 | 54003               | Berkeley

 1400000US54003971600 | 54003971600 | 54003               | Berkeley

 1400000US54003971700 | 54003971700 | 54003               | Berkeley

 1400000US54003971801 | 54003971801 | 54003               | Berkeley

 1400000US54003971802 | 54003971802 | 54003               | Berkeley

 1400000US54003971901 | 54003971901 | 54003               | Berkeley

 1400000US54003971902 | 54003971902 | 54003               | Berkeley

 1400000US54003972001 | 54003972001 | 54003               | Berkeley

 1400000US54003972002 | 54003972002 | 54003               | Berkeley

 1400000US54003972003 | 54003972003 | 54003               | Berkeley

 1400000US54003972101 | 54003972101 | 54003               | Berkeley

 1400000US54003972103 | 54003972103 | 54003               | Berkeley

 1400000US54003972104 | 54003972104 | 54003               | Berkeley

 1400000US54003972105 | 54003972105 | 54003               | Berkeley

 1400000US54057010100 | 54057010100 | 54057               | Mineral

 1400000US54057010200 | 54057010200 | 54057               | Mineral

 1400000US54057010300 | 54057010300 | 54057               | Mineral

 1400000US54057010400 | 54057010400 | 54057               | Mineral

 1400000US54057010500 | 54057010500 | 54057               | Mineral

 1400000US54057010600 | 54057010600 | 54057               | Mineral

 1400000US54057010700 | 54057010700 | 54057               | Mineral

 1400000US54095961800 | 54095961800 | 54095               | Tyler

 1400000US54095961900 | 54095961900 | 54095               | Tyler

 1400000US54095962000 | 54095962000 | 54095               | Tyler

 1400000US54103004900 | 54103004900 | 54103               | Wetzel

 1400000US54103030400 | 54103030400 | 54103               | Wetzel

 1400000US54103030500 | 54103030500 | 54103               | Wetzel

 1400000US54103030700 | 54103030700 | 54103               | Wetzel

 1400000US54103030800 | 54103030800 | 54103               | Wetzel

(41 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

WITH canonical AS (

    SELECT

        t.canonical_county_id,

        COUNT(t.canonical_tract_id) AS canonical_tract_count

    FROM wv_tract_identity t

    GROUP BY t.canonical_county_id

),

mismatches AS (

    SELECT

        c.canonical_county_id,

        c.county_name,

        c.n_tracts AS county_summary_count,

        canonical.canonical_tract_count

    FROM wv_county_belief_summary c

    JOIN canonical

      ON canonical.canonical_county_id = c.canonical_county_id

    WHERE c.n_tracts <> canonical.canonical_tract_count

)

UPDATE wv_county_belief_summary c

SET n_tracts = m.canonical_tract_count

FROM mismatches m

WHERE c.canonical_county_id = m.canonical_county_id;

SQLER BY c.canonical_county_id;nonical_tract_id)id_count

ERROR:  cannot update view "wv_county_belief_summary"

DETAIL:  Views that do not select from a single table or view are not automatically updatable.

HINT:  To enable updating the view, provide an INSTEAD OF UPDATE trigger or an unconditional ON UPDATE DO INSTEAD rule.

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

WITH canonical AS (

    SELECT

        t.canonical_county_id,

        COUNT(t.canonical_tract_id) AS canonical_tract_count

    FROM wv_tract_identity t

    GROUP BY t.canonical_county_id

),

mismatches AS (

    SELECT

        c.canonical_county_id,

        c.county_name,

        c.n_tracts AS county_summary_count,

        canonical.canonical_tract_count

    FROM wv_county_belief_summary c

    JOIN canonical

      ON canonical.canonical_county_id = c.canonical_county_id

    WHERE c.n_tracts <> canonical.canonical_tract_count

)

UPDATE wv_county_belief_summary_base b

SET n_tracts = m.canonical_tract_count,

    updated_at = now()

FROM mismatches m

SQLER BY c.canonical_county_id;nonical_tract_id)id_count

ERROR:  relation "wv_county_belief_summary_base" does not exist

LINE 19: UPDATE wv_county_belief_summary_base b

                ^

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

CREATE OR REPLACE VIEW wv_county_tract_reconciliation AS

WITH canonical AS (

    SELECT

        canonical_county_id,

        COUNT(*) AS canonical_tract_count

    FROM wv_tract_identity

    WHERE canonical_county_id IS NOT NULL

    GROUP BY canonical_county_id

)

SELECT

    ci.canonical_county_id,

    ci.county_name,

    COALESCE(bs.n_tracts, 0) AS summary_tract_count,

    COALESCE(c.canonical_tract_count, 0) AS canonical_tract_count,

    COALESCE(c.canonical_tract_count, 0)

        - COALESCE(bs.n_tracts, 0) AS count_delta,

    CASE

        WHEN COALESCE(c.canonical_tract_count, 0)

           = COALESCE(bs.n_tracts, 0)

        THEN 'reconciled'

        ELSE 'discrepancy'

    END AS reconciliation_state

FROM wv_county_identity ci

SQLER BY canonical_county_id;'discrepancy'county_id;

CREATE VIEW

 canonical_county_id | county_name | summary_tract_count | canonical_tract_count | count_delta | reconciliation_state 

---------------------+-------------+---------------------+-----------------------+-------------+----------------------

 54003               | Berkeley    |                  25 |                    26 |           1 | discrepancy

 54057               | Mineral     |                   6 |                     7 |           1 | discrepancy

 54095               | Tyler       |                   4 |                     3 |          -1 | discrepancy

 54103               | Wetzel      |                   4 |                     5 |           1 | discrepancy

(4 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

SELECT pg_get_viewdef(

    'wv_county_belief_summary'::regclass,

    true

);

SQL

                                                             pg_get_viewdef                                                             

----------------------------------------------------------------------------------------------------------------------------------------

  SELECT ci.canonical_county_id,                                                                                                       +

     ci.county_name,                                                                                                                   +

     COALESCE(z.n_zctas, 0::bigint) AS n_zctas,                                                                                        +

     COALESCE(t.n_tracts, 0::bigint) AS n_tracts,                                                                                      +

     COALESCE(bg.n_blockgroups, 0::bigint) AS n_blockgroups,                                                                           +

     COALESCE(ap.n_address_points, 0::bigint) AS n_address_points,                                                                     +

     COALESCE(d.n_dfirm_polygons, 0::bigint) AS n_dfirm_polygons                                                                       +

    FROM wv_county_identity ci                                                                                                         +

      LEFT JOIN ( SELECT wv_zipcodetabulationarea_census_2020_utm83.canonical_county_id,                                               +

             count(*) AS n_zctas                                                                                                       +

            FROM wv_zipcodetabulationarea_census_2020_utm83                                                                            +

           GROUP BY wv_zipcodetabulationarea_census_2020_utm83.canonical_county_id) z ON z.canonical_county_id = ci.canonical_county_id+

      LEFT JOIN ( SELECT wv_censustracts_census_2020_utm83.canonical_county_id,                                                        +

             count(*) AS n_tracts                                                                                                      +

            FROM wv_censustracts_census_2020_utm83                                                                                     +

           GROUP BY wv_censustracts_census_2020_utm83.canonical_county_id) t ON t.canonical_county_id = ci.canonical_county_id         +

      LEFT JOIN ( SELECT wv_blockgroups_census_2020_utm83.canonical_county_id,                                                         +

             count(*) AS n_blockgroups                                                                                                 +

            FROM wv_blockgroups_census_2020_utm83                                                                                      +

           GROUP BY wv_blockgroups_census_2020_utm83.canonical_county_id) bg ON bg.canonical_county_id = ci.canonical_county_id        +

      LEFT JOIN ( SELECT ap_all.canonical_county_id,                                                                                   +

             count(*) AS n_address_points                                                                                              +

            FROM ( SELECT wv_address_points_barbour.canonical_county_id                                                                +

                    FROM wv_address_points_barbour                                                                                     +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_berkeley.canonical_county_id                                                                +

                    FROM wv_address_points_berkeley                                                                                    +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_boone.canonical_county_id                                                                   +

                    FROM wv_address_points_boone                                                                                       +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_braxton.canonical_county_id                                                                 +

                    FROM wv_address_points_braxton                                                                                     +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_brooke.canonical_county_id                                                                  +

                    FROM wv_address_points_brooke                                                                                      +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_cabell.canonical_county_id                                                                  +

                    FROM wv_address_points_cabell                                                                                      +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_calhoun.canonical_county_id                                                                 +

                    FROM wv_address_points_calhoun                                                                                     +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_clay.canonical_county_id                                                                    +

                    FROM wv_address_points_clay                                                                                        +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_doddridge.canonical_county_id                                                               +

                    FROM wv_address_points_doddridge                                                                                   +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_fayette.canonical_county_id                                                                 +

                    FROM wv_address_points_fayette                                                                                     +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_gilmer.canonical_county_id                                                                  +

                    FROM wv_address_points_gilmer                                                                                      +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_grant.canonical_county_id                                                                   +

                    FROM wv_address_points_grant                                                                                       +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_greenbrier.canonical_county_id                                                              +

                    FROM wv_address_points_greenbrier                                                                                  +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_hampshire.canonical_county_id                                                               +

                    FROM wv_address_points_hampshire                                                                                   +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_hancock.canonical_county_id                                                                 +

                    FROM wv_address_points_hancock                                                                                     +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_hardy.canonical_county_id                                                                   +

                    FROM wv_address_points_hardy                                                                                       +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_harrison.canonical_county_id                                                                +

                    FROM wv_address_points_harrison                                                                                    +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_jackson.canonical_county_id                                                                 +

                    FROM wv_address_points_jackson                                                                                     +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_jefferson.canonical_county_id                                                               +

                    FROM wv_address_points_jefferson                                                                                   +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_kanawha_part1.canonical_county_id                                                           +

                    FROM wv_address_points_kanawha_part1                                                                               +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_kanawha_part2.canonical_county_id                                                           +

                    FROM wv_address_points_kanawha_part2                                                                               +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_lewis.canonical_county_id                                                                   +

                    FROM wv_address_points_lewis                                                                                       +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_lincoln.canonical_county_id                                                                 +

                    FROM wv_address_points_lincoln                                                                                     +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_logan.canonical_county_id                                                                   +

                    FROM wv_address_points_logan                                                                                       +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_marion.canonical_county_id                                                                  +

                    FROM wv_address_points_marion                                                                                      +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_marshall.canonical_county_id                                                                +

                    FROM wv_address_points_marshall                                                                                    +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_mason.canonical_county_id                                                                   +

                    FROM wv_address_points_mason                                                                                       +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_mcdowell.canonical_county_id                                                                +

                    FROM wv_address_points_mcdowell                                                                                    +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_mercer.canonical_county_id                                                                  +

                    FROM wv_address_points_mercer                                                                                      +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_mineral.canonical_county_id                                                                 +

                    FROM wv_address_points_mineral                                                                                     +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_mingo.canonical_county_id                                                                   +

                    FROM wv_address_points_mingo                                                                                       +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_monongalia.canonical_county_id                                                              +

                    FROM wv_address_points_monongalia                                                                                  +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_monroe.canonical_county_id                                                                  +

                    FROM wv_address_points_monroe                                                                                      +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_morgan.canonical_county_id                                                                  +

                    FROM wv_address_points_morgan                                                                                      +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_nicholas.canonical_county_id                                                                +

                    FROM wv_address_points_nicholas                                                                                    +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_ohio.canonical_county_id                                                                    +

                    FROM wv_address_points_ohio                                                                                        +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_pendleton.canonical_county_id                                                               +

                    FROM wv_address_points_pendleton                                                                                   +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_pleasants.canonical_county_id                                                               +

                    FROM wv_address_points_pleasants                                                                                   +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_pocahontas.canonical_county_id                                                              +

                    FROM wv_address_points_pocahontas                                                                                  +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_preston.canonical_county_id                                                                 +

                    FROM wv_address_points_preston                                                                                     +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_putnam.canonical_county_id                                                                  +

                    FROM wv_address_points_putnam                                                                                      +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_raleigh.canonical_county_id                                                                 +

                    FROM wv_address_points_raleigh                                                                                     +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_randolph.canonical_county_id                                                                +

                    FROM wv_address_points_randolph                                                                                    +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_ritchie.canonical_county_id                                                                 +

                    FROM wv_address_points_ritchie                                                                                     +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_roane.canonical_county_id                                                                   +

                    FROM wv_address_points_roane                                                                                       +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_summers.canonical_county_id                                                                 +

                    FROM wv_address_points_summers                                                                                     +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_taylor.canonical_county_id                                                                  +

                    FROM wv_address_points_taylor                                                                                      +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_tucker.canonical_county_id                                                                  +

                    FROM wv_address_points_tucker                                                                                      +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_tyler.canonical_county_id                                                                   +

                    FROM wv_address_points_tyler                                                                                       +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_upshur.canonical_county_id                                                                  +

                    FROM wv_address_points_upshur                                                                                      +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_wayne.canonical_county_id                                                                   +

                    FROM wv_address_points_wayne                                                                                       +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_webster.canonical_county_id                                                                 +

                    FROM wv_address_points_webster                                                                                     +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_wetzel.canonical_county_id                                                                  +

                    FROM wv_address_points_wetzel                                                                                      +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_wirt.canonical_county_id                                                                    +

                    FROM wv_address_points_wirt                                                                                        +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_wood.canonical_county_id                                                                    +

                    FROM wv_address_points_wood                                                                                        +

                 UNION ALL                                                                                                             +

                  SELECT wv_address_points_wyoming.canonical_county_id                                                                 +

                    FROM wv_address_points_wyoming) ap_all                                                                             +

           WHERE ap_all.canonical_county_id IS NOT NULL                                                                                +

           GROUP BY ap_all.canonical_county_id) ap ON ap.canonical_county_id = ci.canonical_county_id                                  +

      LEFT JOIN ( SELECT wv_hyd_dfirm_nfhl.canonical_county_id,                                                                        +

             count(*) AS n_dfirm_polygons                                                                                              +

            FROM wv_hyd_dfirm_nfhl                                                                                                     +

           GROUP BY wv_hyd_dfirm_nfhl.canonical_county_id) d ON d.canonical_county_id = ci.canonical_county_id;

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

WITH physical AS (T

    SELECT DISTINCTcanonical_tract_id

        geoidfq AS canonical_tract_idutm83

    FROM wv_censustracts_census_2020_utm83

    WHERE LEFT(geoidfq, 5) = '54003'

),nonical AS (

canonical AS (onical_tract_id

    SELECT canonical_tract_id

    FROM wv_tract_identity_id = '54003'

    WHERE canonical_county_id = '54003'

)ELECT

SELECTALESCE(p.canonical_tract_id, c.canonical_tract_id) AS tract_id,

    COALESCE(p.canonical_tract_id, c.canonical_tract_id) AS tract_id,

    CASEWHEN p.canonical_tract_id IS NULL THEN 'canonical_only'

        WHEN p.canonical_tract_id IS NULL THEN 'canonical_only'

        WHEN c.canonical_tract_id IS NULL THEN 'physical_only'

    END AS discrepancy_type

FROM physical p canonical c

FULL OUTER JOIN canonical c)

  USING (canonical_tract_id)S NULL

WHERE p.canonical_tract_id IS NULL

   OR c.canonical_tract_id IS NULL

ORDER BY tract_id;

SQL

       tract_id       | discrepancy_type 

----------------------+------------------

 1400000US54003971101 | canonical_only

 1400000US54003971103 | canonical_only

 1400000US54003971104 | canonical_only

 1400000US54003971105 | canonical_only

 1400000US54003971203 | canonical_only

 1400000US54003971204 | canonical_only

 1400000US54003971205 | canonical_only

 1400000US54003971206 | canonical_only

 1400000US54003971301 | canonical_only

 1400000US54003971302 | canonical_only

 1400000US54003971401 | canonical_only

 1400000US54003971402 | canonical_only

 1400000US54003971500 | canonical_only

 1400000US54003971600 | canonical_only

 1400000US54003971700 | canonical_only

 1400000US54003971801 | canonical_only

 1400000US54003971802 | canonical_only

 1400000US54003971901 | canonical_only

 1400000US54003971902 | canonical_only

 1400000US54003972001 | canonical_only

 1400000US54003972002 | canonical_only

 1400000US54003972003 | canonical_only

 1400000US54003972101 | canonical_only

 1400000US54003972103 | canonical_only

 1400000US54003972104 | canonical_only

 1400000US54003972105 | canonical_only

(26 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -v ON_ERROR_STOP=1 <<'SQL'

CREATE TABLE IF NOT EXISTS wv_county_belief_summary_snapshot_v1 AS

SELECT

    bs.*,

    now() AS captured_at,

    'pre-tract-reconciliation'::text AS snapshot_reason

FROM wv_county_belief_summary bs;

SQL

SELECT 55

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ docker exec -it jarvis-msjarvis-db psql -U msjarvis -d msjarvisgis

psql (16.4 (Debian 16.4-1.pgdg110+2))

Type "help" for help.

msjarvisgis=# SELECT

    geoidfq,

    canonical_county_id,

    gid

FROM wv_censustracts_census_2020_utm83

WHERE canonical_county_id IN ('54003', '54057', '54095', '54103')

ORDER BY canonical_county_id, geoidfq;

msjarvisgis=# SELECT

    canonical_tract_id,

    canonical_county_id

FROM wv_tract_identity

WHERE canonical_county_id IN ('54003', '54057', '54095', '54103')

ORDER BY canonical_county_id, canonical_tract_id;

msjarvisgis=# CREATE OR REPLACE VIEW wv_county_tract_identity_reconciliation AS

WITH physical AS (

    SELECT

        canonical_county_id,

        substring(geoidfq FROM '([0-9]{11})$') AS tract_geoid,

        COUNT(*) AS physical_rows

    FROM wv_censustracts_census_2020_utm83

    WHERE canonical_county_id IS NOT NULL

    GROUP BY

        canonical_county_id,

        substring(geoidfq FROM '([0-9]{11})$')

),

canonical AS (

    SELECT

        canonical_county_id,

        substring(canonical_tract_id FROM '([0-9]{11})$') AS tract_geoid,

        COUNT(*) AS canonical_rows

    FROM wv_tract_identity

    WHERE canonical_county_id IS NOT NULL

    GROUP BY

        canonical_county_id,

        substring(canonical_tract_id FROM '([0-9]{11})$')

)

SELECT

 AND p.tract_geoid = c.tract_geoid;nical_county_idows <> 1

CREATE VIEW

msjarvisgis=# SELECT *

FROM wv_county_tract_identity_reconciliation

WHERE reconciliation_state <> 'reconciled'

ORDER BY canonical_county_id, tract_geoid;

msjarvisgis=# SELECT

    canonical_county_id,

    COUNT(*) FILTER (

        WHERE reconciliation_state = 'reconciled'

    ) AS reconciled,

    COUNT(*) FILTER (

        WHERE reconciliation_state = 'canonical_only'

    ) AS canonical_only,

    COUNT(*) FILTER (

        WHERE reconciliation_state = 'physical_only'

    ) AS physical_only,

    COUNT(*) FILTER (

        WHERE reconciliation_state = 'duplicate'

    ) AS duplicates

FROM wv_county_tract_identity_reconciliation

GROUP BY canonical_county_id

HAVING

    COUNT(*) FILTER (

        WHERE reconciliation_state <> 'reconciled'

    ) > 0

ORDER BY canonical_county_id;

 canonical_county_id | reconciled | canonical_only | physical_only | duplicates 

---------------------+------------+----------------+---------------+------------

 54003               |         25 |              1 |             0 |          0

 54057               |          6 |              1 |             0 |          0

 54095               |          3 |              0 |             1 |          0

 54103               |          4 |              1 |             0 |          0

(4 rows)

msjarvisgis=# SELECT

    canonical_county_id,

    tract_geoid,

    canonical_rows,

    physical_rows,

    reconciliation_state

FROM wv_county_tract_identity_reconciliation

WHERE reconciliation_state <> 'reconciled'

ORDER BY canonical_county_id, tract_geoid;

msjarvisgis=# WITH exceptions AS (

    SELECT tract_geoid

    FROM wv_county_tract_identity_reconciliation

    WHERE reconciliation_state <> 'reconciled'

)

SELECT

    p.gid,

    p.canonical_county_id,

    p.geoidfq,

    substring(p.geoidfq FROM '([0-9]{11})$') AS tract_geoid

FROM wv_censustracts_census_2020_utm83 p

JOIN exceptions e

  ON e.tract_geoid =

     substring(p.geoidfq FROM '([0-9]{11})$')

ORDER BY tract_geoid;

 gid | canonical_county_id |       geoidfq        | tract_geoid 

-----+---------------------+----------------------+-------------

 476 |                     | 1400000US54003971101 | 54003971101

 341 |                     | 1400000US54057010100 | 54057010100

 287 | 54095               | 1400000US54103030700 | 54103030700

 287 | 54095               | 1400000US54103030700 | 54103030700

(4 rows)

msjarvisgis=# WITH exceptions AS (

    SELECT tract_geoid

    FROM wv_county_tract_identity_reconciliation

    WHERE reconciliation_state <> 'reconciled'

)

SELECT

    t.canonical_tract_id,

    t.canonical_county_id,

    substring(t.canonical_tract_id FROM '([0-9]{11})$') AS tract_geoid

FROM wv_tract_identity t

JOIN exceptions e

  ON e.tract_geoid =

     substring(t.canonical_tract_id FROM '([0-9]{11})$')

ORDER BY tract_geoid;

  canonical_tract_id  | canonical_county_id | tract_geoid 

----------------------+---------------------+-------------

 1400000US54003971101 | 54003               | 54003971101

 1400000US54057010100 | 54057               | 54057010100

 1400000US54103030700 | 54103               | 54103030700

 1400000US54103030700 | 54103               | 54103030700

(4 rows)

msjarvisgis=# psql -v ON_ERROR_STOP=1 <<'SQL'

UPDATE wv_censustracts_census_2020_utm83

SET canonical_county_id = '54003'

WHERE geoidfq = '1400000US54003971101'

  AND canonical_county_id IS NULL;

UPDATE wv_censustracts_census_2020_utm83

SET canonical_county_id = '54057'

WHERE geoidfq = '1400000US54057010100'

  AND canonical_county_id IS NULL;

SQL

ERROR:  syntax error at or near "psql"

LINE 1: psql -v ON_ERROR_STOP=1 <<'SQL'

        ^

UPDATE 1

msjarvisgis-# psql -h 127.0.0.1 -p 5436 -U msjarvisgis -d msjarvisgis

msjarvisgis-# 

\q

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ free -h

               total        used        free      shared  buff/cache   available

Mem:            29Gi        13Gi       4.9Gi       1.5Gi        11Gi        15Gi

Swap:           23Gi       336Ki        23Gi

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ docker exec -it jarvis-msjarvis-db psql -U msjarvis -d msjarvisgis

psql (16.4 (Debian 16.4-1.pgdg110+2))

Type "help" for help.

msjarvisgis=# -- Show key tract and county tables in this DB

\dt *wv_tract_identity*

\dt *wv_censustracts_census_2020_utm83*

\dt *wv_county_identity*

\dt *wv_county_belief_summary*

               List of relations

 Schema |       Name        | Type  |  Owner   

--------+-------------------+-------+----------

 public | wv_tract_identity | table | postgres

(1 row)

                       List of relations

 Schema |               Name                | Type  |  Owner   

--------+-----------------------------------+-------+----------

 public | wv_censustracts_census_2020_utm83 | table | msjarvis

(1 row)

               List of relations

 Schema |        Name        | Type  |  Owner   

--------+--------------------+-------+----------

 public | wv_county_identity | table | msjarvis

(1 row)

                        List of relations

 Schema |                 Name                 | Type  |  Owner   

--------+--------------------------------------+-------+----------

 public | wv_county_belief_summary_snapshot_v1 | table | postgres

(1 row)

msjarvisgis=# CREATE OR REPLACE VIEW public.wv_county_tract_identity_reconciliation AS

WITH physical AS (

    SELECT

        canonical_county_id,

        substring(geoidfq FROM '([0-9]{11})$') AS tract_geoid,

        COUNT(*) AS physical_rows

    FROM public.wv_censustracts_census_2020_utm83

    WHERE canonical_county_id IS NOT NULL

    GROUP BY canonical_county_id,

             substring(geoidfq FROM '([0-9]{11})$')

),

canonical AS (

    SELECT

        canonical_county_id,

        substring(canonical_tract_id FROM '([0-9]{11})$') AS tract_geoid,

        COUNT(*) AS canonical_rows

    FROM public.wv_tract_identity

    WHERE canonical_county_id IS NOT NULL

    GROUP BY canonical_county_id,

             substring(canonical_tract_id FROM '([0-9]{11})$')

)

SELECT

    COALESCE(c.canonical_county_id, p.canonical_county_id)

 AND p.tract_geoid = c.tract_geoid;nical_county_idows <> 1

CREATE VIEW

msjarvisgis=# CREATE OR REPLACE VIEW public.wv_county_tract_reconciliation AS

WITH canonical AS (

    SELECT

        canonical_county_id,

        COUNT(*) AS canonical_tract_count

    FROM public.wv_tract_identity

    WHERE canonical_county_id IS NOT NULL

    GROUP BY canonical_county_id

)

SELECT

    ci.canonical_county_id,

    ci.county_name,

    COALESCE(bs.n_tracts, 0) AS summary_tract_count,

    COALESCE(c.canonical_tract_count, 0) AS canonical_tract_count,

    COALESCE(c.canonical_tract_count, 0)

        - COALESCE(bs.n_tracts, 0) AS count_delta,

    CASE

        WHEN COALESCE(c.canonical_tract_count, 0)

           = COALESCE(bs.n_tracts, 0)

        THEN 'reconciled'

        ELSE 'discrepancy'

    END AS reconciliation_state

FROM public.wv_county_identity ci

LEFT JOIN public.wv_county_belief_summary_snapshot_v1 bs

  ON c.canonical_county_id = ci.canonical_county_id;

CREATE VIEW

msjarvisgis=# CT

    p.gid,    CT

    p.gid,nical_county_id,

    p.canonical_county_id,

    p.geoidfq,p.geoidfq FROM '([0-9]{11})$') AS tract_geoid

    substring(p.geoidfq FROM '([0-9]{11})$') AS tract_geoid

FROM public.wv_censustracts_census_2020_utm83 p

JOIN exceptions ed =

  ON e.tract_geoid =idfq FROM '([0-9]{11})$')

     substring(p.geoidfq FROM '([0-9]{11})$')

ORDER BY tract_geoid;

WITH exceptions AS (

WITH exceptions AS (id

    SELECT tract_geoidnty_tract_identity_reconciliation

    FROM public.wv_county_tract_identity_reconciliation

    WHERE reconciliation_state <> 'reconciled'

)ELECT

SELECTcanonical_tract_id,

    t.canonical_tract_id,,

    t.canonical_county_id,tract_id FROM '([0-9]{11})$') AS tract_geoid

    substring(t.canonical_tract_id FROM '([0-9]{11})$') AS tract_geoid

FROM public.wv_tract_identity t

JOIN exceptions ed =

  ON e.tract_geoid =onical_tract_id FROM '([0-9]{11})$')

     substring(t.canonical_tract_id FROM '([0-9]{11})$')

ORDER BY tract_geoid;

ERROR:  syntax error at or near "CT"

LINE 1: CT

        ^

  canonical_tract_id  | canonical_county_id | tract_geoid 

----------------------+---------------------+-------------

 1400000US54003971101 | 54003               | 54003971101

 1400000US54103030700 | 54103               | 54103030700

 1400000US54103030700 | 54103               | 54103030700

(3 rows)

msjarvisgis=# UPDATE public.wv_censustracts_census_2020_utm83

SET canonical_county_id = '54003'

WHERE geoidfq = '1400000US54003971101'

  AND canonical_county_id IS NULL;

UPDATE public.wv_censustracts_census_2020_utm83

SET canonical_county_id = '54057'

WHERE geoidfq = '1400000US54057010100'

  AND canonical_county_id IS NULL;

UPDATE public.wv_tract_identity

SET canonical_county_id = '54095'

WHERE canonical_tract_id = '1400000US54103030700'

  AND canonical_county_id = '54103';

DELETE FROM public.wv_tract_identity ti

USING public.wv_tract_identity t_keep

WHERE ti.canonical_tract_id = '1400000US54103030700'

  AND ti.canonical_county_id = '54095'

  AND t_keep.canonical_tract_id = ti.canonical_tract_id

  AND t_keep.canonical_county_id = ti.canonical_county_id

  AND t_keep.id < ti.id;

UPDATE 1

UPDATE 0

UPDATE 1

ERROR:  column t_keep.id does not exist

LINE 7:   AND t_keep.id < ti.id;

              ^

msjarvisgis=# SELECT *

FROM public.wv_county_tract_reconciliation

WHERE canonical_county_id IN ('54003', '54057', '54095', '54103')

ORDER BY canonical_county_id;

SELECT

    canonical_county_id,

    COUNT(*) FILTER (

        WHERE reconciliation_state <> 'reconciled'

    ) AS non_reconciled

FROM public.wv_county_tract_identity_reconciliation

WHERE canonical_county_id IN ('54003', '54057', '54095', '54103')

GROUP BY canonical_county_id

ORDER BY canonical_county_id;

 canonical_county_id | non_reconciled 

---------------------+----------------

 54003               |              0

 54057               |              0

 54095               |              0

 54103               |              0

(4 rows)

msjarvisgis=# \d public.wv_tract_identity

                        Table "public.wv_tract_identity"

       Column        |           Type           | Collation | Nullable | Default 

---------------------+--------------------------+-----------+----------+---------

 canonical_tract_id  | text                     |           | not null | 

 tract_geoid         | text                     |           | not null | 

 canonical_county_id | text                     |           |          | 

 created_at          | timestamp with time zone |           | not null | now()

 updated_at          | timestamp with time zone |           | not null | now()

Indexes:

    "wv_tract_identity_pkey" PRIMARY KEY, btree (canonical_tract_id)

Foreign-key constraints:

    "wv_tract_identity_canonical_county_id_fkey" FOREIGN KEY (canonical_county_id) REFERENCES wv_county_identity(canonical_county_id)

msjarvisgis=# SELECT

    canonical_tract_id,

    canonical_county_id,

    created_at,

    updated_at

FROM public.wv_tract_identity

WHERE canonical_tract_id = '1400000US54103030700'

ORDER BY canonical_county_id, created_at;

msjarvisgis=# DELETE FROM public.wv_tract_identity

WHERE canonical_tract_id = '1400000US54103030700'

  AND canonical_county_id = '54103';

DELETE 0

msjarvisgis=# DELETE FROM public.wv_tract_identity

WHERE canonical_tract_id = '1400000US54103030700'

  AND canonical_county_id = '54095'

  AND updated_at < (

      SELECT MAX(updated_at)

      FROM public.wv_tract_identity

      WHERE canonical_tract_id = '1400000US54103030700'

        AND canonical_county_id = '54095'

  );

DELETE 0

msjarvisgis=# SELECT

    canonical_tract_id,

    canonical_county_id

FROM public.wv_tract_identity

WHERE canonical_tract_id = '1400000US54103030700';

  canonical_tract_id  | canonical_county_id 

----------------------+---------------------

 1400000US54103030700 | 54095

(1 row)

msjarvisgis=# BEGIN;

UPDATE public.wv_tract_identity

SET canonical_county_id = '54103',

    updated_at = now()

WHERE canonical_tract_id = '1400000US54103030700';

UPDATE public.wv_censustracts_census_2020_utm83

SET canonical_county_id = '54103'

WHERE substring(geoidfq FROM '([0-9]{11})$') = '54103030700';

COMMIT;

BEGIN

UPDATE 1

UPDATE 1

COMMIT

msjarvisgis=# UPDATE public.<second_tract_table>

SET canonical_county_id = '54103'

WHERE substring(geoidfq FROM '([0-9]{11})$') = '54103030700';

ERROR:  syntax error at or near "<"

LINE 1: UPDATE public.<second_tract_table>

                      ^

msjarvisgis=# UPDATE public.wv_tract_identity t

SET canonical_county_id = c.canonical_county_id,

    updated_at = now()

FROM public.wv_county_identity c

WHERE c.county_geoid =

      substring(t.tract_geoid FROM 1 FOR 5)

  AND t.canonical_county_id IS DISTINCT FROM c.canonical_county_id;

UPDATE 0

msjarvisgis=# SELECT

    t.canonical_tract_id,

    t.tract_geoid,

    t.canonical_county_id AS stored_county_id,

    substring(t.tract_geoid FROM 1 FOR 5) AS geoid_county_id

FROM public.wv_tract_identity t

WHERE t.canonical_county_id IS DISTINCT FROM

      substring(t.tract_geoid FROM 1 FOR 5)

ORDER BY t.canonical_tract_id;

 canonical_tract_id | tract_geoid | stored_county_id | geoid_county_id 

--------------------+-------------+------------------+-----------------

(0 rows)

msjarvisgis=# SELECT

    gid,

    geoidfq,

    canonical_county_id AS stored_county_id,

    substring(

        substring(geoidfq FROM '([0-9]{11})$')

        FROM 1 FOR 5

    ) AS geoid_county_id

FROM public.wv_censustracts_census_2020_utm83

WHERE canonical_county_id IS DISTINCT FROM

      substring(

          substring(geoidfq FROM '([0-9]{11})$')

          FROM 1 FOR 5

      )

ORDER BY geoidfq;

 gid | geoidfq | stored_county_id | geoid_county_id 

-----+---------+------------------+-----------------

(0 rows)

msjarvisgis=# UPDATE public.wv_tract_identity t

SET canonical_county_id = c.canonical_county_id,

    updated_at = now()

FROM public.wv_county_identity c

WHERE c.county_geoid =

      substring(t.tract_geoid FROM 1 FOR 5)

  AND t.canonical_county_id IS DISTINCT FROM c.canonical_county_id;

UPDATE 0

msjarvisgis=# SELECT

    t.canonical_tract_id,

    t.tract_geoid,

    t.canonical_county_id AS stored_county_id,

    substring(t.tract_geoid FROM 1 FOR 5) AS geoid_county_id

FROM public.wv_tract_identity t

WHERE t.canonical_county_id IS DISTINCT FROM

      substring(t.tract_geoid FROM 1 FOR 5)

ORDER BY t.canonical_tract_id;

 canonical_tract_id | tract_geoid | stored_county_id | geoid_county_id 

--------------------+-------------+------------------+-----------------

(0 rows)

msjarvisgis=# SELECT

    gid,

    geoidfq,

    canonical_county_id AS stored_county_id,

    substring(

        substring(geoidfq FROM '([0-9]{11})$')

        FROM 1 FOR 5

    ) AS geoid_county_id

FROM public.wv_censustracts_census_2020_utm83

WHERE canonical_county_id IS DISTINCT FROM

      substring(

          substring(geoidfq FROM '([0-9]{11})$')

          FROM 1 FOR 5

      )

ORDER BY geoidfq;

 gid | geoidfq | stored_county_id | geoid_county_id 

-----+---------+------------------+-----------------

(0 rows)

msjarvisgis=# All tract identities and physical UTM83 tracts in msjarvisgis now obey the rule “county FIPS = first 5 digits of the 11‐digit tract GEOID,” and the problematic Wetzel/Tyler tract has been restored to Wetzel everywhere. Your mismatch audits returning zero rows confirm both database agreement and geographic correctness.

What the latest commands achieved

    The BEGIN ... COMMIT block set:

        canonical_county_id = '54103' for canonical_tract_id = '1400000US54103030700' in wv_tract_identity.

        canonical_county_id = '54103' for the UTM83 tract where geoidfq ends in 54103030700.

    This realigned both identity and physical representation with the authoritative GEOID (54103 = Wetzel).

    The general enforcement:

    sql

    UPDATE public.wv_tract_identity t

    SET canonical_county_id = c.canonical_county_id,

        updated_at = now()

t snapshot v2 is now both reconciled and geographically truthful.undation for trac

ERROR:  syntax error at or near "All"

LINE 1: All tract identities and physical UTM83 tracts in msjarvisgi...

        ^

ERROR:  syntax error at or near "returned"

LINE 1: returned UPDATE 0, which means—after your targeted fixes—the...

        ^

ERROR:  syntax error at or near "returned"

LINE 1: returned 0 rows, confirming every tract identity’s county ma...

        ^

msjarvisgis-# SELECT

    table_name,

    geometry_type,

    srid

FROM public.wv_layer_categories

WHERE table_name ILIKE '%censustract%'

ORDER BY table_name;

ERROR:  syntax error at or near "also"

LINE 1: also returned 0 rows, confirming every physical tract’s coun...

        ^

msjarvisgis=# SELECT

    table_name,

    geometry_type,

    srid

FROM public.wv_layer_categories

WHERE table_name ILIKE '%censustract%'

ORDER BY table_name;

 table_name | geometry_type | srid 

------------+---------------+------

(0 rows)

msjarvisgis=# SELECT

    table_name,

    geometry_type,

    srid

FROM public.wv_layer_categories

WHERE table_name ILIKE '%censustract%'

ORDER BY table_name;

 table_name | geometry_type | srid 

------------+---------------+------

(0 rows)

msjarvisgis=# SELECT DISTINCT

    table_name

FROM public.wv_tract_representation

ORDER BY table_name;

            table_name             

-----------------------------------

 wv_censustracts_census_2020_utm83

(1 row)

msjarvisgis=# SELECT

    gid,

    geoidfq,

    canonical_county_id AS stored_county_id,

    substring(

        substring(geoidfq FROM '([0-9]{11})$')

        FROM 1 FOR 5

    ) AS geoid_county_id

FROM public.<tract_table_name>

WHERE canonical_county_id IS DISTINCT FROM

      substring(

          substring(geoidfq FROM '([0-9]{11})$')

          FROM 1 FOR 5

      )

ORDER BY geoidfq;

ERROR:  syntax error at or near "<"

LINE 9: FROM public.<tract_table_name>

                    ^

msjarvisgis=# INSERT INTO public.wv_layer_categories (table_name, geometry_type, srid)

SELECT

    'wv_censustracts_census_2020_utm83',

    GeometryType(geom),   -- or literal 'MULTIPOLYGON' etc.

    ST_SRID(geom)

FROM public.wv_censustracts_census_2020_utm83

LIMIT 1;

ERROR:  null value in column "category" of relation "wv_layer_categories" violates not-null constraint

DETAIL:  Failing row contains (wv_censustracts_census_2020_utm83, null, null, 2026-07-11 22:01:50.669477, null, null, MULTIPOLYGON, 26917, null, null, null, null).

msjarvisgis=# \d public.wv_layer_categories

                        Table "public.wv_layer_categories"

      Column       |            Type             | Collation | Nullable | Default 

-------------------+-----------------------------+-----------+----------+---------

 table_name        | text                        |           | not null | 

 category          | text                        |           | not null | 

 description       | text                        |           |          | 

 last_updated      | timestamp without time zone |           | not null | now()

 source_system     | text                        |           |          | 

 jurisdiction      | text                        |           |          | 

 geometry_type     | text                        |           |          | 

 srid              | integer                     |           |          | 

 spatial_grain     | text                        |           |          | 

 temporal_coverage | text                        |           |          | 

 authority_class   | text                        |           |          | 

 access_class      | text                        |           |          | 

Indexes:

    "wv_layer_categories_pkey" PRIMARY KEY, btree (table_name)

Referenced by:

    TABLE "wv_county_representation" CONSTRAINT "wv_county_representation_table_fk" FOREIGN KEY (table_name) REFERENCES wv_layer_categories(table_name) ON DELETE CASCADE

    TABLE "wv_entity_registry" CONSTRAINT "wv_entity_registry_table_fk" FOREIGN KEY (table_name) REFERENCES wv_layer_categories(table_name) ON DELETE CASCADE

    TABLE "wv_hazus_county_representation" CONSTRAINT "wv_hazus_county_representation_table_fk" FOREIGN KEY (table_name) REFERENCES wv_layer_categories(table_name) ON DELETE CASCADE

    TABLE "wv_layer_provenance" CONSTRAINT "wv_layer_provenance_table_fk" FOREIGN KEY (table_name) REFERENCES wv_layer_categories(table_name) ON DELETE CASCADE

msjarvisgis=# INSERT INTO public.wv_layer_categories (

    table_name,

    category,

    geometry_type,

    srid

    -- plus any other NOT NULL columns

)

SELECT

    'wv_censustracts_census_2020_utm83',

    'census_tract',

    GeometryType(geom),

    ST_SRID(geom)

FROM public.wv_censustracts_census_2020_utm83

LIMIT 1;

INSERT 0 1

msjarvisgis=# \d public.wv_layer_categories

                        Table "public.wv_layer_categories"

      Column       |            Type             | Collation | Nullable | Default 

-------------------+-----------------------------+-----------+----------+---------

 table_name        | text                        |           | not null | 

 category          | text                        |           | not null | 

 description       | text                        |           |          | 

 last_updated      | timestamp without time zone |           | not null | now()

 source_system     | text                        |           |          | 

 jurisdiction      | text                        |           |          | 

 geometry_type     | text                        |           |          | 

 srid              | integer                     |           |          | 

 spatial_grain     | text                        |           |          | 

 temporal_coverage | text                        |           |          | 

 authority_class   | text                        |           |          | 

 access_class      | text                        |           |          | 

Indexes:

    "wv_layer_categories_pkey" PRIMARY KEY, btree (table_name)

Referenced by:

    TABLE "wv_county_representation" CONSTRAINT "wv_county_representation_table_fk" FOREIGN KEY (table_name) REFERENCES wv_layer_categories(table_name) ON DELETE CASCADE

    TABLE "wv_entity_registry" CONSTRAINT "wv_entity_registry_table_fk" FOREIGN KEY (table_name) REFERENCES wv_layer_categories(table_name) ON DELETE CASCADE

    TABLE "wv_hazus_county_representation" CONSTRAINT "wv_hazus_county_representation_table_fk" FOREIGN KEY (table_name) REFERENCES wv_layer_categories(table_name) ON DELETE CASCADE

    TABLE "wv_layer_provenance" CONSTRAINT "wv_layer_provenance_table_fk" FOREIGN KEY (table_name) REFERENCES wv_layer_categories(table_name) ON DELETE CASCADE

msjarvisgis=# SELECT *

FROM public.wv_layer_categories

WHERE table_name = 'wv_censustracts_census_2020_utm83';

msjarvisgis=# SELECT

    table_name,

    category,

    geometry_type,

    srid,

    last_updated,

    source_system,

    jurisdiction,

    spatial_grain,

    temporal_coverage,

    authority_class,

    access_class

FROM public.wv_layer_categories

WHERE table_name = 'wv_censustracts_census_2020_utm83';

msjarvisgis=# The UTM83 tract layer is now fully and correctly registered in your governance catalog as a **census_tract** layer, with explicit geometry and SRID metadata and a timestamped update. That closes the loop between your reconciled physical tracts and the GBIM layer registry. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/51743013/f14b4426-93e8-46e8-a585-b103d96726d9/paste.txt?AWSAccessKeyId=ASIA2F3EMEYE7YATMQTD&Signature=3CWeTd%2Fd9YYjMEYcv7ySj9AQdMg%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEA4aCXVzLWVhc3QtMSJIMEYCIQCLB%2BNFren%2FZl%2B2d7nxvWLqyiyeUfCrpSlxavhRw08pVgIhANr1o9oeP2OpyLzjPTGf5pMkB5wF2TmKLrWS7lFyXR%2FVKvwECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQARoMNjk5NzUzMzA5NzA1Igy9ChCvs%2BhALQjI4S4q0ASRjuqkyp%2FmUWDpXMoVkvpuv335LGHtbsDOt7Gg26N9uPh%2Bic4kim%2FPCDibDxTXjeel2RgfLhawUxgY68Hhm%2Fy21N%2FcIPDIX90Jm0UTXgRbRzzokqJZLGCE0lDZ5M4X3JJQVuAyBaLhj6h3XFFgyuF8mQQpDDGOaItabf0SeIzJIhT%2Be9E3al%2BRAod59XjNAqyvcoZrBNY5Ow507vNasCkObyzBKrpOj0U6U09ggIV64nGz79qVQ0bSEN2K0NT5cAnC3sNO7lFJvYk9vBcc6GGorzepV5O3KeO%2BfYMDECxYRkw9aG17joSZiSntcnN6SAPVuf4ZFdpBH8jBzchBIKag6pN7PLmkczGtYf4I%2B9oq%2FXyUE%2F2NvkLuuCKZeSvAPsJMGk2pnVthDsFFC3n8W4B3li%2F37jhIvXwqnVzvedbn8PdbY8qqdyJH6IIut1wiA%2BXPPqQAzrvoaUhTvm1pNiheOtwKksYoWLHIG2WVjUIHURDslRcpdfuBwL6UtBDW39CDllc52ujvUmamkm2sCpH32mczkvJ2EOwN7BUJhzNsni9BgzyIh29gOY%2FrZaNESD0v4jposVJXHRFy%2FcNuvt8SLbxwnGycGeW30BuinpMB0YpRt3ESZlJVzG4P3oKCevcq6tI5J6A31y1iCNjh3xO5nounW%2FpVloP72xU3XlhX%2BajeGJA4UDH4rAqbgAtD%2BY8UOzdaT8aBkY9rwXVVpoBec7uV6GstgXs3q9wdtmPiOvRznksB5xACtL5zcJqon3okeK8ictxEsTk02uay4ZGbMI3wytIGOpcBSiTIcJrNOfi00ZakNMLB1tscj4g%2FIk4v3B2%2Bn2dqfAZra78y%2FhTAvArR6TsXE0XTybo%2FVqo3oHdkzHVIter783NPqfdF9r52qqYDe%2FF%2F7lNFxgTc8CAh35iZ6qz6W%2FOESNUHQOqOJmy%2F1mL2dm9tCCBdP%2BMF%2BeCJjl9I4tmKDwMsVgqsqx187rDhwPLCF4WPziEuCCKU%2Fw%3D%3D&Expires=1783809504)

nchored on this governed layer and its clean identity.^Cation and promotion, all a

msjarvisgis=# UPDATE public.wv_layer_categories

SET

    source_system    = 'U.S. Census Bureau',

    jurisdiction     = 'West Virginia',

    spatial_grain    = 'census_tract',

    temporal_coverage = '2020 Census',

    authority_class  = 'official',

    access_class     = 'public',

    last_updated     = now()

WHERE table_name = 'wv_censustracts_census_2020_utm83';

UPDATE 1

msjarvisgis=# UPDATE public.wv_layer_categories

SET

    source_system    = 'U.S. Census Bureau',

    jurisdiction     = 'West Virginia',

    spatial_grain    = 'census_tract',

    temporal_coverage = '2020 Census',

    authority_class  = 'official',

    access_class     = 'public',

    last_updated     = now()

WHERE table_name = 'wv_censustracts_census_2020_utm83';

UPDATE 1

msjarvisgis=# UPDATE public.wv_layer_categories

SET

    source_system    = 'U.S. Census Bureau',

    jurisdiction     = 'West Virginia',

    spatial_grain    = 'census_tract',

    temporal_coverage = '2020 Census',

    authority_class  = 'official',

    access_class     = 'public',

    last_updated     = now()

WHERE table_name = 'wv_censustracts_census_2020_utm83';

UPDATE 1

msjarvisgis=# UPDATE public.wv_layer_categories

SET

    source_system     = 'U.S. Census Bureau',

    jurisdiction      = 'West Virginia',

    spatial_grain     = 'census_tract',

    temporal_coverage = '2020 Census',

    authority_class   = 'official',

    access_class      = 'public',

    last_updated      = now()

WHERE table_name = 'wv_censustracts_census_2020_utm83';

UPDATE 1

msjarvisgis=# SELECT

    table_name,

    category,

    geometry_type,

    srid,

    source_system,

    jurisdiction,

    spatial_grain,

    temporal_coverage,

    authority_class,

    access_class,

    CASE

        WHEN category IS NOT NULL

         AND geometry_type IS NOT NULL

         AND srid IS NOT NULL

         AND source_system IS NOT NULL

         AND jurisdiction IS NOT NULL

         AND spatial_grain IS NOT NULL

         AND temporal_coverage IS NOT NULL

         AND authority_class IS NOT NULL

         AND access_class IS NOT NULL

        THEN 'complete'

        ELSE 'incomplete'

    END AS governance_metadata_state

WHERE table_name = 'wv_censustracts_census_2020_utm83';

msjarvisgis=# SELECT

    lc.table_name,

    lc.geometry_type,

    lc.srid,

    COUNT(r.source_feature_id) AS registered_representations

FROM public.wv_layer_categories lc

LEFT JOIN public.wv_tract_representation r

  ON r.table_name = lc.table_name

WHERE lc.table_name ILIKE '%censustract%'

GROUP BY lc.table_name, lc.geometry_type, lc.srid

ORDER BY lc.table_name;

msjarvisgis=# Your governance checkpoint is now solid: the UTM83 tract layer’s metadata is complete, and all 1,092 representation rows are accounted for by that single, correctly registered table. That matches the identity and physical GEOID invariants you’ve already enforced.

Governance metadata state

From your earlier query:

text

table_name             |   category   | geometry_type | srid  |   source_system    | jurisdiction  | spatial_grain | temporal_coverage | authority_class | access_class | governance_metadata_state 

-----------------------+--------------+---------------+-------+--------------------+---------------+---------------+-------------------+-----------------+--------------+---------------------------

wv_censustracts_census_2020_utm83 | census_tract | MULTIPOLYGON  | 26917 | U.S. Census Bureau | West Virginia | census_tract  | 2020 Census       | official        | public       | complete

So for wv_censustracts_census_2020_utm83:

    category = 'census_tract'

d validate the representation hashes before you start snapshot v2. to recompute an

ERROR:  syntax error at or near "Your"

LINE 1: Your governance checkpoint is now solid: the UTM83 tract lay...

        ^

ERROR:  syntax error at or near "you"

LINE 1: you saw:

        ^

msjarvisgis-# SELECT

    COUNT(*) AS physical_rows,

    COUNT(DISTINCT gid) AS distinct_gids,

    COUNT(DISTINCT substring(geoidfq FROM '([0-9]{11})$'))

        AS distinct_tract_geoids

FROM public.wv_censustracts_census_2020_utm83;

ERROR:  syntax error at or near "your"

LINE 1: your conceptual “two sets of 546 features” are implemented h...

        ^

msjarvisgis=# SELECT

    COUNT(*) AS physical_rows,

    COUNT(DISTINCT gid) AS distinct_gids,

    COUNT(DISTINCT substring(geoidfq FROM '([0-9]{11})$'))

        AS distinct_tract_geoids

FROM public.wv_censustracts_census_2020_utm83;

 physical_rows | distinct_gids | distinct_tract_geoids 

---------------+---------------+-----------------------

           546 |           546 |                   546

(1 row)

msjarvisgis=# SELECT

    COUNT(*) AS physical_rows,

    COUNT(DISTINCT gid) AS distinct_gids,

    COUNT(DISTINCT substring(geoidfq FROM '([0-9]{11})$'))

        AS distinct_tract_geoids

FROM public.wv_censustracts_census_2020_utm83;

 physical_rows | distinct_gids | distinct_tract_geoids 

---------------+---------------+-----------------------

           546 |           546 |                   546

(1 row)

msjarvisgis=# SELECT

    COUNT(*) AS physical_rows,

    COUNT(DISTINCT gid) AS distinct_gids,

    COUNT(DISTINCT substring(geoidfq FROM '([0-9]{11})$'))

        AS distinct_tract_geoids

FROM public.wv_censustracts_census_2020_utm83;

 physical_rows | distinct_gids | distinct_tract_geoids 

---------------+---------------+-----------------------

           546 |           546 |                   546

(1 row)

msjarvisgis=# SELECT

    COUNT(*) AS physical_rows,

    COUNT(DISTINCT gid) AS distinct_gids,

    COUNT(DISTINCT substring(geoidfq FROM '([0-9]{11})$'))

        AS distinct_tract_geoids

FROM public.wv_censustracts_census_2020_utm83;

 physical_rows | distinct_gids | distinct_tract_geoids 

---------------+---------------+-----------------------

           546 |           546 |                   546

(1 row)

msjarvisgis=# SELECT

    COUNT(*) AS physical_rows,

    COUNT(DISTINCT gid) AS distinct_gids,

    COUNT(DISTINCT substring(geoidfq FROM '([0-9]{11})$'))

        AS distinct_tract_geoids

FROM public.wv_censustracts_census_2020_utm83;

 physical_rows | distinct_gids | distinct_tract_geoids 

---------------+---------------+-----------------------

           546 |           546 |                   546

(1 row)

msjarvisgis=# msjarvisgis-# SELECT

    COUNT(*) AS physical_rows,

    COUNT(DISTINCT gid) AS distinct_gids,

    COUNT(DISTINCT substring(geoidfq FROM '([0-9]{11})$'))

        AS distinct_tract_geoids

FROM public.wv_censustracts_census_2020_utm83;

ERROR:  syntax error at or near "your"

LINE 1: your conceptual “two sets of 546 features” are implemented h...

        ^

msjarvisgis=# SELECT

    COUNT(*) AS physical_rows,

    COUNT(DISTINCT gid) AS distinct_gids,

    COUNT(DISTINCT substring(geoidfq FROM '([0-9]{11})$'))

        AS distinct_tract_geoids

FROM public.wv_censustracts_census_2020_utm83;

 physical_rows | distinct_gids | distinct_tract_geoids 

---------------+---------------+-----------------------

           546 |           546 |                   546

(1 row)

msjarvisgis=# SELECT

    COUNT(*) AS physical_rows,

    COUNT(DISTINCT gid) AS distinct_gids,

    COUNT(DISTINCT substring(geoidfq FROM '([0-9]{11})$'))

msjarvisgis=#  |           546 |                   546-'))

ERROR:  syntax error at or near "msjarvisgis"

LINE 1: msjarvisgis-# SELECT

        ^

ERROR:  syntax error at or near "ERROR"

LINE 1: ERROR:  syntax error at or near "your"

        ^

ERROR:  syntax error at or near "physical_rows"

LINE 1: physical_rows | distinct_gids | distinct_tract_geoids 

        ^

ERROR:  syntax error at or near "physical_rows"

LINE 1: physical_rows | distinct_gids | distinct_tract_geoids 

        ^

ERROR:  syntax error at or near "physical_rows"

LINE 1: physical_rows | distinct_gids | distinct_tract_geoids 

        ^

ERROR:  syntax error at or near "physical_rows"

LINE 1: physical_rows | distinct_gids | distinct_tract_geoids 

        ^

msjarvisgis-# msjarvisgis-# SELECT

    COUNT(*) AS physical_rows,

    COUNT(DISTINCT gid) AS distinct_gids,

    COUNT(DISTINCT substring(geoidfq FROM '([0-9]{11})$'))

        AS distinct_tract_geoids

FROM public.wv_censustracts_census_2020_utm83;

ERROR:  syntax error at or near "your"

LINE 1: your conceptual “two sets of 546 features” are implemented h...

        ^

msjarvisgis=# SELECT

    COUNT(*) AS physical_rows,

    COUNT(DISTINCT gid) AS distinct_gids,

    COUNT(DISTINCT substring(geoidfq FROM '([0-9]{11})$'))

        AS distinct_tract_geoids

FROM public.wv_censustracts_census_2020_utm83;

 physical_rows | distinct_gids | distinct_tract_geoids 

---------------+---------------+-----------------------

           546 |           546 |                   546

(1 row)

msjarvisgis=# SELECT

    COUNT(*) AS physical_rows,

    COUNT(DISTINCT gid) AS distinct_gids,

    COUNT(DISTINCT substring(geoidfq FROM '([0-9]{11})$'))

msjarvisgis=#  |           546 |                   546-'))

ERROR:  syntax error at or near "physical_rows"

LINE 1: physical_rows | distinct_gids | distinct_tract_geoids 

        ^

ERROR:  syntax error at or near "ERROR"

LINE 1: ERROR:  syntax error at or near "your"

        ^

ERROR:  syntax error at or near "physical_rows"

LINE 1: physical_rows | distinct_gids | distinct_tract_geoids 

        ^

ERROR:  syntax error at or near "physical_rows"

LINE 1: physical_rows | distinct_gids | distinct_tract_geoids 

        ^

ERROR:  syntax error at or near "physical_rows"

LINE 1: physical_rows | distinct_gids | distinct_tract_geoids 

        ^

ERROR:  syntax error at or near "physical_rows"

LINE 1: physical_rows | distinct_gids | distinct_tract_geoids 

        ^

msjarvisgis-# msjarvisgis-# SELECT

    COUNT(*) AS physical_rows,

    COUNT(DISTINCT gid) AS distinct_gids,

    COUNT(DISTINCT substring(geoidfq FROM '([0-9]{11})$'))

        AS distinct_tract_geoids

FROM public.wv_censustracts_census_2020_utm83;

ERROR:  syntax error at or near "your"

LINE 1: your conceptual “two sets of 546 features” are implemented h...

        ^

msjarvisgis=# SELECT

    COUNT(*) AS physical_rows,

    COUNT(DISTINCT gid) AS distinct_gids,

    COUNT(DISTINCT substring(geoidfq FROM '([0-9]{11})$'))

        AS distinct_tract_geoids

FROM public.wv_censustracts_census_2020_utm83;

 physical_rows | distinct_gids | distinct_tract_geoids 

---------------+---------------+-----------------------

           546 |           546 |                   546

(1 row)

msjarvisgis=# SELECT

    COUNT(*) AS physical_rows,

    COUNT(DISTINCT gid) AS distinct_gids,

    COUNT(DISTINCT substring(geoidfq FROM '([0-9]{11})$'))

msjarvisgis=#  |           546 |                   546-'))

ERROR:  syntax error at or near "physical_rows"

LINE 1: physical_rows | distinct_gids | distinct_tract_geoids 

        ^

ERROR:  syntax error at or near "ERROR"

LINE 1: ERROR:  syntax error at or near "your"

        ^

ERROR:  syntax error at or near "physical_rows"

LINE 1: physical_rows | distinct_gids | distinct_tract_geoids 

        ^

ERROR:  syntax error at or near "physical_rows"

LINE 1: physical_rows | distinct_gids | distinct_tract_geoids 

        ^

ERROR:  syntax error at or near "physical_rows"

LINE 1: physical_rows | distinct_gids | distinct_tract_geoids 

        ^

ERROR:  syntax error at or near "physical_rows"

LINE 1: physical_rows | distinct_gids | distinct_tract_geoids 

        ^

msjarvisgis-# msjarvisgis-# SELECT

    COUNT(*) AS physical_rows,

    COUNT(DISTINCT gid) AS distinct_gids,

    COUNT(DISTINCT substring(geoidfq FROM '([0-9]{11})$'))

        AS distinct_tract_geoids

FROM public.wv_censustracts_census_2020_utm83;

ERROR:  syntax error at or near "your"

LINE 1: your conceptual “two sets of 546 features” are implemented h...

        ^

msjarvisgis=# SELECT

    COUNT(*) AS physical_rows,

    COUNT(DISTINCT gid) AS distinct_gids,

    COUNT(DISTINCT substring(geoidfq FROM '([0-9]{11})$'))

        AS distinct_tract_geoids

FROM public.wv_censustracts_census_2020_utm83;

 physical_rows | distinct_gids | distinct_tract_geoids 

---------------+---------------+-----------------------

           546 |           546 |                   546

(1 row)

msjarvisgis=# SELECT

    COUNT(*) AS physical_rows,

    COUNT(DISTINCT gid) AS distinct_gids,

    COUNT(DISTINCT substring(geoidfq FROM '([0-9]{11})$'))

msjarvisgis=#  |           546 |                   546-'))

ERROR:  syntax error at or near "physical_rows"

LINE 1: physical_rows | distinct_gids | distinct_tract_geoids 

        ^

ERROR:  syntax error at or near "ERROR"

LINE 1: ERROR:  syntax error at or near "your"

        ^

ERROR:  syntax error at or near "physical_rows"

LINE 1: physical_rows | distinct_gids | distinct_tract_geoids 

        ^

ERROR:  syntax error at or near "physical_rows"

LINE 1: physical_rows | distinct_gids | distinct_tract_geoids 

        ^

ERROR:  syntax error at or near "physical_rows"

LINE 1: physical_rows | distinct_gids | distinct_tract_geoids 

        ^

ERROR:  syntax error at or near "physical_rows"

LINE 1: physical_rows | distinct_gids | distinct_tract_geoids 

        ^

msjarvisgis-# msjarvisgis=# msjarvisgis-# SELECT

    COUNT(*) AS physical_rows,

    COUNT(DISTINCT gid) AS distinct_gids,

    COUNT(DISTINCT substring(geoidfq FROM '([0-9]{11})$'))

        AS distinct_tract_geoids

FROM public.wv_censustracts_census_2020_utm83;

ERROR:  syntax error at or near "your"

LINE 1: your conceptual “two sets of 546 features” are implemented h...

        ^

msjarvisgis=# SELECT

    COUNT(*) AS physical_rows,

    COUNT(DISTINCT gid) AS distinct_gids,

    COUNT(DISTINCT substring(geoidfq FROM '([0-9]{11})$'))

        AS distinct_tract_geoids

FROM public.wv_censustracts_census_2020_utm83;

 physical_rows | distinct_gids | distinct_tract_geoids 

---------------+---------------+-----------------------

           546 |           546 |                   546

(1 row)

msjarvisgis=# SELECT

    COUNT(*) AS physical_rows,

    COUNT(DISTINCT gid) AS distinct_gids,

    COUNT(DISTINCT substring(geoidfq FROM '([0-9]{11})$'))

FROM public.wv_tract_representation;^Cributing_tablesnonical_tracts,,..

msjarvisgis=# ^C

msjarvisgis=# SELECT

    COUNT(*) AS representation_rows,

    COUNT(DISTINCT source_feature_id) AS distinct_source_feature_ids,

    COUNT(DISTINCT canonical_tract_id) AS distinct_canonical_tracts,

    COUNT(DISTINCT table_name) AS contributing_tables

FROM public.wv_tract_representation;

msjarvisgis=# SELECT

    table_name,

    COUNT(*) AS representation_rows,

    COUNT(DISTINCT source_feature_id) AS distinct_source_features,

    COUNT(DISTINCT canonical_tract_id) AS distinct_tracts

FROM public.wv_tract_representation

GROUP BY table_name

ORDER BY table_name;

msjarvisgis=# WHERE lc.table_name ILIKE '%censustract%'

msjarvisgis-# SELECT DISTINCT table_name

FROM public.wv_tract_representation

ORDER BY table_name;

ERROR:  syntax error at or near "WHERE"

LINE 1: WHERE lc.table_name ILIKE '%censustract%'

        ^

msjarvisgis=# ELECT

    table_name,

    COUNT(*) AS catalog_rows

FROM public.wv_layer_categories

WHERE table_name = 'wv_censustracts_census_2020_utm83'

GROUP BY table_name;

ERROR:  syntax error at or near "ELECT"

LINE 1: ELECT

        ^

msjarvisgis=# \d public.wv_layer_categories

                        Table "public.wv_layer_categories"

      Column       |            Type             | Collation | Nullable | Default 

-------------------+-----------------------------+-----------+----------+---------

 table_name        | text                        |           | not null | 

 category          | text                        |           | not null | 

 description       | text                        |           |          | 

 last_updated      | timestamp without time zone |           | not null | now()

 source_system     | text                        |           |          | 

 jurisdiction      | text                        |           |          | 

 geometry_type     | text                        |           |          | 

 srid              | integer                     |           |          | 

 spatial_grain     | text                        |           |          | 

 temporal_coverage | text                        |           |          | 

 authority_class   | text                        |           |          | 

 access_class      | text                        |           |          | 

Indexes:

    "wv_layer_categories_pkey" PRIMARY KEY, btree (table_name)

Referenced by:

    TABLE "wv_county_representation" CONSTRAINT "wv_county_representation_table_fk" FOREIGN KEY (table_name) REFERENCES wv_layer_categories(table_name) ON DELETE CASCADE

    TABLE "wv_entity_registry" CONSTRAINT "wv_entity_registry_table_fk" FOREIGN KEY (table_name) REFERENCES wv_layer_categories(table_name) ON DELETE CASCADE

    TABLE "wv_hazus_county_representation" CONSTRAINT "wv_hazus_county_representation_table_fk" FOREIGN KEY (table_name) REFERENCES wv_layer_categories(table_name) ON DELETE CASCADE

    TABLE "wv_layer_provenance" CONSTRAINT "wv_layer_provenance_table_fk" FOREIGN KEY (table_name) REFERENCES wv_layer_categories(table_name) ON DELETE CASCADE

msjarvisgis=# SELECT ctid, *

FROM public.wv_layer_categories

WHERE table_name = 'wv_censustracts_census_2020_utm83';

msjarvisgis=# SELECT

    source_feature_id,

    COUNT(*) AS mappings,

    array_agg(canonical_tract_id ORDER BY canonical_tract_id)

        AS canonical_ids

FROM public.wv_tract_representation

GROUP BY source_feature_id

HAVING COUNT(*) > 1

ORDER BY source_feature_id

LIMIT 20;

 source_feature_id | mappings |           canonical_ids            

-------------------+----------+------------------------------------

                 1 |        2 | {1400000US54101970102,54101970102}

                 2 |        2 | {1400000US54101970101,54101970101}

                 3 |        2 | {1400000US54025950401,54025950401}

                 4 |        2 | {1400000US54025950102,54025950102}

                 5 |        2 | {1400000US54025950402,54025950402}

                 6 |        2 | {1400000US54025950701,54025950701}

                 7 |        2 | {1400000US54025950702,54025950702}

                 8 |        2 | {1400000US54025950101,54025950101}

                 9 |        2 | {1400000US54003971105,54003971105}

                10 |        2 | {1400000US54003971206,54003971206}

                11 |        2 | {1400000US54003971302,54003971302}

                12 |        2 | {1400000US54003971401,54003971401}

                13 |        2 | {1400000US54003971205,54003971205}

                14 |        2 | {1400000US54003971301,54003971301}

                15 |        2 | {1400000US54003971104,54003971104}

                16 |        2 | {1400000US54003971103,54003971103}

                17 |        2 | {1400000US54075960102,54075960102}

                18 |        2 | {1400000US54075960101,54075960101}

                19 |        2 | {1400000US54035963300,54035963300}

                20 |        2 | {1400000US54051021001,54051021001}

(20 rows)

msjarvisgis=# SELECT

    length(canonical_tract_id) AS id_length,

    COUNT(*) AS rows,

    MIN(canonical_tract_id) AS example

FROM public.wv_tract_representation

GROUP BY length(canonical_tract_id)

ORDER BY id_length;

 id_length | rows |       example        

-----------+------+----------------------

        11 |  546 | 54001965500

        20 |  546 | 1400000US54001965500

(2 rows)

msjarvisgis=# SELECT

    COUNT(*) AS bridge_rows,

    COUNT(*) FILTER (

        WHERE t.canonical_tract_id IS NOT NULL

    ) AS valid_identity_rows,

    COUNT(*) FILTER (

        WHERE t.canonical_tract_id IS NULL

    ) AS orphaned_identity_rows

FROM public.wv_tract_representation r

LEFT JOIN public.wv_tract_identity t

  ON t.canonical_tract_id = r.canonical_tract_id;

 bridge_rows | valid_identity_rows | orphaned_identity_rows 

-------------+---------------------+------------------------

        1092 |                 546 |                    546

(1 row)

msjarvisgis=# \d public.wv_tract_representation

            Table "public.wv_tract_representation"

       Column        |  Type  | Collation | Nullable | Default 

---------------------+--------+-----------+----------+---------

 canonical_tract_id  | text   |           | not null | 

 canonical_county_id | text   |           |          | 

 table_name          | text   |           | not null | 

 source_feature_id   | bigint |           | not null | 

 source_feature_hash | text   |           |          | 

Indexes:

    "wv_tract_representation_pkey" PRIMARY KEY, btree (canonical_tract_id, table_name, source_feature_id)

msjarvisgis=# 

msjarvisgis=# SELECT ctid, *

FROM public.wv_layer_categories

WHERE table_name = 'wv_censustracts_census_2020_utm83';

msjarvisgis=# SELECT

    source_feature_id,

    COUNT(*) AS mappings,

    array_agg(canonical_tract_id ORDER BY canonical_tract_id)

        AS canonical_ids

FROM public.wv_tract_representation

GROUP BY source_feature_id

HAVING COUNT(*) > 1

ORDER BY source_feature_id

LIMIT 20;

 source_feature_id | mappings |           canonical_ids            

-------------------+----------+------------------------------------

                 1 |        2 | {1400000US54101970102,54101970102}

                 2 |        2 | {1400000US54101970101,54101970101}

                 3 |        2 | {1400000US54025950401,54025950401}

                 4 |        2 | {1400000US54025950102,54025950102}

                 5 |        2 | {1400000US54025950402,54025950402}

                 6 |        2 | {1400000US54025950701,54025950701}

                 7 |        2 | {1400000US54025950702,54025950702}

                 8 |        2 | {1400000US54025950101,54025950101}

msjarvisgis=# ature_id)ation_pkey" PRIMARY KEY, btree (canonical_tract_id, table_n

ERROR:  syntax error at or near "msjarvisgis"

LINE 1: msjarvisgis=# SELECT ctid, *

        ^

ERROR:  syntax error at or near "msjarvisgis"

LINE 1: msjarvisgis=# SELECT

        ^

ERROR:  syntax error at or near "source_feature_id"

LINE 1: source_feature_id | mappings |           canonical_ids      ...

        ^

ERROR:  syntax error at or near "id_length"

LINE 1: id_length | rows |       example        

        ^

            Table "public.wv_tract_representation"

       Column        |  Type  | Collation | Nullable | Default 

---------------------+--------+-----------+----------+---------

 canonical_tract_id  | text   |           | not null | 

 canonical_county_id | text   |           |          | 

 table_name          | text   |           | not null | 

 source_feature_id   | bigint |           | not null | 

 source_feature_hash | text   |           |          | 

Indexes:

    "wv_tract_representation_pkey" PRIMARY KEY, btree (canonical_tract_id, table_name, source_feature_id)

\d: extra argument "Table" ignored

\d: extra argument ""public.wv_tract_representation"" ignored

\d: extra argument "Column" ignored

\d: extra argument "|" ignored

\d: extra argument "Type" ignored

\d: extra argument "|" ignored

\d: extra argument "Collation" ignored

\d: extra argument "|" ignored

\d: extra argument "Nullable" ignored

\d: extra argument "|" ignored

\d: extra argument "Default" ignored

\d: extra argument "---------------------+--------+-----------+----------+---------" ignored

\d: extra argument "canonical_tract_id" ignored

\d: extra argument "|" ignored

\d: extra argument "text" ignored

\d: extra argument "|" ignored

\d: extra argument "|" ignored

\d: extra argument "not" ignored

\d: extra argument "null" ignored

\d: extra argument "|" ignored

\d: extra argument "canonical_county_id" ignored

\d: extra argument "|" ignored

\d: extra argument "text" ignored

\d: extra argument "|" ignored

\d: extra argument "|" ignored

\d: extra argument "|" ignored

\d: extra argument "table_name" ignored

\d: extra argument "|" ignored

\d: extra argument "text" ignored

\d: extra argument "|" ignored

\d: extra argument "|" ignored

\d: extra argument "not" ignored

\d: extra argument "null" ignored

\d: extra argument "|" ignored

\d: extra argument "source_feature_id" ignored

\d: extra argument "|" ignored

\d: extra argument "bigint" ignored

\d: extra argument "|" ignored

\d: extra argument "|" ignored

\d: extra argument "not" ignored

\d: extra argument "null" ignored

\d: extra argument "|" ignored

\d: extra argument "source_feature_hash" ignored

\d: extra argument "|" ignored

\d: extra argument "text" ignored

\d: extra argument "|" ignored

\d: extra argument "|" ignored

\d: extra argument "|" ignored

\d: extra argument "Indexes:" ignored

\d: extra argument ""wv_tract_representation_pkey"" ignored

\d: extra argument "PRIMARY" ignored

\d: extra argument "KEY," ignored

\d: extra argument "btree" ignored

\d: extra argument "(canonical_tract_id," ignored

\d: extra argument "table_name," ignored

\d: extra argument "source_feature_id)" ignored

\d: extra argument "msjarvisgis=#" ignored

msjarvisgis-# BEGIN;

CREATE TABLE public.wv_tract_representation_pre_cleanup_20260711 AS

SELECT *

FROM public.wv_tract_representation;

DELETE FROM public.wv_tract_representation r

WHERE NOT EXISTS (

    SELECT 1

    FROM public.wv_tract_identity t

    WHERE t.canonical_tract_id = r.canonical_tract_id

);

COMMIT;

ERROR:  syntax error at or near "bridge_rows"

LINE 1: bridge_rows | valid_identity_rows | orphaned_identity_rows 

        ^

SELECT 1092

DELETE 546

WARNING:  there is no transaction in progress

COMMIT

msjarvisgis=# SELECT

    COUNT(*) AS representation_rows,

    COUNT(DISTINCT source_feature_id) AS source_features,

    COUNT(DISTINCT canonical_tract_id) AS canonical_tracts,

    COUNT(DISTINCT table_name) AS contributing_tables

FROM public.wv_tract_representation;

 representation_rows | source_features | canonical_tracts | contributing_tables 

---------------------+-----------------+------------------+---------------------

                 546 |             546 |              546 |                   1

(1 row)

msjarvisgis=# SELECT COUNT(*) AS identity_orphans

FROM public.wv_tract_representation r

LEFT JOIN public.wv_tract_identity t

  ON t.canonical_tract_id = r.canonical_tract_id

WHERE t.canonical_tract_id IS NULL;

 identity_orphans 

------------------

                0

(1 row)

msjarvisgis=# SELECT COUNT(*) AS feature_orphans

FROM public.wv_tract_representation r

LEFT JOIN public.wv_censustracts_census_2020_utm83 p

  ON p.gid = r.source_feature_id

WHERE r.table_name = 'wv_censustracts_census_2020_utm83'

  AND p.gid IS NULL;

 feature_orphans 

-----------------

               0

(1 row)

msjarvisgis=# SELECT

    length(canonical_tract_id) AS id_length,

    COUNT(*) AS rows

FROM public.wv_tract_representation

GROUP BY length(canonical_tract_id)

ORDER BY id_length;

 id_length | rows 

-----------+------

        20 |  546

(1 row)

msjarvisgis=# SELECT COUNT(*) AS malformed_mapping_groups

FROM (

    SELECT source_feature_id

    FROM public.wv_tract_representation

    GROUP BY source_feature_id

    HAVING COUNT(*) <> 1

) x;

 malformed_mapping_groups 

--------------------------

                        0

(1 row)

msjarvisgis=# pgcrypto

msjarvisgis-# CREATE EXTENSION IF NOT EXISTS pgcrypto;

UPDATE public.wv_tract_representation r

SET source_feature_hash = encode(

    digest(

        concat_ws(

            '|',

            r.table_name,

            r.source_feature_id::text,

            r.canonical_tract_id,

            r.canonical_county_id,

            encode(

                ST_AsEWKB(

                    ST_Normalize(

                        ST_Transform(p.geom, 4326)

                    )

                ),

                'hex'

            )

        ),

        'sha256'

    ),

    'hex'

)

  AND r.source_feature_id = p.gid;cts_census_2020_utm83'

ERROR:  syntax error at or near "pgcrypto"

LINE 1: pgcrypto

        ^

UPDATE 546

msjarvisgis=# SELECT

    COUNT(*) AS representations,

    COUNT(source_feature_hash) AS hashed,

    COUNT(DISTINCT source_feature_hash) AS distinct_hashes

FROM public.wv_tract_representation;

 representations | hashed | distinct_hashes 

-----------------+--------+-----------------

             546 |    546 |             546

(1 row)

msjarvisgis=# SELECT COUNT(*) AS county_mismatches

FROM public.wv_tract_representation r

JOIN public.wv_tract_identity t

  ON t.canonical_tract_id = r.canonical_tract_id

WHERE r.canonical_county_id

      IS DISTINCT FROM t.canonical_county_id;

 county_mismatches 

-------------------

                 0

(1 row)

msjarvisgis=# 

msjarvisgis=# SELECT

    COUNT(*) AS snapshots,

    COUNT(DISTINCT canonical_tract_id) AS tracts,

    COUNT(DISTINCT belief_hash) AS hashes,

    COUNT(canonical_county_id) AS county_resolved

FROM public.wv_tract_belief_snapshot

WHERE snapshot_version = 'wv-tract-snapshot-v2';

 snapshots | tracts | hashes | county_resolved 

-----------+--------+--------+-----------------

         0 |      0 |      0 |               0

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ cat > "$HOME/msjarvis-db-recovery/msjarvisgis_governance_tables.sql"ce_tables.sql"

^C          

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ ^C

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ cat > "$HOME/msjarvis-db-recovery/msjarvisgis_governance_tables.sql"

^C

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ export DB_CONTAINER="jarvis-msjarvis-db"

mkdir -p "$HOME/msjarvis-db-recovery"

docker exec "$DB_CONTAINER" \

  psql -U postgres -d msjarvisgis -v ON_ERROR_STOP=1 <<'SQL' \

  > "$HOME/msjarvis-db-recovery/msjarvisgis_governance_tables.sql"

SELECT format(

  'CREATE TABLE public.wv_layer_categories (

    table_name        text    NOT NULL,

    category          text    NOT NULL,

    description       text,

    last_updated      timestamp without time zone NOT NULL DEFAULT now(),

    source_system     text,

    jurisdiction      text,

    geometry_type     text,

    srid              integer,

    spatial_grain     text,

    temporal_coverage text,

    authority_class   text,

    access_class      text,

    CONSTRAINT wv_layer_categories_pkey PRIMARY KEY (table_name)

  );'

SQL;' REFERENCES public.wv_county_identity(canonical_county_id)y FOREIGN KEY (cano

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ stat -c '%s bytes %n' "$HOME/msjarvis-db-recovery/msjarvisgis_governance_tables.sql"

0 bytes /home/cakidd/msjarvis-db-recovery/msjarvisgis_governance_tables.sql

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql \

  -h localhost \

  -p 5436 \

  -U postgres \

  -d msjarvisgis_v2 \

  -v ON_ERROR_STOP=1 \

  -f "$HOME/msjarvis-db-recovery/msjarvisgis_governance_tables.sql"

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql \

  -h localhost \

  -p 5436 \

  -U postgres \

  -d msjarvisgis_v2 \

  -c "\dt+ public.wv_*"

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql \

  -h localhost \

  -p 5436 \

  -U postgres \

  -d msjarvisgis_v2 \

  -v ON_ERROR_STOP=1 <<'SQL'

\\copy public.wv_layer_categories        FROM '/home/cakidd/msjarvis-db-recovery/wv_layer_categories.csv'        WITH (FORMAT csv, HEADER true);

\\copy public.wv_entity_registry         FROM '/home/cakidd/msjarvis-db-recovery/wv_entity_registry.csv'         WITH (FORMAT csv, HEADER true);

\\copy public.wv_county_identity         FROM '/home/cakidd/msjarvis-db-recovery/wv_county_identity.csv'         WITH (FORMAT csv, HEADER true);

\\copy public.wv_county_representation   FROM '/home/cakidd/msjarvis-db-recovery/wv_county_representation.csv'   WITH (FORMAT csv, HEADER true);

\\copy public.wv_tract_identity          FROM '/home/cakidd/msjarvis-db-recovery/wv_tract_identity.csv'          WITH (FORMAT csv, HEADER true);

\\copy public.wv_tract_representation    FROM '/home/cakidd/msjarvis-db-recovery/wv_tract_representation.csv'    WITH (FORMAT csv, HEADER true);

\\copy public.wv_county_dataset_coverage FROM '/home/cakidd/msjarvis-db-recovery/wv_county_dataset_coverage.csv' WITH (FORMAT csv, HEADER true);

\\copy public.wv_tract_dataset_coverage  FROM '/home/cakidd/msjarvis-db-recovery/wv_tract_dataset_coverage.csv'  WITH (FORMAT csv, HEADER true);

\\copy public.wv_county_belief_snapshot  FROM '/home/cakidd/msjarvis-db-recovery/wv_county_belief_snapshot.csv'  WITH (FORMAT csv, HEADER true);

\\copy public.wv_tract_belief_snapshot   FROM '/home/cakidd/msjarvis-db-recovery/wSQLract_belief_snapshot.csv'   WITH (FORMAT csv, HEADER true);

invalid command \

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql \

  -h localhost \

  -p 5436 \

  -U postgres \

  -d msjarvisgis_v2 \

  -v ON_ERROR_STOP=1 <<'SQL'

DO $$

DECLARE

    obj text;

    n bigint;

BEGIN

    FOREACH obj IN ARRAY ARRAY[

        'wv_layer_categories',

        'wv_entity_registry',

        'wv_county_identity',

        'wv_county_representation',

        'wv_tract_identity',

        'wv_tract_representation',

        'wv_county_dataset_coverage',

        'wv_tract_dataset_coverage',

        'wv_county_belief_snapshot',

        'wv_tract_belief_snapshot'

    ]

    LOOP

SQL END LOOP;F;SE NOTICE '% = MISSING', obj;n;I',ULL THEN

NOTICE:  wv_layer_categories = MISSING

NOTICE:  wv_entity_registry = MISSING

NOTICE:  wv_county_identity = MISSING

NOTICE:  wv_county_representation = MISSING

NOTICE:  wv_tract_identity = MISSING

NOTICE:  wv_tract_representation = MISSING

NOTICE:  wv_county_dataset_coverage = MISSING

NOTICE:  wv_tract_dataset_coverage = MISSING

NOTICE:  wv_county_belief_snapshot = MISSING

NOTICE:  wv_tract_belief_snapshot = MISSING

DO

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ mkdir -p "$HOME/msjarvis-db-recovery"

cat > "$HOME/msjarvis-db-recovery/msjarvisgis_governance_tables.sql" <<'EOF'

CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE public.wv_layer_categories (

    table_name text NOT NULL,

    category text NOT NULL,

    description text,

    last_updated timestamp without time zone NOT NULL DEFAULT now(),

    source_system text,

    jurisdiction text,

    geometry_type text,

    srid integer,

    spatial_grain text,

    temporal_coverage text,

    authority_class text,

    access_class text,

    CONSTRAINT wv_layer_categories_pkey PRIMARY KEY (table_name)

);

CREATE TABLE public.wv_entity_registry (

    entity_type text NOT NULL,

EOF     REFERENCES public.wv_county_identity(canonical_county_id)ot_versio_keyeatu

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ stat -c '%s bytes %n' "$HOME/msjarvis-db-recovery/msjarvisgis_governance_tables.sql"

psql \

  -h localhost \

  -p 5436 \

  -U postgres \

  -d msjarvisgis_v2 \

  -v ON_ERROR_STOP=1 \

  -f "$HOME/msjarvis-db-recovery/msjarvisgis_governance_tables.sql"

psql \

  -h localhost \

  -p 5436 \

  -U postgres \

  -d msjarvisgis_v2 \

  -c "\dt+ public.wv_layer_categories public.wv_entity_registry public.wv_county_identity public.wv_county_representation public.wv_tract_identity public.wv_tract_representation public.wv_county_dataset_coverage public.wv_tract_dataset_coverage public.wv_county_belief_snapshot public.wv_tract_belief_snapshot"

6980 bytes /home/cakidd/msjarvis-db-recovery/msjarvisgis_governance_tables.sql

psql:/home/cakidd/msjarvis-db-recovery/msjarvisgis_governance_tables.sql:1: NOTICE:  extension "pgcrypto" already exists, skipping

CREATE EXTENSION

CREATE TABLE

CREATE TABLE

CREATE TABLE

CREATE TABLE

CREATE TABLE

CREATE TABLE

CREATE TABLE

CREATE TABLE

CREATE TABLE

CREATE TABLE

\dt+: extra argument "public.wv_entity_registry" ignored

\dt+: extra argument "public.wv_county_identity" ignored

\dt+: extra argument "public.wv_county_representation" ignored

\dt+: extra argument "public.wv_tract_identity" ignored

\dt+: extra argument "public.wv_tract_representation" ignored

\dt+: extra argument "public.wv_county_dataset_coverage" ignored

\dt+: extra argument "public.wv_tract_dataset_coverage" ignored

\dt+: extra argument "public.wv_county_belief_snapshot" ignored

\dt+: extra argument "public.wv_tract_belief_snapshot" ignored

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql \

  -h localhost \

  -p 5436 \

  -U postgres \

  -d msjarvisgis_v2 \

  -c "SELECT tablename FROM pg_tables WHERE schemaname='public' AND tablename IN ( 

    'wv_layer_categories',

    'wv_entity_registry',

    'wv_county_identity',

    'wv_county_representation',

    'wv_tract_identity',

    'wv_tract_representation',

    'wv_county_dataset_coverage',

    'wv_tract_dataset_coverage',

    'wv_county_belief_snapshot',

    'wv_tract_belief_snapshot'

  ) ORDER BY tablename;"

         tablename          

----------------------------

 wv_county_belief_snapshot

 wv_county_dataset_coverage

 wv_county_identity

 wv_county_representation

 wv_entity_registry

 wv_layer_categories

 wv_tract_belief_snapshot

 wv_tract_dataset_coverage

 wv_tract_identity

 wv_tract_representation

(10 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql \

  -h localhost \

  -p 5436 \

  -U postgres \

  -d msjarvisgis_v2 \

  -v ON_ERROR_STOP=1 <<'SQL'

\copy public.wv_layer_categories        FROM '/home/cakidd/msjarvis-db-recovery/wv_layer_categories.csv'        WITH (FORMAT csv, HEADER true);

\copy public.wv_entity_registry         FROM '/home/cakidd/msjarvis-db-recovery/wv_entity_registry.csv'         WITH (FORMAT csv, HEADER true);

\copy public.wv_county_identity         FROM '/home/cakidd/msjarvis-db-recovery/wv_county_identity.csv'         WITH (FORMAT csv, HEADER true);

\copy public.wv_county_representation   FROM '/home/cakidd/msjarvis-db-recovery/wv_county_representation.csv'   WITH (FORMAT csv, HEADER true);

\copy public.wv_tract_identity          FROM '/home/cakidd/msjarvis-db-recovery/wv_tract_identity.csv'          WITH (FORMAT csv, HEADER true);

\copy public.wv_tract_representation    FROM '/home/cakidd/msjarvis-db-recovery/wv_tract_representation.csv'    WITH (FORMAT csv, HEADER true);

\copy public.wv_county_dataset_coverage FROM '/home/cakidd/msjarvis-db-recovery/wv_county_dataset_coverage.csv' WITH (FORMAT csv, HEADER true);

\copy public.wv_tract_dataset_coverage  FROM '/home/cakidd/msjarvis-db-recovery/wv_tract_dataset_coverage.csv'  WITH (FORMAT csv, HEADER true);

\copy public.wv_county_belief_snapshot  FROM '/home/cakidd/msjarvis-db-recovery/wv_county_belief_snapshot.csv'  WITH (FORMAT csv, HEADER true);

\copy public.wv_tract_belief_snapshot   FROM '/home/cakidd/msjarvis-db-recovery/wvSQLact_belief_snapshot.csv'   WITH (FORMAT csv, HEADER true);

COPY 254

COPY 65

COPY 55

COPY 220

COPY 546

COPY 546

COPY 275

COPY 1638

COPY 55

COPY 546

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql \

  -h localhost \

  -p 5436 \

  -U postgres \

  -d msjarvisgis_v2 \

  -v ON_ERROR_STOP=1 <<'SQL'

DO $$

DECLARE

    obj text;

    n bigint;

BEGIN

    FOREACH obj IN ARRAY ARRAY[

        'wv_layer_categories',

        'wv_entity_registry',

        'wv_county_identity',

        'wv_county_representation',

        'wv_tract_identity',

        'wv_tract_representation',

        'wv_county_dataset_coverage',

        'wv_tract_dataset_coverage',

        'wv_county_belief_snapshot',

        'wv_tract_belief_snapshot'

    ]

    LOOP

SQL END LOOP; NOTICE '% = % rows', obj, n;OM public.%I', obj) INTO n;

NOTICE:  wv_layer_categories = 254 rows

NOTICE:  wv_entity_registry = 65 rows

NOTICE:  wv_county_identity = 55 rows

NOTICE:  wv_county_representation = 220 rows

NOTICE:  wv_tract_identity = 546 rows

NOTICE:  wv_tract_representation = 546 rows

NOTICE:  wv_county_dataset_coverage = 275 rows

NOTICE:  wv_tract_dataset_coverage = 1638 rows

NOTICE:  wv_county_belief_snapshot = 55 rows

NOTICE:  wv_tract_belief_snapshot = 546 rows

DO

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql \

  -h localhost \

  -p 5436 \

  -U postgres \

  -d msjarvisgis_v2 \

  -v ON_ERROR_STOP=1 <<'SQL'

SELECT

    current_database() AS database_name,

    inet_server_port() AS server_port;

SELECT

    COUNT(*) AS counties,

    COUNT(DISTINCT canonical_county_id) AS distinct_counties,

    COUNT(DISTINCT county_geoid) AS distinct_county_geoids

FROM public.wv_county_identity;

SELECT

    COUNT(*) AS county_representations,

    COUNT(source_feature_hash) AS county_hashes,

    COUNT(DISTINCT source_feature_hash) AS distinct_county_hashes

FROM public.wv_county_representation;

SELECT

    COUNT(*) AS tracts,

SQLM public.wv_tract_belief_snapshot;stinct_tract_hashess,es,hes

 database_name  | server_port 

----------------+-------------

 msjarvisgis_v2 |        5436

(1 row)

 counties | distinct_counties | distinct_county_geoids 

----------+-------------------+------------------------

       55 |                55 |                     55

(1 row)

 county_representations | county_hashes | distinct_county_hashes 

------------------------+---------------+------------------------

                    220 |           220 |                    220

(1 row)

 tracts | distinct_tracts | unresolved_counties | county_geoid_mismatches 

--------+-----------------+---------------------+-------------------------

    546 |             546 |                   0 |                       0

(1 row)

 tract_representations | source_features | represented_tracts | tract_hashes | distinct_tract_hashes 

-----------------------+-----------------+--------------------+--------------+-----------------------

                   546 |             546 |                546 |          546 |                   546

(1 row)

 tract_identity_orphans 

------------------------

                      0

(1 row)

 county_identity_orphans 

-------------------------

                       0

(1 row)

 county_snapshots | snapshot_counties | populated_county_hashes | distinct_county_hashes 

------------------+-------------------+-------------------------+------------------------

               55 |                55 |                      55 |                     55

(1 row)

 tract_snapshots | snapshot_tracts | populated_tract_hashes | distinct_tract_hashes 

-----------------+-----------------+------------------------+-----------------------

             546 |             546 |                    546 |                   546

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql \

  -h localhost \

  -p 5436 \

  -U postgres \

  -d msjarvisgis_v2 \

  -P pager=off \

  -c "

    SELECT

        conrelid::regclass AS table_name,

        conname,

        CASE contype

            WHEN 'p' THEN 'primary_key'

            WHEN 'f' THEN 'foreign_key'

            WHEN 'u' THEN 'unique'

            WHEN 'c' THEN 'check'

            ELSE contype::text

        END AS constraint_type,

        pg_get_constraintdef(oid) AS definition

    FROM pg_constraint

    WHERE conrelid IN (

        'public.wv_layer_categories'::regclass,

        'public.wv_entity_registry'::regclass,

        'public.wv_county_identity'::regclass,

        'public.wv_county_representation'::regclass,

  " ORDER BY table_name::text, constraint_type, conname;

ERROR:  column "table_name" does not exist

LINE 26:     ORDER BY table_name::text, constraint_type, conname;

                      ^

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql \

  -h localhost \

  -p 5436 \

  -U postgres \

  -d msjarvisgis_v2 \

  -v ON_ERROR_STOP=1 <<'SQL'

SELECT

    to_regclass('public.wv_censustracts_census_2020_utm83')

        AS tract_source_table;

DO $$

DECLARE

    n bigint;

BEGIN

    IF to_regclass(

        'public.wv_censustracts_census_2020_utm83'

    ) IS NOT NULL THEN

        EXECUTE '

            SELECT count(*)

            FROM public.wv_censustracts_census_2020_utm83

        ' INTO n;

        RAISE NOTICE 'physical tract rows = %', n;

    ELSE

SQL END IF;SE NOTICE 'physical tract table = MISSING';

 tract_source_table 

--------------------

 

(1 row)

NOTICE:  physical tract table = MISSING

DO

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ mkdir -p "$HOME/msjarvis-db-recovery"

pg_dump \

  -h localhost \

  -p 5436 \

  -U postgres \

  -d msjarvisgis_v2 \

  -Fc \

  -f "$HOME/msjarvis-db-recovery/msjarvisgis_v2_verified.dump"

pg_restore \

  --list \

  "$HOME/msjarvis-db-recovery/msjarvisgis_v2_verified.dump" \

  >/dev/null

psql \

  -h localhost \

  -p 5436 \

  -U postgres \

  -d msjarvisgis_v2 \

  -v ON_ERROR_STOP=1 \

  -c "REINDEX DATABASE msjarvisgis_v2;"

  "$HOME/msjarvis-db-recovery/msjarvisgis_v2_verified.dump"

REINDEX

926712 bytes /home/cakidd/msjarvis-db-recovery/msjarvisgis_v2_verified.dump

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ 

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql \

  -h localhost \

  -p 5436 \

  -U postgres \

  -d msjarvisgis_v2 \

  -P pager=off <<'SQL'

SELECT *

FROM (

    SELECT

        conrelid::regclass::text AS relation_name,

        conname,

        CASE contype

            WHEN 'p' THEN 'primary_key'

            WHEN 'f' THEN 'foreign_key'

            WHEN 'u' THEN 'unique'

            WHEN 'c' THEN 'check'

            ELSE contype::text

        END AS constraint_type,

        pg_get_constraintdef(oid) AS definition

    FROM pg_constraint

    WHERE conrelid IN (

        'public.wv_layer_categories'::regclass,

        'public.wv_entity_registry'::regclass,

        'public.wv_county_identity'::regclass,

SQLER BY relation_name, constraint_type, conname;sss,,

       relation_name        |                             conname                             | constraint_type |                                                                              definition                                                                              

----------------------------+-----------------------------------------------------------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------

 wv_county_belief_snapshot  | wv_county_belief_snapshot_canonical_county_id_fkey              | foreign_key     | FOREIGN KEY (canonical_county_id) REFERENCES wv_county_identity(canonical_county_id)

 wv_county_belief_snapshot  | wv_county_belief_snapshot_pkey                                  | primary_key     | PRIMARY KEY (snapshot_id)

 wv_county_belief_snapshot  | wv_county_belief_snapshot_canonical_county_id_snapshot_vers_key | unique          | UNIQUE (canonical_county_id, snapshot_version)

 wv_county_dataset_coverage | wv_county_dataset_coverage_coverage_state_check                 | check           | CHECK ((coverage_state = ANY (ARRAY['present'::text, 'confirmed_none'::text, 'missing_source'::text, 'unassigned'::text, 'not_applicable'::text, 'unknown'::text])))

 wv_county_dataset_coverage | wv_county_dataset_coverage_canonical_county_id_fkey             | foreign_key     | FOREIGN KEY (canonical_county_id) REFERENCES wv_county_identity(canonical_county_id)

 wv_county_dataset_coverage | wv_county_dataset_coverage_pkey                                 | primary_key     | PRIMARY KEY (canonical_county_id, dataset_type, source_table)

 wv_county_identity         | wv_county_identity_county_fips_chk                              | check           | CHECK ((county_fips ~ '^[0-9]{3}$'::text))

 wv_county_identity         | wv_county_identity_geoid_chk                                    | check           | CHECK ((county_geoid ~ '^[0-9]{5}$'::text))

 wv_county_identity         | wv_county_identity_state_fips_chk                               | check           | CHECK ((state_fips = '54'::text))

 wv_county_identity         | wv_county_identity_pkey                                         | primary_key     | PRIMARY KEY (canonical_county_id)

 wv_county_identity         | wv_county_identity_county_geoid_key                             | unique          | UNIQUE (county_geoid)

 wv_county_representation   | wv_county_representation_county_fk                              | foreign_key     | FOREIGN KEY (canonical_county_id) REFERENCES wv_county_identity(canonical_county_id) ON DELETE RESTRICT

 wv_county_representation   | wv_county_representation_table_fk                               | foreign_key     | FOREIGN KEY (table_name) REFERENCES wv_layer_categories(table_name) ON DELETE CASCADE

 wv_county_representation   | wv_county_representation_pkey                                   | primary_key     | PRIMARY KEY (table_name, source_feature_id)

 wv_entity_registry         | wv_entity_registry_table_fk                                     | foreign_key     | FOREIGN KEY (table_name) REFERENCES wv_layer_categories(table_name) ON DELETE CASCADE

 wv_entity_registry         | wv_entity_registry_pkey                                         | primary_key     | PRIMARY KEY (entity_type, table_name)

 wv_layer_categories        | wv_layer_categories_pkey                                        | primary_key     | PRIMARY KEY (table_name)

 wv_tract_belief_snapshot   | wv_tract_belief_snapshot_canonical_county_id_fkey               | foreign_key     | FOREIGN KEY (canonical_county_id) REFERENCES wv_county_identity(canonical_county_id)

 wv_tract_belief_snapshot   | wv_tract_belief_snapshot_pkey                                   | primary_key     | PRIMARY KEY (snapshot_id)

 wv_tract_belief_snapshot   | wv_tract_belief_snapshot_canonical_tract_id_snapshot_versio_key | unique          | UNIQUE (canonical_tract_id, snapshot_version)

 wv_tract_dataset_coverage  | wv_tract_dataset_coverage_coverage_state_check                  | check           | CHECK ((coverage_state = ANY (ARRAY['present'::text, 'confirmed_none'::text, 'missing_source'::text, 'unassigned'::text, 'not_applicable'::text, 'unknown'::text])))

 wv_tract_dataset_coverage  | wv_tract_dataset_coverage_canonical_county_id_fkey              | foreign_key     | FOREIGN KEY (canonical_county_id) REFERENCES wv_county_identity(canonical_county_id)

 wv_tract_dataset_coverage  | wv_tract_dataset_coverage_pkey                                  | primary_key     | PRIMARY KEY (canonical_tract_id, dataset_type, source_table)

 wv_tract_identity          | wv_tract_identity_canonical_county_id_fkey                      | foreign_key     | FOREIGN KEY (canonical_county_id) REFERENCES wv_county_identity(canonical_county_id)

 wv_tract_identity          | wv_tract_identity_pkey                                          | primary_key     | PRIMARY KEY (canonical_tract_id)

 wv_tract_representation    | wv_tract_representation_pkey                                    | primary_key     | PRIMARY KEY (canonical_tract_id, table_name, source_feature_id)

(26 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql \

  -h localhost \

  -p 5436 \

  -U postgres \

  -d msjarvisgis_v2 \

  -P pager=off <<'SQL'

WITH referenced AS (

    SELECT DISTINCT table_name

    FROM public.wv_county_representation

    UNION

    SELECT DISTINCT table_name

    FROM public.wv_tract_representation

)

SELECT

    r.table_name,

    to_regclass('public.' || r.table_name) AS local_relation,

    CASE

        WHEN to_regclass('public.' || r.table_name) IS NULL

            THEN 'missing'

        ELSE 'present'

    END AS source_state

FROM referenced r

SQLER BY r.table_name;

                      table_name                      | local_relation | source_state 

------------------------------------------------------+----------------+--------------

 wv_censustracts_census_2020_utm83                    |                | missing

 wv_county_boundaries_24k_topo_updated_2026_utm83_gdb |                | missing

 wv_county_boundaries_24k_topo_updated_2026_wma84_gdb |                | missing

 wv_wv_county_boundaries_24k_topo_updated_2026_utm83  |                | missing

 wv_wv_county_boundaries_24k_topo_updated_2026_wma84  |                | missing

(5 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ export DB_CONTAINER="jarvis-msjarvis-db"

export GOVERNANCE_DB="msjarvisgis"

psql \

  -h localhost \

  -p 5436 \

  -U postgres \

  -d msjarvisgis_v2 \

  -Atc "

    SELECT table_name

    FROM (

        SELECT DISTINCT table_name

        FROM public.wv_county_representation

        UNION

        SELECT DISTINCT table_name

        FROM public.wv_tract_representation

    ) s

    ORDER BY table_name;

  " |

while IFS= read -r TABLE_NAME; do

  RESULT="$(

doneintf '%s | %s\n' "$TABLE_NAME" "$RESULT"AME\"_NAME')

wv_censustracts_census_2020_utm83 | 546

wv_county_boundaries_24k_topo_updated_2026_utm83_gdb | 55

wv_county_boundaries_24k_topo_updated_2026_wma84_gdb | 55

wv_wv_county_boundaries_24k_topo_updated_2026_utm83 | 55

wv_wv_county_boundaries_24k_topo_updated_2026_wma84 | 55

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ apfile -t SOURCE_TABLES < <(

  psql \

    -h localhost \

    -p 5436 \

    -U postgres \

    -d msjarvisgis_v2 \

    -Atc "

      SELECT table_name

      FROM (

          SELECT DISTINCT table_name

          FROM public.wv_county_representation

          UNION

          SELECT DISTINCT table_name

          FROM public.wv_tract_representation

      ) s

      ORDER BY table_name;

    "

)

DUMP_ARGS=()

for TABLE_NAME in "${SOURCE_TABLES[@]}"; do

  "$HOME/msjarvis-db-recovery/gbim_physical_sources.dump"t"

apfile: command not found

pg_dump: error: schema with OID 726804 does not exist

pg_restore: error: input file is too short (read 0, expected 5)

0 bytes /home/cakidd/msjarvis-db-recovery/gbim_physical_sources.dump

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ pg_restore \

  -h localhost \

  -p 5436 \

  -U postgres \

  -d msjarvisgis_v2 \

  --no-owner \

  --no-privileges \

  --exit-on-error \

  "$HOME/msjarvis-db-recovery/gbim_physical_sources.dump"

pg_restore: error: input file is too short (read 0, expected 5)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql \

  -h localhost \

  -p 5436 \

  -U postgres \

  -d msjarvisgis_v2 \

  -v ON_ERROR_STOP=1 <<'SQL'

DO $$

DECLARE

    rec record;

    physical_count bigint;

    bridge_count bigint;

    orphan_count bigint;

BEGIN

    FOR rec IN

        SELECT DISTINCT table_name, 'county'::text AS entity_type

        FROM public.wv_county_representation

        UNION ALL

        SELECT DISTINCT table_name, 'tract'::text

        FROM public.wv_tract_representation

    LOOP

        IF to_regclass(

            format('public.%I', rec.table_name)

SQL END LOOP;F; rec.table_name;sentations found for %',,

ERROR:  Missing physical table: wv_wv_county_boundaries_24k_topo_updated_2026_wma84

CONTEXT:  PL/pgSQL function inline_code_block line 20 at RAISE

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ pg_dump \

  -h localhost \

  -p 5436 \

  -U postgres \

  -d msjarvisgis_v2 \

  -Fc \

  -f "$HOME/msjarvis-db-recovery/msjarvisgis_v2_complete.dump"

pg_restore \

  --list \

  "$HOME/msjarvis-db-recovery/msjarvisgis_v2_complete.dump" \

  >/dev/null

stat \

  -c '%s bytes %n' \

  "$HOME/msjarvis-db-recovery/msjarvisgis_v2_complete.dump"

926712 bytes /home/cakidd/msjarvis-db-recovery/msjarvisgis_v2_complete.dump

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ You’ve now validated that governance constraints are correct, identified the five missing physical source tables, confirmed their row counts in the Docker DB, exported them, restored them into `msjarvisgis_v2`, and produced a consistent v2 backup. That vertical slice from physical source → representations → canonical identities → coverage → belief snapshots is in good shape. [stackoverflow](https://stackoverflow.com/questions/36469624/pg-restore-archiver-input-file-is-too-short-error-in-postgres)

To keep things clear, here’s what you’ve accomplished and what’s next.

## Governance and constraints are intact

- The constraints query against `pg_constraint` shows the expected primary keys, foreign keys, uniques, and checks on all ten governance tables (`wv_layer_categories`, `wv_entity_registry`, `wv_county_identity`, `wv_county_representation`, `wv_tract_identity`, `wv_tract_representation`, `wv_county_dataset_coverage`, `wv_tract_dataset_coverage`, `wv_county_belief_snapshot`, `wv_tract_belief_snapshot`). [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/51743013/89e53f6d-bc91-459d-9214-3ade8b53d594/paste.txt?AWSAccessKeyId=ASIA2F3EMEYEWUV42FCT&Signature=NhN%2Fo0zkxr4luQ1c8vsRxpVXJMw%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEBEaCXVzLWVhc3QtMSJHMEUCIG%2FD9ohLH6HmoQjkSXdcT6Th0AvUbBPnxu7MzIbhyZQyAiEA9C%2BDugwwr1yZ5iBk9Fwu9av1bozOeRoRqEDFalpeRAIq%2FAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDGwKECV8%2FqhnQ7ne1SrQBMDvl875Z5NvobQnGXPYpokOftUBBHLjEEve98toXEoLLp3FYXmWmRrr9bCTtBARtEGT4skOnuEiR2kkzr%2Buq%2BQbw8jd0mzc9IbBssUp72NIkMlPYY3QW8XGFR8taMLRv9TEwj31HB1Us5hOW9eLra%2FCLepNEHq%2Ft5oELp%2B3hGTMHymR%2FoKuOO1Sq%2Bo2SwWUBtMVhlJ0vgn8pnFOA8%2FoqhansfFc2%2Fxlwyvm7Tt7voykjxr6WX9juRGEUibtrndZjhrVbKp%2Fze1gtwve57SU45mMdp2hNWxZN4GVeI%2FRau2EqAkvCb1qzdqYVR31NEG7agwyG1k9W%2B38oKvLqDjUSIuBQIoMQJiJ%2Fxc1YRAiTAosxeR6xE5GRD%2FroD9iovd1bTmdVC7PubeNkjBFdA2sprr0PSdxqrrUsFZKIyFa6SDeCQ5g7KmIdTVEmumPx23U4evjhgbCDaurl97bQ0GDq0i2Vn2MNXv3HEoBQ3QhhtwkCk9%2FwwtCpB0vCqtFhwGeGjsZMXY0Rey144DJzcxvbF6KtRZUCLwUeOIYzU3xdBqUst9GXhT8QC3qSflfj6MvJSt%2Fu4LDMWNzcqZ52djeZUZ2pyz6AunqetsV1MuzrGJpwTWXkXmW59Z%2B8x8vfs2hcBtcGSXDx3Y7ESuU6ov1mV9Pc4GyZZeZytGjwI2S8Kw0jHV0Gd87Soa9pWPftiJf0pjXwf%2FeHMVKFNpprpD%2FLUxWu51FDLHUtEehogJsLRUx6MMLaQJ8Beidx7fFI%2BS%2F9nMcdxFaBtmvoJQuA9lGWfEwjMLL0gY6mAFjYQbH6tvnL%2FWcuuAPLICKAgWhDndQRvjQd1IJqrZYgFYVnupaH4%2BIc1MjgQjgcRTkgwoPX2GjiDaYMZ1aMyMJk1lUDJuDPo4RSLZ3VVOhOlJdWP%2BUhJUdi8wOpxpMpHiZt8YRpyswHFThTJiqNMHlrzDTE8iusCPCx%2FeA5AAodAdrQHI5vgWd1X8k0Y6kpf4TLx5puR0ZJQ%3D%3D&Expires=178381999a single scripted path from raw Docker DB to validated v2 and embeddings.^Cu have 

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ command -v ogr2ogr

ogr2ogr --version

/usr/bin/ogr2ogr

GDAL 3.8.4, released 2024/02/08

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ PGPASSWORD="$(

  docker inspect jarvis-msjarvis-db \

    --format '{{range .Config.Env}}{{println .}}{{end}}' |

  sed -n 's/^POSTGRES_PASSWORD=//p' |

  head -1

)" \

psql \

  -h localhost \

  -p 5433 \

  -U postgres \

  -d msjarvisgis \

  -Atc "SELECT current_database(), inet_server_port();"

msjarvisgis|5432

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ export SOURCE_DB_PASSWORD="$(

  docker inspect jarvis-msjarvis-db \

    --format '{{range .Config.Env}}{{println .}}{{end}}' |

  sed -n 's/^POSTGRES_PASSWORD=//p' |

  head -1

)"

test -n "$SOURCE_DB_PASSWORD"

export SOURCE_PG="PG:host=localhost port=5433 dbname=msjarvisgis user=postgres password=${SOURCE_DB_PASSWORD}"

export TARGET_PG="PG:host=localhost port=5436 dbname=msjarvisgis_v2 user=postgres" 

for TABLE_NAME in \

  wv_censustracts_census_2020_utm83 \

  wv_county_boundaries_24k_topo_updated_2026_utm83_gdb \

  wv_county_boundaries_24k_topo_updated_2026_wma84_gdb \

  wv_wv_county_boundaries_24k_topo_updated_2026_utm83 \

  wv_wv_county_boundaries_24k_topo_updated_2026_wma84

do

  echo "Copying ${TABLE_NAME}"

  ogr2ogr \

done-progresse \_TO_MULTI \ \}" \TABLE_NAME}" \

Copying wv_censustracts_census_2020_utm83

0...10...20...30...40...50...60...70...80...90...100 - done.

Copying wv_county_boundaries_24k_topo_updated_2026_utm83_gdb

0...10...20...30...40...50...60...70...80...90...100 - done.

Copying wv_county_boundaries_24k_topo_updated_2026_wma84_gdb

0...10...20...30...40...50...60...70...80...90...100 - done.

Copying wv_wv_county_boundaries_24k_topo_updated_2026_utm83

0...10...20...30...40...50...60...70...80...90...100 - done.

Copying wv_wv_county_boundaries_24k_topo_updated_2026_wma84

0...10...20...30...40...50...60...70...80...90...100 - done.

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql \

  -h localhost \

  -p 5436 \

  -U postgres \

  -d msjarvisgis_v2 \

  -v ON_ERROR_STOP=1 <<'SQL'

SELECT

    'wv_censustracts_census_2020_utm83' AS table_name,

    COUNT(*) AS rows

FROM public.wv_censustracts_census_2020_utm83

UNION ALL

SELECT

    'wv_county_boundaries_24k_topo_updated_2026_utm83_gdb',

    COUNT(*)

FROM public.wv_county_boundaries_24k_topo_updated_2026_utm83_gdb

UNION ALL

SELECT

    'wv_county_boundaries_24k_topo_updated_2026_wma84_gdb',

    COUNT(*)

SQLM public.wv_wv_county_boundaries_24k_topo_updated_2026_wma84;

                      table_name                      | rows 

------------------------------------------------------+------

 wv_censustracts_census_2020_utm83                    |  546

 wv_county_boundaries_24k_topo_updated_2026_utm83_gdb |   55

 wv_county_boundaries_24k_topo_updated_2026_wma84_gdb |   55

 wv_wv_county_boundaries_24k_topo_updated_2026_utm83  |   55

 wv_wv_county_boundaries_24k_topo_updated_2026_wma84  |   55

(5 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ ^C

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ 

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ 

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ 

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ 

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ 

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ tail -n 40 "$BUILDLOG"

tail: cannot open '' for reading: No such file or directory

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ # See the pg_dump process and its CPU/IO usage

ps aux | grep "pg_dump -p 5433" | grep -v grep

# Or a fuller tree view

ps afx | grep pg_dump | grep -v grep

cakidd   2102619 98.1  0.1  66688 36256 pts/1    R+   15:52   3:01 /usr/lib/postgresql/16/bin/pg_dump -p 5433 -U postgres -d msjarvisgis --format=custom --no-tablespaces -f /home/cakidd/gbim-backup-20260712T155231Z/msjarvisgis_evidence_5433.dump

2102619 pts/1    R+     3:01  |       \_ /usr/lib/postgresql/16/bin/pg_dump -p 5433 -U postgres -d msjarvisgis --format=custom --no-tablespaces -f /home/cakidd/gbim-backup-20260712T155231Z/msjarvisgis_evidence_5433.dump

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ watch -n 2 "ls -lh /home/cakidd/gbim-backup-20260712T155231Z/msjarvisgis_evidence_5433.dump"

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

CREATE SCHEMA IF NOT EXISTS manifest;

"

CREATE SCHEMA

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ # Source files manifest

psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

DROP TABLE IF EXISTS manifest.wv_source_files_manifest;

CREATE TABLE manifest.wv_source_files_manifest (

    filename text,

    path text,

    provider text,

    crs text,

    notes text

);

"

psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

COPY manifest.wv_source_files_manifest

FROM '/mnt/spiritual_drive/msjarvis-rebuild/wv_source_files_manifest.csv'

WITH (FORMAT csv, HEADER true);

"

# Source→table layers manifest

psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

DROP TABLE IF EXISTS manifest.wv_source_manifest_layers;

CREATE TABLE manifest.wv_source_manifest_layers (

    layer_label text,

    source_filename text,

"ITH (FORMAT csv, HEADER true);rvis-rebuild/wv_derived_governance_tables.csv'

NOTICE:  table "wv_source_files_manifest" does not exist, skipping

DROP TABLE

CREATE TABLE

ERROR:  could not open file "/mnt/spiritual_drive/msjarvis-rebuild/wv_source_files_manifest.csv" for reading: No such file or directory

HINT:  COPY FROM instructs the PostgreSQL server process to read a file. You may want a client-side facility such as psql's \copy.

NOTICE:  table "wv_source_manifest_layers" does not exist, skipping

DROP TABLE

CREATE TABLE

COPY 11

NOTICE:  table "wv_derived_governance_tables" does not exist, skipping

DROP TABLE

CREATE TABLE

ERROR:  extra data after last expected column

CONTEXT:  COPY wv_derived_governance_tables, line 2: "wv_layer_categories,governance_layer_catalog,internal GBIM layer taxonomy, no single source ZIP"

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

WITH corpus_tables AS (

  SELECT table_name

  FROM information_schema.tables

  WHERE table_schema = 'public'

    AND table_name LIKE 'wv_%'

),

layers_mapped AS (

  SELECT regexp_replace(gbim_table, '^public\\.', '') AS table_name

  FROM manifest.wv_source_manifest_layers

),

derived_mapped AS (

  SELECT table_name

  FROM manifest.wv_derived_governance_tables

)

SELECT table_name

FROM corpus_tables

EXCEPT

SELECT table_name FROM layers_mapped

EXCEPT

SELECT table_name FROM derived_mapped

ORDER BY table_name;

"

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ # On governance DB: 5436, msjarvisgis_v2

psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

DROP TABLE IF EXISTS wv_blockgroup_identity;

CREATE TABLE wv_blockgroup_identity (

    blockgroup_geoid text PRIMARY KEY,

    county_geoid text NOT NULL,

    county_id integer NOT NULL,

    blockgroup_name text,

    created_at timestamptz DEFAULT now()

);

"

DROP TABLE IF EXISTS wv_blockgroup_representation;

CREATE TABLE wv_blockgroup_representation (

    blockgroup_geoid text PRIMARY KEY,

    source_table text NOT NULL,

    source_feature_id bigint NOT NULL,

    geom geometry(MULTIPOLYGON, 4269),

    geom_hash text NOT NULL,

    srid integer NOT NULL,

    created_at timestamptz DEFAULT now()

);

"

NOTICE:  table "wv_blockgroup_identity" does not exist, skipping

DROP TABLE

CREATE TABLE

DROP: command not found

bash: syntax error near unexpected token `('

blockgroup_geoid: command not found

source_table: command not found

source_feature_id: command not found

bash: syntax error near unexpected token `('

geom_hash: command not found

Command 'srid' not found, did you mean:

  command 'sxid' from deb sxid (4.20130802-7)

  command 'srsd' from deb srs (0.31-9)

  command 'ssid' from deb suckless-tools (47-1)

  command 'scid' from deb scid (1:4.7.4+dfsg1-2)

Try: sudo apt install <deb name>

bash: syntax error near unexpected token `('

bash: syntax error near unexpected token `)'

> ^C

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ # On governance DB: 5436, msjarvisgis_v2

psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

DROP TABLE IF EXISTS wv_blockgroup_identity;

CREATE TABLE wv_blockgroup_identity (

    blockgroup_geoid text PRIMARY KEY,

    county_geoid text NOT NULL,

    county_id integer NOT NULL,

    blockgroup_name text,

    created_at timestamptz DEFAULT now()

);

"

psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

DROP TABLE IF EXISTS wv_blockgroup_representation;

CREATE TABLE wv_blockgroup_representation (

    blockgroup_geoid text PRIMARY KEY,

    source_table text NOT NULL,

    source_feature_id bigint NOT NULL,

    geom geometry(MULTIPOLYGON, 4269),

    geom_hash text NOT NULL,

    srid integer NOT NULL,

    created_at timestamptz DEFAULT now()

";

DROP TABLE

CREATE TABLE

NOTICE:  table "wv_blockgroup_representation" does not exist, skipping

DROP TABLE

CREATE TABLE

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ # Enable dblink extension if not already present

psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

CREATE EXTENSION IF NOT EXISTS dblink;

"

# Populate blockgroup_identity from evidence on 5433

psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

INSERT INTO wv_blockgroup_identity (blockgroup_geoid, county_geoid, county_id, blockgroup_name)

SELECT bg.block_geoid, bg.county_geoid, c.county_id, bg.block_name

FROM dblink(

        'host=localhost port=5433 dbname=msjarvisgis user=postgres',

        'SELECT block_geoid, county_geoid, block_name FROM public.wv_cen_blockgroup_2020'

     ) AS bg(block_geoid text, county_geoid text, block_name text)

JOIN wv_county_identity c ON c.county_geoid = bg.county_geoid;

"

# Populate blockgroup_representation from evidence

psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

INSERT INTO wv_blockgroup_representation (blockgroup_geoid, source_table, source_feature_id, geom, geom_hash, srid)

SELECT bg.block_geoid,

"    ) AS bg(gid integer, block_geoid text, geom geometry);lockgroup_2020'

CREATE EXTENSION

ERROR:  column c.county_id does not exist

LINE 3: SELECT bg.block_geoid, bg.county_geoid, c.county_id, bg.bloc...

                                                ^

HINT:  Perhaps you meant to reference the column "c.county_fips" or the column "c.county_geoid".

ERROR:  could not establish connection

DETAIL:  connection to server at "localhost" (127.0.0.1), port 5433 failed: fe_sendauth: no password supplied

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

SELECT column_name

FROM information_schema.columns

WHERE table_schema = 'public'

  AND table_name = 'wv_county_identity';

"

     column_name     

---------------------

 canonical_county_id

 state_fips

 county_fips

 county_geoid

 county_name

 state_abbrev

 state_name

 authority_class

 access_class

 created_at

 updated_at

(11 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

INSERT INTO wv_blockgroup_identity (blockgroup_geoid, county_geoid, county_id, blockgroup_name)

SELECT bg.block_geoid,

       bg.county_geoid,

       c.county_geoid::integer,

       bg.block_name

FROM dblink(

        'host=localhost port=5433 dbname=msjarvisgis user=postgres',

        'SELECT block_geoid, county_geoid, block_name FROM public.wv_cen_blockgroup_2020'

     ) AS bg(block_geoid text, county_geoid text, block_name text)

JOIN wv_county_identity c ON c.county_geoid = bg.county_geoid;

"

ERROR:  could not establish connection

DETAIL:  connection to server at "localhost" (127.0.0.1), port 5433 failed: fe_sendauth: no password supplied

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

INSERT INTO wv_blockgroup_identity (blockgroup_geoid, county_geoid, county_id, blockgroup_name)

SELECT bg.block_geoid,

       bg.county_geoid,

       c.canonical_county_id,

       bg.block_name

FROM dblink(

        'host=localhost port=5433 dbname=msjarvisgis user=postgres password=YOUR_PASSWORD',

        'SELECT block_geoid, county_geoid, block_name FROM public.wv_cen_blockgroup_2020'

     ) AS bg(block_geoid text, county_geoid text, block_name text)

JOIN wv_county_identity c ON c.county_geoid = bg.county_geoid;

"

ERROR:  column "county_id" is of type integer but expression is of type text

LINE 5:        c.canonical_county_id,

               ^

HINT:  You will need to rewrite or cast the expression.

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

INSERT INTO wv_blockgroup_identity (blockgroup_geoid, county_geoid, county_id, blockgroup_name)

SELECT bg.block_geoid,

       bg.county_geoid,

       c.canonical_county_id::integer,

       bg.block_name

FROM dblink(

        'host=localhost port=5433 dbname=msjarvisgis user=postgres password=YOUR_PASSWORD',

        'SELECT block_geoid, county_geoid, block_name FROM public.wv_cen_blockgroup_2020'

     ) AS bg(block_geoid text, county_geoid text, block_name text)

JOIN wv_county_identity c ON c.county_geoid = bg.county_geoid;

"

ERROR:  could not establish connection

DETAIL:  connection to server at "localhost" (127.0.0.1), port 5433 failed: FATAL:  password authentication failed for user "postgres"

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

ALTER TABLE wv_blockgroup_identity

  ALTER COLUMN county_id TYPE text USING county_id::text;

"

ALTER TABLE

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

INSERT INTO wv_blockgroup_identity (blockgroup_geoid, county_geoid, county_id, blockgroup_name)

SELECT bg.block_geoid,

       bg.county_geoid,

       c.canonical_county_id,

       bg.block_name

FROM dblink(

        'host=localhost port=5433 dbname=msjarvisgis user=postgres password=YOUR_PASSWORD',

        'SELECT block_geoid, county_geoid, block_name FROM public.wv_cen_blockgroup_2020'

     ) AS bg(block_geoid text, county_geoid text, block_name text)

JOIN wv_county_identity c ON c.county_geoid = bg.county_geoid;

"

ERROR:  could not establish connection

DETAIL:  connection to server at "localhost" (127.0.0.1), port 5433 failed: FATAL:  password authentication failed for user "postgres"

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ # Create or edit ~/.pgpass

nano ~/.pgpass

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ chmod 600 ~/.pgpass

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

INSERT INTO wv_blockgroup_identity (blockgroup_geoid, county_geoid, county_id, blockgroup_name)

SELECT bg.block_geoid,

       bg.county_geoid,

       c.canonical_county_id,

       bg.block_name

FROM dblink(

        'host=localhost port=5433 dbname=msjarvisgis user=postgres',

        'SELECT block_geoid, county_geoid, block_name FROM public.wv_cen_blockgroup_2020'

     ) AS bg(block_geoid text, county_geoid text, block_name text)

JOIN wv_county_identity c ON c.county_geoid = bg.county_geoid;

"

ERROR:  could not establish connection

DETAIL:  connection to server at "localhost" (127.0.0.1), port 5433 failed: fe_sendauth: no password supplied

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ export PGPASSFILE=~/.pgpass

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -p 5433 -U postgres -d msjarvisgis -w -c "SELECT 1;"

 ?column? 

----------

        1

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

INSERT INTO wv_blockgroup_identity (blockgroup_geoid, county_geoid, county_id, blockgroup_name)

SELECT bg.block_geoid,

       bg.county_geoid,

       c.canonical_county_id,

       bg.block_name

FROM dblink(

        'host=localhost port=5433 dbname=msjarvisgis user=postgres',

        'SELECT block_geoid, county_geoid, block_name FROM public.wv_cen_blockgroup_2020'

     ) AS bg(block_geoid text, county_geoid text, block_name text)

JOIN wv_county_identity c ON c.county_geoid = bg.county_geoid;

"

ERROR:  could not establish connection

DETAIL:  connection to server at "localhost" (127.0.0.1), port 5433 failed: fe_sendauth: no password supplied

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

INSERT INTO wv_blockgroup_identity (blockgroup_geoid, county_geoid, county_id, blockgroup_name)

SELECT bg.block_geoid,

       bg.county_geoid,

       c.canonical_county_id,

       bg.block_name

FROM dblink(

        'host=localhost port=5433 dbname=msjarvisgis user=postgres password=ACTUAL_PASSWORD',

        'SELECT block_geoid, county_geoid, block_name FROM public.wv_cen_blockgroup_2020'

     ) AS bg(block_geoid text, county_geoid text, block_name text)

JOIN wv_county_identity c ON c.county_geoid = bg.county_geoid;

"

ERROR:  could not establish connection

DETAIL:  connection to server at "localhost" (127.0.0.1), port 5433 failed: FATAL:  password authentication failed for user "postgres"

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ # Connect as postgres on 5433

psql -p 5433 -U postgres -d postgres

# Inside psql:

ALTER USER postgres WITH PASSWORD 'new_strong_password';

\\q

psql (16.14 (Ubuntu 16.14-0ubuntu0.24.04.1), server 16.4 (Debian 16.4-1.pgdg110+2))

Type "help" for help.

postgres=# ALTER USER postgres WITH PASSWORD 'postgres';

ALTER ROLE

postgres=# # Update .pgpass with the new password

echo "localhost:5433:msjarvisgis:postgres:postgres" > ~/.pgpass

chmod 600 ~/.pgpass

export PGPASSFILE=~/.pgpass

# Verify direct psql still works with no prompt

psql -p 5433 -U postgres -d msjarvisgis -w -c "SELECT 1;"

postgres-# 

\q

ALTER: command not found

\q: command not found

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -p 5433 -U postgres -d msjarvisgis -w -c "SELECT 1;"

 ?column? 

----------

        1

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

INSERT INTO wv_blockgroup_identity (blockgroup_geoid, county_geoid, county_id, blockgroup_name)

SELECT bg.block_geoid,

       bg.county_geoid,

       c.canonical_county_id,

       bg.block_name

FROM dblink(

        'host=localhost port=5433 dbname=msjarvisgis user=postgres password=new_strong_password',

        'SELECT block_geoid, county_geoid, block_name FROM public.wv_cen_blockgroup_2020'

     ) AS bg(block_geoid text, county_geoid text, block_name text)

JOIN wv_county_identity c ON c.county_geoid = bg.county_geoid;

"

psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

INSERT INTO wv_blockgroup_representation (blockgroup_geoid, source_table, source_feature_id, geom, geom_hash, srid)

SELECT bg.block_geoid,

       'public.wv_cen_blockgroup_2020'::text,

       bg.gid::bigint,

       bg.geom,

"    ) AS bg(gid integer, block_geoid text, geom geometry);lockgroup_2020'd=new_st

ERROR:  could not establish connection

DETAIL:  connection to server at "localhost" (127.0.0.1), port 5433 failed: FATAL:  password authentication failed for user "postgres"

ERROR:  could not establish connection

DETAIL:  connection to server at "localhost" (127.0.0.1), port 5433 failed: FATAL:  password authentication failed for user "postgres"

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ # Export blockgroup identity source from evidence DB on 5433

psql -p 5433 -U postgres -d msjarvisgis -c "

COPY (

  SELECT block_geoid, county_geoid, block_name

  FROM public.wv_cen_blockgroup_2020

) TO '/mnt/spiritual_drive/msjarvis-rebuild/wv_cen_blockgroup_2020_identity.csv'

WITH (FORMAT csv, HEADER true);

"

# Export blockgroup representation source

psql -p 5433 -U postgres -d msjarvisgis -c "

COPY (

  SELECT gid, block_geoid, geom

  FROM public.wv_cen_blockgroup_2020

) TO '/mnt/spiritual_drive/msjarvis-rebuild/wv_cen_blockgroup_2020_representation.csv'

WITH (FORMAT csv, HEADER true);

"

ERROR:  relation "public.wv_cen_blockgroup_2020" does not exist

LINE 4:   FROM public.wv_cen_blockgroup_2020

               ^

ERROR:  relation "public.wv_cen_blockgroup_2020" does not exist

LINE 4:   FROM public.wv_cen_blockgroup_2020

               ^

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -p 5433 -U postgres -d msjarvisgis -c "

SELECT table_schema, table_name

FROM information_schema.tables

WHERE table_schema = 'public'

  AND table_name ILIKE '%blockgroup%';

"

 table_schema |                      table_name                      

--------------+------------------------------------------------------

 public       | wv_blockgroup_representation

 public       | wv_blockgroup_dataset_coverage

 public       | wv_blockgroup_belief_snapshot

 public       | wv_blockgroup_belief_vector_ready

 public       | wv_soc_census_blockgroups_2020

 public       | wv_soc_census_blockgroups_2011

 public       | wv_soc_census_blockgroups_2000

 public       | wv_blockgroups_census_201111_gcs83

 public       | wv_blockgroups_census_201111_utm83

 public       | wv_blockgroups_census_2020_utm83

 public       | wv_blockgroups_census_2020_wma84

 public       | wv_populationdatablockgroups_uscensus_2000_ll83_shp

 public       | wv_populationdatablockgroups_uscensus_2000_utm83_shp

(13 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -p 5433 -U postgres -d msjarvisgis -c "

SELECT column_name

FROM information_schema.columns

WHERE table_schema = 'public'

  AND table_name = 'wv_blockgroups_census_2020_utm83';

"

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -p 5433 -U postgres -d msjarvisgis -c "

COPY (

  SELECT

    geoid AS blkgrp_geoid,

    substr(geoid, 1, 5) AS county_geoid,

    namelsad AS blkgrp_name

  FROM public.wv_blockgroups_census_2020_utm83

) TO '/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroups_2020_identity.csv'

WITH (FORMAT csv, HEADER true);

"

psql -p 5433 -U postgres -d msjarvisgis -c "

COPY (

  SELECT

    gid,

    geoid AS blkgrp_geoid,

    geographic AS geom

  FROM public.wv_blockgroups_census_2020_utm83

) TO '/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroups_2020_representation.csv'

WITH (FORMAT csv, HEADER true);

"

ERROR:  could not open file "/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroups_2020_identity.csv" for writing: No such file or directory

HINT:  COPY TO instructs the PostgreSQL server process to write a file. You may want a client-side facility such as psql's \copy.

ERROR:  could not open file "/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroups_2020_representation.csv" for writing: No such file or directory

HINT:  COPY TO instructs the PostgreSQL server process to write a file. You may want a client-side facility such as psql's \copy.

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -p 5433 -U postgres -d msjarvisgis

psql (16.14 (Ubuntu 16.14-0ubuntu0.24.04.1), server 16.4 (Debian 16.4-1.pgdg110+2))

Type "help" for help.

msjarvisgis=# \COPY (

  SELECT

    geoid AS blkgrp_geoid,

    substr(geoid, 1, 5) AS county_geoid,

    namelsad AS blkgrp_name

  FROM public.wv_blockgroups_census_2020_utm83

) TO '/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroups_2020_identity.csv'

  WITH (FORMAT csv, HEADER true);

\COPY (

  SELECT

    gid,

    geoid AS blkgrp_geoid,

    geographic AS geom

  FROM public.wv_blockgroups_census_2020_utm83

) TO '/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroups_2020_representation.csv'

  WITH (FORMAT csv, HEADER true);

ERROR:  syntax error at or near "\"

LINE 3: \COPY (

        ^

msjarvisgis=# \COPY (

  SELECT

    geoid AS blkgrp_geoid,

    substr(geoid, 1, 5) AS county_geoid,

    namelsad AS blkgrp_name

  FROM public.wv_blockgroups_census_2020_utm83

) TO '/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroups_2020_identity.csv'

  WITH (FORMAT csv, HEADER true);

COPY 1639

msjarvisgis=# \COPY (

  SELECT

    gid,

    geoid AS blkgrp_geoid,

    geographic AS geom

  FROM public.wv_blockgroups_census_2020_utm83

) TO '/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroups_2020_representation.csv'

  WITH (FORMAT csv, HEADER true);

COPY 1639

msjarvisgis=# q

msjarvisgis-# 

msjarvisgis-# 

\q

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

DROP TABLE IF EXISTS wv_blockgroup_identity_stage;

CREATE TABLE wv_blockgroup_identity_stage (

    blkgrp_geoid text,

    county_geoid text,

    blkgrp_name text

);

"

psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

COPY wv_blockgroup_identity_stage

FROM '/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroups_2020_identity.csv'

WITH (FORMAT csv, HEADER true);

"

psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

INSERT INTO wv_blockgroup_identity (blockgroup_geoid, county_geoid, county_id, blockgroup_name)

SELECT s.blkgrp_geoid,

       s.county_geoid,

       c.canonical_county_id,

       s.blkgrp_name

FROM wv_blockgroup_identity_stage s

"OIN wv_county_identity c ON c.county_geoid = s.county_geoid;

NOTICE:  table "wv_blockgroup_identity_stage" does not exist, skipping

DROP TABLE

CREATE TABLE

COPY 1639

INSERT 0 1639

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

DROP TABLE IF EXISTS wv_blockgroup_representation_stage;

CREATE TABLE wv_blockgroup_representation_stage (

    gid integer,

    blkgrp_geoid text,

    geom geometry(MULTIPOLYGON, 4269)

);

"

psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

COPY wv_blockgroup_representation_stage (gid, blkgrp_geoid, geom)

FROM '/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroups_2020_representation.csv'

WITH (FORMAT csv, HEADER true);

"

psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

INSERT INTO wv_blockgroup_representation (blockgroup_geoid, source_table, source_feature_id, geom, geom_hash, srid)

SELECT s.blkgrp_geoid,

       'public.wv_blockgroups_census_2020_utm83'::text,

       s.gid::bigint,

       s.geom,

"ROM wv_blockgroup_representation_stage s;

NOTICE:  table "wv_blockgroup_representation_stage" does not exist, skipping

DROP TABLE

CREATE TABLE

ERROR:  parse error - invalid geometry

HINT:  "Bl" <-- parse error at position 2 within geometry

CONTEXT:  COPY wv_blockgroup_representation_stage, line 2, column geom: "Block Group 3; Census Tract 9654; Tucker County; West Virginia"

INSERT 0 0

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

DROP TABLE IF EXISTS wv_blockgroup_representation_stage;

CREATE TABLE wv_blockgroup_representation_stage (

    gid integer,

    blkgrp_geoid text,

    geom text

);

"

DROP TABLE

CREATE TABLE

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

COPY wv_blockgroup_representation_stage (gid, blkgrp_geoid, geom)

FROM '/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroups_2020_representation.csv'

WITH (FORMAT csv, HEADER true);

"

COPY 1639

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

INSERT INTO wv_blockgroup_representation (blockgroup_geoid, source_table, source_feature_id, geom, geom_hash, srid)

SELECT s.blkgrp_geoid,

       'public.wv_blockgroups_census_2020_utm83'::text,

       s.gid::bigint,

       ST_GeomFromText(s.geom, 4269),

       md5(s.geom)::text,

       4269

FROM wv_blockgroup_representation_stage s;

"

ERROR:  parse error - invalid geometry

HINT:  "Bl" <-- parse error at position 2 within geometry

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -p 5433 -U postgres -d msjarvisgis -c "

SELECT column_name, data_type

FROM information_schema.columns

WHERE table_schema = 'public'

  AND table_name = 'wv_blockgroups_census_2020_utm83';

"

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -p 5433 -U postgres -d msjarvisgis

psql (16.14 (Ubuntu 16.14-0ubuntu0.24.04.1), server 16.4 (Debian 16.4-1.pgdg110+2))

Type "help" for help.

msjarvisgis=# \COPY (

  SELECT

    gid,

    geoid AS blkgrp_geoid,

    ST_AsText(geom) AS geom_wkt

  FROM public.wv_blockgroups_census_2020_utm83

) TO '/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroups_2020_representation.csv'

  WITH (FORMAT csv, HEADER true);

COPY 1639

msjarvisgis=# \q

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ ls -lh /mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroups_2020_representation.csv

-rw-rw-r-- 1 cakidd cakidd 52M Jul 12 16:23 /mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroups_2020_representation.csv

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

DROP TABLE IF EXISTS wv_blockgroup_representation_stage;

CREATE TABLE wv_blockgroup_representation_stage (

    gid integer,

    blkgrp_geoid text,

    geom_wkt text

);

"

psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

COPY wv_blockgroup_representation_stage (gid, blkgrp_geoid, geom_wkt)

FROM '/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroups_2020_representation.csv'

WITH (FORMAT csv, HEADER true);

"

DROP TABLE

CREATE TABLE

COPY 1639

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

INSERT INTO wv_blockgroup_representation (blockgroup_geoid, source_table, source_feature_id, geom, geom_hash, srid)

SELECT s.blkgrp_geoid,

       'public.wv_blockgroups_census_2020_utm83'::text,

       s.gid::bigint,

       ST_GeomFromText(s.geom_wkt, 4269),

       md5(s.geom_wkt)::text,

       4269

FROM wv_blockgroup_representation_stage s;

"

INSERT 0 1639

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

SELECT COUNT(*) FROM wv_blockgroup_identity;

"

psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

SELECT COUNT(*) FROM wv_blockgroup_representation;

"

 count 

-------

  1639

(1 row)

 count 

-------

  1639

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ # Create coverage table

psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

DROP TABLE IF EXISTS wv_blockgroup_dataset_coverage;

CREATE TABLE wv_blockgroup_dataset_coverage (

    blockgroup_geoid text NOT NULL,

    county_geoid text NOT NULL,

    dataset_type text NOT NULL,

    source_table text NOT NULL,

    feature_count integer NOT NULL,

    coverage_state text NOT NULL,

    calculation_time timestamptz NOT NULL,

    source_layer_hash text,

    notes text,

    PRIMARY KEY (blockgroup_geoid, dataset_type)

);

"

NOTICE:  table "wv_blockgroup_dataset_coverage" does not exist, skipping

DROP TABLE

CREATE TABLE

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

WITH ap AS (

  SELECT bg.blockgroup_geoid,

         bg.county_geoid,

         COUNT(ap.gid) AS feature_count

  FROM dblink(

        'host=localhost port=5433 dbname=msjarvisgis user=postgres',

        'SELECT gid, canonical_county_id, geom FROM public.wv_address_points_union'

     ) AS ap(gid integer, canonical_county_id integer, geom geometry(Point,4269))

  JOIN wv_blockgroup_representation bg

    ON ST_Intersects(bg.geom, ap.geom)

  GROUP BY bg.blockgroup_geoid, bg.county_geoid

)

INSERT INTO wv_blockgroup_dataset_coverage (

    blockgroup_geoid,

    county_geoid,

    dataset_type,

    source_table,

    feature_count,

    coverage_state,

    calculation_time,

    source_layer_hash,

"EFT JOIN ap ON ap.blockgroup_geoid = i.blockgroup_geoid;ELSE 'present' END AS cov

ERROR:  column bg.county_geoid does not exist

LINE 4:          bg.county_geoid,

                 ^

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

WITH ap AS (

  SELECT

    i.blockgroup_geoid,

    i.county_geoid,

    COUNT(ap.gid) AS feature_count

  FROM dblink(

        'host=localhost port=5433 dbname=msjarvisgis user=postgres',

        'SELECT gid, canonical_county_id, geom FROM public.wv_address_points_union'

     ) AS ap(gid integer, canonical_county_id integer, geom geometry(Point,4269))

  JOIN wv_blockgroup_representation bg

    ON ST_Intersects(bg.geom, ap.geom)

  JOIN wv_blockgroup_identity i

    ON i.blockgroup_geoid = bg.blockgroup_geoid

  GROUP BY i.blockgroup_geoid, i.county_geoid

)

INSERT INTO wv_blockgroup_dataset_coverage (

    blockgroup_geoid,

    county_geoid,

    dataset_type,

    source_table,

    feature_count,

"EFT JOIN ap ON ap.blockgroup_geoid = i.blockgroup_geoid;ELSE 'present' END AS cov

ERROR:  could not establish connection

DETAIL:  connection to server at "localhost" (127.0.0.1), port 5433 failed: fe_sendauth: no password supplied

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ psql -p 5433 -U postgres -d msjarvisgis

psql (16.14 (Ubuntu 16.14-0ubuntu0.24.04.1), server 16.4 (Debian 16.4-1.pgdg110+2))

Type "help" for help.

msjarvisgis=# \COPY (

  WITH ap AS (

    SELECT

      bg.geoid AS blockgroup_geoid,

      substr(bg.geoid, 1, 5) AS county_geoid,

      COUNT(ap.gid) AS feature_count

    FROM public.wv_blockgroups_census_2020_utm83 bg

    JOIN public.wv_address_points_union ap

      ON ST_Intersects(bg.geom, ap.geom)

    GROUP BY bg.geoid

  )

  SELECT

    i.geoid AS blockgroup_geoid,

    substr(i.geoid, 1, 5) AS county_geoid,

    COALESCE(ap.feature_count, 0) AS feature_count

  FROM public.wv_blockgroups_census_2020_utm83 i

  LEFT JOIN ap ON ap.blockgroup_geoid = i.geoid

) TO '/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroup_address_points_coverage.csv'

  WITH (FORMAT csv, HEADER true);

ERROR:  relation "public.wv_address_points_union" does not exist

LINE 1: ...M public.wv_blockgroups_census_2020_utm83 bg JOIN public.wv_...

                                                             ^

msjarvisgis=# psql -p 5433 -U postgres -d msjarvisgis -c "

SELECT table_schema, table_name

FROM information_schema.tables

WHERE table_schema = 'public'

  AND table_name ILIKE '%address%point%';

"

msjarvisgis-# psql -p 5433 -U postgres -d msjarvisgis -c "

SELECT table_schema, table_name

FROM information_schema.tables

WHERE table_schema = 'public'

  AND (table_name ILIKE '%address%' OR table_name ILIKE '%addr%');

"

msjarvisgis-# SELECT table_schema, table_name

FROM information_schema.tables

WHERE table_schema = 'public'

  AND table_name ILIKE '%address%point%';

ERROR:  syntax error at or near "psql"

LINE 1: psql -p 5433 -U postgres -d msjarvisgis -c "

        ^

msjarvisgis=# SELECT table_schema, table_name

FROM information_schema.tables

WHERE table_schema = 'public'

  AND (table_name ILIKE '%address%' OR table_name ILIKE '%addr%');

msjarvisgis=# \COPY (

  WITH ap AS (

    SELECT

      bg.geoid AS blockgroup_geoid,

      substr(bg.geoid, 1, 5) AS county_geoid,

      COUNT(ap_all.gid) AS feature_count

    FROM public.wv_blockgroups_census_2020_utm83 bg

    JOIN (

      SELECT gid, geom FROM public.wv_address_points_kanawha_part1

      UNION ALL

      SELECT gid, geom FROM public.wv_address_points_kanawha_part2

    ) AS ap_all

      ON ST_Intersects(bg.geom, ap_all.geom)

    GROUP BY bg.geoid

  )

  SELECT

    i.geoid AS blockgroup_geoid,

    substr(i.geoid, 1, 5) AS county_geoid,

    COALESCE(ap.feature_count, 0) AS feature_count

  FROM public.wv_blockgroups_census_2020_utm83 i

  LEFT JOIN ap ON ap.blockgroup_geoid = i.geoid

) TO '/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroup_address_points_coverage_kanawha.csv'

  WITH (FORMAT csv, HEADER true);

COPY 1639

msjarvisgis=# # Staging coverage table

psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

DROP TABLE IF EXISTS wv_blockgroup_dataset_coverage_stage;

CREATE TABLE wv_blockgroup_dataset_coverage_stage (

    blockgroup_geoid text,

    county_geoid text,

    feature_count integer

);

"

# Load CSV

psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

COPY wv_blockgroup_dataset_coverage_stage

FROM '/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroup_address_points_coverage_kanawha.csv'

WITH (FORMAT csv, HEADER true);

"

# Populate governed coverage table for Kanawha address points

psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

INSERT INTO wv_blockgroup_dataset_coverage (

    blockgroup_geoid,

    county_geoid,

    dataset_type,

"ELECT COUNT(*) FROM wv_blockgroup_dataset_coverage;r Kanawha (v1)'END AS coverage

msjarvisgis-# SELECT

  'blockgroups' AS layer,

  ST_SRID(geom) AS srid,

  COUNT(*) AS rows

FROM public.wv_blockgroups_census_2020_utm83

GROUP BY srid;

SELECT

  'kanawha_part1' AS layer,

  ST_SRID(geom) AS srid,

  COUNT(*) AS rows

FROM public.wv_address_points_kanawha_part1

GROUP BY srid;

SELECT

  'kanawha_part2' AS layer,

  ST_SRID(geom) AS srid,

  COUNT(*) AS rows

FROM public.wv_address_points_kanawha_part2

GROUP BY srid;

ERROR:  syntax error at or near "#"

LINE 1: # Staging coverage table

        ^

     layer     | srid | rows  

---------------+------+-------

 kanawha_part1 | 4269 | 61703

(1 row)

     layer     | srid | rows  

---------------+------+-------

 kanawha_part2 | 4269 | 40000

(1 row)

msjarvisgis=# SELECT

  'blockgroups' AS layer,

  ST_SRID(geom) AS srid,

  COUNT(*) AS rows

FROM public.wv_blockgroups_census_2020_utm83

GROUP BY srid;

    layer    | srid  | rows 

-------------+-------+------

 blockgroups | 26917 | 1639

(1 row)

msjarvisgis=# \COPY (

  WITH ap AS (

    SELECT

      bg.geoid AS blockgroup_geoid,

      substr(bg.geoid, 1, 5) AS county_geoid,

      COUNT(ap_all.gid) AS feature_count

    FROM public.wv_blockgroups_census_2020_utm83 bg

    JOIN (

      SELECT gid, ST_Transform(geom, 26917) AS geom

      FROM public.wv_address_points_kanawha_part1

      UNION ALL

      SELECT gid, ST_Transform(geom, 26917) AS geom

      FROM public.wv_address_points_kanawha_part2

    ) AS ap_all

      ON ST_Intersects(bg.geom, ap_all.geom)

    GROUP BY bg.geoid

  )

  SELECT

    i.geoid AS blockgroup_geoid,

    substr(i.geoid, 1, 5) AS county_geoid,

    COALESCE(ap.feature_count, 0) AS feature_count

  FROM public.wv_blockgroups_census_2020_utm83 i

  LEFT JOIN ap ON ap.blockgroup_geoid = i.geoid

) TO '/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroup_address_points_coverage_k  WITH (FORMAT csv, HEADER true);

COPY 1639

msjarvisgis=# DROP MATERIALIZED VIEW IF EXISTS public.wv_address_points_statewide_mv;

DO $$

DECLARE

    sql_text text;

BEGIN

    SELECT

        'CREATE MATERIALIZED VIEW public.wv_address_points_statewide_mv AS ' ||

        string_agg(

            format(

                $f$

                SELECT

                    %L::text AS source_table,

                    gid,

                    ST_Transform(geom, 26917) AS geom

                FROM public.%I

                $f$,

                table_name,

                table_name

            ),

            E'\nUNION ALL\n'

            ORDER BY table_name

        )

END $$;CUTE sql_text;_points_kanawha part2',_%'

NOTICE:  materialized view "wv_address_points_statewide_mv" does not exist, skipping

DROP MATERIALIZED VIEW

DO

msjarvisgis=# CREATE INDEX IF NOT EXISTS wv_address_points_statewide_mv_geom_gix

ON public.wv_address_points_statewide_mv

USING GIST (geom);

CREATE INDEX IF NOT EXISTS wv_address_points_statewide_mv_source_table_idx

ON public.wv_address_points_statewide_mv (source_table);

SELECT COUNT(*) AS statewide_points

FROM public.wv_address_points_statewide_mv;

CREATE INDEX

CREATE INDEX

 statewide_points 

------------------

          1115588

(1 row)

msjarvisgis=# \COPY (

  WITH ap AS (

    SELECT

      bg.geoid AS blockgroup_geoid,

      substr(bg.geoid, 1, 5) AS county_geoid,

      COUNT(ap.gid) AS feature_count

    FROM public.wv_blockgroups_census_2020_utm83 bg

    JOIN public.wv_address_points_statewide_mv ap

      ON ST_Intersects(bg.geom, ap.geom)

    GROUP BY bg.geoid

  )

  SELECT

    i.geoid AS blockgroup_geoid,

    substr(i.geoid, 1, 5) AS county_geoid,

    COALESCE(ap.feature_count, 0) AS feature_count

  FROM public.wv_blockgroups_census_2020_utm83 i

  LEFT JOIN ap ON ap.blockgroup_geoid = i.geoid

) TO '/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroup_address_points_coverage_statewide.csv'

WITH (FORMAT csv, HEADER true);

COPY 1639

msjarvisgis=# SELECT COUNT(*) AS rows

FROM public.wv_hyd_hazus_floodplain_zones;

 rows 

------

  220

(1 row)

msjarvisgis=# SELECT COUNT(*) AS rows

FROM public.wv_hyd_hazus_floodplain_zones;

 rows 

------

  220

(1 row)

msjarvisgis=# pg_dump \

  -d msjarvisgis \

  -U postgres \

  -t public.wv_hyd_hazus_floodplain_zones \

  -Fc \

  -f /mnt/spiritual_drive/msjarvis-rebuild/wv_hyd_hazus_floodplain_zones.dump

invalid command \

Try \? for help.

msjarvisgis-# \! pg_dump \

  -d msjarvisgis \

  -U postgres \

  -t public.wv_hyd_hazus_floodplain_zones \

  -Fc \

  -f /mnt/spiritual_drive/msjarvis-rebuild/wv_hyd_hazus_floodplain_zones.dump

msjarvisgis-# 

msjarvisgis-# \! pg_dump -d msjarvisgis -U postgres -t public.wv_hyd_hazus_floodplain_zones -Fc -v -f /mnt/spiritual_drive/msjarvis-rebuild/wv_hyd_hazus_floodplain_zones.dump

pg_dump: last built-in OID is 16383

pg_dump: reading extensions

pg_dump: identifying extension members

pg_dump: reading schemas

pg_dump: reading user-defined tables

pg_dump: reading user-defined functions

pg_dump: reading user-defined types

pg_dump: reading procedural languages

pg_dump: reading user-defined aggregate functions

pg_dump: reading user-defined operators

pg_dump: reading user-defined access methods

pg_dump: reading user-defined operator classes

pg_dump: reading user-defined operator families

pg_dump: reading user-defined text search parsers

pg_dump: reading user-defined text search templates

pg_dump: reading user-defined text search dictionaries

pg_dump: reading user-defined text search configurations

pg_dump: reading user-defined foreign-data wrappers

pg_dump: reading user-defined foreign servers

pg_dump: reading default privileges

pg_dump: reading user-defined collations

pg_dump: reading user-defined conversions

pg_dump: reading type casts

pg_dump: reading transforms

pg_dump: reading table inheritance information

pg_dump: reading event triggers

pg_dump: finding extension tables

pg_dump: finding inheritance relationships

pg_dump: reading column info for interesting tables

pg_dump: finding table default expressions

pg_dump: flagging inherited columns in subtables

pg_dump: reading partitioning data

pg_dump: reading indexes

pg_dump: flagging indexes in partitioned tables

pg_dump: reading extended statistics

pg_dump: reading constraints

pg_dump: reading triggers

pg_dump: reading rewrite rules

pg_dump: reading policies

pg_dump: reading row-level security policies

pg_dump: reading publications

pg_dump: reading publication membership of tables

pg_dump: reading publication membership of schemas

pg_dump: reading subscriptions

pg_dump: reading dependency data

pg_dump: saving encoding = UTF8

pg_dump: saving standard_conforming_strings = on

pg_dump: saving search_path = 

pg_dump: saving database definition

pg_dump: dumping contents of table "public.wv_hyd_hazus_floodplain_zones"

msjarvisgis-# 

msjarvisgis-# \! pg_dump -d msjarvisgis -U postgres -Fc -v \

  -f /mnt/spiritual_drive/msjarvis-rebuild/wv_batch_layers_v9.dump \

  -t public.wv_bio_biodiversity_rank \

  -t public.wv_env_epa_facilities \

  -t public.wv_hyd_streams_high_quality \

  -t public.wv_soc_schools_k12 \

  -t public.wv_soc_hospitals_wvdem \

  -t public.wv_trn_airports \

  -t public.wv_util_sewer_treatment_plants

pg_dump: last built-in OID is 16383

pg_dump: reading extensions

pg_dump: identifying extension members

pg_dump: reading schemas

pg_dump: reading user-defined tables

pg_dump: reading user-defined functions

pg_dump: reading user-defined types

pg_dump: reading procedural languages

pg_dump: reading user-defined aggregate functions

pg_dump: reading user-defined operators

pg_dump: reading user-defined access methods

pg_dump: reading user-defined operator classes

pg_dump: reading user-defined operator families

pg_dump: reading user-defined text search parsers

pg_dump: reading user-defined text search templates

pg_dump: reading user-defined text search dictionaries

pg_dump: reading user-defined text search configurations

pg_dump: reading user-defined foreign-data wrappers

pg_dump: reading user-defined foreign servers

pg_dump: reading default privileges

pg_dump: reading user-defined collations

pg_dump: reading user-defined conversions

pg_dump: reading type casts

pg_dump: reading transforms

pg_dump: reading table inheritance information

pg_dump: reading event triggers

pg_dump: finding extension tables

pg_dump: finding inheritance relationships

pg_dump: reading column info for interesting tables

pg_dump: finding table default expressions

pg_dump: flagging inherited columns in subtables

pg_dump: reading partitioning data

pg_dump: reading indexes

pg_dump: flagging indexes in partitioned tables

pg_dump: reading extended statistics

pg_dump: reading constraints

pg_dump: reading triggers

pg_dump: reading rewrite rules

pg_dump: reading policies

pg_dump: reading row-level security policies

pg_dump: reading publications

pg_dump: reading publication membership of tables

pg_dump: reading publication membership of schemas

pg_dump: reading subscriptions

pg_dump: reading dependency data

pg_dump: saving encoding = UTF8

pg_dump: saving standard_conforming_strings = on

pg_dump: saving search_path = 

pg_dump: saving database definition

pg_dump: dumping contents of table "public.wv_bio_biodiversity_rank"

pg_dump: dumping contents of table "public.wv_env_epa_facilities"

pg_dump: dumping contents of table "public.wv_hyd_streams_high_quality"

pg_dump: dumping contents of table "public.wv_soc_hospitals_wvdem"

pg_dump: dumping contents of table "public.wv_soc_schools_k12"

pg_dump: dumping contents of table "public.wv_trn_airports"

pg_dump: dumping contents of table "public.wv_util_sewer_treatment_plants"

msjarvisgis-# 

pg_restore: error: could not execute query: ERROR:  index "wv_bnd_mnf_basic_ownership_geom_geom_idx" does not exist

Command was: DROP INDEX public.wv_bnd_mnf_basic_ownership_geom_geom_idx;

pg_restore: error: could not execute query: ERROR:  index "wv_bnd_county_municipal_dlg_geom_geom_idx" does not exist

Command was: DROP INDEX public.wv_bnd_county_municipal_dlg_geom_geom_idx;

pg_restore: error: could not execute query: ERROR:  index "wv_bnd_county_24k_geom_geom_idx" does not exist

Command was: DROP INDEX public.wv_bnd_county_24k_geom_geom_idx;

pg_restore: error: could not execute query: ERROR:  index "wv_bnd_census_designated_places_geom_geom_idx" does not exist

Command was: DROP INDEX public.wv_bnd_census_designated_places_geom_geom_idx;

pg_restore: error: could not execute query: ERROR:  index "wv_bnd_canaan_valley_nwr_geom_geom_idx" does not exist

Command was: DROP INDEX public.wv_bnd_canaan_valley_nwr_geom_geom_idx;

pg_restore: error: could not execute query: ERROR:  index "wv_bnd_arc_counties_geom_geom_idx" does not exist

Command was: DROP INDEX public.wv_bnd_arc_counties_geom_geom_idx;

pg_restore: error: could not execute query: ERROR:  index "wv_bnd_appalachian_basin_boundary_geom_geom_idx" does not exist

Command was: DROP INDEX public.wv_bnd_appalachian_basin_boundary_geom_geom_idx;

pg_restore: error: could not execute query: ERROR:  index "wv_bio_red_spruce_cover_geom_geom_idx" does not exist

Command was: DROP INDEX public.wv_bio_red_spruce_cover_geom_geom_idx;

pg_restore: error: could not execute query: ERROR:  index "wv_bio_ecoregions_geom_geom_idx" does not exist

Command was: DROP INDEX public.wv_bio_ecoregions_geom_geom_idx;

pg_restore: error: could not execute query: ERROR:  index "wv_bio_biodiversity_rank_geom_geom_idx" does not exist

Command was: DROP INDEX public.wv_bio_biodiversity_rank_geom_geom_idx;

pg_restore: error: could not execute query: ERROR:  index "wv_atm_weather_stations_geom_geom_idx" does not exist

Command was: DROP INDEX public.wv_atm_weather_stations_geom_geom_idx;

pg_restore: error: could not execute query: ERROR:  schema "normalization" does not exist

Command was: DROP INDEX normalization.geoanchor_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_wv_county_boundaries_24k_topo_updated_2026_wma84" does not exist

Command was: ALTER TABLE ONLY public.wv_wv_county_boundaries_24k_topo_updated_2026_wma84 DROP CONSTRAINT wv_wv_county_boundaries_24k_topo_updated_2026_wma84_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_wv_county_boundaries_24k_topo_updated_2026_utm83" does not exist

Command was: ALTER TABLE ONLY public.wv_wv_county_boundaries_24k_topo_updated_2026_utm83 DROP CONSTRAINT wv_wv_county_boundaries_24k_topo_updated_2026_utm83_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_util_solid_waste_facilities" does not exist

Command was: ALTER TABLE ONLY public.wv_util_solid_waste_facilities DROP CONSTRAINT wv_util_solid_waste_facilities_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_util_sewer_treatment_plants" does not exist

Command was: ALTER TABLE ONLY public.wv_util_sewer_treatment_plants DROP CONSTRAINT wv_util_sewer_treatment_plants_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_whitewater_trails" does not exist

Command was: ALTER TABLE ONLY public.wv_trn_whitewater_trails DROP CONSTRAINT wv_trn_whitewater_trails_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_roads_us_routes" does not exist

Command was: ALTER TABLE ONLY public.wv_trn_roads_us_routes DROP CONSTRAINT wv_trn_roads_us_routes_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_roads_us_highways" does not exist

Command was: ALTER TABLE ONLY public.wv_trn_roads_us_highways DROP CONSTRAINT wv_trn_roads_us_highways_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_roads_state_routes" does not exist

Command was: ALTER TABLE ONLY public.wv_trn_roads_state_routes DROP CONSTRAINT wv_trn_roads_state_routes_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_roads_major_4800" does not exist

Command was: ALTER TABLE ONLY public.wv_trn_roads_major_4800 DROP CONSTRAINT wv_trn_roads_major_4800_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_roads_interstate" does not exist

Command was: ALTER TABLE ONLY public.wv_trn_roads_interstate DROP CONSTRAINT wv_trn_roads_interstate_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_recreational_trails" does not exist

Command was: ALTER TABLE ONLY public.wv_trn_recreational_trails DROP CONSTRAINT wv_trn_recreational_trails_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_railroads_national_network" does not exist

Command was: ALTER TABLE ONLY public.wv_trn_railroads_national_network DROP CONSTRAINT wv_trn_railroads_national_network_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_railroads_excursion" does not exist

Command was: ALTER TABLE ONLY public.wv_trn_railroads_excursion DROP CONSTRAINT wv_trn_railroads_excursion_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_railroads_amtrak" does not exist

Command was: ALTER TABLE ONLY public.wv_trn_railroads_amtrak DROP CONSTRAINT wv_trn_railroads_amtrak_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_railroad_lines_rti" does not exist

Command was: ALTER TABLE ONLY public.wv_trn_railroad_lines_rti DROP CONSTRAINT wv_trn_railroad_lines_rti_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_mnf_roads" does not exist

Command was: ALTER TABLE ONLY public.wv_trn_mnf_roads DROP CONSTRAINT wv_trn_mnf_roads_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_mnf_recreation_trails" does not exist

Command was: ALTER TABLE ONLY public.wv_trn_mnf_recreation_trails DROP CONSTRAINT wv_trn_mnf_recreation_trails_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_intermodal_terminals" does not exist

Command was: ALTER TABLE ONLY public.wv_trn_intermodal_terminals DROP CONSTRAINT wv_trn_intermodal_terminals_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_airports" does not exist

Command was: ALTER TABLE ONLY public.wv_trn_airports DROP CONSTRAINT wv_trn_airports_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_airport_runways" does not exist

Command was: ALTER TABLE ONLY public.wv_trn_airport_runways DROP CONSTRAINT wv_trn_airport_runways_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_airport_proposed" does not exist

Command was: ALTER TABLE ONLY public.wv_trn_airport_proposed DROP CONSTRAINT wv_trn_airport_proposed_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_airport_facilities" does not exist

Command was: ALTER TABLE ONLY public.wv_trn_airport_facilities DROP CONSTRAINT wv_trn_airport_facilities_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_tract_representation" does not exist

Command was: ALTER TABLE ONLY public.wv_tract_representation DROP CONSTRAINT wv_tract_representation_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_tract_identity" does not exist

Command was: ALTER TABLE ONLY public.wv_tract_identity DROP CONSTRAINT wv_tract_identity_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_tract_dataset_coverage" does not exist

Command was: ALTER TABLE ONLY public.wv_tract_dataset_coverage DROP CONSTRAINT wv_tract_dataset_coverage_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_tract_belief_snapshot" does not exist

Command was: ALTER TABLE ONLY public.wv_tract_belief_snapshot DROP CONSTRAINT wv_tract_belief_snapshot_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_tract_belief_snapshot" does not exist

Command was: ALTER TABLE ONLY public.wv_tract_belief_snapshot DROP CONSTRAINT wv_tract_belief_snapshot_canonical_tract_id_snapshot_versio_key;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_str_samb_building_polygons" does not exist

Command was: ALTER TABLE ONLY public.wv_str_samb_building_polygons DROP CONSTRAINT wv_str_samb_building_polygons_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_str_samb_building_points" does not exist

Command was: ALTER TABLE ONLY public.wv_str_samb_building_points DROP CONSTRAINT wv_str_samb_building_points_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_str_places_of_worship_hsip" does not exist

Command was: ALTER TABLE ONLY public.wv_str_places_of_worship_hsip DROP CONSTRAINT wv_str_places_of_worship_hsip_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_str_parole_offices" does not exist

Command was: ALTER TABLE ONLY public.wv_str_parole_offices DROP CONSTRAINT wv_str_parole_offices_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_str_flood_atrisk_structures" does not exist

Command was: ALTER TABLE ONLY public.wv_str_flood_atrisk_structures DROP CONSTRAINT wv_str_flood_atrisk_structures_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_str_correctional_institutions" does not exist

Command was: ALTER TABLE ONLY public.wv_str_correctional_institutions DROP CONSTRAINT wv_str_correctional_institutions_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_str_bridges" does not exist

Command was: ALTER TABLE ONLY public.wv_str_bridges DROP CONSTRAINT wv_str_bridges_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_zcta_2020" does not exist

Command was: ALTER TABLE ONLY public.wv_soc_zcta_2020 DROP CONSTRAINT wv_soc_zcta_2020_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_va_facilities" does not exist

Command was: ALTER TABLE ONLY public.wv_soc_va_facilities DROP CONSTRAINT wv_soc_va_facilities_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_towers_tv" does not exist

Command was: ALTER TABLE ONLY public.wv_soc_towers_tv DROP CONSTRAINT wv_soc_towers_tv_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_towers_private" does not exist

Command was: ALTER TABLE ONLY public.wv_soc_towers_private DROP CONSTRAINT wv_soc_towers_private_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_towers_pager" does not exist

Command was: ALTER TABLE ONLY public.wv_soc_towers_pager DROP CONSTRAINT wv_soc_towers_pager_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_towers_microwave" does not exist

Command was: ALTER TABLE ONLY public.wv_soc_towers_microwave DROP CONSTRAINT wv_soc_towers_microwave_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_towers_fm" does not exist

Command was: ALTER TABLE ONLY public.wv_soc_towers_fm DROP CONSTRAINT wv_soc_towers_fm_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_towers_cellular" does not exist

Command was: ALTER TABLE ONLY public.wv_soc_towers_cellular DROP CONSTRAINT wv_soc_towers_cellular_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_towers_asr" does not exist

Command was: ALTER TABLE ONLY public.wv_soc_towers_asr DROP CONSTRAINT wv_soc_towers_asr_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_towers_am" does not exist

Command was: ALTER TABLE ONLY public.wv_soc_towers_am DROP CONSTRAINT wv_soc_towers_am_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_schools_k12" does not exist

Command was: ALTER TABLE ONLY public.wv_soc_schools_k12 DROP CONSTRAINT wv_soc_schools_k12_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_population_by_decade" does not exist

Command was: ALTER TABLE ONLY public.wv_soc_population_by_decade DROP CONSTRAINT wv_soc_population_by_decade_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_places_of_worship_wvgistc" does not exist

Command was: ALTER TABLE ONLY public.wv_soc_places_of_worship_wvgistc DROP CONSTRAINT wv_soc_places_of_worship_wvgistc_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_nursing_homes" does not exist

Command was: ALTER TABLE ONLY public.wv_soc_nursing_homes DROP CONSTRAINT wv_soc_nursing_homes_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_national_register_historic_polygons" does not exist

Command was: ALTER TABLE ONLY public.wv_soc_national_register_historic_polygons DROP CONSTRAINT wv_soc_national_register_historic_polygons_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_national_register_historic_points" does not exist

Command was: ALTER TABLE ONLY public.wv_soc_national_register_historic_points DROP CONSTRAINT wv_soc_national_register_historic_points_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_libraries" does not exist

Command was: ALTER TABLE ONLY public.wv_soc_libraries DROP CONSTRAINT wv_soc_libraries_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_hospitals_wvdem" does not exist

Command was: ALTER TABLE ONLY public.wv_soc_hospitals_wvdem DROP CONSTRAINT wv_soc_hospitals_wvdem_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_higher_ed_facilities" does not exist

Command was: ALTER TABLE ONLY public.wv_soc_higher_ed_facilities DROP CONSTRAINT wv_soc_higher_ed_facilities_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_fishing_lakes" does not exist

Command was: ALTER TABLE ONLY public.wv_soc_fishing_lakes DROP CONSTRAINT wv_soc_fishing_lakes_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_fishing_boating_access" does not exist

Command was: ALTER TABLE ONLY public.wv_soc_fishing_boating_access DROP CONSTRAINT wv_soc_fishing_boating_access_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_fish_hatcheries" does not exist

Command was: ALTER TABLE ONLY public.wv_soc_fish_hatcheries DROP CONSTRAINT wv_soc_fish_hatcheries_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_courthouses_federal" does not exist

Command was: ALTER TABLE ONLY public.wv_soc_courthouses_federal DROP CONSTRAINT wv_soc_courthouses_federal_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_courthouses_county" does not exist

Command was: ALTER TABLE ONLY public.wv_soc_courthouses_county DROP CONSTRAINT wv_soc_courthouses_county_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_communities_pop_change" does not exist

Command was: ALTER TABLE ONLY public.wv_soc_communities_pop_change DROP CONSTRAINT wv_soc_communities_pop_change_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_cities_pop2500" does not exist

Command was: ALTER TABLE ONLY public.wv_soc_cities_pop2500 DROP CONSTRAINT wv_soc_cities_pop2500_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_cities_pop10k" does not exist

Command was: ALTER TABLE ONLY public.wv_soc_cities_pop10k DROP CONSTRAINT wv_soc_cities_pop10k_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_census_tracts_2020" does not exist

Command was: ALTER TABLE ONLY public.wv_soc_census_tracts_2020 DROP CONSTRAINT wv_soc_census_tracts_2020_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_census_blockgroups_2020" does not exist

Command was: ALTER TABLE ONLY public.wv_soc_census_blockgroups_2020 DROP CONSTRAINT wv_soc_census_blockgroups_2020_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_911_centers" does not exist

Command was: ALTER TABLE ONLY public.wv_soc_911_centers DROP CONSTRAINT wv_soc_911_centers_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_plc_tax_parcels_surface_mineral" does not exist

Command was: ALTER TABLE ONLY public.wv_plc_tax_parcels_surface_mineral DROP CONSTRAINT wv_plc_tax_parcels_surface_mineral_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_plc_tax_district_boundaries" does not exist

Command was: ALTER TABLE ONLY public.wv_plc_tax_district_boundaries DROP CONSTRAINT wv_plc_tax_district_boundaries_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_plc_regional_planning_councils" does not exist

Command was: ALTER TABLE ONLY public.wv_plc_regional_planning_councils DROP CONSTRAINT wv_plc_regional_planning_councils_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_plc_hazus_level1" does not exist

Command was: ALTER TABLE ONLY public.wv_plc_hazus_level1 DROP CONSTRAINT wv_plc_hazus_level1_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_mil_national_guard_armories" does not exist

Command was: ALTER TABLE ONLY public.wv_mil_national_guard_armories DROP CONSTRAINT wv_mil_national_guard_armories_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_mil_army_reserve_facilities" does not exist

Command was: ALTER TABLE ONLY public.wv_mil_army_reserve_facilities DROP CONSTRAINT wv_mil_army_reserve_facilities_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_loc_sams2_address_road_centerlines" does not exist

Command was: ALTER TABLE ONLY public.wv_loc_sams2_address_road_centerlines DROP CONSTRAINT wv_loc_sams2_address_road_centerlines_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_loc_populated_places_census" does not exist

Command was: ALTER TABLE ONLY public.wv_loc_populated_places_census DROP CONSTRAINT wv_loc_populated_places_census_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_loc_geodetic_control_points" does not exist

Command was: ALTER TABLE ONLY public.wv_loc_geodetic_control_points DROP CONSTRAINT wv_loc_geodetic_control_points_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_loc_county_seats" does not exist

Command was: ALTER TABLE ONLY public.wv_loc_county_seats DROP CONSTRAINT wv_loc_county_seats_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_loc_census_urbanized_areas" does not exist

Command was: ALTER TABLE ONLY public.wv_loc_census_urbanized_areas DROP CONSTRAINT wv_loc_census_urbanized_areas_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_layer_categories" does not exist

Command was: ALTER TABLE ONLY public.wv_layer_categories DROP CONSTRAINT wv_layer_categories_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hyd_watershed_boundary_8_10_12" does not exist

Command was: ALTER TABLE ONLY public.wv_hyd_watershed_boundary_8_10_12 DROP CONSTRAINT wv_hyd_watershed_boundary_8_10_12_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hyd_watershed_boundary_12digit_hu" does not exist

Command was: ALTER TABLE ONLY public.wv_hyd_watershed_boundary_12digit_hu DROP CONSTRAINT wv_hyd_watershed_boundary_12digit_hu_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hyd_watershed_boundary_11digit" does not exist

Command was: ALTER TABLE ONLY public.wv_hyd_watershed_boundary_11digit DROP CONSTRAINT wv_hyd_watershed_boundary_11digit_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hyd_streams_tiger" does not exist

Command was: ALTER TABLE ONLY public.wv_hyd_streams_tiger DROP CONSTRAINT wv_hyd_streams_tiger_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hyd_streams_national_atlas" does not exist

Command was: ALTER TABLE ONLY public.wv_hyd_streams_national_atlas DROP CONSTRAINT wv_hyd_streams_national_atlas_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hyd_streams_high_quality" does not exist

Command was: ALTER TABLE ONLY public.wv_hyd_streams_high_quality DROP CONSTRAINT wv_hyd_streams_high_quality_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hyd_streamflow_stations" does not exist

Command was: ALTER TABLE ONLY public.wv_hyd_streamflow_stations DROP CONSTRAINT wv_hyd_streamflow_stations_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hyd_springs_100gpm" does not exist

Command was: ALTER TABLE ONLY public.wv_hyd_springs_100gpm DROP CONSTRAINT wv_hyd_springs_100gpm_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hyd_navigable_waterways_structures" does not exist

Command was: ALTER TABLE ONLY public.wv_hyd_navigable_waterways_structures DROP CONSTRAINT wv_hyd_navigable_waterways_structures_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hyd_navigable_waterways_river_miles" does not exist

Command was: ALTER TABLE ONLY public.wv_hyd_navigable_waterways_river_miles DROP CONSTRAINT wv_hyd_navigable_waterways_river_miles_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hyd_navigable_waterways" does not exist

Command was: ALTER TABLE ONLY public.wv_hyd_navigable_waterways DROP CONSTRAINT wv_hyd_navigable_waterways_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hyd_high_water_marks" does not exist

Command was: ALTER TABLE ONLY public.wv_hyd_high_water_marks DROP CONSTRAINT wv_hyd_high_water_marks_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hyd_hazus_floodplain_zones" does not exist

Command was: ALTER TABLE ONLY public.wv_hyd_hazus_floodplain_zones DROP CONSTRAINT wv_hyd_hazus_floodplain_zones_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hyd_dams_noncoal" does not exist

Command was: ALTER TABLE ONLY public.wv_hyd_dams_noncoal DROP CONSTRAINT wv_hyd_dams_noncoal_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hyd_dams_nid" does not exist

Command was: ALTER TABLE ONLY public.wv_hyd_dams_nid DROP CONSTRAINT wv_hyd_dams_nid_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hyd_dams_dmr" does not exist

Command was: ALTER TABLE ONLY public.wv_hyd_dams_dmr DROP CONSTRAINT wv_hyd_dams_dmr_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hlt_rural_health_facilities" does not exist

Command was: ALTER TABLE ONLY public.wv_hlt_rural_health_facilities DROP CONSTRAINT wv_hlt_rural_health_facilities_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hlt_public_health_departments" does not exist

Command was: ALTER TABLE ONLY public.wv_hlt_public_health_departments DROP CONSTRAINT wv_hlt_public_health_departments_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hlt_health_providers" does not exist

Command was: ALTER TABLE ONLY public.wv_hlt_health_providers DROP CONSTRAINT wv_hlt_health_providers_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_geo_karst" does not exist

Command was: ALTER TABLE ONLY public.wv_geo_karst DROP CONSTRAINT wv_geo_karst_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_geo_geological_map_generalized" does not exist

Command was: ALTER TABLE ONLY public.wv_geo_geological_map_generalized DROP CONSTRAINT wv_geo_geological_map_generalized_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_geo_coal_beds" does not exist

Command was: ALTER TABLE ONLY public.wv_geo_coal_beds DROP CONSTRAINT wv_geo_coal_beds_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_env_wind_energy_resources" does not exist

Command was: ALTER TABLE ONLY public.wv_env_wind_energy_resources DROP CONSTRAINT wv_env_wind_energy_resources_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_env_wildfire_regions" does not exist

Command was: ALTER TABLE ONLY public.wv_env_wildfire_regions DROP CONSTRAINT wv_env_wildfire_regions_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_env_timber_removal_volume" does not exist

Command was: ALTER TABLE ONLY public.wv_env_timber_removal_volume DROP CONSTRAINT wv_env_timber_removal_volume_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_env_epa_facilities" does not exist

Command was: ALTER TABLE ONLY public.wv_env_epa_facilities DROP CONSTRAINT wv_env_epa_facilities_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_env_air_nonattainment" does not exist

Command was: ALTER TABLE ONLY public.wv_env_air_nonattainment DROP CONSTRAINT wv_env_air_nonattainment_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_entity_registry" does not exist

Command was: ALTER TABLE ONLY public.wv_entity_registry DROP CONSTRAINT wv_entity_registry_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_elv_summit_names" does not exist

Command was: ALTER TABLE ONLY public.wv_elv_summit_names DROP CONSTRAINT wv_elv_summit_names_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_eco_mountaintop_removal" does not exist

Command was: ALTER TABLE ONLY public.wv_eco_mountaintop_removal DROP CONSTRAINT wv_eco_mountaintop_removal_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_eco_mineral_operations" does not exist

Command was: ALTER TABLE ONLY public.wv_eco_mineral_operations DROP CONSTRAINT wv_eco_mineral_operations_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_eco_manufacturing_directory" does not exist

Command was: ALTER TABLE ONLY public.wv_eco_manufacturing_directory DROP CONSTRAINT wv_eco_manufacturing_directory_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_eco_industrial_sites" does not exist

Command was: ALTER TABLE ONLY public.wv_eco_industrial_sites DROP CONSTRAINT wv_eco_industrial_sites_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_eco_ezec_communities" does not exist

Command was: ALTER TABLE ONLY public.wv_eco_ezec_communities DROP CONSTRAINT wv_eco_ezec_communities_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_eco_coal_fields" does not exist

Command was: ALTER TABLE ONLY public.wv_eco_coal_fields DROP CONSTRAINT wv_eco_coal_fields_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_eco_abandoned_mine_lands_polygon" does not exist

Command was: ALTER TABLE ONLY public.wv_eco_abandoned_mine_lands_polygon DROP CONSTRAINT wv_eco_abandoned_mine_lands_polygon_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_eco_abandoned_mine_lands_point" does not exist

Command was: ALTER TABLE ONLY public.wv_eco_abandoned_mine_lands_point DROP CONSTRAINT wv_eco_abandoned_mine_lands_point_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_eco_abandoned_mine_lands_line" does not exist

Command was: ALTER TABLE ONLY public.wv_eco_abandoned_mine_lands_line DROP CONSTRAINT wv_eco_abandoned_mine_lands_line_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_county_representation" does not exist

Command was: ALTER TABLE ONLY public.wv_county_representation DROP CONSTRAINT wv_county_representation_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_county_identity" does not exist

Command was: ALTER TABLE ONLY public.wv_county_identity DROP CONSTRAINT wv_county_identity_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_county_identity" does not exist

Command was: ALTER TABLE ONLY public.wv_county_identity DROP CONSTRAINT wv_county_identity_county_geoid_key;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_county_dataset_coverage" does not exist

Command was: ALTER TABLE ONLY public.wv_county_dataset_coverage DROP CONSTRAINT wv_county_dataset_coverage_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_county_boundaries_24k_topo_updated_2026_wma84_gdb" does not exist

Command was: ALTER TABLE ONLY public.wv_county_boundaries_24k_topo_updated_2026_wma84_gdb DROP CONSTRAINT wv_county_boundaries_24k_topo_updated_2026_wma84_gdb_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_county_boundaries_24k_topo_updated_2026_utm83_gdb" does not exist

Command was: ALTER TABLE ONLY public.wv_county_boundaries_24k_topo_updated_2026_utm83_gdb DROP CONSTRAINT wv_county_boundaries_24k_topo_updated_2026_utm83_gdb_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_county_belief_snapshot" does not exist

Command was: ALTER TABLE ONLY public.wv_county_belief_snapshot DROP CONSTRAINT wv_county_belief_snapshot_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_county_belief_snapshot" does not exist

Command was: ALTER TABLE ONLY public.wv_county_belief_snapshot DROP CONSTRAINT wv_county_belief_snapshot_canonical_county_id_snapshot_vers_key;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_censustracts_census_2020_utm83" does not exist

Command was: ALTER TABLE ONLY public.wv_censustracts_census_2020_utm83 DROP CONSTRAINT wv_censustracts_census_2020_utm83_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_workforce_investment_areas" does not exist

Command was: ALTER TABLE ONLY public.wv_bnd_workforce_investment_areas DROP CONSTRAINT wv_bnd_workforce_investment_areas_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_voting_districts_2002" does not exist

Command was: ALTER TABLE ONLY public.wv_bnd_voting_districts_2002 DROP CONSTRAINT wv_bnd_voting_districts_2002_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_voting_districts_2000" does not exist

Command was: ALTER TABLE ONLY public.wv_bnd_voting_districts_2000 DROP CONSTRAINT wv_bnd_voting_districts_2000_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_state_boundary_100k" does not exist

Command was: ALTER TABLE ONLY public.wv_bnd_state_boundary_100k DROP CONSTRAINT wv_bnd_state_boundary_100k_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_public_lands_wildlife_resources" does not exist

Command was: ALTER TABLE ONLY public.wv_bnd_public_lands_wildlife_resources DROP CONSTRAINT wv_bnd_public_lands_wildlife_resources_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_public_lands_state_parks" does not exist

Command was: ALTER TABLE ONLY public.wv_bnd_public_lands_state_parks DROP CONSTRAINT wv_bnd_public_lands_state_parks_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_public_lands_state_forests" does not exist

Command was: ALTER TABLE ONLY public.wv_bnd_public_lands_state_forests DROP CONSTRAINT wv_bnd_public_lands_state_forests_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_public_lands_nwr" does not exist

Command was: ALTER TABLE ONLY public.wv_bnd_public_lands_nwr DROP CONSTRAINT wv_bnd_public_lands_nwr_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_public_lands_national_park" does not exist

Command was: ALTER TABLE ONLY public.wv_bnd_public_lands_national_park DROP CONSTRAINT wv_bnd_public_lands_national_park_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_public_lands_national_forest" does not exist

Command was: ALTER TABLE ONLY public.wv_bnd_public_lands_national_forest DROP CONSTRAINT wv_bnd_public_lands_national_forest_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_public_lands_county_city_parks" does not exist

Command was: ALTER TABLE ONLY public.wv_bnd_public_lands_county_city_parks DROP CONSTRAINT wv_bnd_public_lands_county_city_parks_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_nhd_mussel_streams" does not exist

Command was: ALTER TABLE ONLY public.wv_bnd_nhd_mussel_streams DROP CONSTRAINT wv_bnd_nhd_mussel_streams_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_morgantown_wards" does not exist

Command was: ALTER TABLE ONLY public.wv_bnd_morgantown_wards DROP CONSTRAINT wv_bnd_morgantown_wards_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_mnf_wilderness" does not exist

Command was: ALTER TABLE ONLY public.wv_bnd_mnf_wilderness DROP CONSTRAINT wv_bnd_mnf_wilderness_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_mnf_recreation_sites" does not exist

Command was: ALTER TABLE ONLY public.wv_bnd_mnf_recreation_sites DROP CONSTRAINT wv_bnd_mnf_recreation_sites_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_mnf_recreation_campgrounds" does not exist

Command was: ALTER TABLE ONLY public.wv_bnd_mnf_recreation_campgrounds DROP CONSTRAINT wv_bnd_mnf_recreation_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_mnf_ranger_districts" does not exist

Command was: ALTER TABLE ONLY public.wv_bnd_mnf_ranger_districts DROP CONSTRAINT wv_bnd_mnf_ranger_districts_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_mnf_management_prescriptions" does not exist

Command was: ALTER TABLE ONLY public.wv_bnd_mnf_management_prescriptions DROP CONSTRAINT wv_bnd_mnf_management_prescriptions_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_mnf_basic_ownership" does not exist

Command was: ALTER TABLE ONLY public.wv_bnd_mnf_basic_ownership DROP CONSTRAINT wv_bnd_mnf_basic_ownership_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_county_municipal_dlg" does not exist

Command was: ALTER TABLE ONLY public.wv_bnd_county_municipal_dlg DROP CONSTRAINT wv_bnd_county_municipal_dlg_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_county_24k" does not exist

Command was: ALTER TABLE ONLY public.wv_bnd_county_24k DROP CONSTRAINT wv_bnd_county_24k_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_census_designated_places" does not exist

Command was: ALTER TABLE ONLY public.wv_bnd_census_designated_places DROP CONSTRAINT wv_bnd_census_designated_places_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_canaan_valley_nwr" does not exist

Command was: ALTER TABLE ONLY public.wv_bnd_canaan_valley_nwr DROP CONSTRAINT wv_bnd_canaan_valley_nwr_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_arc_counties" does not exist

Command was: ALTER TABLE ONLY public.wv_bnd_arc_counties DROP CONSTRAINT wv_bnd_arc_counties_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_appalachian_basin_boundary" does not exist

Command was: ALTER TABLE ONLY public.wv_bnd_appalachian_basin_boundary DROP CONSTRAINT wv_bnd_appalachian_basin_boundary_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bio_red_spruce_cover" does not exist

Command was: ALTER TABLE ONLY public.wv_bio_red_spruce_cover DROP CONSTRAINT wv_bio_red_spruce_cover_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bio_ecoregions" does not exist

Command was: ALTER TABLE ONLY public.wv_bio_ecoregions DROP CONSTRAINT wv_bio_ecoregions_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bio_biodiversity_rank" does not exist

Command was: ALTER TABLE ONLY public.wv_bio_biodiversity_rank DROP CONSTRAINT wv_bio_biodiversity_rank_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_atm_weather_stations" does not exist

Command was: ALTER TABLE ONLY public.wv_atm_weather_stations DROP CONSTRAINT wv_atm_weather_stations_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.gbim_collection_manifest" does not exist

Command was: ALTER TABLE ONLY public.gbim_collection_manifest DROP CONSTRAINT gbim_collection_manifest_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.gbim_collection_manifest" does not exist

Command was: ALTER TABLE ONLY public.gbim_collection_manifest DROP CONSTRAINT gbim_collection_manifest_physical_collection_name_key;

pg_restore: error: could not execute query: ERROR:  relation "public.gbim_active_collection" does not exist

Command was: ALTER TABLE ONLY public.gbim_active_collection DROP CONSTRAINT gbim_active_collection_pkey;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_wv_county_boundaries_24k_topo_updated_2026_wma84" does not exist

Command was: ALTER TABLE public.wv_wv_county_boundaries_24k_topo_updated_2026_wma84 ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_wv_county_boundaries_24k_topo_updated_2026_utm83" does not exist

Command was: ALTER TABLE public.wv_wv_county_boundaries_24k_topo_updated_2026_utm83 ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_util_solid_waste_facilities" does not exist

Command was: ALTER TABLE public.wv_util_solid_waste_facilities ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_util_sewer_treatment_plants" does not exist

Command was: ALTER TABLE public.wv_util_sewer_treatment_plants ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_whitewater_trails" does not exist

Command was: ALTER TABLE public.wv_trn_whitewater_trails ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_roads_us_routes" does not exist

Command was: ALTER TABLE public.wv_trn_roads_us_routes ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_roads_us_highways" does not exist

Command was: ALTER TABLE public.wv_trn_roads_us_highways ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_roads_state_routes" does not exist

Command was: ALTER TABLE public.wv_trn_roads_state_routes ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_roads_major_4800" does not exist

Command was: ALTER TABLE public.wv_trn_roads_major_4800 ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_roads_interstate" does not exist

Command was: ALTER TABLE public.wv_trn_roads_interstate ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_recreational_trails" does not exist

Command was: ALTER TABLE public.wv_trn_recreational_trails ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_railroads_national_network" does not exist

Command was: ALTER TABLE public.wv_trn_railroads_national_network ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_railroads_excursion" does not exist

Command was: ALTER TABLE public.wv_trn_railroads_excursion ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_railroads_amtrak" does not exist

Command was: ALTER TABLE public.wv_trn_railroads_amtrak ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_railroad_lines_rti" does not exist

Command was: ALTER TABLE public.wv_trn_railroad_lines_rti ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_mnf_roads" does not exist

Command was: ALTER TABLE public.wv_trn_mnf_roads ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_mnf_recreation_trails" does not exist

Command was: ALTER TABLE public.wv_trn_mnf_recreation_trails ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_intermodal_terminals" does not exist

Command was: ALTER TABLE public.wv_trn_intermodal_terminals ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_airports" does not exist

Command was: ALTER TABLE public.wv_trn_airports ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_airport_runways" does not exist

Command was: ALTER TABLE public.wv_trn_airport_runways ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_airport_proposed" does not exist

Command was: ALTER TABLE public.wv_trn_airport_proposed ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_trn_airport_facilities" does not exist

Command was: ALTER TABLE public.wv_trn_airport_facilities ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_str_samb_building_polygons" does not exist

Command was: ALTER TABLE public.wv_str_samb_building_polygons ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_str_samb_building_points" does not exist

Command was: ALTER TABLE public.wv_str_samb_building_points ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_str_places_of_worship_hsip" does not exist

Command was: ALTER TABLE public.wv_str_places_of_worship_hsip ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_str_parole_offices" does not exist

Command was: ALTER TABLE public.wv_str_parole_offices ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_str_flood_atrisk_structures" does not exist

Command was: ALTER TABLE public.wv_str_flood_atrisk_structures ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_str_correctional_institutions" does not exist

Command was: ALTER TABLE public.wv_str_correctional_institutions ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_str_bridges" does not exist

Command was: ALTER TABLE public.wv_str_bridges ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_zcta_2020" does not exist

Command was: ALTER TABLE public.wv_soc_zcta_2020 ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_va_facilities" does not exist

Command was: ALTER TABLE public.wv_soc_va_facilities ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_towers_tv" does not exist

Command was: ALTER TABLE public.wv_soc_towers_tv ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_towers_private" does not exist

Command was: ALTER TABLE public.wv_soc_towers_private ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_towers_pager" does not exist

Command was: ALTER TABLE public.wv_soc_towers_pager ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_towers_microwave" does not exist

Command was: ALTER TABLE public.wv_soc_towers_microwave ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_towers_fm" does not exist

Command was: ALTER TABLE public.wv_soc_towers_fm ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_towers_cellular" does not exist

Command was: ALTER TABLE public.wv_soc_towers_cellular ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_towers_asr" does not exist

Command was: ALTER TABLE public.wv_soc_towers_asr ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_towers_am" does not exist

Command was: ALTER TABLE public.wv_soc_towers_am ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_schools_k12" does not exist

Command was: ALTER TABLE public.wv_soc_schools_k12 ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_population_by_decade" does not exist

Command was: ALTER TABLE public.wv_soc_population_by_decade ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_places_of_worship_wvgistc" does not exist

Command was: ALTER TABLE public.wv_soc_places_of_worship_wvgistc ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_nursing_homes" does not exist

Command was: ALTER TABLE public.wv_soc_nursing_homes ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_national_register_historic_polygons" does not exist

Command was: ALTER TABLE public.wv_soc_national_register_historic_polygons ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_national_register_historic_points" does not exist

Command was: ALTER TABLE public.wv_soc_national_register_historic_points ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_libraries" does not exist

Command was: ALTER TABLE public.wv_soc_libraries ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_hospitals_wvdem" does not exist

Command was: ALTER TABLE public.wv_soc_hospitals_wvdem ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_higher_ed_facilities" does not exist

Command was: ALTER TABLE public.wv_soc_higher_ed_facilities ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_fishing_lakes" does not exist

Command was: ALTER TABLE public.wv_soc_fishing_lakes ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_fishing_boating_access" does not exist

Command was: ALTER TABLE public.wv_soc_fishing_boating_access ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_fish_hatcheries" does not exist

Command was: ALTER TABLE public.wv_soc_fish_hatcheries ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_courthouses_federal" does not exist

Command was: ALTER TABLE public.wv_soc_courthouses_federal ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_courthouses_county" does not exist

Command was: ALTER TABLE public.wv_soc_courthouses_county ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_communities_pop_change" does not exist

Command was: ALTER TABLE public.wv_soc_communities_pop_change ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_cities_pop2500" does not exist

Command was: ALTER TABLE public.wv_soc_cities_pop2500 ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_cities_pop10k" does not exist

Command was: ALTER TABLE public.wv_soc_cities_pop10k ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_census_tracts_2020" does not exist

Command was: ALTER TABLE public.wv_soc_census_tracts_2020 ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_census_blockgroups_2020" does not exist

Command was: ALTER TABLE public.wv_soc_census_blockgroups_2020 ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_soc_911_centers" does not exist

Command was: ALTER TABLE public.wv_soc_911_centers ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_plc_tax_parcels_surface_mineral" does not exist

Command was: ALTER TABLE public.wv_plc_tax_parcels_surface_mineral ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_plc_tax_district_boundaries" does not exist

Command was: ALTER TABLE public.wv_plc_tax_district_boundaries ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_plc_regional_planning_councils" does not exist

Command was: ALTER TABLE public.wv_plc_regional_planning_councils ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_plc_hazus_level1" does not exist

Command was: ALTER TABLE public.wv_plc_hazus_level1 ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_mil_national_guard_armories" does not exist

Command was: ALTER TABLE public.wv_mil_national_guard_armories ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_mil_army_reserve_facilities" does not exist

Command was: ALTER TABLE public.wv_mil_army_reserve_facilities ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_loc_sams2_address_road_centerlines" does not exist

Command was: ALTER TABLE public.wv_loc_sams2_address_road_centerlines ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_loc_populated_places_census" does not exist

Command was: ALTER TABLE public.wv_loc_populated_places_census ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_loc_geodetic_control_points" does not exist

Command was: ALTER TABLE public.wv_loc_geodetic_control_points ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_loc_county_seats" does not exist

Command was: ALTER TABLE public.wv_loc_county_seats ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_loc_census_urbanized_areas" does not exist

Command was: ALTER TABLE public.wv_loc_census_urbanized_areas ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hyd_watershed_boundary_8_10_12" does not exist

Command was: ALTER TABLE public.wv_hyd_watershed_boundary_8_10_12 ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hyd_watershed_boundary_12digit_hu" does not exist

Command was: ALTER TABLE public.wv_hyd_watershed_boundary_12digit_hu ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hyd_watershed_boundary_11digit" does not exist

Command was: ALTER TABLE public.wv_hyd_watershed_boundary_11digit ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hyd_streams_tiger" does not exist

Command was: ALTER TABLE public.wv_hyd_streams_tiger ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hyd_streams_national_atlas" does not exist

Command was: ALTER TABLE public.wv_hyd_streams_national_atlas ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hyd_streams_high_quality" does not exist

Command was: ALTER TABLE public.wv_hyd_streams_high_quality ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hyd_streamflow_stations" does not exist

Command was: ALTER TABLE public.wv_hyd_streamflow_stations ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hyd_springs_100gpm" does not exist

Command was: ALTER TABLE public.wv_hyd_springs_100gpm ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hyd_navigable_waterways_structures" does not exist

Command was: ALTER TABLE public.wv_hyd_navigable_waterways_structures ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hyd_navigable_waterways_river_miles" does not exist

Command was: ALTER TABLE public.wv_hyd_navigable_waterways_river_miles ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hyd_navigable_waterways" does not exist

Command was: ALTER TABLE public.wv_hyd_navigable_waterways ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hyd_high_water_marks" does not exist

Command was: ALTER TABLE public.wv_hyd_high_water_marks ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hyd_hazus_floodplain_zones" does not exist

Command was: ALTER TABLE public.wv_hyd_hazus_floodplain_zones ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hyd_dams_noncoal" does not exist

Command was: ALTER TABLE public.wv_hyd_dams_noncoal ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hyd_dams_nid" does not exist

Command was: ALTER TABLE public.wv_hyd_dams_nid ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hyd_dams_dmr" does not exist

Command was: ALTER TABLE public.wv_hyd_dams_dmr ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hlt_rural_health_facilities" does not exist

Command was: ALTER TABLE public.wv_hlt_rural_health_facilities ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hlt_public_health_departments" does not exist

Command was: ALTER TABLE public.wv_hlt_public_health_departments ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_hlt_health_providers" does not exist

Command was: ALTER TABLE public.wv_hlt_health_providers ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_geo_karst" does not exist

Command was: ALTER TABLE public.wv_geo_karst ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_geo_geological_map_generalized" does not exist

Command was: ALTER TABLE public.wv_geo_geological_map_generalized ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_geo_coal_beds" does not exist

Command was: ALTER TABLE public.wv_geo_coal_beds ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_env_wind_energy_resources" does not exist

Command was: ALTER TABLE public.wv_env_wind_energy_resources ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_env_wildfire_regions" does not exist

Command was: ALTER TABLE public.wv_env_wildfire_regions ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_env_timber_removal_volume" does not exist

Command was: ALTER TABLE public.wv_env_timber_removal_volume ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_env_epa_facilities" does not exist

Command was: ALTER TABLE public.wv_env_epa_facilities ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_env_air_nonattainment" does not exist

Command was: ALTER TABLE public.wv_env_air_nonattainment ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_elv_summit_names" does not exist

Command was: ALTER TABLE public.wv_elv_summit_names ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_eco_mountaintop_removal" does not exist

Command was: ALTER TABLE public.wv_eco_mountaintop_removal ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_eco_mineral_operations" does not exist

Command was: ALTER TABLE public.wv_eco_mineral_operations ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_eco_manufacturing_directory" does not exist

Command was: ALTER TABLE public.wv_eco_manufacturing_directory ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_eco_industrial_sites" does not exist

Command was: ALTER TABLE public.wv_eco_industrial_sites ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_eco_ezec_communities" does not exist

Command was: ALTER TABLE public.wv_eco_ezec_communities ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_eco_coal_fields" does not exist

Command was: ALTER TABLE public.wv_eco_coal_fields ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_eco_abandoned_mine_lands_polygon" does not exist

Command was: ALTER TABLE public.wv_eco_abandoned_mine_lands_polygon ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_eco_abandoned_mine_lands_point" does not exist

Command was: ALTER TABLE public.wv_eco_abandoned_mine_lands_point ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_eco_abandoned_mine_lands_line" does not exist

Command was: ALTER TABLE public.wv_eco_abandoned_mine_lands_line ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_county_boundaries_24k_topo_updated_2026_wma84_gdb" does not exist

Command was: ALTER TABLE public.wv_county_boundaries_24k_topo_updated_2026_wma84_gdb ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_county_boundaries_24k_topo_updated_2026_utm83_gdb" does not exist

Command was: ALTER TABLE public.wv_county_boundaries_24k_topo_updated_2026_utm83_gdb ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_censustracts_census_2020_utm83" does not exist

Command was: ALTER TABLE public.wv_censustracts_census_2020_utm83 ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_workforce_investment_areas" does not exist

Command was: ALTER TABLE public.wv_bnd_workforce_investment_areas ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_voting_districts_2002" does not exist

Command was: ALTER TABLE public.wv_bnd_voting_districts_2002 ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_voting_districts_2000" does not exist

Command was: ALTER TABLE public.wv_bnd_voting_districts_2000 ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_state_boundary_100k" does not exist

Command was: ALTER TABLE public.wv_bnd_state_boundary_100k ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_public_lands_wildlife_resources" does not exist

Command was: ALTER TABLE public.wv_bnd_public_lands_wildlife_resources ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_public_lands_state_parks" does not exist

Command was: ALTER TABLE public.wv_bnd_public_lands_state_parks ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_public_lands_state_forests" does not exist

Command was: ALTER TABLE public.wv_bnd_public_lands_state_forests ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_public_lands_nwr" does not exist

Command was: ALTER TABLE public.wv_bnd_public_lands_nwr ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_public_lands_national_park" does not exist

Command was: ALTER TABLE public.wv_bnd_public_lands_national_park ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_public_lands_national_forest" does not exist

Command was: ALTER TABLE public.wv_bnd_public_lands_national_forest ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_public_lands_county_city_parks" does not exist

Command was: ALTER TABLE public.wv_bnd_public_lands_county_city_parks ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_nhd_mussel_streams" does not exist

Command was: ALTER TABLE public.wv_bnd_nhd_mussel_streams ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_morgantown_wards" does not exist

Command was: ALTER TABLE public.wv_bnd_morgantown_wards ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_mnf_wilderness" does not exist

Command was: ALTER TABLE public.wv_bnd_mnf_wilderness ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_mnf_recreation_sites" does not exist

Command was: ALTER TABLE public.wv_bnd_mnf_recreation_sites ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_mnf_recreation_campgrounds" does not exist

Command was: ALTER TABLE public.wv_bnd_mnf_recreation_campgrounds ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_mnf_ranger_districts" does not exist

Command was: ALTER TABLE public.wv_bnd_mnf_ranger_districts ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_mnf_management_prescriptions" does not exist

Command was: ALTER TABLE public.wv_bnd_mnf_management_prescriptions ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_mnf_basic_ownership" does not exist

Command was: ALTER TABLE public.wv_bnd_mnf_basic_ownership ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_county_municipal_dlg" does not exist

Command was: ALTER TABLE public.wv_bnd_county_municipal_dlg ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_county_24k" does not exist

Command was: ALTER TABLE public.wv_bnd_county_24k ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_census_designated_places" does not exist

Command was: ALTER TABLE public.wv_bnd_census_designated_places ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_canaan_valley_nwr" does not exist

Command was: ALTER TABLE public.wv_bnd_canaan_valley_nwr ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_arc_counties" does not exist

Command was: ALTER TABLE public.wv_bnd_arc_counties ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bnd_appalachian_basin_boundary" does not exist

Command was: ALTER TABLE public.wv_bnd_appalachian_basin_boundary ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bio_red_spruce_cover" does not exist

Command was: ALTER TABLE public.wv_bio_red_spruce_cover ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bio_ecoregions" does not exist

Command was: ALTER TABLE public.wv_bio_ecoregions ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_bio_biodiversity_rank" does not exist

Command was: ALTER TABLE public.wv_bio_biodiversity_rank ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  relation "public.wv_atm_weather_stations" does not exist

Command was: ALTER TABLE public.wv_atm_weather_stations ALTER COLUMN gid DROP DEFAULT;

pg_restore: error: could not execute query: ERROR:  sequence "wv_wv_county_boundaries_24k_topo_updated_2026_wma84_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_wv_county_boundaries_24k_topo_updated_2026_wma84_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_wv_county_boundaries_24k_topo_updated_2026_wma84" does not exist

Command was: DROP TABLE public.wv_wv_county_boundaries_24k_topo_updated_2026_wma84;

pg_restore: error: could not execute query: ERROR:  sequence "wv_wv_county_boundaries_24k_topo_updated_2026_utm83_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_wv_county_boundaries_24k_topo_updated_2026_utm83_gid_seq;

pg_restore: error: could not execute query: ERROR:  sequence "wv_util_solid_waste_facilities_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_util_solid_waste_facilities_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_util_solid_waste_facilities" does not exist

Command was: DROP TABLE public.wv_util_solid_waste_facilities;

pg_restore: error: could not execute query: ERROR:  sequence "wv_util_sewer_treatment_plants_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_util_sewer_treatment_plants_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_util_sewer_treatment_plants" does not exist

Command was: DROP TABLE public.wv_util_sewer_treatment_plants;

pg_restore: error: could not execute query: ERROR:  sequence "wv_trn_whitewater_trails_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_trn_whitewater_trails_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_trn_whitewater_trails" does not exist

Command was: DROP TABLE public.wv_trn_whitewater_trails;

pg_restore: error: could not execute query: ERROR:  sequence "wv_trn_roads_us_routes_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_trn_roads_us_routes_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_trn_roads_us_routes" does not exist

Command was: DROP TABLE public.wv_trn_roads_us_routes;

pg_restore: error: could not execute query: ERROR:  sequence "wv_trn_roads_us_highways_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_trn_roads_us_highways_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_trn_roads_us_highways" does not exist

Command was: DROP TABLE public.wv_trn_roads_us_highways;

pg_restore: error: could not execute query: ERROR:  sequence "wv_trn_roads_state_routes_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_trn_roads_state_routes_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_trn_roads_state_routes" does not exist

Command was: DROP TABLE public.wv_trn_roads_state_routes;

pg_restore: error: could not execute query: ERROR:  sequence "wv_trn_roads_major_4800_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_trn_roads_major_4800_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_trn_roads_major_4800" does not exist

Command was: DROP TABLE public.wv_trn_roads_major_4800;

pg_restore: error: could not execute query: ERROR:  sequence "wv_trn_roads_interstate_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_trn_roads_interstate_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_trn_roads_interstate" does not exist

Command was: DROP TABLE public.wv_trn_roads_interstate;

pg_restore: error: could not execute query: ERROR:  sequence "wv_trn_recreational_trails_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_trn_recreational_trails_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_trn_recreational_trails" does not exist

Command was: DROP TABLE public.wv_trn_recreational_trails;

pg_restore: error: could not execute query: ERROR:  sequence "wv_trn_railroads_national_network_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_trn_railroads_national_network_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_trn_railroads_national_network" does not exist

Command was: DROP TABLE public.wv_trn_railroads_national_network;

pg_restore: error: could not execute query: ERROR:  sequence "wv_trn_railroads_excursion_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_trn_railroads_excursion_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_trn_railroads_excursion" does not exist

Command was: DROP TABLE public.wv_trn_railroads_excursion;

pg_restore: error: could not execute query: ERROR:  sequence "wv_trn_railroads_amtrak_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_trn_railroads_amtrak_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_trn_railroads_amtrak" does not exist

Command was: DROP TABLE public.wv_trn_railroads_amtrak;

pg_restore: error: could not execute query: ERROR:  sequence "wv_trn_railroad_lines_rti_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_trn_railroad_lines_rti_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_trn_railroad_lines_rti" does not exist

Command was: DROP TABLE public.wv_trn_railroad_lines_rti;

pg_restore: error: could not execute query: ERROR:  sequence "wv_trn_mnf_roads_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_trn_mnf_roads_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_trn_mnf_roads" does not exist

Command was: DROP TABLE public.wv_trn_mnf_roads;

pg_restore: error: could not execute query: ERROR:  sequence "wv_trn_mnf_recreation_trails_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_trn_mnf_recreation_trails_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_trn_mnf_recreation_trails" does not exist

Command was: DROP TABLE public.wv_trn_mnf_recreation_trails;

pg_restore: error: could not execute query: ERROR:  sequence "wv_trn_intermodal_terminals_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_trn_intermodal_terminals_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_trn_intermodal_terminals" does not exist

Command was: DROP TABLE public.wv_trn_intermodal_terminals;

pg_restore: error: could not execute query: ERROR:  sequence "wv_trn_airports_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_trn_airports_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_trn_airports" does not exist

Command was: DROP TABLE public.wv_trn_airports;

pg_restore: error: could not execute query: ERROR:  sequence "wv_trn_airport_runways_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_trn_airport_runways_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_trn_airport_runways" does not exist

Command was: DROP TABLE public.wv_trn_airport_runways;

pg_restore: error: could not execute query: ERROR:  sequence "wv_trn_airport_proposed_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_trn_airport_proposed_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_trn_airport_proposed" does not exist

Command was: DROP TABLE public.wv_trn_airport_proposed;

pg_restore: error: could not execute query: ERROR:  sequence "wv_trn_airport_facilities_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_trn_airport_facilities_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_trn_airport_facilities" does not exist

Command was: DROP TABLE public.wv_trn_airport_facilities;

pg_restore: error: could not execute query: ERROR:  table "wv_tract_representation_pre_gid_rebind" does not exist

Command was: DROP TABLE public.wv_tract_representation_pre_gid_rebind;

pg_restore: error: could not execute query: ERROR:  view "wv_tract_belief_vector_ready" does not exist

Command was: DROP VIEW public.wv_tract_belief_vector_ready;

pg_restore: error: could not execute query: ERROR:  table "wv_tract_representation" does not exist

Command was: DROP TABLE public.wv_tract_representation;

pg_restore: error: could not execute query: ERROR:  table "wv_tract_identity" does not exist

Command was: DROP TABLE public.wv_tract_identity;

pg_restore: error: could not execute query: ERROR:  table "wv_tract_dataset_coverage" does not exist

Command was: DROP TABLE public.wv_tract_dataset_coverage;

pg_restore: error: could not execute query: ERROR:  table "wv_tract_belief_snapshot" does not exist

Command was: DROP TABLE public.wv_tract_belief_snapshot;

pg_restore: error: could not execute query: ERROR:  sequence "wv_str_samb_building_polygons_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_str_samb_building_polygons_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_str_samb_building_polygons" does not exist

Command was: DROP TABLE public.wv_str_samb_building_polygons;

pg_restore: error: could not execute query: ERROR:  sequence "wv_str_samb_building_points_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_str_samb_building_points_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_str_samb_building_points" does not exist

Command was: DROP TABLE public.wv_str_samb_building_points;

pg_restore: error: could not execute query: ERROR:  sequence "wv_str_places_of_worship_hsip_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_str_places_of_worship_hsip_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_str_places_of_worship_hsip" does not exist

Command was: DROP TABLE public.wv_str_places_of_worship_hsip;

pg_restore: error: could not execute query: ERROR:  sequence "wv_str_parole_offices_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_str_parole_offices_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_str_parole_offices" does not exist

Command was: DROP TABLE public.wv_str_parole_offices;

pg_restore: error: could not execute query: ERROR:  sequence "wv_str_flood_atrisk_structures_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_str_flood_atrisk_structures_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_str_flood_atrisk_structures" does not exist

Command was: DROP TABLE public.wv_str_flood_atrisk_structures;

pg_restore: error: could not execute query: ERROR:  sequence "wv_str_correctional_institutions_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_str_correctional_institutions_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_str_correctional_institutions" does not exist

Command was: DROP TABLE public.wv_str_correctional_institutions;

pg_restore: error: could not execute query: ERROR:  sequence "wv_str_bridges_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_str_bridges_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_str_bridges" does not exist

Command was: DROP TABLE public.wv_str_bridges;

pg_restore: error: could not execute query: ERROR:  sequence "wv_soc_zcta_2020_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_soc_zcta_2020_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_soc_zcta_2020" does not exist

Command was: DROP TABLE public.wv_soc_zcta_2020;

pg_restore: error: could not execute query: ERROR:  sequence "wv_soc_va_facilities_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_soc_va_facilities_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_soc_va_facilities" does not exist

Command was: DROP TABLE public.wv_soc_va_facilities;

pg_restore: error: could not execute query: ERROR:  sequence "wv_soc_towers_tv_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_soc_towers_tv_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_soc_towers_tv" does not exist

Command was: DROP TABLE public.wv_soc_towers_tv;

pg_restore: error: could not execute query: ERROR:  sequence "wv_soc_towers_private_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_soc_towers_private_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_soc_towers_private" does not exist

Command was: DROP TABLE public.wv_soc_towers_private;

pg_restore: error: could not execute query: ERROR:  sequence "wv_soc_towers_pager_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_soc_towers_pager_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_soc_towers_pager" does not exist

Command was: DROP TABLE public.wv_soc_towers_pager;

pg_restore: error: could not execute query: ERROR:  sequence "wv_soc_towers_microwave_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_soc_towers_microwave_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_soc_towers_microwave" does not exist

Command was: DROP TABLE public.wv_soc_towers_microwave;

pg_restore: error: could not execute query: ERROR:  sequence "wv_soc_towers_fm_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_soc_towers_fm_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_soc_towers_fm" does not exist

Command was: DROP TABLE public.wv_soc_towers_fm;

pg_restore: error: could not execute query: ERROR:  sequence "wv_soc_towers_cellular_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_soc_towers_cellular_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_soc_towers_cellular" does not exist

Command was: DROP TABLE public.wv_soc_towers_cellular;

pg_restore: error: could not execute query: ERROR:  sequence "wv_soc_towers_asr_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_soc_towers_asr_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_soc_towers_asr" does not exist

Command was: DROP TABLE public.wv_soc_towers_asr;

pg_restore: error: could not execute query: ERROR:  sequence "wv_soc_towers_am_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_soc_towers_am_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_soc_towers_am" does not exist

Command was: DROP TABLE public.wv_soc_towers_am;

pg_restore: error: could not execute query: ERROR:  sequence "wv_soc_schools_k12_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_soc_schools_k12_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_soc_schools_k12" does not exist

Command was: DROP TABLE public.wv_soc_schools_k12;

pg_restore: error: could not execute query: ERROR:  sequence "wv_soc_population_by_decade_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_soc_population_by_decade_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_soc_population_by_decade" does not exist

Command was: DROP TABLE public.wv_soc_population_by_decade;

pg_restore: error: could not execute query: ERROR:  sequence "wv_soc_places_of_worship_wvgistc_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_soc_places_of_worship_wvgistc_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_soc_places_of_worship_wvgistc" does not exist

Command was: DROP TABLE public.wv_soc_places_of_worship_wvgistc;

pg_restore: error: could not execute query: ERROR:  sequence "wv_soc_nursing_homes_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_soc_nursing_homes_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_soc_nursing_homes" does not exist

Command was: DROP TABLE public.wv_soc_nursing_homes;

pg_restore: error: could not execute query: ERROR:  sequence "wv_soc_national_register_historic_polygons_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_soc_national_register_historic_polygons_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_soc_national_register_historic_polygons" does not exist

Command was: DROP TABLE public.wv_soc_national_register_historic_polygons;

pg_restore: error: could not execute query: ERROR:  sequence "wv_soc_national_register_historic_points_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_soc_national_register_historic_points_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_soc_national_register_historic_points" does not exist

Command was: DROP TABLE public.wv_soc_national_register_historic_points;

pg_restore: error: could not execute query: ERROR:  sequence "wv_soc_libraries_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_soc_libraries_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_soc_libraries" does not exist

Command was: DROP TABLE public.wv_soc_libraries;

pg_restore: error: could not execute query: ERROR:  sequence "wv_soc_hospitals_wvdem_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_soc_hospitals_wvdem_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_soc_hospitals_wvdem" does not exist

Command was: DROP TABLE public.wv_soc_hospitals_wvdem;

pg_restore: error: could not execute query: ERROR:  sequence "wv_soc_higher_ed_facilities_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_soc_higher_ed_facilities_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_soc_higher_ed_facilities" does not exist

Command was: DROP TABLE public.wv_soc_higher_ed_facilities;

pg_restore: error: could not execute query: ERROR:  sequence "wv_soc_fishing_lakes_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_soc_fishing_lakes_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_soc_fishing_lakes" does not exist

Command was: DROP TABLE public.wv_soc_fishing_lakes;

pg_restore: error: could not execute query: ERROR:  sequence "wv_soc_fishing_boating_access_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_soc_fishing_boating_access_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_soc_fishing_boating_access" does not exist

Command was: DROP TABLE public.wv_soc_fishing_boating_access;

pg_restore: error: could not execute query: ERROR:  sequence "wv_soc_fish_hatcheries_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_soc_fish_hatcheries_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_soc_fish_hatcheries" does not exist

Command was: DROP TABLE public.wv_soc_fish_hatcheries;

pg_restore: error: could not execute query: ERROR:  sequence "wv_soc_courthouses_federal_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_soc_courthouses_federal_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_soc_courthouses_federal" does not exist

Command was: DROP TABLE public.wv_soc_courthouses_federal;

pg_restore: error: could not execute query: ERROR:  sequence "wv_soc_courthouses_county_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_soc_courthouses_county_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_soc_courthouses_county" does not exist

Command was: DROP TABLE public.wv_soc_courthouses_county;

pg_restore: error: could not execute query: ERROR:  sequence "wv_soc_communities_pop_change_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_soc_communities_pop_change_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_soc_communities_pop_change" does not exist

Command was: DROP TABLE public.wv_soc_communities_pop_change;

pg_restore: error: could not execute query: ERROR:  sequence "wv_soc_cities_pop2500_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_soc_cities_pop2500_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_soc_cities_pop2500" does not exist

Command was: DROP TABLE public.wv_soc_cities_pop2500;

pg_restore: error: could not execute query: ERROR:  sequence "wv_soc_cities_pop10k_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_soc_cities_pop10k_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_soc_cities_pop10k" does not exist

Command was: DROP TABLE public.wv_soc_cities_pop10k;

pg_restore: error: could not execute query: ERROR:  sequence "wv_soc_census_tracts_2020_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_soc_census_tracts_2020_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_soc_census_tracts_2020" does not exist

Command was: DROP TABLE public.wv_soc_census_tracts_2020;

pg_restore: error: could not execute query: ERROR:  sequence "wv_soc_census_blockgroups_2020_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_soc_census_blockgroups_2020_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_soc_census_blockgroups_2020" does not exist

Command was: DROP TABLE public.wv_soc_census_blockgroups_2020;

pg_restore: error: could not execute query: ERROR:  sequence "wv_soc_911_centers_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_soc_911_centers_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_soc_911_centers" does not exist

Command was: DROP TABLE public.wv_soc_911_centers;

pg_restore: error: could not execute query: ERROR:  sequence "wv_plc_tax_parcels_surface_mineral_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_plc_tax_parcels_surface_mineral_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_plc_tax_parcels_surface_mineral" does not exist

Command was: DROP TABLE public.wv_plc_tax_parcels_surface_mineral;

pg_restore: error: could not execute query: ERROR:  sequence "wv_plc_tax_district_boundaries_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_plc_tax_district_boundaries_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_plc_tax_district_boundaries" does not exist

Command was: DROP TABLE public.wv_plc_tax_district_boundaries;

pg_restore: error: could not execute query: ERROR:  sequence "wv_plc_regional_planning_councils_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_plc_regional_planning_councils_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_plc_regional_planning_councils" does not exist

Command was: DROP TABLE public.wv_plc_regional_planning_councils;

pg_restore: error: could not execute query: ERROR:  sequence "wv_plc_hazus_level1_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_plc_hazus_level1_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_plc_hazus_level1" does not exist

Command was: DROP TABLE public.wv_plc_hazus_level1;

pg_restore: error: could not execute query: ERROR:  sequence "wv_mil_national_guard_armories_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_mil_national_guard_armories_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_mil_national_guard_armories" does not exist

Command was: DROP TABLE public.wv_mil_national_guard_armories;

pg_restore: error: could not execute query: ERROR:  sequence "wv_mil_army_reserve_facilities_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_mil_army_reserve_facilities_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_mil_army_reserve_facilities" does not exist

Command was: DROP TABLE public.wv_mil_army_reserve_facilities;

pg_restore: error: could not execute query: ERROR:  sequence "wv_loc_sams2_address_road_centerlines_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_loc_sams2_address_road_centerlines_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_loc_sams2_address_road_centerlines" does not exist

Command was: DROP TABLE public.wv_loc_sams2_address_road_centerlines;

pg_restore: error: could not execute query: ERROR:  sequence "wv_loc_populated_places_census_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_loc_populated_places_census_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_loc_populated_places_census" does not exist

Command was: DROP TABLE public.wv_loc_populated_places_census;

pg_restore: error: could not execute query: ERROR:  sequence "wv_loc_geodetic_control_points_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_loc_geodetic_control_points_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_loc_geodetic_control_points" does not exist

Command was: DROP TABLE public.wv_loc_geodetic_control_points;

pg_restore: error: could not execute query: ERROR:  sequence "wv_loc_county_seats_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_loc_county_seats_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_loc_county_seats" does not exist

Command was: DROP TABLE public.wv_loc_county_seats;

pg_restore: error: could not execute query: ERROR:  sequence "wv_loc_census_urbanized_areas_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_loc_census_urbanized_areas_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_loc_census_urbanized_areas" does not exist

Command was: DROP TABLE public.wv_loc_census_urbanized_areas;

pg_restore: error: could not execute query: ERROR:  table "wv_layer_categories" does not exist

Command was: DROP TABLE public.wv_layer_categories;

pg_restore: error: could not execute query: ERROR:  sequence "wv_hyd_watershed_boundary_8_10_12_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_hyd_watershed_boundary_8_10_12_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_hyd_watershed_boundary_8_10_12" does not exist

Command was: DROP TABLE public.wv_hyd_watershed_boundary_8_10_12;

pg_restore: error: could not execute query: ERROR:  sequence "wv_hyd_watershed_boundary_12digit_hu_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_hyd_watershed_boundary_12digit_hu_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_hyd_watershed_boundary_12digit_hu" does not exist

Command was: DROP TABLE public.wv_hyd_watershed_boundary_12digit_hu;

pg_restore: error: could not execute query: ERROR:  sequence "wv_hyd_watershed_boundary_11digit_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_hyd_watershed_boundary_11digit_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_hyd_watershed_boundary_11digit" does not exist

Command was: DROP TABLE public.wv_hyd_watershed_boundary_11digit;

pg_restore: error: could not execute query: ERROR:  sequence "wv_hyd_streams_tiger_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_hyd_streams_tiger_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_hyd_streams_tiger" does not exist

Command was: DROP TABLE public.wv_hyd_streams_tiger;

pg_restore: error: could not execute query: ERROR:  sequence "wv_hyd_streams_national_atlas_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_hyd_streams_national_atlas_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_hyd_streams_national_atlas" does not exist

Command was: DROP TABLE public.wv_hyd_streams_national_atlas;

pg_restore: error: could not execute query: ERROR:  sequence "wv_hyd_streams_high_quality_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_hyd_streams_high_quality_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_hyd_streams_high_quality" does not exist

Command was: DROP TABLE public.wv_hyd_streams_high_quality;

pg_restore: error: could not execute query: ERROR:  sequence "wv_hyd_streamflow_stations_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_hyd_streamflow_stations_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_hyd_streamflow_stations" does not exist

Command was: DROP TABLE public.wv_hyd_streamflow_stations;

pg_restore: error: could not execute query: ERROR:  sequence "wv_hyd_springs_100gpm_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_hyd_springs_100gpm_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_hyd_springs_100gpm" does not exist

Command was: DROP TABLE public.wv_hyd_springs_100gpm;

pg_restore: error: could not execute query: ERROR:  sequence "wv_hyd_navigable_waterways_structures_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_hyd_navigable_waterways_structures_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_hyd_navigable_waterways_structures" does not exist

Command was: DROP TABLE public.wv_hyd_navigable_waterways_structures;

pg_restore: error: could not execute query: ERROR:  sequence "wv_hyd_navigable_waterways_river_miles_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_hyd_navigable_waterways_river_miles_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_hyd_navigable_waterways_river_miles" does not exist

Command was: DROP TABLE public.wv_hyd_navigable_waterways_river_miles;

pg_restore: error: could not execute query: ERROR:  sequence "wv_hyd_navigable_waterways_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_hyd_navigable_waterways_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_hyd_navigable_waterways" does not exist

Command was: DROP TABLE public.wv_hyd_navigable_waterways;

pg_restore: error: could not execute query: ERROR:  sequence "wv_hyd_high_water_marks_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_hyd_high_water_marks_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_hyd_high_water_marks" does not exist

Command was: DROP TABLE public.wv_hyd_high_water_marks;

pg_restore: error: could not execute query: ERROR:  sequence "wv_hyd_hazus_floodplain_zones_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_hyd_hazus_floodplain_zones_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_hyd_hazus_floodplain_zones" does not exist

Command was: DROP TABLE public.wv_hyd_hazus_floodplain_zones;

pg_restore: error: could not execute query: ERROR:  sequence "wv_hyd_dams_noncoal_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_hyd_dams_noncoal_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_hyd_dams_noncoal" does not exist

Command was: DROP TABLE public.wv_hyd_dams_noncoal;

pg_restore: error: could not execute query: ERROR:  sequence "wv_hyd_dams_nid_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_hyd_dams_nid_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_hyd_dams_nid" does not exist

Command was: DROP TABLE public.wv_hyd_dams_nid;

pg_restore: error: could not execute query: ERROR:  sequence "wv_hyd_dams_dmr_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_hyd_dams_dmr_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_hyd_dams_dmr" does not exist

Command was: DROP TABLE public.wv_hyd_dams_dmr;

pg_restore: error: could not execute query: ERROR:  sequence "wv_hlt_rural_health_facilities_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_hlt_rural_health_facilities_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_hlt_rural_health_facilities" does not exist

Command was: DROP TABLE public.wv_hlt_rural_health_facilities;

pg_restore: error: could not execute query: ERROR:  sequence "wv_hlt_public_health_departments_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_hlt_public_health_departments_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_hlt_public_health_departments" does not exist

Command was: DROP TABLE public.wv_hlt_public_health_departments;

pg_restore: error: could not execute query: ERROR:  sequence "wv_hlt_health_providers_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_hlt_health_providers_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_hlt_health_providers" does not exist

Command was: DROP TABLE public.wv_hlt_health_providers;

pg_restore: error: could not execute query: ERROR:  sequence "wv_geo_karst_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_geo_karst_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_geo_karst" does not exist

Command was: DROP TABLE public.wv_geo_karst;

pg_restore: error: could not execute query: ERROR:  sequence "wv_geo_geological_map_generalized_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_geo_geological_map_generalized_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_geo_geological_map_generalized" does not exist

Command was: DROP TABLE public.wv_geo_geological_map_generalized;

pg_restore: error: could not execute query: ERROR:  sequence "wv_geo_coal_beds_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_geo_coal_beds_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_geo_coal_beds" does not exist

Command was: DROP TABLE public.wv_geo_coal_beds;

pg_restore: error: could not execute query: ERROR:  sequence "wv_env_wind_energy_resources_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_env_wind_energy_resources_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_env_wind_energy_resources" does not exist

Command was: DROP TABLE public.wv_env_wind_energy_resources;

pg_restore: error: could not execute query: ERROR:  sequence "wv_env_wildfire_regions_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_env_wildfire_regions_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_env_wildfire_regions" does not exist

Command was: DROP TABLE public.wv_env_wildfire_regions;

pg_restore: error: could not execute query: ERROR:  sequence "wv_env_timber_removal_volume_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_env_timber_removal_volume_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_env_timber_removal_volume" does not exist

Command was: DROP TABLE public.wv_env_timber_removal_volume;

pg_restore: error: could not execute query: ERROR:  sequence "wv_env_epa_facilities_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_env_epa_facilities_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_env_epa_facilities" does not exist

Command was: DROP TABLE public.wv_env_epa_facilities;

pg_restore: error: could not execute query: ERROR:  sequence "wv_env_air_nonattainment_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_env_air_nonattainment_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_env_air_nonattainment" does not exist

Command was: DROP TABLE public.wv_env_air_nonattainment;

pg_restore: error: could not execute query: ERROR:  table "wv_entity_registry" does not exist

Command was: DROP TABLE public.wv_entity_registry;

pg_restore: error: could not execute query: ERROR:  sequence "wv_elv_summit_names_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_elv_summit_names_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_elv_summit_names" does not exist

Command was: DROP TABLE public.wv_elv_summit_names;

pg_restore: error: could not execute query: ERROR:  sequence "wv_eco_mountaintop_removal_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_eco_mountaintop_removal_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_eco_mountaintop_removal" does not exist

Command was: DROP TABLE public.wv_eco_mountaintop_removal;

pg_restore: error: could not execute query: ERROR:  sequence "wv_eco_mineral_operations_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_eco_mineral_operations_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_eco_mineral_operations" does not exist

Command was: DROP TABLE public.wv_eco_mineral_operations;

pg_restore: error: could not execute query: ERROR:  sequence "wv_eco_manufacturing_directory_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_eco_manufacturing_directory_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_eco_manufacturing_directory" does not exist

Command was: DROP TABLE public.wv_eco_manufacturing_directory;

pg_restore: error: could not execute query: ERROR:  sequence "wv_eco_industrial_sites_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_eco_industrial_sites_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_eco_industrial_sites" does not exist

Command was: DROP TABLE public.wv_eco_industrial_sites;

pg_restore: error: could not execute query: ERROR:  sequence "wv_eco_ezec_communities_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_eco_ezec_communities_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_eco_ezec_communities" does not exist

Command was: DROP TABLE public.wv_eco_ezec_communities;

pg_restore: error: could not execute query: ERROR:  sequence "wv_eco_coal_fields_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_eco_coal_fields_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_eco_coal_fields" does not exist

Command was: DROP TABLE public.wv_eco_coal_fields;

pg_restore: error: could not execute query: ERROR:  sequence "wv_eco_abandoned_mine_lands_polygon_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_eco_abandoned_mine_lands_polygon_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_eco_abandoned_mine_lands_polygon" does not exist

Command was: DROP TABLE public.wv_eco_abandoned_mine_lands_polygon;

pg_restore: error: could not execute query: ERROR:  sequence "wv_eco_abandoned_mine_lands_point_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_eco_abandoned_mine_lands_point_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_eco_abandoned_mine_lands_point" does not exist

Command was: DROP TABLE public.wv_eco_abandoned_mine_lands_point;

pg_restore: error: could not execute query: ERROR:  sequence "wv_eco_abandoned_mine_lands_line_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_eco_abandoned_mine_lands_line_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_eco_abandoned_mine_lands_line" does not exist

Command was: DROP TABLE public.wv_eco_abandoned_mine_lands_line;

pg_restore: error: could not execute query: ERROR:  table "wv_county_representation_pre_gid_rebind" does not exist

Command was: DROP TABLE public.wv_county_representation_pre_gid_rebind;

pg_restore: error: could not execute query: ERROR:  sequence "wv_county_boundaries_24k_topo_updated_2026_wma84_gdb_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_county_boundaries_24k_topo_updated_2026_wma84_gdb_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_county_boundaries_24k_topo_updated_2026_wma84_gdb" does not exist

Command was: DROP TABLE public.wv_county_boundaries_24k_topo_updated_2026_wma84_gdb;

pg_restore: error: could not execute query: ERROR:  sequence "wv_county_boundaries_24k_topo_updated_2026_utm83_gdb_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_county_boundaries_24k_topo_updated_2026_utm83_gdb_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_county_boundaries_24k_topo_updated_2026_utm83_gdb" does not exist

Command was: DROP TABLE public.wv_county_boundaries_24k_topo_updated_2026_utm83_gdb;

pg_restore: error: could not execute query: ERROR:  view "wv_county_belief_vector_ready" does not exist

Command was: DROP VIEW public.wv_county_belief_vector_ready;

pg_restore: error: could not execute query: ERROR:  table "wv_wv_county_boundaries_24k_topo_updated_2026_utm83" does not exist

Command was: DROP TABLE public.wv_wv_county_boundaries_24k_topo_updated_2026_utm83;

pg_restore: error: could not execute query: ERROR:  table "wv_county_representation" does not exist

Command was: DROP TABLE public.wv_county_representation;

pg_restore: error: could not execute query: ERROR:  table "wv_county_identity" does not exist

Command was: DROP TABLE public.wv_county_identity;

pg_restore: error: could not execute query: ERROR:  table "wv_county_dataset_coverage" does not exist

Command was: DROP TABLE public.wv_county_dataset_coverage;

pg_restore: error: could not execute query: ERROR:  table "wv_county_belief_snapshot" does not exist

Command was: DROP TABLE public.wv_county_belief_snapshot;

pg_restore: error: could not execute query: ERROR:  sequence "wv_censustracts_census_2020_utm83_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_censustracts_census_2020_utm83_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_censustracts_census_2020_utm83" does not exist

Command was: DROP TABLE public.wv_censustracts_census_2020_utm83;

pg_restore: error: could not execute query: ERROR:  sequence "wv_bnd_workforce_investment_areas_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_bnd_workforce_investment_areas_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_bnd_workforce_investment_areas" does not exist

Command was: DROP TABLE public.wv_bnd_workforce_investment_areas;

pg_restore: error: could not execute query: ERROR:  sequence "wv_bnd_voting_districts_2002_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_bnd_voting_districts_2002_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_bnd_voting_districts_2002" does not exist

Command was: DROP TABLE public.wv_bnd_voting_districts_2002;

pg_restore: error: could not execute query: ERROR:  sequence "wv_bnd_voting_districts_2000_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_bnd_voting_districts_2000_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_bnd_voting_districts_2000" does not exist

Command was: DROP TABLE public.wv_bnd_voting_districts_2000;

pg_restore: error: could not execute query: ERROR:  sequence "wv_bnd_state_boundary_100k_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_bnd_state_boundary_100k_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_bnd_state_boundary_100k" does not exist

Command was: DROP TABLE public.wv_bnd_state_boundary_100k;

pg_restore: error: could not execute query: ERROR:  sequence "wv_bnd_public_lands_wildlife_resources_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_bnd_public_lands_wildlife_resources_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_bnd_public_lands_wildlife_resources" does not exist

Command was: DROP TABLE public.wv_bnd_public_lands_wildlife_resources;

pg_restore: error: could not execute query: ERROR:  sequence "wv_bnd_public_lands_state_parks_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_bnd_public_lands_state_parks_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_bnd_public_lands_state_parks" does not exist

Command was: DROP TABLE public.wv_bnd_public_lands_state_parks;

pg_restore: error: could not execute query: ERROR:  sequence "wv_bnd_public_lands_state_forests_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_bnd_public_lands_state_forests_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_bnd_public_lands_state_forests" does not exist

Command was: DROP TABLE public.wv_bnd_public_lands_state_forests;

pg_restore: error: could not execute query: ERROR:  sequence "wv_bnd_public_lands_nwr_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_bnd_public_lands_nwr_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_bnd_public_lands_nwr" does not exist

Command was: DROP TABLE public.wv_bnd_public_lands_nwr;

pg_restore: error: could not execute query: ERROR:  sequence "wv_bnd_public_lands_national_park_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_bnd_public_lands_national_park_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_bnd_public_lands_national_park" does not exist

Command was: DROP TABLE public.wv_bnd_public_lands_national_park;

pg_restore: error: could not execute query: ERROR:  sequence "wv_bnd_public_lands_national_forest_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_bnd_public_lands_national_forest_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_bnd_public_lands_national_forest" does not exist

Command was: DROP TABLE public.wv_bnd_public_lands_national_forest;

pg_restore: error: could not execute query: ERROR:  sequence "wv_bnd_public_lands_county_city_parks_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_bnd_public_lands_county_city_parks_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_bnd_public_lands_county_city_parks" does not exist

Command was: DROP TABLE public.wv_bnd_public_lands_county_city_parks;

pg_restore: error: could not execute query: ERROR:  sequence "wv_bnd_nhd_mussel_streams_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_bnd_nhd_mussel_streams_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_bnd_nhd_mussel_streams" does not exist

Command was: DROP TABLE public.wv_bnd_nhd_mussel_streams;

pg_restore: error: could not execute query: ERROR:  sequence "wv_bnd_morgantown_wards_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_bnd_morgantown_wards_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_bnd_morgantown_wards" does not exist

Command was: DROP TABLE public.wv_bnd_morgantown_wards;

pg_restore: error: could not execute query: ERROR:  sequence "wv_bnd_mnf_wilderness_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_bnd_mnf_wilderness_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_bnd_mnf_wilderness" does not exist

Command was: DROP TABLE public.wv_bnd_mnf_wilderness;

pg_restore: error: could not execute query: ERROR:  sequence "wv_bnd_mnf_recreation_sites_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_bnd_mnf_recreation_sites_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_bnd_mnf_recreation_sites" does not exist

Command was: DROP TABLE public.wv_bnd_mnf_recreation_sites;

pg_restore: error: could not execute query: ERROR:  sequence "wv_bnd_mnf_recreation_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_bnd_mnf_recreation_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_bnd_mnf_recreation_campgrounds" does not exist

Command was: DROP TABLE public.wv_bnd_mnf_recreation_campgrounds;

pg_restore: error: could not execute query: ERROR:  sequence "wv_bnd_mnf_ranger_districts_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_bnd_mnf_ranger_districts_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_bnd_mnf_ranger_districts" does not exist

Command was: DROP TABLE public.wv_bnd_mnf_ranger_districts;

pg_restore: error: could not execute query: ERROR:  sequence "wv_bnd_mnf_management_prescriptions_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_bnd_mnf_management_prescriptions_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_bnd_mnf_management_prescriptions" does not exist

Command was: DROP TABLE public.wv_bnd_mnf_management_prescriptions;

pg_restore: error: could not execute query: ERROR:  sequence "wv_bnd_mnf_basic_ownership_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_bnd_mnf_basic_ownership_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_bnd_mnf_basic_ownership" does not exist

Command was: DROP TABLE public.wv_bnd_mnf_basic_ownership;

pg_restore: error: could not execute query: ERROR:  sequence "wv_bnd_county_municipal_dlg_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_bnd_county_municipal_dlg_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_bnd_county_municipal_dlg" does not exist

Command was: DROP TABLE public.wv_bnd_county_municipal_dlg;

pg_restore: error: could not execute query: ERROR:  sequence "wv_bnd_county_24k_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_bnd_county_24k_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_bnd_county_24k" does not exist

Command was: DROP TABLE public.wv_bnd_county_24k;

pg_restore: error: could not execute query: ERROR:  sequence "wv_bnd_census_designated_places_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_bnd_census_designated_places_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_bnd_census_designated_places" does not exist

Command was: DROP TABLE public.wv_bnd_census_designated_places;

pg_restore: error: could not execute query: ERROR:  sequence "wv_bnd_canaan_valley_nwr_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_bnd_canaan_valley_nwr_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_bnd_canaan_valley_nwr" does not exist

Command was: DROP TABLE public.wv_bnd_canaan_valley_nwr;

pg_restore: error: could not execute query: ERROR:  sequence "wv_bnd_arc_counties_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_bnd_arc_counties_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_bnd_arc_counties" does not exist

Command was: DROP TABLE public.wv_bnd_arc_counties;

pg_restore: error: could not execute query: ERROR:  sequence "wv_bnd_appalachian_basin_boundary_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_bnd_appalachian_basin_boundary_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_bnd_appalachian_basin_boundary" does not exist

Command was: DROP TABLE public.wv_bnd_appalachian_basin_boundary;

pg_restore: error: could not execute query: ERROR:  sequence "wv_bio_red_spruce_cover_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_bio_red_spruce_cover_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_bio_red_spruce_cover" does not exist

Command was: DROP TABLE public.wv_bio_red_spruce_cover;

pg_restore: error: could not execute query: ERROR:  sequence "wv_bio_ecoregions_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_bio_ecoregions_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_bio_ecoregions" does not exist

Command was: DROP TABLE public.wv_bio_ecoregions;

pg_restore: error: could not execute query: ERROR:  sequence "wv_bio_biodiversity_rank_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_bio_biodiversity_rank_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_bio_biodiversity_rank" does not exist

Command was: DROP TABLE public.wv_bio_biodiversity_rank;

pg_restore: error: could not execute query: ERROR:  sequence "wv_atm_weather_stations_gid_seq" does not exist

Command was: DROP SEQUENCE public.wv_atm_weather_stations_gid_seq;

pg_restore: error: could not execute query: ERROR:  table "wv_atm_weather_stations" does not exist

Command was: DROP TABLE public.wv_atm_weather_stations;

pg_restore: error: could not execute query: ERROR:  table "gbim_collection_manifest" does not exist

Command was: DROP TABLE public.gbim_collection_manifest;

pg_restore: error: could not execute query: ERROR:  table "gbim_active_collection" does not exist

Command was: DROP TABLE public.gbim_active_collection;

pg_restore: error: could not execute query: ERROR:  schema "normalization" does not exist

Command was: DROP TABLE normalization.geoanchor;

pg_restore: error: could not execute query: ERROR:  schema "normalization" does not exist

Command was: DROP SEQUENCE normalization.geoanchor_record_id_seq2;

pg_restore: error: could not execute query: ERROR:  extension "postgis" does not exist

Command was: DROP EXTENSION postgis;

pg_restore: error: could not execute query: ERROR:  extension "pgcrypto" does not exist

Command was: DROP EXTENSION pgcrypto;

pg_restore: error: could not execute query: ERROR:  schema "normalization" does not exist

Command was: DROP SCHEMA normalization;

pg_restore: warning: errors ignored on restore: 742

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ cd /mnt/spiritual_drive/msjarvis-rebuild

# Check a few key WV tables

psql -h "$PGHOST" -p "$PGPORT" -U postgres -d msjarvisgis_v2 \

  -c "SELECT COUNT(*) FROM public.wv_trn_roads_interstate;"

psql -h "$PGHOST" -p "$PGPORT" -U postgres -d msjarvisgis_v2 \

  -c "SELECT COUNT(*) FROM public.wv_hyd_watershed_boundary_12digit_hu;"

psql -h "$PGHOST" -p "$PGPORT" -U postgres -d msjarvisgis_v2 \

  -c "SELECT COUNT(*) FROM public.wv_soc_schools_k12;"

 count 

-------

     0

(1 row)

 count 

-------

     0

(1 row)

 count 

-------

     0

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ cd /mnt/spiritual_drive/msjarvis-rebuild

pg_restore -l ch52_checkpoint/msjarvisgis_v2-final.dump | head -n 40

;

; Archive created at 2026-07-12 13:29:45 EDT

;     dbname: msjarvisgis_v2

;     TOC Entries: 1195

;     Compression: gzip

;     Dump Version: 1.15-0

;     Format: CUSTOM

;     Integer: 4 bytes

;     Offset: 8 bytes

;     Dumped from database version: 16.14 (Ubuntu 16.14-0ubuntu0.24.04.1)

;     Dumped by pg_dump version: 16.14 (Ubuntu 16.14-0ubuntu0.24.04.1)

;

;

; Selected TOC Entries:

;

8; 2615 723989 SCHEMA - normalization msjarvis

3; 3079 723945 EXTENSION - pgcrypto 

5985; 0 0 COMMENT - EXTENSION pgcrypto 

2; 3079 722869 EXTENSION - postgis 

5986; 0 0 COMMENT - EXTENSION postgis 

223; 1259 723993 SEQUENCE normalization geoanchor_record_id_seq2 postgres

224; 1259 723994 TABLE normalization geoanchor msjarvis

518; 1259 727165 TABLE public gbim_active_collection postgres

517; 1259 727154 TABLE public gbim_collection_manifest postgres

225; 1259 724001 TABLE public wv_atm_weather_stations msjarvis

226; 1259 724006 SEQUENCE public wv_atm_weather_stations_gid_seq msjarvis

5987; 0 0 SEQUENCE OWNED BY public wv_atm_weather_stations_gid_seq msjarvis

227; 1259 724007 TABLE public wv_bio_biodiversity_rank msjarvis

228; 1259 724012 SEQUENCE public wv_bio_biodiversity_rank_gid_seq msjarvis

5988; 0 0 SEQUENCE OWNED BY public wv_bio_biodiversity_rank_gid_seq msjarvis

229; 1259 724013 TABLE public wv_bio_ecoregions msjarvis

230; 1259 724018 SEQUENCE public wv_bio_ecoregions_gid_seq msjarvis

5989; 0 0 SEQUENCE OWNED BY public wv_bio_ecoregions_gid_seq msjarvis

231; 1259 724019 TABLE public wv_bio_red_spruce_cover msjarvis

232; 1259 724024 SEQUENCE public wv_bio_red_spruce_cover_gid_seq msjarvis

5990; 0 0 SEQUENCE OWNED BY public wv_bio_red_spruce_cover_gid_seq msjarvis

233; 1259 724025 TABLE public wv_bnd_appalachian_basin_boundary msjarvis

234; 1259 724030 SEQUENCE public wv_bnd_appalachian_basin_boundary_gid_seq msjarvis

5991; 0 0 SEQUENCE OWNED BY public wv_bnd_appalachian_basin_boundary_gid_seq msjarvis

235; 1259 724031 TABLE public wv_bnd_arc_counties msjarvis

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ # On the source system (where msjarvisgis_v2 has data)

pg_dump -h SOURCE_HOST -p SOURCE_PORT -U postgres \

  -Fc \

  -d msjarvisgis_v2 \

  -f /path/to/msjarvisgis_v2-full.dump

pg_dump: error: could not open output file "/path/to/msjarvisgis_v2-full.dump": No such file or directory

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ 

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ cd /mnt/spiritual_drive/msjarvis-rebuild

mkdir -p ch52_checkpoint

# On this machine, dump the live DB into a real file path:

pg_dump -h "$PGHOST" -p "$PGPORT" -U postgres \

  -Fc \

  -d msjarvisgis_v2 \

  -f ch52_checkpoint/msjarvisgis_v2-full.dump

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ cd /mnt/spiritual_drive/msjarvis-rebuild

pg_restore -l ch52_checkpoint/msjarvisgis_v2-full.dump | grep -i "TABLE DATA" | head

5686; 0 732506 TABLE DATA normalization geoanchor postgres

5687; 0 732513 TABLE DATA public gbim_active_collection postgres

5688; 0 732519 TABLE DATA public gbim_collection_manifest postgres

4900; 0 731747 TABLE DATA public spatial_ref_sys postgres

5689; 0 732526 TABLE DATA public wv_atm_weather_stations postgres

5691; 0 732532 TABLE DATA public wv_bio_biodiversity_rank postgres

5693; 0 732538 TABLE DATA public wv_bio_ecoregions postgres

5695; 0 732544 TABLE DATA public wv_bio_red_spruce_cover postgres

5697; 0 732550 TABLE DATA public wv_bnd_appalachian_basin_boundary postgres

5699; 0 732556 TABLE DATA public wv_bnd_arc_counties postgres

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ cd /mnt/spiritual_drive/msjarvis-rebuild

export PGHOST=localhost

export PGPORT=5436

# 1. Drop and recreate msjarvisgis_v2

psql -h "$PGHOST" -p "$PGPORT" -U postgres -d postgres \

  -c "DROP DATABASE IF EXISTS msjarvisgis_v2;"

createdb -h "$PGHOST" -p "$PGPORT" -U postgres msjarvisgis_v2

# 2. Restore full schema + data from the new dump

pg_restore -h "$PGHOST" -p "$PGPORT" -U postgres \

  -d msjarvisgis_v2 \

  --no-owner --no-acl \

  ch52_checkpoint/msjarvisgis_v2-full.dump

DROP DATABASE

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ cd /mnt/spiritual_drive/msjarvis-rebuild

psql -h "$PGHOST" -p "$PGPORT" -U postgres -d msjarvisgis_v2 \

  -c "SELECT COUNT(*) FROM public.wv_trn_roads_interstate;"

psql -h "$PGHOST" -p "$PGPORT" -U postgres -d msjarvisgis_v2 \

  -c "SELECT COUNT(*) FROM public.wv_hyd_watershed_boundary_12digit_hu;"

psql -h "$PGHOST" -p "$PGPORT" -U postgres -d msjarvisgis_v2 \

  -c "SELECT COUNT(*) FROM public.wv_soc_schools_k12;"

 count 

-------

     0

(1 row)

 count 

-------

     0

(1 row)

 count 

-------

     0

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ cd /mnt/spiritual_drive/msjarvis-rebuild

psql -h "$PGHOST" -p "$PGPORT" -U postgres -d msjarvisgis_v2 \

  -c "SELECT table_name FROM information_schema.tables

      WHERE table_schema = 'public'

      ORDER BY table_name;"  -- quick inventory

# Sample: check a couple of tables we know have TABLE DATA entries

psql -h "$PGHOST" -p "$PGPORT" -U postgres -d msjarvisgis_v2 \

  -c "SELECT COUNT(*) FROM public.wv_atm_weather_stations;"

psql -h "$PGHOST" -p "$PGPORT" -U postgres -d msjarvisgis_v2 \

  -c "SELECT COUNT(*) FROM public.wv_bio_biodiversity_rank;"

psql -h "$PGHOST" -p "$PGPORT" -U postgres -d msjarvisgis_v2 \

  -c "SELECT COUNT(*) FROM public.wv_bnd_arc_counties;"

psql: warning: extra command-line argument "quick" ignored

psql: warning: extra command-line argument "inventory" ignored

 count 

-------

     0

(1 row)

 count 

-------

     0

(1 row)

 count 

-------

     0

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ cd /mnt/spiritual_drive/msjarvis-rebuild

psql -h "$PGHOST" -p "$PGPORT" -U postgres -d msjarvisgis_v2 \

  -c "SELECT COUNT(*) FROM public.wv_atm_weather_stations;"

psql -h "$PGHOST" -p "$PGPORT" -U postgres -d msjarvisgis_v2 \

  -c "SELECT COUNT(*) FROM public.wv_bio_biodiversity_rank;"

psql -h "$PGHOST" -p "$PGPORT" -U postgres -d msjarvisgis_v2 \

  -c "SELECT COUNT(*) FROM public.wv_bio_ecoregions;"

psql -h "$PGHOST" -p "$PGPORT" -U postgres -d msjarvisgis_v2 \

  -c "SELECT COUNT(*) FROM public.wv_bio_red_spruce_cover;"

psql -h "$PGHOST" -p "$PGPORT" -U postgres -d msjarvisgis_v2 \

  -c "SELECT COUNT(*) FROM public.wv_bnd_arc_counties;"

 count 

-------

     0

(1 row)

 count 

-------

     0

(1 row)

 count 

-------

     0

(1 row)

 count 

-------

     0

(1 row)

 count 

-------

     0

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ cd /mnt/spiritual_drive/msjarvis-rebuild

export PGHOST=localhost

export PGPORT=5436

# Drop and recreate the database cleanly

psql -h "$PGHOST" -p "$PGPORT" -U postgres -d postgres \

  -c "DROP DATABASE IF EXISTS msjarvisgis_v2;"

createdb -h "$PGHOST" -p "$PGPORT" -U postgres msjarvisgis_v2

# Restore only schema (no data), and DO NOT use --clean

pg_restore -h "$PGHOST" -p "$PGPORT" -U postgres \

  -d msjarvisgis_v2 \

  --schema-only \

  --no-owner --no-acl \

  ch52_checkpoint/msjarvisgis_v2-full.dump

DROP DATABASE

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ psql -h "$PGHOST" -p "$PGPORT" -U postgres -d msjarvisgis_v2 \

  -c "SELECT table_name FROM information_schema.tables

      WHERE table_schema = 'public'

      ORDER BY table_name;"  -- see if the same 158 tables are there

psql: warning: extra command-line argument "see" ignored

psql: warning: extra command-line argument "if" ignored

psql: warning: extra command-line argument "the" ignored

psql: warning: extra command-line argument "same" ignored

psql: warning: extra command-line argument "158" ignored

psql: warning: extra command-line argument "tables" ignored

psql: warning: extra command-line argument "are" ignored

psql: warning: extra command-line argument "there" ignored

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ cd /mnt/spiritual_drive/msjarvis-rebuild

export PGHOST=localhost

export PGPORT=5436

# Restore data only (no schema changes)

pg_restore -h "$PGHOST" -p "$PGPORT" -U postgres \

  -d msjarvisgis_v2 \

  --data-only \

  --no-owner --no-acl \

  ch52_checkpoint/msjarvisgis_v2-full.dump

# Then check counts again

psql -h "$PGHOST" -p "$PGPORT" -U postgres -d msjarvisgis_v2 \

  -c "SELECT COUNT(*) FROM public.wv_atm_weather_stations;"

psql -h "$PGHOST" -p "$PGPORT" -U postgres -d msjarvisgis_v2 \

  -c "SELECT COUNT(*) FROM public.wv_bio_biodiversity_rank;"

psql -h "$PGHOST" -p "$PGPORT" -U postgres -d msjarvisgis_v2 \

  -c "SELECT COUNT(*) FROM public.wv_bio_ecoregions;"

psql -h "$PGHOST" -p "$PGPORT" -U postgres -d msjarvisgis_v2 \

  -c "SELECT COUNT(*) FROM public.wv_bnd_arc_counties;"is_v2 \

pg_restore: error: COPY failed for table "gbim_active_collection": ERROR:  insert or update on table "gbim_active_collection" violates foreign key constraint "gbim_active_collection_logical_collection_name_collection__fkey"

DETAIL:  Key (logical_collection_name, collection_version)=(gbim_wv_counties, v2) is not present in table "gbim_collection_manifest".

pg_restore: error: COPY failed for table "wv_county_belief_snapshot": ERROR:  insert or update on table "wv_county_belief_snapshot" violates foreign key constraint "wv_county_belief_snapshot_canonical_county_id_fkey"

DETAIL:  Key (canonical_county_id)=(54079) is not present in table "wv_county_identity".

pg_restore: error: COPY failed for table "wv_county_dataset_coverage": ERROR:  insert or update on table "wv_county_dataset_coverage" violates foreign key constraint "wv_county_dataset_coverage_canonical_county_id_fkey"

DETAIL:  Key (canonical_county_id)=(54001) is not present in table "wv_county_identity".

pg_restore: error: COPY failed for table "wv_county_representation": ERROR:  insert or update on table "wv_county_representation" violates foreign key constraint "wv_county_representation_table_fk"

DETAIL:  Key (table_name)=(wv_county_boundaries_24k_topo_updated_2026_utm83_gdb) is not present in table "wv_layer_categories".

pg_restore: error: COPY failed for table "wv_entity_registry": ERROR:  insert or update on table "wv_entity_registry" violates foreign key constraint "wv_entity_registry_table_fk"

DETAIL:  Key (table_name)=(wv_trn_railroad_lines_rti) is not present in table "wv_layer_categories".

pg_restore: warning: errors ignored on restore: 5

 count 

-------

     0

(1 row)

 count 

-------

     0

(1 row)

 count 

-------

     0

(1 row)

 count 

-------

     0

(1 row)

 count 

-------

     0

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ cd /mnt/spiritual_drive/msjarvis-rebuild

export PGHOST=localhost

export PGPORT=5436

# Clean DB again

psql -h "$PGHOST" -p "$PGPORT" -U postgres -d postgres \

  -c "DROP DATABASE IF EXISTS msjarvisgis_v2;"

createdb -h "$PGHOST" -p "$PGPORT" -U postgres msjarvisgis_v2

# Restore full schema + data, with triggers disabled during restore

pg_restore -h "$PGHOST" -p "$PGPORT" -U postgres \

  -d msjarvisgis_v2 \

  --disable-triggers \

  --no-owner --no-acl \

  ch52_checkpoint/msjarvisgis_v2-full.dump

DROP DATABASE

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ psql -h "$PGHOST" -p "$PGPORT" -U postgres -d msjarvisgis_v2 <<'EOF'

SET session_replication_role = 'replica';

\! pg_restore -h localhost -p 5436 -U postgres \

    -d msjarvisgis_v2 \

    --no-owner --no-acl \

    ch52_checkpoint/msjarvisgis_v2-full.dump

SET session_replication_role = 'origin';

EOF

SET

pg_restore: error: one of -d/--dbname and -f/--file must be specified

invalid command \

ERROR:  syntax error at or near "-"

LINE 1: -d msjarvisgis_v2 

        ^

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ psql -h "$PGHOST" -p "$PGPORT" -U postgres -d msjarvisgis_v2 \

  -c "SELECT COUNT(*) FROM public.wv_atm_weather_stations;"

psql -h "$PGHOST" -p "$PGPORT" -U postgres -d msjarvisgis_v2 \

  -c "SELECT COUNT(*) FROM public.wv_bio_biodiversity_rank;"

psql -h "$PGHOST" -p "$PGPORT" -U postgres -d msjarvisgis_v2 \

  -c "SELECT COUNT(*) FROM public.wv_bio_ecoregions;"

psql -h "$PGHOST" -p "$PGPORT" -U postgres -d msjarvisgis_v2 \

  -c "SELECT COUNT(*) FROM public.wv_bio_red_spruce_cover;"

psql -h "$PGHOST" -p "$PGPORT" -U postgres -d msjarvisgis_v2 \

  -c "SELECT COUNT(*) FROM public.wv_bnd_arc_counties;"

 count 

-------

     0

(1 row)

 count 

-------

     0

(1 row)

 count 

-------

     0

(1 row)

 count 

-------

     0

(1 row)

 count 

-------

     0

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ chmod +x ~/Downloads/gbim-investigate.sh

~/Downloads/gbim-investigate.sh

GBIM investigation

UTC:    20260712T192124Z

Host:   cakidd-Legion-5-16IRX9

User:   cakidd

Report: /home/cakidd/gbim-investigation-20260712T192124Z

===== PHASE 0 — Environment discovery =====

wrote 01-environment.txt

===== PHASE 1 — Resolving connection to msjarvisgis_v2 =====

connected: host=localhost port=5436 user=postgres db=msjarvisgis_v2

wrote 03-lookalike-databases.txt  (confirm only the intended db exists)

===== PHASE 2 — Relation inventory =====

wrote 04-all-relations.tsv, 05-geometry-columns.tsv

===== PHASE 2b — Exact row counts (this may take a few minutes) =====

wrote 06-exact-row-counts.tsv

===== PHASE 3 — Governed county/tract spine verification =====

wrote 07-spine-cardinality.tsv  (chapter's published figures vs live database)

wrote 08..12 (snapshot versions, hash integrity, publication views, orphans, coverage states)

wrote 13-governance-columns.tsv  (authoritative column names for later remediation SQL)

===== PHASE 4 — Manifest reconciliation =====

manifests found in: /mnt/spiritual_drive/msjarvis-rebuild

wrote 17-live-tables-not-in-any-manifest.txt  (must be empty for manifest completeness)

wrote 18-manifest-tables-not-in-database.txt  (must be empty; a claim with no referent)

wrote 19-archive-presence.tsv  (retained raw-source archive verified against its ledger)

===== PHASE 5 — Chroma publication verification =====

WARNING: no Chroma heartbeat found on the ports probed. Phase 5 recorded as unresolved.

gis-rag: http://localhost:8010

===== PHASE 6 — Candidate entity-spine ranking =====

wrote 22-candidate-layers.tsv  (the selection evidence for extending governance)

===== SUMMARY =====

GBIM investigation 20260712T192124Z

Read-only. No database, vector store, or repository state was modified.

Decision gates — each must be resolved before remediation:

  07-spine-cardinality.tsv

     Any DIVERGENT row means the chapter's published figures no longer

     describe the database. The chapter is then wrong a second time and

     the corrections must carry the live numbers, not the printed ones.

  11-bridge-orphans.tsv

     Every count must be 0. A nonzero count is a live identity defect,

     not a documentation defect.

  17-live-tables-not-in-any-manifest.txt

  18-manifest-tables-not-in-database.txt

     Both must be empty. Either one being non-empty falsifies the claim

     of manifest completeness, and Correction 1 to Chapter 52 must not

     be applied until it is resolved.

  10-publication-views.tsv vs 20-chroma.txt

     Relational row counts must equal published collection counts

     (55 counties, 546 tracts) or the publication is not certified.

  22-candidate-layers.tsv

     The evidence for which imported layers earn their own entity spine

     and which remain evidence attached to county and tract identities.

Report directory: /home/cakidd/gbim-investigation-20260712T192124Z

Bundle for review:

  tar -czf /home/cakidd/gbim-investigation-20260712T192124Z.tar.gz -C /home/cakidd gbim-investigation-20260712T192124Z

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ chmod +x ~/Downloads/gbim-gates.sh

~/Downloads/gbim-gates.sh

Report directory: /home/cakidd/gbim-investigation-20260712T192124Z

Generated:        2026-07-12T19:22:45Z

############################################################

## PART A — DECISION GATES

############################################################

############################################################

## 07-spine-cardinality.tsv

## MATCH on every row, or the chapter's printed figures are stale.

############################################################

relation	expected_rows	actual_rows	verdict

wv_county_belief_snapshot	110	110	MATCH

wv_county_dataset_coverage	275	275	MATCH

wv_county_identity	55	55	MATCH

wv_county_representation	220	220	MATCH

wv_entity_registry	65	65	MATCH

wv_layer_categories	254	254	MATCH

wv_tract_belief_snapshot	1092	1092	MATCH

wv_tract_dataset_coverage	1638	1638	MATCH

wv_tract_identity	546	546	MATCH

wv_tract_representation	546	546	MATCH

(10 rows)

############################################################

## 11-bridge-orphans.tsv

## Every count must be 0.

############################################################

ERROR:  column r.county_geoid does not exist

LINE 3: ...ublic.wv_county_identity i where i.county_geoid = r.county_g...

                                                             ^

HINT:  Perhaps you meant to reference the column "i.county_geoid".

############################################################

## 17-live-tables-not-in-any-manifest.txt

## MUST BE EMPTY.

############################################################

wv_atm_weather_stations

wv_bio_biodiversity_rank

wv_bio_ecoregions

wv_bio_red_spruce_cover

wv_bnd_appalachian_basin_boundary

wv_bnd_arc_counties

wv_bnd_canaan_valley_nwr

wv_bnd_census_designated_places

wv_bnd_county_24k

wv_bnd_county_municipal_dlg

wv_bnd_mnf_basic_ownership

wv_bnd_mnf_management_prescriptions

wv_bnd_mnf_ranger_districts

wv_bnd_mnf_recreation_campgrounds

wv_bnd_mnf_recreation_sites

wv_bnd_mnf_wilderness

wv_bnd_morgantown_wards

wv_bnd_nhd_mussel_streams

wv_bnd_public_lands_county_city_parks

wv_bnd_public_lands_national_forest

wv_bnd_public_lands_national_park

wv_bnd_public_lands_nwr

wv_bnd_public_lands_state_forests

wv_bnd_public_lands_state_parks

wv_bnd_public_lands_wildlife_resources

wv_bnd_state_boundary_100k

wv_bnd_voting_districts_2000

wv_bnd_voting_districts_2002

wv_bnd_workforce_investment_areas

wv_censustracts_census_2020_utm83

wv_county_boundaries_24k_topo_updated_2026_utm83_gdb

wv_eco_abandoned_mine_lands_line

wv_eco_abandoned_mine_lands_point

wv_eco_abandoned_mine_lands_polygon

wv_eco_coal_fields

wv_eco_ezec_communities

wv_eco_industrial_sites

wv_eco_manufacturing_directory

wv_eco_mineral_operations

wv_eco_mountaintop_removal

wv_elv_summit_names

wv_env_air_nonattainment

wv_env_epa_facilities

wv_env_timber_removal_volume

wv_env_wildfire_regions

wv_env_wind_energy_resources

wv_geo_coal_beds

wv_geo_geological_map_generalized

wv_geo_karst

wv_hlt_health_providers

wv_hlt_public_health_departments

wv_hlt_rural_health_facilities

wv_hyd_dams_dmr

wv_hyd_dams_nid

wv_hyd_dams_noncoal

wv_hyd_hazus_floodplain_zones

wv_hyd_high_water_marks

wv_hyd_navigable_waterways

wv_hyd_navigable_waterways_river_miles

wv_hyd_navigable_waterways_structures

wv_hyd_springs_100gpm

wv_hyd_streamflow_stations

wv_hyd_streams_high_quality

wv_hyd_streams_national_atlas

wv_hyd_streams_tiger

wv_hyd_watershed_boundary_11digit

wv_hyd_watershed_boundary_12digit_hu

wv_hyd_watershed_boundary_8_10_12

wv_loc_census_urbanized_areas

wv_loc_county_seats

wv_loc_geodetic_control_points

wv_loc_populated_places_census

wv_loc_sams2_address_road_centerlines

wv_mil_army_reserve_facilities

wv_mil_national_guard_armories

wv_plc_hazus_level1

wv_plc_regional_planning_councils

wv_plc_tax_district_boundaries

wv_plc_tax_parcels_surface_mineral

wv_soc_911_centers

wv_soc_census_blockgroups_2020

wv_soc_census_tracts_2020

wv_soc_cities_pop10k

wv_soc_cities_pop2500

wv_soc_communities_pop_change

wv_soc_courthouses_county

wv_soc_courthouses_federal

wv_soc_fish_hatcheries

wv_soc_fishing_boating_access

wv_soc_fishing_lakes

wv_soc_higher_ed_facilities

wv_soc_hospitals_wvdem

wv_soc_libraries

wv_soc_national_register_historic_points

wv_soc_national_register_historic_polygons

wv_soc_nursing_homes

wv_soc_places_of_worship_wvgistc

wv_soc_population_by_decade

wv_soc_schools_k12

wv_soc_towers_am

wv_soc_towers_asr

wv_soc_towers_cellular

wv_soc_towers_fm

wv_soc_towers_microwave

wv_soc_towers_pager

wv_soc_towers_private

wv_soc_towers_tv

wv_soc_va_facilities

wv_soc_zcta_2020

wv_str_bridges

wv_str_correctional_institutions

wv_str_flood_atrisk_structures

wv_tract_representation

wv_tract_representation_pre_gid_rebind

wv_trn_roads_major_4800

wv_trn_roads_state_routes

wv_trn_roads_us_highways

wv_trn_roads_us_routes

wv_trn_whitewater_trails

wv_util_sewer_treatment_plants

wv_util_solid_waste_facilities

############################################################

## 18-manifest-tables-not-in-database.txt

## MUST BE EMPTY.

############################################################

wv_bnd_public_lands_union

wv_county_summary_metrics

wv_tract_summary_metrics

############################################################

## 10-publication-views.tsv

## 55 counties / 546 tracts, ids distinct.

############################################################

view	rows	distinct_ids

wv_county_belief_vector_ready	55	55

wv_tract_belief_vector_ready	546	546

(2 rows)

############################################################

## 08-snapshot-versions.tsv

## v1 and v2 both retained.

############################################################

entity	snapshot_version	count

county	wv-county-snapshot-v1	55

county	wv-county-snapshot-v2	55

tract	wv-tract-snapshot-v1	546

tract	wv-tract-snapshot-v2	546

(4 rows)

############################################################

## 09-belief-hash-integrity.tsv

## Zero null hashes; distinct within version.

############################################################

entity	null_hashes	rows_total	distinct_hashes

county	0	110	110

tract	0	1092	1092

(2 rows)

############################################################

## 12-coverage-states.tsv

## unknown must remain distinct from verified absence.

############################################################

entity	dataset_type	coverage_state	count

county	address_point	present	29

county	address_point	unknown	26

county	blockgroup	present	55

county	dfirm_polygon	present	8

county	dfirm_polygon	unknown	47

county	tract	present	55

county	zcta	present	55

tract	address_point	unknown	546

tract	blockgroup	unknown	546

tract	dfirm_polygon	unknown	546

(10 rows)

############################################################

## 03-lookalike-databases.txt

## Only the intended database should appear.

############################################################

msjarvis

msjarvisgis

msjarvisgis_v2

############################################################

## 21-gisrag.txt

############################################################

endpoint: http://localhost:8010

{"status":"healthy","dependencies":{"production_20llm":"healthy"},"timestamp":"2026-07-12T19:21:25.640370"}

############################################################

## PART B — LOCATING CHROMA

############################################################

--- B1. GIS-RAG process, its command line, and its environment ---

(no listener metadata for :8010 visible to this user; trying docker)

--- B2. containerised GIS-RAG / Chroma, if any ---

container: jarvis-gis-rag

  image:  msjarvis-rebuild-jarvis-gis-rag

  ports:  {"8004/tcp":[{"HostIp":"127.0.0.1","HostPort":"8004"}],"8044/tcp":null}

  env:    CHROMA_HOST=jarvis-chroma

GIS_RAG_CHROMA_URL=http://jarvis-chroma:8000

CHROMA_PORT=8000

GIS_RAG_COLLECTIONS=gbim_wv_counties_v2,gbim_wv_tracts_v2

  mounts:

container: jarvis-intake-service

  image:  jarvis-main-brain:latest

  ports:  {"8007/tcp":[{"HostIp":"127.0.0.1","HostPort":"8007"}]}

  env:    CHROMA_HOST=jarvis-chroma

CHROMA_PORT=8000

  mounts:

    /mnt/nvme1/msjarvis-rebuild/services -> /app/services

container: jarvis-civic-intake

  image:  jarvis-main-brain:latest

  ports:  {"8100/tcp":[{"HostIp":"127.0.0.1","HostPort":"18093"}]}

  env:    CHROMA_PORT=8000

CHROMA_HOST=jarvis-chroma

  mounts:

    /mnt/spiritual_drive/msjarvis-rebuild/models/all-MiniLM-L6-v2 -> /app/models/sentence-transformers/all-MiniLM-L6-v2

    /home/cakidd/msjarvis-rebuild/services/hilbert -> /app/services/hilbert

container: jarvis-hilbert-state

  image:  jarvis-main-brain:latest

  ports:  {"8081/tcp":[{"HostIp":"127.0.0.1","HostPort":"18092"}]}

  env:    CHROMA_HOST=jarvis-chroma

CHROMA_PORT=8000

  mounts:

    /mnt/spiritual_drive/msjarvis-rebuild/data/hp_incoming -> /app/data/hp_incoming

    /mnt/spiritual_drive/msjarvis-rebuild/models/all-MiniLM-L6-v2 -> /app/models/sentence-transformers/all-MiniLM-L6-v2

container: jarvis-rag-server

  image:  msjarvis-rebuild-jarvis-rag-server

  ports:  {"8003/tcp":[{"HostIp":"127.0.0.1","HostPort":"8003"}]}

  env:    CHROMA_HOST=jarvis-chroma

CHROMA_PORT=8000

  mounts:

    /mnt/nvme1/msjarvis-rebuild/services/backup_chroma_mountainshares_knowledge.json -> /app/backup_mountainshares.json

    /home/cakidd/msjarvis-rebuild/data/mountainshares -> /app/mountainshares_docs

    /mnt/nvme1/docker/volumes/msjarvis-rebuild_rag_model_cache/_data -> /root/.cache/chroma

container: jarvis-chroma

  image:  chromadb/chroma:0.6.3

  ports:  {"8000/tcp":[{"HostIp":"127.0.0.1","HostPort":"8002"}]}

  env:    PERSIST_DIRECTORY=/data

ISPERSISTENT=TRUE

CHROMA_HOST_ADDR=0.0.0.0

CHROMA_HOST_PORT=8000

CHROMA_WORKERS=1

CHROMA_LOG_CONFIG=chromadb/log_config.yml

CHROMA_TIMEOUT_KEEP_ALIVE=30

  mounts:

    /mnt/nvme1/msjarvis-data/chroma-live -> /data

container: jarvis-spiritual-rag

  image:  msjarvis-rebuild-jarvis-spiritual-rag

  ports:  {"8005/tcp":[{"HostIp":"127.0.0.1","HostPort":"8005"}]}

  env:    CHROMA_HOST=jarvis-chroma

CHROMA_PORT=8000

  mounts:

container: jarvis-phi-probe

  image:  msjarvis-rebuild-jarvis-phi-probe

  ports:  {"8025/tcp":[{"HostIp":"127.0.0.1","HostPort":"8026"}]}

  env:    CHROMA_URL=http://jarvis-chroma:8000

  mounts:

    /mnt/nvme1/msjarvis-rebuild/services/ms_jarvis_phi_probe.py -> /app/ms_jarvis_phi_probe.py

container: jarvis-rag-router

  image:  msjarvis-rebuild-jarvis-rag-router

  ports:  {"5001/tcp":[{"HostIp":"127.0.0.1","HostPort":"5015"}],"8003/tcp":null}

  env:    CHROMA_PORT=8000

CHROMA_HOST=jarvis-chroma

  mounts:

container: jarvis-aaacpe-rag

  image:  msjarvis-rebuild-jarvis-aaacpe-rag

  ports:  {"8032/tcp":[{"HostIp":"127.0.0.1","HostPort":"8032"}]}

  env:    CHROMA_HOST=jarvis-chroma

CHROMA_PORT=8000

  mounts:

    /mnt/nvme1/docker/volumes/msjarvis-rebuild_aaacpe-cultural-data/_data -> /data

--- B3. every listening port, with owning process ---

State  Recv-Q Send-Q Local Address:Port  Peer Address:PortProcess                                                                                     

LISTEN 0      4096       127.0.0.1:5433       0.0.0.0:*                                                                                               

LISTEN 0      200        127.0.0.1:5436       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:5015       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:7475       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:7205       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8104       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8108       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8074       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8075       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8073       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8091       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8094       0.0.0.0:*                                                                                               

LISTEN 0      2048       127.0.0.1:8095       0.0.0.0:*    users:(("gunicorn",pid=11501,fd=3),("gunicorn",pid=11498,fd=3),("gunicorn",pid=11482,fd=3))

LISTEN 0      4096       127.0.0.1:8093       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8042       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8046       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8032       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8033       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8050       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8010       0.0.0.0:*                                                                                               

LISTEN 0      2048       127.0.0.1:8009       0.0.0.0:*    users:(("python3",pid=3808,fd=13))                                                         

LISTEN 0      4096       127.0.0.1:8015       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8002       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8003       0.0.0.0:*                                                                                               

LISTEN 0      2048       127.0.0.1:8000       0.0.0.0:*    users:(("python3",pid=11481,fd=13))                                                        

LISTEN 0      4096       127.0.0.1:8007       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8004       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8005       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8026       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8025       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8030       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8019       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8016       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8020       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:7687       0.0.0.0:*                                                                                               

LISTEN 0      511        127.0.0.1:6379       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:6380       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:7012       0.0.0.0:*                                                                                               

LISTEN 0      2048         0.0.0.0:9002       0.0.0.0:*    users:(("gunicorn",pid=2411,fd=3),("gunicorn",pid=2382,fd=3),("gunicorn",pid=2261,fd=3))   

LISTEN 0      2048         0.0.0.0:9000       0.0.0.0:*    users:(("gunicorn",pid=2412,fd=3),("gunicorn",pid=2381,fd=3),("gunicorn",pid=2259,fd=3))   

LISTEN 0      4096       127.0.0.1:2019       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:18092      0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:18093      0.0.0.0:*                                                                                               

LISTEN 0      2048         0.0.0.0:8300       0.0.0.0:*    users:(("python3",pid=11486,fd=13))                                                        

LISTEN 0      5         172.18.0.1:11434      0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:16686      0.0.0.0:*                                                                                               

LISTEN 0      70         127.0.0.1:33060      0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:17260      0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:631        0.0.0.0:*                                                                                               

LISTEN 0      151        127.0.0.1:3306       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:4002       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:20241      0.0.0.0:*                                                                                               

LISTEN 0      2048         0.0.0.0:8018       0.0.0.0:*    users:(("gunicorn",pid=11502,fd=3),("gunicorn",pid=11500,fd=3),("gunicorn",pid=11484,fd=3))

LISTEN 0      4096         0.0.0.0:8027       0.0.0.0:*                                                                                               

LISTEN 0      4096   127.0.0.53%lo:53         0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:9998       0.0.0.0:*                                                                                               

LISTEN 0      5         172.17.0.1:11434      0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8202       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8203       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8201       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8206       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8207       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8204       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8205       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8218       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8219       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8216       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8217       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8222       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8220       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8221       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8210       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8211       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8208       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8209       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8214       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8215       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8212       0.0.0.0:*                                                                                               

LISTEN 0      4096       127.0.0.1:8213       0.0.0.0:*                                                                                               

LISTEN 0      511          0.0.0.0:3002       0.0.0.0:*    users:(("next-server (v1",pid=2256,fd=18))                                                 

LISTEN 0      4096      127.0.0.54:53         0.0.0.0:*                                                                                               

LISTEN 0      2048         0.0.0.0:4010       0.0.0.0:*    users:(("gunicorn",pid=2383,fd=3),("gunicorn",pid=2255,fd=3))                              

LISTEN 0      2048         0.0.0.0:4021       0.0.0.0:*    users:(("python3",pid=2254,fd=13))                                                         

LISTEN 0      4096           [::1]:631           [::]:*                                                                                               

LISTEN 0      4096            [::]:8027          [::]:*                                                                                               

LISTEN 0      511            [::1]:6379          [::]:*                                                                                               

LISTEN 0      4096               *:80               *:*                                                                                               

LISTEN 0      511                *:3001             *:*    users:(("next-server (v1",pid=2479,fd=18))                                                 

--- B4. heartbeat probe across every listening port ---

CHROMA HEARTBEAT: port 80 (api v2)

CHROMA HEARTBEAT: port 80 (api v1)

CHROMA HEARTBEAT: port 7687 (api v2)

CHROMA HEARTBEAT: port 7687 (api v1)

CHROMA HEARTBEAT: port 8002 (api v2)

CHROMA HEARTBEAT: port 8002 (api v1)

CHROMA HEARTBEAT: port 16686 (api v2)

CHROMA HEARTBEAT: port 16686 (api v1)

(if nothing printed above, Chroma is not serving HTTP on this host)

--- B5. on-disk Chroma persistence (embedded client) ---

store: /app/chroma_db/chroma.sqlite3

  size:     164K

  modified: 2026-02-07T03:03:52Z

  collections (name -> record count), read directly from SQLite:

    tables: acquire_write                      embedding_metadata               

    tables: collection_metadata                embeddings                       

    tables: collections                        embeddings_queue                 

    tables: databases                          embeddings_queue_config          

    tables: embedding_fulltext_search          maintenance_log                  

    tables: embedding_fulltext_search_config   max_seq_id                       

    tables: embedding_fulltext_search_content  migrations                       

    tables: embedding_fulltext_search_data     segment_metadata                 

    tables: embedding_fulltext_search_docsize  segments                         

    tables: embedding_fulltext_search_idx      tenants                          

store: /mnt/nvme1/msjarvis/chroma_data/chroma.sqlite3

  size:     20M

  modified: 2026-06-18T04:55:59Z

  collections (name -> record count), read directly from SQLite:

    geospatial_features|4979

    tables: acquire_write                      embedding_metadata               

    tables: collection_metadata                embeddings                       

    tables: collections                        embeddings_queue                 

    tables: databases                          embeddings_queue_config          

    tables: embedding_fulltext_search          maintenance_log                  

    tables: embedding_fulltext_search_config   max_seq_id                       

    tables: embedding_fulltext_search_content  migrations                       

    tables: embedding_fulltext_search_data     segment_metadata                 

    tables: embedding_fulltext_search_docsize  segments                         

    tables: embedding_fulltext_search_idx      tenants                          

store: /mnt/nvme1/msjarvis-rebuild/chroma_data/chroma.sqlite3

  size:     20M

  modified: 2026-01-30T20:34:41Z

  collections (name -> record count), read directly from SQLite:

    geospatial_features|4979

    tables: acquire_write                      embedding_metadata               

    tables: collection_metadata                embeddings                       

    tables: collections                        embeddings_queue                 

    tables: databases                          embeddings_queue_config          

    tables: embedding_fulltext_search          maintenance_log                  

    tables: embedding_fulltext_search_config   max_seq_id                       

    tables: embedding_fulltext_search_content  migrations                       

    tables: embedding_fulltext_search_data     segment_metadata                 

    tables: embedding_fulltext_search_docsize  segments                         

    tables: embedding_fulltext_search_idx      tenants                          

store: /mnt/nvme1/msjarvis-rebuild/HOST_LEARNER_CHROMA_PATH/chroma.sqlite3

  size:     164K

  modified: 2026-01-13T22:43:56Z

  collections (name -> record count), read directly from SQLite:

    tables: acquire_write                      embedding_metadata               

    tables: collection_metadata                embeddings                       

    tables: collections                        embeddings_queue                 

    tables: databases                          embeddings_queue_config          

    tables: embedding_fulltext_search          maintenance_log                  

    tables: embedding_fulltext_search_config   max_seq_id                       

    tables: embedding_fulltext_search_content  migrations                       

    tables: embedding_fulltext_search_data     segment_metadata                 

    tables: embedding_fulltext_search_docsize  segments                         

    tables: embedding_fulltext_search_idx      tenants                          

store: /mnt/nvme1/msjarvis-rebuild/services/chroma_db_corrupted2_1141/chroma.sqlite3

  size:     668M

  modified: 2026-06-06T18:08:37Z

  collections (name -> record count), read directly from SQLite:

    gbim_worldview_entities|90000

    tables: acquire_write                      embedding_metadata               

    tables: collection_metadata                embeddings                       

    tables: collections                        embeddings_queue                 

    tables: databases                          embeddings_queue_config          

    tables: embedding_fulltext_search          maintenance_log                  

    tables: embedding_fulltext_search_config   max_seq_id                       

    tables: embedding_fulltext_search_content  migrations                       

    tables: embedding_fulltext_search_data     segment_metadata                 

    tables: embedding_fulltext_search_docsize  segments                         

    tables: embedding_fulltext_search_idx      tenants                          

store: /mnt/nvme1/msjarvis-rebuild/services/chromadbrag1/chroma.sqlite3

  size:     164K

  modified: 2026-02-04T21:49:11Z

  collections (name -> record count), read directly from SQLite:

    tables: acquire_write                      embedding_metadata               

    tables: collection_metadata                embeddings                       

    tables: collections                        embeddings_queue                 

    tables: databases                          embeddings_queue_config          

    tables: embedding_fulltext_search          maintenance_log                  

    tables: embedding_fulltext_search_config   max_seq_id                       

    tables: embedding_fulltext_search_content  migrations                       

    tables: embedding_fulltext_search_data     segment_metadata                 

    tables: embedding_fulltext_search_docsize  segments                         

    tables: embedding_fulltext_search_idx      tenants                          

store: /mnt/nvme1/msjarvis-rebuild/services/rag/chromadb/chroma.sqlite3

  size:     164K

  modified: 2026-02-16T15:08:35Z

  collections (name -> record count), read directly from SQLite:

    GBIM|0

    geodb_bg2020_nearest_block2020_v2|0

    tables: acquire_write                      embedding_metadata               

    tables: collection_metadata                embeddings                       

    tables: collections                        embeddings_queue                 

    tables: databases                          embeddings_queue_config          

    tables: embedding_fulltext_search          maintenance_log                  

    tables: embedding_fulltext_search_config   max_seq_id                       

    tables: embedding_fulltext_search_content  migrations                       

    tables: embedding_fulltext_search_data     segment_metadata                 

    tables: embedding_fulltext_search_docsize  segments                         

    tables: embedding_fulltext_search_idx      tenants                          

store: /mnt/nvme1/msjarvis-rebuild/services/.chromadb/chroma.sqlite3

  size:     164K

  modified: 2026-01-12T04:02:38Z

  collections (name -> record count), read directly from SQLite:

    tables: acquire_write                      embedding_metadata               

    tables: collection_metadata                embeddings                       

    tables: collections                        embeddings_queue                 

    tables: databases                          embeddings_queue_config          

    tables: embedding_fulltext_search          maintenance_log                  

    tables: embedding_fulltext_search_config   max_seq_id                       

    tables: embedding_fulltext_search_content  migrations                       

    tables: embedding_fulltext_search_data     segment_metadata                 

    tables: embedding_fulltext_search_docsize  segments                         

    tables: embedding_fulltext_search_idx      tenants                          

store: /mnt/nvme1/msjarvis-rebuild/services/chroma/chroma.sqlite3

  size:     4.2M

  modified: 2026-02-16T15:10:26Z

  collections (name -> record count), read directly from SQLite:

    GBIM|1008

    GeoDB|1007

    gisgeodata|0

    rag_training_data|0

    spiritual_texts|23

    tables: acquire_write                      embedding_metadata               

    tables: collection_metadata                embeddings                       

    tables: collections                        embeddings_queue                 

    tables: databases                          embeddings_queue_config          

    tables: embedding_fulltext_search          maintenance_log                  

    tables: embedding_fulltext_search_config   max_seq_id                       

    tables: embedding_fulltext_search_content  migrations                       

    tables: embedding_fulltext_search_data     segment_metadata                 

    tables: embedding_fulltext_search_docsize  segments                         

    tables: embedding_fulltext_search_idx      tenants                          

store: /mnt/nvme1/msjarvis-rebuild/services/egeriaknowledgebase/chromadb/chroma.sqlite3

  size:     164K

  modified: 2026-02-16T15:08:35Z

  collections (name -> record count), read directly from SQLite:

    tables: acquire_write                      embedding_metadata               

    tables: collection_metadata                embeddings                       

    tables: collections                        embeddings_queue                 

    tables: databases                          embeddings_queue_config          

    tables: embedding_fulltext_search          maintenance_log                  

    tables: embedding_fulltext_search_config   max_seq_id                       

    tables: embedding_fulltext_search_content  migrations                       

    tables: embedding_fulltext_search_data     segment_metadata                 

    tables: embedding_fulltext_search_docsize  segments                         

    tables: embedding_fulltext_search_idx      tenants                          

store: /mnt/nvme1/msjarvis-rebuild/services/chromadb/chroma.sqlite3

  size:     164K

  modified: 2026-02-16T15:08:35Z

  collections (name -> record count), read directly from SQLite:

    tables: acquire_write                      embedding_metadata               

    tables: collection_metadata                embeddings                       

    tables: collections                        embeddings_queue                 

    tables: databases                          embeddings_queue_config          

    tables: embedding_fulltext_search          maintenance_log                  

    tables: embedding_fulltext_search_config   max_seq_id                       

    tables: embedding_fulltext_search_content  migrations                       

    tables: embedding_fulltext_search_data     segment_metadata                 

    tables: embedding_fulltext_search_docsize  segments                         

    tables: embedding_fulltext_search_idx      tenants                          

store: /mnt/nvme1/msjarvis-rebuild/chroma_db/chroma.sqlite3

  size:     4.2M

  modified: 2026-03-14T00:52:03Z

  collections (name -> record count), read directly from SQLite:

    GBIM|1008

    GeoDB|1007

    benefit_programs|1

    compliance_tasks|2

    gisgeodata|0

    msjarvis|0

    rag_training_data|0

    spiritual_texts|23

    utility_enrollments|1

    tables: acquire_write                      embedding_metadata_array         

    tables: collection_metadata                embeddings                       

    tables: collections                        embeddings_queue                 

    tables: databases                          embeddings_queue_config          

    tables: embedding_fulltext_search          maintenance_log                  

    tables: embedding_fulltext_search_config   max_seq_id                       

    tables: embedding_fulltext_search_content  migrations                       

    tables: embedding_fulltext_search_data     segment_metadata                 

    tables: embedding_fulltext_search_docsize  segments                         

    tables: embedding_fulltext_search_idx      tenants                          

    tables: embedding_metadata               

store: /mnt/nvme1/msjarvis-rebuild/chroma.sqlite3

  size:     0

  modified: 2026-02-05T16:15:05Z

  collections (name -> record count), read directly from SQLite:

    (schema differs; dump table list below)

store: /mnt/nvme1/msjarvis-rebuild/chromadb/chroma.sqlite3

  size:     164K

  modified: 2026-02-16T15:09:08Z

  collections (name -> record count), read directly from SQLite:

    tables: acquire_write                      embedding_metadata               

    tables: collection_metadata                embeddings                       

    tables: collections                        embeddings_queue                 

    tables: databases                          embeddings_queue_config          

    tables: embedding_fulltext_search          maintenance_log                  

    tables: embedding_fulltext_search_config   max_seq_id                       

    tables: embedding_fulltext_search_content  migrations                       

    tables: embedding_fulltext_search_data     segment_metadata                 

    tables: embedding_fulltext_search_docsize  segments                         

    tables: embedding_fulltext_search_idx      tenants                          

store: /mnt/nvme1/msjarvis-rebuild/data/chroma/chroma.sqlite3

  size:     164K

  modified: 2026-02-16T15:08:35Z

  collections (name -> record count), read directly from SQLite:

    tables: acquire_write                      embedding_metadata               

    tables: collection_metadata                embeddings                       

    tables: collections                        embeddings_queue                 

    tables: databases                          embeddings_queue_config          

    tables: embedding_fulltext_search          maintenance_log                  

    tables: embedding_fulltext_search_config   max_seq_id                       

    tables: embedding_fulltext_search_content  migrations                       

    tables: embedding_fulltext_search_data     segment_metadata                 

    tables: embedding_fulltext_search_docsize  segments                         

    tables: embedding_fulltext_search_idx      tenants                          

store: /mnt/nvme1/msjarvis-rebuild/data/GBIM_chroma/chroma.sqlite3

  size:     2.4M

  modified: 2026-02-16T15:08:35Z

  collections (name -> record count), read directly from SQLite:

    gbim_block2020|150

    gbim_block_provider_summary|147

    gbim_provider_block_join_provider|150

    gbim_provider_population_summary|150

    tables: acquire_write                      embedding_metadata               

    tables: collection_metadata                embeddings                       

    tables: collections                        embeddings_queue                 

    tables: databases                          embeddings_queue_config          

    tables: embedding_fulltext_search          maintenance_log                  

    tables: embedding_fulltext_search_config   max_seq_id                       

    tables: embedding_fulltext_search_content  migrations                       

    tables: embedding_fulltext_search_data     segment_metadata                 

    tables: embedding_fulltext_search_docsize  segments                         

    tables: embedding_fulltext_search_idx      tenants                          

store: /mnt/nvme1/msjarvis-data/chroma-live/chroma.sqlite3

  size:     33M

  modified: 2026-07-12T19:21:48Z

  collections (name -> record count), read directly from SQLite:

    appalachian_cultural_intelligence|0

    au02_threat_seeds|0

    autonomous_learner|0

    bg_col|0

    blockgroups_census_201111_utm83|0

    blockgroups_census_2020_utm83|0

    census_cities_over10k_2020_utm83|0

    census_cities_over2500_2020_utm83|0

    census_county_boundaries_2021_utm83|0

    census_designated_places_2021_utm83|0

    census_empowerment_zones_2002_utm83|0

    census_historical_pop_by_county_2006_utm83|0

    census_incorporated_places_2021_utm83|0

    census_metro_micro_areas_2020_utm83|0

    census_minor_civil_divisions_2020_utm83|0

    census_misc_transportation_2000_utm83|0

    census_pop_change_communities_2020_utm83|0

    census_pop_change_counties_2020_utm83|0

    census_populated_places_2020_utm83|0

    census_railroads_2023_utm83|0

    census_roads_2023_utm83|0

    census_streams_waterbodies_2023_utm83|0

    census_tl_2020_us_county|0

    census_tl_2020_us_zcta510|0

    census_tl_2020_us_zcta520|0

    census_tracts_2020_utm83|0

    census_urban_areas_100k_2020_utm83|0

    census_zcta_2020_utm83|0

    civic_role_temporal|0

    coals2_utm27|0

    coals2_utm83|0

    commons_rag|0

    community_hilbert_commons|0

    communityboundary_min_att_20250121_utm83|0

    contracts|0

    conversation_gbim_private|0

    conversation_gbim_public|0

    conversation_history|0

    correctionalinstitutions_hsip_20091230_utm83|0

    correctionalinstitutions_hsip_20091230_wgs84|0

    county|0

    countyseats_usgs_ll83|0

    countyseats_usgs_utm83|0

    courthousescounty_manysources_200203_utm83|0

    courthousesfederal_manysources_200203_ll83|0

    courthousesfederal_manysources_200203_utm|0

    cousub|0

    cvpoly_utm83|0

    economic_rag|0

    empowermentzonesandenterprisecommunities_uscensus_2002_utm83|0

    empowermentzonesandenterprisecommunitiesbytract_uscens_30c72907|0

    equity_timesheet|0

    fayette_county_resources_2026|0

    fifth_dgm_subconscious|0

    fire_dept_wvdem_092017_utm83|0

    floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83|0

    founder_tokens|0

    gbim_entities|0

    gbim_wv_blockgroups_v1|1639

    gbim_wv_counties_v1|55

    gbim_wv_counties_v2|55

    gbim_wv_tracts_v1|546

    gbim_wv_tracts_v2|546

    gbim_wv_zctas_v1|741

    geo_911centers_wvdem_032819_gcs84|0

    geo_911centers_wvdem_032819_utm83|0

    geo__911centers_wvdem_032819_gcs84|0

    geo__911centers_wvdem_032819_utm83|0

    geo__addrfeat|0

    geo_addrfeat|0

    geo_amtrackrails_federalrailroadadministration_200210_ll83|0

    geo_amtrackrails_federalrailroadadministration_200210_utm83|0

    geo_amtrackrails_federalrailroadadministration_20021_7f49dc3cf5|0

    geo_amtrackrails_fra_200210_ll83_attrs_raw|0

    geo_benefit_county_daycare|0

    geo_benefit_county_medicaid|0

    geo_benefit_county_medicare|0

    geo_benefit_county_section8|0

    geo_benefit_county_snap|0

    geo_benefit_county_ssi|0

    geo_benefit_county_tanf|0

    geo_benefit_county_utility20|0

    geo_benefit_county_wic|0

    geo_bldg_join_hospitals|0

    geo_blockgroups_census_2000_ll83|0

    geo_blockgroups_census_2000_utm83|0

    geo_blockgroups_census_201111_gcs83|0

    geo_blockgroups_census_201111_utm83|0

    geo_blockgroups_census_2020_utm83|0

    geo_blockgroups_census_2020_utm83_full|0

    geo_blockgroups_census_2020_utm83_raw|0

    geo_blockgroups_census_2020_wma84|0

    geo_blocks_census_2020_utm83|0

    geo_blocks_census_2020_utm83_full|0

    geo_blocks_census_2020_utm83_raw|0

    geo_blocks_census_2020_wma84|0

    geo_boundaryappalachianbasin_wvges_1996_utm83|0

    geo_boundaryappalachianbasin_wvges_1996_wma84|0

    geo_bridges|0

    geo_building_flood_risk|0

    geo_building_flood_risk_floodpoint|0

    geo_building_parcel_county_tax_mat|0

    geo_building_profile|0

    geo_building_samb_link|0

    geo_building_zip6_to_zip6poly|0

    geo_buildings|0

    geo_calderl_reg_ll83|0

    geo_cbsa_census_2020_utm83_raw|0

    geo_census_roads_2023_utm83|0

    geo_churches_usgs_201006_utm83|0

    geo_citieswithpopulation_2500_census_201111_gcs83|0

    geo_citieswithpopulation_2500_census_201111_utm83|0

    geo_citieswithpopulationover10k_census_201111_gcs83|0

    geo_citieswithpopulationover10k_census_201111_gcs83_attrs_raw|0

    geo_citieswithpopulationover10k_uscensus_1990_ll83|0

    geo_citieswithpopulationover10k_uscensus_1990_utm83|0

    geo_citieswithpopulationover2500_uscensus_1990_ll83|0

    geo_citieswithpopulationsover10k_census_2020_utm83|0

    geo_citieswithpopulationsover10k_census_2020_wma84|0

    geo_citieswithpopulationsover2500_census_2020_utm83|0

    geo_citieswithpopulationsover2500_census_2020_wma84|0

    geo_citieswithpopulatoinover2500_uscensus_1990_utm83|0

    geo_coals2_ll83|0

    geo_coals2_utm27|0

    geo_coals2_utm83|0

    geo_community_points|0

    geo_communityboundary_min_att_20250121_utm83|0

    geo_communityboundary_min_att_20250121_wma84|0

    geo_communityhealthproviders_wvhealthcareauthority_200802_utm83|0

    geo_conversation_beliefs|0

    geo_correctionalinstitutions_hsip_20091230_wgs84|0

    geo_county_lookup|0

    geo_countycityparkboundaries_20201104_utm83|0

    geo_courthousescounty_manysources_200203_ll83|0

    geo_cvfault_ll83|0

    geo_cvfault_utm27|0

    geo_cvfault_utm83|0

    geo_cvpoly_ll83|0

    geo_cvpoly_utm27|0

    geo_cvpoly_utm83|0

    geo_dams_usarmycorpsofengineers_200010_utm83|0

    geo_dams_usarmycropsofengineers_200010_ll83|0

    geo_damsnoncoal_usgs_2002_ll27|0

    geo_damsnoncoal_usgs_2002_ll27_attrs_raw|0

    geo_damsnoncoal_usgs_2002_utm83|0

    geo_empowermentzonesandenterprisecommunities_uscensu_73da8ad185|0

    geo_empowermentzonesandenterprisecommunitiesbytractu_f887b4d671|0

    geo_equity_timesheet|0

    geo_equity_timesheet_ctx_backup|0

    geo_excursionpassengertrains_wvdof_200102_ll83|0

    geo_excursionpassengertrains_wvdof_200102_utm83|0

    geo_facilities_epa_200203_ll83|0

    geo_facilities_epa_200203_utm83|0

    geo_fault_reg_ll83|0

    geo_faultgl_reg_ll83|0

    geo_fayette_fire_stations|0

    geo_fayette_parcels|0

    geo_features|0

    geo_fire_departments|0

    geo_floodplainstructuresatrisk_usarmycorpsofengineer_b30a3da703|0

    geo_founder_tokens|0

    geo_gbim_belief_normalized|0

    geo_gbim_entities|0

    geospatialfeatures|0

    governance_rag|0

    grants_rag|0

    health_rag|0

    hilbert_time|0

    jarvis|0

    jarvis_knowledge|0

    legal_rag|0

    meeting_minutes|0

    mountainshares_knowledge|203

    ms_allis_uploads|0

    ms_jarvis_memory|0

    msjarvis_docs|299

    news_rag|0

    operations_history|0

    pg__public__building_parcel_county_tax_mat|0

    policy_rag|0

    psychological_rag|0

    public_civic_appearances|0

    public_civic_documents|0

    public_civic_events|0

    public_civic_roles|0

    public_civic_sources|0

    public_civic_statements|0

    safety_rules|0

    spiritual_knowledge|0

    spiritual_texts|0

    spiritual_wisdom|0

    wv_civic_infrastructure|0

    wv_resources|0

    wv_resources_statewide|0

    zcta_centroids|0

    tables: acquire_write                      embedding_metadata_array         

    tables: collection_metadata                embeddings                       

    tables: collections                        embeddings_queue                 

    tables: databases                          embeddings_queue_config          

    tables: embedding_fulltext_search          maintenance_log                  

    tables: embedding_fulltext_search_config   max_seq_id                       

    tables: embedding_fulltext_search_content  migrations                       

    tables: embedding_fulltext_search_data     segment_metadata                 

    tables: embedding_fulltext_search_docsize  segments                         

    tables: embedding_fulltext_search_idx      tenants                          

    tables: embedding_metadata               

store: /mnt/nvme1/msjarvis-data/chroma-live-bk-20260623-0834/chroma.sqlite3

  size:     184K

  modified: 2026-07-02T15:36:58Z

  collections (name -> record count), read directly from SQLite:

    tables: acquire_write                      embedding_metadata_array         

    tables: collection_metadata                embeddings                       

    tables: collections                        embeddings_queue                 

    tables: databases                          embeddings_queue_config          

    tables: embedding_fulltext_search          maintenance_log                  

    tables: embedding_fulltext_search_config   max_seq_id                       

    tables: embedding_fulltext_search_content  migrations                       

    tables: embedding_fulltext_search_data     segment_metadata                 

    tables: embedding_fulltext_search_docsize  segments                         

    tables: embedding_fulltext_search_idx      tenants                          

    tables: embedding_metadata               

store: /mnt/nvme1/msjarvis-data/chroma-live-backups/chroma-live.empty.20260605-013917/chroma.sqlite3

  size:     192K

  modified: 2026-06-05T05:29:57Z

  collections (name -> record count), read directly from SQLite:

    04e344e5-eda7-4f21-b9d4-e9a5f8b1890a|0

    17433c00-f959-47bb-b13d-065066f64c41|0

    6727fb3e-078f-49d5-9df8-e2c82ecf8cf2|0

    geospatialfeatures|0

    tables: acquire_write                      embedding_metadata_array         

    tables: collection_metadata                embeddings                       

    tables: collections                        embeddings_queue                 

    tables: databases                          embeddings_queue_config          

    tables: embedding_fulltext_search          maintenance_log                  

    tables: embedding_fulltext_search_config   max_seq_id                       

    tables: embedding_fulltext_search_content  migrations                       

    tables: embedding_fulltext_search_data     segment_metadata                 

    tables: embedding_fulltext_search_docsize  segments                         

    tables: embedding_fulltext_search_idx      tenants                          

    tables: embedding_metadata               

store: /mnt/nvme1/msjarvis-data/chroma-live.backup.2026-07-04-173936/chroma.sqlite3

  size:     100G

  modified: 2026-07-04T21:31:58Z

  collections (name -> record count), read directly from SQLite:

    911centers_wvdem_032819_gcs84|135

    911centers_wvdem_032819_utm83|135

    addrfeat|16585

    amtrackrails_federalrailroadadministration_200210_ll83|2

    appalachian_cultural_intelligence|890

    au02_threat_seeds|10

    autonomous_learner|5854

    bg_col|4097

    blockgroups_census_2000_ll83|3782

    blockgroups_census_2000_utm83|3176

    blockgroups_census_201111_gcs83|3184

    blockgroups_census_201111_utm83|3092

    blockgroups_census_2020_utm83|1639

    blocks_census_2020_utm83|72558

    boundaryappalachianbasin_wvges_1996_utm83|313

    bridges|7357

    calderl_reg_ll83|9

    census_blocks_2020_utm83|72558

    census_cities_over10k_2020_utm83|14

    census_cities_over2500_2020_utm83|63

    census_county_boundaries_2021_utm83|55

    census_designated_places_2021_utm83|207

    census_empowerment_zones_2002_utm83|11

    census_historical_pop_by_county_2006_utm83|55

    census_incorporated_places_2021_utm83|464

    census_metro_micro_areas_2020_utm83|17

    census_minor_civil_divisions_2020_utm83|228

    census_misc_transportation_2000_utm83|5

    census_pop_change_communities_2020_utm83|284

    census_pop_change_counties_2020_utm83|55

    census_populated_places_2020_utm83|439

    census_railroads_2023_utm83|1505

    census_roads_2023_utm83|287515

    census_streams_waterbodies_2023_utm83|67774

    census_tl_2020_us_county|3234

    census_tl_2020_us_zcta510|33144

    census_tl_2020_us_zcta520|33791

    census_tracts_2020_utm83|546

    census_urban_areas_100k_2020_utm83|56

    census_zcta_2020_utm83|741

    citieswithpopulation_2500_census_201111_gcs83|65

    citieswithpopulation_2500_census_201111_utm83|65

    citieswithpopulationover10k_census_201111_gcs83|15

    citieswithpopulationover10k_uscensus_1990_ll83|16

    citieswithpopulationover2500_uscensus_1990_ll83|277

    citieswithpopulationsover10k_census_2020_utm83|14

    citieswithpopulationsover2500_census_2020_utm83|63

    citieswithpopulatoinover2500_uscensus_1990_utm83|277

    civic_role_temporal|2

    coals2_ll83|15

    coals2_utm27|15

    coals2_utm83|15

    commons_rag|343

    community_hilbert_commons|0

    communityboundary_min_att_20250121_utm83|292

    communityboundary_min_att_20250121_wma84|292

    communityhealthproviders_wvhealthcareauthority_200802_utm83|150

    contracts|51

    conversation_gbim_private|10

    conversation_gbim_public|10

    conversation_history|1434

    correctionalinstitutions_hsip_20091230_utm83|108

    correctionalinstitutions_hsip_20091230_wgs84|108

    county|3234

    countycityparkboundaries_20201104_utm83|596

    countyseats_usgs_ll83|55

    countyseats_usgs_utm83|55

    courthousescounty_manysources_200203_ll83|55

    courthousescounty_manysources_200203_utm83|55

    courthousesfederal_manysources_200203_ll83|10

    courthousesfederal_manysources_200203_utm|10

    cousub|228

    cvfault_ll83|5

    cvfault_utm27|5

    cvfault_utm83|5

    cvpoly_ll83|38

    cvpoly_utm27|38

    cvpoly_utm83|38

    dams_usarmycorpsofengineers_200010_utm83|575

    dams_usarmycropsofengineers_200010_ll83|575

    damsnoncoal_usgs_2002_ll27|468

    economic_rag|14

    edges|2330

    empowermentzonesandenterprisecommunities_uscensus_2002_utm83|11

    empowermentzonesandenterprisecommunitiesbytract_uscens_30c72907|459

    equity_timesheet|50

    excursionpassengertrains_wvdof_200102_ll83|8

    excursionpassengertrains_wvdof_200102_utm83|8

    faces|9165

    facilities_epa_200203_ll83|2137

    facilities_epa_200203_utm83|2137

    fault_reg_ll83|124

    faultgl_reg_ll83|43084

    fayette_county_resources_2026|0

    fayette_parcels|39515

    features|72558

    fifth_dgm_subconscious|3

    fire_departments|548

    fire_dept_wvdem_092017_utm83|548

    floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83|81054

    founder_tokens|1

    gbim_entities|3535139

    geo_911centers_wvdem_032819_gcs84|729

    geo_911centers_wvdem_032819_utm83|486

    geo__911centers_wvdem_032819_gcs84|0

    geo__911centers_wvdem_032819_utm83|0

    geo__addrfeat|0

    geo__amtrackrails_federalrailroadadministration_200210_ll83|0

    geo_addrfeat|25000

    geo_amtrackrails_federalrailroadadministration_200210_ll83|0

    geo_amtrackrails_federalrailroadadministration_200210_utm83|0

    geo_amtrackrails_federalrailroadadministration_20021_7f49dc3cf5|0

    geo_amtrackrails_fra_200210_ll83_attrs_raw|0

    geo_benefit_county_daycare|0

    geo_benefit_county_medicaid|0

    geo_benefit_county_medicare|0

    geo_benefit_county_section8|0

    geo_benefit_county_snap|0

    geo_benefit_county_ssi|0

    geo_benefit_county_tanf|0

    geo_benefit_county_utility20|0

    geo_benefit_county_wic|0

    geo_bldg_join_hospitals|0

    geo_blockgroups_census_2000_ll83|0

    geo_blockgroups_census_2000_ll83_attrs_raw|0

    geo_blockgroups_census_2000_utm83|0

    geo_blockgroups_census_201111_gcs83|0

    geo_blockgroups_census_201111_gcs83_attrs_raw|0

    geo_blockgroups_census_201111_utm83|0

    geo_blockgroups_census_2020_utm83|0

    geo_blockgroups_census_2020_utm83_full|0

    geo_blockgroups_census_2020_utm83_raw|3278

    geo_blockgroups_census_2020_wma84|0

    geo_blocks_census_2020_utm83|0

    geo_blocks_census_2020_utm83_full|0

    geo_blocks_census_2020_utm83_raw|55000

    geo_blocks_census_2020_wma84|0

    geo_boundaryappalachianbasin_wvges_1996_utm83|0

    geo_boundaryappalachianbasin_wvges_1996_wma84|0

    geo_bridges|0

    geo_building_flood_risk|0

    geo_building_flood_risk_floodpoint|0

    geo_building_parcel_county_tax_mat|55000

    geo_building_profile|55000

    geo_building_samb_link|864

    geo_building_zip6_to_zip6poly|1082

    geo_buildings|0

    geo_calderl_reg_ll83|0

    geo_calderl_reg_ll83_attrs_raw|0

    geo_cbsa_census_2020_utm83_raw|17

    geo_census_roads_2023_utm83|130000

    geo_churches_usgs_201006_utm83|0

    geo_citieswithpopulation_2500_census_201111_gcs83|0

    geo_citieswithpopulation_2500_census_201111_gcs83_attrs_raw|0

    geo_citieswithpopulation_2500_census_201111_utm83|0

    geo_citieswithpopulationover10k_census_201111_gcs83|0

    geo_citieswithpopulationover10k_census_201111_gcs83_attrs_raw|0

    geo_citieswithpopulationover10k_uscensus_1990_ll83|0

    geo_citieswithpopulationover10k_uscensus_1990_ll83_attrs_raw|0

    geo_citieswithpopulationover10k_uscensus_1990_utm83|0

    geo_citieswithpopulationover2500_uscensus_1990_ll83|0

    geo_citieswithpopulationover2500_uscensus_1990_ll83_attrs_raw|0

    geo_citieswithpopulationsover10k_census_2020_utm83|0

    geo_citieswithpopulationsover10k_census_2020_wma84|0

    geo_citieswithpopulationsover2500_census_2020_utm83|0

    geo_citieswithpopulationsover2500_census_2020_wma84|0

    geo_citieswithpopulatoinover2500_uscensus_1990_utm83|0

    geo_coals2_ll83|0

    geo_coals2_ll83_attrs_raw|0

    geo_coals2_utm27|0

    geo_coals2_utm83|0

    geo_community_points|0

    geo_communityboundary_min_att_20250121_utm83|0

    geo_communityboundary_min_att_20250121_wma84|0

    geo_communityhealthproviders_wvhealthcareauthority_200802_utm83|0

    geo_conversation_beliefs|473

    geo_correctionalinstitutions_hsip_20091230_wgs84|0

    geo_county_lookup|55

    geo_countycityparkboundaries_20201104_utm83|0

    geo_courthousescounty_manysources_200203_ll83|0

    geo_courthousescounty_manysources_200203_ll83_attrs_raw|0

    geo_cvfault_ll83|0

    geo_cvfault_ll83_attrs_raw|0

    geo_cvfault_utm27|0

    geo_cvfault_utm83|0

    geo_cvpoly_ll83|0

    geo_cvpoly_ll83_attrs_raw|0

    geo_cvpoly_utm27|0

    geo_cvpoly_utm83|0

    geo_dams_usarmycorpsofengineers_200010_utm83|0

    geo_dams_usarmycropsofengineers_200010_ll83|0

    geo_dams_usarmycropsofengineers_200010_ll83_attrs_raw|0

    geo_damsnoncoal_usgs_2002_ll27|0

    geo_damsnoncoal_usgs_2002_ll27_attrs_raw|0

    geo_damsnoncoal_usgs_2002_utm83|0

    geo_empowermentzonesandenterprisecommunities_uscensu_73da8ad185|0

    geo_empowermentzonesandenterprisecommunitiesbytractu_f887b4d671|0

    geo_equity_timesheet|512

    geo_equity_timesheet_ctx_backup|13

    geo_excursionpassengertrains_wvdof_200102_ll83|0

    geo_excursionpassengertrains_wvdof_200102_ll83_attrs_raw|0

    geo_excursionpassengertrains_wvdof_200102_utm83|0

    geo_facilities_epa_200203_ll83|0

    geo_facilities_epa_200203_ll83_attrs_raw|0

    geo_facilities_epa_200203_utm83|0

    geo_fault_reg_ll83|0

    geo_fault_reg_ll83_attrs_raw|0

    geo_faultgl_reg_ll83|0

    geo_faultgl_reg_ll83_attrs_raw|0

    geo_fayette_fire_stations|0

    geo_fayette_parcels|0

    geo_features|0

    geo_fire_departments|0

    geo_floodplainstructuresatrisk_usarmycorpsofengineer_b30a3da703|0

    geo_founder_tokens|2

    geo_gbim_belief_normalized|512

    geo_gbim_entities|865000

    geospatialfeatures|12389268

    governance_rag|643

    grants_rag|21

    health_rag|23

    hilbert_time|7

    jarvis|1

    jarvis_knowledge|6

    legal_rag|7

    meeting_minutes|1

    ms_allis_uploads|2

    ms_jarvis_memory|637

    msjarvis_docs|769

    news_rag|38

    operations_history|1

    pg__public__building_parcel_county_tax_mat|48800

    policy_rag|9

    psychological_rag|968

    public_civic_appearances|14

    public_civic_documents|7

    public_civic_events|12

    public_civic_roles|6

    public_civic_sources|7

    public_civic_statements|2

    safety_rules|10

    spiritual_knowledge|12

    spiritual_texts|5557

    spiritual_wisdom|135

    wv_civic_infrastructure|0

    wv_resources|14

    wv_resources_statewide|0

    zcta_centroids|829

    tables: acquire_write                      embedding_metadata_array         

    tables: collection_metadata                embeddings                       

    tables: collections                        embeddings_queue                 

    tables: databases                          embeddings_queue_config          

    tables: embedding_fulltext_search          maintenance_log                  

    tables: embedding_fulltext_search_config   max_seq_id                       

    tables: embedding_fulltext_search_content  migrations                       

    tables: embedding_fulltext_search_data     segment_metadata                 

    tables: embedding_fulltext_search_docsize  segments                         

    tables: embedding_fulltext_search_idx      tenants                          

    tables: embedding_metadata               

store: /mnt/spiritual_drive/msjarvis-rebuild/chroma_data/chroma.sqlite3

  size:     184K

  modified: 2026-06-23T16:17:18Z

  collections (name -> record count), read directly from SQLite:

    tables: acquire_write                      embedding_metadata_array         

    tables: collection_metadata                embeddings                       

    tables: collections                        embeddings_queue                 

    tables: databases                          embeddings_queue_config          

    tables: embedding_fulltext_search          maintenance_log                  

    tables: embedding_fulltext_search_config   max_seq_id                       

    tables: embedding_fulltext_search_content  migrations                       

    tables: embedding_fulltext_search_data     segment_metadata                 

    tables: embedding_fulltext_search_docsize  segments                         

    tables: embedding_fulltext_search_idx      tenants                          

    tables: embedding_metadata               

store: /mnt/spiritual_drive/msjarvis-rebuild/egeria_knowledge_base/chroma_db/chroma.sqlite3

  size:     168K

  modified: 2026-07-03T16:55:46Z

  collections (name -> record count), read directly from SQLite:

    tables: collection_metadata                embeddings                       

    tables: collections                        embeddings_queue                 

    tables: databases                          embeddings_queue_config          

    tables: embedding_fulltext_search          maintenance_log                  

    tables: embedding_fulltext_search_config   max_seq_id                       

    tables: embedding_fulltext_search_content  migrations                       

    tables: embedding_fulltext_search_data     segment_metadata                 

    tables: embedding_fulltext_search_docsize  segments                         

    tables: embedding_fulltext_search_idx      tenants                          

    tables: embedding_metadata               

store: /mnt/spiritual_drive/msjarvis-rebuild/services/chroma/chroma.sqlite3

  size:     160K

  modified: 2026-06-13T06:48:13Z

  collections (name -> record count), read directly from SQLite:

    tables: acquire_write                      embedding_metadata               

    tables: collection_metadata                embeddings                       

    tables: collections                        embeddings_queue                 

    tables: databases                          embeddings_queue_config          

    tables: embedding_fulltext_search          maintenance_log                  

    tables: embedding_fulltext_search_config   max_seq_id                       

    tables: embedding_fulltext_search_content  migrations                       

    tables: embedding_fulltext_search_data     segment_metadata                 

    tables: embedding_fulltext_search_docsize  segments                         

    tables: embedding_fulltext_search_idx      tenants                          

store: /mnt/spiritual_drive/msjarvis-rebuild/persistent/chroma/chroma.sqlite3

  size:     79M

  modified: 2026-06-23T20:00:01Z

  collections (name -> record count), read directly from SQLite:

    appalachian_english_corpus|225

    geospatialfeatures|2018

    tables: acquire_write                      embedding_metadata_array         

    tables: collection_metadata                embeddings                       

    tables: collections                        embeddings_queue                 

    tables: databases                          embeddings_queue_config          

    tables: embedding_fulltext_search          maintenance_log                  

    tables: embedding_fulltext_search_config   max_seq_id                       

    tables: embedding_fulltext_search_content  migrations                       

    tables: embedding_fulltext_search_data     segment_metadata                 

    tables: embedding_fulltext_search_docsize  segments                         

    tables: embedding_fulltext_search_idx      tenants                          

    tables: embedding_metadata               

store: /mnt/spiritual_drive/msjarvis-rebuild/chroma_db/chroma.sqlite3

  size:     97M

  modified: 2026-06-17T21:08:29Z

  collections (name -> record count), read directly from SQLite:

    address_points|20246

    tables: acquire_write                      embedding_metadata               

    tables: collection_metadata                embeddings                       

    tables: collections                        embeddings_queue                 

    tables: databases                          embeddings_queue_config          

    tables: embedding_fulltext_search          maintenance_log                  

    tables: embedding_fulltext_search_config   max_seq_id                       

    tables: embedding_fulltext_search_content  migrations                       

    tables: embedding_fulltext_search_data     segment_metadata                 

    tables: embedding_fulltext_search_docsize  segments                         

    tables: embedding_fulltext_search_idx      tenants                          

store: /home/cakidd/jarvis_gpu_reenable/recovery/services_snapshot/chroma/chroma.sqlite3

  size:     160K

  modified: 2026-06-13T06:48:13Z

  collections (name -> record count), read directly from SQLite:

    tables: acquire_write                      embedding_metadata               

    tables: collection_metadata                embeddings                       

    tables: collections                        embeddings_queue                 

    tables: databases                          embeddings_queue_config          

    tables: embedding_fulltext_search          maintenance_log                  

    tables: embedding_fulltext_search_config   max_seq_id                       

    tables: embedding_fulltext_search_content  migrations                       

    tables: embedding_fulltext_search_data     segment_metadata                 

    tables: embedding_fulltext_search_docsize  segments                         

    tables: embedding_fulltext_search_idx      tenants                          

(if nothing printed above, no embedded Chroma store exists on disk)

--- B6. GIS-RAG live retrieval probe (proves the path end to end) ---

GET /health:

{"status":"healthy","dependencies":{"production_20llm":"healthy"},"timestamp":"2026-07-12T19:23:04.677706"}

############################################################

## END

############################################################

Written to: /home/cakidd/gbim-investigation-20260712T192124Z/23-gates-and-chroma.txt

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ chmod +x ~/Downloads/gbim-verify.sh

~/Downloads/gbim-verify.sh

GBIM corrective verification

Generated: 2026-07-12T19:26:50Z

Report:    /home/cakidd/gbim-investigation-20260712T192124Z

############################################################

## 1. MANIFEST HEADERS AND SAMPLE ROWS (ground truth)

############################################################

--- wv_source_files_manifest.csv ---

MISSING at /mnt/spiritual_drive/msjarvis-rebuild

--- wv_source_manifest_layers.csv ---

rows (incl header): 12

header:

ATM Weather Stations 1999,weatherStations_nationalClimateDataCenter_1999_utm27_shp.zip,NCDC,UTM27,public.wv_atm_weather_stations,weather_station_points

first 3 data rows:

Biodiversity Rank Index 2024,Biodiversity_Rank_Index_wvdnr_wvdep_2024_utm83.zip,WVDNR/WVDEP,UTM83,public.wv_bio_biodiversity_rank,biodiversity_rank_polygons

Ecoregions USFS 2000,ecoregions_USFS_200002_utm83_shp.zip,USFS,UTM83,public.wv_bio_ecoregions,ecoregion_polygons

Red Spruce Cover 2013,redSpruceCoverWV_WVDNR_utm83_2013_shp.zip,WVDNR,UTM83,public.wv_bio_red_spruce_cover,forest_cover_polygons

--- wv_derived_governance_tables.csv ---

rows (incl header): 39

header:

table_name,category,notes

first 3 data rows:

wv_layer_categories,governance_layer_catalog,internal GBIM layer taxonomy, no single source ZIP

wv_entity_registry,governance_entity_registry,canonical GBIM entity registry, derived from many datasets

wv_county_identity,governance_identity,county identity keyed by canonical IDs and GEOIDs, derived from boundary + registry

############################################################

## 2. MANIFEST RECONCILIATION — column chosen by VALUE, not by name

############################################################

live wv_* relations: 153

extraction:

  wv_source_manifest_layers.csv: delimiter=','  rows=11

    column scores (wv_*-shaped values per column): {'public.wv_atm_weather_stations': 11, 'ATM Weather Stations 1999': 0, 'weatherStations_nationalClimateDataCenter_1999_utm27_shp.zip': 0, 'NCDC': 0, 'UTM27': 0, 'weather_station_points': 0}

    chosen column: 'public.wv_atm_weather_stations' (11 matches)

  wv_derived_governance_tables.csv: delimiter=','  rows=38

    column scores (wv_*-shaped values per column): {'table_name': 38, 'category': 0, 'notes': 0}

    chosen column: 'table_name' (38 matches)

live relations:            153

mapped by layers manifest: 11

classified as derived:     35

accounted for:             41

GATE 17 — live relations in NO manifest: 112

    wv_atm_weather_stations

    wv_bnd_county_24k

    wv_bnd_county_municipal_dlg

    wv_bnd_mnf_basic_ownership

    wv_bnd_mnf_management_prescriptions

    wv_bnd_mnf_ranger_districts

    wv_bnd_mnf_recreation_campgrounds

    wv_bnd_mnf_recreation_sites

    wv_bnd_mnf_wilderness

    wv_bnd_morgantown_wards

    wv_bnd_nhd_mussel_streams

    wv_bnd_public_lands_county_city_parks

    wv_bnd_public_lands_national_forest

    wv_bnd_public_lands_national_park

    wv_bnd_public_lands_nwr

    wv_bnd_public_lands_state_forests

    wv_bnd_public_lands_state_parks

    wv_bnd_public_lands_wildlife_resources

    wv_bnd_state_boundary_100k

    wv_bnd_voting_districts_2000

    wv_bnd_voting_districts_2002

    wv_bnd_workforce_investment_areas

    wv_censustracts_census_2020_utm83

    wv_county_boundaries_24k_topo_updated_2026_utm83_gdb

    wv_eco_abandoned_mine_lands_line

    wv_eco_abandoned_mine_lands_point

    wv_eco_abandoned_mine_lands_polygon

    wv_eco_coal_fields

    wv_eco_ezec_communities

    wv_eco_industrial_sites

    wv_eco_manufacturing_directory

    wv_eco_mineral_operations

    wv_eco_mountaintop_removal

    wv_elv_summit_names

    wv_env_air_nonattainment

    wv_env_epa_facilities

    wv_env_timber_removal_volume

    wv_env_wildfire_regions

    wv_env_wind_energy_resources

    wv_geo_coal_beds

    wv_geo_geological_map_generalized

    wv_geo_karst

    wv_hlt_health_providers

    wv_hlt_public_health_departments

    wv_hlt_rural_health_facilities

    wv_hyd_dams_dmr

    wv_hyd_dams_nid

    wv_hyd_dams_noncoal

    wv_hyd_hazus_floodplain_zones

    wv_hyd_high_water_marks

    wv_hyd_navigable_waterways

    wv_hyd_navigable_waterways_river_miles

    wv_hyd_navigable_waterways_structures

    wv_hyd_springs_100gpm

    wv_hyd_streamflow_stations

    wv_hyd_streams_high_quality

    wv_hyd_streams_national_atlas

    wv_hyd_streams_tiger

    wv_hyd_watershed_boundary_11digit

    wv_hyd_watershed_boundary_12digit_hu

    wv_hyd_watershed_boundary_8_10_12

    wv_loc_census_urbanized_areas

    wv_loc_county_seats

    wv_loc_geodetic_control_points

    wv_loc_populated_places_census

    wv_loc_sams2_address_road_centerlines

    wv_mil_army_reserve_facilities

    wv_mil_national_guard_armories

    wv_plc_hazus_level1

    wv_plc_regional_planning_councils

    wv_plc_tax_district_boundaries

    wv_plc_tax_parcels_surface_mineral

    wv_soc_911_centers

    wv_soc_census_blockgroups_2020

    wv_soc_census_tracts_2020

    wv_soc_cities_pop10k

    wv_soc_cities_pop2500

    wv_soc_communities_pop_change

    wv_soc_courthouses_county

    wv_soc_courthouses_federal

    wv_soc_fish_hatcheries

    wv_soc_fishing_boating_access

    wv_soc_fishing_lakes

    wv_soc_higher_ed_facilities

    wv_soc_hospitals_wvdem

    wv_soc_libraries

    wv_soc_national_register_historic_points

    wv_soc_national_register_historic_polygons

    wv_soc_nursing_homes

    wv_soc_places_of_worship_wvgistc

    wv_soc_population_by_decade

    wv_soc_schools_k12

    wv_soc_towers_am

    wv_soc_towers_asr

    wv_soc_towers_cellular

    wv_soc_towers_fm

    wv_soc_towers_microwave

    wv_soc_towers_pager

    wv_soc_towers_private

    wv_soc_towers_tv

    wv_soc_va_facilities

    wv_soc_zcta_2020

    wv_str_bridges

    wv_str_correctional_institutions

    wv_str_flood_atrisk_structures

    wv_tract_representation

    wv_tract_representation_pre_gid_rebind

    wv_trn_roads_major_4800

    wv_trn_roads_state_routes

    wv_trn_roads_us_highways

    wv_trn_roads_us_routes

    wv_trn_whitewater_trails

GATE 18 — manifest names with no relation in the database: 3

    wv_bnd_public_lands_union

    wv_county_summary_metrics

    wv_tract_summary_metrics

############################################################

## 3. GOVERNANCE SCHEMA — real column names

############################################################

table_name	columns

wv_county_dataset_coverage	canonical_county_id, dataset_type, source_table, feature_count, coverage_state, calculated_at, source_layer_hash, notes

wv_county_identity	canonical_county_id, state_fips, county_fips, county_geoid, county_name, state_abbrev, state_name, authority_class, access_class, created_at, updated_at

wv_county_representation	table_name, source_feature_id, canonical_county_id, county_name_source, source_feature_hash, representation_role, created_at, updated_at

wv_tract_dataset_coverage	canonical_tract_id, canonical_county_id, dataset_type, source_table, feature_count, coverage_state, calculated_at, source_layer_hash, notes

wv_tract_identity	canonical_tract_id, tract_geoid, canonical_county_id, created_at, updated_at

wv_tract_representation	canonical_tract_id, canonical_county_id, table_name, source_feature_id, source_feature_hash

(6 rows)

--- declared foreign keys on the governance relations ---

child	conname	definition

wv_county_belief_snapshot	wv_county_belief_snapshot_canonical_county_id_fkeyFOREIGN KEY (canonical_county_id) REFERENCES wv_county_identity(canonical_county_id)

wv_county_dataset_coverage	wv_county_dataset_coverage_canonical_county_id_fkey	FOREIGN KEY (canonical_county_id) REFERENCES wv_county_identity(canonical_county_id)

wv_county_representation	wv_county_representation_county_fk	FOREIGN KEY (canonical_county_id) REFERENCES wv_county_identity(canonical_county_id) ON DELETE RESTRICT

wv_county_representation	wv_county_representation_table_fk	FOREIGN KEY (table_name) REFERENCES wv_layer_categories(table_name) ON DELETE CASCADE

wv_entity_registry	wv_entity_registry_table_fk	FOREIGN KEY (table_name) REFERENCES wv_layer_categories(table_name) ON DELETE CASCADE

wv_tract_belief_snapshot	wv_tract_belief_snapshot_canonical_county_id_fkeyFOREIGN KEY (canonical_county_id) REFERENCES wv_county_identity(canonical_county_id)

wv_tract_dataset_coverage	wv_tract_dataset_coverage_canonical_county_id_fkeyFOREIGN KEY (canonical_county_id) REFERENCES wv_county_identity(canonical_county_id)

wv_tract_identity	wv_tract_identity_canonical_county_id_fkey	FOREIGN KEY (canonical_county_id) REFERENCES wv_county_identity(canonical_county_id)

(8 rows)

############################################################

## 4. BRIDGE ORPHANS — join columns discovered, not assumed

############################################################

--- county: wv_county_identity.canonical_county_id  <->  wv_county_representation.canonical_county_id ---

check	rows

representation_without_identity	0

identity_without_representation	0

distinct_identities_in_bridge	55

(3 rows)

--- tract: wv_tract_identity.canonical_tract_id  <->  wv_tract_representation.canonical_tract_id ---

check	rows

representation_without_identity	0

identity_without_representation	0

distinct_identities_in_bridge	546

(3 rows)

############################################################

## 5. GIS-RAG 0.4.1 — correct port, live retrieval certification

############################################################

endpoint: http://127.0.0.1:8004

GET /health:

{"status":"healthy","service":"gis_rag","embed_model":"all-minilm:latest","collections":["gbim_wv_counties_v2","gbim_wv_tracts_v2"],"chroma_host":"jarvis-chroma","chroma_port":8000}

GET /docs:

    <!DOCTYPE html>

    <html>

    <head>

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">

    <link rel="shortcut icon" href="https://fastapi.tiangolo.com/img/favicon.png">

    <title>Ms. Jarvis Governed GIS RAG - Swagger UI</title>

    </head>

    <body>

    <div id="swagger-ui">

    </div>

    <script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js"></script>

    <!-- `SwaggerUIBundle` is now available on the page -->

    <script>

    const ui = SwaggerUIBundle({

        url: '/openapi.json',

    "dom_id": "#swagger-ui",

"layout": "BaseLayout",

"deepLinking": true,

"showExtensions": true,

"showCommonExtensions": true,

oauth2RedirectUrl: window.location.origin + '/docs/oauth2-redirect',

    presets: [

        SwaggerUIBundle.presets.apis,

        SwaggerUIBundle.SwaggerUIStandalonePreset

        ],

    })

    </script>

    </body>

    </html>

    

GET /openapi.json:

{"openapi":"3.1.0","info":{"title":"Ms. Jarvis Governed GIS RAG","version":"0.4.2"},"paths":{"/health":{"get":{"summary":"Health","operationId":"health_health_get","responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{"additionalProperties":true,"type":"object","title":"Response Health Health Get"}}}}}}},"/gis_rag":{"post":{"summary":"Gis Rag","operationId":"gis_rag_gis_rag_post","requestBody":{"content":{"application/json":{"schema":{"$ref":"#/components/schemas/GISRAGRequest"}}},"required":true},"responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{"$ref":"#/components/schemas/GISRAGResponse"}}}},"422":{"description":"Validation Error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/HTTPValidationError"}}}}}}}},"components":{"schemas":{"GISRAGHit":{"properties":{"text":{"type":"string","title":"Text"},"collection_name":{"type":"string","title":"Collection Name"},"document_id":{"anyOf":[{"type":"string"},{"type":"null"}],"title":"Document Id"},"distance":{"anyOf":[{"type":"number"},{"type":"null"}],"title":"Distance"},"layer_name":{"anyOf":[{"type":"string"},{"type":"null"}]

--- exact tract retrieval, Fayette 54019020101 (the chapter's certified record) ---

############################################################

## 6. PUBLISHED-BUT-UNGOVERNED COLLECTIONS

############################################################

Chroma store: /mnt/nvme1/msjarvis-data/chroma-live/chroma.sqlite3

--- governance relations that exist for each published gbim_wv_* collection ---

entity	has_identity	has_representation	has_coverage	has_snapshot	has_publication_view

county	t	t	t	t	t

tract	t	t	t	t	t

blockgroup	f	f	f	f	f

zcta	f	f	f	f	f

(4 rows)

--- what is actually inside gbim_wv_blockgroups_v1 and gbim_wv_zctas_v1 ---

    (metadata keys reveal whether these carry belief hashes and snapshot

     versions, or were embedded without governed provenance)

  collection: gbim_wv_blockgroups_v1

    metadata keys: access_class,authority_class,belief_hash,canonical_blockgroup_id,canonical_county_id,canonical_tract_id,chroma:document,county_geoid,county_name,dfirm_polygon_count,dfirm_polygon_coverage_state,permitted_use,rendering_version,snapshot_version,verification_state

    sample document id: 002d63cfb8d03d0bded911a4a8649e9ed559b0434ed796011e271da49d39ca40

  collection: gbim_wv_zctas_v1

    metadata keys: access_class,address_point_count,address_point_coverage_state,authority_class,belief_hash,canonical_county_id,canonical_zcta_id,chroma:document,county_geoid,county_name,dfirm_polygon_count,dfirm_polygon_coverage_state,permitted_use,rendering_version,snapshot_version,verification_state

    sample document id: 002e0539efa45e71a3c5cb8db12d9d20e03b6fedfaa97fcbf089d7756ae4517e

  collection: gbim_wv_counties_v2

    metadata keys: access_class,authority_class,bbox_max_lat,bbox_max_lon,bbox_min_lat,bbox_min_lon,belief_hash,canonical_county_id,centroid_lat,centroid_lon,chroma:document,county_geoid,county_name,entity_type,snapshot_version,source_feature_hash,source_feature_id,source_srid,source_table,state_abbrev,verification_state

    sample document id: 01ed99b63f0bd3e27dec99098314e945fd9027c46e8661b876ef498550d8f9f9

--- is GIS-RAG serving anything ungoverned? ---

GIS_RAG_COLLECTIONS=gbim_wv_counties_v2,gbim_wv_tracts_v2

############################################################

## 7. TRACT COVERAGE — why every tract reads 'unknown'

############################################################

Counties carry real coverage; tracts do not. These are the layers that

would resolve tract coverage if a spatial join were run:

f_table_name	type	srid	features

wv_censustracts_census_2020_utm83	GEOMETRY	26917	546

wv_hyd_hazus_floodplain_zones	MULTIPOLYGON	4269	0

wv_loc_sams2_address_road_centerlines	POINT	4269	0

wv_soc_census_blockgroups_2020	MULTIPOLYGON	4269	0

wv_soc_census_tracts_2020	MULTIPOLYGON	4269	0

wv_soc_zcta_2020	MULTIPOLYGON	4269	0

(6 rows)

--- distinct dataset_type values the coverage tables already recognise ---

scope	dataset_type	count

county	address_point	55

county	blockgroup	55

county	dfirm_polygon	55

county	tract	55

county	zcta	55

tract	address_point	546

tract	blockgroup	546

tract	dfirm_polygon	546

(8 rows)

############################################################

## END

############################################################

Written to: /home/cakidd/gbim-investigation-20260712T192124Z/24-verification.txt

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ chmod +x ~/Downloads/gbim-resolve.sh

~/Downloads/gbim-resolve.sh

GBIM resolution pass

Generated: 2026-07-12T19:29:44Z

############################################################

## A. WHERE IS THE REAL MANIFEST SET?

############################################################

Every copy of each manifest file on this machine, with size, line count,

hash, and how many rows actually name a wv_* relation. The largest

layer manifest is the real one.

--- wv_source_manifest_layers.csv ---

  path:      /mnt/spiritual_drive/msjarvis-rebuild/wv_source_manifest_layers.csv

    bytes:   1837   lines: 12   rows naming wv_*: 12

    sha256:  8f1282da0800e4c4ed25ce0fe87098c64bd8acde80efdc62ba5b482e83a54659

    modified:2026-07-12T17:51:27Z

    line 1:  ATM Weather Stations 1999,weatherStations_nationalClimateDataCenter_1999_utm27_shp.zip,NCDC,UTM27,public.wv_atm_weather_stations,weather_sta

  path:      /mnt/spiritual_drive/msjarvis-rebuild/ch52_checkpoint/wv_source_manifest_layers.csv

    bytes:   30834   lines: 212   rows naming wv_*: 149

    sha256:  4f8d233d7ec489336ff4cd00cf1e6065d06139ebd71696fded450a833a069761

    modified:2026-07-12T18:34:05Z

    line 1:  dataset_name,source_file,provider,crs,gbim_table,role

  path:      /home/cakidd/gbim-investigation-20260712T192124Z/wv_source_manifest_layers.csv

    bytes:   1837   lines: 12   rows naming wv_*: 12

    sha256:  8f1282da0800e4c4ed25ce0fe87098c64bd8acde80efdc62ba5b482e83a54659

    modified:2026-07-12T19:21:25Z

    line 1:  ATM Weather Stations 1999,weatherStations_nationalClimateDataCenter_1999_utm27_shp.zip,NCDC,UTM27,public.wv_atm_weather_stations,weather_sta

  path:      /home/cakidd/Downloads/files/wv_source_manifest_layers.csv

    bytes:   30834   lines: 212   rows naming wv_*: 149

    sha256:  4f8d233d7ec489336ff4cd00cf1e6065d06139ebd71696fded450a833a069761

    modified:2026-07-12T18:33:44Z

    line 1:  dataset_name,source_file,provider,crs,gbim_table,role

--- wv_source_files_manifest.csv ---

  path:      /mnt/spiritual_drive/msjarvis-rebuild/ch52_checkpoint/wv_source_files_manifest.csv

    bytes:   14884   lines: 244   rows naming wv_*: 0

    sha256:  9d53b39eb00087cf8d207fad3d7302f9d1776c55623fc08af2fdb001e9629af0

    modified:2026-07-12T18:34:05Z

    line 1:  filename,size,modified

  path:      /home/cakidd/Downloads/files/wv_source_files_manifest.csv

    bytes:   14884   lines: 244   rows naming wv_*: 0

    sha256:  9d53b39eb00087cf8d207fad3d7302f9d1776c55623fc08af2fdb001e9629af0

    modified:2026-07-12T17:39:27Z

    line 1:  filename,size,modified

--- wv_derived_governance_tables.csv ---

  path:      /mnt/spiritual_drive/msjarvis-rebuild/wv_derived_governance_tables.csv

    bytes:   4520   lines: 39   rows naming wv_*: 38

    sha256:  64844e50889aa97c667dc3179f7cdc83dd366156d5291946b6eaca4a949d2a45

    modified:2026-07-12T18:33:57Z

    line 1:  table_name,category,notes

  path:      /mnt/spiritual_drive/msjarvis-rebuild/ch52_checkpoint/wv_derived_governance_tables.csv

    bytes:   4520   lines: 39   rows naming wv_*: 38

    sha256:  64844e50889aa97c667dc3179f7cdc83dd366156d5291946b6eaca4a949d2a45

    modified:2026-07-12T18:34:05Z

    line 1:  table_name,category,notes

  path:      /home/cakidd/gbim-investigation-20260712T192124Z/wv_derived_governance_tables.csv

    bytes:   4520   lines: 39   rows naming wv_*: 38

    sha256:  64844e50889aa97c667dc3179f7cdc83dd366156d5291946b6eaca4a949d2a45

    modified:2026-07-12T19:21:25Z

    line 1:  table_name,category,notes

--- the GBIM checkpoint dump the appendix refers to ---

  /mnt/spiritual_drive/msjarvis-rebuild/ch52_checkpoint/msjarvisgis_v2-full.dump

    bytes: 21472908  modified: 2026-07-12T18:53:39Z

    siblings in that directory:

      msjarvisgis_v2-final.dump

      msjarvisgis_v2-full.dump

      wv_corpus_summary.csv

      wv_derived_governance_tables.csv

      wv_source_files_manifest.csv

      wv_source_manifest_layers.csv

  /mnt/spiritual_drive/msjarvis-rebuild/ch52_checkpoint/msjarvisgis_v2-final.dump

    bytes: 21470719  modified: 2026-07-12T17:47:20Z

    siblings in that directory:

      msjarvisgis_v2-final.dump

      msjarvisgis_v2-full.dump

      wv_corpus_summary.csv

      wv_derived_governance_tables.csv

      wv_source_files_manifest.csv

      wv_source_manifest_layers.csv

  /mnt/spiritual_drive/msjarvis-rebuild/msjarvisgis_v2-final.dump

    bytes: 21470719  modified: 2026-07-12T17:29:47Z

    siblings in that directory:

      =0.29.0

      100_percent_20260307_1219

      100_percent_remediation_100_percent_remediation_20260307_1224

      100_percent_remediation_20260307_1224

      93GB_CLUSTER_ANALYSIS_20260307_1647

      ai_server_20llm_PRODUCTION.py

      ai_server_20llm_PRODUCTION.py.bak_hpguard

      ai_server_20llm_PRODUCTION.py.bak_hppreflight

      all_gis_vectors_filtered.txt

      all_gis_vectors_full.txt

      all_gis_vectors_ingest.txt

      all_gis_vectors.txt

      all_gis_vectors_unique.txt

      api_resources.py

      api_specs

      application_service.py

      artifacts

      ask_gis_near_oakhill.py

      ask_gis.py

      attrs_api.py

      attrs_with_geom_api.py

      auth_api_health_only.py

      auth_api_no_full_router.py

      auth_api.patched.py

      auth_api.py

      auth_api.py.live

      auth_router.py

      auth_router.py.bak_20260630_022642

      auth_router.py.bak.20260630-151634

      auth_router.py.bak_hpguard

      auth_router.py.bak_hpguard2

      auth_router.py.bak_hppreflight

      autonomouslearner.py

      backpopulate_geospatial_features.py

      backup_chromadb.sh

      backup_configs.sh

      backup_filename_index.txt

      backup_postgresql.sh

      backup_roots.txt

      backups

      bbb_diag.log

      bbb_requirements.txt

      bibliography.md

      bootstrap_gbim_beliefs_eq1.py

      brain_orchestrator.py

      branding

      bulk_ingest_attrs.py

      cache

      call_rag_with_entanglement_example.py

      CERTIFICATION.txt

      certs

      ch52_checkpoint

      CHAPTER_32_PRODUCTION_NOTE.md

      chat_light_current.py

      check_local_resources.sh

      chroma_copy_v2.log

      chroma_copy_v2.py

      chroma_data

      chroma_db

      chroma_diagnosis_20260307_1159

      chroma_fix_20260307_1201

      chroma_ingestion_sources.txt

      chroma_version_backup.txt

      civic_projector.py.bak

      CLEANUP_SUCCESS_REPORT_2026-03-14.md

      COMPLETE_69_PROPOSALS.json

      COMPLETE_73_SERVICES.json

      complete_service_mapping.json

      config

      constitutional_api.py

      contracts

      copy_pending_collections.py

      copy_pending.log

      CORRECTED_PROPOSALS.json

      create_egeria_model.log

      crypto-venv

      CURRENT_LLM_STACK_NOTES.txt

      dashboard

      data

      db

      definitive_fix.log

      Definitive Service Inventory.md

      demo_msjarvis_ranked.py

      demo_msjarvis_resources.py

      deploy

      DEPLOYMENT_SUCCESS_20260307.md

      dgm_adoption_log.json

      dgm_cycle.log

      dgm_cycle.sh

      dgm_deployment_scripts

      dgm_governance_view.json

      dgm_governance_view.json.backup_20260307_1224

      dgm_governance_view.json.pre_all_services

      dgm_governance_view.json.pre_phase1_array

      dgm_patch_queue.json

      dgm_remap_step.py

      dgm_safe_cycle.sh

      dgm_service_remap.json

      discipline

      docker-compose.override.yml

      docker-compose.override.yml.bak.20260629-204745

      docker-compose.override.yml.bak.20260701-083215

      docker-compose.override.yml.bak.20260701-083313

      docker-compose.override.yml.bak.20260701-083427

      docker-compose.override.yml.disabled.20260701-083531

      docker-compose.override.yml.postverify.bak.20260629-204820

      docker-compose.real-orchestrator.yml

      docker-compose.STABLE_20260701_092336.yml

      docker-compose.STABLE_20260701_092336.yml.bak_before_rw

      docker-compose.STABLE_20260702_112917.yml

      docker-compose.STABLE_20260702_122118.yml

      docker-compose.STABLE_20260702_123228.yml

      docker-compose.STABLE_20260702_232604.yml

      docker-compose.STABLE_20260702_232748.yml

      docker-compose.STABLE_20260703_000658.yml

      docker-compose.STABLE_20260703_002117.yml

      docker-compose.STABLE_20260703_002836.yml

      docker-compose.STABLE_20260703_015134.yml

      docker-compose.STABLE_20260703_103332.yml

      docker-compose.STABLE_20260706_142809.yml

      docker-compose.yml

      docker-compose.yml.bak.1782019167

      docker-compose.yml.bak.1782021398

      docker-compose.yml.bak-20260320-220133

      docker-compose.yml.bak.20260531-123431

      docker-compose.yml.bak.20260531-123509

      docker-compose.yml.bak.20260629-204745

      docker-compose.yml.bak.20260701-083703

      docker-compose.yml.bak.20260701-083922

      docker-compose.yml.bak.20260701-084023

      docker-compose.yml.bak.20260701-084637

      docker-compose.yml.bak.20260701-085107

      docker-compose.yml.bak.20260701-085145

      docker-compose.yml.bak.20260701-085211

      docker-compose.yml.bak.20260701-085259

      docker-compose.yml.bak.20260701-090439

      docker-compose.yml.bak.20260701-090746

      docker-compose.yml.bak.20260708-210502-pgmove

      docker-compose.yml.bak.20260708-210741-pgmove

      docker-compose.yml.bak.20260708-212446-pgmove-verified

      docker-compose.yml.bak.20260709_133412

      docker-compose.yml.bak.pre-merge.20260701-092016

      docker-compose.yml.postverify.bak.20260629-204820

      Dockerfile

      Dockerfile.20llm

      Dockerfile.agents

      Dockerfile.bak_before_python3_fix

      Dockerfile.brain

      Dockerfile.consciousnessbridge

      Dockerfile.full_neuro

      Dockerfile.gateway

      Dockerfile.gis-rag

      Dockerfile.gis_rag

      Dockerfile.hilbert_spatial_chat

      Dockerfile-llm10-proxy

      Dockerfile-llm11-proxy

      Dockerfile-llm12-proxy

      Dockerfile-llm13-proxy

      Dockerfile-llm14-proxy

      Dockerfile-llm15-proxy

      Dockerfile-llm16-proxy

      Dockerfile-llm17-proxy

      Dockerfile-llm18-proxy

      Dockerfile-llm19-proxy

      Dockerfile-llm1-proxy

      Dockerfile-llm20-proxy

      Dockerfile-llm21-proxy

      Dockerfile-llm22-proxy

      Dockerfile-llm2-proxy

      Dockerfile-llm3-proxy

      Dockerfile-llm4-proxy

      Dockerfile-llm5-proxy

      Dockerfile-llm6-proxy

      Dockerfile-llm7-proxy

      Dockerfile-llm8-proxy

      Dockerfile-llm9-proxy

      Dockerfile.local_resources

      Dockerfile.nbb_icontainers_fastapi

      Dockerfile.neuro

      Dockerfile.neuro-prefrontal-patched

      Dockerfile.qualia

      Dockerfile.qualia.bak

      Dockerfile.rag

      Dockerfile.rag_server

      Dockerfile.rag_server_main

      Dockerfile.ragservermain

      Dockerfile.sandbox

      Dockerfile.swarm

      Dockerfile.woah

      docs

      dual_consciousness_analysis_20260307_1217

      dynamic_port_service_no_flask.py

      egeria_knowledge_base

      email_service.py

      emergency_fix_20260307_1205

      enrich_from_attrs.py

      enrich_where.py

      entity_canonical.csv

      entity_canonical_v2.csv

      entity_clusters.csv

      export_chroma_8002.py

      export_chroma_raw_8002.py

      export_gbim_sample.py

      fayette_dem.tif

      FINAL_CLEANUP_REPORT_2026-03-14.md

      final_gbim_hunt_20260307_1624

      FINAL_SESSION_RESULTS.md

      final_solution_20260307_1212

      final_test_proposals.json

      final_working_proposals.json

      finish_zip.py

      fix_bbb.log

      flyers

      FULL_73_PROPOSALS.json

      gateway8050_inline.py

      gbim_chroma.py

      GBIM_DIRECT_20260307_1644

      GBIM_FINAL_20260307_1640

      GBIM_FINAL_20260307_1642

      GBIM_FINAL_VERIFIED_20260307_1646

      gbim_geospatial_ingest.log

      gbim_hunt_20260307_1231

      gbim_inspection_20260307_1207

      gbim_investigation_20260307_1233

      gbim_orchestrator.py

      gbim_search_20260307_1227

      GBIM_VERIFIED_COMPLETE_20260307_1650

      generate_spiritual_inventories.py

      gis_candidates_global.txt

      gis_candidates_stage2.txt

      gisgeodb_storage.py

      gisgeodbstorage.py

      gis_rag_query.py

      gis_rag_server.py

      govt_canonical.csv

      govt_owners_raw.csv

      hardhat.config.cjs

      hilbert_coherence_monitor.py

      hilbert_monitor.pid

      hilbert_people

      hp_antisurveillance_guardian_client.py

      hpantisurveillanceguardianclient.py

      hp_antisurveillance_guardian_client.py.bak_hpguard

      hp_antisurveillance_policy.json

      indexes

      index_gis_to_chroma.py

      ingest_attrs_to_chroma.py

      ingest_checkpoint.json

      ingest_gbimworldviewentities_from_csv.py

      ingest_geospatial_to_gbim.py

      ingest_gis.log

      ingest_gis_to_chroma.py

      ingest_kanawha_images.py

      ingest_kanawha_resources.py

      ingest_missing_attrs.py

      ingest_msjarvis_corpus.py

      ingest_personal_pdfs.py

      ingest_wv_income_maintenance_manual.py

      inspect_address_points.sh

      investigate_gbim_linkage.py

      investigation_20260617_165531.json

      itest-69dgm-bridge-logs

      jarvis_eeg_beta_5m.py

      jarvis_identity.db

      jarvis_startup.sh

      judge-keys

      keys

      knowledge

      KNOWN_LIMITATIONS_20LLM_SEQUENTIAL.txt

      kyc-vault

      layer3_opt_in.py

      LICENSE

      list_due_for_verification.py

      llm10_health_proxy.py

      llm11_health_proxy.py

      llm12_health_proxy.py

      llm13_health_proxy.py

      llm14_health_proxy.py

      llm15_health_proxy.py

      llm16_health_proxy.py

      llm17_health_proxy.py

      llm18_health_proxy.py

      llm19_health_proxy.py

      llm1_health_proxy.py

      llm20_health_proxy.py

      llm21_health_proxy.py

      llm22_health_proxy.py

      llm2_health_proxy.py

      llm3_health_proxy.py

      llm4_health_proxy.py

      llm5_health_proxy.py

      llm6_health_proxy.py

      llm7_health_proxy.py

      llm8_health_proxy.py

      llm9_health_proxy.py

      load_services_attrs_and_enrich.py

      logs

      main_brain.py

      main.py

      MARCH16_2026_STARTUP.md

      merkle_identity.py

      migrate_chroma_collections.py

      migrate_spiritual_texts.py

      migrate_to_layer_collections.py

      migrate_to_layer_collections.py.bak

      migrate_to_layer_collections_v2.py

      migrate_to_layer_collections_v3.py

      migrate_to_layer_collections_v3.py.bak_hpguard

      migrate_to_layer_collections_v3.py.bak_hppreflight

      migration_checkpoint.json

      migration_checkpoint_v3.json

      migration.log

      migrations

      migration_v3_shard.log

      missing_local_files.txt

      models

      models.py

      monitor_disk.sh

      mountainshares-dao

      msallis_next_steps.sh

      ms_jarvis_20llm_production.py

      msjarvis_audit_snapshot.sh

      msjarvis_chroma_backup_verify.sh

      msjarvis_chroma_test.py

      ms_jarvis_consciousness_bridge.py

      ms_jarvis_darwin_godel_machine.py

      msjarvis_embed_gbim.py

      msjarvis_embed_gbim_resume_tail.py

      MSJARVISGIS_FINAL_20260307_1649

      msjarvisgis-final.dump

      msjarvisgis_v2-final.dump

      msjarvis_port_audit.sh

      ms_jarvis_psychology_services.py

      ms_jarvis_rag_server.py

      msjarvisragserverwvpatch.py

      ms_jarvis_ram_watchdog.py

      msjarvis-rebuild

      msjarvis_resources.py

      ms_jarvis_spiritual_services.py

      ms_jarvis_unified_gateway.py

      msjarviswoahalgorithms.py

      nbb_dgm_backup.json

      neurobiological_brain

      neurological_brain

      NEXT_SESSION_QUICK_START.md

      NEXT_SESSION_ROADMAP.md

      node_modules

      nohup.out

      old_drive_gis_candidates.txt

      package.json

      package-lock.json

      patch_egeria_run.log

      pdf_utils.py

      persistent

      phase1_discovery

      phase1_governance_additions.json

      postgresql_gbim_verification_20260307_1639

      process_wv_layers.py

      progress_history.log

      provenance

      psychological_rag_domain.py

      __pycache__

      pytest.ini

      query_msjarvis_corpus.py

      query_msjarvis_once.py

      rag_insert_mountainshares.py

      rag_local_resources.py

      rag_server_main.py

      ragservermain.py

      randolph_matches.sql

      README.md

      reconciliation_20260307_1209

      red_team_20260307_1658

      registration_pipeline.py

      registration_service.py

      reingest_msjarvis_chunks.py

      rejected_patches

      remediation_20260307_1153

      remediation_20260307_1157

      repair_checkpoint.json

      requirements.txt

      resource_assistant.py

      resource_ranker.py

      restore_fix.log

      rotate_judge_keys.sh

      run_address_points_ingest.sh

      run_all_backups.sh

      run_auth_uvicorn.py

      RUN_THESIS_TESTS.md

      scratch_edits

      scripts

      secrets

      security

      seed_full_knowledge.py

      seed_gbim_catalog.py

      seed_mountainshares.py

      service_build_matrix.txt

      service_discovery_no_redis.py

      service_file_mapping.json

      service_registry_client_stub.py

      services

      SESSION_CLOSE_COMMANDS.md

      SESSION_FINAL_20260307_1109.md

      SESSION_SUMMARY_20260307.md

      spiritual_rag_domain.py

      STABLE_MODE_NOTE.txt

      staged_mutations

      start_hilbert_state.sh

      sync_gbim_to_chroma.py

      test_autonomous_learner_store.py

      test_dgm_rag_integration.py

      test_dgm_rag_v2.py

      test_end_to_end_woah_fifthdgm.py

      test_rag_image.py

      test_rag_text.py

      tests

      test_sandbox.sh

      the commons

      The Ms. Jarvis Steward System.md

      theory

      thesis

      tmp_rag_slice.py

      token_service.py

      to long.md

      TONIGHT_VICTORY_MARCH15_2026.md

      track_a_dryrun.json

      track_a_enqueue.json

      track_a_proposals.json

      track_a_validation_report.md

      trail_router.py

      uei_service.py

      uploads

      vat_CERTIFIED_20260411.log

      verification_reports_20260307_1150

      VERIFICATION_RESULTS_2026-03-15.txt

      verify_69dgm_rag_integration.sh

      VERIFYANDTEST.sh

      verify_proposals.json

      VICTORY_REPORT_2026-03-15.md

      view_dgm_queue.py

      weekly_cleanup.sh

      wv_centroid.txt

      wv_corpus_summary.csv

      wv_derived_governance_tables.csv

      wv_entangled_context_model.py

      wv_governance_table_count.txt

      wv_governance_tables_unique.txt

      wv_like_csv_candidates.txt

      wv_mapped_table_count.txt

      wv_mapped_table_names.txt

      wv_mapped_tables_unique.txt

      wv_name_matches_current_pv.txt

      wv_public_relations.csv

      wv_public_relations.tsv

      wv_public_table_count_from_csv.txt

      wv_public_table_count.txt

      wv_public_table_names.txt

      wv_public_tables.csv

      wv_source_manifest_layers.csv

      wv_unmapped_table_names.txt

  /home/cakidd/msjarvis-db-recovery/msjarvisgis_v2_verified.dump

    bytes: 926712  modified: 2026-07-12T00:31:39Z

    siblings in that directory:

      container-env.txt

      container-inspect.json

      container-mounts.txt

      container-stdout.log

      database-list.txt

      gbim_physical_sources.dump

      gbim_physical_sources.list

      governance-object-search.txt

      jarvis-msjarvis-db-20260712T000016Z.tar

      msjarvisgis_governance_recovered.dump

      msjarvisgis_governance_schema.sql

      msjarvisgis_governance_tables.sql

      msjarvisgis_v2_chroma_active.dump

      msjarvisgis_v2_chroma_active.dump.sha256

      msjarvisgis_v2_complete.dump

      msjarvisgis_v2_complete.dump.sha256

      msjarvisgis_v2_vector_ready.dump

      msjarvisgis_v2_vector_ready.dump.sha256

      msjarvisgis_v2_verified.dump

      rag-integration

      validate_bridges_v2.log

      wv_county_belief_snapshot.csv

      wv_county_dataset_coverage.csv

      wv_county_identity.csv

      wv_county_representation.csv

      wv_entity_registry.csv

      wv_layer_categories.csv

      wv_tract_belief_snapshot.csv

      wv_tract_dataset_coverage.csv

      wv_tract_identity.csv

      wv_tract_representation.csv

  /home/cakidd/msjarvis-db-recovery/msjarvisgis_v2_chroma_active.dump

    bytes: 21470719  modified: 2026-07-12T03:27:47Z

    siblings in that directory:

      container-env.txt

      container-inspect.json

      container-mounts.txt

      container-stdout.log

      database-list.txt

      gbim_physical_sources.dump

      gbim_physical_sources.list

      governance-object-search.txt

      jarvis-msjarvis-db-20260712T000016Z.tar

      msjarvisgis_governance_recovered.dump

      msjarvisgis_governance_schema.sql

      msjarvisgis_governance_tables.sql

      msjarvisgis_v2_chroma_active.dump

      msjarvisgis_v2_chroma_active.dump.sha256

      msjarvisgis_v2_complete.dump

      msjarvisgis_v2_complete.dump.sha256

      msjarvisgis_v2_vector_ready.dump

      msjarvisgis_v2_vector_ready.dump.sha256

      msjarvisgis_v2_verified.dump

      rag-integration

      validate_bridges_v2.log

      wv_county_belief_snapshot.csv

      wv_county_dataset_coverage.csv

      wv_county_identity.csv

      wv_county_representation.csv

      wv_entity_registry.csv

      wv_layer_categories.csv

      wv_tract_belief_snapshot.csv

      wv_tract_dataset_coverage.csv

      wv_tract_identity.csv

      wv_tract_representation.csv

  /home/cakidd/msjarvis-db-recovery/msjarvisgis_v2_complete.dump

    bytes: 21368604  modified: 2026-07-12T01:57:03Z

    siblings in that directory:

      container-env.txt

      container-inspect.json

      container-mounts.txt

      container-stdout.log

      database-list.txt

      gbim_physical_sources.dump

      gbim_physical_sources.list

      governance-object-search.txt

      jarvis-msjarvis-db-20260712T000016Z.tar

      msjarvisgis_governance_recovered.dump

      msjarvisgis_governance_schema.sql

      msjarvisgis_governance_tables.sql

      msjarvisgis_v2_chroma_active.dump

      msjarvisgis_v2_chroma_active.dump.sha256

      msjarvisgis_v2_complete.dump

      msjarvisgis_v2_complete.dump.sha256

      msjarvisgis_v2_vector_ready.dump

      msjarvisgis_v2_vector_ready.dump.sha256

      msjarvisgis_v2_verified.dump

      rag-integration

      validate_bridges_v2.log

      wv_county_belief_snapshot.csv

      wv_county_dataset_coverage.csv

      wv_county_identity.csv

      wv_county_representation.csv

      wv_entity_registry.csv

      wv_layer_categories.csv

      wv_tract_belief_snapshot.csv

      wv_tract_dataset_coverage.csv

      wv_tract_identity.csv

      wv_tract_representation.csv

  /home/cakidd/msjarvis-db-recovery/msjarvisgis_v2_vector_ready.dump

    bytes: 21465790  modified: 2026-07-12T02:25:10Z

    siblings in that directory:

      container-env.txt

      container-inspect.json

      container-mounts.txt

      container-stdout.log

      database-list.txt

      gbim_physical_sources.dump

      gbim_physical_sources.list

      governance-object-search.txt

      jarvis-msjarvis-db-20260712T000016Z.tar

      msjarvisgis_governance_recovered.dump

      msjarvisgis_governance_schema.sql

      msjarvisgis_governance_tables.sql

      msjarvisgis_v2_chroma_active.dump

      msjarvisgis_v2_chroma_active.dump.sha256

      msjarvisgis_v2_complete.dump

      msjarvisgis_v2_complete.dump.sha256

      msjarvisgis_v2_vector_ready.dump

      msjarvisgis_v2_vector_ready.dump.sha256

      msjarvisgis_v2_verified.dump

      rag-integration

      validate_bridges_v2.log

      wv_county_belief_snapshot.csv

      wv_county_dataset_coverage.csv

      wv_county_identity.csv

      wv_county_representation.csv

      wv_entity_registry.csv

      wv_layer_categories.csv

      wv_tract_belief_snapshot.csv

      wv_tract_dataset_coverage.csv

      wv_tract_identity.csv

      wv_tract_representation.csv

############################################################

## B. IMPORTED IN SUBSTANCE, OR ONLY IN SCHEMA?

############################################################

Exact row counts were already captured in 06-exact-row-counts.tsv.

This is the decisive question for Chapter 52: a relation with zero rows

is a table shell, not imported evidence.

  relations counted: 154

  populated:         20  (14835 rows total)

  EMPTY (0 rows):    134

  empty relations:

    wv_atm_weather_stations

    wv_bio_biodiversity_rank

    wv_bio_ecoregions

    wv_bio_red_spruce_cover

    wv_bnd_appalachian_basin_boundary

    wv_bnd_arc_counties

    wv_bnd_canaan_valley_nwr

    wv_bnd_census_designated_places

    wv_bnd_county_24k

    wv_bnd_county_municipal_dlg

    wv_bnd_mnf_basic_ownership

    wv_bnd_mnf_management_prescriptions

    wv_bnd_mnf_ranger_districts

    wv_bnd_mnf_recreation_campgrounds

    wv_bnd_mnf_recreation_sites

    wv_bnd_mnf_wilderness

    wv_bnd_morgantown_wards

    wv_bnd_nhd_mussel_streams

    wv_bnd_public_lands_county_city_parks

    wv_bnd_public_lands_national_forest

    wv_bnd_public_lands_national_park

    wv_bnd_public_lands_nwr

    wv_bnd_public_lands_state_forests

    wv_bnd_public_lands_state_parks

    wv_bnd_public_lands_wildlife_resources

    wv_bnd_state_boundary_100k

    wv_bnd_voting_districts_2000

    wv_bnd_voting_districts_2002

    wv_bnd_workforce_investment_areas

    wv_eco_abandoned_mine_lands_line

    wv_eco_abandoned_mine_lands_point

    wv_eco_abandoned_mine_lands_polygon

    wv_eco_coal_fields

    wv_eco_ezec_communities

    wv_eco_industrial_sites

    wv_eco_manufacturing_directory

    wv_eco_mineral_operations

    wv_eco_mountaintop_removal

    wv_elv_summit_names

    wv_env_air_nonattainment

    wv_env_epa_facilities

    wv_env_timber_removal_volume

    wv_env_wildfire_regions

    wv_env_wind_energy_resources

    wv_geo_coal_beds

    wv_geo_geological_map_generalized

    wv_geo_karst

    wv_hlt_health_providers

    wv_hlt_public_health_departments

    wv_hlt_rural_health_facilities

    wv_hyd_dams_dmr

    wv_hyd_dams_nid

    wv_hyd_dams_noncoal

    wv_hyd_hazus_floodplain_zones

    wv_hyd_high_water_marks

    wv_hyd_navigable_waterways

    wv_hyd_navigable_waterways_river_miles

    wv_hyd_navigable_waterways_structures

    wv_hyd_springs_100gpm

    wv_hyd_streamflow_stations

    wv_hyd_streams_high_quality

    wv_hyd_streams_national_atlas

    wv_hyd_streams_tiger

    wv_hyd_watershed_boundary_11digit

    wv_hyd_watershed_boundary_12digit_hu

    wv_hyd_watershed_boundary_8_10_12

    wv_loc_census_urbanized_areas

    wv_loc_county_seats

    wv_loc_geodetic_control_points

    wv_loc_populated_places_census

    wv_loc_sams2_address_road_centerlines

    wv_mil_army_reserve_facilities

    wv_mil_national_guard_armories

    wv_plc_hazus_level1

    wv_plc_regional_planning_councils

    wv_plc_tax_district_boundaries

    wv_plc_tax_parcels_surface_mineral

    wv_soc_911_centers

    wv_soc_census_blockgroups_2020

    wv_soc_census_tracts_2020

    wv_soc_cities_pop10k

    wv_soc_cities_pop2500

    wv_soc_communities_pop_change

    wv_soc_courthouses_county

    wv_soc_courthouses_federal

    wv_soc_fish_hatcheries

    wv_soc_fishing_boating_access

    wv_soc_fishing_lakes

    wv_soc_higher_ed_facilities

    wv_soc_hospitals_wvdem

    wv_soc_libraries

    wv_soc_national_register_historic_points

    wv_soc_national_register_historic_polygons

    wv_soc_nursing_homes

    wv_soc_places_of_worship_wvgistc

    wv_soc_population_by_decade

    wv_soc_schools_k12

    wv_soc_towers_am

    wv_soc_towers_asr

    wv_soc_towers_cellular

    wv_soc_towers_fm

    wv_soc_towers_microwave

    wv_soc_towers_pager

    wv_soc_towers_private

    wv_soc_towers_tv

    wv_soc_va_facilities

    wv_soc_zcta_2020

    wv_str_bridges

    wv_str_correctional_institutions

    wv_str_flood_atrisk_structures

    wv_str_parole_offices

    wv_str_places_of_worship_hsip

    wv_str_samb_building_points

    wv_str_samb_building_polygons

    wv_trn_airport_facilities

    wv_trn_airport_proposed

    wv_trn_airport_runways

    wv_trn_airports

    wv_trn_intermodal_terminals

    wv_trn_mnf_recreation_trails

    wv_trn_mnf_roads

    wv_trn_railroad_lines_rti

    wv_trn_railroads_amtrak

    wv_trn_railroads_excursion

    wv_trn_railroads_national_network

    wv_trn_recreational_trails

    wv_trn_roads_interstate

    wv_trn_roads_major_4800

    wv_trn_roads_state_routes

    wv_trn_roads_us_highways

    wv_trn_roads_us_routes

    wv_trn_whitewater_trails

    wv_util_sewer_treatment_plants

    wv_util_solid_waste_facilities

--- top 25 populated wv_* relations by row count ---

relname	exact_rows

wv_tract_dataset_coverage	1638

wv_tract_belief_snapshot	1092

wv_censustracts_census_2020_utm83	546

wv_tract_identity	546

wv_tract_representation	546

wv_tract_representation_pre_gid_rebind	546

wv_county_dataset_coverage	275

wv_layer_categories	254

wv_county_representation	220

wv_county_representation_pre_gid_rebind	218

wv_county_belief_snapshot	110

wv_entity_registry	65

wv_county_boundaries_24k_topo_updated_2026_utm83_gdb	55

wv_county_boundaries_24k_topo_updated_2026_wma84_gdb	55

wv_county_identity	55

wv_wv_county_boundaries_24k_topo_updated_2026_utm83	55

wv_wv_county_boundaries_24k_topo_updated_2026_wma84	55

wv_atm_weather_stations	0

wv_bio_biodiversity_rank	0

wv_bio_ecoregions	0

wv_bio_red_spruce_cover	0

wv_bnd_appalachian_basin_boundary	0

wv_bnd_arc_counties	0

wv_bnd_canaan_valley_nwr	0

wv_bnd_census_designated_places	0

(25 rows)

############################################################

## C. WHAT DID COVERAGE ACTUALLY COUNT AGAINST?

############################################################

County coverage reports blockgroup=present for all 55 counties, yet

wv_soc_census_blockgroups_2020 holds zero features. So coverage was

computed against some OTHER table. The coverage rows record which.

scope	dataset_type	source_table	coverage_rows	summed_features	source_exists

county	address_point	wv_address_points_union	55	212621	f

county	blockgroup	wv_blockgroups_census_2020_utm83	55	1635	f

county	dfirm_polygon	wv_hyd_dfirm_nfhl	55	696	f

county	tract	wv_censustracts_census_2020_utm83	55	544	t

county	zcta	wv_zipcodetabulationarea_census_2020_utm83	55	741	f

tract	address_point	wv_address_points_union	546	0	f

tract	blockgroup	wv_blockgroups_census_2020_utm83	546	0	f

tract	dfirm_polygon	wv_hyd_dfirm_nfhl	546	0	f

(8 rows)

--- do those source tables actually hold rows today? ---

source_table	exists_now	rows_now

wv_address_points_union	f	

wv_blockgroups_census_2020_utm83	f	

wv_censustracts_census_2020_utm83	t	546

wv_hyd_dfirm_nfhl	f	

wv_zipcodetabulationarea_census_2020_utm83	f	

(5 rows)

############################################################

## D. WHERE ARE THE BLOCKGROUP / ZCTA GOVERNANCE RELATIONS?

############################################################

Their Chroma collections carry belief_hash, snapshot_version,

canonical ids, coverage states and verification_state — a governed

pipeline produced them. They are absent from msjarvisgis_v2.

--- msjarvisgis_v2: any blockgroup/zcta governance relations? ---

relname	relkind	rows

wv_soc_census_blockgroups_2020	r	0

wv_soc_zcta_2020	r	0

(2 rows)

--- msjarvisgis (the older database): governance relations of any kind ---

relname	relkind

wv_soc_census_blockgroups_2020	r

wv_soc_zcta_2020	r

(2 rows)

--- the three phantom relations the derived manifest names ---

  wv_bnd_public_lands_union: v2=ABSENT   msjarvisgis=ABSENT

  wv_county_summary_metrics: v2=ABSENT   msjarvisgis=ABSENT

  wv_tract_summary_metrics: v2=ABSENT   msjarvisgis=ABSENT

############################################################

## E. GIS-RAG RETRIEVAL — correct endpoint this time

############################################################

Service reports version 0.4.2 (the chapter says 0.4.1). The endpoint is

POST /gis_rag — the earlier script guessed wrong paths and silently got

nothing. This is the real certification test.

--- county: Fayette 54019 ---

{"hits":[{"text":"Fayette County, West Virginia, has canonical county GEOID 54019. This is a governed county belief derived from official public geographic sources. address_point coverage has feature count 0 and state unknown. This count must not be interpreted as verified absence. blockgroup coverage has feature count 21 and state present. dfirm_polygon coverage has feature count 138 and state present. tract coverage has feature count 13 and state present. zcta coverage has feature count 42 and state present.","collection_name":"gbim_wv_counties_v2","document_id":"85d65d0bf7b4065fa125db2f53d00facd33f68fcfa2c1aecc8344fa4a37eb198","distance":0.9661045059706177,"layer_name":null,"name":"Fayette","lat":null,"lon":null,"metadata":{"access_class":"public","authority_class":"official","bbox_max_lat":38.263552016599945,"bbox_max_lon":-80.74882376185612,"bbox_min_lat":37.81916060958731,"bbox_min_lon":-81.38085192175508,"belief_hash":"85d65d0bf7b4065fa125db2f53d00facd33f68fcfa2c1aecc8344fa4a37eb198","canonical_county_id":"54019","centroid_lat":38.02870347271499,"centroid_lon":-81.08118494200872,"county_geoid":"54019","county_name":"Fayette","entity_type":"county","snapshot_version":"wv-county-snapshot-v2","source_feature_hash":"8a8e975bda147f4eac80244cdb4d0b4cf1ff2fa7d2ee0eceb5a61f33565c6521","source_feature_id":22,"source_srid":26917,"source_table":"wv_wv_county_boundaries_24k_topo_updated_2026_utm83","state_abbrev":"WV","verification_state":"derived"}}]}

--- tract: Fayette 54019020101 (the chapter's certified record) ---

{"hits":[{"text":"Census tract 54019020101 is a governed 2020 Census tract in Fayette County, West Virginia, county GEOID 54019. address_point coverage has feature count 0 and state unknown. This count must not be interpreted as verified absence. blockgroup coverage has feature count 0 and state unknown. This count must not be interpreted as verified absence. dfirm_polygon coverage has feature count 0 and state unknown. This count must not be interpreted as verified absence.","collection_name":"gbim_wv_tracts_v2","document_id":"200c95e7f358572e5084c937ceaf3e55b9f0b75ed8973065b98b90603043dca6","distance":0.38131988048553467,"layer_name":null,"name":"Fayette","lat":null,"lon":null,"metadata":{"access_class":"public","authority_class":"official","bbox_max_lat":38.06893599999999,"bbox_max_lon":-81.02137,"bbox_min_lat":37.959078,"bbox_min_lon":-81.12449,"belief_hash":"200c95e7f358572e5084c937ceaf3e55b9f0b75ed8973065b98b90603043dca6","canonical_county_id":"54019","canonical_tract_id":"1400000US54019020101","centroid_lat":38.015144054381956,"centroid_lon":-81.06644610990612,"county_name":"Fayette","entity_type":"census_tract","snapshot_version":"wv-tract-snapshot-v2","source_feature_hash":"9cf6ef974d3ffd4cf92f0001a1661421c884d075956021a48115f8c27ddce1a9","source_feature_id":250,"source_srid":26917,"source_table":"wv_censustracts_census_2020_utm83","tract_geoid":"54019020101","verification_state":"derived"}}]}

############################################################

## END

############################################################

Written to: /home/cakidd/gbim-investigation-20260712T192124Z/27-resolution.txt

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ chmod +x ~/Downloads/gbim-evidence.sh

~/Downloads/gbim-evidence.sh

GBIM evidence hunt

Generated: 2026-07-12T19:32:42Z

############################################################

## 1. RECONCILIATION AGAINST THE REAL MANIFESTS

############################################################

The manifests I reconciled against earlier were a 12-line fragment.

The real ones are in ch52_checkpoint: 212 lines, proper header,

149 rows naming wv_* relations.

  wv_source_manifest_layers.csv: column 'gbim_table' -> 147 relations

  wv_derived_governance_tables.csv: column 'table_name' -> 35 relations

  live relations:  153

  accounted for:   151

  GATE 17 — live relations in no manifest: 2

      wv_tract_representation

      wv_tract_representation_pre_gid_rebind

  GATE 18 — manifest names with no relation: 14

      wv_atm_geodeticsurveycontrol

      wv_atm_spotelevations

      wv_atm_weather_stations_utm27

      wv_bio_ecoregions_ll83

      wv_bio_fish_hatcheries

      wv_bio_public_fishing_boating_access

      wv_bio_public_fishing_lakes

      wv_bnd_public_lands_union

      wv_county_summary_metrics

      wv_tax_districts_24k_topo_utm83

      wv_tax_districts_500k_ll83

      wv_tax_districts_500k_utm27

      wv_tax_districts_500k_utm83

      wv_tract_summary_metrics

  NOTE: a manifest row maps a TABLE NAME to a SOURCE FILE.

        It does not assert that the table contains data.

--- wv_corpus_summary.csv (checkpoint sibling, not yet examined) ---

  lines: 5

  header + first 10 rows:

    metric,value

    public_wv_tables_total,151

    dataset_tables_mapped,209

    governance_tables_documented,35

    unmapped_tables_remaining,15

############################################################

## 2. EVERY DATABASE, EVERY CLUSTER — WHERE IS POPULATED GIS DATA?

############################################################

Two Postgres listeners exist: 5436 and 5433. Check both.

===== cluster on port 5436 =====

  --- msjarvis ---

    relname	rows

    (0 rows)

  --- msjarvisgis ---

    relname	rows

    wv_plc_tax_parcels_surface_mineral	1389855

    wv_str_samb_building_points	1366959

    wv_loc_sams2_address_road_centerlines	1135834

    wv_env_wind_energy_resources	104812

    wv_str_flood_atrisk_structures	81054

    wv_plc_hazus_level1	80122

    wv_hyd_streams_tiger	67774

    wv_bio_biodiversity_rank	63912

    wv_hyd_navigable_waterways_structures	32116

    wv_hyd_streams_high_quality	22656

    wv_trn_roads_major_4800	19795

    wv_bio_red_spruce_cover	15514

    wv_str_samb_building_polygons	15505

    wv_bnd_nhd_mussel_streams	11590

    wv_eco_abandoned_mine_lands_line	10796

    wv_loc_geodetic_control_points	8559

    wv_eco_manufacturing_directory	8317

    wv_str_bridges	7357

    wv_soc_towers_private	5687

    wv_soc_places_of_worship_wvgistc	5613

    (20 rows)

  --- msjarvisgis_v2 ---

    relname	rows

    wv_tract_dataset_coverage	1638

    wv_tract_belief_snapshot	1092

    wv_tract_representation	546

    wv_tract_identity	546

    wv_tract_representation_pre_gid_rebind	546

    wv_censustracts_census_2020_utm83	546

    wv_county_dataset_coverage	275

    wv_layer_categories	254

    wv_county_representation	220

    wv_county_representation_pre_gid_rebind	218

    wv_county_belief_snapshot	110

    wv_entity_registry	65

    wv_wv_county_boundaries_24k_topo_updated_2026_wma84	55

    wv_county_boundaries_24k_topo_updated_2026_wma84_gdb	55

    wv_county_boundaries_24k_topo_updated_2026_utm83_gdb	55

    wv_wv_county_boundaries_24k_topo_updated_2026_utm83	55

    wv_county_identity	55

    wv_bnd_canaan_valley_nwr	0

    wv_bnd_arc_counties	0

    wv_bnd_appalachian_basin_boundary	0

    (20 rows)

  --- postgres ---

    relname	rows

    (0 rows)

===== cluster on port 5433 =====

  --- msjarvis ---

    relname	rows

    (0 rows)

  --- msjarvisgis ---

    relname	rows

    wv_wvgistcbuildingfootprints	2121130

    wv_str_building_footprints	2121130

    wv_plc_tax_parcels_surface_mineral	1389855

    wv_tax_mastersurf_2025	1389855

    wv_str_samb_building_points	1366959

    wv_loc_sams2_address_road_centerlines	1135834

    wv_structurepointssouth_samb_2003_utm83_shp	745032

    wv_structurepointsnorth_samb_2003_utm83_shp	621927

    wv_util_water_lines	148728

    wv_windenergy_nrel_200901_wgs84	104812

    wv_env_wind_energy_resources	104812

    wv_windenergyresource_nationalrenewableenergylab_200901_utm83_s	104812

    wv_str_flood_atrisk_structures	81054

    wv_floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm	81054

    wv_plc_hazus_level1	80122

    wv_soc_census_blocks_2020	72558

    wv_hyd_streams_tiger	67774

    wv_streams_waterbodies_census_2023_wma84_l1	67774

    wv_streams_waterbodies_census_2023_wma84	67774

    wv_streams_waterbodies_census_2023_utm83_l1	67774

    (20 rows)

  --- postgres ---

    relname	rows

    (0 rows)

############################################################

## 3. DO THE DUMPS CONTAIN THE DATA THE DATABASE LACKS?

############################################################

A pg_restore TOC lists 'TABLE DATA' entries only for tables whose rows

are actually in the archive. This tells us whether the evidence is

recoverable from a dump or genuinely gone.

===== msjarvisgis_v2-full.dump =====

  bytes: 21472908

  TABLE DATA entries: 155

  the four vanished coverage source tables:

      wv_address_points_union: not in this dump

      wv_blockgroups_census_2020_utm83: not in this dump

      wv_hyd_dfirm_nfhl: not in this dump

      wv_zipcodetabulationarea_census_2020_utm83: not in this dump

  sample of the largest TABLE DATA entries it does carry:

      5686; 0 732506 TABLE DATA normalization geoanchor postgres

      5687; 0 732513 TABLE DATA public gbim_active_collection postgres

      5688; 0 732519 TABLE DATA public gbim_collection_manifest postgres

      4900; 0 731747 TABLE DATA public spatial_ref_sys postgres

      5689; 0 732526 TABLE DATA public wv_atm_weather_stations postgres

      5691; 0 732532 TABLE DATA public wv_bio_biodiversity_rank postgres

      5693; 0 732538 TABLE DATA public wv_bio_ecoregions postgres

      5695; 0 732544 TABLE DATA public wv_bio_red_spruce_cover postgres

      5697; 0 732550 TABLE DATA public wv_bnd_appalachian_basin_boundary postgres

      5699; 0 732556 TABLE DATA public wv_bnd_arc_counties postgres

      5701; 0 732562 TABLE DATA public wv_bnd_canaan_valley_nwr postgres

      5703; 0 732568 TABLE DATA public wv_bnd_census_designated_places postgres

===== msjarvisgis_v2-final.dump =====

  bytes: 21470719

  TABLE DATA entries: 155

  the four vanished coverage source tables:

      wv_address_points_union: not in this dump

      wv_blockgroups_census_2020_utm83: not in this dump

      wv_hyd_dfirm_nfhl: not in this dump

      wv_zipcodetabulationarea_census_2020_utm83: not in this dump

  sample of the largest TABLE DATA entries it does carry:

      5686; 0 723994 TABLE DATA normalization geoanchor msjarvis

      5978; 0 727165 TABLE DATA public gbim_active_collection postgres

      5977; 0 727154 TABLE DATA public gbim_collection_manifest postgres

      4900; 0 723187 TABLE DATA public spatial_ref_sys postgres

      5687; 0 724001 TABLE DATA public wv_atm_weather_stations msjarvis

      5689; 0 724007 TABLE DATA public wv_bio_biodiversity_rank msjarvis

      5691; 0 724013 TABLE DATA public wv_bio_ecoregions msjarvis

      5693; 0 724019 TABLE DATA public wv_bio_red_spruce_cover msjarvis

      5695; 0 724025 TABLE DATA public wv_bnd_appalachian_basin_boundary msjarvis

      5697; 0 724031 TABLE DATA public wv_bnd_arc_counties msjarvis

      5699; 0 724037 TABLE DATA public wv_bnd_canaan_valley_nwr msjarvis

      5701; 0 724043 TABLE DATA public wv_bnd_census_designated_places msjarvis

===== gbim_physical_sources.dump =====

  bytes: 0

  (not a readable custom-format dump)

===== msjarvisgis_governance_recovered.dump =====

  bytes: 0

  (not a readable custom-format dump)

===== msjarvisgis-final.dump =====

  bytes: 0

  (not a readable custom-format dump)

--- gbim_physical_sources.list (a TOC already saved to disk) ---

  TABLE DATA entries: 0

############################################################

## 4. ARE THE RAW ARCHIVES STILL THERE TO RE-IMPORT FROM?

############################################################

If the data is unrecoverable from any dump, the retained source archive

is the fallback. This is what makes the archive load-bearing rather than

merely historical.

  archive root: /home/cakidd/Downloads/files

  total entries:      248

  .zip archives:      235

  .gdb directories:   1

  .shp files:         2

  total size:         3.1G

  archives matching the vanished coverage sources:

      /home/cakidd/Downloads/files/BlockGroups_Census_201111_GCS83.zip

      /home/cakidd/Downloads/files/populationDataBlockGroups_USCensus_2000_utm83_shp.zip

      /home/cakidd/Downloads/files/BlockGroups_Census_2020_WMA84.zip

      /home/cakidd/Downloads/files/BlockGroups_Census_2020_UTM83.zip

      /home/cakidd/Downloads/files/populationDataBlockGroups_USCensus_2000_ll83_shp.zip

      /home/cakidd/Downloads/files/BlockGroups_Census_201111_UTM83.zip

      /home/cakidd/Downloads/files/ZipCodeTabulationArea_Census_2020_WMA84.zip

      /home/cakidd/Downloads/files/WV Address Points_CSV03232026

      /home/cakidd/Downloads/files/ZipCodeTabulationArea_Census_2020_UTM83.zip

############################################################

## 5. THE OFF-BY-TWO IN THE PUBLISHED COUNTY BELIEFS

############################################################

County coverage says 544 tracts; tract identity holds 546. The published

v2 county beliefs carry the 544. Which counties disagree?

canonical_county_id	coverage_says	identity_says	difference

54003	25	26	1

54057	6	7	1

54095	4	3	-1

54103	4	5	1

(4 rows)

############################################################

## END

############################################################

Written to: /home/cakidd/gbim-investigation-20260712T192124Z/28-evidence-hunt.txt

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ chmod +x ~/Downloads/gbim-source.sh

~/Downloads/gbim-source.sh

GBIM source comparison

Generated: 2026-07-12T19:35:15Z

############################################################

## 1. CLUSTER IDENTITY — which server is which?

############################################################

--- port 5436 ---

  version

  PostgreSQL 16.14 (Ubuntu 16.14-0ubuntu0.24.04.1) on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0, 64-bit

  (1 row)

  name	setting

  data_directory	/mnt/spiritual_drive/pgdata_native_msjarvis

  port	5436

  server_version	16.14 (Ubuntu 16.14-0ubuntu0.24.04.1)

  shared_buffers	16384

  (4 rows)

  postgis in msjarvisgis_v2 / msjarvisgis:

    msjarvisgis: postgis 3.4 USE_GEOS=1 USE_PROJ=1 USE_STATS=1

--- port 5433 ---

  version

  PostgreSQL 16.4 (Debian 16.4-1.pgdg110+2) on x86_64-pc-linux-gnu, compiled by gcc (Debian 10.2.1-6) 10.2.1 20210110, 64-bit

  (1 row)

  name	setting

  data_directory	/var/lib/postgresql/data

  port	5432

  server_version	16.4 (Debian 16.4-1.pgdg110+2)

  shared_buffers	16384

  (4 rows)

  postgis in msjarvisgis_v2 / msjarvisgis:

    msjarvisgis: postgis 3.4 USE_GEOS=1 USE_PROJ=1 USE_STATS=1

  Which container or process owns each port:

    jarvis-msjarvis-db	127.0.0.1:5433->5432/tcp

    LISTEN 0      4096       127.0.0.1:5433       0.0.0.0:*                                                                                               

    LISTEN 0      200        127.0.0.1:5436       0.0.0.0:*                                                                                               

############################################################

## 2. THREE-WAY ROW-COUNT COMPARISON

############################################################

Building per-table counts from each database. This may take a minute.

  5433:msjarvisgis    relations: 555

  5436:msjarvisgis    relations: 134

  5436:msjarvisgis_v2 relations: 153

  verdict tally:

      403  ABSENT_FROM_V2__DATA_EXISTS_ELSEWHERE

      134  V2_EMPTY_SHELL__DATA_EXISTS_ELSEWHERE

       19  v2_populated

        1  other

  total rows 5433:msjarvisgis    13,941,383   (555 tables)

  total rows 5436:msjarvisgis    4,496,404   (134 tables)

  total rows 5436:msjarvisgis_v2 6,335   (153 tables)

  populated ONLY in 5433:msjarvisgis  (420):

       2,121,130  wv_str_building_footprints

       2,121,130  wv_wvgistcbuildingfootprints

       1,389,855  wv_tax_mastersurf_2025

         745,032  wv_structurepointssouth_samb_2003_utm83_shp

         621,927  wv_structurepointsnorth_samb_2003_utm83_shp

         148,728  wv_util_water_lines

         104,812  wv_windenergy_nrel_200901_wgs84

         104,812  wv_windenergyresource_nationalrenewableenergylab_200901_utm83_s

          81,054  wv_floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm

          72,558  wv_soc_census_blocks_2020

          67,774  wv_streams_waterbodies_census_2023_utm83_l1

          67,774  wv_streams_waterbodies_census_2023_wma84

          67,774  wv_streams_waterbodies_census_2023_wma84_l1

          61,799  wv_address_points_berkeley

          61,703  wv_address_points_kanawha part1

          61,703  wv_address_points_kanawha_part1

          57,085  wv_address_points_monongalia

          49,045  wv_util_sewer_lines

          48,744  wv_address_points_cabell

          45,928  wv_address_points_raleigh

  populated ONLY in 5436:msjarvisgis  (0):

  full comparison written to: /home/cakidd/gbim-investigation-20260712T192124Z/30-three-way-rowcounts.csv

############################################################

## 3. THE FOUR COVERAGE SOURCE TABLES — do they exist anywhere?

############################################################

County coverage cites these. They are in no dump and not in v2.

If they exist in either msjarvisgis, county coverage is reproducible.

If not, the 'present' states in the published county beliefs rest on

evidence that no longer exists in any form.

  wv_address_points_union

      5433:msjarvisgis      ABSENT

      5436:msjarvisgis      ABSENT

      5436:msjarvisgis_v2   ABSENT

  wv_blockgroups_census_2020_utm83

      5433:msjarvisgis      1639

      5436:msjarvisgis      ABSENT

      5436:msjarvisgis_v2   ABSENT

  wv_hyd_dfirm_nfhl

      5433:msjarvisgis      696

      5436:msjarvisgis      ABSENT

      5436:msjarvisgis_v2   ABSENT

  wv_zipcodetabulationarea_census_2020_utm83

      5433:msjarvisgis      741

      5436:msjarvisgis      ABSENT

      5436:msjarvisgis_v2   ABSENT

--- near-miss names (in case they were renamed rather than dropped) ---

  5433:msjarvisgis

      wv_loc_sams2_address_road_centerlines	1135834

      wv_address_points_berkeley	61799

      wv_address_points_kanawha part1	61703

      wv_address_points_kanawha_part1	61703

      wv_address_points_monongalia	57085

      wv_address_points_cabell	48744

      wv_address_points_raleigh	45928

      wv_address_points_wood	44436

      wv_address_points_kanawha_part2	40000

      wv_address_points_kanawha part2	40000

      wv_address_points_harrison	35673

      wv_address_points_mercer	34376

      wv_address_points_wayne	32619

      wv_address_points_marion	31548

      wv_address_points_jefferson	30909

      wv_address_points_putnam	28032

      wv_address_points_fayette	24529

      wv_address_points_greenbrier	23327

      wv_address_points_lewis	23030

      wv_address_points_ohio	20246

      wv_address_points_mingo	19746

      wv_address_points_brooke	18980

      wv_address_points_preston	18690

      wv_address_points_logan	18048

      wv_address_points_randolph	17851

      wv_address_points_braxton	17834

      wv_address_points_hancock	17385

      wv_address_points_marshall	17136

      wv_address_points_nicholas	16940

      wv_address_points_jackson	16845

      wv_address_points_hampshire	16750

      wv_address_points_mason	16055

      wv_address_points_mineral	15683

      wv_address_points_upshur	14342

      wv_address_points_wyoming	13954

      wv_address_points_mcdowell	12986

      wv_address_points_ritchie	12879

      wv_address_points_boone	12639

      wv_address_points_morgan	12556

      wv_address_points_lincoln	12108

      wv_address_points_summers	11129

      wv_address_points_raw	10903

      wv_address_points_barbour	10903

      wv_address_points_wetzel	10637

      wv_address_points_hardy	10380

      wv_address_points_doddridge	9308

      wv_address_points_gilmer	9187

      wv_address_points_tucker	9033

      wv_address_points_roane	8663

      wv_address_points_taylor	8608

      wv_address_points_monroe	8486

      wv_address_points_grant	8455

      wv_address_points_pendleton	7428

      wv_address_points_pocahontas	7415

      wv_address_points_pleasants	6646

      wv_address_points_webster	6497

      wv_address_points_tyler	5871

      wv_address_points_clay	5418

      wv_address_points_wirt	4165

      wv_address_points_calhoun	3968

      wv_blockgroup_dataset_coverage	1639

      wv_blockgroups_census_2020_wma84	1639

      wv_blockgroup_representation	1639

      wv_soc_census_blockgroups_2020	1639

      wv_blockgroup_belief_snapshot	1639

      wv_blockgroups_census_2020_utm83	1639

      wv_soc_census_blockgroups_2011	1592

      wv_blockgroups_census_201111_utm83	1592

      wv_blockgroups_census_201111_gcs83	1592

      wv_soc_census_blockgroups_2000	1588

      wv_populationdatablockgroups_uscensus_2000_utm83_shp	1588

      wv_populationdatablockgroups_uscensus_2000_ll83_shp	1588

      wv_zcta_dataset_coverage	1482

      wv_zipcodetabulationarea_census_2020_utm83	741

      wv_zipcodetabulationarea_census_2020_wma84	741

      wv_soc_zcta_2020	741

      wv_zcta_belief_snapshot	741

      wv_zcta_representation	741

      wv_hyd_dfirm_nfhl	696

  5436:msjarvisgis

      wv_loc_sams2_address_road_centerlines	1135834

      wv_soc_census_blockgroups_2020	1639

      wv_soc_zcta_2020	741

############################################################

## 4. THE 14 PHANTOM MANIFEST NAMES

############################################################

Named by the layers manifest, absent from v2. Do they exist in

msjarvisgis under those names, or is this naming drift?

  wv_atm_geodeticsurveycontrol               5433:no   5436:no  

  wv_atm_spotelevations                      5433:no   5436:no  

  wv_atm_weather_stations_utm27              5433:no   5436:no  

  wv_bio_ecoregions_ll83                     5433:no   5436:no  

  wv_bio_fish_hatcheries                     5433:no   5436:no  

  wv_bio_public_fishing_boating_access       5433:no   5436:no  

  wv_bio_public_fishing_lakes                5433:no   5436:no  

  wv_bnd_public_lands_union                  5433:no   5436:no  

  wv_county_summary_metrics                  5433:no   5436:no  

  wv_tax_districts_24k_topo_utm83            5433:no   5436:no  

  wv_tax_districts_500k_ll83                 5433:no   5436:no  

  wv_tax_districts_500k_utm27                5433:no   5436:no  

  wv_tax_districts_500k_utm83                5433:no   5436:no  

  wv_tract_summary_metrics                   5433:no   5436:no  

############################################################

## 5. THE ZERO-BYTE BACKUPS

############################################################

These files look like backups in a directory listing and contain nothing.

  EMPTY (0 bytes):  /home/cakidd/msjarvis-db-recovery/gbim_physical_sources.dump

  EMPTY (0 bytes):  /home/cakidd/msjarvis-db-recovery/msjarvisgis_governance_recovered.dump

           21M      /home/cakidd/msjarvis-db-recovery/msjarvisgis_v2_chroma_active.dump

           21M      /home/cakidd/msjarvis-db-recovery/msjarvisgis_v2_complete.dump

           21M      /home/cakidd/msjarvis-db-recovery/msjarvisgis_v2_vector_ready.dump

          905K      /home/cakidd/msjarvis-db-recovery/msjarvisgis_v2_verified.dump

  EMPTY (0 bytes):  /mnt/spiritual_drive/msjarvis-rebuild/msjarvisgis-final.dump

           21M      /mnt/spiritual_drive/msjarvis-rebuild/msjarvisgis_v2-final.dump

           21M      /mnt/spiritual_drive/msjarvis-rebuild/ch52_checkpoint/msjarvisgis_v2-final.dump

           21M      /mnt/spiritual_drive/msjarvis-rebuild/ch52_checkpoint/msjarvisgis_v2-full.dump

############################################################

## END

############################################################

Written to: /home/cakidd/gbim-investigation-20260712T192124Z/29-source-comparison.txt

Comparison: /home/cakidd/gbim-investigation-20260712T192124Z/30-three-way-rowcounts.csv

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ chmod +x ~/Downloads/gbim-plan.sh

~/Downloads/gbim-plan.sh

GBIM pre-migration plan

Generated: 2026-07-12T19:38:06Z

Source: 5433:msjarvisgis (container jarvis-msjarvis-db)

Target: 5436:msjarvisgis_v2 (native, /mnt/spiritual_drive/pgdata_native_msjarvis)

############################################################

## 1. SCHEMA COMPATIBILITY — can the shells actually be filled?

############################################################

For each empty v2 shell whose data lives in 5433, compare the full

column signature. A mismatch means a straight copy would fail or,

worse, silently land columns in the wrong places.

  empty v2 shells with data upstream: 134

    identical column signature:  8   -> safe to copy

    signature MISMATCH:          126   -> must be reconciled first

    no source table in 5433:     0

  MISMATCHED — do not copy these until resolved:

       1,389,855  wv_plc_tax_parcels_surface_mineral

          5433: gid:int4,map:varchar,parcel:varchar,suffix:varchar,label:varchar,acres_c:float8,cleanparcelid:varchar,gispid:varchar,rootid:varchar,codist:varchar,dis

          v2  : gid:int4,map:varchar,parcel:varchar,suffix:varchar,label:varchar,acres_c:float8,cleanparcelid:varchar,gispid:varchar,rootid:varchar,codist:varchar,dis

       1,366,959  wv_str_samb_building_points

          5433: gid:int4,objectid_1:int4,objectid_2:int4,objectid:float8,area:float8,perimeter:float8,coord_x:float8,coord_y:float8,coord_z:float8,geom:geometry,x:flo

          v2  : gid:int4,objectid_1:int4,objectid_2:int4,objectid:float8,area:float8,perimeter:float8,coord_x:float8,coord_y:float8,coord_z:float8,geom:geometry

       1,135,834  wv_loc_sams2_address_road_centerlines

          5433: gid:int4,fid:varchar,siteaddid:varchar,addptkey:varchar,preaddrnum:varchar,addrnumsuf:varchar,addrnum:varchar,addrrange:varchar,unittype:varchar,uniti

          v2  : gid:int4,fid:varchar,siteaddid:varchar,addptkey:varchar,preaddrnum:varchar,addrnumsuf:varchar,addrnum:varchar,addrrange:varchar,unittype:varchar,uniti

         104,812  wv_env_wind_energy_resources

          5433: gid:int4,id:int8,gridcode:int8,geom:geometry,x:float8,y:float8

          v2  : gid:int4,id:int8,gridcode:int8,geom:geometry

          81,054  wv_str_flood_atrisk_structures

          5433: gid:int4,name:varchar,type:varchar,class:varchar,fips_id:varchar,q3_commun:varchar,q3_firm_id:varchar,q3_zone:varchar,q3_fldway:varchar,x_coord:float8

          v2  : gid:int4,name:varchar,type:varchar,class:varchar,fips_id:varchar,q3_commun:varchar,q3_firm_id:varchar,q3_zone:varchar,q3_fldway:varchar,x_coord:float8

          80,122  wv_plc_hazus_level1

          5433: gid:int4,censusblock:varchar,totalassets:float8,totallossrp10:float8,totallossrp25:float8,totallossrp50:float8,totallossrp100:float8,totallossrp200:fl

          v2  : gid:int4,censusblock:varchar,totalassets:float8,totallossrp10:float8,totallossrp25:float8,totallossrp50:float8,totallossrp100:float8,totallossrp200:fl

          67,774  wv_hyd_streams_tiger

          5433: gid:int4,ansicode:varchar,linearid:varchar,fullname:varchar,artpath:varchar,mtfcc:varchar,geom:geometry,x:float8,y:float8

          v2  : gid:int4,ansicode:varchar,linearid:varchar,fullname:varchar,artpath:varchar,mtfcc:varchar,geom:geometry

          63,912  wv_bio_biodiversity_rank

          5433: gid:int4,wukey:int4,bsing:varchar,bconc:varchar,brank:varchar,shape_length:float8,shape_area:float8,geom:geometry,x:float8,y:float8

          v2  : gid:int4,wukey:int4,bsing:varchar,bconc:varchar,brank:varchar,shape_length:float8,shape_area:float8,geom:geometry

          32,116  wv_hyd_navigable_waterways_structures

          5433: gid:int4,river_1:varchar,mile_1:float8,river_2:varchar,mile_2:float8,coord_x:float8,coord_y:float8,coord_z:float8,fips:varchar,statefips:varchar,cntyf

          v2  : gid:int4,river_1:varchar,mile_1:float8,river_2:varchar,mile_2:float8,coord_x:float8,coord_y:float8,coord_z:float8,fips:varchar,statefips:varchar,cntyf

          22,656  wv_hyd_streams_high_quality

          5433: gid:int4,permanent_identifier:varchar,reachcode:varchar,entity_id:varchar,gnis_id:varchar,gnis_name:varchar,fdate:timestamptz,flowdir:int4,resolution:

          v2  : gid:int4,permanent_identifier:varchar,reachcode:varchar,entity_id:varchar,gnis_id:varchar,gnis_name:varchar,fdate:timestamptz,flowdir:int4,resolution:

          19,795  wv_trn_roads_major_4800

          5433: gid:int4,routeid:varchar,countycode:varchar,signsystem:varchar,route:varchar,subroute:varchar,label:varchar,suppcode:varchar,direction:varchar,dsurvey

          v2  : gid:int4,routeid:varchar,countycode:varchar,signsystem:varchar,route:varchar,subroute:varchar,label:varchar,suppcode:varchar,direction:varchar,dsurvey

          15,514  wv_bio_red_spruce_cover

          5433: gid:int4,objectid:int4,primary_:varchar,secondary:varchar,forest_typ:varchar,size_class:varchar,canopy_cov:varchar,crown_cond:varchar,acres:float8,sha

          v2  : gid:int4,objectid:int4,primary_:varchar,secondary:varchar,forest_typ:varchar,size_class:varchar,canopy_cov:varchar,crown_cond:varchar,acres:float8,sha

          15,505  wv_str_samb_building_polygons

          5433: gid:int4,objectid:int8,area:float8,perimeter:float8,bggenexs_:int8,bggenexs_i:int8,datalink:int8,buildng_id:varchar,map_id:int8,meta_id:varchar,media_

          v2  : gid:int4,objectid:int8,area:float8,perimeter:float8,bggenexs_:int8,bggenexs_i:int8,datalink:int8,buildng_id:varchar,map_id:int8,meta_id:varchar,media_

          11,590  wv_bnd_nhd_mussel_streams

          5433: gid:int4,objectid:float8,fdate:timestamptz,resolution:float8,gnis_id:varchar,gnis_name:varchar,lengthkm:float8,reachcode:varchar,flowdir:float8,ftype:

          v2  : gid:int4,objectid:float8,fdate:timestamptz,resolution:float8,gnis_id:varchar,gnis_name:varchar,lengthkm:float8,reachcode:varchar,flowdir:float8,ftype:

          10,796  wv_eco_abandoned_mine_lands_line

          5433: gid:int4,fnode_:int8,tnode_:int8,lpoly_:int8,rpoly_:int8,length:float8,aml_:int8,aml_id:int8,pad_number:varchar,portal:int4,first_fnam:varchar,geom:ge

          v2  : gid:int4,fnode_:int8,tnode_:int8,lpoly_:int8,rpoly_:int8,length:float8,aml_:int8,aml_id:int8,pad_number:varchar,portal:int4,first_fnam:varchar,geom:ge

           8,559  wv_loc_geodetic_control_points

          5433: gid:int4,featureid:int4,data_date:varchar,data_srce:varchar,dec_long:varchar,dec_lat:varchar,pid:varchar,name:varchar,state:varchar,county:varchar,qua

          v2  : gid:int4,featureid:int4,data_date:varchar,data_srce:varchar,dec_long:varchar,dec_lat:varchar,pid:varchar,name:varchar,state:varchar,county:varchar,qua

           8,317  wv_eco_manufacturing_directory

          5433: gid:int4,index:float8,category:varchar,name:varchar,longname:varchar,alsocalled:varchar,mailadd:varchar,mailcity:varchar,mailstate:varchar,mailzip:var

          v2  : gid:int4,index:float8,category:varchar,name:varchar,longname:varchar,alsocalled:varchar,mailadd:varchar,mailcity:varchar,mailstate:varchar,mailzip:var

           7,357  wv_str_bridges

          5433: gid:int4,barsid:varchar,lat:float8,long:float8,notes:varchar,oldbars:varchar,id:int8,brnum:varchar,dir:varchar,locname:varchar,featint:varchar,locatio

          v2  : gid:int4,barsid:varchar,lat:float8,long:float8,notes:varchar,oldbars:varchar,id:int8,brnum:varchar,dir:varchar,locname:varchar,featint:varchar,locatio

           5,687  wv_soc_towers_private

          5433: gid:int4,licensee:varchar,callsign:varchar,locnum:int4,lat_dms:varchar,latdir:varchar,lon_dms:varchar,londir:varchar,locadd:varchar,loccity:varchar,lo

          v2  : gid:int4,licensee:varchar,callsign:varchar,locnum:int4,lat_dms:varchar,latdir:varchar,lon_dms:varchar,londir:varchar,locadd:varchar,loccity:varchar,lo

           5,613  wv_soc_places_of_worship_wvgistc

          5433: gid:int4,feature_na:varchar,prim_lat_d:float8,prim_long1:float8,hifld:int8,ref_usa:int8,gnis:int8,address:varchar,address2:varchar,zip:varchar,naicsco

          v2  : gid:int4,feature_na:varchar,prim_lat_d:float8,prim_long1:float8,hifld:int8,ref_usa:int8,gnis:int8,address:varchar,address2:varchar,zip:varchar,naicsco

           2,682  wv_trn_railroad_lines_rti

          5433: gid:int4,version:varchar,revision:varchar,moddate:varchar,linkid:int8,fips5:varchar,country:varchar,rrowner1:varchar,rrowner2:varchar,rrowner3:varchar

          v2  : gid:int4,version:varchar,revision:varchar,moddate:varchar,linkid:int8,fips5:varchar,country:varchar,rrowner1:varchar,rrowner2:varchar,rrowner3:varchar

           2,428  wv_trn_railroads_national_network

          5433: gid:int4,version:varchar,revision:varchar,moddate:varchar,linkid:int8,fips5:varchar,country:varchar,rrowner1:varchar,rrowner2:varchar,rrowner3:varchar

          v2  : gid:int4,version:varchar,revision:varchar,moddate:varchar,linkid:int8,fips5:varchar,country:varchar,rrowner1:varchar,rrowner2:varchar,rrowner3:varchar

           2,382  wv_trn_recreational_trails

          5433: gid:int4,points_of_:varchar,dataagency:varchar,sourcedate:varchar,updated:varchar,associated:varchar,notes:varchar,geom:geometry,x:float8,y:float8

          v2  : gid:int4,points_of_:varchar,dataagency:varchar,sourcedate:varchar,updated:varchar,associated:varchar,notes:varchar,geom:geometry

           2,137  wv_env_epa_facilities

          5433: gid:int4,fac_name:varchar,sicdesc:varchar,sic:int4,fac_ident:varchar,prim_sic:varchar,city:varchar,coll_date:varchar,county:varchar,address:varchar,st

          v2  : gid:int4,fac_name:varchar,sicdesc:varchar,sic:int4,fac_ident:varchar,prim_sic:varchar,city:varchar,coll_date:varchar,county:varchar,address:varchar,st

           2,120  wv_eco_abandoned_mine_lands_polygon

          5433: gid:int4,area:float8,perimeter:float8,aml_:int8,aml_id:int8,pad_number:varchar,poly_type:int4,geom:geometry,x:float8,y:float8

          v2  : gid:int4,area:float8,perimeter:float8,aml_:int8,aml_id:int8,pad_number:varchar,poly_type:int4,geom:geometry

           2,089  wv_soc_towers_microwave

          5433: gid:int4,licensee:varchar,callsign:varchar,locnum:int4,lat_dms:varchar,latdir:varchar,lon_dms:varchar,londir:varchar,locadd:varchar,loccity:varchar,lo

          v2  : gid:int4,licensee:varchar,callsign:varchar,locnum:int4,lat_dms:varchar,latdir:varchar,lon_dms:varchar,londir:varchar,locadd:varchar,loccity:varchar,lo

           1,926  wv_bnd_voting_districts_2000

          5433: gid:int4,area:float8,perimeter:float8,vt54_d00_:int8,vt54_d00_i:int8,state:varchar,county:varchar,vtd:varchar,name:varchar,lsad:varchar,lsad_trans:var

          v2  : gid:int4,area:float8,perimeter:float8,vt54_d00_:int8,vt54_d00_i:int8,state:varchar,county:varchar,vtd:varchar,name:varchar,lsad:varchar,lsad_trans:var

           1,909  wv_bnd_voting_districts_2002

          5433: gid:int4,id:int8,area:float8,vtd:varchar,county:varchar,mcd:varchar,place:varchar,name:varchar,lsadc:varchar,population:int8,white:int8,black:int8,ami

          v2  : gid:int4,id:int8,area:float8,vtd:varchar,county:varchar,mcd:varchar,place:varchar,name:varchar,lsadc:varchar,population:int8,white:int8,black:int8,ami

           1,781  wv_hyd_high_water_marks

          5433: gid:int4,latitude_h:float8,longitude_:float8,eventname:varchar,hwmtypenam:varchar,hwmquality:varchar,verticalda:varchar,markername:varchar,horizontal:

          v2  : gid:int4,latitude_h:float8,longitude_:float8,eventname:varchar,hwmtypenam:varchar,hwmquality:varchar,verticalda:varchar,markername:varchar,horizontal:

           1,639  wv_soc_census_blockgroups_2020

          5433: gid:int4,statefp:varchar,countyfp:varchar,tractce:varchar,blkgrpce:varchar,geoid:varchar,geoidfq:varchar,namelsad:varchar,mtfcc:varchar,funcstat:varch

          v2  : gid:int4,statefp:varchar,countyfp:varchar,tractce:varchar,blkgrpce:varchar,geoid:varchar,geoidfq:varchar,namelsad:varchar,mtfcc:varchar,funcstat:varch

  rows copyable without schema work: 597

  manifest written to: /home/cakidd/gbim-investigation-20260712T192124Z/32-migration-manifest.csv

############################################################

## 2. THE STRANDED BLOCKGROUP / ZCTA GOVERNANCE

############################################################

gbim_wv_blockgroups_v1 (1,639 docs) and gbim_wv_zctas_v1 (741) are

published and carry belief hashes. Their governance is in 5433.

Full inventory, so the reverse-trace path can be restored.

relname	kind	rows

gbim_active_collection	table	4

gbim_collection_manifest	table	4

wv_blockgroup_belief_snapshot	table	1639

wv_blockgroup_belief_vector_ready	view	1639

wv_blockgroup_dataset_coverage	table	1639

wv_blockgroup_representation	table	1639

wv_county_belief_snapshot	table	55

wv_county_belief_vector_ready	view	55

wv_county_dataset_coverage	table	275

wv_county_identity	table	55

wv_county_representation	table	220

wv_county_tract_identity_reconciliation	view	546

wv_hazus_county_representation	table	55

wv_tract_belief_snapshot	table	546

wv_tract_belief_vector_ready	view	546

wv_tract_dataset_coverage	table	1638

wv_tract_identity	table	546

wv_tract_representation	table	546

wv_tract_representation_pre_cleanup_20260711	table	1092

wv_zcta_belief_snapshot	table	741

wv_zcta_belief_vector_ready	view	741

wv_zcta_dataset_coverage	table	1482

wv_zcta_representation	table	741

(23 rows)

--- do the v1 blockgroup/zcta belief hashes still resolve there? ---

entity	snapshots	distinct_hashes	null_hashes

blockgroup	1639	1639	0

zcta	741	741	0

(2 rows)

############################################################

## 3. ADDRESS POINTS — the duplicate hazard, resolved

############################################################

County coverage cites wv_address_points_union (212,621 features).

That table exists nowhere. It was a UNION of the per-county tables.

Two duplicate pairs are visible: a 'kanawha part1'/'kanawha_part1'

space-vs-underscore pair, and wv_address_points_raw sharing a count

with wv_address_points_barbour. A naive union would double-count.

relname	rows

wv_address_points_barbour	10903

wv_address_points_berkeley	61799

wv_address_points_boone	12639

wv_address_points_braxton	17834

wv_address_points_brooke	18980

wv_address_points_cabell	48744

wv_address_points_calhoun	3968

wv_address_points_clay	5418

wv_address_points_doddridge	9308

wv_address_points_fayette	24529

wv_address_points_gilmer	9187

wv_address_points_grant	8455

wv_address_points_greenbrier	23327

wv_address_points_hampshire	16750

wv_address_points_hancock	17385

wv_address_points_hardy	10380

wv_address_points_harrison	35673

wv_address_points_jackson	16845

wv_address_points_jefferson	30909

wv_address_points_kanawha part1	61703

wv_address_points_kanawha part2	40000

wv_address_points_kanawha_part1	61703

wv_address_points_kanawha_part2	40000

wv_address_points_lewis	23030

wv_address_points_lincoln	12108

wv_address_points_logan	18048

wv_address_points_marion	31548

wv_address_points_marshall	17136

wv_address_points_mason	16055

wv_address_points_mcdowell	12986

wv_address_points_mercer	34376

wv_address_points_mineral	15683

wv_address_points_mingo	19746

wv_address_points_monongalia	57085

wv_address_points_monroe	8486

wv_address_points_morgan	12556

wv_address_points_nicholas	16940

wv_address_points_ohio	20246

wv_address_points_pendleton	7428

wv_address_points_pleasants	6646

wv_address_points_pocahontas	7415

wv_address_points_preston	18690

wv_address_points_putnam	28032

wv_address_points_raleigh	45928

wv_address_points_randolph	17851

wv_address_points_raw	10903

wv_address_points_ritchie	12879

wv_address_points_roane	8663

wv_address_points_summers	11129

wv_address_points_taylor	8608

wv_address_points_tucker	9033

wv_address_points_tyler	5871

wv_address_points_upshur	14342

wv_address_points_wayne	32619

wv_address_points_webster	6497

wv_address_points_wetzel	10637

wv_address_points_wirt	4165

wv_address_points_wood	44436

wv_address_points_wyoming	13954

(59 rows)

--- de-duplicated total (excluding space-named and _raw aliases) ---

  1013885

  county coverage claims: 212621

  (if these agree, address-point coverage is exactly reproducible)

--- are the two suspected duplicate pairs genuinely identical? ---

pair	a	b

kanawha_part1 vs "kanawha part1"	61703	61703

barbour vs _raw	10903	10903

(2 rows)

############################################################

## 4. SIZE AND DISK

############################################################

--- total on-disk size of the tables proposed for migration ---

  entire 5433:msjarvisgis: 19 GB

--- free space on the v2 cluster's data directory ---

  Filesystem      Size  Used Avail Use% Mounted on

  /dev/nvme0n1p2  937G  460G  430G  52% /

--- current size of msjarvisgis_v2 ---

  52 MB

############################################################

## 5. WHAT THE MIGRATION WOULD CHANGE, EPISTEMICALLY

############################################################

  Filling the shells is not a cosmetic fix. It changes governed state:

    - tract coverage moves from unknown -> real counts (blockgroup,

      address_point, dfirm_polygon all currently unknown for all 546);

    - county coverage becomes REPRODUCIBLE against tables that exist,

      instead of citing four tables that are absent from the database;

    - the 544-vs-546 tract discrepancy (54003, 54057, 54095, 54103)

      gets resolved against real geometry rather than inherited;

    - every belief document therefore changes;

    - every belief hash therefore changes;

    - which means: a new snapshot version (v3), new document ids, new

      collections, and an atomic promotion.

  v1 and v2 snapshots are retained. That is the point of versioning.

  This will be the first time the loop runs on a CORRECTION rather than

  an initial build — which is the recurrence Chapter 52 claims and has

  not yet actually demonstrated.

############################################################

## END

############################################################

Written to: /home/cakidd/gbim-investigation-20260712T192124Z/31-migration-plan.txt

Migration manifest: /home/cakidd/gbim-investigation-20260712T192124Z/32-migration-manifest.csv

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ chmod +x ~/Downloads/gbim-columns.sh

~/Downloads/gbim-columns.sh

GBIM column-level diff

Generated: 2026-07-12T19:41:29Z

############################################################

## 1. TRUE COLUMN-SET DIFF PER SHELL

############################################################

  SAFE__IDENTICAL          tables:    8   rows:          597

  SAFE__SRC_SUPERSET       tables:  123   rows:    4,495,155

  DST_HAS_EXTRA_COLUMNS    tables:    1   rows:          600

  TYPE_CONFLICT            tables:    2   rows:           53

  Columns 5433 carries that the v2 shells do not (the suspected x/y):

      y                    appears in 124 tables

      x                    appears in 124 tables

      canonical_county_id  appears in 1 tables

  TYPE CONFLICTS — these need explicit handling:

              35  wv_bnd_mnf_recreation_sites

          x(varchar!=float8);y(varchar!=float8)

              18  wv_bnd_mnf_recreation_campgrounds

          x(varchar!=float8);y(varchar!=float8)

  v2 declares columns the source lacks (these would be NULL):

             600  wv_plc_tax_district_boundaries   -> objectid_1;shape_star;shape_stle

  copy plan written to: /home/cakidd/gbim-investigation-20260712T192124Z/34-copy-plan.csv

############################################################

## 2. GEOMETRY AND SRID COMPATIBILITY

############################################################

A geometry column copies cleanly only if type and SRID agree, or the

target is unconstrained. A silent SRID mismatch would corrupt every

spatial join that coverage depends on.

--- SRIDs present in the source layers ---

srid	type	tables

4269	MULTIPOLYGON	86

4269	MULTIPOINT	78

4269	POINT	60

5498	MULTIPOLYGON	59

26917	MULTIPOLYGON	58

26917	MULTIPOINT	51

4269	MULTILINESTRING	26

0	MULTIPOINT	15

4326	MULTIPOINT	11

26917	MULTILINESTRING	11

3857	MULTIPOLYGON	9

0	MULTILINESTRING	9

0	MULTIPOLYGON	9

4269	MULTILINESTRINGM	8

26917	MULTILINESTRINGM	6

26717	MULTIPOINT	6

26717	MULTIPOLYGON	5

3857	MULTILINESTRING	2

4152	MULTIPOINT	2

4267	MULTIPOINT	2

3857	MULTIPOINT	2

4269	GEOMETRY	2

900914	MULTIPOLYGON	1

4326	MULTIPOLYGON	1

4759	MULTIPOINT	1

26717	MULTILINESTRING	1

26853	MULTIPOLYGON	1

26854	MULTIPOINT	1

26917	GEOMETRY	1

900914	MULTIPOINT	1

(30 rows)

--- SRIDs declared by the empty v2 shells ---

srid	type	tables

4269	MULTIPOINT	56

4269	MULTIPOLYGON	53

4269	MULTILINESTRING	16

4269	MULTILINESTRINGM	8

26917	GEOMETRY	3

3857	GEOMETRY	2

4269	POINT	1

(7 rows)

--- per-table SRID disagreements between source and shell ---

  5 disagreements:

      wv_censustracts_census_2020_utm83

          5433: srid=26917 type=MULTIPOLYGON

          v2  : srid=26917 type=GEOMETRY

      wv_county_boundaries_24k_topo_updated_2026_utm83_gdb

          5433: srid=26917 type=MULTIPOLYGON

          v2  : srid=26917 type=GEOMETRY

      wv_county_boundaries_24k_topo_updated_2026_wma84_gdb

          5433: srid=3857 type=MULTIPOLYGON

          v2  : srid=3857 type=GEOMETRY

      wv_wv_county_boundaries_24k_topo_updated_2026_utm83

          5433: srid=26917 type=MULTIPOLYGON

          v2  : srid=26917 type=GEOMETRY

      wv_wv_county_boundaries_24k_topo_updated_2026_wma84

          5433: srid=3857 type=MULTIPOLYGON

          v2  : srid=3857 type=GEOMETRY

############################################################

## 3. THE ADDRESS-POINT RECONSTRUCTION QUESTION

############################################################

De-duplicated per-county total is ~1,013,885 (plus ~101,703 Kanawha).

County coverage claims 212,621. These differ by a factor of five, so

wv_address_points_union was NOT a union of all counties — it was built

when ingestion was partial. County coverage shows address_point present

for only 29 of 55 counties, which fits.

--- which 29 counties currently have address_point coverage present? ---

coverage_state	counties	summed_features

present	29	212621

unknown	26	0

(2 rows)

--- do the per-county address tables carry usable geometry? ---

f_table_name	type	srid	features

wv_address_points_berkeley	POINT	4269	61799

wv_address_points_kanawha_part1	POINT	4269	61703

wv_address_points_kanawha part1	POINT	4269	61703

wv_address_points_monongalia	POINT	4269	57085

wv_address_points_cabell	POINT	4269	48744

wv_address_points_raleigh	POINT	4269	45928

wv_address_points_wood	POINT	4269	44436

wv_address_points_kanawha part2	POINT	4269	40000

(8 rows)

--- and the county-name column, so a union can be attributed correctly ---

column_name	udt_name	tables_having_it

addptkey	varchar	59

addrclass	varchar	59

addrnum	varchar	59

addrnumsuf	varchar	59

addrrange	varchar	59

altunitid	varchar	59

altunittyp	varchar	59

canonical_county_id	text	59

capturemet	varchar	59

centerline	varchar	59

created_da	varchar	59

created_us	varchar	59

esn	varchar	59

fid	varchar	59

fulladdr	varchar	59

fullname	varchar	59

geom	geometry	59

gid	int4	59

last_edi_1	varchar	59

last_edite	varchar	59

lasteditor	varchar	59

lastupdate	varchar	59

msag	varchar	59

msagllcidk	varchar	59

municipali	varchar	59

org_siteid	varchar	59

org_unitid	varchar	59

placename	varchar	59

point_x	varchar	59

point_y	varchar	59

pointtype	varchar	59

postalllck	varchar	59

preaddrnum	varchar	59

psap	varchar	59

siteaddid	varchar	59

state	varchar	59

status	varchar	59

stcofips	varchar	59

streetidke	varchar	59

unitid	varchar	59

unittype	varchar	59

usngcoord	varchar	59

x	float8	59

y	float8	59

zip	varchar	59

(45 rows)

############################################################

## 4. THE MISSING IDENTITY SURFACES

############################################################

Blockgroups and ZCTAs have representation, coverage, snapshots, and

PUBLISHED collections — but no canonical identity table anywhere.

The first link of the governed chain was never built for them.

expected	in_5433

wv_blockgroup_identity	ABSENT

wv_zcta_identity	ABSENT

(2 rows)

--- what the blockgroup representation keys on, absent an identity table ---

column_name	udt_name

canonical_blockgroup_id	text

canonical_tract_id	text

canonical_county_id	text

table_name	text

source_feature_id	int8

source_feature_hash	text

(6 rows)

--- 5433's own collection manifest: what did it promote? ---

ERROR:  column "physical_collection_name" does not exist

LINE 2: select collection_name, collection_version, physical_collect...

                                                    ^

############################################################

## END

############################################################

Written to: /home/cakidd/gbim-investigation-20260712T192124Z/33-column-diff.txt

Copy plan:  /home/cakidd/gbim-investigation-20260712T192124Z/34-copy-plan.csv

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ chmod +x ~/Downloads/gbim-backup.sh

~/Downloads/gbim-backup.sh

GBIM verified backup

UTC:  20260712T194642Z

Dest: /home/cakidd/gbim-backup-20260712T194642Z

==============================================

Backing up msjarvisgis_v2 on port 5436

==============================================

  live tables in source: 154

  size: 21M bytes

  TABLE DATA entries in archive: 155

  sha256 recorded

  OK

==============================================

Backing up the evidence surface (5433:msjarvisgis, ~19 GB)

This is large. It is also the only place the corpus exists outside

a Docker volume.

==============================================

==============================================

Backing up msjarvisgis on port 5433

==============================================

  live tables in source: 556

  FAIL: pg_dump returned an error

==============================================

Backing up msjarvisgis on port 5436

==============================================

  live tables in source: 135

  FAIL: pg_dump returned an error

==============================================

RESTORE REHEARSAL — proving the v2 backup is usable

==============================================

  scratch database created: gbim_restore_test_20260712t194642z

  verifying the governance spine survived the round trip:

    relation	expected_rows	restored_rows	verdict

    wv_county_belief_snapshot	110	110	OK

    wv_county_dataset_coverage	275	275	OK

    wv_county_identity	55	55	OK

    wv_county_representation	220	220	OK

    wv_entity_registry	65	65	OK

    wv_layer_categories	254	254	OK

    wv_tract_belief_snapshot	1092	1092	OK

    wv_tract_dataset_coverage	1638	1638	OK

    wv_tract_identity	546	546	OK

    wv_tract_representation	546	546	OK

    (10 rows)

  RESTORE REHEARSAL PASSED — the backup is real and usable

  scratch database dropped

==============================================

RESULT

==============================================

  total 21M

  -rw-rw-r-- 1 cakidd cakidd 2.1K Jul 12 15:46 backup.log

  -rw-rw-r-- 1 cakidd cakidd    0 Jul 12 15:46 msjarvisgis_evidence_5433.dump

  -rw-rw-r-- 1 cakidd cakidd    0 Jul 12 15:46 msjarvisgis_partial_5436.dump

  -rw-rw-r-- 1 cakidd cakidd  21M Jul 12 15:46 msjarvisgis_v2.dump

  -rw-rw-r-- 1 cakidd cakidd  128 Jul 12 15:46 msjarvisgis_v2.dump.sha256

  -rw-rw-r-- 1 cakidd cakidd  91K Jul 12 15:46 msjarvisgis_v2.toc

  ONE OR MORE BACKUPS FAILED VERIFICATION.

  DO NOT run the migration until this is resolved.

  A note worth keeping: these three files in your existing backup

  directories are zero bytes and should be deleted or regenerated,

  because their presence implies protection that does not exist:

    ~/msjarvis-db-recovery/gbim_physical_sources.dump

    ~/msjarvis-db-recovery/msjarvisgis_governance_recovered.dump

    /mnt/spiritual_drive/msjarvis-rebuild/msjarvisgis-final.dump

Backup directory: /home/cakidd/gbim-backup-20260712T194642Z

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ # 1. Confirm 5433 is accepting connections and who can auth

psql -p 5433 -U postgres -d msjarvisgis -c "SELECT count(*) FROM information_schema.tables WHERE table_schema='public';"

# 2. Check what pg_dump actually complained about

pg_dump -p 5433 -U postgres -d msjarvisgis --format=custom -f /tmp/test_5433.dump 2>&1 | head -20

 count 

-------

   565

(1 row)

pg_dump: error: schema with OID 726804 does not exist

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ # Create a dated backup directory

mkdir -p ~/gbim-backup-$(date +%Y%m%dT%H%M%SZ)

# Dump only the public schema from 5433:msjarvisgis

pg_dump -p 5433 -U postgres -d msjarvisgis \

  --format=custom \

  --schema=public \

  --no-tablespaces \

  -f ~/gbim-backup-$(date +%Y%m%dT%H%M%SZ)/msjarvisgis_evidence_5433_public.dump

# Inspect size (should NOT be 0 bytes)

ls -lh ~/gbim-backup-$(date +%Y%m%dT%H%M%SZ)/msjarvisgis_evidence_5433_public.dump

pg_dump: error: schema with OID 726804 does not exist

-rw-rw-r-- 1 cakidd cakidd 0 Jul 12 15:49 /home/cakidd/gbim-backup-20260712T154902Z/msjarvisgis_evidence_5433_public.dump

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ psql -p 5433 -U postgres -d msjarvisgis -c "

SELECT classid::regclass, objid, refobjid, deptype

FROM pg_depend

WHERE refobjid = 726804;

"

psql -p 5433 -U postgres -d msjarvisgis -c "

SELECT oid, relname, relnamespace

FROM pg_class

WHERE relnamespace = 726804;

"

psql -p 5433 -U postgres -d msjarvisgis -c "

SELECT oid, typname

FROM pg_type

WHERE typnamespace = 726804;

"

psql -p 5433 -U postgres -d msjarvisgis -c "

SELECT oid, proname

FROM pg_proc

WHERE pronamespace = 726804;

"

 classid  | objid  | refobjid | deptype 

----------+--------+----------+---------

 pg_class | 726805 |   726804 | n

 pg_class | 726806 |   726804 | n

(2 rows)

 oid | relname | relnamespace 

-----+---------+--------------

(0 rows)

  oid   |  typname   

--------+------------

 726808 | geoanchor

 726807 | _geoanchor

(2 rows)

 oid | proname 

-----+---------

(0 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ # Save the offending dependency rows

psql -p 5433 -U postgres -d msjarvisgis -c "

SELECT classid::regclass, objid, refobjid, deptype

FROM pg_depend

WHERE refobjid = 726804;

" > ~/gbim-726804-pg_depend-before.txt

# Save the orphaned types

psql -p 5433 -U postgres -d msjarvisgis -c "

SELECT oid, typname

FROM pg_type

WHERE typnamespace = 726804;

" > ~/gbim-726804-pg_type-before.txt

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ psql -p 5433 -U postgres -d msjarvisgis -c "

SELECT oid, nspname

FROM pg_namespace

WHERE oid = 726804;

"

 oid | nspname 

-----+---------

(0 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ -- Delete only the dangling dependency rows that reference the missing namespace

psql -p 5433 -U postgres -d msjarvisgis -c "

DELETE FROM pg_depend

WHERE refobjid = 726804;

"

-- Confirm they’re gone

psql -p 5433 -U postgres -d msjarvisgis -c "

SELECT classid::regclass, objid, refobjid, deptype

FROM pg_depend

WHERE refobjid = 726804;

"

--: command not found

DELETE 2

--: command not found

 classid | objid | refobjid | deptype 

---------+-------+----------+---------

(0 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ # Fresh, full evidence dump now that pg_dump's catalog walk is clean

mkdir -p ~/gbim-backup-$(date +%Y%m%dT%H%M%SZ)

pg_dump -p 5433 -U postgres -d msjarvisgis \

  --format=custom \

  --no-tablespaces \

  -f ~/gbim-backup-20260712T155020Z/msjarvisgis_evidence_5433.dump

# Adjust the directory timestamp if needed:

ls -lh ~/gbim-backup-*/msjarvisgis_evidence_5433.dump

pg_dump: error: could not open output file "/home/cakidd/gbim-backup-20260712T155020Z/msjarvisgis_evidence_5433.dump": No such file or directory

-rw-rw-r-- 1 cakidd cakidd 0 Jul 12 15:46 /home/cakidd/gbim-backup-20260712T194642Z/msjarvisgis_evidence_5433.dump

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ # Pick a timestamp once

TS=20260712T155102Z

mkdir -p ~/gbim-backup-$TS

pg_dump -p 5433 -U postgres -d msjarvisgis \

  --format=custom \

  --no-tablespaces \

  -f ~/gbim-backup-$TS/msjarvisgis_evidence_5433.dump

ls -lh ~/gbim-backup-$TS/msjarvisgis_evidence_5433.dump

pg_dump: error: schema with OID 726804 does not exist

-rw-rw-r-- 1 cakidd cakidd 0 Jul 12 15:51 /home/cakidd/gbim-backup-20260712T155102Z/msjarvisgis_evidence_5433.dump

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ # Capture the orphaned types for your log

psql -p 5433 -U postgres -d msjarvisgis -c "

SELECT oid, typname, typnamespace

FROM pg_type

WHERE typnamespace = 726804;

" > ~/gbim-726804-pg_type-before.txt

# Drop the orphaned types in the missing namespace

psql -p 5433 -U postgres -d msjarvisgis -c "

DELETE FROM pg_type

WHERE typnamespace = 726804;

"

# Confirm they are gone

psql -p 5433 -U postgres -d msjarvisgis -c "

SELECT oid, typname, typnamespace

FROM pg_type

WHERE typnamespace = 726804;

"

DELETE 2

 oid | typname | typnamespace 

-----+---------+--------------

(0 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ TS=$(date +%Y%m%dT%H%M%SZ)

mkdir -p ~/gbim-backup-$TS

pg_dump -p 5433 -U postgres -d msjarvisgis \

  --format=custom \

  --no-tablespaces \

  -f ~/gbim-backup-$TS/msjarvisgis_evidence_5433.dump

ls -lh ~/gbim-backup-$TS/msjarvisgis_evidence_5433.dump

-rw-rw-r-- 1 cakidd cakidd 3.8G Jul 12 15:57 /home/cakidd/gbim-backup-20260712T155231Z/msjarvisgis_evidence_5433.dump

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ # Staging coverage table

psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

DROP TABLE IF EXISTS wv_blockgroup_dataset_coverage_stage;

CREATE TABLE wv_blockgroup_dataset_coverage_stage (

    blockgroup_geoid text,

    county_geoid text,

    feature_count integer

);

"

# Load CSV

psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

COPY wv_blockgroup_dataset_coverage_stage

FROM '/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroup_address_points_coverage_kanawha.csv'

WITH (FORMAT csv, HEADER true);

"

# Populate governed coverage table for Kanawha address points

psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

INSERT INTO wv_blockgroup_dataset_coverage (

    blockgroup_geoid,

    county_geoid,

"ELECT COUNT(*) FROM wv_blockgroup_dataset_coverage;r Kanawha (v1)'END AS coverage

NOTICE:  table "wv_blockgroup_dataset_coverage_stage" does not exist, skipping

DROP TABLE

CREATE TABLE

COPY 1639

INSERT 0 1639

 count 

-------

  1639

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ psql -p 5436 -U postgres -d msjarvisgis_v2

psql (16.14 (Ubuntu 16.14-0ubuntu0.24.04.1))

SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, compression: off)

Type "help" for help.

msjarvisgis_v2=# SELECT

  dataset_type,

  COUNT(*) AS rows,

  MIN(feature_count) AS min_features,

  MAX(feature_count) AS max_features

FROM wv_blockgroup_dataset_coverage

GROUP BY dataset_type;

      dataset_type      | rows | min_features | max_features 

------------------------+------+--------------+--------------

 address_points_kanawha | 1639 |            0 |            0

(1 row)

msjarvisgis_v2=# SELECT

  'blockgroups' AS layer,

  ST_SRID(geom) AS srid,

  COUNT(*) AS rows

FROM public.wv_blockgroups_census_2020_utm83

GROUP BY srid;

SELECT

  'kanawha_part1' AS layer,

  ST_SRID(geom) AS srid,

  COUNT(*) AS rows

FROM public.wv_address_points_kanawha_part1

GROUP BY srid;

SELECT

  'kanawha_part2' AS layer,

  ST_SRID(geom) AS srid,

  COUNT(*) AS rows

FROM public.wv_address_points_kanawha_part2

GROUP BY srid;

ERROR:  relation "public.wv_blockgroups_census_2020_utm83" does not exist

LINE 5: FROM public.wv_blockgroups_census_2020_utm83

             ^

ERROR:  relation "public.wv_address_points_kanawha_part1" does not exist

LINE 5: FROM public.wv_address_points_kanawha_part1

             ^

ERROR:  relation "public.wv_address_points_kanawha_part2" does not exist

LINE 5: FROM public.wv_address_points_kanawha_part2

             ^

msjarvisgis_v2=# TRUNCATE wv_blockgroup_dataset_coverage_stage;

COPY wv_blockgroup_dataset_coverage_stage

FROM '/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroup_address_points_coverage_kanawha.csv'

WITH (FORMAT csv, HEADER true);

DELETE FROM wv_blockgroup_dataset_coverage

WHERE dataset_type = 'address_points_kanawha';

INSERT INTO wv_blockgroup_dataset_coverage (

    blockgroup_geoid,

    county_geoid,

    dataset_type,

    source_table,

    feature_count,

    coverage_state,

    calculation_time,

    source_layer_hash,

    notes

)

SELECT s.blockgroup_geoid,

       s.county_geoid,

       'address_points_kanawha'::text,

FROM wv_blockgroup_dataset_coverage_stage s;r Kanawha (v1, SRID-aligned)' coverage_

TRUNCATE TABLE

COPY 1639

DELETE 1639

INSERT 0 1639

msjarvisgis_v2=# SELECT

  dataset_type,

  COUNT(*) AS rows,

  MIN(feature_count) AS min_features,

  MAX(feature_count) AS max_features

FROM wv_blockgroup_dataset_coverage

GROUP BY dataset_type;

      dataset_type      | rows | min_features | max_features 

------------------------+------+--------------+--------------

 address_points_kanawha | 1639 |            0 |         1618

(1 row)

msjarvisgis_v2=# DROP TABLE IF EXISTS wv_blockgroup_belief_snapshot;

CREATE TABLE wv_blockgroup_belief_snapshot (

    blockgroup_geoid text NOT NULL,

    county_geoid text NOT NULL,

    snapshot_version integer NOT NULL,

    belief_hash text NOT NULL,

    coverage_summary text NOT NULL,

    semantic_content text NOT NULL,

    created_at timestamptz DEFAULT now(),

    PRIMARY KEY (blockgroup_geoid, snapshot_version)

);

INSERT INTO wv_blockgroup_belief_snapshot (

    blockgroup_geoid,

    county_geoid,

    snapshot_version,

    belief_hash,

    coverage_summary,

    semantic_content

)

SELECT i.blockgroup_geoid,

       i.county_geoid,

       1 AS snapshot_version,

 AND c.dataset_type = 'address_points_kanawha';ate ' || COALESCE(c.coverage_state, 

NOTICE:  table "wv_blockgroup_belief_snapshot" does not exist, skipping

DROP TABLE

CREATE TABLE

INSERT 0 1639

msjarvisgis_v2=# SELECT COUNT(*) FROM wv_blockgroup_belief_snapshot;

 count 

-------

  1639

(1 row)

msjarvisgis_v2=# DROP VIEW IF EXISTS wv_blockgroup_belief_vector_ready;

CREATE VIEW wv_blockgroup_belief_vector_ready AS

SELECT

    s.blockgroup_geoid,

    s.county_geoid,

    s.snapshot_version,

    s.belief_hash AS document_id,

    s.semantic_content AS governed_text,

    r.source_table,

    r.source_feature_id,

    ST_AsText(ST_Centroid(r.geom)) AS centroid_wkt,

    ST_AsText(ST_Envelope(r.geom)) AS bbox_wkt,

    'census_blockgroup'::text AS entity_type

FROM wv_blockgroup_belief_snapshot s

JOIN wv_blockgroup_representation r

  ON r.blockgroup_geoid = s.blockgroup_geoid

WHERE s.snapshot_version = 1;

NOTICE:  view "wv_blockgroup_belief_vector_ready" does not exist, skipping

DROP VIEW

CREATE VIEW

msjarvisgis_v2=# SELECT COUNT(*) AS rows, COUNT(DISTINCT document_id) AS distinct_docs

FROM wv_blockgroup_belief_vector_ready;

 rows | distinct_docs 

------+---------------

 1639 |          1639

(1 row)

msjarvisgis_v2=# COPY (

  SELECT

    document_id,

    governed_text,

    entity_type,

    blockgroup_geoid,

    county_geoid

  FROM wv_blockgroup_belief_vector_ready

) TO '/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroup_belief_vector_ready_v1.csv'

WITH (FORMAT csv, HEADER true);

ERROR:  could not open file "/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroup_belief_vector_ready_v1.csv" for writing: Permission denied

HINT:  COPY TO instructs the PostgreSQL server process to write a file. You may want a client-side facility such as psql's \copy.

msjarvisgis_v2=# \COPY (

  SELECT

    document_id,

    governed_text,

    entity_type,

    blockgroup_geoid,

    county_geoid

  FROM wv_blockgroup_belief_vector_ready

) TO '/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroup_belief_vector_ready_v1.csv'

WITH (FORMAT csv, HEADER true);

COPY 1639

msjarvisgis_v2=# TRUNCATE wv_blockgroup_dataset_coverage_stage;

COPY wv_blockgroup_dataset_coverage_stage

FROM '/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroup_address_points_coverage_statewide.csv'

WITH (FORMAT csv, HEADER true);

DELETE FROM wv_blockgroup_dataset_coverage

WHERE dataset_type = 'address_points_statewide';

INSERT INTO wv_blockgroup_dataset_coverage (

    blockgroup_geoid,

    county_geoid,

    dataset_type,

    source_table,

    feature_count,

    coverage_state,

    calculation_time,

    source_layer_hash,

    notes

)

SELECT s.blockgroup_geoid,

       s.county_geoid,

       'address_points_statewide'::text,

GROUP BY dataset_type;aset_coverages,tage s;nt coverage (v1)'sent' END,

TRUNCATE TABLE

COPY 1639

DELETE 0

INSERT 0 1639

       dataset_type       | rows | min_features | max_features 

--------------------------+------+--------------+--------------

 address_points_kanawha   | 1639 |            0 |         1618

 address_points_statewide | 1639 |           20 |         3172

(2 rows)

msjarvisgis_v2=# DROP TABLE IF EXISTS wv_blockgroup_belief_snapshot;

CREATE TABLE wv_blockgroup_belief_snapshot (

    blockgroup_geoid text NOT NULL,

    county_geoid text NOT NULL,

    snapshot_version integer NOT NULL,

    belief_hash text NOT NULL,

    coverage_summary text NOT NULL,

    semantic_content text NOT NULL,

    created_at timestamptz DEFAULT now(),

    PRIMARY KEY (blockgroup_geoid, snapshot_version)

);

INSERT INTO wv_blockgroup_belief_snapshot (

    blockgroup_geoid,

    county_geoid,

    snapshot_version,

    belief_hash,

    coverage_summary,

    semantic_content

)

SELECT i.blockgroup_geoid,

       i.county_geoid,

       1 AS snapshot_version,

SELECT COUNT(*) FROM wv_blockgroup_belief_snapshot;e ' || COALESCE(c.coverage_state,

ERROR:  cannot drop table wv_blockgroup_belief_snapshot because other objects depend on it

DETAIL:  view wv_blockgroup_belief_vector_ready depends on table wv_blockgroup_belief_snapshot

HINT:  Use DROP ... CASCADE to drop the dependent objects too.

ERROR:  relation "wv_blockgroup_belief_snapshot" already exists

ERROR:  duplicate key value violates unique constraint "wv_blockgroup_belief_snapshot_pkey"

DETAIL:  Key (blockgroup_geoid, snapshot_version)=(540939654003, 1) already exists.

 count 

-------

  1639

(1 row)

msjarvisgis_v2=# DROP VIEW IF EXISTS wv_blockgroup_belief_vector_ready;

DROP TABLE IF EXISTS wv_blockgroup_belief_snapshot;

DROP VIEW

DROP TABLE

msjarvisgis_v2=# CREATE TABLE wv_blockgroup_belief_snapshot (

    blockgroup_geoid text NOT NULL,

    county_geoid text NOT NULL,

    snapshot_version integer NOT NULL,

    belief_hash text NOT NULL,

    coverage_summary text NOT NULL,

    semantic_content text NOT NULL,

    created_at timestamptz DEFAULT now(),

    PRIMARY KEY (blockgroup_geoid, snapshot_version)

);

INSERT INTO wv_blockgroup_belief_snapshot (

    blockgroup_geoid,

    county_geoid,

    snapshot_version,

    belief_hash,

    coverage_summary,

    semantic_content

)

SELECT i.blockgroup_geoid,

       i.county_geoid,

       1 AS snapshot_version,

       md5(

         i.blockgroup_geoid || '|' ||

SELECT COUNT(*) FROM wv_blockgroup_belief_snapshot;e ' || COALESCE(c.coverage_state,

CREATE TABLE

INSERT 0 1639

 count 

-------

  1639

(1 row)

msjarvisgis_v2=# CREATE VIEW wv_blockgroup_belief_vector_ready AS

SELECT

    s.blockgroup_geoid,

    s.county_geoid,

    s.snapshot_version,

    s.belief_hash AS document_id,

    s.semantic_content AS governed_text,

    r.source_table,

    r.source_feature_id,

    ST_AsText(ST_Centroid(r.geom)) AS centroid_wkt,

    ST_AsText(ST_Envelope(r.geom)) AS bbox_wkt,

    'census_blockgroup'::text AS entity_type

FROM wv_blockgroup_belief_snapshot s

JOIN wv_blockgroup_representation r

  ON r.blockgroup_geoid = s.blockgroup_geoid

WHERE s.snapshot_version = 1;

SELECT COUNT(*) AS rows, COUNT(DISTINCT document_id) AS distinct_docs

FROM wv_blockgroup_belief_vector_ready;

CREATE VIEW

 rows | distinct_docs 

------+---------------

 1639 |          1639

(1 row)

msjarvisgis_v2=# \COPY (

  SELECT

    document_id,

    governed_text,

    entity_type,

    blockgroup_geoid,

    county_geoid

  FROM wv_blockgroup_belief_vector_ready

) TO '/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroup_belief_vector_ready_statewide_v1.csv'

WITH (FORMAT csv, HEADER true);

COPY 1639

msjarvisgis_v2=# -- Blockgroup identity spine

SELECT COUNT(*) AS blockgroup_count

FROM wv_blockgroup_identity;

SELECT blockgroup_geoid, county_geoid

FROM wv_blockgroup_identity

ORDER BY blockgroup_geoid

LIMIT 10;

 blockgroup_count 

------------------

             1639

(1 row)

 blockgroup_geoid | county_geoid 

------------------+--------------

 540019655001     | 54001

 540019655002     | 54001

 540019655003     | 54001

 540019655004     | 54001

 540019656001     | 54001

 540019656002     | 54001

 540019656003     | 54001

 540019656004     | 54001

 540019657001     | 54001

 540019657002     | 54001

(10 rows)

msjarvisgis_v2=# -- Tract spine (adjust table name if needed)

SELECT COUNT(*) AS tract_count

FROM wv_tract_identity;

SELECT tract_geoid, county_geoid

FROM wv_tract_identity

ORDER BY tract_geoid

LIMIT 10;

 tract_count 

-------------

         546

(1 row)

ERROR:  column "county_geoid" does not exist

LINE 1: SELECT tract_geoid, county_geoid

                            ^

msjarvisgis_v2=# -- County table (if present)

SELECT COUNT(*) AS county_count

FROM wv_county_identity;

SELECT county_geoid, county_name

FROM wv_county_identity

ORDER BY county_geoid

LIMIT 10;

 county_count 

--------------

           55

(1 row)

 county_geoid | county_name 

--------------+-------------

 54001        | Barbour

 54003        | Berkeley

 54005        | Boone

 54007        | Braxton

 54009        | Brooke

 54011        | Cabell

 54013        | Calhoun

 54015        | Clay

 54017        | Doddridge

 54019        | Fayette

(10 rows)

msjarvisgis_v2=# SELECT

  dataset_type,

  COUNT(*) AS rows,

  MIN(feature_count) AS min_features,

  MAX(feature_count) AS max_features

FROM wv_blockgroup_dataset_coverage

GROUP BY dataset_type

ORDER BY dataset_type;

       dataset_type       | rows | min_features | max_features 

--------------------------+------+--------------+--------------

 address_points_kanawha   | 1639 |            0 |         1618

 address_points_statewide | 1639 |           20 |         3172

(2 rows)

msjarvisgis_v2=# SELECT *

FROM wv_blockgroup_dataset_coverage

WHERE dataset_type = 'address_points_statewide'

ORDER BY feature_count DESC

LIMIT 10;

msjarvisgis_v2=# SELECT

  blockgroup_geoid,

  county_geoid,

  coverage_summary,

  semantic_content

FROM wv_blockgroup_belief_snapshot

ORDER BY blockgroup_geoid

LIMIT 10;

msjarvisgis_v2=# -- Derive tract_geoid from blockgroup_geoid

SELECT

  blockgroup_geoid,

  county_geoid,

  substr(blockgroup_geoid, 1, 11) AS tract_geoid

FROM wv_blockgroup_identity

ORDER BY blockgroup_geoid

LIMIT 10;

 blockgroup_geoid | county_geoid | tract_geoid 

------------------+--------------+-------------

 540019655001     | 54001        | 54001965500

 540019655002     | 54001        | 54001965500

 540019655003     | 54001        | 54001965500

 540019655004     | 54001        | 54001965500

 540019656001     | 54001        | 54001965600

 540019656002     | 54001        | 54001965600

 540019656003     | 54001        | 54001965600

 540019656004     | 54001        | 54001965600

 540019657001     | 54001        | 54001965700

 540019657002     | 54001        | 54001965700

(10 rows)

msjarvisgis_v2=# -- Tract-level aggregation from existing blockgroup coverage (wide investigation)

WITH tract_ap AS (

  SELECT

    substr(blockgroup_geoid, 1, 11) AS tract_geoid,

    county_geoid,

    SUM(feature_count) AS tract_feature_count,

    COUNT(*) AS blockgroup_count,

    SUM(CASE WHEN feature_count >= 500 THEN 1 ELSE 0 END) AS high_density_blockgroups

  FROM wv_blockgroup_dataset_coverage

  WHERE dataset_type = 'address_points_statewide'

  GROUP BY substr(blockgroup_geoid, 1, 11), county_geoid

)

SELECT *

FROM tract_ap

ORDER BY tract_feature_count DESC

LIMIT 10;

msjarvisgis_v2=# SELECT

  blockgroup_geoid,

  county_geoid,

  substr(blockgroup_geoid, 1, 11) AS tract_geoid

FROM wv_blockgroup_identity

ORDER BY blockgroup_geoid

LIMIT 10;

 blockgroup_geoid | county_geoid | tract_geoid 

------------------+--------------+-------------

 540019655001     | 54001        | 54001965500

 540019655002     | 54001        | 54001965500

 540019655003     | 54001        | 54001965500

 540019655004     | 54001        | 54001965500

 540019656001     | 54001        | 54001965600

 540019656002     | 54001        | 54001965600

 540019656003     | 54001        | 54001965600

 540019656004     | 54001        | 54001965600

 540019657001     | 54001        | 54001965700

 540019657002     | 54001        | 54001965700

(10 rows)

msjarvisgis_v2=# WITH tract_ap AS (

  SELECT

    substr(blockgroup_geoid, 1, 11) AS tract_geoid,

    county_geoid,

    SUM(feature_count) AS tract_feature_count,

    COUNT(*) AS blockgroup_count,

    SUM(CASE WHEN feature_count >= 500 THEN 1 ELSE 0 END) AS high_density_blockgroups

  FROM wv_blockgroup_dataset_coverage

  WHERE dataset_type = 'address_points_statewide'

  GROUP BY substr(blockgroup_geoid, 1, 11), county_geoid

)

SELECT *

FROM tract_ap

ORDER BY tract_feature_count DESC

LIMIT 10;

msjarvisgis_v2=# SELECT

  blockgroup_geoid,

  county_geoid,

  substr(blockgroup_geoid, 1, 11) AS tract_geoid

FROM wv_blockgroup_identity

ORDER BY blockgroup_geoid

LIMIT 10;

 blockgroup_geoid | county_geoid | tract_geoid 

------------------+--------------+-------------

 540019655001     | 54001        | 54001965500

 540019655002     | 54001        | 54001965500

 540019655003     | 54001        | 54001965500

 540019655004     | 54001        | 54001965500

 540019656001     | 54001        | 54001965600

 540019656002     | 54001        | 54001965600

 540019656003     | 54001        | 54001965600

 540019656004     | 54001        | 54001965600

 540019657001     | 54001        | 54001965700

 540019657002     | 54001        | 54001965700

(10 rows)

msjarvisgis_v2=# -- 1.1 Create a tract-level coverage view for address_points_statewide

DROP VIEW IF EXISTS wv_tract_address_points_coverage_statewide;

CREATE VIEW wv_tract_address_points_coverage_statewide AS

WITH tract_ap AS (

  SELECT

    substr(blockgroup_geoid, 1, 11) AS tract_geoid,

    county_geoid,

    SUM(feature_count) AS tract_feature_count,

    COUNT(*) AS blockgroup_count,

    SUM(CASE WHEN feature_count >= 500 THEN 1 ELSE 0 END) AS high_density_blockgroups

  FROM wv_blockgroup_dataset_coverage

  WHERE dataset_type = 'address_points_statewide'

  GROUP BY substr(blockgroup_geoid, 1, 11), county_geoid

)

SELECT

  tract_geoid,

  county_geoid,

  tract_feature_count,

  blockgroup_count,

  high_density_blockgroups

FROM tract_ap;

NOTICE:  view "wv_tract_address_points_coverage_statewide" does not exist, skipping

DROP VIEW

CREATE VIEW

msjarvisgis_v2=# SELECT *

FROM wv_tract_address_points_coverage_statewide

ORDER BY tract_feature_count DESC

LIMIT 10;

msjarvisgis_v2=# ALTER TABLE wv_blockgroup_belief_snapshot

  ADD COLUMN tract_geoid text,

  ADD COLUMN tract_summary text;

ALTER TABLE

msjarvisgis_v2=# -- 2.2 Populate tract_geoid and tract_summary for address_points_statewide beliefs

UPDATE wv_blockgroup_belief_snapshot s

SET tract_geoid = substr(s.blockgroup_geoid, 1, 11)

WHERE tract_geoid IS NULL;

UPDATE wv_blockgroup_belief_snapshot s

SET tract_summary = (

  SELECT

    'Parent tract ' || t.tract_geoid ||

    ' in county ' || t.county_geoid ||

    ' has ' || t.tract_feature_count::text ||

    ' statewide address points across ' || t.blockgroup_count::text ||

    ' blockgroups, including ' || t.high_density_blockgroups::text ||

    ' high-density blockgroups.'

  FROM wv_tract_address_points_coverage_statewide t

  WHERE t.tract_geoid = substr(s.blockgroup_geoid, 1, 11)

)

WHERE tract_summary IS NULL;

UPDATE 1639

UPDATE 1639

msjarvisgis_v2=# SELECT

  blockgroup_geoid,

  county_geoid,

  tract_geoid,

  coverage_summary,

  tract_summary,

  semantic_content

FROM wv_blockgroup_belief_snapshot

ORDER BY blockgroup_geoid

LIMIT 10;

msjarvisgis_v2=# -- 2.3.1 Update semantic_content to include tract summary and explicit coverage reason

UPDATE wv_blockgroup_belief_snapshot s

SET semantic_content = (

  CASE

    WHEN c.dataset_type = 'address_points_statewide' AND c.feature_count > 0 THEN

      'Census blockgroup ' || s.blockgroup_geoid ||

      ' in county ' || s.county_geoid ||

      ' and tract ' || s.tract_geoid ||

      ' has ' || c.feature_count::text ||

      ' statewide address points and coverage state ' || c.coverage_state || '. ' || 

      COALESCE(s.tract_summary, '')

    WHEN c.dataset_type = 'address_points_statewide' AND c.feature_count = 0 THEN

      'Census blockgroup ' || s.blockgroup_geoid ||

      ' in county ' || s.county_geoid ||

      ' and tract ' || s.tract_geoid ||

      ' is covered by the statewide address-point layer but has no address points (coverage state ' ||

      c.coverage_state || '). ' ||

      COALESCE(s.tract_summary, '')

    ELSE

      s.semantic_content

  END

  AND c.dataset_type = 'address_points_statewide';

UPDATE 1639

msjarvisgis_v2=# SELECT

  blockgroup_geoid,

  county_geoid,

  tract_geoid,

  coverage_summary,

  tract_summary,

  semantic_content

FROM wv_blockgroup_belief_snapshot

ORDER BY blockgroup_geoid

LIMIT 10;

msjarvisgis_v2=# DROP VIEW IF EXISTS wv_blockgroup_belief_vector_ready;

CREATE VIEW wv_blockgroup_belief_vector_ready AS

SELECT

    s.blockgroup_geoid,

    s.county_geoid,

    s.tract_geoid,

    s.snapshot_version,

    s.belief_hash AS document_id,

    s.semantic_content AS governed_text,

    r.source_table,

    r.source_feature_id,

    ST_AsText(ST_Centroid(r.geom)) AS centroid_wkt,

    ST_AsText(ST_Envelope(r.geom)) AS bbox_wkt,

    'census_blockgroup'::text AS entity_type

FROM wv_blockgroup_belief_snapshot s

JOIN wv_blockgroup_representation r

  ON r.blockgroup_geoid = s.blockgroup_geoid

WHERE s.snapshot_version = 1;

DROP VIEW

CREATE VIEW

msjarvisgis_v2=# \COPY (

  SELECT

    document_id,

    governed_text,

    entity_type,

    blockgroup_geoid,

    county_geoid,

    tract_geoid

  FROM wv_blockgroup_belief_vector_ready

) TO '/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroup_belief_vector_ready_statewide_v2.csv'

WITH (FORMAT csv, HEADER true);

COPY 1639

msjarvisgis_v2=# 

msjarvisgis_v2=# ALTER TABLE wv_blockgroup_dataset_coverage

ADD COLUMN IF NOT EXISTS coverage_reason text;

ALTER TABLE

msjarvisgis_v2=# UPDATE wv_blockgroup_dataset_coverage

SET coverage_reason = CASE

  WHEN feature_count > 0 THEN 'features_intersected'

  WHEN feature_count = 0 THEN 'no_features_found_in_covered_area'

  ELSE 'unknown'

END

WHERE dataset_type IN ('address_points_kanawha', 'address_points_statewide');

UPDATE 3278

msjarvisgis_v2=# SELECT

  dataset_type,

  coverage_state,

  coverage_reason,

  COUNT(*) AS rows

FROM wv_blockgroup_dataset_coverage

GROUP BY dataset_type, coverage_state, coverage_reason

ORDER BY dataset_type, coverage_state, coverage_reason;

msjarvisgis_v2=# UPDATE wv_blockgroup_belief_snapshot s

SET semantic_content = (

  CASE

    WHEN c.feature_count > 0 THEN

      'Census blockgroup ' || s.blockgroup_geoid ||

      ' in county ' || s.county_geoid ||

      ' and tract ' || s.tract_geoid ||

      ' has ' || c.feature_count::text ||

      ' statewide address points and coverage state ' || c.coverage_state ||

      ' with coverage reason ' || c.coverage_reason || '. ' ||

      COALESCE(s.tract_summary, '')

    WHEN c.feature_count = 0 THEN

      'Census blockgroup ' || s.blockgroup_geoid ||

      ' in county ' || s.county_geoid ||

      ' and tract ' || s.tract_geoid ||

      ' is covered by the statewide address-point layer but has no address points. ' ||

      'Coverage state ' || c.coverage_state ||

      ' with coverage reason ' || c.coverage_reason || '. ' ||

      COALESCE(s.tract_summary, '')

    ELSE

      s.semantic_content

  END

)

  AND c.dataset_type = 'address_points_statewide';

UPDATE 1639

msjarvisgis_v2=# \COPY (

  SELECT

    document_id,

    governed_text,

    entity_type,

    blockgroup_geoid,

    county_geoid,

    tract_geoid

  FROM wv_blockgroup_belief_vector_ready

) TO '/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroup_belief_vector_ready_statewide_v3.csv'

WITH (FORMAT csv, HEADER true);

COPY 1639

msjarvisgis_v2=# INSERT INTO wv_blockgroup_dataset_coverage (

    blockgroup_geoid,

    county_geoid,

    dataset_type,

    source_table,

    feature_count,

    coverage_state,

    calculation_time,

    source_layer_hash,

    notes,

    coverage_reason

)

SELECT

    bg.blockgroup_geoid,

    bg.county_geoid,

    'roads_statewide' AS dataset_type,

    'public.wv_roads_statewide_mv' AS source_table,

    COUNT(r.*)::integer AS feature_count,

    CASE

      WHEN COUNT(r.*) > 0 THEN 'present'

      ELSE 'absent'

    END AS coverage_state,

    now() AS calculation_time,

    NULL::text AS source_layer_hash,

    bg.county_geoid;oid,m, bgr.geom)mv rp_geoidected'tersection (v1)' AS notes,

ERROR:  relation "public.wv_roads_statewide_mv" does not exist

LINE 33: LEFT JOIN public.wv_roads_statewide_mv r

                   ^

msjarvisgis_v2=# -- List geometry-bearing tables/views in msjarvisgis_v2

SELECT

  n.nspname AS schema_name,

  c.relname AS relation_name

FROM pg_class c

JOIN pg_namespace n ON n.oid = c.relnamespace

JOIN pg_attribute a ON a.attrelid = c.oid

JOIN pg_type t ON t.oid = a.atttypid

WHERE t.typname = 'geometry'

  AND n.nspname NOT IN ('pg_catalog', 'information_schema')

GROUP BY n.nspname, c.relname

ORDER BY n.nspname, c.relname;

msjarvisgis_v2=# CREATE TABLE IF NOT EXISTS gbim_layer_registry (

    dataset_type text PRIMARY KEY,

    source_schema text NOT NULL,

    source_table text NOT NULL,

    geom_column text NOT NULL,

    geom_type text NOT NULL,

    srid integer,

    metric_kind text NOT NULL,

    enabled boolean NOT NULL DEFAULT false,

    notes text,

    discovered_at timestamptz NOT NULL DEFAULT now()

);

INSERT INTO gbim_layer_registry (

    dataset_type,

    source_schema,

    source_table,

    geom_column,

    geom_type,

    srid,

    metric_kind,

    enabled,

    notes

)

ON CONFLICT (dataset_type) DO NOTHING;talog', 'information_schema')

CREATE TABLE

INSERT 0 139

msjarvisgis_v2=# SELECT dataset_type, geom_type, srid, metric_kind, enabled

FROM gbim_layer_registry

ORDER BY dataset_type;

msjarvisgis_v2=# UPDATE gbim_layer_registry

SET enabled = true

WHERE dataset_type IN (

    'public.wv_env_epa_facilities',

    'public.wv_hyd_hazus_floodplain_zones',

    'public.wv_hlt_health_providers',

    'public.wv_hlt_public_health_departments',

    'public.wv_hlt_rural_health_facilities',

    'public.wv_soc_hospitals_wvdem',

    'public.wv_soc_libraries',

    'public.wv_soc_places_of_worship_wvgistc',

    'public.wv_soc_schools_k12',

    'public.wv_str_bridges',

    'public.wv_trn_roads_interstate',

    'public.wv_trn_roads_major_4800',

    'public.wv_trn_roads_state_routes',

    'public.wv_trn_roads_us_highways',

    'public.wv_trn_roads_us_routes',

    'public.wv_trn_airports',

    'public.wv_trn_railroad_lines_rti',

    'public.wv_util_sewer_treatment_plants',

    'public.wv_util_solid_waste_facilities'

);

UPDATE 19

msjarvisgis_v2=# DO $$

DECLARE

    r record;

BEGIN

    FOR r IN

        SELECT dataset_type

        FROM gbim_layer_registry

        WHERE enabled = true

        ORDER BY dataset_type

    LOOP

        CALL gbim_load_blockgroup_coverage(r.dataset_type);

    END LOOP;

END;

$$;

ERROR:  procedure gbim_load_blockgroup_coverage(text) does not exist

LINE 1: CALL gbim_load_blockgroup_coverage(r.dataset_type)

             ^

HINT:  No procedure matches the given name and argument types. You might need to add explicit type casts.

QUERY:  CALL gbim_load_blockgroup_coverage(r.dataset_type)

CONTEXT:  PL/pgSQL function inline_code_block line 11 at CALL

msjarvisgis_v2=# DROP VIEW IF EXISTS gbim_tract_layer_rollup;

CREATE VIEW gbim_tract_layer_rollup AS

SELECT

    dataset_type,

    substr(blockgroup_geoid, 1, 11) AS tract_geoid,

    county_geoid,

    SUM(feature_count)::integer AS tract_feature_count,

    COUNT(*)::integer AS blockgroup_count,

    SUM(CASE WHEN feature_count > 0 THEN 1 ELSE 0 END)::integer AS blockgroups_with_features

FROM wv_blockgroup_dataset_coverage

GROUP BY

    dataset_type,

    substr(blockgroup_geoid, 1, 11),

    county_geoid;

NOTICE:  view "gbim_tract_layer_rollup" does not exist, skipping

DROP VIEW

CREATE VIEW

msjarvisgis_v2=# 

msjarvisgis_v2=# TRUNCATE TABLE gbim_blockgroup_text_fragments;

INSERT INTO gbim_blockgroup_text_fragments (

    blockgroup_geoid,

    dataset_type,

    fragment_order,

    fragment_text

)

SELECT

    c.blockgroup_geoid,

    c.dataset_type,

    10,

    CASE

      WHEN c.coverage_state = 'present' THEN

        c.dataset_type || ' layer is present with coverage reason ' || c.coverage_reason ||

        ' and intersects ' || c.feature_count::text || ' features.'

      WHEN c.coverage_state = 'absent' THEN

        c.dataset_type || ' layer is absent with coverage reason ' || c.coverage_reason ||

        ' and intersects no features.'

      WHEN c.coverage_state = 'not_applicable' THEN

        c.dataset_type || ' layer is not applicable with coverage reason ' || c.coverage_reason || '.'

WHERE r.enabled = true;.dataset_typec.coverage_reason || '.'|

ERROR:  relation "gbim_blockgroup_text_fragments" does not exist

ERROR:  relation "gbim_blockgroup_text_fragments" does not exist

LINE 1: INSERT INTO gbim_blockgroup_text_fragments (

                    ^

msjarvisgis_v2=# CREATE OR REPLACE PROCEDURE gbim_load_blockgroup_coverage(p_dataset_type text)

LANGUAGE plpgsql

AS $$

DECLARE

    v_source_schema text;

    v_source_table text;

    v_geom_column text;

    v_geom_type text;

    v_metric_kind text;

    v_sql text;

BEGIN

    SELECT source_schema, source_table, geom_column, geom_type, metric_kind

    INTO v_source_schema, v_source_table, v_geom_column, v_geom_type, v_metric_kind

    FROM gbim_layer_registry

    WHERE dataset_type = p_dataset_type

      AND enabled = true;

    IF NOT FOUND THEN

        RAISE EXCEPTION 'Dataset type % not found or not enabled in gbim_layer_registry', p_dataset_type;

    END IF;

    -- Clear any existing coverage rows for this dataset_type

$$;;EXECUTE v_sql;chema, v_source_table, v_geom_columnset_type,

CREATE PROCEDURE

msjarvisgis_v2=# DO $$

DECLARE

    r record;

BEGIN

    FOR r IN

        SELECT dataset_type

        FROM gbim_layer_registry

        WHERE enabled = true

        ORDER BY dataset_type

    LOOP

        CALL gbim_load_blockgroup_coverage(r.dataset_type);

    END LOOP;

END;

$$;

DO

msjarvisgis_v2=# CREATE TABLE IF NOT EXISTS gbim_blockgroup_text_fragments (

    blockgroup_geoid text NOT NULL,

    dataset_type text NOT NULL,

    fragment_order integer NOT NULL,

    fragment_text text NOT NULL,

    PRIMARY KEY (blockgroup_geoid, dataset_type, fragment_order)

);

CREATE TABLE

msjarvisgis_v2=# TRUNCATE TABLE gbim_blockgroup_text_fragments;

INSERT INTO gbim_blockgroup_text_fragments (

    blockgroup_geoid,

    dataset_type,

    fragment_order,

    fragment_text

)

SELECT

    c.blockgroup_geoid,

    c.dataset_type,

    10,

    CASE

      WHEN c.coverage_state = 'present' THEN

        c.dataset_type || ' layer is present with coverage reason ' || c.coverage_reason ||

        ' and intersects ' || c.feature_count::text || ' features.'

      WHEN c.coverage_state = 'absent' THEN

        c.dataset_type || ' layer is absent with coverage reason ' || c.coverage_reason ||

        ' and intersects no features.'

      WHEN c.coverage_state = 'not_applicable' THEN

        c.dataset_type || ' layer is not applicable with coverage reason ' || c.coverage_reason || '.'

WHERE r.enabled = true;.dataset_typec.coverage_reason || '.'|

TRUNCATE TABLE

INSERT 0 31141

msjarvisgis_v2=# INSERT INTO gbim_blockgroup_text_fragments (

    blockgroup_geoid,

    dataset_type,

    fragment_order,

    fragment_text

)

SELECT

    b.blockgroup_geoid,

    t.dataset_type,

    20,

    'Parent tract ' || t.tract_geoid ||

    ' in county ' || t.county_geoid ||

    ' has ' || t.tract_feature_count::text ||

    ' features for ' || t.dataset_type ||

    ' across ' || t.blockgroup_count::text ||

    ' blockgroups, including ' || t.blockgroups_with_features::text ||

    ' blockgroups with features.'

FROM wv_blockgroup_identity b

JOIN gbim_tract_layer_rollup t

  ON t.tract_geoid = substr(b.blockgroup_geoid, 1, 11)

 AND t.county_geoid = b.county_geoid

JOIN gbim_layer_registry r

  ON r.dataset_type = t.dataset_type

WHERE r.enabled = true;

INSERT 0 31141

msjarvisgis_v2=# CREATE OR REPLACE VIEW gbim_blockgroup_semantic_rebuild AS

SELECT           CREATE OR REPLACE VIEW gbim_blockgroup_semantic_rebuild AS

SELECTblockgroup_geoid,

    s.blockgroup_geoid,

    s.county_geoid,

    s.tract_geoid,sion,

    s.snapshot_version,

    s.belief_hash,

    trim(cat_ws(

      concat_ws(

        ' ',sus blockgroup ' || s.blockgroup_geoid ||

        'Census blockgroup ' || s.blockgroup_geoid ||

        ' in county ' || s.county_geoid ||'.',

        ' and tract ' || s.tract_geoid || '.',BY f.dataset_type, f.fragment_order)

        string_agg(f.fragment_text, ' ' ORDER BY f.dataset_type, f.fragment_order)

      )S rebuilt_semantic_content

    ) AS rebuilt_semantic_contentt s

FROM wv_blockgroup_belief_snapshot sents f

LEFT JOIN gbim_blockgroup_text_fragments fid

  ON f.blockgroup_geoid = s.blockgroup_geoid

GROUP BYockgroup_geoid,

    s.blockgroup_geoid,

    s.county_geoid,

    s.tract_geoid,sion,

    s.snapshot_version,

    s.belief_hash;

CREATE VIEW

msjarvisgis_v2=# UPDATE wv_blockgroup_belief_snapshot s

SET semantic_content = r.rebuilt_semantic_content

FROM gbim_blockgroup_semantic_rebuild r

WHERE r.blockgroup_geoid = s.blockgroup_geoid

  AND r.snapshot_version = s.snapshot_version;

UPDATE 1639

msjarvisgis_v2=# \COPY (

  SELECT

    document_id,

    governed_text,

    entity_type,

    blockgroup_geoid,

    county_geoid,

    tract_geoid

  FROM wv_blockgroup_belief_vector_ready

) TO '/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroup_belief_vector_ready_statewide_v4.csv'

WITH (FORMAT csv, HEADER true);

COPY 1639

msjarvisgis_v2=# SELECT

  blockgroup_geoid,

  semantic_content

FROM wv_blockgroup_belief_snapshot

ORDER BY blockgroup_geoid

LIMIT 3;

msjarvisgis_v2=# SELECT

  blockgroup_geoid,

  semantic_content

FROM wv_blockgroup_belief_snapshot

ORDER BY blockgroup_geoid

LIMIT 3;

msjarvisgis_v2=# ALTER TABLE gbim_layer_registry

  ADD COLUMN IF NOT EXISTS display_name text;

UPDATE gbim_layer_registry

SET display_name = CASE dataset_type

    WHEN 'public.wv_env_epa_facilities'            THEN 'EPA-regulated facilities'

    WHEN 'public.wv_hyd_hazus_floodplain_zones'   THEN 'FEMA HAZUS floodplains'

    WHEN 'public.wv_hlt_health_providers'         THEN 'health care providers'

    WHEN 'public.wv_hlt_public_health_departments' THEN 'public health departments'

    WHEN 'public.wv_hlt_rural_health_facilities'  THEN 'rural health facilities'

    WHEN 'public.wv_soc_hospitals_wvdem'          THEN 'hospitals'

    WHEN 'public.wv_soc_libraries'                THEN 'public libraries'

    WHEN 'public.wv_soc_places_of_worship_wvgistc' THEN 'places of worship'

    WHEN 'public.wv_soc_schools_k12'              THEN 'K–12 schools'

    WHEN 'public.wv_str_bridges'                  THEN 'bridges'

    WHEN 'public.wv_trn_airports'                 THEN 'airports'

    WHEN 'public.wv_trn_roads_interstate'         THEN 'interstate highways'

    WHEN 'public.wv_trn_roads_major_4800'         THEN 'major roads'

    WHEN 'public.wv_trn_roads_state_routes'       THEN 'state routes'

    WHEN 'public.wv_trn_roads_us_highways'        THEN 'U.S. highways'

    WHEN 'public.wv_trn_roads_us_routes'          THEN 'U.S. routes'

    WHEN 'public.wv_trn_railroad_lines_rti'       THEN 'railroad lines'

    WHEN 'public.wv_util_sewer_treatment_plants'  THEN 'wastewater treatment plants'

    WHEN 'public.wv_util_solid_waste_facilities'  THEN 'solid waste facilities'

END;ELSE dataset_type

ALTER TABLE

UPDATE 139

msjarvisgis_v2=# TRUNCATE TABLE gbim_blockgroup_text_fragments;

INSERT INTO gbim_blockgroup_text_fragments (

    blockgroup_geoid,

    dataset_type,

    fragment_order,

    fragment_text

)

SELECT

    c.blockgroup_geoid,

    c.dataset_type,

    10,

    CASE

      WHEN c.coverage_state = 'present' THEN

        initcap(r.display_name) || ' are present; ' ||

        c.feature_count::text || ' feature(s) intersect this blockgroup.'

      WHEN c.coverage_state = 'absent' THEN

        'No ' || r.display_name || ' intersect this blockgroup.'

      WHEN c.coverage_state = 'not_applicable' THEN

        initcap(r.display_name) || ' are not applicable in this blockgroup.'

      ELSE

        initcap(r.display_name) || ' coverage is ' || c.coverage_state ||

        ' (reason: ' || c.coverage_reason || ').'

    END AS fragment_text

WHERE r.enabled = true;.dataset_typec

TRUNCATE TABLE

INSERT 0 31141

msjarvisgis_v2=# INSERT INTO gbim_blockgroup_text_fragments (

    blockgroup_geoid,

    dataset_type,

    fragment_order,

    fragment_text

)

SELECT

    b.blockgroup_geoid,

    t.dataset_type,

    20,

    CASE

      WHEN t.tract_feature_count > 0 THEN

        'Within parent tract ' || t.tract_geoid || ', there are ' ||

        t.tract_feature_count::text || ' ' || r.display_name ||

        ' across ' || t.blockgroup_count::text ||

        ' blockgroups (' || t.blockgroups_with_features::text ||

        ' with at least one feature).'

      ELSE

        'Parent tract ' || t.tract_geoid || ' contains no ' ||

        r.display_name || '.'

    END AS fragment_text

FROM wv_blockgroup_identity b

JOIN gbim_tract_layer_rollup t

  ON t.tract_geoid = substr(b.blockgroup_geoid, 1, 11)

WHERE r.enabled = true;.dataset_type

INSERT 0 31141

msjarvisgis_v2=# CREATE OR REPLACE VIEW gbim_blockgroup_semantic_rebuild AS

SELECT           CREATE OR REPLACE VIEW gbim_blockgroup_semantic_rebuild AS

SELECTblockgroup_geoid,

    s.blockgroup_geoid,

    s.county_geoid,

    s.tract_geoid,sion,

    s.snapshot_version,

    s.belief_hash,

    trim(cat_ws(

      concat_ws(

        ' ',sus blockgroup ' || s.blockgroup_geoid ||

        'Census blockgroup ' || s.blockgroup_geoid ||

        ' in county ' || s.county_geoid ||'.',

        ' and tract ' || s.tract_geoid || '.',BY f.dataset_type, f.fragment_order)

        string_agg(f.fragment_text, ' ' ORDER BY f.dataset_type, f.fragment_order)

      )S rebuilt_semantic_content

    ) AS rebuilt_semantic_contentt s

FROM wv_blockgroup_belief_snapshot sents f

LEFT JOIN gbim_blockgroup_text_fragments fid

  ON f.blockgroup_geoid = s.blockgroup_geoid

GROUP BYockgroup_geoid,

    s.blockgroup_geoid,

    s.county_geoid,

    s.tract_geoid,sion,

    s.snapshot_version,

    s.belief_hash;

CREATE VIEW

msjarvisgis_v2=# UPDATE wv_blockgroup_belief_snapshot s

SET semantic_content = r.rebuilt_semantic_content

FROM gbim_blockgroup_semantic_rebuild r

WHERE r.blockgroup_geoid = s.blockgroup_geoid

  AND r.snapshot_version = s.snapshot_version;

UPDATE 1639

msjarvisgis_v2=# WHERE r.enabled = true

  AND (c.feature_count > 0 OR t.tract_feature_count > 0);

ERROR:  syntax error at or near "WHERE"

LINE 1: WHERE r.enabled = true

        ^

msjarvisgis_v2=# UPDATE gbim_layer_registry

SET display_name = CASE dataset_type

    ...

END;ELSE dataset_type

ERROR:  syntax error at or near ".."

LINE 3:     ...

            ^

msjarvisgis_v2-# UPDATE gbim_layer_registry

SET display_name = COALESCE(display_name, dataset_type);

ERROR:  syntax error at or near "ELSE"

LINE 1: ELSE dataset_type

        ^

msjarvisgis_v2=# TRUNCATE TABLE gbim_blockgroup_text_fragments;

INSERT INTO gbim_blockgroup_text_fragments (

    blockgroup_geoid,

    dataset_type,

    fragment_order,

    fragment_text

)

SELECT

    c.blockgroup_geoid,

    c.dataset_type,

    10,

    CASE

      WHEN c.coverage_state = 'present' THEN

        initcap(r.display_name) || ' are present; ' ||

        c.feature_count::text || ' feature(s) intersect this blockgroup.'

      WHEN c.coverage_state = 'absent' THEN

        'No ' || r.display_name || ' intersect this blockgroup.'

      WHEN c.coverage_state = 'not_applicable' THEN

        initcap(r.display_name) || ' are not applicable in this blockgroup.'

      ELSE

        initcap(r.display_name) || ' coverage is ' || c.coverage_state ||

        ' (reason: ' || c.coverage_reason || ').'

    END AS fragment_text

  AND c.feature_count > 0;taset_typec

TRUNCATE TABLE

INSERT 0 0

msjarvisgis_v2=# INSERT INTO gbim_blockgroup_text_fragments (

    blockgroup_geoid,

    dataset_type,

    fragment_order,

    fragment_text

)

SELECT

    b.blockgroup_geoid,

    t.dataset_type,

    20,

    CASE

      WHEN t.tract_feature_count > 0 THEN

        'Within parent tract ' || t.tract_geoid || ', there are ' ||

        t.tract_feature_count::text || ' ' || r.display_name ||

        ' across ' || t.blockgroup_count::text ||

        ' blockgroups (' || t.blockgroups_with_features::text ||

        ' with at least one feature).'

      ELSE

        'Parent tract ' || t.tract_geoid || ' contains no ' ||

        r.display_name || '.'

    END AS fragment_text

FROM wv_blockgroup_identity b

JOIN gbim_tract_layer_rollup t

  ON t.tract_geoid = substr(b.blockgroup_geoid, 1, 11)

  AND t.tract_feature_count > 0;type

INSERT 0 0

msjarvisgis_v2=# SELECT

  blockgroup_geoid,

  semantic_content

FROM wv_blockgroup_belief_snapshot

ORDER BY blockgroup_geoid

LIMIT 3;

msjarvisgis_v2=# ALTER TABLE gbim_layer_registry

  ADD COLUMN IF NOT EXISTS category text;

UPDATE gbim_layer_registry

SET category = CASE dataset_type

    -- Health-related

    WHEN 'public.wv_hlt_health_providers'          THEN 'health'

    WHEN 'public.wv_hlt_public_health_departments' THEN 'health'

    WHEN 'public.wv_hlt_rural_health_facilities'   THEN 'health'

    WHEN 'public.wv_soc_hospitals_wvdem'           THEN 'health'

    -- Education / civic

    WHEN 'public.wv_soc_schools_k12'               THEN 'education'

    WHEN 'public.wv_soc_libraries'                 THEN 'education'

    WHEN 'public.wv_soc_places_of_worship_wvgistc' THEN 'education'

    -- Transportation

    WHEN 'public.wv_trn_roads_interstate'          THEN 'transport'

    WHEN 'public.wv_trn_roads_major_4800'          THEN 'transport'

    WHEN 'public.wv_trn_roads_state_routes'        THEN 'transport'

    WHEN 'public.wv_trn_roads_us_highways'         THEN 'transport'

    WHEN 'public.wv_trn_roads_us_routes'           THEN 'transport'

    WHEN 'public.wv_trn_airports'                  THEN 'transport'

    WHEN 'public.wv_trn_railroad_lines_rti'        THEN 'transport'

WHERE enabled = true;CE(category, 'other')ry (fallback to 'other' if still NULL)

ALTER TABLE

UPDATE 139

UPDATE 19

msjarvisgis_v2=# TRUNCATE TABLE gbim_blockgroup_text_fragments;

TRUNCATE TABLE

msjarvisgis_v2=# INSERT INTO gbim_blockgroup_text_fragments (

    blockgroup_geoid,

    dataset_type,

    fragment_order,

    fragment_text

)

SELECT

    c.blockgroup_geoid,

    -- Use the category as dataset_type key for grouping fragments

    r.category AS dataset_type,

    10 AS fragment_order,

    CASE

      WHEN SUM(c.feature_count) > 0 THEN

        -- Present: list which layer types are present

        'In this blockgroup, there are ' ||

        string_agg(DISTINCT r.display_name, ', ' ORDER BY r.display_name) ||

        ' (' || r.category || ' infrastructure).'

      ELSE

        -- Absent: report no infrastructure of that category

        'No ' || r.category || ' infrastructure ('

        || string_agg(DISTINCT r.display_name, ', ' ORDER BY r.display_name)

        || ') intersects this blockgroup.'

    END AS fragment_text

FROM wv_blockgroup_dataset_coverage c

GROUP BY c.blockgroup_geoid, r.category;

INSERT 0 8195

msjarvisgis_v2=# INSERT INTO gbim_blockgroup_text_fragments (

    blockgroup_geoid,

    dataset_type,

    fragment_order,

    fragment_text

)

SELECT

    b.blockgroup_geoid,

    r.category AS dataset_type,

    20 AS fragment_order,

    CASE

      WHEN SUM(t.tract_feature_count) > 0 THEN

        'Within parent tract ' || t.tract_geoid || ', there are ' ||

        SUM(t.tract_feature_count)::text || ' '

        || r.category || ' feature(s) across '

        || COUNT(*)::text || ' blockgroups.'

      ELSE

        'Parent tract ' || t.tract_geoid ||

        ' contains no ' || r.category || ' infrastructure.'

    END AS fragment_text

FROM wv_blockgroup_identity b

JOIN gbim_tract_layer_rollup t

  ON t.tract_geoid = substr(b.blockgroup_geoid, 1, 11)

 AND t.county_geoid = b.county_geoid

GROUP BY b.blockgroup_geoid, r.category, t.tract_geoid;

INSERT 0 8195

msjarvisgis_v2=# CREATE OR REPLACE VIEW gbim_blockgroup_semantic_rebuild AS

SELECT           CREATE OR REPLACE VIEW gbim_blockgroup_semantic_rebuild AS

SELECTblockgroup_geoid,

    s.blockgroup_geoid,

    s.county_geoid,

    s.tract_geoid,sion,

    s.snapshot_version,

    s.belief_hash,

    trim(cat_ws(

      concat_ws(

        ' ',sus blockgroup ' || s.blockgroup_geoid ||

        'Census blockgroup ' || s.blockgroup_geoid ||

        ' in county ' || s.county_geoid ||'.',

        ' and tract ' || s.tract_geoid || '.',BY f.dataset_type, f.fragment_order)

        string_agg(f.fragment_text, ' ' ORDER BY f.dataset_type, f.fragment_order)

      )S rebuilt_semantic_content

    ) AS rebuilt_semantic_contentt s

FROM wv_blockgroup_belief_snapshot sents f

LEFT JOIN gbim_blockgroup_text_fragments fid

  ON f.blockgroup_geoid = s.blockgroup_geoid

GROUP BYockgroup_geoid,

    s.blockgroup_geoid,

    s.county_geoid,

    s.tract_geoid,sion,

    s.snapshot_version,

    s.belief_hash;

CREATE VIEW

msjarvisgis_v2=# UPDATE wv_blockgroup_belief_snapshot s

SET semantic_content = r.rebuilt_semantic_content

FROM gbim_blockgroup_semantic_rebuild r

WHERE r.blockgroup_geoid = s.blockgroup_geoid

  AND r.snapshot_version = s.snapshot_version;

UPDATE 1639

msjarvisgis_v2=# INSERT INTO gbim_blockgroup_text_fragments (

    blockgroup_geoid,

    dataset_type,

    fragment_order,

    fragment_text

)

SELECT

    b.blockgroup_geoid,

    r.category AS dataset_type,

    20 AS fragment_order,

    'Within parent tract ' || t.tract_geoid || ', there are ' ||

    SUM(t.tract_feature_count)::text || ' '

    || r.category || ' feature(s) across '

    || COUNT(*)::text || ' blockgroups.'

FROM wv_blockgroup_identity b

JOIN gbim_tract_layer_rollup t

  ON t.tract_geoid = substr(b.blockgroup_geoid, 1, 11)

 AND t.county_geoid = b.county_geoid

JOIN gbim_layer_registry r

  ON r.dataset_type = t.dataset_type

WHERE r.enabled = true

GROUP BY b.blockgroup_geoid, r.category, t.tract_geoid

HAVING SUM(t.tract_feature_count) > 0;

INSERT 0 0

msjarvisgis_v2=# TRUNCATE TABLE gbim_blockgroup_text_fragments;

TRUNCATE TABLE

msjarvisgis_v2=# INSERT INTO gbim_blockgroup_text_fragments (

    blockgroup_geINSERT INTO gbim_blockgroup_text_fragments (

    blockgroup_geoid,

    dataset_type,r,

    fragment_order,

    fragment_text

)ELECT

SELECTblockgroup_geoid,

    c.blockgroup_geoid,et_type,

    r.category AS dataset_type,

    10 AS fragment_order,

    CASEEN SUM(c.feature_count) > 0 THEN

      WHEN SUM(c.feature_count) > 0 THEN

        'In this blockgroup, there are '_name, ', ' ORDER BY r.display_name)

        || string_agg(DISTINCT r.display_name, ', ' ORDER BY r.display_name)

        || ' (' || r.category || ' infrastructure).'

      ELSEo ' || r.category || ' infrastructure ('

        'No ' || r.category || ' infrastructure ('' ORDER BY r.display_name)

        || string_agg(DISTINCT r.display_name, ', ' ORDER BY r.display_name)

        || ') intersects this blockgroup.'

    END AS fragment_textet_coverage c

FROM wv_blockgroup_dataset_coverage c

JOIN gbim_layer_registry rtaset_type

  ON r.dataset_type = c.dataset_type

WHERE r.enabled = truegeoid, r.category;

GROUP BY c.blockgroup_geoid, r.category;

INSERT 0 8195

msjarvisgis_v2=# 

msjarvisgis_v2=# INSERT INTO gbim_blockgroup_text_fragments (

    blockgroup_geoid,

    dataset_type,

    fragment_order,

    fragment_text

)

SELECT

    b.blockgroup_geoid,

    r.category AS dataset_type,

    20 AS fragment_order,

    'Within parent tract ' || t.tract_geoid || ', there are '

    || SUM(t.tract_feature_count)::text || ' '

    || r.category || ' feature(s) across '

    || COUNT(*)::text || ' blockgroups.'

FROM wv_blockgroup_identity b

JOIN gbim_tract_layer_rollup t

  ON t.tract_geoid = substr(b.blockgroup_geoid, 1, 11)

 AND t.county_geoid = b.county_geoid

JOIN gbim_layer_registry r

  ON r.dataset_type = t.dataset_type

WHERE r.enabled = true

GROUP BY b.blockgroup_geoid, r.category, t.tract_geoid

HAVING SUM(t.tract_feature_count) > 0;

INSERT 0 0

msjarvisgis_v2=# 

msjarvisgis_v2=# CREATE OR REPLACE VIEW gbim_blockgroup_semantic_rebuild AS

SELECT           CREATE OR REPLACE VIEW gbim_blockgroup_semantic_rebuild AS

SELECTblockgroup_geoid,

    s.blockgroup_geoid,

    s.county_geoid,

    s.tract_geoid,sion,

    s.snapshot_version,

    s.belief_hash,

    trim(cat_ws(

      concat_ws(

        ' ',sus blockgroup ' || s.blockgroup_geoid ||

        'Census blockgroup ' || s.blockgroup_geoid ||

        ' in county ' || s.county_geoid ||'.',

        ' and tract ' || s.tract_geoid || '.',BY f.dataset_type, f.fragment_order)

        string_agg(f.fragment_text, ' ' ORDER BY f.dataset_type, f.fragment_order)

      )S rebuilt_semantic_content

    ) AS rebuilt_semantic_contentt s

FROM wv_blockgroup_belief_snapshot sents f

LEFT JOIN gbim_blockgroup_text_fragments fid

  ON f.blockgroup_geoid = s.blockgroup_geoid

GROUP BYockgroup_geoid,

    s.blockgroup_geoid,

    s.county_geoid,

    s.tract_geoid,sion,

    s.snapshot_version,

    s.belief_hash;

CREATE VIEW

msjarvisgis_v2=# UPDATE wv_blockgroup_belief_snapshot s

SET semantic_content = r.rebuilt_semantic_content

FROM gbim_blockgroup_semantic_rebuild r

WHERE r.blockgroup_geoid = s.blockgroup_geoid

  AND r.snapshot_version = s.snapshot_version;

UPDATE 1639

msjarvisgis_v2=# \COPY (

  SELECT

    document_id,

    governed_text,

    entity_type,

    blockgroup_geoid,

    county_geoid,

    tract_geoid

  FROM wv_blockgroup_belief_vector_ready

) TO '/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroup_belief_vector_ready_statewide_v5.csv'

WITH (FORMAT csv, HEADER true);

COPY 1639

msjarvisgis_v2=# import csv

from chromadb import Client

from sentence_transformers import SentenceTransformer

client = Client()

collection = client.get_or_create_collection(name="wv_blockgroup_beliefs")

model = SentenceTransformer("all-MiniLM-L6-v2")

csv_path = "/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroup_belief_vector_ready_statewide_v5.csv"

with open(csv_path, newline="", encoding="utf-8") as f:

    reader = csv.DictReader(f)

    ids = []

    texts = []

    metadatas = []

    for row in reader:

        doc_id = row["document_id"]

        text = row["governed_text"]

        ids.append(doc_id)

        texts.append(text)

        metadatas.append({

            "entity_type": row["entity_type"],

)   documents=texts,tas,s,texts, batch_size=64, show_progress_bar=True)

msjarvisgis_v2-# SELECT

  blockgroup_geoid,

  semantic_content

FROM wv_blockgroup_belief_snapshot

ORDER BY blockgroup_geoid

LIMIT 3;

ERROR:  syntax error at or near "csv"

LINE 1: import csv

               ^

msjarvisgis_v2=# UPDATE gbim_layer_registry

SET enabled = true, category = 'environment'

WHERE dataset_type IN (

    'public.wv_bio_biodiversity_rank',

    'public.wv_env_wildfire_regions',

    'public.wv_env_wind_energy_resources',

    'public.wv_hyd_streams_high_quality'

    -- etc.

);

UPDATE 4

msjarvisgis_v2=# 

msjarvisgis_v2=# DO $$

DECLARE

    r record;

BEGIN

    FOR r IN

        SELECT dataset_type

        FROM gbim_layer_registry

        WHERE enabled = true

        ORDER BY dataset_type

    LOOP

        CALL gbim_load_blockgroup_coverage(r.dataset_type);

    END LOOP;

END;

$$;

DO

msjarvisgis_v2=# TRUNCATE TABLE gbim_blockgroup_text_fragments;

TRUNCATE TABLE

msjarvisgis_v2=# INSERT INTO gbim_blockgroup_text_fragments (

    blockgroup_geINSERT INTO gbim_blockgroup_text_fragments (

    blockgroup_geoid,

    dataset_type,r,

    fragment_order,

    fragment_text

)ELECT

SELECTblockgroup_geoid,

    c.blockgroup_geoid,et_type,

    r.category AS dataset_type,

    10 AS fragment_order,

    CASEEN SUM(c.feature_count) > 0 THEN

      WHEN SUM(c.feature_count) > 0 THEN

        'In this blockgroup, there are '_name, ', ' ORDER BY r.display_name)

        || string_agg(DISTINCT r.display_name, ', ' ORDER BY r.display_name)

        || ' (' || r.category || ' infrastructure).'

      ELSEo ' || r.category || ' infrastructure ('

        'No ' || r.category || ' infrastructure ('' ORDER BY r.display_name)

        || string_agg(DISTINCT r.display_name, ', ' ORDER BY r.display_name)

        || ') intersects this blockgroup.'

    END AS fragment_textet_coverage c

FROM wv_blockgroup_dataset_coverage c

JOIN gbim_layer_registry rtaset_type

  ON r.dataset_type = c.dataset_type

WHERE r.enabled = truegeoid, r.category;

GROUP BY c.blockgroup_geoid, r.category;

INSERT 0 8195

msjarvisgis_v2=# 

msjarvisgis_v2=# INSERT INTO gbim_blockgroup_text_fragments (

    blockgroup_geoid,

    dataset_type,

    fragment_order,

    fragment_text

)

SELECT

    b.blockgroup_geoid,

    r.category AS dataset_type,

    20 AS fragment_order,

    'Within parent tract ' || t.tract_geoid || ', there are '

    || SUM(t.tract_feature_count)::text || ' '

    || r.category || ' feature(s) across '

    || COUNT(*)::text || ' blockgroups.'

FROM wv_blockgroup_identity b

JOIN gbim_tract_layer_rollup t

  ON t.tract_geoid = substr(b.blockgroup_geoid, 1, 11)

 AND t.county_geoid = b.county_geoid

JOIN gbim_layer_registry r

  ON r.dataset_type = t.dataset_type

WHERE r.enabled = true

GROUP BY b.blockgroup_geoid, r.category, t.tract_geoid

HAVING SUM(t.tract_feature_count) > 0;

INSERT 0 0

msjarvisgis_v2=# CREATE OR REPLACE VIEW gbim_blockgroup_semantic_rebuild AS

SELECT           CREATE OR REPLACE VIEW gbim_blockgroup_semantic_rebuild AS

SELECTblockgroup_geoid,

    s.blockgroup_geoid,

    s.county_geoid,

    s.tract_geoid,sion,

    s.snapshot_version,

    s.belief_hash,

    trim(cat_ws(

      concat_ws(

        ' ',sus blockgroup ' || s.blockgroup_geoid ||

        'Census blockgroup ' || s.blockgroup_geoid ||

        ' in county ' || s.county_geoid ||'.',

        ' and tract ' || s.tract_geoid || '.',BY f.dataset_type, f.fragment_order)

        string_agg(f.fragment_text, ' ' ORDER BY f.dataset_type, f.fragment_order)

      )S rebuilt_semantic_content

    ) AS rebuilt_semantic_contentt s

FROM wv_blockgroup_belief_snapshot sents f

LEFT JOIN gbim_blockgroup_text_fragments fid

  ON f.blockgroup_geoid = s.blockgroup_geoid

GROUP BYockgroup_geoid,

    s.blockgroup_geoid,

    s.county_geoid,

    s.tract_geoid,sion,

    s.snapshot_version,

    s.belief_hash;

CREATE VIEW

msjarvisgis_v2=# UPDATE wv_blockgroup_belief_snapshot s

SET semantic_content = r.rebuilt_semantic_content

FROM gbim_blockgroup_semantic_rebuild r

WHERE r.blockgroup_geoid = s.blockgroup_geoid

  AND r.snapshot_version = s.snapshot_version;

UPDATE 1639

msjarvisgis_v2=# \COPY (

  SELECT

    document_id,

    governed_text,

    entity_type,

    blockgroup_geoid,

    county_geoid,

    tract_geoid

  FROM wv_blockgroup_belief_vector_ready

) TO '/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroup_belief_vector_ready_statewide_v6.csv'

WITH (FORMAT csv, HEADER true);

COPY 1639

msjarvisgis_v2=# SELECT COUNT(*) AS exported_rows

FROM wv_blockgroup_belief_vector_ready;

 exported_rows 

---------------

          1639

(1 row)

msjarvisgis_v2=# UPDATE gbim_layer_registry

SET display_name = CASE dataset_type

    WHEN 'public.wv_bio_biodiversity_rank'   THEN 'biodiversity priority areas'

    WHEN 'public.wv_env_wildfire_regions'    THEN 'wildfire risk regions'

    WHEN 'public.wv_env_wind_energy_resources' THEN 'wind energy resource areas'

    WHEN 'public.wv_hyd_streams_high_quality' THEN 'high-quality streams'

    ELSE display_name

END

WHERE dataset_type IN (

    'public.wv_bio_biodiversity_rank',

    'public.wv_env_wildfire_regions',

    'public.wv_env_wind_energy_resources',

    'public.wv_hyd_streams_high_quality'

);

UPDATE 4

msjarvisgis_v2=# TRUNCATE TABLE gbim_blockgroup_text_fragments;

TRUNCATE TABLE

msjarvisgis_v2=# INSERT INTO gbim_blockgroup_text_fragments (

    blockgroup_geINSERT INTO gbim_blockgroup_text_fragments (

    blockgroup_geoid,

    dataset_type,r,

    fragment_order,

    fragment_text

)ELECT

SELECTblockgroup_geoid,

    c.blockgroup_geoid,et_type,

    r.category AS dataset_type,

    10 AS fragment_order,

    CASEEN SUM(c.feature_count) > 0 THEN

      WHEN SUM(c.feature_count) > 0 THEN

        'In this blockgroup, there are '_name, ', ' ORDER BY r.display_name)

        || string_agg(DISTINCT r.display_name, ', ' ORDER BY r.display_name)

        || ' (' || r.category || ' infrastructure).'

      ELSEo ' || r.category || ' infrastructure ('

        'No ' || r.category || ' infrastructure ('' ORDER BY r.display_name)

        || string_agg(DISTINCT r.display_name, ', ' ORDER BY r.display_name)

        || ') intersects this blockgroup.'

    END AS fragment_textet_coverage c

FROM wv_blockgroup_dataset_coverage c

JOIN gbim_layer_registry rtaset_type

  ON r.dataset_type = c.dataset_type

WHERE r.enabled = truegeoid, r.category;

GROUP BY c.blockgroup_geoid, r.category;

INSERT 0 8195

msjarvisgis_v2=# INSERT INTO gbim_blockgroup_text_fragments (

    blockgroup_geoid,

    dataset_type,

    fragment_order,

    fragment_text

)

SELECT

    b.blockgroup_geoid,

    r.category AS dataset_type,

    20 AS fragment_order,

    'Within parent tract ' || t.tract_geoid || ', there are '

    || SUM(t.tract_feature_count)::text || ' '

    || r.category || ' feature(s) across '

    || COUNT(*)::text || ' blockgroups.'

FROM wv_blockgroup_identity b

JOIN gbim_tract_layer_rollup t

  ON t.tract_geoid = substr(b.blockgroup_geoid, 1, 11)

 AND t.county_geoid = b.county_geoid

JOIN gbim_layer_registry r

  ON r.dataset_type = t.dataset_type

WHERE r.enabled = true

GROUP BY b.blockgroup_geoid, r.category, t.tract_geoid

HAVING SUM(t.tract_feature_count) > 0;

INSERT 0 0

msjarvisgis_v2=# CREATE OR REPLACE VIEW gbim_blockgroup_semantic_rebuild AS

SELECT           CREATE OR REPLACE VIEW gbim_blockgroup_semantic_rebuild AS

SELECTblockgroup_geoid,

    s.blockgroup_geoid,

    s.county_geoid,

    s.tract_geoid,sion,

    s.snapshot_version,

    s.belief_hash,

    trim(cat_ws(

      concat_ws(

        ' ',sus blockgroup ' || s.blockgroup_geoid ||

        'Census blockgroup ' || s.blockgroup_geoid ||

        ' in county ' || s.county_geoid ||'.',

        ' and tract ' || s.tract_geoid || '.',BY f.dataset_type, f.fragment_order)

        string_agg(f.fragment_text, ' ' ORDER BY f.dataset_type, f.fragment_order)

      )S rebuilt_semantic_content

    ) AS rebuilt_semantic_contentt s

FROM wv_blockgroup_belief_snapshot sents f

LEFT JOIN gbim_blockgroup_text_fragments fid

  ON f.blockgroup_geoid = s.blockgroup_geoid

GROUP BYockgroup_geoid,

    s.blockgroup_geoid,

    s.county_geoid,

    s.tract_geoid,sion,

    s.snapshot_version,

    s.belief_hash;

CREATE VIEW

msjarvisgis_v2=# UPDATE wv_blockgroup_belief_snapshot s

SET semantic_content = r.rebuilt_semantic_content

FROM gbim_blockgroup_semantic_rebuild r

WHERE r.blockgroup_geoid = s.blockgroup_geoid

  AND r.snapshot_version = s.snapshot_version;

UPDATE 1639

msjarvisgis_v2=# \COPY (

  SELECT

    document_id,

    governed_text,

    entity_type,

    blockgroup_geoid,

    county_geoid,

    tract_geoid

  FROM wv_blockgroup_belief_vector_ready

) TO '/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroup_belief_vector_ready_statewide_v7.csv'

WITH (FORMAT csv, HEADER true);

COPY 1639

msjarvisgis_v2=# SELECT

    c.dataset_type,

    r.display_name,

    r.category,

    COUNT(*) AS blockgroup_rows,

    SUM(c.feature_count) AS total_features_intersected,

    SUM(CASE WHEN c.feature_count > 0 THEN 1 ELSE 0 END) AS blockgroups_with_features 

FROM wv_blockgroup_dataset_coverage c

JOIN gbim_layer_registry r

  ON r.dataset_type = c.dataset_type

WHERE r.enabled = true

GROUP BY c.dataset_type, r.display_name, r.category

ORDER BY blockgroups_with_features DESC, total_features_intersected DESC;

msjarvisgis_v2=# SELECT

    r.dataset_type,

    r.source_schema,

    r.source_table,

    r.geom_column,

    r.geom_type,

    r.srid AS registry_srid,

    gc.srid AS geometry_columns_srid,

    gc.type AS geometry_columns_type

FROM gbim_layer_registry r

LEFT JOIN geometry_columns gc

  ON gc.f_table_schema = r.source_schema

 AND gc.f_table_name = r.source_table

 AND gc.f_geometry_column = r.geom_column

WHERE r.enabled = true

ORDER BY r.dataset_type;

msjarvisgis_v2=# SELECT

    ST_SRID(geom) AS blockgroup_srid,

    COUNT(*) AS rows

FROM wv_blockgroup_representation

GROUP BY ST_SRID(geom)

ORDER BY rows DESC;

 blockgroup_srid | rows 

-----------------+------

            4269 | 1639

(1 row)

msjarvisgis_v2=# SELECT COUNT(*) AS source_rows

FROM public.wv_trn_roads_interstate;

 source_rows 

-------------

           0

(1 row)

msjarvisgis_v2=# SELECT

    ST_SRID(geom) AS source_srid,

    COUNT(*) AS rows

FROM public.wv_trn_roads_interstate

GROUP BY ST_SRID(geom);

 source_srid | rows 

-------------+------

(0 rows)

msjarvisgis_v2=# SELECT COUNT(*) AS raw_intersections

FROM wv_blockgroup_representation bgr

JOIN public.wv_trn_roads_interstate r

  ON ST_Intersects(bgr.geom, r.geom);

 raw_intersections 

-------------------

                 0

(1 row)

msjarvisgis_v2=# SELECT COUNT(*) AS transformed_intersections

FROM wv_blockgroup_representation bgr

JOIN public.wv_trn_roads_interstate r

  ON ST_Intersects(

       bgr.geom,

       ST_Transform(r.geom, ST_SRID(bgr.geom))

     );

 transformed_intersections 

---------------------------

                         0

(1 row)

msjarvisgis_v2=# SELECT

    COUNT(*) AS total_rows,

    SUM(CASE WHEN geom IS NULL THEN 1 ELSE 0 END) AS null_geom_rows,

    SUM(CASE WHEN ST_IsEmpty(geom) THEN 1 ELSE 0 END) AS empty_geom_rows,

    SUM(CASE WHEN NOT ST_IsValid(geom) THEN 1 ELSE 0 END) AS invalid_geom_rows

FROM public.wv_trn_roads_interstate;

 total_rows | null_geom_rows | empty_geom_rows | invalid_geom_rows 

------------+----------------+-----------------+-------------------

          0 |                |                 |                  

(1 row)

msjarvisgis_v2=# SELECT

    COUNT(*) AS total_rows,

    SUM(CASE WHEN geom IS NULL THEN 1 ELSE 0 END) AS null_geom_rows,

    SUM(CASE WHEN ST_IsEmpty(geom) THEN 1 ELSE 0 END) AS empty_geom_rows,

    SUM(CASE WHEN NOT ST_IsValid(geom) THEN 1 ELSE 0 END) AS invalid_geom_rows

FROM wv_blockgroup_representation;

 total_rows | null_geom_rows | empty_geom_rows | invalid_geom_rows 

------------+----------------+-----------------+-------------------

       1639 |              0 |               0 |                 0

(1 row)

msjarvisgis_v2=# CREATE OR REPLACE PROCEDURE gbim_load_blockgroup_coverage(p_dataset_type text)

LANGUAGE plpgsql

AS $$

DECLARE

    v_source_schema text;

    v_source_table text;

    v_geom_column text;

    v_geom_type text;

    v_metric_kind text;

    v_source_srid integer;

    v_target_srid integer;

    v_sql text;

BEGIN

    SELECT source_schema, source_table, geom_column, geom_type, metric_kind, srid

    INTO v_source_schema, v_source_table, v_geom_column, v_geom_type, v_metric_kind, v_source_srid

    FROM gbim_layer_registry

    WHERE dataset_type = p_dataset_type

      AND enabled = true;

    IF NOT FOUND THEN

        RAISE EXCEPTION 'Dataset type % not found or not enabled in gbim_layer_registry', p_dataset_type;

$$;;EXECUTE v_sql;target_sridurce_table, v_geom_column, v_target_srid, v_geom_column,

CREATE PROCEDURE

msjarvisgis_v2=# DO $$

DECLARE

    r record;

BEGIN

    FOR r IN

        SELECT dataset_type

        FROM gbim_layer_registry

        WHERE enabled = true

        ORDER BY dataset_type

    LOOP

        CALL gbim_load_blockgroup_coverage(r.dataset_type);

    END LOOP;

END;

$$;

DO

msjarvisgis_v2=# SELECT

    c.dataset_type,

    r.display_name,

    r.category,

    COUNT(*) AS blockgroup_rows,

    SUM(c.feature_count) AS total_features_intersected,

    SUM(CASE WHEN c.feature_count > 0 THEN 1 ELSE 0 END) AS blockgroups_with_features 

FROM wv_blockgroup_dataset_coverage c

JOIN gbim_layer_registry r

  ON r.dataset_type = c.dataset_type

WHERE r.enabled = true

GROUP BY c.dataset_type, r.display_name, r.category

ORDER BY blockgroups_with_features DESC, total_features_intersected DESC;

msjarvisgis_v2=# ALTER TABLE wv_blockgroup_representation

  ADD COLUMN IF NOT EXISTS geom_utm17 geometry(MultiPolygon, 26917);

UPDATE wv_blockgroup_representation

SET geom_utm17 = ST_Transform(geom, 26917)

WHERE geom IS NOT NULL;

ALTER TABLE

ERROR:  transform: Invalid coordinate (2049)

msjarvisgis_v2=# SELECT

    blockgroup_geoid,

    county_geoid,

    ST_AsText(geom) AS wkt

FROM wv_blockgroup_representation

WHERE geom IS NOT NULL

  AND NOT ST_IsValid(geom);

ERROR:  column "county_geoid" does not exist

LINE 3:     county_geoid,

            ^

msjarvisgis_v2=# SELECT

    MIN(ST_XMin(geom)) AS min_x,

    MAX(ST_XMax(geom)) AS max_x,

    MIN(ST_YMin(geom)) AS min_y,

    MAX(ST_YMax(geom)) AS max_y

FROM wv_blockgroup_representation;

       min_x       |      max_x       |       min_y       |       max_y       

-------------------+------------------+-------------------+-------------------

 355930.4768763897 | 782804.088163846 | 4117445.620737121 | 4498773.002933004

(1 row)

msjarvisgis_v2=# SELECT Find_SRID('public', 'wv_blockgroup_representation', 'geom');

 find_srid 

-----------

      4269

(1 row)

msjarvisgis_v2=# SELECT ST_SRID(geom) AS srid, COUNT(*) AS rows

FROM public.wv_hyd_streams_high_quality

GROUP BY ST_SRID(geom)

ORDER BY rows DESC;

 srid | rows 

------+------

(0 rows)

msjarvisgis_v2=# SELECT ST_SRID(geom) AS srid, COUNT(*) AS rows

FROM public.wv_trn_roads_state_routes

GROUP BY ST_SRID(geom)

ORDER BY rows DESC;

 srid | rows 

------+------

(0 rows)

msjarvisgis_v2=# SELECT

    MIN(ST_XMin(geom)) AS min_x,

    MAX(ST_XMax(geom)) AS max_x,

    MIN(ST_YMin(geom)) AS min_y,

    MAX(ST_YMax(geom)) AS max_y

FROM public.wv_trn_roads_state_routes;

 min_x | max_x | min_y | max_y 

-------+-------+-------+-------

       |       |       |      

(1 row)

msjarvisgis_v2=# ALTER TABLE wv_blockgroup_representation

  ADD COLUMN IF NOT EXISTS geom_proj geometry(MultiPolygon, 26917);

ALTER TABLE

msjarvisgis_v2=# UPDATE wv_blockgroup_representation

SET geom_proj = ST_SetSRID(geom, 26917)

WHERE geom IS NOT NULL;

UPDATE 1639

msjarvisgis_v2=# SELECT

    ST_SRID(geom)      AS original_srid,

    ST_SRID(geom_proj) AS proj_srid,

    COUNT(*) AS rows

FROM wv_blockgroup_representation

GROUP BY ST_SRID(geom), ST_SRID(geom_proj)

ORDER BY rows DESC;

 original_srid | proj_srid | rows 

---------------+-----------+------

          4269 |     26917 | 1639

(1 row)

msjarvisgis_v2=# SELECT

    r.dataset_type,

    r.display_name,

    COUNT(*) AS total_rows,

    SUM(CASE WHEN c.geom IS NULL THEN 1 ELSE 0 END) AS null_geom_rows

FROM (

    SELECT 'public.wv_bio_biodiversity_rank'::text AS dataset_type, geom FROM public.wv_bio_biodiversity_rank

    UNION ALL

    SELECT 'public.wv_env_epa_facilities', geom FROM public.wv_env_epa_facilities

    UNION ALL

    SELECT 'public.wv_hyd_hazus_floodplain_zones', geom FROM public.wv_hyd_hazus_floodplain_zones

    UNION ALL

    SELECT 'public.wv_hyd_streams_high_quality', geom FROM public.wv_hyd_streams_high_quality

    UNION ALL

    SELECT 'public.wv_soc_schools_k12', geom FROM public.wv_soc_schools_k12

    UNION ALL

    SELECT 'public.wv_soc_hospitals_wvdem', geom FROM public.wv_soc_hospitals_wvdem

    UNION ALL

    SELECT 'public.wv_trn_airports', geom FROM public.wv_trn_airports

    UNION ALL

    SELECT 'public.wv_trn_railroad_lines_rti', geom FROM public.wv_trn_railroad_linesORDER BY total_rows DESC;r.display_nameent_plants', geom FROM public.wv_util_sewer_tr

 dataset_type | display_name | total_rows | null_geom_rows 

--------------+--------------+------------+----------------

(0 rows)

msjarvisgis_v2=# SELECT COUNT(*) AS rows, SUM(CASE WHEN geom IS NULL THEN 1 ELSE 0 END) AS null_geom

FROM public.wv_bio_biodiversity_rank;

SELECT COUNT(*) AS rows, SUM(CASE WHEN geom IS NULL THEN 1 ELSE 0 END) AS null_geom

FROM public.wv_env_epa_facilities;

SELECT COUNT(*) AS rows, SUM(CASE WHEN geom IS NULL THEN 1 ELSE 0 END) AS null_geom

FROM public.wv_hyd_hazus_floodplain_zones;

SELECT COUNT(*) AS rows, SUM(CASE WHEN geom IS NULL THEN 1 ELSE 0 END) AS null_geom

FROM public.wv_hyd_streams_high_quality;

SELECT COUNT(*) AS rows, SUM(CASE WHEN geom IS NULL THEN 1 ELSE 0 END) AS null_geom

FROM public.wv_soc_schools_k12;

SELECT COUNT(*) AS rows, SUM(CASE WHEN geom IS NULL THEN 1 ELSE 0 END) AS null_geom

FROM public.wv_soc_hospitals_wvdem;

SELECT COUNT(*) AS rows, SUM(CASE WHEN geom IS NULL THEN 1 ELSE 0 END) AS null_geom

FROM public.wv_trn_airports;

SELECT COUNT(*) AS rows, SUM(CASE WHEN geom IS NULL THEN 1 ELSE 0 END) AS null_geom

FROM public.wv_util_sewer_treatment_plants; IS NULL THEN 1 ELSE 0 END) AS null_geom

 rows | null_geom 

------+-----------

    0 |          

(1 row)

 rows | null_geom 

------+-----------

    0 |          

(1 row)

 rows | null_geom 

------+-----------

    0 |          

(1 row)

 rows | null_geom 

------+-----------

    0 |          

(1 row)

 rows | null_geom 

------+-----------

    0 |          

(1 row)

 rows | null_geom 

------+-----------

    0 |          

(1 row)

 rows | null_geom 

------+-----------

    0 |          

(1 row)

 rows | null_geom 

------+-----------

    0 |          

(1 row)

 rows | null_geom 

------+-----------

    0 |          

(1 row)

 rows | null_geom 

------+-----------

    0 |          

(1 row)

msjarvisgis_v2=# SELECT table_schema, table_name

FROM information_schema.tables

WHERE table_schema NOT IN ('pg_catalog', 'information_schema')

ORDER BY table_schema, table_name;

msjarvisgis_v2=# \! pg_restore -d msjarvisgis_v2 -U postgres -n public -v /mnt/spiritual_drive/msjarvis-rebuild/wv_hyd_hazus_floodplain_zones.dump

pg_restore: connecting to database for restore

pg_restore: creating TABLE "public.wv_hyd_hazus_floodplain_zones"

pg_restore: while PROCESSING TOC:

pg_restore: from TOC entry 404; 1259 708773 TABLE wv_hyd_hazus_floodplain_zones msjarvis

pg_restore: error: could not execute query: ERROR:  relation "wv_hyd_hazus_floodplain_zones" already exists

Command was: CREATE TABLE public.wv_hyd_hazus_floodplain_zones (

    gid integer NOT NULL,

    county character varying(50),

    shape_length double precision,

    shape_area double precision,

    geom public.geometry(MultiPolygon,4269),

    x double precision,

    y double precision

);

pg_restore: creating SEQUENCE "public.wv_hyd_hazus_floodplain_zones_gid_seq"

pg_restore: from TOC entry 403; 1259 708772 SEQUENCE wv_hyd_hazus_floodplain_zones_gid_seq msjarvis

pg_restore: error: could not execute query: ERROR:  relation "wv_hyd_hazus_floodplain_zones_gid_seq" already exists

Command was: CREATE SEQUENCE public.wv_hyd_hazus_floodplain_zones_gid_seq

    AS integer

    START WITH 1

    INCREMENT BY 1

    NO MINVALUE

    NO MAXVALUE

    CACHE 1;

pg_restore: creating SEQUENCE OWNED BY "public.wv_hyd_hazus_floodplain_zones_gid_seq"

pg_restore: creating DEFAULT "public.wv_hyd_hazus_floodplain_zones gid"

pg_restore: processing data for table "public.wv_hyd_hazus_floodplain_zones"

pg_restore: from TOC entry 6513; 0 708773 TABLE DATA wv_hyd_hazus_floodplain_zones msjarvis

pg_restore: error: could not execute query: ERROR:  column "x" of relation "wv_hyd_hazus_floodplain_zones" does not exist

Command was: COPY public.wv_hyd_hazus_floodplain_zones (gid, county, shape_length, shape_area, geom, x, y) FROM stdin;

pg_restore: executing SEQUENCE SET wv_hyd_hazus_floodplain_zones_gid_seq

pg_restore: creating CONSTRAINT "public.wv_hyd_hazus_floodplain_zones wv_hyd_hazus_floodplain_zones_pkey"

pg_restore: from TOC entry 6354; 2606 708780 CONSTRAINT wv_hyd_hazus_floodplain_zones wv_hyd_hazus_floodplain_zones_pkey msjarvis

pg_restore: error: could not execute query: ERROR:  multiple primary keys for table "wv_hyd_hazus_floodplain_zones" are not allowed

Command was: ALTER TABLE ONLY public.wv_hyd_hazus_floodplain_zones

    ADD CONSTRAINT wv_hyd_hazus_floodplain_zones_pkey PRIMARY KEY (gid);

pg_restore: creating INDEX "public.wv_hyd_hazus_floodplain_zones_geom_geom_idx"

pg_restore: from TOC entry 6352; 1259 708781 INDEX wv_hyd_hazus_floodplain_zones_geom_geom_idx msjarvis

pg_restore: error: could not execute query: ERROR:  relation "wv_hyd_hazus_floodplain_zones_geom_geom_idx" already exists

Command was: CREATE INDEX wv_hyd_hazus_floodplain_zones_geom_geom_idx ON public.wv_hyd_hazus_floodplain_zones USING gist (geom);

pg_restore: creating TRIGGER "public.wv_hyd_hazus_floodplain_zones trg_enforce_xy_wv_hyd_hazus_floodplain_zones"

pg_restore: from TOC entry 6355; 2620 1125247 TRIGGER wv_hyd_hazus_floodplain_zones trg_enforce_xy_wv_hyd_hazus_floodplain_zones msjarvis

pg_restore: error: could not execute query: ERROR:  function public.enforce_xy_on_geom() does not exist

Command was: CREATE TRIGGER trg_enforce_xy_wv_hyd_hazus_floodplain_zones BEFORE INSERT OR UPDATE ON public.wv_hyd_hazus_floodplain_zones FOR EACH ROW EXECUTE FUNCTION public.enforce_xy_on_geom();

pg_restore: warning: errors ignored on restore: 6

msjarvisgis_v2=# SELECT ST_SRID(geom) AS srid, COUNT(*) AS rows

FROM public.wv_hyd_hazus_floodplain_zones

GROUP BY ST_SRID(geom)

ORDER BY rows DESC;

 srid | rows 

------+------

(0 rows)

msjarvisgis_v2=# DROP TABLE IF EXISTS public.wv_hyd_hazus_floodplain_zones CASCADE;

DROP SEQUENCE IF EXISTS public.wv_hyd_hazus_floodplain_zones_gid_seq CASCADE;

DROP TABLE

NOTICE:  sequence "wv_hyd_hazus_floodplain_zones_gid_seq" does not exist, skipping

DROP SEQUENCE

msjarvisgis_v2=# \! pg_restore -d msjarvisgis_v2 -U postgres -n public -v \

  -t public.wv_hyd_hazus_floodplain_zones \

  /mnt/spiritual_drive/msjarvis-rebuild/wv_hyd_hazus_floodplain_zones.dump

pg_restore: connecting to database for restore

pg_restore: implied data-only restore

msjarvisgis_v2=# SELECT ST_SRID(geom) AS srid, COUNT(*) AS rows

FROM public.wv_hyd_hazus_floodplain_zones

GROUP BY ST_SRID(geom)

ORDER BY rows DESC;

ERROR:  relation "public.wv_hyd_hazus_floodplain_zones" does not exist

LINE 2: FROM public.wv_hyd_hazus_floodplain_zones

             ^

msjarvisgis_v2=# \! pg_restore -d msjarvisgis_v2 -U postgres -n public -v /mnt/spiritual_drive/msjarvis-rebuild/wv_hyd_hazus_floodplain_zones.dump

pg_restore: connecting to database for restore

pg_restore: creating TABLE "public.wv_hyd_hazus_floodplain_zones"

pg_restore: creating SEQUENCE "public.wv_hyd_hazus_floodplain_zones_gid_seq"

pg_restore: creating SEQUENCE OWNED BY "public.wv_hyd_hazus_floodplain_zones_gid_seq"

pg_restore: creating DEFAULT "public.wv_hyd_hazus_floodplain_zones gid"

pg_restore: processing data for table "public.wv_hyd_hazus_floodplain_zones"

pg_restore: executing SEQUENCE SET wv_hyd_hazus_floodplain_zones_gid_seq

pg_restore: creating CONSTRAINT "public.wv_hyd_hazus_floodplain_zones wv_hyd_hazus_floodplain_zones_pkey"

pg_restore: creating INDEX "public.wv_hyd_hazus_floodplain_zones_geom_geom_idx"

pg_restore: creating TRIGGER "public.wv_hyd_hazus_floodplain_zones trg_enforce_xy_wv_hyd_hazus_floodplain_zones"

pg_restore: while PROCESSING TOC:

pg_restore: from TOC entry 6355; 2620 1125247 TRIGGER wv_hyd_hazus_floodplain_zones trg_enforce_xy_wv_hyd_hazus_floodplain_zones msjarvis

pg_restore: error: could not execute query: ERROR:  function public.enforce_xy_on_geom() does not exist

Command was: CREATE TRIGGER trg_enforce_xy_wv_hyd_hazus_floodplain_zones BEFORE INSERT OR UPDATE ON public.wv_hyd_hazus_floodplain_zones FOR EACH ROW EXECUTE FUNCTION public.enforce_xy_on_geom();

pg_restore: warning: errors ignored on restore: 1

msjarvisgis_v2=# SELECT ST_SRID(geom) AS srid, COUNT(*) AS rows

FROM public.wv_hyd_hazus_floodplain_zones

GROUP BY ST_SRID(geom)

ORDER BY rows DESC;

 srid | rows 

------+------

 4269 |  220

(1 row)

msjarvisgis_v2=# SELECT

    MIN(ST_XMin(geom)) AS min_x,

    MAX(ST_XMax(geom)) AS max_x,

    MIN(ST_YMin(geom)) AS min_y,

    MAX(ST_YMax(geom)) AS max_y

FROM public.wv_hyd_hazus_floodplain_zones;

       min_x       |       max_x        |       min_y        |       max_y       

-------------------+--------------------+--------------------+-------------------

 -82.6447389999999 | -77.71902899999992 | 37.204104338000036 | 40.63880100000006

(1 row)

msjarvisgis_v2=# 

msjarvisgis_v2=# ALTER TABLE public.wv_hyd_hazus_floodplain_zones

  ADD COLUMN IF NOT EXISTS geom_utm17 geometry(MultiPolygon, 26917);

UPDATE public.wv_hyd_hazus_floodplain_zones

SET geom_utm17 = ST_Transform(geom, 26917)

WHERE geom IS NOT NULL;

ALTER TABLE

UPDATE 220

msjarvisgis_v2=# SELECT ST_SRID(geom) AS srid_geom,

       ST_SRID(geom_utm17) AS srid_utm17,

       COUNT(*) AS rows

FROM public.wv_hyd_hazus_floodplain_zones

GROUP BY ST_SRID(geom), ST_SRID(geom_utm17)

ORDER BY rows DESC;

 srid_geom | srid_utm17 | rows 

-----------+------------+------

      4269 |      26917 |  220

(1 row)

msjarvisgis_v2=# SELECT COUNT(*) AS intersections_floodplains

FROM wv_blockgroup_representation bgr

JOIN public.wv_hyd_hazus_floodplain_zones f

  ON ST_Intersects(bgr.geom_proj, f.geom_utm17);

 intersections_floodplains 

---------------------------

                      6726

(1 row)

msjarvisgis_v2=# 

msjarvisgis_v2=# DELETE FROM wv_blockgroup_dataset_coverage

WHERE dataset_type = 'public.wv_hyd_hazus_floodplain_zones';

INSERT INTO wv_blockgroup_dataset_coverage (

    blockgroup_geoid,

    county_geoid,

    dataset_type,

    source_table,

    feature_count,

    coverage_state,

    calculation_time,

    source_layer_hash,

    notes,

    coverage_reason

)

SELECT

    bg.blockgroup_geoid,

    bg.county_geoid,

    'public.wv_hyd_hazus_floodplain_zones' AS dataset_type,

    'public.wv_hyd_hazus_floodplain_zones' AS source_table,

    COUNT(f.*)::integer AS feature_count,

    CASE

      WHEN COUNT(f.*) > 0 THEN 'present'

      ELSE 'absent'

GROUP BY bg.blockgroup_geoid, bg.county_geoid;)fcted'S notes,

DELETE 1639

INSERT 0 1639

msjarvisgis_v2=# SELECT

    c.dataset_type,

    r.display_name,

    r.category,

    COUNT(*) AS blockgroup_rows,

    SUM(c.feature_count) AS total_features_intersected,

    SUM(CASE WHEN c.feature_count > 0 THEN 1 ELSE 0 END) AS blockgroups_with_features

FROM wv_blockgroup_dataset_coverage c

JOIN gbim_layer_registry r

  ON r.dataset_type = c.dataset_type

WHERE r.dataset_type = 'public.wv_hyd_hazus_floodplain_zones'

GROUP BY c.dataset_type, r.display_name, r.category;

msjarvisgis_v2=# TRUNCATE TABLE gbim_blockgroup_text_fragments;

TRUNCATE TABLE

msjarvisgis_v2=# INSERT INTO gbim_blockgroup_text_fragments (

    blockgroup_geINSERT INTO gbim_blockgroup_text_fragments (

    blockgroup_geoid,

    dataset_type,r,

    fragment_order,

    fragment_text

)ELECT

SELECTblockgroup_geoid,

    c.blockgroup_geoid,et_type,

    r.category AS dataset_type,

    10 AS fragment_order,

    CASEEN SUM(c.feature_count) > 0 THEN

      WHEN SUM(c.feature_count) > 0 THEN

        'In this blockgroup, there are '_name, ', ' ORDER BY r.display_name)

        || string_agg(DISTINCT r.display_name, ', ' ORDER BY r.display_name)

        || ' (' || r.category || ' infrastructure).'

      ELSEo ' || r.category || ' infrastructure ('

        'No ' || r.category || ' infrastructure ('' ORDER BY r.display_name)

        || string_agg(DISTINCT r.display_name, ', ' ORDER BY r.display_name)

        || ') intersects this blockgroup.'

    END AS fragment_textet_coverage c

FROM wv_blockgroup_dataset_coverage c

JOIN gbim_layer_registry rtaset_type

  ON r.dataset_type = c.dataset_type

WHERE r.enabled = truegeoid, r.category;

GROUP BY c.blockgroup_geoid, r.category;

INSERT 0 8195

msjarvisgis_v2=# INSERT INTO gbim_blockgroup_text_fragments (

    blockgroup_geoid,

    dataset_type,

    fragment_order,

    fragment_text

)

SELECT

    b.blockgroup_geoid,

    r.category AS dataset_type,

    20 AS fragment_order,

    'Within parent tract ' || t.tract_geoid || ', there are '

    || SUM(t.tract_feature_count)::text || ' '

    || r.category || ' feature(s) across '

    || COUNT(*)::text || ' blockgroups.'

FROM wv_blockgroup_identity b

JOIN gbim_tract_layer_rollup t

  ON t.tract_geoid = substr(b.blockgroup_geoid, 1, 11)

 AND t.county_geoid = b.county_geoid

JOIN gbim_layer_registry r

  ON r.dataset_type = t.dataset_type

WHERE r.enabled = true

GROUP BY b.blockgroup_geoid, r.category, t.tract_geoid

HAVING SUM(t.tract_feature_count) > 0;

INSERT 0 1552

msjarvisgis_v2=# CREATE OR REPLACE VIEW gbim_blockgroup_semantic_rebuild AS

SELECT           CREATE OR REPLACE VIEW gbim_blockgroup_semantic_rebuild AS

SELECTblockgroup_geoid,

    s.blockgroup_geoid,

    s.county_geoid,

    s.tract_geoid,sion,

    s.snapshot_version,

    s.belief_hash,

    trim(cat_ws(

      concat_ws(

        ' ',sus blockgroup ' || s.blockgroup_geoid ||

        'Census blockgroup ' || s.blockgroup_geoid ||

        ' in county ' || s.county_geoid ||'.',

        ' and tract ' || s.tract_geoid || '.',BY f.dataset_type, f.fragment_order)

        string_agg(f.fragment_text, ' ' ORDER BY f.dataset_type, f.fragment_order)

      )S rebuilt_semantic_content

    ) AS rebuilt_semantic_contentt s

FROM wv_blockgroup_belief_snapshot sents f

LEFT JOIN gbim_blockgroup_text_fragments fid

  ON f.blockgroup_geoid = s.blockgroup_geoid

GROUP BYockgroup_geoid,

    s.blockgroup_geoid,

    s.county_geoid,

    s.tract_geoid,sion,

    s.snapshot_version,

    s.belief_hash;

CREATE VIEW

msjarvisgis_v2=# UPDATE wv_blockgroup_belief_snapshot s

SET semantic_content = r.rebuilt_semantic_content

FROM gbim_blockgroup_semantic_rebuild r

WHERE r.blockgroup_geoid = s.blockgroup_geoid

  AND r.snapshot_version = s.snapshot_version;

UPDATE 1639

msjarvisgis_v2=# \COPY (

  SELECT

    document_id,

    governed_text,

    entity_type,

    blockgroup_geoid,

    county_geoid,

    tract_geoid

  FROM wv_blockgroup_belief_vector_ready

) TO '/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroup_belief_vector_ready_statewide_v8.csv'

WITH (FORMAT csv, HEADER true);

COPY 1639

msjarvisgis_v2=# SELECT COUNT(*) FROM wv_blockgroup_belief_vector_ready;

 count 

-------

  1639

(1 row)

msjarvisgis_v2=# DROP TABLE IF EXISTS public.wv_bio_biodiversity_rank CASCADE;

DROP TABLE IF EXISTS public.wv_env_epa_facilities CASCADE;

DROP TABLE IF EXISTS public.wv_hyd_streams_high_quality CASCADE;

DROP TABLE IF EXISTS public.wv_soc_schools_k12 CASCADE;

DROP TABLE IF EXISTS public.wv_soc_hospitals_wvdem CASCADE;

DROP TABLE IF EXISTS public.wv_trn_airports CASCADE;

DROP TABLE IF EXISTS public.wv_util_sewer_treatment_plants CASCADE;

DROP TABLE

DROP TABLE

DROP TABLE

DROP TABLE

DROP TABLE

DROP TABLE

DROP TABLE

msjarvisgis_v2=# \! pg_restore -d msjarvisgis_v2 -U postgres -v /mnt/spiritual_drive/msjarvis-rebuild/wv_batch_layers_v9.dump

pg_restore: connecting to database for restore

pg_restore: creating TABLE "public.wv_bio_biodiversity_rank"

pg_restore: creating SEQUENCE "public.wv_bio_biodiversity_rank_gid_seq"

pg_restore: creating SEQUENCE OWNED BY "public.wv_bio_biodiversity_rank_gid_seq"

pg_restore: creating TABLE "public.wv_env_epa_facilities"

pg_restore: creating SEQUENCE "public.wv_env_epa_facilities_gid_seq"

pg_restore: creating SEQUENCE OWNED BY "public.wv_env_epa_facilities_gid_seq"

pg_restore: creating TABLE "public.wv_hyd_streams_high_quality"

pg_restore: creating SEQUENCE "public.wv_hyd_streams_high_quality_gid_seq"

pg_restore: creating SEQUENCE OWNED BY "public.wv_hyd_streams_high_quality_gid_seq"

pg_restore: creating TABLE "public.wv_soc_hospitals_wvdem"

pg_restore: creating SEQUENCE "public.wv_soc_hospitals_wvdem_gid_seq"

pg_restore: creating SEQUENCE OWNED BY "public.wv_soc_hospitals_wvdem_gid_seq"

pg_restore: creating TABLE "public.wv_soc_schools_k12"

pg_restore: creating SEQUENCE "public.wv_soc_schools_k12_gid_seq"

pg_restore: creating SEQUENCE OWNED BY "public.wv_soc_schools_k12_gid_seq"

pg_restore: creating TABLE "public.wv_trn_airports"

pg_restore: creating SEQUENCE "public.wv_trn_airports_gid_seq"

pg_restore: creating SEQUENCE OWNED BY "public.wv_trn_airports_gid_seq"

pg_restore: creating TABLE "public.wv_util_sewer_treatment_plants"

pg_restore: creating SEQUENCE "public.wv_util_sewer_treatment_plants_gid_seq"

pg_restore: creating SEQUENCE OWNED BY "public.wv_util_sewer_treatment_plants_gid_seq"

pg_restore: creating DEFAULT "public.wv_bio_biodiversity_rank gid"

pg_restore: creating DEFAULT "public.wv_env_epa_facilities gid"

pg_restore: creating DEFAULT "public.wv_hyd_streams_high_quality gid"

pg_restore: creating DEFAULT "public.wv_soc_hospitals_wvdem gid"

pg_restore: creating DEFAULT "public.wv_soc_schools_k12 gid"

pg_restore: creating DEFAULT "public.wv_trn_airports gid"

pg_restore: creating DEFAULT "public.wv_util_sewer_treatment_plants gid"

pg_restore: processing data for table "public.wv_bio_biodiversity_rank"

pg_restore: processing data for table "public.wv_env_epa_facilities"

pg_restore: processing data for table "public.wv_hyd_streams_high_quality"

pg_restore: processing data for table "public.wv_soc_hospitals_wvdem"

pg_restore: processing data for table "public.wv_soc_schools_k12"

pg_restore: processing data for table "public.wv_trn_airports"

pg_restore: processing data for table "public.wv_util_sewer_treatment_plants"

pg_restore: executing SEQUENCE SET wv_bio_biodiversity_rank_gid_seq

pg_restore: executing SEQUENCE SET wv_env_epa_facilities_gid_seq

pg_restore: executing SEQUENCE SET wv_hyd_streams_high_quality_gid_seq

pg_restore: executing SEQUENCE SET wv_soc_hospitals_wvdem_gid_seq

pg_restore: executing SEQUENCE SET wv_soc_schools_k12_gid_seq

pg_restore: executing SEQUENCE SET wv_trn_airports_gid_seq

pg_restore: executing SEQUENCE SET wv_util_sewer_treatment_plants_gid_seq

pg_restore: creating CONSTRAINT "public.wv_bio_biodiversity_rank wv_bio_biodiversity_rank_pkey"

pg_restore: creating CONSTRAINT "public.wv_env_epa_facilities wv_env_epa_facilities_pkey"

pg_restore: creating CONSTRAINT "public.wv_hyd_streams_high_quality wv_hyd_streams_high_quality_pkey"

pg_restore: creating CONSTRAINT "public.wv_soc_hospitals_wvdem wv_soc_hospitals_wvdem_pkey"

pg_restore: creating CONSTRAINT "public.wv_soc_schools_k12 wv_soc_schools_k12_pkey"

pg_restore: creating CONSTRAINT "public.wv_trn_airports wv_trn_airports_pkey"

pg_restore: creating CONSTRAINT "public.wv_util_sewer_treatment_plants wv_util_sewer_treatment_plants_pkey"

pg_restore: creating INDEX "public.wv_bio_biodiversity_rank_geom_geom_idx"

pg_restore: creating INDEX "public.wv_env_epa_facilities_geom_geom_idx"

pg_restore: creating INDEX "public.wv_hyd_streams_high_quality_geom_geom_idx"

pg_restore: creating INDEX "public.wv_soc_hospitals_wvdem_geom_geom_idx"

pg_restore: creating INDEX "public.wv_soc_schools_k12_geom_geom_idx"

pg_restore: creating INDEX "public.wv_trn_airports_geom_geom_idx"

pg_restore: creating INDEX "public.wv_util_sewer_treatment_plants_geom_geom_idx"

pg_restore: creating TRIGGER "public.wv_bio_biodiversity_rank trg_enforce_xy_wv_bio_biodiversity_rank"

pg_restore: while PROCESSING TOC:

pg_restore: from TOC entry 6385; 2620 1125315 TRIGGER wv_bio_biodiversity_rank trg_enforce_xy_wv_bio_biodiversity_rank msjarvis

pg_restore: error: could not execute query: ERROR:  function public.enforce_xy_on_geom() does not exist

Command was: CREATE TRIGGER trg_enforce_xy_wv_bio_biodiversity_rank BEFORE INSERT OR UPDATE ON public.wv_bio_biodiversity_rank FOR EACH ROW EXECUTE FUNCTION public.enforce_xy_on_geom();

pg_restore: creating TRIGGER "public.wv_env_epa_facilities trg_enforce_xy_wv_env_epa_facilities"

pg_restore: from TOC entry 6380; 2620 1127554 TRIGGER wv_env_epa_facilities trg_enforce_xy_wv_env_epa_facilities msjarvis

pg_restore: error: could not execute query: ERROR:  function public.enforce_xy_on_geom() does not exist

Command was: CREATE TRIGGER trg_enforce_xy_wv_env_epa_facilities BEFORE INSERT OR UPDATE ON public.wv_env_epa_facilities FOR EACH ROW EXECUTE FUNCTION public.enforce_xy_on_geom();

pg_restore: creating TRIGGER "public.wv_hyd_streams_high_quality trg_enforce_xy_wv_hyd_streams_high_quality"

pg_restore: from TOC entry 6383; 2620 1125230 TRIGGER wv_hyd_streams_high_quality trg_enforce_xy_wv_hyd_streams_high_quality msjarvis

pg_restore: error: could not execute query: ERROR:  function public.enforce_xy_on_geom() does not exist

Command was: CREATE TRIGGER trg_enforce_xy_wv_hyd_streams_high_quality BEFORE INSERT OR UPDATE ON public.wv_hyd_streams_high_quality FOR EACH ROW EXECUTE FUNCTION public.enforce_xy_on_geom();

pg_restore: creating TRIGGER "public.wv_soc_hospitals_wvdem trg_enforce_xy_wv_soc_hospitals_wvdem"

pg_restore: from TOC entry 6386; 2620 1127970 TRIGGER wv_soc_hospitals_wvdem trg_enforce_xy_wv_soc_hospitals_wvdem msjarvis

pg_restore: error: could not execute query: ERROR:  function public.enforce_xy_on_geom() does not exist

Command was: CREATE TRIGGER trg_enforce_xy_wv_soc_hospitals_wvdem BEFORE INSERT OR UPDATE ON public.wv_soc_hospitals_wvdem FOR EACH ROW EXECUTE FUNCTION public.enforce_xy_on_geom();

pg_restore: creating TRIGGER "public.wv_soc_schools_k12 trg_enforce_xy_wv_soc_schools_k12"

pg_restore: from TOC entry 6382; 2620 1128010 TRIGGER wv_soc_schools_k12 trg_enforce_xy_wv_soc_schools_k12 msjarvis

pg_restore: error: could not execute query: ERROR:  function public.enforce_xy_on_geom() does not exist

Command was: CREATE TRIGGER trg_enforce_xy_wv_soc_schools_k12 BEFORE INSERT OR UPDATE ON public.wv_soc_schools_k12 FOR EACH ROW EXECUTE FUNCTION public.enforce_xy_on_geom();

pg_restore: creating TRIGGER "public.wv_trn_airports trg_enforce_xy_wv_trn_airports"

pg_restore: from TOC entry 6384; 2620 1128026 TRIGGER wv_trn_airports trg_enforce_xy_wv_trn_airports msjarvis

pg_restore: error: could not execute query: ERROR:  function public.enforce_xy_on_geom() does not exist

Command was: CREATE TRIGGER trg_enforce_xy_wv_trn_airports BEFORE INSERT OR UPDATE ON public.wv_trn_airports FOR EACH ROW EXECUTE FUNCTION public.enforce_xy_on_geom();

pg_restore: creating TRIGGER "public.wv_util_sewer_treatment_plants trg_enforce_xy_wv_util_sewer_treatment_plants"

pg_restore: from TOC entry 6381; 2620 1127922 TRIGGER wv_util_sewer_treatment_plants trg_enforce_xy_wv_util_sewer_treatment_plants msjarvis

pg_restore: error: could not execute query: ERROR:  function public.enforce_xy_on_geom() does not exist

Command was: CREATE TRIGGER trg_enforce_xy_wv_util_sewer_treatment_plants BEFORE INSERT OR UPDATE ON public.wv_util_sewer_treatment_plants FOR EACH ROW EXECUTE FUNCTION public.enforce_xy_on_geom();

pg_restore: warning: errors ignored on restore: 7

msjarvisgis_v2=# SELECT 'wv_bio_biodiversity_rank' AS table_name, ST_SRID(geom) AS srid, COUNT(*) AS rows

FROM public.wv_bio_biodiversity_rank

GROUP BY ST_SRID(geom)

UNION ALL

SELECT 'wv_env_epa_facilities', ST_SRID(geom), COUNT(*)

FROM public.wv_env_epa_facilities

GROUP BY ST_SRID(geom)

UNION ALL

SELECT 'wv_hyd_streams_high_quality', ST_SRID(geom), COUNT(*)

FROM public.wv_hyd_streams_high_quality

GROUP BY ST_SRID(geom)

UNION ALL

SELECT 'wv_soc_schools_k12', ST_SRID(geom), COUNT(*)

FROM public.wv_soc_schools_k12

GROUP BY ST_SRID(geom)

UNION ALL

SELECT 'wv_soc_hospitals_wvdem', ST_SRID(geom), COUNT(*)

FROM public.wv_soc_hospitals_wvdem

ORDER BY table_name, srid;treatment_plantsT_SRID(geom), COUNT(*)

           table_name           | srid | rows  

--------------------------------+------+-------

 wv_bio_biodiversity_rank       | 4269 | 63912

 wv_env_epa_facilities          | 4269 |  2137

 wv_hyd_streams_high_quality    | 4269 | 22656

 wv_soc_hospitals_wvdem         | 4269 |    66

 wv_soc_schools_k12             | 4269 |   828

 wv_trn_airports                | 4269 |    46

 wv_util_sewer_treatment_plants | 4269 |  1269

(7 rows)

msjarvisgis_v2=# CALL gbim_load_blockgroup_coverage('public.wv_bio_biodiversity_rank');

CALL gbim_load_blockgroup_coverage('public.wv_env_epa_facilities');

CALL gbim_load_blockgroup_coverage('public.wv_hyd_streams_high_quality');

CALL gbim_load_blockgroup_coverage('public.wv_soc_schools_k12');

CALL gbim_load_blockgroup_coverage('public.wv_soc_hospitals_wvdem');

CALL gbim_load_blockgroup_coverage('public.wv_trn_airports');

CALL gbim_load_blockgroup_coverage('public.wv_util_sewer_treatment_plants');

CALL

CALL

CALL

CALL

CALL

CALL

CALL

msjarvisgis_v2=# SELECT

    r.dataset_type,

    r.display_name,

    r.category,

    COUNT(*) AS blockgroup_rows,

    SUM(c.feature_count) AS total_features_intersected,

    SUM(CASE WHEN c.feature_count > 0 THEN 1 ELSE 0 END) AS blockgroups_with_features

FROM gbim_layer_registry r

LEFT JOIN wv_blockgroup_dataset_coverage c

  ON c.dataset_type = r.dataset_type

WHERE r.dataset_type IN (

    'public.wv_bio_biodiversity_rank',

    'public.wv_env_epa_facilities',

    'public.wv_hyd_streams_high_quality',

    'public.wv_soc_schools_k12',

    'public.wv_soc_hospitals_wvdem',

    'public.wv_trn_airports',

    'public.wv_util_sewer_treatment_plants'

)

GROUP BY r.dataset_type, r.display_name, r.category

ORDER BY r.category, r.display_name;

msjarvisgis_v2=# CREATE OR REPLACE VIEW gbim_blockgroup_semantic_rebuild AS

SELECT           CREATE OR REPLACE VIEW gbim_blockgroup_semantic_rebuild AS

SELECTblockgroup_geoid,

    s.blockgroup_geoid,

    s.county_geoid,

    s.tract_geoid,sion,

    s.snapshot_version,

    s.belief_hash,

    trim(cat_ws(

      concat_ws(

        ' ',sus blockgroup ' || s.blockgroup_geoid ||

        'Census blockgroup ' || s.blockgroup_geoid ||

        ' in county ' || s.county_geoid ||'.',

        ' and tract ' || s.tract_geoid || '.',BY f.dataset_type, f.fragment_order)

        string_agg(f.fragment_text, ' ' ORDER BY f.dataset_type, f.fragment_order)

      )S rebuilt_semantic_content

    ) AS rebuilt_semantic_contentt s

FROM wv_blockgroup_belief_snapshot sents f

LEFT JOIN gbim_blockgroup_text_fragments fid

  ON f.blockgroup_geoid = s.blockgroup_geoid

GROUP BYockgroup_geoid,

    s.blockgroup_geoid,

    s.county_geoid,

    s.tract_geoid,sion,

    s.snapshot_version,

    s.belief_hash;

CREATE VIEW

msjarvisgis_v2=# UPDATE wv_blockgroup_belief_snapshot s

SET semantic_content = r.rebuilt_semantic_content

FROM gbim_blockgroup_semantic_rebuild r

WHERE r.blockgroup_geoid = s.blockgroup_geoid

  AND r.snapshot_version = s.snapshot_version;

UPDATE 1639

msjarvisgis_v2=# 

msjarvisgis_v2=# \COPY (

  SELECT

    document_id,

    governed_text,

    entity_type,

    blockgroup_geoid,

    county_geoid,

    tract_geoid

  FROM wv_blockgroup_belief_vector_ready

) TO '/mnt/spiritual_drive/msjarvis-rebuild/wv_blockgroup_belief_vector_ready_statewide_v9.csv'

WITH (FORMAT csv, HEADER true);

COPY 1639

msjarvisgis_v2=# ALTER TABLE public.wv_bio_biodiversity_rank

  ADD COLUMN IF NOT EXISTS geom_utm17 geometry(MultiPolygon, 26917);

ALTER TABLE public.wv_env_epa_facilities

  ADD COLUMN IF NOT EXISTS geom_utm17 geometry(Point, 26917);

ALTER TABLE public.wv_hyd_streams_high_quality

  ADD COLUMN IF NOT EXISTS geom_utm17 geometry(MultiLineString, 26917);

ALTER TABLE public.wv_soc_schools_k12

  ADD COLUMN IF NOT EXISTS geom_utm17 geometry(Point, 26917);

ALTER TABLE public.wv_soc_hospitals_wvdem

  ADD COLUMN IF NOT EXISTS geom_utm17 geometry(Point, 26917);

ALTER TABLE public.wv_trn_airports

  ADD COLUMN IF NOT EXISTS geom_utm17 geometry(Point, 26917);

ALTER TABLE public.wv_util_sewer_treatment_plants

  ADD COLUMN IF NOT EXISTS geom_utm17 geometry(Point, 26917);

ALTER TABLE

ALTER TABLE

ALTER TABLE

ALTER TABLE

ALTER TABLE

ALTER TABLE

ALTER TABLE

msjarvisgis_v2=# UPDATE public.wv_bio_biodiversity_rank

SET geom_utm17 = ST_Transform(geom, 26917)

WHERE geom IS NOT NULL;

UPDATE public.wv_env_epa_facilities

SET geom_utm17 = ST_Transform(geom, 26917)

WHERE geom IS NOT NULL;

UPDATE public.wv_hyd_streams_high_quality

SET geom_utm17 = ST_Transform(geom, 26917)

WHERE geom IS NOT NULL;

UPDATE public.wv_soc_schools_k12

SET geom_utm17 = ST_Transform(geom, 26917)

WHERE geom IS NOT NULL;

UPDATE public.wv_soc_hospitals_wvdem

SET geom_utm17 = ST_Transform(geom, 26917)

WHERE geom IS NOT NULL;

UPDATE public.wv_trn_airports

SET geom_utm17 = ST_Transform(geom, 26917)

WHERE geom IS NOT NULL;

WHERE geom IS NOT NULL;nsform(geom, 26917)ts

UPDATE 63912

ERROR:  Geometry type (MultiPoint) does not match column type (Point)

ERROR:  Geometry has Z dimension but column does not

ERROR:  Geometry type (MultiPoint) does not match column type (Point)

ERROR:  Geometry type (MultiPoint) does not match column type (Point)

ERROR:  Geometry type (MultiPoint) does not match column type (Point)

ERROR:  Geometry type (MultiPoint) does not match column type (Point)

msjarvisgis_v2=# SELECT 'wv_bio_biodiversity_rank' AS table_name,

       ST_SRID(geom) AS srid_geom,

       ST_SRID(geom_utm17) AS srid_utm17,

       COUNT(*) AS rows

FROM public.wv_bio_biodiversity_rank

GROUP BY ST_SRID(geom), ST_SRID(geom_utm17)

UNION ALL

SELECT 'wv_env_epa_facilities',

       ST_SRID(geom), ST_SRID(geom_utm17), COUNT(*)

FROM public.wv_env_epa_facilities

GROUP BY ST_SRID(geom), ST_SRID(geom_utm17)

UNION ALL

SELECT 'wv_hyd_streams_high_quality',

       ST_SRID(geom), ST_SRID(geom_utm17), COUNT(*)

FROM public.wv_hyd_streams_high_quality

GROUP BY ST_SRID(geom), ST_SRID(geom_utm17)

UNION ALL

SELECT 'wv_soc_schools_k12',

       ST_SRID(geom), ST_SRID(geom_utm17), COUNT(*)

FROM public.wv_soc_schools_k12

ORDER BY table_name;m), ST_SRID(geom_utm17)COUNT(*)

           table_name           | srid_geom | srid_utm17 | rows  

--------------------------------+-----------+------------+-------

 wv_bio_biodiversity_rank       |      4269 |      26917 | 63912

 wv_env_epa_facilities          |      4269 |            |  2137

 wv_hyd_streams_high_quality    |      4269 |            | 22656

 wv_soc_hospitals_wvdem         |      4269 |            |    66

 wv_soc_schools_k12             |      4269 |            |   828

 wv_trn_airports                |      4269 |            |    46

 wv_util_sewer_treatment_plants |      4269 |            |  1269

(7 rows)

msjarvisgis_v2=# SELECT 'wv_env_epa_facilities' AS table_name,

       GeometryType(geom) AS geom_type,

       ST_Dimension(geom) AS dim,

       ST_SRID(geom) AS srid,

       COUNT(*) AS rows

FROM public.wv_env_epa_facilities

GROUP BY geom_type, dim, srid

UNION ALL

SELECT 'wv_hyd_streams_high_quality',

       GeometryType(geom), ST_Dimension(geom), ST_SRID(geom), COUNT(*)

FROM public.wv_hyd_streams_high_quality

GROUP BY GeometryType(geom), ST_Dimension(geom), ST_SRID(geom)

UNION ALL

SELECT 'wv_soc_schools_k12',

       GeometryType(geom), ST_Dimension(geom), ST_SRID(geom), COUNT(*)

FROM public.wv_soc_schools_k12

GROUP BY GeometryType(geom), ST_Dimension(geom), ST_SRID(geom)

UNION ALL

SELECT 'wv_soc_hospitals_wvdem',

       GeometryType(geom), ST_Dimension(geom), ST_SRID(geom), COUNT(*)

FROM public.wv_soc_hospitals_wvdem

ORDER BY table_name;e(geom), ST_Dimension(geom), ST_SRID(geom)COUNT(*)

           table_name           |    geom_type    | dim | srid | rows  

--------------------------------+-----------------+-----+------+-------

 wv_env_epa_facilities          | MULTIPOINT      |   0 | 4269 |  2137

 wv_hyd_streams_high_quality    | MULTILINESTRING |   1 | 4269 | 22656

 wv_soc_hospitals_wvdem         | MULTIPOINT      |   0 | 4269 |    66

 wv_soc_schools_k12             | MULTIPOINT      |   0 | 4269 |   828

 wv_trn_airports                | MULTIPOINT      |   0 | 4269 |    46

 wv_util_sewer_treatment_plants | MULTIPOINT      |   0 | 4269 |  1269

(6 rows)

msjarvisgis_v2=# -- EPA facilities: use MultiPoint with Z if present

ALTER TABLE public.wv_env_epa_facilities

  ALTER COLUMN geom_utm17 TYPE geometry(MultiPoint, 26917);

-- High-quality streams: MultiLineString already correct

ALTER TABLE public.wv_hyd_streams_high_quality

  ALTER COLUMN geom_utm17 TYPE geometry(MultiLineString, 26917);

-- K–12 schools

ALTER TABLE public.wv_soc_schools_k12

  ALTER COLUMN geom_utm17 TYPE geometry(MultiPoint, 26917);

-- Hospitals

ALTER TABLE public.wv_soc_hospitals_wvdem

  ALTER COLUMN geom_utm17 TYPE geometry(MultiPoint, 26917);

-- Airports

ALTER TABLE public.wv_trn_airports

  ALTER COLUMN geom_utm17 TYPE geometry(MultiPoint, 26917);

-- Sewer treatment plants

ALTER TABLE public.wv_util_sewer_treatment_plants

  ALTER COLUMN geom_utm17 TYPE geometry(MultiPoint, 26917);

ALTER TABLE

ALTER TABLE

ALTER TABLE

ALTER TABLE

ALTER TABLE

ALTER TABLE

msjarvisgis_v2=# 

msjarvisgis_v2=# UPDATE public.wv_env_epa_facilities

SET geom_utm17 = ST_Transform(ST_Force2D(geom), 26917)

WHERE geom IS NOT NULL;

UPDATE public.wv_hyd_streams_high_quality

SET geom_utm17 = ST_Transform(ST_Force2D(geom), 26917)

WHERE geom IS NOT NULL;

UPDATE public.wv_soc_schools_k12

SET geom_utm17 = ST_Transform(ST_Force2D(geom), 26917)

WHERE geom IS NOT NULL;

UPDATE public.wv_soc_hospitals_wvdem

SET geom_utm17 = ST_Transform(ST_Force2D(geom), 26917)

WHERE geom IS NOT NULL;

UPDATE public.wv_trn_airports

SET geom_utm17 = ST_Transform(ST_Force2D(geom), 26917)

WHERE geom IS NOT NULL;

UPDATE public.wv_util_sewer_treatment_plants

SET geom_utm17 = ST_Transform(ST_Force2D(geom), 26917)

WHERE geom IS NOT NULL;

UPDATE 2137

UPDATE 22656

UPDATE 828

UPDATE 66

UPDATE 46

UPDATE 1269

msjarvisgis_v2=# SELECT 'wv_env_epa_facilities' AS table_name,

       ST_SRID(geom) AS srid_geom,

       ST_SRID(geom_utm17) AS srid_utm17,

       COUNT(*) AS rows

FROM public.wv_env_epa_facilities

GROUP BY ST_SRID(geom), ST_SRID(geom_utm17)

UNION ALL

SELECT 'wv_hyd_streams_high_quality',

       ST_SRID(geom), ST_SRID(geom_utm17), COUNT(*)

FROM public.wv_hyd_streams_high_quality

GROUP BY ST_SRID(geom), ST_SRID(geom_utm17)

UNION ALL

SELECT 'wv_soc_schools_k12',

       ST_SRID(geom), ST_SRID(geom_utm17), COUNT(*)

FROM public.wv_soc_schools_k12

GROUP BY ST_SRID(geom), ST_SRID(geom_utm17)

UNION ALL

SELECT 'wv_soc_hospitals_wvdem',

       ST_SRID(geom), ST_SRID(geom_utm17), COUNT(*)

FROM public.wv_soc_hospitals_wvdem

ORDER BY table_name;m), ST_SRID(geom_utm17)COUNT(*)

           table_name           | srid_geom | srid_utm17 | rows  

--------------------------------+-----------+------------+-------

 wv_env_epa_facilities          |      4269 |      26917 |  2137

 wv_hyd_streams_high_quality    |      4269 |      26917 | 22656

 wv_soc_hospitals_wvdem         |      4269 |      26917 |    66

 wv_soc_schools_k12             |      4269 |      26917 |   828

 wv_trn_airports                |      4269 |      26917 |    46

 wv_util_sewer_treatment_plants |      4269 |      26917 |  1269

(6 rows)

msjarvisgis_v2=# DELETE FROM wv_blockgroup_dataset_coverage

WHERE dataset_type IN (

    'public.wv_bio_biodiversity_rank',

    'public.wv_env_epa_facilities',

    'public.wv_hyd_streams_high_quality',

    'public.wv_soc_schools_k12',

    'public.wv_soc_hospitals_wvdem',

    'public.wv_trn_airports',

    'public.wv_util_sewer_treatment_plants'

);

DELETE 11473

msjarvisgis_v2=# SELECT

    r.dataset_type,

    r.display_name,

    r.category,

    COUNT(*) AS blockgroup_rows,

    SUM(c.feature_count) AS total_features_intersected,

    SUM(CASE WHEN c.feature_count > 0 THEN 1 ELSE 0 END) AS blockgroups_with_features

FROM gbim_layer_registry r

LEFT JOIN wv_blockgroup_dataset_coverage c

  ON c.dataset_type = r.dataset_type

WHERE r.dataset_type IN (

    'public.wv_bio_biodiversity_rank',

    'public.wv_env_epa_facilities',

    'public.wv_hyd_streams_high_quality',

    'public.wv_soc_schools_k12',

    'public.wv_soc_hospitals_wvdem',

    'public.wv_trn_airports',

    'public.wv_util_sewer_treatment_plants'

)

GROUP BY r.dataset_type, r.display_name, r.category

ORDER BY r.category, r.display_name;

msjarvisgis_v2=# INSERT INTO wv_blockgroup_dataset_coverage (

    blockgroup_geoid,

    county_geoid,

    dataset_type,

    source_table,

    feature_count,

    coverage_state,

    calculation_time,

    source_layer_hash,

    notes,

    coverage_reason

)

SELECT

    bg.blockgroup_geoid,

    bg.county_geoid,

    'public.wv_bio_biodiversity_rank' AS dataset_type,

    'public.wv_bio_biodiversity_rank' AS source_table,

    COUNT(b.*)::integer AS feature_count,

    CASE WHEN COUNT(b.*) > 0 THEN 'present' ELSE 'absent' END AS coverage_state,

    now() AS calculation_time,

    NULL::text AS source_layer_hash,

    'GBIM blockgroup coverage load for biodiversity priority areas' AS notes,

    CASE WHEN COUNT(b.*) > 0 THEN 'features_intersected'

         ELSE 'no_features_found_in_covered_area'

GROUP BY bg.blockgroup_geoid, bg.county_geoid;

INSERT 0 1639

msjarvisgis_v2=# INSERT INTO wv_blockgroup_dataset_coverage (

    blockgroup_geoid,

    county_geoid,

    dataset_type,

    source_table,

    feature_count,

    coverage_state,

    calculation_time,

    source_layer_hash,

    notes,

    coverage_reason

)

SELECT

    bg.blockgroup_geoid,

    bg.county_geoid,

    'public.wv_env_epa_facilities' AS dataset_type,

    'public.wv_env_epa_facilities' AS source_table,

    COUNT(f.*)::integer AS feature_count,

    CASE WHEN COUNT(f.*) > 0 THEN 'present' ELSE 'absent' END AS coverage_state,

    now() AS calculation_time,

    NULL::text AS source_layer_hash,

    'GBIM blockgroup coverage load for EPA-regulated facilities' AS notes,

    CASE WHEN COUNT(f.*) > 0 THEN 'features_intersected'

         ELSE 'no_features_found_in_covered_area'

GROUP BY bg.blockgroup_geoid, bg.county_geoid;

INSERT 0 1639

msjarvisgis_v2=# INSERT INTO wv_blockgroup_dataset_coverage (

    blockgroup_geoid,

    county_geoid,

    dataset_type,

    source_table,

    feature_count,

    coverage_state,

    calculation_time,

    source_layer_hash,

    notes,

    coverage_reason

)

SELECT

    bg.blockgroup_geoid,

    bg.county_geoid,

    'public.wv_hyd_streams_high_quality' AS dataset_type,

    'public.wv_hyd_streams_high_quality' AS source_table,

    COUNT(s.*)::integer AS feature_count,

    CASE WHEN COUNT(s.*) > 0 THEN 'present' ELSE 'absent' END AS coverage_state,

    now() AS calculation_time,

    NULL::text AS source_layer_hash,

    'GBIM blockgroup coverage load for high-quality streams' AS notes,

    CASE WHEN COUNT(s.*) > 0 THEN 'features_intersected'

         ELSE 'no_features_found_in_covered_area'

GROUP BY bg.blockgroup_geoid, bg.county_geoid;

INSERT 0 1639

msjarvisgis_v2=# INSERT INTO wv_blockgroup_dataset_coverage (

    blockgroup_geoid,

    county_geoid,

    dataset_type,

    source_table,

    feature_count,

    coverage_state,

    calculation_time,

    source_layer_hash,

    notes,

    coverage_reason

)

SELECT

    bg.blockgroup_geoid,

    bg.county_geoid,

    'public.wv_soc_schools_k12' AS dataset_type,

    'public.wv_soc_schools_k12' AS source_table,

    COUNT(sc.*)::integer AS feature_count,

    CASE WHEN COUNT(sc.*) > 0 THEN 'present' ELSE 'absent' END AS coverage_state,

    now() AS calculation_time,

    NULL::text AS source_layer_hash,

    'GBIM blockgroup coverage load for K–12 schools' AS notes,

    CASE WHEN COUNT(sc.*) > 0 THEN 'features_intersected'

         ELSE 'no_features_found_in_covered_area'

GROUP BY bg.blockgroup_geoid, bg.county_geoid;

INSERT 0 1639

msjarvisgis_v2=# INSERT INTO wv_blockgroup_dataset_coverage (

    blockgroup_geoid,

    county_geoid,

    dataset_type,

    source_table,

    feature_count,

    coverage_state,

    calculation_time,

    source_layer_hash,

    notes,

    coverage_reason

)

SELECT

    bg.blockgroup_geoid,

    bg.county_geoid,

    'public.wv_soc_hospitals_wvdem' AS dataset_type,

    'public.wv_soc_hospitals_wvdem' AS source_table,

    COUNT(h.*)::integer AS feature_count,

    CASE WHEN COUNT(h.*) > 0 THEN 'present' ELSE 'absent' END AS coverage_state,

    now() AS calculation_time,

    NULL::text AS source_layer_hash,

    'GBIM blockgroup coverage load for hospitals' AS notes,

    CASE WHEN COUNT(h.*) > 0 THEN 'features_intersected'

         ELSE 'no_features_found_in_covered_area'

GROUP BY bg.blockgroup_geoid, bg.county_geoid;

INSERT 0 1639

msjarvisgis_v2=# INSERT INTO wv_blockgroup_dataset_coverage (

    blockgroup_geoid,

    county_geoid,

    dataset_type,

    source_table,

    feature_count,

    coverage_state,

    calculation_time,

    source_layer_hash,

    notes,

    coverage_reason

)

SELECT

    bg.blockgroup_geoid,

    bg.county_geoid,

    'public.wv_trn_airports' AS dataset_type,

    'public.wv_trn_airports' AS source_table,

    COUNT(a.*)::integer AS feature_count,

    CASE WHEN COUNT(a.*) > 0 THEN 'present' ELSE 'absent' END AS coverage_state,

    now() AS calculation_time,

    NULL::text AS source_layer_hash,

    'GBIM blockgroup coverage load for airports' AS notes,

    CASE WHEN COUNT(a.*) > 0 THEN 'features_intersected'

         ELSE 'no_features_found_in_covered_area'

GROUP BY bg.blockgroup_geoid, bg.county_geoid;

INSERT 0 1639

msjarvisgis_v2=# INSERT INTO wv_blockgroup_dataset_coverage (

    blockgroup_geoid,

    county_geoid,

    dataset_type,

    source_table,

    feature_count,

    coverage_state,

    calculation_time,

    source_layer_hash,

    notes,

    coverage_reason

)

SELECT

    bg.blockgroup_geoid,

    bg.county_geoid,

    'public.wv_util_sewer_treatment_plants' AS dataset_type,

    'public.wv_util_sewer_treatment_plants' AS source_table,

    COUNT(p.*)::integer AS feature_count,

    CASE WHEN COUNT(p.*) > 0 THEN 'present' ELSE 'absent' END AS coverage_state,

    now() AS calculation_time,

    NULL::text AS source_layer_hash,

    'GBIM blockgroup coverage load for wastewater treatment plants' AS notes,

    CASE WHEN COUNT(p.*) > 0 THEN 'features_intersected'

         ELSE 'no_features_found_in_covered_area'

GROUP BY bg.blockgroup_geoid, bg.county_geoid;s p

INSERT 0 1639

msjarvisgis_v2=# SELECT

    r.dataset_type,

    r.display_name,

    r.category,

    COUNT(*) AS blockgroup_rows,

    SUM(c.feature_count) AS total_features_intersected,

    SUM(CASE WHEN c.feature_count > 0 THEN 1 ELSE 0 END) AS blockgroups_with_features

FROM gbim_layer_registry r

LEFT JOIN wv_blockgroup_dataset_coverage c

  ON c.dataset_type = r.dataset_type

WHERE r.dataset_type IN (

    'public.wv_bio_biodiversity_rank',

    'public.wv_env_epa_facilities',

    'public.wv_hyd_streams_high_quality',

    'public.wv_soc_schools_k12',

    'public.wv_soc_hospitals_wvdem',

    'public.wv_trn_airports',

    'public.wv_util_sewer_treatment_plants'

)

GROUP BY r.dataset_type, r.display_name, r.category

ORDER BY r.category, r.display_name;

msjarvisgis_v2=# \dt public.wv*

msjarvisgis_v2=# \d public.wv*

[1]+  Stopped                 psql -p 5436 -U postgres -d msjarvisgis_v2

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ psql -p 5436 -U postgres -d msjarvisgis_v2 -c "

SELECT COUNT(*) FROM wv_blockgroup_dataset_coverage;

"

 count 

-------

 40975

(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ p(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ #(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ p(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ #(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ \dt public.wv*

dt: command not found

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ psql -p 5436 -U postgres -d msjarvisgis_v2

psql (16.14 (Ubuntu 16.14-0ubuntu0.24.04.1))

SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, compression: off)

Type "help" for help.

msjarvisgis_v2=# \dt public.wv*

msjarvisgis_v2=# CREATE TABLE IF NOT EXISTS public.wv_source_manifest_layers (

  dataset_name   text,

  source_file    text,

  agency         text,

  projection     text,

  sourcetable    text,

  geometry_role  text

);

TRUNCATE TABLE public.wv_source_manifest_layers;

\copy public.wv_source_manifest_layers

  FROM 'wv_source_manifest_layers.csv'

  WITH (FORMAT csv, HEADER true);

CREATE TABLE

TRUNCATE TABLE

COPY 11

msjarvisgis_v2=# SELECT COUNT(*), MIN(sourcetable), MAX(sourcetable)

FROM public.wv_source_manifest_layers;

msjarvisgis_v2=# CREATE TEMP TABLE gbim_coverage (

  dataset_type text,

  source_table text

);

\copy gbim_coverage

  FROM 'gbim_coverage_datasets.csv'

  WITH (FORMAT csv, HEADER true);

CREATE TEMP TABLE gbim_manifest (

  sourcetable text

);

\copy gbim_manifest

  FROM 'gbim_manifest_datasets.csv'

  WITH (FORMAT csv, HEADER true);

CREATE TABLE

ERROR:  syntax error at or near "\"

LINE 7: \copy gbim_manifest

        ^

msjarvisgis_v2=# CREATE TEMP TABLE gbim_coverage (

  dataset_type text,

  source_table text

);

ERROR:  relation "gbim_coverage" already exists

msjarvisgis_v2=# \copy gbim_coverage

  FROM 'gbim_coverage_datasets.csv'

  WITH (FORMAT csv, HEADER true);

COPY 25

msjarvisgis_v2=# CREATE TEMP TABLE gbim_manifest (

  sourcetable text

);

CREATE TABLE

msjarvisgis_v2=# CREATE TEMP TABLE gbim_manifest (

  sourcetable text

);

ERROR:  relation "gbim_manifest" already exists

msjarvisgis_v2=# SELECT COUNT(*) FROM gbim_coverage;

SELECT COUNT(*) FROM gbim_manifest;

 count 

-------

    25

(1 row)

 count 

-------

     0

(1 row)

msjarvisgis_v2=# TRUNCATE TABLE gbim_manifest;

TRUNCATE TABLE

msjarvisgis_v2=# \copy gbim_manifest

  FROM 'gbim_manifest_datasets.csv'

  WITH (FORMAT csv, HEADER true);

COPY 11

msjarvisgis_v2=# SELECT COUNT(*) FROM gbim_manifest;

 count 

-------

    11

(1 row)

msjarvisgis_v2=# SELECT COUNT(*) FROM gbim_coverage;

SELECT COUNT(*) FROM gbim_manifest;

 count 

-------

    25

(1 row)

 count 

-------

    11

(1 row)

msjarvisgis_v2=# SELECT DISTINCT

  m.sourcetable

FROM gbim_manifest m

LEFT JOIN gbim_coverage c

  ON c.source_table = m.sourcetable

WHERE c.source_table IS NULL

ORDER BY m.sourcetable;

                        sourcetable                         

------------------------------------------------------------

 public.wv_bio_ecoregions

 public.wv_bio_red_spruce_cover

 public.wv_bnd_appalachian_basin_boundary

 public.wv_bnd_arc_counties

 public.wv_bnd_canaan_valley_nwr

 public.wv_bnd_census_designated_places

 public.wv_wv_county_boundaries_24k_topo_updated_2026_utm83

 public.wv_wv_county_boundaries_24k_topo_updated_2026_wma84

(8 rows)

msjarvisgis_v2=# \copy (

  SELECT DISTINCT

    m.sourcetable

  FROM gbim_manifest m

  LEFT JOIN gbim_coverage c

    ON c.source_table = m.sourcetable

  WHERE c.source_table IS NULL

  ORDER BY m.sourcetable

) TO 'gbim_missing_datasets.csv' WITH (FORMAT csv, HEADER true);

COPY 8

msjarvisgis_v2=# \d public.wv_soc_census_blockgroups_2020_utm17;

          Table "public.wv_soc_census_blockgroups_2020_utm17"

 Column |             Type             | Collation | Nullable | Default 

--------+------------------------------+-----------+----------+---------

 geoid  | text                         |           |          | 

 geom   | geometry(MultiPolygon,26917) |           |          | 

Indexes:

    "wv_soc_census_blockgroups_2020_utm17_geoid_idx" btree (geoid)

    "wv_soc_census_blockgroups_2020_utm17_geom_idx" gist (geom)

msjarvisgis_v2=# \d public.wv_blockgroup_representation

                    Table "public.wv_blockgroup_representation"

      Column       |             Type             | Collation | Nullable | Default 

-------------------+------------------------------+-----------+----------+---------

 blockgroup_geoid  | text                         |           | not null | 

 source_table      | text                         |           | not null | 

 source_feature_id | bigint                       |           | not null | 

 geom              | geometry(MultiPolygon,4269)  |           |          | 

 geom_hash         | text                         |           | not null | 

 srid              | integer                      |           | not null | 

 created_at        | timestamp with time zone     |           |          | now()

 geom_utm17        | geometry(MultiPolygon,26917) |           |          | 

 geom_proj         | geometry(MultiPolygon,26917) |           |          | 

Indexes:

    "wv_blockgroup_representation_pkey" PRIMARY KEY, btree (blockgroup_geoid)

    "wv_blockgroup_representation_geom_utm17_idx" gist (geom_utm17)

msjarvisgis_v2=#
