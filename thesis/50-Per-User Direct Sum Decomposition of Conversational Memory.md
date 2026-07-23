# 50. Per-User Direct Sum Decomposition of Conversational Memory

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 22, 2026*

---

## 50.1 What This Chapter Is Allowed to Claim

Within this gate, Chapter 50 may be rewritten as an **as‑built direct‑sum memory chapter**.

It may claim that:

- conversational memory now uses an explicit **per‑user direct‑sum routing module**;  
- **history**, **private**, and **staged** collections are named and handled as **per‑user subspaces**;  
- **durable history/private admission requires retention consent**;  
- **role, request purpose, permitted‑use, and legal‑authority presence** are projected into routing evidence;  
- **surveillance‑shaped metadata is suppressed** before any durable admission;  
- live vector‑store writes prove **alpha and beta users land in disjoint collections** with **no cross‑user record leak**;  
- relevant safeguards (BBB, guardian, Hilbert‑state, Hilbert‑time, commons, and vector‑store health) are passing.

It must **not** claim:

- unconsented durable conversation retention;  
- a single unrestricted global/shared conversation memory as the authority path;  
- automatic publication of private conversation memory into commons;  
- clinical, legal, or universal safety guarantees.

---

## 50.2 Plain‑Language Purpose for Rural Developers

For rural operators, this chapter answers:

> “When Ms. Jarvis remembers past conversations, how does she keep each person’s memory separate, governed, and non‑surveillance‑shaped?”

This chapter explains, step by step:

- how conversational memory is now **split per user**;  
- how each user gets **three per‑user tiers** (history, private, staged);  
- how **consent** and **purpose** control durable memory;  
- how tests show **alpha and beta users** stay fully disjoint;  
- how **forbidden metadata** is suppressed before write.

It talks only about **what is actually implemented and probed**.

---

## 50.3 Per‑User Conversation Families

Conversational memory is now organized into **per‑user families of collections** instead of one shared conversation store.

For the two demo users in the probe:

- user `ch50_demo_alpha` has:

  - history: `conversation_history_user_ch50_demo_alpha`;  
  - private: `conversation_private_user_ch50_demo_alpha`;  
  - staged: `conversation_staged_user_ch50_demo_alpha`.

- user `ch50_demo_beta` has:

  - history: `conversation_history_user_ch50_demo_beta`;  
  - private: `conversation_private_user_ch50_demo_beta`;  
  - staged: `conversation_staged_user_ch50_demo_beta`.

The routing module:

- takes a **user slug** (for example, `ch50_demo_alpha`);  
- resolves it to the correct **history/private/staged** collection names;  
- writes and reads **only within that user’s family**.

This is the “direct‑sum” decomposition in practice: each user gets a separate trio of subspaces.

---

## 50.4 Three Tiers: History, Private, Staged

For each user, conversational memory is split into three tiers:

- **History tier**  
  - Durable, general conversational memory;  
  - Used for normal continuity and “remember this” behavior;  
  - Requires **retention consent** to admit a record.

- **Private tier**  
  - More sensitive or tightly scoped conversational memory;  
  - Also requires **retention consent**;  
  - Subject to additional metadata checks (forbidden fields suppressed).

- **Staged tier**  
  - Short‑lived or under‑review conversational state;  
  - Used as a “waiting room” before deciding whether something should become durable;  
  - Does **not** require retention consent to exist, because it is not yet durable.

The probe shows all three tiers for `ch50_demo_alpha`, and the history tiers for both alpha and beta.

---

## 50.5 Consent‑Gated Durable History

Durable history admission is **explicitly gated on retention consent**.

The history examples in the probe:

- for `ch50_demo_alpha`:

  - `tier`: `"history"`;  
  - `retention_consent`: `true`;  
  - `actor_role`: `"user"`;  
  - `request_purpose`: `"conversation"`;  
  - `permitted_use`: `"memory_retrieval"`;  
  - `public_opt_in`: `false`;  
  - `legal_authority_present`: `false`;  
  - `verdict`: `"PERMIT"`;  
  - `reason`: `"per_user_direct_sum_route_permitted"`;  
  - `collection`: `conversation_history_user_ch50_demo_alpha`.

- for `ch50_demo_beta`:

  - same structure, but with `user_slug: "ch50_demo_beta"` and its own history collection.

A **no‑consent** example shows the opposite:

- `tier`: `"history"`;  
- `retention_consent`: `false`;  
- `verdict`: `"SUPPRESS"`;  
- `reason`: `"retention_consent_required_for_durable_tier"`;  
- `collection`: `null`.

So:

- if `retention_consent == true`, the system can write to the user’s history collection;  
- if `retention_consent == false`, it **refuses** to create the durable history record.

For rural developers, this means **no durable history without consent**.

---

## 50.6 Staged Tier: Per‑User but Non‑Durable

The staged tier for `ch50_demo_alpha` demonstrates **per‑user staging**:

- `tier`: `"staged"`;  
- `retention_consent`: `false`;  
- `collection`: `conversation_staged_user_ch50_demo_alpha`;  
- `verdict`: `"PERMIT"`;  
- `reason`: `"per_user_direct_sum_route_permitted"`;  
- `actor_role`: `"user"`;  
- `request_purpose`: `"conversation"`;  
- `permitted_use`: `"memory_retrieval"`;  
- `public_opt_in`: `false`;  
- `legal_authority_present`: `false`.

The vector store shows:

- `conversation_staged_user_ch50_demo_alpha` has `count: 1` and the expected `record_id` present.

This shows that:

- per‑user staging works;  
- staging does not require consent because **it is not yet durable**;  
- the record still stays in the **per‑user staged collection**, not in a global pool.

Staged is how Ms. Jarvis **“holds something lightly”** before deciding whether to remember it.

---

## 50.7 Surveillance‑Shaped Metadata Suppression

The contract includes a **forbidden metadata** example:

- tier: `"private"`;  
- `user_slug`: `"ch50_demo_alpha"`;  
- `retention_consent`: `true`;  
- `verdict`: `"SUPPRESS"`;  
- `reason`: `"forbidden_metadata:face_embedding"`;  
- `collection`: `null`.

This shows that:

- even when consent is present and the tier is private, certain metadata (here, a face embedding) is **not allowed**;  
- the routing module sees this forbidden field and returns **SUPPRESS** instead of writing a record.

So the system:

- does not merely rely on consent;  
- also checks **field types** to avoid building biometric or surveillance‑shaped memories.

This is built into the **per‑user direct‑sum routing**, not bolted on afterward.

---

## 50.8 No Cross‑User Leak and No Shared Collection Use

The probe’s `disjoint` flag is `true`, and the vector‑store write results show:

- `conversation_history_user_ch50_demo_alpha` has:

  - `count`: 1;  
  - `record_id`: `convds_af4129…`;  
  - `record_present`: `true`.

- `conversation_history_user_ch50_demo_beta` has:

  - `count`: 1;  
  - `record_id`: `convds_ff2448…`;  
  - `record_present`: `true`.

The `cross_leak_beta_id_in_alpha_collection` list is empty.

Additionally:

- `shared_collection_used`: `false` for both alpha and beta;  
- `legacy_shared_collection_used`: `false` in the contract;  
- the probe notes that a legacy shared conversation collection **still exists** (`legacy_shared_conversation_history_visible: true`), but it is **not used** for new writes.

This proves:

- alpha writes land only in alpha collections;  
- beta writes land only in beta collections;  
- no record ID from beta is present in alpha history;  
- the old “one big shared conversation collection” is now **retired as an authority path**.

---

## 50.9 Role, Purpose, Permitted‑Use, Legal Authority

The routing evidence for each case carries:

- `actor_role`: `"user"`;  
- `request_purpose`: `"conversation"`;  
- `permitted_use`: `"memory_retrieval"`;  
- `public_opt_in`: `false`;  
- `legal_authority_present`: `false`.

This shows that:

- conversation memories are created under the **“memory_retrieval”** permitted‑use;  
- the declared **purpose** is `"conversation"`;  
- the actor is a **user**, not a system admin or external process;  
- no special legal authority is present;  
- **public_opt_in` is `false`, so these are not treated as public/commons material.

These fields are part of the **routing projection**, meaning:

- the direct‑sum module **sees and uses** them when deciding whether to write;  
- per‑user routing is tied directly to **role and purpose**, not just to a user ID.

---

## 50.10 Direct‑Sum Picture for Rural Developers

From a local operator’s point of view, the as‑built per‑user direct‑sum memory path looks like:

1. **Identify the user.**  
   - The system resolves a `user_slug` (for example, `ch50_demo_alpha`).

2. **Pick the tier.**  
   - The caller indicates whether this is `staged`, `history`, or `private`.

3. **Check consent and metadata.**  
   - For `history` and `private`, `retention_consent` must be `true`;  
   - forbidden fields (for example, face embeddings) cause suppression.

4. **Project role and purpose.**  
   - Role, request purpose, permitted‑use, and legal authority are included in the routing decision.

5. **Route to the per‑user family.**  
   - History: `conversation_history_user_<slug>`;  
   - Private: `conversation_private_user_<slug>`;  
   - Staged: `conversation_staged_user_<slug>`.

6. **Write or suppress.**  
   - If all gates pass, the system writes to the resolved collection;  
   - Otherwise, it returns `SUPPRESS` or `REVIEW` without writing.

No write goes to a **shared conversation collection**, and **no cross‑user leak** is allowed by design or by test.

---

## 50.11 What This Chapter Does Not Claim

To stay within the gate, this chapter does **not** claim:

- durable conversation memory without consent;  
- a single unrestricted, global conversation memory store as the authority;  
- automatic publication of private conversation memory into commons or public datasets;  
- clinical, legal, or universal safety guarantees.

It only claims:

- **bounded per‑user conversational subspaces**;  
- **consent‑gated durable history/private memory**;  
- **staged/private/history tier separation** at the per‑user level;  
- **live evidence** that alpha and beta users write into disjoint collections with no cross‑leak, and that legacy shared history is no longer used for new writes.

---

## 50.12 Closing Statement

Per‑user direct‑sum decomposition is now an **as‑built feature** of conversational memory.

Each user has their own history, private, and staged conversation collections. Durable tiers require retention consent; staged tiers provide a non‑durable buffer; forbidden surveillance‑shaped metadata is suppressed; and live tests show that user alpha’s records never appear in user beta’s space or in a shared history collection. In this way, the formal idea of a per‑user direct sum becomes a concrete routing and storage behavior that rural developers can inspect, reason about, and rely on within the limits this gate defines.
