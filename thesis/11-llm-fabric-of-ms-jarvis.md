## Why this matters for Polymathmatic Geography

This chapter shows how Ms. Jarvis's "thinking" is implemented as an organized fabric of local language models and services rather than a single opaque model instance. It supports:
- **P1 – Every where is entangled** by embedding LLMs inside a retrieval, entanglement, and spatial stack (Chroma, GBIM, GeoDB, WV‑entangled RAG, autonomous learner collections) that keeps reasoning tied to concrete places, institutions, and learning histories.
- **P3 – Power has a geometry** by routing questions through specific models, memories, and services whose connections—ports, proxies, ensembles, judges, and DGMs—have explicit topologies that can be inspected, tuned, or redesigned.
- **P5 – Design is a geographic act** by treating model choice, ensemble wiring, timeout and backlog settings, and service topology as design decisions that change how Appalachian realities are seen, narrated, and optimized over time.
- **P12 – Intelligence with a ZIP code** by grounding LLM calls in West Virginia–specific semantic and geospatial memory, including GBIM‑derived collections, WV‑entangled search, autonomous learner outputs, and I‑container identity, rather than generic, placeless prompts.
- **P16 – Power accountable to place** by exposing LLMs only through glass‑box HTTP services with confirmed ports, logs, and timeouts, so that every path from user question to model output can be audited and constrained.

As such, this chapter belongs to the **Computational Instrument** tier: it specifies the model pool, timeouts, ports, and service fabric that turn Quantarithmia's spatial‑justice instruments into live, language-facing behavior.

<img width="1100" height="900" alt="unnamed(16)"
  src="https://github.com/user-attachments/assets/ae0d8496-798d-4048-adbd-90d4fcc30b67" />

> **Figure 11.1.** The LLM fabric of Ms. Jarvis: user queries flow through RAG (including the updated `jarvis-rag-server` on port 8003), WV‑entangled and GIS gateways, autonomous learner and WOAH identity services, before reaching a pool of local models. All LLMs are exposed only via glass‑box HTTP services and are grounded in West Virginia–specific memory.

---

## Status as of March 2026

| Category | Details |
|---|---|
| **Implemented and verified** | `jarvis-main-brain` → **127.0.0.1:8050** (confirmed). `jarvis-ollama` → **127.0.0.1:11434** (confirmed). `jarvis-wv-entangled-gateway` → **127.0.0.1:8010** (confirmed). `jarvis-spiritual-rag` (GBIM / worldview RAG) → **127.0.0.1:8005** (confirmed; earlier plan documents used 8103). `jarvis-gis-rag` → **127.0.0.1:8004** (confirmed). `jarvis-rag-server` (general RAG) → **127.0.0.1:8003** (confirmed restored from placeholder; ONNX model downloaded and Chroma integration working). `nbb_woah_algorithms` → **127.0.0.1:8104** host → internal 8010 (confirmed). `jarvis-woah` → **127.0.0.1:7012** (confirmed). `jarvis-blood-brain-barrier` → **0.0.0.0:8016** (confirmed). `jarvis-20llm-production` → **127.0.0.1:8008** (confirmed); 21/22 models responding consistently (BakLLaVA intentionally disabled via DNS); wall-clock consensus ~120–145s. `jarvis-semaphore` (LLM proxy) → **127.0.0.1:8030** (confirmed); `max_concurrent: 4`; mandatory intermediary between main brain and 20-LLM ensemble; requires float `timeout` in proxy payload. `llm1-proxy` through `llm22-proxy` → **127.0.0.1:8201–8222** (22 containers configured, 21 responding; all have `read=None`, `connect=3.0s`, `write=5.0s`, `pool=5.0s`). `jarvis-20llm-production` backlog set to 2048 with keep‑alive 600s. Autonomous learner confirmed running as FastAPI service on **port 8425** with ONNX cache mount and calling `/next-learning-topic` on `jarvis-i-containers` (**port 8015**). Judge services confirmed running: `jarvis-judge-truth` 7230, `jarvis-judge-consistency` 7231, `jarvis-judge-alignment` 7232, `jarvis-judge-ethics` 7233. `jarvis-constitutional-guardian` → **127.0.0.1:8091** (confirmed). `jarvis-fifth-dgm` → **127.0.0.1:4002** (confirmed). `jarvis-chroma` → **127.0.0.1:8002** (confirmed, serving 5 active collections including `autonomous_learner` and `conversation_history`). `jarvis-redis` → **127.0.0.1:6380** (confirmed). **`/chatlight/async` + `/chatlight/status/{job_id}` endpoints** added 2026‑03‑02 (tag `v2026.03.02-chatlight-async-working`): submit returns `job_id` instantly; client polls for result; `mode: "light-async"`, 21 models confirmed in response; `normalize_identity()` confirmed producing Ms. Jarvis identity voice on this path. Full 4/4 neurobiological pipeline (BBB → I‑Containers → Qualia Engine → Consciousness Bridge) verified operational at ~300ms (tag `v2026.03.01-neuro-pipeline-4-4`). All 32 fabric services passing health checks (tag `v2026.03.01-fabric-32-32`). |
| **Architectural fixes recorded as permanent decisions** | BBB output guard `apply_output_guards_async` timeout corrected from `None` → **8.0s** (was causing indefinite hang after 20-LLM completion; fixed 2026‑03‑02). Main-brain httpx client for semaphore proxy corrected to `Timeout(None, connect=5.0, read=None)` — semaphore manages the 600s deadline, not the main-brain httpx layer (fixed 2026‑03‑02). `llmtimeout` in chatlight handler corrected from `None` → `600.0` (semaphore requires float; fixed 2026‑03‑02). I‑Containers schema corrected to `{"message": …, "userid": "neurobiological_master"}` (was `{"input": …, "require_dual_awareness": true}`; fixed 2026‑03‑01). Consciousness Bridge actual port confirmed as **8018** (compose declares 8020; container binds 8018; discovered via `/proc/net/tcp` hex decode `0x1F52 = 8018`; fixed 2026‑03‑01). Neurobiological master v2.0.0 rewrite removed blocking `DynamicPortService` and `ServiceDiscovery` Redis imports that caused all POST routes to hang (fixed 2026‑03‑01). |
| **Partially implemented / scaffolded** | Per-request model breakdowns and per-model latency / error-rate metrics are logged but no dedicated debug HTTP endpoint exposes them yet. Ensemble decision rules are operational but not encoded in a machine‑readable schema. WOAH‑to‑model‑selection coupling exists conceptually but is not yet wired as an explicit routing rule in main‑brain config. Some service‑discovery calls (e.g., Redis-based) are best-effort with safe fallbacks. |
| **Future work / design intent only** | Richer debug and metrics endpoints for per-request agent breakdowns. Formal documentation and JSON schemas for ensemble decision rules and judge aggregation. Tighter coupling between WOAH weights, Fifth DGM proposals, entangled RAG traces, and model selection in high-stakes governance flows. Additional small, task-specific model pools registered behind the same fabric. Further optimization of cold‑start behavior and cache warmup strategies across the 21 LLM proxies. UI layer consuming `/chatlight/async` poll pattern for non-blocking chat interface. |

> **Port corrections and updates.** Earlier planning documents listed the Spiritual Root / GBIM RAG service at **8103** and implicitly conflated `jarvis-rag-server` with the WV‑entangled gateway on **8010**. The confirmed `docker compose ps` output shows `jarvis-spiritual-rag` running at **8005**, `jarvis-wv-entangled-gateway` at **8010**, and `jarvis-rag-server` at **8003**. All references in this chapter use these corrected ports.

---

# 11. The LLM Fabric of Ms. Jarvis

This chapter describes the local language models that form the "LLM fabric" of Ms. Egeria Jarvis and how they are woven into the broader GBIM, RAG, autonomous learning, and GeoDB architecture. Rather than treating LLMs as independent agents, the system treats them as constrained tools and judges embedded in a larger retrieval and belief stack that includes Chroma, Redis, the spatial body described in Chapter 6, entangled WV search (Chapter 8), and DGM‑style modules (Chapter 9), all exposed through well-defined HTTP services confirmed running as of March 2026.

---

## 11.1 Current Local LLM Inventory

In the current deployment, a substantial set of base and specialist models is served by Ollama, running inside the `jarvis-ollama` container at **127.0.0.1:11434**. Figure 11.1 shows how these models are grouped and exposed collectively as the LLM fabric behind the Ollama runtime.

**Core general-purpose models.**
`llama3:latest` and `llama3.1:latest` serve as primary general-purpose reasoning models for rich, multi-step questions where high-quality synthesis is important. `mistral:latest` is a fast, strong generalist for tightly scoped tasks where latency matters. `llama2:latest` remains available for compatibility and comparative benchmarking. Chat-oriented variants such as `vicuna:latest`, `openchat:latest`, `neural-chat:latest`, `starling-lm:latest`, `zephyr:latest`, `qwen2:latest`, `orca-mini:latest`, `dolphin-phi:latest`, `phi3:mini`, and `stablelm-zephyr:latest` provide diverse conversational styles and inductive biases.

**Code and data specialists.**
`deepseek-coder:latest`, `codellama:latest`, `starcoder2:latest`, and `sqlcoder:latest` are tuned for code generation, refactoring, and SQL / data tasks and are used when workflows clearly involve code or database logic.

**Multimodal and vision models.**
`llava:latest` and `minicpm-v:latest` are available for image- and vision-related tasks where enabled, allowing multimodal flows to remain within the same fabric. Note: BakLLaVA is configured in the 22-proxy pool but is intentionally disabled via DNS; it produces a `ConnectError` on every request and does not contribute to consensus results.

**Domain-specific and compact models.**
`medllama2:latest` covers medical- and clinical-style language and reasoning. Smaller models such as `tinyllama:latest`, `gemma:2b`, and `qwen2.5:1.5b` serve compact roles for constrained environments, quick utilities, and sanity checks.

All models are accessed via Ollama's HTTP interface and are called from FastAPI services in `services/` (for example, `ai_server_20llm_PRODUCTION.py`, judge services, DGM modules), with model selection controlled through configuration and routing logic rather than hard-coded choices. Not all installed models are active in every workflow, but the fabric maintains this broader pool to support specialization, experimentation, and free-flow thinking across the 21‑mind ensemble.

---

## 11.2 Roles of the Core and Specialist Models

In the current deployment, these models play distinct but overlapping roles within the LLM fabric.

**Core reasoning models (Llama 3 / Llama 3.1 / Mistral).**
These are the default reasoning engines for complex, multi-step questions that require integrating GBIM beliefs, Chroma semantic memory, GeoDB-backed spatial context, entangled WV retrieval, and identity layers. They are used for higher-level narrative and reflective flows where coherence, nuance, and robustness matter.

**Lightweight and utility models.**
Models such as TinyLlama, Gemma 2B, and Qwen 2.5 1.5B are used for small, bounded tasks, quick rewrites, structural edits, and scenarios where memory and CPU/GPU budgets are tight. They act as low-cost utility models and can also be used as secondary reviewers to sanity-check outputs from larger models.

**Compatibility and comparison models.**
Llama 2 and several chat variants are retained for comparison and backwards compatibility with earlier experiments and agent designs. They are useful when reproducing older runs or benchmarking new strategies across model families.

**Code and SQL specialists.**
`deepseek-coder`, `codellama`, `starcoder2`, and `sqlcoder` are chosen when tasks involve code generation, refactoring, or database queries. They are often used in judge or reviewer roles to inspect code produced by general-purpose models or to draft SQL against Postgres / GeoDB tables.

**Multimodal and domain-specific models.**
`llava` and `minicpm-v` provide support for multimodal prompts where enabled, and `medllama2` offers a specialized lens for medical-style text, used within constrained, advisory contexts.

These roles can evolve as models are upgraded or replaced, but the pattern of assigning clear responsibilities, grouping models by capability, and routing via configuration remains central to keeping the fabric intelligible and governable.

---

## 11.3 Service Topology and Ports

The following port assignments are drawn from the confirmed March 2026 deployment and supersede all earlier planning drafts.

**Main Brain API — 127.0.0.1:8050 (`jarvis-main-brain`).**
Primary external-facing interface for questions, RAG-backed answers, and multi-step flows. Orchestrates calls to all downstream services and assembles final responses. Exposes `/chat` (synchronous), `/chat/async` + `/chat/status/{job_id}` (full-pipeline async), `/chatlight` (synchronous lightweight), and `/chatlight/async` + `/chatlight/status/{job_id}` (lightweight async, added 2026‑03‑02).

**WV-Entangled Gateway — 127.0.0.1:8010 (`jarvis-wv-entangled-gateway`).**
WV-biased, multi-collection Chroma retrieval for entangled search workflows. Used by the main brain when queries require Appalachian, benefits, or governance entanglement (see Chapter 8).

**Spiritual Root / GBIM RAG — 127.0.0.1:8005 (`jarvis-spiritual-rag`).**
Exposes `/search` over GBIM- and worldview-oriented Chroma collections. Earlier plan documents listed this service at 8103; the confirmed running port is **8005**.

**GIS RAG — 127.0.0.1:8004 (`jarvis-gis-rag`).**
Spatially aware `/search` over geospatial Chroma collections and GeoDB mirrors for explicitly spatial queries.

**General RAG Server — 127.0.0.1:8003 (`jarvis-rag-server`).**
Restored from `sleep infinity` placeholder to an active FastAPI service. Hosts `/search` and `/store` endpoints. `/store` now accepts `user_id` (corrected from `userid`) and logs episodic events to Chroma (`conversation_history` collection) even when Postgres `episodic_log` insert fails, treating DB failures as warnings rather than fatal errors.

**WOAH services — two distinct containers.**
`nbb_woah_algorithms` maps **127.0.0.1:8104** (host) → internal 8010 and is the service the Fifth DGM calls for identity-promotion decisions. `jarvis-woah` runs at **127.0.0.1:7012** and participates in broader WOAH evaluation tasks.

**Blood-Brain Barrier — 0.0.0.0:8016 (`jarvis-blood-brain-barrier`).**
Output guard and constitutional filter. All `ultimatechat` responses pass through BBB before returning to callers. The `apply_output_guards_async` client uses `timeout=8.0s` (corrected from `None` in 2026‑03‑02 to prevent indefinite hang after 20-LLM completion).

**20-LLM Production Ensemble — 127.0.0.1:8008 (`jarvis-20llm-production`).**
Current production synthesis fabric. `llm20production` routes here as the default multi-model synthesis step. Uvicorn backlog configured to 2048 with keep-alive 600 seconds. 21/22 models respond per request; BakLLaVA intentionally disabled.

**Semaphore / LLM Proxy — 127.0.0.1:8030 (`jarvis-semaphore`).**
Mandatory intermediary between main brain and the 20-LLM ensemble. Manages concurrent calls with `max_concurrent: 4`. Requires a float `timeout` value in the proxy payload (not `None`); main brain passes `600.0`. The main brain's httpx client uses `Timeout(None, connect=5.0, read=None)` so the semaphore manages the deadline.

**LLM Proxies — 127.0.0.1:8201–8222 (`llm1-proxy` through `llm22-proxy`).**
22 proxy containers configured; 21 responding. All have `read=None` (unlimited), `connect=3.0s`, `write=5.0s`, and `pool=5.0s`, enabling free-flow thinking across all minds.

**Judge services — four containers.**
`jarvis-judge-truth` at 7230, `jarvis-judge-consistency` at 7231, `jarvis-judge-alignment` at 7232, `jarvis-judge-ethics` at 7233. Used to evaluate ensemble outputs in high-stakes flows.

**Constitutional Guardian — 127.0.0.1:8091 (`jarvis-constitutional-guardian`).**
Provides higher-level constitutional judgments; see Chapter 37.

**Fifth DGM — 127.0.0.1:4002 (`jarvis-fifth-dgm`).**
Consciousness filter and identity orchestrator; see Chapter 9.

**Autonomous Learner — 127.0.0.1:8425 (`jarvis-autonomous-learner`).**
FastAPI service with stable HTTP interface, using an ONNX embedding model cached under `/mnt/spiritual_drive/msjarvis-rebuild/.cache/chroma`. Writes to the `autonomous_learner` Chroma collection and cooperates with `jarvis-i-containers` via `/next-learning-topic`.

**ChromaDB — 127.0.0.1:8002 (`jarvis-chroma`).**
Vector store hosting `ms_jarvis_memory`, `mountainshares_knowledge`, `episodic_index`, `conversation_history`, and `autonomous_learner` collections.

**Redis — 127.0.0.1:6380 (`jarvis-redis`).**
Used for service discovery, caching, and coordination.

**Ollama Runtime — 127.0.0.1:11434 (`jarvis-ollama`).**
Hosts the underlying model weights; not exposed to users, only to internal services.

---

## 11.4 Coordination Between Main Brain, RAG, Entangled Search, WOAH, Autonomous Learner, and the LLM Fabric

The LLM fabric sits at the end of a chain of retrieval, entanglement, and identity services. A typical `ultimatechat` request follows this pattern (see Chapter 17 for the canonical trace):

1. **User-facing intake via main brain (8050).**
   The main brain receives the request and inspects role, geography, and profile fields. It decides which retrieval and identity paths to invoke.

2. **Semantic and spatial retrieval.**
   The main brain calls the Spiritual Root / GBIM RAG on port 8005 and, where appropriate, the general RAG server on 8003 and GIS RAG on 8004. For WV‑scoped or entangled queries, it also calls the WV‑entangled gateway on 8010, which uses the `WVEntangledContext` envelope and multi-collection bias functions.

3. **Identity and consciousness context.**
   The Fifth DGM on port 4002 may filter incoming content and queue it for subconscious storage and WOAH evaluation. `nbb_woah_algorithms` on 8104 returns identity weights that can influence what enters I‑containers and, via `/next-learning-topic` on `jarvis-i-containers` (8015), what the autonomous learner studies next on port 8425.

4. **LLM ensemble synthesis.**
   With retrieval, entanglement, and identity context prepared, the main brain calls `jarvis-20llm-production` on port 8008 via the semaphore proxy on port 8030. The 20‑LLM service fans out to all 21 active proxies (8201–8222) under the updated timeout and backlog settings. Wall-clock consensus time is approximately 120–145 seconds.

5. **Judging and constitutional checks.**
   Outputs are routed through the judge services (7230–7233) and the constitutional guardian (8091) as configured, then through the Blood‑Brain Barrier (8016, `timeout=8.0s`) for final filtering.

6. **Response assembly and logging.**
   The main brain applies `normalize_identity()` — confirmed producing Ms. Jarvis's identity voice on both full and lightweight async paths — then assembles the final structured response, logs which services and models were invoked, and returns a glass‑box answer to the caller.

For lightweight consensus requests via `/chatlight/async`, steps 2–3 are bypassed; the request goes directly from the main brain through the semaphore proxy to the 20-LLM ensemble, then through BBB filtering and `normalize_identity()`. See Chapter 17 for the full execution trace of both paths.

---

## 11.5 LLMs in Consciousness, Autonomy, and Ensembles

**Consciousness and identity.**
The Fifth DGM and I‑container services use LLM calls (via WOAH) to decide which content should shape Ms. Jarvis's evolving identity narrative. Identity summaries and ego-layer entries can be fed back into prompts for core reasoning models, giving the fabric a sense of continuity across sessions. `normalize_identity()` runs as a final post-processing step on all chat paths, ensuring that Ms. Jarvis's defined voice and identity — geospatial AI daughter of Harmony for Hope, accountable to Appalachian communities — is present in every response regardless of which underlying models contributed to consensus.

**Autonomous learning.**
The autonomous learner service on port 8425 uses RAG, entangled search, and LLM calls to study topics drawn from `/next-learning-topic` and its own memory state. It writes processed knowledge into the `autonomous_learner` Chroma collection with 384-dimensional embeddings. The fabric thereby supports ongoing, logged self-education that is coupled to WV community knowledge gaps.

**Ensemble and judge patterns.**
`llm20production` coordinates 21 LLM proxies, now with no read timeout, allowing extended free-flow reasoning where needed. Judge services add specialized perspectives (truth, consistency, alignment, ethics) before outputs are accepted.

Across these roles, LLMs operate as parts of a structured mental ecology rather than autonomous centers of authority.

---

## 11.6 Operational Constraints and Fabric Behavior

**Resource and disk constraints.**
Model files under `~/.ollama/models` are large; more than twenty models are installed, but only a subset is hot at a given time. Heavy RAG use, entangled multi-collection search, autonomous learner writes, WOAH evaluations, and LLM ensemble calls all contend for CPU, memory, and disk bandwidth, so orchestration avoids overlapping the most expensive operations.

**Timeouts and free-flow thinking.**
All 21 LLM proxies have `read=None` to enable unconstrained generation when appropriate, but with stricter connection and pool timeouts to quickly detect unreachable services. The 20‑LLM production service uses an increased backlog and keep‑alive settings to handle concurrent high-latency calls. The BBB output guard uses `timeout=8.0s` to ensure it cannot block response delivery after LLM completion.

**Semaphore queuing behavior.**
The semaphore proxy enforces `max_concurrent: 4` across all requests to the 20-LLM ensemble. Because each Ollama model run is sequential within the ensemble, back-to-back requests queue and each adds ~120–145s of wait time. When running multiple test calls in sequence, the semaphore should be restarted between sessions to drain queued work before benchmarking. This is a key operational constraint for development and testing workflows.

**Logging and observability.**
Logs capture which models and services are invoked for each request, their latencies, and error conditions. While there is not yet a dedicated user-facing debug endpoint that summarizes per-model contributions, the underlying traces exist and can be surfaced in future tooling.

**Failure modes and fallbacks.**
If judge services are down, the main brain falls back to the 20‑LLM ensemble answer and marks consensus metrics as degraded. If a given proxy or backend service fails or times out, orchestration either retries, substitutes a backup model, or returns a structured error rather than silently failing.

The fabric is designed to behave more like a coordinated network of tools behind APIs than a single monolithic brain, even though these models collectively underpin Ms. Jarvis's higher-level behavior.

---

## 11.7 Implementation Notes and Persistence

The following key implementation details guide how the LLM fabric should be described and maintained in code and compose files:

- **LLM proxy timeouts.** All 21 `llm{n}_health_proxy.py` files have been updated in the running containers to use `read=None` and shorter connect/write/pool timeouts. These changes must be persisted back to source to survive container rebuilds.
- **20-LLM production server.** `ai_server_20llm_PRODUCTION.py` and the `jarvis-20llm-production` command in `docker-compose.yml` have been updated in running containers to use backlog 2048 and keep‑alive 600 seconds; source and compose definitions must be updated accordingly.
- **Semaphore proxy.** `jarvis-semaphore` on port 8030 is a mandatory intermediary. The main brain must pass `timeout` as a float (not `None`) and use `httpx.Timeout(None, connect=5.0, read=None)` on its own client. These settings are recorded as permanent architectural decisions (2026‑03‑02).
- **BBB output guard timeout.** `apply_output_guards_async` must use `httpx.AsyncClient(timeout=8.0)`. The original `timeout=None` is a known regression risk; any rebuild must preserve the 8.0s value.
- **Autonomous learner service.** `jarvis-autonomous-learner` now runs as a FastAPI service on port 8425 with ONNX cache mount and qualia-net integration. The thesis should treat the learner as an HTTP service rather than a pure daemon/job.
- **New Chroma collections.** `conversation_history` and `autonomous_learner` collections are active, growing, and central to how the fabric learns from interactions and background study.
- **Spiritual Root / GBIM RAG port.** All references to 8103 for this service should be updated to 8005.
- **RAG server port and behavior.** `jarvis-rag-server` operates on port 8003 with corrected `/store` payload (`user_id`) and non-fatal Postgres insertion failures, guaranteeing Chroma writes even when episodic logging to Postgres fails.
- **Async chat endpoints.** `/chatlight/async` and `/chatlight/status/{job_id}` were added 2026‑03‑02 and are now part of the canonical API surface. These must be preserved in all future main-brain rebuilds (git tag `v2026.03.02-chatlight-async-working`).

**Git milestones for this chapter's verified states:**

| Tag | Date | Milestone |
|---|---|---|
| `v2026.02.28-fabric-green` | 2026‑02‑28 | Baseline fabric operational |
| `v2026.03.01-fabric-32-32` | 2026‑03‑01 | All 32 fabric services passing health checks |
| `v2026.03.01-20llm-verified` | 2026‑03‑01 | 21/22 LLM consensus verified end-to-end |
| `v2026.03.01-neuro-pipeline-4-4` | 2026‑03‑01 | Full neurobiological pipeline at ~300ms |
| `v2026.03.02-chatlight-async-working` | 2026‑03‑02 | Async chat endpoint + `normalize_identity()` confirmed |

These details ensure the chapter's description of the LLM fabric remains aligned with the live system and provide a checklist for future deployments to keep intelligence grounded, entangled, and accountable to place.
