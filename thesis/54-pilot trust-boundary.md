# MountainShares / Ms. Jarvis Trust Architecture v1.0

**Status:** Architecture Specification  
**Authority:** Canonical design reference for pilot trust-boundary work  
**Date:** 2026-08-07  
**Scope:** Software provenance, user sovereignty, Commons integrity, and policy-governed AI projections.

## 1. Core Principle

> Integrity proves what happened. Authority proves who may cause it. Policy proves whether it was allowed.

Merkle structures provide tamper-evident integrity evidence. Cryptographic keys and signatures establish attributable authority. The Constitutional Guardian evaluates applicable policy. A runtime may act on protected data only when it can verify an unexpired authorization receipt issued under the applicable policy.

A hash, CID, file, image, container, record, or service does not become authoritative merely because it exists or can be referenced.

## 2. Trust Domains

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

## 3. Governance Plane

The governance plane defines:

- Authorized signing identities and key rotation rules.
- Roles, delegation limits, and threshold-approval requirements.
- Versioned policies and policy-decision semantics.
- Revocation, incident response, and audit-retention rules.
- Which protected capabilities fail closed.

A Merkle root is evidence. Governance keys, role assignments, policies, and verified signatures are the authority layer.

## 4. Software Provenance Domain

The software provenance domain establishes which artifacts are approved to execute.

```text
Source -> Commit -> Build Recipe -> SBOM -> Image Digest
      -> Runtime Authority Manifest -> Deployment Approval -> Running Service
```

A pilot Runtime Authority Manifest MUST pin immutable image digests, enumerate required services and health contracts, identify approved policy versions, include SBOM references, define dependency failure modes, and carry required release/governance signatures.

`latest` tags, filenames, backup status, and container existence are not authority assertions.

## 5. User Sovereignty Domain

```text
Private User Vault -> Signed Vault Root -> Authorization Receipt
                  -> Projection Service -> Ms. Jarvis Reasoning -> Response Receipt
```

> Ms. Jarvis does not possess user memory. Ms. Jarvis receives authorized projections of user memory.

Private records MUST be encrypted before content-addressed storage. Vault roots SHOULD be private by default. Public commitments MUST contain no plaintext private memory, predictable identifiers, wallet addresses, or other correlatable low-entropy values.

The reasoning system MUST NOT receive long-lived vault keys or unrestricted semantic-store access. It receives the minimum projection necessary for the approved purpose.

## 6. Memory Authorization Receipt

A Memory Authorization Receipt (MAR) binds user authority, Guardian policy approval, authorized scope, and approved runtime identity.

```json
{
  "type": "mountainshares.memory-authorization-receipt/v1",
  "receipt_id": "urn:uuid:<receipt-id>",
  "subject": "did:mountainshares:<user>",
  "recipient": "did:mountainshares:service:<service>",
  "audience_instance": "sha256:<approved-image-digest>",
  "purpose": "personal-assistant-context",
  "operation": "semantic-retrieval",
  "projection_policy": "redacted-semantic-context",
  "vault_root": "sha256:<signed-vault-root>",
  "authorized_record_refs": ["opaque-encrypted-record-reference"],
  "policy_id": "guardian-policy-v1",
  "policy_decision_id": "urn:uuid:<decision-id>",
  "issued_at": "RFC3339 timestamp",
  "expires_at": "RFC3339 timestamp",
  "max_uses": 1,
  "subject_signature": "<user-signature>",
  "guardian_attestation": "<guardian-signature>"
}
```

The projection service MUST verify subject authority, Guardian attestation, recipient and runtime-image binding, purpose, expiry, use count, vault root, and revocation state before releasing protected material.

Revocation prevents future authorization and decryption. It cannot erase plaintext already disclosed to a recipient; short-lived receipts and minimal projections limit that exposure.

## 7. Constitutional Guardian Contract

The Constitutional Guardian decides whether a protected capability may be exercised. Protected data projection, private-memory retrieval, identity verification, signature verification, Commons contribution, and governance action MUST fail closed when no valid policy decision or authorization receipt exists.

A general chat interface may remain available during a Guardian outage only if it does not access protected user memory, protected identity data, or Commons contribution functions.

```text
Guardian available + policy approves -> issue MAR -> permit bounded projection
Guardian denies                  -> disclose nothing
Guardian unavailable             -> no MAR -> protected capability unavailable
```

## 8. Commons Contribution Domain

The Commons receives explicitly authorized transformations, not raw private-vault graphs.

```text
Private Vault -> User-approved transformation -> Contribution Receipt
              -> Aggregation -> Commons Epoch Root -> Governance Decision
```

Each transformation receipt MUST identify the authorized input commitment, output aggregate commitment, approved algorithm and version, privacy mechanism, minimum cohort threshold, applicable policy, executing approved runtime, timestamp, and required governance/privacy attestations.

A Commons Merkle root proves a committed aggregate history. It does not itself prove anonymization or ethical legitimacy; those require a specified transformation, policy decision, and reviewable privacy controls.

## 9. Receipts and Audit

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

Each receipt MUST have a schema version, immutable identifier, issuer identity, timestamp, policy reference where applicable, integrity commitment, and verifiable signature or attestation.

## 10. Verification Requirements

| Capability | Required proof |
|---|---|
| Approved production service | Pinned digest, SBOM, runtime manifest, release approvals, health and contract checks |
| Private-memory access | Valid MAR, policy decision, vault-root match, recipient/runtime binding, unexpired scope |
| Semantic projection | Projection receipt with source commitments, purpose, minimization policy, and expiry |
| Commons contribution | User authorization plus contribution and transformation receipts |
| Governance decision | Epoch root, approved aggregation method, policy record, required signatures |
| Revocation | Current revocation-state check before every new protected projection |

## 11. Pilot Implementation Order

1. Define governance roles, keys, policy versions, and failure-mode matrix.
2. Produce a signed Runtime Authority Manifest for the pilot deployment.
3. Define JSON Schemas for MARs, policy decisions, projections, transformations, and revocations.
4. Implement Guardian issuance and projection-service verification of short-lived MARs.
5. Remove unrestricted private-memory access from reasoning paths.
6. Implement contribution and transformation receipts before publishing Commons aggregates.
7. Test denial, expiry, replay, revocation, policy-version mismatch, unapproved-image, and Guardian-outage cases.

## 12. Governing Rule

> Every request for protected memory must produce a verifiable answer to: who authorized it, what was authorized, why it was allowed, what was disclosed, which runtime processed it, and when that authority expired.
