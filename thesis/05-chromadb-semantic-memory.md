# 5. ChromaDB as Semantic Memory

## Why This Matters for Polymathmatic Geography

This chapter describes how Ms. Jarvis uses ChromaDB as its primary semantic memory layer to support place-based reasoning about West Virginia. The system combines 5,416,521 GBIM worldview entities stored as embeddings in ChromaDB with structured PostgreSQL databases (msjarvis for belief relationships, msjarvisgis for PostGIS spatial data) to create an inspectable, queryable memory system that grounds AI responses in verified geographic and institutional context.

This architecture supports:

- **P1 – Every where is entangled** by storing GBIM entities, GIS features, and resource documents as searchable embeddings in ChromaDB collections (gbim_worldview_entities, autonomous_learner, gis_wv_benefits) that can be jointly retrieved, filtered by metadata, and linked back to structured PostgreSQL belief tables and PostGIS geometries, treating legal, infrastructural, and social facts about Appalachia as interconnected memory rather than isolated files.
- **P3 – Power has a geometry** by representing institutional relationships and access to services as explicit GBIM belief edges in PostgreSQL, ChromaDB embeddings with geographic metadata, and PostGIS spatial features whose retrieval paths can be logged, inspected, and audited.
- **P5 – Design is a geographic act** by treating ChromaDB collection schemas, embedding model choices, metadata conventions, PostgreSQL GBIM table structures, and RAG retrieval rules as deliberate interventions into how West Virginia is represented and searched.
- **P12 – Intelligence with a ZIP code** by binding ChromaDB collections and PostgreSQL spatial tables to West Virginia-specific layers, with GBIM entities carrying county/ZIP metadata and PostGIS tables containing 993 WV ZCTA centroids.
- **P16 – Power accountable to place** by making semantic memory, retrieval behavior, and query-to-evidence links explicit and queryable through ChromaDB collection logs, PostgreSQL GBIM belief provenance tables, and PostGIS spatial joins.

---

## 5.1 Purpose and Scope

This chapter explains how Ms. Jarvis uses ChromaDB as the primary semantic memory layer for the Hilbert-space representation, GBIM worldview entities, autonomous learning, and resource retrieval. ChromaDB is a vector database that stores high-dimensional embedding vectors with associated metadata and provides efficient similarity search and filtering operations.

In this system, ChromaDB serves as the concrete implementation of long-term, queryable memory for:

- 5,416,521 GBIM worldview entities (geographic features across West Virginia)
- Autonomous learning patterns and research traces — 21,181+ items as of March 18, 2026 (~288/day)
- Community resource documents and benefits guides
- Governance texts and thesis materials
- Psychological safety and spiritual corpora

> **⚠️ CRITICAL API CORRECTION — March 25, 2026:** The ChromaDB `/api/v1/` endpoint path is DEAD. The current deployed ChromaDB version returns HTTP 410 Gone for all `/api/v1/` requests. All query, collection, and heartbeat calls must use the v2 API path:
> - Heartbeat: `GET /api/v2/heartbeat`
> - Collection query: `POST /api/v2/tenants/default_tenant/databases/default_database/collections/{collection_name}/query`
> - Collection list: `GET /api/v2/tenants/default_tenant/databases/default_database/collections`
>
> Any code or documentation referencing `/api/v1/` is incorrect and must be updated.

> **⚠️ PORT CORRECTION — Confirmed March 22, 2026:** ChromaDB host port is **8002** (`127.0.0.1:8002->8000/tcp`). Container-internal port is 8000. All host-side scripts, health checks, and documentation must use port 8002. Container-internal calls use port 8000.

---

## 5.2 Role in the Ms. Jarvis Architecture

ChromaDB plays several interlocking roles in the system:

**Semantic memory store (non-spatial)** — Embeddings of texts and artifacts live in domain-specific collections: governance documents, thesis content, autonomous learner outputs, resource guides, research traces. These support semantic retrieval independent of geography.

**Geospatial semantic layer (spatial)** — The unified gbim_worldview_entities collection holds 5,416,521 embeddings of West Virginia geospatial features, providing semantic representation of the spatial body.

**Retrieval engine for RAG** — Services embed queries and use ChromaDB similarity search with metadata filters to retrieve relevant context. Text RAG handles general semantic queries; GIS RAG (port 8004) uses spatial collections backed by msjarvisgis.

**Phase 1.45 — Semantic Community Memory Retrieval** — Before queries reach the LLM ensemble, the main brain performs a dedicated semantic memory retrieval step against the autonomous_learner collection:

1. Generates a 384-dimensional embedding of the query using all-minilm:latest via jarvis-ollama:11434/api/embeddings
2. Queries the autonomous_learner ChromaDB collection using the embedding
3. Retrieves the 5 most semantically similar community interaction records
4. Prepends retrieved memories to enhanced_message before the LLM ensemble

> **Critical note:** All ChromaDB collections use 384-dimensional vectors. The required embedding model is **all-minilm:latest**. nomic-embed-text produces 768-dimensional vectors and is incompatible with all existing production collections. Any rebuild, migration, or new collection must use all-minilm:latest.

**Consciousness pipeline integration — ACTIVE as of March 25, 2026** — jarvis-consciousness-bridge (port 8020) now calls ChromaDB using the v2 API (`/api/v2/heartbeat`). End-to-end consciousness pipeline confirmed producing persona-consistent Appalachian-voice responses with Hilbert local entity recall.

---

## 5.3 Collections and Data Domains

The primary ChromaDB instance (host port 8002, container-internal 8000) exposes collections across three families: spatial memory, general semantic memory, and resource-focused collections.

> March 25, 2026 audit: **31 collections confirmed active** (up from 13 confirmed at the March 22 audit). Total items: **6,665,093**.

### 5.3.1 Production Spatial Collection

Primary spatial memory (Verified complete March 14, 2026; confirmed March 25, 2026):

| Field | Value |
|---|---|
| Collection name | gbim_worldview_entities |
| Record count | 5,416,521 |
| Source | 206 West Virginia GIS source layers |
| Coordinate system | EPSG:26917 (UTM Zone 17N NAD83) |
| Embedding dimensions | 384 (all-minilm:latest) |
| Temporal decay | all entities carry last_verified, confidence_decay, needs_verification |

Ingest timeline:
- Start: March 13, 2026
- Completion: March 14, 2026, 15:45 EDT
- Duration: ~40 hours
- Processing rate: ~40,000 entities/minute

### 5.3.2 General Semantic Collections

**autonomous_learner** (21,181+ items; growing ~288/day)
- Deployed March 14, 2026
- Stores autonomous research findings every 5 minutes
- Queried directly at Phase 1.45 — top-5 results prepended to enhanced_message before every production query

**psychological_rag** (968 items) — Mental health and psychological safety resources; port 8006

**appalachian_cultural_intelligence** (5 items) — Appalachian cultural context corpus — expand needed

**spiritual_texts** (23 items) / **spiritual_rag** — Mother Carrie Protocol spiritual corpus; multi-tradition with Quaker-Appalachian prioritization

**msjarvis_docs** (2,348 items) — 52 verified WV community resources (50 Kanawha + 2 Fayette) + 2,296 system docs

**local_resources** — Default RAG collection for jarvis-rag-server

**conversation_history** — Session context storage; ⚠️ not formally wired to production pipeline (OI-05 open)

**geospatialfeatures** (0 items) — Scaffolded, pending ingest

**GBIM_Fayette_sample** (0 items) — Scaffolded, pending ingest

### 5.3.3 Resource and Benefits Collections

Key metadata fields:
- county, state, zip_codes
- resource_type (e.g., seasonal_assistance, housing, utilities, senior_services)
- source_url, file_id
- local_resource_id (links to jarvis-local-resources-db on port 5435)

**gis_wv_benefits** — Semantic descriptions of benefits facilities (DHHR offices, assistance centers) with county, ZIP, and spatial metadata. Enables queries like "benefits near Mount Hope" or "Fayette County assistance offices."

Community validation: Harmony for Hope's Community Champions group provides ground-truth verification. Boone County resident Crystal Colyer serves as lead validator, verifying food pantries and resource locations across Boone, Kanawha, and nearby counties.

---

## 5.4 Database Architecture (Verified March 25, 2026)

Ms. Jarvis uses a dual-database PostgreSQL cluster plus a dedicated community resources database. The system runs on a Lenovo Legion 5 development machine located in **Mount Hope, West Virginia**.

**Database 1: msjarvis** (8 MB, 6 tables) — port 5433
- GBIM belief structure and relationships
- Tables: gbim_beliefs, gbim_belief_edges, gbim_belief_evidence, gbim_evidence, gbim_layer_catalog, gbim_worldviews
- 5,416,521 verified GBIM entities; 80 epochs; 206 source layers
- GBIM temporal confidence decay deployed March 15: all entities carry last_verified, confidence_decay, needs_verification metadata

**Database 2: msjarvisgis** (91 GB, 501 tables) — port 5432
- PostGIS-enabled spatial database
- Contains zcta_wv_centroids (993 West Virginia ZIP centroids)
- gbimbeliefnormalized table: 5,416,522 rows including 20,593 landowner beliefs
- mvw_gbim_landowner_spatial materialized view: 20,593 spatially-indexed landowner beliefs

**Database 3: jarvis-local-resources-db** — port 5435
- Community resources registry keyed by ZIP code and county
- Sourced from Harmony for Hope Community Champions validation
- building_parcel_county_tax_mv: 7,354,707 rows (97.17% address coverage)
- redteam_sessions and redteam_feedback tables (DB: postgres)

---

## 5.5 Embedding Model and Dimensionality

Ms. Jarvis uses **all-minilm:latest** as the required embedding model for all production ChromaDB collections, producing **384-dimensional vectors**.

> **⚠️ Critical architectural constraint:** All existing ChromaDB collections — including gbim_worldview_entities (5,416,521 entities), autonomous_learner (21,181+ items), and all resource and semantic collections — use 384-dimensional vectors. The nomic-embed-text model produces 768-dimensional vectors and is **incompatible** with all existing production collections. Any rebuild, migration, or new collection ingestion must use all-minilm:latest. This was confirmed and enforced on March 25, 2026 when all six active service files referencing nomic-embed-text were patched.

---

## 5.6 Clients, RAG Services, and Deployment Topology

### 5.6.1 ChromaDB Container Configuration (Production — March 25, 2026)

| Field | Value |
|---|---|
| Container | jarvis-chroma |
| Host port | 8002 (127.0.0.1:8002->8000/tcp) |
| Container-internal port | 8000 |
| API version | v2 active — /api/v1/ returns HTTP 410 Gone |
| Heartbeat endpoint | GET /api/v2/heartbeat |
| Status | ✅ Production — part of 49-container running stack |
| Collections confirmed | 31 |
| Total items confirmed | 6,665,093 |

Port auto-detection:

```bash
docker port jarvis-chroma 8000/tcp
# Returns: 127.0.0.1:8002
```

v2 API heartbeat example:

```python
import httpx

# From host — use port 8002
resp = httpx.get("http://127.0.0.1:8002/api/v2/heartbeat")
assert resp.status_code == 200  # 410 means v1 path was used by mistake
```

v2 API collection query example:

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
    "include": ["documents", "metadatas", "distances"]
})
```

Legacy Python client (container-internal only):

```python
import chromadb
# Container-internal — use port 8000
client = chromadb.HttpClient(host="jarvis-chroma", port=8000)
collection = client.get_collection("gbim_worldview_entities")
print("Total entities:", collection.count())
# Output: Total entities: 5416521
```

### 5.6.2 Active Collections — March 25, 2026 Audit

31 collections confirmed. Total items: 6,665,093. All collections use 384-dimensional vectors (all-minilm:latest).

| Collection | Domain | Record Count | Status |
|---|---|---|---|
| gbim_worldview_entities | GBIM spatial worldview | 5,416,521 | ✅ COMPLETE — primary spatial corpus |
| autonomous_learner | Autonomous learning patterns | 21,181+ | ✅ Active — Phase 1.45 community memory |
| psychological_rag | Psychological safety corpus | 968 | ✅ Active — port 8006 |
| appalachian_cultural_intelligence | Appalachian cultural context | 5 | ✅ Active — expand needed |
| spiritual_texts | Multi-tradition spiritual corpus | 23 | ✅ Active — Mother Carrie Protocol |
| spiritual_rag | Spiritual RAG corpus | Active | ✅ Active |
| GBIM_sample_rows | GBIM test sample | 5,000 | ✅ Active |
| GBIM_sample | General GBIM sample | Active | ✅ Active |
| msjarvis-smoke | Smoke test collection | 1 | ✅ Active |
| msjarvis_docs | System docs + community resources | 2,348 | ✅ Active |
| local_resources | Default RAG server collection | Active | ✅ Active |
| gis_wv_benefits | WV benefits facilities | Active | ✅ Active |
| ms_jarvis_memory | Persistent conversation memory | Active | ✅ Active |
| mountainshares_knowledge | MountainShares governance | Active | ✅ Active |
| episodic_index | Episodic memory index | Active | ✅ Active |
| conversation_history | Conversation history | Active | ✅ Active — ⚠️ not pipeline-wired (OI-05) |
| gbim_beliefs_v2 | GBIM beliefs v2 | Active | ⚠️ UNVERIFIED — item count not confirmed |
| governance | WV governance corpus | Active | ✅ Active |
| thesis | Theory corpus | Active | ✅ Active |
| economic_rag | Economic intelligence | Active | ✅ Active |
| policy_rag | Policy corpus | Active | ✅ Active |
| grants_rag | Grant corpus | Active | ✅ Active |
| legal_rag | Legal corpus | Active | ✅ Active |
| health_rag | Health corpus | Active | ✅ Active |
| commons_rag | Commons corpus | Active | ✅ Active |
| news_rag | News corpus | Active | ✅ Active |
| meeting_minutes | Meeting documents | Active | ✅ Active |
| contracts | Contracts corpus | Active | ✅ Active |
| address_points | WV address points | Active | ✅ Active |
| safety_rules | Safety rules | Active | ✅ Active |
| fifth_dgm_subconscious | 5th DGM subconscious layer | Active | ✅ Active — write path stub |
| geospatialfeatures | GIS feature embeddings | 0 | ⚠️ Scaffolded — pending ingest |
| GBIM_Fayette_sample | Fayette County sample | 0 | ⚠️ Scaffolded — pending ingest |

### 5.6.3 PostgreSQL Database Access

For GBIM belief provenance queries (msjarvis — port 5433):

```python
import psycopg2
conn = psycopg2.connect(
    host="localhost", port=5433,
    database="msjarvis", user="postgres", password="postgres"
)
cursor = conn.cursor()
cursor.execute("""
    SELECT belief_id, proposition, belief_state,
           confidence_decay, needs_verification
    FROM gbim_beliefs
    WHERE entity_id = %s
""", (entity_id,))
```

For PostGIS spatial queries (msjarvisgis — port 5432):

```python
import psycopg2
conn = psycopg2.connect(
    host="localhost", port=5432,
    database="msjarvisgis", user="postgres", password="postgres"
)
cursor = conn.cursor()
cursor.execute("""
    SELECT zip, lat, lon
    FROM zcta_wv_centroids
    WHERE zip = %s
""", ('25880',))
# Result: ('25880', 37.8782, -81.2056) -- Mount Hope, WV
```

For community resource queries (jarvis-local-resources-db — port 5435):

```python
import psycopg2
conn = psycopg2.connect(
    host="localhost", port=5435,
    database="postgres", user="postgres", password="postgres"
)
cursor = conn.cursor()
cursor.execute("""
    SELECT resource_name, resource_type, address, phone
    FROM community_resources
    WHERE county = %s
""", ('Fayette',))
```

For Phase 1.45 semantic community memory retrieval:

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
community_memories = "\n".join(result["documents"])
enhanced_message = community_memories + "\n\n" + original_message
```

---

## 5.7 Integration with GBIM, PostGIS, and RAG

**GBIM linkage (msjarvis — port 5433)** — GBIM worldview entities in ChromaDB carry entity_id metadata linking to msjarvis.gbim_beliefs. Temporal confidence decay (deployed March 15, 2026) attenuates response confidence for entities not recently confirmed. needs_verification=TRUE is the trigger for the future POC verification loop.

**PostGIS integration (msjarvisgis — port 5432)** — Spatial collections include coordinates and identifiers that join to PostGIS tables. The zcta_wv_centroids table (993 rows) provides ZIP code centroids for proximity queries.

Example spatial query flow:

1. User: "hospitals near Mount Hope"
2. ChromaDB (host port 8002): Retrieve entities with semantic similarity to "hospital" via v2 API
3. PostGIS (msjarvisgis): Query zcta_wv_centroids for Mount Hope (25880) centroid
4. Filter: ChromaDB results within 10-mile radius
5. Response: Ranked hospitals with distances

**Community resources integration (jarvis-local-resources-db — port 5435)** — Queried directly by the production pipeline. building_parcel_county_tax_mv (7,354,707 rows, 97.17% address coverage) provides building-level spatial coverage.

**RAG context building** — The full RAG pipeline:

1. Phase 1.45: autonomous_learner queried via all-minilm:latest — top-5 community memories prepended to enhanced_message
2. Uses entity_id to query msjarvis.gbim_beliefs for provenance and decay metadata
3. Uses spatial metadata to query msjarvisgis PostGIS tables
4. Queries jarvis-local-resources-db for community resource data
5. LM Synthesizer (port 8001, Phase 3.5) pre-processes RAG context before 21-model ensemble
6. Judges evaluate the consensus answer
7. Applies confidence_decay multiplier

---

## 5.8 Query Paths and JSON Structures

### 5.8.1 ChromaDB Query Request — v2 API

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

### 5.8.2 ChromaDB Response Structure

```json
{
    "ids": [["entity_1", "entity_2"]],
    "distances": [[0.234, 0.456]],
    "metadatas": [[
        {
            "entity_id": "uuid",
            "county": "Fayette",
            "source_table": "hospitals",
            "confidence_decay": 0.95,
            "needs_verification": true
        }
    ]],
    "documents": [["Hospital facility description..."]]
}
```

---

## 5.9 Operational Considerations

**Reliability and persistence** — ChromaDB runs as Docker container jarvis-chroma with the chroma_data persistent volume. Part of the 49-container running production stack on the Mount Hope development machine.

**API version requirement** — As of March 25, 2026, ChromaDB v2 API is the only active API. Any service still calling `/api/v1/` will receive HTTP 410 Gone.

**Performance** — With 5,416,521 entities in production, bulk ingest used batches of 5,400 with attention to index compaction. End-to-end benchmark confirmed ~100–107s response time (March 22, 2026).

**Disk usage** — As of March 14, 2026, disk utilization on the development machine (Lenovo Legion 5, Mount Hope, WV) was at 96%. The chroma_data Docker volume must be monitored. Disk cleanup and/or migration to larger storage remains a prerequisite for the next large-scale ingest cycle.

**Schema management** — The embedding model (all-minilm:latest, 384-dim) is a locked dependency. Changing it requires a full re-embed of all collections. Migrations are treated as explicit schema changes.

---

## 5.10 Production Deployment State (March 25, 2026)

**Hardware:** Lenovo Legion 5 — Mount Hope, West Virginia (ZIP 25880)

**ChromaDB:**
- Container: jarvis-chroma — Running with chroma_data Docker volume
- Host port: 8002 (127.0.0.1:8002->8000/tcp)
- API: v2 active — /api/v1/ returns HTTP 410 Gone
- Heartbeat: GET /api/v2/heartbeat → 200 ✅
- Collections confirmed: 31
- Total items confirmed: 6,665,093
- gbim_worldview_entities: 5,416,521 ✅
- autonomous_learner: 21,181+ (growing ~288/day) ✅
- psychological_rag: 968 items ✅
- msjarvis_docs: 2,348 items ✅
- geospatialfeatures: 0 items — pending ingest
- GBIM_Fayette_sample: 0 items — pending ingest
- gbim_beliefs_v2: Present — ⚠️ item count UNVERIFIED
- Embedding model: all-minilm:latest (384-dim) — all collections locked

**PostgreSQL Cluster:**
- Port 5433 — msjarvis (8 MB, 6 GBIM tables) — 5,416,521 entities; temporal decay deployed
- Port 5432 — msjarvisgis (91 GB, 501 PostGIS tables) — 993 WV ZIP centroids; 5,416,522 normalized rows
- Port 5435 — jarvis-local-resources-db — 7,354,707 building rows; Community Champions validated

**RAG Services:**
- Phase 1.45 community memory: all-minilm:latest → autonomous_learner (v2 API) → top-5 prepended ✅
- GIS RAG (port 8004): Confirmed operational March 25, 2026 — returning live WV geodata ✅
- Text RAG / jarvis-rag-server (host:8003 → container:8016): ✅ ACTIVE
- psychological-rag (port 8006): ✅ Active
- jarvis-web-research (port 8008 internal): ✅ Restored March 25, 2026
- jarvis-ingest-api (port 8009): ✅ Restored March 25, 2026
- gbim_query_router (port 7205): PostgreSQL-native landowner path — NO ChromaDB ✅

**Consciousness pipeline:**
- jarvis-consciousness-bridge (port 8020): ACTIVE — Chroma v2 heartbeat 200 ✅
- jarvis-woah: ACTIVE — stdlib stub, qualia-net ✅
- Pipeline confirmed producing persona-consistent Appalachian-voice responses ✅

**Container stack:** 49/49 containers Up — zero Restarting, zero Exited (March 25, 2026 19:33 EDT)

---

## 5.11 Sprint Progress Log

| Sprint | Dates | Items Closed | Status |
|---|---|---|---|
| Initial ChromaDB deployment | March 13–15, 2026 | gbim_worldview_entities ingest complete (5,416,521); ChromaDB containerized; chroma_data volume created | ✅ Complete |
| Autonomous Learner + Phase 1.45 | March 14–18, 2026 | autonomous_learner deployed (21,181 items); Phase 1.45 live; all-minilm:latest confirmed locked | ✅ Complete |
| Red team hardening sprint | March 21–22, 2026 | Host port confirmed at 8002; 2,348 system docs ingested; 83 compose services verified; systemd deployed; public URL live | ✅ Complete |
| Consciousness pipeline + v2 API migration | March 22–25, 2026 | WOAH fixed; consciousness bridge patched for v2 API; RAG server port corrected; 31 collections confirmed; 6,665,093 items confirmed; two commits merged to main | ✅ Complete |
| Embedding model fix + container restoration | March 25, 2026 | All 6 nomic-embed-text references patched to all-minilm:latest; jarvis-gis-rag restored (returning live Fayette County geodata); jarvis-web-research restored from backup; jarvis-ingest-api relaunched with correct uvicorn entrypoint; Dockerfile.gis-rag created; 49/49 containers Up | ✅ Complete — committed 2e8b4b2 |

---

## 5.12 Limitations and Future Work

**Completed foundations (March 25, 2026):**

- ✅ gbim_worldview_entities ingest complete (5,416,521 entities)
- ✅ Autonomous Learner deployed, active, and queried at Phase 1.45
- ✅ Three-database PostgreSQL architecture (ports 5433, 5432, 5435)
- ✅ 993 WV ZCTA centroids in PostGIS
- ✅ ChromaDB containerized at host port 8002 / container port 8000
- ✅ psychological-rag (port 8006) operational
- ✅ GBIM temporal confidence decay deployed across all 5,416,521 entities
- ✅ all-minilm:latest (384-dim) confirmed and enforced; nomic-embed-text incompatibility resolved March 25, 2026
- ✅ Phase 1.45 semantic community memory retrieval live
- ✅ ChromaDB v2 API migration complete
- ✅ 31 collections confirmed — 6,665,093 total items
- ✅ Consciousness pipeline ACTIVE March 25, 2026
- ✅ 49/49 containers Up — zero crash-looping
- ✅ GIS RAG (port 8004) returning live WV geodata
- ✅ jarvis-ingest-api and jarvis-web-research restored

**Remaining work:**

**gbim_beliefs_v2 verification — OPEN** — Present in collection list but item count unverified. Query with GET .../collections/gbim_beliefs_v2 to confirm count before treating as production data source.

**conversation_history pipeline wiring — OI-05 OPEN** — Collection confirmed present. Not formally wired to the production pipeline.

**GBIM temporal decay — POC verification loop** — All 5,416,521 GBIM entities are currently flagged needs_verification=TRUE. The POC verification loop — where the system autonomously contacts a resource's designated point of contact when needs_verification=TRUE and resets confidence_decay to 1.0 on confirmation — is not yet automated.

**Community resource data loading — OPEN** — Verified knowledge bases return empty results for Mount Hope queries. Real community resource data must be entered into jarvis-local-resources-db by Community Champions before local-specific resource queries will return verified results.

**geospatialfeatures and GBIM_Fayette_sample ingestion — OPEN** — Both collections scaffolded at 0 items. Ingest pipeline ready; data loading pending.

**Disk capacity** — At 96% utilization on the Mount Hope development machine, the next large-scale ingest cycle requires either cleanup or migration to larger storage before proceeding.
