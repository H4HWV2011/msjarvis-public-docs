# 36. Identity and Registration

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 22, 2026*

---

## 36.1 Why Identity and Registration Are Separate

In Ms. Allis, **identity** is not just “who you are” in one big bucket. It is split into:

- what is known **for this session right now**;  
- what is allowed to **persist as registered identity**;  
- what, if anything, is allowed to be **seen publicly**.

This chapter explains how a **bounded, consent‑gated registration module** works: what it requires, where it writes, and how guardian review blocks registrations that do not have proper consent. It does **not** claim biometric production readiness, legal identity proof, institutional endorsement, universal fraud prevention, or clinical guarantees.

---

## 36.2 Ephemeral Session Identity

Every interaction with Ms. Allis runs inside a **session**.

During a session, the system may keep:

- a session ID;  
- temporary preferences (for example, “talk slower,” “use code examples”);  
- current tasks and partial answers;  
- short‑term context about the person speaking.

This is called **ephemeral session identity**:

- it lives in the sandbox;  
- it exists to keep the conversation coherent;  
- it is **not** automatically written into any long‑term identity record.

For rural users, you can think of this as “what the system remembers **for this visit only**,” unless a later, governed step says otherwise.

---

## 36.3 What Counts as Registration

**Registration** is the step where some part of what is known about a person becomes **durable, governed identity state**.

The as‑built registration module requires, at minimum:

- **user identity** – enough information to tell one person from another inside the system;  
- **session identity** – which session produced the information being registered;  
- an **approved artifact** – something that has already passed internal checks (for example, verified contact info or a KYC result);  
- a **permitted actor role** – the actor asking to register must be allowed to do so;  
- a **valid registration layer** – which internal “bucket” the identity data will go into;  
- a **KYC‑vault target** – where regulated identity material is stored;  
- **retention consent** – explicit agreement about storing the material.

If any of these are missing or invalid, the registration should not succeed.

---

## 36.4 KYC Vault and Registration Layers

When registration succeeds, identity data does **not** just land in one place.

Two important destinations are:

- a **KYC vault** – a highly protected store for sensitive identity material (for example, documents used to verify who someone is);  
- one or more **registration layers** – internal structures that track:  
  - that the person is registered;  
  - which services may see which parts of that identity;  
  - what retention rules apply.

Registration‑layer metadata travels alongside the data itself, indicating:

- “this is KYC‑linked” or “this is non‑KYC”;  
- which subspace or service may read it;  
- what kind of retention and disclosure rules apply.

This makes it possible to have **fine‑grained identity governance**, not just a yes/no flag.

---

## 36.5 Public Disclosure as a Separate Step

Public disclosure is **not** automatic after registration.

The system treats **public exposure** as its own transition that requires:

- explicit **`public_opt_in`** from the user (or equivalent policy decision);  
- a separate path that writes to **public‑facing indices or records**;  
- guardian checks to make sure public exposure is appropriate and allowed.

So there are at least two different moves:

1. **Register** – store identity in internal, governed layers (possibly with KYC).  
2. **Disclose publicly** – publish some of that identity (for example, a public profile), but **only** with explicit `public_opt_in`.

This protects rural users from discovering that something they agreed to store privately has quietly become public.

---

## 36.6 Suppression of Surveillance-Shaped Metadata

The registration module is required to **suppress surveillance‑shaped metadata**.

Examples of what is suppressed or excluded from normal registration:

- unnecessary cross‑site activity trails;  
- detailed location histories not needed for the service;  
- fine‑grained behavioral fingerprints;  
- extra data collected “just in case.”

Instead:

- only the identity information needed for the stated purpose is kept;  
- other metadata is either dropped, heavily redacted, or held under stricter, separate rules.

For you as an operator, this means registration is deliberately shaped **around consent and necessity**, not around maximum tracking.

---

## 36.7 Registration Metadata in Hilbert and Chroma

When a registration write happens, the system keeps a **metadata trace** in its state and memory layers (Hilbert and Chroma).

This metadata includes:

- which **registration layer** was used;  
- whether **`public_opt_in`** was present at the time;  
- the **KYC‑vault target** involved (if any);  
- retention and consent flags.

Importantly, this metadata is **source‑visible** in the write path, meaning:

- developers and auditors can see **how** and **why** a registration happened;  
- it is possible to reconstruct which consents were in place when identity data was stored;  
- later checks can confirm whether exposure and retention match the original terms.

This is part of making identity registration **auditable**, not opaque.

---

## 36.8 Guardian Review and Fail-Closed Behavior

Before a registration is finalized, the **guardian** layer reviews the registration payload.

Guardian review checks for things like:

- missing **retention consent**;  
- an invalid or disallowed **registration layer**;  
- attempts to write sensitive identity data without targeting the proper **KYC vault**;  
- requests to mark something public without `public_opt_in`.

If any of these checks fail, the system **fails closed**:

- the registration is blocked;  
- no partial identity record is silently written;  
- the failure is logged, so an operator can see what went wrong.

This prevents “accidental” identity registration without consent.

---

## 36.9 Consent-Gated Identity Registration (Step-by-Step)

For rural developers, a typical, consent‑gated registration flow looks like this:

1. A user completes an interaction where some identity‑relevant artifact is produced (for example, “create me an account”).  
2. The system gathers required fields: user ID, session ID, artifact, actor role, registration layer, KYC target (if any), and explicit **retention consent**.  
3. The **identity‑registration promotion module** checks that all required pieces are present.  
4. The full registration payload is sent through **guardian review**.  
5. If guardian review passes, the system writes:  
   - sensitive identity material into the **KYC vault**;  
   - registration metadata into **Hilbert/Chroma**.  
6. If the user also gave `public_opt_in`, a **separate** write populates public representation, under its own rules.  
7. If any check fails, nothing is registered and the system logs a **fail‑closed** event.

This flow makes “what is stored where, and why” visible and inspectable.

---

## 36.10 What the Chapter Does Not Claim

Within this gate, Chapter 36 **does not** claim:

- biometric production readiness;  
- that it can legally prove identity;  
- endorsement from banks, governments, or institutions;  
- universal fraud prevention;  
- clinical or safety guarantees about how identity data will be used by others.

It only claims:

- a **bounded, consent‑gated registration module**;  
- clear separation between registration and public disclosure;  
- KYC‑vault targeting where needed;  
- suppression of surveillance‑shaped metadata;  
- guardian‑enforced, fail‑closed handling of missing‑consent cases.

---

## 36.11 Closing Statement

Identity and registration in Ms. Allis are treated as **governed transitions**, not a one‑time label. Ephemeral session identity supports live conversations, while a separate, consent‑gated module controls which parts become durable registered identity and, only with explicit `public_opt_in`, which parts become public.

By combining KYC vaults, registration layers, Hilbert/Chroma metadata, surveillance‑metadata suppression, and guardian fail‑closed review, Chapter 36 fixes identity registration as a **careful, auditable process** that rural communities can understand and inspect, rather than a hidden, all‑or‑nothing data grab.
