## Why this matters for Polymathmatic Geography

This chapter describes how Ms. Jarvis uses ChromaDB as its primary semantic memory layer to support place-based reasoning about West Virginia. The system combines 5,416,521 GBIM worldview entities stored as embeddings in ChromaDB with structured PostgreSQL databases (`msjarvis` for belief relationships, `gisdb` for PostGIS spatial data) to create an inspectable, queryable memory system that grounds AI responses in verified geographic and institutional context.

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
- 5,416,521 GBIM worldview entities (geographic features across West Virginia)
- Autonomous learning patterns and research traces — 21,181 items as of March 18, 2026
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

**Database Architecture (Verified March 18, 2026):**

Ms. Jarvis uses a **dual-database PostgreSQL cluster** on port 5433, plus a dedicated community resources database on port 5435:

**Database 1: `msjarvis` (8 MB, 6 tables) — port 5433**
- GBIM belief structure and relationships
- Tables: `gbim_beliefs`, `gbim_belief_edges`, `gbim_belief_evidence`, `gbim_evidence`, `gbim_layer_catalog`, `gbim_worldviews`
- Stores belief provenance, epistemic relationships, evidence chains
- 5,416,521 verified GBIM entities; 80 epochs; 206 source layers
- GBIM temporal confidence decay deployed March 15: all entities carry `last_verified`, `confidence_decay`, `needs_verification` metadata
- Small size because bulk entity data lives in ChromaDB

**Database 2: `gisdb` (13 GB, 39 tables) — port 5433**
- PostGIS-enabled spatial database
- Contains `zcta_wv_centroids` (993 West Virginia ZIP centroids)
- Spatial reference tables, geographic boundaries, infrastructure layers
- Enables geographic queries and spatial joins

**Database 3: `jarvis-local-resources-db` — port 5435**
- Community resources registry keyed by ZIP code and county
- Sourced from Harmony for Hope Community Champions validation
- Queried directly by the 9-phase production pipeline for community resource queries
- Confirmed operational in the March 15, 2026 end-to-end benchmark (~349.87s)

**ChromaDB (Primary Semantic Storage) — port 8000:**
- 5,416,521 GBIM worldview entities in `gbim_worldview_entities` collection
- 21,181 autonomous learning entries (as of March 18, 2026; growing ~288/day)
- Multiple resource and benefits collections
- Total storage: Substantial vector index (10+ GB persistent volume)
- **Port 8000 restored March 15, 2026** — `chroma_data` Docker volume created; previously crashed due to missing volume mount
- `psychological_rag_domain` service (port 8006) restored simultaneously

> **March 15, 2026 update:** ChromaDB was previously running as a host-system HTTP server on port 8002 (verified March 14). As of March 15, ChromaDB is fully containerized at **port 8000**, backed by the `chroma_data` Docker volume created March 15. All service references to ChromaDB should use port 8000. The `psychological_rag_domain` service (port 8006) is now confirmed operational, having been unavailable prior to the volume restoration.

This separation enables:
- Independent backup/restore strategies
- PostGIS spatial optimization in dedicated database
- Lightweight GBIM belief graph in PostgreSQL
- Bulk semantic search in ChromaDB vector store
- Community resource queries via dedicated port 5435 database

---

### 5.2 Role in the Ms. Jarvis Architecture

ChromaDB plays several interlocking roles in the system:

**Semantic memory store (non-spatial)**
Embeddings of texts and artifacts live in domain-specific collections: governance documents, thesis content, autonomous learner outputs, resource guides, research traces. These support semantic retrieval independent of geography.

**Geospatial semantic layer (spatial)**
The unified `gbim_worldview_entities` collection holds 5,416,521 embeddings of West Virginia geospatial features, providing semantic representation of the spatial body. Complementary collections like `gis_wv_benefits` focus on benefits-relevant facilities and programs.

**Retrieval engine for RAG**
Services embed queries and use ChromaDB similarity search with metadata filters to retrieve relevant context. Text RAG handles general semantic queries; GIS RAG (port 8004) uses spatial collections backed by `gisdb`. Retrieved items link back to PostgreSQL for full provenance before being passed to the ensemble. The LM Synthesizer (port 8001, Phase 3.5 of the 9-phase pipeline) pre-processes RAG-retrieved context from all three PostgreSQL databases and ChromaDB before it enters the 21-model ensemble.

**Phase 1.45 — Semantic Community Memory Retrieval (NEW — March 17, 2026)**
Before queries reach the LLM ensemble, the main brain performs a dedicated semantic memory retrieval step against the `autonomous_learner` collection:

1. Generates a 384-dimensional embedding of the query using `all-minilm:latest` via `jarvis-ollama:11434/api/embeddings`
2. Queries the `autonomous_learner` ChromaDB collection (21,181 records) using the embedding
3. Retrieves the 5 most semantically similar community interaction records
4. Prepends retrieved memories to `enhanced_message` before Phase 1.75

> **Critical note:** All ChromaDB collections use **384-dimensional vectors**. The required embedding model is `all-minilm:latest` (pulled March 17, 2026). `nomic-embed-text` produces 768-dimensional vectors and is **incompatible** with all existing collections. Any rebuild, migration, or new collection must use `all-minilm:latest`.

**Psychological RAG layer**
`psychological_rag_domain` (port 8006) provides the curated psychological corpus (therapy, mindfulness, trauma, depression, anxiety, social support), backed by ChromaDB's `chroma_data` volume. Confirmed operational March 15, 2026; feeds Phase 3 psychology pre-assessment via `jarvis-psychology-services` (port 8019).

**Structural backbone for inspectable memory**
Collections and metadata explicitly mirror GBIM structure, PostGIS spatial tables, and resource registries. This enables enumeration, inspection, auditing, and correlation of RAG calls with underlying memory, avoiding hidden internal state.

This design makes semantic memory inspectable and debuggable: operators can see what's stored, how it's grouped, which collections underpin particular responses, and how retrieval results link to structured PostgreSQL provenance.

---

### 5.3 Collections and Data Domains

The primary ChromaDB instance exposes collections across three families: spatial memory, general semantic memory, and resource-focused collections.

#### 5.3.1 Production Spatial Collection

**Primary spatial memory (Verified complete March 14, 2026; ChromaDB containerized March 15):**

- **Collection name:** `gbim_worldview_entities`
- **Record count:** 5,416,521 (verified via `col.count()`)
- **Source:** 200+ West Virginia GIS layers (206 source layers)
- **Coordinate system:** EPSG:26917 (UTM Zone 17N NAD83)
- **Metadata:** Entity IDs, source tables, centroids, counties, ZIPs
- **Embedding dimensions:** 384 (`all-minilm:latest`)
- **Temporal decay:** All 5,416,521 entities carry `last_verified`, `confidence_decay`, `needs_verification` metadata (deployed March 15); 100% flagged `needs_verification=TRUE` at launch (expected baseline)

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

**`autonomous_learner` (21,181 items as of March 18, 2026; growing ~288/day)**
- Deployed March 14, 2026 (ChromaDB-Lite architecture)
- Stores autonomous research findings every 5 minutes
- Topics: MountainShares security, Appalachian development, governance systems, AI ethics
- **Queried directly at Phase 1.45** — semantic community memory retrieval prepends top-5 results to `enhanced_message` before every production query reaches the LLM ensemble
- Embedding model: `all-minilm:latest` (384-dim)

**`psychological_rag` (968 items)**
- Mental health and psychological safety resources
- Used for queries about trauma, wellbeing, counseling
- Backed by `psychological_rag_domain` service (port 8006), confirmed operational March 15

**`appalachian_cultural_intelligence` (5 items)**
- Appalachian cultural context corpus

**`spiritual_texts` (23 items)**
- Mother Carrie Protocol spiritual corpus
- Multi-tradition texts with Quaker-Appalachian prioritization

**`msjarvis_docs` (system documentation)**
- Technical documentation and architecture guides
- Thesis materials and research notes

**`GBIM_sample_rows` (5,000 items)**
- GBIM testing and validation sample
- Representative cross-section for development

**`GBIM_sample` (3 items), `msjarvis-smoke` (1 item)**
- Smoke test and minimal sample collections

**`GBIM_Fayette_sample` (0 items), `geospatialfeatures` (0 items), `msjarvis_docs` (0 items)**
- Scaffolded collections pending full ingest; present and queryable, currently empty

---

#### 5.3.4 Resource and Benefits Collections

Resource-focused collections store community assistance guides, program descriptions, and benefits information with metadata linking to structured registries:

**Key metadata fields:**
- `county`, `state`, `zip_codes`
- `resource_type` (e.g., `seasonal_assistance`, `housing`, `utilities`, `senior_services`)
- `source_url`, `file_id`
- `local_resource_id` (links to `jarvis-local-resources-db` on port 5435 when available)

**`gis_wv_benefits` collection:**
Semantic descriptions of benefits facilities (DHHR offices, assistance centers) with county, ZIP, and spatial metadata. Enables queries like "benefits near Oak Hill" or "Raleigh County assistance offices."

**Community validation:**
Harmony for Hope's **Community Champions** group provides ground-truth verification. Boone County resident **Crystal Colyer** serves as lead validator, verifying food pantries and resource locations across Boone, Kanawha, and nearby counties. Her fieldwork ensures Ms. Jarvis's answers about Charleston and surrounding communities rest on community-validated data stored in `jarvis-local-resources-db` (port 5435).

> **Known issue — OPEN as of March 18, 2026:** Verified knowledge bases (`gis_rag`, `local_resources`) return empty results for Mount Hope queries. LLMs are generating responses from training data for community resource queries. Factually accurate programs (LIHEAP, WV 2-1-1) pass the BBB. Fabricated organization names are blocked by the ethical filter. Root cause: real community resource data not yet loaded into verified databases. Resolution: field-validated data entry by Community Champions is the next priority.

---

### 5.4 From Hilbert Space to ChromaDB (and PostgreSQL)

ChromaDB provides concrete realization of the Hilbert-space representation, while PostgreSQL databases (`msjarvis`, `gisdb`, `jarvis-local-resources-db`) provide structured provenance, spatial primitives, and community resource data.

**Embeddings as vectors**
The embedding model (`all-minilm:latest`, 384-dim) maps texts and entities into high-dimensional real vectors. ChromaDB stores these with metadata (identifiers, timestamps, geographies) and exposes nearest-neighbor search and filtering.

**Collections as working subspaces**
Each collection corresponds to an empirically instantiated subset of H_App, grouping vectors by purpose (governance, conversation, resources) or entity type (buildings, blocks, benefits facilities). The `gbim_worldview_entities` collection represents a comprehensive spatial subspace.

**Queries as projections plus database joins**
Incoming queries are embedded and probe relevant collections, projecting into appropriate subsets of H_App. ChromaDB returns vectors and metadata. Ms. Jarvis then:

1. Uses metadata (`entity_id`, `source_table`) to query PostgreSQL `msjarvis.gbim_beliefs` for belief provenance
2. Uses spatial identifiers to join PostGIS `gisdb.zcta_wv_centroids` for geographic context
3. Queries `jarvis-local-resources-db` (port 5435) for community resource data
4. Applies `confidence_decay` multiplier from GBIM temporal metadata (Phase 5 of 9-phase pipeline)
5. Combines structured and semantic data for ensemble reasoning

This enables memory to be described both geometrically (Hilbert space projections) and operationally (concrete collection queries + SQL joins).

---

### 5.5 Embedding Model and Dimensionality

Ms. Jarvis uses **`all-minilm:latest`** as the required embedding model, producing **384-dimensional vectors**. This model was pulled March 17, 2026 and confirmed as the active embedding model for all ChromaDB collections.

> **⚠️ Critical architectural note:** All existing ChromaDB collections — including `gbim_worldview_entities` (5,416,521 entities), `autonomous_learner` (21,181 items), and all resource and semantic collections — use **384-dimensional vectors**. The `nomic-embed-text` model produces **768-dimensional vectors** and is **incompatible** with all existing collections. Any service that calls `jarvis-ollama:11434/api/embeddings` must specify `all-minilm:latest`. This applies to Phase 1.45 semantic retrieval, GIS RAG, text RAG, the autonomous learner, and any future collection creation.

Previously, documentation referenced `nomic-embed-text` as the embedding model. That reference is incorrect and has been superseded. All new code, configuration, and documentation must reference `all-minilm:latest` (384-dim).

This 384-dimensional embedding space defines the ambient dimension of H_text for all text-based collections and applies uniformly to spatial collections (which embed feature descriptions), benefits collections, and resource documents.

---

### 5.6 Clients, RAG Services, and Deployment Topology

#### 5.6.1 ChromaDB Container Configuration (Production — March 18, 2026)

**Verified March 15, 2026 (containerized); confirmed March 18, 2026:**
- **Host:** `127.0.0.1`
- **Port:** `8000`
- **Instance type:** ChromaDB Docker container (`chroma_data` volume)
- **Storage:** `chroma_data` Docker volume (created March 15)
- **Status:** ✅ Stable — part of fully compose-managed 79-container stack (Docker Compose v5.1.0)

```python
import chromadb
client = chromadb.HttpClient(host="127.0.0.1", port=8000)
collection = client.get_collection("gbim_worldview_entities")
print("Total entities:", collection.count())
# Output: Total entities: 5416521
```

> **Note:** Prior to March 15, ChromaDB was accessed at port 8002 as a host-system process. The canonical production port is **8000** (containerized with `chroma_data` volume). All service configurations must reference port 8000. Never reference port 8002.

Services connect to this shared instance for all semantic memory operations. The canonical container is the authoritative memory store used by Phase 1.45 community memory retrieval, text RAG, GIS RAG (port 8004), `psychological_rag_domain` (port 8006), the Autonomous Learner (port 8425), and ensemble reasoning.

#### 5.6.2 Active Collections (Verified March 18, 2026)

| Collection | Domain | Record Count | Status |
|---|---|---|---|
| `gbim_worldview_entities` | GBIM spatial worldview | 5,416,521 | ✅ **COMPLETE** |
| `autonomous_learner` | Autonomous learning patterns | 21,181 | ✅ Active — queried at Phase 1.45 |
| `psychological_rag` | Psychological safety corpus | 968 | ✅ Active — port 8006 |
| `appalachian_cultural_intelligence` | Appalachian cultural context | 5 | ✅ Active |
| `spiritual_texts` | Multi-tradition spiritual corpus | 23 | ✅ Active |
| `GBIM_sample_rows` | GBIM test sample | 5,000 | ✅ Active |
| `GBIM_sample` | General GBIM sample | 3 | ✅ Active |
| `msjarvis-smoke` | Smoke test collection | 1 | ✅ Active |
| `geospatialfeatures` | GIS feature embeddings | 0 | ⚠️ Scaffolded — pending ingest |
| `msjarvis_docs` | System documentation | 0 | ⚠️ Scaffolded — pending ingest |
| `GBIM_Fayette_sample` | Fayette County sample | 0 | ⚠️ Scaffolded — pending ingest |
| `gis_wv_benefits` | WV benefits facilities | Active | ✅ Active |
| `ms_jarvis_memory` | Conversation memory | Active | ✅ Active |
| `mountainshares_knowledge` | MountainShares governance | Active | ✅ Active |
| `episodic_index` | Episodic memory index | Active | ✅ Active |
| `conversation_history` | Conversation history | Active | ✅ Active |
| `gbim_beliefs_v2` | GBIM beliefs v2 | Active | ✅ Active |

> **All collections use 384-dimensional vectors (`all-minilm:latest`).** Do not add collections or run ingests using any other embedding model.

#### 5.6.3 PostgreSQL Database Access (Three-Database Architecture)

**For GBIM belief provenance queries (`msjarvis` — port 5433):**
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
    SELECT belief_id, proposition, belief_state,
           confidence_decay, needs_verification
    FROM gbim_beliefs
    WHERE entity_id = %s
""", (entity_id,))
```

**For PostGIS spatial queries (`gisdb` — port 5433):**
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

**For community resource queries (`jarvis-local-resources-db` — port 5435):**
```python
import psycopg2
conn = psycopg2.connect(
    host="localhost",
    port=5435,
    database="jarvis-local-resources-db",
    user="postgres",
    password="postgres"
)
cursor = conn.cursor()
cursor.execute("""
    SELECT resource_name, resource_type, address, phone
    FROM community_resources
    WHERE county = %s
""", ('Fayette',))
```

**For Phase 1.45 semantic community memory retrieval:**
```python
import httpx

# Step 1: Generate 384-dim embedding via all-minilm:latest
response = httpx.post(
    "http://jarvis-ollama:11434/api/embeddings",
    json={"model": "all-minilm:latest", "prompt": user_query}
)
embedding = response.json()["embedding"]  # 384-dimensional vector

# Step 2: Query autonomous_learner collection
import chromadb
client = chromadb.HttpClient(host="127.0.0.1", port=8000)
collection = client.get_collection("autonomous_learner")
results = collection.query(
    query_embeddings=[embedding],
    n_results=5,
    include=["documents", "metadatas", "distances"]
)

# Step 3: Prepend to enhanced_message
community_memories = "\n".join(results["documents"])
enhanced_message = community_memories + "\n\n" + original_message
```

---

### 5.7 Integration with GBIM, PostGIS, and RAG

ChromaDB integrates tightly with all three PostgreSQL databases and RAG services:

**GBIM linkage (`msjarvis` database — port 5433)**
GBIM worldview entities in ChromaDB carry `entity_id` metadata linking to `msjarvis.gbim_beliefs` table. This enables round-trip queries from semantic search results to full belief provenance via PostgreSQL.

The `msjarvis` database stores:
- `gbim_beliefs`: Belief propositions, states, and temporal decay metadata (`last_verified`, `confidence_decay`, `needs_verification`)
- `gbim_belief_edges`: Relationships between beliefs
- `gbim_belief_evidence`: Evidence chains
- `gbim_worldviews`: Worldview contexts
- `gbim_layer_catalog`: Source layer metadata (206 source layers)

**Temporal confidence decay integration**
As of March 15, 2026, all 5,416,521 GBIM entities carry temporal decay metadata. The `confidence_decay` multiplier is applied as Phase 5 of the 9-phase production pipeline, attenuating response confidence for answers that rely on entities not recently confirmed. The `needs_verification` flag (currently 100% TRUE at launch baseline) is the trigger for the future POC verification loop (see §5.11).

**PostGIS integration (`gisdb` database — port 5433)**
Spatial collections include coordinates and identifiers that join to PostGIS tables in `gisdb`. The `zcta_wv_centroids` table (993 rows) provides ZIP code centroids for proximity queries.

Example spatial query flow:
1. User: "hospitals near Mount Hope"
2. ChromaDB (port 8000): Retrieve entities with semantic similarity to "hospital"
3. PostGIS (`gisdb`): Query `zcta_wv_centroids` for Mount Hope (25880) centroid
4. Filter: ChromaDB results within 10-mile radius
5. Response: Ranked hospitals with distances

**Community resources integration (`jarvis-local-resources-db` — port 5435)**
The `jarvis-local-resources-db` is queried directly by the 9-phase production pipeline for community resource queries. In the March 15, 2026 end-to-end benchmark, this database was confirmed as a live retrieval source contributing to the ~349.87s benchmark result. Note: as of March 18, 2026, verified resource data for Mount Hope is not yet loaded — see Known Issues in §5.3.4.

**RAG context building (9-phase pipeline)**
The full RAG pipeline queries ChromaDB (port 8000) and all three PostgreSQL databases, then:
1. Phase 1.45: `autonomous_learner` queried via `all-minilm:latest` embedding — top-5 community memories prepended to `enhanced_message`
2. Uses `entity_id` to query `msjarvis.gbim_beliefs` for provenance and decay metadata
3. Uses spatial metadata to query `gisdb` PostGIS tables
4. Queries `jarvis-local-resources-db` for community resource data
5. LM Synthesizer (port 8001, Phase 3.5) calls `jarvis-ollama:11434/api/generate` directly with `llama3.1:latest` and Ms. Egeria Jarvis persona prompt — delivers final response (Phase 3.75 eliminated)
6. Judges evaluate the consensus answer only — raw_responses dump eliminated (Phase 3; ~60–86s)
7. Applies `confidence_decay` multiplier at Phase 5

**Psychological RAG path**
`psychological_rag_domain` (port 8006) queries ChromaDB's `psychological_rag` collection (968 items), returning therapeutic guidance, mindfulness resources, and crisis information. This feeds `jarvis-psychology-services` (port 8019), which provides Phase 3 pre-assessment for every production request. Both confirmed operational March 15, 2026.

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
- `query_texts`: Strings to embed and search (uses `all-minilm:latest` internally — 384-dim)
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
        {"entity_id": "uuid", "county": "Fayette",
         "source_table": "hospitals",
         "confidence_decay": 0.95,
         "needs_verification": True},
        ...
    ]],
    "documents": [["Hospital facility...", ...]]
}
```

Metadata entries include identifiers needed to rejoin PostgreSQL tables and temporal decay fields, supporting traceable RAG behavior with confidence-aware responses.

---

### 5.9 Operational Considerations

**Reliability and persistence**
ChromaDB runs as a Docker container (port 8000) with the `chroma_data` persistent volume created March 15, 2026. The container is part of the 79-container fully compose-managed production stack (Docker Compose v5.1.0). All `build:` directives have been replaced with `image:` references — no rebuild required on startup.

**Performance and scaling**
With 5,416,521 entities in production, index configuration affects query latency. Bulk ingest used batches of 5,400 with attention to index compaction. The March 15 end-to-end benchmark (~349.87s) includes ChromaDB query time across the RAG retrieval phase. The March 18 benchmark is ~436s reflecting the richer Phase 1.45 community memory retrieval added to the pipeline.

**Disk usage**
As of March 14, 2026, disk utilization on the development machine (Lenovo Legion 5, Oak Hill WV) was at 96%. The `chroma_data` Docker volume creation on March 15 must be monitored for additional disk impact. Disk cleanup and/or migration to larger storage remains a prerequisite for the next large-scale ingest cycle.

**Security and privacy**
Documented deployment focuses on public/research data: West Virginia GIS layers, public resource guides, internal research. Conversational or personal-memory collections are curated before broader use.

**Schema management**
Collection names, metadata schemas, embedding configs, and RAG routing rules are versioned. The embedding model (`all-minilm:latest`, 384-dim) is a locked dependency — changing it requires a full re-embed of all collections. Migrations (e.g., consolidating collections, adding metadata fields, temporal decay field additions) are treated as explicit schema changes with evaluation.

---

### 5.10 Production Deployment Characteristics (March 18, 2026)

**Verified system state (March 18, 2026):**

**ChromaDB (containerized, port 8000):**
- `gbim_worldview_entities`: **5,416,521 / 5,416,521 complete**
- `autonomous_learner`: **21,181 items** (growing ~288/day; queried at Phase 1.45)
- `psychological_rag`: 968 items (accessible via port 8006)
- `appalachian_cultural_intelligence`: 5 items
- Container: Running with `chroma_data` Docker volume, fully compose-managed
- Port: **8000** (containerized; never use port 8002)
- Embedding model: **`all-minilm:latest` (384-dim)** — all collections; `nomic-embed-text` incompatible

**PostgreSQL Cluster — Three Databases:**

Port 5433 — `msjarvis` database (8 MB, 6 GBIM tables):
- `gbim_beliefs`, `gbim_belief_edges`, `gbim_belief_evidence`
- `gbim_evidence`, `gbim_layer_catalog`, `gbim_worldviews`
- 5,416,521 verified entities; 80 epochs; 206 source layers
- Temporal decay deployed: all entities carry `last_verified`, `confidence_decay`, `needs_verification`

Port 5433 — `gisdb` database (13 GB, 39 PostGIS tables):
- `zcta_wv_centroids`: 993 West Virginia ZIP centroids
- Spatial reference tables, infrastructure layers

Port 5435 — `jarvis-local-resources-db`:
- Community resources registry (ZIP/county-keyed)
- Community Champions validated
- Confirmed in March 15 end-to-end benchmark
- ⚠️ Mount Hope resource data not yet loaded — see §5.3.4 Known Issue

**RAG Services:**
- Phase 1.45 community memory: `all-minilm:latest` embedding → `autonomous_learner` collection → top-5 prepended to `enhanced_message`
- Text RAG: Queries general semantic collections (ChromaDB port 8000)
- GIS RAG (port 8004): Queries `gbim_worldview_entities` and spatial collections; joins to `gisdb`
- `psychological_rag_domain` (port 8006): Queries psychological corpus
- LM Synthesizer (port 8001, Phase 3.5): Calls `jarvis-ollama:11434/api/generate` directly with `llama3.1:latest`; Ms. Egeria Jarvis persona injected; Phase 3.75 eliminated

**Ensemble:**
- **21 active models** / 22 proxies (BakLLaVA permanently disabled — CLIP load issues)
- Receives enriched context from RAG (ChromaDB + all three PostgreSQL databases + Phase 1.45 community memories)
- Judges evaluate consensus answer only (raw_responses dump eliminated); ~60–86s
- `confidence_decay` multiplier applied at Phase 5
- End-to-end benchmark: **~436s** (full pipeline with community memory enrichment; 532s baseline before optimization)

**Async job management (new — March 17, 2026):**
- Redis (`jarvis-redis:6379`) backs all async job state (30-min TTL)
- `/chat/async`, `/chat/status/{job_id}`, `/chat/cancel/{job_id}`, `/chat/cancel/all`
- True asyncio task cancellation — 21-LLM pipeline stops immediately mid-run

**Logging:**
- ChromaDB collection access logged
- PostgreSQL query logs capture GBIM/PostGIS/resources joins
- RAG pipeline logs show retrieval-to-response flow
- Temporal decay multipliers recorded per response
- Phase 1.45 retrieval results logged per query

---

### 5.11 Limitations and Future Work

**Completed foundations (March 18, 2026):**
- ✅ `gbim_worldview_entities` ingest complete (5,416,521 entities)
- ✅ Autonomous Learner deployed, active, and queried at Phase 1.45 (21,181 items)
- ✅ Three-database PostgreSQL architecture (`msjarvis` + `gisdb` port 5433; `jarvis-local-resources-db` port 5435)
- ✅ 993 WV ZCTA centroids in PostGIS
- ✅ Deterministic joins from ChromaDB → PostgreSQL
- ✅ ChromaDB containerized at port 8000 (`chroma_data` volume)
- ✅ `psychological_rag_domain` (port 8006) restored and operational
- ✅ GBIM temporal confidence decay deployed across all 5,416,521 entities
- ✅ `all-minilm:latest` (384-dim) confirmed as the embedding model; `nomic-embed-text` incompatibility documented
- ✅ Phase 1.45 semantic community memory retrieval live in production pipeline
- ✅ All 79 containers compose-managed; Docker Compose v5.1.0
- ✅ End-to-end 9-phase pipeline confirmed pulling from all three PostgreSQL databases + ChromaDB

**Remaining work:**

**GBIM temporal decay — POC verification loop**
All 5,416,521 GBIM entities are currently flagged `needs_verification=TRUE` (expected at launch). The POC verification loop — where the system autonomously contacts a resource's designated point of contact when `needs_verification=TRUE` and resets `confidence_decay` to 1.0 on confirmation — is not yet automated. Current state: flag-and-attenuate only. Highest-priority semantic memory work item.

**Community resource data loading — OPEN**
Verified knowledge bases (`gis_rag`, `local_resources`) return empty results for Mount Hope queries. Real community resource data must be entered into `jarvis-local-resources-db` by Community Champions before local-specific resource queries will return verified results.

**Metadata backfill for spatial collection**
Extended metadata fields (`worldview_id`, `bbox`, `dataset`) need backfill across all 5,416,521 entities.

**General semantic collection completion**
`geospatialfeatures`, `msjarvis_docs`, `GBIM_Fayette_sample` are scaffolded but empty. Governance, thesis, and resource corpora are under-embedded compared to spatial collections.

**Disk space management**
96% disk utilization (as of March 14) blocks further operations. Cleanup and/or migration to larger storage required before the next ingest cycle.

**Embedding model dependencies**
`all-minilm:latest` (384-dim) is a locked dependency for all existing collections. Any upgrade requires a full re-embed of all 5,416,521+ entities and is treated as a major migration with evaluation.

**Semantic representation limits**
Vector embeddings struggle with embodied experience, oral history, and spiritual traditions. Supplementary strategies needed: graphs, qualitative annotations, community-led tagging.

**Future directions:**
- Automate POC verification loop (contacts resource POC, resets `confidence_decay` to 1.0 on confirmation)
- Load verified community resource data for Mount Hope and Fayette County into `jarvis-local-resources-db`
- Run `gbim_worldview_entities` metadata backfill (`worldview_id`, `bbox`, `dataset`)
- Complete `geospatialfeatures`, `msjarvis_docs`, and resource collection ingestion
- Address disk utilization before next major ingest
- Document all collection schemas and RAG routing in queryable registry
- Add traced examples: Phase 1.45 retrieval → ChromaDB → PostgreSQL provenance → ensemble answer
- Explore hybrid architectures: vectors + graphs + PostgreSQL + participatory workflows
- Implement incremental sync from PostgreSQL instead of full rebuilds
- Fine-tune embeddings on Appalachian place names and local terminology

---

### 5.12 Implementation Status

**Badge: PRODUCTION / COMPLETE (GBIM SPATIAL CORPUS) — Updated March 18, 2026**

The `gbim_worldview_entities` collection is fully populated at 5,416,521 entities, verified against source data March 14, 2026. ChromaDB is fully containerized at port 8000 with the `chroma_data` Docker volume, part of a fully compose-managed 79-container stack (Docker Compose v5.1.0). The `autonomous_learner` collection (21,181 items) is now queried directly at Phase 1.45 of every production request, prepending community interaction memories to each query before it reaches the 21-model ensemble. The required embedding model for all collections is `all-minilm:latest` (384-dim); `nomic-embed-text` is documented as incompatible.

The three-database PostgreSQL architecture (`msjarvis` for belief provenance, `gisdb` for PostGIS spatial queries, `jarvis-local-resources-db` for community resources) complements ChromaDB's semantic layer, providing structured joins, spatial primitives, and validated community data. GBIM temporal confidence decay is deployed across all entities, with the `confidence_decay` multiplier applied at Phase 5 of every production request. Together, these systems enable Ms. Jarvis to act as an accountable, place-based steward for West Virginia communities.

*Last updated: 2026-03-18 by Carrie Kidd, Mount Hope WV*
