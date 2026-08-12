# MountainShares / Ms. Jarvis Trust Architecture v1.2

**Status:** Architecture Freeze Candidate — Implementation and Verification Update (Revision v1.2)  
**Authority:** Canonical design reference for pilot trust-boundary work  
**Date:** 2026-08-11  
**Supersedes:** v1.1 (same date)  
**Scope:** Software provenance, runtime authority, user sovereignty, Commons integrity, policy-governed AI projections, receipt-based authorization, and fail-closed governance boundaries.

---

## Revision Note (v1.1 → v1.2)

This revision records verification and implementation progress made after the v1.1 snapshot. It does not change the governing principle or any non-goal. It advances several "current state" descriptions from *implemented* toward *verified*, introduces one new governance construct, and leaves every production-authorization gate exactly where v1.1 left it.

Concrete changes in this revision:

1. **Guardian Authority Bundle introduced (§4).** Caller identities, subject keys, and revocation state are now carried in a single governance-signed authority bundle gated by a three-role threshold, replacing the earlier separately configured caller, subject-key, and revocation registries.
2. **PDR issuance verified end-to-end (§9, §14, §15).** The issue → durable-consume → replay-deny path has been demonstrated under a provisioned Guardian signer. Production signer enrollment in the production trusted registry remains the outstanding gate.
3. **Revocation enforced at the decision boundary (§7, §11, §14, §15).** Subject and intent revocation are checked in the request path via the signed authority bundle and fail closed. Projection-path revocation integration remains pending.
4. **Adversarial verification matrix partially closed (§14).** Decision-boundary cases are verified; expiration, policy-version mismatch, unapproved-image, Guardian-outage, and the full projection chain remain.
5. **Custodian ceremony initiated (§16, §17).** The activation ceremony has begun; it is not complete and grants no authority.

No capability is upgraded to *production-authorized* by this revision. The system remains a tested, evidence-backed, fail-closed release candidate.

---

## 1. Core Principle

> Integrity proves what happened. Authority proves who may cause it. Policy proves whether it was allowed.

Merkle structures provide tamper-evident integrity evidence. Cryptographic keys and signatures establish attributable authority. The Constitutional Guardian evaluates applicable policy. A runtime may act on protected data only when it can verify the applicable authorization chain and any required unexpired authorization receipt.

A hash, CID, file, image, container, record, or service does not become authoritative merely because it exists or can be referenced.

A Merkle root without a valid controlling signature, timestamp context, and governance interpretation is only an integrity commitment. It has no authority value on its own.

The implementation work completed through the Stage 6 trust-development sequence reinforces this separation. Runtime admission, caller authentication, signed operation-intent verification, policy evaluation, receipt issuance, and production activation are separate authority boundaries.

A successful test, an existing artifact, or a valid cryptographic commitment does not by itself authorize deployment or protected-data access.

---

## 2. Non-Goals

This architecture does not attempt to:

- Create a universal public memory graph.
- Make all user information globally discoverable.
- Treat hashes as identity.
- Treat AI inference as authority.
- Replace human governance with automated decisions.
- Guarantee deletion of information already disclosed to another recipient.
- Claim anonymization solely from a cryptographic commitment.
- Treat the existence of a container, file, service, image, or repository branch as proof that it is canonical or authorized.
- Give a reasoning model unrestricted access to personal memory, private identity data, or long-lived decryption keys.
- Treat successful software tests as equivalent to production authorization.
- Treat a release-candidate evidence bundle as an active authority system.
- Treat an available signing key as sufficient authority without the corresponding governance policy, role, registry, runtime, and authorization conditions.
- Treat an OpenPGP release-signing key as interchangeable with a raw Ed25519 Guardian signing key.
- Treat a governance-signed authority bundle validated with test or ephemeral governance keys as equivalent to a production authority bundle signed by the established production governance board.
- Treat a technically deployable topology as authorized merely because it can be deployed.
- Treat interaction with Ms. Jarvis as authorization to contribute private information to the Commons.

The architecture intentionally preserves the distinction between:

1. evidence of correctness;
2. authority to act;
3. authorization to perform a particular operation; and
4. production activation.

---

## 3. Trust Domains

```
                          GOVERNANCE PLANE
       Keys - Roles - Policies - Threshold Approvals - Revocation
                                 |
                                 v
                      POLICY DECISION ENGINE

      -----------------------------------------------------------
      |                         |                               |
      v                         v                               v
SOFTWARE PROVENANCE       USER SOVEREIGNTY              COMMONS INTEGRITY
Build Merkle Tree         Vault Merkle Tree             Epoch Merkle Tree
Runtime Authority         Authorization Receipts       Contribution Receipts
Admission Records         Projection Receipts          Transformation Receipts
```

The domains may reference each other through signed receipts, but no domain inherits authority merely from a reference.

The operational trust chain is:

```
Source / Build Evidence
        |
        v
Runtime Authority
        |
        v
Runtime Admission
        |
        v
Authenticated Caller
        |
        v
Signed Operation Intent
        |
        v
Policy Decision
        |
        v
Policy Decision Receipt
        |
        v
Memory Authorization Receipt
        |
        v
Projection Authorization
        |
        v
Bounded Context
        |
        v
Reasoning Runtime
```

Not every stage in this chain is currently production-activated. The chain is deliberately designed so that a missing downstream authority does not cause an upstream component to silently grant access.

---

## 4. Governance Plane

The governance plane defines:

- Authorized signing identities and key-rotation rules.
- Roles, delegation limits, and threshold-approval requirements.
- Versioned policies and policy-decision semantics.
- Revocation, incident-response, and audit-retention rules.
- Required review procedures for high-impact actions.
- Which protected capabilities fail closed.
- The authority required to approve a runtime, policy, transformation, or Commons governance action.

A Merkle root is evidence. Governance keys, role assignments, policies, and verified signatures are the authority layer.

The Policy Decision Engine evaluates requests against the active policy set. It does not replace human governance. It applies the policies and delegations established by governance.

The current trust-development model distinguishes operational approval from Guardian authority and from governance-board authority. These roles are not interchangeable.

The production governance model requires the relevant roles, policies, registries, and signing authorities to be independently established before production activation.

The existing release-signing mechanism is likewise distinct from the raw Ed25519 Guardian PDR signing authority. Possession or verification of a release-signing key does not create Guardian authorization.

### Guardian Authority Bundle

The governance plane's concrete authority carrier at the decision boundary is the Guardian Authority Bundle. Rather than sourcing caller identities, subject keys, and revocation state from separately configured, individually trusted files, the Guardian consumes one governance-signed bundle that carries all three together and is only accepted when it satisfies a governance threshold.

```
{
  "type": "mountainshares.guardian-authority-bundle/v1",
  "bundle_id": "<bundle-id>",
  "release": "<release-profile>",

  "issued_at": "RFC3339 timestamp",
  "expires_at": "RFC3339 timestamp",

  "callers": {
    "sha256:<caller-token-commitment>": {
      "caller_id": "did:mountainshares:<caller>",
      "roles": ["caller"],
      "status": "active"
    }
  },

  "subject_keys": {
    "<subject-key-id>": {
      "public_key": "<base64-ed25519-public-key>",
      "roles": ["subject"],
      "controller": "did:mountainshares:<subject>",
      "status": "active"
    }
  },

  "revocations": {
    "revoked_subjects": [],
    "revoked_intent_ids": [],
    "revoked_receipt_ids": []
  },

  "approvals": [
    { "role": "operations-approver", "key_id": "<id>", "algorithm": "Ed25519", "value": "<signature>" },
    { "role": "security-approver",   "key_id": "<id>", "algorithm": "Ed25519", "value": "<signature>" },
    { "role": "governance-board",    "key_id": "<id>", "algorithm": "Ed25519", "value": "<signature>" }
  ]
}
```

The Guardian MUST verify, before trusting any field in the bundle:

- The canonical bundle payload against each declared approval signature.
- Each approver key against the governance public-key registry, including its role.
- That the set of approvals satisfies the active policy's `minimum_approvals` and `required_roles` threshold for the declared release.
- Bundle expiration.
- That caller authentication, subject-key lookup, and revocation checks are drawn only from this verified bundle — never from an unsigned or separately configured source.

Caller tokens are matched by commitment, not by storing the raw token. Subject keys carry an explicit `controller` and `status`, so an inactive subject key is rejected even when structurally present. Revocation of a subject, an intent, or a prior receipt is expressed inside the same signed bundle, so revocation state inherits the bundle's governance signature rather than being a separately trusted input.

#### Current state

The Guardian Authority Bundle schema, canonical-payload verifier, and three-role threshold enforcement are implemented and verified end-to-end at the decision boundary. Verification has been demonstrated against governance keys and a policy requiring `operations-approver`, `security-approver`, and `governance-board` approvals, using ephemeral test governance keys.

This establishes the mechanism. It does not establish production authority. A production authority bundle signed by the *established* production governance board — including a real, enrolled `governance-board` key — remains outstanding. Verification with ephemeral governance keys demonstrates the code path; it is not equivalent to a governance-approved production bundle (see §2).

---

## 5. Software Provenance Domain

The software provenance domain establishes which artifacts are approved to execute.

```
Source -> Commit -> Build Recipe -> SBOM -> Image Digest
      -> Runtime Authority Manifest -> Deployment Approval
      -> Runtime Admission -> Running Service
```

A Runtime Authority Manifest MUST:

- Pin immutable container image digests.
- Enumerate required services, health contracts, and network dependencies.
- Identify approved policy versions.
- Include or reference SBOMs.
- Define dependency failure modes.
- Identify approved configuration references.
- Carry required release and governance signatures.
- Identify rollback targets and revocation procedures.

`latest` tags, filenames, backup status, container existence, and source-tree location are not authority assertions.

A file existing in a repository is historical evidence unless an approved build and signed Runtime Authority Manifest declare it part of the current runtime.

### Current implementation and verification state

Runtime-authority verification has progressed beyond the original architecture-only definition.

The Stage 6.11 runtime-authority work established signature-verification infrastructure and produced evidence for verification of the applicable runtime-authority manifest. The resulting verification evidence was subsequently preserved through the project's evidence-sealing process.

Runtime admission was also advanced from a conceptual boundary to an implemented fail-closed enforcement mechanism. The runtime must satisfy the applicable authority conditions before protected operations can proceed.

The existing Guardian runtime has been associated with a specific immutable image digest rather than an unrestricted mutable image tag.

A candidate deployment topology for the provisioned Guardian exists but is intentionally not deployable as written: it references a Guardian PDR signer that is absent from the trusted signer registry, and the currently running topology is deliberately unprovisioned. The current deployment therefore fails closed. This is a concrete instance of the non-goal that a technically deployable topology is not authorized merely because it can be deployed.

These results establish meaningful runtime-authority and admission evidence.

They do not, by themselves, establish final production deployment authority.

Production activation remains dependent on the outstanding governance, signer-registry, policy, and release conditions described later in this document.

---

## 6. User Sovereignty Domain

```
Private User Vault -> Signed Vault Root -> Authorization Receipt
                  -> Projection Service -> Ms. Jarvis Reasoning
                  -> Response Receipt
```
> Ms. Jarvis does not possess user memory. Ms. Jarvis receives authorized projections of user memory.

Private records MUST be encrypted before content-addressed storage. Vault roots SHOULD be private by default.

Public commitments MUST contain no plaintext private memory, predictable identifiers, wallet addresses, social handles, or other correlatable low-entropy values.

The reasoning system MUST NOT receive long-lived vault keys or unrestricted semantic-store access. It receives the minimum projection necessary for the approved purpose.

A projection may be:

- A selected set of decrypted records.
- A redacted summary.
- A semantic retrieval result.
- A computed feature vector.
- A policy answer.
- An anonymized contribution.
- A selective-disclosure proof.

The system MUST use the least powerful representation sufficient for the authorized task.

The existence of a semantic-memory system does not itself authorize that system to expose the underlying private corpus.

---

## 7. Operational Trust Boundary

```
             USER REQUEST
                  |
                  v
        Caller Authentication
                  |
                  v
         Runtime Admission
                  |
                  v
       Signed Operation Intent
                  |
                  v
        Constitutional Guardian
                  |
                  v
        Policy Decision Receipt
                  |
                  v
       Memory Authorization Receipt
                  |
                  v
          Projection Service
                  |
       +----------+----------+
       |                     |
       v                     v
Encrypted User Vault     Audit Receipts
       |
       v
Minimal Context Projection
       |
       v
    Ms. Jarvis
       |
       v
 Auditable Response
```

The Guardian evaluates whether a protected operation is permitted.

The Projection Service verifies the resulting authorization and creates the bounded context available to Ms. Jarvis.

The reasoning layer is not an authority oracle. It cannot expand the scope of a valid authorization receipt.

### Current implementation state

The front portion of this trust boundary has been materially implemented and, in several respects, verified end-to-end at the decision boundary.

The remediation history establishes:

- caller-identity authentication before protected decision logic;
- fail-closed `401` behavior for missing or invalid caller credentials;
- runtime admission enforcement;
- fail-closed admission when required authority configuration is absent or invalid;
- signed operation-intent verification, including denial of tampered or untrusted-signature intents;
- binding between the authenticated caller and signed intent subject;
- binding between the signed intent and requested operation;
- caller identity, subject keys, and revocation state sourced from the verified governance-signed Guardian Authority Bundle rather than from separately configured inputs;
- subject and intent revocation checked in the request path, failing closed;
- protected operation handling that does not silently fall back to unrestricted behavior;
- Policy Decision Receipt issuance verified end-to-end under a provisioned Guardian signer, including durable consumption and replay denial.

The complete private-memory projection chain is not yet production-complete, and production Guardian signer enrollment remains outstanding (see §9).

---

## 8. Memory Authorization Receipt

A Memory Authorization Receipt, or MAR, binds user authority, Guardian policy approval, authorized scope, and approved runtime identity.

```
{
  "type": "mountainshares.memory-authorization-receipt/v1",
  "receipt_id": "urn:uuid:<receipt-id>",

  "subject": "did:mountainshares:<user>",
  "recipient": "did:mountainshares:service:<service>",
  "audience_instance": "sha256:<approved-runtime-image-digest>",

  "purpose": "personal-assistant-context",
  "operation": "semantic-retrieval",
  "projection_policy": "redacted-semantic-context",

  "vault_root": "sha256:<signed-vault-root>",
  "authorized_record_refs": [
    "opaque-encrypted-record-reference"
  ],

  "policy_id": "guardian-policy-v1",
  "policy_decision_id": "urn:uuid:<policy-decision-id>",

  "issued_at": "RFC3339 timestamp",
  "expires_at": "RFC3339 timestamp",
  "max_uses": 1,

  "subject_signature": "<user-signature>",
  "guardian_attestation": "<guardian-signature>"
}
```

The Projection Service MUST verify:

- Subject authority.
- Guardian attestation.
- Recipient identity.
- Approved runtime-image binding.
- Purpose and operation scope.
- Projection-policy constraints.
- Expiration.
- Use count.
- Vault-root match.
- Current revocation state.
- Referenced policy and Policy Decision Receipt validity.

Revocation prevents future authorization and decryption. It cannot erase plaintext already disclosed to a recipient.

Short-lived receipts, narrow scopes, minimal projections, and limited plaintext retention reduce exposure.

### Current state

The MAR is a defined authorization layer and receipt infrastructure component.

The remediation history does not establish a fully activated production protected-memory path in which MAR issuance, validation, projection, and recipient runtime admission are all operating as one complete production chain.

Therefore MAR remains part of the remaining closure work even though its surrounding receipt and authorization infrastructure has advanced substantially.

---

## 9. Policy Decision Receipt

The Policy Decision Receipt records the Constitutional Guardian evaluation that authorizes, denies, or marks an operation as indeterminate.

The receipt provides provenance for the decision itself. It MUST NOT store unnecessary plaintext private context. Sensitive policy inputs MUST be represented through encrypted references, redacted fields, or cryptographic commitments.

```
{
  "type": "mountainshares.policy-decision-receipt/v1",
  "decision_id": "urn:uuid:<decision-id>",
  "request_id": "urn:uuid:<request-id>",

  "subject": "did:mountainshares:<user>",
  "recipient": "did:mountainshares:service:<service>",

  "requested_operation": "semantic-retrieval",
  "purpose": "personal-assistant-context",

  "policy_id": "guardian-policy-v1",
  "policy_version": "1.0.0",

  "evaluated_context_commitment":
    "sha256:<canonical-redacted-or-encrypted-context>",

  "decision": "allow",
  "decision_reason": "authorized-purpose-and-valid-subject-consent",

  "constraints": {
    "projection_policy": "redacted-semantic-context",
    "max_uses": 1,
    "expires_at": "RFC3339 timestamp",
    "allowed_record_scope_commitment":
      "sha256:<authorized-scope>"
  },

  "guardian_runtime_digest":
    "sha256:<approved-guardian-image-digest>",

  "issued_at": "RFC3339 timestamp",
  "expires_at": "RFC3339 timestamp",

  "guardian_signature": "<guardian-signature>"
}
```

Valid decision values are:

- `allow`
- `deny`
- `indeterminate`

A decision marked `indeterminate` MUST NOT authorize protected data projection.

The `request_id` binds the decision to one request and supports replay detection.

A MAR derived from a Policy Decision Receipt MUST NOT exceed the scope, lifetime, or use count established by that receipt.

### Current implementation state

The PDR architecture has progressed substantially beyond the original conceptual state, and the issuance path is now verified end-to-end under a provisioned Guardian signer.

The trust-receipt work established:

- PDR schema and validation infrastructure;
- receipt verification and binding requirements;
- issuance infrastructure;
- durable consumption/ledger mechanisms;
- fail-closed behavior when required signer authority is unavailable;
- negative security validation around invalid or untrusted signer conditions.

Verification has additionally demonstrated the complete decision-boundary path: on a valid, authorized request the Guardian issues a schema-valid, cryptographically signed PDR bound to the verified operation intent; the issued receipt is durably consumed; and a replay of the same intent is denied. This was demonstrated with a provisioned (ephemeral, test) Guardian signer whose public key carried the `guardian` role in the trusted registry.

The Guardian therefore does not treat a policy `allow` as sufficient by itself to authorize a protected operation.

A valid PDR must be cryptographically issued under the required Guardian authority.

### Production authority remains incomplete

The remediation history explicitly preserves a distinction between a verified PDR issuance path and a production Guardian signing *authority*.

The production Guardian PDR signer is not yet established as a trusted production authority in the required signer registry. The production trusted-key registry currently contains only the operations-approver and security-approver runtime approval identities; the `guardian-pdr-ed25519-v1` signer is not enrolled, so a live production request would correctly fail closed with an untrusted-signer denial.

The correct behavior is therefore fail closed rather than manufacturing or accepting an unauthorized PDR.

Accordingly:
> The PDR issuance path is implemented and verified end-to-end under a provisioned signer; enrolling a production Guardian signer in the production trusted registry remains the outstanding activation requirement.
---

## 10. Projection Receipt

A Projection Receipt records the transformation from an authorized data scope into the context supplied to a reasoning system.

It answers the question:
> What information actually crossed the protected vault boundary into the reasoning boundary?

A Projection Receipt MUST be created whenever protected vault material is transformed into a reasoning-context projection.

```
{
  "type": "mountainshares.projection-receipt/v1",

  "projection_id": "urn:uuid:<projection-id>",
  "mar_id": "urn:uuid:<memory-authorization-receipt-id>",
  "policy_decision_id": "urn:uuid:<policy-decision-id>",

  "source_vault_root": "sha256:<signed-vault-root>",
  "source_scope_commitment": "sha256:<authorized-record-set>",

  "projection_type": "redacted-semantic-context",
  "projection_policy": "redacted-semantic-context",

  "records_released": 3,
  "tokens_released": 1200,

  "recipient_runtime_digest":
    "sha256:<approved-jarvis-runtime-image>",
  "projection_runtime_digest":
    "sha256:<approved-projection-service-image>",

  "created_at": "RFC3339 timestamp",
  "expires_at": "RFC3339 timestamp",

  "projection_output_commitment":
    "sha256:<canonical-projection-output>",

  "projection_signature": "<projection-service-signature>"
}
```

The Projection Receipt MUST:

- Reference a valid, unexpired MAR.
- Bind the released projection to the MAR's approved vault root and scope.
- Identify the approved runtime that received the projection.
- Identify the approved projection-service runtime that generated it.
- Record the projection type and minimization policy.
- Commit to the canonical projection output without requiring publication of its plaintext.
- Expire no later than the associated MAR.
- Be auditable without becoming a second plaintext memory store.

### Current state

Projection Receipt architecture remains defined.

The remediation history does not establish complete production activation of:

- the Projection Service;
- its runtime-authority chain;
- protected retrieval;
- complete MAR validation at the projection boundary;
- recipient-runtime binding;
- projection-output commitment;
- full protected-memory isolation from unrestricted reasoning access.

These remain explicit Chapter 54 closure requirements.

---

## 11. Constitutional Guardian Contract

The Constitutional Guardian decides whether a protected capability may be exercised.

The following capabilities MUST fail closed when no valid Policy Decision Receipt or authorization receipt exists:

- Protected data projection.
- Private-memory retrieval.
- Identity verification.
- Signature verification.
- Commons contribution.
- Governance action.
- Protected citizen or member data access.
- Release approval and runtime admission.

A general chat interface may remain available during a Guardian outage only if it does not access protected user memory, protected identity data, protected Commons functions, or governance capabilities.

```
Guardian available + policy approves -> issue Policy Decision Receipt
                                      -> issue MAR
                                      -> permit bounded projection

Guardian denies                      -> disclose nothing

Guardian indeterminate               -> disclose nothing

Guardian unavailable                 -> no receipt
                                      -> protected capability unavailable
```

The system MAY provide a clearly labeled, non-personalized response when protected capabilities are unavailable.

It MUST NOT silently degrade into unauthorized private-memory access.

### Current implementation state

The Guardian boundary is no longer merely conceptual.

The remediation history establishes implementation and verification of:

- runtime admission;
- caller authentication;
- signed operation-intent verification, including tampered- and untrusted-signature denial;
- caller/subject binding;
- request/operation binding;
- fail-closed admission;
- caller, subject-key, and revocation authority sourced from the verified governance-signed Guardian Authority Bundle;
- subject and intent revocation enforcement at the decision boundary;
- protected operation routing;
- PDR issuance verified end-to-end under a provisioned signer, with durable consumption and replay denial;
- negative security cases in which required trust conditions are absent.

The Guardian therefore represents a materially implemented and tested trust boundary.

However, the Guardian is not yet a fully activated production authority for the complete protected-memory architecture.

Production PDR signer enrollment, production governance-board authority, a production authority bundle, complete projection admission, and the remaining Chapter 54 closure requirements remain outstanding.

---

## 12. Commons Contribution Domain

The Commons receives explicitly authorized transformations, not raw private-vault graphs.

```
Private Vault -> User-approved transformation -> Contribution Receipt
              -> Transformation Receipt -> Aggregation
              -> Commons Epoch Root -> Governance Decision
```

Each Commons Transformation Receipt MUST identify:

- Authorized input commitment.
- Output aggregate commitment.
- Approved transformation algorithm and version.
- Applicable data schema.
- Privacy mechanism.
- Minimum cohort threshold.
- Applicable policy.
- Approved executing runtime.
- Timestamp.
- Required governance and privacy attestations.

A Commons Merkle root proves a committed aggregate history.

It does not itself prove anonymization, non-discrimination, legal compliance, or ethical legitimacy.

Those require a specified transformation, policy decision, privacy control, and reviewable governance process.

The Commons MUST NOT ingest raw private-vault graphs merely because a user has interacted with Ms. Jarvis.
> Interaction history with Ms. Jarvis is not itself a contribution authorization event.

### Current state

The Commons architecture remains defined, but the remediation history does not establish full production implementation and authorization of:

- Contribution Receipts;
- Transformation Receipts;
- Commons Epoch Root governance;
- privacy attestations;
- complete contribution authorization;
- production governance approval of Commons transformations.

These remain outstanding.

---

## 13. Receipts and Audit

Required receipt and governance-authority classes include:

- Guardian Authority Bundle.
- Runtime Authority Manifest.
- Memory Authorization Receipt.
- Policy Decision Receipt.
- Projection Receipt.
- Response Receipt.
- Contribution Receipt.
- Commons Transformation Receipt.
- Commons Epoch Root Record.
- Revocation Receipt.

Each receipt or authority artifact MUST have:

- A schema version.
- An immutable identifier.
- An issuer identity.
- A timestamp.
- A policy reference where applicable.
- An integrity commitment.
- A verifiable signature or attestation.
- Clear retention and revocation semantics.

The Guardian Authority Bundle additionally carries a threshold set of governance approvals rather than a single issuer signature, and expresses revocation state inline so that revocation inherits the same governance signature as the authority it governs.

Audit records MUST minimize personal data.

Auditability is not permission to create a parallel surveillance database.

### Evidence and sealing

The Stage 6 development process has established evidence capture, reproducibility capture, trust gates, review gates, promotion seals, and durable evidence artifacts as part of the project's development discipline.

This means that verification claims should be tied to preserved evidence rather than to an unrecorded statement that a test once passed.

The same principle applies to architecture documentation:
> A documented capability MUST NOT be described as production-authorized merely because an implementation or test exists.

A capability may instead be described as:

- defined;
- implemented;
- verified;
- sealed;
- promoted;
- production-authorized.

These are distinct states.

---

## 14. Current Implementation and Verification Alignment

| Component                            | Current state                                                                                                                                                                                            |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Constitutional Guardian              | **Implemented and materially hardened.** Runtime admission, caller authentication, signed operation-intent enforcement, authority-bundle sourcing, revocation enforcement, and fail-closed protected decision boundaries are implemented. |
| Guardian Authority Bundle            | **Implemented and verified at the decision boundary.** Three-role threshold verification and caller/subject-key/revocation sourcing demonstrated under test-provisioned governance keys. A production bundle signed by the established governance board remains pending. |
| Runtime Authority Manifest           | **Implemented and cryptographically verified in the trust-development chain.** Evidence has been preserved/sealed. Final production authorization remains gated.                                         |
| Runtime Admission                    | **Implemented and verified.** The protected runtime boundary fails closed when required authority conditions are absent or invalid.                                                                      |
| Caller Identity Authentication       | **Implemented and verified.** `/constitutional/check` authenticates the caller before protected decision logic and fails closed on missing/invalid caller credentials. Caller identities are sourced from the verified authority bundle. |
| Signed Operation Intent              | **Implemented and verified at the protected decision boundary.** Caller, subject, request, and operation bindings are enforced; tampered- and untrusted-signature and inactive-subject-key intents are denied. |
| Policy Decision Receipt schema       | **Implemented.** Trust-receipt schema and validation infrastructure exist.                                                                                                                               |
| Policy Decision Receipt verification | **Implemented.** Cryptographic and structural verification/binding infrastructure exists.                                                                                                                |
| Policy Decision Receipt issuance     | **Implemented and verified end-to-end under a provisioned signer.** Issue, durable-consume, and replay-deny demonstrated. Production issuance remains dependent on a trusted production Guardian signer. |
| Guardian PDR signing authority       | **Not production-authorized.** The issuance path is verified; a production Guardian signer enrolled in the production trusted registry (with the `guardian` role) remains the outstanding activation gate. |
| Existing runtime approver keys       | **Verified.** Existing security and operations approval identities have been validated against their registered public-key material.                                                                     |
| Runtime approval chain               | **Verified for the implemented development/release boundary.** The stronger final production governance boundary remains outstanding.                                                                    |
| Production governance policy         | **Not yet fully established as production authority.** Existing policy artifacts must not be mistaken for final production governance activation.                                                        |
| Governance-board authority           | **Not yet established for final production activation.** No production `governance-board` signer has been enrolled.                                                                                       |
| Memory Authorization Receipt         | **Defined and supported by receipt infrastructure; complete protected-memory production path remains pending.**                                                                                          |
| Projection Receipt                   | **Defined; complete production projection boundary remains pending.**                                                                                                                                    |
| Projection Service                   | **Not production-activated.** Runtime admission and protected retrieval integration remain outstanding.                                                                                                  |
| Chroma / semantic memory             | **Existing semantic-memory capability.** Protected data must remain behind the authorization/projection boundary.                                                                                        |
| Hilbert People Space                 | **Existing implementation/conceptual layer.** It must operate as a bounded projection/indexing layer rather than unrestricted private-memory authority.                                                  |
| BBB / disclosure boundary            | **Existing safety/disclosure boundary.** Full receipt-aware protected-memory integration remains part of the closure path.                                                                               |
| Commons Contribution Receipts        | **Defined; production implementation remains pending.**                                                                                                                                                  |
| Commons Transformation Receipts      | **Defined; production implementation remains pending.**                                                                                                                                                  |
| Commons Epoch Roots                  | **Defined; production governance integration remains pending.**                                                                                                                                          |
| Revocation                           | **Implemented and verified at the decision boundary.** Subject and intent revocation are sourced from the signed authority bundle and fail closed. Integration into the protected-memory/projection path remains pending. |
| Durable receipt/consumption ledger   | **Implemented and verified.** Durable consumption and replay denial demonstrated within the trust-receipt development work.                                                                              |
| Trust gates                          | **Implemented and exercised.**                                                                                                                                                                           |
| Reproducibility capture              | **Completed for the applicable development stage.**                                                                                                                                                      |
| Promotion seals                      | **Completed for applicable completed stages.**                                                                                                                                                           |
| Negative security cases              | **Validated for the completed trust-boundary work.**                                                                                                                                                     |
| Adversarial verification matrix      | **Partially closed.** Decision-boundary cases verified (unregistered caller, missing/tampered/mismatched intent, inactive subject key, subject and intent revocation, PDR replay). Remaining cells — expiration, policy-version mismatch, unapproved-image, Guardian outage — and the full projection chain remain. |
| Custodian ceremony                   | **Started; not complete.** Custodian 1 has enrolled 4 of 11 required public enrollment records. At least two independent custodians, the remaining records, and a threshold-signed production authority/governance registry remain. Grants no authority. |
| Release-candidate evidence           | **Completed as a tested, evidence-backed, fail-closed package.** Commitment `sha256:f805a817…`; `AUTHORITY_STATUS: INACTIVE`; `DEPLOYMENT_ADMISSION: BLOCKED`; no private keys in the package.            |
| Live authority system                | **Not active.** Deployment remains intentionally blocked pending governance, signing, projection, and final activation prerequisites.                                                                    |

This table distinguishes architecture, implementation, verification, evidence, promotion, and production authority.

A declared component is not automatically running.

An implemented component is not automatically production-authorized.

A verified component is not automatically production-authorized.

A sealed evidence artifact is not automatically production-authorized.

A release candidate is not automatically an active authority system.

---

## 15. Verification Requirements

| Capability                  | Required proof                                                                                                      | Current status                                                                                      |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Approved production service | Pinned digest, SBOM, runtime manifest, release approvals, health checks, contract checks                            | **Partially demonstrated; final production release closure remains**                                |
| Runtime authority           | Valid signed manifest, trusted signers, policy compatibility, image binding                                         | **Signature verification and admission evidence demonstrated; final production governance remains** |
| Guardian authority bundle   | Governance-signed bundle meeting `minimum_approvals` and `required_roles`, verified approver keys, valid expiry     | **Threshold verification demonstrated under test-provisioned governance keys; production bundle remains** |
| Caller authenticity         | Valid caller credential (bundle-sourced) before protected decision logic                                            | **Implemented and verified fail-closed**                                                            |
| Signed operation intent     | Valid subject signature, trusted subject key, operation binding, caller/subject binding                             | **Implemented and verified fail-closed; tampered/mismatched/inactive-key denials verified**         |
| PDR issuance                | Valid Guardian signer, trusted registry entry, policy binding, durable consumption, cryptographic signature         | **End-to-end issuance, durable consumption, and replay denial verified under a provisioned signer; production signer enrollment remains blocked** |
| Private-memory access       | Valid MAR, valid PDR, vault-root match, recipient/runtime binding, unexpired scope                                  | **Not fully production-closed**                                                                     |
| Semantic projection         | Projection Receipt with source commitments, purpose, minimization policy, expiry, output commitment, and use record | **Not fully production-closed**                                                                     |
| Commons contribution        | User authorization, valid Contribution Receipt, applicable PDR                                                      | **Pending**                                                                                         |
| Commons transformation      | Transformation Receipt, approved runtime digest, privacy mechanism, cohort threshold, required attestations         | **Pending**                                                                                         |
| Governance decision         | Epoch root, approved aggregation method, policy record, required signatures                                         | **Pending full production integration**                                                             |
| Revocation                  | Current revocation-state check before every new protected projection                                                | **Subject and intent revocation verified at the decision boundary via the signed bundle; projection-path integration pending** |
| Guardian outage             | Protected capability denial; no fallback to unapproved data access                                                  | **Fail-closed behavior implemented in the applicable trust path**                                   |
| Unapproved runtime          | Receipt verification failure and denial of protected projection                                                     | **Runtime admission boundary implemented; full protected projection path remains**                  |
| Receipt replay              | Request binding, expiry, use-count enforcement, replay detection                                                    | **Replay denial verified end-to-end via durable PDR consumption; full production-chain closure remains** |

---

## 16. Pilot Implementation and Closure Order

The original architecture remains the governing roadmap, but the starting point has advanced substantially because several foundational stages are now implemented and verified.

### Completed or materially advanced

1. Define governance roles, keys, policy versions, threshold requirements, and failure-mode requirements.
2. Define runtime-authority structures.
3. Implement runtime-authority signature verification.
4. Establish runtime admission enforcement.
5. Establish Guardian admission evidence.
6. Establish trust gates and reproducibility capture.
7. Establish evidence sealing and applicable promotion gates.
8. Implement caller authentication.
9. Implement signed operation-intent verification and binding, including tampered/mismatched/inactive-key denial.
10. Implement trust-receipt schemas and verification infrastructure.
11. Implement durable receipt/consumption ledger behavior and verify replay denial.
12. Implement and verify the end-to-end PDR issuance path under a provisioned signer.
13. Implement the governance-signed Guardian Authority Bundle, its three-role threshold verification, and bundle-sourced caller/subject-key/revocation authority.
14. Enforce subject and intent revocation at the decision boundary.
15. Validate decision-boundary adversarial cases (unregistered caller, missing/tampered/mismatched intent, inactive subject key, subject and intent revocation, PDR replay).
16. Validate negative security cases around the completed trust boundaries.
17. Initiate the human custodian ceremony (Custodian 1 enrollment) without activating any authority.
18. Produce evidence-backed release-candidate artifacts without activating production authority.

### Remaining closure work

The remaining work MUST preserve the same fail-closed discipline.

1. Establish the authorized production governance decision and corresponding production policy registry.
2. Establish the required production governance-board authority and enroll a real `governance-board` signer.
3. Establish dedicated Guardian PDR signing authority and enroll it, with the `guardian` role, in the production trusted signer registry.
4. Produce a production Guardian Authority Bundle carrying a genuine three-role threshold of production approvals.
5. Complete production Guardian authority activation and demonstrate a live, cryptographically valid PDR issuance path against production authority.
6. Establish signed runtime-admission chains for the Projection Service and reasoning recipient.
7. Implement and verify MAR issuance and validation in the protected-memory path.
8. Implement Projection Service verification before protected retrieval.
9. Remove unrestricted private-memory access from reasoning paths.
10. Implement and verify Projection Receipts and their output commitments.
11. Implement Contribution and Transformation Receipts before publishing Commons aggregates.
12. Establish Commons Epoch Root and governance integration.
13. Integrate revocation state into the protected-memory/projection authorization checks (beyond the decision boundary already covered).
14. Close the remaining adversarial verification cells across the complete production chain:
  - expiration;
  - policy-version mismatch;
  - unapproved-image access;
  - Guardian outage;
  - and the full projection/MAR chain for the cases already closed at the decision boundary.
15. Build and verify one reproducible pilot release from a fully governed signed Runtime Authority Manifest.
16. Complete the human governance and custodian ceremony for actual activation — at least two independent custodians and the remaining public enrollment records (7 of 11 outstanding), culminating in a threshold-signed active governance registry.
17. Demonstrate durable shared-ledger conformance before multi-replica deployment where required by the final release boundary.

These remaining requirements MUST NOT be inferred to be complete merely because their supporting infrastructure exists.

---

## 17. Current Release Boundary

The current system state MUST be described as:
> **A tested, evidence-backed, fail-closed release candidate rather than a live authority system.**

The remediation history establishes an intentionally inactive production authority boundary. The final release-candidate evidence package records this explicitly:

- Release-candidate commitment: `sha256:f805a817…`
- `AUTHORITY_STATUS: INACTIVE`
- `DEPLOYMENT_ADMISSION: BLOCKED`
- Private keys in the package: none.

The custodian ceremony has begun but is not complete: Custodian 1 has enrolled four public records (emergency-revoker, governance-steward, policy-approver, release-approver); at least two independent custodians and seven further enrollment records remain before an active governance registry can be threshold-signed. Beginning the ceremony grants no authority.

A candidate Guardian deployment topology exists but is intentionally not deployable: it references a Guardian PDR signer absent from the trusted registry, and the running topology is deliberately unprovisioned, so the current deployment fails closed.

The public evidence package is designed to contain the relevant non-secret evidence while excluding:

- private keys;
- passphrases;
- seeds;
- runtime secrets;
- signer material;
- other sensitive authority material.

The release-candidate evidence therefore demonstrates implementation, testing, provenance, and fail-closed behavior without granting production authority.

This distinction is deliberate.

The architecture is designed to stop before live authority is granted when required governance, signing, registry, runtime, or projection conditions are absent.

---

## 18. Status Interpretation

For documentation and future audit purposes, the following terminology is normative.

### Defined

The architecture, schema, contract, or requirement has been specified.

### Implemented

A concrete software or artifact mechanism exists in the system.

### Verified

The implementation has produced evidence demonstrating the required behavior or cryptographic property.

### Sealed

The relevant evidence has been preserved as an identifiable, integrity-bound artifact in the development history.

### Promoted

The relevant stage has passed its defined promotion gate and has been recorded as such.

### Production-authorized

The required governance authority, signing authority, runtime admission, policy, and activation conditions exist and have been explicitly authorized.

These states MUST NOT be conflated.

In particular:
> **Implemented does not mean production-authorized.**
> **Verified does not mean production-authorized.**
> **Sealed evidence does not mean production-authorized.**
> **Promoted does not mean production-authorized.**
> **A release candidate does not mean an active authority system.**

This distinction is fundamental to the MountainShares / Ms. Jarvis trust architecture.

---

## 19. Final Architectural Position

The architecture has progressed beyond a purely conceptual trust model.

The current system contains meaningful, evidence-backed implementation of the trust boundary around:

- runtime authority;
- signed runtime admission;
- Guardian admission enforcement;
- caller authentication;
- signed operation-intent verification, including tampered/mismatched/inactive-key denial;
- the governance-signed Guardian Authority Bundle and its three-role threshold verification;
- subject and intent revocation enforcement at the decision boundary;
- fail-closed protected decision paths;
- Policy Decision Receipt schema, verification infrastructure, and end-to-end issuance verified under a provisioned signer with replay denial;
- durable receipt-consumption infrastructure;
- trust gates;
- reproducibility capture;
- evidence sealing;
- applicable stage promotion;
- negative security validation;
- non-authorizing release-candidate packaging.

These accomplishments materially change the implementation status from the original architecture snapshot.

However, the architecture deliberately preserves the remaining boundaries around:

- final production governance authority;
- a production governance-board signer;
- a production Guardian PDR signer enrolled in the production trusted registry;
- a production Guardian Authority Bundle carrying genuine three-role approvals;
- production policy registries;
- Projection Service admission;
- reasoning-runtime admission;
- complete MAR activation;
- protected semantic projection;
- unrestricted-memory removal;
- Commons contribution and transformation receipts;
- revocation integration into the protected-memory/projection path;
- the remaining adversarial verification cells;
- final reproducible pilot-release authorization;
- completion of the human custodian/governance activation ceremony.

The result is not an architecture claiming completion prematurely.

It is an architecture in which the remaining work can now be expressed as explicit authority, implementation, and verification gates rather than unspecified future architecture.

The governing principle remains unchanged:
> **Integrity proves what happened. Authority proves who may cause it. Policy proves whether it was allowed.**

The documentation therefore records both sides of the current state:

**What has actually been built, tested, verified, sealed, and promoted; and what remains deliberately blocked because the required authority has not yet been established.**

That distinction is itself part of the trust architecture.
