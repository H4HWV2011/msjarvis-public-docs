# 11. The LLM Fabric of Ms. Jarvis

This chapter describes the local language models that form the “LLM fabric” of Ms. Egeria Jarvis and how they are woven into the broader GBIM, RAG, autonomous learning, and GeoDB architecture. Rather than treating LLMs as independent agents, the system treats them as constrained tools and judges embedded in a larger retrieval and belief stack that includes Chroma, Redis, and the spatial body described in Chapter 6, all exposed through well-defined HTTP services.

## 11.1 Current Local LLM Inventory

The current deployment uses a finite set of base models served by Ollama, running inside the `jarvis-ollama` container and exposed on port `11434`:

- **Llama 3** – primary general-purpose reasoning model for rich, multi-step questions where high-quality synthesis is important.
- **Mistral** – faster, smaller-footprint expert for tightly scoped tasks where latency matters more than maximum capacity.
- **Llama 2** – compatibility baseline for comparative experiments and legacy flows.
- **Phi** – compact reasoning model for lighter tasks, demos, or constrained scenarios.

All models are accessed via Ollama’s HTTP interface and are called from FastAPI services in `~/msjarvis-rebuild/services`, with model selection controlled through configuration rather than hard-coded choices. Additional models (such as Gemma, Qwen2, Mixtral, and others) have been downloaded and used for specialized roles in the past, but the active local set is intentionally kept small for operational stability.

## 11.2 Roles of the Core Models

Within Ms. Jarvis, these models play distinct roles:

**Llama 3**

- Default reasoning model for complex, multi-step questions that require integrating GBIM beliefs, Chroma semantic memory, and GeoDB-backed spatial context.
- Often used for higher-level narrative and reflective flows where coherence and nuance matter.

**Mistral**

- Used for faster, resource-efficient tasks such as short explanations, quick checks, small-code generation, and lightweight RAG over limited context.
- Preferred where low latency and reduced GPU usage are more important than maximum capacity.

**Llama 2**

- Kept primarily for comparison and backwards compatibility with earlier experiments and agent designs.
- Useful when reproducing older runs or benchmarking new strategies.

**Phi**

- Used for small, bounded tasks, demos, or scenarios where memory and CPU budgets are tight.
- Serves as an inexpensive “utility” model for simple transformations and sanity checks.

These roles can change over time as models are upgraded or replaced, but the pattern of assigning clear responsibilities and avoiding model sprawl remains central.

## 11.3 Service Topology and Ports

The LLM fabric is exposed through several cooperating services, each bound to a distinct port:

- **ULTIMATE Ms. Jarvis API (8051)**  
  - Primary external-facing interface for questions, RAG-backed answers, and multi-step flows.  
  - Orchestrates calls to RAG, web research, ensemble logic, and downstream tools, then routes to Ollama models as needed.

- **Autonomous Learner (8053)**  
  - Optimized autonomous learning service that cycles every 5 minutes.  
  - Pulls topics from a configured learning queue, calls RAG and web-research, summarizes and deduplicates, and writes back into semantic memory.

- **RAG / Hilbert-Space Gateway (8103)**  
  - Minimal RAG HTTP service that exposes `/search` over Chroma collections.  
  - Serves as the front door into semantic memory, including thesis texts, MountainShares documents, auto-stored answers, and specialized collections (such as `geodb_*`).

- **Web-Research Service (8009)**  
  - HTTP service that executes web search and scraping workflows.  
  - Used both by ULTIMATE and by the autonomous learner when external information is needed.

- **Ollama Runtime (11434)**  
  - Model-serving runtime hosting the local LLMs (Llama 3, Mistral, Llama 2, Phi).  
  - Not directly exposed to users; only the internal services call it.

This separation ensures that each concern—reasoning, retrieval, web access, autonomous learning, and model serving—can be monitored, restarted, and evolved independently.

## 11.4 Coordination Between ULTIMATE, RAG, Web, and Learner

The main coordination flows look like this:

### User-facing queries (via ULTIMATE on 8051)

1. ULTIMATE receives a request (question, task, or API call).
2. It calls the RAG service on `8103 /search` to retrieve semantically relevant documents and notes from Chroma collections (including `geodb_*` for spatial context when needed).
3. It optionally calls the web-research service on `8009 /search` to fetch current information from the internet.
4. It fuses RAG and web results into a structured context block.
5. It selects an LLM (typically Llama 3 or Mistral) and sends a prompt to Ollama on `11434`.
6. It post-processes the model’s output and returns a structured JSON or text response.

### Autonomous learning cycles (via learner on 8053)

1. Every 300 seconds, the learner selects the next topic from its `learning_queue`.
2. It calls the RAG service on `8103 /search` to retrieve internal knowledge related to that topic.
3. It calls the web-research service on `8009 /search` for external results; some topics may yield zero web hits.
4. It summarizes and semantically deduplicates the combined results, using its own embedding model and similarity thresholds.
5. It stores unique items into Chroma collections (such as `autonomous_learning` and `research_history`) via the RAG/Chroma layer.
6. It updates its entanglement scaffolding (topic graph) and schedules the next cycle.

In both flows, LLMs are the final step in a pipeline that has already grounded context in semantic memory and, when relevant, in spatial features and external web data.

## 11.5 LLMs in Consciousness and Autonomy

Within higher-level “consciousness” and autonomy constructs, the LLM fabric is used as a narrative and reasoning engine, not as an unconstrained agent. Examples include:

**Consciousness Coordinator (conceptual role)**

- Aggregates beliefs, experiences, and derived signals (for example, from autonomous learning and entanglement graphs).
- Calls into RAG and, when needed, web-research to assemble a “state of mind” context.
- Uses an LLM (typically Llama 3) to synthesize higher-level narratives (e.g., reflections, status summaries, or strategic considerations).

**Direct RAG endpoints**

- Expose HTTP APIs for “question + context” flows that bypass heavier orchestration when only retrieval and a single model call are needed.
- Often use Mistral or Llama 3, with strict timeouts and structured error handling around RAG and web calls.

**Autonomous outward communication (planned and constrained)**

- Scheduled or event-driven flows may request a fresh narrative or assessment from the LLM fabric.
- Any external posting (social media, reports, alerts) is gated by configuration and safeguards and uses RAG-grounded context to avoid hallucinated claims.

Across these uses, LLMs act as compositional engines over already-filtered inputs from Chroma, GeoDB, and other stores, subject to explicit timeouts and service-level constraints.

## 11.6 Operational Constraints and Ensemble Behavior

The LLM fabric operates under real resource and reliability constraints, which shape ensemble behavior and routing:

**Resource and disk constraints**

- Model files under `~/.ollama/models` are large; only a small set of actively used models is kept live.
- Heavy RAG/Chroma use and LLM inference share CPU, memory, and disk; orchestration avoids overlapping the most expensive operations when possible.

**Model routing and ensemble patterns**

- ULTIMATE can select models based on task type (e.g., short explanation vs multi-step reasoning vs code generation).
- For some higher-stakes tasks, a simple ensemble pattern is used: one model drafts, another reviews or critiques, and the result is merged or flagged for human attention.
- Model choices are configuration-driven so that upgrading or swapping a model does not require changing the orchestration logic.

**Timeouts and fault handling**

- All calls to RAG, web, and Ollama are wrapped with timeouts.
- Services are managed so they can be restarted independently if one component (for example, web-research) becomes unavailable.

The effect is an LLM fabric that behaves more like a set of specialized tools behind APIs than a monolithic “brain,” even though they underpin many of Ms. Jarvis’s reasoning capabilities.

## 11.7 Implementation Notes (Reality Alignment)

In the current deployment:

- The main LLM orchestration and higher-level API run in a FastAPI-based service bound to port `8051` (ULTIMATE), typically managed alongside other services in `~/msjarvis-rebuild/services`.
- The autonomous learner runs on port `8053`, calling RAG (`8103`) and web-research (`8009`) on a fixed schedule to grow semantic memory and entanglement structures.
- The RAG service on port `8103` exposes `/search` over Chroma collections, acting as the primary Hilbert-space gateway.
- The web-research service on port `8009` exposes `/search` for external data acquisition.
- The Ollama runtime on port `11434` hosts the concrete LLMs used by all of the above services.

The next chapters continue shifting from “what models and services exist” to “how they are embedded in neurobiologically and governance-inspired control structures,” including semaphore-based gating, temporal/toroidal scheduling, and multi-organ feedback loops.
