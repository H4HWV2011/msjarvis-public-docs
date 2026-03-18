> **Why this matters for Polymathmatic Geography**
> This chapter explains how Ms. Jarvis's "front lobe" decides which instruments to play on each request, including a distinct neuro-inspired prefrontal stage. It supports:
> - **P1 – Every where is entangled** by routing between spatial, semantic, commons, and neurobiological services as one coordinated instrument grounded in three PostgreSQL databases (`msjarvis` port 5433 with 5,416,521 verified GBIM beliefs; `gisdb` port 5433 with 13 GB PostGIS spatial data; `jarvis-local-resources-db` port 5435 with community resources), including a prefrontal NBB layer that runs ahead of deeper reasoning.
> - **P3 – Power has a geometry** by making control flow and authority legible in the microservice graph and in explicit `consciousness_layers`, rather than hiding them inside a monolith.
> - **P5 – Design is a geographic act** by encoding how Appalachian questions are steered through local RAG sourced from PostgreSQL GBIM, web research, spiritual and BBB filters, a prefrontal cortex microservice, and a psychological pre-assessment layer.
> - **P12 – Intelligence with a ZIP code** by prioritizing place-aware services (GIS-backed RAG from PostgreSQL `gisdb`, MountainShares knowledge, local web research, community resources from `jarvis-local-resources-db`) whenever they are healthy.
> - **P16 – Power accountable to place** by exposing routing decisions, prefrontal verdicts, health state, and memory writes through explicit APIs, logs, and `consciousness_layers`, with temporal confidence decay (`confidence_decay` multiplier) applied to every response at Phase 5.
>
> As such, this chapter belongs to the **Computational Instrument** tier: it specifies the executive coordinator that turns a set of independent services into a single, inspectable cognitive system with a measurable prefrontal phase and a verified 9-phase production pipeline (~436s end-to-end benchmark, March 18, 2026).

```
┌─────────────────────────────────────────────────────────────┐
│   Executive Coordination Flow — 9-Phase Pipeline            │
│   (Production State: March 18, 2026)                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  UltimateRequest (message, userid, role)                    │
│      ↓                                                       │
│  Phase 1 — Service Discovery & Prefrontal Planning          │
│      -  discover_services() → available_services map         │
│         (health results cached 30s TTL, 2s timeout/service) │
│      -  Append prefrontal_planner ConsciousnessLayer         │
│      -  call_nbb_prefrontal → nbb-i-containers (8101)        │
│      ↓                                                       │
│  Phase 1.4 — BBB Input Filter (7 filters)                   │
│      -  EthicalFilter, SpiritualFilter                       │
│      -  SafetyMonitor (word-boundary regex, March 15)        │
│      -  ThreatDetection                                      │
│      -  SteganographyDetection (March 15)                    │
│      -  TruthVerification (March 15)                         │
│      -  ContextAwareness (March 15)                          │
│      -  truth_score null guard (March 18)                    │
│      -  fail-open on HTTP 500 (March 18)                     │
│      ↓                                                       │
│  Phase 1.45 — Community Memory Retrieval (NEW March 17)     │
│      -  all-minilm:latest → 384-dim embedding               │
│         via jarvis-ollama:11434/api/embeddings               │
│      -  Query autonomous_learner (21,181 records)            │
│      -  Top-5 memories prepended to enhanced_message         │
│      ↓                                                       │
│  Phase 2 — Truth Verdict                                    │
│      -  call_truth_filter → BBB POST /truth (port 8016)      │
│      -  truthverdict attached (advisory)                     │
│      ↓                                                       │
│  Phase 3 — Psychology Pre-Assessment                        │
│      -  jarvis-psychology-services (port 8019)               │
│      -  /psychological_assessment endpoint                   │
│      -  Severity classification, crisis indicator check      │
│      -  Deployed March 15, 2026                              │
│      ↓                                                       │
│  Phase 4 — Context Building (RAG)                           │
│      -  build_rag_context → jarvis-spiritual-rag (8005)      │
│        Queries PostgreSQL msjarvis (GBIM beliefs)           │
│        Queries PostgreSQL gisdb (PostGIS, 993 ZCTA)         │
│        Queries jarvis-local-resources-db (port 5435)        │
│        Queries ChromaDB (port 8000, chroma_data vol)        │
│        Queries psychological_rag_domain (port 8006)         │
│      -  build_web_context → jarvis-web-research (internal)   │
│      ↓                                                       │
│  Phase 3.5 — LM Synthesizer + Voice Delivery (MERGED)      │
│      -  jarvis-lm-synthesizer (port 8001)                    │
│      -  Calls jarvis-ollama:11434/api/generate directly      │
│      -  model: llama3.1:latest                               │
│      -  Ms. Egeria Jarvis persona prompt injected            │
│      -  Phase 3.75 ELIMINATED — merged into this pass        │
│      -  ~30–55s; saves ~40s vs. previous two-pass design     │
│      ↓                                                       │
│  Phase 2.5 — LLM Ensemble Synthesis                         │
│      -  Semaphore proxy (port 8030, max_concurrent: 4)       │
│      -  jarvis-20llm-production (port 8008)                  │
│      -  21 active models (22 proxies; StarCoder2 returns     │
│         0 chars on community queries)                        │
│      -  ~320–360s wall clock (rich prompt, CPU-only)         │
│      ↓                                                       │
│  Phase 3 — Judge Pipeline (UPDATED)                         │
│      -  4 judges evaluate consensus answer ONLY              │
│      -  raw_responses dump eliminated                        │
│      -  judge time reduced from ~85-100s to ~60-86s          │
│      -  ports: 7230 / 7231 / 7232 / 7233 (fixed March 16)  │
│      ↓                                                       │
│  Phase 7 — 69-DGM Cascade Validation                        │
│      -  jarvis-69dgm-bridge (port 9000)                      │
│      -  23 connectors × 3 stages = 69 DGM operations/pass    │
│      -  Architecturally authoritative                        │
│      ↓                                                       │
│  Phase 4.5 — BBB Output Guard                               │
│      -  apply_output_guards_async → BBB /filter (8.0s)       │
│      -  fail-open on HTTP 500 (March 18)                     │
│      -  debug logging: approved/blocked status               │
│      ↓                                                       │
│  Phase 5 — Confidence Decay Multiplier                      │
│      -  confidence_decay from GBIM temporal metadata         │
│      -  Applied to all responses (deployed March 15)         │
│      ↓                                                       │
│  Post-Processing                                            │
│      -  clean_response_for_display                           │
│      -  normalize_identity (Ms. Jarvis voice)                │
│      -  background_rag_store → ms_jarvis_memory              │
│      ↓                                                       │
│  UltimateResponse                                           │
│      -  response, servicesused, consciousnesslevel           │
│      -  processingtime, architecturelayers                   │
│      -  consciousnesslayers, truthverdict                    │
│      -  confidence_decay_applied                             │
│                                                              │
│  End-to-end benchmark (March 18, 2026): ~436 seconds        │
│  (optimized from 532s baseline; richer pipeline with        │
│   community memory enrichment)                              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> **Figure 17.1.** Executive coordination flow in Ms. Jarvis ULTIMATE: the 9-phase pipeline from UltimateRequest through service discovery (with 30s health cache) and prefrontal planning, BBB 7-filter input guard (with fail-open), Phase 1.45 community memory retrieval (21,181-item `autonomous_learner`), truth verdict, psychology pre-assessment, RAG context building from three PostgreSQL databases and ChromaDB, LM Synthesizer + Voice Delivery (merged, Phase 3.5), 21-model LLM ensemble synthesis, judge pipeline (consensus-only, Phase 3), 69-DGM cascade validation, BBB output guard (fail-open), confidence decay multiplier, and post-processing to UltimateResponse. End-to-end benchmark: ~436 seconds (March 18, 2026, optimized from 532s baseline).

---

## Status as of March 18, 2026

| Category | Details |
|---|---|
| **Implemented and verified (March 18, 2026)** | `jarvis-main-brain` confirmed running at **127.0.0.1:8050**. `UltimateRequest` model (message, userid, role, useallservices) and `UltimateResponse` (response, servicesused, consciousnesslevel, processingtime, architecturelayers, consciousnesslayers, truthverdict, confidence_decay_applied) both live. `SERVICES` registry and `discover_services()` health-check loop operational — **health results cached 30s TTL, 2s timeout per service** (added March 18). `prefrontal_planner` `ConsciousnessLayer` appended on every `/chat` call. `call_nbb_prefrontal` called unconditionally at the start of every `ultimate_chat` execution; NBB prefrontal cortex is `nbb-i-containers` at **127.0.0.1:8101** (internal 7005), confirmed running; payload `message` field confirmed correct (422 errors resolved). **Phase 1.4 — BBB 7-filter input stack:** EthicalFilter, SpiritualFilter, SafetyMonitor (word-boundary regex fix applied March 15), ThreatDetection, SteganographyDetection, TruthVerification, ContextAwareness — all confirmed operational. **`truth_score` null guard and fail-open on HTTP 500 added March 18.** **Phase 1.45 — Community Memory Retrieval (NEW March 17, 2026):** Semantic retrieval via `all-minilm:latest` (384-dim, pulled March 17 into `jarvis-ollama:11434`) queries `autonomous_learner` ChromaDB collection (21,181 records); top-5 most semantically similar community interaction records are prepended to `enhanced_message` before LLM processing. All ChromaDB collections use 384-dimensional vectors — `nomic-embed-text` (768-dim) is incompatible and must not be used. `call_truth_filter` invoking BBB on **0.0.0.0:8016** (`jarvis-blood-brain-barrier`, confirmed) for input truth verdict (Phase 2), attached as `truthverdict` on `UltimateResponse`. **Phase 3 — Psychology Pre-Assessment:** `jarvis-psychology-services` at **127.0.0.1:8019** providing `/psychological_assessment` — severity classification and crisis indicator check on every production request. **Phase 4 — RAG from three PostgreSQL databases + ChromaDB:** PostgreSQL `msjarvis` at **127.0.0.1:5433** (5,416,521 verified GBIM entities, 80 epochs, 206 source layers); `gisdb` at **127.0.0.1:5433** (PostGIS, 13 GB, 39 tables, 993 ZCTA centroids); `jarvis-local-resources-db` at **127.0.0.1:5435** (community resources); ChromaDB at **127.0.0.1:8000** (`chroma_data` volume, restored March 15); `psychological_rag_domain` at **127.0.0.1:8006** (restored March 15). **Phase 3.5 — LM Synthesizer + Voice Delivery (MERGED March 18):** `jarvis-lm-synthesizer` at **127.0.0.1:8001** now calls `jarvis-ollama:11434/api/generate` directly with `llama3.1:latest` and the Ms. Egeria Jarvis persona prompt injected. The previously separate Phase 3.75 (Final Polish via `llm22-proxy`) is **eliminated** — merged into a single Ollama pass, saving ~40 seconds per query. `jarvis-20llm-production` at **127.0.0.1:8008** (confirmed) as primary LLM fabric; **21 active models** (22 proxies; StarCoder2 returns 0 characters on community queries and is excluded from consensus); wall-clock consensus ~320–360s (rich prompt, CPU-only). Semaphore proxy (`jarvis-semaphore`, **port 8030**, `max_concurrent: 4`) confirmed as mandatory intermediary. **Phase 3 — Judge Pipeline (UPDATED):** 4 judges (truth, consistency, alignment, ethics) at ports 7230/7231/7232/7233 (corrected from 7239, March 16) now evaluate the **consensus answer only** — `raw_responses` dump from all 21 models is no longer sent to judges, reducing judge time from ~85–100s to ~60–86s. **Phase 7 — 69-DGM cascade:** `jarvis-69dgm-bridge` port 9000, 23 connectors × 3 stages = 69 DGM operations per pass, architecturally authoritative; `CHROMA_HOST` fix deployed March 16. `apply_output_guards_async` calling BBB `/filter` as Phase 4.5 output guard; timeout **8.0s** (fixed 2026-03-02); **fail-open on HTTP 500 and debug logging added March 18.** **Phase 5 — Confidence decay multiplier:** `confidence_decay` from GBIM temporal metadata applied to all responses. `normalize_identity` applied to every response. `background_rag_store` scheduling near-duplicate check and RAG write after every `/chat` response. **Redis-backed async job system (NEW March 17):** `/chat/async` + `/chat/status/{job_id}` + `/chat/cancel/{job_id}` + `/chat/cancel/all` — job state persists in Redis (`jarvis-redis:6379`) with 30-minute TTL; true asyncio task cancellation stops 21-LLM pipeline mid-run. **All 79 containers fully compose-managed as of March 17** (`~/msjarvis-rebuild-working/msjarvis-rebuild/docker-compose.yml`, Docker Compose v5.1.0, all `build:` → `image:` conversions complete). **End-to-end benchmark: ~436 seconds** (March 18, 2026, optimized from 532s baseline; richer pipeline with community memory enrichment). |
| **Partially implemented / scaffolded** | `truth_verdict` is attached to every response and is advisory in the current deployment — it does not hard-gate the input pipeline. Modules in `SERVICES` registry including `qualia_engine`, `i_containers`, `neurobiological_master`, and `autonomous_learner` are exercised in other workflows but not yet wired into the `/chat` path. `ms_jarvis_memory` is currently append-only; deduplication via near-duplicate similarity check is advisory. POC verification loop for GBIM `needs_verification=TRUE` entities not yet automated (flag-and-attenuate only). Hallucination from LLMs on community resources (Mount Hope, local nonprofits) remains open: verified knowledge bases (`gis_rag`, `local_resources`) return empty for Mount Hope queries; factually accurate programs (LIHEAP, WV 2-1-1) pass BBB; fabricated organization names are blocked by ethical filter. Root cause: real community resource data not yet in verified databases. |
| **Future work / design intent only** | Hard-gate behavior on `truth_verdict` for certain role or threat levels. Full wiring of `qualia_engine`, `i_containers`, `neurobiological_master`, and `autonomous_learner` into the `/chat` execution path. Automated POC verification loop (re-contact resource POC when `confidence_decay` threshold crossed, reset `confidence` to 1.0 on confirmation). Richer per-phase timing and per-model latency exposure via a dedicated metrics endpoint. UI layer consuming `/chat/async` poll pattern for non-blocking chat interface. GPU server acceleration (WVU partnership — pending). |

> **This chapter is the canonical description of the `ultimatechat` and `chatlight` execution paths.** All other chapters that reference "what happens on a user chat," "main brain coordination," or the `UltimateResponse` structure should cross-reference here.
>
> **`ultimatechat` authoritative 9-phase sequence (March 18, 2026):**
> `UltimateRequest` received → `prefrontal_planner` layer appended → `call_nbb_prefrontal` executed → **Phase 1.4** BBB 7-filter input stack (fail-open, `truth_score` null guard) → **Phase 1.45** community memory retrieval (`all-minilm:latest` → `autonomous_learner` 21,181 records → top-5 prepended to `enhanced_message`) → **Phase 2** `call_truth_filter` via BBB port 8016 `POST /truth` → `truthverdict` attached (advisory) → **Phase 3 (pre-LLM)** psychology pre-assessment via `jarvis-psychology-services` port 8019 → **Phase 4** RAG context via `jarvis-spiritual-rag` port 8005 (queries PostgreSQL `msjarvis` + `gisdb` + `jarvis-local-resources-db` + ChromaDB port 8000 + `psychological_rag_domain` port 8006) + `jarvis-web-research` (internal) → **Phase 3.5** LM Synthesizer port 8001 → `jarvis-ollama:11434/api/generate` (`llama3.1:latest`, Ms. Jarvis persona, merged with former Phase 3.75) → **Phase 2.5** `llm20production` synthesis via semaphore proxy port 8030 → `jarvis-20llm-production` port 8008 → **Phase 3 (post-LLM)** 4-judge pipeline ports 7230–7233 (consensus answer only, `raw_responses` eliminated) → **Phase 7** 69-DGM cascade port 9000 → **Phase 4.5** `apply_output_guards_async` via BBB (8.0s timeout, fail-open) → **Phase 5** `confidence_decay` multiplier → `normalize_identity` → `background_rag_store` into `ms_jarvis_memory` → `UltimateResponse` returned.
>
> **`/chat/async` + `/chat/status/{job_id}` (Redis-backed async, March 17, 2026):**
> `POST /chat/async` received → `job_id` returned instantly → background task runs full 9-phase pipeline → job state stored in Redis (`jarvis-redis:6379`, 30-min TTL, survives container restarts) → client polls `GET /chat/status/{job_id}` → result with full `UltimateResponse` fields. `DELETE /chat/cancel/{job_id}` and `DELETE /chat/cancel/all` perform true asyncio task cancellation — 21-LLM pipeline stops immediately mid-run.

---

# 17. Executive Coordination Overview

This chapter describes the concrete control layer implemented by the `Ms. Jarvis ULTIMATE` main-brain service on **port 8050**, which decides which subsystems to invoke, in what order, and under which constraints for each request. It serves as a bridge between the neuro-inspired NBB modules and the containerized services that implement them, with emphasis on responsibilities, information flows, and observed runtime behavior. As of March 18, 2026, the full 9-phase production pipeline has been end-to-end verified at approximately **436 seconds** (optimized from a 532s pre-optimization baseline), with Phase 1.45 community memory retrieval added, Phase 3 judges operating on consensus-only, and Phases 3.5 and 3.75 merged into a single LM Synthesizer + Voice Delivery pass.

---

## 17.1 Role in the System

In the current deployment, the executive layer is realized by a single FastAPI application, `jarvis-main-brain` (confirmed running at **127.0.0.1:8050**), which coordinates 79 operational containers across consciousness, processing, and infrastructure services based on a static `SERVICES` registry and live health checks (cached 30s TTL, 2s per-service timeout as of March 18). For each user request, this layer interprets the input, runs a neuro-inspired prefrontal stage, runs a 7-filter BBB input gate, retrieves semantic community memories (Phase 1.45), performs psychology pre-assessment, builds RAG context from three PostgreSQL databases and ChromaDB, synthesizes via the 21-active-model ensemble, validates through the judge pipeline and 69-DGM cascade, applies the BBB output guard, and applies the GBIM temporal confidence decay multiplier before returning a coherent reply.

Interpretation is handled via the `UltimateRequest` model, which captures the user's message, `userid`, a `role` (for example `"community"`), and a `useallservices` flag indicating whether broad fan-out is permitted. Planning is expressed in explicit code that uses the `SERVICES` dictionary plus `discover_services()` to decide which components are actually available. Integration merges the outputs of selected components, applies BBB-based safety filtering, normalizes Ms. Jarvis's identity, applies the confidence decay multiplier, and returns an `UltimateResponse` containing `response`, `servicesused`, `consciousnesslevel`, `processingtime`, `architecturelayers`, `consciousnesslayers`, `truthverdict`, and `confidence_decay_applied`.

This chapter is the system of record for what actually happens on a live user chat. Other chapters describing "main brain behavior," "consciousness coordinator," or "executive layer" — including Chapters 11, 12, 16, 23, and 25 — should point here for the authoritative execution path.

---

## 17.2 Inputs and Signals

When deciding how to process a `/chat` call, the coordinator draws on several classes of signals. The primary input is the `UltimateRequest` payload, which encodes the current message, the user identity, a role label, and a high-level instruction about whether to use all services. A second key input is the dynamic `available_services` map, obtained by probing each entry in the `SERVICES` dictionary for a healthy response via `check_service_health` — **results are now cached for 30 seconds with a 2-second per-service timeout** (added March 18, eliminating the ~0.7s-per-query overhead after the first check).

The `SERVICES` registry includes: `qualia_engine`, `consciousness_bridge`, `blood_brain_barrier`, `neurobiological_master`, `i_containers`, `autonomous_learner`, `rag_server`, `web_research`, `llm20_production`, `lm_synthesizer` (port 8001), `psychology_services` (port 8019), `psychological_rag_domain` (port 8006), and NBB microservices. All three PostgreSQL databases (ports 5433 and 5435) and ChromaDB (port 8000, checked via `/api/v1/heartbeat`) are also monitored. Ollama is checked via `/api/tags` to eliminate double-404 round trips.

For asynchronous jobs created via `/chat/async`, the system maintains Redis-backed job tables (`jarvis-redis:6379`, 30-minute TTL) keyed by `job_id`, with each entry storing job status (queued, running, done, or error), a progress string, creation time, the original message and `userid`, and on completion the full result object. True asyncio task cancellation is supported — `DELETE /chat/cancel/{job_id}` or `DELETE /chat/cancel/all` stops the 21-LLM pipeline immediately mid-run via `_job_tasks[job_id].cancel()`. Global settings — including the API key, the `MAX_CONCURRENT_CHATS` semaphore limit (2 sessions), and service URLs — are represented via environment variables and module-level constants.

---

## 17.3 Concrete Request Flow — 9-Phase Pipeline

In the current deployment, the concrete decision flow for a synchronous `/chat` request is implemented by the `ultimate_chat` handler and follows a reproducible, fixed 9-phase sequence. The full pipeline end-to-end benchmark is approximately **436 seconds** (March 18, 2026, optimized from 532s baseline).

**Phase 1 — Service discovery and prefrontal planning.** When a request arrives, the coordinator logs the message and constructs an empty `available_services` dictionary, populating it by iterating over all `(service_name, url)` pairs in `SERVICES` and invoking `check_service_health`. Health results are **cached for 30 seconds** with a **2-second timeout per service** — after the first query, Phase 1 completes in ~0.7s or less. The coordinator then appends a `ConsciousnessLayer` named `"prefrontal_planner"` with `kind="prefrontal"` and `status="active"`. Immediately afterward, it calls `call_nbb_prefrontal` with the raw message and a simple context dictionary containing `userid` and `role`. The NBB prefrontal cortex service is `nbb-i-containers` at **127.0.0.1:8101** (internal 7005), confirmed running; the correct payload uses the `message` field (422 errors resolved March 18). Its result is recorded as a second `ConsciousnessLayer` named `"nbb_prefrontal_cortex"`. This stage runs unconditionally at the start of every `ultimate_chat` call.

**Phase 1.4 — BBB 7-filter input stack.** Before community memory retrieval, the request passes through the 7-filter blood-brain barrier input stack on **port 8016**: EthicalFilter, SpiritualFilter, SafetyMonitor (word-boundary regex fix applied March 15 — word-boundary threshold ≤3 chars eliminates false-positives on community resource terms), ThreatDetection, SteganographyDetection (deployed March 15), TruthVerification (deployed March 15), and ContextAwareness (deployed March 15). **As of March 18:** a `truth_score` null guard prevents `KeyError` crashes on BBB responses with missing fields, and the BBB input filter is **fail-open on HTTP 500** — if the BBB service returns a non-200 response, the pipeline continues rather than blocking. Total Phase 1.4 cost: ~1.3s. See **Chapter 16** for full BBB specification.

**Phase 1.45 — Semantic community memory retrieval (NEW — March 17, 2026).** After the BBB input filter approves the query and before truth verdict, the main brain performs semantic memory retrieval grounded in the `autonomous_learner` ChromaDB collection:

1. The query is embedded via `all-minilm:latest` at `jarvis-ollama:11434/api/embeddings`, producing a **384-dimensional** vector.
2. The vector is used to query `autonomous_learner` (21,181 records as of March 18, 2026).
3. The 5 most semantically similar community interaction records are retrieved (documents + metadata + distances).
4. The retrieved memories are prepended to `enhanced_message` before it reaches the LLM ensemble.

> **Critical — Embedding model lock:** All ChromaDB collections use **384-dimensional vectors** produced by `all-minilm:latest`. The `nomic-embed-text` model produces **768-dimensional vectors** and is **incompatible** with all existing collections. Any service, script, or migration that generates embeddings for ChromaDB must use `all-minilm:latest`. The `_DummyCollection` error that previously blocked semantic retrieval is resolved — `all-minilm` semantic retrieval is the fix.

**Phase 2 — Truth verdict on the input.** The coordinator sends the original user message through `call_truth_filter`, which invokes `jarvis-blood-brain-barrier` on **port 8016** via `POST /truth` and returns a slim verdict containing `valid`, `confidence`, and `principalreasons`. This verdict is attached as `truthverdict` in the final response. In the current deployment, the pipeline treats this verdict as advisory rather than as a hard gate; hard-gate behavior for specific role or threat levels is identified as future work.

**Phase 3 (pre-LLM) — Psychology pre-assessment.** The request is assessed by `jarvis-psychology-services` at **127.0.0.1:8019** (deployed March 15, 2026) via `/psychological_assessment`. This service classifies severity and checks for crisis indicators on every production request, returning `psychological_assessment`, `therapeutic_guidance`, `emotional_support`, `wellbeing_recommendations`, and `evidence_based_approaches`. It is backed by `psychological_rag_domain` (port 8006), which queries ChromaDB's psychological corpus (968 records). This phase was absent prior to March 15 due to missing container builds and the missing ChromaDB volume.

**Phase 4 — Context building with RAG and web research.** For context gathering, the coordinator checks whether `"rag_server"` and `"web_research"` appear in `available_services` and, if so, calls them via `build_rag_context` and `build_web_context`. The RAG helper queries `jarvis-spiritual-rag` at **port 8005** (confirmed running — earlier plan documents listed 8103; the correct port is **8005**) via its `/search` endpoint, which in turn queries:
- PostgreSQL `msjarvis` (port 5433) — 5,416,521 GBIM beliefs with temporal decay metadata
- PostgreSQL `gisdb` (port 5433) — PostGIS, 13 GB, 39 tables, 993 ZCTA centroids
- PostgreSQL `jarvis-local-resources-db` (port 5435) — community resources (confirmed in end-to-end benchmark)
- ChromaDB (port 8000, `chroma_data` volume) — `gbim_worldview_entities` and other collections (all 384-dim, `all-minilm:latest`)
- `psychological_rag_domain` (port 8006) — psychological corpus (968 records)

The web helper calls `jarvis-web-research` (internal Docker network). These blocks are combined into a `context_block` and used by `build_egeria_prompt` to construct the enhanced prompt grounded in PostgreSQL GBIM spatial and institutional knowledge, with Phase 1.45 community memories already prepended.

**Phase 3.5 — LM Synthesizer + Voice Delivery (MERGED — March 18, 2026).** The previously separate Phase 3.5 (LM Synthesizer refinement) and Phase 3.75 (Final LLM Polish via `llm22-proxy`) have been **merged into a single Ollama call**. `jarvis-lm-synthesizer` at **port 8001** now:
1. Takes the judge pipeline's `final_answer` directly.
2. Calls `jarvis-ollama:11434/api/generate` with `llama3.1:latest` (LM Synthesizer URL fixed from `jarvis-roche-llm` to `jarvis-ollama`, March 18).
3. Injects the Ms. Egeria Jarvis persona prompt — warm, maternal, Appalachian voice, no meta-commentary.
4. Returns the final response directly without a separate polish pass.

**Phase 3.75 is eliminated.** The redundant `llm22-proxy` call is removed, saving approximately **40 seconds per query**. Wall-clock cost for the merged Phase 3.5: ~30–55s.

**Phase 2.5 — LLM fabric selection and execution.** The coordinator targets `llm20_production` as its primary LLM fabric. The ensemble (`jarvis-20llm-production`, port **8008**) is accessed via the semaphore proxy (`jarvis-semaphore`, port **8030**, `max_concurrent: 4`), which is a mandatory intermediary that serializes concurrent Ollama requests. The semaphore proxy requires a float `timeout` value in its payload; the main brain passes `600.0` and uses `httpx.Timeout(None, connect=5.0, read=None)` on its own client. **21 of 22 proxy containers produce usable responses**; StarCoder2 (llm7-proxy, port 8207) frequently returns 0-character responses on community queries and is excluded from consensus extraction. Wall-clock ensemble time is approximately **320–360 seconds** for the full pipeline (rich prompt, CPU-only inference). Standalone direct calls to port 8008 with short prompts complete in ~110s; the difference reflects prompt size in the full pipeline.

**Active LLM model roster (21 active, 22 proxies):**

| Proxy | Port | Model |
|---|---|---|
| llm1-proxy | 8201 | TinyLlama (`tinyllama:latest`) |
| llm2-proxy | 8202 | Gemma (`gemma:2b`) |
| llm3-proxy | 8203 | MedLlama2 (`medllama2:latest`) |
| llm4-proxy | 8204 | MiniCPM-V (`minicpm-v:latest`) |
| llm5-proxy | 8205 | LLaVA (`llava:latest`) |
| llm6-proxy | 8206 | SQLCoder (`sqlcoder:latest`) |
| llm7-proxy | 8207 | StarCoder2 (`starcoder2:latest`) — **0-char on community queries** |
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

For full details on the ensemble and judge pipeline, see **Chapter 33**.

**Phase 3 (post-LLM) — Judge pipeline (UPDATED — March 16, 2026).** All LLM ensemble outputs pass through the 4-judge pipeline (truth, consistency, alignment, ethics) at ports 7230, 7231, 7232, and 7233 (corrected from previously wrong port 7239). **Critically, the judges now evaluate the consensus answer only** — the full `raw_responses` dump from all 21 models is no longer sent to the judge payload. This change reduced judge pipeline wall-clock time from ~85–100s to **~60–86s**, a significant throughput improvement. Judge outputs are architecturally authoritative and inform the `final_answer` handed to the LM Synthesizer.

**Phase 7 — 69-DGM cascade validation.** All responses pass through `jarvis-69dgm-bridge` at **port 9000**, which runs 23 active connectors through a 3-stage observe–propose–evaluate cascade: 23 × 3 = 69 DGM operations per pass. `CHROMA_HOST` fix deployed March 16 restored ChromaDB connectivity for the bridge. Verdicts are architecturally authoritative and are not overridden by downstream components. All validation is grounded in PostgreSQL `msjarvis` GBIM beliefs. See **Chapter 32** for full 69-DGM specification.

**Phase 4.5 — BBB output guard.** The raw LLM output passes through `clean_response_for_display` to strip legacy RAG metadata, then through `apply_output_guards_async`, which calls the BBB's `/filter` endpoint on port 8016 using `httpx.AsyncClient(timeout=8.0)`. The 8-second timeout is a permanent architectural fix (2026-03-02). **As of March 18:** the output guard is **fail-open on HTTP 500** — if the BBB `/filter` endpoint returns a non-200 response, the filtered content passes through unchanged and the failure is logged. Debug logging now emits explicit `approved`/`blocked` status on every output guard invocation.

**Phase 5 — Confidence decay multiplier.** The GBIM temporal confidence decay metadata (deployed March 15, 2026) is applied to the response. Every GBIM entity carries `last_verified`, `confidence_decay`, and `needs_verification` fields. The `confidence_decay` multiplier attenuates response confidence when the response draws on entities not recently confirmed. At the March 18 baseline, 100% of 5,416,521 entities carry `needs_verification=TRUE` — the expected state at system launch, not a data quality error. The POC verification loop (future work) will clear this flag as entities are confirmed.

**Post-processing.** After Phase 5, `normalize_identity` ensures the answer speaks as Ms. Egeria Jarvis rather than as a generic LLM — confirmed producing identity-aware responses on both synchronous and async paths. In parallel, `background_rag_store` checks for near-duplicate entries via `/search` with `top_k=1` and, if no near-duplicate is found, stores a truncated version of the query and response plus metadata into `ms_jarvis_memory`. The final `UltimateResponse` aggregates the safe, normalized answer, `servicesused`, `consciousnesslevel` (currently `"ultimate_collective"`), total `processingtime`, `architecturelayers`, the consciousness layers, the BBB `truthverdict`, and `confidence_decay_applied`.

---

## 17.4 Interaction with Other Layers

Because the `SERVICES` registry spans consciousness, processing, gateway, and infrastructure layers, the executive coordinator sits at their intersection. It decides whether a given request will be routed through context layers (all three PostgreSQL databases, ChromaDB, `psychological_rag_domain`) or handled with a narrower subset when those subsystems are unavailable, and it unconditionally exercises the NBB prefrontal cortex, Phase 1.45 community memory retrieval, 7-filter BBB input stack, psychology pre-assessment, LM Synthesizer + Voice (merged), judge pipeline, 69-DGM cascade, and BBB output guard on every production request.

Although the registry includes modules like `qualia_engine`, `i_containers`, `autonomous_learner` (queried at Phase 1.45 for community memory; not yet wired into the core `/chat` orchestration path), and `neurobiological_master`, these remain available for other workflows and are identified as future expansion points for the `/chat` path. Three new services deployed March 15 — `jarvis-hippocampus` (episodic memory indexing), `jarvis-toroidal-geometry` (topological spatial reasoning), and `jarvis-psychology-services` port 8019 — are now wired into the production path. All 79 containers are fully compose-managed as of March 17, 2026, via `~/msjarvis-rebuild-working/msjarvis-rebuild/docker-compose.yml` (Docker Compose v5.1.0, all `build:` directives converted to `image:` references — no rebuilds required on startup).

---

## 17.5 Asynchronous Job Handling

The executive layer exposes a Redis-backed asynchronous interface for long-running requests.

**Full-pipeline async (`/chat/async`, `/chat/status/{job_id}`, `/chat/cancel/{job_id}`, `/chat/cancel/all`) — NEW March 17, 2026.** When a client submits an async request, the service generates a `job_id`, stores an entry in Redis (`jarvis-redis:6379`, 30-minute TTL) with `status: "processing"`, and launches `process_chat_job` as an independent asyncio task registered in `_job_tasks`. That coroutine runs the full 9-phase `ultimate_chat` coordination pipeline — service discovery, NBB prefrontal execution, 7-filter BBB input stack, Phase 1.45 community memory retrieval, truth verdict, psychology pre-assessment, RAG context building, LM Synthesizer + Voice (merged), 21-model ensemble synthesis, judge pipeline (consensus-only), 69-DGM validation, BBB output guard, confidence decay multiplier, identity normalization, and background RAG storage — updating job status as it proceeds and marking the entry `"complete"` or `"error"` on termination. **Job state survives `jarvis-main-brain` container restarts** because Redis persists the state independently. `DELETE /chat/cancel/{job_id}` performs true asyncio task cancellation — the 21-LLM pipeline stops immediately mid-run. `DELETE /chat/cancel/all` cancels all active jobs simultaneously.

**Lightweight consensus async (`/chatlight/async` + `/chatlight/status/{job_id}`).** Added 2026-03-02 (git tag `v2026.03.02-chatlight-async-working`). This interface bypasses the full prefrontal, community memory, RAG, and web-research pipeline and routes directly to the 21-model ensemble via the semaphore proxy. The submit endpoint returns a `job_id` and `poll_url` instantly. The client polls `/chatlight/status/{job_id}` at any interval; the response includes `status` (queued / running / done / error), `elapsed` seconds, and on completion a `result` object containing `answer`, `response`, `latency`, `mode: "light-async"`, `models_responded`, and `userid`. `normalize_identity` is applied, confirming that Ms. Jarvis's identity voice is present on the lightweight path. Note: `/chatlight` does not include Phase 1.45 community memory enrichment; use `/chat/async` for community-memory-grounded responses.

---

## 17.6 Verified Reboot Sequence (NEW — March 17, 2026)

After any system reboot or `docker compose` restart, Ms. Egeria Jarvis is brought back online with two commands:

```bash
# Step 1: Start all compose-managed containers (79 total)
cd ~/msjarvis-rebuild-working/msjarvis-rebuild && docker compose up -d

# Step 2: Start and verify the six pipeline containers + health checks
~/jarvis_startup.sh
```

**Go signal:** The startup script confirms six green health checkmarks:
- `jarvis-judge-truth` ✅
- `jarvis-judge-consistency` ✅
- `jarvis-judge-alignment` ✅
- `jarvis-judge-ethics` ✅
- `jarvis-judge-pipeline` ✅
- `jarvis-69dgm-bridge` ✅

The startup script (`~/jarvis_startup.sh`) manages these six containers for historical reasons; it includes health verification with retry logic using `docker exec` Python `urllib` internally, as these containers do not expose ports to the host. Container management details as of March 17, 2026:

- All 79 containers defined in `~/msjarvis-rebuild-working/msjarvis-rebuild/docker-compose.yml`
- All `build:` directives replaced with `image:` references — **no rebuild required on startup**
- Docker Compose v5.1.0 (upgraded from broken v1.29.2, which caused `ContainerConfig` crash bug)
- All 8 previously hash-prefixed container names (e.g., `981f44e18cf6_jarvis-20llm-production`) now have clean names via `container_name:` in compose
- All corpus containers (including `jarvis-local-resources`, `jarvis-hippocampus`, `jarvis-gis-rag`, `jarvis-spiritual-rag`) added to compose permanently

---

## 17.7 RAG Storage and Memory Integration

The executive coordinator not only consumes RAG context from three PostgreSQL databases and ChromaDB but also contributes new experience back into `ms_jarvis_memory` via `background_rag_store`. After assembling a final response for a `/chat` request, it schedules this coroutine with the original message, the final response text, and the list of `servicesused`. The background task first calls the RAG server's `/search` endpoint with the query and `top_k=1` to check for near-duplicates; if the top result's similarity score exceeds a configured threshold, the task logs a `rag_skip_duplicate` event and skips the write.

If the query is sufficiently novel, the task calls the RAG server's `/store` endpoint with a payload that includes a system `userid` (for example `"autosystem"`), truncated versions of the query and response, an ISO-formatted timestamp, and metadata such as the first few `servicesused` and flags indicating the record was auto-stored and deduplicated. In the current deployment, `ms_jarvis_memory` is append-only; the deduplication check is advisory. Because this consolidation occurs in the background, the main `/chat` response returns promptly while memory updates proceed asynchronously. The `autonomous_learner` collection (21,181 records, growing ~288/day) is written separately by the autonomous learning subsystem and is the source queried at Phase 1.45 — not written by `background_rag_store`.

---

## 17.8 Health-Check and Prefrontal Behavior

Service discovery uses `check_service_health` to probe each configured service, preferring `/health` when available and otherwise falling back to a GET on the service's primary operation path or root URL. **As of March 18:** ChromaDB is checked via `/api/v1/heartbeat` and Ollama via `/api/tags` (eliminates double-404 round trips). All health results are **cached for 30 seconds** — the ~0.7s Phase 1 cost only occurs on the first query; subsequent queries within the window use cached results.

With `nbb-i-containers` at **127.0.0.1:8101** confirmed running and the `message` field payload confirmed correct (422 errors resolved), `discover_services` includes `"nbb_prefrontal_cortex"` in `available_services`, enabling the prefrontal stage to run reliably at the start of each `ultimate_chat` request. The prefrontal call uses a short timeout (currently 3 seconds) and does not block the rest of the pipeline: if the NBB service is slow or unavailable, `call_nbb_prefrontal` returns a status of `"timeout"` or `"exception"` and the main coordinator continues. When the NBB service responds successfully, its consciousness-bridge-style summary is recorded under `prefrontal_response` and its internal layers are nested under `consciousnesslayers`.

---

## 17.9 Operational Pattern and Performance

Empirical measurements from the reference host (Legion 5, Intel i9, NVIDIA RTX 4050 — **CPU-only inference, size_vram: 0 on all models**, 29 GB RAM, 20 GB Ollama container limit) show the following latency profile as of March 18, 2026:

| Phase | Wall-clock cost |
|---|---|
| Phase 1: Health checks | ~0.7s (cached after first query) |
| Phase 1.4: BBB input (7 filters) | ~1.3s total (incl. Phase 1.45) |
| Phase 1.45: Community memory (ChromaDB) | included in Phase 1.4 total |
| Phase 1.75–3: Pre-LLM consciousness layers | ~0.5s |
| Phase 2.5: 21 LLMs (rich prompt) | ~320–360s (hardware floor, CPU-only) |
| Phase 3: Judge pipeline (consensus only) | ~60–86s |
| Phase 3.5: LM Synthesizer + Voice (merged) | ~30–55s |
| Phase 4 + 4.5: Bridge + BBB output | ~0.5s |
| **End-to-end total** | **~436s (optimized from 532s baseline)** |

For comparison: direct calls to port 8008 with short prompts complete in ~110s; the ~320–360s ensemble time in the full pipeline reflects the richer, community-memory-enriched prompt. The path to faster inference is GPU server acceleration via the WVU partnership (pending).

- **`/chatlight/async` (lightweight consensus):** 21-model ensemble completes in ~120–145s; full job wall clock ~130–160s including semaphore queuing, BBB output guard (8s), and identity normalization. Does not include Phase 1.45 community memory enrichment.
- **`/chat/async` (full 9-phase pipeline, Redis-backed):** Same ~436s as synchronous; returns `job_id` instantly; client polls for result.
- **Semaphore queuing effect:** Multiple concurrent requests queue in `jarvis-semaphore` (max 4 concurrent). Back-to-back test calls accumulate ~320–360s each. Restart the semaphore between test sessions to drain queued work before benchmarking.

---

## 17.10 Implementation vs. Conceptual Model

In the current deployment, the running implementation of the executive layer closely tracks the conceptual responsibilities set out at the beginning of the chapter. The March 15–18, 2026 deployment cycle completes the gap between declared 9-phase architecture and live pipeline execution:

- **Previously declared but unconfirmed (March 15 baseline):** LM Synthesizer Phase 3.5, psychology pre-assessment Phase 3, SteganographyDetection + TruthVerification + ContextAwareness in BBB Phase 1.4, 69-DGM cascade Phase 7, confidence decay multiplier Phase 5, `jarvis-local-resources-db` RAG retrieval.
- **Confirmed operational March 15–18:** All of the above, plus: Phase 1.45 community memory retrieval (new), judge pipeline consensus-only mode (faster), Phase 3.5/3.75 merged (saves ~40s), 21-active-model consensus, Redis-backed async jobs with true cancellation, health-check caching, BBB fail-open on HTTP 500, all 79 containers fully compose-managed.

There remain deliberate gaps between the broader architectural vision and this entrypoint's wiring. The `SERVICES` registry includes additional neurobiological and community-oriented modules (`qualia_engine`, `i_containers`, `neurobiological_master`, `autonomous_learner` — the last of which is queried at Phase 1.45 but not yet wired into the broader `/chat` orchestration) that are exercised in other workflows but not yet integrated into the core `/chat` decision path. The automated POC verification loop for GBIM `needs_verification=TRUE` entities remains future work. This staged integration strategy allows the system to deliver robust, explainable responses while preserving room for future experiments in deeper neurobiological and community-governance coupling.

---

## 17.11 Summary

The executive coordination layer — realized by `jarvis-main-brain` at **127.0.0.1:8050** — provides a concrete and instrumented account of how a multi-layer cognitive architecture is orchestrated in practice across 79 operational containers. The confirmed execution sequences are:

**`/chat` (synchronous, full 9-phase pipeline — ~436s benchmark, March 18, 2026):**
1. `UltimateRequest` (message, userid, role, useallservices) received at `/chat`
2. `prefrontal_planner` `ConsciousnessLayer` appended; `available_services` populated (30s cache, 2s timeout)
3. `call_nbb_prefrontal` executed unconditionally → `nbb-i-containers` at **127.0.0.1:8101** (payload: `message` field)
4. **Phase 1.4** — BBB 7-filter input stack → **0.0.0.0:8016** (EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection, SteganographyDetection, TruthVerification, ContextAwareness; `truth_score` null guard; fail-open on HTTP 500)
5. **Phase 1.45** — Community memory retrieval: `all-minilm:latest` (384-dim) via `jarvis-ollama:11434/api/embeddings` → `autonomous_learner` (21,181 records) → top-5 prepended to `enhanced_message`
6. **Phase 2** — `call_truth_filter` → BBB **port 8016** `POST /truth` → `truthverdict` attached (advisory)
7. **Phase 3 (pre-LLM)** — `jarvis-psychology-services` **port 8019** → `/psychological_assessment` severity classification
8. **Phase 4** — RAG context: `jarvis-spiritual-rag` **port 8005** queries PostgreSQL `msjarvis` (port 5433) + `gisdb` (port 5433) + `jarvis-local-resources-db` (port 5435) + ChromaDB (port 8000) + `psychological_rag_domain` (port 8006); web context: `jarvis-web-research` (internal Docker network)
9. **Phase 3.5** — LM Synthesizer **port 8001** → `jarvis-ollama:11434/api/generate` (`llama3.1:latest`, Ms. Jarvis persona, merged with eliminated Phase 3.75; ~30–55s)
10. **Phase 2.5** — `llm20production` synthesis → semaphore proxy (port 8030) → `jarvis-20llm-production` **port 8008** (~320–360s, 21 active models)
11. **Phase 3 (post-LLM)** — 4-judge pipeline ports 7230–7233 (consensus answer only, `raw_responses` eliminated; ~60–86s)
12. **Phase 7** — 69-DGM cascade **port 9000** (23 × 3 = 69 DGM operations, authoritative)
13. **Phase 4.5** — `apply_output_guards_async` → BBB **port 8016** `/filter` (8.0s timeout, fail-open on HTTP 500, debug logging)
14. **Phase 5** — `confidence_decay` multiplier applied from GBIM temporal metadata
15. `normalize_identity` applied
16. `background_rag_store` scheduled → `ms_jarvis_memory` (append-only, dedup advisory)
17. `UltimateResponse` returned: `response`, `servicesused`, `consciousnesslevel`, `processingtime`, `architecturelayers`, `consciousnesslayers`, `truthverdict`, `confidence_decay_applied`

**`/chat/async` + `/chat/status/{job_id}` (Redis-backed full-pipeline async — March 17, 2026):**
1. `POST /chat/async` received → `job_id` returned instantly; state stored in Redis (`jarvis-redis:6379`, 30-min TTL)
2. Background asyncio task registered in `_job_tasks[job_id]`; runs full 9-phase pipeline (same as `/chat` above)
3. Job state (`processing` → `complete`/`error`) survives `jarvis-main-brain` container restarts
4. `DELETE /chat/cancel/{job_id}` — true asyncio task cancellation, stops 21-LLM pipeline mid-run
5. `DELETE /chat/cancel/all` — cancels all active jobs simultaneously
6. Client polls `GET /chat/status/{job_id}` → returns `status`, `progress`, and on completion full `result`

**`/chatlight/async` + `/chatlight/status/{job_id}` (async, lightweight consensus — verified March 2, 2026):**
1. `POST /chatlight/async` received → `job_id` + `poll_url` returned instantly
2. Background task acquires `chat_semaphore`; calls `discover_services()`
3. `build_egeria_prompt` constructs enhanced message (no Phase 1.45 community memory on this path)
4. `httpx.Timeout(None, connect=5.0, read=None)` client → semaphore proxy (port 8030) → `jarvis-20llm-production` (port 8008, timeout 600.0 passed to semaphore)
5. 21-model ensemble completes (~120–145s); response extracted from `body["response"]`
6. `clean_response_for_display` → `apply_output_guards_async` (BBB, 8.0s timeout, fail-open) → `normalize_identity`
7. Job marked `done`; `result` includes `answer`, `latency`, `mode: "light-async"`, `models_responded`
8. Client polls `GET /chatlight/status/{job_id}` → returns `status`, `elapsed`, `result`

By anchoring the high-level metaphors of prefrontal control, community memory grounding, introspection, and consolidation in specific code paths, data structures, and performance measurements — grounded in three PostgreSQL databases (`msjarvis` port 5433: 5,416,521 GBIM entities, 80 epochs, 206 source layers; `gisdb` port 5433: 13 GB PostGIS, 993 ZCTA centroids; `jarvis-local-resources-db` port 5435: community resources) and confirmed at ~436s end-to-end (optimized from 532s baseline) — this layer demonstrates that the thesis's coordination concepts are not only architecturally coherent but also implementable, measurable, and amenable to targeted optimization. For details on the 21-active-model ensemble and judge pipeline (consensus-only, ~60–86s) invoked at Phases 2.5 and 3, see **Chapter 33**. For the 69-DGM cascade see **Chapter 32**. For the BBB 7-filter stack see **Chapter 16**. For the Neurobiological Master's own BBB → I-containers → Qualia → consciousness-bridge pipeline (a separate flow not in the primary `/chat` path) see **Chapter 12**. For GBIM temporal confidence decay and POC verification loop design see **Chapter 9**.
