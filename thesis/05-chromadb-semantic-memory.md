## Why this matters for Polymathmatic Geography

This chapter describes how Ms. Jarvis uses ChromaDB as its primary semantic memory layer to support place-based reasoning about West Virginia. The system combines 5.4 million GBIM worldview entities stored as embeddings in ChromaDB with structured PostgreSQL databases (`msjarvis` for belief relationships, `gisdb` for PostGIS spatial data) to create an inspectable, queryable memory system that grounds AI responses in verified geographic and institutional context.

This architecture supports:

- **P1 – Every where is entangled** by storing GBIM entities, GIS features, and resource documents as searchable embeddings in ChromaDB collections (`gbim_worldview_entities`, `autonomous_learner`, `gis_wv_benefits`) that can be jointly retrieved, filtered by metadata, and linked back to structured PostgreSQL belief tables and PostGIS geometries, treating legal, infrastructural, and social facts about Appalachia as interconnected memory rather than isolated files.

- **P3 – Power has a geometry** by representing institutional relationships and access to services as explicit GBIM belief edges in PostgreSQL, ChromaDB embeddings with geographic metadata, and PostGIS spatial features whose retrieval paths can be logged, inspected, and audited, making it possible to trace how the system traverses memory when answering questions about extraction, obligation, and care.

- **P5 – Design is a geographic act** by treating ChromaDB collection schemas, embedding model choices, metadata conventions, PostgreSQL GBIM table structures, and RAG retrieval rules as deliberate interventions into how West Virginia is represented and searched, ensuring that design decisions about semantic memory are understood as decisions about regional perception and action.

- **P12 – Intelligence with a ZIP code** by binding ChromaDB collections and PostgreSQL spatial tables to West Virginia-specific layers, with GBIM entities carrying county/ZIP metadata and PostGIS tables containing 993 WV ZCTA centroids, so that queries about help, risk, or opportunity are resolved through structures that explicitly encode where people live and which institutions serve them.

- **P16 – Power accountable to place** by making semantic memory, retrieval behavior, and query-to-evidence links explicit and queryable through ChromaDB collection logs, PostgreSQL GBIM belief provenance tables, and PostGIS spatial joins that show which entities, features, and resources contributed to answers about particular communities, instead of hiding choices in opaque model weights.

This chapter belongs to the **Computational Instrument** tier: it defines the production semantic memory substrate—centered on ChromaDB collections and dual PostgreSQL databases (`msjarvis` for beliefs, `gisdb` for spatial data)—that Quantarithmia's reasoning, GBIM's belief structures, spatial queries, and MountainShares governance analysis run on in the live system.

---

## 5. ChromaDB as Semantic Memory

### 5.1 Purpose and Scope

This chapter explains how Ms. Jarvis uses ChromaDB as the primary semantic memory layer for the Hilbert-space representation, GBIM worldview entities, autonomous learning, and resource retrieval. ChromaDB is a vector database that stores high-dimensional embedding vectors with associated metadata and provides efficient similarity search and filtering operations.

In this system, ChromaDB serves as the concrete implementation of long-term, queryable memory for:
- 5.4 million GBIM worldview entities (geographic features across West Virginia)
- Autonomous learning patterns and research traces
- Community resource documents and benefits guides
- Governance texts and thesis materials
- Psychological safety and spiritual corpora

<p align="center">
  <img src="https://github.com/user-attachments/assets/5f6bf0d9-91ca-4692-8b1c-95fbceec81b7"
       alt="ChromaDB as Semantic Memory in Ms. Jarvis"
       width="900">
</p>

> *Figure 1 – ChromaDB as Semantic Memory in Ms. Jarvis. Services embed texts and GIS features into ChromaDB collections. The semantic layer links back to structured PostgreSQL databases (msjarvis for GBIM beliefs, gisdb for PostGIS spatial data) enabling traceable, inspectable retrieval for RAG.*

Within the Quantarithmia program, ChromaDB bridges abstract Hilbert-space representation and stored embeddings: vectors in each collection approximate elements of the high-dimensional inner-product space, realized through a specific embedding model and index implementation. Collections like `gbim_worldview_entities` correspond to empirically instantiated subsets of H_App, with stored vectors linking to structured PostgreSQL belief tables and PostGIS geometries.

**Database Architecture (Verified March 14, 2026):**

Ms. Jarvis uses a **dual-database PostgreSQL cluster** on port 5433:

**Database 1: `msjarvis` (8 MB, 6 tables)**
- GBIM belief structure and relationships
- Tables: `gbim_beliefs`, `gbim_belief_edges`, `gbim_belief_evidence`, `gbim_evidence`, `gbim_layer_catalog`, `gbim_worldviews`
- Stores belief provenance, epistemic relationships, evidence chains
- Small size because bulk entity data lives in ChromaDB

**Database 2: `gisdb` (13 GB, 39 tables)**  
- PostGIS-enabled spatial database
- Contains `zcta_wv_centroids` (993 West Virginia ZIP centroids)
- Spatial reference tables, geographic boundaries, infrastructure layers
- Enables geographic queries and spatial joins

**ChromaDB (Primary Semantic Storage):**
- 5,416,521 GBIM worldview entities in `gbim_worldview_entities` collection
- 21,160+ autonomous learning entries
- Multiple resource and benefits collections
- Total storage: Substantial vector index (10+ GB persistent volume)

This separation enables:
- Independent backup/restore strategies
- PostGIS spatial optimization in dedicated database
- Lightweight GBIM belief graph in PostgreSQL
- Bulk semantic search in ChromaDB vector store

---

### 5.2 Role in the Ms. Jarvis Architecture

ChromaDB plays several interlocking roles in the system:

**Semantic memory store (non-spatial)**  
Embeddings of texts and artifacts live in domain-specific collections: governance documents, thesis content, autonomous learner outputs, resource guides, research traces. These support semantic retrieval independent of geography.

**Geospatial semantic layer (spatial)**  
The unified `gbim_worldview_entities` collection holds 5,416,521 embeddings of West Virginia geospatial features, providing semantic representation of the spatial body. Complementary collections like `gis_wv_benefits` focus on benefits-relevant facilities and programs.

**Retrieval engine for RAG**  
Services embed queries and use ChromaDB similarity search with metadata filters to retrieve relevant context. Text RAG handles general semantic queries; GIS RAG uses spatial collections. Retrieved items link back to PostgreSQL for full provenance before being passed to the ensemble.

**Structural backbone for inspectable memory**  
Collections and metadata explicitly mirror GBIM structure, PostGIS spatial tables, and resource registries. This enables enumeration, inspection, auditing, and correlation of RAG calls with underlying memory, avoiding hidden internal state.

This design makes semantic memory inspectable and debuggable: operators can see what's stored, how it's grouped, which collections underpin particular responses, and how retrieval results link to structured PostgreSQL provenance.

---

### 5.3 Collections and Data Domains

The primary ChromaDB instance exposes collections across three families: spatial memory, general semantic memory, and resource-focused collections.

#### 5.3.1 Production Spatial Collection

**Primary spatial memory (Verified complete March 14, 2026):**

- **Collection name:** `gbim_worldview_entities`
- **Record count:** 5,416,521 (verified via `col.count()`)
- **Source:** 200+ West Virginia GIS layers
- **Coordinate system:** EPSG:26917 (UTM Zone 17N NAD83)
- **Metadata:** Entity IDs, source tables, centroids, counties, ZIPs

This collection represents the complete GBIM worldview export: every standardized geospatial feature from West Virginia's official GIS datasets, enriched with spatial and provenance metadata, indexed as searchable text embeddings.

**Ingest timeline:**
- Start: March 13, 2026
- Completion: March 14, 2026, 15:45 EDT
- Duration: ~40 hours
- Processing rate: ~40,000 entities/minute

<p align="center">
  <img src="https://github.com/user-attachments/assets/1469b3c1-f9e8-4b9d-a021-a79baa89ee58"
       alt="End-to-End Spatial RAG Query through ChromaDB and GBIM"
       width="900">
</p>

> *Figure 2 – Consolidated spatial memory collection. The unified spatial collection links ChromaDB vectors to PostgreSQL GBIM belief tables (msjarvis database) and PostGIS geometries (gisdb database) for traceable spatial RAG.*

**Document structure example:**
```text
wvgistcbuildingfootprints feat_1703912
```

**Core metadata fields:**
- `entity_id`: UUID linking to PostgreSQL belief records
- `source_table`: Dataset name (e.g., `wvgistcbuildingfootprints`, `blocks_census_2020`)
- `source_pk`: Primary key in source table
- `label`: Human-readable entity label
- `centroid_x`, `centroid_y`: UTM coordinates

**Extended metadata (via backfill pipeline):**
- `worldview_id`: Worldview context UUID
- `bbox`: GeoJSON geometry or bounding box
- `dataset`: Source dataset for provenance
- `county`: West Virginia county
- `zip`: ZIP code where applicable

---

#### 5.3.2 Legacy Spatial Collections

Prior to consolidation, spatial memory existed as individual `*_attrs` collections per GIS layer. These remain for backward compatibility but are superseded by the unified `gbim_worldview_entities` collection. New queries target the consolidated index.

---

#### 5.3.3 General Semantic Collections

Principal non-spatial collections include:

**`autonomous_learner` (21,160+ items, growing)**  
- Deployed March 14, 2026 (ChromaDB-Lite architecture)
- Stores autonomous research findings every 5 minutes
- Topics: MountainShares security, Appalachian development, governance systems, AI ethics
- Growth rate: ~288 items/day

**`psychological_rag` (968 items)**  
- Mental health and psychological safety resources
- Used for queries about trauma, wellbeing, counseling

**`spiritual_texts` (23 items)**  
- Mother Carrie Protocol spiritual corpus
- Multi-tradition texts with Quaker-Appalachian prioritization

**`msjarvis_docs` (system documentation)**  
- Technical documentation and architecture guides
- Thesis materials and research notes

**`GBIM_sample_rows` (5,000 items)**  
- GBIM testing and validation sample
- Representative cross-section for development

---

#### 5.3.4 Resource and Benefits Collections

Resource-focused collections store community assistance guides, program descriptions, and benefits information with metadata linking to structured registries:

**Key metadata fields:**
- `county`, `state`, `zip_codes`
- `resource_type` (e.g., `seasonal_assistance`, `housing`, `utilities`, `senior_services`)
- `source_url`, `file_id`
- `local_resource_id` (links to structured registry when available)

**`gis_wv_benefits` collection:**  
Semantic descriptions of benefits facilities (DHHR offices, assistance centers) with county, ZIP, and spatial metadata. Enables queries like "benefits near Oak Hill" or "Raleigh County assistance offices."

**Community validation:**  
Harmony for Hope's **Community Champions** group provides ground-truth verification. Boone County resident **Crystal Colyer** serves as lead validator, verifying food pantries and resource locations across Boone, Kanawha, and nearby counties. Her fieldwork ensures Ms. Jarvis's answers about Charleston and surrounding communities rest on community-validated data.

---

### 5.4 From Hilbert Space to ChromaDB (and PostgreSQL)

ChromaDB provides concrete realization of the Hilbert-space representation, while PostgreSQL databases (`msjarvis`, `gisdb`) provide structured provenance and spatial primitives.

**Embeddings as vectors**  
The embedding model maps texts and entities into high-dimensional real vectors. ChromaDB stores these with metadata (identifiers, timestamps, geographies) and exposes nearest-neighbor search and filtering.

**Collections as working subspaces**  
Each collection corresponds to an empirically instantiated subset of H_App, grouping vectors by purpose (governance, conversation, resources) or entity type (buildings, blocks, benefits facilities). The `gbim_worldview_entities` collection represents a comprehensive spatial subspace.

**Queries as projections plus database joins**  
Incoming queries are embedded and probe relevant collections, projecting into appropriate subsets of H_App. ChromaDB returns vectors and metadata. Ms. Jarvis then:

1. Uses metadata (`entity_id`, `source_table`) to query PostgreSQL `msjarvis.gbim_beliefs` for belief provenance
2. Uses spatial identifiers to join PostGIS `gisdb.zcta_wv_centroids` for geographic context
3. Combines structured and semantic data for ensemble reasoning

This enables memory to be described both geometrically (Hilbert space projections) and operationally (concrete collection queries + SQL joins).

---

### 5.5 Embedding Model and Dimensionality

Ms. Jarvis uses a **384-dimensional sentence-embedding model** as the primary text embedding channel. All ChromaDB collections are configured for 384-dimensional vectors.

This defines the ambient dimension of H_text for text-based collections and applies uniformly to spatial collections (which embed feature descriptions), benefits collections, and resource documents.

---

### 5.6 Clients, RAG Services, and Deployment Topology

#### 5.6.1 Shared HTTP Service (Production Configuration)

**Verified March 14, 2026:**
- **Host:** `127.0.0.1`
- **Port:** `8002`
- **Instance type:** ChromaDB HTTP server (persistent, host-system process)
- **Storage:** On-disk, host filesystem
```python
import chromadb
client = chromadb.HttpClient(host="127.0.0.1", port=8002)
collection = client.get_collection("gbim_worldview_entities")
print("Total entities:", collection.count())
# Output: Total entities: 5416521
```

Services connect to this shared instance for all semantic memory operations. The canonical server is the authoritative memory store used by text RAG, GIS RAG, Autonomous Learner, and ensemble reasoning.

#### 5.6.2 Active Collections (Verified March 14, 2026)

| Collection | Domain | Status |
|---|---|---|
| `gbim_worldview_entities` | GBIM spatial worldview | ✅ **COMPLETE — 5,416,521 / 5,416,521** |
| `autonomous_learner` | Autonomous learning patterns | ✅ Active (21,160+ items) |
| `psychological_rag` | Psychological safety corpus | ✅ Active (968 items) |
| `spiritual_texts` | Multi-tradition spiritual texts | ✅ Active (23 items) |
| `GBIM_sample_rows` | GBIM test sample | ✅ Active (5,000 items) |
| `geospatialfeatures` | GIS feature embeddings | ✅ Active |
| `msjarvis_docs` | System documentation | ✅ Active |
| `GBIM_Fayette_sample` | Fayette County sample | ✅ Active |
| `GBIM_sample` | General GBIM sample | ✅ Active |
| `msjarvis-smoke` | Smoke test collection | ✅ Active |

#### 5.6.3 PostgreSQL Database Access

**For GBIM belief provenance queries:**
```python
import psycopg2
conn = psycopg2.connect(
    host="localhost",
    port=5433,
    database="msjarvis",
    user="postgres",
    password="postgres"
)
cursor = conn.cursor()
cursor.execute("""
    SELECT belief_id, proposition, belief_state
    FROM gbim_beliefs
    WHERE entity_id = %s
""", (entity_id,))
```

**For PostGIS spatial queries:**
```python
import psycopg2
conn = psycopg2.connect(
    host="localhost",
    port=5433,
    database="gisdb",
    user="postgres",
    password="postgres"
)
cursor = conn.cursor()
cursor.execute("""
    SELECT zip, lat, lon
    FROM zcta_wv_centroids
    WHERE zip = %s
""", ('25880',))
# Result: ('25880', 37.8782, -81.2056) -- Mount Hope
```

---

### 5.7 Integration with GBIM, PostGIS, and RAG

ChromaDB integrates tightly with PostgreSQL databases and RAG services:

**GBIM linkage (msjarvis database)**  
GBIM worldview entities in ChromaDB carry `entity_id` metadata linking to `msjarvis.gbim_beliefs` table. This enables round-trip queries from semantic search results to full belief provenance via PostgreSQL.

The `msjarvis` database stores:
- `gbim_beliefs`: Belief propositions and states
- `gbim_belief_edges`: Relationships between beliefs
- `gbim_belief_evidence`: Evidence chains
- `gbim_worldviews`: Worldview contexts
- `gbim_layer_catalog`: Source layer metadata

**PostGIS integration (gisdb database)**  
Spatial collections include coordinates and identifiers that join to PostGIS tables in `gisdb`. The `zcta_wv_centroids` table (993 rows) provides ZIP code centroids for proximity queries.

Example spatial query flow:
1. User: "hospitals near Mount Hope"
2. ChromaDB: Retrieve entities with semantic similarity to "hospital"
3. PostGIS: Query `gisdb.zcta_wv_centroids` for Mount Hope (25880) centroid
4. Filter: ChromaDB results within 10-mile radius
5. Response: Ranked hospitals with distances

**RAG context building**  
The RAG pipeline queries ChromaDB collections, retrieves entities/documents, then:
1. Uses `entity_id` to query `msjarvis.gbim_beliefs` for provenance
2. Uses spatial metadata to query `gisdb` PostGIS tables
3. Combines semantic embeddings + structured data into context windows
4. Passes enriched context to 21-model ensemble

**Traceability**  
Logs record which ChromaDB collections, entity IDs, PostgreSQL tables, and SQL queries contributed to each response. This enables post-hoc inspection of memory usage and reasoning paths.

---

### 5.8 Query Paths and JSON Structures

#### 5.8.1 ChromaDB Query Request

Typical query structure:
```python
results = collection.query(
    query_texts=["hospitals near Mount Hope"],
    n_results=5,
    where={"county": "Fayette"},
    include=["metadatas", "documents", "distances"]
)
```

Parameters:
- `query_texts`: Strings to embed and search
- `n_results`: Number of nearest neighbors per query
- `where`: Metadata filter (e.g., county, resource_type, ZIP)
- `include`: Fields to return

#### 5.8.2 ChromaDB Response Structure

Responses contain parallel lists:
```python
{
    "ids": [["entity_1", "entity_2", ...]],
    "distances": [[0.234, 0.456, ...]],
    "metadatas": [[
        {"entity_id": "uuid", "county": "Fayette", "source_table": "hospitals"},
        ...
    ]],
    "documents": [["Hospital facility...", ...]]
}
```

Metadata entries include identifiers needed to rejoin PostgreSQL tables, supporting traceable RAG behavior.

---

### 5.9 Operational Considerations

**Reliability and persistence**  
ChromaDB HTTP server runs on host system with persistent on-disk storage. Backups are taken around large ingests. The March 14, 2026 completion of `gbim_worldview_entities` (5.4M entities) should be followed by full backup before further operations.

**Performance and scaling**  
With 5.4M entities in production, index configuration affects query latency. Bulk ingest used batches of 5,400 with attention to index compaction. Chat endpoint latency reflects both model inference and ChromaDB query time.

**Disk usage (CRITICAL)**  
As of March 14, 2026: **96% disk utilization** on development machine (Lenovo Legion 5, Oak Hill WV). This is the highest-priority operational constraint. Disk cleanup required before any further large-scale operations.

**Security and privacy**  
Documented deployment focuses on public/research data: West Virginia GIS layers, public resource guides, internal research. Conversational or personal-memory collections are curated before broader use.

**Schema management**  
Collection names, metadata schemas, embedding configs, and RAG routing rules are versioned. Migrations (e.g., consolidating collections, adding metadata fields) are treated as explicit schema changes with evaluation.

---

### 5.10 Production Deployment Characteristics (March 2026)

**Verified system state (March 14, 2026):**

**ChromaDB:**
- `gbim_worldview_entities`: **5,416,521 / 5,416,521 complete**
- `autonomous_learner`: 21,160+ items (deployed March 14, ChromaDB-Lite)
- Shared HTTP server: `127.0.0.1:8002`

**PostgreSQL Cluster (port 5433):**
- `msjarvis` database: 8 MB, 6 GBIM tables
  - `gbim_beliefs`, `gbim_belief_edges`, `gbim_belief_evidence`
  - `gbim_evidence`, `gbim_layer_catalog`, `gbim_worldviews`
- `gisdb` database: 13 GB, 39 PostGIS tables
  - `zcta_wv_centroids`: 993 West Virginia ZIP centroids
  - Spatial reference tables, infrastructure layers

**RAG Services:**
- Text RAG: Queries general semantic collections
- GIS RAG: Queries `gbim_worldview_entities` and spatial collections
- Both services join ChromaDB results to PostgreSQL for provenance

**Ensemble:**
- 21 models confirmed responding (March 14, 2026)
- Receives enriched context from RAG (ChromaDB + PostgreSQL joins)
- Logs record which collections, entities, and database queries contributed

**Logging:**
- ChromaDB collection access logged
- PostgreSQL query logs capture GBIM/PostGIS joins
- RAG pipeline logs show retrieval-to-response flow

---

### 5.11 Limitations and Future Work

**Completed foundations (March 2026):**
- ✅ `gbim_worldview_entities` ingest complete (5.4M entities)
- ✅ Autonomous Learner deployed and writing to ChromaDB
- ✅ Dual PostgreSQL architecture (msjarvis + gisdb)
- ✅ 993 WV ZCTA centroids in PostGIS
- ✅ Deterministic joins from ChromaDB → PostgreSQL

**Remaining work:**

**Metadata backfill for spatial collection**  
Extended metadata fields (`worldview_id`, `bbox`, `dataset`) need backfill across all 5.4M entities. Backfill pipeline exists but requires execution post-ingest.

**General semantic collection completion**  
Governance, thesis, and resource corpora are under-embedded compared to spatial collections. Full ingestion needed for consistent cross-domain memory.

**Disk space management (URGENT)**  
96% disk utilization blocks further operations. Cleanup and/or migration to larger storage required before next ingest cycle.

**Embedding model dependencies**  
Retrieval quality depends on 384-dimensional model, index parameters, collection design. Upgrades treated as migrations with evaluation.

**Semantic representation limits**  
Vector embeddings struggle with embodied experience, oral history, spiritual traditions. Supplementary strategies needed: graphs, qualitative annotations, community-led tagging.

**Future directions:**
- Run `gbim_worldview_entities` metadata backfill
- Complete resource and governance collection ingestion
- Address 96% disk utilization before next major ingest
- Document all collection schemas and RAG routing in queryable registry
- Add traced examples: ChromaDB retrieval → PostgreSQL provenance → ensemble answer
- Explore hybrid architectures: vectors + graphs + PostgreSQL + participatory workflows
- Implement incremental sync from PostgreSQL instead of full rebuilds
- Fine-tune embeddings on Appalachian place names and local terminology

---

### 5.12 Implementation Status

**Badge: PRODUCTION / COMPLETE (GBIM SPATIAL CORPUS)**

The `gbim_worldview_entities` collection is fully populated at 5,416,521 entities, verified against source data March 14, 2026. Autonomous Learner is deployed and active. ChromaDB semantic memory is exercised by text RAG, GIS RAG, and autonomous learning services behind main chat endpoints.

The dual PostgreSQL architecture (`msjarvis` for belief provenance, `gisdb` for PostGIS spatial queries) complements ChromaDB's semantic layer, providing structured joins and spatial primitives. Together, these systems enable Ms. Jarvis to act as an accountable, place-based steward for West Virginia communities.

*Last updated: 2026-03-14 23:45 EDT by Carrie Kidd, Oak Hill WV*
