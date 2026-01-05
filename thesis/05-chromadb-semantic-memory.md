# ChromaDB as Semantic Memory

This chapter explains how Ms. Egeria Jarvis uses ChromaDB as the primary semantic memory layer backing the Hilbert‑space state, GBIM, and the broader semantic fabric. ChromaDB is a vector database: it stores high‑dimensional embedding vectors with associated metadata and enables efficient similarity search over them. In this system, ChromaDB is not just a convenience library; it is the concrete implementation of long‑term, queryable memory for documents, GIS features, governance texts, autonomous‑learning traces, and thesis materials.

Within the thesis, ChromaDB is treated as the bridge between abstract Hilbert‑space state and actual stored knowledge: it is where beliefs, contexts, and references are made durable and retrievable for reasoning and retrieval‑augmented generation (RAG).

## Role in the Ms. Jarvis Architecture

In the Ms. Jarvis architecture, ChromaDB plays several key roles:

- **Semantic memory store (non‑spatial):**  
  Embeddings of texts and artifacts are stored in collections corresponding to domains such as governance, thesis content, autonomous learner outputs, conversations, and user memory.

- **Geospatial Hilbert layer (spatial):**  
  A large family of `geodb*` and `gedb*` collections stores embeddings and metadata for West Virginia geospatial features, mirroring PostGIS tables and providing the Hilbert‑space representation of the spatial body described in Chapter 6.

- **Retrieval engine:**  
  At query time, services project inputs into the embedding space and use ChromaDB similarity search to retrieve the most relevant items for context and reasoning.

- **Structural backbone:**  
  Because collections and metadata are explicitly defined, ChromaDB’s structure mirrors core parts of GBIM, the GeoDB layer, and the thesis organization, making it easier to reason about what the Steward System knows and how that knowledge is organized.

This design makes the memory system inspectable: researchers can see collections, document counts, and metadata, rather than relying on opaque, hidden state.

## Collections and Data Domains

In the live deployment examined in late 2025 and early 2026, the primary Chroma instance exposes a concrete set of collections that fall into two broad families: **general semantic memory** and **GeoDB‑derived spatial memory**.

### General Semantic Collections

Representative general collections include:

- `conversations`  
- `ms_jarvis_memory`  
- `user_memory_vectors`  
- `autonomous_learning`  
- `research_history`  
- `mountainshares_knowledge`  
- `spiritual_wisdom`  
- `thesis_materials` (or equivalent)  
- `default` 

and other small auxiliary collections used for development and diagnostics  

These collections correspond to distinct data domains:

- **Conversations and user memory:**  
  `conversations`, `ms_jarvis_memory`, and `user_memory_vectors` store selected interaction snippets, higher‑level conversational summaries, and explicit user‑memory embeddings used by certain agents and bridges.

- **Governance and norms:**  
  `mountainshares_knowledge` stores MountainShares rules, constitutional principles, governance deliberation texts, and related commentary, providing a focused corpus for economic and governance questions.

- **Learner and research history:**  
  `autonomous_learning` and `research_history` store web‑research outputs, per‑cycle summaries, and RAG traces emitted by the autonomous learner, capturing what was studied, when, and why.

- **Spiritual and contextual materials:**  
  `spiritual_wisdom` stores spiritual, reflective, and contextual texts that inform the qualitative and ethical framing of responses.

- **Thesis and internal materials:**  
  Collections like `thesis_materials` (where present) hold drafts, notes, and supporting texts referenced within the Quantarithmia research program.

In some of these collections, embeddings are fully populated and used for similarity search; in others (for example, some governance or thesis collections), documents and metadata are present but embeddings are still being backfilled for all items.

### GeoDB‑Derived `geodb*` and `gedb*` Collections

A second, much larger family of collections is generated automatically from the PostGIS GeoDB:

- `geodbblockscensus2020utm83`, `geodbblockgroupscensus2020utm83`, and their `wma84` variants.  
- `geodbboundaryappalachianbasinwvges1996utm83`, `geodbbridges`, and other infrastructure layers.  
- Hazard layers such as `geodbminesabandonedlandslinewvdep1996noprojectoin`, `geodbminesabandonedlandspolygonwvdep1996noprojection`, `geodbdamsusarmycorpsofengineers200010utm83`, `geodbdamsnoncoalusgs2002utm83`, floodplain structures, fault and geology layers, and many more.  
- Civic and facility layers such as `geodbhospitalswvdem040519utm83`, `gedbnursinghomeswvdem041219utm83`, `geodbfiredeptwvdem092017utm83`, `geodbpolicedeptwvdem012319utm83`, `geodbcountycityparkboundaries20201104utm83`, libraries, schools, and public health departments.  
- Governance and boundary layers such as regional planning councils, ZIP code tabulation areas, county seats, courthouses, National Register points and polygons, empowerment zones, and community‑defined boundaries.  

For nearly every such `geodb*` collection, there is a corresponding aliased `gedb*` collection (for example, `geodbblockscensus2020utm83` and `gedbblockscensus2020utm83`). The `geodb*` collections hold embeddings and base metadata keyed to PostGIS feature IDs; the `gedb*` collections provide a stable alias layer (often with “dummy” documents and copied metadata) that can be used by higher‑level services without coupling them directly to ingestion internals.

Together, these collections form the Hilbert‑space representation of Ms. Jarvis’s spatial body, aligning directly with the PostGIS tables described in Chapter 6.

## From Hilbert Space to ChromaDB

Conceptually, ChromaDB is one concrete realization of the Hilbert‑space state described in the surrounding chapters:

- **Embeddings as vectors:**  
  The embedding model maps texts and entities into a high‑dimensional vector space; ChromaDB stores these vectors and exposes operations like nearest‑neighbor search.

- **Collections as subspaces:**  
  Each ChromaDB collection corresponds to a subspace or region of the overall Hilbert space, grouping related vectors by purpose (governance, conversation, learner history) or by entity type (blocks, buildings, mines, dams, facilities).

- **Queries as projections:**  
  Incoming queries are embedded and then used to probe the relevant collections, effectively projecting the query into the appropriate subspace and retrieving nearby vectors for further reasoning.

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

    Model: all-MiniLM-L6-v2

    Dimensionality: 384

This dimensionality defines the Hilbert‑space dimension for the main text‑embedding channel used in RAG. Any Chroma collection that stores embeddings produced by this model must be configured to accept 384‑dimensional vectors. In the current deployment:

    The GeoDB‑derived geodb* collections are fully embedded at 384 dimensions and aliased into corresponding gedb* collections.

    Several general semantic collections (for example, parts of mountainshares_knowledge or certain thesis/governance collections) still have documents and metadatas present for all items, with embeddings being backfilled or recomputed as migration work proceeds.

The chapter therefore treats 384‑dimensional embeddings as the current standard, while acknowledging that backfill and potential future model upgrades are part of an ongoing migration process.
ChromaDB Implementation and Clients

ChromaDB is accessed both as a shared HTTP service and, historically, as per‑service local stores.
Shared HTTP Service (Primary)

In the active environment, services connect to a shared ChromaDB instance via an HTTP client. A typical pattern is:

python
import chromadb
from chromadb.config import Settings

client = chromadb.HttpClient(
    host="localhost",
    port=8002,
    settings=Settings(anonymized_telemetry=False),
)
print("Collections:", [c.name for c in client.list_collections()])

This client is used by ingestion scripts, GeoDB ETL pipelines, RAG gateways, and other services that treat Chroma as a central semantic memory server. The live instance exposes both the general collections and the large family of geodb* / gedb* collections described above.
Historical and Auxiliary Persistent Clients

Other services, especially those responsible for earlier ingestion experiments and specialized domains, have historically used chromadb.PersistentClient against container‑local paths (for example, .chromadb or chroma_db):

python
import chromadb

client = chromadb.PersistentClient(path=".chromadb")
collection = client.get_collection("ms_jarvis_memory")

These local stores have been used for:

    Isolated experiments and unit tests.

    Service‑specific memory (for example, early learner experiments or social‑media‑related data).

    Transitional states prior to consolidation into the main shared instance.

As of late 2025 and early 2026, the operational intent is to converge on the shared HTTP‑backed store for primary semantic memory (including GeoDB embeddings), while carefully managing remaining per‑service stores and migration paths. The conceptual description in this chapter refers to the unified logical memory; any residual local stores are treated as legacy or experimental.
Integration with GBIM, GeoDB, and RAG

ChromaDB is tightly integrated with GBIM, the GeoDB layer, and the broader RAG pipeline:

    GBIM linkage:
    GBIM entities (places, infrastructures, institutions, persons, policies) reference Chroma collections via stable IDs and metadata. For spatial entities, geodb* collections store feature‑level embeddings and metadata keyed to PostGIS tables; for non‑spatial entities, general collections (such as mountainshares_knowledge or ms_jarvis_memory) store associated documents and summaries.

    GeoDB integration:
    The GeoDB ETL pipeline reads per‑feature attributes from PostGIS, constructs embeddings, and upserts them into geodb* collections before aliasing into gedb*. Keys and metadata (such as source table, primary key, and location tags) allow results to be rejoined to GBIM entities and geometries.

    RAG context building:
    When Ms. Jarvis answers a question, the RAG pipeline uses ChromaDB to pull relevant documents and feature‑level embeddings. Retrieved texts, metadata, and spatial IDs are assembled into context windows for the language models, with filtering by collection, geography, topic, and source.

    Governance‑specific retrieval:
    For MountainShares‑related queries, retrieval is scoped to mountainshares_knowledge and closely related collections, ensuring that responses are grounded in published rules, local economic context, and spatial justice considerations rather than generic web search.

The pipeline therefore acts as a structured walk through a curated, domain‑specific memory organized around GBIM, the GeoDB spatial body, and Quantarithmia’s research concepts.
Query Paths and JSON Structures

To connect the conceptual description with concrete operations, this section gives canonical request and response shapes.
Gateway‑Level Request Shape

Gateway or bridge services conceptually receive simplified query objects. A typical request schema is:

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

Which yields:

json
{
  "collection": "mountainshares_knowledge",
  "query": "Fayette County Community Arts Center",
  "n_results": 5
}

This object is then translated into a lower‑level Chroma query.
Chroma Query Request Body

Given a live Chroma client and a selected collection, a typical query looks like:

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

The corresponding HTTP JSON body sent to Chroma’s /api/v1/collections/{collection_id}/query endpoint has the form:

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

The response contains parallel lists for ids, documents, metadatas, distances, and optionally embeddings (when an embedding function is configured). In collections where embeddings are not yet present for every item, the embeddings field may be null or sparsely populated while the remaining structures are still fully populated.

These two JSON structures—gateway‑level request and Chroma‑level query body—provide concrete, drop‑in examples for documentation and debugging.
Operational Considerations

Using ChromaDB as a production memory layer introduces practical concerns:

    Reliability and persistence:
    The main Chroma instance is bound to a persistent on‑disk directory and must be backed up regularly. Backup scripts can also snapshot any residual .chromadb directories from earlier local stores to ensure historical data is preserved during consolidation.

    Performance and scaling:
    As collections grow (large GIS corpora, expansive learner outputs, thesis materials), index choice and hardware resources directly affect query latency. Chroma’s local HNSW‑based indexing is used by default; query defaults are tuned so that requesting more results than available items yields predictable behavior and avoids unnecessary warnings.

    Security and privacy:
    The documented Chroma deployment is treated as documentation‑ and research‑oriented: sensitive user data, private keys, and non‑consensual logs are excluded by design. Collections like conversations and ms_jarvis_memory are curated and may be redacted or summarized before being included in public exports.

These details link the conceptual role of ChromaDB to the realities of running a live, research‑grade governance and advisory system.
Limitations and Future Work

Current use of ChromaDB has several limitations:

    Partial embedding coverage in non‑GeoDB domains:
    While GeoDB‑derived geodb* collections are fully embedded and aliased, some general semantic collections (for example, parts of mountainshares_knowledge, thesis_materials, or legacy memory collections) still contain documents and metadata with incomplete embedding backfill.

    Model and index dependence:
    Retrieval quality depends on the choice of embedding model (all-MiniLM-L6-v2 at 384 dimensions), index parameters, and collection design; changes to any of these can alter the Steward System’s apparent memory and must be managed as schema and model migrations.

    Semantic gaps:
    Certain forms of knowledge (embodied experience, collective trauma narratives, spiritual traditions) are difficult to represent solely as short text embeddings. Additional representational strategies (graph structures, qualitative annotations, GBIM‑linked justice metrics, and community‑led tagging) are needed.

    Evolving schema and topology:
    As GBIM, GeoDB, and Quantarithmia evolve, the set of collections, metadata fields, and indexing strategies will continue to change. Migration tools and versioned schemas are necessary to maintain continuity across thesis revisions and deployments, including clear documentation of when historical local stores were consolidated into the shared HTTP‑backed instance.

Future work includes:

    Completing backfill of embeddings for all key general collections with coherent, documented embedding functions.

    Documenting all collection names, metadata schemas, and embedding dimensions in a single schema registry, including how they map to GBIM entities, GeoDB layers, and thesis concepts.

    Adding traced end‑to‑end examples of RAG flows showing how Chroma retrieval augments queries and how those traces are logged and inspected.

    Exploring hybrid memory architectures that combine vector stores with graphs, relational databases, and participatory annotation workflows, enabling communities to inspect and shape what is stored and how it is used.

Implementation Status Badge

🔄 PARTIAL / CONSOLIDATING — The conceptual role of ChromaDB as semantic memory is implemented via a shared HTTP‑backed Chroma service with extensive geodb* / gedb* spatial collections and several core general collections. Historical per‑service stores, full embedding coverage in governance and thesis domains, and complete end‑to‑end RAG traces are still being consolidated and documented.

