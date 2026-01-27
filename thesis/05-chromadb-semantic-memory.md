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
  A large family of GIS‑derived collections holds embeddings and metadata for West Virginia geospatial features, mirroring PostGIS tables and providing the Hilbert‑space representation of the spatial body described in the GBIM chapter. **The current production deployment centers on the `gbim_worldview_entities` collection**, which contains 6.1M entities with full spatial provenance linking back to PostGIS geometries and belief graph edges.

- **Retrieval engine for RAG.**  
  At query time, services embed inputs and use ChromaDB similarity search, often with metadata filters, to retrieve the most relevant items for context and reasoning. This behavior instantiates the query projection and neighborhood selection mechanisms described in the Hilbert‑space model.

- **Structural backbone for inspectable memory.**  
  Because collections and metadata are explicitly defined, ChromaDB's structure mirrors core parts of GBIM, the GeoDB layer, and the thesis organization. This makes it possible to enumerate collections, inspect document counts, and audit metadata, rather than relying on hidden internal state.

This design makes the semantic memory system inspectable and debuggable: researchers and community partners can see what is stored, how it is grouped, and which collections underpin particular advisory behaviors.

---

### 5.3 Collections and Data Domains

In the deployment examined in late 2025 and early 2026, the primary Chroma instance exposes collections that fall into two broad families: general semantic memory and GeoDB‑derived spatial memory. **A major consolidation completed in January 2026 ingested all 5.5M GBIM worldview entities into a unified `gbim_worldview_entities` collection**, replacing the earlier fragmented `*_attrs` pattern with a single, comprehensive spatial memory index.

#### 5.3.1 Production Spatial Collection: `gbim_worldview_entities`

**The primary spatial memory collection** in production as of January 2026:

- **Collection name:** `gbim_worldview_entities`
- **Entity count:** 6,119,134 (includes multi-representation geometries)
- **Unique worldview entities:** 5,491,566 (from `public.gbim_worldview_entity`)
- **Source datasets:** 204 standardized West Virginia GIS layers
- **Worldview context:** UUID `002c2c84-2f18-40b7-8a98-b8d813dd6cc7`

**Document structure:**

{source_table} {label}

text
Example: `wvgistcbuildingfootprints feat_1703912`

**Metadata fields:**
- `entity_id`: UUID linking to `gbim_worldview_entity.id`
- `source_table`: Dataset name (e.g., `wvgistcbuildingfootprints`, `blocks_census_2020_utm83_full`)
- `source_pk`: Primary key in source table (links to `gbim_attrs.geodbid`)
- `label`: Human-readable entity label
- `centroid_x`, `centroid_y`: Spatial coordinates (EPSG:26917 - UTM Zone 17N NAD83)

**Extended metadata** (populated during ingestion):
- `worldview_id`: Worldview context UUID
- `bbox`: GeoJSON bounding box
- `confidence`: Belief confidence score (1.0 for all GIS-derived entities)
- `dataset`: Source dataset name for provenance
- `geodb_id`: Original GeoDB identifier
- `srid`: Spatial reference identifier (26917)

**Representative source tables** (top 10 by entity count):
1. `wvgistcbuildingfootprints` - 2,120,825 building footprints
2. `wv_microsoft_20180207_utm17n83` - 1,020,048 Microsoft building footprints
3. `structurepointssouth_samb_2003_utm83` - 745,032 southern structure points
4. `structurepointsnorth_samb_2003_utm83` - 621,927 northern structure points
5. `blocks_census_2020_utm83_full` - 145,116 census blocks (full attribution)
6. `windenergyresource_nationalrenewableenergylab_200901_utm83` - 104,812 wind resource assessments
7. `floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83` - 81,054 flood-risk structures
8. `blocks_census_2020_utm83` - 72,558 census blocks (standard)
9. `hospitals_wvdem_040519_utm83` - Healthcare facilities
10. `railnetworkwv_usdot_200203_utm83` - Rail infrastructure

**Ingestion status (January 27, 2026):**
- Export completed: 6,119,134 entities to CSV (4.3GB)
- Batch size: 5,460 entities (ChromaDB maximum)
- Ingestion rate: ~95 entities/second
- Estimated completion: 18 hours from start (in progress)

#### 5.3.2 Legacy and Historical Spatial Collections

Prior to the January 2026 consolidation, spatial memory was distributed across individual `*_attrs` collections corresponding to each GIS layer. These collections remain in the system for backward compatibility but are superseded by `gbim_worldview_entities`:

- `GBIM_ATTRS_CSV` - Consolidated attribute index (227 source tables)
- `statewide_counties` (55 county entities)
- Per-layer collections like `wv_county_boundaries_24k_topo_updated_2022_utm83_attrs`, legislative district layers, infrastructure collections, etc.

**Migration status:** New queries should target `gbim_worldview_entities`; legacy collections are maintained for historical queries and debugging.

#### 5.3.3 General Semantic Collections

In the current deployment, the principal general‑semantic collections are:

- `autonomous_learning`  
- `research_history`  
- `gbim_msjarvis_corpus`  
- `gbim_cakidd_personal_docs`  
- `msjarvis_hilbertspace`  
- `msjarvis_learner_corpus`  

**Current status:** These collections are structurally defined with schema declarations but contain minimal or zero embeddings. They represent reserved namespaces for future ingestion of governance documents, thesis materials, autonomous learner outputs, and personal research corpora. Their presence establishes the intended semantic architecture, but they should not be described as active memory stores in this deployment without explicit population.

---

### 5.4 From Hilbert Space to ChromaDB

ChromaDB provides the concrete realization of the Hilbert‑space representation described in the previous chapter.

- **Embeddings as vectors.**  
  The embedding model maps texts and entities into high‑dimensional real vectors. ChromaDB stores these vectors alongside metadata (such as identifiers, timestamps, entity types, and geographic tags) and exposes operations such as nearest‑neighbor search, filtered retrieval, and upsert.

- **Collections as working subspaces.**  
  Each ChromaDB collection corresponds to an empirically instantiated subset of the Hilbert space \(H_{\text{App}}\), grouping related vectors by purpose (for example, governance, conversation, thesis) or by entity type (for example, blocks, buildings, infrastructure). **The `gbim_worldview_entities` collection represents the comprehensive spatial subspace** \(H_{\text{spatial}}\), containing all 5.5M GBIM entities with their provenance and belief graph connections.

- **Queries as projections.**  
  Incoming queries are embedded and used to probe relevant collections. This process effectively projects each query into the appropriate subset of \(H_{\text{App}}\), retrieves nearby vectors with respect to the inner‑product‑induced similarity measure, and returns associated documents and metadata for downstream reasoning.

This mapping allows Ms. Jarvis's memory to be described both geometrically, in terms of subsets and projections of a Hilbert space, and operationally, in terms of concrete collection queries and metadata filters.

---

### 5.5 Embedding Model and Dimensionality

In the RAG stack under analysis, Ms. Jarvis uses a sentence‑embedding model with **384‑dimensional outputs** as the primary text embedding channel. The deployed Chroma catalog shows collections configured with dimension 384, confirming the ambient dimension of the main \(H_{\text{text}}\) component for text‑based collections.

Any Chroma collection that stores embeddings produced by this model must be configured to accept 384‑dimensional vectors. This requirement applies both to general semantic collections and to the `gbim_worldview_entities` spatial collection, which uses consistent text embeddings for feature descriptions and attribute summaries.

**Production deployment:**
- `gbim_worldview_entities`: 384-dimensional embeddings (in progress)
- General semantic collections: 384-dimensional schema declared (awaiting population)
- Legacy `*_attrs` collections: 384-dimensional embeddings (partial coverage)

The chapter therefore treats 384‑dimensional embeddings as the standard for the main semantic channel, while recognizing that additional channels or model upgrades may be introduced in future, along with corresponding schema and migration procedures.

---

### 5.6 ChromaDB Clients and Deployment Topology

ChromaDB is accessed as a shared HTTP service in this deployment; historical patterns using per‑service local stores are now considered legacy.

#### 5.6.1 Shared HTTP Service

In the active environment, services connect to a shared ChromaDB instance through an HTTP client configured with explicit host and port:

- **Endpoint:** `http://localhost:8002`
- **Container:** `jarvis-chroma` (Docker, 3 days uptime as of Jan 27, 2026)
- **Python client:** `chromadb.HttpClient(host="localhost", port=8002)`
- **Persistent storage:** `persistent/chroma` directory on host, mounted at `/data` in container

**Connection example:**
``python
import chromadb

client = chromadb.HttpClient(host="localhost", port=8002)
collection = client.get_collection("gbim_worldview_entities")
print(f"Total entities: {collection.count():,}")

The shared instance exposes both the production gbim_worldview_entities collection and legacy spatial collections. It is bound to persistent on-disk storage and includes a chroma.sqlite3 catalog plus HNSW index directories. The instance is treated as the canonical semantic memory store for this deployment.

5.6.2 Historical and Auxiliary Persistent Clients

Historically, some services used PersistentClient instances pointing to per‑service local paths such as .chromadb or chroma_db. Those local stores were used for isolated experiments, early autonomous‑learner work, and transitional states before consolidation into the shared instance.

As of January 2026, the operational intent is to converge on the shared HTTP‑backed store for primary semantic memory. Residual local stores are treated as legacy or experimental; their contents are either migrated or preserved as snapshots with clear documentation of their status.

5.7 Integration with GBIM, GeoDB, and RAG

ChromaDB is tightly integrated with GBIM, the GeoDB layer, and the broader RAG pipeline.

  GBIM linkage.
  All 5.5M GBIM worldview entities are indexed in gbim_worldview_entities with metadata fields linking back to PostGIS tables via source_table and source_pk. The entity_id field provides stable UUID references to gbim_worldview_entity.id, enabling round-trip queries from semantic search results to full belief provenance including how, why, for_whom, and authority edges.
  
  GeoDB integration.
    The gbim_worldview_entities collection mirrors the complete PostGIS gbim.gbim_attrs corpus. Spatial coordinates (centroid_x, centroid_y) and bounding boxes enable hybrid queries that combine semantic similarity with spatial filtering. Keys and metadata allow retrieval results to be rejoined to GBIM entities and geometries for display in geospatial tools.
    
   RAG context building.
    When Ms. Jarvis answers a question, the RAG pipeline queries gbim_worldview_entities to retrieve relevant spatial entities and feature-level embeddings. Retrieved texts, metadata, and spatial identifiers are combined into context windows for language models, with filtering by collection, geography, topic, and source. This implements the context subspace selection and HeffHeff restriction described in the Hilbert‑space chapter.
    
  Belief graph traversal.
    Once Chroma returns entity IDs, the system performs SQL queries against cakidd.gbim_graph_edges to retrieve the full epistemic context: data sources (how edges), policy justifications (why edges), beneficiary communities (for_whom edges), and authorizing frameworks (authority edges).

Example end-to-end query:

python
# Step 1: Semantic search in ChromaDB
import chromadb
client = chromadb.HttpClient(host="localhost", port=8002)
collection = client.get_collection("gbim_worldview_entities")

results = collection.query(
    query_texts=["hospitals in Morgantown"],
    n_results=10,
    where={"source_table": {"$in": ["hospitals_wvdem_040519_utm83"]}}
)

entity_ids = results['ids']

# Step 2: Retrieve full belief provenance from PostGIS + graph
import psycopg2
conn = psycopg2.connect("dbname=msjarvisgis")
cursor = conn.cursor()

for entity_id in entity_ids:
    cursor.execute("""
        SELECT 
            e.source_table,
            e.label,
            ST_AsText(a.geom) AS location,
            e.belief_state->'provenance' AS evidence,
            array_agg(g.role || ': ' || g.target_ref) AS edges
        FROM gbim_worldview_entity e
        JOIN gbim.gbim_attrs a ON (a.sourcetable = e.source_table AND a.geodbid::text = e.source_pk)
        LEFT JOIN cakidd.gbim_graph_edges g ON g.belief_ref = e.id::text
        WHERE e.id = %s
        GROUP BY e.id, e.source_table, e.label, a.geom, e.belief_state
    """, (entity_id,))
    
    row = cursor.fetchone()
    print(f"Hospital: {row}")
    print(f"Location: {row}")
    print(f"Evidence: {row}")
    print(f"Edges: {row}")

The end‑to‑end pipeline thus behaves as a structured walk through curated, domain‑specific memory organized around GBIM, the GeoDB spatial body, and Quantarithmia's research concepts.

5.8 Query Paths and JSON Structures

To connect the conceptual description with concrete operations, this section outlines canonical request and response shapes.

5.8.1 ChromaDB Query Request

A typical query against gbim_worldview_entities includes:

  query_texts: List of query strings to embed and search

  n_results: Number of nearest neighbors to return per query

  where: Optional metadata filter (e.g., restricting to source_table or spatial bounds)

  include: Fields to return (["metadatas", "documents", "distances"])

Example:

python
results = collection.query(
    query_texts=["buildings near flood zones"],
    n_results=100,
    where={"source_table": {"$in": ["wvgistcbuildingfootprints"]}},
    include=["distances", "metadatas", "documents"]
)


5.8.2 ChromaDB Response Structure

The response contains parallel lists:

python
{
    'ids': [['entity-uuid-1', 'entity-uuid-2', ...]],
    'distances': [[0.23, 0.45, ...]],
    'metadatas': [[
        {
            'entity_id': 'uuid',
            'source_table': 'wvgistcbuildingfootprints',
            'source_pk': '1703912',
            'label': 'feat_1703912',
            'centroid_x': 518670.34845,
            'centroid_y': 4307829.86015,
            'dataset': 'wvgistcbuildingfootprints',
            'geodb_id': '1703912',
            'confidence': 1.0,
            'srid': '26917'
        },
        ...
    ]],
    'documents': [['wvgistcbuildingfootprints feat_1703912', ...]]
}

These structures provide concrete anchors for documentation, testing, and debugging, making it possible to trace RAG behavior end‑to‑end.

5.9 Operational Considerations

Using ChromaDB as a production memory layer introduces several practical considerations.
Reliability and Persistence

The main Chroma instance is bound to the persistent/chroma directory on the host, mounted into the jarvis-chroma container as /data. Regular backups of this directory are required, particularly during the ongoing 6.1M entity ingestion. Residual local .chromadb directories from earlier stores should be either archived or formally decommissioned to avoid ambiguity.

Performance and Scaling

As gbim_worldview_entities grows to 6.1M entities, index configuration and hardware resources directly affect query latency. Current ingestion performance:

  Batch size: 5,460 entities (ChromaDB maximum)

  Ingestion rate: ~95 entities/second

  Total ingestion time: ~18 hours for full corpus

  Query latency (projected): <100ms for top-10 semantic search once indexing completes

Chroma's HNSW indices must be configured and monitored so that query latency remains acceptable even as the stored item count increases.

Security and Privacy

The documented Chroma deployment focuses on public or research‑grade data: West Virginia GIS layers and internal research corpora. Any collections that would contain sensitive user data, private keys, or non‑consensual logs must be excluded, redacted, or restricted. Conversational or personal‑memory collections must be curated before being used outside a controlled environment.

Schema and Configuration Management

Collection names, metadata schemas, and embedding configurations (model and dimension) are versioned and recorded in a central registry. The January 2026 consolidation to gbim_worldview_entities represents a major schema migration from fragmented *_attrs collections to a unified spatial index. Forward‑ and backward‑compatibility considerations are documented, with legacy collections maintained for historical queries.

5.10 Production Deployment Statistics (January 2026)

Spatial memory (gbim_worldview_entities):

  6,119,134 entities exported from PostGIS

  5,491,566 unique worldview entities (deduplication in progress)

  204 source GIS datasets

  100% spatial metadata coverage (all entities have centroid coordinates)

  100% provenance coverage (all entities link to belief_state with dataset, geodb_id, bbox)

  SRID 26917 (UTM Zone 17N NAD83) standardization

Belief graph integration:

  5,491,566 how edges (every entity → source dataset)

  5,491,566 for_whom edges (census blocks → residents; infrastructure → west_virginia_public)

  2,121,230 why edges (legacy worldview 3)

  2,121,230 authority edges (legacy worldview 3)

Storage and performance:

  Export file: 4.3GB CSV

  Persistent storage: persistent/chroma directory

  Container: jarvis-chroma (Docker, running on port 8002)

  Embedding dimension: 384 (sentence transformer)

  Batch ingestion: 5,460 entities per batch

  Ingestion rate: ~95 entities/second

  Estimated completion: 18 hours (in progress as of Jan 27, 2026)

General semantic collections:

  autonomous_learning, research_history, gbim_msjarvis_corpus, gbim_cakidd_personal_docs, msjarvis_hilbertspace, msjarvis_learner_corpus: Schema declared, awaiting population

5.11 Limitations and Future Work

Current use of ChromaDB has several limitations and active areas of work:
Partial Embedding Coverage in General‑Semantic Domains

Spatial collections are heavily populated with the ongoing ingestion of 6.1M entities into gbim_worldview_entities, but key Ms. Jarvis semantic corpora (gbim_msjarvis_corpus, msjarvis_hilbertspace, msjarvis_learner_corpus, research_history) are present with zero embeddings. Completing ingestion and embedding backfill for these collections is a priority for achieving a fully realized semantic memory.

Model and Index Dependence

Retrieval quality depends on the chosen embedding model (currently 384‑dimensional), index parameters, and collection design. Changes to any of these elements can alter the Steward System's apparent memory; model upgrades and reindexing are therefore treated as explicit migrations with before/after evaluation.

Semantic Gaps and Representational Limits

Certain forms of knowledge—such as embodied experience, collective trauma narratives, and spiritual traditions—are difficult to represent as short text embeddings alone. Additional representational strategies, including graph structures, qualitative annotations, GBIM‑linked justice metrics, and community‑led tagging, are needed to supplement the vector store.

Evolving Schema and Topology

As GBIM, GeoDB, and Quantarithmia evolve, the set of collections, metadata fields, and indexing strategies will continue to change. The January 2026 consolidation from *_attrs to gbim_worldview_entities demonstrates this evolution. Migration tools and versioned schemas are necessary to maintain continuity across thesis revisions and deployments.
Future Work

  Complete gbim_worldview_entities ingestion (18 hours remaining as of Jan 27, 2026)

  Backfill general semantic collections with governance documents, thesis materials, autonomous learner outputs
  Document all collection schemas in a single, queryable registry

  Add traced end‑to‑end RAG examples showing Chroma retrieval → GBIM provenance → belief graph traversal
  
  Explore hybrid memory architectures combining vector stores with graphs, relational databases, and participatory annotation workflows
  
  Incremental sync infrastructure for daily delta updates instead of full rebuilds
  
  Custom embedding model fine-tuned on Appalachian place names and infrastructure terminology

Implementation Status

Badge: PRODUCTION / CONSOLIDATING

The conceptual role of ChromaDB as semantic memory is fully implemented for spatial entities through:

  Production gbim_worldview_entities collection with 6.1M entities (ingestion in progress)
    
  Shared HTTP‑backed Chroma service (jarvis-chroma container on port 8002)

  100% spatial metadata and provenance coverage
   
  Full belief graph integration (how, why, for_whom, authority edges)
  
  Round-trip query capability from semantic search → PostGIS geometries → belief provenance

In consolidation:
  
  General semantic collections (governance, thesis, autonomous learner) schema declared but unpopulated

  Legacy *_attrs collections maintained for backward compatibility

  Full end‑to‑end RAG trace documentation in progress

