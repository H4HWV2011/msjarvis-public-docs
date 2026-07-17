(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/msjarvis-rebuild$ cd /opt/msjarvis-rebuild/msjarvis-rebuild

echo "=== 1) Detect actual ZCTA collection name in Chroma ==="
ZCTA_REAL_NAME="$(
docker exec -i jarvis-chroma python3 - <<'PY'
import chromadb
client = chromadb.HttpClient(host="localhost", port=8000)
names = [str(x) for x in client.list_collections()]
z = [n for n in names if "zcta" in n.lower()]
print(z[0] if z else "")
PY
)"
echo "ZCTA_REAL_NAME=$ZCTA_REAL_NAME"
test -n "$ZCTA_REAL_NAME"

echo
echo "=== 2) Show current GIS_RAG_COLLECTIONS in compose and container ==="
grep -n "GIS_RAG_COLLECTIONS" docker-compose.yml
docker inspect -f '{{range .Config.Env}}{{println .}}{{end}}' jarvis-gis-rag | grep '^GIS_RAG_COLLECTIONS='

echo
echo "=== 3) Update docker-compose GIS_RAG_COLLECTIONS to real ZCTA name ==="PY  ))  h.get("distance"),name"),s distance=%s" % ("ginia","nresults":5,"requ
=== 1) Detect actual ZCTA collection name in Chroma ===
ZCTA_REAL_NAME=gbim_wv_zctas_v1

=== 2) Show current GIS_RAG_COLLECTIONS in compose and container ===
1366:    - GIS_RAG_COLLECTIONS=gbimwvcountiesv2,gbimwvtractsv2,gbimwvblockgroupsv2,gbim_wv_zctas_v1
GIS_RAG_COLLECTIONS=gbimwvcountiesv2,gbimwvtractsv2,gbimwvblockgroupsv2,gbim_wv_zctas_v1

=== 3) Update docker-compose GIS_RAG_COLLECTIONS to real ZCTA name ===
GIS_RAG_COLLECTIONS=gbimwvcountiesv2,gbimwvtractsv2,gbimwvblockgroupsv2,gbim_wv_zctas_v1
1366:    - GIS_RAG_COLLECTIONS=gbimwvcountiesv2,gbimwvtractsv2,gbimwvblockgroupsv2,gbim_wv_zctas_v1

=== 4) Align runtime manifest physical_collection_name to real Chroma name ===
UPDATE 1
 logical_collection_name | physical_collection_name |        collection_version_id         |           permitted_use           
-------------------------+--------------------------+--------------------------------------+-----------------------------------
 gbim_wv_zctas           | gbim_wv_zctas_v1         | 49e820bd-4f9b-42f6-a7fb-2f36e22f82e0 | public_civic_geographic_retrieval
(1 row)


=== 5) Align host-side manifest physical_collection_name to real Chroma name ===
UPDATE 1
 logical_collection_name | physical_collection_name |        collection_version_id         |           permitted_use           
-------------------------+--------------------------+--------------------------------------+-----------------------------------
 gbim_wv_zctas           | gbim_wv_zctas_v1         | 49e820bd-4f9b-42f6-a7fb-2f36e22f82e0 | public_civic_geographic_retrieval
(1 row)


=== 6) Add verified promotion events for active WV counties, tracts, blockgroups in runtime DB ===
INSERT 0 3
   collection_name   |        collection_version_id         |          promotion_event_id          | signature_valid | coherence_ok 
---------------------+--------------------------------------+--------------------------------------+-----------------+--------------
 gbim_wv_blockgroups | 4c6638de-274d-485c-bb64-ab078426a5a5 | 16087c63-865f-4367-9f32-eaf6dd73131c | t               | t
 gbim_wv_counties    | f43b510a-12d5-4855-a203-65a2690ae6b0 | 71d22018-cf52-4fb6-a421-66163ec7bb6b | t               | t
 gbim_wv_tracts      | fcac67c8-1ece-4f13-a18b-9e21809e8188 | a60c31fb-9b3e-4ebb-afaf-d8eb4896d461 | t               | t
(3 rows)


=== 7) Backfill permitted_use in runtime manifest now that promotion events exist ===
UPDATE 3
 logical_collection_name | physical_collection_name |        collection_version_id         |           permitted_use           
-------------------------+--------------------------+--------------------------------------+-----------------------------------
 gbim_wv_blockgroups     | gbimwvblockgroupsv2      | 59ad7b32-2d88-4578-9e57-7c883f44a720 | public_civic_geographic_retrieval
 gbim_wv_counties        | gbimwvcountiesv2         | f43b510a-12d5-4855-a203-65a2690ae6b0 | public_civic_geographic_retrieval
 gbim_wv_tracts          | gbimwvtractsv2           | fcac67c8-1ece-4f13-a18b-9e21809e8188 | public_civic_geographic_retrieval
 gbim_wv_zctas           | gbim_wv_zctas_v1         | 49e820bd-4f9b-42f6-a7fb-2f36e22f82e0 | public_civic_geographic_retrieval
(4 rows)


=== 8) Recreate GIS-RAG with updated env ===
[+] up 77/77
 ✔ Container 687596ae0eb1_llm22-proxy                   Running          0.0s
 ✔ Container jarvis-agents-service                      Running          0.0s
 ✔ Container jarvis-brain-orchestrator                  Running          0.0s
 ✔ Container jarvis-chroma                              Running          0.0s
 ✔ Container jarvis-msjarvis-db                         Running          0.0s
 ✔ Container jarvis-neurobiological-master              Running          0.0s
 ✔ Container jarvis-gis-rag-tls                         Running          0.0s
 ✔ Container jarvis-intake-service                      Running          0.0s
 ✔ Container 1e1783a0cae3_jarvis-temporal-consciousness Running          0.0s
 ✔ Container jarvis-semaphore                           Running          0.0s
 ✔ Container jarvis-pia-sampler                         Running          0.0s
 ✔ Container jarvis-eeg-beta                            Running          0.0s
 ✔ Container jarvis-nbb-i-containers-2                  Running          0.0s
 ✔ Container jarvis-gbim-query-router                   Running          0.0s
 ✔ Container jarvis-provenance                          Running          0.0s
 ✔ Container neo4j                                      Running          0.0s
 ✔ Container 22cb4468dbd5_llm8-proxy                    Running          0.0s
 ✔ Container jarvis-consciousness-bridge                Running          0.0s
 ✔ Container ms-allis-internal-sandbox                  Running          0.0s
 ✔ Container nbb_pituitary_gland                        Running          0.0s
 ✔ Container c68db82137f8_llm9-proxy                    Running          0.0s
 ... 56 more                                                                 
GIS_RAG_COLLECTIONS=gbimwvcountiesv2,gbimwvtractsv2,gbimwvblockgroupsv2,gbim_wv_zctas_v1

=== 9) GIS-RAG health ===
{
    "status": "healthy",
    "service": "gis_rag",
    "embed_model": "all-minilm:latest",
    "collections": [
        "gbimwvcountiesv2",
        "gbimwvtractsv2",
        "gbimwvblockgroupsv2",
        "gbim_wv_zctas_v1"
    ],
    "chroma_host": "jarvis-chroma",
    "chroma_port": 8000
}

=== 10) Verify direct ZCTA collection visibility inside Chroma ===
{'collection': 'gbim_wv_zctas_v1', 'count': 741}

=== 11) Query GIS-RAG for ZCTA retrieval ===
{"hits":[{"text":"Census tract 54017965100 is a governed 2020 Census tract in Doddridge County, West Virginia, county GEOID 54017. Governed snapshot version wv-tract-snapshot-v2. Block-group count: 0. Block-group coverage state: unknown. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.","collection_name":"gbimwvtractsv2","document_id":"92965a51a7be9f1dabacd35ee9f2a84e5a9b0cb72a8015be6a7312030147df54","distance":0.566646933555603,"layer_name":null,"name":"Doddridge","lat":null,"lon":null,"metadata":{"address_point_count":0,"address_point_coverage_state":"unknown","bbox_max_lat":39.39546499999999,"bbox_max_lon":-80.683154,"bbox_min_lat":39.14524199999999,"bbox_min_lon":-80.91384,"belief_hash":"92965a51a7be9f1dabacd35ee9f2a84e5a9b0cb72a8015be6a7312030147df54","blockgroup_count":0,"blockgroup_coverage_state":"unknown","canonical_county_id":"54017","canonical_tract_id":"1400000US54017965100","centroid_lat":39.27037499999999,"centroid_lon":-80.82956239378836,"county_geoid":"54017","county_name":"Doddridge","dfirm_polygon_count":0,"dfirm_polygon_coverage_state":"unknown","embedding_model":"all-minilm:latest","entity_type":"census_tract","metadata_crs":"EPSG:4326","physical_collection":"gbimwvtractsv2","publication_source_view":"public.wv_tract_belief_vector_ready_v2","snapshot_version":"wv-tract-snapshot-v2","source_crs":"EPSG:26917","source_feature_id":306,"source_table":"public.wv_censustracts_census_2020_utm83","tract_geoid":"54017965100","verification_state":"derived"}},{"text":"Census tract 54043955401 is a governed 2020 Census tract in Lincoln County, West Virginia, county GEOID 54043. Governed snapshot version wv-tract-snapshot-v2. Block-group count: 0. Block-group coverage state: unknown. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.","collection_name":"gbimwvtractsv2","document_id":"53d638a1ff09c88059c2292dad2074782d1cc8d5e655082c78566c205c95c8bf","distance":0.5714752674102783,"layer_name":null,"name":"Lincoln","lat":null,"lon":null,"metadata":{"address_point_count":0,"address_point_coverage_state":"unknown","bbox_max_lat":38.325596999999995,"bbox_max_lon":-81.801464,"bbox_min_lat":38.16143699999999,"bbox_min_lon":-81.92208,"belief_hash":"53d638a1ff09c88059c2292dad2074782d1cc8d5e655082c78566c205c95c8bf","blockgroup_count":0,"blockgroup_coverage_state":"unknown","canonical_county_id":"54043","canonical_tract_id":"1400000US54043955401","centroid_lat":38.24350799999999,"centroid_lon":-81.85346676788731,"county_geoid":"54043","county_name":"Lincoln","dfirm_polygon_count":0,"dfirm_polygon_coverage_state":"unknown","embedding_model":"all-minilm:latest","entity_type":"census_tract","metadata_crs":"EPSG:4326","physical_collection":"gbimwvtractsv2","publication_source_view":"public.wv_tract_belief_vector_ready_v2","snapshot_version":"wv-tract-snapshot-v2","source_crs":"EPSG:26917","source_feature_id":92,"source_table":"public.wv_censustracts_census_2020_utm83","tract_geoid":"54043955401","verification_state":"derived"}},{"text":"Census tract 54043955500 is a governed 2020 Census tract in Lincoln County, West Virginia, county GEOID 54043. Governed snapshot version wv-tract-snapshot-v2. Block-group count: 0. Block-group coverage state: unknown. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.","collection_name":"gbimwvtractsv2","document_id":"a5886a5094c3d89a440fc51ef684cbcaf779983c766a14f1c477eaf884b226a4","distance":0.5725570917129517,"layer_name":null,"name":"Lincoln","lat":null,"lon":null,"metadata":{"address_point_count":0,"address_point_coverage_state":"unknown","bbox_max_lat":38.37677999999998,"bbox_max_lon":-81.997406,"bbox_min_lat":38.204138,"bbox_min_lon":-82.16907500000002,"belief_hash":"a5886a5094c3d89a440fc51ef684cbcaf779983c766a14f1c477eaf884b226a4","blockgroup_count":0,"blockgroup_coverage_state":"unknown","canonical_county_id":"54043","canonical_tract_id":"1400000US54043955500","centroid_lat":38.290443499999995,"centroid_lon":-82.10573672879778,"county_geoid":"54043","county_name":"Lincoln","dfirm_polygon_count":0,"dfirm_polygon_coverage_state":"unknown","embedding_model":"all-minilm:latest","entity_type":"census_tract","metadata_crs":"EPSG:4326","physical_collection":"gbimwvtractsv2","publication_source_view":"public.wv_tract_belief_vector_ready_v2","snapshot_version":"wv-tract-snapshot-v2","source_crs":"EPSG:26917","source_feature_id":386,"source_table":"public.wv_censustracts_census_2020_utm83","tract_geoid":"54043955500","verification_state":"derived"}},{"text":"Census tract 54017965000 is a governed 2020 Census tract in Doddridge County, West Virginia, county GEOID 54017. Governed snapshot version wv-tract-snapshot-v2. Block-group count: 0. Block-group coverage state: unknown. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.","collection_name":"gbimwvtractsv2","document_id":"c7c37663587abe6a0e0591a0fbf2d5f469453c1cd6b1966fe0591d5590e9e90b","distance":0.5727807879447937,"layer_name":null,"name":"Doddridge","lat":null,"lon":null,"metadata":{"address_point_count":0,"address_point_coverage_state":"unknown","bbox_max_lat":39.45141499999998,"bbox_max_lon":-80.525644,"bbox_min_lat":39.09027799999999,"bbox_min_lon":-80.839919,"belief_hash":"c7c37663587abe6a0e0591a0fbf2d5f469453c1cd6b1966fe0591d5590e9e90b","blockgroup_count":0,"blockgroup_coverage_state":"unknown","canonical_county_id":"54017","canonical_tract_id":"1400000US54017965000","centroid_lat":39.270841999999995,"centroid_lon":-80.66248840415103,"county_geoid":"54017","county_name":"Doddridge","dfirm_polygon_count":0,"dfirm_polygon_coverage_state":"unknown","embedding_model":"all-minilm:latest","entity_type":"census_tract","metadata_crs":"EPSG:4326","physical_collection":"gbimwvtractsv2","publication_source_view":"public.wv_tract_belief_vector_ready_v2","snapshot_version":"wv-tract-snapshot-v2","source_crs":"EPSG:26917","source_feature_id":307,"source_table":"public.wv_censustracts_census_2020_utm83","tract_geoid":"54017965000","verification_state":"derived"}},{"text":"Census tract 54043955402 is a governed 2020 Census tract in Lincoln County, West Virginia, county GEOID 54043. Governed snapshot version wv-tract-snapshot-v2. Block-group count: 0. Block-group coverage state: unknown. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.","collection_name":"gbimwvtractsv2","document_id":"8e578616a8f4704928d758d17e90607c75d213fe451768b1eb23628dbb7defb2","distance":0.5788745880126953,"layer_name":null,"name":"Lincoln","lat":null,"lon":null,"metadata":{"address_point_count":0,"address_point_coverage_state":"unknown","bbox_max_lat":38.320589999999996,"bbox_max_lon":-81.877052,"bbox_min_lat":38.13630199999999,"bbox_min_lon":-82.04064500000001,"belief_hash":"8e578616a8f4704928d758d17e90607c75d213fe451768b1eb23628dbb7defb2","blockgroup_count":0,"blockgroup_coverage_state":"unknown","canonical_county_id":"54043","canonical_tract_id":"1400000US54043955402","centroid_lat":38.228430999999986,"centroid_lon":-81.97148725644747,"county_geoid":"54043","county_name":"Lincoln","dfirm_polygon_count":0,"dfirm_polygon_coverage_state":"unknown","embedding_model":"all-minilm:latest","entity_type":"census_tract","metadata_crs":"EPSG:4326","physical_collection":"gbimwvtractsv2","publication_source_view":"public.wv_tract_belief_vector_ready_v2","snapshot_version":"wv-tract-snapshot-v2","source_crs":"EPSG:26917","source_feature_id":91,"source_table":"public.wv_censustracts_census_2020_utm83","tract_geoid":"54043955402","verification_state":"derived"}},{"text":"Census tract 54009031401 is a governed 2020 Census tract in Brooke County, West Virginia, county GEOID 54009. Governed snapshot version wv-tract-snapshot-v2. Block-group count: 0. Block-group coverage state: unknown. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.","collection_name":"gbimwvtractsv2","document_id":"4d8a95f778c46d5bd25386d1fa6c42d1ae9a0096b840ea8dc79f3334cc4fa519","distance":0.5815219879150391,"layer_name":null,"name":"Brooke","lat":null,"lon":null,"metadata":{"address_point_count":0,"address_point_coverage_state":"unknown","bbox_max_lat":40.297564,"bbox_max_lon":-80.60672,"bbox_min_lat":40.263524999999994,"bbox_min_lon":-80.618829,"belief_hash":"4d8a95f778c46d5bd25386d1fa6c42d1ae9a0096b840ea8dc79f3334cc4fa519","blockgroup_count":0,"blockgroup_coverage_state":"unknown","canonical_county_id":"54009","canonical_tract_id":"1400000US54009031401","centroid_lat":40.280613,"centroid_lon":-80.6120045340256,"county_geoid":"54009","county_name":"Brooke","dfirm_polygon_count":0,"dfirm_polygon_coverage_state":"unknown","embedding_model":"all-minilm:latest","entity_type":"census_tract","metadata_crs":"EPSG:4326","physical_collection":"gbimwvtractsv2","publication_source_view":"public.wv_tract_belief_vector_ready_v2","snapshot_version":"wv-tract-snapshot-v2","source_crs":"EPSG:26917","source_feature_id":55,"source_table":"public.wv_censustracts_census_2020_utm83","tract_geoid":"54009031401","verification_state":"derived"}},{"text":"Census tract 54023969500 is a governed 2020 Census tract in Grant County, West Virginia, county GEOID 54023. Governed snapshot version wv-tract-snapshot-v2. Block-group count: 0. Block-group coverage state: unknown. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.","collection_name":"gbimwvtractsv2","document_id":"de9409a31dac037d94af576c6964074c831fa8a45040b85d92def23fc2cde4b8","distance":0.5822997093200684,"layer_name":null,"name":"Grant","lat":null,"lon":null,"metadata":{"address_point_count":0,"address_point_coverage_state":"unknown","bbox_max_lat":39.15495731268632,"bbox_max_lon":-79.05684762685486,"bbox_min_lat":38.8686729582898,"bbox_min_lon":-79.35766608461152,"belief_hash":"de9409a31dac037d94af576c6964074c831fa8a45040b85d92def23fc2cde4b8","blockgroup_count":0,"blockgroup_coverage_state":"unknown","canonical_county_id":"54023","canonical_tract_id":"1400000US54023969500","centroid_lat":39.01177023356148,"centroid_lon":-79.17254317696427,"county_geoid":"54023","county_name":"Grant","dfirm_polygon_count":0,"dfirm_polygon_coverage_state":"unknown","embedding_model":"all-minilm:latest","entity_type":"census_tract","metadata_crs":"EPSG:4326","physical_collection":"gbimwvtractsv2","publication_source_view":"public.wv_tract_belief_vector_ready_v2","snapshot_version":"wv-tract-snapshot-v2","source_crs":"EPSG:26917","source_feature_id":106,"source_table":"public.wv_censustracts_census_2020_utm83","tract_geoid":"54023969500","verification_state":"derived"}},{"text":"Census tract 54043955800 is a governed 2020 Census tract in Lincoln County, West Virginia, county GEOID 54043. Governed snapshot version wv-tract-snapshot-v2. Block-group count: 0. Block-group coverage state: unknown. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.","collection_name":"gbimwvtractsv2","document_id":"a5d4579134f7b5ef044865d196eb489069e43f762181c130188239dcb62d14b8","distance":0.5826345682144165,"layer_name":null,"name":"Lincoln","lat":null,"lon":null,"metadata":{"address_point_count":0,"address_point_coverage_state":"unknown","bbox_max_lat":38.278193,"bbox_max_lon":-81.90516,"bbox_min_lat":38.01866299999999,"bbox_min_lon":-82.20557100000003,"belief_hash":"a5d4579134f7b5ef044865d196eb489069e43f762181c130188239dcb62d14b8","blockgroup_count":0,"blockgroup_coverage_state":"unknown","canonical_county_id":"54043","canonical_tract_id":"1400000US54043955800","centroid_lat":38.14828549999999,"centroid_lon":-82.06765251447877,"county_geoid":"54043","county_name":"Lincoln","dfirm_polygon_count":0,"dfirm_polygon_coverage_state":"unknown","embedding_model":"all-minilm:latest","entity_type":"census_tract","metadata_crs":"EPSG:4326","physical_collection":"gbimwvtractsv2","publication_source_view":"public.wv_tract_belief_vector_ready_v2","snapshot_version":"wv-tract-snapshot-v2","source_crs":"EPSG:26917","source_feature_id":385,"source_table":"public.wv_censustracts_census_2020_utm83","tract_geoid":"54043955800","verification_state":"derived"}},{"text":"Census tract 54023969400 is a governed 2020 Census tract in Grant County, West Virginia, county GEOID 54023. Governed snapshot version wv-tract-snapshot-v2. Block-group count: 0. Block-group coverage state: unknown. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.","collection_name":"gbimwvtractsv2","document_id":"b108de8e84e04b77e617652bb8bf6d48cc6805bc739935247c77060e1dc1b015","distance":0.5827555656433105,"layer_name":null,"name":"Grant","lat":null,"lon":null,"metadata":{"address_point_count":0,"address_point_coverage_state":"unknown","bbox_max_lat":39.32799781955305,"bbox_max_lon":-78.97989707529561,"bbox_min_lat":38.964940903614114,"bbox_min_lon":-79.48717443524387,"belief_hash":"b108de8e84e04b77e617652bb8bf6d48cc6805bc739935247c77060e1dc1b015","blockgroup_count":0,"blockgroup_coverage_state":"unknown","canonical_county_id":"54023","canonical_tract_id":"1400000US54023969400","centroid_lat":39.1465008340427,"centroid_lon":-79.26106885988848,"county_geoid":"54023","county_name":"Grant","dfirm_polygon_count":0,"dfirm_polygon_coverage_state":"unknown","embedding_model":"all-minilm:latest","entity_type":"census_tract","metadata_crs":"EPSG:4326","physical_collection":"gbimwvtractsv2","publication_source_view":"public.wv_tract_belief_vector_ready_v2","snapshot_version":"wv-tract-snapshot-v2","source_crs":"EPSG:26917","source_feature_id":108,"source_table":"public.wv_censustracts_census_2020_utm83","tract_geoid":"54023969400","verification_state":"derived"}},{"text":"Census tract 54043955600 is a governed 2020 Census tract in Lincoln County, West Virginia, county GEOID 54043. Governed snapshot version wv-tract-snapshot-v2. Block-group count: 0. Block-group coverage state: unknown. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.","collection_name":"gbimwvtractsv2","document_id":"2fa76cecd9d5c8427e813a01e107b5cb476532d474fdfb02eee53ebd6d812958","distance":0.5833310484886169,"layer_name":null,"name":"Lincoln","lat":null,"lon":null,"metadata":{"address_point_count":0,"address_point_coverage_state":"unknown","bbox_max_lat":38.33978699999999,"bbox_max_lon":-82.15138800000001,"bbox_min_lat":38.086716,"bbox_min_lon":-82.28626600000004,"belief_hash":"2fa76cecd9d5c8427e813a01e107b5cb476532d474fdfb02eee53ebd6d812958","blockgroup_count":0,"blockgroup_coverage_state":"unknown","canonical_county_id":"54043","canonical_tract_id":"1400000US54043955600","centroid_lat":38.21329299999999,"centroid_lon":-82.22854808597886,"county_geoid":"54043","county_name":"Lincoln","dfirm_polygon_count":0,"dfirm_polygon_coverage_state":"unknown","embedding_model":"all-minilm:latest","entity_type":"census_tract","metadata_crs":"EPSG:4326","physical_collection":"gbimwvtractsv2","publication_source_view":"public.wv_tract_belief_vector_ready_v2","snapshot_version":"wv-tract-snapshot-v2","source_crs":"EPSG:26917","source_feature_id":387,"source_table":"public.wv_censustracts_census_2020_utm83","tract_geoid":"54043955600","verification_state":"derived"}}]}
{
    "hits": [
        {
            "text": "Census tract 54017965100 is a governed 2020 Census tract in Doddridge County, West Virginia, county GEOID 54017. Governed snapshot version wv-tract-snapshot-v2. Block-group count: 0. Block-group coverage state: unknown. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.",
            "collection_name": "gbimwvtractsv2",
            "document_id": "92965a51a7be9f1dabacd35ee9f2a84e5a9b0cb72a8015be6a7312030147df54",
            "distance": 0.566646933555603,
            "layer_name": null,
            "name": "Doddridge",
            "lat": null,
            "lon": null,
            "metadata": {
                "address_point_count": 0,
                "address_point_coverage_state": "unknown",
                "bbox_max_lat": 39.39546499999999,
                "bbox_max_lon": -80.683154,
                "bbox_min_lat": 39.14524199999999,
                "bbox_min_lon": -80.91384,
                "belief_hash": "92965a51a7be9f1dabacd35ee9f2a84e5a9b0cb72a8015be6a7312030147df54",
                "blockgroup_count": 0,
                "blockgroup_coverage_state": "unknown",
                "canonical_county_id": "54017",
                "canonical_tract_id": "1400000US54017965100",
                "centroid_lat": 39.27037499999999,
                "centroid_lon": -80.82956239378836,
                "county_geoid": "54017",
                "county_name": "Doddridge",
                "dfirm_polygon_count": 0,
                "dfirm_polygon_coverage_state": "unknown",
                "embedding_model": "all-minilm:latest",
                "entity_type": "census_tract",
                "metadata_crs": "EPSG:4326",
                "physical_collection": "gbimwvtractsv2",
                "publication_source_view": "public.wv_tract_belief_vector_ready_v2",
                "snapshot_version": "wv-tract-snapshot-v2",
                "source_crs": "EPSG:26917",
                "source_feature_id": 306,
                "source_table": "public.wv_censustracts_census_2020_utm83",
                "tract_geoid": "54017965100",
                "verification_state": "derived"
            }
        },
        {
            "text": "Census tract 54043955401 is a governed 2020 Census tract in Lincoln County, West Virginia, county GEOID 54043. Governed snapshot version wv-tract-snapshot-v2. Block-group count: 0. Block-group coverage state: unknown. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.",
            "collection_name": "gbimwvtractsv2",
            "document_id": "53d638a1ff09c88059c2292dad2074782d1cc8d5e655082c78566c205c95c8bf",
            "distance": 0.5714752674102783,
            "layer_name": null,
            "name": "Lincoln",
            "lat": null,
            "lon": null,
            "metadata": {
                "address_point_count": 0,
                "address_point_coverage_state": "unknown",
                "bbox_max_lat": 38.325596999999995,
                "bbox_max_lon": -81.801464,
                "bbox_min_lat": 38.16143699999999,
                "bbox_min_lon": -81.92208,
                "belief_hash": "53d638a1ff09c88059c2292dad2074782d1cc8d5e655082c78566c205c95c8bf",
                "blockgroup_count": 0,
                "blockgroup_coverage_state": "unknown",
                "canonical_county_id": "54043",
                "canonical_tract_id": "1400000US54043955401",
                "centroid_lat": 38.24350799999999,
                "centroid_lon": -81.85346676788731,
                "county_geoid": "54043",
                "county_name": "Lincoln",
                "dfirm_polygon_count": 0,
                "dfirm_polygon_coverage_state": "unknown",
                "embedding_model": "all-minilm:latest",
                "entity_type": "census_tract",
                "metadata_crs": "EPSG:4326",
                "physical_collection": "gbimwvtractsv2",
                "publication_source_view": "public.wv_tract_belief_vector_ready_v2",
                "snapshot_version": "wv-tract-snapshot-v2",
                "source_crs": "EPSG:26917",
                "source_feature_id": 92,
                "source_table": "public.wv_censustracts_census_2020_utm83",
                "tract_geoid": "54043955401",
                "verification_state": "derived"
            }
        },
        {
            "text": "Census tract 54043955500 is a governed 2020 Census tract in Lincoln County, West Virginia, county GEOID 54043. Governed snapshot version wv-tract-snapshot-v2. Block-group count: 0. Block-group coverage state: unknown. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.",
            "collection_name": "gbimwvtractsv2",
            "document_id": "a5886a5094c3d89a440fc51ef684cbcaf779983c766a14f1c477eaf884b226a4",
            "distance": 0.5725570917129517,
            "layer_name": null,
            "name": "Lincoln",
            "lat": null,
            "lon": null,
            "metadata": {
                "address_point_count": 0,
                "address_point_coverage_state": "unknown",
                "bbox_max_lat": 38.37677999999998,
                "bbox_max_lon": -81.997406,
                "bbox_min_lat": 38.204138,
                "bbox_min_lon": -82.16907500000002,
                "belief_hash": "a5886a5094c3d89a440fc51ef684cbcaf779983c766a14f1c477eaf884b226a4",
                "blockgroup_count": 0,
                "blockgroup_coverage_state": "unknown",
                "canonical_county_id": "54043",
                "canonical_tract_id": "1400000US54043955500",
                "centroid_lat": 38.290443499999995,
                "centroid_lon": -82.10573672879778,
                "county_geoid": "54043",
                "county_name": "Lincoln",
                "dfirm_polygon_count": 0,
                "dfirm_polygon_coverage_state": "unknown",
                "embedding_model": "all-minilm:latest",
                "entity_type": "census_tract",
                "metadata_crs": "EPSG:4326",
                "physical_collection": "gbimwvtractsv2",
                "publication_source_view": "public.wv_tract_belief_vector_ready_v2",
                "snapshot_version": "wv-tract-snapshot-v2",
                "source_crs": "EPSG:26917",
                "source_feature_id": 386,
                "source_table": "public.wv_censustracts_census_2020_utm83",
                "tract_geoid": "54043955500",
                "verification_state": "derived"
            }
        },
        {
            "text": "Census tract 54017965000 is a governed 2020 Census tract in Doddridge County, West Virginia, county GEOID 54017. Governed snapshot version wv-tract-snapshot-v2. Block-group count: 0. Block-group coverage state: unknown. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.",
            "collection_name": "gbimwvtractsv2",
            "document_id": "c7c37663587abe6a0e0591a0fbf2d5f469453c1cd6b1966fe0591d5590e9e90b",
            "distance": 0.5727807879447937,
            "layer_name": null,
            "name": "Doddridge",
            "lat": null,
            "lon": null,
            "metadata": {
                "address_point_count": 0,
                "address_point_coverage_state": "unknown",
                "bbox_max_lat": 39.45141499999998,
                "bbox_max_lon": -80.525644,
                "bbox_min_lat": 39.09027799999999,
                "bbox_min_lon": -80.839919,
                "belief_hash": "c7c37663587abe6a0e0591a0fbf2d5f469453c1cd6b1966fe0591d5590e9e90b",
                "blockgroup_count": 0,
                "blockgroup_coverage_state": "unknown",
                "canonical_county_id": "54017",
                "canonical_tract_id": "1400000US54017965000",
                "centroid_lat": 39.270841999999995,
                "centroid_lon": -80.66248840415103,
                "county_geoid": "54017",
                "county_name": "Doddridge",
                "dfirm_polygon_count": 0,
                "dfirm_polygon_coverage_state": "unknown",
                "embedding_model": "all-minilm:latest",
                "entity_type": "census_tract",
                "metadata_crs": "EPSG:4326",
                "physical_collection": "gbimwvtractsv2",
                "publication_source_view": "public.wv_tract_belief_vector_ready_v2",
                "snapshot_version": "wv-tract-snapshot-v2",
                "source_crs": "EPSG:26917",
                "source_feature_id": 307,
                "source_table": "public.wv_censustracts_census_2020_utm83",
                "tract_geoid": "54017965000",
                "verification_state": "derived"
            }
        },
        {
            "text": "Census tract 54043955402 is a governed 2020 Census tract in Lincoln County, West Virginia, county GEOID 54043. Governed snapshot version wv-tract-snapshot-v2. Block-group count: 0. Block-group coverage state: unknown. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.",
            "collection_name": "gbimwvtractsv2",
            "document_id": "8e578616a8f4704928d758d17e90607c75d213fe451768b1eb23628dbb7defb2",
            "distance": 0.5788745880126953,
            "layer_name": null,
            "name": "Lincoln",
            "lat": null,
            "lon": null,
            "metadata": {
                "address_point_count": 0,
                "address_point_coverage_state": "unknown",
                "bbox_max_lat": 38.320589999999996,
                "bbox_max_lon": -81.877052,
                "bbox_min_lat": 38.13630199999999,
                "bbox_min_lon": -82.04064500000001,
                "belief_hash": "8e578616a8f4704928d758d17e90607c75d213fe451768b1eb23628dbb7defb2",
                "blockgroup_count": 0,
                "blockgroup_coverage_state": "unknown",
                "canonical_county_id": "54043",
                "canonical_tract_id": "1400000US54043955402",
                "centroid_lat": 38.228430999999986,
                "centroid_lon": -81.97148725644747,
                "county_geoid": "54043",
                "county_name": "Lincoln",
                "dfirm_polygon_count": 0,
                "dfirm_polygon_coverage_state": "unknown",
                "embedding_model": "all-minilm:latest",
                "entity_type": "census_tract",
                "metadata_crs": "EPSG:4326",
                "physical_collection": "gbimwvtractsv2",
                "publication_source_view": "public.wv_tract_belief_vector_ready_v2",
                "snapshot_version": "wv-tract-snapshot-v2",
                "source_crs": "EPSG:26917",
                "source_feature_id": 91,
                "source_table": "public.wv_censustracts_census_2020_utm83",
                "tract_geoid": "54043955402",
                "verification_state": "derived"
            }
        },
        {
            "text": "Census tract 54009031401 is a governed 2020 Census tract in Brooke County, West Virginia, county GEOID 54009. Governed snapshot version wv-tract-snapshot-v2. Block-group count: 0. Block-group coverage state: unknown. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.",
            "collection_name": "gbimwvtractsv2",
            "document_id": "4d8a95f778c46d5bd25386d1fa6c42d1ae9a0096b840ea8dc79f3334cc4fa519",
            "distance": 0.5815219879150391,
            "layer_name": null,
            "name": "Brooke",
            "lat": null,
            "lon": null,
            "metadata": {
                "address_point_count": 0,
                "address_point_coverage_state": "unknown",
                "bbox_max_lat": 40.297564,
                "bbox_max_lon": -80.60672,
                "bbox_min_lat": 40.263524999999994,
                "bbox_min_lon": -80.618829,
                "belief_hash": "4d8a95f778c46d5bd25386d1fa6c42d1ae9a0096b840ea8dc79f3334cc4fa519",
                "blockgroup_count": 0,
                "blockgroup_coverage_state": "unknown",
                "canonical_county_id": "54009",
                "canonical_tract_id": "1400000US54009031401",
                "centroid_lat": 40.280613,
                "centroid_lon": -80.6120045340256,
                "county_geoid": "54009",
                "county_name": "Brooke",
                "dfirm_polygon_count": 0,
                "dfirm_polygon_coverage_state": "unknown",
                "embedding_model": "all-minilm:latest",
                "entity_type": "census_tract",
                "metadata_crs": "EPSG:4326",
                "physical_collection": "gbimwvtractsv2",
                "publication_source_view": "public.wv_tract_belief_vector_ready_v2",
                "snapshot_version": "wv-tract-snapshot-v2",
                "source_crs": "EPSG:26917",
                "source_feature_id": 55,
                "source_table": "public.wv_censustracts_census_2020_utm83",
                "tract_geoid": "54009031401",
                "verification_state": "derived"
            }
        },
        {
            "text": "Census tract 54023969500 is a governed 2020 Census tract in Grant County, West Virginia, county GEOID 54023. Governed snapshot version wv-tract-snapshot-v2. Block-group count: 0. Block-group coverage state: unknown. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.",
            "collection_name": "gbimwvtractsv2",
            "document_id": "de9409a31dac037d94af576c6964074c831fa8a45040b85d92def23fc2cde4b8",
            "distance": 0.5822997093200684,
            "layer_name": null,
            "name": "Grant",
            "lat": null,
            "lon": null,
            "metadata": {
                "address_point_count": 0,
                "address_point_coverage_state": "unknown",
                "bbox_max_lat": 39.15495731268632,
                "bbox_max_lon": -79.05684762685486,
                "bbox_min_lat": 38.8686729582898,
                "bbox_min_lon": -79.35766608461152,
                "belief_hash": "de9409a31dac037d94af576c6964074c831fa8a45040b85d92def23fc2cde4b8",
                "blockgroup_count": 0,
                "blockgroup_coverage_state": "unknown",
                "canonical_county_id": "54023",
                "canonical_tract_id": "1400000US54023969500",
                "centroid_lat": 39.01177023356148,
                "centroid_lon": -79.17254317696427,
                "county_geoid": "54023",
                "county_name": "Grant",
                "dfirm_polygon_count": 0,
                "dfirm_polygon_coverage_state": "unknown",
                "embedding_model": "all-minilm:latest",
                "entity_type": "census_tract",
                "metadata_crs": "EPSG:4326",
                "physical_collection": "gbimwvtractsv2",
                "publication_source_view": "public.wv_tract_belief_vector_ready_v2",
                "snapshot_version": "wv-tract-snapshot-v2",
                "source_crs": "EPSG:26917",
                "source_feature_id": 106,
                "source_table": "public.wv_censustracts_census_2020_utm83",
                "tract_geoid": "54023969500",
                "verification_state": "derived"
            }
        },
        {
            "text": "Census tract 54043955800 is a governed 2020 Census tract in Lincoln County, West Virginia, county GEOID 54043. Governed snapshot version wv-tract-snapshot-v2. Block-group count: 0. Block-group coverage state: unknown. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.",
            "collection_name": "gbimwvtractsv2",
            "document_id": "a5d4579134f7b5ef044865d196eb489069e43f762181c130188239dcb62d14b8",
            "distance": 0.5826345682144165,
            "layer_name": null,
            "name": "Lincoln",
            "lat": null,
            "lon": null,
            "metadata": {
                "address_point_count": 0,
                "address_point_coverage_state": "unknown",
                "bbox_max_lat": 38.278193,
                "bbox_max_lon": -81.90516,
                "bbox_min_lat": 38.01866299999999,
                "bbox_min_lon": -82.20557100000003,
                "belief_hash": "a5d4579134f7b5ef044865d196eb489069e43f762181c130188239dcb62d14b8",
                "blockgroup_count": 0,
                "blockgroup_coverage_state": "unknown",
                "canonical_county_id": "54043",
                "canonical_tract_id": "1400000US54043955800",
                "centroid_lat": 38.14828549999999,
                "centroid_lon": -82.06765251447877,
                "county_geoid": "54043",
                "county_name": "Lincoln",
                "dfirm_polygon_count": 0,
                "dfirm_polygon_coverage_state": "unknown",
                "embedding_model": "all-minilm:latest",
                "entity_type": "census_tract",
                "metadata_crs": "EPSG:4326",
                "physical_collection": "gbimwvtractsv2",
                "publication_source_view": "public.wv_tract_belief_vector_ready_v2",
                "snapshot_version": "wv-tract-snapshot-v2",
                "source_crs": "EPSG:26917",
                "source_feature_id": 385,
                "source_table": "public.wv_censustracts_census_2020_utm83",
                "tract_geoid": "54043955800",
                "verification_state": "derived"
            }
        },
        {
            "text": "Census tract 54023969400 is a governed 2020 Census tract in Grant County, West Virginia, county GEOID 54023. Governed snapshot version wv-tract-snapshot-v2. Block-group count: 0. Block-group coverage state: unknown. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.",
            "collection_name": "gbimwvtractsv2",
            "document_id": "b108de8e84e04b77e617652bb8bf6d48cc6805bc739935247c77060e1dc1b015",
            "distance": 0.5827555656433105,
            "layer_name": null,
            "name": "Grant",
            "lat": null,
            "lon": null,
            "metadata": {
                "address_point_count": 0,
                "address_point_coverage_state": "unknown",
                "bbox_max_lat": 39.32799781955305,
                "bbox_max_lon": -78.97989707529561,
                "bbox_min_lat": 38.964940903614114,
                "bbox_min_lon": -79.48717443524387,
                "belief_hash": "b108de8e84e04b77e617652bb8bf6d48cc6805bc739935247c77060e1dc1b015",
                "blockgroup_count": 0,
                "blockgroup_coverage_state": "unknown",
                "canonical_county_id": "54023",
                "canonical_tract_id": "1400000US54023969400",
                "centroid_lat": 39.1465008340427,
                "centroid_lon": -79.26106885988848,
                "county_geoid": "54023",
                "county_name": "Grant",
                "dfirm_polygon_count": 0,
                "dfirm_polygon_coverage_state": "unknown",
                "embedding_model": "all-minilm:latest",
                "entity_type": "census_tract",
                "metadata_crs": "EPSG:4326",
                "physical_collection": "gbimwvtractsv2",
                "publication_source_view": "public.wv_tract_belief_vector_ready_v2",
                "snapshot_version": "wv-tract-snapshot-v2",
                "source_crs": "EPSG:26917",
                "source_feature_id": 108,
                "source_table": "public.wv_censustracts_census_2020_utm83",
                "tract_geoid": "54023969400",
                "verification_state": "derived"
            }
        },
        {
            "text": "Census tract 54043955600 is a governed 2020 Census tract in Lincoln County, West Virginia, county GEOID 54043. Governed snapshot version wv-tract-snapshot-v2. Block-group count: 0. Block-group coverage state: unknown. Address-point count: 0. Address-point coverage state: unknown. D-FIRM polygon count: 0. D-FIRM coverage state: unknown. A zero with unknown coverage must not be interpreted as verified absence.",
            "collection_name": "gbimwvtractsv2",
            "document_id": "2fa76cecd9d5c8427e813a01e107b5cb476532d474fdfb02eee53ebd6d812958",
            "distance": 0.5833310484886169,
            "layer_name": null,
            "name": "Lincoln",
            "lat": null,
            "lon": null,
            "metadata": {
                "address_point_count": 0,
                "address_point_coverage_state": "unknown",
                "bbox_max_lat": 38.33978699999999,
                "bbox_max_lon": -82.15138800000001,
                "bbox_min_lat": 38.086716,
                "bbox_min_lon": -82.28626600000004,
                "belief_hash": "2fa76cecd9d5c8427e813a01e107b5cb476532d474fdfb02eee53ebd6d812958",
                "blockgroup_count": 0,
                "blockgroup_coverage_state": "unknown",
                "canonical_county_id": "54043",
                "canonical_tract_id": "1400000US54043955600",
                "centroid_lat": 38.21329299999999,
                "centroid_lon": -82.22854808597886,
                "county_geoid": "54043",
                "county_name": "Lincoln",
                "dfirm_polygon_count": 0,
                "dfirm_polygon_coverage_state": "unknown",
                "embedding_model": "all-minilm:latest",
                "entity_type": "census_tract",
                "metadata_crs": "EPSG:4326",
                "physical_collection": "gbimwvtractsv2",
                "publication_source_view": "public.wv_tract_belief_vector_ready_v2",
                "snapshot_version": "wv-tract-snapshot-v2",
                "source_crs": "EPSG:26917",
                "source_feature_id": 387,
                "source_table": "public.wv_censustracts_census_2020_utm83",
                "tract_geoid": "54043955600",
                "verification_state": "derived"
            }
        }
    ]
}

=== 12) Summarize returned collections ===
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "/usr/lib/python3.12/json/__init__.py", line 293, in load
    return loads(fp.read(),
           ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/msjarvis-rebuild$ 

