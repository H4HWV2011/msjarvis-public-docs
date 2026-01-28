> **Why this matters for Polymathmatic Geography**  
> This chapter specifies how Ms. Jarvis's semantic memory is implemented in practice, turning abstract Hilbert‑space representation and GBIM entities into a concrete, inspectable memory system. It supports:  
> - **P1 – Every where is entangled** by storing texts, GIS features, governance rules, and spatial materials in shared collections that can be jointly retrieved and analyzed.  
> - **P3 – Power has a geometry** by representing institutional and spatial relationships as vectors and metadata that can be queried and clustered to reveal patterns of extraction, access, and obligation.  
> - **P5 – Design is a geographic act** by treating collection design, metadata schemas, and index parameters as deliberate interventions into how a region's knowledge and memory are structured.  
> - **P12 – Intelligence with a ZIP code** by binding memory collections to West Virginia–specific spatial layers, governance documents, and community narratives.  
> - **P16 – Power accountable to place** by making Ms. Jarvis's long‑term memory explicit, queryable, and auditable, rather than hidden inside opaque model parameters.  
> As such, this chapter belongs to the **Computational Instrument** tier: it defines the semantic memory substrate on which Quantarithmia's reasoning, GBIM's belief structures, and MountainShares‑oriented governance analysis actually run.

## 5. ChromaDB as Semantic Memory

### 5.1 Purpose and Scope

This chapter explains how Ms. Egeria Jarvis uses ChromaDB as the primary semantic memory layer backing the Hilbert‑space representation, GBIM, and the broader semantic fabric. ChromaDB is a vector database that stores high‑dimensional embedding vectors with associated metadata and exposes efficient similarity search and filtering operations. In this system, ChromaDB is not merely a convenience library; it is the concrete implementation of long‑term, queryable memory for documents, GIS features, governance texts, autonomous‑learning traces, and thesis materials.

Within the Quantarithmia program, ChromaDB is treated as the bridge between abstract Hilbert‑space representation and stored embeddings: vectors in each collection approximate elements of the high‑dimensional inner‑product space described in the previous chapter, but are realized through a specific embedding model and index implementation. It is the place where beliefs, contexts, and references become durable and retrievable for reasoning and retrieval‑augmented generation (RAG). Conceptually, each collection corresponds to an empirically instantiated subset of the Hilbert space \(H_{\text{App}}\), and stored vectors approximate elements of the spaces described in the previous chapter.

---

### 5.2 Role in the Ms. Jarvis Architecture

In the Ms. Jarvis architecture, ChromaDB plays several interlocking roles.

- **Semantic memory store (non‑spatial).**  
  Embeddings of texts and artifacts live in collections corresponding to domains such as governance, thesis content, autonomous learner outputs, conversations, and curated user‑memory–like traces. These collections support general semantic retrieval independent of geography.

- **Geospatial Hilbert layer (spatial).**  
  A unified GIS‑derived collection holds embeddings and metadata for West Virginia geospatial features, mirroring PostGIS tables and providing the Hilbert‑space representation of the spatial body described in the GBIM chapter. The current production deployment centers on the `gbim_worldview_entities` collection, which contains over 6.1M records with spatial provenance linking back to PostGIS geometries and belief graph edges.

- **Retrieval engine for RAG.**  
  At query time, services embed inputs and use ChromaDB similarity search, often with metadata filters, to retrieve the most relevant items for context and reasoning. This behavior instantiates the query projection and neighborhood selection mechanisms described in the Hilbert‑space model.

- **Structural backbone for inspectable memory.**  
  Because collections and metadata are explicitly defined, ChromaDB's structure mirrors core parts of GBIM, the GeoDB layer, and the thesis organization. This makes it possible to enumerate collections, inspect document counts, and audit metadata, rather than relying on hidden internal state.

This design makes the semantic memory system inspectable and debuggable: researchers and community partners can see what is stored, how it is grouped, and which collections underpin particular advisory behaviors.

---

### 5.3 Collections and Data Domains

In the deployment examined in late 2025 and early 2026, the primary Chroma instance exposes collections that fall into two broad families: general semantic memory and GeoDB‑derived spatial memory. A major consolidation completed in January 2026 ingested the GBIM worldview corpus into a unified `gbim_worldview_entities` collection, replacing the earlier fragmented `*_attrs` pattern with a single, comprehensive spatial memory index.

#### 5.3.1 Production Spatial Collection: `gbim_worldview_entities`

The primary spatial memory collection in production as of January 2026 is:

- **Collection name:** `gbim_worldview_entities`  
- **Record count:** 6,119,134  
- **Records with worldview context and spatial provenance:** 5,491,856  
- **Records currently lacking worldview, bbox, and dataset metadata:** 627,278  
- **Source datasets:** 204 standardized West Virginia GIS layers  
- **Worldview context:** UUID `002c2c84-2f18-40b7-8a98-b8d813dd6cc7`  

This collection is built by exporting GBIM worldview entities and their attributes from PostGIS, enriching them with spatial and provenance metadata, and indexing them as text embeddings in ChromaDB.

**Document structure**

Text documents use the pattern:

{source_table} {label}

Example:

text
wvgistcbuildingfootprints feat_1703912

**Core metadata fields (present for all records)**

  -  entity_id: UUID linking to gbim_worldview_entity.id

   - source_table: dataset name (for example, wvgistcbuildingfootprints, blocks_census_2020_utm83_full)

   -source_pk: primary key in source table (links to gbim_attrs.geodbid)

  -label: human‑readable entity label

-    centroid_x, centroid_y: spatial coordinates (EPSG:26917 – UTM Zone 17N NAD83)

**Extended metadata (populated via a backfill pipeline)**

  - worldview_id: worldview context UUID

  -  bbox: GeoJSON geometry or bounding box

   - confidence: belief confidence score (1.0 for GIS‑derived entities in this deployment)

   - dataset: source dataset name for provenance

   - geodb_id: original GeoDB identifier

   - srid: spatial reference identifier (26917)

A dedicated backfill process derives these extended fields from gbim_worldview_entity and gbim.gbim_attrs and attaches them to existing records in gbim_worldview_entities. As of January 28, 2026, 5,491,856 of the 6,119,134 records have non‑null worldview_id, bbox, and dataset fields, yielding approximately 90% extended metadata coverage. The remaining 627,278 records are left without these fields and are treated as a known gap to be addressed in future enrichment passes.

Coverage is monitored via automated scripts that iterate over the collection in batches, count non‑null values for key metadata fields across all 6,119,134 stored records, and report totals for worldview_id, bbox, and dataset.

**Representative source tables** (illustrative examples by entity count)

   - wvgistcbuildingfootprints – building footprints

   - wv_microsoft_20180207_utm17n83 – Microsoft building footprints

  - structurepointssouth_samb_2003_utm83 – southern structure points

   - structurepointsnorth_samb_2003_utm83 – northern structure points

  - blocks_census_2020_utm83_full – census blocks (full attribution)

  - windenergyresource_nationalrenewableenergylab_200901_utm83 – wind resource assessments

- floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83 – flood‑risk structures

- blocks_census_2020_utm83 – census blocks (standard)

- hospitals_wvdem_040519_utm83 – healthcare facilities

- railnetworkwv_usdot_200203_utm83 – rail infrastructure

**Ingestion status (January 2026)**

  - Export completed: 6,119,134 entities to a multi‑gigabyte CSV

  -  Batch ingestion into Chroma: thousands of entities per batch, respecting ChromaDB limits

   - Bulk ingest time: on the order of tens of hours of wall‑clock time, including a tuned resume pass after an initial compaction error

#### 5.3.2 Legacy and Historical Spatial Collections

Prior to the January 2026 consolidation, spatial memory was distributed across individual *_attrs collections corresponding to each GIS layer. These collections remain in the system for backward compatibility but are superseded by gbim_worldview_entities:

  - GBIM_ATTRS_CSV – consolidated attribute index (227 source tables)

  -  statewide_counties – 55 county entities

   - Per‑layer collections like wv_county_boundaries_24k_topo_updated_2022_utm83_attrs, legislative district layers, and infrastructure collections

Migration status: new queries should target gbim_worldview_entities; legacy collections are maintained for historical queries, validation, and debugging.

#### 5.3.3 General Semantic Collections

In the current deployment, the principal general‑semantic collections are:

  - autonomous_learning

  -  research_history

   - gbim_msjarvis_corpus

  - gbim_cakidd_personal_docs

  -  msjarvis_hilbertspace

   - msjarvis_learner_corpus

**Current status:** these collections are structurally defined with schema declarations but contain minimal or zero embeddings. They represent reserved namespaces for future ingestion of governance documents, thesis materials, autonomous learner outputs, and personal research corpora. Their presence establishes the intended semantic architecture, but they should not be described as active memory stores in this deployment without explicit population.

### 5.4 From Hilbert Space to ChromaDB

ChromaDB provides the concrete realization of the Hilbert‑space representation described in the previous chapter.

  - **Embeddings as vectors.**
    The embedding model maps texts and entities into high‑dimensional real vectors. ChromaDB stores these vectors alongside metadata (such as identifiers, timestamps, entity types, and geographic tags) and exposes operations such as nearest‑neighbor search, filtered retrieval, and upsert.

  -  **Collections as working subspaces.**
    Each ChromaDB collection corresponds to an empirically instantiated subset of the Hilbert space HAppHApp, grouping related vectors by purpose (for example, governance, conversation, thesis) or by entity type (for example, blocks, buildings, infrastructure). The gbim_worldview_entities collection represents the comprehensive spatial subspace HspatialHspatial in this deployment, containing the GBIM worldview entities with their provenance and belief‑graph connections.

   - **Queries as projections.**
    Incoming queries are embedded and used to probe relevant collections. This process effectively projects each query into the appropriate subset of HAppHApp, retrieves nearby vectors with respect to the inner‑product‑induced similarity measure, and returns associated documents and metadata for downstream reasoning.

This mapping allows Ms. Jarvis's memory to be described both geometrically, in terms of subsets and projections of a Hilbert space, and operationally, in terms of concrete collection queries and metadata filters.

### 5.5 Embedding Model and Dimensionality

In the RAG stack under analysis, Ms. Jarvis uses a sentence‑embedding model with 384‑dimensional outputs as the primary text embedding channel. The deployed Chroma catalog shows collections configured with dimension 384, confirming the ambient dimension of the main HtextHtext component for text‑based collections.

Any Chroma collection that stores embeddings produced by this model must be configured to accept 384‑dimensional vectors. This requirement applies both to general semantic collections and to the gbim_worldview_entities spatial collection, which uses consistent text embeddings for feature descriptions and attribute summaries.

 **Production deployment**

  - gbim_worldview_entities: 384‑dimensional embeddings (deployed)

  -  General semantic collections: 384‑dimensional schema declared (awaiting population)

   - Legacy *_attrs collections: 384‑dimensional embeddings (partial coverage)

The chapter therefore treats 384‑dimensional embeddings as the standard for the main semantic channel, while recognizing that additional channels or model upgrades may be introduced in future, along with corresponding schema and migration procedures.

### 5.6 ChromaDB Clients and Deployment Topology

ChromaDB is accessed as a shared HTTP service in this deployment; historical patterns using per‑service local stores are now considered legacy.

#### 5.6.1 Shared HTTP Service

In the active environment, services connect to a shared ChromaDB instance through an HTTP client configured with explicit host and port:

  - Endpoint: http://localhost:8002

  -  Container: jarvis-chroma (Docker)

   - Python client: chromadb.HttpClient(host="localhost", port=8002)

   - Persistent storage: persistent/chroma directory on host, mounted at /data in the container

**Connection example:**

python
import chromadb

client = chromadb.HttpClient(host="localhost", port=8002)
collection = client.get_collection("gbim_worldview_entities")
print(f"Total entities: {collection.count():,}")

The shared instance exposes both the production gbim_worldview_entities collection and legacy spatial collections. It is bound to persistent on‑disk storage and includes a chroma.sqlite3 catalog plus HNSW index directories. The instance is treated as the canonical semantic memory store for this deployment.

#### 5.6.2 Historical and Auxiliary Persistent Clients

Historically, some services used PersistentClient instances pointing to per‑service local paths such as .chromadb or chroma_db. Those local stores were used for isolated experiments, early autonomous‑learner work, and transitional states before consolidation into the shared instance.

As of January 2026, the operational intent is to converge on the shared HTTP‑backed store for primary semantic memory. Residual local stores are treated as legacy or experimental; their contents are either migrated or preserved as snapshots with clear documentation of their status.

### 5.7 Integration with GBIM, GeoDB, and RAG

ChromaDB is tightly integrated with GBIM, the GeoDB layer, and the broader RAG pipeline.

  - **GBIM linkage.**
    GBIM worldview entities are indexed in gbim_worldview_entities with metadata fields linking back to PostGIS tables via source_table and source_pk. The entity_id field provides stable UUID references to gbim_worldview_entity.id, enabling round‑trip queries from semantic search results to full belief provenance, including how, why, for_whom, and authority edges.

  -  **GeoDB integration.**
    The gbim_worldview_entities collection mirrors the gbim.gbim_attrs corpus. Spatial coordinates (centroid_x, centroid_y) and bounding boxes enable hybrid queries that combine semantic similarity with spatial filtering. Keys and metadata allow retrieval results to be rejoined to GBIM entities and geometries for display in geospatial tools.

   - **RAG context building.**
    For spatial questions, the intended RAG pipeline queries gbim_worldview_entities to retrieve relevant spatial entities and feature‑level embeddings. Retrieved texts, metadata, and spatial identifiers are combined into context windows for language models, with filtering by collection, geography, topic, and source. A prototype implementation follows this pattern and is in the process of being promoted to the default path for relevant query types.

   - **Belief graph traversal.**
    Once Chroma returns entity IDs, the system can perform SQL queries against GBIM belief and edge tables to retrieve the full epistemic context: data sources (how edges), policy justifications (why edges), beneficiary communities (for_whom edges), and authorizing frameworks (authority edges). Reference implementations exist; wiring them into all advisory flows is part of ongoing consolidation.

Example end‑to‑end query

python
##### Step 1: Semantic search in ChromaDB
import chromadb
client = chromadb.HttpClient(host="localhost", port=8002)
collection = client.get_collection("gbim_worldview_entities")

results = collection.query(
    query_texts=["hospitals in Morgantown"],
    n_results=10,
    where={"source_table": {"$in": ["hospitals_wvdem_040519_utm83"]}}
)

entity_ids = results["ids"]  # first query's IDs

##### Step 2: Retrieve full belief provenance from PostGIS + graph
import psycopg2
conn = psycopg2.connect("dbname=msjarvisgis")
cursor = conn.cursor()

for entity_id in entity_ids:
    cursor.execute("""
        SELECT 
            e.source_table,
            e.label,
            ST_AsText(a.geom) AS location,
            e.belief_state->'provenance' AS evidence
        FROM gbim_worldview_entity e
        JOIN gbim.gbim_attrs a
          ON a.sourcetable = e.source_table
         AND a.geodbid::text = e.source_pk
        WHERE e.id = %s
    """, (entity_id,))
    
    row = cursor.fetchone()
    print("Hospital:", row)

The end‑to‑end pipeline thus behaves as a structured walk through curated, domain‑specific memory organized around GBIM, the GeoDB spatial body, and Quantarithmia's research concepts.

### 5.8 Query Paths and JSON Structures

To connect the conceptual description with concrete operations, this section outlines canonical request and response shapes.

#### 5.8.1 ChromaDB Query Request

A typical query against gbim_worldview_entities includes:

  - query_texts: list of query strings to embed and search

  -  n_results: number of nearest neighbors to return per query

   - where: optional metadata filter (for example, restricting to source_table or spatial bounds)

   - include: fields to return (for example, ["metadatas", "documents", "distances"])

Example:

python
results = collection.query(
    query_texts=["buildings near flood zones"],
    n_results=100,
    where={"source_table": {"$in": ["wvgistcbuildingfootprints"]}},
    include=["distances", "metadatas", "documents"]
)

#### 5.8.2 ChromaDB Response Structure

The response contains parallel lists:

python
{
    "ids": [["entity-uuid-1", "entity-uuid-2", ...]],
    "distances": [[0.23, 0.45, ...]],
    "metadatas": [[
        {
            "entity_id": "uuid",
            "source_table": "wvgistcbuildingfootprints",
            "source_pk": "1703912",
            "label": "feat_1703912",
            "centroid_x": 518670.34845,
            "centroid_y": 4307829.86015,
            "dataset": "wvgistcbuildingfootprints",
            "geodb_id": "1703912",
            "confidence": 1.0,
            "srid": 26917
        },
        ...
    ]],
    "documents": [["wvgistcbuildingfootprints feat_1703912", ...]]
}

These structures provide concrete anchors for documentation, testing, and debugging, making it possible to trace RAG behavior end‑to‑end.

### 5.9 Operational Considerations

Using ChromaDB as a production memory layer introduces several practical considerations.

**Reliability and persistence**

The main Chroma instance is bound to the persistent/chroma directory on the host, mounted into the jarvis-chroma container as /data. Regular backups of this directory are required, particularly around large ingests and metadata backfills. Residual local .chromadb directories from earlier stores should be either archived or formally decommissioned to avoid ambiguity.

**Performance and scaling**

As gbim_worldview_entities grows past 6M records, index configuration and hardware resources directly affect query latency and throughput for similarity search.[web:1136] Bulk ingest has used batch sizes on the order of several thousand entities and sustained throughput on the order of hundreds of entities per second. Chroma's HNSW indices must be configured and monitored so that query latency remains acceptable even as the stored item count increases.

**Security and privacy**

The documented Chroma deployment focuses on public or research‑grade data: West Virginia GIS layers and internal research corpora. Any collections that would contain sensitive user data, private keys, or non‑consensual logs must be excluded, redacted, or restricted. Conversational or personal‑memory collections must be curated before being used outside a controlled environment.

**Schema and configuration management**

Collection names, metadata schemas, and embedding configurations (model and dimension) are versioned and recorded in a central registry. The January 2026 consolidation to gbim_worldview_entities represents a major schema migration from fragmented *_attrs collections to a unified spatial index. Forward‑ and backward‑compatibility considerations are documented, with legacy collections maintained for historical queries.

## 5.10 Production Deployment Statistics (January 2026)

**Spatial memory (gbim_worldview_entities)**

   - 6,119,134 records exported from PostGIS

   - 5,491,856 records with extended provenance metadata (worldview_id, bbox, and dataset) present

  - 627,278 records currently lacking extended provenance metadata, treated as a known enrichment backlog

   - 204 source GIS datasets

  *Core spatial metadata coverage*: all records have entity_id, source_table, source_pk, and centroid coordinates

-   Extended provenance fields (worldview_id, bbox, dataset, geodb_id, srid, confidence) attached via a dedicated backfill pipeline for approximately 90% of records, with coverage monitored by automated scripts

-    SRID 26917 (UTM Zone 17N NAD83) standardization

**Belief graph integration**

-   GBIM belief and edge tables encode how, why, for_whom, and authority relationships for millions of worldview entities

-  Chroma metadata (entity_id, source_table, source_pk) enables deterministic joins from semantic results into these belief structures

**Storage and performance**

   - CSV export: multi‑gigabyte file in /tmp/gbim_entities_for_chroma_backfill.csv used for bulk ingest and metadata backfill

   - Persistent storage: persistent/chroma directory backing the shared Chroma instance

-    Container: jarvis-chroma (Docker, serving HTTP on port 8002)

 -   Embedding dimension: 384 (sentence‑embedding model)

  -  Batch ingestion: several thousand entities per batch

   - Bulk ingest throughput: on the order of 100 entities per second during initial load

**General semantic collections**

  -  autonomous_learning, research_history, gbim_msjarvis_corpus, gbim_cakidd_personal_docs, msjarvis_hilbertspace, msjarvis_learner_corpus: schema declared, awaiting systematic population

### 5.11 Limitations and Future Work

**Partial embedding coverage in general‑semantic domains**

Spatial collections are heavily populated via gbim_worldview_entities, but key Ms. Jarvis semantic corpora (gbim_msjarvis_corpus, msjarvis_hilbertspace, msjarvis_learner_corpus, research_history) are present with few or no embeddings. Completing ingestion and embedding backfill for these collections is a priority for achieving a fully realized semantic memory.

**Model and index dependence**

Retrieval quality depends on the chosen embedding model (currently 384‑dimensional), index parameters, and collection design. Changes to any of these elements can alter the Steward System's apparent memory; model upgrades and reindexing are therefore treated as explicit migrations with before/after evaluation.

**Semantic gaps and representational limits**

Certain forms of knowledge—such as embodied experience, collective trauma narratives, and spiritual traditions—are difficult to represent as short text embeddings alone. Additional representational strategies, including graph structures, qualitative annotations, GBIM‑linked justice metrics, and community‑led tagging, are needed to supplement the vector store.

**Evolving schema and topology**

As GBIM, GeoDB, and Quantarithmia evolve, the set of collections, metadata fields, and indexing strategies will continue to change. The January 2026 consolidation from *_attrs to gbim_worldview_entities demonstrates this evolution. Migration tools and versioned schemas are necessary to maintain continuity across thesis revisions and deployments.

**Future work**

  -  Maintain gbim_worldview_entities via incremental updates and periodic metadata backfills

 -   Backfill general semantic collections with governance documents, thesis materials, and autonomous learner outputs

  -  Document all collection schemas in a single, queryable registry

  -  Add traced end‑to‑end RAG examples showing Chroma retrieval → GBIM provenance → belief‑graph traversal

 -   Explore hybrid memory architectures combining vector stores with graphs, relational databases, and participatory annotation workflows

  -  Implement incremental sync infrastructure for daily delta updates instead of full rebuilds

  -  Develop or adopt embedding models fine‑tuned on Appalachian place names and infrastructure terminology

**Implementation Status**

**Badge: PRODUCTION / CONSOLIDATING**

The conceptual role of ChromaDB as semantic memory is fully implemented for spatial entities through:

   - A production gbim_worldview_entities collection with 6,119,134 records indexed in a shared HTTP‑backed Chroma service

  -  A shared jarvis-chroma container on port 8002 with persistent on‑disk storage

  -  Core spatial metadata coverage (entity_id, source_table, source_pk, centroids) enabling deterministic joins back to GBIM

- **Consolidation:**

   - Extended provenance metadata (worldview_id, bbox, dataset, geodb_id, srid, confidence) has been successfully attached for 5,491,856 records, with the remaining 627,278 records explicitly tracked for future enrichment

-    Belief‑graph integration (how, why, for_whom, authority edges) is implemented in GBIM and used in prototype end‑to‑end flows, with full adoption across advisory behaviors in progress

   - General semantic collections (governance, thesis, autonomous learner) have schema declared but are not yet fully populated

 -   Full end‑to‑end RAG trace documentation, from query through Chroma and GBIM to belief provenance, is under active development

