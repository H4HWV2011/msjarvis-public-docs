# Part II: System Architecture and LLM Fabric

This part describes the concrete architecture that makes Ms. Egeria Jarvis work as a distributed, multi-agent AI system. It focuses on how retrieval, entanglement, self-improvement mechanisms, optimization layers, and multiple language models are wired together into a coherent fabric that can be inspected and audited.

Chapters in this part cover:

- RAG pipeline and routers:
  - How ChromaDB, GIS/GeoDB, and topic-specific routers feed context into specialist and generalist LLMs.
  - How routers, judges, and service registries decide which agents and models to invoke for a given query.

- Quantum-inspired entanglement:
  - How Hilbert-space embeddings, cross-collection links, and weighting schemes couple different memory and reasoning modules.
  - How entanglement-inspired ideas shape similarity, attention, and the sharing of state across services without claiming literal quantum computation.

- Darwin–Gödel Machines:
  - How self-improving agents propose and evaluate changes to code, workflows, and governance structures.
  - How these DGMs use LLMs both as tools (for code generation, analysis, explanation) and as judges that score proposed modifications.

- W.O.A.H. (Weighted Optimization Algorithm Hierarchy):
  - How WO-inspired services score and weight agents, shaping multi-LLM orchestration and routing.
  - Why this is framed as a practical, heuristic hierarchy rather than a full, formally analyzed Whale Optimization Algorithm.

- The LLM fabric of Ms. Jarvis:
  - How a finite set of base LLMs (local Ollama models and, historically, remote models) are assigned roles, combined in ensembles, and integrated with DGMs, WOAH, RAG, and the neurobiological layers.
  - How agent roles, prompts, and judge chains create many “minds” on top of a smaller set of underlying model weights.

Throughout Part II, the emphasis is on honest engineering: how the system actually routes requests, uses multiple LLMs, records and retrieves state, and evolves behavior over time, rather than on idealized diagrams or overstated claims.
