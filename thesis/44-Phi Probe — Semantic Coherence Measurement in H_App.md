# 44. Phi Probe — Governed Coherence in the Geographic Corpus (As-Built)

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: July 27, 2026*

---

## 44.1 What This Chapter Is Allowed to Claim

Within this closure gate, Chapter 44 is limited to **live Phi measurement and gate wiring over the governed geographic corpus**, backed by working Hilbert-state services and confirmed row-count evidence from the July 26, 2026 architecture closeout.

It may claim that:

- the **Hilbert state** service is live and connected to Redis;
- **state set/get, projection, transition, and entanglement** are proven by a live probe;
- the **Phi probe service** is live on its configured port and can reach Chroma through `CHROMA_URL`;
- Phi can **sample governed geographic collections** for West Virginia counties, tracts, and block groups;
- Phi writes its state to Redis under `pituitary:phi_state`;
- the `/phi` and `/phi/cached` endpoints return sampled coherence payloads;
- a **hard coherence gate probe passes**, and coherence gate code exists in `gbim_query_router`, `phi_promotion_gate`, and `coherence_remediation`;
- the **current baseline Phi measurement** — 93,423 admissible rows out of 237,655 total GBIM records (39.3% admissibility rate), confirmed on July 26, 2026 — is the concrete, verified coherence baseline against which future measurements are compared;
- tests for these pieces pass in isolated batches.

It may **not** claim downstream outcome calibration across all domains or universal coherence guarantees. This scope is limited to what has been demonstrated for the **governed geographic corpus**.

---

## 44.2 Plain-Language Purpose

For rural developers, the Phi probe in this chapter answers a simple question:

> "Before Ms. Allis uses a big, governed map of West Virginia to support decisions, how does she check that the map is internally hanging together?"

Here, **Phi** is the name of a service that:

- looks at the **governed GIS data** (counties, tracts, block groups);
- measures whether that data is **internally coherent** in the shared embedding space;
- records that reading for other parts of the system to use when deciding whether to **trust and act on** that geographic belief state.

Phi is not a truth oracle. It does not say "these maps are correct." It says, "these counties, tracts, and block groups **fit together** in a stable way under the system's own geometry."

As of July 26, 2026, Phi has a concrete baseline to compare future readings against: **39.3% of GBIM records are admissible** — meaning they satisfy all ten conditions of the public admissibility predicate. That ratio is the system's first measured coherence baseline.

---

## 44.3 Hilbert State Service and Redis

The **Hilbert state service** keeps track of live semantic state in a way that other services can read.

Within this gate, it is safe to say that:

- the Hilbert state service is **up and running**;
- it is **connected to Redis**, which it uses as a backing store;
- basic operations — **set, get, projection, transition, entanglement** — all work and are proven by a live probe.

For a rural operator, this means there is a **central place** where Ms. Allis saves and fetches the current "shape" of her understanding, and that place is actually reachable and responsive in the running system.

---

## 44.4 Phi Service and Chroma Connection

The **Phi probe** is its own service.

Within this scope, Chapter 44 may claim that:

- Phi runs as a live service listening on its configured port (port 8026);
- Phi resolves the Chroma vector store through `CHROMA_URL`;
- Phi can connect to Chroma and **sample from governed collections**.

This connection matters because Phi's job is to measure coherence **in the vector space**, not just to look at raw tables. The embedding model and Chroma store give Phi a shared semantic space where counties, tracts, and block groups can be compared.

---

## 44.5 Governed Geographic Collections in Scope

The governed geographic corpus under this gate includes at least:

- `gbim_wv_counties_v2` — West Virginia counties;
- `gbim_wv_tracts_v2` — West Virginia census tracts;
- `gbimwvblockgroupsv2` — West Virginia block groups.

These three collections together form the **GEO_BELIEF** domain for West Virginia.

Chapter 44 may claim that Phi:

- can **sample embeddings** from each of these collections;
- can compute a **coherence reading** across them in the shared embedding space;
- has done so successfully in live probes.

For rural developers, that means Phi is checking not just one map, but how **all three levels of map** talk to each other in one semantic frame.

---

## 44.6 The July 26, 2026 Baseline Coherence Measurement

On July 26, 2026, the architecture closeout produced the following row counts, confirmed in `runtime_governance.public_answer_audit` and verified by the `ALTER TABLE` spacetime/provenance CHECK constraint pass:

| Measurement | Count |
|---|---|
| Total rows in `public.gbim_record` | 237,655 |
| Rows satisfying all ten admissibility conditions | 93,423 |
| Rows stored but not yet admissible | 144,232 |
| **Admissibility rate (Phi baseline)** | **39.3%** |

This ratio — **93,423 admissible out of 237,655 total, or 39.3%** — is the system's first concrete **Phi Probe baseline measurement**. It represents the proportion of the governed GBIM corpus that, as of July 26, 2026, simultaneously satisfies all of the following:

- is promoted to `authorized` status (`C2`);
- is explicitly flagged as publicly claimable (`C3`);
- carries fully populated provenance (`C4`, `C5`, `C6`);
- is in a `fresh` or `aging` lifecycle state (`C7`);
- carries the three new structural columns added on July 26, 2026: `spatial_unit_id` (`C8`), `spatial_unit_kind` (`C9`), and `valid_time_start` (`C10`).

### 44.6.1 What 39.3% Means

A 39.3% admissibility rate means that **more than half the stored records are currently inadmissible**, not because they are wrong or corrupt, but because they have not yet completed the full promotion and spacetime-anchoring journey required by the ten-condition predicate.

The 144,232 inadmissible rows fall into several categories:

- records with `public_claim_allowed = false` — held in the governed store but not cleared for public claims;
- records missing one or more of `spatial_unit_id`, `spatial_unit_kind`, or `valid_time_start` — ingested before the July 26, 2026 spacetime columns were added, and awaiting backfill;
- records with `degradation_status = 'stale'` — aged out of the admissible window by the lifecycle decay schedule.

None of these categories represent a coherence failure. They represent **work in the pipeline** — records that are stored and governed but not yet speakable. The baseline measurement makes the current state visible so that future Phi readings can be compared against it.

### 44.6.2 How to Use the Baseline

The 39.3% rate is recorded in `runtime_governance.public_answer_audit` with a `snapshot_at` timestamp of `2026-07-26`. Future lifecycle jobs and Phi probe runs should compare against this snapshot:

- A **rising admissibility rate** signals that backfill, promotion, and lifecycle management are progressing correctly.
- A **falling admissibility rate** is not automatically bad: it may reflect intentional expiry, lifecycle decay, or a change in the admissibility predicate. The direction and cause should both be logged.
- A **sudden large drop** — for example, more than 10 percentage points between scheduled lifecycle jobs — should trigger a coherence investigation.

For rural developers, this baseline functions like a **known-good reading on a gauge**. You always compare the current reading to the baseline, not to an abstract ideal.

---

## 44.7 How Phi Measures Coherence

At a high level, Phi:

1. **Samples vectors** from the governed geographic collections in Chroma.
2. Measures how similar or aligned those vectors are in the embedding space.
3. Produces a **coherence score and mode** (for example, "coherent" above a threshold).
4. Writes a summary into Redis as `pituitary:phi_state`.

The July 26, 2026 baseline row-count ratio is the **structural coherence measure** — what fraction of stored GBIM records meet every governance condition simultaneously. The Chroma-based vector coherence measure — how well the embeddings of admitted records align in the shared semantic space — is a complementary reading. Both together constitute the Phi Probe's full picture.

Phi also exposes:

- `/phi` — a live sampling endpoint;
- `/phi/cached` — a version that returns the latest recorded state from Redis.

Both endpoints return structured payloads that include the collections sampled and the coherence reading.

---

## 44.8 Coherence Gate Wiring

The gate evidence confirms a **"hard coherence gate probe"** and the presence of coherence gate code in:

- `gbim_query_router`;
- `phi_promotion_gate`;
- `coherence_remediation`.

Within this scope, Chapter 44 may claim that:

- a **coherence gate** exists in code and can be exercised;
- the gate can inspect Phi's readings and make decisions (for example, whether to allow or remediate certain operations on the geographic corpus);
- **coherence remediation code** exists to respond when Phi detects problems (for example, by triggering re-sampling, cleaning, or other corrective steps).

In plain terms: the system does not just measure coherence for curiosity; it has code paths that can **act on the measurement** when needed, at least for the governed GIS corpus. The 39.3% baseline gives those code paths a concrete reference point for "normal" versus "anomalous" admissibility.

---

## 44.9 What Coherence Means (and Does Not Mean)

In this chapter, **coherence** means:

- the **internal fit** of the geographic belief state in the embedding space;
- whether counties, tracts, and block groups **support and reinforce** each other's semantic patterns;
- whether the vector space looks stable and well-structured, rather than fragmented or degenerate;
- at the structural level: whether the proportion of admissible-to-total records is stable and understood.

Coherence does **not** mean:

- guaranteed factual accuracy of every map entry;
- full calibration of Phi scores across every domain;
- that a good score in geography automatically implies good scores elsewhere;
- that a 39.3% admissibility rate is the correct or ideal long-term target — it is the **current measured baseline**, not a design target.

The gate explicitly forbids claiming "downstream outcome calibration across all domains" on the basis of this evidence. Coherence here is **local to the governed geographic corpus** and is one signal alongside truth checks, governance, and other safeguards.

---

## 44.10 Live State and Caching

Phi writes its current reading to Redis under a key such as:

- `pituitary:phi_state`

This key:

- stores the latest coherence payload from `/phi`;
- allows other services to read the state **quickly** without re-sampling every time;
- ensures that coherence readings are **part of the shared live state**, not just an internal calculation.

The July 26, 2026 lifecycle snapshot — 93,423 admissible / 237,655 total — is stored in `runtime_governance.public_answer_audit` with a `snapshot_at` timestamp and serves as the baseline for Redis-cached state comparisons.

For rural operators, you can think of `pituitary:phi_state` as a **small gauge on the dashboard**: if something is off with the geographic corpus, that gauge can reflect it — and you now have a concrete number to compare it against.

---

## 44.11 Tests and Reliability at This Scope

The closure evidence states that relevant tests **pass in isolated batches**.

Within this gate, Chapter 44 may say that:

- unit or integration tests for the Hilbert state service, Phi service, Chroma connectivity, and coherence gate wiring are passing;
- these tests cover basic pathways for set/get, projection, transition, entanglement, Phi sampling, and gate invocation.

The phrase "isolated batches" keeps the claim honest: this is a **tested subsystem**, not a guarantee that every possible interaction in the whole stack has been explored.

---

## 44.12 Step-by-Step View for Rural Developers

A rural operator can understand Chapter 44's Phi path as:

1. **Hilbert state is live.**
   - There is a running service that uses Redis to track semantic state.

2. **Phi service runs and can reach Chroma.**
   - Phi uses `CHROMA_URL` to connect to the vector store.

3. **Phi samples governed GIS beliefs.**
   - It pulls vectors from `gbim_wv_counties_v2`, `gbim_wv_tracts_v2`, and `gbimwvblockgroupsv2`.

4. **Phi computes a coherence reading.**
   - It summarizes how well those three levels of geography fit together in the embedding space.

5. **Phi compares against the baseline.**
   - The July 26, 2026 baseline is 93,423 admissible out of 237,655 total (39.3%). Any new reading is compared to this number. A rising rate means the pipeline is progressing. A large sudden drop is a signal to investigate.

6. **Phi writes its result to Redis.**
   - The reading lands at `pituitary:phi_state`.

7. **Other services call `/phi` or `/phi/cached`.**
   - They can see the current coherence state and decide how to proceed.

8. **Coherence gate code can act.**
   - If coherence is too low or shows a problem, gate and remediation code in the GBIM router and related services can respond.

If any of these steps fail, the architecture expects services to **fail closed or enter remediation**, not to ignore the problem and act as if everything is fine.

---

## 44.13 What This Chapter Does Not Claim

To stay within the academic scope, Chapter 44 does **not** claim:

- that 39.3% is the target or ideal admissibility rate — it is only the confirmed baseline as of July 26, 2026;
- calibrated thresholds that are proven to predict real-world outcomes;
- full coherence measurement across all semantic domains in Ms. Allis;
- human-level judgment about the quality of geographic decisions;
- universal guarantees that a coherent reading means "safe to act" in every context.

It only claims **live, working Phi measurement and gate wiring over the governed West Virginia geographic corpus**, with the Hilbert state service, Redis, Chroma, and the associated gates all proven to function, and a concrete baseline admissibility measurement of 39.3% (93,423 / 237,655) confirmed on July 26, 2026.

---

## 44.14 Closing Statement

Chapter 44 places Phi squarely inside the **governed GIS path** of Ms. Allis, and adds the first concrete baseline coherence measurement to the thesis record.

Hilbert state is live and Redis-backed. Phi can reach Chroma and sample the governed county, tract, and block-group collections. Phi writes its readings into shared state and exposes them over `/phi` and `/phi/cached`. The coherence gate wiring in GBIM and related services has been exercised with passing tests.

As of July 26, 2026, the structural Phi baseline is **93,423 admissible records out of 237,655 total — a 39.3% admissibility rate**. This number is stored in `runtime_governance.public_answer_audit`, anchored to a `snapshot_at` timestamp, and available for comparison by every future Phi reading, lifecycle job, and coherence gate invocation. It is not a design target; it is a measured fact about the system's current governed state, recorded here so that future change is visible and auditable.

This gives rural developers a concrete, step-by-step picture of how Ms. Allis measures and uses **internal coherence** in her West Virginia geographic beliefs — without overstating what that measurement can prove beyond this specific, verified scope.

---

*Chapter 44 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
