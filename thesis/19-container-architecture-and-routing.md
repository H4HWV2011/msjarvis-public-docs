# Chapter 19 — Container Architecture and Routing

> **Correction applied March 22, 2026:**
> **Ghost file fix — FULLY FIXED March 22, 2026.** The March 21, 2026 remediation restored all real judge scripts to `services/` and rebuilt images with `--no-cache`. However, one artefact remained: a `COPY lm_synthesizer.py /app/` line in `services/Dockerfile.judge` that silently copied the synthesizer file into every judge image layer. This line was removed from `Dockerfile.judge` on March 22, 2026, and a final `--no-cache` rebuild was completed and verified across all 5 judge images. The fix is now fully complete. See §19.14 and §19.11.

---

# Why This Matters for Polymathmatic Geography

This chapter explains how Ms. Jarvis's containers receive, sort, and route the flows of experience that later become memory and decision support. It supports:

- **P1 – Every where is entangled** by treating events from people, places, and institutions as a shared stream that must be carefully routed into PostgreSQL `msjarvis`/`gis` (port 5432, 91 GB, 501 tables, 5,416,522 verified GBIM beliefs including 20,593 landowner beliefs) and ChromaDB memory.

- **P3 – Power has a geometry** by making explicit which services, ports, and stores stand between communities' data and long-term inference in PostgreSQL, and by naming `gbimqueryrouter` (port 7205) as the service that makes corporate and government land ownership queryable by natural language for the first time.

- **P5 – Design is a geographic act** by encoding how Appalachian events move through Ms. Jarvis and into PostgreSQL spatial, semantic, and commons-oriented stores, and by treating the routing decision to bypass ChromaDB entirely for landowner queries as an explicit architectural choice with geographic and ethical consequences.

- **P12 – Intelligence with a ZIP code** by prioritizing spatial, governance, and commons contexts from PostgreSQL GeoDB in the way container records are tagged and stored, and by recognizing `gbimqueryrouter` as the service that closes the *who* axis at parcel scale.

- **P16 – Power accountable to place** by using auditable container flows and verification scripts so communities can see where their data goes in PostgreSQL `msjarvis`/`gis` and ChromaDB, and by ensuring that corporate and government landholdings are queryable with full assessor provenance through `gbimqueryrouter`.

As such, this chapter belongs to the **Computational Instrument** tier: it describes the container and routing structures that turn raw events into traceable, place-aware memory anchored in PostgreSQL.

```
┌─────────────────────────────────────────────────────────────────┐
│  Container Architecture and Routing Flow                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Incoming Events                                                 │
│  - User queries (chat, chat_async)                               │
│  - Internal tasks (autonomous learner, Fifth DGM)                │
│  - External signals                                              │
│  - Structural changes (GBIM updates)                             │
│      ↓                                                           │
│  Normalization Layer                                             │
│  - Core fields: ID, timestamps, origin                           │
│  - Context: role, geography, tags                                │
│  - Content summary                                               │
│  - Links: PostgreSQL GBIM, ChromaDB, GIS                         │
│  - Control flags: safety, urgency, sensitivity                   │
│      ↓                                                           │
│  First-Level Routing                                             │
│  - Eligibility checks: BBB 7-filter (fail-open)                  │
│  - Phase 1.45: community memory retrieval (all-minilm)           │
│  - Priority assignment                                           │
│  - Track assignment                                              │
│      ↓                        ↓                    ↓            │
│  Affective/Care Path   Analytical/Tech Path   landowner-gbim     │
│  - Psychological RAG   - GIS/Spatial          gbimqueryrouter    │
│  - Community support   - Infrastructure       SQL direct →       │
│  - Ethical interpret   - Landowner GBIM       PostgreSQL only    │
│      ↓                        ↓                                  │
│  Container Records                                               │
│  - Marked for evaluation                                         │
│  - Held back or dropped                                          │
│  - Introspective logs                                            │
│      ↓                                                           │
│  Long-Term Storage                                               │
│  - PostgreSQL msjarvis/gis (port 5432)                           │
│    GBIM beliefs: 5,416,522 verified, incl. 20,593 landowner      │
│    LANDOWNER_CORPORATE / LANDOWNER_GOVERNMENT (as of Mar 20)     │
│    GeoDB spatial: 501 tables, 91 GB                              │
│    mvw_gbim_landowner_spatial: materialized, live                │
│  - ChromaDB (port 8000, chroma_data volume)                      │
│    Semantic collections: 384-dim, all-minilm-latest              │
│    Landowner beliefs NOT in ChromaDB (see below)                 │
│  - I-Containers (port 8015)                                      │
│  - Redis job state (jarvis-redis:6379, 30-min TTL)               │
│  - Audit logs                                                    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

> **Figure 19.1.** Container architecture and routing flow. As of March 21, 2026, all 80 containers are fully compose-managed via Docker Compose v5.1.0 at `msjarvis-rebuild-working/msjarvis-rebuild/docker-compose.yml`. `gbimqueryrouter` (port 7205) is the 80th container, added March 20, 2026, serving the GBIM landowner belief layer via a PostgreSQL-native path that bypasses ChromaDB entirely. **Ghost file fix fully completed March 22, 2026** — `COPY lm_synthesizer.py /app/` line removed from `services/Dockerfile.judge`; `--no-cache` rebuild confirmed across all 5 judge images.

---

## Status as of March 22, 2026

| Category | Details |
|---|---|
| **Implemented and verified** | All 80 production containers fully compose-managed via Docker Compose v5.1.0. `gbimqueryrouter` port 7205 live since March 20, 2026. All build directives converted to image references for non-judge services (no rebuilds on startup). Judge service source files confirmed real (not `lm_synthesizer.py` clones) March 21, 2026. **Ghost file fix FULLY COMPLETE March 22, 2026:** real scripts restored March 21; stray `COPY lm_synthesizer.py /app/` line removed from `services/Dockerfile.judge` March 22; `--no-cache` rebuild completed and verified across all 5 judge images March 22. Sub-judge default ports corrected from all-7239 to 7230/7231/7232/7233 in `judge_pipeline.py` lines 16–19. `bbb_check_verdict` live async httpx POST confirmed March 21. 5,416,522 GBIM beliefs including 20,593 landowner beliefs in `gbim_belief_normalized`. `mvw_gbim_landowner_spatial` materialized and spatially indexed. Autonomous learner: 21,181 records, growing 288/day. End-to-end benchmark: 436s (optimized from 532s baseline). |
| **Partially implemented / scaffolded** | `geospatial_features`, `msjarvis-docs`, `GBIMFayette_sample` ChromaDB collections scaffolded — pending ingest. Community resource data for Mount Hope/Fayette County not yet loaded (hallucination on local resource queries is the current open gap — see §19.11). `judgesigner.py` post-quantum signing scaffolded — see Chapter 42 §42.10. |
| **Future work / design intent only** | `rag_grounded_v2` truth verification for BBB `heuristic_contradiction_v1` upgrade path. GPU inference (WVU partnership pending). Full public documentation of BBB filter logic. Dedicated ChromaDB quarantine collections for blocked content. Deeper PIA review loop automation. |

> **Cross-reference note:** The judge pipeline BBB integration is documented in Chapter 16 §16.11 and Chapter 33 §33.2. Build context integrity (§19.14) is the prerequisite for all judge image rebuilds. Post-quantum signing of judge verdicts is documented in Chapter 42 §42.10. Ghost file fix completeness is also documented in Chapter 42 §42.10.

---

# 19. Container Architecture and Routing

This chapter describes the high-level layout of the container-based structures that receive activity from earlier layers and route it into deeper evaluation paths anchored in PostgreSQL `msjarvis`/`gis` (port 5432, 91 GB, 501 tables, 5,416,522 verified GBIM beliefs including 20,593 landowner beliefs as of March 20, 2026). The goal is to separate the flow of events into clear stages, so that each stage has a well-defined role in deciding what is ignored, what is kept for background consideration, and what becomes part of PostgreSQL or ChromaDB central stores. In the implemented system, these responsibilities are realized by a set of Dockerized services that cooperate via HTTP and shared data stores. As of March 21, 2026, all 80 production containers are defined in a single `docker-compose.yml` and managed via Docker Compose v5.1.0 — no manual service startup is required beyond `jarvis_startup.sh` for the six judge/gateway pipeline containers. The 80th container, `gbimqueryrouter` (port 7205), was promoted to production on March 20, 2026, and is the first Ms. Jarvis service whose retrieval path is entirely relational — no ChromaDB, no vector similarity, no embedding pipeline.

**March 21–22, 2026 addendum:** A structural vulnerability was discovered and remediated across two sessions. On March 21, inspection of the running judge containers revealed that all four sub-judge source files in `services/` — the Docker build context for all judge images — had been silently replaced with `lm_synthesizer.py` clones bearing incorrect names. Real judge scripts were restored and images were rebuilt `--no-cache` on March 21. On March 22, a residual artefact was identified and removed: a `COPY lm_synthesizer.py /app/` line that had remained in `services/Dockerfile.judge` after the March 21 restore. This line was removed and a final `--no-cache` rebuild was completed and verified across all 5 judge images on March 22, 2026. The fix is now fully complete. This incident motivates the §19.14 Build Context Integrity subsection, which documents mandatory verification procedures for the `services/` canonical directory.

---

## 19.1 Position in the Overall System

In practice, the intake layer receives several broad categories of events that must be handled in a unified way:

- **Direct interactions** — User queries and responses that have already passed through initial retrieval from PostgreSQL-sourced RAG and constraint checks via the `jarvis-main-brain` chat pipeline. These include synchronous requests and asynchronous jobs that are tracked via job IDs and status records persisted in Redis (`jarvis-redis:6379`, 30-minute TTL). The `chat_async` endpoint returns a `job_id` immediately; polling via `chat_status/{job_id}` retrieves progress and result. True asyncio task cancellation via `chat_cancel/{job_id}` stops the 21-LLM pipeline mid-run.

- **Internal tasks** — Results from scheduled analyses, background maintenance jobs, and optimization routines. Examples include outputs from the autonomous learner (21,181 records as of March 20, 2026, growing 288/day), Fifth DGM optimization steps, and WOAH evaluations, which generate candidate content for the I-Container and other long-term structures.

- **External signals** — Notifications or status changes from connected systems such as messaging platforms, web front ends, or external data sources. These may arrive via dedicated services or be polled and converted into internal events.

- **Structural changes** — Updates to PostgreSQL `msjarvis`/`gis` memory, GBIM belief graphs, or spatial layers that may require special attention. The March 20, 2026 ingestion of 20,593 landowner belief records and the promotion of `gbimqueryrouter` to production are examples of structural change events that trigger container-level processing and validation and that update the GBIM corpus stats propagated to downstream services.

Each event is accompanied by metadata such as timestamps, role identifiers, user or agent IDs, and source information. Container logic uses this metadata to make routing decisions, enforce policy, and maintain traceability back to PostgreSQL sources.

---

## 19.2 Types of Incoming Events

*(See §19.1 above for the full enumeration of event categories.)*

---

## 19.3 Normalization into Container Records

Before events are passed to deeper stages, they are normalized into container records with a common structure. This normalization is implemented in several places:

- In the Ms. Jarvis ULTIMATE main-brain, where incoming `chat` and `chat_async` requests are converted into structured request models and then into RAG storage records in ChromaDB backed by PostgreSQL GBIM queries.
- In the autonomous learning and Fifth DGM flows, where internal discoveries are wrapped into I-Container entries.

A typical normalized record includes:

- **Core fields** — A unique identifier, creation and update timestamps, origin (e.g., `user_chat`, `autonomous_learner`, `gbim_landowner_update`, or `external_signal`), and a reference to the initiating service or job.

- **Context** — Active role or profile, relevant geographic or institutional context from PostgreSQL GeoDB, and tags describing the domain (e.g., `governance`, `infrastructure`, `landowner`, or `community_culture`). For chat records, this includes the `user_id` and any declared `mode` (e.g., `landowner_gbim` for ownership queries routed to `gbimqueryrouter`, or `ultimate` for the full LLM ensemble path). For async jobs, the Redis-persisted `job_id` links the normalized record to its lifecycle state.

- **Content summary** — Key text, numerical values, or structured data extracted from the event. For chat interactions, this is typically a truncated version of the query and response plus any derived summaries. For internal tasks, it may include candidate knowledge statements, metrics, or optimization results. For landowner queries, it includes the routing decision (`mode: landowner_gbim`, `route_type: parcel_ownership`) and the SQL aggregation result from `mvw_gbim_landowner_spatial`.

- **Links** — References to memory items (ChromaDB embeddings, all 384-dim via `all-minilm-latest`; PostgreSQL GBIM graph nodes/edges at port 5432; relational records; spatial features; PostgreSQL GeoDB entities; and introspective entries such as job logs and verification reports). For landowner queries, links point directly to `mvw_gbim_landowner_spatial` rows in `msjarvis/gis` — not to ChromaDB, which does not hold landowner beliefs.

- **Control information** — Flags indicating initial assessments such as urgency, sensitivity, safety status (e.g., BBB-approved or denied, with fail-open on HTTP 500), expected resource cost, and whether the item is considered high-value for long-term retention in PostgreSQL `msjarvis`/`gis`.

---

## 19.4 First-Level Routing Decisions

Once a record is normalized, the intake layer applies initial routing logic. In the running system, this logic appears in:

- The main-brain's decision to send a request through the BBB 7-filter stack (with `truth_score` null guard and fail-open on HTTP 500), Phase 1.45 community memory retrieval (`autonomous_learner` via `all-minilm-latest` 384-dim semantic search, top-5 records prepended), PostgreSQL-sourced RAG, web research, and LLM ensembles, and then to queue RAG storage with specific metadata.

- The `gbimqueryrouter` routing decision: when `mode=landowner_gbim` is detected, the request bypasses ChromaDB, the LLM ensemble, and web research, and routes directly to `mvw_gbim_landowner_spatial` via SQL aggregation. This is a **complete routing bypass** — the shortest and most deterministic path in the system.

- The autonomous learner and Fifth DGM scripts that decide when to push new candidate items into the I-Container and when to leave them as transient results.

The first-level routing includes:

- **Eligibility checks** — Confirming that the record is allowed to enter container paths under current global settings. This includes safety checks (BBB 7-filter stack against PostgreSQL GBIM ground truth, with fail-open if BBB returns HTTP 500 — the pipeline continues rather than blocking), role-based constraints, and checks for service availability via health probes (30s TTL cache, 2s timeout per service; URL overrides for ChromaDB `api/v1/heartbeat` and Ollama `api/tags`).

- **Phase 1.45 community memory injection** — After BBB input approval, the main brain generates a 384-dim embedding via `all-minilm-latest` at `jarvis-ollama:11434/api/embeddings`, queries the `autonomous_learner` ChromaDB collection (21,181 records), retrieves the 5 most semantically similar community interaction records, and prepends them to `enhanced_message` before it reaches the 21 LLMs. This step applies to all standard chat paths. It does not apply to `gbimqueryrouter` landowner paths, which resolve entirely within PostgreSQL.

- **Priority assignment** — Assigning a simple priority or track indicator that influences ordering and resource allocation.

- **Track assignment** — Deciding whether the record should be sent to specific container subsystems such as the I-Container, psychological RAG domains, PostgreSQL GBIM graph updates, `gbimqueryrouter` landowner path, or audit logs.

---

## 19.5 Parallel Paths

The architecture supports multiple parallel paths that share a common structural pattern: intake → normalization → gating → storage in PostgreSQL or ChromaDB or discard. Conceptually, two broad tracks can be distinguished:

- **Affective and care-oriented paths** — Used when events are framed in terms of meaning, care, or psychological support. These involve specialized RAG domains, therapeutic or community-oriented analysis, and services that emphasize ethical interpretation and human impact.

- **Analytical and technical paths** — Used for more conventional problem-solving tasks, such as infrastructure planning using PostgreSQL GeoDB, spatial reasoning, optimization over data, and structured ownership queries via `gbimqueryrouter`. These paths emphasize quantitative reasoning, model-based analysis, and technical verification against PostgreSQL GBIM ground truth.

The `gbimqueryrouter` landowner path is a third, structurally distinct track: deterministic relational retrieval. It does not involve LLM reasoning, ChromaDB vector search, or web research. It is the system's only fully deterministic query path — an exact SQL aggregation over verified GBIM belief records with full assessor provenance.

---

## 19.6 Outputs of the Routing Layer

After routing, the container layer produces several types of outputs that feed later stages and support evaluation:

- **Records marked for immediate evaluation** — Items that pass eligibility checks and have sufficient priority are forwarded to downstream evaluators (e.g., 21-model LLM consensus, truth validators against PostgreSQL GBIM, or `gbimqueryrouter` SQL aggregation). Their container records carry all necessary context and links to PostgreSQL tables.

- **Records held back or dropped** — Events may be held back (queued, delayed, or rate-limited) or dropped entirely based on policy.

- **Introspective logs and verification entries** — The system records which paths were chosen, which services were invoked, what PostgreSQL queries were executed, and what the outcomes were. `gbimqueryrouter` results are logged with their full SQL provenance (canonical entity name, parcel count, total area, county scope) so that every landowner answer can be traced to specific rows in `gbim_belief_normalized`.

---

## 19.7 Conceptual Summary

Conceptually, the container architecture provides a structured way to receive, normalize, and direct events into deeper evaluative paths anchored in PostgreSQL `msjarvis`/`gis` (port 5432, 91 GB, 501 tables, 5,416,522 verified GBIM beliefs as of March 20, 2026). It defines how diverse inputs — user interactions, internal learning results, external signals, and structural changes — enter the system's evaluative core. By enforcing clear stages and control flags, it supports disciplined decision-making about what is ignored, what is kept for background consideration, and what is integrated into PostgreSQL central memory and GBIM belief structures.

The remaining sections of this chapter ground this abstraction in the current production deployment topology, focusing on Docker containers, port mappings, compose management, and service roles as of March 22, 2026.

---

## 19.8 Operational Container Topology (March 22, 2026)

> **This section is the authoritative operational state as of March 22, 2026**, superseding the March 21, 2026 snapshot. The topology is derived from `msjarvis-rebuild-working/msjarvis-rebuild/docker-compose.yml` (Docker Compose v5.1.0), runtime `docker ps` output, `jarvis_startup.sh`, and verification scripts.

**Compose management baseline — March 22, 2026:**
All 80 production containers are defined in a single `docker-compose.yml`. `gbimqueryrouter` (port 7205) was added to compose on March 20, 2026, as the 80th container. All build directives remain converted to image references for non-judge services — no image rebuilds occur on startup for those containers. Judge service images were rebuilt with `--no-cache` on March 21, 2026 (real scripts restored after ghost file detection), and rebuilt again with `--no-cache` on March 22, 2026 (stray `COPY lm_synthesizer.py /app/` line removed from `services/Dockerfile.judge` — ghost file fix now **fully complete**). See §19.14. Reboot sequence is unchanged: `docker compose up -d` followed by `jarvis_startup.sh`.

### Core Orchestration Layer

| Container | Port Mapping | Role |
|---|---|---|
| `jarvis-main-brain` | 8051→8050 | External API entry point (`chat`, `chat_async`); 30s TTL health-check cache; Phase 1.45 community memory retrieval; service orchestration; Redis-backed async job management; RAG queueing to ChromaDB backed by PostgreSQL GBIM; routes `mode=landowner_gbim` queries to `gbimqueryrouter` |

The `jarvis-main-brain` container hosts the Ms. Jarvis ULTIMATE main-brain FastAPI application. It exposes `/health`, `/chat`, `/chat_async`, `/chat_status/{job_id}`, `/chat_cancel/{job_id}`, and `/chat_cancel_all` endpoints. Health checks use a 30s TTL cache with 2s per-service timeout and URL overrides (`ChromaDB: api/v1/heartbeat`; `Ollama: api/tags`). Async job state persists in Redis with 30-minute TTL and survives container restarts.

### Safety and Filtering Layer

| Container | Port Mapping | Role |
|---|---|---|
| `jarvis-blood-brain-barrier` | 8016→8016 | 6-filter content filter (ethical, spiritual, safety, threat_detection, steganography, truth_verification) with `truth_score` null guard and fail-open on HTTP 500; `barrier_stats` live; `bbb_check_verdict` wired from judge pipeline March 21, 2026; **steganography aggregation bug fixed March 22, 2026** (see Chapter 16 §16.14) |
| `jarvis-20llm-production` | 8008→8008 | 21-active-model LLM ensemble; 22 proxies; StarCoder2 returns 0-char on community queries |
| `jarvis-llm22-proxy` (semaphore) | 8030→8030 | Semaphore proxy for `jarvis-20llm-production`; `max_tokens: -1`, unlimited output |
| `jarvis-lm-synthesizer` | 8001 internal | LM Synthesizer; calls `jarvis-ollama:11434/api/generate` with `llama3.1:latest`; Ms. Jarvis persona prompt merged; Phase 3.5/3.75 single pass |
| `jarvis-web-research` | 18009→9009 | External knowledge retrieval; web-based context enhancement; excluded for `landowner_gbim` mode |

### Coordination Services — ULTIMATE Path

| Container | Internal Port | Source File | Role |
|---|---|---|---|
| `jarvis-judge-pipeline` | 7239 | `services/judge_pipeline.py` | Coordinator: `POST /evaluate`, `asyncio.gather`, aggregation, `bbb_check_verdict` live httpx POST |
| `jarvis-judge-truth` | 7230 | `services/judge_truth_filter.py` | Truth evaluation: `heuristic_contradiction_v1` |
| `jarvis-judge-consistency` | 7231 | `services/judge_consistency_engine.py` | Internal coherence, contradiction detection |
| `jarvis-judge-alignment` | 7232 | `services/judge_alignment_filter.py` | Ms. Jarvis identity adherence, community values |
| `jarvis-judge-ethics` | 7233 | `services/judge_ethics_filter.py` | Harm screening, spiritual appropriateness |
| `jarvis-69dgm-bridge` | 9000 | — | 69-DGM cascade; 23-connector; 3-stage; validates every production response |

All five judge service containers are compose-managed with `restart: unless-stopped`. Source files confirmed as real judge scripts (not `lm_synthesizer.py` clones) on March 21, 2026. **Ghost file fix fully complete March 22, 2026:** stray `COPY lm_synthesizer.py /app/` line removed from `services/Dockerfile.judge`; `--no-cache` rebuild completed and verified across all 5 judge images. Sub-judge default ports corrected from all-7239 to 7230/7231/7232/7233 in `judge_pipeline.py` lines 16–19. See §19.14 for build context integrity requirements.

### Memory, Learning, and Optimization Services

| Container | Port Mapping | Role |
|---|---|---|
| `jarvis-autonomous-learner` | 18053→8053 | Autonomous learning; 21,181 records, growing 288/day from March 14 baseline |
| `jarvis-i-containers` | 18115→8015 | Container orchestration; storage of curated knowledge items |
| `jarvis-fifth-dgm` | 14002→4002 | Darwin–Gödel-style optimization and filtering |
| `jarvis-neurobiological-master` | 18118→8018 | Higher-level coordination among neurobiological modules |
| `jarvis-hippocampus` | 8011→8011 | Hippocampal consolidation; GBIM beliefs → ChromaDB pipeline; added to compose March 17 |

### RAG Domain Services

| Container | Port Mapping | Role |
|---|---|---|
| `jarvis-gis-rag` | 8004→8004 | GIS spatial RAG queries; `geospatial_features`; PostgreSQL GeoDB; added to compose March 17 |
| `jarvis-spiritual-rag` | 8005→8005 | Spiritual/cultural RAG; `spiritual_texts` collection; added to compose March 17 |
| `jarvis-psychology-services` | 8019→8019 | Psychological safety services; Phase 3 pre-assessment |
| `psychological-rag-domain` | 8006→8006 | Psychological RAG domain; `psychological_rag` 968 records |
| **`gbimqueryrouter`** | **7205→7205** | **NEW — March 20, 2026.** GBIM landowner belief query router. PostgreSQL-native path only. Queries `mvw_gbim_landowner_spatial` in `msjarvis/gis` (port 5432) via SQL aggregation. `proposition_codes`: `LANDOWNER_CORPORATE`, `LANDOWNER_GOVERNMENT`. `worldview = eq1`. 20,593 verified landowner beliefs. **NO ChromaDB — bypassed entirely.** `mode=landowner_gbim`, `route_type=parcel_ownership`. |

> **`gbimqueryrouter` architectural note:** This is the only RAG-class service in the Ms. Jarvis stack that does not use ChromaDB. Every other RAG service passes through the shared ChromaDB instance (port 8000) for 384-dim `all-minilm-latest` vector similarity search. `gbimqueryrouter` routes directly to `mvw_gbim_landowner_spatial` via SQL aggregation — a deliberate architectural decision reflecting that corporate and government landowner queries have exact, deterministic answers in the relational GBIM corpus. Approximate vector nearest-neighbor search would introduce unnecessary error. The relational path is faster, more accurate, and fully auditable to specific `gbim_belief_normalized` rows with nine-axis provenance.

Verified query patterns (both confirmed March 20, 2026):

```python
import httpx

# Pattern 1: Statewide top landowners
statewide = httpx.post("http://127.0.0.1:7205/query", json={
    "question": "Who are the largest landowners in West Virginia?",
    "mode": "landowner_gbim",
    "route_type": "parcel_ownership",
    "scope": "statewide",
    "limit": 20
})

# Pattern 2: County-scoped landowners
county = httpx.post("http://127.0.0.1:7205/query", json={
    "question": "Who owns the most land in Fayette County?",
    "mode": "landowner_gbim",
    "route_type": "parcel_ownership",
    "county": "Fayette",
    "limit": 20
})
```

### LLM Proxy Layer (21 active models, 22 proxies)

| Proxy | Port | Model |
|---|---|---|
| `llm1-proxy` | 8201 | TinyLlama `tinyllama:latest` |
| `llm2-proxy` | 8202 | Gemma `gemma:2b` |
| `llm3-proxy` | 8203 | MedLlama2 `medllama2:latest` |
| `llm4-proxy` | 8204 | MiniCPM-V `minicpm-v:latest` |
| `llm5-proxy` | 8205 | LLaVA `llava:latest` |
| `llm6-proxy` | 8206 | SQLCoder `sqlcoder:latest` |
| `llm7-proxy` | 8207 | StarCoder2 `starcoder2:latest` — occasionally returns 0-char on community queries |
| `llm8-proxy` | 8208 | CodeLlama `codellama:latest` |
| `llm9-proxy` | 8209 | DeepSeek Coder `deepseek-coder:latest` |
| `llm10-proxy` | 8210 | Phi3 Mini `phi3:mini` |
| `llm11-proxy` | 8211 | assigned — verify against `llm_consensus_20FINAL.py` |
| `llm12-proxy` | 8212 | Dolphin-Phi `dolphin-phi:latest` |
| `llm13-proxy` | 8213 | Orca-Mini `orca-mini:latest` |
| `llm14-proxy` | 8214 | Qwen2 `qwen2:latest` |
| `llm15-proxy` | 8215 | Zephyr `zephyr:latest` |
| `llm16-proxy` | 8216 | Starling-LM `starling-lm:latest` |
| `llm17-proxy` | 8217 | Neural-Chat `neural-chat:latest` |
| `llm18-proxy` | 8218 | OpenChat `openchat:latest` |
| `llm19-proxy` | 8219 | Vicuna `vicuna:latest` |
| `llm20-proxy` | 8220 | LLaMA 2 `llama2:latest` |
| `llm21-proxy` | 8221 | Mistral `mistral:latest` |
| `llm22-proxy` | 8222 | LLaMA 3.1 `llama3:latest` |

All 22 proxies route through `jarvis-20llm-production` (port 8008) via the semaphore proxy (port 8030). 21 models reliably active; StarCoder2 (`llm7-proxy`) proxied but frequently returns 0-character responses on community-domain queries. All inference is CPU-only (`size_vram: 0`); GPU inference (WVU partnership) pending. The LM Synthesizer calls `jarvis-ollama:11434/api/generate` directly with `llama3.1:latest`. Note: `gbimqueryrouter` landowner queries do not pass through the LLM ensemble — they return structured SQL results directly.

### Data Persistence and Semantics

| Container | Port Mapping | Role |
|---|---|---|
| `jarvis-chroma` | 8000→8000 | Canonical ChromaDB instance; `chroma_data` volume; 384-dim `all-minilm-latest`; **landowner beliefs NOT stored here** |
| `postgresql-msjarvis` | 5433→5433 | PostgreSQL 16; GBIM beliefs (5,416,521 entities); normalized beliefs; temporal decay |
| `postgresql-gisdb` (`msjarvis/gis`) | 5432→5432 | PostgreSQL 16 + PostGIS; 91 GB, 501 tables; 5,416,522 rows in `gbim_belief_normalized` incl. 20,593 landowner beliefs; `mvw_gbim_landowner_spatial` live |
| `jarvis-local-resources-db` | 5435→5435 | Community resources database; `building_parcel_county_tax_mv` 7,354,707 rows; added to compose March 17 |
| `jarvis-redis` | 6379→6379 | Redis async job state; 30-min TTL; idempotency TTL 1,800s; health cache |
| `jarvis-ollama` | 11434→11434 | Ollama LLM backend; `all-minilm-latest` 384-dim embeddings; `llama3.1:latest` LM Synthesizer; all 22 model proxies |

**Canonical ChromaDB collections — March 22, 2026 (all 384-dim via `all-minilm-latest`):**

| Collection | Records | Notes |
|---|---|---|
| `gbim_worldview_entities` | 5,416,521 | Complete WV GBIM spatial corpus |
| `autonomous_learner` | 21,181 | Growing 288/day; Phase 1.45 active retrieval on every chat |
| `psychological_rag` | 968 | Psychological domain RAG |
| `spiritual_texts` | 23 | Spiritual/cultural domain RAG |
| `appalachian_cultural_intelligence` | 5 | Appalachian cultural intelligence |
| `GBIM_sample_rows` | 5,000 | GBIM sample rows |
| `GBIM_sample` | 3 | GBIM sample |
| `msjarvis-smoke` | 1 | Smoke test record |
| `msjarvis_docs` | 0 | Scaffolded — pending ingest |
| `GBIM_Fayette_sample` | 0 | Scaffolded — pending ingest |
| `geospatial_features` | 0 | Scaffolded — pending backfill ingest |

> **LANDOWNER BELIEFS (`LANDOWNER_CORPORATE`, `LANDOWNER_GOVERNMENT`) are NOT in ChromaDB.** They are served exclusively by `gbimqueryrouter` (port 7205) via `mvw_gbim_landowner_spatial` in `msjarvis/gis`. 20,593 records. PostgreSQL-native path only.

> **Critical:** `nomic-embed-text` produces 768-dim vectors and is incompatible with all existing collections. Only `all-minilm-latest` (384-dim) may be used for any ChromaDB embedding generation.

---

## 19.8 (cont.) — Service Registry, Dynamic Ports, and Discovery

In addition to static ports defined in `docker-compose.yml`, the system uses a service registry and Redis-based dynamic port allocation for some components. Scripts such as `verify_all_claims.sh` check:

- Existence and contents of `service_registry.json`, which lists services with names and ports (updated March 20, 2026 to include `gbimqueryrouter` at port 7205).
- Redis keys of the form `service:{name}` that map to dynamically assigned ports.
- Health of registered services by iterating over the registry and issuing `GET /health` checks (results cached for 30s; per-service timeout: 2s).

---

## 19.8 (cont.) — Verified Reboot Sequence (March 22, 2026)

After any system reboot or `docker compose restart`, the full 80-container production stack is brought online with two commands:

```bash
# Step 1: Start all 80 compose-managed containers (includes gbimqueryrouter)
cd msjarvis-rebuild-working/msjarvis-rebuild
docker compose up -d

# Step 2: Start and verify the six pipeline containers (health checks)
./jarvis_startup.sh
# Go signal: Six green health check marks from jarvis_startup.sh:
#   ✅ jarvis-judge-truth
#   ✅ jarvis-judge-consistency
#   ✅ jarvis-judge-alignment
#   ✅ jarvis-judge-ethics
#   ✅ jarvis-judge-pipeline
#   ✅ jarvis-69dgm-bridge
```

`gbimqueryrouter` is compose-managed and starts with Step 1. It does not require `jarvis_startup.sh` intervention.

> **Important:** Before running `docker compose up -d` after any change to judge service source files in `services/`, verify build context integrity per §19.14. If source files were renamed, corrected, or restored, rebuild with `--no-cache` before bringing services up. This now explicitly includes checking that `COPY lm_synthesizer.py /app/` is **absent** from `services/Dockerfile.judge`.

---

## 19.8 (cont.) — External Access Points and LLM Backend

Only a small subset of ports are exposed to the host:

- **8051** — External API endpoint (mapped to `jarvis-main-brain` on 8050): `chat`, `chat_async`, `chat_status`, `chat_cancel`
- **7205** — `gbimqueryrouter` landowner GBIM queries (may be restricted to internal access only in production hardening)
- **11434** — Ollama LLM backend (`jarvis-ollama`): `all-minilm-latest` embeddings; all 22 model proxies; `llama3.1:latest` for LM Synthesizer
- **5432** — PostgreSQL `msjarvis/gis`: GBIM spatial, landowner beliefs, GeoDB source of truth
- **5433** — PostgreSQL `msjarvis`: GBIM belief store, RAG-facing
- **5435** — PostgreSQL `jarvis-local-resources-db`: community resources
- **6379** — Redis (`jarvis-redis`): async job state, idempotency, health cache

All other services communicate over the `qualia-net` Docker bridge network using container names and internal ports for discovery.

---

## 19.9 Async Job Management API

| Endpoint | Method | Function |
|---|---|---|
| `/chat_async` | POST | Create async job; returns `job_id` immediately |
| `/chat_status/{job_id}` | GET | Poll for progress and result |
| `/chat_cancel/{job_id}` | DELETE | Cancel a specific running job |
| `/chat_cancel_all` | DELETE | Cancel all running jobs |

**Implementation details:**
- Job state persists in Redis (`jarvis-redis:6379`) with 30-minute TTL
- State survives `jarvis-main-brain` container restarts
- Cancel operations perform true asyncio task cancellation — the 21-LLM pipeline stops immediately mid-run
- The `job_tasks` dict maps `job_id` to `asyncio.Task` for true interruption
- Idempotency TTL: Redis-backed, 1,800s
- Note: `gbimqueryrouter` landowner queries resolve in milliseconds via SQL and do not use the async job system unless called through the main-brain `chat_async` wrapper

The `/chat` endpoint is synchronous and takes ~436 seconds for a full pipeline run. The async job API (deployed March 17, 2026) allows immediate response with polling.

---

## 19.10 Observed Routing Behavior in Verification Scripts

Several shell scripts provide concrete evidence of how the container architecture behaves in practice:

- **`VERIFY_AND_TEST.sh`** — Checks RAG, web UI, and selected services, confirming that containerized components are reachable, that PostgreSQL `msjarvis/gis` is accessible at port 5432, and that semantic memory is populated. Updated March 20, 2026 to include `gbimqueryrouter` health check at port 7205.

- **`verify_all_claims.sh`** — Exercises a complete autonomous learning and I-Container flow, testing: current I-Container size and growth capacity; service registry and dynamic port integration via Redis (including `gbimqueryrouter` entry at port 7205); health of key services including `gbimqueryrouter`; PostgreSQL `msjarvis/gis` connection health and GBIM belief counts (now reporting 5,416,522 total: 5,395,929 spatial/facility + 20,593 landowner); `mvw_gbim_landowner_spatial` row count and spatial index health; I-Container analysis tools that report size, status, keywords, and suggested topics.

- **`VERIFY CHROMADB` sections** — Confirm that ChromaDB directories exist, that collections can be queried, that embedding counts match expectations, that all collections use 384-dim vectors (`all-minilm-latest`), and that landowner beliefs are correctly **absent** from ChromaDB (verified by confirming no `LANDOWNER_CORPORATE` or `LANDOWNER_GOVERNMENT` records in any ChromaDB collection).

---

## 19.11 Known Issues and Resolution Status (March 22, 2026)

| Issue | Status |
|---|---|
| Response truncation (730 chars, `max_tokens: 500`) | ✅ FIXED — `max_tokens` set to `-1` (unlimited); `llm22-proxy` 8,192-token limit confirmed |
| ChromaDB `DummyCollection` blocking semantic retrieval | ✅ FIXED — `all-minilm-latest` 384-dim semantic retrieval implemented March 17 |
| Redis response persistence in-memory only | ✅ FIXED — full Redis-backed job system with 30-min TTL deployed March 17 |
| 33 services not in `docker-compose.yml` | ✅ FIXED — all containers now in compose |
| Idempotency TTL in-memory only | ✅ FIXED — Redis-backed, 1,800s TTL |
| Judge pipeline URL: wrong port 7239 for all judges | ✅ FIXED — corrected to 7230/7231/7232/7233 March 16; default ports in `judge_pipeline.py` also corrected March 21 |
| LM Synthesizer calling `jarvis-roche-llm` (HTTP 500) | ✅ FIXED — now calls `jarvis-ollama:11434/api/generate` directly March 18 |
| NBB Prefrontal Cortex 422 errors | ✅ RESOLVED — `message` field payload confirmed correct; service healthy |
| I-Containers 422 errors | ✅ RESOLVED — port corrected to 8015 March 13 |
| BBB `truth_score` KeyError crash | ✅ FIXED — null guard added to BBB orchestrator March 18 |
| BBB blocking entire pipeline on HTTP 500 | ✅ FIXED — fail-open behavior on non-200 BBB responses March 18 |
| `web-research` and `rag-server` restart loops | ✅ FIXED — source files deployed via `docker cp` |
| Hash-prefixed container names | ✅ FIXED — `container_name` added to all 8 affected containers March 17–18 |
| `hilbert-gateway` port conflict | ✅ FIXED — resolved during March 17 compose audit |
| Build directives causing slow/unpredictable startup | ✅ FIXED — all `build` entries converted to `image` references for non-judge services March 17 |
| Docker Compose v1.29.2 `ContainerConfig` crash bug | ✅ FIXED — upgraded to Docker Compose v5.1.0 March 17 |
| *who* / *under whose authority* axes unpopulated at parcel scale | ✅ FIXED — 20,593 landowner beliefs ingested; `gbimqueryrouter` live March 20 |
| Landowner queries returning no results | ✅ FIXED — `mvw_gbim_landowner_spatial` materialized; both statewide and county-scoped patterns verified March 20 |
| Ghost file contamination (`lm_synthesizer.py` clones in `services/`) | ✅ **FULLY FIXED March 22, 2026** — real judge scripts restored from `services-safe` March 21; stray `COPY lm_synthesizer.py /app/` line removed from `services/Dockerfile.judge` March 22; `--no-cache` rebuild completed and verified across all 5 judge images March 22. Sub-judge default ports corrected; `bbb_check_verdict` stub replaced with live httpx call. See §19.14. |
| `bbb_check_verdict` stub — no live BBB call from judge pipeline | ✅ FIXED — live async httpx POST to `jarvis-blood-brain-barrier:8016/filter` March 21, 2026 |
| BBB steganography aggregation bug | ✅ FIXED — `steg_blocked=True` overrides `content_approved` when `clean=False` AND `threat_level` in (`critical`, `high`) — March 22, 2026 (see Chapter 16 §16.14) |
| Hallucination on local community resources (Mount Hope, Fayette County) | 🔴 **OPEN** — `gis_rag` and `local_resources` databases return empty for Mount Hope queries; LLMs generating from training data. Factually accurate programs (LIHEAP, WV 2-1-1) pass BBB. Fabricated organization names blocked by ethical filter. Root cause: real community resource data not yet loaded. Resolution: Community Champions data entry — next priority. |
| BBB ethical filter blocking "certainly" | ⚠️ **BY DESIGN** — ethical filter correctly detecting unverified specific claims; not a false positive |
| StarCoder2 returning 0-char responses on community queries | ⚠️ **KNOWN** — 21 of 22 models active; consensus extracted correctly; StarCoder2 proxied but unreliable on non-code queries |

---

## 19.12 Container Count History

| Date | Containers | Notable Addition |
|---|---|---|
| Initial deployment | 70 | Core stack |
| March 13, 2026 | 73 | I-Containers port fix; 3 corpus containers identified missing |
| March 17, 2026 | 79 | 9 missing containers added to compose; Redis async job system; Docker Compose v5.1.0 upgrade |
| March 18, 2026 | 79 | Compose audit complete; all `build` → `image` for non-judge services; hash-prefix names resolved |
| March 20, 2026 | 80 | `gbimqueryrouter` port 7205; landowner belief layer live |
| March 21, 2026 | 80 | Ghost file remediation (real judge scripts restored; sub-judge ports corrected; `bbb_check_verdict` live; `judgesigner.py` deployed) — container count unchanged |
| **March 22, 2026** | **80** | **Ghost file fix completed:** stray `COPY lm_synthesizer.py /app/` line removed from `services/Dockerfile.judge`; `--no-cache` rebuild verified across all 5 judge images; BBB steganography aggregation fix deployed — container count unchanged |

---

## 19.13 Summary

The container architecture and routing layer described here provide the structural glue between external interfaces, executive coordination, autonomous learning, and PostgreSQL long-term memory. As of March 22, 2026, this architecture is fully operationalized in an 80-container production stack, entirely managed by Docker Compose v5.1.0, with a verified two-command reboot sequence and Redis-backed async job management. The most significant updates since the March 21 snapshot are the March 22, 2026 ghost file fix completion (the stray `COPY lm_synthesizer.py /app/` line removed from `services/Dockerfile.judge` and `--no-cache` rebuild confirmed across all 5 judge images) and the BBB steganography aggregation fix. Together these close the last two silent failure modes identified in March sprint3: judge containers that could silently receive synthesizer logic through a Dockerfile residue, and a steganography detection that fired correctly but did not gate content. Build context integrity verification (§19.14) is now a required practice before any judge image rebuild, and it explicitly includes verification that `Dockerfile.judge` contains no `COPY lm_synthesizer.py` line.

Through a combination of Dockerized services, service registry mechanisms, 30s TTL health-check caching, Phase 1.45 community memory retrieval via `all-minilm-latest` 384-dim, and structured normalization of events into container records, the system can:

- Receive and categorize diverse inputs from users (synchronous and async), internal processes, and external signals.
- Apply safety filters (BBB 7-filter stack with `truth_score` null guard and fail-open on HTTP 500), eligibility checks against PostgreSQL GBIM truth, and basic policy decisions at the intake stage.
- Inject top-5 semantically relevant community memories from `autonomous_learner` (21,181 records) into every LLM prompt at Phase 1.45.
- Route `mode=landowner_gbim` queries directly to `gbimqueryrouter` (port 7205 → `mvw_gbim_landowner_spatial`), bypassing ChromaDB, the LLM ensemble, and web research entirely.
- Route normalized records into parallel paths for affective and analytical evaluation.
- Feed curated content into PostgreSQL long-term stores (I-Container, ChromaDB `chroma_data` volume, all collections 384-dim, GBIM graphs in PostgreSQL `msjarvis/gis` port 5432, 91 GB, 501 tables, 5,416,522 verified beliefs), and Redis-backed job state.

All memory and routing flows are ultimately anchored to PostgreSQL `msjarvis/gis` at port 5432.

---

## 19.14 Build Context Integrity (Updated — March 22, 2026)

> **This section was added March 21, 2026 and updated March 22, 2026 to document the full two-day ghost file remediation.**

### The Vulnerability — Silent Source File Contamination

On March 21, 2026, inspection of the running judge containers revealed that all four sub-judge source files in `services/` — the Docker build context for all judge images — were not real judge scripts. They were copies of `lm_synthesizer.py` with incorrect names, a silent artifact of a prior `mv` operation that had been committed without content verification. The corruption was undetectable by Docker alone. The containers:

- Built successfully — the clones were syntactically valid FastAPI services
- Started successfully — they bound to ports and responded to health checks
- Produced scores — they generated output indistinguishable in structure from real judge output

Only behavioral analysis (all four sub-judges producing identical behavior regardless of input) revealed the problem. The contamination persisted for multiple days across multiple sessions.

**March 22, 2026 residual artefact:** After real scripts were restored on March 21, a second issue was identified on March 22: `services/Dockerfile.judge` still contained the line:

```
COPY lm_synthesizer.py /app/
```

This line was a residue from the prior corrupted state. It did not prevent the corrected judge scripts from running (they were copied and started correctly by their respective `CMD` directives), but it silently deposited `lm_synthesizer.py` into every rebuilt judge image layer. This constituted an incomplete fix. The line was removed from `services/Dockerfile.judge` on March 22, 2026, and a full `--no-cache` rebuild was completed and verified across all 5 judge images. The ghost file fix is now **fully complete**.

### Why `services/` Is the Critical Directory

`services/` is the Docker build context for all five judge service images:

```yaml
jarvis-judge-pipeline:
  build:
    context: ./services
    dockerfile: Dockerfile.judge
  command: python judge_pipeline.py
jarvis-judge-truth:
  build:
    context: ./services
    dockerfile: Dockerfile.judge
  command: python judge_truth_filter.py
# ... and so on for all 5 judge services
```

When Docker builds a judge image, it copies **everything** in `services/` into the image layer. The `command` directive specifies which Python file to execute at container startup. If `judge_truth_filter.py` in `services/` contains `lm_synthesizer.py` code, the built image runs LM Synthesizer logic when told to execute `judge_truth_filter.py` — and Docker has no mechanism to detect that the file content does not match its name. Similarly, if `Dockerfile.judge` contains a `COPY lm_synthesizer.py /app/` line, that file will be silently deposited into the image even after the main judge scripts are corrected.

This makes `services/` a high-risk directory: any incorrect file copy, rename operation, or Dockerfile residue that deposits wrong content will silently corrupt the next image build, and that corruption will be invisible until the running behavior is inspected.

### Why `services-safe` Exists

`services-safe/` is the authoritative backup directory — a read-only reference copy of the canonical judge scripts and `Dockerfile.judge` that is never modified by routine operations. Its purpose is:
1. To provide a known-good source for restoration when `services/` is suspected or confirmed corrupted
2. To serve as the diff target for automated drift detection
3. To persist the verified versions of all judge scripts and `Dockerfile.judge` across sessions and branches

`services-safe/` should contain exactly:

```
services-safe/Dockerfile.judge          ← must NOT contain COPY lm_synthesizer.py /app/
services-safe/judge_pipeline.py
services-safe/judge_truth_filter.py
services-safe/judge_consistency_engine.py
services-safe/judge_alignment_filter.py
services-safe/judge_ethics_filter.py
services-safe/judge_signer.py
```

`services-safe/` must never be used as the Docker build context. It is a reference and restoration source only.

### Restoration Procedure

If ghost file contamination is detected in `services/`, restore all judge scripts **and** `Dockerfile.judge` from `services-safe/` before rebuilding:

```bash
# Restore all judge scripts and Dockerfile from authoritative backup
cp services-safe/judge_pipeline.py          services/judge_pipeline.py
cp services-safe/judge_truth_filter.py      services/judge_truth_filter.py
cp services-safe/judge_consistency_engine.py services/judge_consistency_engine.py
cp services-safe/judge_alignment_filter.py  services/judge_alignment_filter.py
cp services-safe/judge_ethics_filter.py     services/judge_ethics_filter.py
cp services-safe/Dockerfile.judge           services/Dockerfile.judge
cp services-safe/judge_signer.py            services/judge_signer.py

# Verify content after restore — no lm_synthesizer artifacts:
grep -l "lm_synthesizer" services/judge*.py
# Expected: empty output

# Verify Dockerfile.judge does NOT contain the stray COPY line (March 22, 2026 fix):
grep "COPY lm_synthesizer" services/Dockerfile.judge
# Expected: empty output

# Rebuild with --no-cache:
docker compose build --no-cache \
  jarvis-judge-pipeline \
  jarvis-judge-truth \
  jarvis-judge-consistency \
  jarvis-judge-alignment \
  jarvis-judge-ethics
```

### Detecting Drift Between `services/` and `services-safe/`

The primary drift detection command — run before every judge image rebuild:

```bash
# Check that services/ and services-safe/ contain the same judge-related files:
diff <(ls services/ | grep judge | sort) <(ls services-safe/ | grep judge | sort)
# Expected: empty output (no diff)

# If diff shows files missing from services/, restore from services-safe/:
cp services-safe/<missing_file> services/<missing_file>
```

Content verification — detect ghost file contamination even when filenames match:

```bash
# Verify no judge script in services/ contains lm_synthesizer artifacts:
grep -l "lm_synthesizer\|LMSynthesizer\|class LMSynthesizer\|port.*8001" services/judge*.py
# Expected: empty output

# Verify Dockerfile.judge does NOT contain stray COPY line (March 22, 2026 fix):
grep "COPY lm_synthesizer" services/Dockerfile.judge
# Expected: empty output

# Verify Dockerfile.judge is present in services/:
ls -la services/Dockerfile.judge
# Expected: file present, non-zero size

# Verify judge_signer.py is present in services/:
ls -la services/judge_signer.py
# Expected: file present, non-zero size

# Full content diff between services/ and services-safe/ for all judge files:
for f in judge_pipeline.py judge_truth_filter.py judge_consistency_engine.py \
          judge_alignment_filter.py judge_ethics_filter.py judge_signer.py Dockerfile.judge; do
  if ! diff -q services/$f services-safe/$f > /dev/null 2>&1; then
    echo "DRIFT DETECTED: $f"
  fi
done
# Expected: empty output (all files identical)
```

### The `--no-cache` Requirement

Docker's layer cache is based on file modification timestamps and build context hashes — not on file content semantics. When source files in `services/` are renamed, corrected, or restored, Docker may serve a cached image layer built from previous incorrect file content if `--no-cache` is not specified.

**Rule:** Any time a judge source file or `Dockerfile.judge` in `services/` is renamed, replaced, or restored, the judge images **must** be rebuilt with `--no-cache`:

```bash
# Rebuild all judge images without cache after any services/ file change:
docker compose build --no-cache \
  jarvis-judge-pipeline \
  jarvis-judge-truth \
  jarvis-judge-consistency \
  jarvis-judge-alignment \
  jarvis-judge-ethics

# Then bring services back up:
docker compose up -d \
  jarvis-judge-pipeline \
  jarvis-judge-truth \
  jarvis-judge-consistency \
  jarvis-judge-alignment \
  jarvis-judge-ethics
```

The `--no-cache` flag forces Docker to re-read every file in the build context from disk, guaranteeing that the rebuilt image reflects the actual current content of `services/` rather than a cached layer from a prior build.

### Operational Rule

Never use `docker compose build` without `--no-cache` for judge services after any file change in `services/`. Always run the pre-rebuild checklist. Always restore from `services-safe/` if content drift is detected. The build cache is a silent failure mode for this class of corruption. This rule applies regardless of how minor the change appears. A rename that looks cosmetic may have deposited wrong content under a correct name. A Dockerfile residue line may silently copy unwanted files into the image. The checklist is the only defense.

### Complete Pre-Rebuild Checklist

Before rebuilding any judge image, run all of the following in order:

```bash
# 1. Verify filename set matches between services/ and services-safe/:
diff <(ls services/ | grep judge | sort) <(ls services-safe/ | grep judge | sort)

# 2. Verify no ghost lm_synthesizer content in judge scripts:
grep -l "lm_synthesizer\|LMSynthesizer" services/judge*.py

# 3. Verify Dockerfile.judge does NOT contain stray COPY lm_synthesizer line (March 22, 2026):
grep "COPY lm_synthesizer" services/Dockerfile.judge
# Expected: empty output

# 4. Verify correct default sub-judge ports in judge_pipeline.py (lines 16-19):
grep "JUDGE.*URL.*7239" services/judge_pipeline.py
# Expected: empty output (7239 is coordinator only)

# 5. Verify bbb_check_verdict is not a stub:
grep "bbb_status.*stub" services/judge_pipeline.py
# Expected: empty output

# 6. Verify Dockerfile.judge and judge_signer.py are present:
ls -la services/Dockerfile.judge services/judge_signer.py

# 7. Only if all checks pass — rebuild with --no-cache:
docker compose build --no-cache \
  jarvis-judge-pipeline \
  jarvis-judge-truth \
  jarvis-judge-consistency \
  jarvis-judge-alignment \
  jarvis-judge-ethics

# 8. Bring services up and verify:
docker compose up -d \
  jarvis-judge-pipeline \
  jarvis-judge-truth \
  jarvis-judge-consistency \
  jarvis-judge-alignment \
  jarvis-judge-ethics
docker compose ps | grep judge
# Expected: all 5 services running, not restarting
```

*Last updated: 2026-03-22 by Carrie Kidd (Mamma Kidd), Mount Hope WV*
