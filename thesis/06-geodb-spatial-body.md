# 6. GeoDB Spatial Body

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*

## Why This Matters for Polymathmatic Geography

This chapter specifies how Ms. Allis's language models are bound to *place‑aware, collection‑aware, and registry‑aware memory* instead of free‑floating text generation. It makes the Hilbert‑space representation, GBIM structures, ChromaDB‑backed semantic memory, and the verified local resource registry from earlier chapters operational by defining concrete services that retrieve from semantic memory, the spatial body, the web, and structured program tables. In the current deployment, this design is realized as a production RAG stack that delivers West Virginia benefits intelligence through a multi-model consciousness bridge anchored in ChromaDB, GBIM‑derived entities from the PostgreSQL `msallis` and `msallisgis` databases (both in the `postgis-forensic` container, **port 5432** — confirmed April 17, 2026), GIS‑aware collections, and a WV‑first routing policy. It supports:

- **P1 – Every where is entangled** by requiring that answers emerge from an entangled memory of governance texts, spatial layers, research notes, belief structures from PostgreSQL GBIM tables, and local resource registries, rather than from an abstract model prior.
- **P3 – Power has a geometry** by letting retrieval paths expose which collections—and thus which institutional, spatial, and programmatic perspectives—shape a given answer, including WV‑specific benefits facilities in `gis_wv_benefits`, spatial entities derived from PostgreSQL GBIM and `msallisgis`, benefits‑focused resource collections, and the GBIM landowner belief layer (`mvw_gbim_landowner_spatial`) that makes corporate and government land ownership computable and queryable by natural language.
- **P5 – Design is a geographic act** by treating routing rules, collection choices, registry lookups, and gateway boundaries as design decisions that change how the system "sees" and acts within a region — including the explicit decision to route landowner queries through a PostgreSQL-native path rather than through vector similarity search.
- **P12 – Intelligence with a ZIP code** by privileging West Virginia‑specific collections in retrieval, and by coupling text RAG both to a state‑scale PostgreSQL `msallisgis` spatial body (port **5432**, `postgis-forensic` container — 95 GB, 742 tables, 9 schemas) and `msallis` GBIM application layer (port **5432**, same container — 92 tables, 5,416,521 verified beliefs) for spatial questions and to a ZIP‑ and county‑aware `allis-local-resources-db` registry (port 5435) for concrete program referrals, including flows for Mount Hope, Oak Hill, Beckley, and broader Fayette/Raleigh County.
- **P16 – Power accountable to place** by making retrieval calls, filters, scores, registry lookups, and sources visible at the API and logging layer so that communities and researchers can audit what informed a Steward response — and by making the `gbim_query_router` landowner path explicitly inspectable as a structured SQL aggregation over verified GBIM belief records rather than an opaque embedding similarity result.

As such, this chapter belongs to the **Computational Instrument** tier: it defines the retrieval and routing machinery that connects ChromaDB‑backed semantic memory (host port **8002**, container port **8000**), the PostgreSQL GBIM/`msallisgis` spatial body (5,416,521 verified beliefs, 742 PostGIS tables, port **5432**), the verified local resource registry (`allis-local-resources-db`, port 5435), the GBIM landowner belief layer (`mvw_gbim_landowner_spatial`, routed via `gbim_query_router` port 7205), the live confidence decay and reverification loop, and web research to the live outputs of Ms. Allis.

> **⚠️ Port 5452 DEPRECATED — OI-C6-1 CLOSED April 17, 2026**
> Port **5452** was a stale, never-active reference. It has **never** corresponded to a live container in any production build. Both `msallisgis` and `msallis` are served from port **5432** (`postgis-forensic` container). Any script, config, or documentation referencing port 5452 must be corrected to **5432**. The "★ restored March 28, 2026" language in prior drafts that framed 5452→5432 as a migration event was incorrect — **no migration occurred; 5432 was always correct.**

---

## 6. GeoDB Spatial Body and RAG Pipeline

### 6.0 Overview and Scope

This chapter describes the retrieval‑augmented generation (RAG) infrastructure that binds Ms. Egeria Allis's language models to the semantic and spatial memory systems defined in earlier chapters. In the current deployment, language models are no longer queried "from scratch": they are constrained and informed by:

- a **Phase 1.45 semantic community memory step** that prepends the top-5 most relevant `autonomous_learner` memories to every query before it reaches the LLM ensemble,
- a text RAG service backed by a shared HTTP‑exposed ChromaDB instance (host port **8002**, container port **8000**),
- a `msallisgis`‑coupled GIS RAG path for West Virginia features built on GBIM‑derived spatial entities from the PostgreSQL `msallis` / `msallisgis` databases (port **5432**, `postgis-forensic` container) and `gis_wv_benefits`,
- a **GBIM landowner query path** routed through `gbim_query_router` (port 7205) directly against `mvw_gbim_landowner_spatial` in `msallisgis` — a PostgreSQL-native path that bypasses ChromaDB entirely for structured ownership questions,
- a **live confidence decay and reverification loop** (`services.confidence_decay_loop`) running as a persistent async scheduled task inside `allis-ingest-watcher`, operating against `msallisgis.public.gbim_entities` (port **5432**) on a 24-hour cycle,
- a web‑research gateway, and
- a resolver path into the `allis-local-resources-db` registry (port 5435) for programmatic help,

all orchestrated by `allis-main-brain` (port **8050**) and the blood-brain-barrier services.

At runtime, queries enter through `allis-unified-gateway` (host **18018** → container **8001** — ✅ confirmed April 17, 2026) and are routed by the executive coordinator into a RAG layer that spans ChromaDB collections, PostgreSQL GIS features, GBIM landowner beliefs, and verified local‑resource rows. In production as of April 17, 2026, the full pipeline:

```text
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

> **⚠️ Embedding Model Lock — Confirmed April 17, 2026:**
> All ChromaDB collections use **384-dimensional vectors** produced by **`all-minilm:latest`** (`hnsw:space: cosine`). The `nomic-embed-text` model produces **768-dimensional vectors** and is **incompatible** with all existing collections. Any service, script, or migration that generates embeddings for ChromaDB **must** use `all-minilm:latest`. The `gbim_query_router` landowner path does **not** use embeddings — it routes directly to PostgreSQL.

> **★★ Security posture — confirmed April 17, 2026:** All services bound to `127.0.0.1` or internal Docker DNS. Zero `0.0.0.0` exposures. `_auth()` confirmed on all sensitive routes. `ALLIS_API_KEY` env var confirmed set in production.

> **★★ ChromaDB API and Port — confirmed April 17, 2026:**
> ChromaDB is running the **v2 multi-tenant API**. Host port: **8002** (`127.0.0.1:8002→8000/tcp`). Container-internal port: **8000**. The SQLite store is authoritative: **50 collections, 6,740,616 total embedding rows** (April 17, 2026). The `/api/v1/` endpoints are deprecated on this stack.

> **★★ Database architecture — confirmed April 17, 2026:** Both `msallisgis` (95 GB, 742 tables, 9 schemas — PostGIS spatial) and `msallis` (92 tables — GBIM application layer) are in the **`postgis-forensic`** container on **port 5432**. **There is no port 5433 container.** All prior references to `msallis:5433` are superseded. `gbim_entities` is in **`msallisgis`** (public schema) — NOT `msallis`. See §6.2.7.

> **★★ gbim_worldview_entity schema disambiguation — confirmed April 17, 2026:** Two separate `gbim_worldview_entity` tables exist — one in each database — with completely different schemas:
>
> | Database | Columns | Purpose |
> |---|---|---|
> | **`msallisgis`** | id, worldview_id, entity_type, source_table, source_pk, label, belief_state, centroid_geom, county_name_tag, confidence_decay, needs_verification, … | **Full spatial GBIM table — authoritative for all spatial and decay operations** |
> | `msallis` | id, entity_type, label, belief_state | Lightweight application mirror — 4 columns only |
>
> The decay loop, spatial ingest, and reverification all belong in **`msallisgis`**. Any operation targeting `msallis.gbim_worldview_entity` for decay or spatial purposes is incorrect.

```
┌─────────────────────────────────────────────────────────────┐
│            Ms. Allis RAG Pipeline Architecture               │
│            ★★ April 17, 2026 — Final Production Baseline    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  User Query                                                  │
│      ↓                                                       │
│  allis-unified-gateway (host:18018 → container:8001)        │
│      ↓                                                       │
│  allis-main-brain (port 8050)                               │
│      ↓                                                       │
│  BBB Input Filter — Phase 1.4                               │
│    allis-blood-brain-barrier:8016                           │
│    [6 filters — barrier_active: true]                       │
│    BLOCKED → architecture_layers=1, truthverdict=null       │
│      ↓ (passes)                                              │
│  Phase 1.45 — Community Memory Retrieval                    │
│    all-minilm:latest (384-dim) → autonomous_learner         │
│    top-5 memories prepended to enhanced_message             │
│    [21,159 items — April 17, 2026 — ~288/day]               │
│      ↓                                                       │
│  Main Brain Orchestration                                   │
│      ├──→ Text RAG (allis-rag-server host:8003→ctr:8003)   │
│      ├──→ GIS RAG (port 8004)                               │
│      ├──→ GBIM Landowner Router (port 7205)                 │
│      │       PostgreSQL-native → mvw_gbim_landowner_spatial │
│      │       NO ChromaDB                                    │
│      ├──→ WV-Entangled Gateway (port 8010) ✅              │
│      │       Static WV context injection via /chat_wv       │
│      ├──→ Web Research (excluded for WV queries)            │
│      └──→ Registry (allis-local-resources-db port 5435)     │
│      ↓                                                       │
│  Context Assembly (WV-first for WV queries)                 │
│      ↓                                                       │
│  LLM Ensemble (allis-ollama:11434 — 1.0 GiB RAM loaded)    │
│      ↓                                                       │
│  Judge Pipeline — judge_pipeline_v2.1-rag-grounded ✅       │
│    nbb_pituitary_gland:8108→80 — mode: elevated             │
│    allis-qualia-engine (internal:8017, DNS only)            │
│      ↓                                                       │
│  BBB Output Filter                                          │
│    allis-bbb-output-filter (internal:8017)                  │
│    {"status":"ok","service":"bbb-output-filter"} ✅         │
│      ↓                                                       │
│  UltimateResponse                                           │
│    { architecture_layers: 7, truthverdict: {                │
│        consensus_score: 0.95,                               │
│        validated_by:                                        │
│          "judge_pipeline_v2.1-rag-grounded" } }             │
│                                                              │
│  Background (async, 24h cycle):                             │
│  allis-ingest-watcher                                       │
│    → services.confidence_decay_loop                         │
│    → msallisgis.public.gbim_entities (port 5432)            │
│    → 461–466 entities / cycle, 0 flagged (April 17, 2026)  │
│    → Redis escalation consumer (allis-redis:6379)           │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> Figure 6‑1. RAG pipeline overview — April 17, 2026 final production baseline. `allis-unified-gateway` (host:**18018** → container:**8001**) is the external entry point. `allis-main-brain` (port **8050**) is the primary orchestrator. The confidence decay loop runs as a background async service inside `allis-ingest-watcher` on a 24-hour cycle against `msallisgis.public.gbim_entities`. 99 containers Up, zero Restarting, zero Exited (April 17, 2026).

---

### 6.1 Alignment with GBIM, Hilbert Space, Semantic Memory, GeoDB, and Registries

The GeoBelief Information Model (GBIM) defines how entities, places, and normative claims are represented across documents and spatial features. The `msallisgis` database (port **5432**, `postgis-forensic` container — 95 GB, 742 tables) is the authoritative spatial body. `msallis` (port **5432**, same container — 92 tables) is the GBIM application layer. The two `gbim_worldview_entity` tables in these databases have completely different schemas — the `msallisgis` version is the full spatial GBIM table with `confidence_decay`, `needs_verification`, and spatial geometry columns; the `msallis` version is a lightweight 4-column mirror. All decay, spatial ingest, and reverification operations target `msallisgis`.

As of March 20, 2026, GBIM beliefs include 20,593 landowner records (`LANDOWNER_CORPORATE` and `LANDOWNER_GOVERNMENT` proposition codes) ingested from the WV assessor corpus and materialized in `mvw_gbim_landowner_spatial` in `msallisgis`. These landowner beliefs are accessed via a dedicated PostgreSQL-native path through `gbim_query_router` (port 7205). As of April 17, 2026, `gbim_entities` in `msallisgis` carries **466 tracked entities** with a confirmed-live decay loop running on a 24-hour cycle.

The Hilbert‑space state view treats the system's overall knowledge and constraints as a very high‑dimensional state vector. RAG interactions are projections into lower‑dimensional subspaces. For text, those projections use **384-dimensional vectors from `all-minilm:latest`** (`hnsw:space: cosine`). For space, they use centroid‑based spatial filters over PostgreSQL `msallisgis`‑derived features. For structured ownership questions, they use SQL aggregations over `mvw_gbim_landowner_spatial`. For belief quality, the decay loop continuously reduces confidence scores and flags entities whose decay crosses a threshold — resetting to 1.0 when a `reverify_*()` function confirms the entity in source.

**Database Integration — ★★ Confirmed April 17, 2026:**

```python
import psycopg2
import chromadb

# PostgreSQL msallis (GBIM application layer) — port 5432
# ★★ CONFIRMED April 17, 2026: msallis is in postgis-forensic on port 5432
# ★★ There is NO port 5433 container. All prior msallis:5433 references SUPERSEDED.
# ★★ gbim_entities is in msallisgis — NOT msallis. Do not run decay queries here.
pg_conn_msallis = psycopg2.connect(
    host="localhost", port=5432,
    database="msallis", user="postgres", password="postgres"
)

# PostgreSQL msallisgis (PostGIS spatial + GBIM landowner layer + gbim_entities) — port 5432
# ★★ CONFIRMED April 17, 2026: decay loop targets msallisgis.public.gbim_entities
# ★★ Do NOT connect to port 5452 — that port has never existed in production.
pg_conn_msallisgis = psycopg2.connect(
    host="localhost", port=5432,
    database="msallisgis", user="postgres", password="postgres"
)

# PostgreSQL allis-local-resources-db — port 5435
# ⚠️ Confirmed: database name is "postgres", not the container name
# ⚠️ Gate 26 MUST use port 5435 — do NOT substitute port 5432.
#    The memories table does not exist on msallis schema.
pg_conn_resources = psycopg2.connect(
    host="localhost", port=5435,
    database="postgres",
    user="postgres", password="postgres"
)

# ChromaDB semantic memory — host port 8002 (container port 8000)
# REQUIRED: all-minilm:latest (384-dim, hnsw:space: cosine)
# DO NOT use nomic-embed-text (768-dim — incompatible with all collections)
chroma_client = chromadb.HttpClient(host="127.0.0.1", port=8002)
```

---

### 6.2 Core RAG and Search Components

At the implementation level, the retrieval layer consists of Phase 1.45 community memory retrieval, four main retrieval services, a GBIM landowner router, a registry resolver, a live confidence decay loop, and orchestration:

```
┌─────────────────────────────────────────────────────────────┐
│          Core Ms. Allis RAG Components                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Phase 1.45 — Community Memory Retrieval             │  │
│  │  -  Embedding: all-minilm:latest (384-dim)           │  │
│  │  -  Source: allis-ollama:11434/api/embeddings        │  │
│  │  -  Collection: autonomous_learner (~288/day)        │  │
│  │  -  Top-5 results prepended to enhanced_message      │  │
│  │  -  Fires after BBB input filter, before text RAG    │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Text RAG Service                                    │  │
│  │  allis-rag-server: host:8003 → container:8003        │  │
│  │  ★★ Both ports confirmed 8003 — April 17, 2026       │  │
│  │  -  ChromaDB backend (host port 8002)                │  │
│  │  -  Embedding: all-minilm:latest (384-dim, cosine)   │  │
│  │  -  Collections: local_resources (default),          │  │
│  │    governance_rag (643 chunks),                      │  │
│  │    commons_rag (306 chunks), thesis, research,       │  │
│  │    msallis_docs, mountainshares_knowledge,           │  │
│  │    conversation_history, episodic_index,             │  │
│  │    ms_allis_memory, gbim_beliefs_v2                  │  │
│  │  -  Metadata filters: county, source, worldview      │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  GIS RAG Service (port 8004)                         │  │
│  │  -  PostgreSQL msallisgis source (port 5432)         │  │
│  │  -  ChromaDB spatial collections (host port 8002)    │  │
│  │  -  Collections: gbim_worldview_entities,            │  │
│  │    gis_wv_benefits,                                  │  │
│  │    geospatialfeatures (60,000 items — live)          │  │
│  │    GBIM_Fayette_sample (1,535 items — live)          │  │
│  │  -  Returns: centroids, GBIM IDs, spatial metadata   │  │
│  │  -  Embedding: all-minilm:latest (384-dim)           │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  GBIM Landowner Router (port 7205)                   │  │
│  │  -  PostgreSQL msallisgis source (port 5432)         │  │
│  │  -  View: mvw_gbim_landowner_spatial                  │  │
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
│  │  ★★ LIVE — OI-C6-4 CLOSED April 17, 2026            │  │
│  │  -  Service: allis-ingest-watcher                    │  │
│  │  -  File: /app/services/services/                    │  │
│  │           confidence_decay_loop.py                   │  │
│  │  -  Target: msallisgis.public.gbim_entities          │  │
│  │  -  NOT msallis (4-column mirror)                    │  │
│  │  -  461–466 entities/cycle, 0 flagged (Apr 17)       │  │
│  │  -  Reset path: reverify_*() → decay=1.0             │  │
│  │  -  Escalation: allis-redis (redis:7-alpine)         │  │
│  │  -  Consumer: services/                              │  │
│  │     allis_decay_escalation_consumer.py               │  │
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
│  │  -  allis-local-resources-db (port 5435)             │  │
│  │  -  database: "postgres" (NOT the container name)    │  │
│  │  -  Filters: county, ZIP, resource_type              │  │
│  │  -  Returns: verified program records                │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> Figure 6‑2. Core retrieval components. `allis-rag-server` confirmed host:8003→container:8003 (April 17, 2026). Confidence decay loop confirmed live against `msallisgis.public.gbim_entities` — NOT `msallis`. `geospatialfeatures` (60,000 items) and `GBIM_Fayette_sample` (1,535 items) confirmed live March 26, 2026.

---

### 6.2.0 Phase 1.45 — Semantic Community Memory Retrieval (live since March 17, 2026)

Phase 1.45 fires after the BBB input filter approves the query (Phase 1.4) and before the main text and GIS RAG services (Phase 1.5). It is the first retrieval step that enriches `enhanced_message`.

**How it works:**

1. The main brain calls `allis-ollama:11434/api/embeddings` with model `all-minilm:latest` and the user query as the prompt, receiving a 384-dimensional embedding vector.
2. The embedding is used to query the `autonomous_learner` ChromaDB collection (growing ~288/day) via the v2 API (host port 8002).
3. The 5 most semantically similar community interaction records are retrieved (documents + metadata + distances).
4. The retrieved memories are prepended to `enhanced_message` before it reaches the LLM ensemble.

As of April 17, 2026: **21,159 items** in `autonomous_learner`.

```python
import httpx
import chromadb

# Step 1: Generate 384-dim embedding
# NOTE: single-string "prompt" field — not a list
# NOTE: use /api/embeddings not /api/embed — see ghost record warning in Ch 7 §7.0.2
response = httpx.post(
    "http://allis-ollama:11434/api/embeddings",
    json={"model": "all-minilm:latest", "prompt": user_query}
)
embedding = response.json()["embedding"]  # must be 384-dim

# Step 2: Query autonomous_learner via v2 API (host port 8002)
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

> **Critical:** Embedding model **must** be `all-minilm:latest` (384-dim, cosine). Using `nomic-embed-text` (768-dim) will cause a dimension mismatch error against all existing ChromaDB collections.

---

### 6.2.1 Text RAG Service (ChromaDB‑Backed)

The text RAG service takes a query string, a `top_k` parameter, optional metadata filters (collection, source, county, dataset, worldview), and optional role and geography hints. It issues similarity searches against one or more ChromaDB collections using **`all-minilm:latest` (384-dimensional embeddings, `hnsw:space: cosine`)**.

> **★★ Port confirmed April 17, 2026:** `allis-rag-server` maps **host:8003 → container:8003**. Both host and container ports are **8003**.

**Active collections for text RAG — ★★ UPDATED April 17, 2026:**

| Collection | Items | Purpose |
|---|---|---|
| `local_resources` | Active | **Default collection** — community queries; verified Fayette County resource data |
| `autonomous_learner` | 21,159 (~288/day) | Community interaction memories — queried at Phase 1.45 |
| `gbim_worldview_entities` | 5,416,521 | Complete WV GBIM spatial corpus |
| `gbim_beliefs_v2` | 5,000 | GBIM beliefs v2 — `wv_tag=true`, WV address point records with coordinates and ESN numbers |
| `gis_wv_benefits` | Active | WV benefits facilities |
| `governance_rag` | **643 chunks** | MountainShares DAO corpus + US Constitution — LIVE |
| `commons_rag` | **306 chunks** | Commons governance + gamification — LIVE |
| `psychological_rag` | **968** | Mental health corpus (port 8006) |
| `appalachian_cultural_intelligence` | **820** | Appalachian cultural context — confirmed distinct from `aaacpe_corpus` |
| `aaacpe_corpus` | **65 docs** | AaaCPE live web scrape corpus — `allis-aaacpe-scraper` port 8033, 39 sources |
| `spiritual_rag` | Deduplicated | Mother Carrie Protocol corpus — 19,338 duplicate vectors removed March 28, 2026 |
| `geospatialfeatures` | **60,000** | GIS feature embeddings — LIVE |
| `GBIM_Fayette_sample` | **1,535** | Fayette County sample — LIVE |
| `ms_allis_memory` | Active | Conversation memory |
| `mountainshares_knowledge` | Active | MountainShares governance |
| `episodic_index` | Active | Episodic memory index |
| `conversation_history` | 567 | Conversation history — wired in production (OI-05 CLOSED April 17, 2026) |
| `GBIM_sample_rows` | 5,000 | GBIM test sample |
| `msallis_docs` | **4,192** | System docs + verified WV community resources |

> **★★ April 17, 2026 full audit: 50 active collections, 6,740,616 total vectors.** All collections: 384-dim, `all-minilm:latest`, `hnsw:space: cosine`. Do not use `nomic-embed-text`.

---

### 6.2.2 GIS RAG Service (PostgreSQL `msallisgis`/GBIM‑Backed, port 8004)

The GIS RAG service is a dedicated geospatial retrieval path that serves West Virginia‑focused spatial questions. It queries:

- `gbim_worldview_entities` — 5,416,521 embeddings of West Virginia geospatial features from PostgreSQL `msallisgis` / `msallis`
- `gis_wv_benefits` — semantic descriptions and metadata for benefits‑related facilities such as Oak Hill hubs and Beckley DHHR offices
- `geospatialfeatures` — **60,000 items, confirmed live March 26, 2026**
- `GBIM_Fayette_sample` — **1,535 items, confirmed live March 26, 2026**

Each indexed entity stores a short text description and metadata fields including `worldview_id`, `dataset`, `county`, `gbim_entity`, `centroid_x`, and `centroid_y` (SRID 26917, also transformed to EPSG:4326). Metadata links back to `msallisgis.gbim_entities` (port **5432**) and `msallisgis.zcta_wv_centroids` (993 WV ZIP centroids).

All embeddings use **`all-minilm:latest` (384-dim, `hnsw:space: cosine`)**.

> **Routing distinction:** The GIS RAG service handles spatial feature questions requiring semantic similarity matching (e.g., "hospitals near Oak Hill"). Landowner/parcel ownership questions are routed through the GBIM Landowner Router (port 7205, §6.2.6). The GIS RAG service does not query `mvw_gbim_landowner_spatial`.

---

### 6.2.3 Web‑Research Gateway

External web retrieval is handled by a dedicated gateway rather than allowing arbitrary outbound calls from each agent or service. It applies policy filters and rate limits to outbound web access, normalizes results into a uniform structure, and logs queries and responses for audit.

In the WV‑first design, the main brain only admits web context for non‑WV or clearly extra‑state questions. When a query is WV‑scoped, web context is deliberately excluded so that external search results cannot override the in‑state RAG, GIS, landowner, and registry evidence. Under `nbb_pituitary_gland` `mode=elevated` (confirmed April 17, 2026), web exclusion for WV queries is **mandatory**. See §6.9.

---

### 6.2.4 Local Resource Registry Resolver (`allis-local-resources-db`, port 5435)

The local resource resolver accepts structured hints such as `county`, `zip`, and `resource_type` and queries `allis-local-resources-db` (port **5435**, database: `postgres`) for rows matching these constraints.

> **🔴 Gate 26 Port Warning — OI-C6-2 CLOSED April 17, 2026:**
> Gate 26 validation queries **MUST** be run against `allis-local-resources-db` on port **5435** (database: `postgres`). Running Gate 26 against port **5432** (`msallis` GBIM application layer) will produce a **false pass** — the `memories` table does not exist on that schema, so the query returns an error rather than the required non-zero `confidence_decay` count.
>
> ```bash
> psql -h 127.0.0.1 -p 5435 -U postgres -d postgres \
>   -c "SELECT COUNT(*) FROM memories WHERE confidence_decay IS NOT NULL;"
> # Required: non-zero result — any error or zero = gate FAIL
> ```
>
> **Never substitute port 5432 for port 5435 in Gate 26 or any gate referencing the `memories` table.**

As of April 17, 2026: **101 embeddings present; Fayette pipeline active**. AAACPE ingest remains an ops task to expand coverage.

---

### 6.2.5 Orchestration and Main Brain

The main brain routes each job through an orchestration layer that decides whether to invoke Phase 1.45 community memory, the text RAG service, the GIS RAG service, the GBIM landowner router, the web gateway, the local resource resolver, or some combination, based on:

- The request type (policy question, spatial query, landowner/ownership question, resource lookup, system status).
- The active role (researcher, governance engineer, community‑facing advisor).
- Any explicit or inferred geography (county, ZIP, worldview region).
- The presence of a `mode: landowner_gbim` flag, which routes to the GBIM landowner path regardless of other signals.

For WV‑scoped queries, the main brain:

- Fires Phase 1.45 community memory retrieval first (top-5 `autonomous_learner` memories prepended to `enhanced_message`).
- Treats West Virginia RAG (text + GIS from PostgreSQL `msallisgis` + registry) as mandatory input.
- Routes ownership/landowner questions to `gbim_query_router` (port 7205) rather than to GIS RAG or ChromaDB.
- Builds a WV‑first context window from RAG, GIS, landowner, and registry material, excluding `web_context`.

---

### 6.2.6 GBIM Landowner Router (`gbim_query_router`, port 7205) — Live since March 20, 2026

> **Field note — March 20, 2026, evening session.**
> The `gbim_query_router` service is live on port 7205 and verified on both statewide and county-scoped landowner queries. This service routes directly to `mvw_gbim_landowner_spatial` in `msallisgis` (PostgreSQL port **5432**) — it does not touch ChromaDB.
>
> *Verified March 20, 2026, ~19:45 EDT — Carrie Kidd (Mamma Kidd), Mount Hope WV*

#### Purpose and Design Rationale

The `gbim_query_router` handles structured landowner and parcel ownership queries against the GBIM belief layer. Ownership aggregation questions such as "who are the largest landowners in West Virginia?" are structurally relational — they require exact grouping, counting, and area summation over verified belief records, not semantic approximation. Routing these through ChromaDB would introduce vector-space approximation errors into a question that has a deterministic, auditable SQL answer. This aligns with **P16 – Power accountable to place**.

#### Landowner Routing Guarantee — OI-C6-3 CLOSED April 17, 2026

> **Architectural guarantee:** Landowner and parcel ownership queries in Ms. Allis are **always** resolved through PostgreSQL-native SQL aggregation via `gbim_query_router` (port 7205). They are **never** routed through ChromaDB vector similarity search. This is a structural routing constraint, not a configuration option.

```python
LANDOWNER_PATTERNS = [
    "landowner", "who owns", "largest owner",
    "owns the most land", "parcel ownership", "land ownership"
]

def route_query(query: str, mode: str) -> str:
    if mode == "landowner_gbim" or any(p in query.lower() for p in LANDOWNER_PATTERNS):
        return "gbim_query_router"   # SQL aggregation — port 7205 — NO ChromaDB
    return "rag_stack"               # ChromaDB path — port 8003/8002
```

#### Verified Query Patterns (March 20, 2026)

**Pattern 1 — Statewide top landowners:**

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

Underlying SQL against `mvw_gbim_landowner_spatial`:

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

Verified results:
- UNITED STATES OF AMERICA ~662,191 acres (`LANDOWNER_GOVERNMENT`)
- WEYERHAEUSER COMPANY ~242,892 acres (`LANDOWNER_CORPORATE`)

**Pattern 2 — County-scoped landowners:**

```bash
curl -s http://127.0.0.1:7205/query \
  -H "Content-Type: application/json" \
  -H "X-Allis-Role: researcher" \
  -d '{
    "question": "Who owns the most land in Fayette County?",
    "mode": "landowner_gbim",
    "route_type": "parcel_ownership",
    "county": "Fayette",
    "limit": 20
  }'
```

#### Ethical Constraint Enforcement

The `gbim_query_router` queries only rows with `proposition_code IN ('LANDOWNER_CORPORATE', 'LANDOWNER_GOVERNMENT')`. Individual residential owner names are not present in `mvw_gbim_landowner_spatial` and cannot be returned — this is a structural guarantee, not a runtime filter. WEYERHAEUSER COMPANY and 40 other landowners confirmed returned with `reverify_*()` reset path available via the decay loop (§6.2.7).

---

### 6.2.7 confidence_decay and needs_reverification — Live Production Service (OI-C6-4 CLOSED April 17, 2026)

> **★★ All prior "aspirational" and "not yet implemented" language in this section is superseded. The confidence decay and reverification loop is a confirmed live production service as of April 17, 2026 at 11:57–12:00 EDT.**

The confidence decay and reverification loop (`services.confidence_decay_loop`) runs as a persistent async scheduled task inside `allis-ingest-watcher`, confirmed live April 17, 2026. It operates against **`msallisgis.public.gbim_entities`** (`postgis-forensic` container, port **5432**) — **not `msallis`** — and processes all tracked GBIM entities per 24-hour cycle.

> **★★ Database target confirmed April 17, 2026:** `gbim_entities` is in **`msallisgis`** (public schema, `postgis-forensic` container, port **5432**). It is **not** in `msallis`. Any script or documentation referencing `msallis.gbim_entities` is incorrect.

**Confirmed live state — April 17, 2026:**

```text
Decay applied to 461 entities. 0 below flag threshold.
No entities below flag threshold. Cycle complete.
Next cycle in 86400s

[+] up 1/1
✔ Container allis-confidence-decay  Started
```

**Service deployment details:**

| Parameter | Value |
|---|---|
| Service container | `allis-confidence-decay` |
| Host file path | `services/confidence_decay_loop.py` |
| Container file path | `/app/services/services/confidence_decay_loop.py` (**COPY . /app/services** copies the whole repo including `services/` subfolder) |
| Cycle interval | 86400s (24 hours) |
| Target database | `msallisgis` (port 5432) — NOT `msallis` |
| Target table | `msallisgis.public.gbim_entities` |
| Entities per cycle | 461–466 |
| Flagged (April 17, 2026) | **0** |
| Redis container | `allis-redis` (image: `redis:7-alpine`) |
| Escalation consumer | `services/allis_decay_escalation_consumer.py` |
| Dockerfile fix | `psycopg2-binary` + `redis` added |

**gbim_entities column mapping — confirmed April 17, 2026:**

```text
msallisgis.public.gbim_entities uses:
  feature_type  (NOT entity_type)
  name          (NOT label)
```

> Any ingest or update script using `entity_type` or `label` against `gbim_entities` is incorrect and must be updated to `feature_type` / `name`.

**Decay cycle behavior — confirmed live paths:**

| Path | Trigger | Action | Example |
|---|---|---|---|
| ✅ DECAY | Scheduled 24h cycle | `confidence_decay` reduced per entity | All 461–466 entities processed |
| ✅ FLAG | `confidence_decay` below threshold | Entity marked `needs_reverification = true` | 0 flagged April 17, 2026 |
| ✅ RESET | `reverify_*()` finds entity in source | `confidence_decay → 1.0`, `reverification_result = confirmed`, `needs_reverification = false` | WEYERHAEUSER + 40 landowners |
| ✅ ESCALATE | Flagged entity — Redis consumer | `allis_decay_escalation_consumer.py` → `allis-redis` | Live consumer confirmed |

**Seed fixtures — confirmed April 17, 2026:**

| Action | Result |
|---|---|
| Watershed row inserted into `gbim_worldview_entity` (msallisgis) | ✅ |
| health_facility row inserted into `gbim_worldview_entity` (msallisgis) | ✅ |
| Seed fixtures 1/472–475 deleted | ✅ |
| Decay cycle: 461 entities, 0 flagged | ✅ Clean |

**What is NOT in `msallis.gbim_worldview_entity` (4-column mirror):** The lightweight `msallis` mirror has only `id`, `entity_type`, `label`, `belief_state`. It does not have `confidence_decay`, `needs_verification`, spatial geometry, or `county_name_tag`. Do not run decay, spatial ingest, or reverification against `msallis`. Always target `msallisgis`.

**Decay loop implementation stub — confirmed architecture:**

```python
# services/confidence_decay_loop.py
# Container path: /app/services/services/confidence_decay_loop.py
# Target: msallisgis.public.gbim_entities — NOT msallis

import asyncio
import psycopg2
import redis

DECAY_RATE = 0.01          # per cycle reduction
FLAG_THRESHOLD = 0.5       # below this → needs_reverification = true
CYCLE_INTERVAL = 86400     # 24 hours

async def run_decay_cycle():
    conn = psycopg2.connect(
        host="localhost", port=5432,
        database="msallisgis",    # ★★ NOT msallis
        user="postgres", password="postgres"
    )
    cursor = conn.cursor()

    # Apply decay to all tracked entities
    cursor.execute("""
        UPDATE gbim_entities
        SET confidence_decay = GREATEST(0, confidence_decay - %s)
        WHERE confidence_decay > 0
    """, (DECAY_RATE,))

    # Flag entities below threshold
    cursor.execute("""
        UPDATE gbim_entities
        SET needs_reverification = true
        WHERE confidence_decay < %s
          AND needs_reverification = false
    """, (FLAG_THRESHOLD,))

    cursor.execute("SELECT COUNT(*) FROM gbim_entities")
    total = cursor.fetchone()

    cursor.execute("SELECT COUNT(*) FROM gbim_entities WHERE needs_reverification = true")
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
        host="localhost", port=5432,
        database="msallisgis",    # ★★ NOT msallis
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

### 6.3 Retrieval Flows

#### 6.3.1 Non‑Spatial RAG Flow

**Query intake.** A user or upstream component sends a request through `allis-unified-gateway` (host:**18018** → container:**8001**) to `allis-main-brain` (port **8050**).

**Phase 1.45 — Community memory retrieval.** Before any other RAG service is invoked, the main brain embeds the query via `all-minilm:latest` (384-dim, `hnsw:space: cosine`) and retrieves the top-5 most similar records from `autonomous_learner` (host port **8002**). These are prepended to `enhanced_message`.

**Routing to text RAG and/or web.** For governance‑ and thesis‑style questions, the orchestration prefers ChromaDB‑backed collections (`governance_rag`, `commons_rag`, thesis, GBIM collections) and only consults the web when the question clearly depends on external or time‑varying facts.

**Retrieval from ChromaDB.** The text RAG service embeds the query, runs similarity search against selected collections, and returns high‑scoring documents and their metadata.

**Generation and judging.** The LLM ensemble (`allis-ollama:11434`) generates the candidate answer. `judge_pipeline_v2.1-rag-grounded` validates it, then the BBB output filter (`allis-bbb-output-filter`, internal:8017) applies post-hoc guardrails. A healthy full-stack response returns `architecture_layers = 7`, `truthverdict.consensus_score ≥ 0.95`.

---

#### 6.3.2 Spatial RAG Flow

```
┌─────────────────────────────────────────────────────────────┐
│   Spatial RAG: Semantic + Geographic Retrieval               │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Query type determination:                                  │
│    - Spatial feature question → GIS RAG (ChromaDB +         │
│        msallisgis port 5432)                                │
│    - Ownership/landowner question → gbim_query_router        │
│      (PostgreSQL-native, bypasses ChromaDB entirely)        │
│                                                              │
│  Semantic Retrieval (ChromaDB host port 8002)               │
│  ┌────────────────────────────────────────────────┐         │
│  │  Query: "hospitals near Oak Hill"              │         │
│  │  Embed query (all-minilm:latest, 384-dim)      │         │
│  │  → Search gis_wv_benefits +                    │         │
│  │    gbim_worldview_entities +                   │         │
│  │    geospatialfeatures (60,000 items) +          │         │
│  │    GBIM_Fayette_sample (1,535 items)            │         │
│  └────────────────────────────────────────────────┘         │
│              ↓                                               │
│  Geographic Filtering (PostgreSQL msallisgis port 5432)     │
│  ┌────────────────────────────────────────────────┐         │
│  │  SELECT zip, lat, lon                          │         │
│  │    FROM msallisgis.zcta_wv_centroids           │         │
│  │    WHERE zip = '25880'  -- Mount Hope          │         │
│  │  Then: spatial filter within 10-mile radius    │         │
│  └────────────────────────────────────────────────┘         │
│              ↓                                               │
│  GBIM Belief Quality (msallisgis.public.gbim_entities)      │
│  ★★ port 5432 — postgis-forensic — NOT msallis              │
│  ┌────────────────────────────────────────────────┐         │
│  │  Query: SELECT feature_type, name,             │         │
│  │    confidence_decay, needs_reverification      │         │
│  │    FROM gbim_entities WHERE entity_id = ?      │         │
│  │  Decay loop: 461 entities, 0 flagged           │         │
│  │  (April 17, 2026 — clean cycle)                │         │
│  └────────────────────────────────────────────────┘         │
│              ↓                                               │
│  Combined Results → LLM Context                             │
│                                                              │
│  ─────────────────────────────────────────────────          │
│  LANDOWNER PATH (bypasses all ChromaDB steps above)         │
│  ┌────────────────────────────────────────────────┐         │
│  │  Query: "Who owns the most land in Fayette?"   │         │
│  │  → Detected as landowner_gbim mode             │         │
│  │  → Route to gbim_query_router (port 7205)      │         │
│  │  → SQL aggregation over                        │         │
│  │    mvw_gbim_landowner_spatial                  │         │
│  │    in msallisgis (port 5432)                   │         │
│  │  → proposition_codes: CORPORATE + GOVERNMENT   │         │
│  │  → decay reset via reverify_*() when confirmed │         │
│  │  → No embeddings. No ChromaDB. Exact SQL.      │         │
│  └────────────────────────────────────────────────┘         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> Figure 6‑3. Spatial RAG flow. GBIM belief quality now queries `msallisgis.public.gbim_entities` on port **5432** using `feature_type`/`name` columns (not `entity_type`/`label`). Decay loop confirmed live — 461 entities, 0 flagged, April 17, 2026. Port 5433 and port 5452 are invalid and must not appear in any connection string.

---

#### 6.3.3 Resource‑Oriented RAG Flow

**Resource query intake.** The main brain receives the question and identifies it as a resource‑oriented request, extracting any available location hints (ZIP, county, town) and population signals.

**Phase 1.45 — Community memory.** Top-5 `autonomous_learner` memories are prepended.

**Interpretation via text and spatial RAG.** Text RAG and/or GIS RAG retrieve resource guides, flyers, benefits facilities, or prior notes. These hits may carry `local_resource_id` and `county` metadata linking them to `allis-local-resources-db`.

**Resolution via local resource resolver.** Queries `allis-local-resources-db` (port **5435**, database: `postgres`). As of April 17, 2026: 101 embeddings present; Fayette pipeline active.

**Context assembly and generation.** The orchestration layer builds a context from unstructured descriptions and structured `allis-local-resources-db` fields. The LLM ensemble applies the Ms. Egeria Allis persona.

---

### 6.4 Routing, Roles, Geography, and WV‑First Policy

#### 6.4.1 Design Intent

| Query type | Primary routing target |
|---|---|
| Governance, policy, thesis | Text RAG (ChromaDB — `governance_rag`, `commons_rag`, thesis, GBIM collections) |
| Spatial features, facilities | GIS RAG (ChromaDB + PostgreSQL `msallisgis`, port 5432) |
| Land ownership, landowners | `gbim_query_router` (PostgreSQL `msallisgis`, port 7205) — PostgreSQL-native |
| Belief quality / decay status | `msallisgis.public.gbim_entities` via decay loop (24h cycle) |
| Resource and referral | Text RAG + `allis-local-resources-db` resolver (port 5435) |
| System status | Internal orchestration |

**WV‑first behavior.** For West Virginia, whenever a query is WV‑scoped, the system treats WV RAG, PostgreSQL `msallisgis` GIS, GBIM landowner beliefs, and registry context as the authoritative sources, and excludes web context. Under `nbb_pituitary_gland` `mode=elevated` (confirmed April 17, 2026), WV exclusion of web context is **mandatory**. See §6.9.

#### 6.4.2 Service Routing Table — ★★ FINAL April 17, 2026

| Service | Host Port | Container Port | Notes |
|---|---|---|---|
| `allis-unified-gateway` | **18018** | **8001** | ✅ External entry — confirmed April 17, 2026 |
| `allis-main-brain` | 8050 | 8050 | ✅ Primary orchestrator |
| `allis-rag-server` | **8003** | **8003** | ✅ Both ports confirmed 8003 — April 17, 2026 |
| GIS RAG | 8004 | — | ✅ Active — live Fayette County geodata |
| `allis-psychological-rag` | 8006 | — | ✅ 968 docs serving correctly |
| `allis-wv-entangled-gateway` | 8010 | 8010 | ✅ Healthy — static WV injection via `/chat_wv` |
| `allis-web-research` | 8008 (internal) | — | ✅ Restored March 25, 2026 |
| `allis-ingest-api` | 8009 | — | ✅ Restored March 25, 2026 |
| `allis-blood-brain-barrier` | 8016 | 8016 | ✅ 6 filters — `barrier_active: true` |
| `allis-bbb-output-filter` | internal | 8017 | ✅ `{"status":"ok","service":"bbb-output-filter"}` |
| `allis-qualia-engine` | internal (DNS only) | 8017 | ✅ `allis-qualia-engine:8017` |
| `allis-consciousness-bridge` | internal | 8020 | ✅ `http://allis-consciousness-bridge:8020` |
| `allis-neurobiological-master` | internal | 8018 | ✅ `http://allis-neurobiological-master:8018` |
| `allis-i-containers` | internal | 8015 | ✅ `http://allis-i-containers:8015` |
| `allis-aaacpe-rag` | 8032 | — | ✅ `aaacpe_corpus` (65 docs, 39 sources) |
| `allis-aaacpe-scraper` | 8033 | — | ✅ Live |
| `gbim_query_router` | 7205 | 7205 | ✅ RBAC-gated — `X-Allis-Role` required |
| `allis-confidence-decay` | internal | — | ✅ **Live** — 24h cycle, 461 entities, 0 flagged |
| ChromaDB | 8002 (host) | 8000 (container) | ✅ 50 collections, 6,740,616 vectors |
| `nbb_pituitary_gland` | 8108 | 80 | ✅ mode=elevated (protocols: port 8107) |
| `msallisgis` + `msallis` | **5432** | **5432** | ✅ `postgis-forensic` — 95 GB, 742 tables. **No port 5433. No port 5452.** |
| `allis-local-resources-db` | 5435 | 5435 | ✅ 101 embeddings; `database="postgres"` |
| `allis-ollama` | 11434 | 11434 | ✅ 1.0 GiB RAM loaded |
| `allis-redis` | internal | 6379 | ✅ `redis:7-alpine` — decay escalation consumer |

---

### 6.5 Context Construction and Structure

**Source separation.** The text RAG service returns a `results_by_source` dictionary keyed by collection name. Phase 1.45 community memories are prepended as a distinct block. The GIS RAG service returns dataset names and feature labels traceable to PostgreSQL `msallisgis`. The GBIM landowner router returns structured rows from `mvw_gbim_landowner_spatial` labeled with proposition codes. The decay loop provides a continuous quality signal on `gbim_entities` (`confidence_decay`, `needs_reverification`) that is available to any service querying `msallisgis.public.gbim_entities`. The local resource resolver returns normalized rows from `allis-local-resources-db`.

**Relevance ordering and bounded size.** Phase 1.45 is hard-capped at top-5 results. `gbim_query_router` landowner results are hard-capped at the `limit` parameter in the request (default 20). Only entities with `confidence_decay` above the flag threshold are treated as fully authoritative; flagged entities (`needs_reverification = true`) surface a provenance note in the assembled context.

**Role‑, geography‑, and WV‑aware scaffolding.** For WV‑scoped queries, the ultimate prompt specifies that WV RAG, PostgreSQL `msallisgis` context, GBIM landowner beliefs, and `allis-local-resources-db` are authoritative; that web snippets are absent; and that the GBIM landowner layer contains only institutional/government entities. Decay quality metadata from `msallisgis.public.gbim_entities` is available to annotate retrieved entities with confidence status.

```
┌─────────────────────────────────────────────────────────────┐
│         Contextual Input Structure for LLM Reasoning        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  System Prompt (role, geography, constraints)               │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Phase 1.45 Community Memories                 │         │
│  │  └─ Top-5 autonomous_learner records           │         │
│  │     (all-minilm:latest, 384-dim)               │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  WV RAG Context                                │         │
│  │  ├─ governance_rag (643 chunks — LIVE)         │         │
│  │  ├─ commons_rag (306 chunks — LIVE)            │         │
│  │  ├─ Thesis fragments                           │         │
│  │  └─ GBIM beliefs (msallisgis port 5432)        │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  PostgreSQL GIS Context                        │         │
│  │  ├─ Spatial features (msallisgis tables)       │         │
│  │  ├─ Facilities (gis_wv_benefits)               │         │
│  │  ├─ geospatialfeatures (60,000 items)          │         │
│  │  ├─ GBIM_Fayette_sample (1,535 items)          │         │
│  │  ├─ GBIM worldview entities (5,416,521)        │         │
│  │  └─ gbim_entities decay quality signal         │         │
│  │     (461 entities, 0 flagged — April 17)       │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  GBIM Landowner Context (when mode=landowner)  │         │
│  │  └─ mvw_gbim_landowner_spatial (msallisgis)    │         │
│  │     via gbim_query_router (port 7205)          │         │
│  │     PostgreSQL-native — no ChromaDB            │         │
│  │     proposition_codes: CORPORATE + GOVERNMENT  │         │
│  │     decay reset: reverify_*() → decay=1.0      │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Registry Context                              │         │
│  │  └─ Programs (allis-local-resources-db,        │         │
│  │       port 5435, database: postgres, verified)  │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  Grounding Instruction (WV-first for WV queries)            │
│      ↓                                                       │
│  User Query                                                  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> Figure 6‑5. Structure of contextual input assembled for language‑model reasoning. All PostgreSQL references use port **5432** (`postgis-forensic` container). `gbim_entities` decay quality signal is from `msallisgis.public.gbim_entities` — 461 entities, 0 flagged, April 17, 2026. No port 5433 or 5452 references remain.

---

### 6.6 Constraints, Provenance, and Logging (continued)

**Decoding‑time guards.** After retrieval and generation, the main brain routes candidate responses through `judge_pipeline_v2.1-rag-grounded` (supersedes `heuristic_contradiction_v1`), then through the BBB output filter (`allis-bbb-output-filter`, internal:8017). The BBB output guard is fail-open on HTTP 500 — content passes through unchanged, failure is logged. Under `nbb_pituitary_gland` `mode=elevated`, the `consensus_score` floor is elevated above the standard threshold. The confirmed live `consensus_score` is **0.95** (April 17, 2026).

```
┌─────────────────────────────────────────────────────────────┐
│       Provenance and Guardrail Flow in RAG Pipeline         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Query → Phase 1.45 → Retrieval (all logged)               │
│    ↓                                                         │
│  Sources Captured:                                          │
│    - autonomous_learner top-5 (Phase 1.45)                  │
│    - ChromaDB collections queried (host port 8002)          │
│    - PostgreSQL msallisgis tables (port 5432)               │
│       ★★ postgis-forensic — port 5432 ONLY                  │
│    - gbim_entities decay quality (msallisgis port 5432)     │
│       feature_type/name columns — 461 entities tracked      │
│    - mvw_gbim_landowner_spatial (msallisgis port 5432)      │
│       via gbim_query_router (port 7205)                     │
│    - allis-local-resources-db rows (port 5435)              │
│    - Metadata filters applied                               │
│    ↓                                                         │
│  Context Assembly (with provenance)                         │
│    ↓                                                         │
│  LLM Ensemble (allis-ollama:11434 — 1.0 GiB RAM loaded)   │
│    ↓                                                         │
│  Judge Pipeline — judge_pipeline_v2.1-rag-grounded          │
│    nbb_pituitary_gland: mode=elevated                        │
│    consensus_score floor: elevated                           │
│    ↓                                                         │
│  Blood-Brain Barrier Output Filter                          │
│    allis-bbb-output-filter (internal:8017)                  │
│    fail-open on HTTP 500                                     │
│    {"status":"ok","service":"bbb-output-filter"} ✅         │
│    ↓                                                         │
│  UltimateResponse                                           │
│    architecture_layers: 7                                   │
│    truthverdict.consensus_score: 0.95                       │
│    truthverdict.bbb_checked: true                           │
│    truthverdict.validated_by:                               │
│      "judge_pipeline_v2.1-rag-grounded"                     │
│                                                              │
│  Background (async, 24h):                                   │
│  allis-confidence-decay                                     │
│    → Redis escalation (allis-redis:6379)                    │
│    → allis_decay_escalation_consumer.py                     │
│    → 0 flagged entities (April 17, 2026)                    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> Figure 6‑6. Provenance and guardrail flow ensuring accountable generation. The confidence decay loop runs as a background process independent of the query path — it provides continuous quality metadata on `msallisgis.public.gbim_entities` that the retrieval and context assembly layers can consume.

**Post‑hoc review and logging.** Logs capture which services were called, which collections were queried, which PostgreSQL tables and views were accessed (including `mvw_gbim_landowner_spatial`, `gbim_entities`, and which port/database they were served from), Phase 1.45 community memory results, `gbim_entities` decay status per entity queried, which filters and scores were applied, which registries were accessed, and which documents or features were returned.

***

### 6.7 Relation to Long‑Term Memory, GeoDB, Registries, and Entanglement**Long‑term memory.** ChromaDB collections hold embedded representations at **384 dimensions (`all-minilm:latest`, `hnsw:space: cosine`)**: `gbim_worldview_entities` (5,416,521 entities), `autonomous_learner` (21,159 items, growing ~288/day), `gis_wv_benefits`, `governance_rag` (643 chunks), `commons_rag` (306 chunks), `geospatialfeatures` (60,000 items), `GBIM_Fayette_sample` (1,535 items), `appalachian_cultural_intelligence` (820 items), `aaacpe_corpus` (65 documents), `spiritual_rag` (deduplicated — 19,338 duplicate vectors removed March 28, 2026), `psychological_rag` (968 items), `msallis_docs` (4,192 items), and 20+ additional collections. **★★ April 17, 2026 full audit: 50 active collections, 6,740,616 total vectors.**

Structured tables such as `allis-local-resources-db` (port 5435, database: `postgres`) hold normalized, versioned records addressable via RAG‑inferred keys. The GBIM landowner materialized view `mvw_gbim_landowner_spatial` in `msallisgis` (port 5432) holds 20,593 verified institutional landowner beliefs queryable via `gbim_query_router` (port 7205). The decay loop maintains continuous quality metadata on `msallisgis.public.gbim_entities` — 461–466 entities tracked, decay applied every 24 hours, `reverify_*()` reset path confirmed live (April 17, 2026).

**Short‑term context.** Each retrieval call assembles a temporary context window from Phase 1.45 community memories plus retrieved items, sorted by relevance and grouped by collection, layer, registry, and router. For WV‑scoped queries, this window is explicitly WV‑first: assembled from community memories, WV RAG (including live governance and commons RAG), PostgreSQL `msallisgis` GIS (including live spatial feature collections), GBIM landowner beliefs, registry material, and `gbim_entities` decay quality annotations — with web content excluded.

**Coupled updates and entanglement.** The `autonomous_learner`'s continuous growth (~288/day) represents one axis of the coupled update loop. The confidence decay loop represents a second axis: as WV assessor data is refreshed and `reverify_*()` confirms entities in source, decay resets to 1.0 and the belief layer reflects current ground truth. As watershed, health_facility, and other entity types are seeded into `msallisgis.gbim_worldview_entity` (the full spatial table — not the 4-column `msallis` mirror), those entities enter the decay cycle and become trackable quality signals in every retrieval pass that touches `gbim_entities`.

***

## 6.8 Production State Summary — ★★ FINAL April 17, 2026

**Container stack:** **99 containers Up — zero Restarting, zero Exited — confirmed April 17, 2026**

**Security posture — ★★ April 17, 2026:**
- All services bound to `127.0.0.1` or internal Docker DNS ✅
- Zero `0.0.0.0` exposures ✅
- `_auth()` confirmed on all sensitive routes ✅
- `ALLIS_API_KEY` env var confirmed set ✅

**ChromaDB (`allis-chroma`) — ★★ April 17, 2026 final audit:**
- Host port: **8002** (`127.0.0.1:8002→8000/tcp`) ✅
- API: v2 active — `/api/v1/` deprecated ✅
- Active collections: **50** ✅
- Total vectors: **6,740,616** ✅
- Embedding model: `all-minilm:latest` (384-dim, cosine) — all collections locked ✅

**PostgreSQL cluster — ★★ April 17, 2026:**
- Port **5432** — `postgis-forensic` container hosts both:
  - `msallisgis` — 95 GB, 742 tables, 9 schemas, PostGIS spatial ✅
  - `msallis` — 92 tables, GBIM application layer ✅
- **No port 5433 container exists.** All prior `msallis:5433` references superseded ✅
- **No port 5452 container exists.** All prior port 5452 references superseded (OI-C6-1 CLOSED) ✅
- Port **5435** — `allis-local-resources-db` — 101 embeddings; `database="postgres"` ✅- `gbim_entities` in `msallisgis.public` — 461–466 entities tracked by decay loop ✅

**gbim_worldview_entity disambiguation — ★★ April 17, 2026:**
- `msallisgis.gbim_worldview_entity` — full spatial table (worldview_id, entity_type, source_table, source_pk, label, belief_state, centroid_geom, county_name_tag, confidence_decay, needs_verification, …) — **authoritative** ✅
- `msallis.gbim_worldview_entity` — 4-column mirror (id, entity_type, label, belief_state) — lightweight only ✅
- Watershed row inserted into `msallisgis.gbim_worldview_entity` ✅
- health_facility row inserted into `msallisgis.gbim_worldview_entity` ✅
- Seed fixtures 1/472–475 deleted ✅

**Confidence decay loop — ★★ OI-C6-4 CLOSED April 17, 2026:**
- Container: `allis-confidence-decay` — ✅ UP
- Target: `msallisgis.public.gbim_entities` (port 5432) — NOT `msallis` ✅
- File path in container: `/app/services/services/confidence_decay_loop.py` ✅
- Column names confirmed: `feature_type` / `name` (not `entity_type` / `label`) ✅
- Cycle: 24h (86400s) ✅
- Result: 461 entities processed, 0 flagged ✅
- Redis: `allis-redis` (`redis:7-alpine`) ✅
- Escalation consumer: `services/allis_decay_escalation_consumer.py` ✅
- Dockerfile: `psycopg2-binary` + `redis` added ✅
- All 22 `llm*-proxy` YAML `volumes:` keys restored ✅

**RAG and routing:**
- Phase 1.45 community memory: live — 21,159 items ✅
- Text RAG (`allis-rag-server` host:8003 → container:8003): confirmed ✅
- GIS RAG (port 8004): operational ✅
- `psychological_rag` (port 8006): 968 docs ✅
- `gbim_query_router` (port 7205): RBAC-gated, PostgreSQL-native landowner path live ✅
- `allis-wv-entangled-gateway` (port 8010): static WV injection via `/chat_wv` ✅
- `allis-aaacpe-rag` (port 8032): live ✅
- `allis-aaacpe-scraper` (port 8033): live ✅
- `allis-web-research` (port 8008 internal): live ✅
- `allis-ingest-api` (port 8009): live ✅

**Judge pipeline:**
- `judge_pipeline_v2.1-rag-grounded` confirmed live ✅
- `heuristic_contradiction_v1` superseded ✅
- `consensus_score`: 0.95 confirmed ✅
- `architecture_layers`: 7 (healthy full-stack) ✅

**Open Issues — ALL CLOSED April 17, 2026:**

| ID | Issue | Status |
|:--|:--|:--|
| **OI-C6-1** | Port 5452 stale reference in Ch 6 | ✅ CLOSED — never-active port; 5432 always correct |
| **OI-C6-2** | Gate 26 false-pass on wrong port | ✅ CLOSED — Gate 26 must use port 5435 || **OI-C6-3** | Landowner SQL-only routing guarantee undocumented | ✅ CLOSED — §6.2.6 structural guarantee documented |
| **OI-C6-4** | confidence_decay loop aspirational | ✅ CLOSED — **FULLY LIVE** — 461 entities, 0 flagged, 24h cycle |
| **OI-C6-5** | nbb_pituitary_gland cross-reference missing from Ch 6 | ✅ CLOSED — §6.9 added |
| **OI-C6-6** | nbb_pituitary_gland routing modulation undocumented in Ch 7 | ✅ CLOSED — Ch 7 §7.2.9 added |

**No open issues remain in Chapter 6 as of April 17, 2026.**

***

## 6.9 nbb_pituitary_gland — Upstream RAG Routing Modulation (OI-C6-5 CLOSED April 17, 2026)

> **Cross-reference:** Full neurobiological architecture of `nbb_pituitary_gland` is documented in **Chapter 13 (Neurobiological Bridge)** and **Chapter 15 (Governance Protocol Stack)**. This section documents only the RAG routing modulation surface relevant to the pipeline described in this chapter.

The `nbb_pituitary_gland` service (`allis-neurobiological-master`, container-internal port **8018**, host port **8108** → container port **80** — ✅ `mode=elevated` confirmed April 17, 2026) acts as the **upstream modulator** of RAG routing weights in the Ms. Allis pipeline. It is the neurobiological analog of the pituitary gland in human endocrine architecture: it does not perform retrieval itself, but it sets the **operating mode and weighting context** under which all downstream RAG services operate.

**Confirmed live state — April 17, 2026:**

```bash
# Internal-only — must use docker exec; port 8018 is not host-exposed
docker exec allis-neurobiological-master curl -s http://localhost:8018/health
# Returns:
# {"status":"healthy","threat_level":"ELEVATED","redis":"ok",
#  "policy_hash":"5eaa2f31d5d5c7e9fe2f14985d825bc52e39a7c192a93f8082be02cac4a11f06"}

# Five governance protocols active (port 8107 — host-exposed):
curl -s -H "Authorization: Bearer $ALLIS_API_KEY" http://127.0.0.1:8107/protocols
# Returns:
# { "protocols": {
#     "dignity":      "Every person has inherent worth. No action may degrade human dignity.",
#     "sovereignty":  "Community data belongs to the community. No extraction without consent.",
#     "appalachian":  "Rooted in place. Resilient. No outside authority overrides local need.",
#     "transparency": "All decisions must be explainable to the people they affect.",
#     "protection":   "Protect the vulnerable first. Optimize for the margin, not the mean."
#   } }
```

**What `mode=elevated` changes in the RAG routing context:**

| Behavior | Normal mode | Elevated mode |
|---|---|---|
| WV RAG | Preferred | Mandatory — web context fully excluded |
| Landowner pattern detection | On explicit `landowner_gbim` flag | Sensitivity increased || BBB input threshold | Standard | Heightened — `threat_level: ELEVATED` |
| Judge pipeline `consensus_score` floor | Standard | Elevated |
| WV-entangled context injection | Applied | Amplified via `/chat_wv` |
| Decay loop quality signal | Available | Surfaced in context assembly |

**Known instrumentation gaps — April 17, 2026:**

| Endpoint | Result | Status |
|---|---|---|
| `GET http://127.0.0.1:8010/debug/weights` | `{"detail":"Not Found"}` | WOAH weight envelope not yet exposed — applied structurally via static WV context injection in `/chat_wv` |
| `GET http://127.0.0.1:8056/events?event_type=container_lifecycle` | `{"detail":"Method Not Allowed"}` | Pituitary lifecycle events logged to Redis internally — GET filter endpoint not yet implemented on `allis-memory:8056` |

Both gaps are future instrumentation tasks. Neither affects current production behavior.

> **See Chapter 13** for the full neurobiological bridge architecture and DGM integration.
>
> **See Chapter 15** for the governance protocol stack and how the five active protocols map to routing weights and judge pipeline thresholds under elevated threat posture.

***

*Chapter 6 — FINAL. Last updated: April 17, 2026, Mount Hope WV — Carrie Kidd (Mamma Kidd)*

*OI-C6-1 through OI-C6-6: ALL CLOSED April 17, 2026.*

*Port corrections applied: port 5452 deprecated (never active); port 5433 deprecated (never active); all msallis and msallisgis connections confirmed on port 5432 (`postgis-forensic` container). `allis-rag-server` confirmed host:8003→container:8003. `allis-unified-gateway` confirmed host:18018→container:8001.*

*OI-C6-4 CLOSED DEPLOYED: confidence decay loop fully live — `allis-confidence-decay` container UP, 461 entities processed, 0 flagged, 24h cycle, target `msallisgis.public.gbim_entities` (NOT `msallis`), `feature_type`/`name` columns confirmed, Redis escalation consumer live, watershed + health_facility rows inserted into `msallisgis.gbim_worldview_entity` (full spatial table), all 22 `llm*-proxy` YAML `volumes:` keys restored.*

*gbim_worldview_entity disambiguation confirmed: `msallisgis` version is full spatial table (authoritative for decay and spatial ops); `msallis` version is 4-column mirror only.*

*Prior update history: March 26, 2026 — `geospatialfeatures` (60,000 items) and `GBIM_Fayette_sample` (1,535 items) confirmed live. March 27, 2026 — all `gisdb` references corrected to `msallisgis`; `allis-local-resources-db` connection string corrected to `database="postgres"`. March 28, 2026 — security remediation complete; `spiritual_rag` deduplicated; `psychological_rag` restored (968 docs); `msallis_docs` expanded (4,192 items); 40 collections / 6,675,442 vectors audit. April 1, 2026 — LEARN-01, LEARN-02, LEARN-03 resolved; autonomous learner restored; 96/96 containers confirmed. April 17, 2026 — 99/99 containers confirmed; 50 collections / 6,740,616 vectors; all OIs closed; confidence decay loop deployed and live.*
