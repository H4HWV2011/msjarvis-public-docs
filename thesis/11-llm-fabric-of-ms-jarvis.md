## Why this matters for Polymathmatic Geography

This chapter shows how Ms. Jarvis’s "thinking" is implemented as an organized fabric of local language models and services rather than a single opaque model instance. It supports:  
- **P1 – Every where is entangled** by embedding LLMs inside a retrieval, entanglement, and spatial stack (Chroma, GBIM, GeoDB, WV‑entangled RAG, autonomous learner collections) that keeps reasoning tied to concrete places, institutions, and learning histories.  
- **P3 – Power has a geometry** by routing questions through specific models, memories, and services whose connections—ports, proxies, ensembles, judges, and DGMs—have explicit topologies that can be inspected, tuned, or redesigned.  
- **P5 – Design is a geographic act** by treating model choice, ensemble wiring, timeout and backlog settings, and service topology as design decisions that change how Appalachian realities are seen, narrated, and optimized over time.  
- **P12 – Intelligence with a ZIP code** by grounding LLM calls in West Virginia–specific semantic and geospatial memory, including GBIM‑derived collections, WV‑entangled search, autonomous learner outputs, and I‑container identity, rather than generic, placeless prompts.  
- **P16 – Power accountable to place** by exposing LLMs only through glass‑box HTTP services with confirmed ports, logs, and timeouts, so that every path from user question to model output can be audited and constrained.

As such, this chapter belongs to the **Computational Instrument** tier: it specifies the model pool, timeouts, ports, and service fabric that turn Quantarithmia’s spatial‑justice instruments into live, language-facing behavior.

<img width="1100" height="900" alt="unnamed(16)"
  src="https://github.com/user-attachments/assets/ae0d8496-798d-4048-adbd-90d4fcc30b67" />

> **Figure 11.1.** The LLM fabric of Ms. Jarvis: user queries flow through RAG (including the updated `jarvis-rag-server` on port 8003), WV‑entangled and GIS gateways, autonomous learner and WOAH identity services, before reaching a pool of local models. All LLMs are exposed only via glass‑box HTTP services and are grounded in West Virginia–specific memory.

---

## Status as of February 2026

| Category | Details |
|---|---|
| **Implemented now** | `jarvis-main-brain` → **127.0.0.1:8050** (confirmed). `jarvis-ollama` → **127.0.0.1:11434** (confirmed). `jarvis-wv-entangled-gateway` → **127.0.0.1:8010** (confirmed). `jarvis-spiritual-rag` (GBIM / worldview RAG) → **127.0.0.1:8005** (confirmed; earlier plan documents used 8103). `jarvis-gis-rag` → **127.0.0.1:8004** (confirmed). `jarvis-rag-server` (general RAG) → **127.0.0.1:8003** (confirmed restored from placeholder; ONNX model downloaded and Chroma integration working). `nbb_woah_algorithms` → **127.0.0.1:8104** host → internal 8010 (confirmed). `jarvis-woah` → **127.0.0.1:7012** (confirmed). `jarvis-blood-brain-barrier` → **0.0.0.0:8016** (confirmed). `jarvis-20llm-production` → **127.0.0.1:8008** (confirmed). `jarvis-semaphore` (LLM proxy) → **127.0.0.1:8030** (confirmed). `llm1-proxy` through `llm22-proxy` → **127.0.0.1:8201–8222** (all confirmed). All 21 LLM proxy read timeouts set to **None** (unlimited) with connect timeout 3.0s, write timeout 5.0s, pool timeout 5.0s. `jarvis-20llm-production` backlog set to 2048 with keep‑alive 600s. Autonomous learner confirmed running as FastAPI service on **port 8425** with ONNX cache mount and calling `/next-learning-topic` on `jarvis-i-containers` (**port 8015**) to select WV knowledge‑gap topics. Judge services confirmed running: `jarvis-judge-truth` 7230, `jarvis-judge-consistency` 7231, `jarvis-judge-alignment` 7232, `jarvis-judge-ethics` 7233. `jarvis-constitutional-guardian` → **127.0.0.1:8091** (confirmed). `jarvis-fifth-dgm` → **127.0.0.1:4002** (confirmed). `jarvis-chroma` → **127.0.0.1:8002** (confirmed, serving 5 active collections including `autonomous_learner` and `conversation_history`). `jarvis-redis` → **127.0.0.1:6380** (confirmed). |
| **Partially implemented / scaffolded** | Per-request model breakdowns and per-model latency / error-rate metrics are logged but no dedicated debug HTTP endpoint exposes them yet. Ensemble decision rules are operational but not encoded in a machine‑readable schema. WOAH‑to‑model‑selection coupling exists conceptually but is not yet wired as an explicit routing rule in main‑brain config. Some service‑discovery calls (e.g., Redis-based) are best-effort with safe fallbacks. |
| **Future work / design intent only** | Richer debug and metrics endpoints for per-request agent breakdowns. Formal documentation and JSON schemas for ensemble decision rules and judge aggregation. Tighter coupling between WOAH weights, Fifth DGM proposals, entangled RAG traces, and model selection in high-stakes governance flows. Additional small, task-specific model pools registered behind the same fabric. Further optimization of cold‑start behavior and cache warmup strategies across the 21 LLM proxies. |

> **Port corrections and updates.** Earlier planning documents listed the Spiritual Root / GBIM RAG service at **8103** and implicitly conflated `jarvis-rag-server` with the WV‑entangled gateway on **8010**. The confirmed `docker compose ps` output shows `jarvis-spiritual-rag` running at **8005**, `jarvis-wv-entangled-gateway` at **8010**, and `jarvis-rag-server` at **8003**. All references in this chapter use these corrected ports.

---

# 11. The LLM Fabric of Ms. Jarvis

This chapter describes the local language models that form the "LLM fabric" of Ms. Egeria Jarvis and how they are woven into the broader GBIM, RAG, autonomous learning, and GeoDB architecture. Rather than treating LLMs as independent agents, the system treats them as constrained tools and judges embedded in a larger retrieval and belief stack that includes Chroma, Redis, the spatial body described in Chapter 6, entangled WV search (Chapter 8), and DGM‑style modules (Chapter 9), all exposed through well-defined HTTP services confirmed running as of February 26, 2026.

---

## 11.1 Current Local LLM Inventory

In the current deployment, a substantial set of base and specialist models is served by Ollama, running inside the `jarvis-ollama` container at **127.0.0.1:11434**. Figure 11.1 shows how these models are grouped and exposed collectively as the LLM fabric behind the Ollama runtime.

**Core general-purpose models.**  
`llama3:latest` and `llama3.1:latest` serve as primary general-purpose reasoning models for rich, multi-step questions where high-quality synthesis is important. `mistral:latest` is a fast, strong generalist for tightly scoped tasks where latency matters. `llama2:latest` remains available for compatibility and comparative benchmarking. Chat-oriented variants such as `vicuna:latest`, `openchat:latest`, `neural-chat:latest`, `starling-lm:latest`, `zephyr:latest`, `qwen2:latest`, `orca-mini:latest`, `dolphin-phi:latest`, `phi3:mini`, and `stablelm-zephyr:latest` provide diverse conversational styles and inductive biases.

**Code and data specialists.**  
`deepseek-coder:latest`, `codellama:latest`, `starcoder2:latest`, and `sqlcoder:latest` are tuned for code generation, refactoring, and SQL / data tasks and are used when workflows clearly involve code or database logic.

**Multimodal and vision models.**  
`llava:latest` and `minicpm-v:latest` are available for image- and vision-related tasks where enabled, allowing multimodal flows to remain within the same fabric.

**Domain-specific and compact models.**  
`medllama2:latest` covers medical- and clinical-style language and reasoning. Smaller models such as `tinyllama:latest`, `gemma:2b`, and `qwen2.5:1.5b` serve compact roles for constrained environments, quick utilities, and sanity checks.

All models are accessed via Ollama’s HTTP interface and are called from FastAPI services in `services/` (for example, `ai_server_20llm_PRODUCTION.py`, judge services, DGM modules), with model selection controlled through configuration and routing logic rather than hard-coded choices. Not all installed models are active in every workflow, but the fabric maintains this broader pool to support specialization, experimentation, and free-flow thinking across the 21‑mind ensemble.

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

The following port assignments are drawn from the confirmed February 26, 2026 deployment and supersede earlier planning drafts.

**Main Brain API — 127.0.0.1:8050 (`jarvis-main-brain`).**  
Primary external-facing interface for questions, RAG-backed answers, and multi-step flows. Orchestrates calls to all downstream services and assembles final responses.

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
Output guard and constitutional filter. All `ultimatechat` responses pass through BBB before returning to callers.

**20-LLM Production Ensemble — 127.0.0.1:8008 (`jarvis-20llm-production`).**  
Current production synthesis fabric. `llm20production` routes here as the default multi-model synthesis step. Uvicorn backlog configured to 2048 with keep-alive 600 seconds.

**Semaphore / LLM Proxy — 127.0.0.1:8030 (`jarvis-semaphore`).**  
Manages concurrent calls to the 21 LLM proxies with updated timeout configuration.

**LLM Proxies — 127.0.0.1:8201–8222 (`llm1-proxy` through `llm22-proxy`).**  
21 LLM proxy services confirmed running; all have `read=None` (unlimited), `connect=3.0` seconds, `write=5.0` seconds, and `pool=5.0` seconds, enabling free-flow thinking across all minds.

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
   With retrieval, entanglement, and identity context prepared, the main brain calls `jarvis-20llm-production` on port 8008. The 20‑LLM service fans out to all 21 proxies (8201–8222) under the updated timeout and backlog settings. 21/21 minds are confirmed responsive, with warm response times around 115 seconds and cold (model-load) times around 530 seconds.

5. **Judging and constitutional checks.**  
   Outputs are routed through the judge services (7230–7233) and the constitutional guardian (8091) as configured, then through the Blood‑Brain Barrier (8016) for final filtering.

6. **Response assembly and logging.**  
   The main brain assembles the final structured response, logs which services and models were invoked (including timing and error summaries), and returns a glass‑box answer to the caller.

Throughout this process, the LLM fabric is treated as a compositional engine over already-filtered inputs from Chroma, GeoDB, GBIM, entangled RAG, autonomous learner collections, and identity services.

---

## 11.5 LLMs in Consciousness, Autonomy, and Ensembles

**Consciousness and identity.**  
The Fifth DGM and I‑container services use LLM calls (via WOAH) to decide which content should shape Ms. Jarvis’s evolving identity narrative. Identity summaries and ego-layer entries can be fed back into prompts for core reasoning models, giving the fabric a sense of continuity across sessions.

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
All 21 LLM proxies have `read=None` to enable unconstrained generation when appropriate, but with stricter connection and pool timeouts to quickly detect unreachable services. The 20‑LLM production service uses an increased backlog and keep‑alive settings to handle concurrent high-latency calls.

**Logging and observability.**  
Logs capture which models and services are invoked for each request, their latencies, and error conditions. While there is not yet a dedicated user-facing debug endpoint that summarizes per-model contributions, the underlying traces exist and can be surfaced in future tooling.

**Failure modes and fallbacks.**  
If judge services are down, the main brain falls back to the 20‑LLM ensemble answer and marks consensus metrics as degraded. If a given proxy or backend service fails or times out, orchestration either retries, substitutes a backup model, or returns a structured error rather than silently failing.

The fabric is designed to behave more like a coordinated network of tools behind APIs than a single monolithic brain, even though these models collectively underpin Ms. Jarvis’s higher-level behavior.

---

## 11.7 Implementation Notes and Persistence

The following key implementation details guide how the LLM fabric should be described and maintained in code and compose files:

- **LLM proxy timeouts.** All 21 `llm{n}_health_proxy.py` files have been updated in the running containers to use `read=None` and shorter connect/write/pool timeouts. These changes must be persisted back to source to survive container rebuilds.  
- **20-LLM production server.** `ai_server_20llm_PRODUCTION.py` and the `jarvis-20llm-production` command in `docker-compose.yml` have been updated in running containers to use backlog 2048 and keep‑alive 600 seconds; source and compose definitions must be updated accordingly.  
- **Autonomous learner service.** `jarvis-autonomous-learner` now runs as a FastAPI service on port 8425 with ONNX cache mount and qualia-net integration. The thesis should treat the learner as an HTTP service rather than a pure daemon/job.  
- **New Chroma collections.** `conversation_history` and `autonomous_learner` collections are active, growing, and central to how the fabric learns from interactions and background study.  
- **Spiritual Root / GBIM RAG port.** All references to 8103 for this service should be updated to 8005.  
- **RAG server port and behavior.** `jarvis-rag-server` operates on port 8003 with corrected `/store` payload (`user_id`) and non-fatal Postgres insertion failures, guaranteeing Chroma writes even when episodic logging to Postgres fails.

These details ensure the chapter’s description of the LLM fabric remains aligned with the live system and provide a checklist for future deployments to keep intelligence grounded, entangled, and accountable to place.
