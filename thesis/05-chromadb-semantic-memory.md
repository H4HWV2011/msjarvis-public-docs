# ChromaDB as Semantic Memory

This chapter explains how Ms. Egeria Jarvis uses ChromaDB as the primary semantic memory layer backing the Hilbert-space state, GBIM, and the broader semantic fabric. ChromaDB is a vector database: it stores high-dimensional embedding vectors with associated metadata and enables efficient similarity search over them. In this system, ChromaDB is not just a convenience library; it is the concrete implementation of long-term, queryable memory for documents, GIS features, governance texts, and thesis materials.

Within the thesis, ChromaDB is treated as the bridge between abstract Hilbert-space state and actual stored knowledge: it is where beliefs, contexts, and references are made durable and retrievable for reasoning and retrieval-augmented generation (RAG).

## Role in Ms. Jarvis Architecture

In the Ms. Jarvis architecture, ChromaDB plays several key roles:

- Semantic memory store:
  - Embeddings of texts, geospatial entities, and other artifacts are stored in collections, each corresponding to a particular domain (for example, GIS, governance, thesis, learner outputs, and conversational memory).
- Retrieval engine:
  - At query time, services project inputs into the embedding space and use ChromaDB similarity search to retrieve the most relevant items for context and reasoning.
- Structural backbone:
  - Because collections and metadata are explicitly defined, ChromaDB’s structure mirrors core parts of GBIM and the thesis organization, making it easier to reason about what Ms. Jarvis knows and how that knowledge is organized.

This design makes the memory system inspectable: researchers can see collections, document counts, and metadata, rather than relying on opaque, hidden state.

## Collections and Data Domains

In the live deployment examined in early 2026, the primary Chroma instance exposes a concrete set of collections, including:

`
[
  "conversations",
  "shapefile_features",
  "spiritual_wisdom",
  "research_history",
  "autonomous_learning",
  "census_points",
  "default",
  "mountainshares_knowledge",
  "user_memory_vectors",
  "gis_geospatial",
  "ms_jarvis_memory"
]
' 

These collections correspond to distinct data domains:

- **Geospatial collections:**
  - `gis_geospatial`, `shapefile_features`, and `census_points` hold GIS-derived content (features, census points, and related spatial attributes) that ground GBIM entities in physical space.

- **Governance and norms:**
  - `mountainshares_knowledge` stores MountainShares rules, constitutional principles, and related governance texts, providing a focused corpus for economic and governance questions.

- **Learner and research history:**
  - `autonomous_learning` and `research_history` store web-research outputs and per-cycle summaries emitted by the autonomous learner, capturing what was studied and when.

- **Conversations and user memory:**
  - `conversations` and `ms_jarvis_memory` store interaction snippets and higher-level conversational memory; `user_memory_vectors` provides a more explicit vectorized user-memory layer used by certain bridges.

- **Spiritual and contextual materials:**
  - `spiritual_wisdom` stores spiritual and reflective texts that inform the qualitative and ethical framing of responses.

- **Default and auxiliary:**
  - `default` serves as a generic or temporary collection used by development and diagnostic utilities.

In some collections, embeddings are fully populated and used for similarity search; in others (for example, `mountainshares_knowledge` in the current snapshot), documents and metadata are present but embeddings are not yet attached for all items, reflecting an ongoing migration from document-only to fully embedded memory.

Each collection stores documents plus metadata such as IDs, source type, timestamps, and geography tags, allowing queries to be filtered or scoped by domain, time, and place. Where embeddings are present, these collections operate as true vector subspaces; where embeddings are not yet present, they still function as structured, filterable document stores that can be upgraded to full semantic memory later.

## From Hilbert Space to ChromaDB

Conceptually, ChromaDB is one concrete realization of the Hilbert-space state described in the surrounding chapters:

- **Embeddings as vectors:**
  - The embedding model maps texts and entities into a high-dimensional vector space; ChromaDB stores these vectors and exposes operations like nearest-neighbor search.

- **Collections as subspaces:**
  - Each ChromaDB collection corresponds to a subspace or region of the overall Hilbert space, grouping related vectors by purpose and domain.

- **Queries as projections:**
  - Incoming queries are embedded and then used to probe the relevant collections, effectively projecting the query into the appropriate subspace and retrieving nearby vectors for further reasoning.

This mapping lets the thesis describe Ms. Jarvis’s memory both geometrically (in terms of Hilbert space) and operationally (in terms of stored vectors and queries).

## Embedding Model and Dimension

In the RAG stack currently under analysis, Ms. Jarvis uses a SentenceTransformer model to produce text embeddings for semantic search:


python3 - << 'PY'
from sentence_transformers import SentenceTransformer
m = SentenceTransformer("all-MiniLM-L6-v2")
v = m.encode("test")
print("SentenceTransformer dim:", v.shape)
PY

# Output:
# SentenceTransformer dim: 384
The chosen embedding model is therefore:

- Model: `all-MiniLM-L6-v2`
- Dimensionality: 384

This dimensionality defines the Hilbert-space dimension for the main text-embedding channel used in RAG. Any Chroma collection that stores embeddings produced by this model must be configured to accept 384-dimensional vectors. At the time of inspection, some collections (for example, `mountainshares_knowledge`) respond to queries with `embeddings: null` while still returning structured `documents`, `metadatas`, and `distances` lists, which indicates that those collections are currently operating in a document/metadata-only mode. The chapter therefore treats 384-dimensional embeddings as the intended standard, while acknowledging that backfill and full adoption are still underway.

## ChromaDB Implementation and Clients

ChromaDB is accessed both as a shared HTTP service and, historically, as per-service local stores.

### Shared HTTP Service

In the active environment, services connect to a shared ChromaDB instance via an HTTP client. The typical pattern is:

python
import chromadb
from chromadb.config import Settings

client = chromadb.HttpClient(
    host="localhost",
    port=8002,
    settings=Settings(anonymized_telemetry=False),
)
print("Collections:", [c.name for c in client.list_collections()])

This client is used by scripts and services that treat Chroma as a central semantic memory server. The live instance exposes the collections listed earlier and serves as the main Hilbert-space gateway for retrieval.

## Historical and Auxiliary Persistent Clients

Other services, especially those responsible for ingestion and specialized domains (such as Facebook integration, autonomous learning, and bulk loaders), have historically used `chromadb.PersistentClient` against container-local paths (for example, `.chromadb` or `chroma_db`):

python
import chromadb

client = chromadb.PersistentClient(path=".chromadb")
collection = client.get_collection("ms_jarvis_memory")

These local stores have been used for:

- Isolated experiments and unit tests.
- Service-specific memory (for example, Facebook post performance or internal learners).
- Transitional states prior to consolidation into the main shared instance.

As of late 2025 and early 2026, the operational intent is to converge on the shared HTTP-backed store for primary semantic memory, while carefully managing any remaining per-service stores and migration paths. The chapter therefore distinguishes between the conceptually unified semantic memory and the still-mixed implementation reality.

## Integration with GBIM and RAG

ChromaDB is tightly integrated with GBIM and the broader RAG pipeline:

- **GBIM linkage:**
  - Geospatial entities in GBIM (such as districts, facilities, infrastructures, and other spatial units) have associated documents and, where configured, embeddings stored in collections like `gis_geospatial`, `shapefile_features`, and `census_points`. Metadata links these records back to their geospatial representations and evidence sources.

- **RAG context building:**
  - When Ms. Jarvis answers a question, the RAG pipeline uses ChromaDB to pull relevant documents and, when available, embeddings and distances. Retrieved texts and metadata are assembled into context windows for the language models, with filtering by collection, geography, topic, and source.

- **Governance-specific retrieval:**
  - For MountainShares-related queries, retrieval is scoped to `mountainshares_knowledge` and closely related collections, ensuring that responses are grounded in published rules, local economic context, and spatial justice considerations rather than generic web search.

The pipeline therefore acts as a structured walk through a curated, domain-specific memory organized around GBIM and Quantarithmia.

## Query Paths and JSON Structures

To connect the conceptual description with concrete operations, this section gives canonical JSON structures that match the observed system.

### Gateway-Level Request Shape

Gateway or bridge services (such as a unified RAG or chroma gateway) conceptually receive simplified query objects. A typical request schema is:

python
from pydantic import BaseModel

class QueryRequest(BaseModel):
    collection: str
    query: str
    n_results: int

req = QueryRequest(
    collection="mountainshares_knowledge",Which yields the gateway-level JSON:

json
{
  "collection": "mountainshares_knowledge",
  "query": "Fayette County Community Arts Center",
  "n_results": 5
}

This object is then translated into a lower-level Chroma query.

### Chroma Query Request Body

Given a live Chroma client and a selected collection, a typical query looks like:

import chromadb
from chromadb.config import Settings

client = chromadb.HttpClient(
    host="localhost",
    port=8002,
    settings=Settings(anonymized_telemetry=False),
)
col = client.get_collection("mountainshares_knowledge")

res = col.query(
    query_texts=["Fayette County Community Arts Center"],
    n_results=3,
    where={"entity_type": "organization"},
)
print(res)

The corresponding HTTP JSON body sent to Chroma’s /api/v1/collections/{collection_id}/query endpoint takes the form:



    query="Fayette County Community Arts Center",
    n_results=5,
)
print(req.model_dump_json(indent=2))

{
  "query_texts": [
    "Fayette County Community Arts Center"
  ],
  "n_results": 3,
  "where": {
    "entity_type": "organization"
  },
  "include": [
    "metadatas",
    "documents",
    "distances"
  ]
}

The response contains parallel lists for ids, documents, metadatas, distances, and optionally embeddings (when an embedding function is configured) and uris or other fields when enabled. In collections where embeddings are not yet present, the embeddings field may be null while the remaining structures are still populated.

These two JSON structures—gateway-level request and Chroma-level query body—provide concrete, drop-in examples for documentation and debugging.

## Operational Considerations

Using ChromaDB as a production memory layer introduces practical concerns:

- **Reliability and persistence:**
  - The main Chroma instance is bound to a persistent on-disk directory mounted into the `chromadb` container and must be backed up regularly. Backup scripts can also snapshot the `.chromadb` directories associated with earlier local stores to ensure no historical data is lost during consolidation.

- **Performance and scaling:**
  - As collections grow (large GIS corpora, expansive learner outputs, thesis materials), index choice and hardware resources directly affect query latency. Chroma’s local persistent HNSW index is used by default; warnings about requesting more results than available items highlight the need for monitoring and index-size-aware query defaults.

- **Security and privacy:**
  - The documented Chroma deployment is treated as documentation- and research-only: sensitive user data, private keys, and non-consensual logs are excluded by design. Collections like `conversations` and `ms_jarvis_memory` are curated and may be redacted or summarized before being included in public exports.

These details link the conceptual role of ChromaDB to the realities of running a live, research-grade governance and advisory system.

## Limitations and Future Work

Current use of ChromaDB has several limitations:

- **Partial embedding coverage:**
  - Some collections (for example, `mountainshares_knowledge`) currently return `embeddings: null` and empty or sparse result sets for certain queries, suggesting that the embedding and ingestion pipeline has not yet been fully applied to all domains.

- **Model and index dependence:**
  - Retrieval quality depends on the choice of embedding model (`all-MiniLM-L6-v2` at 384 dimensions), index parameters, and collection design; changes to any of these can alter Ms. Jarvis’s apparent memory and must be managed as schema and model migrations.

- **Semantic gaps:**
  - Certain forms of knowledge (embodied experience, collective trauma narratives, spiritual traditions) are difficult to represent solely as short text embeddings. Additional representational strategies (graph structures, qualitative annotations, and community-led tagging) are needed.

- **Evolving schema:**
  - As GBIM and Quantarithmia evolve, the set of collections, metadata fields, and indexing strategies will continue to change. Migration tools and versioned schemas are necessary to maintain continuity across thesis revisions and deployments.

Future work includes:

- Completing backfill of embeddings for all key collections with coherent, documented embedding functions.
- Documenting all collection names, metadata schemas, and embedding dimensions in a single schema registry, including how they map to GBIM entities and thesis concepts.
- Adding traced end-to-end examples of RAG flows showing how Chroma retrieval augments queries and how those traces are logged and inspected.
- Exploring hybrid memory architectures that combine vector stores with graphs, relational databases, and participatory annotation workflows, enabling communities to inspect and shape what is stored and how it is used.

## Empirical Validation (Late 2025 – Early 2026)

### Multi-Instance Topology

Multiple ChromaDB instances have been observed in the Docker and virtual environment topology over time, including:

- Shared HTTP-backed Chroma accessible on a well-known port (for example, `8002`) via `HttpClient`.
- Historical per-service persistent stores (for example, `.chromadb` and `chroma_db` paths bound into individual containers).
- Experimental or legacy instances used for testing and development.

This history reflects a transition from earlier, fragmented experiments toward the consolidated shared layout described in this chapter. The precise roles of each historical instance and the full flow of RAG writes across them have been partially characterized and remain an active subject of trace analysis and refactoring.

### RAG Storage Pipeline

The RAG and “ULTIMATE” pipelines are designed so that final responses, intermediate contexts, or both can be written into Chroma-backed collections for later retrieval and analysis. In practice, this includes:

- Storing learner outputs and research histories into `autonomous_learning` and `research_history`.
- Storing governance-relevant texts and annotations into `mountainshares_knowledge`.
- Storing selected conversational or reflective material into `conversations`, `ms_jarvis_memory`, and `user_memory_vectors`.

Because of the evolving topology, the exact target instance and collection for each write path must be confirmed by inspecting the main-brain RAG handlers, gateway services, and associated Chroma client configuration.

### Implementation Status Badge

🔄 **PARTIAL** — The conceptual role of ChromaDB as semantic memory is implemented via a shared HTTP-backed Chroma service and several core collections, but the multi-instance topology, full set of collection schemas, embedding coverage, and end-to-end RAG traces are still being consolidated and documented.

### Future Work

- Add traced examples showing RAG retrieval enhancing queries with prior context from ChromaDB, including real gateway logs and Chroma HTTP bodies.
- Finalize documentation of all collection names, metadata schemas, and embedding dimensions used in the live system, with clear versioning and migration plans.
- Specify the embedding models currently in use and document how model changes (for example, moving beyond `all-MiniLM-L6-v2`) will be handled, including re-embedding and index migration strategies.
- Provide a ChromaDB collection schema diagram that links GBIM entities, governance documents, and thesis materials to their collections and metadata fields, and indicates which collections are fully embedded versus document-only at each major thesis milestone.
