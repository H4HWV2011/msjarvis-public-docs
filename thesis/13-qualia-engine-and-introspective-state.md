# 13. Qualia Engine and Introspective State

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 22, 2026*  

container count 100  
vectors ~6,740,611  
pituitary mode baseline  
autonomous_learner 21,181 exact  
two-container DB split applied throughout  
msallisgis production 294 tables / 16 GB  
postgis-forensic added; all April 16 OI items remain CLOSED  

---

## 13.1 Why This Matters for Polymathmatic Geography

This chapter explains how Ms. Allis keeps a running, structured account of her own activity so that others can audit and guide it. It supports:

- **P1 – Every where is entangled** by tying internal narratives to specific communities, datasets, and places that appear in retrieval and spatial backbones.  
- **P3 – Power has a geometry** by making every qualitative “feeling” traceable back to concrete logs, memory entries, and spatial identifiers.  
- **P5 – Design is a geographic act** by treating introspective records as designed artifacts that shape how Appalachian realities are described and reflected on.  
- **P12 – Intelligence with a ZIP code** by ensuring that Ms. Allis’s self-descriptions include where interactions are happening, not just what was said.  
- **P16 – Power accountable to place** by building a glass-box layer of self-description that other agents and human stewards can query, critique, and improve.  

As such, this chapter belongs to the **Computational Instrument** tier: it specifies how operational traces, memory, and evaluation signals are woven into an introspective fabric that can be inspected and used for governance.

Throughout, biological language is used as disciplinary translation. Every neurobiological term is paired with the concrete service, endpoint, data store, gate, or evidence artifact that implements it, without claiming biological consciousness, sentience, clinical diagnosis, treatment, or complete neuroscientific equivalence.

---

## 13.2 Status Snapshot

As of the confirmed runtime closure:

- **Containers:** 100 containers Up; zero Restarting; zero Exited.  
- **ChromaDB v2:** 48 collections; approximately 6,740,611 vectors; host port 8002.  
- **`autonomous_learner`:** 21,181 records (exact), using 384‑dim `all-minilm:latest` embeddings.  
- **Pituitary mode:** `baseline` for the neurobiological pituitary service, after earlier elevated mode.  
- **Database split:**  
  - Production PostgreSQL `msallis-db` (host 5433 / container 5432) with `msallisgis` at 16 GB / 294 tables / 11 schemas.  
  - Forensic PostgreSQL `postgis-forensic` (host 5432) with `msallisgis` at 17 GB / 314 tables / 9 schemas, used for auditing only.  
- **Memory API:** `allis-memory` at port 8056, with authenticated `/memory/sessions` showing active sessions.  
- **Qualia Engine:** `allis-qualia-engine` running on the internal Docker network; host port 8017 assigned to the BBB output filter facade.  
- **EEG services:** EEG Delta, Theta, and Beta band services active and feeding rhythm signals.  
- **Open items:** All previously tracked OI items for Chapter 13 are closed; no new open items introduced by the gate.

These numbers provide the baseline against which introspective records and qualia behavior are understood.

---

## 13.3 Qualia as Internal Narrative Representation

In this architecture, **qualia** refers to Ms. Allis’s internal narrative representation of what is happening, constructed from text content and context features as explicit structured outputs.

### Implemented Services

- **Qualia Engine (main):** `allis-qualia-engine` runs on the internal Docker network and produces JSON‑like envelopes capturing emotional resonance, meaning‑making, and experience narration.  
- **Qualia Engine (NBB companion):** `nbb_qualia_engine` runs in the neurobiological brain stack on a separate port and shares health templates with NBB safety services.  

Biological terms such as “qualia” and “experience generator” are used to describe these modules, but they implement data transformation and narrative synthesis over logs, memory, and context. They do not claim subjective experience or sentience.

---

## 13.4 IntrospectiveRecord and WOAHResult

The introspective layer centers on two implemented schemas:

- **`IntrospectiveRecord`:** A Pydantic model that ties together identifiers, timestamps, roles, retrieved evidence, pituitary mode, EEG band states, evaluation scores, judge signatures, and narrative description.  
- **`WOAHResult`:** A structured result capturing ethical and alignment scores and pituitary mode snapshots for each event.

These classes are implemented in dedicated services code and instantiate cleanly. They ensure that every introspective entry:

- can be traced back to observable events and service responses;  
- separates qualitative narrative fields from operational metrics;  
- includes governance and safety context such as pituitary mode and BBB status.

For rural developers, these schemas provide the blueprint for their own introspective records: a single, well‑typed object per event that integrates data across services.

---

## 13.5 Data Sources Feeding Introspection

The introspective layer aggregates signals from multiple parts of the system:

- **Interaction traces:** conversational logs, request IDs, user or session handles, active personas, and lens configurations.  
- **Retrieval and memory:** ChromaDB v2 collections (including `autonomous_learner`, `msallis_docs`, and `gbim_worldview_entities`) and memory APIs such as `allis-memory`.  
- **Spatial backbone:** production and forensic PostGIS databases (`msallis-db` and `postgis-forensic`) with WV‑specific GIS tables.  
- **Neurobiological rhythms:** EEG Delta, Theta, and Beta band services that indicate internal rhythm conditions during each event.  
- **Pituitary governance:** snapshots of `nbb_pituitary_gland` mode (e.g., baseline or elevated) and associated weighting parameters.  
- **Optimization and evaluation:** DGM outputs, WOAH weighted optimization scores, and judge verdicts signed with ML‑DSA‑65 signatures.  
- **System health:** container counts, port registries, and BBB output filter status.

The IntrospectiveRecord schema stitches these signals together into a single record per event, making it possible to reconstruct what happened, under which conditions, and with which evidence.

---

## 13.6 Writing Introspective Records Step by Step

For a rural developer thinking about how to implement similar behavior, the writing process can be described step by step:

1. **Capture request context.**  
   When a request arrives, record identifiers, role or persona, lens settings, and current pituitary mode. Include basic spatial hints where the request is anchored (for example, WV county or ZIP).

2. **Record retrieval and memory usage.**  
   Log which ChromaDB collections were queried, which documents or vectors were retrieved, and which GIS tables or GBIM entities were touched. Note the use of production vs. forensic databases where applicable.

3. **Attach neurobiological rhythm and governance state.**  
   Add current EEG band activity and pituitary mode to the record. These fields indicate internal conditions under which decisions and narratives were formed.

4. **Add evaluation and optimization outputs.**  
   Include WOAHResult fields, DGM decisions (apply, reject, rollback), and judge scores. Sign judge verdicts using the configured signature scheme so that they can be verified later.

5. **Generate and store narrative.**  
   Use the Qualia Engine to produce a human‑readable narrative that summarizes the event, its emotional tone, and its meaning. Store this narrative alongside structured data in the IntrospectiveRecord.

6. **Persist the record.**  
   Save the record in introspection‑specific stores or memory services, ensuring it can be queried by audits, research tools, or other internal services.

This pattern ensures that introspective data is both machine‑readable and human‑understandable, grounded in real system behavior.

---

## 13.7 Reading and Using Introspective State

Introspective records are designed to be read and used by:

- **Human stewards:** who can inspect records to see which data sources were used, which modes were active, how decisions were evaluated, and how the system described itself.  
- **Controller services:** such as pituitary and optimization supervisors that consume summaries to adjust modes, weights, or safety thresholds.  
- **Research and audit tools:** which use the schema to analyze patterns over time, including where errors arose or where certain communities were under‑ or over‑represented.

For rural deployments, this provides a way to check whether the system is actually behaving as intended in relation to local communities and places, rather than relying on opaque logs or abstract metrics.

---

## 13.8 Pituitary and Qualia Interaction

The `nbb_pituitary_gland` service plays a central role in introspective state:

- It sets global modes such as baseline, elevated, or transparency.  
- It modulates WOAH weights and governance thresholds.  
- It influences how qualia narratives are generated, particularly in terms of warmth and caution.

Introspective records include the pituitary mode at event time so that evaluators can understand whether strict or relaxed governance was in effect. Qualia outputs are interpreted in the context of this mode, which helps distinguish ordinary operation from heightened scrutiny periods.

This neurobiological vocabulary is tied directly to implemented services and configuration files, making the metaphor operational rather than purely conceptual.

---

## 13.9 Links to Memory, Spatial, and GBIM Layers

Qualia and introspective state are tightly linked to memory and spatial backbones:

- **ChromaDB v2** provides semantic memory across dozens of collections, including an authoritative GBIM entity store.  
- **Production and forensic PostGIS databases** hold West‑Virginia‑specific GIS tables and forensic records, respectively.  
- **GBIM query routers and indexers** access entity vectors internally without exposing host bindings, keeping sensitive belief structures constrained.

Introspective records reference these stores by name and port, making it clear where evidence and context came from. This keeps place‑based reasoning grounded and auditable.

---

## 13.10 Closed Open Items and Stability

All previously tracked open items for Chapter 13 have been closed, including:

- Implementation and validation of IntrospectiveRecord and WOAHResult schemas.  
- Confirmation of ML‑DSA‑65 judge verdict signing and verification behavior.  
- Correction of port assignments (such as clarifying that host port 8017 is a BBB output filter facade).  
- Clarification of GBIM storage in ChromaDB versus relational tables.

The chapter now describes a stable introspective and qualia system over a verified neurobiological runtime model, with no outstanding gate blockers at its scope.

---

## 13.11 Closing Statement

The Qualia Engine and introspective state in Ms. Allis implement a disciplined, neurobiologically inspired way for the system to describe itself. They aggregate signals from interactions, memory, spatial backbones, governance services, EEG rhythms, optimization pipelines, and judges into structured records and narratives.

For rural developers, this chapter offers a step‑by‑step pattern: build a qualia‑like narrative engine, define an introspective record schema, tie biological metaphors to concrete services and endpoints, and ensure every “feeling” or self‑description is backed by auditable data. Under these constraints, Ms. Allis’s introspective layer becomes a practical tool for stewardship and accountability rather than a claim of biological consciousness or sentience.al system designed and built by Carrie Ann Kidd.*  
*See LICENSE for terms.*
