# 47. Hilbert People Space Without Surveillance (As-Built)

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: August 17, 2026*

---

## 47.1 What This Chapter Is Allowed to Claim

Within this closure gate, Chapter 47 is limited to **implemented, governed people-space behavior** for the West Virginia slice of H_App and H_geo, with a specific focus on **non-surveillance boundaries**.

It may claim that:

- there is a **live non-surveillance boundary** enforced at the database layer for `public.gbim_record` when accessed under the `public_instrument_role`;
- attempts by `public_instrument_role` to read or query person-identifiable GBIM records result in **permission denied**, not silent access;
- this permission denial is **intentional, governed, and verified**, not an accident of misconfiguration;
- the non-surveillance boundary complements the **overflow design** by ensuring that:
  - instruments and public tools see only **admissible, minimized public fields**;
  - direct surveillance-style access to the governed GBIM corpus is blocked;
- ordinary access to people-space must be constrained by role-based access control, attribute-based access control, tenant scoping, assignment relationships, consent, purpose, and data classification;
- exceptional Guardian/PDR-governed operationalization is currently disabled because no specific consented use case, active Guardian identities, or required governance approval has been established.

It must **not** claim perfect global non-surveillance behavior across all systems, a fully general privacy algebra, or active authorization for Guardian-governed data operationalization.

---

## 47.2 Plain-Language Purpose

For rural developers, this chapter answers a concrete question:

> “How does Ms. Allis keep people-space safe from being turned into a surveillance engine?”

This chapter explains:

- what **Hilbert people space** means in this narrow context;
- how **permission denied** on `gbim_record` under `public_instrument_role` works as a live non-surveillance boundary;
- how that boundary aligns with overflow-design principles of minimal fields and least privilege;
- how ordinary role, tenant, assignment, consent, and purpose controls limit routine access;
- why the system keeps exceptional governed operationalization disabled until a specific consented use case, active identities, and governance approval exist.

The focus is on **what is enforced today** in the governed stack, not on every possible privacy theory.

---

## 47.3 Hilbert People Space in This Gate

In earlier chapters, Hilbert spaces were used to describe structured bodies of knowledge and state. Here, “Hilbert people space” is a conceptual name for the governed body of people-related information:

- person-space events;
- validation results;
- registered identity metadata;
- assignment and relationship metadata where authorized;
- governed GBIM records that touch individual experience indirectly through geography and infrastructure;
- consent, retention, disclosure, and tenant-scope metadata.

Within this gate, Hilbert people space is:

- a **structured, governed body of state** about people and their context;
- subject to **non-surveillance constraints** that prevent direct high-resolution person tracking by public instruments;
- linked to geography through H_geo, but not available for unrestricted inspection under public-use roles;
- governed through ordinary authorization boundaries before any user, service, or role can access a relevant portion of it;
- not an automatically available source for exceptional data operationalization.

For rural developers, Hilbert people space is “everything in the system about people and their places that must not be turned into a live surveillance feed.”

---

## 47.4 The Non-Surveillance Boundary: `permission denied` on `gbim_record`

The key live enforcement mechanism at this gate is simple and strong:

- under the **`public_instrument_role`**, direct access to `public.gbim_record` is **denied**;
- attempts to read or query GBIM records using that role result in `permission denied`, not partial access.

This is not a bug. It is enforcement of the non-surveillance boundary.

### 47.4.1 What “Permission Denied” Means Here

At the database level, `permission denied` means:

- the role `public_instrument_role` does **not** have `SELECT` on `public.gbim_record`;
- it cannot run queries that dump governed GBIM rows;
- it is restricted to higher-level, minimized views or functions designed for public answers and instruments.

From a non-surveillance viewpoint:

- instruments cannot quietly bypass governance and pull raw person-space or fine-grained infrastructure data at will;
- access must go through governed public surfaces designed to minimize fields and enforce least privilege;
- public-answer access does not create access to the full governed corpus.

The denial is the live wall that keeps Hilbert people space from becoming a surveillance data lake for public tools.

### 47.4.2 What the Boundary Does Not Mean

The database denial does not mean every actor is denied every people-space workflow.

It means public instruments cannot directly browse the raw governed table. Other access remains subject to applicable ordinary controls:

- role-based access control;
- attribute-based access control;
- tenant scoping;
- assignment-based relationships;
- consent;
- purpose limitation;
- data classification;
- workflow state;
- audit requirements.

The boundary is intentionally layered. A valid application role may enable a narrowly scoped workflow without granting raw-table access or exceptional Guardian authority.

---

## 47.5 Ordinary Access: RBAC, ABAC, Tenant, and Assignment Boundaries

Routine access to people-space is governed through ordinary application authorization, not through the Guardian authority bundle.

### Role-Based Access Control

Role-based access control, or RBAC, defines the routine permissions associated with application roles such as:

- administrator;
- organization administrator;
- mentor;
- participant;
- support;
- auditor.

These roles determine what an authenticated person may do in ordinary application workflows. For example:

- a participant may view their own authorized information;
- a mentor may work with assigned participants or cohorts;
- a support worker may address an approved support case;
- an auditor may inspect authorized audit surfaces;
- an organization administrator may manage members and settings within their own organization;
- a platform administrator may perform separately controlled platform operations.

A role name alone should not grant broad access to people-space.

### Attribute-Based Access Control

Attribute-based access control, or ABAC, adds contextual requirements to a decision.

Relevant attributes may include:

- tenant or organization identifier;
- organization membership;
- mentor-participant assignment;
- support-case assignment;
- program enrollment;
- consent scope;
- data classification;
- purpose of access;
- workflow state;
- service area or geography;
- time window;
- public-opt-in status.

For example, a mentor with a valid mentor role may still be denied access if the participant is not assigned to that mentor, belongs to a different organization, has not provided the applicable consent, or has data classified outside the mentor workflow.

### Tenant Scoping

Tenant scoping determines **where** an application role applies.

- An organization administrator in Organization A does not automatically administer Organization B.
- A mentor assigned in one organization cannot browse participants in another organization.
- A support worker may see only records necessary for an approved support task.
- An auditor may see only records within an assigned audit scope.
- A platform administrator should not inherit unrestricted access to all people-space records by default.

Tenant scoping prevents a legitimate local role from becoming a cross-community surveillance credential.

### Assignment-Based Access

Assignment-based access requires a specific working relationship in addition to a general role.

Examples include:

- a mentor assigned to a participant or cohort;
- a support worker assigned to a support case;
- an auditor assigned to an audit engagement;
- a coordinator assigned to an approved program;
- an organization administrator acting inside the organization they administer.

For rural developers, this is the difference between “you work at the clinic” and “you are assigned to this person’s care team.” A general role may establish a category of work; a specific assignment establishes a bounded reason to access a particular case.

---

## 47.6 How This Complements Overflow Design

Other chapters describe overflow queues and overflow public context designed with:

- **minimal fields** — carrying only what is necessary to route and understand overflow events;
- **least privilege** — exposing the smallest slice of state needed for the job;
- **bounded public context** — preventing raw governed state from being copied into public-facing queue payloads.

The `permission denied` boundary for `public_instrument_role` complements that design:

- overflow payloads are already minimized;
- even if someone tried to use `public_instrument_role` to rehydrate full GBIM context behind those events, they would hit the permission wall;
- a public instrument cannot transform a minimized overflow hint into arbitrary raw-person-space access.

In practical terms:

- overflow events contain only carefully selected public-context fields;
- the role used by instruments to read public hints about those events cannot reach back to the full GBIM corpus;
- ordinary application users who need a workflow-specific view remain limited by RBAC, ABAC, tenant, assignment, consent, and purpose controls;
- exceptional governed operationalization remains unavailable unless separately activated through its own authority process.

For rural developers, this means the overflow design is not just about structuring payloads. It is supported by real access controls that prevent misuse.

---

## 47.7 Exceptional Guardian/PDR-Governed Operations

Ordinary access to people-space and exceptional governed operationalization are different.

The protected Guardian operation is:

```text
user-data-operationalization
```

This operation is not enabled by:

- being a participant;
- being a mentor;
- being support staff;
- being an auditor;
- being an organization administrator;
- being a platform administrator;
- being assigned to a participant, case, program, or audit;
- being in the correct tenant;
- having access to an admissible view;
- having database or runtime-governance permissions.

A Guardian/PDR-governed operation requires a separate, high-assurance sequence:

1. Caller token.
2. Verified authority bundle.
3. Runtime admission.
4. Signed operation intent.
5. Caller and subject identity match.
6. Exact operation, scope, audience, purpose, validity-window, and revocation checks.
7. Constitutional and policy review.
8. Policy Decision Receipt issuance.
9. One-time operation-intent consumption.

This sequence ensures that routine application permissions do not quietly become authority to operationalize user data.

---

## 47.8 Decision: Keep Governed Operationalization Disabled

As of August 17, 2026, the operating decision is:

```text
Keep user-data-operationalization off.
```

The Guardian authority bundle is intentionally unprovisioned for active governed operations:

```json
{
  "active_callers": 0,
  "active_subject_keys": 0,
  "governed_operation_authorization": "unavailable_fail_closed"
}
```

This means:

- no active caller can authenticate for the Guardian-governed path;
- no active subject key can sign an accepted operation intent;
- no standard application role is treated as a Guardian caller or Guardian subject;
- no Policy Decision Receipt can be issued for `user-data-operationalization`;
- a request for that operation fails closed.

### Conditions Required Before Activation

Governed operationalization must remain disabled until all of the following exist:

1. **A specific consented use case**  
   The operation must have a concrete, documented purpose. “Possible future use” or broad administrative convenience is not enough. The use case must identify what data is involved, why operationalization is necessary, who benefits, what risks exist, and what the approved boundaries are.

2. **Active identities**  
   The authority system must have deliberately provisioned active caller identities and active subject keys. These identities must be limited to the approved use case and maintained through controlled credential custody, revocation, expiration, and audit procedures.

3. **Governance approval**  
   The use case, authority-bundle configuration, runtime admission conditions, consent requirements, subject-intent rules, PDR policy, and one-time-consumption procedures must receive the required governance approval before activation.

4. **Operational evidence**  
   The activation path must be tested in a controlled environment and validated for fail-closed behavior, consent handling, tenant boundaries, logging, revocation, replay protection, and rollback.

5. **Community and legal review where applicable**  
   Technical authorization does not replace appropriate community, institutional, ethical, or legal review. These review requirements depend on the actual use case.

Until those conditions exist together, the correct state is:

```text
governed operation authorization unavailable fail closed
```

This is a safety and accountability decision, not a missing feature to be bypassed.

### Cross-Reference to Related Controls

This decision aligns with:

- Chapter 36, which distinguishes identity registration and ordinary application roles from Guardian authority;
- Chapter 37, which documents the caller-token-to-PDR Guardian sequence and intentional unprovisioned state;
- Chapter 40, which records production validation and the explicit fail-closed operational state;
- Chapter 43, which distinguishes ordinary RBAC, ABAC, tenant scoping, and assignment-based access from exceptional Guardian/PDR-governed operations.

---

## 47.9 Step-by-Step Explanation for Rural Developers

From a local operator’s point of view, the non-surveillance boundary over Hilbert people space can be understood in seven steps:

1. **A governed GBIM corpus exists.**  
   GBIM records hold spatially and temporally anchored infrastructure and geography-linked state, including fields that could contribute to a surveillance story if misused.

2. **Public instruments use `public_instrument_role`.**  
   Dashboards, public tools, and similar instruments connect using a role intended for public-facing, least-privilege behavior.

3. **Direct GBIM access is denied.**  
   That role does not have `SELECT` rights on `public.gbim_record`. Attempts to query it return `permission denied`.

4. **Public surfaces are minimized.**  
   Instruments can see only minimized views or derived public packets that expose necessary public fields and respect admissibility and overflow-safe design.

5. **Ordinary application access is bounded.**  
   A participant, mentor, support worker, auditor, administrator, or organization administrator receives only the access permitted by role, tenant, assignment, consent, purpose, and data classification.

6. **Exceptional operationalization remains off.**  
   No ordinary role, assignment, or tenant relationship can activate Guardian-governed data operationalization.

7. **Hilbert people space remains governed.**  
   High-resolution person-space state remains inside governed cores. It is not available to public instruments for arbitrary querying, and it is not available for exceptional data operationalization until a specific consented use case, active identities, and governance approval exist.

This is the live shape of “Hilbert people space without surveillance” at this gate.

---

## 47.10 Why This Matters for Rural Communities

GIS-anchored data and GBIM records are powerful. Without boundaries, they could be misused:

- to track individuals or groups across time and space;
- to infer sensitive information about small communities;
- to build unauthorized surveillance tools;
- to combine ordinary organizational access with excessive people-space visibility;
- to treat administrative convenience as a reason to operationalize sensitive user data.

The `permission denied` boundary for `public_instrument_role` matters because it ensures:

- public tools cannot quietly become surveillance dashboards over governed GBIM data;
- access to person- or place-linked data must go through governed public-answer surfaces;
- routine application access can be narrowed by role, assignment, tenant, consent, and purpose;
- high-assurance data operationalization cannot be activated merely because someone has an ordinary administrative or service role.

For rural communities, this is a concrete safeguard:

- the same system that helps plan broadband or infrastructure is not simultaneously turned into an ungoverned tracker of individual lives;
- the non-surveillance promise is supported by live data-layer enforcement;
- exceptional authority remains disabled until there is a real, consented, approved reason to create it.

---

## 47.11 Relationship to Admissibility and Phi Probe

Earlier chapters introduced:

- **ten-condition admissibility**, which governs which records are allowed to support public claims;
- the **Phi probe**, which measures semantic coherence by counting admissible records.

The non-surveillance boundary described here interacts with those layers consistently:

- admissibility determines **what can be spoken** as public claims;
- the Phi probe measures **how much governed state is ready to be spoken**;
- ordinary authorization determines **who may access what routine workflow information under what scope**;
- the non-surveillance boundary determines **how public instruments can see or cannot see the underlying governed corpus**;
- Guardian/PDR governance determines whether a narrow, exceptional user-data operationalization operation can gain authority.

Together:

- admissibility and Phi say “what is speakable and coherent”;
- RBAC, ABAC, tenant, and assignment rules say “who may access a bounded workflow context”;
- `permission denied` for `public_instrument_role` says “public instruments cannot dump raw governed state”;
- the disabled Guardian path says “no exceptional operationalization occurs without a consented use case, active identities, and governance approval.”

For rural developers, this is layered protection: coherence, admissibility, least privilege, tenant boundaries, consent, and exceptional authority controls reinforce one another.

---

## 47.12 Implementation Status

Within this gate, Chapter 47 is allowed to record the following implementation status:

- `public_instrument_role` lacks `SELECT` on `public.gbim_record`; attempts to query GBIM records under this role result in `permission denied`.
- Overflow-safe public context and public-answer surfaces are designed with minimal fields and least privilege, so instruments use these surfaces instead of raw tables.
- Hilbert people space is not directly visible to public instruments; it remains inside governed cores and answer packets.
- Ordinary future application roles are conceptually bounded by RBAC, ABAC, tenant scoping, and assignment-based access rather than treated as broad people-space permissions.
- Guardian/PDR-governed `user-data-operationalization` is intentionally disabled.
- The current Guardian authority state is:

  ```text
  governed operation authorization unavailable fail closed
  ```

- Activation is deferred until a specific consented use case, active caller and subject identities, required governance approval, and operational validation are in place.

The non-surveillance boundary and fail-closed governance posture are live design commitments, not hypothetical aspirations.

---

## 47.13 What This Chapter Does Not Claim

To stay inside scope, this chapter does **not** claim:

- global non-surveillance perfection across all possible roles, services, or deployments;
- a complete privacy calculus for every domain;
- that no misconfiguration could ever occur elsewhere;
- that every future application role matrix has already been provisioned;
- that an ordinary application role, assignment, or tenant membership can authorize Guardian/PDR-governed operations;
- that governed operationalization is currently active;
- that a technical approval alone is sufficient without a specific consented use case and appropriate governance review.

It claims:

- a specific, implemented non-surveillance boundary for `public.gbim_record` under `public_instrument_role`;
- alignment of this boundary with overflow-design principles of minimal fields and least privilege;
- a governed Hilbert people space protected from direct public-instrument queries;
- ordinary access boundaries based on RBAC, ABAC, tenant scoping, assignment, consent, purpose, and data classification;
- an explicit decision to keep `user-data-operationalization` disabled until a specific consented use case, active identities, and governance approval exist.

---

## 47.14 Closing Statement

Chapter 47 records an **as-built non-surveillance boundary** over Hilbert people space.

By denying direct access to `public.gbim_record` for `public_instrument_role`, and by pairing that denial with minimized overflow and public-answer surfaces, the system ensures that public instruments serving rural communities cannot quietly turn governed GBIM data into a surveillance feed.

Ordinary access is not unrestricted either. It must be controlled through role-based access, attributes, tenant boundaries, assignment relationships, consent, purpose, and data classification. Standard roles such as participant, mentor, support, auditor, organization administrator, and administrator belong to those ordinary access controls. They do not create Guardian authority.

The system also makes an explicit operational decision: keep `user-data-operationalization` disabled. It remains unavailable and fail closed until there is a specific consented use case, deliberately provisioned active caller and subject identities, required governance approval, and successful operational validation.

For rural developers, this means they can build and operate public instruments on top of H_App and H_geo while knowing that core people-space is not exposed for arbitrary querying or exceptional operationalization. The boundary is simple, strong, and live: permission denied where surveillance would begin, and fail closed where exceptional authority would otherwise be claimed.

---

*Chapter 47 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*  
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*  
*See LICENSE for terms.*
