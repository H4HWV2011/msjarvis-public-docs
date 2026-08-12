# MountainShares / Ms. Jarvis Trust Architecture v1.3

**Status:** Architecture Freeze Candidate — Runtime-Isolation and Production-Closure Update  
**Authority:** Canonical design reference for pilot trust-boundary work  
**Date:** 2026-08-12  
**Supersedes:** v1.2 (2026-08-11)  
**Scope:** Software provenance, runtime authority, user sovereignty, Commons integrity, policy-governed AI projections, receipt-based authorization, runtime isolation, and fail-closed governance boundaries.

---

## Revision Note (v1.2 → v1.3)

This revision incorporates the verified privacy-gateway runtime-isolation pilot into the architecture’s implementation and release-boundary record.

It does not activate production authority, authorize protected-memory access, establish production governance, or change the architecture’s non-goals. It records a verified local runtime baseline and clarifies that production progress now depends primarily on governance authority, signer enrollment, governed release provenance, approved secret delivery, and completion of the protected-memory projection chain.

Concrete updates in this revision:

1. **Runtime-isolation pilot verified.** A pilot Redis, egress, admission API, and privacy-worker runtime was deployed and verified with non-root execution, read-only root filesystems, `no-new-privileges`, dropped Linux capabilities, scoped writable tmpfs mounts, Redis authentication, and Nginx configuration validation.

2. **Egress policy verified.** The pilot egress gateway accepts only `POST /chat`, rejects requests without its required shared-secret header with HTTP 403, rejects non-POST requests with HTTP 405, and strips selected inbound credentials and client-identity headers before proxying.

3. **Pilot credentials rotated.** Previously exposed pilot egress and Redis credentials were retired and replaced. Runtime evidence was revised to avoid capturing rendered configuration or active secret values.

4. **Secret-management boundary clarified.** Restricted local environment files remain a temporary pilot mechanism. They are not a production secret-management design. Local file-backed Compose secrets are not accepted as the target production mechanism for the mixed non-root runtime identity model.

5. **Docker Swarm excluded as a pilot-only secret migration.** The current Jarvis deployment uses a large local bridge-network topology. Moving only the pilot egress service to Swarm would break its network path to `jarvis-main-brain`; a Swarm conversion would be a broader coordinated infrastructure migration, not a secrets-only change.

6. **Production closure order updated.** The next practical work is production governance and signer enrollment, followed by an approved external secret-management implementation and completion of the protected-memory authorization and projection chain.

No capability is upgraded to `production-authorized` by this revision.

The system remains a tested, evidence-backed, fail-closed release candidate.

---

## 1. Core Principle

> Integrity proves what happened. Authority proves who may cause it. Policy proves whether it was allowed.

Merkle structures provide tamper-evident integrity evidence. Cryptographic keys and signatures establish attributable authority. The Constitutional Guardian evaluates applicable policy. A runtime may act on protected data only when it can verify the applicable authorization chain and any required unexpired authorization receipt.

A hash, CID, file, image, container, record, service, source tree, or repository branch does not become authoritative merely because it exists or can be referenced.

A Merkle root without a valid controlling signature, timestamp context, and governance interpretation is only an integrity commitment. It has no authority value on its own.

The implementation work completed through the trust-development sequence reinforces this separation. Runtime admission, caller authentication, signed operation-intent verification, policy evaluation, receipt issuance, runtime isolation, secret delivery, and production activation are separate boundaries.

A successful test, existing artifact, valid cryptographic commitment, running container, or verified pilot configuration does not independently authorize deployment or protected-data access.

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
- Treat pilot secret rotation or Docker hardening as a substitute for governed production secret custody.
- Treat interaction with Ms. Jarvis as authorization to contribute private information to the Commons.

The architecture intentionally preserves the distinction between:

1. Evidence of correctness.
2. Authority to act.
3. Authorization to perform a particular operation.
4. Runtime isolation.
5. Production activation.

---

## 3. Trust Domains

    GOVERNANCE PLANE
    Keys — Roles — Policies — Threshold Approvals — Revocation
                              |
                              v
                    POLICY DECISION ENGINE

    -------------------------------------------------------------
    |                           |                               |
    v                           v                               v

    SOFTWARE PROVENANCE     USER SOVEREIGNTY              COMMONS INTEGRITY
    Build Evidence          Vault Authority               Aggregate Authority
    Runtime Authority       Authorization Receipts         Contribution Receipts
    Admission Records       Projection Receipts            Transformation Receipts

The domains may reference each other through signed receipts, but no domain inherits authority merely from a reference.

The operational trust chain is:

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

Not every stage in this chain is currently production-activated. A missing downstream authority must not cause an upstream component to silently grant access.

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

The current trust-development model distinguishes operational approval, Guardian authority, release authority, and governance-board authority. These roles are not interchangeable.

The production governance model requires the relevant roles, policies, registries, custody procedures, and signing authorities to be independently established before production activation.

### Guardian Authority Bundle

The Guardian Authority Bundle is the concrete authority carrier at the decision boundary. Rather than sourcing caller identities, subject keys, and revocation state from separately trusted files, the Guardian consumes one governance-signed bundle that carries all three together and is accepted only when it satisfies the required governance threshold.

The bundle carries:

- A versioned bundle identifier and release profile.
- Issued and expiration timestamps.
- Caller-token commitments mapped to active caller identities and roles.
- Subject signing keys, controllers, statuses, and roles.
- Revoked subjects, intent identifiers, and receipt identifiers.
- Threshold approvals from the required governance roles.

Before trusting any bundle field, the Guardian must verify:

- The canonical bundle payload against each declared approval signature.
- Each approver key against the governance public-key registry and required role.
- The active policy’s required roles and minimum approval threshold.
- Bundle lifetime and expiry.
- That caller authentication, subject-key lookup, and revocation checks are drawn only from the verified bundle.

Caller tokens are matched by commitment rather than stored as raw authority data. Subject keys carry explicit controller and status fields. Revocation state inherits the governance signature of the bundle rather than becoming an independent unsigned input.

### Current state

The Guardian Authority Bundle schema, canonical-payload verifier, three-role threshold enforcement, caller sourcing, subject-key sourcing, and decision-boundary revocation checks are implemented and verified using test-provisioned governance keys.

This establishes the mechanism. It does not establish production authority.

A production authority bundle signed by the established production governance board, including a real enrolled governance-board signer and valid production policy threshold, remains outstanding.

---

## 5. Software Provenance and Runtime Isolation

The software provenance domain establishes which artifacts are approved to execute.

    Source
      |
      v
    Commit
      |
      v
    Build Recipe
      |
      v
    SBOM
      |
      v
    Immutable Image Digest
      |
      v
    Runtime Authority Manifest
      |
      v
    Deployment Approval
      |
      v
    Runtime Admission
      |
      v
    Running Service

A Runtime Authority Manifest must:

- Pin immutable container image digests.
- Enumerate required services, health contracts, and network dependencies.
- Identify approved policy versions.
- Include or reference SBOMs.
- Define dependency failure modes.
- Identify approved configuration references.
- Carry required release and governance signatures.
- Identify rollback targets and revocation procedures.
- Identify the approved secret-delivery mechanism without embedding plaintext secret values.

`latest` tags, filenames, backup status, container existence, source-tree location, local image presence, and compose-project status are not authority assertions.

A file existing in a repository is historical evidence unless an approved build and signed Runtime Authority Manifest declare it part of the current runtime.

### Current runtime-isolation pilot

The current pilot runtime contains:

- Redis.
- A non-root Nginx egress gateway.
- An admission API.
- A privacy worker.
- A private pilot network.
- An egress path to the existing `jarvis-main-brain` service on the local Jarvis network.

The verified pilot baseline includes:

- Non-root Nginx execution.
- Redis running under its non-root image identity.
- Read-only root filesystems for Redis, egress, admission API, and privacy worker.
- `no-new-privileges:true`.
- `cap_drop: ALL`.
- Scoped writable tmpfs mounts only where runtime operation requires them.
- A Redis password-bearing configuration restricted to owner-readable permissions.
- Redis authenticated health verification.
- Nginx syntax validation.
- Running-state verification for Redis, egress, admission API, and privacy worker.
- Egress enforcement requiring `POST /chat`.
- HTTP 403 rejection for `/chat` requests without the required egress secret.
- HTTP 405 rejection for non-POST `/chat` requests.
- Removal of selected inbound authorization, cookie, session-token, and client-address headers before egress proxying.
- Rotation of previously exposed pilot egress and Redis credentials.
- Redacted, checksum-backed verification evidence.

The accepted pilot marker is:

    PILOT_RUNTIME_FINAL_VERIFICATION_PASS

This marker proves the pilot runtime controls were active at verification time. It does not establish production runtime authority, production release approval, protected-memory authorization, or a production secret-management architecture.

### Secret-delivery boundary

The current `.pilot-*.env` files are a temporary pilot secret-delivery mechanism. Their restricted host permissions reduce exposure but do not create the identity-separated custody, auditable rotation, or production secret-delivery guarantees required for production activation.

Before production activation:

- Secret values must be removed from local environment-file delivery.
- Secret values must not be embedded in Compose YAML, source, images, shell history, rendered configuration captures, logs, or evidence.
- Each service must receive only the secret material it requires.
- Secret rotation, revocation, recovery, and incident response must be governed and auditable.
- An approved external secret-management system must support the non-root runtime identities without broadening host-file permissions.
- All pilot and pre-production credentials must be rotated during the production cutover.

Local file-backed Compose secrets are not accepted as the target production mechanism for this mixed non-root runtime identity model.

Docker Swarm secrets are not a pilot-only migration path for the current host topology. The existing Jarvis environment uses a broad local bridge-network deployment, and the pilot egress service currently reaches `jarvis-main-brain` through that local network. Moving only the pilot gateway to Swarm would remove that path. A Swarm conversion, if ever selected, must be planned as a coordinated infrastructure migration.

### Current provenance and admission state

Runtime-authority signature verification and fail-closed runtime admission are implemented in the trust-development boundary.

The existing Guardian runtime has been associated with an immutable image digest rather than an unrestricted mutable image tag.

A candidate deployment topology for a provisioned Guardian exists but is intentionally not active as production authority. The current production-signing and governance conditions are not yet complete, and the system must fail closed rather than manufacture authority from a technically deployable configuration.

These results establish meaningful runtime-authority, runtime-admission, and runtime-isolation evidence.

They do not establish final production deployment authority.

---

## 6. User Sovereignty Domain

    Private User Vault
            |
            v
    Signed Vault Root
            |
            v
    Authorization Receipt
            |
            v
    Projection Service
            |
            v
    Ms. Jarvis Reasoning
            |
            v
    Response Receipt

> Ms. Jarvis does not possess user memory. Ms. Jarvis receives authorized projections of user memory.

Private records must be encrypted before content-addressed storage. Vault roots should be private by default.

Public commitments must contain no plaintext private memory, predictable identifiers, wallet addresses, social handles, or other correlatable low-entropy values.

The reasoning system must not receive long-lived vault keys or unrestricted semantic-store access. It receives the minimum projection necessary for the approved purpose.

A projection may be:

- A selected set of decrypted records.
- A redacted summary.
- A semantic retrieval result.
- A computed feature vector.
- A policy answer.
- An anonymized contribution.
- A selective-disclosure proof.

The system must use the least powerful representation sufficient for the authorized task.

The existence of a semantic-memory system does not authorize that system to expose the underlying private corpus.

---

## 7. Operational Trust Boundary

    User Request
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
         +--------------------------+
         |                          |
         v                          v
    Encrypted User Vault       Audit Receipts
         |
         v
    Minimal Context Projection
         |
         v
    Ms. Jarvis Reasoning
         |
         v
    Auditable Response

The Guardian evaluates whether a protected operation is permitted.

The Projection Service verifies resulting authorization and creates the bounded context available to Ms. Jarvis.

The reasoning layer is not an authority oracle. It cannot expand the scope of a valid authorization receipt.

### Current implementation state

The front portion of this trust boundary is materially implemented and, in several respects, verified at the decision boundary.

The remediation history establishes:

- Caller authentication before protected decision logic.
- Fail-closed HTTP 401 behavior for missing or invalid caller credentials.
- Runtime-admission enforcement.
- Fail-closed denial when required authority configuration is absent or invalid.
- Signed operation-intent verification.
- Denial of tampered, malformed, expired, untrusted, revoked, inactive-key, caller-subject-mismatched, and request-operation-mismatched intent conditions.
- Caller identity, subject keys, and revocation state sourced from the verified governance-signed Guardian Authority Bundle.
- Subject and intent revocation checks in the request path.
- Protected-operation routing that does not silently fall back to unrestricted behavior.
- PDR issuance verified under provisioned non-production signer material, including durable consumption and replay denial.
- A separate hardened runtime-isolation pilot for the egress, Redis, admission API, and privacy worker boundary.

The complete private-memory projection chain is not yet production-complete.

---

## 8. Memory Authorization Receipt

A Memory Authorization Receipt, or MAR, binds user authority, Guardian policy approval, authorized scope, and approved runtime identity.

A MAR must identify:

- A schema version and immutable receipt identifier.
- Subject identity.
- Recipient service identity.
- Recipient runtime digest.
- Purpose and operation.
- Projection policy.
- Vault-root commitment.
- Authorized record references or approved scope commitment.
- Applicable policy and PDR identifiers.
- Issue and expiry times.
- Use limit.
- Subject signature.
- Guardian attestation.

The Projection Service must verify:

- Subject authority.
- Guardian attestation.
- Recipient identity.
- Approved recipient-runtime binding.
- Purpose and operation scope.
- Projection-policy constraints.
- Expiration.
- Use count.
- Vault-root match.
- Current revocation state.
- Referenced PDR validity.

Revocation prevents future authorization and decryption. It cannot erase plaintext already disclosed to a recipient.

Short-lived receipts, narrow scopes, minimal projections, and limited plaintext retention reduce exposure.

### Current state

MAR is a defined authorization layer supported by receipt infrastructure.

The current record does not establish a fully activated production protected-memory path in which MAR issuance, validation, projection, recipient runtime admission, revocation, scope enforcement, and durable use control operate as one complete production chain.

MAR remains part of the remaining closure work.

---

## 9. Policy Decision Receipt

The Policy Decision Receipt records the Constitutional Guardian evaluation that authorizes, denies, or marks an operation as indeterminate.

It provides provenance for the decision itself. It must not store unnecessary plaintext private context. Sensitive policy inputs must be represented through encrypted references, redacted fields, or cryptographic commitments.

A PDR must identify:

- A schema version and immutable decision identifier.
- Request identifier.
- Subject and recipient.
- Requested operation and purpose.
- Policy identifier and policy version.
- Evaluated context commitment.
- Decision and decision reason.
- Scope, projection, use-count, and expiry constraints.
- Approved Guardian runtime digest.
- Issued and expiration timestamps.
- Guardian signature.

Valid decision values are:

- `allow`
- `deny`
- `indeterminate`

A decision marked `indeterminate` must not authorize protected data projection.

A MAR derived from a PDR must not exceed the PDR’s scope, lifetime, policy constraints, or use count.

### Current implementation state

The PDR architecture has progressed beyond a conceptual state.

The trust-receipt work establishes:

- PDR schema and validation infrastructure.
- Receipt verification and binding requirements.
- PDR factory and issuance infrastructure.
- Durable consumption-ledger mechanisms.
- Replay-denial behavior.
- Fail-closed behavior when signer authority is absent, invalid, untrusted, or wrong-role.
- Negative security validation for invalid and untrusted signer conditions.
- Canonical receipt-chain verification modules.

End-to-end PDR issuance, durable consumption, and replay denial have been demonstrated under provisioned non-production Guardian signer material.

A policy `allow` is not sufficient by itself to authorize a protected operation. A valid PDR must be cryptographically issued under the required Guardian authority.

### Production authority remains incomplete

The production Guardian PDR signer is not yet established as a trusted production authority in the required signer registry.

The production trusted registry does not yet contain an enrolled production Guardian signer with the required `guardian` role and governance authorization.

The correct current behavior is fail closed rather than manufacturing or accepting unauthorized PDRs.

---

## 10. Projection Receipt

A Projection Receipt records the transformation from an authorized data scope into the bounded context supplied to a reasoning system.

It answers:

> What information crossed the protected vault boundary into the reasoning boundary?

A Projection Receipt must be created whenever protected vault material is transformed into reasoning-context material.

A Projection Receipt must identify:

- A schema version and immutable projection identifier.
- MAR and PDR identifiers.
- Source vault-root and scope commitments.
- Projection type and minimization policy.
- Released record and token limits where applicable.
- Recipient runtime digest.
- Projection-service runtime digest.
- Issue and expiry timestamps.
- Projection output commitment.
- Projection-service signature.

The Projection Receipt must:

- Reference a valid, unexpired MAR.
- Bind the projection to the authorized vault root and scope.
- Identify the approved recipient runtime.
- Identify the approved Projection Service runtime.
- Record the applicable minimization policy.
- Commit to canonical output without publishing unnecessary plaintext.
- Expire no later than the associated MAR.
- Be auditable without becoming a second plaintext memory store.

### Current state

Projection Receipt architecture remains defined.

The remediation record does not establish complete production activation of:

- Projection Service deployment.
- Projection Service runtime authority.
- Protected retrieval.
- Complete MAR validation at the projection boundary.
- Recipient-runtime binding.
- Projection output commitment.
- Revocation checks at the projection boundary.
- Full protected-memory isolation from unrestricted reasoning access.

These remain explicit production closure requirements.

---

## 11. Constitutional Guardian Contract

The Constitutional Guardian decides whether a protected capability may be exercised.

The following capabilities must fail closed when no valid PDR or required authorization receipt exists:

- Protected data projection.
- Private-memory retrieval.
- Identity verification.
- Signature verification.
- Commons contribution.
- Governance action.
- Protected citizen or member data access.
- Release approval and runtime admission.

    Guardian available + policy approves
        -> issue PDR
        -> issue MAR
        -> permit bounded projection

    Guardian denies
        -> disclose nothing

    Guardian indeterminate
        -> disclose nothing

    Guardian unavailable
        -> no receipt
        -> protected capability unavailable

A general chat interface may remain available during Guardian outage only if it cannot access protected user memory, protected identity data, protected Commons functions, or governance capabilities.

The system may provide a clearly labeled, non-personalized response when protected capabilities are unavailable.

It must not silently degrade into unauthorized private-memory access.

### Current implementation state

The Guardian is a materially implemented and tested trust boundary.

The remediation history establishes:

- Runtime admission.
- Caller authentication.
- Signed operation-intent verification.
- Caller-subject binding.
- Request-operation binding.
- Authority-bundle sourcing.
- Subject and intent revocation enforcement at the decision boundary.
- Fail-closed protected decision routing.
- PDR issuance verified under provisioned non-production signer material.
- Durable PDR consumption and replay denial.
- Negative security tests for required trust-condition failures.

The Guardian is not yet a fully activated production authority for the complete protected-memory architecture.

Production governance-board authority, production Guardian signer enrollment, production Authority Bundle approval, production policy activation, complete projection admission, and full protected-memory closure remain outstanding.

---

## 12. Commons Contribution Domain

The Commons receives explicitly authorized transformations, not raw private-vault graphs.

    Private Vault
         |
         v
    User-Approved Transformation
         |
         v
    Contribution Receipt
         |
         v
    Transformation Receipt
         |
         v
    Aggregation
         |
         v
    Commons Epoch Root
         |
         v
    Governance Decision

Each Commons Transformation Receipt must identify:

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

It does not independently prove anonymization, non-discrimination, legal compliance, or ethical legitimacy.

The Commons must not ingest raw private-vault graphs merely because a user has interacted with Ms. Jarvis.

> Interaction history with Ms. Jarvis is not itself a contribution authorization event.

### Current state

The Commons architecture remains defined.

The current implementation record does not establish full production implementation and authorization of:

- Contribution Receipts.
- Transformation Receipts.
- Commons Epoch Root governance.
- Privacy attestations.
- Complete contribution authorization.
- Production governance approval of Commons transformations.

These remain outstanding.

---

## 13. Receipts, Audit, and Evidence

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

Each receipt or authority artifact must have:

- A schema version.
- An immutable identifier.
- An issuer identity.
- A timestamp.
- A policy reference where applicable.
- An integrity commitment.
- A verifiable signature or attestation.
- Clear retention and revocation semantics.

Audit records must minimize personal data.

Auditability is not permission to create a parallel surveillance database.

### Evidence and sealing

The trust-development process establishes evidence capture, reproducibility capture, trust gates, review gates, promotion seals, runtime verification artifacts, and durable evidence records.

Verification claims must be tied to preserved evidence rather than an unrecorded statement that a test once passed.

Runtime evidence must not contain:

- Private keys.
- Passphrases.
- Seeds.
- Runtime secrets.
- Full secret-bearing environment files.
- Redis connection URLs containing credentials.
- Rendered Nginx configuration containing active shared secrets.
- Raw authorization headers.
- Session tokens.
- Plaintext protected user content.

A capability may be described as:

- Defined.
- Implemented.
- Verified.
- Sealed.
- Promoted.
- Production-authorized.

These are distinct states.

---

## 14. Current Implementation and Verification Alignment

| Component | Current state |
|---|---|
| Constitutional Guardian | Implemented and materially hardened at the decision boundary. Runtime admission, caller authentication, signed operation-intent enforcement, Authority Bundle sourcing, revocation enforcement, and fail-closed protected decision boundaries are implemented. |
| Guardian Authority Bundle | Implemented and verified with test-provisioned governance keys. Production governance-board authority and a genuine production bundle remain pending. |
| Runtime Authority Manifest | Implemented and cryptographically verified in the trust-development boundary. Final production release authority remains gated. |
| Runtime Admission | Implemented and verified. Protected runtime boundaries fail closed when required authority conditions are absent or invalid. |
| Caller authentication | Implemented and verified fail closed. |
| Signed operation intent | Implemented and verified at the protected decision boundary, including mismatch, tampering, trust, status, and revocation denial paths. |
| PDR schema and verification | Implemented. Structural, cryptographic, lifetime, and binding infrastructure exists. |
| PDR factory and issuance | Implemented and verified under provisioned non-production signer material. Production signer enrollment remains outstanding. |
| Guardian PDR signing authority | Not production-authorized. A dedicated production signer with the required registry role and governance authorization remains required. |
| Durable receipt ledger | Implemented and verified for consumption and replay denial in the trust-development boundary. |
| Runtime-isolation pilot | Verified. Redis, egress, admission API, and privacy worker passed final runtime checks with read-only roots, dropped capabilities, non-root execution where configured, Redis authentication, Nginx validation, and egress enforcement. |
| Egress boundary | Verified for `/chat`: unauthenticated POST rejection with HTTP 403 and non-POST rejection with HTTP 405. |
| Pilot secret rotation | Egress and Redis credentials previously exposed during remediation were rotated. Current local environment-file delivery is temporary and not production-ready. |
| External secret manager | Not yet implemented. Required before production activation. |
| Docker Swarm migration | Not approved as a pilot-only secret migration because the current local bridge-network topology would require coordinated broader infrastructure migration. |
| MAR | Defined and supported by receipt infrastructure; complete protected-memory production path remains pending. |
| Projection Receipt | Defined; complete production projection boundary remains pending. |
| Projection Service | Not production-activated. |
| Reasoning isolation | Existing semantic-memory and reasoning capabilities must remain behind the authorization and projection boundary. |
| Commons receipts and governance | Defined; production implementation remains pending. |
| Revocation | Verified at the Guardian decision boundary; projection-path integration remains pending. |
| Adversarial matrix | Partially closed. Decision-boundary cases are verified; expiration, policy mismatch, unapproved-image, outage, secret-manager failure, and full projection-chain cases remain. |
| Custodian ceremony | Started but incomplete. It grants no authority until the required independent custodians, remaining enrollment records, and threshold-signed governance registry are complete. |
| Release-candidate evidence | Completed as a tested, evidence-backed, fail-closed package. It is not an active authority system. |
| Live authority system | Not active. Production activation remains blocked pending governance, signer, secret-management, projection, release, and final authorization prerequisites. |

An implemented component is not automatically production-authorized.

A verified pilot is not automatically a production release.

A sealed evidence artifact is not automatically an active authority system.

---

## 15. Verification Requirements

| Capability | Required proof | Current status |
|---|---|---|
| Approved production service | Pinned digest, SBOM, Runtime Authority Manifest, governance approval, health checks, contract checks, rollback evidence | Partially demonstrated; final production release closure remains |
| Runtime authority | Valid signed manifest, trusted signers, policy compatibility, image binding | Signature and admission evidence demonstrated; final production governance remains |
| Guardian Authority Bundle | Production-signed bundle satisfying required roles, threshold, expiry, key validity, and revocation state | Test-provisioned mechanism verified; production bundle remains |
| Caller authenticity | Valid bundle-sourced caller credential before protected decision logic | Implemented and verified fail closed |
| Signed operation intent | Valid signature, trusted active subject key, caller-subject binding, request-operation binding, revocation enforcement | Implemented and verified fail closed |
| PDR issuance | Valid production Guardian signer, trusted registry entry, policy binding, durable consumption, cryptographic signature | Verified under provisioned non-production signer; production enrollment remains blocked |
| Secret delivery | Approved external manager, least privilege, non-root compatibility, auditable rotation and recovery | Not complete |
| Runtime isolation | Read-only roots, least privilege, scoped writable paths, tested egress enforcement, authenticated dependencies | Verified for the pilot baseline |
| Private-memory access | Valid MAR, valid PDR, vault-root match, recipient-runtime binding, unexpired scope, use-count and revocation enforcement | Not production-closed |
| Semantic projection | Valid Projection Receipt, minimization policy, output commitment, recipient binding, expiry, use controls | Not production-closed |
| Commons contribution | User authorization, valid Contribution Receipt, applicable PDR | Pending |
| Commons transformation | Transformation Receipt, approved runtime digest, privacy mechanism, cohort threshold, required attestations | Pending |
| Governance decision | Epoch root, approved aggregation method, policy record, required signatures | Pending |
| Revocation | Current revocation-state check before every protected projection | Decision-boundary verification complete; projection-path integration pending |
| Guardian outage | Protected capability denial; no fallback to unapproved access | Applicable trust path fails closed; full protected-memory path remains pending |
| Secret-manager outage | Protected capability denial and safe recovery without secret disclosure | Pending |
| Unapproved runtime | Verification failure and denial of protected projection | Runtime admission implemented; full projection path remains pending |
| Receipt replay | Binding, expiry, use count, durable replay detection | PDR replay denial verified; full chain remains pending |
| Multi-replica ledger | Durable shared-ledger conformance | Pending before multi-replica production deployment |

---

## 16. Pilot Implementation and Production Closure Order

### 16.1 Purpose and status

This section records the current implementation boundary and the remaining closure work required before any component may be represented as production-authorized.

The system has progressed beyond an architecture-only design. It now includes meaningful, evidence-backed implementation and verification of trust-boundary controls, receipt infrastructure, Guardian decision-boundary controls, and a hardened privacy-gateway runtime pilot.

Those accomplishments are real and operationally valuable. They do not activate production authority, authorize protected-memory access, establish governance approval, or permit a live authority system.

The present status is:

    RELEASE STATE: tested, evidence-backed, fail-closed release candidate
    AUTHORITY STATUS: inactive
    DEPLOYMENT ADMISSION: blocked pending production governance, signing,
    runtime-authority, protected-memory, projection, secret-management,
    and activation conditions

The verified privacy-gateway pilot is a runtime-isolation baseline. It is not the completion of the MountainShares / Ms. Jarvis production trust architecture.

### 16.2 Completed or materially advanced work

The following work has been implemented, materially hardened, or verified:

1. Governance-role, policy, threshold, and failure-mode architecture has been defined.
2. Runtime-authority structures have been defined and verification infrastructure implemented.
3. Runtime admission has been implemented as a fail-closed boundary.
4. Guardian admission evidence, trust gates, reproducibility capture, evidence sealing, and applicable promotion records have been established.
5. Caller authentication has been implemented before protected decision logic.
6. Signed operation-intent verification and caller-subject-request-operation binding have been implemented.
7. Tampered, untrusted, inactive-key, malformed, mismatched, and revoked intent conditions are denied fail closed.
8. Guardian Authority Bundle verification, threshold approval checks, and bundle-sourced caller, subject-key, and revocation authority have been implemented and verified with test governance material.
9. Subject and intent revocation are enforced at the Guardian decision boundary.
10. Trust-receipt schemas, canonical verification modules, PDR factory infrastructure, and receipt-chain checks have been implemented.
11. Durable PDR consumption and replay denial have been implemented and verified under provisioned non-production signer material.
12. Negative security cases have been validated around completed decision-boundary controls.
13. Custodian enrollment has begun without activating authority.
14. Evidence-backed release-candidate artifacts have been produced without private keys or production authority activation.
15. The runtime-isolation pilot has been deployed and verified.
16. Pilot egress and Redis credentials exposed during remediation were rotated.
17. Final pilot verification confirms operational Redis, egress, admission API, and privacy worker services with intended runtime controls.

### 16.3 Remaining closure work

The remaining work must preserve the same fail-closed discipline.

#### Governance and authority

1. Establish the authorized production governance decision and corresponding production policy registry.
2. Establish the required production governance-board authority and enroll a real governance-board signer.
3. Complete the independent-custodian enrollment and governance activation ceremony.
4. Produce a threshold-signed active production governance registry.
5. Establish production key-rotation, revocation, incident-response, and emergency-suspension procedures.

#### Guardian signer and PDR activation

6. Establish dedicated Guardian PDR signing authority in approved secure custody.
7. Enroll its public key, with the required `guardian` role, in the production trusted signer registry.
8. Produce a production Guardian Authority Bundle carrying genuine production approvals and valid expiry.
9. Demonstrate a live, cryptographically valid PDR issuance path against production authority.
10. Demonstrate durable production receipt consumption and replay denial.
11. Ensure Guardian outage and signer failure deny protected capabilities rather than creating fallback authorization.

#### Runtime authority and secrets

12. Build and verify one reproducible pilot release from a fully governed signed Runtime Authority Manifest.
13. Pin exact production image digests, SBOMs, dependencies, policies, health contracts, rollback targets, and release approvals.
14. Implement approved external secret management compatible with the non-root runtime.
15. Replace temporary local environment-file secret delivery.
16. Rotate all pre-production credentials during the governed production cutover.
17. Verify that no secret values appear in source, Compose configuration, rendered configuration output, evidence, logs, shell history, or repository history.
18. Define and test secret-manager outage, recovery, rotation, and revocation behavior.

#### Protected memory and projection

19. Establish signed runtime-admission chains for the Projection Service and reasoning recipient.
20. Implement and verify MAR issuance and validation in the protected-memory path.
21. Implement Projection Service verification before protected retrieval.
22. Remove unrestricted private-memory access from reasoning paths.
23. Implement and verify Projection Receipts and their output commitments.
24. Bind recipient runtime identity, projection scope, purpose, policy, expiry, and use count before reasoning-context release.
25. Integrate revocation into protected-memory and projection authorization checks before every new projection.

#### Commons and full-chain verification

26. Implement Contribution and Transformation Receipts before publishing Commons aggregates.
27. Establish Commons Epoch Root governance and required privacy attestations.
28. Close the remaining adversarial verification cells:
    - Authority and receipt expiration.
    - Policy-version mismatch.
    - Unapproved-image access.
    - Guardian outage.
    - Secret-manager outage.
    - PDR, MAR, projection, and response replay.
    - Full protected-memory projection chain.
29. Demonstrate durable shared-ledger conformance before any multi-replica deployment requiring shared receipt consumption.
30. Exercise backup recovery, rollback, incident response, observability, and evidence-retention procedures.

### 16.4 Production acceptance criteria

The system may be described as production-authorized only when all of the following are true for the exact immutable release in operation:

- Required governance authority is active and valid.
- Required production signers are securely provisioned, enrolled, role-authorized, non-revoked, and governed.
- A valid production Guardian Authority Bundle satisfies the required approval threshold.
- Runtime Authority Manifest verification succeeds for the exact running image digests.
- Approved external secret delivery is active and no plaintext secret values are exposed through disallowed channels.
- Protected operations require valid caller authority, signed operation intent, runtime admission, PDR, MAR, and projection authorization as applicable.
- Protected-memory retrieval is bounded by valid authorization, scope, expiry, recipient binding, and revocation controls.
- The reasoning recipient is runtime-approved and receives only authorized minimal context.
- Receipt consumption and replay prevention operate durably at the intended deployment scale.
- Required negative, outage, rollback, and recovery tests pass.
- Commons contribution controls are active before contribution or publication paths are enabled.
- The release is reproducible, evidenced, approved, observable, recoverable, and reversible.
- Required governance authority has approved activation of that exact release.

Until these conditions are satisfied, the correct description remains:

    A tested, evidence-backed, fail-closed release candidate with a verified
    runtime-isolation pilot baseline; not a production-authorized live authority system.

### 16.5 Immediate practical next project

The immediate next project is:

1. Production governance and signer enrollment.
2. Approved external secret-manager implementation.
3. Governed Runtime Authority Manifest and reproducible release closure.
4. Protected-memory MAR and Projection Service activation.
5. End-to-end production-chain adversarial verification.

The immediate next project is not another emergency Docker hardening change. The pilot has established a hardened runtime baseline. Production progress now depends on legitimate authority, signer custody, governed secret delivery, immutable release authority, and completion of the protected-memory authorization and projection chain.

---

## 17. Current Release Boundary

The current system state must be described as:

> A tested, evidence-backed, fail-closed release candidate rather than a live authority system.

The release boundary is intentionally inactive.

The current public or shareable evidence package must exclude:

- Private keys.
- Passphrases.
- Seeds.
- Runtime secrets.
- Signer private material.
- Full secret-bearing configuration.
- Plaintext protected data.
- Other sensitive authority material.

The current pilot verification evidence demonstrates runtime isolation, service health, credential rotation, egress enforcement, Redis authentication, and fail-closed boundary controls without granting production authority.

The custodian ceremony has begun but is incomplete. Partial enrollment grants no authority.

A candidate Guardian deployment topology may be technically deployable but remains unauthorized until the required governance, signer, authority-bundle, runtime-manifest, secret-management, and protected-memory conditions are complete.

The architecture is designed to stop before live authority is granted when required governance, signing, registry, runtime, secret-delivery, or projection conditions are absent.

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

Relevant evidence has been preserved as an identifiable, integrity-bound artifact.

### Promoted

The relevant stage has passed its defined promotion gate and has been recorded as such.

### Production-authorized

The required governance authority, signing authority, runtime admission, policy, secret-management, release, and activation conditions exist and have been explicitly authorized.

These states must not be conflated.

> Implemented does not mean production-authorized.  
> Verified does not mean production-authorized.  
> Sealed evidence does not mean production-authorized.  
> Promoted does not mean production-authorized.  
> A hardened pilot does not mean production-authorized.  
> A release candidate does not mean an active authority system.

---

## 19. Final Architectural Position

The architecture has progressed beyond a purely conceptual trust model.

The current system contains meaningful, evidence-backed implementation of:

- Runtime authority.
- Signed runtime admission.
- Guardian admission enforcement.
- Caller authentication.
- Signed operation-intent verification.
- Caller-subject and request-operation binding.
- Governance-signed Guardian Authority Bundle verification.
- Subject and intent revocation enforcement at the decision boundary.
- Fail-closed protected decision paths.
- PDR schema, factory, verification infrastructure, issuance under provisioned non-production signer material, durable consumption, and replay denial.
- Runtime-isolation pilot controls.
- Non-root service operation where configured.
- Read-only roots, dropped capabilities, and no-new-privileges controls.
- Scoped writable runtime paths.
- Redis authentication and protected configuration permissions.
- Egress method and shared-secret enforcement.
- Credential rotation after pilot exposure.
- Trust gates, reproducibility capture, evidence sealing, and applicable stage promotion.
- Negative security validation.
- Non-authorizing release-candidate packaging.

These accomplishments materially advance the implementation state.

However, the architecture deliberately preserves the remaining boundaries around:

- Final production governance authority.
- A production governance-board signer.
- A production Guardian PDR signer enrolled in the production trusted registry.
- A production Guardian Authority Bundle carrying genuine threshold approvals.
- Production policy registries.
- Approved external secret management.
- Governed immutable release authority.
- Projection Service admission.
- Reasoning-recipient admission.
- Complete MAR activation.
- Protected semantic projection.
- Removal of unrestricted private-memory access.
- Contribution and Transformation Receipts.
- Commons Epoch Root governance.
- Revocation integration into the protected-memory and projection path.
- Remaining adversarial verification cells.
- Durable shared-ledger verification at production scale.
- Final reproducible release authorization.
- Completion of human custodian and governance activation.

The result is not an architecture claiming completion prematurely.

It is an architecture in which remaining work is expressed as explicit authority, implementation, operational, and verification gates rather than unspecified future work.

The governing principle remains unchanged:

> Integrity proves what happened. Authority proves who may cause it. Policy proves whether it was allowed.

The documentation records both sides of the current state:

> What has actually been built, tested, verified, sealed, and promoted; and what remains deliberately blocked because the required authority has not yet been established.
