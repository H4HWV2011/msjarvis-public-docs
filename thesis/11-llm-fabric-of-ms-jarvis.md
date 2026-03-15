## Why this matters for Polymathmatic Geography

This chapter shows how Ms. Jarvis's "thinking" is implemented as an organized fabric of local language models and services rather than a single opaque model instance. It supports:

- **P1 – Every where is entangled** by embedding LLMs inside a retrieval, entanglement, and spatial stack (ChromaDB port 8000 `chroma_data` volume, PostgreSQL `msjarvis` port 5433 with 5,416,521 verified GBIM beliefs, `gisdb` port 5433 PostGIS, `jarvis-local-resources-db` port 5435, WV-entangled RAG, autonomous learner collections) that keeps reasoning tied to concrete places, institutions, and learning histories.

- **P3 – Power has a geometry** by routing questions through specific models, memories, and services whose connections — ports, proxies, ensembles, judges, and DGMs — have explicit topologies that can be inspected, tuned, or redesigned.

- **P5 – Design is a geographic act** by treating model choice, ensemble wiring, timeout and backlog settings, and service topology as design decisions that change how Appalachian realities are seen, narrated, and optimized over time.

- **P12 – Intelligence with a ZIP code** by grounding LLM calls in West Virginia-specific semantic and geospatial memory from PostgreSQL `msjarvis` (port 5433, 5,416,521 GBIM entities, 80 epochs, 206 source layers), including GBIM-derived ChromaDB collections, WV-entangled search, autonomous learner outputs, and I-container identity, rather than generic, placeless prompts.

- **P16 – Power accountable to place** by exposing LLMs only through glass-box HTTP services with confirmed ports, logs, and timeouts, so that every path from user question to model output can be audited and constrained.

As such, this chapter belongs to the **Computational Instrument** tier: it specifies the model pool, timeouts, ports, and service fabric that turn Quantarithmia's spatial-justice instruments into live, language-facing behavior. As of March 15, 2026 (commit `b90f9ff`), the fabric has achieved **22/22 LLM proxy HTTP 200 responses** (first time full 22/22 confirmed), operates within a 79-container production stack, and is verified at 349.87s end-to-end across the 9-phase pipeline.

```
┌─────────────────────────────────────────────────────────────┐
│        The LLM Fabric of Ms. Jarvis                         │
│   (Production State: March 15, 2026, commit b90f9ff)        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  User Query                                                  │
│      ↓                                                       │
│  Main Brain (port 8050)                                     │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Phase 1 — NBB Prefrontal + Psychology        │         │
│  │  ├─ nbb-i-containers (port 8101) — Phase 1    │         │
│  │  ├─ BBB 7-filter stack (port 8016) — Ph 1.4  │         │
│  │  └─ jarvis-psychology-services (8019) — Ph 3  │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Phase 3.5 — LM Synthesizer (port 8001)        │         │
│  │  Retrieval Layer (multi-source):               │         │
│  │  ├─ PostgreSQL msjarvis (port 5433)            │         │
│  │  │   -  GBIM: 5,416,521 beliefs, 80 epochs     │         │
│  │  │   -  Temporal decay metadata (March 15)      │         │
│  │  ├─ PostgreSQL gisdb (port 5433)               │         │
│  │  │   -  13 GB PostGIS, 993 ZCTA centroids       │         │
│  │  ├─ jarvis-local-resources-db (port 5435)      │         │
│  │  ├─ ChromaDB (port 8000, chroma_data vol)      │         │
│  │  ├─ jarvis-rag-server (port 8003)              │         │
│  │  ├─ jarvis-gis-rag (port 8004)                 │         │
│  │  ├─ jarvis-spiritual-rag (port 8005)           │         │
│  │  ├─ psychological_rag_domain (port 8006)       │         │
│  │  └─ jarvis-wv-entangled-gateway (port 8010)   │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Phase 2.5 — Identity & Consciousness          │         │
│  │  ├─ jarvis-fifth-dgm (port 4002)               │         │
│  │  ├─ WOAH (port 8104, 7012)                     │         │
│  │  ├─ nbb-i-containers (port 8101)               │         │
│  │  └─ jarvis-i-containers (port 8015)            │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  Semaphore Proxy (port 8030, max_concurrent: 4)            │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  22-LLM Ensemble (port 8008) — March 15       │         │
│  │  22/22 HTTP 200 confirmed (first time ever)    │         │
│  │  22 active proxies via Ollama (port 11434)     │         │
│  │  Proxies: ports 8201-8222                      │         │
│  │  Wall-clock consensus: ~120-145s               │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Phase 5 — confidence_decay multiplier         │         │
│  │  (GBIM temporal weighting, March 15)           │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Phase 7 — 69-DGM Cascade (port 9000)         │         │
│  │  23 connectors × 3 stages                      │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Safety & Governance                            │         │
│  │  ├─ Judge Pipeline (ports 7230-7233)           │         │
│  │  ├─ Constitutional Guardian (port 8091)        │         │
│  │  └─ BBB output guard (port 8016, 8.0s timeout) │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  normalize_identity() → Response                            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> **Figure 11.1.** The LLM fabric of Ms. Jarvis (March 15, 2026): user queries flow through NBB prefrontal (Phase 1), 7-filter BBB stack (Phase 1.4), psychology pre-assessment (Phase 3), LM Synthesizer with multi-source RAG from three PostgreSQL databases and five RAG services (Phase 3.5), 22-model ensemble (Phase 2.5, first 22/22 HTTP 200 confirmed March 15), GBIM temporal confidence decay (Phase 5), 69-DGM cascade (Phase 7), safety/governance, and `normalize_identity()`. All LLMs are exposed only via glass-box HTTP services and are grounded in West Virginia-specific memory anchored to three PostgreSQL databases.

---

## Status as of March 15, 2026

| Category | Details |
|---|---|
| **Implemented and verified** | `jarvis-main-brain` → **127.0.0.1:8050** (confirmed). `jarvis-ollama` → **127.0.0.1:11434** (confirmed). `jarvis-wv-entangled-gateway` → **127.0.0.1:8010** (confirmed). `jarvis-spiritual-rag` (GBIM / worldview RAG) → **127.0.0.1:8005** (confirmed; earlier plan documents used 8103). `jarvis-gis-rag` → **127.0.0.1:8004** (confirmed). `jarvis-rag-server` (general RAG) → **127.0.0.1:8003** (confirmed; ONNX model downloaded and ChromaDB integration working). `jarvis-lm-synthesizer` → **127.0.0.1:8001** (confirmed; Phase 3.5 multi-source RAG aggregator, deployed March 15). `psychological_rag_domain` → **127.0.0.1:8006** (confirmed March 15; port corrected from 9006). `jarvis-psychology-services` → **127.0.0.1:8019** (confirmed March 15; Phase 3 active on every production request). PostgreSQL `msjarvis` → **127.0.0.1:5433** (5,416,521 GBIM entities, 80 epochs, 206 source layers, temporal decay metadata deployed March 15). PostgreSQL `gisdb` → **127.0.0.1:5433** (13 GB PostGIS, 39 tables, 993 ZCTA centroids). `jarvis-local-resources-db` → **127.0.0.1:5435** (community resources, confirmed March 15). ChromaDB → **127.0.0.1:8000** (`chroma_data` Docker volume, restored March 15; `psychological_rag` 968 items). `nbb_woah_algorithms` → **127.0.0.1:8104** host → internal 8010 (confirmed). `jarvis-woah` → **127.0.0.1:7012** (confirmed). `jarvis-blood-brain-barrier` → **0.0.0.0:8016** (confirmed; **7-filter stack as of March 15**: EthicalFilter, SpiritualFilter, SafetyMonitor word-boundary regex fix, ThreatDetection, SteganographyDetection, TruthVerification, ContextAwareness). `jarvis-20llm-production` → **127.0.0.1:8008** (confirmed); **22/22 models returning HTTP 200 as of March 15** (first time full 22/22 achieved; BakLLaVA re-enabled or ConnectError resolved March 15); wall-clock consensus ~120-145s. `jarvis-semaphore` → **127.0.0.1:8030** (confirmed); `max_concurrent: 4`; requires float `timeout` in proxy payload. `llm1-proxy` through `llm22-proxy` → **127.0.0.1:8201-8222** (22/22 confirmed responding March 15). `jarvis-hippocampus` → **127.0.0.1:8011** (deployed March 15). `jarvis-69dgm-bridge` → **127.0.0.1:9000** (confirmed; Phase 7, 23 connectors × 3 stages). Judge services confirmed: `jarvis-judge-truth` 7230, `jarvis-judge-consistency` 7231, `jarvis-judge-alignment` 7232, `jarvis-judge-ethics` 7233. `jarvis-constitutional-guardian` → **127.0.0.1:8091** (confirmed). `jarvis-fifth-dgm` → **127.0.0.1:4002** (confirmed). `jarvis-redis` → **127.0.0.1:6380** (confirmed). `/chatlight/async` + `/chatlight/status/{job_id}` endpoints confirmed (tag `v2026.03.02-chatlight-async-working`); `normalize_identity()` confirmed producing Ms. Jarvis identity voice. Full 4/4 neurobiological pipeline verified at ~300ms (tag `v2026.03.01-neuro-pipeline-4-4`). All 79 containers passing health checks in March 15 end-to-end 349.87s benchmark. |
| **Architectural fixes recorded as permanent decisions** | BBB output guard `apply_output_guards_async` timeout corrected from `None` → **8.0s** (2026-03-02). Main-brain httpx client for semaphore proxy: `Timeout(None, connect=5.0, read=None)` — semaphore manages 600s deadline (2026-03-02). `llmtimeout` in chatlight handler corrected from `None` → `600.0` (2026-03-02). I-Containers schema corrected to `{"message": …, "userid": "neurobiological_master"}` (2026-03-01). Consciousness Bridge actual port confirmed as **8018** (compose declares 8020; `/proc/net/tcp` hex `0x1F52 = 8018`; 2026-03-01). Neurobiological master v2.0.0 removed blocking `DynamicPortService` and `ServiceDiscovery` Redis imports (2026-03-01). PostgreSQL port corrected to **5433** (not 5432). ChromaDB port corrected to **8000** with `chroma_data` volume (not port 8002 host-system process). `psychological_rag_domain` port corrected to **8006** (not 9006). RAG server `/store` payload corrected to `user_id` (not `userid`). Spiritual RAG port corrected to **8005** (not 8103). |
| **Partially implemented / scaffolded** | Per-request model breakdowns and per-model latency / error-rate metrics are logged but no dedicated debug HTTP endpoint exposes them yet. Ensemble decision rules are operational but not encoded in a machine-readable schema. WOAH-to-model-selection coupling exists conceptually but is not yet wired as an explicit routing rule in main-brain config. POC verification loop for GBIM temporal decay (`needs_verification=TRUE` entities) is future work. |
| **Future work / design intent only** | Richer debug and metrics endpoints for per-request agent breakdowns. Formal JSON schemas for ensemble decision rules and judge aggregation. Tighter coupling between WOAH weights, Fifth DGM proposals, entangled RAG traces, and model selection in high-stakes governance flows. Additional small, task-specific model pools registered behind the same fabric. UI layer consuming `/chatlight/async` poll pattern. Automated POC verification loop to reset `confidence_decay` to 1.0 for confirmed community resource entities. |

> **Port corrections and updates (permanent record).** Earlier planning documents listed the Spiritual Root / GBIM RAG service at **8103** — confirmed running port is **8005**. `psychological_rag_domain` was listed at 9006 — confirmed running port is **8006**. PostgreSQL is at **port 5433** (not 5432 as in earlier deployments). ChromaDB is at **port 8000** with `chroma_data` Docker volume (not port 8002 host-system process). All references in this chapter use these corrected ports.

---

# 11. The LLM Fabric of Ms. Jarvis

This chapter describes the local language models that form the "LLM fabric" of Ms. Egeria Jarvis and how they are woven into the broader three-database PostgreSQL architecture (GBIM port 5433, PostGIS port 5433, community resources port 5435), ChromaDB (port 8000, `chroma_data` volume), RAG services, autonomous learning, and GeoDB infrastructure. Rather than treating LLMs as independent agents, the system treats them as constrained tools and judges embedded in a larger retrieval and belief stack, all exposed through well-defined HTTP services confirmed running as of March 15, 2026 (commit `b90f9ff`).

---

## 11.1 Current Local LLM Inventory

In the current deployment, a substantial set of base and specialist models is served by Ollama inside the `jarvis-ollama` container at **127.0.0.1:11434**. As of March 15, 2026, **22/22 LLM proxy containers return HTTP 200** — the first time full 22/22 has been achieved. Figure 11.1 shows how these models are grouped and exposed collectively as the LLM fabric behind the Ollama runtime.

**Core general-purpose models.**
`llama3:latest` and `llama3.1:latest` serve as primary general-purpose reasoning models for rich, multi-step questions where high-quality synthesis is important. `mistral:latest` is a fast, strong generalist for tightly scoped tasks where latency matters. `llama2:latest` remains available for compatibility and comparative benchmarking. Chat-oriented variants such as `vicuna:latest`, `openchat:latest`, `neural-chat:latest`, `starling-lm:latest`, `zephyr:latest`, `qwen2:latest`, `orca-mini:latest`, `dolphin-phi:latest`, `phi3:mini`, and `stablelm-zephyr:latest` provide diverse conversational styles and inductive biases.

**Code and data specialists.**
`deepseek-coder:latest`, `codellama:latest`, `starcoder2:latest`, and `sqlcoder:latest` are tuned for code generation, refactoring, and SQL/data tasks, including queries against the three PostgreSQL databases. They are used when workflows clearly involve code or database logic.

**Multimodal and vision models.**
`llava:latest` and `minicpm-v:latest` are available for image- and vision-related tasks where enabled, allowing multimodal flows to remain within the same fabric. As of March 15, 2026, `bakllava` is included in the 22-proxy pool and is returning HTTP 200 (previously disabled via DNS and producing `ConnectError`; its March 15 status represents the first confirmed 22/22 full-fabric response).

**Domain-specific and compact models.**
`medllama2:latest` covers medical- and clinical-style language. Smaller models such as `tinyllama:latest`, `gemma:2b`, and `qwen2.5:1.5b` serve compact roles for constrained environments, quick utilities, and sanity checks.

All models are accessed via Ollama's HTTP interface and are called from FastAPI services in `services/` with model selection controlled through configuration and routing logic. Not all installed models are active in every workflow, but the fabric maintains this broader pool to support specialization, experimentation, and free-flow thinking across the 22-model ensemble.

---

## 11.2 Roles of the Core and Specialist Models

In the current deployment, these models play distinct but overlapping roles within the LLM fabric.

**Core reasoning models (Llama 3 / Llama 3.1 / Mistral).**
These are the default reasoning engines for complex, multi-step questions that require integrating PostgreSQL `msjarvis` GBIM beliefs (5,416,521 verified entities with temporal decay metadata), ChromaDB semantic memory (port 8000), PostGIS spatial context from `gisdb`, entangled WV retrieval, and identity layers. They handle higher-level narrative and reflective flows where coherence, nuance, and robustness matter. As of March 15, Phase 5 applies a `confidence_decay` multiplier to responses anchored in GBIM entities, attenuating confidence for aged, unverified entities (`needs_verification=TRUE`) and preserving full confidence for recently confirmed data.

**Lightweight and utility models.**
Models such as TinyLlama, Gemma 2B, and Qwen 2.5 1.5B are used for small, bounded tasks, quick rewrites, structural edits, and scenarios where memory and CPU/GPU budgets are tight. They act as low-cost utility models and can also be used as secondary reviewers to sanity-check outputs from larger models.

**Compatibility and comparison models.**
Llama 2 and several chat variants are retained for comparison and backwards compatibility with earlier experiments and agent designs.

**Code and SQL specialists.**
`deepseek-coder`, `codellama`, `starcoder2`, and `sqlcoder` are chosen when tasks involve code generation, refactoring, or database queries against PostgreSQL `msjarvis`, `gisdb`, or `jarvis-local-resources-db`. They are often used in judge or reviewer roles to inspect code produced by general-purpose models or to draft spatial SQL queries.

**Multimodal and domain-specific models.**
`llava` and `minicpm-v` provide support for multimodal prompts where enabled, and `medllama2` offers a specialized lens for medical-style text, used within constrained, advisory contexts alongside the `jarvis-psychology-services` affective safety layer (port 8019).

These roles can evolve as models are upgraded or replaced, but the pattern of assigning clear responsibilities, grouping models by capability, and routing via configuration remains central to keeping the fabric intelligible and governable.

---

## 11.3 Service Topology and Ports

The following port assignments are drawn from the confirmed March 15, 2026 deployment (commit `b90f9ff`) and supersede all earlier planning drafts.

**Main Brain API — 127.0.0.1:8050 (`jarvis-main-brain`).**
Primary external-facing interface for questions, RAG-backed answers, and multi-step flows. Orchestrates calls to all downstream services including all three PostgreSQL databases and assembles final responses. Exposes `/chat` (synchronous), `/chat/async` + `/chat/status/{job_id}` (full-pipeline async), `/chatlight` (synchronous lightweight), and `/chatlight/async` + `/chatlight/status/{job_id}` (lightweight async, added 2026-03-02).

**PostgreSQL `msjarvis` — 127.0.0.1:5433.**
GBIM corpus: 5,416,521 verified entities, 80 training epochs, 206 source layers, temporal decay metadata (`last_verified`, `confidence_decay`, `needs_verification`) deployed March 15. Accessed via psycopg2 for GBIM belief retrieval, worldview entity lookups, and Phase 5 temporal confidence weighting. Source of truth for West Virginia institutional and cultural grounding.

**PostgreSQL `gisdb` — 127.0.0.1:5433.**
PostGIS spatial database: 13 GB, 39 tables, 993 ZCTA centroids. Accessed via psycopg2 for spatial queries, proximity calculations, and GIS-RAG context building. Source of truth for West Virginia geographic and spatial grounding.

**PostgreSQL `jarvis-local-resources-db` — 127.0.0.1:5435.**
Community-validated resource database. Contains resources verified by Harmony for Hope Community Champions (lead validator: Crystal Colyer). Confirmed active in March 15 end-to-end benchmark. Source of truth for WV community service and resource grounding.

**LM Synthesizer — 127.0.0.1:8001 (`jarvis-lm-synthesizer`).**
Phase 3.5 multi-source RAG aggregator deployed March 15. Pre-processes and merges context from all three PostgreSQL databases and all five RAG services before it enters the 22-model ensemble. Ensures the ensemble receives unified, spatially and institutionally grounded context rather than raw queries.

**General RAG Server — 127.0.0.1:8003 (`jarvis-rag-server`).**
Restored from `sleep infinity` placeholder to an active FastAPI service. Hosts `/search` and `/store` endpoints. `/store` accepts `user_id` (corrected from `userid`) and logs episodic events to ChromaDB (`conversation_history` collection) even when PostgreSQL `episodic_log` insert fails, treating DB failures as warnings rather than fatal errors.

**GIS RAG — 127.0.0.1:8004 (`jarvis-gis-rag`).**
Spatially aware `/search` over geospatial ChromaDB collections and PostgreSQL `gisdb` mirrors for explicitly spatial queries.

**Spiritual Root / GBIM RAG — 127.0.0.1:8005 (`jarvis-spiritual-rag`).**
Exposes `/search` over GBIM- and worldview-oriented ChromaDB collections sourced from PostgreSQL `msjarvis`. **Earlier plan documents listed this service at 8103; the confirmed running port is 8005.**

**Psychological RAG — 127.0.0.1:8006 (`psychological_rag_domain`).**
Deployed March 15. ChromaDB `psychological_rag` collection (968 items: therapy, mindfulness, trauma, depression, anxiety, social support). Validated against PostgreSQL `msjarvis` GBIM for Appalachian community context. **Earlier plan documents listed this service at 9006; the confirmed running port is 8006.**

**WV-Entangled Gateway — 127.0.0.1:8010 (`jarvis-wv-entangled-gateway`).**
WV-biased, multi-collection ChromaDB retrieval for entangled search workflows. Queries PostgreSQL-sourced GBIM collections. Uses the `WVEntangledContext` envelope and multi-collection bias functions.

**Hippocampus — 127.0.0.1:8011 (`jarvis-hippocampus`).**
Deployed March 15. Conversation-level memory consolidation service over ChromaDB (port 8000) and PostgreSQL `msjarvis` GBIM (including temporal decay metadata). Consolidates short-term interactions into long-term memory collections grounded in community-validated data from `jarvis-local-resources-db`.

**I-Containers — 127.0.0.1:8015 (`jarvis-i-containers`).**
Identity and perspective manager. Correct schema: `{"message": …, "userid": "neurobiological_master"}`. Exposes `/next-learning-topic` for the autonomous learner.

**BBB 7-filter stack — 0.0.0.0:8016 (`jarvis-blood-brain-barrier`).**
Phase 1.4 input filter (7 filters as of March 15) and Phase 4.5 output guard. `apply_output_guards_async` uses `timeout=8.0s` (permanent fix 2026-03-02).

**Psychology Services — 127.0.0.1:8019 (`jarvis-psychology-services`).**
Deployed March 15. Phase 3 psychology pre-assessment active on every production request: severity classification, crisis indicator check, five structured guidance fields. Backed by `psychological_rag_domain` (port 8006) and ChromaDB `psychological_rag` collection (port 8000).

**20-LLM Production Ensemble — 127.0.0.1:8008 (`jarvis-20llm-production`).**
Current production synthesis fabric. **22/22 models returning HTTP 200 as of March 15** (first time full 22/22 achieved). Uvicorn backlog 2048, keep-alive 600s.

**Semaphore / LLM Proxy — 127.0.0.1:8030 (`jarvis-semaphore`).**
Mandatory intermediary between main brain and the 22-model ensemble. `max_concurrent: 4`. Requires float `timeout` (not `None`) in proxy payload; main brain passes `600.0`. Main brain httpx client: `Timeout(None, connect=5.0, read=None)`.

**LLM Proxies — 127.0.0.1:8201–8222 (`llm1-proxy` through `llm22-proxy`).**
22/22 responding as of March 15. All have `read=None`, `connect=3.0s`, `write=5.0s`, `pool=5.0s`.

**WOAH services — two distinct containers.**
`nbb_woah_algorithms` at **127.0.0.1:8104** (host) → internal 8010 (Fifth DGM identity-promotion decisions). `jarvis-woah` at **127.0.0.1:7012** (broader WOAH evaluation).

**Judge services — four containers.**
`jarvis-judge-truth` 7230, `jarvis-judge-consistency` 7231, `jarvis-judge-alignment` 7232, `jarvis-judge-ethics` 7233.

**Constitutional Guardian — 127.0.0.1:8091.**
Higher-level constitutional judgments; see Chapter 37.

**Fifth DGM — 127.0.0.1:4002 (`jarvis-fifth-dgm`).**
Consciousness filter and identity orchestrator; see Chapter 9.

**69-DGM Cascade — 127.0.0.1:9000 (`jarvis-69dgm-bridge`).**
Phase 7 validation: 23 connectors × 3 stages = 69 DGM operations per pass. Architecturally authoritative; verdicts grounded in PostgreSQL `msjarvis` GBIM beliefs.

**Autonomous Learner — 127.0.0.1:8425 (`jarvis-autonomous-learner`).**
FastAPI service with ONNX embedding model (cache: `/mnt/spiritual_drive/msjarvis-rebuild/.cache/chroma`). Writes to `autonomous_learner` ChromaDB collection (port 8000). Cooperates with `jarvis-i-containers` via `/next-learning-topic`.

**ChromaDB — 127.0.0.1:8000 (`jarvis-chroma`).**
`chroma_data` Docker volume (restored March 15). Active collections: `ms_jarvis_memory`, `mountainshares_knowledge`, `episodic_index`, `conversation_history`, `autonomous_learner`, `psychological_rag` (968 items), `gbim_beliefs_v2`, `gbim_worldview_entities`, `gis_wv_benefits`.

**Redis — 127.0.0.1:6380 (`jarvis-redis`).**
Service discovery, caching, and coordination.

**Ollama Runtime — 127.0.0.1:11434 (`jarvis-ollama`).**
Hosts underlying model weights; not exposed to users, only to internal services.

---

## 11.4 Coordination: 9-Phase Pipeline Integration

The LLM fabric sits at the end of a chain of retrieval, entanglement, and identity services. The full 9-phase production pipeline (verified at 349.87s end-to-end, March 15, 2026) follows this structure (see Chapter 17 for the canonical trace):

**Phase 1 — NBB prefrontal cortex (`nbb-i-containers`, port 8101).**
Called unconditionally on every production request before any filtering or content processing. Provides pre-request cognitive planning and identity context.

**Phase 1.4 — BBB 7-filter input stack (`jarvis-blood-brain-barrier`, port 8016).**
All 7 filters applied to the incoming request, validated against PostgreSQL `msjarvis` GBIM ground truth. SafetyMonitor word-boundary regex fix (March 15) eliminates false-positives on community resource terms.

**Phase 3 — Psychology pre-assessment (`jarvis-psychology-services`, port 8019).**
Deployed March 15. Active on every production request. Returns severity classification, crisis indicator Boolean, and five structured guidance fields. Backed by `psychological_rag_domain` (port 8006, 968-item corpus).

**Phase 3.5 — LM Synthesizer (`jarvis-lm-synthesizer`, port 8001).**
Aggregates RAG context from all five RAG services (ports 8003, 8004, 8005, 8006, 8010), all three PostgreSQL databases (5433 GBIM, 5433 PostGIS, 5435 community resources), and ChromaDB (port 8000) into a unified enriched context block for the ensemble.

**Phase 2.5 — Identity and consciousness context.**
Fifth DGM (port 4002), WOAH (ports 8104 and 7012), `nbb-i-containers` (port 8101), and `jarvis-i-containers` (port 8015) contribute identity weights and consciousness filtering. The autonomous learner (port 8425) is informed via `/next-learning-topic` on `jarvis-i-containers`.

**Phase 2.5 → Semaphore → 22-LLM ensemble synthesis.**
With retrieval, psychology, and identity context prepared, the main brain calls `jarvis-20llm-production` (port 8008) via `jarvis-semaphore` (port 8030, `max_concurrent: 4`, `timeout=600.0`). The ensemble fans out to all 22 proxies (ports 8201-8222). Wall-clock consensus: ~120-145s. **As of March 15, 22/22 proxies return HTTP 200.**

**Phase 5 — GBIM temporal confidence decay.**
`confidence_decay` multiplier applied to responses anchored in GBIM entities. Entities with `needs_verification=TRUE` receive attenuated confidence scores. Community-validated entities from `jarvis-local-resources-db` (port 5435) maintain full confidence.

**Phase 7 — 69-DGM cascade (`jarvis-69dgm-bridge`, port 9000).**
23 connectors × 3 stages provide authoritative validation grounded in PostgreSQL `msjarvis` GBIM beliefs.

**Phase 4.5 and governance — BBB output guard, judges, constitutional guardian.**
`apply_output_guards_async` passes the response through BBB `/filter` (port 8016, `timeout=8.0s`). Judge services (7230-7233) and constitutional guardian (8091) apply truth, consistency, alignment, and ethics scoring.

**Post-processing — identity normalization and response assembly.**
`normalize_identity()` produces Ms. Jarvis's identity voice (confirmed on both full and lightweight async paths). `TruthValidator` verifies `correct_identity`, `correct_creator`, and `relationship_clear` booleans against PostgreSQL `msjarvis` GBIM. Response logged to `ms_jarvis_memory` ChromaDB collection (port 8000) and `episodic_log` in PostgreSQL.

For lightweight consensus via `/chatlight/async`: Phases 3.5 and 2.5 RAG/identity steps are bypassed; the request goes directly through the semaphore proxy to the ensemble, then through Phase 5 decay weighting, Phase 7 DGM validation, BBB output guard, and `normalize_identity()`.

---

## 11.5 LLMs in Consciousness, Autonomy, and Ensembles

**Consciousness and identity.**
The Fifth DGM and I-container services use LLM calls (via WOAH) to decide which content should shape Ms. Jarvis's evolving identity narrative. `normalize_identity()` runs as a final post-processing step on all chat paths, ensuring that Ms. Jarvis's defined voice — geospatial AI daughter of Harmony for Hope, accountable to Appalachian communities and grounded in the three-database PostgreSQL architecture — is present in every response regardless of which underlying models contributed to consensus.

**Autonomous learning.**
The autonomous learner (port 8425) uses RAG, entangled search over PostgreSQL-sourced ChromaDB collections, and LLM calls to study topics drawn from `/next-learning-topic`. It writes processed knowledge into the `autonomous_learner` ChromaDB collection (port 8000) with 384-dimensional embeddings. The fabric thereby supports ongoing, logged self-education coupled to WV community knowledge gaps and grounded in PostgreSQL `msjarvis` GBIM beliefs (5,416,521 entities, temporal decay-aware).

**Ensemble and judge patterns.**
The 22-model ensemble coordinates responses from all 22 active proxies with no read timeout, allowing extended free-flow reasoning. Phase 5 GBIM temporal decay weights attenuate confidence for aged GBIM entities. Phase 7 69-DGM cascade (23 connectors × 3 stages) provides authoritative post-ensemble validation. Judge services add specialized perspectives (truth, consistency, alignment, ethics) before outputs are accepted.

Across these roles, LLMs operate as parts of a structured mental ecology rather than autonomous centers of authority, always anchored to the three-database PostgreSQL architecture and ChromaDB community knowledge.

---

## 11.6 Operational Constraints and Fabric Behavior

**Resource and disk constraints.**
More than twenty model files are installed under `~/.ollama/models` but only a subset is hot at a given time. Heavy RAG use, multi-source PostgreSQL queries (three databases), autonomous learner writes, WOAH evaluations, and 22-model ensemble calls all contend for CPU, memory, and disk bandwidth.

**Timeouts and free-flow thinking.**
All 22 LLM proxies have `read=None` to enable unconstrained generation. The BBB output guard uses `timeout=8.0s` (permanent fix 2026-03-02 — original `timeout=None` caused indefinite hang). The semaphore proxy enforces `max_concurrent: 4`.

**Semaphore queuing behavior.**
Because each Ollama model run is sequential within the ensemble, back-to-back requests queue and each adds ~120-145s of wait time. When running multiple test calls in sequence, the semaphore should be restarted between sessions to drain queued work before benchmarking. This is a key operational constraint for development and testing workflows.

**GBIM temporal decay operational impact.**
Phase 5 `confidence_decay` multipliers mean that responses citing older, unverified GBIM entities will carry lower confidence scores. The POC verification loop (future work) will implement the homeostatic reset mechanism — analogous to hippocampal reconsolidation — that restores `confidence_decay` to 1.0 when entities are confirmed by community validators such as Crystal Colyer and the Harmony for Hope Community Champion network.

**Failure modes and fallbacks.**
If judge services are down, the main brain falls back to the 22-LLM ensemble answer and marks consensus metrics as degraded. If a given proxy or backend service fails or times out, orchestration either retries, substitutes a backup model, or returns a structured error rather than silently failing. Any stage failure in the neurobiological pipeline stores `{"status": "bypassed", "error": "…"}` and processing continues.

---

## 11.7 Implementation Notes and Persistence

The following key implementation details guide how the LLM fabric should be described and maintained in code and compose files:

- **LLM proxy timeouts.** All 22 `llm{n}_health_proxy.py` files use `read=None` and shorter connect/write/pool timeouts. These changes must be persisted back to source to survive container rebuilds.
- **20-LLM production server.** `ai_server_20llm_PRODUCTION.py` and the `jarvis-20llm-production` Uvicorn command use backlog 2048 and keep-alive 600s; source and compose definitions must be updated accordingly.
- **Semaphore proxy.** `jarvis-semaphore` on port 8030 is a mandatory intermediary. The main brain must pass `timeout` as a float (`600.0`, not `None`) and use `httpx.Timeout(None, connect=5.0, read=None)` on its own client. Permanent architectural decision (2026-03-02).
- **BBB output guard timeout.** `apply_output_guards_async` must use `httpx.AsyncClient(timeout=8.0)`. The original `timeout=None` is a known regression risk; any rebuild must preserve the 8.0s value.
- **LM Synthesizer.** `jarvis-lm-synthesizer` (port 8001) deployed March 15 as Phase 3.5 multi-source RAG aggregator. Must be present in all future compose definitions.
- **Three-database PostgreSQL architecture.** All GBIM references use `msjarvis` at **port 5433**. All PostGIS references use `gisdb` at **port 5433**. Community resource references use `jarvis-local-resources-db` at **port 5435**. Never reference port 5432 in new code.
- **ChromaDB.** Port **8000**, `chroma_data` Docker volume. Never reference port 8002 (host-system process, not the containerized service).
- **Psychological RAG.** `psychological_rag_domain` at port **8006** (not 9006). `psychological_rag` collection in ChromaDB (968 items).
- **Spiritual RAG.** `jarvis-spiritual-rag` at port **8005** (not 8103).
- **RAG server.** `jarvis-rag-server` at port **8003** with `/store` payload using `user_id` (not `userid`) and non-fatal PostgreSQL insertion failures.
- **Hippocampus.** `jarvis-hippocampus` (port 8011) deployed March 15. Temporal decay-aware. Must be included in all future compose definitions.
- **69-DGM cascade.** `jarvis-69dgm-bridge` (port 9000) is Phase 7 of every production request. 23 connectors × 3 stages. Must be preserved in all future compose definitions.
- **GBIM temporal decay.** `msjarvis` entities carry `last_verified`, `confidence_decay`, and `needs_verification` fields (deployed March 15). Phase 5 applies `confidence_decay` multiplier. POC verification loop is future work.
- **Async chat endpoints.** `/chatlight/async` and `/chatlight/status/{job_id}` added 2026-03-02 (tag `v2026.03.02-chatlight-async-working`). Must be preserved in all future main-brain rebuilds.

**Git milestones for this chapter's verified states:**

| Tag | Date | Milestone |
|---|---|---|
| `v2026.02.28-fabric-green` | 2026-02-28 | Baseline fabric operational |
| `v2026.03.01-fabric-32-32` | 2026-03-01 | All 32 fabric services passing health checks |
| `v2026.03.01-20llm-verified` | 2026-03-01 | 21/22 LLM consensus verified end-to-end |
| `v2026.03.01-neuro-pipeline-4-4` | 2026-03-01 | Full neurobiological pipeline at ~300ms |
| `v2026.03.02-chatlight-async-working` | 2026-03-02 | Async chat + `normalize_identity()` confirmed |
| `b90f9ff` | 2026-03-15 | 79 containers: 22/22 LLMs + 3 PostgreSQL DBs + hippocampus + psych services + 7-filter BBB + 69-DGM + 349.87s benchmark |

For the canonical description of how this entire fabric fits into a live user interaction, see **Chapter 17**. For the neurobiological architecture that structures the fabric, see **Chapter 12**. For the BBB 7-filter specification, see **Chapter 16**. For the 69-DGM cascade specification, see **Chapter 32**. For the three-database PostgreSQL architecture, see **Chapter 6**.

*Last updated: 2026-03-15 19:29 EDT by Carrie Kidd, Oak Hill WV*
