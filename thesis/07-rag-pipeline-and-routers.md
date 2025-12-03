# 07. RAG Pipeline and Routers

This chapter explains how Ms. Egeria Jarvis uses a retrieval-augmented generation (RAG) pipeline to answer questions and support governance decisions. In this architecture, language models do not respond from a blank slate; they are constrained and informed by retrieval from ChromaDB, GBIM, the GeoDB/PostGIS layer, and other structured sources, orchestrated through explicit routing and role-aware logic.

Within the Quantarithmia program, the RAG pipeline is the mechanism that connects Hilbert-space state, semantic memory, and the spatial body described in Chapter 6 to actual outputs, making it possible to trace how an answer was constructed and which knowledge it relied on.

## 06.1 Goals of the RAG Design

The RAG system is designed to achieve several goals:

- Grounding: Ensure that Ms. Jarvis’s responses are anchored in curated, domain-specific memory (GBIM, governance docs, GeoDB-backed geodb_* collections, thesis materials) rather than arbitrary model associations.
- Transparency: Make it possible to inspect which documents, entities, or spatial features were retrieved and how they influenced the final answer.
- Constraint enforcement: Apply constitutional principles, ethical guards, and role-based limits before and after generation, not just as an afterthought.

These goals reflect the broader thesis commitments to glassbox AI and spatial justice: the system should show its work and respect community-defined boundaries, including geographic ones.

## 06.2 High-Level RAG Flow

At a high level, a typical RAG interaction in Ms. Jarvis follows this sequence:

1. Query intake: A user or system sends a request (for example, a research question, a governance proposal summary, or a GIS query).
2. Role and context identification: The system determines the active role (researcher, advisor, governance support) and relevant geospatial or institutional context.
3. Embedding and routing: The query is embedded into the Hilbert-space state and passed through routers that decide which ChromaDB collections, GeoDB-backed geodb_* collections, and services should handle retrieval.
4. Retrieval: Relevant documents, GBIM entities, spatial features, and other artifacts are fetched from ChromaDB, PostGIS, and related services, filtered by role, geography, and constraints.
5. Context assembly: Retrieved items are combined into a structured context window, with clear separation between sources (GIS/GeoDB, governance, thesis, logs) and annotations about their relevance.
6. Generation under constraints: A language model generates an answer using the assembled context, with constitutional and ethical guards active during decoding.
7. Post-hoc checks and explanation: Outputs may be checked again, and Ms. Jarvis can provide explanations of which sources were used and how they shaped the answer.

This flow turns RAG from a simple “vector search + LLM” pattern into a more disciplined pipeline aligned with the project’s governance, transparency, and spatial grounding goals.

## 06.3 Routers and Role-Aware Retrieval

Routing is a central part of this RAG design:

- Topic/intent routers: Lightweight classifiers or rules determine whether a query is primarily about GIS/geospatial context, governance, thesis theory, infrastructure status, or other domains.
- Role-aware routers: The active role influences which collections and services are eligible (for example, a community-facing advisor role may be restricted to public documentation, while a researcher role can access more technical thesis materials and sensitive spatial layers).
- Geography-aware routers: Queries mentioning or tagged with specific places (such as Mount Hope, particular districts, counties, or coordinates) are routed to GBIM-linked collections and the GeoDB/PostGIS layer, using geodb_* Chroma collections as the semantic front-end for spatial features.

Routers thus narrow the search space before retrieval, reducing noise and preventing inappropriate cross-domain leakage (for example, mixing internal operational logs into community-facing answers, or exposing sensitive spatial layers in public-facing roles).

## 06.4 Context Construction and Structure

The way context is constructed from retrieved items matters:

- Source separation: Retrieved chunks are grouped by source (GIS/GeoDB, governance, thesis, logs) so that the language model can respect their different roles and levels of authority.
- Relevance ordering: Items are sorted by similarity score and, where applicable, by recency, explicit importance tags, or spatial relevance (such as distance from a target feature or area).
- Size and diversity: The context window balances including enough diverse evidence against overloading the model with redundant or low-value text or features.

This structured context helps Ms. Jarvis generate answers that are both grounded and interpretable, and makes it easier to trace back from a statement to the supporting retrievals, including specific spatial features.

## 06.5 Constraints During and After Generation

Constitutional and ethical constraints interact with the RAG pipeline at multiple points:

- Pre-retrieval filters: Certain query types or topics may be blocked or redirected before retrieval if they fall outside allowed use (for example, attempting to weaponize the system against individuals or communities).
- Retrieval-time filters: Retrieved items can be filtered to exclude sensitive or out-of-scope content for the active role or audience, including spatial layers that are not appropriate for public exposure.
- Decoding-time guards: During generation, guardrails monitor the output stream for violations of constitutional principles (such as incitement to harm or harassment) and can block, rephrase, or annotate responses.
- Post-hoc review: For high-stakes decisions, outputs and their underlying retrievals (documents and spatial features) can be logged for human review, making the pipeline auditable.

These layered constraints reinforce the thesis claim that Ms. Jarvis is designed as a constrained, accountable system rather than an unconstrained text generator.

## 06.6 Relation to Long-Term Memory, GeoDB, and Entanglement

The RAG pipeline sits between static memory and dynamic reasoning:

- Long-term memory: ChromaDB and GBIM provide the relatively stable backbone of embeddings and geospatially anchored beliefs, while the GeoDB/PostGIS layer and associated geodb_* collections provide the spatial body described in Chapter 6.
- Short-term context: The RAG context window represents a temporary, task-specific slice of that memory and spatial state assembled for a particular query.
- Coupled updates: When the thesis later discusses the “quantum-inspired entanglement” algorithm, it describes how certain updates or constraints propagate across related regions of the state space—semantic, spatial, and normative—influencing future retrieval, routing decisions, and which parts of the GeoDB are emphasized.

In this way, RAG is not just a one-off retrieval step but part of an ongoing interaction between Ms. Jarvis’s memory, spatial body, state, and governance constraints.

> Status: This chapter is a draft overview of the RAG pipeline and routing logic in Ms. Jarvis. More detailed diagrams, pseudo-code, and evaluations of retrieval quality, spatial coverage, and constraint effectiveness will appear in technical appendices and implementation-focused documentation.
