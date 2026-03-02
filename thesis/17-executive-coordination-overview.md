> **Why this matters for Polymathmatic Geography**
> This chapter explains how Ms. Jarvis's "front lobe" now decides which instruments to play on
> each request, including a distinct neuro‑inspired prefrontal stage. It supports:
> - **P1 – Every where is entangled** by routing between spatial, semantic, commons, and
>   neurobiological services as one coordinated instrument, including a prefrontal NBB layer that
>   runs ahead of deeper reasoning.
> - **P3 – Power has a geometry** by making control flow and authority legible in the microservice
>   graph and in explicit `consciousness_layers`, rather than hiding them inside a monolith.
> - **P5 – Design is a geographic act** by encoding how Appalachian questions are steered through
>   local RAG, web research, spiritual and BBB filters, and a prefrontal cortex microservice.
> - **P12 – Intelligence with a ZIP code** by prioritizing place‑aware services (GIS‑backed RAG,
>   MountainShares knowledge, local web research) whenever they are healthy.
> - **P16 – Power accountable to place** by exposing routing decisions, prefrontal verdicts, health
>   state, and memory writes through explicit APIs, logs, and `consciousness_layers`.
>
> As such, this chapter belongs to the **Computational Instrument** tier: it specifies the
> executive coordinator that turns a set of independent services into a single, inspectable
> cognitive system with a measurable prefrontal phase.

---

## Status as of March 2026

| Category | Details |
|---|---|
| **Implemented and verified** | `jarvis-main-brain` confirmed running at **127.0.0.1:8050**. `UltimateRequest` model (message, userid, role, useallservices) and `UltimateResponse` (response, servicesused, consciousnesslevel, processingtime, architecturelayers, consciousnesslayers, truthverdict) both live. `SERVICES` registry and `discover_services()` health-check loop operational. `prefrontal_planner` `ConsciousnessLayer` appended on every `/chat` call. `call_nbb_prefrontal` called unconditionally at the start of every `ultimate_chat` execution; NBB prefrontal cortex is `nbb-i-containers` at **127.0.0.1:8101** (internal 7005), confirmed running. `call_truth_filter` invoking BBB on **0.0.0.0:8016** (`jarvis-blood-brain-barrier`, confirmed) for input truth verdict, attached as `truthverdict` on `UltimateResponse`. `jarvis-20llm-production` at **127.0.0.1:8008** (confirmed) as primary LLM fabric; 21/22 models responding consistently (BakLLaVA intentionally disabled); wall-clock consensus ~120–145s. Semaphore proxy (`jarvis-semaphore`, **port 8030**, `max_concurrent: 4`) confirmed as mandatory intermediary between main brain and 20-LLM ensemble; requires float `timeout` in proxy payload. `apply_output_guards_async` calling BBB `/filter` as decoding-time output guard; timeout corrected to **8.0s** (was `None`, caused indefinite hang after LLM completion — fixed 2026‑03‑02). `normalize_identity` applied to every response; confirmed firing on async path producing identity-aware Ms. Jarvis voice (2026‑03‑02). `background_rag_store` scheduling near-duplicate check and RAG write after every `/chat` response. `/chatlight/async` + `/chatlight/status/{job_id}` async interface live (added 2026‑03‑02); returns `job_id` instantly, polls for result, `mode: "light-async"` in response. `/chat/async` + `/chat/status/{job_id}` full-pipeline async interface also live with in-memory `active_jobs` table. `ms_jarvis_memory` confirmed written via `background_rag_store` (verified in 2026‑02‑15 case study; see Chapter 9 §9.3.5). `jarvis-spiritual-rag` at **127.0.0.1:8005** used as RAG server (earlier plan documents listed 8103; confirmed port is **8005**). `jarvis-web-research` reachable on internal Docker network only (port 8008/tcp, no host binding); distinct from `jarvis-20llm-production` which binds host port 8008. |
| **Partially implemented / scaffolded** | `truth_verdict` is attached to every response and is advisory in the current deployment — it does not hard-gate the input pipeline. Modules in `SERVICES` registry including `qualia_engine`, `i_containers`, `neurobiological_master`, and `autonomous_learner` are exercised in other workflows but not yet wired into the `/chat` path. `ms_jarvis_memory` is currently append-only; deduplication via near-duplicate similarity check is advisory (affects reuse and skip logic, not write). `active_jobs` for both async interfaces is in-memory only; does not survive container restarts. |
| **Future work / design intent only** | Hard-gate behavior on `truth_verdict` for certain role or threat levels. Full wiring of `qualia_engine`, `i_containers`, `neurobiological_master`, and `autonomous_learner` into the `/chat` execution path. Persistent job store replacing in-memory `active_jobs`. Richer per-phase timing and per-model latency exposure via a dedicated metrics endpoint. UI layer consuming `/chatlight/async` poll pattern for non-blocking chat interface. |

> **This chapter is the canonical description of the `ultimatechat` and `chatlight` execution
> paths.** All other chapters that reference "what happens on a user chat," "main brain
> coordination," or the `UltimateResponse` structure should cross-reference here.
>
> **`ultimatechat` authoritative sequence:**
> `UltimateRequest` received → `prefrontal_planner` layer appended → `call_nbb_prefrontal`
> executed → `call_truth_filter` via BBB (port 8016) → RAG context via `jarvis-spiritual-rag`
> (port 8005) + `jarvis-web-research` (internal) → `llm20production` synthesis via
> `jarvis-20llm-production` (port 8008) → `apply_output_guards_async` via BBB (8.0s timeout) →
> `normalize_identity` → `background_rag_store` into `ms_jarvis_memory` → `UltimateResponse`
> returned.
>
> **`chatlight/async` authoritative sequence:**
> `POST /chatlight/async` received → `job_id` returned instantly → background task: semaphore
> proxy (port 8030) → `jarvis-20llm-production` (port 8008, ~120–145s) →
> `apply_output_guards_async` via BBB (8.0s timeout) → `normalize_identity` → job marked
> `done`; client polls `GET /chatlight/status/{job_id}` → result with `mode: "light-async"`,
> `models_responded`, `latency`.

---

# 17. Executive Coordination Overview

This chapter describes the concrete control layer implemented by the `Ms. Jarvis ULTIMATE`
main-brain service on **port 8050**, which decides which subsystems to invoke, in what order,
and under which constraints for each request. It serves as a bridge between the neuro‑inspired
NBB modules and the containerized services that implement them, with emphasis on
responsibilities, information flows, and observed runtime behavior rather than deployment detail.

---

## 17.1 Role in the System

In the current deployment, the executive layer is realized by a single FastAPI application,
`jarvis-main-brain` (confirmed running at **127.0.0.1:8050**), which coordinates more than twenty
consciousness, processing, and infrastructure services based on a static `SERVICES` registry and
live health checks. For each user request, this layer interprets the input, runs a neuro‑inspired
prefrontal stage, plans a service route based on current health and configuration, and integrates
downstream outputs into one coherent reply.

Interpretation is handled via the `UltimateRequest` model, which captures the user's message,
`userid`, a `role` (for example `"community"`), and a `useallservices` flag indicating whether
broad fan-out is permitted. Planning is expressed in explicit code that uses the `SERVICES`
dictionary plus `discover_services()` to decide which components are actually available for a
given request. Integration merges the outputs of the selected components, applies BBB-based safety
filtering, normalizes Ms. Jarvis's identity, and returns an `UltimateResponse` containing
`response`, `servicesused`, `consciousnesslevel`, `processingtime`, `architecturelayers`,
`consciousnesslayers`, and a BBB `truthverdict`.

This chapter is the system of record for what actually happens on a live user chat. Other
chapters describing "main brain behavior," "consciousness coordinator," or "executive layer" —
including Chapters 11, 12, 23, and 25 — should point here for the authoritative execution path
rather than describing their own alternative accounts of what runs in `ultimatechat`.

---

## 17.2 Inputs and Signals

When deciding how to process a `/chat` call, in the current deployment the coordinator draws on
several classes of signals. The primary input is the `UltimateRequest` payload, which encodes the
current message, the user identity, a role label, and a high‑level instruction about whether to
use all services. A second key input is the dynamic `available_services` map, obtained by probing
each entry in the `SERVICES` dictionary — `qualia_engine`, `consciousness_bridge`,
`blood_brain_barrier`, `neurobiological_master`, `i_containers`, `autonomous_learner`,
`rag_server`, `web_research`, `llm20_production`, and NBB microservices — for a healthy response
via `check_service_health`.

For asynchronous jobs created via `/chat/async` or `/chatlight/async`, in the current deployment
the system maintains in-memory job tables keyed by `job_id`, with each entry storing job status
(queued, running, done, or error), a progress string, creation time, the original message and
`userid`, and on completion the full result object. External clients can call the corresponding
`/status/{job_id}` endpoint to see whether a request is still running, what stage it has
reached, and how long it has been active. Global settings — including the API key, the
`MAX_CONCURRENT_CHATS` semaphore limit, and service URLs — are represented via environment
variables and module-level constants.

---

## 17.3 Concrete Request Flow

In the current deployment, the concrete decision flow for a synchronous `/chat` request is
implemented by the `ultimate_chat` handler and follows a reproducible, fixed sequence.

**Step 1 — Service discovery and prefrontal planning.** When a request arrives, the coordinator
logs the message and constructs an empty `available_services` dictionary, which it populates by
iterating over all `(service_name, url)` pairs in `SERVICES` and invoking
`check_service_health`. It then appends a `ConsciousnessLayer` named `"prefrontal_planner"` with
`kind="prefrontal"` and `status="active"`, whose details record the list of available service
names. Immediately afterward, it calls `call_nbb_prefrontal` with the raw message and a simple
context dictionary containing `userid` and `role`. The NBB prefrontal cortex service is
`nbb-i-containers` at **127.0.0.1:8101** (internal 7005), confirmed running. Its result is
recorded as a second `ConsciousnessLayer` named `"nbb_prefrontal_cortex"`. This stage runs
unconditionally at the start of every `ultimate_chat` call.

**Step 2 — Truth verdict on the input.** Before building extended context, in the current
deployment the coordinator sends the original user message through `call_truth_filter`, which
invokes `jarvis-blood-brain-barrier` on **port 8016** and returns a slim verdict containing
`valid`, `confidence`, and `principalreasons`. This verdict is attached as `truthverdict` in the
final response. In the current deployment, the pipeline treats this verdict as advisory rather
than as a hard gate on the user's input; hard-gate behavior for specific role or threat levels
is identified as future work.

**Step 3 — Context building with RAG and web research.** For context gathering, in the current
deployment the coordinator checks whether `"rag_server"` and `"web_research"` appear in
`available_services` and, if so, calls them via `build_rag_context` and `build_web_context`. The
RAG helper queries `jarvis-spiritual-rag` at **port 8005** (confirmed running; earlier plan
documents listed 8103 — the correct port is **8005**) via its `/search` endpoint with the user's
message and an optional metadata filter based on role, then constructs a labeled
`From Knowledge Base:` block. The web helper calls `jarvis-web-research` (internal Docker
network, port 8008/tcp, no host binding — distinct from `jarvis-20llm-production` which binds
host port 8008) via its `/search` endpoint and wraps any returned summary in a
`From Web Research:` block. These blocks are combined into a `context_block` and used by
`build_egeria_prompt` to construct the enhanced prompt.

**Step 4 — LLM fabric selection and execution.** For answer synthesis, in the current deployment
the coordinator targets `llm20_production` as its primary LLM fabric. The 20-LLM ensemble
(`jarvis-20llm-production`, port **8008**) is accessed via the semaphore proxy
(`jarvis-semaphore`, port **8030**, `max_concurrent: 4`), which is a mandatory intermediary that
serializes concurrent Ollama requests. The semaphore proxy requires a float `timeout` value (not
`None`) in its payload; the main brain passes `600.0` as the timeout and uses
`httpx.Timeout(None, connect=5.0, read=None)` on its own client so the semaphore manages the
deadline rather than the main brain's httpx layer. The ensemble dispatches to 22 model proxy
containers (llm1-proxy:8201 through llm22-proxy:8222), of which 21 respond consistently
(BakLLaVA is intentionally disabled via DNS). Wall-clock consensus time is approximately
120–145 seconds depending on system load. If `llm20_production` is unavailable or returns a
non-200 status, the coordinator raises an HTTP error; no further fallback fabric is currently
wired into this entrypoint. For full details on the 20-LLM ensemble and judge pipeline, see
**Chapter 33**.

**Step 5 — Post-processing, safety guard, and background storage.** Once a raw LLM output is
obtained, in the current deployment the coordinator feeds it through `clean_response_for_display`
to strip legacy RAG metadata and multi-agent analysis scaffolding. It then passes the cleaned
text through `apply_output_guards_async`, which calls the BBB's `/filter` endpoint on port 8016
as a decoding-time output guard using `httpx.AsyncClient(timeout=8.0)`. The 8-second timeout is
a permanent architectural fix (2026‑03‑02): the original `timeout=None` caused the entire chat
response to hang indefinitely after the 20-LLM ensemble completed, because the BBB filter call
blocked without bound. After the output guard, `normalize_identity` is applied to ensure the
answer speaks as Ms. Egeria Jarvis rather than as a generic LLM — confirmed producing
identity-aware responses on the async path (2026‑03‑02). In parallel, the coordinator schedules
a `background_rag_store` task that checks for near-duplicate entries via `/search` with `top_k=1`
and, if no near-duplicate is found, stores a truncated version of the query and response plus
metadata into `ms_jarvis_memory`. The final `UltimateResponse` aggregates the safe, normalized
answer, `servicesused`, `consciousnesslevel` (currently `"ultimate_collective"`), total
`processingtime`, `architecturelayers`, the consciousness layers themselves, and the earlier BBB
`truthverdict`.

---

## 17.4 Interaction with Other Layers

In the current deployment, because the `SERVICES` registry spans consciousness, processing,
gateway, and infrastructure layers, the executive coordinator sits at their intersection. It
decides whether a given request will be routed through context layers such as `rag_server` and
`web_research`, or handled with a narrower subset when those subsystems are unavailable, and it
unconditionally exercises the NBB prefrontal cortex at the beginning of every `ultimate_chat`
call.

Although the registry includes modules like `qualia_engine`, `i_containers`,
`autonomous_learner`, and `neurobiological_master`, in the current deployment the `/chat` path
primarily wires in `blood_brain_barrier`, `rag_server`, `web_research`, `llm20_production`, and
the NBB prefrontal cortex. Additional modules remain available for other workflows and are
identified as future expansion points for this entrypoint. Upstream, unified gateways and
academic front-ends treat `Ms. Jarvis ULTIMATE` as a single main-brain endpoint, calling
`/chat`, `/chatlight`, `/chatlight/async`, or `/chat/async` with standard payloads. Downstream,
the executive layer fans out to the confirmed running Dockerized services described in this
chapter and in Chapters 11, 12, 16, 33, and 9.

---

## 17.5 Asynchronous Job Handling

The executive layer exposes two asynchronous interfaces for long-running requests.

**Full-pipeline async (`/chat/async` + `/chat/status/{job_id}`).** When a client submits an async
request, the service generates a `job_id`, inserts an entry into the `active_jobs` dictionary
with `status: "processing"`, and launches `process_chat_job` as an independent task. That
coroutine runs the full `ultimate_chat` coordination pipeline — service discovery, NBB prefrontal
execution, context building, `llm20production` synthesis, BBB guarding, identity normalization,
and background RAG storage — updating job status as it proceeds and marking the entry `"complete"`
or `"error"` on termination.

**Lightweight consensus async (`/chatlight/async` + `/chatlight/status/{job_id}`).** Added
2026‑03‑02 (git tag `v2026.03.02-chatlight-async-working`). This interface bypasses the full
prefrontal, RAG, and web-research pipeline and routes directly to the 20-LLM ensemble via the
semaphore proxy. It is designed for UI development and scenarios where a non-blocking connection
and a 2–3 minute consensus result are preferable to a 9–10 minute full-pipeline response. The
submit endpoint returns a `job_id` and `poll_url` instantly. The client polls
`/chatlight/status/{job_id}` at any interval; the response includes `status` (queued / running /
done / error), `elapsed` seconds, and on completion a `result` object containing `answer`,
`response`, `latency`, `mode: "light-async"`, `models_responded`, and `userid`. The
`normalize_identity` step is applied, confirming that Ms. Jarvis's identity voice is present even
on the lightweight path. In both async interfaces, `active_jobs` is an in-memory table; a
persistent job store is identified as future work.

---

## 17.6 RAG Storage and Memory Integration

In the current deployment, the executive coordinator not only consumes RAG context but also
contributes new experience back into `ms_jarvis_memory` via `background_rag_store`. After
assembling a final response for a `/chat` request, it schedules this coroutine with the original
message, the final response text, and the list of `servicesused`. The background task first calls
the RAG server's `/search` endpoint with the query and `top_k=1` to check for near-duplicates;
if the top result's similarity score exceeds a configured threshold, the task logs a
`rag_skip_duplicate` event and skips the write.

If the query is sufficiently novel, the task calls the RAG server's `/store` endpoint with a
payload that includes a system `userid` (for example `"autosystem"`), truncated versions of the
query and response, an ISO-formatted timestamp, and metadata such as the first few `servicesused`
and flags indicating the record was auto-stored and deduplicated. In the current deployment,
`ms_jarvis_memory` is append-only; the deduplication check is advisory and affects the skip
logic, not the write path. Because this consolidation occurs in the background, the main `/chat`
response returns promptly while memory updates proceed asynchronously.

---

## 17.7 Health-Check and Prefrontal Behavior

In the current deployment, service discovery uses `check_service_health` to probe each
configured service, preferring `/health` when available and otherwise falling back to a GET on
the service's primary operation path or root URL. Certain services such as `chroma`, `redis`,
`lm_synthesizer`, and `rag_server` are treated as always healthy or are checked via specialized
endpoints to avoid unnecessary overhead.

With `nbb-i-containers` at **127.0.0.1:8101** confirmed running, `discover_services` includes
`"nbb_prefrontal_cortex"` in `available_services`, enabling the prefrontal stage to run reliably
at the start of each `ultimate_chat` request and exposing its status and inner
`consciousnesslayers` in the final response.

The prefrontal call itself uses a short timeout (currently 3 seconds) and does not block the rest
of the pipeline: if the NBB service is slow or unavailable, `call_nbb_prefrontal` returns a
status of `"timeout"` or `"exception"` and the main coordinator continues with context building
and LLM synthesis. When the NBB service responds successfully, its consciousness-bridge-style
summary is recorded under `prefrontal_response`, and its internal layers — such as input
reception, context analysis, and synthesis completion — are nested under `consciousnesslayers`
for inspection.

---

## 17.8 Operational Pattern and Performance

In the current deployment on the reference host (Legion 5, local Docker), empirical runs show
the following latency profile:

- **`/chatlight/async` (lightweight consensus):** 20-LLM ensemble completes in ~120–145s; full
  job wall clock ~130–160s including semaphore queuing, BBB guard (8s timeout), and identity
  normalization. HTTP connection returns instantly; client polls for result.
- **`/chat` (full pipeline, synchronous):** End-to-end latency on the order of 9–10 minutes,
  with most time inside `llm20_production`. NBB prefrontal cortex, RAG context building, and web
  research each have explicit timeouts and do not dominate under these workloads.
- **Semaphore queuing effect:** Multiple concurrent requests to the 20-LLM service queue in the
  semaphore proxy (max 4 concurrent). Each Ollama model run is sequential within the ensemble,
  so back-to-back test calls accumulate wait time. The semaphore should be restarted between
  test sessions to drain queued work before benchmarking.

The `MAX_CONCURRENT_CHATS` semaphore and explicit logging of per-phase timing provide operators
with levers for tuning throughput and responsiveness without sacrificing safety or introspection.

---

## 17.9 Implementation vs. Conceptual Model

In the current deployment, the running implementation of the executive layer closely tracks the
conceptual responsibilities set out at the beginning of the chapter. Interpretation is realized
by typed request models, explicit logging of user messages, and job-level bookkeeping for both
synchronous and asynchronous flows. Planning is operationalized as a health-informed routing
strategy that always consults the NBB prefrontal cortex and, when available, routes through
`rag_server`, `web_research`, and the `llm20_production` fabric, with BBB used both to evaluate
inputs and to guard outputs.

There remain deliberate gaps between the broader architectural vision and this particular
entrypoint's wiring. The `SERVICES` registry includes additional neurobiological and
community-oriented modules (`qualia_engine`, `i_containers`, `neurobiological_master`,
`autonomous_learner`, and others) that are exercised in other workflows but not yet integrated
into the `/chat` path. This staged integration strategy allows the system to deliver robust,
explainable responses while preserving room for future experiments in deeper neurobiological and
community-governance coupling.

---

## 17.10 Summary

In the current deployment, the executive coordination layer — realized by `jarvis-main-brain` at
**127.0.0.1:8050** — provides a concrete and instrumented account of how a multi-layer cognitive
architecture is orchestrated in practice, including a dedicated prefrontal NBB phase. The
confirmed execution sequences are:

**`/chat` (synchronous, full pipeline):**

1. `UltimateRequest` (message, userid, role, useallservices) received at `/chat`
2. `prefrontal_planner` `ConsciousnessLayer` appended; `available_services` populated
3. `call_nbb_prefrontal` executed unconditionally → `nbb-i-containers` at **127.0.0.1:8101**
4. `call_truth_filter` → BBB at **0.0.0.0:8016** → `truthverdict` attached (advisory)
5. `build_rag_context` → `jarvis-spiritual-rag` at **127.0.0.1:8005**
6. `build_web_context` → `jarvis-web-research` (internal Docker network, port 8008/tcp)
7. `llm20_production` synthesis → semaphore proxy (port 8030) → `jarvis-20llm-production` at **127.0.0.1:8008** (~120–145s, 21/22 models)
8. `apply_output_guards_async` → BBB at **0.0.0.0:8016** (output guard, 8.0s timeout)
9. `normalize_identity` applied
10. `background_rag_store` scheduled → `ms_jarvis_memory` (append-only, dedup advisory)
11. `UltimateResponse` returned with `response`, `servicesused`, `consciousnesslevel`, `processingtime`, `architecturelayers`, `consciousnesslayers`, `truthverdict`

**`/chatlight/async` + `/chatlight/status/{job_id}` (async, lightweight consensus):**

1. `POST /chatlight/async` received → `job_id` + `poll_url` returned instantly
2. Background task acquires `chat_semaphore`; calls `discover_services()`
3. `build_egeria_prompt` constructs enhanced message
4. `httpx.Timeout(None, connect=5.0, read=None)` client → semaphore proxy (port 8030) → `jarvis-20llm-production` (port 8008, timeout 600.0 passed to semaphore)
5. 20-LLM ensemble completes (~120–145s); response extracted from `body["response"]`
6. `clean_response_for_display` → `apply_output_guards_async` (BBB, 8.0s timeout) → `normalize_identity`
7. Job marked `done`; `result` includes `answer`, `latency`, `mode: "light-async"`, `models_responded`
8. Client polls `GET /chatlight/status/{job_id}` → returns `status`, `elapsed`, `result`

By anchoring the high-level metaphors of prefrontal control, introspection, and consolidation in
specific code paths, data structures, and performance measurements, this layer demonstrates that
the thesis's coordination concepts are not only architecturally coherent but also implementable,
measurable, and amenable to targeted optimization in a real-world deployment. For details on
the 20-LLM ensemble and judge pipeline invoked at step 7, see **Chapter 33**. For the
Neurobiological Master's own BBB → I-containers → Qualia → consciousness-bridge pipeline (a
separate flow not in the primary `/chat` path), see **Chapter 12**.
