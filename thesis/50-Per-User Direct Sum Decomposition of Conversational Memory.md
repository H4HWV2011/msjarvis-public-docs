# 50 — Per-User Direct Sum Decomposition of Conversational Memory

*Carrie Kidd (Mamma Kidd) — Mount Hope, West Virginia*
*Last Updated: July 29, 2026*
*Status: Closed As-Built — July 2026 Production Gate*

> **Gate Status:** This chapter is sealed as-built. No component described here
> is aspirational. Every claim is backed by live vector-store writes and routing
> probe results confirmed July 29, 2026. The Chapter 51 prerequisite is
> satisfied. All prior text describing Chapter 50 as "planned," "gated," or
> "prerequisite not yet satisfied" is superseded by this sealed record.

---

## What This Chapter Is About

This chapter explains how Ms. Jarvis keeps each person's conversational memory
completely separate, governed, and free of surveillance-shaped data.

The central question for rural developers is:

> "When Ms. Jarvis remembers past conversations, how does she keep each
> person's memory separate, governed, and non-surveillance-shaped?"

The answer is the per-user direct-sum routing module: a live, tested piece of
the system that writes each user's conversation history, private, and staged
records into that user's own named collections — and nowhere else.

**This chapter may claim:**

- Conversational memory uses an explicit per-user direct-sum routing module
- History, private, and staged collections are named and handled as per-user
  subspaces — not partitions of a shared store
- Durable history and private admission requires retention consent, enforced at
  the routing layer
- Role, request purpose, permitted-use, and legal-authority presence are
  projected into routing evidence before every write decision
- Surveillance-shaped metadata (e.g., `face_embedding`) is suppressed before
  any durable admission, even with user consent
- Live vector-store writes prove alpha and beta users land in disjoint
  collections with no cross-user record leak
- The legacy shared history collection is retired as an authority path for
  new writes
- Chapter 50 is a satisfied prerequisite for Chapter 51

**This chapter must not claim:**

- Unconsented durable conversation retention
- A single unrestricted global conversation memory as the authority path
- Automatic publication of private conversation memory into commons
- Clinical, legal, or universal safety guarantees

---

## 50.1 The Core Concept: Direct Sum in Plain Language

In mathematics, a direct sum of spaces means each component is completely
separate — no element of one space leaks into another, and the full combined
space is simply the collection of all the individual parts.

In Ms. Jarvis, this means:

- User Alpha's conversational memory occupies its own space
- User Beta's conversational memory occupies its own space
- The two spaces never mix, and no record from one appears in the other
- The full conversational memory of the system is the sum of all individual
  per-user spaces, nothing more and nothing less

For rural developers, the practical meaning is this: the system cannot
accidentally show you someone else's conversation history, and it cannot
silently merge your conversations into a shared pool without your knowledge.
These are not policy promises. They are structural constraints enforced at
the routing layer and confirmed by live test.

---

## 50.2 Per-User Collection Families

Each user gets their own family of three named collections in the vector store.
These are not logical partitions of one shared collection — they are separate,
named stores with separate record IDs and separate counts.

**For the two demo users verified in the July 2026 probe:**

User `ch50_demo_alpha` has:
- `conversation_history_user_ch50_demo_alpha`
- `conversation_private_user_ch50_demo_alpha`
- `conversation_staged_user_ch50_demo_alpha`

User `ch50_demo_beta` has:
- `conversation_history_user_ch50_demo_beta`
- `conversation_private_user_ch50_demo_beta`
- `conversation_staged_user_ch50_demo_beta`

The routing module takes a user slug (for example, `ch50_demo_alpha`), resolves
it to the correct history, private, and staged collection names, and writes and
reads only within that user's family. There is no code path that routes a new
write to a shared or legacy collection.

For rural developers: if you deploy Ms. Jarvis for community members in Fayette
County, each member's slug will generate their own three-collection family. No
member can see, overwrite, or contaminate another member's conversational
subspace.

---

## 50.3 The Three Tiers

Every user's memory family is divided into three tiers with different purposes
and different rules.

| Tier | Purpose | Requires Consent | Durable |
|------|---------|-----------------|---------|
| History | General conversational continuity, "remember this" behavior | Yes | Yes |
| Private | Sensitive or tightly scoped conversational memory | Yes | Yes |
| Staged | Short-lived holding state before deciding what to remember | No | No |

**History** is what most people think of as "memory." It is durable, used for
continuity across sessions, and requires the user to have given retention
consent before a record can be written there.

**Private** is for more sensitive material that should not flow into general
history. It also requires retention consent and has additional checks for
forbidden field types.

**Staged** is a waiting room. The system can write something to staging without
consent because staging is not permanent. The record sits there until a decision
is made: promote to history, promote to private, or discard. Staged records are
still per-user — they never go into a shared pool.

---

## 50.4 Step 1 — Consent-Gated Durable Memory

The July 2026 probe verified two outcomes for the history tier: one with consent
granted and one with consent refused.

**With consent — the PERMIT case:**

```json
{
  "tier": "history",
  "user_slug": "ch50_demo_alpha",
  "retention_consent": true,
  "actor_role": "user",
  "request_purpose": "conversation",
  "permitted_use": "memory_retrieval",
  "public_opt_in": false,
  "legal_authority_present": false,
  "verdict": "PERMIT",
  "reason": "per_user_direct_sum_route_permitted",
  "collection": "conversation_history_user_ch50_demo_alpha"
}
```

**Without consent — the SUPPRESS case:**

```json
{
  "tier": "history",
  "user_slug": "ch50_demo_alpha",
  "retention_consent": false,
  "verdict": "SUPPRESS",
  "reason": "retention_consent_required_for_durable_tier",
  "collection": null
}
```

The system does not attempt to find a workaround when consent is absent. It
returns `SUPPRESS`, sets `collection` to null, and writes nothing. No record
is created in any collection. For rural developers, this is the foundational
rule: **no durable history without consent, enforced at the routing layer —
not just in a privacy policy document.**

---

## 50.5 Step 2 — Staged Tier: Per-User Without Requiring Consent

The staged tier allows Ms. Jarvis to hold something lightly — to put it in a
user's space without yet committing to making it permanent.

**Staging probe result for `ch50_demo_alpha`:**

```json
{
  "tier": "staged",
  "user_slug": "ch50_demo_alpha",
  "retention_consent": false,
  "actor_role": "user",
  "request_purpose": "conversation",
  "permitted_use": "memory_retrieval",
  "public_opt_in": false,
  "legal_authority_present": false,
  "verdict": "PERMIT",
  "reason": "per_user_direct_sum_route_permitted",
  "collection": "conversation_staged_user_ch50_demo_alpha"
}
```

**Vector-store confirmation:**

```
conversation_staged_user_ch50_demo_alpha
  count: 1
  record_id: present
  record_present: true
```

Notice: `retention_consent` is `false`, yet the verdict is `PERMIT`. This is
correct behavior. Staging is not durable. The record is held in the user's own
staged collection — not in a shared pool — and it can be deleted, promoted, or
allowed to expire without ever becoming a permanent memory.

For rural developers: staging is how the system handles uncertainty gracefully.
It does not force a permanent write to resolve a temporary situation.

---

## 50.6 Step 3 — Surveillance-Shaped Metadata Suppression

Consent alone is not enough to permit a write. The routing module also checks
whether the record contains forbidden field types — fields that would create
biometric or surveillance-shaped memories even with the user's agreement.

**Forbidden metadata probe result:**

```json
{
  "tier": "private",
  "user_slug": "ch50_demo_alpha",
  "retention_consent": true,
  "verdict": "SUPPRESS",
  "reason": "forbidden_metadata:face_embedding",
  "collection": null
}
```

Here, the user has given consent, the tier is private, and the user slug is
correctly resolved — but the record contains a `face_embedding` field. The
routing module detects the forbidden field and returns `SUPPRESS`. Nothing is
written.

The system does not write biometric data to conversational memory, even when
the user has consented to memory retention. This suppression is built into the
per-user direct-sum routing, not bolted on afterward.

For rural developers: this is the difference between a system that asks for
permission and a system that also has structural limits on what it will do
with that permission. Both are necessary. A system that will store your
face-embedding if you click "agree" is not a non-surveillance-shaped system —
it is just one with a consent dialogue.

---

## 50.7 Step 4 — Proof of Disjoint Collections

The most important verification in this chapter is the disjoint proof: that
records written for alpha never appear in beta's collections, and vice versa.

**Vector-store write results from the July 2026 probe:**

```
conversation_history_user_ch50_demo_alpha
  count: 1
  record_id: convds_af4129…
  record_present: true
  shared_collection_used: false

conversation_history_user_ch50_demo_beta
  count: 1
  record_id: convds_ff2448…
  record_present: true
  shared_collection_used: false
```

**Cross-leak check:**

```
cross_leak_beta_id_in_alpha_collection: []   ← empty
disjoint: true
legacy_shared_collection_used: false
```

The `cross_leak_beta_id_in_alpha_collection` list is empty. Beta's record ID
does not appear anywhere in alpha's history collection. The `disjoint` flag is
`true`. The `legacy_shared_collection_used` flag is `false`.

A legacy shared conversation collection still exists in the system
(`legacy_shared_conversation_history_visible: true`), but it is not used for
new writes. The old "one big shared conversation collection" pattern is retired
as an authority path. New writes go only to per-user families.

---

## 50.8 Routing Evidence Fields

Every routing decision carries a standard set of evidence fields. These are
not just logged metadata — the routing module reads and uses them to decide
whether to write.

| Field | Role in Routing |
|-------|----------------|
| `actor_role` | Confirms the caller is a user, not a system admin or external process |
| `request_purpose` | Must be `"conversation"` for conversational memory writes |
| `permitted_use` | Must be `"memory_retrieval"` for this path |
| `public_opt_in` | False — these records are not treated as commons material |
| `legal_authority_present` | False — no special legal authority is claimed |
| `retention_consent` | Gates durable tier writes |
| `forbidden_metadata` | Triggers SUPPRESS regardless of consent status |

For rural developers, these fields make the routing module auditable. Every
write decision is traceable back to the specific evidence that justified it —
or the specific reason it was suppressed. If a community member asks "why did
the system not remember that conversation?", the answer is available in the
routing trace.

---

## 50.9 Step 5 — The Legacy Shared Collection Is Retired

The probe confirmed:

```
legacy_shared_collection_used: false
legacy_shared_conversation_history_visible: true
```

The legacy shared history collection still exists in the system — it was not
deleted. But it is not used for new writes.

Any code, script, or integration that routes conversational writes to the old
shared pattern must be updated. The per-user family routing module is the
only authorised write path as of the July 2026 production gate.

For rural developers deploying or integrating: do not write to the legacy
shared collection. If you find code that does, treat it as a routing error to
be corrected, not an acceptable fallback.

---

## 50.10 Chapter 50 as Prerequisite for Chapter 51

The Community Hilbert Commons (Chapter 51) requires that per-user memory
partitioning is working before community-level aggregation can be trusted.
The prerequisite logic is:

- If user subspaces are not genuinely disjoint, aggregating across them creates
  a pool that may re-identify individuals
- If forbidden metadata is not suppressed, aggregation can inadvertently create
  a community-level biometric dataset
- If durable memory can be written without consent, the consent model for
  commons promotion cannot be trusted

All three conditions are now satisfied by design and by test. Chapter 50 is
closed as-built. The formal components in Chapter 51 — including the
k-anonymity thresholds, the aggregation operator, and the noninvertibility
proof — can be assessed in a context where individual user spaces are
demonstrably separate.

---

## 50.11 Step-by-Step Summary for Rural Developers

1. **Every user gets their own collection family.**
   History, private, and staged are separate named stores — not partitions of
   one shared store. `conversation_history_user_<slug>` belongs only to that
   user.

2. **Durable tiers require consent.**
   History and private writes return `SUPPRESS` and write nothing if
   `retention_consent` is `false`. This is enforced at the routing layer,
   not in a policy document.

3. **Staging does not require consent.**
   Staged writes are permitted without consent because staged is not durable.
   The record is still per-user — it never goes to a shared pool.

4. **Forbidden field types block writes even with consent.**
   If a record contains `face_embedding` or another forbidden metadata field,
   the routing module returns `SUPPRESS` regardless of consent status. The
   system will not build biometric profiles from conversational memory.

5. **Role and purpose are part of every routing decision.**
   The module checks `actor_role`, `request_purpose`, `permitted_use`,
   `public_opt_in`, and `legal_authority_present` before writing anything.
   These fields are in every routing trace.

6. **No cross-user leak by design and by test.**
   The July 2026 probe confirmed: alpha's record IDs do not appear in beta's
   collections. The `disjoint` flag is `true`. This is not an assumption —
   it is a confirmed measurement.

7. **The legacy shared collection is retired.**
   It still exists but is not used for new writes. Any code routing to the
   old shared collection pattern must be updated to use per-user family routing.

8. **Chapter 50 is a satisfied prerequisite.**
   All prior text describing Chapter 50 as "planned" or "gated" is superseded.
   The Chapter 51 prerequisite is met and the Community Hilbert Commons chapter
   may proceed from this foundation.

---

## 50.12 What This Chapter Does Not Claim

To remain within the gate, this chapter does not claim:

- Durable conversation memory without consent
- A single unrestricted global conversation memory store as the authority path
- Automatic publication of private conversation memory into commons or public
  datasets
- Clinical, legal, or universal safety guarantees

It claims only:

- Bounded per-user conversational subspaces, live in production
- Consent-gated durable history and private memory, enforced at the routing layer
- Staged, private, and history tier separation at the per-user level
- Live evidence that alpha and beta users write into disjoint collections with
  no cross-user leak
- The legacy shared history collection is no longer used for new writes
- Chapter 51 prerequisite: satisfied

---

## 50.13 Closing Statement

Per-user direct-sum decomposition is an as-built feature of conversational
memory in the July 2026 production stack.

Each user in Mount Hope, across Fayette County, or anywhere Ms. Jarvis is
deployed has their own history, private, and staged conversation collections.
Durable tiers require retention consent. Staged tiers provide a non-durable
buffer. Forbidden surveillance-shaped metadata is suppressed at the routing
layer. Live tests show that user alpha's records never appear in user beta's
space or in a shared history collection.

For rural developers, the practical consequence is this: the system you are
building on does not silently merge your users' memories into a common pool,
does not retain conversations without consent, and does not build biometric
profiles regardless of what the user agreed to. Those are structural
constraints built into the routing module — not promises in a privacy policy.

The formal idea of a per-user direct sum is now a concrete routing and storage
behavior that can be inspected, tested, and relied on within the limits this
gate defines.

---

*Chapter 50 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
*Sealed: July 29, 2026 — July 2026 Production Gate.*
*Status: Closed as-built. Chapter 51 prerequisite satisfied.*
