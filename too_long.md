              ^
(.venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ # See the exact table name and query the login function uses
grep -n "SELECT\|users\|login\|password\|TABLE\|FROM\|ms_user_profile\|founder_tokens" \
  /opt/msjarvis-rebuild/auth_api.py | head -40
5:  GET  /login          — magic link token handler → sets cookie → redirect
187:@app.get("/login")
188:def login(token: str, response: Response):
(.venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ # Check ms_user_profile for your username
docker exec jarvis-local-resources-db psql -U postgres -d local_resources \
  -c "SELECT * FROM ms_user_profile LIMIT 5;"

# Check founder_tokens
docker exec jarvis-local-resources-db psql -U postgres -d local_resources \
  -c "SELECT * FROM founder_tokens LIMIT 5;"

# Check ueid_immutable_security
docker exec jarvis-local-resources-db psql -U postgres -d local_resources \
  -c "\d ueid_immutable_security"
docker exec jarvis-local-resources-db psql -U postgres -d local_resources \
  -c "SELECT * FROM ueid_immutable_security LIMIT 3;"
     user_id     | display_name |          created_at           | rank  | is_groundbreaker |        rank_updated_at        | first_activity_at | tenure_days | bsa_flag | bsa_warn_threshold | bsa_hard_cap | pms_blocked | kyc_tier | can_vote | can_cosponsor | can_stand_steward |     governance_updated_at     
-----------------+--------------+-------------------------------+-------+------------------+-------------------------------+-------------------+-------------+----------+--------------------+--------------+-------------+----------+----------+---------------+-------------------+-------------------------------
 MS-FOUNDER-0001 | Carrie Kidd  | 2026-05-28 22:35:48.890905+00 | elder | t                | 2026-05-28 22:35:48.890905+00 |                   |           0 | t        |             200.00 |       400.00 | f           |        3 | t        | t             | t                 | 2026-05-28 22:35:48.890905+00
(1 row)

 serial_number |            ueid            | minted_by | cohort  |  allocation_type   |           minted_at           
---------------+----------------------------+-----------+---------+--------------------+-------------------------------
             2 | MS-JARVIS-03230A7CD30E4BBE | cakidd    | phase_0 | red_team           | 2026-05-28 23:08:14.566943+00
             1 | MS-JARVIS-FC2383781EA2EF74 | cakidd    | phase_0 | founding_architect | 2025-03-23 00:00:00+00
(2 rows)

                             Table "public.ueid_immutable_security"
    Column     |           Type           | Collation | Nullable |           Default            
---------------+--------------------------+-----------+----------+------------------------------
 ueid          | character varying(64)    |           | not null | 
 entity_type   | character varying(32)    |           | not null | 'founder'::character varying
 entity_name   | text                     |           |          | 
 created_at    | timestamp with time zone |           | not null | now()
 metadata_json | jsonb                    |           | not null | '{}'::jsonb
Indexes:
    "ueid_immutable_security_pkey" PRIMARY KEY, btree (ueid)
Check constraints:
    "ueid_format" CHECK (ueid::text ~ '^MS-[A-Z0-9-]+$'::text)
Referenced by:
    TABLE "mountainshares_ledger" CONSTRAINT "mountainshares_ledger_ueid_fkey" FOREIGN KEY (ueid) REFERENCES ueid_immutable_security(ueid) ON DELETE RESTRICT DEFERRABLE INITIALLY DEFERRED
    TABLE "ms_user_profile" CONSTRAINT "ms_user_profile_user_id_fkey" FOREIGN KEY (user_id) REFERENCES ueid_immutable_security(ueid) ON DELETE RESTRICT DEFERRABLE INITIALLY DEFERRED

            ueid            |   entity_type   | entity_name |          created_at           |                                                                                           metadata_json                                                                                            
----------------------------+-----------------+-------------+-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 MS-FOUNDER-0001            | founder         | Carrie Kidd | 2026-05-28 22:35:41.422638+00 | {"org": "Kidd's Technical Services, LLC", "role": "founder", "email": "kiddstechnical@gmail.com", "is_groundbreaker": true}
 MS-JARVIS-03230A7CD30E4BBE | county_champion | Taryn Moser | 2026-05-28 23:08:14.566943+00 | {"county": "Fayette", "source": "manual_backfill", "enrolled_by": "cakidd", "public_uuid": "2bd130ec-0970-4e97-9337-a42e866e0157", "wallet_address": "0x366F88Eb5ac95D4e32662fAb1Ed4F0C463215E26"}
 MS-JARVIS-FC2383781EA2EF74 | founder         | Carrie Kidd | 2025-03-23 00:00:00+00        | {}
(3 rows)

(.venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ # Test all 4 GIS-adjacent Chroma collections
for id in 77393847-dfe0-4b74-a2a6-3e23c4fb7ab9 \
           83e5ae3a-de6f-4511-8c4f-b55d894b050e \
           b25f29af-9860-4523-a958-fa10d882f5d2 \
           39a7f546-c952-4b31-acd4-d29067a2162b; do
  echo -n "$id: "
  curl -s "http://localhost:8002/api/v2/tenants/default_tenant/databases/default_database/collections/$id/count"
  echo
done

# Get row counts from PostGIS — find the richest tables to vectorize first
docker exec jarvis-local-resources-db psql -U postgres -d msjarvisgis \
  -c "SELECT tablename, n_live_tup FROM pg_stat_user_tables ORDER BY n_live_tup DESC LIMIT 15;"
77393847-dfe0-4b74-a2a6-3e23c4fb7ab9: 270
83e5ae3a-de6f-4511-8c4f-b55d894b050e: 0
b25f29af-9860-4523-a958-fa10d882f5d2: 829
39a7f546-c952-4b31-acd4-d29067a2162b: 0
ERROR:  column "tablename" does not exist
LINE 1: SELECT tablename, n_live_tup FROM pg_stat_user_tables ORDER ...
               ^
(.venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ find /opt/msjarvis-rebuild -name "*ingest*" -o -name "*vectorize*" \
  -o -name "*embed*" -o -name "*load_gis*" 2>/dev/null | grep -v ".pyc"

# Also check the gis-rag service for a /ingest or /load endpoint
docker exec jarvis-gis-rag grep -rn "ingest\|load\|vectorize\|upsert" /app/ | grep "def \|route\|@app" | head -20
/opt/msjarvis-rebuild/reload_and_ingest_gis.sh
/opt/msjarvis-rebuild/_archive/generated_20260430/ingest_csv_to_gisgeodb.py
/opt/msjarvis-rebuild/_archive/generated_20260430/ingest_gbim_to_chroma_fast.py
/opt/msjarvis-rebuild/_archive/generated_20260430/ingest_imm_to_chroma.py
/opt/msjarvis-rebuild/_archive/generated_20260430/ingest_benefit_programs.py
/opt/msjarvis-rebuild/_archive/generated_20260430/embed_gbim.py
/opt/msjarvis-rebuild/_archive/generated_20260430/ingest_full_attributed_docs.py
/opt/msjarvis-rebuild/_archive/generated_20260430/embed_geodb.py
/opt/msjarvis-rebuild/_archive/generated_20260430/ingest_hospitals.py
/opt/msjarvis-rebuild/_archive/generated_20260430/ingest_benefit_programs_to_chroma.py
/opt/msjarvis-rebuild/_archive/generated_20260430/embed_and_query.py
/opt/msjarvis-rebuild/_archive/generated_20260430/ingest_gbim_to_chroma_ultrafast.py
/opt/msjarvis-rebuild/_archive/generated_20260430/ingest_documents_to_chromadb.py
/opt/msjarvis-rebuild/_archive/generated_20260430/load_gis_to_chroma.py
/opt/msjarvis-rebuild/_archive/generated_20260430/ingest_h4h_cultural_heritage.py
/opt/msjarvis-rebuild/_archive/generated_20260430/ingest_gbim_to_chroma.py
/opt/msjarvis-rebuild/_archive/generated_20260430/ingest_utility_enrollments_to_chroma.py
/opt/msjarvis-rebuild/_archive/generated_20260430/ingest_gis_features_to_chromadb.py
/opt/msjarvis-rebuild/_archive/generated_20260430/embed_and_add.py
/opt/msjarvis-rebuild/_archive/generated_20260430/ingest_gbim_to_chroma_resume.py
/opt/msjarvis-rebuild/_archive/generated_20260430/ingest_compliance_tasks_to_chroma.py
/opt/msjarvis-rebuild/_archive/generated_20260430/ingest_knowledge_simple.py
/opt/msjarvis-rebuild/_archive/generated_20260430/ingest_mrsid_imagery.py
/opt/msjarvis-rebuild/_archive/generated_20260430/ingest_additional_kbs.py
/opt/msjarvis-rebuild/ingest_gbimworldviewentities_from_csv.py
/opt/msjarvis-rebuild/ingest_attrs_to_chroma.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sklearn/manifold/_spectral_embedding.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sklearn/manifold/tests/test_spectral_embedding.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sklearn/feature_extraction/tests/test_dict_vectorizer.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sklearn/feature_extraction/_dict_vectorizer.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/onnx/backend/test/case/node/tfidfvectorizer.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/onnx/backend/test/case/node/rotaryembedding.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/onnx/backend/test/data/node/test_rotary_embedding_no_position_ids
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/onnx/backend/test/data/node/test_rotary_embedding
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/onnx/backend/test/data/node/test_rotary_embedding_with_rotary_dim_expanded
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/onnx/backend/test/data/node/test_tfidfvectorizer_tf_uniandbigrams_skip5
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/onnx/backend/test/data/node/test_tfidfvectorizer_tf_onlybigrams_skip5
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/onnx/backend/test/data/node/test_rotary_embedding_expanded
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/onnx/backend/test/data/node/test_rotary_embedding_no_position_ids_interleaved_expanded
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/onnx/backend/test/data/node/test_rotary_embedding_with_interleaved_rotary_dim
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/onnx/backend/test/data/node/test_rotary_embedding_no_position_ids_rotary_dim
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/onnx/backend/test/data/node/test_tfidfvectorizer_tf_batch_onlybigrams_skip0
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/onnx/backend/test/data/node/test_rotary_embedding_3d_input_expanded
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/onnx/backend/test/data/node/test_rotary_embedding_no_position_ids_rotary_dim_expanded
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/onnx/backend/test/data/node/test_tfidfvectorizer_tf_onlybigrams_levelempty
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/onnx/backend/test/data/node/test_tfidfvectorizer_tf_batch_uniandbigrams_skip5
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/onnx/backend/test/data/node/test_rotary_embedding_3d_input
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/onnx/backend/test/data/node/test_rotary_embedding_no_position_ids_interleaved
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/onnx/backend/test/data/node/test_rotary_embedding_interleaved_expanded
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/onnx/backend/test/data/node/test_rotary_embedding_no_position_ids_expanded
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/onnx/backend/test/data/node/test_tfidfvectorizer_tf_only_bigrams_skip0
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/onnx/backend/test/data/node/test_rotary_embedding_interleaved
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/onnx/backend/test/data/node/test_rotary_embedding_with_rotary_dim
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/onnx/backend/test/data/node/test_rotary_embedding_with_interleaved_rotary_dim_expanded
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/onnx/backend/test/data/node/test_tfidfvectorizer_tf_batch_onlybigrams_skip5
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/onnx/reference/ops/aionnxml/op_dict_vectorizer.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/onnx/reference/ops/aionnxml/op_feature_vectorizer.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/onnx/reference/ops/op_rotary_embedding.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/onnx/reference/ops/op_tfidf_vectorizer.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/torch/csrc/api/include/torch/nn/modules/embedding.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/torch/csrc/api/include/torch/nn/options/embedding.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/torch/csrc/api/include/torch/nn/functional/embedding.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/caffe2/perfkernels/embedding_lookup_idx.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/google/protobuf/compiler/js/well_known_types_embed.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/embedding_backward_ops.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/embedding.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/embedding_bag_compositeimplicitautograd_dispatch.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/embedding_renorm.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag_dense_backward_cpu_dispatch.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/embedding_backward_compositeimplicitautograd_dispatch.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/embedding_bag_native.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/embedding_sparse_backward_native.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/diag_embed_ops.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/hinge_embedding_loss_native.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/embedding_renorm_compositeexplicitautograd_dispatch.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/embedding_dense_backward_cuda_dispatch.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/embedding_renorm_meta_dispatch.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag_per_sample_weights_backward_compositeexplicitautograd_dispatch.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag_forward_only.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/cosine_embedding_loss_ops.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag_backward.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag_sparse_backward_native.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag_forward_only_native.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag_forward_only_compositeexplicitautograd_dispatch.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/embedding_dense_backward_cpu_dispatch.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag_backward_native.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag_dense_backward.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/embedding_bag_ops.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/embedding_sparse_backward_compositeimplicitautograd_dispatch.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/embedding_dense_backward.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/diag_embed_compositeexplicitautogradnonfunctional_dispatch.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag_per_sample_weights_backward.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/embedding_renorm_cpu_dispatch.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag_cpu_dispatch.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/embedding_renorm_native.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/embedding_backward.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag_per_sample_weights_backward_cuda_dispatch.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/embedding_dense_backward_compositeexplicitautograd_dispatch.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag_native.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag_sparse_backward_compositeimplicitautograd_dispatch.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag_forward_only_cuda_dispatch.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/embedding_dense_backward_ops.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag_per_sample_weights_backward_cpu_dispatch.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag_dense_backward_compositeexplicitautograd_dispatch.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/hinge_embedding_loss_ops.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/cosine_embedding_loss.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/cosine_embedding_loss_native.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag_compositeexplicitautograd_dispatch.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag_backward_cuda_dispatch.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag_cuda_dispatch.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/cosine_embedding_loss_compositeimplicitautograd_dispatch.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag_dense_backward_ops.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag_backward_ops.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/diag_embed.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/hinge_embedding_loss_compositeimplicitautograd_dispatch.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag_per_sample_weights_backward_ops.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag_dense_backward_native.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag_dense_backward_cuda_dispatch.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/embedding_sparse_backward_ops.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag_forward_only_ops.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag_per_sample_weights_backward_native.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/embedding_compositeexplicitautograd_dispatch.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag_sparse_backward.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/diag_embed_compositeexplicitautograd_dispatch.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/embedding_bag.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/embedding_sparse_backward.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/embedding_native.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/diag_embed_native.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/hinge_embedding_loss.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/embedding_renorm_cuda_dispatch.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag_ops.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag_backward_cpu_dispatch.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag_forward_only_cpu_dispatch.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/embedding_backward_native.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/embedding_ops.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/_embedding_bag_sparse_backward_ops.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/embedding_dense_backward_native.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/ops/embedding_renorm_ops.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/native/quantized/cpu/qembeddingbag_prepack.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/ATen/native/quantized/cpu/qembeddingbag.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/include/pybind11/embed.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/distributed/tensor/_ops/_embedding_ops.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/distributed/_shard/sharding_spec/chunk_sharding_spec_ops/embedding.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/distributed/_shard/sharding_spec/chunk_sharding_spec_ops/embedding_bag.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/ao/nn/quantized/modules/embedding_ops.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/ao/nn/qat/modules/embedding_ops.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/ao/quantization/quantizer/embedding_quantizer.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/nn/quantized/modules/embedding_ops.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/nn/qat/modules/embedding_ops.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/nn/utils/_expanded_weights/embedding_expanded_weights.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/utils/tensorboard/_embedding.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/torch/utils/_cpp_embed_headers.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/timm/layers/patch_embed.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/timm/layers/pos_embed_sincos.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/timm/layers/pos_embed_rel.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/timm/layers/hybrid_embed.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/timm/layers/pos_embed.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/pandas/_libs/tslibs/vectorized.pyi
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/pandas/_libs/tslibs/vectorized.cpython-312-x86_64-linux-gnu.so
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/onnxruntime/transformers/fusion_embedlayer.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/onnxruntime/quantization/operators/embed_layernorm.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/open_clip/pos_embed.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/schemas/embedding_functions
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/schemas/embedding_functions/fastembed_sparse.json
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/mysql/ai/genai/embedding.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/shapely/vectorized
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/shapely/tests/legacy/test_vectorized.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/matplotlib/mpl-data/sample_data/embedding_in_wx3.xrc
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/cffi/_embedding.h
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/optimum/fx/parallelization/parallel_layers/embedding.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/db/mixins/embeddings_queue.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/ingest
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/utils/sparse_embedding_utils.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/cloudflare_workers_ai_embedding_function.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/baseten_embedding_function.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/instructor_embedding_function.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/google_embedding_function.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/fastembed_sparse_embedding_function.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/together_ai_embedding_function.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/voyageai_embedding_function.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/text2vec_embedding_function.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/huggingface_embedding_function.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_cloud_qwen_embedding_function.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/bm25_embedding_function.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/jina_embedding_function.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/cohere_embedding_function.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/huggingface_sparse_embedding_function.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_cloud_splade_embedding_function.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/openai_embedding_function.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/amazon_bedrock_embedding_function.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/roboflow_embedding_function.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/morph_embedding_function.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/sentence_transformer_embedding_function.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/ollama_embedding_function.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_langchain_embedding_function.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_bm25_embedding_function.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/mistral_embedding_function.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/open_clip_embedding_function.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/nomic_embedding_function.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/migrations/embeddings_queue
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/migrations/embeddings_queue/00001-embeddings.sqlite.sql
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/migrations/embeddings_queue/00002-embeddings-queue-config.sqlite.sql
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/migrations/metadb/00002-embedding-metadata.sqlite.sql
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/migrations/metadb/00001-embedding-metadata.sqlite.sql
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/test/ef/test_chroma_bm25_embedding_function.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/test/utils/test_embedding_function_schemas.py
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/test/property/test_embeddings.py
/opt/msjarvis-rebuild/services/ingest_csv_to_gisgeodb.py
/opt/msjarvis-rebuild/services/ingest_gbim_to_chroma_fast.py
/opt/msjarvis-rebuild/services/ingestcsvtogisgeodb.py
/opt/msjarvis-rebuild/services/ingest_imm_to_chroma.py
/opt/msjarvis-rebuild/services/gbim_ingest_safe.log
/opt/msjarvis-rebuild/services/ingest_benefit_programs.py
/opt/msjarvis-rebuild/services/embed_gbim.py
/opt/msjarvis-rebuild/services/requirements-ingest.txt
/opt/msjarvis-rebuild/services/web_page_ingest.py
/opt/msjarvis-rebuild/services/safe_ingest_gbim_to_chroma.py
/opt/msjarvis-rebuild/services/gbim_ingest.log
/opt/msjarvis-rebuild/services/web_page_ingest.current.log
/opt/msjarvis-rebuild/services/ingest_full_attributed_docs.py
/opt/msjarvis-rebuild/services/embed_geodb.py
/opt/msjarvis-rebuild/services/ingest_hospitals.py
/opt/msjarvis-rebuild/services/ingest_benefit_programs_to_chroma.py
/opt/msjarvis-rebuild/services/embed_and_query.py
/opt/msjarvis-rebuild/services/ingest_gbim_to_chroma_ultrafast.py
/opt/msjarvis-rebuild/services/ingest_documents_to_chromadb.py
/opt/msjarvis-rebuild/services/chunked_ingest_gbim_to_chroma.py
/opt/msjarvis-rebuild/services/ingest_batch3_geofeatures.py
/opt/msjarvis-rebuild/services/ingest
/opt/msjarvis-rebuild/services/ingest_batch3_resume.py
/opt/msjarvis-rebuild/services/load_gis_to_chroma.py
/opt/msjarvis-rebuild/services/Dockerfile.data_ingest
/opt/msjarvis-rebuild/services/mountainshares_ingest.py
/opt/msjarvis-rebuild/services/ingest_h4h_cultural_heritage.py
/opt/msjarvis-rebuild/services/gateway_embeddings.log
/opt/msjarvis-rebuild/services/ingest_gbim_to_chroma.py
/opt/msjarvis-rebuild/services/_vendor/cytoolz/tests/test_embedded_sigs.py
/opt/msjarvis-rebuild/services/ingest_utility_enrollments_to_chroma.py
/opt/msjarvis-rebuild/services/ingest_gis_features_to_chromadb.py
/opt/msjarvis-rebuild/services/embed_and_add.py
/opt/msjarvis-rebuild/services/aapcappe_ingest.py
/opt/msjarvis-rebuild/services/ms_jarvis_complete_knowledge_ingestion.py
/opt/msjarvis-rebuild/services/ingest_gbim_to_chroma_resume.py
/opt/msjarvis-rebuild/services/ingest_compliance_tasks_to_chroma.py
/opt/msjarvis-rebuild/services/gbim_reingest_placeholder.py
/opt/msjarvis-rebuild/services/ingest_postgis_to_chroma.py
/opt/msjarvis-rebuild/services/ingest_knowledge_simple.py
/opt/msjarvis-rebuild/services/ingest_gis_features_fixed.py
/opt/msjarvis-rebuild/services/ingest_watcher
/opt/msjarvis-rebuild/services/ingest_watcher/ingest_runner.py
/opt/msjarvis-rebuild/services/ingest_watcher/ingest_watcher.py
/opt/msjarvis-rebuild/services/vectorize_gis_to_chromadb.py
/opt/msjarvis-rebuild/services/aacpe_ingest_community.py
/opt/msjarvis-rebuild/services/ingest_mrsid_imagery.py
/opt/msjarvis-rebuild/services/embed_utils.py
/opt/msjarvis-rebuild/services/resume_ingest_gbim_to_chroma.py
/opt/msjarvis-rebuild/services/ms_jarvis_complete_knowledge_ingestion_9627.log
/opt/msjarvis-rebuild/services/aaacpe_initial_ingest.py
/opt/msjarvis-rebuild/services/ingest_batch3_resume2.py
/opt/msjarvis-rebuild/services/jarvis_data_ingest.py
/opt/msjarvis-rebuild/services/ingest_additional_kbs.py
/opt/msjarvis-rebuild/ingest_wv_income_maintenance_manual.py
/opt/msjarvis-rebuild/ingest
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/cytoolz/tests/test_embedded_sigs.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/onnxruntime/transformers/fusion_embedlayer.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/onnxruntime/quantization/operators/embed_layernorm.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/schemas/embedding_functions
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/schemas/embedding_functions/fastembed_sparse.json
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/cffi/_embedding.h
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/db/mixins/embeddings_queue.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/ingest
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/utils/sparse_embedding_utils.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/cloudflare_workers_ai_embedding_function.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/baseten_embedding_function.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/instructor_embedding_function.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/google_embedding_function.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/fastembed_sparse_embedding_function.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/together_ai_embedding_function.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/voyageai_embedding_function.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/text2vec_embedding_function.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/huggingface_embedding_function.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_cloud_qwen_embedding_function.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/bm25_embedding_function.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/jina_embedding_function.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/cohere_embedding_function.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/huggingface_sparse_embedding_function.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_cloud_splade_embedding_function.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/openai_embedding_function.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/amazon_bedrock_embedding_function.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/roboflow_embedding_function.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/morph_embedding_function.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/perplexity_embedding_function.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/sentence_transformer_embedding_function.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/ollama_embedding_function.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_langchain_embedding_function.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_bm25_embedding_function.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/mistral_embedding_function.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/open_clip_embedding_function.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/nomic_embedding_function.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/migrations/embeddings_queue
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/migrations/embeddings_queue/00001-embeddings.sqlite.sql
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/migrations/embeddings_queue/00002-embeddings-queue-config.sqlite.sql
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/migrations/metadb/00002-embedding-metadata.sqlite.sql
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/migrations/metadb/00001-embedding-metadata.sqlite.sql
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/test/ef/test_chroma_bm25_embedding_function.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/test/utils/test_embedding_function_schemas.py
/opt/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/test/property/test_embeddings.py
/opt/msjarvis-rebuild/ingest_kanawha_images.py
/opt/msjarvis-rebuild/logs-archive/bridge_ms_jarvis_main_gateway_to_ingest_knowledge_simple.log
/opt/msjarvis-rebuild/logs-archive/bridge_ms_jarvis_main_gateway_to_ingest_csv_to_gisgeodb.log
/opt/msjarvis-rebuild/logs-archive/bridge_ms_jarvis_main_gateway_to_ingest_documents_to_chromadb.log
/opt/msjarvis-rebuild/logs-archive/bridge_ms_jarvis_main_gateway_to_vectorize_gis_to_chromadb.log
/opt/msjarvis-rebuild/logs-archive/bridge_ms_jarvis_main_gateway_to_ingest_gis_features_to_chromadb.log
/opt/msjarvis-rebuild/logs-archive/bridge_ms_jarvis_main_gateway_to_embed_and_add.log
/opt/msjarvis-rebuild/logs-archive/bridge_ms_jarvis_main_gateway_to_ingest_mrsid_imagery.log
/opt/msjarvis-rebuild/logs-archive/bridge_ms_jarvis_main_gateway_to_embed_and_query.log
/opt/msjarvis-rebuild/logs-archive/bridge_ms_jarvis_main_gateway_to_ingest_full_attributed_docs.log
/opt/msjarvis-rebuild/logs-archive/bridge_ms_jarvis_main_gateway_to_ms_jarvis_complete_knowledge_ingestion.log
/opt/msjarvis-rebuild/ingest_missing.log
/opt/msjarvis-rebuild/all_gis_vectors_ingest.txt
/opt/msjarvis-rebuild/ingest_missing_attrs.py
/opt/msjarvis-rebuild/ingest_personal_pdfs.py
/opt/msjarvis-rebuild/bulk_ingest_attrs.py
/opt/msjarvis-rebuild/ingest_kanawha_resources.py
/opt/msjarvis-rebuild/ingest.log
/opt/msjarvis-rebuild/reingest_msjarvis_chunks.py
/opt/msjarvis-rebuild/msjarvis_embed_gbim.py
/opt/msjarvis-rebuild/chroma_ingestion_sources.txt
/opt/msjarvis-rebuild/data/ingest
/opt/msjarvis-rebuild/data/ingest/civic_programs/ingest_to_chroma.py
/opt/msjarvis-rebuild/ingest_msjarvis_corpus.py
/opt/msjarvis-rebuild/bulk_ingest.log
/opt/msjarvis-rebuild/ingest_wvgistc_to_chroma.py
/opt/msjarvis-rebuild/msjarvis_embed_gbim_resume_tail.py
/opt/msjarvis-rebuild/ops_history/dump_ops_history_for_embeddings.sh
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/onnxruntime/transformers/fusion_embedlayer.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/onnxruntime/quantization/operators/embed_layernorm.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/schemas/embedding_functions
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/schemas/embedding_functions/fastembed_sparse.json
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/db/mixins/embeddings_queue.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/ingest
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/utils/sparse_embedding_utils.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/utils/embedding_functions
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/utils/embedding_functions/cloudflare_workers_ai_embedding_function.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/utils/embedding_functions/baseten_embedding_function.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/utils/embedding_functions/instructor_embedding_function.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/utils/embedding_functions/google_embedding_function.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/utils/embedding_functions/fastembed_sparse_embedding_function.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/utils/embedding_functions/together_ai_embedding_function.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/utils/embedding_functions/voyageai_embedding_function.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/utils/embedding_functions/text2vec_embedding_function.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/utils/embedding_functions/huggingface_embedding_function.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_cloud_qwen_embedding_function.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/utils/embedding_functions/bm25_embedding_function.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/utils/embedding_functions/jina_embedding_function.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/utils/embedding_functions/cohere_embedding_function.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/utils/embedding_functions/huggingface_sparse_embedding_function.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_cloud_splade_embedding_function.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/utils/embedding_functions/openai_embedding_function.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/utils/embedding_functions/amazon_bedrock_embedding_function.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/utils/embedding_functions/roboflow_embedding_function.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/utils/embedding_functions/morph_embedding_function.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/utils/embedding_functions/sentence_transformer_embedding_function.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/utils/embedding_functions/ollama_embedding_function.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_langchain_embedding_function.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_bm25_embedding_function.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/utils/embedding_functions/mistral_embedding_function.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/utils/embedding_functions/open_clip_embedding_function.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/utils/embedding_functions/nomic_embedding_function.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/migrations/embeddings_queue
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/migrations/embeddings_queue/00001-embeddings.sqlite.sql
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/migrations/embeddings_queue/00002-embeddings-queue-config.sqlite.sql
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/migrations/metadb/00002-embedding-metadata.sqlite.sql
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/migrations/metadb/00001-embedding-metadata.sqlite.sql
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/test/ef/test_chroma_bm25_embedding_function.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/test/utils/test_embedding_function_schemas.py
/opt/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/chromadb/test/property/test_embeddings.py
/opt/msjarvis-rebuild/scripts/ingest_landowner_parcels.sh
/opt/msjarvis-rebuild/scripts/ingest_chroma.py
/opt/msjarvis-rebuild/scripts/ingest_health_emergency_to_chroma.py
/opt/msjarvis-rebuild/scripts/dump_ops_history_for_embeddings.sh
/opt/msjarvis-rebuild/scripts/ingest_county_worldview.sql
/opt/msjarvis-rebuild/scripts/bulk_ingest_msjarvisgis.py
/opt/msjarvis-rebuild/scripts/ingest_watershed_worldview.sql
/opt/msjarvis-rebuild/logs/ch40_closeout/oi_latency_tracing_trace_ingest_status.txt
/opt/msjarvis-rebuild/logs/ch40_closeout/oi_ops_history_embeddings_status.txt
/opt/msjarvis-rebuild/logs/gbim_embed_2026-02-24_06-53.log
/opt/msjarvis-rebuild/logs/msjarvis_embed_gbim_2026-02-24_06-53.py
/opt/msjarvis-rebuild/gbim_ingest
/opt/msjarvis-rebuild/gbim_ingest/01b_ingest_wv9.py
/opt/msjarvis-rebuild/gbim_ingest/04_ingest_wv17_gis.py
/opt/msjarvis-rebuild/gbim_ingest/03_ingest_chroma_wv11_16.py
/opt/msjarvis-rebuild/gbim_ingest/02_ingest_wv10.py
/opt/msjarvis-rebuild/gbim_ingest/logs/embed_main_20260531_2211.log
/opt/msjarvis-rebuild/gbim_ingest/logs/embed_main_20260531_2216.log
/opt/msjarvis-rebuild/gbim_ingest/logs/embed_main_20260531_2145.log
/opt/msjarvis-rebuild/gbim_ingest/logs/embed_main_20260531_2223.log
/opt/msjarvis-rebuild/test_rag_embedding_roundtrip.sh
/opt/msjarvis-rebuild/chroma_db/chroma-embeddings.parquet
grep: /app/__pycache__/gis_rag_service.cpython-311.pyc: binary file matches
/app/gis_rag_service.py:42:    logging.warning(f"GIS PostGIS router not loaded: {_e}")
(.venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ 

