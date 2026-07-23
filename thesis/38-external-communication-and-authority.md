# 38. External Communication and Authority

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 22, 2026*

---

## 38.1 Why External Communication Is Governed

In Ms. Allis, sending anything **outside** the system is treated as an **authority-bearing act**, not just “printing a message.”

External communication can:

- expose private information;  
- look like an official promise or commitment;  
- affect how public partners and neighbors understand the system;  
- create obligations that last beyond a single session.

Because of this, every external send is wrapped in a **governed contract** and recorded in an **audit corpus** instead of being a free‑form print statement.

---

## 38.2 External Authority Audit Records

External communication authority is tracked in a Chroma collection called:

- **`external_authority_audit_records`**

From the July 2026 gate:

- the collection exists, is healthy, and remains at a stable family count;  
- records like `extauth_c57f9…` and `extauth_0ecf…` are stored there;  
- these records are **durable and queryable**, so operators can see:  
  - what was sent (or proposed);  
  - to whom;  
  - under what consent and authority;  
  - with what verdict (PERMIT / REVIEW / BLOCK).

This turns external authority into something you can **inspect**, not just trust.

---

## 38.3 The Projection Contract

Every external communication candidate is represented as a **projection** with fields such as:

- `actor_role` – who is acting (system, public_steward, municipal_partner, governance_operator).  
- `channel` – which lane (public_report, governance_notice, research_correspondence, human_review_packet).  
- `recipient_class` – public, municipal_partner, research_partner, internal_review.  
- `content_class` – public_civic, person_linked_context, private_user_memory.  
- `contains_private_identity` – whether personal identity is involved.  
- `binding_commitment_requested` – whether the message tries to make a binding promise.  
- `external_send_requested` – whether an actual send out of the system is requested.  
- `public_opt_in` – whether the user or source has opted in to public disclosure.  
- `retention_consent` – whether consent for retention has been given.  
- `human_approved` – whether a human has already signed off.  
- `legal_authority_present` – whether a real legal basis is present.  
- `purpose` – public_information, governance_review, research_review, human_escalation.  
- `provenance_hash` and `source_id` – link back to where the content came from.

These fields let the system **reason about authority and consent** before sending anything out.

---

## 38.4 Example Cases from the Gate

The July 2026 probe shows several concrete examples.

### 38.4.1 Public civic report (PERMIT)

Projection `public_report`:

- `actor_role`: `public_steward`  
- `channel`: `public_report`  
- `recipient_class`: `public`  
- `content_class`: `public_civic`  
- `contains_private_identity`: `false`  
- `public_opt_in`: `true`  
- `external_send_requested`: `true`  
- `human_approved`: `true`  
- `legal_authority_present`: `false` (not needed for simple public info)  
- `purpose`: `public_information`  

Verdict:

- `verdict`: `PERMIT`  
- `reason`: `bounded_external_communication_authorized`  
- `collection`: `external_authority_audit_records`  
- `record_id`: `extauth_c57f9…`

Meaning: a **non‑private, public report** with human approval and public opt‑in is allowed and logged.

### 38.4.2 Binding commitment (REVIEW)

Projection `binding`:

- `actor_role`: `municipal_partner`  
- `binding_commitment_requested`: `true`  
- `channel`: `governance_notice`  
- `legal_authority_present`: `true`  
- `external_send_requested`: `true`  
- `human_approved`: `false`  

Verdict:

- `verdict`: `REVIEW`  
- `reason`: `binding_commitment_requires_human_authority`  
- `collection`: `null` (no write yet)  

Meaning: **binding legal‑style commitments** never go out automatically; they always require **human authority** before any send or record is finalized.

### 38.4.3 Private person‑linked review (REVIEW)

Projection `private_needs_review`:

- `contains_private_identity`: `true`  
- `content_class`: `person_linked_context`  
- `recipient_class`: `research_partner`  
- `external_send_requested`: `true`  
- `retention_consent`: `true`  
- `public_opt_in`: `true`  
- `human_approved`: `false`  

Verdict:

- `verdict`: `REVIEW`  
- `reason`: `private_external_disclosure_requires_human_review`  
- `collection`: `null`

Meaning: even with consents set, **person‑linked private context** sent to research partners still requires **human review** before sending.

### 38.4.4 Private, no consent (BLOCK)

Projection `private_no_consent`:

- `contains_private_identity`: `true`  
- `content_class`: `private_user_memory`  
- `retention_consent`: `false`  
- `external_send_requested`: `true`  

Verdict:

- `verdict`: `BLOCK`  
- `reason`: `private_content_requires_retention_consent`

Meaning: if there is **no retention consent**, private user memory is **blocked** from external send, full stop.

### 38.4.5 Raw secret (BLOCK)

Projection `raw_secret`:

- `content_class`: `public_civic` (but tagged with secret metadata)  
- `external_send_requested`: `true`  
- `public_opt_in`: `true`  
- `human_approved`: `true`  

Verdict:

- `verdict`: `BLOCK`  
- `reason`: `forbidden_metadata:secret`

Meaning: anything flagged as containing **secrets, credentials, biometrics, or financial data** fails closed, even if someone tried to approve it.

### 38.4.6 Internal review packet (PERMIT, no external send)

Projection `review_packet`:

- `channel`: `human_review_packet`  
- `recipient_class`: `internal_review`  
- `contains_private_identity`: `true`  
- `external_send_requested`: `false`  
- `retention_consent`: `true`  
- `purpose`: `human_escalation`  

Verdict:

- `verdict`: `PERMIT`  
- `reason`: `bounded_external_communication_authorized`  
- `collection`: `external_authority_audit_records`  
- `record_id`: `extauth_0ecf…`

Meaning: **internal escalation packets** (for human review inside the system) can be recorded as audit entries **without** any external send.

---

## 38.5 Fail-Closed Disclosure Controls

From the closed evidence:

- **Secret, credential, biometric, financial, and binding‑action metadata fail closed.**  
- Missing or invalid consent causes **BLOCK** or **REVIEW**, not “best effort send.”  
- Internal review packets can be recorded but are **not sent outside**.  
- All permitted sends are written to `external_authority_audit_records` for later inspection.

This means the system prefers **no send** over a risky or unclear send.

---

## 38.6 Relationship to Consent and Legal Authority

The system combines:

- **Consent fields** – `public_opt_in`, `retention_consent`.  
- **Legal authority** – `legal_authority_present` for cases where law or contract may permit certain disclosures.  
- **Human approval** – `human_approved` to mark that a person has checked the projection.

Rules from the gate:

- Public civic information with **public opt‑in** and **human approval** can be permitted.  
- Binding commitments must go to **REVIEW** even when legal authority exists.  
- Private person‑linked disclosures need both **retention consent** and, usually, **human review** before any send.  
- Lack of consent or presence of forbidden metadata leads to **BLOCK**.

---

## 38.7 No Autonomous External Sending or Binding Authority

Within this chapter’s scope, the system **does not**:

- autonomously send messages outside without passing through this contract and verdict logic;  
- hold **binding legal authority** on its own;  
- send out unconsented private data;  
- send credentials, secrets, or financial instructions;  
- guarantee perfect safety for all external communications.

It **only** claims:

- bounded audit records;  
- projection‑based consent and legal‑authority checks;  
- human‑review routing;  
- fail‑closed handling for risky or forbidden content.

---

## 38.8 Step-by-Step View for Rural Developers

On a running system, external communication works roughly like this:

1. The system (or an operator) wants to send something out.  
2. A **projection** is built describing actor, channel, recipient, privacy, consent, and purpose.  
3. The projection is run through the **external authority gate**, which issues a verdict: PERMIT, REVIEW, or BLOCK.  
4. If PERMIT and the channel is external, the message may be sent and an **audit record** stored in `external_authority_audit_records`.  
5. If REVIEW, the projection waits for a **human** to inspect and decide.  
6. If BLOCK, the system does **not** send, and the reason is logged.

This lets you see, with your own tools, how and why a given external message was allowed, delayed, or blocked.

---

## 38.9 Closing Statement

Chapter 38 fixes **external communication and authority** as a governed, auditable process. Every outgoing message is evaluated via a structured projection that accounts for actor role, channel, recipient, privacy, consent, legal authority, and human approval, with results recorded in `external_authority_audit_records`.

By routing binding commitments and private disclosures to **human review**, blocking secrets and unconsented data, and treating permitted messages as logged audit events, the system keeps external communication **bounded, inspectable, and answerable to rural communities**, instead of letting it become an uncontrolled side effect of internal reasoning.
