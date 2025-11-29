# 11. The LLM Fabric of Ms. Jarvis

This chapter describes the local language models that form the “LLM fabric” of Ms. Egeria Jarvis and how they are woven into the broader GBIM, RAG, and GeoDB architecture. Rather than treating LLMs as independent agents, the system treats them as constrained tools and judges embedded in a larger retrieval and belief stack that includes ChromaDB, Neo4j, Redis, and the spatial body described in Chapter 6.

## 11.1 Current Local LLM Inventory

The current deployment uses a finite set of base models served by Ollama:

- Llama 3 – primary general-purpose reasoning model for consciousness and GBIM flows when rich Chroma/Neo4j context is available.
- Mistral – faster, smaller-footprint expert for tightly scoped tasks where latency matters more than raw capacity.
- Llama 2 – compatibility baseline for comparative experiments and legacy flows.
- Phi – compact reasoning model for lighter tasks, demos, or constrained scenarios.

All four are accessed via Ollama’s HTTP interface and are called from FastAPI services in `~/msjarvis-rebuild/services`, with model selection controlled through configuration rather than hard-coded choices. Historically, additional models (such as Gemma, Qwen2, Mixtral, and others) have been downloaded and used for specialized roles, but the active local set is intentionally kept small for operational reasons.

## 11.2 Roles of the Core Models

Within Ms. Jarvis, these models play distinct roles:

- Llama 3:
  - Default reasoning model for complex, multi-step questions that require integrating GBIM beliefs, Chroma semantic memory, and GeoDB-backed spatial context.
  - Often used in consciousness-related flows where narrative quality and introspection matter.
- Mistral:
  - Used for faster, resource-efficient tasks such as short explanations, quick checks, and lightweight RAG over limited context.
  - Useful where low latency is more important than maximum capacity.
- Llama 2:
  - Kept primarily for comparison and backwards compatibility with earlier experiments and agent designs.
- Phi:
  - Used for small, bounded tasks, demos, or scenarios where memory and CPU budgets are tight.

These roles can change over time as models are upgraded or replaced, but the pattern of assigning clear responsibilities and avoiding “model sprawl” remains central.

## 11.3 Integration into the GBIM + RAG + GeoDB Stack

The LLMs sit at the top of a multi-layer retrieval and belief architecture:

- Vector store (ChromaDB):
  - Embeddings for textual knowledge, governance documents, thesis materials, and geospatial entities via geodb_* collections.
- Belief and experience stores:
  - Neo4j for integrated beliefs, conflicts, and governance structures.
  - Redis for recent experiences, counters, and fast-changing signals.
- Spatial backbone:
  - PostGIS-backed GeoDB and the spatial body described in Chapter 6, with feature IDs and geometries mirrored into Chroma’s geodb_* collections.
- RAG orchestrators:
  - Services that query Chroma, Redis, Neo4j, and GeoDB to assemble context, then invoke an Ollama model with strict timeouts.

For each operation, the RAG layer:

1. Plans retrieval (which Chroma collections, geodb_* collections, and belief types to hit).
2. Gathers matching embeddings, raw documents, and feature metadata from Chroma and GeoDB.
3. Builds a structured prompt reflecting GBIM’s current beliefs, relevant spatial features, and recent experiences.
4. Calls the selected LLM and parses/validates the output.

The LLMs’ function is thus constrained to narrative, reasoning, and transformation over already-filtered, spatially and semantically grounded context, not free-form hallucination.

## 11.4 LLMs in Consciousness and Autonomy

Key components using the LLMs include:

- Consciousness Coordinator:
  - Aggregates beliefs, experiences, and quantum-inspired insights from DGMs and WOAH.
  - Calls a RAG pipeline to produce samples such as `beliefs_sample`, `experiences_sample`, `quantum_insight_sample`, and `conscious_narrative`.
  - Uses an LLM (typically Llama 3) to synthesize coherent narratives from GBIM, Chroma, and GeoDB context.

- Direct RAG layer:
  - Exposes endpoints (for example, `/direct_rag`) for question + context queries.
  - Chooses an appropriate LLM (often Mistral or Llama 3) and constructs prompts from retrieved textual and spatial context.
  - Enforces timeouts and propagates structured errors (for example, connection failures, missing collections).

- Facebook Autonomy Service:
  - On a scheduled cadence, asks the coordinator for a fresh `conscious_narrative`.
  - Posts it to Facebook as “What’s on my mind” using Graph API credentials from shared configuration.
  - Relies on an LLM to synthesize self-reflective narratives that can include spatially grounded content (for example, references to specific communities or regions) drawn from the GeoDB-backed memory.

In these loops, LLMs are components of a retrieval-augmented consciousness pipeline, not standalone agents.

## 11.5 Operational Constraints

Running local LLMs introduces practical constraints:

- Disk usage:
  - `~/.ollama/models` is one of the largest directories on the system, alongside GIS datasets and Python environments.
- Model lifecycle:
  - Only a small number of models are kept active; historical models may remain in storage but are pruned or archived as needed to manage disk and complexity.
- Timeouts and resilience:
  - Autonomous posting and RAG flows impose strict timeouts and rely on systemd (or equivalent) to restart critical services (RAG, coordinator, Facebook poster) after failures.
- Resource contention:
  - Heavy GeoDB/Chroma operations and LLM inference share CPU, memory, and disk bandwidth; orchestration must avoid pathological contention patterns.

These constraints shape how and when LLMs are invoked, reserving deeper narratives for less frequent conscious ticks and posts, and favoring smaller models or non-LLM logic for routine checks.

## 11.6 Summary

This chapter outlined:

- The current local LLM inventory and why it is intentionally small.
- The distinct roles of the core models in Ms. Jarvis.
- How LLMs integrate with ChromaDB, Neo4j, Redis, and the GeoDB spatial body.
- How they power consciousness and autonomous behaviors while operating within real resource and reliability constraints.

The next chapters continue to shift the focus from “what models are available” to “how they are embedded in neurobiologically inspired control structures and feedback loops,” building on the spatial and semantic foundations described earlier.
