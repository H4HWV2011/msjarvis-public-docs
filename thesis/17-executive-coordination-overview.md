> **Why this matters for Polymathmatic Geography**
> This chapter explains how Ms. Jarvis's "front lobe" decides which instruments to play on each request, including a distinct neuro-inspired prefrontal stage. It supports:
> - **P1 – Every where is entangled** by routing between spatial, semantic, commons, and neurobiological services as one coordinated instrument grounded in three PostgreSQL databases (`msjarvis` port 5433 with 5,416,521 verified GBIM beliefs; `gisdb` port 5433 with 13 GB PostGIS spatial data; `jarvis-local-resources-db` port 5435 with community resources), including a prefrontal NBB layer that runs ahead of deeper reasoning.
> - **P3 – Power has a geometry** by making control flow and authority legible in the microservice graph and in explicit `consciousness_layers`, rather than hiding them inside a monolith.
> - **P5 – Design is a geographic act** by encoding how Appalachian questions are steered through local RAG sourced from PostgreSQL GBIM, web research, spiritual and BBB filters, a prefrontal cortex microservice, and a psychological pre-assessment layer.
> - **P12 – Intelligence with a ZIP code** by prioritizing place-aware services (GIS-backed RAG from PostgreSQL `gisdb`, MountainShares knowledge, local web research, community resources from `jarvis-local-resources-db`) whenever they are healthy.
> - **P16 – Power accountable to place** by exposing routing decisions, prefrontal verdicts, health state, and memory writes through explicit APIs, logs, and `consciousness_layers`, with temporal confidence decay (`confidence_decay` multiplier) applied to every response at Phase 5.
>
> As such, this chapter belongs to the **Computational Instrument** tier: it specifies the executive coordinator that turns a set of independent services into a single, inspectable cognitive system with a measurable prefrontal phase and a verified 9-phase production pipeline (349.87s end-to-end benchmark, March 15, 2026).

```
┌─────────────────────────────────────────────────────────────┐
│   Executive Coordination Flow — 9-Phase Pipeline            │
│   (Production State: March 15, 2026, commit b90f9ff)        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  UltimateRequest (message, userid, role)                    │
│      ↓                                                       │
│  Phase 1 — Service Discovery & Prefrontal Planning          │
│      -  discover_services() → available_services map         │
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
│  Phase 3.5 — LM Synthesizer Pre-Processing                  │
│      -  jarvis-lm-synthesizer (port 8001)                    │
│      -  Structures/enriches RAG context before ensemble      │
│      -  Confirmed operational March 15, 2026                 │
│      ↓                                                       │
│  Phase 2.5 — LLM Ensemble Synthesis                         │
│      -  Semaphore proxy (port 8030, max_concurrent: 4)       │
│      -  jarvis-20llm-production (port 8008)                  │
│      -  22/22 models HTTP 200 (March 15, 2026)               │
│      -  ~120-145s wall clock                                 │
│      ↓                                                       │
│  Phase 7 — 69-DGM Cascade Validation                        │
│      -  jarvis-69dgm-bridge (port 9000)                      │
│      -  23 connectors × 3 stages = 69 DGM operations/pass    │
│      -  Architecturally authoritative                        │
│      ↓                                                       │
│  Phase 4.5 — BBB Output Guard                               │
│      -  apply_output_guards_async → BBB /filter (8.0s)       │
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
│  End-to-end benchmark (March 15, 2026): 349.87 seconds      │
│  Query: "What community resources are available in          │
│          Fayette County, WV?" — all 9 phases approved       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> **Figure 17.1.** Executive coordination flow in Ms. Jarvis ULTIMATE: the 9-phase pipeline from UltimateRequest through service discovery and prefrontal planning, BBB 7-filter input guard, truth verdict, psychology pre-assessment, RAG context building from three PostgreSQL databases and ChromaDB, LM Synthesizer pre-processing, LLM ensemble synthesis, 69-DGM cascade validation, BBB output guard, confidence decay multiplier, and post-processing to UltimateResponse. End-to-end benchmark: 349.87 seconds (March 15, 2026, all phases approved).

---

## Status as of March 15, 2026

| Category | Details |
|---|---|
| **Implemented and verified (March 15, 2026)** | `jarvis-main-brain` confirmed running at **127.0.0.1:8050**. `UltimateRequest` model (message, userid, role, useallservices) and `UltimateResponse` (response, servicesused, consciousnesslevel, processingtime, architecturelayers, consciousnesslayers, truthverdict, confidence_decay_applied) both live. `SERVICES` registry and `discover_services()` health-check loop operational. `prefrontal_planner` `ConsciousnessLayer` appended on every `/chat` call. `call_nbb_prefrontal` called unconditionally at the start of every `ultimate_chat` execution; NBB prefrontal cortex is `nbb-i-containers` at **127.0.0.1:8101** (internal 7005), confirmed running. **Phase 1.4 — BBB 7-filter input stack:** EthicalFilter, SpiritualFilter, SafetyMonitor (word-boundary regex fix applied March 15), ThreatDetection, SteganographyDetection, TruthVerification, ContextAwareness — all confirmed operational. `call_truth_filter` invoking BBB on **0.0.0.0:8016** (`jarvis-blood-brain-barrier`, confirmed) for input truth verdict (Phase 2), attached as `truthverdict` on `UltimateResponse`. **Phase 3 — Psychology Pre-Assessment:** `jarvis-psychology-services` at **127.0.0.1:8019** (deployed March 15) providing `/psychological_assessment` — severity classification and crisis indicator check on every production request. **Phase 4 — RAG from three PostgreSQL databases + ChromaDB:** PostgreSQL `msjarvis` at **127.0.0.1:5433** (5,416,521 verified GBIM entities, 80 epochs, 206 source layers); `gisdb` at **127.0.0.1:5433** (PostGIS, 13 GB, 39 tables, 993 ZCTA centroids); `jarvis-local-resources-db` at **127.0.0.1:5435** (community resources, confirmed in March 15 end-to-end benchmark); ChromaDB at **127.0.0.1:8000** (`chroma_data` volume, restored March 15); `psychological_rag_domain` at **127.0.0.1:8006** (restored March 15). **Phase 3.5 — LM Synthesizer:** `jarvis-lm-synthesizer` at **127.0.0.1:8001** — pre-processes and structures RAG-retrieved context before passing to 22-model ensemble; confirmed operational March 15. `jarvis-20llm-production` at **127.0.0.1:8008** (confirmed) as primary LLM fabric; **22/22 models HTTP 200** (March 15, first time achieved); wall-clock consensus ~120–145s. Semaphore proxy (`jarvis-semaphore`, **port 8030**, `max_concurrent: 4`) confirmed as mandatory intermediary. **Phase 7 — 69-DGM cascade:** `jarvis-69dgm-bridge` port 9000, 23 connectors × 3 stages = 69 DGM operations per pass, architecturally authoritative. `apply_output_guards_async` calling BBB `/filter` as Phase 4.5 output guard; timeout **8.0s** (fixed 2026-03-02). **Phase 5 — Confidence decay multiplier:** `confidence_decay` from GBIM temporal metadata (deployed March 15) applied to all responses; 100% of 5,416,521 entities carry `needs_verification=TRUE` at launch baseline. `normalize_identity` applied to every response. `background_rag_store` scheduling near-duplicate check and RAG write after every `/chat` response. `/chatlight/async` + `/chatlight/status/{job_id}` async interface live (added 2026-03-02). `/chat/async` + `/chat/status/{job_id}` full-pipeline async interface live. **End-to-end 9-phase pipeline test PASSED March 15: 349.87 seconds** — query "What community resources are available in Fayette County, WV?" — all 9 phases approved. Git commit `b90f9ff`. |
| **Partially implemented / scaffolded** | `truth_verdict` is attached to every response and is advisory in the current deployment — it does not hard-gate the input pipeline. Modules in `SERVICES` registry including `qualia_engine`, `i_containers`, `neurobiological_master`, and `autonomous_learner` are exercised in other workflows but not yet wired into the `/chat` path. `ms_jarvis_memory` is currently append-only; deduplication via near-duplicate similarity check is advisory. `active_jobs` for both async interfaces is in-memory only; does not survive container restarts. POC verification loop for GBIM `needs_verification=TRUE` entities not yet automated (flag-and-attenuate only). |
| **Future work / design intent only** | Hard-gate behavior on `truth_verdict` for certain role or threat levels. Full wiring of `qualia_engine`, `i_containers`, `neurobiological_master`, and `autonomous_learner` into the `/chat` execution path. Persistent job store replacing in-memory `active_jobs`. Automated POC verification loop (re-contact resource POC when `confidence_decay` threshold crossed, reset `confidence` to 1.0 on confirmation). Richer per-phase timing and per-model latency exposure via a dedicated metrics endpoint. UI layer consuming `/chatlight/async` poll pattern for non-blocking chat interface. |

> **This chapter is the canonical description of the `ultimatechat` and `chatlight` execution paths.** All other chapters that reference "what happens on a user chat," "main brain coordination," or the `UltimateResponse` structure should cross-reference here.
>
> **`ultimatechat` authoritative 9-phase sequence (March 15, 2026):**
> `UltimateRequest` received → `prefrontal_planner` layer appended → `call_nbb_prefrontal` executed → **Phase 1.4** BBB 7-filter input stack → **Phase 2** `call_truth_filter` via BBB port 8016 → **Phase 3** psychology pre-assessment via `jarvis-psychology-services` port 8019 → **Phase 4** RAG context via `jarvis-spiritual-rag` port 8005 (queries PostgreSQL `msjarvis` + `gisdb` + `jarvis-local-resources-db` + ChromaDB port 8000 + `psychological_rag_domain` port 8006) + `jarvis-web-research` (internal) → **Phase 3.5** LM Synthesizer port 8001 pre-processing → **Phase 2.5** `llm20production` synthesis via semaphore proxy port 8030 → `jarvis-20llm-production` port 8008 → **Phase 7** 69-DGM cascade port 9000 → **Phase 4.5** `apply_output_guards_async` via BBB (8.0s timeout) → **Phase 5** `confidence_decay` multiplier → `normalize_identity` → `background_rag_store` into `ms_jarvis_memory` → `UltimateResponse` returned.
>
> **`chatlight/async` authoritative sequence:**
> `POST /chatlight/async` received → `job_id` returned instantly → background task: semaphore proxy (port 8030) → `jarvis-20llm-production` (port 8008, ~120–145s) → `apply_output_guards_async` via BBB (8.0s timeout) → `normalize_identity` → job marked `done`; client polls `GET /chatlight/status/{job_id}` → result with `mode: "light-async"`, `models_responded`, `latency`.

---

# 17. Executive Coordination Overview

This chapter describes the concrete control layer implemented by the `Ms. Jarvis ULTIMATE` main-brain service on **port 8050**, which decides which subsystems to invoke, in what order, and under which constraints for each request. It serves as a bridge between the neuro-inspired NBB modules and the containerized services that implement them, with emphasis on responsibilities, information flows, and observed runtime behavior. As of March 15, 2026 (commit `b90f9ff`), the full 9-phase production pipeline has been end-to-end verified at 349.87 seconds, with all phases approved.

---

## 17.1 Role in the System

In the current deployment, the executive layer is realized by a single FastAPI application, `jarvis-main-brain` (confirmed running at **127.0.0.1:8050**), which coordinates 79 operational containers across consciousness, processing, and infrastructure services based on a static `SERVICES` registry and live health checks. For each user request, this layer interprets the input, runs a neuro-inspired prefrontal stage, runs a 7-filter BBB input gate, performs psychology pre-assessment, builds RAG context from three PostgreSQL databases and ChromaDB, synthesizes via the 22-model ensemble, validates through the 69-DGM cascade, applies the BBB output guard, and applies the GBIM temporal confidence decay multiplier before returning a coherent reply.

Interpretation is handled via the `UltimateRequest` model, which captures the user's message, `userid`, a `role` (for example `"community"`), and a `useallservices` flag indicating whether broad fan-out is permitted. Planning is expressed in explicit code that uses the `SERVICES` dictionary plus `discover_services()` to decide which components are actually available. Integration merges the outputs of selected components, applies BBB-based safety filtering, normalizes Ms. Jarvis's identity, applies the confidence decay multiplier, and returns an `UltimateResponse` containing `response`, `servicesused`, `consciousnesslevel`, `processingtime`, `architecturelayers`, `consciousnesslayers`, `truthverdict`, and `confidence_decay_applied`.

This chapter is the system of record for what actually happens on a live user chat. Other chapters describing "main brain behavior," "consciousness coordinator," or "executive layer" — including Chapters 11, 12, 16, 23, and 25 — should point here for the authoritative execution path.

---

## 17.2 Inputs and Signals

When deciding how to process a `/chat` call, the coordinator draws on several classes of signals. The primary input is the `UltimateRequest` payload, which encodes the current message, the user identity, a role label, and a high-level instruction about whether to use all services. A second key input is the dynamic `available_services` map, obtained by probing each entry in the `SERVICES` dictionary for a healthy response via `check_service_health`.

The `SERVICES` registry includes: `qualia_engine`, `consciousness_bridge`, `blood_brain_barrier`, `neurobiological_master`, `i_containers`, `autonomous_learner`, `rag_server`, `web_research`, `llm20_production`, `lm_synthesizer` (port 8001), `psychology_services` (port 8019), `psychological_rag_domain` (port 8006), and NBB microservices. All three PostgreSQL databases (ports 5433 and 5435) and ChromaDB (port 8000) are also monitored.

For asynchronous jobs created via `/chat/async` or `/chatlight/async`, the system maintains in-memory job tables keyed by `job_id`, with each entry storing job status (queued, running, done, or error), a progress string, creation time, the original message and `userid`, and on completion the full result object. Global settings — including the API key, the `MAX_CONCURRENT_CHATS` semaphore limit (2 sessions), and service URLs — are represented via environment variables and module-level constants.

---

## 17.3 Concrete Request Flow — 9-Phase Pipeline

In the current deployment, the concrete decision flow for a synchronous `/chat` request is implemented by the `ultimate_chat` handler and follows a reproducible, fixed 9-phase sequence. The full pipeline was end-to-end verified on March 15, 2026 at 349.87 seconds.

**Phase 1 — Service discovery and prefrontal planning.** When a request arrives, the coordinator logs the message and constructs an empty `available_services` dictionary, populating it by iterating over all `(service_name, url)` pairs in `SERVICES` and invoking `check_service_health`. It then appends a `ConsciousnessLayer` named `"prefrontal_planner"` with `kind="prefrontal"` and `status="active"`. Immediately afterward, it calls `call_nbb_prefrontal` with the raw message and a simple context dictionary containing `userid` and `role`. The NBB prefrontal cortex service is `nbb-i-containers` at **127.0.0.1:8101** (internal 7005), confirmed running. Its result is recorded as a second `ConsciousnessLayer` named `"nbb_prefrontal_cortex"`. This stage runs unconditionally at the start of every `ultimate_chat` call.

**Phase 1.4 — BBB 7-filter input stack.** Before truth verdict, the request passes through the 7-filter blood-brain barrier input stack on **port 8016**: EthicalFilter, SpiritualFilter, SafetyMonitor (word-boundary regex fix applied March 15 — eliminates false-positives on community resource terms), ThreatDetection, SteganographyDetection (deployed March 15), TruthVerification (deployed March 15), and ContextAwareness (deployed March 15). All 7 filters are confirmed operational as of March 15, 2026. See **Chapter 16** for full BBB specification.

**Phase 2 — Truth verdict on the input.** The coordinator sends the original user message through `call_truth_filter`, which invokes `jarvis-blood-brain-barrier` on **port 8016** via `POST /truth` and returns a slim verdict containing `valid`, `confidence`, and `principalreasons`. This verdict is attached as `truthverdict` in the final response. In the current deployment, the pipeline treats this verdict as advisory rather than as a hard gate; hard-gate behavior for specific role or threat levels is identified as future work.

**Phase 3 — Psychology pre-assessment.** The request is assessed by `jarvis-psychology-services` at **127.0.0.1:8019** (deployed March 15, 2026) via `/psychological_assessment`. This service classifies severity and checks for crisis indicators on every production request, returning `psychological_assessment`, `therapeutic_guidance`, `emotional_support`, `wellbeing_recommendations`, and `evidence_based_approaches`. It is backed by `psychological_rag_domain` (port 8006), which queries ChromaDB's psychological corpus (restored March 15 with `chroma_data` volume). This phase was absent prior to March 15 due to missing container builds and the missing ChromaDB volume.

**Phase 4 — Context building with RAG and web research.** For context gathering, the coordinator checks whether `"rag_server"` and `"web_research"` appear in `available_services` and, if so, calls them via `build_rag_context` and `build_web_context`. The RAG helper queries `jarvis-spiritual-rag` at **port 8005** (confirmed running; earlier plan documents listed 8103 — the correct port is **8005**) via its `/search` endpoint, which in turn queries:
- PostgreSQL `msjarvis` (port 5433) — 5,416,521 GBIM beliefs with temporal decay metadata
- PostgreSQL `gisdb` (port 5433) — PostGIS, 13 GB, 39 tables, 993 ZCTA centroids
- PostgreSQL `jarvis-local-resources-db` (port 5435) — community resources (confirmed in March 15 benchmark)
- ChromaDB (port 8000, `chroma_data` volume) — `gbim_worldview_entities` and other collections
- `psychological_rag_domain` (port 8006) — psychological corpus

The web helper calls `jarvis-web-research` (internal Docker network, port 8008/tcp, no host binding — distinct from `jarvis-20llm-production` which binds host port 8008). These blocks are combined into a `context_block` and used by `build_egeria_prompt` to construct the enhanced prompt grounded in PostgreSQL GBIM spatial and institutional knowledge.

**Phase 3.5 — LM Synthesizer pre-processing.** Before ensemble synthesis, the RAG-retrieved context passes through `jarvis-lm-synthesizer` at **port 8001** (confirmed operational March 15). The LM Synthesizer normalizes, structures, and enriches the combined context from all three PostgreSQL databases and ChromaDB before it enters the 22-model ensemble. Prior to March 15 this service was returning HTTP 500, meaning ensemble inputs were unstructured RAG concatenations.

**Phase 2.5 — LLM fabric selection and execution.** The coordinator targets `llm20_production` as its primary LLM fabric. The ensemble (`jarvis-20llm-production`, port **8008**) is accessed via the semaphore proxy (`jarvis-semaphore`, port **8030**, `max_concurrent: 4`), which is a mandatory intermediary that serializes concurrent Ollama requests. The semaphore proxy requires a float `timeout` value in its payload; the main brain passes `600.0` and uses `httpx.Timeout(None, connect=5.0, read=None)` on its own client so the semaphore manages the deadline. **22/22 LLM proxy containers respond with HTTP 200** as of March 15, 2026 — the first time full 22/22 response has been achieved (previously 21/22 with BakLLaVA disabled). Wall-clock consensus time is approximately 120–145 seconds depending on system load. For full details on the 22-model ensemble and judge pipeline (consistency score 0.975), see **Chapter 33**.

**Phase 7 — 69-DGM cascade validation.** All responses pass through `jarvis-69dgm-bridge` at **port 9000**, which runs 23 active connectors through a 3-stage observe–propose–evaluate cascade: 23 × 3 = 69 DGM operations per pass. Verdicts are architecturally authoritative and are not overridden by downstream components. All validation is grounded in PostgreSQL `msjarvis` GBIM beliefs. See **Chapter 32** for full 69-DGM specification.

**Phase 4.5 — BBB output guard.** The raw LLM output passes through `clean_response_for_display` to strip legacy RAG metadata, then through `apply_output_guards_async`, which calls the BBB's `/filter` endpoint on port 8016 using `httpx.AsyncClient(timeout=8.0)`. The 8-second timeout is a permanent architectural fix (2026-03-02): the original `timeout=None` caused the entire chat response to hang indefinitely after the ensemble completed.

**Phase 5 — Confidence decay multiplier.** The GBIM temporal confidence decay metadata (deployed March 15, 2026) is applied to the response. Every GBIM entity carries `last_verified`, `confidence_decay`, and `needs_verification` fields. The `confidence_decay` multiplier attenuates response confidence when the response draws on entities not recently confirmed. At the March 15 launch baseline, 100% of 5,416,521 entities carry `needs_verification=TRUE` — the expected state at system launch, not a data quality error. The POC verification loop (future work) will clear this flag as entities are confirmed.

**Post-processing.** After Phase 5, `normalize_identity` ensures the answer speaks as Ms. Egeria Jarvis rather than as a generic LLM — confirmed producing identity-aware responses on both synchronous and async paths. In parallel, `background_rag_store` checks for near-duplicate entries via `/search` with `top_k=1` and, if no near-duplicate is found, stores a truncated version of the query and response plus metadata into `ms_jarvis_memory`. The final `UltimateResponse` aggregates the safe, normalized answer, `servicesused`, `consciousnesslevel` (currently `"ultimate_collective"`), total `processingtime`, `architecturelayers`, the consciousness layers, the BBB `truthverdict`, and `confidence_decay_applied`.

---

## 17.4 Interaction with Other Layers

Because the `SERVICES` registry spans consciousness, processing, gateway, and infrastructure layers, the executive coordinator sits at their intersection. It decides whether a given request will be routed through context layers (all three PostgreSQL databases, ChromaDB, `psychological_rag_domain`) or handled with a narrower subset when those subsystems are unavailable, and it unconditionally exercises the NBB prefrontal cortex, 7-filter BBB input stack, psychology pre-assessment, LM Synthesizer, 69-DGM cascade, and BBB output guard on every production request.

Although the registry includes modules like `qualia_engine`, `i_containers`, `autonomous_learner`, and `neurobiological_master`, in the current `/chat` path these remain available for other workflows and are identified as future expansion points. Three new services deployed March 15 — `jarvis-hippocampus` (episodic memory indexing), `jarvis-toroidal-geometry` (topological spatial reasoning), and `jarvis-psychology-services` port 8019 — are now wired into the production path. Upstream, unified gateways and academic front-ends treat `Ms. Jarvis ULTIMATE` as a single main-brain endpoint. Downstream, the executive layer fans out to 79 operational containers.

---

## 17.5 Asynchronous Job Handling

The executive layer exposes two asynchronous interfaces for long-running requests.

**Full-pipeline async (`/chat/async` + `/chat/status/{job_id}`).** When a client submits an async request, the service generates a `job_id`, inserts an entry into the `active_jobs` dictionary with `status: "processing"`, and launches `process_chat_job` as an independent task. That coroutine runs the full 9-phase `ultimate_chat` coordination pipeline — service discovery, NBB prefrontal execution, 7-filter BBB input stack, truth verdict, psychology pre-assessment, RAG context building from three PostgreSQL databases and ChromaDB, LM Synthesizer pre-processing, 22-model ensemble synthesis, 69-DGM validation, BBB output guard, confidence decay multiplier, identity normalization, and background RAG storage — updating job status as it proceeds and marking the entry `"complete"` or `"error"` on termination.

**Lightweight consensus async (`/chatlight/async` + `/chatlight/status/{job_id}`).** Added 2026-03-02 (git tag `v2026.03.02-chatlight-async-working`). This interface bypasses the full prefrontal, RAG, and web-research pipeline and routes directly to the 22-model ensemble via the semaphore proxy. The submit endpoint returns a `job_id` and `poll_url` instantly. The client polls `/chatlight/status/{job_id}` at any interval; the response includes `status` (queued / running / done / error), `elapsed` seconds, and on completion a `result` object containing `answer`, `response`, `latency`, `mode: "light-async"`, `models_responded`, and `userid`. `normalize_identity` is applied, confirming that Ms. Jarvis's identity voice is present on the lightweight path. In both async interfaces, `active_jobs` is in-memory only; a persistent job store is identified as future work.

---

## 17.6 RAG Storage and Memory Integration

The executive coordinator not only consumes RAG context from three PostgreSQL databases and ChromaDB but also contributes new experience back into `ms_jarvis_memory` via `background_rag_store`. After assembling a final response for a `/chat` request, it schedules this coroutine with the original message, the final response text, and the list of `servicesused`. The background task first calls the RAG server's `/search` endpoint with the query and `top_k=1` to check for near-duplicates; if the top result's similarity score exceeds a configured threshold, the task logs a `rag_skip_duplicate` event and skips the write.

If the query is sufficiently novel, the task calls the RAG server's `/store` endpoint with a payload that includes a system `userid` (for example `"autosystem"`), truncated versions of the query and response, an ISO-formatted timestamp, and metadata such as the first few `servicesused` and flags indicating the record was auto-stored and deduplicated. In the current deployment, `ms_jarvis_memory` is append-only; the deduplication check is advisory. Because this consolidation occurs in the background, the main `/chat` response returns promptly while memory updates proceed asynchronously, maintaining the three-database PostgreSQL-grounded knowledge base without blocking user interactions.

---

## 17.7 Health-Check and Prefrontal Behavior

Service discovery uses `check_service_health` to probe each configured service, preferring `/health` when available and otherwise falling back to a GET on the service's primary operation path or root URL. ChromaDB (port 8000), Redis, LM Synthesizer (port 8001), and `rag_server` are treated as always healthy or checked via specialized endpoints to avoid unnecessary overhead. All three PostgreSQL databases (ports 5433 and 5435) are monitored for connectivity.

With `nbb-i-containers` at **127.0.0.1:8101** confirmed running, `discover_services` includes `"nbb_prefrontal_cortex"` in `available_services`, enabling the prefrontal stage to run reliably at the start of each `ultimate_chat` request. The prefrontal call uses a short timeout (currently 3 seconds) and does not block the rest of the pipeline: if the NBB service is slow or unavailable, `call_nbb_prefrontal` returns a status of `"timeout"` or `"exception"` and the main coordinator continues. When the NBB service responds successfully, its consciousness-bridge-style summary is recorded under `prefrontal_response` and its internal layers are nested under `consciousnesslayers`.

---

## 17.8 Operational Pattern and Performance

Empirical measurements from the reference host (Legion 5, local Docker) show the following latency profile as of March 15, 2026:

- **`/chatlight/async` (lightweight consensus):** 22-model ensemble completes in ~120–145s; full job wall clock ~130–160s including semaphore queuing, BBB output guard (8s), and identity normalization. HTTP connection returns instantly; client polls for result.
- **`/chat` (full 9-phase pipeline, synchronous):** End-to-end latency **349.87 seconds** (verified March 15, 2026, all 9 phases approved). LLM ensemble (~120–145s) is the largest single contributor; RAG retrieval from three PostgreSQL databases and ChromaDB, LM Synthesizer (port 8001), 69-DGM cascade, BBB guard, psychology pre-assessment, and confidence decay multiplier account for the remainder.
- **Semaphore queuing effect:** Multiple concurrent requests queue in `jarvis-semaphore` (max 4 concurrent). Each Ollama model run is sequential within the ensemble, so back-to-back test calls accumulate ~120–145s each. The semaphore should be restarted between test sessions to drain queued work before benchmarking.
- **Hardware envelope:** Legion 5 (Intel i9, NVIDIA RTX 4050, 29 GB RAM); Ollama container memory limit 20 GB; MAX_CONCURRENT_CHATS 2 sessions.

The `MAX_CONCURRENT_CHATS` semaphore and explicit logging of per-phase timing provide operators with levers for tuning throughput and responsiveness without sacrificing safety or introspection.

---

## 17.9 Implementation vs. Conceptual Model

In the current deployment, the running implementation of the executive layer closely tracks the conceptual responsibilities set out at the beginning of the chapter. The March 15, 2026 deployment (commit `b90f9ff`) completes the gap between declared 9-phase architecture and live pipeline execution:

- **Previously declared but unconfirmed:** LM Synthesizer Phase 3.5, psychology pre-assessment Phase 3, SteganographyDetection + TruthVerification + ContextAwareness in BBB Phase 1.4, 69-DGM cascade Phase 7, confidence decay multiplier Phase 5, `jarvis-local-resources-db` RAG retrieval.
- **Confirmed operational March 15:** All of the above, plus 22/22 LLM proxy HTTP 200 (up from 21/22), ChromaDB `chroma_data` volume restored, `jarvis-hippocampus` and `jarvis-toroidal-geometry` deployed.

There remain deliberate gaps between the broader architectural vision and this entrypoint's wiring. The `SERVICES` registry includes additional neurobiological and community-oriented modules (`qualia_engine`, `i_containers`, `neurobiological_master`, `autonomous_learner`) that are exercised in other workflows but not yet integrated into the `/chat` path. The automated POC verification loop for GBIM `needs_verification=TRUE` entities remains future work. This staged integration strategy allows the system to deliver robust, explainable responses while preserving room for future experiments in deeper neurobiological and community-governance coupling.

---

## 17.10 Summary

The executive coordination layer — realized by `jarvis-main-brain` at **127.0.0.1:8050** — provides a concrete and instrumented account of how a multi-layer cognitive architecture is orchestrated in practice across 79 operational containers. The confirmed execution sequences are:

**`/chat` (synchronous, full 9-phase pipeline — verified 349.87s, March 15, 2026):**
1. `UltimateRequest` (message, userid, role, useallservices) received at `/chat`
2. `prefrontal_planner` `ConsciousnessLayer` appended; `available_services` populated
3. `call_nbb_prefrontal` executed unconditionally → `nbb-i-containers` at **127.0.0.1:8101**
4. **Phase 1.4** — BBB 7-filter input stack → **0.0.0.0:8016** (EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection, SteganographyDetection, TruthVerification, ContextAwareness)
5. **Phase 2** — `call_truth_filter` → BBB **port 8016** `POST /truth` → `truthverdict` attached (advisory)
6. **Phase 3** — `jarvis-psychology-services` **port 8019** → `/psychological_assessment` severity classification
7. **Phase 4** — RAG context: `jarvis-spiritual-rag` **port 8005** queries PostgreSQL `msjarvis` (port 5433) + `gisdb` (port 5433) + `jarvis-local-resources-db` (port 5435) + ChromaDB (port 8000) + `psychological_rag_domain` (port 8006); web context: `jarvis-web-research` (internal Docker network, port 8008/tcp)
8. **Phase 3.5** — LM Synthesizer **port 8001** structures RAG context before ensemble
9. **Phase 2.5** — `llm20production` synthesis → semaphore proxy (port 8030) → `jarvis-20llm-production` **port 8008** (~120–145s, 22/22 models)
10. **Phase 7** — 69-DGM cascade **port 9000** (23 × 3 = 69 DGM operations, authoritative)
11. **Phase 4.5** — `apply_output_guards_async` → BBB **port 8016** `/filter` (8.0s timeout)
12. **Phase 5** — `confidence_decay` multiplier applied from GBIM temporal metadata
13. `normalize_identity` applied
14. `background_rag_store` scheduled → `ms_jarvis_memory` (append-only, dedup advisory)
15. `UltimateResponse` returned: `response`, `servicesused`, `consciousnesslevel`, `processingtime`, `architecturelayers`, `consciousnesslayers`, `truthverdict`, `confidence_decay_applied`

**`/chatlight/async` + `/chatlight/status/{job_id}` (async, lightweight consensus — verified March 2, 2026):**
1. `POST /chatlight/async` received → `job_id` + `poll_url` returned instantly
2. Background task acquires `chat_semaphore`; calls `discover_services()`
3. `build_egeria_prompt` constructs enhanced message
4. `httpx.Timeout(None, connect=5.0, read=None)` client → semaphore proxy (port 8030) → `jarvis-20llm-production` (port 8008, timeout 600.0 passed to semaphore)
5. 22-model ensemble completes (~120–145s); response extracted from `body["response"]`
6. `clean_response_for_display` → `apply_output_guards_async` (BBB, 8.0s timeout) → `normalize_identity`
7. Job marked `done`; `result` includes `answer`, `latency`, `mode: "light-async"`, `models_responded`
8. Client polls `GET /chatlight/status/{job_id}` → returns `status`, `elapsed`, `result`

By anchoring the high-level metaphors of prefrontal control, introspection, and consolidation in specific code paths, data structures, and performance measurements — grounded in three PostgreSQL databases (`msjarvis` port 5433: 5,416,521 GBIM entities, 80 epochs, 206 source layers; `gisdb` port 5433: 13 GB PostGIS, 993 ZCTA centroids; `jarvis-local-resources-db` port 5435: community resources) and confirmed at 349.87s end-to-end — this layer demonstrates that the thesis's coordination concepts are not only architecturally coherent but also implementable, measurable, and amenable to targeted optimization. For details on the 22-model ensemble and judge pipeline (0.975 consistency) invoked at Phase 2.5, see **Chapter 33**. For the 69-DGM cascade see **Chapter 32**. For the BBB 7-filter stack see **Chapter 16**. For the Neurobiological Master's own BBB → I-containers → Qualia → consciousness-bridge pipeline (a separate flow not in the primary `/chat` path) see **Chapter 12**. For GBIM temporal confidence decay and POC verification loop design see **Chapter 9**.
