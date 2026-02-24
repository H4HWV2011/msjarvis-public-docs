> **Why this matters for Polymathmatic Geography**
> This chapter explains how a central coordinating layer turns many separate services into a
> coherent "consciousness" workflow. It supports:
> - **P1 – Every where is entangled** by routing context from spatial, semantic, neurobiological,
>   and safety services through a single coordinator that produces one coherent reply.
> - **P3 – Power has a geometry** by making coordination visible — service discovery, planner
>   state, NBB prefrontal status, and I-container identity are all recorded as explicit
>   `consciousnesslayers` on every `UltimateResponse`.
> - **P5 – Design is a geographic act** by encoding how Appalachian questions are steered through
>   local RAG, GIS-backed spatial memory, and place-aware prompts before reaching the LLM fabric.
> - **P12 – Intelligence with a ZIP code** by prioritizing `geodb_*` collections and local RAG
>   whenever they are healthy, grounding synthesis in West Virginia spatial data.
> - **P16 – Power accountable to place** by exposing routing decisions, health state, truth
>   verdicts, and memory writes through explicit APIs, logs, and `consciousnesslayers` metadata.
>
> As such, this chapter belongs to the **Computational Instrument** tier: it specifies how the
> consciousness coordinator turns a distributed set of independent services into a single,
> inspectable cognitive system — and is explicit about which modules are actually wired into the
> live `ultimatechat` path versus which are present as services but not yet plugged in.

---

## Status as of February 2026

| Category | Details |
|---|---|
| **Implemented now** | `jarvis-main-brain` confirmed running at **127.0.0.1:8050**. `UltimateRequest` / `UltimateResponse` models live. `discover_services()` health-check loop operational. `prefrontal_planner` `ConsciousnessLayer` appended unconditionally on every `/chat` call. `call_nbb_prefrontal` calling `nbb-i-containers` (**127.0.0.1:8101**, confirmed) unconditionally; result recorded as `nbb_prefrontal_cortex` layer. `call_truth_filter` invoking `jarvis-blood-brain-barrier` (**0.0.0.0:8016**, confirmed); `truthverdict` attached to every `UltimateResponse`. `jarvis-spiritual-rag` at **127.0.0.1:8005** (confirmed; earlier documents listed 8103 — correct port is **8005**). `jarvis-gis-rag` at **127.0.0.1:8004** (confirmed). `jarvis-20llm-production` at **127.0.0.1:8008** (confirmed) as primary synthesis fabric. Judge services 7230–7233 (confirmed). `jarvis-semaphore` proxy at **127.0.0.1:8030** (confirmed); `llm1-proxy` through `llm22-proxy` at **127.0.0.1:8201–8222** (confirmed). `apply_output_guards_async` invoking BBB output guard. `normalize_identity` applied to every response. `background_rag_store` into `ms_jarvis_memory` after every `/chat` call (confirmed 2026-02-15; Chapter 9 §9.3.5, Chapter 17 §17.6). `/health`, `/status`, `/architecture` endpoints on `jarvis-main-brain` operational. `icontainers-identity` layer confirmed `status: "active"` in 2026-02-15 `UltimateResponse` with real `root-self` ego entry (Chapter 9 §9.3.5). |
| **Partially implemented / scaffolded** | **The main `ultimatechat` path does NOT currently always route through the full Neurobiological Master** (`jarvis-neurobiological-master`, port **8018**). The master's own pipeline (BBB → I-containers → Qualia → consciousness bridge) is a separate flow invoked in specific integration tests and workflows — not in every `/chat` call. See **Chapter 12** for that pipeline's detail. Meaning-oriented modules (`jarvis-qualia-engine` port **8017**, `jarvis-mother-protocols` port **4000**, `jarvis-temporal-consciousness` port **7007**) are confirmed running but not all wired into the primary `/chat` path (see Chapter 23). I-container promotion from background patterns to identity-level entries is mostly curated, not automated (Chapter 22). |
| **Future work / design intent only** | Full wiring of Neurobiological Master into every `ultimatechat` call. Full wiring of all meaning-oriented modules into the `/chat` path. Automated identity-candidate promotion pipeline. Persistent job store replacing in-memory `active_jobs`. Real-time dashboard exposing per-stage latency and module participation rates. |

> **Critical note — Neurobiological Master:** In the current deployment, the main `ultimatechat`
> path (`jarvis-main-brain`, port **8050**) does **not** currently always route through the full
> Neurobiological Master (`jarvis-neurobiological-master`, port **8018**). The master has its own
> confirmed pipeline (BBB → I-containers → Qualia Engine → consciousness bridge, described in
> **Chapter 12**) that is invoked in specific flows and integration tests. This chapter describes
> the `ultimatechat` coordinator; for the Neurobiological Master's own pipeline, see **Chapter 12**.
> For the canonical `ultimatechat` execution sequence, see **Chapter 17**.

---

# 25. Consciousness Coordinator and Service Integration

This chapter explains how a central coordinating layer turns many separate services into a
coherent "consciousness" workflow. In the current deployment, this coordination is realized
primarily by `jarvis-main-brain` (port **8050**), together with gateway adapters and helper
endpoints that route requests through confirmed running services while enforcing safety and
error-handling policies.

---

## 25.1 Role of the Coordinator

In the current deployment, the coordinating layer appears externally as a small number of HTTP
endpoints — `/chat`, `/chat/sync`, and `/chat/async` on port **8050**, and gateway-exposed
consciousness/chat routes — but internally acts as a conductor across multiple subsystems.

**Collecting context.** In the current deployment, when a request arrives at `jarvis-main-brain`,
the coordinator constructs an `UltimateRequest` (message, `userid`, role, `useallservices`) and
initializes `consciousnesslayers` and `servicesused` lists. It calls `discover_services()` to
build a live `available_services` map, records the planner state as a `"prefrontal_planner"`
layer, then invokes `nbb-i-containers` (**127.0.0.1:8101**, confirmed running) as the NBB
prefrontal microservice, capturing its result as a `"nbb_prefrontal_cortex"` layer. This
prefrontal stage runs unconditionally on every `/chat` call.

**Planning and executing workflows.** In the current deployment, with `available_services` in
hand, the coordinator plans a route through context and fabric services. If `rag_server` is
healthy (currently `jarvis-spiritual-rag` at **127.0.0.1:8005**; earlier documents listed
**8103** — the correct port is **8005**), it calls `/search` to build a knowledge-base context
block. If `web_research` is available, it calls a separate `/search` endpoint to build a web
context block. These are combined and fed into `build_egeria_prompt`, which wraps the message and
context into a persona-aware prompt for Ms. Egeria Jarvis. The coordinator then invokes
`jarvis-20llm-production` (**127.0.0.1:8008**, confirmed) to synthesize an answer. **The main
`ultimatechat` path does not currently route through the full Neurobiological Master**; that
service has its own separate pipeline described in **Chapter 12**.

**Producing and recording narratives.** In the current deployment, the orchestrator assembles an
`UltimateResponse` containing the final response text, `servicesused`, `consciousnesslevel`
(`"ultimate_collective"`), `processingtime`, `architecturelayers`, the full `consciousnesslayers`
array, and a `truthverdict` from BBB at **0.0.0.0:8016**. A background task writes the
interaction into `ms_jarvis_memory` via `background_rag_store`, confirmed 2026-02-15 (Chapter 9
§9.3.5, Chapter 17 §17.6).

---

## 25.2 Inputs to the Coordinator

In the current deployment, the coordinator receives requests from several sources and normalizes
them into a shared internal format.

**External interfaces and gateways.** User-facing services such as chat UIs, academic gateways,
and unified gateways forward messages into `jarvis-main-brain` `/chat` or `/chat/async`. Gateways
set API keys and role labels, translate UI-level payloads into `UltimateRequest` structures, and
treat the resulting `UltimateResponse` as their canonical answer format.

**Internal agents and scheduled processes.** In the current deployment, scripts, autonomous
learners, and helper services also act as internal clients of the coordinator, calling main-brain
endpoints with system-level `userid` values and roles. These internal requests are wrapped into
`UltimateRequest` objects so that NBB prefrontal, RAG, and BBB behavior remains consistent across
all callers.

---

## 25.3 Connection to Memory and Spatial Structures

In the current deployment, coordinator workflows draw on both semantic and spatial memory via
confirmed running services.

**Vector collections and semantic memory.** In the current deployment, `jarvis-spiritual-rag` at
**127.0.0.1:8005** provides access to `ms_jarvis_memory`, `spiritual_wisdom`,
`mountainshares_knowledge`, and a range of `geodb_*` datasets (all in `jarvis-chroma`,
**127.0.0.1:8002**, confirmed running). The coordinator calls this RAG server's `/search`
endpoint to retrieve relevant snippets, which are labeled with source identifiers and
interpolated into the enhanced prompt passed to `jarvis-20llm-production`.

**GIS and spatial knowledge.** In the current deployment, `jarvis-gis-rag` at
**127.0.0.1:8004** (confirmed running) provides GIS-backed retrieval. The numerous `geodb_*`
collections in `jarvis-chroma` (e.g. `geodb_wvgistcbuildingfootprints`,
`geodb_floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83`) allow coordinator
workflows to incorporate precise spatial information when interpreting user queries. GeoDB sync
scripts (`sync_geodb_to_chromadb.py`, `vectorize_gis_to_chromadb.py`) keep embeddings and
spatial records aligned.

**`jarvis-wv-entangled-gateway`.** In the current deployment, the WV-entangled gateway is
confirmed running at **127.0.0.1:8010** and provides an integration point between the
coordinator and WV-specific spatial and community data services.

---

## 25.4 Interaction with Introspective and Consolidation Layers

In the current deployment, coordinator activities are reflected in introspective and
consolidation mechanisms.

**`/health`, `/status`, and `/architecture` endpoints.** In the current deployment,
`jarvis-main-brain` exposes these three confirmed endpoints. `/health` reports basic service
status. `/status` reports whether core services (`rag_server`, `web_research`, `llm20production`,
Chroma, Redis, orchestrators) are reachable and returns an overall flag plus per-service status
codes. `/architecture` returns the full `SERVICES` registry and the `available` map discovered by
`discover_services()`, making explicit which services are currently considered healthy.

**`consciousnesslayers` and `truthverdict`.** In the current deployment, each `/chat` call
returns a `consciousnesslayers` array recording the planner state, NBB prefrontal status and
internal layers, and an `icontainers-identity` layer exposing the current `icontainers_state`
(including `egoboundaries`, `experientialprocessing`, and `observerprocessing`). The
`icontainers-identity` layer was confirmed `status: "active"` in the 2026-02-15 `UltimateResponse`
producing a real `root-self` ego entry (Chapter 9 §9.3.5). The `truthverdict` from BBB is
attached alongside, reporting `valid`, `confidence`, and `principalreasons`.

**Narrative endpoints and promotion triggers.** The design intends that higher-level gateways and
helper APIs will integrate with the main brain by turning external data into messages processed
through the full coordination pipeline, with outputs promotable into deeper memory layers. In the
current deployment, this promotion is manual curation (Chapter 22) rather than an automated
pipeline.

---

## 25.5 Use of Global Modes and Settings

In the current deployment, coordinator workflows are constrained by global safety, policy, and
resource settings.

**Safety and ethical constraints.** In the current deployment, BBB at **0.0.0.0:8016** provides
input truth filtering via `call_truth_filter` and output guarding via `apply_output_guards_async`.
The `truthverdict` attached to `UltimateResponse` is advisory in the current deployment; hard-gate
behavior for specific threat levels is future work (Chapter 16).

**Service discovery and concurrency limits.** In the current deployment, `discover_services()`
performs health checks over the `SERVICES` registry to build `available_services`. A semaphore
(`MAX_CONCURRENT_CHATS`) bounds concurrent `/chat` and `/chat/async` requests. When
`llm20production` or `rag_server` are unavailable, the coordinator raises clear errors rather
than silently misrouting traffic; no fallback fabric is currently wired into this entrypoint.

**Logging and observability.** In the current deployment, structured logging captures request
start, service call failures, BBB guard errors, prefrontal stage status, and request completion
with durations and body previews. Combined with `/status` and `/architecture` endpoints, this
supports operational observability and allows reconstruction of how a particular request was
processed.

---

## 25.6 Coordination with Container Paths and NBB Layers

In the current deployment, the coordinator is coupled to the neurobiological and container paths
through NBB microservices and consciousness metadata.

**Prefrontal and I-container layers.** In the current deployment, at the start of each
`ultimatechat` call the coordinator records a `"prefrontal_planner"` layer capturing available
services, then invokes `nbb-i-containers` (**127.0.0.1:8101**, confirmed) and records its status
and internal `consciousnesslayers` under `"nbb_prefrontal_cortex"` — or marks it skipped if not
responding. It also queries the I-container-style service (`jarvis-i-containers`, port **8015**,
confirmed), whose response is reflected in an `"icontainers-identity"` layer with `icontainers_state`.

**What the NBB prefrontal service returns.** In the current deployment, when `nbb-i-containers`
responds successfully, it returns a short analysis and a dictionary of its own
`consciousnesslayers` indicating which internal stages (input reception, context analysis, memory
access, synthesis) were exercised. The coordinator stores this under `prefrontal_response` and
nests those internal layers in `consciousnesslayers`. In the 2026-02-15 case study, the
`nbb_prefrontal_cortex` layer was `status: "skipped"` with reason `"nbbprefrontalcortex not
configured"`, while `icontainers-identity` was `status: "active"` — a contrast that documents
exactly which NBB layers fired for that request (Chapter 9 §9.3.5).

**What is NOT in the `ultimatechat` path.** In the current deployment, the full Neurobiological
Master pipeline (BBB → I-containers → Qualia Engine → consciousness bridge, `jarvis-neurobiological-master`
port **8018**) is **not** invoked on every `/chat` call. It has its own `POST /process` endpoint
and is invoked in specific integration flows and tests. For that pipeline's detail see
**Chapter 12**. The `jarvis-qualia-engine` (port **8017**), `jarvis-mother-protocols` (port
**4000**), and `jarvis-temporal-consciousness` (port **7007**) are confirmed running but not
currently wired into the primary `/chat` path (Chapter 23).

---

## 25.7 Orchestration of Language Models and Evaluators

In the current deployment, language models and evaluators participate in coordinator workflows
through `jarvis-20llm-production` and the judge pipeline.

**Model selection and prompt construction.** In the current deployment, for answer synthesis the
main brain targets `jarvis-20llm-production` (**127.0.0.1:8008**, confirmed) as the primary
fabric. It builds a persona-aware enhanced message including RAG and web-research context when
available, then sends this prompt with the `userid` to the fabric's `/chat` endpoint. The
response is parsed for common output fields (`response`, `result`, `output`, `answer`), and
`"llm20production"` is recorded in `servicesused`. Logs from the 2026-02-15 deployment show 21
distinct model proxies responding sequentially behind this fabric (**127.0.0.1:8201–8222**,
confirmed; proxy at **127.0.0.1:8030**, confirmed). For full detail on the ensemble and judge
pipeline see **Chapter 33**.

**Judge pipeline.** In the current deployment, judge services at **7230** (truth), **7231**
(consistency), **7232** (alignment), **7233** (ethics) evaluate ensemble output. If the judge
pipeline is down, `jarvis-main-brain` falls back to the 20-LLM answer and marks consensus
metrics as degraded (Chapter 33).

**Output evaluation, guards, and identity normalization.** In the current deployment, after
obtaining a raw response, the coordinator runs `clean_response_for_display` to strip legacy
multi-agent scaffolding, passes the result through `apply_output_guards_async` (BBB
`/filter` at **0.0.0.0:8016**), and applies `normalize_identity` to ensure the answer speaks
as Ms. Egeria Jarvis. `TruthValidator` identity and hallucination checks are applied as part
of the `truthverdict` computation.

---

## 25.8 Error Handling, Resilience, and Observed Performance

In the current deployment, error handling and resilience are explicit design concerns.

**Endpoint-level error handling and timeouts.** In the current deployment, `jarvis-main-brain`
wraps all external service calls in try/except blocks, logs errors with structured metadata, and
uses explicit timeouts for RAG, web research, NBB prefrontal, and LLM fabric calls. The NBB
prefrontal call uses a 3-second timeout; if `nbb-i-containers` times out or raises an exception,
`call_nbb_prefrontal` returns a `"timeout"` or `"exception"` status and the coordinator
continues (Chapter 17 §17.7). When `llm20production` is unavailable, the coordinator raises an
HTTP error; no fallback fabric is currently wired.

**Service health monitoring.** In the current deployment, `/status` and `/architecture`
endpoints allow operators and automated monitors to detect when key pipeline components are down
or misconfigured. `discover_services()` centralizes health probing so all stages work from a
consistent view of system health.

**Empirical performance.** In the current deployment on the reference host (Legion 5, local
Docker), heavy `/chat` requests with all major services enabled take on the order of 9–10
minutes end-to-end, with most time inside `jarvis-20llm-production`. The NBB prefrontal, RAG,
and web-research stages each have explicit timeouts and remain small contributors to overall
latency (Chapter 17 §17.8).

---

## 25.9 Summary

In the current deployment, the consciousness coordinator is implemented as `jarvis-main-brain`
(port **8050**) together with gateway adapters and helper services, managing context collection,
workflow planning, and narrative production across confirmed running services. It ties together
`jarvis-chroma`-backed semantic memory, dual-track neurobiological and container paths, BBB
safety and verification modules, the `llm20production` ensemble fabric and judge pipeline, and
`background_rag_store` memory writes.

**Key asymmetries in the current deployment:** The main `ultimatechat` path always runs the
analytical path (ensemble + judges + BBB); meaning-oriented modules are partly present as
confirmed running services but not all wired into `/chat`. The full Neurobiological Master
pipeline is a separate flow, not invoked on every user chat. These asymmetries are deliberate
staged integration choices.

By recording detailed `consciousnesslayers` metadata, attaching BBB `truthverdict` to every
response, surfacing `/health`, `/status`, and `/architecture` endpoints, and incorporating
explicit error handling and timeouts, the coordinator turns a complex distributed system into a
single, inspectable process whose latency and behavior can be empirically verified. For the
canonical execution sequence see **Chapter 17**. For the Neurobiological Master's own pipeline
see **Chapter 12**. For the ensemble and judge stack see **Chapter 33**.
