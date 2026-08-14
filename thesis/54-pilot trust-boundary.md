# MountainShares / Ms. Jarvis Trust Architecture v1.4

**Status:** Architecture Freeze Candidate — Runtime-Isolation, Controlled Email Pilot, and Production-Closure Update  
**Authority:** Canonical design reference for pilot trust-boundary work  
**Date:** 2026-08-14  
**Supersedes:** v1.3 (2026-08-12)  
**Scope:** Software provenance, runtime authority, user sovereignty, Commons integrity, policy-governed AI projections, receipt-based authorization, runtime isolation, controlled email delivery, and fail-closed governance boundaries.

---

## Revision Note (v1.3 → v1.4)

This revision incorporates the verified controlled email-delivery pilot into the architecture’s implementation and release-boundary record.

It does not activate production authority, authorize protected-memory access, enable live email delivery, establish a multi-user institutional-support service, or change the architecture’s non-goals. It records a verified local, one-shot, dry-run email-processing baseline and clarifies that the email component is a bounded pilot capability rather than an always-running, production-authorized worker system.

Concrete updates in this revision:

1. **Three-service email trust boundary verified.** The controlled email path consists of `email-worker → email-egress-auth → email-egress`. The worker holds no Resend API key. The authentication sidecar alone validates the worker shared token. The egress gateway alone receives the Resend API key and has the designated outbound network path.

2. **Distroless proxy runtime verified.** The auth and egress services use pinned `gcr.io/distroless/python3-debian13` runtime images at the verified immutable digest:
   `gcr.io/distroless/python3-debian13@sha256:1c680cdb442a9e7a89f64fd1706367c62302ea1f9ab80fdebdb72ae9fcded46f`.

3. **Least-privilege proxy execution verified.** The auth proxy runs as UID:GID `10002:10002`; the egress proxy runs as UID:GID `10003:10003`. Their root filesystems are read-only, Linux capabilities are dropped, `no-new-privileges` is enabled, and only scoped tmpfs paths are writable.

4. **Real-secret readiness verified without disclosure.** Controlled proxy checks confirmed that the mounted worker-auth token and Resend API key were regular files, accessible to their intended service identities, and effective as UID-owned mode-`0400` secrets. The verification recorded only metadata, not values.

5. **Email worker packaging corrected and verified.** The worker image now copies both `email_worker.py` and its required `email_templates.py` module. Offline imports passed with no network and no mounted secrets.

6. **One-shot dry-run behavior verified.** With `MSJARVIS_EMAIL_DRY_RUN=true`, the worker accepts one valid JSON request from standard input, validates and renders the permitted test template, emits redacted audit events, and exits without loading its worker token, forwarding to the authentication proxy, contacting Resend, or sending email.

7. **Persistent Compose image references updated.** The controlled Compose configuration now references the verified release-tagged worker, auth-proxy, and egress-proxy images. The profile remains intentionally disabled by default and must be explicitly enabled for a controlled invocation.

8. **Production boundary clarified.** The email component is not a persistent queue consumer, multi-user service, multi-tenant institutional-support platform, or live email-sending system. Production progress requires identity and authorization architecture, durable work handling, managed secrets, observability, operational governance, and explicit live-send controls.

No capability is upgraded to `production-authorized` by this revision.

The system remains a tested, evidence-backed, fail-closed release candidate.

---

## 1. Core Principle

> Integrity proves what happened. Authority proves who may cause it. Policy proves whether it was allowed.

Merkle structures provide tamper-evident integrity evidence. Cryptographic keys and signatures establish attributable authority. The Constitutional Guardian evaluates applicable policy. A runtime may act on protected data only when it can verify the applicable authorization chain and any required unexpired authorization receipt.

A hash, CID, file, image, container, record, service, source tree, repository branch, successful test, or locally available secret does not become authoritative merely because it exists or can be referenced.

A Merkle root without a valid controlling signature, timestamp context, and governance interpretation is only an integrity commitment. It has no authority value on its own.

The implementation work completed through the trust-development sequence reinforces this separation. Runtime admission, caller authentication, signed operation-intent verification, policy evaluation, receipt issuance, runtime isolation, secret delivery, controlled email processing, and production activation are separate boundaries.

A successful test, existing artifact, valid cryptographic commitment, running container, verified pilot configuration, or healthy endpoint does not independently authorize deployment, protected-data access, contribution to the Commons, or live email delivery.

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
- Treat a dry-run audit event as proof of email delivery.
- Treat a working Resend credential as approval to send email.
- Treat a one-shot stdin-driven worker as a persistent, multi-user job-processing system.
- Treat a local Docker Compose configuration as a complete institutional-production deployment platform.
- Treat local file-backed secrets, even when mounted with effective least-privilege permissions, as the final production secret-management architecture.
- Treat an email-delivery pilot as evidence that institutional SSO, tenant isolation, role-based authorization, privacy governance, support workflows, or operational readiness have been completed.

The architecture intentionally preserves the distinction between:

1. Evidence of correctness.
2. Authority to act.
3. Authorization to perform a particular operation.
4. Runtime isolation.
5. Controlled pilot operation.
6. Production activation.

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
                                Egress Gateway / Resend

In the verified default mode, the dry-run gate terminates processing before the worker reads its shared authentication token or forwards an HTTP request. Therefore, neither the auth proxy nor egress gateway is required for a one-shot dry-run worker invocation.

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
- The authority required to approve a runtime, policy, transformation, Commons governance action, or transition from controlled email dry run to live email delivery.
- The institutional roles and governance approvals required before any multi-user support workflow is represented as production-authorized.

A Merkle root is evidence. Governance keys, role assignments, policies, and verified signatures are the authority layer.

The Policy Decision Engine evaluates requests against the active policy set. It does not replace human governance. It applies the policies and delegations established by governance.

The current trust-development model distinguishes operational approval, Guardian authority, release authority, email-delivery authorization, and governance-board authority. These roles are not interchangeable.

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
- Define whether a component is a one-shot job, a controlled pilot service, or an approved persistent production workload.
- Define the approved transition conditions between dry-run and live behavior.

`latest` tags, filenames, backup status, container existence, source-tree location, local image presence, Compose-project status, and successful local builds are not authority assertions.

A file existing in a repository is historical evidence unless an approved build and signed Runtime Authority Manifest declare it part of the current runtime.

### Current runtime-isolation pilot

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

    PILOT_RUNTIME_FINAL_VERIFICATION_PASS

This marker proves the pilot runtime controls were active at verification time. It does not establish production runtime authority, production release approval, protected-memory authorization, institutional multi-user authorization, or a production secret-management architecture.

### Controlled email runtime boundary

The controlled email-delivery pilot is a separate, bounded runtime path:

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
    api.resend.com

The verified Compose topology contains three services:

| Service | Purpose | Runtime identity | Secret access | Networks |
|---|---|---:|---|---|
| `email-worker` | One-shot request validation, permitted-template rendering, redacted audit emission, and controlled forwarding only when dry run is disabled | `10001:10001` | Worker authentication token only | `email_worker_auth` |
| `email-egress-auth` | Validates the worker’s authentication header using constant-time comparison and forwards only authorized requests | `10002:10002` | Worker authentication token only | `email_worker_auth`, `email_auth_egress` |
| `email-egress` | Receives authorized email payloads and, only on an authorized live path, performs the outbound Resend request | `10003:10003` | Resend API key only | `email_auth_egress`, `email_egress_outbound` |

The worker is intentionally excluded from the egress gateway network. It cannot directly reach the egress service or the designated external email endpoint through the approved topology.

The auth proxy is the only component that receives both:

- The worker-originated request on the worker/auth internal network.
- The worker shared-secret material required to validate `X-MsJarvis-Worker-Auth`.

The egress gateway is the only component that receives:

- Requests from the auth proxy on the auth/egress internal network.
- The Resend API key.
- The designated outbound network path.

The worker does not receive the Resend key. The auth proxy does not receive the Resend key. The egress gateway does not receive the worker-auth token.

This separation is a trust-boundary control. It is not by itself a complete institutional authorization model.

### Verified email image identities

The currently referenced verified images are:

| Component | Image reference | Verified role |
|---|---|---|
| Email worker | `msjarvis-email-worker:worker-template-fix-20260814T025643Z` | One-shot dry-run or controlled forwarding client |
| Auth proxy | `msjarvis-email-egress-auth:distroless-20260814T023959Z` | Internal request authentication boundary |
| Egress gateway | `msjarvis-email-egress-gateway:distroless-20260814T023959Z` | Restricted outbound email gateway |

The auth and egress proxies are built from the pinned distroless Python 3.13 runtime:

    gcr.io/distroless/python3-debian13@sha256:1c680cdb442a9e7a89f64fd1706367c62302ea1f9ab80fdebdb72ae9fcded46f

Their verified image configuration is:

| Service | User | Working directory | Entrypoint |
|---|---|---|---|
| `email-egress-auth` | `10002:10002` | `/app` | `/usr/bin/python3.13 /app/auth_proxy.py` |
| `email-egress` | `10003:10003` | `/app` | `/usr/bin/python3.13 /app/egress_proxy.py` |

The worker image is based on its current Python 3.11 build definition and includes:

- `email_worker.py`.
- `email_templates.py`.
- Declared worker dependencies.
- Non-root execution as `10001:10001`.
- `MSJARVIS_EMAIL_DRY_RUN=true` as the image-level default and Compose-level operating setting.

The worker packaging correction was verified offline: both `email_templates` and `email_worker` imported successfully with no network and no mounted secrets.

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

The auth and egress proxies were verified to initialize successfully under:

- A read-only root filesystem.
- All Linux capabilities dropped.
- `no-new-privileges`.
- No network access during offline module-import verification.
- Synthetic format-valid credentials written only to ephemeral tmpfs during that offline verification.

Controlled runtime verification with the existing Docker secret mounts subsequently confirmed:

- `email-egress-auth` returned HTTP 200 with `{"status":"ok"}` from `GET /healthz`.
- `email-egress` returned HTTP 200 with `{"status":"ok"}` from `GET /healthz`.
- The auth token appeared as a regular file at `/run/secrets/worker-auth-token`, with effective UID:GID `10002:10002` and mode `0400`.
- The Resend key appeared as a regular file at `/run/secrets/resend-api-key`, with effective UID:GID `10003:10003` and mode `0400`.
- Secret values were not printed or preserved in verification output.

These checks verify a bounded runtime configuration. They do not authorize live email delivery.

### Email egress policy

The auth proxy accepts:

- `GET /healthz` for local runtime health verification.
- An authorized email-forwarding request only on its defined request path and only when the supplied worker authentication header matches the mounted worker token using `hmac.compare_digest`.

The auth proxy rejects a missing or invalid worker token rather than forwarding the request.

The egress gateway accepts:

- `GET /healthz` for local runtime health verification.
- Its defined proxied email request path from the auth proxy.

The egress gateway performs the actual outbound Resend request only if it receives a valid request through its normal forwarding path. The health endpoint does not invoke Resend.

Health success confirms that a service is running and has initialized its required secret material. It does not confirm a live delivery transaction, sender-domain authorization, recipient policy compliance, or operational authorization to email any person.

### One-shot worker operating model

The worker is intentionally not a daemon, queue consumer, or persistent service. Its execution model is:

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
             |
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

The worker’s `main()` function reads one JSON object using standard input, processes it once, and exits. It is therefore not correctly deployed as a detached persistent container with no supplied request payload.

The correct controlled invocation pattern is:

```bash
docker compose \
  --profile email-worker-disabled \
  -f "$HOME/msjarvis-resend-email-pilot-20260814T000519Z/docker-compose.email-worker.design.yml" \
  run --rm --no-deps --no-TTY -T email-worker < approved-request.json
```

The profile name is retained for deliberate activation control. It does not by itself establish production approval.

In the verified configuration, `MSJARVIS_EMAIL_DRY_RUN=true`. The worker therefore audits the allowed request and exits before it loads the worker token or sends a request to the auth proxy.

### Controlled email verification record

The verified controlled email evidence includes:

| Verification activity | Result |
|---|---|
| Distroless auth and egress image build | Passed |
| Auth and egress offline import with synthetic tmpfs credentials | Passed |
| Proxy health checks with real mounted Docker secrets | Passed |
| Effective in-container secret metadata check | Passed; intended non-root UID ownership and mode `0400` observed |
| Worker image offline import | Passed after inclusion of `email_templates.py` |
| Full-stack dry-run request | Passed |
| Worker request audit event | Emitted |
| Worker dry-run audit event | Emitted |
| Worker forwarding indicator during dry run | Not observed |
| Intentional Resend contact during dry run | Not performed |
| Intentional email POST during dry run | Not performed |

The full-stack dry-run used the only currently permitted template, `email_delivery_test`, with a synthetic `.invalid` recipient. Audit output recorded digest values rather than raw recipient, subject, body, or idempotency material.

### Secret-delivery boundary

The current local Compose secret mounts are an evidence-backed pilot mechanism for the controlled email services. They are not the final production secret-management architecture.

The Compose implementation may issue a warning that file-secret `uid`, `gid`, and `mode` declarations are not supported in the active local Compose mode. The effective in-container secret metadata was separately verified for the proxy services and showed the intended ownership and permissions at the time of the controlled test.

That observed result does not remove the production requirement for a governed external secret-management system.

Before production activation:

- Secret values must not be embedded in source, images, Compose YAML, shell history, rendered configuration captures, logs, or evidence.
- Each service must receive only the secret material it requires.
- Secret rotation, revocation, recovery, access review, and incident response must be governed and auditable.
- Production secret delivery must support the intended non-root runtime identities without broadening access.
- All pilot and pre-production credentials must be rotated during any approved production cutover.
- A secret-management outage must fail protected capabilities safely and must have a tested recovery procedure.
- The production system must not rely on undocumented host-file ownership behavior.

Local file-backed Compose secrets are not accepted as the target production mechanism for the complete MountainShares / Ms. Jarvis architecture or for an institutional multi-user email-support system.

Docker Swarm secrets are not a pilot-only migration path for the current host topology. The existing Jarvis environment uses a broad local bridge-network deployment, and moving one component into Swarm would be a coordinated infrastructure migration rather than a secrets-only change.

### Current provenance and admission state

Runtime-authority signature verification and fail-closed runtime admission are implemented in the trust-development boundary.

The existing Guardian runtime has been associated with an immutable image digest rather than an unrestricted mutable image tag.

The email auth and egress proxy runtimes are pinned to an immutable distroless base-image digest and referenced by release tags in the controlled Compose file. That evidence provides traceability and repeatability for the verified local build. It does not substitute for a signed production Runtime Authority Manifest, governed SBOM review, approved deployment authority, or institutional operations approval.

A candidate deployment topology for a provisioned Guardian exists but is intentionally not active as production authority. The current production-signing and governance conditions are not yet complete, and the system must fail closed rather than manufacture authority from a technically deployable configuration.

These results establish meaningful runtime-authority, runtime-admission, runtime-isolation, and controlled-email-pilot evidence.

They do not establish final production deployment authority.

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
- Define whether a component is a one-shot job, a controlled pilot service, or an approved persistent production workload.
- Define the approved transition conditions between dry-run and live behavior.

`latest` tags, filenames, backup status, container existence, source-tree location, local image presence, Compose-project status, and successful local builds are not authority assertions.

A file existing in a repository is historical evidence unless an approved build and signed Runtime Authority Manifest declare it part of the current runtime.

### Current runtime-isolation pilot

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

    PILOT_RUNTIME_FINAL_VERIFICATION_PASS

This marker proves the pilot runtime controls were active at verification time. It does not establish production runtime authority, production release approval, protected-memory authorization, institutional multi-user authorization, or a production secret-management architecture.

### Controlled email runtime boundary

The controlled email-delivery pilot is a separate, bounded runtime path:

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
    api.resend.com

The verified Compose topology contains three services:

| Service | Purpose | Runtime identity | Secret access | Networks |
|---|---|---:|---|---|
| `email-worker` | One-shot request validation, permitted-template rendering, redacted audit emission, and controlled forwarding only when dry run is disabled | `10001:10001` | Worker authentication token only | `email_worker_auth` |
| `email-egress-auth` | Validates the worker’s authentication header using constant-time comparison and forwards only authorized requests | `10002:10002` | Worker authentication token only | `email_worker_auth`, `email_auth_egress` |
| `email-egress` | Receives authorized email payloads and, only on an authorized live path, performs the outbound Resend request | `10003:10003` | Resend API key only | `email_auth_egress`, `email_egress_outbound` |

The worker is intentionally excluded from the egress gateway network. It cannot directly reach the egress service or the designated external email endpoint through the approved topology.

The auth proxy is the only component that receives both:

- The worker-originated request on the worker/auth internal network.
- The worker shared-secret material required to validate `X-MsJarvis-Worker-Auth`.

The egress gateway is the only component that receives:

- Requests from the auth proxy on the auth/egress internal network.
- The Resend API key.
- The designated outbound network path.

The worker does not receive the Resend key. The auth proxy does not receive the Resend key. The egress gateway does not receive the worker-auth token.

This separation is a trust-boundary control. It is not by itself a complete institutional authorization model.

### Verified email image identities

The currently referenced verified images are:

| Component | Image reference | Verified role |
|---|---|---|
| Email worker | `msjarvis-email-worker:worker-template-fix-20260814T025643Z` | One-shot dry-run or controlled forwarding client |
| Auth proxy | `msjarvis-email-egress-auth:distroless-20260814T023959Z` | Internal request authentication boundary |
| Egress gateway | `msjarvis-email-egress-gateway:distroless-20260814T023959Z` | Restricted outbound email gateway |

The auth and egress proxies are built from the pinned distroless Python 3.13 runtime:

    gcr.io/distroless/python3-debian13@sha256:1c680cdb442a9e7a89f64fd1706367c62302ea1f9ab80fdebdb72ae9fcded46f

Their verified image configuration is:

| Service | User | Working directory | Entrypoint |
|---|---|---|---|
| `email-egress-auth` | `10002:10002` | `/app` | `/usr/bin/python3.13 /app/auth_proxy.py` |
| `email-egress` | `10003:10003` | `/app` | `/usr/bin/python3.13 /app/egress_proxy.py` |

The worker image is based on its current Python 3.11 build definition and includes:

- `email_worker.py`.
- `email_templates.py`.
- Declared worker dependencies.
- Non-root execution as `10001:10001`.
- `MSJARVIS_EMAIL_DRY_RUN=true` as the image-level default and Compose-level operating setting.

The worker packaging correction was verified offline: both `email_templates` and `email_worker` imported successfully with no network and no mounted secrets.

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

The auth and egress proxies were verified to initialize successfully under:

- A read-only root filesystem.
- All Linux capabilities dropped.
- `no-new-privileges`.
- No network access during offline module-import verification.
- Synthetic format-valid credentials written only to ephemeral tmpfs during that offline verification.

Controlled runtime verification with the existing Docker secret mounts subsequently confirmed:

- `email-egress-auth` returned HTTP 200 with `{"status":"ok"}` from `GET /healthz`.
- `email-egress` returned HTTP 200 with `{"status":"ok"}` from `GET /healthz`.
- The auth token appeared as a regular file at `/run/secrets/worker-auth-token`, with effective UID:GID `10002:10002` and mode `0400`.
- The Resend key appeared as a regular file at `/run/secrets/resend-api-key`, with effective UID:GID `10003:10003` and mode `0400`.
- Secret values were not printed or preserved in verification output.

These checks verify a bounded runtime configuration. They do not authorize live email delivery.

### Email egress policy

The auth proxy accepts:

- `GET /healthz` for local runtime health verification.
- An authorized email-forwarding request only on its defined request path and only when the supplied worker authentication header matches the mounted worker token using `hmac.compare_digest`.

The auth proxy rejects a missing or invalid worker token rather than forwarding the request.

The egress gateway accepts:

- `GET /healthz` for local runtime health verification.
- Its defined proxied email request path from the auth proxy.

The egress gateway performs the actual outbound Resend request only if it receives a valid request through its normal forwarding path. The health endpoint does not invoke Resend.

Health success confirms that a service is running and has initialized its required secret material. It does not confirm a live delivery transaction, sender-domain authorization, recipient policy compliance, or operational authorization to email any person.

### One-shot worker operating model

The worker is intentionally not a daemon, queue consumer, or persistent service. Its execution model is:

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
             |
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

The worker’s `main()` function reads one JSON object using standard input, processes it once, and exits. It is therefore not correctly deployed as a detached persistent container with no supplied request payload.

The correct controlled invocation pattern is:

```bash
docker compose \
  --profile email-worker-disabled \
  -f "$HOME/msjarvis-resend-email-pilot-20260814T000519Z/docker-compose.email-worker.design.yml" \
  run --rm --no-deps --no-TTY -T email-worker < approved-request.json
```

The profile name is retained for deliberate activation control. It does not by itself establish production approval.

In the verified configuration, `MSJARVIS_EMAIL_DRY_RUN=true`. The worker therefore audits the allowed request and exits before it loads the worker token or sends a request to the auth proxy.

### Controlled email verification record

The verified controlled email evidence includes:

| Verification activity | Result |
|---|---|
| Distroless auth and egress image build | Passed |
| Auth and egress offline import with synthetic tmpfs credentials | Passed |
| Proxy health checks with real mounted Docker secrets | Passed |
| Effective in-container secret metadata check | Passed; intended non-root UID ownership and mode `0400` observed |
| Worker image offline import | Passed after inclusion of `email_templates.py` |
| Full-stack dry-run request | Passed |
| Worker request audit event | Emitted |
| Worker dry-run audit event | Emitted |
| Worker forwarding indicator during dry run | Not observed |
| Intentional Resend contact during dry run | Not performed |
| Intentional email POST during dry run | Not performed |

The full-stack dry-run used the only currently permitted template, `email_delivery_test`, with a synthetic `.invalid` recipient. Audit output recorded digest values rather than raw recipient, subject, body, or idempotency material.

### Secret-delivery boundary

The current local Compose secret mounts are an evidence-backed pilot mechanism for the controlled email services. They are not the final production secret-management architecture.

The Compose implementation may issue a warning that file-secret `uid`, `gid`, and `mode` declarations are not supported in the active local Compose mode. The effective in-container secret metadata was separately verified for the proxy services and showed the intended ownership and permissions at the time of the controlled test.

That observed result does not remove the production requirement for a governed external secret-management system.

Before production activation:

- Secret values must not be embedded in source, images, Compose YAML, shell history, rendered configuration captures, logs, or evidence.
- Each service must receive only the secret material it requires.
- Secret rotation, revocation, recovery, access review, and incident response must be governed and auditable.
- Production secret delivery must support the intended non-root runtime identities without broadening access.
- All pilot and pre-production credentials must be rotated during any approved production cutover.
- A secret-management outage must fail protected capabilities safely and must have a tested recovery procedure.
- The production system must not rely on undocumented host-file ownership behavior.

Local file-backed Compose secrets are not accepted as the target production mechanism for the complete MountainShares / Ms. Jarvis architecture or for an institutional multi-user email-support system.

Docker Swarm secrets are not a pilot-only migration path for the current host topology. The existing Jarvis environment uses a broad local bridge-network deployment, and moving one component into Swarm would be a coordinated infrastructure migration rather than a secrets-only change.

### Current provenance and admission state

Runtime-authority signature verification and fail-closed runtime admission are implemented in the trust-development boundary.

The existing Guardian runtime has been associated with an immutable image digest rather than an unrestricted mutable image tag.

The email auth and egress proxy runtimes are pinned to an immutable distroless base-image digest and referenced by release tags in the controlled Compose file. That evidence provides traceability and repeatability for the verified local build. It does not substitute for a signed production Runtime Authority Manifest, governed SBOM review, approved deployment authority, or institutional operations approval.

A candidate deployment topology for a provisioned Guardian exists but is intentionally not active as production authority. The current production-signing and governance conditions are not yet complete, and the system must fail closed rather than manufacture authority from a technically deployable configuration.

These results establish meaningful runtime-authority, runtime-admission, runtime-isolation, and controlled-email-pilot evidence.

They do not establish final production deployment authority.

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

The controlled email-delivery pilot does not alter user-sovereignty requirements. A request to render, audit, or eventually deliver an email must be separately authorized under the applicable institutional, user, and policy controls. The current dry-run worker accepts only an explicit limited test template and does not establish a general-purpose user messaging authority.

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

### Controlled email operational boundary

The controlled email component has a narrower and separate operational boundary:

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

The complete private-memory projection chain is not yet production-complete.

The controlled email component is also not a complete production workflow. It currently lacks institutional caller authentication, durable job handling, tenant-aware authorization, and an approved transition to live delivery.

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

The controlled email dry-run does not issue or consume a PDR because it does not access protected-memory material, invoke a protected capability, or initiate a live delivery request. A future live email workflow that uses protected data or constitutes a governed institutional action must not treat a generic dry-run result as a replacement for the applicable PDR and authorization chain.

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

The controlled email pilot does not create a Projection Receipt because its verified dry-run request uses a fixed permitted test template with no private-memory projection. This is a deliberate limitation. It must not be generalized into a claim that email rendering is approved to consume unrestricted reasoning context, user records, or institutional data.

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

The current controlled email worker does not claim to be a Guardian-authorized institutional support workflow. It is a fixed-scope, manually invoked dry-run component. Any expansion to user-initiated, administrator-initiated, support-initiated, or automated live messaging must first define the relevant policy classification and enforce the applicable Guardian, identity, authorization, tenant, and approval controls.

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

The controlled email pilot is not a Commons-contribution path. Its redacted local audit events are operational evidence for a bounded test workflow and must not be repurposed as Commons data, user-profile data, institutional analytics, or contribution evidence without a separate authorized transformation and applicable governance approval.

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
- Resend API key.
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
- Redis connection URLs containing credentials.
- Rendered Nginx configuration containing active shared secrets.
- Raw authorization headers.
- Session tokens.
- Plaintext protected user content.
- Raw worker-auth tokens.
- Raw Resend API keys.
- Secret-bearing Compose-rendered content.
- Raw recipient information, message bodies, or unredacted institutional support records unless such retention is separately approved and governed.

A capability may be described as:

- Defined.
- Implemented.
- Verified.
- Sealed.
- Promoted.
- Production-authorized.

These are distinct states.

### Controlled email evidence record

The current email pilot generated the following evidence directories beneath the local pilot evidence root:

| Evidence activity | Evidence directory |
|---|---|
| Distroless auth and egress build | `evidence/distroless-20260814T023959Z` |
| Offline proxy import with synthetic credentials | `evidence/distroless-runtime-verify-final-20260814T024513Z` |
| Controlled proxy health check with real secret mounts | `evidence/distroless-controlled-health-20260814T024757Z` |
| Persistent proxy Compose image-reference update | `evidence/distroless-compose-persist-20260814T024905Z` |
| Proxy readiness and effective secret-metadata verification | `evidence/distroless-proxy-pair-readiness-20260814T025145Z` |
| Worker packaging correction, rebuild, and offline import | `evidence/worker-template-fix-20260814T025643Z` |
| Corrected full-stack one-shot dry-run verification | `evidence/distroless-full-stack-dry-run-fixed-20260814T025847Z` |

These directories are local implementation evidence. They are not independently signed production authority artifacts unless and until they are incorporated into an approved, governed evidence and release process.

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
| Controlled email topology | Verified for one-shot worker, auth-proxy, and egress-gateway separation. The worker does not receive the Resend key; the auth proxy does not receive the Resend key; the egress gateway does not receive the worker token. |
| Email auth proxy | Verified as a pinned distroless Python 3.13 image running as UID:GID `10002:10002`, with an explicit Python entrypoint, read-only root filesystem, dropped capabilities, no-new-privileges, and restricted secret access. |
| Email egress gateway | Verified as a pinned distroless Python 3.13 image running as UID:GID `10003:10003`, with an explicit Python entrypoint, read-only root filesystem, dropped capabilities, no-new-privileges, and restricted Resend-key access. |
| Email secret mount metadata | Verified during controlled runtime checks: auth token effective ownership `10002:10002`, egress key effective ownership `10003:10003`, both mode `0400`; values were not read or logged. |
| Email worker image | Verified after packaging correction. `email_worker.py` and `email_templates.py` import successfully under the worker image’s dry-run configuration. |
| Email worker dry-run | Verified. A permitted one-shot request generated `email_dispatch_requested` and `email_dispatch_dry_run` audit events and exited without a forwarding event. |
| Email worker persistence | Not implemented by design. The worker is stdin-driven and exits after one request; it is not a queue consumer, daemon, or persistent service. |
| Live email delivery | Not enabled or production-authorized. The verified default is `MSJARVIS_EMAIL_DRY_RUN=true`. |
| Institutional multi-user support workflow | Not implemented or production-authorized. Institutional identity, tenant isolation, roles, durable work orchestration, operational support controls, and live-send governance remain pending. |
| External secret manager | Not yet implemented. Required before production activation. |
| Docker Swarm migration | Not approved as a pilot-only secret migration because the current local bridge-network topology would require coordinated broader infrastructure migration. |
| MAR | Defined and supported by receipt infrastructure; complete protected-memory production path remains pending. |
| Projection Receipt | Defined; complete production projection boundary remains pending. |
| Projection Service | Not production-activated. |
| Reasoning isolation | Existing semantic-memory and reasoning capabilities must remain behind the authorization and projection boundary. |
| Commons receipts and governance | Defined; production implementation remains pending. |
| Revocation | Verified at the Guardian decision boundary; projection-path integration remains pending. |
| Adversarial matrix | Partially closed. Decision-boundary cases are verified; expiration, policy mismatch, unapproved-image, outage, secret-manager failure, full projection-chain, and multi-user email-policy cases remain. |
| Custodian ceremony | Started but incomplete. It grants no authority until the required independent custodians, remaining enrollment records, and threshold-signed governance registry are complete. |
| Release-candidate evidence | Completed as a tested, evidence-backed, fail-closed package. It is not an active authority system. |
| Live authority system | Not active. Production activation remains blocked pending governance, signer, secret-management, projection, release, institutional operating, and final authorization prerequisites. |

An implemented component is not automatically production-authorized.

A verified pilot is not automatically a production release.

A sealed evidence artifact is not automatically an active authority system.

A healthy service is not automatically an authorized service.

A successful dry-run is not an approved live action.

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
| Secret delivery | Approved external manager, least privilege, non-root compatibility, auditable rotation and recovery | Pilot secret isolation verified; production mechanism not complete |
| Runtime isolation | Read-only roots, least privilege, scoped writable paths, tested egress enforcement, authenticated dependencies | Verified for the privacy-gateway pilot baseline and controlled email proxy pair |
| Email dry-run | Approved fixed template, schema validation, dry-run policy enabled, redacted audit evidence, no forwarding event | Verified for one-shot controlled invocation |
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

## 16. Pilot Implementation and Production Closure Order

### 16.1 Purpose and status

This section records the current implementation boundary and the remaining closure work required before any component may be represented as production-authorized.

The system has progressed beyond an architecture-only design. It now includes meaningful, evidence-backed implementation and verification of trust-boundary controls, receipt infrastructure, Guardian decision-boundary controls, a hardened privacy-gateway runtime pilot, and a controlled email-processing pilot.

Those accomplishments are real and operationally valuable. They do not activate production authority, authorize protected-memory access, establish governance approval, permit a live authority system, authorize live email delivery, or establish an institutional multi-user support platform.

The present status is:

    RELEASE STATE: tested, evidence-backed, fail-closed release candidate
    AUTHORITY STATUS: inactive
    DEPLOYMENT ADMISSION: blocked pending production governance, signing,
    runtime-authority, protected-memory, projection, secret-management,
    institutional operating, and activation conditions

    CONTROLLED EMAIL STATE: verified one-shot dry-run pilot
    LIVE EMAIL STATE: disabled and not production-authorized
    EMAIL WORKER MODE: stdin-driven single-request process; not persistent

The verified privacy-gateway pilot is a runtime-isolation baseline. The verified email pilot is a bounded dry-run processing baseline. Neither is the completion of the MountainShares / Ms. Jarvis production trust architecture.

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
19. Email proxy images have been rebuilt as pinned distroless Python 3.13 runtimes with numeric non-root identities, explicit entrypoints, read-only roots, dropped capabilities, no-new-privileges, and scoped writable temporary storage.
20. The worker authentication secret and Resend API key have been separated so that each is mounted only into its respective service boundary.
21. Offline auth and egress initialization was verified with synthetic credentials created only in ephemeral tmpfs and no network access.
22. Controlled health verification confirmed that both proxies initialize with their existing Docker secret mounts and return HTTP 200 for `GET /healthz`.
23. Controlled metadata verification observed effective service-specific secret ownership and mode `0400` without reading secret contents.
24. The worker image packaging defect was corrected by including `email_templates.py` with `email_worker.py`.
25. The corrected worker imported successfully offline with `MSJARVIS_EMAIL_DRY_RUN=true`, no network, and no mounted secrets.
26. A full-stack one-shot dry-run produced the expected request and dry-run audit events without forwarding to the auth proxy, intentionally contacting Resend, or sending email.
27. Controlled Compose image references now retain the verified release-tagged worker, auth, and egress images.

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

#### Guardian signer and PDR activation

8. Establish dedicated Guardian PDR signing authority in approved secure custody.
9. Enroll its public key, with the required `guardian` role, in the production trusted signer registry.
10. Produce a production Guardian Authority Bundle carrying genuine production approvals and valid expiry.
11. Demonstrate a live, cryptographically valid PDR issuance path against production authority.
12. Demonstrate durable production receipt consumption and replay denial.
13. Ensure Guardian outage and signer failure deny protected capabilities rather than creating fallback authorization.
14. Determine and enforce which institutional support and live email actions require a PDR, MAR, additional approval receipt, or all of these controls.

#### Runtime authority and secrets

15. Build and verify one reproducible pilot release from a fully governed signed Runtime Authority Manifest.
16. Pin exact production image digests, SBOMs, dependencies, policies, health contracts, rollback targets, and release approvals.
17. Implement approved external secret management compatible with the non-root runtime.
18. Replace temporary local environment-file and local file-backed Compose secret delivery.
19. Rotate all pre-production credentials during the governed production cutover.
20. Verify that no secret values appear in source, Compose configuration, rendered configuration output, evidence, logs, shell history, or repository history.
21. Define and test secret-manager outage, recovery, rotation, revocation, and break-glass behavior.
22. Establish vulnerability management, SBOM review, image scanning, patch cadence, and release-dependency review processes.

#### Institutional multi-user support readiness

23. Implement institutional single sign-on using the approved identity provider and required multifactor-authentication policy.
24. Define and enforce server-side roles and permissions, including least-privilege support, administrator, auditor, and governance roles as applicable.
25. Define a tenant or organizational-boundary model and ensure every protected query, request, receipt, audit event, and workflow is scoped and enforced server-side.
26. Implement user lifecycle controls: account provisioning, deprovisioning, suspension, access review, role change, and session revocation.
27. Define data classification, consent, retention, deletion, disclosure, and support-record handling requirements.
28. Complete institutional privacy, security, accessibility, procurement, legal, and records-management review as applicable to the intended deployment.
29. Establish support ownership, incident escalation, on-call responsibility, operational runbooks, and service-level objectives.
30. Establish centralized redacted logging, monitoring, metrics, tracing, alerting, retention, and audit access controls.

#### Persistent email processing and live-send controls

31. Do not deploy the current stdin-driven worker as a persistent service. It is a one-shot process by design.
32. If persistent processing is required, design and implement a durable input mechanism, such as an authenticated API plus durable queue, with clear command ownership and authorization.
33. Implement durable idempotency storage rather than relying solely on caller-provided request values.
34. Implement retry, backoff, timeout, failure classification, dead-letter, replay-review, and recovery procedures.
35. Implement concurrency limits, quota enforcement, rate limits, recipient-domain policy, template allowlists, sender-domain controls, and abuse prevention.
36. Implement a live-send control plane with environment isolation, explicit change approval, runtime policy check, audit trail, and immediate kill switch.
37. Verify that `MSJARVIS_EMAIL_DRY_RUN=true` remains the default and that disabling it requires an approved, recorded, policy-governed activation process.
38. Conduct controlled live-send testing only after all required governance, operational, and provider-side sender-domain prerequisites are complete, using an approved test recipient and an explicit, auditable authorization.
39. Verify external-provider failure handling, delivery-status processing, bounce/complaint handling, revocation behavior, and recipient suppression controls before live institutional use.

#### Protected memory and projection

40. Establish signed runtime-admission chains for the Projection Service and reasoning recipient.
41. Implement and verify MAR issuance and validation in the protected-memory path.
42. Implement Projection Service verification before protected retrieval.
43. Remove unrestricted private-memory access from reasoning paths.
44. Implement and verify Projection Receipts and their output commitments.
45. Bind recipient runtime identity, projection scope, purpose, policy, expiry, and use count before reasoning-context release.
46. Integrate revocation into protected-memory and projection authorization checks before every new projection.
47. Ensure that any email generated from protected-memory or institutional data receives only an authorized minimum context projection and remains within the relevant scope, purpose, recipient, and retention constraints.

#### Commons and full-chain verification

48. Implement Contribution and Transformation Receipts before publishing Commons aggregates.
49. Establish Commons Epoch Root governance and required privacy attestations.
50. Close the remaining adversarial verification cells:
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
51. Demonstrate durable shared-ledger conformance before any multi-replica deployment requiring shared receipt consumption.
52. Exercise backup recovery, rollback, incident response, observability, and evidence-retention procedures.

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

    A tested, evidence-backed, fail-closed release candidate with a verified
    runtime-isolation pilot baseline and a verified controlled one-shot
    email dry-run capability; not a production-authorized live authority,
    multi-user institutional-support, or live email-delivery system.

### 16.5 Immediate practical next project

The immediate next project is:

1. Production governance and signer enrollment.
2. Approved external secret-manager implementation.
3. Governed Runtime Authority Manifest and reproducible release closure.
4. Protected-memory MAR and Projection Service activation.
5. Institutional identity, authorization, and tenant-boundary design.
6. Durable, policy-governed email work orchestration if persistent processing is required.
7. End-to-end production-chain adversarial verification.

The immediate next project is not another emergency Docker hardening change. The privacy-gateway and controlled-email pilots have established hardened runtime baselines.

Production progress now depends on legitimate authority, signer custody, governed secret delivery, immutable release authority, protected-memory authorization and projection closure, institutional operating controls, and a deliberately designed live-delivery control plane.

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
- Raw email recipients, message bodies, worker tokens, provider keys, or institution-specific support content unless explicitly approved under a separate governed retention process.

The current pilot verification evidence demonstrates runtime isolation, service health, credential rotation, egress enforcement, Redis authentication, controlled email secret placement, proxy readiness, worker dry-run behavior, and fail-closed boundary controls without granting production authority.

The custodian ceremony has begun but is incomplete. Partial enrollment grants no authority.

A candidate Guardian deployment topology may be technically deployable but remains unauthorized until the required governance, signer, authority-bundle, runtime-manifest, secret-management, institutional identity, operational, and protected-memory conditions are complete.

The controlled email topology may be technically runnable but remains restricted to verified one-shot dry-run behavior. It must not be represented as an authorized live email system or persistent support service until the relevant production controls are complete.

The architecture is designed to stop before live authority is granted when required governance, signing, registry, runtime, secret-delivery, identity, authorization, tenant, operational, delivery-policy, or projection conditions are absent.

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

The required governance authority, signing authority, runtime admission, policy, secret-management, release, institutional operating, and activation conditions exist and have been explicitly authorized.

These states must not be conflated.

> Implemented does not mean production-authorized.  
> Verified does not mean production-authorized.  
> Sealed evidence does not mean production-authorized.  
> Promoted does not mean production-authorized.  
> A hardened pilot does not mean production-authorized.  
> A release candidate does not mean an active authority system.  
> A successful dry-run does not mean live delivery is authorized.  
> A running container does not mean a persistent service design is complete.  
> A valid provider key does not mean an institution has approved the action it could enable.

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
- A controlled three-service email topology that separates worker authentication from external provider credentials.
- Distroless, pinned, numeric-non-root auth and egress proxy runtimes.
- Controlled secret-mount metadata verification without secret disclosure.
- Corrected worker packaging and offline import verification.
- A verified one-shot dry-run email workflow that renders only the approved test template, emits redacted audit events, and exits without forwarding or sending.

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
- Institutional authentication, multifactor controls, and account lifecycle management.
- Tenant isolation and server-side role-based or attribute-based authorization.
- Institutional privacy, retention, accessibility, security, and operational review.
- Durable multi-user work processing.
- Idempotency, retry, dead-letter, and recovery controls for persistent delivery work.
- Live email delivery governance, sender policy, recipient safeguards, rate controls, suppression handling, and emergency stop capability.
- Centralized observability, incident response, backup recovery, and operating ownership.
- Remaining adversarial verification cells.
- Durable shared-ledger verification at production scale.
- Final reproducible release authorization.
- Completion of human custodian and governance activation.

The result is not an architecture claiming completion prematurely.

It is an architecture in which remaining work is expressed as explicit authority, implementation, operational, institutional, and verification gates rather than unspecified future work.

The governing principle remains unchanged:

> Integrity proves what happened. Authority proves who may cause it. Policy proves whether it was allowed.

The documentation records both sides of the current state:

> What has actually been built, tested, verified, sealed, and promoted; and what remains deliberately blocked because the required authority has not yet been established.
