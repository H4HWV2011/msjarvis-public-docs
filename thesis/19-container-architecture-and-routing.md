## Why this matters for Polymathmatic Geography
This chapter explains how Ms. Jarvis's "containers" receive, sort, and route the flows of experience that later become memory and decision support. It supports:
- **P1 – Every where is entangled** by treating events from people, places, and institutions as a shared stream that must be carefully routed into PostgreSQL `msjarvisgis` (port 5432, 91 GB, 501 tables, 5.4M+ verified GBIM beliefs) and ChromaDB memory.
- **P3 – Power has a geometry** by making explicit which services, ports, and stores stand between communities' data and long-term inference in PostgreSQL.
- **P5 – Design is a geographic act** by encoding how Appalachian events move through Ms. Jarvis and into PostgreSQL spatial, semantic, and commons-oriented stores.
- **P12 – Intelligence with a ZIP code** by prioritizing spatial, governance, and commons contexts from PostgreSQL GeoDB in the way container records are tagged and stored.
- **P16 – Power accountable to place** by using auditable container flows and verification scripts so communities can see where their data goes in PostgreSQL `msjarvisgis` and ChromaDB.

As such, this chapter belongs to the **Computational Instrument** tier: it describes the container and routing structures that turn raw events into traceable, place-aware memory anchored in PostgreSQL.

```
┌─────────────────────────────────────────────────────────────┐
│   Container Architecture and Routing Flow                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Incoming Events                                            │
│  -  User queries (/chat, /chat/async)                        │
│  -  Internal tasks (autonomous learner, Fifth DGM)           │
│  -  External signals                                         │
│  -  Structural changes (GBIM updates)                        │
│      ↓                                                       │
│  Normalization Layer                                        │
│  -  Core fields (ID, timestamps, origin)                     │
│  -  Context (role, geography, tags)                          │
│  -  Content summary                                          │
│  -  Links (PostgreSQL GBIM, ChromaDB, GIS)                   │
│  -  Control flags (safety, urgency, sensitivity)             │
│      ↓                                                       │
│  First-Level Routing                                        │
│  -  Eligibility checks (BBB 7-filter + fail-open)            │
│  -  Phase 1.45 community memory retrieval (all-minilm)       │
│  -  Priority assignment                                      │
│  -  Track assignment                                         │
│      ↓                                                       │
│  ┌──────────────────────┬──────────────────────┐            │
│  │  Affective/Care Path │  Analytical/Tech Path│            │
│  │  -  Psychological RAG │  -  GIS/Spatial       │            │
│  │  -  Community support │  -  Infrastructure    │            │
│  │  -  Ethical interpret │  -  Optimization      │            │
│  └──────────────────────┴──────────────────────┘            │
│      ↓                        ↓                             │
│  Container Records                                          │
│  -  Marked for evaluation                                   │
│  -  Held back or dropped                                    │
│  -  Introspective logs                                      │
│      ↓                                                       │
│  Long-Term Storage                                          │
│  -  PostgreSQL msjarvisgis (port 5432)                       │
│  -    GBIM beliefs (5.4M+ verified)                          │
│  -    GeoDB spatial (501 tables, 91 GB)                      │
│  -  ChromaDB (port 8000, chroma_data volume)                 │
│  -    Semantic collections (384-dim, all-minilm:latest)      │
│  -  I-Containers (port 8015)                                 │
│  -  Redis job state (jarvis-redis:6379, 30-min TTL)          │
│  -  Audit logs                                               │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> **Figure 19.1.** Container architecture and routing flow: incoming events from multiple sources are normalized, evaluated through first-level routing (including Phase 1.45 community memory retrieval via `all-minilm:latest` 384-dim semantic search), distributed across parallel evaluation paths, and stored in PostgreSQL `msjarvisgis` (port 5432, 5.4M+ GBIM beliefs), ChromaDB (`chroma_data` volume, port 8000), and Redis-backed async job state with full audit trails. As of March 18, 2026, all 79 containers are fully compose-managed via Docker Compose v5.1.0 at `~/msjarvis-rebuild-working/msjarvis-rebuild/docker-compose.yml`.

---

# 19. Container Architecture and Routing

This chapter describes the high-level layout of the container-based structures that receive activity from earlier layers and route it into deeper evaluation paths anchored in PostgreSQL `msjarvisgis` (port 5432, 91 GB, 501 tables, 5.4M+ verified GBIM beliefs). The goal is to separate the flow of events into clear stages, so that each stage has a well-defined role in deciding what is ignored, what is kept for background consideration, and what becomes part of PostgreSQL or ChromaDB central stores. In the implemented system, these responsibilities are realized by a set of Dockerized services that cooperate via HTTP and shared data stores. As of March 18, 2026, all 79 production containers are defined in a single `docker-compose.yml` and managed via Docker Compose v5.1.0 — no manual service startup is required beyond `~/jarvis_startup.sh` for the six judge/gateway pipeline containers. Conceptually, this reflects microservice and modular-control patterns as described by Lewis & Fowler and modular coordination work such as Goyal et al.

**Production state (March 18, 2026):**
- All 79 containers: ✅ Fully compose-managed via Docker Compose v5.1.0
- Compose file: `~/msjarvis-rebuild-working/msjarvis-rebuild/docker-compose.yml`
- All `build:` directives: ✅ Converted to `image:` references — no rebuilds on startup
- Hash-prefixed container names: ✅ Resolved — `container_name:` added to all 8 affected containers
- 9 previously missing containers: ✅ Added to compose (3 corpus containers + 6 service containers)
- `hilbert-gateway` port conflict: ✅ Resolved in `docker-compose.yml`
- Docker Compose v1.29.2 `ContainerConfig` crash bug: ✅ Eliminated by upgrade to v5.1.0
- Redis-backed async job system: ✅ Deployed March 17, 2026 (`/chat/async`, `/chat/status`, `/chat/cancel`)
- Health check cache: ✅ 30s TTL, 2s per-service timeout (deployed March 18, 2026)
- End-to-end benchmark: ~436s (optimized from 532s baseline)

---

## 19.1 Position in the Overall System

The container layer sits between external interfaces and the lower-level retrieval, optimization, and global control mechanisms. It is visible both in the main-brain service that handles `/chat` and `/chat/async` requests and in the autonomous learning and Fifth DGM pipelines that generate and refine internal content. Its main responsibilities are to:

- Accept events coming from many sources, including question-handling flows, scheduled jobs, and self-improving processes.
- Normalize these events into a common format that can be evaluated and stored consistently in PostgreSQL `msjarvisgis` and ChromaDB.
- Dispatch normalized items into successive evaluation stages, while obeying system-wide constraints such as safety filters (BBB 7-filter stack with fail-open behavior), resource limits, and service health (30s TTL cache, 2s timeout per service).

Earlier parts of the work have described how information is retrieved from PostgreSQL GBIM, evaluated, and stored. This chapter focuses on how those elements are wrapped in container structures — both conceptual and literal Docker containers — that manage their entry into higher-level evaluative paths and PostgreSQL long-term memory. The full 79-container production stack is defined in a single compose file and requires no manual container management beyond the startup script.

---

## 19.2 Types of Incoming Events

In practice, the intake layer receives several broad categories of events that must be handled in a unified way:

- **Direct interactions**
  User queries and responses that have already passed through initial retrieval from PostgreSQL-sourced RAG and constraint checks via the `jarvis-main-brain` `/chat` pipeline. These include synchronous requests and asynchronous jobs that are tracked via job IDs and status records persisted in Redis (`jarvis-redis:6379`, 30-minute TTL). The `/chat/async` endpoint returns a `job_id` immediately; polling via `/chat/status/{job_id}` retrieves progress and result. True asyncio task cancellation via `/chat/cancel/{job_id}` stops the 21-LLM pipeline mid-run.

- **Internal tasks**
  Results from scheduled analyses, background maintenance jobs, and optimization routines. Examples include outputs from the autonomous learner (21,181 records as of March 18, growing ~288/day), Fifth DGM optimization steps, and WOAH evaluations, which generate candidate content for the I-Container and other long-term structures.

- **External signals**
  Notifications or status changes from connected systems such as messaging platforms, web front ends, or external data sources. These may arrive via dedicated services or be polled and converted into internal events.

- **Structural changes**
  Updates to PostgreSQL `msjarvisgis` memory, GBIM belief graphs, or spatial layers that may require special attention. For instance, a new GBIM graph edge in PostgreSQL, a significant ChromaDB embedding insertion, or an update to access-control metadata can trigger container-level processing and validation.

Each event is accompanied by metadata such as timestamps, role identifiers, user or agent IDs, and source information. Container logic uses this metadata to make routing decisions, enforce policy, and maintain traceability back to PostgreSQL sources.

---

## 19.3 Normalization into Container Records

Before events are passed to deeper stages, they are normalized into container records with a common structure. This normalization is implemented in several places:

- In the `Ms. Jarvis ULTIMATE` main-brain, where incoming `/chat` and `/chat/async` requests are converted into structured request models and then into RAG storage records in ChromaDB backed by PostgreSQL GBIM queries.
- In the autonomous learning and Fifth DGM flows, where internal discoveries are wrapped into I-Container entries.

A typical normalized record includes:

- **Core fields**
  A unique identifier, creation and update timestamps, origin (for example, `user_chat`, `autonomous_learner`, or `external_signal`), and a reference to the initiating service or job.

- **Context**
  Active role or profile, relevant geographic or institutional context from PostgreSQL GeoDB, and tags describing the domain (such as `governance`, `infrastructure`, or `community_culture`). For chat records, this includes the user_id and any declared mode (for example, ultimate vs. simpler paths). For async jobs, the Redis-persisted `job_id` links the normalized record to its lifecycle state.

- **Content summary**
  Key text, numerical values, or structured data extracted from the event. For chat interactions, this is typically a truncated version of the query and response plus any derived summaries. For internal tasks, it may include candidate knowledge statements, metrics, or optimization results.

- **Links**
  References to memory items (ChromaDB embeddings — all 384-dim via `all-minilm:latest` — PostgreSQL GBIM graph nodes/edges at port 5432, relational records), spatial features (PostgreSQL GeoDB entities), and introspective entries (job logs, verification reports). These links make it possible to traverse from a container record back into PostgreSQL underlying stores.

- **Control information**
  Flags indicating initial assessments such as urgency, sensitivity, safety status (for example, BBB-approved or denied — with fail-open on HTTP 500), expected resource cost, and whether the item is considered high-value for long-term retention in PostgreSQL `msjarvisgis`.

This normalization step allows subsequent stages — such as I-Container growth, truth filtering against PostgreSQL GBIM, or consolidation — to apply uniform logic regardless of where the event originated. The overall pattern parallels retrieval and routing architectures in tool-using and agentic LLM systems, as surveyed in Ram et al., Schick et al., and Trivedi et al.

---

## 19.4 First-Level Routing Decisions

Once a record is normalized, the intake layer applies initial routing logic. In the running system, this logic appears in:

- The main-brain's decision to send a request through BBB (7-filter stack with `truth_score` null guard and fail-open on HTTP 500), Phase 1.45 community memory retrieval (`autonomous_learner` via `all-minilm:latest` 384-dim semantic search, top-5 records prepended), PostgreSQL-sourced RAG, web-research, and LLM ensembles, and then to queue RAG storage with specific metadata.
- The autonomous learner and Fifth DGM scripts that decide when to push new candidate items into the I-Container and when to leave them as transient results.

The first-level routing includes:

- **Eligibility checks**
  Confirming that the record is allowed to enter container paths under current global settings. This includes safety checks (BBB 7-filter stack against PostgreSQL GBIM ground truth — with fail-open: if BBB returns HTTP 500, the pipeline continues rather than blocking), role-based constraints, and checks for service availability via health probes (30s TTL cache, 2s timeout per service, URL overrides for ChromaDB `/api/v1/heartbeat` and Ollama `/api/tags`).

- **Phase 1.45 community memory injection**
  After BBB input approval, the main brain generates a 384-dim embedding via `all-minilm:latest` at `jarvis-ollama:11434/api/embeddings`, queries the `autonomous_learner` ChromaDB collection (21,181 records), retrieves the 5 most semantically similar community interaction records, and prepends them to `enhanced_message` before it reaches the 21 LLMs. This is an always-on first-level routing step for every `/chat` and `/chat/async` request.

- **Priority assignment**
  Assigning a simple priority or track indicator that influences ordering and resource allocation. For example, user-facing requests may be processed before low-priority background maintenance items, and safety-relevant events may be escalated for additional scrutiny.

- **Track assignment**
  Deciding whether the record should be sent to specific container subsystems such as the I-Container, psychological RAG domains, PostgreSQL GBIM graph updates, or audit logs. The same record may feed multiple tracks — for instance, both ChromaDB memory and PostgreSQL introspective audit — depending on its control flags.

At this stage, routing focuses on structural compatibility, basic policy, and safety, leaving deeper judgments (such as long-term importance or thematic clustering) to later stages.

---

## 19.5 Parallel Paths

The architecture supports multiple parallel paths that share a common structural pattern: intake → normalization → gating → storage in PostgreSQL or ChromaDB or discard. Conceptually, two broad tracks can be distinguished:

- **Affective and care-oriented paths**
  Used when events are framed in terms of meaning, care, or psychological support. These may involve specialized RAG domains, therapeutic or community-oriented analysis, and services that emphasize ethical interpretation and human impact.

- **Analytical and technical paths**
  Used for more conventional problem-solving tasks, such as infrastructure planning using PostgreSQL GeoDB, spatial reasoning, and optimization over data. These paths emphasize quantitative reasoning, model-based analysis, and technical verification against PostgreSQL GBIM ground truth.

The intake layer uses metadata, simple classifiers, and explicit flags to decide whether a record is best handled by one path, the other, or both. Each path then applies its own evaluation criteria and modules but retains the same overarching sequence of stages: initial safety, context integration from PostgreSQL GBIM, analysis, and optional storage into PostgreSQL long-term structures. Similar dual-track designs — separating meaning-focused and analysis-focused flows — appear in broader discussions of interpretability and explanation, such as Doshi-Velez & Kim and Lipton.

In concrete terms, these paths are supported by distinct services and RAG domains (for example, psychological RAG vs. general knowledge RAG sourced from PostgreSQL GBIM), as well as by specialized orchestration scripts that test different flows (such as the full autonomous learning + Fifth DGM + I-Container route).

---

## 19.6 Outputs of the Routing Layer

After routing, the container layer produces several types of outputs that feed later stages and support evaluation:

- **Records marked for immediate evaluation**
  Items that pass eligibility checks and have sufficient priority are forwarded to downstream evaluators (for example, 21-model LLM consensus, truth validators against PostgreSQL GBIM, or optimization routines). Their container records carry all necessary context and links to PostgreSQL tables. For async requests, the record is linked to a Redis-backed job with 30-minute TTL and true asyncio cancellation support.

- **Records held back or dropped**
  Events may be held back (queued, delayed, or rate-limited) or dropped entirely based on policy. Reasons include safety denials, low priority under heavy load, redundancy detected by RAG similarity checks against ChromaDB, or failure of essential services (fail-open behavior ensures BBB HTTP 500 does not block the full pipeline).

- **Introspective logs and verification entries**
  The system records which paths were chosen, which services were invoked, what PostgreSQL queries were executed, and what the outcomes were. Scripts such as `VERIFYANDTEST.sh` and `verifyallclaims.sh` generate structured summaries of service health, I-Container growth, autonomous learning cycles, ChromaDB status, and PostgreSQL connection health. These introspective outputs make the behavior of the routing layer auditable and support both debugging and research, consistent with AI auditing approaches described by Raji et al. and ISO/IEC 42001 guidance.

Together, these outputs ensure that downstream stages receive appropriately prepared inputs and that routing choices can be reconstructed and analyzed when necessary, with full traceability back to PostgreSQL `msjarvisgis` sources.

---

## 19.7 Conceptual Summary

Conceptually, the container architecture provides a structured way to receive, normalize, and direct events into deeper evaluative paths anchored in PostgreSQL `msjarvisgis` (port 5432, 91 GB, 501 tables, 5.4M+ verified GBIM beliefs). It defines how diverse inputs — user interactions, internal learning results, external signals, and structural changes — enter the system's evaluative core. By enforcing clear stages and control flags, it supports disciplined decision-making about what is ignored, what is kept for background consideration, and what is integrated into PostgreSQL central memory and GBIM belief structures.

The remaining sections of this chapter ground this abstraction in the current production deployment topology, focusing on Docker containers, port mappings, compose management, and service roles as of March 18, 2026.

---

## 19.8 Operational Container Topology (March 18, 2026)

This section summarizes the current production deployment topology, grounding the abstract container architecture in a concrete set of services. It should be read as the authoritative operational state as of March 18, 2026 — superseding the December 2025 snapshot documented in earlier drafts. The topology is derived from `~/msjarvis-rebuild-working/msjarvis-rebuild/docker-compose.yml` (Docker Compose v5.1.0), runtime `docker ps` output, `~/jarvis_startup.sh`, and verification scripts.

> **Compose management baseline (March 17–18, 2026):**
> All 79 production containers are now defined in a single `docker-compose.yml`. All `build:` directives have been converted to `image:` references — no image rebuilds occur on startup. Docker Compose was upgraded from v1.29.2 (which caused a `ContainerConfig` crash bug) to v5.1.0. Nine containers previously missing from compose have been added: 3 corpus containers (`jarvis-local-resources`, and 2 others) and 6 service containers (`jarvis-hippocampus`, `jarvis-gis-rag`, `jarvis-spiritual-rag`, and 3 others). The `hilbert-gateway` port conflict identified during the March 17 compose audit has been resolved. Eight containers previously running with hash-prefixed names (e.g., `981f44e18cf6_jarvis-20llm-production`) now have clean, stable names via `container_name:` entries.

### Core Orchestration Layer

| Container | Port Mapping | Role |
|---|---:|---|
| jarvis-main-brain | 8051→8050 | External API entry point (`/chat`, `/chat/async`); 30s TTL health-check cache; Phase 1.45 community memory retrieval; service orchestration; Redis-backed async job management; RAG queueing to ChromaDB backed by PostgreSQL GBIM |

The `jarvis-main-brain` container hosts the `Ms. Jarvis ULTIMATE` main-brain FastAPI application. It exposes `/health`, `/chat`, `/chat/async`, `/chat/status/{job_id}`, `/chat/cancel/{job_id}`, and `/chat/cancel/all` endpoints. Health checks use a 30s TTL cache with 2s per-service timeout and URL overrides (ChromaDB: `/api/v1/heartbeat`; Ollama: `/api/tags`). Async job state persists in Redis with 30-minute TTL and survives container restarts. The `_job_tasks` dict maps `job_id` to `asyncio.Task` for true mid-pipeline cancellation. The executive coordination pattern is described in Chapter 17.

### Coordination Services (ULTIMATE Path)

| Container | Port Mapping | Role |
|---|---:|---|
| jarvis-blood-brain-barrier | 8016→8016 | 7-filter content filter with `truth_score` null guard and fail-open on HTTP 500 |
| jarvis-20llm-production | 8008→8008 | 21-active-model LLM ensemble (22 proxies; StarCoder2 returns 0-char on community queries) |
| jarvis-llm22-proxy (semaphore) | 8030→8030 | Semaphore proxy for `jarvis-20llm-production` (max_tokens -1, unlimited output) |
| jarvis-lm-synthesizer | (internal) | LM Synthesizer: calls `jarvis-ollama:11434/api/generate` with `llama3.1:latest` + Ms. Jarvis persona prompt; merged Phase 3.5 + 3.75 single pass |
| jarvis-web-research | 18009→8009 | External knowledge retrieval; web-based context enhancement |

These services implement the intake and early-routing behavior described above. The main-brain calls the BBB (with fail-open on HTTP 500), performs Phase 1.45 community memory retrieval from `autonomous_learner` via `all-minilm:latest` (384-dim), invokes web-research and PostgreSQL-sourced RAG for context, routes through the 21-LLM ensemble via the semaphore proxy, and calls the LM Synthesizer (merged Phase 3.5 + 3.75) for final persona-injected voice delivery.

### Judge Pipeline (ports not exposed to host — accessed via `docker exec` from `jarvis_startup.sh`)

| Container | Internal Port | Role |
|---|---:|---|
| jarvis-judge-truth | 7230 | Deterministic truth judge; evaluates consensus answer only |
| jarvis-judge-consistency | 7231 | Deterministic consistency judge |
| jarvis-judge-alignment | 7232 | Deterministic alignment judge |
| jarvis-judge-ethics | 7233 | Deterministic ethics judge |
| jarvis-judge-pipeline | (internal) | Judge pipeline orchestrator |
| jarvis-69dgm-bridge | 9000 | 69-DGM cascade (23-connector × 3-stage); validates every production response |

These six containers are managed by `~/jarvis_startup.sh` outside compose for historical reasons. The startup script performs health verification with retry logic using `docker exec` Python urllib internally. The judge pipeline was updated March 16, 2026 to evaluate the consensus answer only (not the full `raw_responses` dump), reducing judge pipeline time from ~85–100s to ~60–86s. Port corrections from the erroneous 7239 to the correct 7230/7231/7232/7233 were applied March 16. `jarvis-69dgm-bridge` had its `CHROMA_HOST` fix deployed March 16.

### Memory, Learning, and Optimization Services

| Container | Port Mapping | Role |
|---|---:|---|
| jarvis-autonomous-learner | 18053→8053 | Autonomous learning; 21,181 records (growing ~288/day) |
| jarvis-i-containers | 18115→8015 | Container orchestration; storage of curated knowledge items |
| jarvis-fifth-dgm | 14002→4002 | Darwin–Gödel–style optimization and filtering |
| jarvis-neurobiological-master | 18118→8018 | Higher-level coordination among neurobiological modules |
| jarvis-hippocampus | 8011→8011 | Hippocampal consolidation; GBIM + beliefs + ChromaDB pipeline (added to compose March 17) |

The `jarvis-hippocampus` service (previously missing from compose, added March 17) participates in Phase 4 RAG context building via the `geospatialfeatures` ChromaDB collection and supplies `confidence_decay` multipliers at Phase 5. Verification scripts demonstrate a complete autonomous learning → Fifth DGM → I-Container flow with measurable I-Container growth. The `jarvis-i-containers` port was corrected to 8015 March 13, 2026.

### RAG Domain Services (added to compose March 17)

| Container | Port Mapping | Role |
|---|---:|---|
| jarvis-gis-rag | 8004→8004 | GIS spatial RAG; queries `geospatialfeatures` + PostgreSQL GeoDB (added to compose March 17) |
| jarvis-spiritual-rag | 8005→8005 | Spiritual/cultural RAG; `spiritual_texts` collection (added to compose March 17) |
| jarvis-psychology-services | 8019→8019 | Psychological safety services; Phase 3 pre-assessment |
| psychological-rag-domain | 8006→8006 | Psychological RAG domain; `psychological_rag` 968 records |

These RAG services were previously running outside compose and have been added with correct `image:` references as of March 17, 2026. The `jarvis-gis-rag` service queries the `geospatialfeatures` ChromaDB collection and PostgreSQL `gisdb` (port 5433, PostGIS, 13 GB, 39 tables). The `jarvis-spiritual-rag` service queries `spiritual_texts` (23 records). All RAG services use `all-minilm:latest` (384-dim) for embedding generation. Note: `gis_rag` and `local_resources` databases currently return empty for Mount Hope-specific queries — community resource data not yet loaded; LLMs generating from training data is an open issue (see Section 19.11 known issues).

### LLM Proxy Layer (21 active models, 22 proxies)

| Proxy | Port | Model |
|---|---:|---|
| llm1-proxy | 8201 | TinyLlama (`tinyllama:latest`) |
| llm2-proxy | 8202 | Gemma (`gemma:2b`) |
| llm3-proxy | 8203 | MedLlama2 (`medllama2:latest`) |
| llm4-proxy | 8204 | MiniCPM-V (`minicpm-v:latest`) |
| llm5-proxy | 8205 | LLaVA (`llava:latest`) |
| llm6-proxy | 8206 | SQLCoder (`sqlcoder:latest`) |
| llm7-proxy | 8207 | StarCoder2 (`starcoder2:latest`) — occasionally returns 0-char on community queries |
| llm8-proxy | 8208 | CodeLlama (`codellama:latest`) |
| llm9-proxy | 8209 | DeepSeek Coder (`deepseek-coder:latest`) |
| llm10-proxy | 8210 | Phi3 Mini (`phi3:mini`) |
| llm11-proxy | 8211 | (assigned — verify against `llm_consensus_20_FINAL.py`) |
| llm12-proxy | 8212 | Dolphin-Phi (`dolphin-phi:latest`) |
| llm13-proxy | 8213 | Orca-Mini (`orca-mini:latest`) |
| llm14-proxy | 8214 | Qwen2 (`qwen2:latest`) |
| llm15-proxy | 8215 | Zephyr (`zephyr:latest`) |
| llm16-proxy | 8216 | Starling-LM (`starling-lm:latest`) |
| llm17-proxy | 8217 | Neural-Chat (`neural-chat:latest`) |
| llm18-proxy | 8218 | OpenChat (`openchat:latest`) |
| llm19-proxy | 8219 | Vicuna (`vicuna:latest`) |
| llm20-proxy | 8220 | LLaMA 2 (`llama2:latest`) |
| llm21-proxy | 8221 | Mistral (`mistral:latest`) |
| llm22-proxy | 8222 | LLaMA 3.1 (`llama3:latest`) |

All 22 proxies route through `jarvis-20llm-production` (port 8008) via the semaphore proxy (port 8030). 21 models are reliably active; StarCoder2 (llm7-proxy) is proxied but frequently returns 0-character responses on community-domain queries. Consensus is extracted correctly from the active 21. All inference is CPU-only (`size_vram: 0` on all models); GPU inference (WVU partnership) is pending. The LM Synthesizer calls `jarvis-ollama:11434/api/generate` directly with `llama3.1:latest` — it does not route through `jarvis-roche-llm` (fixed March 18).

### Data Persistence and Semantics

| Container | Port Mapping | Role |
|---|---:|---|
| jarvis-chroma | 8000→8000 | Canonical ChromaDB instance (`chroma_data` volume; 384-dim `all-minilm:latest`) |
| postgresql-msjarvis | 5433→5433 | PostgreSQL 16: GBIM beliefs (5,416,521 entities), normalized beliefs, temporal decay |
| postgresql-gisdb | 5433→5433 | PostgreSQL 16: PostGIS, 13 GB, 39 tables, 993 ZCTA centroids |
| jarvis-local-resources-db | 5435→5435 | Community resources database (added to compose March 17) |
| jarvis-redis | 6379→6379 | Redis: async job state (30-min TTL), idempotency TTL (1,800s), health cache |
| jarvis-ollama | 11434→11434 | Ollama LLM backend: `all-minilm:latest` (384-dim embeddings), `llama3.1:latest` (LM Synthesizer), all 22 model proxies |

> **Canonical ChromaDB collections (March 18, 2026 — all 384-dim via `all-minilm:latest`):**
>
> | Collection | Records | Notes |
> |---|---:|---|
> | `autonomous_learner` | 21,181 | Growing ~288/day; Phase 1.45 active retrieval on every `/chat` |
> | `gbim_worldview_entities` | 5,416,521 | Complete WV GBIM spatial corpus |
> | `psychological_rag` | 968 | Psychological domain RAG |
> | `spiritual_texts` | 23 | Spiritual/cultural domain RAG |
> | `appalachian_cultural_intelligence` | 5 | Appalachian cultural intelligence |
> | `GBIM_sample_rows` | 5,000 | GBIM sample rows |
> | `GBIM_sample` | 3 | GBIM sample |
> | `msjarvis-smoke` | 1 | Smoke test record |
> | `msjarvis_docs` | 0 | Scaffolded — pending ingest |
> | `GBIM_Fayette_sample` | 0 | Scaffolded — pending ingest |
> | `geospatialfeatures` | 0 | Scaffolded — pending backfill ingest |
>
> **Critical:** `nomic-embed-text` produces 768-dim vectors and is **incompatible** with all existing collections. Only `all-minilm:latest` (384-dim) may be used for ChromaDB embedding generation.

The `services-chroma-1`, `msjarvis-rebuild-chroma-1`, `services-neo4j-1`, and `services-mysql-1` containers are not part of the current production stack. PostgreSQL `msjarvis` (port 5433) and `gisdb` (port 5433) have superseded Neo4j and MySQL as the canonical structured data stores.

### Service Registry, Dynamic Ports, and Discovery

In addition to static ports defined in `docker-compose.yml`, the system uses a service registry and Redis-based dynamic port allocation for some components. Scripts such as `verifyallclaims.sh` check:

- Existence and contents of `serviceregistry.json`, which lists services with names and ports.
- Redis keys of the form `service:<name>` that map to dynamically assigned ports.
- Health of registered services by iterating over the registry and issuing `GET /health` checks (results cached for 30s; per-service timeout 2s).

This registry layer supports the container architecture by allowing certain services to join and leave dynamically while remaining discoverable by orchestrators and container logic. Similar concerns about monitoring, liveness, and controllers appear in cloud-native design discussions by Brewer and in controller patterns documented by Burns et al.

### Verified Reboot Sequence (March 17, 2026)

After any system reboot or `docker compose` restart, the full 79-container production stack is brought online with two commands:

```bash
# Step 1: Start all 79 compose-managed containers
cd ~/msjarvis-rebuild-working/msjarvis-rebuild && docker compose up -d

# Step 2: Start and verify the six pipeline containers + health checks
~/jarvis_startup.sh
```

**Go signal:** Six green health check marks from `jarvis_startup.sh`:
- `jarvis-judge-truth`
- `jarvis-judge-consistency`
- `jarvis-judge-alignment`
- `jarvis-judge-ethics`
- `jarvis-judge-pipeline`
- `jarvis-69dgm-bridge`

The startup script manages the six judge/gateway containers that run outside compose for historical reasons. It performs health verification with retry logic using `docker exec` Python urllib internally (these containers do not expose ports to the host). No manual `docker run` commands are required for any other container. The `~/jarvis_startup.sh` file was created March 17, 2026 and includes IPv4 binding fixes.

### External Access Points and LLM Backend

Only a small subset of ports are exposed to the host:

- **8051** — External API endpoint (mapped to `jarvis-main-brain` on 8050; `/chat`, `/chat/async`, `/chat/status`, `/chat/cancel`)
- **11434** — Ollama LLM backend (`jarvis-ollama`; `all-minilm:latest` embeddings + all 22 model proxies + `llama3.1:latest` for LM Synthesizer)
- **5433** — PostgreSQL `msjarvis` and `gisdb` (GBIM and GeoDB source of truth)
- **5435** — PostgreSQL `jarvis-local-resources-db` (community resources)
- **6379** — Redis (`jarvis-redis`; async job state, idempotency, health cache)

All other services communicate over the `qualia-net` Docker bridge network using container names and internal ports for discovery.

---

## 19.9 Async Job Management API

The `/chat` endpoint is synchronous and takes ~436 seconds for a full pipeline run. The async job API (deployed March 17, 2026) allows immediate response with polling:

| Endpoint | Method | Function |
|---|---|---|
| `/chat/async` | POST | Create async job — returns `job_id` immediately |
| `/chat/status/{job_id}` | GET | Poll for progress and result |
| `/chat/cancel/{job_id}` | DELETE | Cancel a specific running job |
| `/chat/cancel/all` | DELETE | Cancel all running jobs |

**Implementation details:**
- Job state persists in Redis (`jarvis-redis:6379`) with 30-minute TTL
- State survives `jarvis-main-brain` container restarts
- Cancel operations perform true `asyncio` task cancellation — the 21-LLM pipeline stops immediately mid-run
- The `_job_tasks` dict maps `job_id` to `asyncio.Task` for true interruption
- Idempotency TTL: Redis-backed, 1,800s (previously in-memory only — fixed March 17)

---

## 19.10 Observed Routing Behavior in Verification Scripts

Several shell scripts provide concrete evidence of how the container architecture behaves in practice:

- **VERIFYANDTEST.sh**
  Checks RAG, web UI, and selected services, confirming that containerized components are reachable, that PostgreSQL `msjarvisgis` is accessible at port 5432, and that semantic memory is populated.

- **verifyallclaims.sh**
  Exercises a complete autonomous learning and I-Container flow, testing:
  - Current I-Container size and growth capacity.
  - Service registry and dynamic port integration via Redis.
  - Health of key services (Fifth DGM, WOAH, I-Containers, Consciousness Bridge, Autonomous Learner, Web Research, LLM Bridge, Qualia Engine, Swarm Intelligence).
  - PostgreSQL `msjarvisgis` connection health and GBIM belief counts.
  - I-Container analysis tools that report size, status, keywords, and suggested topics.

- **VERIFY CHROMADB sections**
  Confirm that ChromaDB directories exist, that collections can be queried, that embedding counts match expectations, that all collections use 384-dim vectors (`all-minilm:latest`), and that PostgreSQL-sourced GBIM collections are properly synchronized, tying container records back to semantic memory and PostgreSQL ground truth.

These scripts demonstrate that the container architecture is not merely conceptual: it is instrumented and testable, with observable behaviors that align with the intake–normalization–routing pattern described in this chapter and anchored in PostgreSQL `msjarvisgis`. They also mirror best practices for health checks and monitoring in distributed systems as discussed by Brewer and Burns et al.

---

## 19.11 Known Issues and Resolution Status (March 18, 2026)

| Issue | Status |
|---|---|
| Response truncation (~730 chars, `max_tokens: 500`) | ✅ FIXED — `max_tokens` set to -1 (unlimited); `llm22-proxy` 8,192-token limit confirmed |
| ChromaDB `_DummyCollection` blocking semantic retrieval | ✅ FIXED — `all-minilm:latest` (384-dim) semantic retrieval implemented March 17 |
| Redis response persistence (in-memory only) | ✅ FIXED — full Redis-backed job system with 30-min TTL deployed March 17 |
| 33 services not in `docker-compose.yml` | ✅ FIXED — all 79 containers now in compose (March 17) |
| Idempotency TTL in-memory only | ✅ FIXED — Redis-backed, 1,800s TTL |
| Judge pipeline URL wrong (port 7239 for all judges) | ✅ FIXED — corrected to 7230/7231/7232/7233 (March 16) |
| LM Synthesizer calling `jarvis-roche-llm` (HTTP 500) | ✅ FIXED — now calls `jarvis-ollama:11434/api/generate` directly (March 18) |
| NBB Prefrontal Cortex 422 errors | ✅ RESOLVED — `message` field payload confirmed correct; service healthy |
| I-Containers 422 errors | ✅ RESOLVED — port corrected to 8015 (March 13) |
| BBB `truth_score` `KeyError` crash | ✅ FIXED — null guard added to BBB orchestrator (March 18) |
| BBB blocking entire pipeline on HTTP 500 | ✅ FIXED — fail-open behavior on non-200 BBB responses, both input and output guard (March 18) |
| `web-research` and `rag-server` restart loops | ✅ FIXED — source files deployed via `docker cp` |
| Hash-prefixed container names (e.g., `981f44e18cf6_jarvis-20llm-production`) | ✅ FIXED — `container_name:` added to all 8 affected containers (March 17–18) |
| `hilbert-gateway` port conflict in `docker-compose.yml` | ✅ FIXED — resolved during March 17 compose audit |
| `build:` directives causing slow/unpredictable startup | ✅ FIXED — all `build:` entries converted to `image:` references (March 17) |
| Docker Compose v1.29.2 `ContainerConfig` crash bug | ✅ FIXED — upgraded to Docker Compose v5.1.0 (March 17) |
| 9 containers missing from compose | ✅ FIXED — 3 corpus + 6 service containers added (March 17) |
| Hallucination on local community resources (Mount Hope, Fayette County) | 🔴 OPEN — `gis_rag` and `local_resources` databases return empty for Mount Hope queries; LLMs generating from training data. Factually accurate programs (LIHEAP, WV 2-1-1) pass BBB. Fabricated organization names blocked by ethical filter. Root cause: real community resource data not yet loaded. Resolution: Community Champions data entry next priority. |
| BBB ethical filter blocking "certainly" | BY DESIGN — ethical filter correctly detecting unverified specific claims; not a false positive |
| StarCoder2 returning 0-char responses on community queries | KNOWN — 21 of 22 models active; consensus extracted correctly; StarCoder2 proxied but unreliable on non-code queries |

---

## 19.12 Summary

The container architecture and routing layer described here provide the structural glue between external interfaces, executive coordination, autonomous learning, and PostgreSQL long-term memory. As of March 18, 2026, this architecture is fully operationalized in a 79-container production stack, entirely managed by Docker Compose v5.1.0 (`image:` references only, no rebuilds), with a verified two-command reboot sequence and Redis-backed async job management. Through a combination of Dockerized services, service registry mechanisms, 30s TTL health-check caching, Phase 1.45 community memory retrieval via `all-minilm:latest` (384-dim), and structured normalization of events into container records, the system can:

- Receive and categorize diverse inputs from users (synchronous and async), internal processes, and external signals.
- Apply safety filters (BBB 7-filter stack with `truth_score` null guard and fail-open on HTTP 500), eligibility checks against PostgreSQL GBIM truth, and basic policy decisions at the intake stage.
- Inject top-5 semantically relevant community memories (from `autonomous_learner`, 21,181 records) into every LLM prompt at Phase 1.45.
- Route normalized records into parallel paths for affective and analytical evaluation.
- Feed curated content into PostgreSQL long-term stores such as the I-Container, ChromaDB (`chroma_data` volume, all collections 384-dim), GBIM graphs in PostgreSQL `msjarvisgis` (port 5432, 91 GB, 501 tables, 5.4M+ verified beliefs), and Redis-backed job state.

By grounding the abstract design in the March 18, 2026 production topology, this chapter demonstrates that the container architecture is both fully implemented and empirically observable, with all memory and routing flows ultimately anchored to PostgreSQL `msjarvisgis` at port 5432. Subsequent chapters will build on this foundation to describe how filtered and routed items are further evaluated, consolidated, and woven into longer-term cognitive and memory structures in PostgreSQL.

*Last updated: 2026-03-18 by Carrie Kidd, Mount Hope WV*
