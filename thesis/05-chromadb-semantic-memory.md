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
- Autonomous learning patterns and research traces — **57 items confirmed post-fix (April 1, 2026); historical baseline 21,181 as of March 20, 2026; accumulation resuming at ~288/day** — confirmed live per `docker exec` query
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

**Geospatial semantic layer (spatial)** — The unified `gbim_worldview_entities` collection holds 5,416,521 embeddings of West Virginia geospatial features, providing semantic representation of the spatial body. The `geospatialfeatures` collection holds **60,000 items** (confirmed March 26, 2026).

**Retrieval engine for RAG** — Services embed queries and use ChromaDB similarity search with metadata filters to retrieve relevant context. Text RAG handles general semantic queries; GIS RAG (port 8004) uses spatial collections backed by `msjarvisgis`.

**Phase 1.45 — Semantic Community Memory Retrieval** — Before queries reach the LLM ensemble, the main brain performs a dedicated semantic memory retrieval step against the `autonomous_learner` collection:

1. Generates a 384-dimensional embedding of the query using `all-minilm:latest` via `jarvis-ollama:11434/api/embeddings`
2. Queries the `autonomous_learner` ChromaDB collection using the embedding
3. Retrieves the 5 most semantically similar community interaction records
4. Prepends retrieved memories to `enhanced_message` before the LLM ensemble

**Consciousness pipeline integration — ACTIVE as of March 25, 2026** — `jarvis-consciousness-bridge` (port 8020) calls ChromaDB using the v2 API (`/api/v2/heartbeat`). End-to-end consciousness pipeline confirmed producing persona-consistent Appalachian-voice responses with Hilbert local entity recall.

**★ Security posture — March 28, 2026** — All services are bound to `127.0.0.1`. The `0.0.0.0` exposure on `jarvis-i-containers` (8015) and `jarvis-memory` (8056) was corrected during the March 28 remediation sprint. `_auth()` is confirmed present and correctly called on all 4 sensitive routes in `ms_jarvis_memory.py`. The `JARVIS_API_KEY` env var is confirmed set in production.

---

## 5.3 Collections and Data Domains

The primary ChromaDB instance (host port 8002, container-internal 8000, `hnsw:space: cosine`) exposes collections across three families: spatial memory, general semantic memory, and resource-focused collections.

> **★ March 28, 2026 full inventory audit: 40 active collections confirmed. Total vectors: 6,675,442.** (7 orphaned empty collections present — no active service queries them. 19,338 duplicate vectors removed from `spiritual_rag` during March 28 remediation. `psychological_rag` restored to 968 documents. `msjarvis_docs` expanded to 4,192 items.)

> **★ April 1, 2026 — Autonomous learner debug sprint (LEARN-01/02/03 resolved):** The `autonomous_learning` collection is confirmed healthy at **57 items post-fix** following the LEARN-01 cosine similarity bug fix and LEARN-03 crash-loop recovery. The dedup gate is running cleanly with explicit `np.float64` and `float()` casting enforced. Historical baseline of 21,181 items (March 20, 2026) is preserved; accumulation at ~288/day is expected to resume. A semantic dedup audit of the `autonomous_learning` collection is recommended once sufficient post-fix cycles have accumulated, as the dedup gate was erroring silently during the LEARN-01 error window. The GBIM Query Router (port 7205) briefly returned HTTP 422 during the repair window (LEARN-02) — resolved same day, returning HTTP 200 OK and stable.

> **★ April 19–20, 2026 — OI-05 FULLY CLOSED. `conversation_history` collection now pipeline-wired.** Root causes resolved: (1) `ai_server_20llm_PRODUCTION.py` line 248 — model name injection bug fixed (`f"You are {model_name}. {message}"` removed); (2) `synthesize()` raw-concatenation replaced with weighted synthesis — one bad model no longer poisons the final answer; (3) `main_brain.py` ~1148 — `_full_prompt[:200]` truncation fixed — Phi3 now receives full prompt with complete history; (4) `main_brain.py` ~860 — `conv_history` injection moved outside RAG block — personal Q&A with no RAG hit now receives history; (5) `main_brain.py` ~1128 — system prompt hardened with concrete rules and worked example for small models. Identity verified: *"Carrie, my name is Egeria Jarvis and I was built by Harmony for Hope Inc. here in Mount Hope, West Virginia, where you also call home."* All checks green. `mvw_gbim_landowner_spatial` CONCURRENT REFRESH complete — 20,593 rows. Unique index deployed. Nightly cron at 3 AM active.

### 5.3.1 Production Spatial Collection

Primary spatial memory (verified complete March 14, 2026; confirmed March 25–28, 2026):

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

**`autonomous_learner`** — **57 items confirmed post-fix (April 1, 2026); historical baseline 21,181 (March 20, 2026); accumulation resuming ~288/day** — confirmed live per `docker exec` query
- Deployed March 14, 2026
- Stores autonomous research findings every 5 minutes
- Queried directly at Phase 1.45 — top-5 results prepended to `enhanced_message` before every production query
- **★ April 1, 2026 — LEARN-01 resolved:** cosine similarity dedup gate bug fixed with explicit `np.float64` dtype enforcement and `float()` return cast. Dedup gate running cleanly. 4 post-fix cycles confirmed, 0 duplicates encountered, 7 entanglement graph nodes, 0 gap failures.
- **⚠️ Semantic dedup audit pending:** the dedup gate was erroring silently during the LEARN-01 error window; items may have been stored without dedup checking during that period. Audit recommended once post-fix cycle count is sufficient.

**`psychological_rag`** — ★ **968 items** — Mental health and psychological safety resources; port 8006. **★ March 28, 2026: restored** — was serving 0 documents despite 968 present; fixed via `PSY_COLLECTION=psychological_rag` env var.

**`appalachian_cultural_intelligence`** — **820 items** — ✅ Confirmed distinct collection from `aaacpe_corpus`. Appalachian cultural context corpus (curated text, values, and cultural intelligence content) ingested March 26, 2026 (OI-14 CLOSED). Volume persisted through AaaCPE deployment. 820 is the authoritative count.

**`aaacpe_corpus`** — ★ **65 documents** — ✅ Confirmed distinct collection from `appalachian_cultural_intelligence`. Live AaaCPE web scrape corpus populated March 27, 2026 by `jarvis-aaacpe-scraper` (port 8033) from 39 Appalachian emergency and community resource sources (`total_runs: 1`). RAG retrieval verified March 27, 2026.

**`spiritual_rag`** ★ — Deduplicated — Mother Carrie Protocol multi-tradition spiritual corpus with Quaker-Appalachian prioritization. **★ March 28, 2026: 19,338 duplicate vectors removed.** Canonical collection name is `spiritual_rag` (previously also referenced as `spiritual_texts`).

**`msjarvis_docs`** — ★ **4,192 items** — ★ March 28, 2026: expanded from 2,348 items. Verified WV community resources + system docs.

**`local_resources`** — Default RAG collection for `jarvis-rag-server`

**`conversation_history`** — Session context storage; ✅ **OI-05 CLOSED April 19–20, 2026 — now fully pipeline-wired.** See §5.3 note above for root cause stack and fix summary.

**`geospatialfeatures`** — ★ **60,000 items** — CONFIRMED LIVE March 26, 2026 (was: 0 items; OI-12 CLOSED)

**`GBIM_Fayette_sample`** — ★ **1,535 items** — CONFIRMED LIVE March 26, 2026 (was: 0 items; OI-13 CLOSED)

### 5.3.3 Governance and Thesis Collections — ★ UPDATED March 26, 2026

**`governance_rag`** — ★ **643 chunks** — CONFIRMED LIVE March 26, 2026 (was: missing/empty)

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

**`commons_rag`** — ★ **306 chunks** — CONFIRMED LIVE March 26, 2026 (was: missing/empty)

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

## 5.4 Database Architecture — ★ Confirmed April 19–20, 2026

Ms. Jarvis uses a dual-database PostgreSQL cluster plus a dedicated community resources database. The system runs on a Lenovo Legion 5 development machine located in **Mount Hope, West Virginia** (ZIP 25880).

**Database 1: `msjarvis`** (8 MB, 6 tables) — port 5433 — ★ **restored March 28, 2026**
- GBIM belief structure and relationships
- Tables: `gbim_beliefs`, `gbim_belief_edges`, `gbim_belief_evidence`, `gbim_evidence`, `gbim_layer_catalog`, `gbim_worldviews`
- 5,416,521 verified GBIM entities; 80 epochs; 206 source layers
- GBIM temporal confidence decay deployed March 15: all entities carry `last_verified`, `confidence_decay`, `needs_verification` metadata
- `jarvis_local_resources` schema also restored March 28, 2026

**Database 2: `msjarvisgis`** (91 GB, 501 tables) — port 5432
- PostGIS-enabled spatial database
- Contains `zcta_wv_centroids` (993 West Virginia ZIP centroids)
- `gbimbeliefnormalized` table: 5,416,521 rows including 20,593 landowner beliefs
- `mvw_gbim_landowner_spatial` materialized view: ★ **20,593 rows — CONCURRENT REFRESH complete April 19–20, 2026. Unique index deployed. Nightly cron at 3 AM active.**

**Database 3: `jarvis-local-resources-db`** — port 5435
- Community resources registry keyed by ZIP code and county
- Sourced from Harmony for Hope Community Champions validation
- `building_parcel_county_tax_mv`: 7,354,707 rows (97.17% address coverage)
- `redteam_sessions` and `redteam_feedback` tables (DB: postgres)

---

## 5.5 Embedding Model and Dimensionality — ★ CONFIRMED LIVE March 28, 2026

Ms. Jarvis uses **`all-minilm:latest`** as the required and confirmed live embedding model for all production ChromaDB collections, producing **384-dimensional vectors** with `hnsw:space: cosine` distance.

> **⚠️ Critical architectural constraint — enforced:** All existing ChromaDB collections — including `gbim_worldview_entities` (5,416,521 entities), `autonomous_learner` (57 items post-fix April 1, 2026; historical baseline 21,181; growing ~288/day), `governance_rag` (643 chunks), `commons_rag` (306 chunks), and all other production collections — use 384-dimensional vectors. The `nomic-embed-text` model produces 768-dimensional vectors and is **incompatible** with all existing production collections. Any rebuild, migration, or new collection ingestion must use `all-minilm:latest`. Confirmed and enforced March 25, 2026 when all six active service files referencing `nomic-embed-text` were patched.

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

### 5.6.1 ChromaDB Container Configuration — ★ April 19, 2026

| Field | Value |
|---|---|
| Container | `jarvis-chroma` |
| Host port | **8002** (`127.0.0.1:8002->8000/tcp`) |
| Container-internal port | 8000 |
| Distance function | `hnsw:space: cosine` |
| API version | v2 active — `/api/v1/` returns HTTP 410 Gone |
| Heartbeat endpoint | `GET /api/v2/heartbeat` |
| Image | `chromadb/chroma@sha256:7605e7b398f96dba833ed1b6272f815b9d33414dde45c68bd246e84447db8591` (Feb 2026 build, schema v10, pinned April 19, 2026) |
| Status | ✅ Production — part of **96-container running stack** |
| Collections confirmed | **49 active** — confirmed April 19, 2026 |
| Total vectors (April 19, 2026) | **6,740,000+** — confirmed April 19, 2026 |

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

### 5.6.2 Active Collections — ★ UPDATED April 19–20, 2026

49 active collections confirmed as of April 19, 2026. All collections use 384-dimensional vectors (`all-minilm:latest`, `hnsw:space: cosine`).

> **★ March 28, 2026 — `appalachian_cultural_intelligence` / `aaacpe_corpus` discrepancy RESOLVED.**
>
> Full ChromaDB inventory audit confirmed both collections exist as distinct entries:
> - `appalachian_cultural_intelligence` — **820 items**: curated Appalachian cultural context corpus, ingested March 26, 2026 (OI-14). Volume persisted through AaaCPE deployment. 820 is the authoritative and current count.
> - `aaacpe_corpus` — **65 documents**: live AaaCPE web scrape corpus, `jarvis-aaacpe-scraper` (port 8033), 39 sources, `total_runs: 1`, March 27, 2026.
>
> These are two distinct collections with different names, different provenance, and different item counts. Discrepancy flag closed.

| Collection | Domain | Record Count | Status |
|---|---|---|---|
| `gbim_worldview_entities` | GBIM spatial worldview | **5,416,521** | ✅ COMPLETE — primary spatial corpus |
| `autonomous_learner` | Autonomous learning patterns | **57 items post-fix (April 1, 2026); baseline 21,181 (March 20); ~288/day resuming** ★ | ✅ Active — Phase 1.45 community memory; LEARN-01/03 resolved; dedup gate clean; semantic dedup audit pending |
| `psychological_rag` ★ | Psychological safety corpus | **968** | ✅ **Restored March 28** — was serving 0; fixed via `PSY_COLLECTION` env var. Port 8006. |
| `appalachian_cultural_intelligence` | Appalachian cultural context | **820** ✅ | ✅ CONFIRMED — OI-14 CLOSED March 26. Distinct from `aaacpe_corpus`. |
| `aaacpe_corpus` ★ | AaaCPE web scrape corpus | **65 docs** | ✅ LIVE March 27 — `jarvis-aaacpe-scraper` port 8033, 39 sources, `total_runs: 1`. Distinct from `appalachian_cultural_intelligence`. |
| `spiritual_rag` ★ | Multi-tradition spiritual corpus | Deduplicated | ✅ **March 28: 19,338 duplicate vectors removed.** Mother Carrie Protocol. Canonical name: `spiritual_rag`. |
| `governance_rag` | MountainShares DAO + US Constitution | ★ **643 chunks** | ✅ COMPLETE — OI-16 CLOSED March 26 (was: missing) |
| `commons_rag` | Commons governance + gamification | ★ **306 chunks** | ✅ COMPLETE — OI-17 CLOSED March 26 (was: missing) |
| `GBIM_sample_rows` | GBIM test sample | 5,000 | ✅ Active |
| `GBIM_sample` | General GBIM sample | Active | ✅ Active |
| `msjarvis-smoke` | Smoke test collection | 1 | ✅ Active |
| `msjarvis_docs` ★ | System docs + community resources | **4,192** | ✅ **Expanded March 28** (was: 2,348) |
| `local_resources` | Default RAG server collection | Active | ✅ Active |
| `gis_wv_benefits` | WV benefits facilities | Active | ✅ Active |
| `ms_jarvis_memory` | Persistent conversation memory | Active | ✅ Active |
| `mountainshares_knowledge` | MountainShares governance | Active | ✅ Active |
| `episodic_index` | Episodic memory index | Active | ✅ Active |
| `conversation_history` | Conversation history | Active | ✅ **OI-05 CLOSED April 19–20, 2026 — fully pipeline-wired** |
| `gbim_beliefs_v2` | GBIM beliefs v2 | Active | ✅ Active |
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
| `fayette_county_resources_2026` | Fayette County resource packet | Active | ✅ Live — confirmed April 19, 2026 |
| `ms_jarvis_identity` | Ms. Jarvis identity corpus | Active | ✅ Live — seeded |
| `wv_resources` | WV statewide resources | Active | ✅ Live |
| `gis_data` | GIS data corpus | Active | ✅ Live |
| `spiritual_knowledge` | Spiritual knowledge base | Active | ✅ Live |
| `psychological_knowledge` | Psychological knowledge base | Active | ✅ Live |
| `gbim_entities` | GBIM entity corpus | Active | ✅ Live |
| `zcta_centroids` | ZCTA centroid embeddings | Active | ✅ Live |
| `operations_history` | Operations history log | Active | ✅ Live |
| `spiritual_wisdom` | Spiritual wisdom corpus | Active | ✅ Live |
| `appalachian_english_corpus` | Appalachian English corpus | Active | ✅ Live |
| `au02_threat_seeds` | A-U02 threat seed corpus | Active | ✅ Live |
| `pia_records` | PIA records | Active | ✅ Live |
| `autonomous_learning` | Autonomous learning (alt name) | Active | ✅ Live |
| `research_history` | Research history log | Active | ✅ Live |
| `jarvis` | Jarvis core corpus | Active | ✅ Live |
| `jarvis_knowledge` | Jarvis knowledge base | Active | ✅ Live |

**Total: 6,740,000+ vectors across 49 active collections — confirmed April 19, 2026**

### 5.6.3 PostgreSQL Database Access

For GBIM belief provenance queries (`msjarvis` — port 5433 — ★ restored March 28, 2026):

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

**GBIM linkage (`msjarvis` — port 5433 — ★ restored March 28, 2026)** — GBIM worldview entities in ChromaDB carry `entity_id` metadata linking to `msjarvis.gbim_beliefs`. Temporal confidence decay (deployed March 15, 2026) attenuates response confidence for entities not recently confirmed. `needs_verification=TRUE` is the trigger for the future POC verification loop. `jarvis_local_resources` schema also restored March 28, 2026.

**PostGIS integration (`msjarvisgis` — port 5432)** — Spatial collections include coordinates and identifiers that join to PostGIS tables. The `zcta_wv_centroids` table (993 rows) provides ZIP code centroids for proximity queries. ★ `mvw_gbim_landowner_spatial` CONCURRENT REFRESH complete April 19–20, 2026 — 20,593 rows, unique index deployed, nightly cron at 3 AM active.

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
5. LM Synthesizer (port 8001, Phase 3.5) pre-processes RAG context before 21-model ensemble — ★ **fast-path bypass deployed April 19–20, 2026**
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

**Reliability and persistence** — ChromaDB runs as Docker container `jarvis-chroma` with the `chroma_data` persistent volume. Part of the **96-container running production stack** on the Mount Hope development machine as of April 1, 2026 (post-recovery).

**API version requirement** — As of March 25, 2026, ChromaDB v2 API is the only active API. Any service still calling `/api/v1/` will receive HTTP 410 Gone.

**Performance** — With 5,416,521 entities in production, bulk ingest used batches of 5,400 with attention to index compaction. End-to-end benchmark confirmed ~100–107s response time (March 22, 2026). `hnsw:space: cosine` is the confirmed distance function for all collections.

**Disk usage** — At 96% utilization on the Mount Hope development machine (Lenovo Legion 5), the `chroma_data` Docker volume must be monitored. Disk cleanup and/or migration to larger storage remains a prerequisite for the next large-scale ingest cycle.

**Security** — ★ All services are bound to `127.0.0.1` as of March 28, 2026. Zero `0.0.0.0` exposures remain in production. `_auth()` is confirmed present and correctly called on all 4 sensitive routes in `ms_jarvis_memory.py`. `JARVIS_API_KEY` env var confirmed set.

**Schema management** — The embedding model (`all-minilm:latest`, 384-dim, `hnsw:space: cosine`) is a locked dependency. Changing it requires a full re-embed of all collections. The 100-word chunk constraint is a fixed schema parameter for all collections. Migrations are treated as explicit schema changes.

---

## 5.10 Production Deployment State — ★ UPDATED April 19–20, 2026

**Hardware:** Lenovo Legion 5 — Mount Hope, West Virginia (ZIP 25880)

**ChromaDB:**
- Container: `jarvis-chroma` — Running with `chroma_data` Docker volume
- Host port: **8002** (`127.0.0.1:8002->8000/tcp`)
- Container-internal port: 8000
- Distance function: `hnsw:space: cosine`
- API: v2 active — `/api/v1/` returns HTTP 410 Gone
- Heartbeat: `GET /api/v2/heartbeat` → 200 ✅
- Image: `chromadb/chroma@sha256:7605e7b398f96dba833ed1b6272f815b9d33414dde45c68bd246e84447db8591` (Feb 2026 build, schema v10, pinned April 19, 2026)
- Collections confirmed: **49 active** — confirmed April 19, 2026
- Total vectors (April 19, 2026): **6,740,000+** ✅
- `gbim_worldview_entities`: 5,416,521 ✅
- `autonomous_learner`: **57 items post-fix (April 1, 2026); baseline 21,181; ~288/day resuming** ✅ — LEARN-01/03 resolved; dedup gate clean; semantic dedup audit pending
- `psychological_rag`: **968 items** — ★ restored March 28 ✅
- `msjarvis_docs`: **4,192 items** — ★ expanded March 28 ✅
- `governance_rag`: ★ **643 chunks** ✅ (was: missing)
- `commons_rag`: ★ **306 chunks** ✅ (was: missing)
- `appalachian_cultural_intelligence`: **820 items** ✅ — confirmed distinct from `aaacpe_corpus`
- `aaacpe_corpus`: **65 documents** ✅ — confirmed distinct from `appalachian_cultural_intelligence`
- `spiritual_rag`: deduplicated ✅ — 19,338 duplicate vectors removed March 28
- `geospatialfeatures`: ★ **60,000 items** ✅ (was: 0)
- `GBIM_Fayette_sample`: ★ **1,535 items** ✅ (was: 0)
- `conversation_history`: ✅ **OI-05 CLOSED — fully pipeline-wired April 19–20, 2026**
- `gbim_beliefs_v2`: Active ✅
- Embedding model: `all-minilm:latest` (384-dim, cosine) — all collections locked

**PostgreSQL Cluster:**
- Port 5433 — `msjarvis` (8 MB, 6 GBIM tables) — 5,416,521 entities; temporal decay deployed — ★ **restored March 28, 2026**
- Port 5432 — `msjarvisgis` (91 GB, 501 PostGIS tables) — 993 WV ZIP centroids; 5,416,521 normalized rows; 20,593 landowner beliefs
  - ★ `mvw_gbim_landowner_spatial` — **20,593 rows — CONCURRENT REFRESH complete April 19–20, 2026. Unique index deployed. Nightly cron at 3 AM active.**
- Port 5435 — `jarvis-local-resources-db` — 7,354,707 building rows; Community Champions validated

**RAG Services:**
- Phase 1.45 community memory: `all-minilm:latest` → `autonomous_learner` (v2 API) → top-5 prepended ✅
- GIS RAG (port 8004): Confirmed operational March 25, 2026 ✅
- Text RAG / `jarvis-rag-server` (host:8003 → container:8016): ✅ ACTIVE
- `psychological_rag` (port 8006): ✅ **Restored March 28** — 968 docs now serving correctly
- `jarvis-web-research` (port 8008 internal): ✅ Restored March 25, 2026
- `jarvis-ingest-api` (port 8009): ✅ Restored March 25, 2026
- `gbim_query_router` (port 7205): ✅ HTTP 200 OK stable — confirmed April 19, 2026. All 3 routing branches live: GBIM fan-out, hospital PostGIS proximity, health access PostGIS. Running from `services/gbim_query_router.py` (765-line real implementation, not stub). Container: `jarvis-gbim-query-router` on `qualia-net`.
- `jarvis-aaacpe-rag` (host:8032): ✅ Running March 27, 2026 — 65 documents, 39 sources
- `jarvis-aaacpe-scraper` (host:8033): ✅ Running March 27, 2026 — `total_runs: 1`
- `lm_synthesizer` fast-path bypass: ✅ **Deployed April 19–20, 2026**

**20LLM Production Inference (`ai_server_20llm_PRODUCTION.py`):**
- ✅ **Running (warm on next query) — April 19–20, 2026**
- ★ Model name injection bug fixed — `f"You are {model_name}. {message}"` removed from line 248; models no longer see their own name before the prompt
- ★ `synthesize()` weighted synthesis deployed — raw top-3 concatenation removed; one bad model no longer poisons the final answer
- Identity verified (T2): *"Carrie, my name is Egeria Jarvis and I was built by Harmony for Hope Inc. here in Mount Hope, West Virginia, where you also call home."*
- Identity verified (T3): *"I'm Ms. Egeria Jarvis, built by Harmony for Hope Inc., designed to serve Appalachian communities in West Virginia."*

**`main_brain.py` fixes — April 19–20, 2026:**
- ★ `_full_prompt[:200]` truncation at ~1148 removed — Phi3 and small models now receive full prompt with complete conversation history
- ★ `conv_history` injection moved outside RAG block (~860) — personal Q&A with no RAG hit now receives history
- ★ System prompt hardened (~1128) — concrete rules and worked example added; small models now follow identity instructions reliably

**Consciousness pipeline:**
- `jarvis-consciousness-bridge` (port 8020): ACTIVE — Chroma v2 heartbeat 200 ✅
- `jarvis-woah`: ACTIVE — stdlib stub, qualia-net ✅
- Pipeline confirmed producing persona-consistent Appalachian-voice responses ✅

**Security posture:**
- All services bound to `127.0.0.1` ✅ — March 28, 2026
- `_auth()` confirmed on all 4 sensitive routes in `ms_jarvis_memory.py` ✅
- `JARVIS_API_KEY` env var confirmed set ✅

**Container stack:** **96/96 containers Up — zero Restarting, zero Exited — confirmed April 1, 2026 (post-recovery)**

---

## 5.11 Sprint Progress Log

| Sprint | Dates | Items Closed | Status |
|---|---|---|---|
| Initial ChromaDB deployment | March 13–15, 2026 | `gbim_worldview_entities` ingest complete (5,416,521); ChromaDB containerized; `chroma_data` volume created | ✅ Complete |
| Autonomous Learner + Phase 1.45 | March 14–18, 2026 | `autonomous_learner` deployed; Phase 1.45 live; `all-minilm:latest` confirmed locked | ✅ Complete |
| Red team hardening sprint | March 21–22, 2026 | Host port confirmed at 8002; 2,348 system docs ingested; 83 compose services verified; systemd deployed; public URL live | ✅ Complete |
| Consciousness pipeline + v2 API migration | March 22–25, 2026 | WOAH fixed; consciousness bridge patched for v2 API; RAG server port corrected; 31 collections confirmed; 6,665,093 items confirmed | ✅ Complete |
| Embedding model fix + container restoration | March 25, 2026 | All 6 `nomic-embed-text` references patched to `all-minilm:latest`; `jarvis-gis-rag` restored; `jarvis-web-research` restored; `jarvis-ingest-api` relaunched; `Dockerfile.gis-rag` created | ✅ Complete — committed 2e8b4b2 |
| RAG corpus completion sprint | March 26, 2026 | `governance_rag` (643 chunks), `commons_rag` (306 chunks), `appalachian_cultural_intelligence` (820), `spiritual_texts` (19,338), `geospatialfeatures` (60,000), `GBIM_Fayette_sample` (1,535) — all confirmed live; semantic retrieval verified | ✅ Complete — March 26, 2026 |
| AaaCPE cultural intelligence deployment | March 27, 2026 | `jarvis-aaacpe-rag` (port 8032) and `jarvis-aaacpe-scraper` (port 8033) built and running; `aaacpe_corpus` (65 docs, 39 sources); RAG search verified; container stack 96/96 | ✅ Complete — March 27, 2026 |
| Security + memory remediation sprint | March 28, 2026 | All `0.0.0.0` exposures corrected; `_auth()` confirmed on 4 sensitive routes; `JARVIS_API_KEY` confirmed set; `spiritual_rag` deduplicated (−19,338 vectors); `psychological_rag` restored (968 docs); `msjarvis_docs` expanded (4,192); `msjarvis` port 5433 restored; `aaacpe_corpus` vs. `appalachian_cultural_intelligence` discrepancy resolved; 40 active collections / 6,675,442 vectors confirmed | ✅ Complete — March 28, 2026 |
| Autonomous learner debug sprint | April 1, 2026 | LEARN-01: `cosine_similarity` numpy dtype bug fixed — explicit `np.float64` and `float()` casting enforced; LEARN-02: GBIM Query Router (port 7205) HTTP 422 schema mismatch resolved — HTTP 200 OK stable; LEARN-03: learner crash-loop resolved — source patched on host, copied into container, restarted; `ms_jarvis_autonomous_learner_optimized.py` and `ms_jarvis_rag_server.py` synced to `services-safe`; 4 post-fix cycles confirmed; `autonomous_learning` collection at 57 items; 7 entanglement graph nodes; 0 gap failures | ✅ Complete — April 1, 2026 |
| ChromaDB version recovery + router restoration | April 19, 2026 | ChromaDB 1.0.0 Rust panic diagnosed (schema v10 incompatible with 1.0.0 Rust SQLite driver); restored from `chroma.sqlite3.bak-20260419-1213`; running image pinned to `sha256:7605e7b` (Feb 2026, 0.6.x); 49 collections / 6.74M vectors confirmed live; GBIM router rebuilt from `services/gbim_query_router.py` (765-line real implementation); all 3 routing branches verified (fan-out, hospital PostGIS, health access PostGIS) | ✅ Complete — April 19, 2026 |
| OI-05 name/identity/history + materialized view sprint | April 19–20, 2026 | OI-05 FULLY CLOSED: `ai_server_20llm_PRODUCTION.py` line 248 model-name injection bug fixed; `synthesize()` weighted synthesis deployed (raw concatenation removed); `main_brain.py` `_full_prompt[:200]` truncation removed (full prompt to all models); `conv_history` injection moved outside RAG block (history now injected on all paths); system prompt hardened with concrete rules + worked example; identity verified T2 + T3. `lm_synthesizer` fast-path bypass deployed. `mvw_gbim_landowner_spatial` CONCURRENT REFRESH complete (20,593 rows); unique index deployed; nightly cron at 3 AM active. 20LLM production container warm. | ✅ Complete — April 20, 2026 |

---

## 5.13 Semantic Retrieval Smoke Tests — ★ CONFIRMED March 26–27, 2026

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
│  Result:   ✅ Top results = SNAP enrollment,               │
│               Medicaid eligibility, WV food assistance      │
│  Notes:    Semantic bridging confirmed — "BSA" query        │
│            correctly surfaces food/benefits context         │
│                                                             │
│  Test 2 — governance_rag                                    │
│  Query: "DAO governance rules"                              │
│  Expected: MountainShares DAO Charter / governance docs     │
│  Result:   ✅ Top results = MountainShares DAO Charter,    │
│               Program Rules, Parameter Tables               │
│  Notes:    643-chunk corpus retrieval confirmed accurate;   │
│            governance docs semantically indexed correctly   │
│                                                             │
│  Test 3 — governance_rag                                    │
│  Query: "constitution amendment"                            │
│  Expected: Amendment XIV (US Constitution)                  │
│  Result:   ✅ Top result = Amendment XIV,                  │
│               Section 1 (equal protection / due process)   │
│  Notes:    97 US Constitution chunks correctly indexed;     │
│            constitutional text semantically retrievable     │
│                                                             │
│  Test 4 — aaacpe_corpus ★                                  │
│  Query: "emergency crisis response"                         │
│  Expected: Emergency protocol document                      │
│  Result:   ✅ Top result = emergency protocol              │
│               (crisis response, strip pleasantries)         │
│  Notes:    AaaCPE scraper confirmed live March 27, 2026;   │
│            65 docs from 39 sources; emergency protocol      │
│            correctly indexed and retrievable                │
│                                                             │
│  Test 5 — aaacpe_corpus ★                                  │
│  Query: "electric bill assistance Fayette County"           │
│  Expected: Fayette County utility example                   │
│  Result:   ✅ Top result = Fayette County utility example  │
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
4. **AaaCPE emergency protocol is correctly indexed and retrievable** — "emergency crisis response" → emergency protocol document confirms that `jarvis-aaacpe-rag` is serving Appalachian cultural intelligence content correctly via the `aaacpe_corpus` collection.
5. **AaaCPE place-specific utility assistance is retrievable** — "electric bill assistance Fayette County" → Mountain Heart Community Action example confirms that the AaaCPE corpus is correctly capturing and surfacing local West Virginia resource context, exactly as designed under P12 – Intelligence with a ZIP code.

---

## 5.12 Limitations and Future Work

**Completed foundations — April 20, 2026:**

- ✅ `gbim_worldview_entities` ingest complete (5,416,521 entities)
- ✅ Autonomous Learner deployed, active, and queried at Phase 1.45 — **LEARN-01/02/03 resolved April 1, 2026; 57 items post-fix; dedup gate clean**
- ✅ Three-database PostgreSQL architecture (ports 5433 ★restored, 5432, 5435)
- ✅ 993 WV ZCTA centroids in PostGIS
- ✅ ChromaDB containerized at host port 8002 / container port 8000, `hnsw:space: cosine`
- ✅ `psychological_rag` (port 8006) — ★ restored March 28, 968 docs now serving correctly
- ✅ GBIM temporal confidence decay deployed across all 5,416,521 entities
- ✅ `all-minilm:latest` (384-dim) confirmed and enforced; 100-word chunk constraint documented
- ✅ Phase 1.45 semantic community memory retrieval live
- ✅ ChromaDB v2 API migration complete
- ✅ **49 active collections — 6,740,000+ total vectors** — confirmed April 19, 2026
- ✅ Consciousness pipeline ACTIVE
- ✅ **96/96 containers Up** — zero crash-looping — April 1, 2026 (post-recovery)
- ✅ GIS RAG (port 8004) returning live WV geodata
- ✅ `jarvis-ingest-api` and `jarvis-web-research` restored
- ✅ `governance_rag` (643 chunks) — LIVE, retrieval verified
- ✅ `commons_rag` (306 chunks) — LIVE, retrieval verified
- ✅ `spiritual_rag` deduplicated (−19,338 vectors) — March 28, 2026
- ✅ `geospatialfeatures` (60,000 items) — LIVE
- ✅ `GBIM_Fayette_sample` (1,535 items) — LIVE
- ✅ Semantic retrieval smoke tests passed — Tests 1–5
- ✅ **AaaCPE dual-service system (`jarvis-aaacpe-rag` port 8032, `jarvis-aaacpe-scraper` port 8033) — March 27, 2026**
- ✅ **`aaacpe_corpus` (65 docs) confirmed distinct from `appalachian_cultural_intelligence` (820 items) — March 28, 2026**
- ✅ **Port security — all `127.0.0.1`, zero `0.0.0.0` exposures — March 28, 2026**
- ✅ **`_auth()` confirmed on all 4 sensitive routes in `ms_jarvis_memory.py` — March 28, 2026**
- ✅ **`msjarvis_docs` expanded to 4,192 items — March 28, 2026**
- ✅ **`ms_jarvis_autonomous_learner_optimized.py` and `ms_jarvis_rag_server.py` synced to `services-safe` — April 1, 2026**
- ✅ **GBIM Query Router (port 7205) HTTP 200 OK stable — all 3 routing branches live (GBIM fan-out, hospital PostGIS, health access PostGIS) — April 19, 2026**
- ✅ **ChromaDB image pinned to `sha256:7605e7b` (Feb 2026 build, schema v10) — April 19, 2026**
- ✅ **OI-05 FULLY CLOSED — `conversation_history` pipeline-wired; `ai_server_20llm_PRODUCTION.py` model-name injection fixed; `synthesize()` weighted synthesis deployed; `main_brain.py` prompt truncation removed, `conv_history` injected on all paths, system prompt hardened — April 19–20, 2026**
- ✅ **`lm_synthesizer` fast-path bypass deployed — April 19–20, 2026**
- ✅ **`mvw_gbim_landowner_spatial` CONCURRENT REFRESH complete — 20,593 rows; unique index deployed; nightly cron at 3 AM active — April 19–20, 2026**
- ✅ **20LLM production container running (warm on next query) — April 19–20, 2026**

**Remaining work:**

**Judge GBIM grounding gap — OPEN (highest priority)** — Truth and alignment judges still use `heuristic_contradiction_v1` rather than live GBIM queries. See Chapter 2, Section 2.8.

**GBIM temporal decay — POC verification loop** — All 5,416,521 GBIM entities carry `needs_verification=TRUE`. The POC verification loop is not yet automated.

**Semantic dedup audit of `autonomous_learning` collection — RECOMMENDED** — The LEARN-01 dedup gate error window means items may have been stored without dedup checking between the last stable restart and the April 1, 2026 fix. Audit recommended once post-fix cycle count is sufficient to surface potential near-duplicates.

**Community resource data loading — OPEN** — Verified knowledge bases return empty results for Mount Hope queries. Real community resource data must be entered into `jarvis-local-resources-db` by Community Champions before local-specific resource queries return verified results.

**WV state constitution ingest** — US Constitution (97 chunks) is live in `governance_rag`; WV state constitution is the next governance document to ingest using the confirmed 100-word chunking rule.

**Chunk audit for pre-constraint collections** — Collections ingested before March 26, 2026 (when the 100-word constraint was formally documented) should be audited for oversized chunks.

**RAG → gateway inference wiring** — All RAG collections are populated; formal wiring of RAG retrieval into the `jarvis-gateway` inference endpoint is the next sprint milestone.

---

*Last updated: 2026-04-20, Mount Hope WV — Carrie Kidd (Mamma Kidd)*
*Major update March 26, 2026: All six previously sparse/empty RAG collections confirmed live; smoke tests 1–3 added (Section 5.13); ChromaDB port 8002 and `hnsw:space: cosine` documented; 100-word chunk constraint confirmed.*
*★ March 27, 2026: AaaCPE scraper live — `aaacpe_corpus` (65 docs, 39 sources, `total_runs: 1`). Smoke tests 4–5 added. Container stack 96/96.*
*★ March 28, 2026: Security remediation complete — all `127.0.0.1`, `_auth()` confirmed, `JARVIS_API_KEY` set. `spiritual_rag` deduplicated (−19,338 vectors). `psychological_rag` restored (968 docs, `PSY_COLLECTION` fix). `msjarvis_docs` expanded (4,192 items). `msjarvis` port 5433 restored. `aaacpe_corpus` vs. `appalachian_cultural_intelligence` discrepancy resolved — two distinct collections confirmed. 40 active collections / 6,675,442 total vectors confirmed via full inventory audit.*
*★ April 1, 2026: Autonomous learner debug sprint complete — LEARN-01 (cosine_similarity numpy dtype bug fixed: explicit np.float64 and float() casting enforced), LEARN-02 (GBIM Query Router port 7205 HTTP 422 schema mismatch resolved — HTTP 200 OK stable), LEARN-03 (crash-loop resolved — source patched on host, copied into container, restarted). Post-fix confirmed: 4 cycles, 4 items stored, 0 deduplicated, 7 entanglement graph nodes, 0 gap failures, autonomous_learning collection at 57 items. ms_jarvis_autonomous_learner_optimized.py and ms_jarvis_rag_server.py synced to services-safe. §5.1, §5.3.2 autonomous_learner entry, §5.6.1 container config, §5.6.2 collections table, §5.10 production state block, §5.11 sprint log, §5.12 completed foundations and remaining work — all updated to reflect post-fix state.*
*★ April 19, 2026: ChromaDB image version recovery — 1.0.0 Rust panic on schema v10 resolved by pinning to Feb 2026 build (sha256:7605e7b). 49 active collections / 6.74M vectors confirmed. GBIM Query Router restored from 765-line real implementation (services/gbim_query_router.py) — all 3 routing branches live. §5.6.1, §5.6.2, §5.10, §5.11, §5.12 updated.*
*★ April 20, 2026: OI-05 FULLY CLOSED — conversation_history pipeline-wired; ai_server_20llm_PRODUCTION.py model-name injection bug fixed (line 248); synthesize() weighted synthesis deployed; main_brain.py prompt truncation removed (~1148), conv_history injected on all paths (~860), system prompt hardened with worked example (~1128); identity verified (T2 + T3: "Carrie, my name is Egeria Jarvis…"). lm_synthesizer fast-path bypass deployed. mvw_gbim_landowner_spatial CONCURRENT REFRESH complete — 20,593 rows, unique index deployed, nightly cron at 3 AM. 20LLM production container warm. §5.3, §5.3.2, §5.4, §5.6.2, §5.7, §5.10, §5.11, §5.12 updated.*
