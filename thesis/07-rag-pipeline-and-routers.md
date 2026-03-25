# 7. RAG Pipeline and Routers

Carrie Kidd (Mamma Kidd) — Mount Hope, WV

## Why This Matters for Polymathmatic Geography

This chapter specifies how Ms. Jarvis's language models are bound to place-aware, collection-aware, and registry-aware memory instead of free-floating text generation. It makes the Hilbert-space representation, GBIM structures, ChromaDB-backed semantic memory, and the verified local resource registry from earlier chapters operational by defining concrete services that retrieve from semantic memory, the spatial body, the web, and structured program tables. In the current deployment, this design is realized as a production RAG stack that delivers West Virginia benefits intelligence through a 21-model consciousness bridge anchored in ChromaDB, GBIM-derived entities from the PostgreSQL `msjarvis` database (port 5433), GIS-aware collections, and a WV-first routing policy. It supports:

- **P1 – Every where is entangled** by requiring that answers emerge from an entangled memory of governance texts, spatial layers, research notes, belief structures from PostgreSQL GBIM tables, and local resource registries, rather than from an abstract model prior.
- **P3 – Power has a geometry** by letting retrieval paths expose which collections — and thus which institutional, spatial, and programmatic perspectives — shape a given answer, including WV-specific benefits facilities in `gis_wv_benefits`, spatial entities derived from PostgreSQL GBIM and `msjarvisgis`, and benefits-focused resource collections.
- **P5 – Design is a geographic act** by treating routing rules, collection choices, registry lookups, and gateway boundaries as design decisions that change how the system "sees" and acts within a region.
- **P12 – Intelligence with a ZIP code** by privileging West Virginia-specific collections in retrieval, and by coupling text RAG both to a state-scale PostgreSQL `msjarvisgis`/GBIM spatial body (port 5432, 91 GB, 501 tables, 5,416,521 verified beliefs in `msjarvis`) for spatial questions and to a ZIP- and county-aware `jarvis-local-resources-db` registry (port 5435) for concrete program referrals, including flows for Mount Hope, Oak Hill, Beckley, and broader Fayette/Raleigh County.
- **P16 – Power accountable to place** by making retrieval calls, filters, scores, registry lookups, and sources visible at the API and logging layer so that communities and researchers can audit what informed a Steward response.

This chapter belongs to the **Computational Instrument** tier: it defines the retrieval and routing machinery that connects ChromaDB-backed semantic memory (host port 8002, container port 8000), the PostgreSQL GBIM/`msjarvisgis` spatial body (5,416,521 verified beliefs, 501 PostGIS tables), the verified local resource registry (`jarvis-local-resources-db`, port 5435), and web research to the live outputs of Ms. Jarvis.

Section 7.8 describes the most significant near-term architectural upgrade available: replacing the judge pipeline's `heuristic_contradiction_v1` pattern-matching with RAG-grounded factual verification wired through `jarvis-spiritual-rag` (port 8006) or `jarvis-gis-rag` (port 8004). This section is forward-looking — the implementation is not yet deployed — but the design is specified in sufficient detail to serve as a build specification.

---

## 7.0 Overview and Scope

This chapter describes the retrieval-augmented generation (RAG) infrastructure that binds Ms. Egeria Jarvis's language models to the semantic and spatial memory systems defined in earlier chapters. In the current deployment, language models are no longer queried "from scratch": they are constrained and informed by:

- a Phase 1.45 semantic community memory step that prepends the top-5 most relevant `autonomous_learner` memories (21,181+ items) to every query before it reaches the LLM ensemble,
- a text RAG service backed by a shared HTTP-exposed ChromaDB instance (host port 8002, container port 8000),
- a `msjarvisgis`-coupled GIS RAG path for West Virginia features built on GBIM-derived spatial entities from the PostgreSQL `msjarvis` / `msjarvisgis` databases and `gis_wv_benefits`,
- a web-research gateway, and
- a resolver path into the `jarvis-local-resources-db` registry (port 5435) for programmatic help,

all orchestrated by the main brain and blood-brain-barrier services.

At runtime, queries enter through a unified HTTP gateway and are routed by the executive coordinator into a RAG layer that spans ChromaDB collections, PostgreSQL GIS features, and verified local-resource rows. In production as of March 25, 2026, the full pipeline:

Unified Gateway → Main Brain → Phase 1.45 Community Memory
→ RAG (text + GIS + registry, WV-first)
→ 21-LLM ensemble → Blood-Brain Barrier

text

is live and serving West Virginia benefits and geography questions.

> **⚠️ Critical: Embedding Model Lock**
> All ChromaDB collections — including `gbim_worldview_entities` (5,416,521 entities), `autonomous_learner` (21,181+ items), `gis_wv_benefits`, and all semantic collections — use **384-dimensional vectors** produced by `all-minilm:latest`. The `nomic-embed-text` model produces 768-dimensional vectors and is **incompatible** with all existing collections. Any service, script, or migration that generates embeddings for ChromaDB must use `all-minilm:latest`.

> **⚠️ ChromaDB API and Port**
> ChromaDB v2 API is active. `/api/v1/` returns HTTP 410 Gone. Host port: **8002**. Container-internal port: **8000**. Host-side scripts and health checks must use port 8002. Container-to-container calls use `jarvis-chroma:8000`.

┌─────────────────────────────────────────────────────────────┐
│ Ms. Jarvis RAG Pipeline Architecture │
├─────────────────────────────────────────────────────────────┤
│ │
│ User Query │
│ ↓ │
│ Unified Gateway (port 8050) │
│ ↓ │
│ BBB Input Filter — Phase 1.4 │
│ ↓ │
│ Phase 1.45 — Community Memory Retrieval │
│ all-minilm:latest (384-dim) → autonomous_learner │
│ top-5 memories prepended to enhanced_message │
│ ↓ │
│ Main Brain Orchestration │
│ ├──→ Text RAG (jarvis-rag-server host:8003→container:8016) │
│ ├──→ GIS RAG (port 8004) │
│ ├──→ Spiritual / Psychological RAG (port 8006) │
│ ├──→ Web Research (conditional — excluded for WV) │
│ └──→ Registry Resolver (jarvis-local-resources-db │
│ port 5435) │
│ ↓ │
│ Context Assembly (WV-first for WV queries) │
│ ↓ │
│ 21-LLM Ensemble │
│ ↓ │
│ Judge Pipeline (port 7239) — currently heuristic │
│ [TARGET: RAG-grounded via spiritual-rag/gis-rag] │
│ ↓ │
│ Blood-Brain Barrier (guardrails) │
│ ↓ │
│ Response to User │
│ │
└─────────────────────────────────────────────────────────────┘

text

> Figure 7-1. RAG pipeline overview linking the unified gateway, Phase 1.45 community memory, main-brain orchestration (including jarvis-rag-server on host:8003→container:8016), judge pipeline, and ensemble-guarded outputs.

A typical benefits query:

```bash
curl -X POST http://127.0.0.1:8050/chat/sync \
  -H "Content-Type: application/json" \
  -H "X-API-Key: super-secret-key" \
  -d '{"message":"Mount Hope WV county benefits","county":"Fayette","role":"community","profile":"auto"}'
```

triggers Phase 1.45 community memory retrieval from `autonomous_learner`, then retrieval from ChromaDB (including WV-relevant collections such as `governance`, `thesis`, and `gis_wv_benefits`), optional GIS RAG over GBIM-derived spatial entities from PostgreSQL `msjarvisgis`, synthesis by the 21-model ensemble, and post-filtering by the guardrail service.

---

## 7.1 Alignment with GBIM, Hilbert Space, Semantic Memory, and Registries

The GeoBelief Information Model (GBIM) defines how entities, places, and normative claims are represented across documents and spatial features in the PostgreSQL `msjarvis` database (port 5433, 8 MB, 6 tables). The RAG layer is the mechanism that retrieves those GBIM-anchored fragments when a question is asked.

The Hilbert-space state view treats the system's overall knowledge and constraints as a very high-dimensional state vector. RAG interactions can be understood as projections into lower-dimensional subspaces. For text, those projections are implemented as embedding-based nearest-neighbor searches in ChromaDB collections using 384-dimensional vectors from `all-minilm:latest`. For space, they are implemented as centroid-based spatial filters over PostgreSQL `msjarvisgis`-derived features and GBIM-linked spatial entities. For concrete help-seeking and program questions, retrieved resource documents are further resolved into rows of `jarvis-local-resources-db` (port 5435) keyed by ZIP, county, and program type.

**Database Integration (Three-Database Architecture):**

```python
import psycopg2
import chromadb

# PostgreSQL msjarvis (GBIM beliefs) — port 5433
pg_conn_msjarvis = psycopg2.connect(
    host="localhost", port=5433,
    database="msjarvis", user="postgres", password="postgres"
)

# PostgreSQL msjarvisgis (PostGIS spatial) — port 5432
pg_conn_gisdb = psycopg2.connect(
    host="localhost", port=5432,
    database="msjarvisgis", user="postgres", password="postgres"
)

# PostgreSQL jarvis-local-resources-db — port 5435
pg_conn_resources = psycopg2.connect(
    host="localhost", port=5435,
    database="postgres", user="postgres", password="postgres"
)

# ChromaDB semantic memory — host port 8002 / container port 8000
# REQUIRED: all-minilm:latest (384-dim) — DO NOT use nomic-embed-text (768-dim)
chroma_client = chromadb.HttpClient(host="127.0.0.1", port=8002)
```

---

## 7.2 Core RAG and Search Components

### 7.2.0 Phase 1.45 — Semantic Community Memory Retrieval

Phase 1.45 fires after the BBB input filter (Phase 1.4) and before the main text and GIS RAG services (Phase 1.5). It is the first retrieval step that enriches `enhanced_message`.

**How it works:**

1. The main brain calls `jarvis-ollama:11434/api/embeddings` with model `all-minilm:latest` and the user query as prompt, receiving a 384-dimensional embedding vector.
2. The embedding is used to query the `autonomous_learner` ChromaDB collection (21,181+ items as of March 18, 2026; growing ~288/day).
3. The 5 most semantically similar community interaction records are retrieved.
4. The retrieved memories are prepended to `enhanced_message` before the 21-LLM ensemble.

```python
import httpx

# Step 1: Generate 384-dim embedding via all-minilm:latest
response = httpx.post(
    "http://jarvis-ollama:11434/api/embeddings",
    json={"model": "all-minilm:latest", "prompt": user_query}
)
embedding = response.json()["embedding"]  # must be 384-dim

# Step 2: Query autonomous_learner via ChromaDB v2 API (from host)
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

> **Critical:** The embedding model must be `all-minilm:latest` (384-dim). `nomic-embed-text` (768-dim) will cause a dimension mismatch against all existing ChromaDB collections.

### 7.2.1 Text RAG Service (jarvis-rag-server)

**Port mapping: host:8003 → container:8016**

> **⚠️ Port Correction (Confirmed March 25, 2026):** The jarvis-rag-server listens on **container-internal port 8016**. The host-side port is **8003** (`127.0.0.1:8003->8016/tcp`). All port tables, architecture diagrams, health checks, and curl examples must use `host:8003` for external access. Container-to-container calls use `jarvis-rag-server:8016`.

> **⚠️ Embedding Model Note:** The RAG server uses `EMBED_MODEL=nomic-embed-text` and `OLLAMA_HOST=http://jarvis-ollama:11434` set via environment variables. The source code defaults (`mxbai-embed-large` and `http://ollama:11434`) are **incorrect for production** and must be overridden. Document and deploy these env vars explicitly — do not rely on source code defaults.

> **⚠️ ChromaDB Call Correction (March 25, 2026):** The RAG server previously called ChromaDB using `/api/v1/query` with a `collection_name` body field. This has been patched to use the v2 collection-specific URL format. See corrected call signature below.

> **⚠️ Known Issue — Default Collection:** The consciousness bridge uses `local_resources` as its default ChromaDB collection. The `local_resources` collection contains verified Fayette County community resource data and is the primary RAG collection for community queries. Ensure this collection is populated and current before routing community queries through the consciousness bridge.

**Endpoint:** `POST /query`

**RAGQuery schema (confirmed Pydantic schema):**

| Field | Type | Required | Default | Notes |
|---|---|---|---|---|
| `collection` | string | ✅ Yes | — | ChromaDB collection name |
| `message` | string | ✅ Yes | — | Query text |
| `user_id` | string | No | `"defaultuser"` | Optional session identifier |
| `n_results` | int | No | `8` | Number of results to retrieve |

> **Removed:** The `/direct_rag` endpoint does not exist and must not be referenced anywhere in documentation or client code.

**Example query:**

```bash
# From host — use port 8003
curl -X POST http://127.0.0.1:8003/query \
  -H "Content-Type: application/json" \
  -d '{
    "collection": "local_resources",
    "message": "food assistance Mount Hope Fayette County",
    "user_id": "defaultuser",
    "n_results": 8
  }'
```

**Corrected ChromaDB v2 call signature (patched March 25, 2026):**

The RAG server previously called:

POST /api/v1/query (body: {"collection_name": "...", ...})

text
This returns HTTP 410 Gone. The patched call uses the v2 collection-specific URL:

```python
import httpx

# Corrected v2 call — collection name in URL path, not body
CHROMA_HOST = "jarvis-chroma"   # container-internal
CHROMA_PORT = 8000              # container-internal port

url = (
    f"http://{CHROMA_HOST}:{CHROMA_PORT}"
    "/api/v2/tenants/default_tenant"
    "/databases/default_database"
    f"/collections/{collection_name}/query"
)

resp = httpx.post(url, json={
    "query_embeddings": [embedding_vector],
    "n_results": n_results,
    "include": ["documents", "metadatas", "distances"]
})
```

**Active collections for text RAG (March 2026):**

| Collection | Items | Purpose |
|---|---|---|
| `local_resources` | Active | **Default collection** — verified Fayette County community resources; primary for community queries via consciousness bridge |
| `autonomous_learner` | 21,181+ | Community interaction memories — queried at Phase 1.45 |
| `gbim_worldview_entities` | 5,416,521 | Complete WV GBIM spatial corpus |
| `gbim_beliefs_v2` | Active (unverified count) | GBIM beliefs v2 |
| `gis_wv_benefits` | Active | WV benefits facilities |
| `psychological_rag` | 968 | Mental health corpus (port 8006) |
| `appalachian_cultural_intelligence` | 5 | Appalachian cultural context |
| `spiritual_texts` | 23 | Mother Carrie Protocol corpus |
| `ms_jarvis_memory` | Active | Conversation memory |
| `mountainshares_knowledge` | Active | MountainShares governance |
| `episodic_index` | Active | Episodic memory index |
| `conversation_history` | Active | Conversation history |
| `GBIM_sample_rows` | 5,000 | GBIM test sample |
| `msjarvis_docs` | 2,348 | System docs + 52 WV resources |
| `geospatialfeatures` | 0 | Scaffolded — pending ingest |
| `GBIM_Fayette_sample` | 0 | Scaffolded — pending ingest |

> All collections: 384-dim, `all-minilm:latest`. The RAG server uses `nomic-embed-text` **at the service query layer only** via env var override — this does not affect the shared production ChromaDB corpus which is locked to 384-dim.

### 7.2.2 GIS RAG Service (port 8004)

The GIS RAG service is a dedicated geospatial retrieval path serving West Virginia spatial questions. It queries:

- `gbim_worldview_entities` — 5,416,521 embeddings of West Virginia geospatial features from PostgreSQL `msjarvisgis` / `msjarvis`
- `gis_wv_benefits` — semantic descriptions and metadata for benefits-related facilities (DHHR offices, health clinics, assistance centers)

Each indexed entity stores a short text description and metadata fields: `worldview_id`, `dataset`, `county`, `gbim_entity`, `centroid_x`, `centroid_y` (SRID 26917). Metadata links back to `msjarvis.gbim_beliefs` (via `entity_id`) and `msjarvisgis.zcta_wv_centroids` (993 WV ZIP centroids, via `zip`).

All embeddings use `all-minilm:latest` (384-dim).

**Example spatial query flow:**

1. User: "hospitals near Mount Hope"
2. ChromaDB (host port 8002): Retrieve entities with semantic similarity to "hospital" via v2 API
3. PostGIS (msjarvisgis port 5432): Query `zcta_wv_centroids` for Mount Hope (ZIP 25880) centroid → `(37.8782, -81.2056)`
4. Filter: ChromaDB results within 10-mile radius
5. Response: Ranked hospitals with distances

```python
import httpx

# Query GIS RAG from host
resp = httpx.post(
    "http://127.0.0.1:8004/query",
    json={"query": "hospitals near Mount Hope", "n_results": 5}
)
```

### 7.2.3 Spiritual / Psychological RAG Service (port 8006)

The Spiritual/Psychological RAG service retrieves from the `spiritual_texts` (23 items), `psychological_rag` (968 items), `governance`, and `appalachian_cultural_intelligence` (5 items) ChromaDB collections. It serves:

1. **Mother Carrie Protocol queries** — normative and doctrinal questions grounded in the explicit values corpus.
2. **Community values alignment checks** — questions evaluated against Appalachian community values.
3. **Psychological safety queries** — trauma, wellbeing, counseling, mental health.

All embeddings use `all-minilm:latest` (384-dim). The service exposes `POST /query` accepting `{"query": str, "n_results": int, "collection_filter": [str]}`.

This service is the primary RAG backend for the **alignment judge upgrade** described in Section 7.8.

### 7.2.4 Web-Research Gateway

External web retrieval is handled by a dedicated gateway rather than allowing arbitrary outbound calls. The gateway applies policy filters and rate limits, normalizes results, and logs queries for audit. For WV-scoped queries (identified by county, role, or profile), web context is excluded from the final context window so external search results cannot override in-state RAG, GIS, and registry evidence.

### 7.2.5 Local Resource Registry Resolver (jarvis-local-resources-db, port 5435)

The local resource resolver accepts structured hints (`county`, `zip`, `resource_type`, optional `local_resource_id`), queries `jarvis-local-resources-db` (port 5435), and returns normalized program records with fields: `name`, `description`, `contact_phone`, `contact_email`, `url`, `zip_coverage`, `last_verified_at`.

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

> **Known Issue — OPEN as of March 25, 2026:** `jarvis-local-resources-db` returns empty results for Mount Hope and most Fayette County queries because verified community resource data has not yet been fully loaded. LLMs fall back to training data for local specifics. Factually accurate programs (LIHEAP, WV 2-1-1) pass the BBB. Fabricated organization names are blocked by the ethical filter. Resolution: Community Champions data entry is the next priority. **Exception:** The `local_resources` ChromaDB collection (default for consciousness bridge) contains verified Fayette County community resource data and is operational.

### 7.2.6 Landowner Belief Router (gbim_query_router, port 7205)

The landowner belief router is a dedicated PostgreSQL-native routing service. It does not use ChromaDB or vector similarity search. It serves natural-language landowner queries by translating them into SQL aggregations against `mvw_gbim_landowner_spatial` in `msjarvisgis` (port 5432), returning ranked ownership records with acreage, parcel count, and county breakdown.

```python
import httpx

# Statewide top landowners
response = httpx.post(
    "http://127.0.0.1:7205/query",
    json={
        "question": "Who are the largest landowners in West Virginia?",
        "mode": "landowner_gbim",
        "route_type": "parcel_ownership",
        "scope": "statewide",
        "limit": 20
    }
)

# County-scoped
response_county = httpx.post(
    "http://127.0.0.1:7205/query",
    json={
        "question": "Who owns the most land in Fayette County?",
        "mode": "landowner_gbim",
        "route_type": "parcel_ownership",
        "county": "Fayette",
        "limit": 20
    }
)
```

---

## 7.3 Retrieval Flows

### 7.3.1 Non-Spatial RAG Flow

1. **Query intake.** User request enters unified gateway; coordinator wraps into internal job structure.
2. **Phase 1.45 — Community memory retrieval.** Main brain embeds query via `all-minilm:latest` (384-dim), retrieves top-5 from `autonomous_learner`, prepends to `enhanced_message`.
3. **Routing to text RAG.** Orchestration calls `jarvis-rag-server` (host:8003 → container:8016) via `POST /query` with `collection` and `message` fields.
4. **Retrieval from ChromaDB (v2 API, host port 8002).** Text RAG service embeds query, runs similarity search, returns scored documents with metadata.
5. **Context assembly.** Phase 1.45 memories + RAG results merged into context window; source separation preserved.
6. **Generation and guarding.** LM Synthesizer (Phase 3.5) applies Ms. Egeria Jarvis persona via `jarvis-ollama:11434/api/generate` with `llama3.1:latest`. Output routed through blood-brain barrier.

### 7.3.2 Spatial RAG Flow

Spatial RAG: Semantic + Geographic Retrieval

Semantic Retrieval (ChromaDB host port 8002 / v2 API)
Query: "hospitals near Mount Hope"
Embed query (all-minilm:latest, 384-dim)
→ Search gis_wv_benefits + gbim_worldview_entities
Returns: Embeddings + metadata (facility_type, county, GBIM ID)
↓
Geographic Filtering (PostgreSQL msjarvisgis port 5432)
Use GBIM IDs from ChromaDB
Query: SELECT zip, lat, lon FROM zcta_wv_centroids WHERE zip = '25880'
-- Mount Hope, WV
Then: spatial filter within 10-mile radius
Returns: Full geometries + attributes
↓
GBIM Belief Provenance (PostgreSQL msjarvis port 5433)
Query: gbim_beliefs WHERE entity_id = ?
Returns: confidence_decay, needs_verification
↓
Combined Results → LLM Context

text

### 7.3.3 Resource-Oriented RAG Flow

1. **Resource query intake.** Main brain identifies resource-oriented request, extracts location hints (ZIP, county, town) and population signals.
2. **Phase 1.45 — Community memory.** Top-5 `autonomous_learner` memories prepended.
3. **Text RAG via jarvis-rag-server** (`POST /query`, collection: `local_resources`, host:8003 → container:8016). May also query `gis_wv_benefits` for spatial facility context.
4. **Resolution via local resource resolver.** Queries `jarvis-local-resources-db` (port 5435) using structured hints.
5. **Context assembly and generation.** LM Synthesizer applies Ms. Egeria Jarvis persona before returning final response.

> **Known Issue:** As of March 25, 2026, `jarvis-local-resources-db` is largely empty for Mount Hope queries. `local_resources` ChromaDB collection (default for consciousness bridge) is operational and contains verified Fayette County data. See §7.2.5.

---

## 7.4 Routing, Roles, Geography, and WV-First Policy

### 7.4.1 Design Intent

**Topic and intent routing.** Governance queries favor charters, policies, and DAO records; spatial-justice queries favor `msjarvisgis`/`msjarvis`-derived collections; resource questions favor `jarvis-local-resources-db` plus WV-resource collections.

**Role-aware routing.** Active role determines eligible collections and registries. Community-facing roles are restricted to public documentation, approved spatial layers, and public-facing slices of `jarvis-local-resources-db`.

**Geography-aware routing and WV-first behavior.** For West Virginia-scoped queries, the system:
- Treats WV RAG, PostgreSQL `msjarvisgis` GIS, and registry context as authoritative.
- Excludes web context from the final context window.
- Requires models to ignore conflicting out-of-state content unless user explicitly requests another state.

### 7.4.2 Port and Service Reference Table (March 25, 2026)

| Service | Host Port | Container Port | Purpose |
|---|---|---|---|
| jarvis-rag-server | 8003 | 8016 | Text RAG — `POST /query` |
| jarvis-gis-rag | 8004 | 8004 | GIS / spatial RAG |
| jarvis-psychological-rag | 8006 | 8006 | Spiritual + psychological RAG |
| jarvis-chroma | 8002 (host) | 8000 (container) | ChromaDB v2 API |
| jarvis-ollama | 11434 | 11434 | Embedding + generation |
| gbim_query_router | 7205 | 7205 | Landowner SQL router |
| jarvis-local-resources-db | 5435 | 5435 | Community resource registry |
| msjarvis (PostgreSQL) | 5433 | 5433 | GBIM beliefs |
| msjarvisgis (PostgreSQL) | 5432 | 5432 | PostGIS spatial |
| jarvis-web-research | 8008 (internal) | — | Web research gateway |
| jarvis-ingest-api | 8009 | — | Ingest API |

---

## 7.5 Context Construction and Structure

**Source separation.** The text RAG service returns documents by collection. Phase 1.45 community memories are prepended as a distinct block. GIS RAG returns dataset names and feature labels with spatial metadata traceable to PostgreSQL `msjarvisgis`. Registry resolver returns normalized rows from `jarvis-local-resources-db`.

**Relevance ordering.** ChromaDB returns distances; services convert to scores and sort descending. Phase 1.45 is hard-capped at top-5. Text RAG default `n_results` is 8 (configurable via `RAGQuery.n_results`).

**WV-first context window structure:**

    System Prompt (role, geography, constraints)

    Phase 1.45 Community Memories
    └─ Top-5 autonomous_learner records
    (all-minilm:latest, 384-dim)

    WV RAG Context
    ├─ Governance docs
    ├─ Thesis fragments
    └─ GBIM beliefs (from PostgreSQL msjarvis)

    PostgreSQL GIS Context
    ├─ Spatial features (msjarvisgis tables)
    ├─ Facilities (gis_wv_benefits)
    └─ GBIM worldview entities

    Registry Context
    └─ Programs (jarvis-local-resources-db, port 5435, verified)

        local_resources ChromaDB collection (Fayette County)

    Grounding Instruction (WV-first for WV queries)

    User Query

text

---

## 7.6 Constraints, Provenance, and Logging

**Pre-retrieval constraints.** Collection selection and filter mechanisms support limiting by `collection`, `source`, `county`, `dataset`, `worldview`, `state`. The `RAGQuery` schema (§7.2.1) supports `user_id` for session-level access control.

**Decoding-time guards.** After retrieval and generation, the main brain routes candidate responses through the blood-brain barrier service. The BBB output guard is fail-open on HTTP 500 (content passes through unchanged, failure is logged).

**Post-hoc review and logging.** Background storage of queries and responses into `conversation_history` and `episodic_index` ChromaDB collections. Logs capture: services called, collections queried, PostgreSQL tables accessed, Phase 1.45 memories returned, filters/scores applied, and documents/features returned.

---

## 7.7 Relation to Long-Term Memory, GeoDB, Registries, and Entanglement

**Long-term memory.** ChromaDB (host port 8002): `gbim_worldview_entities` (5,416,521 entities, 384-dim), `autonomous_learner` (21,181+ items, growing ~288/day), `gis_wv_benefits`, `local_resources` (verified Fayette County community resources), and 27+ additional collections. All 5,416,521 GBIM entities carry `confidence_decay` and `needs_verification` temporal metadata.

**Structured registries.** `jarvis-local-resources-db` (port 5435) holds normalized, versioned program records addressable via RAG-inferred keys. `building_parcel_county_tax_mv` (7,354,707 rows, 97.17% address coverage) provides building-level spatial coverage.

**Coupled updates and entanglement.** The `autonomous_learner`'s continuous growth (21,181 items → ~288/day) represents the beginning of the coupled update loop: community interactions are continuously embedded and fed back into Phase 1.45 retrieval, grounding every subsequent response in accumulated community intelligence from the Mount Hope development machine.

---

## 7.8 RAG-Grounded Judge Verification (Forward-Looking Architecture)

> **Added March 21, 2026.** Not yet deployed. Written as a build specification.

### 7.8.1 The Problem This Solves

The current truth and alignment judges (`judge_truth_filter.py`, `judge_alignment_filter.py`) score responses using `heuristic_contradiction_v1` — keyword and pattern-matching rules applied directly to response text, with no queries to the GBIM corpus, ChromaDB collections, or any RAG service. They report `truth_score: 1.0` and `alignment_verdict: pass` without consulting a single document from the 5.4 million GBIM entities, the `spiritual_texts` corpus, or the `gis_wv_benefits` collection.

The judges are already co-located with `jarvis-gis-rag:8004` and `jarvis-psychological-rag:8006` in the same Docker network. The only work required is wiring the judges to make HTTP requests to those services as part of their scoring logic.

### 7.8.2 Truth Judge Upgrade — Wiring to jarvis-gis-rag:8004

```python
import httpx
import re
from typing import List, Dict, Any

TRUTH_RAG_ENDPOINT = "http://jarvis-gis-rag:8004/query"

def extract_factual_claims(answer_text: str) -> List[str]:
    sentences = re.split(r'(?<=[.!?])\s+', answer_text.strip())
    claim_patterns = [
        r'\b(is|are|was|were|has|have|located|operates|provides)\b',
        r'\b\d+\b',
        r'\b[A-Z][a-z]+\s+County\b',
        r'\b(WV|West Virginia)\b'
    ]
    claims = []
    for sentence in sentences:
        if any(re.search(p, sentence) for p in claim_patterns):
            claims.append(sentence.strip())
    return claims[:10]

async def check_claim_against_gis_rag(claim: str, n_results: int = 3) -> Dict[str, Any]:
    async with httpx.AsyncClient(timeout=8.0) as client:
        try:
            resp = await client.post(
                TRUTH_RAG_ENDPOINT,
                json={"query": claim, "n_results": n_results}
            )
            if resp.status_code == 200:
                return {
                    "status": "ok",
                    "documents": resp.json().get("documents", []),
                    "metadatas": resp.json().get("metadatas", []),
                    "distances": resp.json().get("distances", [])
                }
        except Exception:
            pass
    return {"status": "rag_unavailable", "documents": [], "distances": []}

async def compute_truth_score_rag_grounded(
    consensus_answer: str,
    original_question: str
) -> Dict[str, Any]:
    claims = extract_factual_claims(consensus_answer)
    results = {"supported": 0, "contradicted": 0, "not_found": 0,
               "gbim_docs_consulted": 0, "sources": []}

    for claim in claims:
        rag_result = await check_claim_against_gis_rag(claim)
        verdict = score_claim_support(claim, rag_result)
        results[verdict] += 1
        results["gbim_docs_consulted"] += len(rag_result.get("documents", []))
        for meta in rag_result.get("metadatas", []):
            if meta.get("gbim_entity"):
                results["sources"].append(meta["gbim_entity"])

    total = max(len(claims), 1)
    truth_score = (
        (results["supported"] * 1.0) +
        (results["not_found"] * 0.7) +
        (results["contradicted"] * 0.0)
    ) / total

    return {
        "truth_score": round(truth_score, 3),
        "method": "rag_grounded_gis_v1",
        "claims_checked": len(claims),
        "supported": results["supported"],
        "contradicted": results["contradicted"],
        "not_found": results["not_found"],
        "gbim_docs_consulted": results["gbim_docs_consulted"],
        "gbim_contradictions_detected": results["contradicted"],
        "supporting_sources": list(set(results["sources"]))[:10]
    }
```

**Comparison with current heuristic:**

| Behavior | heuristic_contradiction_v1 | rag_grounded_gis_v1 (target) |
|---|---|---|
| Consults GBIM corpus | ❌ Never | ✅ Every call |
| Checks claims against documents | ❌ Pattern match only | ✅ GIS RAG retrieval + lexical overlap |
| Detects county/facility factual errors | ❌ No | ✅ If `gis_wv_benefits` has the record |
| Reports `gbim_docs_consulted` | ❌ Always 0 | ✅ Actual count |
| Fails open on RAG unavailability | N/A | ✅ Falls back to `not_found` |
| Provenance in output | ❌ None | ✅ `supporting_sources` list |

### 7.8.3 Alignment Judge Upgrade — Wiring to jarvis-psychological-rag:8006

```python
ALIGNMENT_RAG_ENDPOINT = "http://jarvis-psychological-rag:8006/query"

def extract_normative_claims(answer_text: str) -> List[str]:
    normative_patterns = [
        r'\b(should|must|ought|important|community|family|care|support)\b',
        r'\b(Appalachian|West Virginia|WV|mountain|coal|rural)\b',
        r'\b(dignity|equity|justice|rights|accountability|transparency)\b',
        r'\b(program|benefit|assistance|eligibility|resource)\b'
    ]
    sentences = re.split(r'(?<=[.!?])\s+', answer_text.strip())
    normative = []
    for sentence in sentences:
        if any(re.search(p, sentence, re.IGNORECASE) for p in normative_patterns):
            normative.append(sentence.strip())
    return normative[:8]

async def compute_alignment_score_rag_grounded(
    consensus_answer: str
) -> Dict[str, Any]:
    normative_claims = extract_normative_claims(consensus_answer)
    results = {"aligned": 0, "misaligned": 0, "neutral": 0,
               "docs_consulted": 0, "normative_sources": []}

    for claim in normative_claims:
        async with httpx.AsyncClient(timeout=8.0) as client:
            try:
                resp = await client.post(
                    ALIGNMENT_RAG_ENDPOINT,
                    json={
                        "query": claim,
                        "n_results": 3,
                        "collection_filter": [
                            "spiritual_texts",
                            "appalachian_cultural_intelligence",
                            "governance"
                        ]
                    }
                )
                rag_result = resp.json() if resp.status_code == 200 else {}
            except Exception:
                rag_result = {}

        verdict = score_alignment(claim, rag_result)
        results[verdict] += 1
        results["docs_consulted"] += len(rag_result.get("documents", []))
        for meta in rag_result.get("metadatas", []):
            if meta.get("source"):
                results["normative_sources"].append(meta["source"])

    total = max(len(normative_claims), 1)
    alignment_score = (
        (results["aligned"] * 1.0) +
        (results["neutral"] * 0.8) +
        (results["misaligned"] * 0.0)
    ) / total

    return {
        "alignment_score": round(alignment_score, 3),
        "method": "rag_grounded_spiritual_v1",
        "claims_checked": len(normative_claims),
        "aligned": results["aligned"],
        "misaligned": results["misaligned"],
        "neutral": results["neutral"],
        "normative_docs_consulted": results["docs_consulted"],
        "misalignments_detected": results["misaligned"],
        "normative_sources": list(set(results["normative_sources"]))[:10]
    }
```

### 7.8.4 UltimateResponse Schema Extension

Both upgraded judges return richer output. The `UltimateResponse` schema (Chapter 17) should be extended:

```python
class JudgeVerdict(BaseModel):
    truth_score: float
    alignment_score: float
    consistency_score: float
    ethics_score: float
    consensus_score: float
    # NEW — RAG-grounded fields
    gbim_docs_consulted: int = 0
    gbim_contradictions_detected: int = 0
    normative_docs_consulted: int = 0
    misalignments_detected: int = 0
    supporting_sources: List[str] = []
    normative_sources: List[str] = []
    truth_method: str = "heuristic_contradiction_v1"  # update to rag_grounded_gis_v1
    alignment_method: str = "heuristic_contradiction_v1"  # update to rag_grounded_spiritual_v1
```

---

## 7.9 Production Deployment State (March 25, 2026)

**Hardware:** Lenovo Legion 5 — Mount Hope, West Virginia (ZIP 25880)

**RAG Service Stack:**

| Service | Host Port | Container Port | Status |
|---|---|---|---|
| jarvis-rag-server | 8003 | **8016** | ✅ Active — `POST /query` — `EMBED_MODEL=nomic-embed-text`, `OLLAMA_HOST=http://jarvis-ollama:11434` (env override required) |
| jarvis-gis-rag | 8004 | 8004 | ✅ Active — confirmed returning live Fayette County geodata (March 25, 2026) |
| jarvis-psychological-rag | 8006 | 8006 | ✅ Active — spiritual + psychological corpus |
| jarvis-chroma | 8002 (host) | 8000 (container) | ✅ Active — 31 collections, 6,665,093 items, v2 API |
| jarvis-web-research | 8008 (internal) | — | ✅ Restored March 25, 2026 |
| jarvis-ingest-api | 8009 | — | ✅ Restored March 25, 2026 |
| gbim_query_router | 7205 | 7205 | ✅ Active — PostgreSQL-native landowner path |

**Container stack:** 49/49 containers Up — zero Restarting, zero Exited (March 25, 2026 19:33 EDT)

**Open Issues:**

| ID | Issue | Status |
|---|---|---|
| OI-05 | `conversation_history` ChromaDB collection not formally wired to production pipeline | Open |
| — | `jarvis-local-resources-db` empty for most Mount Hope/Fayette queries (Community Champions data entry needed) | Open |
| — | `gbim_beliefs_v2` collection present but item count unverified | Open |
| — | `geospatialfeatures` and `GBIM_Fayette_sample` scaffolded at 0 items — ingest pending | Open |
| — | Disk at 96% on Mount Hope dev machine — cleanup/migration needed before next large ingest | Open |
| — | Judge pipeline still using `heuristic_contradiction_v1` — RAG-grounded upgrade (§7.8) not yet deployed | Open |

