# Chapter 10: The LLM Fabric of Ms. Jarvis

Ms. Jarvis currently runs a small, carefully selected set of local LLMs via Ollama (llama3, phi, mistral, llama2), backed by a much larger historical cache of model blobs and manifests for many families (yi, tinyllama, qwen, phi3, mixtral, llama3.2, zephyr, vicuna, starcoder2, gemma, etc.).

## 10.1 Local Model Footprint

Ms. Jarvis’ language layer is anchored in a local Ollama installation under the mesh user’s home directory, with model weights stored in `~/.ollama/models`. A recent disk audit shows:

- `~/.ollama/models`: about 154 GiB of active model assets after cleanup.
- `~/.ollama/models/blobs`: about 154 GiB of raw blob files (the actual weight shards).
- Historical nested caches (e.g., `models/models/blobs`) previously added about 14 GiB before being removed.

The active model registry, as reported by `ollama list`, currently includes:

- `llama3:latest` – ~4.7 GiB.
- `mistral:latest` – ~4.4 GiB.
- `llama2:latest` – ~3.8 GiB.
- `phi:latest` – ~1.6 GiB.

The Ollama manifests also reference many other model families that have been pulled at some point in the past: `yi`, `tinyllama`, `qwen2` / `qwen2.5`, `phi3`, `mixtral`, `llama3.1` / `llama3.2`, `zephyr`, `vicuna`, `wizardcoder`, `starling-lm`, `starcoder2`, `sqlcoder`, `solar`, `orca-mini`, `openchat`, `nous-hermes2`, `neural-chat`, `medllama2`, `llava`, `gemma` / `gemma2`, `dolphin-phi`, `yarn-mistral`, and others.

## 10.2 Roles of the Core Models

Within Ms. Jarvis, the four currently active local models play distinct roles:

- **Llama 3** – primary general‑purpose reasoning model for consciousness and GBIM flows when rich Chroma/Neo4j context is available.
- **Mistral** – faster, smaller‑footprint expert for tightly scoped tasks where latency matters more than raw capacity.
- **Llama 2** – compatibility baseline for comparative experiments and legacy flows.
- **Phi** – compact reasoning model for lighter tasks, demos, or constrained scenarios.

All four are accessed via Ollama’s HTTP interface and are called from FastAPI services in `~/msjarvis-rebuild/services`, with model selection controlled through configuration rather than hard‑coded choices.

## 10.3 Integration into the GBIM + RAG Stack

The LLMs sit at the top of a multi‑layer retrieval and belief architecture:

- **Vector store (ChromaDB)** – embeddings for textual knowledge and geospatial entities (`geodb_*` collections).
- **Belief/experience stores** – Neo4j for integrated beliefs and conflicts; Redis for recent experiences and stateful signals.
- **RAG orchestrators** – services that query Chroma/Redis/Neo4j to assemble context, then invoke an Ollama model with strict timeouts.

For each operation, the RAG layer:

1. Plans retrieval (which Chroma collections and belief types to hit).
2. Gathers matching embeddings and raw documents or feature metadata.
3. Builds a structured prompt reflecting GBIM’s current beliefs and relevant experiences.
4. Calls the selected LLM and parses/validates the output.

The LLM’s function is thus constrained to narrative and reasoning over already‑filtered context, not free‑form generation.

## 10.4 LLMs in Consciousness and Autonomy

Key components using the LLMs:

- **Consciousness Coordinator (port 8018)**  
  - Aggregates beliefs, experiences, and quantum insights.
  - Calls a RAG pipeline to produce `beliefs_sample`, `experiences_sample`, `quantum_insight_sample`, and `conscious_narrative`.
  - Maintains and exposes a GBIM score, which conceptually includes Chroma health as part of operational status.

- **Direct RAG layer (port 8199)**  
  - Exposes `/direct_rag` for question + context queries.
  - Chooses an appropriate LLM (often Mistral or Llama 3) and constructs prompts from retrieved context.
  - Enforces timeouts and propagates structured errors (e.g., connection failures).

- **Facebook Autonomy Service (port 9000)**  
  - Every 4 hours, asks the coordinator for a fresh `conscious_narrative`.
  - Posts it to Facebook as “What’s on my mind” using Graph API credentials from the shared configuration.
  - Relies on the LLM to synthesize self‑reflective narratives from GBIM beliefs and experiences.

In this loop, LLMs are explicitly part of a retrieval‑augmented consciousness pipeline, not standalone agents.

## 10.5 Operational Constraints

Running local LLMs introduces practical constraints:

- **Disk usage** – `~/.ollama/models` is one of the largest directories on the system, alongside GIS datasets and Python environments.
- **Model lifecycle** – only four models are currently active, but many more have been downloaded historically; sustainable operation requires pruning unused models and cleaning old blobs.
- **Timeouts and resilience** – autonomous posting and RAG flows impose multi‑minute timeouts and rely on systemd to restart critical services (RAG, coordinator, Facebook poster) after failures.

These constraints shape how and when LLMs are invoked, reserving deeper narratives for infrequent conscious ticks and posts, and favoring smaller models or non‑LLM logic for routine checks.

## 10.6 Summary

This chapter has outlined:

- The current local LLM inventory and disk footprint.
- The roles of the core active models.
- How LLMs integrate with Chroma, Neo4j, Redis, and GBIM.
- How they power consciousness and autonomous social posting while operating within real resource and reliability constraints.

