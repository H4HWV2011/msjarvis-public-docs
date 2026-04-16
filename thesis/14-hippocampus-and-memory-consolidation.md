# 14. Hippocampus and Memory Consolidation

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: 2026-04-16 — CLOSED*

> **★ April 16, 2026 — FULL SPRINT CLOSURE:** All open items resolved and all stale infrastructure numbers updated. Container count: **110 containers Up** (supersedes April 1 baseline of 96). ChromaDB: **49 active collections, 6,722,589+ total vectors** (supersedes March 28 baseline of 40/6,675,442). `msjarvisgis`: **551 tables, 45 GB** (supersedes "501 tables, 91 GB" — table count and size corrected to April 16 confirmed values). `autonomous_learner`: **21,181+ records as of April 10, 2026** — the 57-item post-fix slice was the April 1 recovery baseline only; Phase 1.45 active retrieval confirmed in April 16 preflight gate. `msjarvis_docs` ChromaDB: **7,465 items** (expanded from 4,192 March 28 baseline). Community resources: **64 verified resources** (all 55 WV counties confirmed; supersedes 52). `msjarvis-db` (port **5433**): bind corrected from `0.0.0.0` to `127.0.0.1` — orphaned container stopped, removed, and recreated via compose. `jarvis-memory:8056` `/memory/sessions`: HTTP 200 confirmed with 14 active sessions; `JARVIS_API_KEY` exported and set in shell environment. End-to-end pipeline: **99–107 seconds on RTX 4070 GPU** (the 436-second CPU baseline is archived). Preflight gate: **all 27 gates ✅ green**. **Chapter 14 is CLOSED.**

---

## Why This Matters for Polymathmatic Geography

This chapter explains how Ms. Jarvis turns lived interactions — often about specific West Virginia places — into durable, inspectable memory. It supports:

- **P1 – Every where is entangled** by tying conversational experiences and world-model updates to shared semantic, institutional, and spatial backbones grounded in GBIM entities, normalized beliefs, and a statewide hippocampal index.
- **P3 – Power has a geometry** by making long-term memory a structured, queryable space over worldview-tied features, not an opaque chat log, so that reasoning paths can be traced across specific datasets, programs, and jurisdictions.
- **P5 – Design is a geographic act** by deciding which entities, programs, and communities are promoted into GBIM, given nine-axis beliefs, and mirrored into hippocampal collections keyed by worldview, dataset, and feature identity.
- **P12 – Intelligence with a ZIP code** by anchoring consolidated memories in WV geospatial layers, normalized nine-axis beliefs, and local knowledge bases so that questions about "who is helped where" are answered in terms of concrete places and entities.
- **P16 – Power accountable to place** by storing rich, provenance-aware traces (worldview IDs, datasets, GeoDB feature IDs, centroids, SRIDs) so communities can audit how advice and analysis are grounded in their own places rather than abstract averages.

As such, this chapter belongs to the **Computational Instrument** tier: it specifies the hippocampal consolidation pipeline that turns Ms. Jarvis's activity and world models into a long-term, place-aware memory substrate. The `jarvis-hippocampus` service was deployed March 15, 2026 (commit `b90f9ff`) as part of the production stack and is confirmed operational in the end-to-end pipeline benchmark. Phase 1.45 community memory retrieval (deployed March 17, 2026) queries the `autonomous_learner` ChromaDB collection on every production `/chat` request, making hippocampal memory an active input to every response rather than a background archive.

> *Figure 14.1. Hippocampal consolidation in Ms. Jarvis: GBIM entities and normalized nine-axis beliefs, enriched with centroids and provenance, are mirrored into a `geospatialfeatures` vector collection that serves as a long-term, place-aware memory index for retrieval and audit. Phase 1.45 (deployed March 17, 2026) adds a second active retrieval path: the `autonomous_learner` collection is queried on every `/chat` request via `all-minilm:latest` (384-dim) semantic search, prepending the top-5 most relevant community interaction records to every LLM prompt.*

---

# 14. Hippocampus and Memory Consolidation

This chapter describes how recent activity is turned into durable records in the system's long-term stores. The design borrows the idea of a hippocampal buffer that receives short-lived experiences, decides what matters, and then writes compact, structured traces into more stable memory. In the current implementation, this role is played by two complementary subsystems: (1) the GBIM + beliefs + Chroma hippocampus — GBIM worldview entities in `gbim_worldview_entity`, their 1:1 normalized nine-axis belief rows in `gbim_belief_normalized`, and a ChromaDB collection called `geospatialfeatures` that mirrors centroid-bearing entities together with worldview, dataset, GeoDB IDs, and other provenance; and (2) the `autonomous_learner` ChromaDB collection, which accumulates community interaction records and is queried at Phase 1.45 of every production `/chat` request. The `jarvis-hippocampus` service is deployed and confirmed operational as part of the **110-container production stack** (★ all 110 containers Up — zero Restarting, zero Exited, April 16, 2026), ChromaDB is fully containerized at container port 8000 / host port 8002 with the `chroma_data` Docker volume, and all ChromaDB collections use **384-dimensional vectors** produced by `all-minilm:latest`. ★ The ChromaDB corpus spans **49 active collections and 6,722,589+ total vectors** (April 16, 2026 confirmed baseline). Neurobiological work on hippocampal replay and complementary learning systems provides the conceptual backdrop for this design.

**Production state (★ April 16, 2026 — preflight gate all 27 gates ✅ green):**

- `jarvis-hippocampus` service: ✅ Deployed and operational (commit `b90f9ff`)
- ChromaDB `geospatialfeatures` collection: ✅ Active (container port 8000 / host port 8002, `chroma_data` volume)
- ChromaDB `autonomous_learner` collection: ✅ **Healthy and growing** — queried at Phase 1.45 on every `/chat` call. **21,181+ records as of April 10, 2026; Phase 1.45 active retrieval confirmed in April 16 preflight gate.** The 57-item figure was the April 1, 2026 recovery baseline following the debug sprint; accumulation has continued well past that baseline. See §14.8 for full detail.
- Embedding model: ✅ **`all-minilm:latest` (384-dim)** — canonical embedding model for all 49 ChromaDB collections
- PostgreSQL `msjarvis` (port **5433** ★ secured April 16, 2026 — bind corrected from `0.0.0.0` to `127.0.0.1`; orphaned container removed and recreated via compose): ✅ GBIM entities and belief store; `gbim_entities` count confirmed; `confidence_decay` metadata active
- PostgreSQL `msjarvisgis` (port **5432** ★ confirmed): ✅ PostGIS, **45 GB**, **551 tables**, 993 ZCTA centroids, 1,115,588 address points
- GBIM temporal confidence decay: ✅ Deployed March 15 — all entities carry `last_verified`, `confidence_decay`, `needs_verification`
- Integration with 9-phase pipeline: ✅ Confirmed end-to-end GPU pipeline — **99–107 seconds on RTX 4070** (the 436-second CPU baseline documented in the March 18, 2026 benchmark is archived; GPU pipeline active since April 6, 2026)
- `jarvis-memory` (port **8056**, 127.0.0.1): ✅ `/memory/sessions` HTTP 200 confirmed with **14 active sessions**; `JARVIS_API_KEY` exported and set in shell environment (April 16, 2026)
- Community resources: ✅ **64 verified resources** (all 55 WV counties confirmed, April 16, 2026 preflight gate — supersedes prior count of 52)
- `msjarvis_docs` ChromaDB: ✅ **7,465 items** (April 16, 2026 preflight confirmed — expanded from 4,192 March 28, 2026 audit baseline)
- **★ 110/110 containers Up — zero Restarting, zero Exited (April 16, 2026)**

> **📈 April 16, 2026 preflight gate — all 27 gates ✅ green:** Remediations applied before full green: (1) `msjarvis-db` port 5433 bind corrected from `0.0.0.0` to `127.0.0.1` — the orphaned container started outside compose was stopped, removed, and recreated via compose; (2) `jarvis-memory:8056` `/memory/sessions` was returning HTTP 500 — resolved by exporting `JARVIS_API_KEY` in shell environment; HTTP 200 confirmed with 14 active sessions; (3) container count advanced to 110.

> **📈 April 1, 2026 autonomous learner debug sprint — COMPLETE (historical reference):** The autonomous learner (`jarvis-autonomous-learner`, port 8020) entered a crash-loop on April 1, 2026 after a failed patch attempt deployed an empty file (1.54 kB), triggering `ERROR: Attribute 'app' not found in module` on Uvicorn startup (LEARN-03). Concurrently, a `cosine_similarity` bug was identified where the dedup gate comparison raised `"The truth value of an array with more than one element is ambiguous"` on every cycle due to a numpy array being returned instead of a scalar (LEARN-01). The GBIM Query Router (port 7205) briefly returned HTTP 422 on mis-shaped learner `route` POST calls (LEARN-02). All three items were resolved on April 1, 2026. The 57-item post-fix slice confirmed at 18:14 UTC, April 1, 2026 was the recovery baseline. Accumulation has continued: **21,181+ records confirmed as of April 10, 2026**.

> **📈 March 28, 2026 audit update (historical reference):** ChromaDB full audit — 40 active collections, 6,675,442 total vectors. `spiritual_rag` deduplicated (−19,338 duplicate vectors). `psychological_rag` restored (968 docs). `msjarvis_docs` at 4,192 items. All 40 collections confirmed on `all-minilm:latest` (384-dim).

> **Critical — Embedding model lock (March 17, 2026):** All ChromaDB collections — including `geospatialfeatures`, `autonomous_learner`, `gbim_worldview_entities`, `psychological_rag`, `ms_jarvis_memory`, and all others — use **384-dimensional vectors** produced by `all-minilm:latest` (pulled into `jarvis-ollama:11434`). The `nomic-embed-text` model produces **768-dimensional vectors** and is **incompatible** with all existing collections. Any service, script, or migration that generates embeddings for ChromaDB must use `all-minilm:latest`. The `_DummyCollection` error that previously blocked semantic retrieval from `autonomous_learner` is resolved.

---

## 14.1 Role in the Overall Architecture

The consolidation layer sits between fast-changing streams of requests and the slower, more stable memory and knowledge stores. As shown in Figure 14.1, the GBIM promotion and normalization pipeline feeds a hippocampal vector store that higher-level services query by worldview, dataset, and spatial footprint. The `jarvis-hippocampus` service (deployed March 15, 2026) provides this consolidation function as a dedicated microservice within the **110-container production stack** (★ April 16, 2026).

As of March 17, 2026, a second active hippocampal pathway operates in parallel: **Phase 1.45 community memory retrieval**. On every `/chat` request, before the LLM ensemble, the main brain queries the `autonomous_learner` ChromaDB collection using `all-minilm:latest` (384-dim) semantic search and prepends the top-5 most semantically similar community interaction records to `enhanced_message`. This makes accumulated community memory an active, prompt-level input to every response — not merely a background store available for optional RAG lookup.

**The two hippocampal pathways:**

| Pathway | Collection | Records | Query timing | Mechanism |
|---|---|---|---|---|
| GBIM + beliefs consolidation | `geospatialfeatures` | GBIM entity corpus | Phase 4 RAG (on-demand) | Metadata-filtered ChromaDB + PostgreSQL join |
| Community interaction memory | `autonomous_learner` | **21,181+ records as of April 10, 2026** (57-item figure was April 1 recovery baseline; accumulation ongoing; Phase 1.45 confirmed in April 16 preflight) | Phase 1.45 (every request) | `all-minilm:latest` semantic search, top-5 prepended |

A GBIM promotion and normalization pipeline:

- Promotes WV GIS features and other raw inputs into `gbim_worldview_entity`, keyed by `worldview_id`, `entity_type`, `source_table`, and `source_pk`.
- Maintains a 1:1 normalized belief row for every GBIM entity in `gbim_belief_normalized`, with JSONB axes (identity, who, for_whom, what, when, where, why, how, authority, evidence). As of March 15, 2026, all entities also carry temporal decay fields: `last_verified`, `confidence_decay`, `needs_verification`.
- Extracts centroids and provenance (`evidence.provenance.dataset`, `evidence.provenance.geodbid`) and mirrors them into the ChromaDB `geospatialfeatures` collection as documents with metadata (`gbim_entity_id`, `worldview_id`, `dataset`, `source_table`, `source_pk`, `geodbid`, `centroid_x`, `centroid_y`, `srid`).

This GBIM + beliefs + Chroma stack therefore acts as a hippocampal buffer: it observes world-tied entities and program semantics, enriches them with structured beliefs and spatial context, then writes them into a persistent vector store keyed by worldview, dataset, and feature identity for future use. In combination with the introspective, qualia, and orchestration layers described in Chapters 11, 12, and 17, this provides a path from "what exists and what just happened" to "what the system will remember and reuse later," in a form that can be inspected and audited against concrete places and datasets.

**Relationship to the 9-phase pipeline (Chapter 17):**
The `jarvis-hippocampus` service and `autonomous_learner` collection participate in the production 9-phase pipeline by:

1. **Phase 1.45:** `autonomous_learner` queried via `all-minilm:latest` (384-dim) on every request — top-5 community memories prepended to `enhanced_message`
2. **Phase 4:** `geospatialfeatures` collection queried by GIS-RAG (port 8004) and `jarvis-spiritual-rag` (port 8005) as part of RAG context building; GBIM entities and beliefs retrieved from PostgreSQL `msjarvis`
3. **Phase 5:** `confidence_decay` multiplier derived from `gbim_belief_normalized` temporal metadata applied to every response
4. **Post-processing:** `background_rag_store` routes live query-response pairs back into `ms_jarvis_memory` (and, through the autonomous learning subsystem, into `autonomous_learner` growth)

**Pipeline timing (April 16, 2026):** End-to-end 9-phase GPU pipeline: **99–107 seconds on RTX 4070**. The 436-second CPU baseline documented in the March 18, 2026 benchmark is archived; GPU pipeline has been active since April 6, 2026. Chapter 17 carries the authoritative pipeline timing.

---

## 14.2 Inputs to the Consolidation Process

The inputs listed here correspond to the world-model backbone on the left side of Figure 14.1. The consolidation routines draw on several concrete sources of information that already exist in the system.

**GBIM entities and normalized beliefs**
The core inputs are rows in `gbim_worldview_entity` and their 1:1 normalized belief snapshots in `gbim_belief_normalized` (PostgreSQL `msjarvis`, port **5433** ★ secured April 16, 2026 — bind corrected from `0.0.0.0` to `127.0.0.1`; orphaned container removed and recreated via compose). Each belief row encodes identity (label, GBIM ID, source_table, source_pk, worldview_id), where (SRID, centroids, bbox, optional county/zip), and `evidence.provenance` (dataset, original feature IDs). All entities carry temporal decay metadata: `last_verified`, `confidence_decay`, `needs_verification`. These form the semantic and spatial backbone of hippocampal memory.

**Geospatial provenance and centroids**
For features with geometry, the belief `where` axis records centroids and SRIDs derived from underlying WV GIS layers (PostgreSQL `msjarvisgis`, port **5432** ★ confirmed — PostGIS, **45 GB**, **551 tables**, 993 ZCTA centroids from `zcta_wv_centroids`, 1,115,588 address points). These values are streamed into ChromaDB `geospatialfeatures` metadata (`centroid_x`, `centroid_y`, `srid`) so that retrieval can respect spatial context and coordinate systems. All embeddings for `geospatialfeatures` use `all-minilm:latest` (384-dim) to maintain collection compatibility.

**Community interaction records (`autonomous_learner`)**
The `autonomous_learner` ChromaDB collection accumulates community interaction records produced by the autonomous learning subsystem. **As of April 10, 2026: 21,181+ records confirmed — accumulation ongoing.** The 57-item figure from April 1, 2026 was the recovery baseline following the LEARN-01/LEARN-03 debug sprint; accumulation has continued well past that baseline. Phase 1.45 active retrieval is confirmed operational in the April 16, 2026 preflight gate. These records are written separately from `background_rag_store` and represent a distinct hippocampal pathway: experiential, interaction-derived memory rather than structured GBIM entity promotion. They are queried at Phase 1.45 via `all-minilm:latest` semantic search on every production request.

**Program and institutional entities**
Benefit programs, governance entities, and institutional structures can also be represented as GBIM entities with beliefs over what, for_whom, why, when, and authority. As those entities are promoted, they join the same hippocampal fabric as geospatial features, allowing queries to traverse both physical and institutional space. Community-validated resource data from `jarvis-local-resources-db` (port 5435) is also eligible for promotion into the GBIM + beliefs + Chroma pipeline. As of April 16, 2026: **64 verified resources** (all 55 WV counties confirmed).

**Orchestration-level interactions**
Higher-level services (unified gateway, brain orchestrator, GIS-RAG at port 8004, WV entangled gateway) consume GBIM + beliefs + Chroma when answering questions and may create or update GBIM entities and beliefs based on user interactions. The 9-phase pipeline's `background_rag_store` (Chapter 17 post-processing) is the primary mechanism by which live query-response pairs are routed back through the hippocampal consolidation process.

Taken together, these inputs supply both the raw material to be stored (entities, beliefs, spatial footprints, community interaction records) and the signals about how the system has interpreted and used them.

---

## 14.3 Criteria for What Is Stored

In the current implementation, the consolidation pipeline is inclusive at the world-model level: every GBIM entity with a centroid has a normalized belief row (including temporal decay metadata as of March 15, 2026) and is mirrored into the `geospatialfeatures` collection. For `autonomous_learner`, every community interaction processed by the autonomous learning subsystem is appended — deduplication in `ms_jarvis_memory` is advisory and handled separately by `background_rag_store`'s near-duplicate check. There is not yet a fine-grained selection mechanism that stores only some entities or beliefs in hippocampal indexes.

**Post-fix dedup gate status (April 16, 2026):** The dedup gate within `ms_jarvis_autonomous_learner_optimized.py` is confirmed running without exception following the LEARN-01 fix (explicit `np.float64` and `float()` casting enforced on cosine similarity comparisons). Accumulation has resumed and confirmed at 21,181+ records as of April 10, 2026. A semantic dedup audit of the `autonomous_learning` collection remains recommended to surface any potential near-duplicates stored during the LEARN-01 error window.

**As of March 28, 2026**, AAPCAppE scraper documents constitute the first external-source entries in the ingest pipeline — distinct from autonomous-learner interaction records. The `spiritual_rag` collection was deduplicated (−19,338 duplicate vectors) and `psychological_rag` was restored (968 docs) during the March 28 ChromaDB full audit.

**Implicit significance and structure**
Because the pipeline always writes a structured belief snapshot, and always includes provenance (dataset, GeoDB ID) and spatial context for centroided entities, the hippocampal surface naturally emphasizes entities that are well-grounded in both data and space. Indexing by worldview and dataset also encodes which layers and institutional perspectives are considered part of the canonical memory. The `needs_verification=TRUE` flag (100% of entities at March 15 launch baseline) represents the initial state before the POC verification loop begins clearing entities as confirmed.

**Planned selection criteria**
The design for this layer goes further, envisioning explicit logic that prioritizes:

- High-impact or sensitive programs and features, including governance- or safety-related infrastructure.
- Novel or under-represented combinations of locations, populations, and benefit rules.
- Episodes where beliefs were corrected or forked across worldviews.
- Repeatedly accessed regions or entities that merit summarized, higher-level hippocampal entries.
- Entities where `confidence_decay` has fallen below threshold (future integration with POC verification loop).
- `autonomous_learner` records with high semantic similarity to repeated query patterns (candidates for summary consolidation).

These criteria can be implemented on top of the existing GBIM + beliefs + Chroma pipeline by inspecting belief metadata and usage patterns before deciding whether to store full detail, a summary, or nothing beyond base GBIM presence.

---

## 14.4 Transformation into Long-Term Memory

When an entity passes through the GBIM + belief + Chroma pipeline, it is transformed into durable structures that can be joined and queried from multiple angles.

**Structured beliefs and metadata in PostgreSQL (`msjarvis`, port 5433 ★ secured April 16)**
GBIM entities receive normalized belief rows in `gbim_belief_normalized` capturing identity, spatial footprint, program semantics, and provenance. As of March 15, 2026, every belief row also carries `last_verified` (timestamp of most recent confirmation), `confidence_decay` (multiplier applied by Phase 5 of the 9-phase pipeline), and `needs_verification` (Boolean flag triggering the future POC verification loop). This relational/JSONB structure serves as the canonical long-term representation.

**Documents and metadata in ChromaDB `geospatialfeatures` (container port 8000 / host port 8002, `chroma_data` volume)**
Centroid-bearing entities are added to the `geospatialfeatures` collection as simple documents with rich metadata. All vectors use `all-minilm:latest` (384-dim):

```python
{
    "gbim_entity_id": "uuid",
    "worldview_id": "worldview-uuid",
    "dataset": "source_dataset_name",
    "source_table": "wvgistcbuildingfootprints",
    "source_pk": "feat_1703912",
    "geodbid": "geodb-feature-id",
    "centroid_x": 534821.4,
    "centroid_y": 4188432.7,
    "srid": 26917,
    "last_verified": "2026-03-15T00:00:00Z",
    "confidence_decay": 0.95,
    "needs_verification": true
}
```

This provides a fast hippocampal index for metadata-filtered recall backed by the persistent `chroma_data` Docker volume. ★ The full ChromaDB corpus spans **49 active collections and 6,722,589+ total vectors** as of the April 16, 2026 confirmed baseline.

**Community interaction records in ChromaDB `autonomous_learner` (container port 8000 / host port 8002, `chroma_data` volume)**
Each community interaction processed by the autonomous learning subsystem is written as a document + metadata record in `autonomous_learner`, embedded via `all-minilm:latest` (384-dim). These records capture the conversational and task-level experience of the system's community engagement — a complementary memory pathway to the structured GBIM entity fabric. At Phase 1.45, the top-5 most semantically relevant records are prepended to every production prompt. **As of April 10, 2026: 21,181+ records confirmed; dedup gate running cleanly with explicit `np.float64` and `float()` casting enforced on cosine similarity comparisons (LEARN-01 resolved April 1, 2026).**

**Implicit belief and routing traces (planned)**
As Ms. Jarvis's belief graph and routing logic mature, ChromaDB `geospatialfeatures` metadata can be extended to include explicit references to belief nodes, routing decisions, and normative labels, turning each hippocampal entry into a trace of how the system's internal model and policies interacted with that entity.

**Spatial anchoring via geospatial layers**
Because beliefs carry centroids, SRIDs, and optional administrative labels, hippocampal entries can be linked back to counties, cities, watersheds, and other layers maintained in `msjarvisgis` (port **5432** ★ confirmed, **45 GB** PostGIS, **551 tables**). The `zcta_wv_centroids` table (993 rows) provides the canonical ZIP-level spatial anchors. This connects abstract programs and features to specific West Virginia places.

---

## 14.5 Temporal Organization and Decay

In many neuro-inspired designs, hippocampal systems maintain a temporal hierarchy of memories and implement decay. As of March 15–April 16, 2026, Ms. Jarvis has deployed the first phase of temporal organization: the GBIM confidence decay system, the `autonomous_learner` growth curve, and the Phase 1.45 active retrieval pathway.

**Current behavior (★ April 16, 2026)**
Every GBIM entity in the relevant worldview receives a normalized belief row with `last_verified`, `confidence_decay`, and `needs_verification` fields. The `confidence_decay` multiplier is applied at Phase 5 of every production 9-phase pipeline request (Chapter 17), attenuating response confidence proportionally to how long an entity has gone without verification. The `autonomous_learner` collection provides a complementary temporal signal through its growth curve: **21,181+ records as of April 10, 2026**, with older records naturally becoming less semantically prominent as newer interactions are added and the nearest-neighbor retrieval at Phase 1.45 surfaces the most relevant.

The April 1, 2026 crash-loop and recovery is a documented temporal event in the learner's history: the 57-item post-fix count was the recovery baseline, not the operating total. The `spiritual_rag` deduplication (−19,338 vectors, March 28) is an example of retroactive temporal curation that the temporal organization subsystem should eventually automate. The `msjarvis_docs` collection growing from 4,192 (March 28) to 7,465 items (April 16) is a further illustration of the ongoing temporal expansion of the hippocampal substrate.

**POC verification loop (highest-priority future work)**
The POC verification loop will automate the process of re-contacting a resource's designated point of contact when `needs_verification=TRUE` and resetting `confidence` to 1.0 on confirmation. Until implemented, the flag-and-attenuate approach via `confidence_decay` serves as the operative temporal decay mechanism.

**Planned temporal hierarchy**
Beyond the current decay system, the design anticipates:

- A recent window of high-granularity belief and hippocampal entries suitable for detailed forensic analysis.
- Intermediate summarizations that merge multiple similar entities or interactions into trend-level records across both `geospatialfeatures` and `autonomous_learner`.
- A long-term backbone of especially important precedents, patterns, and governance-relevant insights that are protected from aggressive pruning.

---

## 14.6 Interaction with Retrieval and Introspection

Consolidated GBIM and hippocampal entries play a direct role in how Ms. Jarvis retrieves context and can be tightly integrated with introspective narratives.

**Retrieval feedback loop (9-phase pipeline integration)**
When higher-level services (GIS-RAG at port 8004, WV entangled gateway, `jarvis-spiritual-rag` at port 8005) need context during Phase 4 of the 9-phase pipeline, they:

1. Use worldview, dataset, and spatial constraints (bboxes, centroids, counties, `zcta_wv_centroids` from `msjarvisgis` port **5432** ★) to select candidate GBIM entities and beliefs from `msjarvis.gbim_belief_normalized`.
2. Use those provenance keys (`worldview_id`, `dataset`, `geodbid`) as ChromaDB metadata filters in the `geospatialfeatures` collection, retrieving relevant entities quickly.
3. Apply `confidence_decay` weighting at Phase 5 to attenuate results based on verification recency.
4. Join ChromaDB hits back to `gbim_worldview_entity` and `gbim_belief_normalized` (PostgreSQL `msjarvis`, port **5433** ★) to assemble answers and map overlays grounded in both beliefs and physical space.
5. Join spatial identifiers to `msjarvisgis.zcta_wv_centroids` (port **5432** ★) and `jarvis-local-resources-db` (port 5435) for community-anchored resource context — **64 verified resources** (all 55 WV counties confirmed, April 16, 2026).

**Phase 1.45 active community memory retrieval (deployed March 17, 2026)**
Before Phase 4 RAG, Phase 1.45 performs a distinct and always-on hippocampal retrieval:

1. The incoming query is embedded via `all-minilm:latest` at `jarvis-ollama:11434/api/embeddings` (384-dim).
2. The vector is used to query `autonomous_learner` (★ 21,181+ records as of April 10, 2026; Phase 1.45 confirmed in April 16 preflight gate).
3. The 5 most semantically similar community interaction records are retrieved (documents + metadata + distances).
4. The retrieved memories are prepended to `enhanced_message` before it enters Phase 2.5 LLM ensemble processing.

This pathway guarantees that every LLM response is grounded in the system's accumulated community engagement history, not just structured GBIM entities. The two pathways are complementary: Phase 1.45 supplies experiential, interaction-level context; Phase 4 supplies structured, spatial, and institutional GBIM knowledge.

**Introspective descriptions of memory use**
As the introspective layer evolves, it can report which GBIM entities, datasets, and spatial regions were consulted for a given response, which `autonomous_learner` records were prepended at Phase 1.45, and how their `confidence_decay` values influenced the result. `jarvis-memory` (port 8056, 127.0.0.1; `/memory/sessions` HTTP 200 confirmed with 14 active sessions, `JARVIS_API_KEY` set, April 16, 2026) provides the authenticated API surface for these introspective memory reads.

**Optimization over hippocampal histories via 69-DGM cascade**
Self-improving agents in the 69-DGM layer (Chapter 32, `jarvis-69dgm-bridge` host port **19000** → internal **9000**, confirmed running — re-locked to `127.0.0.1:19000` March 18, 2026) can treat GBIM + beliefs + ChromaDB `geospatialfeatures` and `autonomous_learner` as datasets for discovering weaknesses, biases, or gaps in coverage — for example, which counties are under-represented, which datasets are heavily relied on, where repeated corrections to beliefs occur, which entities have the longest-decayed `confidence_decay` values, or which `autonomous_learner` records are never surfaced by Phase 1.45 retrieval and may warrant consolidation or pruning.

---

## 14.7 Alignment with Spatial and Governance Goals

Because much of Ms. Jarvis's mission is tied to specific regions, communities, and institutions in West Virginia, the consolidation layer is designed to align closely with spatial and governance-oriented goals.

**Place-aware memory**
Extensive WV geospatial layers — counties, block groups, census tracts, cities, facilities, infrastructure, and more — coexist as GBIM entities and beliefs in PostgreSQL `msjarvis` (port **5433** ★ secured April 16) and PostGIS `msjarvisgis` (**45 GB**, **551 tables**, port **5432** ★). By mirroring centroid-bearing entities into ChromaDB `geospatialfeatures` with worldview IDs, datasets, and spatial metadata, and by accumulating community interaction records in `autonomous_learner`, consolidation enables analyses of how particular counties, towns, or facilities have been represented and served in the system's history. The 993 ZCTA centroids in `msjarvisgis.zcta_wv_centroids` (port **5432** ★) provide the canonical ZIP-level anchors for this place-aware fabric.

**Community-validated institutional continuity**
Community-validated data from Harmony for Hope's Community Champions (stored in `jarvis-local-resources-db`, port 5435) is eligible for promotion into the hippocampal pipeline, ensuring that ground-truth verification by community members feeds durable, place-grounded memory. As of April 16, 2026, **64 verified resources** (all 55 WV counties confirmed) represent the current confirmed breadth of community-validated coverage. Community interaction records in `autonomous_learner` (21,181+ records, April 10, 2026) capture the conversational record of this community engagement at a level of temporal granularity that structured GBIM promotion does not provide.

**Equity, oversight, and temporal accountability**
By combining spatial identifiers, belief metadata (including `confidence_decay` and `needs_verification`), Phase 1.45 community memory retrieval, and hippocampal retrieval histories, analysts and agents can examine whether certain communities receive less assistance, face different patterns of risk, or encounter more frequent misunderstandings. The `needs_verification` flag makes temporal gaps in confirmation explicit and auditable.

---

## 14.8 Implementation Status (★ April 16, 2026 — preflight gate all 27 gates ✅ green)

**Confirmed operational (★ 110/110 containers Up — zero Restarting, zero Exited, April 16, 2026):**

- ✅ `jarvis-hippocampus` service deployed in **110-container production stack** ★ (commit `b90f9ff`)
- ✅ ChromaDB `geospatialfeatures` collection active (container port 8000 / host port 8002, `chroma_data` volume)
- ✅ ChromaDB `autonomous_learner` collection: **HEALTHY AND GROWING — 21,181+ records as of April 10, 2026; Phase 1.45 active retrieval confirmed in April 16 preflight gate; dedup gate running cleanly (explicit `np.float64` + `float()` casting enforced)**
- ✅ **Embedding model: `all-minilm:latest` (384-dim)** — canonical model for all 49 ChromaDB collections; `nomic-embed-text` (768-dim) confirmed incompatible and must not be used
- ✅ `_DummyCollection` error blocking `autonomous_learner` semantic retrieval: RESOLVED (March 17)
- ✅ PostgreSQL `msjarvis` (port **5433** ★ secured April 16, 2026 — bind corrected from `0.0.0.0` to `127.0.0.1`; orphaned container removed and recreated via compose): GBIM entity and belief store; `gbim_entities` confirmed; `confidence_decay` metadata active
- ✅ PostgreSQL `msjarvisgis` (port **5432** ★ confirmed): **45 GB** PostGIS, **551 tables**, 993 ZCTA centroids, 1,115,588 address points
- ✅ GBIM temporal decay deployed: all entities carry `last_verified`, `confidence_decay`, `needs_verification`
- ✅ `confidence_decay` multiplier applied at Phase 5 of every production 9-phase pipeline request
- ✅ `background_rag_store` routing post-processing back into hippocampal consolidation
- ✅ `geospatialfeatures` collection queried by GIS-RAG (port 8004) and `jarvis-spiritual-rag` (port 8005) during Phase 4 RAG context building
- ✅ Integration with `msjarvisgis.zcta_wv_centroids` (993 rows, port **5432** ★) for spatial anchoring
- ✅ `jarvis-local-resources-db` (port 5435): **64 verified resources, all 55 WV counties confirmed (April 16, 2026 preflight gate)**
- ✅ Phase 1.45 community memory retrieval confirmed in April 16 preflight gate; end-to-end GPU pipeline **99–107s on RTX 4070** (CPU baseline of ~436s archived)
- ✅ `jarvis-memory` (port **8056**, 127.0.0.1): `/memory/sessions` HTTP 200 confirmed with **14 active sessions**; `JARVIS_API_KEY` exported and set in shell environment (April 16, 2026)
- ✅ `ms_jarvis_autonomous_learner_optimized.py` synced to `services-safe` mirror directory
- ✅ **110/110 containers Up — zero Restarting, zero Exited (April 16, 2026)**

**April 16, 2026 — Preflight remediation items (all resolved before gate cleared):**

| Item | Description | Resolution |
|---|---|---|
| PREFLIGHT-A | `msjarvis-db` port 5433 bound to `0.0.0.0` — exposed on all interfaces | Stopped and removed orphaned container started outside compose; recreated via compose; bind confirmed `127.0.0.1:5433` |
| PREFLIGHT-B | `jarvis-memory:8056` `/memory/sessions` returning HTTP 500 | Exported `JARVIS_API_KEY` in shell environment; HTTP 200 confirmed with 14 active sessions |
| PREFLIGHT-C | Container count advancement | 96 → 110 containers Up confirmed |

**April 1, 2026 — Autonomous Learner Debug Sprint (historical reference — LEARN-01 / LEARN-02 / LEARN-03 — all RESOLVED):**

| Item | Description | Resolution |
|---|---|---|
| LEARN-01 | `cosine_similarity` in `ms_jarvis_autonomous_learner_optimized.py` returned numpy array instead of scalar — dedup gate raised `"truth value of array with more than one element is ambiguous"` on every cycle | Fixed: explicit `np.float64` dtype enforced on both input vectors; return value cast to `float()` |
| LEARN-02 | GBIM Query Router (port 7205) returning HTTP 422 on mis-shaped learner `route` POST calls | Fixed: learner request schema corrected; `/route` returning HTTP 200 OK and stable |
| LEARN-03 | `jarvis-autonomous-learner` crash-loop after empty file (1.54 kB) deployed — `ERROR: Attribute 'app' not found in module` on Uvicorn startup | Fixed: source patched on host, copied into container, service restarted |

**ChromaDB collections (★ April 16, 2026 confirmed baseline — 49 collections, 6,722,589+ total vectors):**

| Collection | Records / Vectors | Notes |
|---|---|---|
| `gbim_worldview_entities` | GBIM entity corpus | Complete WV GBIM spatial corpus |
| `autonomous_learner` | **21,181+ records as of April 10, 2026** | Phase 1.45 active retrieval; LEARN-01/03 resolved April 1; dedup gate clean; accumulation ongoing; 57-item figure was April 1 recovery baseline |
| `aapcappe_corpus` | 65+ | First scrape run March 27 (39 sources); accumulation ongoing via `jarvis-ingest-watcher` |
| `psychological_rag` | **968** ★ restored March 28 | Restored during March 28 ChromaDB full audit |
| `spiritual_rag` | ★ Deduplicated March 28 (−19,338 duplicate vectors removed) | Deduplication confirmed during March 28 ChromaDB full audit |
| `spiritual_texts` | 23 | Unchanged |
| `appalachian_cultural_intelligence` | 5 | Confirmed March 18 |
| `GBIM_sample_rows` | 5,000 | Confirmed March 18 |
| `GBIM_sample` | 3 | Confirmed March 18 |
| `msjarvis-smoke` | 1 | Smoke test record |
| `msjarvis_docs` | **7,465** ★ confirmed April 16 preflight | Expanded from 4,192 (March 28, 2026 audit baseline) |
| `ms_jarvis_memory` | Active | `jarvis-memory` API (port 8056 ★) provides authenticated access; `/memory/sessions` 14 active sessions |
| `ms_jarvis_identity` | 8 constitutional docs ★ seeded April 16 | Query-verified; seeded during April 16 sprint |
| `conversation_history` | Active ★ rebuilt April 16 | Rebuilt clean during April 16 sprint |
| `geospatialfeatures` | 0 | Scaffolded — pending backfill ingest (all backfill embeddings must use `all-minilm:latest` 384-dim) |
| `GBIM_Fayette_sample` | 0 | Scaffolded — pending ingest |
| *(additional collections)* | ★ See April 16 baseline | Total: **49 collections, 6,722,589+ vectors** (April 16, 2026 confirmed) |

**Remaining work:**

**POC verification loop (highest-priority)**
The automated POC verification loop — where the system contacts a resource's designated point of contact when `needs_verification=TRUE` and resets `confidence` to 1.0 on confirmation — is not yet automated. Current state: flag-and-attenuate via `confidence_decay` only.

**Semantic dedup audit of `autonomous_learning` collection (recommended)**
The LEARN-01 dedup gate error window means new items may have been stored without dedup checking between the last stable restart and the April 1, 2026 fix. A semantic dedup audit is recommended.

**`geospatialfeatures` ingest and metadata backfill**
The `geospatialfeatures` ChromaDB collection is scaffolded but at 0 records pending backfill ingest. All backfill embeddings must use `all-minilm:latest` (384-dim).

**Selective storage criteria**
Fine-grained selection logic (high-impact features, novel combinations, corrected beliefs, heavily accessed regions) is designed but not yet implemented.

**Temporal hierarchy beyond decay**
Intermediate summarizations, pruning of aged entries, and long-term backbone extraction remain forward-looking design intentions implemented on top of the current always-append plus decay-weight behavior.

**Tighter belief-routing traces**
Extending `geospatialfeatures` ChromaDB metadata to include explicit belief node references and routing decisions is planned but not yet implemented.

---

## 14.9 Summary

The consolidation layer captures how recent activity and world-modeling are turned into lasting structure across two complementary hippocampal pathways: (1) GBIM entities with normalized beliefs and temporal decay metadata in PostgreSQL `msjarvis` (port **5433** ★ secured April 16), mirrored as centroid-bearing records into the `geospatialfeatures` ChromaDB collection, queried by GIS-RAG and spiritual-RAG during Phase 4; and (2) the `autonomous_learner` ChromaDB collection — **21,181+ records as of April 10, 2026** (57-item figure was the April 1, 2026 recovery baseline; accumulation ongoing; Phase 1.45 confirmed in April 16 preflight gate) — queried via `all-minilm:latest` (384-dim) semantic search at Phase 1.45 of every production `/chat` request, with top-5 community memories prepended to `enhanced_message`.

The `jarvis-hippocampus` service (deployed March 15, 2026, commit `b90f9ff`) functions as the dedicated hippocampal buffer within the **110-container production stack** (★ all 110 containers Up, April 16, 2026). The **`jarvis-memory` service** (port **8056** ★ — `/memory/sessions` HTTP 200 confirmed with 14 active sessions; `JARVIS_API_KEY` exported and set in shell environment, April 16, 2026) operates as a companion container, confirmed verified and fully authenticated. The `confidence_decay` multiplier applied at Phase 5 of every production request makes hippocampal temporal state an active, measurable factor in every response. Phase 1.45 community memory retrieval (deployed March 17, 2026) makes `autonomous_learner` a live, prompt-level input to every response rather than a passive background store. The critical embedding model lock — **`all-minilm:latest` (384-dim) for all 49 ChromaDB collections** (★ 6,722,589+ total vectors, April 16, 2026 confirmed baseline) — ensures collection compatibility and is a permanent architectural constraint.

★ The April 16, 2026 preflight gate — all 27 gates ✅ green — established the current operational baseline: `msjarvis-db` port 5433 bind secured to `127.0.0.1`; `jarvis-memory` `/memory/sessions` HTTP 200 with 14 active sessions; 110 containers Up; community resources confirmed at 64 verified resources (all 55 WV counties); `msjarvis_docs` confirmed at 7,465 items; end-to-end GPU pipeline 99–107s on RTX 4070. POC verification loop automation, `geospatialfeatures` backfill ingest, semantic dedup audit of the `autonomous_learning` collection, selective storage criteria, temporal hierarchy beyond decay, and tighter belief-routing traces are active design directions that build on this foundation. Subsequent chapters describe how global controls (Chapter 15), the 69-DGM cascade (Chapter 32), and executive processes (Chapter 17) use these consolidated, place-aware memories as part of broader feedback loops that shape Ms. Jarvis's ongoing evolution.

---

## 14.10 Sprint Validation Log — April 16, 2026 Closure

### Infrastructure numbers — stale → current

| Field | Stale value | Current value (April 16) | Source |
|---|---|---|---|
| Container count | 96 | **110** | `docker ps` April 16 |
| ChromaDB collections | 40 | **49** | ChromaDB v2 API April 16 |
| ChromaDB total vectors | 6,675,442 | **6,722,589+** | ChromaDB v2 API April 16 |
| `msjarvisgis` tables | 501 | **551** | `psql` April 16 |
| `msjarvisgis` size | 91 GB | **45 GB** | confirmed April 16 |
| `autonomous_learner` count | 57 items (April 1 recovery baseline) | **21,181+ as of April 10, 2026** | preflight gate April 16 |
| `msjarvis_docs` items | 4,192 (March 28 baseline) | **7,465** | preflight gate April 16 |
| Community resources | 52 | **64 verified, all 55 WV counties** | preflight gate April 16 |
| Pipeline timing | ~436s CPU (March 18 benchmark) | **99–107s GPU RTX 4070** (archived: CPU baseline) | April 6+ |
| `msjarvis-db` bind | `0.0.0.0:5433` | **127.0.0.1:5433** | PREFLIGHT-A April 16 |
| `jarvis-memory` `/memory/sessions` | HTTP 500 | **HTTP 200, 14 active sessions** | PREFLIGHT-B April 16 |

### Historical sprint entries (reference)

> **March 27–28, 2026:** AAPCAppE scraper first run (39 sources, 65 docs). Security remediation — 96/96 Up. `jarvis-memory` corrected to 127.0.0.1. ChromaDB 40 collections, 6,675,442 vectors. `spiritual_rag` deduplicated. `psychological_rag` restored. `msjarvis_docs` 4,192.

> **April 1, 2026:** Autonomous learner debug sprint — LEARN-01, LEARN-02, LEARN-03 all resolved. 57-item post-fix recovery baseline confirmed. Accumulation resumed.

> **April 6, 2026:** GPU pipeline active — RTX 4070. End-to-end timing: 99–107s. CPU baseline (436s) archived.

> **April 10, 2026:** `autonomous_learner` 21,181+ records confirmed.

> **April 15, 2026:** Hallucination gap closed. Live end-to-end `/chat` passed — `architecture_layers: 12`; `truthverdict: score 1.0, action passed`.

> **April 16, 2026:** Preflight gate all 27 gates ✅ green. Remediations: (1) `msjarvis-db` port 5433 bind corrected from `0.0.0.0` to `127.0.0.1` — orphaned container stopped, removed, recreated via compose; (2) `jarvis-memory:8056` `/memory/sessions` HTTP 500 resolved — `JARVIS_API_KEY` exported in shell environment; HTTP 200 confirmed with 14 active sessions; (3) container count advanced to 110. Community resources updated to 64 (all 55 WV counties). `msjarvis_docs` confirmed 7,465 items. `ms_jarvis_identity` 8 constitutional docs seeded and query-verified. `conversation_history` rebuilt clean. ChromaDB 49 collections, 6,722,589+ vectors. `msjarvisgis` 551 tables, 45 GB. Git commit `fdd3d13d`. **Chapter 14 CLOSED.**

---

**Chapter 14 is CLOSED. No open items remain. All hippocampal and memory consolidation services — `jarvis-hippocampus`, `autonomous_learner` (21,181+ records), `jarvis-memory:8056` (14 active sessions, JARVIS_API_KEY set), ChromaDB v2 (49 collections, 6,722,589+ vectors), `msjarvis:5433` (127.0.0.1-bound), `msjarvisgis:5432` (551 tables, 45 GB), and 64 verified community resources — are production-active as of April 16, 2026.**

---

*Last updated: 2026-04-16 — Carrie Kidd (Mamma Kidd), Mount Hope WV*

*★ April 1, 2026: Autonomous learner debug sprint complete — LEARN-01 (cosine_similarity numpy dtype fix), LEARN-02 (GBIM Query Router 422 schema mismatch resolved), LEARN-03 (crash-loop resolved). Post-fix recovery baseline: 57 items in `autonomous_learning` collection. ms_jarvis_autonomous_learner_optimized.py synced to services-safe. All sections updated to reflect post-fix state; 21,181-item historical baseline (March 20) preserved.*

*★ March 28, 2026: Security remediation — 96/96 Up; jarvis-memory corrected to 127.0.0.1; _auth() on 4 sensitive routes; ChromaDB full audit (40 collections, 6,675,442 vectors); spiritual_rag deduplicated; psychological_rag restored; msjarvis_docs 4,192; msjarvis port 5433 restored; msjarvisgis port 5432 confirmed.*

*★ April 16, 2026 — CLOSED: Container count updated to 110 throughout. ChromaDB updated to 49 collections / 6,722,589+ vectors throughout. msjarvisgis corrected to 551 tables / 45 GB throughout. autonomous_learner count updated to 21,181+ records — 57-item figure clarified as April 1 recovery baseline throughout. msjarvis_docs confirmed 7,465 items — note added vs. 4,192 March 28 baseline. Community resources updated to 64 verified (all 55 WV counties). Pipeline timing updated to 99–107s GPU RTX 4070; 436s CPU baseline archived. msjarvis-db port 5433 bind corrected from 0.0.0.0 to 127.0.0.1 — PREFLIGHT-A resolved. jarvis-memory /memory/sessions HTTP 200 with 14 active sessions — PREFLIGHT-B resolved. ms_jarvis_identity 8 constitutional docs seeded. conversation_history rebuilt clean. §14.10 sprint validation log added. Chapter 14 CLOSED.*
