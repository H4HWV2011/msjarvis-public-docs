## Why this matters for Polymathmatic Geography

This chapter specifies how Ms. Jarvis's language models are bound to *place‑aware, collection‑aware, and registry‑aware memory* instead of free‑floating text generation. It makes the Hilbert‑space representation, GBIM structures, ChromaDB‑backed semantic memory, and the verified local resource registry from earlier chapters operational by defining concrete services that retrieve from semantic memory, the spatial body, the web, and structured program tables. In the current deployment, this design is realized as a production RAG stack that delivers West Virginia benefits intelligence through a 21‑model consciousness bridge anchored in ChromaDB, GBIM‑derived entities from the PostgreSQL `msjarvis` database (port 5433), GIS‑aware collections, and a WV‑first routing policy. It supports:

- **P1 – Every where is entangled** by requiring that answers emerge from an entangled memory of governance texts, spatial layers, research notes, belief structures from PostgreSQL GBIM tables, and local resource registries, rather than from an abstract model prior.

- **P3 – Power has a geometry** by letting retrieval paths expose which collections—and thus which institutional, spatial, and programmatic perspectives—shape a given answer, including WV‑specific benefits facilities in `gis_wv_benefits`, spatial entities derived from PostgreSQL GBIM and `gisdb`, benefits‑focused resource collections, and now the GBIM landowner belief layer (`mvw_gbim_landowner_spatial`) that makes corporate and government land ownership computable and queryable by natural language.

- **P5 – Design is a geographic act** by treating routing rules, collection choices, registry lookups, and gateway boundaries as design decisions that change how the system "sees" and acts within a region — including the explicit decision to route landowner queries through a PostgreSQL-native path rather than through vector similarity search.

- **P12 – Intelligence with a ZIP code** by privileging West Virginia‑specific collections in retrieval, and by coupling text RAG both to a state‑scale PostgreSQL `gisdb`/GBIM spatial body (port 5433, 13 GB, 39 tables, 5,416,521 verified beliefs in `msjarvis`) for spatial questions and to a ZIP‑ and county‑aware `jarvis-local-resources-db` registry (port 5435) for concrete program referrals, including flows for Oak Hill, Beckley, and broader Fayette/Raleigh County.

- **P16 – Power accountable to place** by making retrieval calls, filters, scores, registry lookups, and sources visible at the API and logging layer so that communities and researchers can audit what informed a Steward response — and by making the `gbim_query_router` landowner path explicitly inspectable as a structured SQL aggregation over verified GBIM belief records rather than an opaque embedding similarity result.

As such, this chapter belongs to the **Computational Instrument** tier: it defines the retrieval and routing machinery that connects ChromaDB‑backed semantic memory (port 8000), the PostgreSQL GBIM/`gisdb` spatial body (5,416,521 verified beliefs, 39 PostGIS tables), the verified local resource registry (`jarvis-local-resources-db`, port 5435), the GBIM landowner belief layer (`mvw_gbim_landowner_spatial`, routed via `gbim_query_router` port 7205), and web research to the live outputs of Ms. Jarvis.

---

## 7.0 Overview and Scope

This chapter describes the retrieval‑augmented generation (RAG) infrastructure that binds Ms. Egeria Jarvis's language models to the semantic and spatial memory systems defined in earlier chapters. In the current deployment, language models are no longer queried "from scratch": they are constrained and informed by:

- a **Phase 1.45 semantic community memory step** that prepends the top-5 most relevant `autonomous_learner` memories (21,181 items) to every query before it reaches the LLM ensemble,
- a text RAG service backed by a shared HTTP‑exposed ChromaDB instance (port 8000),
- a `gisdb`‑coupled GIS RAG path for West Virginia features built on GBIM‑derived spatial entities from the PostgreSQL `msjarvis` / `gisdb` databases (port 5433) and `gis_wv_benefits`,
- a **GBIM landowner query path** routed through `gbim_query_router` (port 7205) directly against `mvw_gbim_landowner_spatial` in `msjarvisgis` — a PostgreSQL-native path that bypasses ChromaDB entirely for structured ownership questions,
- a web‑research gateway, and
- a resolver path into the `jarvis-local-resources-db` registry (port 5435) for programmatic help,

all orchestrated by the main brain and blood–brain‑barrier services.

At runtime, queries enter through a unified HTTP gateway (for example, `POST /chat` or `POST /chat/async` on the main‑brain port) and are routed by the executive coordinator into a RAG layer that spans ChromaDB collections, PostgreSQL GIS features, GBIM landowner beliefs, and verified local‑resource rows. In production as of March 20, 2026, the full pipeline:

```text
Unified Gateway → Main Brain → Phase 1.45 Community Memory → RAG (text + GIS + landowner + registry, WV‑first) → 21‑LLM ensemble → Blood–Brain Barrier
```

is live and serving West Virginia benefits, geography, and land ownership questions. For WV‑scoped queries, the main brain treats West Virginia RAG as mandatory and suppresses generic web context when a county or WV role/profile is present, so that out‑of‑state material cannot quietly override in‑state evidence.

> **⚠️ Critical: Embedding Model Lock**
> All ChromaDB collections — including `gbim_worldview_entities` (5,416,521 entities), `autonomous_learner` (21,181 items), `gis_wv_benefits`, and all semantic collections — use **384-dimensional vectors** produced by **`all-minilm:latest`** (pulled March 17, 2026, via `jarvis-ollama:11434/api/embeddings`). The `nomic-embed-text` model produces **768-dimensional vectors** and is **incompatible** with all existing collections. Any service, script, or migration that generates embeddings for ChromaDB **must** use `all-minilm:latest`. This includes Phase 1.45, text RAG, GIS RAG, the autonomous learner, and any new collection ingestion. The `gbim_query_router` landowner path does **not** use embeddings — it routes directly to PostgreSQL.

A typical benefits query such as:
```bash
curl -X POST http://127.0.0.1:8050/chat/sync \
  -H "Content-Type: application/json" \
  -H "X-API-Key: super-secret-key" \
  -d '{"message":"Oak Hill WV county benefits","county":"Fayette","role":"community","profile":"auto"}'
```

triggers Phase 1.45 community memory retrieval from `autonomous_learner`, then retrieval from ChromaDB (including WV‑relevant collections such as governance, thesis, and `gis_wv_benefits`), optional GIS RAG over GBIM‑derived spatial entities from PostgreSQL `gisdb`, synthesis by the 21‑model ensemble, and post‑filtering by the guardrail service, with WV RAG, GIS context from PostgreSQL, and `jarvis-local-resources-db` treated as authoritative when they conflict with external web information.

A typical land ownership query such as:
```bash
curl -X POST http://127.0.0.1:8050/chat/sync \
  -H "Content-Type: application/json" \
  -H "X-API-Key: super-secret-key" \
  -d '{"message":"Who are the largest landowners in Fayette County?","county":"Fayette","role":"researcher","mode":"landowner_gbim"}'
```

routes through `gbim_query_router` (port 7205) directly against `mvw_gbim_landowner_spatial` in `msjarvisgis` — bypassing ChromaDB entirely and returning a structured SQL aggregation over verified GBIM landowner beliefs.

Within the overall architecture, the RAG layer is the primary bridge between relatively slow‑changing long‑term memory (ChromaDB collections, PostgreSQL `msjarvis`/`gisdb` at port 5433, structured registries like `jarvis-local-resources-db` at port 5435, and the GBIM landowner materialized view at `msjarvisgis`) and fast, per‑query reasoning in the language models.

```
┌─────────────────────────────────────────────────────────────┐
│            Ms. Jarvis RAG Pipeline Architecture              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  User Query                                                  │
│      ↓                                                       │
│  Unified Gateway (port 8050)                                │
│      ↓                                                       │
│  BBB Input Filter (port 8016) — Phase 1.4                  │
│      ↓                                                       │
│  Phase 1.45 — Community Memory Retrieval                    │
│    all-minilm:latest (384-dim) → autonomous_learner         │
│    top-5 memories prepended to enhanced_message             │
│      ↓                                                       │
│  Main Brain Orchestration                                   │
│      ├──→ Text RAG (ChromaDB port 8000)                     │
│      ├──→ GIS RAG (PostgreSQL gisdb port 5433 + ChromaDB)  │
│      ├──→ GBIM Landowner Router (port 7205 — PostgreSQL     │
│      │       native, bypasses ChromaDB)                     │
│      ├──→ Web Research (conditional — excluded for WV)      │
│      └──→ Registry Resolver (jarvis-local-resources-db      │
│              port 5435)                                      │
│      ↓                                                       │
│  Context Assembly (WV-first for WV queries)                 │
│      ↓                                                       │
│  21-LLM Ensemble                                            │
│      ↓                                                       │
│  Blood-Brain Barrier (guardrails)                           │
│      ↓                                                       │
│  Response to User                                           │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> Figure 7‑1. Retrieval‑augmented generation (RAG) pipeline overview linking the unified gateway, Phase 1.45 community memory, main‑brain orchestration (including the PostgreSQL-native GBIM landowner router), and ensemble‑guarded outputs.

---

## 7.1 Alignment with GBIM, Hilbert Space, Semantic Memory, GeoDB, and Registries

The GeoBelief Information Model (GBIM) defines how entities, places, and normative claims are represented across documents and spatial features in the PostgreSQL `msjarvis` database (port 5433, 8 MB, 6 tables). The RAG layer is the mechanism that actually retrieves those GBIM‑anchored fragments when a question is asked. GBIM worldview entities and other beliefs from PostgreSQL are surfaced into ChromaDB as metadata‑rich records in `gbim_worldview_entities` (5,416,521 entities), and the RAG services are structured so they can filter, group, and boost results by these identifiers as metadata coverage matures.

As of March 20, 2026, GBIM beliefs now include 20,593 landowner records (`LANDOWNER_CORPORATE` and `LANDOWNER_GOVERNMENT` proposition codes) ingested from the WV assessor corpus and materialized in `mvw_gbim_landowner_spatial` in `msjarvisgis`. These landowner beliefs are accessed via a dedicated PostgreSQL-native path through `gbim_query_router` (port 7205) rather than through ChromaDB vector search — a deliberate routing distinction described fully in Section 7.2.6.

The Hilbert‑space state view treats the system's overall knowledge and constraints as a very high‑dimensional state vector. RAG interactions can be understood as projections into lower‑dimensional subspaces that correspond to "what matters for this query, given this role and place." For text, those projections are implemented as embedding‑based nearest‑neighbor searches in ChromaDB collections using **384-dimensional vectors from `all-minilm:latest`**. For space, they are implemented as centroid‑based spatial filters over PostgreSQL `gisdb`‑derived features and as neighborhood queries over GBIM‑linked spatial entities. For structured ownership questions, they are implemented as SQL aggregations over `mvw_gbim_landowner_spatial` — a Hilbert-space projection that uses relational structure rather than vector geometry. For concrete help‑seeking and program questions, retrieved resource documents and metadata are further resolved into rows of `jarvis-local-resources-db` (port 5435) keyed by ZIP, county, and program type.

ChromaDB‑backed semantic memory (Chapter 5) is the substrate for governance texts, thesis fragments, research notes, GBIM worldview entities, and resource guides, while PostgreSQL `gisdb` (Chapter 6) defines the spatial body composed of PostGIS layers and exported worldview entities. In the March 2026 deployment, this alignment is implemented concretely:

- ChromaDB collections like `gbim_worldview_entities` (consolidated GBIM spatial index), `autonomous_learner` (21,181 items, queried at Phase 1.45), `gis_wv_benefits`, `psychological_rag` (968 items), `appalachian_cultural_intelligence` (5 items), `spiritual_texts` (23 items), `gbim_beliefs_v2`, and others are configured at **384 dimensions (`all-minilm:latest`)** and accessed over a shared HTTP ChromaDB service at port 8000.
- GIS RAG queries can reference metadata such as `worldview_id`, `county`, `dataset`, and `gbim_entity` to tie vector results back to PostgreSQL `msjarvis` GBIM and `gisdb`.
- Landowner queries are routed through `gbim_query_router` (port 7205), which issues SQL aggregations over `mvw_gbim_landowner_spatial` in `msjarvisgis` — no embeddings involved.
- Resource‑related collections tag documents with `local_resource_id`, allowing RAG hits to be resolved to `jarvis-local-resources-db` rows for facilities in Oak Hill, Beckley, and surrounding ZIP codes, as those registries are populated and verified.

**Database Integration (Four-Database Architecture, March 20, 2026):**
```python
import psycopg2
import chromadb

# PostgreSQL msjarvis (GBIM beliefs) — port 5433
pg_conn_msjarvis = psycopg2.connect(
    host="localhost", port=5433,
    database="msjarvis", user="postgres", password="postgres"
)

# PostgreSQL gisdb (PostGIS spatial) — port 5433
pg_conn_gisdb = psycopg2.connect(
    host="localhost", port=5433,
    database="gisdb", user="postgres", password="postgres"
)

# PostgreSQL msjarvisgis (GeoDB + GBIM landowner layer) — port 5432
pg_conn_msjarvisgis = psycopg2.connect(
    host="localhost", port=5432,
    database="msjarvisgis", user="postgres", password="postgres"
)

# PostgreSQL jarvis-local-resources-db — port 5435
pg_conn_resources = psycopg2.connect(
    host="localhost", port=5435,
    database="jarvis-local-resources-db",
    user="postgres", password="postgres"
)

# ChromaDB semantic memory — port 8000
# REQUIRED: all-minilm:latest (384-dim) — DO NOT use nomic-embed-text (768-dim)
chroma_client = chromadb.HttpClient(host="127.0.0.1", port=8000)
```

---

## 7.2 Core RAG and Search Components

At the implementation level, the retrieval layer consists of Phase 1.45 community memory retrieval, four main retrieval services, a GBIM landowner router, a registry resolver, and orchestration:

```
┌─────────────────────────────────────────────────────────────┐
│          Core Ms. Jarvis RAG Components                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Phase 1.45 — Community Memory Retrieval (NEW)        │  │
│  │  -  Embedding: all-minilm:latest (384-dim)             │  │
│  │  -  Source: jarvis-ollama:11434/api/embeddings         │  │
│  │  -  Collection: autonomous_learner (21,181 items)      │  │
│  │  -  Top-5 results prepended to enhanced_message        │  │
│  │  -  Fires after BBB input filter, before text RAG      │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Text RAG Service                                     │  │
│  │  -  ChromaDB backend (port 8000)                       │  │
│  │  -  Embedding: all-minilm:latest (384-dim)             │  │
│  │  -  Collections: governance, thesis, research,         │  │
│  │    msjarvis_docs, mountainshares_knowledge,           │  │
│  │    conversation_history, episodic_index,              │  │
│  │    ms_jarvis_memory, gbim_beliefs_v2                  │  │
│  │  -  Metadata filters: county, source, worldview        │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  GIS RAG Service (port 8004)                          │  │
│  │  -  PostgreSQL gisdb source (port 5433)               │  │
│  │  -  ChromaDB spatial collections (port 8000)           │  │
│  │  -  Collections: gbim_worldview_entities,             │  │
│  │    gis_wv_benefits, geospatialfeatures               │  │
│  │  -  Returns: centroids, GBIM IDs, spatial metadata    │  │
│  │  -  Embedding: all-minilm:latest (384-dim)             │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  GBIM Landowner Router (port 7205) — NEW             │  │
│  │  -  PostgreSQL msjarvisgis source (port 5432)          │  │
│  │  -  View: mvw_gbim_landowner_spatial                   │  │
│  │  -  Proposition codes: LANDOWNER_CORPORATE,           │  │
│  │    LANDOWNER_GOVERNMENT                               │  │
│  │  -  Worldview: eq1                                     │  │
│  │  -  NO ChromaDB — PostgreSQL-native path only         │  │
│  │  -  Returns: ranked owner names, parcel counts,       │  │
│  │    area (km²), county, proposition code               │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Web Research Gateway                                 │  │
│  │  -  Rate-limited external search                       │  │
│  │  -  Excluded for WV-scoped queries                     │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Local Resource Registry Resolver                     │  │
│  │  -  jarvis-local-resources-db (port 5435)              │  │
│  │  -  Filters: county, ZIP, resource_type                │  │
│  │  -  Returns: verified program records                  │  │
│  │  -  Community Champions validated                      │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Main Brain Orchestration                             │  │
│  │  -  Routes to appropriate services                     │  │
│  │  -  Assembles WV-first context                         │  │
│  │  -  Coordinates with 21-LLM ensemble                   │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> Figure 7‑2. Core retrieval components composing the Ms. Jarvis RAG layer, including Phase 1.45 community memory retrieval and the new GBIM landowner router (port 7205).

### 7.2.0 Phase 1.45 — Semantic Community Memory Retrieval (NEW — March 17, 2026)

Phase 1.45 fires after the BBB input filter approves the query (Phase 1.4) and before the main text and GIS RAG services (Phase 1.5). It is the first retrieval step that enriches `enhanced_message`.

**How it works:**

1. The main brain calls `jarvis-ollama:11434/api/embeddings` with model `all-minilm:latest` and the user query as the prompt, receiving a 384-dimensional embedding vector.
2. The embedding is used to query the `autonomous_learner` ChromaDB collection (21,181 items as of March 18, 2026; growing ~288/day).
3. The 5 most semantically similar community interaction records are retrieved (documents + metadata + distances).
4. The retrieved memories are prepended to `enhanced_message` before it reaches the 21-LLM ensemble.

**Why it matters:** The `autonomous_learner` collection holds autonomous research findings covering MountainShares security, Appalachian development, governance systems, and AI ethics — accumulated every 5 minutes since March 14, 2026. Prepending these memories grounds every response in the system's own accumulated community intelligence, not just the static corpus.

**Code example:**
```python
import httpx
import chromadb

# Step 1: Generate 384-dim embedding
response = httpx.post(
    "http://jarvis-ollama:11434/api/embeddings",
    json={"model": "all-minilm:latest", "prompt": user_query}
)
embedding = response.json()["embedding"]  # must be 384-dim

# Step 2: Query autonomous_learner
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

> **Critical:** The embedding model **must** be `all-minilm:latest` (384-dim). Using `nomic-embed-text` (768-dim) will cause a dimension mismatch error against all existing ChromaDB collections.

---

### 7.2.1 Text RAG Service (ChromaDB‑Backed)

The text RAG service exposes a structured HTTP API used by main‑brain chat paths that takes a query string, a `top_k` parameter, optional metadata filters (such as collection, source, county, dataset, or worldview), and optional role and geography hints. It issues similarity searches against one or more ChromaDB collections using **`all-minilm:latest` (384-dimensional embeddings)**, and returns both a flat list of top results and a `results_by_source` mapping keyed by collection name.

**Active collections for text RAG (March 20, 2026):**

| Collection | Items | Purpose |
|---|---|---|
| `autonomous_learner` | 21,181 (growing) | Community interaction memories — queried at Phase 1.45 |
| `gbim_worldview_entities` | 5,416,521 | Complete WV GBIM spatial corpus |
| `gbim_beliefs_v2` | Active | GBIM beliefs v2 |
| `gis_wv_benefits` | Active | WV benefits facilities |
| `psychological_rag` | 968 | Mental health corpus (port 8006) |
| `appalachian_cultural_intelligence` | 5 | Appalachian cultural context |
| `spiritual_texts` | 23 | Mother Carrie Protocol corpus |
| `ms_jarvis_memory` | Active | Conversation memory |
| `mountainshares_knowledge` | Active | MountainShares governance |
| `episodic_index` | Active | Episodic memory index |
| `conversation_history` | Active | Conversation history |
| `GBIM_sample_rows` | 5,000 | GBIM test sample |
| `msjarvis_docs` | 0 | Scaffolded — pending ingest |
| `geospatialfeatures` | 0 | Scaffolded — pending ingest |

> All collections: **384-dim, `all-minilm:latest`**. Do not use `nomic-embed-text`.

---

### 7.2.2 GIS RAG Service (PostgreSQL `gisdb`/GBIM‑Backed, port 8004)

The GIS RAG service is a dedicated geospatial retrieval path that serves West Virginia‑focused spatial questions. It exposes an endpoint that accepts a natural‑language query and an `n_results` parameter and returns a list of spatial hits. Internally, it queries:

- `gbim_worldview_entities` — 5,416,521 embeddings of West Virginia geospatial features from PostgreSQL `gisdb` / `msjarvis`, and
- `gis_wv_benefits` — semantic descriptions and metadata for benefits‑related facilities such as Oak Hill hubs and Beckley DHHR offices.

Each indexed entity stores a short text description and metadata fields such as `worldview_id`, `dataset`, `county`, `gbim_entity`, `centroid_x`, and `centroid_y` (SRID 26917, also transformed to EPSG:4326 for map display). Metadata links back to `msjarvis.gbim_beliefs` (via `entity_id`) and `gisdb.zcta_wv_centroids` (993 WV ZIP centroids, via `zip`).

All embeddings use **`all-minilm:latest` (384-dim)**.

> **Routing distinction — GIS RAG vs. GBIM Landowner Router:** The GIS RAG service handles spatial feature questions that require semantic similarity matching (e.g., "hospitals near Oak Hill", "facilities in Fayette County"). Landowner/parcel ownership questions are a structurally different query type — they ask who owns how much land where, which is fully answerable by SQL aggregation over verified GBIM belief records. Those queries are routed through the GBIM Landowner Router (port 7205, Section 7.2.6), not through GIS RAG. The GIS RAG service does not query `mvw_gbim_landowner_spatial`.

---

### 7.2.3 Web‑Research Gateway

External web retrieval is handled by a dedicated gateway rather than allowing arbitrary outbound calls from each agent or service. This gateway exposes an HTTP endpoint that accepts a JSON body with a query string and a limit on the number of results. It applies policy filters and rate limits to outbound web access, normalizes results into a uniform structure, and logs queries and responses for audit and debugging.

In the WV‑first design, the main brain only admits web context into the ultimate context window for non‑WV or clearly extra‑state questions. When a query is WV‑scoped (for example, has a West Virginia county or uses a WV benefits profile/role), web context is deliberately excluded so that external search results cannot override the in‑state RAG, GIS, landowner, and registry evidence.

---

### 7.2.4 Local Resource Registry Resolver (`jarvis-local-resources-db`, port 5435)

The local resource resolver is a thin service or module that sits alongside text and GIS RAG. It does not perform embedding search itself. Instead, it accepts structured hints such as `county`, `zip`, and `resource_type`, plus optional keys such as `local_resource_id` coming from RAG metadata, and queries `jarvis-local-resources-db` (port 5435) for rows that match these constraints and have an acceptable `verification_status`.

In help‑seeking flows, the main brain uses RAG primarily to interpret the question and surface relevant resource descriptions, then delegates final program selection to this resolver so that recommendations are grounded in a maintained, auditable registry rather than in unstructured text alone.

> **Known Issue — OPEN as of March 18, 2026:** `jarvis-local-resources-db` returns empty results for Mount Hope and Fayette County queries because verified community resource data has not yet been loaded. LLMs fall back to training data for local specifics. Factually accurate programs (LIHEAP, WV 2-1-1) pass the BBB. Fabricated organization names are blocked by the ethical filter. Resolution: Community Champions data entry is the next priority.

---

### 7.2.5 Orchestration and Main Brain

The main brain does not typically call language models directly. Instead, it routes each job through an orchestration layer that decides whether to invoke Phase 1.45 community memory, the text RAG service, the GIS RAG service, the GBIM landowner router, the web gateway, the local resource resolver, or some combination, based on:

- The request type (policy question, spatial query, landowner/ownership question, resource lookup, system status).
- The active role (researcher, governance engineer, community‑facing advisor).
- Any explicit or inferred geography (county, ZIP, worldview region).
- The presence of a `mode: landowner_gbim` flag, which routes to the GBIM landowner path regardless of other signals.

For WV‑scoped queries, the main brain:

- Fires Phase 1.45 community memory retrieval first (top-5 `autonomous_learner` memories prepended to `enhanced_message`).
- Treats West Virginia RAG (text + GIS from PostgreSQL `gisdb` + registry) as mandatory input.
- Routes ownership/landowner questions to `gbim_query_router` (port 7205) rather than to GIS RAG or ChromaDB.
- Builds a WV‑first context window from RAG, GIS, landowner, and registry material, excluding `web_context`.
- Prepends a strong grounding instruction that explicitly tells the ensemble to treat WV RAG, GIS context from PostgreSQL `gisdb`, `jarvis-local-resources-db`, and GBIM landowner beliefs as authoritative for West Virginia.

---

### 7.2.6 GBIM Landowner Router (`gbim_query_router`, port 7205) — NEW — March 20, 2026

> **Field note — March 20, 2026, evening session.**
> The `gbim_query_router` service is live on port 7205 and verified on both statewide and county-scoped landowner queries. This service routes directly to `mvw_gbim_landowner_spatial` in `msjarvisgis` (PostgreSQL port 5432) — it does not touch ChromaDB. Both `LANDOWNER_CORPORATE` and `LANDOWNER_GOVERNMENT` proposition codes are confirmed returning correct results.
>
> *Verified March 20, 2026, ~19:45 EDT by Carrie Kidd (Mamma Kidd), Oak Hill WV*

#### Purpose and Design Rationale

The `gbim_query_router` is a dedicated Docker service that handles structured landowner and parcel ownership queries against the GBIM belief layer. It was purpose-built to serve a query type that does not benefit from vector similarity search: ownership aggregation questions such as "who are the largest landowners in West Virginia?" or "who owns the most land in Fayette County?" are structurally relational — they require exact grouping, counting, and area summation over verified belief records, not semantic approximation.

Routing these queries through ChromaDB would introduce vector-space approximation errors into a question that has a deterministic, inspectable SQL answer. The `gbim_query_router` makes the routing decision explicit: landowner questions are answered by PostgreSQL-native aggregation over `mvw_gbim_landowner_spatial`, not by embedding similarity over `gbim_worldview_entities`.

This aligns with **P16 – Power accountable to place**: the answer to "who owns the land" is not an approximate nearest-neighbor result — it is an exact, auditable fact derived from WV assessor records ingested into the GBIM belief stack. The router preserves that exactness.

#### Routing Schema

```json
{
  "mode": "landowner_gbim",
  "route_type": "parcel_ownership",
  "proposition_codes": ["LANDOWNER_CORPORATE", "LANDOWNER_GOVERNMENT"],
  "worldview": "eq1",
  "source_db": "msjarvisgis",
  "source_view": "mvw_gbim_landowner_spatial"
}
```

The `mode: landowner_gbim` flag is the primary routing signal. When the main brain detects this flag — either explicitly in the request or inferred from the query pattern (ownership, landowner, "who owns", "largest landowner", parcel control) — it bypasses the ChromaDB RAG stack entirely for the landowner component and delegates to `gbim_query_router`.

#### Verified Query Patterns (March 20, 2026)

**Pattern 1 — Statewide top landowners:**

```bash
curl -s http://127.0.0.1:7205/query \
  -H "Content-Type: application/json" \
  -d '{
    "question": "Who are the largest landowners in West Virginia?",
    "mode": "landowner_gbim",
    "route_type": "parcel_ownership",
    "scope": "statewide",
    "limit": 20
  }'
```

Underlying SQL executed by the router against `mvw_gbim_landowner_spatial`:

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

**Pattern 2 — County-scoped landowners:**

```bash
curl -s http://127.0.0.1:7205/query \
  -H "Content-Type: application/json" \
  -d '{
    "question": "Who owns the most land in Fayette County?",
    "mode": "landowner_gbim",
    "route_type": "parcel_ownership",
    "county": "Fayette",
    "limit": 20
  }'
```

Underlying SQL:

```sql
SELECT
    who_axis->>'canonical_entity_name'  AS owner,
    proposition_code,
    COUNT(*)                             AS parcel_count,
    ROUND(SUM(ST_Area(geom::geography)/1e6)::numeric, 2) AS area_km2
FROM mvw_gbim_landowner_spatial
WHERE proposition_code IN ('LANDOWNER_CORPORATE', 'LANDOWNER_GOVERNMENT')
  AND where_axis->>'county' = 'Fayette'
GROUP BY owner, proposition_code
ORDER BY area_km2 DESC NULLS LAST
LIMIT 20;
```

Both patterns were verified returning correct results on March 20, 2026. Results include the `proposition_code` column in the output so that corporate and government landholders remain distinguishable in LLM context assembly.

#### Ethical Constraint Enforcement

The `gbim_query_router` enforces the ethical constraint established in Chapter 6, Section 6.6.1 at the service level: it queries only rows in `mvw_gbim_landowner_spatial` with `proposition_code IN ('LANDOWNER_CORPORATE', 'LANDOWNER_GOVERNMENT')`. Individual residential owner names are not present in `mvw_gbim_landowner_spatial` and cannot be returned by any query routed through this service. This is not a runtime filter applied to potentially dangerous data — it is a structural guarantee: individual residential names were never ingested into the belief layer that this router queries.

#### Integration with Main Brain Context Assembly

When the main brain routes a query through `gbim_query_router`, the structured results are assembled into the LLM context as a distinct block clearly labeled as GBIM landowner beliefs derived from verified WV assessor records. This block is formatted for the ensemble to reason over:

```
[GBIM LANDOWNER BELIEFS — msjarvisgis / mvw_gbim_landowner_spatial]
Source: WV assessor parcel records ingested into GBIM (March 20, 2026)
Proposition codes: LANDOWNER_CORPORATE, LANDOWNER_GOVERNMENT
Scope: Fayette County

Rank | Owner                          | Type        | Parcels | Area (km²)
-----|-------------------------------|-------------|---------|----------
1    | [canonical_entity_name]        | CORPORATE   | [n]     | [x.xx]
2    | [canonical_entity_name]        | GOVERNMENT  | [n]     | [x.xx]
...

Note: Individual residential owner names are not included in this layer.
All entries represent institutional or government landholders only.
```

The ensemble is instructed to treat this block as authoritative for questions about land ownership in West Virginia, in the same way it treats WV RAG and GIS context as authoritative for benefits and spatial questions.

---

## 7.3 Retrieval Flows

This section sketches the typical flows for non‑spatial, spatial, landowner, and resource‑oriented queries. In each case, the retrieval layer is where abstract Hilbert‑space projections and GBIM entities from PostgreSQL become concrete calls and responses.

### 7.3.1 Non‑Spatial RAG Flow

A typical governance or thesis question progresses as follows:

**Query intake.**
A user or upstream component sends a request to the unified gateway or main brain. The coordinator wraps it into an internal job structure containing the raw text, any structured fields (project, county, worldview), and role hints.

**Phase 1.45 — Community memory retrieval.**
Before any other RAG service is invoked, the main brain embeds the query via `all-minilm:latest` and retrieves the top-5 most similar records from `autonomous_learner` (21,181 items). These are prepended to `enhanced_message`.

**Routing to text RAG and/or web.**
The orchestration logic decides whether to call the local text RAG service, the web gateway, or both. For most governance‑ and thesis‑style questions, it prefers ChromaDB‑backed collections (governance, thesis, GBIM, or MountainShares collections) and only consults the web when the question clearly depends on external or time‑varying facts.

**Retrieval from ChromaDB (384-dim, `all-minilm:latest`).**
The text RAG service embeds the query, runs similarity search against the selected collections, and returns high‑scoring documents and their metadata.

**Context assembly.**
The orchestration layer merges the retrieved items — Phase 1.45 community memories, text RAG results, and any web‑research snippets (if allowed) — into a context window alongside system prompts and role‑specific instructions.

**Generation and guarding.**
One or more language models generate an answer conditioned on this assembled context. The LM Synthesizer (Phase 3.5) applies the Ms. Egeria Jarvis persona via `jarvis-ollama:11434/api/generate` with `llama3.1:latest`. The main brain then routes the candidate answer through the blood–brain barrier service.

---

### 7.3.2 Spatial RAG Flow

```
┌─────────────────────────────────────────────────────────────┐
│   Spatial RAG: Semantic + Geographic Retrieval               │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Query type determination:                                  │
│    - Spatial feature question → GIS RAG (ChromaDB + gisdb)  │
│    - Ownership/landowner question → gbim_query_router        │
│      (PostgreSQL-native, bypasses ChromaDB entirely)        │
│                                                              │
│  Semantic Retrieval (ChromaDB port 8000)                    │
│  ┌────────────────────────────────────────────────┐         │
│  │  Query: "hospitals near Oak Hill"              │         │
│  │  Embed query (all-minilm:latest, 384-dim)      │         │
│  │  → Search gis_wv_benefits + gbim_worldview_entities     │
│  │  Returns: Embeddings + metadata                │         │
│  │    -  facility_type, county, GBIM ID            │         │
│  └────────────────────────────────────────────────┘         │
│              ↓                                               │
│  Geographic Filtering (PostgreSQL gisdb port 5433)          │
│  ┌────────────────────────────────────────────────┐         │
│  │  Use GBIM IDs from ChromaDB                    │         │
│  │  Query: SELECT zip, lat, lon                   │         │
│  │    FROM zcta_wv_centroids                      │         │
│  │    WHERE zip = '25880'  -- Mount Hope          │         │
│  │  Then: spatial filter within 10-mile radius    │         │
│  │  Returns: Full geometries + attributes         │         │
│  └────────────────────────────────────────────────┘         │
│              ↓                                               │
│  GBIM Belief Provenance (PostgreSQL msjarvis port 5433)     │
│  ┌────────────────────────────────────────────────┐         │
│  │  Query: gbim_beliefs WHERE entity_id = ?       │         │
│  │  Returns: confidence_decay, needs_verification │         │
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
│  │    in msjarvisgis (port 5432)                  │         │
│  │  → Proposition codes: LANDOWNER_CORPORATE,    │         │
│  │    LANDOWNER_GOVERNMENT                        │         │
│  │  → Returns: ranked owners, parcel counts,     │         │
│  │    area_km2, proposition_code                  │         │
│  │  → No embeddings. No ChromaDB. Exact SQL.      │         │
│  └────────────────────────────────────────────────┘         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> Figure 7‑3. Spatial RAG flow showing both the semantic+geographic path (GIS RAG via ChromaDB + gisdb) and the PostgreSQL-native landowner path (gbim_query_router → mvw_gbim_landowner_spatial). These are distinct routing paths — landowner queries bypass ChromaDB entirely.

Spatially explicit questions (for example, "roads in Fayette County", "hospitals near Oak Hill", "which buildings lie in this floodplain?") follow the GIS RAG path as described. Landowner and parcel ownership questions follow the separate PostgreSQL-native path:

**Landowner query detection.**
The main brain or a routing-aware client detects the query as ownership-oriented — either by an explicit `mode: landowner_gbim` flag in the request body or by pattern matching on terms such as "who owns", "largest landowner", "land ownership", "corporate landowner", or "government land". When detected, the query is routed to `gbim_query_router` (port 7205) rather than to GIS RAG.

**PostgreSQL-native aggregation.**
`gbim_query_router` issues a SQL aggregation over `mvw_gbim_landowner_spatial` in `msjarvisgis` (port 5432). The query groups by `canonical_entity_name` and `proposition_code`, sums parcel area using `ST_Area(geom::geography)`, counts parcels, and orders by area descending. No embedding is generated. No ChromaDB collection is queried.

**County scoping.**
If a county is specified (via the `county` field in the request or inferred from context), the aggregation adds a `WHERE where_axis->>'county' = '<county>'` clause. County-scoped queries return the top institutional landholders within that county only.

**Context injection.**
The ranked landowner results are assembled into a clearly labeled GBIM belief block and injected into the LLM context window. The ensemble is instructed to treat this as authoritative WV landowner data derived from verified assessor records.

---

### 7.3.3 Resource‑Oriented RAG Flow

Help‑seeking or resource questions (for example, "What Christmas help is available in Oak Hill this year?" or "Where can a grandmother in ZIP 25840 get utility assistance?") combine semantic retrieval with structured registry lookups:

**Resource query intake.**
The main brain receives the question and identifies it as a resource‑oriented request, extracting any available location hints (ZIP, county, town) and population signals.

**Phase 1.45 — Community memory.**
Top-5 `autonomous_learner` memories are prepended, providing any prior community interactions about similar resource queries.

**Interpretation via text and spatial RAG.**
Text RAG and/or GIS RAG retrieve resource guides, flyers, benefits facilities, or prior notes related to the apparent need category (such as seasonal assistance or utility help). These hits may carry `local_resource_id` and `county` metadata linking them to structured registry entries in `jarvis-local-resources-db`.

**Resolution via local resource resolver.**
The local resource resolver queries `jarvis-local-resources-db` (port 5435) using structured hints (ZIP, county, `resource_type`) and any concrete IDs, returning candidate program rows that are currently verified or recently verified.

> **Known Issue:** As of March 18, 2026, `jarvis-local-resources-db` is empty for Mount Hope queries. See §7.2.4.

**Context assembly and generation.**
The orchestration layer builds a context that includes both unstructured descriptions (for narrative framing) and structured fields from `jarvis-local-resources-db` (for factual details such as phones, emails, deadlines, and coverage). The LM Synthesizer (Phase 3.5) applies the Ms. Egeria Jarvis persona before returning the final response.

---

## 7.4 Routing, Roles, Geography, and WV‑First Policy

Routing is conceptually central to the RAG design. It is GBIM‑aware, role‑aware, geography‑aware, registry‑aware, query-type-aware, and explicitly WV‑first for West Virginia–scoped questions.

### 7.4.1 Design Intent

**Topic and intent routing.**
The system distinguishes between queries about governance, geospatial context, thesis theory, MountainShares economics, resource and referral questions, infrastructure status, and land ownership, routing each toward appropriate services and collections:

| Query type | Primary routing target |
|---|---|
| Governance, policy, thesis | Text RAG (ChromaDB — governance, thesis, GBIM collections) |
| Spatial features, facilities | GIS RAG (ChromaDB + PostgreSQL gisdb, port 5433) |
| Land ownership, landowners | `gbim_query_router` (PostgreSQL msjarvisgis, port 5432) — PostgreSQL-native |
| Resource and referral | Text RAG + `jarvis-local-resources-db` resolver |
| System status | Internal orchestration |

**Role‑aware routing.**
The active role determines which collections and registries are eligible. Internal or sensitive material is only surfaced for trusted roles, while community‑facing roles are restricted to public documentation, approved spatial layers, and public‑facing slices of `jarvis-local-resources-db`.

**Geography‑aware routing and WV‑first behavior.**
For West Virginia, whenever a query is WV‑scoped, the system treats WV RAG, PostgreSQL `gisdb` GIS, GBIM landowner beliefs, and registry context as the authoritative sources, and excludes web context from the final assembled context window.

### 7.4.2 Current Implementation (March 20, 2026)

```
┌─────────────────────────────────────────────────────────────┐
│     Intelligence with a ZIP Code - WV Geographic Routing     │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Query: "Who owns land in Fayette County WV?"               │
│      ↓                                                       │
│  WV-Scoped + Landowner Detection:                           │
│    -  County = "Fayette"                                      │
│    -  State = "WV"                                            │
│    -  Mode detected: landowner_gbim                          │
│      ↓                                                       │
│  Phase 1.45 — Community Memory:                             │
│    all-minilm:latest → autonomous_learner → top-5 prepended │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  gbim_query_router (port 7205)                 │         │
│  │  → mvw_gbim_landowner_spatial (msjarvisgis)    │         │
│  │  → WHERE county = 'Fayette'                    │         │
│  │  → proposition_codes: CORPORATE + GOVERNMENT   │         │
│  │  → Returns: ranked owners + area_km2           │         │
│  │  → PostgreSQL-native. No ChromaDB.             │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  WV-First Context Assembly:                                 │
│    -  INCLUDE: community memories +                          │
│               GBIM landowner beliefs +                      │
│               WV RAG (if supplementary context needed)      │
│    -  EXCLUDE: web_context (out-of-state suppressed)        │
│      ↓                                                       │
│  Grounding Instruction:                                     │
│    "Treat GBIM landowner beliefs from                       │
│     mvw_gbim_landowner_spatial as authoritative             │
│     for WV land ownership. These are verified               │
│     assessor records. Ignore conflicting external info."    │
│      ↓                                                       │
│  21-LLM Ensemble → LM Synthesizer (llama3.1:latest)        │
│      → Response                                             │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> Figure 7‑4. Geography‑aware and query-type-aware routing in the Ms. Jarvis retrieval layer, showing the landowner_gbim path that routes directly to `gbim_query_router` rather than to ChromaDB.

---

## 7.5 Context Construction and Structure

**Source separation.**
The text RAG service returns a `results_by_source` dictionary keyed by collection name. Phase 1.45 community memories are prepended as a distinct block. The GIS RAG service returns dataset names and feature labels with spatial metadata traceable to PostgreSQL `gisdb`. The GBIM landowner router returns structured rows from `mvw_gbim_landowner_spatial` labeled with proposition codes and clearly identified as WV assessor-derived GBIM beliefs. The local resource resolver returns normalized rows from `jarvis-local-resources-db` with clearly typed fields.

**Relevance ordering and bounded size.**
ChromaDB returns distances, which the services convert into scores; flat results are sorted in descending score order. Clients specify `top_k` per collection or `n_results` per GIS query, and the services enforce these limits. Phase 1.45 is hard-capped at top-5 results. `gbim_query_router` landowner results are hard-capped at the `limit` parameter in the request (default 20).

**Role‑, geography‑, and WV‑aware scaffolding.**
For WV‑scoped queries, the ultimate prompt spells out that WV RAG, PostgreSQL `gisdb` context, GBIM landowner beliefs from `mvw_gbim_landowner_spatial`, and `jarvis-local-resources-db` are authoritative, that web snippets are absent, and that the GBIM landowner layer contains only institutional/government entities — individual residential owner names are not present.

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
│  │     (all-minilm:latest, 384-dim, 21,181 items) │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  WV RAG Context                                 │         │
│  │  ├─ Governance docs (collection: governance)   │         │
│  │  ├─ Thesis fragments (collection: thesis)      │         │
│  │  └─ GBIM beliefs (from PostgreSQL msjarvis)    │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  PostgreSQL GIS Context                         │         │
│  │  ├─ Spatial features (gisdb tables)            │         │
│  │  ├─ Facilities (gis_wv_benefits)               │         │
│  │  └─ GBIM worldview entities                    │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  GBIM Landowner Context (when mode=landowner)  │         │
│  │  └─ mvw_gbim_landowner_spatial (msjarvisgis)   │         │
│  │     via gbim_query_router (port 7205)           │         │
│  │     PostgreSQL-native — no ChromaDB             │         │
│  │     proposition_codes: CORPORATE + GOVERNMENT  │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Registry Context                               │         │
│  │  └─ Programs (jarvis-local-resources-db,       │         │
│  │       port 5435, verified)                      │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  Grounding Instruction (WV-first for WV queries)            │
│      ↓                                                       │
│  User Query                                                  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> Figure 7‑5. Structure of contextual input assembled for language‑model reasoning, now including GBIM Landowner Context as a distinct block when the landowner_gbim routing mode is active.

---

## 7.6 Constraints, Provenance, and Logging

**Pre‑retrieval and retrieval‑time constraints.**
Collection selection and filter mechanisms support limiting retrieval by collection, source, county, dataset, worldview, and state. The `gbim_query_router` enforces the ethical constraint that only `LANDOWNER_CORPORATE` and `LANDOWNER_GOVERNMENT` proposition codes are returned — individual residential owner names are not present in `mvw_gbim_landowner_spatial` and cannot be returned. For WV‑scoped queries, context assembly enforces a hard separation between WV evidence (community memories + RAG + PostgreSQL `gisdb` + landowner beliefs + registries) and generic web content.

**Decoding‑time guards.**
After retrieval and generation, the main brain routes candidate responses through the blood–brain barrier service. The BBB output guard (`apply_output_guards_async`) is fail-open on HTTP 500 (content passes through unchanged, failure is logged). In WV‑scoped flows, the guardrail is applied after the WV‑first context and instructions have already constrained the ensemble's behavior.

```
┌─────────────────────────────────────────────────────────────┐
│       Provenance and Guardrail Flow in RAG Pipeline         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Query → Phase 1.45 → Retrieval (all logged)               │
│    ↓                                                         │
│  Sources Captured:                                          │
│    -  autonomous_learner top-5 (Phase 1.45)                  │
│    -  ChromaDB collections queried (port 8000)               │
│    -  PostgreSQL tables accessed (msjarvis/gisdb port 5433)  │
│    -  mvw_gbim_landowner_spatial (msjarvisgis port 5432)     │
│       via gbim_query_router (port 7205)                     │
│    -  jarvis-local-resources-db rows (port 5435)             │
│    -  Metadata filters applied                               │
│    ↓                                                         │
│  Context Assembly (with provenance)                         │
│    ↓                                                         │
│  21-LLM Ensemble → LM Synthesizer (llama3.1:latest)        │
│    ↓                                                         │
│  Blood-Brain Barrier (guardrails — fail-open on HTTP 500)  │
│    -  Constitutional check                                    │
│    -  Safety validation                                       │
│    -  WV-first enforcement (for WV queries)                  │
│    ↓                                                         │
│  Response (with logged sources)                             │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> Figure 7‑6. Provenance and guardrail flow ensuring accountable generation in the Ms. Jarvis retrieval pipeline, now including `mvw_gbim_landowner_spatial` via `gbim_query_router` in the logged source list.

**Post‑hoc review and logging.**
Logs capture which services were called, which collections were queried, which PostgreSQL tables and views were accessed (including `mvw_gbim_landowner_spatial` and which port/database it was served from), Phase 1.45 community memory results, which filters and scores were applied, which registries were accessed, and which documents or features were returned.

---

## 7.7 Relation to Long‑Term Memory, GeoDB, Registries, and Entanglement

**Long‑term memory.**
ChromaDB collections hold embedded representations at **384 dimensions (`all-minilm:latest`)**: `gbim_worldview_entities` (5,416,521 entities), `autonomous_learner` (21,181 items, growing ~288/day), `gis_wv_benefits`, and 10+ additional collections. Structured tables such as `jarvis-local-resources-db` (port 5435) hold normalized, versioned records addressable via RAG‑inferred keys. PostgreSQL `msjarvis` and `gisdb` (port 5433) encode belief graphs and spatial bodies reachable via `entity_id`, `source_table`, and `source_pk` fields returned in ChromaDB metadata. The GBIM landowner materialized view `mvw_gbim_landowner_spatial` in `msjarvisgis` (port 5432) holds 20,593 verified institutional landowner beliefs queryable via `gbim_query_router` (port 7205) — not embedded in ChromaDB, but fully integrated into the WV-first context assembly pipeline.

**Short‑term context.**
Each retrieval call assembles a temporary context window from Phase 1.45 community memories plus retrieved items, sorted by relevance and grouped by collection, layer, registry, and router. For WV‑scoped queries, this window is explicitly WV‑first: assembled from community memories, West Virginia RAG, PostgreSQL `gisdb` GIS, GBIM landowner beliefs, and registry material, with web content excluded.

**Coupled updates and future entanglement.**
The broader entanglement concept envisions updates to semantic memory, PostgreSQL spatial layers, registries like `jarvis-local-resources-db`, GBIM belief structures, landowner belief records, and normative constraints as mutually influencing. The `autonomous_learner`'s continuous growth (21,181 items → ~288/day) represents the beginning of this coupled update loop. As WV assessor data is refreshed and new parcel records are ingested into `mvw_gbim_landowner_spatial`, the landowner belief layer will be updated and `gbim_query_router` results will reflect those changes automatically on the next materialized view refresh.

In this way, the present retrieval deployment should be understood as a working but intentionally conservative layer — already anchored in named collections, Phase 1.45 community memory, explicit retrieval calls, structured registry lookups, and a PostgreSQL-native landowner path that makes the most consequential form of institutional power over place directly queryable by natural language.

*Last updated: 2026-03-20 by Carrie Kidd (Mamma Kidd), Mount Hope WV*
