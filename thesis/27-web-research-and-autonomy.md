> **Why this matters for Polymathmatic Geography**
> This chapter shows how Ms. Jarvis "looks things up" on its own — under constraints — and folds that knowledge back into place‑based memory anchored in PostgreSQL `msjarvisgis` (port 5432, 91 GB, 501 tables, 5.4M+ verified GBIM beliefs). It supports:
> - **P1 – Every where is entangled** by letting external and internal sources about specific communities and regions accumulate together over time in shared ChromaDB + PostgreSQL GeoDB structures.
> - **P3 – Power has a geometry** by centralizing web and autonomous access behind gateways, learners, and filters whose flows and ports can be audited and redesigned.
> - **P5 – Design is a geographic act** by embedding web research outputs directly into the same RAG and PostgreSQL spatial backbones that serve Appalachian governance, benefits, and resilience questions.
> - **P12 – Intelligence with a ZIP code** by steering curiosity through topics selected from West Virginia–relevant queues and knowledge‑gap maps grounded in PostgreSQL GBIM rather than generic, placeless lists.
> - **P16 – Power accountable to place** by making autonomous learning schedulable, loggable, and subject to the same constitutional and identity filters validated against PostgreSQL as user‑facing flows.
>
> As such, this chapter belongs to the **Computational Instrument** tier: it describes how periodic web research and topic selection are implemented as controlled, observable processes that feed back into entangled, place‑aware memory in PostgreSQL `msjarvisgis`.

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: March 27, 2026 — ChromaDB port corrected to 8000; AAPCAppE scraper first-run results added (39 sources, 65 documents in Chroma); autonomous learner record count updated to 21,181; jarvis-rag-server endpoint corrected to /query*

```
┌─────────────────────────────────────────────────────────────┐
│   Autonomous Learning and Web Research Architecture         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Scheduled Learning Cycle                                   │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Topic Selection                               │         │
│  │  -  Configured learning_queue                   │         │
│  │  -  /next-learning-topic (I-containers 8015)    │         │
│  │  -  Knowledge gaps from PostgreSQL GBIM         │         │
│  │  -  15 Appalachian community domains            │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Retrieval & Filtering                         │         │
│  │  ┌──────────────────┬──────────────────────┐   │         │
│  │  │  Internal (RAG)  │  External (Web)      │   │         │
│  │  │  -  ChromaDB 8000 │  -  Web gateways      │   │         │
│  │  │  -  Postgres-     │  -  Domain policies   │   │         │
│  │  │    sourced RAG   │  -  Rate limits       │   │         │
│  │  │    (8003-8005)   │  -  Geographic filters│   │         │
│  │  └──────────────────┴──────────────────────┘   │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Summarization & Embedding                     │         │
│  │  -  ONNX sentence embeddings (384-dim)          │         │
│  │  -  LLM-based summarization                     │         │
│  │  -  Semantic deduplication check                │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Storage Integration                           │         │
│  │  -  ChromaDB collections (append)               │         │
│  │    - autonomous_learner                        │         │
│  │    - ms_jarvis_memory                          │         │
│  │    - conversation_history                      │         │
│  │  -  PostgreSQL msjarvisgis (validated)          │         │
│  │    - High-confidence spatial/institutional     │         │
│  │    - GBIM belief enrichment                    │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  Governance & Safety Gates                                  │
│  -  BBB ethical filtering (8016)                             │
│  -  TruthValidator (vs PostgreSQL GBIM)                      │
│  -  Constitutional guardians                                 │
│  -  Role constraints                                         │
│      ↓                                                       │
│  Future RAG Availability                                    │
│  -  User-driven queries retrieve autonomous content          │
│  -  ULTIMATE flows use enriched contexts                     │
│  -  PostgreSQL GeoDB spatial integration                     │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> **Figure 27.1.** Autonomous learning and web research architecture: scheduled cycles select topics from PostgreSQL GBIM knowledge gaps, retrieve internal (ChromaDB at **8000** + PostgreSQL-sourced RAG) and external (web gateway) content, summarize and embed results, apply governance filters validated against PostgreSQL, and store in ChromaDB (append-only) and PostgreSQL `msjarvisgis` (validated writes), making content available for future user and system queries.

---

## Status as of March 27, 2026

| Category | Details |
|---|---|
| **Implemented now** | `jarvis-autonomous-learner` confirmed running at **127.0.0.1:8425** with ONNX sentence-embedding model cached on host, FastAPI HTTP interface, configurable `learning_queue`, and restart policy `unless-stopped`. `autonomous_learner` ChromaDB collection contains **21,181 records** as of March 14 baseline, growing ≈288/day (see Ch 19 §19.8.10 for full 31-collection inventory). ChromaDB (`jarvis-chroma`, port **8000**, confirmed `/api/v2/heartbeat` 200 March 25) with collections `autonomous_learner`, `ms_jarvis_memory`, `conversation_history`, `jarvis_consciousness`, `spiritual_wisdom` confirmed active and growing. PostgreSQL `msjarvisgis` at **127.0.0.1:5432** (91 GB, 501 tables, 5.4M+ verified GBIM beliefs) as authoritative ground truth for topic selection and validation. I-containers service (port **8015**) providing `GET /next-learning-topic` endpoint querying ChromaDB for knowledge gaps across 15 Appalachian community domains validated against PostgreSQL GBIM. RAG gateways operational: general RAG **8003**, spiritual/GBIM RAG **8005** (queries PostgreSQL-sourced collections), GIS RAG **8004** (queries PostgreSQL GeoDB), WV-entangled gateway **8010**. `jarvis-rag-server` correct endpoint confirmed as `/query` (see Ch 25 §25.9 Patch 3A — `/direct_rag` does not exist). Web research gateways providing structured results with domain policies, rate limits, geographic filters. Learner conducts embedding operations, ChromaDB insertions, topic selections, web-gateway calls with deduplication. System verification scripts report autonomous learner, web research, and RAG servers as "CONFIRMED OPERATIONAL" with collection counts and response times. **March 27, 2026: RAG loaded 53 documents total — 7 new base cultural docs ingested. Live production milestone for the autonomous learning and ingestion path.** **March 27, 2026: AAPCAppE scraper (Ch 30) completed first run — 39 sources, total_runs: 1, 65 documents ingested into Chroma. RAG search returning exact results (emergency protocol + Fayette County utility example confirmed). See §27.1a and Ch 30.** Logging captures embedding operations, PostgreSQL validation, ChromaDB writes, topic selections, web calls. |
| **Partially implemented / scaffolded** | Topic graph (`topic_graph.json`) and session embeddings for entangled topic selection present in historical code but not fully active in current deployment. Autonomous promotion of high-confidence items from ChromaDB to PostgreSQL `msjarvisgis` is not yet automated; requires manual validation. Debug endpoints exposing provenance tracing (which sources used, how ranked, how context assembled) not yet implemented. Spatial integration via GeoDB sync scripts operational but not yet triggered automatically by autonomous learning cycles. Real-time dashboard showing autonomous learning activity, knowledge gap coverage, PostgreSQL write rates not yet implemented. |
| **Future work / design intent only** | Fully automated entangled topic selection using topic graph and session embeddings for structured walks through knowledge space. Automated high-confidence content promotion from ChromaDB to PostgreSQL `msjarvisgis` based on configurable validation thresholds. Real-time debug endpoints for autonomous learning provenance. Automated triggering of GeoDB sync scripts after spatial learning cycles. Dashboard exposing autonomous learning metrics, knowledge gap coverage per Appalachian domain, PostgreSQL enrichment rates. Scheduled introspective reports summarizing autonomous contributions to PostgreSQL GBIM. |

> **Cross-reference:** Autonomous learning integrates with the container paths (Chapter 19), first-stage filtering (Chapter 20), identity-focused retention (Chapter 22), dual tracks (Chapter 23), and feedback mechanisms (Chapter 24). All autonomous outputs are subject to the same BBB safety filtering (Chapter 16) and truth validation against PostgreSQL `msjarvisgis` as user-facing flows. For canonical `ultimatechat` execution where web research appears, see **Chapter 17**.

---

# 27. Web Research and Autonomous Topic Selection

This chapter describes the periodic web‑research and autonomous learning processes that now run as first‑class services alongside user‑facing chat, all grounded in PostgreSQL `msjarvisgis` (port 5432, 91 GB, 501 tables, 5.4M+ verified GBIM beliefs). These processes allow the system to identify topics of interest, collect both internal and external material under constraints validated against PostgreSQL ground truth, and feed that material back into internal stores in a controlled way. The basic pattern — scheduled retrieval via gateways, semantic storage in ChromaDB, validated writes to PostgreSQL, and filtered reuse — parallels retrieval‑augmented and tool‑using designs in the broader literature while being adapted to Ms. Jarvis's WV‑first, PostgreSQL GBIM‑anchored architecture.

---

## 27.1 Role of Periodic Web Research and Autonomous Learning

Periodic web research and autonomous learning serve three primary functions, distinct from heartbeat or status checks, all grounded in PostgreSQL `msjarvisgis`.

**Background updating.** By running independently of direct user queries, the learner keeps selected areas of knowledge current. It periodically retrieves internal embeddings from ChromaDB collections such as `autonomous_learner` and `ms_jarvis_memory` (sourced from or validated against PostgreSQL GBIM, accessed via `jarvis-chroma:8000`), and augments them with freshly retrieved web content via the web‑research gateway. This allows the system's knowledge base to evolve in response to changes in the outside world while maintaining fidelity to PostgreSQL ground truth, rather than only when prompted by users.

**Curiosity and topic exploration.** The learner's `learning_queue`, the `/next-learning-topic` endpoint querying PostgreSQL GBIM knowledge gaps, and its embedding‑based summarization infrastructure allow the system to pursue topics of intrinsic interest and local importance grounded in West Virginia institutional and community data — such as "large language model coordination systems" or Appalachian community resilience themes validated against PostgreSQL. Over time, this queue is extended by suggestions derived from I‑container interests, autonomous logs, governance priorities anchored in PostgreSQL GBIM, and explicit human input.

**Support for later tasks.** Items stored by the learner become part of the corpus available to RAG pipelines and orchestrated reasoning paths. When later questions arise in governance, spatial planning from PostgreSQL GeoDB, or community advice, ULTIMATE and related services can retrieve both user‑driven and autonomously learned material validated against PostgreSQL. This increases the diversity and depth of the contexts used for planning and decision‑making, while preserving a clear boundary between automatically discovered knowledge and PostgreSQL-validated inputs.

These functions operate within bounds set by truth filters validated against PostgreSQL GBIM, Blood–Brain Barrier modules, role‑ and geography‑aware routing anchored in PostgreSQL GeoDB, and logging requirements, ensuring that autonomous knowledge acquisition remains subordinate to safety and governance constraints grounded in PostgreSQL.

### 27.1a AAPCAppE Scraper — First Run Results (March 27, 2026)

> **March 27, 2026:** The AAPCAppE scraper (see **Ch 30** for corpus architecture) completed its first successful run. Scraper reporting:
> - **39 sources** indexed
> - **total_runs: 1**
> - **65 documents** ingested into Chroma on startup
>
> This is the first live execution of the corpus ingestion path described in this chapter. RAG search is returning exact results — emergency protocol and Fayette County utility examples confirmed retrievable. This milestone establishes that the AAPCAppE autonomous ingestion path is operational end-to-end, not merely scaffolded. See **Ch 30** for full corpus architecture and ingestion pipeline documentation.

---

## 27.2 Scheduling, Cadence, and Logging

Autonomous learning and web research run on a regular, observable schedule with explicit tracking of PostgreSQL validation.

**Periodic cadence.** The learner is configured as a long‑lived service that executes a learning cycle at fixed or configurable intervals. Verification reports include fields indicating that `jarvis-autonomous-learner` is "CONFIRMED OPERATIONAL" and that the autonomous research and storage pipeline is active with PostgreSQL connection health confirmed, forming part of a broader integration healthcheck. As of March 14 baseline, the `autonomous_learner` ChromaDB collection contains **21,181 records growing ≈288/day** (see **Ch 19 §19.8.10** for the full 31-collection ChromaDB inventory).

**Coordinated use of RAG and web services.** Within each cycle, the learner constructs embeddings for topic summaries, queries ChromaDB collections for related internal content (sourced from PostgreSQL GBIM, via `jarvis-chroma:8000`), and calls web‑research gateways for external material. Per‑cycle resource use is bounded by explicit limits on the number of RAG and web calls per topic, preventing background learning from starving user‑facing services or PostgreSQL query capacity.

**Logging and status reports.** Learner logs record embedding operations, ChromaDB insertions, topic selections validated against PostgreSQL GBIM, PostgreSQL validation checks, and web‑gateway calls. System‑wide verification scripts summarize autonomous activity with structured tables that list running containers (including `jarvis-autonomous-learner`, `jarvis-rag-server`, `jarvis-web-research`), collection counts, PostgreSQL connection status, and response times. These reports make autonomy visible as part of the system's overall "vitals" anchored to PostgreSQL.

This combination of rhythm, controlled retrieval, PostgreSQL validation, and explicit logging allows operators to monitor and adjust autonomous learning without instrumenting every internal operation.

---

## 27.3 Topic Selection

Each autonomous learning cycle starts by selecting one or more topics to investigate, guided by configuration, identity signals, and PostgreSQL GBIM knowledge gaps.

**Configured topic lists and embeddings.** The learner maintains an internal list of topics to study and uses a sentence‑embedding model to encode both raw texts and higher‑level session summaries. These embeddings structure internal memory and provide a basis for similarity calculations between candidate research items and the existing corpus sourced from PostgreSQL.

**Knowledge‑gap–driven selection.** The `/next-learning-topic` endpoint on the I‑containers service (port **8015**) queries ChromaDB (via `jarvis-chroma:8000`) to identify knowledge gaps across fifteen Appalachian community domains validated against PostgreSQL GBIM beliefs. The endpoint returns a topic, a `source_type` that distinguishes between filling gaps and reinforcing existing knowledge grounded in PostgreSQL, and a set of relevant ChromaDB collection names. The autonomous learner calls this endpoint to pick topics that are informed by its own memory coverage anchored to PostgreSQL rather than a static queue alone.

**Hooks for entangled topic dynamics.** Historical variants of the learner code include scaffolding for a `topic_graph.json` and session embeddings that can be used to construct a graph of related topics anchored in PostgreSQL spatial and institutional features. As in the entangled RAG design, the long‑term plan is to bias future topic selection toward neighbors of recently studied topics, turning autonomous learning into a structured walk through entangled regions of knowledge grounded in PostgreSQL GeoDB.

Topic selection therefore blends configured lists, PostgreSQL GBIM memory‑driven knowledge‑gap suggestions, and entanglement‑ready structures, ensuring that autonomous learning reflects both prior design and current PostgreSQL memory state.

---

## 27.4 Retrieval, Filtering, and Deduplication

Once topics are selected, each cycle performs retrieval and screening to convert raw search results into curated, semantically indexed knowledge validated against PostgreSQL `msjarvisgis`.

**Internal retrieval via ChromaDB and PostgreSQL.** The learner queries internal ChromaDB collections such as `autonomous_learner`, `ms_jarvis_memory`, and `conversation_history` through HTTP‑based ChromaDB clients pointed at `jarvis-chroma:8000`, all sourced from or validated against PostgreSQL GBIM. Retrieved items serve as prior context grounded in PostgreSQL, help identify coverage gaps, and provide material for multi‑document summaries.

**External retrieval via web gateways.** Web search is conducted through dedicated research gateways that return structured results. The learner translates topics into queries, obtains a bounded number of results per cycle, and respects centralized policies on domains and rate limits. External content is validated against PostgreSQL GBIM before acceptance. As of March 25, 2026 sprint, `jarvis-rag-server` correct endpoint is `/query` — the prior `/direct_rag` endpoint does not exist (see **Ch 25 §25.9 Patch 3A**).

**Summarization and structuring.** Internal and external items are combined into intermediate structures that may represent individual sources or aggregated views. The learner uses LLMs and embeddings to summarize and compress these materials into session‑level notes suited for storage and reuse, with validation against PostgreSQL ground truth.

**Semantic deduplication and selective storage.** Before writing new entries to ChromaDB, the learner embeds candidate summaries and compares them with existing vectors. Near duplicates are dropped, with counters recording deduplicated items; genuinely new entries are stored with metadata including `topic`, `source_type`, `url` (if applicable), `collection`, and timestamps. High-confidence items passing additional validation thresholds are promoted to PostgreSQL `msjarvisgis`.

Through this pipeline anchored in PostgreSQL, the learner transforms noisy, redundant search results into a compact, vectorized knowledge base that can be reused across future tasks while maintaining fidelity to PostgreSQL ground truth.

---

## 27.5 Integration with Memory and Spatial Layers

Accepted items from autonomous learning cycles are folded into the same memory and spatial structures anchored in PostgreSQL `msjarvisgis` used by other components.

**Semantic memory collections.** New items are written into ChromaDB collections such as `autonomous_learner` and `ms_jarvis_memory` at `jarvis-chroma:8000`, using the same embedding configuration as the rest of the system. These entries become available to RAG services on ports 8003, 8005 (querying PostgreSQL-sourced GBIM collections), and 8010, and can appear in both autonomous and user‑driven retrieval flows.

**PostgreSQL msjarvisgis validated writes.** High-confidence items passing additional validation thresholds are promoted from ChromaDB to PostgreSQL `msjarvisgis`, enriching the 5.4M+ verified GBIM beliefs with autonomously discovered institutional and community knowledge. This promotion is currently manual; automated promotion based on configurable thresholds is future work. **March 27, 2026: RAG loaded 53 documents total — 7 new base cultural docs ingested. This is a live production milestone for the autonomous learning and ingestion path** (see status table and §27.1a for AAPCAppE scraper first-run context).

**Spatial integration and GIS export.** Existing scripts connect ChromaDB (at `jarvis-chroma:8000`) and PostgreSQL GeoDB, allowing semantic entries to be exported as GeoJSON and PostgreSQL spatial features to be embedded back into ChromaDB collections. Autonomous learning about spatial themes — such as infrastructure, flood risk, or service access — can therefore be tied to PostgreSQL locations and later recovered through GIS RAG querying PostgreSQL GeoDB.

**Belief and identity layers.** Over time, autonomously acquired material about actors, relationships, and norms validated against PostgreSQL GBIM can inform GBIM beliefs, governance reasoning, and identity formation. For instance, repeated autonomous learning about Fayette County service networks validated against PostgreSQL may be reflected in ULTIMATE reports, identity narratives, or spatial‑justice analyses.

Integrating autonomous learning into both ChromaDB semantic and PostgreSQL spatial backbones ensures that background research enriches the same entangled memory stack anchored to PostgreSQL `msjarvisgis` that supports day‑to‑day stewardship.

---

## 27.6 Interaction with Container and Governance Paths

Autonomous outputs are subject to the same container and governance processes validated against PostgreSQL as user‑driven inputs.

**I‑containers and subconscious RAG.** Newly learned items can be treated as candidates for subconscious storage and identity influence validated against PostgreSQL GBIM. The Fifth DGM service and WOAH algorithms can evaluate these items, deciding whether they remain in background ChromaDB collections, are promoted into I‑containers, are validated for PostgreSQL writes, or are filtered out.

**Governance filters and role constraints.** Governance and ethics components validated against PostgreSQL GBIM can restrict topics or sources deemed sensitive, enforcing additional checks on autonomous learning in domains such as health, law, or vulnerable populations. Truth filters, constitutional guardians, and the Blood–Brain Barrier validated against PostgreSQL can be applied both to web research outputs and to the autonomous learner's summaries before they are stored in ChromaDB or promoted to PostgreSQL.

**Background influence on future decisions.** Once admitted to ChromaDB and potentially promoted to PostgreSQL `msjarvisgis`, autonomous items contribute to the contexts retrieved by ULTIMATE and related orchestrators. For example, if autonomous learning repeatedly surfaces new flood‑risk evidence for a region and validates it against PostgreSQL GeoDB, later spatial or governance queries about that region will be answered against a richer, more current evidence set anchored in PostgreSQL.

This integration makes autonomous learning a managed contributor to the broader evaluative and decision‑making apparatus grounded in PostgreSQL, not a free‑floating process.

---

## 27.7 Safeguards and Oversight

Because web research introduces new external material, autonomous learning is equipped with multiple layers of safeguards and oversight validated against PostgreSQL `msjarvisgis`.

**Source restrictions and gateway policies.** Web‑research gateways define permitted domains, result limits, and geographic filters. Centralizing these policies ensures that external access can be tightened or adapted without redeploying the learner, with all outputs subject to PostgreSQL validation.

**Environment‑based gating and operational control.** Environment variables and process supervisors provide simple mechanisms for enabling, disabling, or throttling autonomous learning. Verification scripts explicitly report whether autonomous services are active, whether PostgreSQL connections are healthy, and whether the "complete flow" is working, giving operators a clear picture of autonomy at a glance.

**Logging, verification, and system‑wide reports.** Logs from the learner, web gateways, and RAG servers are combined with periodic verification reports that list running containers, ChromaDB collection counts (e.g. `autonomous_learner` at 21,181 records as of March 14), PostgreSQL connection status, GIS data health, and performance metrics. These reports can be archived to provide an audit trail for when autonomy was active, what it accessed, how it validated against PostgreSQL, and how it interacted with other services.

These safeguards align autonomous learning with the program's glassbox and spatial‑justice commitments grounded in PostgreSQL, keeping curiosity accountable to place and governance.

---

## 27.8 Web Research in the ULTIMATE Path

Beyond background learning, web research participates directly in user‑driven, high‑stakes reasoning validated against PostgreSQL `msjarvisgis`.

**Position in the orchestration pipeline.** In ULTIMATE‑style flows, web research is typically invoked after initial filtering and before deep ensemble reasoning. The main brain may call web gateways alongside PostgreSQL-sourced RAG services (via `jarvis-rag-server:8016/query` — confirmed correct endpoint as of March 25 sprint), then pass the resulting context to the 22-registered / 21-active LLM ensemble and judge stack, ensuring that external content is integrated deliberately and validated against PostgreSQL rather than incidentally.

**Latency and resource considerations.** Web research adds latency, particularly when reaching out to remote sources. Timeouts, bounded result counts, and careful scheduling help prevent web access from dominating response times or PostgreSQL query capacity. Verification scripts measure both chat and web‑research latencies, PostgreSQL query performance, allowing operators to adjust settings and expectations.

**Planned introspection and debugging.** Future versions of the web‑research gateways are intended to expose debug endpoints that show, for a given request, which internal PostgreSQL and ChromaDB sources and which external sources were used, how they were ranked, and how context was assembled with PostgreSQL validation. Combined with autonomous learner and container logs, this will support detailed provenance tracing for complex answers anchored to PostgreSQL.

In this way, web research functions as a shared, policy‑constrained capability validated against PostgreSQL that supports both autonomous and interactive reasoning.

---

## 27.9 Summary

Autonomous web research and topic selection provide Ms. Jarvis with a controlled form of curiosity grounded in PostgreSQL `msjarvisgis` (port 5432, 91 GB, 501 tables, 5.4M+ verified GBIM beliefs): the ability to seek and structure knowledge on a schedule, under constraints validated against PostgreSQL, and with clear integration into long‑term ChromaDB and PostgreSQL memory and spatial layers. By centralizing external access through web‑research gateways, selecting topics via `/next-learning-topic` querying PostgreSQL GBIM knowledge gaps and identity‑aware queues, storing results in ChromaDB collections at `jarvis-chroma:8000` that are also linked to PostgreSQL GIS data, validating high-confidence content for PostgreSQL writes, and subjecting all autonomous outputs to the same container and governance paths validated against PostgreSQL as user‑driven inputs, the system balances the benefits of ongoing learning with the requirements of safety, accountability, and community oversight anchored to PostgreSQL ground truth.

As of March 27, 2026, this chapter's core architecture is validated by live results: the AAPCAppE scraper first run (39 sources, 65 documents — §27.1a), 53-document RAG load with 7 new cultural base docs (§27.5), and the `autonomous_learner` collection at 21,181 records and growing (§27.2). These are no longer design intents — they are confirmed production milestones.
`````
