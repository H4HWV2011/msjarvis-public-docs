# 7. RAG Pipeline and Routers

This chapter describes how Ms. Egeria Jarvis uses a retrieval-augmented generation (RAG) pipeline to answer questions and support governance decisions. In this architecture, language models do not respond from a blank slate: they are constrained and informed by retrieval from ChromaDB, GBIM, the GeoDB/PostGIS layer, and other structured sources, orchestrated through explicit routing and role-aware logic.

Within the Quantarithmia program, the RAG pipeline is the mechanism that connects Hilbert-space state, semantic memory, and the spatial body described in Chapter 6 to actual outputs, making it possible to trace how an answer was constructed and which knowledge it relied on.

## 7.1 Goals of the RAG Design

The RAG system is designed to achieve several goals:

- Grounding:
  - Ensure that Ms. Jarvis’s responses are anchored in curated, domain-specific memory (GBIM, governance docs, GeoDB-backed collections, thesis materials) rather than arbitrary model associations.
- Transparency:
  - Make it possible to inspect which documents, entities, or spatial features were retrieved and how they influenced the final answer.
- Constraint enforcement:
  - Apply constitutional principles, ethical guards, and role-based limits before and after generation, not just as an afterthought.

These goals reflect the broader thesis commitments to glassbox AI and spatial justice: the system should show its work and respect community-defined boundaries, including geographic ones.

## 7.2 High-Level RAG Flow

At a high level, a typical RAG interaction in Ms. Jarvis follows this sequence:

1. Query intake:
   - A user or system sends a request (for example, a research question, a governance proposal summary, or a GIS query).
2. Role and context identification:
   - The system determines the active role (researcher, advisor, governance support) and relevant geospatial or institutional context.
3. Embedding and routing:
   - The query is embedded into the Hilbert-space state and passed through routers that decide which ChromaDB collections, GeoDB-backed collections, and services should handle retrieval.
4. Retrieval:
   - Relevant documents, GBIM entities, spatial features, and other artifacts are fetched from ChromaDB, PostGIS, and related services, filtered by role, geography, and constraints.
5. Context assembly:
   - Retrieved items are combined into a structured context window, with clear separation between sources (GIS/GeoDB, governance, thesis, logs) and annotations about their relevance.
6. Generation under constraints:
   - A language model generates an answer using the assembled context, with constitutional and ethical guards active during decoding.
7. Post-hoc checks and explanation:
   - Outputs may be checked again, and Ms. Jarvis can provide explanations of which sources were used and how they shaped the answer.

This flow turns RAG from a simple vector search + LLM pattern into a more disciplined pipeline aligned with the project’s governance, transparency, and spatial grounding goals.

## 7.3 Routers and Role-Aware Retrieval

Routing is a central part of this RAG design:

- Topic/intent routers:
  - Lightweight classifiers or rules determine whether a query is primarily about GIS/geospatial context, governance, thesis theory, infrastructure status, or other domains.
- Role-aware routers:
  - The active role influences which collections and services are eligible; for example, a community-facing advisor role may be restricted to public documentation, while a researcher role can access more technical thesis materials and sensitive spatial layers.
- Geography-aware routers:
  - Queries mentioning or tagged with specific places (such as Mount Hope, particular districts, counties, or coordinates) are routed to GBIM-linked collections and the GeoDB/PostGIS layer, using Chroma-backed collections as the semantic front-end for spatial features.

Routers thus narrow the search space before retrieval, reducing noise and preventing inappropriate cross-domain leakage (for example, mixing internal operational logs into community-facing answers, or exposing sensitive spatial layers in public-facing roles).

## 7.4 Context Construction and Structure

The way context is constructed from retrieved items matters:

- Source separation:
  - Retrieved chunks are grouped by source (GIS/GeoDB, governance, thesis, logs) so that the language model can respect their different roles and levels of authority.
- Relevance ordering:
  - Items are sorted by similarity score and, where applicable, by recency, explicit importance tags, or spatial relevance (such as distance from a target feature or area).
- Size and diversity:
  - The context window balances including enough diverse evidence against overloading the model with redundant or low-value text or features.

This structured context helps Ms. Jarvis generate answers that are both grounded and interpretable, and makes it easier to trace back from a statement to the supporting retrievals, including specific spatial features.

## 7.5 Constraints During and After Generation

Constitutional and ethical constraints interact with the RAG pipeline at multiple points:

- Pre-retrieval filters:
  - Certain query types or topics may be blocked or redirected before retrieval if they fall outside allowed use (for example, attempting to weaponize the system against individuals or communities).
- Retrieval-time filters:
  - Retrieved items can be filtered to exclude sensitive or out-of-scope content for the active role or audience, including spatial layers that are not appropriate for public exposure.
- Decoding-time guards:
  - During generation, guardrails monitor the output stream for violations of constitutional principles (such as incitement to harm or harassment) and can block, rephrase, or annotate responses.
- Post-hoc review:
  - For high-stakes decisions, outputs and their underlying retrievals (documents and spatial features) can be logged for human review, making the pipeline auditable.

These layered constraints reinforce the thesis claim that Ms. Jarvis is designed as a constrained, accountable system rather than an unconstrained text generator.

## 06.x Web research gateway service

The autonomous learner and certain RAG flows rely on a dedicated web research gateway instead of making ad hoc external calls.

- Service and endpoint:
  - A FastAPI-based service runs on port 8009 and exposes a `POST /search` endpoint for controlled web queries.
  - Requests are JSON objects with the shape `{"query": "<string>", "max_results": <int>}`, where `max_results` bounds the number of returned items.
- Response shape:
  - The gateway returns an object containing:
    - `query`: The original query string.
    - `count`: The number of results available or returned.
    - `results`: A list of objects, each with `title`, `snippet`, `url`, and `source` fields.
  - This structure makes it straightforward to normalize results and feed them into summarization, embedding, and storage steps.
- Integration with RAG and autonomy:
  - The optimized autonomous learner uses this gateway on each cycle to obtain candidate material for a selected topic before summarization and deduplication.
  - Interactive RAG pipelines can reuse the same service when they need web-origin content, ensuring that external access policies, logging, and rate limits are centralized rather than scattered across services.

By routing web queries through this gateway, the system keeps external retrieval within a well-defined channel that can be monitored, constrained, and evolved over time.

## 06.6 Relation to Long-Term Memory, GeoDB, and Entanglement
## 7.6 Relation to Long-Term Memory, GeoDB, and Entanglement

The RAG pipeline sits between static memory and dynamic reasoning:

- Long-term memory:
  - ChromaDB and GBIM provide the relatively stable backbone of embeddings and geospatially anchored beliefs, while the GeoDB/PostGIS layer and associated collections provide the spatial body described in other chapters.
- Short-term context:
  - The RAG context window represents a temporary, task-specific slice of that memory and spatial state assembled for a particular query.
- Coupled updates:
  - When the thesis later discusses the quantum-inspired entanglement algorithm, it describes how certain updates or constraints propagate across related regions of the state space—semantic, spatial, and normative— influencing future retrieval, routing decisions, and which parts of the GeoDB are emphasized.

In this way, RAG is not just a one-off retrieval step but part of an ongoing interaction between Ms. Jarvis’s memory, spatial body, state, and governance constraints.

Status: This chapter is a draft overview of the RAG pipeline and routing logic in Ms. Jarvis. More detailed diagrams, pseudo-code, and evaluations of retrieval quality, spatial coverage, and constraint effectiveness will appear in technical appendices and implementation-focused documentation.

## Operational Architecture (Dece/chat request
↓
main_brain receives request
↓
Health check sweep (identify 8/23 services)
↓
BBB query_service call (filter + context)
↓
web_research query_service call (enhance context)
↓
### Storage Backend (UNKNOWN - Requires Investigation)

**Which ChromaDB instance receives RAG writes?**
- jarvis-chroma (8002→8000)?
- services-chroma-1 (8010→8010)?
- msjarvis-rebuild-chroma-1 (8000→8000)?

**TODO**: Inspect main_brain code to determine RAG storage target.

### Retrieval Mechanism (NOT YET TRACED)

**Current gap**: No retrieval operations observed in logs during testing.

**Questions**:
- When is RAG retrieval triggered?
- What semantic similarity threshold triggers context injection?
- How many prior contexts are retrieved per query?
- What embedding model is used?

### Implementation Status Badge

🔄 **PARTIAL** - Storage queuing validated, storage backend unknown, retrieval path not yet traced

### Performance Characteristics

- RAG storage: Asynchronous queue (non-blocking)
- Estimated retrieval latency: 100-500ms (if triggered)
- Storage throughput: ~1 write per ULTIMATE response (measured: 195-353s intervals)

### Recommendations for Phase 2

1. Add RAG debug endpoint showing:
   - Storage operations (writes)
   - Retrieval operations (queries)
   - Semantic similarity scores
   - Retrieved context payloads

2. Document RAG routing logic:
   - Query classification (factual? reasoning? creative?)
   - Context selection criteria
   - Injection point in llm_bridge pipeline

3. Measure retrieval impact on latency

llm_bridge query_service call (22-agent synthesis)
↓
Response aggregation
↓
RAG storage queuing (every response)
↓
Return response to client

mber 11, 2025)

### Validated Request Flow

