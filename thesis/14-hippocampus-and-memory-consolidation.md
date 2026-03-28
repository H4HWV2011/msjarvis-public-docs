# 14. Hippocampus and Memory Consolidation

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*

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

This chapter describes how recent activity is turned into durable records in the system's long-term stores. The design borrows the idea of a hippocampal buffer that receives short-lived experiences, decides what matters, and then writes compact, structured traces into more stable memory. In the current implementation, this role is played by two complementary subsystems: (1) the GBIM + beliefs + Chroma hippocampus — GBIM worldview entities in `gbim_worldview_entity`, their 1:1 normalized nine-axis belief rows in `gbim_belief_normalized`, and a ChromaDB collection called `geospatialfeatures` that mirrors centroid-bearing entities together with worldview, dataset, GeoDB IDs, and other provenance; and (2) the `autonomous_learner` ChromaDB collection, which accumulates community interaction records and is queried at Phase 1.45 of every production `/chat` request. The `jarvis-hippocampus` service is deployed and confirmed operational as part of the **96-container production stack** (★ all 96 containers Up — zero Restarting, zero Exited, March 28, 2026), ChromaDB is fully containerized at port 8000 with the `chroma_data` Docker volume, and all ChromaDB collections use **384-dimensional vectors** produced by `all-minilm:latest`. ★ The ChromaDB corpus now spans **40 active collections and 6,675,442 total vectors** (March 28, 2026 full audit). Neurobiological work on hippocampal replay and complementary learning systems provides the conceptual backdrop for this design.

**Production state (★ March 28, 2026):**

- `jarvis-hippocampus` service: ✅ Deployed and operational (commit `b90f9ff`)
- ChromaDB `geospatialfeatures` collection: ✅ Active (port 8000, `chroma_data` volume)
- ChromaDB `autonomous_learner` collection: ✅ Growing — queried at Phase 1.45 on every `/chat` call (★ see §14.8 for updated March 28 vector counts)
- Embedding model: ✅ **`all-minilm:latest` (384-dim)** — canonical embedding model for ★ all 40 ChromaDB collections
- PostgreSQL `msjarvis` (port **5433** ★ restored): ✅ 5,416,521 GBIM entities, 80 epochs, 206 source layers
- PostgreSQL `msjarvisgis` (port **5432** ★ confirmed): ✅ 91 GB PostGIS, 501 tables, 993 ZCTA centroids
- GBIM temporal confidence decay: ✅ Deployed March 15 — all entities carry `last_verified`, `confidence_decay`, `needs_verification`
- Integration with 9-phase pipeline: ✅ Confirmed in end-to-end benchmark (~436s, March 18, 2026, optimized from 532s baseline)
- `jarvis-memory` (port **8056**): ✅ ★ Corrected from `0.0.0.0` to `127.0.0.1` March 28, 2026; `_auth()` confirmed on 4 sensitive routes; `JARVIS_API_KEY` confirmed set
- **★ 96/96 containers Up — zero Restarting, zero Exited (March 28, 2026)**

> **📈 March 28, 2026 audit update:** ChromaDB full audit complete — **40 active collections, 6,675,442 total vectors**. `spiritual_rag` deduplicated (−19,338 duplicate vectors). `psychological_rag` restored (968 docs). `msjarvis_docs` expanded (4,192 items). `autonomous_learner` continues to grow (first external-source AAPCAppE documents flowing as of March 27). All 40 collections confirmed on `all-minilm:latest` (384-dim). See §14.8 for the updated full collection table.

> **📈 March 27, 2026 sprint update:** 65 additional documents confirmed in Chroma from AAPCAppE scraper first run (`jarvis-ingest-watcher`). RAG confirmed loading 53 documents (7 new base cultural docs). `autonomous_learner` collection trajectory: first external-source documents now flowing. Scraper reporting 39 sources, `total_runs: 1`. See §14.8 for updated collection table.

> **Critical — Embedding model lock (March 17, 2026):** All ChromaDB collections — including `geospatialfeatures`, `autonomous_learner`, `gbim_worldview_entities`, `psychological_rag`, `ms_jarvis_memory`, and all others — use **384-dimensional vectors** produced by `all-minilm:latest` (pulled into `jarvis-ollama:11434`, March 17). The `nomic-embed-text` model produces **768-dimensional vectors** and is **incompatible** with all existing collections. Any service, script, or migration that generates embeddings for ChromaDB must use `all-minilm:latest`. The `_DummyCollection` error that previously blocked semantic retrieval from `autonomous_learner` is resolved by this implementation.

---

## 14.1 Role in the Overall Architecture

The consolidation layer sits between fast-changing streams of requests and the slower, more stable memory and knowledge stores. As shown in Figure 14.1, the GBIM promotion and normalization pipeline feeds a hippocampal vector store that higher-level services query by worldview, dataset, and spatial footprint. The `jarvis-hippocampus` service (deployed March 15, 2026) provides this consolidation function as a dedicated microservice within the **96-container production stack** (★ March 28, 2026).

As of March 17, 2026, a second active hippocampal pathway operates in parallel: **Phase 1.45 community memory retrieval**. On every `/chat` request, before the LLM ensemble, the main brain queries the `autonomous_learner` ChromaDB collection using `all-minilm:latest` (384-dim) semantic search and prepends the top-5 most semantically similar community interaction records to `enhanced_message`. This makes accumulated community memory an active, prompt-level input to every response — not merely a background store available for optional RAG lookup.

**The two hippocampal pathways:**

| Pathway | Collection | Records | Query timing | Mechanism |
|---|---|---|---|---|
| GBIM + beliefs consolidation | `geospatialfeatures` | ~5.4M entities mirrored | Phase 4 RAG (on-demand) | Metadata-filtered ChromaDB + PostgreSQL join |
| Community interaction memory | `autonomous_learner` | Growing — 65 new external-source docs from AAPCAppE scraper (March 27); ★ see §14.8 for March 28 vector count | Phase 1.45 (every request) | `all-minilm:latest` semantic search, top-5 prepended |

A GBIM promotion and normalization pipeline:

- Promotes WV GIS features and other raw inputs into `gbim_worldview_entity`, keyed by `worldview_id`, `entity_type`, `source_table`, and `source_pk`.
- Maintains a 1:1 normalized belief row for every GBIM entity in `gbim_belief_normalized`, with JSONB axes (identity, who, for_whom, what, when, where, why, how, authority, evidence). As of March 15, 2026, all 5,416,521 entities also carry temporal decay fields: `last_verified`, `confidence_decay`, `needs_verification`.
- Extracts centroids and provenance (`evidence.provenance.dataset`, `evidence.provenance.geodbid`) and mirrors them into the ChromaDB `geospatialfeatures` collection (port 8000, `chroma_data` volume) as documents with metadata (`gbim_entity_id`, `worldview_id`, `dataset`, `source_table`, `source_pk`, `geodbid`, `centroid_x`, `centroid_y`, `srid`).

This GBIM + beliefs + Chroma stack therefore acts as a hippocampal buffer: it observes world-tied entities and program semantics, enriches them with structured beliefs and spatial context, then writes them into a persistent vector store keyed by worldview, dataset, and feature identity for future use. In combination with the introspective, qualia, and orchestration layers described in Chapters 11, 12, and 17, this provides a path from "what exists and what just happened" to "what the system will remember and reuse later," in a form that can be inspected and audited against concrete places and datasets.

**Relationship to the 9-phase pipeline (Chapter 17):**
The `jarvis-hippocampus` service and `autonomous_learner` collection participate in the production 9-phase pipeline by:

1. **Phase 1.45:** `autonomous_learner` queried via `all-minilm:latest` (384-dim) on every request — top-5 community memories prepended to `enhanced_message`
2. **Phase 4:** `geospatialfeatures` collection queried by GIS-RAG (port 8004) and `jarvis-spiritual-rag` (port 8005) as part of RAG context building; GBIM entities and beliefs retrieved from PostgreSQL `msjarvis`
3. **Phase 5:** `confidence_decay` multiplier derived from `gbim_belief_normalized` temporal metadata applied to every response
4. **Post-processing:** `background_rag_store` routes live query-response pairs back into `ms_jarvis_memory` (and, through the autonomous learning subsystem, into `autonomous_learner` growth)

---

## 14.2 Inputs to the Consolidation Process

The inputs listed here correspond to the world-model backbone on the left side of Figure 14.1. The consolidation routines draw on several concrete sources of information that already exist in the system.

**GBIM entities and normalized beliefs**
The core inputs are rows in `gbim_worldview_entity` and their 1:1 normalized belief snapshots in `gbim_belief_normalized` (PostgreSQL `msjarvis`, port **5433** ★ restored). Each belief row encodes identity (label, GBIM ID, source_table, source_pk, worldview_id), where (SRID, centroids, bbox, optional county/zip), and `evidence.provenance` (dataset, original feature IDs). As of March 15, 2026, all 5,416,521 entities also carry temporal decay metadata: `last_verified`, `confidence_decay`, `needs_verification`. These form the semantic and spatial backbone of hippocampal memory.

**Geospatial provenance and centroids**
For features with geometry, the belief `where` axis records centroids and SRIDs derived from underlying WV GIS layers (PostgreSQL `msjarvisgis`, port **5432** ★ confirmed — PostGIS, 91 GB, 501 tables, 993 ZCTA centroids from `zcta_wv_centroids`). These values are streamed into ChromaDB `geospatialfeatures` metadata (`centroid_x`, `centroid_y`, `srid`) so that retrieval can respect spatial context and coordinate systems. All embeddings for `geospatialfeatures` use `all-minilm:latest` (384-dim) to maintain collection compatibility.

**Community interaction records (`autonomous_learner`)**
The `autonomous_learner` ChromaDB collection accumulates community interaction records produced by the autonomous learning subsystem (★ see §14.8 for current vector count from the March 28, 2026 full audit; baseline was 21,181 records as of March 18, growing ~288/day). These records are written separately from `background_rag_store` and represent a different hippocampal pathway: experiential, interaction-derived memory rather than structured GBIM entity promotion. They are queried at Phase 1.45 via `all-minilm:latest` semantic search on every production request. As of March 27, 2026, the AAPCAppE scraper first run has begun adding external-source documents to the ingest pipeline — see §14.3 and §14.8.

**Program and institutional entities**
Benefit programs, governance entities, and institutional structures can also be represented as GBIM entities with beliefs over what, for_whom, why, when, and authority. As those entities are promoted, they join the same hippocampal fabric as geospatial features, allowing queries to traverse both physical and institutional space. Community-validated resource data from `jarvis-local-resources-db` (port 5435) is also eligible for promotion into the GBIM + beliefs + Chroma pipeline.

**Orchestration-level interactions**
Higher-level services (unified gateway, brain orchestrator, GIS-RAG at port 8004, WV entangled gateway) consume GBIM + beliefs + Chroma when answering questions and may create or update GBIM entities and beliefs based on user interactions. In this way, interactions feed into the GBIM belief space and, through ingestion, into the hippocampal ChromaDB collections. The 9-phase pipeline's `background_rag_store` (Chapter 17 post-processing) is the primary mechanism by which live query-response pairs are routed back through the hippocampal consolidation process.

Taken together, these inputs supply both the raw material to be stored (entities, beliefs, spatial footprints, community interaction records) and the signals about how the system has interpreted and used them.

---

## 14.3 Criteria for What Is Stored

In the current implementation, the consolidation pipeline is inclusive at the world-model level: every GBIM entity with a centroid has a normalized belief row (including temporal decay metadata as of March 15, 2026) and is mirrored into the `geospatialfeatures` collection. For `autonomous_learner`, every community interaction processed by the autonomous learning subsystem is appended — deduplication in `ms_jarvis_memory` is advisory and handled separately by `background_rag_store`'s near-duplicate check. There is not yet a fine-grained selection mechanism that stores only some entities or beliefs in hippocampal indexes.

**As of March 28, 2026**, AAPCAppE scraper documents now constitute the first external-source entries in the ingest pipeline — distinct from autonomous-learner interaction records. ★ The `spiritual_rag` collection was deduplicated (−19,338 duplicate vectors) and `psychological_rag` was restored (968 docs) during the March 28 ChromaDB full audit. Deduplication between the two pathways (scraper-ingested documents vs. autonomous-learner interaction records) remains a documented future work item.

**Implicit significance and structure**
Because the pipeline always writes a structured belief snapshot, and always includes provenance (dataset, GeoDB ID) and spatial context for centroided entities, the hippocampal surface naturally emphasizes entities that are well-grounded in both data and space. Indexing by worldview and dataset also encodes which layers and institutional perspectives are considered part of the canonical memory. The `needs_verification=TRUE` flag (100% of 5,416,521 entities at March 15 launch baseline) represents the initial state before the POC verification loop begins clearing entities as confirmed.

**Planned selection criteria**
The design for this layer goes further, envisioning explicit logic that prioritizes:

- High-impact or sensitive programs and features, including governance- or safety-related infrastructure.
- Novel or under-represented combinations of locations, populations, and benefit rules.
- Episodes where beliefs were corrected or forked across worldviews.
- Repeatedly accessed regions or entities that merit summarized, higher-level hippocampal entries.
- Entities where `confidence_decay` has fallen below threshold (future integration with POC verification loop).
- `autonomous_learner` records with high semantic similarity to repeated query patterns (candidates for summary consolidation).

These criteria can be implemented on top of the existing GBIM + beliefs + Chroma pipeline by inspecting belief metadata and usage patterns before deciding whether to store full detail, a summary, or nothing beyond base GBIM presence. At present, consolidation is intentionally broad, ensuring that a rich, place-tied backbone is available.

---

## 14.4 Transformation into Long-Term Memory

When an entity passes through the GBIM + belief + Chroma pipeline, it is transformed into durable structures that can be joined and queried from multiple angles.

**Structured beliefs and metadata in PostgreSQL (`msjarvis`, port 5433 ★ restored)**
GBIM entities receive normalized belief rows in `gbim_belief_normalized` capturing identity, spatial footprint, program semantics, and provenance. As of March 15, 2026, every belief row also carries `last_verified` (timestamp of most recent confirmation), `confidence_decay` (multiplier applied by Phase 5 of the 9-phase pipeline), and `needs_verification` (Boolean flag triggering the future POC verification loop). This relational/JSONB structure serves as the canonical long-term representation.

**Documents and metadata in ChromaDB `geospatialfeatures` (port 8000, `chroma_data` volume)**
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

This provides a fast hippocampal index for metadata-filtered recall backed by the persistent `chroma_data` Docker volume (restored March 15, 2026). ★ The full ChromaDB corpus now spans 40 active collections and 6,675,442 total vectors as of the March 28, 2026 full audit.

**Community interaction records in ChromaDB `autonomous_learner` (port 8000, `chroma_data` volume)**
Each community interaction processed by the autonomous learning subsystem is written as a document + metadata record in `autonomous_learner`, embedded via `all-minilm:latest` (384-dim). These records capture the conversational and task-level experience of the system's community engagement — a complementary memory pathway to the structured GBIM entity fabric. At Phase 1.45, the top-5 most semantically relevant records are prepended to every production prompt. ★ See §14.8 for the current vector count from the March 28, 2026 full audit.

**Implicit belief and routing traces (planned)**
As Ms. Jarvis's belief graph and routing logic mature, ChromaDB `geospatialfeatures` metadata can be extended to include explicit references to belief nodes, routing decisions, and normative labels, turning each hippocampal entry into a trace of how the system's internal model and policies interacted with that entity.

**Spatial anchoring via geospatial layers**
Because beliefs carry centroids, SRIDs, and optional administrative labels, hippocampal entries can be linked back to counties, cities, watersheds, and other layers maintained in `msjarvisgis` (port **5432** ★ confirmed, 91 GB PostGIS, 501 tables). The `zcta_wv_centroids` table (993 rows) provides the canonical ZIP-level spatial anchors. This connects abstract programs and features to specific West Virginia places.

These transformations map directly to the central pipeline and hippocampal store blocks in Figure 14.1.

---

## 14.5 Temporal Organization and Decay

In many neuro-inspired designs, hippocampal systems maintain a temporal hierarchy of memories and implement decay. As of March 15–28, 2026, Ms. Jarvis has deployed the first phase of temporal organization: the GBIM confidence decay system, the `autonomous_learner` growth curve, and the Phase 1.45 active retrieval pathway.

**Current behavior (★ March 28, 2026)**
Every GBIM entity in the relevant worldview receives a normalized belief row with `last_verified`, `confidence_decay`, and `needs_verification` fields. The `confidence_decay` multiplier is applied at Phase 5 of every production 9-phase pipeline request (Chapter 17), attenuating response confidence proportionally to how long an entity has gone without verification. At the March 15 launch baseline, 100% of 5,416,521 entities carry `needs_verification=TRUE` — the expected initial state, not a data quality error. The `autonomous_learner` collection provides a complementary temporal signal through its growth curve: records accumulating represent the system's lived engagement history, with older records naturally becoming less semantically prominent as newer interactions are added and the nearest-neighbor retrieval at Phase 1.45 surfaces the most relevant. ★ The `spiritual_rag` deduplication (−19,338 vectors, March 28) is an example of retroactive temporal curation that the temporal organization subsystem should eventually automate.

**POC verification loop (planned, highest-priority future work)**
The POC (Point of Contact) verification loop will automate the process of re-contacting a resource's designated point of contact when `needs_verification=TRUE` and resetting `confidence` to 1.0 on confirmation. This is the primary mechanism for clearing the initial 100% flagged state and for maintaining temporal freshness of GBIM-anchored hippocampal memory. Until implemented, the flag-and-attenuate approach via `confidence_decay` serves as the operative temporal decay mechanism.

**Planned temporal hierarchy**
Beyond the current decay system, the design anticipates:

- A recent window of high-granularity belief and hippocampal entries suitable for detailed forensic analysis.
- Intermediate summarizations that merge multiple similar entities or interactions into trend-level records across both `geospatialfeatures` and `autonomous_learner`.
- A long-term backbone of especially important precedents, patterns, and governance-relevant insights that are protected from aggressive pruning.

These behaviors can be implemented as periodic jobs or 69-DGM-driven optimization steps (Chapter 32) over the GBIM and ChromaDB layers. For now, descriptions of temporal hierarchy beyond `confidence_decay` should be understood as forward-looking design notes grounded in the current always-append behavior with decay-weighted confidence.

---

## 14.6 Interaction with Retrieval and Introspection

Consolidated GBIM and hippocampal entries play a direct role in how Ms. Jarvis retrieves context and can be tightly integrated with introspective narratives.

**Retrieval feedback loop (9-phase pipeline integration)**
When higher-level services (GIS-RAG at port 8004, WV entangled gateway, `jarvis-spiritual-rag` at port 8005) need context during Phase 4 of the 9-phase pipeline, they:

1. Use worldview, dataset, and spatial constraints (bboxes, centroids, counties, `zcta_wv_centroids` from `msjarvisgis` port **5432** ★) to select candidate GBIM entities and beliefs from `msjarvis.gbim_belief_normalized`.
2. Use those provenance keys (`worldview_id`, `dataset`, `geodbid`) as ChromaDB metadata filters in the `geospatialfeatures` collection (port 8000), retrieving relevant entities quickly.
3. Apply `confidence_decay` weighting at Phase 5 to attenuate results based on verification recency.
4. Join ChromaDB hits back to `gbim_worldview_entity` and `gbim_belief_normalized` (PostgreSQL `msjarvis`, port **5433** ★) to assemble answers and map overlays grounded in both beliefs and physical space.
5. Join spatial identifiers to `msjarvisgis.zcta_wv_centroids` (port **5432** ★) and `jarvis-local-resources-db` (port 5435) for community-anchored resource context.

**Phase 1.45 active community memory retrieval (deployed March 17, 2026)**
Before Phase 4 RAG, Phase 1.45 performs a distinct and always-on hippocampal retrieval:

1. The incoming query is embedded via `all-minilm:latest` at `jarvis-ollama:11434/api/embeddings` (384-dim).
2. The vector is used to query `autonomous_learner` (★ see §14.8 for current count from March 28, 2026 full audit).
3. The 5 most semantically similar community interaction records are retrieved (documents + metadata + distances).
4. The retrieved memories are prepended to `enhanced_message` before it enters Phase 2.5 LLM ensemble processing.

This pathway guarantees that every LLM response is grounded in the system's accumulated community engagement history, not just structured GBIM entities. The two pathways are complementary: Phase 1.45 supplies experiential, interaction-level context; Phase 4 supplies structured, spatial, and institutional GBIM knowledge.

**Introspective descriptions of memory use**
As the introspective layer evolves, it can report which GBIM entities, datasets, and spatial regions were consulted for a given response, which `autonomous_learner` records were prepended at Phase 1.45, and how their `confidence_decay` values influenced the result. Instead of referring only to "conversation documents," introspection can speak about buildings, roads, programs, and jurisdictions as concrete memory units with known verification timestamps, alongside community interaction records with known semantic relevance scores. ★ `jarvis-memory` (port 8056, corrected from `0.0.0.0` to `127.0.0.1` March 28, `_auth()` confirmed) provides the authenticated API surface for these introspective memory reads.

**Optimization over hippocampal histories via 69-DGM cascade**
Self-improving agents in the 69-DGM layer (Chapter 32, `jarvis-69dgm-bridge` host port **19000** → internal **9000**, confirmed running — re-locked to `127.0.0.1:19000` March 18, 2026) can treat GBIM + beliefs + ChromaDB `geospatialfeatures` and `autonomous_learner` as datasets for discovering weaknesses, biases, or gaps in coverage — for example, which counties are under-represented, which datasets are heavily relied on, where repeated corrections to beliefs occur, which entities have the longest-decayed `confidence_decay` values, or which `autonomous_learner` records are never surfaced by Phase 1.45 retrieval and may warrant consolidation or pruning. The 23-connector × 3-stage cascade (69 DGM operations per pass) that validates every production response is the current implementation of this optimization loop.

---

## 14.7 Alignment with Spatial and Governance Goals

Because much of Ms. Jarvis's mission is tied to specific regions, communities, and institutions in West Virginia, the consolidation layer is designed to align closely with spatial and governance-oriented goals.

**Place-aware memory**
Extensive WV geospatial layers — counties, block groups, census tracts, cities, facilities, infrastructure, and more — coexist as GBIM entities and beliefs in PostgreSQL `msjarvis` (5,416,521 entities from 206 source layers, port **5433** ★) and PostGIS `msjarvisgis` (91 GB, 501 tables, port **5432** ★). By mirroring centroid-bearing entities into ChromaDB `geospatialfeatures` with worldview IDs, datasets, and spatial metadata, and by accumulating community interaction records in `autonomous_learner`, consolidation enables later analyses to ask how particular counties, towns, or facilities have been represented and served in the system's history. The 993 ZCTA centroids in `msjarvisgis.zcta_wv_centroids` (port **5432** ★) provide the canonical ZIP-level anchors for this place-aware fabric.

**Community-validated institutional continuity**
As governance-relevant beliefs and norms are encoded in GBIM worldviews, hippocampal entries link entities and episodes to the councils, districts, or organizations they involve. Community-validated data from Harmony for Hope's Community Champions (stored in `jarvis-local-resources-db`, port 5435, confirmed in the end-to-end benchmark) is eligible for promotion into the hippocampal pipeline, ensuring that ground-truth verification by community members like lead validator Crystal Colyer feeds durable, place-grounded memory. Community interaction records in `autonomous_learner` capture the conversational record of this community engagement at a level of temporal granularity that structured GBIM promotion does not provide.

**Equity, oversight, and temporal accountability**
By combining spatial identifiers, belief metadata (including `confidence_decay` and `needs_verification`), Phase 1.45 community memory retrieval, and hippocampal retrieval histories, analysts and agents can examine whether certain communities receive less assistance, face different patterns of risk, or encounter more frequent misunderstandings. The `needs_verification` flag makes temporal gaps in confirmation explicit and auditable: communities can see not only which entities were used in a response but how recently those entities were confirmed against ground truth. These insights can inform adjustments to routing, content, or outreach so that the system's behavior better supports equitable outcomes.

---

## 14.8 Implementation Status (★ March 28, 2026)

**Confirmed operational (★ March 28, 2026 — 96/96 containers Up):**
- ✅ `jarvis-hippocampus` service deployed in **96-container production stack** ★ (commit `b90f9ff`)
- ✅ ChromaDB `geospatialfeatures` collection active (port 8000, `chroma_data` volume)
- ✅ ChromaDB `autonomous_learner` collection: growing — Phase 1.45 active retrieval every `/chat` call (★ see collection table below for March 28, 2026 vector count)
- ✅ **Embedding model: `all-minilm:latest` (384-dim)** — canonical model for ★ all 40 ChromaDB collections; `nomic-embed-text` (768-dim) confirmed incompatible and must not be used
- ✅ `_DummyCollection` error blocking `autonomous_learner` semantic retrieval: RESOLVED (March 17) — `all-minilm:latest` semantic retrieval is the fix
- ✅ PostgreSQL `msjarvis` (port **5433** ★ restored): 5,416,521 GBIM entities with normalized `gbim_belief_normalized` rows
- ✅ PostgreSQL `msjarvisgis` (port **5432** ★ confirmed): 91 GB PostGIS, 501 tables, 993 ZCTA centroids
- ✅ GBIM temporal decay deployed: all 5,416,521 entities carry `last_verified`, `confidence_decay`, `needs_verification`
- ✅ `confidence_decay` multiplier applied at Phase 5 of every production 9-phase pipeline request
- ✅ `background_rag_store` routing post-processing back into hippocampal consolidation (verified in Chapter 17 benchmark)
- ✅ `geospatialfeatures` collection queried by GIS-RAG (port 8004) and `jarvis-spiritual-rag` (port 8005) during Phase 4 RAG context building
- ✅ Integration with `msjarvisgis.zcta_wv_centroids` (993 rows, port **5432** ★) for spatial anchoring
- ✅ `jarvis-local-resources-db` (port 5435) community resource data eligible for GBIM promotion
- ✅ Phase 1.45 community memory retrieval confirmed in ~436s end-to-end benchmark (March 18, 2026)
- ✅ `jarvis-memory` (port **8056**): ★ corrected from `0.0.0.0` to `127.0.0.1` March 28, 2026; `_auth()` confirmed on 4 sensitive routes; `JARVIS_API_KEY` confirmed set
- ✅ ★ **96/96 containers Up — zero Restarting, zero Exited (March 28, 2026)**

**ChromaDB collections (★ March 28, 2026 full audit — 40 collections, 6,675,442 total vectors):**

| Collection | Records / Vectors | Notes |
|---|---|---|
| `gbim_worldview_entities` | 5,416,521 | Complete WV GBIM spatial corpus |
| `autonomous_learner` | ★ See March 28 audit count (baseline 21,181 as of March 18, growing ~288/day) | Phase 1.45 active retrieval; first external-source docs (AAPCAppE) flowing as of March 27 |
| `aapcappe_corpus` | 65 | First scrape run complete March 27, 2026 (39 sources, `total_runs: 1`); 53 RAG-loaded, 7 new base cultural docs |
| `psychological_rag` | **968** ★ restored March 28 | Restored during March 28 ChromaDB full audit |
| `spiritual_rag` | ★ Deduplicated March 28 (−19,338 duplicate vectors removed) | Deduplication confirmed during March 28 ChromaDB full audit |
| `spiritual_texts` | 23 | Unchanged |
| `appalachian_cultural_intelligence` | 5 | Confirmed March 18 |
| `GBIM_sample_rows` | 5,000 | Confirmed March 18 |
| `GBIM_sample` | 3 | Confirmed March 18 |
| `msjarvis-smoke` | 1 | Smoke test record |
| `msjarvis_docs` | **4,192** ★ expanded March 28 | Expanded during March 28 ChromaDB full audit (previously 53 from March 27 RAG load) |
| `ms_jarvis_memory` | ★ See March 28 audit count | Active memory collection; `jarvis-memory` API (port 8056 ★) provides authenticated access |
| `geospatialfeatures` | 0 | Scaffolded — pending backfill ingest (all backfill embeddings must use `all-minilm:latest` 384-dim) |
| `GBIM_Fayette_sample` | 0 | Scaffolded — pending ingest |
| *(additional collections)* | ★ See March 28 audit for full 40-collection enumeration | Total: 40 collections, 6,675,442 vectors |

**Remaining work:**

**POC verification loop (highest-priority future work)**
The automated POC verification loop — where the system contacts a resource's designated point of contact when `needs_verification=TRUE` and resets `confidence` to 1.0 on confirmation — is not yet automated. Current state: flag-and-attenuate via `confidence_decay` only. This is the primary mechanism for clearing the initial 100% flagged baseline.

**`geospatialfeatures` ingest and metadata backfill**
The `geospatialfeatures` ChromaDB collection is scaffolded but currently at 0 records pending backfill ingest. Extended metadata fields (`worldview_id`, `bbox`, `dataset`) need population across all 5,416,521 GBIM entities. Backfill pipeline exists but requires execution post-ingest (see Chapter 5 §5.11). All backfill embeddings must use `all-minilm:latest` (384-dim).

**Selective storage criteria**
Fine-grained selection logic (high-impact features, novel combinations, corrected beliefs, heavily accessed regions) is designed but not yet implemented. Currently all centroided entities are intended for mirroring to `geospatialfeatures`; `autonomous_learner` receives all community interaction records without filtering.

**Temporal hierarchy beyond decay**
Intermediate summarizations, pruning of aged entries, and long-term backbone extraction remain forward-looking design intentions implemented on top of the current always-append plus decay-weight behavior. ★ The `spiritual_rag` deduplication (−19,338 vectors, March 28) demonstrates that retroactive curation is feasible at scale and should be incorporated into the temporal hierarchy roadmap.

**Tighter belief-routing traces**
Extending `geospatialfeatures` ChromaDB metadata to include explicit belief node references, routing decisions, and normative labels — turning each hippocampal entry into a full trace of the system's internal model interaction — is planned but not yet implemented.

---

## 14.9 Summary

The consolidation layer captures how recent activity and world-modeling are turned into lasting structure across two complementary hippocampal pathways: (1) GBIM entities with normalized beliefs and temporal decay metadata in PostgreSQL `msjarvis` (port **5433** ★ restored), mirrored as centroid-bearing records into the `geospatialfeatures` ChromaDB collection (port 8000, `chroma_data` volume), queried by GIS-RAG and spiritual-RAG during Phase 4; and (2) the `autonomous_learner` ChromaDB collection (★ see §14.8 for the March 28, 2026 vector count from the full audit; first external-source AAPCAppE documents flowing as of March 27, 2026), queried via `all-minilm:latest` (384-dim) semantic search at Phase 1.45 of every production `/chat` request, with top-5 community memories prepended to `enhanced_message`.

The `jarvis-hippocampus` service (deployed March 15, 2026, commit `b90f9ff`) functions as the dedicated hippocampal buffer within the **96-container production stack** (★ all 96 containers Up, March 28, 2026). The **`jarvis-memory` service** (port **8056** ★ corrected from `0.0.0.0` to `127.0.0.1` March 28, `_auth()` confirmed on 4 sensitive routes, `JARVIS_API_KEY` set) operates as a companion container to `jarvis-hippocampus`, confirmed verified in the March 28, 2026 security remediation sprint (see **Chapter 12 §12.12**). The `confidence_decay` multiplier applied at Phase 5 of every production request makes hippocampal temporal state an active, measurable factor in every response — not merely an archival attribute. Phase 1.45 community memory retrieval (deployed March 17, 2026) makes `autonomous_learner` a live, prompt-level input to every response rather than a passive background store. The critical embedding model lock — **`all-minilm:latest` (384-dim) for all 40 ChromaDB collections** (★ 6,675,442 total vectors, March 28, 2026 full audit) — ensures collection compatibility and is a permanent architectural constraint.

★ The March 28, 2026 ChromaDB full audit — 40 collections, 6,675,442 total vectors; `spiritual_rag` deduplicated (−19,338 vectors); `psychological_rag` restored (968 docs); `msjarvis_docs` expanded (4,192 items) — is the first comprehensive baseline of the full hippocampal vector corpus and establishes the foundation for all future temporal organization, selective storage, and deduplication work described in this chapter.

POC verification loop automation, `geospatialfeatures` backfill ingest, selective storage criteria, temporal hierarchy beyond decay, and tighter belief-routing traces are active design directions that build on this foundation. Subsequent chapters describe how global controls, the 69-DGM cascade (Chapter 32), and executive processes (Chapter 17) use these consolidated, place-aware memories as part of broader feedback loops that shape Ms. Jarvis's ongoing evolution. Chapter 5 describes the ChromaDB `chroma_data` volume and collection architecture in detail. Chapter 17 describes how Phase 1.45 community memory retrieval and the `confidence_decay` multiplier are applied in the 9-phase production pipeline.

---

*Last updated: 2026-03-28 — Carrie Kidd (Mamma Kidd), Mount Hope WV*

*★ March 27, 2026: Production state block updated — AAPCAppE scraper first run confirmed 65 documents in Chroma, RAG loaded 53 documents (7 new base cultural docs), first external-source documents now flowing into autonomous_learner pipeline; §14.3 selective storage note added — AAPCAppE scraper documents are first external-source entries, deduplication between scraper and autonomous-learner pathways is documented future work; §14.8 ChromaDB table updated — msjarvis_docs row updated from 0 to 53 (March 27 RAG load), aapcappe_corpus row added (65 docs, 39 sources, total_runs: 1, first scrape March 27), autonomous_learner row updated with March 27 sprint note; §14.9 jarvis-memory companion container note added — confirmed in March 27 container audit, see Ch. 12 §12.11.*

*★ March 28, 2026: Security remediation complete — 96/96 containers Up; `jarvis-memory` (8056) corrected from `0.0.0.0` to `127.0.0.1`; `_auth()` on 4 sensitive routes confirmed; `JARVIS_API_KEY` set confirmed. Container count updated from 79 → 96 throughout. ChromaDB full audit (40 collections, 6,675,442 total vectors) propagated to introduction, production state block, §14.1, §14.2, §14.3, §14.4, §14.6, §14.8 collection table, §14.9. `spiritual_rag` deduplicated (−19,338 vectors) added to §14.3, §14.5, §14.8, §14.9. `psychological_rag` restored (968 docs) added to §14.8. `msjarvis_docs` expanded to 4,192 items in §14.8. `msjarvis` port 5433 restored and `msjarvisgis` port 5432 confirmed (91 GB PostGIS, 501 tables) — replaced all `gisdb` port 5433 / 13 GB / 39 tables references throughout: §14.2, §14.4, §14.6, §14.7, §14.8, §14.9. Ch. 12 §12.11 cross-reference updated to §12.12 to reflect chapter restructuring. §14.9 jarvis-memory security remediation note updated from March 27 container audit to March 28 security remediation sprint.*
