## Why this matters for Polymathmatic Geography

This chapter specifies how Ms. Jarvis's language models are bound to *place‑aware, collection‑aware, and registry‑aware memory* instead of free‑floating text generation. It makes the Hilbert‑space representation, GBIM structures, ChromaDB‑backed semantic memory, and the verified local resource registry from earlier chapters operational by defining concrete services that retrieve from semantic memory, the spatial body, the web, and structured program tables. In the current deployment, this design is realized as a production RAG stack that delivers West Virginia benefits intelligence through a 21‑model consciousness bridge anchored in ChromaDB, GBIM‑derived entities from the PostgreSQL `msjarvis` database (port 5433), GIS‑aware collections, and a WV‑first routing policy. It supports:

- **P1 – Every where is entangled** by requiring that answers emerge from an entangled memory of governance texts, spatial layers, research notes, belief structures from PostgreSQL GBIM tables, and local resource registries, rather than from an abstract model prior.

- **P3 – Power has a geometry** by letting retrieval paths expose which collections—and thus which institutional, spatial, and programmatic perspectives—shape a given answer, including WV‑specific benefits facilities in `gis_wv_benefits`, spatial entities derived from PostgreSQL GBIM and `gisdb`, and benefits‑focused resource collections.

- **P5 – Design is a geographic act** by treating routing rules, collection choices, registry lookups, and gateway boundaries as design decisions that change how the system "sees" and acts within a region.

- **P12 – Intelligence with a ZIP code** by privileging West Virginia‑specific collections in retrieval, and by coupling text RAG both to a state‑scale PostgreSQL `gisdb`/GBIM spatial body (port 5433, 13 GB, 39 tables, 5,416,521 verified beliefs in `msjarvis`) for spatial questions and to a ZIP‑ and county‑aware `jarvis-local-resources-db` registry (port 5435) for concrete program referrals, including flows for Oak Hill, Beckley, and broader Fayette/Raleigh County.

- **P16 – Power accountable to place** by making retrieval calls, filters, scores, registry lookups, and sources visible at the API and logging layer so that communities and researchers can audit what informed a Steward response.

As such, this chapter belongs to the **Computational Instrument** tier: it defines the retrieval and routing machinery that connects ChromaDB‑backed semantic memory (port 8000), the PostgreSQL GBIM/`gisdb` spatial body (5,416,521 verified beliefs, 39 PostGIS tables), the verified local resource registry (`jarvis-local-resources-db`, port 5435), and web research to the live outputs of Ms. Jarvis.

---

## 7.0 Overview and Scope

This chapter describes the retrieval‑augmented generation (RAG) infrastructure that binds Ms. Egeria Jarvis's language models to the semantic and spatial memory systems defined in earlier chapters. In the current deployment, language models are no longer queried "from scratch": they are constrained and informed by:

- a **Phase 1.45 semantic community memory step** that prepends the top-5 most relevant `autonomous_learner` memories (21,181 items) to every query before it reaches the LLM ensemble,
- a text RAG service backed by a shared HTTP‑exposed ChromaDB instance (port 8000),
- a `gisdb`‑coupled GIS RAG path for West Virginia features built on GBIM‑derived spatial entities from the PostgreSQL `msjarvis` / `gisdb` databases (port 5433) and `gis_wv_benefits`,
- a web‑research gateway, and
- a resolver path into the `jarvis-local-resources-db` registry (port 5435) for programmatic help,

all orchestrated by the main brain and blood–brain‑barrier services.

At runtime, queries enter through a unified HTTP gateway (for example, `POST /chat` or `POST /chat/async` on the main‑brain port) and are routed by the executive coordinator into a RAG layer that spans ChromaDB collections, PostgreSQL GIS features, and verified local‑resource rows. In production as of March 18, 2026, the full pipeline:

```text
Unified Gateway → Main Brain → Phase 1.45 Community Memory → RAG (text + GIS + registry, WV‑first) → 21‑LLM ensemble → Blood–Brain Barrier
```

is live and serving West Virginia benefits and geography questions. For WV‑scoped queries, the main brain treats West Virginia RAG as mandatory and suppresses generic web context when a county or WV role/profile is present, so that out‑of‑state material cannot quietly override in‑state evidence.

> **⚠️ Critical: Embedding Model Lock**  
> All ChromaDB collections — including `gbim_worldview_entities` (5,416,521 entities), `autonomous_learner` (21,181 items), `gis_wv_benefits`, and all semantic collections — use **384-dimensional vectors** produced by **`all-minilm:latest`** (pulled March 17, 2026, via `jarvis-ollama:11434/api/embeddings`). The `nomic-embed-text` model produces **768-dimensional vectors** and is **incompatible** with all existing collections. Any service, script, or migration that generates embeddings for ChromaDB **must** use `all-minilm:latest`. This includes Phase 1.45, text RAG, GIS RAG, the autonomous learner, and any new collection ingestion.

A typical benefits query such as:
```bash
curl -X POST http://127.0.0.1:8050/chat/sync \
  -H "Content-Type: application/json" \
  -H "X-API-Key: super-secret-key" \
  -d '{"message":"Oak Hill WV county benefits","county":"Fayette","role":"community","profile":"auto"}'
```

triggers Phase 1.45 community memory retrieval from `autonomous_learner`, then retrieval from ChromaDB (including WV‑relevant collections such as governance, thesis, and `gis_wv_benefits`), optional GIS RAG over GBIM‑derived spatial entities from PostgreSQL `gisdb`, synthesis by the 21‑model ensemble, and post‑filtering by the guardrail service, with WV RAG, GIS context from PostgreSQL, and `jarvis-local-resources-db` treated as authoritative when they conflict with external web information.

Within the overall architecture, the RAG layer is the primary bridge between relatively slow‑changing long‑term memory (ChromaDB collections, PostgreSQL `msjarvis`/`gisdb` at port 5433, and structured registries like `jarvis-local-resources-db` at port 5435) and fast, per‑query reasoning in the language models. It is also the place where the Hilbert‑space state metaphor becomes operational: each RAG call carves out a small, query‑conditioned subspace of the much larger semantic, spatial, institutional, and program state space, and hands that subspace to the models as their working context. Finally, the retrieval services provide concrete, inspectable interfaces where retrieval calls, filters, and source collections can be logged, audited, and tuned in service of the program's glassbox and spatial‑justice commitments.

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

> Figure 7‑1. Retrieval‑augmented generation (RAG) pipeline overview linking the unified gateway, Phase 1.45 community memory, main‑brain orchestration, and ensemble‑guarded outputs.

---

## 7.1 Alignment with GBIM, Hilbert Space, Semantic Memory, GeoDB, and Registries

The GeoBelief Information Model (GBIM) defines how entities, places, and normative claims are represented across documents and spatial features in the PostgreSQL `msjarvis` database (port 5433, 8 MB, 6 tables). The RAG layer is the mechanism that actually retrieves those GBIM‑anchored fragments when a question is asked. GBIM worldview entities and other beliefs from PostgreSQL are surfaced into ChromaDB as metadata‑rich records in `gbim_worldview_entities` (5,416,521 entities), and the RAG services are structured so they can filter, group, and boost results by these identifiers as metadata coverage matures.

The Hilbert‑space state view treats the system's overall knowledge and constraints as a very high‑dimensional state vector. RAG interactions can be understood as projections into lower‑dimensional subspaces that correspond to "what matters for this query, given this role and place." For text, those projections are implemented as embedding‑based nearest‑neighbor searches in ChromaDB collections using **384-dimensional vectors from `all-minilm:latest`**. For space, they are implemented as centroid‑based spatial filters over PostgreSQL `gisdb`‑derived features and as neighborhood queries over GBIM‑linked spatial entities. For concrete help‑seeking and program questions, retrieved resource documents and metadata are further resolved into rows of `jarvis-local-resources-db` (port 5435) keyed by ZIP, county, and program type, which are themselves part of the structured Hilbert‑space state.

ChromaDB‑backed semantic memory (Chapter 5) is the substrate for governance texts, thesis fragments, research notes, GBIM worldview entities, and resource guides, while PostgreSQL `gisdb` (Chapter 6) defines the spatial body composed of PostGIS layers and exported worldview entities. The text RAG server is the front‑door to semantic memory: it queries explicitly named ChromaDB collections, respects metadata filters such as source, county, dataset, or worldview, and returns scored snippets along with their provenance. The GIS RAG service plays the parallel role for the spatial body: it queries geospatial collections such as GBIM‑derived spatial entities and `gis_wv_benefits`, and returns entities with dataset names, centroids, and core attributes. For local‑resource questions, a dedicated resolver component uses RAG outputs and structured hints (such as county, ZIP, `resource_type`, and `local_resource_id`) to look up matching rows in `jarvis-local-resources-db`, ensuring that final recommendations rest on explicit, versioned program records rather than unstructured text alone.

In the March 2026 deployment, this alignment is implemented concretely:

- ChromaDB collections like `gbim_worldview_entities` (consolidated GBIM spatial index), `autonomous_learner` (21,181 items, queried at Phase 1.45), `gis_wv_benefits`, `psychological_rag` (968 items), `appalachian_cultural_intelligence` (5 items), `spiritual_texts` (23 items), `gbim_beliefs_v2`, and others are configured at **384 dimensions (`all-minilm:latest`)** and accessed over a shared HTTP ChromaDB service at port 8000.
- GIS RAG queries can reference metadata such as `worldview_id`, `county`, `dataset`, and `gbim_entity` to tie vector results back to PostgreSQL `msjarvis` GBIM and `gisdb`.
- Resource‑related collections tag documents with `local_resource_id`, allowing RAG hits to be resolved to `jarvis-local-resources-db` rows for facilities in Oak Hill, Beckley, and surrounding ZIP codes, as those registries are populated and verified.

**Database Integration (Three-Database Architecture):**
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

# PostgreSQL jarvis-local-resources-db — port 5435
pg_conn_resources = psycopg2.connect(
    host="localhost", port=5435,
    database="jarvis-local-resources-db",
    user="postgres", password="postgres"
)

# ChromaDB semantic memory — port 8000
# REQUIRED: all-minilm:latest (384-dim) — DO NOT use nomic-embed-text (768-dim)
chroma_client = chromadb.HttpClient(host="127.0.0.1", port=8000)

# Example: Retrieve GBIM beliefs for RAG
cursor = pg_conn_msjarvis.cursor()
cursor.execute("""
    SELECT belief_id, proposition, belief_state, confidence_decay
    FROM gbim_beliefs
    WHERE entity_id = %s
""", (entity_id,))
beliefs = cursor.fetchall()

# Embed and index in ChromaDB using all-minilm:latest
collection = chroma_client.get_collection("gbim_beliefs_v2")
```

---

## 7.2 Core RAG and Search Components

At the implementation level, the retrieval layer consists of Phase 1.45 community memory retrieval, four main retrieval services, a registry resolver, and orchestration:

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

> Figure 7‑2. Core retrieval components composing the Ms. Jarvis RAG layer, including Phase 1.45 community memory retrieval.

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

> **Critical:** The embedding model **must** be `all-minilm:latest` (384-dim). Using `nomic-embed-text` (768-dim) will cause a dimension mismatch error against all existing ChromaDB collections. This applies to Phase 1.45, text RAG, GIS RAG, and any other ChromaDB write or query operation.

### 7.2.1 Text RAG Service (ChromaDB‑Backed)

The text RAG service exposes a structured HTTP API used by main‑brain chat paths that takes a query string, a `top_k` parameter, optional metadata filters (such as collection, source, county, dataset, or worldview), and optional role and geography hints. It issues similarity searches against one or more ChromaDB collections using **`all-minilm:latest` (384-dimensional embeddings)**, and returns both a flat list of top results and a `results_by_source` mapping keyed by collection name. Each result item carries:

- The retrieved text snippet or document identifier.
- Collection and source names.
- Metadata fields (for example, dataset, `worldview_id`, county, `local_resource_id`).
- A similarity‑derived score.

**Active collections for text RAG (March 18, 2026):**

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

From the Hilbert‑space perspective, each collection represents a finite subset of the component spaces \(H_{\text{text}}, H_{\text{geo}}, H_{\text{inst}}\), and the RAG query selects a neighborhood around the embedded query vector. From the GBIM perspective, the same calls return belief fragments whose provenance and `worldview_id` can be inspected and composed, with source data traceable back to PostgreSQL `msjarvis`.

### 7.2.2 GIS RAG Service (PostgreSQL `gisdb`/GBIM‑Backed, port 8004)

The GIS RAG service is a dedicated geospatial retrieval path that serves West Virginia‑focused spatial questions. It exposes an endpoint that accepts a natural‑language query and an `n_results` parameter and returns a list of spatial hits. Internally, it queries:

- `gbim_worldview_entities` — 5,416,521 embeddings of West Virginia geospatial features from PostgreSQL `gisdb` / `msjarvis`, and
- `gis_wv_benefits` — semantic descriptions and metadata for benefits‑related facilities such as Oak Hill hubs and Beckley DHHR offices.

Each indexed entity stores a short text description and metadata fields such as `worldview_id`, `dataset`, `county`, `gbim_entity`, `centroid_x`, and `centroid_y` (SRID 26917, also transformed to EPSG:4326 for map display). Metadata links back to `msjarvis.gbim_beliefs` (via `entity_id`) and `gisdb.zcta_wv_centroids` (993 WV ZIP centroids, via `zip`).

All embeddings use **`all-minilm:latest` (384-dim)**. Example:

```python
import chromadb

client = chromadb.HttpClient(host="127.0.0.1", port=8000)
col = client.get_or_create_collection("gis_wv_benefits")

col.add(
    documents=[
        "Oak Hill WV FAYETTE County SNAP WIC Medicaid hub (New River Health District)",
        "Beckley WV DHHR benefits office social services hub",
        "New River Health Oak Hill clinic medical assistance"
    ],
    metadatas=[
        {"worldview_id": "wv_benefits_2026", "county": "Fayette",
         "gbim_entity": "oak_hill_fayette_corrected"},
        {"worldview_id": "wv_benefits_2026", "county": "Raleigh",
         "gbim_entity": "beckley_dhhr"},
        {"worldview_id": "wv_benefits_2026", "county": "Fayette",
         "gbim_entity": "new_river_health"}
    ],
    ids=["gbim001", "gbim002", "gbim003"]
)
# NOTE: embeddings generated automatically by ChromaDB using all-minilm:latest
# Do NOT pass pre-computed nomic-embed-text vectors to this collection
```

GIS RAG outputs are composable with text RAG outputs: each hit is both a semantic object (a facility, boundary, or infrastructure feature) and a spatial object (with coordinates, SRID, and GBIM identifiers traceable to PostgreSQL `gisdb`) that the main brain can reason about in the same Hilbert‑space frame.

### 7.2.3 Web‑Research Gateway

External web retrieval is handled by a dedicated gateway rather than allowing arbitrary outbound calls from each agent or service. This gateway exposes an HTTP endpoint that accepts a JSON body with a query string and a limit on the number of results. It:

- Applies policy filters and rate limits to outbound web access.
- Normalizes results into a uniform structure with fields like `title`, `snippet`, `url`, `source`, and sometimes `published_at`.
- Logs queries and responses for audit and debugging.

In the WV‑first design, the main brain only admits web context into the ultimate context window for non‑WV or clearly extra‑state questions. When a query is WV‑scoped (for example, has a West Virginia county or uses a WV benefits profile/role), web context is deliberately excluded so that external search results cannot override the in‑state RAG, GIS (from PostgreSQL), and registry evidence.

### 7.2.4 Local Resource Registry Resolver (`jarvis-local-resources-db`, port 5435)

The local resource resolver is a thin service or module that sits alongside text and GIS RAG. It does not perform embedding search itself. Instead, it:

- Accepts structured hints such as `county`, `zip`, and `resource_type`, plus optional keys such as `local_resource_id` coming from RAG metadata.
- Queries `jarvis-local-resources-db` (port 5435) for rows that match these constraints and have an acceptable `verification_status`.
- Returns normalized program records with fields like `name`, `description`, `contact_phone`, `contact_email`, `url`, `zip_coverage`, `last_verified_at`, and internal IDs.

In help‑seeking flows, the main brain uses RAG primarily to interpret the question and surface relevant resource descriptions, then delegates final program selection to this resolver so that recommendations are grounded in a maintained, auditable registry rather than in unstructured text alone.

> **Known Issue — OPEN as of March 18, 2026:** `jarvis-local-resources-db` returns empty results for Mount Hope and Fayette County queries because verified community resource data has not yet been loaded. LLMs fall back to training data for local specifics. Factually accurate programs (LIHEAP, WV 2-1-1) pass the BBB. Fabricated organization names are blocked by the ethical filter. Resolution: Community Champions data entry is the next priority.

### 7.2.5 Orchestration and Main Brain

The main brain does not typically call language models directly. Instead, it routes each job through an orchestration layer that decides whether to invoke Phase 1.45 community memory, the text RAG service, the GIS RAG service (which queries PostgreSQL-sourced spatial entities via `gisdb`), the web gateway, the local resource resolver, or some combination, based on:

- The request type (for example, policy question, spatial query, resource lookup, system status).
- The active role (for example, researcher, governance engineer, community‑facing advisor).
- Any explicit or inferred geography (for example, county, ZIP, worldview region).

The same orchestration layer composes the final context window for the models and sends candidate responses through downstream guardrail services such as the blood–brain barrier.

In the March 2026 deployment, orchestration calls into the 21‑model ensemble service, which queries a set of model proxies and aggregates their outputs. The LM Synthesizer (port 8001, Phase 3.5) then calls `jarvis-ollama:11434/api/generate` directly with `llama3.1:latest` and the Ms. Egeria Jarvis persona prompt injected.

For WV‑scoped queries, the main brain:

- Fires Phase 1.45 community memory retrieval first (top-5 `autonomous_learner` memories prepended to `enhanced_message`).
- Treats West Virginia RAG (text + GIS from PostgreSQL `gisdb` + registry) as mandatory input.
- Builds a WV‑first context window from RAG, GIS, and registry material, excluding `web_context`.
- Prepends a strong grounding instruction that explicitly tells the ensemble to treat WV RAG, GIS context from PostgreSQL `gisdb`, and `jarvis-local-resources-db` as authoritative for West Virginia and to ignore conflicting out‑of‑state information unless the user clearly asks about another state.

Ensemble outputs are then filtered by the blood–brain‑barrier and returned via unified chat endpoints. Async queries use the Redis-backed job API (`/chat/async`, `/chat/status/{job_id}`, `/chat/cancel/{job_id}`).

---

## 7.3 Retrieval Flows

This section sketches the typical flows for non‑spatial, spatial, and resource‑oriented queries. In each case, the retrieval layer is where abstract Hilbert‑space projections and GBIM entities from PostgreSQL become concrete calls and responses.

### 7.3.1 Non‑Spatial RAG Flow

A typical governance or thesis question progresses as follows:

**Query intake.**  
A user or upstream component sends a request to the unified gateway or main brain. The coordinator wraps it into an internal job structure containing the raw text, any structured fields (project, county, worldview), and role hints.

**Phase 1.45 — Community memory retrieval.**  
Before any other RAG service is invoked, the main brain embeds the query via `all-minilm:latest` and retrieves the top-5 most similar records from `autonomous_learner` (21,181 items). These are prepended to `enhanced_message`.

**Routing to text RAG and/or web.**  
The orchestration logic decides whether to call the local text RAG service, the web gateway, or both. For most governance‑ and thesis‑style questions, it prefers ChromaDB‑backed collections (for example, governance, thesis, GBIM, or MountainShares collections) and only consults the web when the question clearly depends on external or time‑varying facts.

**Retrieval from ChromaDB (384-dim, `all-minilm:latest`).**  
The text RAG service embeds the query, runs similarity search against the selected collections, and returns high‑scoring documents and their metadata. Collection selection and metadata filters act as an early constraint layer, narrowing the effective Hilbert‑space subspace.

**Context assembly.**  
The orchestration layer merges the retrieved items — Phase 1.45 community memories, text RAG results, and any web‑research snippets (if allowed) — into a context window alongside system prompts and role‑specific instructions. Source separation is preserved so governance texts, GBIM descriptions from PostgreSQL, and thesis excerpts remain distinguishable.

**Generation and guarding.**  
One or more language models generate an answer conditioned on this assembled context. The LM Synthesizer (Phase 3.5) applies the Ms. Egeria Jarvis persona via `jarvis-ollama:11434/api/generate` with `llama3.1:latest`. The main brain then routes the candidate answer through the blood–brain barrier service.

### 7.3.2 Spatial RAG Flow

```
┌─────────────────────────────────────────────────────────────┐
│   Spatial RAG: Semantic + Geographic Retrieval               │
├─────────────────────────────────────────────────────────────┤
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
└─────────────────────────────────────────────────────────────┘
```

> Figure 7‑3. Semantic (embedding‑based) and spatial (geographic‑filter) retrieval operations using ChromaDB port 8000, `gisdb` port 5433, and `msjarvis` port 5433.

Spatially explicit questions (for example, "roads in Fayette County," "hospitals near Oak Hill," or "which buildings lie in this floodplain?") introduce the GIS RAG path:

**Spatial query intake.**  
The main brain or a spatially aware client calls the GIS RAG endpoint (port 8004) with a natural‑language query and `n_results`, and may additionally pass a center point, bounding box, county, or GBIM region identifier if known.

**Semantic and spatial retrieval.**  
The GIS RAG service embeds the query using `all-minilm:latest` (384-dim) and runs similarity search over geospatial ChromaDB collections. Because each entity includes centroids and region metadata sourced from PostgreSQL `gisdb`, the service can apply geometric or administrative filters by querying `gisdb.zcta_wv_centroids` (993 WV ZIP centroids) or joining to `msjarvis.gbim_beliefs` for temporal decay metadata.

**Return of geospatial hits.**  
The service returns a list of hits, each including a compact textual description, the source dataset or layer name, a feature label, metadata (`worldview_id`, `dataset`, `county`, `gbim_entity`), and coordinates. Upstream, these hits can be shown in map or tabular form, used to fetch richer GBIM records or PostgreSQL `gisdb` PostGIS geometries, or combined with text RAG results and registry entries.

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

Routing is conceptually central to the RAG design. It is meant to be GBIM‑aware, role‑aware, geography‑aware, registry‑aware, and explicitly WV‑first for West Virginia–scoped questions.

### 7.4.1 Design Intent

**Topic and intent routing.**  
The system distinguishes between queries about governance, geospatial context, thesis theory, MountainShares economics, resource and referral questions, and infrastructure status, routing each toward appropriate services and collections. Governance queries favor charters, policies, and DAO records; spatial‑justice queries favor PostgreSQL `gisdb`/`msjarvis`‑derived collections; resource questions favor `jarvis-local-resources-db` plus WV‑resource collections.

**Role‑aware routing.**  
The active role (for example, researcher, governance engineer, community‑facing advisor) determines which collections and registries are eligible. Internal or sensitive material is only surfaced for trusted roles, while community‑facing roles are restricted to public documentation, approved spatial layers, and public‑facing slices of `jarvis-local-resources-db`.

**Geography‑aware routing and WV‑first behavior.**  
Queries with explicit or implicit place references steer retrieval toward collections encoding GBIM entities from PostgreSQL, GBIM‑derived spatial entities, PostgreSQL `gisdb`/PostGIS features, and `jarvis-local-resources-db` rows in the relevant region. For West Virginia, whenever a query is WV‑scoped, the system:

- Treats WV RAG, PostgreSQL `gisdb` GIS, and registry context as the authoritative sources.
- Excludes web context from the final assembled context window.
- Requires models to ignore conflicting out‑of‑state content unless the user explicitly requests another state.

### 7.4.2 Current Implementation

```
┌─────────────────────────────────────────────────────────────┐
│     Intelligence with a ZIP Code - WV Geographic Routing     │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Query: "food assistance Fayette County WV"                 │
│      ↓                                                       │
│  WV-Scoped Detection:                                       │
│    -  County = "Fayette"                                      │
│    -  State = "WV"                                            │
│    -  Profile = "benefits"                                    │
│      ↓                                                       │
│  Phase 1.45 — Community Memory:                             │
│    all-minilm:latest → autonomous_learner → top-5 prepended │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  PostgreSQL msjarvis (port 5433)               │         │
│  │  Query: GBIM beliefs for Fayette County        │         │
│  │  Tables: gbim_beliefs, gbim_worldviews         │         │
│  │    ↓                                            │         │
│  │  PostgreSQL gisdb (port 5433)                  │         │
│  │  Query: zcta_wv_centroids for Fayette ZIPs     │         │
│  │    ↓                                            │         │
│  │  ChromaDB gis_wv_benefits (port 8000)          │         │
│  │  Filter: {county: "Fayette", type: "food"}     │         │
│  │    ↓                                            │         │
│  │  jarvis-local-resources-db (port 5435)         │         │
│  │  Filter: county='Fayette', verified=true       │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  WV-First Context Assembly:                                 │
│    -  INCLUDE: community memories + WV RAG +                 │
│               PostgreSQL GIS + registry                     │
│    -  EXCLUDE: web_context (out-of-state suppressed)        │
│      ↓                                                       │
│  Grounding Instruction:                                     │
│    "Treat WV RAG, PostgreSQL GIS, and                       │
│     jarvis-local-resources-db as authoritative.             │
│     Ignore conflicting external info."                      │
│      ↓                                                       │
│  21-LLM Ensemble → LM Synthesizer (llama3.1:latest)        │
│      → Response                                             │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> Figure 7‑4. Geography‑aware routing and data prioritization in the Ms. Jarvis retrieval layer for Fayette and Raleigh Counties, West Virginia.

As of March 18, 2026:

- The text RAG API exposes optional `role` and `geography` fields and uses them to choose which ChromaDB collections to query. All collections use 384-dim `all-minilm:latest` embeddings. WV‑specific benefits and governance collections are explicitly favored for WV benefits flows.
- Phase 1.45 fires for every query, ensuring community memory is always prepended before LLM reasoning.
- The GIS RAG service (port 8004) is focused on West Virginia, indexing GBIM‑ and PostgreSQL `gisdb`‑derived layers and benefits facilities (`gis_wv_benefits`), with centroids standardized to SRID 26917.
- The local resource resolver is wired to `jarvis-local-resources-db` (port 5435) and can be called explicitly when a flow is tagged as resource‑oriented.
- In the main brain's ultimate path, context assembly computes a WV‑scoped flag based on county and role, builds a `context_block` from `[community_memories, rag_context, gis_context, registry_context]` for WV queries (dropping `web_context`), and injects a strong WV grounding instruction.

---

## 7.5 Context Construction and Structure

**Source separation.**  
The text RAG service returns a `results_by_source` dictionary keyed by collection name, and each item carries `collection`, `source`, and `metadata` fields. Phase 1.45 community memories are prepended as a distinct block. The GIS RAG service returns dataset names and feature labels with spatial metadata traceable to PostgreSQL `gisdb`. The local resource resolver returns normalized rows from `jarvis-local-resources-db` with clearly typed fields.

**Relevance ordering and bounded size.**  
ChromaDB returns distances, which the services convert into scores; flat results are sorted in descending score order. Clients specify `top_k` per collection or `n_results` per GIS query, and the services enforce these limits. Phase 1.45 is hard-capped at top-5 results.

**Role‑, geography‑, and WV‑aware scaffolding.**  
Where role and geography are known, upstream prompt builders add headers or structure that make those constraints explicit. For WV‑scoped queries, the ultimate prompt spells out that WV RAG and PostgreSQL `gisdb` context are authoritative, that web snippets are absent, and that any registry entries included represent current, community‑governed knowledge of local programs.

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

> Figure 7‑5. Structure of contextual input assembled for language‑model reasoning, including Phase 1.45 community memories as the first enrichment block.

---

## 7.6 Constraints, Provenance, and Logging

**Pre‑retrieval and retrieval‑time constraints.**  
Collection selection and filter mechanisms support limiting retrieval by collection, source, county, dataset, worldview, and state. The APIs include `role` and `geography` fields that govern access‑level and spatial filters. For WV‑scoped queries, context assembly enforces a hard separation between WV evidence (community memories + RAG + PostgreSQL `gisdb` + registries) and generic web content.

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

> Figure 7‑6. Provenance and guardrail flow ensuring accountable generation in the Ms. Jarvis retrieval pipeline.

**Post‑hoc review and logging.**  
The retrieval server and main brain support background storage of queries and responses into `conversation_history` and `episodic_index` ChromaDB collections (both active as of March 18, 2026). Logs capture which services were called, which collections were queried, which PostgreSQL tables were accessed, Phase 1.45 community memory results, which filters and scores were applied, which registries were accessed, and which documents or features were returned.

---

## 7.7 Relation to Long‑Term Memory, GeoDB, Registries, and Entanglement

**Long‑term memory.**  
ChromaDB collections hold embedded representations at **384 dimensions (`all-minilm:latest`)**: `gbim_worldview_entities` (5,416,521 entities), `autonomous_learner` (21,181 items, growing ~288/day), `gis_wv_benefits`, and 10+ additional collections. Structured tables such as `jarvis-local-resources-db` (port 5435) hold normalized, versioned records addressable via RAG‑inferred keys. PostgreSQL `msjarvis` and `gisdb` (port 5433) encode belief graphs and spatial bodies reachable via `entity_id`, `source_table`, and `source_pk` fields returned in ChromaDB metadata. All 5,416,521 GBIM entities carry `confidence_decay` and `needs_verification` temporal metadata.

**Short‑term context.**  
Each retrieval call assembles a temporary context window from Phase 1.45 community memories plus retrieved items, sorted by relevance and grouped by collection, layer, and registry. For WV‑scoped queries, this window is explicitly WV‑first: assembled from community memories, West Virginia RAG, PostgreSQL `gisdb` GIS, and registry material, with web content excluded.

**Coupled updates and future entanglement.**  
The broader entanglement concept envisions updates to semantic memory, PostgreSQL spatial layers, registries like `jarvis-local-resources-db`, GBIM belief structures, and normative constraints as mutually influencing. The current implementation provides a stable, inspectable interface that can later be extended with richer entanglement‑aware routing, access policies, and metadata propagation across collections and registries, including automated updates when WV program verification or worldview changes occur in PostgreSQL. The `autonomous_learner`'s continuous growth (21,181 items → ~288/day) represents the beginning of this coupled update loop: community interactions are continuously embedded and fed back into Phase 1.45 retrieval.

In this way, the present retrieval deployment should be understood as a working but intentionally conservative layer. It already anchors Ms. Jarvis's outputs in named collections, Phase 1.45 community memory, explicit retrieval calls, and structured registry lookups — including a concrete WV‑first path from PostgreSQL `msjarvis`/`gisdb` spatial features and from `jarvis-local-resources-db` program records into generation — but it still relies on forthcoming work in metadata design, spatial integration, registry governance, and explanation tooling to fully satisfy the program's glassbox and spatial‑justice commitments.

*Last updated: 2026-03-18 by Carrie Kidd, Mount Hope WV*
