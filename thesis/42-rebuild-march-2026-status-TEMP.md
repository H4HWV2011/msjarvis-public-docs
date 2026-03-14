# Chapter 42 — Rebuild Status: March 2026 (TEMPORARY — DELETE WHEN CH39/40/41 UPDATED)

> **⚠️ This chapter is a temporary working document.**
> It captures the real-world wiring state of the Ms. Jarvis `msjarvis-rebuild` stack as of March 13, 2026.
> Once chapters 39, 40, and 41 are updated to reflect this status, this file should be deleted.

---

## Context

The `msjarvis-rebuild` stack is a clean Docker Compose rebuild of the full Ms. Jarvis architecture,
run from `/home/cakidd/msjarvis-rebuild-working/msjarvis-rebuild/` on the development machine
(Legion 5 16IRX9, Oak Hill WV). This document captures what is wired, what is degraded, and what
is not yet running as of the March 13 2026 session.

---

## Current Service Wiring Status

| Service | Container Name | Port | Status | Glassbox Visible | Notes |
|---|---|---|---|---|---|
| Unified Gateway | jarvis-unified-gateway | 18018 | ✅ Running | ✅ BBB + pipeline | TEMP echo `/chat` handler active; `consciousness` block is stub `{"error":""}` |
| Blood-Brain Barrier | jarvis-blood-brain-barrier | active | ✅ Running | ✅ | 0 blocks, 100% pass rate |
| Consciousness Bridge | jarvis-consciousness-bridge | 8020 | ✅ Running | ❌ Not surfaced in glassbox | Returns valid JSON; processes in ~120s; unified gateway not yet calling it |
| Hilbert WV Gateway | jarvis-hilbert-gateway | 8010 | ✅ Running | ❌ Timeout error string | `/chat_wv` times out at 120s; `/wv_summary` fast path not yet implemented |
| WOAH | jarvis-woah | 7012 | ✅ Running | ❌ Not surfaced | WOAH reasoning available from bridge; not yet in unified glassbox |
| Ollama | jarvis-ollama | active | ✅ Running | N/A | LLM backend |
| Redis | jarvis-redis | active | ✅ Running | N/A | Cache layer |
| ChromaDB (HTTP) | host-system process | 8002 | ✅ Running | ✅ | Live at 127.0.0.1:8002; full GBIM ingest running as of 2026-03-13 evening |
| Direct RAG | jarvis-direct-rag | 8199 | ❌ DNS Fail | ❌ | `[Errno -2] Name or service not known` inside Docker network; container DNS not resolving |
| Neurobiological Master | jarvis-neurobiological-master | 8018 | ⚠️ 405 on health | ❌ | HTTP method mismatch on health endpoint |
| 20-LLM Production | jarvis-20llm-production | 8008 | ❌ Not running | ❌ | Not yet in rebuild compose file; required by `/chat_wv` full path |

---

## Glassbox Contract (as designed, not yet fully wired)

Every `/chat` call to the unified gateway (18018) should produce a `pipeline` block containing:

```json
{
  "query": "...",
  "user_id": "...",
  "bbb": { "...BBB filter result..." },
  "consciousness": {
    "status": "success",
    "message": "Consciousness bridge processed in Xs",
    "services_used": ["unified_gateway","neuro_master","direct_rag","hilbert","woah"],
    "consciousness_state": {
      "user_profile": { "user_id": "...", "display_name": "...", "role": "..." },
      "chromadb_context": "Chroma health: 200",
      "rag_consensus": { "...RAG result..." },
      "hilbert_spatial": {
        "status": "ok",
        "used_wv_entangled_context": true,
        "gbim_entities": 3,
        "local_resources_rows": 0,
        "msjarvisgis_rag_hits": 0
      },
      "woah_reasoning": { "...WOAH result..." }
    },
    "timestamp": "..."
  }
}
```

Currently, only `bbb` is populated. `consciousness` is `{"error":""}`.

---

## What Happened Today (March 13, 2026 — Daytime Session)

1. `msjarvisconsciousnessbridge.py` timeout raised from 45s → 120s (Hilbert `/chat_wv` takes ~120s).
2. Bridge container rebuilt and confirmed returning valid JSON at port 8020.
3. Unified gateway currently running TEMP echo handler (not calling bridge).
4. Attempts to patch `ms_jarvis_unified_gateway.py` to call bridge failed due to file name mismatch (`ms_jarvis_web_research_simple.py` does not exist in rebuild).
5. Confirmed active gateway file is `services/ms_jarvis_unified_gateway.py`.
6. `recovered-services/services/ms_jarvis_unified_gateway.py` has the real `process_unified` implementation that calls the consciousness bridge — needs to be copied and validated.
7. Hilbert `/chat_wv` times out because it calls `jarvis-20llm-production:8008` which is not running in rebuild stack.
8. Plan: add `/wv_summary` fast path to `jarvis-wv-entangled-gateway` that returns WV context metadata without calling 20-LLM.

---

## GBIM Chroma Restoration Session (March 13, 2026 — Evening)

### Background
Working directory for this session:
```
~/msjarvis-safe/recovered-services_20llm_full/
```
Virtual environment: `~/msjarvis-venvs/chroma_venv/`

### ChromaDB Server Confirmed Live
The host-system ChromaDB HTTP server at `127.0.0.1:8002` was confirmed running with 10 collections accessible.

### Active Collections (Verified 2026-03-13 ~21:00 EDT)

| Collection | Domain |
|---|---|
| `msjarvis-smoke` | Smoke test |
| `GBIM_sample_rows` | GBIM testing sample (5,000 rows) |
| `GBIM_Fayette_sample` | Fayette County GBIM sample |
| `spiritual_texts` | Spiritual and values corpus |
| `psychological_rag` | Psychological safety corpus |
| `geospatialfeatures` | GIS feature embeddings |
| `GBIM_sample` | General GBIM sample |
| `gbim_worldview_entities` | GBIM spatial worldview — **full 5.4M ingest running** |
| `autonomous_learner` | Autonomous learning patterns |
| `msjarvis_docs` | System documentation |

### Legacy Archive Located
The prior ChromaDB on-disk store was found at:
```
/mnt/nvme1/msjarvis-rebuild/chroma_db
```
This is on the second NVMe drive (`/dev/nvme1n1p1`, mounted at `/mnt/nvme1`).
**Status: read-only historical archive. Do not write to this path.**
All active ingest targets the HTTP server at `127.0.0.1:8002`.

### Second NVMe Contents
`/mnt/nvme1/` contains three directories:
- `gbim_data/` — GBIM source data
- `msjarvis-data/` — Ms. Jarvis data assets
- `msjarvis-rebuild/` — prior rebuild artifacts (includes legacy `chroma_db/`)

### Full GBIM Ingest Launched
A full ingest of all 5.4M+ GBIM worldview entities was launched into `gbim_worldview_entities`.
Source file:
```
data/gbim/gbim_entities_for_chroma.csv
```
Batch size: 5,400. Progress confirmed with first batch log: `Added 5400 GBIM entities`.
Ingest is **running as background process** and is expected to take several hours.

The ingest script uses `col.add()` with id-based upsert — safe to re-run if interrupted.
Each document text is constructed as:
```
{entity_type} {source_table} {label}
```
with all non-empty CSV fields included as metadata (values truncated to 500 chars).

### Significance for Thesis
This session demonstrates end-to-end GBIM semantic memory restoration:
- Live ChromaDB HTTP server at `127.0.0.1:8002`
- Source: PostgreSQL `msjarvisgis.gbim_worldview_entity` → CSV → Chroma
- Collection `gbim_worldview_entities` now receiving all 5.4M+ West Virginia spatial entities
- Spatial provenance: EPSG:26917 (UTM Zone 17N NAD83) centroids in metadata
- Prior sample-only limitation (5,000 rows) eliminated — full corpus being ingested
- Eliminates the last major gap between documented architecture and live system capability

---

## Immediate Next Steps (before deleting this file)

- [ ] Monitor GBIM full ingest completion — check `col.count()` on `gbim_worldview_entities` until it reaches 5.4M+
- [ ] Wire `recovered-services/services/ms_jarvis_unified_gateway.py` `process_unified` into active `services/ms_jarvis_unified_gateway.py`
- [ ] Add `/wv_summary` endpoint to `services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py`
- [ ] Fix `jarvis-direct-rag` DNS resolution inside Docker network
- [ ] Add `jarvis-20llm-production` to rebuild compose (or document as out-of-scope for rebuild phase 1)
- [ ] Update chapters 05, 06 with confirmed second NVMe mount and legacy archive location
- [ ] Once `consciousness` block is fully populated in glassbox, update chapters 39, 40, 41 and delete this file

---

*Last updated: 2026-03-13 21:28 EDT by Carrie Kidd (Mamma Kidd), Oak Hill WV*
