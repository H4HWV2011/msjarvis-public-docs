````markdown
## Why this matters for Polymathmatic Geography

This chapter describes how Ms. Jarvis uses ChromaDB as its primary semantic memory layer to support place-based reasoning about West Virginia. The system combines 5,416,521 GBIM worldview entities stored as embeddings in ChromaDB with structured PostgreSQL databases (`msjarvis` for belief relationships, `msjarvisgis` for PostGIS spatial data) to create an inspectable, queryable memory system that grounds AI responses in verified geographic and institutional context.

This architecture supports:

- **P1 – Every where is entangled** by storing GBIM entities, GIS features, and resource documents as searchable embeddings in ChromaDB collections (`gbim_worldview_entities`, `autonomous_learner`, `gis_wv_benefits`) that can be jointly retrieved, filtered by metadata, and linked back to structured PostgreSQL belief tables and PostGIS geometries, treating legal, infrastructural, and social facts about Appalachia as interconnected memory rather than isolated files.

- **P3 – Power has a geometry** by representing institutional relationships and access to services as explicit GBIM belief edges in PostgreSQL, ChromaDB embeddings with geographic metadata, and PostGIS spatial features whose retrieval paths can be logged, inspected, and audited, making it possible to trace how the system traverses memory when answering questions about extraction, obligation, and care.

- **P5 – Design is a geographic act** by treating ChromaDB collection schemas, embedding model choices, metadata conventions, PostgreSQL GBIM table structures, and RAG retrieval rules as deliberate interventions into how West Virginia is represented and searched, ensuring that design decisions about semantic memory are understood as decisions about regional perception and action.

- **P12 – Intelligence with a ZIP code** by binding ChromaDB collections and PostgreSQL spatial tables to West Virginia-specific layers, with GBIM entities carrying county/ZIP metadata and PostGIS tables containing 993 WV ZCTA centroids, so that queries about help, risk, or opportunity are resolved through structures that explicitly encode where people live and which institutions serve them.

- **P16 – Power accountable to place** by making semantic memory, retrieval behavior, and query-to-evidence links explicit and queryable through ChromaDB collection logs, PostgreSQL GBIM belief provenance tables, and PostGIS spatial joins that show which entities, features, and resources contributed to answers about particular communities, instead of hiding choices in opaque model weights.

This chapter belongs to the **Computational Instrument** tier: it defines the production semantic memory substrate—centered on ChromaDB collections and dual PostgreSQL databases (`msjarvis` for beliefs, `msjarvisgis` for spatial data)—that Quantarithmia's reasoning, GBIM's belief structures, spatial queries, and MountainShares governance analysis run on in the live system.

---

## 5. ChromaDB as Semantic Memory

### 5.1 Purpose and Scope

This chapter explains how Ms. Jarvis uses ChromaDB as the primary semantic memory layer for the Hilbert-space representation, GBIM worldview entities, autonomous learning, and resource retrieval. ChromaDB is a vector database that stores high-dimensional embedding vectors with associated metadata and provides efficient similarity search and filtering operations.

In this system, ChromaDB serves as the concrete implementation of long-term, queryable memory for:
- 5,416,521 GBIM worldview entities (geographic features across West Virginia)
- Autonomous learning patterns and research traces — 21,181+ items as of March 18, 2026 (~288/day)
- Community resource documents and benefits guides
- Governance texts and thesis materials
- Psychological safety and spiritual corpora

> **⚠️ CRITICAL API CORRECTION — March 25, 2026:** The ChromaDB `/api/v1/` endpoint path is **DEAD**. The current deployed ChromaDB version returns **HTTP 410 Gone** for all `/api/v1/` requests. All query, collection, and heartbeat calls must use the **v2 API path**:
>
> - Heartbeat: `GET /api/v2/heartbeat`
> - Collection query: `POST /api/v2/tenants/default_tenant/databases/default_database/collections/{collection_name}/query`
> - Collection list: `GET /api/v2/tenants/default_tenant/databases/default_database/collections`
>
> Any code or documentation referencing `/api/v1/` is **incorrect and must be updated**. Two commits merged to `main` on March 25, 2026 update the consciousness bridge and rag-server to v2 endpoints.

> **⚠️ PORT CORRECTION — Confirmed March 22, 2026:** ChromaDB host port is **8002** (`127.0.0.1:8002->8000/tcp`). Container-internal port is 8000. All host-side scripts, health checks, and documentation must use **port 8002**. Container-internal calls (between Docker services) use port 8000. To auto-detect: `docker port jarvis-chroma 8000/tcp`.

<p align="center">
  <img src="https://github.com/user-attachments/assets/5f6bf0d9-91ca-4692-8b1c-95fbceec81b7"
       alt="ChromaDB as Semantic Memory in Ms. Jarvis"
       width="900">
</p>

> *Figure 1 – ChromaDB as Semantic Memory in Ms. Jarvis. Services embed texts and GIS features into ChromaDB collections. The semantic layer links back to structured PostgreSQL databases (msjarvis for GBIM beliefs, msjarvisgis for PostGIS spatial data) enabling traceable, inspectable retrieval for RAG.*

Within the Quantarithmia program, ChromaDB bridges abstract Hilbert-space representation and stored embeddings: vectors in each collection approximate elements of the high-dimensional inner-product space, realized through a specific embedding model and index implementation. Collections like `gbim_worldview_entities` correspond to empirically instantiated subsets of H_App, with stored vectors linking to structured PostgreSQL belief tables and PostGIS geometries.

**Database Architecture (Verified March 22, 2026):**

Ms. Jarvis uses a **dual-database PostgreSQL cluster** plus a dedicated community resources database:

**Database 1: `msjarvis` (8 MB, 6 tables) — port 5433**
- GBIM belief structure and relationships
- Tables: `gbim_beliefs`, `gbim_belief_edges`, `gbim_belief_evidence`, `gbim_evidence`, `gbim_layer_catalog`, `gbim_worldviews`
- Stores belief provenance, epistemic relationships, evidence chains
- 5,416,521 verified GBIM entities; 80 epochs; 206 source layers
- GBIM temporal confidence decay deployed March 15: all entities carry `last_verified`, `confidence_decay`, `needs_verification` metadata
- Small size because bulk entity data lives in ChromaDB

**Database 2: `msjarvisgis` (91 GB, 501 tables) — port 5432**
- PostGIS-enabled spatial database
- Contains `zcta_wv_centroids` (993 West Virginia ZIP centroids)
- Spatial reference tables, geographic boundaries, infrastructure layers
- `gbimbeliefnormalized` table: 5,416,522 rows including 20,593 landowner beliefs
- `mvw_gbim_landowner_spatial` materialized view: 20,593 spatially-indexed landowner beliefs
- Enables geographic queries and spatial joins

**Database 3: `jarvis-local-resources-db` — port 5435**
- Community resources registry keyed by ZIP code and county
- Sourced from Harmony for Hope Community Champions validation
- `building_parcel_county_tax_mv`: 7,354,707 rows (97.17% address coverage)
- `redteam_sessions` and `redteam_feedback` tables (DB: postgres)
- Queried directly by the production pipeline for community resource queries

**ChromaDB (Primary Semantic Storage) — host port 8002, container-internal 8000:**
- **31 confirmed collections** as of March 25, 2026 (up from 13 at March 22 audit)
- **6,665,093 total items** confirmed March 25, 2026
- 5,416,521 GBIM worldview entities in `gbim_worldview_entities` collection
- 21,181+ autonomous learning entries (growing ~288/day)
- ChromaDB v2 API active — `/api/v1/` returns HTTP 410 Gone

---

### 5.2 Role in the Ms. Jarvis Architecture

ChromaDB plays several interlocking roles in the system:

**Semantic memory store (non-spatial)**
Embeddings of texts and artifacts live in domain-specific collections: governance documents, thesis content, autonomous learner outputs, resource guides, research traces. These support semantic retrieval independent of geography.

**Geospatial semantic layer (spatial)**
The unified `gbim_worldview_entities` collection holds 5,416,521 embeddings of West Virginia geospatial features, providing semantic representation of the spatial body. Complementary collections like `gis_wv_benefits` focus on benefits-relevant facilities and programs.

**Retrieval engine for RAG**
Services embed queries and use ChromaDB similarity search with metadata filters to retrieve relevant context. Text RAG handles general semantic queries; GIS RAG (port 8005) uses spatial collections backed by `msjarvisgis`. Retrieved items link back to PostgreSQL for full provenance before being passed to the ensemble. The LM Synthesizer (port 8001, Phase 3.5) pre-processes RAG-retrieved context from all three PostgreSQL databases and ChromaDB before it enters the 21-model ensemble.

**Phase 1.45 — Semantic Community Memory Retrieval**
Before queries reach the LLM ensemble, the main brain performs a dedicated semantic memory retrieval step against the `autonomous_learner` collection:

1. Generates a 384-dimensional embedding of the query using `all-minilm:latest` via `jarvis-ollama:11434/api/embeddings`
2. Queries the `autonomous_learner` ChromaDB collection using the embedding
3. Retrieves the 5 most semantically similar community interaction records
4. Prepends retrieved memories to `enhanced_message` before the LLM ensemble

> **Critical note:** All ChromaDB collections use **384-dimensional vectors**. The required embedding model is `all-minilm:latest`. `nomic-embed-text` produces 768-dimensional vectors and is **incompatible** with all existing production collections. The `jarvis-rag-server` uses `nomic-embed-text` only for its own query-time embedding at the service level — this does not affect the shared production ChromaDB corpus. Any rebuild, migration, or new collection must use `all-minilm:latest`.

**Consciousness pipeline integration — ACTIVE as of March 25, 2026**
`jarvis-consciousness-bridge` (port 8020) now calls ChromaDB using the v2 API (`/api/v2/heartbeat`). WOAH service (`jarvis-woah`, port 7012) is live on `qualia-net`. End-to-end consciousness pipeline confirmed producing persona-consistent Appalachian-voice responses with Hilbert local entity recall. Two commits merged to `main` March 25, 2026.

**Psychological RAG layer**
`psychological-rag` (port 8006) provides the curated psychological corpus (therapy, mindfulness, trauma, depression, anxiety, social support), backed by ChromaDB's `chroma_data` volume (968 items). Confirmed operational.

**Structural backbone for inspectable memory**
Collections and metadata explicitly mirror GBIM structure, PostGIS spatial tables, and resource registries. This enables enumeration, inspection, auditing, and correlation of RAG calls with underlying memory, avoiding hidden internal state.

---

### 5.3 Collections and Data Domains

The primary ChromaDB instance (host port **8002**, container-internal 8000) exposes collections across three families: spatial memory, general semantic memory, and resource-focused collections.

> **March 25, 2026 audit:** **31 collections confirmed active** (up from 13 confirmed at the March 22 audit). Total items: **6,665,093**. The full confirmed list is in §5.6.2.

#### 5.3.1 Production Spatial Collection

**Primary spatial memory (Verified complete March 14, 2026; confirmed March 25, 2026):**

- **Collection name:** `gbim_worldview_entities`
- **Record count:** 5,416,521 (verified via v2 API query)
- **Source:** 200+ West Virginia GIS layers (206 source layers)
- **Coordinate system:** EPSG:26917 (UTM Zone 17N NAD83)
- **Metadata:** Entity IDs, source tables, centroids, counties, ZIPs
- **Embedding dimensions:** 384 (`all-minilm:latest`)
- **Temporal decay:** All 5,416,521 entities carry `last_verified`, `confidence_decay`, `needs_verification` metadata

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

> *Figure 2 – Consolidated spatial memory collection. The unified spatial collection links ChromaDB vectors to PostgreSQL GBIM belief tables (msjarvis database) and PostGIS geometries (msjarvisgis database) for traceable spatial RAG.*

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

**`autonomous_learner` (21,181+ items; growing ~288/day)**
- Deployed March 14, 2026
- Stores autonomous research findings every 5 minutes
- Topics: MountainShares security, Appalachian development, governance systems, AI ethics
- **Queried directly at Phase 1.45** — semantic community memory retrieval prepends top-5 results to `enhanced_message` before every production query reaches the LLM ensemble
- Embedding model: `all-minilm:latest` (384-dim)

**`psychological_rag` (968 items)**
- Mental health and psychological safety resources
- Used for queries about trauma, wellbeing, counseling
- Backed by `psychological-rag` service (port 8006)

**`appalachian_cultural_intelligence` (5 items)**
- Appalachian cultural context corpus — expand needed

**`spiritual_texts` (23 items)** / **`spiritual_rag` (Active)**
- Mother Carrie Protocol spiritual corpus
- Multi-tradition texts with Quaker-Appalachian prioritization

**`msjarvis_docs` (2,348 items — Active as of March 22, 2026)**
- 52 verified WV community resources (50 Kanawha + 2 Fayette)
- 2,296 system docs ingested March 22, 2026

**`GBIM_sample_rows` (5,000 items)**
- GBIM testing and validation sample

**`local_resources` (Active)**
- Default RAG collection for `jarvis-rag-server`
- Target for community resource queries via the RAG server path

**`geospatialfeatures` (0 items — scaffolded, NOT YET INGESTED)**
- Confirmed present at March 25, 2026 audit
- 0 items — pending ingest

**`GBIM_Fayette_sample` (0 items — scaffolded, NOT YET INGESTED)**
- Confirmed present at March 25, 2026 audit
- 0 items — pending ingest

**`fifth_dgm_subconscious` (Active)**
- Subconscious layer for 5th DGM
- Write path is stub — active for reads

**`conversation_history` (Active)**
- Session context storage
- Present and confirmed at March 25 audit
- ⚠️ Not formally wired to the production pipeline — OI-05 open

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

---

### 5.4 From Hilbert Space to ChromaDB (and PostgreSQL)

ChromaDB provides concrete realization of the Hilbert-space representation, while PostgreSQL databases (`msjarvis`, `msjarvisgis`, `jarvis-local-resources-db`) provide structured provenance, spatial primitives, and community resource data.

**Embeddings as vectors**
The embedding model (`all-minilm:latest`, 384-dim) maps texts and entities into high-dimensional real vectors. ChromaDB stores these with metadata (identifiers, timestamps, geographies) and exposes nearest-neighbor search and filtering.

**Collections as working subspaces**
Each collection corresponds to an empirically instantiated subset of H_App, grouping vectors by purpose (governance, conversation, resources) or entity type (buildings, blocks, benefits facilities). The `gbim_worldview_entities` collection represents a comprehensive spatial subspace.

**Queries as projections plus database joins**
Incoming queries are embedded and probe relevant collections, projecting into appropriate subsets of H_App. ChromaDB returns vectors and metadata. Ms. Jarvis then:

1. Uses metadata (`entity_id`, `source_table`) to query PostgreSQL `msjarvis.gbim_beliefs` for belief provenance
2. Uses spatial identifiers to join PostGIS `msjarvisgis` tables for geographic context
3. Queries `jarvis-local-resources-db` (port 5435) for community resource data
4. Applies `confidence_decay` multiplier from GBIM temporal metadata
5. Combines structured and semantic data for ensemble reasoning

This enables memory to be described both geometrically (Hilbert space projections) and operationally (concrete collection queries + SQL joins).

---

### 5.5 Embedding Model and Dimensionality

Ms. Jarvis uses **`all-minilm:latest`** as the required embedding model for all production ChromaDB collections, producing **384-dimensional vectors**.

> **⚠️ Critical architectural note:** All existing ChromaDB collections — including `gbim_worldview_entities` (5,416,521 entities), `autonomous_learner` (21,181+ items), and all resource and semantic collections — use **384-dimensional vectors**. The `nomic-embed-text` model produces **768-dimensional vectors** and is **incompatible** with all existing production collections. The `jarvis-rag-server` uses `nomic-embed-text` only for its own query-time embedding at the service layer — this is a service-internal behavior and does not affect the shared ChromaDB corpus. Any rebuild, migration, or new collection ingestion must use `all-minilm:latest`. This applies to Phase 1.45 semantic retrieval, GIS RAG, text RAG, the autonomous learner, and any future collection creation.

This 384-dimensional embedding space defines the ambient dimension of H_text for all text-based collections and applies uniformly to spatial collections (which embed feature descriptions), benefits collections, and resource documents.

---

### 5.6 Clients, RAG Services, and Deployment Topology

#### 5.6.1 ChromaDB Container Configuration (Production — March 25, 2026)

**Verified and confirmed March 25, 2026:**
- **Container:** `jarvis-chroma`
- **Host port:** `8002` (`127.0.0.1:8002->8000/tcp`)
- **Container-internal port:** `8000`
- **Instance type:** ChromaDB Docker container (`chroma_data` volume)
- **API version:** v2 active — `/api/v1/` returns HTTP 410 Gone
- **Heartbeat endpoint:** `GET /api/v2/heartbeat`
- **Status:** ✅ Production — part of 83-container compose-managed stack
- **Collections confirmed:** 31
- **Total items confirmed:** 6,665,093

> **Port summary:** Host-side scripts and external health checks must use **port 8002**. Docker container-to-container calls use `jarvis-chroma:8000` (or `127.0.0.1:8000` from host). Never reference port 8002 from inside a container — use the Docker network name.

> **To auto-detect host port at runtime:**
```bash
docker port jarvis-chroma 8000/tcp
# Returns: 127.0.0.1:8002
```

**v2 API usage example (heartbeat):**
```python
import httpx

# From host — use port 8002
resp = httpx.get("http://127.0.0.1:8002/api/v2/heartbeat")
assert resp.status_code == 200  # 410 means v1 path was used by mistake
```

**v2 API collection query example:**
```python
import httpx

# From host — use port 8002
url = (
    "http://127.0.0.1:8002"
    "/api/v2/tenants/default_tenant"
    "/databases/default_database"
    "/collections/gbim_worldview_entities/query"
)
resp = httpx.post(url, json={
    "query_embeddings": [embedding_384dim],
    "n_results": 5,
    "include": ["documents", "metadatas", "distances"]
})
```

**Legacy Python client (container-internal only):**
```python
import chromadb
# Container-internal — use port 8000
client = chromadb.HttpClient(host="jarvis-chroma", port=8000)
collection = client.get_collection("gbim_worldview_entities")
print("Total entities:", collection.count())
# Output: Total entities: 5416521
```

#### 5.6.2 Active Collections — March 25, 2026 Audit

> **31 collections confirmed** as of March 25, 2026 audit (up from 13 confirmed at March 22 audit). Total items: **6,665,093**. All collections use **384-dimensional vectors (`all-minilm:latest`)**.

| Collection | Domain | Record Count | Status / Notes |
|---|---|---|---|
| `gbim_worldview_entities` | GBIM spatial worldview | 5,416,521 | ✅ COMPLETE — primary spatial corpus |
| `autonomous_learner` | Autonomous learning patterns | 21,181+ | ✅ Active — Phase 1.45 community memory |
| `psychological_rag` | Psychological safety corpus | 968 | ✅ Active — port 8006 |
| `appalachian_cultural_intelligence` | Appalachian cultural context | 5 | ✅ Active — expand needed |
| `spiritual_texts` | Multi-tradition spiritual corpus | 23 | ✅ Active — Mother Carrie Protocol |
| `spiritual_rag` | Spiritual RAG corpus | Active | ✅ Active |
| `GBIM_sample_rows` | GBIM test sample | 5,000 | ✅ Active |
| `GBIM_sample` | General GBIM sample | Active | ✅ Active |
| `msjarvis-smoke` | Smoke test collection | 1 | ✅ Active |
| `msjarvis_docs` | System documentation + community resources | 2,348 | ✅ Active — 52 WV resources + 2,296 system docs (Mar 22) |
| `local_resources` | Default RAG server collection | Active | ✅ Active — `jarvis-rag-server` default target |
| `gis_wv_benefits` | WV benefits facilities | Active | ✅ Active |
| `ms_jarvis_memory` | Persistent conversation memory | Active | ✅ Active |
| `mountainshares_knowledge` | MountainShares governance | Active | ✅ Active |
| `episodic_index` | Episodic memory index | Active | ✅ Active |
| `conversation_history` | Conversation history | Active | ✅ Active — ⚠️ not formally pipeline-wired (OI-05) |
| `gbim_beliefs_v2` | GBIM beliefs v2 | Active | ⚠️ UNVERIFIED — not confirmed in March 22 CLI output |
| `governance` | WV governance corpus | Active | ✅ Active |
| `thesis` | Theory corpus | Active | ✅ Active |
| `economic_rag` | Economic intelligence | Active | ✅ Active |
| `policy_rag` | Policy corpus | Active | ✅ Active |
| `grants_rag` | Grant corpus | Active | ✅ Active |
| `legal_rag` | Legal corpus | Active | ✅ Active |
| `health_rag` | Health corpus | Active | ✅ Active |
| `commons_rag` | Commons corpus | Active | ✅ Active |
| `news_rag` | News corpus | Active | ✅ Active |
| `meeting_minutes` | Meeting documents | Active | ✅ Active |
| `contracts` | Contracts corpus | Active | ✅ Active |
| `address_points` | WV address points | Active | ✅ Active |
| `safety_rules` | Safety rules | Active | ✅ Active |
| `fifth_dgm_subconscious` | 5th DGM subconscious layer | Active | ✅ Active — write path is stub |
| `conversation_gbim_private` | GBIM private conversation | Active | ✅ Active |
| `conversation_gbim_public` | GBIM public conversation | Active | ✅ Active |
| `geospatialfeatures` | GIS feature embeddings | 0 | ⚠️ Scaffolded — **confirmed empty** — pending ingest |
| `GBIM_Fayette_sample` | Fayette County sample | 0 | ⚠️ Scaffolded — **confirmed empty** — pending ingest |

> **Note on `gbim_beliefs_v2`:** Present in the collection list but item count could not be confirmed during March 22 CLI audit. Do not treat as fully validated until a count query returns a non-zero result.

> **All collections use 384-dimensional vectors (`all-minilm:latest`).** Do not add collections or run ingests using any other embedding model without a full re-embed migration plan.

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

**For PostGIS spatial queries (`msjarvisgis` — port 5432):**
```python
import psycopg2
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="msjarvisgis",
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
    database="postgres",
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

# Step 2: Query autonomous_learner collection via v2 API (from host)
url = (
    "http://127.0.0.1:8002"
    "/api/v2/tenants/default_tenant"
    "/databases/default_database"
    "/collections/autonomous_learner/query"
)
result = httpx.post(url, json={
    "query_embeddings": [embedding],
    "n_results": 5,
    "include": ["documents", "metadatas", "distances"]
}).json()

# Step 3: Prepend to enhanced_message
community_memories = "\n".join(result["documents"][0])
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
As of March 15, 2026, all 5,416,521 GBIM entities carry temporal decay metadata. The `confidence_decay` multiplier is applied during production pipeline processing, attenuating response confidence for answers that rely on entities not recently confirmed. The `needs_verification` flag (currently 100% TRUE at launch baseline) is the trigger for the future POC verification loop (see §5.11).

**PostGIS integration (`msjarvisgis` database — port 5432)**
Spatial collections include coordinates and identifiers that join to PostGIS tables in `msjarvisgis`. The `zcta_wv_centroids` table (993 rows) provides ZIP code centroids for proximity queries. The `gbimbeliefnormalized` table (5,416,522 rows) is the primary GBIM relational store.

Example spatial query flow:
1. User: "hospitals near Mount Hope"
2. ChromaDB (host port 8002): Retrieve entities with semantic similarity to "hospital" via v2 API
3. PostGIS (`msjarvisgis`): Query `zcta_wv_centroids` for Mount Hope (25880) centroid
4. Filter: ChromaDB results within 10-mile radius
5. Response: Ranked hospitals with distances

**Community resources integration (`jarvis-local-resources-db` — port 5435)**
The `jarvis-local-resources-db` is queried directly by the production pipeline for community resource queries. `building_parcel_county_tax_mv` (7,354,707 rows, 97.17% address coverage) provides building-level spatial coverage.

**RAG context building**
The full RAG pipeline queries ChromaDB (host port 8002, v2 API) and all three PostgreSQL databases, then:
1. Phase 1.45: `autonomous_learner` queried via `all-minilm:latest` embedding — top-5 community memories prepended to `enhanced_message`
2. Uses `entity_id` to query `msjarvis.gbim_beliefs` for provenance and decay metadata
3. Uses spatial metadata to query `msjarvisgis` PostGIS tables
4. Queries `jarvis-local-resources-db` for community resource data
5. LM Synthesizer (port 8001, Phase 3.5) calls `jarvis-ollama:11434/api/generate` directly with Ms. Egeria Jarvis persona prompt
6. Judges evaluate the consensus answer
7. Applies `confidence_decay` multiplier

**Consciousness pipeline integration — ACTIVE March 25, 2026**
`jarvis-consciousness-bridge` (port 8020) confirmed active. Chroma health check calls `GET /api/v2/heartbeat` — returns 200. `jarvis-woah` (port 7012) stdlib stub live on `qualia-net`. `jarvis-rag-server` (host:8003 → container:8016) reachable at `/query` endpoint. Embedder v2 query patch written; pending container restart for full RAG integration.

**Psychological RAG path**
`psychological-rag` (port 8006) queries ChromaDB's `psychological_rag` collection (968 items), returning therapeutic guidance, mindfulness resources, and crisis information.

**Traceability**
Logs record which ChromaDB collections, entity IDs, PostgreSQL tables, and SQL queries contributed to each response. This enables post-hoc inspection of memory usage and reasoning paths.

---

### 5.8 Query Paths and JSON Structures

#### 5.8.1 ChromaDB Query Request — v2 API

> **CORRECTION — March 25, 2026:** The `/api/v1/` path is gone. All queries must use the v2 path shown below.

Typical query structure (v2 HTTP API, from host at port 8002):
```python
import httpx

url = (
    "http://127.0.0.1:8002"
    "/api/v2/tenants/default_tenant"
    "/databases/default_database"
    "/collections/gbim_worldview_entities/query"
)
resp = httpx.post(url, json={
    "query_embeddings": [embedding_384dim],
    "n_results": 5,
    "where": {"county": "Fayette"},
    "include": ["metadatas", "documents", "distances"]
})
```

Parameters:
- `query_embeddings`: Pre-computed 384-dim vectors (must use `all-minilm:latest`)
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
ChromaDB runs as Docker container `jarvis-chroma` with the `chroma_data` persistent volume. Host port: **8002**. Container-internal port: **8000**. The container is part of the 83-container fully compose-managed production stack. All `build:` directives have been replaced with `image:` references — no rebuild required on startup.

**API version requirement**
As of March 25, 2026, ChromaDB v2 API is the only active API. All internal services have been patched to use v2 endpoints. Any service still calling `/api/v1/` will receive HTTP 410 Gone. Health checks must call `GET /api/v2/heartbeat`.

**Performance and scaling**
With 5,416,521 entities in production, index configuration affects query latency. Bulk ingest used batches of 5,400 with attention to index compaction. The March 22, 2026 end-to-end benchmark confirmed ~100–107s end-to-end response time, including ChromaDB query time across the RAG retrieval phase.

**Disk usage**
As of March 14, 2026, disk utilization on the development machine (Lenovo Legion 5, Oak Hill WV) was at 96%. The `chroma_data` Docker volume must be monitored for continued growth. Disk cleanup and/or migration to larger storage remains a prerequisite for the next large-scale ingest cycle.

**Security and privacy**
Documented deployment focuses on public/research data: West Virginia GIS layers, public resource guides, internal research. Conversational or personal-memory collections are curated before broader use.

**Schema management**
Collection names, metadata schemas, embedding configs, and RAG routing rules are versioned. The embedding model (`all-minilm:latest`, 384-dim) is a locked dependency — changing it requires a full re-embed of all collections. Migrations are treated as explicit schema changes with evaluation.

---

### 5.10 Production Deployment Characteristics (March 25, 2026)

**Verified system state (March 25, 2026):**

**ChromaDB:**
- Container: `jarvis-chroma` — Running with `chroma_data` Docker volume, fully compose-managed
- Host port: **8002** (`127.0.0.1:8002->8000/tcp`)
- Container-internal port: **8000**
- API: **v2 active** — `/api/v1/` returns HTTP 410 Gone
- Heartbeat: `GET /api/v2/heartbeat` → 200 ✅
- Collections confirmed: **31**
- Total items confirmed: **6,665,093**
- `gbim_worldview_entities`: **5,416,521** (complete)
- `autonomous_learner`: **21,181+** (growing ~288/day; queried at Phase 1.45)
- `psychological_rag`: 968 items (accessible via port 8006)
- `appalachian_cultural_intelligence`: 5 items
- `msjarvis_docs`: **2,348 items** ✅ Active (52 WV resources + 2,296 system docs)
- `local_resources`: Active — default `jarvis-rag-server` collection
- `geospatialfeatures`: **0 items** — scaffolded, pending ingest
- `GBIM_Fayette_sample`: **0 items** — scaffolded, pending ingest
- `gbim_beliefs_v2`: Present — ⚠️ item count UNVERIFIED
- Embedding model: **`all-minilm:latest` (384-dim)** — all collections; `nomic-embed-text` incompatible with production corpus

**PostgreSQL Cluster — Three Databases:**

Port 5433 — `msjarvis` database (8 MB, 6 GBIM tables):
- `gbim_beliefs`, `gbim_belief_edges`, `gbim_belief_evidence`
- `gbim_evidence`, `gbim_layer_catalog`, `gbim_worldviews`
- 5,416,521 verified entities; 80 epochs; 206 source layers
- Temporal decay deployed: all entities carry `last_verified`, `confidence_decay`, `needs_verification`

Port 5432 — `msjarvisgis` database (91 GB, 501 PostGIS tables):
- `zcta_wv_centroids`: 993 West Virginia ZIP centroids
- `gbimbeliefnormalized`: 5,416,522 rows (incl. 20,593 landowner beliefs)
- `mvw_gbim_landowner_spatial`: 20,593 rows (spatially indexed)

Port 5435 — `jarvis-local-resources-db`:
- Community resources registry (ZIP/county-keyed)
- `building_parcel_county_tax_mv`: 7,354,707 rows; 97.17% address coverage
- `redteam_sessions` and `redteam_feedback` tables (DB: postgres)
- Community Champions validated

**RAG Services (March 25, 2026):**
- Phase 1.45 community memory: `all-minilm:latest` embedding → `autonomous_learner` collection (v2 API) → top-5 prepended to `enhanced_message` ✅
- Text RAG / `jarvis-rag-server` (host:8003 → container:8016): ⚠️ PARTIALLY ACTIVE — `/query` endpoint confirmed reachable; embedder v2 query patch written, pending container restart
- GIS RAG (port 8005): Queries `gbim_worldview_entities` and spatial collections; joins to `msjarvisgis`
- `psychological-rag` (port 8006): Queries psychological corpus ✅
- `gbim_query_router` (port 7205): PostgreSQL-native landowner path — NO ChromaDB ✅

**Consciousness pipeline (March 25, 2026):**
- `jarvis-consciousness-bridge` (port 8020): **ACTIVE** — Chroma v2 heartbeat 200, WOAH 200, RAG /query reachable ✅
- `jarvis-woah` (port 7012): **ACTIVE** — stdlib stub, qualia-net ✅
- Pipeline confirmed producing persona-consistent Appalachian-voice responses with Hilbert entity recall ✅

**Preflight gate:**
- **24 PASS / 0 FAIL** — validated March 22, 2026; re-validated March 25, 2026; no regression detected

**Ensemble:**
- **21 active models** / 22 proxies (ports 8201–8222)
- Receives enriched context from RAG (ChromaDB + all three PostgreSQL databases + Phase 1.45 community memories)
- End-to-end benchmark: **~100–107s** (March 22, 2026)

---

### 5.11 Sprint Progress Log

| Sprint | Dates | Items Closed | Status |
|---|---|---|---|
| Initial ChromaDB deployment | March 13–15, 2026 | `gbim_worldview_entities` ingest complete (5,416,521); ChromaDB containerized; `chroma_data` volume created; port confirmed as 8000 (container) | ✅ Complete |
| Autonomous Learner + Phase 1.45 | March 14–18, 2026 | `autonomous_learner` deployed (21,181 items); Phase 1.45 semantic community memory retrieval live; `all-minilm:latest` confirmed as locked embedding model | ✅ Complete |
| Red team hardening sprint | March 21–22, 2026 | Host port confirmed at **8002**; 2,348 system docs + community resources ingested to `msjarvis_docs`; 83 compose services verified; systemd services deployed; public URL live | ✅ Complete |
| Consciousness pipeline + v2 API migration | March 22–25, 2026 | WOAH service (`jarvis-woah` port 7012) fixed — stdlib stub, `qualia-net` confirmed; consciousness bridge patched for Chroma v2 API (all `/api/v1/` removed, `/api/v2/heartbeat` and collection query paths added); RAG server port corrected (host 8003 → container 8016), endpoint corrected (`/direct_rag` → `/query`); gateway `dict.lower()` crash guard added; neuro-master proxy corrected; end-to-end chat **ACTIVE** with Hilbert entity recall and prior session context; 31 collections confirmed (up from 13); total items 6,665,093 confirmed; two commits merged to `main` | ✅ Closed — RAG embedder restart pending |

---

### 5.12 Limitations and Future Work

**Completed foundations (March 25, 2026):**
- ✅ `gbim_worldview_entities` ingest complete (5,416,521 entities)
- ✅ Autonomous Learner deployed, active, and queried at Phase 1.45
- ✅ Three-database PostgreSQL architecture (`msjarvis` port 5433; `msjarvisgis` port 5432; `jarvis-local-resources-db` port 5435)
- ✅ 993 WV ZCTA centroids in PostGIS (`msjarvisgis`)
- ✅ Deterministic joins from ChromaDB → PostgreSQL
- ✅ ChromaDB containerized at host port 8002 / container port 8000 (`chroma_data` volume)
- ✅ `psychological-rag` (port 8006) operational
- ✅ GBIM temporal confidence decay deployed across all 5,416,521 entities
- ✅ `all-minilm:latest` (384-dim) confirmed as the embedding model; `nomic-embed-text` incompatibility documented
- ✅ Phase 1.45 semantic community memory retrieval live in production pipeline
- ✅ 83 containers compose-managed
- ✅ ChromaDB v2 API migration complete — all internal services patched
- ✅ **31 collections confirmed** — 6,665,093 total items
- ✅ Consciousness pipeline **ACTIVE** March 25, 2026
- ✅ `msjarvis_docs` collection active — 2,348 items (52 WV community resources + 2,296 system docs)

**Remaining work:**

**RAG embedder restart — OPEN**
`jarvis-rag-server` embedder v2 Chroma query patch written. Pending container restart to activate. Expected to complete full RAG integration.

**`gbim_beliefs_v2` verification — OPEN**
Present in collection list but item count unverified. Query with `GET .../collections/gbim_beliefs_v2` to confirm count before treating as production data source.

**`conversation_history` pipeline wiring — OI-05 OPEN**
Collection confirmed present. Not formally wired to the production pipeline — retrieval from this collection does not yet influence responses.

**GBIM temporal decay — POC verification loop**
All 5,416,521 GBIM entities are currently flagged `needs_verification=TRUE` (expected at launch). The POC verification loop — where the system autonomously contacts a resource's designated point of contact when `needs_verification=TRUE` and resets `confidence_decay` to 1.0 on confirmation — is not yet automated. Current state: flag-and-attenuate only.

**Community resource data loading — OPEN**
Verified knowledge bases return empty results for Mount Hope queries. Real community resource data must be entered into `jarvis-local-resources-db` by Community Champions before local-specific resource queries will return verified results.

**Metadata backfill for spatial collection**
Extended metadata fields (`worldview_id`, `bbox`, `dataset`) need backfill across all 5,416,521 entities.

**Empty scaffolded collections**
`geospatialfeatures` and `GBIM_Fayette_sample` are confirmed at 0 items. Ingest pipelines must be run before these collections contribute to retrieval.

**Disk space management**
96% disk utilization (as of March 14) blocks further operations. Cleanup and/or migration to larger storage required before the next ingest cycle.

**Embedding model dependencies**
`all-minilm:latest` (384-dim) is a locked dependency for all existing collections. Any upgrade requires a full re-embed of all 5,416,521+ entities and is treated as a major migration with evaluation.

**Future directions:**
- Complete `jarvis-rag-server` embedder restart and confirm full RAG integration
- Verify `gbim_beliefs_v2` item count and add to confirmed inventory
- Wire `conversation_history` collection to production pipeline (OI-05)
- Automate POC verification loop
- Load verified community resource data for Mount Hope and Fayette County
- Run `gbim_worldview_entities` metadata backfill
- Complete `geospatialfeatures` and `GBIM_Fayette_sample` ingestion
- Address disk utilization before next major ingest
- Document all collection schemas and RAG routing in queryable registry
- Explore hybrid architectures: vectors + graphs + PostgreSQL + participatory workflows
- Fine-tune embeddings on Appalachian place names and local terminology

---

### 5.13 Implementation Status

**Badge: PRODUCTION / ACTIVE — Updated March 25, 2026**

The `gbim_worldview_entities` collection is fully populated at 5,416,521 entities, verified against source data March 14, 2026. ChromaDB is fully containerized at **host port 8002** (container-internal 8000) with the `chroma_data` Docker volume, part of a fully compose-managed 83-container stack. **31 collections confirmed active** as of March 25, 2026, with **6,665,093 total items**. The ChromaDB v2 API is the only active API — all internal services have been patched; `/api/v1/` returns HTTP 410 Gone. The `autonomous_learner` collection is queried directly at Phase 1.45 of every production request, prepending community interaction memories to each query before it reaches the 21-model ensemble. The consciousness pipeline is **ACTIVE** as of March 25, 2026, with `jarvis-consciousness-bridge` calling ChromaDB via v2 API, `jarvis-woah` live, and end-to-end chat confirmed producing persona-consistent Appalachian-voice responses. The required embedding model for all production collections is `all-minilm:latest` (384-dim); `nomic-embed-text` is documented as incompatible with the production corpus.

The three-database PostgreSQL architecture (`msjarvis` port 5433 for belief provenance, `msjarvisgis` port 5432 for PostGIS spatial queries + GBIM, `jarvis-local-resources-db` port 5435 for community resources) complements ChromaDB's semantic layer, providing structured joins, spatial primitives, and validated community data. GBIM temporal confidence decay is deployed across all entities, with the `confidence_decay` multiplier applied during production pipeline processing. Together, these systems enable Ms. Jarvis to act as an accountable, place-bound steward for West Virginia communities.

*Last updated: 2026-03-25 (evening) by Carrie Kidd (Mamma Kidd), Mount Hope WV*
*Public URL: https://egeria.mountainshares.us*
````
