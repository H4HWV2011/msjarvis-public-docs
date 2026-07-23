# 48. Hilbert People Space — Implementation-Aligned Closure

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 22, 2026*

---

## 48.1 What This Chapter Is Allowed to Claim

Within this sealed closure, Chapter 48 is limited to **the people‑space behavior that has actually been implemented and exercised**.

It may claim that:

- session‑derived, person‑linked **candidate promotion logic exists** in the people‑session promotion service;  
- promotion requires **identity, session identity, allowed actor role, constitutional pass, retention consent, and a non‑expired retention state**;  
- **surveillance‑shaped metadata is suppressed** before anything is written into durable people‑space;  
- durable people‑space records are **partitioned into per‑user collections**, with **multi‑actor partitioning demonstrated**;  
- **retention pruning and explicit per‑user deletion** are implemented and tested;  
- **commons isolation holds**, as shown by an unchanged community commons count when people‑space is exercised.

It does **not** claim large‑scale deployment or a rich external civic corpus. The focus is on **correctness of behavior at the current scale**, not on volume.

---

## 48.2 Plain‑Language Purpose for Rural Developers

For rural operators, this chapter answers:

> “When Ms. Jarvis writes anything about people into long‑term memory, what rules does she follow, and how do we know she is not quietly building a surveillance file?”

This chapter explains, step by step:

- how **session behavior** turns into **candidate person‑linked records**;  
- what checks must pass before those candidates become **durable people‑space entries**;  
- how those entries are **kept separate per user**;  
- how **deletion and pruning** actually work;  
- how **commons collections stay unchanged** when people‑space is exercised.

The chapter stays inside the evidence: it talks only about behavior already verified in code and tests.

---

## 48.3 Where Session‑Derived Promotion Logic Lives

Session‑derived, person‑linked candidate promotion is implemented in a dedicated people‑session promotion component.

At a high level, that component:

- takes **person‑linked signals** from a session (for example, continuity or identity‑relevant context);  
- evaluates whether they are **eligible to become durable people‑space records**;  
- applies a series of **gates**;  
- only then writes to per‑user people‑space collections.

This means that **not every session interaction** ends up as durable people‑space. There is a concrete promotion service in the path, and it is configured to **refuse writes when its conditions are not met**.

---

## 48.4 Promotion Conditions: Identity, Role, Constitution, Consent, Expiry

For a person‑linked candidate to be promoted from a session into durable people‑space, all of the following must be satisfied:

- **Identity**: the candidate must be tied to a specific user identity;  
- **Session identity**: it must come from a session that is properly identified, not from an anonymous or ill‑formed context;  
- **Allowed actor role**: the caller or subsystem must have a role that is permitted to request this promotion;  
- **Constitutional pass**: a constitutional or guardian check must not block the promotion;  
- **Retention consent**: the user’s consent posture must allow this kind of retention;  
- **Non‑expired retention state**: the retention configuration must say that such a record is allowed to be active (not already past its intended lifetime).

If any of these checks fail, the promotion logic does **not** write a durable record. The candidate remains ephemeral or is discarded.

For rural developers, you can think of it as a **six‑gate doorway**: identity, session, role, constitution, consent, and retention all have to say “yes” before the memory is stored.

---

## 48.5 Surveillance‑Shaped Metadata Suppression

Before any record enters durable people‑space, surveillance‑shaped metadata is **removed or never written**.

This includes dropping or suppressing:

- unnecessary fine‑grained timestamps that would make activity tracking too precise;  
- device or network identifiers that are not required for the stated purpose;  
- internal IDs that would allow someone to reconstruct a detailed movement or behavior log across sessions.

The promotion pipeline enforces this at write time, so:

- the durable people‑space record contains **only what is needed**;  
- tracking‑style fields are **kept out of long‑term person‑linked storage**.

The effect is that people‑space behaves like **purpose‑bound memory**, not like a background tracking log.

---

## 48.6 Per‑User People‑Space Collections

Durable records landing in Hilbert People Space are stored in **per‑user collections**, not in a single shared people bucket.

Concretely:

- each user has a **dedicated people‑space collection**;  
- the promotion logic writes only to **that user’s collection**;  
- a query for one user’s people‑space does not reach another user’s records.

This is more than an access‑control rule; it is a **storage‑level separation**. The data is partitioned per user, and the system uses these partitions consistently.

---

## 48.7 Multi‑Actor Partitioning: Alpha and Beta People‑Space

The system’s multi‑actor behavior has been demonstrated by creating at least two distinct people‑space collections, often referred to as “alpha” and “beta”.

In practice, this means:

- separate people‑space collections were created for two different actors;  
- promotion logic wrote records into each actor’s people‑space;  
- checks confirmed that **no records leaked** from one to the other;  
- retrieval for alpha did not surface beta’s data, and vice versa.

This test proves that per‑user partitioning works **for more than one user**, not just in a single hard‑coded example.

---

## 48.8 Retention Pruning and Explicit Per‑User Deletion

This closure confirms that **retention pruning and explicit per‑user deletion are implemented and tested**.

Two mechanisms exist:

- **Retention pruning**: background jobs or scheduled processes look at retention metadata (such as timestamps and configured lifetimes) and remove expired people‑space records;  
- **Explicit deletion**: a per‑user deletion request can target that user’s people‑space, and the system actually removes the selected records.

Tests validate that:

- after pruning runs, **expired records are gone**;  
- after an explicit deletion, those records **no longer appear** in people‑space for that user;  
- these operations do not affect other users’ collections.

For rural developers, this means people‑space has **real “forget” behavior**, not just promises.

---

## 48.9 Commons Isolation: Community Commons Stays Unchanged

Commons isolation means that **private people‑space does not quietly feed community‑wide or public collections**.

This is demonstrated by:

- running people‑space promotion and deletion operations;  
- observing that the **`community_hilbert_commons`** collection’s document count remains unchanged;  
- verifying that no code path in the people‑space pipeline writes into the commons collection.

So even when people‑space is active:

- the community commons remains **empty or unchanged**;  
- people‑linked records do **not** “spill over” into shared civic or public views.

This is a concrete, testable version of the promise “private stays private unless explicitly promoted under different rules.”

---

## 48.10 No Claim of Scale

The academic limitation for this closure is clear:

- it does **not** claim that people‑space has been populated at large scale;  
- it does **not** claim a **rich external civic corpus** of person‑linked data.

Instead, it claims:

- that the **pipeline and safeguards** described above work on the current, limited corpus;  
- that the same paths **would apply at larger scale**, but such scaling is **not yet demonstrated** in this runtime.

For readers and rural operators, that means you can trust the **shape and behavior** of people‑space, but you should not assume it already holds a large, diverse body of real‑world civic person data.

---

## 48.11 Step‑by‑Step View for Rural Developers

Putting the implementation‑aligned behavior together, the people‑space path looks like this:

1. **Session produces a person‑linked candidate.**  
   - Ms. Jarvis identifies something that might be useful to remember about a person.

2. **Promotion logic runs.**  
   - Checks identity, session identity, actor role, constitutional rules, consent, and retention settings.

3. **If checks pass, a record is prepared.**  
   - Surveillance‑shaped metadata is dropped or suppressed.  
   - The record is scoped to one user.

4. **Record is written to that user’s people‑space collection.**  
   - Alpha goes to alpha’s collection; beta to beta’s; no mixing.

5. **Pruning and deletion keep space bounded.**  
   - Expired records are pruned.  
   - Per‑user deletion requests remove selected records.

6. **Commons stays separate.**  
   - Community commons collections do not change when people‑space is exercised, unless a separate, explicit promotion path for civic data is used.

If anything in steps 2–4 fails, the system **fails closed** by not promoting, rather than writing an unsafe record.

---

## 48.12 Closing Statement

Chapter 48, at this sealed closure, presents **Hilbert People Space as it actually behaves today**.

Session‑derived person‑linked promotion logic exists and is guarded by identity, role, constitutional, consent, and retention checks. Surveillance‑shaped metadata is suppressed before durable storage, durable people‑space is partitioned per user with multi‑actor separation demonstrated, deletion and pruning are real and tested, and commons collections remain unchanged when people‑space is active. The system therefore holds person‑linked state in a way that is **governed, bounded, and non‑surveillance‑shaped** at the current scale, while honestly acknowledging that large‑scale civic population remains future work.
