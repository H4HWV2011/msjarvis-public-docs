# MountainShares / Ms. Jarvis Trust Architecture v1.5

**Status:** Architecture Freeze Candidate — Runtime-Isolation, Controlled Email Pilot, and Administrative Recovery Update  
**Authority:** Canonical design reference for pilot trust-boundary work  
**Date:** 2026-08-15  
**Supersedes:** v1.4 (2026-08-14)  
**Scope:** Software provenance, runtime authority, user sovereignty, Commons integrity, policy-governed AI projections, receipt-based authorization, runtime isolation, controlled email delivery, administrative runtime recovery, and fail-closed governance boundaries.

---

## Revision Note (v1.4 → v1.5)

This revision incorporates the verified administrative recovery of the two critical Jarvis runtime services:

- `jarvis-main-brain`
- `jarvis-hilbert-state`

The recovery establishes a bounded, declaratively owned runtime contract for those services under the dedicated Docker Compose project:

    jarvis-legacy-recovery

The recovery does not activate production authority, authorize protected-memory access, complete the broad Jarvis stack consolidation, establish an institutional multi-user service, enable unrestricted live email delivery, or convert the current release candidate into a production-authorized authority system.

It records an important administrative fact:

> A service can be running, reachable, and recovered without yet being production-authorized.

Concrete updates in this revision:

1. **Critical service recovery recorded.** `jarvis-main-brain` and `jarvis-hilbert-state` are operating under the dedicated `jarvis-legacy-recovery` Compose project rather than being managed through the broad historical aggregate stack.

2. **Main Brain runtime boundary clarified.** The recovered Main Brain uses the legacy-compatible candidate image and is exposed only on loopback through `127.0.0.1:18058` to container port `8008`. Its Chroma dependency is explicitly addressed through the internal service endpoint `jarvis-chroma:8000`.

3. **Hilbert State runtime boundary clarified.** The recovered Hilbert State is exposed only on loopback through `127.0.0.1:18092` to container port `8081`. Its expected network and read-only mount requirements remain part of its declared runtime contract.

4. **Health evidence recorded.** At recovery verification time, both services were running and externally reachable through their defined local health paths. This is operational evidence, not production authorization.

5. **Administrative ownership boundary recorded.** The historical `msjarvis-rebuild` aggregate remains a broad, mixed-origin environment containing many additional services and layered Compose inputs. It must not be treated as the lifecycle owner of the recovered Main Brain and Hilbert State services.

6. **Administrative-production status clarified.** The recovered pair is administratively improved and operationally stable, but the wider stack is not yet an as-built administrative-production deployment. Full closure still requires authoritative service inventory, one approved declarative owner per production service, immutable release binding, governed secret delivery, explicit health contracts, rollback procedures, and change governance.

7. **Secret-handling boundary reinforced.** Recovery artifacts, rendered configuration, local environment files, terminal history, and verification evidence must not disclose secret values. Any credentials exposed during earlier recovery or rendered-configuration work must be treated as candidates for rotation.

No capability is upgraded to `production-authorized` by this revision.

The system remains a tested, evidence-backed, fail-closed release candidate with a recovered administrative core.

---

## 1. Core Principle

> Integrity proves what happened. Authority proves who may cause it. Policy proves whether it was allowed.

Merkle structures provide tamper-evident integrity evidence. Cryptographic keys and signatures establish attributable authority. The Constitutional Guardian evaluates applicable policy. A runtime may act on protected data only when it can verify the applicable authorization chain and any required unexpired authorization receipt.

A hash, CID, file, image, container, record, service, source tree, repository branch, successful test, locally available secret, healthy endpoint, or recovered Compose deployment does not become authoritative merely because it exists or can be referenced.

A Merkle root without a valid controlling signature, timestamp context, and governance interpretation is only an integrity commitment. It has no authority value on its own.

A running container without an approved Runtime Authority Manifest, valid deployment approval, governed secret-delivery path, applicable policy, and required operating authorization is only evidence that software is running.

The implementation work completed through the trust-development sequence reinforces this separation. Runtime admission, caller authentication, signed operation-intent verification, policy evaluation, receipt issuance, runtime isolation, secret delivery, controlled email processing, administrative recovery, and production activation are separate boundaries.

A successful test, existing artifact, valid cryptographic commitment, running container, verified pilot configuration, healthy endpoint, or recovered local service does not independently authorize deployment, protected-data access, contribution to the Commons, or live email delivery.

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
- Treat the existence of a container, file, service, image, repository branch, or Compose project as proof that it is canonical or authorized.
- Treat a healthy endpoint as proof that the service is approved to access protected data or perform governed actions.
- Give a reasoning model unrestricted access to personal memory, private identity data, or long-lived decryption keys.
- Treat successful software tests as equivalent to production authorization.
- Treat a release-candidate evidence bundle as an active authority system.
- Treat an available signing key as sufficient authority without the corresponding governance policy, role, registry, runtime, and authorization conditions.
- Treat an OpenPGP release-signing key as interchangeable with a raw Ed25519 Guardian signing key.
- Treat a governance-signed authority bundle validated with test or ephemeral governance keys as equivalent to a production authority bundle signed by the established production governance board.
- Treat a technically deployable topology as authorized merely because it can be deployed.
- Treat pilot secret rotation, local environment files, or Docker hardening as a substitute for governed production secret custody.
- Treat interaction with Ms. Jarvis as authorization to contribute private information to the Commons.
- Treat a dry-run audit event as proof of email delivery.
- Treat a working provider credential as approval to send email.
- Treat a one-shot stdin-driven worker as a persistent, multi-user job-processing system.
- Treat a local Docker Compose configuration as a complete institutional-production deployment platform.
- Treat local file-backed secrets, even when mounted with effective least-privilege permissions, as the final production secret-management architecture.
- Treat the recovery of Main Brain and Hilbert State as proof that the full historical Jarvis stack has been consolidated or production-authorized.
- Treat the broad `msjarvis-rebuild` aggregate as an approved authoritative deployment definition merely because many containers remain running under it.
- Treat an email-delivery pilot as evidence that institutional SSO, tenant isolation, role-based authorization, privacy governance, support workflows, or operational readiness have been completed.

The architecture intentionally preserves the distinction between:

1. Evidence of correctness.
2. Authority to act.
3. Authorization to perform a particular operation.
4. Runtime isolation.
5. Controlled pilot operation.
6. Administrative recovery.
7. As-built administrative production.
8. Production activation.

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

The administrative recovery path is separate from protected-data authorization:

    Preserved Runtime Evidence
             |
             v
    Reconstructed Compose Contract
             |
             v
    Scoped Recovery Project
             |
             v
    Local Network and Dependency Verification
             |
             v
    Health Verification
             |
             v
    Recovery Evidence Capture
             |
             v
    Administrative Review
             |
             v
    Production Closure Decision

The recovery path establishes operational control and evidence. It does not bypass runtime authority, governance approval, secret-management requirements, receipt validation, or protected-memory policy.

The controlled email pilot is a separate, narrower operational path:

    Approved One-Shot Request
             |
             v
    Email Worker
             |
             v
    Dry-Run Gate
             |
             +----------------------------+
             |                            |
             v                            v
    Redacted Audit and Exit        Live-Forwarding Path
                                   (disabled by default)
                                          |
                                          v
                               Egress Authentication Proxy
                                          |
                                          v
                                Egress Gateway / Provider

In the verified default mode, the dry-run gate terminates processing before the worker reads its shared authentication token or forwards an HTTP request. Therefore, neither the authentication proxy nor the egress gateway is required for a one-shot dry-run worker invocation.

Not every stage in these chains is currently production-activated. A missing downstream authority must not cause an upstream component to silently grant access.

---

## 4. Governance Plane

The governance plane defines:

- Authorized signing identities and key-rotation rules.
- Roles, delegation limits, and threshold-approval requirements.
- Versioned policies and policy-decision semantics.
- Revocation, incident-response, and audit-retention rules.
- Required review procedures for high-impact actions.
- Which protected capabilities fail closed.
- The authority required to approve a runtime, policy, transformation, Commons governance action, transition from controlled email dry run to live email delivery, or promotion from administrative recovery to production operation.
- The institutional roles and governance approvals required before any multi-user support workflow is represented as production-authorized.
- The administrative authority responsible for approving as-built service contracts, rollback definitions, change windows, and operational ownership.

A Merkle root is evidence. Governance keys, role assignments, policies, and verified signatures are the authority layer.

The Policy Decision Engine evaluates requests against the active policy set. It does not replace human governance. It applies the policies and delegations established by governance.

The current trust-development model distinguishes operational approval, Guardian authority, release authority, email-delivery authorization, administrative recovery approval, and governance-board authority. These roles are not interchangeable.

The production governance model requires the relevant roles, policies, registries, custody procedures, signing authorities, and institutional operating approvals to be independently established before production activation.

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

## 5. Software Provenance, Runtime Isolation, and Administrative Recovery

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
- Define whether a component is a one-shot job, a controlled pilot service, an administratively recovered service, or an approved persistent production workload.
- Define the approved transition conditions between dry-run and live behavior.
- Define the authoritative lifecycle owner for each service.
- Define the approved networks, ports, mounts, dependency endpoints, and health contracts.
- Define how live-state conformance is checked against the approved contract.

`latest` tags, filenames, backup status, container existence, source-tree location, local image presence, Compose-project status, successful local builds, and successful recovery are not authority assertions.

A file existing in a repository is historical evidence unless an approved build and signed Runtime Authority Manifest declare it part of the current runtime.

### Administrative recovery boundary

The critical recovered services are declared under the dedicated administrative recovery project:

```text
jarvis-legacy-recovery
```

The project uses the legacy-compatible recovery manifest:

```text
/mnt/nvme1/msjarvis-rebuild/jarvis-legacy-compatible.chroma.yml
```

The recovered service state at verification was:

| Service | Image | Local exposure | Operational condition |
|---|---|---|---|
| `jarvis-main-brain` | `jarvis-main-brain:timeout-none-candidate-20260815` | `127.0.0.1:18058 -> 8008/tcp` | Running and health-reachable |
| `jarvis-hilbert-state` | `jarvis-main-brain:latest` | `127.0.0.1:18092 -> 8081/tcp` | Running and health-reachable |

The current contract is intentionally local-only at the host boundary. Neither recovered service is presented as a public internet-facing production endpoint by this recovery definition.

The Main Brain recovery contract includes:

- The legacy-compatible Main Brain image reference.
- Internal application port `8008`.
- Loopback-only host publication at `127.0.0.1:18058`.
- Access to required Jarvis internal networking.
- Explicit Chroma service addressing through `jarvis-chroma:8000`.
- No assumption that a host loopback dependency is reachable from within the container.
- Recovery evidence and rendered configuration sufficient to reproduce the verified local operating state.

The Hilbert State recovery contract includes:

- The currently running service image reference.
- Internal application port `8081`.
- Loopback-only host publication at `127.0.0.1:18092`.
- Required network attachments.
- Required read-only model and intake mounts.
- Recovery evidence and rendered configuration sufficient to reproduce the verified local operating state.

The recovered pair is not owned by the broad historical aggregate stack merely because those services may depend on networks and companion services created elsewhere.

The historical aggregate environment remains operationally distinct:

```text
msjarvis-rebuild
```

It contains a broad mixed-origin service population, historical Compose layers, candidate material, legacy configurations, and additional dependencies. It is not yet a clean authoritative production deployment definition.

The following rule is therefore normative:

> Do not use the broad aggregate Compose project to recreate, tear down, or modify the recovered Main Brain and Hilbert State pair without an explicit reviewed migration plan.

Recovery procedure, evidence capture, and future operational work must preserve this ownership boundary.

### Current administrative-production state

The recovered Main Brain and Hilbert State pair is:

- Declaratively scoped.
- Locally reachable through loopback-only published ports.
- Running under a dedicated Compose project.
- Connected to its required known dependencies.
- Supported by recovery evidence.
- Operationally healthier and more administratively legible than before recovery.

The recovered pair is not yet fully as-built administrative production because:

- The complete authoritative inventory of all production-required services is not yet closed.
- The broad aggregate environment has not yet been decomposed into approved service ownership boundaries.
- The Hilbert State image reference remains mutable and must be replaced with an immutable release binding.
- Docker-native health contracts are not yet uniformly declared for the recovered services.
- Dependency readiness, restart, failure, and recovery semantics require formal definition.
- Secret rotation and migration to governed external secret delivery remain incomplete.
- Complete release manifests, SBOM bindings, rollback artifacts, and change-control procedures remain pending.
- The boundary between core production services, platform dependencies, experiments, candidates, and historical remnants remains to be formally recorded.

The proper current description is:

> A recovered and administratively bounded core runtime, operating as a release-candidate environment, not yet a complete as-built administrative-production stack.

### Core recovery inventory target

The next authoritative administrative inventory must classify at least the following services:

| Service class | Expected examples | Required administrative record |
|---|---|---|
| Core application | Main Brain, Hilbert State | Image binding, ports, mounts, networks, health, owner, rollback |
| Platform dependencies | Chroma, Redis, Ollama, Hilbert Time | Dependency contract, persistence, health, ownership, failure mode |
| Data services | Local databases and persistent stores | Data owner, backup, restore, credentials, network scope |
| Security and policy services | Guardian, admission boundary, egress controls | Runtime authority, policies, signer dependencies, failure behavior |
| Pilot services | Privacy gateway and controlled email components | Explicit pilot status, no production implication, activation gate |
| Candidate or historical services | Legacy, experimental, abandoned, or duplicate containers | Classification, evidence retention, decommission or migration plan |

No service should be considered administratively production-ready until it has one approved declarative lifecycle owner.

### Runtime-isolation pilot

The current privacy-gateway pilot runtime contains:

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

```text
PILOT_RUNTIME_FINAL_VERIFICATION_PASS
```

This marker proves the pilot runtime controls were active at verification time. It does not establish production runtime authority, production release approval, protected-memory authorization, institutional multi-user authorization, or a production secret-management architecture.

### Controlled email runtime boundary

The controlled email-delivery pilot is a separate, bounded runtime path:

```text
email-worker
    |
    | internal HTTP only when dry run is disabled
    v
email-egress-auth
    |
    | internal HTTP only
    v
email-egress
    |
    | designated outbound HTTPS path
    v
email provider
```

The verified Compose topology contains three services:

| Service | Purpose | Runtime identity | Secret access | Networks |
|---|---|---:|---|---|
| `email-worker` | One-shot request validation, permitted-template rendering, redacted audit emission, and controlled forwarding only when dry run is disabled | `10001:10001` | Worker authentication token only | `email_worker_auth` |
| `email-egress-auth` | Validates the worker authentication header using constant-time comparison and forwards only authorized requests | `10002:10002` | Worker authentication token only | `email_worker_auth`, `email_auth_egress` |
| `email-egress` | Receives authorized email payloads and, only on an authorized live path, performs the outbound provider request | `10003:10003` | Provider API key only | `email_auth_egress`, `email_egress_outbound` |

The worker is intentionally excluded from the egress-gateway network. It cannot directly reach the egress service or designated external email endpoint through the approved topology.

The worker does not receive the provider API key. The authentication proxy does not receive the provider API key. The egress gateway does not receive the worker-authentication token.

This separation is a trust-boundary control. It is not by itself a complete institutional authorization model.

### Email runtime hardening controls

The verified Compose design applies the following controls to the email services:

- `read_only: true`.
- Numeric non-root `user` identities.
- `security_opt: no-new-privileges:true`.
- `cap_drop: ALL`.
- Scoped `/tmp` tmpfs mounts with service-specific UIDs and GIDs.
- Per-service CPU and memory limits.
- Internal networks for worker-to-auth and auth-to-egress paths.
- A separate designated outbound network for the egress gateway.
- Docker secret mounts scoped to the service that requires the corresponding secret.

The auth and egress proxies were verified to initialize under read-only roots, dropped capabilities, `no-new-privileges`, and offline import conditions without persistent secret disclosure.

Controlled runtime verification confirmed that both proxies initialized with their intended mounted secrets and returned HTTP 200 health responses. Verification captured only access metadata and did not preserve secret values.

These checks verify a bounded runtime configuration. They do not authorize live email delivery.

### One-shot worker operating model

The worker is intentionally not a daemon, queue consumer, or persistent service. Its execution model is:

```text
One JSON object on stdin
         |
         v
Validate allowed request schema
         |
         v
Render approved template
         |
         v
Emit redacted audit event
         |
         v
Evaluate MSJARVIS_EMAIL_DRY_RUN
     +----+----+
     |         |
     v         v
  true       false
     |         |
     v         v
Audit and    Read worker token
exit         Forward to auth proxy
              |
              v
          Exit after outcome
```

The worker’s `main()` function reads one JSON object using standard input, processes it once, and exits. It is therefore not correctly deployed as a detached persistent container with no supplied request payload.

The controlled invocation pattern is:

```bash
docker compose \
  --profile email-worker-disabled \
  -f "$HOME/msjarvis-resend-email-pilot/docker-compose.email-worker.design.yml" \
  run --rm --no-deps --no-TTY -T email-worker < approved-request.json
```

The profile name is retained for deliberate activation control. It does not by itself establish production approval.

In the verified configuration, `MSJARVIS_EMAIL_DRY_RUN=true`. The worker therefore audits the allowed request and exits before it loads the worker token or sends a request to the authentication proxy.

### Secret-delivery boundary

The current local Compose secret mounts are an evidence-backed pilot mechanism for controlled email services. They are not the final production secret-management architecture.

Before production activation:

- Secret values must not be embedded in source, images, Compose YAML, shell history, rendered configuration captures, logs, or evidence.
- Each service must receive only the secret material it requires.
- Secret rotation, revocation, recovery, access review, and incident response must be governed and auditable.
- Production secret delivery must support intended non-root runtime identities without broadening access.
- All pilot, recovery, and pre-production credentials must be rotated during any approved production cutover.
- A secret-management outage must fail protected capabilities safely and must have a tested recovery procedure.
- The production system must not rely on undocumented host-file ownership behavior.
- Recovery evidence must not contain full secret-bearing environment files, raw connection strings, provider keys, or authorization tokens.

Local file-backed Compose secrets are not accepted as the target production mechanism for the complete MountainShares / Ms. Jarvis architecture or for an institutional multi-user email-support system.

### Current provenance and admission state

Runtime-authority signature verification and fail-closed runtime admission are implemented in the trust-development boundary.

The recovered Main Brain and Hilbert State services demonstrate that legacy runtime reconstruction can be brought under a scoped declarative ownership model. That operational achievement does not substitute for:

- A signed production Runtime Authority Manifest.
- Immutable image-digest pinning for every service.
- Governed SBOM review.
- Approved deployment authority.
- Production-grade secret delivery.
- Institutional operations approval.
- Complete dependency ownership and failure contracts.

These results establish meaningful runtime-authority, runtime-admission, runtime-isolation, controlled-email-pilot, and administrative-recovery evidence.

They do not establish final production deployment authority.

---

## 6. User Sovereignty Domain

```text
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
```

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

The controlled email-delivery pilot and administrative recovery work do not alter user-sovereignty requirements. A request to render, audit, or eventually deliver an email must be separately authorized under applicable institutional, user, and policy controls.

The current dry-run worker accepts only an explicit limited test template and does not establish a general-purpose user messaging authority.

The recovered Main Brain must not be interpreted as having unrestricted authority to retrieve or expose private-memory material merely because the service is healthy and reachable.

---

## 7. Operational Trust Boundary

```text
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
```

The Guardian evaluates whether a protected operation is permitted.

The Projection Service verifies resulting authorization and creates the bounded context available to Ms. Jarvis.

The reasoning layer is not an authority oracle. It cannot expand the scope of a valid authorization receipt.

The recovered Main Brain is an application-runtime component within this boundary. Its operational recovery does not make it the authority for caller authentication, policy evaluation, receipt issuance, private-memory projection, governance decisions, or Commons contribution.

A healthy Main Brain service must not bypass the Guardian, substitute a runtime-local configuration for verified authorization, or silently degrade into unrestricted private-memory access if an authorization dependency is absent.

### Administrative core operational boundary

The current administrative core operates within a narrower service relationship:

```text
Local Administrator
        |
        v
Scoped Recovery Manifest
        |
        v
jarvis-main-brain
        |
        +------------------------+
        |                        |
        v                        v
jarvis-chroma              jarvis-hilbert-state
        |                        |
        v                        v
Vector-state dependency     Hilbert state interface
```

The intended recovery boundary is:

- Main Brain receives local traffic only through its loopback-bound host port.
- Hilbert State receives local traffic only through its loopback-bound host port.
- Main Brain uses the declared internal Chroma service endpoint rather than assuming host-loopback reachability from inside the container.
- Required inter-service communication remains limited to explicitly attached networks.
- Main Brain and Hilbert State retain their scoped service ownership under `jarvis-legacy-recovery`.
- Shared dependencies may remain separately owned during recovery, but their interfaces, names, ports, networks, health conditions, and failure modes must be documented before administrative-production promotion.
- A broad aggregate Compose invocation must not silently alter the recovered pair.

The operational recovery path must preserve the distinction between:

```text
Service reachable
    !=
Service healthy under a declared contract
    !=
Service approved for protected operations
    !=
Service production-authorized
```

### Controlled email operational boundary

The controlled email component has a narrower and separate operational boundary:

```text
Approved Request Payload
     |
     v
Request Schema Validation
     |
     v
Approved Template Rendering
     |
     v
Redacted Audit Event
     |
     v
Dry-Run Policy Gate
     |
+----+---------------------------+
|                                |
v                                v
Dry-run enabled                 Dry-run disabled
|                                |
v                                v
Audit and exit                 Worker token validation
                                     |
                                     v
                              Auth-proxy verification
                                     |
                                     v
                              Egress-gateway request
                                     |
                                     v
                         Authorized external provider request
```

The currently verified default path ends at `Audit and exit`.

The current worker supports only the defined `email_delivery_test` template. Its allowed request fields are constrained to:

- `template`.
- `recipient`.
- `idempotency_key`.
- `template_data`.

The worker validates the request before rendering. The current stage permits only empty `template_data` for the allowed template.

The worker’s audit output is intentionally redacted. It records event type, template identifier, UTC time, and SHA-256 commitments for relevant request and rendered-output values rather than raw recipient, subject, body, or idempotency values.

### Current implementation state

The front portion of the primary trust boundary is materially implemented and, in several respects, verified at the decision boundary.

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
- A separate hardened runtime-isolation pilot for the egress, Redis, admission API, and privacy-worker boundary.
- A separate controlled email pilot with one-shot worker validation, non-root proxy isolation, narrow secret placement, and verified default dry-run behavior.
- Administrative recovery and loopback-only operation of the Main Brain and Hilbert State core pair under the dedicated `jarvis-legacy-recovery` project.

The complete private-memory projection chain is not yet production-complete.

The controlled email component is also not a complete production workflow. It currently lacks institutional caller authentication, durable job handling, tenant-aware authorization, and an approved transition to live delivery.

The recovered administrative core is not yet a complete as-built administrative-production stack. It currently lacks a fully consolidated authoritative dependency inventory, immutable binding for all service images, universal declared health contracts, governed production secret delivery, and complete release/rollback governance.

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

The controlled email pilot does not bypass MAR requirements for any future protected-memory-derived message. If a future email workflow uses private-memory context, recipient identity, or protected institutional records, the relevant MAR, PDR, projection, tenant, and policy controls must be validated before that context may be released to the email-rendering path.

The recovery of Main Brain and Hilbert State likewise does not bypass MAR requirements. A recovered application runtime may receive protected context only when it is the approved recipient runtime identified by a valid receipt chain and when all required scope, expiry, policy, and revocation checks succeed.

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

The controlled email dry run does not issue or consume a PDR because it does not access protected-memory material, invoke a protected capability, or initiate a live delivery request.

A future live email workflow that uses protected data or constitutes a governed institutional action must not treat a generic dry-run result as a replacement for the applicable PDR and authorization chain.

The recovered Main Brain and Hilbert State services do not obtain independent policy authority from administrative recovery. Any future protected operation through either service must validate the required PDR and related authorization chain.

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

The controlled email pilot does not create a Projection Receipt because its verified dry-run request uses a fixed permitted test template with no private-memory projection. This is a deliberate limitation.

It must not be generalized into a claim that email rendering is approved to consume unrestricted reasoning context, user records, or institutional data.

The recovered Main Brain and Hilbert State services do not create authority to bypass the projection boundary. If either becomes a recipient of protected context, its exact immutable runtime identity, approved service role, receipt binding, policy scope, and revocation state must be verified before release of that context.

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
- Any future live email delivery that is classified by active policy as a protected, high-impact, tenant-scoped, or institutionally governed action.
- Any release of protected context to a recovered or newly deployed application runtime.

```text
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
```

A general chat interface may remain available during Guardian outage only if it cannot access protected user memory, protected identity data, protected Commons functions, governance capabilities, or governed delivery functions.

The system may provide a clearly labeled, non-personalized response when protected capabilities are unavailable.

It must not silently degrade into unauthorized private-memory access or an unauthorized delivery path.

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

The current controlled email worker does not claim to be a Guardian-authorized institutional support workflow. It is a fixed-scope, manually invoked dry-run component.

Any expansion to user-initiated, administrator-initiated, support-initiated, or automated live messaging must first define the relevant policy classification and enforce the applicable Guardian, identity, authorization, tenant, and approval controls.

The recovered Main Brain and Hilbert State pair is likewise not a Guardian-authorized replacement for governance. The pair may provide application and state functions within an approved runtime boundary, but it may not independently issue, interpret, broaden, or override authority receipts.

### Guardian and recovered-runtime requirements

Before a recovered service can participate in a protected production workflow, all of the following must be true:

- Its image is pinned to an approved immutable digest.
- Its approved service identity is recorded in the Runtime Authority Manifest.
- Its required networks, dependencies, ports, mounts, and health contract are declared.
- Its deployment is authorized for the exact runtime configuration in use.
- Its secret-delivery path is approved and auditable.
- Its role in the receipt chain is explicitly defined.
- It receives only the minimum protected context permitted by an applicable MAR and Projection Receipt.
- Its admission and runtime identity are verified before protected context is released.
- Its failure behavior is fail closed for protected capabilities.
- Its recovery, rollback, and incident procedures are defined and tested.

Administrative recovery may establish the conditions for this work. It does not satisfy them automatically.

---

## 12. Commons Contribution Domain

The Commons receives explicitly authorized transformations, not raw private-vault graphs.

```text
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
```

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

The controlled email pilot is not a Commons-contribution path. Its redacted local audit events are operational evidence for a bounded test workflow and must not be repurposed as Commons data, user-profile data, institutional analytics, or contribution evidence without a separate authorized transformation and applicable governance approval.

The administrative recovery of Main Brain and Hilbert State is not a Commons-contribution event. Recovery logs, health checks, runtime metadata, Compose configurations, and evidence packages must not be repurposed as Commons inputs unless a separate authorized transformation, retention policy, privacy review, and governance approval permit that use.

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
- Administrative Recovery Record.
- As-Built Runtime Contract Record.
- Deployment Approval Record.
- Rollback Authorization Record.

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

### Administrative recovery evidence

Administrative recovery is only credible when it is supported by evidence adequate to reconstruct and review the operating claim without exposing credentials or protected information.

The recovery record for a service must include, as appropriate:

- Source and configuration provenance.
- Original observed runtime identity.
- Reconstructed Compose or deployment contract.
- Container image reference and, where available, immutable digest.
- Network membership and dependency endpoints.
- Published-port scope.
- Mounts, including read-only and writable requirements.
- Runtime user, capability, and filesystem-hardening settings where applicable.
- Environment-variable names and configuration references, excluding values.
- Health-check method and observed result.
- Dependency connectivity verification.
- Pre-change and post-change runtime evidence.
- Rendered configuration checksums after secret redaction.
- Rollback image and manifest references.
- Administrative reviewer and approval record.

The recovery record must not include:

- Private keys.
- Passphrases.
- Seeds.
- Raw bearer tokens.
- API keys.
- Passwords.
- Unredacted database URLs.
- Full secret-bearing environment files.
- Raw authorization headers.
- Session tokens.
- Plaintext protected user content.
- Unredacted email recipients, message bodies, worker tokens, or provider keys.
- Any other material whose retention would expand access beyond the approved evidence purpose.

A recovered service may be described as **verified operationally recovered** only when its declared recovery contract has been checked against observed live state and its required local health behavior has been verified.

It may be described as **as-built administratively governed** only when it also has a named lifecycle owner, approved release contract, defined rollback procedure, dependency ownership record, change-control process, and an auditable secret-delivery path.

### Controlled email audit boundary

The controlled email worker emits limited audit events:

- `email_dispatch_requested`
- `email_dispatch_dry_run`
- `email_dispatch_forwarded_to_auth` only when dry run is disabled and a forwarding attempt succeeds

The verified dry-run path emitted:

- `email_dispatch_requested`
- `email_dispatch_dry_run`

It did not emit the forwarding event.

For the current permitted template, audit events include:

- Event name.
- UTC timestamp.
- Template identifier.
- SHA-256 commitment of the recipient.
- SHA-256 commitment of the idempotency key.
- SHA-256 commitment of the rendered subject.
- SHA-256 commitment of the rendered body.

They do not intentionally include:

- Raw recipient address.
- Raw idempotency key.
- Raw subject.
- Raw message body.
- Worker authentication token.
- Provider API key.
- Authorization header values.

Hashing reduces direct disclosure but does not automatically make a value anonymous. Low-entropy or predictable inputs may remain susceptible to correlation or guessing. Audit retention, access, aggregation, and disclosure rules must therefore remain governed.

### Evidence and sealing

The trust-development process establishes evidence capture, reproducibility capture, trust gates, review gates, promotion seals, runtime verification artifacts, and durable evidence records.

Verification claims must be tied to preserved evidence rather than an unrecorded statement that a test once passed.

Runtime evidence must not contain:

- Private keys.
- Passphrases.
- Seeds.
- Runtime secrets.
- Full secret-bearing environment files.
- Database connection URLs containing credentials.
- Rendered proxy configuration containing active shared secrets.
- Raw authorization headers.
- Session tokens.
- Plaintext protected user content.
- Raw worker-authentication tokens.
- Raw provider API keys.
- Secret-bearing Compose-rendered content.
- Raw recipient information, message bodies, or unredacted institutional support records unless such retention is separately approved and governed.
- Host-specific recovery material that unnecessarily reveals private network topology, personal filesystem layouts, or unrelated service credentials.

A capability may be described as:

- Defined.
- Implemented.
- Verified.
- Sealed.
- Promoted.
- Administratively recovered.
- As-built administratively governed.
- Production-authorized.

These are distinct states.

### Controlled email evidence record

The current email pilot generated evidence for:

| Verification activity | Result |
|---|---|
| Distroless auth and egress image build | Passed |
| Auth and egress offline import with synthetic tmpfs credentials | Passed |
| Proxy health checks with real mounted Docker secrets | Passed |
| Effective in-container secret metadata check | Passed; intended non-root ownership and mode `0400` observed |
| Worker image offline import | Passed after inclusion of `email_templates.py` |
| Full-stack dry-run request | Passed |
| Worker request audit event | Emitted |
| Worker dry-run audit event | Emitted |
| Worker forwarding indicator during dry run | Not observed |
| Intentional provider contact during dry run | Not performed |
| Intentional email send during dry run | Not performed |

The full-stack dry run used the only currently permitted template, `email_delivery_test`, with a synthetic `.invalid` recipient. Audit output recorded commitments rather than raw recipient, subject, body, or idempotency material.

These artifacts are local implementation evidence. They are not independently signed production authority artifacts unless and until they are incorporated into an approved, governed evidence and release process.

### Administrative core evidence record

The current Main Brain and Hilbert State recovery record includes evidence that:

| Recovery activity | Result |
|---|---|
| Dedicated recovery project created | Verified as `jarvis-legacy-recovery` |
| Main Brain legacy-compatible service started | Running |
| Hilbert State service started | Running |
| Main Brain local port scope verified | Loopback-only `127.0.0.1:18058 -> 8008` |
| Hilbert State local port scope verified | Loopback-only `127.0.0.1:18092 -> 8081` |
| Main Brain Chroma endpoint corrected | Declared as internal `jarvis-chroma:8000` |
| Main Brain health behavior | Verified reachable at recovery time |
| Hilbert State health behavior | Verified reachable at recovery time |
| Recovery manifest retained | Available as legacy-compatible recovery contract |
| Broad aggregate project ownership | Explicitly not accepted as recovered-pair lifecycle owner |
| Full administrative-production closure | Pending |

The current record demonstrates a controlled recovery boundary. It does not establish immutable release closure, governance activation, final secret-management architecture, or complete production operations.

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
| Privacy-gateway runtime-isolation pilot | Verified. Redis, egress, admission API, and privacy worker passed final runtime checks with read-only roots, dropped capabilities, non-root execution where configured, Redis authentication, proxy validation, and egress enforcement. |
| Egress boundary | Verified for `/chat`: unauthenticated POST rejection with HTTP 403 and non-POST rejection with HTTP 405. |
| Pilot secret rotation | Egress and Redis credentials previously exposed during remediation were rotated. Current local environment-file delivery is temporary and not production-ready. |
| Controlled email topology | Verified for one-shot worker, authentication proxy, and egress-gateway separation. The worker does not receive the provider key; the authentication proxy does not receive the provider key; the egress gateway does not receive the worker token. |
| Email auth proxy | Verified as a pinned distroless Python runtime running under a dedicated non-root identity, with explicit Python entrypoint, read-only root filesystem, dropped capabilities, no-new-privileges, and restricted secret access. |
| Email egress gateway | Verified as a pinned distroless Python runtime running under a dedicated non-root identity, with explicit Python entrypoint, read-only root filesystem, dropped capabilities, no-new-privileges, and restricted provider-key access. |
| Email secret mount metadata | Verified during controlled runtime checks with service-specific ownership and mode `0400`; values were not read or logged. |
| Email worker image | Verified after packaging correction. `email_worker.py` and `email_templates.py` import successfully under the worker image’s dry-run configuration. |
| Email worker dry run | Verified. A permitted one-shot request generated `email_dispatch_requested` and `email_dispatch_dry_run` audit events and exited without a forwarding event. |
| Email worker persistence | Not implemented by design. The worker is stdin-driven and exits after one request; it is not a queue consumer, daemon, or persistent service. |
| Live email delivery | Not enabled or production-authorized. The verified default is `MSJARVIS_EMAIL_DRY_RUN=true`. |
| Institutional multi-user support workflow | Not implemented or production-authorized. Institutional identity, tenant isolation, roles, durable work orchestration, operational support controls, and live-send governance remain pending. |
| Main Brain recovery | Verified operationally recovered under `jarvis-legacy-recovery`, using loopback-only host exposure and an explicit internal Chroma endpoint. It is not yet a complete immutable production release. |
| Hilbert State recovery | Verified operationally recovered under `jarvis-legacy-recovery`, with loopback-only host exposure and retained network/mount contract. Its image binding must be made immutable before production promotion. |
| Core-pair lifecycle owner | Defined for recovery as `jarvis-legacy-recovery`. Broader dependency ownership and full-stack as-built authority remain incomplete. |
| Broad aggregate stack | Operationally present but not accepted as the authoritative lifecycle owner for the recovered Main Brain and Hilbert State pair. Its layered historical definitions require inventory and classification. |
| Docker health contracts for recovered core | External health reachability verified; complete declarative Docker health checks and dependency-readiness policy remain pending. |
| External secret manager | Not yet implemented. Required before production activation. |
| MAR | Defined and supported by receipt infrastructure; complete protected-memory production path remains pending. |
| Projection Receipt | Defined; complete production projection boundary remains pending. |
| Projection Service | Not production-activated. |
| Reasoning isolation | Existing semantic-memory and reasoning capabilities must remain behind the authorization and projection boundary. |
| Commons receipts and governance | Defined; production implementation remains pending. |
| Revocation | Verified at the Guardian decision boundary; projection-path integration remains pending. |
| Adversarial matrix | Partially closed. Decision-boundary cases are verified; expiration, policy mismatch, unapproved-image, outage, secret-manager failure, full projection-chain, multi-user email-policy, and complete administrative-recovery cases remain. |
| Custodian ceremony | Started but incomplete. It grants no authority until the required independent custodians, remaining enrollment records, and threshold-signed governance registry are complete. |
| Release-candidate evidence | Completed as a tested, evidence-backed, fail-closed package. It is not an active authority system. |
| Live authority system | Not active. Production activation remains blocked pending governance, signer, secret-management, projection, release, institutional operating, and final authorization prerequisites. |

An implemented component is not automatically production-authorized.

A verified pilot is not automatically a production release.

A sealed evidence artifact is not automatically an active authority system.

A healthy service is not automatically an authorized service.

A recovered service is not automatically an as-built production service.

A successful dry run is not an approved live action.

---

## 15. Verification Requirements

| Capability | Required proof | Current status |
|---|---|---|
| Approved production service | Pinned digest, SBOM, Runtime Authority Manifest, governance approval, health checks, contract checks, rollback evidence | Partially demonstrated; final production release closure remains |
| Recovered administrative service | Reconstructed manifest, scoped lifecycle owner, observed network/port/mount contract, dependency checks, health evidence, rollback reference, redacted evidence | Demonstrated for Main Brain and Hilbert State recovery pair |
| As-built administrative production service | Approved declarative owner, immutable image, dependency ownership, health and readiness contract, secret-delivery record, change control, rollback procedure, operational owner | Not yet complete for the core pair or the broader stack |
| Runtime authority | Valid signed manifest, trusted signers, policy compatibility, image binding | Signature and admission evidence demonstrated; final production governance remains |
| Guardian Authority Bundle | Production-signed bundle satisfying required roles, threshold, expiry, key validity, and revocation state | Test-provisioned mechanism verified; production bundle remains |
| Caller authenticity | Valid bundle-sourced caller credential before protected decision logic | Implemented and verified fail closed |
| Signed operation intent | Valid signature, trusted active subject key, caller-subject binding, request-operation binding, revocation enforcement | Implemented and verified fail closed |
| PDR issuance | Valid production Guardian signer, trusted registry entry, policy binding, durable consumption, cryptographic signature | Verified under provisioned non-production signer; production enrollment remains blocked |
| Secret delivery | Approved external manager, least privilege, non-root compatibility, auditable rotation and recovery | Pilot secret isolation verified; production mechanism not complete |
| Runtime isolation | Read-only roots, least privilege, scoped writable paths, tested egress enforcement, authenticated dependencies | Verified for the privacy-gateway pilot baseline and controlled email proxy pair |
| Recovered core service health | Explicit endpoint or Docker health check, dependency connectivity, expected local port scope, evidence capture | Local health behavior and loopback publication verified; declarative Docker health contracts remain pending |
| Main Brain dependency binding | Explicit Chroma service endpoint, required networks, dependency health behavior, defined failure mode | Internal Chroma endpoint verified as `jarvis-chroma:8000`; full dependency contract pending |
| Hilbert State runtime binding | Immutable image, required network attachments, read-only mounts, health contract, rollback reference | Recovered runtime contract established; immutable image binding and full production contract pending |
| Aggregate-stack governance | Inventory, classification, approved lifecycle owner for each retained service, decommission plan for orphans | Pending |
| Email dry run | Approved fixed template, schema validation, dry-run policy enabled, redacted audit evidence, no forwarding event | Verified for one-shot controlled invocation |
| Email live send | Explicit governance approval, approved sender/domain, recipient controls, rate limits, policy enforcement, audit, kill switch, authorized secrets, and controlled egress | Not authorized or verified |
| Persistent email processing | Durable queue or service contract, idempotency persistence, retry/backoff, dead-letter process, observability, concurrency limits, recovery tests | Not implemented |
| Institutional multi-user support | Institutional SSO/MFA, tenant isolation, server-side authorization, support roles, privacy review, operational ownership, incident and retention controls | Not implemented |
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
| Production observability | Centralized redacted logging, metrics, tracing, alerting, retention, incident ownership, and tested recovery | Pending |
| Recovery rollback | Exact prior image/manifest reference, data-impact assessment, local health verification, approved rollback procedure | Recovery evidence partially available; formal rollback procedure pending |
| Change governance | Reviewed release manifest, preflight, approval, scoped apply, post-change verification, retained evidence | Informally applied during recovery; formal production process pending |

## 16. Pilot Implementation and Production Closure Order

### 16.1 Purpose and status

This section records the current implementation boundary and the remaining closure work required before any component may be represented as production-authorized.

The system has progressed beyond an architecture-only design. It now includes meaningful, evidence-backed implementation and verification of trust-boundary controls, receipt infrastructure, Guardian decision-boundary controls, a hardened privacy-gateway runtime pilot, a controlled email-processing pilot, and the administrative recovery of the Main Brain and Hilbert State core runtime pair.

Those accomplishments are real and operationally valuable. They do not activate production authority, authorize protected-memory access, establish governance approval, permit a live authority system, authorize live email delivery, establish an institutional multi-user support platform, or complete the broader Jarvis stack’s administrative-production closure.

The present status is:

```text
RELEASE STATE:
tested, evidence-backed, fail-closed release candidate

AUTHORITY STATUS:
inactive

DEPLOYMENT ADMISSION:
blocked pending production governance, signing, runtime authority,
protected-memory, projection, secret-management, institutional operating,
and activation conditions

ADMINISTRATIVE CORE STATE:
Main Brain and Hilbert State recovered under a dedicated scoped project

CORE-PAIR OPERATING STATE:
locally running, loopback-bound, dependency-connected, health-verified

AS-BUILT ADMINISTRATIVE PRODUCTION:
not complete

CONTROLLED EMAIL STATE:
verified one-shot dry-run pilot

LIVE EMAIL STATE:
disabled and not production-authorized

EMAIL WORKER MODE:
stdin-driven single-request process; not persistent
```

The verified privacy-gateway pilot is a runtime-isolation baseline.

The verified email pilot is a bounded dry-run processing baseline.

The recovered Main Brain and Hilbert State pair is an administrative recovery baseline.

None of these independently completes the MountainShares / Ms. Jarvis production trust architecture.

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
15. The privacy-gateway runtime-isolation pilot has been deployed and verified.
16. Pilot egress and Redis credentials exposed during remediation were rotated.
17. Final privacy-gateway pilot verification confirms operational Redis, egress, admission API, and privacy worker services with intended runtime controls.
18. A controlled three-service email boundary has been implemented: worker to authentication proxy to egress gateway.
19. Email proxy images have been rebuilt as pinned distroless runtimes with numeric non-root identities, explicit entrypoints, read-only roots, dropped capabilities, no-new-privileges, and scoped writable temporary storage.
20. The worker authentication secret and provider API key have been separated so that each is mounted only into its respective service boundary.
21. Offline authentication-proxy and egress-proxy initialization was verified with synthetic credentials created only in ephemeral tmpfs and no network access.
22. Controlled health verification confirmed that both proxies initialize with their existing Docker secret mounts and return successful health responses.
23. Controlled metadata verification observed effective service-specific secret ownership and mode `0400` without reading secret contents.
24. The worker image packaging defect was corrected by including `email_templates.py` with `email_worker.py`.
25. The corrected worker imported successfully offline with `MSJARVIS_EMAIL_DRY_RUN=true`, no network, and no mounted secrets.
26. A full-stack one-shot dry run produced the expected request and dry-run audit events without forwarding to the authentication proxy, intentionally contacting the provider, or sending email.
27. Controlled Compose image references now retain verified release-tagged worker, authentication, and egress images.
28. The Main Brain was recovered under the dedicated `jarvis-legacy-recovery` project using the legacy-compatible recovery manifest.
29. The recovered Main Brain is locally exposed only through `127.0.0.1:18058` to its internal application port.
30. The Main Brain Chroma dependency was explicitly corrected to use the internal service endpoint `jarvis-chroma:8000`.
31. Hilbert State was recovered under the same dedicated project and is locally exposed only through `127.0.0.1:18092` to its internal application port.
32. Main Brain and Hilbert State were both observed running and health-reachable at recovery verification time.
33. The recovered pair has been separated administratively from the broad `msjarvis-rebuild` aggregate stack for lifecycle-control purposes.
34. Recovery evidence, runtime inspection material, manifests, and verification records were preserved without making the recovery equivalent to production authorization.

### 16.3 Remaining closure work

The remaining work must preserve the same fail-closed discipline.

#### Governance and authority

1. Establish the authorized production governance decision and corresponding production policy registry.
2. Establish the required production governance-board authority and enroll a real governance-board signer.
3. Complete the independent-custodian enrollment and governance activation ceremony.
4. Produce a threshold-signed active production governance registry.
5. Establish production key-rotation, revocation, incident-response, and emergency-suspension procedures.
6. Define the institutional authority authorized to approve multi-user support workflows, protected messaging functions, and any transition from dry run to live email delivery.
7. Define sender, recipient, template, retention, escalation, and emergency-stop policy for every live delivery workflow.
8. Define the administrative authority authorized to promote a recovered service from recovery status to an as-built production service.
9. Define required review and approval thresholds for core service changes, rollback, dependency migration, and stack decommissioning.

#### Guardian signer and PDR activation

10. Establish dedicated Guardian PDR signing authority in approved secure custody.
11. Enroll its public key, with the required `guardian` role, in the production trusted signer registry.
12. Produce a production Guardian Authority Bundle carrying genuine production approvals and valid expiry.
13. Demonstrate a live, cryptographically valid PDR issuance path against production authority.
14. Demonstrate durable production receipt consumption and replay denial.
15. Ensure Guardian outage and signer failure deny protected capabilities rather than creating fallback authorization.
16. Determine and enforce which institutional support and live email actions require a PDR, MAR, additional approval receipt, or all of these controls.

#### Runtime authority and secrets

17. Build and verify one reproducible pilot release from a fully governed signed Runtime Authority Manifest.
18. Pin exact production image digests, SBOMs, dependencies, policies, health contracts, rollback targets, and release approvals.
19. Replace mutable image references in recovered services, including the current Hilbert State image reference, with approved immutable release bindings.
20. Define a canonical release manifest for the recovered Main Brain and Hilbert State pair that supersedes recovery-only naming while preserving its verified contract.
21. Define Docker health checks, readiness contracts, failure modes, restart behavior, and dependency ordering for the recovered core pair.
22. Implement approved external secret management compatible with the non-root runtime.
23. Replace temporary local environment-file and local file-backed Compose secret delivery.
24. Rotate all pre-production credentials during the governed production cutover.
25. Verify that no secret values appear in source, Compose configuration, rendered configuration output, evidence, logs, shell history, or repository history.
26. Define and test secret-manager outage, recovery, rotation, revocation, and break-glass behavior.
27. Establish vulnerability management, SBOM review, image scanning, patch cadence, and release-dependency review processes.

#### As-built administrative stack closure

28. Inventory every running service, container, image, volume, network, port, mount, label, and dependency relationship in the broad Jarvis environment.
29. Classify each running component as core production, platform dependency, data service, security boundary, controlled pilot, candidate, historical artifact, or orphan.
30. Assign each retained production service exactly one approved declarative lifecycle owner.
31. Record the approved project boundary for Main Brain and Hilbert State and prevent broad aggregate Compose actions from unintentionally changing the pair.
32. Identify every external network, volume, database, local path, and shared dependency required by the core pair.
33. Define service-to-service DNS, port, protocol, authentication, health, readiness, timeout, and failure semantics for each core dependency.
34. Define persistent-data ownership, backup, restore, migration, retention, and rollback procedures for each production-relevant state store.
35. Create a decommission, migration, or containment plan for duplicate, abandoned, experimental, historical, and orphaned services.
36. Establish a rendered-manifest review process that redacts secrets and compares expected contract state with live runtime state.
37. Define pre-change, change, post-change, and rollback evidence requirements.
38. Establish formal production change governance for scoped service operations, including explicit approval before destructive or broad lifecycle actions.
39. Demonstrate that the complete core service set can be recreated from approved manifests and governed dependencies without reliance on undocumented host state or emergency reconstruction steps.
40. Retain recovery artifacts as historical evidence while ensuring that no recovery-only files become accidental permanent production authority.

#### Institutional multi-user support readiness

41. Implement institutional single sign-on using the approved identity provider and required multifactor-authentication policy.
42. Define and enforce server-side roles and permissions, including least-privilege support, administrator, auditor, and governance roles as applicable.
43. Define a tenant or organizational-boundary model and ensure every protected query, request, receipt, audit event, and workflow is scoped and enforced server-side.
44. Implement user lifecycle controls: account provisioning, deprovisioning, suspension, access review, role change, and session revocation.
45. Define data classification, consent, retention, deletion, disclosure, and support-record handling requirements.
46. Complete institutional privacy, security, accessibility, procurement, legal, and records-management review as applicable to the intended deployment.
47. Establish support ownership, incident escalation, on-call responsibility, operational runbooks, and service-level objectives.
48. Establish centralized redacted logging, monitoring, metrics, tracing, alerting, retention, and audit access controls.

#### Persistent email processing and live-send controls

49. Do not deploy the current stdin-driven worker as a persistent service. It is a one-shot process by design.
50. If persistent processing is required, design and implement a durable input mechanism, such as an authenticated API plus durable queue, with clear command ownership and authorization.
51. Implement durable idempotency storage rather than relying solely on caller-provided request values.
52. Implement retry, backoff, timeout, failure classification, dead-letter, replay-review, and recovery procedures.
53. Implement concurrency limits, quota enforcement, rate limits, recipient-domain policy, template allowlists, sender-domain controls, and abuse prevention.
54. Implement a live-send control plane with environment isolation, explicit change approval, runtime policy check, audit trail, and immediate kill switch.
55. Verify that `MSJARVIS_EMAIL_DRY_RUN=true` remains the default and that disabling it requires an approved, recorded, policy-governed activation process.
56. Conduct controlled live-send testing only after all required governance, operational, and provider-side sender-domain prerequisites are complete, using an approved test recipient and an explicit, auditable authorization.
57. Verify external-provider failure handling, delivery-status processing, bounce and complaint handling, revocation behavior, and recipient suppression controls before live institutional use.

#### Protected memory and projection

58. Establish signed runtime-admission chains for the Projection Service and reasoning recipient.
59. Implement and verify MAR issuance and validation in the protected-memory path.
60. Implement Projection Service verification before protected retrieval.
61. Remove unrestricted private-memory access from reasoning paths.
62. Implement and verify Projection Receipts and their output commitments.
63. Bind recipient runtime identity, projection scope, purpose, policy, expiry, and use count before reasoning-context release.
64. Integrate revocation into protected-memory and projection authorization checks before every new projection.
65. Ensure that any email generated from protected-memory or institutional data receives only an authorized minimum context projection and remains within the relevant scope, purpose, recipient, and retention constraints.
66. Ensure that recovered or newly promoted core application services can receive protected context only through approved recipient-runtime and receipt bindings.

#### Commons and full-chain verification

67. Implement Contribution and Transformation Receipts before publishing Commons aggregates.
68. Establish Commons Epoch Root governance and required privacy attestations.
69. Close the remaining adversarial verification cells:
- Authority and receipt expiration.
- Policy-version mismatch.
- Unapproved-image access.
- Guardian outage.
- Secret-manager outage.
- PDR, MAR, projection, and response replay.
- Full protected-memory projection chain.
- Tenant-isolation failure.
- Role-escalation attempt.
- Cross-tenant audit disclosure.
- Email request duplication.
- Unauthorized live-send attempt.
- Recipient-policy failure.
- Queue, retry, and dead-letter recovery.
- Recovery manifest drift.
- Unapproved core-service image substitution.
- Aggregate-stack lifecycle interference.
- Dependency-health or network-contract failure.
70. Demonstrate durable shared-ledger conformance before any multi-replica deployment requiring shared receipt consumption.
71. Exercise backup recovery, rollback, incident response, observability, evidence-retention, and core-stack recreation procedures.

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

For an as-built administrative-production core stack, all of the following must also be true:

- Every retained core service has one approved declarative lifecycle owner.
- Main Brain, Hilbert State, and all required dependencies are represented by approved version-controlled manifests.
- All production-relevant image references are immutable and bound to approved SBOM and release records.
- Service networks, ports, mounts, volumes, external dependencies, and data stores are explicitly documented.
- Health checks, readiness checks, dependency failure behavior, restart policy, and rollback procedures are declared and tested.
- Secrets are supplied by an approved governed mechanism and are absent from public documentation, evidence, logs, shell history, and rendered manifests.
- Persistent data has documented ownership, backup, restore, retention, and migration procedures.
- The production core can be recreated from approved artifacts without reconstructing undocumented legacy host state.
- Broad aggregate Compose operations cannot unintentionally take control of or destroy scoped core services.
- Operational ownership, incident response, change approval, and maintenance responsibilities are assigned.
- A contract-versus-live-state verification process is available and produces redacted evidence.

For a multi-user institutional-support deployment, all of the following must also be true:

- Institutional authentication, session management, and required multifactor controls are active.
- Tenant or organizational boundaries are enforced by trusted server-side identity and authorization controls.
- Roles, permissions, support workflows, and administrative boundaries are reviewed and tested.
- Privacy, retention, accessibility, and institutional operating requirements are approved.
- Centralized redacted observability, alerting, audit access, incident response, and operational ownership are active.
- Persistent workflow processing has a durable queue or equivalent controlled mechanism, idempotency storage, retries, dead-letter handling, and tested recovery.
- Live email is disabled by default and can be enabled only through an explicit, governed, auditable activation process.
- Sender identity, provider configuration, recipient safeguards, rate limits, suppression handling, and emergency kill-switch controls have been verified.
- Live delivery has been separately approved for the exact production release, configuration, and operating environment.

Until these conditions are satisfied, the correct description remains:

```text
A tested, evidence-backed, fail-closed release candidate with a verified
runtime-isolation pilot baseline, a verified controlled one-shot email
dry-run capability, and an administratively recovered Main Brain and
Hilbert State core pair; not a production-authorized live authority,
complete as-built administrative-production stack, multi-user
institutional-support platform, or live email-delivery system.
```

### 16.5 Immediate practical next project

The immediate next project is:

1. Production governance and signer enrollment.
2. Approved external secret-manager implementation.
3. Governed Runtime Authority Manifest and reproducible release closure.
4. Core-stack administrative inventory, ownership assignment, and immutable runtime binding.
5. Declarative health, readiness, rollback, data-ownership, and change-governance closure for Main Brain, Hilbert State, and their required dependencies.
6. Protected-memory MAR and Projection Service activation.
7. Institutional identity, authorization, and tenant-boundary design.
8. Durable, policy-governed email work orchestration if persistent processing is required.
9. End-to-end production-chain and administrative-stack adversarial verification.

The immediate next project is not another emergency Docker hardening change.

The privacy-gateway and controlled-email pilots have established hardened runtime baselines.

The Main Brain and Hilbert State recovery has established an administratively scoped core runtime baseline.

Production progress now depends on legitimate authority, signer custody, governed secret delivery, immutable release authority, complete core service ownership, protected-memory authorization and projection closure, institutional operating controls, and a deliberately designed live-delivery control plane.

---

## 17. Current Release Boundary

The current system state must be described as:

> A tested, evidence-backed, fail-closed release candidate with an administratively recovered core runtime, rather than a live authority system or complete as-built administrative-production stack.

The release boundary is intentionally inactive.

The recovered Main Brain and Hilbert State pair is operationally useful and locally stable. It remains within a bounded recovery scope and must not be represented as final production activation.

The current public or shareable evidence package must exclude:

- Private keys.
- Passphrases.
- Seeds.
- Runtime secrets.
- Signer private material.
- Full secret-bearing configuration.
- Plaintext protected data.
- Other sensitive authority material.
- Raw email recipients, message bodies, worker tokens, provider keys, or institution-specific support content unless explicitly approved under a separate governed retention process.
- Unredacted local host paths where they reveal sensitive infrastructure layout without an approved documentation purpose.
- Full container-inspection outputs when they include environment values, mount contents, access tokens, or unrelated dependency details.
- Unredacted Compose-rendered output when it contains secret values or credentials.
- Local recovery environment files and shell-history content.

The current pilot verification evidence demonstrates runtime isolation, service health, credential rotation, egress enforcement, Redis authentication, controlled email secret placement, proxy readiness, worker dry-run behavior, and fail-closed boundary controls without granting production authority.

The current recovery evidence demonstrates that the Main Brain and Hilbert State services can operate under a dedicated recovery project with loopback-only host exposure, explicit dependency addressing, and preserved runtime-contract evidence.

The custodian ceremony has begun but is incomplete. Partial enrollment grants no authority.

A candidate Guardian deployment topology may be technically deployable but remains unauthorized until the required governance, signer, authority-bundle, runtime-manifest, secret-management, institutional identity, operational, and protected-memory conditions are complete.

The controlled email topology may be technically runnable but remains restricted to verified one-shot dry-run behavior. It must not be represented as an authorized live email system or persistent support service until the relevant production controls are complete.

The recovered Main Brain and Hilbert State topology may be technically runnable and locally healthy but remains an administrative recovery boundary until immutable release binding, formal health and readiness contracts, dependency ownership, governed secrets, rollback governance, and core-stack closure are complete.

The architecture is designed to stop before live authority is granted when required governance, signing, registry, runtime, secret-delivery, identity, authorization, tenant, operational, delivery-policy, or projection conditions are absent.

It is also designed to stop before an emergency recovery configuration is silently reclassified as production merely because it remains running.

### Recovery-boundary operating rules

The following rules are normative for the current recovered core:

1. `jarvis-main-brain` and `jarvis-hilbert-state` remain lifecycle-owned by the dedicated `jarvis-legacy-recovery` project until a reviewed and approved migration establishes a successor owner.

2. Broad aggregate Compose operations must not be used to recreate, stop, remove, or modify the recovered pair unless the exact implications have been reviewed and an explicit change authorization exists.

3. The current loopback-only published ports are part of the recovery boundary. Any expansion of network exposure requires a separate reviewed security, policy, and operations decision.

4. Main Brain must use the declared internal Chroma service endpoint rather than relying on implicit host-loopback behavior from within a container.

5. A health response is operational evidence only. It does not authorize protected data access, policy decisions, Commons actions, or live email delivery.

6. Any image replacement, dependency relocation, network modification, mount change, secret change, port exposure, or runtime-configuration change must be treated as a scoped deployment change and must preserve rollback evidence.

7. Recovery manifests, local runtime configuration, and evidence must be treated as sensitive operational artifacts even when they contain no direct secret values.

8. The current recovery state must not be used to justify an unreviewed full-stack `up`, `down`, pruning, rebuild, or migration action against the broad historical environment.

9. The recovery boundary must remain fail closed for protected capabilities while production authority, projection controls, and institutional operating requirements remain incomplete.

10. Promotion from recovered status to as-built administrative production requires affirmative evidence against the administrative-production acceptance criteria in this document.

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

### Administratively recovered

A previously unavailable, ambiguous, or unmanaged runtime component has been reconstructed into a scoped operating contract; its observed service state, essential dependencies, network exposure, and local health behavior have been verified; and recovery evidence has been retained.

Administrative recovery does not imply an immutable release, complete service ownership, secret-management closure, production governance, or authority to perform protected operations.

### As-built administratively governed

A service or stack has an approved declarative lifecycle owner, immutable release binding, explicit dependency and data ownership, health and readiness contract, governed secret delivery, approved rollback procedure, operational ownership, documented change process, and evidence that the approved contract matches the live runtime.

As-built administrative governance is necessary but not sufficient for production authorization of protected capabilities.

### Production-authorized

The required governance authority, signing authority, runtime admission, policy, secret-management, release, institutional operating, and activation conditions exist and have been explicitly authorized.

These states must not be conflated.

> Implemented does not mean production-authorized.  
> Verified does not mean production-authorized.  
> Sealed evidence does not mean production-authorized.  
> Promoted does not mean production-authorized.  
> A hardened pilot does not mean production-authorized.  
> A recovered service does not mean as-built administratively governed.  
> An as-built administratively governed service does not automatically mean it is authorized for protected operations.  
> A release candidate does not mean an active authority system.  
> A successful dry run does not mean live delivery is authorized.  
> A running container does not mean a persistent service design is complete.  
> A healthy endpoint does not mean the service is authorized.  
> A valid provider key does not mean an institution has approved the action it could enable.  
> A broad Compose project does not mean its configuration is the approved source of truth.

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
- A controlled three-service email topology that separates worker authentication from external-provider credentials.
- Distroless, pinned, numeric-non-root authentication and egress proxy runtimes.
- Controlled secret-mount metadata verification without secret disclosure.
- Corrected worker packaging and offline import verification.
- A verified one-shot dry-run email workflow that renders only the approved test template, emits redacted audit events, and exits without forwarding or sending.
- Administrative recovery of Main Brain and Hilbert State under a dedicated scoped Compose project.
- Loopback-only host publication for the recovered Main Brain and Hilbert State services.
- Explicit Main Brain Chroma dependency addressing through the internal service endpoint.
- Preserved recovery manifests, runtime observations, health evidence, and administrative boundary records.
- Explicit separation of the recovered core pair from the broad historical aggregate stack for lifecycle-control purposes.

These accomplishments materially advance the implementation state.

However, the architecture deliberately preserves the remaining boundaries around:

- Final production governance authority.
- A production governance-board signer.
- A production Guardian PDR signer enrolled in the production trusted registry.
- A production Guardian Authority Bundle carrying genuine threshold approvals.
- Production policy registries.
- Approved external secret management.
- Governed immutable release authority.
- Immutable production image binding for every recovered core service.
- Canonical as-built manifests for Main Brain, Hilbert State, and all required dependencies.
- Declarative health, readiness, failure, restart, and rollback contracts.
- Complete service, dependency, network, volume, data, and lifecycle ownership inventory.
- Separation, containment, migration, or decommissioning of historical and orphaned aggregate-stack components.
- Persistent-data ownership, backup, restoration, retention, and migration controls.
- Production change governance and contract-versus-live-state verification.
- Projection Service admission.
- Reasoning-recipient admission.
- Complete MAR activation.
- Protected semantic projection.
- Removal of unrestricted private-memory access.
- Contribution and Transformation Receipts.
- Commons Epoch Root governance.
- Revocation integration into the protected-memory and projection path.
- Institutional authentication, multifactor controls, and account lifecycle management.
- Tenant isolation and server-side role-based or attribute-based authorization.
- Institutional privacy, retention, accessibility, security, and operational review.
- Durable multi-user work processing.
- Idempotency, retry, dead-letter, and recovery controls for persistent delivery work.
- Live email delivery governance, sender policy, recipient safeguards, rate controls, suppression handling, and emergency-stop capability.
- Centralized observability, incident response, backup recovery, and operating ownership.
- Remaining adversarial verification cells.
- Durable shared-ledger verification at production scale.
- Final reproducible release authorization.
- Completion of human custodian and governance activation.

The result is not an architecture claiming completion prematurely.

It is an architecture in which remaining work is expressed as explicit authority, implementation, administrative, operational, institutional, and verification gates rather than unspecified future work.

The governing principle remains unchanged:

> Integrity proves what happened. Authority proves who may cause it. Policy proves whether it was allowed.

The documentation records both sides of the current state:

> What has actually been built, tested, verified, sealed, promoted, and administratively recovered; and what remains deliberately blocked because the required authority, administrative closure, and production conditions have not yet been established.
