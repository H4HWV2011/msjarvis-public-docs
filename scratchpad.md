hell remains active.
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-trust-integration$ set +e 
set +u

summary='/tmp/msjarvis-guardian-contract-summary-20260808T011756Z.json'
contract='/tmp/msjarvis-guardian-pdr-mar-build-contract.json'

if test -f "$summary"; then
  python3 - "$summary" "$contract" <<'PY'
import json
import sys
from pathlib import Path

source = Path(sys.argv[1])
target = Path(sys.argv[2])
data = json.loads(source.read_text(encoding="utf-8"))

api = data.get("constitutional_api", {})
functions = api.get("functions", [])
routes = api.get("routes", [])
related = data.get("related_python_files", [])
tests = data.get("service_tests", [])
schemas = data.get("json_schema_candidates", [])
echo 'Shell remains active.'al summary: $summary") + "\n",r test passes."
/tmp/msjarvis-guardian-pdr-mar-build-contract.json
bytes=15210

=== build contract ===
{
  "existing_contract_assets": {
    "crypto_or_receipt_files": [
      "schemas/mountainshares-trust-receipts/v1/admit_runtime_authority_manifest.py",
      "schemas/mountainshares-trust-receipts/v1/durable_ledger/models.py",
      "schemas/mountainshares-trust-receipts/v1/durable_ledger/sqlite_backend.py",
      "schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py",
      "schemas/mountainshares-trust-receipts/v1/memory_authorization_gate.py",
      "schemas/mountainshares-trust-receipts/v1/operation_intent_rules.py",
      "schemas/mountainshares-trust-receipts/v1/receipt_chain_errors.py",
      "schemas/mountainshares-trust-receipts/v1/receipt_chain_rules.py",
      "schemas/mountainshares-trust-receipts/v1/receipt_crypto.py",
      "schemas/mountainshares-trust-receipts/v1/receipt_rules.py",
      "schemas/mountainshares-trust-receipts/v1/runtime_manifest_crypto.py",
      "schemas/mountainshares-trust-receipts/v1/test_canonicalization_contract.py",
      "schemas/mountainshares-trust-receipts/v1/test_canonicalization_cross_module_integration.py",
      "schemas/mountainshares-trust-receipts/v1/test_canonicalization_mutation_integrity.py",
      "schemas/mountainshares-trust-receipts/v1/test_canonicalization_negative_paths.py",
      "schemas/mountainshares-trust-receipts/v1/test_canonicalization_replay_determinism.py",
      "schemas/mountainshares-trust-receipts/v1/test_durable_ledger.py",
      "schemas/mountainshares-trust-receipts/v1/test_durable_ledger_sqlite.py",
      "schemas/mountainshares-trust-receipts/v1/test_intent_consumption.py",
      "schemas/mountainshares-trust-receipts/v1/test_receipt_chain_rules.py",
      "schemas/mountainshares-trust-receipts/v1/test_runtime_authority_manifest_canonicalization.py",
      "schemas/mountainshares-trust-receipts/v1/test_runtime_authority_manifest_schema.py",
      "schemas/mountainshares-trust-receipts/v1/usage_ledger.py",
      "schemas/mountainshares-trust-receipts/v1/validate_receipt.py",
      "schemas/mountainshares-trust-receipts/v1/verify_admission_linked_receipt_chain.py",
      "schemas/mountainshares-trust-receipts/v1/verify_memory_authorization_receipt.py",
      "schemas/mountainshares-trust-receipts/v1/verify_policy_decision_receipt.py",
      "schemas/mountainshares-trust-receipts/v1/verify_projection_receipt.py",
      "schemas/mountainshares-trust-receipts/v1/verify_response_receipt.py",
      "schemas/mountainshares-trust-receipts/v1/verify_runtime_admission_record.py",
      "schemas/mountainshares-trust-receipts/v1/verify_runtime_authority_manifest.py",
      "services/bbb_signature_verifier.py",
      "services/conversion_service.py",
      "services/crypto_client.py",
      "services/governed_manifest_promote.py",
      "services/hilbert/sign_promotion_event.py",
      "services/hilbert/verify_promotion_event.py",
      "services/jarviscryptopolicy.py",
      "services/judgesigner.py",
      "services/ms_egeria_facebook_autopost.py",
      "tests/test_ch33_ch35_judge_verdict_contract.py",
      "thesis_chapter_gates/probes/ch19_container_architecture_routing_probe.py"
    ],
    "guardian_or_policy_files": [
      "auth_router.py",
      "diagnostics/gateway_head_1_220.py",
      "diagnostics/gateway_mid_220_420.py",
      "diagnostics/gateway_tail_420_700.py",
      "diagnostics/unified_gateway_extended_policy_sections_20260801T022011Z.py",
      "diagnostics/unified_gateway_live_20260801T020501Z.py",
      "schemas/mountainshares-trust-receipts/v1/durable_ledger/models.py",
      "schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py",
      "schemas/mountainshares-trust-receipts/v1/memory_authorization_gate.py",
      "schemas/mountainshares-trust-receipts/v1/receipt_chain_rules.py",
      "schemas/mountainshares-trust-receipts/v1/test_canonicalization_contract.py",
      "schemas/mountainshares-trust-receipts/v1/test_canonicalization_cross_module_integration.py",
      "schemas/mountainshares-trust-receipts/v1/test_canonicalization_mutation_integrity.py",
      "schemas/mountainshares-trust-receipts/v1/test_canonicalization_negative_paths.py",
      "schemas/mountainshares-trust-receipts/v1/test_canonicalization_replay_determinism.py",
      "schemas/mountainshares-trust-receipts/v1/test_durable_ledger.py",
      "schemas/mountainshares-trust-receipts/v1/test_durable_ledger_sqlite.py",
      "schemas/mountainshares-trust-receipts/v1/test_receipt_chain_rules.py",
      "schemas/mountainshares-trust-receipts/v1/test_runtime_authority_manifest_canonicalization.py",
      "schemas/mountainshares-trust-receipts/v1/verify_admission_linked_receipt_chain.py",
      "schemas/mountainshares-trust-receipts/v1/verify_memory_authorization_receipt.py",
      "schemas/mountainshares-trust-receipts/v1/verify_policy_decision_receipt.py",
      "services/belief_revision_engine.py",
      "services/constitutional_api.PROD_BACKUP.py",
      "services/constitutional_api.py",
      "services/constitutional_guardian.PROD_BACKUP.py",
      "services/constitutional_guardian.py",
      "services/hilbert/automated_learning_gap_review.py",
      "services/hilbert/ch21_background_patterns_probe.py",
      "services/hilbert/ch22_identity_retention_probe.py",
      "services/hilbert/ch25_consciousness_coordinator_probe.py",
      "services/hilbert/ch36_identity_registration_probe.py",
      "services/hilbert/ch51_community_commons_probe.py",
      "services/hilbert/ch52_recurrent_epistemic_loop_probe.py",
      "services/hilbert/continuous_validation_harness.py",
      "services/hilbert/dgm_closure_probe.py",
      "services/hilbert/dual_track_meaning_analysis.py",
      "services/hilbert/internal_state_sandbox_probe.py",
      "services/hilbert/people_session_promotion.py",
      "services/hilbert/pia_subspace_stability_review.py",
      "services/hilbert/pituitary_global_modes_probe.py",
      "services/hilbert/woah_closure_probe.py",
      "services/jarvis-constitutional-guardian_constitutional_api.py",
      "services/jarvis-hippocampus_hippocampus_service.py",
      "services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py",
      "services/jarviscryptopolicy.py",
      "services/manifest_endpoints.py",
      "services/ms_jarvis_blood_brain_barrier.py",
      "services/ms_jarvis_unified_gateway_mountainshares_private.py",
      "services/nbb_darwin_godel_machines.py",
      "services/spatial_sandbox.py",
      "services/test_caller_auth.py",
      "services/test_stage_6_11_6_enforcement.py",
      "services/test_stage_6_11_7_admission_live.py",
      "tests/test_antisurveillance_guard.py",
      "tests/test_ch07_executive_routing_contract.py",
      "tests/test_ch11_gateway_orchestration_contract.py",
      "tests/test_ch26_governance_watchdog_contract.py",
      "tests/test_ch33_ch35_judge_verdict_contract.py",
      "thesis_chapter_gates/probes/ch03_mountainshares_dao_probe.py",
      "thesis_chapter_gates/probes/ch08_quantum_inspired_entanglement_probe.py",
      "thesis_chapter_gates/probes/ch17_probe.py",
      "thesis_chapter_gates/probes/ch17_probe_v2.py",
      "thesis_chapter_gates/probes/ch19_container_architecture_routing_probe.py",
      "thesis_chapter_gates/probes/ch20_probe.py",
      "thesis_chapter_gates/probes/ch23_dual_tracks_meaning_analysis_probe.py",
      "thesis_chapter_gates/probes/ch24_feedback_broader_layers_probe.py",
      "thesis_chapter_gates/probes/ch27_probe.py",
      "thesis_chapter_gates/probes/ch32_probe.py",
      "thesis_chapter_gates/probes/ch34_spiritual_root_mother_carrie_probe.py",
      "thesis_chapter_gates/probes/ch38_external_communication_authority_probe.py",
      "thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py",
      "thesis_chapter_gates/probes/ch50_per_user_direct_sum_probe.py"
    ],
    "schema_candidates": [
      "schemas/mountainshares-trust-receipts/v1/memory-authorization-receipt.schema.json",
      "schemas/mountainshares-trust-receipts/v1/policy-decision-receipt.schema.json",
      "schemas/mountainshares-trust-receipts/v1/projection-receipt.schema.json",
      "schemas/mountainshares-trust-receipts/v1/response-receipt.schema.json",
      "schemas/mountainshares-trust-receipts/v1/runtime-admission-record.schema.json",
      "schemas/mountainshares-trust-receipts/v1/runtime-authority-manifest.schema.json",
      "schemas/mountainshares-trust-receipts/v1/signed-operation-intent.schema.json"
    ],
    "service_tests": [
      "services/test_aacpe_features.py",
      "services/test_aapcappe_corpus.py",
      "services/test_aapcappe_retrieval.py",
      "services/test_caller_auth.py",
      "services/test_chroma_client.py",
      "services/test_chromadb_heartbeat.py",
      "services/test_chromadb_v2_heartbeat.py",
      "services/test_ddg_verbose.py",
      "services/test_end_to_end_woah_fifthdgm.py",
      "services/test_fifth_dgm_integration.py",
      "services/test_full_brain_integration.py",
      "services/test_gbim_llm_summary.py",
      "services/test_gbim_semantic_query.py",
      "services/test_geodb_llm_summary.py",
      "services/test_gis_chat.py",
      "services/test_health_access_gbim.py",
      "services/test_imm_query.py",
      "services/test_knowledge_base.py",
      "services/test_method_tracking.py",
      "services/test_multi_collection_query.py",
      "services/test_rag.py",
      "services/test_retrieval_endpoint.py",
      "services/test_spatial_awareness.py",
      "services/test_stage_6_11_6_enforcement.py",
      "services/test_stage_6_11_7_admission_live.py"
    ]
  },
  "git": {
    "branch": "stage-6.11.6-runtime-admission-enhancement",
    "head": "5f728e632eb130e919f9b1a22c16f27d2e2566ce",
    "root": "/home/cakidd/msjarvis-trust-integration",
    "status_short": []
  },
  "implementation_rule": "Do not generate a guardian private key, issue a receipt, or admit protected projection until every verifier test passes.",
  "implementation_target": {
    "all_routes": [
      {
        "function": "health",
        "line": 124,
        "method": "GET",
        "path": "/health"
      },
      {
        "function": "constitutional_status",
        "line": 133,
        "method": "GET",
        "path": "/constitutional/status"
      },
      {
        "function": "constitutional_principles",
        "line": 147,
        "method": "GET",
        "path": "/constitutional/principles"
      },
      {
        "function": "constitutional_check",
        "line": 296,
        "method": "POST",
        "path": "/constitutional/check"
      },
      {
        "function": "constitutional_audit",
        "line": 401,
        "method": "GET",
        "path": "/constitutional/audit"
      },
      {
        "function": "constitutional_audit_stats",
        "line": 424,
        "method": "GET",
        "path": "/constitutional/audit/stats"
      },
      {
        "function": "constitutional_versions",
        "line": 459,
        "method": "GET",
        "path": "/constitutional/versions"
      },
      {
        "function": "constitutional_changes",
        "line": 494,
        "method": "GET",
        "path": "/constitutional/changes/{version}"
      },
      {
        "function": "constitutional_transparency",
        "line": 529,
        "method": "GET",
        "path": "/constitutional/transparency"
      }
    ],
    "all_top_level_functions": [
      {
        "async": false,
        "line": 59,
        "name": "write_audit_entry",
        "routes": []
      },
      {
        "async": false,
        "line": 68,
        "name": "read_audit_log",
        "routes": []
      },
      {
        "async": true,
        "line": 102,
        "name": "load_constitution_versions",
        "routes": []
      },
      {
        "async": true,
        "line": 124,
        "name": "health",
        "routes": [
          {
            "method": "GET",
            "path": "/health"
          }
        ]
      },
      {
        "async": true,
        "line": 133,
        "name": "constitutional_status",
        "routes": [
          {
            "method": "GET",
            "path": "/constitutional/status"
          }
        ]
      },
      {
        "async": true,
        "line": 147,
        "name": "constitutional_principles",
        "routes": [
          {
            "method": "GET",
            "path": "/constitutional/principles"
          }
        ]
      },
      {
        "async": false,
        "line": 170,
        "name": "_sha256_commitment",
        "routes": []
      },
      {
        "async": false,
        "line": 180,
        "name": "_require_runtime_admission",
        "routes": []
      },
      {
        "async": false,
        "line": 269,
        "name": "_authenticate_caller",
        "routes": []
      },
      {
        "async": true,
        "line": 296,
        "name": "constitutional_check",
        "routes": [
          {
            "method": "POST",
            "path": "/constitutional/check"
          }
        ]
      },
      {
        "async": true,
        "line": 401,
        "name": "constitutional_audit",
        "routes": [
          {
            "method": "GET",
            "path": "/constitutional/audit"
          }
        ]
      },
      {
        "async": true,
        "line": 424,
        "name": "constitutional_audit_stats",
        "routes": [
          {
            "method": "GET",
            "path": "/constitutional/audit/stats"
          }
        ]
      },
      {
        "async": true,
        "line": 459,
        "name": "constitutional_versions",
        "routes": [
          {
            "method": "GET",
            "path": "/constitutional/versions"
          }
        ]
      },
      {
        "async": true,
        "line": 494,
        "name": "constitutional_changes",
        "routes": [
          {
            "method": "GET",
            "path": "/constitutional/changes/{version}"
          }
        ]
      },
      {
        "async": true,
        "line": 529,
        "name": "constitutional_transparency",
        "routes": [
          {
            "method": "GET",
            "path": "/constitutional/transparency"
          }
        ]
      }
    ],
    "api_path": "services/constitutional_api.py",
    "api_sha256": "3a94b20a56bc0e3720f0b87fd2e96735804d6b4f6f6de37eb3ff9fe23f282b84",
    "constitutional_check_routes": [
      {
        "function": "constitutional_check",
        "line": 296,
        "method": "POST",
        "path": "/constitutional/check"
      }
    ]
  },
  "required_new_contracts": [
    "Policy Decision Receipt schema",
    "Memory Authorization Receipt schema",
    "Canonical signed-payload procedure",
    "Guardian issuer-key registry and key identifier",
    "PDR signature verifier",
    "MAR subject-signature verifier",
    "MAR Guardian-attestation verifier",
    "Receipt expiration verification",
    "Receipt request-binding and replay-state enforcement",
    "Fail-closed denial tests"
  ],
  "required_runtime_dependencies": {
    "cryptography": "available",
    "fastapi": "available",
    "jsonschema": "available",
    "pydantic": "available"
  },
  "type": "msjarvis.pdr-mar-build-contract/v1"
}

=== contract hash ===
6280e66934c41a3a3a2c8178a61df88f49216df3cb43baa5737955df7c99b1b9  /tmp/msjarvis-guardian-pdr-mar-build-contract.json

Shell remains active.
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-trust-integration$ 

