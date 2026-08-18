# 43 — Role-Gated Knowledge Access

*Carrie Kidd (Mamma Kidd) — Mount Hope, West Virginia*  
*Last Updated: August 17, 2026*

---

## 43.1 Purpose of Role-Gated Access

This chapter describes how Ms. Jarvis governs who can see and do what inside its knowledge system.

The architecture has two distinct access-control domains:

1. **Ordinary application and database access control** — role-based access control, attribute-based access control, tenant scoping, and assignment-based permissions.
2. **Exceptional Guardian/PDR-governed operations** — a narrow, high-assurance authority path for the protected operation `user-data-operationalization`.

These domains must not be confused.

Ordinary access control determines whether an authenticated person, service, or database role may access a resource within a defined scope. Exceptional Guardian authority determines whether a narrowly defined governed operation may receive constitutional authorization and a Policy Decision Receipt.

For rural developers, this chapter explains why some queries succeed, others fail, and why holding a normal application role does not automatically grant authority for exceptional governed operations.

---

## 43.2 Two Access-Control Domains

### Ordinary RBAC, ABAC, and Assignment-Based Access

Ordinary access control governs routine work in the application and database.

It includes:

- **RBAC — role-based access control:** permissions associated with a role, such as participant, mentor, support, auditor, organization administrator, or platform administrator.
- **ABAC — attribute-based access control:** permission decisions based on attributes such as tenant ID, organization membership, assignment relationship, consent scope, data classification, workflow state, geography, or time window.
- **Assignment-based access:** access granted because a person is specifically assigned to a participant, program, support case, audit engagement, organization, or operational task.
- **Tenant scoping:** limits that prevent a valid role in one organization from automatically accessing records or functions in another organization.
- **Database roles and row-level security:** controls that determine which services and database users can access raw tables, admissible views, audit records, or governance functions.

These controls answer questions such as:

- Is this participant allowed to view their own record?
- Is this mentor assigned to this participant or cohort?
- Is this organization administrator acting within their own tenant?
- Is this support worker assigned to this approved support case?
- Is this auditor authorized to inspect this audit scope?
- Is this public instrument role allowed to read the admissible view but not the raw governed table?

### Exceptional Guardian/PDR-Governed Operations

Guardian/PDR governance applies only to the narrow protected operation:

```text
user-data-operationalization
```

This is not normal application access. It is not granted by holding an application role, possessing a tenant membership, having a mentor assignment, or being an organization administrator.

The protected Guardian path requires:

- a caller token;
- a verified authority bundle;
- runtime admission;
- a signed operation intent;
- caller and subject identity matching;
- operation, scope, audience, purpose, and revocation checks;
- constitutional and policy review;
- Policy Decision Receipt issuance;
- one-time intent consumption.

This path answers a different question:

**May this exact, explicitly governed operation gain high-assurance authority?**

---

## 43.3 The Three-Tier Database Role Model

The database knowledge-access architecture uses three core roles:

1. `postgres` superuser.
2. `runtime_governance_role`.
3. `public_instrument_role`.

Each database role has a specific job and specific permissions. Together, they ensure that:

- full database access is rare and carefully handled;
- governance operations see what they need to maintain lifecycle and admissibility;
- public-facing tools see only filtered, admissible evidence and approved audit surfaces;
- no ordinary database role is silently treated as a Guardian authority identity.

| Database role | Main function | Raw governed data | Public admissible data | Guardian authority |
|---|---|---:|---:|---:|
| `postgres` | Database maintenance and emergency administration | Full access | Full access | Not automatically granted |
| `runtime_governance_role` | Lifecycle, admissibility, governance functions, audit writing | Full governed access | Access as needed | Not automatically granted |
| `public_instrument_role` | Public answer and public-context serving | No direct access | Read-only approved access | Not automatically granted |

The word “role” therefore has different meanings depending on context:

- a database role controls database permissions;
- an application role controls routine product permissions;
- a Guardian authority identity participates in a separate cryptographic authorization system.

A person or service can hold one of these forms of role without possessing the others.

---

## 43.4 Tier One — postgres Superuser

### 43.4.1 Responsibilities

The `postgres` superuser is the top-level database administrator. This role:

- manages schema changes and migrations;
- creates and alters roles and permissions;
- installs or updates functions, views, and policies;
- manages row-level-security policy definitions;
- performs rare maintenance or emergency recovery operations.

In practice, this role is used sparingly. It exists for maintenance and emergency operations, not everyday application queries.

### 43.4.2 Access Level

The superuser:

- can bypass row-level security and see all tables;
- can modify governed tables and views;
- can create, alter, or remove policies and constraints;
- can manage database roles and grants.

Because this role is powerful, it is not used by application code. Rural developers should treat it like the key to the whole building: necessary, but not something to hand out freely.

### 43.4.3 Superuser Is Not Guardian Authority

Possessing database-superuser access does not automatically create Guardian authority.

A `postgres` superuser:

- is not automatically an active Guardian caller;
- does not automatically receive a Guardian caller token;
- does not automatically possess an active Guardian subject key;
- cannot legitimately bypass the Guardian/PDR sequence for `user-data-operationalization`;
- is not authorized to convert a database permission into a constitutional authorization.

Database administration and exceptional governed-operation authority remain separate controls.

---

## 43.5 Tier Two — runtime_governance_role

### 43.5.1 Responsibilities

The `runtime_governance_role` is responsible for **internal governance operations**. This includes:

- running lifecycle-refresh functions;
- maintaining admissible views;
- logging audit entries;
- performing test-harness operations;
- evaluating governed state needed to decide what becomes speakable;
- operating approved promotion, validation, and minimization functions.

This role is where runtime governance lives. It sees stored and admissible state in order to decide what becomes publicly speakable.

### 43.5.2 Access Level

The `runtime_governance_role` has:

- full access to `public.gbim_record`, the stored governed table;
- a row-level-security policy using:

  ```text
  USING (true)
  ```

- permission to read and write governance tables in `runtime_governance`;
- permission to call governance functions that affect lifecycle and admissibility;
- authority to maintain audit records and governed views.

In effect, `runtime_governance_role` is the internal caretaker of governed state. It must see necessary internal data to decide what becomes admissible, but it does not speak directly to the public.

For rural developers, this role is like the worker who can enter the storage rooms, rearrange shelves, inspect inventory, and update stock, but cannot directly run the public front desk.

### 43.5.3 Runtime Governance Is Not Guardian Authority

The ability to evaluate lifecycle, maintain admissible views, or write an audit record does not grant Guardian authority.

`runtime_governance_role`:

- does not automatically hold a Guardian caller token;
- does not automatically create or sign an operation intent;
- does not automatically act as a subject in Guardian authorization;
- cannot treat a database-level promotion function as a Policy Decision Receipt;
- cannot authorize `user-data-operationalization` merely because it has access to internal governed state.

If a future workflow requires the exceptional Guardian-governed operation, it must still satisfy the separate caller-token, authority-bundle, runtime-admission, signed-intent, caller-subject-match, PDR-issuance, and one-time-consumption sequence.

---

## 43.6 Tier Three — public_instrument_role

### 43.6.1 Responsibilities

The `public_instrument_role` backs public-facing tools and services. This role:

- calls `public_answer_packet` to serve structured answers;
- reads admissible views and approved audit logs;
- interacts with approved public-context and overflow surfaces;
- provides the public-facing voice of the system within bounded evidence rules.

Its vision is deliberately limited.

### 43.6.2 Access Level

The `public_instrument_role` has:

- **read-only access** to the admissible materialized view, such as `public.public_admissible_gbim_mv`;
- **read-only access** to governance audit tables, such as `runtime_governance.public_answer_audit`;
- permission to execute hardened functions such as `runtime_governance.public_answer_packet`;
- **no direct access** to `public.gbim_record`.

Attempts by `public_instrument_role` to select from the raw governed table result in a permission error.

This means that the public instrument can see only what has been declared admissible or intentionally exposed through approved audit surfaces. It cannot browse raw governed state.

For rural developers, this role is like the front-desk clerk: able to see the catalog and records of what has been approved for public handling, but unable to walk into the back room without permission.

### 43.6.3 Public Instrument Is Not Guardian Authority

The public instrument is not a Guardian authority holder.

It cannot:

- turn an ordinary public answer into a governed data operation;
- create Guardian caller credentials;
- sign subject operation intents;
- obtain a PDR merely because a request is visible through an admissible view;
- use public-facing access to bypass consent, tenant, or authority boundaries.

Public speakability is not the same thing as authority to operationalize user data.

---

## 43.7 Application RBAC and Tenant Scoping

Database roles are only one layer of access control. Application users require a separate, ordinary authorization model.

Standard future application roles may include:

- administrator;
- organization administrator;
- mentor;
- participant;
- support;
- auditor.

These roles belong to ordinary application authorization. Their permissions should be determined through RBAC, ABAC, tenant scoping, and assignment relationships.

### Role-Based Access Control

RBAC assigns permissions associated with a role.

Examples include:

- A **participant** may view their own authorized information and participate in approved workflows.
- A **mentor** may review information from participants or cohorts to whom they are assigned.
- A **support** worker may access an approved support case.
- An **auditor** may read authorized audit surfaces.
- An **organization administrator** may manage members and settings within their own organization.
- A platform **administrator** may perform controlled platform operations.

A role name should never be treated as unlimited access. Permissions should be explicit and least-privilege.

### Attribute-Based Access Control

ABAC adds context-sensitive conditions to an access decision.

Relevant attributes can include:

- tenant or organization ID;
- membership status;
- mentor-participant assignment;
- support-case assignment;
- program enrollment;
- consent scope;
- data classification;
- geography or service area;
- time window;
- workflow state;
- purpose of access;
- public-opt-in status.

For example, a mentor may have a mentor role but still be denied access if:

- the participant is not assigned to that mentor;
- the participant belongs to a different tenant;
- the data classification does not permit mentor access;
- the consent scope does not cover the requested use;
- the access occurs outside an authorized program or time window.

### Tenant Scoping

Tenant scoping determines where an application role applies.

Examples:

- An organization administrator in Organization A does not automatically manage Organization B.
- A mentor assigned in one organization cannot browse participants in another organization.
- A support worker should see only cases necessary for an approved support task.
- An auditor should see only audit records within the audit scope they were assigned.
- A platform administrator should not inherit unrestricted user-data access in every tenant by default.

Tenant scoping prevents a legitimate role from becoming a broad cross-community access credential.

---

## 43.8 Assignment-Based Access

Assignment-based access adds a practical boundary beyond general role membership.

A person may have the correct general role but still require a specific assignment to access a particular record, person, case, program, or workflow.

Examples:

- A mentor must be assigned to a participant or cohort before accessing mentorship materials.
- A support worker must be assigned to an active support case before seeing case-specific details.
- An auditor must be assigned to a defined audit engagement or scope.
- A program coordinator must be assigned to an approved program before managing program-specific participant workflows.
- An organization administrator must act within the tenant they administer.
- A participant may access only their own records unless another approved relationship is present.

Assignment-based access supports least privilege. It reduces the risk that broad organizational roles become broad surveillance permissions.

For rural developers, it is the difference between “you work at the clinic” and “you are assigned to this patient’s care team.” The first may establish a general role; the second establishes a specific, purpose-bounded relationship.

---

## 43.9 Ordinary Access Does Not Create Guardian Authority

Ordinary RBAC, ABAC, tenant scoping, and assignment-based access are essential. They do not, however, substitute for exceptional Guardian/PDR governance.

The following conditions are insufficient to authorize `user-data-operationalization` on their own:

- being a platform administrator;
- being an organization administrator;
- being a mentor;
- being a participant;
- being a support worker;
- being an auditor;
- being assigned to a participant, support case, program, or audit;
- belonging to the correct tenant;
- holding a database role;
- having access to an admissible view;
- having access to a raw governed table through an authorized governance function.

The exceptional Guardian path requires all of the following:

1. A caller token for an active registered Guardian caller.
2. A verified authority bundle.
3. Runtime admission.
4. A signed operation intent from an active subject key.
5. Caller and subject identity match.
6. Exact operation, scope, purpose, audience, validity-window, and revocation checks.
7. Constitutional and policy approval.
8. Policy Decision Receipt issuance.
9. One-time intent consumption to prevent replay.

As of August 17, 2026, this authority path is intentionally unprovisioned:

```json
{
  "active_callers": 0,
  "active_subject_keys": 0,
  "governed_operation_authorization": "unavailable_fail_closed"
}
```

Therefore, no ordinary application role, assignment, tenant relationship, or database role can currently complete a Guardian/PDR-governed operation.

This is intentional. Routine product access should remain functional through ordinary authorization while exceptional authority-bearing operations remain unavailable until separately, deliberately provisioned.

---

## 43.10 How Row-Level Security Fits In

### 43.10.1 Row-Level Security on gbim_record

Row-level security, or RLS, is enabled on `public.gbim_record`. The policy for `runtime_governance_role` is:

```text
USING (true)
```

This means:

- for this role, all rows are visible;
- other roles must follow different policies or have no access at all.

Row-level security ensures that even if a table is technically accessible, the role’s view can be filtered.

### 43.10.2 RLS, ABAC, and Tenant Scoping

RLS can serve as one enforcement layer for ordinary ABAC and tenant scoping.

For example, an RLS policy can require that a row’s tenant identifier match the authorized tenant context of the requesting role or session. Other policies can restrict access by:

- assignment relationship;
- data classification;
- consent status;
- workflow state;
- public-claim eligibility;
- organization membership.

The demonstrated `runtime_governance_role` policy is intentionally broad because that role must maintain lifecycle and admissibility over all governed records. It is not a model for ordinary application-user access.

### 43.10.3 Why RLS Matters Here

RLS provides fine-grained control over which roles can see which rows.

In this architecture:

- `runtime_governance_role` sees all rows in `gbim_record` because it must manage lifecycle and admissibility.
- `public_instrument_role` does not see `gbim_record` directly; it relies on admissible views instead.
- future application roles should be constrained by their tenant, assignment, purpose, consent, and data-classification attributes.
- Guardian/PDR authorization remains a separate authority system, not an RLS policy result.

This prevents public or ordinary application access from bypassing governance rules by querying internal tables directly.

---

## 43.11 Overflow and Person-Space in Context of Roles

Overflow enforcement and person-space promotion are meaningful only when viewed through access-control boundaries.

### 43.11.1 Person-Space Promotion

Person-space promotion — moving a cognition packet into a committed person-space event — is managed by governance scripts and functions that run as `runtime_governance_role`.

This role:

- evaluates readiness and validation;
- ensures person-space events are constructed properly;
- logs decisions for later review;
- applies applicable consent, minimization, and governance checks.

It does not expose raw person-space events directly to the public. Instead, it prepares minimized events and passes them into controlled lanes.

Future application access to person-space material should follow ordinary RBAC, ABAC, tenant scoping, and assignment rules. For example, a mentor should not see person-space information merely by being a mentor; the mentor must also be appropriately assigned, tenant-scoped, and permitted by consent and data classification.

### 43.11.2 Overflow Enforcement

Overflow enforcement — sending events to queues such as:

```text
overflow:queue:overflow_retriable_public_context
```

is also carried out under governance roles and functions.

The overflow path:

- checks person-space validation;
- minimizes event payloads to public-context fields;
- enqueues events into bounded queues;
- limits what public-facing surfaces may retrieve.

From the public instrument’s perspective, overflow is visible only through high-level functions, APIs, admissible views, and audit logs. The public instrument does not directly manipulate overflow queues at the raw-record level.

Ordinary role assignment does not change that. A support worker, mentor, or organization administrator should access only the overflow context necessary for their authorized and assigned workflow, and only within the relevant tenant.

### 43.11.3 Overflow Is Not Guardian Authority

Overflow handling, person-space validation, and ordinary promotion logic are not Guardian/PDR authorization by themselves.

They may be necessary safeguards for a route, but they do not create:

- an active Guardian caller;
- a subject signing key;
- a valid operation intent;
- a Policy Decision Receipt;
- authority to perform `user-data-operationalization`.

---

## 43.12 Why Role-Gated Access Is Necessary

Role-gated knowledge access is necessary for:

- **Privacy** — preventing raw person-space and governed records from being visible to public tools or unrelated tenants.
- **Governance** — ensuring lifecycle decisions are made by the correct internal role.
- **Security** — limiting the blast radius of mistakes, compromised accounts, and configuration errors.
- **Community accountability** — making visible who may access what, for what purpose, and within which organization.
- **Separation of powers** — preventing ordinary access roles from quietly becoming exceptional authority roles.

Without these controls:

- any part of the system could query `gbim_record` directly;
- admissibility rules could be bypassed;
- overflow and person-space handling could become leaky;
- a role in one tenant could become access to another;
- a normal administrator role could be mistaken for constitutional authority.

For rural developers, role-gated access is the difference between a system where everything is readable by anyone who finds a connection string and a system where responsibilities, tenant boundaries, assignments, and exceptional authority are divided and enforced.

---

## 43.13 Implementation Status

**Role-Gated Knowledge Access: Demonstrated.**

As of August 17, 2026:

- The three-tier database role model is in place:
  - `postgres` superuser for maintenance;
  - `runtime_governance_role` with full `gbim_record` access and row-level policy `USING (true)`;
  - `public_instrument_role` with read-only access to `public_admissible_gbim_mv` and `runtime_governance.public_answer_audit`.
- Attempts by `public_instrument_role` to read `public.gbim_record` result in permission errors, confirming the non-surveillance boundary.
- Governance functions and overflow scripts run under appropriate roles, enforcing promotion, validation, and minimization.
- Ordinary application authorization is conceptually separated into RBAC, ABAC, tenant scoping, and assignment-based access.
- Standard future roles — administrator, organization administrator, mentor, participant, support, and auditor — are application roles, not Guardian authority-bundle identities.
- The Guardian-governed `user-data-operationalization` path is explicitly unavailable and fail closed because there are zero active callers and zero active subject keys.

Within the academic scope of this chapter, the architecture’s claims about role-gated knowledge access are supported by concrete role definitions, observed public-reader isolation, and an explicit separation between ordinary authorization and exceptional Guardian/PDR authority.

---

## 43.14 Step-by-Step Summary for Rural Developers

To use or reason about role-gated access:

1. **Separate ordinary access from exceptional authority.**  
   RBAC, ABAC, tenant scoping, and assignment relationships govern routine application access. Guardian/PDR governs only a narrow exceptional operation.

2. **Know the three database roles.**  
   `postgres`, `runtime_governance_role`, and `public_instrument_role` each have a distinct database function.

3. **Understand what each role can do.**  
   Superuser can maintain the database; runtime governance can manage internal state; public instrument can see only admissible evidence and approved audit logs.

4. **Apply tenant and assignment limits.**  
   A valid application role should be limited to the relevant organization, relationship, purpose, consent scope, and data classification.

5. **Remember row-level security.**  
   RLS policies can enforce row-level boundaries, but they do not replace application authorization or Guardian/PDR governance.

6. **Connect roles to overflow and person-space.**  
   Governance roles handle promotion and overflow. Ordinary application roles access only the minimized, tenant-scoped, assigned, and authorized results.

7. **Use denials as guides.**  
   A permission error, tenant mismatch, missing assignment, consent failure, or Guardian authorization denial is often evidence that a boundary is doing its job.

8. **Do not confuse standard roles with Guardian identities.**  
   Administrator, organization administrator, mentor, participant, support, auditor, and database roles do not automatically grant Guardian caller credentials, subject keys, signed intent authority, or PDR issuance.

9. **Stay within scope.**  
   This chapter documents the demonstrated database three-tier model and the architecture’s access-control distinctions. It does not claim every future application permission matrix has already been provisioned.

---

## 43.15 Closing

Role-gated knowledge access is the backbone of Ms. Jarvis’s privacy and governance story. By defining what `postgres`, `runtime_governance_role`, and `public_instrument_role` can and cannot do, the system keeps sensitive state behind appropriate database gates and exposes only governed, admissible evidence to public tools.

Ordinary application access should be governed through RBAC, ABAC, tenant scoping, and assignment-based relationships. Those controls make it possible for participants, mentors, support workers, auditors, organization administrators, and platform administrators to perform legitimate work without broad or cross-tenant access.

Exceptional Guardian/PDR-governed operations remain separate. They require a specific caller, a verified authority bundle, runtime admission, a signed subject intent, caller-subject matching, constitutional approval, a Policy Decision Receipt, and one-time intent consumption. As of August 17, 2026, that exceptional authority path is intentionally unavailable and fail closed.

For rural developers, this chapter provides the map: who has the keys to which rooms, what each room
