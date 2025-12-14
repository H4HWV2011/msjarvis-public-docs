# 11. The LLM Fabric of Ms. Jarvis

This chapter describes the local language models that form the “LLM fabric” of Ms. Egeria Jarvis and how they are woven into the broader GBIM, RAG, autonomous learning, and GeoDB architecture. Rather than treating LLMs as independent agents, the system treats them as constrained tools and judges embedded in a larger retrieval and belief stack that includes Chroma, Redis, and the spatial body described in Chapter 6, all exposed through well-defined HTTP services.

## 11.1 Current Local LLM Inventory

The current deployment uses a substantial set of base and specialist models served by Ollama, running inside the `jarvis-ollama` container and exposed on port `11434`. These models fall into several families:

- **Core general-purpose models**
  - `llama3:latest`, `llama3.1:8b` – primary general-purpose reasoning models for rich, multi-step questions where high-quality synthesis is important.
  - `mistral:latest` – fast, strong generalist for tightly scoped tasks where latency matters.
  - `llama2:latest` – compatibility baseline for comparative experiments and legacy flows.
  - Chat-oriented variants such as `vicuna:latest`, `openchat:latest`, `neural-chat:latest`, `starling-lm:latest`, `zephyr:latest`, `qwen2:latest`, `orca-mini:latest`, `dolphin-phi:latest`, `phi:latest`, and `phi3:mini` for different tradeoffs of style, speed, and capacity.

- **Code and data specialists**
  - `deepseek-coder:latest`, `codellama:latest`, `starcoder2:latest`, `sqlcoder:latest` – tuned for code generation, refactoring, and SQL.

- **Multimodal and vision models**
  - `llava:latest`, `bakllava:latest`, `minicpm-v:latest` – for image- and vision-related tasks where enabled.

- **Domain-specific and compact models**
  - `medllama2:latest` – for medical or clinical-style language and reasoning.
  - `tinyllama:latest`, `tinyllama:1.1b`, `gemma:2b` – smaller variants for constrained environments and quick utility tasks.

All models are accessed via Ollama’s HTTP interface and are called from FastAPI services in `~/msjarvis-rebuild/services`, with model selection controlled through configuration and routing logic rather than hard-coded choices. Not all installed models are active in every workflow, but the fabric maintains this broader pool to support specialization and experimentation.

## 11.2 Roles of the Core and Specialist Models

Within Ms. Jarvis, these models play distinct but overlapping roles:

**Core reasoning models (Llama 3 / Llama 3.1 / Mistral)**

- Default reasoning engines for complex, multi-step questions that require integrating GBIM beliefs, Chroma semantic memory, and GeoDB-backed spatial context.
- Used for higher-level narrative and reflective flows where coherence, nuance, and robustness matter.

**Lightweight and utility models (Phi, TinyLlama, Gemma 2B, etc.)**

- Used for small, bounded tasks, demos, quick rewrites, or scenarios where memory and CPU/GPU budgets are tight.
- Serve as inexpensive utility models for simple transformations and sanity checks.

**Compatibility and comparison models (Llama 2, chat variants)**

- Kept for comparison and backwards compatibility with earlier experiments and agent designs.
- Useful when reproducing older runs or benchmarking new strategies across model families.

**Code and SQL specialists**

- `deepseek-coder`, `codellama`, `starcoder2`, and `sqlcoder` are chosen when the task clearly involves code generation, refactoring, or database queries.
- Often used in “judge” or “reviewer” roles to check or refine code produced by a general-purpose model.

**Multimodal and domain-specific models**

- `llava`, `bakllava`, and `minicpm-v` are available for workflows that involve images or multimodal prompts, where enabled.
- `medllama2` provides a specialized lens for medical-style text, used cautiously and typically within constrained, advisory contexts.

These roles can change over time as models are upgraded or replaced, but the pattern of assigning clear responsibilities, grouping models by capability, and avoiding uncontrolled model sprawl remains central.

## 11.3 Service Topology and Ports

The LLM fabric is exposed through several cooperating services, each bound to a distinct port:

- **ULTIMATE Ms. Jarvis API (8051)**  
  - Primary external-facing interface for questions, RAG-backed answers, and multi-step flows.  
  - Orchestrates calls to RAG, web research, the LLM fabric (including ensembles and judges), and downstream tools, then routes to Ollama models as needed.

- **Autonomous Learner (8053)**  
  - Optimized autonomous learning service that cycles every 5 minutes.  
  - Pulls topics from a configured learning queue, calls RAG and web-research, summarizes and deduplicates, updates the entanglement topic graph, and writes unique items into semantic memory.

- **RAG / Hilbert-Space Gateway (8103)**  
  - Minimal RAG HTTP service that exposes `/search` over Chroma collections.  
  - Serves as the front door into semantic memory, including thesis texts, MountainShares documents, autonomous-learning outputs, and specialized collections (such as `geodb_*`).

- **Web-Research Service (8009)**  
  - HTTP service that executes web search and scraping workflows.  
  - Used both by ULTIMATE and by the autonomous learner when external information is needed.

- **Ollama Runtime (11434)**  
  - Model-serving runtime hosting the local LLMs listed above.  
  - Not directly exposed to users; only the internal services call it.

This separation ensures that each concern—reasoning, retrieval, web access, autonomous learning, and model serving—can be monitored, restarted, and evolved independently.

## 11.4 Coordination Between ULTIMATE, RAG, Web, Learner, and the LLM Fabric

The main coordination flows look like this:

### User-facing queries (via ULTIMATE on 8051)

1. ULTIMATE receives a request (question, task, or API call).
2. It calls the RAG service on `8103 /search` to retrieve semantically relevant documents and notes from Chroma collections (including `geodb_*` for spatial context when needed).
3. It optionally calls the web-research service on `8009 /search` to fetch current information from the internet.
4. It fuses RAG and web results into a structured context block.
5. It chooses an appropriate model or model pair from the LLM fabric (for example, Llama 3.1 for primary reasoning, or a code model for code-specific tasks) and sends a prompt to Ollama on `11434`.
6. For some tasks, it may invoke a secondary “judge” model to review or critique the primary output before returning a result.
7. It post-processes the model’s output and returns a structured JSON or text response.

### Autonomous learning cycles (via learner on 8053)

1. Every 300 seconds, the learner selects the next topic from its `learning_queue` (with planned bias from the entanglement topic graph).
2. It calls the RAG service on `8103 /search` to retrieve internal knowledge related to that topic.
3. It calls the web-research service on `8009 /search` for external results; some topics may yield zero web hits.
4. It summarizes and semantically deduplicates the combined results, using its own embedding model and similarity thresholds.
5. It stores unique items into Chroma collections (such as `autonomous_learning` and `research_history`) via the RAG/Chroma layer.
6. It updates its entanglement scaffolding (topic graph) and schedules the next cycle.

In both flows, LLMs are the final step in a pipeline that has already grounded context in semantic memory and, when relevant, in spatial features and external web data. The LLM fabric is treated as a pool of tools and judges, not as an unconstrained monolithic agent.

## 11.5 LLMs in Consciousness, Autonomy, and Ensembles

Within higher-level “consciousness” and autonomy constructs, the LLM fabric is used as a narrative and reasoning engine, often in ensemble patterns:

**Consciousness coordinator (conceptual role)**

- Aggregates beliefs, experiences, and derived signals (for example, from autonomous learning and entanglement graphs).
- Calls into RAG and, when needed, web-research to assemble a “state of mind” context.
- Uses a primary LLM (typically a Llama 3–class model) to synthesize higher-level narratives (for example, reflections, status summaries, or strategic considerations).

**Direct RAG endpoints**

- Expose HTTP APIs for “question + context” flows that bypass heavier orchestration when only retrieval and a single model call are needed.
- Often use Mistral or Llama 3.* models, with strict timeouts and structured error handling around RAG and web calls.

**Ensemble and judge patterns**

- For some higher-stakes or specialized tasks, ULTIMATE uses a two-step pattern:
  - A primary model drafts an answer (for example, Llama 3.1).
  - A secondary specialist or judge model (for example, a code model, SQL model, or a different chat model) reviews the draft, flags issues, or proposes corrections.
- The orchestration logic then merges, selects, or rejects outputs based on these internal checks, optionally deferring to a simpler fallback if disagreement or uncertainty is high.

**Autonomous outward communication (planned and constrained)**

- Scheduled or event-driven flows may request a fresh narrative or assessment from the LLM fabric (for example, for reports or public updates).
- Any external posting (social media, reports, alerts) is gated by configuration and safeguards and uses RAG-grounded context to avoid hallucinated claims.

Across these uses, LLMs act as compositional engines over already-filtered inputs from Chroma, GeoDB, and other stores, subject to explicit timeouts, ensemble checks, and service-level constraints.

## 11.6 Operational Constraints and Fabric Behavior

The LLM fabric operates under real resource and reliability constraints, which shape ensemble behavior and routing:

**Resource and disk constraints**

- Model files under `~/.ollama/models` are large; more than twenty models are installed, but only a subset are actively used in core flows at any given time.
- Heavy RAG/Chroma use and LLM inference share CPU, memory, and disk bandwidth; orchestration avoids overlapping the most expensive operations when possible.

**Model routing and selection**

- ULTIMATE and related services can select models based on task type (for example, short explanation vs multi-step reasoning vs code generation vs SQL vs multimodal).
- Routing is configuration-driven: updating or swapping a model (for example, moving from Llama 3 to Llama 3.1) can be done without changing core orchestration logic.

**Ensemble usage patterns**

- Simple ensembles (primary + judge) are used where correctness matters more than speed, such as code or data-related tasks.
- Logs and traces include which models were used for each request, enabling per-model latency, error rates, and ensemble outcomes to be analyzed in the operational evaluation chapter.

**Timeouts and fault handling**

- All calls to RAG, web, and Ollama are wrapped with timeouts.
- Services are managed so they can be restarted independently if one component (for example, web-research or RAG) becomes unavailable.
- When upstream services fail, the LLM fabric surfaces clear error responses rather than partial or hallucinated outputs.

The effect is an LLM fabric that behaves more like a set of specialized tools behind APIs than a single monolithic “brain,” even though these models collectively underpin many of Ms. Jarvis’s reasoning capabilities.

## 11.7 Implementation Notes (Reality Alignment)

In the current deployment, the main LLM orchestration and higher-level API run in a FastAPI-based service bound to port `8051` (ULTIMATE), typically managed alongside other services in `~/msjarvis-rebuild/services`. The autonomous learner runs on port `8053`, calling RAG (`8103`) and web-research (`8009`) on a fixed five-minute schedule to grow semantic memory and entanglement structures. The RAG service on port `8103` exposes `/search` over Chroma collections, acting as the primary Hilbert-space gateway. The web-research service on port `8009` exposes `/search` for external data acquisition. The Ollama runtime on port `11434` hosts the concrete LLMs used by all of the above services, including both core generalists and specialists.

> Status: This chapter describes the current LLM fabric as a production but evolving set of services. Future work includes richer debug and metrics endpoints (for example, per-request agent breakdown in `llm_bridge`), more explicit documentation of ensemble decision rules, and tighter coupling between WOAH weights, DGM proposals, and model selection in high-stakes governance flows.
