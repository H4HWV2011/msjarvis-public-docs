(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-trust-integration$ set +e 
set +u

summary='/tmp/msjarvis-guardian-contract-summary-20260808T011756Z.json'
capsule='/tmp/msjarvis-guardian-implementation-capsule.md'

if test -f "$summary"; then
  python3 - "$summary" "$capsule" <<'PY'
import json
import sys
from pathlib import Path

summary_path = Path(sys.argv[1])
capsule_path = Path(sys.argv[2])

data = json.loads(summary_path.read_text(encoding="utf-8"))

api = data.get("constitutional_api", {})
git = data.get("git", {})

lines = [
    "# Guardian PDR/MAR Implementation Capsule",
    "",
echo 'Shell remains active.': $summary"ize}")n", encoding="utf-8")', '')}"
/tmp/msjarvis-guardian-implementation-capsule.md
bytes=13891

=== compact capsule ===
# Guardian PDR/MAR Implementation Capsule

## Git
- Root: `/home/cakidd/msjarvis-trust-integration`
- Branch: `stage-6.11.6-runtime-admission-enhancement`
- HEAD: `5f728e632eb130e919f9b1a22c16f27d2e2566ce`
- Status: `[]`

## Constitutional API
- Path: `services/constitutional_api.py`
- SHA-256: `3a94b20a56bc0e3720f0b87fd2e96735804d6b4f6f6de37eb3ff9fe23f282b84`

### Routes
- `GET /health` → `health` at line 124
- `GET /constitutional/status` → `constitutional_status` at line 133
- `GET /constitutional/principles` → `constitutional_principles` at line 147
- `POST /constitutional/check` → `constitutional_check` at line 296
- `GET /constitutional/audit` → `constitutional_audit` at line 401
- `GET /constitutional/audit/stats` → `constitutional_audit_stats` at line 424
- `GET /constitutional/versions` → `constitutional_versions` at line 459
- `GET /constitutional/changes/{version}` → `constitutional_changes` at line 494
- `GET /constitutional/transparency` → `constitutional_transparency` at line 529

### Functions
- `write_audit_entry` (line 59; async=False; routes=none)
- `read_audit_log` (line 68; async=False; routes=none)
- `load_constitution_versions` (line 102; async=True; routes=none)
- `health` (line 124; async=True; routes=GET /health)
- `constitutional_status` (line 133; async=True; routes=GET /constitutional/status)
- `constitutional_principles` (line 147; async=True; routes=GET /constitutional/principles)
- `_sha256_commitment` (line 170; async=False; routes=none)
- `_require_runtime_admission` (line 180; async=False; routes=none)
- `_authenticate_caller` (line 269; async=False; routes=none)
- `constitutional_check` (line 296; async=True; routes=POST /constitutional/check)
- `constitutional_audit` (line 401; async=True; routes=GET /constitutional/audit)
- `constitutional_audit_stats` (line 424; async=True; routes=GET /constitutional/audit/stats)
- `constitutional_versions` (line 459; async=True; routes=GET /constitutional/versions)
- `constitutional_changes` (line 494; async=True; routes=GET /constitutional/changes/{version})
- `constitutional_transparency` (line 529; async=True; routes=GET /constitutional/transparency)

## Receipt/Signing Files
- `auth_router.py` — guardian
- `diagnostics/gateway_head_1_220.py` — guardian
- `diagnostics/gateway_mid_220_420.py` — guardian
- `diagnostics/gateway_tail_420_700.py` — guardian
- `diagnostics/unified_gateway_extended_policy_sections_20260801T022011Z.py` — guardian
- `diagnostics/unified_gateway_live_20260801T020501Z.py` — guardian
- `schemas/mountainshares-trust-receipts/v1/admit_runtime_authority_manifest.py` — signature
- `schemas/mountainshares-trust-receipts/v1/durable_ledger/models.py` — policy_decision, signature
- `schemas/mountainshares-trust-receipts/v1/durable_ledger/sqlite_backend.py` — signature
- `schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py` — canonical_payload, ed25519, guardian, policy_decision, receipt, receipt_crypto, signature
- `schemas/mountainshares-trust-receipts/v1/memory_authorization_gate.py` — ed25519, guardian, memory_authorization, receipt, receipt_crypto, signature
- `schemas/mountainshares-trust-receipts/v1/operation_intent_rules.py` — ed25519, receipt, receipt_crypto, signature
- `schemas/mountainshares-trust-receipts/v1/receipt_chain_errors.py` — receipt
- `schemas/mountainshares-trust-receipts/v1/receipt_chain_rules.py` — guardian, memory_authorization, policy_decision, receipt
- `schemas/mountainshares-trust-receipts/v1/receipt_crypto.py` — canonical_payload, ed25519, receipt, signature
- `schemas/mountainshares-trust-receipts/v1/receipt_rules.py` — receipt
- `schemas/mountainshares-trust-receipts/v1/runtime_manifest_crypto.py` — ed25519, signature
- `schemas/mountainshares-trust-receipts/v1/test_canonicalization_contract.py` — canonical_payload, ed25519, guardian, receipt, receipt_crypto, signature
- `schemas/mountainshares-trust-receipts/v1/test_canonicalization_cross_module_integration.py` — canonical_payload, ed25519, guardian, receipt, receipt_crypto, signature
- `schemas/mountainshares-trust-receipts/v1/test_canonicalization_mutation_integrity.py` — canonical_payload, ed25519, guardian, receipt, receipt_crypto, signature
- `schemas/mountainshares-trust-receipts/v1/test_canonicalization_negative_paths.py` — canonical_payload, ed25519, guardian, receipt, receipt_crypto, signature
- `schemas/mountainshares-trust-receipts/v1/test_canonicalization_replay_determinism.py` — canonical_payload, ed25519, guardian, receipt, receipt_crypto, signature
- `schemas/mountainshares-trust-receipts/v1/test_durable_ledger.py` — policy_decision, signature
- `schemas/mountainshares-trust-receipts/v1/test_durable_ledger_sqlite.py` — policy_decision, signature
- `schemas/mountainshares-trust-receipts/v1/test_intent_consumption.py` — receipt
- `schemas/mountainshares-trust-receipts/v1/test_receipt_chain_rules.py` — policy_decision, receipt
- `schemas/mountainshares-trust-receipts/v1/test_runtime_authority_manifest_canonicalization.py` — canonical_payload, ed25519, guardian, signature
- `schemas/mountainshares-trust-receipts/v1/test_runtime_authority_manifest_schema.py` — receipt
- `schemas/mountainshares-trust-receipts/v1/usage_ledger.py` — receipt
- `schemas/mountainshares-trust-receipts/v1/validate_receipt.py` — receipt
- `schemas/mountainshares-trust-receipts/v1/verify_admission_linked_receipt_chain.py` — memory_authorization, policy_decision, receipt
- `schemas/mountainshares-trust-receipts/v1/verify_memory_authorization_receipt.py` — ed25519, guardian, memory_authorization, receipt, receipt_crypto, signature
- `schemas/mountainshares-trust-receipts/v1/verify_policy_decision_receipt.py` — ed25519, guardian, policy_decision, receipt, receipt_crypto, signature
- `schemas/mountainshares-trust-receipts/v1/verify_projection_receipt.py` — ed25519, receipt, receipt_crypto, signature
- `schemas/mountainshares-trust-receipts/v1/verify_response_receipt.py` — ed25519, receipt, receipt_crypto, signature
- `schemas/mountainshares-trust-receipts/v1/verify_runtime_admission_record.py` — signature
- `schemas/mountainshares-trust-receipts/v1/verify_runtime_authority_manifest.py` — receipt
- `services/bbb_signature_verifier.py` — signature
- `services/belief_revision_engine.py` — guardian
- `services/constitutional_api.PROD_BACKUP.py` — guardian
- `services/constitutional_api.py` — guardian
- `services/constitutional_guardian.PROD_BACKUP.py` — guardian
- `services/constitutional_guardian.py` — guardian
- `services/conversion_service.py` — receipt
- `services/crypto_client.py` — ed25519
- `services/governed_manifest_promote.py` — signature
- `services/hilbert/automated_learning_gap_review.py` — guardian
- `services/hilbert/ch21_background_patterns_probe.py` — guardian
- `services/hilbert/ch22_identity_retention_probe.py` — guardian
- `services/hilbert/ch25_consciousness_coordinator_probe.py` — guardian
- `services/hilbert/ch36_identity_registration_probe.py` — guardian
- `services/hilbert/ch51_community_commons_probe.py` — guardian
- `services/hilbert/ch52_recurrent_epistemic_loop_probe.py` — guardian
- `services/hilbert/continuous_validation_harness.py` — guardian
- `services/hilbert/dgm_closure_probe.py` — guardian
- `services/hilbert/dual_track_meaning_analysis.py` — guardian
- `services/hilbert/internal_state_sandbox_probe.py` — guardian
- `services/hilbert/people_session_promotion.py` — guardian
- `services/hilbert/pia_subspace_stability_review.py` — guardian
- `services/hilbert/pituitary_global_modes_probe.py` — guardian
- `services/hilbert/sign_promotion_event.py` — signature
- `services/hilbert/verify_promotion_event.py` — signature
- `services/hilbert/woah_closure_probe.py` — guardian
- `services/jarvis-constitutional-guardian_constitutional_api.py` — guardian
- `services/jarvis-hippocampus_hippocampus_service.py` — guardian
- `services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py` — guardian
- `services/jarviscryptopolicy.py` — revocation, signature
- `services/judgesigner.py` — signature
- `services/manifest_endpoints.py` — guardian
- `services/ms_egeria_facebook_autopost.py` — signature
- `services/ms_jarvis_blood_brain_barrier.py` — guardian
- `services/ms_jarvis_unified_gateway_mountainshares_private.py` — guardian
- `services/nbb_darwin_godel_machines.py` — guardian
- `services/spatial_sandbox.py` — guardian
- `services/test_caller_auth.py` — guardian
- `services/test_stage_6_11_6_enforcement.py` — guardian
- `services/test_stage_6_11_7_admission_live.py` — guardian
- `tests/test_antisurveillance_guard.py` — guardian
- `tests/test_ch07_executive_routing_contract.py` — guardian
- `tests/test_ch11_gateway_orchestration_contract.py` — guardian
- `tests/test_ch26_governance_watchdog_contract.py` — guardian
- `tests/test_ch33_ch35_judge_verdict_contract.py` — guardian, signature
- `thesis_chapter_gates/probes/ch03_mountainshares_dao_probe.py` — guardian
- `thesis_chapter_gates/probes/ch08_quantum_inspired_entanglement_probe.py` — guardian
- `thesis_chapter_gates/probes/ch17_probe.py` — guardian
- `thesis_chapter_gates/probes/ch17_probe_v2.py` — guardian
- `thesis_chapter_gates/probes/ch19_container_architecture_routing_probe.py` — guardian, signature
- `thesis_chapter_gates/probes/ch20_probe.py` — guardian
- `thesis_chapter_gates/probes/ch23_dual_tracks_meaning_analysis_probe.py` — guardian
- `thesis_chapter_gates/probes/ch24_feedback_broader_layers_probe.py` — guardian
- `thesis_chapter_gates/probes/ch27_probe.py` — guardian
- `thesis_chapter_gates/probes/ch32_probe.py` — guardian
- `thesis_chapter_gates/probes/ch34_spiritual_root_mother_carrie_probe.py` — guardian
- `thesis_chapter_gates/probes/ch38_external_communication_authority_probe.py` — guardian
- `thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py` — guardian
- `thesis_chapter_gates/probes/ch50_per_user_direct_sum_probe.py` — guardian

## Tests
- `services/test_aacpe_features.py`
- `services/test_aapcappe_corpus.py`
- `services/test_aapcappe_retrieval.py`
- `services/test_caller_auth.py`
- `services/test_chroma_client.py`
- `services/test_chromadb_heartbeat.py`
- `services/test_chromadb_v2_heartbeat.py`
- `services/test_ddg_verbose.py`
- `services/test_end_to_end_woah_fifthdgm.py`
- `services/test_fifth_dgm_integration.py`
- `services/test_full_brain_integration.py`
- `services/test_gbim_llm_summary.py`
- `services/test_gbim_semantic_query.py`
- `services/test_geodb_llm_summary.py`
- `services/test_gis_chat.py`
- `services/test_health_access_gbim.py`
- `services/test_imm_query.py`
- `services/test_knowledge_base.py`
- `services/test_method_tracking.py`
- `services/test_multi_collection_query.py`
- `services/test_rag.py`
- `services/test_retrieval_endpoint.py`
- `services/test_spatial_awareness.py`
- `services/test_stage_6_11_6_enforcement.py`
- `services/test_stage_6_11_7_admission_live.py`

## JSON Schema Candidates
- `schemas/mountainshares-trust-receipts/v1/memory-authorization-receipt.schema.json`
- `schemas/mountainshares-trust-receipts/v1/policy-decision-receipt.schema.json`
- `schemas/mountainshares-trust-receipts/v1/projection-receipt.schema.json`
- `schemas/mountainshares-trust-receipts/v1/response-receipt.schema.json`
- `schemas/mountainshares-trust-receipts/v1/runtime-admission-record.schema.json`
- `schemas/mountainshares-trust-receipts/v1/runtime-authority-manifest.schema.json`
- `schemas/mountainshares-trust-receipts/v1/signed-operation-intent.schema.json`

## Dependencies
- `cryptography`: available
- `fastapi`: available
- `jsonschema`: available
- `nacl`: missing
- `pydantic`: available

## WS1 Test Result
- Exit code: `0`
- Output: `.....                                                                    [100%]
=============================== warnings summary ===============================
services/test_caller_auth.py::test_missing_token_denied_401
services/test_caller_auth.py::test_invalid_token_denied_401
services/test_caller_auth.py::test_valid_token_admitted_200
services/test_caller_auth.py::test_auth_runs_before_admission
services/test_caller_auth.py::test_unconfigured_registry_fails_closed_401
  /home/cakidd/msjarvis-trust-integration/services/constitutional_api.py:101: DeprecationWarning: 
          on_event is deprecated, use lifespan event handlers instead.
  
          Read more about it in the
          [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).
          
    @app.on_event("startup")

services/test_caller_auth.py::test_missing_token_denied_401
services/test_caller_auth.py::test_invalid_token_denied_401
services/test_caller_auth.py::test_valid_token_admitted_200
services/test_caller_auth.py::test_auth_runs_before_admission
services/test_caller_auth.py::test_unconfigured_registry_fails_closed_401
  /mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/fastapi/applications.py:4495: DeprecationWarning: 
          on_event is deprecated, use lifespan event handlers instead.
  
          Read more about it in the
          [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).
          
    return self.router.on_event(event_type)

services/test_caller_auth.py::test_valid_token_admitted_200
  /home/cakidd/msjarvis-trust-integration/services/constitutional_api.py:361: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    "timestamp": datetime.utcnow().isoformat(),

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
5 passed, 11 warnings in 0.34s`

Shell remains active.
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-trust-integration$ 

