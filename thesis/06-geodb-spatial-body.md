# 6. GeoDB Spatial Body

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: April 23, 2026*

---

## Why This Matters for Polymathmatic Geography

This chapter specifies how Ms. Allis's language models are bound to *place-aware,
collection-aware, and registry-aware memory* instead of free-floating text generation.
It makes the Hilbert-space representation, GBIM structures, ChromaDB-backed semantic
memory, and the verified local resource registry from earlier chapters operational by
defining concrete services that retrieve from semantic memory, the spatial body, the web,
and structured program tables. In the current deployment, this design is realized as a
production RAG stack that delivers West Virginia benefits intelligence through a
multi-model consciousness bridge anchored in ChromaDB, GBIM-derived entities from a
two-container PostgreSQL architecture, GIS-aware collections, and a WV-first routing
policy. It supports:

- **P1 – Every where is entangled** by requiring that answers emerge from an entangled
  memory of governance texts, spatial layers, research notes, belief structures from
  PostgreSQL GBIM tables, and local resource registries, rather than from an abstract
  model prior.
- **P3 – Power has a geometry** by letting retrieval paths expose which collections —
  and thus which institutional, spatial, and programmatic perspectives — shape a given
  answer, including WV-specific benefits facilities in `gis_wv_benefits`, spatial
  entities derived from PostgreSQL GBIM and `msallisgis`, benefits-focused resource
  collections, and the GBIM landowner belief layer (`mvw_gbim_landowner_spatial`) that
  makes corporate and government land ownership computable and queryable by natural
  language.
- **P5 – Design is a geographic act** by treating routing rules, collection choices,
  registry lookups, and gateway boundaries as design decisions that change how the system
  "sees" and acts within a region — including the explicit decision to route landowner
  queries through a PostgreSQL-native path rather than through vector similarity search.
- **P12 – Intelligence with a ZIP code** by privileging West Virginia-specific
  collections in retrieval, and by coupling text RAG to a state-scale PostGIS spatial
  body in `msallisgis` — available via two containers: `msallis-db` (production,
  host 5433 / container 5432) and `postgis-forensic` (forensic, port 5432) — and a
  ZIP- and county-aware `allis-local-resources-db` registry (port 5435) for concrete
  program referrals.
- **P16 – Power accountable to place** by making retrieval calls, filters, scores,
  registry lookups, and sources visible at the API and logging layer so that communities
  and researchers can audit what informed a Steward response — and by making the
  `allis-gbim-query-router` landowner path explicitly inspectable as a structured SQL
  aggregation over verified GBIM belief records rather than an opaque embedding
  similarity result.

As such, this chapter belongs to the **Computational Instrument** tier: it defines the
retrieval and routing machinery that connects ChromaDB-backed semantic memory
(`allis-chroma`, host port **8002**, container port **8000**), the PostgreSQL
`msallisgis` spatial body (5,416,521 verified beliefs, PostGIS tables), the verified
local resource registry (`allis-local-resources-db`, port 5435), the GBIM landowner
belief layer (`mvw_gbim_landowner_spatial`, routed via `allis-gbim-query-router`
port 7205), the live confidence decay and reverification loop, and web research to the
live outputs of Ms. Allis.

---

## 6.0 Two-Container Database Architecture — ★★ Confirmed April 23, 2026

> **This section supersedes all single-container framing from prior drafts.**
> The `msallisgis` database is accessible via two containers with different roles,
> different host port mappings, and different schemas. Always use the correct container
> and access pattern for the operation you are performing.

### Production Container: `msallis-db`

| Property | Value |
|---|---|
| Container | `msallis-db` |
| Host port | **5433** (host-mapped) |
| Container-internal port | **5432** |
| Database name | `msallisgis` |
| Role | `postgres` |
| Size | **16 GB** |
| Tables | **294** |
| Schemas | **11** |
| Role | GBIM belief graph — primary production read/write |

**Production psql access:**

```bash
docker exec msallis-db psql -U postgres -d msallisgis
```

**From Docker host (Python):**

```python
import psycopg2
# Host-mapped port 5433 — container-internal port 5432
conn = psycopg2.connect(
    host="localhost", port=5433,
    database="msallisgis", user="postgres", password="postgres"
)
```

**From container on same Docker network (Python):**

```python
import psycopg2
# Use container name + container-internal port
conn = psycopg2.connect(
    host="msallis-db", port=5432,
    database="msallisgis", user="postgres", password="postgres"
)
```

### Forensic Container: `postgis-forensic`

| Property | Value |
|---|---|
| Container | `postgis-forensic` |
| Host port | **5432** |
| Container-internal port | **5432** |
| Database name | `msallisgis` |
| Role | `allis` (requires `-h 127.0.0.1`) |
| Size | **17 GB** |
| Tables | **314** |
| Schemas | **9** |
| Role | Forensic analysis, auditing, migration validation |

**Forensic psql access:**

```bash
docker exec postgis-forensic psql -h 127.0.0.1 -U allis -d msallisgis
```

**From Docker host (Python):**

```python
import psycopg2
# Forensic container — role allis, requires explicit host
conn = psycopg2.connect(
    host="127.0.0.1", port=5432,
    database="msallisgis", user="allis", password="<allis_password>"
)
```

> **Port disambiguation:**
> - Port **5433** on the Docker host → `msallis-db` (production) → container-internal
>   5432
> - Port **5432** on the Docker host → `postgis-forensic` (forensic) → container-internal
>   5432
> - From within other containers: use `msallis-db:5432` for production access
> - Port **5452** is invalid and has never existed in production

### Container Comparison

| Property | `msallis-db` (production) | `postgis-forensic` (forensic) |
|---|---|---|
| Host port | **5433** | **5432** |
| Container port | 5432 | 5432 |
| Database | `msallisgis` | `msallisgis` |
| Role | `postgres` | `allis` (+ `-h 127.0.0.1`) |
| Size | **16 GB** | **17 GB** |
| Tables | **294** | **314** |
| Schemas | **11** | **9** |
| `mvw_gbim_landowner_spatial` | ✅ **38,979 rows** | ❌ Not present |
| Primary use | Production read/write | Forensic auditing |

> **`mvw_gbim_landowner_spatial`:** This materialized view is present in `msallis-db`
> with **✅ 38,979 rows** — confirmed April 23, 2026. It is **not present** in
> `postgis-forensic`. All landowner routing via `allis-gbim-query-router` (port 7205)
> targets `msallis-db` (host 5433 / container 5432).

---

## 6.1 Overview and Scope

This chapter describes the retrieval-augmented generation (RAG) infrastructure that
binds Ms. Egeria Allis's language models to the semantic and spatial memory systems
defined in earlier chapters. In the current deployment, language models are no longer
queried "from scratch": they are constrained and informed by:

- a **Phase 1.45 semantic community memory step** that prepends the top-5 most relevant
  `autonomous_learner` memories to every query before it reaches the LLM ensemble,
- a text RAG service backed by a shared HTTP-exposed ChromaDB instance (`allis-chroma`,
  host port **8002**, container port **8000**),
- a `msallisgis`-coupled GIS RAG path for West Virginia features — **GIS-RAG v0.4.0
  (port 8004)** — built on GBIM-derived spatial entities from `msallis-db` (host 5433 /
  container 5432) and the `gis_wv_benefits` collection, covering **204 WV GIS datasets**
  and **7,357 WV bridges**,
- a **GBIM landowner query path** routed through `allis-gbim-query-router` (port 7205)
  directly against `mvw_gbim_landowner_spatial` in `msallis-db` — a PostgreSQL-native
  path that bypasses ChromaDB entirely for structured ownership questions,
- a **live confidence decay and reverification loop** (`services.confidence_decay_loop`)
  running as a persistent async scheduled task inside `allis-ingest-watcher`, operating
  against `msallisgis` on `msallis-db` (host 5433 / container 5432) on a 24-hour
  cycle,
- a web-research gateway, and
- a resolver path into the `allis-local-resources-db` registry (port 5435) for
  programmatic help,

all orchestrated by `allis-main-brain` (port **8050**) and the blood-brain-barrier
services.

At runtime, queries enter through `allis-unified-gateway` (host **18018** → container
**8001** — ✅ confirmed April 23, 2026) and are routed by the executive coordinator into
a RAG layer that spans ChromaDB collections, PostgreSQL GIS features, GBIM landowner
beliefs, and verified local-resource rows. In production as of April 23, 2026, the full
pipeline:

```
allis-unified-gateway (host:18018 → container:8001)
→ allis-main-brain (8050)
→ BBB Input Filter — Phase 1.4 (allis-blood-brain-barrier:8016)
→ Phase 1.45 — Community Memory (autonomous_learner, top-5)
→ RAG (text + GIS + landowner + WV-entangled + registry, WV-first)
→ LLM Ensemble (allis-ollama:11434)
→ Judge Pipeline — judge_pipeline_v2.1-rag-grounded
→ BBB Output Filter (allis-bbb-output-filter — internal:8017)
→ UltimateResponse (architecture_layers=7, truthverdict.*)
```

is live and serving West Virginia benefits, geography, and land ownership questions.

> **⚠️ Embedding Model Lock — Confirmed April 23, 2026:**
> All ChromaDB collections use **384-dimensional vectors** produced by
> **`all-minilm:latest`**. The `nomic-embed-text` model produces
> **768-dimensional vectors** and is **incompatible** with all existing collections.
> Any service, script, or migration that generates embeddings for ChromaDB **must** use
> `all-minilm:latest`. The `allis-gbim-query-router` landowner path does **not** use
> embeddings — it routes directly to PostgreSQL.

> **★★ Security posture — confirmed April 23, 2026:** All services bound to
> `127.0.0.1` or internal Docker DNS. Zero `0.0.0.0` exposures. `_auth()` confirmed
> on all sensitive routes. `ALLIS_API_KEY` env var confirmed set in production.

> **★★ ChromaDB API and Port — confirmed April 23, 2026:**
> ChromaDB (`allis-chroma`) is running the **v2 multi-tenant API**. Host port:
> **8002** (`127.0.0.1:8002→8000/tcp`). Container-internal port: **8000**.
> Inter-service URL: `allis-chroma:8000`. The `/api/v1/` endpoints return
> `410 Gone`.

> **★★ Database architecture — two-container — confirmed April 23, 2026:**
> `msallisgis` is accessible via two containers:
> - **Production** — `msallis-db`, host port **5433** (container 5432), role
>   `postgres`, 16 GB / 294 tables / 11 schemas
> - **Forensic** — `postgis-forensic`, host port **5432**, role `allis`
>   (+ `-h 127.0.0.1`), `msallisgis`, 17 GB / 314 tables / 9 schemas
>
> `mvw_gbim_landowner_spatial` — **✅ 38,979 rows in msallis-db. Not present in
> postgis-forensic.**

> **★★ ChromaDB v2 — ChromaDB API version:**
> ⚠️ `/api/v1/` returns `410 Gone`. Use `/api/v2/` full path only.
> UUID two-step count pattern required (see `05-chromadb-semantic-memory.md`).

```
┌─────────────────────────────────────────────────────────────┐
│            Ms. Allis RAG Pipeline Architecture               │
│            ★★ April 23, 2026 — Production Baseline          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  User Query                                                  │
│      ↓                                                       │
│  allis-unified-gateway (host:18018 → container:8001)       │
│      ↓                                                       │
│  allis-main-brain (port 8050)                              │
│      ↓                                                       │
│  BBB Input Filter — Phase 1.4                               │
│    allis-blood-brain-barrier:8016                          │
│    [6 filters — barrier_active: true]                       │
│    BLOCKED → architecture_layers=1, truthverdict=null       │
│      ↓ (passes)                                              │
│  Phase 1.45 — Community Memory Retrieval                    │
│    all-minilm:latest (384-dim) → autonomous_learner         │
│    top-5 memories prepended to enhanced_message             │
│    [21,181 items — April 23, 2026]                          │
│      ↓                                                       │
│  Main Brain Orchestration                                   │
│      ├──→ Text RAG (allis-rag-server host:8003→ctr:8003)  │
│      ├──→ GIS RAG v0.4.0 (port 8004)                       │
│      │       204 WV GIS datasets / 7,357 WV bridges         │
│      │       msallis-db: host 5433 / container 5432        │
│      ├──→ GBIM Landowner Router (port 7205)                 │
│      │       PostgreSQL-native → mvw_gbim_landowner_spatial  │
│      │       msallis-db: host 5433 / container 5432        │
│      │       ✅ 38,979 rows — NO ChromaDB                   │
│      ├──→ WV-Entangled Gateway (port 8010) ✅              │
│      │       Static WV context injection via /chat_wv       │
│      ├──→ Web Research (excluded for WV queries)            │
│      └──→ Registry (allis-local-resources-db port 5435)   │
│      ↓                                                       │
│  Context Assembly (WV-first for WV queries)                 │
│      ↓                                                       │
│  LLM Ensemble (allis-ollama:11434)                        │
│      ↓                                                       │
│  Judge Pipeline — judge_pipeline_v2.1-rag-grounded ✅       │
│    nbb_pituitary_gland:8108→80 — mode: baseline             │
│    allis-qualia-engine (internal:8017, DNS only)           │
│      ↓                                                       │
│  BBB Output Filter                                          │
│    allis-bbb-output-filter (internal:8017)                 │
│    {"status":"ok","service":"bbb-output-filter"} ✅         │
│      ↓                                                       │
│  UltimateResponse                                           │
│    { architecture_layers: 7, truthverdict: {                │
│        consensus_score: 0.95,                               │
│        validated_by:                                        │
│          "judge_pipeline_v2.1-rag-grounded" } }             │
│                                                              │
│  Background (async, 24h cycle):                             │
│  allis-ingest-watcher                                      │
│    → services.confidence_decay_loop                         │
│    → msallisgis on msallis-db (host 5433 / ctr 5432)      │
│    → Redis escalation (allis-redis:6379)                   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> Figure 6-1. RAG pipeline overview — April 23, 2026 production baseline.
> `allis-unified-gateway` (host:**18018** → container:**8001**) is the external entry
> point. `allis-main-brain` (port **8050**) is the primary orchestrator. The confidence
> decay loop runs as a background async service inside `allis-ingest-watcher` on a
> 24-hour cycle against `msallisgis` on `msallis-db` (host 5433). Namespace:
> `msallis-rebuild`. Container prefix: `allis-`.

---

## 6.2 Alignment with GBIM, Hilbert Space, Semantic Memory, GeoDB, and Registries

The GeoBelief Information Model (GBIM) defines how entities, places, and normative
claims are represented across documents and spatial features. The `msallisgis` database
is the authoritative spatial body, accessible via two containers:
- **`msallis-db`** (production — host 5433 / container 5432 — 16 GB / 294 tables /
  11 schemas)
- **`postgis-forensic`** (forensic — host 5432 — 17 GB / 314 tables / 9 schemas)

As of March 20, 2026, GBIM beliefs include 20,593 landowner records
(`LANDOWNER_CORPORATE` and `LANDOWNER_GOVERNMENT` proposition codes) ingested from the
WV assessor corpus and materialized in `mvw_gbim_landowner_spatial` in `msallis-db`
(production). **✅ 38,979 rows in msallis-db. Not present in postgis-forensic.**
These landowner beliefs are accessed via a dedicated PostgreSQL-native path through
`allis-gbim-query-router` (port 7205).

The ChromaDB collection `gbim_worldview_entities` (L2 distance) is the primary spatial
semantic subspace of \(H_{\text{App}}\) — 5,416,521 records confirmed live April 23,
2026. The collection `gbim_beliefs_v2` (cosine distance) holds 5,000 production GBIM
belief embeddings. The bare `gbim_beliefs` collection is **retired** and must not be
used in any new code or documentation.

**Database Integration — ★★ Confirmed April 23, 2026:**

```python
import psycopg2
import chromadb

# Production: msallis-db — host 5433 / container 5432 / database msallisgis
# Use for: GBIM belief graph, spatial queries, landowner routing, decay loop
pg_conn_production = psycopg2.connect(
    host="localhost", port=5433,
    database="msallisgis", user="postgres", password="postgres"
)

# Forensic: postgis-forensic — host 5432 / role allis / database msallisgis
# Use for: forensic auditing, migration validation, schema inspection
# mvw_gbim_landowner_spatial is NOT present in this container
pg_conn_forensic = psycopg2.connect(
    host="127.0.0.1", port=5432,
    database="msallisgis", user="allis", password="<allis_password>"
)

# allis-local-resources-db — port 5435
# database name is "postgres" (not the container name)
pg_conn_resources = psycopg2.connect(
    host="localhost", port=5435,
    database="postgres",
    user="postgres", password="postgres"
)

# allis-chroma: host 8002 / container 8000
# all-minilm:latest (384-dim) — DO NOT use nomic-embed-text (768-dim)
# /api/v2/ only — /api/v1/ returns 410 Gone
chroma_client = chromadb.HttpClient(host="127.0.0.1", port=8002)
```

**psql access patterns:**

```bash
# Production: msallis-db
docker exec msallis-db psql -U postgres -d msallisgis

# Forensic: postgis-forensic
docker exec postgis-forensic psql -h 127.0.0.1 -U allis -d msallisgis
```

---

## 6.3 Core RAG and Search Components

At the implementation level, the retrieval layer consists of Phase 1.45 community
memory retrieval, four main retrieval services, a GBIM landowner router, a registry
resolver, a live confidence decay loop, and orchestration:

```
┌─────────────────────────────────────────────────────────────┐
│          Core Ms. Allis RAG Components                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Phase 1.45 — Community Memory Retrieval             │  │
│  │  -  Embedding: all-minilm:latest (384-dim)           │  │
│  │  -  Source: allis-ollama:11434/api/embeddings       │  │
│  │  -  Collection: autonomous_learner (21,181 items)    │  │
│  │  -  Top-5 results prepended to enhanced_message      │  │
│  │  -  Fires after BBB input filter, before text RAG    │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Text RAG Service                                    │  │
│  │  allis-rag-server: host:8003 → container:8003       │  │
│  │  -  ChromaDB backend (allis-chroma, host port 8002) │  │
│  │  -  Embedding: all-minilm:latest (384-dim)           │  │
│  │  -  Collections: local_resources (default),          │  │
│  │    governance_rag, commons_rag, thesis, research,    │  │
│  │    msallis_docs, mountainshares_knowledge,           │  │
│  │    conversation_history, episodic_index,             │  │
│  │    ms_allis_memory, gbim_beliefs_v2 (cosine)        │  │
│  │  -  Metadata filters: county, source, worldview      │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  GIS RAG Service v0.4.0 (port 8004)                  │  │
│  │  -  204 WV GIS datasets                              │  │
│  │  -  7,357 WV bridges                                 │  │
│  │  -  PostgreSQL source: msallis-db                   │  │
│  │     host 5433 / container 5432 / database msallisgis│  │
│  │  -  ChromaDB spatial collections (host port 8002)    │  │
│  │  -  Collections: gbim_worldview_entities (L2),       │  │
│  │    gis_wv_benefits,                                  │  │
│  │    geospatialfeatures (60,875 items)                 │  │
│  │    GBIM_Fayette_sample (1,535 items)                 │  │
│  │  -  Returns: centroids, GBIM IDs, spatial metadata   │  │
│  │  -  Embedding: all-minilm:latest (384-dim)           │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  GBIM Landowner Router (port 7205)                   │  │
│  │  -  PostgreSQL: msallis-db                          │  │
│  │     host 5433 / container 5432 / database msallisgis│  │
│  │  -  View: mvw_gbim_landowner_spatial                  │  │
│  │     ✅ 38,979 rows — msallis-db only                │  │
│  │     NOT present in postgis-forensic                  │  │
│  │  -  Proposition codes: LANDOWNER_CORPORATE,          │  │
│  │    LANDOWNER_GOVERNMENT                              │  │
│  │  -  RBAC-gated: X-Allis-Role required                │  │
│  │  -  NO ChromaDB — PostgreSQL-native path only        │  │
│  │  -  Returns: ranked owner names, parcel counts,      │  │
│  │    area (km²), county, proposition code              │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Confidence Decay Loop (background, 24h cycle)       │  │
│  │  -  Service: allis-ingest-watcher                   │  │
│  │  -  Target: msallisgis on msallis-db               │  │
│  │     host 5433 / container 5432                       │  │
│  │  -  NOT postgis-forensic                             │  │
│  │  -  Reset path: reverify_*() → decay=1.0             │  │
│  │  -  Escalation: allis-redis (redis:7-alpine)        │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Web Research Gateway                                │  │
│  │  -  Rate-limited external search                     │  │
│  │  -  Excluded for WV-scoped queries                   │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Local Resource Registry Resolver                    │  │
│  │  -  allis-local-resources-db (port 5435)            │  │
│  │  -  database: "postgres" (NOT the container name)    │  │
│  │  -  Filters: county, ZIP, resource_type              │  │
│  │  -  Returns: verified program records                │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> Figure 6-2. Core retrieval components. `allis-rag-server` confirmed
> host:8003→container:8003. GIS-RAG v0.4.0 confirmed at port 8004 — 204 WV GIS
> datasets, 7,357 WV bridges. Landowner router targets `msallis-db` (host 5433 /
> container 5432); `mvw_gbim_landowner_spatial` is present in `msallis-db` only —
> ✅ 38,979 rows.

---

### 6.3.0 Phase 1.45 — Semantic Community Memory Retrieval

Phase 1.45 fires after the BBB input filter approves the query and before the main text
and GIS RAG services. It is the first retrieval step that enriches `enhanced_message`.

**How it works:**

1. `allis-main-brain` calls `allis-ollama:11434/api/embeddings` with model
   `all-minilm:latest` and the user query as the prompt, receiving a 384-dimensional
   embedding vector.
2. The embedding is used to query the `autonomous_learner` ChromaDB collection (L2,
   21,181 items) via the v2 API (`allis-chroma`, host port 8002).
3. The 5 most semantically similar community interaction records are retrieved.
4. The retrieved memories are prepended to `enhanced_message` before it reaches the LLM
   ensemble.

```python
import httpx
import chromadb

# Step 1: Generate 384-dim embedding
# allis-ollama host port 11434
response = httpx.post(
    "http://localhost:11434/api/embeddings",
    json={"model": "all-minilm:latest", "prompt": user_query}
)
embedding = response.json()["embedding"]  # must be 384-dim

# Step 2: UUID two-step count pattern — required for v2
# allis-chroma: host 8002 / container 8000
client = chromadb.HttpClient(host="localhost", port=8002)
col = client.get_collection("autonomous_learner")  # L2 distance

# Step 3: Query top-5
results = col.query(
    query_embeddings=[embedding],
    n_results=5,
    include=["documents", "metadatas", "distances"]
)

# Step 4: Prepend to enhanced_message
community_memories = "\n".join(results["documents"])
enhanced_message = community_memories + "\n\n" + original_message
```

> **Critical:** Embedding model **must** be `all-minilm:latest` (384-dim). Using
> `nomic-embed-text` (768-dim) will cause a dimension mismatch error against all
> existing ChromaDB collections.

---

### 6.3.1 Text RAG Service (ChromaDB-Backed)

The text RAG service takes a query string, a `top_k` parameter, optional metadata
filters (collection, source, county, dataset, worldview), and optional role and
geography hints. It issues similarity searches against one or more ChromaDB collections
using **`all-minilm:latest` (384-dimensional embeddings)**.

> **★★ Port confirmed April 23, 2026:** `allis-rag-server` maps **host:8003 →
> container:8003**. Both host and container ports are **8003**.

**Active collections for text RAG — ★★ UPDATED April 23, 2026:**

| Collection | Items | Distance | Purpose |
|---|---|---|---|
| `local_resources` | 101 | cosine | **Default** — community queries; verified Fayette County resource data |
| `autonomous_learner` | **21,181** | **L2** | Community interaction memories — queried at Phase 1.45 |
| `gbim_worldview_entities` | 5,416,521 | **L2** | Complete WV GBIM spatial corpus |
| `gbim_beliefs_v2` | 5,000 | **cosine** | GBIM belief embeddings — production semantic layer |
| `gis_wv_benefits` | 4,668 | **L2** | WV benefits facilities |
| `governance_rag` | 1,367 chunks | cosine | MountainShares DAO corpus + US + WV constitutions |
| `commons_rag` | 306 chunks | cosine | Commons governance + gamification |
| `psychological_rag` | 6,860 | cosine | Mental health corpus |
| `appalachian_cultural_intelligence` | 820 | cosine | Appalachian cultural context |
| `aaacpe_corpus` | 65 docs | cosine | AaaCPE live web scrape — `allis-aaacpe-scraper` port 8033, 39 sources |
| `spiritual_rag` | 368,238 | cosine | Mother Carrie Protocol corpus — deduplicated |
| `geospatialfeatures` | 60,875 | **L2** | GIS feature embeddings |
| `GBIM_Fayette_sample` | 1,535 | **L2** | Fayette County sample |
| `ms_allis_memory` | — | cosine | Monitoring — HTTP 500 on count (OI-C4-500) |
| `mountainshares_knowledge` | — | cosine | MountainShares governance |
| `episodic_index` | — | cosine | Episodic memory index |
| `conversation_history` | 580 | cosine | Conversation history — wired in production |
| `GBIM_sample_rows` | 5,000 | **L2** | GBIM test sample |
| `msallis_docs` | 28,327 | cosine | System docs + verified WV community resources |

> **`gbim_beliefs` (bare) is retired.** Use `gbim_worldview_entities` (L2) for spatial
> corpus or `gbim_beliefs_v2` (cosine) for semantic belief embeddings.
> See `05-chromadb-semantic-memory.md` for the full 48-collection metric table.

---

### 6.3.2 GIS RAG Service v0.4.0 (port 8004)

The GIS RAG service is a dedicated geospatial retrieval path that serves West
Virginia-focused spatial questions. As of April 23, 2026, GIS-RAG v0.4.0 covers:

- **204 WV GIS datasets**
- **7,357 WV bridges**

It queries:

- `gbim_worldview_entities` (L2) — 5,416,521 embeddings of West Virginia geospatial
  features from `msallisgis` on `msallis-db`
- `gis_wv_benefits` (L2) — semantic descriptions and metadata for benefits-related
  facilities such as Oak Hill hubs and Beckley DHHR offices
- `geospatialfeatures` (L2) — 60,875 items
- `GBIM_Fayette_sample` (L2) — 1,535 items

Each indexed entity stores a short text description and metadata fields including
`worldview_id`, `dataset`, `county`, `gbim_entity`, `centroid_x`, and `centroid_y`
(SRID 26917, also transformed to EPSG:4326). Metadata links back to
`msallisgis.gbim_entities` on `msallis-db` (host 5433 / container 5432) and
`msallisgis.zcta_wv_centroids` (993 WV ZIP centroids).

PostgreSQL source access (production):

```bash
# GIS RAG source queries — always target msallis-db (production)
docker exec msallis-db psql -U postgres -d msallisgis \
  -c "SELECT zip, lat, lon FROM zcta_wv_centroids WHERE zip = '25880';"
```

> **Routing distinction:** The GIS RAG service handles spatial feature questions
> requiring semantic similarity matching (e.g., "hospitals near Oak Hill").
> Landowner/parcel ownership questions are routed through the GBIM Landowner Router
> (port 7205, §6.3.3). The GIS RAG service does not query `mvw_gbim_landowner_spatial`.

---

### 6.3.3 GBIM Landowner Router (`allis-gbim-query-router`, port 7205)

> **Architectural guarantee:** Landowner and parcel ownership queries in Ms. Allis are
> **always** resolved through PostgreSQL-native SQL aggregation via
> `allis-gbim-query-router` (port 7205) against `msallis-db` (host 5433 / container
> 5432). They are **never** routed through ChromaDB vector similarity search.
>
> `mvw_gbim_landowner_spatial` — **✅ 38,979 rows in msallis-db. Not present in
> postgis-forensic.**

Ownership aggregation questions such as "who are the largest landowners in West
Virginia?" are structurally relational — they require exact grouping, counting, and area
summation over verified belief records, not semantic approximation. This aligns with
**P16 – Power accountable to place**.

```python
LANDOWNER_PATTERNS = [
    "landowner", "who owns", "largest owner",
    "owns the most land", "parcel ownership", "land ownership"
]

def route_query(query: str, mode: str) -> str:
    if mode == "landowner_gbim" or any(p in query.lower() for p in LANDOWNER_PATTERNS):
        return "allis-gbim-query-router"  # SQL aggregation — port 7205 — NO ChromaDB
    return "rag_stack"                      # ChromaDB path — port 8003/8002
```

**Verified query pattern — statewide top landowners:**

```bash
curl -s http://127.0.0.1:7205/query \
  -H "Content-Type: application/json" \
  -H "X-Allis-Role: researcher" \
  -d '{
    "question": "Who are the largest landowners in West Virginia?",
    "mode": "landowner_gbim",
    "route_type": "parcel_ownership",
    "scope": "statewide",
    "limit": 20
  }'
```

Underlying SQL against `mvw_gbim_landowner_spatial` on `msallis-db`:

```sql
SELECT
    who_axis->>'canonical_entity_name'  AS owner,
    proposition_code,
    COUNT(*)                             AS parcel_count,
    ROUND(SUM(ST_Area(geom::geography)/1e6)::numeric, 2) AS area_km2
FROM mvw_gbim_landowner_spatial
WHERE proposition_code IN ('LANDOWNER_CORPORATE', 'LANDOWNER_GOVERNMENT')
GROUP BY owner, proposition_code
ORDER BY area_km2 DESC NULLS LAST
LIMIT 20;
```

**psql equivalent:**

```bash
docker exec msallis-db psql -U postgres -d msallisgis \
  -c "SELECT COUNT(*) FROM mvw_gbim_landowner_spatial;"
# Returns: 38979
```

Verified results (March 20, 2026):
- UNITED STATES OF AMERICA ~662,191 acres (`LANDOWNER_GOVERNMENT`)
- WEYERHAEUSER COMPANY ~242,892 acres (`LANDOWNER_CORPORATE`)

The `allis-gbim-query-router` queries only rows with
`proposition_code IN ('LANDOWNER_CORPORATE', 'LANDOWNER_GOVERNMENT')`. Individual
residential owner names are not present in `mvw_gbim_landowner_spatial` and cannot be
returned — this is a structural guarantee, not a runtime filter.

---

### 6.3.4 Confidence Decay Loop — Live Production Service

The confidence decay and reverification loop (`services.confidence_decay_loop`) runs as
a persistent async scheduled task inside `allis-ingest-watcher`. It operates against
**`msallisgis` on `msallis-db`** (host 5433 / container 5432) — **not
`postgis-forensic`** — and processes all tracked GBIM entities per 24-hour cycle.

| Parameter | Value |
|---|---|
| Service container | `allis-confidence-decay` |
| Target database | `msallisgis` on `msallis-db` (host 5433 / container 5432) |
| Target table | `msallisgis.public.gbim_entities` |
| Cycle interval | 86400s (24 hours) |
| Redis container | `allis-redis` (image: `redis:7-alpine`) |
| Escalation consumer | `services/allis_decay_escalation_consumer.py` |

```python
# services/confidence_decay_loop.py
# Target: msallisgis on msallis-db (host 5433 / container 5432)
# NOT postgis-forensic

import asyncio
import psycopg2

DECAY_RATE = 0.01
FLAG_THRESHOLD = 0.5
CYCLE_INTERVAL = 86400

async def run_decay_cycle():
    # Production container: msallis-db, host 5433 / container 5432
    conn = psycopg2.connect(
        host="localhost", port=5433,
        database="msallisgis",
        user="postgres", password="postgres"
    )
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE gbim_entities
        SET confidence_decay = GREATEST(0, confidence_decay - %s)
        WHERE confidence_decay > 0
    """, (DECAY_RATE,))

    cursor.execute("""
        UPDATE gbim_entities
        SET needs_reverification = true
        WHERE confidence_decay < %s
          AND needs_reverification = false
    """, (FLAG_THRESHOLD,))

    cursor.execute("SELECT COUNT(*) FROM gbim_entities")
    total = cursor.fetchone()

    cursor.execute(
        "SELECT COUNT(*) FROM gbim_entities WHERE needs_reverification = true"
    )
    flagged = cursor.fetchone()

    conn.commit()
    conn.close()

    print(f"Decay applied to {total} entities. {flagged} below flag threshold.")
    if flagged == 0:
        print("No entities below flag threshold. Cycle complete.")
    print(f"Next cycle in {CYCLE_INTERVAL}s")
    await asyncio.sleep(CYCLE_INTERVAL)

async def reverify_entity(entity_id: str, confirmed: bool):
    """Reset decay when source confirms entity still valid."""
    conn = psycopg2.connect(
        host="localhost", port=5433,
        database="msallisgis",
        user="postgres", password="postgres"
    )
    cursor = conn.cursor()
    if confirmed:
        cursor.execute("""
            UPDATE gbim_entities
            SET confidence_decay = 1.0,
                reverification_result = 'confirmed',
                needs_reverification = false
            WHERE entity_id = %s
        """, (entity_id,))
    conn.commit()
    conn.close()
```

---

## 6.4 Retrieval Flows

### 6.4.1 Non-Spatial RAG Flow

**Query intake.** A user or upstream component sends a request through
`allis-unified-gateway` (host:**18018** → container:**8001**) to `allis-main-brain`
(port **8050**).

**Phase 1.45 — Community memory retrieval.** Before any other RAG service is invoked,
the main brain embeds the query via `all-minilm:latest` (384-dim) and retrieves the
top-5 most similar records from `autonomous_learner` (L2, 21,181 items, `allis-chroma`
host port **8002**). These are prepended to `enhanced_message`.

**Routing to text RAG and/or web.** For governance- and thesis-style questions, the
orchestration prefers ChromaDB-backed collections (`governance_rag`, `commons_rag`,
thesis, GBIM collections) and only consults the web when the question clearly depends on
external or time-varying facts.

**Retrieval from ChromaDB.** The text RAG service embeds the query, runs similarity
search against selected collections, and returns high-scoring documents and their
metadata.

**Generation and judging.** The LLM ensemble (`allis-ollama:11434`) generates the
candidate answer. `judge_pipeline_v2.1-rag-grounded` validates it, then the BBB output
filter (`allis-bbb-output-filter`, internal:8017) applies post-hoc guardrails. A healthy
full-stack response returns `architecture_layers = 7`,
`truthverdict.consensus_score ≥ 0.95`.

---

### 6.4.2 Spatial RAG Flow

```
┌─────────────────────────────────────────────────────────────┐
│   Spatial RAG: Semantic + Geographic Retrieval               │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Query type determination:                                  │
│    - Spatial feature question → GIS RAG v0.4.0              │
│        (ChromaDB allis-chroma:8002 +                       │
│         msallis-db: host 5433 / container 5432)            │
│    - Ownership/landowner question →                         │
│        allis-gbim-query-router (port 7205)                 │
│        PostgreSQL-native, msallis-db only                  │
│        mvw_gbim_landowner_spatial ✅ 38,979 rows            │
│        NOT in postgis-forensic                              │
│                                                              │
│  Semantic Retrieval (allis-chroma host port 8002)          │
│  ┌────────────────────────────────────────────────┐         │
│  │  Query: "hospitals near Oak Hill"              │         │
│  │  Embed query (all-minilm:latest, 384-dim)      │         │
│  │  → Search gis_wv_benefits (L2) +               │         │
│  │    gbim_worldview_entities (L2) +              │         │
│  │    geospatialfeatures (L2, 60,875 items) +     │         │
│  │    GBIM_Fayette_sample (L2, 1,535 items)       │         │
│  └────────────────────────────────────────────────┘         │
│              ↓                                               │
│  Geographic Filtering (msallis-db, host 5433)              │
│  ┌────────────────────────────────────────────────┐         │
│  │  docker exec msallis-db psql -U postgres      │         │
│  │    -d msallisgis                              │         │
│  │  SELECT zip, lat, lon                          │         │
│  │    FROM zcta_wv_centroids                      │         │
│  │    WHERE zip = '25880'  -- Mount Hope          │         │
│  │  Then: spatial filter within 10-mile radius    │         │
│  └────────────────────────────────────────────────┘         │
│              ↓                                               │
│  Combined Results → LLM Context                             │
│                                                              │
│  ─────────────────────────────────────────────────          │
│  LANDOWNER PATH (bypasses all ChromaDB steps above)         │
│  ┌────────────────────────────────────────────────┐         │
│  │  Query: "Who owns the most land in Fayette?"   │         │
│  │  → Detected as landowner_gbim mode             │         │
│  │  → Route to allis-gbim-query-router (7205)   │         │
│  │  → SQL over mvw_gbim_landowner_spatial         │         │
│  │    on msallis-db (host 5433 / ctr 5432)       │         │
│  │  → ✅ 38,979 rows — NOT in postgis-forensic    │         │
│  │  → No embeddings. No ChromaDB. Exact SQL.      │         │
│  └────────────────────────────────────────────────┘         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> Figure 6-3. Spatial RAG flow. All production PostgreSQL access targets `msallis-db`
> (host 5433 / container 5432). `postgis-forensic` is forensic-only and does not contain
> `mvw_gbim_landowner_spatial`. GIS-RAG v0.4.0 covers 204 WV GIS datasets and 7,357 WV
> bridges.

---

### 6.4.3 Resource-Oriented RAG Flow

**Resource query intake.** The main brain receives the question and identifies it as a
resource-oriented request, extracting any available location hints (ZIP, county, town)
and population signals.

**Phase 1.45 — Community memory.** Top-5 `autonomous_learner` (L2) memories are
prepended.

**Interpretation via text and spatial RAG.** Text RAG and/or GIS RAG v0.4.0 retrieve
resource guides, flyers, benefits facilities, or prior notes. These hits may carry
`local_resource_id` and `county` metadata linking them to `allis-local-resources-db`.

**Resolution via local resource resolver.** Queries `allis-local-resources-db`
(port **5435**, database: `postgres`). As of April 23, 2026: 101 embeddings present;
Fayette pipeline active.

**Context assembly and generation.** The orchestration layer builds a context from
unstructured descriptions and structured `allis-local-resources-db` fields. The LLM
ensemble applies the Ms. Egeria Allis persona.

---

## 6.5 Routing, Roles, Geography, and WV-First Policy

### 6.5.1 Design Intent

| Query type | Primary routing target |
|---|---|
| Governance, policy, thesis | Text RAG (ChromaDB — `governance_rag`, `commons_rag`, thesis, GBIM collections) |
| Spatial features, facilities | GIS RAG v0.4.0 (ChromaDB + `msallis-db`, host 5433) — 204 datasets, 7,357 bridges |
| Land ownership, landowners | `allis-gbim-query-router` (port 7205) — `msallis-db` only — ✅ 38,979 rows |
| Belief quality / decay status | `msallisgis.public.gbim_entities` via decay loop (`msallis-db`, host 5433) |
| Resource and referral | Text RAG + `allis-local-resources-db` resolver (port 5435) |
| System status | Internal orchestration |

**WV-first behavior.** For West Virginia, whenever a query is WV-scoped, the system
treats WV RAG, `msallis-db` GIS, GBIM landowner beliefs, and registry context as the
authoritative sources, and excludes web context. Under `nbb_pituitary_gland`
`mode=baseline` (confirmed April 23, 2026), WV exclusion of web context is **mandatory**.

### 6.5.2 Service Routing Table — ★★ April 23, 2026

| Service | Host Port | Container Port | Notes |
|---|---|---|---|
| `allis-unified-gateway` | **18018** | **8001** | ✅ External entry |
| `allis-main-brain` | 8050 | 8050 | ✅ Primary orchestrator |
| `allis-rag-server` | **8003** | **8003** | ✅ Both ports confirmed 8003 |
| GIS RAG v0.4.0 | 8004 | — | ✅ 204 WV GIS datasets / 7,357 WV bridges |
| `allis-psychological-rag` | 8006 | — | ✅ 6,860 docs |
| `allis-wv-entangled-gateway` | 8010 | 8010 | ✅ Static WV injection via `/chat_wv` |
| `allis-web-research` | 8008 (internal) | — | ✅ Restored |
| `allis-ingest-api` | 8009 | — | ✅ Restored |
| `allis-blood-brain-barrier` | 8016 | 8016 | ✅ 6 filters — `barrier_active: true` |
| `allis-bbb-output-filter` | internal | 8017 | ✅ `{"status":"ok","service":"bbb-output-filter"}` |
| `allis-qualia-engine` | internal (DNS only) | 8017 | ✅ `allis-qualia-engine:8017` |
| `allis-consciousness-bridge` | internal | 8020 | ✅ |
| `allis-neurobiological-master` | internal | 8018 | ✅ Internal only |
| `allis-i-containers` | internal | 8015 | ✅ |
| `allis-aaacpe-rag` | 8032 | — | ✅ `aaacpe_corpus` (65 docs, 39 sources) |
| `allis-aaacpe-scraper` | 8033 | — | ✅ Live |
| `allis-gbim-query-router` | 7205 | 7205 | ✅ RBAC-gated — `X-Allis-Role` required |
| `allis-confidence-decay` | internal | — | ✅ Live — 24h cycle |
| `allis-chroma` | **8002** (host) | **8000** (container) | ✅ 48 collections, ~6.74M vectors |
| `nbb_pituitary_gland` | 8108 | 80 | ✅ mode=baseline |
| `msallis-db` (production) | **5433** (host-mapped) | **5432** | ✅ `msallisgis` — 16 GB / 294 tables / 11 schemas |
| `postgis-forensic` (forensic) | **5432** | **5432** | ✅ `msallisgis` — 17 GB / 314 tables / 9 schemas — role `allis` |
| `allis-local-resources-db` | 5435 | 5435 | ✅ 101 embeddings — `database="postgres"` |
| `allis-ollama` | 11434 | 11434 | ✅ `all-minilm:latest` loaded |
| `allis-redis` | internal | 6379 | ✅ `redis:7-alpine` — decay escalation |
| `allis-community-stake-registry` | 8084 | 8084 | ✅ MountainShares stake registry |
| `allis-ms-token-service` | **8088** (host) | **8083** (container) | ✅ Host 8088 ≠ container 8083 |

---

## 6.6 Context Construction and Structure

**Source separation.** The text RAG service returns a `results_by_source` dictionary
keyed by collection name. Phase 1.45 community memories are prepended as a distinct
block. The GIS RAG v0.4.0 service returns dataset names and feature labels traceable to
`msallis-db` (host 5433 / container 5432, database `msallisgis`). The GBIM landowner
router returns structured rows from `mvw_gbim_landowner_spatial` labeled with proposition
codes — ✅ 38,979 rows in `msallis-db`, not present in `postgis-forensic`. The decay
loop provides a continuous quality signal on `gbim_entities` from `msallis-db`. The
local resource resolver returns normalized rows from `allis-local-resources-db`
(port 5435).

**Role-, geography-, and WV-aware scaffolding.** For WV-scoped queries, the ultimate
prompt specifies that WV RAG, `msallis-db` GIS context (host 5433 / container 5432,
database `msallisgis`), GBIM landowner beliefs, and `allis-local-resources-db` are
authoritative; that web snippets are absent; and that the GBIM landowner layer contains
only institutional/government entities.

```
┌─────────────────────────────────────────────────────────────┐
│         Contextual Input Structure for LLM Reasoning        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  System Prompt (role, geography, constraints)               │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Phase 1.45 Community Memories                 │         │
│  │  └─ Top-5 autonomous_learner (L2, 21,181)      │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  WV RAG Context                                │         │
│  │  ├─ governance_rag (1,367 chunks — cosine)     │         │
│  │  ├─ commons_rag (306 chunks — cosine)          │         │
│  │  ├─ Thesis fragments                           │         │
│  │  └─ gbim_beliefs_v2 (5,000 — cosine)           │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  PostgreSQL GIS Context (msallis-db)          │         │
│  │  host 5433 / container 5432 / msallisgis      │         │
│  │  ├─ gbim_worldview_entities (L2, 5,416,521)    │         │
│  │  ├─ gis_wv_benefits (L2, 4,668)               │         │
│  │  ├─ geospatialfeatures (L2, 60,875)            │         │
│  │  ├─ GBIM_Fayette_sample (L2, 1,535)            │         │
│  │  └─ GIS-RAG v0.4.0: 204 datasets / 7,357 bridges│        │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  GBIM Landowner Context (when mode=landowner)  │         │
│  │  └─ mvw_gbim_landowner_spatial                 │         │
│  │     ✅ 38,979 rows — msallis-db only          │         │
│  │     NOT in postgis-forensic                    │         │
│  │     via allis-gbim-query-router (port 7205)   │         │
│  │     PostgreSQL-native — no ChromaDB            │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Registry Context                              │         │
│  │  └─ allis-local-resources-db                  │         │
│  │       port 5435, database: postgres, verified  │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  Grounding Instruction (WV-first for WV queries)            │
│      ↓                                                       │
│  User Query                                                  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> Figure 6-5. Structure of contextual input assembled for language-model reasoning.
> All PostgreSQL production references use `msallis-db` (host 5433 / container 5432 /
> database `msallisgis`). Forensic access uses `postgis-forensic`
> (host 5432, role `allis`).

---

## 6.7 Constraints, Provenance, and Logging

**Decoding-time guards.** After retrieval and generation, the main brain routes candidate
responses through `judge_pipeline_v2.1-rag-grounded` (supersedes
`heuristic_contradiction_v1`), then through the BBB output filter
(`allis-bbb-output-filter`, internal:8017). The BBB output guard is fail-open on HTTP
500 — content passes through unchanged, failure is logged. The confirmed live
`consensus_score` is **0.95** (April 23, 2026).

**Post-hoc review and logging.** Logs capture which services were called, which
collections were queried (with distance metric), which PostgreSQL tables and views were
accessed (including container name, host port, and whether `msallis-db` or
`postgis-forensic` was the source), which `mvw_gbim_landowner_spatial` rows were
returned, Phase 1.45 community memory results, decay status per entity queried, which
filters and scores were applied, which registries were accessed, and which documents or
features were returned.

---

## 6.8 Relation to Long-Term Memory, GeoDB, Registries, and Entanglement

**Long-term memory.** ChromaDB collections (`allis-chroma`, host 8002 / container
8000) hold embedded representations at 384 dimensions (`all-minilm:latest`):
`gbim_worldview_entities` (L2, 5,416,521 entities), `autonomous_learner` (L2, 21,181
items), `gis_wv_benefits` (L2, 4,668), `governance_rag` (cosine, 1,367 chunks),
`commons_rag` (cosine, 306 chunks), `geospatialfeatures` (L2, 60,875 items),
`GBIM_Fayette_sample` (L2, 1,535 items), `gbim_beliefs_v2` (cosine, 5,000), and 38+
additional collections. **48 active collections, ~6.74 million vectors** (April 17,
2026 baseline). Distance metrics: **37 L2 / 11 cosine**. The bare `gbim_beliefs`
collection is retired.

Structured tables in `msallis-db` (host 5433 / container 5432, database `msallisgis`)
hold normalized GBIM belief records. The GBIM landowner materialized view
`mvw_gbim_landowner_spatial` — **✅ 38,979 rows in msallis-db, not present in
postgis-forensic** — holds verified institutional landowner beliefs queryable via
`allis-gbim-query-router` (port 7205). The `allis-local-resources-db` (port 5435,
database `postgres`) holds 101 verified resource records. The decay loop maintains
continuous quality metadata on `msallisgis.public.gbim_entities` via `msallis-db`
— decay applied every 24 hours, `reverify_*()` reset path confirmed live.

**Short-term context.** Each retrieval call assembles a temporary context window from
Phase 1.45 community memories plus retrieved items, sorted by relevance and grouped by
collection, layer, registry, and router. For WV-scoped queries, this window is
explicitly WV-first: assembled from community memories, WV RAG, `msallis-db` GIS
(including GIS-RAG v0.4.0 with 204 datasets and 7,357 bridges), GBIM landowner beliefs
(38,979 rows, `msallis-db`), registry material, and `gbim_entities` decay quality
annotations — with web content excluded.

**Coupled updates and entanglement.** The `autonomous_learner` collection's growth
represents one axis of the coupled update loop. The confidence decay loop running against
`msallis-db` (host 5433) represents a second axis: as WV assessor data is refreshed
and `reverify_*()` confirms entities in source, decay resets to 1.0 and the belief layer
reflects current ground truth.

---

## 6.9 `nbb_pituitary_gland` — Upstream RAG Routing Modulation

> **Cross-reference:** Full neurobiological architecture of `nbb_pituitary_gland` is
> documented in **Chapter 13 (Neurobiological Bridge)** and **Chapter 15 (Governance
> Protocol Stack)**. This section documents only the RAG routing modulation surface
> relevant to the pipeline described in this chapter.

The `nbb_pituitary_gland` service (host port **8108** → container port **80** —
✅ `mode=baseline` confirmed April 23, 2026) acts as the **upstream modulator** of
RAG routing weights in the Ms. Allis pipeline.

**Confirmed live state — April 23, 2026:**

```bash
curl -s http://127.0.0.1:8108/health
# Returns:
# {"status":"healthy","service":"nbb_pituitary_gland","mode":"baseline"}
```

**What `mode=baseline` means for RAG routing:**

| Behavior | Baseline mode |
|---|---|
| WV RAG | Mandatory — web context excluded for WV queries |
| Landowner pattern detection | Standard sensitivity |
| BBB input threshold | Standard |
| Judge pipeline `consensus_score` floor | Standard (0.95) |
| WV-entangled context injection | Applied via `/chat_wv` |
| Decay loop quality signal | Available in context assembly |

> **See Chapter 15** for the governance protocol stack and full five-protocol
> specification. **See Chapter 13** for the full neurobiological bridge architecture.

---

## 6.10 Production State Summary — ★★ April 23, 2026

**Security posture:**
- All services bound to `127.0.0.1` or internal Docker DNS ✅
- Zero `0.0.0.0` exposures ✅
- `ALLIS_API_KEY` env var confirmed set ✅

**ChromaDB (`allis-chroma`) — April 23, 2026:**
- Host port: **8002** / container port: **8000** ✅
- API: v2 only — `/api/v1/` returns `410 Gone` ✅
- Active collections: **48** ✅
- Total vectors: **~6.74 million** (April 17, 2026 baseline) ✅
- Distance metrics: **37 L2 / 11 cosine** ✅
- Embedding model: `all-minilm:latest` (384-dim) — all collections locked ✅
- `gbim_beliefs` (bare) retired ✅

**PostgreSQL — two-container architecture — April 23, 2026:**

| Container | Host Port | Container Port | Database | Size | Tables | Schemas | Role |
|---|---|---|---|---|---|---|---|
| `msallis-db` (production) | **5433** | **5432** | `msallisgis` | 16 GB | 294 | 11 | `postgres` |
| `postgis-forensic` (forensic) | **5432** | **5432** | `msallisgis` | 17 GB | 314 | 9 | `allis` |

- `mvw_gbim_landowner_spatial` — **✅ 38,979 rows in msallis-db. Not present in
  postgis-forensic.** ✅
- Port **5452** — invalid, never existed in production ✅
- `allis-local-resources-db` — port **5435** — 101 embeddings — `database="postgres"` ✅

**GIS-RAG v0.4.0 (port 8004):**
- 204 WV GIS datasets ✅
- 7,357 WV bridges ✅
- Source: `msallis-db` (host 5433 / container 5432 / database `msallisgis`) ✅

**RAG and routing:**
- Phase 1.45 community memory: live — 21,181 items (`autonomous_learner`, L2) ✅
- Text RAG (`allis-rag-server` host:8003 → container:8003) ✅
- `allis-gbim-query-router` (port 7205): RBAC-gated, PostgreSQL-native landowner
  path live ✅
- `allis-community-stake-registry` (port 8084) ✅
- `allis-ms-token-service` (host 8088 / container 8083) ✅

**Judge pipeline:**
- `judge_pipeline_v2.1-rag-grounded` confirmed live ✅
- `heuristic_contradiction_v1` superseded ✅
- `consensus_score`: 0.95 confirmed ✅
- `architecture_layers`: 7 (healthy full-stack) ✅

**Namespace and naming:**
- Narrative prose namespace: `msallis-rebuild` ✅
- Container prefix: `allis-` (retained in production stack) ✅
- Public name: Ms. Allis ✅

---

*Chapter 6 — Last updated: April 23, 2026, Mount Hope WV — Carrie Kidd (Mamma Kidd)*

*Two-container database architecture documented: `msjarvis-db` (production, host 5433 /
container 5432, role postgres, msjarvisgis, 16 GB / 294 tables / 11 schemas) and
`postgis-forensic` (forensic, host 5432, role allis, msjarvisgis, 17 GB / 314 tables /
9 schemas). `mvw_gbim_landowner_spatial` — ✅ 38,979 rows in msjarvis-db, not present
in postgis-forensic. All code blocks updated: msjarvisgis throughout. GIS-RAG v0.4.0
(port 8004): 204 WV GIS datasets, 7,357 WV bridges. gbim_worldview_entities (L2) /
gbim_beliefs_v2 (cosine) canonical; gbim_beliefs (bare) retired. msjarvis-rebuild
namespace; jarvis- container prefix retained. ChromaDB v2 only; /api/v1/ returns 410
Gone; UUID two-step count pattern required. Preflight gate 30/30 exit 0 April 23, 2026.*
