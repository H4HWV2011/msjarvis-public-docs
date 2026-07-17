build$ psql -h localhost -p 5432 -U postgres -d msjarvisgis -c "\d promotion_events"

psql -h localhost -p 5432 -U postgres -d msjarvisgis -c "
SELECT *
FROM promotion_events
ORDER BY promoted_at DESC NULLS LAST
LIMIT 20;
"

psql -h localhost -p 5432 -U postgres -d msjarvisgis -c "
SELECT pe.*
FROM promotion_events pe
JOIN gbim_collection_manifest cm
  ON cm.collection_version_id = pe.collection_version_id
WHERE cm.collection_name IN ('gbim_wv_counties','gbim_wv_tracts','gbim_wv_blockgroups')
ORDER BY pe.promoted_at DESC NULLS LAST;
"
ERROR:  column "promoted_at" does not exist
LINE 4: ORDER BY promoted_at DESC NULLS LAST
                 ^
ERROR:  column pe.collection_version_id does not exist
LINE 5:   ON cm.collection_version_id = pe.collection_version_id
                                        ^
HINT:  Perhaps you meant to reference the column "cm.collection_version_id".
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/msjarvis-rebuild$ rg -n "permitted_use|request_purpose|x-msallis-purpose|gbim_chroma_publication_manifest|public_civic_geographic_retrieval|analysis" \
  /mnt/spiritual_drive/msjarvis-rebuild /opt/msjarvis-rebuild/msjarvis-rebuild --type py 2>/dev/null | grep -v site-packages | head -120
/mnt/spiritual_drive/msjarvis-rebuild/main_brain.py:349:        # match temporal_consciousness stub (/temporalanalysis)
/mnt/spiritual_drive/msjarvis-rebuild/main_brain.py:350:        "temporal_consciousness": "/temporalanalysis",
/opt/msjarvis-rebuild/msjarvis-rebuild/main_brain.py:349:        # match temporal_consciousness stub (/temporalanalysis)
/opt/msjarvis-rebuild/msjarvis-rebuild/main_brain.py:350:        "temporal_consciousness": "/temporalanalysis",
/mnt/spiritual_drive/msjarvis-rebuild/services/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py:133:            consciousness_analysis = enhanced_data.get(consciousness_analysis, {})
/mnt/spiritual_drive/msjarvis-rebuild/services/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py:139:                    "layers_analyzed": consciousness_analysis.get(layers_activated, 0),
/mnt/spiritual_drive/msjarvis-rebuild/services/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py:140:                    "layer_details": consciousness_analysis.get(layer_analyses, []),
/mnt/spiritual_drive/msjarvis-rebuild/services/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py:141:                    "integration": consciousness_analysis.get(integration, ),
/opt/msjarvis-rebuild/msjarvis-rebuild/services/rag_query_router.py:287:        f"and keyword/metadata analysis (scores={scores})."
/opt/msjarvis-rebuild/msjarvis-rebuild/services/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py:133:            consciousness_analysis = enhanced_data.get(consciousness_analysis, {})
/opt/msjarvis-rebuild/msjarvis-rebuild/services/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py:139:                    "layers_analyzed": consciousness_analysis.get(layers_activated, 0),
/opt/msjarvis-rebuild/msjarvis-rebuild/services/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py:140:                    "layer_details": consciousness_analysis.get(layer_analyses, []),
/opt/msjarvis-rebuild/msjarvis-rebuild/services/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py:141:                    "integration": consciousness_analysis.get(integration, ),
/mnt/spiritual_drive/msjarvis-rebuild/services/rag_query_router.py:287:        f"and keyword/metadata analysis (scores={scores})."
/opt/msjarvis-rebuild/msjarvis-rebuild/services/add_full_brain_class.py:54:                    logger.info("✅ Neurobiological analysis added")
/opt/msjarvis-rebuild/msjarvis-rebuild/services/llm_consensus_20_FINAL.py:171:        "specialty": "Code analysis",
/opt/msjarvis-rebuild/msjarvis-rebuild/services/ai_server_19llm_CONSCIOUS.backup_20251013_082519.py:88:    {"name": "zephyr:latest", "timeout": 65, "tier": 2, "role": "analysis"},
/opt/msjarvis-rebuild/msjarvis-rebuild/services/ai_server_19llm_CONSCIOUS.backup_20251013_082519.py:121:                "sentiment-analysis",
/opt/msjarvis-rebuild/msjarvis-rebuild/services/ai_server_19llm_CONSCIOUS.backup_20251013_082519.py:141:            # Emotional state analysis
/mnt/spiritual_drive/msjarvis-rebuild/services/add_full_brain_class.py:54:                    logger.info("✅ Neurobiological analysis added")
/opt/msjarvis-rebuild/msjarvis-rebuild/services/llm_consensus_22_SMALL_TO_LARGE.py:53:     "specialty": "Code analysis", "role": "coding", "weight": 0.85, "timeout": 90},
/opt/msjarvis-rebuild/msjarvis-rebuild/services/llm_consensus_22_SMALL_TO_LARGE.py:71:     "specialty": "Advanced analysis", "role": "core_reasoning", "weight": 1.0, "timeout": 180},
/opt/msjarvis-rebuild/msjarvis-rebuild/services/integrate_complete_architecture.py:59:    """Query Qualia Engine for subjective experience analysis"""
/opt/msjarvis-rebuild/msjarvis-rebuild/services/integrate_complete_architecture.py:127:        qualia_analysis = await query_qualia_engine(
/opt/msjarvis-rebuild/msjarvis-rebuild/services/integrate_complete_architecture.py:132:        if qualia_analysis:
/opt/msjarvis-rebuild/msjarvis-rebuild/services/integrate_complete_architecture.py:133:            context['qualia'] = qualia_analysis
/mnt/spiritual_drive/msjarvis-rebuild/services/llm_consensus_20_FINAL.py:171:        "specialty": "Code analysis",
/mnt/spiritual_drive/msjarvis-rebuild/services/llm_consensus_22_SMALL_TO_LARGE.py:53:     "specialty": "Code analysis", "role": "coding", "weight": 0.85, "timeout": 90},
/mnt/spiritual_drive/msjarvis-rebuild/services/llm_consensus_22_SMALL_TO_LARGE.py:71:     "specialty": "Advanced analysis", "role": "core_reasoning", "weight": 1.0, "timeout": 180},
/mnt/spiritual_drive/msjarvis-rebuild/services/ai_server_19llm_CONSCIOUS.backup_20251013_082519.py:88:    {"name": "zephyr:latest", "timeout": 65, "tier": 2, "role": "analysis"},
/mnt/spiritual_drive/msjarvis-rebuild/services/ai_server_19llm_CONSCIOUS.backup_20251013_082519.py:121:                "sentiment-analysis",
/mnt/spiritual_drive/msjarvis-rebuild/services/ai_server_19llm_CONSCIOUS.backup_20251013_082519.py:141:            # Emotional state analysis
/opt/msjarvis-rebuild/msjarvis-rebuild/services/update_theological_boundaries.py:14:Transform this technical analysis into a nurturing, motherly response while maintaining all technical accuracy:
/opt/msjarvis-rebuild/msjarvis-rebuild/services/update_theological_boundaries.py:30:Transform the analysis above into your warm, maternal response:"""'''
/opt/msjarvis-rebuild/msjarvis-rebuild/services/update_theological_boundaries.py:42:Transform this technical analysis into a nurturing, motherly response while maintaining all technical accuracy:
/opt/msjarvis-rebuild/msjarvis-rebuild/services/update_theological_boundaries.py:59:Transform the analysis above into your warm, maternal response:"""'''
/opt/msjarvis-rebuild/msjarvis-rebuild/services/ai_server.py:62:        self.sentiment_pipeline = pipeline("sentiment-analysis", 
/opt/msjarvis-rebuild/msjarvis-rebuild/services/psychology_loop_closer.py:25:    async def store_interaction(self, ueid, user_msg, response_text, dgm_analysis=None, psychology_context=None):
/opt/msjarvis-rebuild/msjarvis-rebuild/services/psychology_loop_closer.py:38:                dgm_analysis.get('sentiment', 0) if dgm_analysis else 0,
/opt/msjarvis-rebuild/msjarvis-rebuild/services/psychology_loop_closer.py:39:                json.dumps(dgm_analysis.get('emotions', []) if dgm_analysis else []),
/opt/msjarvis-rebuild/msjarvis-rebuild/services/psychology_loop_closer.py:81:def sync_store(ueid, user_msg, response, dgm_analysis=None, psychology_context=None):
/opt/msjarvis-rebuild/msjarvis-rebuild/services/psychology_loop_closer.py:85:        loop_closer.store_interaction(ueid, user_msg, response, dgm_analysis, psychology_context)
/mnt/spiritual_drive/msjarvis-rebuild/services/integrate_complete_architecture.py:59:    """Query Qualia Engine for subjective experience analysis"""
/mnt/spiritual_drive/msjarvis-rebuild/services/integrate_complete_architecture.py:127:        qualia_analysis = await query_qualia_engine(
/mnt/spiritual_drive/msjarvis-rebuild/services/integrate_complete_architecture.py:132:        if qualia_analysis:
/mnt/spiritual_drive/msjarvis-rebuild/services/integrate_complete_architecture.py:133:            context['qualia'] = qualia_analysis
/opt/msjarvis-rebuild/msjarvis-rebuild/services/llm_judge_v3.py:3:Extends judge_pipeline v2.0.0 with evidence-grounded claim analysis.
/mnt/spiritual_drive/msjarvis-rebuild/services/update_theological_boundaries.py:14:Transform this technical analysis into a nurturing, motherly response while maintaining all technical accuracy:
/mnt/spiritual_drive/msjarvis-rebuild/services/update_theological_boundaries.py:30:Transform the analysis above into your warm, maternal response:"""'''
/mnt/spiritual_drive/msjarvis-rebuild/services/update_theological_boundaries.py:42:Transform this technical analysis into a nurturing, motherly response while maintaining all technical accuracy:
/mnt/spiritual_drive/msjarvis-rebuild/services/update_theological_boundaries.py:59:Transform the analysis above into your warm, maternal response:"""'''
/mnt/spiritual_drive/msjarvis-rebuild/services/ai_server.py:62:        self.sentiment_pipeline = pipeline("sentiment-analysis", 
/mnt/spiritual_drive/msjarvis-rebuild/services/psychology_loop_closer.py:25:    async def store_interaction(self, ueid, user_msg, response_text, dgm_analysis=None, psychology_context=None):
/mnt/spiritual_drive/msjarvis-rebuild/services/psychology_loop_closer.py:38:                dgm_analysis.get('sentiment', 0) if dgm_analysis else 0,
/mnt/spiritual_drive/msjarvis-rebuild/services/psychology_loop_closer.py:39:                json.dumps(dgm_analysis.get('emotions', []) if dgm_analysis else []),
/mnt/spiritual_drive/msjarvis-rebuild/services/psychology_loop_closer.py:81:def sync_store(ueid, user_msg, response, dgm_analysis=None, psychology_context=None):
/mnt/spiritual_drive/msjarvis-rebuild/services/psychology_loop_closer.py:85:        loop_closer.store_interaction(ueid, user_msg, response, dgm_analysis, psychology_context)
/opt/msjarvis-rebuild/msjarvis-rebuild/services/llm_conscious_OPTIMIZED.py:10:    {"name": "zephyr", "timeout": 65, "tier": 2, "role": "analysis"},
/opt/msjarvis-rebuild/msjarvis-rebuild/services/jarvis-psychology-services_psychology_integration_adapter.py:56:                    logger.info(f"🧠 Psychology analysis for {ueid}: {result.get('psychological_assessment', '')[:50]}...")
/opt/msjarvis-rebuild/msjarvis-rebuild/services/jarvis-psychology-services_psychology_integration_adapter.py:59:            logger.warning(f"Psychology analysis error: {e}")
/opt/msjarvis-rebuild/msjarvis-rebuild/services/jarvis-psychology-services_psychology_integration_adapter.py:61:        return self._fallback_analysis(message)
/opt/msjarvis-rebuild/msjarvis-rebuild/services/jarvis-psychology-services_psychology_integration_adapter.py:63:    async def get_dgm_analysis(self, ueid: str) -> Dict[str, Any]:
/opt/msjarvis-rebuild/msjarvis-rebuild/services/jarvis-psychology-services_psychology_integration_adapter.py:65:        Get DGM analysis for user from Layer 2
/opt/msjarvis-rebuild/msjarvis-rebuild/services/jarvis-psychology-services_psychology_integration_adapter.py:81:            logger.warning(f"DGM analysis error: {e}")
/opt/msjarvis-rebuild/msjarvis-rebuild/services/jarvis-psychology-services_psychology_integration_adapter.py:114:            # Get psychology analysis
/opt/msjarvis-rebuild/msjarvis-rebuild/services/jarvis-psychology-services_psychology_integration_adapter.py:118:            dgm_data = await self.get_dgm_analysis(ueid)
/opt/msjarvis-rebuild/msjarvis-rebuild/services/jarvis-psychology-services_psychology_integration_adapter.py:152:        Store psychology analysis event in GISGEODB
/opt/msjarvis-rebuild/msjarvis-rebuild/services/jarvis-psychology-services_psychology_integration_adapter.py:165:                'psychology_analysis',
/opt/msjarvis-rebuild/msjarvis-rebuild/services/jarvis-psychology-services_psychology_integration_adapter.py:181:    def _fallback_analysis(self, message: str) -> Dict[str, Any]:
/opt/msjarvis-rebuild/msjarvis-rebuild/services/jarvis-psychology-services_psychology_integration_adapter.py:182:        """Fallback analysis if psychology service unavailable"""
/mnt/spiritual_drive/msjarvis-rebuild/services/llm_judge_v3.py:3:Extends judge_pipeline v2.0.0 with evidence-grounded claim analysis.
/mnt/spiritual_drive/msjarvis-rebuild/services/llm_conscious_OPTIMIZED.py:10:    {"name": "zephyr", "timeout": 65, "tier": 2, "role": "analysis"},
/opt/msjarvis-rebuild/msjarvis-rebuild/services/patch_mother_persona.py:49:            if 'Transform this technical analysis' in lines[j]:
/opt/msjarvis-rebuild/msjarvis-rebuild/services/hierarchical_integration.py:64:            agents_task = self.run_multi_agent_analysis(message, context)
/opt/msjarvis-rebuild/msjarvis-rebuild/services/hierarchical_integration.py:126:                agent_responses = await self.run_multi_agent_analysis(message, context)
/opt/msjarvis-rebuild/msjarvis-rebuild/services/response_filter.py:32:    text = re.sub(r'the\s+(?:specialist\s+)?team\s+of\s+experts', 'careful analysis', text, flags=re.IGNORECASE)
/mnt/spiritual_drive/msjarvis-rebuild/services/jarvis-psychology-services_psychology_integration_adapter.py:56:                    logger.info(f"🧠 Psychology analysis for {ueid}: {result.get('psychological_assessment', '')[:50]}...")
/mnt/spiritual_drive/msjarvis-rebuild/services/jarvis-psychology-services_psychology_integration_adapter.py:59:            logger.warning(f"Psychology analysis error: {e}")
/mnt/spiritual_drive/msjarvis-rebuild/services/jarvis-psychology-services_psychology_integration_adapter.py:61:        return self._fallback_analysis(message)
/mnt/spiritual_drive/msjarvis-rebuild/services/jarvis-psychology-services_psychology_integration_adapter.py:63:    async def get_dgm_analysis(self, ueid: str) -> Dict[str, Any]:
/mnt/spiritual_drive/msjarvis-rebuild/services/jarvis-psychology-services_psychology_integration_adapter.py:65:        Get DGM analysis for user from Layer 2
/mnt/spiritual_drive/msjarvis-rebuild/services/jarvis-psychology-services_psychology_integration_adapter.py:81:            logger.warning(f"DGM analysis error: {e}")
/mnt/spiritual_drive/msjarvis-rebuild/services/jarvis-psychology-services_psychology_integration_adapter.py:114:            # Get psychology analysis
/mnt/spiritual_drive/msjarvis-rebuild/services/jarvis-psychology-services_psychology_integration_adapter.py:118:            dgm_data = await self.get_dgm_analysis(ueid)
/mnt/spiritual_drive/msjarvis-rebuild/services/jarvis-psychology-services_psychology_integration_adapter.py:152:        Store psychology analysis event in GISGEODB
/mnt/spiritual_drive/msjarvis-rebuild/services/jarvis-psychology-services_psychology_integration_adapter.py:165:                'psychology_analysis',
/mnt/spiritual_drive/msjarvis-rebuild/services/jarvis-psychology-services_psychology_integration_adapter.py:181:    def _fallback_analysis(self, message: str) -> Dict[str, Any]:
/mnt/spiritual_drive/msjarvis-rebuild/services/jarvis-psychology-services_psychology_integration_adapter.py:182:        """Fallback analysis if psychology service unavailable"""
/opt/msjarvis-rebuild/msjarvis-rebuild/services/msjarvis-rebuild-nbb_i_containers-1_ms_jarvis_consciousness_unified_bridge.py:133:            consciousness_analysis = enhanced_data.get(consciousness_analysis, {})
/opt/msjarvis-rebuild/msjarvis-rebuild/services/msjarvis-rebuild-nbb_i_containers-1_ms_jarvis_consciousness_unified_bridge.py:139:                    "layers_analyzed": consciousness_analysis.get(layers_activated, 0),
/opt/msjarvis-rebuild/msjarvis-rebuild/services/msjarvis-rebuild-nbb_i_containers-1_ms_jarvis_consciousness_unified_bridge.py:140:                    "layer_details": consciousness_analysis.get(layer_analyses, []),
/opt/msjarvis-rebuild/msjarvis-rebuild/services/msjarvis-rebuild-nbb_i_containers-1_ms_jarvis_consciousness_unified_bridge.py:141:                    "integration": consciousness_analysis.get(integration, ),
/opt/msjarvis-rebuild/msjarvis-rebuild/services/jarvis-rag-server_ms_jarvis_consciousness_unified_bridge.py:133:            consciousness_analysis = enhanced_data.get(consciousness_analysis, {})
/opt/msjarvis-rebuild/msjarvis-rebuild/services/jarvis-rag-server_ms_jarvis_consciousness_unified_bridge.py:139:                    "layers_analyzed": consciousness_analysis.get(layers_activated, 0),
/opt/msjarvis-rebuild/msjarvis-rebuild/services/jarvis-rag-server_ms_jarvis_consciousness_unified_bridge.py:140:                    "layer_details": consciousness_analysis.get(layer_analyses, []),
/opt/msjarvis-rebuild/msjarvis-rebuild/services/jarvis-rag-server_ms_jarvis_consciousness_unified_bridge.py:141:                    "integration": consciousness_analysis.get(integration, ),
/opt/msjarvis-rebuild/msjarvis-rebuild/services/mesh_coordinator_interface.py:179:    CREATE TABLE IF NOT EXISTS mesh_coordinator_analysis (
/opt/msjarvis-rebuild/msjarvis-rebuild/services/psychology_integration_adapter.py:56:                    logger.info(f"🧠 Psychology analysis for {ueid}: {result.get('psychological_assessment', '')[:50]}...")
/opt/msjarvis-rebuild/msjarvis-rebuild/services/psychology_integration_adapter.py:59:            logger.warning(f"Psychology analysis error: {e}")
/opt/msjarvis-rebuild/msjarvis-rebuild/services/psychology_integration_adapter.py:61:        return self._fallback_analysis(message)
/opt/msjarvis-rebuild/msjarvis-rebuild/services/psychology_integration_adapter.py:63:    async def get_dgm_analysis(self, ueid: str) -> Dict[str, Any]:
/opt/msjarvis-rebuild/msjarvis-rebuild/services/psychology_integration_adapter.py:65:        Get DGM analysis for user from Layer 2
/opt/msjarvis-rebuild/msjarvis-rebuild/services/psychology_integration_adapter.py:81:            logger.warning(f"DGM analysis error: {e}")
/opt/msjarvis-rebuild/msjarvis-rebuild/services/psychology_integration_adapter.py:114:            # Get psychology analysis
/opt/msjarvis-rebuild/msjarvis-rebuild/services/psychology_integration_adapter.py:118:            dgm_data = await self.get_dgm_analysis(ueid)
/opt/msjarvis-rebuild/msjarvis-rebuild/services/psychology_integration_adapter.py:152:        Store psychology analysis event in GISGEODB
/opt/msjarvis-rebuild/msjarvis-rebuild/services/psychology_integration_adapter.py:165:                'psychology_analysis',
/opt/msjarvis-rebuild/msjarvis-rebuild/services/psychology_integration_adapter.py:181:    def _fallback_analysis(self, message: str) -> Dict[str, Any]:
/opt/msjarvis-rebuild/msjarvis-rebuild/services/psychology_integration_adapter.py:182:        """Fallback analysis if psychology service unavailable"""
/opt/msjarvis-rebuild/msjarvis-rebuild/services/test_full_brain_integration.py:43:            brain = data.get('brain_analysis', {})
/opt/msjarvis-rebuild/msjarvis-rebuild/services/safe_integration.py:49:                    logger.info("✅ Neurobiological analysis integrated")
/opt/msjarvis-rebuild/msjarvis-rebuild/services/ai_server_19llm_CONSCIOUS.py:65:    {"name": "zephyr", "timeout": 65, "tier": 2, "role": "analysis"},
/opt/msjarvis-rebuild/msjarvis-rebuild/services/ai_server_19llm_CONSCIOUS.py:100:                "sentiment-analysis",
/opt/msjarvis-rebuild/msjarvis-rebuild/services/ai_server_19llm_CONSCIOUS.py:120:            # Emotional state analysis
/opt/msjarvis-rebuild/msjarvis-rebuild/services/gateway_messenger_integration.py:47:    consciousness response with complete temporal-depth analysis.
/opt/msjarvis-rebuild/msjarvis-rebuild/services/gateway_messenger_integration.py:63:    Full context for academic citation and analysis.
/opt/msjarvis-rebuild/msjarvis-rebuild/services/llm_consensus_19_PRODUCTION.py:52:     "specialty": "Code analysis", "role": "coding", "weight": 0.85, "timeout": 90},
/mnt/spiritual_drive/msjarvis-rebuild/services/hierarchical_integration.py:64:            agents_task = self.run_multi_agent_analysis(message, context)
/mnt/spiritual_drive/msjarvis-rebuild/services/hierarchical_integration.py:126:                agent_responses = await self.run_multi_agent_analysis(message, context)
/opt/msjarvis-rebuild/msjarvis-rebuild/services/jarvis-agents-service_ms_jarvis_consciousness_unified_bridge.py:133:            consciousness_analysis = enhanced_data.get(consciousness_analysis, {})
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/msjarvis-rebuild$ RESP=$(curl -s -X POST http://localhost:8004/gis_rag \
  -H 'Content-Type: application/json' \
  -H 'x-msallis-role: researcher' \
  -H 'x-msallis-purpose: public_civic_geographic_retrieval' \
  -H 'x-msallis-legal-basis: authorized internal audit' \
  --data '{"query":"ZIP code 25901 Oak Hill West Virginia","nresults":3,"request_purpose":"public_civic_geographic_retrieval"}')

printf '%s\n' "$RESP"
printf '%s' "$RESP" | python3 -m json.tool
{"detail":"manifest permitted_use missing for collection 'gbimwvzctasv1'"}
{
    "detail": "manifest permitted_use missing for collection 'gbimwvzctasv1'"
}
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/msjarvis-rebuild$ psql -h localhost -p 5432 -U postgres -d msjarvisgis <<'SQL'
\pset pager off

SELECT table_name, column_name, data_type
FROM information_schema.columns
WHERE table_schema = 'public'
  AND table_name IN (
    'promotion_events',
    'gbim_chroma_publication_manifest',
    'gbim_collection_manifest',
    'gbim_vector_publication',
    'gbim_active_collection'
  )
ORDER BY table_name, ordinal_position;

SELECT
  tc.table_name,
  kcu.column_name,
  ccu.table_name AS foreign_table_name,
  ccu.column_name AS foreign_column_name,
  tc.constraint_name
FROM information_schema.table_constraints AS tc
JOIN information_schema.key_column_usage AS kcu
SQLIT 20;issued_at DESC, nonce DESCnt_name;mege AS ccu
Pager usage is off.
            table_name            |       column_name        |        data_type         
----------------------------------+--------------------------+--------------------------
 gbim_active_collection           | logical_collection_name  | text
 gbim_active_collection           | collection_version_id    | uuid
 gbim_active_collection           | physical_collection_name | text
 gbim_active_collection           | activated_at             | timestamp with time zone
 gbim_chroma_publication_manifest | logical_collection_name  | text
 gbim_chroma_publication_manifest | physical_collection_name | text
 gbim_chroma_publication_manifest | collection_version_id    | uuid
 gbim_chroma_publication_manifest | updated_at               | timestamp with time zone
 gbim_chroma_publication_manifest | permitted_use            | text
 gbim_collection_manifest         | collection_version_id    | uuid
 gbim_collection_manifest         | collection_name          | text
 gbim_collection_manifest         | collection_version       | text
 gbim_collection_manifest         | source_view              | text
 gbim_collection_manifest         | snapshot_version         | text
 gbim_collection_manifest         | rendering_version        | text
 gbim_collection_manifest         | embedding_model          | text
 gbim_collection_manifest         | embedding_dimension      | integer
 gbim_collection_manifest         | record_count             | integer
 gbim_collection_manifest         | collection_hash          | text
 gbim_collection_manifest         | build_status             | text
 gbim_collection_manifest         | permitted_use            | text
 gbim_collection_manifest         | built_at                 | timestamp with time zone
 gbim_collection_manifest         | validated_at             | timestamp with time zone
 gbim_collection_manifest         | promoted_at              | timestamp with time zone
 gbim_collection_manifest         | superseded_at            | timestamp with time zone
 gbim_collection_manifest         | notes                    | text
 gbim_vector_publication          | publication_id           | uuid
 gbim_vector_publication          | collection_version_id    | uuid
 gbim_vector_publication          | document_id              | text
 gbim_vector_publication          | canonical_entity_id      | text
 gbim_vector_publication          | belief_hash              | text
 gbim_vector_publication          | snapshot_version         | text
 gbim_vector_publication          | chroma_record_id         | text
 gbim_vector_publication          | publication_status       | text
 gbim_vector_publication          | published_at             | timestamp with time zone
 gbim_vector_publication          | verified_at              | timestamp with time zone
 gbim_vector_publication          | error_message            | text
 gbim_vector_publication          | centroid_lat             | double precision
 gbim_vector_publication          | centroid_lon             | double precision
 gbim_vector_publication          | bbox_min_lon             | double precision
 gbim_vector_publication          | bbox_min_lat             | double precision
 gbim_vector_publication          | bbox_max_lon             | double precision
 gbim_vector_publication          | bbox_max_lat             | double precision
 gbim_vector_publication          | source_crs               | text
 gbim_vector_publication          | metadata_crs             | text
 gbim_vector_publication          | source_table             | text
 gbim_vector_publication          | source_feature_id        | bigint
 promotion_events                 | id                       | uuid
 promotion_events                 | manifest_row_id          | uuid
 promotion_events                 | nonce                    | bigint
 promotion_events                 | issued_at                | timestamp with time zone
 promotion_events                 | issued_by                | text
 promotion_events                 | algorithm                | text
 promotion_events                 | public_key               | bytea
 promotion_events                 | signature                | bytea
 promotion_events                 | payload_sha256           | text
 promotion_events                 | signature_valid          | boolean
 promotion_events                 | coherence_ok             | boolean
(58 rows)

            table_name            |      column_name      |    foreign_table_name    |  foreign_column_name  |                       constraint_name                       
----------------------------------+-----------------------+--------------------------+-----------------------+-------------------------------------------------------------
 gbim_active_collection           | collection_version_id | gbim_collection_manifest | collection_version_id | gbim_active_collection_collection_version_id_fkey
 gbim_chroma_publication_manifest | collection_version_id | gbim_collection_manifest | collection_version_id | gbim_chroma_publication_manifest_collection_version_id_fkey
 gbim_vector_publication          | collection_version_id | gbim_collection_manifest | collection_version_id | gbim_vector_publication_collection_version_id_fkey
(3 rows)

                  id                  |           manifest_row_id            | nonce |           issued_at           |     issued_by     |     algorithm     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   public_key                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             signature                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                          payload_sha256                          | signature_valid | coherence_ok 
--------------------------------------+--------------------------------------+-------+-------------------------------+-------------------+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+-----------------+--------------
 57b59ac9-e5c9-4eeb-96c6-3583793f7510 | 4c6638de-274d-485c-bb64-ab078426a5a5 |     3 | 2026-07-16 18:27:43.390487+00 | msjarvis-operator | RSASSA-PSS-SHA256 | \x2d2d2d2d2d424547494e2043455254494649434154452d2d2d2d2d0a4d494946376a43434139616741774942416749555055493763435333474d714c514b396f57627a596546594641354d774451594a4b6f5a496876634e4151454c0a425141776444454c4d416b474131554542684d4356564d78437a414a42674e564241674d416c64574d524d7745515944565151484441704e62335675644342490a6233426c4d524577447759445651514b4441684e63307068636e5a70637a45524d4138474131554543777749535735305a584a75595777784854416242674e560a42414d4d4645317a536d4679646d6c7a49456c7564475679626d467349454e424d423458445449324d4463784e6a45314e5467304e6c6f58445449344d5441780a4f4445314e5467304e6c6f77627a454c4d416b474131554542684d4356564d78437a414a42674e564241674d416c64574d524d7745515944565151484441704e0a62335675644342496233426c4d524577447759445651514b4441684e63307068636e5a70637a45524d4138474131554543777749535735305a584a75595777780a4744415742674e5642414d4d4432317a616d4679646d6c7a4c574e736157567564444343416949774451594a4b6f5a496876634e4151454242514144676749500a4144434341676f4367674942414f464338304546612f69637a48664854624154654b544a366b59562b754b44497032776a435a64662f516c746846716e44542f0a6548343776764f34664a3063455067317530614f78415956692f4a6e686f74677556524e2f38445051783570544b784f2b454e5a7346554773786b75345244340a4c5951744d43474d6e63577a6c7755353538474b68752f51724b70726e34436c70675738366f4434597637316c44677059544b6e63684c496436376d6c532b480a46315242467043384c422b6b52575855704739476b43716c38454670683066304135793742674833486b734458384b49384d74324f3073392f4b7174326c62580a586353615368554d472b676739635637756b5939626c63572b696544514548484e59434d774f62546a72417058427442363142413653436172375564486e35720a6442616b6541695864765133686b4941576376317443445031466362493964366b525a374d5469484a6572716e335249723747787551354b3672504370594f330a6a7a37432b3634457a654a66785655693643494c4a5479773655546d76683950394952735961484779424e4b526b445252586456613249666c396a6c394e32790a322f726b7273346554685a4470796d65417470346e61483969546d2b39744a4f5969786954697976633737616e3761742f4f495274676a6a624c415a6e6e59390a39494241753970544954386e79585a5668546e42382f4d4154413557506b2b306a4631633571343746356778586249582b677a6844785062324f505163614c620a4f36346336615456716b75364f704767797045374a5a345131545a67474a654172515931507648646c57414c514d7a4847416c36385a6e6579324f77486337760a61446a6a474d726c697168533649546a514758636e75563271682b526d7932325079345a30645962416f343557302f463363694a312b496641674d424141476a0a665442374d426f4741315564455151544d4247434432317a616d4679646d6c7a4c574e73615756756444416442674e5648535545466a415542676772426745460a42516344415159494b7759424251554841774977485159445652304f4242594546466a677a736171654b6c4d732b4d544336507252587576357a66614d4238470a41315564497751594d42614146473270385243475633375071616c62364e70637a527350694150654d41304743537147534962334451454243775541413449430a415142496d55384656484f5a6e5234437a7a6468546c45597641553872566a6478355132637362485346632f48747953636a6b3951793557785159507331416f0a534b6f6b46635a73313547623052394441374b377370684c4346314d6e534c485651513631724d6454324b7a5a612f316e3957762b6d3445374d4357486c53660a476137304c5a5a5953642f3833304454615853454731454376364d51746f48475a43725052697232624d7332646b4c745479584b593577767a6e41746c726a370a6e57776f6e4d546f756b474e5759457059524963782f5a36376255376f336c33624859546e5941623149706366624e3471572f2f746550306a44362f315a692f0a7a7645366469665756646a596f32666a5a32316c6245587a6a2f5a4c6534686a703263624a4b563672444c44614b464437324e5554456148793165497248674f0a70737a654d3436367245446b6e50736d4a5a6a43374d31506b62524b63555459486c364b664e534b69766d61394968702f59615444442b4e574e3275364254310a5932497a56307467424b704b44414139576848526f6f2b58355875456e77514e6456776273535378622b4c79485474616f2f442b4f514e4e2f3467427041694d0a487955317a3537736c694655562f6864356b327779347364374158517a3534514f4d6a724f5169442f41617150776d7a643473694e59693353444c36787868500a6a3471423669416571634c6466682b596b2b7a6a435948562b47556c4745413966654e632b6e417a463436306159782b4a6d55326a4f3168796859684c44434c0a4e45326a3247764559356366336c487667324a6a3245325366442f4b547445714e306e487a477a687367627a483733447954452f5755596a462b32736e4959480a427a4a4c54494b496a4a4e52624c37734f5448514d7a78765666756a306d58774377315679304d76687935744e413d3d0a2d2d2d2d2d454e442043455254494649434154452d2d2d2d2d0a | \x5578bbd196f360b9601204b4e4f2d26f8e2b4820d9b40aea705f7c74ca8dadefa8a95a9ad12e3f93fc3b19adbbb8b13061c4ec4723080c939b8cb68695929b805fc24b69986053331fadf5a70f010fe799c9ed1cabf0ae2296e3ce2de731cabd4de10a8950a9cb8b01078cc490cf389c6593092ebaaa5edd14f2dd0215b461fcc8384ea80609dfd65c3ba83f4211d10e7e78c8165ef9f12b37a24c780715a2e08237573963865accf77f9c87a57803b159d6237e61d32396f692b5dc76c64326453d42d726b659f393cbce06ffa86df7d72a0bafc9385e9c59d074cbec54f720df91952fe90a3c69e13a72228d2d3afd842ead113d44dd004607f976df7ec8eb3d2d8593bcc8111d0daa18da627c294a53047113756b1f7874d780b1bf4de3394c23c931bc4b2bc43164f661a6bcd8c525cd0d8fbcf97bd44b6dbea386379695f0639e180edf2418873e278aad066898a501a37a590612f1f08dcb8e5085b0d3ea43c0ad83be1441d5f946822a270a095982c549f1dc7e0a56af335d4c588129ed8ac5c729000244d6ed52d258cf94baecf8d9256e7871200fa4c51a83f40da269b98cf42e2f068297c48d8bae61de098f8d7b190f34f7072b93f959dd090565555b6ee268194aca9b33e52e11319236a01039ef702393bb84ba6a275db03cc2f0d153bdb94eac56f88f250609bea4361187c364ee3a37742ad5f37ace2390b9 | 5ef51d8f4648b6554fa09220417f92cd778f419e0df7ca95c7e0f093f71fbea7 | t               | t
 2bf1c300-2563-4ff6-95e8-c38c8071ca7d | f43b510a-12d5-4855-a203-65a2690ae6b0 |     2 | 2026-07-16 18:12:12.126862+00 | msjarvis-operator | RSASSA-PSS-SHA256 | \x2d2d2d2d2d424547494e2043455254494649434154452d2d2d2d2d0a4d494946376a43434139616741774942416749555055493763435333474d714c514b396f57627a596546594641354d774451594a4b6f5a496876634e4151454c0a425141776444454c4d416b474131554542684d4356564d78437a414a42674e564241674d416c64574d524d7745515944565151484441704e62335675644342490a6233426c4d524577447759445651514b4441684e63307068636e5a70637a45524d4138474131554543777749535735305a584a75595777784854416242674e560a42414d4d4645317a536d4679646d6c7a49456c7564475679626d467349454e424d423458445449324d4463784e6a45314e5467304e6c6f58445449344d5441780a4f4445314e5467304e6c6f77627a454c4d416b474131554542684d4356564d78437a414a42674e564241674d416c64574d524d7745515944565151484441704e0a62335675644342496233426c4d524577447759445651514b4441684e63307068636e5a70637a45524d4138474131554543777749535735305a584a75595777780a4744415742674e5642414d4d4432317a616d4679646d6c7a4c574e736157567564444343416949774451594a4b6f5a496876634e4151454242514144676749500a4144434341676f4367674942414f464338304546612f69637a48664854624154654b544a366b59562b754b44497032776a435a64662f516c746846716e44542f0a6548343776764f34664a3063455067317530614f78415956692f4a6e686f74677556524e2f38445051783570544b784f2b454e5a7346554773786b75345244340a4c5951744d43474d6e63577a6c7755353538474b68752f51724b70726e34436c70675738366f4434597637316c44677059544b6e63684c496436376d6c532b480a46315242467043384c422b6b52575855704739476b43716c38454670683066304135793742674833486b734458384b49384d74324f3073392f4b7174326c62580a586353615368554d472b676739635637756b5939626c63572b696544514548484e59434d774f62546a72417058427442363142413653436172375564486e35720a6442616b6541695864765133686b4941576376317443445031466362493964366b525a374d5469484a6572716e335249723747787551354b3672504370594f330a6a7a37432b3634457a654a66785655693643494c4a5479773655546d76683950394952735961484779424e4b526b445252586456613249666c396a6c394e32790a322f726b7273346554685a4470796d65417470346e61483969546d2b39744a4f5969786954697976633737616e3761742f4f495274676a6a624c415a6e6e59390a39494241753970544954386e79585a5668546e42382f4d4154413557506b2b306a4631633571343746356778586249582b677a6844785062324f505163614c620a4f36346336615456716b75364f704767797045374a5a345131545a67474a654172515931507648646c57414c514d7a4847416c36385a6e6579324f77486337760a61446a6a474d726c697168533649546a514758636e75563271682b526d7932325079345a30645962416f343557302f463363694a312b496641674d424141476a0a665442374d426f4741315564455151544d4247434432317a616d4679646d6c7a4c574e73615756756444416442674e5648535545466a415542676772426745460a42516344415159494b7759424251554841774977485159445652304f4242594546466a677a736171654b6c4d732b4d544336507252587576357a66614d4238470a41315564497751594d42614146473270385243475633375071616c62364e70637a527350694150654d41304743537147534962334451454243775541413449430a415142496d55384656484f5a6e5234437a7a6468546c45597641553872566a6478355132637362485346632f48747953636a6b3951793557785159507331416f0a534b6f6b46635a73313547623052394441374b377370684c4346314d6e534c485651513631724d6454324b7a5a612f316e3957762b6d3445374d4357486c53660a476137304c5a5a5953642f3833304454615853454731454376364d51746f48475a43725052697232624d7332646b4c745479584b593577767a6e41746c726a370a6e57776f6e4d546f756b474e5759457059524963782f5a36376255376f336c33624859546e5941623149706366624e3471572f2f746550306a44362f315a692f0a7a7645366469665756646a596f32666a5a32316c6245587a6a2f5a4c6534686a703263624a4b563672444c44614b464437324e5554456148793165497248674f0a70737a654d3436367245446b6e50736d4a5a6a43374d31506b62524b63555459486c364b664e534b69766d61394968702f59615444442b4e574e3275364254310a5932497a56307467424b704b44414139576848526f6f2b58355875456e77514e6456776273535378622b4c79485474616f2f442b4f514e4e2f3467427041694d0a487955317a3537736c694655562f6864356b327779347364374158517a3534514f4d6a724f5169442f41617150776d7a643473694e59693353444c36787868500a6a3471423669416571634c6466682b596b2b7a6a435948562b47556c4745413966654e632b6e417a463436306159782b4a6d55326a4f3168796859684c44434c0a4e45326a3247764559356366336c487667324a6a3245325366442f4b547445714e306e487a477a687367627a483733447954452f5755596a462b32736e4959480a427a4a4c54494b496a4a4e52624c37734f5448514d7a78765666756a306d58774377315679304d76687935744e413d3d0a2d2d2d2d2d454e442043455254494649434154452d2d2d2d2d0a | \x4ca40b4df1fdf7b09c05a4e8d68aa65a6e0e254a871b1999365f2823c42fd8fa73fb443f5b4b524b7b20024f73627fbc1fa3d831943411066d1cad1a3361d5a372ec0ed9d1366dc9626dec366df81b038838fc1273ea6fe426fb89f50b95bc2ff53c7c5fc61184cb6aa94ee50a02588c73383c49690bff010b14219151cacd20c46010be9a5d49a5f06f13c77d7235e99630cfc9a0938cd7cfdf0e53f1df3ea0c298069ee782dc55ddb1c0706127f22df35ae2c537360c68d2eee5323abf1cd0e9af884fb9e7ce9f823b236a069280384479e32f51253f13072592ca907437983e058b17e58ace02e72fa36444c5c1db15aab58945b8c2a29d72433375fc95a990bf1d5e3a02551afa7ff56d815f9e8a0ddd37b5ecc74a247156625b4050af6ea848bb33c92389afa9f715d9d4b0c4e2ebf435fd7425a4d305b6ba8cc6d773a5fb02c5c5683f8aa078d69d4303691985ca010862caa45f25066c200d91d72378bc214c9a0c0f17341e357da7cf2d53b311267d024eea42500efe8d2861f96e214857bf9628c1bd3fcef61b3046014ca8ac6d6c1c1333ed5ea8b330e8702fe972d82e7aeb0750c4420b6ae0c064d68b8785e2327fc2a5d5a61f6386a2a0319f859203a8df494b2b155325fccb8395f2d68870cce02883f23297b4c8dc82b3952bc70fccfa02600846b92f2a3cfd447c215295543be4d46cb96dd2378cc93e72d8 | 4471fb17c30749a9392be1a9a553008beb600754971156bd4dac937d1f74aeaf | t               | t
 2a448844-fbe1-40cb-bb0d-2970059e3d99 | f43b510a-12d5-4855-a203-65a2690ae6b0 |     1 | 2026-07-16 18:08:08.748975+00 | msjarvis-operator | TEST-NONCRYPTO    | \x00                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | \x00                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                  | f               | f
(3 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/msjarvis-rebuild$ psql -h localhost -p 5432 -U postgres -d msjarvisgis <<'SQL'
\pset pager off

SELECT *
FROM gbim_chroma_publication_manifest
ORDER BY logical_collection_name;

SELECT *
FROM gbim_collection_manifest
WHERE collection_name IN ('gbim_wv_counties','gbim_wv_tracts','gbim_wv_blockgroups','gbim_wv_zctas')
ORDER BY collection_name, collection_version;

SELECT *
FROM gbim_vector_publication
ORDER BY 1
LIMIT 50;

SELECT *
FROM gbim_active_collection
ORDER BY 1
LIMIT 50;
SQL
Pager usage is off.
 logical_collection_name | physical_collection_name |        collection_version_id         |          updated_at           | permitted_use 
-------------------------+--------------------------+--------------------------------------+-------------------------------+---------------
 gbim_wv_blockgroups     | gbimwvblockgroupsv1      | 4c6638de-274d-485c-bb64-ab078426a5a5 | 2026-07-15 16:15:13.739685+00 | analysis
 gbim_wv_counties        | gbimwvcountiesv2         | f43b510a-12d5-4855-a203-65a2690ae6b0 | 2026-07-15 16:15:13.739685+00 | analysis
 gbim_wv_tracts          | gbimwvtractsv2           | fcac67c8-1ece-4f13-a18b-9e21809e8188 | 2026-07-15 16:15:13.739685+00 | analysis
(3 rows)

        collection_version_id         |   collection_name   | collection_version |             source_view              |     snapshot_version      |    rendering_version    |  embedding_model  | embedding_dimension | record_count |                         collection_hash                          | build_status |           permitted_use           |           built_at            |         validated_at          |          promoted_at          |         superseded_at         |                                                                                                                                                                                                                                                         notes                                                                                                                                                                                                                                                          
--------------------------------------+---------------------+--------------------+--------------------------------------+---------------------------+-------------------------+-------------------+---------------------+--------------+------------------------------------------------------------------+--------------+-----------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 4c6638de-274d-485c-bb64-ab078426a5a5 | gbim_wv_blockgroups | v1                 | wv_blockgroup_belief_vector_ready    | wv-blockgroup-snapshot-v1 | blockgroup-render-v1    | all-minilm:latest |                 384 |         1639 | 1368a33250945109fb8c293fac1a48b0b66f9c61a50d1061fa9d5f6c70b5b2d4 | superseded   | public_civic_geographic_retrieval | 2026-07-11 19:12:07.933882+00 | 2026-07-15 03:33:42.829679+00 | 2026-07-11 19:12:33.45012+00  | 2026-07-17 15:22:21.617483+00 | First governed block-group belief collection | Physical Chroma lineage repaired and revalidated against all 1,639 verified publication rows; hybrid GEOID retrieval accepted; previous physical collection retained in quarantine. | Superseded by v2 (59ad7b32-2d88-4578-9e57-7c883f44a720) 2026-07-16 after acceptance test.
 59ad7b32-2d88-4578-9e57-7c883f44a720 | gbim_wv_blockgroups | v2                 | wv_blockgroup_belief_vector_ready_v2 | wv-blockgroup-snapshot-v2 | blockgroup-v2-banded-v1 | all-minilm:latest |                 384 |         1639 | 6e861ab596c1eb74c207b7398de073cc943421a5147ca37c0bec74692474005e | active       | public_civic_geographic_retrieval | 2026-07-15 16:15:13.739685+00 | 2026-07-15 16:15:13.739685+00 | 2026-07-17 15:22:21.566681+00 |                               | Validated governed block-group v2 physical collection gbimwvblockgroupsv2; four-layer coverage; 724 invalid source geometries repaired without row loss; calibrated hybrid semantic acceptance passed at top-1; awaiting consumer activation. | Promoted 2026-07-16 after live acceptance test on gbimwvblockgroupsv2governedcandidate: exact-GEOID query returned distance 0.0 on 540019655001; semantic floodplain query returned 5 relevant Barbour County hits (distance 0.44-0.45) with full coverage provenance.
 f43b510a-12d5-4855-a203-65a2690ae6b0 | gbim_wv_counties    | v1                 | wv_county_belief_vector_ready        | wv-county-snapshot-v1     | county-render-v1        | all-minilm:latest |                 384 |           55 | 2611039d50da6e37664a96a314ab77879aaf0861f80390a761a0067275f0720a | active       | public_civic_geographic_retrieval | 2026-07-11 18:41:45.712014+00 | 2026-07-15 04:22:55.269141+00 | 2026-07-11 18:46:18.531273+00 |                               | First governed county belief collection | Canonical physical lineage reconciled and revalidated through GIS-RAG during Chapter 46 closure.
 a5a8716d-02aa-4cf7-8f28-81fcf7a8749d | gbim_wv_tracts      | v1                 | wv_tract_belief_vector_ready         | wv-tract-snapshot-v1      | tract-render-v1         | all-minilm:latest |                 384 |          546 |                                                                  | superseded   | public_civic_geographic_retrieval | 2026-07-11 19:03:08.245313+00 | 2026-07-11 19:08:19.127298+00 | 2026-07-11 19:04:35.713377+00 | 2026-07-15 04:22:55.269141+00 | First governed tract belief collection | Superseded by canonical tract v2 after Chapter 46 consumer acceptance.
 fcac67c8-1ece-4f13-a18b-9e21809e8188 | gbim_wv_tracts      | v2                 | wv_tract_belief_vector_ready_v2      | wv-tract-snapshot-v2      | tract-render-v2         | all-minilm:latest |                 384 |          546 | c5dc5e30c58e104bc89ba3f58bb8d6a5d7f3b2bdbd025d2241007ead26cff09e | active       | public_civic_geographic_retrieval | 2026-07-15 04:05:02.984473+00 | 2026-07-15 04:22:55.269141+00 | 2026-07-15 04:22:55.269141+00 |                               | Chapter 46 canonical three-grain lineage reconciliation. | County lineage repaired for all 546 tracts; canonical physical publication accepted through exact and county-restricted semantic retrieval.
 49e820bd-4f9b-42f6-a7fb-2f36e22f82e0 | gbim_wv_zctas       | v1                 | wv_zcta_belief_vector_ready          | wv-zcta-snapshot-v1       | zcta-render-v1          | all-minilmlatest  |                 384 |          741 |                                                                  | active       | public_civic_geographic_retrieval | 2026-07-11 19:20:22.231766+00 | 2026-07-11 19:20:22.231766+00 | 2026-07-11 19:20:43.87546+00  |                               | First governed ZCTA belief collection
(6 rows)

            publication_id            |        collection_version_id         |                           document_id                            | canonical_entity_id  |                           belief_hash                            |     snapshot_version      |                         chroma_record_id                         | publication_status |         published_at          |          verified_at          | error_message |    centroid_lat    |    centroid_lon    |    bbox_min_lon    |    bbox_min_lat    |    bbox_max_lon    |    bbox_max_lat    | source_crs | metadata_crs |               source_table               | source_feature_id 
--------------------------------------+--------------------------------------+------------------------------------------------------------------+----------------------+------------------------------------------------------------------+---------------------------+------------------------------------------------------------------+--------------------+-------------------------------+-------------------------------+---------------+--------------------+--------------------+--------------------+--------------------+--------------------+--------------------+------------+--------------+------------------------------------------+-------------------
 0003362c-cbb6-4047-a5f8-4672f457733f | a5a8716d-02aa-4cf7-8f28-81fcf7a8749d | 05440fda80042020dffe2f4c15f1ec74744d897deb72986d27cfd8baddefa77b | 54069000600          | 05440fda80042020dffe2f4c15f1ec74744d897deb72986d27cfd8baddefa77b | wv-tract-snapshot-v1      | 05440fda80042020dffe2f4c15f1ec74744d897deb72986d27cfd8baddefa77b | verified           | 2026-07-11 19:03:08.245313+00 | 2026-07-11 19:03:08.245313+00 |               |                    |                    |                    |                    |                    |                    |            |              |                                          |                  
 00074a7b-6f44-4047-85a7-1c6f019e3065 | 49e820bd-4f9b-42f6-a7fb-2f36e22f82e0 | ea3e1ff5ec7ab9e1d3a05d54a50dd03609f786ab42fa5b7e58f6ef40ca128db9 | 26519                | ea3e1ff5ec7ab9e1d3a05d54a50dd03609f786ab42fa5b7e58f6ef40ca128db9 | wv-zcta-snapshot-v1       | ea3e1ff5ec7ab9e1d3a05d54a50dd03609f786ab42fa5b7e58f6ef40ca128db9 | verified           | 2026-07-11 19:20:22.231766+00 | 2026-07-11 19:20:22.231766+00 |               |                    |                    |                    |                    |                    |                    |            |              |                                          |                  
 00147196-8701-4a6f-83fd-fb7a92f1f7d6 | 4c6638de-274d-485c-bb64-ab078426a5a5 | dcda7790be928b003a111544abe7c98ce75bad7959a27b109d77074d284e23d6 | 540690014004         | dcda7790be928b003a111544abe7c98ce75bad7959a27b109d77074d284e23d6 | wv-blockgroup-snapshot-v1 | dcda7790be928b003a111544abe7c98ce75bad7959a27b109d77074d284e23d6 | verified           | 2026-07-11 19:12:07.933882+00 | 2026-07-15 04:22:55.269141+00 |               | 40.065933499999986 | -80.68138491748526 |         -80.684435 |  40.05964099999999 | -80.67808700000002 |  40.07215299999999 | EPSG:26917 | EPSG:4326    | public.wv_blockgroups_census_2020_utm83  |               140
 001e9423-a9c6-4f1e-9aef-8a32f36bd150 | 4c6638de-274d-485c-bb64-ab078426a5a5 | 6eeb14a7e1844cdb8b8cbc8986f0613fe3396b8fa97b17e3123e1143d674373f | 540990205003         | 6eeb14a7e1844cdb8b8cbc8986f0613fe3396b8fa97b17e3123e1143d674373f | wv-blockgroup-snapshot-v1 | 6eeb14a7e1844cdb8b8cbc8986f0613fe3396b8fa97b17e3123e1143d674373f | verified           | 2026-07-11 19:12:07.933882+00 | 2026-07-15 04:22:55.269141+00 |               |  38.28006549999999 | -82.40425958974802 | -82.45908300000009 |  38.24341399999999 | -82.32788400000004 |  38.31671099999999 | EPSG:26917 | EPSG:4326    | public.wv_blockgroups_census_2020_utm83  |               935
 003dca97-af8e-4c83-90a0-3b80af9be71f | 59ad7b32-2d88-4578-9e57-7c883f44a720 | e117d19a04263c0c5d1d166fb66c84c2790245b2aed5c281878d9ad41383e6b6 | 540179650001         | e117d19a04263c0c5d1d166fb66c84c2790245b2aed5c281878d9ad41383e6b6 | wv-blockgroup-snapshot-v2 | e117d19a04263c0c5d1d166fb66c84c2790245b2aed5c281878d9ad41383e6b6 | verified           | 2026-07-15 16:15:13.739685+00 | 2026-07-15 16:15:13.739685+00 |               |  39.37851781948974 | -80.58366986776464 |         -80.733229 | 39.305677999999986 |         -80.531808 |  39.45141499999998 | EPSG:26917 | EPSG:4326    | public.wv_blockgroups_census_2020_utm83  |      540179650001
 003f9a4f-e1e9-4c13-be3a-757ce236377b | 49e820bd-4f9b-42f6-a7fb-2f36e22f82e0 | 5badbe69a082bcd62148d074057d3ad1fad5d3f06561c7047237e368af5f243e | 26378                | 5badbe69a082bcd62148d074057d3ad1fad5d3f06561c7047237e368af5f243e | wv-zcta-snapshot-v1       | 5badbe69a082bcd62148d074057d3ad1fad5d3f06561c7047237e368af5f243e | verified           | 2026-07-11 19:20:22.231766+00 | 2026-07-11 19:20:22.231766+00 |               |                    |                    |                    |                    |                    |                    |            |              |                                          |                  
 0048cb7c-a41f-4efb-82aa-0dee560dfe7c | 4c6638de-274d-485c-bb64-ab078426a5a5 | 766870e19cb7d182866e57b119f9a8c75c94b4907fc26bb555806927fa7d0cf5 | 540330314001         | 766870e19cb7d182866e57b119f9a8c75c94b4907fc26bb555806927fa7d0cf5 | wv-blockgroup-snapshot-v1 | 766870e19cb7d182866e57b119f9a8c75c94b4907fc26bb555806927fa7d0cf5 | verified           | 2026-07-11 19:12:07.933882+00 | 2026-07-15 04:22:55.269141+00 |               |  39.21615849999999 |   -80.405781715876 |          -80.41975 | 39.196706999999996 |         -80.374921 |          39.235603 | EPSG:26917 | EPSG:4326    | public.wv_blockgroups_census_2020_utm83  |               283
 0049f0af-7fff-414e-953f-2028471e4b6b | 59ad7b32-2d88-4578-9e57-7c883f44a720 | 99832647c4a1ee008ca8ee658deb33f8adce4d9fc9397653461e74782f9f740b | 540039718022         | 99832647c4a1ee008ca8ee658deb33f8adce4d9fc9397653461e74782f9f740b | wv-blockgroup-snapshot-v2 | 99832647c4a1ee008ca8ee658deb33f8adce4d9fc9397653461e74782f9f740b | verified           | 2026-07-15 16:15:13.739685+00 | 2026-07-15 16:15:13.739685+00 |               |  39.43156569070945 | -78.05876609462344 | -78.10967860401661 |   39.3896218914982 | -78.01980322093095 | 39.474343951407164 | EPSG:26917 | EPSG:4326    | public.wv_blockgroups_census_2020_utm83  |      540039718022
 004ad1de-452f-41a3-88b2-6edc0679d1f5 | 4c6638de-274d-485c-bb64-ab078426a5a5 | d7646be4adc35f0d50ecddf95467e421fa2c8c4e6836c242bd289995669cc728 | 540039711042         | d7646be4adc35f0d50ecddf95467e421fa2c8c4e6836c242bd289995669cc728 | wv-blockgroup-snapshot-v1 | d7646be4adc35f0d50ecddf95467e421fa2c8c4e6836c242bd289995669cc728 | verified           | 2026-07-11 19:12:07.933882+00 | 2026-07-15 04:22:55.269141+00 |               |  39.58064562176334 | -77.90709706537265 | -77.94215386618114 |  39.56244411690087 | -77.87077461506884 | 39.598824118934296 | EPSG:26917 | EPSG:4326    | public.wv_blockgroups_census_2020_utm83  |               504
 004ba0ef-7fea-48ff-a091-9a14d7393037 | a5a8716d-02aa-4cf7-8f28-81fcf7a8749d | 182a6342d67dfae1b247bdb30bc3e1088ecbbbc1ea254f9ac6fa5d813552e60a | 54039000600          | 182a6342d67dfae1b247bdb30bc3e1088ecbbbc1ea254f9ac6fa5d813552e60a | wv-tract-snapshot-v1      | 182a6342d67dfae1b247bdb30bc3e1088ecbbbc1ea254f9ac6fa5d813552e60a | verified           | 2026-07-11 19:03:08.245313+00 | 2026-07-11 19:03:08.245313+00 |               |                    |                    |                    |                    |                    |                    |            |              |                                          |                  
 004e80e7-d167-476d-b83d-0cb8e4329db9 | 49e820bd-4f9b-42f6-a7fb-2f36e22f82e0 | ae32e09ea6f9eeb3d722d58b42a7015a2e7240c09693509fb943552ef0ea5b70 | 24846                | ae32e09ea6f9eeb3d722d58b42a7015a2e7240c09693509fb943552ef0ea5b70 | wv-zcta-snapshot-v1       | ae32e09ea6f9eeb3d722d58b42a7015a2e7240c09693509fb943552ef0ea5b70 | verified           | 2026-07-11 19:20:22.231766+00 | 2026-07-11 19:20:22.231766+00 |               |                    |                    |                    |                    |                    |                    |            |              |                                          |                  
 005bea8c-4e12-4cf8-9db0-550d806e01c6 | 4c6638de-274d-485c-bb64-ab078426a5a5 | 14a6918691f1b5d57db7e95d40962ce864b1836e86f2cf1710e670baf8c3e5b5 | 540019655003         | 14a6918691f1b5d57db7e95d40962ce864b1836e86f2cf1710e670baf8c3e5b5 | wv-blockgroup-snapshot-v1 | 14a6918691f1b5d57db7e95d40962ce864b1836e86f2cf1710e670baf8c3e5b5 | verified           | 2026-07-11 19:12:07.933882+00 | 2026-07-15 04:22:55.269141+00 |               |  39.08723799999999 |  -80.1141194650124 |         -80.227173 | 39.037731999999984 |         -80.038651 | 39.137237999999996 | EPSG:26917 | EPSG:4326    | public.wv_blockgroups_census_2020_utm83  |               191
 0063dde3-8b05-4d54-adfe-270e2c6e1903 | a5a8716d-02aa-4cf7-8f28-81fcf7a8749d | ba66d35e098ca0b283e6c755f0a3529afb0265d10f9249bf76189b05160c14f7 | 54107000802          | ba66d35e098ca0b283e6c755f0a3529afb0265d10f9249bf76189b05160c14f7 | wv-tract-snapshot-v1      | ba66d35e098ca0b283e6c755f0a3529afb0265d10f9249bf76189b05160c14f7 | verified           | 2026-07-11 19:03:08.245313+00 | 2026-07-11 19:03:08.245313+00 |               |                    |                    |                    |                    |                    |                    |            |              |                                          |                  
 007e7cd1-48a6-4f4d-9d41-76616d8ba8b6 | 59ad7b32-2d88-4578-9e57-7c883f44a720 | 2b75793dc972e98a5c46f612c561513df8df81218699b90c28060011db83612b | 540390113011         | 2b75793dc972e98a5c46f612c561513df8df81218699b90c28060011db83612b | wv-blockgroup-snapshot-v2 | 2b75793dc972e98a5c46f612c561513df8df81218699b90c28060011db83612b | verified           | 2026-07-15 16:15:13.739685+00 | 2026-07-15 16:15:13.739685+00 |               |   38.3617751301582 | -81.42375456927144 |         -81.502216 | 38.320574999999984 |         -81.366748 | 38.402944999999995 | EPSG:26917 | EPSG:4326    | public.wv_blockgroups_census_2020_utm83  |      540390113011
 0080d67b-663b-4c37-8c80-231d7b3803db | 49e820bd-4f9b-42f6-a7fb-2f36e22f82e0 | c1f8450579768e2410b2dbfafaba931d17538c34f587c28ca40f35f416db1262 | 25670                | c1f8450579768e2410b2dbfafaba931d17538c34f587c28ca40f35f416db1262 | wv-zcta-snapshot-v1       | c1f8450579768e2410b2dbfafaba931d17538c34f587c28ca40f35f416db1262 | verified           | 2026-07-11 19:20:22.231766+00 | 2026-07-11 19:20:22.231766+00 |               |                    |                    |                    |                    |                    |                    |            |              |                                          |                  
 0090a0de-fabc-4ec1-8cdb-bddf39433698 | 59ad7b32-2d88-4578-9e57-7c883f44a720 | c93e5aa68033ee8c7d9e1bad7a5a28e2230bdfafc5f52a33837f0fdf197396cb | 540439557001         | c93e5aa68033ee8c7d9e1bad7a5a28e2230bdfafc5f52a33837f0fdf197396cb | wv-blockgroup-snapshot-v2 | c93e5aa68033ee8c7d9e1bad7a5a28e2230bdfafc5f52a33837f0fdf197396cb | verified           | 2026-07-15 16:15:13.739685+00 | 2026-07-15 16:15:13.739685+00 |               | 38.053129113484594 | -82.16591931617074 | -82.23968000000004 |          38.001738 | -82.11263100000001 |  38.10393199999999 | EPSG:26917 | EPSG:4326    | public.wv_blockgroups_census_2020_utm83  |      540439557001
 00c59ef9-cfe2-4112-93e7-8f997cfff087 | 49e820bd-4f9b-42f6-a7fb-2f36e22f82e0 | 98542de6bd1bedd1f449118e87f0337da3a015ef33f2265fef7cf0ae5620dfca | 24828                | 98542de6bd1bedd1f449118e87f0337da3a015ef33f2265fef7cf0ae5620dfca | wv-zcta-snapshot-v1       | 98542de6bd1bedd1f449118e87f0337da3a015ef33f2265fef7cf0ae5620dfca | verified           | 2026-07-11 19:20:22.231766+00 | 2026-07-11 19:20:22.231766+00 |               |                    |                    |                    |                    |                    |                    |            |              |                                          |                  
 00c7ccbc-455f-41a7-b425-2258641fb22e | 59ad7b32-2d88-4578-9e57-7c883f44a720 | edebb38ce94c712df788e116751a2f9a8b79defafbcfaa3de338e2b8735b013f | 540390134002         | edebb38ce94c712df788e116751a2f9a8b79defafbcfaa3de338e2b8735b013f | wv-blockgroup-snapshot-v2 | edebb38ce94c712df788e116751a2f9a8b79defafbcfaa3de338e2b8735b013f | verified           | 2026-07-15 16:15:13.739685+00 | 2026-07-15 16:15:13.739685+00 |               |  38.37811388537578 | -81.80066632305551 |         -81.807096 | 38.375288999999995 |         -81.793684 |  38.38104700000002 | EPSG:26917 | EPSG:4326    | public.wv_blockgroups_census_2020_utm83  |      540390134002
 00dace49-6f3d-4c4a-aa0c-9f33773cc546 | 49e820bd-4f9b-42f6-a7fb-2f36e22f82e0 | 60553cbebba2084f05c4da7765d7fdec9e0b95bab613ddc96d867633553cce6d | 25234                | 60553cbebba2084f05c4da7765d7fdec9e0b95bab613ddc96d867633553cce6d | wv-zcta-snapshot-v1       | 60553cbebba2084f05c4da7765d7fdec9e0b95bab613ddc96d867633553cce6d | verified           | 2026-07-11 19:20:22.231766+00 | 2026-07-11 19:20:22.231766+00 |               |                    |                    |                    |                    |                    |                    |            |              |                                          |                  
 00eb1994-b6cb-45b0-b418-63535c380961 | fcac67c8-1ece-4f13-a18b-9e21809e8188 | 19cc5fb1d6945eafb51cd3ebd3febea35c0b5f9e2a194c3e252b8c2f4d52684e | 1400000US54081000500 | 19cc5fb1d6945eafb51cd3ebd3febea35c0b5f9e2a194c3e252b8c2f4d52684e | wv-tract-snapshot-v2      | 19cc5fb1d6945eafb51cd3ebd3febea35c0b5f9e2a194c3e252b8c2f4d52684e | verified           | 2026-07-15 04:22:55.269141+00 | 2026-07-15 04:22:55.269141+00 |               |  37.80800949999999 | -81.19870258139971 |         -81.215347 | 37.786094999999996 |         -81.173464 | 37.829684999999984 | EPSG:26917 | EPSG:4326    | public.wv_censustracts_census_2020_utm83 |               271
 00efdb02-d923-4b0f-9a5a-988298bcd6f4 | fcac67c8-1ece-4f13-a18b-9e21809e8188 | a669dffcd6c3b80a1e1bb120cb59e4f489f9f324c709b54e47f7a9c0285f7bf1 | 1400000US54107000100 | a669dffcd6c3b80a1e1bb120cb59e4f489f9f324c709b54e47f7a9c0285f7bf1 | wv-tract-snapshot-v2      | a669dffcd6c3b80a1e1bb120cb59e4f489f9f324c709b54e47f7a9c0285f7bf1 | verified           | 2026-07-15 04:22:55.269141+00 | 2026-07-15 04:22:55.269141+00 |               |          39.293133 | -81.52420665363903 |         -81.543052 |          39.283039 |         -81.504616 |  39.30322600000001 | EPSG:26917 | EPSG:4326    | public.wv_censustracts_census_2020_utm83 |               497
 00f40e7b-8607-40fb-9449-a91d6d534c1b | 49e820bd-4f9b-42f6-a7fb-2f36e22f82e0 | 44e145d2e37226c09aa7ca5f6f114ed7cb6db17bdf6fae49d2489e38a4f773b5 | 26372                | 44e145d2e37226c09aa7ca5f6f114ed7cb6db17bdf6fae49d2489e38a4f773b5 | wv-zcta-snapshot-v1       | 44e145d2e37226c09aa7ca5f6f114ed7cb6db17bdf6fae49d2489e38a4f773b5 | verified           | 2026-07-11 19:20:22.231766+00 | 2026-07-11 19:20:22.231766+00 |               |                    |                    |                    |                    |                    |                    |            |              |                                          |                  
 00fe5c3e-1332-409f-9ecb-adfadfdae947 | 4c6638de-274d-485c-bb64-ab078426a5a5 | c5b4e2221815ab3f0d37ccc9a03cb0638470e23467774716a17318fa8a1633f5 | 540570107001         | c5b4e2221815ab3f0d37ccc9a03cb0638470e23467774716a17318fa8a1633f5 | wv-blockgroup-snapshot-v1 | c5b4e2221815ab3f0d37ccc9a03cb0638470e23467774716a17318fa8a1633f5 | verified           | 2026-07-11 19:12:07.933882+00 | 2026-07-15 04:22:55.269141+00 |               |  39.36694471827907 | -79.17810877780866 | -79.27169361574119 |    39.314975887971 | -79.12714057241645 |  39.41888564317238 | EPSG:26917 | EPSG:4326    | public.wv_blockgroups_census_2020_utm83  |              1015
 01098f6f-8b29-41d6-9ba1-d33552f96967 | a5a8716d-02aa-4cf7-8f28-81fcf7a8749d | ef6f79a7f033d30dd0265e540c5d3ed55fe5aeb227765b5ea7f7478dfd8c9907 | 54011010600          | ef6f79a7f033d30dd0265e540c5d3ed55fe5aeb227765b5ea7f7478dfd8c9907 | wv-tract-snapshot-v1      | ef6f79a7f033d30dd0265e540c5d3ed55fe5aeb227765b5ea7f7478dfd8c9907 | verified           | 2026-07-11 19:03:08.245313+00 | 2026-07-11 19:03:08.245313+00 |               |                    |                    |                    |                    |                    |                    |            |              |                                          |                  
 010ea304-6d75-420b-88e3-e97bb11f41de | 49e820bd-4f9b-42f6-a7fb-2f36e22f82e0 | 1890351d599f6ab6776b4020ed59e7355778831c2dcf034308abf14b58030699 | 25674                | 1890351d599f6ab6776b4020ed59e7355778831c2dcf034308abf14b58030699 | wv-zcta-snapshot-v1       | 1890351d599f6ab6776b4020ed59e7355778831c2dcf034308abf14b58030699 | verified           | 2026-07-11 19:20:22.231766+00 | 2026-07-11 19:20:22.231766+00 |               |                    |                    |                    |                    |                    |                    |            |              |                                          |                  
 01357587-2314-434d-897b-5591843635d8 | 49e820bd-4f9b-42f6-a7fb-2f36e22f82e0 | 571b6e0904ede8d40ebe8ccb872ff46b0b4d397d381a712a7f7d0e7e889547fd | 24868                | 571b6e0904ede8d40ebe8ccb872ff46b0b4d397d381a712a7f7d0e7e889547fd | wv-zcta-snapshot-v1       | 571b6e0904ede8d40ebe8ccb872ff46b0b4d397d381a712a7f7d0e7e889547fd | verified           | 2026-07-11 19:20:22.231766+00 | 2026-07-11 19:20:22.231766+00 |               |                    |                    |                    |                    |                    |                    |            |              |                                          |                  
 01371277-f3fd-4fc5-a287-f612c5e9e314 | 4c6638de-274d-485c-bb64-ab078426a5a5 | e7721a6bd737145910455068c6de2e8a9ce1d8973114662b4190e0acf9aa75ad | 540279683011         | e7721a6bd737145910455068c6de2e8a9ce1d8973114662b4190e0acf9aa75ad | wv-blockgroup-snapshot-v1 | e7721a6bd737145910455068c6de2e8a9ce1d8973114662b4190e0acf9aa75ad | verified           | 2026-07-11 19:12:07.933882+00 | 2026-07-15 04:22:55.269141+00 |               | 39.356890055510476 | -78.65663995641398 | -78.71423493991621 |  39.31189257106456 | -78.60158373875932 |  39.40186144390811 | EPSG:26917 | EPSG:4326    | public.wv_blockgroups_census_2020_utm83  |              1620
 013cc555-bbf3-49e9-be46-844fdb15d6f5 | fcac67c8-1ece-4f13-a18b-9e21809e8188 | dd5740a4f7e1644cf0a9a96ab4dc89f3273f4b29a0034dc92595c0380ea8c22f | 1400000US54009031103 | dd5740a4f7e1644cf0a9a96ab4dc89f3273f4b29a0034dc92595c0380ea8c22f | wv-tract-snapshot-v2      | dd5740a4f7e1644cf0a9a96ab4dc89f3273f4b29a0034dc92595c0380ea8c22f | verified           | 2026-07-15 04:22:55.269141+00 | 2026-07-15 04:22:55.269141+00 |               |  40.38773549999999 | -80.61367575627102 |         -80.632732 | 40.376555999999994 |         -80.584971 |  40.39887499999999 | EPSG:26917 | EPSG:4326    | public.wv_censustracts_census_2020_utm83 |                52
 01537736-e35d-44aa-9549-ead95253f545 | 59ad7b32-2d88-4578-9e57-7c883f44a720 | 393af251b3261a452c8d75d8583a41ee7718903623fbf2684a11ce780eaf283f | 540679506004         | 393af251b3261a452c8d75d8583a41ee7718903623fbf2684a11ce780eaf283f | wv-blockgroup-snapshot-v2 | 393af251b3261a452c8d75d8583a41ee7718903623fbf2684a11ce780eaf283f | verified           | 2026-07-15 16:15:13.739685+00 | 2026-07-15 16:15:13.739685+00 |               |  38.19199582740023 | -80.65574042350327 |         -80.818924 | 38.081382999999995 |         -80.586191 |          38.302902 | EPSG:26917 | EPSG:4326    | public.wv_blockgroups_census_2020_utm83  |      540679506004
 0159de9d-33f4-4a37-a5a0-e4c8fa594683 | 59ad7b32-2d88-4578-9e57-7c883f44a720 | 76eabe8a3b947b2c2980dd04fbeab731004acaae521321dc04a03c539040725c | 540379725031         | 76eabe8a3b947b2c2980dd04fbeab731004acaae521321dc04a03c539040725c | wv-blockgroup-snapshot-v2 | 76eabe8a3b947b2c2980dd04fbeab731004acaae521321dc04a03c539040725c | verified           | 2026-07-15 16:15:13.739685+00 | 2026-07-15 16:15:13.739685+00 |               | 39.316510798610345 | -77.82963544876804 | -77.83794015574392 | 39.307183497966385 | -77.81953407558618 |  39.32591744304156 | EPSG:26917 | EPSG:4326    | public.wv_blockgroups_census_2020_utm83  |      540379725031
 0164951a-7d17-40f1-b0db-a022dd9ffff9 | 4c6638de-274d-485c-bb64-ab078426a5a5 | 4e43742d95189298a680142e884cfaaa76ba1536fa0d8994d9fa9828d686ae76 | 541070008021         | 4e43742d95189298a680142e884cfaaa76ba1536fa0d8994d9fa9828d686ae76 | wv-blockgroup-snapshot-v1 | 4e43742d95189298a680142e884cfaaa76ba1536fa0d8994d9fa9828d686ae76 | verified           | 2026-07-11 19:12:07.933882+00 | 2026-07-15 04:22:55.269141+00 |               | 39.237432999999996 |  -81.5194583101007 |         -81.536456 |  39.21894799999999 |         -81.510481 |  39.25580899999999 | EPSG:26917 | EPSG:4326    | public.wv_blockgroups_census_2020_utm83  |               632
 016bfcb7-47fc-46e5-bd29-37edd71ed2b7 | 59ad7b32-2d88-4578-9e57-7c883f44a720 | 97b6168211fc5247ae5cfb051f921c8973f870e5ba5db05d1ce8c3fe8e349512 | 540839665002         | 97b6168211fc5247ae5cfb051f921c8973f870e5ba5db05d1ce8c3fe8e349512 | wv-blockgroup-snapshot-v2 | 97b6168211fc5247ae5cfb051f921c8973f870e5ba5db05d1ce8c3fe8e349512 | verified           | 2026-07-15 16:15:13.739685+00 | 2026-07-15 16:15:13.739685+00 |               |  38.72061502308276 | -79.88343956023496 |         -79.979466 |  38.59852599999999 | -79.72052199999997 |  38.84132699999999 | EPSG:26917 | EPSG:4326    | public.wv_blockgroups_census_2020_utm83  |      540839665002
 0183fcac-bebd-4338-a4d7-eefa1587148c | 49e820bd-4f9b-42f6-a7fb-2f36e22f82e0 | 6996b255b80ea736baf4ff6f3a7e05e8572bcf5282757b4959f0dcf75ae4dac2 | 26585                | 6996b255b80ea736baf4ff6f3a7e05e8572bcf5282757b4959f0dcf75ae4dac2 | wv-zcta-snapshot-v1       | 6996b255b80ea736baf4ff6f3a7e05e8572bcf5282757b4959f0dcf75ae4dac2 | verified           | 2026-07-11 19:20:22.231766+00 | 2026-07-11 19:20:22.231766+00 |               |                    |                    |                    |                    |                    |                    |            |              |                                          |                  
 019b274f-7256-41f5-9620-9f6e52dde6c6 | 4c6638de-274d-485c-bb64-ab078426a5a5 | c38f691e152f6d6429e51f088a547d359f3f8f1c99d9662880a82bf40c2cabec | 540510213004         | c38f691e152f6d6429e51f088a547d359f3f8f1c99d9662880a82bf40c2cabec | wv-blockgroup-snapshot-v1 | c38f691e152f6d6429e51f088a547d359f3f8f1c99d9662880a82bf40c2cabec | verified           | 2026-07-11 19:12:07.933882+00 | 2026-07-15 04:22:55.269141+00 |               | 40.009096499999984 | -80.71044457113402 |         -80.733459 |          39.991439 |         -80.680318 |           40.02653 | EPSG:26917 | EPSG:4326    | public.wv_blockgroups_census_2020_utm83  |               412
 01afc335-205a-4d70-9a52-c712ee4d3ee4 | 59ad7b32-2d88-4578-9e57-7c883f44a720 | 80526111512953887b50702a7c099bb785732d21f78ccd19110f18ff28b5f68a | 540810008042         | 80526111512953887b50702a7c099bb785732d21f78ccd19110f18ff28b5f68a | wv-blockgroup-snapshot-v2 | 80526111512953887b50702a7c099bb785732d21f78ccd19110f18ff28b5f68a | verified           | 2026-07-15 16:15:13.739685+00 | 2026-07-15 16:15:13.739685+00 |               | 37.725672058245635 |  -81.1185043658523 |         -81.156018 |  37.70189499999999 |          -81.10161 | 37.749417999999984 | EPSG:26917 | EPSG:4326    | public.wv_blockgroups_census_2020_utm83  |      540810008042
 01b06c2d-a935-4765-867d-316bcbf7f520 | 59ad7b32-2d88-4578-9e57-7c883f44a720 | 8e44a52144ecbe75b2e8015df69480883cb68b292e183df563ecb06a8f4d74c4 | 540179651002         | 8e44a52144ecbe75b2e8015df69480883cb68b292e183df563ecb06a8f4d74c4 | wv-blockgroup-snapshot-v2 | 8e44a52144ecbe75b2e8015df69480883cb68b292e183df563ecb06a8f4d74c4 | verified           | 2026-07-15 16:15:13.739685+00 | 2026-07-15 16:15:13.739685+00 |               |  39.30910553769433 | -80.83353805211908 |          -80.91384 |  39.26860599999999 |         -80.777082 |  39.34953499999999 | EPSG:26917 | EPSG:4326    | public.wv_blockgroups_census_2020_utm83  |      540179651002
 01b2c4d6-5041-40f8-a427-368bca8fda41 | 4c6638de-274d-485c-bb64-ab078426a5a5 | 7f4c71f754452a6e0269ca063c9f2fe81417f5cd29636f09ae4c0d40aa86d7d2 | 540679507001         | 7f4c71f754452a6e0269ca063c9f2fe81417f5cd29636f09ae4c0d40aa86d7d2 | wv-blockgroup-snapshot-v1 | 7f4c71f754452a6e0269ca063c9f2fe81417f5cd29636f09ae4c0d40aa86d7d2 | verified           | 2026-07-11 19:12:07.933882+00 | 2026-07-15 04:22:55.269141+00 |               |         38.1501105 | -80.77842260286457 |         -80.842785 | 38.079128999999995 |         -80.699463 | 38.221122999999984 | EPSG:26917 | EPSG:4326    | public.wv_blockgroups_census_2020_utm83  |               184
 01b3a5e2-bb52-4090-b46e-1d4f019d8cbc | 49e820bd-4f9b-42f6-a7fb-2f36e22f82e0 | 78a62fcc433ce479d1cda301983aa1760aeaa1f3ae6446ac5840dcb1fbebcdc4 | 25048                | 78a62fcc433ce479d1cda301983aa1760aeaa1f3ae6446ac5840dcb1fbebcdc4 | wv-zcta-snapshot-v1       | 78a62fcc433ce479d1cda301983aa1760aeaa1f3ae6446ac5840dcb1fbebcdc4 | verified           | 2026-07-11 19:20:22.231766+00 | 2026-07-11 19:20:22.231766+00 |               |                    |                    |                    |                    |                    |                    |            |              |                                          |                  
 01bca1de-7185-446c-84d4-6e2b8cd42ca2 | 59ad7b32-2d88-4578-9e57-7c883f44a720 | 796d2952971d13424d7f3e63497e0454250a6ce912911cf02c5a46e5990b0504 | 540690020004         | 796d2952971d13424d7f3e63497e0454250a6ce912911cf02c5a46e5990b0504 | wv-blockgroup-snapshot-v2 | 796d2952971d13424d7f3e63497e0454250a6ce912911cf02c5a46e5990b0504 | verified           | 2026-07-15 16:15:13.739685+00 | 2026-07-15 16:15:13.739685+00 |               |  40.13539303513324 | -80.64197021291724 |         -80.667931 |          40.109493 |         -80.606194 | 40.161279999999984 | EPSG:26917 | EPSG:4326    | public.wv_blockgroups_census_2020_utm83  |      540690020004
 01d1cbee-1fe6-485c-af6e-269f9526b82b | a5a8716d-02aa-4cf7-8f28-81fcf7a8749d | 1348a303eb068070663454810ea9b4e1521fd55cb7ceeda00dd90d19e2b096aa | 54069002200          | 1348a303eb068070663454810ea9b4e1521fd55cb7ceeda00dd90d19e2b096aa | wv-tract-snapshot-v1      | 1348a303eb068070663454810ea9b4e1521fd55cb7ceeda00dd90d19e2b096aa | verified           | 2026-07-11 19:03:08.245313+00 | 2026-07-11 19:03:08.245313+00 |               |                    |                    |                    |                    |                    |                    |            |              |                                          |                  
 01d6f2cc-d517-435b-92f3-649646a77d3f | 49e820bd-4f9b-42f6-a7fb-2f36e22f82e0 | 41f64ec67b74025e5b794b0c2f9f85d30a00ddc89dd3424465aaea332c5246a6 | 24938                | 41f64ec67b74025e5b794b0c2f9f85d30a00ddc89dd3424465aaea332c5246a6 | wv-zcta-snapshot-v1       | 41f64ec67b74025e5b794b0c2f9f85d30a00ddc89dd3424465aaea332c5246a6 | verified           | 2026-07-11 19:20:22.231766+00 | 2026-07-11 19:20:22.231766+00 |               |                    |                    |                    |                    |                    |                    |            |              |                                          |                  
 022ba454-1dd2-4760-95a0-127cc863c86a | 59ad7b32-2d88-4578-9e57-7c883f44a720 | dd35d419a024b010c79dfdbeac09e218b0ef113f2cd717fb445130a9e9670697 | 540539548023         | dd35d419a024b010c79dfdbeac09e218b0ef113f2cd717fb445130a9e9670697 | wv-blockgroup-snapshot-v2 | dd35d419a024b010c79dfdbeac09e218b0ef113f2cd717fb445130a9e9670697 | verified           | 2026-07-15 16:15:13.739685+00 | 2026-07-15 16:15:13.739685+00 |               | 38.885788667996465 | -81.97236605582903 | -82.04852300000002 |          38.838956 |          -81.89847 | 38.933626999999994 | EPSG:26917 | EPSG:4326    | public.wv_blockgroups_census_2020_utm83  |      540539548023
 024689d1-abb9-4488-b9e5-18a8fa8afa4d | a5a8716d-02aa-4cf7-8f28-81fcf7a8749d | d8ba3dd9f58052ed4bd077e8a32b1a9081849a8b486812528dab95c4927ce5ec | 54027968401          | d8ba3dd9f58052ed4bd077e8a32b1a9081849a8b486812528dab95c4927ce5ec | wv-tract-snapshot-v1      | d8ba3dd9f58052ed4bd077e8a32b1a9081849a8b486812528dab95c4927ce5ec | verified           | 2026-07-11 19:03:08.245313+00 | 2026-07-11 19:03:08.245313+00 |               |                    |                    |                    |                    |                    |                    |            |              |                                          |                  
 0256757a-e62f-4ce6-b179-5773ed070e64 | 59ad7b32-2d88-4578-9e57-7c883f44a720 | a21bb7b1b8a1647d0847d189aa35f30c16e50cd8d0c48ed2f2a0dd5b4ba0719e | 540290212004         | a21bb7b1b8a1647d0847d189aa35f30c16e50cd8d0c48ed2f2a0dd5b4ba0719e | wv-blockgroup-snapshot-v2 | a21bb7b1b8a1647d0847d189aa35f30c16e50cd8d0c48ed2f2a0dd5b4ba0719e | verified           | 2026-07-15 16:15:13.739685+00 | 2026-07-15 16:15:13.739685+00 |               |   40.4787315368716 | -80.56923816149917 |         -80.598536 |          40.449593 |         -80.546358 |          40.507818 | EPSG:26917 | EPSG:4326    | public.wv_blockgroups_census_2020_utm83  |      540290212004
 025e108c-ab02-40c2-96a0-ef6d1a8aaaab | 4c6638de-274d-485c-bb64-ab078426a5a5 | 2cb6abf2d85c274280beabfcdafde5893704aeaa84c63308a23ab4b815caa16a | 541070009011         | 2cb6abf2d85c274280beabfcdafde5893704aeaa84c63308a23ab4b815caa16a | wv-blockgroup-snapshot-v1 | 2cb6abf2d85c274280beabfcdafde5893704aeaa84c63308a23ab4b815caa16a | verified           | 2026-07-11 19:12:07.933882+00 | 2026-07-15 04:22:55.269141+00 |               |  39.24879649999998 | -81.55301707885957 |           -81.5705 | 39.236721999999986 |         -81.541476 |  39.26087400000001 | EPSG:26917 | EPSG:4326    | public.wv_blockgroups_census_2020_utm83  |               719
 025f5b08-51f4-4a7d-828d-8af03a1f0248 | a5a8716d-02aa-4cf7-8f28-81fcf7a8749d | a492754de57d822240f9596a3ee361c278fca80b84029e7cfd80ed5fa4511f5a | 54055002000          | a492754de57d822240f9596a3ee361c278fca80b84029e7cfd80ed5fa4511f5a | wv-tract-snapshot-v1      | a492754de57d822240f9596a3ee361c278fca80b84029e7cfd80ed5fa4511f5a | verified           | 2026-07-11 19:03:08.245313+00 | 2026-07-11 19:03:08.245313+00 |               |                    |                    |                    |                    |                    |                    |            |              |                                          |                  
 02618d03-951a-47e1-8fb1-4be228a572b5 | fcac67c8-1ece-4f13-a18b-9e21809e8188 | 719ebb975f6786ac14e2bfb8b2453e129d4cb99a912753d4374ed4944a8c4801 | 1400000US54033031600 | 719ebb975f6786ac14e2bfb8b2453e129d4cb99a912753d4374ed4944a8c4801 | wv-tract-snapshot-v2      | 719ebb975f6786ac14e2bfb8b2453e129d4cb99a912753d4374ed4944a8c4801 | verified           | 2026-07-15 04:22:55.269141+00 | 2026-07-15 04:22:55.269141+00 |               |  39.27266899999999 | -80.55500810485535 |         -80.604301 |          39.246087 |         -80.523768 | 39.299142999999994 | EPSG:26917 | EPSG:4326    | public.wv_censustracts_census_2020_utm83 |               316
 0273ee1a-067a-47d6-8e6b-b48c3d710f7a | 59ad7b32-2d88-4578-9e57-7c883f44a720 | 035c0f3db541389f7580714ac8257fc5f67ad9bb14ec19e11060a46161825cf0 | 540690015001         | 035c0f3db541389f7580714ac8257fc5f67ad9bb14ec19e11060a46161825cf0 | wv-blockgroup-snapshot-v2 | 035c0f3db541389f7580714ac8257fc5f67ad9bb14ec19e11060a46161825cf0 | verified           | 2026-07-15 16:15:13.739685+00 | 2026-07-15 16:15:13.739685+00 |               |  40.08966957606278 | -80.68381374377933 |         -80.699109 |  40.07763599999999 |         -80.667035 |  40.10177199999998 | EPSG:26917 | EPSG:4326    | public.wv_blockgroups_census_2020_utm83  |      540690015001
 0274f454-1ad5-49cf-98c4-3d50641aa31e | fcac67c8-1ece-4f13-a18b-9e21809e8188 | bac5aa595f009d4bf44700b9857f4585622493ff10542939ccb8040818741f0b | 1400000US54049021001 | bac5aa595f009d4bf44700b9857f4585622493ff10542939ccb8040818741f0b | wv-tract-snapshot-v2      | bac5aa595f009d4bf44700b9857f4585622493ff10542939ccb8040818741f0b | verified           | 2026-07-15 04:22:55.269141+00 | 2026-07-15 04:22:55.269141+00 |               |          39.472235 | -80.03217429659612 |         -80.109792 | 39.393688999999995 | -79.93887799999999 | 39.550768999999995 | EPSG:26917 | EPSG:4326    | public.wv_censustracts_census_2020_utm83 |               370
 028b4d06-0bc2-402e-9ff5-2c17b064d5a9 | 4c6638de-274d-485c-bb64-ab078426a5a5 | 43673c73a624c8f1d743d3375e373391edf0139f14e3270911e0cf046ec94a0f | 540110010002         | 43673c73a624c8f1d743d3375e373391edf0139f14e3270911e0cf046ec94a0f | wv-blockgroup-snapshot-v1 | 43673c73a624c8f1d743d3375e373391edf0139f14e3270911e0cf046ec94a0f | verified           | 2026-07-11 19:12:07.933882+00 | 2026-07-15 04:22:55.269141+00 |               |  38.40838049999999 | -82.48746185647134 | -82.49501800000009 |  38.40522799999999 | -82.48018300000008 |  38.41147599999998 | EPSG:26917 | EPSG:4326    | public.wv_blockgroups_census_2020_utm83  |               696
(50 rows)

 logical_collection_name |        collection_version_id         | physical_collection_name |         activated_at          
-------------------------+--------------------------------------+--------------------------+-------------------------------
 gbim_wv_blockgroups     | 4c6638de-274d-485c-bb64-ab078426a5a5 | gbim_wv_blockgroups_v1   | 2026-07-11 19:12:33.436517+00
 gbim_wv_counties        | f43b510a-12d5-4855-a203-65a2690ae6b0 | gbim_wv_counties_v1      | 2026-07-11 18:46:18.528621+00
 gbim_wv_tracts          | a5a8716d-02aa-4cf7-8f28-81fcf7a8749d | gbim_wv_tracts_v1        | 2026-07-11 19:04:35.699597+00
 gbim_wv_zctas           | 49e820bd-4f9b-42f6-a7fb-2f36e22f82e0 | gbim_wv_zctas_v1         | 2026-07-11 19:20:43.861534+00
(4 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/msjarvis-rebuild$ psql -h localhost -p 5432 -U postgres -d msjarvisgis <<'SQL'
\pset pager off

SELECT
  m.logical_collection_name,
  m.physical_collection_name,
  m.collection_version_id,
  m.permitted_use,
  p.id               AS promotion_event_id,
  p.issued_at,
  p.issued_by,
  p.algorithm,
  p.signature_valid,
  p.coherence_ok,
  p.payload_sha256,
  octet_length(p.public_key) AS public_key_bytes,
  octet_length(p.signature)  AS signature_bytes
FROM gbim_chroma_publication_manifest m
LEFT JOIN promotion_events p
  ON p.manifest_row_id = m.collection_version_id
ORDER BY m.logical_collection_name, p.issued_at DESC NULLS LAST;
SQL
Pager usage is off.
 logical_collection_name | physical_collection_name |        collection_version_id         | permitted_use |          promotion_event_id          |           issued_at           |     issued_by     |     algorithm     | signature_valid | coherence_ok |                          payload_sha256                          | public_key_bytes | signature_bytes 
-------------------------+--------------------------+--------------------------------------+---------------+--------------------------------------+-------------------------------+-------------------+-------------------+-----------------+--------------+------------------------------------------------------------------+------------------+-----------------
 gbim_wv_blockgroups     | gbimwvblockgroupsv1      | 4c6638de-274d-485c-bb64-ab078426a5a5 | analysis      | 57b59ac9-e5c9-4eeb-96c6-3583793f7510 | 2026-07-16 18:27:43.390487+00 | msjarvis-operator | RSASSA-PSS-SHA256 | t               | t            | 5ef51d8f4648b6554fa09220417f92cd778f419e0df7ca95c7e0f093f71fbea7 |             2118 |             512
 gbim_wv_counties        | gbimwvcountiesv2         | f43b510a-12d5-4855-a203-65a2690ae6b0 | analysis      | 2bf1c300-2563-4ff6-95e8-c38c8071ca7d | 2026-07-16 18:12:12.126862+00 | msjarvis-operator | RSASSA-PSS-SHA256 | t               | t            | 4471fb17c30749a9392be1a9a553008beb600754971156bd4dac937d1f74aeaf |             2118 |             512
 gbim_wv_counties        | gbimwvcountiesv2         | f43b510a-12d5-4855-a203-65a2690ae6b0 | analysis      | 2a448844-fbe1-40cb-bb0d-2970059e3d99 | 2026-07-16 18:08:08.748975+00 | msjarvis-operator | TEST-NONCRYPTO    | f               | f            |                                                                  |                1 |               1
 gbim_wv_tracts          | gbimwvtractsv2           | fcac67c8-1ece-4f13-a18b-9e21809e8188 | analysis      |                                      |                               |                   |                   |                 |              |                                                                  |                  |                
(4 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/msjarvis-rebuild$ rg -n \
  "gbim_chroma_publication_manifest|promotion_events|manifest_row_id|signature_valid|coherence_ok|payload_sha256|enforce_gbim_manifest_promotion|manifest permitted_use missing for collection" \
  /mnt/spiritual_drive/msjarvis-rebuild /opt/msjarvis-rebuild/msjarvis-rebuild \
  --glob '!**/site-packages/**' \
  --glob '!**/.venv/**' \
  --glob '!**/venv/**' \
  --glob '!**/node_modules/**'
/mnt/spiritual_drive/msjarvis-rebuild/chapter46_exact_patch_context.json
2134:      "content": "import os\nfrom functools import lru_cache\nimport psycopg\n\nPG_DSN = os.getenv(\"GBIM_PG_DSN\", \"postgresql://postgres@localhost:5436/msjarvisgis_v2\")\n\nLOGICAL_TO_DEFAULT = {\n    \"hp-public-appearances-v1\": \"public_civic_appearances\",\n    \"hp-public-documents-v1\": \"public_civic_documents\",\n    \"hp-public-statements-v1\": \"public_civic_statements\",\n    \"public-civic-roles-v1\": \"public_civic_roles\",\n    \"public-civic-events-v1\": \"public_civic_events\",\n    \"public-civic-sources-v1\": \"public_civic_sources\",\n    \"civic-role-temporal-v1\": \"civic_role_temporal\",\n    \"hilbert-time-v1\": \"hilbert_time\",\n}\n\n@lru_cache(maxsize=64)\ndef resolve_collection(logical_name: str) -> str:\n    default_name = LOGICAL_TO_DEFAULT.get(logical_name, logical_name)\n    try:\n        with psycopg.connect(PG_DSN) as conn:\n            with conn.cursor() as cur:\n                cur.execute(\n                    \"\"\"\n                    SELECT physical_collection_name\n                    FROM public.gbim_chroma_publication_manifest\n                    WHERE logical_collection_name = %s\n                    \"\"\",\n                    (logical_name,),\n                )\n                row = cur.fetchone()\n                if row and row[0]:\n                    return row[0]\n    except Exception:\n        pass\n    return default_name\n\ndef hp_public_appearances():\n    return resolve_collection(\"hp-public-appearances-v1\")\n\ndef hp_public_documents():\n    return resolve_collection(\"hp-public-documents-v1\")\n\ndef hp_public_statements():\n    return resolve_collection(\"hp-public-statements-v1\")\n\ndef public_civic_roles():\n    return resolve_collection(\"public-civic-roles-v1\")\n\ndef public_civic_events():\n    return resolve_collection(\"public-civic-events-v1\")\n\ndef public_civic_sources():\n    return resolve_collection(\"public-civic-sources-v1\")\n\ndef civic_role_temporal():\n    return resolve_collection(\"civic-role-temporal-v1\")\n\ndef hilbert_time():\n    return resolve_collection(\"hilbert-time-v1\")\n"

/mnt/spiritual_drive/msjarvis-rebuild/check_hilbert_people_v3.sh
41:banner "2. Resolver sanity check against gbim_chroma_publication_manifest"
45:FROM public.gbim_chroma_publication_manifest

/mnt/spiritual_drive/msjarvis-rebuild/chapter42_evidence_2026-07-16.txt
4:- Manifest trigger trg_enforce_gbim_manifest_promotion present on public.gbim_chroma_publication_manifest.
5:- Trigger function requires pe.manifest_row_id = NEW.collection_version_id and pe.signature_valid IS TRUE.
10:- Promotion event marked signature_valid = TRUE.

/mnt/spiritual_drive/msjarvis-rebuild/check_hilbert_people_v4.sh
42:banner "2. Resolver sanity check against gbim_chroma_publication_manifest"
46:FROM public.gbim_chroma_publication_manifest

/mnt/spiritual_drive/msjarvis-rebuild/check_hilbert_people_v2.sh
50:banner "2. Resolver sanity check against gbim_chroma_publication_manifest"
54:FROM public.gbim_chroma_publication_manifest

/opt/msjarvis-rebuild/msjarvis-rebuild/chapter46_exact_patch_context.json
2134:      "content": "import os\nfrom functools import lru_cache\nimport psycopg\n\nPG_DSN = os.getenv(\"GBIM_PG_DSN\", \"postgresql://postgres@localhost:5436/msjarvisgis_v2\")\n\nLOGICAL_TO_DEFAULT = {\n    \"hp-public-appearances-v1\": \"public_civic_appearances\",\n    \"hp-public-documents-v1\": \"public_civic_documents\",\n    \"hp-public-statements-v1\": \"public_civic_statements\",\n    \"public-civic-roles-v1\": \"public_civic_roles\",\n    \"public-civic-events-v1\": \"public_civic_events\",\n    \"public-civic-sources-v1\": \"public_civic_sources\",\n    \"civic-role-temporal-v1\": \"civic_role_temporal\",\n    \"hilbert-time-v1\": \"hilbert_time\",\n}\n\n@lru_cache(maxsize=64)\ndef resolve_collection(logical_name: str) -> str:\n    default_name = LOGICAL_TO_DEFAULT.get(logical_name, logical_name)\n    try:\n        with psycopg.connect(PG_DSN) as conn:\n            with conn.cursor() as cur:\n                cur.execute(\n                    \"\"\"\n                    SELECT physical_collection_name\n                    FROM public.gbim_chroma_publication_manifest\n                    WHERE logical_collection_name = %s\n                    \"\"\",\n                    (logical_name,),\n                )\n                row = cur.fetchone()\n                if row and row[0]:\n                    return row[0]\n    except Exception:\n        pass\n    return default_name\n\ndef hp_public_appearances():\n    return resolve_collection(\"hp-public-appearances-v1\")\n\ndef hp_public_documents():\n    return resolve_collection(\"hp-public-documents-v1\")\n\ndef hp_public_statements():\n    return resolve_collection(\"hp-public-statements-v1\")\n\ndef public_civic_roles():\n    return resolve_collection(\"public-civic-roles-v1\")\n\ndef public_civic_events():\n    return resolve_collection(\"public-civic-events-v1\")\n\ndef public_civic_sources():\n    return resolve_collection(\"public-civic-sources-v1\")\n\ndef civic_role_temporal():\n    return resolve_collection(\"civic-role-temporal-v1\")\n\ndef hilbert_time():\n    return resolve_collection(\"hilbert-time-v1\")\n"

/mnt/spiritual_drive/msjarvis-rebuild/services/gis_rag_service.py
301:                FROM public.gbim_chroma_publication_manifest AS pub
341:                detail=f"manifest permitted_use missing for collection '{collection_name}'",

/mnt/spiritual_drive/msjarvis-rebuild/services/hilbert/phi_promotion_gate.py
55:def mark_event(event_id: str, coherence_ok: bool):
62:                UPDATE public.promotion_events
63:                SET coherence_ok = %s
66:                (coherence_ok, event_id),
84:        "coherence_ok": ok,

/mnt/spiritual_drive/msjarvis-rebuild/services/hilbert/sign_promotion_event.py
21:    "manifest_row_id": collection_version_id,

/mnt/spiritual_drive/msjarvis-rebuild/services/hilbert/collection_manifest.py
27:                    FROM public.gbim_chroma_publication_manifest

/opt/msjarvis-rebuild/msjarvis-rebuild/check_hilbert_people_v3.sh
41:banner "2. Resolver sanity check against gbim_chroma_publication_manifest"
45:FROM public.gbim_chroma_publication_manifest

/opt/msjarvis-rebuild/msjarvis-rebuild/chapter42_evidence_2026-07-16.txt
4:- Manifest trigger trg_enforce_gbim_manifest_promotion present on public.gbim_chroma_publication_manifest.
5:- Trigger function requires pe.manifest_row_id = NEW.collection_version_id and pe.signature_valid IS TRUE.
10:- Promotion event marked signature_valid = TRUE.

/opt/msjarvis-rebuild/msjarvis-rebuild/services/hilbert/phi_promotion_gate.py
55:def mark_event(event_id: str, coherence_ok: bool):
62:                UPDATE public.promotion_events
63:                SET coherence_ok = %s
66:                (coherence_ok, event_id),
84:        "coherence_ok": ok,

/opt/msjarvis-rebuild/msjarvis-rebuild/services/hilbert/sign_promotion_event.py
21:    "manifest_row_id": collection_version_id,

/opt/msjarvis-rebuild/msjarvis-rebuild/services/hilbert/collection_manifest.py
27:                    FROM public.gbim_chroma_publication_manifest

/opt/msjarvis-rebuild/msjarvis-rebuild/check_hilbert_people_v4.sh
42:banner "2. Resolver sanity check against gbim_chroma_publication_manifest"
46:FROM public.gbim_chroma_publication_manifest

/opt/msjarvis-rebuild/msjarvis-rebuild/services/gis_rag_service.py
301:                FROM public.gbim_chroma_publication_manifest AS pub
341:                detail=f"manifest permitted_use missing for collection '{collection_name}'",

/opt/msjarvis-rebuild/msjarvis-rebuild/check_hilbert_people_v2.sh
50:banner "2. Resolver sanity check against gbim_chroma_publication_manifest"
54:FROM public.gbim_chroma_publication_manifest
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/msjarvis-rebuild$ sed -n '1,260p' /opt/msjarvis-rebuild/msjarvis-rebuild/services/gis_rag*.py 2>/dev/null
sed -n '1,260p' /mnt/spiritual_drive/msjarvis-rebuild/services/gis_rag*.py 2>/dev/null

sed -n '1,260p' /opt/msjarvis-rebuild/msjarvis-rebuild/services/*publication*.py 2>/dev/null
sed -n '1,260p' /mnt/spiritual_drive/msjarvis-rebuild/services/*publication*.py 2>/dev/null

sed -n '1,260p' /opt/msjarvis-rebuild/msjarvis-rebuild/services/*manifest*.py 2>/dev/null
sed -n '1,260p' /mnt/spiritual_drive/msjarvis-rebuild/services/*manifest*.py 2>/dev/null
import logging
import os
import re
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

import httpx
import chromadb
from chromadb.config import Settings
from fastapi import Body, FastAPI, Header, HTTPException
from pydantic import BaseModel, Field
import psycopg2

CHROMA_HOST = os.getenv("CHROMA_HOST", "jarvis-chroma")
CHROMA_PORT = int(os.getenv("CHROMA_PORT", "8000"))

POSTGRES_DSN = os.getenv("POSTGRES_DSN", "postgresql://msjarvis@jarvis-msjarvis-db:5432/msjarvisgis")
ANONYMIZED_TELEMETRY = os.getenv("ANONYMIZED_TELEMETRY", "FALSE").strip().lower() in {"1", "true", "yes", "on"}
COLLECTIONS = [x.strip() for x in os.getenv("GIS_RAG_COLLECTIONS", "gbim_wv_counties_v2,gbim_wv_tracts_v2").split(",") if x.strip()]
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://jarvis-ollama:11434").rstrip("/")
EMBED_MODEL = os.getenv("GIS_EMBED_MODEL", "all-minilm:latest")
EMBED_DIMENSION = int(os.getenv("GIS_EMBED_DIMENSION", "384"))

app = FastAPI(title="Ms. Jarvis Governed GIS RAG", version="0.4.3")
logger = logging.getLogger("gis_rag_service")
if not logger.handlers:
    import sys
    _handler = logging.StreamHandler(sys.stdout)
    _handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s"))
    logger.addHandler(_handler)
logger.setLevel(logging.INFO)
logger.propagate = False

async def probe_phi_for_gisrag(
    request: "GISRAGRequest",
    projection: "ProjectionContext",
) -> Dict[str, Any]:
    phi_url = os.getenv("PHI_PROBE_URL", "http://jarvis-phi-probe:8025/phi")
    timeout = float(os.getenv("PHI_PROBE_TIMEOUT_SECONDS", "20"))
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.get(phi_url)
        response.raise_for_status()
        payload = response.json()
        if isinstance(payload, dict):
            payload["observed_at"] = datetime.now(timezone.utc).isoformat()
            payload["observed_via"] = "gis_rag"
            payload["query"] = request.query
            payload["n_results"] = request.n_results
            payload["projection_role"] = projection.role
            payload["projection_purpose"] = projection.purpose
            payload["projection_legal_basis"] = projection.legal_basis
            if projection.time:
                payload["projection_time"] = projection.time
        logger.info("phi_soft_gate=%s", payload)
        return payload if isinstance(payload, dict) else {"note": "non-dict phi payload"}
    except Exception as e:
        logger.warning("phi_soft_gate_error=%s", e)
        return {
            "note": "phi probe unavailable",
            "error": str(e),
            "observed_at": datetime.now(timezone.utc).isoformat(),
            "observed_via": "gis_rag",
            "query": request.query,
            "n_results": request.n_results,
            "projection_role": projection.role,
            "projection_purpose": projection.purpose,
            "projection_legal_basis": projection.legal_basis,
            "projection_time": projection.time,
        }


class ProjectionContext(BaseModel):
    role: str
    purpose: str
    legal_basis: str
    time: Optional[str] = None

def require_projection(
    x_msallis_role: Optional[str],
    x_msallis_purpose: Optional[str],
    x_msallis_legal_basis: Optional[str],
    x_msallis_time: Optional[str],
) -> ProjectionContext:
    if not x_msallis_role or not x_msallis_role.strip():
        raise HTTPException(status_code=422, detail="Missing required projection header: x-msallis-role")
    if not x_msallis_purpose or not x_msallis_purpose.strip():
        raise HTTPException(status_code=422, detail="Missing required projection header: x-msallis-purpose")
    if not x_msallis_legal_basis or not x_msallis_legal_basis.strip():
        raise HTTPException(status_code=422, detail="Missing required projection header: x-msallis-legal-basis")
    return ProjectionContext(
        role=x_msallis_role.strip(),
        purpose=x_msallis_purpose.strip(),
        legal_basis=x_msallis_legal_basis.strip(),
        time=(x_msallis_time.strip() if x_msallis_time and x_msallis_time.strip() else None),
    )

class GISRAGRequest(BaseModel):
    query: str = Field(min_length=1)
    n_results: int = Field(default=10, ge=1, le=100)
    county: Optional[str] = None
    bbox: Optional[List[float]] = None
    entity_type: Optional[str] = None
    tract_geoid: Optional[str] = None
    blockgroup_geoid: Optional[str] = None
    request_purpose: Optional[str] = None

class GISRAGHit(BaseModel):
    text: str
    collection_name: str
    document_id: Optional[str] = None
    distance: Optional[float] = None
    layer_name: Optional[str] = None
    name: Optional[str] = None
    lat: Optional[float] = None
    lon: Optional[float] = None
    metadata: Dict[str, Any]

class GISRAGResponse(BaseModel):
    hits: List[GISRAGHit]

def chroma_client():
    return chromadb.HttpClient(host=CHROMA_HOST, port=CHROMA_PORT,
        settings=Settings(anonymized_telemetry=ANONYMIZED_TELEMETRY)
    )

async def embed_query(client: httpx.AsyncClient, text: str) -> List[float]:
    response = await client.post(
        f"{OLLAMA_HOST}/api/embeddings",
        json={"model": EMBED_MODEL, "prompt": text},
        timeout=120.0,
    )
    if response.status_code != 200:
        raise HTTPException(status_code=502, detail=f"Ollama embedding error: {response.text[:300]}")
    payload = response.json()
    embedding = payload.get("embedding")
    if not isinstance(embedding, list) or not embedding:
        raise HTTPException(status_code=502, detail="Ollama returned no valid embedding.")
    if len(embedding) != EMBED_DIMENSION:
        raise HTTPException(
            status_code=502,
            detail=f"Unexpected embedding dimension: expected {EMBED_DIMENSION}, received {len(embedding)}",
        )
    return embedding

def metadata_where(request: GISRAGRequest) -> Optional[Dict[str, Any]]:
    predicates: List[Dict[str, Any]] = []

    if request.county:
        county = request.county.strip()
        predicates.append({"canonical_county_id": county})

    if request.entity_type:
        et = request.entity_type.strip().lower()
        if et == "county":
            predicates.append({"entity_type": "county"})
        elif et in ("tract", "census_tract", "censustract"):
            predicates.append({"entity_type": "census_tract"})

    if request.tract_geoid:
        predicates.append({"tract_geoid": request.tract_geoid.strip()})

    if not predicates:
        return None
    if len(predicates) == 1:
        return predicates[0]
    return {"$and": predicates}

BLOCKGROUP_COLLECTION_FALLBACK = "gbimwvblockgroupsv2"
WV_BLOCKGROUP_GEOID_RE = re.compile(r"\b(54\d{10})\b")

def extract_blockgroup_geoid(request: GISRAGRequest) -> Optional[str]:
    if request.blockgroup_geoid:
        supplied = request.blockgroup_geoid.strip()
        if WV_BLOCKGROUP_GEOID_RE.fullmatch(supplied):
            return supplied
    match = WV_BLOCKGROUP_GEOID_RE.search(request.query)
    if match:
        return match.group(1)
    return None

def query_blockgroup_exact(
    embedding: List[float],
    request: GISRAGRequest,
) -> List[GISRAGHit]:
    geoid = extract_blockgroup_geoid(request)
    if not geoid:
        return []

    try:
        client = chroma_client()
        bg_collection_name = None
        for name in COLLECTIONS:
            if "blockgroup" in name.lower():
                bg_collection_name = name
                break
        if bg_collection_name is None:
            bg_collection_name = BLOCKGROUP_COLLECTION_FALLBACK
        collection = client.get_collection(bg_collection_name)
    except Exception as e:
        raise HTTPException(
            status_code=502,
            detail=f"Unable to resolve block-group collection: {e}",
        )

    try:
        data = collection.get(
            where={"canonical_blockgroup_id": geoid},
            limit=request.n_results,
            include=["documents", "metadatas"],
        )
        logger.info("gis_rag_exact_blockgroup_lookup collection=%s canonical_blockgroup_id=%s hit_count=%d", bg_collection_name, geoid, len(data.get("ids") or []))
    except Exception as e:
        raise HTTPException(
            status_code=502,
            detail=f"Chroma block-group exact get failed: {e}",
        )

    ids = data.get("ids") or []
    docs = data.get("documents") or []
    metas = data.get("metadatas") or []
    dists = [0.0] * len(docs)

    hits: List[GISRAGHit] = []
    for i in range(len(docs)):
        md = metas[i] if i < len(metas) and isinstance(metas[i], dict) else {}
        md = dict(md)
        md["retrieval_mode"] = "exact_metadata"
        md.setdefault("canonical_blockgroup_id", geoid)
        hits.append(
            GISRAGHit(
                text=docs[i],
                collection_name=bg_collection_name,
                document_id=ids[i] if i < len(ids) else None,
                distance=dists[i] if i < len(dists) else None,
                layer_name=md.get("sourcetable") or md.get("source_table"),
                name=md.get("county_name") or md.get("tract_geoid") or geoid,
                lat=md.get("centroidlat") or md.get("centroid_lat"),
                lon=md.get("centroidlon") or md.get("centroid_lon"),
                metadata=md,
            )
        )
    return hits

def query_collection(
    collection_name: str,
    embedding: List[float],
    request: GISRAGRequest,
) -> List[GISRAGHit]:
    try:
        client = chroma_client()
        collection = client.get_collection(collection_name)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Unable to resolve Chroma collection {collection_name!r}: {e}")

    kwargs: Dict[str, Any] = {
        "query_embeddings": [embedding],
        "n_results": request.n_results,
        "include": ["documents", "metadatas", "distances"],
    }
import logging
import os
import re
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

import httpx
import chromadb
from chromadb.config import Settings
from fastapi import Body, FastAPI, Header, HTTPException
from pydantic import BaseModel, Field
import psycopg2

CHROMA_HOST = os.getenv("CHROMA_HOST", "jarvis-chroma")
CHROMA_PORT = int(os.getenv("CHROMA_PORT", "8000"))

POSTGRES_DSN = os.getenv("POSTGRES_DSN", "postgresql://msjarvis@jarvis-msjarvis-db:5432/msjarvisgis")
ANONYMIZED_TELEMETRY = os.getenv("ANONYMIZED_TELEMETRY", "FALSE").strip().lower() in {"1", "true", "yes", "on"}
COLLECTIONS = [x.strip() for x in os.getenv("GIS_RAG_COLLECTIONS", "gbim_wv_counties_v2,gbim_wv_tracts_v2").split(",") if x.strip()]
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://jarvis-ollama:11434").rstrip("/")
EMBED_MODEL = os.getenv("GIS_EMBED_MODEL", "all-minilm:latest")
EMBED_DIMENSION = int(os.getenv("GIS_EMBED_DIMENSION", "384"))

app = FastAPI(title="Ms. Jarvis Governed GIS RAG", version="0.4.3")
logger = logging.getLogger("gis_rag_service")
if not logger.handlers:
    import sys
    _handler = logging.StreamHandler(sys.stdout)
    _handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s"))
    logger.addHandler(_handler)
logger.setLevel(logging.INFO)
logger.propagate = False

async def probe_phi_for_gisrag(
    request: "GISRAGRequest",
    projection: "ProjectionContext",
) -> Dict[str, Any]:
    phi_url = os.getenv("PHI_PROBE_URL", "http://jarvis-phi-probe:8025/phi")
    timeout = float(os.getenv("PHI_PROBE_TIMEOUT_SECONDS", "20"))
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.get(phi_url)
        response.raise_for_status()
        payload = response.json()
        if isinstance(payload, dict):
            payload["observed_at"] = datetime.now(timezone.utc).isoformat()
            payload["observed_via"] = "gis_rag"
            payload["query"] = request.query
            payload["n_results"] = request.n_results
            payload["projection_role"] = projection.role
            payload["projection_purpose"] = projection.purpose
            payload["projection_legal_basis"] = projection.legal_basis
            if projection.time:
                payload["projection_time"] = projection.time
        logger.info("phi_soft_gate=%s", payload)
        return payload if isinstance(payload, dict) else {"note": "non-dict phi payload"}
    except Exception as e:
        logger.warning("phi_soft_gate_error=%s", e)
        return {
            "note": "phi probe unavailable",
            "error": str(e),
            "observed_at": datetime.now(timezone.utc).isoformat(),
            "observed_via": "gis_rag",
            "query": request.query,
            "n_results": request.n_results,
            "projection_role": projection.role,
            "projection_purpose": projection.purpose,
            "projection_legal_basis": projection.legal_basis,
            "projection_time": projection.time,
        }


class ProjectionContext(BaseModel):
    role: str
    purpose: str
    legal_basis: str
    time: Optional[str] = None

def require_projection(
    x_msallis_role: Optional[str],
    x_msallis_purpose: Optional[str],
    x_msallis_legal_basis: Optional[str],
    x_msallis_time: Optional[str],
) -> ProjectionContext:
    if not x_msallis_role or not x_msallis_role.strip():
        raise HTTPException(status_code=422, detail="Missing required projection header: x-msallis-role")
    if not x_msallis_purpose or not x_msallis_purpose.strip():
        raise HTTPException(status_code=422, detail="Missing required projection header: x-msallis-purpose")
    if not x_msallis_legal_basis or not x_msallis_legal_basis.strip():
        raise HTTPException(status_code=422, detail="Missing required projection header: x-msallis-legal-basis")
    return ProjectionContext(
        role=x_msallis_role.strip(),
        purpose=x_msallis_purpose.strip(),
        legal_basis=x_msallis_legal_basis.strip(),
        time=(x_msallis_time.strip() if x_msallis_time and x_msallis_time.strip() else None),
    )

class GISRAGRequest(BaseModel):
    query: str = Field(min_length=1)
    n_results: int = Field(default=10, ge=1, le=100)
    county: Optional[str] = None
    bbox: Optional[List[float]] = None
    entity_type: Optional[str] = None
    tract_geoid: Optional[str] = None
    blockgroup_geoid: Optional[str] = None
    request_purpose: Optional[str] = None

class GISRAGHit(BaseModel):
    text: str
    collection_name: str
    document_id: Optional[str] = None
    distance: Optional[float] = None
    layer_name: Optional[str] = None
    name: Optional[str] = None
    lat: Optional[float] = None
    lon: Optional[float] = None
    metadata: Dict[str, Any]

class GISRAGResponse(BaseModel):
    hits: List[GISRAGHit]

def chroma_client():
    return chromadb.HttpClient(host=CHROMA_HOST, port=CHROMA_PORT,
        settings=Settings(anonymized_telemetry=ANONYMIZED_TELEMETRY)
    )

async def embed_query(client: httpx.AsyncClient, text: str) -> List[float]:
    response = await client.post(
        f"{OLLAMA_HOST}/api/embeddings",
        json={"model": EMBED_MODEL, "prompt": text},
        timeout=120.0,
    )
    if response.status_code != 200:
        raise HTTPException(status_code=502, detail=f"Ollama embedding error: {response.text[:300]}")
    payload = response.json()
    embedding = payload.get("embedding")
    if not isinstance(embedding, list) or not embedding:
        raise HTTPException(status_code=502, detail="Ollama returned no valid embedding.")
    if len(embedding) != EMBED_DIMENSION:
        raise HTTPException(
            status_code=502,
            detail=f"Unexpected embedding dimension: expected {EMBED_DIMENSION}, received {len(embedding)}",
        )
    return embedding

def metadata_where(request: GISRAGRequest) -> Optional[Dict[str, Any]]:
    predicates: List[Dict[str, Any]] = []

    if request.county:
        county = request.county.strip()
        predicates.append({"canonical_county_id": county})

    if request.entity_type:
        et = request.entity_type.strip().lower()
        if et == "county":
            predicates.append({"entity_type": "county"})
        elif et in ("tract", "census_tract", "censustract"):
            predicates.append({"entity_type": "census_tract"})

    if request.tract_geoid:
        predicates.append({"tract_geoid": request.tract_geoid.strip()})

    if not predicates:
        return None
    if len(predicates) == 1:
        return predicates[0]
    return {"$and": predicates}

BLOCKGROUP_COLLECTION_FALLBACK = "gbimwvblockgroupsv2"
WV_BLOCKGROUP_GEOID_RE = re.compile(r"\b(54\d{10})\b")

def extract_blockgroup_geoid(request: GISRAGRequest) -> Optional[str]:
    if request.blockgroup_geoid:
        supplied = request.blockgroup_geoid.strip()
        if WV_BLOCKGROUP_GEOID_RE.fullmatch(supplied):
            return supplied
    match = WV_BLOCKGROUP_GEOID_RE.search(request.query)
    if match:
        return match.group(1)
    return None

def query_blockgroup_exact(
    embedding: List[float],
    request: GISRAGRequest,
) -> List[GISRAGHit]:
    geoid = extract_blockgroup_geoid(request)
    if not geoid:
        return []

    try:
        client = chroma_client()
        bg_collection_name = None
        for name in COLLECTIONS:
            if "blockgroup" in name.lower():
                bg_collection_name = name
                break
        if bg_collection_name is None:
            bg_collection_name = BLOCKGROUP_COLLECTION_FALLBACK
        collection = client.get_collection(bg_collection_name)
    except Exception as e:
        raise HTTPException(
            status_code=502,
            detail=f"Unable to resolve block-group collection: {e}",
        )

    try:
        data = collection.get(
            where={"canonical_blockgroup_id": geoid},
            limit=request.n_results,
            include=["documents", "metadatas"],
        )
        logger.info("gis_rag_exact_blockgroup_lookup collection=%s canonical_blockgroup_id=%s hit_count=%d", bg_collection_name, geoid, len(data.get("ids") or []))
    except Exception as e:
        raise HTTPException(
            status_code=502,
            detail=f"Chroma block-group exact get failed: {e}",
        )

    ids = data.get("ids") or []
    docs = data.get("documents") or []
    metas = data.get("metadatas") or []
    dists = [0.0] * len(docs)

    hits: List[GISRAGHit] = []
    for i in range(len(docs)):
        md = metas[i] if i < len(metas) and isinstance(metas[i], dict) else {}
        md = dict(md)
        md["retrieval_mode"] = "exact_metadata"
        md.setdefault("canonical_blockgroup_id", geoid)
        hits.append(
            GISRAGHit(
                text=docs[i],
                collection_name=bg_collection_name,
                document_id=ids[i] if i < len(ids) else None,
                distance=dists[i] if i < len(dists) else None,
                layer_name=md.get("sourcetable") or md.get("source_table"),
                name=md.get("county_name") or md.get("tract_geoid") or geoid,
                lat=md.get("centroidlat") or md.get("centroid_lat"),
                lon=md.get("centroidlon") or md.get("centroid_lon"),
                metadata=md,
            )
        )
    return hits

def query_collection(
    collection_name: str,
    embedding: List[float],
    request: GISRAGRequest,
) -> List[GISRAGHit]:
    try:
        client = chroma_client()
        collection = client.get_collection(collection_name)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Unable to resolve Chroma collection {collection_name!r}: {e}")

    kwargs: Dict[str, Any] = {
        "query_embeddings": [embedding],
        "n_results": request.n_results,
        "include": ["documents", "metadatas", "distances"],
    }
import uuid
from pathlib import Path
from datetime import datetime

import pandas as pd

WORLDVIEW_3 = "002c2c84-2f18-40b7-8a98-b8d813dd6cc7"
MANIFEST_PATH = Path("services/msjarvis_gis_manifest.csv")
CSV_TARGET_PATH = Path("services/msjarvisattributesgis.csv")

def deterministic_feature_id(source_system: str, source_id: str) -> str:
    namespace = uuid.UUID("11111111-2222-3333-4444-555555555555")
    name = f"{source_system}:{source_id}"
    return str(uuid.uuid5(namespace, name))

def process_manifest_row(row):
    src_path      = Path(row["source_path"])
    layer_name    = row["layer_name"]
    theme         = row["theme"]
    source_system = row["source_system"]
    source_version= row["source_version"]
    id_field      = row["id_field"]
    name_field    = row["name_field"]
    lon_field     = row["lon_field"] or None
    lat_field     = row["lat_field"] or None
    wkt_field     = row["wkt_field"] or None

    df_src = pd.read_csv(src_path)
    now_iso = datetime.utcnow().replace(microsecond=0).isoformat() + "Z"

    records = []
    for _, r in df_src.iterrows():
        source_id = str(r[id_field]) if id_field in r and pd.notna(r[id_field]) else str(uuid.uuid4())
        feature_id = deterministic_feature_id(source_system, source_id)

        feature_label = str(r[name_field]) if name_field in r and pd.notna(r[name_field]) else layer_name

        lon = float(r[lon_field]) if lon_field and lon_field in r and pd.notna(r[lon_field]) else None
        lat = float(r[lat_field]) if lat_field and lat_field in r and pd.notna(r[lat_field]) else None

        geom_wkt = None
        if wkt_field and wkt_field in r and isinstance(r[wkt_field], str) and r[wkt_field].strip():
            geom_wkt = r[wkt_field].strip()

        records.append({
            "layer_name":      layer_name,
            "feature_id":      feature_id,
            "feature_label":   feature_label,
            "worldview_id":    WORLDVIEW_3,
            "geometry_type":   "GEOMETRY",
            "lon":             lon,
            "lat":             lat,
            "geom_wkt":        geom_wkt,
            "county":          None,
            "theme":           theme,
            "source_system":   source_system,
            "source_id":       source_id,
            "source_version":  source_version,
            "source_path":     str(src_path),
            "captured_at":     None,
            "imported_at":     now_iso,
            "import_batch_id": f"batch_{layer_name}_{now_iso}",
            "source_type":     "attributes_csv",
            "created_by":      "msjarvis-etl",
        })

    return pd.DataFrame.from_records(records)

def main():
    manifest = pd.read_csv(MANIFEST_PATH)
    dfs = []
    for _, row in manifest.iterrows():
        dfs.append(process_manifest_row(row))

    if not dfs:
        print("No manifest rows to process.")
        return

    df_new = pd.concat(dfs, ignore_index=True)

    if CSV_TARGET_PATH.exists():
        df_existing = pd.read_csv(CSV_TARGET_PATH)
        all_cols = list(df_existing.columns)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        df_combined.to_csv(CSV_TARGET_PATH, index=False, columns=all_cols)
    else:
        df_new.to_csv(CSV_TARGET_PATH, index=False)

    print(f"Appended {len(df_new)} records from manifest to {CSV_TARGET_PATH}")

if __name__ == "__main__":
    main()
import csv
import os
import chromadb
from chromadb.config import Settings

# HTTP Chroma configuration
CHROMA_HOST = os.getenv("CHROMA_HOST", "localhost")
CHROMA_PORT = int(os.getenv("CHROMA_PORT", "8002"))

client = chromadb.HttpClient(
    host=CHROMA_HOST,
    port=CHROMA_PORT,
    settings=Settings(anonymized_telemetry=False),
)

# Optional: restrict to specific collections via env var
env_collections = os.getenv("CHROMA_COLLECTIONS")

if env_collections:
    COLLECTIONS = [c.strip() for c in env_collections.split(",") if c.strip()]
else:
    # Discover all collections from this Chroma instance
    COLLECTIONS = [c.name for c in client.list_collections()]

with open("chroma_manifest.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "collection",
        "id",
        "file_id",
        "ueid",
        "layer_name",
        "lat",
        "lon",
        "bbox",
        "place_name",
        "county",
        "state",
        "country",
        "geodb_id",
        "sourcetable",
    ])

    for coll_name in COLLECTIONS:
        coll = client.get_collection(coll_name)
        offset = 0
        batch = 500

        while True:
            res = coll.get(
                include=["metadatas"],
                limit=batch,
                offset=offset,
            )
            ids = res.get("ids", [])
            if not ids:
                break

            metadatas = res.get("metadatas", []) or []
            for i, doc_id in enumerate(ids):
                md = metadatas[i] or {}
                writer.writerow([
                    coll_name,
                    doc_id,
                    md.get("file_id") or md.get("ueid") or "",
                    md.get("ueid") or "",
                    md.get("layer_name") or "",
                    md.get("lat") or "",
                    md.get("lon") or "",
                    md.get("bbox") or "",
                    md.get("place_name") or "",
                    md.get("county") or "",
                    md.get("state") or "",
                    md.get("country") or "",
                    md.get("geodb_id") or "",
                    md.get("sourcetable") or "",
                ])

            offset += batch
from services.hilbert.collection_manifest import hp_public_documents, hp_public_statements
from services.hilbert import civic_query
import chromadb

client = chromadb.HttpClient(host="jarvis-chroma", port=8000)

doc_entity = "smoke-manifest-doc-20260713"
stmt_entity = "smoke-manifest-stmt-20260713"

doc_content = "Smoke test document for manifest-resolved public civic documents collection (E2E harness)."
stmt_content = "Smoke test statement for manifest-resolved public civic statements collection (E2E harness)."

doc_col = client.get_collection(hp_public_documents())
stmt_col = client.get_collection(hp_public_statements())

# 1) Ingest
doc_id = "doc-" + doc_entity
stmt_id = "stmt-" + stmt_entity

doc_meta = {
    "registration_layer": 1,
    "public_opt_in": False,
    "source": "stack-smoke-test",
    "entity_id": doc_entity,
    "display_name": "Smoke Manifest Document",
    "doc_type": "smoke-test",
}
stmt_meta = {
    "registration_layer": 1,
    "public_opt_in": False,
    "source": "stack-smoke-test",
    "entity_id": stmt_entity,
    "display_name": "Smoke Manifest Statement",
    "statement_type": "smoke-test",
}

doc_col.upsert(ids=[doc_id], documents=[doc_content], metadatas=[doc_meta])
stmt_col.upsert(ids=[stmt_id], documents=[stmt_content], metadatas=[stmt_meta])

# 2) Query via civic_query (manifest-backed names)
doc_get = doc_col.get(
    where={"entity_id": {"$eq": doc_entity}},
    include=["documents", "metadatas"],
)
stmt_get = stmt_col.get(
    where={"entity_id": {"$eq": stmt_entity}},
    include=["documents", "metadatas"],
)

doc_query = civic_query.query_documents(
    text="Smoke test document manifest resolved public civic documents collection",
    n_results=5,
    source="stack-smoke-test",
    doc_type="smoke-test",
)
stmt_query = civic_query.query_statements(
    text="Smoke test statement manifest resolved public civic statements collection",
    n_results=5,
    source="stack-smoke-test",
    statement_type="smoke-test",
)

ok = True
ok = ok and len(doc_get.get("ids", [])) > 0
ok = ok and len(stmt_get.get("ids", [])) > 0
ok = ok and any(
    (r.get("metadata") or {}).get("entity_id") == doc_entity
    for r in doc_query
)
ok = ok and any(
    (r.get("metadata") or {}).get("entity_id") == stmt_entity
    for r in stmt_query
)

print("MANIFEST_E2E_PASS" if ok else "MANIFEST_E2E_FAIL")

# 3) Cleanup
targets = [
    (hp_public_documents(), doc_entity),
    (hp_public_statements(), stmt_entity),
]
for cname, entity_id in targets:
    col = client.get_collection(cname)
    res = col.get(where={"entity_id": {"$eq": entity_id}})
    ids = res.get("ids", [])
    if ids:
        col.delete(ids=ids)
from datetime import datetime
from fastapi import Depends, HTTPException, Header
import uuid
from pathlib import Path
from datetime import datetime

import pandas as pd

WORLDVIEW_3 = "002c2c84-2f18-40b7-8a98-b8d813dd6cc7"
MANIFEST_PATH = Path("services/msjarvis_gis_manifest.csv")
CSV_TARGET_PATH = Path("services/msjarvisattributesgis.csv")

def deterministic_feature_id(source_system: str, source_id: str) -> str:
    namespace = uuid.UUID("11111111-2222-3333-4444-555555555555")
    name = f"{source_system}:{source_id}"
    return str(uuid.uuid5(namespace, name))

def process_manifest_row(row):
    src_path      = Path(row["source_path"])
    layer_name    = row["layer_name"]
    theme         = row["theme"]
    source_system = row["source_system"]
    source_version= row["source_version"]
    id_field      = row["id_field"]
    name_field    = row["name_field"]
    lon_field     = row["lon_field"] or None
    lat_field     = row["lat_field"] or None
    wkt_field     = row["wkt_field"] or None

    df_src = pd.read_csv(src_path)
    now_iso = datetime.utcnow().replace(microsecond=0).isoformat() + "Z"

    records = []
    for _, r in df_src.iterrows():
        source_id = str(r[id_field]) if id_field in r and pd.notna(r[id_field]) else str(uuid.uuid4())
        feature_id = deterministic_feature_id(source_system, source_id)

        feature_label = str(r[name_field]) if name_field in r and pd.notna(r[name_field]) else layer_name

        lon = float(r[lon_field]) if lon_field and lon_field in r and pd.notna(r[lon_field]) else None
        lat = float(r[lat_field]) if lat_field and lat_field in r and pd.notna(r[lat_field]) else None

        geom_wkt = None
        if wkt_field and wkt_field in r and isinstance(r[wkt_field], str) and r[wkt_field].strip():
            geom_wkt = r[wkt_field].strip()

        records.append({
            "layer_name":      layer_name,
            "feature_id":      feature_id,
            "feature_label":   feature_label,
            "worldview_id":    WORLDVIEW_3,
            "geometry_type":   "GEOMETRY",
            "lon":             lon,
            "lat":             lat,
            "geom_wkt":        geom_wkt,
            "county":          None,
            "theme":           theme,
            "source_system":   source_system,
            "source_id":       source_id,
            "source_version":  source_version,
            "source_path":     str(src_path),
            "captured_at":     None,
            "imported_at":     now_iso,
            "import_batch_id": f"batch_{layer_name}_{now_iso}",
            "source_type":     "attributes_csv",
            "created_by":      "msjarvis-etl",
        })

    return pd.DataFrame.from_records(records)

def main():
    manifest = pd.read_csv(MANIFEST_PATH)
    dfs = []
    for _, row in manifest.iterrows():
        dfs.append(process_manifest_row(row))

    if not dfs:
        print("No manifest rows to process.")
        return

    df_new = pd.concat(dfs, ignore_index=True)

    if CSV_TARGET_PATH.exists():
        df_existing = pd.read_csv(CSV_TARGET_PATH)
        all_cols = list(df_existing.columns)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        df_combined.to_csv(CSV_TARGET_PATH, index=False, columns=all_cols)
    else:
        df_new.to_csv(CSV_TARGET_PATH, index=False)

    print(f"Appended {len(df_new)} records from manifest to {CSV_TARGET_PATH}")

if __name__ == "__main__":
    main()
import csv
import os
import chromadb
from chromadb.config import Settings

# HTTP Chroma configuration
CHROMA_HOST = os.getenv("CHROMA_HOST", "localhost")
CHROMA_PORT = int(os.getenv("CHROMA_PORT", "8002"))

client = chromadb.HttpClient(
    host=CHROMA_HOST,
    port=CHROMA_PORT,
    settings=Settings(anonymized_telemetry=False),
)

# Optional: restrict to specific collections via env var
env_collections = os.getenv("CHROMA_COLLECTIONS")

if env_collections:
    COLLECTIONS = [c.strip() for c in env_collections.split(",") if c.strip()]
else:
    # Discover all collections from this Chroma instance
    COLLECTIONS = [c.name for c in client.list_collections()]

with open("chroma_manifest.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "collection",
        "id",
        "file_id",
        "ueid",
        "layer_name",
        "lat",
        "lon",
        "bbox",
        "place_name",
        "county",
        "state",
        "country",
        "geodb_id",
        "sourcetable",
    ])

    for coll_name in COLLECTIONS:
        coll = client.get_collection(coll_name)
        offset = 0
        batch = 500

        while True:
            res = coll.get(
                include=["metadatas"],
                limit=batch,
                offset=offset,
            )
            ids = res.get("ids", [])
            if not ids:
                break

            metadatas = res.get("metadatas", []) or []
            for i, doc_id in enumerate(ids):
                md = metadatas[i] or {}
                writer.writerow([
                    coll_name,
                    doc_id,
                    md.get("file_id") or md.get("ueid") or "",
                    md.get("ueid") or "",
                    md.get("layer_name") or "",
                    md.get("lat") or "",
                    md.get("lon") or "",
                    md.get("bbox") or "",
                    md.get("place_name") or "",
                    md.get("county") or "",
                    md.get("state") or "",
                    md.get("country") or "",
                    md.get("geodb_id") or "",
                    md.get("sourcetable") or "",
                ])

            offset += batch
from services.hilbert.collection_manifest import hp_public_documents, hp_public_statements
from services.hilbert import civic_query
import chromadb

client = chromadb.HttpClient(host="jarvis-chroma", port=8000)

doc_entity = "smoke-manifest-doc-20260713"
stmt_entity = "smoke-manifest-stmt-20260713"

doc_content = "Smoke test document for manifest-resolved public civic documents collection (E2E harness)."
stmt_content = "Smoke test statement for manifest-resolved public civic statements collection (E2E harness)."

doc_col = client.get_collection(hp_public_documents())
stmt_col = client.get_collection(hp_public_statements())

# 1) Ingest
doc_id = "doc-" + doc_entity
stmt_id = "stmt-" + stmt_entity

doc_meta = {
    "registration_layer": 1,
    "public_opt_in": False,
    "source": "stack-smoke-test",
    "entity_id": doc_entity,
    "display_name": "Smoke Manifest Document",
    "doc_type": "smoke-test",
}
stmt_meta = {
    "registration_layer": 1,
    "public_opt_in": False,
    "source": "stack-smoke-test",
    "entity_id": stmt_entity,
    "display_name": "Smoke Manifest Statement",
    "statement_type": "smoke-test",
}

doc_col.upsert(ids=[doc_id], documents=[doc_content], metadatas=[doc_meta])
stmt_col.upsert(ids=[stmt_id], documents=[stmt_content], metadatas=[stmt_meta])

# 2) Query via civic_query (manifest-backed names)
doc_get = doc_col.get(
    where={"entity_id": {"$eq": doc_entity}},
    include=["documents", "metadatas"],
)
stmt_get = stmt_col.get(
    where={"entity_id": {"$eq": stmt_entity}},
    include=["documents", "metadatas"],
)

doc_query = civic_query.query_documents(
    text="Smoke test document manifest resolved public civic documents collection",
    n_results=5,
    source="stack-smoke-test",
    doc_type="smoke-test",
)
stmt_query = civic_query.query_statements(
    text="Smoke test statement manifest resolved public civic statements collection",
    n_results=5,
    source="stack-smoke-test",
    statement_type="smoke-test",
)

ok = True
ok = ok and len(doc_get.get("ids", [])) > 0
ok = ok and len(stmt_get.get("ids", [])) > 0
ok = ok and any(
    (r.get("metadata") or {}).get("entity_id") == doc_entity
    for r in doc_query
)
ok = ok and any(
    (r.get("metadata") or {}).get("entity_id") == stmt_entity
    for r in stmt_query
)

print("MANIFEST_E2E_PASS" if ok else "MANIFEST_E2E_FAIL")

# 3) Cleanup
targets = [
    (hp_public_documents(), doc_entity),
    (hp_public_statements(), stmt_entity),
]
for cname, entity_id in targets:
    col = client.get_collection(cname)
    res = col.get(where={"entity_id": {"$eq": entity_id}})
    ids = res.get("ids", [])
    if ids:
        col.delete(ids=ids)
from datetime import datetime
from fastapi import Depends, HTTPException, Header
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/msjarvis-rebuild$ for Q in \
  '{"query":"Fayette County West Virginia","nresults":2,"request_purpose":"public_civic_geographic_retrieval"}' \
  '{"query":"Census tract Oak Hill West Virginia","nresults":2,"request_purpose":"public_civic_geographic_retrieval"}'
do
  echo "=== QUERY ==="
  echo "$Q"
  RESP=$(curl -s -X POST http://localhost:8004/gis_rag \
    -H 'Content-Type: application/json' \
    -H 'x-msallis-role: researcher' \
    -H 'x-msallis-purpose: public_civic_geographic_retrieval' \
    -H 'x-msallis-legal-basis: authorized internal audit' \
    --data "$Q")
  printf '%s\n' "$RESP"
  printf '%s' "$RESP" | python3 -m json.tool || true
  echo
done
=== QUERY ===
{"query":"Fayette County West Virginia","nresults":2,"request_purpose":"public_civic_geographic_retrieval"}
{"detail":"manifest permitted_use missing for collection 'gbimwvzctasv1'"}
{
    "detail": "manifest permitted_use missing for collection 'gbimwvzctasv1'"
}

=== QUERY ===
{"query":"Census tract Oak Hill West Virginia","nresults":2,"request_purpose":"public_civic_geographic_retrieval"}
{"detail":"manifest permitted_use missing for collection 'gbimwvzctasv1'"}
{
    "detail": "manifest permitted_use missing for collection 'gbimwvzctasv1'"
}

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/msjarvis-rebuild$ 

