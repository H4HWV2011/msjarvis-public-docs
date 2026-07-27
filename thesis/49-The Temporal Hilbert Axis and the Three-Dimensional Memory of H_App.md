# 49. The Temporal Hilbert Axis and the Three-Dimensional Memory of H_App (As-Built)

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 27, 2026*

---

## 49.1 What This Chapter Is Allowed to Claim

Within this closure gate, Chapter 49 is limited to **implemented temporal behavior** of H_App as it actually runs today, across three practical memory dimensions and one temporal validator.

It may claim that:

- H_App uses **ephemeral reasoning**, **staged candidates**, and **historical memory** as three distinct strata of temporal memory;
- these strata are implemented as:
  - **ephemeral reasoning → session/scratchpad context**;
  - **staged candidates → `promotion_state = 'candidate'` rows**;
  - **historical memory → `public_admissible_gbim_mv` (93,423 fresh rows)**;
- the system demonstrates **hysteresis** via an **18‑month decay to `stale`** for governed records;
- the **temporal promotion validator** is concretely implemented as the `gbim_record_spacetime_provenance_chk` constraint on `public.gbim_record`.

It must **not** claim a complete Hilbert-space formalization of all time behavior in every subsystem, nor perfect global memory management beyond the implemented axis described here.

---

## 49.2 Plain-Language Purpose

For rural developers, this chapter answers a simple question:

> "How does Ms. Allis remember things over time without mixing up what she is just thinking about, what she is testing, and what is already trusted?"

This chapter explains:

- how **ephemeral reasoning, staged candidates, and historical memory** form a three-dimensional memory model;
- how those dimensions are implemented using **session context**, **promotion states**, and **admissible views**;
- how **hysteresis** (memory that slowly goes stale) works in practice;
- how the **temporal promotion validator** ensures that time and provenance are correct when records move into historical memory.

The focus is on **live implementation**, not on all possible theory.

---

## 49.3 The Temporal Hilbert Axis: Three Memory Dimensions

Within this gate, the “Temporal Hilbert Axis” is a way of naming three practical memory dimensions that line up along time:

1. **Ephemeral reasoning** — what the system is thinking about right now in a session.
2. **Staged candidates** — records that might become history, but are still being checked.
3. **Historical memory** — records that have passed checks and are ready to back public claims.

These dimensions form a path:

- from **scratchpad thoughts**,  
- through **candidate records**,  
- into **admissible historical memory**.

The axis is temporal because it tracks how information matures over time.

---

## 49.4 Ephemeral Reasoning → Session/Scratchpad Context

The first dimension is **ephemeral reasoning**.

### 49.4.1 What Ephemeral Reasoning Is

Ephemeral reasoning is:

- the **short-term, in-session thought** the system uses to answer questions;
- not stored as governed history;
- subject to being discarded when the session ends.

In H_App, this is implemented as **session or scratchpad context**. It may include:

- temporary calculations;
- intermediate chains of reasoning;
- draft interpretations that never become stored records.

For rural developers, it is like notes on the back of an envelope that help answer a question but are not kept as formal records.

### 49.4.2 Why Ephemeral Reasoning Is Separate

Ephemeral reasoning is intentionally kept:

- **out of** GBIM tables;
- **out of** admissible public views;
- **away from** long-term historical memory.

This prevents:

- half-formed thoughts from being treated as governed facts;
- transient reasoning from polluting long-term state.

On the temporal axis, ephemeral reasoning lives “closest to now,” but farthest from permanent storage.

---

## 49.5 Staged Candidates → `promotion_state = 'candidate'` Rows

The second dimension is **staged candidates**.

### 49.5.1 What Staged Candidates Are

Staged candidates are:

- records that have **left the scratchpad**,  
- but have **not yet been fully promoted** to historical memory;
- stored inside the governed corpus with **`promotion_state = 'candidate'`**.

In `public.gbim_record`, this is the set of rows whose `promotion_state` column is `'candidate'`. They are in the database, but they are still waiting for:

- provenance checks;
- lifecycle checks;
- spatial and temporal anchoring checks;
- policy and admissibility decisions.

### 49.5.2 How Candidates Fit the Temporal Axis

On the temporal axis:

- candidates are **closer to long-term memory** than ephemeral reasoning;
- they are **not yet historical** because they can still be rejected, corrected, or updated.

For rural developers, candidates are like drafts saved in a folder: not just thoughts, but not yet official.

---

## 49.6 Historical Memory → `public_admissible_gbim_mv` (93,423 Fresh Rows)

The third dimension is **historical memory**.

### 49.6.1 What Historical Memory Is

Historical memory is:

- the body of **governed records that have passed all admissibility checks**;
- ready to back public claims;
- anchored in space and time.

In this system, historical memory is implemented as the materialized view:

- **`public.public_admissible_gbim_mv`**,  
- containing **93,423 fresh rows** as of the July 26, 2026 gate.

These rows satisfy the ten-condition predicate for admissibility, including:

- correct promotion state (`'authorized'`);
- correct lifecycle status (`'fresh'` or `'aging'`);
- full provenance;
- fully populated spatial and temporal anchors.

### 49.6.2 Why Historical Memory Matters

On the temporal axis:

- historical memory is where **long-lived, trusted facts** reside;
- it is the source of **answers that stand up to scrutiny**.

For rural developers:

- if a question relies on historical infrastructure or geography facts, it should draw from **admissible historical memory**;
- the 93,423 fresh rows are the subset that is **currently trusted enough** to back public answers.

---

## 49.7 Hysteresis Proof → 18-Month Decay to `stale`

The system demonstrates **hysteresis** in memory via **decay to `stale` over 18 months**.

### 49.7.1 What Hysteresis Means Here

Hysteresis in this context means:

- memory does **not instantly vanish** when time passes;
- instead, records **stay “fresh” or “aging” for a bounded period**;
- after that period (18 months), they **decay to `stale`**.

This behavior:

- prevents the system from treating old facts as perpetually fresh;
- ensures that, over time, data that is too old for current decisions is marked as such.

### 49.7.2 How 18-Month Decay Works

In practice:

- a record enters historical memory with a lifecycle status (for example, `degradation_status = 'fresh'`);
- as time passes, the record may move to `'aging'`;
- after about **18 months**, it moves to `'stale'`.

Once a record is `stale`:

- it no longer qualifies for admissible public claims;
- it is kept for internal reference, but treated as **historically inert** for answers.

For rural developers, this is like keeping old reports in a filing cabinet: they exist, but you do not base new county decisions on them without re-verification.

---

## 49.8 Temporal Promotion Validator → `gbim_record_spacetime_provenance_chk`

The **temporal promotion validator** ensures that records are properly anchored in time and space, and correctly governed, before they enter or remain in historical memory.

### 49.8.1 What the Validator Does

The validator is implemented as a database constraint:

- **`gbim_record_spacetime_provenance_chk`**  
  on `public.gbim_record`.

This constraint enforces conditions such as:

- non-null `spatial_unit_id`, `spatial_unit_kind`, and `valid_time_start`;
- required promotion and lifecycle fields;
- required provenance fields.

If a record fails these conditions:

- it cannot be promoted into the admissible set;
- the constraint rejects updates that would violate temporal or spatial requirements.

### 49.8.2 Why This Is a Temporal Validator

On the temporal axis, the validator:

- ensures that records have a **real time anchor** (`valid_time_start`);
- guards against **time-ambiguous promotion** (records with missing or incorrect temporal context).

For rural developers:

- this is the check that keeps historical memory from filling up with records whose “since when” is unknown;
- it guarantees that promoted records have full spacetime and provenance context.

---

## 49.9 Implementation Status Addendum: Mapping the Three Dimensions

This chapter adds an **Implementation Status Addendum** to make the mapping between theory and implementation explicit.

### 49.9.1 Ephemeral Reasoning

- **Theory:** Ephemeral reasoning — short-term, in-session thought.
- **Implementation:** **Session/scratchpad context**.
- **Status:** Implemented as non-governed, discardable session state that does not enter GBIM tables or admissible views.

### 49.9.2 Staged Candidates

- **Theory:** Staged candidates — records under consideration.
- **Implementation:** **`promotion_state = 'candidate'` rows** in `public.gbim_record`.
- **Status:** Implemented as governed database rows that have left the scratchpad but have not yet passed admissibility checks.

### 49.9.3 Historical Memory

- **Theory:** Historical memory — trusted, long-lived records.
- **Implementation:** **`public_admissible_gbim_mv`** materialized view.
- **Status:** Implemented as 93,423 fresh rows (as of July 26, 2026) that satisfy all ten admissibility conditions, including temporal and spatial anchoring.

### 49.9.4 Hysteresis Proof

- **Theory:** Hysteresis — memory fades over time, not instantly.
- **Implementation:** **18-month decay to `stale`** in lifecycle status.
- **Status:** Implemented as a lifecycle path where records move from `fresh` to `aging` to `stale` over about 18 months, exiting admissible historical memory when stale.

### 49.9.5 Temporal Promotion Validator

- **Theory:** Temporal promotion validator — guardrail for time-aware promotion.
- **Implementation:** **`gbim_record_spacetime_provenance_chk` constraint**.
- **Status:** Implemented and applied to all 237,655 GBIM records, enforcing non-null spacetime and provenance fields and rejecting invalid updates.

---

## 49.10 Step-by-Step View for Rural Developers

From a local operator’s point of view, the temporal memory of H_App works like this:

1. **Think in the session.**  
   Ms. Allis uses ephemeral reasoning in a session/scratchpad to explore and reason. Nothing in this phase is yet a governed fact.

2. **Write down candidates.**  
   When something is strong enough to consider, it becomes a GBIM record with `promotion_state = 'candidate'`. It is stored, but not yet trusted history.

3. **Promote to history.**  
   After passing checks (including the temporal validator), records are promoted into historical memory in `public_admissible_gbim_mv`, joining the 93,423 fresh rows that back public claims.

4. **Let old history fade.**  
   Over about 18 months, records degrade through lifecycle states and eventually become `stale`, leaving the admissible set. They remain for reference but stop being used for new public answers.

5. **Trust the validator.**  
   Throughout, the `gbim_record_spacetime_provenance_chk` constraint ensures that promoted records have proper time and space anchors and provenance.

This is how the temporal Hilbert axis becomes a practical memory path.

---

## 49.11 What This Chapter Does Not Claim

To stay inside the academic scope of this gate, Chapter 49 does **not** claim:

- a complete formalization of every temporal behavior in H_App as a Hilbert space;
- perfect global memory hygiene across all services;
- that every future update will always obey the same 18‑month decay window.

It only claims:

- the implemented three-dimensional memory mapping described above;
- the existence of an 18‑month hysteresis path to `stale`;
- the enforcement of temporal promotion rules via `gbim_record_spacetime_provenance_chk`.

---

## 49.12 Closing Statement

Chapter 49 now records a **concrete, implemented temporal memory structure** for H_App.

Ephemeral reasoning lives in session context and never becomes history by accident. Staged candidates reside in GBIM tables with `promotion_state = 'candidate'`, awaiting checks. Historical memory is represented by 93,423 fresh admissible rows in `public_admissible_gbim_mv`, anchored in time and space and ready to back public claims. Over roughly 18 months, records decay to `stale`, demonstrating hysteresis rather than instant forgetting. The `gbim_record_spacetime_provenance_chk` constraint stands as the temporal promotion validator that keeps the axis honest.

For rural developers, this means Ms. Allis’s memory is not a mystery. It is a three-dimensional, time-aware path that separates what she is thinking about now, what she is testing, and what she already trusts, with clear rules for how information moves and fades over time.

---

*Chapter 49 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*  
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*  
*See LICENSE for terms.*  
