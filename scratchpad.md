(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-trust-integration$ python3 - <<'PY'
from pathlib import Path

path = Path("schemas/mountainshares-trust-receipts/v1/test_authority_admission.py")
text = path.read_text()

old_import = "from pathlib import Path\nimport json\nimport sys\n"
new_import = "from dataclasses import replace\nfrom pathlib import Path\nimport json\nimport sys\n"

if text.count(old_import) != 1:
    raise SystemExit("EXPECTED_EXACTLY_ONE_AUTHORITY_ADMISSION_IMPORT_BLOCK")

marker = '\n\nif __name__ == "__main__":\n'
if text.count(marker) != 1:
    raise SystemExit("EXPECTED_EXACTLY_ONE_AUTHORITY_ADMISSION_MAIN_MARKER")

tests = r'''

    def test_invalid_intent_signature_never_calls_ledger(self) -> None:
        original = package()
        invalid_signature = replace(
PYint("AUTHORITY_ADMISSION_DENIAL_MATRIX_EXPANDED")d, second_consumed.event_id))
AUTHORITY_ADMISSION_DENIAL_MATRIX_EXPANDED
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-trust-integration$ python3 "$TEST"
test_broken_receipt_chain_artifact_never_calls_ledger (__main__.AuthorityAdmissionTests.test_broken_receipt_chain_artifact_never_calls_ledger) ... ok
test_changed_projection_commitment_never_calls_ledger (__main__.AuthorityAdmissionTests.test_changed_projection_commitment_never_calls_ledger) ... ok
test_changed_scope_commitment_never_calls_ledger (__main__.AuthorityAdmissionTests.test_changed_scope_commitment_never_calls_ledger) ... ok
test_expired_receipt_never_calls_ledger (__main__.AuthorityAdmissionTests.test_expired_receipt_never_calls_ledger) ... ok
test_invalid_intent_signature_never_calls_ledger (__main__.AuthorityAdmissionTests.test_invalid_intent_signature_never_calls_ledger) ... ok
test_missing_receipt_artifact_never_calls_ledger (__main__.AuthorityAdmissionTests.test_missing_receipt_artifact_never_calls_ledger) ... ok
test_missing_required_receipt_field_never_calls_ledger (__main__.AuthorityAdmissionTests.test_missing_required_receipt_field_never_calls_ledger) ... ok
test_valid_admission_preserves_ledger_idempotent_reservation (__main__.AuthorityAdmissionTests.test_valid_admission_preserves_ledger_idempotent_reservation) ... ok
test_valid_receipt_constructs_context_and_reaches_ledger (__main__.AuthorityAdmissionTests.test_valid_receipt_constructs_context_and_reaches_ledger) ... ok
test_wrong_runtime_identity_never_calls_ledger (__main__.AuthorityAdmissionTests.test_wrong_runtime_identity_never_calls_ledger) ... ok
test_wrong_subject_never_calls_ledger (__main__.AuthorityAdmissionTests.test_wrong_subject_never_calls_ledger) ... ok

----------------------------------------------------------------------
Ran 11 tests in 7.375s

OK
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-trust-integration$ (
  find "$ROOT" -type f -name '*.schema.json' -print |
    LC_ALL=C sort |
    xargs -r sha256sum
) > "$ROOT/SCHEMA_BASELINE.sha256"
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-trust-integration$ (
  find "$ROOT" -type f \( -name '*.py' -o -name '*.schema.json' -o -name '*.sh' \) -print |
    LC_ALL=C sort |
    xargs -r sha256sum
) > "$ROOT/TRUST_BUILD_BASELINE.sha256"
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-trust-integration$ "$ROOT/run_trust_build_gate.sh"
TRUST_SCHEMAS_META_VALID
schemas/mountainshares-trust-receipts/v1/memory-authorization-receipt.schema.json: OK
schemas/mountainshares-trust-receipts/v1/policy-decision-receipt.schema.json: OK
schemas/mountainshares-trust-receipts/v1/projection-receipt.schema.json: OK
schemas/mountainshares-trust-receipts/v1/response-receipt.schema.json: OK
schemas/mountainshares-trust-receipts/v1/runtime-admission-record.schema.json: OK
schemas/mountainshares-trust-receipts/v1/runtime-authority-manifest.schema.json: OK
schemas/mountainshares-trust-receipts/v1/signed-operation-intent.schema.json: OK
schemas/mountainshares-trust-receipts/v1/admit_runtime_authority_manifest.py: OK
schemas/mountainshares-trust-receipts/v1/durable_ledger/__init__.py: OK
schemas/mountainshares-trust-receipts/v1/durable_ledger/authority_admission.py: OK
schemas/mountainshares-trust-receipts/v1/durable_ledger/errors.py: OK
schemas/mountainshares-trust-receipts/v1/durable_ledger/interface.py: OK
schemas/mountainshares-trust-receipts/v1/durable_ledger/models.py: OK
schemas/mountainshares-trust-receipts/v1/durable_ledger/sqlite_backend.py: OK
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py: OK
schemas/mountainshares-trust-receipts/v1/intent_consumption_ledger.py: OK
schemas/mountainshares-trust-receipts/v1/memory-authorization-receipt.schema.json: OK
schemas/mountainshares-trust-receipts/v1/memory_authorization_gate.py: OK
schemas/mountainshares-trust-receipts/v1/operation_intent_consumption.py: OK
schemas/mountainshares-trust-receipts/v1/operation_intent_rules.py: OK
schemas/mountainshares-trust-receipts/v1/policy-decision-receipt.schema.json: OK
schemas/mountainshares-trust-receipts/v1/projection-receipt.schema.json: OK
schemas/mountainshares-trust-receipts/v1/receipt_chain_errors.py: OK
schemas/mountainshares-trust-receipts/v1/receipt_chain_rules.py: OK
schemas/mountainshares-trust-receipts/v1/receipt_crypto.py: OK
schemas/mountainshares-trust-receipts/v1/receipt_rules.py: OK
schemas/mountainshares-trust-receipts/v1/response-receipt.schema.json: OK
schemas/mountainshares-trust-receipts/v1/run_trust_build_gate.sh: OK
schemas/mountainshares-trust-receipts/v1/runtime-admission-record.schema.json: OK
schemas/mountainshares-trust-receipts/v1/runtime-authority-manifest.schema.json: OK
schemas/mountainshares-trust-receipts/v1/runtime_manifest_crypto.py: OK
schemas/mountainshares-trust-receipts/v1/signed-operation-intent.schema.json: OK
schemas/mountainshares-trust-receipts/v1/test_authority_admission.py: OK
schemas/mountainshares-trust-receipts/v1/test_durable_ledger.py: OK
schemas/mountainshares-trust-receipts/v1/test_durable_ledger_sqlite.py: OK
schemas/mountainshares-trust-receipts/v1/test_intent_consumption.py: OK
schemas/mountainshares-trust-receipts/v1/test_receipt_chain_rules.py: OK
schemas/mountainshares-trust-receipts/v1/usage_ledger.py: OK
schemas/mountainshares-trust-receipts/v1/validate_receipt.py: OK
schemas/mountainshares-trust-receipts/v1/verify_admission_linked_receipt_chain.py: OK
schemas/mountainshares-trust-receipts/v1/verify_memory_authorization_receipt.py: OK
schemas/mountainshares-trust-receipts/v1/verify_policy_decision_receipt.py: OK
schemas/mountainshares-trust-receipts/v1/verify_projection_receipt.py: OK
schemas/mountainshares-trust-receipts/v1/verify_response_receipt.py: OK
schemas/mountainshares-trust-receipts/v1/verify_runtime_admission_record.py: OK
schemas/mountainshares-trust-receipts/v1/verify_runtime_authority_manifest.py: OK
schemas/mountainshares-trust-receipts/v1/verify_runtime_governance_policy.py: OK
schemas/mountainshares-trust-receipts/v1/verify_runtime_image_binding.py: OK
schemas/mountainshares-trust-receipts/v1/verify_signed_operation_intent.py: OK
RUNTIME_ADMISSION_RECORD_VERIFIED sha256:adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/runtime-admission-records-portable-test/runtime-admission-adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3.json
SIGNED_OPERATION_INTENT_VALID admission-chain-subject-key admission-chain-intent-001 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/operation-intent.valid.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-subject-key admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.memory-authorization.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-projection-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.projection.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-response-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.response.signed.json
ADMISSION_LINKED_RECEIPT_CHAIN_VALID sha256:adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3 admission-chain-pdr-001 admission-chain-mar-001 admission-chain-projection-001 admission-chain-response-001
SIGNED_OPERATION_INTENT_VALID admission-chain-subject-key admission-chain-intent-001 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/operation-intent.valid.signed.json
SIGNED_OPERATION_INTENT_INVALID INVALID_RECEIPT_LIFETIME
SIGNED_OPERATION_INTENT_INVALID UNTRUSTED_SUBJECT_KEY_ID admission-chain-unknown-subject-key
SIGNED_OPERATION_INTENT_INVALID INVALID_SIGNATURE
INTENT_CONSUMPTION_VALID admission-chain-subject-key admission-chain-intent-001
INTENT_REPLAY_REJECTED admission-chain-intent-001
INTENT_CONTEXT_MISMATCH_REJECTED admission-chain-intent-001
INTENT_NONCE_REPLAY_REJECTED admission-chain-intent-nonce-replay-001
INTENT_EXPIRED_AFTER_CONSUMPTION_REJECTED
INTENT_CONSUMED_STATE_PRESERVED_AFTER_EXPIRY
RUNTIME_ADMISSION_RECORD_VERIFIED sha256:adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/runtime-admission-records-portable-test/runtime-admission-adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3.json
SIGNED_OPERATION_INTENT_VALID admission-chain-subject-key admission-chain-intent-001 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/operation-intent.valid.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-subject-key admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.memory-authorization.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-projection-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.projection.policy-decision-mismatch.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-response-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.response.signed.json
PROJECTION_POLICY_DECISION_MISMATCH
RUNTIME_ADMISSION_RECORD_VERIFIED sha256:adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/runtime-admission-records-portable-test/runtime-admission-adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3.json
SIGNED_OPERATION_INTENT_VALID admission-chain-subject-key admission-chain-intent-001 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/operation-intent.valid.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-subject-key admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.memory-authorization.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-projection-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.projection.authorization-mismatch.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-response-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.response.signed.json
PROJECTION_AUTHORIZATION_MISMATCH
RUNTIME_ADMISSION_RECORD_VERIFIED sha256:adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/runtime-admission-records-portable-test/runtime-admission-adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3.json
SIGNED_OPERATION_INTENT_VALID admission-chain-subject-key admission-chain-intent-001 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/operation-intent.valid.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-subject-key admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.memory-authorization.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-projection-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.projection.scope-mismatch.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-response-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.response.signed.json
PROJECTION_SCOPE_COMMITMENT_MISMATCH
RUNTIME_ADMISSION_RECORD_VERIFIED sha256:adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/runtime-admission-records-portable-test/runtime-admission-adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3.json
SIGNED_OPERATION_INTENT_VALID admission-chain-subject-key admission-chain-intent-001 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/operation-intent.valid.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-subject-key admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.memory-authorization.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-projection-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.projection.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-response-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.response.projection-mismatch.signed.json
RESPONSE_PROJECTION_MISMATCH
RUNTIME_ADMISSION_RECORD_VERIFIED sha256:adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/runtime-admission-records-portable-test/runtime-admission-adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3.json
SIGNED_OPERATION_INTENT_VALID admission-chain-subject-key admission-chain-intent-001 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/operation-intent.valid.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-subject-key admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.memory-authorization.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-projection-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.projection.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-response-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.response.provenance-mismatch.signed.json
RESPONSE_PROVENANCE_MISMATCH
RUNTIME_ADMISSION_RECORD_VERIFIED sha256:adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/runtime-admission-records-portable-test/runtime-admission-adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3.json
SIGNED_OPERATION_INTENT_VALID admission-chain-subject-key admission-chain-intent-001 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/operation-intent.valid.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.intent-id-mismatch.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-subject-key admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.memory-authorization.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-projection-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.projection.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-response-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.response.signed.json
INTENT_PDR_ID_MISMATCH
RUNTIME_ADMISSION_RECORD_VERIFIED sha256:adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/runtime-admission-records-portable-test/runtime-admission-adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3.json
SIGNED_OPERATION_INTENT_VALID admission-chain-subject-key admission-chain-intent-001 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/operation-intent.valid.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.adapter-mismatch.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-subject-key admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.memory-authorization.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-projection-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.projection.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-response-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.response.signed.json
INTENT_PDR_ADAPTER_MISMATCH
RUNTIME_ADMISSION_RECORD_VERIFIED sha256:adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/runtime-admission-records-portable-test/runtime-admission-adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3.json
SIGNED_OPERATION_INTENT_VALID admission-chain-subject-key admission-chain-intent-001 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/operation-intent.valid.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.projection-commitment-mismatch.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-subject-key admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.memory-authorization.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-projection-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.projection.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-response-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.response.signed.json
INTENT_PROJECTION_COMMITMENT_MISMATCH
RECEIPT_CHAIN_RULES_VALID admission-chain-pdr-001
RECEIPT_CHAIN_RULES_REJECTED PROJECTION_POLICY_DECISION_MISMATCH
RECEIPT_CHAIN_RULES_REJECTED PROJECTION_AUTHORIZATION_MISMATCH
RECEIPT_CHAIN_RULES_REJECTED PROJECTION_SCOPE_COMMITMENT_MISMATCH
RECEIPT_CHAIN_RULES_REJECTED RESPONSE_PROJECTION_MISMATCH
RECEIPT_CHAIN_RULES_REJECTED RESPONSE_PROVENANCE_MISMATCH
test_context_digest_changes_when_a_bound_field_changes (__main__.DurableLedgerContractTests.test_context_digest_changes_when_a_bound_field_changes) ... ok
test_context_digest_is_stable_for_identical_context (__main__.DurableLedgerContractTests.test_context_digest_is_stable_for_identical_context) ... ok
test_context_is_immutable (__main__.DurableLedgerContractTests.test_context_is_immutable) ... ok
test_context_requires_every_bound_field (__main__.DurableLedgerContractTests.test_context_requires_every_bound_field) ... ok
test_event_requires_matching_intent_context (__main__.DurableLedgerContractTests.test_event_requires_matching_intent_context) ... ok
test_event_requires_positive_sequence (__main__.DurableLedgerContractTests.test_event_requires_positive_sequence) ... ok
test_head_requires_sha256_context_digest (__main__.DurableLedgerContractTests.test_head_requires_sha256_context_digest) ... ok
test_interface_is_abstract (__main__.DurableLedgerContractTests.test_interface_is_abstract) ... ok
test_reservation_requires_positive_sequence (__main__.DurableLedgerContractTests.test_reservation_requires_positive_sequence) ... ok
test_state_machine_vocabulary_is_contract_complete (__main__.DurableLedgerContractTests.test_state_machine_vocabulary_is_contract_complete) ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.000s

OK
test_sqlite_audit_sequence_monotonic (__main__.SQLiteDurableLedgerTests.test_sqlite_audit_sequence_monotonic) ... ok
test_sqlite_changed_context_preserves_consumed (__main__.SQLiteDurableLedgerTests.test_sqlite_changed_context_preserves_consumed) ... ok
test_sqlite_identical_retry_is_idempotent (__main__.SQLiteDurableLedgerTests.test_sqlite_identical_retry_is_idempotent) ... ok
test_sqlite_independent_connections_create_one_consumption_event (__main__.SQLiteDurableLedgerTests.test_sqlite_independent_connections_create_one_consumption_event) ... ok
test_sqlite_nonce_reuse_across_intents_is_rejected (__main__.SQLiteDurableLedgerTests.test_sqlite_nonce_reuse_across_intents_is_rejected) ... ok
test_sqlite_reserved_intent_cannot_duplicate_after_restart (__main__.SQLiteDurableLedgerTests.test_sqlite_reserved_intent_cannot_duplicate_after_restart) ... ok
test_sqlite_restart_preserves_consumption (__main__.SQLiteDurableLedgerTests.test_sqlite_restart_preserves_consumption) ... ok
test_sqlite_single_consume (__main__.SQLiteDurableLedgerTests.test_sqlite_single_consume) ... ok

----------------------------------------------------------------------
Ran 8 tests in 1.170s

OK
test_broken_receipt_chain_artifact_never_calls_ledger (__main__.AuthorityAdmissionTests.test_broken_receipt_chain_artifact_never_calls_ledger) ... ok
test_changed_projection_commitment_never_calls_ledger (__main__.AuthorityAdmissionTests.test_changed_projection_commitment_never_calls_ledger) ... ok
test_changed_scope_commitment_never_calls_ledger (__main__.AuthorityAdmissionTests.test_changed_scope_commitment_never_calls_ledger) ... ok
test_expired_receipt_never_calls_ledger (__main__.AuthorityAdmissionTests.test_expired_receipt_never_calls_ledger) ... ok
test_invalid_intent_signature_never_calls_ledger (__main__.AuthorityAdmissionTests.test_invalid_intent_signature_never_calls_ledger) ... ok
test_missing_receipt_artifact_never_calls_ledger (__main__.AuthorityAdmissionTests.test_missing_receipt_artifact_never_calls_ledger) ... ok
test_missing_required_receipt_field_never_calls_ledger (__main__.AuthorityAdmissionTests.test_missing_required_receipt_field_never_calls_ledger) ... ok
test_valid_admission_preserves_ledger_idempotent_reservation (__main__.AuthorityAdmissionTests.test_valid_admission_preserves_ledger_idempotent_reservation) ... ok
test_valid_receipt_constructs_context_and_reaches_ledger (__main__.AuthorityAdmissionTests.test_valid_receipt_constructs_context_and_reaches_ledger) ... ok
test_wrong_runtime_identity_never_calls_ledger (__main__.AuthorityAdmissionTests.test_wrong_runtime_identity_never_calls_ledger) ... ok
test_wrong_subject_never_calls_ledger (__main__.AuthorityAdmissionTests.test_wrong_subject_never_calls_ledger) ... ok

----------------------------------------------------------------------
Ran 11 tests in 7.435s

OK
MOUNTAINSHARES_TRUST_CI_GATE_VALID
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-trust-integration$ test -z "$(
  git diff --name-only -- \
    "$ROOT/durable_ledger/authority_admission.py" \
    "$ROOT/durable_ledger/interface.py" \
    "$ROOT/durable_ledger/models.py" \
    "$ROOT/durable_ledger/sqlite_backend.py" \
    "$ROOT/run_trust_build_gate.sh"
)"
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-trust-integration$ git add \
  "$ROOT/test_authority_admission.py" \
  "$ROOT/SCHEMA_BASELINE.sha256" \
  "$ROOT/TRUST_BUILD_BASELINE.sha256"
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-trust-integration$ git diff --cached --check
git diff --cached
diff --git a/schemas/mountainshares-trust-receipts/v1/TRUST_BUILD_BASELINE.sha256 b/schemas/mountainshares-trust-receipts/v1/TRUST_BUILD_BASELINE.sha256
index 203ee45..d301646 100644
--- a/schemas/mountainshares-trust-receipts/v1/TRUST_BUILD_BASELINE.sha256
+++ b/schemas/mountainshares-trust-receipts/v1/TRUST_BUILD_BASELINE.sha256
@@ -23,7 +23,7 @@ a465eca17a8b85d03ce2172a2ecc7eabc5eaed524271996872a68f9a55910221  schemas/mounta
 43b1be3be963197b6afd616908fd2e2d651bc6e6e74c353635a4e79a27d2f079  schemas/mountainshares-trust-receipts/v1/runtime-authority-manifest.schema.json
 2e004e12585c51991707febe939551ece6b08a5f773e4e3c786d1dbb058e1b8a  schemas/mountainshares-trust-receipts/v1/runtime_manifest_crypto.py
 228f38cd59d96d3131c14a51f985fc39f96a0dbad41fc467f8a332d618e31d53  schemas/mountainshares-trust-receipts/v1/signed-operation-intent.schema.json
-1c3b413949efca5b05a9bc82d279ba150933e4c8e712e2844dec24ac4a089f54  schemas/mountainshares-trust-receipts/v1/test_authority_admission.py
+dcbf52626a223083798f50a5c87f9822daaf5b6391bcf8a5e65896f990610d1b  schemas/mountainshares-trust-receipts/v1/test_authority_admission.py
 cc714d16b09ab36f274d1b2d98ce0bd104fea3380a2349a064aa056bb5e6db6d  schemas/mountainshares-trust-receipts/v1/test_durable_ledger.py
 427b32155448c35f1f4efb55368109d2c8e230b0e8b6fadd29eea8886b49692a  schemas/mountainshares-trust-receipts/v1/test_durable_ledger_sqlite.py
 0274a9c527f3f5b96843efc26ec1c0e16e98f48ecee3e02e38b8d2779841e624  schemas/mountainshares-trust-receipts/v1/test_intent_consumption.py
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-trust-integration$ git commit -m "test(trust): expand authority admission denial matrix"
[stage-6.4 0bfc4d8] test(trust): expand authority admission denial matrix
 2 files changed, 98 insertions(+), 1 deletion(-)
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-trust-integration$ "$ROOT/run_trust_build_gate.sh"
TRUST_SCHEMAS_META_VALID
schemas/mountainshares-trust-receipts/v1/memory-authorization-receipt.schema.json: OK
schemas/mountainshares-trust-receipts/v1/policy-decision-receipt.schema.json: OK
schemas/mountainshares-trust-receipts/v1/projection-receipt.schema.json: OK
schemas/mountainshares-trust-receipts/v1/response-receipt.schema.json: OK
schemas/mountainshares-trust-receipts/v1/runtime-admission-record.schema.json: OK
schemas/mountainshares-trust-receipts/v1/runtime-authority-manifest.schema.json: OK
schemas/mountainshares-trust-receipts/v1/signed-operation-intent.schema.json: OK
schemas/mountainshares-trust-receipts/v1/admit_runtime_authority_manifest.py: OK
schemas/mountainshares-trust-receipts/v1/durable_ledger/__init__.py: OK
schemas/mountainshares-trust-receipts/v1/durable_ledger/authority_admission.py: OK
schemas/mountainshares-trust-receipts/v1/durable_ledger/errors.py: OK
schemas/mountainshares-trust-receipts/v1/durable_ledger/interface.py: OK
schemas/mountainshares-trust-receipts/v1/durable_ledger/models.py: OK
schemas/mountainshares-trust-receipts/v1/durable_ledger/sqlite_backend.py: OK
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py: OK
schemas/mountainshares-trust-receipts/v1/intent_consumption_ledger.py: OK
schemas/mountainshares-trust-receipts/v1/memory-authorization-receipt.schema.json: OK
schemas/mountainshares-trust-receipts/v1/memory_authorization_gate.py: OK
schemas/mountainshares-trust-receipts/v1/operation_intent_consumption.py: OK
schemas/mountainshares-trust-receipts/v1/operation_intent_rules.py: OK
schemas/mountainshares-trust-receipts/v1/policy-decision-receipt.schema.json: OK
schemas/mountainshares-trust-receipts/v1/projection-receipt.schema.json: OK
schemas/mountainshares-trust-receipts/v1/receipt_chain_errors.py: OK
schemas/mountainshares-trust-receipts/v1/receipt_chain_rules.py: OK
schemas/mountainshares-trust-receipts/v1/receipt_crypto.py: OK
schemas/mountainshares-trust-receipts/v1/receipt_rules.py: OK
schemas/mountainshares-trust-receipts/v1/response-receipt.schema.json: OK
schemas/mountainshares-trust-receipts/v1/run_trust_build_gate.sh: OK
schemas/mountainshares-trust-receipts/v1/runtime-admission-record.schema.json: OK
schemas/mountainshares-trust-receipts/v1/runtime-authority-manifest.schema.json: OK
schemas/mountainshares-trust-receipts/v1/runtime_manifest_crypto.py: OK
schemas/mountainshares-trust-receipts/v1/signed-operation-intent.schema.json: OK
schemas/mountainshares-trust-receipts/v1/test_authority_admission.py: OK
schemas/mountainshares-trust-receipts/v1/test_durable_ledger.py: OK
schemas/mountainshares-trust-receipts/v1/test_durable_ledger_sqlite.py: OK
schemas/mountainshares-trust-receipts/v1/test_intent_consumption.py: OK
schemas/mountainshares-trust-receipts/v1/test_receipt_chain_rules.py: OK
schemas/mountainshares-trust-receipts/v1/usage_ledger.py: OK
schemas/mountainshares-trust-receipts/v1/validate_receipt.py: OK
schemas/mountainshares-trust-receipts/v1/verify_admission_linked_receipt_chain.py: OK
schemas/mountainshares-trust-receipts/v1/verify_memory_authorization_receipt.py: OK
schemas/mountainshares-trust-receipts/v1/verify_policy_decision_receipt.py: OK
schemas/mountainshares-trust-receipts/v1/verify_projection_receipt.py: OK
schemas/mountainshares-trust-receipts/v1/verify_response_receipt.py: OK
schemas/mountainshares-trust-receipts/v1/verify_runtime_admission_record.py: OK
schemas/mountainshares-trust-receipts/v1/verify_runtime_authority_manifest.py: OK
schemas/mountainshares-trust-receipts/v1/verify_runtime_governance_policy.py: OK
schemas/mountainshares-trust-receipts/v1/verify_runtime_image_binding.py: OK
schemas/mountainshares-trust-receipts/v1/verify_signed_operation_intent.py: OK
RUNTIME_ADMISSION_RECORD_VERIFIED sha256:adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/runtime-admission-records-portable-test/runtime-admission-adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3.json
SIGNED_OPERATION_INTENT_VALID admission-chain-subject-key admission-chain-intent-001 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/operation-intent.valid.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-subject-key admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.memory-authorization.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-projection-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.projection.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-response-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.response.signed.json
ADMISSION_LINKED_RECEIPT_CHAIN_VALID sha256:adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3 admission-chain-pdr-001 admission-chain-mar-001 admission-chain-projection-001 admission-chain-response-001
SIGNED_OPERATION_INTENT_VALID admission-chain-subject-key admission-chain-intent-001 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/operation-intent.valid.signed.json
SIGNED_OPERATION_INTENT_INVALID INVALID_RECEIPT_LIFETIME
SIGNED_OPERATION_INTENT_INVALID UNTRUSTED_SUBJECT_KEY_ID admission-chain-unknown-subject-key
SIGNED_OPERATION_INTENT_INVALID INVALID_SIGNATURE
INTENT_CONSUMPTION_VALID admission-chain-subject-key admission-chain-intent-001
INTENT_REPLAY_REJECTED admission-chain-intent-001
INTENT_CONTEXT_MISMATCH_REJECTED admission-chain-intent-001
INTENT_NONCE_REPLAY_REJECTED admission-chain-intent-nonce-replay-001
INTENT_EXPIRED_AFTER_CONSUMPTION_REJECTED
INTENT_CONSUMED_STATE_PRESERVED_AFTER_EXPIRY
RUNTIME_ADMISSION_RECORD_VERIFIED sha256:adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/runtime-admission-records-portable-test/runtime-admission-adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3.json
SIGNED_OPERATION_INTENT_VALID admission-chain-subject-key admission-chain-intent-001 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/operation-intent.valid.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-subject-key admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.memory-authorization.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-projection-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.projection.policy-decision-mismatch.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-response-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.response.signed.json
PROJECTION_POLICY_DECISION_MISMATCH
RUNTIME_ADMISSION_RECORD_VERIFIED sha256:adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/runtime-admission-records-portable-test/runtime-admission-adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3.json
SIGNED_OPERATION_INTENT_VALID admission-chain-subject-key admission-chain-intent-001 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/operation-intent.valid.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-subject-key admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.memory-authorization.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-projection-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.projection.authorization-mismatch.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-response-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.response.signed.json
PROJECTION_AUTHORIZATION_MISMATCH
RUNTIME_ADMISSION_RECORD_VERIFIED sha256:adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/runtime-admission-records-portable-test/runtime-admission-adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3.json
SIGNED_OPERATION_INTENT_VALID admission-chain-subject-key admission-chain-intent-001 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/operation-intent.valid.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-subject-key admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.memory-authorization.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-projection-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.projection.scope-mismatch.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-response-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.response.signed.json
PROJECTION_SCOPE_COMMITMENT_MISMATCH
RUNTIME_ADMISSION_RECORD_VERIFIED sha256:adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/runtime-admission-records-portable-test/runtime-admission-adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3.json
SIGNED_OPERATION_INTENT_VALID admission-chain-subject-key admission-chain-intent-001 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/operation-intent.valid.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-subject-key admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.memory-authorization.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-projection-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.projection.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-response-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.response.projection-mismatch.signed.json
RESPONSE_PROJECTION_MISMATCH
RUNTIME_ADMISSION_RECORD_VERIFIED sha256:adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/runtime-admission-records-portable-test/runtime-admission-adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3.json
SIGNED_OPERATION_INTENT_VALID admission-chain-subject-key admission-chain-intent-001 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/operation-intent.valid.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-subject-key admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.memory-authorization.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-projection-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.projection.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-response-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.response.provenance-mismatch.signed.json
RESPONSE_PROVENANCE_MISMATCH
RUNTIME_ADMISSION_RECORD_VERIFIED sha256:adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/runtime-admission-records-portable-test/runtime-admission-adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3.json
SIGNED_OPERATION_INTENT_VALID admission-chain-subject-key admission-chain-intent-001 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/operation-intent.valid.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.intent-id-mismatch.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-subject-key admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.memory-authorization.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-projection-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.projection.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-response-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.response.signed.json
INTENT_PDR_ID_MISMATCH
RUNTIME_ADMISSION_RECORD_VERIFIED sha256:adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/runtime-admission-records-portable-test/runtime-admission-adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3.json
SIGNED_OPERATION_INTENT_VALID admission-chain-subject-key admission-chain-intent-001 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/operation-intent.valid.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.adapter-mismatch.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-subject-key admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.memory-authorization.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-projection-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.projection.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-response-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.response.signed.json
INTENT_PDR_ADAPTER_MISMATCH
RUNTIME_ADMISSION_RECORD_VERIFIED sha256:adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/runtime-admission-records-portable-test/runtime-admission-adca06dc524dda9045fc908a7a9aae36a475d8c99fac4a2ba29fe432bc5b48f3.json
SIGNED_OPERATION_INTENT_VALID admission-chain-subject-key admission-chain-intent-001 /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/operation-intent.valid.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.projection-commitment-mismatch.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-subject-key admission-chain-guardian-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.memory-authorization.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-projection-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.projection.signed.json
STRUCTURAL_AND_CRYPTOGRAPHIC_VALID admission-chain-response-key /home/cakidd/msjarvis-trust-integration/schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.response.signed.json
INTENT_PROJECTION_COMMITMENT_MISMATCH
RECEIPT_CHAIN_RULES_VALID admission-chain-pdr-001
RECEIPT_CHAIN_RULES_REJECTED PROJECTION_POLICY_DECISION_MISMATCH
RECEIPT_CHAIN_RULES_REJECTED PROJECTION_AUTHORIZATION_MISMATCH
RECEIPT_CHAIN_RULES_REJECTED PROJECTION_SCOPE_COMMITMENT_MISMATCH
RECEIPT_CHAIN_RULES_REJECTED RESPONSE_PROJECTION_MISMATCH
RECEIPT_CHAIN_RULES_REJECTED RESPONSE_PROVENANCE_MISMATCH
test_context_digest_changes_when_a_bound_field_changes (__main__.DurableLedgerContractTests.test_context_digest_changes_when_a_bound_field_changes) ... ok
test_context_digest_is_stable_for_identical_context (__main__.DurableLedgerContractTests.test_context_digest_is_stable_for_identical_context) ... ok
test_context_is_immutable (__main__.DurableLedgerContractTests.test_context_is_immutable) ... ok
test_context_requires_every_bound_field (__main__.DurableLedgerContractTests.test_context_requires_every_bound_field) ... ok
test_event_requires_matching_intent_context (__main__.DurableLedgerContractTests.test_event_requires_matching_intent_context) ... ok
test_event_requires_positive_sequence (__main__.DurableLedgerContractTests.test_event_requires_positive_sequence) ... ok
test_head_requires_sha256_context_digest (__main__.DurableLedgerContractTests.test_head_requires_sha256_context_digest) ... ok
test_interface_is_abstract (__main__.DurableLedgerContractTests.test_interface_is_abstract) ... ok
test_reservation_requires_positive_sequence (__main__.DurableLedgerContractTests.test_reservation_requires_positive_sequence) ... ok
test_state_machine_vocabulary_is_contract_complete (__main__.DurableLedgerContractTests.test_state_machine_vocabulary_is_contract_complete) ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.001s

OK
test_sqlite_audit_sequence_monotonic (__main__.SQLiteDurableLedgerTests.test_sqlite_audit_sequence_monotonic) ... ok
test_sqlite_changed_context_preserves_consumed (__main__.SQLiteDurableLedgerTests.test_sqlite_changed_context_preserves_consumed) ... ok
test_sqlite_identical_retry_is_idempotent (__main__.SQLiteDurableLedgerTests.test_sqlite_identical_retry_is_idempotent) ... ok
test_sqlite_independent_connections_create_one_consumption_event (__main__.SQLiteDurableLedgerTests.test_sqlite_independent_connections_create_one_consumption_event) ... ok
test_sqlite_nonce_reuse_across_intents_is_rejected (__main__.SQLiteDurableLedgerTests.test_sqlite_nonce_reuse_across_intents_is_rejected) ... ok
test_sqlite_reserved_intent_cannot_duplicate_after_restart (__main__.SQLiteDurableLedgerTests.test_sqlite_reserved_intent_cannot_duplicate_after_restart) ... ok
test_sqlite_restart_preserves_consumption (__main__.SQLiteDurableLedgerTests.test_sqlite_restart_preserves_consumption) ... ok
test_sqlite_single_consume (__main__.SQLiteDurableLedgerTests.test_sqlite_single_consume) ... ok

----------------------------------------------------------------------
Ran 8 tests in 1.132s

OK
test_broken_receipt_chain_artifact_never_calls_ledger (__main__.AuthorityAdmissionTests.test_broken_receipt_chain_artifact_never_calls_ledger) ... ok
test_changed_projection_commitment_never_calls_ledger (__main__.AuthorityAdmissionTests.test_changed_projection_commitment_never_calls_ledger) ... ok
test_changed_scope_commitment_never_calls_ledger (__main__.AuthorityAdmissionTests.test_changed_scope_commitment_never_calls_ledger) ... ok
test_expired_receipt_never_calls_ledger (__main__.AuthorityAdmissionTests.test_expired_receipt_never_calls_ledger) ... ok
test_invalid_intent_signature_never_calls_ledger (__main__.AuthorityAdmissionTests.test_invalid_intent_signature_never_calls_ledger) ... ok
test_missing_receipt_artifact_never_calls_ledger (__main__.AuthorityAdmissionTests.test_missing_receipt_artifact_never_calls_ledger) ... ok
test_missing_required_receipt_field_never_calls_ledger (__main__.AuthorityAdmissionTests.test_missing_required_receipt_field_never_calls_ledger) ... ok
test_valid_admission_preserves_ledger_idempotent_reservation (__main__.AuthorityAdmissionTests.test_valid_admission_preserves_ledger_idempotent_reservation) ... ok
test_valid_receipt_constructs_context_and_reaches_ledger (__main__.AuthorityAdmissionTests.test_valid_receipt_constructs_context_and_reaches_ledger) ... ok
test_wrong_runtime_identity_never_calls_ledger (__main__.AuthorityAdmissionTests.test_wrong_runtime_identity_never_calls_ledger) ... ok
test_wrong_subject_never_calls_ledger (__main__.AuthorityAdmissionTests.test_wrong_subject_never_calls_ledger) ... ok

----------------------------------------------------------------------
Ran 11 tests in 7.291s

OK
MOUNTAINSHARES_TRUST_CI_GATE_VALID
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-trust-integration$ git status --short
git log --decorate --oneline -5
git show --stat --oneline HEAD
0bfc4d8 (HEAD -> stage-6.4) test(trust): expand authority admission denial matrix
de78155 feat(trust): enforce receipt scope verification boundary
243adcd chore(trust): establish stage 6.4 development boundary
0dab4a4 (tag: trust-ledger-sqlite-stage-6-3-0dab4a479175, guardian-admission-integration) feat(trust): add sqlite durable ledger reference backend
694b3ea feat(trust): add sqlite durable ledger reference backend
0bfc4d8 (HEAD -> stage-6.4) test(trust): expand authority admission denial matrix
 .../v1/TRUST_BUILD_BASELINE.sha256                 |  2 +-
 .../v1/test_authority_admission.py                 | 97 ++++++++++++++++++++++
 2 files changed, 98 insertions(+), 1 deletion(-)
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-trust-integration$ 

