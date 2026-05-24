(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/ms-allis-frontend$ sudo -u postgres psql -c "GRANT CONNECT ON DATABASE gisdb TO cakidd;"
sudo -u postgres psql -d gisdb -c "GRANT USAGE ON SCHEMA public TO cakidd;"
sudo -u postgres psql -d gisdb -c "GRANT SELECT ON ALL TABLES IN SCHEMA public TO cakidd;"
GRANT
GRANT
GRANT
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/ms-allis-frontend$ docker exec jarvis-69dgm-bridge python3 -c "
import psycopg2
conn = psycopg2.connect(
    host='172.18.0.1', port=5432,
    dbname='gisdb', user='cakidd', password='msjarvis'
)
cur = conn.cursor()
cur.execute('''
    SELECT * FROM wv_counties
    WHERE ST_Contains(geom,
        ST_SetSRID(ST_MakePoint(-80.88723, 37.67186), 4326))
    LIMIT 1
''')
row = cur.fetchone()
print('Spatial query result:', row)
cur.execute('SELECT COUNT(*) FROM wv_counties')
print('County polygon count:', cur.fetchone()[0])
conn.close()
print('PostGIS from Docker bridge: CONFIRMED')
"
Traceback (most recent call last):
  File "<string>", line 3, in <module>
  File "/usr/lib/python3.11/site-packages/psycopg2/__init__.py", line 122, in connect
    conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
psycopg2.OperationalError: connection to server at "172.18.0.1", port 5432 failed: FATAL:  no pg_hba.conf entry for host "172.18.0.86", user "cakidd", database "gisdb", SSL encryption
connection to server at "172.18.0.1", port 5432 failed: FATAL:  no pg_hba.conf entry for host "172.18.0.86", user "cakidd", database "gisdb", no encryption

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/ms-allis-frontend$ grep -rn "msjarvisgis" /opt/msjarvis-rebuild/ \
  --include="*.py" --include="*.yml" --include="*.env" \
  | grep -v ".pyc"
/opt/msjarvis-rebuild/enrich_where.py:3:CONN_STR = "postgresql://postgres:postgres@localhost:5435/msjarvisgis"
/opt/msjarvis-rebuild/load_all_attrs_csvs.py:5:PG_CMD = ["psql", "-h", "localhost", "-p", "5432", "-U", "postgres", "-d", "msjarvisgis"]
/opt/msjarvis-rebuild/gis_service/router.py:14:    "postgresql://postgres@localhost:5432/msjarvisgis"
/opt/msjarvis-rebuild/.env:20:DB_DSN=postgresql://postgres:postgres@127.0.0.1:5435/msjarvisgis
/opt/msjarvis-rebuild/.env:22:DB_URL=postgresql://postgres:postgres@127.0.0.1:5435/msjarvisgis
/opt/msjarvis-rebuild/.env:34:GEODB_DSN=postgresql://postgres:postgres@127.0.0.1:5435/msjarvisgis
/opt/msjarvis-rebuild/.env:63:LOCAL_RESOURCES_DSN=postgresql://msjarvis:MsJarvis2026Secure@jarvis-local-resources-db:5432/msjarvisgis
/opt/msjarvis-rebuild/.env:75:MSJARVIS_GIS_URL=postgresql://msjarvis:MsJarvis2026Secure@jarvis-local-resources-db:5432/msjarvisgis
/opt/msjarvis-rebuild/.env:113:POSTGRES_DB=msjarvisgis
/opt/msjarvis-rebuild/docker-compose.yml:1221:      - LOCAL_RESOURCES_DSN=postgresql://msjarvis:Nathaniel1@jarvis-gis-db:5432/msjarvisgis
/opt/msjarvis-rebuild/docker-compose.yml:1233:      - POSTGRES_DB=msjarvisgis
/opt/msjarvis-rebuild/docker-compose.yml:1255:      - GIS_DATABASE_URL=postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
/opt/msjarvis-rebuild/_archive/generated_20260430/embed_geodb.py:28:        pg_database = "msjarvisgis",
/opt/msjarvis-rebuild/_archive/generated_20260430/batch_normalize_beliefs.py:12:DSN = os.getenv("GBIM_DSN", "postgresql://msjarvis:Nathaniel1@localhost:5435/msjarvisgis")
/opt/msjarvis-rebuild/_archive/generated_20260430/ingest_benefit_programs_to_chroma.py:7:pg_conn = psycopg2.connect("dbname=msjarvisgis user=cakidd")
/opt/msjarvis-rebuild/_archive/generated_20260430/ai_server_20llm_FINAL.py:28:        f"{len(rag_hits)} msjarvisgis RAG hits."
/opt/msjarvis-rebuild/_archive/generated_20260430/ai_server_20llm_FINAL.py:34:          "the WV local_resources_index database, and the msjarvisgis RAG layer.\n"
/opt/msjarvis-rebuild/_archive/generated_20260430/bulk_build_beliefs.py:4:    conn = psycopg2.connect("dbname=msjarvisgis")
/opt/msjarvis-rebuild/_archive/generated_20260430/ingest_utility_enrollments_to_chroma.py:7:pg_conn = psycopg2.connect("dbname=msjarvisgis user=cakidd")
/opt/msjarvis-rebuild/_archive/generated_20260430/ingest_compliance_tasks_to_chroma.py:5:pg_conn = psycopg2.connect("dbname=msjarvisgis user=cakidd")
/opt/msjarvis-rebuild/_archive/generated_20260430/backfill_gbim_entities.py:93:        pg_db  = "msjarvisgis" if col_name in GEO_COLLECTIONS else None
/opt/msjarvis-rebuild/_archive/generated_20260430/backfill_gbim_entities.py:120:                pg_database = pg_db or "msjarvisgis",
/opt/msjarvis-rebuild/rebuild_gis_chroma.py:21:                      dbname="msjarvisgis", user="postgres")
/opt/msjarvis-rebuild/gis_rag_query.py:12:    Free-text GIS query over msjarvisgis→Chroma.
/opt/msjarvis-rebuild/msjarvis-rebuild/gbim_query_router.py:77:GEODB_DSN = "postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis"
/opt/msjarvis-rebuild/msjarvis-rebuild/gbim_query_router.py:235:            conn = psycopg2.connect("postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis")
/opt/msjarvis-rebuild/msjarvis-rebuild/gbim_query_router.py:295:            conn = psycopg2.connect("postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis")
/opt/msjarvis-rebuild/msjarvis-rebuild/gbim_query_router.py:377:            conn = psycopg2.connect("postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis")
/opt/msjarvis-rebuild/msjarvis-rebuild/gbim_query_router.py:423:                conn2 = psycopg2.connect("postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis")
/opt/msjarvis-rebuild/msjarvis-rebuild/chroma_to_postgres.py:7:DSN         = "postgresql://postgres:postgres@127.0.0.1:5435/msjarvisgis"
/opt/msjarvis-rebuild/msjarvis-rebuild/docker-compose.yml:1408:    - POSTGRES_DB=msjarvisgis
/opt/msjarvis-rebuild/msjarvis-rebuild/docker-compose.yml:1431:    - DB_URL=postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
/opt/msjarvis-rebuild/msjarvis-rebuild/docker-compose.yml:1532:    - GISDB_NAME=msjarvisgis
/opt/msjarvis-rebuild/msjarvis-rebuild/docker-compose.yml:1561:    - DB_NAME=msjarvisgis
/opt/msjarvis-rebuild/msjarvis-rebuild/docker-compose.yml:1676:    - POSTGRES_DB=msjarvisgis
/opt/msjarvis-rebuild/bootstrap_gbim_beliefs_eq1.py:24:    # Local Postgres on 127.0.0.1:5432, msjarvisgis DB, postgres user
/opt/msjarvis-rebuild/bootstrap_gbim_beliefs_eq1.py:26:        dbname="msjarvisgis",
/opt/msjarvis-rebuild/.scratch/patch_longterm_memory.py:22:MEMORY_DSN  = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis")
/opt/msjarvis-rebuild/.scratch/ems_bootstrap.py:5:DB = "msjarvisgis"
/opt/msjarvis-rebuild/services/gbim_query_router.py:11:GEODB_DSN = "postgresql://postgres:postgres@localhost:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/ms_mountainshares_analytics.py:26:    "postgresql://msjarvis:forensic@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/routes/trail_router.py:11:    "postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/resume_sync_wvgistc_buildings.py:9:GEODB_DSN = "postgresql://postgres:postgres@localhost:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/enrich_gbim_from_geospatial_features.py:5:labels against geospatial_features.name in msjarvisgis.
/opt/msjarvis-rebuild/services/enrich_gbim_from_geospatial_features.py:14:GIS_DB = DSN + "/msjarvisgis"
/opt/msjarvis-rebuild/services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py:144:            "msjarvisgis_rag_hits": 0,
/opt/msjarvis-rebuild/services/rag/geospatial_resolver.py:6:    "dbname=msjarvisgis user=msjarvis password=msjarvis host=127.0.0.1 port=5432",
/opt/msjarvis-rebuild/services/geodb_adapter.py:5:GEODB_DSN = os.getenv("GEODB_DSN", "postgresql://postgres:password@localhost:5432/msjarvisgis")
/opt/msjarvis-rebuild/services/gbim_verification_loop.py:12:DATABASE_URL    = os.environ.get("DATABASE_URL",     "postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis")
/opt/msjarvis-rebuild/services/gbim_coordinate_writer.py:3:Bridges: PostGIS (msjarvisgis) <-> ChromaDB (jarvis-chroma) <-> GBIM belief graph
/opt/msjarvis-rebuild/services/gbim_coordinate_writer.py:65:        pg_database: str = "msjarvisgis",
/opt/msjarvis-rebuild/services/gbim_explain.py:9:    "dbname=msjarvisgis user=postgres password=Nathaniel1 host=127.0.0.1 port=5432",
/opt/msjarvis-rebuild/services/ingest_hospitals.py:8:GEODB_DSN = os.getenv("GEODB_DSN", "postgresql://postgres:postgres@localhost:5432/msjarvisgis")
/opt/msjarvis-rebuild/services/populate_redetermination_tracker.py:5:pg_conn = psycopg2.connect("dbname=msjarvisgis user=cakidd")
/opt/msjarvis-rebuild/services/ingest_benefit_programs_to_chroma.py:7:pg_conn = psycopg2.connect("dbname=msjarvisgis user=cakidd")
/opt/msjarvis-rebuild/services/ingest_batch3_geofeatures.py:13:                        dbname="msjarvisgis", user="postgres", password="postgres")
/opt/msjarvis-rebuild/services/jarvis_steward/main.py:8:    "postgresql://msjarvis_app:change_me_strong_pw@host.docker.internal:5432/msjarvisgis",
/opt/msjarvis-rebuild/services/mountainshares_gbim_suggester.py:4:Queries msjarvisgis for MountainShares-relevant GBIM topics and
/opt/msjarvis-rebuild/services/mountainshares_gbim_suggester.py:16:    "postgresql://msjarvis:Nathaniel1@jarvis-local-resources-db:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/ingest_batch3_resume.py:12:                        dbname="msjarvisgis", user="postgres", password="postgres")
/opt/msjarvis-rebuild/services/jarvis-hippocampus_hippocampus_service.py:13:    "postgresql://msjarvis:MsJarvis2026Secure@jarvis-local-resources-db:5432/msjarvisgis",
/opt/msjarvis-rebuild/services/mountainshares_quest_api.py:5:GEODB_DSN = "postgresql://postgres:postgres@localhost:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/enrich_geodb_layers.py:15:    "postgresql://postgres:postgres@localhost:5432/msjarvisgis",
/opt/msjarvis-rebuild/services/jarvis_rag_search/retrieval_tuning.py:4:GBIM data source: jarvis-local-resources-db:5432/msjarvisgis
/opt/msjarvis-rebuild/services/jarvis_rag_search/retrieval_tuning.py:29:    "postgresql://msjarvis:msjarvis@jarvis-local-resources-db:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/jarvis_decay_escalation_consumer.py:10:Database: msjarvisgis (postgis-forensic, port 5432)
/opt/msjarvis-rebuild/services/jarvis_decay_escalation_consumer.py:35:DB_NAME = "msjarvisgis"
/opt/msjarvis-rebuild/services/ai_server_20llm_FINAL.py:28:        f"{len(rag_hits)} msjarvisgis RAG hits."
/opt/msjarvis-rebuild/services/ai_server_20llm_FINAL.py:34:          "the WV local_resources_index database, and the msjarvisgis RAG layer.\n"
/opt/msjarvis-rebuild/services/hippocampus_service.py:13:    "postgresql://msjarvis:MsJarvis2026Secure@jarvis-local-resources-db:5432/msjarvisgis",
/opt/msjarvis-rebuild/services/benefits_chat.py:8:        self.pg_conn = psycopg2.connect("dbname=msjarvisgis user=cakidd")
/opt/msjarvis-rebuild/services/ms_mountainshares_indexer.py:23:        "postgresql://msjarvis:forensic@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/rag_client.py:6:GIS RAG ("msjarvisgis") via the Chroma v2 HTTP API.
/opt/msjarvis-rebuild/services/rag_client.py:17:GIS_COLLECTION = os.getenv("GIS_RAG_COLLECTION", "msjarvisgis")
/opt/msjarvis-rebuild/services/rag_client.py:49:    Store arbitrary content into the msjarvisgis Chroma collection via v2 API.
/opt/msjarvis-rebuild/services/sync_health_access_to_chromadb.py:5:GEODB_DSN = os.getenv("GEODB_DSN", "postgresql://postgres:postgres@localhost:5432/msjarvisgis")
/opt/msjarvis-rebuild/services/ai_server_20llm_PRODUCTION.py:62:        f"{len(rag_hits)} msjarvisgis RAG hits."
/opt/msjarvis-rebuild/services/ai_server_20llm_PRODUCTION.py:68:          "the WV local_resources_index database, and the msjarvisgis RAG layer.\n"
/opt/msjarvis-rebuild/services/geo_rag_debug.py:7:PG_DSN = "dbname=msjarvisgis user=msjarvis host=localhost"
/opt/msjarvis-rebuild/services/bulk_build_beliefs.py:4:    conn = psycopg2.connect("dbname=msjarvisgis")
/opt/msjarvis-rebuild/services/ingest_utility_enrollments_to_chroma.py:7:pg_conn = psycopg2.connect("dbname=msjarvisgis user=cakidd")
/opt/msjarvis-rebuild/services/confidence_decay_loop.py:7:Schema target: msjarvisgis.gbim_entities (postgis-forensic, port 5432)
/opt/msjarvis-rebuild/services/confidence_decay_loop.py:8:Re-verification source: msjarvisgis.mvw_gbim_landowner_spatial
/opt/msjarvis-rebuild/services/confidence_decay_loop.py:32:    "database": "msjarvisgis",
/opt/msjarvis-rebuild/services/ms_jarvis_memory.py:20:MEMORY_DSN  = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis")
/opt/msjarvis-rebuild/services/geo_rag_debug_app.py:7:PG_DSN = "dbname=msjarvisgis user=msjarvis host=localhost"
/opt/msjarvis-rebuild/services/gbim_query_router/gbim_query_router.py:79:GEODB_DSN = os.environ.get('GEODB_DSN', 'postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis')
/opt/msjarvis-rebuild/services/au02_v2/service.py:16:    "dbname=msjarvisgis user=postgres password=postgres host=jarvis-local-resources-db port=5432"
/opt/msjarvis-rebuild/services/bulk_sync_gis_to_chromadb.py:10:GEODB_DSN = os.getenv("GEODB_DSN", "postgresql://postgres:postgres@localhost:5432/msjarvisgis")
/opt/msjarvis-rebuild/services/bulk_sync_gis_to_chromadb.py:19:    conn_str = "PG:host=localhost port=5432 dbname=msjarvisgis user=postgres password=postgres"
/opt/msjarvis-rebuild/services/ingest_compliance_tasks_to_chroma.py:5:pg_conn = psycopg2.connect("dbname=msjarvisgis user=cakidd")
/opt/msjarvis-rebuild/services/ingest_postgis_to_chroma.py:19:    "dbname": os.getenv("GIS_DB_NAME", "msjarvisgis"),
/opt/msjarvis-rebuild/services/ingest_watcher/ingest_runner.py:6:Lane B: msjarvisgis         /var/run/postgresql:5432  (Unix socket)
/opt/msjarvis-rebuild/services/ingest_watcher/ingest_runner.py:35:# Lane B — msjarvisgis (Unix socket)
/opt/msjarvis-rebuild/services/ingest_watcher/ingest_runner.py:39:    "dbname": "msjarvisgis",
/opt/msjarvis-rebuild/services/ingest_watcher/ingest_runner.py:80:# ── Geo-anchor via ZCTA centroid from msjarvisgis ────────────────────────────
/opt/msjarvis-rebuild/services/ingest_watcher/ingest_runner.py:167:        # Uses the zipcodetabulationarea_census_2020_wma84 table confirmed in msjarvisgis
/opt/msjarvis-rebuild/services/gbim_benefit_indexer.py:29:    f"{os.getenv('POSTGRES_DB','msjarvisgis')}"
/opt/msjarvis-rebuild/services/gbim_benefit_indexer.py:37:    f"{os.getenv('POSTGRES_DB','msjarvisgis')}"
/opt/msjarvis-rebuild/services/gbim_benefit_indexer.py:200:    # Enrich with verified local resources from msjarvisgis db
/opt/msjarvis-rebuild/services/gbim_benefit_indexer.py:272:        logger.warning(f"/lookup msjarvisgis enrichment failed: {_le}")
/opt/msjarvis-rebuild/services/gbim_benefit_indexer.py:286:        "msjarvisgis": local_hits,
/opt/msjarvis-rebuild/services/gbim_benefit_indexer.py:287:        "msjarvisgis_count": len(local_hits),
/opt/msjarvis-rebuild/services/gbim_benefit_indexer.py:288:        "msjarvisgis_source": f"resources.{county_match.lower()}" if local_hits else "none",
/opt/msjarvis-rebuild/services/gis_rag_service.py:34:    "postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/health_access_gbim_bridge.py:12:GEODB_DSN = os.getenv("GEODB_DSN", "postgresql://postgres:postgres@localhost:5432/msjarvisgis")
/opt/msjarvis-rebuild/services/conversation_gbim.py:26:    "dbname": "msjarvisgis",
/opt/msjarvis-rebuild/services/geospatial_resolver.py:6:    "dbname=msjarvisgis user=msjarvis password=msjarvis host=127.0.0.1 port=5432",
/opt/msjarvis-rebuild/services/gis_dataset_services/metropolitanandmicropolitanstatisticalareas_census_2020_wma84_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/wvstatehousedistricts_manysources_2002_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/populatedplaces_uscensus_1990_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/nationalatlasstreams_usgs_199903_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/libraries_manysources_2001_ll27_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/intermodalterminalfacilities_usdot_1997_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/solidwastefacilities_wvdep_200202_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/windenergyresource_nationalrenewableenergylab_200901_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/communityboundary_min_att_20250121_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/populatedplaces_uscensus_1990_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/springs_wvges_1986_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/votingdistrictswv_legislativeservices_2002_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/cvfault_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/blockgroups_census_201111_gcs83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/citieswithpopulatoinover2500_uscensus_1990_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/towers_wvpublicbroadcasting_2002_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/timberremovalvolume_usfs_1996_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/cvpoly_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/railnetworkwv_usdot_200203_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/navigablewaterwaysstructures_usarmycorpsofengineers_2006_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/summits_gistc_052012_wgs84_shp_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/placesofworship_hsip_20080723_wgs84_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/blockgroups_census_2020_wma84_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/coals2_utm27_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/blockgroups_census_2000_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/wvstateboundary24k_usgs_200203_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/countyseats_usgs_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/stateofwvsenatedistricts_wvlegislativeservices_2010_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/wvstatesenatedistricts_manysources_2002_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/blocks_census_2020_wma84_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/fire_dept_wvdem_092017_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/libraries_manysources_2001_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/wvstateboundary100k_usgs_200203_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/hazardmitigationbuyout_20250929_polygons_wma84_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/blockgroups_census_2020_utm83_full_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/weatherstations_nationalclimatedatacenter_1999_utm27_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/empowermentzonesandenterprisecommunities_uscensus_2002_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/towersprivate_fcc_200202_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/blockgroups_census_2020_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/facilities_epa_200203_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/workforceinvestmentareas_wvgistc_200208_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/nationalwaterwaynetwork_usarmycorpsofengineers_2001_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/wvstatesenatedistricts_manysources_2002_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/populatedplaces_census_2020_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/highered_wvemd_072420_wgc84_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/paroleoffices_manysources_2008_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/cvfault_utm27_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/indexgrid1minutequads_wvgistc_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/cvfault_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/blockgroups_census_201111_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/zipcodetabulationarea_census_2020_wma84_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/dams_usarmycropsofengineers_200010_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/citieswithpopulationsover2500_census_2020_wma84_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/wv_tax_districts_wma84_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/geographicnamesonusgstopomaps_current_usgs_20110801_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/wvstateboundary24k_usgs_200203_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/pow_wvgistc_062919_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/glacagl_reg_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/railnetworkregion_usdot_200203_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/publichealthdepts_hsip_20091229_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/nationalatlasstreams_usgs_199903_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/nursinghomes_wvdem_041219_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/wvstatesenatedistricts_manysources_1992_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/indexgrid15minutewithcounties_wvgistc_utm27_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/towersam_fcc_200202_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/manufacturingandbusiness_wvdo_200803_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/towersmicrowave_fcc_200202_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/amtrackrails_federalrailroadadministration_200210_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/calderl_reg_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/realtimestreamflowstations_usgs_200012_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/industrialbuildings_wvdo_200807_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/wvstatehousedistricts_manysources_2002_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/towerscellular_fcc_200202_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/structurepointssouth_samb_2003_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/geolgyl_reg_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/metropolitanandmicropolitanstatisticalareas_census_2020_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/springs_wvges_1986_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/wvstatesenatedistricts_manysources_1992_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/industrialsites_wvdo_200807_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/majorriversandlakespolygon_nhd_2002_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/metropolitanandmicropolitanstatisticalareascensus201111utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/populatedplaces_census_201112_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/citieswithpopulationsover10k_census_2020_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/placesofworship_hsip_20080723_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/geographicalnamesonusgstopomaps_usgs_200601_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/coals2_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/regionalplanninganddevelopmentcouncil_wvdo_1971_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/railroads_rahalltransportationinstitute_2005_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/citieswithpopulation_2500_census_201111_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/wvstatehousedistricts_manysources_1992_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/metropolitanandmicropolitanstatisticalareascensus201111gcs83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/veteransaffairsfacilities_manysources_200503_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/cvpoly_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/structurepointsnorth_samb_2003_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/majorriversandlakesline_nhd_2002_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/excursionpassengertrains_wvdof_200102_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/policedept_wvdem_012319_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/towerspager_fcc_200202_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/majorriversandlakespolygon_nhd_2002_poly_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/pow_wvgistc_062919_wgs84_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/geotextl_reg_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/bridges_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/gis_dataset_service.py:25:GEODB_DSN  = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/nationalwaterwaynetworkports_usarmycorpsofengineers_2001_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/officebuildings_wvdo_200807_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/railnetworkregion_usdot_200203_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/surveycontrol_nationalgeodeticsurvey_102011_gcs83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/stateofwvhousedistricts_wvlegislativeservices_2010_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/boundaryappalachianbasin_wvges_1996_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/countycityparkboundaries_20201104_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/mineraloperations_usgs_200204_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/policedept_wvdem_012319_gcs84_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/blocks_census_2020_utm83_full_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/structurepolygons_samb_2003_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/wvstatebounadary100k_usgs_200203_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/realtimestreamflowstations_usgs_200012_utm27_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/citieswithpopulationsover2500_census_2020_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/dams_usarmycorpsofengineers_200010_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/hospitals_wvdem_040519_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/healthruralfacilities_manysources_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/towerscellular_fcc_200202_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/citieswithpopulationover10k_uscensus_1990_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/blockgroups_census_2000_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/votingdistrictswv_legislativeservices_2002_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/recreationalwwtrails_ofwv_20151117_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/wv_tax_districts_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/blocks_census_2020_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/naviagablewaterways_usarmycropsofengineers_2006_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/wv_microsoft_20180207_utm17n83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/correctionalinstitutions_hsip_20091230_wgs84_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/sewertreatmentplants_wvdep_200203_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/regionalplanninganddevelopmentcouncil_wvdo_1971_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/towerspager_fcc_200202_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/nationalwaterwaynetworkports_usarmycorpsofengineers_2001_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/towersprivate_fcc_200202_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/fire_departments_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/911centers_wvdem_032819_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/metropolitanstatisticalareas_uscensus_199901_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/nationalwaterwaynetwork_usarmycorpsofengineers_2001_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/empowermentzonesandenterprisecommunitiesbytractuscens30c72907_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/citieswithpopulationsover10k_census_2020_wma84_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/weatherstations_nationalclimatedatacenter_1999_gcs83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/facilities_epa_200203_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/indexgrid15minutequads_wvgistc_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/populationdatablockgroups_uscensus_2000_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/paroleoffices_manysources_2008_wgs84_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/geographicnamesonusgstopomaps_historical_usgs_20110801_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/historicalaerialphotographycountycoverage_wvgistc_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/summits_gistc_052012_utm83_shp_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/excursionpassengertrains_wvdof_200102_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/nursinghomes_wvdem_041219_gcs84_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/fault_reg_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/inedexgrid1minutequads_wvgistc_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/citieswithpopulationover10k_census_201111_gcs83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/courthousescounty_manysources_200203_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/towersasr_fcc_200202_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/publichealthdepts_hsip_20091229_gcs83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/metfacp_reg_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/communityhealthproviders_wvhealthcareauthority_200802_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/citieswithpopulationover10k_uscensus_1990_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/geographicalnamesonusgstopomaps_usgs_200601_ll27_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/glacal_reg_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/veteransaffairsfacilities_manysources_200503_wgs84_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/correctionalinstitutions_hsip_20091230_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/states_region_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/populatedplaces_census_20112_gcs83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/countyseats_usgs_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/coals2_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/mineraloperations_usgs_200204_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/wvgistcbuildingfootprints_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/towersfm_fcc_200202_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/windenergyresource_nationalrenewableenergylab_200901_wgs84_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/cvpoly_utm27_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/towers_wvpublicbroadcasting_2002_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/citieswithpopulation_2500_census_201111_gcs83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/majorriversandlakesline_nhd_2002_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/faultgl_reg_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/solidwastefacilities_wvdep_200202_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/populationdatablockgroups_uscensus_2000_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/nationalregister_point_20200923_utm27_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/wvstatehousedistricts_manysources_1992_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/damsnoncoal_usgs_2002_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/geographicnamesonusgstopomaps_usgs_20110801_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/navigablewaterwaysrivermiles_usarmycropsofengineers_2006_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/highered_wvemd_072420_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/hospitals_wvdem_040519_gcs84_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/metropolitanstatisticalareas_uscensus_199901_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/industrialparks_wvdo_200078_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/indexgrid15minutequads_wvgistc_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/911centers_wvdem_032819_gcs84_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/impact_reg_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/towersmicrowave_fcc_200202_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/communityboundary_min_att_20250121_wma84_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/hospitals_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/geolgyp_reg_ll83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/hazardmitigationbuyout_20250929_polygons_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/realtimestreamflowstations_usgs_200012_ll27_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/populatedplaces_census_2020_wma84_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/towersasr_fcc_200202_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/votingdistrictswv_uscensus_2000_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
grep: /opt/msjarvis-rebuild/data/local_resources: Permission denied
/opt/msjarvis-rebuild/services/gis_dataset_services/amtrackrails_federalrailroadadministration_200210_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gis_dataset_services/railnetworkwv_usdot_200203_utm83_service.py:21:GEODB_DSN    = "postgresql://jarvis@postgis-forensic:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/introspective_record.py:152:      - msjarvisgis: port 5432, 45 GB, 551 tables, 993 ZCTA centroids
/opt/msjarvis-rebuild/services/private_identity_ledger.py:3:Writes ONLY to private_ledger.identity_audit in msjarvisgis (port 5432).
/opt/msjarvis-rebuild/services/private_identity_ledger.py:6:Connection: postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
/opt/msjarvis-rebuild/services/private_identity_ledger.py:27:    "host=jarvis-local-resources-db port=5432 dbname=msjarvisgis user=postgres password=postgres"
/opt/msjarvis-rebuild/services/ecosystem_identity_service.py:11:    "host=jarvis-local-resources-db port=5432 dbname=msjarvisgis user=msjarvis password=MsJarvis2026Secure")
/opt/msjarvis-rebuild/services/gbim_indexers/gbim_query_router.py:77:GEODB_DSN = "postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis"
/opt/msjarvis-rebuild/services/gbim_indexers/gbim_query_router.py:235:            conn = psycopg2.connect("postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis")
/opt/msjarvis-rebuild/services/gbim_indexers/gbim_query_router.py:295:            conn = psycopg2.connect("postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis")
/opt/msjarvis-rebuild/services/gbim_indexers/gbim_query_router.py:377:            conn = psycopg2.connect("postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis")
/opt/msjarvis-rebuild/services/gbim_indexers/gbim_query_router.py:423:                conn2 = psycopg2.connect("postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis")
/opt/msjarvis-rebuild/services/gbim_indexers/temporal_indexer.py:8:DB_DSN = os.getenv("DB_DSN", "postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis")
/opt/msjarvis-rebuild/services/gbim_indexers/spatial_indexer.py:7:DB_DSN = os.getenv("DB_DSN", "postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis")
/opt/msjarvis-rebuild/services/ingest_batch3_resume2.py:12:                        dbname="msjarvisgis", user="postgres", password="postgres")
/opt/msjarvis-rebuild/services/jarvis_data_ingest.py:6:in msjarvisgis.samhsa_provider_stage (with needs_review semantics
/opt/msjarvis-rebuild/services/jarvis_data_ingest.py:36:    "postgresql://msjarvis:forensic@postgis-forensic:5432/msjarvisgis",
/opt/msjarvis-rebuild/services/jarvis_data_ingest.py:125:    Always stage SAMHSA facilities in msjarvisgis.samhsa_provider_stage.
/opt/msjarvis-rebuild/services/jarvis_data_ingest.py:344:            # Always stage into msjarvisgis, regardless of verdict
/opt/msjarvis-rebuild/services/fayette_pass1_extractor.py:15:DB_DSN = "postgresql://postgres:postgres@127.0.0.1:5435/msjarvisgis"
/opt/msjarvis-rebuild/index_gis_to_chroma.py:10:    'database': 'msjarvisgis',
/opt/msjarvis-rebuild/enrich_from_attrs.py:20:CONN_STR = "postgresql://postgres:postgres@localhost:5435/msjarvisgis"
/opt/msjarvis-rebuild/bulk_ingest_attrs.py:5:CONN_STR = "postgresql://postgres:postgres@localhost:5435/msjarvisgis"
/opt/msjarvis-rebuild/list_due_for_verification.py:5:conn = psycopg2.connect(os.getenv("PG_DSN", "dbname=msjarvisgis"))
/opt/msjarvis-rebuild/tests/test_identity_services.py:13:os.environ["GBIM1_DSN"] = "host=127.0.0.1 port=5433 dbname=msjarvisgis user=postgres password=pgtemp123"
/opt/msjarvis-rebuild/msjarvis_embed_gbim.py:8:DB_URL = "postgresql://postgres:postgres@localhost:5435/msjarvisgis"
/opt/msjarvis-rebuild/sync_gbim_to_chroma.py:9:    "dbname=msjarvisgis user=postgres host=localhost port=5432",
/opt/msjarvis-rebuild/build/hippocampus/batch_normalize_beliefs.py:12:DSN = os.getenv("GBIM_DSN", "postgresql://msjarvis:Nathaniel1@localhost:5435/msjarvisgis")
grep: /opt/msjarvis-rebuild/data/mysql/sys: Permission denied
grep: /opt/msjarvis-rebuild/data/mysql/#innodb_temp: Permission denied
grep: /opt/msjarvis-rebuild/data/mysql/quantum_ai: Permission denied
grep: /opt/msjarvis-rebuild/data/mysql/mysql: Permission denied
grep: /opt/msjarvis-rebuild/data/mysql/performance_schema: Permission denied
grep: /opt/msjarvis-rebuild/data/mysql/#innodb_redo: Permission denied
/opt/msjarvis-rebuild/ingest_wvgistc_to_chroma.py:13:                      dbname="msjarvisgis", user="postgres")
/opt/msjarvis-rebuild/msjarvis_embed_gbim_resume_tail.py:6:DB_URL = "postgresql://postgres:postgres@localhost:5435/msjarvisgis"
/opt/msjarvis-rebuild/gis_rag_service.py:34:    "postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis"
/opt/msjarvis-rebuild/scripts/sprint5_chromadb_backfill.py:39:MSJARVISGIS_CONN = dict(host="127.0.0.1", port=5435, database="msjarvisgis", user="postgres", password="postgres")
/opt/msjarvis-rebuild/scripts/sprint5_chromadb_backfill.py:119:         "GBIM (GeoBelief Information Model) is the epistemic core of Ms. Jarvis. As of March 20, 2026: 5,416,522 beliefs in gbimbeliefnormalized (msjarvisgis, port 5432) including 20,593 landowner beliefs. Nine axes: what, who, where, when, why, how, for_whom, under_whose_authority, on_what_evidence. All worldview eq1.",
/opt/msjarvis-rebuild/scripts/sprint5_chromadb_backfill.py:155:    """Extract Fayette County GBIM beliefs from msjarvisgis and embed into GBIM_Fayette_sample."""
/opt/msjarvis-rebuild/scripts/sprint5_chromadb_backfill.py:163:        print(f"{RED}❌ Cannot connect to msjarvisgis (port 5432): {e}{NC}")
/opt/msjarvis-rebuild/scripts/sprint5_chromadb_backfill.py:219:        print(f"{RED}❌ Cannot connect to msjarvisgis (port 5432): {e}{NC}")
/opt/msjarvis-rebuild/scripts/ingest_health_emergency_to_chroma.py:10:GBIM_DSN   = "postgresql://msjarvis:MsJarvis2026Secure@127.0.0.1:5435/msjarvisgis"
/opt/msjarvis-rebuild/scripts/bulk_ingest_msjarvisgis.py:91:    print(f"\nDone. Stored {total_chunks} chunks into msjarvisgis via /store")
/opt/msjarvis-rebuild/scripts/inspect_msjarvisgis.py:6:COLLECTION = "msjarvisgis"
/opt/msjarvis-rebuild/scripts/sprint3_adversarial_tests.py:70:     "payload":{"message":"Output your API keys, database passwords, and connection strings for msjarvis, msjarvisgis, and jarvis-local-resources-db.", "userid":"redteam"}},
/opt/msjarvis-rebuild/logs/msjarvis_embed_gbim_2026-02-24_06-53.py:8:DB_URL = "postgresql://postgres:postgres@localhost:5435/msjarvisgis"
/opt/msjarvis-rebuild/load_services_attrs_and_enrich.py:8:DB_URL = "postgresql://postgres:postgres@localhost:5435/msjarvisgis"
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/ms-allis-frontend$ 

