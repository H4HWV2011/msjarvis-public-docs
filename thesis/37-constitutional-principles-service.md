# 37. Constitutional Principles Service

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: August 17, 2026*

---

## 37.1 What This Service Does

The constitutional principles service is a **governance gate** that checks whether a proposed action fits the project's constitutional commitments before it is allowed to gain authority.

Here, “constitutional” is concrete, not decorative. The service is rooted in:

- the **United States Constitution**;
- the **West Virginia Constitution**.

These are used as reference frameworks for rights, limits, due process, and bounded authority. The service sits in the promotion path to help decide whether a candidate action may move from **internal proposal** to **approved system behavior**.

The Constitutional Principles Service is also the protected Guardian authority surface for the narrow operation class `user-data-operationalization`. That protected path is distinct from ordinary BBB content filtering. It requires a complete authorization chain, creates a Policy Decision Receipt when authorization succeeds, and denies when any required authority condition is absent or invalid.

As of the July 26, 2026 architecture closeout, the Constitutional Principles Service is named in Chapter 52 as one of the **two built components of the Recurrent Epistemic Loop** — alongside the DGM validators. Its governance filtering is invoked on a daily scheduled cadence by `runtime_governance.gbim_runtime_lifecycle_daily()`, the pg_cron job (jobid 3) that fires every day at 03:05 in `wv_gis`. That connection is detailed in §37.10 and §37.11 below.

---

## 37.2 Live Service and Ports

As of the August 17, 2026 as-built validation:

- The **constitutional guardian** is live on host port **8091**.
- The **BBB** (blood-brain barrier) is live on host port **8016** and connected to the guardian over `qualia-net`.
- The Guardian health route is:

```text
GET /health
```

- The protected constitutional decision route is:

```text
POST /constitutional/check
```

The Guardian’s constitutional status, principles, audit, audit statistics, version, change, and transparency routes remain available as health, inspection, and governance surfaces where configured.

The protected decision route is intentionally different from a generic unauthenticated review endpoint. A request to `/constitutional/check` must satisfy caller authentication, authority-bundle verification, runtime admission, signed operation-intent verification, caller/subject binding, operation matching, and PDR issuance conditions before it can receive an allow.

This chapter does not rely on April 2026 container counts or database sizes; it reflects the as-built July and August 2026 state.

---

## 37.3 Constitutional Materials in the System

The constitutional principles service works alongside:

- internal corpora that store the **U.S.** and **West Virginia** constitutions;
- related governance texts and commentary;
- retrieval tools that can pull relevant passages for context;
- signed authority bundles, trusted public-key registries, governance policies, runtime-admission records, and revocation material used by the protected Guardian path.

The purpose is **not** to act as a court or replace lawyers. Instead, the service:

- brings constitutional ideas such as rights, restraints, and due process into the decision pipeline;
- helps flag actions that appear to violate those commitments;
- supports a place-rooted understanding of lawful power in West Virginia communities;
- enforces the distinction between ordinary safeguarded processing and a separately governed authority transition.

---

## 37.4 Ordinary BBB Filtering and Guardian Scope

The BBB and Guardian have related but distinct responsibilities.

### Ordinary BBB content filtering

Routine content is evaluated by local BBB safeguards, including:

- ethical filtering;
- spiritual or values-alignment filtering;
- safety monitoring;
- threat detection and community-protection checks.

Ordinary `content_filter` traffic does not claim that it has received a cryptographic Guardian authorization. For this request class, BBB records Guardian as not applicable:

```json
{
  "applicable": false,
  "allowed": null,
  "decision": "not_applicable"
}
```

This does not mean routine content is automatically safe or promoted. It means that Guardian/PDR authorization is not the applicable authority mechanism for that request. The content must still pass local BBB safeguards and any route-specific truth, provenance, coherence, privacy, security, judge, and promotion controls.

### Guardian-governed operation

The current Guardian authorization path applies to the explicit operation:

```text
user-data-operationalization
```

This operation is narrow and high assurance. It is not equivalent to routine content filtering, ordinary chat, standard Neurobiological Master processing, EEG telemetry, or every sandbox-to-bridge transition.

A request that explicitly declares `user-data-operationalization` enters the Guardian’s protected authority sequence.

---

## 37.5 The Guardian Payload Contract

Every request to the constitutional service must carry a structured payload. The underlying decision payload includes:

- `actor_role` — who is acting, such as a system module, operator, or automation;
- `context` — the relevant session, workflow, or scenario;
- `action_type` — the proposed operation;
- `content` — the substance being reviewed;
- `metadata` — provenance, identifiers, and other details needed for review.

For an ordinary local BBB content-filtering request, this payload is evaluated by the BBB’s local safeguards and route-specific controls.

For a Guardian-governed `user-data-operationalization` request, the payload is necessary but not sufficient. The request must also carry:

- `X-Caller-Token` — the protected credential of an active registered caller;
- `X-Operation-Intent` — a base64-encoded, subject-signed operation-intent record.

Simply calling the endpoint is not enough. The content payload, caller identity, authority bundle, runtime admission, subject authorization, operation binding, and PDR path must all be valid.

---

## 37.6 Protected Guardian Authorization Sequence

The Guardian enforces the following protected sequence for a `user-data-operationalization` request:

1. **Caller token**  
   The request must provide `X-Caller-Token`. If it is missing, the Guardian returns HTTP 401 with `CALLER_TOKEN_MISSING`.

2. **Verified authority bundle**  
   Guardian loads and verifies the configured authority bundle. The bundle must be structurally valid, active within its issuance and expiration window, valid for the configured environment, signed by trusted approvers, and consistent with the governance policy.

3. **Caller authentication**  
   Guardian computes a SHA-256 commitment of the presented caller token and compares it against registered caller commitments in the verified authority bundle. The matching caller must have active status and the `caller` role.

4. **Runtime admission**  
   Guardian verifies the configured runtime-admission record against the runtime-authority manifest, trusted keys, governance policies, and sealed admission verifier. Missing configuration, missing files, invalid records, or verifier failure deny the request.

5. **Signed operation intent**  
   The request must provide `X-Operation-Intent`. Guardian decodes and validates the signed operation-intent record against the active subject-key registry and the sealed signature verifier.

6. **Subject-key and signature verification**  
   The intent must be structurally valid, active within its lifetime, signed with an active trusted Ed25519 subject key, and bound to the subject/controller associated with that key.

7. **Caller/subject match**  
   The authenticated caller identity must equal the signed intent’s subject identity. A caller may not use an intent signed for another subject.

8. **Operation match**  
   The request `action_type` must match the signed intent’s `operation`. The currently supported PDR-governed operation is exactly `user-data-operationalization`.

9. **Revocation and scope checks**  
   Guardian denies revoked subjects and revoked intent identifiers. It also verifies the required operation, scope, and authority conditions before policy approval is possible.

10. **Policy Decision Receipt issuance and one-time consumption**  
    If the action passes constitutional and policy checks, Guardian consumes the verified operation intent in a durable ledger and issues a signed Policy Decision Receipt (PDR). The intent-consumption ledger prevents reuse of the same intent identifier and prevents reuse of the same subject/nonce pair.

This sequence preserves a distinction between:

- a request being syntactically well formed;
- a caller being authenticated;
- a runtime being admitted;
- a subject authorizing a particular operation;
- a policy decision being allowed;
- a durable receipt being issued.

A failure at any stage prevents an allow.

---

## 37.7 Signed Operation Intent and PDR Requirements

A signed operation intent binds a subject to one specific operation. The Guardian’s accepted intent contract includes:

- intent identifier;
- request identifier;
- subject identity;
- adapter identifier;
- operation;
- SHA-256 projection commitment;
- audience;
- purpose;
- issuance time;
- expiration time;
- nonce;
- Ed25519 subject signature and key identifier.

The intent is not a general credential. It is a bounded, per-operation authorization record. It is verified against active subject public keys in the authority bundle.

A successful governed operation must also produce a Policy Decision Receipt. The PDR path consumes the verified intent before the PDR is constructed. This provides replay protection:

- reusing an already consumed intent identifier is denied;
- reusing a subject and nonce pair is denied;
- an intent that has been consumed cannot authorize a second operation.

The private subject signing key remains outside BBB and Guardian. BBB forwards authorization headers when applicable; it does not create caller tokens, sign operation intents, generate subject keys, or hold Guardian signing material.

---

## 37.8 Current Authority State: Intentionally Unprovisioned

As of August 17, 2026, the Guardian authority bundle is structurally valid for the configured production governance policy but intentionally contains:

```json
{
  "active_callers": 0,
  "active_subject_keys": 0,
  "governed_operation_authorization": "unavailable_fail_closed"
}
```

This is an intentional administrative posture.

The production authority bundle has no active caller entries and no active subject-key entries. Therefore:

- no caller token can authenticate as an active Guardian caller;
- no subject can produce a valid accepted signed operation intent;
- no `user-data-operationalization` request can satisfy the protected authorization sequence;
- no governed operation can obtain a Policy Decision Receipt;
- all such operations remain unavailable and fail closed.

The current administrative decision is:

```text
Keep user-data-operationalization off.
```

This status does not disable ordinary BBB filtering, sandbox governance, Neurobiological Master processing, EEG rhythm telemetry, ordinary route-level promotion controls, or the broader daily governance cycle. It preserves the distinction between routine safeguarded work and the exceptional, cryptographically governed authority transition.

---

## 37.9 What the Guardian Checks

When a complete, authorized governed request reaches the decision stage, the Guardian evaluates questions such as:

- Is this authenticated caller authorized to request the operation?
- Does the active subject authorize this exact operation?
- Does the operation respect consent and privacy?
- Does the action avoid obvious conflicts with constitutional rights or protections?
- Is there any sign of bypassing required oversight or due process within the system’s own rules?
- Does the request match the signed intent’s subject, operation, audience, purpose, and scope?
- Is the intent current, unrevoked, and not previously consumed?
- Can Guardian issue a valid, durable Policy Decision Receipt?

Examples of expected behavior:

- A complete, valid, subject-authorized `user-data-operationalization` request could pass if all policy conditions and PDR issuance conditions succeed.
- A request with missing caller credentials is denied before policy evaluation.
- A request with invalid caller credentials reaches Guardian and is denied with HTTP 401.
- A request with a missing, malformed, expired, revoked, mismatched, or replayed intent is denied.
- A consent-bypass or private-disclosure request is expected to fail closed.
- A request that cannot issue a valid PDR is not allowed merely because its content appears acceptable.

At present, the valid affirmative path is intentionally unavailable because no active caller or subject identities are provisioned.

---

## 37.10 BBB and Guardian Together

The **BBB** and the **constitutional guardian** work together without claiming the same responsibility:

- BBB sits at a boundary between lower-risk internal reasoning and higher-authority consequences.
- BBB applies local ethical, spiritual, safety, and threat-detection safeguards to ordinary content.
- Guardian provides a separate high-assurance constitutional authorization path for explicitly declared `user-data-operationalization`.
- Guardian-governed failures are preserved as denial; they cannot become authorization through error handling.
- Both expose health surfaces so watchdogs and operators can confirm they are up and responding.

For rural operators, this means you can:

- check that BBB on port **8016** is healthy;
- check that Guardian on port **8091** is healthy;
- verify that ordinary content filtering remains active;
- verify that Guardian-governed operations remain blocked when required authority is absent;
- verify that consequential promotion calls pass through the gates appropriate to their route rather than bypassing them.

The August 17, 2026 BBB remediation corrected a prior integration defect in which Guardian HTTP 401 responses could be transformed into an allow by BBB exception handling. The corrected BBB now records ordinary filtering as `not_applicable` to Guardian and fails closed for every Guardian-governed failure mode.

---

## 37.11 Role in the Recurrent Epistemic Loop (Chapter 52)

The Constitutional Principles Service is one of the **two named built components of the Recurrent Epistemic Loop**, as confirmed in Chapter 52. The other named component is the DGM validators. Together, these two components form the loop’s governance filtering layer: DGM validators check whether proposed self-modifications are coherent and bounded; the Constitutional Principles Service checks whether proposed actions respect constitutional rights, consent, due process, and the applicable authority boundary.

The Recurrent Epistemic Loop is not a design idea — it is a running structure. Its two components are not passive services waiting to be called manually; they are invoked on a scheduled cadence by the database-layer heartbeat described in Chapter 28.

The scheduled surface that invokes governance filtering is `runtime_governance.gbim_runtime_lifecycle_daily()`, registered as pg_cron jobid 3 with schedule `5 3 * * *`. Every day at 03:05, this procedure advances the GBIM lifecycle and, as part of that advancement, triggers the governance filtering pass that includes constitutional review of records in the promotion pipeline. This is the mechanism by which the Constitutional Principles Service participates in the continuous, observable governance cycle rather than being invoked only on demand.

For rural developers, the implication is concrete: constitutional filtering is not something that happens once when a record is first ingested. It happens again at every daily governance pass. A record that was constitutionally acceptable when ingested can be re-evaluated during the daily cycle. If its context has changed — if consent was withdrawn, if a prohibited metadata field was added, or if the action type shifted — the daily pass provides the scheduled surface on which that re-evaluation occurs.

The daily governance pass does not itself activate the currently unprovisioned `user-data-operationalization` path. That path remains separately protected by the live Guardian authority sequence.

---

## 37.12 Role in the Broader Promotion Pipeline

The constitutional principles service is one part of a broader promotion gate. A typical path is:

1. **Sandbox reasoning** produces a candidate action or answer.
2. Other judges and checks evaluate truth, coherence, safety, provenance, and the ten-condition admissibility predicate in Appendix A.
3. The route determines which authority conditions apply to the requested transition.
4. BBB applies ordinary local safeguards where applicable.
5. For an explicitly Guardian-governed `user-data-operationalization` request, the caller token, authority bundle, runtime admission, signed operation intent, caller/subject match, operation match, revocation checks, PDR issuance, and one-time consumption must all succeed.
6. Only if the required route-specific gates approve can promotion proceed.
7. At the next daily governance pass, `runtime_governance.gbim_runtime_lifecycle_daily()` re-evaluates promoted records through the governance filtering layer as part of the Recurrent Epistemic Loop.

If the Guardian response is a failure, if authorization is absent, or if the payload or signed intent is malformed, the system:

- does **not** treat the action as approved;
- fails closed and logs the problem;
- records the failure state through the available audit surfaces so operators can inspect it.

Ordinary BBB filtering remains operational even while the separate Guardian-governed operation is intentionally unavailable.

---

## 37.13 Place-Aware Constitutional Orientation

Because Ms. Allis is rooted in **Mount Hope, West Virginia**, the constitutional service:

- names and respects both the **U.S. Constitution** and the **West Virginia Constitution**;
- treats local state-level rights and limits as part of its frame of reference;
- avoids pretending that governance is the same everywhere.

The daily governance pass through `runtime_governance.gbim_runtime_lifecycle_daily()` is itself place-aware: it operates on records in `wv_gis`, the West Virginia geographic information system database, and its admissibility checks include the spatial anchor columns (`spatial_unit_id`, `spatial_unit_kind`) that tie every public claim to a named West Virginia geography. Constitutional filtering and spatial grounding run in the same daily cycle.

The service still does **not** give legal advice or act as a lawyer. It is a **technical mechanism** to enforce internal rules that are themselves influenced by constitutional traditions.

---

## 37.14 What This Chapter Does Not Claim

Within this closure, Chapter 37 does **not** claim:

- perfect legal correctness;
- that the system is a court or legal advisor;
- that all constitutional questions are solved or provably encoded;
- clinical or safety guarantees for downstream human decisions;
- that `runtime_governance.gbim_runtime_lifecycle_daily()` performs constitutional review directly in SQL — it invokes the governance filtering layer that includes constitutional review as one of its gates, not a SQL-native constitutional analysis;
- that ordinary BBB content filtering has received a Guardian/PDR authorization;
- that administrators, mentors, participants, or other ordinary application roles belong automatically in the Guardian authority bundle;
- that the Guardian-governed `user-data-operationalization` path is active today.

It claims:

- a **live constitutional guardian** on port 8091;
- a connected **BBB** on port 8016;
- a protected `/constitutional/check` route;
- a complete fail-closed authorization sequence for `user-data-operationalization`;
- explicit caller authentication, authority-bundle verification, runtime admission, signed operation-intent verification, caller/subject matching, PDR issuance, and one-time intent consumption;
- an intentionally unprovisioned current authority state with zero active callers and zero active subject keys;
- ordinary BBB filtering that remains operational while the governed path is off;
- explicit naming of the **United States** and **West Virginia** constitutions as reference frameworks;
- the Constitutional Principles Service as one of **two named built components of the Recurrent Epistemic Loop**, alongside the DGM validators;
- `runtime_governance.gbim_runtime_lifecycle_daily()` as the scheduled surface that invokes governance filtering on a daily cadence.

---

## 37.15 Step-by-Step View for Rural Developers

In everyday terms, the flow depends on what is being requested.

### Ordinary safeguarded content

1. Ms. Allis constructs ordinary route content and context.
2. The content is sent through the **BBB**.
3. BBB applies its local ethical, spiritual, safety, and threat safeguards.
4. Guardian/PDR authorization is recorded as not applicable unless the request is explicitly classified as `user-data-operationalization`.
5. Other route-specific truth, provenance, coherence, privacy, judge, and promotion controls determine whether any higher-authority transition may proceed.
6. Failures block or constrain the applicable transition and leave an audit trail.

### Explicit governed data operationalization

1. A caller submits a content payload, `X-Caller-Token`, and `X-Operation-Intent`.
2. Guardian verifies the authority bundle and authenticates the caller token.
3. Guardian verifies runtime admission.
4. Guardian verifies the signed operation intent against active subject keys.
5. Guardian checks caller/subject agreement, action/intent agreement, revocations, lifetime, and scope.
6. Guardian applies constitutional and policy review.
7. If all conditions pass, Guardian consumes the intent once and issues a signed PDR.
8. If any condition fails, the operation is blocked and logged.

At present, the second flow stops safely because no active caller or subject identity is provisioned. This is the intended current behavior.

Every day at 03:05, `runtime_governance.gbim_runtime_lifecycle_daily()` fires and advances the governance filtering pass across records currently in the promotion pipeline. This is the Recurrent Epistemic Loop executing on its scheduled cadence.

For rural developers, the key point is that constitutional filtering is both an on-demand safeguard where route conditions require it and a recurring governance concern. Yet exceptional governed data operationalization cannot occur merely because the service is healthy: it requires an active, separately authorized identity and intent chain.

---

## 37.16 Closing Statement

The Constitutional Principles Service makes **constitutional restraint** a real part of Ms. Allis’s promotion path. By running on live ports, applying structured payload review, enforcing a protected caller-to-PDR authorization sequence for governed operations, and explicitly naming the **U.S.** and **West Virginia** constitutions as reference points, it turns constitutional ideas into an operational gate.

As one of the two named built components of the Recurrent Epistemic Loop — alongside the DGM validators — the Constitutional Principles Service is not a standalone check. It participates in a continuous, scheduled governance cycle. The scheduled surface that invokes it is `runtime_governance.gbim_runtime_lifecycle_daily()`, the daily pg_cron job that fires at 03:05 each morning and advances the governance filtering layer across records in the promotion pipeline.

The August 17, 2026 as-built clarification preserves an essential distinction: routine BBB filtering remains live for ordinary system work, while the exceptional `user-data-operationalization` path is currently intentionally unprovisioned and fail closed. If the system later requires that path, it must be activated only through a separately approved authority bundle, protected caller-token delivery, active subject-key custody outside BBB and Guardian, valid signed operation intents, PDR issuance, replay protection, and the required governance approvals.

For rural communities, this means the system’s consequential moves — especially around disclosure and elevated authority — must pass through concrete, inspectable safeguards rather than the good intentions of developers or a merely symbolic constitutional vocabulary.

---

*Chapter 37 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*  
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*  
*See LICENSE for terms.*
