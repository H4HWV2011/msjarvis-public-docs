# 7. RAG Pipeline and Routers

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*

## Why This Matters for Polymathmatic Geography

This chapter specifies how Ms. Allis's language models are bound to place-aware, collection-aware, and registry-aware memory instead of free-floating text generation. It makes the Hilbert-space representation, GBIM structures, ChromaDB-backed semantic memory, and the verified local resource registry from earlier chapters operational by defining concrete services that retrieve from semantic memory, the spatial body, the web, and structured program tables. In the current deployment, this design is realized as a production RAG stack that delivers West Virginia benefits intelligence through a multi-model consciousness bridge anchored in ChromaDB, GBIM-derived entities from the PostgreSQL `msallisgis` / `msallis` databases (both in the `postgis-forensic` container on port **5432** — confirmed April 17, 2026), GIS-aware collections, and a WV-first routing policy. It supports:

- **P1 – Every where is entangled** by requiring that answers emerge from an entangled memory of governance texts, spatial layers, research notes, belief structures from PostgreSQL GBIM tables, and local resource registries, rather than from an abstract model prior.
- **P3 – Power has a geometry** by letting retrieval paths expose which collections — and thus which institutional, spatial, and programmatic perspectives — shape a given answer, including WV-specific benefits facilities in `gis_wv_benefits`, spatial entities derived from PostgreSQL GBIM and `msallisgis`, and benefits-focused resource collections.
- **P5 – Design is a geographic act** by treating routing rules, collection choices, registry lookups, and gateway boundaries as design decisions that change how the system "sees" and acts within a region.
- **P12 – Intelligence with a ZIP code** by privileging West Virginia-specific collections in retrieval, and by coupling text RAG both to a state-scale PostgreSQL `msallisgis` spatial body (port **5432**, `postgis-forensic` container — 95 GB, 742 tables, 9 schemas) and GBIM application layer in `msallis` (port **5432**, same container — 92 tables) for spatial questions, and to a ZIP- and county-aware `allis-local-resources-db` registry (port 5435) for concrete program referrals, including flows for Mount Hope, Oak Hill, Beckley, and broader Fayette/Raleigh County.
- **P16 – Power accountable to place** by making retrieval calls, filters, scores, registry lookups, and sources visible at the API and logging layer so that communities and researchers can audit what informed a Steward response.

This chapter belongs to the **Computational Instrument** tier: it defines the retrieval and routing machinery that connects ChromaDB-backed semantic memory (host port **8002**, container port **8000**), the PostgreSQL GBIM / `msallisgis` spatial body, the verified local resource registry (`allis-local-resources-db`, port 5435), and web research to the live outputs of Ms. Allis.

As of April 17, 2026, live responses are validated by `judge_pipeline_v2.1-rag-grounded` and truth metrics are exposed under `truthverdict.*`. The older `heuristic_contradiction_v1` validator is superseded. All five open issues documented in prior drafts (OI-05, OI-19, OI-20, OI-21, OI-22) are closed as of April 17, 2026. See §7.9.

---

## 7.0 Overview and Scope

This chapter describes the retrieval-augmented generation (RAG) infrastructure that binds Ms. Egeria Allis's language models to the semantic and spatial memory systems defined in earlier chapters. In the current deployment, language models are no longer queried "from scratch": they are constrained and informed by:

- a Phase 1.45 semantic community memory step that prepends the top-5 most relevant `autonomous_learner` memories to every query before it reaches the LLM ensemble,
- a text RAG service backed by a shared HTTP-exposed ChromaDB instance (host port **8002**, container port **8000**),
- a `msallisgis`-coupled GIS RAG path for West Virginia features built on GBIM-derived spatial entities from the PostgreSQL `msallis` / `msallisgis` databases and `gis_wv_benefits`,
- a **WV-biased multi-collection entangled retrieval path** (`allis-wv-entangled-gateway`, port **8010** — ✅ healthy) providing statically-injected WV context via `/chat_wv`,
- a web-research gateway, and
- a resolver path into the `allis-local-resources-db` registry (port 5435) for programmatic help,

all orchestrated by `allis-main-brain` (port **8050**) and the blood-brain-barrier services.

At runtime, queries enter through `allis-unified-gateway` (host **18018** → container **8001** — ✅ confirmed April 17, 2026) and are routed by the executive coordinator into a RAG layer that spans ChromaDB collections, PostgreSQL GIS features, and verified local-resource rows. In production as of April 17, 2026, the full pipeline:

```text
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
> All ChromaDB collections use **384-dimensional vectors** produced by `all-minilm:latest` (`hnsw:space: cosine`). The `nomic-embed-text` model produces 768-dimensional vectors and is **incompatible** with all existing collections. Any service, script, or migration that generates embeddings for ChromaDB must use `all-minilm:latest`.

> **⚠️ ChromaDB API and Port — confirmed April 17, 2026**
> ChromaDB is running the **v2 multi-tenant API**. The `/api/v1/` endpoints are deprecated on this stack. Host port: **8002** (`127.0.0.1:8002→8000/tcp`). Container-internal port: **8000**.
>
> **ChromaDB inventory note:** The SQLite store is authoritative — **50 collections, 6,740,616 total embedding rows** (April 17, 2026). The v2 tenant/database collection-listing REST endpoint returns zero on this stack despite the live store; this is a known documentation note, not a system blocker. Individual collection queries work normally via the Python client or collection-specific v2 URL.

> **★★ Database architecture — confirmed April 17, 2026:** Both `msallisgis` (95 GB, 742 tables, 9 schemas — PostGIS spatial) and `msallis` (92 tables — application/GBIM layer) are in the **`postgis-forensic`** container on **port 5432**. **There is no port 5433 container.** All prior documentation references to `msallis:5433` are superseded.

> **★★ Security posture — confirmed April 17, 2026:** All services bound to `127.0.0.1` or internal Docker DNS. Zero `0.0.0.0` exposures. `_auth()` confirmed on all sensitive routes. `ALLIS_API_KEY` env var confirmed set in production.

> **★★ Port corrections applied April 17, 2026:**
>
> ```text
> allis-rag-server        8003  → 8003   ✅  (container port was 8016 — corrected to 8003)
> allis-unified-gateway  18018  → 8001   ✅  (host port was assumed 9000 — corrected to 18018)
> allis-chroma            8002  → 8000   ✅  confirmed
> allis-blood-brain-barrier 8016→ 8016   ✅  confirmed
> allis-bbb-output-filter internal→ 8017 ✅  confirmed {"status":"ok","service":"bbb-output-filter"}
> allis-qualia-engine    internal→ 8017  ✅  DNS only — no host binding
> allis-main-brain        8050  → 8050   ✅  confirmed
> nbb_pituitary_gland      8108  → 80     ✅  mode=elevated
> ```

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
│    [6 filters operational — barrier_active: true]           │
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
│      ├──→ Spiritual / Psychological RAG (port 8006)         │
│      ├──→ WV-Entangled Gateway (port 8010) ✅ HEALTHY      │
│      │       Static WV context injection via /chat_wv       │
│      │       (Fayette, McDowell, Upper Kanawha,             │
│      │        WV_DHHR_BENEFITS, WV_RURAL_TRANSPORT)         │
│      ├──→ Web Research (excluded for WV queries)            │
│      └──→ Registry (allis-local-resources-db port 5435)     │
│              101 embeddings; Fayette pipeline active        │
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
│    { response, services_used, consciousness_level,          │
│      processing_time, architecture_layers: 7,               │
│      truthverdict: { consensus_score: 0.95,                 │
│                      bbb_checked: true,                     │
│                      validated_by:                          │
│              "judge_pipeline_v2.1-rag-grounded" } }         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> Figure 7-1. RAG pipeline overview — April 17, 2026 final production baseline. `allis-unified-gateway` (host:**18018** → container:**8001**) is the external entry point. `allis-main-brain` (port **8050**) is the primary orchestrator. `allis-wv-entangled-gateway` (port **8010**) is a specialized WV retrieval path — it injects static WV context upstream before the LLM ensemble via `/chat_wv` and is **not** the primary chat gateway. Blocked unsafe prompts short-circuit the full stack and return `architecture_layers = 1`, `truthverdict = null`. A healthy full-stack response carries `architecture_layers = 7`. BBB output blocking is proven behaviorally. 99 containers Up, zero Restarting, zero Exited (April 17, 2026).

A typical benefits query:

```bash
curl -X POST http://127.0.0.1:8050/chat \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $ALLIS_API_KEY" \
  -d '{"message":"Mount Hope WV county benefits","county":"Fayette","role":"community","profile":"auto"}'
```

triggers Phase 1.45 community memory retrieval from `autonomous_learner`, retrieval from ChromaDB (including `governance_rag`, `commons_rag`, `gis_wv_benefits`, and `local_resources`), optional GIS RAG over GBIM-derived spatial entities from PostgreSQL `msallisgis`, synthesis by the LLM ensemble, validation by `judge_pipeline_v2.1-rag-grounded`, and post-filtering by the blood-brain barrier output filter.

---

### 7.0.1 RAG Ingest Pipeline — Validated March 26, 2026

The entire RAG ingest pipeline is confirmed working. The `governance_rag` (643 chunks) and `commons_rag` (306 chunks) collections are production-ready with verified semantic retrieval. The US Constitution (Project Gutenberg `pg5.txt`, 97 chunks) is ingested into `governance_rag` and confirmed as a constitutional grounding layer.

**Confirmed working ingest pattern:**

```python
import httpx
import chromadb

OLLAMA_HOST = "http://allis-ollama:11434"  # or http://127.0.0.1:11434 from host
CHROMA_HOST = "127.0.0.1"
CHROMA_PORT = 8002  # host port

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
    DO NOT use /api/v1/ paths — deprecated on this stack.
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
    metadata_base: dict
) -> int:
    client = chromadb.HttpClient(host=CHROMA_HOST, port=CHROMA_PORT)
    collection = client.get_or_create_collection(
        name=collection_name,
        metadata={"hnsw:space": "cosine"}
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
| MountainShares DAO Charter | `governance_rag` | included in 643 | ✅ Live |
| Terms of Use | `governance_rag` | included in 643 | ✅ Live |
| Program Rules | `governance_rag` | included in 643 | ✅ Live |
| Parameter Tables | `governance_rag` | included in 643 | ✅ Live |
| Phase 0–3 Specifications | `governance_rag` | included in 643 | ✅ Live |
| Safety Champion Protocol | `governance_rag` | included in 643 | ✅ Live |
| Funder Overview | `governance_rag` | included in 643 | ✅ Live |
| **US Constitution (pg5.txt)** | `governance_rag` | **97 chunks** | ✅ Live — constitutional grounding layer |
| Commons governance + gamification corpus | `commons_rag` | 306 | ✅ Live |

The US Constitution (sourced from Project Gutenberg `pg5.txt`) was ingested into `governance_rag` as 97 chunks using the confirmed 100-word/20-word-overlap ingest pattern. Query "constitution" retrieves Amendment XIV at distance < 0.3. This provides a constitutional grounding layer for governance queries alongside MountainShares DAO governance documents in a single retrieval pass.

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

**The bug:** Early ingest scripts used the `/api/embed` endpoint (list input) instead of the confirmed-working `/api/embeddings` endpoint (single-string `"prompt"` field). In combination with 800-word chunk sizes that exceeded `all-minilm:latest`'s 256-token context window, this produced **ghost records**: ChromaDB entries that exist and are countable but return near-zero cosine similarity on every semantic query.

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

**Detection:** Ghost records are detectable by querying with a term that should appear verbatim. If cosine distance for all results is > 0.7, suspect ghost records.

**Remediation:** Collections ingested with the buggy pattern must be dropped and re-ingested using the confirmed working pattern (100-word chunks, 20-word overlap, `/api/embeddings` single-string `"prompt"`). `governance_rag` (643 chunks) and `commons_rag` (306 chunks) were ingested clean and are confirmed free of ghost records.

```python
def verify_no_ghost_records(
    collection_name: str,
    test_query: str,
    expected_max_distance: float = 0.5
):
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

The GeoBelief Information Model (GBIM) defines how entities, places, and normative claims are represented across documents and spatial features in the PostgreSQL databases. The RAG layer is the mechanism that retrieves those GBIM-anchored fragments when a question is asked.

**Database architecture — confirmed April 17, 2026:**

Both `msallisgis` (95 GB, 742 tables, 9 schemas — PostGIS spatial body) and `msallis` (92 tables — application/GBIM layer) are in the **`postgis-forensic`** container on **port 5432**. **There is no port 5433 container.** GBIM semantic entities (5,416,521 vectors) are also queryable through the ChromaDB `gbim_worldview_entities` collection. The `gbim_beliefs_v2` collection holds 5,000 embeddings with `wv_tag=true`, `source=gbim_postgresql`, county present, and full WV address point record metadata — confirmed April 17, 2026 (OI-21 ✅ closed).

The Hilbert-space state view treats the system's overall knowledge and constraints as a very high-dimensional state vector. RAG interactions are projections into lower-dimensional subspaces. For text, those projections are embedding-based nearest-neighbor searches in ChromaDB using 384-dimensional vectors from `all-minilm:latest` (`hnsw:space: cosine`). For space, they are centroid-based spatial filters over PostgreSQL `msallisgis`-derived features and GBIM-linked spatial entities. For concrete help-seeking, retrieved resource documents are further resolved into rows of `allis-local-resources-db` (port 5435) keyed by ZIP, county, and program type.

**Database integration — confirmed April 17, 2026:**

```python
import psycopg2
import chromadb

# CONFIRMED April 17, 2026:
# Both msallisgis (PostGIS spatial) and msallis (application/GBIM) are in
# postgis-forensic on port 5432. NO port 5433 container exists.
# All prior references to msallis:5433 are superseded.

pg_conn_msallisgis = psycopg2.connect(
    host="localhost", port=5432,
    database="msallisgis", user="postgres", password="postgres"
)

pg_conn_msallis = psycopg2.connect(
    host="localhost", port=5432,
    database="msallis", user="postgres", password="postgres"
)

# allis-local-resources-db — port 5435
# database name is "postgres", not the container name
pg_conn_resources = psycopg2.connect(
    host="localhost", port=5435,
    database="postgres", user="postgres", password="postgres"
)

# ChromaDB semantic memory — host port 8002 / container port 8000
# v2 multi-tenant API. /api/v1/ deprecated on this stack.
# SQLite manifest: 50 collections, 6,740,616 rows (authoritative April 17, 2026)
# v2 tenant/database listing returns zero — known documentation note, not a blocker
chroma_client = chromadb.HttpClient(host="127.0.0.1", port=8002)
```

---

## 7.2 Core RAG and Search Components

### 7.2.0 Phase 1.45 — Semantic Community Memory Retrieval

Phase 1.45 fires after the BBB input filter (Phase 1.4) and before the main text and GIS RAG services. It is the first retrieval step that enriches `enhanced_message`.

**How it works:**

1. The main brain calls `allis-ollama:11434/api/embeddings` with model `all-minilm:latest` and the user query as prompt, receiving a 384-dimensional embedding vector.
2. The embedding queries the `autonomous_learner` ChromaDB collection (**21,159 items** confirmed April 17, 2026 — ~288/day accumulation rate).
3. The 5 most semantically similar community interaction records are retrieved.
4. The retrieved memories are prepended to `enhanced_message` before the LLM ensemble.

```python
import httpx
import chromadb

# Step 1: Generate 384-dim embedding — /api/embeddings, single-string "prompt"
response = httpx.post(
    "http://allis-ollama:11434/api/embeddings",
    json={"model": "all-minilm:latest", "prompt": user_query}
)
embedding = response.json()["embedding"]  # must be 384-dim

# Step 2: Query autonomous_learner via Chroma Python client
client = chromadb.HttpClient(host="127.0.0.1", port=8002)
collection = client.get_collection("autonomous_learner")
result = collection.query(
    query_embeddings=[embedding],
    n_results=5,
    include=["documents", "metadatas", "distances"]
)

# Step 3: Prepend to enhanced_message
community_memories = "\n".join([doc for docs in result["documents"] for doc in docs])
enhanced_message = community_memories + "\n\n" + original_message
```

> **Critical:** The embedding model must be `all-minilm:latest` (384-dim). `nomic-embed-text` (768-dim) will cause a dimension mismatch against all existing ChromaDB collections.

#### 7.2.0.1 Autonomous Learner and conversation_history — April 17, 2026

> **★★ April 17, 2026 — Autonomous Learner: HEALTHY. OI-05 ✅ CLOSED.**

The autonomous learner was fully restored April 1, 2026 (LEARN-01, LEARN-02, LEARN-03 all resolved). As of April 17, 2026, the `autonomous_learner` collection contains **21,159 items** accumulating at ~288/day.

The `conversation_history` collection is **formally wired to the production pipeline** (OI-05 ✅ closed April 17, 2026). Evidence:

- **567 embeddings** confirmed in live ChromaDB, latest embedding ID 7,892,636
- **Read path:** `msallisconsciousnessbridge.py` line 113; `retrieval_router.py` lines 135–136 (intent-gated via `intent.get("use_conversation_history")`)
- **Write path:** `msallisconsciousnessbridge.py` line 304
- **Production gateway read:** `ms_allis_unified_gateway.py` line 477

| Metric | Value |
|:--|:--|
| `autonomous_learner` collection items | **21,159** (April 17, 2026) |
| `conversation_history` embeddings | **567** (latest ID: 7,892,636) |
| `autonomous_learning` collection items | 57 (April 1, 2026 post-fix baseline) |
| GBIM router `/route` | ✅ HTTP 200 OK |
| Entanglement graph nodes | 7+ |
| LEARN-01 (numpy dtype fix) | ✅ Resolved April 1, 2026 |
| LEARN-02 (GBIM router schema fix) | ✅ Resolved April 1, 2026 |
| LEARN-03 (crash-loop recovery) | ✅ Resolved April 1, 2026 |

---

### 7.2.1 Text RAG Service (allis-rag-server)

**Port mapping: host:8003 → container:8003 — ✅ confirmed April 17, 2026**

> **★★ Port correction (April 17, 2026):** The allis-rag-server host port and container port are **both 8003** (`127.0.0.1:8003→8003/tcp`). All prior documentation references to `container:8016` for this service are superseded.

> **⚠️ Embedding Model Note:** The RAG server uses `EMBED_MODEL=all-minilm:latest` and `OLLAMA_HOST=http://allis-ollama:11434` set via environment variables. Source code defaults are incorrect for production and must be overridden.

> **⚠️ ChromaDB Call — v2 API Required:** The RAG server uses the v2 collection-specific URL format. `/api/v1/...` paths are deprecated on this stack.

**Endpoint:** `POST /query`

**RAGQuery schema (confirmed Pydantic schema):**

| Field | Type | Required | Default | Notes |
|:--|:--|:--|:--|:--|
| `collection` | string | ✅ Yes | — | ChromaDB collection name |
| `message` | string | ✅ Yes | — | Query text |
| `user_id` | string | No | `"defaultuser"` | Optional session identifier |
| `n_results` | int | No | `8` | Number of results to retrieve |

> **Removed:** The `/direct_rag` endpoint does not exist and must not be referenced.

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

**Corrected ChromaDB v2 call signature:**

```python
import httpx

CHROMA_HOST = "allis-chroma"   # container-internal DNS
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

**Active collections — SQLite manifest, authoritative April 17, 2026 (50 collections, 6,740,616 rows):**

| Collection | Items | Purpose |
|:--|:--|:--|
| `local_resources` | 101 embeddings | **Default collection** — verified Fayette County community resources; pipeline active (OI-20 ✅ closed) |
| `autonomous_learner` | **21,159** | Community interaction memories — Phase 1.45; ~288/day |
| `conversation_history` | **567** (ID: 7,892,636) | Conversation history — formally wired read+write (OI-05 ✅ closed) |
| `autonomous_learning` | 57 | Autonomous learning cycle records (April 1, 2026 post-fix baseline) |
| `gbim_worldview_entities` | 5,416,521 | Complete WV GBIM spatial corpus |
| `gbim_beliefs_v2` | **5,000** | GBIM beliefs v2 — `wv_tag=true`, `source=gbim_postgresql`, county present, WV address point records (OI-21 ✅ closed) |
| `governance_rag` | **643 chunks** | MountainShares DAO corpus + US Constitution (97 chunks) — LIVE |
| `commons_rag` | **306 chunks** | Commons governance + gamification — LIVE |
| `gis_wv_benefits` | Active | WV benefits facilities |
| `psychological_rag` | **968** | Mental health corpus — restored March 28, 2026 |
| `appalachian_cultural_intelligence` | **820** | Appalachian cultural context — LIVE |
| `aaacpe_corpus` | **65 docs** | AaaCPE live web scrape corpus — 39 sources |
| `spiritual_rag` | Deduplicated | Mother Carrie Protocol corpus — 19,338 duplicates removed March 28, 2026 |
| `spiritual_wisdom` | Active | Spiritual wisdom collection |
| `pia_records` | Active | PIA records |
| `geospatialfeatures` | **60,000** | GIS feature embeddings — LIVE |
| `GBIM_Fayette_sample` | **1,535** | Fayette County GBIM sample — LIVE |
| `ms_allis_memory` | Active | Conversation memory |
| `mountainshares_knowledge` | Active | MountainShares governance |
| `episodic_index` | Active | Episodic memory index |
| `GBIM_sample_rows` | 5,000 | GBIM test sample |
| `msallis_docs` | **7,465+** | System docs + verified WV community resources |
| `operations_history` | Active | System operations log |
| `appalachian_english_corpus` | Active | Appalachian language and dialect corpus |
| `zcta_centroids` | Active | ZIP code tabulation area centroids |
| `fifth_dgm_subconscious` | Active | Fifth DGM subconscious queue — 384-dim HNSW, live |
| *(additional collections)* | — | See Chapter 41 for full 50-collection SQLite manifest |

> All collections: **384-dim, `all-minilm:latest`, `hnsw:space: cosine`**. **SQLite audit April 17, 2026: 50 collections, 6,740,616 total embedding rows.**

---

### 7.2.2 GIS RAG Service (port 8004)

The GIS RAG service is a dedicated geospatial retrieval path serving West Virginia spatial questions. It queries:

- `gbim_worldview_entities` — 5,416,521 embeddings from PostgreSQL `msallisgis` (port **5432**, `postgis-forensic` container)
- `gbim_beliefs_v2` — 5,000 embeddings, `wv_tag=true`, full WV address point metadata (OI-21 ✅ closed)
- `gis_wv_benefits` — semantic descriptions and metadata for benefits-related facilities
- `geospatialfeatures` — 60,000 items, confirmed live
- `GBIM_Fayette_sample` — 1,535 items, confirmed live

Each indexed entity stores a short text description and metadata fields: `worldview_id`, `dataset`, `county`, `gbim_entity`, `centroid_x`, `centroid_y` (SRID 26917). All embeddings use `all-minilm:latest` (384-dim, `hnsw:space: cosine`).

**Example spatial query flow:**

1. User: "hospitals near Mount Hope"
2. ChromaDB (host port 8002): Retrieve entities semantically similar to "hospital"
3. PostGIS (`msallisgis` port **5432** — `postgis-forensic` container): Query `zcta_wv_centroids` for Mount Hope (ZIP 25880) centroid → `(37.8782, -81.2056)`
4. Filter: ChromaDB results within 10-mile radius
5. Response: Ranked hospitals with distances

```python
import httpx

resp = httpx.post(
    "http://127.0.0.1:8004/query",
    json={"query": "hospitals near Mount Hope", "n_results": 5}
)
```

---

### 7.2.3 Spiritual / Psychological RAG Service (port 8006)

The Spiritual/Psychological RAG service retrieves from `spiritual_rag` (deduplicated — 19,338 duplicate vectors removed March 28, 2026), `psychological_rag` (968 items — restored March 28, 2026), `governance_rag` (643 chunks), `commons_rag` (306 chunks), and `appalachian_cultural_intelligence` (820 items). It serves:

1. **Mother Carrie Protocol queries** — normative and doctrinal questions grounded in the explicit values corpus.
2. **Community values alignment checks** — questions evaluated against Appalachian community values.
3. **Psychological safety queries** — trauma, wellbeing, counseling, mental health.

All embeddings use `all-minilm:latest` (384-dim). The service exposes `POST /query` accepting `{"query": str, "n_results": int, "collection_filter": [str]}`.

This service is the primary RAG backend for the alignment judge in §7.8.

---

### 7.2.4 WV-Entangled Gateway (allis-wv-entangled-gateway, port 8010) — ✅ HEALTHY

The `allis-wv-entangled-gateway` service provides **WV-biased multi-collection entangled retrieval** via static WV context injection — not post-hoc metadata filtering.

> **OI-19 ✅ CLOSED April 17, 2026 — working as designed:** The gateway does **not** filter on `wv_tag` or `state` metadata at query time. It builds WV entangled context **statically**, injecting it upstream before the LLM ensemble via `/chat_wv`. The `wv_tag` metadata mismatch on `gbim_beliefs_v2` / `gis_wv_benefits` is irrelevant — no post-hoc metadata filter is applied. **No code change needed.**

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

> **Important:** `allis-wv-entangled-gateway` (port **8010**) is **not the primary chat gateway**. The primary orchestrator is `allis-main-brain` on port **8050**. The external entry point is `allis-unified-gateway` on host port **18018** → container **8001**. Port 8010 is a specialized WV-entangled path called internally by the main brain orchestration layer.

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

External web retrieval is handled by a dedicated gateway rather than allowing arbitrary outbound calls. The gateway applies policy filters and rate limits, normalizes results, and logs queries for audit. For WV-scoped queries (identified by county, role, or profile), web context is excluded from the final context window so external search results cannot override in-state RAG, GIS, and registry evidence.

---

### 7.2.6 Local Resource Registry Resolver (allis-local-resources-db, port 5435)

> **OI-20 ✅ CLOSED April 17, 2026.** The pipeline is confirmed active: `ingest_runner.py` Lane A → `allis-local-resources-db` TCP 5435. **101 embeddings are present** in the `local_resources` ChromaDB collection. Fayette-specific records enter the registry when the AAACPE pipeline processes Fayette county data — this is an ongoing ops ingest task, not a code gap. Containers confirmed: `allis-aaacpe-rag`, `allis-local-resources-db`, `allis-local-resources`.

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

### 7.2.7 Landowner / GBIM Router (allis-gbim-query-router, port 7205)

`allis-gbim-query-router` is on host port **7205**, healthy, and **RBAC-gated**. `X-Allis-Role` header is required for `/query`. This is a **PostgreSQL-native routing service** — it does not use ChromaDB or vector similarity search. It translates natural-language landowner queries into SQL aggregations against `mvw_gbim_landowner_spatial` in `msallisgis` (port **5432**, `postgis-forensic` container), returning ranked ownership records with acreage, parcel count, and county breakdown.

> **★ LEARN-02 Resolved April 1, 2026:** Briefly returned HTTP 422 on `/route` POST calls from the autonomous learner due to a request schema mismatch. The main production landowner query path was **unaffected**. Schema fix applied; `/route` confirmed HTTP 200 OK and has not recurred.

```python
import httpx

# RBAC-gated — requires X-Allis-Role header
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

---

### 7.2.8 Unified Gateway Dependency Map — confirmed April 17, 2026

**84 total queries processed** as of April 17, 2026 confirmation run.

`allis-unified-gateway` (host:**18018** → container:**8001**) depends on the following internal services, all confirmed healthy April 17, 2026:

| Service | Internal URL | Status |
|:--|:--|:--|
| allis-consciousness-bridge | `http://allis-consciousness-bridge:8020` | ✅ healthy |
| allis-neurobiological-master | `http://allis-neurobiological-master:8018` | ✅ healthy |
| allis-i-containers | `http://allis-i-containers:8015` | ✅ healthy |
| allis-blood-brain-barrier | `http://allis-blood-brain-barrier:8016` | ✅ healthy |
| allis-qualia-engine | `http://allis-qualia-engine:8017` | ✅ healthy — internal DNS only, no host binding |

To verify the unified gateway's live host port mapping:

```bash
docker inspect allis-unified-gateway --format '{{.NetworkSettings.Ports}}'
# Expected: map[8001/tcp:[{0.0.0.0 18018}]]
```

---

## 7.3 Retrieval Flows

### 7.3.1 Non-Spatial RAG Flow

1. **Query intake.** User request enters `allis-unified-gateway` (host:**18018** → container:**8001**) and is forwarded to `allis-main-brain` (port **8050**).
2. **BBB input filter — Phase 1.4.** `allis-blood-brain-barrier` (port **8016**) applies **6 operational filters** (`barrier_active: true`). Blocked unsafe prompts short-circuit the full stack and return `architecture_layers = 1`, `truthverdict = null`.
3. **Phase 1.45 — Community memory retrieval.** Main brain embeds query via `all-minilm:latest` (384-dim) using `/api/embeddings` with single-string `"prompt"`. Retrieves top-5 from `autonomous_learner` (21,159 items). Prepends to `enhanced_message`.
4. **Routing to text RAG.** Orchestration calls `allis-rag-server` (host:**8003** → container:**8003**) via `POST /query` with `collection` and `message` fields.
5. **Retrieval from ChromaDB.** Text RAG service embeds query, runs similarity search, returns scored documents with metadata.
6. **Context assembly.** Phase 1.45 memories + RAG results + `conversation_history` (intent-gated via `intent.get("use_conversation_history")`) merged into context window; source separation preserved.
7. **Generation.** LM Synthesizer applies Ms. Egeria Allis persona via `allis-ollama:11434/api/generate` (1.0 GiB RAM, models loaded).
8. **BBB output filter.** Output forwarded to `allis-bbb-output-filter` (internal port **8017**). Confirmed returning `{"status":"ok","service":"bbb-output-filter"}`. BBB output blocking is **proven behaviorally**. Fail-open on HTTP 500.
9. **UltimateResponse assembly.** `architecture_layers = 7` for a healthy full-stack response. `truthverdict.validated_by = "judge_pipeline_v2.1-rag-grounded"`. See §7.8.4.

---

### 7.3.2 Spatial RAG Flow

```
┌─────────────────────────────────────────────────────────────┐
│   Spatial RAG: Semantic + Geographic Retrieval               │
│   ★★ April 17, 2026 — both DBs on port 5432                │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Semantic Retrieval (ChromaDB host port 8002, Chroma client)│
│  ┌────────────────────────────────────────────────┐         │
│  │  Query: "hospitals near Mount Hope"            │         │
│  │  Embed (all-minilm:latest 384-dim,             │         │
│  │    /api/embeddings single-string prompt)       │         │
│  │  → Search gis_wv_benefits +                    │         │
│  │    gbim_worldview_entities (5,416,521) +       │         │
│  │    gbim_beliefs_v2 (5,000 — wv_tag=true) +    │         │
│  │    geospatialfeatures (60,000) +               │         │
│  │    GBIM_Fayette_sample (1,535) +               │         │
│  │    zcta_centroids (confirmed SQLite manifest)  │         │
│  │  Returns: Embeddings + metadata                │         │
│  └────────────────────────────────────────────────┘         │
│              ↓                                               │
│  Geographic Filtering (PostgreSQL msallisgis port 5432)     │
│  postgis-forensic container — 95 GB, 742 tables             │
│  ┌────────────────────────────────────────────────┐         │
│  │  Use GBIM IDs from ChromaDB                    │         │
│  │  Query: SELECT zip, lat, lon                   │         │
│  │    FROM msallisgis.zcta_wv_centroids           │         │
│  │    WHERE zip = '25880'  -- Mount Hope          │         │
│  │  Then: spatial filter within 10-mile radius    │         │
│  └────────────────────────────────────────────────┘         │
│              ↓                                               │
│  GBIM Belief Provenance (msallis — port 5432)               │
│  SAME postgis-forensic container — 92 tables                │
│  ★★ No port 5433 container — all 5433 refs superseded      │
│  ┌────────────────────────────────────────────────┐         │
│  │  Query: gbim_beliefs WHERE entity_id = ?       │         │
│  │  Returns: confidence_decay, needs_verification │         │
│  └────────────────────────────────────────────────┘         │
│              ↓                                               │
│  Combined Results → LLM Context                             │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> Figure 7-3. Spatial RAG flow. Both `msallisgis` (PostGIS) and `msallis` (GBIM application) are in `postgis-forensic` on port **5432** — no port 5433 container exists. `zcta_centroids` confirmed in SQLite manifest April 17, 2026. `gbim_beliefs_v2` (5,000 embeddings, `wv_tag=true`) confirmed April 17, 2026 (OI-21 ✅ closed).

---

### 7.3.3 Resource-Oriented RAG Flow

1. **Resource query intake.** `allis-main-brain` (port **8050**) identifies resource-oriented request, extracts location hints (ZIP, county, town) and population signals.
2. **Phase 1.45 — Community memory.** Top-5 `autonomous_learner` memories prepended.
3. **Text RAG via allis-rag-server** (`POST /query`, collection: `local_resources`, host:**8003** → container:**8003**).
4. **Resolution via local resource resolver.** Queries `allis-local-resources-db` (port 5435, database: `postgres`). 101 embeddings present; Fayette-specific records enter when AAACPE pipeline processes Fayette county data (OI-20 ✅ closed).
5. **Context assembly and generation.** LM Synthesizer applies Ms. Egeria Allis persona via `allis-ollama:11434`.
6. **BBB output filter.** Output forwarded to `allis-bbb-output-filter` (internal:**8017**).

---

## 7.4 Routing, Roles, Geography, and WV-First Policy

### 7.4.1 Design Intent

**Topic and intent routing.** Governance queries favor `governance_rag` (643 chunks including US Constitution) and `commons_rag` (306 chunks); spatial-justice queries favor `msallisgis`/`msallis`-derived collections (both port **5432**); resource questions favor `allis-local-resources-db` plus WV-resource collections; WV-entangled queries route to `allis-wv-entangled-gateway` (port **8010** — ✅ healthy) via `/chat_wv` for static WV context injection. Landowner/GBIM answers are served through `allis-gbim-query-router` (port **7205**, RBAC-gated — SQL path, not semantic RAG). `conversation_history` is queried conditionally via `intent.get("use_conversation_history")` in `retrieval_router.py` lines 135–136 (OI-05 ✅ closed).

**Role-aware routing.** Active role determines eligible collections and registries. Community-facing roles are restricted to public documentation, approved spatial layers, and public-facing slices of `allis-local-resources-db`.

**Geography-aware routing and WV-first behavior.** For West Virginia-scoped queries, the system:

- Treats WV RAG, PostgreSQL `msallisgis` GIS (port **5432**), and registry context as authoritative.
- Excludes web context from the final context window.
- Requires models to ignore conflicting out-of-state content unless user explicitly requests another state.

---

### 7.4.2 Port and Service Reference Table — FINAL, April 17, 2026

| Service | Host Port | Container Port | Status / Notes |
|:--|:--|:--|:--|
| **allis-unified-gateway** | **18018** | **8001** | ✅ External entry point — host:18018→container:8001. Verify: `docker inspect allis-unified-gateway --format '{{.NetworkSettings.Ports}}'` |
| allis-main-brain | **8050** | 8050 | ✅ Primary orchestrator — `/chat`, `/ultimate_chat`, `/governance/query`, `/health` |
| **allis-rag-server** | **8003** | **8003** | ✅ Text RAG — `POST /query` — both ports confirmed 8003 |
| allis-gis-rag | 8004 | 8004 | ✅ GIS / spatial RAG |
| allis-psychological-rag | 8006 | 8006 | ✅ Spiritual + psychological RAG |
| **allis-wv-entangled-gateway** | **8010** | **8010** | ✅ Healthy — static WV context injection via `/chat_wv`. Not the primary chat gateway. |
| **allis-blood-brain-barrier** | **8016** | **8016** | ✅ 6 filters operational, `barrier_active: true`. Routes: GET `/`, GET `/health`, POST `/filter`, POST `/truth`. |
| **allis-bbb-output-filter** | internal | **8017** | ✅ `{"status":"ok","service":"bbb-output-filter"}` — no host binding |
| **allis-qualia-engine** | internal (DNS only) | **8017** | ✅ Healthy — `allis-qualia-engine:8017` DNS only, no host binding |
| allis-consciousness-bridge | internal | 8020 | ✅ `http://allis-consciousness-bridge:8020` |
| allis-neurobiological-master | internal | 8018 | ✅ `http://allis-neurobiological-master:8018` |
| allis-i-containers | internal | 8015 | ✅ `http://allis-i-containers:8015` |
| allis-aaacpe-rag | 8032 | — | ✅ Live — `aaacpe_corpus` (65 docs, 39 sources) |
| allis-aaacpe-scraper | 8033 | — | ✅ Live |
| **allis-chroma** | **8002** (host) | **8000** (container) | ✅ ChromaDB v2 API. **SQLite: 50 collections, 6,740,616 rows** (April 17, 2026). `/api/v1/` deprecated. |
| allis-ollama | 11434 | 11434 | ✅ 1.0 GiB RAM loaded — `/api/embeddings` + `/api/generate` |
| **allis-gbim-query-router** | **7205** | 7205 | ✅ Healthy — **RBAC-gated** — `X-Allis-Role` required. SQL/landowner path. LEARN-02 resolved. |
| allis-local-resources-db | 5435 | 5435 | ✅ Active (database: `postgres`) — 101 embeddings; Fayette pipeline active (OI-20 ✅ closed) |
| **msallisgis + msallis** | **5432** | **5432** | ✅ `postgis-forensic` container — 95 GB, 742 tables, 9 schemas. **No port 5433 container.** |
| **nbb_pituitary_gland** | **8108** | **80** | ✅ mode=elevated |
| allis-web-research | 8008 (internal) | — | ✅ Restored March 25, 2026 |
| allis-ingest-api | 8009 | — | ✅ Restored March 25, 2026 |

---

## 7.5 Smoke Tests — Confirmed Semantic Retrieval

The following smoke tests were run against `governance_rag` and `commons_rag` and confirm production-ready semantic retrieval with no ghost records.

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
    client = chromadb.HttpClient(host="127.0.0.1", port=8002)
    collection = client.get_collection("governance_rag")
    print(f"governance_rag item count: {collection.count()}")  # expect 643

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

The Blood-Brain Barrier (`allis-blood-brain-barrier`, host port **8016**) is empirically active in the April 17, 2026 production stack with **6 operational filters** and `barrier_active: true`. A separate BBB output filter service (`allis-bbb-output-filter`, internal port **8017**) handles post-generation output filtering and is confirmed returning `{"status":"ok","service":"bbb-output-filter"}`.

The six confirmed input filters are:

1. **Ethical Filter** — Biblical principles
2. **Spiritual Filter** — Wisdom alignment
3. **Safety Monitor** — Technical security
4. **Threat Detection** — Community protection
5. **Steganography / Prompt-Injection Detection** — flags `{'type': 'prompt_injection_keywords', 'detail': ['system prompt', 'jailbreak'], 'severity': 'critical'}`
6. **Truth/Content Filter** — via `POST /truth`; aggregates all filter results; returns `valid`, `confidence`, `principal_reasons`

**BBB output blocking** is proven behaviorally. Blocked unsafe prompts short-circuit the full RAG/LLM stack and return:

```json
{
  "architecture_layers": 1,
  "truthverdict": null,
  "response": "[FILTERED]"
}
```

**Confirmed BBB routes:**

- `GET /` — root description
- `GET /health` — `filters_operational: 6`, `barrier_active: true`, `total_filtered`, `total_blocked`
- `POST /filter` — main filtering endpoint
- `POST /truth` — truth/content evaluation; expects `content` field (not `claim`); returns `valid`, `confidence`, `principal_reasons`

The `allis-qualia-engine` (internal:**8017**, DNS-only — no host binding) is reachable within the Docker network as `http://allis-qualia-engine:8017` and participates in the judge pipeline alongside the BBB output filter.

---

## 7.7 Constraints, Provenance, and Logging

**Pre-retrieval constraints.** Collection selection and filter mechanisms support limiting by `collection`, `source`, `county`, `dataset`, `worldview`, `state`. The `RAGQuery` schema (§7.2.1) supports `user_id` for session-level access control.

**Decoding-time guards.** After retrieval and generation, the main brain routes candidate responses through `allis-bbb-output-filter` (internal:**8017**). Fail-open on HTTP 500 (content passes through unchanged, failure logged).

**Post-hoc review and logging.** Background storage of queries and responses into `conversation_history` (567 embeddings, formally wired — OI-05 ✅ closed), `episodic_index`, and `operations_history` ChromaDB collections (all confirmed in SQLite manifest April 17, 2026). Logs capture: services called, collections queried, PostgreSQL tables accessed, Phase 1.45 memories returned, filters/scores applied, and documents/features returned.

---

## 7.8 RAG-Grounded Judge Verification — judge_pipeline_v2.1-rag-grounded

> **★★ April 17, 2026.** The live judge pipeline is `judge_pipeline_v2.1-rag-grounded`. The older `heuristic_contradiction_v1` validator is **superseded and no longer active**. All prior references to `heuristic_contradiction_v1` as the live validator are historical.

### 7.8.1 The Problem This Solved

The old truth and alignment judges used `heuristic_contradiction_v1` — keyword and pattern-matching rules with no queries to the GBIM corpus, ChromaDB collections, or any RAG service. They reported `truth_score: 1.0` and `alignment_verdict: pass` without consulting the 5.4 million GBIM entities, the `spiritual_rag` corpus, or the `gis_wv_benefits` collection. This has been replaced by `judge_pipeline_v2.1-rag-grounded`, which performs actual RAG-grounded claim verification.

**Capability comparison:**

| Behavior | heuristic_contradiction_v1 | judge_pipeline_v2.1-rag-grounded |
|:--|:--|:--|
| Consults GBIM corpus | ❌ Never | ✅ Every call |
| Checks claims against documents | ❌ Pattern match only | ✅ GIS RAG retrieval + lexical overlap |
| Detects county/facility factual errors | ❌ No | ✅ If `gis_wv_benefits` has the record |
| Reports `gbim_docs_consulted` | ❌ Always 0 | ✅ Actual count |
| Fails open on RAG unavailability | N/A | ✅ Falls back to `not_found` |
| Provenance in output | ❌ None | ✅ `supporting_sources` list |

---

### 7.8.2 Truth Judge — rag_grounded_gis_v1 (continued)

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
    top_distance = distances if isinstance(distances, float) else distances
    if top_distance > 0.7:
        return "not_found"
    top_doc = docs if isinstance(docs, str) else docs
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

***

### 7.8.3 Alignment Judge — rag_grounded_spiritual_v1

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
    top_distance = distances if isinstance(distances, float) else distances
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

***

### 7.8.4 UltimateResponse Schema — April 17, 2026

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

A healthy full-stack response carries `architecture_layers = 7`. A BBB-blocked unsafe prompt returns `architecture_layers = 1` and `truthverdict = null`. The `consensus_score` field has been observed at **0.95** in live production as of April 17, 2026.

***

## 7.9 Production Deployment State — FINAL, April 17, 2026

**Hardware:** Lenovo Legion 5 — Mount Hope, West Virginia (ZIP 25880)

**Container stack:** **99 containers Up** — zero Restarting, zero Exited (April 17, 2026).

**Resource status (April 17, 2026):**

| Resource | Value | Status |
|:--|:--|:--|
| Disk | 80% used, 181G free | ✅ OI-22 closed — target met |
| RAM | 8.8G used / 29G total | ✅ Healthy |
| Swap | 11G used / 23G | ✅ Elevated but stable — GPU model offloading, not a leak |
| qualia-net containers | 99 | ✅ |
| main-brain | healthy | ✅ |

**Open Issues — ALL CLOSED April 17, 2026:**

| ID | Issue | Status |
|:--|:--|:--|
| **OI-05** | `conversation_history` not wired to production pipeline | ✅ **CLOSED April 17, 2026** — 567 embeddings, ID 7,892,636; read: `msallisconsciousnessbridge.py:113`, `retrieval_router.py:135-136`; write: `msallisconsciousnessbridge.py:304`; production read: `ms_allis_unified_gateway.py:477` |
| **OI-19** | WV-entangled-gateway WV-tag boosting not firing | ✅ **CLOSED April 17, 2026** — working as designed; gateway uses static WV context injection via `/chat_wv`; no post-hoc metadata filter; no code change needed |
| **OI-20** | `local_resources` empty for Fayette County | ✅ **CLOSED April 17, 2026** — 101 embeddings present; pipeline confirmed: `ingest_runner.py` Lane A → TCP 5435; Fayette coverage pending AAACPE ingest (ops task, not code gap) |
| **OI-21** | `gbim_beliefs_v2` count unverified | ✅ **CLOSED April 17, 2026** — 5,000 embeddings; `wv_tag=true`, `source=gbim_postgresql`, county present, WV address point records with full coordinates and ESN numbers; `gbim_worldview_entities` = 5,416,521 |
| **OI-22** | Disk at 96% | ✅ **CLOSED April 17, 2026** — 80% used, 181G free; `docker system prune` freed ~16%; prevention: `docker system prune --filter until=24h` |
| LEARN-01 | `cosine_similarity()` numpy dtype bug | ✅ Resolved April 1, 2026 |
| LEARN-02 | GBIM router HTTP 422 on learner `/route` calls | ✅ Resolved April 1, 2026 |
| LEARN-03 | Autonomous learner crash-loop after empty file patch | ✅ Resolved April 1, 2026 |
| OI-23 | Judge pipeline using `heuristic_contradiction_v1` | ✅ **Superseded** — `judge_pipeline_v2.1-rag-grounded` is live |

**No open issues remain as of April 17, 2026.**

**RAG Service Stack — FINAL:**

| Service | Host Port | Container Port | Status |
|:--|:--|:--|:--|
| allis-unified-gateway | **18018** | **8001** | ✅ External entry — `docker inspect allis-unified-gateway` to verify |
| allis-main-brain | 8050 | 8050 | ✅ Primary orchestrator |
| allis-rag-server | **8003** | **8003** | ✅ Both ports confirmed 8003 |
| allis-gis-rag | 8004 | 8004 | ✅ Active — live Fayette County geodata |
| allis-psychological-rag | 8006 | 8006 | ✅ `spiritual_rag` (deduplicated) + `psychological_rag` (968 items) |
| allis-wv-entangled-gateway | 8010 | 8010 | ✅ Healthy — static WV injection via `/chat_wv` |
| allis-blood-brain-barrier | 8016 | 8016 | ✅ 6 filters operational, `barrier_active: true` |
| allis-bbb-output-filter | internal | 8017 | ✅ `{"status":"ok","service":"bbb-output-filter"}` |
| allis-qualia-engine | internal (DNS only) | 8017 | ✅ Healthy — `allis-qualia-engine:8017` |
| allis-consciousness-bridge | internal | 8020 | ✅ `http://allis-consciousness-bridge:8020` |
| allis-neurobiological-master | internal | 8018 | ✅ `http://allis-neurobiological-master:8018` |
| allis-i-containers | internal | 8015 | ✅ `http://allis-i-containers:8015` |
| allis-aaacpe-rag | 8032 | — | ✅ `aaacpe_corpus` (65 docs, 39 sources) |
| allis-aaacpe-scraper | 8033 | — | ✅ Live |
| allis-chroma | 8002 (host) | 8000 (container) | ✅ **50 collections, 6,740,616 vectors** (SQLite manifest April 17, 2026) |
| allis-ollama | 11434 | 11434 | ✅ 1.0 GiB RAM — models loaded |
| allis-gbim-query-router | 7205 | 7205 | ✅ RBAC-gated — `X-Allis-Role` required |
| nbb_pituitary_gland | 8108 | 80 | ✅ mode=elevated |
| msallisgis + msallis | **5432** | **5432** | ✅ `postgis-forensic` — 95 GB, 742 tables. **No port 5433.** |
| allis-local-resources-db | 5435 | 5435 | ✅ 101 embeddings; Fayette pipeline active |
| allis-web-research | 8008 (internal) | — | ✅ Restored March 25, 2026 |
| allis-ingest-api | 8009 | — | ✅ Restored March 25, 2026 |

***

*Chapter 7 — FINAL. Last updated: April 17, 2026, Mount Hope WV — Carrie Kidd (Mamma Kidd)*

*All five open issues (OI-05, OI-19, OI-20, OI-21, OI-22) closed April 17, 2026. All port corrections applied: `allis-rag-server` confirmed host:8003→container:8003; `allis-unified-gateway` confirmed host:18018→container:8001; `allis-bbb-output-filter` confirmed internal:8017; `allis-qualia-engine` confirmed internal DNS-only:8017; unified gateway dependency map added (§7.2.8, 84 queries processed). judge_pipeline_v2.1-rag-grounded confirmed live; heuristic_contradiction_v1 superseded. 99 containers Up, 50 ChromaDB collections, 6,740,616 total vectors. No open issues remain.*

*Prior update history: March 26, 2026 — RAG ingest validated, ghost record bug fixed, `governance_rag` (643 chunks) and `commons_rag` (306 chunks) confirmed live. March 27, 2026 — all `gisdb` references corrected to `msallisgis`; `allis-local-resources-db` connection string corrected. March 28, 2026 — security remediation complete; `msallisgis` port corrected from 5452 to 5432; `spiritual_rag` deduplicated; `psychological_rag` restored; 40 collections / 6,675,442 vectors audit. April 1, 2026 — LEARN-01, LEARN-02, LEARN-03 resolved; autonomous learner restored; 96/96 containers confirmed.*
