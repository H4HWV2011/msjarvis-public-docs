# 14. Hippocampus and Memory Consolidation

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: April 23, 2026 — CLOSED; container count → 100; ChromaDB → 48
collections / ~6,740,611 vectors; `autonomous_learner` → 21,181 exact; two-container
DB split applied throughout; `msallisgis` → 294 tables / 16 GB production /
314 tables / 17 GB forensic; `postgis-forensic` added; all April 16 items remain
CLOSED.*

> **★ April 23, 2026 UPDATE:** Container count → **100 Up** (zero Restarting, zero
> Exited). ChromaDB v2 → **48 collections, ~6,740,611 vectors** (host port **8002**).
> `autonomous_learner` → **21,181 records** (exact, April 23, 2026). Two-container DB
> split: **Production:** `msallis-db` host **5433** / container **5432** —
> `msallisgis` **16 GB / 294 tables / 11 schemas**. **Forensic:** `postgis-forensic`
> host **5432** — `msallisgis` **17 GB / 314 tables / 9 schemas** — forensic only.
> `allis-memory` / `allis-memory` port **8056**: `/memory/sessions` HTTP 200 with
> **14 active sessions** (authenticated, `ALLIS_API_KEY`). GPU pipeline: **102.58s**
> confirmed (RTX 4070). All April 16 OI items remain CLOSED.

> **★ April 16, 2026 — FULL SPRINT CLOSURE (historical baseline):** Container count:
> **110 containers Up**. ChromaDB: **49 active collections, 6,722,589+ total vectors**.
> `msallisgis`: **551 tables, 45 GB**. `autonomous_learner`: **21,181+ records as of
> April 10, 2026** — the 57-item post-fix slice was the April 1 recovery baseline only;
> Phase 1.45 active retrieval confirmed in April 16 preflight gate. `msallis_docs`
> ChromaDB: **7,465 items**. Community resources: **64 verified resources** (all 55 WV
> counties confirmed). `msallis-db` (port **5433**): bind corrected from `0.0.0.0` to
> `127.0.0.1`. `allis-memory:8056` `/memory/sessions`: HTTP 200 confirmed with 14
> active sessions. End-to-end pipeline: **99–107 seconds on RTX 4070 GPU** (the
> 436-second CPU baseline is archived). Preflight gate: **all 27 gates ✅ green**.
> **Chapter 14 CLOSED.**

---

## Why This Matters for Polymathmatic Geography

This chapter explains how Ms. Allis turns lived interactions — often about specific West
Virginia places — into durable, inspectable memory. It supports:

- **P1 – Every where is entangled** by tying conversational experiences and world-model
  updates to shared semantic, institutional, and spatial backbones grounded in GBIM
  entities, normalized beliefs, and a statewide hippocampal index.
- **P3 – Power has a geometry** by making long-term memory a structured, queryable space
  over worldview-tied features, not an opaque chat log, so that reasoning paths can be
  traced across specific datasets, programs, and jurisdictions.
- **P5 – Design is a geographic act** by deciding which entities, programs, and
  communities are promoted into GBIM, given nine-axis beliefs, and mirrored into
  hippocampal collections keyed by worldview, dataset, and feature identity.
- **P12 – Intelligence with a ZIP code** by anchoring consolidated memories in WV
  geospatial layers, normalized nine-axis beliefs, and local knowledge bases so that
  questions about "who is helped where" are answered in terms of concrete places and
  entities.
- **P16 – Power accountable to place** by storing rich, provenance-aware traces
  (worldview IDs, datasets, GeoDB feature IDs, centroids, SRIDs) so communities can
  audit how advice and analysis are grounded in their own places rather than abstract
  averages.

As such, this chapter belongs to the **Computational Instrument** tier: it specifies the
hippocampal consolidation pipeline that turns Ms. Allis's activity and world models into
a long-term, place-aware memory substrate. The `allis-hippocampus` service was deployed
March 15, 2026 (commit `b90f9ff`) as part of the production stack and is confirmed
operational in the end-to-end pipeline benchmark. Phase 1.45 community memory retrieval
(deployed March 17, 2026) queries the `autonomous_learner` ChromaDB collection on every
production `/chat` request, making hippocampal memory an active input to every response
rather than a background archive.

> *Figure 14.1. Hippocampal consolidation in Ms. Allis: GBIM entities and normalized
> nine-axis beliefs, enriched with centroids and provenance, are mirrored into a
> `geospatialfeatures` vector collection that serves as a long-term, place-aware memory
> index for retrieval and audit. Phase 1.45 (deployed March 17, 2026) adds a second
> active retrieval path: the `autonomous_learner` collection is queried on every `/chat`
> request via `all-minilm:latest` (384-dim) semantic search, prepending the top-5 most
> relevant community interaction records to every LLM prompt.*

---

# 14. Hippocampus and Memory Consolidation

This chapter describes how recent activity is turned into durable records in the
system's long-term stores. The design borrows the idea of a hippocampal buffer that
receives short-lived experiences, decides what matters, and then writes compact,
structured traces into more stable memory. In the current implementation, this role is
played by two complementary subsystems: (1) the GBIM + beliefs + Chroma hippocampus —
GBIM worldview entities in `gbim_worldview_entity`, their 1:1 normalized nine-axis
belief rows in `gbim_belief_normalized`, and a ChromaDB collection called
`geospatialfeatures` that mirrors centroid-bearing entities together with worldview,
dataset, GeoDB IDs, and other provenance; and (2) the `autonomous_learner` ChromaDB
collection, which accumulates community interaction records and is queried at Phase 1.45
of every production `/chat` request.

The `allis-hippocampus` service is deployed and confirmed operational as part of the
**100-container production stack** (★ all 100 containers Up — zero Restarting, zero
Exited, April 23, 2026). ChromaDB is fully containerized at container port 8000 / host
port 8002 with the `chroma_data` Docker volume. All ChromaDB collections use
**384-dimensional vectors** produced by `all-minilm:latest`. ★ The ChromaDB corpus
spans **48 active collections and ~6,740,611 total vectors** (April 23, 2026 confirmed
baseline).

**Production state (★ April 23, 2026 — preflight gate all 27 gates ✅ green):**

- `allis-hippocampus` service: ✅ Deployed and operational (commit `b90f9ff`)
- ChromaDB `geospatialfeatures` collection: ✅ Active (container port 8000 / host port
  8002, `chroma_data` volume)
- ChromaDB `autonomous_learner` collection: ✅ **Healthy — 21,181 records (April 23,
  2026 exact); Phase 1.45 active retrieval confirmed**
- Embedding model: ✅ **`all-minilm:latest` (384-dim)** — canonical embedding model for
  all 48 ChromaDB collections
- **Production DB:** `msallis-db` host **5433** / container **5432**, bound to
  `127.0.0.1`, role `postgres`, `msallisgis` **16 GB / 294 tables / 11 schemas** ✅
- **Forensic DB:** `postgis-forensic` host **5432**, role `allis`, `msallisgis`
  **17 GB / 314 tables / 9 schemas** — forensic auditing only ✅
- GBIM temporal confidence decay: ✅ Deployed March 15 — all entities carry
  `last_verified`, `confidence_decay`, `needs_verification`
- Integration with 9-phase pipeline: ✅ Confirmed end-to-end GPU pipeline —
  **102.58s on RTX 4070** (the 436-second CPU baseline is archived)
- `allis-memory` / `allis-memory` (port **8056**, 127.0.0.1): ✅ `/memory/sessions`
  HTTP 200 confirmed with **14 active sessions**; `ALLIS_API_KEY` exported and set
- Community resources: ✅ **64 verified resources** (all 55 WV counties confirmed)
- `msallis_docs` ChromaDB: ✅ **7,465 items**
- **★ 100/100 containers Up — zero Restarting, zero Exited (April 23, 2026)**

> **📈 April 23, 2026 preflight gate — all 27 gates ✅ green:** Two-container DB split
> applied — production `msallis-db` (host **5433**) and forensic `postgis-forensic`
> (host **5432**) confirmed. All containers bound to `127.0.0.1`. Zero `0.0.0.0`
> exposures. `ALLIS_API_KEY` exported and set. ChromaDB v2 → 48 collections /
> ~6,740,611 vectors. `autonomous_learner` → 21,181 exact.

> **📈 April 16, 2026 preflight gate — all 27 gates ✅ green (historical baseline):**
> Remediations applied before full green: (1) `msallis-db` port 5433 bind corrected
> from `0.0.0.0` to `127.0.0.1` — orphaned container stopped, removed, and recreated
> via compose; (2) `allis-memory:8056` `/memory/sessions` was returning HTTP 500 —
> resolved by exporting `ALLIS_API_KEY`; HTTP 200 confirmed with 14 active sessions;
> (3) container count advanced to 110.

> **📈 April 1, 2026 autonomous learner debug sprint — COMPLETE (historical
> reference):** The autonomous learner (`allis-autonomous-learner`, port 8020) entered
> a crash-loop on April 1, 2026 after a failed patch attempt deployed an empty file
> (1.54 kB), triggering `ERROR: Attribute 'app' not found in module` on Uvicorn startup
> (LEARN-03). Concurrently, a `cosine_similarity` bug was identified where the dedup
> gate comparison raised `"The truth value of an array with more than one element is
> ambiguous"` on every cycle due to a numpy array being returned instead of a scalar
> (LEARN-01). The GBIM Query Router (port 7205) briefly returned HTTP 422 on
> mis-shaped learner `route` POST calls (LEARN-02). All three items were resolved on
> April 1, 2026. The 57-item post-fix slice was the recovery baseline. Accumulation
> continued: **21,181 records confirmed April 23, 2026**.

> **📈 March 28, 2026 audit update (historical reference):** ChromaDB full audit — 40
> active collections, 6,675,442 total vectors. `spiritual_rag` deduplicated (−19,338
> duplicate vectors). `psychological_rag` restored (968 docs). `msallis_docs` at 4,192
> items. All 40 collections confirmed on `all-minilm:latest` (384-dim).

> **Critical — Embedding model lock (March 17, 2026):** All ChromaDB collections —
> including `geospatialfeatures`, `autonomous_learner`, `gbim_worldview_entities`,
> `psychological_rag`, `ms_allis_memory`, and all others — use **384-dimensional
> vectors** produced by `all-minilm:latest` (pulled into `allis-ollama:11434`). The
> `nomic-embed-text` model produces **768-dimensional vectors** and is
> **incompatible** with all existing collections. Any service, script, or migration
> that generates embeddings for ChromaDB must use `all-minilm:latest`. The
> `_DummyCollection` error that previously blocked semantic retrieval from
> `autonomous_learner` is resolved.

---

## 14.1 Role in the Overall Architecture

The consolidation layer sits between fast-changing streams of requests and the slower,
more stable memory and knowledge stores. As shown in Figure 14.1, the GBIM promotion
and normalization pipeline feeds a hippocampal vector store that higher-level services
query by worldview, dataset, and spatial footprint. The `allis-hippocampus` service
(deployed March 15, 2026) provides this consolidation function as a dedicated
microservice within the **100-container production stack** (★ April 23, 2026).

As of March 17, 2026, a second active hippocampal pathway operates in parallel:
**Phase 1.45 community memory retrieval**. On every `/chat` request, before the LLM
ensemble, the main brain queries the `autonomous_learner` ChromaDB collection using
`all-minilm:latest` (384-dim) semantic search and prepends the top-5 most semantically
similar community interaction records to `enhanced_message`. This makes accumulated
community memory an active, prompt-level input to every response — not merely a
background store available for optional RAG lookup.

**The two hippocampal pathways:**

| Pathway | Collection | Records | Query timing | Mechanism |
|:--|:--|:--|:--|:--|
| GBIM + beliefs consolidation | `geospatialfeatures` | GBIM entity corpus | Phase 4 RAG (on-demand) | Metadata-filtered ChromaDB + PostgreSQL join |
| Community interaction memory | `autonomous_learner` | **21,181 records (April 23, 2026 exact)** | Phase 1.45 (every request) | `all-minilm:latest` semantic search, top-5 prepended |

A GBIM promotion and normalization pipeline:

- Promotes WV GIS features and other raw inputs into `gbim_worldview_entity`, keyed by
  `worldview_id`, `entity_type`, `source_table`, and `source_pk`.
- Maintains a 1:1 normalized belief row for every GBIM entity in
  `gbim_belief_normalized`, with JSONB axes (identity, who, for_whom, what, when, where,
  why, how, authority, evidence). As of March 15, 2026, all entities also carry temporal
  decay fields: `last_verified`, `confidence_decay`, `needs_verification`.
- Extracts centroids and provenance (`evidence.provenance.dataset`,
  `evidence.provenance.geodbid`) and mirrors them into the ChromaDB `geospatialfeatures`
  collection as documents with metadata (`gbim_entity_id`, `worldview_id`, `dataset`,
  `source_table`, `source_pk`, `geodbid`, `centroid_x`, `centroid_y`, `srid`).

This GBIM + beliefs + Chroma stack therefore acts as a hippocampal buffer: it observes
world-tied entities and program semantics, enriches them with structured beliefs and
spatial context, then writes them into a persistent vector store keyed by worldview,
dataset, and feature identity for future use. In combination with the introspective,
qualia, and orchestration layers described in Chapters 11, 12, and 17, this provides a
path from "what exists and what just happened" to "what the system will remember and
reuse later," in a form that can be inspected and audited against concrete places and
datasets.

**Relationship to the 9-phase pipeline (Chapter 17):**
The `allis-hippocampus` service and `autonomous_learner` collection participate in the
production 9-phase pipeline by:

1. **Phase 1.45:** `autonomous_learner` queried via `all-minilm:latest` (384-dim) on
   every request — top-5 community memories prepended to `enhanced_message`
2. **Phase 4:** `geospatialfeatures` collection queried by GIS-RAG (port 8004) and
   `allis-spiritual-rag` (port 8005) as part of RAG context building; GBIM entities and
   beliefs retrieved from production PostgreSQL `msallis-db` (port **5433**)
3. **Phase 5:** `confidence_decay` multiplier derived from `gbim_belief_normalized`
   temporal metadata applied to every response
4. **Post-processing:** `background_rag_store` routes live query-response pairs back
   into `ms_allis_memory` and through the autonomous learning subsystem into
   `autonomous_learner` growth

**Pipeline timing (April 23, 2026):** End-to-end 9-phase GPU pipeline: **102.58s on
RTX 4070**. The 436-second CPU baseline documented in the March 18, 2026 benchmark is
archived; GPU pipeline has been active since April 6, 2026. Chapter 17 carries the
authoritative pipeline timing.

---

## 14.2 Inputs to the Consolidation Process

The inputs listed here correspond to the world-model backbone on the left side of
Figure 14.1. The consolidation routines draw on several concrete sources of information
that already exist in the system.

**GBIM entities and normalized beliefs**
The core inputs are rows in `gbim_worldview_entity` and their 1:1 normalized belief
snapshots in `gbim_belief_normalized`. Two-container DB architecture (April 23, 2026):
**Production:** `msallis-db` host **5433** / container **5432**, bound to `127.0.0.1`,
role `postgres`, `msallisgis` **16 GB / 294 tables / 11 schemas** — all production
writes. **Forensic:** `postgis-forensic` host **5432**, role `allis`, `msallisgis`
**17 GB / 314 tables / 9 schemas** — forensic auditing only. Each belief row encodes
identity (label, GBIM ID, source_table, source_pk, worldview_id), where (SRID,
centroids, bbox, optional county/zip), and `evidence.provenance` (dataset, original
feature IDs). All entities carry temporal decay metadata: `last_verified`,
`confidence_decay`, `needs_verification`. These form the semantic and spatial backbone
of hippocampal memory.

**Geospatial provenance and centroids**
For features with geometry, the belief `where` axis records centroids and SRIDs derived
from underlying WV GIS layers. Production DB `msallis-db` (host **5433**) contains the
GBIM entity and belief store. Spatial data sourced from production `msallisgis`
(**16 GB**, **294 tables**, host port **5433**) and forensic `postgis-forensic`
(**17 GB**, **314 tables**, host port **5432** — forensic only). 993 ZCTA centroids from
`zcta_wv_centroids`, 1,115,588 address points. These values are streamed into ChromaDB
`geospatialfeatures` metadata (`centroid_x`, `centroid_y`, `srid`). All embeddings for
`geospatialfeatures` use `all-minilm:latest` (384-dim).

**Community interaction records (`autonomous_learner`)**
The `autonomous_learner` ChromaDB collection accumulates community interaction records
produced by the autonomous learning subsystem. **21,181 records (April 23, 2026 —
exact).** The 57-item figure from April 1, 2026 was the recovery baseline following the
LEARN-01/LEARN-03 debug sprint; accumulation continued and is now stable at 21,181.
Phase 1.45 active retrieval is confirmed operational. These records are written
separately from `background_rag_store` and represent a distinct hippocampal pathway:
experiential, interaction-derived memory rather than structured GBIM entity promotion.
They are queried at Phase 1.45 via `all-minilm:latest` semantic search on every
production request.

**Program and institutional entities**
Benefit programs, governance entities, and institutional structures can also be
represented as GBIM entities with beliefs over what, for_whom, why, when, and authority.
As those entities are promoted, they join the same hippocampal fabric as geospatial
features, allowing queries to traverse both physical and institutional space.
Community-validated resource data from `allis-local-resources-db` (port 5435) is also
eligible for promotion into the GBIM + beliefs + Chroma pipeline. As of April 23, 2026:
**64 verified resources** (all 55 WV counties confirmed).

**Orchestration-level interactions**
Higher-level services (unified gateway, brain orchestrator, GIS-RAG at port 8004, WV
entangled gateway) consume GBIM + beliefs + Chroma when answering questions and may
create or update GBIM entities and beliefs based on user interactions. The 9-phase
pipeline's `background_rag_store` (Chapter 17 post-processing) is the primary mechanism
by which live query-response pairs are routed back through the hippocampal consolidation
process.

---

## 14.3 Criteria for What Is Stored

In the current implementation, the consolidation pipeline is inclusive at the
world-model level: every GBIM entity with a centroid has a normalized belief row
(including temporal decay metadata as of March 15, 2026) and is mirrored into the
`geospatialfeatures` collection. For `autonomous_learner`, every community interaction
processed by the autonomous learning subsystem is appended — deduplication in
`ms_allis_memory` is advisory and handled separately by `background_rag_store`'s
near-duplicate check.

**Post-fix dedup gate status (April 23, 2026):** The dedup gate within
`ms_allis_autonomous_learner_optimized.py` is confirmed running without exception
following the LEARN-01 fix (explicit `np.float64` and `float()` casting enforced on
cosine similarity comparisons). 21,181 records confirmed (April 23, 2026 — exact).
A semantic dedup audit of the `autonomous_learning` collection remains recommended to
surface any potential near-duplicates stored during the LEARN-01 error window.

**As of March 28, 2026**, AAPCAppE scraper documents constitute the first
external-source entries in the ingest pipeline — distinct from autonomous-learner
interaction records. The `spiritual_rag` collection was deduplicated (−19,338 duplicate
vectors) and `psychological_rag` was restored (968 docs) during the March 28 ChromaDB
full audit.

**Implicit significance and structure**
Because the pipeline always writes a structured belief snapshot, and always includes
provenance (dataset, GeoDB ID) and spatial context for centroided entities, the
hippocampal surface naturally emphasizes entities that are well-grounded in both data
and space. Indexing by worldview and dataset also encodes which layers and institutional
perspectives are considered part of the canonical memory. The `needs_verification=TRUE`
flag (100% of entities at March 15 launch baseline) represents the initial state before
the POC verification loop begins clearing entities as confirmed.

**Planned selection criteria**
The design for this layer goes further, envisioning explicit logic that prioritizes:

- High-impact or sensitive programs and features, including governance- or
  safety-related infrastructure
- Novel or under-represented combinations of locations, populations, and benefit rules
- Episodes where beliefs were corrected or forked across worldviews
- Repeatedly accessed regions or entities that merit summarized, higher-level
  hippocampal entries
- Entities where `confidence_decay` has fallen below threshold (future integration with
  POC verification loop)
- `autonomous_learner` records with high semantic similarity to repeated query patterns
  (candidates for summary consolidation)

---

## 14.4 Transformation into Long-Term Memory

When an entity passes through the GBIM + belief + Chroma pipeline, it is transformed
into durable structures that can be joined and queried from multiple angles.

**Structured beliefs and metadata in PostgreSQL (production `msallis-db`, host
port 5433, 127.0.0.1)**
GBIM entities receive normalized belief rows in `gbim_belief_normalized` capturing
identity, spatial footprint, program semantics, and provenance. As of March 15, 2026,
every belief row also carries `last_verified`, `confidence_decay` (multiplier applied
by Phase 5 of the 9-phase pipeline), and `needs_verification`. This relational/JSONB
structure serves as the canonical long-term representation.

**Documents and metadata in ChromaDB `geospatialfeatures` (container port 8000 / host
port 8002, `chroma_data` volume)**
Centroid-bearing entities are added to the `geospatialfeatures` collection as simple
documents with rich metadata. All vectors use `all-minilm:latest` (384-dim):

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

This provides a fast hippocampal index for metadata-filtered recall backed by the
persistent `chroma_data` Docker volume. ★ The full ChromaDB corpus spans **48 active
collections and ~6,740,611 total vectors** (April 23, 2026 confirmed baseline).

**Community interaction records in ChromaDB `autonomous_learner` (container port 8000 /
host port 8002, `chroma_data` volume)**
Each community interaction processed by the autonomous learning subsystem is written as
a document + metadata record in `autonomous_learner`, embedded via `all-minilm:latest`
(384-dim). At Phase 1.45, the top-5 most semantically relevant records are prepended to
every production prompt. **21,181 records (April 23, 2026 — exact); dedup gate running
cleanly with explicit `np.float64` and `float()` casting enforced (LEARN-01 resolved
April 1, 2026).**

**Spatial anchoring via geospatial layers**
Because beliefs carry centroids, SRIDs, and optional administrative labels, hippocampal
entries can be linked back to counties, cities, watersheds, and other layers maintained
in production `msallisgis` (host **5433**, **16 GB**, **294 tables**) and forensic
`msallisgis` (host **5432**, **17 GB**, **314 tables** — forensic only). The
`zcta_wv_centroids` table (993 rows) provides the canonical ZIP-level spatial anchors.
This connects abstract programs and features to specific West Virginia places.

---

## 14.5 Temporal Organization and Decay

**Current behavior (★ April 23, 2026)**
Every GBIM entity in the relevant worldview receives a normalized belief row with
`last_verified`, `confidence_decay`, and `needs_verification` fields. The
`confidence_decay` multiplier is applied at Phase 5 of every production 9-phase
pipeline request (Chapter 17). The `autonomous_learner` collection provides a
complementary temporal signal through its record count: **21,181 records (April 23,
2026 — exact)**, with older records naturally becoming less semantically prominent as
newer interactions are added and nearest-neighbor retrieval at Phase 1.45 surfaces the
most relevant.

The April 1, 2026 crash-loop and recovery is a documented temporal event in the
learner's history: the 57-item post-fix count was the recovery baseline, not the
operating total. The `spiritual_rag` deduplication (−19,338 vectors, March 28) is an
example of retroactive temporal curation that the temporal organization subsystem should
eventually automate. The `msallis_docs` collection growing from 4,192 (March 28) to
7,465 items (April 16) is a further illustration of the ongoing temporal expansion of
the hippocampal substrate.

**POC verification loop (highest-priority future work)**
The POC verification loop will automate the process of re-contacting a resource's
designated point of contact when `needs_verification=TRUE` and resetting `confidence`
to 1.0 on confirmation. Until implemented, the flag-and-attenuate approach via
`confidence_decay` serves as the operative temporal decay mechanism.

**Planned temporal hierarchy**
Beyond the current decay system, the design anticipates:

- A recent window of high-granularity belief and hippocampal entries suitable for
  detailed forensic analysis
- Intermediate summarizations that merge multiple similar entities or interactions into
  trend-level records across both `geospatialfeatures` and `autonomous_learner`
- A long-term backbone of especially important precedents, patterns, and
  governance-relevant insights protected from aggressive pruning

---

## 14.6 Interaction with Retrieval and Introspection

**Retrieval feedback loop (9-phase pipeline integration)**
When higher-level services (GIS-RAG at port 8004, WV entangled gateway,
`allis-spiritual-rag` at port 8005) need context during Phase 4 of the 9-phase
pipeline, they:

1. Use worldview, dataset, and spatial constraints (bboxes, centroids, counties,
   `zcta_wv_centroids`) to select candidate GBIM entities and beliefs from
   `msallis.gbim_belief_normalized` (production `msallis-db`, host **5433** ★).
2. Use those provenance keys (`worldview_id`, `dataset`, `geodbid`) as ChromaDB
   metadata filters in the `geospatialfeatures` collection, retrieving relevant
   entities quickly.
3. Apply `confidence_decay` weighting at Phase 5 to attenuate results based on
   verification recency.
4. Join ChromaDB hits back to `gbim_worldview_entity` and `gbim_belief_normalized`
   (production `msallis-db`, host **5433** ★) to assemble answers grounded in both
   beliefs and physical space.
5. Join spatial identifiers to `zcta_wv_centroids` (production `msallisgis`,
   host **5433** ★) and `allis-local-resources-db` (port 5435) for community-anchored
   resource context — **64 verified resources** (all 55 WV counties confirmed,
   April 23, 2026).

**Phase 1.45 active community memory retrieval (deployed March 17, 2026)**
Before Phase 4 RAG, Phase 1.45 performs a distinct and always-on hippocampal retrieval:

1. The incoming query is embedded via `all-minilm:latest` at
   `allis-ollama:11434/api/embeddings` (384-dim).
2. The vector is used to query `autonomous_learner` (★ **21,181 records**, April 23,
   2026 — exact; Phase 1.45 confirmed in April 23 preflight gate).
3. The 5 most semantically similar community interaction records are retrieved
   (documents + metadata + distances).
4. The retrieved memories are prepended to `enhanced_message` before it enters Phase
   2.5 LLM ensemble processing.

This pathway guarantees that every LLM response is grounded in the system's accumulated
community engagement history, not just structured GBIM entities. The two pathways are
complementary: Phase 1.45 supplies experiential, interaction-level context; Phase 4
supplies structured, spatial, and institutional GBIM knowledge.

**Introspective descriptions of memory use**
As the introspective layer evolves (Chapter 13), it can report which GBIM entities,
datasets, and spatial regions were consulted for a given response, which
`autonomous_learner` records were prepended at Phase 1.45, and how their
`confidence_decay` values influenced the result. `allis-memory` / `allis-memory`
(port **8056**, 127.0.0.1) — `/memory/sessions` HTTP 200 confirmed with **14 active
sessions** (authenticated with `ALLIS_API_KEY`, April 23, 2026).

**Optimization over hippocampal histories via 69-DGM cascade**
Self-improving agents in the 69-DGM layer (Chapter 32, `allis-69dgm-bridge` host port
**19000** → internal **9000**, bound to `127.0.0.1:19000`) can treat GBIM + beliefs +
ChromaDB `geospatialfeatures` and `autonomous_learner` as datasets for discovering
weaknesses, biases, or gaps in coverage — for example, which counties are
under-represented, which datasets are heavily relied on, where repeated corrections to
beliefs occur, which entities have the longest-decayed `confidence_decay` values, or
which `autonomous_learner` records are never surfaced by Phase 1.45 retrieval and may
warrant consolidation or pruning.

---

## 14.7 Alignment with Spatial and Governance Goals

**Place-aware memory**
Extensive WV geospatial layers — counties, block groups, census tracts, cities,
facilities, infrastructure, and more — coexist as GBIM entities and beliefs in
production `msallis-db` (host **5433** ★ secured, 127.0.0.1) and PostGIS `msallisgis`
(**16 GB**, **294 tables**, host **5433** ★). By mirroring centroid-bearing entities
into ChromaDB `geospatialfeatures` with worldview IDs, datasets, and spatial metadata,
and by accumulating community interaction records in `autonomous_learner`, consolidation
enables analyses of how particular counties, towns, or facilities have been represented
and served in the system's history. The 993 ZCTA centroids in
`msallisgis.zcta_wv_centroids` provide the canonical ZIP-level anchors for this
place-aware fabric.

**Community-validated institutional continuity**
Community-validated data from Harmony for Hope's Community Champions (stored in
`allis-local-resources-db`, port 5435) is eligible for promotion into the hippocampal
pipeline, ensuring that ground-truth verification by community members feeds durable,
place-grounded memory. As of April 23, 2026, **64 verified resources** (all 55 WV
counties confirmed) represent the current confirmed breadth of community-validated
coverage. Community interaction records in `autonomous_learner` (**21,181 records**,
April 23, 2026) capture the conversational record of this community engagement at a
level of temporal granularity that structured GBIM promotion does not provide.

**Equity, oversight, and temporal accountability**
By combining spatial identifiers, belief metadata (including `confidence_decay` and
`needs_verification`), Phase 1.45 community memory retrieval, and hippocampal retrieval
histories, analysts and agents can examine whether certain communities receive less
assistance, face different patterns of risk, or encounter more frequent
misunderstandings. The `needs_verification` flag makes temporal gaps in confirmation
explicit and auditable.

---

## 14.8 Implementation Status (★ April 23, 2026 — preflight gate all 27 gates ✅ green)

**Confirmed operational (★ 100/100 containers Up — zero Restarting, zero Exited,
April 23, 2026):**

- ✅ `allis-hippocampus` service deployed in **100-container production stack** ★
  (commit `b90f9ff`)
- ✅ ChromaDB `geospatialfeatures` collection active (container port 8000 / host port
  8002, `chroma_data` volume)
- ✅ ChromaDB `autonomous_learner` collection: **21,181 records (April 23, 2026 —
  exact); Phase 1.45 active retrieval confirmed; dedup gate running cleanly**
- ✅ **Embedding model: `all-minilm:latest` (384-dim)** — canonical model for all 48
  ChromaDB collections; `nomic-embed-text` (768-dim) confirmed incompatible
- ✅ `_DummyCollection` error blocking `autonomous_learner` semantic retrieval: RESOLVED
  (March 17)
- ✅ **Production DB:** `msallis-db` host **5433** / container **5432**, bound to
  `127.0.0.1`, role `postgres`, `msallisgis` **16 GB / 294 tables / 11 schemas**
- ✅ **Forensic DB:** `postgis-forensic` host **5432**, role `allis`, `msallisgis`
  **17 GB / 314 tables / 9 schemas** — forensic auditing only
- ✅ GBIM temporal decay deployed: all entities carry `last_verified`,
  `confidence_decay`, `needs_verification`
- ✅ `confidence_decay` multiplier applied at Phase 5 of every production 9-phase
  pipeline request
- ✅ `background_rag_store` routing post-processing back into hippocampal consolidation
- ✅ `geospatialfeatures` collection queried by GIS-RAG (port 8004) and
  `allis-spiritual-rag` (port 8005) during Phase 4 RAG context building
- ✅ Integration with `zcta_wv_centroids` (993 rows, production `msallisgis`,
  host **5433** ★) for spatial anchoring
- ✅ `allis-local-resources-db` (port 5435): **64 verified resources, all 55 WV
  counties confirmed**
- ✅ Phase 1.45 community memory retrieval confirmed; end-to-end GPU pipeline
  **102.58s on RTX 4070** (CPU baseline ~436s archived)
- ✅ `allis-memory` / `allis-memory` (port **8056**, 127.0.0.1): `/memory/sessions`
  HTTP 200 confirmed with **14 active sessions**; `ALLIS_API_KEY` exported and set
- ✅ `ms_allis_autonomous_learner_optimized.py` synced to `services-safe` mirror
  directory
- ✅ **100/100 containers Up — zero Restarting, zero Exited (April 23, 2026)**

**April 16, 2026 — Preflight remediation items (all resolved — historical reference):**

| Item | Description | Resolution |
|:--|:--|:--|
| PREFLIGHT-A | `msallis-db` port 5433 bound to `0.0.0.0` | Orphaned container stopped and removed; recreated via compose; bind confirmed `127.0.0.1:5433` |
| PREFLIGHT-B | `allis-memory:8056` `/memory/sessions` returning HTTP 500 | Exported `ALLIS_API_KEY`; HTTP 200 confirmed with 14 active sessions |
| PREFLIGHT-C | Container count advancement | 96 → 110 → **100** (April 23, 2026) |

**April 1, 2026 — Autonomous Learner Debug Sprint (historical — all RESOLVED):**

| Item | Description | Resolution |
|:--|:--|:--|
| LEARN-01 | `cosine_similarity` returned numpy array — dedup gate raised "truth value of array" error | Fixed: explicit `np.float64` + `float()` casting enforced |
| LEARN-02 | GBIM Query Router (port 7205) returning HTTP 422 on mis-shaped `route` POST | Fixed: learner request schema corrected; `/route` returning HTTP 200 |
| LEARN-03 | `allis-autonomous-learner` crash-loop after empty file (1.54 kB) deployed | Fixed: source patched on host, copied into container, service restarted |

**ChromaDB collections (★ April 23, 2026 confirmed baseline — 48 collections,
~6,740,611 total vectors):**

| Collection | Records / Vectors | Notes |
|:--|:--|:--|
| `gbim_worldview_entities` | 5,416,521 vectors | Authoritative GBIM entity store |
| `autonomous_learner` | **21,181 records (April 23, 2026 exact)** | Phase 1.45 active retrieval; LEARN-01/03 resolved; dedup gate clean |
| `aapcappe_corpus` | 65+ | Accumulation ongoing via `allis-ingest-watcher` |
| `psychological_rag` | **968** ★ restored March 28 | Restored during March 28 audit |
| `spiritual_texts` | **79,181 vectors** | Absorbs former `spiritual_rag` |
| `spiritual_wisdom` | **135 vectors** | Split from former `spiritual_rag` |
| `spiritual_knowledge` | **12 vectors** | Split from former `spiritual_rag` |
| `appalachian_cultural_intelligence` | 890 docs | Threshold ≥563 |
| `GBIM_sample_rows` | 5,000 | Confirmed March 18 |
| `GBIM_sample` | 3 | Confirmed March 18 |
| `msallis-smoke` | 1 | Smoke test record |
| `msallis_docs` | **7,465** ★ confirmed | Expanded from 4,192 (March 28 baseline) |
| `ms_allis_memory` | Active | `allis-memory` API (port 8056 ★) provides authenticated access; 14 active sessions |
| `ms_allis_identity` | 8 constitutional docs ★ | Seeded and query-verified April 16 |
| `conversation_history` | Active ★ | Rebuilt clean April 16 |
| `geospatialfeatures` | 0 | Scaffolded — pending backfill ingest (`all-minilm:latest` 384-dim required) |
| `gbim_entities` | 0 | Empty placeholder — distinct from `gbim_worldview_entities` (5,416,521 vectors) |
| *(additional collections)* | ★ See April 23 baseline | Total: **48 collections, ~6,740,611 vectors** |

**Remaining work:**

**POC verification loop (highest-priority)**
The automated POC verification loop — where the system contacts a resource's designated
point of contact when `needs_verification=TRUE` and resets `confidence` to 1.0 on
confirmation — is not yet automated. Current state: flag-and-attenuate via
`confidence_decay` only.

**Semantic dedup audit of `autonomous_learning` collection (recommended)**
The LEARN-01 dedup gate error window means items may have been stored without dedup
checking. A semantic dedup audit is recommended.

**`geospatialfeatures` ingest and metadata backfill**
The `geospatialfeatures` ChromaDB collection is scaffolded but at 0 records pending
backfill ingest. All backfill embeddings must use `all-minilm:latest` (384-dim).

**Selective storage criteria, temporal hierarchy beyond decay, tighter belief-routing
traces** — designed but not yet implemented.

---

## 14.9 Summary

The consolidation layer captures how recent activity and world-modeling are turned into
lasting structure across two complementary hippocampal pathways: (1) GBIM entities with
normalized beliefs and temporal decay metadata in production `msallis-db` (host
**5433** ★ secured, 127.0.0.1), mirrored as centroid-bearing records into the
`geospatialfeatures` ChromaDB collection, queried by GIS-RAG and spiritual-RAG during
Phase 4; and (2) the `autonomous_learner` ChromaDB collection — **21,181 records
(April 23, 2026 — exact)** — queried via `all-minilm:latest` (384-dim) semantic search
at Phase 1.45 of every production `/chat` request, with top-5 community memories
prepended to `enhanced_message`.

The `allis-hippocampus` service (deployed March 15, 2026, commit `b90f9ff`) functions
as the dedicated hippocampal buffer within the **100-container production stack** (★ all
100 containers Up, April 23, 2026). The **`allis-memory` / `allis-memory` service**
(port **8056** ★) operates as a companion container — `/memory/sessions` HTTP 200
confirmed with **14 active sessions** (authenticated, `ALLIS_API_KEY`). The
`confidence_decay` multiplier applied at Phase 5 of every production request makes
hippocampal temporal state an active, measurable factor in every response. Phase 1.45
community memory retrieval (deployed March 17, 2026) makes `autonomous_learner` a live,
prompt-level input to every response. The critical embedding model lock —
**`all-minilm:latest` (384-dim) for all 48 ChromaDB collections** (★ ~6,740,611 total
vectors, April 23, 2026 confirmed baseline) — ensures collection compatibility and is
a **permanent architectural constraint**.

★ The April 23, 2026 preflight gate — all 27 gates ✅ green — establishes the current
operational baseline: `msallis-db` host **5433** / `postgis-forensic` host **5452**
two-container split confirmed; all containers bound to `127.0.0.1`; zero `0.0.0.0`
exposures; `allis-memory` `/memory/sessions` HTTP 200 / 14 sessions; 100 containers
Up; community resources 64 verified (all 55 WV counties); `msallis_docs` 7,465;
GPU pipeline 102.58s on RTX 4070.

---

## 14.10 Sprint Validation Log — April 23, 2026 Update

### Infrastructure numbers — April 16 → April 23

| Field | April 16 Value | April 23 Value | Source |
|:--|:--|:--|:--|
| Container count | 110 | **100** | `docker ps` April 23 |
| ChromaDB collections | 49 | **48** | ChromaDB v2 API April 23 |
| ChromaDB total vectors | 6,722,589+ | **~6,740,611** | ChromaDB v2 API April 23 |
| `autonomous_learner` records | 21,181+ | **21,181 exact** | April 23, 2026 |
| `msallisgis` tables (production) | 551 | **294** | Two-container split applied |
| `msallisgis` size (production) | 45 GB | **16 GB** | `msallis-db` host 5433 |
| Forensic DB | Not split | **`postgis-forensic` host 5452 / 314 tables / 17 GB** | Two-container split confirmed |
| GPU pipeline | 99–107s | **102.58s confirmed** (RTX 4070) | April 23 |
| CPU baseline | 436s archived | **RETIRED STALE** | Permanent |
| `allis-memory` `/memory/sessions` | HTTP 200 / 14 sessions | **HTTP 200 / 14 sessions confirmed** | April 23 |
| `msallis-db` bind | 127.0.0.1:5433 | **127.0.0.1:5433 confirmed** | April 23 |

### Historical sprint entries (reference)

> **March 27–28, 2026:** AAPCAppE scraper first run (39 sources, 65 docs). Security
> remediation — 96/96 Up. `allis-memory` corrected to 127.0.0.1. ChromaDB 40
> collections, 6,675,442 vectors. `spiritual_rag` deduplicated. `psychological_rag`
> restored. `msallis_docs` 4,192.

> **April 1, 2026:** Autonomous learner debug sprint — LEARN-01, LEARN-02, LEARN-03 all
> resolved. 57-item post-fix recovery baseline confirmed. Accumulation resumed.

> **April 6, 2026:** GPU pipeline active — RTX 4070. End-to-end timing: 99–107s. CPU
> baseline (436s) archived.

> **April 10, 2026:** `autonomous_learner` 21,181+ records confirmed.

> **April 15, 2026:** Hallucination gap closed. Live end-to-end `/chat` passed —
> `architecture_layers: 12`; `truthverdict: score 1.0, action passed`.

> **April 16, 2026:** Preflight gate all 27 gates ✅ green. Container count advanced to
> 110. ChromaDB 49 collections / 6,722,589+ vectors. `msallisgis` 551 tables / 45 GB.
> `msallis_docs` 7,465. Community resources 64 (all 55 WV counties). `msallis-db`
> port 5433 bind corrected to 127.0.0.1. `allis-memory` `/memory/sessions` HTTP 200 /
> 14 sessions. `ms_allis_identity` seeded. `conversation_history` rebuilt.
> **Chapter 14 CLOSED.**

> **April 23, 2026:** Two-container DB split applied. Container count → 100. ChromaDB
> → 48 collections / ~6,740,611 vectors. `autonomous_learner` → 21,181 exact.
> `msallisgis` production → 294 tables / 16 GB. `postgis-forensic` → 314 tables /
> 17 GB. GPU pipeline → 102.58s confirmed. All values propagated throughout chapter.

---

**Chapter 14 is CLOSED. No open items remain. All hippocampal and memory consolidation
services — `allis-hippocampus`, `autonomous_learner` (21,181 records), `allis-memory` /
`allis-memory` (port 8056, 14 active sessions, ALLIS_API_KEY set), ChromaDB v2 (48
collections, ~6,740,611 vectors), `msallis-db` host 5433 (127.0.0.1-bound, 294 tables /
16 GB), `postgis-forensic` host 5452 (314 tables / 17 GB — forensic only), and 64
verified community resources — are production-active as of April 23, 2026.**

---

*Last updated: April 23, 2026 — Carrie Kidd (Mamma Kidd), Mount Hope WV*

*★ April 16, 2026 — CLOSED: Container count updated to 110. ChromaDB 49 collections /
6,722,589+ vectors. `msallisgis` 551 tables / 45 GB. `autonomous_learner` 21,181+
records. `msallis-db` port 5433 bind corrected to 127.0.0.1. `allis-memory`
`/memory/sessions` HTTP 200 / 14 sessions. `ms_allis_identity` seeded.
`conversation_history` rebuilt. §14.10 sprint validation log added. Chapter 14 CLOSED.*

*★ April 23, 2026 UPDATE: Two-container DB split applied throughout — production
`msallis-db` (host 5433 / 294 tables / 16 GB) and forensic `postgis-forensic` (host
5452 / 314 tables / 17 GB). Container count → 100. ChromaDB → 48 collections /
~6,740,611 vectors. `autonomous_learner` → 21,181 exact. GPU pipeline → 102.58s
confirmed. All April 16 OI items remain CLOSED.*
