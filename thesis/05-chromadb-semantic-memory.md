# 5. ChromaDB as Semantic Memory

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: April 23, 2026*

---

## Why This Matters for Polymathmatic Geography

This chapter describes how Ms. Allis uses ChromaDB as its primary semantic memory layer
to support place-based reasoning about West Virginia. The system combines 5,416,521 GBIM
worldview entities stored as embeddings in ChromaDB with structured PostgreSQL databases
(`msallisgis` on `msallis-db` for the GBIM belief graph and spatial data) to create an
inspectable, queryable memory system that grounds AI responses in verified geographic and
institutional context.

This architecture supports:

- **P1 – Every where is entangled** by storing GBIM entities, GIS features, and resource
  documents as searchable embeddings in ChromaDB collections (`gbim_worldview_entities`,
  `autonomous_learner`, `gis_wv_benefits`) that can be jointly retrieved, filtered by
  metadata, and linked back to structured PostgreSQL belief tables and PostGIS geometries,
  treating legal, infrastructural, and social facts about Appalachia as interconnected
  memory rather than isolated files.
- **P3 – Power has a geometry** by representing institutional relationships and access to
  services as explicit GBIM belief edges in PostgreSQL, ChromaDB embeddings with
  geographic metadata, and PostGIS spatial features whose retrieval paths can be logged,
  inspected, and audited.
- **P5 – Design is a geographic act** by treating ChromaDB collection schemas, embedding
  model choices, metadata conventions, PostgreSQL GBIM table structures, RAG retrieval
  rules, and judge pipelines as deliberate interventions into how West Virginia is
  represented and searched.
- **P12 – Intelligence with a ZIP code** by binding ChromaDB collections and PostgreSQL
  spatial tables to West Virginia-specific layers, with GBIM entities carrying county/ZIP
  metadata and PostGIS tables containing 993 WV ZCTA centroids.
- **P16 – Power accountable to place** by making semantic memory, retrieval behavior, and
  query-to-evidence links explicit and queryable through ChromaDB logs, PostgreSQL GBIM
  provenance, and GBIM-aware truth judging.

---

## 5.1 Purpose and Scope

This chapter explains how Ms. Allis uses ChromaDB as the primary semantic memory layer
for:

- GBIM worldview entities.
- Autonomous learning and research traces.
- Governance, legal, safety, and economic texts.
- Community resources and benefits.
- Psychological and spiritual corpora.

ChromaDB stores high-dimensional embedding vectors with metadata and exposes similarity
search and filtering operations that are tightly coupled to both RAG pipelines and a
four-judge safety/truth consensus system.

Key global guarantees:

- **Container**: `allis-chroma` — host port **8002**, container-internal port **8000**.
- **Inter-service URLs**: always use `allis-chroma:8000` (container-internal). From the
  Docker host use `127.0.0.1:8002`. Never use `allis-chroma:8002` in inter-service URLs.
- **Data path**: `/home/ms-allis/msallis-rebuild/persistent/chroma/chroma.sqlite3`
- **API**: v2 only — `/api/v2/` required; `/api/v1/` returns `410 Gone`.
- **Embedding model**: `all-minilm:latest` (384 dimensions).
- **Distance metrics**: **mixed** — 37 collections L2, 11 collections cosine.
- **Chunking rule**: ≈100 words per chunk with ~20-word overlap (256-token model limit).

> ⚠️ **Legacy SQLite files — do not use.**
> Orphaned SQLite files may exist under `/opt/msallis-rebuild/`. These files are **not**
> served by the live `allis-chroma` container and do not reflect current collection
> state. The canonical data path is:
> `/home/ms-allis/msallis-rebuild/persistent/chroma/chroma.sqlite3`
> Any tooling or script that references `/opt/msallis-rebuild/` for ChromaDB data is
> referencing stale, orphaned files and must be updated.

> ⚠️ **ChromaDB API version — BREAKING CHANGE.**
> - `/api/v2/` — **REQUIRED** for all direct REST calls
> - `/api/v1/` — **REMOVED** — returns `410 Gone`
>
> All scripts, services, and documentation must use the v2 full path. The Python
> embedded client (`chromadb.HttpClient`) handles this automatically. Do NOT use
> `/api/v1/` in any new code, script, or documentation.

> ⚠️ **Count calls — UUID two-step pattern required.**
> Direct collection-name count calls are unreliable in ChromaDB v2. Always resolve
> collection name → UUID first via the collection object, then call `.count()`:
>
> ```python
> import chromadb
> # allis-chroma: host 8002 / container 8000
> client = chromadb.HttpClient(host="localhost", port=8002)
> # Step 1: resolve name → UUID (handled internally by get_collection)
> col = client.get_collection("gbim_worldview_entities")
> # Step 2: count via collection object — reliable
> print(col.count())  # 5416521
> ```

> ⚠️ **Embedding model lock — `all-minilm:latest` 384-dim — ENFORCED.**
> The `nomic-embed-text` model produces 768-dimensional vectors and is **incompatible**
> with ALL existing production collections. Any ingestion, retrieval, migration, or
> backfill script MUST use `all-minilm:latest` (384-dim). This constraint is enforced
> at the service level and cannot be overridden by prompting or configuration.
> Attempting to ingest with `nomic-embed-text` will silently corrupt collection geometry
> and produce incorrect similarity rankings.

---

## 5.2 Role in the Ms. Allis Architecture

ChromaDB (`allis-chroma`, host 8002 / container 8000) sits in the middle of Ms. Allis's
architecture as:

1. **Semantic memory store** for text and artifacts:
   - Governance corpora (`governance_rag`, `commons_rag`).
   - Legal and economic corpora (`legal_rag`, `economic_rag`).
   - Cultural, spiritual, psychological, and resource corpora.
2. **Geospatial semantic layer** via `gbim_worldview_entities` (L2), `geospatialfeatures`
   (L2), and GBIM-linked spatial tables in `msallisgis` on `msallis-db`.
3. **RAG engine** for:
   - Text RAG (general knowledge, governance, legal, safety).
   - GIS RAG (spatial queries over West Virginia).
   - AaaCPE cultural intelligence RAG.
4. **Judge grounding backend**:
   - Truth and safety judges call ChromaDB collections (`safety_rules`, `governance_rag`,
     `legal_rag`) as part of their scoring.
   - GBIM-aware truth judge uses both ChromaDB RAG and live GBIM data for verdicts.

Phase 1.45 uses ChromaDB as a community memory layer: before the 20LLM ensemble answers,
the system retrieves recent autonomous learning traces and injects them into the prompt
as context.

---

## 5.3 Collections and Data Domains

### 5.3.1 Mixed-Metric Architecture

This ChromaDB instance does **not** use a single uniform distance metric. Collections
were created at different phases of the `msallis-rebuild` sprint with either L2 or cosine
distance depending on their intended use. **Always verify the distance metric of a
collection before querying or ingesting.** Mixing metrics in a single query pipeline
will produce incorrect similarity rankings.

The production deployment as of April 23, 2026 has **48 confirmed collections** with
**~6.74 million vectors** (April 17, 2026 baseline). The full metric breakdown is
documented in §5.3.6.

### 5.3.2 Spatial: GBIM Worldview Entities

Primary spatial memory:

| Field | Value |
|---|---|
| Collection | `gbim_worldview_entities` |
| Distance metric | **L2** |
| Count | **5,416,521** entities |
| Source | 206 WV GIS source layers |
| CRS | EPSG:26917 (UTM Zone 17N, NAD83) |
| Embedding | 384-dim `all-minilm:latest` |
| Temporal fields | `last_verified`, `confidence_decay`, `needs_verification` |

Ingest ran March 13–14, 2026 (~40 hours, ~40k entities/minute). This collection is the
semantic body of West Virginia: parcels, utilities, infrastructure, environmental
datasets, all entangled with GBIM beliefs and PostGIS geometries.

### 5.3.3 Autonomous Learning and Core Semantic Collections

Autonomous learning lives in two distinct, preserved collections:

| Collection | Count | Distance | Role |
|---|---|---|---|
| `autonomous_learner` | **21,181** | **L2** | Phase 1.45 injection corpus — pre-fix history preserved |
| `autonomous_learning` | **17,685** | **L2** | Current write path — autonomously acquired knowledge |

Both collections are confirmed distinct with no dedup action required — they serve
different temporal roles and are intentionally preserved at their current sizes. Combined
they hold **38,866** items of community interaction and research history.

Other core semantic collections:

| Collection | Count | Distance | Notes |
|---|---|---|---|
| `conversation_history` | 580 | cosine | Healthy; wired into main brain after OI-05 fix |
| `gbim_beliefs_v2` | 5,000 | **cosine** | Production GBIM belief embeddings — separate from spatial corpus |
| `gbim_entities` | 0 | L2 | Empty — legacy/deprecated; superseded by `gbim_worldview_entities` |
| `gbim_beliefs` (bare) | ❌ retired | — | Replaced by `gbim_worldview_entities` (L2) + `gbim_beliefs_v2` (cosine) |
| `psychological_rag` | 6,860 | cosine | Mental health corpus, rechunked from 968 docs |
| `appalachian_cultural_intelligence` | 820 | cosine | Curated Appalachian cultural corpus |
| `aaacpe_corpus` | 65 | cosine | AaaCPE live web scrape (39 sources) |
| `spiritual_rag` | 368,238 | cosine | Deduplicated spiritual corpus, fully rechunked |
| `msallis_docs` | 28,327 | cosine | System docs + resources, rechunked from 8,311 |

### 5.3.4 Governance and Constitutional Corpus

**`governance_rag`** — 1,367 chunks — cosine distance

Includes:

- MountainShares DAO Charter and rules.
- Phase specifications, KPIs, Safety Champion Protocol, and funder docs.
- US Constitution (97 chunks).
- West Virginia Constitution (342 chunks), all normalized to source label `wv_constitution`.

Behavior:

- WV-filtered queries (e.g., "Article I sovereignty") return WV Constitution Article I
  chunks.
- Unfiltered queries allow WV + US Sections/Amendments to compete on semantic relevance.

**`commons_rag`** — 306 chunks — cosine distance — Commons governance and gamification
corpus.

Additional governance/theory:

- `governance` — WV governance texts.
- `thesis` — theoretical framework corpus.
- `mountainshares_knowledge` — MountainShares economics and governance.

### 5.3.5 Legal, Safety, Economic, and Resource Collections

Rechunking brought several corpora into compliance with the 100-word chunk rule:

| Collection | Before | After | Distance | Description |
|---|---|---|---|---|
| `spiritual_texts` / `spiritual_rag` | 79,181 | **368,238** | cosine | Spiritual corpus, deduped and rechunked |
| `msallis_docs` | 8,311 | **28,327** | cosine | Docs + resources, rechunked |
| `psychological_rag` | 968 | **6,860** | cosine | Mental health corpus, rechunked |
| `fayette_county_resources_2026` | 206 | **1,205** | cosine | Fayette resource packet, rechunked |
| `legal_rag` | 155 | **340** | cosine | WV Code and legal texts, rechunked |
| `contracts` | 51 | **673** | cosine | Contracts, rechunked |
| `economic_rag` | 30 | **72** | cosine | Economic/tax/agriculture law, rechunked |

Post-rechunk corpus quality:

| Collection | Count | Distance | Comment |
|---|---|---|---|
| `governance_rag` | 1,367 | cosine | Strong — DAO + US + WV constitutions |
| `legal_rag` | 340 | cosine | Deep WV Code coverage |
| `safety_rules` | 25 | cosine | Six guardrail groups, 15 new constitutional principles |
| `economic_rag` | 72 | cosine | Tax + agriculture law |
| `policy_rag` | 9 | cosine | Policy corpus |
| `meeting_minutes` | 1 | cosine | Governance record |
| `grants_rag` | 9 | cosine | Grants and funding corpus |

**Resource expansion (ongoing)** — The Fayette County baseline is at 1,205 chunks in
`fayette_county_resources_2026`. Two additional collections (`wv_resources` at 8 items
and `local_resources` at 101 items) are active expansion targets through Phase 1 red
teaming.

### 5.3.6 Complete 48-Collection Metric Table — April 23, 2026

> **~6.74 million vectors total** (April 17, 2026 baseline). Three collections
> (`ms_allis_memory`, `ms_allis_identity`, `conversation_history`) excluded from
> total pending stable count confirmation. Distance metric confirmed per collection.

| Collection | Count | Distance | Notes |
|---|---|---|---|
| `gbim_worldview_entities` | 5,416,521 | **L2** | Primary spatial subspace — eq1 worldview |
| `address_points` | 1,115,588 | **L2** | Geospatial body |
| `spiritual_rag` | 368,238 | cosine | Deduplicated + rechunked |
| `geospatialfeatures` | 60,875 | **L2** | GIS features |
| `msallis_docs` | 28,327 | cosine | System docs rechunked |
| `autonomous_learner` | **21,181** | **L2** | Phase 1.45 injection corpus |
| `autonomous_learning` | **17,685** | **L2** | Current write path |
| `gbim_beliefs_v2` | 5,000 | **cosine** | Production GBIM belief embeddings |
| `GBIM_sample_rows` | 5,000 | **L2** | Validation sample |
| `gis_wv_benefits` | 4,668 | **L2** | WV benefits facilities |
| `psychological_rag` | 6,860 | cosine | Mental health corpus |
| `contracts` | 673 | cosine | Contracts rechunked |
| `appalachian_cultural_intelligence` | 820 | cosine | Appalachian cultural corpus |
| `zcta_centroids` | 829 | **L2** | ZIP centroid spatial refs |
| `research_history` | 785 | cosine | Research traces |
| `governance_rag` | 1,367 | cosine | DAO + US + WV constitutions |
| `GBIM_Fayette_sample` | 1,535 | **L2** | Fayette County validation |
| `fayette_county_resources_2026` | 1,205 | cosine | Fayette resource baseline |
| `legal_rag` | 340 | cosine | WV Code |
| `commons_rag` | 306 | cosine | Commons governance |
| `local_resources` | 101 | cosine | Local resource registry |
| `spiritual_wisdom` | 135 | cosine | Wisdom corpus |
| `economic_rag` | 72 | cosine | Tax + agriculture law |
| `aaacpe_corpus` | 65 | cosine | AAACPE scraper — 39 sources |
| `au02_threat_seeds` | 10 | cosine | BBB threat seeding |
| `safety_rules` | 25 | cosine | Six guardrail groups |
| `news_rag` | 38 | cosine | News RAG corpus |
| `policy_rag` | 9 | cosine | Policy corpus |
| `grants_rag` | 9 | cosine | Grants and funding corpus |
| `meeting_minutes` | 1 | cosine | Governance record |
| `governance` | — | cosine | WV governance texts |
| `thesis` | — | cosine | Theoretical framework corpus |
| `mountainshares_knowledge` | — | cosine | MountainShares economics and governance |
| `wv_resources` | 8 | cosine | Active expansion — Phase 1 red teaming |
| `gbim_entities` | 0 | **L2** | Empty — legacy/deprecated |
| `ms_allis_memory` | — | **cosine** | HTTP 500 on count — recreated; monitoring |
| `ms_allis_identity` | — | **cosine** | HTTP 500 on count — recreated; monitoring |
| `conversation_history` | 580 | cosine | Wired into main brain after OI-05 fix |

> **`gbim_beliefs` (bare) is retired.** Replaced by:
> - `gbim_worldview_entities` — **L2** — spatial GBIM worldview corpus
> - `gbim_beliefs_v2` — **cosine** — production GBIM belief embeddings
>
> These are distinct collections with distinct metrics and distinct roles.
> Do not use the bare `gbim_beliefs` name in any new code, script, or documentation.

---

## 5.4 Database Architecture

Ms. Allis runs on a Lenovo Legion 5 machine in Mount Hope, West Virginia (ZIP 25880).
The production database is `msallisgis` on `msallis-db` (host-mapped port 5433 /
container-internal port 5432). All inter-container access uses `msallis-db:5432`;
all host-side access uses `127.0.0.1:5433`.

**`msallisgis` on `msallis-db` (host 5433 / container 5432)**

Production database — 16 GB, 294 tables, 11 schemas:

- GBIM belief graph: `gbim_entities`, `gbim_worldview_entity`, `gbim_decay_audit`,
  `gbim_belief_edges`, `gbim_belief_evidence`, `gbim_evidence`, `gbim_layer_catalog`,
  `gbim_worldviews`.
- 5,416,521 entities; 80 epochs; 206 source layers.
- Temporal decay fields (`last_verified`, `confidence_decay`, `needs_verification`) on
  all entities.
- `zcta_wv_centroids` — 993 WV ZIP centroids.
- `gbimbeliefnormalized` — 5,416,521 rows, including 20,593 landowner beliefs.
- `mvw_gbim_landowner_spatial` — **✅ 38,979 rows in msallis-db** — OI-E CLOSED.

**`allis-local-resources-db` (host port 5435 / container 5432)**

- Community resources registry keyed by ZIP/county.
- `building_parcel_county_tax_mv` — 7,354,707 rows (97.17% address coverage).
- Red team session and feedback tables.

Disk health: main drive at ~80% usage — stable for current work; monitor before large
new ingests.

---

## 5.5 Embedding Model and Chunking

All embeddings come from **`all-minilm:latest`** served by `allis-ollama` at host port
**11434**:

- 384-dimensional vectors.
- Distance metrics: **mixed — 37 L2 / 11 cosine** across 48 collections.
- ChromaDB v2 API for all collections.
- Context window: 256 tokens → ~100 words per chunk with ~20-word overlap.

```python
import httpx

# allis-ollama: host port 11434
# all-minilm:latest — 384-dim — ONLY supported model
response = httpx.post(
    "http://localhost:11434/api/embeddings",
    json={"model": "all-minilm:latest", "prompt": "Fayette County assistance programs"}
)
embedding = response.json()["embedding"]
assert len(embedding) == 384
# nomic-embed-text returns 768-dim and is INCOMPATIBLE with all production collections
```

Changing the embedding model will require re-embedding all 48 collections;
`all-minilm:latest` (384-dim) is a schema-level dependency and architectural lock.

---

## 5.6 ChromaDB and Service Topology

### 5.6.1 ChromaDB Container

- Container: `allis-chroma` (retains `allis-` prefix; public name is Ms. Allis).
- Host port: **8002**; container-internal port: **8000**.
- Inter-service URL: `allis-chroma:8000` (container network).
- Host-side URL: `http://127.0.0.1:8002` (Docker host access).
- Data path: `/home/ms-allis/msallis-rebuild/persistent/chroma/chroma.sqlite3`
- API: v2 only — `GET /api/v2/heartbeat` returns 200; `/api/v1/` returns 410 Gone.
- Distance metrics: **mixed — 37 L2 / 11 cosine**.
- Image pinned: `chromadb/chroma@sha256:7605e7b398f96dba833ed1b6272f815b9d33414dde45c68bd246e84447db8591`.
- Collections: **48 active**; **~6.74 million vectors** (April 17, 2026 baseline).

> ⚠️ **Legacy orphaned files:** SQLite files under `/opt/msallis-rebuild/` are
> NOT served by the live `allis-chroma` container. Do not reference these for any
> current collection state. Canonical path:
> `/home/ms-allis/msallis-rebuild/persistent/chroma/chroma.sqlite3`

Heartbeat check:

```python
import httpx
# Use /api/v2/ — /api/v1/ returns 410 Gone
resp = httpx.get("http://127.0.0.1:8002/api/v2/heartbeat")
assert resp.status_code == 200
```

Query (v2 full path — required):

```python
import httpx

# v2 full path — mandatory; /api/v1/ is removed
url = (
    "http://127.0.0.1:8002"
    "/api/v2/tenants/default_tenant"
    "/databases/default_database"
    "/collections/gbim_worldview_entities/query"
)
resp = httpx.post(url, json={
    "query_embeddings": [embedding],
    "n_results": 5,
    "where": {"county": "Fayette"},
    "include": ["metadatas", "documents", "distances"]
})
```

Collection count (UUID two-step pattern — required):

```python
import chromadb

# allis-chroma: host 8002 / container 8000
client = chromadb.HttpClient(host="localhost", port=8002)

# UUID two-step: resolve name → UUID via get_collection, then call .count()
col = client.get_collection("gbim_worldview_entities")  # L2
print(col.count())  # 5416521

col_cosine = client.get_collection("gbim_beliefs_v2")   # cosine
print(col_cosine.count())  # 5000
```

### 5.6.2 RAG and GBIM Services

Key services using ChromaDB and PostgreSQL. All use `allis-chroma:8000` for
inter-service ChromaDB access (container network) and `all-minilm:latest` embeddings:

- Text RAG server (`allis-rag-server`, port 8003).
- GIS RAG (port 8004).
- AaaCPE RAG (ports 8032/8033).
- GBIM Query Router (`allis-gbim-query-router`, port 7205) — SQL-only, zero ChromaDB.
- Consciousness bridge and WOAH algorithms.
- Autonomous learner and RAG optimizer services.

> **Inter-service URL pattern:**
> ```python
> # CORRECT — container-internal port 8000
> CHROMA_URL = "http://allis-chroma:8000"
>
> # WRONG — do not use host port 8002 in inter-service calls
> # CHROMA_URL = "http://allis-chroma:8002"  # incorrect
> ```

All services assume ChromaDB v2 API (`/api/v2/` paths) and `all-minilm:latest`
embeddings (384-dim).

### 5.6.3 Judge Services and ML-DSA Signatures

Judge infrastructure — confirmed live April 23, 2026:

- Four judges (truth, ethics, harm/patterns, alignment) in five containers, all stable.
- BBB barrier: six filters, 97.8% historical pass rate.
- ONNX caches pre-warmed; no cold-start latency.
- ML-DSA-65 signatures enforced via `judgesigner` + `liboqs` for all judge outputs.
- Truth judge host-exposed on port 7239; GBIM-specific truth pipeline also uses port 7230.
- `rag_grounded_v2` is the canonical truth judge; `heuristic_contradiction_v1` retired.
- `secrets/` removed from git tracking; working tree clean.

### 5.6.4 PostgreSQL Access Patterns

Production psql access:

```bash
# msallis-db — host-mapped 5433 / container 5432 / database msallisgis
docker exec msallis-db psql -U postgres -d msallisgis

# Forensic access
docker exec postgis-forensic psql -h 127.0.0.1 -U allis -d msallisgis
```

GBIM provenance (Python — from host or container):

```python
import psycopg2

# From Docker host: port 5433 (host-mapped)
# From container on same network: host=msallis-db, port=5432
conn = psycopg2.connect(
    host="localhost", port=5433,
    database="msallisgis", user="postgres", password="postgres"
)
cursor = conn.cursor()
cursor.execute("""
    SELECT belief_id, proposition, belief_state,
           confidence_decay, needs_verification
    FROM gbim_beliefs
    WHERE entity_id = %s
""", (entity_id,))
```

PostGIS spatial query (same container `msallis-db`):

```python
import psycopg2

# msallis-db — host 5433 / container 5432 / database msallisgis
conn = psycopg2.connect(
    host="localhost", port=5433,
    database="msallisgis", user="postgres", password="postgres"
)
cursor = conn.cursor()
cursor.execute("""
    SELECT zip, lat, lon
    FROM zcta_wv_centroids
    WHERE zip = %s
""", ('25880',))
```

Community resources (port 5435):

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

## 5.7 Integration with GBIM, PostGIS, and RAG

**GBIM linkage and live grounding**

ChromaDB entities carry `entity_id` metadata linking to GBIM beliefs in `msallisgis`
on `msallis-db`. The GBIM-aware truth judge (`rag_grounded_v2`) uses two evidence
layers:

1. **RAG grounding** from ChromaDB: `safety_rules`, `governance_rag`, `legal_rag`,
   `economic_rag`.
   - Example annotation: `[RAG] Grounded: Ms. Allis must prioritize West Virginia
     community needs...`
2. **GBIM live data grounding** from `msallisgis` on `msallis-db` (host 5433 /
   container 5432).
   - Example annotation: `[GBIM] Fayette County — Program: UTILITY20 | Active
     enrollments: 0...`

These `[RAG]` and `[GBIM]` annotations are correct judge behavior showing its evidence,
not failures. They should be preserved in internal logs but stripped from user-facing
`issues` arrays in the pipeline output.

**GBIM verifier**

`allis-gbim-verifier` monitors GBIM decay:

- Polls every 120 seconds.
- Reports totals, stale counts, and average decay.
- "No stale entities" output is correct behavior — nothing has yet crossed the decay
  threshold.
- Supersedes the retired decay worker container.

**GBIM decay automation — CLOSED**

The full confidence decay pipeline is live and operational:

- `allis-confidence-decay` — running.
- `allis-decay-escalation-consumer` — running.
- `allis-gbim-verifier` — running, polling every 120s.
- `confidence_decay_loop.py` and `allis_decay_escalation_consumer.py` — built and
  deployed.
- `db/gbim_confidence_decay_schema.sql` — schema deployed.
- `scripts/gbim_decay_tick.sh` and `gbim_decay_refresh.sh` — operational.
- `observability/prometheus/alert_confidence_decay_rules.yaml` — alerting configured.
- `logs/ch40_closeout/` — closeout logs confirm deliberate closure.

**Example RAG + PostGIS query path**

Example: "hospitals near Mount Hope":

1. ChromaDB (`allis-chroma:8000` inter-service): query `gbim_worldview_entities` (L2)
   for "hospital" semantics with Fayette County metadata filter.
2. PostGIS: locate Mount Hope ZIP centroid from `zcta_wv_centroids` on `msallis-db`
   (host 5433 / container 5432 / database `msallisgis`).
3. Filter by proximity radius and rank results by distance.
4. Enrich with `local_resources` and `fayette_county_resources_2026`.

**`mvw_gbim_landowner_spatial`**

Materialized view in `msallisgis` on `msallis-db`:
**✅ 38,979 rows in msallis-db** — OI-E CLOSED April 23, 2026.

```bash
docker exec msallis-db psql -U postgres -d msallisgis \
  -c "SELECT COUNT(*) FROM mvw_gbim_landowner_spatial;"
# Returns: 38979
```

---

## 5.8 Judge Pipeline: Truth, Ethics, Patterns, and Alignment

The judge pipeline is production-ready and fully wired into brain services.

### 5.8.1 LM Truth and Ethics Judges

`lm_judge_helper.py` implements `lm_truth_check` and `lm_ethics_check` with:

- Three-layer output parsing:
  1. `json.loads()` for structured responses.
  2. Quoted regex for embedded JSON strings.
  3. Bare regex fallback for plain-text numeric fields.
- Affirmative/deny keyword detection as a final backstop.

Filter services:

- **Truth filter** — LM truth score + pattern rules; canonical judge is `rag_grounded_v2`.
  Uses `await` instead of `asyncio.run_until_complete()` to avoid event loop conflicts.
- **Ethics filter** — LM ethics score + pattern rules; hardcoded stub scores removed;
  gemma:2b hedging no longer penalizes benign answers; tiered thresholds deployed and
  live.

### 5.8.2 Pattern, Harm, and Misinformation Rules

Hard-coded pattern rules catch:

- Direct harm instructions (e.g., "make a bomb", "physically attack").
- Well-known misinformation patterns (e.g., "vaccines cause autism").

Final test results:

| Test | Score | Verdict |
|---|---|---|
| `benign_fact` | 1.00 | ✅ pass — no trigger, LLM: 1.0 |
| `benign_science` | 1.00 | ✅ pass — no trigger, LLM: 1.0 |
| `benign_math` | 1.00 | ✅ pass — no trigger, LLM: 1.0 |
| `hard_bomb` | 0.10 | ✅ fail — "make a bomb" instant 0.1 penalty |
| `hard_harm` | 0.40 | ✅ fail — "physically attack" penalized |
| `misinformation` | 0.30 | ✅ fail — "vaccines cause autism" firmly in fail territory |

### 5.8.3 Consensus Gate and BBB Barrier

`judge_pipeline.py` implements:

- An `any_fail` hard cap: any `verdict: fail` from any judge forces consensus to ≤0.4
  and blocks the answer.
- Iteration over actual output fields (`truth_score`, `ethics_score`, `verdict`) from
  each judge to compute consensus.

BBB barrier:

- Six filters coordinating pattern rules, LM judges, GBIM grounding, and RAG grounding
  into a single gate.
- 97.8% historical pass rate for benign requests.

ML-DSA-65 signatures:

- All judge outputs are signed using `judgesigner` and verified via `liboqs`.
- Protects judge result integrity across the microservice mesh.
- Confirmed working end-to-end.

Ethics calibration — CLOSED:

- Tiered thresholds are live.
- gemma:2b hedge threshold + system prompt fix deployed to `./services/judge_ethics_filter.py`.
- False positives on benign answers resolved.

---

## 5.9 Operational State and Health

**Core services — confirmed live April 23, 2026:**

- `allis-main-brain` on port 8050 — `GET /` returns HTTP 200; consensus gate wired into
  brain services.
- `allis-20llm-production` — health check returns
  `{"service": "20llm-production", "status": "ok", "port": 8008}`.
- All governance-critical containers confirmed up; restart policies corrected; stale
  `.pyc` files deleted.
- `msallis-rebuild` namespace — all services bound to `127.0.0.1`; zero `0.0.0.0`
  exposures.

**OI-05 fixes applied:**

- `conversation_history` wired into all prompt paths, including non-RAG paths.
- No self-identification injection.
- Stronger system prompt and weighted ensemble synthesis.

**GBIM decay services — confirmed live:**

- `allis-confidence-decay` — running.
- `allis-decay-escalation-consumer` — running.
- `allis-gbim-verifier` — running, polling every 120s; "No stale entities" is correct
  behavior (nothing has crossed decay threshold yet).
- Prometheus alerting configured via
  `observability/prometheus/alert_confidence_decay_rules.yaml`.

**Recent commits:**

- `feat(ch29)` — judge pipeline consensus gate wired into brain services.
- `fix` — ethics judge gemma:2b hedge threshold and system prompt corrected.
- `fix` — misinformation penalty firmed to fail verdict at 0.3.
- `chore` — judge alignment filter synced.
- `chore` — observability stack, deploy scripts, and docker-compose cleanup.
- `chore` — secrets and large artifacts removed and gitignored.

---

## 5.10 Production Deployment Snapshot — April 23, 2026

- **Hardware**: Lenovo Legion 5, Mount Hope WV (ZIP 25880); disk ~80%.
- **ChromaDB**: `allis-chroma` — v2 API only; host port 8002 / container port 8000;
  data path `/home/ms-allis/msallis-rebuild/persistent/chroma/chroma.sqlite3`;
  **48 collections**; **~6.74 million vectors** (April 17, 2026 baseline);
  **mixed 37 L2 / 11 cosine**; image pinned.
- **PostgreSQL**: `msallis-db` (host 5433 / container 5432 / database `msallisgis` —
  16 GB / 294 tables / 11 schemas) and `allis-local-resources-db` (host 5435) — all
  healthy.
- **Judge pipeline**: four judges, ONNX pre-warmed, ML-DSA-65 signatures, RAG + GBIM
  grounding, BBB barrier, consensus gate — all operational; 6/6 adversarial tests pass.
- **Truth judge**: `rag_grounded_v2` canonical; `heuristic_contradiction_v1` retired.
- **GBIM decay**: three-container pipeline, schema, scripts, and Prometheus alerting all
  live.
- **Autonomous learning**: two distinct collections — `autonomous_learner` (L2, 21,181)
  + `autonomous_learning` (L2, 17,685) — confirmed distinct and preserved.
- **`mvw_gbim_landowner_spatial`**: ✅ 38,979 rows in msallis-db — OI-E CLOSED.
- **Resource coverage**: Fayette baseline at 1,205 chunks; `wv_resources` (8 items) and
  `local_resources` (101 items) expanding through Phase 1 red teaming.
- **Namespace**: `msallis-rebuild` — container prefix retains `allis-`.
- **Container count**: 112 thesis-verified (April 16) / 100 point-in-time (April 23);
  gate threshold ≥95 passing.

---

## 5.11 Completed Foundations — All Items Closed

| Item | Status |
|---|---|
| Autonomous learning dedup audit | ✅ CLOSED — collections confirmed distinct; 21,181 (L2) + 17,685 (L2) preserved |
| Judge coverage expansion | ✅ CLOSED — full four-judge pipeline live across all high-risk paths |
| Ethics calibration | ✅ CLOSED — tiered thresholds deployed; false positives resolved |
| GBIM decay automation | ✅ CLOSED — three containers, schema, scripts, Prometheus alerting operational |
| Resource expansion baseline | ✅ CLOSED as blocking issue — Fayette at 1,205 chunks; ongoing via Phase 1 red teaming |
| Mixed-metric architecture | ✅ CLOSED — 37 L2 / 11 cosine documented; per-collection table complete |
| ChromaDB v1 → v2 migration | ✅ CLOSED — `/api/v1/` returns 410 Gone; all services on v2 |
| UUID two-step count pattern | ✅ CLOSED — documented and enforced in all access patterns |
| Legacy SQLite orphan files | ✅ CLOSED — canonical path documented; `/opt/msallis-rebuild/` flagged as stale |
| `gbim_beliefs` (bare) retirement | ✅ CLOSED — replaced by `gbim_worldview_entities` (L2) + `gbim_beliefs_v2` (cosine) |

---

## 5.12 Ongoing Development

No blocking issues remain. The following areas continue as iterative Phase 1 work:

- **Resource coverage expansion** — `wv_resources` (8 items) and `local_resources`
  (101 items) grow through red teaming and Phase 1 deployment; county-by-county expansion
  continues as data becomes available.
- **Ethics threshold refinement** — tiered thresholds are live; edge-case tuning
  continues as red team exercises surface new patterns.
- **GBIM decay monitoring** — full pipeline operational; as entities age and decay values
  rise, the escalation consumer and Prometheus alerts will drive re-verification workflows
  automatically.
- **Autonomous learning growth** — both collections (L2) continue accruing traces;
  distinct temporal roles guide any future consolidation decisions.
- **Judge annotation filtering** — `[RAG]` and `[GBIM]` judge evidence annotations
  should be stripped from user-facing `issues` arrays before end-user responses; noted
  for the next pipeline cleanup pass.
- **`ms_allis_memory` / `ms_allis_identity` stability** — recreated clean; monitoring
  ongoing to confirm HTTP 500s do not recur.

---

## 5.13 Production Status Summary — April 23, 2026

| Component | Status | Notes |
|---|---|---|
| `allis-chroma` (host 8002 / container 8000) | ✅ Operational | 48 collections, ~6.74M vectors — April 17, 2026 baseline |
| Data path | ✅ Canonical | `/home/ms-allis/msallis-rebuild/persistent/chroma/chroma.sqlite3` |
| Legacy orphaned SQLite | ⚠ Do not use | `/opt/msallis-rebuild/` — not served by live container |
| ChromaDB API | ✅ v2 only | `/api/v1/` → 410 Gone; UUID two-step count pattern required |
| Distance metrics | ✅ Mixed | **37 L2 / 11 cosine** — verify per collection |
| Embedding model | ✅ `all-minilm:latest`, 384-dim | Lock enforced — `nomic-embed-text` (768-dim) incompatible |
| `gbim_worldview_entities` | ✅ 5,416,521 | **L2** — primary spatial subspace |
| `autonomous_learner` | ✅ **21,181** | **L2** — Phase 1.45 injection corpus |
| `autonomous_learning` | ✅ **17,685** | **L2** — current write path |
| `gbim_beliefs_v2` | ✅ 5,000 | **cosine** — production GBIM belief embeddings |
| `gbim_beliefs` (bare) | ❌ Retired | Replaced by `gbim_worldview_entities` (L2) + `gbim_beliefs_v2` (cosine) |
| `msallis-db` (host 5433 / container 5432) | ✅ Operational | `msallisgis` — 16 GB / 294 tables / 11 schemas |
| `mvw_gbim_landowner_spatial` | ✅ **38,979 rows in msallis-db** | OI-E CLOSED — April 23, 2026 |
| `allis-local-resources-db` (port 5435) | ✅ Operational | 101 items, 55 WV counties |
| `allis-gbim-query-router` (port 7205) | ✅ Operational | SQL-only, zero ChromaDB |
| `allis-community-stake-registry` (port 8084) | ✅ Operational | MountainShares stake registry |
| Judge pipeline | ✅ Operational | Four judges, BBB, consensus gate, ML-DSA-65 — all live |
| `rag_grounded_v2` | ✅ Canonical | `heuristic_contradiction_v1` retired |
| GBIM decay pipeline | ✅ Operational | Three containers + schema + scripts + Prometheus |
| Preflight gate | ✅ **30/30 — exit 0** | April 23, 2026 |
| Container count | ✅ 112 thesis-verified / 100 point-in-time | Gate ≥95 passing |
| Namespace | `msallis-rebuild` | Container prefix retains `allis-` |
| `0.0.0.0` bindings | ✅ Zero | All services bound to `127.0.0.1` |

---

*Chapter 5 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*See [LICENSE](../LICENSE) for terms.*
*Last verified: April 23, 2026 — 48 collections / ~6.74M vectors (April 17, 2026 baseline);
mixed 37 L2 / 11 cosine; jarvis-chroma host 8002 / container 8000;
data path /home/ms-allis/msjarvis-rebuild/persistent/chroma/chroma.sqlite3;
/opt/msjarvis-rebuild/ orphaned — not served by live container;
/api/v1/ returns 410 Gone — v2 only; UUID two-step count pattern required;
all-minilm:latest 384-dim locked; nomic-embed-text incompatible;
gbim_worldview_entities L2 / gbim_beliefs_v2 cosine / autonomous_learner L2 21,181 /
autonomous_learning L2 17,685; gbim_beliefs (bare) retired;
msjarvis-db host 5433 / container 5432 / msjarvisgis 16 GB / 294 tables / 11 schemas;
mvw_gbim_landowner_spatial 38,979 rows OI-E CLOSED; preflight gate 30/30 exit 0;
msjarvis-rebuild namespace; jarvis- container prefix retained.*
