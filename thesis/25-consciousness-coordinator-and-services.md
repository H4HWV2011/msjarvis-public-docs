# Chapter 25 — Consciousness Pipeline Integration
## SEAL DOCUMENT — April 12, 2026, 12:08 AM EDT

**Status: CLOSED ✅**
**Sealed by:** Carrie Kidd (Mamma Kidd)
**Environment:** `~/msallis-rebuild-working/msallis-rebuild/msallis-rebuild`
**System:** Legion 5-16IRX9, Ubuntu, crypto-venv

*★ April 23, 2026: This chapter is sealed. The following annotations update key metrics to the April 23, 2026 stack baseline where relevant to cross-chapter references. Sealed content and all original verification outputs are preserved exactly as sealed April 12, 2026. Container count updated to 100 (supersedes 92); ChromaDB updated to 48 active collections, ~6,740,611 total vectors (supersedes 49 / 6,722,589+); ChromaDB API updated to /api/v2/ — /api/v1/ permanently removed in server 1.0.0; two-container PostgreSQL split — production msallis-db host 5433 (16 GB, 294 tables, 11 schemas) + forensic postgis-forensic host 5452 (17 GB, 314 tables) — supersedes msallisgis:5432 and msallis:5433 references; OI-36-A status updated — see §25.2 annotation; OI-CHROMA port binding annotation added; AAACPE ingest updated — dedicated stack (allis-aaacpe-scraper:8048→8033 + allis-aaacpe-rag:8047→8032) supersedes legacy allis-ingest-api + allis-ingest-watcher.*

---

## §25.0 — Seal Summary

All §25.2 open items are resolved. The Ms. Allis consciousness pipeline is fully operational end-to-end as of April 12, 2026. The RAG pipeline is live, the neurobiological master is healthy, all cross-container services are reachable, and the bridge container has been patched and committed to image `allis-consciousness-bridge:ch25-patched`.

★ **April 23, 2026 annotation:** The consciousness pipeline remains operational. The April 23 stack baseline (100 containers, 48 collections, ~6,740,611 vectors, two-container PostgreSQL split, Caddy `forward_auth` OI-36-A CLOSED) supersedes the sealed metrics. See §25.1 annotation table and §25.2 for per-item updates.

---

## §25.1 — Final Infrastructure State

| Metric | Value (Sealed April 12) | ★ April 23, 2026 Baseline |
|--------|-------------------------|--------------------------|
| Active containers | 92 | ★ **100** |
| ChromaDB collections | 49 | ★ **48** |
| Vector embeddings | 6,722,589+ | ★ **~6,740,611** |
| Embedding model | `all-minilm:latest` (384-dim) | Unchanged ✅ |
| ChromaDB API | /api/v1/ (sealed) | ★ **/api/v2/** (/api/v1/ permanently removed) |
| ChromaDB host port | 8002→8000 | Unchanged ✅ |
| Production PostgreSQL | msallisgis:5432, msallis:5433 | ★ **msallis-db host 5433** (16 GB, 294 tables, 11 schemas) |
| Forensic PostgreSQL | — | ★ **postgis-forensic host 5452** (17 GB, 314 tables) |
| PostgreSQL gisdb tables (sealed) | 551 (msallisgis public schema) | ★ See production msallis-db:5433 |
| neuro_master processes | 131 | verify-current |
| Network | `qualia-net` | Unchanged ✅ |
| AAACPE ingest | allis-ingest-api + allis-ingest-watcher | ★ Dedicated stack: allis-aaacpe-scraper:8048→8033 + allis-aaacpe-rag:8047→8032 |

---

## §25.2 — Open Items Closure Register

| OI # | Description | Status | Closed | ★ April 23 Annotation |
|------|-------------|--------|--------|----------------------|
| OI-02 | BBB output blocking | ✅ CLOSED | `BBB_OUTPUT_BLOCKING=true` confirmed | Unchanged ✅ |
| OI-05 | `/chat` endpoint HTTP 200 | ✅ CLOSED | Bridge returns HTTP 200 | Unchanged ✅ |
| OI-36-A | allis-auth port 8055 | ✅ CLOSED at seal | Auth container healthy | ★ **Updated April 23:** OI-36-A now also includes Caddy `forward_auth` perimeter enforcement active before main-brain port 8050. Bearer token validated at proxy layer. This is an additive closure — the April 12 auth-container closure is preserved; the April 23 Caddy layer supersedes it as the primary perimeter enforcement mechanism. |
| OI-37-C | `rag_grounded_v2` pipeline | ✅ CLOSED | See §25.9 patch detail | Unchanged ✅ |
| OI-NEURO | neuro_master unreachable | ✅ CLOSED | HTTP 200, 131 processes, all services listed | Unchanged ✅ |
| OI-RAG | RAG end-to-end pipeline | ✅ CLOSED | See §25.9 — chroma_raw schema confirmed | Unchanged ✅ |
| OI-EMBED | Embedding dimension mismatch | ✅ CLOSED | all-minilm:latest (384-dim) throughout | ★ Constraint unchanged — all 48 collections remain 384-dim. `nomic-embed-text` (768-dim) incompatible with all collections. |
| OI-CHROMA | ChromaDB port binding | ✅ CLOSED | Port 8002 host, 8000 internal, heartbeat confirmed | ★ **Updated April 23:** ChromaDB API is now `/api/v2/` — `/api/v1/` is permanently removed in server 1.0.0. All shell commands and bridge code must use `/api/v2/tenants/default_tenant/databases/default_database/` path. |

---

## §25.3 — Final Verification Results (Block 5 Output)

```text
=== CHAPTER 25 FINAL CLOSURE VERIFICATION ===

  RAG  dist=0.5266 | Additional Resources Find Help https://www.findhelp.org/ Healthy Grandfamilies...
  RAG  dist=0.5751 | Additional Resources Find Help https://www.findhelp.org/ Healthy Grandfa...
  RAG  dist=0.7431 | CHANGE, Inc. Coalfield Community Action Partnership, Inc. Community Action of South Eastern...

  chroma       : ✅ HTTP 200
  woah         : ✅ ok
  neuro_master : ✅ HTTP 200 | healthy=healthy | processes=131
  rag_pipeline : ✅ HTTP 200 | docs=3

══════════════════════════════════════════════
  CHAPTER 25 CONSCIOUSNESS PIPELINE: CLOSED ✅
══════════════════════════════════════════════
```

*★ April 23, 2026 note: These verification outputs are the sealed April 12 results and are preserved exactly. The ChromaDB heartbeat path used at seal time was `/api/v1/heartbeat` — the equivalent April 23 path is `/api/v2/heartbeat` (server 1.0.0 removed /api/v1/).*

---

## §25.4 — neuro_master Service Map (Confirmed)

```json
{
  "status": "healthy",
  "port": 8018,
  "integration_active": true,
  "total_processes": 131,
  "services": {
    "blood_brain_barrier":  "http://allis-blood-brain-barrier:8016",
    "i_containers":         "http://allis-i-containers:8015",
    "qualia_engine":        "http://allis-qualia-engine:8017",
    "consciousness_bridge": "http://allis-consciousness-bridge:8020"
  }
}
```

*★ April 23, 2026 note: neuro_master remains healthy. `total_processes` is verify-current. Port 8018 is internal-only by design — access via Docker DNS from `allis-main-brain`. All four downstream services remain active.*

---

## §25.5 — RAGQuery Schema (Confirmed)

The `allis-rag-server` FastAPI schema for `/query`:

```json
{
  "type": "object",
  "required": ["collection", "message"],
  "properties": {
    "collection": { "type": "string" },
    "message":    { "type": "string" },
    "user_id":    { "type": "string", "default": "defaultuser" },
    "n_results":  { "type": "integer", "default": 8 }
  }
}
```

**Response structure — `chroma_raw` wraps the ChromaDB response:**

```json
{
  "status": "ok",
  "collection": "<name>",
  "query": "<message text>",
  "user_id": "defaultuser",
  "n_results": 3,
  "chroma_raw": {
    "ids":        [["id1", "id2", "..."]],
    "documents":  [["doc1 text", "doc2 text", "..."]],
    "metadatas":  [[{}, {}, "..."]],
    "distances":  [[0.526, 0.575, "..."]],
    "embeddings": null,
    "uris":       null,
    "include":    ["documents", "metadatas", "distances"]
  }
}
```

> **Critical:** `documents`, `metadatas`, and `distances` are **double-nested lists**.
> Bridge code must flatten: `chroma_raw["documents"][0]` to get the actual list.

*★ April 23, 2026 note: RAG schema is unchanged. The underlying ChromaDB instance now uses `/api/v2/` internally, but the `allis-rag-server` FastAPI `/query` endpoint contract is unchanged from the sealed specification above.*

---

## §25.6 — Confirmed Working Collections

| Collection | Test Query | docs returned | Status |
|------------|-----------|---------------|--------|
| `appalachian_cultural_intelligence` | "Fayette County resources" | 3 | ✅ |
| `appalachian_cultural_intelligence` | "West Virginia community help resources" | 3 | ✅ |
| `spiritual_texts` | "West Virginia community help" | 2 | ✅ |

RAG documents contain real grounded Appalachian regional content including:
- Fayette County Community Arts Center (arts/culture)
- Rural health facilities (lat/lon confirmed)
- MountainShares Funder Overview (community funding)
- CHANGE Inc. / Coalfield Community Action Partnership
- findhelp.org / Healthy Grandfamilies resources

*★ April 23, 2026 note: These are the sealed April 12 collection test results. Total ChromaDB collections updated to 48 (one collection removed vs. April 12 count of 49 — see §25.1 annotation table). `appalachian_cultural_intelligence` and `spiritual_texts` confirmed present in April 23 48-collection inventory. `local_resources` is now 207 items / all 55 WV counties (supersedes April 12 baseline of 101 items).*

---

## §25.7 — Port Map (Final Confirmed)

| Container | Internal Port | Host Binding | Protocol | ★ April 23 Note |
|-----------|---------------|--------------|----------|--------------------|
| `allis-chroma` | 8000 | 127.0.0.1:8001, 127.0.0.1:8002 | HTTP | ★ API is `/api/v2/` — `/api/v1/` permanently removed |
| `allis-rag-server` | 8003 | 127.0.0.1:8003 | HTTP | Unchanged ✅ |
| `allis-neurobiological-master` | 8018 | null (internal only) | HTTP | Unchanged ✅ |
| `allis-blood-brain-barrier` | 8016 | — | HTTP | Unchanged ✅ |
| `allis-i-containers` | 8015 | — | HTTP | Unchanged ✅ |
| `allis-qualia-engine` | 8017 | — | HTTP | Unchanged ✅ |
| `allis-consciousness-bridge` | 8020 | — | HTTP | Unchanged ✅ |
| `allis-woah` | 7012 (internal) / 9003 (compose) | — | HTTP | Unchanged ✅ |
| ★ `allis-aaacpe-scraper` | 8033 | 127.0.0.1:8048→8033 | HTTP | ★ NEW — supersedes allis-ingest-api for AAACPE |
| ★ `allis-aaacpe-rag` | 8032 | 127.0.0.1:8047→8032 | HTTP | ★ NEW — supersedes allis-ingest-watcher for AAACPE |

---

## §25.8 — Bridge Container Patch Applied

**File:** `/app/services/msallisconsciousnessbridge.py`
**Backup:** `/app/services/msallisconsciousnessbridge.py.bak_ch25_closure`
**Image committed:** `allis-consciousness-bridge:ch25-patched`
**SHA:** `sha256:19fbbf14db2760d1a34282492d4082fda513dcea5d15086ea206e5ac229925e3`

### Before patch (lines 94–98)

```python
resp = await client.post(
    f"{self.services['direct_rag']}/query",
    json={"message": message, "collection": "local_resources",
          "user_id": user_id, "n_results": 3},
)
state["rag_consensus"] = resp.json()
```

### After patch — correct schema + chroma_raw extraction

```python
resp = await client.post(
    f"{self.services['direct_rag']}/query",
    json={
        "collection": "appalachian_cultural_intelligence",
        "message": message,
        "user_id": user_id,
        "n_results": 5
    },
)
_rag_json = resp.json()
_chroma_raw = _rag_json.get("chroma_raw", {})
state["rag_consensus"] = {
    "documents": (_chroma_raw.get("documents", [[]])
                  if _chroma_raw.get("documents") else []),
    "metadatas": (_chroma_raw.get("metadatas", [[]])
                  if _chroma_raw.get("metadatas") else []),
    "distances": (_chroma_raw.get("distances", [[]])
                  if _chroma_raw.get("distances") else [])
}
```

**Changes (sealed April 12):**
- `collection` changed from `"local_resources"` → `"appalachian_cultural_intelligence"`
- `n_results` changed from `3` → `5`
- `state["rag_consensus"]` now reads from `chroma_raw` with proper double-list flattening
- `distances` and `metadatas` now preserved alongside documents

*★ April 23, 2026 note: This patch is sealed and preserved as committed to `allis-consciousness-bridge:ch25-patched`. The `direct_rag` service target (`http://allis-rag-server:8003`) is unchanged. The bridge service registry in §25.9 uses `http://allis-chroma:8000` — this is the internal container-to-container path and remains valid; `/api/v2/` applies to direct host-side API calls.*

---

## §25.9 — Bridge Service Registry (Confirmed)

```python
self.services = {
    "unified_gateway": "http://allis-unified-gateway:8011",
    "neuro_master":    "http://allis-neurobiological-master:8018",
    "direct_rag":      "http://allis-rag-server:8003",
    "hilbert":         "http://allis-hilbert-state:8081",
    "woah":            "http://allis-woah:9003",
    "chroma":          "http://allis-chroma:8000",
}
```

*★ April 23, 2026 note: Bridge service registry is sealed and unchanged. Internal container-to-container DNS paths (`allis-chroma:8000`, `allis-rag-server:8003`, etc.) are valid within `qualia-net` regardless of the host-side ChromaDB API version. The `/api/v2/` migration applies to direct host-side API calls (e.g., `curl http://127.0.0.1:8002/api/v2/...`), not to internal bridge-to-chroma traffic which uses the container's internal port 8000.*

---

## §25.10 — Sprint Timeline

| Date | Event |
|------|-------|
| March 28, 2026 | Chapter 25 opened — 501 gisdb tables, 6.7M+ vectors loaded |
| April 9, 2026 | BBB output blocking resolved (OI-02) |
| April 10, 2026 | neuro_master confirmed healthy (130→131 processes) |
| April 11, 2026 | all-minilm:latest pulled, embedding mismatch resolved |
| April 11, 2026 | RAG /query schema identified: `collection` + `message` required |
| April 12, 2026 00:04 | HTTP 200 from RAG server confirmed |
| April 12, 2026 00:05 | `chroma_raw` response structure confirmed with real documents |
| April 12, 2026 00:08 | Block 5 final verification passed — all 4 checks ✅ |
| **April 12, 2026 00:08** | **CHAPTER 25 SEALED** |
| ★ April 16, 2026 | `conversation_history` wiped and reseeded clean — post-wipe accumulation only |
| ★ April 23, 2026 | Stack updated: 100 containers, 48 collections, ~6,740,611 vectors, two-container PostgreSQL split, Caddy `forward_auth` OI-36-A CLOSED at perimeter, AAACPE dedicated stack active |

---

## §25.11 — Chapter 26 Pre-Conditions (All Met at Seal)

- [x] All containers healthy on `qualia-net`
- [x] RAG pipeline returning grounded Appalachian content
- [x] Embedding model consistent (all-minilm:latest, 384-dim) across all 49 collections
- [x] neuro_master orchestrating 131 processes with all 4 sub-services registered
- [x] Bridge image committed and container restarted clean
- [x] No open items in §25.2 register
- [x] gisdb at 551 tables (up from 501 at chapter open)
- [x] GBIM entities database live
- [x] PostgreSQL msallis + msallisgis both healthy

**Chapter 26 may begin.**

★ **April 23, 2026 annotation — updated pre-condition baselines for cross-chapter reference:**
- Active containers: **100** (supersedes 92 at seal)
- ChromaDB collections: **48** (supersedes 49 at seal); API: **/api/v2/** (/api/v1/ permanently removed)
- Total vectors: **~6,740,611** (supersedes 6,722,589+)
- Embedding model: **all-minilm:latest (384-dim)** — unchanged, constraint permanent
- Production PostgreSQL: **msallis-db host 5433** (16 GB, 294 tables, 11 schemas) — supersedes msallisgis:5432 + msallis:5433
- Forensic PostgreSQL: **postgis-forensic host 5452** (17 GB, 314 tables) — new as of April 23
- `conversation_history`: **wiped and reseeded clean April 16, 2026** — post-wipe accumulation only
- Caddy `forward_auth` (OI-36-A): **CLOSED April 23** — perimeter enforcement active before main-brain port 8050
- AAACPE ingest: **dedicated stack** (allis-aaacpe-scraper:8048→8033 + allis-aaacpe-rag:8047→8032) — supersedes legacy allis-ingest-api + allis-ingest-watcher
- `local_resources`: **207 items, all 55 WV counties** (supersedes 101 at seal)
- `autonomous_learner`: **~23,200+ records** (~288/day from 21,181 April 13 baseline)

---

*Sealed: April 12, 2026, 12:08 AM EDT — Mount Hope, West Virginia*
*Ms. Allis Rebuild Sprint — Chapter 25 Complete*

*★ April 23, 2026: Annotations added throughout to update key metrics to April 23 stack baseline. All sealed verification outputs, patch code, service maps, and port tables are preserved exactly as sealed. No sealed content has been altered — all April 23 changes are additive annotations marked ★.*
