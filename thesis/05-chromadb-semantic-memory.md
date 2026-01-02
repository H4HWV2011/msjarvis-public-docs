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

```bash
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

```bash
python3 - << 'PY'
from sentence_transformers import SentenceTransformer
m = SentenceTransformer("all-MiniLM-L6-v2")
v = m.encode("test")
print("SentenceTransformer dim:", v.shape)
PY

# Output:
# SentenceTransformer dim: 384
.
