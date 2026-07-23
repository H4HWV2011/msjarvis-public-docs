# 44. Phi Probe — Governed Coherence in the Geographic Corpus

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 22, 2026*

---

## 44.1 What This Chapter Is Allowed to Claim

Within this closure gate, Chapter 44 is limited to **live Phi measurement and gate wiring over the governed geographic corpus**, backed by working Hilbert‑state services.

It may claim that:

- the **Hilbert state** service is live and connected to Redis;  
- **state set/get, projection, transition, and entanglement** are proven by a live probe;  
- the **Phi probe service** is live on its configured port and can reach Chroma through `CHROMA_URL`;  
- Phi can **sample governed geographic collections** for West Virginia counties, tracts, and block groups;  
- Phi writes its state to Redis under `pituitary:phi_state`;  
- the `/phi` and `/phi/cached` endpoints return sampled coherence payloads;  
- a **hard coherence gate probe passes**, and coherence gate code exists in `gbim_query_router`, `phi_promotion_gate`, and `coherence_remediation`;  
- tests for these pieces pass in isolated batches.

It may **not** claim downstream outcome calibration across all domains or universal coherence guarantees. This scope is limited to what has been demonstrated for the **governed geographic corpus**.

---

## 44.2 Plain‑Language Purpose

For rural developers, the Phi probe in this chapter answers a simple question:

> “Before Ms. Jarvis uses a big, governed map of West Virginia to support decisions, how does she check that the map is internally hanging together?”

Here, **Phi** is the name of a service that:

- looks at the **governed GIS data** (counties, tracts, block groups);  
- measures whether that data is **internally coherent** in the shared embedding space;  
- records that reading for other parts of the system to use when deciding whether to **trust and act on** that geographic belief state.

Phi is not a truth oracle. It does not say “these maps are correct.” It says, “these counties, tracts, and block groups **fit together** in a stable way under the system’s own geometry.”

---

## 44.3 Hilbert State Service and Redis

The **Hilbert state service** keeps track of live semantic state in a way that other services can read.

Within this gate, it is safe to say that:

- the Hilbert state service is **up and running**;  
- it is **connected to Redis**, which it uses as a backing store;  
- basic operations — **set, get, projection, transition, entanglement** — all work and are proven by a live probe.

For a rural operator, this means there is a **central place** where Ms. Jarvis saves and fetches the current “shape” of her understanding, and that place is actually reachable and responsive in the running system.

---

## 44.4 Phi Service and Chroma Connection

The **Phi probe** is its own service.

Within this scope, Chapter 44 may claim that:

- Phi runs as a live service listening on its configured port (for example, 8026);  
- Phi resolves the Chroma vector store through `CHROMA_URL`;  
- Phi can connect to Chroma and **sample from governed collections**.

This connection matters because Phi’s job is to measure coherence **in the vector space**, not just to look at raw tables. The embedding model and Chroma store give Phi a shared semantic space where counties, tracts, and block groups can be compared.

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

## 44.6 How Phi Measures Coherence

At a high level, Phi:

1. **Samples vectors** from the governed geographic collections in Chroma.  
2. Measures how similar or aligned those vectors are in the embedding space.  
3. Produces a **coherence score and mode** (for example, “coherent” above a threshold).  
4. Writes a summary into Redis as `pituitary:phi_state`.

This gives other services a compact view of **“how well the geographic belief corpus is holding together right now.”**

Phi also exposes:

- `/phi` — a live sampling endpoint;  
- `/phi/cached` — a version that returns the latest recorded state from Redis.

Both endpoints return structured payloads that include the collections sampled and the coherence reading.

---

## 44.7 Coherence Gate Wiring

The gate evidence confirms a **“hard coherence gate probe”** and the presence of coherence gate code in:

- `gbim_query_router`;  
- `phi_promotion_gate`;  
- `coherence_remediation`.

Within this scope, chapter 44 may claim that:

- a **coherence gate** exists in code and can be exercised;  
- the gate can inspect Phi’s readings and make decisions (for example, whether to allow or remediate certain operations on the geographic corpus);  
- **coherence remediation code** exists to respond when Phi detects problems (for example, by triggering re‑sampling, cleaning, or other corrective steps).

In plain terms: the system does not just measure coherence for curiosity; it has code paths that can **act on the measurement** when needed, at least for the governed GIS corpus.

---

## 44.8 What Coherence Means (and Does Not Mean)

In this chapter, **coherence** means:

- the **internal fit** of the geographic belief state in the embedding space;  
- whether counties, tracts, and block groups **support and reinforce** each other’s semantic patterns;  
- whether the vector space looks stable and well‑structured, rather than fragmented or degenerate.

Coherence does **not** mean:

- guaranteed factual accuracy of every map entry;  
- full calibration of Phi scores across every domain;  
- that a good score in geography automatically implies good scores elsewhere.

The gate explicitly forbids claiming “downstream outcome calibration across all domains” on the basis of this evidence. Coherence here is **local to the governed geographic corpus** and is one signal alongside truth checks, governance, and other safeguards.

---

## 44.9 Live State and Caching

Phi writes its current reading to Redis under a key such as:

- `pituitary:phi_state`

This key:

- stores the latest coherence payload from `/phi`;  
- allows other services to read the state **quickly** without re‑sampling every time;  
- ensures that coherence readings are **part of the shared live state**, not just an internal calculation.

For rural operators, this means you can think of `pituitary:phi_state` as a **small gauge on the dashboard**: if something is off with the geographic corpus, that gauge can reflect it.

---

## 44.10 Tests and Reliability at This Scope

The closure evidence states that relevant tests **pass in isolated batches**.

Within this gate, Chapter 44 may say that:

- unit or integration tests for the Hilbert state service, Phi service, Chroma connectivity, and coherence gate wiring are passing;  
- these tests cover basic pathways for set/get, projection, transition, entanglement, Phi sampling, and gate invocation.

The phrase “isolated batches” keeps the claim honest: this is a **tested subsystem**, not a guarantee that every possible interaction in the whole stack has been explored.

---

## 44.11 Step‑by‑Step View for Rural Developers

A rural operator can understand Chapter 44’s Phi path as:

1. **Hilbert state is live.**  
   - There is a running service that uses Redis to track semantic state.

2. **Phi service runs and can reach Chroma.**  
   - Phi uses `CHROMA_URL` to connect to the vector store.

3. **Phi samples governed GIS beliefs.**  
   - It pulls vectors from `gbim_wv_counties_v2`, `gbim_wv_tracts_v2`, and `gbimwvblockgroupsv2`.

4. **Phi computes a coherence reading.**  
   - It summarizes how well those three levels of geography fit together.

5. **Phi writes its result to Redis.**  
   - The reading lands at `pituitary:phi_state`.

6. **Other services call `/phi` or `/phi/cached`.**  
   - They can see the current coherence state and decide how to proceed.

7. **Coherence gate code can act.**  
   - If coherence is too low or shows a problem, gate and remediation code in the GBIM router and related services can respond.

If any of these steps fail, the architecture expects services to **fail closed or enter remediation**, not to ignore the problem and act as if everything is fine.

---

## 44.12 What This Chapter Does Not Claim

To stay within the academic scope, Chapter 44 does **not** claim:

- calibrated thresholds that are proven to predict real‑world outcomes;  
- full coherence measurement across all semantic domains in Ms. Allis;  
- human‑level judgment about the quality of geographic decisions;  
- universal guarantees that a coherent reading means “safe to act” in every context.

It only claims **live, working Phi measurement and gate wiring over the governed West Virginia geographic corpus**, with the Hilbert state service, Redis, Chroma, and the associated gates all proven to function at the time of closure.

---

## 44.13 Closing Statement

Chapter 44 places Phi squarely inside the **governed GIS path** of Ms. Allis.

Hilbert state is live and Redis‑backed, Phi can reach Chroma and sample the governed county, tract, and block‑group collections, Phi writes its readings into shared state and exposes them over `/phi` and `/phi/cached`, and the coherence gate wiring in GBIM and related services has been exercised with passing tests. This gives rural developers a concrete, step‑by‑step picture of how Ms. Jarvis measures and uses **internal coherence** in her West Virginia geographic beliefs—without overstating what that measurement can prove beyond this specific, verified scope.
