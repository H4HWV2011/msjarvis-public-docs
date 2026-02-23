## Why this matters for Polymathmatic Geography

This chapter describes how Ms. Jarvis already uses a concrete semantic memory system to support place‑based reasoning about West Virginia, connecting GBIM beliefs, a statewide spatial corpus, and an emerging local resource registry into an inspectable retrieval pipeline. It supports:  
- **P1 – Every where is entangled** by storing texts, GIS‑derived entities, and program records in shared relational tables and vector collections that can be jointly retrieved and joined, so that legal, economic, infrastructural, and social facts about Appalachia are handled as a single interconnected memory rather than as disconnected files or ad‑hoc lookups.  
- **P3 – Power has a geometry** by representing relationships among institutions, places, and access to help as explicit database records, embeddings, and retrieval paths whose behavior can be inspected, clustered, and audited, making it possible to see how different parts of the system are actually traversed when answering questions about extraction, obligation, and care.  
- **P5 – Design is a geographic act** by treating collection schemas, metadata choices, enrichment scripts, retrieval rules, and join logic as deliberate interventions into how West Virginia is represented and searched, so that design decisions about Ms. Jarvis’s memory layer are understood as decisions about how the region itself can be perceived and acted upon.  
- **P12 – Intelligence with a ZIP code** by binding memory collections and registries to West Virginia–specific layers and records, including GBIM‑derived geographies and a program registry keyed by county and ZIP where populated, so that queries about help, risk, or opportunity are resolved through structures that explicitly encode where people live and which institutions serve them.  
- **P16 – Power accountable to place** by making long‑term memory, retrieval behavior, and query‑to‑evidence links explicit and queryable, with logs and database joins that show which beliefs, features, and program rows were used in answers about particular communities, instead of hiding those choices inside opaque model weights.

As such, this chapter belongs to the **Computational Instrument** tier: it defines the semantic memory substrate and retrieval layer on which Quantarithmia’s reasoning, GBIM’s belief structures, the verified local‑resources band, the West Virginia benefits RAG flows, and MountainShares‑oriented governance analysis currently run.

## 5. ChromaDB as Semantic Memory

### 5.1 Purpose and Scope

This chapter explains how Ms. Egeria Jarvis uses ChromaDB as the primary semantic memory layer backing the Hilbert‑space representation, GBIM, the verified local resource registry, and the broader semantic fabric. ChromaDB is a vector database that stores high‑dimensional embedding vectors with associated metadata and exposes efficient similarity search and filtering operations. In this system, ChromaDB is not merely a convenience library; it is the concrete implementation of long‑term, queryable memory for documents, GIS features, governance texts, autonomous‑learning traces, resource guides, and thesis materials, as well as a central back‑end for the text and GIS RAG services.

<p align="center">
  <img src="https://github.com/user-attachments/assets/5f6bf0d9-91ca-4692-8b1c-95fbceec81b7"
       alt="ChromaDB as Semantic Memory in Ms. Jarvis"
       width="900">
</p>

> *Figure 1 – ChromaDB as Semantic Memory in Ms. Jarvis. Services embed texts and GIS features into ChromaDB collections so that abstract Hilbert‑space state becomes a concrete, queryable memory layer for RAG. Local resource documents sit alongside GBIM exports and are linked to structured entries in a `local_resources` table keyed by ZIP and program type. Dedicated collections such as `gis_wv_benefits` support benefits‑focused GIS RAG.*

Within the Quantarithmia program, ChromaDB is treated as the bridge between abstract Hilbert‑space representation and stored embeddings: vectors in each collection approximate elements of the high‑dimensional inner‑product space described in the previous chapter, but are realized through a specific embedding model and index implementation. It is the place where beliefs, contexts, resource descriptions, and references become durable and retrievable for reasoning and retrieval‑augmented generation (RAG). Conceptually, each collection corresponds to an empirically instantiated subset of the Hilbert space \(H_{\text{App}}\), and stored vectors approximate elements of the spaces described in the previous chapter while linking out to structured registers such as GBIM and `local_resources`.

---

### 5.2 Role in the Ms. Jarvis Architecture

In the Ms. Jarvis architecture, ChromaDB plays several interlocking roles.

- **Semantic memory store (non‑spatial).**  
  Embeddings of texts and artifacts live in collections corresponding to domains such as governance, thesis content, autonomous learner outputs, conversations, local resource guides, and curated research traces. These collections support general semantic retrieval independent of geography.

- **Geospatial semantic layer (spatial).**  
  A unified GIS‑derived collection holds embeddings and metadata for West Virginia geospatial features, mirroring PostGIS tables and providing the semantic representation of the spatial body described in the GBIM chapter. The current production deployment centers on a consolidated worldview collection with millions of records and spatial provenance linking back to PostGIS geometries and belief rows, complemented by task‑specific collections such as `gis_wv_benefits` that focus on benefits‑relevant facilities.

- **Retrieval engine for RAG.**  
  At query time, services embed inputs and use ChromaDB similarity search, often with metadata filters, to retrieve the most relevant items for context and reasoning. A text RAG service handles general semantic retrieval; a GIS RAG service uses geospatial collections for spatial questions. This behavior instantiates the query projection and neighborhood selection mechanisms described in the Hilbert‑space model and forms the unstructured side of Ms. Jarvis’s memory, which is then joined against structured stores like GBIM and `local_resources` before being handed to the 21‑LLM ensemble.

- **Structural backbone for inspectable memory.**  
  Because collections and metadata are explicitly defined, ChromaDB’s structure mirrors core parts of GBIM, the GeoDB layer, the thesis organization, and the local‑resources band. This makes it possible to enumerate collections, inspect document counts, audit metadata, and correlate logs of RAG calls with the underlying memory, rather than relying on hidden internal state.

Taken together, this design makes the semantic memory system inspectable and debuggable: researchers and community partners can see what is stored, how it is grouped, which collections underpin particular advisory behaviors, how unstructured resource documents tie back to specific, verified program rows in the relational registry, and how RAG and the ensemble use these elements to answer live questions.

---

### 5.3 Collections and Data Domains

In the deployment examined in late 2025 and early 2026, the primary Chroma instance exposes collections that fall into three broad families: general semantic memory, GeoDB‑derived spatial memory, and resource‑related materials that link into `local_resources` and benefits RAG paths.

#### 5.3.1 Production Spatial Collection

The primary spatial memory collection in production as of early 2026 is a consolidated GBIM export:

- Collection name: `gbim_worldview_entities` (or equivalent consolidated spatial index).  
- Record count: on the order of millions of records.  
- Records with worldview context and spatial provenance: a large majority of the collection.  
- Records currently lacking full worldview, bounding box, and dataset metadata: a residual backlog tracked for enrichment.  
- Source datasets: more than 200 standardized West Virginia GIS layers.  
- Worldview context: a stable UUID tying spatial entities to a particular worldview.

This collection is built by exporting GBIM worldview entities and their attributes from PostGIS, enriching them with spatial and provenance metadata, and indexing them as text embeddings in ChromaDB.

<p align="center">
  <img src="https://github.com/user-attachments/assets/1469b3c1-f9e8-4b9d-a021-a79baa89ee58"
       alt="End-to-End Spatial RAG Query through ChromaDB and GBIM"
       width="900">
</p>

> *Figure 2 – Consolidated spatial memory collection. The unified spatial collection links ChromaDB vectors back to GBIM worldview entities and PostGIS geometries, and forward into GIS RAG responses.*

**Document structure**

Text documents follow a simple pattern such as:

```text
wvgistcbuildingfootprints feat_1703912
```

Core metadata fields (present for all records):

- `entity_id`: UUID linking to `gbim_worldview_entity.id`.  
- `source_table`: dataset name (for example, `wvgistcbuildingfootprints`, `blocks_census_2020_utm83_full`).  
- `source_pk`: primary key in the source table (linked to GBIM/GeoDB attributes).  
- `label`: human‑readable entity label.  
- `centroid_x`, `centroid_y`: spatial coordinates in the standard projected system.

Extended metadata (populated via a backfill pipeline):

- `worldview_id`: worldview context UUID.  
- `bbox`: GeoJSON geometry or bounding box.  
- `dataset`: source dataset name for provenance.  
- `geodb_id`: original GeoDB identifier.  
- `srid`: spatial reference identifier.

A dedicated backfill process derives these extended fields from GBIM and GeoDB tables and attaches them to existing records in the consolidated spatial collection. Coverage is monitored via scripts that iterate over the collection and count non‑null values for key metadata fields.

---

### 5.3.2 Legacy and Historical Spatial Collections

Prior to consolidation, spatial memory was distributed across individual `*_attrs` collections corresponding to each GIS layer. These collections remain in the system for backward compatibility but are superseded by the unified spatial collection. Migration practice is: new queries target the consolidated index; legacy collections are maintained for historical queries, validation, and debugging.

---

### 5.3.3 General Semantic Collections

In the current deployment, principal general‑semantic collections are defined for:

- autonomous learning traces,  
- research history and notebook‑like notes,  
- thesis and GBIM‑related documentation,  
- personal and organizational documents for the steward/author,  
- Hilbert‑space and learner‑corpus materials.

These collections have schemas declared and are intended to hold embeddings for governance documents, thesis materials, autonomous learner outputs, and personal research corpora. Their presence establishes the intended semantic architecture, even when embeddings are still being backfilled.

---

### 5.3.4 Resource‑Related and Benefits Collections

Resource‑related documents (for example, county quick guides, seasonal assistance flyers, teacher resource lists, utility assistance PDFs, and agency fact sheets) are ingested into one or more semantic collections, with metadata fields such as:

- `county`, `state`, `zip_codes` or `zip_hint`,  
- `resource_type` (for example, seasonal assistance, housing, utilities, senior services, education support),  
- `source_url` or `file_id`,  
- `local_resource_id` linking to a structured row in the `local_resources` table when available.

In addition, a dedicated collection such as `gis_wv_benefits` stores semantic descriptions and metadata for benefits‑related facilities, keyed by spatial identifiers, county, and GBIM entities. These collections provide the unstructured side of local resources and benefits. At retrieval time, Ms. Jarvis uses metadata and `local_resource_id` (or facility IDs) to resolve from an embedded snippet in ChromaDB to a normalized registry entry or GBIM entity that contains ZIP coverage, phones, emails, contacts, and verification metadata.

---

### 5.4 From Hilbert Space to ChromaDB (and Back to Registries)

ChromaDB provides the concrete realization of the Hilbert‑space representation described in the previous chapter, while structured stores such as GBIM tables and `local_resources` provide the “hard edges” that RAG resolves into.

**Embeddings as vectors.**  
The embedding model maps texts and entities into high‑dimensional real vectors. ChromaDB stores these vectors alongside metadata (identifiers, timestamps, entity types, geographies, resource keys) and exposes operations such as nearest‑neighbor search, filtered retrieval, and upsert.

**Collections as working subspaces.**  
Each ChromaDB collection corresponds to an empirically instantiated subset of \(H_{\text{App}}\), grouping related vectors by purpose (for example, governance, conversation, thesis, resource guides) or by entity type (for example, blocks, buildings, infrastructure, benefits hubs). The consolidated spatial collection represents a comprehensive spatial subspace in this deployment, while resource and benefits collections approximate a semantic subspace of “who helps whom, where, and how.”

**Queries as projections plus joins.**  
Incoming queries are embedded and used to probe relevant collections. This effectively projects each query into the appropriate subset of \(H_{\text{App}}\), retrieves nearby vectors with respect to the inner‑product‑induced similarity measure, and returns documents and metadata. For resource‑ and benefits‑related flows, Ms. Jarvis then uses metadata (such as `local_resource_id`, `county`, `ZIP`, and `gbim_entity`) to join that unstructured context against `local_resources` and GBIM, enforcing that any recommended program or facility has concrete, structured backing and a verification state, and that RAG answers can be traced back to specific entities and rows.

This mapping allows Ms. Jarvis’s memory to be described both geometrically, in terms of subsets and projections of a Hilbert space, and operationally, in terms of concrete collection queries, metadata filters, RAG calls, and joins to structured registries.

---

### 5.5 Embedding Model and Dimensionality

In the RAG stack under analysis, Ms. Jarvis uses a sentence‑embedding model with 384‑dimensional outputs as the primary text embedding channel. Chroma collections are configured with dimension 384, confirming the ambient dimension of the main \(H_{\text{text}}\) component for text‑based collections.

Any Chroma collection that stores embeddings produced by this model is configured to accept 384‑dimensional vectors. This requirement applies both to general semantic collections and to spatial and benefits collections, which use consistent text embeddings for feature descriptions and attribute summaries, as well as to resource‑document collections.

---

### 5.6 Clients, RAG Services, and Deployment Topology

ChromaDB is accessed as a shared HTTP service in this deployment; earlier patterns using per‑service local stores are now considered legacy.

#### 5.6.1 Shared HTTP Service

In the active environment, services connect to a shared ChromaDB instance through an HTTP client configured with explicit host and port, with:

- a container dedicated to the vector store,  
- persistent on‑disk storage mounted into the container, and  
- a single catalog that includes spatial, semantic, resource‑document, and benefits collections.

Connection patterns follow a simple template:

```python
import chromadb

client = chromadb.HttpClient(host="localhost", port=8000)
collection = client.get_collection("gbim_worldview_entities")
print("Total entities:", collection.count())
```

The shared instance is treated as the canonical semantic memory store for this deployment and is used by the text RAG, GIS RAG, and other memory‑aware services behind the main chat and search endpoints.

---

### 5.7 Integration with GBIM, GeoDB, Local Resources, and RAG

ChromaDB is tightly integrated with GBIM, the GeoDB layer, the local resource registry, the benefits‑focused collections, and the broader RAG pipeline.

**GBIM linkage.**  
GBIM worldview entities are indexed in the consolidated spatial collection with metadata fields linking back to PostGIS tables via `source_table` and `source_pk`. The `entity_id` field provides stable UUID references to `gbim_worldview_entity.id`, enabling round‑trip queries from semantic search results to full belief provenance, including the nine epistemic axes described in the GBIM chapter.

**GeoDB integration.**  
The spatial collection mirrors the GBIM attributes corpus. Spatial coordinates and bounding boxes enable hybrid queries that combine semantic similarity with spatial filtering. Keys and metadata allow retrieval results to be rejoined to GBIM entities and geometries for display in geospatial tools and for inclusion in GIS RAG responses.

**Local resource registry integration.**  
Resource‑related collections index unstructured PDFs and guides while tagging entries with `local_resource_id` or other keys. Once a snippet is retrieved, Ms. Jarvis resolves it to a row in the `local_resources` table, which encodes `resource_type`, county, ZIP coverage, contact details, and verification fields. This ensures that recommendations are backed by explicit, up‑to‑date program records rather than free‑floating text alone.

**Benefits and GIS RAG integration.**  
The `gis_wv_benefits` collection indexes semantic descriptions of benefits facilities and is queried by GIS RAG services for prompts like “benefits near Oak Hill” or “Raleigh County assistance offices.” Metadata such as county and GBIM entity identifiers enable joins back to GBIM and relationships to other worldview entities. Combined with text RAG over other collections, this yields blended semantic and spatial context for the ensemble.

**RAG context building.**  
For spatial or resource questions, the RAG pipeline queries both spatial and resource collections to retrieve relevant entities, PDFs, and program descriptions. Retrieved texts, metadata, spatial identifiers, and registry keys are combined into context windows for language models, with filtering by collection, geography, topic, resource type, and verification status. Logs record which collections and IDs were used per query.

**Belief graph and registry traversal.**  
Once ChromaDB returns entity IDs and resource keys, the system performs SQL queries against GBIM belief and edge tables and against `local_resources` to retrieve the full epistemic and practical context: data sources (how), policy justifications (why), beneficiary communities (for whom), authorizing frameworks (authority), and concrete program details and verification history.

End‑to‑end, the pipeline behaves as a structured walk through curated, domain‑specific memory organized around GBIM, the GeoDB spatial body, resource registries, and Quantarithmia’s research concepts, mediated by ChromaDB and observed through RAG and ensemble logs.

---

### 5.8 Query Paths and JSON Structures

To connect the conceptual description with concrete operations, this section outlines canonical request and response shapes.

#### 5.8.1 ChromaDB Query Request

A typical query against a collection includes:

- `query_texts`: list of query strings to embed and search,  
- `n_results`: number of nearest neighbors to return per query,  
- `where`: optional metadata filter (for example, restricting to certain `source_table` values or to entities in a given county),  
- `include`: fields to return (for example, `["metadatas", "documents", "distances"]`).

Resource and benefits collections follow the same pattern, with additional filters like `resource_type`, `local_resource_id`, or `county`.

#### 5.8.2 ChromaDB Response Structure

ChromaDB responses contain parallel lists of IDs, distances, metadatas, and documents, where metadata entries include the identifiers needed to rejoin to GBIM entities or to registry rows in `local_resources`. This structure underpins traceable, explainable RAG behavior and supports reconstruction of which memory elements contributed to a given ensemble answer.

---

### 5.9 Operational Considerations

Using ChromaDB as a production memory layer introduces several practical considerations.

**Reliability and persistence.**  
The main ChromaDB instance is backed by persistent on‑disk storage, with regular backups around large ingests and metadata backfills. Legacy local stores are archived or decommissioned to avoid ambiguity.

**Performance and scaling.**  
As collections grow into the millions of records, index configuration and hardware resources directly affect query latency and throughput for similarity search. Bulk ingest is performed in batches, with attention to index compaction and memory usage. Latency characteristics of chat and search endpoints reflect both model inference and ChromaDB query performance.

**Security and privacy.**  
The documented deployment focuses on public or research‑grade data: West Virginia GIS layers, public resource guides, and internal research corpora. Collections containing sensitive user data are excluded or carefully controlled. Conversational or personal‑memory collections are curated before being used in broader contexts.

**Schema and configuration management.**  
Collection names, metadata schemas, embedding configurations, and RAG routing rules are versioned and recorded. Consolidations (such as merging many `*_attrs` collections into a single GBIM‑backed spatial index, adding `local_resource_id` metadata to resource documents, or introducing `gis_wv_benefits`) are treated as explicit migrations with before/after evaluation.

---

### 5.10 Production Deployment Characteristics (Early 2026)

In early 2026, the live system exhibits the following characteristics:

- A consolidated spatial collection with millions of records and widespread coverage of spatial provenance fields.  
- Standardized SRID 26917 (UTM Zone 17N NAD83) for spatial coordinates in metadata.  
- GBIM belief and edge tables encoding how, why, for whom, authority, and evidence relationships for millions of worldview entities, with partial coverage where enrichment is ongoing.  
- Resource and benefits collections that tie unstructured guides and facility descriptions to `local_resources` rows and GBIM entities.  
- Text and GIS RAG services that query these collections, apply metadata filters, and pass retrieved content to a multi‑model ensemble via chat endpoints.  
- Logging that captures which collections, IDs, registry rows, and spatial entities were touched per query, enabling post‑hoc inspection of memory usage and behavior.

---

### 5.11 Limitations and Future Work

**Partial embedding coverage in general‑semantic domains.**  
Spatial collections are heavily populated, but some planned semantic corpora remain under‑embedded. Completing ingestion and backfill is necessary for a fully realized semantic memory that behaves consistently across domains.

**Dependence on models, indices, and routing.**  
Retrieval quality depends on the embedding model, index parameters, collection design, and RAG routing configuration. Upgrades are treated as migrations with evaluation, including checks that benefits and resource flows for places like Oak Hill and Beckley still behave as intended.

**Semantic gaps and representational limits.**  
Certain forms of knowledge—embodied experience, oral history, spiritual traditions—are difficult to represent as short text embeddings alone. Additional representational strategies (graphs, qualitative annotations, GBIM‑linked justice metrics, community‑led tagging, and registries like `local_resources`) are needed to supplement the vector store.

**Evolving schema and topology.**  
As GBIM, GeoDB, RAG services, and Quantarithmia evolve, the set of collections, metadata fields, and indexing strategies will continue to change. Consolidations like the GBIM spatial merge, the introduction of `gis_wv_benefits`, and the link from resource collections into `local_resources` demonstrate this evolution.

Future work will:

- Maintain the consolidated spatial collection via incremental updates and periodic metadata backfills.  
- Backfill general semantic collections with governance documents, thesis materials, autonomous learner outputs, and resource guides.  
- Document all collection schemas and RAG routing rules in a single, queryable registry.  
- Add traced end‑to‑end examples showing ChromaDB retrieval → GBIM provenance → belief‑graph traversal → local resource resolution → ensemble answer.  
- Explore hybrid memory architectures combining vector stores with graphs, relational databases, and participatory annotation workflows.  
- Implement incremental sync infrastructure for daily delta updates instead of full rebuilds.  
- Develop or adopt embedding models and metadata conventions fine‑tuned on Appalachian place names, infrastructure terminology, and local program language, and integrate them with the verified local resource registry and verification loop.

**Implementation Status**

**Badge: PRODUCTION / CONSOLIDATING**  
The conceptual role of ChromaDB as semantic memory is fully implemented for spatial entities and increasingly for resource guides and benefits facilities, and it is now directly exercised by text and GIS RAG services behind the main chat endpoints. A verified `local_resources` band in Postgres complements ChromaDB, providing structured, ZIP‑aware, and periodically re‑verified program information that Ms. Jarvis uses alongside semantic retrieval to act as an accountable, place‑based Steward System in West Virginia.
