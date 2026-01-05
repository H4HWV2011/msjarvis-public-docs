# ChromaDB as Semantic Memory

This chapter explains how Ms. Egeria Jarvis uses ChromaDB as the primary semantic memory layer backing the Hilbert‑space state, GBIM, and the broader semantic fabric. ChromaDB functions as a vector database that stores high‑dimensional embedding vectors with associated metadata and enables efficient similarity search. In this system, ChromaDB is not just a convenience library; it is the concrete implementation of long‑term, queryable memory for documents, GIS features, governance texts, autonomous‑learning traces, and thesis materials.

Within the thesis, ChromaDB is treated as the bridge between abstract Hilbert‑space state and actual stored knowledge. It is the place where beliefs, contexts, and references become durable and retrievable for reasoning and retrieval‑augmented generation (RAG).

## Role in the Ms. Jarvis Architecture

In the Ms. Jarvis architecture, ChromaDB plays several key roles.

- **Semantic memory store (non‑spatial)**  
  Embeddings of texts and artifacts live in collections that correspond to domains such as governance, thesis content, autonomous learner outputs, conversations, and user memory.

- **Geospatial Hilbert layer (spatial)**  
  A large family of `geodb*` and `gedb*` collections holds embeddings and metadata for West Virginia geospatial features, mirroring PostGIS tables and providing the Hilbert‑space representation of the spatial body described in Chapter 6.

- **Retrieval engine**  
  At query time, services project inputs into the embedding space and use ChromaDB similarity search to retrieve the most relevant items for context and reasoning.

- **Structural backbone**  
  Because collections and metadata are explicitly defined, ChromaDB’s structure mirrors core parts of GBIM, the GeoDB layer, and the thesis organization. This makes it easier to understand what the Steward System knows and how that knowledge is organized.

This design makes the memory system inspectable; researchers can see collections, document counts, and metadata rather than relying on hidden internal state.

## Collections and Data Domains

In the live deployment examined in late 2025 and early 2026, the primary Chroma instance exposes a concrete set of collections that fall into two broad families: general semantic memory and GeoDB‑derived spatial memory.

### General Semantic Collections

Representative general collections include

- `conversations`  
- `ms_jarvis_memory`  
- `user_memory_vectors`  
- `autonomous_learning`  
- `research_history`  
- `mountainshares_knowledge`  
- `spiritual_wisdom`  
- `thesis_materials` (or an equivalent thesis collection)  
- `default`  
- `smaller auxiliary collections used for development and diagnostics`  

These collections correspond to distinct data domains.

- **Conversations and user memory**  
  `conversations`, `ms_jarvis_memory`, and `user_memory_vectors` store selected interaction snippets, higher‑level conversational summaries, and explicit user‑memory embeddings used by certain agents and bridges.

- **Governance and norms**  
  `mountainshares_knowledge` stores MountainShares rules, constitutional principles, governance deliberation texts, and related commentary, providing a focused corpus for economic and governance questions.

- **Learner and research history**  
  `autonomous_learning` and `research_history` store web‑research outputs, per‑cycle summaries, and RAG traces emitted by the autonomous learner, capturing what was studied, when it was studied, and why it was studied.

- **Spiritual and contextual materials**  
  `spiritual_wisdom` stores spiritual, reflective, and contextual texts that inform the qualitative and ethical framing of responses.

- **Thesis and internal materials**  
  Collections such as `thesis_materials` hold drafts, notes, and supporting texts referenced within the Quantarithmia research program.

In some of these collections, embeddings are fully populated and used for similarity search. In others, especially certain governance or thesis collections, documents and metadata are present but embeddings are still being backfilled.

### GeoDB‑Derived `geodb*` and `gedb*` Collections

A second, much larger family of collections is generated automatically from the PostGIS GeoDB.

Examples include

- `geodbblockscensus2020utm83`, `geodbblockgroupscensus2020utm83`, and their `wma84` variants  
- `geodbboundaryappalachianbasinwvges1996utm83`, `geodbbridges`, and similar infrastructure layers  
- hazard layers such as `geodbminesabandonedlandslinewvdep1996noprojectoin`, `geodbminesabandonedlandspolygonwvdep1996noprojection`, `geodbdamsusarmycorpsofengineers200010utm83`, `geodbdamsnoncoalusgs2002utm83`, floodplain structures, faults, geology, and related themes  
- civic and facility layers such as `geodbhospitalswvdem040519utm83`, `gedbnursinghomeswvdem041219utm83`, `geodbfiredeptwvdem092017utm83`, `geodbpolicedeptwvdem012319utm83`, `geodbcountycityparkboundaries20201104utm83`, along with libraries, schools, and public health departments  
- governance and boundary layers such as regional planning councils, ZIP code tabulation areas, county seats, courthouses, National Register points and polygons, empowerment zones, and community‑defined boundaries  

For nearly every such `geodb*` collection, there is a corresponding aliased `gedb*` collection, such as `geodbblockscensus2020utm83` and `gedbblockscensus2020utm83`. The `geodb*` collections hold embeddings and base metadata keyed to PostGIS feature identifiers. The `gedb*` collections provide a stable alias layer, often with simple placeholder documents and copied metadata, which higher‑level services can use without coupling directly to ingestion internals.

Together, these collections form the Hilbert‑space representation of Ms. Jarvis’s spatial body and align directly with the PostGIS tables described in Chapter 6.

## From Hilbert Space to ChromaDB

ChromaDB provides a concrete realization of the Hilbert‑space state described in the surrounding chapters.

- **Embeddings as vectors**  
  The embedding model maps texts and entities into a high‑dimensional vector space. ChromaDB stores these vectors and exposes operations such as nearest‑neighbor search.

- **Collections as subspaces**  
  Each ChromaDB collection corresponds to a subspace or region of the overall Hilbert space, grouping related vectors by purpose, such as governance or conversation, or by entity type, such as blocks, buildings, mines, dams, or facilities.

- **Queries as projections**  
  Incoming queries are embedded and then used to probe the relevant collections. This process effectively projects each query into the appropriate subspace and retrieves nearby vectors for further reasoning.

This mapping lets the thesis describe Ms. Jarvis’s memory in geometric terms and in operational terms at the same time.

## Embedding Model and Dimension

In the RAG stack under analysis, Ms. Jarvis uses a SentenceTransformer model to produce text embeddings for semantic search.

python3 - << 'PY'
from sentence_transformers import SentenceTransformer
m = SentenceTransformer("all-MiniLM-L6-v2")
v = m.encode("test")
print("SentenceTransformer dim:", v.shape)
PY
# Output
# SentenceTransformer dim: 384

The chosen embedding model has the following properties.

    Model all-MiniLM-L6-v2

    Dimensionality 384

This dimensionality defines the Hilbert‑space dimension for the main text‑embedding channel used in RAG. Any Chroma collection that stores embeddings produced by this model must accept 384‑dimensional vectors.

In the current deployment, the GeoDB‑derived geodb* collections are fully embedded at 384 dimensions and aliased into corresponding gedb* collections. Several general semantic collections, such as parts of mountainshares_knowledge or some thesis and governance collections, still contain documents and metadata for all items, with embedding backfill and recomputation underway. The chapter therefore treats 384‑dimensional embeddings as the standard while noting that backfill and potential future model upgrades remain active work.

## ChromaDB Implementation and Clients

ChromaDB is accessed both as a shared HTTP service and, historically, as per‑service local stores.
Shared HTTP Service

In the active environment, services connect to a shared ChromaDB instance through an HTTP client. A typical pattern is

python
import chromadb
from chromadb.config import Settings

client = chromadb.HttpClient(
    host="localhost",
    port=8002,
    settings=Settings(anonymized_telemetry=False),
)
print("Collections", [c.name for c in client.list_collections()])

This client is used by ingestion scripts, GeoDB ETL pipelines, RAG gateways, and other services that treat Chroma as a central semantic memory server. The live instance exposes both the general collections and the large family of geodb* and gedb* collections described above.
Historical and Auxiliary Persistent Clients

Other services, especially those responsible for earlier ingestion experiments and specialized domains, have historically used chromadb.PersistentClient against container‑local paths such as .chromadb or chroma_db.

python
import chromadb

client = chromadb.PersistentClient(path=".chromadb")
collection = client.get_collection("ms_jarvis_memory")

These local stores have supported isolated experiments and unit tests, service‑specific memory such as early learner experiments or social‑media‑related data, and transitional states before consolidation into the main shared instance. As of late 2025 and early 2026, the operational intent is to converge on the shared HTTP‑backed store for primary semantic memory, including GeoDB embeddings. The conceptual description in this chapter refers to the unified logical memory; any residual local stores are treated as legacy or experimental.
Integration with GBIM, GeoDB, and RAG

ChromaDB is tightly integrated with GBIM, the GeoDB layer, and the broader RAG pipeline.

# GBIM linkage
GBIM entities, including places, infrastructures, institutions, persons, and policies, reference Chroma collections through stable identifiers and metadata. For spatial entities, geodb* collections store feature‑level embeddings and metadata keyed to PostGIS tables. For non‑spatial entities, general collections such as mountainshares_knowledge or ms_jarvis_memory store associated documents and summaries.

# GeoDB integration
The GeoDB ETL pipeline reads per‑feature attributes from PostGIS, constructs embeddings, and upserts them into geodb* collections before creating aliases in gedb*. Keys and metadata, including source table, primary key, and location tags, allow results to be rejoined to GBIM entities and geometries.

# RAG context building
When Ms. Jarvis answers a question, the RAG pipeline uses ChromaDB to pull relevant documents and feature‑level embeddings. Retrieved texts, metadata, and spatial identifiers are combined into context windows for the language models, with filtering by collection, geography, topic, and source.

# Governance‑specific retrieval
For MountainShares‑related queries, retrieval scopes to mountainshares_knowledge and closely related collections. This keeps responses grounded in published rules, local economic context, and spatial justice considerations instead of generic web material.

The pipeline therefore behaves as a structured walk through curated, domain‑specific memory organized around GBIM, the GeoDB spatial body, and Quantarithmia’s research concepts.
Query Paths and JSON Structures

To connect the conceptual description with concrete operations, this section outlines canonical request and response shapes.
Gateway‑Level Request Shape

Gateway or bridge services conceptually receive simplified query objects. A typical request schema looks like this.

python
from pydantic import BaseModel

class QueryRequest(BaseModel):
    collection: str
    query: str
    n_results: int

req = QueryRequest(
    collection="mountainshares_knowledge",
    query="Fayette County Community Arts Center",
    n_results=5,
)
print(req.model_dump_json(indent=2))

This prints
`
json
{
  "collection": "mountainshares_knowledge",
  "query": "Fayette County Community Arts Center",
  "n_results": 5
}
`
The gateway translates this object into a lower‑level Chroma query.
Chroma Query Request Body

Given a live Chroma client and a selected collection, a typical query looks like this.

python
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
    include=["metadatas", "documents", "distances"],
)
print(res)

The corresponding HTTP JSON body sent to Chroma’s query endpoint takes the following form.
`
json
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
`
The response contains parallel lists for identifiers, documents, metadata, distances, and, when configured, embeddings. In collections where embeddings are not present for every item, the embeddings field may be null or sparsely populated while the remaining structures are fully populated.

These two JSON structures, the gateway‑level request and the Chroma‑level query body, provide concrete examples for documentation and debugging.
Operational Considerations

Using ChromaDB as a production memory layer introduces several practical concerns.

#  Reliability and persistence
The main Chroma instance is bound to a persistent on‑disk directory and must be backed up regularly. Backup scripts can also snapshot any residual .chromadb directories from earlier local stores to preserve historical data during consolidation.

#  Performance and scaling
As collections grow, including large GIS corpora, extensive learner outputs, and thesis materials, index configuration and hardware resources directly affect query latency. Chroma’s HNSW‑based indexing is used by default, and query defaults are tuned so that requests remain predictable even when asking for more results than the current number of stored items.

# Security and privacy
 The documented Chroma deployment is treated as documentation‑ and research‑oriented. Sensitive user data, private keys, and non‑consensual logs are excluded by design. Collections such as conversations and ms_jarvis_memory are curated and may be redacted or summarized before any public export.

These details connect the conceptual role of ChromaDB to the realities of running a live, research‑grade governance and advisory system.
Limitations and Future Work

Current use of ChromaDB has several limitations.

# Partial embedding coverage in non‑GeoDB domains
GeoDB‑derived geodb* collections are fully embedded and aliased. Some general semantic collections, including portions of mountainshares_knowledge, thesis_materials, and older memory collections, still hold documents and metadata with incomplete embedding backfill.

# Model and index dependence
Retrieval quality depends on the chosen embedding model, currently all-MiniLM-L6-v2 at 384 dimensions, along with index parameters and collection design. Changes to any of these elements can alter the Steward System’s apparent memory and must be handled as explicit schema and model migrations.

# Semantic gaps
Certain forms of knowledge, such as embodied experience, collective trauma narratives, and spiritual traditions, are difficult to represent as short text embeddings alone. Additional representational strategies, including graph structures, qualitative annotations, GBIM‑linked justice metrics, and community‑led tagging, are needed.

# Evolving schema and topology
As GBIM, GeoDB, and Quantarithmia evolve, the set of collections, metadata fields, and indexing strategies will continue to change. Migration tools and versioned schemas are necessary to maintain continuity across thesis revisions and deployments, including clear documentation of the point at which historical local stores were consolidated into the shared HTTP‑backed instance.

Future work includes completing embedding backfill for all key general collections with documented embedding functions, documenting all collection names, metadata schemas, and embedding dimensions in a single registry, adding traced end‑to‑end examples of RAG flows that show how Chroma retrieval augments queries, and exploring hybrid memory architectures that combine vector stores with graphs, relational databases, and participatory annotation workflows. These efforts aim to let communities inspect and shape what is stored and how it is used.
Implementation Status Badge

🔄 PARTIAL / CONSOLIDATING
The conceptual role of ChromaDB as semantic memory is implemented through a shared HTTP‑backed Chroma service with extensive geodb* and gedb* spatial collections and several core general collections. Historical per‑service stores, full embedding coverage in governance and thesis domains, and complete end‑to‑end RAG traces are still in the process of consolidation and documentation.

