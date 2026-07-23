# 22. Identity-Focused Retention

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 22, 2026*

---

## 22.1 Why This Matters for Polymathmatic Geography

This chapter explains how Ms. Allis keeps identity‑linked information without turning every session into a permanent file. It describes how per‑user retention is gated by consent, pruning, and clear separation between private memory and public disclosure.

It supports:

- **P1 – Every where is entangled** by letting identity, place, and meaning stay connected while keeping strict retention boundaries.  
- **P3 – Power has a geometry** by locating identity retention behind explicit gates instead of letting it happen at the moment of thought.  
- **P5 – Design is a geographic act** by treating identity retention and disclosure as design decisions, not accidental side effects.  
- **P12 – Intelligence with a ZIP code** by allowing place‑aware, person‑relevant memory only when it has crossed the right consent and retention paths.  
- **P16 – Power accountable to place** by making identity‑linked updates traceable, prunable, and separate from public “commons” content.

This chapter belongs to the **Computational Instrument** tier. It documents identity‑focused retention as built, not as a promise of legal proof or indefinite storage.

---

## 22.2 What Identity-Focused Retention Covers

Identity‑focused retention governs **how Ms. Allis remembers a person over time**.

It covers:

- per‑user preferences (for example, “prefers step‑by‑step guidance”);  
- stable constraints (for example, “has limited connectivity”);  
- long‑term projects or situations the user chooses to track;  
- place‑linked identity context (for example, “works on Appalachian community mapping”).

It does **not** simply mirror everything that passes through the sandbox or chat:

- not every sentence is kept;  
- not every inference becomes identity memory;  
- not every session becomes a permanent story.

Retention is a separate, governed step.

---

## 22.3 Consent-Gated Identity Registration

No identity memory is created without **explicit retention consent**.

The system distinguishes between:

- **Using information in the moment** – allowed for answering the current question.  
- **Registering information as identity** – only allowed when the user has opted in to retention.

Concretely:

- if retention consent is **missing or revoked**, identity registration is suppressed;  
- if the user has consented, identity updates can still be **selective and bounded**;  
- consent can be reconsidered, and retention behavior must follow the latest setting.

This keeps the default posture closer to “forget by default, remember on purpose” instead of “remember everything unless told otherwise.”[web:141]

---

## 22.4 Per-User Identity Partitioning

Identity‑linked data is stored in **per‑user partitions**, not in one global pool.

Each user gets:

- a private identity/people‑space area;  
- session‑linked collections for recent context;  
- staged or experimental areas that can be pruned before consolidation.

This per‑user design means:

- one user’s identity memory does not automatically leak into another’s;  
- deletion can be scoped to a single user;  
- inspection tools can show “what this system knows about this person” in one place.

From a rural developer’s point of view, the key idea is that identity memory is **namespaced by user**, so you can clear or audit one person’s space without touching others.

---

## 22.5 Session-Derived People-Space and Pruning

Identity‑linked content usually starts as **session‑derived** context.

The pipeline is:

1. A conversation creates provisional identity‑relevant observations.  
2. Those observations live in **session‑scoped** or **staged** collections.  
3. Retention logic decides what, if anything, should be consolidated.

Session‑derived people‑space retention must support:

- **deletion** – the ability to remove a user’s records on request;  
- **expired‑record pruning** – automatic trimming of old or low‑value entries;  
- **bounded size** – no unlimited growth of per‑user histories.

If these behaviors fail, identity retention gates block until fixed, as seen in the gate’s early “people_session_retention_probe_failed” status.

---

## 22.6 Private, Staged, and Public Memory Families

The architecture uses distinct **memory families** for identity‑related information:

- **Private per‑user collections** – only visible to that user’s context; not shared or published.  
- **Staged conversation collections** – recent or experimental material that may be pruned or consolidated later.  
- **Commons collections** – public resources; **not** identity‑focused by default.

Chapter 22’s gate closes only when:

- per‑user/private/staged conversation families are visible in the backing store;  
- identity content resides in private/staged families by default;  
- no identity‑linked item is sent to commons without explicit `public_opt_in`.

This separation prevents accidental “promotion” of private identity material into public resources.

---

## 22.7 Public Disclosure vs Retention

Identity‑focused retention and **public disclosure** are deliberately separated.

- Retention says, “May the system remember this about you for future interactions?”  
- Public disclosure says, “May this content or pattern be made visible to others as part of a commons or shared artifact?”

Rules:

- **Missing `public_opt_in` → no public disclosure.**  
- Consent for retention does **not** imply consent for commons publication.  
- Public sharing requires a separate, explicit yes.

For example, a user might allow Ms. Allis to remember that they are working on a specific community project, but not to use their stories or patterns in any public knowledge base.

---

## 22.8 Suppression Rules

Two suppression behaviors are central and are now enforced:

1. **Missing retention consent is suppressed.**  
   - When consent is missing, the system does not write new identity records.  
   - Existing identity records may be pruned or held back from use, depending on policy.

2. **Public disclosure without opt‑in is suppressed.**  
   - Even if data is correctly retained in per‑user space, it does not enter commons without a `public_opt_in` flag.  
   - Queries or processes that try to treat identity memory as public are blocked or downscoped.

These suppression rules are what turned Chapter 22 from “BLOCKED” into “CLOSED_FOR_REWRITE” in the gate reports.

---

## 22.9 What Chapter 22 Does Not Claim

Within this gate, identity‑focused retention does **not** claim:

- legal identity proofing or strong verification of who the user “really” is;  
- indefinite retention or archival guarantees;  
- automatic public disclosure of any retained fact;  
- biometric production readiness;  
- clinical or psychological safety guarantees.

Instead, it claims:

- **bounded, consent‑gated retention**;  
- **per‑user partitions** with deletion and pruning;  
- **clear separation** between private identity memory and public commons content.

---

## 22.10 Step-by-Step View for Rural Developers

If you are running Ms. Allis on your own hardware, identity‑focused retention behaves like this:

1. **Consent setup.**  
   - You decide whether retention is enabled and at what level.

2. **Live use.**  
   - Ms. Allis can use what you say during a session to help you, regardless of retention.

3. **Retention check.**  
   - If retention is enabled, selected, validated pieces of identity‑relevant information may be written to your per‑user collections.

4. **Pruning and deletion.**  
   - You (or an operator) can prune or delete per‑user records.  
   - Systems jobs clean up old or expired entries.

5. **Public sharing (optional).**  
   - Only if you explicitly opt in, certain patterns or artifacts may be promoted into commons collections.

At every step, the separation between **using** information and **remembering** it—and between **remembering** and **publishing**—is part of the design, not something bolted on later.

---

## 22.11 Closing Statement

Identity‑focused retention in Ms. Allis is consent‑gated, per‑user partitioned, and prunable. Identity‑linked material begins life in session‑scoped or staged collections, becomes retention‑eligible only after validation and consent checks, and never becomes public without explicit opt‑in.

This structure lets Ms. Allis offer continuity and personalization while remaining accountable to the people and places it serves, rather than silently accumulating and broadcasting personal histories.
