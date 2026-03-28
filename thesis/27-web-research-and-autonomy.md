> **Why this matters for Polymathmatic Geography**
> This chapter shows how Ms. Jarvis "looks things up" on its own — under constraints — and folds that knowledge back into place-based memory anchored in PostgreSQL `msjarvisgis` (port **5432** ★, **91 GB PostGIS, 501 tables**, 993 ZCTA centroids) and `msjarvis` (port **5433** ★, **5,416,521 GBIM entities** with `confidence_decay` metadata). It supports:
> - **P1 – Every where is entangled** by letting external and internal sources about specific communities and regions accumulate together over time in shared ChromaDB (★ **40 collections, 6,675,442 total vectors**) + PostgreSQL GeoDB structures.
> - **P3 – Power has a geometry** by centralizing web and autonomous access behind gateways, learners, and filters whose flows and ports can be audited and redesigned. ★ BBB gate decisions are now durably logged at `jarvis-memory:8056` (secured March 28).
> - **P5 – Design is a geographic act** by embedding web research outputs directly into the same RAG and PostgreSQL spatial backbones (`msjarvisgis:5432` ★, 91 GB PostGIS, 501 tables, 993 ZCTA centroids) that serve Appalachian governance, benefits, and resilience questions.
> - **P12 – Intelligence with a ZIP code** by steering curiosity through topics selected from West Virginia–relevant queues and knowledge-gap maps grounded in PostgreSQL GBIM from `msjarvis:5433` ★ (5,416,521 entities with `confidence_decay` metadata) rather than generic, placeless lists. ★ AAPCAppE now supplies `msjarvis_docs` (4,192 items) as an additional ZIP-coded substrate.
> - **P16 – Power accountable to place** by making autonomous learning schedulable, loggable, and subject to the same constitutional and identity filters validated against PostgreSQL as user-facing flows. ★ All BBB and `truthverdict` filter decisions now persist to `jarvis-memory:8056` (secured March 28).
>
> As such, this chapter belongs to the **Computational Instrument** tier: it describes how periodic web research and topic selection are implemented as controlled, observable processes that feed back into entangled, place-aware memory in PostgreSQL `msjarvisgis` ★ and `msjarvis` ★.

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*

*Last updated: 2026-03-28 — ★ March 28, 2026: 96/96 containers Up — zero Restarting, zero Exited; `msjarvis` port 5433 restored (5,416,521 GBIM entities with `confidence_decay` metadata); `msjarvisgis` port 5432 confirmed (91 GB PostGIS, 501 tables, 993 ZCTA centroids); ChromaDB full audit (★ **40 active collections, 6,675,442 total vectors**); `jarvis-ingest-api` + `jarvis-ingest-watcher` restored to active inventory; AAPCAppE `msjarvis_docs` expanded to 4,192 items; `jarvis-memory` port 8056 corrected `0.0.0.0` → `127.0.0.1`, `_auth()` confirmed, `JARVIS_API_KEY` set, BBB audit trail persistence secured; `spiritual_rag` deduplicated (−19,338 vectors); `psychological_rag` restored (968 docs); LLM ensemble confirmed 22 proxies registered / 21 active. March 27, 2026: ChromaDB port corrected to 8000; AAPCAppE scraper first-run results added (39 sources, 65 documents in Chroma); autonomous learner record count updated to 21,181; `jarvis-rag-server` endpoint corrected to `/query`.*

```
┌─────────────────────────────────────────────────────────────┐
│   Autonomous Learning and Web Research Architecture         │
│   ★ Updated March 28, 2026 — 96/96 containers Up           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Scheduled Learning Cycle                                   │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Topic Selection                               │         │
│  │  -  Configured learning_queue                   │         │
│  │  -  /next-learning-topic (I-containers 8015 ★) │         │
│  │  -  Knowledge gaps from msjarvis:5433 ★ GBIM   │         │
│  │     5,416,521 entities, confidence_decay        │         │
│  │  -  15 Appalachian community domains            │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Retrieval & Filtering                         │         │
│  │  ┌──────────────────┬──────────────────────┐   │         │
│  │  │  Internal (RAG)  │  External (Web)      │   │         │
│  │  │  - ChromaDB ★    │  - Web gateways ★    │   │         │
│  │  │    8000 ★        │  - Domain policies   │   │         │
│  │  │    40 collections│  - Rate limits       │   │         │
│  │  │    6,675,442 vecs│  - Geographic filters│   │         │
│  │  │  - Postgres-     │  - AAPCAppE ingest ★ │   │         │
│  │  │    sourced RAG   │    jarvis-ingest-api  │   │         │
│  │  │    (8003-8005 ★) │    + ingest-watcher ★│   │         │
│  │  │    msjarvis:5433 │                      │   │         │
│  │  │    msjarvisgis:  │                      │   │         │
│  │  │    5432 ★        │                      │   │         │
│  │  └──────────────────┴──────────────────────┘   │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Summarization & Embedding                     │         │
│  │  -  ONNX sentence embeddings (384-dim)          │         │
│  │  -  LLM-based summarization (21 active ★)       │         │
│  │  -  Semantic deduplication check                │         │
│  │     ★ spiritual_rag: −19,338 vecs deduped       │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Storage Integration                           │         │
│  │  -  ChromaDB collections (append) ★            │         │
│  │    - autonomous_learner (21,181 records ★)     │         │
│  │    - ms_jarvis_memory                          │         │
│  │    - conversation_history                      │         │
│  │    - msjarvis_docs (4,192 items ★ AAPCAppE)    │         │
│  │    - psychological_rag (968 docs ★ restored)   │         │
│  │    ★ 40 total collections, 6,675,442 vectors   │         │
│  │  -  PostgreSQL msjarvisgis:5432 ★ (validated)  │         │
│  │    - High-confidence spatial/institutional     │         │
│  │    - 91 GB PostGIS, 501 tables, 993 ZCTAs      │         │
│  │  -  PostgreSQL msjarvis:5433 ★ (validated)     │         │
│  │    - GBIM belief enrichment                    │         │
│  │    - 5,416,521 entities, confidence_decay      │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  Governance & Safety Gates                                  │
│  -  BBB ethical filtering (8016 ★)                          │
│    ★ audit → jarvis-memory:8056 (secured March 28)          │
│  -  TruthValidator (vs msjarvis:5433 ★ GBIM)                │
│  -  Constitutional guardians                                 │
│  -  Role constraints                                         │
│      ↓                                                       │
│  Future RAG Availability                                    │
│  -  User-driven queries retrieve autonomous content          │
│  -  ULTIMATE flows use enriched contexts                     │
│  -  PostgreSQL GeoDB spatial integration ★                   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> **Figure 27.1.** Autonomous learning and web research architecture: scheduled cycles select topics from PostgreSQL GBIM knowledge gaps (`msjarvis:5433` ★, 5,416,521 entities with `confidence_decay` metadata), retrieve internal (ChromaDB at **8000** ★, ★ 40 collections, 6,675,442 total vectors + PostgreSQL-sourced RAG) and external (web gateway + ★ AAPCAppE `jarvis-ingest-api`/`jarvis-ingest-watcher`) content, summarize and embed results (★ `spiritual_rag` −19,338 deduped), apply governance filters validated against PostgreSQL (★ audit → `jarvis-memory:8056`), and store in ChromaDB (append-only; ★ `msjarvis_docs` 4,192 items, `psychological_rag` 968 docs restored) and PostgreSQL `msjarvisgis:5432` ★ (validated writes, 91 GB PostGIS, 501 tables, 993 ZCTA centroids), making content available for future user and system queries.

---

## Status as of ★ March 28, 2026

| Category | Details |
|---|---|
| **Implemented now** | `jarvis-autonomous-learner` confirmed running at **127.0.0.1:8425** ★ with ONNX sentence-embedding model cached on host, FastAPI HTTP interface, configurable `learning_queue`, and restart policy `unless-stopped`. `autonomous_learner` ChromaDB collection contains **21,181 records** as of March 14 baseline, growing ≈288/day (see Ch 19 §19.8.10 for full ★ 40-collection ChromaDB inventory). ChromaDB (`jarvis-chroma`, port **8000** ★, confirmed `/api/v2/heartbeat` 200 March 25; ★ confirmed Up March 28; ★ **40 active collections, 6,675,442 total vectors** as of March 28 full audit) with collections `autonomous_learner`, `ms_jarvis_memory`, `conversation_history`, `jarvis_consciousness`, `spiritual_wisdom` (★ deduplicated −19,338 vectors March 28), `psychological_rag` (★ restored 968 docs March 28), `msjarvis_docs` (★ expanded 4,192 items March 28, AAPCAppE) confirmed active and growing. PostgreSQL `msjarvisgis` at **127.0.0.1:5432** ★ (91 GB PostGIS, 501 tables, 993 ZCTA centroids) as authoritative spatial ground truth for topic selection and validation. PostgreSQL `msjarvis` at **127.0.0.1:5433** ★ (5,416,521 GBIM entities with `confidence_decay` metadata, restored March 28) as authoritative GBIM belief store — topic selection knowledge-gap queries are now grounded against this richer evidentiary substrate, with `confidence_decay` weighting available. I-containers service (port **8015** ★) providing `GET /next-learning-topic` endpoint querying ChromaDB for knowledge gaps across 15 Appalachian community domains validated against PostgreSQL GBIM (`msjarvis:5433` ★). RAG gateways operational ★: general RAG **8003**, spiritual/GBIM RAG **8005** (queries PostgreSQL-sourced collections from `msjarvis:5433` ★), GIS RAG **8004** (queries PostgreSQL GeoDB `msjarvisgis:5432` ★), WV-entangled gateway **8010**. `jarvis-rag-server` correct endpoint confirmed as `/query` (see Ch 25 §25.9 Patch 3A — `/direct_rag` does not exist). Web research gateways providing structured results with domain policies, rate limits, geographic filters. ★ **AAPCAppE ingest pipeline operational** (`jarvis-ingest-api` + `jarvis-ingest-watcher`, ★ restored to active inventory March 28): 39 sources, total_runs: 1, 65 documents ingested on first run (March 27); `msjarvis_docs` 4,192 items; RAG search returning exact results (emergency protocol + Fayette County utility example confirmed). ★ **BBB audit trail secured**: `jarvis-memory:8056` corrected `0.0.0.0` → `127.0.0.1`, `_auth()` confirmed, `JARVIS_API_KEY` set (March 28) — all BBB and `truthverdict` autonomous learning filter decisions durably logged. System verification scripts report autonomous learner, web research, and RAG servers as "CONFIRMED OPERATIONAL" with collection counts and response times. **March 27, 2026: RAG loaded 53 documents total — 7 new base cultural docs ingested. Live production milestone for the autonomous learning and ingestion path.** **March 27, 2026: AAPCAppE scraper (Ch 30) completed first run — 39 sources, total_runs: 1, 65 documents ingested into Chroma. RAG search returning exact results — emergency protocol + Fayette County utility example confirmed. See §27.1a and Ch 30.** Logging captures embedding operations, PostgreSQL validation, ChromaDB writes, topic selections, web calls. ★ **96/96 containers Up — zero Restarting, zero Exited** as of March 28, 2026. |
| **Partially implemented / scaffolded** | Topic graph (`topic_graph.json`) and session embeddings for entangled topic selection present in historical code but not fully active in current deployment. Autonomous promotion of high-confidence items from ChromaDB to PostgreSQL `msjarvisgis` ★ is not yet automated; requires manual validation. Debug endpoints exposing provenance tracing (which sources used, how ranked, how context assembled) not yet implemented. Spatial integration via GeoDB sync scripts operational but not yet triggered automatically by autonomous learning cycles. Real-time dashboard showing autonomous learning activity, knowledge gap coverage, PostgreSQL write rates not yet implemented. |
| **Future work / design intent only** | Fully automated entangled topic selection using topic graph and session embeddings for structured walks through knowledge space grounded in `msjarvis:5433` ★ GBIM. Automated high-confidence content promotion from ChromaDB to PostgreSQL `msjarvisgis` ★ based on configurable validation thresholds. Real-time debug endpoints for autonomous learning provenance. Automated triggering of GeoDB sync scripts after spatial learning cycles. Dashboard exposing autonomous learning metrics, knowledge gap coverage per Appalachian domain, PostgreSQL enrichment rates. Scheduled introspective reports summarizing autonomous contributions to PostgreSQL GBIM (`msjarvis:5433` ★, 5,416,521 entities). ★ Judge pipeline upgrade from `heuristic_contradiction_v1` to RAG-grounded truth scoring querying `msjarvis:5433` ★ and `msjarvisgis:5432` ★ (Chapter 7 §7.8) — both stores confirmed at correct ports; upgrade sprint pending. |

> **Cross-reference:** Autonomous learning integrates with the container paths (Chapter 19), first-stage filtering (Chapter 20), identity-focused retention (Chapter 22), dual tracks (Chapter 23), and feedback mechanisms (Chapter 24). All autonomous outputs are subject to the same BBB safety filtering (Chapter 16; ★ audit → `jarvis-memory:8056`) and truth validation against PostgreSQL `msjarvisgis` ★ and `msjarvis` ★ as user-facing flows. For canonical `ultimatechat` execution where web research appears, see **Chapter 17**.

---

# 27. Web Research and Autonomous Topic Selection

This chapter describes the periodic web-research and autonomous learning processes that now run as first-class services alongside user-facing chat, all grounded in PostgreSQL `msjarvisgis` (port **5432** ★, **91 GB PostGIS, 501 tables**, 993 ZCTA centroids) and `msjarvis` (port **5433** ★, **5,416,521 GBIM entities** with `confidence_decay` metadata). These processes allow the system to identify topics of interest, collect both internal and external material under constraints validated against PostgreSQL ground truth, and feed that material back into internal stores in a controlled way. The basic pattern — scheduled retrieval via gateways, semantic storage in ChromaDB (★ 40 active collections, 6,675,442 total vectors), validated writes to both PostgreSQL stores, and filtered reuse — parallels retrieval-augmented and tool-using designs in the broader literature while being adapted to Ms. Jarvis's WV-first, PostgreSQL GBIM-anchored architecture.

---

## 27.1 Role of Periodic Web Research and Autonomous Learning

Periodic web research and autonomous learning serve three primary functions, distinct from heartbeat or status checks, all grounded in PostgreSQL `msjarvisgis` ★ and `msjarvis` ★.

**Background updating.** By running independently of direct user queries, the learner keeps selected areas of knowledge current. It periodically retrieves internal embeddings from ChromaDB collections such as `autonomous_learner` and `ms_jarvis_memory` (sourced from or validated against PostgreSQL GBIM from `msjarvis:5433` ★, accessed via `jarvis-chroma:8000` ★; ★ 40 collections, 6,675,442 total vectors), and augments them with freshly retrieved web content via the web-research gateway. This allows the system's knowledge base to evolve in response to changes in the outside world while maintaining fidelity to PostgreSQL ground truth, rather than only when prompted by users. ★ As of March 28, 2026: the AAPCAppE ingest pipeline (`jarvis-ingest-api` + `jarvis-ingest-watcher`, restored to active inventory) provides a second, always-on background updating pathway that operates independently of both user queries and the web-research gateway — community resource documents enter `msjarvis_docs` (4,192 items) continuously.

**Curiosity and topic exploration.** The learner's `learning_queue`, the `/next-learning-topic` endpoint querying PostgreSQL GBIM knowledge gaps from `msjarvis:5433` ★ (5,416,521 entities with `confidence_decay` metadata), and its embedding-based summarization infrastructure allow the system to pursue topics of intrinsic interest and local importance grounded in West Virginia institutional and community data — such as "large language model coordination systems" or Appalachian community resilience themes. ★ The `confidence_decay` metadata on `msjarvis:5433` ★ entities provides a graded knowledge-gap signal: beliefs with high `confidence_decay` are weaker anchors and represent stronger candidates for targeted autonomous research to refresh or corroborate. Over time, this queue is extended by suggestions derived from I-container interests, autonomous logs, governance priorities anchored in PostgreSQL GBIM, and explicit human input.

**Support for later tasks.** Items stored by the learner become part of the corpus available to RAG pipelines and orchestrated reasoning paths. When later questions arise in governance, spatial planning from PostgreSQL GeoDB (`msjarvisgis:5432` ★, 501 tables, 993 ZCTA centroids), or community advice, ULTIMATE and related services can retrieve both user-driven and autonomously learned material validated against PostgreSQL. This increases the diversity and depth of the contexts used for planning and decision-making, while preserving a clear boundary between automatically discovered knowledge and PostgreSQL-validated inputs.

These functions operate within bounds set by truth filters validated against `msjarvis:5433` ★ GBIM entities, Blood–Brain Barrier modules (★ audit → `jarvis-memory:8056` secured March 28), role- and geography-aware routing anchored in PostgreSQL GeoDB (`msjarvisgis:5432` ★), and logging requirements, ensuring that autonomous knowledge acquisition remains subordinate to safety and governance constraints grounded in PostgreSQL.

### 27.1a AAPCAppE Scraper — First Run Results (March 27, 2026; ★ pipeline active March 28)

> **March 27, 2026:** The AAPCAppE scraper (see **Ch 30** for corpus architecture) completed its first successful run. Scraper reporting:
> - **39 sources** indexed
> - **total_runs: 1**
> - **65 documents** ingested into Chroma on startup
> - ★ **`msjarvis_docs` expanded to 4,192 items** as of March 28 (subsequent AAPCAppE ingest runs)
>
> This is the first live execution of the corpus ingestion path described in this chapter. RAG search is returning exact results — emergency protocol and Fayette County utility examples confirmed retrievable. This milestone establishes that the AAPCAppE autonomous ingestion path is operational end-to-end, not merely scaffolded. ★ As of March 28, 2026: `jarvis-ingest-api` + `jarvis-ingest-watcher` confirmed restored to active inventory (96/96 Up) — the pipeline is continuously active. See **Ch 30** for full corpus architecture and ingestion pipeline documentation.

---

## 27.2 Scheduling, Cadence, and Logging

Autonomous learning and web research run on a regular, observable schedule with explicit tracking of PostgreSQL validation.

**Periodic cadence.** The learner is configured as a long-lived service that executes a learning cycle at fixed or configurable intervals. Verification reports include fields indicating that `jarvis-autonomous-learner` is "CONFIRMED OPERATIONAL" and that the autonomous research and storage pipeline is active with PostgreSQL connection health confirmed for both `msjarvisgis:5432` ★ and `msjarvis:5433` ★. As of March 14 baseline, the `autonomous_learner` ChromaDB collection contains **21,181 records growing ≈288/day** (see **Ch 19 §19.8.10** for the full ★ 40-collection ChromaDB inventory; ★ total 6,675,442 vectors across all collections as of March 28 full audit).

**Coordinated use of RAG and web services.** Within each cycle, the learner constructs embeddings for topic summaries, queries ChromaDB collections for related internal content (sourced from PostgreSQL GBIM from `msjarvis:5433` ★, via `jarvis-chroma:8000` ★; ★ 40 collections, 6,675,442 total vectors), and calls web-research gateways for external material. Per-cycle resource use is bounded by explicit limits on the number of RAG and web calls per topic, preventing background learning from starving user-facing services or PostgreSQL query capacity. ★ The AAPCAppE ingest pipeline (`jarvis-ingest-api` + `jarvis-ingest-watcher`, restored March 28) runs as a second scheduled ingest process alongside the web-research gateway cycle — its cadence and backpressure policy are candidates for explicit scheduling governance alongside existing learner intervals.

**Logging and status reports.** Learner logs record embedding operations, ChromaDB insertions, topic selections validated against `msjarvis:5433` ★ GBIM entities (5,416,521 beliefs with `confidence_decay` metadata), PostgreSQL validation checks, and web-gateway calls. ★ All BBB and `TruthFilterBBBValidator` gate decisions applied to autonomous learning outputs now persist to `jarvis-memory:8056` (secured March 28) — autonomous learning filter decisions are durably and securely logged alongside user-facing filter decisions. System-wide verification scripts summarize autonomous activity with structured tables that list running containers (including `jarvis-autonomous-learner`, `jarvis-rag-server`, `jarvis-web-research`, ★ `jarvis-ingest-api`, `jarvis-ingest-watcher`), collection counts, PostgreSQL connection status for both stores ★, and response times. These reports make autonomy visible as part of the system's overall "vitals" anchored to PostgreSQL.

This combination of rhythm, controlled retrieval, PostgreSQL validation, and explicit logging allows operators to monitor and adjust autonomous learning without instrumenting every internal operation.

---

## 27.3 Topic Selection

Each autonomous learning cycle starts by selecting one or more topics to investigate, guided by configuration, identity signals, and PostgreSQL GBIM knowledge gaps from `msjarvis:5433` ★.

**Configured topic lists and embeddings.** The learner maintains an internal list of topics to study and uses a sentence-embedding model (ONNX, 384-dim — the only compatible embedding model for all ★ 40 ChromaDB collections, per Ch 19 §19.8.8a) to encode both raw texts and higher-level session summaries. These embeddings structure internal memory and provide a basis for similarity calculations between candidate research items and the existing corpus sourced from PostgreSQL.

**Knowledge-gap–driven selection.** The `/next-learning-topic` endpoint on the I-containers service (port **8015** ★) queries ChromaDB (via `jarvis-chroma:8000` ★; ★ 40 collections, 6,675,442 vectors) to identify knowledge gaps across fifteen Appalachian community domains validated against PostgreSQL GBIM beliefs from `msjarvis:5433` ★ (5,416,521 entities with `confidence_decay` metadata). The endpoint returns a topic, a `source_type` that distinguishes between filling gaps and reinforcing existing knowledge grounded in PostgreSQL, and a set of relevant ChromaDB collection names. ★ The `confidence_decay` metadata on `msjarvis:5433` ★ entities provides a graded signal for gap prioritization: high-decay beliefs represent weaker anchors and stronger candidates for fresh autonomous research. The autonomous learner calls this endpoint to pick topics that are informed by its own memory coverage anchored to PostgreSQL rather than a static queue alone.

**Hooks for entangled topic dynamics.** Historical variants of the learner code include scaffolding for a `topic_graph.json` and session embeddings that can be used to construct a graph of related topics anchored in PostgreSQL spatial and institutional features (`msjarvisgis:5432` ★, 501 tables, 993 ZCTA centroids). As in the entangled RAG design, the long-term plan is to bias future topic selection toward neighbors of recently studied topics, turning autonomous learning into a structured walk through entangled regions of knowledge grounded in PostgreSQL GeoDB.

Topic selection therefore blends configured lists, `msjarvis:5433` ★ GBIM memory-driven knowledge-gap suggestions (graded by `confidence_decay`), and entanglement-ready structures, ensuring that autonomous learning reflects both prior design and current PostgreSQL memory state.

---

## 27.4 Retrieval, Filtering, and Deduplication

Once topics are selected, each cycle performs retrieval and screening to convert raw search results into curated, semantically indexed knowledge validated against PostgreSQL `msjarvisgis` ★ and `msjarvis` ★.

**Internal retrieval via ChromaDB and PostgreSQL.** The learner queries internal ChromaDB collections such as `autonomous_learner`, `ms_jarvis_memory`, `conversation_history`, and `msjarvis_docs` (★ 4,192 items, AAPCAppE) through HTTP-based ChromaDB clients pointed at `jarvis-chroma:8000` ★, all sourced from or validated against PostgreSQL GBIM from `msjarvis:5433` ★. Retrieved items serve as prior context grounded in PostgreSQL, help identify coverage gaps, and provide material for multi-document summaries.

**External retrieval via web gateways and AAPCAppE.** Web search is conducted through dedicated research gateways that return structured results. The learner translates topics into queries, obtains a bounded number of results per cycle, and respects centralized policies on domains and rate limits. External content is validated against `msjarvis:5433` ★ GBIM entities before acceptance. ★ In addition, the AAPCAppE ingest pipeline (`jarvis-ingest-api` + `jarvis-ingest-watcher`, restored March 28) provides a parallel external retrieval pathway: community resource documents from 39 confirmed external sources are continuously harvested and written to `msjarvis_docs` (4,192 items) without requiring per-cycle topic selection queries. As of March 25, 2026 sprint, `jarvis-rag-server` correct endpoint is `/query` — the prior `/direct_rag` endpoint does not exist (see **Ch 25 §25.9 Patch 3A**).

**Summarization and structuring.** Internal and external items are combined into intermediate structures that may represent individual sources or aggregated views. The learner uses LLMs (★ 22 registered / 21 active) and ONNX 384-dim embeddings to summarize and compress these materials into session-level notes suited for storage and reuse, with validation against PostgreSQL ground truth from both stores.

**Semantic deduplication and selective storage.** Before writing new entries to ChromaDB, the learner embeds candidate summaries and compares them with existing vectors. Near duplicates are dropped, with counters recording deduplicated items; genuinely new entries are stored with metadata including `topic`, `source_type`, `url` (if applicable), `collection`, and timestamps. ★ `spiritual_rag` (−19,338 vectors deduped March 28) demonstrates the deduplication pipeline operating at scale. High-confidence items passing additional validation thresholds are promoted to PostgreSQL `msjarvisgis` ★.

Through this pipeline anchored in PostgreSQL, the learner transforms noisy, redundant search results into a compact, vectorized knowledge base (★ 40 collections, 6,675,442 total vectors) that can be reused across future tasks while maintaining fidelity to PostgreSQL ground truth.

---

## 27.5 Integration with Memory and Spatial Layers

Accepted items from autonomous learning cycles are folded into the same memory and spatial structures anchored in PostgreSQL `msjarvisgis` ★ and `msjarvis` ★ used by other components.

**Semantic memory collections.** New items are written into ChromaDB collections such as `autonomous_learner`, `ms_jarvis_memory`, and `msjarvis_docs` (★ 4,192 items, AAPCAppE) at `jarvis-chroma:8000` ★, using the same ONNX 384-dim embedding configuration as the rest of the system. These entries become available to RAG services on ports **8003** ★, **8005** ★ (querying `msjarvis:5433` ★ GBIM collections — 5,416,521 entities with `confidence_decay` metadata), and **8010** ★, and can appear in both autonomous and user-driven retrieval flows.

**PostgreSQL `msjarvisgis` and `msjarvis` validated writes.** High-confidence items passing additional validation thresholds are promoted from ChromaDB to PostgreSQL `msjarvisgis` ★ (91 GB PostGIS, 501 tables, 993 ZCTA centroids), enriching the spatial and institutional record with autonomously discovered knowledge. High-confidence GBIM-relevant items may similarly be promoted to `msjarvis:5433` ★ (5,416,521 entities with `confidence_decay` metadata), enriching the belief store. This promotion is currently manual; automated promotion based on configurable thresholds is future work. **March 27, 2026: RAG loaded 53 documents total — 7 new base cultural docs ingested. This is a live production milestone for the autonomous learning and ingestion path** (see status table and §27.1a for AAPCAppE scraper first-run context). ★ `msjarvis_docs` expanded to 4,192 items (March 28) — a second production milestone for the AAPCAppE ingest path.

**Spatial integration and GIS export.** Existing scripts connect ChromaDB (at `jarvis-chroma:8000` ★; ★ 40 collections, 6,675,442 vectors) and PostgreSQL GeoDB (`msjarvisgis:5432` ★, 993 ZCTA centroids), allowing semantic entries to be exported as GeoJSON and PostgreSQL spatial features to be embedded back into ChromaDB collections such as `geodb_*`. Autonomous learning about spatial themes — such as infrastructure, flood risk, or service access — can therefore be tied to PostgreSQL locations and later recovered through GIS RAG querying PostgreSQL GeoDB.

**Belief and identity layers.** Over time, autonomously acquired material about actors, relationships, and norms validated against `msjarvis:5433` ★ GBIM entities (5,416,521 beliefs with `confidence_decay` metadata) can inform GBIM beliefs, governance reasoning, and identity formation. ★ The `confidence_decay` metadata means that autonomously promoted beliefs begin their lifecycle with a baseline decay score that increases if they are not subsequently corroborated — aligning autonomous learning contributions with the evidentiary discipline of the broader GBIM belief store. For instance, repeated autonomous learning about Fayette County service networks validated against PostgreSQL may be reflected in ULTIMATE reports, identity narratives, or spatial-justice analyses.

Integrating autonomous learning into both ChromaDB semantic (★ 40 collections, 6,675,442 total vectors) and PostgreSQL spatial backbones ensures that background research enriches the same entangled memory stack anchored to PostgreSQL `msjarvisgis` ★ and `msjarvis` ★ that supports day-to-day stewardship.

---

## 27.6 Interaction with Container and Governance Paths

Autonomous outputs are subject to the same container and governance processes validated against PostgreSQL as user-driven inputs.

**I-containers and subconscious RAG.** Newly learned items can be treated as candidates for subconscious storage and identity influence validated against `msjarvis:5433` ★ GBIM entities (5,416,521 beliefs with `confidence_decay` metadata). The Fifth DGM service and WOAH algorithms (★ ACTIVE (stub), `jarvis-woah:7012` confirmed Up March 28) can evaluate these items, deciding whether they remain in background ChromaDB collections (★ 40 collections, 6,675,442 vectors), are promoted into I-containers, are validated for PostgreSQL writes, or are filtered out.

**Governance filters and role constraints.** Governance and ethics components validated against `msjarvis:5433` ★ GBIM entities can restrict topics or sources deemed sensitive, enforcing additional checks on autonomous learning in domains such as health, law, or vulnerable populations. Truth filters, constitutional guardians, and the Blood–Brain Barrier (port **8016** ★) validated against PostgreSQL can be applied both to web research outputs and to the autonomous learner's summaries before they are stored in ChromaDB or promoted to PostgreSQL. ★ All BBB and `TruthFilterBBBValidator` gate decisions for autonomous learning flows now persist to `jarvis-memory:8056` (secured March 28) — governance filter decisions over autonomous outputs are durably logged.

**Background influence on future decisions.** Once admitted to ChromaDB (★ 40 collections) and potentially promoted to PostgreSQL `msjarvisgis` ★ (91 GB PostGIS, 501 tables, 993 ZCTA centroids) or `msjarvis` ★ (5,416,521 GBIM entities), autonomous items contribute to the contexts retrieved by ULTIMATE and related orchestrators. For example, if autonomous learning repeatedly surfaces new flood-risk evidence for a region and validates it against PostgreSQL GeoDB, later spatial or governance queries about that region will be answered against a richer, more current evidence set anchored in PostgreSQL.

This integration makes autonomous learning a managed contributor to the broader evaluative and decision-making apparatus grounded in PostgreSQL, not a free-floating process.

---

## 27.7 Safeguards and Oversight

Because web research introduces new external material, autonomous learning is equipped with multiple layers of safeguards and oversight validated against PostgreSQL `msjarvisgis` ★ and `msjarvis` ★.

**Source restrictions and gateway policies.** Web-research gateways define permitted domains, result limits, and geographic filters. Centralizing these policies ensures that external access can be tightened or adapted without redeploying the learner, with all outputs subject to PostgreSQL validation against `msjarvis:5433` ★ GBIM entities and `msjarvisgis:5432` ★ spatial data.

**Environment-based gating and operational control.** Environment variables and process supervisors provide simple mechanisms for enabling, disabling, or throttling autonomous learning. Verification scripts explicitly report whether autonomous services are active, whether PostgreSQL connections are healthy for both stores ★, and whether the "complete flow" is working, giving operators a clear picture of autonomy at a glance. ★ As of March 28, 2026: 96/96 containers Up — the widest confirmed active scope for autonomous learning oversight.

**Logging, verification, and system-wide reports.** Logs from the learner, web gateways, RAG servers, and ★ `jarvis-ingest-api`/`jarvis-ingest-watcher` (AAPCAppE) are combined with periodic verification reports that list running containers, ChromaDB collection counts (★ 40 active collections, 6,675,442 total vectors; `autonomous_learner` at 21,181 records and growing; `msjarvis_docs` at 4,192 items), PostgreSQL connection status for both stores ★, GIS data health, and performance metrics. ★ All BBB and `TruthFilterBBBValidator` autonomous learning filter decisions now additionally persist to `jarvis-memory:8056` (secured March 28) — providing a durable, authenticated audit trail beyond ephemeral container logs. These reports can be archived to provide a full audit trail for when autonomy was active, what it accessed, how it validated against PostgreSQL, and how it interacted with other services.

These safeguards align autonomous learning with the program's glassbox and spatial-justice commitments grounded in PostgreSQL, keeping curiosity accountable to place and governance.

---

## 27.8 Web Research in the ULTIMATE Path

Beyond background learning, web research participates directly in user-driven, high-stakes reasoning validated against PostgreSQL `msjarvisgis` ★ and `msjarvis` ★.

**Position in the orchestration pipeline.** In ULTIMATE-style flows, web research is typically invoked after initial filtering and before deep ensemble reasoning. The main brain (port **8050** ★) may call web gateways alongside PostgreSQL-sourced RAG services (via `jarvis-rag-server:8016/query` ★ — confirmed correct endpoint as of March 25 sprint), then pass the resulting context to the ★ 22-registered / 21-active LLM ensemble and judge stack, ensuring that external content is integrated deliberately and validated against `msjarvis:5433` ★ GBIM entities (5,416,521 beliefs with `confidence_decay` metadata) rather than incidentally.

**Latency and resource considerations.** Web research adds latency, particularly when reaching out to remote sources. Timeouts, bounded result counts, and careful scheduling help prevent web access from dominating response times or PostgreSQL query capacity for `msjarvisgis:5432` ★ and `msjarvis:5433` ★. Verification scripts measure both chat and web-research latencies, PostgreSQL query performance for both stores ★, allowing operators to adjust settings and expectations.

**Planned introspection and debugging.** Future versions of the web-research gateways are intended to expose debug endpoints that show, for a given request, which internal PostgreSQL (both `msjarvisgis:5432` ★ and `msjarvis:5433` ★) and ChromaDB sources (★ 40 collections) and which external sources were used, how they were ranked, and how context was assembled with PostgreSQL validation. ★ The secured `jarvis-memory:8056` (March 28) audit store provides the durable foundation for this provenance tracing capability — gate decisions affecting web research results are already logged; provenance for RAG and source selection is the next layer. Combined with autonomous learner and container logs, this will support detailed provenance tracing for complex answers anchored to PostgreSQL.

In this way, web research functions as a shared, policy-constrained capability validated against PostgreSQL that supports both autonomous and interactive reasoning.

---

## 27.9 Summary

Autonomous web research and topic selection provide Ms. Jarvis with a controlled form of curiosity grounded in PostgreSQL `msjarvisgis` (port **5432** ★, **91 GB PostGIS, 501 tables**, 993 ZCTA centroids) and `msjarvis` (port **5433** ★, **5,416,521 GBIM entities** with `confidence_decay` metadata): the ability to seek and structure knowledge on a schedule, under constraints validated against PostgreSQL, and with clear integration into long-term ChromaDB (★ 40 active collections, 6,675,442 total vectors) and PostgreSQL memory and spatial layers. By centralizing external access through web-research gateways, selecting topics via `/next-learning-topic` querying `msjarvis:5433` ★ GBIM knowledge gaps (with `confidence_decay` grading available for gap prioritization), storing results in ChromaDB collections at `jarvis-chroma:8000` ★ that are also linked to PostgreSQL GIS data, validating high-confidence content for PostgreSQL writes, and subjecting all autonomous outputs to the same container and governance paths validated against PostgreSQL as user-driven inputs (★ audit → `jarvis-memory:8056`), the system balances the benefits of ongoing learning with the requirements of safety, accountability, and community oversight anchored to PostgreSQL ground truth.

As of ★ March 28, 2026, this chapter's core architecture is validated by confirmed production milestones: the AAPCAppE scraper first run (39 sources, 65 documents — §27.1a) and subsequent expansion (`msjarvis_docs` 4,192 items, `jarvis-ingest-api` + `jarvis-ingest-watcher` confirmed Up); 53-document RAG load with 7 new cultural base docs (§27.5); `autonomous_learner` collection at 21,181 records and growing (§27.2); `msjarvis:5433` ★ restored (5,416,521 GBIM entities with `confidence_decay` metadata, providing graded knowledge-gap signaling for the first time); ★ BBB audit trail secured at `jarvis-memory:8056`; and the widest confirmed container scope — **96/96 Up** — ensuring all autonomous learning service paths are simultaneously active.
