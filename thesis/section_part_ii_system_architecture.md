# Part II: System Architecture and LLM Fabric

This part documents the concrete implementation of Ms. Jarvis as a distributed mesh system, including service topology, vector stores, retrieval pipelines, and the local LLM stack.

It connects the high-level GBIM theory to the actual running services, focusing on:

- Core services and ports (consciousness coordinator, RAG, Facebook autonomy, storage layers).
- ChromaDB and geospatial integration (GBIM + GIS + `geodb_*` collections).
- Local LLM environment and the LLM fabric (Chapter 10 and related chapters).
- Operational constraints: disk, memory, timeouts, and resilience mechanisms.

Part II bridges the conceptual model of consciousness with the concrete engineering choices that make Ms. Jarvis run on real hardware in Mount Hope, WV.
