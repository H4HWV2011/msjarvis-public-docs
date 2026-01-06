## 5. ChromaDB as Semantic Memory

### 5.1 Purpose and Scope

This chapter explains how Ms. Egeria Jarvis uses ChromaDB as the primary semantic memory layer backing the Hilbert‑space state, GBIM, and the broader semantic fabric. ChromaDB is a vector database that stores high‑dimensional embedding vectors with associated metadata and exposes efficient similarity search and filtering operations. In this system, ChromaDB is not merely a convenience library; it is the concrete implementation of long‑term, queryable memory for documents, GIS features, governance texts, autonomous‑learning traces, and thesis materials.

Within the Quantarithmia program, ChromaDB is treated as the bridge between abstract Hilbert‑space state and actual stored knowledge. It is the place where beliefs, contexts, and references become durable and retrievable for reasoning and retrieval‑augmented generation (RAG). Conceptually, each collection corresponds to a subset of the Hilbert space, and stored vectors approximate elements of the spaces described in the previous chapter.

---

### 5.2 Role in the Ms. Jarvis Architecture

In the Ms. Jarvis architecture, ChromaDB plays several interlocking roles.

- **Semantic memory store (non‑spatial).**  
  Embeddings of texts and artifacts live in collections corresponding to domains such as governance, thesis content, autonomous learner outputs, conversations, and curated user memory. These collections support general semantic retrieval independent of geography.

- **Geospatial Hilbert layer (spatial).**  
  A large family of `geodb*` and `gedb*` collections holds embeddings and metadata for West Virginia geospatial features, mirroring PostGIS tables and providing the Hilbert‑space representation of the spatial body described in the GBIM chapter. These collections connect directly to GeoDB entities and geometries.

- **Retrieval engine for RAG.**  
  At query time, services embed inputs and use ChromaDB similarity search, often with metadata filters, to retrieve the most relevant items for context and reasoning. This behavior instantiates the query projection and neighborhood selection mechanisms described in the Hilbert‑space model.

- **Structural backbone for inspectable memory.**  
  Because collections and metadata are explicitly defined, ChromaDB’s structure mirrors core parts of GBIM, the GeoDB layer, and the thesis organization. This makes it possible to enumerate collections, inspect document counts, and audit metadata, rather than relying on hidden internal state.

This design makes the semantic memory system inspectable and debuggable: researchers and community partners can see what is stored, how it is grouped, and which collections underpin particular advisory behaviors.

---

### 5.3 Collections and Data Domains

In the deployment examined in late 2025 and early 2026, the primary Chroma instance exposes a concrete set of collections that fall into two broad families: general semantic memory and GeoDB‑derived spatial memory. This section describes typical collections and their intended semantics. Collection names and schemas are documented in the system’s registry and may evolve in a controlled, versioned manner.

#### 5.3.1 General Semantic Collections

Representative general collections include:

- `conversations`  
- `ms_jarvis_memory`  
- `user_memory_vectors`  
- `autonomous_learning`  
- `research_history`  
- `mountainshares_knowledge`  
- `spiritual_wisdom`  
- `thesis_materials` (or a closely related thesis collection)  
- `default`  
- smaller auxiliary collections used for development and diagnostics.

These collections correspond to distinct data domains:

- **Conversations and user memory.**  
  Collections such as `conversations`, `ms_jarvis_memory`, and `user_memory_vectors` store selected interaction snippets, higher‑level conversational summaries, and explicit user‑memory embeddings used by certain agents and bridges. They provide continuity and context across sessions, subject to privacy and curation policies.

- **Governance and norms.**  
  `mountainshares_knowledge` stores MountainShares rules, constitutional principles, governance deliberation texts, and related commentary, providing a focused corpus for economic and governance questions. Its contents are curated to reflect official project documents and carefully selected supporting materials.

- **Learner and research history.**  
  `autonomous_learning` and `research_history` store web‑research outputs, per‑cycle summaries, and RAG traces emitted by the autonomous learner. These collections capture what was studied, when it was studied, and how it was summarized, enabling both introspection and incremental learning.

- **Spiritual and contextual materials.**  
  `spiritual_wisdom` stores spiritual, reflective, and contextual texts that inform qualitative and ethical framings of responses. This collection is curated and explicitly documented so that its role remains transparent.

- **Thesis and internal materials.**  
  Collections such as `thesis_materials` hold drafts, notes, and supporting texts referenced within the Quantarithmia research program. They provide a local, versioned corpus for internal reasoning and documentation.

In some of these collections, embeddings are fully populated and used for similarity search. In others, especially certain governance or thesis collections, documents and metadata may be fully present while embeddings are still being backfilled or recomputed. The system registry records which collections have complete embedding coverage at any given time.

#### 5.3.2 GeoDB‑Derived `geodb*` and `gedb*` Collections

A second, much larger family of collections is generated automatically from the PostGIS GeoDB. These collections provide the embedding‑space representation of GBIM’s spatial body. Typical examples include:

- **Census and boundary layers.**  
  Collections such as `geodbblockscensus2020utm83`, `geodbblockgroupscensus2020utm83`, and corresponding `wma84` variants represent blocks and block groups; other collections capture ZIP code tabulation areas, county and municipal boundaries, regional planning councils, and related governance outlines.

- **Infrastructure and hazard layers.**  
  Collections such as `geodbbridges`, `geodbdamsusarmycorpsofengineers200010utm83`, `geodbdamsnoncoalusgs2002utm83`, and multiple abandoned‑mine, floodplain, fault, and geology layers represent critical infrastructure and environmental risk features.

- **Facilities and civic entities.**  
  Collections such as `geodbhospitalswvdem040519utm83`, `gedbnursinghomeswvdem041219utm83`, `geodbfiredeptwvdem092017utm83`, `geodbpolicedeptwvdem012319utm83`, `geodbcountycityparkboundaries20201104utm83`, as well as collections for libraries, schools, and public health departments, represent facilities and services with direct implications for community well‑being.

- **Historic and governance‑relevant features.**  
  Collections capturing National Register of Historic Places points and polygons, courthouses, county seats, empowerment zones, and community‑defined boundaries provide context for spatial justice and heritage‑related analysis.

For nearly every `geodb*` collection, there is a corresponding `gedb*` collection, such as `geodbblockscensus2020utm83` and `gedbblockscensus2020utm83`. The `geodb*` collections hold embeddings and base metadata keyed to PostGIS feature identifiers. The `gedb*` collections serve as stable alias layers, often with simple placeholder documents and copied metadata, so that higher‑level services can depend on consistent collection names and schemas even as ingestion pipelines evolve.

Together, the `geodb*` and `gedb*` families form the Hilbert‑space representation of Ms. Jarvis’s spatial body and align directly with the PostGIS tables described in the GBIM and GeoDB chapters.

---

### 5.4 From Hilbert Space to ChromaDB

ChromaDB provides the concrete realization of the Hilbert‑space state described in the previous chapter.

- **Embeddings as vectors.**  
  The embedding model maps texts and entities into high‑dimensional real vectors. ChromaDB stores these vectors alongside metadata (such as identifiers, timestamps, entity types, and geographic tags) and exposes operations such as nearest‑neighbor search, filtered retrieval, and upsert.

- **Collections as subspaces.**  
  Each ChromaDB collection corresponds to an empirically instantiated subset of the Hilbert space `H_App`, grouping related vectors by purpose (for example, governance, conversation, thesis) or by entity type (for example, blocks, buildings, mines, dams, or facilities). Conceptually, each collection spans a subspace of `H_App`.

- **Queries as projections.**  
  Incoming queries are embedded and used to probe relevant collections. This process effectively projects each query into the appropriate subspace, retrieves nearby vectors with respect to the inner‑product‑induced similarity measure, and returns associated documents and metadata for downstream reasoning.

This mapping allows Ms. Jarvis’s memory to be described both geometrically, in terms of subspaces and projections, and operationally, in terms of concrete collection queries and metadata filters.

---

### 5.5 Embedding Model and Dimensionality

In the RAG stack under analysis, Ms. Jarvis uses a sentence‑embedding model with 384‑dimensional outputs (for example, a SentenceTransformer such as `all-MiniLM-L6-v2`) as the primary text embedding channel. A simple inspection script confirms the dimensionality of the embedding vectors; this dimension defines the ambient dimension of the main `H_text` component for text‑based collections.

Any Chroma collection that stores embeddings produced by this model must be configured to accept 384‑dimensional vectors. This requirement applies both to general semantic collections and to GeoDB‑derived collections, which use consistent text embeddings for feature descriptions, attribute summaries, and linked narrative content.

In the examined deployment:

- GeoDB‑derived `geodb*` collections are embedded at the standard dimensionality and aliased into corresponding `gedb*` collections.
- Several general semantic collections, including portions of `mountainshares_knowledge`, `thesis_materials`, and older memory collections, hold complete document and metadata records, with embedding backfill either completed or in progress as documented in the system registry.

The chapter therefore treats 384‑dimensional embeddings as the standard for the main semantic channel, while recognizing that additional channels or model upgrades may be introduced in future, along with corresponding schema and migration procedures.

---

### 5.6 ChromaDB Clients and Deployment Topology

ChromaDB is accessed both as a shared HTTP service and, historically, as per‑service local stores. The architecture is transitioning toward a unified, HTTP‑backed deployment as the canonical semantic memory.

#### 5.6.1 Shared HTTP Service

In the active environment, services connect to a shared ChromaDB instance through an HTTP client configured with explicit host, port, and telemetry settings. In pseudocode:

- a client is created against the shared host,
- collections are listed and retrieved by name, and
- ingestion scripts, GeoDB ETL pipelines, RAG gateways, and other services use this client to upsert and query vectors.

This shared instance exposes both the general semantic collections and the `geodb*` / `gedb*` spatial collections. It is bound to a persistent on‑disk directory, and its configuration is recorded in the system configuration registry to support reproducibility and backup.

#### 5.6.2 Historical and Auxiliary Persistent Clients

Historically, some services used `PersistentClient` instances pointing to per‑service local paths such as `.chromadb` or `chroma_db`. These local stores were used for:

- isolated experiments and unit tests,
- service‑specific memory (such as early autonomous learner experiments or social‑media‑related data), and
- transitional states prior to consolidation into the shared instance.

As of late 2025 and early 2026, the operational intent is to converge on the shared HTTP‑backed store for primary semantic memory, including GeoDB embeddings. Residual local stores are treated as legacy or experimental; their contents are either migrated or preserved as snapshots with clear documentation of their status.

---

### 5.7 Integration with GBIM, GeoDB, and RAG

ChromaDB is tightly integrated with GBIM, the GeoDB layer, and the broader RAG pipeline.

- **GBIM linkage.**  
  GBIM entities—including places, infrastructures, institutions, persons, and policies—reference Chroma collections through stable identifiers and metadata fields. For spatial entities, `geodb*` collections store feature‑level embeddings and metadata keyed to PostGIS tables; for non‑spatial entities, general collections such as `mountainshares_knowledge` or `ms_jarvis_memory` store associated documents and summaries. This linkage allows GBIM entities to be mapped into `H_App` and retrieved by semantic or spatial criteria.

- **GeoDB integration.**  
  The GeoDB ETL pipeline reads per‑feature attributes from PostGIS, constructs embeddings, and upserts them into `geodb*` collections before creating aliases in `gedb*`. Keys and metadata—including source table, primary key, geometry tags, and classification fields—allow retrieval results to be rejoined to GBIM entities and geometries. This process ensures that ChromaDB remains synchronized with the spatial database for the prioritized layers.

- **RAG context building.**  
  When Ms. Jarvis answers a question, the RAG pipeline uses ChromaDB to retrieve relevant documents and feature‑level embeddings. Retrieved texts, metadata, and spatial identifiers are combined into context windows for the language models, with filtering by collection, geography, topic, and source. This behavior implements the context subspace selection and `H_eff` restriction described in the Hilbert‑space chapter.

- **Governance‑specific retrieval.**  
  For MountainShares‑related queries, retrieval is scoped to `mountainshares_knowledge` and closely related collections, optionally intersected with relevant GeoDB layers. This keeps responses grounded in published rules, local economic context, and spatial justice considerations, rather than generic web material or unrelated training data.

The end‑to‑end pipeline thus behaves as a structured walk through curated, domain‑specific memory organized around GBIM, the GeoDB spatial body, and Quantarithmia’s research concepts.

---

### 5.8 Query Paths and JSON Structures

To connect the conceptual description with concrete operations, this section outlines canonical request and response shapes. Schemas are expressed in a language‑agnostic way and implemented in gateway and service code using typed models.

#### 5.8.1 Gateway‑Level Request Shape

Gateway or bridge services conceptually receive simplified query objects containing at least:

- a target collection or collection family (for example, `mountainshares_knowledge`),
- a natural‑language query string, and
- a desired number of results.

Additional fields may specify roles, geographic filters, or constraint flags. The gateway translates these objects into lower‑level Chroma queries, adding appropriate `where` and `include` parameters and routing to the correct collection.

#### 5.8.2 Chroma Query Request and Response

At the Chroma level, a typical query against a collection includes:

- `query_texts`: a list of query strings to embed and search,
- `n_results`: the number of nearest neighbors to return per query,
- `where`: an optional metadata filter (for example, `{"entity_type": "organization"}` or spatial tags), and
- `include`: a list specifying which fields to return (for example, `["metadatas", "documents", "distances"]`).

The JSON request body follows Chroma’s documented schema. The response contains parallel lists for identifiers, documents, metadata, distances, and, when configured, embeddings. In collections where embeddings are not present for every item, the embeddings field may be null or sparsely populated while documents and metadata remain fully populated. Downstream components are written to handle these cases explicitly.

These request and response structures provide concrete anchors for documentation, testing, and debugging, and they make it possible to trace RAG behavior end‑to‑end.

---

### 5.9 Operational Considerations

Using ChromaDB as a production memory layer introduces several practical considerations that must be documented and maintained.

- **Reliability and persistence.**  
  The main Chroma instance is bound to a persistent on‑disk directory. Regular backups are required, and backup scripts may also snapshot residual local `.chromadb` directories from earlier stores to preserve historical data during consolidation. Restoration procedures are documented alongside the registry of collections and embeddings.

- **Performance and scaling.**  
  As collections grow—including large GIS corpora, extensive learner outputs, and thesis materials—index configuration and hardware resources directly affect query latency. Chroma’s approximate nearest‑neighbor indices (such as HNSW) are configured explicitly, and query defaults are tuned so that requests remain predictable even when approaching the current number of stored items. Monitoring tracks query volumes and latencies per collection.

- **Security and privacy.**  
  The documented Chroma deployment is treated as documentation‑ and research‑oriented, with an explicit exclusion of sensitive user data, private keys, and non‑consensual logs. Collections such as `conversations` and `ms_jarvis_memory` are curated, and sensitive content may be redacted, summarized, or omitted entirely before any public export or external analysis.

- **Schema and configuration management.**  
  Collection names, metadata schemas, and embedding configurations are versioned and recorded in a central registry. Any changes to models, dimensions, or index parameters are treated as schema migrations, with forward‑ and backward‑compatibility considerations documented.

These operational details connect the conceptual role of ChromaDB to the realities of running a live, research‑grade governance and advisory system.

---

### 5.10 Limitations and Future Work

Current use of ChromaDB has several limitations and active areas of work:

- **Partial embedding coverage in some domains.**  
  GeoDB‑derived `geodb*` collections are fully embedded and aliased into `gedb*` collections for the prioritized layers. Some general semantic collections, including portions of `mountainshares_knowledge`, `thesis_materials`, and older memory collections, contain complete document and metadata records but only partial embedding coverage. Backfill and recomputation plans are documented and tracked.

- **Model and index dependence.**  
  Retrieval quality depends on the chosen embedding model (currently a 384‑dimensional sentence‑embedding model), index parameters, and collection design. Changes to any of these elements can alter the Steward System’s apparent memory. Model upgrades and reindexing are therefore treated as explicit migrations with before/after evaluation.

- **Semantic gaps and representational limits.**  
  Certain forms of knowledge—such as embodied experience, collective trauma narratives, and spiritual traditions—are difficult to represent as short text embeddings alone. Additional representational strategies, including graph structures, qualitative annotations, GBIM‑linked justice metrics, and community‑led tagging, are needed to supplement the vector store.

- **Evolving schema and topology.**  
  As GBIM, GeoDB, and Quantarithmia evolve, the set of collections, metadata fields, and indexing strategies will continue to change. Migration tools and versioned schemas are necessary to maintain continuity across thesis revisions and deployments, including clear documentation of the point at which historical local stores were consolidated into the shared HTTP‑backed instance.

Future work includes:

- completing embedding backfill for all key general collections with clearly documented embedding functions and dimensions,
- documenting all collection names, metadata schemas, and embedding configurations in a single, queryable registry,
- adding traced end‑to‑end examples of RAG flows that show precisely how Chroma retrieval augments queries in different roles and geographies, and
- exploring hybrid memory architectures that combine vector stores with graphs, relational databases, and participatory annotation workflows, so that communities can inspect and shape what is stored and how it is used.

An implementation‑status badge for this chapter is therefore: **PARTIAL / CONSOLIDATING**. The conceptual role of ChromaDB as semantic memory is implemented through a shared HTTP‑backed Chroma service with extensive `geodb*` and `gedb*` spatial collections and several core general collections. Historical per‑service stores, full embedding coverage in governance and thesis domains, and complete end‑to‑end RAG traces are in the process of consolidation and documentation.
