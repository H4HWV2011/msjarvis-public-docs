# 48. Hilbert People Space — Implementation-Aligned Closure

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: August 17, 2026*

---

## 48.1 What This Chapter Is Allowed to Claim

Within this sealed closure, Chapter 48 is limited to **the people-space behavior that has actually been implemented and exercised**.

It may claim that:

- session-derived, person-linked **candidate promotion logic exists** in the people-session promotion service;
- promotion requires **identity, session identity, an allowed application actor role, applicable governance checks, retention consent, and a non-expired retention state**;
- **surveillance-shaped metadata is suppressed** before anything is written into durable people-space;
- durable people-space records are **partitioned into per-user collections**, with **multi-actor partitioning demonstrated**;
- **retention pruning and explicit per-user deletion** are implemented and tested;
- **commons isolation holds**, as shown by an unchanged community commons count when people-space is exercised;
- multi-user readiness depends on application identity, tenant separation, consent, retention, ordinary role enforcement, attribute conditions, and assignment-based access;
- multi-user readiness does **not** depend on enabling Guardian/PDR authorization for every ordinary user interaction;
- the exceptional Guardian-governed `user-data-operationalization` operation remains intentionally disabled and fail closed until a specific consented use case, active identities, governance approval, and operational validation exist.

It does **not** claim large-scale deployment, a rich external civic corpus, fully provisioned multi-tenant production operations, or active Guardian authorization for general people-space use. The focus is on correctness of behavior at the current scale, not volume.

---

## 48.2 Plain-Language Purpose for Rural Developers

For rural operators, this chapter answers:

> “When Ms. Jarvis writes anything about people into long-term memory, what rules does she follow, and how do we know she is not quietly building a surveillance file?”

This chapter explains, step by step:

- how session behavior turns into candidate person-linked records;
- what checks must pass before those candidates become durable people-space entries;
- how entries are kept separate per user and, in future multi-user use, per tenant;
- how deletion and pruning work;
- how commons collections stay unchanged when people-space is exercised;
- why responsible multi-user readiness depends on ordinary application controls rather than activating exceptional Guardian authority for every interaction.

The chapter stays inside the evidence. It addresses behavior already verified in code and tests, while identifying the ordinary application controls required before broader multi-user operation.

---

## 48.3 Where Session-Derived Promotion Logic Lives

Session-derived, person-linked candidate promotion is implemented in a dedicated people-session promotion component.

At a high level, that component:

- takes person-linked signals from a session, such as continuity or identity-relevant context;
- evaluates whether they are eligible to become durable people-space records;
- applies a series of gates;
- only then writes to per-user people-space collections.

This means that **not every session interaction** ends up as durable people-space. There is a concrete promotion service in the path, and it is configured to refuse writes when its conditions are not met.

The promotion service is a routine people-space control. It is not evidence that every session has invoked the exceptional Guardian/PDR-governed operation.

---

## 48.4 Promotion Conditions: Identity, Role, Governance, Consent, and Expiry

For a person-linked candidate to be promoted from a session into durable people-space, the required conditions include:

- **Identity**: the candidate must be tied to a specific user identity;
- **Session identity**: it must come from a properly identified session, not an anonymous or malformed context;
- **Allowed application actor role**: the caller or subsystem must have a role permitted to request the promotion within the ordinary application workflow;
- **Tenant scope where applicable**: the request must be associated with the correct organization, tenant, or bounded service context;
- **Assignment or relationship scope where applicable**: a mentor, support worker, auditor, or other role must have an appropriate relationship to the person or record;
- **Applicable governance pass**: relevant constitutional, privacy, consent, safety, provenance, and promotion controls must not block the promotion;
- **Retention consent**: the user’s consent posture must allow this kind of retention;
- **Non-expired retention state**: the retention configuration must permit the record to remain active and must not already be past its intended lifetime.

If any required condition fails, the promotion logic does not write a durable record. The candidate remains ephemeral or is discarded.

For rural developers, this is a multi-gate doorway: identity, session, application authorization, relevant scope, governance, consent, and retention must all say “yes” before memory is stored.

### Ordinary Governance Does Not Mean Guardian PDR

An applicable governance pass for ordinary people-space promotion does not mean that a Policy Decision Receipt has been issued or that the request has activated Guardian-governed `user-data-operationalization`.

Routine people-space behavior is governed through ordinary application authorization and applicable safeguards. It does not require the exceptional Guardian/PDR pathway for every user interaction.

---

## 48.5 Multi-User Readiness: What It Depends On

Multi-user readiness is not achieved by turning on Guardian for every participant, mentor, administrator, support worker, or session.

It depends on a sound ordinary application-control foundation:

1. **Application identity**  
   The system must reliably distinguish users, sessions, services, and organization contexts. Ephemeral session identity must remain separate from durable registered identity.

2. **Tenant separation**  
   Each organization or tenant must have clear boundaries. A role in one tenant must not automatically create access to people-space records in another tenant.

3. **Consent**  
   Durable retention, disclosure, role-specific use, and any sharing must follow the relevant consent scope. Consent must be recorded, reviewable, and capable of withdrawal where applicable.

4. **Retention enforcement**  
   People-space records must carry and obey retention rules. Records must be pruned when expired, and explicit user deletion must operate within the intended scope.

5. **Role enforcement**  
   Ordinary application roles such as administrator, organization administrator, mentor, participant, support, and auditor must be controlled through role-based permissions.

6. **Attribute and assignment enforcement**  
   Access must also consider tenant, organization membership, mentor-participant assignment, support-case assignment, audit assignment, program membership, purpose, data classification, and workflow state.

7. **Auditable access paths**  
   The system must record relevant promotion, retention, deletion, access, and denial events so operators can investigate whether people-space boundaries are working.

These are the controls that make multi-user use responsible and workable. They keep routine people-space interactions bounded without treating every ordinary memory operation as an exceptional authority transition.

---

## 48.6 Standard Roles Belong to Application Authorization

Future standard roles may include:

- administrator;
- organization administrator;
- mentor;
- participant;
- support;
- auditor.

These are ordinary application roles. They should be managed through role-based access control, attribute-based access control, tenant scoping, and assignment-based access.

### Examples of Ordinary Access Boundaries

- A **participant** may access their own authorized people-space records and approved services.
- A **mentor** may access only the information necessary for participants or cohorts assigned to that mentor.
- A **support** worker may access only the records necessary to resolve an approved support case.
- An **auditor** may inspect approved audit surfaces within a defined audit scope.
- An **organization administrator** may manage members and settings inside their own organization without automatically gaining broad access to all people-space content.
- A platform **administrator** may perform controlled platform operations but should not automatically receive unrestricted access to people-space across all tenants.

These roles do not automatically receive:

- Guardian caller tokens;
- active Guardian caller identities;
- active Guardian subject keys;
- authority to sign operation intents;
- authority to issue or receive a Policy Decision Receipt;
- authority to perform `user-data-operationalization`.

Application authorization answers: “What may this actor do in this tenant, assignment, and workflow?” Guardian authority answers a separate, exceptional question: “May this specific governed operation gain high-assurance constitutional authority?”

---

## 48.7 Surveillance-Shaped Metadata Suppression

Before any record enters durable people-space, surveillance-shaped metadata is removed or never written.

This includes dropping or suppressing:

- unnecessary fine-grained timestamps that would make activity tracking too precise;
- device or network identifiers not required for the stated purpose;
- internal identifiers that would allow reconstruction of a detailed movement or behavior log across sessions;
- cross-tenant identifiers unnecessary for the active workflow;
- broad relationship histories that are unrelated to the stated retention purpose.

The promotion pipeline enforces this at write time, so:

- the durable people-space record contains only what is needed;
- tracking-style fields are kept out of long-term person-linked storage;
- tenant and assignment information remains bounded to the access-control purpose rather than becoming a behavior-tracking record.

The result is that people-space behaves like purpose-bound memory, not a background tracking log.

---

## 48.8 Per-User and Tenant-Scoped People-Space Collections

Durable records landing in Hilbert People Space are stored in **per-user collections**, not in one shared people bucket.

Concretely:

- each user has a dedicated people-space collection;
- promotion logic writes only to that user’s collection;
- a query for one user’s people-space does not reach another user’s records.

This is more than an access-control rule; it is a **storage-level separation**. The data is partitioned per user, and the system uses these partitions consistently.

For future multi-user operation, per-user partitioning must also be paired with tenant separation:

- user identity should be associated with the correct tenant or organization context where relevant;
- tenant-scoped access checks should prevent a user or role in one organization from crossing into another organization’s people-space;
- role and assignment rules should determine whether any person other than the subject can access an approved bounded view.

Per-user storage separation is necessary, but by itself it is not the entire multi-user authorization model.

---

## 48.9 Multi-Actor Partitioning: Alpha and Beta People-Space

The system’s multi-actor behavior has been demonstrated by creating at least two distinct people-space collections, often referred to as “alpha” and “beta.”

In practice, this means:

- separate people-space collections were created for two different actors;
- promotion logic wrote records into each actor’s people-space;
- checks confirmed that no records leaked from one to the other;
- retrieval for alpha did not surface beta’s data, and vice versa.

This test proves that per-user partitioning works for more than one user, not just in a single hard-coded example.

The alpha-and-beta demonstration does not, by itself, prove every future tenant, organization, mentor assignment, support case, audit scope, or production identity workflow. It demonstrates the storage-level foundation on which those additional ordinary authorization controls must operate.

---

## 48.10 Retention Pruning and Explicit Per-User Deletion

This closure confirms that **retention pruning and explicit per-user deletion are implemented and tested**.

Two mechanisms exist:

- **Retention pruning**: background jobs or scheduled processes look at retention metadata, such as timestamps and configured lifetimes, and remove expired people-space records;
- **Explicit deletion**: a per-user deletion request can target that user’s people-space, and the system removes the selected records.

Tests validate that:

- after pruning runs, expired records are gone;
- after explicit deletion, those records no longer appear in people-space for that user;
- these operations do not affect other users’ collections.

For rural developers, this means people-space has real “forget” behavior, not merely promises.

For future multi-user readiness, deletion and retention workflows must also respect:

- the correct user identity;
- the relevant tenant or organizational boundary;
- the consent and retention basis for the record;
- role and assignment restrictions for administrative support;
- the distinction between a user’s request to delete their own record and a privileged administrative retention workflow.

Retention and deletion do not require enabling Guardian/PDR authorization for every routine action. They require reliable application identity, consent, retention policy, tenant separation, and ordinary role enforcement.

---

## 48.11 Commons Isolation: Community Commons Stays Unchanged

Commons isolation means that private people-space does not quietly feed community-wide or public collections.

This is demonstrated by:

- running people-space promotion and deletion operations;
- observing that the `community_hilbert_commons` collection’s document count remains unchanged;
- verifying that no code path in the people-space pipeline writes into the commons collection.

So even when people-space is active:

- the community commons remains empty or unchanged;
- people-linked records do not spill over into shared civic or public views;
- a user’s role, organization membership, mentor assignment, or support relationship does not itself create a public disclosure right.

This is a concrete, testable version of the promise: private stays private unless an explicit, separately governed disclosure or civic-promotion path applies.

---

## 48.12 Exceptional Guardian/PDR-Governed Operations

The protected Guardian/PDR-governed operation is:

```text
user-data-operationalization
```

It is intentionally distinct from:

- normal session continuity;
- ordinary identity registration;
- ordinary people-space candidate promotion;
- routine retention pruning;
- explicit per-user deletion;
- ordinary participant, mentor, support, auditor, or administrator workflows;
- tenant-scoped and assignment-based access decisions.

Guardian/PDR governance requires a separate high-assurance sequence:

1. Caller token.
2. Verified authority bundle.
3. Runtime admission.
4. Signed operation intent.
5. Caller-subject identity match.
6. Exact operation, scope, audience, purpose, validity, and revocation checks.
7. Constitutional and policy approval.
8. Policy Decision Receipt issuance.
9. One-time operation-intent consumption.

As of August 17, 2026, this authority path is intentionally unprovisioned:

```json
{
  "active_callers": 0,
  "active_subject_keys": 0,
  "governed_operation_authorization": "unavailable_fail_closed"
}
```

The operating decision is:

```text
Keep user-data-operationalization off.
```

This means that ordinary multi-user readiness must be built and assessed through application identity, tenant separation, consent, retention, and role enforcement. It does not require, and should not be confused with, enabling Guardian for every user interaction.

---

## 48.13 Conditions Before Governed Operationalization

The exceptional governed operation must remain disabled until all of the following exist:

1. **A specific consented use case**  
   The use case must identify what data is involved, why operationalization is necessary, who is affected, what consent is required, what benefits and risks exist, and what boundaries apply.

2. **Deliberately provisioned active identities**  
   Active Guardian callers and active subject signing keys must be created only for the approved use case, with controlled custody, expiration, revocation, and audit procedures.

3. **Governance approval**  
   The authority bundle, runtime-admission record, consent model, operation-intent policy, PDR policy, and replay-protection process must receive required governance approval.

4. **Operational validation**  
   The path must be tested for fail-closed behavior, tenant isolation, consent handling, identity binding, logging, revocation, one-time intent consumption, and rollback readiness.

5. **Applicable community, institutional, ethical, and legal review**  
   Technical authorization is not a substitute for the review appropriate to the actual use case.

Until these conditions are met, the correct and intended state is:

```text
governed operation authorization unavailable fail closed
```

This is a protective decision, not a feature gap to bypass.

---

## 48.14 No Claim of Scale

The academic limitation for this closure is clear:

- it does not claim that people-space has been populated at large scale;
- it does not claim a rich external civic corpus of person-linked data;
- it does not claim that every future multi-tenant application workflow has been fully provisioned;
- it does not claim that ordinary roles can substitute for consent, tenant boundaries, retention enforcement, or assignment checks;
- it does not claim that Guardian-governed operationalization is active.

Instead, it claims:

- that the people-space pipeline and safeguards described above work on the current, limited corpus;
- that per-user partitioning has been demonstrated across more than one actor;
- that retention pruning, explicit deletion, metadata suppression, and commons isolation are implemented and tested;
- that responsible multi-user readiness requires ordinary application identity, tenant separation, consent, retention, and role enforcement;
- that exceptional Guardian/PDR authority remains intentionally disabled until separately justified, consented, approved, provisioned, and validated.

For readers and rural operators, that means you can trust the shape and tested behavior of people-space at the current scale, but should not assume it already holds a large, diverse body of real-world civic person data or a completed multi-user production program.

---

## 48.15 Step-by-Step View for Rural Developers

Putting the implementation-aligned behavior together, the people-space path looks like this:

1. **A session produces a person-linked candidate.**  
   Ms. Jarvis identifies something that might be useful to remember about a person.

2. **The ordinary promotion logic runs.**  
   It checks identity, session identity, application role, tenant and assignment scope where applicable, governance rules, consent, and retention settings.

3. **If checks pass, a record is prepared.**  
   Surveillance-shaped metadata is dropped or suppressed, and the record is scoped to one user.

4. **The record is written to that user’s people-space collection.**  
   Alpha goes to alpha’s collection; beta goes to beta’s; no mixing occurs.

5. **Ordinary access remains bounded.**  
   Any future participant, mentor, support, auditor, organization administrator, or administrator access must be controlled through role, tenant, assignment, consent, purpose, and data-classification rules.

6. **Pruning and deletion keep the space bounded.**  
   Expired records are pruned, and authorized per-user deletion requests remove selected records.

7. **Commons stays separate.**  
   Community commons collections do not change when people-space is exercised unless a separate explicit civic-promotion path is used.

8. **Exceptional governed operationalization remains off.**  
   Routine people-space use does not require Guardian/PDR authorization. The exceptional `user-data-operationalization` path stays disabled until a specific consented use case, active identities, governance approval, and operational validation exist.

If an ordinary promotion condition fails, the system fails closed by not promoting. If an exceptional governed operation is requested, it also fails closed under the current intentionally unprovisioned authority state.

---

## 48.16 Closing Statement

Chapter 48 presents **Hilbert People Space as it actually behaves today**.

Session-derived person-linked promotion logic exists and is guarded by identity, session, ordinary application authorization, applicable governance checks, consent, and retention conditions. Surveillance-shaped metadata is suppressed before durable storage. Durable people-space is partitioned per user with multi-actor separation demonstrated. Deletion and pruning are real and tested. Commons collections remain unchanged when people-space is active.

Responsible multi-user readiness depends on application identity, tenant separation, consent, retention, ordinary RBAC and ABAC, assignment-based access, and auditable enforcement. It does not require enabling Guardian/PDR authority for every user interaction.

The exceptional `user-data-operationalization` path remains intentionally disabled and fail closed. It should be activated only when a specific consented use case, deliberately provisioned active identities, required governance approval, and operational validation exist.

The system therefore holds person-linked state in a governed, bounded, and non-surveillance-shaped way at the current scale while honestly acknowledging that broader multi-user deployment and large-scale civic population remain future work.

---

*Chapter 48 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*  
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*  
*See LICENSE for terms.*
