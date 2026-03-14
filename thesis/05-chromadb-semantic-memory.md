## Why this matters for Polymathmatic Geography

This chapter describes how Ms. Jarvis already uses a concrete semantic memory system to support place‑based reasoning about West Virginia, connecting GBIM beliefs, the msjarvisgis statewide spatial corpus, and a verified local resource registry into an inspectable retrieval pipeline. It supports:  
- **P1 – Every where is entangled** by storing texts, GIS‑derived entities, and programme records in shared relational tables and production vector collections such as `gbim_beliefs_v2`, `gbim_worldview_entities`, and `gis_wv_benefits` that can be jointly retrieved and joined, so that legal, economic, infrastructural, and social facts about Appalachia are handled as a single interconnected memory rather than as disconnected files or ad‑hoc lookups.  
- **P3 – Power has a geometry** by representing relationships among institutions, places, and access to help as explicit GBIM records, GeoDB features in msjarvisgis, Chroma collections, and logged retrieval paths whose behaviour can be inspected, clustered, and audited, making it possible to see how different parts of the system are actually traversed when answering questions about extraction, obligation, and care.  
- **P5 – Design is a geographic act** by treating collection schemas, metadata choices, enrichment scripts, retrieval rules, and join logic in the GBIM/GeoDB/Chroma stack as deliberate interventions into how West Virginia is represented and searched, so that design decisions about Ms. Jarvis’s semantic memory layer are understood as decisions about how the region itself can be perceived and acted upon.  
- **P12 – Intelligence with a ZIP code** by binding memory collections and registries to West Virginia–specific layers and records, including GBIM‑derived geographies, msjarvisgis features, and a programme registry keyed by county and ZIP where populated, so that queries about help, risk, or opportunity are resolved through structures that explicitly encode where people live and which institutions serve them.  
- **P16 – Power accountable to place** by making long‑term memory, retrieval behaviour, and query‑to‑evidence links explicit and queryable, with logs and database joins that show which GBIM beliefs, GeoDB features, vector‑collection entries, and local_resources rows were used in answers about particular communities, instead of hiding those choices inside opaque model weights.

As such, this chapter belongs to the **Computational Instrument** tier: it defines the production semantic memory substrate and retrieval layer—centred on collections such as `gbim_beliefs_v2`, `gbim_worldview_entities`, and `gis_wv_benefits` and on the msjarvisgis/GBIM/local_resources apparatus—that Quantarithmia’s reasoning, GBIM’s belief structures, the verified `local_resources` band, the West Virginia benefits RAG flows, and MountainShares‑oriented governance analysis already run on in the live system.

## 5. ChromaDB as Semantic Memory

### 5.1 Purpose and Scope

This chapter explains how Ms. Egeria Jarvis uses ChromaDB as the primary semantic memory layer backing the Hilbert‑space representation, GBIM, the verified local resource registry, and the broader semantic fabric. ChromaDB is a vector database that stores high‑dimensional embedding vectors with associated metadata and exposes efficient similarity search and filtering operations. In this system, ChromaDB is not merely a convenience library; it is the concrete implementation of long‑term, queryable memory for documents, GIS features, governance texts, autonomous‑learning traces, resource guides, and thesis materials, as well as a central back‑end for the text and GIS RAG services.

<p align="center">
  <img src="https://github.com/user-attachments/assets/5f6bf0d9-91ca-4692-8b1c-95fbceec81b7"
       alt="ChromaDB as Semantic Memory in Ms. Jarvis"
       width="900">
</p>

> *Figure 1 – ChromaDB as Semantic Memory in Ms. Jarvis. Services embed texts and GIS features into ChromaDB collections so that abstract Hilbert‑space state becomes a concrete, queryable memory layer for RAG. Local resource documents sit alongside GBIM exports and are linked to structured entries in a `local_resources` table keyed by ZIP and programme type. Dedicated collections such as `gis_wv_benefits` support benefits‑focused GIS RAG.*

Within the Quantarithmia programme, ChromaDB is treated as the bridge between abstract Hilbert‑space representation and stored embeddings: vectors in each collection approximate elements of the high‑dimensional inner‑product space described in the previous chapter, but are realized through a specific embedding model and index implementation. It is the place where beliefs, contexts, resource descriptions, and references become durable and retrievable for reasoning and retrieval‑augmented generation (RAG). Conceptually, collections such as `gbim_beliefs_v2`, `gbim_worldview_entities`, and `gis_wv_benefits` correspond to empirically instantiated subsets of the Hilbert space H_App, and stored vectors approximate elements of the spaces described in the previous chapter while linking out to structured registers such as the PostgreSQL msjarvisgis GBIM database and `local_resources`.

**Database Integration Note:** All GBIM collections in ChromaDB are populated from the PostgreSQL 16 `msjarvisgis` database (port 5432, host system). The primary source tables include `gbimbeliefnormalized` (5.4M+ verified rows, 21 GB), `gbim_worldview_entity` (5.4M+ rows, 47 GB), and various spatial tables across 501 total tables in the 91 GB database.

---

### 5.2 Role in the Ms. Jarvis Architecture

In the Ms. Jarvis architecture, ChromaDB plays several interlocking roles.

- **Semantic memory store (non‑spatial).**  
  Embeddings of texts and artefacts live in collections corresponding to domains such as governance, thesis content, autonomous learner outputs, conversations, local resource guides, and curated research traces. These collections support general semantic retrieval independent of geography and include the unified GBIM text collection `gbim_beliefs_v2`, which stores embeddings for rows in `gbimbeliefnormalized` and serves as the production semantic memory layer for GBIM beliefs.

- **Geospatial semantic layer (spatial).**  
  A unified GIS‑derived collection such as `gbim_worldview_entities` holds embeddings and metadata for West Virginia geospatial features, mirroring PostGIS tables in the msjarvisgis database and providing the semantic representation of the spatial body described in the GBIM and GeoDB chapters. The current production deployment centres on this consolidated worldview collection with millions of records and spatial provenance linking back to PostgreSQL PostGIS geometries and belief rows, complemented by task‑specific collections such as `gis_wv_benefits` that focus on benefits‑relevant facilities.

- **Retrieval engine for RAG.**  
  At query time, services embed inputs and use ChromaDB similarity search, often with metadata filters, to retrieve the most relevant items for context and reasoning. A text RAG service handles general semantic retrieval over collections like `gbim_beliefs_v2`; a GIS RAG service uses `gbim_worldview_entities` and `gis_wv_benefits` for spatial questions. This behaviour instantiates the query projection and neighbourhood selection mechanisms described in the Hilbert‑space model and forms the unstructured side of Ms. Jarvis’s memory, which is then deterministically joined against structured stores like the PostgreSQL msjarvisgis GBIM database and `local_resources` before being handed to the ensemble.

- **Structural backbone for inspectable memory.**  
  Because collections and metadata are explicitly defined, ChromaDB’s structure mirrors core parts of GBIM, the msjarvisgis GeoDB layer, the thesis organisation, and the local‑resources band. This makes it possible to enumerate collections, inspect document counts, audit metadata, and correlate logs of RAG calls with the underlying memory, rather than relying on hidden internal state.

Taken together, this design makes the semantic memory system inspectable and debuggable: researchers and community partners can see what is stored, how it is grouped, which collections underpin particular advisory behaviours, how unstructured resource documents tie back to specific, verified programme rows in the relational registry, and how RAG and the ensemble use these elements to answer live questions.

---

### 5.3 Collections and Data Domains

In the deployment examined in late 2025 and early 2026, the primary Chroma instance exposes collections that fall into three broad families: general semantic memory, GeoDB‑derived spatial memory, and resource‑related materials that link into `local_resources` and benefits RAG paths.

#### 5.3.1 Production Spatial Collection

The primary spatial memory collection in production as of early 2026 is a consolidated GBIM export:

- Collection name: `gbim_worldview_entities` (or equivalent consolidated spatial index).  
- Record count: on the order of millions of records (5.4M+ corresponding to PostgreSQL source).  
- Records with worldview context and spatial provenance: a large majority of the collection.  
- Records currently lacking full worldview, bounding box, and dataset metadata: a residual backlog tracked for enrichment.  
- Source datasets: more than 200 standardised West Virginia GIS layers from the 501 tables in msjarvisgis.  
- Worldview context: a stable UUID tying spatial entities to a particular worldview.

This collection is built by exporting GBIM worldview entities and their attributes from the PostgreSQL msjarvisgis PostGIS database, enriching them with spatial and provenance metadata, and indexing them as text embeddings in ChromaDB.

<p align="center">
  <img src="https://github.com/user-attachments/assets/1469b3c1-f9e8-4b9d-a021-a79baa89ee58"
       alt="End-to-End Spatial RAG Query through ChromaDB and GBIM"
       width="900">
</p>

> *Figure 2 – Consolidated spatial memory collection. The unified spatial collection links ChromaDB vectors back to GBIM worldview entities and PostgreSQL PostGIS geometries in msjarvisgis, and forward into GIS RAG responses.*

**Document structure**

Text documents follow a simple pattern such as:
```text
wvgistcbuildingfootprints feat_1703912
```

Core metadata fields (present for all records):

- `entity_id`: UUID linking to PostgreSQL `msjarvisgis.gbim_worldview_entity.id`.  
- `source_table`: dataset name (for example, `wvgistcbuildingfootprints`, `blocks_census_2020_utm83_full`).  
- `source_pk`: primary key in the source table (linked to GBIM/GeoDB attributes in PostgreSQL).  
- `label`: human‑readable entity label.  
- `centroid_x`, `centroid_y`: spatial coordinates in the standard projected system.

Extended metadata (populated via a backfill pipeline):

- `worldview_id`: worldview context UUID.  
- `bbox`: GeoJSON geometry or bounding box.  
- `dataset`: source dataset name for provenance.  
- `geodb_id`: original GeoDB identifier.  
- `srid`: spatial reference identifier.

A dedicated backfill process derives these extended fields from PostgreSQL GBIM and GeoDB tables in msjarvisgis and attaches them to existing records in the consolidated spatial collection. Coverage is monitored via scripts that iterate over the collection and count non‑null values for key metadata fields.

---

### 5.3.2 Legacy and Historical Spatial Collections

Prior to consolidation, spatial memory was distributed across individual `*_attrs` collections corresponding to each GIS layer. These collections remain in the system for backward compatibility but are superseded by the unified spatial collection. Migration practice is: new queries target the consolidated index; legacy collections are maintained for historical queries, validation, and debugging.

---

### 5.3.3 General Semantic Collections

In the current deployment, principal general‑semantic collections are defined for:

- autonomous learning traces,  
- research history and notebook‑like notes,  
- thesis and GBIM‑related documentation,  
- personal and organisational documents for the steward/author,  
- Hilbert‑space and learner‑corpus materials.

The flagship GBIM belief collection `gbim_beliefs_v2` sits in this family. It is populated directly from PostgreSQL `msjarvisgis.gbimbeliefnormalized` (5.4M+ verified rows), with each row embedded as a document whose text is constructed from the nine GBIM axes and whose metadata carries belief identifiers, epochs, and dataset provenance. This collection is already in production and is the primary semantic memory surface for structured beliefs in the RAG services.

---

### 5.3.4 Resource‑Related and Benefits Collections

Resource‑related documents (for example, county quick guides, seasonal assistance flyers, teacher resource lists, utility assistance PDFs, and agency fact sheets) are ingested into one or more semantic collections, with metadata fields such as:

- `county`, `state`, `zip_codes` or `zip_hint`.  
- `resource_type` (for example, `seasonal_assistance`, `housing`, `utilities`, `senior_services`, `education_support`).  
- `source_url` or `file_id`.  
- `local_resource_id` linking to a structured row in the `local_resources` table when available.

In addition, a dedicated `gis_wv_benefits` collection stores semantic descriptions and metadata for benefits‑related facilities (for example, Oak Hill hubs and Beckley DHHR offices), keyed by county, ZIP, and GBIM entities from the PostgreSQL msjarvisgis database. These collections provide the unstructured side of local resources and benefits. At retrieval time, Ms. Jarvis uses metadata and `local_resource_id` (or facility IDs) to resolve from an embedded snippet in ChromaDB to a normalized registry entry or GBIM entity that contains ZIP coverage, phones, emails, contacts, and verification metadata.

A key aspect of this band is that the underlying data are not purely desk‑compiled. Harmony for Hope has convened a **Community Champions** group to ground‑truth resource information, with Boone County resident **Crystal Colyer** serving as a lead “boots‑on‑the‑ground” validator. Working especially across Boone, Kanawha, and nearby counties, she verifies the existence, hours, and accessibility of food pantries and other supports, and her findings drive updates to both the `local_resources` registry and the associated resource‑document collections. In Kanawha County in particular, many of the food and resource locations currently represented in Ms. Jarvis’s semantic memory come directly from her fieldwork, ensuring that the system’s answers about help in Charleston and surrounding communities rest on community‑validated data rather than unverified lists.

---

### 5.4 From Hilbert Space to ChromaDB (and Back to Registries)

ChromaDB provides the concrete realization of the Hilbert‑space representation described in the previous chapter, while structured stores such as the PostgreSQL msjarvisgis GBIM tables and `local_resources` provide the “hard edges” that RAG resolves into.

**Embeddings as vectors.**  
The embedding model maps texts and entities into high‑dimensional real vectors. ChromaDB stores these vectors alongside metadata (identifiers, timestamps, entity types, geographies, resource keys) and exposes operations such as nearest‑neighbor search, filtered retrieval, and upsert.

**Collections as working subspaces.**  
Each ChromaDB collection corresponds to an empirically instantiated subset of H_App, grouping related vectors by purpose (for example, governance, conversation, thesis, resource guides) or by entity type (for example, blocks, buildings, infrastructure, benefits hubs). The consolidated spatial collection represents a comprehensive spatial subspace in this deployment, while resource and benefits collections approximate a semantic subspace of “who helps whom, where, and how.”

**Queries as projections plus joins.**  
Incoming queries are embedded and used to probe relevant collections. This effectively projects each query into the appropriate subset of H_App, retrieves nearby vectors with respect to the inner‑product‑induced similarity measure, and returns documents and metadata. For resource‑ and benefits‑related flows, Ms. Jarvis then uses metadata (such as `local_resource_id`, `county`, `ZIP`, and `gbim_entity`) to join that unstructured context against `local_resources` and the PostgreSQL msjarvisgis GBIM database, enforcing that any recommended programme or facility has concrete, structured backing and a verification state, and that RAG answers can be traced back to specific entities and rows.

This mapping allows Ms. Jarvis’s memory to be described both geometrically, in terms of subsets and projections of a Hilbert space, and operationally, in terms of concrete collection queries, metadata filters, RAG calls, and joins to structured registries.

---

### 5.5 Embedding Model and Dimensionality

In the RAG stack under analysis, Ms. Jarvis uses a sentence‑embedding model with 384‑dimensional outputs as the primary text embedding channel. Chroma collections are configured with dimension 384, confirming the ambient dimension of the main H_text component for text‑based collections.

Any Chroma collection that stores embeddings produced by this model is configured to accept 384‑dimensional vectors. This requirement applies both to general semantic collections and to spatial and benefits collections, which use consistent text embeddings for feature descriptions and attribute summaries, as well as to resource‑document collections.

---

### 5.6 Clients, RAG Services, and Deployment Topology

ChromaDB is accessed as a shared HTTP service in this deployment; earlier patterns using per‑service local stores are now considered legacy.

#### 5.6.1 Shared HTTP Service — Confirmed Configuration (March 13, 2026)

In the active environment, services connect to a shared ChromaDB instance through an HTTP client. The **canonical production address** as of March 13, 2026 is:

- **Host:** `127.0.0.1`
- **Port:** `8002`
- **Instance type:** ChromaDB HTTP server (persistent, host-system process)
- **Storage:** on-disk, host filesystem (not containerized)

```python
import chromadb

client = chromadb.HttpClient(host="127.0.0.1", port=8002)
collection = client.get_collection("gbim_worldview_entities")
print("Total entities:", collection.count())
```

The shared instance is treated as the canonical semantic memory store and is used by the text RAG, GIS RAG, and other memory‑aware services behind the main chat and search endpoints.

#### 5.6.2 Active Collections (Verified March 13, 2026)

The following collections were confirmed present on the live server via `client.list_collections()`:

| Collection | Domain | Status |
|---|---|---|
| `gbim_worldview_entities` | GBIM spatial worldview | 🔄 Full 5.4M ingest running |
| `psychological_rag` | Psychological safety corpus | ✅ Active |
| `autonomous_learner` | Autonomous learning patterns | ✅ Active |
| `spiritual_texts` | Spiritual and values corpus | ✅ Active |
| `geospatialfeatures` | GIS feature embeddings | ✅ Active |
| `msjarvis_docs` | System documentation | ✅ Active |
| `GBIM_sample_rows` | GBIM testing sample (5,000 rows) | ✅ Active |
| `GBIM_Fayette_sample` | Fayette County GBIM sample | ✅ Active |
| `GBIM_sample` | General GBIM sample | ✅ Active |
| `msjarvis-smoke` | Smoke test collection | ✅ Active |

#### 5.6.3 Legacy Archive Location

A prior ChromaDB on-disk store was located at:

```
/mnt/nvme1/msjarvis-rebuild/chroma_db
```

This path is on the second NVMe drive (`/dev/nvme1n1p1`, mounted at `/mnt/nvme1`). This store is treated as a **read-only historical archive** and is not the active HTTP server. It should not be written to or used for new ingest. All active work targets the HTTP server at `127.0.0.1:8002`.

---

### 5.7 Integration with GBIM, GeoDB, Local Resources, and RAG

ChromaDB is tightly integrated with the PostgreSQL msjarvisgis GBIM database, the GeoDB layer, the local resource registry, the benefits‑focused collections, and the broader RAG pipeline.

**GBIM linkage.**  
GBIM worldview entities from the PostgreSQL msjarvisgis database are indexed in the consolidated spatial collection with metadata fields linking back to PostGIS tables via `source_table` and `source_pk`. The `entity_id` field provides stable UUID references to `msjarvisgis.gbim_worldview_entity.id`, enabling round‑trip queries from semantic search results to full belief provenance, including the nine epistemic axes described in the GBIM chapter and stored in the PostgreSQL database.

**GeoDB integration.**  
The spatial collection mirrors the GBIM attributes corpus from the PostgreSQL msjarvisgis database (91 GB, 501 tables). Spatial coordinates and bounding boxes enable hybrid queries that combine semantic similarity with spatial filtering. Keys and metadata allow retrieval results to be rejoined to PostgreSQL GBIM entities and PostGIS geometries for display in geospatial tools and for inclusion in GIS RAG responses.

**Local resource registry integration.**  
Resource‑related collections index unstructured PDFs and guides while tagging entries with `local_resource_id` or other keys. Once a snippet is retrieved, Ms. Jarvis resolves it to a row in the `local_resources` table, which encodes `resource_type`, county, ZIP coverage, contact details, and verification fields. This ensures that recommendations are backed by explicit, up‑to‑date programme records rather than free‑floating text alone.

**Benefits and GIS RAG integration.**  
The `gis_wv_benefits` collection indexes semantic descriptions of benefits facilities and is queried by GIS RAG services for prompts like “benefits near Oak Hill” or “Raleigh County assistance offices.” Metadata such as county and GBIM entity identifiers (linking to PostgreSQL msjarvisgis) enable joins back to GBIM and relationships to other worldview entities. Combined with text RAG over other collections, this yields blended semantic and spatial context for the ensemble.

**RAG context building.**  
For spatial or resource questions, the RAG pipeline queries both spatial and resource collections to retrieve relevant entities, PDFs, and programme descriptions. Retrieved texts, metadata, spatial identifiers, and registry keys are combined into context windows for language models, with filtering by collection, geography, topic, resource type, and verification status. Logs record which collections and IDs were used per query.

**Belief graph and registry traversal.**  
Once ChromaDB returns entity IDs and resource keys, the system performs SQL queries against PostgreSQL GBIM belief and edge tables in msjarvisgis and against `local_resources` to retrieve the full epistemic and practical context: data sources (how), policy justifications (why), beneficiary communities (for whom), authorising frameworks (authority), and concrete programme details and verification history.

**Database Access Example:**
```python
import psycopg2

# Access GBIM for belief graph traversal after ChromaDB retrieval
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="msjarvisgis",
    user="postgres"
)

# Retrieve full belief context for entity
cursor = conn.cursor()
cursor.execute("""
    SELECT belief_id, worldview_id, proposition, belief_state
    FROM gbim_beliefs
    WHERE feature_ref = %s
""", (entity_ref,))
```

End‑to‑end, the pipeline behaves as a structured walk through curated, domain‑specific memory organised around the PostgreSQL msjarvisgis GBIM database, the GeoDB spatial body, resource registries, and Quantarithmia’s research concepts, mediated by ChromaDB and observed through RAG and ensemble logs.

---

### 5.8 Query Paths and JSON Structures

To connect the conceptual description with concrete operations, this section outlines canonical request and response shapes.

#### 5.8.1 ChromaDB Query Request

A typical query against a collection includes:

- `query_texts`: list of query strings to embed and search,  
- `n_results`: number of nearest neighbours to return per query,  
- `where`: optional metadata filter (for example, restricting to certain `source_table` values or to entities in a given county),  
- `include`: fields to return (for example, `["metadatas", "documents", "distances"]`).

Resource and benefits collections follow the same pattern, with additional filters like `resource_type`, `local_resource_id`, or `county`.

#### 5.8.2 ChromaDB Response Structure

ChromaDB responses contain parallel lists of IDs, distances, metadatas, and documents, where metadata entries include the identifiers needed to rejoin to PostgreSQL GBIM entities in msjarvisgis or to registry rows in `local_resources`. This structure underpins traceable, explainable RAG behaviour and supports reconstruction of which memory elements contributed to a given ensemble answer.

---

### 5.9 Operational Considerations

Using ChromaDB as a production memory layer introduces several practical considerations.

**Reliability and persistence.**  
The main ChromaDB instance is backed by persistent on‑disk storage, with regular backups around large ingests and metadata backfills. Legacy local stores are archived or decommissioned to avoid ambiguity.

**Performance and scaling.**  
As collections grow into the millions of records (matching the 5.4M+ scale of the PostgreSQL GBIM source), index configuration and hardware resources directly affect query latency and throughput for similarity search. Bulk ingest is performed in batches, with attention to index compaction and memory usage. Latency characteristics of chat and search endpoints reflect both model inference and ChromaDB query performance.

**Security and privacy.**  
The documented deployment focuses on public or research‑grade data: West Virginia GIS layers from the PostgreSQL msjarvisgis database, public resource guides, and internal research corpora. Collections containing sensitive user data are excluded or carefully controlled. Conversational or personal‑memory collections are curated before being used in broader contexts.

**Schema and configuration management.**  
Collection names, metadata schemas, embedding configurations, and RAG routing rules are versioned and recorded. Consolidations (such as merging many `*_attrs` collections into a single GBIM‑backed spatial index populated from PostgreSQL, adding `local_resource_id` metadata to resource documents, or introducing `gis_wv_benefits`) are treated as explicit migrations with before/after evaluation.

---

### 5.10 Production Deployment Characteristics (Early 2026)

In early 2026, the live system exhibits the following characteristics:

- A consolidated spatial collection such as `gbim_worldview_entities` with millions of records (5.4M+) sourced from the PostgreSQL msjarvisgis database with widespread coverage of spatial provenance fields.  
- A unified GBIM embedding collection `gbim_beliefs_v2` in production, loaded from PostgreSQL `msjarvisgis.gbimbeliefnormalized` (5.4M+ verified rows) and used by the text RAG services described in later chapters.  
- Standardised SRID 26917 (UTM Zone 17N NAD83) for spatial coordinates in metadata.  
- PostgreSQL GBIM belief and edge tables in msjarvisgis encoding how, why, for whom, authority, and evidence relationships for millions of worldview entities, with partial coverage where enrichment is ongoing.  
- Resource and benefits collections that tie unstructured guides and facility descriptions to `local_resources` rows and GBIM entities in the PostgreSQL database.  
- Text and GIS RAG services that query these collections, apply metadata filters, and pass retrieved content to a multi‑model ensemble via chat endpoints.  
- Logging that captures which collections, IDs, PostgreSQL registry rows, and spatial entities were touched per query, enabling post‑hoc inspection of memory usage and behaviour.

Auditability and traceability for this semantic memory layer rely on the same production apparatus used elsewhere in the system: logged PostgreSQL GBIM beliefs from msjarvisgis, GeoDB features, vector collection identifiers (`gbim_beliefs_v2`, `gbim_worldview_entities`), and governance and application logs together provide an evidence trail for how embeddings, retrievals, and joins contributed to particular answers and recommendations.

---

### 5.11 Limitations and Future Work

Several originally “future‑work” items have now been completed and should be treated as foundations rather than as open tasks:

- A unified GBIM embedding collection (`gbim_beliefs_v2`) populated from PostgreSQL `msjarvisgis.gbimbeliefnormalized` and used by RAG.  
- A West‑Virginia‑biased spatial semantic memory built around a consolidated spatial collection such as `gbim_worldview_entities`, with coordinates and provenance that mirror the PostgreSQL msjarvisgis GeoDB corpus (91 GB, 501 tables).  
- Deterministic joins from ChromaDB results back to PostgreSQL GBIM and GeoDB via stable identifiers (`entity_id`, `source_table`, `source_pk`) and to `local_resources` via `local_resource_id` and facility IDs.

Remaining limitations and genuine future work include:

- **Partial embedding coverage in general‑semantic domains.**  
  Spatial and GBIM belief collections are heavily populated from the PostgreSQL source, but some planned semantic corpora (governance, thesis, autonomous learner outputs) remain under‑embedded. Completing ingestion and backfill is necessary for a fully realised semantic memory that behaves consistently across domains.

- **Dependence on models, indices, and routing.**  
  Retrieval quality depends on the embedding model, index parameters, collection design, and RAG routing configuration. Upgrades are treated as migrations with evaluation, including checks that benefits and resource flows for places like Oak Hill and Beckley still behave as intended.

- **Semantic gaps and representational limits.**  
  Certain forms of knowledge—embodied experience, oral history, spiritual traditions—are difficult to represent as short text embeddings alone. Additional representational strategies (graphs, qualitative annotations, GBIM‑linked justice metrics, community‑led tagging, and registries like `local_resources`) are needed to supplement the vector store.

- **Evolving schema and topology.**  
  As the PostgreSQL msjarvisgis GBIM database, GeoDB, RAG services, and Quantarithmia evolve, the set of collections, metadata fields, and indexing strategies will continue to change. Consolidations like the GBIM spatial merge from PostgreSQL, the introduction of `gis_wv_benefits`, and the link from resource collections into `local_resources` demonstrate this evolution.

Future work will:

- Maintain the consolidated spatial and GBIM belief collections via incremental updates and periodic metadata backfills synchronized with the PostgreSQL msjarvisgis source.  
- Backfill general semantic collections with governance documents, thesis materials, autonomous learner outputs, and resource guides.  
- Document all collection schemas and RAG routing rules in a single, queryable registry.  
- Add traced end‑to‑end examples showing ChromaDB retrieval → PostgreSQL GBIM provenance → belief‑graph traversal → local resource resolution → ensemble answer.  
- Explore hybrid memory architectures combining vector stores with graphs, PostgreSQL relational databases, and participatory annotation workflows.  
- Implement incremental sync infrastructure for daily delta updates from PostgreSQL instead of full rebuilds.  
- Develop or adopt embedding models and metadata conventions fine‑tuned on Appalachian place names, infrastructure terminology, and local programme language, and integrate them with the verified local resource registry and verification loop.

**Implementation Status**

**Badge: PRODUCTION / CONSOLIDATING**  
The conceptual role of ChromaDB as semantic memory is fully implemented for spatial entities and GBIM beliefs sourced from the PostgreSQL 16 msjarvisgis database (91 GB, 5.4M+ verified beliefs), and increasingly for resource guides and benefits facilities, and it is now directly exercised by text and GIS RAG services behind the main chat endpoints. A verified `local_resources` band in Postgres complements ChromaDB, providing structured, ZIP‑aware, and periodically re‑verified programme information that Ms. Jarvis uses alongside semantic retrieval to act as an accountable, place‑based Steward System in West Virginia.
