# 7. RAG Pipeline and Routers

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: April 23, 2026*

---

## Why This Matters for Polymathmatic Geography

This chapter specifies how Ms. Allis's language models are bound to place-aware,
collection-aware, and registry-aware memory instead of free-floating text generation.
It makes the Hilbert-space representation, GBIM structures, ChromaDB-backed semantic
memory, and the verified local resource registry from earlier chapters operational by
defining concrete services that retrieve from semantic memory, the spatial body, the
web, and structured program tables. In the current deployment, this design is realized
as a production RAG stack that delivers West Virginia benefits intelligence through a
multi-model consciousness bridge anchored in ChromaDB, GBIM-derived entities from the
PostgreSQL `msallisgis` database (two-container architecture — see §7.1), GIS-aware
collections, and a WV-first routing policy. It supports:

- **P1 – Every where is entangled** by requiring that answers emerge from an entangled
  memory of governance texts, spatial layers, research notes, belief structures from
  PostgreSQL GBIM tables, and local resource registries, rather than from an abstract
  model prior.
- **P3 – Power has a geometry** by letting retrieval paths expose which collections —
  and thus which institutional, spatial, and programmatic perspectives — shape a given
  answer, including WV-specific benefits facilities in `gis_wv_benefits`, spatial
  entities derived from PostgreSQL GBIM and `msallisgis`, and benefits-focused resource
  collections.
- **P5 – Design is a geographic act** by treating routing rules, collection choices,
  registry lookups, and gateway boundaries as design decisions that change how the system
  "sees" and acts within a region.
- **P12 – Intelligence with a ZIP code** by privileging West Virginia-specific
  collections in retrieval, and by coupling text RAG to a state-scale PostgreSQL
  `msallisgis` spatial body — accessible via two containers: `msallis-db` (production,
  host 5433 / container 5432, role `postgres`, 16 GB / 294 tables / 11 schemas) and
  `postgis-forensic` (forensic, host 5432, role `allis`, 17 GB / 314 tables / 9
  schemas) — and a ZIP- and county-aware `allis-local-resources-db` registry (port
  5435) for concrete program referrals, including flows for Mount Hope, Oak Hill,
  Beckley, and broader Fayette/Raleigh County.
- **P16 – Power accountable to place** by making retrieval calls, filters, scores,
  registry lookups, and sources visible at the API and logging layer so that communities
  and researchers can audit what informed a Steward response.

This chapter belongs to the **Computational Instrument** tier: it defines the retrieval
and routing machinery that connects ChromaDB-backed semantic memory (`allis-chroma`,
host port **8002**, container port **8000**), the PostgreSQL `msallisgis` spatial body,
the verified local resource registry (`allis-local-resources-db`, port 5435), and web
research to the live outputs of Ms. Allis.

As of April 17, 2026, live responses are validated by `judge_pipeline_v2.1-rag-grounded`
and truth metrics are exposed under `truthverdict.*`. The older
`heuristic_contradiction_v1` validator is superseded. All five open issues documented in
prior drafts (OI-05, OI-19, OI-20, OI-21, OI-22) are closed as of April 17, 2026.
See §7.9.

---

## 7.0 Overview and Scope

This chapter describes the retrieval-augmented generation (RAG) infrastructure that
binds Ms. Egeria Allis's language models to the semantic and spatial memory systems
defined in earlier chapters. In the current deployment, language models are no longer
queried "from scratch": they are constrained and informed by:

- a Phase 1.45 semantic community memory step that prepends the top-5 most relevant
  `autonomous_learner` memories to every query before it reaches the LLM ensemble,
- a text RAG service backed by a shared HTTP-exposed ChromaDB instance (`allis-chroma`,
  host port **8002**, container port **8000** — inter-service URL:
  `http://allis-chroma:8000`),
- a `msallisgis`-coupled GIS RAG path for West Virginia features built on GBIM-derived
  spatial entities from `msallis-db` (production, host 5433 / container 5432) and
  `gis_wv_benefits`,
- a **WV-biased multi-collection entangled retrieval path** (`allis-wv-entangled-gateway`,
  port **8010** — ✅ healthy) providing statically-injected WV context via `/chat_wv`,
- a web-research gateway, and
- a resolver path into the `allis-local-resources-db` registry (port 5435) for
  programmatic help,

all orchestrated by `allis-main-brain` (port **8050**) and the blood-brain-barrier
services.

At runtime, queries enter through `allis-unified-gateway` (host **18018** → container
**8001** — ✅ confirmed April 17, 2026) and are routed by the executive coordinator into
a RAG layer that spans ChromaDB collections, PostgreSQL GIS features, and verified
local-resource rows. In production as of April 17, 2026, the full pipeline:

```
allis-unified-gateway (host:18018 → container:8001)
→ allis-main-brain (8050)
→ BBB Input Filter — Phase 1.4 (allis-blood-brain-barrier:8016, 6 filters, barrier_active: true)
→ Phase 1.45 — Community Memory (autonomous_learner, top-5)
→ RAG (text + GIS + WV-entangled + registry, WV-first)
→ LLM Ensemble (allis-ollama:11434)
→ Judge Pipeline — judge_pipeline_v2.1-rag-grounded
→ BBB Output Filter (allis-bbb-output-filter — internal:8017)
→ UltimateResponse (architecture_layers=7, truthverdict.*)
```

is live and serving West Virginia benefits and geography questions.

> **⚠️ Embedding Model Lock — confirmed April 17, 2026**
> All ChromaDB collections use **384-dimensional vectors** produced by
> `all-minilm:latest`. The `nomic-embed-text` model produces 768-dimensional vectors
> and is **incompatible** with all existing collections. Any service, script, or
> migration that generates embeddings for ChromaDB must use `all-minilm:latest`.

> **⚠️ ChromaDB API — v2 ONLY — confirmed April 23, 2026**
> `allis-chroma` is running the **v2 multi-tenant API**. The `/api/v1/` endpoints
> return **410 Gone** on this stack — do not use `/api/v1/` paths in any code or
> tooling. All ChromaDB calls must use the full v2 path:
>
> ```
> /api/v2/tenants/default_tenant/databases/default_database/collections/{name}/...
> ```
>
> Host port: **8002** (`127.0.0.1:8002→8000/tcp`). Container-internal port: **8000**.
> Inter-service URL from other containers: `http://allis-chroma:8000`.
>
> **Count calls — UUID two-step pattern required:** The v2 `/count` endpoint requires
> the collection UUID, not the collection name. Retrieve the UUID first, then call
> `/collections/{uuid}/count`. The Python client `collection.count()` handles this
> transparently.

> **★★ ChromaDB inventory — April 23, 2026:**
> **48 collections** confirmed (historical note: prior drafts referenced 50 collections
> from the April 17, 2026 SQLite audit; two collections were removed during
> deduplication cleanup; 48 is the current confirmed count). Total vectors: **~6.74
> million**. Distance metrics: **37 L2 / 11 cosine**. All collections use
> `all-minilm:latest` 384-dim.

> **★★ Database architecture — two-container — confirmed April 23, 2026:**
> `msallisgis` is accessible via two containers:
> - **Production** — `msallis-db`, host port **5433** (container 5432), role
>   `postgres`, 16 GB / 294 tables / 11 schemas
> - **Forensic** — `postgis-forensic`, host port **5432**, role `allis`
>   (+ `-h 127.0.0.1`), 17 GB / 314 tables / 9 schemas
>
> `mvw_gbim_landowner_spatial` — **✅ 38,979 rows in msallis-db. Not present in
> postgis-forensic.** Port **5452** is invalid and has never existed in production.

> **★★ Security posture — confirmed April 23, 2026:** All services bound to
> `127.0.0.1` or internal Docker DNS. Zero `0.0.0.0` exposures. `_auth()` confirmed
> on all sensitive routes. `ALLIS_API_KEY` env var confirmed set in production.

> **★★ Port corrections applied April 17, 2026:**
>
> ```
> allis-rag-server         8003  → 8003   ✅  (container port was 8016 — corrected to 8003)
> allis-unified-gateway   18018  → 8001   ✅  (host port was assumed 9000 — corrected to 18018)
> allis-chroma             8002  → 8000   ✅  confirmed (inter-service: allis-chroma:8000)
> allis-blood-brain-barrier 8016 → 8016   ✅  confirmed
> allis-bbb-output-filter internal → 8017 ✅  confirmed {"status":"ok","service":"bbb-output-filter"}
> allis-qualia-engine    internal → 8017  ✅  DNS only — no host binding
> allis-main-brain         8050  → 8050   ✅  confirmed
> nbb_pituitary_gland        8108  → 80     ✅  mode=baseline
> ```

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
│    [6 filters operational — barrier_active: true]           │
│    BLOCKED → architecture_layers=1, truthverdict=null       │
│      ↓ (passes)                                              │
│  Phase 1.45 — Community Memory Retrieval                    │
│    all-minilm:latest (384-dim) → autonomous_learner (L2)    │
│    top-5 memories prepended to enhanced_message             │
│    [21,181 items — April 23, 2026]                          │
│      ↓                                                       │
│  Main Brain Orchestration                                   │
│      ├──→ Text RAG (allis-rag-server host:8003→ctr:8003)  │
│      ├──→ GIS RAG v0.4.0 (port 8004)                       │
│      │       204 WV GIS datasets / 7,357 WV bridges         │
│      │       Source: msallis-db (host 5433 / ctr 5432)     │
│      ├──→ GBIM Landowner Router (port 7205)                 │
│      │       allis-gbim-query-router                       │
│      │       PostgreSQL-native → mvw_gbim_landowner_spatial  │
│      │       msallis-db (host 5433 / ctr 5432)             │
│      │       ✅ 38,979 rows — NOT in postgis-forensic       │
│      ├──→ Spiritual / Psychological RAG (port 8006)         │
│      ├──→ WV-Entangled Gateway (port 8010) ✅ HEALTHY      │
│      │       Static WV context injection via /chat_wv       │
│      ├──→ Web Research (excluded for WV queries)            │
│      └──→ Registry (allis-local-resources-db port 5435)   │
│              101 embeddings; Fayette pipeline active        │
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
│    { response, services_used, consciousness_level,          │
│      processing_time, architecture_layers: 7,               │
│      truthverdict: { consensus_score: 0.95,                 │
│                      bbb_checked: true,                     │
│                      validated_by:                          │
│              "judge_pipeline_v2.1-rag-grounded" } }         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> Figure 7-1. RAG pipeline overview — April 23, 2026 production baseline.
> `allis-unified-gateway` (host:**18018** → container:**8001**) is the external entry
> point. `allis-main-brain` (port **8050**) is the primary orchestrator.
> `allis-wv-entangled-gateway` (port **8010**) injects static WV context upstream
> before the LLM ensemble via `/chat_wv` and is **not** the primary chat gateway.
> Blocked unsafe prompts return `architecture_layers = 1`, `truthverdict = null`.
> A healthy full-stack response carries `architecture_layers = 7`. Namespace:
> `msallis-rebuild`. Container prefix: `allis-`.

A typical benefits query:

```bash
curl -X POST http://127.0.0.1:8050/chat \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $ALLIS_API_KEY" \
  -d '{"message":"Mount Hope WV county benefits","county":"Fayette","role":"community","profile":"auto"}'
```

triggers Phase 1.45 community memory retrieval from `autonomous_learner` (L2),
retrieval from ChromaDB (including `governance_rag`, `commons_rag`, `gis_wv_benefits`,
and `local_resources`), optional GIS RAG over GBIM-derived spatial entities from
PostgreSQL `msallisgis` on `msallis-db` (host 5433 / container 5432), synthesis by
the LLM ensemble, validation by `judge_pipeline_v2.1-rag-grounded`, and post-filtering
by the blood-brain barrier output filter.

---

### 7.0.1 RAG Ingest Pipeline — Validated March 26, 2026

The entire RAG ingest pipeline is confirmed working. The `governance_rag` and
`commons_rag` collections are production-ready with verified semantic retrieval. The
US Constitution (Project Gutenberg `pg5.txt`, 97 chunks) is ingested into
`governance_rag` and confirmed as a constitutional grounding layer.

**Confirmed working ingest pattern:**

```python
import httpx
import chromadb

OLLAMA_HOST = "http://allis-ollama:11434"  # or http://127.0.0.1:11434 from host
CHROMA_HOST = "127.0.0.1"
CHROMA_PORT = 8002  # host-mapped port
# Inter-service URL: http://allis-chroma:8000

def chunk_text(text: str, max_words: int = 100, overlap: int = 20) -> list[str]:
    """
    Confirmed chunk size: 100 words max, 20-word overlap.
    all-minilm:latest has a 256-token context window (~0.75 tokens/word).
    Chunks exceeding ~100 words risk truncation. Hard architectural constraint.
    """
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = min(start + max_words, len(words))
        chunks.append(" ".join(words[start:end]))
        start += max_words - overlap
    return chunks

def embed_chunk(text: str) -> list[float]:
    """
    Confirmed: /api/embeddings with single-string "prompt".
    DO NOT use /api/embed (list input) — see §7.0.2.
    DO NOT use /api/v1/ paths — returns 410 Gone on this stack.
    """
    response = httpx.post(
        f"{OLLAMA_HOST}/api/embeddings",
        json={"model": "all-minilm:latest", "prompt": text}
    )
    embedding = response.json()["embedding"]
    assert len(embedding) == 384, f"Expected 384-dim, got {len(embedding)}"
    return embedding

def ingest_document(
    text: str,
    collection_name: str,
    doc_id_prefix: str,
    metadata_base: dict,
    distance_metric: str = "cosine"
) -> int:
    # Python client handles v2 UUID two-step count pattern transparently
    client = chromadb.HttpClient(host=CHROMA_HOST, port=CHROMA_PORT)
    collection = client.get_or_create_collection(
        name=collection_name,
        metadata={"hnsw:space": distance_metric}
    )
    chunks = chunk_text(text, max_words=100, overlap=20)
    for i, chunk in enumerate(chunks):
        embedding = embed_chunk(chunk)
        metadata = {**metadata_base, "chunk_index": i, "total_chunks": len(chunks)}
        collection.add(
            ids=[f"{doc_id_prefix}_chunk_{i}"],
            embeddings=[embedding],
            documents=[chunk],
            metadatas=[metadata]
        )
    return len(chunks)
```

**Confirmed production ingest results:**

| Document | Collection | Chunks | Status |
|:--|:--|:--|:--|
| MountainShares DAO Charter | `governance_rag` | included in 1,367 | ✅ Live |
| Terms of Use | `governance_rag` | included in 1,367 | ✅ Live |
| Program Rules | `governance_rag` | included in 1,367 | ✅ Live |
| Parameter Tables | `governance_rag` | included in 1,367 | ✅ Live |
| Phase 0–3 Specifications | `governance_rag` | included in 1,367 | ✅ Live |
| Safety Champion Protocol | `governance_rag` | included in 1,367 | ✅ Live |
| Funder Overview | `governance_rag` | included in 1,367 | ✅ Live |
| US Constitution (pg5.txt) | `governance_rag` | 97 chunks | ✅ Live — constitutional grounding layer |
| WV Constitution | `governance_rag` | included in 1,367 | ✅ Live |
| Commons governance + gamification corpus | `commons_rag` | 306 | ✅ Live |

The US Constitution (sourced from Project Gutenberg `pg5.txt`) was ingested into
`governance_rag` as 97 chunks using the confirmed 100-word/20-word-overlap ingest
pattern. Query "constitution" retrieves Amendment XIV at distance < 0.3. This provides
a constitutional grounding layer for governance queries alongside MountainShares DAO
governance documents in a single retrieval pass.

```python
# Confirmed smoke test — constitution retrieval
embedding = embed_chunk("What does the Constitution say about citizenship?")
results = collection.query(
    query_embeddings=[embedding],
    n_results=3,
    include=["documents", "metadatas", "distances"]
)
# Returns: Amendment XIV text chunks from pg5.txt
# Distance < 0.3 confirms semantic match
```

---

### 7.0.2 Bug Found and Fixed: `/api/embed` vs `/api/embeddings` — Ghost Record Problem

> **Critical architectural finding — confirmed and fixed March 26, 2026.**

**The bug:** Early ingest scripts used the `/api/embed` endpoint (list input) instead of
the confirmed-working `/api/embeddings` endpoint (single-string `"prompt"` field). In
combination with 800-word chunk sizes that exceeded `all-minilm:latest`'s 256-token
context window, this produced **ghost records**: ChromaDB entries that exist and are
countable but return near-zero cosine similarity on every semantic query.

**Root cause — two compounding errors:**

| Error | Symptom | Fix |
|:--|:--|:--|
| Wrong endpoint: `/api/embed` accepts a list | Embeddings generated from truncated or malformed input | Use `/api/embeddings` with single-string `"prompt"` field |
| 800-word chunks exceed 256-token window | Model truncates input silently; output vector is low-information | Enforce ≤100-word chunks |

```python
# BUG — do not use this pattern
response = httpx.post(
    f"{OLLAMA_HOST}/api/embed",
    json={"model": "all-minilm:latest", "input": [chunk_text]}  # list input — WRONG
)
# Result: ghost record — present and counted, but semantically inert

# CORRECT — confirmed working
response = httpx.post(
    f"{OLLAMA_HOST}/api/embeddings",
    json={"model": "all-minilm:latest", "prompt": chunk_text}  # single string — CORRECT
)
```

**Detection:** Ghost records are detectable by querying with a term that should appear
verbatim. If cosine distance for all results is > 0.7, suspect ghost records.

**Remediation:** Collections ingested with the buggy pattern must be dropped and
re-ingested using the confirmed working pattern (100-word chunks, 20-word overlap,
`/api/embeddings` single-string `"prompt"`). `governance_rag` and `commons_rag` were
ingested clean and are confirmed free of ghost records.

```python
def verify_no_ghost_records(
    collection_name: str,
    test_query: str,
    expected_max_distance: float = 0.5
):
    # Python client handles v2 UUID two-step count pattern transparently
    client = chromadb.HttpClient(host="127.0.0.1", port=8002)
    collection = client.get_collection(collection_name)
    embedding = embed_chunk(test_query)
    results = collection.query(
        query_embeddings=[embedding],
        n_results=1,
        include=["documents", "distances"]
    )
    distance = results["distances"]
    assert distance < expected_max_distance, (
        f"Ghost record suspected in {collection_name}: "
        f"top result distance {distance:.3f} > threshold {expected_max_distance}. "
        f"Re-ingest required."
    )
    print(f"✅ {collection_name}: top result distance {distance:.3f} — clean ingest confirmed")
```

---

## 7.1 Alignment with GBIM, Hilbert Space, Semantic Memory, and Registries

The GeoBelief Information Model (GBIM) defines how entities, places, and normative
claims are represented across documents and spatial features in the PostgreSQL databases.
The RAG layer is the mechanism that retrieves those GBIM-anchored fragments when a
question is asked.

**Database architecture — two-container — confirmed April 23, 2026:**

`msallisgis` is accessible via two containers:
- **Production** — `msallis-db`, host port **5433** (container 5432), role `postgres`,
  16 GB / 294 tables / 11 schemas — primary target for all GBIM, spatial, landowner,
  and decay operations
- **Forensic** — `postgis-forensic`, host port **5432**, role `allis`
  (+ `-h 127.0.0.1`), 17 GB / 314 tables / 9 schemas — forensic auditing and migration
  validation only

GBIM semantic entities (5,416,521 vectors) are also queryable through the ChromaDB
`gbim_worldview_entities` collection (L2 distance). The `gbim_beliefs_v2` collection
holds 5,000 embeddings with `wv_tag=true`, `source=gbim_postgresql`, county present,
and full WV address point record metadata — confirmed April 17, 2026 (OI-21 ✅ closed).
The bare `gbim_beliefs` collection is **retired** — use `gbim_worldview_entities` (L2)
or `gbim_beliefs_v2` (cosine).

The Hilbert-space state view treats the system's overall knowledge and constraints as a
very high-dimensional state vector. RAG interactions are projections into
lower-dimensional subspaces. For text, those projections are embedding-based
nearest-neighbor searches in `allis-chroma` using 384-dimensional vectors from
`all-minilm:latest`. For space, they are centroid-based spatial filters over
`msallisgis`-derived features on `msallis-db` (host 5433 / container 5432). For
concrete help-seeking, retrieved resource documents are further resolved into rows of
`allis-local-resources-db` (port 5435) keyed by ZIP, county, and program type.

**Database integration — confirmed April 23, 2026:**

```python
import psycopg2
import chromadb

# Production: msallis-db — host 5433 / container 5432 / database msallisgis
# Use for: GBIM belief graph, spatial queries, landowner routing, decay loop
# mvw_gbim_landowner_spatial is HERE — ✅ 38,979 rows
pg_conn_production = psycopg2.connect(
    host="localhost", port=5433,
    database="msallisgis", user="postgres", password="postgres"
)

# Forensic: postgis-forensic — host 5432 / role allis / database msallisgis
# Use for: forensic auditing and migration validation ONLY
# mvw_gbim_landowner_spatial NOT present in this container
pg_conn_forensic = psycopg2.connect(
    host="127.0.0.1", port=5432,
    database="msallisgis", user="allis", password="<allis_password>"
)

# allis-local-resources-db — port 5435
# database name is "postgres" (not the container name)
pg_conn_resources = psycopg2.connect(
    host="localhost", port=5435,
    database="postgres", user="postgres", password="postgres"
)

# allis-chroma: host 8002 / container 8000
# Inter-service URL: http://allis-chroma:8000
# v2 API ONLY — /api/v1/ returns 410 Gone
# Count calls use UUID two-step pattern (Python client handles transparently)
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

## 7.2 Core RAG and Search Components

### 7.2.0 Phase 1.45 — Semantic Community Memory Retrieval

Phase 1.45 fires after the BBB input filter (Phase 1.4) and before the main text and
GIS RAG services. It is the first retrieval step that enriches `enhanced_message`.

**How it works:**

1. The main brain calls `allis-ollama:11434/api/embeddings` with model
   `all-minilm:latest` and the user query as prompt, receiving a 384-dimensional
   embedding vector.
2. The embedding queries the `autonomous_learner` ChromaDB collection (L2 distance,
   **21,181 items** confirmed April 23, 2026).
3. The 5 most semantically similar community interaction records are retrieved.
4. The retrieved memories are prepended to `enhanced_message` before the LLM ensemble.

```python
import httpx
import chromadb

# Step 1: Generate 384-dim embedding — /api/embeddings, single-string "prompt"
# DO NOT use /api/embed or /api/v1/ paths
response = httpx.post(
    "http://allis-ollama:11434/api/embeddings",
    json={"model": "all-minilm:latest", "prompt": user_query}
)
embedding = response.json()["embedding"]  # must be 384-dim

# Step 2: Query autonomous_learner via Chroma Python client
# host 8002 = allis-chroma host-mapped port; inter-service: allis-chroma:8000
# Python client handles v2 UUID two-step count pattern transparently
client = chromadb.HttpClient(host="127.0.0.1", port=8002)
collection = client.get_collection("autonomous_learner")  # L2 distance
result = collection.query(
    query_embeddings=[embedding],
    n_results=5,
    include=["documents", "metadatas", "distances"]
)

# Step 3: Prepend to enhanced_message
community_memories = "\n".join([doc for docs in result["documents"] for doc in docs])
enhanced_message = community_memories + "\n\n" + original_message
```

> **Critical:** The embedding model must be `all-minilm:latest` (384-dim).
> `nomic-embed-text` (768-dim) will cause a dimension mismatch against all existing
> ChromaDB collections.

#### 7.2.0.1 Autonomous Learner and conversation_history — April 23, 2026

> **★★ Autonomous Learner: HEALTHY. OI-05 ✅ CLOSED.**

The autonomous learner was fully restored April 1, 2026 (LEARN-01, LEARN-02, LEARN-03
all resolved). As of April 23, 2026, the `autonomous_learner` collection contains
**21,181 items** (L2 distance).

The `conversation_history` collection is **formally wired to the production pipeline**
(OI-05 ✅ closed April 17, 2026). Evidence:

- **580 embeddings** confirmed in live ChromaDB (April 23, 2026 baseline)
- **Read path:** `msallisconsciousnessbridge.py` line 113; `retrieval_router.py` lines
  135–136 (intent-gated via `intent.get("use_conversation_history")`)
- **Write path:** `msallisconsciousnessbridge.py` line 304
- **Production gateway read:** `ms_allis_unified_gateway.py` line 477

| Metric | Value |
|:--|:--|
| `autonomous_learner` items (L2) | **21,181** (April 23, 2026) |
| `conversation_history` embeddings | **580** (April 23, 2026) |
| `autonomous_learning` items | 57 (April 1, 2026 post-fix baseline) |
| `allis-gbim-query-router` `/route` | ✅ HTTP 200 OK |
| LEARN-01 (numpy dtype fix) | ✅ Resolved April 1, 2026 |
| LEARN-02 (GBIM router schema fix) | ✅ Resolved April 1, 2026 |
| LEARN-03 (crash-loop recovery) | ✅ Resolved April 1, 2026 |

---

### 7.2.1 Text RAG Service (`allis-rag-server`)

**Port mapping: host:8003 → container:8003 — ✅ confirmed April 17, 2026**

> **⚠️ Embedding Model Note:** The RAG server uses `EMBED_MODEL=all-minilm:latest` and
> `OLLAMA_HOST=http://allis-ollama:11434` set via environment variables.

> **⚠️ ChromaDB Call — v2 API Required:** The RAG server uses the v2 collection-specific
> URL format. `/api/v1/` paths are deprecated (return 410 Gone) on this stack.
> Inter-service URL: `http://allis-chroma:8000`.
> Count calls use the UUID two-step pattern (Python client handles transparently).

**Endpoint:** `POST /query`

**RAGQuery schema (confirmed Pydantic schema):**

| Field | Type | Required | Default | Notes |
|:--|:--|:--|:--|:--|
| `collection` | string | ✅ Yes | — | ChromaDB collection name |
| `message` | string | ✅ Yes | — | Query text |
| `user_id` | string | No | `"defaultuser"` | Optional session identifier |
| `n_results` | int | No | `8` | Number of results to retrieve |

```bash
# From host — use port 8003
curl -X POST http://127.0.0.1:8003/query \
  -H "Content-Type: application/json" \
  -d '{
    "collection": "governance_rag",
    "message": "What does the DAO charter say about membership?",
    "user_id": "defaultuser",
    "n_results": 8
  }'
```

**Corrected ChromaDB v2 call signature (direct HTTP, for reference):**

```python
import httpx

# Inter-service: allis-chroma:8000 (container-internal)
# From host: 127.0.0.1:8002
CHROMA_HOST = "allis-chroma"   # container-internal DNS name
CHROMA_PORT = 8000               # container-internal port

url = (
    f"http://{CHROMA_HOST}:{CHROMA_PORT}"
    "/api/v2/tenants/default_tenant"
    "/databases/default_database"
    f"/collections/{collection_name}/query"
)
# NOTE: /api/v1/ returns 410 Gone — do not use

resp = httpx.post(url, json={
    "query_embeddings": [embedding_vector],
    "n_results": n_results,
    "include": ["documents", "metadatas", "distances"]
})
```

**UUID two-step count pattern (direct HTTP):**

```python
import httpx

CHROMA_BASE = "http://allis-chroma:8000"  # inter-service URL

# Step 1: Get collection UUID by name
col_resp = httpx.get(
    f"{CHROMA_BASE}/api/v2/tenants/default_tenant"
    f"/databases/default_database/collections/{collection_name}"
)
collection_uuid = col_resp.json()["id"]

# Step 2: Get count using UUID
count_resp = httpx.get(
    f"{CHROMA_BASE}/api/v2/tenants/default_tenant"
    f"/databases/default_database/collections/{collection_uuid}/count"
)
count = count_resp.json()
# Note: Python client collection.count() handles this two-step transparently
```

**Active collections — 48 confirmed (April 23, 2026):**

> **Historical note:** Prior drafts (April 17, 2026 SQLite audit) referenced 50
> collections / 6,740,616 rows. Two collections were removed during deduplication
> cleanup; **48 collections** and **~6.74 million vectors** is the current confirmed
> count. All collections use `all-minilm:latest` 384-dim. Distance metrics:
> **37 L2 / 11 cosine**.

| Collection | Items | Distance | Purpose |
|:--|:--|:--|:--|
| `local_resources` | 101 embeddings | cosine | **Default** — verified Fayette County community resources; Fayette pipeline active (OI-20 ✅ closed) |
| `autonomous_learner` | **21,181** | **L2** | Community interaction memories — Phase 1.45 |
| `conversation_history` | **580** | cosine | Conversation history — formally wired read+write (OI-05 ✅ closed) |
| `autonomous_learning` | 57 | cosine | Autonomous learning cycle records (April 1, 2026 post-fix baseline) |
| `gbim_worldview_entities` | 5,416,521 | **L2** | Complete WV GBIM spatial corpus — authoritative |
| `gbim_beliefs_v2` | **5,000** | **cosine** | GBIM beliefs v2 — `wv_tag=true`, `source=gbim_postgresql`, county present, WV address point records (OI-21 ✅ closed) |
| `governance_rag` | **1,367 chunks** | cosine | MountainShares DAO corpus + US Constitution (97 chunks) + WV Constitution — LIVE |
| `commons_rag` | **306 chunks** | cosine | Commons governance + gamification — LIVE |
| `gis_wv_benefits` | 4,668 | **L2** | WV benefits facilities |
| `psychological_rag` | **6,860** | cosine | Mental health corpus |
| `appalachian_cultural_intelligence` | **820** | cosine | Appalachian cultural context — LIVE |
| `aaacpe_corpus` | **65 docs** | cosine | AaaCPE live web scrape — 39 sources |
| `spiritual_rag` | 368,238 | cosine | Mother Carrie Protocol corpus — deduplicated |
| `spiritual_wisdom` | Active | cosine | Spiritual wisdom collection |
| `pia_records` | Active | cosine | PIA records |
| `geospatialfeatures` | **60,875** | **L2** | GIS feature embeddings — LIVE |
| `GBIM_Fayette_sample` | **1,535** | **L2** | Fayette County GBIM sample — LIVE |
| `ms_allis_memory` | Active | cosine | Conversation memory (HTTP 500 on count — OI-C4-500, monitoring only) |
| `mountainshares_knowledge` | Active | cosine | MountainShares governance |
| `episodic_index` | Active | cosine | Episodic memory index |
| `GBIM_sample_rows` | 5,000 | **L2** | GBIM test sample |
| `msallis_docs` | **28,327** | cosine | System docs + verified WV community resources |
| `operations_history` | Active | cosine | System operations log |
| `appalachian_english_corpus` | Active | cosine | Appalachian language and dialect corpus |
| `zcta_centroids` | Active | **L2** | ZIP code tabulation area centroids |
| `fifth_dgm_subconscious` | Active | **L2** | Fifth DGM subconscious queue — 384-dim HNSW |
| *(additional collections)* | — | — | See Chapter 41 for full 48-collection manifest |

> **`gbim_beliefs` (bare) is retired.** Use `gbim_worldview_entities` (L2) for the
> spatial corpus or `gbim_beliefs_v2` (cosine) for semantic belief embeddings.

---

### 7.2.2 GIS RAG Service v0.4.0 (port 8004)

The GIS RAG service is a dedicated geospatial retrieval path serving West Virginia
spatial questions. As of April 23, 2026, GIS-RAG v0.4.0 covers **204 WV GIS datasets**
and **7,357 WV bridges**. It queries:

- `gbim_worldview_entities` (L2) — 5,416,521 embeddings from `msallisgis` on
  `msallis-db` (host 5433 / container 5432)
- `gbim_beliefs_v2` (cosine) — 5,000 embeddings, `wv_tag=true`, full WV address point
  metadata (OI-21 ✅ closed)
- `gis_wv_benefits` (L2) — semantic descriptions and metadata for benefits-related
  facilities
- `geospatialfeatures` (L2) — 60,875 items, confirmed live
- `GBIM_Fayette_sample` (L2) — 1,535 items, confirmed live

Each indexed entity stores a short text description and metadata fields:
`worldview_id`, `dataset`, `county`, `gbim_entity`, `centroid_x`, `centroid_y`
(SRID 26917). All embeddings use `all-minilm:latest` (384-dim).

**Example spatial query flow:**

1. User: "hospitals near Mount Hope"
2. `allis-chroma` (host port 8002): Retrieve entities semantically similar to "hospital"
3. `msallisgis` on `msallis-db` (host 5433): Query `zcta_wv_centroids` for Mount Hope
   (ZIP 25880) centroid → `(37.8782, -81.2056)`
4. Filter: ChromaDB results within 10-mile radius
5. Response: Ranked hospitals with distances

```python
import httpx

resp = httpx.post(
    "http://127.0.0.1:8004/query",
    json={"query": "hospitals near Mount Hope", "n_results": 5}
)
```

**Production psql access for GIS RAG source data:**

```bash
# Always target msallis-db (production container)
docker exec msallis-db psql -U postgres -d msallisgis \
  -c "SELECT zip, lat, lon FROM zcta_wv_centroids WHERE zip = '25880';"
```

---

### 7.2.3 Spiritual / Psychological RAG Service (port 8006)

The Spiritual/Psychological RAG service retrieves from `spiritual_rag` (deduplicated —
19,338 duplicate vectors removed March 28, 2026), `psychological_rag` (6,860 items),
`governance_rag` (1,367 chunks), `commons_rag` (306 chunks), and
`appalachian_cultural_intelligence` (820 items). It serves:

1. **Mother Carrie Protocol queries** — normative and doctrinal questions grounded in
   the explicit values corpus.
2. **Community values alignment checks** — questions evaluated against Appalachian
   community values.
3. **Psychological safety queries** — trauma, wellbeing, counseling, mental health.

All embeddings use `all-minilm:latest` (384-dim). The service exposes `POST /query`
accepting `{"query": str, "n_results": int, "collection_filter": [str]}`.

This service is the primary RAG backend for the alignment judge in §7.8.

---

### 7.2.4 WV-Entangled Gateway (`allis-wv-entangled-gateway`, port 8010) — ✅ HEALTHY

The `allis-wv-entangled-gateway` service provides **WV-biased multi-collection
entangled retrieval** via static WV context injection — not post-hoc metadata filtering.

> **OI-19 ✅ CLOSED April 17, 2026 — working as designed:** The gateway does **not**
> filter on `wv_tag` or `state` metadata at query time. It builds WV entangled context
> **statically**, injecting it upstream before the LLM ensemble via `/chat_wv`. The
> `wv_tag` metadata mismatch on `gbim_beliefs_v2` / `gis_wv_benefits` is irrelevant —
> no post-hoc metadata filter is applied. **No code change needed.**

```python
# Static WV context injected by allis-wv-entangled-gateway on every /chat_wv request
wv_context = {
    "state": ["WV"],
    "counties": [
        {"type": "county", "id": "GBIM_WV_FAYETTE"},
        {"type": "county", "id": "GBIM_WV_MCDOWELL"}
    ],
    "watersheds": [
        {"type": "watershed", "id": "GBIM_WV_UPPER_KANAWHA"}
    ],
    "rulesets": ["WV_DHHR_BENEFITS", "WV_RURAL_TRANSPORT"]
}
# Every request through /chat_wv is already WV-entangled by construction.
```

> **Important:** `allis-wv-entangled-gateway` (port **8010**) is **not the primary
> chat gateway**. The primary orchestrator is `allis-main-brain` on port **8050**. The
> external entry point is `allis-unified-gateway` on host port **18018** → container
> **8001**. Port 8010 is a specialized WV-entangled path called internally by the main
> brain orchestration layer.

```bash
curl -X POST http://127.0.0.1:8010/chat_wv \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Fayette County land ownership and benefits facilities",
    "county": "Fayette",
    "n_results": 10
  }'
```

---

### 7.2.5 Web-Research Gateway

External web retrieval is handled by a dedicated gateway rather than allowing arbitrary
outbound calls. The gateway applies policy filters and rate limits, normalizes results,
and logs queries for audit. For WV-scoped queries (identified by county, role, or
profile), web context is excluded from the final context window so external search
results cannot override in-state RAG, GIS, and registry evidence.

---

### 7.2.6 Local Resource Registry Resolver (`allis-local-resources-db`, port 5435)

> **OI-20 ✅ CLOSED April 17, 2026.** The pipeline is confirmed active:
> `ingest_runner.py` Lane A → `allis-local-resources-db` TCP 5435. **101 embeddings
> are present** in the `local_resources` ChromaDB collection. Fayette-specific records
> enter the registry when the AAACPE pipeline processes Fayette county data — this is
> an ongoing ops ingest task, not a code gap. Containers confirmed: `allis-aaacpe-rag`,
> `allis-local-resources-db`, `allis-local-resources`.

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

---

### 7.2.7 Landowner / GBIM Router (`allis-gbim-query-router`, port 7205)

`allis-gbim-query-router` is on host port **7205**, healthy, and **RBAC-gated**.
`X-Allis-Role` header is required for `/query`. This is a **PostgreSQL-native routing
service** — it does not use ChromaDB or vector similarity search. It translates
natural-language landowner queries into SQL aggregations against
`mvw_gbim_landowner_spatial` in `msallisgis` on `msallis-db` (host 5433 / container
5432), returning ranked ownership records with acreage, parcel count, and county
breakdown.

> **`mvw_gbim_landowner_spatial` — ✅ 38,979 rows in msallis-db. Not present in
> postgis-forensic.** All landowner routing targets `msallis-db` (production container,
> host 5433 / container 5432).

> **★ LEARN-02 Resolved April 1, 2026:** Briefly returned HTTP 422 on `/route` POST
> calls from the autonomous learner due to a request schema mismatch. The main
> production landowner query path was **unaffected**. Schema fix applied; `/route`
> confirmed HTTP 200 OK.

```python
import httpx

# RBAC-gated — requires X-Allis-Role header
# Target: msallis-db (host 5433 / container 5432 / database msallisgis)
response = httpx.post(
    "http://127.0.0.1:7205/query",
    headers={"X-Allis-Role": "admin"},
    json={
        "question": "Who are the largest landowners in West Virginia?",
        "mode": "landowner_gbim",
        "route_type": "parcel_ownership",
        "scope": "statewide",
        "limit": 20
    }
)

response_county = httpx.post(
    "http://127.0.0.1:7205/query",
    headers={"X-Allis-Role": "admin"},
    json={
        "question": "Who owns the most land in Fayette County?",
        "mode": "landowner_gbim",
        "route_type": "parcel_ownership",
        "county": "Fayette",
        "limit": 20
    }
)
```

```bash
# Verify mvw_gbim_landowner_spatial row count
docker exec msallis-db psql -U postgres -d msallisgis \
  -c "SELECT COUNT(*) FROM mvw_gbim_landowner_spatial;"
# Returns: 38979
```

---

### 7.2.8 Unified Gateway Dependency Map — confirmed April 17, 2026

**84 total queries processed** as of April 17, 2026 confirmation run.

`allis-unified-gateway` (host:**18018** → container:**8001**) depends on the following
internal services, all confirmed healthy April 17, 2026:

| Service | Internal URL | Status |
|:--|:--|:--|
| allis-consciousness-bridge | `http://allis-consciousness-bridge:8020` | ✅ healthy |
| allis-neurobiological-master | `http://allis-neurobiological-master:8018` | ✅ healthy |
| allis-i-containers | `http://allis-i-containers:8015` | ✅ healthy |
| allis-blood-brain-barrier | `http://allis-blood-brain-barrier:8016` | ✅ healthy |
| allis-qualia-engine | `http://allis-qualia-engine:8017` | ✅ healthy — internal DNS only, no host binding |

```bash
docker inspect allis-unified-gateway --format '{{.NetworkSettings.Ports}}'
# Expected: map[8001/tcp:[{0.0.0.0 18018}]]
```

---

## 7.3 Retrieval Flows

### 7.3.1 Non-Spatial RAG Flow

1. **Query intake.** User request enters `allis-unified-gateway` (host:**18018** →
   container:**8001**) and is forwarded to `allis-main-brain` (port **8050**).
2. **BBB input filter — Phase 1.4.** `allis-blood-brain-barrier` (port **8016**)
   applies **6 operational filters** (`barrier_active: true`). Blocked unsafe prompts
   short-circuit the full stack and return `architecture_layers = 1`,
   `truthverdict = null`.
3. **Phase 1.45 — Community memory retrieval.** Main brain embeds query via
   `all-minilm:latest` (384-dim) using `/api/embeddings` with single-string `"prompt"`.
   Retrieves top-5 from `autonomous_learner` (L2, 21,181 items). Prepends to
   `enhanced_message`.
4. **Routing to text RAG.** Orchestration calls `allis-rag-server`
   (host:**8003** → container:**8003**) via `POST /query` with `collection` and
   `message` fields.
5. **Retrieval from ChromaDB.** Text RAG service embeds query, runs similarity search
   via v2 API (`allis-chroma:8000`), returns scored documents with metadata.
6. **Context assembly.** Phase 1.45 memories + RAG results + `conversation_history`
   (intent-gated via `intent.get("use_conversation_history")`) merged into context
   window; source separation preserved.
7. **Generation.** LM Synthesizer applies Ms. Egeria Allis persona via
   `allis-ollama:11434/api/generate`.
8. **BBB output filter.** Output forwarded to `allis-bbb-output-filter`
   (internal port **8017**). Confirmed returning
   `{"status":"ok","service":"bbb-output-filter"}`. Fail-open on HTTP 500.
9. **UltimateResponse assembly.** `architecture_layers = 7` for a healthy full-stack
   response. `truthverdict.validated_by = "judge_pipeline_v2.1-rag-grounded"`.
   See §7.8.4.

---

### 7.3.2 Spatial RAG Flow

```
┌─────────────────────────────────────────────────────────────┐
│   Spatial RAG: Semantic + Geographic Retrieval               │
│   ★★ April 23, 2026 — two-container DB architecture         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Semantic Retrieval (allis-chroma host 8002)               │
│  Inter-service: http://allis-chroma:8000                   │
│  API: v2 ONLY — /api/v1/ returns 410 Gone                   │
│  Count calls: UUID two-step pattern                         │
│  ┌────────────────────────────────────────────────┐         │
│  │  Query: "hospitals near Mount Hope"            │         │
│  │  Embed (all-minilm:latest 384-dim,             │         │
│  │    /api/embeddings single-string prompt)       │         │
│  │  → Search gis_wv_benefits (L2) +              │         │
│  │    gbim_worldview_entities (L2, 5,416,521) +  │         │
│  │    gbim_beliefs_v2 (cosine, 5,000 wv_tag) +  │         │
│  │    geospatialfeatures (L2, 60,875) +           │         │
│  │    GBIM_Fayette_sample (L2, 1,535) +           │         │
│  │    zcta_centroids (L2, confirmed)              │         │
│  │  Returns: Embeddings + metadata                │         │
│  └────────────────────────────────────────────────┘         │
│              ↓                                               │
│  Geographic Filtering (msallis-db, production)             │
│  host 5433 / container 5432 / database msallisgis          │
│  ┌────────────────────────────────────────────────┐         │
│  │  docker exec msallis-db psql -U postgres      │         │
│  │    -d msallisgis                              │         │
│  │  SELECT zip, lat, lon                          │         │
│  │    FROM zcta_wv_centroids                      │         │
│  │    WHERE zip = '25880'  -- Mount Hope          │         │
│  │  Then: spatial filter within 10-mile radius    │         │
│  └────────────────────────────────────────────────┘         │
│              ↓                                               │
│  GBIM Belief Provenance (msallis-db, production)           │
│  host 5433 / container 5432 / database msallisgis          │
│  ┌────────────────────────────────────────────────┐         │
│  │  Query: gbim_beliefs WHERE entity_id = ?       │         │
│  │  Returns: confidence_decay, needs_verification │         │
│  └────────────────────────────────────────────────┘         │
│              ↓                                               │
│  LANDOWNER PATH (PostgreSQL-native, bypasses ChromaDB)      │
│  allis-gbim-query-router (port 7205)                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  mvw_gbim_landowner_spatial                    │         │
│  │  ✅ 38,979 rows — msallis-db ONLY             │         │
│  │  NOT present in postgis-forensic               │         │
│  └────────────────────────────────────────────────┘         │
│              ↓                                               │
│  Combined Results → LLM Context                             │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> Figure 7-3. Spatial RAG flow. All production PostgreSQL access targets `msallis-db`
> (host 5433 / container 5432, database `msallisgis`). `postgis-forensic` is
> forensic-only. `allis-chroma` inter-service URL: `http://allis-chroma:8000`.
> ChromaDB API: v2 only — `/api/v1/` returns 410 Gone. Count calls use UUID two-step
> pattern. `gbim_beliefs_v2` (5,000 embeddings, cosine, `wv_tag=true`) confirmed
> April 17, 2026 (OI-21 ✅ closed).

---

### 7.3.3 Resource-Oriented RAG Flow

1. **Resource query intake.** `allis-main-brain` (port **8050**) identifies
   resource-oriented request, extracts location hints (ZIP, county, town) and population
   signals.
2. **Phase 1.45 — Community memory.** Top-5 `autonomous_learner` (L2) memories
   prepended.
3. **Text RAG via allis-rag-server** (`POST /query`, collection: `local_resources`,
   host:**8003** → container:**8003**).
4. **Resolution via local resource resolver.** Queries `allis-local-resources-db`
   (port 5435, database: `postgres`). 101 embeddings present; Fayette-specific records
   enter when AAACPE pipeline processes Fayette county data (OI-20 ✅ closed).
5. **Context assembly and generation.** LM Synthesizer applies Ms. Egeria Allis persona
   via `allis-ollama:11434`.
6. **BBB output filter.** Output forwarded to `allis-bbb-output-filter`
   (internal:**8017**).

---

## 7.4 Routing, Roles, Geography, and WV-First Policy

### 7.4.1 Design Intent

**Topic and intent routing.** Governance queries favor `governance_rag` (1,367 chunks
including US and WV Constitutions) and `commons_rag` (306 chunks); spatial-justice
queries favor `msallisgis`-derived collections on `msallis-db` (host 5433); resource
questions favor `allis-local-resources-db` plus WV-resource collections;
WV-entangled queries route to `allis-wv-entangled-gateway` (port **8010** — ✅
healthy) via `/chat_wv` for static WV context injection. Landowner/GBIM answers are
served through `allis-gbim-query-router` (port **7205**, RBAC-gated — SQL path, not
semantic RAG; `mvw_gbim_landowner_spatial` ✅ 38,979 rows in `msallis-db` only).
`conversation_history` is queried conditionally via
`intent.get("use_conversation_history")` in `retrieval_router.py` lines 135–136
(OI-05 ✅ closed).

**Role-aware routing.** Active role determines eligible collections and registries.
Community-facing roles are restricted to public documentation, approved spatial layers,
and public-facing slices of `allis-local-resources-db`.

**Geography-aware routing and WV-first behavior.** For West Virginia-scoped queries,
the system:

- Treats WV RAG, `msallis-db` GIS (`msallisgis`, host 5433), and registry context
  as authoritative.
- Excludes web context from the final context window.
- Requires models to ignore conflicting out-of-state content unless user explicitly
  requests another state.

---

### 7.4.2 Port and Service Reference Table — April 23, 2026

| Service | Host Port | Container Port | Status / Notes |
|:--|:--|:--|:--|
| `allis-unified-gateway` | **18018** | **8001** | ✅ External entry point |
| `allis-main-brain` | **8050** | 8050 | ✅ Primary orchestrator |
| `allis-rag-server` | **8003** | **8003** | ✅ Text RAG — `POST /query` — both ports confirmed 8003 |
| `allis-gis-rag` v0.4.0 | 8004 | 8004 | ✅ GIS / spatial RAG — 204 WV GIS datasets / 7,357 WV bridges |
| `allis-psychological-rag` | 8006 | 8006 | ✅ Spiritual + psychological RAG — 6,860 items |
| `allis-wv-entangled-gateway` | **8010** | **8010** | ✅ Healthy — static WV context via `/chat_wv` |
| `allis-blood-brain-barrier` | **8016** | **8016** | ✅ 6 filters operational, `barrier_active: true` |
| `allis-bbb-output-filter` | internal | **8017** | ✅ `{"status":"ok","service":"bbb-output-filter"}` — no host binding |
| `allis-qualia-engine` | internal (DNS only) | **8017** | ✅ `allis-qualia-engine:8017` DNS only |
| `allis-consciousness-bridge` | internal | 8020 | ✅ `http://allis-consciousness-bridge:8020` |
| `allis-neurobiological-master` | internal | 8018 | ✅ `http://allis-neurobiological-master:8018` |
| `allis-i-containers` | internal | 8015 | ✅ `http://allis-i-containers:8015` |
| `allis-aaacpe-rag` | 8032 | — | ✅ Live — `aaacpe_corpus` (65 docs, 39 sources) |
| `allis-aaacpe-scraper` | 8033 | — | ✅ Live |
| `allis-chroma` | **8002** (host) | **8000** (container) | ✅ v2 API only — `/api/v1/` returns 410 Gone. Inter-service: `http://allis-chroma:8000`. **48 collections, ~6.74M vectors** |
| `allis-ollama` | 11434 | 11434 | ✅ `all-minilm:latest` + LLM loaded |
| `allis-gbim-query-router` | **7205** | 7205 | ✅ Healthy — **RBAC-gated** — `X-Allis-Role` required. SQL/landowner path. `mvw_gbim_landowner_spatial` ✅ 38,979 rows (msallis-db only) |
| `allis-local-resources-db` | 5435 | 5435 | ✅ Active (`database: postgres`) — 101 embeddings; Fayette pipeline active |
| `msallis-db` (production) | **5433** | **5432** | ✅ `msallisgis` — 16 GB / 294 tables / 11 schemas — role `postgres` |
| `postgis-forensic` (forensic) | **5432** | **5432** | ✅ `msallisgis` — 17 GB / 314 tables / 9 schemas — role `allis` |
| `nbb_pituitary_gland` | **8108** | **80** | ✅ mode=baseline |
| `allis-web-research` | 8008 (internal) | — | ✅ Restored March 25, 2026 |
| `allis-ingest-api` | 8009 | — | ✅ Restored March 25, 2026 |

---

## 7.5 Smoke Tests — Confirmed Semantic Retrieval

The following smoke tests were run against `governance_rag` and `commons_rag` and
confirm production-ready semantic retrieval with no ghost records.

**`governance_rag` smoke tests:**

| Query | Expected result | Confirmed |
|:--|:--|:--|
| "BSA" / "Boy Scouts" | Retrieves SNAP/Medicaid context | ✅ Distance < 0.4 |
| "governance" | Retrieves DAO charter text | ✅ Distance < 0.3 |
| "constitution" | Retrieves Amendment XIV (pg5.txt) | ✅ Distance < 0.3 |
| "membership requirements" | Retrieves Phase 0 invite-only beta spec | ✅ Distance < 0.35 |

**`commons_rag` smoke tests:**

| Query | Expected result | Confirmed |
|:--|:--|:--|
| "commons gamification" | Retrieves gamification rules | ✅ Distance < 0.4 |
| "community participation" | Retrieves commons governance text | ✅ Distance < 0.35 |

**Smoke test runner:**

```python
def run_governance_smoke_tests():
    # Python client handles v2 UUID two-step count pattern transparently
    client = chromadb.HttpClient(host="127.0.0.1", port=8002)
    collection = client.get_collection("governance_rag")
    print(f"governance_rag item count: {collection.count()}")  # expect 1367

    test_cases = [
        ("BSA SNAP Medicaid benefits", 0.5, "BSA → SNAP/Medicaid retrieval"),
        ("governance DAO charter", 0.4, "governance → DAO charter"),
        ("constitution Amendment XIV", 0.4, "constitution → Amendment XIV (pg5.txt)"),
    ]

    for query_text, max_dist, label in test_cases:
        embedding = embed_chunk(query_text)
        results = collection.query(
            query_embeddings=[embedding],
            n_results=1,
            include=["documents", "distances"]
        )
        dist = results["distances"]
        status = "✅" if dist < max_dist else "❌ GHOST RECORD SUSPECTED"
        print(f"{status} {label}: distance={dist:.3f} (threshold={max_dist})")
        print(f"   Top result: {results['documents'][:120]}...")
```

---

## 7.6 BBB Safety and RAG Interaction

The Blood-Brain Barrier (`allis-blood-brain-barrier`, host port **8016**) is
empirically active with **6 operational filters** and `barrier_active: true`. A separate
BBB output filter service (`allis-bbb-output-filter`, internal port **8017**) handles
post-generation output filtering and is confirmed returning
`{"status":"ok","service":"bbb-output-filter"}`.

The six confirmed input filters are:

1. **Ethical Filter** — Biblical principles
2. **Spiritual Filter** — Wisdom alignment
3. **Safety Monitor** — Technical security
4. **Threat Detection** — Community protection
5. **Steganography / Prompt-Injection Detection** — flags
   `{'type': 'prompt_injection_keywords', 'detail': ['system prompt', 'jailbreak'], 'severity': 'critical'}`
6. **Truth/Content Filter** — via `POST /truth`; aggregates all filter results; returns
   `valid`, `confidence`, `principal_reasons`

**BBB output blocking** is proven behaviorally. Blocked unsafe prompts short-circuit
the full RAG/LLM stack and return:

```json
{
  "architecture_layers": 1,
  "truthverdict": null,
  "response": "[FILTERED]"
}
```

**Confirmed BBB routes:**

- `GET /` — root description
- `GET /health` — `filters_operational: 6`, `barrier_active: true`, `total_filtered`,
  `total_blocked`
- `POST /filter` — main filtering endpoint
- `POST /truth` — truth/content evaluation; expects `content` field (not `claim`);
  returns `valid`, `confidence`, `principal_reasons`

The `allis-qualia-engine` (internal:**8017**, DNS-only — no host binding) is reachable
within the Docker network as `http://allis-qualia-engine:8017` and participates in the
judge pipeline alongside the BBB output filter.

---

## 7.7 Constraints, Provenance, and Logging

**Pre-retrieval constraints.** Collection selection and filter mechanisms support
limiting by `collection`, `source`, `county`, `dataset`, `worldview`, `state`. The
`RAGQuery` schema (§7.2.1) supports `user_id` for session-level access control.

**Decoding-time guards.** After retrieval and generation, the main brain routes candidate
responses through `allis-bbb-output-filter` (internal:**8017**). Fail-open on HTTP 500
(content passes through unchanged, failure logged).

**Post-hoc review and logging.** Background storage of queries and responses into
`conversation_history` (580 embeddings, cosine, formally wired — OI-05 ✅ closed),
`episodic_index`, and `operations_history` ChromaDB collections (all confirmed in
48-collection manifest). Logs capture: services called, collections queried (with
distance metric), PostgreSQL container and host port used, Phase 1.45 memories
returned, filters/scores applied, and documents/features returned.

---

## 7.8 RAG-Grounded Judge Verification — `judge_pipeline_v2.1-rag-grounded`

> **★★ April 17, 2026.** The live judge pipeline is
> `judge_pipeline_v2.1-rag-grounded`. The older `heuristic_contradiction_v1` validator
> is **superseded and no longer active**.

### 7.8.1 The Problem This Solved

The old truth and alignment judges used `heuristic_contradiction_v1` — keyword and
pattern-matching rules with no queries to the GBIM corpus, ChromaDB collections, or any
RAG service. They reported `truth_score: 1.0` and `alignment_verdict: pass` without
consulting the 5.4 million GBIM entities, the `spiritual_rag` corpus, or the `gis_wv_benefits`
collection. This has been replaced by `judge_pipeline_v2.1-rag-grounded`, which
performs actual RAG-grounded claim verification.

**Capability comparison:**

| Behavior | `heuristic_contradiction_v1` | `judge_pipeline_v2.1-rag-grounded` |
|:--|:--|:--|
| Consults GBIM corpus | ❌ Never | ✅ Every call |
| Checks claims against documents | ❌ Pattern match only | ✅ GIS RAG retrieval + lexical overlap |
| Detects county/facility factual errors | ❌ No | ✅ If `gis_wv_benefits` has the record |
| Reports `gbim_docs_consulted` | ❌ Always 0 | ✅ Actual count |
| Fails open on RAG unavailability | N/A | ✅ Falls back to `not_found` |
| Provenance in output | ❌ None | ✅ `supporting_sources` list |

---

### 7.8.2 Truth Judge — `rag_grounded_gis_v1`

```python
import httpx
import re
from typing import List, Dict, Any

TRUTH_RAG_ENDPOINT = "http://allis-gis-rag:8004/query"

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

def score_claim_support(claim: str, rag_result: Dict[str, Any]) -> str:
    if rag_result["status"] == "rag_unavailable":
        return "not_found"
    docs = rag_result.get("documents", [])
    distances = rag_result.get("distances", [])
    if not docs or not distances:
        return "not_found"
    top_distance = distances if isinstance(distances, list) else distances
    if top_distance > 0.7:
        return "not_found"
    top_doc = docs if isinstance(docs, list) else docs
    claim_words = set(claim.lower().split())
    doc_words = set(top_doc.lower().split())
    overlap = len(claim_words & doc_words) / max(len(claim_words), 1)
    if overlap > 0.3 and top_distance < 0.4:
        return "supported"
    elif top_distance < 0.5:
        return "not_found"
    else:
        return "contradicted"

async def compute_truth_score_rag_grounded(
    consensus_answer: str,
    original_question: str
) -> Dict[str, Any]:
    claims = extract_factual_claims(consensus_answer)
    results = {
        "supported": 0, "contradicted": 0, "not_found": 0,
        "gbim_docs_consulted": 0, "sources": []
    }

    for claim in claims:
        rag_result = await check_claim_against_gis_rag(claim)
        verdict = score_claim_support(claim, rag_result)
        results[verdict] += 1
        results["gbim_docs_consulted"] += len(rag_result.get("documents", []))
        for meta in rag_result.get("metadatas", []):
            if isinstance(meta, dict) and meta.get("gbim_entity"):
                results["sources"].append(meta["gbim_entity"])
            elif isinstance(meta, list):
                for m in meta:
                    if isinstance(m, dict) and m.get("gbim_entity"):
                        results["sources"].append(m["gbim_entity"])

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

---

### 7.8.3 Alignment Judge — `rag_grounded_spiritual_v1`

```python
ALIGNMENT_RAG_ENDPOINT = "http://allis-psychological-rag:8006/query"

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

def score_alignment(claim: str, rag_result: Dict[str, Any]) -> str:
    if not rag_result or not rag_result.get("documents"):
        return "neutral"
    docs = rag_result.get("documents", [])
    distances = rag_result.get("distances", [])
    if not docs or not distances:
        return "neutral"
    top_distance = distances if isinstance(distances, list) else distances
    if top_distance < 0.35:
        return "aligned"
    elif top_distance < 0.6:
        return "neutral"
    else:
        return "misaligned"

async def compute_alignment_score_rag_grounded(
    consensus_answer: str
) -> Dict[str, Any]:
    normative_claims = extract_normative_claims(consensus_answer)
    results = {
        "aligned": 0, "misaligned": 0, "neutral": 0,
        "docs_consulted": 0, "normative_sources": []
    }

    for claim in normative_claims:
        async with httpx.AsyncClient(timeout=8.0) as client:
            try:
                resp = await client.post(
                    ALIGNMENT_RAG_ENDPOINT,
                    json={
                        "query": claim,
                        "n_results": 3,
                        "collection_filter": [
                            "spiritual_rag",
                            "appalachian_cultural_intelligence",
                            "governance_rag"
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
            if isinstance(meta, dict) and meta.get("source"):
                results["normative_sources"].append(meta["source"])
            elif isinstance(meta, list):
                for m in meta:
                    if isinstance(m, dict) and m.get("source"):
                        results["normative_sources"].append(m["source"])

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

---

### 7.8.4 UltimateResponse Schema — April 23, 2026

```python
from pydantic import BaseModel
from typing import List, Optional

class TruthVerdict(BaseModel):
    truth_score: float
    alignment_score: float
    consistency_score: float
    ethics_score: float
    consensus_score: float
    bbb_checked: bool = True
    validated_by: str = "judge_pipeline_v2.1-rag-grounded"
    # RAG-grounded fields — live as of April 17, 2026
    gbim_docs_consulted: int = 0
    gbim_contradictions_detected: int = 0
    normative_docs_consulted: int = 0
    misalignments_detected: int = 0
    supporting_sources: List[str] = []
    normative_sources: List[str] = []
    truth_method: str = "rag_grounded_gis_v1"
    alignment_method: str = "rag_grounded_spiritual_v1"

class UltimateResponse(BaseModel):
    response: str
    services_used: List[str]
    consciousness_level: str
    processing_time: float
    architecture_layers: int          # 7 = healthy full-stack; 1 = BBB-blocked
    truthverdict: Optional[TruthVerdict]  # null when BBB blocks at Phase 1.4
```

A healthy full-stack response carries `architecture_layers = 7`. A BBB-blocked unsafe
prompt returns `architecture_layers = 1` and `truthverdict = null`. The `consensus_score`
field has been observed at **0.95** in live production as of April 17, 2026.

---

## 7.9 Production Deployment State — April 23, 2026

**Hardware:** Lenovo Legion 5 — Mount Hope, West Virginia (ZIP 25880)

**Container stack:** Confirmed healthy as of April 23, 2026.

**Resource status (April 23, 2026):**

| Resource | Value | Status |
|:--|:--|:--|
| Disk | ~80% used | ✅ OI-22 closed — `docker system prune --filter until=24h` prevention in place |
| RAM | 8.8G used / 29G total | ✅ Healthy |
| Swap | 11G used / 23G | ✅ Elevated but stable — GPU model offloading |
| `msallis-db` tables | 294 / 11 schemas | ✅ Production |
| `postgis-forensic` tables | 314 / 9 schemas | ✅ Forensic only |
| `allis-chroma` collections | **48** | ✅ (historical note: was 50 on April 17, 2026 before cleanup) |
| ChromaDB total vectors | ~6.74M | ✅ |
| main-brain | healthy | ✅ |

**Open Issues — ALL CLOSED as of April 17, 2026:**

| ID | Issue | Status |
|:--|:--|:--|
| **OI-05** | `conversation_history` not wired to production pipeline | ✅ **CLOSED** — 580 embeddings; read: `msallisconsciousnessbridge.py:113`, `retrieval_router.py:135-136`; write: `msallisconsciousnessbridge.py:304`; production gateway: `ms_allis_unified_gateway.py:477` |
| **OI-19** | WV-entangled-gateway WV-tag boosting not firing | ✅ **CLOSED** — working as designed; static WV context injection via `/chat_wv`; no post-hoc metadata filter needed |
| **OI-20** | `local_resources` empty for Fayette County | ✅ **CLOSED** — 101 embeddings present; pipeline: `ingest_runner.py` Lane A → TCP 5435; Fayette coverage is ongoing ops ingest |
| **OI-21** | `gbim_beliefs_v2` count unverified | ✅ **CLOSED** — 5,000 embeddings; `wv_tag=true`, `source=gbim_postgresql`, county present, WV address point records with full coordinates and ESN numbers |
| **OI-22** | Disk at 96% | ✅ **CLOSED** — ~80% used, 181G free; `docker system prune` freed ~16% |
| LEARN-01 | `cosine_similarity()` numpy dtype bug | ✅ Resolved April 1, 2026 |
| LEARN-02 | GBIM router HTTP 422 on learner `/route` calls | ✅ Resolved April 1, 2026 |
| LEARN-03 | Autonomous learner crash-loop after empty file patch | ✅ Resolved April 1, 2026 |
| OI-23 | Judge pipeline using `heuristic_contradiction_v1` | ✅ **Superseded** — `judge_pipeline_v2.1-rag-grounded` is live |

**No open issues remain as of April 23, 2026.**

**RAG Service Stack — April 23, 2026:**

| Service | Host Port | Container Port | Status |
|:--|:--|:--|:--|
| `allis-unified-gateway` | **18018** | **8001** | ✅ External entry — `docker inspect allis-unified-gateway --format '{{.NetworkSettings.Ports}}'` |
| `allis-main-brain` | 8050 | 8050 | ✅ Primary orchestrator |
| `allis-rag-server` | **8003** | **8003** | ✅ Both ports confirmed 8003 |
| `allis-gis-rag` v0.4.0 | 8004 | 8004 | ✅ 204 WV GIS datasets / 7,357 WV bridges |
| `allis-psychological-rag` | 8006 | 8006 | ✅ `spiritual_rag` (deduplicated) + `psychological_rag` (6,860 items) |
| `allis-wv-entangled-gateway` | 8010 | 8010 | ✅ Healthy — static WV injection via `/chat_wv` |
| `allis-blood-brain-barrier` | 8016 | 8016 | ✅ 6 filters operational, `barrier_active: true` |
| `allis-bbb-output-filter` | internal | 8017 | ✅ `{"status":"ok","service":"bbb-output-filter"}` |
| `allis-qualia-engine` | internal (DNS only) | 8017 | ✅ `allis-qualia-engine:8017` |
| `allis-consciousness-bridge` | internal | 8020 | ✅ `http://allis-consciousness-bridge:8020` |
| `allis-neurobiological-master` | internal | 8018 | ✅ `http://allis-neurobiological-master:8018` |
| `allis-i-containers` | internal | 8015 | ✅ `http://allis-i-containers:8015` |
| `allis-aaacpe-rag` | 8032 | — | ✅ `aaacpe_corpus` (65 docs, 39 sources) |
| `allis-aaacpe-scraper` | 8033 | — | ✅ Live |
| `allis-chroma` | 8002 (host) | 8000 (container) | ✅ v2 API only. Inter-service: `http://allis-chroma:8000`. **48 collections, ~6.74M vectors** |
| `allis-ollama` | 11434 | 11434 | ✅ `all-minilm:latest` + LLM loaded |
| `allis-gbim-query-router` | 7205 | 7205 | ✅ RBAC-gated — `X-Allis-Role` required. `mvw_gbim_landowner_spatial` ✅ 38,979 rows (msallis-db only) |
| `nbb_pituitary_gland` | 8108 | 80 | ✅ mode=baseline |
| `msallis-db` (production) | **5433** | **5432** | ✅ `msallisgis` — 16 GB / 294 tables / 11 schemas — role `postgres` |
| `postgis-forensic` (forensic) | **5432** | **5432** | ✅ `msallisgis` — 17 GB / 314 tables / 9 schemas — role `allis` — forensic only |
| `allis-local-resources-db` | 5435 | 5435 | ✅ 101 embeddings; Fayette pipeline active |
| `allis-web-research` | 8008 (internal) | — | ✅ Restored March 25, 2026 |
| `allis-ingest-api` | 8009 | — | ✅ Restored March 25, 2026 |

---

*Chapter 7 — FINAL. Last updated: April 23, 2026, Mount Hope WV — Carrie Kidd (Mamma Kidd)*

*Applied April 23, 2026: `jarvis-chroma` inter-service URL corrected to
`http://jarvis-chroma:8000`; ChromaDB API confirmed v2 only (`/api/v1/` returns
410 Gone); count calls documented as UUID two-step pattern; `jarvis-gbim-query-router`
confirmed port 7205; collection names confirmed (`msjarvis_docs`, `ms_jarvis_memory`,
`gbim_worldview_entities`); collection count updated to 48 with historical note (was 50
on April 17, 2026 pre-cleanup); `

*Prior update history: April 17, 2026 — all five open issues (OI-05, OI-19, OI-20,
OI-21, OI-22) closed; port corrections applied; `judge_pipeline_v2.1-rag-grounded`
confirmed live; `heuristic_contradiction_v1` superseded; 99 containers Up; 50
ChromaDB collections (pre-cleanup). April 1, 2026 — LEARN-01, LEARN-02, LEARN-03
resolved; autonomous learner restored. March 28, 2026 — security remediation complete;
`msjarvisgis` port corrected from 5452 to 5432; `spiritual_rag` deduplicated;
`psychological_rag` restored. March 27, 2026 — all `gisdb` references corrected to
`majarvisgis`. March 26, 2026 — RAG ingest validated, ghost record bug fixed,
`governance_rag` and `commons_rag` confirmed live.*
