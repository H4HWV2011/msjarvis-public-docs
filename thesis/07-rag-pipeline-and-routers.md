# 7. RAG Pipeline and Routers

This chapter describes the current retrieval‑augmented generation (RAG) infrastructure used by Ms. Egeria Jarvis and clarifies which elements are implemented in production and which remain design targets. In the present deployment, language models are no longer queried “from scratch”: they are constrained and informed by a dedicated RAG service backed by ChromaDB, a web‑research gateway, and explicit routing logic in the main brain and orchestration layer. The more advanced role‑ and geography‑aware behaviors described in earlier drafts are treated here as planned extensions rather than accomplished facts.

Within the Ms.Jarvis program, the RAG layer is the primary mechanism that connects the semantic memory substrate described in the previous chapter to live outputs. It provides a concrete place where retrieval calls, context assembly, and downstream generation can be inspected and tested, even though full provenance tracking and spatial coupling are still under active development.

## 7.1 Goals of the RAG Design

The RAG system is engineered around three principled goals that guide both the current implementation and the roadmap:

- Grounding.  
  The RAG service should ensure that Ms. Jarvis’s responses are anchored in curated, domain‑specific memory rather than arbitrary model associations. In the current system, this means querying explicitly named ChromaDB collections (for example, governance and project‑specific collections) and returning scored text snippets with associated metadata, rather than relying solely on the internal priors of the language model.

- Transparency.  
  The retrieval process should be inspectable. The production RAG server therefore exposes a structured `/search` endpoint that returns both a flat list of results and a `results_by_source` mapping keyed by collection name, along with similarity‑derived scores and the `where` filter actually applied. This provides a minimal but concrete basis for tracing which collections contributed evidence to a given answer.

- Constraint enforcement.  
  The broader architecture is designed to support layered constraints before, during, and after generation. At present this is realized most concretely in two places: (1) selection of which collections are queried for a given request, and (2) decoding‑time output guarding, where the main brain can send completed responses through a separate “blood–brain barrier” service for filtering. Role‑ and geography‑aware constraints are partially wired in the RAG API but not yet backed by comprehensive metadata.

These goals match the overall thesis commitments to glassbox AI and spatial justice, but the chapter is careful to distinguish live behavior from work that remains to be completed.

## 7.2 Current High‑Level RAG Flow

A typical RAG interaction in the current Ms. Jarvis stack proceeds through the following stages:

1. Query intake.  
   A user or upstream service submits a request to the unified gateway or directly to the main brain. The main brain wraps this request into an internal job structure and routes it through an orchestration service, which may invoke the RAG server, the web‑research gateway, and one or more language‑model backends.

2. Routing to retrieval services.  
   The orchestration layer decides whether to call the local RAG server, the web‑research gateway, or both, based on the type of request. At the time of writing, this routing is implemented by explicit service calls and configuration rather than learned classifiers, but it already separates “internal knowledge” retrieval (ChromaDB‑backed) from “external web” retrieval.

3. Retrieval from ChromaDB.  
   The RAG server queries one or more configured Chroma collections using the incoming query string, a caller‑supplied `top_k` parameter, and an optional filter object that can constrain the search by metadata fields such as source, collection name, county, or state. For each collection, the server returns documents, metadata, and distances, which are converted into scores and packaged into `results_by_source`.

4. Context assembly upstream.  
   The main brain or its orchestration layer receives RAG results and assembles them into a context window alongside any additional information (for example, web‑research results or internal status). In the current implementation, this assembly is largely handled in service‑specific logic rather than a single centralized context builder, but all paths share the expectation that retrieved snippets are grouped by source and accompanied by metadata.

5. Generation under constraints.  
   A language model (or a set of models in the 20‑LLM consensus backend) generates an answer conditioned on the retrieved context. After generation, the main brain applies a decoding‑time guard by sending the response through the blood–brain barrier service, which is allowed to rewrite or reject unsafe outputs, implementing a first layer of constitutional constraints.

6. Logging and optional storage.  
   The RAG server supports a `/store` endpoint for background storage of queries and responses into a conversation‑history collection. This is used by the main brain to persist a subset of interactions for later analysis, retraining, or auditing, though a full provenance and explanation stack is still in progress.

This flow elevates RAG from a simple “vector search plus LLM” pattern to a coordinated service that the rest of the fabric can depend on. It also creates clear integration points for the more advanced routing and spatial coupling described later in the thesis.

## 7.3 Routers and Role‑Aware Retrieval (Design vs. Implementation)

Routing is conceptually central to the RAG design, but at this stage there is an important distinction between the target design and the deployed behavior.

On the design side:

- Topic and intent routing.  
  The system is intended to distinguish between queries about governance, geospatial context, thesis theory, and infrastructure status, and to send each to appropriate services and collections. For example, a governance query should favor collections containing policy documents, while an infrastructure query might emphasize logs or status traces.

- Role‑aware routing.  
  The intended architecture allows the active role (for example, researcher, governance support, community‑facing advisor) to determine which collections are eligible. Under this design, internal or sensitive material would only be surfaced for trusted roles, while community‑facing roles would be restricted to public documentation and appropriately filtered geospatial layers.

- Geography‑aware routing.  
  Queries with explicit or implicit place references should be routed toward collections that encode GBIM entities and GeoDB/PostGIS‑linked features, using Chroma metadata fields such as place, region, or precomputed region identifiers.

On the implementation side:

- The RAG server already exposes `role` and `geography` fields in its public `/search` API and uses them to select collections and construct a `where` clause, but the underlying Chroma collections are only partially populated with the corresponding metadata. As a result, role‑ and geography‑aware behaviors are presently conservative extensions of a generic RAG flow, not fully realized routing policies.

- At present, routing decisions are implemented as explicit calls from the orchestration layer to specific services and collections. Lightweight learned routers are planned but not yet necessary for the current scale of the system.

The chapter therefore treats role‑ and geography‑aware routing as an active area of development, with the RAG server’s API and code already shaped to accommodate them, but the data and metadata still being brought up to the level required for strict enforcement.

## 7.4 Context Construction and Structure

Even in the current deployment, how retrieved material is structured for the language model is a significant design choice. The RAG server and upstream services adopt several principles to keep context both usable and inspectable:

- Source separation.  
  The RAG server returns a `results_by_source` dictionary keyed by collection name, and each item carries `collection`, `source`, and `metadata` fields. This makes it possible to keep, for example, governance documents distinct from research notes or spatial features, and allows upstream logic to treat them differently when building prompts.

- Relevance ordering.  
  Chroma returns distances, which the server converts into scores; flat results are sorted in descending score order. Upstream services are expected to respect this ordering, and can optionally combine it with recency or importance tags in the metadata.

- Bounded context size.  
  Clients specify `top_k` per collection, and the RAG server enforces this limit. This prevents over‑large contexts while still allowing multiple collections to contribute. In future iterations, more sophisticated diversity and redundancy controls may be applied, but even the current `top_k` policy enforces an explicit trade‑off between breadth and depth.

The combination of collection‑aware grouping, explicit scores, and bounded retrieval gives the language model a structured input that is closer to an evidence set than an undifferentiated text blob. As the metadata schemas mature, this same structure will also support richer tracing from answers back to the specific documents and collections that informed them.

## 7.5 Constraints During and After Generation

Constitutional and ethical constraints in the present system interact with the RAG pipeline at several points, though not yet with the full subtlety envisioned in the long‑term design.

- Pre‑retrieval and retrieval‑time constraints.  
  The RAG server’s filter mechanism already supports limiting retrieval by collection, source, county, and state, and its API now includes `role` and `geography` fields that will govern access‑level and spatial filters as the metadata is filled in. For now, these features are used conservatively, and many queries still fall back to role‑agnostic retrieval for lack of complete metadata.

- Decoding‑time guards.  
  After retrieval and generation, the main brain routes candidate responses through a dedicated guardrail service that can refuse, rewrite, or annotate outputs that violate constitutional or safety principles. This decoding‑time guard operates over the final answer, regardless of which retrieval path produced it, and is intended to complement (not replace) the earlier filters.

- Post‑hoc review and logging.  
  The RAG server’s `/store` endpoint and the main brain’s logging hooks already capture enough information to reconstruct which services were involved in answering a given query and, in some cases, what was retrieved. However, a fully structured, user‑facing explanation interface—where Ms. Jarvis can explicitly list the documents and spatial features relied upon—is still marked as future work.

Together, these mechanisms move the system away from unconstrained text generation toward a constrained, accountable pipeline, while leaving room to tighten role‑ and geography‑specific policies as the underlying memory schemas stabilize.

## 7.6 Web Research Gateway Service

External web retrieval is handled by a dedicated gateway rather than allowing arbitrary outbound calls from each agent or service. This gateway supports both autonomous learning loops and interactive RAG flows.

- Service and endpoint.  
  The gateway is implemented as a FastAPI service exposing a `POST /search` endpoint. Requests are JSON objects that include a query string and a limit on the number of results. The gateway is responsible for enforcing external access policies, rate limits, and logging.

- Response structure.  
  Gateway responses standardize web search results into a predictable shape, including the original query, a result count, and a list of items with fields such as title, snippet, URL, and source. This uniform structure simplifies downstream summarization, embedding, and storage into ChromaDB.

- Integration with RAG and autonomy.  
  The autonomous learner service uses the gateway to obtain fresh web material for chosen topics before either embedding it into Chroma or discarding it as irrelevant. Interactive RAG flows can reuse the same gateway when a query explicitly requires web‑origin information, ensuring that the boundary between local semantic memory and external sources remains explicit and monitored.

By channeling all web access through this gateway, the architecture keeps external retrieval within a clearly defined, auditable path that can evolve independently of the internal RAG service.

## 7.7 Relation to Long‑Term Memory, GeoDB, and Entanglement

The RAG layer sits between relatively static long‑term memory and dynamic, per‑query reasoning, and it is the primary place where semantic and spatial representations are expected to meet.

- Long‑term memory.  
  ChromaDB collections hold embedded representations of governance documents, project‑specific knowledge, and other curated materials. Additional collections are reserved for GBIM and GeoDB‑related content, with metadata fields planned to encode access levels and spatial attributes such as place and region.

- Short‑term context.  
  Each RAG call assembles a temporary context window from the retrieved items, sorted by relevance and grouped by collection. This window serves as the immediate working memory for the language models and orchestration services as they construct an answer.

- Coupled updates and future entanglement.  
  The thesis’ broader entanglement concept envisions updates to semantic memory, spatial layers, and normative constraints as mutually influencing. The current RAG implementation does not yet realize this fully; instead, it provides a stable, inspectable interface that can later be extended with entanglement‑aware routing, access policies, and metadata propagation across collections.

In this way, the present RAG deployment should be understood as a working but intentionally conservative layer: it already anchors Ms. Jarvis’s outputs in named collections and explicit retrieval calls, but it still relies on forthcoming work in metadata design, spatial integration, and explanation tooling to fully satisfy the program’s glassbox and spatial‑justice commitments.
