# 5. ChromaDB as Semantic Memory

## Why This Matters for Polymathmatic Geography

This chapter describes how Ms. Jarvis uses ChromaDB as its primary semantic memory layer to support place-based reasoning about West Virginia. The system combines 5,416,521 GBIM worldview entities stored as embeddings in ChromaDB with structured PostgreSQL databases (`msjarvis` for belief relationships, `msjarvisgis` for PostGIS spatial data) to create an inspectable, queryable memory system that grounds AI responses in verified geographic and institutional context.

This architecture supports:

- **P1 – Every where is entangled** by storing GBIM entities, GIS features, and resource documents as searchable embeddings in ChromaDB collections (`gbim_worldview_entities`, `autonomous_learner`, `gis_wv_benefits`) that can be jointly retrieved, filtered by metadata, and linked back to structured PostgreSQL belief tables and PostGIS geometries, treating legal, infrastructural, and social facts about Appalachia as interconnected memory rather than isolated files.
- **P3 – Power has a geometry** by representing institutional relationships and access to services as explicit GBIM belief edges in PostgreSQL, ChromaDB embeddings with geographic metadata, and PostGIS spatial features whose retrieval paths can be logged, inspected, and audited.
- **P5 – Design is a geographic act** by treating ChromaDB collection schemas, embedding model choices, metadata conventions, PostgreSQL GBIM table structures, and RAG retrieval rules as deliberate interventions into how West Virginia is represented and searched.
- **P12 – Intelligence with a ZIP code** by binding ChromaDB collections and PostgreSQL spatial tables to West Virginia-specific layers, with GBIM entities carrying county/ZIP metadata and PostGIS tables containing 993 WV ZCTA centroids.
- **P16 – Power accountable to place** by making semantic memory, retrieval behavior, and query-to-evidence links explicit and queryable through ChromaDB collection logs, PostgreSQL GBIM belief provenance tables, and PostGIS spatial joins.

---

## 5.1 Purpose and Scope

This chapter explains how Ms. Jarvis uses ChromaDB as the primary semantic memory layer for the Hilbert-space representation, GBIM worldview entities, autonomous learning, and resource retrieval. ChromaDB is a vector database that stores high-dimensional embedding vectors with associated metadata and provides efficient similarity search and filtering operations.

In this system, ChromaDB serves as the concrete implementation of long-term, queryable memory for:

- 5,416,521 GBIM worldview entities (geographic features across West Virginia)
- Autonomous learning patterns and research traces — growing ~288/day — **current count per live `docker exec` query as of March 27, 2026**
- Community resource documents and benefits guides
- Governance texts — **643 chunks in `governance_rag`, 306 chunks in `commons_rag`** — confirmed live March 26, 2026
- Psychological safety and spiritual corpora

> **⚠️ CRITICAL API REQUIREMENT — Confirmed March 25, 2026:** The ChromaDB `/api/v1/` endpoint path is DEAD. The current deployed ChromaDB version returns HTTP 410 Gone for all `/api/v1/` requests. All query, collection, and heartbeat calls must use the v2 API path:
> - Heartbeat: `GET /api/v2/heartbeat`
> - Collection query: `POST /api/v2/tenants/default_tenant/databases/default_database/collections/{collection_name}/query`
> - Collection list: `GET /api/v2/tenants/default_tenant/databases/default_database/collections`
>
> Any code or documentation referencing `/api/v1/` is incorrect and must be updated.

> **⚠️ PORT — Confirmed March 22, 2026:** ChromaDB host port is **8002** (`127.0.0.1:8002->8000/tcp`). Container-internal port is 8000. All host-side scripts, health checks, and documentation must use port 8002.

> **⚠️ EMBEDDING MODEL LOCK — Confirmed March 25–26, 2026:** All ChromaDB collections use **`all-minilm:latest`** (384-dimensional, `hnsw:space: cosine`). The `nomic-embed-text` model produces 768-dimensional vectors and is **incompatible** with all existing production collections. All six service files referencing `nomic-embed-text` were patched on March 25, 2026. This constraint is permanent for the current collection architecture.

> **⚠️ CHUNK SIZE CONSTRAINT — Architectural finding confirmed March 26, 2026:** `all-minilm:latest` operates under a **256-token context window**. At ~0.75 tokens/word, this limits meaningful semantic content to **≤100 words per chunk** (20-word overlap). This is not a soft preference — oversized chunks risk truncation and degraded retrieval quality. All ingestion pipelines must enforce this constraint. The `governance_rag` (643 chunks) and `commons_rag` (306 chunks) collections were ingested using this constraint and are correctly structured.

---

## 5.2 Role in the Ms. Jarvis Architecture

ChromaDB plays several interlocking roles in the system:

**Semantic memory store (non-spatial)** — Embeddings of texts and artifacts live in domain-specific collections: governance documents (`governance_rag`: 643 chunks, `commons_rag`: 306 chunks), thesis content, autonomous learner outputs, resource guides, research traces. These support semantic retrieval independent of geography.

**Geospatial semantic layer (spatial)** — The unified `gbim_worldview_entities` collection holds 5,416,521 embeddings of West Virginia geospatial features, providing semantic representation of the spatial body. The `geospatialfeatures` collection now holds **60,000 items** (confirmed March 26, 2026).

**Retrieval engine for RAG** — Services embed queries and use ChromaDB similarity search with metadata filters to retrieve relevant context. Text RAG handles general semantic queries; GIS RAG (port 8004) uses spatial collections backed by `msjarvisgis`.

**Phase 1.45 — Semantic Community Memory Retrieval** — Before queries reach the LLM ensemble, the main brain performs a dedicated semantic memory retrieval step against the `autonomous_learner` collection:

1. Generates a 384-dimensional embedding of the query using `all-minilm:latest` via `jarvis-ollama:11434/api/embeddings`
2. Queries the `autonomous_learner` ChromaDB collection using the embedding
3. Retrieves the 5 most semantically similar community interaction records
4. Prepends retrieved memories to `enhanced_message` before the LLM ensemble

**Consciousness pipeline integration — ACTIVE as of March 25, 2026** — `jarvis-consciousness-bridge` (port 8020) calls ChromaDB using the v2 API (`/api/v2/heartbeat`). End-to-end consciousness pipeline confirmed producing persona-consistent Appalachian-voice responses with Hilbert local entity recall.

---

## 5.3 Collections and Data Domains

The primary ChromaDB instance (host port 8002, container-internal 8000, `hnsw:space: cosine`) exposes collections across three families: spatial memory, general semantic memory, and resource-focused collections.

> **★ March 26, 2026 audit: 31 collections confirmed active. Total items: 6,727,956** (updated from 6,665,093 following completion of the March 26, 2026 RAG corpus sprint — six previously sparse or empty collections now fully populated). **★ March 27, 2026: AaaCPE scraper confirmed live — see Section 5.6.2 and discrepancy note below for updated `appalachian_cultural_intelligence` count.**

### 5.3.1 Production Spatial Collection

Primary spatial memory (verified complete March 14, 2026; confirmed March 25–26, 2026):

| Field | Value |
|---|---|
| Collection name | `gbim_worldview_entities` |
| Record count | **5,416,521** |
| Source | 206 West Virginia GIS source layers |
| Coordinate system | EPSG:26917 (UTM Zone 17N NAD83) |
| Embedding dimensions | 384 (`all-minilm:latest`) |
| Distance function | cosine (`hnsw:space: cosine`) |
| Temporal decay | All entities carry `last_verified`, `confidence_decay`, `needs_verification` |

Ingest timeline:
- Start: March 13, 2026
- Completion: March 14, 2026, 15:45 EDT
- Duration: ~40 hours
- Processing rate: ~40,000 entities/minute

### 5.3.2 General Semantic Collections

**`autonomous_learner`** — growing ~288/day — **current count per live `docker exec` query as of March 27, 2026**
- Deployed March 14, 2026
- Stores autonomous research findings every 5 minutes
- Queried directly at Phase 1.45 — top-5 results prepended to `enhanced_message` before every production query

**`psychological_rag`** (968 items) — Mental health and psychological safety resources; port 8006

**`appalachian_cultural_intelligence`** — ⚠️ **DISCREPANCY — REQUIRES RESOLUTION before committing Chapter 5.**
- Chapter 5 (this file, March 26, 2026 sprint): **820 items** — OI-14 CLOSED March 26, 2026 (was: 5 items)
- Chapter 30 (AaaCPE chapter) and March 27, 2026 AaaCPE scraper deployment: **65 documents** in `appalachian_cultural_intelligence` — from `jarvis-aaacpe-scraper` (port 8033), 39 sources, `total_runs: 1`
- **Most likely resolution:** If the `appalachian_cultural_intelligence` Docker volume was reset during the container rebuild that deployed `jarvis-aaacpe-rag` and `jarvis-aaacpe-scraper`, the correct current count is **65** (first scrape run only). If the volume persisted from the March 26, 2026 sprint ingest (820 items), the scraper would have added ~55 documents → **875**. The 10→65 delta described in Ch 30 suggests the volume was reset and the scraper populated from scratch.
- **Required action before commit:** `curl http://localhost:8032/` to confirm `jarvis-aaacpe-rag` document count, and run ChromaDB v2 API collection count for `appalachian_cultural_intelligence`. Update this entry with the confirmed live count.
- Current table entry: **see §5.6.2 — flagged row**

**`spiritual_texts`** — ★ **19,338 items** — Mother Carrie Protocol multi-tradition spiritual corpus with Quaker-Appalachian prioritization — **CONFIRMED LIVE March 26, 2026** (was: 23 items; OI-15 CLOSED)

**`msjarvis_docs`** (2,348 items) — 52 verified WV community resources (50 Kanawha + 2 Fayette) + 2,296 system docs

**`local_resources`** — Default RAG collection for `jarvis-rag-server`

**`conversation_history`** — Session context storage; ⚠️ not formally wired to production pipeline (OI-05 open)

**`geospatialfeatures`** — ★ **60,000 items** — **CONFIRMED LIVE March 26, 2026** (was: 0 items; OI-12 CLOSED)

**`GBIM_Fayette_sample`** — ★ **1,535 items** — **CONFIRMED LIVE March 26, 2026** (was: 0 items; OI-13 CLOSED)

### 5.3.3 Governance and Thesis Collections — ★ UPDATED March 26, 2026

**`governance_rag`** — ★ **643 chunks** — **CONFIRMED LIVE March 26, 2026** (was: missing/empty)

Full ingested corpus:
- MountainShares DAO Charter
- Terms of Use
- Program Rules
- Parameter Tables
- Phase 0 Specification (invite-only beta)
- Phase 0 Audit Template
- Phase 1–3 Specifications
- KPI Specification
- Safety Champion Protocol
- Funder Overview
- US Constitution (97 chunks, Project Gutenberg pg5.txt)

Semantic retrieval verified March 26, 2026 — see Section 5.13 (smoke test results).

**`commons_rag`** — ★ **306 chunks** — **CONFIRMED LIVE March 26, 2026** (was: missing/empty)

Full Commons governance and gamification corpus ingested. Semantic retrieval verified March 26, 2026.

**`governance`** — WV governance texts (Active)

**`thesis`** — Theoretical framework corpus (Active)

**`mountainshares_knowledge`** — MountainShares DAO economics (Active)

### 5.3.4 Resource and Benefits Collections

Key metadata fields:
- `county`, `state`, `zip_codes`
- `resource_type` (e.g., `seasonal_assistance`, `housing`, `utilities`, `senior_services`)
- `source_url`, `file_id`
- `local_resource_id` (links to `jarvis-local-resources-db` on port 5435)

**`gis_wv_benefits`** — Semantic descriptions of benefits facilities (DHHR offices, assistance centers) with county, ZIP, and spatial metadata. Enables queries like "benefits near Mount Hope" or "Fayette County assistance offices."

Community validation: Harmony for Hope's Community Champions group provides ground-truth verification. Boone County resident Crystal Colyer serves as lead validator, verifying food pantries and resource locations across Boone, Kanawha, and nearby counties.

---

## 5.4 Database Architecture (Verified March 25–26, 2026)

Ms. Jarvis uses a dual-database PostgreSQL cluster plus a dedicated community resources database. The system runs on a Lenovo Legion 5 development machine located in **Mount Hope, West Virginia** (ZIP 25880).

**Database 1: `msjarvis`** (8 MB, 6 tables) — port 5433
- GBIM belief structure and relationships
- Tables: `gbim_beliefs`, `gbim_belief_edges`, `gbim_belief_evidence`, `gbim_evidence`, `gbim_layer_catalog`, `gbim_worldviews`
- 5,416,521 verified GBIM entities; 80 epochs; 206 source layers
- GBIM temporal confidence decay deployed March 15: all entities carry `last_verified`, `confidence_decay`, `needs_verification` metadata

**Database 2: `msjarvisgis`** (91 GB, 501 tables) — port 5432
- PostGIS-enabled spatial database
- Contains `zcta_wv_centroids` (993 West Virginia ZIP centroids)
- `gbimbeliefnormalized` table: 5,416,522 rows including 20,593 landowner beliefs
- `mvw_gbim_landowner_spatial` materialized view: 20,593 spatially-indexed landowner beliefs

**Database 3: `jarvis-local-resources-db`** — port 5435
- Community resources registry keyed by ZIP code and county
- Sourced from Harmony for Hope Community Champions validation
- `building_parcel_county_tax_mv`: 7,354,707 rows (97.17% address coverage)
- `redteam_sessions` and `redteam_feedback` tables (DB: postgres)

---

## 5.5 Embedding Model and Dimensionality — ★ CONFIRMED LIVE March 26, 2026

Ms. Jarvis uses **`all-minilm:latest`** as the required and confirmed live embedding model for all production ChromaDB collections, producing **384-dimensional vectors** with `hnsw:space: cosine` distance.

> **⚠️ Critical architectural constraint — enforced:** All existing ChromaDB collections — including `gbim_worldview_entities` (5,416,521 entities), `autonomous_learner` (growing ~288/day), `governance_rag` (643 chunks), `commons_rag` (306 chunks), and all other production collections — use 384-dimensional vectors. The `nomic-embed-text` model produces 768-dimensional vectors and is **incompatible** with all existing production collections. Any rebuild, migration, or new collection ingestion must use `all-minilm:latest`. Confirmed and enforced March 25, 2026 when all six active service files referencing `nomic-embed-text` were patched.

**Confirmed embedding API call pattern:**

```python
import httpx

# Single-string prompt — /api/embeddings endpoint
response = httpx.post(
    "http://jarvis-ollama:11434/api/embeddings",
    json={"model": "all-minilm:latest", "prompt": "Fayette County assistance programs"}
)
embedding = response.json()["embedding"]
assert len(embedding) == 384  # confirmed production dimension
```

> **⚠️ API shape:** The `/api/embeddings` endpoint accepts a single string in the `"prompt"` field, not a list. Scripts that pass a list will receive an error. This is distinct from the `/api/embed` batch endpoint. Use `"prompt"` (single string) for all production collection queries.

**Chunk size constraint (confirmed architectural finding, March 26, 2026):**

| Parameter | Value |
|---|---|
| Model context window | 256 tokens |
| Tokens per word (approximate) | ~0.75 |
| Maximum words per chunk | **100 words** |
| Overlap | 20 words |
| Impact | Chunks exceeding ~100 words risk truncation and degraded cosine similarity |
| Affected collections | ALL — this is a model-level constraint, not collection-level |
| Resolution | None — permanent for `all-minilm:latest`; changing models requires full collection rebuilds |

All current governance and RAG collections were ingested using the 100-word/20-word-overlap chunking rule and are correctly structured.

---

## 5.6 Clients, RAG Services, and Deployment Topology

### 5.6.1 ChromaDB Container Configuration (Production — ★ March 27, 2026)

| Field | Value |
|---|---|
| Container | `jarvis-chroma` |
| Host port | **8002** (`127.0.0.1:8002->8000/tcp`) |
| Container-internal port | 8000 |
| Distance function | `hnsw:space: cosine` |
| API version | v2 active — `/api/v1/` returns HTTP 410 Gone |
| Heartbeat endpoint | `GET /api/v2/heartbeat` |
| Status | ✅ Production — part of **96-container running stack** |
| Collections confirmed | 31 (verify current count — AaaCPE added 2 containers March 27, 2026; collection count may have changed) |
| Total items (March 27, 2026) | **6,727,956 + AaaCPE delta** ⚠️ — base count 6,727,956 (March 26); add AaaCPE corpus net new documents. If `appalachian_cultural_intelligence` was reset and repopulated with 65 docs (from 820), net change is −755 + 65 = −690 → 6,727,266. If volume persisted and scraper added 55 new docs, net change is +55 → 6,728,011. **Confirm live count per `docker exec` query before committing.** |

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

### 5.6.2 Active Collections — ★ UPDATED March 27, 2026

31 collections confirmed as of March 26, 2026 — verify current count after AaaCPE deployment March 27, 2026. All collections use 384-dimensional vectors (`all-minilm:latest`, `hnsw:space: cosine`).

> ⚠️ **`appalachian_cultural_intelligence` discrepancy — CRITICAL — must resolve before committing Chapter 5.**
>
> - March 26, 2026 sprint (OI-14): 820 items confirmed live (was: 5 items)
> - March 27, 2026 AaaCPE deployment (`jarvis-aaacpe-scraper`, port 8033): 65 documents reported in `appalachian_cultural_intelligence`, 39 sources, `total_runs: 1`
>
> **If the Docker volume for `appalachian_cultural_intelligence` was reset during the AaaCPE container build**, the 820-item corpus was wiped and the scraper populated 65 documents on its first run. This is the most likely scenario given the 10→65 delta described in Chapter 30 (implying a near-empty starting state).
>
> **If the volume persisted**, the scraper added ~55 net-new documents → current count should be ~875.
>
> **Required action:** `curl http://localhost:8032/` to confirm `jarvis-aaacpe-rag` document count. Then run ChromaDB v2 API collection list/count for `appalachian_cultural_intelligence`. Update row below with confirmed count before committing Chapter 5.

| Collection | Domain | Record Count | Status |
|---|---|---|---|
| `gbim_worldview_entities` | GBIM spatial worldview | **5,416,521** | ✅ COMPLETE — primary spatial corpus |
| `autonomous_learner` | Autonomous learning patterns | growing ~288/day ★ | ✅ Active — Phase 1.45 community memory — **update count per live docker query** |
| `psychological_rag` | Psychological safety corpus | 968 | ✅ Active — port 8006 |
| `appalachian_cultural_intelligence` | Appalachian cultural context + AaaCPE | ⚠️ **65 or 820 or 875** | ⚠️ **DISCREPANCY — see note above.** March 26 sprint: 820 (OI-14 CLOSED). March 27 AaaCPE scraper: 65 docs reported. Volume reset status unknown. **Confirm live count before committing.** |
| `spiritual_texts` | Multi-tradition spiritual corpus | ★ **19,338** | ✅ COMPLETE — OI-15 CLOSED March 26 (was: 23) |
| `spiritual_rag` | Spiritual RAG corpus | Active | ✅ Active |
| `governance_rag` | MountainShares DAO + US Constitution | ★ **643 chunks** | ✅ COMPLETE — OI-16 CLOSED March 26 (was: missing) |
| `commons_rag` | Commons governance + gamification | ★ **306 chunks** | ✅ COMPLETE — OI-17 CLOSED March 26 (was: missing) |
| `GBIM_sample_rows` | GBIM test sample | 5,000 | ✅ Active |
| `GBIM_sample` | General GBIM sample | Active | ✅ Active |
| `msjarvis-smoke` | Smoke test collection | 1 | ✅ Active |
| `msjarvis_docs` | System docs + community resources | 2,348 | ✅ Active |
| `local_resources` | Default RAG server collection | Active | ✅ Active |
| `gis_wv_benefits` | WV benefits facilities | Active | ✅ Active |
| `ms_jarvis_memory` | Persistent conversation memory | Active | ✅ Active |
| `mountainshares_knowledge` | MountainShares governance | Active | ✅ Active |
| `episodic_index` | Episodic memory index | Active | ✅ Active |
| `conversation_history` | Conversation history | Active | ✅ Active — ⚠️ not pipeline-wired (OI-05) |
| `gbim_beliefs_v2` | GBIM beliefs v2 | Active | ⚠️ Item count not confirmed |
| `governance` | WV governance corpus | Active | ✅ Active |
| `thesis` | Theory corpus | Active | ✅ Active |
| `economic_rag` | Economic intelligence | Active | ✅ Active |
| `policy_rag` | Policy corpus | Active | ✅ Active |
| `grants_rag` | Grant corpus | Active | ✅ Active |
| `legal_rag` | Legal corpus | Active | ✅ Active |
| `health_rag` | Health corpus | Active | ✅ Active |
| `news_rag` | News corpus | Active | ✅ Active |
| `meeting_minutes` | Meeting documents | Active | ✅ Active |
| `contracts` | Contracts corpus | Active | ✅ Active |
| `address_points` | WV address points | Active | ✅ Active |
| `safety_rules` | Safety rules | Active | ✅ Active |
| `fifth_dgm_subconscious` | 5th DGM subconscious layer | Active | ✅ Active — write path stub |
| `geospatialfeatures` | GIS feature embeddings | ★ **60,000** | ✅ COMPLETE — OI-12 CLOSED March 26 (was: 0) |
| `GBIM_Fayette_sample` | Fayette County sample | ★ **1,535** | ✅ COMPLETE — OI-13 CLOSED March 26 (was: 0) |

### 5.6.3 PostgreSQL Database Access

For GBIM belief provenance queries (`msjarvis` — port 5433):

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

For PostGIS spatial queries (`msjarvisgis` — port 5432):

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

For community resource queries (`jarvis-local-resources-db` — port 5435):

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
# NOTE: single-string "prompt" field — not a list
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

**GBIM linkage (`msjarvis` — port 5433)** — GBIM worldview entities in ChromaDB carry `entity_id` metadata linking to `msjarvis.gbim_beliefs`. Temporal confidence decay (deployed March 15, 2026) attenuates response confidence for entities not recently confirmed. `needs_verification=TRUE` is the trigger for the future POC verification loop.

**PostGIS integration (`msjarvisgis` — port 5432)** — Spatial collections include coordinates and identifiers that join to PostGIS tables. The `zcta_wv_centroids` table (993 rows) provides ZIP code centroids for proximity queries.

Example spatial query flow:

1. User: "hospitals near Mount Hope"
2. ChromaDB (host port 8002): Retrieve entities with semantic similarity to "hospital" via v2 API, `hnsw:space: cosine`
3. PostGIS (`msjarvisgis`): Query `zcta_wv_centroids` for Mount Hope (25880) centroid
4. Filter: ChromaDB results within 10-mile radius
5. Response: Ranked hospitals with distances

**Community resources integration (`jarvis-local-resources-db` — port 5435)** — Queried directly by the production pipeline. `building_parcel_county_tax_mv` (7,354,707 rows, 97.17% address coverage) provides building-level spatial coverage.

**RAG context building** — The full RAG pipeline:

1. Phase 1.45: `autonomous_learner` queried via `all-minilm:latest` — top-5 community memories prepended to `enhanced_message`
2. Uses `entity_id` to query `msjarvis.gbim_beliefs` for provenance and decay metadata
3. Uses spatial metadata to query `msjarvisgis` PostGIS tables
4. Queries `jarvis-local-resources-db` for community resource data
5. LM Synthesizer (port 8001, Phase 3.5) pre-processes RAG context before 21-model ensemble
6. Judges evaluate the consensus answer
7. Applies `confidence_decay` multiplier

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

**Reliability and persistence** — ChromaDB runs as Docker container `jarvis-chroma` with the `chroma_data` persistent volume. Part of the **96-container running production stack** on the Mount Hope development machine as of March 27, 2026.

**API version requirement** — As of March 25, 2026, ChromaDB v2 API is the only active API. Any service still calling `/api/v1/` will receive HTTP 410 Gone.

**Performance** — With 5,416,521 entities in production, bulk ingest used batches of 5,400 with attention to index compaction. End-to-end benchmark confirmed ~100–107s response time (March 22, 2026). `hnsw:space: cosine` is the confirmed distance function for all collections.

**Disk usage** — At 96% utilization on the Mount Hope development machine (Lenovo Legion 5), the `chroma_data` Docker volume must be monitored. Disk cleanup and/or migration to larger storage remains a prerequisite for the next large-scale ingest cycle.

**Schema management** — The embedding model (`all-minilm:latest`, 384-dim, `hnsw:space: cosine`) is a locked dependency. Changing it requires a full re-embed of all collections. The 100-word chunk constraint is a fixed schema parameter for all collections. Migrations are treated as explicit schema changes.

---

## 5.10 Production Deployment State — ★ UPDATED March 27, 2026

**Hardware:** Lenovo Legion 5 — Mount Hope, West Virginia (ZIP 25880)

**ChromaDB:**
- Container: `jarvis-chroma` — Running with `chroma_data` Docker volume
- Host port: **8002** (`127.0.0.1:8002->8000/tcp`)
- Container-internal port: 8000
- Distance function: `hnsw:space: cosine`
- API: v2 active — `/api/v1/` returns HTTP 410 Gone
- Heartbeat: `GET /api/v2/heartbeat` → 200 ✅
- Collections confirmed: 31 (verify after March 27, 2026 AaaCPE deployment)
- Total items (March 27, 2026): **confirm per live docker query** — base 6,727,956 (March 26) ± AaaCPE delta
- `gbim_worldview_entities`: 5,416,521 ✅
- `autonomous_learner`: growing ~288/day — **update count per live docker query** ✅
- `psychological_rag`: 968 items ✅
- `msjarvis_docs`: 2,348 items ✅
- `governance_rag`: ★ **643 chunks** ✅ (was: missing)
- `commons_rag`: ★ **306 chunks** ✅ (was: missing)
- `appalachian_cultural_intelligence`: ⚠️ **65 or 820 or 875** — confirm live count (see §5.6.2 discrepancy note)
- `spiritual_texts`: ★ **19,338 items** ✅ (was: 23)
- `geospatialfeatures`: ★ **60,000 items** ✅ (was: 0)
- `GBIM_Fayette_sample`: ★ **1,535 items** ✅ (was: 0)
- `gbim_beliefs_v2`: Present — ⚠️ item count not confirmed
- Embedding model: `all-minilm:latest` (384-dim, cosine) — all collections locked

**PostgreSQL Cluster:**
- Port 5433 — `msjarvis` (8 MB, 6 GBIM tables) — 5,416,521 entities; temporal decay deployed
- Port 5432 — `msjarvisgis` (91 GB, 501 PostGIS tables) — 993 WV ZIP centroids; 5,416,522 normalized rows; 20,593 landowner beliefs
- Port 5435 — `jarvis-local-resources-db` — 7,354,707 building rows; Community Champions validated

**RAG Services:**
- Phase 1.45 community memory: `all-minilm:latest` → `autonomous_learner` (v2 API) → top-5 prepended ✅
- GIS RAG (port 8004): Confirmed operational March 25, 2026 ✅
- Text RAG / `jarvis-rag-server` (host:8003 → container:8016): ✅ ACTIVE
- `psychological-rag` (port 8006): ✅ Active
- `jarvis-web-research` (port 8008 internal): ✅ Restored March 25, 2026
- `jarvis-ingest-api` (port 8009): ✅ Restored March 25, 2026
- `gbim_query_router` (port 7205): PostgreSQL-native landowner path — NO ChromaDB ✅
- `jarvis-aaacpe-rag` (host:8032): ✅ **Built and running March 27, 2026** — 65 documents (confirm current count via `curl http://localhost:8032/`), 39 sources scraped, `total_runs: 1`
- `jarvis-aaacpe-scraper` (host:8033): ✅ **Built and running March 27, 2026** — first automated scrape run confirmed on startup; 39 sources, `total_runs: 1`

**Consciousness pipeline:**
- `jarvis-consciousness-bridge` (port 8020): ACTIVE — Chroma v2 heartbeat 200 ✅
- `jarvis-woah`: ACTIVE — stdlib stub, qualia-net ✅
- Pipeline confirmed producing persona-consistent Appalachian-voice responses ✅

**Container stack:** **96/96 containers Up — zero Restarting, zero Exited — last verified March 27, 2026** (both `jarvis-aaacpe-rag` and `jarvis-aaacpe-scraper` added to stack March 27, 2026)

---

## 5.11 Sprint Progress Log

| Sprint | Dates | Items Closed | Status |
|---|---|---|---|
| Initial ChromaDB deployment | March 13–15, 2026 | `gbim_worldview_entities` ingest complete (5,416,521); ChromaDB containerized; `chroma_data` volume created | ✅ Complete |
| Autonomous Learner + Phase 1.45 | March 14–18, 2026 | `autonomous_learner` deployed; Phase 1.45 live; `all-minilm:latest` confirmed locked | ✅ Complete |
| Red team hardening sprint | March 21–22, 2026 | Host port confirmed at 8002; 2,348 system docs ingested; 83 compose services verified; systemd deployed; public URL live | ✅ Complete |
| Consciousness pipeline + v2 API migration | March 22–25, 2026 | WOAH fixed; consciousness bridge patched for v2 API; RAG server port corrected; 31 collections confirmed; 6,665,093 items confirmed | ✅ Complete |
| Embedding model fix + container restoration | March 25, 2026 | All 6 `nomic-embed-text` references patched to `all-minilm:latest`; `jarvis-gis-rag` restored; `jarvis-web-research` restored; `jarvis-ingest-api` relaunched; `Dockerfile.gis-rag` created; 49/49 containers Up | ✅ Complete — committed 2e8b4b2 |
| RAG corpus completion sprint | March 26, 2026 | `governance_rag` (643 chunks), `commons_rag` (306 chunks), `appalachian_cultural_intelligence` (820), `spiritual_texts` (19,338), `geospatialfeatures` (60,000), `GBIM_Fayette_sample` (1,535) — all confirmed live; semantic retrieval verified; 56/56 containers Up | ✅ Complete — March 26, 2026 |
| AaaCPE cultural intelligence deployment | March 27, 2026 | `jarvis-aaacpe-rag` (port 8032) and `jarvis-aaacpe-scraper` (port 8033) built and running; RAG loaded 53 documents (7 new base cultural docs); scraper reporting 39 sources, `total_runs: 1`, 65 documents in `appalachian_cultural_intelligence` from first scrape run on startup; RAG search confirmed returning emergency protocol + Fayette County utility example; container stack updated to 96/96 | ✅ Complete — March 27, 2026 |

---

## 5.13 Semantic Retrieval Smoke Tests — ★ UPDATED March 27, 2026

Semantic retrieval accuracy was verified across three collections on March 26, 2026, and extended to the AaaCPE collection on March 27, 2026, using `all-minilm:latest` embeddings (384-dim, cosine) via the v2 API (host port 8002).

```
┌─────────────────────────────────────────────────────────────┐
│      Semantic Retrieval Smoke Test Results                  │
│      all-minilm:latest · 384-dim · cosine · v2 API          │
│      March 26–27, 2026                                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Test 1 — msjarvis_docs                                     │
│  Query: "Boy Scouts food pantry"                            │
│  Expected: SNAP / Medicaid / food assistance records        │
│  Result:   ✅ Top results = SNAP enrollment,                │
│               Medicaid eligibility, WV food assistance      │
│  Notes:    Semantic bridging confirmed — "BSA" query        │
│            correctly surfaces food/benefits context         │
│                                                             │
│  Test 2 — governance_rag                                    │
│  Query: "DAO governance rules"                              │
│  Expected: MountainShares DAO Charter / governance docs     │
│  Result:   ✅ Top results = MountainShares DAO Charter,     │
│               Program Rules, Parameter Tables               │
│  Notes:    643-chunk corpus retrieval confirmed accurate;   │
│            governance docs semantically indexed correctly   │
│                                                             │
│  Test 3 — governance_rag                                    │
│  Query: "constitution amendment"                            │
│  Expected: Amendment XIV (US Constitution)                  │
│  Result:   ✅ Top result = Amendment XIV,                   │
│               Section 1 (equal protection / due process)   │
│  Notes:    97 US Constitution chunks correctly indexed;     │
│            constitutional text semantically retrievable     │
│                                                             │
│  Test 4 — appalachian_cultural_intelligence (AaaCPE) ★     │
│  Query: "emergency crisis response"                         │
│  Expected: Emergency protocol document                      │
│  Result:   ✅ Top result = emergency protocol               │
│               (crisis response, strip pleasantries)         │
│  Notes:    AaaCPE scraper confirmed live March 27, 2026;   │
│            65 docs from 39 sources; emergency protocol      │
│            correctly indexed and retrievable                │
│                                                             │
│  Test 5 — appalachian_cultural_intelligence (AaaCPE) ★     │
│  Query: "electric bill assistance Fayette County"           │
│  Expected: Fayette County utility example                   │
│  Result:   ✅ Top result = Fayette County utility example   │
│               (Mountain Heart Community Action)             │
│  Notes:    RAG search returning exactly the right results   │
│            — confirmed March 27, 2026. Place-specific       │
│            Appalachian cultural intelligence confirmed       │
│            working end-to-end.                              │
│                                                             │
│  ALL FIVE SMOKE TESTS PASSED — March 26–27, 2026           │
│  Semantic memory layer confirmed accurate and production-   │
│  ready across community resources, governance,              │
│  constitutional, and AaaCPE cultural intelligence corpora.  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

*Figure 5.1. Semantic retrieval smoke test results, March 26–27, 2026. Five representative queries across three collections confirm that the `all-minilm:latest` embedding model is correctly indexing and retrieving semantically related content — including cross-domain bridging (BSA → food assistance), intra-domain governance retrieval, constitutional text retrieval, and AaaCPE Appalachian cultural intelligence (emergency protocol + Fayette County utility assistance).*

These results confirm:

1. **Community resource semantic bridging is accurate** — A query about "Boy Scouts" correctly surfaces food assistance resources (SNAP, Medicaid) because the model captures semantic context, not just lexical matches.

2. **`governance_rag` is correctly indexed** — DAO governance queries surface Charter, Program Rules, and Parameter Tables as top results.

3. **US Constitution is correctly embedded and retrievable** — "constitution amendment" → Amendment XIV confirms 97-chunk constitutional corpus fidelity for governance reasoning.

4. **AaaCPE emergency protocol is correctly indexed and retrievable** — "emergency crisis response" → emergency protocol document confirms that `jarvis-aaacpe-rag` is serving Appalachian cultural intelligence content correctly.

5. **AaaCPE place-specific utility assistance is retrievable** — "electric bill assistance Fayette County" → Mountain Heart Community Action example confirms that the AaaCPE corpus is correctly capturing and surfacing local West Virginia resource context, exactly as designed under P12 – Intelligence with a ZIP code.

---

## 5.12 Limitations and Future Work

**Completed foundations (March 27, 2026):**

- ✅ `gbim_worldview_entities` ingest complete (5,416,521 entities)
- ✅ Autonomous Learner deployed, active, and queried at Phase 1.45
- ✅ Three-database PostgreSQL architecture (ports 5433, 5432, 5435)
- ✅ 993 WV ZCTA centroids in PostGIS
- ✅ ChromaDB containerized at host port 8002 / container port 8000, `hnsw:space: cosine`
- ✅ `psychological-rag` (port 8006) operational
- ✅ GBIM temporal confidence decay deployed across all 5,416,521 entities
- ✅ `all-minilm:latest` (384-dim) confirmed and enforced; 100-word chunk constraint documented
- ✅ Phase 1.45 semantic community memory retrieval live
- ✅ ChromaDB v2 API migration complete
- ✅ 31 collections confirmed — **6,727,956 total items** (March 26, 2026) — update per live query March 27, 2026
- ✅ Consciousness pipeline ACTIVE
- ✅ **96/96 containers Up** — zero crash-looping — March 27, 2026
- ✅ GIS RAG (port 8004) returning live WV geodata
- ✅ `jarvis-ingest-api` and `jarvis-web-research` restored
- ✅ `governance_rag` (643 chunks) — LIVE, retrieval verified
- ✅ `commons_rag` (306 chunks) — LIVE, retrieval verified
- ✅ `spiritual_texts` (19,338 items) — LIVE
- ✅ `geospatialfeatures` (60,000 items) — LIVE
- ✅ `GBIM_Fayette_sample` (1,535 items) — LIVE
- ✅ Semantic retrieval smoke tests passed — Tests 1–5 (BSA → SNAP; DAO → Charter; constitution → Amendment XIV; emergency protocol; Fayette County utility)
- ✅ **AaaCPE dual-service system (`jarvis-aaacpe-rag` port 8032, `jarvis-aaacpe-scraper` port 8033) built and running — March 27, 2026**
- ✅ **`appalachian_cultural_intelligence` collection — 65 documents (confirm live count), 39 sources, `total_runs: 1`, first scrape run confirmed on startup — March 27, 2026**
- ✅ **RAG search verified returning emergency protocol + Fayette County utility example — March 27, 2026**

**Remaining work:**

**`appalachian_cultural_intelligence` count reconciliation — OPEN ⚠️** — 820 (March 26 sprint) vs. 65 (March 27 AaaCPE scraper) discrepancy must be resolved. Run `curl http://localhost:8032/` and ChromaDB v2 collection count before committing Chapters 4 and 5.

**`gbim_beliefs_v2` verification — OPEN** — Present in collection list but item count unverified. Query with `GET .../collections/gbim_beliefs_v2` to confirm count before treating as production data source.

**`conversation_history` pipeline wiring — OI-05 OPEN** — Collection confirmed present. Not formally wired to the production pipeline.

**GBIM temporal decay — POC verification loop** — All 5,416,521 GBIM entities are currently flagged `needs_verification=TRUE`. The POC verification loop is not yet automated.

**Community resource data loading — OPEN** — Verified knowledge bases return empty results for Mount Hope queries. Real community resource data must be entered into `jarvis-local-resources-db` by Community Champions before local-specific resource queries return verified results.

**Disk capacity** — At 96% utilization on the Mount Hope development machine, the next large-scale ingest cycle requires either cleanup or migration before proceeding.

**WV state constitution ingest** — US Constitution (97 chunks) is live in `governance_rag`; WV state constitution is the next governance document to ingest using the confirmed 100-word chunking rule.

**Chunk audit for pre-constraint collections** — Collections ingested before March 26, 2026 (when the 100-word constraint was formally documented) should be audited for oversized chunks.

---

*Last updated: 2026-03-27, Mount Hope WV — Carrie Kidd (Mamma Kidd)*
*Major update March 26, 2026: All six previously sparse/empty RAG collections confirmed live; smoke tests 1–3 added (Section 5.13); ChromaDB port 8002 and `hnsw:space: cosine` documented; 100-word chunk constraint confirmed; total item count updated to 6,727,956; container stack updated to 56/56.*
*★ March 27, 2026: AaaCPE scraper went live — 65 docs in `appalachian_cultural_intelligence`, 53 in RAG (`jarvis-aaacpe-rag`), 39 sources, `total_runs: 1`. Smoke tests 4–5 added (emergency protocol + Fayette County utility — both ✅). Container stack updated to 96/96. `appalachian_cultural_intelligence` count discrepancy (820 vs. 65) flagged — requires live docker exec confirmation before final commit.*
`````
