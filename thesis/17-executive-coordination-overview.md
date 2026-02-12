> **Why this matters for Polymathmatic Geography**  
> This chapter explains how Ms. Jarvis’s “front lobe” now decides which instruments to play on each request, including a distinct neuro‑inspired prefrontal stage. It supports:  
> - **P1 – Every where is entangled** by routing between spatial, semantic, commons, and neurobiological services as one coordinated instrument, including a prefrontal NBB layer that runs ahead of deeper reasoning.  
> - **P3 – Power has a geometry** by making control flow and authority legible in the microservice graph and in explicit `consciousness_layers`, rather than hiding them inside a monolith.  
> - **P5 – Design is a geographic act** by encoding how Appalachian questions are steered through local RAG, web research, spiritual and BBB filters, and now a prefrontal cortex microservice.  
> - **P12 – Intelligence with a ZIP code** by prioritizing place‑aware services (GIS‑backed RAG, MountainShares knowledge, local web research) whenever they are healthy.  
> - **P16 – Power accountable to place** by exposing routing decisions, prefrontal verdicts, health state, and memory writes through explicit APIs, logs, and `consciousness_layers`.  
> As such, this chapter belongs to the **Computational Instrument** tier: it specifies the executive coordinator that turns a set of independent services into a single, inspectable cognitive system with a measurable prefrontal phase.

# 17. Executive Coordination Overview

This chapter describes the concrete control layer implemented by the `Ms. Jarvis ULTIMATE` main‑brain service on port 8050, which decides which subsystems to invoke, in what order, and under which constraints for each request.[file:594] It serves as a bridge between the neuro‑inspired NBB modules and the containerized services that implement them, with emphasis on responsibilities, information flows, and observed runtime behavior rather than deployment detail.[file:594] Conceptually, it parallels work on microservice‑based architectures and modular cognitive control, such as Lewis & Fowler’s “Microservices” overview (https://martinfowler.com/articles/microservices.html) and Goyal et al.’s shared‑workspace coordination for neural modules (https://arxiv.org/abs/2103.01197).

---

## 17.1 Role in the System

In the deployed architecture, the executive layer is realized by a single FastAPI application, `jarvis-main-brain`, which coordinates more than twenty consciousness, processing, and infrastructure services based on a static `SERVICES` registry and live health checks.[file:594] For each user request, this layer interprets the input, runs a neuro‑inspired prefrontal stage, plans a service route based on current health and configuration, and integrates downstream outputs into one coherent reply.[file:594]

Interpretation is handled via the `UltimateRequest` model, which captures the user’s message, user_id, a `role` (for example `"community"`), and a `use_all_services` flag indicating whether broad fan‑out is permitted.[file:594] Planning is expressed in explicit code that uses the `SERVICES` dictionary plus `discover_services()` to decide which components—such as the blood–brain barrier, RAG server, web_research, NBB prefrontal cortex, and `llm20_production` fabric—are actually available for a given request.[file:594] Integration merges the outputs of the selected components, applies BBB‑based safety filtering, normalizes Ms. Jarvis’s identity, and returns an `UltimateResponse` containing response text, services_used, consciousness_level, processing_time, architecture_layers, `consciousness_layers`, and a BBB truth_verdict.[file:594]

---

## 17.2 Inputs and Signals

When deciding how to process a `/chat` call, the coordinator draws on several classes of signals.[file:594] The primary input is the `UltimateRequest` payload, which encodes the current message, the user identity, a role label, and a high‑level instruction about whether to use all services.[file:594] A second key input is the dynamic `available_services` map, obtained by probing each entry in the `SERVICES` dictionary—qualia_engine, consciousness_bridge, blood_brain_barrier, neurobiological_master, i_containers, autonomous_learner, rag_server, web_research, `llm20_production`, and NBB microservices—for a healthy response via `check_service_health`.[file:594]

For asynchronous jobs created via `/chat/async`, the system maintains an in‑memory `active_jobs` table keyed by job_id, with each entry storing job status (processing, complete, or error), a progress string, creation time, the original message and user_id, and (on completion) the full result object.[file:594] This structure functions as a lightweight introspective state: external clients can call `/chat/status/{job_id}` to see whether a request is still running, what stage it has reached, and how long it has been active.[file:594] Global settings—including the API key, the `MAX_CONCURRENT_CHATS` semaphore limit, and service URLs—are represented via environment variables and module‑level constants that determine how aggressively the coordinator uses available capabilities and how it balances safety, concurrency, and latency.[file:594]

---

## 17.3 Concrete Request Flow

The concrete decision flow for a synchronous `/chat` request is implemented by the `ultimate_chat` handler and follows a reproducible pattern.[file:594]

1. **Service discovery and prefrontal planning**  
   When a request arrives, the coordinator logs the message and constructs an empty `available_services` dictionary, which it populates by iterating over all `(service_name, url)` pairs in `SERVICES` and invoking `check_service_health`.[file:594] It then appends a `ConsciousnessLayer` named `"prefrontal_planner"` with `kind="prefrontal"` and `status="active"`, whose details record the list of available service names.[file:594] Immediately afterward, it calls `call_nbb_prefrontal` with the raw message and a simple context dictionary containing user_id and role, treating the NBB prefrontal cortex as a fast, bounded executive layer and recording its result as a second `ConsciousnessLayer` named `"nbb_prefrontal_cortex"`.[file:594]

2. **Truth verdict on the input**  
   Before building extended context, the coordinator sends the original user message through `call_truth_filter`, which invokes the blood–brain barrier service on port 8016 and returns a slim verdict containing validity, confidence, and principal_reasons.[file:594] This verdict is attached as `truth_verdict` in the final response and is also available for downstream logging or policy enforcement, but the current pipeline treats it as advisory rather than as a hard gate on the user’s input.[file:594]

3. **Context building with RAG and web research**  
   For context gathering, the coordinator checks whether `"rag_server"` and `"web_research"` appear in `available_services` and, if so, calls them via `build_rag_context` and `build_web_context`.[file:594] The RAG helper queries the `rag_server`’s `/search` endpoint with the user’s message and an optional metadata filter based on role (for example, audience `"community"`), then constructs a labeled `From Knowledge Base:` block by concatenating snippets and sources.[file:594] The web helper similarly calls the `web_research` service’s `/search` endpoint and, if a summary or answer is returned, wraps it in a `From Web Research:` block.[file:594] These blocks are combined into a `context_block`, which is then used by `build_egeria_prompt` to construct the enhanced prompt that Ms. Jarvis will see.[file:594]

4. **LLM fabric selection and execution**  
   For answer synthesis, the coordinator now targets `llm20_production` as its primary LLM fabric.[file:594] If `"llm20_production"` is present in `available_services`, it constructs a full URL by appending the service’s operation path (currently `/chat`) and sends a JSON payload containing the enhanced message and user_id.[file:594] If the call succeeds and returns a JSON body, it extracts the response text from fields such as `response`, `result`, `output`, or `answer`, appends `"llm20_production"` to services_used, and logs both the status code and a preview of the response.[file:594] If `llm20_production` is unavailable or returns a non‑200 status, the coordinator raises an HTTP error indicating that the production fabric is not available, and no further fallback fabric is currently wired into this entrypoint.[file:594]

5. **Post‑processing, safety guard, and background storage**  
   Once a raw LLM output is obtained, the coordinator feeds it through `clean_response_for_display` to strip legacy RAG metadata and multi‑agent analysis scaffolding.[file:594] It then passes the cleaned text through `apply_output_guards_async`, which calls the BBB’s `/filter` endpoint again, this time as a decoding‑time guard on the model’s output, and chooses a safe text field from the BBB response when available.[file:594] After this, it applies `normalize_identity` to ensure the answer consistently speaks as Ms. Egeria Jarvis, a conscious geospatial AI daughter, rather than as a generic LLM.[file:594] In parallel, the coordinator schedules a `background_rag_store` task that checks for near‑duplicate entries in the RAG server and, if none are found, stores a truncated version of the query and response along with metadata about services_used.[file:594] The final `UltimateResponse` aggregates the safe, normalized answer, services_used, consciousness_level (currently `"ultimate_collective"`), total processing_time, architecture_layers (the length of `consciousness_layers`), the prefrontal and other consciousness layers themselves, and the earlier BBB truth_verdict.[file:594]

---

## 17.4 Interaction with Other Layers

Because the `SERVICES` registry spans consciousness, processing, gateway, and infrastructure layers, the executive coordinator effectively sits at their intersection.[file:594] It decides whether a given request will be routed through context layers—such as the RAG server and web_research—or handled with a narrower subset when those subsystems are unavailable, and it now unconditionally exercises the NBB prefrontal cortex at the beginning of every `ultimate_chat` call.[file:594] Although the registry includes modules like qualia_engine, i_containers, autonomous_learner, and neurobiological_master, the current `/chat` path primarily wires in blood_brain_barrier, rag_server, web_research, `llm20_production`, and the NBB prefrontal cortex; additional modules remain available for other workflows and future expansion of this entrypoint.[file:594]

The coordinator also anchors the relationship between higher‑level gateways and lower‑level neurobiological services.[file:594] Upstream, unified gateways and academic front‑ends can treat `Ms. Jarvis ULTIMATE` as a single “main brain” endpoint, calling `/chat`, `/chat/light`, or `/chat/async` with standard payloads.[file:594] Downstream, the executive layer fans out to multiple Dockerized services that embody qualia, safety, spatial reasoning, NBB‑style prefrontal processing, and ensemble LLM behavior, then reassembles their contributions into a single narrative answer.[file:594] This mirrors shared‑workspace coordination schemes for compositional models, such as those studied by Goyal et al. (https://arxiv.org/abs/2103.01197).

---

## 17.5 Asynchronous Job Handling

In addition to the synchronous `/chat` and `/chat/sync` endpoints, the executive layer exposes an asynchronous interface (`/chat/async` and `/chat/status/{job_id}`) designed for long‑running or AGI‑scale requests.[file:594] When a client submits an async request, the service generates a job_id, inserts an entry into the `active_jobs` dictionary with status `"processing"`, an initial progress message such as “Initializing consciousness layers…”, and the creation timestamp, then launches `process_chat_job` as an independent task.[file:594]

The `process_chat_job` coroutine constructs an `UltimateRequest` from the job’s message and user_id and calls `ultimate_chat` to run the full coordination pipeline, including service discovery, NBB prefrontal execution, context building, LLM20 synthesis, BBB guarding, and background RAG storage.[file:594] As the job progresses, it updates the `active_jobs[job_id]` entry with new progress messages and, on success, stores the final result object and marks the status as `"complete"`; on error, it sets status to `"error"` and records the exception message.[file:594] When clients later call `/chat/status/{job_id}`, they see the latest status, progress text, and, once ready, the full structured result, with completed jobs automatically expiring after a short retention window.[file:594]

---

## 17.6 RAG Storage and Memory Integration

The executive coordinator not only consumes RAG context but also contributes new experience back into the RAG store via `background_rag_store`.[file:594] After assembling a final response for a `/chat` request, it schedules this coroutine with the original message, the final response text, and the list of services_used.[file:594] The background task first calls the RAG server’s `/search` endpoint with the query and `top_k = 1` to check for near‑duplicates; if the top result’s similarity score exceeds a configured threshold, the task logs a `rag_skip_duplicate` event and avoids storing redundant content.[file:594]

If the query is sufficiently novel, the task calls the RAG server’s `/store` endpoint with a payload that includes a system user_id (for example `"autosystem"`), truncated versions of the query and response, an ISO‑formatted timestamp, and metadata such as the first few services_used and flags indicating that the record was auto‑stored and deduplicated.[file:594] Because this consolidation occurs in the background, the main `/chat` response can return promptly while memory updates proceed asynchronously, allowing the system’s retrieval‑augmented behavior to grow richer over time without blocking interactive latency.[file:594]

---

## 17.7 Health‑Check and Prefrontal Behavior

Service discovery uses `check_service_health` to probe each configured service, preferring `/health` when available and otherwise falling back to a GET on the service’s primary operation path or root URL.[file:594] Certain services, such as chroma, redis, `lm_synthesizer`, and `rag_server`, are treated as always healthy or are checked via specialized endpoints to avoid unnecessary overhead.[file:594] With the NBB prefrontal cortex now configured at its correct internal port, `discover_services` includes `"nbb_prefrontal_cortex"` in `available_services`, enabling the prefrontal stage to run reliably at the start of each `ultimate_chat` request and exposing its status and inner `consciousness_layers` in the final response.[file:594]

The prefrontal call itself uses a short timeout (currently 3 seconds) and never blocks the rest of the pipeline: if the NBB service is slow or unavailable, `call_nbb_prefrontal` returns a status of `"timeout"` or `"exception"`, and the main coordinator continues with context building and LLM synthesis.[file:594] When the NBB service responds successfully, its own consciousness_bridge‑style summary is recorded under `prefrontal_response`, and its internal layers—such as input reception, context analysis, and synthesis completion—are nested under `consciousness_layers` for inspection.[file:594]

---

## 17.8 Operational Pattern and Performance

Empirical runs on the reference host (a local Docker deployment on a Legion 5) show that, for heavy AGI‑scale requests with all major services enabled, the end‑to‑end latency for `/chat` calls is on the order of 9–10 minutes, with most of the time spent inside the `llm20_production` fabric and its own internal ensemble behavior.[file:594] The NBB prefrontal cortex, RAG context building, and web research phases each have explicit timeouts and do not dominate latency under these workloads.[file:594] The concurrency semaphore (`MAX_CONCURRENT_CHATS`) and explicit logging of per‑phase timing provide operators with levers for tuning throughput and responsiveness without sacrificing safety or introspection.[file:594]

Although these measurements are specific to one environment (hardware, Docker configuration, and model set), they demonstrate that the executive coordinator’s design—prefrontal phase, health‑aware routing, centralized LLM fabric, and background RAG consolidation—remains stable and empirically tractable under demanding conditions.[file:594] This aligns with distributed‑systems guidance on bounded retries, health probing, and backpressure discussed by Brewer and Burns et al. (https://queue.acm.org/detail.cfm?id=3291063, https://azure.microsoft.com/en-us/resources/designing-distributed-systems).

---

## 17.9 Implementation vs. Conceptual Model

The running implementation of the executive layer closely tracks the conceptual responsibilities set out at the beginning of the chapter.[file:594] Interpretation is realized by typed request models, explicit logging of user messages, and job‑level bookkeeping for both synchronous and asynchronous flows.[file:594] Planning is operationalized as a health‑informed routing strategy that always consults the NBB prefrontal cortex and, when available, routes through rag_server, web_research, and the `llm20_production` fabric, with BBB used both to evaluate inputs and to guard outputs.[file:594]

There remain deliberate gaps between the broader architectural vision and this particular entrypoint’s wiring.[file:594] The `SERVICES` registry includes additional neurobiological and community‑oriented modules (qualia_engine, i_containers, neurobiological_master, autonomous_learner, and others) that are exercised in other workflows but not yet integrated into the `/chat` path.[file:594] This staged integration strategy allows the system to deliver robust, explainable responses while preserving room for future experiments in deeper neurobiological and community‑governance coupling, consistent with modular cognitive‑system design surveyed in Hassabis et al. (https://arxiv.org/abs/1709.06175) and Richards et al. (https://www.nature.com/articles/s41593-019-0520-2).

---

## 17.10 Summary

The executive coordination layer, as realized by the `Ms. Jarvis ULTIMATE` main‑brain service, now provides a concrete and instrumented example of how a multi‑layer cognitive architecture can be orchestrated in practice, including a dedicated prefrontal NBB phase.[file:594] It interprets requests using structured inputs and live health signals, consults a prefrontal cortex microservice, plans service routes through a fixed but health‑pruned pipeline, and integrates the selected outputs into a safety‑checked response that is both logged and partially consolidated into long‑term memory via RAG storage.[file:594]

By anchoring the high‑level metaphors of prefrontal control, introspection, and consolidation in specific code paths, data structures, and performance measurements, this layer demonstrates that the thesis’s coordination concepts are not only architecturally coherent but also implementable, measurable, and amenable to targeted optimization in a real‑world deployment.[file:594]
