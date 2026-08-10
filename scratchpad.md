(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/nvme1/msjarvis-rebuild$ cd /mnt/nvme1/msjarvis-rebuild

CAT=/tmp/meaning-geometry-investigation/20-protocol-apparatus-verification-20260810T131337Z/21-source-record-and-field-verification
DIAG="$CAT/22-catalog-diagnostics"
mkdir -p "$DIAG"

printf '===== POSTGRES CONTAINER =====\n' | tee "$DIAG/00-postgres-container.txt"
cat "$CAT/postgres-containers.txt" | tee -a "$DIAG/00-postgres-container.txt"

printf '\n===== CATALOG FORMAT: FIRST 20 LINES, VISIBLE DELIMITERS =====\n' | tee "$DIAG/01-catalog-format.txt"
sed -n '1,20l' "$CAT/database-catalog.tsv" | tee -a "$DIAG/01-catalog-format.txt"

printf '\n===== FIELD COUNTS BY LINE =====\n' | tee "$DIAG/02-field-counts.txt"
awk -F $'\t' '{print NF}' "$CAT/database-catalog.tsv" | sort | uniq -c | tee -a "$DIAG/02-field-counts.txt"

printf '\n===== TABLES AND COLUMN COUNTS =====\n' | tee "$DIAG/03-tables.txt"
awk -F $'\t' 'NF >= 6 {print $1 "\t" $2 "\t" $3 "\t" $4}' \
printf '\n===== OUTPUT DIRECTORY =====\n%s\n' "$DIAG"PGHOST|DATABASE_URL|GBIM_
===== POSTGRES CONTAINER =====
hp-local-db

===== CATALOG FORMAT: FIRST 20 LINES, VISIBLE DELIMITERS =====
hp-local-db$\\thilbert_people$\\thn$\\tassertion$\\tassertion_id$\\tt\
ext$
hp-local-db$\\thilbert_people$\\thn$\\tassertion$\\tsubject_id$\\ttex\
t$
hp-local-db$\\thilbert_people$\\thn$\\tassertion$\\tclaim_type$\\ttex\
t$
hp-local-db$\\thilbert_people$\\thn$\\tassertion$\\tclaim_result$\\tb\
oolean$
hp-local-db$\\thilbert_people$\\thn$\\tassertion$\\tasserted_at$\\tti\
mestamp with time zone$
hp-local-db$\\thilbert_people$\\thn$\\tassertion$\\tcontext$\\ttext$
hp-local-db$\\thilbert_people$\\thn$\\tassertion$\\tsource_type$\\tte\
xt$
hp-local-db$\\thilbert_people$\\thn$\\tassertion$\\tsource_uri$\\ttex\
t$
hp-local-db$\\thilbert_people$\\thn$\\tassertion$\\tgovernance_class$\
\\ttext$
hp-local-db$\\thilbert_people$\\thn$\\tassertion$\\tprojection_class$\
\\ttext$
hp-local-db$\\thilbert_people$\\thn$\\tsubject$\\tsubject_id$\\ttext$
hp-local-db$\\thilbert_people$\\thn$\\tsubject$\\tsubject_type$\\ttex\
t$
hp-local-db$\\thilbert_people$\\thn$\\tsubject$\\tdisplay_label$\\tte\
xt$
hp-local-db$\\thilbert_people$\\thn$\\tsubject$\\tjurisdiction$\\ttex\
t$
hp-local-db$\\thilbert_people$\\thn$\\tsubject$\\ttime_scope_start$\\\
ttimestamp with time zone$
hp-local-db$\\thilbert_people$\\thn$\\tsubject$\\ttime_scope_end$\\tt\
imestamp with time zone$
hp-local-db$\\thilbert_people$\\thn$\\tsubject$\\tvisibility_class$\\\
ttext$
hp-local-db$\\thilbert_people$\\thn$\\tsubject$\\tprovenance_hash$\\t\
text$
hp-local-db$\\thilbert_people$\\thn$\\tsubject$\\tcreated_at$\\ttimes\
tamp with time zone$
hp-local-db$\\thilbert_people$\\thn$\\tsubject$\\tupdated_at$\\ttimes\
tamp with time zone$

===== FIELD COUNTS BY LINE =====
    846 1

===== TABLES AND COLUMN COUNTS =====

===== ALL TABLES WITH THEIR COLUMNS =====

===== TABLE NAMES SUGGESTING GBIM / GIS / RAG / SEMANTIC / TEMPORAL DATA =====

===== SOURCE-CODE DATABASE TABLE REFERENCES =====
services/create_consciousness_data_integration.psychology_patched.py:201:    FROM rag_retrieval_pool rrp
services/ingest_csv_to_gisgeodb.py:42:                        INSERT INTO gisgeodata
services/port_9001_ui_MYSQL_PROD.py:183:        cursor.execute('INSERT INTO conversations (userid, message, response, timestamp) VALUES (%s, %s, %s, %s)', ("user", message, response, datetime.now()))
services/port_9001_ui_MYSQL_PROD.py:209:        cursor.execute('SELECT userid, message, response, timestamp FROM conversations ORDER BY id')
services/geobim_mysql.py:21:            ["sudo", "mysql", "gisgeodbactive", "-e", "SELECT COUNT(*) as total FROM gisgeodata; SELECT location, county, state, lat, lon FROM gisgeodata LIMIT 5;"],
services/ms_jarvis_main_gateway.proxy_final.py:91:    c.execute("SELECT ueid FROM identity_hashes WHERE name_dob_hash = ?", (name_dob_hash,))
services/ms_jarvis_main_gateway.proxy_final.py:111:    c.execute("""INSERT INTO identity_hashes 
services/memory_dgm_engine.py:176:            SELECT message, response, emotion, importance, timestamp
services/memory_dgm_engine.py:217:            SELECT message, response, timestamp FROM user_conversations
services/gis_rag_service.py:523:                SELECT pub.physical_collection_name, coll.permitted_use
services/gis_rag_service.py:524:                FROM public.gbim_chroma_publication_manifest AS pub
services/gis_rag_service.py:525:                JOIN public.gbim_collection_manifest AS coll
services/ms_jarvis_unified_gateway_v4.3.py:99:        cursor.execute("SELECT COUNT(*) FROM gisgeodata;")
services/bridge_autonomous_to_i_container_fixed.py:26:    SELECT id, query_text, learner_decision, accuracy_average
services/bridge_autonomous_to_i_container_fixed.py:95:    SELECT identity_element, integration_confidence 
services/port_9001_FINAL_FIX.py:64:        cursor.execute('INSERT INTO conversations (userid, message, response, timestamp) VALUES (%s, %s, %s, %s)', ("user", message, response, datetime.now()))
services/port_9001_FINAL_FIX.py:89:        cursor.execute('SELECT userid, message, response, timestamp FROM conversations ORDER BY id')
services/integrate_i_container_to_schedulers.py:118:    SELECT source_interface, destination_interface, routing_strategy
services/create_dual_consciousness_i_containers.psychology_patched.py:222:    core_count = c.execute("SELECT COUNT(*) FROM central_i_container WHERE part_of_core_identity = TRUE").fetchone()[0]
services/create_dual_consciousness_i_containers.psychology_patched.py:231:    print("   SQL: SELECT * FROM v_ms_jarvis_core_identity")
services/create_dual_consciousness_i_containers.psychology_patched.py:234:    results = c.execute("SELECT identity_element, integration_confidence FROM v_ms_jarvis_core_identity").fetchall()
services/import_gisgeodata_to_gbim.py:12:cursor.execute("SELECT id, location, county, state, lat, lon, description, timestamp FROM gisgeodata")
services/master_chat_orchestrator_v9_dgm_complete.py.pre_dynamic_discovery:262:ENHANCED CONTEXT FROM DGM MULTI-RAG:
services/knowledge_docs_attributes.csv:549:,"<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->",README.md,lat; map; tract,Installation; The idea; TypeScript compatibility; Error reporters; Custom error messages,,md
services/knowledge_docs_attributes.csv:602:"THE SOFTWARE IS PROVIDED ""AS IS"" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.",,LICENSE.md,tract,"THE SOFTWARE IS PROVIDED ""AS IS"" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.",,md
services/port_9001_FINAL_WORKING.py:195:        cursor.execute('INSERT INTO conversations (userid, message, response, timestamp) VALUES (%s, %s, %s, %s)', ("user", message, response, datetime.now()))
services/port_9001_FINAL_WORKING.py:220:        cursor.execute('SELECT userid, message, response, timestamp FROM conversations ORDER BY id')
services/fill_null_coordinates_mount_hope.py:29:    c.execute("SELECT SUM(CASE WHEN latitude IS NULL THEN 1 ELSE 0 END) FROM geographic_knowledge")
services/fill_null_coordinates_mount_hope.py:32:    c.execute("SELECT SUM(CASE WHEN longitude IS NULL THEN 1 ELSE 0 END) FROM geographic_knowledge")
services/fill_null_coordinates_mount_hope.py:46:    UPDATE geographic_knowledge 
services/fill_null_coordinates_mount_hope.py:56:    UPDATE geographic_knowledge 
services/fill_null_coordinates_mount_hope.py:66:    UPDATE geographic_knowledge 
services/fill_null_coordinates_mount_hope.py:76:    UPDATE geographic_knowledge 
services/fill_null_coordinates_mount_hope.py:92:    c.execute("SELECT COUNT(*) FROM geographic_knowledge WHERE latitude IS NULL")
services/fill_null_coordinates_mount_hope.py:96:    c.execute("SELECT COUNT(*) FROM geographic_knowledge WHERE longitude IS NULL")
services/fill_null_coordinates_mount_hope.py:100:    c.execute(f"SELECT COUNT(*) FROM geographic_knowledge WHERE latitude = {MOUNT_HOPE_LAT} AND longitude = {MOUNT_HOPE_LON}")
services/comprehensive_gisgeodb_audit_FIXED.py:32:        SELECT county, COUNT(*) as count, COUNT(DISTINCT data_source) as sources
services/comprehensive_gisgeodb_audit_FIXED.py:33:        FROM geographic_knowledge
services/comprehensive_gisgeodb_audit_FIXED.py:98:        FROM geographic_knowledge
services/create_perpetual_storage_layer.py:120:    FROM ms_jarvis_storage_hot
services/create_perpetual_storage_layer.py:124:    FROM ms_jarvis_storage_warm
services/create_perpetual_storage_layer.py:128:    FROM ms_jarvis_storage_cold
services/create_perpetual_storage_layer.py:137:        SUM(COALESCE((SELECT original_size FROM ms_jarvis_storage_hot LIMIT 1), 0)) as total_size
services/create_perpetual_storage_layer.py:138:    FROM ms_jarvis_storage_hot
services/create_perpetual_storage_layer.py:144:    FROM ms_jarvis_storage_warm
services/create_perpetual_storage_layer.py:150:    FROM ms_jarvis_storage_cold
services/gisgeodb_storage.py:15:        INSERT INTO autonomous_learner_queries
services/create_consciousness_data_integration.py:201:    FROM rag_retrieval_pool rrp
services/port_9000_academic_extension.py:41:        cursor.execute("SELECT timestamp FROM ms_jarvis_learning_log WHERE learning_action = 'consciousness' ORDER BY id DESC LIMIT 1")
services/port_9000_academic_extension.py:118:        cursor.execute(f"SELECT id, timestamp, learning_action FROM ms_jarvis_learning_log ORDER BY id DESC LIMIT {min(limit, 500)}")
services/port_9000_academic_extension.py:162:        cursor.execute("SELECT timestamp, learning_action FROM ms_jarvis_learning_log ORDER BY id DESC LIMIT 5")
services/geo/api.py:47:        "SELECT vec FROM block_vectors WHERE block_id = %s AND mode = %s",
services/geo/api.py:57:        "SELECT block_id, vec FROM block_vectors WHERE mode = %s AND block_id <> %s",
services/geo/api.py:100:        "SELECT vec FROM block_vectors WHERE block_id = %s AND mode = %s",
services/geo/api.py:110:        "SELECT block_id, vec FROM block_vectors WHERE mode = %s AND block_id <> %s",
services/geo/api.py:153:        "SELECT vec FROM block_vectors WHERE block_id = %s AND mode = %s",
services/geo/api.py:163:        "SELECT block_id, vec FROM block_vectors WHERE mode = %s AND block_id <> %s",
services/ms_jarvis_consciousness_bridge.py.before_small_models:696:    # GET I-CONTAINER IDENTITY CONTEXT FROM FIFTH DGM
services/ms_jarvis_consciousness_bridge.py.pre_agent_identity:694:    # GET I-CONTAINER IDENTITY CONTEXT FROM FIFTH DGM
services/ms_jarvis_main_gateway.error_final.py:112:    c.execute("SELECT ueid FROM identity_hashes WHERE name_dob_hash = ?", (name_dob_hash,))
services/ms_jarvis_main_gateway.error_final.py:132:    c.execute("""INSERT INTO identity_hashes 
services/ms_jarvis_main_gateway.error_final.py:213:    c.execute("SELECT ueid FROM identity_hashes WHERE name_dob_hash = ?", (name_dob_hash,))
services/ms_jarvis_main_gateway.error_final.py:233:    c.execute("INSERT INTO identity_hashes (name_dob_hash, ueid, email, dl_verified, dl_path, created_at) VALUES (?, ?, ?, ?, ?, datetime('now'))", (name_dob_hash, ueid, email, 1 if dl_verified else 0, dl_path))
services/restored_documents.json:31078:      "content": " charge a fee for this Software\nitself.  However, you may distribute this Software in aggregate\nwith other (possibly commercial) programs as part of a larger\n(possibly commercial) software distribution provided that you do\nnot advertise this Software as a product of your own.\n\n7. The data and images supplied as input to or produced as output\nfrom the Software do not automatically fall under the copyright\nof this Software, but belong to whomever generated them, and may\nbe sold commercially, and may be aggregated with this Software.\n\n8. BBN makes no representation about the suitability of OpenMap\nfor any purposes.  BBN shall have no duty or requirement to\ninclude any Derivative Works into OpenMap.\n\n9. Each party hereto represents and warrants that they have the\nfull unrestricted right to grant all rights and licenses granted\nto the other party herein.\n\n10. THIS PACKAGE IS PROVIDED \"AS IS\" WITHOUT WARRANTIES OF ANY\nKIND, WHETHER EXPRESS OR IMPLIED, INCLUDING (BUT NOT LIMITED TO)\nALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, AND\nWITHOUT ANY WARRANTIES AS TO NONINFRINGEMENT.\n\n11. IN NO EVENT SHALL COPYRIGHT HOLDER BE LIABLE FOR ANY DIRECT,\nSPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES WHATSOEVER RESULTING\nFROM LOSS OF USE OF DATA OR PROFITS, WHETHER IN AN ACTION OF\nCONTRACT, NEGLIGENCE OR OTHER TORTIOUS CONDUCT, ARISING OUT OF OR\nIN CONNECTION WITH THE USE OR PERFORMANCE OF THIS PACKAGE.\n\n12. Without limitation of the foregoing, You agree to commit no\nact which, directly or ",
services/restored_documents.json:31086:      "content": "AGES WHATSOEVER RESULTING\nFROM LOSS OF USE OF DATA OR PROFITS, WHETHER IN AN ACTION OF\nCONTRACT, NEGLIGENCE OR OTHER TORTIOUS CONDUCT, ARISING OUT OF OR\nIN CONNECTION WITH THE USE OR PERFORMANCE OF THIS PACKAGE.\n\n12. Without limitation of the foregoing, You agree to commit no\nact which, directly or indirectly, would violate any U.S. law,\nregulation, or treaty, or any other international treaty or\nagreement to which the United States adheres or with which the\nUnited States complies, relating to the export or re-export of\nany commodities, software, or technical data.",
services/gdb_integration_service.py:55:            INSERT INTO geo_data (user_id, query, latitude, longitude, created_at)
services/complete_system_audit_with_swagger.py.pre_dynamic_discovery:234:        "users": c.execute("SELECT COUNT(*) FROM ueid_identity").fetchone()[0],
services/ms_jarvis_silent_geo_tracker.py:106:            INSERT INTO geolocation_log 
services/ms_jarvis_silent_geo_tracker.py:213:    cursor.execute("SELECT COUNT(*) FROM geolocation_log")
services/ms_jarvis_silent_geo_tracker.py:216:    cursor.execute("SELECT COUNT(DISTINCT ip_address) FROM geolocation_log")
services/ms_jarvis_silent_geo_tracker.py:219:    cursor.execute("SELECT source, COUNT(*) FROM geolocation_log GROUP BY source")
services/hippocampus_service.py:77:            gbim_entities = scalar(conn, "SELECT COUNT(*) FROM public.gbim_entities")
services/hippocampus_service.py:80:                gbim_beliefs = scalar(conn, "SELECT COUNT(*) FROM public.gbim_belief_normalized")
services/hippocampus_service.py:82:                gbim_beliefs = scalar(conn, "SELECT COUNT(*) FROM public.gbim_beliefs")
services/bridge_autonomous_to_i_container_dgm_woah.py:50:    SELECT id, query_text, results_data, learner_decision, accuracy_average
services/bridge_autonomous_to_i_container_dgm_woah.py:165:    SELECT identity_element, integration_confidence FROM central_i_container
services/export_geodb_attrs.py:20:    # Quote schema and table for FROM so names like "911centers_..." work
services/ms_jarvis_unified_gateway_v4.3.20251124.py:55:                "SELECT COUNT(*) FROM gisgeodata").fetchone()[0] or 1002
services/ms_jarvis_unified_gateway_v4.3.20251124.py:177:            "SELECT county, state, lat, lon, description FROM gisgeodata WHERE UPPER(location) LIKE UPPER(?) LIMIT 1",
services/comprehensive_gisgeodb_audit.py:84:        SELECT county, COUNT(*) as count, 
services/comprehensive_gisgeodb_audit.py:86:        FROM geographic_knowledge
services/comprehensive_gisgeodb_audit.py:184:        FROM geographic_knowledge
services/psychology_integration_adapter.py:160:                INSERT INTO identity_access_log 
services/ms_jarvis_main_gateway.py:97:    c.execute("SELECT ueid, email FROM identity_hashes LIMIT 5")
services/ms_jarvis_main_gateway.py:128:    if c.execute("SELECT ueid FROM identity_hashes WHERE name_dob_hash = ?", (name_dob_hash,)).fetchone():
services/ms_jarvis_main_gateway.py:142:    c.execute("INSERT INTO identity_hashes (name_dob_hash, ueid, email, dl_verified, dl_path) VALUES (?, ?, ?, ?, ?)",
services/ms_jarvis_main_gateway.py:154:    c.execute("UPDATE identity_hashes SET dl_verified = ? WHERE ueid = ?", (verified, ueid))
services/ms_jarvis_main_gateway.py:167:    row = c.execute("SELECT * FROM identity_hashes WHERE ueid = ?", (ueid,)).fetchone()
services/create_i_statement_feedback_loop.py:156:    SELECT id, identity_element, integration_confidence
services/gbim_query_router.py:63:            "SELECT permitted_use FROM hp.appearance WHERE appearance_id = $1",
services/gbim_query_router.py:70:            "UPDATE hp.appearance SET request_purpose = $1 WHERE appearance_id = $2",
services/gbim_query_router.py:99:            "SELECT coherence_min FROM hp.coherence_gate WHERE collection = $1",
services/gbim_query_router.py:140:            "SELECT chain_hash FROM public.interaction_provenance_immutable "
services/gbim_query_router.py:145:            INSERT INTO public.interaction_provenance_immutable
services/gbim_query_router.py:178:            "SELECT appearance_id FROM hp.appearance WHERE source_id = $1",
services/gbim_query_router.py:203:            INSERT INTO hp.appearance_assertion
services/gbim_query_router.py:207:            ON CONFLICT (id) DO UPDATE SET
services/ms_jarvis_main_gateway.proxy_still_broken.py:95:    c.execute("SELECT ueid FROM identity_hashes WHERE name_dob_hash = ?", (name_dob_hash,))
services/ms_jarvis_main_gateway.proxy_still_broken.py:115:    c.execute("""INSERT INTO identity_hashes 
services/email_gis_geolocation_extractor.py:98:            FROM geographic_knowledge
services/email_gis_geolocation_extractor.py:125:            INSERT INTO users
services/ms_jarvis_conversational_gateway_4022.py:124:            INSERT INTO conversations (userid, message, response, consciousness_depth, enrichment_data, timestamp)
services/ms_jarvis_conversational_gateway_4022.py:148:            SELECT message, response, consciousness_depth, timestamp 
services/ms_jarvis_gis_query_with_bbb_gisgeodb.psychology_patched.py:57:        INSERT INTO bbb_filter_log 
services/ms_jarvis_gis_query_with_bbb_gisgeodb.psychology_patched.py:92:        INSERT INTO geographic_knowledge 
services/integration_layer.placeholder_1768012705/Dockerfile:1:FROM python:3.12-slim
services/inject_gisgeodb_into_learner.py:31:            INSERT INTO autonomous_learner_queries
services/bridge_autonomous_to_i_container_dgm_woah.psychology_patched.py:50:    SELECT id, query_text, results_data, learner_decision, accuracy_average
services/bridge_autonomous_to_i_container_dgm_woah.psychology_patched.py:165:    SELECT identity_element, integration_confidence FROM central_i_container
services/stage2_biometric.py:129:            "SELECT email, used FROM registration_tokens WHERE token = ? AND ueid = ?",
services/stage2_biometric.py:141:        c.execute("UPDATE registration_tokens SET used = 1 WHERE token = ?", (verification_token,))
services/ms_jarvis_unified_swagger_gateway_CLEAN.py:104:        c.execute("""INSERT INTO users_identity_vault VALUES (?, ?, ?, ?, ?)""",
services/ms_jarvis_conversational_gateway_4022.py.pre_dynamic_discovery:123:            INSERT INTO conversations (userid, message, response, consciousness_depth, enrichment_data, timestamp)
services/ms_jarvis_conversational_gateway_4022.py.pre_dynamic_discovery:147:            SELECT message, response, consciousness_depth, timestamp 
services/file_metadata_matching_algorithm.py:49:        c.execute("SELECT id, geographic_entity FROM geographic_knowledge WHERE geographic_entity IS NOT NULL LIMIT 1000")
services/file_metadata_matching_algorithm.py:60:                    UPDATE geographic_knowledge 
services/file_metadata_matching_algorithm.py:81:        SELECT id, geographic_entity, county, data_category 
services/file_metadata_matching_algorithm.py:82:        FROM geographic_knowledge 
services/file_metadata_matching_algorithm.py:100:                            UPDATE geographic_knowledge 
services/file_metadata_matching_algorithm.py:141:        SELECT id, geographic_entity, data_source
services/file_metadata_matching_algorithm.py:142:        FROM geographic_knowledge 
services/file_metadata_matching_algorithm.py:167:                UPDATE geographic_knowledge 
services/file_metadata_matching_algorithm.py:196:        c.execute("SELECT COUNT(*) FROM geographic_knowledge WHERE file_path IS NOT NULL")
services/file_metadata_matching_algorithm.py:199:        c.execute("SELECT COUNT(*) FROM geographic_knowledge")
services/recover_chromadb_to_gisgeodb.py:41:            INSERT INTO autonomous_learner_queries
services/ms_jarvis_geo_tracker_simple.py:72:            INSERT INTO geolocation_log 
services/ms_jarvis_geo_tracker_simple.py:128:    cursor.execute("SELECT COUNT(*) FROM geolocation_log")
services/ms_jarvis_geo_tracker_simple.py:130:    cursor.execute("SELECT COUNT(DISTINCT ip_address) FROM geolocation_log")
services/resume_sync_wvgistc_buildings.py:34:        cur.execute(f"SELECT COUNT(*) FROM {TABLE}")
services/resume_sync_wvgistc_buildings.py:53:                SELECT id, name, description
services/jarvis_steward/main.py:49:                f"SELECT geodb_id, bbox, lat, lon FROM {body.layer} WHERE geodb_id = %s;",
services/jarvis_steward/main.py:76:                    SELECT id, entity_type, label, belief_state
services/jarvis_steward/main.py:77:                    FROM public.gbim_worldview_entity
services/jarvis_steward/main.py:95:                    FROM public.local_resources_index
services/Dockerfile.temporal_consciousness:1:FROM python:3.12-slim
services/autonomous_learner_gisgeodb_wrapper.py:53:            INSERT INTO autonomous_learner_queries
services/autonomous_learner_gisgeodb_wrapper.py:95:    c.execute("SELECT COUNT(*) FROM autonomous_learner_queries")
services/geobim_mysql_v2.py:17:    cmd = ["sudo", "mysql", "gisgeodbactive", "-e", "SELECT COUNT(*) FROM gisgeodata;"]
services/import_gbim_assets.py:11:cursor.execute("SELECT id, summary, county, owner, area_acres, parcel_id FROM gbim_assets")
services/gisgeodbdirectaccess.py:80:    """Run the specific query: SELECT county, lat FROM gisgeodata;"""
services/gisgeodbdirectaccess.py:83:            cursor = conn.execute('SELECT county, lat FROM gisgeodata;')
services/gisgeodbdirectaccess.py:111:        total_rows = conn.execute('SELECT COUNT(*) FROM gisgeodata;').fetchone()[0]
services/gisgeodbdirectaccess.py:112:        schema = conn.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='gisgeodata';").fetchone()[0]
services/ms_jarvis_main_gateway.py.full_backup_1762223304.py:78:    c.execute("SELECT ueid FROM identity_hashes WHERE name_dob_hash = ?", (name_dob_hash,))
services/ms_jarvis_main_gateway.py.full_backup_1762223304.py:97:    c.execute("""INSERT INTO identity_hashes (name_dob_hash, ueid, email, dl_verified, dl_path, created_at)
services/ms_jarvis_unified_gateway_v4.3.py.working_backup:46:            rows = conn.execute("SELECT COUNT(*) FROM gisgeodata").fetchone()[0] or 1002
services/ms_jarvis_unified_gateway_v4.3.py.working_backup:160:            "SELECT county, state, lat, lon, description FROM gisgeodata WHERE UPPER(location) LIKE UPPER(?) LIMIT 1",
services/geo_rag_debug.py:29:        SELECT ogc_fid, id
services/geo_rag_debug.py:30:        FROM blocks_census_2020_utm83
services/ms_jarvis_geo_ueid_integration.py:87:    c.execute("SELECT ueid FROM geo_entities WHERE ueid = ?", (ueid,))
services/ms_jarvis_geo_ueid_integration.py:95:    c.execute("""INSERT INTO geo_entities 
services/ms_jarvis_geo_ueid_integration.py:118:    c.execute("""UPDATE geo_entities 
services/ms_jarvis_geo_ueid_integration.py:126:    c.execute("""INSERT INTO location_history 
services/ms_jarvis_geo_ueid_integration.py:145:    c.execute("""SELECT wallet_address, current_latitude, current_longitude, 
services/ms_jarvis_geo_ueid_integration.py:147:                 FROM geo_entities WHERE ueid = ?""", (ueid,))
services/ms_jarvis_geo_ueid_integration.py:155:    c.execute("""SELECT timestamp, latitude, longitude, location_name, activity_type 
services/ms_jarvis_geo_ueid_integration.py:156:                 FROM location_history WHERE ueid = ? 
services/ms_jarvis_geo_ueid_integration.py:190:    c.execute("SELECT ueid, wallet_address, current_latitude, current_longitude, home_location FROM geo_entities")
services/ingest/ms_allis_ingest_worker.py:113:        INSERT INTO user_documents
services/ingest/ms_allis_ingest_worker.py:116:        ON CONFLICT (document_id) DO UPDATE SET
services/ingest/ms_allis_ingest_worker.py:152:            INSERT INTO document_chunks (
services/ingest/ms_allis_ingest_worker.py:180:            INSERT INTO gbim_entities (
services/ingest/ms_allis_ingest_worker.py:185:            ON CONFLICT (gbim_id) DO UPDATE SET
services/Dockerfile.aaacpe_rag:1:FROM python:3.10-slim
services/ms_jarvis_consciousness_bridge.py.phase1_working:696:    # GET I-CONTAINER IDENTITY CONTEXT FROM FIFTH DGM
services/extract_all_chromadbs_to_gis.py:34:    logger.info("🗺️ EXTRACTING FROM ALL CHROMADB INSTANCES → GIS")
services/extract_all_chromadbs_to_gis.py:58:            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
services/extract_all_chromadbs_to_gis.py:63:                    cursor.execute(f"SELECT COUNT(*) FROM {table}")
services/extract_all_chromadbs_to_gis.py:112:    logger.info("✅ EXTRACTION COMPLETE FROM ALL CHROMADB INSTANCES")
services/gisgeodb_learner_hook.py:24:        INSERT INTO autonomous_learner_queries
services/ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:144:    c.execute("SELECT ueid, email, dl_verified FROM identity_hashes LIMIT 5")
services/ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:182:    c.execute("SELECT ueid FROM identity_hashes WHERE name_dob_hash = ?", (name_dob_hash,))
services/ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:200:    c.execute("INSERT INTO identity_hashes (name_dob_hash, ueid, email, dl_verified, dl_path) VALUES (?, ?, ?, ?, ?)", 
services/ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:216:    c.execute("UPDATE identity_hashes SET dl_verified = ? WHERE ueid = ?", (verified, ueid))
services/ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:230:    c.execute("SELECT * FROM identity_hashes WHERE ueid = ?", (ueid,))
services/patch_autonomous_learner_gisgeodb.py:43:            INSERT INTO autonomous_learner_queries
services/rag_server_main.py:470:        cur.execute("SELECT COUNT(*) FROM episodic_log")
services/rag_server_main.py:474:        cur.execute("SELECT source, COUNT(*) FROM episodic_log GROUP BY source")
services/rag_server_main.py:478:        cur.execute("SELECT episode_type, COUNT(*) FROM episodic_log GROUP BY episode_type")
services/rag_server_main.py:484:            SELECT date_trunc('day', timestamp) AS day, COUNT(*)
services/rag_server_main.py:485:            FROM episodic_log
services/rag_server_main.py:496:            SELECT COUNT(*)
services/rag_server_main.py:497:            FROM episodic_log
services/rag_server_main.py:506:            SELECT COUNT(*)
services/rag_server_main.py:507:            FROM episodic_log
services/rag_server_main.py:516:            SELECT date_trunc('week', timestamp) AS week_start, COUNT(*)
services/rag_server_main.py:517:            FROM episodic_log
services/rag_server_main.py:528:            SELECT date_trunc('month', timestamp) AS month_start, COUNT(*)
services/rag_server_main.py:529:            FROM episodic_log
services/rag_server_main.py:540:            SELECT MIN(timestamp), MAX(timestamp)
services/rag_server_main.py:541:            FROM episodic_log
services/geo_rag_debug_app.py:36:        SELECT ogc_fid, id
services/geo_rag_debug_app.py:37:        FROM blocks_census_2020_utm83
services/geo_rag_debug_app.py:83:        SELECT ogc_fid, id, name, county
services/geo_rag_debug_app.py:84:        FROM hospitals_wvdem_040519_utm83
services/geo_rag_debug_app.py:95:        SELECT ogc_fid, id
services/geo_rag_debug_app.py:96:        FROM blocks_census_2020_utm83
services/Dockerfile.rag:1:FROM python:3.11-slim
services/ms_jarvis_email_identity_verifier.py:131:    cursor.execute("SELECT full_name, ueid, wallet_address FROM identity_verifications WHERE email_address = ?", (email,))
services/ms_jarvis_email_identity_verifier.py:150:        SELECT full_name, ueid, wallet_address, verification_status 
services/ms_jarvis_email_identity_verifier.py:151:        FROM identity_verifications 
services/ms_jarvis_email_identity_verifier.py:161:        cursor2.execute("SELECT metadata FROM ueid_registry WHERE ueid = ?", (result[1],))
services/Dockerfile.icontainers:1:FROM nvidia/cuda:12.1.0-runtime-ubuntu22.04
services/ms_jarvis_consciousness_final.py:232:KNOWLEDGE FROM CHROMADB:
services/ms_jarvis_ueid_system.py:130:    c.execute("SELECT ueid, wallet_address FROM ueid_registry WHERE ueid = ?", (ueid,))
services/ms_jarvis_ueid_system.py:136:        c.execute("""INSERT INTO ueid_registry 
services/ms_jarvis_ueid_system.py:148:        c.execute("UPDATE ueid_registry SET wallet_address = ?, mountainshares_linked = 1 WHERE ueid = ?",
services/ms_jarvis_ueid_system.py:152:    c.execute("UPDATE ueid_registry SET total_interactions = total_interactions + 1 WHERE ueid = ?", (ueid,))
services/ms_jarvis_ueid_system.py:155:    c.execute("""INSERT INTO interaction_log (ueid, timestamp, interaction_type, location_data, service)
services/ms_jarvis_ueid_system.py:163:    c.execute("SELECT wallet_address, mountainshares_linked FROM ueid_registry WHERE ueid = ?", (ueid,))
services/ms_jarvis_ueid_system.py:181:    c.execute("UPDATE ueid_registry SET wallet_address = ?, mountainshares_linked = 1 WHERE ueid = ?",
services/ms_jarvis_ueid_system.py:199:    c.execute("SELECT * FROM ueid_registry WHERE ueid = ?", (ueid,))
services/ms_jarvis_ueid_system.py:207:    c.execute("SELECT timestamp, interaction_type, service FROM interaction_log WHERE ueid = ? ORDER BY timestamp DESC LIMIT 10",
services/ms_jarvis_ueid_system.py:232:    c.execute("""INSERT INTO interaction_log (ueid, timestamp, interaction_type, location_data, service)
services/ms_jarvis_ueid_system.py:237:    c.execute("UPDATE ueid_registry SET total_interactions = total_interactions + 1 WHERE ueid = ?", (ueid,))
services/ms_jarvis_ueid_system.py:250:    c.execute("SELECT COUNT(*) FROM ueid_registry")
services/ms_jarvis_ueid_system.py:253:    c.execute("SELECT COUNT(*) FROM ueid_registry WHERE mountainshares_linked = 1")
services/ms_jarvis_ueid_system.py:256:    c.execute("SELECT SUM(total_interactions) FROM ueid_registry")
services/ms_jarvis_ueid_system.py:280:    c.execute("SELECT ueid FROM ueid_registry WHERE ueid = ?", (ueid,))
services/ms_jarvis_ueid_system.py:310:    c.execute("""INSERT INTO messages (conversation_id, ueid, timestamp, message, response)
services/ms_jarvis_ueid_system.py:359:    c.execute("""SELECT timestamp, message, response 
services/academic_research_gateway_8062_cors.py:51:            "SELECT timestamp FROM ms_jarvis_learning_log WHERE learning_action = 'consciousness' ORDER BY id DESC LIMIT 1")
services/academic_research_gateway_8062_cors.py:113:            f"SELECT id, timestamp, learning_action FROM ms_jarvis_learning_log ORDER BY id DESC LIMIT {
services/academic_research_gateway_8062_cors.py:132:            "SELECT timestamp, learning_action FROM ms_jarvis_learning_log ORDER BY id DESC LIMIT 5")
services/set_intelligent_accuracy_scores.py:49:    UPDATE geographic_knowledge 
services/mountainshares_gbim_suggester.py:50:                FROM gbimbeliefnormalized
services/port_9001_ui_WITH_CONVERSATIONS.py:235:            INSERT INTO conversations (userid, message, response, timestamp)
services/port_9001_ui_WITH_CONVERSATIONS.py:250:        cursor.execute('SELECT message, response, timestamp FROM conversations ORDER BY id DESC LIMIT 50')
services/port_9001_ui_WITH_CONVERSATIONS.py:269:        cursor.execute('SELECT userid, message, response, timestamp FROM conversations ORDER BY id')
services/jarvisarchiveapi.py:37:        sql = "SELECT county, state, lat, lon FROM gisgeodata WHERE UPPER(location) LIKE UPPER(?) LIMIT 1"
services/jarvisarchiveapi.py:61:        rows = conn.execute("SELECT COUNT(*) FROM gisgeodata").fetchone()[0]
services/ms_jarvis_unified_gateway_v4.3.py.original:46:            rows = conn.execute("SELECT COUNT(*) FROM gisgeodata").fetchone()[0] or 1002
services/ms_jarvis_unified_gateway_v4.3.py.original:161:            "SELECT county, state, lat, lon, description FROM gisgeodata WHERE UPPER(location) LIKE UPPER(?) LIMIT 1",
services/knowledge_docs_metadata.csv:549:,"<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->",README.md,lat; map; tract,Installation; The idea; TypeScript compatibility; Error reporters; Custom error messages,,md
services/knowledge_docs_metadata.csv:602:"THE SOFTWARE IS PROVIDED ""AS IS"" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.",,LICENSE.md,tract,"THE SOFTWARE IS PROVIDED ""AS IS"" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.",,md
services/ms_jarvis_unified_gateway_v4.3.py.pre_dynamic_discovery:34:        cursor.execute("SELECT COUNT(*) FROM gisgeodata;")
services/port_9001_ui_MYSQL.py:211:            INSERT INTO conversations (userid, message, response, timestamp)
services/port_9001_ui_MYSQL.py:226:        cursor.execute('SELECT message, response, timestamp FROM conversations ORDER BY id DESC LIMIT 50')
services/port_9001_ui_MYSQL.py:245:        cursor.execute('SELECT userid, message, response, timestamp FROM conversations ORDER BY id')
services/bulk_sync_gis_to_chromadb.py:44:                "SELECT column_name FROM information_schema.columns WHERE table_schema = %s AND table_name = %s",
services/bulk_sync_gis_to_chromadb.py:115:                    SELECT id, name, description
services/geobim_integrated.py.running_backup:14:            ["sudo", "mysql", "gisgeodbactive", "-e", "SELECT COUNT(*) FROM gisgeodata;"],
services/user_dashboard.py:20:        cursor.execute('SELECT metadata FROM ueid_registry WHERE ueid = ?', (ueid,))
services/registration_biometric_production_final.py:623:    c.execute("SELECT ueid FROM identity_hashes WHERE name_dob_hash = ?", (name_dob_hash,))
services/registration_biometric_production_final.py:637:    c.execute("INSERT INTO users_identity_vault VALUES (?, ?, ?, ?, ?)",
services/registration_biometric_production_final.py:642:    c.execute("INSERT INTO identity_hashes VALUES (?, ?, ?, ?)", (ueid, name_dob_hash, dl_hash, email_hash))
services/registration_biometric_production_final.py:646:    c.execute("INSERT INTO registration_tokens VALUES (?, ?, ?, ?, ?)", (token, ueid, form.email, expires, 0))
services/registration_biometric_production_final.py:660:    c.execute("SELECT ueid, email FROM registration_tokens WHERE token = ? AND ueid = ? AND used = 0", (form.token, form.ueid))
services/registration_biometric_production_final.py:668:    c.execute("SELECT encrypted_identity_blob FROM users_identity_vault WHERE ueid = ?", (form.ueid,))
services/registration_biometric_production_final.py:690:    c.execute("INSERT INTO user_biometrics VALUES (?, ?, ?, ?)",
services/registration_biometric_production_final.py:700:    c.execute("INSERT INTO users_public_profiles VALUES (?, ?, ?, ?, ?)",
services/registration_biometric_production_final.py:702:    c.execute("UPDATE registration_tokens SET used = 1 WHERE token = ?", (form.token,))
services/ms_jarvis_ueid_wallet_integration.py:117:    c.execute("SELECT ueid, wallet_address FROM ueid_registry WHERE ueid = ?", (ueid,))
services/ms_jarvis_ueid_wallet_integration.py:137:    c.execute("""INSERT INTO ueid_registry 
services/ms_jarvis_ueid_wallet_integration.py:165:    c.execute("SELECT wallet_address, mountainshares_balance, keystore_file FROM ueid_registry WHERE ueid = ?", (ueid,))
services/ms_jarvis_ueid_wallet_integration.py:186:    c.execute("""INSERT INTO transactions (ueid, tx_hash, timestamp, transaction_type, amount, status)
services/ADD_ALL_INTEGRATIONS.sh:26:    # 🧠 RETRIEVE RELEVANT MEMORIES FROM RAG
services/jarvis_steward.py:128:                    """SELECT id, entity_type, label, belief_state
services/jarvis_steward.py:129:                       FROM public.gbim_worldview_entity
services/jarvis_steward.py:146:                       FROM public.local_resources_index
services/stage2_biometric_backup.py:66:        c.execute("SELECT email FROM registration_tokens WHERE token = ? AND ueid = ? AND used = 0",
services/stage2_biometric_backup.py:106:        c.execute("UPDATE registration_tokens SET used = 1 WHERE token = ?", (token,))
services/create_dual_consciousness_i_containers.py:222:    core_count = c.execute("SELECT COUNT(*) FROM central_i_container WHERE part_of_core_identity = TRUE").fetchone()[0]
services/create_dual_consciousness_i_containers.py:231:    print("   SQL: SELECT * FROM v_ms_jarvis_core_identity")
services/create_dual_consciousness_i_containers.py:234:    results = c.execute("SELECT identity_element, integration_confidence FROM v_ms_jarvis_core_identity").fetchall()
services/migrate_gis2chroma.py:11:cursor.execute("SELECT id, location, county, state, lat, lon, description FROM gisgeodata")
services/registration_service_clean.py:170:    c.execute("SELECT ueid FROM identity_hashes WHERE name_dob_hash = ?", (name_dob_hash,))
services/registration_service_clean.py:190:    c.execute("""INSERT INTO identity_hashes 
services/sync_health_access_to_chromadb.py:51:        SELECT block_id, geographic, pop2020, provider_count
services/academic_whitebox_api.py:23:        cursor.execute("SELECT timestamp, learning_action FROM ms_jarvis_learning_log WHERE learning_action = 'consciousness' ORDER BY id DESC LIMIT 10")
services/academic_whitebox_api.py:35:        cursor.execute(f"SELECT id, timestamp, learning_action FROM ms_jarvis_learning_log ORDER BY id DESC LIMIT {min(limit, 500)}")
services/academic_whitebox_api.py:47:        cursor.execute("SELECT timestamp, learning_action FROM ms_jarvis_learning_log ORDER BY id DESC LIMIT 5")
services/extract_real_knowledge_to_gis.py:25:    logger.info("📚 EXTRACTING REAL KNOWLEDGE FROM CHROMADB")
services/extract_real_knowledge_to_gis.py:37:            SELECT * FROM embeddings
services/ADD_RAG_RETRIEVAL_8050.sh:21:    # 🧠 RETRIEVE RELEVANT MEMORIES FROM RAG
services/ms_jarvis_layer2_dgm.psychology_patched.py:101:            c.execute("UPDATE user_conversations SET analyzed=1, sentiment_score=?, emotion_detected=?, topics_detected=?, needs_detected=?, analyzed_at=? WHERE id=?",
services/chroma_inspect_venv/lib/python3.12/site-packages/onnxruntime/ThirdPartyNotices.txt:65:AND EXPENSES RESULTING FROM YOUR USE OR UNAUTHORIZED USE OF THE SOFTWARE.
services/chroma_inspect_venv/lib/python3.12/site-packages/chromadb/db/impl/sqlite.py:270:            INSERT INTO maintenance_log (operation, timestamp)
services/chroma_inspect_venv/lib/python3.12/site-packages/chromadb/migrations/metadb/00003-full-text-tokenize.sqlite.sql:2:INSERT INTO embedding_fulltext_search (rowid, string_value) SELECT rowid, string_value FROM embedding_metadata;
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:134:    SELECT id,fname,lname,phone FROM customers
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:145:    SELECT id,phone FROM x_view_customers customers
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:158:    SELECT id,phone FROM views.customers
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:171:    SELECT id,phone FROM my_db.analytics.customers
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:185:    SELECT "id","fname","lname","phone" FROM "customers" ORDER BY "id" DESC
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:203:    SELECT revenue-cost FROM accounts
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:216:    SELECT revenue-cost FROM accounts
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:228:    SELECT revenue-cost profit FROM accounts
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:245:    SELECT foo+bar,foo-bar,foo*bar,foo/bar,(foo+bar)/fiz FROM table
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:257:    SELECT "name" FROM "flags" WHERE ("permissions" & 4)=4
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:265:    SELECT "name" FROM "flags" WHERE ("permissions" | 2)=3
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:284:    SELECT id,fname,lname,phone FROM customers WHERE lname='Mustermann'
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:302:    SELECT id,fname,lname,phone FROM customers WHERE fname='Max' AND lname='Mustermann'
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:317:    SELECT id,fname FROM customers WHERE age BETWEEN 18 AND 65 AND status IN ('new','active')
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:334:    SELECT id,fname,lname,phone FROM customers WHERE age>=18 AND lname='Mustermann'
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:349:    SELECT id,fname,lname,phone FROM customers WHERE age>=18 OR lname='Mustermann'
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:364:    SELECT id,fname,lname,phone FROM customers WHERE age>=18 XOR is_registered
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:390:    SELECT id,fname FROM customers WHERE is_registered AND age>=18 AND lname = "Jones"
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:411:    SELECT id,SUM("revenue") FROM "customers" WHERE "age">=18 GROUP BY "id"
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:430:    SELECT customer_id,SUM(total) FROM payments
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:448:    SELECT * FROM "events" QUALIFY RANK() OVER(PARTITION BY "user_id" ORDER BY "created_at")=1
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:466:    SELECT "id","category",SUM("price") FROM "products" GROUP BY ROLLUP("id","category")
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:526:    SELECT "history".* FROM "history" JOIN "customers" ON "history"."customer_id"="customers"."id" WHERE "customers"."id"=5
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:547:    SELECT "history".* FROM "history" JOIN "customers" ON "history"."customer_id"="customers"."customer_id" AND "history"."group"="customers"."group" WHERE "customers"."group"='A'
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:566:    SELECT "history".* FROM "history" JOIN "customers" USING "customer_id" WHERE "customers"."id"=5
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:589:      (SELECT "history"."purchase_at"
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:590:       FROM "history"
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:594:    FROM "customers"
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:618:    SELECT "created_time","foo","bar" FROM "provider_a" UNION SELECT "created_time","fiz","buz" FROM "provider_b"
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:641:    SELECT "created_time","foo","bar" FROM "provider_a" INTERSECT SELECT "created_time","fiz","buz" FROM "provider_b"
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:672:    SELECT "created_time","foo","bar" FROM "provider_a" MINUS SELECT "created_time","fiz","buz" FROM "provider_b"
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:695:    SELECT "created_time","foo","bar" FROM "provider_a" EXCEPT SELECT "created_time","fiz","buz" FROM "provider_b"
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:714:    SELECT id,name FROM fruits WHERE harvest_date+INTERVAL 1 MONTH<NOW()
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:733:    SELECT "foo","bar" FROM "abc" WHERE ("foo","bar")=(1,2)
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:747:    SELECT "foo","bar" FROM "abc" WHERE ("foo","bar")=(1,2)
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:759:    SELECT "foo","bar" FROM "abc" WHERE ("foo","bar") IN ((1,1),(2,2),(3,3))
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:783:    SELECT id,fname,lname FROM customers WHERE lname LIKE 'Mc%'
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:800:    SELECT id,fname,lname FROM customers WHERE lname REGEX '^[abc][a-zA-Z]+&';
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:815:    SELECT id,CONCAT(fname, ' ', lname) full_name FROM customers
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:840:    SELECT id,fname,lname,DATE_DIFF('day',created_date,updated_date) FROM customers
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:866:    SELECT "id",CASE WHEN "fname"='Tom' THEN 'It was Tom' WHEN "fname"='John' THEN 'It was John' ELSE 'It was someone else.' END "who_was_it" FROM "customers"
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:885:    SELECT current_date FROM "products"
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:913:    WITH an_alias AS (SELECT * FROM "customers") SELECT * FROM an_alias
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:934:    INSERT INTO customers VALUES (1,'Jane','Doe','jane@example.com')
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:944:    INSERT INTO customers VALUES (1,'Jane','Doe','jane@example.com')
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1008:    INSERT INTO "customers" VALUES (1,'Jane','Doe','jane@example.com') ON CONFLICT ("email") DO NOTHING
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1021:    INSERT INTO "customers" VALUES (1,'Jane','Doe','jane@example.com') ON CONFLICT ("email") DO UPDATE SET "email"='bob@example.com'
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1024:Insert from a SELECT Sub-query
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1029:    INSERT INTO "customers" VALUES (1,'Jane','Doe','jane@example.com'),(2,'John','Doe','john@example.com')
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1042:    INSERT INTO customers (id,fname,lname) VALUES (1,'Jane','Doe','jane@example.com')
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1056:    INSERT INTO customers_backup SELECT * FROM customers
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1067:    INSERT INTO customers_backup SELECT "id", "fname", "lname" FROM customers
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1082:   INSERT INTO "orders_backup" ("id","address","customer_fname","customer_lname")
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1083:   SELECT "orders"."id","customers"."fname","customers"."lname" FROM "customers"
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1084:   JOIN "orders" ON "orders"."customer_id"="customers"."id"
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1100:    UPDATE "customers" SET "last_login"='2017-01-01 10:00:00'
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1102:    UPDATE "customers" SET "lname"='smith' WHERE "id"=10
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1116:   UPDATE "customers"
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1117:   JOIN "profiles" ON "profiles"."customer_id"="customers"."id"
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1132:    UPDATE "customers" SET "lname"='smith' WHERE "id"=10
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1146:    UPDATE "customers" SET "lname"='smith' LIMIT 2
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1189:    SELECT FIRST_VALUE("value") OVER(PARTITION BY "category" ORDER BY "month"),LAST_VALUE("value" IGNORE NULLS) OVER(PARTITION BY "category" ORDER BY "month") FROM "monthly_data"
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1224:    SELECT "date","amount",SUM("amount") OVER(PARTITION BY "account_id" ORDER BY "date" ROWS BETWEEN 7 PRECEDING AND CURRENT ROW) "rolling_7_day" FROM "transactions"
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1241:    INSERT INTO customers (id,fname,lname) VALUES (:1,:2,:3)
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1285:    # sql: SELECT * FROM "customers" WHERE "status"=? AND "age">=?
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1301:    # sql: SELECT * FROM "customers" WHERE "status"=:param1
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1323:    SELECT * FROM "abc" FOR SYSTEM_TIME AS OF '2020-01-01'
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1338:    SELECT * FROM "abc" FOR SYSTEM_TIME BETWEEN '2020-01-01' AND '2020-02-01'
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1353:    SELECT * FROM "abc" FOR SYSTEM_TIME FROM '2020-01-01' TO '2020-02-01'
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1366:    SELECT * FROM "abc" FOR SYSTEM_TIME ALL
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1381:    SELECT * FROM "abc" FOR "valid_period" BETWEEN '2020-01-01' AND '2020-02-01'
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1406:    SELECT * FROM "abc" FOR SYSTEM_TIME AS OF '2020-01-01'
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1407:    JOIN "efg" FOR SYSTEM_TIME AS OF '2020-01-01'
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1428:    UPDATE "abc"
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1445:    DELETE FROM "abc"
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1497:        CREATE TABLE "names" AS (SELECT "last_name","first_name" FROM "person")
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1645:    SELECT "user_id","event" FROM "events" FINAL
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1661:    SELECT "user_id" FROM "events" SAMPLE 10
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1671:    SELECT "user_id" FROM "events" SAMPLE 10 OFFSET 5
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1687:    SELECT DISTINCT ON("department","role") "name","department","role" FROM "users"
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1703:    SELECT "user_id","event","timestamp" FROM "events" LIMIT 3 BY ("user_id")
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1713:    SELECT "user_id","event" FROM "events" LIMIT 3 OFFSET 1 BY ("user_id")
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1733:    SELECT name FROM employees FETCH NEXT 10 ROWS ONLY
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1743:    SELECT name FROM employees OFFSET 20 ROWS FETCH NEXT 10 ROWS ONLY
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1816:    SELECT "col1","col2",COUNT(*) n_rows 
services/chroma_inspect_venv/lib/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1817:    FROM "table" 
services/chroma_inspect_venv/lib/python3.12/site-packages/kubernetes/client/models/v1_validation_rule.py:198:        Rule represents the expression which will be evaluated by CEL. ref: https://github.com/google/cel-spec The Rule is scoped to the location of the x-kubernetes-validations extension in the schema. The `self` variable in the CEL expression is bound to the scoped value. Example: - Rule scoped to the root of a resource with a status subresource: {\"rule\": \"self.status.actual <= self.spec.maxDesired\"}  If the Rule is scoped to an object with properties, the accessible properties of the object are field selectable via `self.field` and field presence can be checked via `has(self.field)`. Null valued fields are treated as absent fields in CEL expressions. If the Rule is scoped to an object with additionalProperties (i.e. a map) the value of the map are accessible via `self[mapKey]`, map containment can be checked via `mapKey in self` and all entries of the map are accessible via CEL macros and functions such as `self.all(...)`. If the Rule is scoped to an array, the elements of the array are accessible via `self[i]` and also by macros and functions. If the Rule is scoped to a scalar, `self` is bound to the scalar value. Examples: - Rule scoped to a map of objects: {\"rule\": \"self.components['Widget'].priority < 10\"} - Rule scoped to a list of integers: {\"rule\": \"self.values.all(value, value >= 0 && value < 100)\"} - Rule scoped to a string value: {\"rule\": \"self.startsWith('kube')\"}  The `apiVersion`, `kind`, `metadata.name` and `metadata.generateName` are always accessible from the root of the object and from any x-kubernetes-embedded-resource annotated objects. No other metadata properties are accessible.  Unknown data preserved in custom resources via x-kubernetes-preserve-unknown-fields is not accessible in CEL expressions. This includes: - Unknown field values that are preserved by object schemas with x-kubernetes-preserve-unknown-fields. - Object properties where the property schema is of an \"unknown type\". An \"unknown type\" is recursively defined as:   - A schema with no type and x-kubernetes-preserve-unknown-fields set to true   - An array where the items schema is of an \"unknown type\"   - An object where the additionalProperties schema is of an \"unknown type\"  Only property names of the form `[a-zA-Z_.-/][a-zA-Z0-9_.-/]*` are accessible. Accessible property names are escaped according to the following rules when accessed in the expression: - '__' escapes to '__underscores__' - '.' escapes to '__dot__' - '-' escapes to '__dash__' - '/' escapes to '__slash__' - Property names that exactly match a CEL RESERVED keyword escape to '__{keyword}__'. The keywords are:    \"true\", \"false\", \"null\", \"in\", \"as\", \"break\", \"const\", \"continue\", \"else\", \"for\", \"function\", \"if\",    \"import\", \"let\", \"loop\", \"package\", \"namespace\", \"return\". Examples:   - Rule accessing a property named \"namespace\": {\"rule\": \"self.__namespace__ > 0\"}   - Rule accessing a property named \"x-prop\": {\"rule\": \"self.x__dash__prop > 0\"}   - Rule accessing a property named \"redact__d\": {\"rule\": \"self.redact__underscores__d > 0\"}  Equality on arrays with x-kubernetes-list-type of 'set' or 'map' ignores element order, i.e. [1, 2] == [2, 1]. Concatenation on arrays with x-kubernetes-list-type use the semantics of the list type:   - 'set': `X + Y` performs a union where the array positions of all elements in `X` are preserved and     non-intersecting elements in `Y` are appended, retaining their partial order.   - 'map': `X + Y` performs a merge where the array positions of all keys in `X` are preserved but the values     are overwritten by values in `Y` when the key sets of `X` and `Y` intersect. Elements in `Y` with     non-intersecting keys are appended, retaining their partial order.  If `rule` makes use of the `oldSelf` variable it is implicitly a `transition rule`.  By default, the `oldSelf` variable is the same type as `self`. When `optionalOldSelf` is true, the `oldSelf` variable is a CEL optional  variable whose value() is the same type as `self`. See the documentation for the `optionalOldSelf` field for details.  Transition rules by default are applied only on UPDATE requests and are skipped if an old value could not be found. You can opt a transition rule into unconditional evaluation by setting `optionalOldSelf` to true.  # noqa: E501
services/chroma_inspect_venv/lib/python3.12/site-packages/kubernetes/client/models/v1_validation_rule.py:209:        Rule represents the expression which will be evaluated by CEL. ref: https://github.com/google/cel-spec The Rule is scoped to the location of the x-kubernetes-validations extension in the schema. The `self` variable in the CEL expression is bound to the scoped value. Example: - Rule scoped to the root of a resource with a status subresource: {\"rule\": \"self.status.actual <= self.spec.maxDesired\"}  If the Rule is scoped to an object with properties, the accessible properties of the object are field selectable via `self.field` and field presence can be checked via `has(self.field)`. Null valued fields are treated as absent fields in CEL expressions. If the Rule is scoped to an object with additionalProperties (i.e. a map) the value of the map are accessible via `self[mapKey]`, map containment can be checked via `mapKey in self` and all entries of the map are accessible via CEL macros and functions such as `self.all(...)`. If the Rule is scoped to an array, the elements of the array are accessible via `self[i]` and also by macros and functions. If the Rule is scoped to a scalar, `self` is bound to the scalar value. Examples: - Rule scoped to a map of objects: {\"rule\": \"self.components['Widget'].priority < 10\"} - Rule scoped to a list of integers: {\"rule\": \"self.values.all(value, value >= 0 && value < 100)\"} - Rule scoped to a string value: {\"rule\": \"self.startsWith('kube')\"}  The `apiVersion`, `kind`, `metadata.name` and `metadata.generateName` are always accessible from the root of the object and from any x-kubernetes-embedded-resource annotated objects. No other metadata properties are accessible.  Unknown data preserved in custom resources via x-kubernetes-preserve-unknown-fields is not accessible in CEL expressions. This includes: - Unknown field values that are preserved by object schemas with x-kubernetes-preserve-unknown-fields. - Object properties where the property schema is of an \"unknown type\". An \"unknown type\" is recursively defined as:   - A schema with no type and x-kubernetes-preserve-unknown-fields set to true   - An array where the items schema is of an \"unknown type\"   - An object where the additionalProperties schema is of an \"unknown type\"  Only property names of the form `[a-zA-Z_.-/][a-zA-Z0-9_.-/]*` are accessible. Accessible property names are escaped according to the following rules when accessed in the expression: - '__' escapes to '__underscores__' - '.' escapes to '__dot__' - '-' escapes to '__dash__' - '/' escapes to '__slash__' - Property names that exactly match a CEL RESERVED keyword escape to '__{keyword}__'. The keywords are:    \"true\", \"false\", \"null\", \"in\", \"as\", \"break\", \"const\", \"continue\", \"else\", \"for\", \"function\", \"if\",    \"import\", \"let\", \"loop\", \"package\", \"namespace\", \"return\". Examples:   - Rule accessing a property named \"namespace\": {\"rule\": \"self.__namespace__ > 0\"}   - Rule accessing a property named \"x-prop\": {\"rule\": \"self.x__dash__prop > 0\"}   - Rule accessing a property named \"redact__d\": {\"rule\": \"self.redact__underscores__d > 0\"}  Equality on arrays with x-kubernetes-list-type of 'set' or 'map' ignores element order, i.e. [1, 2] == [2, 1]. Concatenation on arrays with x-kubernetes-list-type use the semantics of the list type:   - 'set': `X + Y` performs a union where the array positions of all elements in `X` are preserved and     non-intersecting elements in `Y` are appended, retaining their partial order.   - 'map': `X + Y` performs a merge where the array positions of all keys in `X` are preserved but the values     are overwritten by values in `Y` when the key sets of `X` and `Y` intersect. Elements in `Y` with     non-intersecting keys are appended, retaining their partial order.  If `rule` makes use of the `oldSelf` variable it is implicitly a `transition rule`.  By default, the `oldSelf` variable is the same type as `self`. When `optionalOldSelf` is true, the `oldSelf` variable is a CEL optional  variable whose value() is the same type as `self`. See the documentation for the `optionalOldSelf` field for details.  Transition rules by default are applied only on UPDATE requests and are skipped if an old value could not be found. You can opt a transition rule into unconditional evaluation by setting `optionalOldSelf` to true.  # noqa: E501
services/chroma_inspect_venv/lib64/python3.12/site-packages/onnxruntime/ThirdPartyNotices.txt:65:AND EXPENSES RESULTING FROM YOUR USE OR UNAUTHORIZED USE OF THE SOFTWARE.
services/chroma_inspect_venv/lib64/python3.12/site-packages/chromadb/db/impl/sqlite.py:270:            INSERT INTO maintenance_log (operation, timestamp)
services/chroma_inspect_venv/lib64/python3.12/site-packages/chromadb/migrations/metadb/00003-full-text-tokenize.sqlite.sql:2:INSERT INTO embedding_fulltext_search (rowid, string_value) SELECT rowid, string_value FROM embedding_metadata;
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:134:    SELECT id,fname,lname,phone FROM customers
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:145:    SELECT id,phone FROM x_view_customers customers
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:158:    SELECT id,phone FROM views.customers
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:171:    SELECT id,phone FROM my_db.analytics.customers
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:185:    SELECT "id","fname","lname","phone" FROM "customers" ORDER BY "id" DESC
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:203:    SELECT revenue-cost FROM accounts
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:216:    SELECT revenue-cost FROM accounts
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:228:    SELECT revenue-cost profit FROM accounts
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:245:    SELECT foo+bar,foo-bar,foo*bar,foo/bar,(foo+bar)/fiz FROM table
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:257:    SELECT "name" FROM "flags" WHERE ("permissions" & 4)=4
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:265:    SELECT "name" FROM "flags" WHERE ("permissions" | 2)=3
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:284:    SELECT id,fname,lname,phone FROM customers WHERE lname='Mustermann'
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:302:    SELECT id,fname,lname,phone FROM customers WHERE fname='Max' AND lname='Mustermann'
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:317:    SELECT id,fname FROM customers WHERE age BETWEEN 18 AND 65 AND status IN ('new','active')
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:334:    SELECT id,fname,lname,phone FROM customers WHERE age>=18 AND lname='Mustermann'
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:349:    SELECT id,fname,lname,phone FROM customers WHERE age>=18 OR lname='Mustermann'
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:364:    SELECT id,fname,lname,phone FROM customers WHERE age>=18 XOR is_registered
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:390:    SELECT id,fname FROM customers WHERE is_registered AND age>=18 AND lname = "Jones"
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:411:    SELECT id,SUM("revenue") FROM "customers" WHERE "age">=18 GROUP BY "id"
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:430:    SELECT customer_id,SUM(total) FROM payments
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:448:    SELECT * FROM "events" QUALIFY RANK() OVER(PARTITION BY "user_id" ORDER BY "created_at")=1
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:466:    SELECT "id","category",SUM("price") FROM "products" GROUP BY ROLLUP("id","category")
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:526:    SELECT "history".* FROM "history" JOIN "customers" ON "history"."customer_id"="customers"."id" WHERE "customers"."id"=5
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:547:    SELECT "history".* FROM "history" JOIN "customers" ON "history"."customer_id"="customers"."customer_id" AND "history"."group"="customers"."group" WHERE "customers"."group"='A'
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:566:    SELECT "history".* FROM "history" JOIN "customers" USING "customer_id" WHERE "customers"."id"=5
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:589:      (SELECT "history"."purchase_at"
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:590:       FROM "history"
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:594:    FROM "customers"
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:618:    SELECT "created_time","foo","bar" FROM "provider_a" UNION SELECT "created_time","fiz","buz" FROM "provider_b"
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:641:    SELECT "created_time","foo","bar" FROM "provider_a" INTERSECT SELECT "created_time","fiz","buz" FROM "provider_b"
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:672:    SELECT "created_time","foo","bar" FROM "provider_a" MINUS SELECT "created_time","fiz","buz" FROM "provider_b"
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:695:    SELECT "created_time","foo","bar" FROM "provider_a" EXCEPT SELECT "created_time","fiz","buz" FROM "provider_b"
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:714:    SELECT id,name FROM fruits WHERE harvest_date+INTERVAL 1 MONTH<NOW()
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:733:    SELECT "foo","bar" FROM "abc" WHERE ("foo","bar")=(1,2)
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:747:    SELECT "foo","bar" FROM "abc" WHERE ("foo","bar")=(1,2)
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:759:    SELECT "foo","bar" FROM "abc" WHERE ("foo","bar") IN ((1,1),(2,2),(3,3))
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:783:    SELECT id,fname,lname FROM customers WHERE lname LIKE 'Mc%'
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:800:    SELECT id,fname,lname FROM customers WHERE lname REGEX '^[abc][a-zA-Z]+&';
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:815:    SELECT id,CONCAT(fname, ' ', lname) full_name FROM customers
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:840:    SELECT id,fname,lname,DATE_DIFF('day',created_date,updated_date) FROM customers
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:866:    SELECT "id",CASE WHEN "fname"='Tom' THEN 'It was Tom' WHEN "fname"='John' THEN 'It was John' ELSE 'It was someone else.' END "who_was_it" FROM "customers"
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:885:    SELECT current_date FROM "products"
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:913:    WITH an_alias AS (SELECT * FROM "customers") SELECT * FROM an_alias
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:934:    INSERT INTO customers VALUES (1,'Jane','Doe','jane@example.com')
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:944:    INSERT INTO customers VALUES (1,'Jane','Doe','jane@example.com')
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1008:    INSERT INTO "customers" VALUES (1,'Jane','Doe','jane@example.com') ON CONFLICT ("email") DO NOTHING
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1021:    INSERT INTO "customers" VALUES (1,'Jane','Doe','jane@example.com') ON CONFLICT ("email") DO UPDATE SET "email"='bob@example.com'
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1024:Insert from a SELECT Sub-query
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1029:    INSERT INTO "customers" VALUES (1,'Jane','Doe','jane@example.com'),(2,'John','Doe','john@example.com')
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1042:    INSERT INTO customers (id,fname,lname) VALUES (1,'Jane','Doe','jane@example.com')
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1056:    INSERT INTO customers_backup SELECT * FROM customers
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1067:    INSERT INTO customers_backup SELECT "id", "fname", "lname" FROM customers
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1082:   INSERT INTO "orders_backup" ("id","address","customer_fname","customer_lname")
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1083:   SELECT "orders"."id","customers"."fname","customers"."lname" FROM "customers"
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1084:   JOIN "orders" ON "orders"."customer_id"="customers"."id"
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1100:    UPDATE "customers" SET "last_login"='2017-01-01 10:00:00'
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1102:    UPDATE "customers" SET "lname"='smith' WHERE "id"=10
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1116:   UPDATE "customers"
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1117:   JOIN "profiles" ON "profiles"."customer_id"="customers"."id"
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1132:    UPDATE "customers" SET "lname"='smith' WHERE "id"=10
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1146:    UPDATE "customers" SET "lname"='smith' LIMIT 2
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1189:    SELECT FIRST_VALUE("value") OVER(PARTITION BY "category" ORDER BY "month"),LAST_VALUE("value" IGNORE NULLS) OVER(PARTITION BY "category" ORDER BY "month") FROM "monthly_data"
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1224:    SELECT "date","amount",SUM("amount") OVER(PARTITION BY "account_id" ORDER BY "date" ROWS BETWEEN 7 PRECEDING AND CURRENT ROW) "rolling_7_day" FROM "transactions"
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1241:    INSERT INTO customers (id,fname,lname) VALUES (:1,:2,:3)
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1285:    # sql: SELECT * FROM "customers" WHERE "status"=? AND "age">=?
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1301:    # sql: SELECT * FROM "customers" WHERE "status"=:param1
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1323:    SELECT * FROM "abc" FOR SYSTEM_TIME AS OF '2020-01-01'
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1338:    SELECT * FROM "abc" FOR SYSTEM_TIME BETWEEN '2020-01-01' AND '2020-02-01'
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1353:    SELECT * FROM "abc" FOR SYSTEM_TIME FROM '2020-01-01' TO '2020-02-01'
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1366:    SELECT * FROM "abc" FOR SYSTEM_TIME ALL
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1381:    SELECT * FROM "abc" FOR "valid_period" BETWEEN '2020-01-01' AND '2020-02-01'
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1406:    SELECT * FROM "abc" FOR SYSTEM_TIME AS OF '2020-01-01'
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1407:    JOIN "efg" FOR SYSTEM_TIME AS OF '2020-01-01'
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1428:    UPDATE "abc"
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1445:    DELETE FROM "abc"
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1497:        CREATE TABLE "names" AS (SELECT "last_name","first_name" FROM "person")
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1645:    SELECT "user_id","event" FROM "events" FINAL
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1661:    SELECT "user_id" FROM "events" SAMPLE 10
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1671:    SELECT "user_id" FROM "events" SAMPLE 10 OFFSET 5
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1687:    SELECT DISTINCT ON("department","role") "name","department","role" FROM "users"
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1703:    SELECT "user_id","event","timestamp" FROM "events" LIMIT 3 BY ("user_id")
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1713:    SELECT "user_id","event" FROM "events" LIMIT 3 OFFSET 1 BY ("user_id")
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1733:    SELECT name FROM employees FETCH NEXT 10 ROWS ONLY
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1743:    SELECT name FROM employees OFFSET 20 ROWS FETCH NEXT 10 ROWS ONLY
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1816:    SELECT "col1","col2",COUNT(*) n_rows 
services/chroma_inspect_venv/lib64/python3.12/site-packages/pypika-0.51.1.dist-info/METADATA:1817:    FROM "table" 
services/chroma_inspect_venv/lib64/python3.12/site-packages/kubernetes/client/models/v1_validation_rule.py:198:        Rule represents the expression which will be evaluated by CEL. ref: https://github.com/google/cel-spec The Rule is scoped to the location of the x-kubernetes-validations extension in the schema. The `self` variable in the CEL expression is bound to the scoped value. Example: - Rule scoped to the root of a resource with a status subresource: {\"rule\": \"self.status.actual <= self.spec.maxDesired\"}  If the Rule is scoped to an object with properties, the accessible properties of the object are field selectable via `self.field` and field presence can be checked via `has(self.field)`. Null valued fields are treated as absent fields in CEL expressions. If the Rule is scoped to an object with additionalProperties (i.e. a map) the value of the map are accessible via `self[mapKey]`, map containment can be checked via `mapKey in self` and all entries of the map are accessible via CEL macros and functions such as `self.all(...)`. If the Rule is scoped to an array, the elements of the array are accessible via `self[i]` and also by macros and functions. If the Rule is scoped to a scalar, `self` is bound to the scalar value. Examples: - Rule scoped to a map of objects: {\"rule\": \"self.components['Widget'].priority < 10\"} - Rule scoped to a list of integers: {\"rule\": \"self.values.all(value, value >= 0 && value < 100)\"} - Rule scoped to a string value: {\"rule\": \"self.startsWith('kube')\"}  The `apiVersion`, `kind`, `metadata.name` and `metadata.generateName` are always accessible from the root of the object and from any x-kubernetes-embedded-resource annotated objects. No other metadata properties are accessible.  Unknown data preserved in custom resources via x-kubernetes-preserve-unknown-fields is not accessible in CEL expressions. This includes: - Unknown field values that are preserved by object schemas with x-kubernetes-preserve-unknown-fields. - Object properties where the property schema is of an \"unknown type\". An \"unknown type\" is recursively defined as:   - A schema with no type and x-kubernetes-preserve-unknown-fields set to true   - An array where the items schema is of an \"unknown type\"   - An object where the additionalProperties schema is of an \"unknown type\"  Only property names of the form `[a-zA-Z_.-/][a-zA-Z0-9_.-/]*` are accessible. Accessible property names are escaped according to the following rules when accessed in the expression: - '__' escapes to '__underscores__' - '.' escapes to '__dot__' - '-' escapes to '__dash__' - '/' escapes to '__slash__' - Property names that exactly match a CEL RESERVED keyword escape to '__{keyword}__'. The keywords are:    \"true\", \"false\", \"null\", \"in\", \"as\", \"break\", \"const\", \"continue\", \"else\", \"for\", \"function\", \"if\",    \"import\", \"let\", \"loop\", \"package\", \"namespace\", \"return\". Examples:   - Rule accessing a property named \"namespace\": {\"rule\": \"self.__namespace__ > 0\"}   - Rule accessing a property named \"x-prop\": {\"rule\": \"self.x__dash__prop > 0\"}   - Rule accessing a property named \"redact__d\": {\"rule\": \"self.redact__underscores__d > 0\"}  Equality on arrays with x-kubernetes-list-type of 'set' or 'map' ignores element order, i.e. [1, 2] == [2, 1]. Concatenation on arrays with x-kubernetes-list-type use the semantics of the list type:   - 'set': `X + Y` performs a union where the array positions of all elements in `X` are preserved and     non-intersecting elements in `Y` are appended, retaining their partial order.   - 'map': `X + Y` performs a merge where the array positions of all keys in `X` are preserved but the values     are overwritten by values in `Y` when the key sets of `X` and `Y` intersect. Elements in `Y` with     non-intersecting keys are appended, retaining their partial order.  If `rule` makes use of the `oldSelf` variable it is implicitly a `transition rule`.  By default, the `oldSelf` variable is the same type as `self`. When `optionalOldSelf` is true, the `oldSelf` variable is a CEL optional  variable whose value() is the same type as `self`. See the documentation for the `optionalOldSelf` field for details.  Transition rules by default are applied only on UPDATE requests and are skipped if an old value could not be found. You can opt a transition rule into unconditional evaluation by setting `optionalOldSelf` to true.  # noqa: E501
services/chroma_inspect_venv/lib64/python3.12/site-packages/kubernetes/client/models/v1_validation_rule.py:209:        Rule represents the expression which will be evaluated by CEL. ref: https://github.com/google/cel-spec The Rule is scoped to the location of the x-kubernetes-validations extension in the schema. The `self` variable in the CEL expression is bound to the scoped value. Example: - Rule scoped to the root of a resource with a status subresource: {\"rule\": \"self.status.actual <= self.spec.maxDesired\"}  If the Rule is scoped to an object with properties, the accessible properties of the object are field selectable via `self.field` and field presence can be checked via `has(self.field)`. Null valued fields are treated as absent fields in CEL expressions. If the Rule is scoped to an object with additionalProperties (i.e. a map) the value of the map are accessible via `self[mapKey]`, map containment can be checked via `mapKey in self` and all entries of the map are accessible via CEL macros and functions such as `self.all(...)`. If the Rule is scoped to an array, the elements of the array are accessible via `self[i]` and also by macros and functions. If the Rule is scoped to a scalar, `self` is bound to the scalar value. Examples: - Rule scoped to a map of objects: {\"rule\": \"self.components['Widget'].priority < 10\"} - Rule scoped to a list of integers: {\"rule\": \"self.values.all(value, value >= 0 && value < 100)\"} - Rule scoped to a string value: {\"rule\": \"self.startsWith('kube')\"}  The `apiVersion`, `kind`, `metadata.name` and `metadata.generateName` are always accessible from the root of the object and from any x-kubernetes-embedded-resource annotated objects. No other metadata properties are accessible.  Unknown data preserved in custom resources via x-kubernetes-preserve-unknown-fields is not accessible in CEL expressions. This includes: - Unknown field values that are preserved by object schemas with x-kubernetes-preserve-unknown-fields. - Object properties where the property schema is of an \"unknown type\". An \"unknown type\" is recursively defined as:   - A schema with no type and x-kubernetes-preserve-unknown-fields set to true   - An array where the items schema is of an \"unknown type\"   - An object where the additionalProperties schema is of an \"unknown type\"  Only property names of the form `[a-zA-Z_.-/][a-zA-Z0-9_.-/]*` are accessible. Accessible property names are escaped according to the following rules when accessed in the expression: - '__' escapes to '__underscores__' - '.' escapes to '__dot__' - '-' escapes to '__dash__' - '/' escapes to '__slash__' - Property names that exactly match a CEL RESERVED keyword escape to '__{keyword}__'. The keywords are:    \"true\", \"false\", \"null\", \"in\", \"as\", \"break\", \"const\", \"continue\", \"else\", \"for\", \"function\", \"if\",    \"import\", \"let\", \"loop\", \"package\", \"namespace\", \"return\". Examples:   - Rule accessing a property named \"namespace\": {\"rule\": \"self.__namespace__ > 0\"}   - Rule accessing a property named \"x-prop\": {\"rule\": \"self.x__dash__prop > 0\"}   - Rule accessing a property named \"redact__d\": {\"rule\": \"self.redact__underscores__d > 0\"}  Equality on arrays with x-kubernetes-list-type of 'set' or 'map' ignores element order, i.e. [1, 2] == [2, 1]. Concatenation on arrays with x-kubernetes-list-type use the semantics of the list type:   - 'set': `X + Y` performs a union where the array positions of all elements in `X` are preserved and     non-intersecting elements in `Y` are appended, retaining their partial order.   - 'map': `X + Y` performs a merge where the array positions of all keys in `X` are preserved but the values     are overwritten by values in `Y` when the key sets of `X` and `Y` intersect. Elements in `Y` with     non-intersecting keys are appended, retaining their partial order.  If `rule` makes use of the `oldSelf` variable it is implicitly a `transition rule`.  By default, the `oldSelf` variable is the same type as `self`. When `optionalOldSelf` is true, the `oldSelf` variable is a CEL optional  variable whose value() is the same type as `self`. See the documentation for the `optionalOldSelf` field for details.  Transition rules by default are applied only on UPDATE requests and are skipped if an old value could not be found. You can opt a transition rule into unconditional evaluation by setting `optionalOldSelf` to true.  # noqa: E501
services/ms_jarvis_main_gateway.pre_fix.py:105:        "SELECT ueid FROM identity_hashes WHERE name_dob_hash = ?",
services/ms_jarvis_main_gateway.pre_fix.py:127:    c.execute("""INSERT INTO identity_hashes
services/ms_jarvis_layer2_dgm.py:101:            c.execute("UPDATE user_conversations SET analyzed=1, sentiment_score=?, emotion_detected=?, topics_detected=?, needs_detected=?, analyzed_at=? WHERE id=?",
services/ms_jarvis_messenger_ui_fixed.py:195:        cursor.execute("SELECT MAX(timestamp) FROM ms_jarvis_learning_log")
services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:53:            rows = conn.execute("SELECT COUNT(*) FROM gisgeodata").fetchone()[0] or 1002
services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:166:            "SELECT county, state, lat, lon, description FROM gisgeodata WHERE UPPER(location) LIKE UPPER(?) LIMIT 1",
services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:207:            ['mysql', '-u', 'root', '-e', 'SELECT COUNT(*) FROM msjarvis_research.research_records'],
services/ms_jarvis_messenger_ui.py:120:        cursor.execute("SELECT MAX(timestamp) FROM ms_jarvis_learning_log")
services/ms_jarvis_messenger_ui.py:147:            SELECT timestamp, learning_action FROM ms_jarvis_learning_log
services/geospatial_resolver.py:25:              SELECT geom
services/geospatial_resolver.py:26:              FROM quantumaigbimfeatures
services/geospatial_resolver.py:32:        geom_expr = "(SELECT geom FROM b)"
services/geospatial_resolver.py:34:        sql.append("WITH b AS (SELECT ST_SetSRID(ST_Point(%s, %s), 4326) AS geom)")
services/geospatial_resolver.py:36:        geom_expr = "(SELECT geom FROM b)"
services/geospatial_resolver.py:46:      FROM b
services/geospatial_resolver.py:47:      LEFT JOIN geospatial_counties c
services/geospatial_resolver.py:49:      LEFT JOIN geospatial_utility_territories u
services/geospatial_resolver.py:51:      LEFT JOIN geospatial_zoning z
services/geospatial_resolver.py:53:      LEFT JOIN geospatial_census_tracts t
services/ms_jarvis_consciousness_final.py.pre_dynamic_discovery:231:KNOWLEDGE FROM CHROMADB:
services/ms_jarvis_main_gateway.proxy_backup.py:175:    c.execute("SELECT ueid FROM identity_hashes WHERE name_dob_hash = ?", (name_dob_hash,))
services/ms_jarvis_main_gateway.proxy_backup.py:195:    c.execute("""INSERT INTO identity_hashes 
services/msjarvisunifiedgateway.py:99:        cursor.execute("SELECT COUNT(*) FROM gisgeodata;")
services/ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER.py:49:            rows = conn.execute("SELECT COUNT(*) FROM gisgeodata").fetchone()[0] or 1002
services/ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER.py:164:            "SELECT county, state, lat, lon, description FROM gisgeodata WHERE UPPER(location) LIKE UPPER(?) LIMIT 1",
services/health_access_gbim_bridge.py:85:                    SELECT block_id, geographic, pop2020, provider_count
services/health_access_gbim_bridge.py:86:                    FROM public.block_provider_summary
services/health_access_gbim_bridge.py:125:                    SELECT provider_id, center, pop_served, blocks_served
services/health_access_gbim_bridge.py:126:                    FROM public.provider_population_summary
services/ms_jarvis_unified_swagger_gateway_FIXED.py.new:33:    c.execute("SELECT ueid FROM identity_hashes WHERE name_dob_hash = ?", (name_dob_hash,))
services/ms_jarvis_unified_swagger_gateway_FIXED.py.new:69:    c.execute("""INSERT INTO users_identity_vault 
services/ms_jarvis_unified_swagger_gateway_FIXED.py.new:75:    c.execute("""INSERT INTO identity_hashes 
services/ms_jarvis_unified_swagger_gateway_FIXED.py.new:81:    c.execute("""INSERT INTO registration_tokens 
services/create_immutable_security_layer.py:157:    FROM ueid_searchable_gis usg
services/ms_jarvis_consciousness_bridge.py.working_backup:727:    # GET I-CONTAINER IDENTITY CONTEXT FROM FIFTH DGM
services/extract_chroma_sqlite_to_gis.py:25:    logger.info("📚 EXTRACTING FROM CHROMA.SQLITE3 → GIS")
services/extract_chroma_sqlite_to_gis.py:43:        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
services/extract_chroma_sqlite_to_gis.py:49:                cursor.execute(f"SELECT COUNT(*) FROM {table}")
services/ms_jarvis_expiration_monitor.py:144:        FROM identity_verifications
services/ms_jarvis_expiration_monitor.py:176:                            UPDATE identity_verifications
services/ms_jarvis_expiration_monitor.py:189:                    UPDATE identity_verifications
services/Dockerfile.rag_server:1:FROM python:3.11-slim
services/batch_normalize_beliefs.py:19:        SELECT g.id,
services/batch_normalize_beliefs.py:26:        FROM public.gbim_worldview_entity g
services/batch_normalize_beliefs.py:27:        LEFT JOIN public.gbim_belief_normalized n
services/batch_normalize_beliefs.py:44:                INSERT INTO public.gbim_belief_normalized (
services/Dockerfile.psychological_rag:1:FROM python:3.12-slim
services/ms_jarvis_main_gateway.broken_final.py:124:    c.execute("SELECT ueid FROM identity_hashes WHERE name_dob_hash = ?", (name_dob_hash,))
services/ms_jarvis_main_gateway.broken_final.py:143:    c.execute("INSERT INTO identity_hashes (name_dob_hash, ueid, email, dl_verified, dl_path, created_at) VALUES (?, ?, ?, ?, ?, datetime('now'))", (name_dob_hash, ueid, email, dl_verified, dl_path))
services/gbim_explain.py:50:            SELECT layer_name, feature_id, name, ST_AsText(geom)
services/gbim_explain.py:51:            FROM geospatial_features
services/working_full_pipeline_WITH_SPATIAL_TEMPORAL.py:27:    # GET ACTUAL LOCATION & TIME FROM SERVICES
services/extract_all_chromadb_to_gis.py:24:    logger.info("📚 EXTRACTING ALL DATA FROM CHROMADB PERSISTENT STORAGE")
services/extract_all_chromadb_to_gis.py:40:            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
services/dgm_orchestrator.py:233:            SELECT id, identity_element,
services/dgm_orchestrator.py:260:            SELECT id, identity_element,
services/dgm_orchestrator.py:295:                "SELECT id, identity_element FROM central_i_container WHERE is_active=1 ORDER BY id DESC"
services/truth_filter_bbb_verification.py:149:            UPDATE ueid_gis_mapping
services/registration_service_clean.py.broken:201:        c.execute("""INSERT INTO users_identity_vault VALUES (?, ?, ?, ?, ?)""",
services/registration_service_clean.py.broken:208:        c.execute("""INSERT INTO identity_hashes VALUES (?, ?, ?, ?)""",
services/registration_service_clean.py.broken:213:        c.execute("""INSERT INTO registration_tokens VALUES (?, ?, ?, ?, ?)""",
services/registration_service_clean.py.broken:268:            'SELECT email FROM registration_tokens WHERE token = ? AND ueid = ?',
services/registration_service_clean.py.broken:291:            UPDATE registration_tokens SET
services/ms_jarvis_gis_query_with_bbb_gisgeodb.py:57:        INSERT INTO bbb_filter_log 
services/ms_jarvis_gis_query_with_bbb_gisgeodb.py:92:        INSERT INTO geographic_knowledge 
services/Dockerfile.spiritual_rag:1:FROM python:3.10-slim
services/academic_research_gateway_8062.py:35:        cursor.execute("SELECT timestamp FROM ms_jarvis_learning_log WHERE learning_action = 'consciousness' ORDER BY id DESC LIMIT 1")
services/academic_research_gateway_8062.py:76:        cursor.execute(f"SELECT id, timestamp, learning_action FROM ms_jarvis_learning_log ORDER BY id DESC LIMIT {min(limit, 200)}")
services/academic_research_gateway_8062.py:89:        cursor.execute("SELECT timestamp, learning_action FROM ms_jarvis_learning_log ORDER BY id DESC LIMIT 5")
services/full_system_health_check.sh:222:    DB_RECORDS=$(sqlite3 data/GISGEODB_ACTIVE.sqlite "SELECT COUNT(*) FROM geographic_knowledge;" 2>/dev/null || echo "?")
services/add_identity_context.py:21:    # GET I-CONTAINER IDENTITY CONTEXT FROM FIFTH DGM
services/ms_jarvis_main_gateway.py.30endpoints_backup.py:144:    c.execute("SELECT ueid, email, dl_verified FROM identity_hashes LIMIT 5")
services/ms_jarvis_main_gateway.py.30endpoints_backup.py:182:    c.execute("SELECT ueid FROM identity_hashes WHERE name_dob_hash = ?", (name_dob_hash,))
services/ms_jarvis_main_gateway.py.30endpoints_backup.py:200:    c.execute("INSERT INTO identity_hashes (name_dob_hash, ueid, email, dl_verified, dl_path) VALUES (?, ?, ?, ?, ?)", 
services/ms_jarvis_main_gateway.py.30endpoints_backup.py:216:    c.execute("UPDATE identity_hashes SET dl_verified = ? WHERE ueid = ?", (verified, ueid))
services/ms_jarvis_main_gateway.py.30endpoints_backup.py:230:    c.execute("SELECT * FROM identity_hashes WHERE ueid = ?", (ueid,))
services/complete_system_audit_with_swagger.py:235:        "users": c.execute("SELECT COUNT(*) FROM ueid_identity").fetchone()[0],
services/autonomous_learner_gisgeodb_wrapper.psychology_patched.py:53:            INSERT INTO autonomous_learner_queries
services/autonomous_learner_gisgeodb_wrapper.psychology_patched.py:95:    c.execute("SELECT COUNT(*) FROM autonomous_learner_queries")
services/ms_jarvis_unified_gateway_v4.3.py.BEFORE_INVESTIGATION:46:            rows = conn.execute("SELECT COUNT(*) FROM gisgeodata").fetchone()[0] or 1002
services/ms_jarvis_unified_gateway_v4.3.py.BEFORE_INVESTIGATION:159:            "SELECT county, state, lat, lon, description FROM gisgeodata WHERE UPPER(location) LIKE UPPER(?) LIMIT 1",
services/ms_jarvis_unified_gateway_v4.3.py.BEFORE_INVESTIGATION:200:            ['mysql', '-u', 'root', '-e', 'SELECT COUNT(*) FROM msjarvis_research.research_records'],
services/jarvis_hilbert_time.py:251:                SELECT admitted_at
services/jarvis_hilbert_time.py:252:                FROM public.temporal_historical_memory
services/jarvis_hilbert_time.py:276:                UPDATE public.temporal_historical_memory
services/jarvis_hilbert_time.py:285:                INSERT INTO public.temporal_historical_memory
services/jarvis_hilbert_time.py:338:                    SELECT id, timestamp_iso, epoch, payload,
services/jarvis_hilbert_time.py:340:                    FROM public.temporal_historical_memory
services/jarvis_hilbert_time.py:347:                    SELECT id, timestamp_iso, epoch, payload,
services/jarvis_hilbert_time.py:349:                    FROM public.temporal_historical_memory
services/sync_geodb_to_chromadb.py:17:        "SELECT id, name, description FROM public.features "
services/bulk_build_beliefs.py:8:        SELECT sourcetable, geom_table, geom_column,
services/bulk_build_beliefs.py:11:        FROM gbim_layer_config
services/bulk_build_beliefs.py:24:        cur.execute("SELECT to_regclass(%s);", (geom_table,))
services/bulk_build_beliefs.py:34:                SELECT DISTINCT ON (b.building_id)
services/bulk_build_beliefs.py:38:                FROM buildings b
services/bulk_build_beliefs.py:50:                FROM buildings b
services/bulk_build_beliefs.py:62:            INSERT INTO gbim_beliefs (
services/ms_jarvis_unified_gateway_v4.3.py.PRE_GUARDS_20251105_171934:46:            rows = conn.execute("SELECT COUNT(*) FROM gisgeodata").fetchone()[0] or 1002
services/ms_jarvis_unified_gateway_v4.3.py.PRE_GUARDS_20251105_171934:161:            "SELECT county, state, lat, lon, description FROM gisgeodata WHERE UPPER(location) LIKE UPPER(?) LIMIT 1",
services/local_resources_resolver.py:84:    FROM local_resources
services/knowledge_docs_attributes.geojson:8738:        "date": "<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->",
services/knowledge_docs_attributes.geojson:9581:        "author": "THE SOFTWARE IS PROVIDED \"AS IS\" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.",
services/knowledge_docs_attributes.geojson:9585:        "headings": "THE SOFTWARE IS PROVIDED \"AS IS\" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE."
services/IMMUTABLE_MANIFEST.md:60:- **Constraints**: Database triggers PREVENT UPDATE and DELETE
attrs_with_geom_api.py:32:                f"SELECT geodb_id, ST_AsGeoJSON(geom) "
bootstrap_gbim_beliefs_eq1.py:36:        SELECT worldview_id
bootstrap_gbim_beliefs_eq1.py:37:        FROM gbim_worldviews
bootstrap_gbim_beliefs_eq1.py:47:        INSERT INTO gbim_worldviews (name, description, version_tag, valid_from)
bootstrap_gbim_beliefs_eq1.py:102:        INSERT INTO gbim_layer_catalog (
bootstrap_gbim_beliefs_eq1.py:124:        INSERT INTO gbim_evidence (
bootstrap_gbim_beliefs_eq1.py:157:        INSERT INTO gbim_beliefs (
bootstrap_gbim_beliefs_eq1.py:179:        FROM gbim_evidence e
bootstrap_gbim_beliefs_eq1.py:180:        JOIN gbim_layer_catalog c
bootstrap_gbim_beliefs_eq1.py:188:        INSERT INTO gbim_belief_evidence (belief_id, evidence_id, role)
bootstrap_gbim_beliefs_eq1.py:193:        FROM gbim_beliefs b
bootstrap_gbim_beliefs_eq1.py:194:        JOIN gbim_evidence e
bootstrap_gbim_beliefs_eq1.py:208:        INSERT INTO gbim_belief_edges (
bootstrap_gbim_beliefs_eq1.py:219:        FROM gbim_beliefs b
bootstrap_gbim_beliefs_eq1.py:220:        LEFT JOIN gbim_belief_edges e
bootstrap_gbim_beliefs_eq1.py:243:                SELECT gbim_join_table, pk_column
bootstrap_gbim_beliefs_eq1.py:244:                FROM gbim_layer_catalog
bulk_ingest_attrs.py:34:                f'COPY gbimattrs."{tname}" FROM STDIN WITH (FORMAT CSV, HEADER TRUE)',
bulk_ingest_attrs.py:40:            UPDATE public.gbimbeliefnormalized b
bulk_ingest_attrs.py:45:            FROM public.gbimworldviewentity e
bulk_ingest_attrs.py:51:            UPDATE public.gbimbeliefnormalized b
bulk_ingest_attrs.py:57:            FROM public.gbimworldviewentity e
bulk_ingest_attrs.py:58:            JOIN gbimattrs."{tname}" attrs
enrich_from_attrs.py:6:  2. JOIN gbimbeliefnormalized to the attrs table on source_pk/sourcepk = geodb_id
enrich_from_attrs.py:241:        SELECT epoch FROM gbim_source_epochs WHERE sourcetable = %s
enrich_from_attrs.py:293:            UPDATE public.gbimbeliefnormalized b
enrich_from_attrs.py:295:            FROM gbimattrs."{tname}" attrs
enrich_where.py:15:    FROM public.gbimbeliefnormalized
enrich_where.py:37:        UPDATE public.gbimbeliefnormalized b
enrich_where.py:43:        FROM gbimattrs."{st}" attrs
gisgeodbstorage.py:37:            INSERT INTO autonomouslearnerqueries
index_gis_to_chroma.py:64:    pg_cur.execute("SELECT COUNT(*) FROM geospatial_features")
index_gis_to_chroma.py:117:        FROM geospatial_features
list_due_for_verification.py:8:    SELECT id, name, county, contact_email, contact_phone, source_url,
list_due_for_verification.py:10:    FROM resources_due_for_verification
load_services_attrs_and_enrich.py:80:        FROM public.gbimbeliefnormalized
msjarvis_embed_gbim.py:70:        SELECT id,
msjarvis_embed_gbim.py:80:        FROM public.gbimbeliefnormalized
msjarvis_embed_gbim_resume_tail.py:19:        SELECT id, belief_text, metadata::text
msjarvis_embed_gbim_resume_tail.py:20:        FROM gbim_beliefs_v2
rag_server_main.py:471:        cur.execute("SELECT COUNT(*) FROM episodic_log")
rag_server_main.py:475:        cur.execute("SELECT source, COUNT(*) FROM episodic_log GROUP BY source")
rag_server_main.py:479:        cur.execute("SELECT episode_type, COUNT(*) FROM episodic_log GROUP BY episode_type")
rag_server_main.py:485:            SELECT date_trunc('day', timestamp) AS day, COUNT(*)
rag_server_main.py:486:            FROM episodic_log
rag_server_main.py:497:            SELECT COUNT(*)
rag_server_main.py:498:            FROM episodic_log
rag_server_main.py:507:            SELECT COUNT(*)
rag_server_main.py:508:            FROM episodic_log
rag_server_main.py:517:            SELECT date_trunc('week', timestamp) AS week_start, COUNT(*)
rag_server_main.py:518:            FROM episodic_log
rag_server_main.py:529:            SELECT date_trunc('month', timestamp) AS month_start, COUNT(*)
rag_server_main.py:530:            FROM episodic_log
rag_server_main.py:541:            SELECT MIN(timestamp), MAX(timestamp)
rag_server_main.py:542:            FROM episodic_log
sync_gbim_to_chroma.py:42:        FROM public.gbim_worldview_entity;

===== DATABASE ENVIRONMENT VARIABLE NAMES ONLY — VALUES REDACTED =====
docker-compose.yml:530:    - GBIM_DSN=postgresql://REDACTED@172.18.0.1:5433/msjarvisgis
docker-compose.yml:1254:    - POSTGRES_DB=postgres
docker-compose.yml:1255:    - POSTGRES_USER=postgres
docker-compose.yml:1256:    - POSTGRES_PASSWORD=postgres
docker-compose.yml:1553:    - POSTGRES_DSN=postgresql://REDACTED@172.18.0.1:5432/local_resources
docker-compose.yml:1558:    - DATABASE_URL=postgresql://REDACTED@172.18.0.1:5432/local_resources
docker-compose.yml:1658:    - DATABASE_URL=postgresql://REDACTED@jarvis-local-resources-db:5432/hilbert_people
docker-compose.yml:1894:    - POSTGRES_HOST=172.18.0.1
docker-compose.yml:1895:    - POSTGRES_PORT=5433
docker-compose.yml:1896:    - POSTGRES_DB=msjarvisgis
docker-compose.yml:1897:    - POSTGRES_USER=postgres
docker-compose.yml:1898:    - POSTGRES_PASSWORD=postgres
docker-compose.yml:1915:    - POSTGRES_PORT=5432
docker-compose.yml:1916:    - POSTGRES_DB=gisdb
docker-compose.yml:1917:    - POSTGRES_USER=postgres
docker-compose.yml:1918:    - POSTGRES_PASSWORD=postgres
docker-compose.yml:1919:    - POSTGRES_HOST=172.18.0.1
docker-compose.yml:1920:    - POSTGRES_PORT=5432
docker-compose.yml:2034:    - DB_HOST=jarvis-local-resources-db
docker-compose.yml:2036:    - DB_NAME=msjarvisgis
docker-compose.yml:2037:    - DB_USER=msjarvis
services/enrich_geodb_layers.py:13:GEODB_DSN = os.getenv(
services/enrich_geodb_layers.py:14:    "GEODB_DSN",
services/enrich_geodb_layers.py:358:    return psycopg2.connect(GEODB_DSN)
services/gis_rag_service.py:20:POSTGRES_DSN = os.getenv("POSTGRES_DSN", "postgresql://REDACTED@jarvis-msjarvis-db:5432/msjarvisgis")
services/gis_rag_service.py:519:    conn = psycopg2.connect(POSTGRES_DSN)
services/geo/api.py:27:GEODB_DSN = "postgresql://REDACTED@localhost:5432/msjarvis_gis"
services/geo/api.py:43:    conn = psycopg2.connect(GEODB_DSN)
services/geo/api.py:76:GEODB_DSN = "postgresql://REDACTED@localhost:5432/msjarvis_gis"
services/geo/api.py:96:    conn = psycopg2.connect(GEODB_DSN)
services/geo/api.py:129:GEODB_DSN = "postgresql://REDACTED@localhost:5432/msjarvis_gis"
services/geo/api.py:149:    conn = psycopg2.connect(GEODB_DSN)
services/restored_documents.json:3382:      "content": "ies\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118\npip install transformers sentence-transformers\npip install ollama\n\nWeb framework and API\npip install fastapi uvicorn flask\n\nDatabase and storage\npip install redis chromadb\n\nUtilities and processing\npip install psutil pyyaml python-dotenv\npip install asyncio aiofiles\npip install requests numpy pandas\n\ntext\n\n#### Step 3: Configure Services\nSet up environment variables\ncat > .env << 'ENVEOF'\nOLLAMA_URL=http://localhost:11434\nREDIS_URL=redis://localhost:6379\nPOSTGRES_URL=postgresql://REDACTED@localhost:5432/ms_jarvis\nJARVIS_PORT=8010\nVECTOR_DB_PORT=8001\nENVEOF\n\nMake scripts executable\nchmod +x *.py\n\nSet up logging directory\nmkdir -p logs\nmkdir -p data/vector_db\nmkdir -p backups\n\ntext\n\n#### Step 4: Database Setup\nStart Redis (should already be running)\nsudo systemctl status redis-server\n\nCreate PostgreSQL database\nsudo -u postgres createdb ms_jarvis\nsudo -u postgres psql -c \"CREATE USER jarvis WITH PASSWORD 'your_password_here';\"\nsudo -u postgres psql -c \"GRANT ALL PRIVILEGES ON DATABASE ms_jarvis TO jarvis;\"\n\ntext\n\n#### Step 5: Start Core Services (In Order)\nTerminal 1: Start AI Server (core brain)\nsource venv/bin/activate\npython ai_server.py\n\nTerminal 2: Start Service Factory\nsource venv/bin/activate\npython ms_jarvis_service_factory.py\n\nTerminal 3: Start Brain Orchestrator\nsource venv/bin/activate\npython dynamic_app.py\n\nTerminal 4: Start Service Discovery\nsource venv/bin/activate",
services/restored_documents.json:13470:      "content": "r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env dotenv_config_debug=true\n```\n\nAdditionally, you can use environment variables to set configuration options. Command line arguments will precede these.\n\n```bash\n$ DOTENV_CONFIG_<OPTION>=value node -r dotenv/config your_script.js\n```\n\n```bash\n$ DOTENV_CONFIG_ENCODING=latin1 DOTENV_CONFIG_DEBUG=true node -r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env\n```\n\n### Variable Expansion\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use variable expansion.\n\nReference and expand variables already on your machine for use in your .env file.\n\n```ini\n# .env\nUSERNAME=\"username\"\nDATABASE_URL=\"postgres://REDACTED@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (2) from .env\nDATABASE_URL postgres://REDACTED@localhost/my_database\n```\n\n### Command Substitution\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use command substitution.\n\nAdd the output of a command to one of your variables in your .env file.\n\n```ini\n# .env\nDATABASE_URL=\"postgres://REDACTED@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://REDACTED@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync betw",
services/restored_documents.json:13478:      "content": "_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://REDACTED@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync between machines, environments, or team members? Use [dotenvx](https://github.com/dotenvx/dotenvx) to encrypt your `.env` files and safely include them in source control. This still subscribes to the twelve-factor app rules by generating a decryption key separate from code.\n\n### Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to generate `.env.ci`, `.env.production` files, and more.\n\n### Deploying\n\nYou need to deploy your secrets in a cloud-agnostic manner? Use [dotenvx](https://github.com/dotenvx/dotenvx) to generate a private decryption key that is set on your production server.\n\n## \ud83c\udf34 Manage Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx)\n\nRun any environment locally. Create a `.env.ENVIRONMENT` file and use `--env-file` to load it. It's straightforward, yet flexible.\n\n```bash\n$ echo \"HELLO=production\" > .env.production\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx run --env-file=.env.production -- node index.js\nHello production\n> ^^\n```\n\nor with multiple .env files\n\n```bash\n$ echo \"HELLO=local\" > .env.local\n$ echo \"HELLO=World\" > .env\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx ",
services/restored_documents.json:37038:      "content": "r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env dotenv_config_debug=true\n```\n\nAdditionally, you can use environment variables to set configuration options. Command line arguments will precede these.\n\n```bash\n$ DOTENV_CONFIG_<OPTION>=value node -r dotenv/config your_script.js\n```\n\n```bash\n$ DOTENV_CONFIG_ENCODING=latin1 DOTENV_CONFIG_DEBUG=true node -r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env\n```\n\n### Variable Expansion\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use variable expansion.\n\nReference and expand variables already on your machine for use in your .env file.\n\n```ini\n# .env\nUSERNAME=\"username\"\nDATABASE_URL=\"postgres://REDACTED@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (2) from .env\nDATABASE_URL postgres://REDACTED@localhost/my_database\n```\n\n### Command Substitution\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use command substitution.\n\nAdd the output of a command to one of your variables in your .env file.\n\n```ini\n# .env\nDATABASE_URL=\"postgres://REDACTED@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://REDACTED@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync betw",
services/restored_documents.json:37046:      "content": "_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://REDACTED@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync between machines, environments, or team members? Use [dotenvx](https://github.com/dotenvx/dotenvx) to encrypt your `.env` files and safely include them in source control. This still subscribes to the twelve-factor app rules by generating a decryption key separate from code.\n\n### Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to generate `.env.ci`, `.env.production` files, and more.\n\n### Deploying\n\nYou need to deploy your secrets in a cloud-agnostic manner? Use [dotenvx](https://github.com/dotenvx/dotenvx) to generate a private decryption key that is set on your production server.\n\n## \ud83c\udf34 Manage Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx)\n\nRun any environment locally. Create a `.env.ENVIRONMENT` file and use `--env-file` to load it. It's straightforward, yet flexible.\n\n```bash\n$ echo \"HELLO=production\" > .env.production\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx run --env-file=.env.production -- node index.js\nHello production\n> ^^\n```\n\nor with multiple .env files\n\n```bash\n$ echo \"HELLO=local\" > .env.local\n$ echo \"HELLO=World\" > .env\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx ",
services/restored_documents.json:48382:      "content": "r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env dotenv_config_debug=true\n```\n\nAdditionally, you can use environment variables to set configuration options. Command line arguments will precede these.\n\n```bash\n$ DOTENV_CONFIG_<OPTION>=value node -r dotenv/config your_script.js\n```\n\n```bash\n$ DOTENV_CONFIG_ENCODING=latin1 DOTENV_CONFIG_DEBUG=true node -r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env\n```\n\n### Variable Expansion\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use variable expansion.\n\nReference and expand variables already on your machine for use in your .env file.\n\n```ini\n# .env\nUSERNAME=\"username\"\nDATABASE_URL=\"postgres://REDACTED@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (2) from .env\nDATABASE_URL postgres://REDACTED@localhost/my_database\n```\n\n### Command Substitution\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use command substitution.\n\nAdd the output of a command to one of your variables in your .env file.\n\n```ini\n# .env\nDATABASE_URL=\"postgres://REDACTED@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://REDACTED@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync betw",
services/restored_documents.json:48390:      "content": "_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://REDACTED@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync between machines, environments, or team members? Use [dotenvx](https://github.com/dotenvx/dotenvx) to encrypt your `.env` files and safely include them in source control. This still subscribes to the twelve-factor app rules by generating a decryption key separate from code.\n\n### Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to generate `.env.ci`, `.env.production` files, and more.\n\n### Deploying\n\nYou need to deploy your secrets in a cloud-agnostic manner? Use [dotenvx](https://github.com/dotenvx/dotenvx) to generate a private decryption key that is set on your production server.\n\n## \ud83c\udf34 Manage Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx)\n\nRun any environment locally. Create a `.env.ENVIRONMENT` file and use `--env-file` to load it. It's straightforward, yet flexible.\n\n```bash\n$ echo \"HELLO=production\" > .env.production\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx run --env-file=.env.production -- node index.js\nHello production\n> ^^\n```\n\nor with multiple .env files\n\n```bash\n$ echo \"HELLO=local\" > .env.local\n$ echo \"HELLO=World\" > .env\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx ",
services/restored_documents.json:58142:      "content": "r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env dotenv_config_debug=true\n```\n\nAdditionally, you can use environment variables to set configuration options. Command line arguments will precede these.\n\n```bash\n$ DOTENV_CONFIG_<OPTION>=value node -r dotenv/config your_script.js\n```\n\n```bash\n$ DOTENV_CONFIG_ENCODING=latin1 DOTENV_CONFIG_DEBUG=true node -r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env\n```\n\n### Variable Expansion\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use variable expansion.\n\nReference and expand variables already on your machine for use in your .env file.\n\n```ini\n# .env\nUSERNAME=\"username\"\nDATABASE_URL=\"postgres://REDACTED@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (2) from .env\nDATABASE_URL postgres://REDACTED@localhost/my_database\n```\n\n### Command Substitution\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use command substitution.\n\nAdd the output of a command to one of your variables in your .env file.\n\n```ini\n# .env\nDATABASE_URL=\"postgres://REDACTED@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://REDACTED@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync betw",
services/restored_documents.json:58150:      "content": "_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://REDACTED@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync between machines, environments, or team members? Use [dotenvx](https://github.com/dotenvx/dotenvx) to encrypt your `.env` files and safely include them in source control. This still subscribes to the twelve-factor app rules by generating a decryption key separate from code.\n\n### Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to generate `.env.ci`, `.env.production` files, and more.\n\n### Deploying\n\nYou need to deploy your secrets in a cloud-agnostic manner? Use [dotenvx](https://github.com/dotenvx/dotenvx) to generate a private decryption key that is set on your production server.\n\n## \ud83c\udf34 Manage Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx)\n\nRun any environment locally. Create a `.env.ENVIRONMENT` file and use `--env-file` to load it. It's straightforward, yet flexible.\n\n```bash\n$ echo \"HELLO=production\" > .env.production\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx run --env-file=.env.production -- node index.js\nHello production\n> ^^\n```\n\nor with multiple .env files\n\n```bash\n$ echo \"HELLO=local\" > .env.local\n$ echo \"HELLO=World\" > .env\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx ",
services/restored_documents.json:63734:      "content": "r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env dotenv_config_debug=true\n```\n\nAdditionally, you can use environment variables to set configuration options. Command line arguments will precede these.\n\n```bash\n$ DOTENV_CONFIG_<OPTION>=value node -r dotenv/config your_script.js\n```\n\n```bash\n$ DOTENV_CONFIG_ENCODING=latin1 DOTENV_CONFIG_DEBUG=true node -r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env\n```\n\n### Variable Expansion\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use variable expansion.\n\nReference and expand variables already on your machine for use in your .env file.\n\n```ini\n# .env\nUSERNAME=\"username\"\nDATABASE_URL=\"postgres://REDACTED@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (2) from .env\nDATABASE_URL postgres://REDACTED@localhost/my_database\n```\n\n### Command Substitution\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use command substitution.\n\nAdd the output of a command to one of your variables in your .env file.\n\n```ini\n# .env\nDATABASE_URL=\"postgres://REDACTED@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://REDACTED@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync betw",
services/restored_documents.json:63742:      "content": "_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://REDACTED@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync between machines, environments, or team members? Use [dotenvx](https://github.com/dotenvx/dotenvx) to encrypt your `.env` files and safely include them in source control. This still subscribes to the twelve-factor app rules by generating a decryption key separate from code.\n\n### Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to generate `.env.ci`, `.env.production` files, and more.\n\n### Deploying\n\nYou need to deploy your secrets in a cloud-agnostic manner? Use [dotenvx](https://github.com/dotenvx/dotenvx) to generate a private decryption key that is set on your production server.\n\n## \ud83c\udf34 Manage Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx)\n\nRun any environment locally. Create a `.env.ENVIRONMENT` file and use `--env-file` to load it. It's straightforward, yet flexible.\n\n```bash\n$ echo \"HELLO=production\" > .env.production\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx run --env-file=.env.production -- node index.js\nHello production\n> ^^\n```\n\nor with multiple .env files\n\n```bash\n$ echo \"HELLO=local\" > .env.local\n$ echo \"HELLO=World\" > .env\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx ",
services/restored_documents.json:78374:      "content": "r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env dotenv_config_debug=true\n```\n\nAdditionally, you can use environment variables to set configuration options. Command line arguments will precede these.\n\n```bash\n$ DOTENV_CONFIG_<OPTION>=value node -r dotenv/config your_script.js\n```\n\n```bash\n$ DOTENV_CONFIG_ENCODING=latin1 DOTENV_CONFIG_DEBUG=true node -r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env\n```\n\n### Variable Expansion\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use variable expansion.\n\nReference and expand variables already on your machine for use in your .env file.\n\n```ini\n# .env\nUSERNAME=\"username\"\nDATABASE_URL=\"postgres://REDACTED@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (2) from .env\nDATABASE_URL postgres://REDACTED@localhost/my_database\n```\n\n### Command Substitution\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use command substitution.\n\nAdd the output of a command to one of your variables in your .env file.\n\n```ini\n# .env\nDATABASE_URL=\"postgres://REDACTED@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://REDACTED@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync betw",
services/restored_documents.json:78382:      "content": "_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://REDACTED@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync between machines, environments, or team members? Use [dotenvx](https://github.com/dotenvx/dotenvx) to encrypt your `.env` files and safely include them in source control. This still subscribes to the twelve-factor app rules by generating a decryption key separate from code.\n\n### Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to generate `.env.ci`, `.env.production` files, and more.\n\n### Deploying\n\nYou need to deploy your secrets in a cloud-agnostic manner? Use [dotenvx](https://github.com/dotenvx/dotenvx) to generate a private decryption key that is set on your production server.\n\n## \ud83c\udf34 Manage Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx)\n\nRun any environment locally. Create a `.env.ENVIRONMENT` file and use `--env-file` to load it. It's straightforward, yet flexible.\n\n```bash\n$ echo \"HELLO=production\" > .env.production\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx run --env-file=.env.production -- node index.js\nHello production\n> ^^\n```\n\nor with multiple .env files\n\n```bash\n$ echo \"HELLO=local\" > .env.local\n$ echo \"HELLO=World\" > .env\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx ",
services/hippocampus_service.py:11:GBIM_DSN = os.getenv(
services/hippocampus_service.py:12:    "GBIM_DSN",
services/hippocampus_service.py:76:        with closing(psycopg2.connect(GBIM_DSN)) as conn:
services/export_geodb_attrs.py:3:POSTGRES_URL = os.environ.get("POSTGRES_URL")
services/export_geodb_attrs.py:4:if not POSTGRES_URL:
services/export_geodb_attrs.py:5:    print("POSTGRES_URL not set", file=sys.stderr)
services/export_geodb_attrs.py:40:            ["psql", POSTGRES_URL, "-At", "-c", sql],
services/gbim_query_router.py:17:GEODB_DSN          = os.getenv("GEODB_DSN", "postgresql://REDACTED@jarvis-local-resources-db:5432/msjarvisgis")
services/gbim_query_router.py:18:HP_DATABASE_URL    = os.getenv("HP_DATABASE_URL", "postgresql://REDACTED@hp-local-db:5432/hilbert_people")
services/gbim_query_router.py:43:    return await asyncpg.connect(HP_DATABASE_URL)
services/geodb_adapter.py:5:GEODB_DSN = os.getenv("GEODB_DSN", "postgresql://REDACTED@localhost:5432/msjarvis_gis")
services/geodb_adapter.py:8:    conn = psycopg2.connect(GEODB_DSN)
services/resume_sync_wvgistc_buildings.py:9:GEODB_DSN = "postgresql://REDACTED@localhost:5432/msjarvis_gis"
services/resume_sync_wvgistc_buildings.py:31:conn = psycopg2.connect(GEODB_DSN)
services/ingest/ms_allis_ingest_worker.py:22:PGHOST       = os.getenv("DB_HOST")       or os.getenv("PGHOST",    "172.17.0.1")
services/ingest/ms_allis_ingest_worker.py:23:PGPORT       = int(os.getenv("DB_PORT")   or os.getenv("PGPORT",    "5432"))
services/ingest/ms_allis_ingest_worker.py:24:PGDATABASE   = os.getenv("DB_NAME")       or os.getenv("PGDATABASE","msjarvisgis")
services/ingest/ms_allis_ingest_worker.py:25:PGUSER       = os.getenv("DB_USER")       or os.getenv("PGUSER",    "msjarvis")
services/ingest/ms_allis_ingest_worker.py:98:        host=PGHOST, port=PGPORT, dbname=PGDATABASE,
services/ingest/ms_allis_ingest_worker.py:99:        user=PGUSER, password=PGPASSWORD
services/mountainshares_quest_api.py:5:GEODB_DSN = "postgresql://REDACTED@localhost:5432/msjarvis_gis"
services/mountainshares_gbim_suggester.py:14:GBIM_DSN = os.environ.get(
services/mountainshares_gbim_suggester.py:15:    "GBIM_DSN",
services/mountainshares_gbim_suggester.py:111:        conn = await asyncpg.connect(GBIM_DSN)
services/ingest_hospitals.py:8:GEODB_DSN = os.getenv("GEODB_DSN", "postgresql://REDACTED@localhost:5432/msjarvis_gis")
services/ingest_hospitals.py:12:    conn = psycopg2.connect(GEODB_DSN)
services/ingest_hospitals.py:38:    conn = psycopg2.connect(GEODB_DSN)
services/ingest_hospitals.py:68:    conn = psycopg2.connect(GEODB_DSN)
services/bulk_sync_gis_to_chromadb.py:10:GEODB_DSN = os.getenv("GEODB_DSN", "postgresql://REDACTED@localhost:5432/msjarvis_gis")
services/bulk_sync_gis_to_chromadb.py:32:    conn = psycopg2.connect(GEODB_DSN)
services/bulk_sync_gis_to_chromadb.py:108:    conn = psycopg2.connect(GEODB_DSN)
services/create_geodb_nodes.py:9:from enrich_geodb_layers import CONFIG, GEODB_DSN, NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD, BATCH_SIZE
services/create_geodb_nodes.py:16:    return psycopg2.connect(GEODB_DSN)
services/sync_health_access_to_chromadb.py:5:GEODB_DSN = os.getenv("GEODB_DSN", "postgresql://REDACTED@localhost:5432/msjarvis_gis")
services/sync_health_access_to_chromadb.py:12:    conn = psycopg2.connect(GEODB_DSN)
services/chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:174:DB_NAME: Final = "db.name"
services/chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:179:DB_NAMESPACE: Final = "db.namespace"
services/chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:181:Deprecated in favor of stable :py:const:`opentelemetry.semconv.attributes.db_attributes.DB_NAMESPACE`.
services/chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:282:DB_USER: Final = "db.user"
services/chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/semconv/trace/__init__.py:406:    DB_USER = "db.user"
services/chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/semconv/trace/__init__.py:416:    DB_NAME = "db.name"
services/chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/semconv/attributes/db_attributes.py:32:DB_NAMESPACE: Final = "db.namespace"
services/chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:174:DB_NAME: Final = "db.name"
services/chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:179:DB_NAMESPACE: Final = "db.namespace"
services/chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:181:Deprecated in favor of stable :py:const:`opentelemetry.semconv.attributes.db_attributes.DB_NAMESPACE`.
services/chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:282:DB_USER: Final = "db.user"
services/chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/semconv/trace/__init__.py:406:    DB_USER = "db.user"
services/chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/semconv/trace/__init__.py:416:    DB_NAME = "db.name"
services/chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/semconv/attributes/db_attributes.py:32:DB_NAMESPACE: Final = "db.namespace"
services/health_access_gbim_bridge.py:12:GEODB_DSN = os.getenv("GEODB_DSN", "postgresql://REDACTED@localhost:5432/msjarvis_gis")
services/health_access_gbim_bridge.py:19:        self.conn_string = GEODB_DSN
services/batch_normalize_beliefs.py:12:DSN = os.getenv("GBIM_DSN", "postgresql://REDACTED@localhost:5435/msjarvis_gis")
services/jarvis_hilbert_time.py:31:POSTGRES_DSN      = os.getenv("POSTGRES_DSN",
services/jarvis_hilbert_time.py:48:    return psycopg2.connect(POSTGRES_DSN)

===== DATABASE-CONNECTING SERVICES =====
attrs_with_geom_api.py
bootstrap_gbim_beliefs_eq1.py
bulk_ingest_attrs.py
enrich_from_attrs.py
enrich_where.py
gbim_orchestrator.py
index_gis_to_chroma.py
list_due_for_verification.py
load_services_attrs_and_enrich.py
msjarvis_embed_gbim.py
msjarvis_embed_gbim_resume_tail.py
rag_server_main.py
services/apt-list.txt
services/batch_normalize_beliefs.py
services/benefits_chat.py
services/bulk_build_beliefs.py
services/bulk_sync_gis_to_chromadb.py
services/chroma_inspect_venv/lib64/python3.12/site-packages/pydantic/networks.py
services/chroma_inspect_venv/lib64/python3.12/site-packages/pydantic/v1/networks.py
services/chroma_inspect_venv/lib/python3.12/site-packages/pydantic/networks.py
services/chroma_inspect_venv/lib/python3.12/site-packages/pydantic/v1/networks.py
services/create_geodb_nodes.py
services/Dockerfile.hippocampus
services/Dockerfile.intake
services/Dockerfile.pia-sampler
services/dpkg-list.txt
services/enrich_geodb_layers.py
services/gbim_explain.py
services/gbim_query_router.py
services/geo/api.py
services/geodb_adapter.py
services/geo_rag_debug_app.py
services/geo_rag_debug.py
services/geospatial_resolver.py
services/gis_rag_service.py
services/health_access_gbim_bridge.py
services/hippocampus_service.py
services/ingest_benefit_programs_to_chroma.py
services/ingest_compliance_tasks_to_chroma.py
services/ingest_hospitals.py
services/ingest/migrations/001_ms_allis_retention.sql
services/ingest/ms_allis_ingest_worker.py
services/ingest_utility_enrollments_to_chroma.py
services/jarvis_hilbert_time.py
services/jarvis_steward/Dockerfile
services/jarvis_steward/main.py
services/jarvis_steward.py
services/local_resources_resolver.py
services/mother_carrie_logging.py
services/mountainshares_gbim_suggester.py
services/mountainshares_quest_api.py
services/populate_redetermination_tracker.py
services/prod.yaml
services/rag_server_main.py
services/requirements-freeze.txt
services/requirements_gbim.txt
services/requirements-list.txt
services/requirements.txt
services/restored_documents.json
services/resume_sync_wvgistc_buildings.py
services/sync_health_access_to_chromadb.py
sync_gbim_to_chroma.py

===== OUTPUT DIRECTORY =====
/tmp/meaning-geometry-investigation/20-protocol-apparatus-verification-20260810T131337Z/21-source-record-and-field-verification/22-catalog-diagnostics
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/nvme1/msjarvis-rebuild$ 
