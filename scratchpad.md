gS(e,t,us)}function ND(e,t){return gS(e,t,yS)}function OD(e,t,r){if(e.charCodeAt(t+1)===47&&t+2<r&&e.charCodeAt(t+2)===47){let s=e.substring(t,r);return!!(b2.test(s)||T2.test(s)||i8.test(s)||a8.test(s))}return!1}function vS(e,t){return e.charCodeAt(t+1)===42&&e.charCodeAt(t+2)===33}function MD(e,t){let r=new Map(t.map(w=>[`${Ls(e,w.range.end).line}`,w])),s=new Map;return{getUnusedExpectations:f,markUsed:x};function f(){return Za(r.entries()).filter(w=>{let[A,g]=w;return g.type===0&&!s.get(A)}).map(w=>{let[A,g]=w;return g})}function x(w){return r.has(`${w}`)?(s.set(`${w}`,!0),!0):!1}}function Io(e,t,r){return va(e)?e.pos:Uy(e)||e.kind===11?Ar((t||Si(e)).text,e.pos,!1,!0):r&&ya(e)?Io(e.jsDoc[0],t):e.kind===354&&e._children.length>0?Io(e._children[0],t,r):Ar((t||Si(e)).text,e.pos,!1,!1,qS(e))}function LD(e,t){let r=!va(e)&&fc(e)?te(e.modifiers,zl):void 0;return r?Ar((t||Si(e)).text,r.end):Io(e,t)}function No(e,t){let r=arguments.length>2&&arguments[2]!==void 0?arguments[2]:!1;return B_(e.text,t,r)}function RD(e){return!!zi(e,lE)}function bS(e){return!!(cc(e)&&e.exportClause&&ld(e.exportClause)&&e.exportClause.name.escapedText==="default")}function B_(e,t){let r=arguments.length>2&&arguments[2]!==void 0?arguments[2]:!1;if(va(t))return"";let s=e.substring(r?t.pos:Ar(e,t.pos),t.end);return RD(t)&&(s=s.split(/\r\n|\n|\r/).map(f=>nl(f.replace(/^\s*\*/,""))).join(`
schemas/mountainshares-trust-receipts/v1/SCHEMA_BASELINE.sha256:1:a240ed842c341615d73db9e786dbb70778022169b11f7dbcd6a8d03ffc780bf0  schemas/mountainshares-trust-receipts/v1/memory-authorization-receipt.schema.json
schemas/mountainshares-trust-receipts/v1/SCHEMA_BASELINE.sha256:2:bac25e507208be5eb18f19792c452d93fc786aff258047f494e83de17f7552db  schemas/mountainshares-trust-receipts/v1/policy-decision-receipt.schema.json
schemas/mountainshares-trust-receipts/v1/TRUST_BUILD_BASELINE.sha256:9:a240ed842c341615d73db9e786dbb70778022169b11f7dbcd6a8d03ffc780bf0  schemas/mountainshares-trust-receipts/v1/memory-authorization-receipt.schema.json
schemas/mountainshares-trust-receipts/v1/TRUST_BUILD_BASELINE.sha256:10:07d4100af18452d797c987172ff5d8bd579b57cf7ad5e739e403d03e83433381  schemas/mountainshares-trust-receipts/v1/memory_authorization_gate.py
schemas/mountainshares-trust-receipts/v1/TRUST_BUILD_BASELINE.sha256:13:bac25e507208be5eb18f19792c452d93fc786aff258047f494e83de17f7552db  schemas/mountainshares-trust-receipts/v1/policy-decision-receipt.schema.json
schemas/mountainshares-trust-receipts/v1/TRUST_BUILD_BASELINE.sha256:17:4e1233804d735bdaa0057db54f3c7d721510482fcc15488da881e86134676411  schemas/mountainshares-trust-receipts/v1/receipt_crypto.py
schemas/mountainshares-trust-receipts/v1/TRUST_BUILD_BASELINE.sha256:39:e325f5d308144684eefcfb262ba29eca42d629fe9ee1a1dc2fe183e16d17e3b5  schemas/mountainshares-trust-receipts/v1/verify_memory_authorization_receipt.py
schemas/mountainshares-trust-receipts/v1/TRUST_BUILD_BASELINE.sha256:40:43ba65b24edec0bfbe8b2b7328ac483e8e8d4c336881869adea17318a4bc2274  schemas/mountainshares-trust-receipts/v1/verify_policy_decision_receipt.py
schemas/mountainshares-trust-receipts/v1/durable_ledger/models.py:23:    subject_signature_key_id: str
schemas/mountainshares-trust-receipts/v1/durable_ledger/models.py:30:    policy_decision_id: str
schemas/mountainshares-trust-receipts/v1/durable_ledger/sqlite_backend.py:34:    subject_signature_key_id TEXT NOT NULL,
schemas/mountainshares-trust-receipts/v1/durable_ledger/sqlite_backend.py:53:    subject_signature_key_id TEXT NOT NULL,
schemas/mountainshares-trust-receipts/v1/durable_ledger/sqlite_backend.py:67:ON intent_heads(subject_signature_key_id, nonce);
schemas/mountainshares-trust-receipts/v1/durable_ledger/sqlite_backend.py:183:                subject_signature_key_id,
schemas/mountainshares-trust-receipts/v1/durable_ledger/sqlite_backend.py:209:                context.subject_signature_key_id,
schemas/mountainshares-trust-receipts/v1/durable_ledger/sqlite_backend.py:242:            WHERE subject_signature_key_id = ?
schemas/mountainshares-trust-receipts/v1/durable_ledger/sqlite_backend.py:245:            (context.subject_signature_key_id, context.nonce),
schemas/mountainshares-trust-receipts/v1/durable_ledger/sqlite_backend.py:328:                    subject_signature_key_id,
schemas/mountainshares-trust-receipts/v1/durable_ledger/sqlite_backend.py:340:                    context.subject_signature_key_id,
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.memory-authorization.signed.json:8:  "guardian_attestation": {
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.memory-authorization.signed.json:9:    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.memory-authorization.signed.json:16:  "policy_decision_id": "admission-chain-pdr-001",
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.memory-authorization.signed.json:20:  "receipt_id": "admission-chain-mar-001",
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.memory-authorization.signed.json:23:  "subject_signature": {
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.memory-authorization.signed.json:24:    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.memory-authorization.signed.json:28:  "type": "mountainshares.memory-authorization-receipt/v1",
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.adapter-mismatch.signed.json:12:  "decision_id": "admission-chain-pdr-001",
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.adapter-mismatch.signed.json:16:  "guardian_signature": {
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.adapter-mismatch.signed.json:17:    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.adapter-mismatch.signed.json:30:  "type": "mountainshares.policy-decision-receipt/v1"
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.intent-id-mismatch.signed.json:12:  "decision_id": "admission-chain-pdr-001",
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.intent-id-mismatch.signed.json:16:  "guardian_signature": {
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.intent-id-mismatch.signed.json:17:    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.intent-id-mismatch.signed.json:30:  "type": "mountainshares.policy-decision-receipt/v1"
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.projection-commitment-mismatch.signed.json:12:  "decision_id": "admission-chain-pdr-001",
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.projection-commitment-mismatch.signed.json:16:  "guardian_signature": {
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.projection-commitment-mismatch.signed.json:17:    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.projection-commitment-mismatch.signed.json:30:  "type": "mountainshares.policy-decision-receipt/v1"
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.signed.json:12:  "decision_id": "admission-chain-pdr-001",
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.signed.json:16:  "guardian_signature": {
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.signed.json:17:    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.signed.json:30:  "type": "mountainshares.policy-decision-receipt/v1"
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.projection.authorization-mismatch.signed.json:7:  "policy_decision_id": "admission-chain-pdr-001",
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.projection.authorization-mismatch.signed.json:13:    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.projection.policy-decision-mismatch.signed.json:7:  "policy_decision_id": "admission-chain-pdr-mismatch-001",
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.projection.policy-decision-mismatch.signed.json:13:    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.projection.scope-mismatch.signed.json:7:  "policy_decision_id": "admission-chain-pdr-001",
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.projection.scope-mismatch.signed.json:13:    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.projection.signed.json:7:  "policy_decision_id": "admission-chain-pdr-001",
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.projection.signed.json:13:    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.response.projection-mismatch.signed.json:9:    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.response.provenance-mismatch.signed.json:9:    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.response.signed.json:9:    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/memory-authorization.signed.json:7:  "guardian_attestation": {
schemas/mountainshares-trust-receipts/v1/fixtures/memory-authorization.signed.json:8:    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/memory-authorization.signed.json:15:  "policy_decision_id": "pdr-allow-001",
schemas/mountainshares-trust-receipts/v1/fixtures/memory-authorization.signed.json:19:  "receipt_id": "signed-mar-001",
schemas/mountainshares-trust-receipts/v1/fixtures/memory-authorization.signed.json:22:  "subject_signature": {
schemas/mountainshares-trust-receipts/v1/fixtures/memory-authorization.signed.json:23:    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/memory-authorization.signed.json:27:  "type": "mountainshares.memory-authorization-receipt/v1",
schemas/mountainshares-trust-receipts/v1/fixtures/memory-authorization.signed.tampered.json:7:  "guardian_attestation": {
schemas/mountainshares-trust-receipts/v1/fixtures/memory-authorization.signed.tampered.json:8:    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/memory-authorization.signed.tampered.json:15:  "policy_decision_id": "pdr-allow-001",
schemas/mountainshares-trust-receipts/v1/fixtures/memory-authorization.signed.tampered.json:19:  "receipt_id": "signed-mar-001",
schemas/mountainshares-trust-receipts/v1/fixtures/memory-authorization.signed.tampered.json:22:  "subject_signature": {
schemas/mountainshares-trust-receipts/v1/fixtures/memory-authorization.signed.tampered.json:23:    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/memory-authorization.signed.tampered.json:27:  "type": "mountainshares.memory-authorization-receipt/v1",
schemas/mountainshares-trust-receipts/v1/fixtures/operation-intent.expired.signed.json:13:  "subject_signature": {
schemas/mountainshares-trust-receipts/v1/fixtures/operation-intent.expired.signed.json:14:    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/operation-intent.signed.tampered.json:13:  "subject_signature": {
schemas/mountainshares-trust-receipts/v1/fixtures/operation-intent.signed.tampered.json:14:    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/operation-intent.untrusted-key.json:13:  "subject_signature": {
schemas/mountainshares-trust-receipts/v1/fixtures/operation-intent.untrusted-key.json:14:    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/operation-intent.valid.signed.json:13:  "subject_signature": {
schemas/mountainshares-trust-receipts/v1/fixtures/operation-intent.valid.signed.json:14:    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.expired.json:9:  "decision_id": "signed-fixture-pdr-001",
schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.expired.json:13:  "guardian_signature": {
schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.expired.json:14:    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.expired.json:26:  "type": "mountainshares.policy-decision-receipt/v1"
schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.invalid-lifetime.json:9:  "decision_id": "signed-fixture-pdr-001",
schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.invalid-lifetime.json:13:  "guardian_signature": {
schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.invalid-lifetime.json:14:    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.invalid-lifetime.json:26:  "type": "mountainshares.policy-decision-receipt/v1"
schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.missing-constraints.json:3:  "decision_id": "fixture-pdr-allow-001",
schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.missing-constraints.json:7:  "guardian_signature": {
schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.missing-constraints.json:8:    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.missing-constraints.json:20:  "type": "mountainshares.policy-decision-receipt/v1"
schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.signed.json:9:  "decision_id": "signed-fixture-pdr-001",
schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.signed.json:13:  "guardian_signature": {
schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.signed.json:14:    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.signed.json:26:  "type": "mountainshares.policy-decision-receipt/v1"
schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.signed.tampered.json:9:  "decision_id": "signed-fixture-pdr-001",
schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.signed.tampered.json:13:  "guardian_signature": {
schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.signed.tampered.json:14:    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.signed.tampered.json:26:  "type": "mountainshares.policy-decision-receipt/v1"
schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.untrusted-key.json:9:  "decision_id": "signed-fixture-pdr-001",
schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.untrusted-key.json:13:  "guardian_signature": {
schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.untrusted-key.json:14:    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.untrusted-key.json:26:  "type": "mountainshares.policy-decision-receipt/v1"
schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.valid.json:9:  "decision_id": "fixture-pdr-allow-001",
schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.valid.json:13:  "guardian_signature": {
schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.valid.json:14:    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.valid.json:26:  "type": "mountainshares.policy-decision-receipt/v1"
schemas/mountainshares-trust-receipts/v1/fixtures/projection.signed.json:5:  "policy_decision_id": "signed-fixture-pdr-001",
schemas/mountainshares-trust-receipts/v1/fixtures/projection.signed.json:11:    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/projection.signed.tampered.json:5:  "policy_decision_id": "signed-fixture-pdr-001",
schemas/mountainshares-trust-receipts/v1/fixtures/projection.signed.tampered.json:11:    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/response.signed.json:8:    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/response.signed.tampered.json:8:    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/runtime-authority-manifest.duplicate-key.json:4:      "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/runtime-authority-manifest.duplicate-key.json:10:      "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/runtime-authority-manifest.duplicate-role.json:4:      "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/runtime-authority-manifest.duplicate-role.json:10:      "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/runtime-authority-manifest.expired.json:4:      "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/runtime-authority-manifest.expired.json:10:      "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/runtime-authority-manifest.signed.json:4:      "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/runtime-authority-manifest.signed.json:10:      "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/runtime-authority-manifest.tampered-release.json:4:      "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/fixtures/runtime-authority-manifest.tampered-release.json:10:      "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:8:from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:12:from receipt_crypto import canonical_payload
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:36:def sign(receipt, signature_field, private_key, signature_fields=None):
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:37:    payload = canonical_payload(receipt, signature_fields or signature_field)
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:39:        private_key.sign(payload)
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:43:    return Ed25519PrivateKey.from_private_bytes(
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:73:    "type": "mountainshares.policy-decision-receipt/v1",
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:78:    "decision_id": "admission-chain-pdr-001",
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:97:    "guardian_signature": {
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:98:        "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:103:sign(pdr, "guardian_signature", guardian_private)
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:107:sign(
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:109:    "guardian_signature",
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:115:sign(
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:117:    "guardian_signature",
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:125:sign(
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:127:    "guardian_signature",
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:144:    "subject_signature": {
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:145:        "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:150:sign(operation_intent, "subject_signature", subject_private)
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:154:sign(expired_operation_intent, "subject_signature", subject_private)
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:157:untrusted_operation_intent["subject_signature"]["key_id"] = (
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:165:    "type": "mountainshares.memory-authorization-receipt/v1",
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:167:    "receipt_id": "admission-chain-mar-001",
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:177:    "policy_decision_id": pdr["decision_id"],
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:181:    "subject_signature": {
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:182:        "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:186:    "guardian_attestation": {
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:187:        "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:192:sign(
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:194:    "subject_signature",
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:196:    ("subject_signature", "guardian_attestation"),
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:198:sign(
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:200:    "guardian_attestation",
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:202:    ("subject_signature", "guardian_attestation"),
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:209:    "mar_id": mar["receipt_id"],
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:210:    "policy_decision_id": pdr["decision_id"],
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:224:        "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:229:sign(projection, "projection_signature", projection_private)
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:243:        "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:248:sign(response, "response_signature", response_private)
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:250:projection_policy_decision_mismatch = json.loads(json.dumps(projection))
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:251:projection_policy_decision_mismatch["policy_decision_id"] = (
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:254:sign(
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:255:    projection_policy_decision_mismatch,
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:264:sign(
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:272:sign(
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:282:sign(
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:292:sign(
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:299:    "admission-chain.policy-decision.signed.json": pdr,
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:300:    "admission-chain.memory-authorization.signed.json": mar,
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:303:    "admission-chain.projection.policy-decision-mismatch.signed.json": projection_policy_decision_mismatch,
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:308:    "admission-chain.policy-decision.intent-id-mismatch.signed.json": pdr_intent_id_mismatch,
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:309:    "admission-chain.policy-decision.adapter-mismatch.signed.json": pdr_adapter_mismatch,
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py:310:    "admission-chain.policy-decision.projection-commitment-mismatch.signed.json": pdr_projection_commitment_mismatch,
schemas/mountainshares-trust-receipts/v1/memory-authorization-receipt.schema.json:25:    "guardian_attestation": {
schemas/mountainshares-trust-receipts/v1/memory-authorization-receipt.schema.json:60:    "policy_decision_id": {
schemas/mountainshares-trust-receipts/v1/memory-authorization-receipt.schema.json:76:    "receipt_id": {
schemas/mountainshares-trust-receipts/v1/memory-authorization-receipt.schema.json:88:    "subject_signature": {
schemas/mountainshares-trust-receipts/v1/memory-authorization-receipt.schema.json:112:      "const": "mountainshares.memory-authorization-receipt/v1"
schemas/mountainshares-trust-receipts/v1/memory-authorization-receipt.schema.json:121:    "receipt_id",
schemas/mountainshares-trust-receipts/v1/memory-authorization-receipt.schema.json:131:    "policy_decision_id",
schemas/mountainshares-trust-receipts/v1/memory-authorization-receipt.schema.json:135:    "subject_signature",
schemas/mountainshares-trust-receipts/v1/memory-authorization-receipt.schema.json:136:    "guardian_attestation"
schemas/mountainshares-trust-receipts/v1/memory_authorization_gate.py:5:from receipt_crypto import verify_ed25519
schemas/mountainshares-trust-receipts/v1/memory_authorization_gate.py:11:def verify_memory_authorization(receipt,registry):
schemas/mountainshares-trust-receipts/v1/memory_authorization_gate.py:12:    schema=json.loads((ROOT/"memory-authorization-receipt.schema.json").read_text())
schemas/mountainshares-trust-receipts/v1/memory_authorization_gate.py:17:    signature_fields=("subject_signature","guardian_attestation")
schemas/mountainshares-trust-receipts/v1/memory_authorization_gate.py:19:    for signature_field,required_role in (("subject_signature","subject"),("guardian_attestation","guardian")):
schemas/mountainshares-trust-receipts/v1/memory_authorization_gate.py:24:        verify_ed25519(receipt,signature_field,entry["public_key"],signature_fields)
schemas/mountainshares-trust-receipts/v1/memory_authorization_gate.py:29:    verified_key_ids=verify_memory_authorization(receipt,registry)
schemas/mountainshares-trust-receipts/v1/memory_authorization_gate.py:30:    uses=consume(ledger_path,receipt["receipt_id"],receipt["max_uses"])
schemas/mountainshares-trust-receipts/v1/operation_intent_rules.py:6:from receipt_crypto import verify_ed25519
schemas/mountainshares-trust-receipts/v1/operation_intent_rules.py:33:    signature = intent["subject_signature"]
schemas/mountainshares-trust-receipts/v1/operation_intent_rules.py:47:    verified_key_id = verify_ed25519(
schemas/mountainshares-trust-receipts/v1/operation_intent_rules.py:49:        "subject_signature",
schemas/mountainshares-trust-receipts/v1/policy-decision-receipt.schema.json:77:    "decision_id": {
schemas/mountainshares-trust-receipts/v1/policy-decision-receipt.schema.json:97:    "guardian_signature": {
schemas/mountainshares-trust-receipts/v1/policy-decision-receipt.schema.json:153:      "const": "mountainshares.policy-decision-receipt/v1"
schemas/mountainshares-trust-receipts/v1/policy-decision-receipt.schema.json:170:    "decision_id",
schemas/mountainshares-trust-receipts/v1/policy-decision-receipt.schema.json:183:    "guardian_signature",
schemas/mountainshares-trust-receipts/v1/projection-receipt.schema.json:21:    "policy_decision_id": {
schemas/mountainshares-trust-receipts/v1/projection-receipt.schema.json:100:    "policy_decision_id",
schemas/mountainshares-trust-receipts/v1/receipt_chain_rules.py:107:        pdr["decision_id"],
schemas/mountainshares-trust-receipts/v1/receipt_chain_rules.py:108:        mar["policy_decision_id"],
schemas/mountainshares-trust-receipts/v1/receipt_chain_rules.py:110:        "mar.policy_decision_id",
schemas/mountainshares-trust-receipts/v1/receipt_chain_rules.py:137:        mar["receipt_id"],
schemas/mountainshares-trust-receipts/v1/receipt_chain_rules.py:143:        pdr["decision_id"],
schemas/mountainshares-trust-receipts/v1/receipt_chain_rules.py:144:        projection["policy_decision_id"],
schemas/mountainshares-trust-receipts/v1/receipt_chain_rules.py:146:        "projection.policy_decision_id",
schemas/mountainshares-trust-receipts/v1/receipt_chain_rules.py:207:        "policy_decision_id": pdr["decision_id"],
schemas/mountainshares-trust-receipts/v1/receipt_chain_rules.py:208:        "memory_authorization_id": mar["receipt_id"],
schemas/mountainshares-trust-receipts/v1/receipt_crypto.py:3:from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
schemas/mountainshares-trust-receipts/v1/receipt_crypto.py:5:def canonical_payload(receipt,signature_fields):
schemas/mountainshares-trust-receipts/v1/receipt_crypto.py:17:def verify_ed25519(receipt,signature_field,public_key_b64,signature_fields=None):
schemas/mountainshares-trust-receipts/v1/receipt_crypto.py:19:    if signature_object["algorithm"]!="Ed25519":
schemas/mountainshares-trust-receipts/v1/receipt_crypto.py:24:        public_key=Ed25519PublicKey.from_public_bytes(public_key_bytes)
schemas/mountainshares-trust-receipts/v1/receipt_crypto.py:28:        public_key.verify(signature,canonical_payload(receipt,signature_fields or (signature_field,)))
schemas/mountainshares-trust-receipts/v1/run_trust_build_gate.sh:46:  'BEGIN (EC |RSA |OPENSSH |PRIVATE )?PRIVATE KEY|private_key[[:space:]]*[:=]|Ed25519PrivateKey\.from_private_bytes|Ed25519PrivateKey\.generate' \
schemas/mountainshares-trust-receipts/v1/run_trust_build_gate.sh:66:  "$ROOT/fixtures/admission-chain.policy-decision.signed.json" \
schemas/mountainshares-trust-receipts/v1/run_trust_build_gate.sh:67:  "$ROOT/fixtures/admission-chain.memory-authorization.signed.json" \
schemas/mountainshares-trust-receipts/v1/run_trust_build_gate.sh:105:    "$ROOT/fixtures/admission-chain.policy-decision.signed.json" \
schemas/mountainshares-trust-receipts/v1/run_trust_build_gate.sh:106:    "$ROOT/fixtures/admission-chain.memory-authorization.signed.json" \
schemas/mountainshares-trust-receipts/v1/run_trust_build_gate.sh:116:  "projection-policy-decision" \
schemas/mountainshares-trust-receipts/v1/run_trust_build_gate.sh:117:  "$ROOT/fixtures/admission-chain.projection.policy-decision-mismatch.signed.json" \
schemas/mountainshares-trust-receipts/v1/run_trust_build_gate.sh:141:  "$ROOT/fixtures/admission-chain.policy-decision.intent-id-mismatch.signed.json" \
schemas/mountainshares-trust-receipts/v1/run_trust_build_gate.sh:142:  "$ROOT/fixtures/admission-chain.policy-decision.adapter-mismatch.signed.json" \
schemas/mountainshares-trust-receipts/v1/run_trust_build_gate.sh:143:  "$ROOT/fixtures/admission-chain.policy-decision.projection-commitment-mismatch.signed.json"
schemas/mountainshares-trust-receipts/v1/run_trust_build_gate.sh:153:    "$ROOT/fixtures/admission-chain.memory-authorization.signed.json" \
schemas/mountainshares-trust-receipts/v1/runtime_authority_manifest/runtime_authority_manifest_v1.json:61:            "const": "Ed25519"
schemas/mountainshares-trust-receipts/v1/runtime_manifest_crypto.py:3:from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
schemas/mountainshares-trust-receipts/v1/runtime_manifest_crypto.py:18:    if approval["algorithm"]!="Ed25519":
schemas/mountainshares-trust-receipts/v1/runtime_manifest_crypto.py:23:        public_key=Ed25519PublicKey.from_public_bytes(public_key_bytes)
schemas/mountainshares-trust-receipts/v1/runtime_manifest_crypto.py:27:        public_key.verify(signature,canonical_manifest_payload(manifest))
schemas/mountainshares-trust-receipts/v1/signed-operation-intent.schema.json:49:    "subject_signature": {
schemas/mountainshares-trust-receipts/v1/signed-operation-intent.schema.json:53:          "const": "Ed25519"
schemas/mountainshares-trust-receipts/v1/signed-operation-intent.schema.json:88:    "subject_signature"
schemas/mountainshares-trust-receipts/v1/test_canonicalization_contract.py:10:from receipt_crypto import canonical_payload
schemas/mountainshares-trust-receipts/v1/test_canonicalization_contract.py:23:                    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/test_canonicalization_contract.py:49:                    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/test_canonicalization_contract.py:55:                    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/test_canonicalization_contract.py:78:                    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/test_canonicalization_contract.py:97:                "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/test_canonicalization_contract.py:107:            canonical_payload(receipt, "signature"),
schemas/mountainshares-trust-receipts/v1/test_canonicalization_contract.py:108:            canonical_payload(changed, "signature"),
schemas/mountainshares-trust-receipts/v1/test_canonicalization_cross_module_integration.py:9:from receipt_crypto import canonical_payload
schemas/mountainshares-trust-receipts/v1/test_canonicalization_cross_module_integration.py:22:                    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/test_canonicalization_cross_module_integration.py:53:                "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/test_canonicalization_cross_module_integration.py:59:        generated_payload = canonical_payload(
schemas/mountainshares-trust-receipts/v1/test_canonicalization_cross_module_integration.py:66:        verified_payload = canonical_payload(
schemas/mountainshares-trust-receipts/v1/test_canonicalization_cross_module_integration.py:87:                "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/test_canonicalization_cross_module_integration.py:95:            canonical_payload(receipt, "signature"),
schemas/mountainshares-trust-receipts/v1/test_canonicalization_mutation_integrity.py:9:from receipt_crypto import canonical_payload
schemas/mountainshares-trust-receipts/v1/test_canonicalization_mutation_integrity.py:22:                    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/test_canonicalization_mutation_integrity.py:45:                    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/test_canonicalization_mutation_integrity.py:64:                "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/test_canonicalization_mutation_integrity.py:74:            canonical_payload(receipt, "signature"),
schemas/mountainshares-trust-receipts/v1/test_canonicalization_mutation_integrity.py:75:            canonical_payload(mutated, "signature"),
schemas/mountainshares-trust-receipts/v1/test_canonicalization_mutation_integrity.py:83:                "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/test_canonicalization_mutation_integrity.py:94:            canonical_payload(receipt, "signature"),
schemas/mountainshares-trust-receipts/v1/test_canonicalization_mutation_integrity.py:95:            canonical_payload(mutated, "signature"),
schemas/mountainshares-trust-receipts/v1/test_canonicalization_negative_paths.py:8:from receipt_crypto import canonical_payload
schemas/mountainshares-trust-receipts/v1/test_canonicalization_negative_paths.py:31:            canonical_payload(receipt, "signature")
schemas/mountainshares-trust-receipts/v1/test_canonicalization_negative_paths.py:43:                "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/test_canonicalization_negative_paths.py:50:        payload = canonical_payload(receipt, "signature")
schemas/mountainshares-trust-receipts/v1/test_canonicalization_negative_paths.py:53:        self.assertIn(b'"Ed25519"', payload)
schemas/mountainshares-trust-receipts/v1/test_canonicalization_negative_paths.py:61:                "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/test_canonicalization_negative_paths.py:70:                "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/test_canonicalization_negative_paths.py:77:            canonical_payload(first, "signature"),
schemas/mountainshares-trust-receipts/v1/test_canonicalization_negative_paths.py:78:            canonical_payload(second, "signature")
schemas/mountainshares-trust-receipts/v1/test_canonicalization_replay_determinism.py:10:from receipt_crypto import canonical_payload
schemas/mountainshares-trust-receipts/v1/test_canonicalization_replay_determinism.py:23:                    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/test_canonicalization_replay_determinism.py:29:                    "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/test_canonicalization_replay_determinism.py:71:                "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/test_canonicalization_replay_determinism.py:77:        first = canonical_payload(receipt, "signature")
schemas/mountainshares-trust-receipts/v1/test_canonicalization_replay_determinism.py:78:        second = canonical_payload(copy.deepcopy(receipt), "signature")
schemas/mountainshares-trust-receipts/v1/test_canonicalization_replay_determinism.py:88:                "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/test_canonicalization_replay_determinism.py:97:            canonical_payload(receipt, "signature"),
schemas/mountainshares-trust-receipts/v1/test_canonicalization_replay_determinism.py:98:            canonical_payload(replay, "signature"),
schemas/mountainshares-trust-receipts/v1/test_durable_ledger.py:29:        subject_signature_key_id="durable-ledger-subject-key-001",
schemas/mountainshares-trust-receipts/v1/test_durable_ledger.py:36:        policy_decision_id="durable-ledger-pdr-001",
schemas/mountainshares-trust-receipts/v1/test_durable_ledger_sqlite.py:31:        subject_signature_key_id="sqlite-subject-key-001",
schemas/mountainshares-trust-receipts/v1/test_durable_ledger_sqlite.py:38:        policy_decision_id="sqlite-pdr-001",
schemas/mountainshares-trust-receipts/v1/test_receipt_chain_rules.py:24:    (fixtures / "admission-chain.policy-decision.signed.json").read_text()
schemas/mountainshares-trust-receipts/v1/test_receipt_chain_rules.py:27:    (fixtures / "admission-chain.memory-authorization.signed.json").read_text()
schemas/mountainshares-trust-receipts/v1/test_receipt_chain_rules.py:48:print("RECEIPT_CHAIN_RULES_VALID", result["policy_decision_id"])
schemas/mountainshares-trust-receipts/v1/test_receipt_chain_rules.py:53:        "admission-chain.projection.policy-decision-mismatch.signed.json",
schemas/mountainshares-trust-receipts/v1/test_runtime_authority_manifest_canonicalization.py:42:                "algorithm": "Ed25519",
schemas/mountainshares-trust-receipts/v1/test_runtime_authority_manifest_canonicalization.py:64:    def test_canonical_payload_excludes_signature_value(self):
schemas/mountainshares-trust-receipts/v1/test_runtime_authority_manifest_canonicalization.py:70:        self.assertIn(b'"algorithm":"Ed25519"', payload)
schemas/mountainshares-trust-receipts/v1/usage_ledger.py:3:def consume(db_path,receipt_id,max_uses):
schemas/mountainshares-trust-receipts/v1/usage_ledger.py:11:        connection.execute("CREATE TABLE IF NOT EXISTS receipt_uses (receipt_id TEXT PRIMARY KEY,max_uses INTEGER NOT NULL,uses INTEGER NOT NULL CHECK(uses>=0))")
schemas/mountainshares-trust-receipts/v1/usage_ledger.py:12:        row=connection.execute("SELECT max_uses,uses FROM receipt_uses WHERE receipt_id=?",(receipt_id,)).fetchone()
schemas/mountainshares-trust-receipts/v1/usage_ledger.py:15:            connection.execute("INSERT INTO receipt_uses(receipt_id,max_uses,uses) VALUES(?,?,?)",(receipt_id,max_uses,uses))
schemas/mountainshares-trust-receipts/v1/usage_ledger.py:23:            connection.execute("UPDATE receipt_uses SET uses=? WHERE receipt_id=?",(uses,receipt_id))
schemas/mountainshares-trust-receipts/v1/verify_admission_linked_receipt_chain.py:48:        str(base / "verify_policy_decision_receipt.py"),
schemas/mountainshares-trust-receipts/v1/verify_admission_linked_receipt_chain.py:54:        str(base / "verify_memory_authorization_receipt.py"),
schemas/mountainshares-trust-receipts/v1/verify_admission_linked_receipt_chain.py:101:    pdr["decision_id"],
schemas/mountainshares-trust-receipts/v1/verify_admission_linked_receipt_chain.py:102:    mar["receipt_id"],
schemas/mountainshares-trust-receipts/v1/verify_memory_authorization_receipt.py:6:from receipt_crypto import verify_ed25519
schemas/mountainshares-trust-receipts/v1/verify_memory_authorization_receipt.py:10:    raise SystemExit("USAGE: verify_memory_authorization_receipt.py RECEIPT_JSON TRUSTED_PUBLIC_KEYS_JSON")
schemas/mountainshares-trust-receipts/v1/verify_memory_authorization_receipt.py:16:schema_path=Path(__file__).parent/"memory-authorization-receipt.schema.json"
schemas/mountainshares-trust-receipts/v1/verify_memory_authorization_receipt.py:19:if receipt.get("type")!="mountainshares.memory-authorization-receipt/v1":
schemas/mountainshares-trust-receipts/v1/verify_memory_authorization_receipt.py:32:signature_fields=("subject_signature","guardian_attestation")
schemas/mountainshares-trust-receipts/v1/verify_memory_authorization_receipt.py:34:for signature_field,required_role in (("subject_signature","subject"),("guardian_attestation","guardian")):
schemas/mountainshares-trust-receipts/v1/verify_memory_authorization_receipt.py:40:        verified_key_ids.append(verify_ed25519(receipt,signature_field,entry["public_key"],signature_fields))
schemas/mountainshares-trust-receipts/v1/verify_policy_decision_receipt.py:6:from receipt_crypto import verify_ed25519
schemas/mountainshares-trust-receipts/v1/verify_policy_decision_receipt.py:10:    raise SystemExit("USAGE: verify_policy_decision_receipt.py RECEIPT_JSON TRUSTED_PUBLIC_KEYS_JSON")
schemas/mountainshares-trust-receipts/v1/verify_policy_decision_receipt.py:16:schema_path=Path(__file__).parent/"policy-decision-receipt.schema.json"
schemas/mountainshares-trust-receipts/v1/verify_policy_decision_receipt.py:19:if receipt.get("type")!="mountainshares.policy-decision-receipt/v1":
schemas/mountainshares-trust-receipts/v1/verify_policy_decision_receipt.py:32:key_id=receipt["guardian_signature"]["key_id"]
schemas/mountainshares-trust-receipts/v1/verify_policy_decision_receipt.py:39:    verified_key_id=verify_ed25519(receipt,"guardian_signature",public_key_b64)
schemas/mountainshares-trust-receipts/v1/verify_projection_receipt.py:6:from receipt_crypto import verify_ed25519
schemas/mountainshares-trust-receipts/v1/verify_projection_receipt.py:39:    verified_key_id=verify_ed25519(receipt,"projection_signature",entry["public_key"])
schemas/mountainshares-trust-receipts/v1/verify_response_receipt.py:6:from receipt_crypto import verify_ed25519
schemas/mountainshares-trust-receipts/v1/verify_response_receipt.py:32:    verified_key_id=verify_ed25519(receipt,"response_signature",entry["public_key"])
services/crypto_client.py:12:    "signing":      {"primary_sig": "ML-DSA-65", "fallback_sig": "Ed25519",
services/hilbert/sign_promotion_event.py:28:signature = private_key.sign(
services/hilbert/verify_promotion_event.py:18:public_key.verify(
services/jarviscryptopolicy.py:76:def _sign(data: str) -> str:
services/jarviscryptopolicy.py:81:    sig = _sign(payload)
services/jarviscryptopolicy.py:90:        if not hmac.compare_digest(_sign(payload), sig):
services/jarviscryptopolicy.py:95:        # Check revocation list
services/jarviscryptopolicy.py:171:    sig = _sign(f"{req.key_id}:{req.data}")
services/judgesigner.py:52:        def sign(sk_bytes: bytes, message: bytes) -> bytes:
services/judgesigner.py:54:                return s.sign(message)
services/judgesigner.py:57:        def verify(pk_bytes: bytes, message: bytes, signature: bytes) -> bool:
services/judgesigner.py:59:                return v.verify(message, signature, pk_bytes)
services/judgesigner.py:73:        def sign(sk_bytes: bytes, message: bytes) -> bytes:
services/judgesigner.py:74:            return _DilithiumClass.sign(sk_bytes, message)
services/judgesigner.py:77:        def verify(pk_bytes: bytes, message: bytes, signature: bytes) -> bool:
services/judgesigner.py:78:            return _DilithiumClass.verify(pk_bytes, message, signature)
services/judgesigner.py:134:    sig_bytes = ML_DSA_65.sign(sk, msg_hash)
services/judgesigner.py:172:        return ML_DSA_65.verify(pk, msg_hash, sig_bytes)
services/llm_judge_v3.py:80:async def verify(request: V3JudgeRequest) -> V3Verdict:
services/rag_grounded_v2.py:61:async def verify(request: GroundedRequest) -> GroundedVerdict:
thesis_chapter_gates/close_ch16_container_native.sh:181:if suite.get("fallback_sig") != "Ed25519":
thesis_chapter_gates/close_ch16_container_native.sh:182:    raise SystemExit("fallback_sig is not Ed25519")
thesis_chapter_gates/close_ch16_container_native_strict.sh:201:if suite.get("fallback_sig") != "Ed25519":
thesis_chapter_gates/close_ch16_container_native_strict.sh:202:    raise SystemExit("fallback_sig is not Ed25519")
thesis_chapter_gates/close_ch16_container_native_strict.sh:205:require_text "$TMP/safe_fallback.json" '"fallback_sig": "Ed25519"' "safe_fallback_ed25519"
thesis_chapter_gates/continue_ch42_ch29_after_pia_subspace.sh:102:if primary != "ML-DSA-65" or fallback != "Ed25519":
thesis_chapter_gates/continue_ch42_ch29_after_pia_subspace.sh:155:echo "Ch42 may claim ML-DSA-65 judge signing, public-key availability, tamper/unsigned rejection, BBB verifier delegation, and Ed25519 fallback at verified runtime scope. Ch29 may claim BBB/guardian safeguards plus PIA review over Ms. Jarvis's H_p/subspace stability pathway: per-user partitioning, non-surveillance suppression, deletion, pruning, commons isolation, Phi stability floor, and guardian audit. Do not present this as clinical diagnosis, therapy, or guaranteed psychological safety."
thesis_chapter_gates/seal_ch42_ch29_and_gate_ch28_ch39.sh:44:echo "- Ch42 may claim ML-DSA-65 judge signing, public-key endpoints, tamper/unsigned rejection, BBB verifier delegation, and Ed25519 fallback at verified runtime scope."
thesis_chapter_gates/seal_ch47_ch43_and_gate_ch42_ch29.sh:84:[ -f "$CH42" ] && rg -n "post.quantum|quantum|ML-DSA|Dilithium|signature|judge|public.key|verify|tamper|unsigned|fallback|Ed25519|not yet|aspirational|future|will|TODO|demonstrated" "$CH42" || true
thesis_chapter_gates/seal_ch47_ch43_and_gate_ch42_ch29.sh:216:if suite.get("primary_sig") != "ML-DSA-65" or suite.get("fallback_sig") != "Ed25519":
thesis_chapter_gates/seal_ch47_ch43_and_gate_ch42_ch29.sh:269:echo "Ch42 may claim ML-DSA-65 judge signing, public-key endpoints, tamper/unsigned rejection, BBB verifier delegation, and Ed25519 fallback only at the verified Ch16 runtime scope. Ch29 may claim BBB, constitutional guardian, audit logging, policy tests, and fail-closed suppression paths where verified; avoid clinical, therapeutic, diagnostic, or universal harm-prevention claims unless separately proven."

=== relevant Python files ===
./evidence/stage-6.11.7/provisioned-chain/runtime-authority-manifest.guardian.signed.json
./schemas/mountainshares-trust-receipts/v1/durable_ledger/models.py
./schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.memory-authorization.signed.json
./schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.adapter-mismatch.signed.json
./schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.intent-id-mismatch.signed.json
./schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.projection-commitment-mismatch.signed.json
./schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.policy-decision.signed.json
./schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.projection.authorization-mismatch.signed.json
./schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.projection.policy-decision-mismatch.signed.json
./schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.projection.scope-mismatch.signed.json
./schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.projection.signed.json
./schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.response.projection-mismatch.signed.json
./schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.response.provenance-mismatch.signed.json
./schemas/mountainshares-trust-receipts/v1/fixtures/admission-chain.response.signed.json
./schemas/mountainshares-trust-receipts/v1/fixtures/memory-authorization.signed.json
./schemas/mountainshares-trust-receipts/v1/fixtures/memory-authorization.signed.tampered.json
./schemas/mountainshares-trust-receipts/v1/fixtures/operation-intent.expired.signed.json
./schemas/mountainshares-trust-receipts/v1/fixtures/operation-intent.signed.tampered.json
./schemas/mountainshares-trust-receipts/v1/fixtures/operation-intent.untrusted-key.json
./schemas/mountainshares-trust-receipts/v1/fixtures/operation-intent.valid.signed.json
./schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.expired.json
./schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.invalid-lifetime.json
./schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.missing-constraints.json
./schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.signed.json
./schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.signed.tampered.json
./schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.untrusted-key.json
./schemas/mountainshares-trust-receipts/v1/fixtures/policy-allow.valid.json
./schemas/mountainshares-trust-receipts/v1/fixtures/projection.signed.json
./schemas/mountainshares-trust-receipts/v1/fixtures/projection.signed.tampered.json
./schemas/mountainshares-trust-receipts/v1/fixtures/response.signed.json
./schemas/mountainshares-trust-receipts/v1/fixtures/response.signed.tampered.json
./schemas/mountainshares-trust-receipts/v1/fixtures/runtime-authority-manifest.duplicate-key.json
./schemas/mountainshares-trust-receipts/v1/fixtures/runtime-authority-manifest.duplicate-role.json
./schemas/mountainshares-trust-receipts/v1/fixtures/runtime-authority-manifest.expired.json
./schemas/mountainshares-trust-receipts/v1/fixtures/runtime-authority-manifest.signed.json
./schemas/mountainshares-trust-receipts/v1/fixtures/runtime-authority-manifest.tampered-release.json
./schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py
./schemas/mountainshares-trust-receipts/v1/memory_authorization_gate.py
./schemas/mountainshares-trust-receipts/v1/memory-authorization-receipt.schema.json
./schemas/mountainshares-trust-receipts/v1/operation_intent_rules.py
./schemas/mountainshares-trust-receipts/v1/policy-decision-receipt.schema.json
./schemas/mountainshares-trust-receipts/v1/projection-receipt.schema.json
./schemas/mountainshares-trust-receipts/v1/receipt_chain_rules.py
./schemas/mountainshares-trust-receipts/v1/receipt_crypto.py
./schemas/mountainshares-trust-receipts/v1/runtime_authority_manifest/runtime_authority_manifest_v1.json
./schemas/mountainshares-trust-receipts/v1/runtime_manifest_crypto.py
./schemas/mountainshares-trust-receipts/v1/signed-operation-intent.schema.json
./schemas/mountainshares-trust-receipts/v1/test_canonicalization_contract.py
./schemas/mountainshares-trust-receipts/v1/test_canonicalization_cross_module_integration.py
./schemas/mountainshares-trust-receipts/v1/test_canonicalization_mutation_integrity.py
./schemas/mountainshares-trust-receipts/v1/test_canonicalization_negative_paths.py
./schemas/mountainshares-trust-receipts/v1/test_canonicalization_replay_determinism.py
./schemas/mountainshares-trust-receipts/v1/test_durable_ledger.py
./schemas/mountainshares-trust-receipts/v1/test_durable_ledger_sqlite.py
./schemas/mountainshares-trust-receipts/v1/test_receipt_chain_rules.py
./schemas/mountainshares-trust-receipts/v1/test_runtime_authority_manifest_canonicalization.py
./schemas/mountainshares-trust-receipts/v1/verify_admission_linked_receipt_chain.py
./schemas/mountainshares-trust-receipts/v1/verify_memory_authorization_receipt.py
./schemas/mountainshares-trust-receipts/v1/verify_policy_decision_receipt.py
./schemas/mountainshares-trust-receipts/v1/verify_projection_receipt.py
./schemas/mountainshares-trust-receipts/v1/verify_response_receipt.py
./services/crypto_client.py

=== current test files ===
services/chroma_python_test.py
services/chroma_test.py
services/hilbert/test_hilbert_state.py
services/overflow_policy/test_overflow_guard.py
services/person_space_policy/test_person_space_guard.py
services/populate_security_layers_test.py
services/test_aacpe_features.py
services/test_aapcappe_corpus.py
services/test_aapcappe_retrieval.py
services/test_caller_auth.py
services/test_chroma_client.py
services/test_chromadb_heartbeat.py
services/test_chromadb_v2_heartbeat.py
services/test_ddg_verbose.py
services/test_end_to_end_woah_fifthdgm.py
services/test_fifth_dgm_integration.py
services/test_full_brain_integration.py
services/test_gbim_llm_summary.py
services/test_gbim_semantic_query.py
services/test_geodb_llm_summary.py
services/test_gis_chat.py
services/test_health_access_gbim.py
services/test_imm_query.py
services/test_knowledge_base.py
services/test_method_tracking.py
services/test_multi_collection_query.py
services/test_rag.py
services/test_retrieval_endpoint.py
services/test_spatial_awareness.py
services/test_stage_6_11_6_enforcement.py
services/test_stage_6_11_7_admission_live.py

=== schema files ===
schemas/mountainshares-trust-receipts/v1/admit_runtime_authority_manifest.py
schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py
schemas/mountainshares-trust-receipts/v1/guardian-admission-integration-scope.json
schemas/mountainshares-trust-receipts/v1/intent_consumption_ledger.py
schemas/mountainshares-trust-receipts/v1/memory_authorization_gate.py
schemas/mountainshares-trust-receipts/v1/memory-authorization-receipt.schema.json
schemas/mountainshares-trust-receipts/v1/operation_intent_consumption.py
schemas/mountainshares-trust-receipts/v1/operation_intent_rules.py
schemas/mountainshares-trust-receipts/v1/policy-decision-receipt.schema.json
schemas/mountainshares-trust-receipts/v1/projection-receipt.schema.json
schemas/mountainshares-trust-receipts/v1/receipt_chain_errors.py
schemas/mountainshares-trust-receipts/v1/receipt_chain_rules.py
schemas/mountainshares-trust-receipts/v1/receipt_crypto.py
schemas/mountainshares-trust-receipts/v1/receipt_rules.py
schemas/mountainshares-trust-receipts/v1/response-receipt.schema.json
schemas/mountainshares-trust-receipts/v1/runtime-admission-record.schema.json
schemas/mountainshares-trust-receipts/v1/runtime-authority-manifest.schema.json
schemas/mountainshares-trust-receipts/v1/runtime_manifest_crypto.py
schemas/mountainshares-trust-receipts/v1/run_trust_build_gate.sh
schemas/mountainshares-trust-receipts/v1/SCHEMA_BASELINE.sha256
schemas/mountainshares-trust-receipts/v1/signed-operation-intent.schema.json
schemas/mountainshares-trust-receipts/v1/test_canonicalization_contract.py
schemas/mountainshares-trust-receipts/v1/test_canonicalization_cross_module_integration.py
schemas/mountainshares-trust-receipts/v1/test_canonicalization_mutation_integrity.py
schemas/mountainshares-trust-receipts/v1/test_canonicalization_negative_paths.py
schemas/mountainshares-trust-receipts/v1/test_canonicalization_replay_determinism.py
schemas/mountainshares-trust-receipts/v1/test_durable_ledger.py
schemas/mountainshares-trust-receipts/v1/test_durable_ledger_sqlite.py
schemas/mountainshares-trust-receipts/v1/test_intent_consumption.py
schemas/mountainshares-trust-receipts/v1/test_receipt_chain_rules.py
schemas/mountainshares-trust-receipts/v1/test_runtime_authority_manifest_canonicalization.py
schemas/mountainshares-trust-receipts/v1/test_runtime_authority_manifest_schema.py
schemas/mountainshares-trust-receipts/v1/TRUST_BUILD_BASELINE.sha256
schemas/mountainshares-trust-receipts/v1/usage_ledger.py
schemas/mountainshares-trust-receipts/v1/validate_receipt.py
schemas/mountainshares-trust-receipts/v1/verify_admission_linked_receipt_chain.py
schemas/mountainshares-trust-receipts/v1/verify_memory_authorization_receipt.py
schemas/mountainshares-trust-receipts/v1/verify_policy_decision_receipt.py
schemas/mountainshares-trust-receipts/v1/verify_projection_receipt.py
schemas/mountainshares-trust-receipts/v1/verify_response_receipt.py
schemas/mountainshares-trust-receipts/v1/verify_runtime_admission_record.py
schemas/mountainshares-trust-receipts/v1/verify_runtime_authority_manifest.py
schemas/mountainshares-trust-receipts/v1/verify_runtime_governance_policy.py
schemas/mountainshares-trust-receipts/v1/verify_runtime_image_binding.py
schemas/mountainshares-trust-receipts/v1/verify_signed_operation_intent.py

=== installed implementation dependencies ===
cryptography=available
nacl=missing
jsonschema=available
fastapi=available
pydantic=available

=== caller-registry protection ===
::	.guardian-callers
.gitignore:248:.guardian-callers/	.guardian-callers/example.json

=== source hashes ===
3a94b20a56bc0e3720f0b87fd2e96735804d6b4f6f6de37eb3ff9fe23f282b84  services/constitutional_api.py
1ad8e95beeb163b42655d7de1ac036bb83852af91ca9c540c4869a8f4d43d17b  services/test_caller_auth.py
1ffa0cf47836f504e3e492386175920bf0855fa594fca834836ddb8a2139a56d  .gitignore

=== current HEAD integrity ===
5f728e6 Remove stale autonomous learner symlink

preflight_report=/tmp/msjarvis-guardian-pdr-mar-preflight-20260808T011532Z.txt

Shell remains active.
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-trust-integration$ 

