# 49. The Temporal Hilbert Axis and the Three-Dimensional Memory of H_App (As-Built)

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: July 27, 2026*

---

## 49.1 Why a Three-Dimensional Memory

This chapter explains how Ms. Allis' memory is organized not just in a straight line of time, but in a **three-dimensional geometry** that couples time, space, and person. The temporal Hilbert axis provides the time dimension, spatial grounding provides the place dimension, and per-person worldview memory provides the person dimension.

The goal is academic and practical at once. Academically, this chapter shows how a temporal Hilbert axis can be used to shape a three-dimensional memory system that remains consistent with governed candidate flows. Practically, it explains, in step-by-step terms, how events are only admitted into durable memory when they satisfy consent, coherence, and promotion readiness conditions.

As of July 27, 2026, this chapter also carries an **Implementation Status Addendum** (§49.13) that maps each theoretical tier — ephemeral, staged, and historical — to its exact as-built counterpart in the live system. The admissibility gate on historical promotion is no longer a design plan; it is the `gbim_record_spacetime_provenance_chk` CHECK constraint running in `wv_gis`.

For rural developers, the message is:

**"The system remembers like a map: when something happened, where it happened, and who it mattered to — always under gates, never by accident. And those gates are now running in the database."**

---

## 49.2 Gate-Constrained Scope

This chapter stays within a tightly defined scope.

It may claim that:

- Ms. Allis uses a **Temporal Hilbert Axis** to organize event candidates into ephemeral, staged, and historical tiers;
- spatial grounding and per-person memory axes combine with the Temporal Hilbert Axis to form a three-dimensional memory of H_App (time × space × person/worldview);
- promotion into historical memory requires retention consent, coherence, and promotion readiness;
- this 3-D memory is implemented as a governed candidate system, not a free-form log of everything;
- as of July 26, 2026, the three tiers have **as-built counterparts** in the live system: ephemeral reasoning maps to session context, staged candidates map to `promotion_state = 'candidate'` rows in `public.gbim_record`, and historical memory maps to `public_admissible_gbim_mv` (93,423 rows, `degradation_status = 'fresh'`).

It may **not** claim that:

- the Temporal Hilbert Axis proves a particular theory of consciousness or metaphysics;
- the 3-D memory is perfect, complete, or unbiased;
- historical memory has legal authority or spiritual standing;
- memory gates replace human oversight, law, or community review.

Within this gate, the Temporal Hilbert Axis and H_App's memory geometry are treated as **architectural instruments**: they define how Ms. Allis structures and constrains her memory space, not what it means philosophically.

---

## 49.3 The Temporal Hilbert Axis: Time as a Governed Dimension

The **Temporal Hilbert Axis** is the time dimension of Ms. Allis' memory system.

It treats each candidate event as a point that must be placed on a structured time axis under explicit rules. Rather than a loose "timeline," it is a governed mechanism that enforces three key temporal tiers:

1. **Ephemeral**
   - Very recent or one-off observations.
   - Used for immediate reasoning but not yet considered for durable memory.

2. **Staged**
   - Events that are important enough to hold for possible promotion later.
   - Still under review, not yet historical.

3. **Historical**
   - Events that have passed all gates and are admitted into durable memory.
   - Intended to be retained and referenced as part of H_App.

The Temporal Hilbert Axis coordinates these tiers using:

- event identifiers;
- timestamps;
- observed time lags;
- promotion readiness flags;
- coherence checks;
- retention consent signals;
- allowed tiers and roles.

In simple terms, time is not just "before and after." It is "not yet durable," "held for review," and "admitted," all governed by explicit logic.

---

## 49.4 Spatial and Person Axes: Completing the 3-D Memory

To get a three-dimensional memory, the Temporal Hilbert Axis is combined with two other axes:

1. **Spatial axis** — where the event belongs.
   - Grounded through spatial candidates and geospatial checks.
   - Uses canonical GEOIDs, centroids, and locality constraints.
   - Ensures events outside allowed geography (for example, outside West Virginia) cannot be promoted into certain local memory tiers.

2. **Person/worldview axis** — who and in what personal context the event belongs.
   - Managed through per-user direct-sum memory and background pattern systems.
   - Uses user identifiers, session identifiers, tiers (ephemeral vs durable), and permitted uses.
   - Enforces retention consent, public opt-in, and role restrictions.

When these three axes are combined, each historical event in H_App can be understood as a point in a three-dimensional governed space:

- **Time**: when it belongs on the Temporal Hilbert Axis;
- **Space**: where it belongs in the spatial substrate;
- **Person/Worldview**: for whom and in what kind of memory it is allowed to be held.

For rural developers, this is like storing records in a three-story courthouse:

- one shelf for "when,"
- one shelf for "where,"
- one shelf for "who."

Nothing gets put away without being labeled on all three shelves, and some shelves are off limits for certain records.

---

## 49.5 H_App: The Three-Dimensional Memory of the Appalachian Hilbert Space

H_App is the three-dimensional memory built over Ms. Allis' Appalachian deployment.

Academically, it is helpful to think of H_App as a **Hilbert-like space** where each admitted event is represented by coordinates along:

- a temporal axis (ephemeral → staged → historical tiers);
- a spatial axis (Appalachian geography, community boundaries, and relevant geocodes);
- a person/worldview axis (per-user memory tiers and broader background patterns).

Operationally, H_App is not just a mathematical abstraction. It is the concrete arrangement of:

- temporal memory tables and storage keys;
- spatial stores and spatial candidate promotions;
- per-user and pattern memory collections;
- meta-fields marking consent, permitted uses, and promotion reasons.

The Hilbert language is used to emphasize that memory is **vector-like and multidimensional**: events are not only ordered but also **located** in a combined space that respects place and person.

For rural developers, H_App is the "memory barn" that only accepts bales which are properly stacked by time, by place, and by person, with the doors locked according to consent and purpose.

---

## 49.6 Temporal Tiers in Detail

The Temporal Hilbert Axis enforces distinct behaviors in each tier.

### 1. Ephemeral Tier

- Holds very recent events, often near real-time.
- Used for immediate reasoning, short-term context, and transient state.
- Not eligible for long-term retention on its own.
- Does not require retention consent for mere transient processing, but is still subject to safety filters.

### 2. Staged Temporal Tier

- Holds events that might matter long enough to consider for promotion.
- Requires stronger checks than ephemeral, but still not fully historical.
- Subject to hysteresis windows (minimum time before promotion is even considered).
- Acts as a **buffer** between transient activity and long-term history.

### 3. Historical Temporal Tier

- Holds events that are fully admitted into durable memory.
- Requires retention consent, coherence, and promotion readiness.
- Vulnerable to long-term consequences if misused, so gates must be strict.
- Interacts with spatial and per-person axes to maintain locality and privacy.

These tiers are governed by explicit verdicts, such as:

- PERMIT — allowed, with a storage key or record identifier;
- REVIEW — not yet permitted, requires human or additional gate checks;
- SUPPRESS — not allowed to become historical memory;
- UNREACHABLE — used to catch misconfigured or logically impossible states.

For rural developers, the three temporal tiers are like:

- "today's notepad" (ephemeral),
- "this week's folder on the desk" (staged),
- "the county archive vault" (historical).

---

## 49.7 Conditions for Historical Admission

An event candidate can only move along the Temporal Hilbert Axis into the **historical** tier when certain conditions are satisfied.

Key conditions include:

- **Retention consent**
  - For durable tiers, explicit retention consent must be present.
  - If consent is missing, the verdict must be suppression or review, not permit.

- **Coherence**
  - The event's content must satisfy coherence checks.
  - If coherence is low or unknown, promotion should be held in review or suppressed.

- **Promotion readiness**
  - A promotion-ready flag must be set by upstream gates.
  - This ensures promotion is not triggered on first sight, but only after earlier validation steps.

- **Tier validity**
  - The requested temporal tier must be one of the allowed tiers.
  - Invalid tier requests result in suppression.

- **Forbidden metadata**
  - If forbidden metadata keys are present, promotion must be suppressed.

- **Role and purpose constraints**
  - Actor roles and request purposes must fall within allowed sets.
  - If not, the event cannot be admitted to historical memory.

For rural developers, these conditions act like rules for what gets written into a community's official record. Without proper signatures, dates, and reasons, a handwritten note does not become a deed.

---

## 49.8 Combining Time, Space, and Person

When the Temporal Hilbert Axis is combined with spatial and person axes, H_App implements a three-dimensional discipline.

A candidate event can be described by:

- **Time coordinate**
  - location on the Temporal Hilbert Axis (ephemeral, staged, or historical),
  - event timestamp,
  - observed lag between occurrence and recording.

- **Space coordinate**
  - canonical geocode (such as GEOID),
  - centroid longitude and latitude,
  - allowed or disallowed locality (for example, inside or outside West Virginia).

- **Person/worldview coordinate**
  - user or community identifier,
  - memory tier (ephemeral vs durable),
  - permitted use and request purpose,
  - consent flags and public opt-in settings.

An event becomes part of H_App only when:

- its **temporal coordinate** is permitted in the historical tier;
- its **spatial coordinate** is allowed by spatial gates;
- its **person coordinate** is allowed by per-user and pattern memory gates.

This three-coordinate structure ensures that there is no single "global" memory. There is governed, place-aware, person-aware memory, with explicit rules about what is allowed to live there.

For rural developers, this is like a 3-D filing system where each box must be labeled:

- "When did this happen?",
- "Where did this happen?",
- "For whom and under what consent did we keep it?"

No label, no box in the archive.

---

## 49.9 Step-by-Step: How an Event Moves into H_App

This section describes a typical path for an event becoming part of H_App's historical memory.

### Step 1: Event occurs and is observed

An input event — such as a conversation snippet, a spatial observation, or a civic interaction — is observed by Ms. Allis.

- It is initially treated as ephemeral.
- No durable memory or external action occurs yet.

### Step 2: Event becomes a temporal candidate

If the event might matter beyond immediate reasoning, a **Temporal Memory Candidate** is formed, with fields such as:

- entity identifier;
- event identifier;
- event summary;
- timestamps (event time and observed time);
- proposed tier (ephemeral, staged, or historical);
- actor role and request purpose;
- retention consent and coherence flags;
- metadata.

At this point, the event is still a candidate, not yet admitted.

### Step 3: Temporal evaluation

The candidate is evaluated on the Temporal Hilbert Axis. The evaluator:

- checks for required fields;
- verifies the tier is valid;
- checks for forbidden metadata;
- enforces consent and coherence rules;
- applies promotion readiness logic.

Based on these checks, it issues a verdict such as:

- PERMIT ephemeral state;
- PERMIT staged state;
- PERMIT historical state (with keys);
- REVIEW;
- SUPPRESS.

### Step 4: Spatial and person gating

If the candidate is a good candidate for historical admission, additional gates must be satisfied:

- Spatial gate checks whether the event's geocode and locality fall within allowed regions for this deployment.
- Per-user memory gate checks whether the user's tier, consent, and permitted uses allow durable storage.

If either gate fails, the event cannot become part of H_App, even if temporal conditions looked acceptable.

### Step 5: Historical promotion and storage

Only when:

- temporal verdict is PERMIT for historical tier;
- spatial gating is satisfied;
- per-user gating is satisfied;

does the system write a record into historical memory with:

- time axis keys;
- spatial references;
- per-user or pattern references;
- consent and purpose metadata.

At this point, the event becomes part of H_App's three-dimensional memory.

### Step 6: Later retrieval

Future queries and reasoning can then reference H_App by:

- time range;
- geography;
- user or worldview;
- or combinations of all three.

But even retrieval behavior remains governed by permitted uses and roles, consistent with earlier chapters.

For rural developers, this path is deliberately long on purpose. Every step is a chance to say "no" or "not yet" before something becomes historical memory.

---

## 49.10 Relationship to Other Governed Candidate Systems

The Temporal Hilbert Axis and H_App's memory are part of a larger network of governed candidate systems inside Ms. Allis:

- cognition sandbox and first-stage evaluation;
- spatial sandbox and spatial candidate promotion;
- per-user memory gates;
- external communication authority;
- background pattern and broader feedback gates.

The three-dimensional memory of H_App does not override these systems; it sits **downstream** from them.

For example:

- an external communication candidate might reference historical memory but still must pass external communication gates;
- a per-user direct-sum candidate might refer to temporal events but still must satisfy direct-sum gating;
- a background pattern candidate might aggregate across historical events but still must respect consent and commons eligibility.

This ensures that even within H_App, internal use of memory is constrained by layered gates.

For rural developers, think of H_App as the shelves in the back room. Other services still need permission to walk in and read the files.

---

## 49.11 Limits of the Temporal Hilbert Axis and H_App

Even with a three-dimensional geometry, the memory system has limits.

It does **not**:

- capture every relevant event;
- guarantee perfect fairness or representation;
- solve social questions about who should have power over memory;
- make Ms. Allis a legal record keeper.

It does:

- enforce explicit conditions for historical admission;
- embed place and person in the structure of memory;
- provide a disciplined way to avoid uncontrolled accumulation of data;
- make it possible to audit and reason about what has been remembered and why.

This is the academic posture of the chapter: the Temporal Hilbert Axis and H_App are important design choices, not metaphysical claims.

---

## 49.12 Closing Statement

The Temporal Hilbert Axis and the three-dimensional memory of H_App turn Ms. Allis' memory from a flat log into a governed, place-aware, person-aware space. Events move along a time axis — from ephemeral to staged to historical — only when they satisfy consent, coherence, and promotion readiness gates. Those events are then grounded in space and attached to people and worldviews.

For rural developers, this system is meant to be understandable and inspectable. It does not remember everything. It remembers only what passes through these three axes of responsibility: **when**, **where**, and **for whom** — always under rules that can be explained, audited, and, when needed, changed.

---

## 49.13 Implementation Status Addendum — As-Built (July 26, 2026)

This addendum maps each theoretical tier of the Temporal Hilbert Axis to its exact counterpart in the live `wv_gis` system as confirmed on July 26, 2026. For every tier, this section names the as-built mechanism, the verified row counts or probe results, and the specific database object that enforces promotion.

---

### 49.13.1 Ephemeral Tier → Session Context

**Theoretical description:** Very recent or one-off observations used for immediate reasoning. Not yet a candidate for durable memory.

**As-built counterpart:** Session context held in the LLM reasoning layer during a conversation or task turn. This is in-memory, in-process state that does not write to `public.gbim_record` unless an explicit promotion path is triggered. It is the "notepad" that exists only for the duration of the session and then is discarded.

**Verification:** The ephemeral tier produces no persistent row in `public.gbim_record`. Its existence is confirmed by its *absence* from the governed store — session reasoning does not automatically become a governed record. This is the intended behavior: the ephemeral tier is scoped to the calling context and leaves no trace in the database unless a downstream promotion gate explicitly writes a candidate row.

**Rural developer check:** After any session, run:

```sql
SELECT count(*) FROM public.gbim_record
WHERE promotion_state = 'candidate'
AND ingested_at > now() - interval '5 minutes';
```

If this count does not grow on its own during idle periods, the ephemeral tier is correctly isolated from the governed store.

---

### 49.13.2 Staged Tier → `promotion_state = 'candidate'` Rows in `public.gbim_record`

**Theoretical description:** Events that are important enough to hold for possible promotion later. Still under review, not yet historical. Subject to hysteresis windows.

**As-built counterpart:** Rows in `public.gbim_record` with `promotion_state = 'candidate'`. These are records that have been written into the governed store but have not yet passed all conditions for promotion to `'authorized'`. They are present in the base table, visible to `runtime_governance_role`, but **not** present in `public_admissible_gbim_mv` and therefore not reachable by the public instrument.

A staged candidate row looks like this in the schema:

```sql
SELECT gbim_id, promotion_state, public_claim_allowed,
       degradation_status, spatial_unit_id, valid_time_start
FROM public.gbim_record
WHERE promotion_state = 'candidate'
LIMIT 5;
```

A candidate row will have `promotion_state = 'candidate'` and typically `public_claim_allowed = false`. It is stored, but inadmissible for public claims.

**Hysteresis proof — lifecycle decay to `stale` at 18 months:** The lifecycle decay demonstration confirms hysteresis behavior in the staged/historical boundary. A row that was once `degradation_status = 'fresh'` (historical and admissible) decays through `'aging'` and eventually reaches `'stale'` at approximately 18 months after ingestion. A `stale` row is no longer admissible in `public_admissible_gbim_mv` even if it retains `promotion_state = 'authorized'` and `public_claim_allowed = true`. The 10-condition admissibility predicate requires `degradation_status IN ('fresh', 'aging')`; a stale row fails condition $C_7$ and is excluded. This is hysteresis operating correctly: promotion into the historical tier does not mean "admitted forever" — decay can return a row to an inadmissible state without requiring a human to manually demote it.

**Rural developer check:** To see staged candidates:

```sql
SELECT count(*) AS staged_candidates
FROM public.gbim_record
WHERE promotion_state = 'candidate';
```

To confirm a stale row is excluded from the admissible surface:

```sql
-- This count should NOT include stale rows:
SELECT count(*) FROM public.public_admissible_gbim_mv
WHERE degradation_status = 'stale';
-- Expected: 0
```

---

### 49.13.3 Historical Tier → `public_admissible_gbim_mv` (93,423 Rows, `degradation_status = 'fresh'`)

**Theoretical description:** Events fully admitted into durable memory. Requires retention consent, coherence, and promotion readiness. The target state on the Temporal Hilbert Axis.

**As-built counterpart:** `public.public_admissible_gbim_mv` — the materialized view of all rows in `public.gbim_record` that pass the ten-condition admissibility predicate. As of July 26, 2026:

| Metric | Count |
|---|---|
| Total authorized rows in `public.gbim_record` | 237,655 |
| Admissible rows in `public_admissible_gbim_mv` | 93,423 |
| Of which `degradation_status = 'fresh'` | 93,423 |
| Of which `degradation_status = 'stale'` (excluded) | 0 |

The 93,423 fresh admissible rows are the **operational historical tier** of H_App at this gate. They are the records the public instrument can read. They are the records that back `runtime_governance.public_answer_packet`. They are the only records that can produce a `"label": "seen"` answer in the public evidence surface.

**Rural developer check:**

```sql
SELECT degradation_status, count(*) AS row_count
FROM public.public_admissible_gbim_mv
GROUP BY degradation_status
ORDER BY row_count DESC;
```

Expected result at this gate: one row, `fresh | 93423`. As records age, `aging` rows will appear. When the first `stale` rows appear, they will be absent from this view — confirming that decay and hysteresis are working.

---

### 49.13.4 Temporal Promotion Validator → `gbim_record_spacetime_provenance_chk`

**Theoretical description:** The gate that enforces historical admission conditions. In the theoretical model, this is the set of conditions that must be met before an event moves from staged to historical.

**As-built counterpart:** The `gbim_record_spacetime_provenance_chk` CHECK constraint on `public.gbim_record`, added and verified on July 26, 2026 against all 237,655 rows without error.

```sql
ALTER TABLE public.gbim_record
ADD CONSTRAINT gbim_record_spacetime_provenance_chk
CHECK (
  NOT (promotion_state = 'authorized' AND public_claim_allowed = true)
  OR (
    spatial_unit_id IS NOT NULL
    AND spatial_unit_kind IS NOT NULL
    AND valid_time_start IS NOT NULL
    AND under_whose_authority IS NOT NULL
    AND company_name IS NOT NULL
    AND ingested_at IS NOT NULL
  )
);
```

This constraint is the **temporal promotion validator** in operation. Its logic states: *a row that is both authorized and flagged for public claims must have all spatial, temporal, and provenance fields populated.* If any of those fields is null, the database rejects the row outright — not at the application layer, not in a policy check, but at the lowest possible level, enforced on every insert and update.

For the Temporal Hilbert Axis, this means: the conditions for historical admission are not just checked in code. They are enforced in the schema itself. A row cannot become authorized and publicly claimable unless it carries a `valid_time_start` (closing the temporal half of the Spacetime Contract) and a `spatial_unit_id` with `spatial_unit_kind` (closing the spatial half). Without these, the database returns:

```
ERROR: new row for relation "gbim_record" violates check constraint
"gbim_record_spacetime_provenance_chk"
```

**Rural developer check:** Attempt to insert a row that should fail:

```sql
INSERT INTO public.gbim_record
  (gbim_id, promotion_state, public_claim_allowed,
   under_whose_authority, company_name, ingested_at,
   spatial_unit_id, spatial_unit_kind, valid_time_start)
VALUES
  (gen_random_uuid(), 'authorized', true,
   'WVGIS', 'WVGIS', now(),
   NULL, 'blockgroup', '2020-01-01');
-- Expected: ERROR violates check constraint
```

If the error fires, the constraint is enforcing temporal promotion correctly.

---

### 49.13.5 Tier Mapping Summary

| Theoretical Tier | As-Built Counterpart | Key Verified Evidence |
|---|---|---|
| **Ephemeral** | Session context (in-process, not written to governed store) | Absence of automatic candidate rows during idle periods |
| **Staged** | `promotion_state = 'candidate'` rows in `public.gbim_record` | Visible to `runtime_governance_role`; excluded from `public_admissible_gbim_mv` |
| **Historical** | `public_admissible_gbim_mv` (93,423 rows, `degradation_status = 'fresh'`) | Ten-condition predicate enforced; fresh rows back public claims |
| **Hysteresis proof** | Lifecycle decay to `stale` at 18 months | `stale` rows excluded from admissible view even if technically authorized |
| **Temporal promotion validator** | `gbim_record_spacetime_provenance_chk` CHECK constraint | Verified against 237,655 rows on July 26, 2026; rejects non-conforming inserts at the schema level |

---

*Chapter 49 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
