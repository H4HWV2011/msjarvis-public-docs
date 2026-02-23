> **Why this matters for Polymathmatic Geography**
> This chapter shows how Ms. Jarvis's "thinking" is implemented as an organized fabric of local
> language models rather than a single opaque model. It supports:
> - **P1 – Every where is entangled** by embedding LLMs inside a retrieval and spatial stack
>   (Chroma, GBIM, GeoDB) that keeps reasoning tied to concrete places and institutions.
> - **P3 – Power has a geometry** by routing questions through specific models, memories, and
>   services whose connections can be inspected and redesigned.
> - **P5 – Design is a geographic act** by treating model choice, ensemble wiring, and service
>   topology as design decisions that change how Appalachian realities are seen and narrated.
> - **P12 – Intelligence with a ZIP code** by grounding LLM calls in West Virginia–specific
>   semantic and geospatial memory rather than generic, placeless prompts.
> - **P16 – Power accountable to place** by exposing LLMs only through glass‑box HTTP services
>   that can be logged, audited, and constrained, not as hidden backends with direct user access.
>
> As such, this chapter belongs to the **Computational Instrument** tier: it specifies the model
> pool and service fabric that turn Quantarithmia's spatial‑justice instruments into live,
> language-facing behavior.

<img width="1100" height="900" alt="unnamed(16)"
  src="https://github.com/user-attachments/assets/ae0d8496-798d-4048-adbd-90d4fcc30b67" />

> **Figure 11.1.** The LLM fabric of Ms. Jarvis: user queries flow through RAG, WV‑entangled and
> GIS gateways, and WOAH identity services before reaching a pool of local models; all LLMs are
> exposed only via glass‑box HTTP services, grounded in West Virginia–specific memory.

---

## Status as of February 2026

| Category | Details |
|---|---|
| **Implemented now** | `jarvis-main-brain` → **127.0.0.1:8050** (confirmed `docker compose ps`). `jarvis-ollama` → **127.0.0.1:11434** (confirmed). `jarvis-wv-entangled-gateway` → **127.0.0.1:8010** (confirmed). `jarvis-spiritual-rag` → **127.0.0.1:8005** (confirmed; earlier plan documents called this port 8103 — see note below). `jarvis-gis-rag` → **127.0.0.1:8004** (confirmed). `nbb_woah_algorithms` → **127.0.0.1:8104** host → internal 8010 (confirmed). `jarvis-woah` → **127.0.0.1:7012** (confirmed; second distinct WOAH-related service). `jarvis-blood-brain-barrier` → **0.0.0.0:8016** (confirmed). `jarvis-20llm-production` → **127.0.0.1:8008** (confirmed). `jarvis-semaphore` (LLM proxy) → **127.0.0.1:8030** (confirmed). `llm1-proxy` through `llm22-proxy` → **127.0.0.1:8201–8222** (all confirmed). Judge services confirmed running: `jarvis-judge-truth` 7230, `jarvis-judge-consistency` 7231, `jarvis-judge-alignment` 7232, `jarvis-judge-ethics` 7233. `jarvis-constitutional-guardian` → **127.0.0.1:8091** (confirmed). `jarvis-fifth-dgm` → **127.0.0.1:4002** (confirmed). `jarvis-chroma` → **127.0.0.1:8002** (confirmed). `jarvis-redis` → **127.0.0.1:6380** (confirmed). Background autonomous learner wrappers operational as jobs capturing results into GISGEODB and Chroma. |
| **Partially implemented / scaffolded** | Per-request model breakdowns and per-model latency / error-rate metrics are logged but no dedicated debug endpoint exposes them yet. Ensemble decision rules are operational but not formally documented in a machine-readable schema. Autonomous learner does not expose a stable HTTP service interface; it runs as a daemon / job. WOAH-to-model-selection coupling exists conceptually but is not yet wired as an explicit routing rule in the main-brain configuration. |
| **Future work / design intent only** | Richer debug and metrics endpoints for per-request agent breakdowns. Formal documentation of ensemble decision rules. Tighter coupling between WOAH weights, Fifth DGM proposals, and model selection in high-stakes governance flows. Stable HTTP service interface for the autonomous learner aligned with main-brain routing patterns. |

> **Port correction — Spiritual Root / GBIM RAG:** Earlier planning documents (including the
> cumulative editing plan) listed this service at port **8103**. The confirmed `docker compose ps`
> output shows `jarvis-spiritual-rag` running at **127.0.0.1:8005**. All references in this
> chapter use port **8005**. Any chapter that references 8103 for this service should be updated
> to match. For the canonical description of how these services chain together in a live user
> chat, see **Chapter 17**. For full details on the 20-LLM + judge pipeline, see **Chapter 33**.

---

# 11. The LLM Fabric of Ms. Jarvis

This chapter describes the local language models that form the "LLM fabric" of Ms. Egeria Jarvis
and how they are woven into the broader GBIM, RAG, autonomous learning, and GeoDB architecture.
Rather than treating LLMs as independent agents, in the current deployment the system treats them
as constrained tools and judges embedded in a larger retrieval and belief stack that includes
Chroma, Redis, and the spatial body described in Chapter 6, all exposed through well-defined HTTP
services confirmed running as of February 2026.

---

## 11.1 Current Local LLM Inventory

In the current deployment, a substantial set of base and specialist models is served by Ollama,
running inside the `jarvis-ollama` container at **127.0.0.1:11434** (confirmed `docker compose
ps`). Figure 11.1 shows how these models are grouped and exposed collectively as the LLM fabric
behind the Ollama runtime.

**Core general-purpose models.** `llama3:latest` and `llama3.1:latest` are the primary
general-purpose reasoning models for rich, multi-step questions where high-quality synthesis is
important. `mistral:latest` is a fast, strong generalist for tightly scoped tasks where latency
matters. `llama2:latest` serves as a compatibility baseline for comparative experiments and legacy
flows. Chat-oriented variants include `vicuna:latest`, `openchat:latest`, `neural-chat:latest`,
`starling-lm:latest`, `zephyr:latest`, `qwen2:latest`, `orca-mini:latest`, `dolphin-phi:latest`,
`phi3:mini`, and `stablelm-zephyr:latest` for different tradeoffs of style, speed, and capacity.

**Code and data specialists.** `deepseek-coder:latest`, `codellama:latest`, `starcoder2:latest`,
and `sqlcoder:latest` are tuned for code generation, refactoring, and SQL.

**Multimodal and vision models.** `llava:latest` and `minicpm-v:latest` are available for image-
and vision-related tasks where enabled.

**Domain-specific and compact models.** `medllama2:latest` covers medical or clinical-style
language and reasoning. `tinyllama:latest`, `gemma:2b`, and `qwen2.5:1.5b` are smaller variants
for constrained environments and quick utility tasks.

All models are accessed via Ollama's HTTP interface and are called from FastAPI services in
`~/msjarvis-rebuild/services`, with model selection controlled through configuration and routing
logic rather than hard-coded choices. Not all installed models are active in every workflow, but
the fabric maintains this broader pool to support specialization and experimentation.

---

## 11.2 Roles of the Core and Specialist Models

In the current deployment, these models play distinct but overlapping roles.

**Core reasoning models (Llama 3 / Llama 3.1 / Mistral).** Default reasoning engines for
complex, multi-step questions that require integrating GBIM beliefs, Chroma semantic memory, and
GeoDB-backed spatial context. Used for higher-level narrative and reflective flows where
coherence, nuance, and robustness matter.

**Lightweight and utility models (TinyLlama, Gemma 2B, Qwen 2.5 1.5B, etc.).** Used for small,
bounded tasks, demos, quick rewrites, or scenarios where memory and CPU / GPU budgets are tight.
They serve as low-cost utility models for simple transformations and sanity checks.

**Compatibility and comparison models (Llama 2, chat variants).** Kept for comparison and
backwards compatibility with earlier experiments and agent designs. Useful when reproducing older
runs or benchmarking new strategies across model families.

**Code and SQL specialists.** `deepseek-coder`, `codellama`, `starcoder2`, and `sqlcoder` are
chosen when the task clearly involves code generation, refactoring, or database queries. Often
used in "judge" or "reviewer" roles to check or refine code produced by a general-purpose model.

**Multimodal and domain-specific models.** `llava` and `minicpm-v` are available for workflows
that involve images or multimodal prompts, where enabled. `medllama2` provides a specialized lens
for medical-style text, used cautiously and typically within constrained, advisory contexts.

These roles can change over time as models are upgraded or replaced, but the pattern of assigning
clear responsibilities, grouping models by capability, and avoiding uncontrolled model sprawl
remains central.

---

## 11.3 Service Topology and Ports

The following port assignments are drawn directly from `docker compose ps` (February 2026). Any
prior document that lists a different port for a service named here should be treated as outdated.

**Main Brain API — 127.0.0.1:8050 (`jarvis-main-brain`).** Primary external-facing interface for
questions, RAG-backed answers, and multi-step flows. Orchestrates calls to all downstream
services. For the complete `ultimatechat` execution path through this service, see **Chapter 17**.

**WV-Entangled Gateway — 127.0.0.1:8010 (`jarvis-wv-entangled-gateway`).** WV-biased,
multi-collection Chroma retrieval for entangled search workflows. Used by the main brain when
queries require Appalachian, benefits, or governance entanglement. For full details see
**Chapter 8**.

**Spiritual Root / GBIM RAG — 127.0.0.1:8005 (`jarvis-spiritual-rag`).** Exposes `/search` over
GBIM- and worldview-oriented Chroma collections. Earlier planning documents listed this service
at port 8103; the confirmed running port is **8005**. Serves as a core entry point into semantic
memory, including GBIM worldview entities and entangled spatial narratives.

**GIS RAG — 127.0.0.1:8004 (`jarvis-gis-rag`).** Spatially indexed `/search` over Chroma
collections and GeoDB mirrors. Used for explicitly spatial questions where PostGIS filtering and
spatial metadata are central.

**WOAH services — two distinct containers confirmed running.**
`nbb_woah_algorithms` maps **127.0.0.1:8104** (host) → internal 8010; this is the service the
Fifth DGM calls for identity-promotion decisions. `jarvis-woah` runs at **127.0.0.1:7012**. Both
are up and their respective roles are described further in Chapter 9 and Chapter 12.

**Blood-Brain Barrier — 0.0.0.0:8016 (`jarvis-blood-brain-barrier`).** Output guard and
truth-verdict service. All `ultimatechat` responses pass through BBB before being returned to the
caller.

**20-LLM Production Ensemble — 127.0.0.1:8008 (`jarvis-20llm-production`).** Current production
synthesis fabric. `llm20production` routes here as the default multi-model synthesis step. Proxy
at **127.0.0.1:8030** (`jarvis-semaphore`). Model proxies `llm1-proxy` through `llm22-proxy`
confirmed running at **127.0.0.1:8201–8222**. For full details see **Chapter 33**.

**Judge services — four containers confirmed running.** `jarvis-judge-truth` at 7230,
`jarvis-judge-consistency` at 7231, `jarvis-judge-alignment` at 7232, `jarvis-judge-ethics` at
7233. If any judge service is down, the main brain falls back to the 20-LLM answer and marks
consensus metrics as degraded. See **Chapter 33**.

**Constitutional Guardian — 127.0.0.1:8091 (`jarvis-constitutional-guardian`).** Confirmed
running. See **Chapter 37** for full details.

**Fifth DGM — 127.0.0.1:4002 (`jarvis-fifth-dgm`).** Confirmed running. See **Chapter 9**.

**Ollama Runtime — 127.0.0.1:11434 (`jarvis-ollama`).** Model-serving runtime hosting the local
LLMs listed in §11.1. Not directly exposed to users; only internal services call it.

> **Note on earlier drafts:** The cumulative editing plan listed "Spiritual Root / GBIM RAG →
> 8103." The running system uses **port 8005** for this service. All other port assignments
> above match the plan and are confirmed by `docker compose ps`.

---

## 11.4 Coordination Between Main Brain, RAG, Entangled Search, WOAH, and the LLM Fabric

The steps below describe the coordination pattern as seen from this chapter. For the
authoritative, step-by-step account of the full `ultimatechat` flow see **Chapter 17**.

**User-facing queries via main brain on port 8050.** The main brain receives a request, calls the
Spiritual Root / GBIM RAG gateway on port **8005** `/search` to retrieve semantically relevant
documents from Chroma, and for WV-entangled queries consults the WV-entangled gateway on port
**8010**. Where needed it incorporates identity weights from `nbb_woah_algorithms` on port
**8104**. It then routes through `jarvis-20llm-production` on port **8008** for ensemble
synthesis, followed by the judge services (7230–7233), and passes the result through BBB on port
**8016** before returning a structured response to the caller. For some tasks it may invoke a
secondary specialist model to review or refine the primary output.

**Background and autonomous-style learning flows.** In the current deployment, background learners
select topics from configured queues or from I-container interests, using helper modules such as
`autonomous_learner_topic_source.py`. They call the Spiritual Root RAG on port 8005 and, when
available, web-research or other external sources. The middleware
`autonomous_learner_gisgeodb_wrapper.py` intercepts queries and stores summaries and search
results into GISGEODB and Chroma, treating autonomous learning as a logged, inspectable process.
Entanglement scaffolding and topic graphs are updated to bias future topic selection toward
WV-relevant and identity-relevant themes (see **Chapter 8**).

In both flows, LLMs are the final step in a pipeline that has already grounded context in
semantic memory, spatial features, entangled retrieval, and identity weights. The LLM fabric is
treated as a pool of tools and judges, not as an unconstrained monolithic agent.

---

## 11.5 LLMs in Consciousness, Autonomy, and Ensembles

**Consciousness coordinator.** The design intends that a consciousness coordinator will aggregate
beliefs, experiences, WOAH-driven identity signals, and derived structures from autonomous
learning and entanglement graphs, then use a primary LLM to synthesize higher-level narratives.
In the current deployment, this role is partly realized through the `prefrontal-planner` and
`icontainers-identity` layers visible in the `consciousnesslayers` field of `UltimateResponse`
(confirmed active on 2026-02-15; see Chapter 9 §9.3.5), but it is not yet a discrete, separately
running service. See **Chapters 12 and 25** for the neurobiological and identity dimensions of
this coordination.

**Direct RAG endpoints.** In the current deployment, HTTP APIs for "question + context" flows
bypass heavier orchestration when only retrieval and a single model call are needed. These
typically use Mistral or Llama 3.* models, with strict timeouts and structured error handling
around RAG and search calls.

**Ensemble and judge patterns.** `llm20production` is the production ensemble fabric. The main
brain routes through the 20-LLM ensemble on port 8008 followed by the judge services
(7230–7233). If any judge service is down, the main brain falls back to the 20-LLM answer and
marks consensus metrics as degraded. For full details see **Chapter 33**.

**Autonomous outward communication.** The design intends that scheduled or event-driven flows
will request fresh narratives or assessments from the LLM fabric for reports or public updates,
gated by configuration and safeguards. In the current deployment, external posting is not yet
automated; this remains future work.

Across these uses, LLMs act as compositional engines over already-filtered inputs from Chroma,
GeoDB, GBIM, and identity services, subject to explicit timeouts, ensemble checks, and
service-level constraints.

---

## 11.6 Operational Constraints and Fabric Behavior

**Resource and disk constraints.** Model files under `~/.ollama/models` are large; more than
twenty models are installed, but only a subset are actively used in core flows at any given time.
Heavy RAG / Chroma use, entangled multi-collection search, identity evaluation, and LLM inference
share CPU, memory, and disk bandwidth; orchestration avoids overlapping the most expensive
operations when possible.

**Model routing and selection.** The main brain and related services select models based on task
type. Routing is configuration-driven: updating or swapping a model can be done without changing
core orchestration code.

**Ensemble usage patterns.** Simple ensembles (primary + judge) are used where correctness
matters more than speed. Logs and traces record which models were used for each request, enabling
per-model latency, error rates, and ensemble outcomes to be analyzed. A dedicated debug endpoint
exposing these breakdowns per-request is identified as near-term work.

**Timeouts and fault handling.** In the current deployment, calls to RAG, entangled search,
identity services, and Ollama are wrapped with timeouts. Services are managed so they can be
restarted independently. When upstream services fail, the LLM fabric surfaces clear error
responses. If the judge services are down, the main brain falls back to the 20-LLM answer and
marks consensus metrics as degraded.

The effect is an LLM fabric that behaves more like a set of specialized tools behind APIs than a
single monolithic "brain," even though these models collectively underpin many of Ms. Jarvis's
reasoning capabilities.

---

## 11.7 Implementation Notes (Reality Alignment)

The following service-to-port mapping is authoritative for this chapter, drawn from `docker
compose ps` on the development host `cakidd-Legion-5-16IRX9`, February 2026:

- `jarvis-main-brain` → **127.0.0.1:8050**
- `jarvis-wv-entangled-gateway` → **127.0.0.1:8010**
- `jarvis-spiritual-rag` → **127.0.0.1:8005** *(earlier plan said 8103; 8005 is correct)*
- `jarvis-gis-rag` → **127.0.0.1:8004**
- `nbb_woah_algorithms` → **127.0.0.1:8104** host → internal 8010
- `jarvis-woah` → **127.0.0.1:7012**
- `jarvis-blood-brain-barrier` → **0.0.0.0:8016**
- `jarvis-20llm-production` → **127.0.0.1:8008**
- `jarvis-semaphore` (LLM proxy) → **127.0.0.1:8030**
- `llm1-proxy` through `llm22-proxy` → **127.0.0.1:8201–8222**
- Judge services → 7230, 7231, 7232, 7233
- `jarvis-constitutional-guardian` → **127.0.0.1:8091**
- `jarvis-fifth-dgm` → **127.0.0.1:4002**
- `jarvis-chroma` → **127.0.0.1:8002**
- `jarvis-redis` → **127.0.0.1:6380**
- `jarvis-ollama` → **127.0.0.1:11434**

In the current deployment, background autonomous learning capabilities exist as Python services
and wrappers (`ms_jarvis_autonomous_learner_optimized.py` and
`autonomous_learner_gisgeodb_wrapper.py`) that run as jobs or daemons, capturing results into
GISGEODB and Chroma. The design intends that as the system stabilizes these learners will converge
toward a consistently exposed service interface aligned with main-brain routing patterns; a stable
HTTP port for the autonomous learner is identified as near-term work.

For cross-reference: the authoritative description of how all of these services chain together in
a single live user chat is in **Chapter 17**. Full details on the 20-LLM + judge pipeline stack
that `llm20production` uses are in **Chapter 33**. The neurobiological master service
(`jarvis-neurobiological-master`, port 8018, confirmed running) and its relationship to the LLM
fabric are covered in **Chapter 12**.
