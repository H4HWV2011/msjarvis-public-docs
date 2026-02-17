> **Why this matters for Polymathmatic Geography**  
> This chapter shows how Ms. Jarvis’s “thinking” is implemented as an organized fabric of local language models rather than a single opaque model. It supports:  
> - **P1 – Every where is entangled** by embedding LLMs inside a retrieval and spatial stack (Chroma, GBIM, GeoDB) that keeps reasoning tied to concrete places and institutions.  
> - **P3 – Power has a geometry** by routing questions through specific models, memories, and services whose connections can be inspected and redesigned.  
> - **P5 – Design is a geographic act** by treating model choice, ensemble wiring, and service topology as design decisions that change how Appalachian realities are seen and narrated.  
> - **P12 – Intelligence with a ZIP code** by grounding LLM calls in West Virginia–specific semantic and geospatial memory rather than generic, placeless prompts.  
> - **P16 – Power accountable to place** by exposing LLMs only through glass‑box HTTP services that can be logged, audited, and constrained, not as hidden backends with direct user access.  
> As such, this chapter belongs to the **Computational Instrument** tier: it specifies the model pool and service fabric that turn Quantarithmia’s spatial‑justice instruments into live, language-facing behavior.

<img width="1100" height="900" alt="unnamed(16)" src="https://github.com/user-attachments/assets/ae0d8496-798d-4048-adbd-90d4fcc30b67" />

>Figure 11.1. The LLM fabric of Ms. Jarvis: user queries flow through RAG, WV‑entangled and GIS gateways, and WOAH identity services before reaching a pool of local models; all LLMs are exposed only via glass‑box HTTP services, grounded in West Virginia–specific memory.​


# 11. The LLM Fabric of Ms. Jarvis

This chapter describes the local language models that form the “LLM fabric” of Ms. Egeria Jarvis and how they are woven into the broader GBIM, RAG, autonomous learning, and GeoDB architecture. Rather than treating LLMs as independent agents, the system treats them as constrained tools and judges embedded in a larger retrieval and belief stack that includes Chroma, Redis, and the spatial body described in Chapter 6, all exposed through well-defined HTTP services.

---

## 11.1 Current Local LLM Inventory

The current deployment uses a substantial set of base and specialist models served by Ollama, running inside the `jarvis-ollama` container and exposed on port `11434`. Figure 11.1 shows how these models are grouped and exposed collectively as the LLM fabric behind the Ollama runtime. These models fall into several families:

- **Core general-purpose models**  
  - `llama3:latest`, `llama3.1:latest` – primary general-purpose reasoning models for rich, multi-step questions where high-quality synthesis is important.  
  - `mistral:latest` – fast, strong generalist for tightly scoped tasks where latency matters.  
  - `llama2:latest` – compatibility baseline for comparative experiments and legacy flows.  
  - Chat-oriented variants such as `vicuna:latest`, `openchat:latest`, `neural-chat:latest`, `starling-lm:latest`, `zephyr:latest`, `qwen2:latest`, `orca-mini:latest`, `dolphin-phi:latest`, `phi3:mini`, and `stablelm-zephyr:latest` for different tradeoffs of style, speed, and capacity.

- **Code and data specialists**  
  - `deepseek-coder:latest`, `codellama:latest`, `starcoder2:latest`, `sqlcoder:latest` – tuned for code generation, refactoring, and SQL.

- **Multimodal and vision models**  
  - `llava:latest`, `minicpm-v:latest` – for image- and vision-related tasks where enabled.

- **Domain-specific and compact models**  
  - `medllama2:latest` – for medical or clinical-style language and reasoning.  
  - `tinyllama:latest`, `gemma:2b`, `qwen2.5:1.5b` – smaller variants for constrained environments and quick utility tasks.

All models are accessed via Ollama’s HTTP interface and are called from FastAPI services in `~/msjarvis-rebuild/services`, with model selection controlled through configuration and routing logic rather than hard-coded choices. Not all installed models are active in every workflow, but the fabric maintains this broader pool to support specialization and experimentation.

---

## 11.2 Roles of the Core and Specialist Models

Within Ms. Jarvis, these models play distinct but overlapping roles:

**Core reasoning models (Llama 3 / Llama 3.1 / Mistral)**

- Default reasoning engines for complex, multi-step questions that require integrating GBIM beliefs, Chroma semantic memory, and GeoDB-backed spatial context.  
- Used for higher-level narrative and reflective flows where coherence, nuance, and robustness matter.

**Lightweight and utility models (TinyLlama, Gemma 2B, Qwen 2.5 1.5B, etc.)**

- Used for small, bounded tasks, demos, quick rewrites, or scenarios where memory and CPU/GPU budgets are tight.  
- Serve as inexpensive utility models for simple transformations and sanity checks.

**Compatibility and comparison models (Llama 2, chat variants)**

- Kept for comparison and backwards compatibility with earlier experiments and agent designs.  
- Useful when reproducing older runs or benchmarking new strategies across model families.

**Code and SQL specialists**

- `deepseek-coder`, `codellama`, `starcoder2`, and `sqlcoder` are chosen when the task clearly involves code generation, refactoring, or database queries.  
- Often used in “judge” or “reviewer” roles to check or refine code produced by a general-purpose model.

**Multimodal and domain-specific models**

- `llava` and `minicpm-v` are available for workflows that involve images or multimodal prompts, where enabled.  
- `medllama2` provides a specialized lens for medical-style text, used cautiously and typically within constrained, advisory contexts.

These roles can change over time as models are upgraded or replaced, but the pattern of assigning clear responsibilities, grouping models by capability, and avoiding uncontrolled model sprawl remains central.

---

## 11.3 Service Topology and Ports

The LLM fabric is exposed through several cooperating services, each bound to a distinct port:

- **Main Brain API (8050)**  
  - Primary external-facing interface for questions, RAG-backed answers, and multi-step flows.  
  - Orchestrates calls to RAG, WV-entangled gateways, WOAH, the LLM fabric (including ensembles and judges), and downstream tools, then routes to Ollama models as needed.

- **WV-Entangled Gateway (8010)**  
  - Gateway that provides WV-biased, multi-collection Chroma retrieval for entangled search workflows.  
  - Used by the main brain and related services when queries require Appalachian, benefits, or governance entanglement.

- **Spiritual Root / Hilbert-Space Gateway (8103)**  
  - RAG HTTP service mapped to `127.0.0.1:8103`, exposing `/search` over GBIM- and worldview-oriented Chroma collections.  
  - Serves as a core entry point into semantic memory, including GBIM worldview entities and entangled spatial narratives.

- **GIS RAG Service (8004)**  
  - GIS-focused RAG HTTP service exposing spatially indexed `/search` over Chroma collections and GeoDB mirrors.  
  - Used for explicitly spatial questions where PostGIS filtering and spatial metadata are central.

- **WOAH Algorithms Service (8104)**  
  - Identity-weighting and population-dynamics service that evaluates content for hierarchical importance and identity relevance.  
  - Supplies weights to Fifth DGM and other introspective components, indirectly influencing which content is privileged in memory and identity.

- **Ollama Runtime (11434)**  
  - Model-serving runtime hosting the local LLMs listed above.  
  - Bound to `127.0.0.1:11434` and not directly exposed to users; only internal services call it.

Additional services such as the unified gateway, blood–brain barrier, qualia engine, and consciousness bridge participate in the broader orchestration but are described in more detail in other chapters. As illustrated in Figure 11.1, user queries hit the main brain on port 8050, which then coordinates RAG gateways, WOAH, and the Ollama-backed LLM fabric on 11434. The focus here is on how the main brain and retrieval gateways coordinate with the LLM fabric.

---

## 11.4 Coordination Between Main Brain, RAG, Entangled Search, WOAH, and the LLM Fabric

The steps below correspond to the vertical flow from user queries to the LLM Fabric and back in Figure 11.1. The main coordination flows look like this:

### User-facing queries (via main brain on 8050)

1. The main brain receives a request (question, task, or API call), potentially annotated with WV county, ZIP, or governance context.  
2. It calls the RAG gateway on `8103 /search` to retrieve semantically relevant documents and notes from Chroma collections, including GBIM worldview entities and WV benefits mirrors when appropriate.  
3. For WV-entangled queries, it consults the WV-entangled gateway on `8010`, which aggregates across multiple collections using WV-first biasing and entanglement envelopes.  
4. Where needed, it incorporates identity weights and categories from the WOAH algorithms service to modulate which memories and narratives are emphasized.  
5. It chooses an appropriate model or model pair from the LLM fabric (for example, Llama 3.1 for primary reasoning, or a code model for code-specific tasks) and sends a prompt to Ollama on `11434`.  
6. For some tasks, it may invoke a secondary “judge” or specialist model to review or critique the primary output before returning a result.  
7. It passes results through intermediate services such as the qualia engine and blood–brain barrier, then returns a structured JSON or text response to the caller.

### Background and autonomous-style learning flows

1. Background learners and tools select topics from configured queues or from I-container interests, using helper modules such as `autonomous_learner_topic_source.py`.  
2. They call RAG (`8103`) and, when available, web-research or other external sources to gather material.  
3. Middleware such as `autonomous_learner_gisgeodb_wrapper.py` intercepts queries and stores summaries and search results into GISGEODB and Chroma, treating autonomous learning as a logged, inspectable process.  
4. Entanglement scaffolding and topic graphs are updated to bias future topic selection toward WV-relevant and identity-relevant themes.

In both flows, LLMs are the final step in a pipeline that has already grounded context in semantic memory, spatial features, entangled retrieval, and, when appropriate, identity weights. The LLM fabric is treated as a pool of tools and judges, not as an unconstrained monolithic agent.

---

## 11.5 LLMs in Consciousness, Autonomy, and Ensembles

Within higher-level “consciousness” and autonomy constructs, the LLM fabric is used as a narrative and reasoning engine, often in ensemble patterns.

**Consciousness coordinator (conceptual role)**

- Aggregates beliefs, experiences, WOAH-driven identity signals, and derived structures from autonomous learning and entanglement graphs.  
- Calls into RAG, GIS-aware RAG, WV-entangled search, and, when needed, external research to assemble a rich “state of mind” context.  
- Uses a primary LLM (typically a Llama 3–class model) to synthesize higher-level narratives such as reflections, status summaries, or strategic considerations.

**Direct RAG endpoints**

- Expose HTTP APIs for “question + context” flows that bypass heavier orchestration when only retrieval and a single model call are needed.  
- Often use Mistral or Llama 3.* models, with strict timeouts and structured error handling around RAG and search calls.

**Ensemble and judge patterns**

- For higher-stakes or specialized tasks, the main brain uses a two-step pattern:  
  - A primary model drafts an answer (for example, Llama 3.1).  
  - A secondary specialist or judge model (for example, a code model, SQL model, or a different chat model) reviews the draft, flags issues, or proposes corrections.  
- Orchestration logic then merges, selects, or rejects outputs based on these internal checks, and may fall back to a simpler route if disagreement or uncertainty is high.

**Autonomous outward communication (planned and constrained)**

- Scheduled or event-driven flows may request fresh narratives or assessments from the LLM fabric (for example, for reports or public updates).  
- External posting (social media, reports, alerts) is gated by configuration and safeguards and uses GBIM-, GeoDB-, and RAG-grounded context to avoid hallucinated claims.

Across these uses, LLMs act as compositional engines over already-filtered inputs from Chroma, GeoDB, GBIM, and identity services, subject to explicit timeouts, ensemble checks, and service-level constraints.

---

## 11.6 Operational Constraints and Fabric Behavior

The LLM fabric operates under real resource and reliability constraints, which shape ensemble behavior and routing:

**Resource and disk constraints**

- Model files under `~/.ollama/models` are large; more than twenty models are installed, but only a subset are actively used in core flows at any given time.  
- Heavy RAG/Chroma use, entangled multi-collection search, identity evaluation, and LLM inference share CPU, memory, and disk bandwidth; orchestration avoids overlapping the most expensive operations when possible.

**Model routing and selection**

- The main brain and related services select models based on task type (for example, short explanation vs multi-step reasoning vs code generation vs SQL vs multimodal).  
- Routing is configuration-driven: updating or swapping a model (for example, moving from `llama3:latest` to `llama3.1:latest`) can be done without changing core orchestration code.

**Ensemble usage patterns**

- Simple ensembles (primary + judge) are used where correctness matters more than speed, such as code or data-related tasks.  
- Logs and traces indicate which models were used for each request, enabling per-model latency, error rates, and ensemble outcomes to be analyzed in operational evaluation work.

**Timeouts and fault handling**

- Calls to RAG, entangled search, identity services, and Ollama are wrapped with timeouts.  
- Services are managed so they can be restarted independently if one component (for example, a gateway or identity service) becomes unavailable.  
- When upstream services fail, the LLM fabric surfaces clear error responses rather than partial or hallucinated outputs.

The effect is an LLM fabric that behaves more like a set of specialized tools behind APIs than a single monolithic “brain,” even though these models collectively underpin many of Ms. Jarvis’s reasoning capabilities.

---

## 11.7 Implementation Notes (Reality Alignment)

In the current deployment, the main LLM orchestration and higher-level API run in a FastAPI-based service bound to port `8050` (`jarvis-main-brain`), typically managed alongside other services in `~/msjarvis-rebuild`. The WV-entangled gateway runs on port `8010`, providing WV-biased multi-collection retrieval. The spiritual-root RAG gateway is mapped to `127.0.0.1:8103`, exposing `/search` over worldview-oriented Chroma collections. GIS RAG runs on port `8004`, focusing on spatially indexed retrieval. The WOAH algorithms service is mapped to `127.0.0.1:8104`, providing identity weights and population dynamics to the rest of the stack. The Ollama runtime on port `11434` hosts the concrete LLMs used by these services, including both core generalists and specialists, and is reachable only from within the Docker network and the host loopback interface.

Background autonomous learning capabilities exist as Python services and wrappers (for example, `ms_jarvis_autonomous_learner_optimized.py` and `autonomous_learner_gisgeodb_wrapper.py`) that can be run as jobs or daemons, capturing results into GISGEODB and Chroma, even when no dedicated HTTP port is exposed. As the system stabilizes, these learners are expected to converge toward a more consistently exposed service interface aligned with the main brain’s routing patterns.

> **Status:** This chapter describes the current LLM fabric as a production but evolving set of services and workers. Future work includes richer debug and metrics endpoints (for example, per-request agent breakdowns in the main brain), more explicit documentation of ensemble decision rules, and tighter coupling between WOAH weights, Fifth DGM proposals, and model selection in high-stakes governance flows.
