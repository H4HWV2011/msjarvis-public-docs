# 36. Identity and Registration

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: August 17, 2026*

---

## 36.1 Why Identity and Registration Are Separate

In Ms. Allis, **identity** is not just “who you are” in one large bucket. It is separated into:

- what is known **for this session right now**;
- what is allowed to **persist as registered identity**;
- what is allowed to be **seen publicly**;
- what authority, if any, an application role has within a specific organization or tenant;
- what narrow, exceptional authority is recognized by the Constitutional Guardian.

These are different questions and must not be treated as interchangeable.

This chapter explains a **bounded, consent-gated registration module**: what it requires, where it writes, and how review blocks registrations without proper consent. It also clarifies that future standard roles — administrator, organization administrator, mentor, participant, support, and auditor — belong to the application’s authorization and tenant-scoping layer. They do not belong in the Constitutional Guardian’s authority bundle.

This chapter does **not** claim biometric production readiness, legal identity proof, institutional endorsement, universal fraud prevention, clinical guarantees, or activation of Guardian-governed data operationalization.

---

## 36.2 Identity, Authorization, and Authority

Ms. Allis distinguishes three related but separate concepts.

| Concept | Question answered | Typical example | Primary control |
|---|---|---|---|
| Identity | Who is interacting with the system? | A registered participant or a session visitor | Registration, session handling, consent records |
| Application authorization | What may this person do within a tenant or application context? | A mentor may view assigned participant work; an organization administrator may manage their organization | Role-based authorization and tenant scoping |
| Guardian authority | May a specially governed operation gain high-assurance constitutional authority? | `user-data-operationalization` with caller authentication, signed intent, and PDR issuance | Constitutional Guardian authority bundle |

A person may have a valid application identity and a valid application role without having any Guardian authority.

For example:

- A **participant** may access their own account and approved services.
- A **mentor** may review work from participants assigned within the same organization.
- A **support** worker may assist with approved troubleshooting workflows.
- An **auditor** may inspect authorized audit surfaces.
- An **organization administrator** may manage members, settings, and permissions inside their own tenant.
- A platform **administrator** may perform platform operations under separately controlled administrative procedures.

None of those application roles automatically creates a Guardian caller credential, a Guardian subject key, a signed operation intent, or the right to receive a Policy Decision Receipt.

---

## 36.3 Ephemeral Session Identity

Every interaction with Ms. Allis runs inside a **session**.

During a session, the system may keep:

- a session ID;
- temporary preferences, such as “talk slower” or “use code examples”;
- current tasks and partial answers;
- short-term context about the person speaking;
- the tenant or organization context in which the session is taking place, when applicable.

This is called **ephemeral session identity**:

- it lives in the sandbox or other short-lived session layers;
- it exists to keep the conversation coherent;
- it is **not** automatically written into a long-term identity record;
- it is not, by itself, evidence of a durable application role;
- it is not Guardian authority.

For rural users, think of this as “what the system remembers **for this visit only**,” unless a later governed step permits durable registration.

---

## 36.4 What Counts as Registration

**Registration** is the step where some part of what is known about a person becomes **durable, governed identity state**.

The as-built registration module requires, at minimum:

- **user identity** — enough information to distinguish one person from another inside the system;
- **session identity** — the session that produced the information being registered;
- an **approved artifact** — material that has already passed relevant internal checks, such as verified contact information or a KYC result;
- a **permitted application actor role** — the actor requesting registration must be allowed to perform that application workflow;
- a **valid registration layer** — the internal layer or bucket in which identity information will be placed;
- a **KYC-vault target** — where regulated or sensitive identity material is stored, when required;
- **retention consent** — explicit agreement about storing the material;
- a **tenant or organization scope**, when registration occurs inside a multi-organization application context.

If any required element is missing or invalid, registration should not succeed.

A permitted application actor role means permission within the registration workflow. It does not mean that the actor is entered into the Guardian authority bundle.

---

## 36.5 Application Roles and Tenant Scoping

The following are standard future application roles:

- **Administrator**
- **Organization administrator**
- **Mentor**
- **Participant**
- **Support**
- **Auditor**

These roles belong to the application authorization model. They should be assigned, evaluated, and limited through role-based access control and tenant scoping.

### Role-based authorization

Application authorization determines whether a person may perform a function within the product, such as:

- creating or managing an organization;
- inviting or managing organization members;
- participating in an approved program or service;
- mentoring assigned participants;
- providing support through approved support workflows;
- reviewing authorized audit records;
- administering platform configuration under administrative controls.

The exact permissions for each role should be explicit, least-privilege, and auditable. A role name alone should not grant broad access.

### Tenant scoping

Tenant scoping determines **where** an application role applies.

For example:

- An organization administrator for Organization A should not automatically administer Organization B.
- A mentor assigned to one organization should not automatically see participants from another organization.
- A support role should access only the cases, records, and organizations necessary for the approved support task.
- An auditor should see only audit surfaces within the audit scope they are authorized to inspect.
- A platform administrator should use separately controlled platform-wide administrative access rather than inheriting unrestricted tenant access by default.

Tenant boundaries prevent a valid role in one organization from becoming a general passport into unrelated organizations, communities, or records.

### Application roles are not Guardian identities

Standard roles are not placed in the Guardian authority bundle merely because they are important application roles.

They do not automatically receive:

- Guardian caller tokens;
- Guardian caller entries;
- active Guardian subject keys;
- authority to sign operation intents;
- authority to request or obtain Policy Decision Receipts;
- authority to perform `user-data-operationalization`.

Application roles answer “what may this user do in this tenant?” Guardian authority answers the much narrower question “may this explicitly governed operation receive high-assurance constitutional authorization?”

Those controls must remain separate.

---

## 36.6 KYC Vault and Registration Layers

When registration succeeds, identity data does **not** simply land in one general-purpose database.

Two important destinations are:

- a **KYC vault** — a highly protected store for sensitive identity material, such as documents used to verify identity;
- one or more **registration layers** — internal structures that track:
  - that the person is registered;
  - which tenant or service may see which parts of the identity;
  - what application roles may use the identity data;
  - what retention rules apply;
  - what disclosure rules apply.

Registration-layer metadata travels alongside the data itself, indicating:

- whether the record is KYC-linked or non-KYC;
- which tenant, subspace, or service may read it;
- which application authorization scope applies;
- what retention and disclosure rules apply;
- whether a public representation is permitted.

This makes fine-grained identity governance possible. It is not a single universal yes-or-no identity flag.

---

## 36.7 Public Disclosure as a Separate Step

Public disclosure is **not** automatic after registration.

The system treats **public exposure** as a separate transition that requires:

- explicit `public_opt_in` from the user or an equivalent applicable policy decision;
- a separate path that writes to public-facing indices or records;
- review to make sure public exposure is appropriate and allowed;
- application authorization and tenant rules that identify who may initiate or review the disclosure workflow.

There are at least two different moves:

1. **Register** — store identity in internal, governed layers, possibly with KYC.
2. **Disclose publicly** — publish some portion of that identity, such as a public profile, only with explicit `public_opt_in`.

A valid application role does not eliminate the need for public opt-in. For example, an organization administrator may be authorized to manage organization membership, but that does not permit publishing a participant’s identity without the participant’s applicable consent and disclosure conditions.

This protects rural users from discovering that something they agreed to store privately has quietly become public.

---

## 36.8 Suppression of Surveillance-Shaped Metadata

The registration module is required to **suppress surveillance-shaped metadata**.

Examples of metadata that should be suppressed or excluded from ordinary registration include:

- unnecessary cross-site activity trails;
- detailed location histories not required for the service;
- fine-grained behavioral fingerprints;
- extra data collected “just in case”;
- unnecessary tenant-crossing identifiers;
- broad role or organization histories that are unrelated to the requested service.

Instead:

- only identity information needed for the stated purpose is kept;
- tenant membership and role data are scoped to the relevant organization or application boundary;
- other metadata is dropped, heavily redacted, or held under stricter separate rules;
- access to identity material is based on purpose, role, consent, and tenant scope rather than maximum data collection.

For operators, this means registration is shaped around **consent, necessity, and bounded access**, not maximum tracking.

---

## 36.9 Registration Metadata in Hilbert and Chroma

When a registration write happens, the system keeps a **metadata trace** in its state and memory layers, including Hilbert and Chroma.

This metadata includes:

- which registration layer was used;
- the relevant tenant or organization scope, when applicable;
- which application authorization path permitted the registration workflow;
- whether `public_opt_in` was present at the time;
- the KYC-vault target involved, if any;
- retention and consent flags;
- provenance needed to reconstruct why the registration occurred.

Importantly, this metadata is **source-visible** in the write path. That means:

- developers and auditors can see how and why a registration happened;
- it is possible to reconstruct which consent and authorization conditions were present;
- later checks can confirm whether retention, tenant access, and disclosure match the original terms;
- audit can distinguish application authorization from Guardian authority.

This is part of making identity registration auditable rather than opaque.

Metadata traces must not be mistaken for permission to expose the underlying identity material broadly. Audit visibility should itself remain tenant-scoped and authorization-controlled.

---

## 36.10 Guardian Review and Fail-Closed Behavior

Before a registration is finalized, the system applies the relevant governance review.

Registration review checks for conditions such as:

- missing retention consent;
- an invalid or disallowed registration layer;
- attempts to write sensitive identity data without targeting the proper KYC vault;
- requests to mark material public without `public_opt_in`;
- a role attempting an action outside its application authorization;
- a request attempting to cross tenant boundaries without explicit authorization;
- missing provenance, consent, or required workflow context.

If any of these checks fail, the system **fails closed**:

- registration is blocked;
- no partial identity record is silently written;
- the failure is logged so an operator can inspect what went wrong;
- no application role is silently escalated into Guardian authority.

### Guardian distinction

The Constitutional Guardian’s high-assurance authority bundle is not the normal role-management system for registration, mentorship, support, auditing, or organization administration.

Guardian authority is reserved for the narrow protected operation:

```text
user-data-operationalization
```

That operation requires a separate authorization sequence:

- caller token;
- verified authority bundle;
- runtime admission;
- signed operation intent;
- caller-subject match;
- policy approval;
- Policy Decision Receipt issuance;
- one-time intent consumption.

As of August 17, 2026, the Guardian authority bundle intentionally contains no active callers and no active subject keys. Therefore:

```text
governed operation authorization unavailable fail closed
```

This does not mean standard application roles are unavailable. It means that application authorization must not be confused with the exceptional Guardian authority path.

---

## 36.11 Consent-Gated Identity Registration

For rural developers, a typical consent-gated registration flow looks like this:

1. A user completes an interaction where an identity-relevant artifact is produced, such as “create me an account.”
2. The system gathers required fields: user identity, session identity, approved artifact, application actor role, tenant scope, registration layer, KYC target if any, and explicit retention consent.
3. The identity-registration promotion module checks that required elements are present and that the actor is authorized for the requested action within the relevant tenant.
4. The registration payload passes through the applicable governance review.
5. If review passes, the system writes:
   - sensitive identity material into the KYC vault when required;
   - registration metadata into Hilbert and Chroma;
   - tenant-scoped identity and role associations into the appropriate application authorization layer.
6. If the user also gave `public_opt_in`, a separate disclosure workflow may populate public representation under its own disclosure rules.
7. If any required check fails, nothing is registered and the system records a fail-closed event.

This flow makes “what is stored where, why, who may access it, and which tenant it belongs to” visible and inspectable.

---

## 36.12 Example: Mentor and Participant

Consider a future mentoring program operated by one organization.

- A **participant** registers with retention consent and is associated with that organization’s tenant.
- A **mentor** is assigned through the application authorization system to support that participant or an approved cohort.
- The mentor can see only information that is necessary for the approved mentorship function and allowed by tenant rules, consent, and data classification.
- An **organization administrator** can manage the organization’s membership and approved program settings but cannot automatically publish participant records.
- A **support** worker can assist with an approved support case but does not gain broad access to all participant records.
- An **auditor** can inspect approved audit surfaces within the audit scope but does not become a Guardian authority holder.
- A platform **administrator** may maintain platform operations under separately controlled administrative procedures but does not automatically receive the authority to operationalize user data through Guardian.

If any workflow would require the separate protected `user-data-operationalization` operation, it cannot proceed merely because one of these people holds an application role. It remains unavailable unless the Guardian’s separate authority system is deliberately provisioned and the full authorization chain succeeds.

---

## 36.13 What This Chapter Does Not Claim

Within this gate, Chapter 36 does **not** claim:

- biometric production readiness;
- that it can legally prove identity;
- endorsement from banks, governments, or institutions;
- universal fraud prevention;
- clinical or safety guarantees about how identity data will be used by others;
- that an administrator, organization administrator, mentor, participant, support worker, or auditor automatically holds Guardian authority;
- that application roles can bypass consent, disclosure controls, KYC-vault requirements, or tenant boundaries;
- that the Guardian-governed `user-data-operationalization` path is active.

It claims:

- a bounded, consent-gated registration module;
- clear separation between registration and public disclosure;
- KYC-vault targeting where needed;
- suppression of surveillance-shaped metadata;
- application authorization and tenant scoping for standard future roles;
- separation between ordinary application roles and Guardian authority;
- fail-closed handling of missing consent, invalid scope, invalid registration layer, and unauthorized cross-tenant registration conditions;
- an intentionally unprovisioned Guardian authority state for governed data operationalization.

---

## 36.14 Closing Statement

Identity and registration in Ms. Allis are treated as **governed transitions**, not a one-time label. Ephemeral session identity supports live conversations, while a separate consent-gated module controls which parts become durable registered identity and, only with explicit `public_opt_in`, which parts become public.

Standard future roles — administrator, organization administrator, mentor, participant, support, and auditor — belong to application authorization and tenant-scoping systems. They define what an authenticated person may do within a bounded product and organizational context. They are not Guardian authority-bundle identities and do not independently authorize high-assurance governed data operationalization.

By combining KYC vaults, registration layers, tenant-scoped application authorization, Hilbert and Chroma metadata, surveillance-metadata suppression, and fail-closed review, Chapter 36 establishes identity registration as a careful, auditable process that rural communities can understand and inspect rather than a hidden, all-or-nothing data grab.

---

*Chapter 36 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*  
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*  
*See LICENSE for terms.*
