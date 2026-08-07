# MountainShares / Ms. Jarvis Trust Architecture v1.0

**Status:** Architecture Freeze Candidate  
**Authority:** Canonical design reference for pilot trust-boundary work  
**Date:** 2026-08-07  
**Scope:** Software provenance, user sovereignty, Commons integrity, and policy-governed AI projections.

## 1. Core Principle

> Integrity proves what happened. Authority proves who may cause it. Policy proves whether it was allowed.

Merkle structures provide tamper-evident integrity evidence. Cryptographic keys and signatures establish attributable authority. The Constitutional Guardian evaluates applicable policy. A runtime may act on protected data only when it can verify an unexpired authorization receipt issued under the applicable policy.

A hash, CID, file, image, container, record, or service does not become authoritative merely because it exists or can be referenced.

A Merkle root without a valid controlling signature, timestamp context, and governance interpretation is only an integrity commitment. It has no authority value on its own.

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

## 3. Trust Domains

```text
                         GOVERNANCE PLANE
      Keys -  Roles -  Policies -  Threshold Approvals -  Revocation
                                |
                                v
                     POLICY DECISION ENGINE

     -----------------------------------------------------------
     |                         |                               |
     v                         v                               v
SOFTWARE PROVENANCE       USER SOVEREIGNTY              COMMONS INTEGRITY
Build Merkle Tree         Vault Merkle Tree             Epoch Merkle Tree
```

The domains may reference each other through signed receipts, but no domain inherits authority merely from a reference.

## 4. Governance Plane

The governance plane defines:

- Authorized signing identities and key rotation rules.
- Roles, delegation limits, and threshold-approval requirements.
- Versioned policies and policy-decision semantics.
- Revocation, incident response, and audit-retention rules.
- Required review procedures for high-impact actions.
- Which protected capabilities fail closed.
- The authority required to approve a runtime, policy, transformation, or Commons governance action.

A Merkle root is evidence. Governance keys, role assignments, policies, and verified signatures are the authority layer.

The Policy Decision Engine evaluates requests against the active policy set. It does not replace human governance. It applies the policies and delegations established by governance.

## 5. Software Provenance Domain

The software provenance domain establishes which artifacts are approved to execute.

```text
Source -> Commit -> Build Recipe -> SBOM -> Image Digest
      -> Runtime Authority Manifest -> Deployment Approval -> Running Service
```

A pilot Runtime Authority Manifest MUST:

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

## 6. User Sovereignty Domain

```text
Private User Vault -> Signed Vault Root -> Authorization Receipt
                  -> Projection Service -> Ms. Jarvis Reasoning -> Response Receipt
```

> Ms. Jarvis does not possess user memory. Ms. Jarvis receives authorized projections of user memory.

Private records MUST be encrypted before content-addressed storage. Vault roots SHOULD be private by default. Public commitments MUST contain no plaintext private memory, predictable identifiers, wallet addresses, social handles, or other correlatable low-entropy values.

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

## 7. Operational Trust Boundary

```text
                  USER REQUEST
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
        +--------------+--------------+
        |                             |
        v                             v
Encrypted User Vault            Audit Receipts
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

The Guardian evaluates whether a protected operation is permitted. The Projection Service verifies the resulting authorization and creates the bounded context available to Ms. Jarvis.

The reasoning layer is not an authority oracle. It cannot expand the scope of a valid authorization receipt.

## 8. Memory Authorization Receipt

A Memory Authorization Receipt, or MAR, binds user authority, Guardian policy approval, authorized scope, and approved runtime identity.

```json
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

Revocation prevents future authorization and decryption. It cannot erase plaintext already disclosed to a recipient. Short-lived receipts, narrow scopes, minimal projections, and limited plaintext retention reduce exposure.

## 9. Policy Decision Receipt

The Policy Decision Receipt records the Constitutional Guardian evaluation that authorizes, denies, or marks an operation as indeterminate.

The receipt provides provenance for the decision itself. It MUST NOT store unnecessary plaintext private context. Sensitive policy inputs MUST be represented through encrypted references, redacted fields, or cryptographic commitments.

```json
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

  "evaluated_context_commitment": "sha256:<canonical-redacted-or-encrypted-context>",
  "decision": "allow",
  "decision_reason": "authorized-purpose-and-valid-subject-consent",

  "constraints": {
    "projection_policy": "redacted-semantic-context",
    "max_uses": 1,
    "expires_at": "RFC3339 timestamp",
    "allowed_record_scope_commitment": "sha256:<authorized-scope>"
  },

  "guardian_runtime_digest": "sha256:<approved-guardian-image-digest>",
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

The `request_id` binds the decision to one request and supports replay detection. A MAR derived from a Policy Decision Receipt MUST not exceed the scope, lifetime, or use count established by that receipt.

## 10. Projection Receipt

A Projection Receipt records the transformation from an authorized data scope into the context supplied to a reasoning system.

It answers the question:

> What information actually crossed the protected vault boundary into the reasoning boundary?

A Projection Receipt MUST be created whenever protected vault material is transformed into a reasoning-context projection.

```json
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

  "recipient_runtime_digest": "sha256:<approved-jarvis-runtime-image>",
  "projection_runtime_digest": "sha256:<approved-projection-service-image>",

  "created_at": "RFC3339 timestamp",
  "expires_at": "RFC3339 timestamp",

  "projection_output_commitment": "sha256:<canonical-projection-output>",
  "projection_signature": "<projection-service-signature>"
}
```

The Projection Receipt MUST:

- Reference a valid, unexpired MAR.
- Bind the released projection to the MAR’s approved vault root and scope.
- Identify the approved runtime that received the projection.
- Identify the approved projection-service runtime that generated it.
- Record the projection type and minimization policy.
- Commit to the canonical projection output without requiring publication of its plaintext.
- Expire no later than the associated MAR.
- Be auditable without becoming a second plaintext memory store.

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

```text
Guardian available + policy approves -> issue Policy Decision Receipt
                                      -> issue MAR
                                      -> permit bounded projection

Guardian denies                      -> disclose nothing

Guardian indeterminate               -> disclose nothing

Guardian unavailable                 -> no receipt
                                      -> protected capability unavailable
```

The system MAY provide a clearly labeled, non-personalized response when protected capabilities are unavailable. It MUST NOT silently degrade into unauthorized private-memory access.

## 12. Commons Contribution Domain

The Commons receives explicitly authorized transformations, not raw private-vault graphs.

```text
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

A Commons Merkle root proves a committed aggregate history. It does not itself prove anonymization, non-discrimination, legal compliance, or ethical legitimacy. Those require a specified transformation, policy decision, privacy control, and reviewable governance process.

The Commons MUST NOT ingest raw private-vault graphs merely because a user has interacted with Ms. Jarvis.

> Interaction history with Ms. Jarvis is not itself a contribution authorization event.

## 13. Receipts and Audit

Required receipt classes:

- Runtime Authority Manifest.
- Memory Authorization Receipt.
- Policy Decision Receipt.
- Projection Receipt.
- Response Receipt.
- Contribution Receipt.
- Commons Transformation Receipt.
- Commons Epoch Root Record.
- Revocation Receipt.

Each receipt MUST have:

- A schema version.
- An immutable identifier.
- An issuer identity.
- A timestamp.
- A policy reference where applicable.
- An integrity commitment.
- A verifiable signature or attestation.
- Clear retention and revocation semantics.

Audit records MUST minimize personal data. Auditability is not permission to create a parallel surveillance database.

## 14. Current Implementation Alignment

| Component | Current state |
|---|---|
| Constitutional Guardian | Implemented in the existing system; fail-closed hardening for protected capabilities is required |
| Runtime Authority Manifest | Conceptually defined; not yet canonicalized as a signed pilot-release artifact |
| Software provenance chain | Partial; active runtime discovery exists, but release workflow, SBOM policy, and signed manifest remain incomplete |
| User Vault Merkle Root | Architecture defined; implementation pending |
| Memory Authorization Receipt | Architecture and initial payload shape defined; schema and implementation pending |
| Policy Decision Receipt | Architecture and initial payload shape defined; schema and implementation pending |
| Projection Receipt | Architecture and initial payload shape defined; schema and implementation pending |
| Projection Service | Architecture defined; implementation pending |
| Chroma and semantic memory | Existing semantic-memory capability; must be placed behind projection and authorization boundaries for protected data |
| Hilbert People Space | Existing conceptual and implementation layer; must operate as a projection/indexing layer rather than unrestricted private-memory authority |
| BBB | Existing disclosure and safety concept; must enforce receipt-aware protected-data boundaries where applicable |
| Commons Transformation Receipts | Architecture defined; implementation pending |
| Commons Epoch Roots | Architecture defined; implementation pending |
| Signed pilot release manifest | Pending |
| Full pilot verification suite | Pending |

This table distinguishes architecture intent from demonstrated implementation. A declared or built component is not automatically running, called, verified, or fail-safe.

## 15. Verification Requirements

| Capability | Required proof |
|---|---|
| Approved production service | Pinned digest, SBOM, runtime manifest, release approvals, health checks, contract checks |
| Private-memory access | Valid MAR, valid Policy Decision Receipt, vault-root match, recipient/runtime binding, unexpired scope |
| Semantic projection | Projection Receipt with source commitments, purpose, minimization policy, expiry, output commitment, and use record |
| Commons contribution | User authorization, valid Contribution Receipt, applicable Policy Decision Receipt |
| Commons transformation | Transformation Receipt, approved runtime digest, stated privacy mechanism, cohort threshold, required attestations |
| Governance decision | Epoch root, approved aggregation method, policy record, required signatures |
| Revocation | Current revocation-state check before every new protected projection |
| Guardian outage | Protected capability denial; no fallback to unapproved data access |
| Unapproved runtime | Receipt verification failure and denial of protected projection |
| Receipt replay | Request binding, expiry, use-count enforcement, and replay detection |

## 16. Pilot Implementation Order

1. Define governance roles, keys, policy versions, threshold requirements, and the failure-mode matrix.
2. Produce a signed Runtime Authority Manifest for the pilot deployment.
3. Define JSON Schemas for MARs, Policy Decision Receipts, Projection Receipts, Contribution Receipts, Transformation Receipts, Runtime Authority Manifests, and Revocation Receipts.
4. Implement schema validation and signature verification.
5. Implement Guardian issuance of short-lived Policy Decision Receipts and MARs.
6. Implement Projection Service verification of MARs before protected retrieval.
7. Remove unrestricted private-memory access from reasoning paths.
8. Implement Contribution and Transformation Receipts before publishing Commons aggregates.
9. Test denial, expiration, replay, revocation, policy-version mismatch, unapproved-image access, invalid signature, and Guardian-outage cases.
10. Build and verify one reproducible pilot release from a signed Runtime Authority Manifest.

## 17. Governing Rule

> Every request for protected memory must produce a verifiable answer to: who authorized it, what was authorized, why it was allowed, what was disclosed, which runtime processed it, which policy governed it, and when that authority expired.
