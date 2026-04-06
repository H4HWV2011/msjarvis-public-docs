# Chapter 35 — Swarm Functions and Eternal Watchdogs

*MountainShares Artificial Learning & Location Intelligence (Ms. Jarvis)*
*Carrie Kidd (Mamma Kidd) — Pax, WV*
*Last updated: ★★★★ April 6, 2026 — FINAL REWRITE*

---

## Chapter Stamp — ★★★★ April 6, 2026 (FINAL)

| Item | Confirmed Value |
|:--|:--|
| Running containers | **105** — clean baseline, zero exposed ports |
| Preflight gate | **31 PASS ❌ 0 FAIL ⚠️ 0 WARN** |
| ChromaDB | **47 collections / 6,722,589 vectors / 12 GB** — v2 API, port 8002 |
| `psychological_rag` | **968 docs** |
| `zcta_centroids` | **829 WV ZCTAs** — seeded April 4, 2026 |
| `local_resources` | **101 records** — all 55 WV counties |
| Address points | **1,115,588** |
| Landowner spatial rows | **20,593** |
| `gbim_entities` schema | ✅ present — 10 records |
| `gbim_worldview_entities` (ChromaDB) | **5,416,521 vectors** — operational GBIM corpus |
| `autonomous_learner` (ChromaDB) | **21,181 records** — accumulating |
| Cloudflare tunnel | **live** — `https://egeria.mountainshares.us` |
| Auth enforced | unauthenticated `/chat` → HTTP 401 |
| BBB + RAG + EthicalFilter | **Verified** |
| `jarvis-memory` | **Healthy** |
| Judge signing keys | **5 of 5 present** |
| BELIEFS_DSN | Corrected → `local_resources:5435` |
| Fire/EMS column mismatches | **Fixed** |
| Log-before-result bug | **Fixed** — all 6 branches |
| All 6 GBIM benefit indexer routes | **Verified live** |
| `msjarvisgis` (production) | **5432 / 45 GB / 548 tables** — Ch. 33 ground truth |
| `msjarvisgis` (rebuild container) | **5435** — 829 ZCTA centroids, PostGIS 3.4 |
| `msjarvis` GBIM | **5433** — 5,416,521 entities, `confidence_decay` metadata |
| `truth_verification` BBB filter | **`rag_grounded_v2`** — supersedes `heuristic_contradiction_v1` per OI-37-C (closed April 3, 2026) |
| BakLLaVA | **FULLY ELIMINATED** — not in Ollama, not in source, .pyc cache cleared |
| StarCoder2 (8207) | **Proxied — 0-char on community queries, excluded from consensus scoring** |
| Chapter status | **✅ FINAL** |

**Port note — `msjarvisgis`.** Two `msjarvisgis` instances exist across the thesis. The production instance (Chapter 33 ground truth) is at host port **5432 / 45 GB / 548 tables**. The rebuild container instance is at host port **5435** (829 ZCTA centroids, PostGIS 3.4 confirmed April 4, 2026). All §35.2 and §35.9 references to `gisdb:5432` and `msjarvisgis` refer to the production instance at its corrected Chapter 33 values. The rebuild container at `5435` is documented separately in Chapter 34 §34.5.

---

## RED TEAM GATE — SEALED — April 4, 2026 FINAL

```
════════════════════════════════════════════════════════════
RED TEAM GATE: SEALED ✅ — April 4, 2026
CHAPTER 35 STATUS: SEALED ✅ — Updated to 105 containers April 6
════════════════════════════════════════════════════════════
105 containers running  |  0 ports exposed on 0.0.0.0
47 ChromaDB collections |  968 psychological_rag docs
829 zcta_centroids      |  101 local_resources (all 55 WV counties)
1,115,588 address pts   |  20,593 landowner spatial rows
gbim_entities schema present  |  10 GBIM records
gbim_worldview_entities: 5,416,521 vectors (ChromaDB)
autonomous_learner: 21,181 records (accumulating)
Cloudflare tunnel live: https://egeria.mountainshares.us
Auth enforced: unauthenticated /chat → HTTP 401
BBB + RAG + EthicalFilter verified
jarvis-memory healthy   |  All 5 judge signing keys present
BELIEFS_DSN → local_resources DB (corrected)
Fire/EMS column mismatches fixed | log-before-result fixed (6 branches)
All 6 GBIM benefit indexer routes verified live
truth_verification: rag_grounded_v2 (OI-37-C, closed April 3)
BakLLaVA: FULLY ELIMINATED (not in Ollama, not in source)
StarCoder2: Proxied — 0-char on community queries, excluded from consensus
scripts/preflight_gate.sh: 31 PASS  ❌ FAIL: 0  ⚠️ WARN: 0
════════════════════════════════════════════════════════════
```

### 10 Issues Closed — April 4, 2026

**Preflight Failures Resolved:**

| # | Check | Root Cause | Fix Applied |
|:--|:--|:--|:--|
| 1 | `jarvis-memory:8056` HTTP 404 | Preflight hit `/memories?limit=1` — requires auth | Switched to `/health` unauthenticated endpoint |
| 2 | `confidence_decay` MISSING | Preflight used `psql -h localhost -p 5433` — not reachable from host | Switched to `docker exec msjarvis-pgdata-rescue psql`; `information_schema.columns` schema check |
| 3 | RAG 0 documents | `/query` requires `collection` + `message` fields — neither sent | Added required fields to POST body; fixed `documents` vs `results` parse |
| 4 | BBB EthicalFilter scored 0 | Preflight hit `/check` (wrong endpoint), wrong field names | Fixed to `/filter`, correct body `content`/`actor_role`, check `content_approved` |
| 5 | `neurobiological-master` curl OCI error | `docker exec` into container — curl not installed | Changed to host-side `curl http://127.0.0.1:8018/health` |
| 6 | `line 188: pass: command not found` | Python `pass` syntax in bash script | Replaced with bash no-op `:` |
| 7 | ChromaDB < 40 (found 2) | Hitting wrong port/API version | Fixed to `localhost:8002/api/v1/collections` |

**Preflight Warnings Resolved:**

| # | Check | Root Cause | Fix Applied |
|:--|:--|:--|:--|
| 8 | `local_resources` < 100 | Only 48 verified records — 55 WV counties not seeded | Ran `seed_local_resources.py` → 101 records, all 55 counties |
| 9 | `psychological_rag` 0 docs | ChromaDB port mismatch in preflight | Fixed with ChromaDB port fix above |

**Script Bug Fixed:**

| # | File | Issue | Fix |
|:--|:--|:--|:--|
| 10 | `VERIFYANDTEST.sh` | `sed` failed on URL in pattern for 8060 health check | Replaced dead REST check with `docker exec jarvis-redis redis-cli ping` |

### Chapter 35 Layer Status at Seal

| Layer | Status |
|:--|:--|
| Infrastructure | 105 containers, zero exposed ports ✅ |
| Security perimeter | Caddy + auth + Cloudflare tunnel enforced ✅ |
| Data integrity | PostGIS, ChromaDB (47 collections, 829 zcta_centroids), RAG all populated ✅ |
| AI pipeline | BBB, GBIM, judges (5 signing keys), memory all healthy ✅ |
| Identity safety | LM Synthesizer identity rules confirmed ✅ |
| GBIM benefit indexer | All 6 routes live, BELIEFS_DSN corrected, Fire/EMS fixed ✅ |
| Preflight gate | 31 PASS ❌ 0 FAIL ⚠️ 0 WARN ✅ |

### Chapter 36 Pre-conditions — MET ✅

- [x] `jarvis-memory:8056` healthy and auth-confirmed (`JARVIS_API_KEY` set)
- [x] All 5 judge signing keys present
- [x] `ms_jarvis_identity` ChromaDB collection populated
- [x] Auth enforced on `/chat` — unauthenticated → HTTP 401
- [x] Cloudflare tunnel live at `https://egeria.mountainshares.us`
- [x] BBB EthicalFilter verified (`/filter` endpoint, `content_approved` field)
- [x] 105 containers running, zero `0.0.0.0` exposures
- [x] `preflight_gate.sh` 31 PASS 0 FAIL
- [x] 829 `zcta_centroids` seeded — WV ZIP-code spatial grounding active
- [x] All 6 GBIM benefit indexer routes verified live

---

## Why This Matters for Polymathmatic Geography

The MountainShares Artificial Learning & Location Intelligence system operates as a polymathmatic geography instrument: every response it produces must be accountable to a specific place, a specific community, and a specific moment in Appalachian life. Swarm functions and eternal watchdogs are the mechanisms that make this accountability possible at scale.

This chapter is grounded in PostgreSQL `msjarvis:5433` (5,416,521 GBIM entities with `confidence_decay` metadata, 80 epochs, 206 source layers) and `gisdb`/`msjarvisgis` at port 5432 (PostGIS, 45 GB, 548 tables — Chapter 33 April 6, 2026 ground truth). The `zcta_centroids` ChromaDB collection — 829 West Virginia ZIP Code Tabulation Areas — ties every swarm query to a physical location on the Appalachian landscape.

This chapter supports the following polymathmatic geography principles:

- **P1 – Every where is entangled** — a single query is distributed across 22 specialized models, each contributing a domain perspective, before synthesis is validated against PostgreSQL GBIM.
- **P3 – Power has a geometry** — visibility into which models contribute to consensus and which are silenced by memory constraints, resource limits, or intentional disabling reveals structural power embedded in the ensemble.
- **P5 – Design is a geographic act** — semaphore slots, container memory limits, concurrency gates, and model tier groupings reshape what the system can reason about and how quickly it responds to Appalachian community questions grounded in PostGIS (production `gisdb:5432` — 45 GB / 548 tables; `zcta_centroids:8002` — 829 WV ZCTAs).
- **P12 – Intelligence with a ZIP code** — every query routes through a 22-slot ensemble organized into four tiers spanning code, medicine, language, vision, and structured data reasoning, binding the synthesized answer to DGM cascade validation grounded in constitutional and community commitments.
- **P16 – Power accountable to place** — every model's participation or failure in each consensus cycle is logged at `jarvis-memory:8056`, making ensemble behavior inspectable and auditable over time as PostgreSQL-backed operational history.

---

```
┌─────────────────────────────────────────────────────────────┐
│   Swarm Functions & Eternal Watchdogs Architecture          │
│   ★★★★ April 6, 2026 — FINAL — 105 containers              │
│   Pax, West Virginia                                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌────────────────────────────────────────────────┐        │
│  │  22-Slot LLM Ensemble (Swarm Function)         │        │
│  │  jarvis-20llm-production (port 8008)           │        │
│  │  ★ Up — 105/105 confirmed April 6              │        │
│  │                                                │        │
│  │  TINY_MODELS (2):                              │        │
│  │  -  TinyLlama (8201), Gemma (8202)             │        │
│  │                                                │        │
│  │  SMALL_MODELS (3):                             │        │
│  │  -  Phi3 Mini (8210), Dolphin-Phi (8212)       │        │
│  │  -  Orca-Mini (8213)                           │        │
│  │                                                │        │
│  │  MEDIUM_MODELS (8 active, 1 eliminated):       │        │
│  │  -  MedLlama2 (8203), MiniCPM-V (8204)        │        │
│  │  -  LLaVA (8205), SQLCoder (8206)             │        │
│  │  -  Zephyr (8215), Starling-LM (8216)         │        │
│  │  -  Neural-Chat (8217), OpenChat (8218)        │        │
│  │  -  BakLLaVA (8211): FULLY ELIMINATED         │        │
│  │       not in Ollama, not in source             │        │
│  │                                                │        │
│  │  LARGE_MODELS (8):                             │        │
│  │  -  StarCoder2 (8207): PROXIED — 0-char on    │        │
│  │       community queries, excluded from         │        │
│  │       consensus scoring (OI pending)           │        │
│  │  -  CodeLlama (8208), DeepSeek Coder (8209)    │        │
│  │  -  Qwen2 (8214), Vicuna (8219)                │        │
│  │  -  LLaMA 2 (8220), Mistral (8221)             │        │
│  │  -  LLaMA 3.1 (8222)                           │        │
│  │                                                │        │
│  │  Coordination:                                 │        │
│  │  -  asyncio.Semaphore(4) — max 4 concurrent   │        │
│  │  -  Timeout: 600.0s (jarvis-semaphore:8030)   │        │
│  │  -  21/22 contributing consensus               │        │
│  │  -  Judge consistency: 0.975                   │        │
│  │  -  GPU active: RTX 4070                       │        │
│  │  -  End-to-end: 99–107s (GPU baseline)         │        │
│  └────────────────────────────────────────────────┘        │
│      ↓                                                      │
│  ┌────────────────────────────────────────────────┐        │
│  │  jarvis-semaphore (port 8030)                  │        │
│  │  -  max_concurrent: 4                          │        │
│  │  -  timeout: 600.0                             │        │
│  └────────────────────────────────────────────────┘        │
│      ↓                                                      │
│  ┌────────────────────────────────────────────────┐        │
│  │  Dual Blood-Brain Barrier Architecture         │        │
│  │                                                │        │
│  │  jarvis-blood-brain-barrier (8016) PRIMARY     │        │
│  │  -  Phase 1.4 six-filter input stack:          │        │
│  │     EthicalFilter, SpiritualFilter,            │        │
│  │     SafetyMonitor, ThreatDetection,            │        │
│  │     steganography_filter,                      │        │
│  │     truth_verification (rag_grounded_v2        │        │
│  │     per OI-37-C, closed April 3, 2026)         │        │
│  │  -  EthicalFilter: POST /filter                │        │
│  │     body: {content, actor_role}                │        │
│  │     response: content_approved                 │        │
│  │  -  Phase 4.5: log+passthrough mode            │        │
│  │  -  Durable audit: jarvis-memory:8056          │        │
│  │                                                │        │
│  │  nbb_blood_brain_barrier (8301)                │        │
│  │  -  NBB-INTERNAL — neurobiological variant     │        │
│  │  -  Phase 1 / NBB subconscious pathway         │        │
│  └────────────────────────────────────────────────┘        │
│      ↓                                                      │
│  ┌────────────────────────────────────────────────┐        │
│  │  Five-Layer Watchdog System                    │        │
│  │                                                │        │
│  │  1. VERIFYANDTEST.sh                           │        │
│  │     105 containers (April 6)                   │        │
│  │     preflight_gate.sh: 31 PASS 0 FAIL          │        │
│  │     8060: docker exec jarvis-redis             │        │
│  │       redis-cli ping (April 4 fix)             │        │
│  │                                                │        │
│  │  2. Ollama Internal Memory Scheduler           │        │
│  │     20 GB container limit                      │        │
│  │     OLLAMA_NUM_PARALLEL=1                      │        │
│  │     OLLAMA_MAX_LOADED_MODELS=1                 │        │
│  │                                                │        │
│  │  3. Asyncio Semaphore + jarvis-semaphore:8030  │        │
│  │     max_concurrent: 4, timeout: 600.0          │        │
│  │                                                │        │
│  │  4. MAX_CONCURRENT_CHATS Gate (set to 2)       │        │
│  │                                                │        │
│  │  5. Redis DynamicPortService                   │        │
│  │     jarvis-redis Up — redis-cli ping: PONG     │        │
│  └────────────────────────────────────────────────┘        │
│      ↓                                                      │
│  ┌────────────────────────────────────────────────┐        │
│  │  GBIM Benefit Indexer — All 6 routes live      │        │
│  │                                                │        │
│  │  benefit_lookup  — Kanawha lr=10  ✅           │        │
│  │  hospitals       — 10 results    ✅           │        │
│  │  fire_departments— 20 results    ✅           │        │
│  │  ems_stations    — 20 results    ✅           │        │
│  │  geo_knowledge   — both paths    ✅           │        │
│  │  conversation_beliefs — all 6    ✅           │        │
│  │                                                │        │
│  │  BELIEFS_DSN → local_resources DB (5435)       │        │
│  │  wv_fire_stations_clean — corrected            │        │
│  │  owner_name AS name — corrected                │        │
│  │  log-before-result — fixed (6 branches)        │        │
│  │                                                │        │
│  │  Deferred: lr=0 Raleigh/Logan/Cabell/Fayette   │        │
│  │  → Crystal Coyler Chapter 5 data batch         │        │
│  └────────────────────────────────────────────────┘        │
│                                                             │
│  External Access                                           │
│  -  Cloudflare tunnel: https://egeria.mountainshares.us    │
│  -  Auth enforced: unauthenticated /chat → HTTP 401        │
│  -  Zero 0.0.0.0 exposed ports confirmed                   │
│                                                             │
│  Integration Points (PostgreSQL-Grounded)                  │
│  -  msjarvis:5433  — GBIM 5,416,521 entities               │
│  -  gisdb:5432     — PostGIS 45 GB / 548 tables            │
│     (Ch. 33 April 6 ground truth)                          │
│  -  local_resources:5435 — 101 records, 55 WV counties     │
│  -  ChromaDB:8002  — 47 collections / 6,722,589 vectors    │
│     zcta_centroids: 829 WV ZCTAs                           │
│     autonomous_learner: 21,181 records                     │
│  -  jarvis-memory:8056 — durable BBB audit trail           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

*Figure 35.1. Swarm functions, eternal watchdogs, and GBIM benefit indexer architecture (★★★★ April 6, 2026 FINAL — 105 containers, zero exposed ports): dual-BBB with `jarvis-blood-brain-barrier:8016` (EthicalFilter verified at `/filter`, `content_approved` field; `truth_verification` now `rag_grounded_v2` per OI-37-C closed April 3, 2026; Phase 4.5 log+passthrough; all gate decisions durable at `jarvis-memory:8056`) and `nbb_blood_brain_barrier:8301` (NBB-internal); BakLLaVA FULLY ELIMINATED; StarCoder2 proxied — 0-char on community queries, excluded from consensus scoring; 22-slot LLM ensemble with `jarvis-semaphore:8030` (max_concurrent: 4, timeout: 600.0); 21/22 consensus at 0.975 judge consistency; RTX 4070 GPU 99–107s; five-layer watchdog; preflight 31 PASS 0 FAIL; PostgreSQL `msjarvis:5433` (5,416,521 GBIM entities), `gisdb:5432` (45 GB / 548 tables — Ch. 33 April 6 ground truth), `local_resources:5435` (101 records, all 55 WV counties); ChromaDB 47 collections / 6,722,589 vectors including 829 `zcta_centroids` and 21,181 `autonomous_learner` records; GBIM benefit indexer all 6 routes live; BELIEFS_DSN corrected; lr=0 Raleigh/Logan/Cabell/Fayette deferred pending Crystal Coyler Chapter 5 data.*

---

## Status as of ★★★★ April 6, 2026 — FINAL (105 containers — zero exposed ports)

| Category | Details |
|:--|:--|
| **Sealed state** | RED TEAM GATE: SEALED — April 4, 2026. Chapter stamp updated April 6. `scripts/preflight_gate.sh`: **31 PASS ❌ 0 FAIL ⚠️ 0 WARN**. 105 containers, zero `0.0.0.0` exposures. 47 ChromaDB collections / 6,722,589 vectors. 829 `zcta_centroids`. 21,181 `autonomous_learner` records. 968 `psychological_rag` docs. 101 `local_resources` (all 55 WV counties). 1,115,588 address points. 20,593 landowner spatial rows. `gbim_entities` schema present (10 records). `gbim_worldview_entities` 5,416,521 vectors. Cloudflare tunnel live. Auth enforced. BBB EthicalFilter verified. `jarvis-memory` healthy. All 5 judge signing keys present. BakLLaVA FULLY ELIMINATED. |
| **10 preflight issues closed** | 7 ❌ failures + 2 ⚠️ warnings + 1 script bug — all resolved April 4, 2026. See seal block above. |
| **GBIM benefit indexer** | All 6 routes verified live. BELIEFS_DSN corrected to `local_resources:5435`. Fire/EMS column mismatches fixed (`owner_name AS name`, `wv_fire_stations_clean`, correct `r[0]..r[n]` index mapping). Log-before-result bug fixed across all 6 branches. `conversation_beliefs` logging confirmed all 6 modes with correct `user_id`. lr=0 for Raleigh/Logan/Cabell/Fayette intentionally deferred — Crystal Coyler Chapter 5 data dependency; zero code changes needed on arrival. |
| **Implemented and verified** | 22-slot LLM ensemble (21/22 consensus). `jarvis-semaphore:8030` (max_concurrent: 4, timeout: 600.0). Dual-BBB: `8016` (primary) + `8301` (NBB-internal). `truth_verification` now `rag_grounded_v2` (OI-37-C, closed April 3). `jarvis-memory:8056` durable audit trail. PostgreSQL `msjarvis:5433` (5,416,521 GBIM entities). `gisdb:5432` (45 GB / 548 tables — Ch. 33 ground truth). `local_resources:5435` (101 records). ChromaDB `zcta_centroids` 829 items. Redis PONG confirmed. RTX 4070 (99–107s). Judge consistency 0.975. |
| **Partially implemented / scaffolded** | ChromaDB `operations_history` automated ingestion not yet active. Phase 4.5 BBB output guard in log+passthrough mode pending recalibration. StarCoder2 routing-layer fix tracked — OI pending. `confidence_decay`-aware automated decay-flagging not yet implemented. |
| **Future work / design intent** | Automated VERIFYANDTEST.sh log ingestion to ChromaDB. PostgreSQL time-series analytics dashboard. Dynamic model tier selection by query complexity. Phase 4.5 BBB full verdict-dict enforcement after recalibration. StarCoder2 routing-layer exclusion from community query dispatch. lr=0 county resolution on Crystal Coyler Chapter 5 data arrival. |

Cross-reference: Chapter 5 (Crystal Coyler data — lr=0 county resolution), Chapter 12 (NBB/neurobiological), Chapter 16 (primary BBB), Chapter 17 (ultimatechat execution), Chapter 33 (judge pipeline + April 6 ground truth), Chapter 34 (spiritual architecture — msjarvisgis rebuild port 5435), Chapter 36 (identity and registration — pre-conditions MET), Chapter 40 §40-C (March 18 security hardening).

---

## 35.1 Purpose of Swarm and Watchdog Layers

The MountainShares Artificial Learning & Location Intelligence system operates as a polymathmatic geography instrument: every response must be accountable to a specific place, a specific community, and a specific moment in Appalachian life. Swarm functions and eternal watchdogs are the mechanisms that make this accountability possible at scale.

**Coordination.** Swarm functions allow multiple agents and services to contribute from their own specialization. In the current deployment this is the 22-slot LLM ensemble organized into four model tiers, where each proxy container contributes a weighted response to every query with context sourced from PostgreSQL-backed RAG collections. The GBIM benefit indexer operates as a parallel swarm function for community resource queries — routing housing, health, fire/EMS, and geographic knowledge requests to the appropriate PostGIS or local_resources data source.

**Oversight.** Watchdogs provide continuous monitoring of key signals, intervening when behavior deviates from expected bounds. This is realized through `VERIFYANDTEST.sh`, Ollama's internal memory scheduler, `jarvis-semaphore:8030`, the `MAX_CONCURRENT_CHATS` gate, and the Redis-backed DynamicPortService. All BBB gate decisions are durably logged at `jarvis-memory:8056`, adding persistent accountability to the watchdog record.

**Stability.** Together they keep the system responsive and aligned even as individual components change or fail. The February 2026 hardening session demonstrated this directly: without semaphore and concurrency controls, the system degraded from 20/22 models to 0/22 under concurrent load. With them in place, 21/22 models respond reliably on every warm-cache query. The March 22, 2026 GPU activation (RTX 4070) reduced end-to-end latency to 99–107s from approximately 330s.

**Consciousness grounding.** The consciousness bridge (`jarvis-consciousness-bridge`) and brain orchestrator (`jarvis-brain-orchestrator`) are essential infrastructure, not optional. All swarm coordination and watchdog monitoring operates within this framework — the brain orchestrator maintains swarm coherence across all operational cycles.

---

## 35.2 Dual Blood-Brain Barrier Architecture

As of April 6, 2026 (105 containers, zero exposed ports), two BBB containers run simultaneously. Their roles are distinct and must not be conflated.

### jarvis-blood-brain-barrier (port 8016) — Primary, Judge Pipeline Output Guard

`jarvis-blood-brain-barrier` at `127.0.0.1:8016` is the architecturally authoritative BBB, serving two roles:

- **Phase 1.4 — input stack:** All six filters active — EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection, steganography_filter, truth_verification.
  - ★ **`truth_verification` filter update (OI-37-C, closed April 3, 2026).** The `truth_verification` filter has been upgraded from `heuristic_contradiction_v1` to `rag_grounded_v2`. Verification is now grounded against the RAG corpus rather than heuristic pattern matching. This supersedes all earlier Chapter 35 descriptions of `truth_verification` as a heuristic filter.
  - ★ **EthicalFilter (April 4, 2026 verified).** Correct endpoint: `/filter`. Correct body fields: `content`, `actor_role`. Correct response field: `content_approved`.
- **Phase 4.5 — output guard.** After the 22-model ensemble and DGM cascade, `apply_output_guards_async` posts the full judge verdict dict to `jarvis-blood-brain-barrier:8016/output_guard` (integrated March 18, 2026; 8.0s timeout; fail-open on HTTP 500). Phase 4.5 is currently in log+passthrough mode (commit 18b8ddac, March 22, 2026) pending output threshold recalibration.

★ All Phase 1.4 filter events and Phase 4.5 output guard events are persistently logged at `jarvis-memory:8056`. Gate decisions survive container restarts and are independently queryable for governance accountability.

### nbb_blood_brain_barrier (port 8301) — NBB-Internal Neurobiological Variant

`nbb_blood_brain_barrier` at `127.0.0.1:8301` is the NBB-internal neurobiological variant. It operates on the Phase 1 / NBB subconscious pathway. It does not receive the judge pipeline verdict dict, does not set `bbb_checked: true` in the main UltimateResponse, and does not replace `jarvis-blood-brain-barrier:8016`.

```
┌──────────────────────────────────────────────────────┐
│   Dual-BBB Architecture — Role Disambiguation        │
│   ★★★★ April 6, 2026 FINAL                           │
├──────────────────────────────────────────────────────┤
│                                                      │
│  jarvis-blood-brain-barrier (8016) ★ Up              │
│  Role: PRIMARY — judge pipeline output guard         │
│  Phase 1.4 input filters (six):                      │
│    EthicalFilter, SpiritualFilter, SafetyMonitor,    │
│    ThreatDetection, steganography_filter,            │
│    truth_verification (rag_grounded_v2               │
│      per OI-37-C, closed April 3, 2026)              │
│  EthicalFilter: POST /filter                         │
│    body: {content, actor_role}                       │
│    response field: content_approved                  │
│  Phase 4.5: log+passthrough (commit 18b8ddac)        │
│  Receives: full judge verdict dict                   │
│  Sets: bbb_checked: true in UltimateResponse         │
│  Durable audit: jarvis-memory:8056                   │
│                                                      │
│  nbb_blood_brain_barrier (8301) ★ Up                 │
│  Role: NBB-INTERNAL — neurobiological variant        │
│  Phase 1 / NBB subconscious pathway                  │
│  Port 8016 ≠ Port 8301. Do not substitute.           │
│                                                      │
└──────────────────────────────────────────────────────┘
```

*Figure 35.2. Dual-BBB role disambiguation (★★★★ April 6, 2026 FINAL).*

**Verified integration pattern:**

```bash
# Primary BBB — EthicalFilter:
curl -s -X POST http://127.0.0.1:8016/filter \
  -H "Content-Type: application/json" \
  -d '{"content": "test message", "actor_role": "user"}' \
  | python3 -c "import sys,json; r=json.load(sys.stdin); \
    print('content_approved:', r.get('content_approved'))"
# Expected: content_approved: True

# NBB-internal BBB:
curl -s http://127.0.0.1:8301/health | python3 -m json.tool

# Durable audit trail:
curl -H "Authorization: Bearer $JARVIS_API_KEY" http://localhost:8056/health
# Expected: healthy

# Redis session-sidecar health (April 4 fix):
docker exec jarvis-redis redis-cli ping
# Expected: PONG
```

---

## 35.3 Swarm Functions: The 22-Slot LLM Ensemble

The primary swarm function is the 20-LLM production service (`jarvis-20llm-production`, port 8008 on host), managing 22 proxy containers (`llm1-proxy` through `llm22-proxy`, ports 8201–8222) organized into four tiers in `llm_consensus_20_FINAL.py`. The `jarvis-semaphore:8030` service (`max_concurrent: 4`, `timeout: 600.0`) is the compose-managed semaphore gate.

### Model Roster by Tier

**TINY_MODELS (2 configured)**

| Proxy | Port | Model | Name |
|:--|:--|:--|:--|
| llm1-proxy | 8201 | tinyllama:1.1b | TinyLlama |
| llm2-proxy | 8202 | gemma:latest | Gemma |

**SMALL_MODELS (3 configured)**

| Proxy | Port | Model | Name |
|:--|:--|:--|:--|
| llm10-proxy | 8210 | phi3:mini | Phi3 Mini |
| llm12-proxy | 8212 | dolphin-phi:latest | Dolphin-Phi |
| llm13-proxy | 8213 | orca-mini:latest | Orca-Mini |

**MEDIUM_MODELS (8 active, 1 eliminated)**

| Proxy | Port | Model | Name | Status |
|:--|:--|:--|:--|:--|
| llm3-proxy | 8203 | medllama2:latest | MedLlama2 | ✅ active |
| llm4-proxy | 8204 | minicpm-v:latest | MiniCPM-V | ✅ active |
| llm5-proxy | 8205 | llava:latest | LLaVA | ✅ active |
| llm6-proxy | 8206 | sqlcoder:latest | SQLCoder | ✅ active |
| llm15-proxy | 8215 | zephyr:latest | Zephyr | ✅ active |
| llm16-proxy | 8216 | starling-lm:latest | Starling-LM | ✅ active |
| llm17-proxy | 8217 | neural-chat:latest | Neural-Chat | ✅ active |
| llm18-proxy | 8218 | openchat:latest | OpenChat | ✅ active |
| llm11-proxy | 8211 | bakllava:latest | BakLLaVA | ❌ **FULLY ELIMINATED** — not in Ollama, not in source, .pyc cache cleared (Ch. 33 confirmed) |

**LARGE_MODELS (8 configured)**

| Proxy | Port | Model | Status | Notes |
|:--|:--|:--|:--|:--|
| llm7-proxy | 8207 | starcoder2:latest | ⚠️ Proxied | **0-char on community queries — excluded from consensus scoring.** Routing-layer fix tracked, OI pending. (Ch. 33 §33.3 harmonized.) |
| llm8-proxy | 8208 | codellama:latest | ✅ active | |
| llm9-proxy | 8209 | deepseek-coder:latest | ✅ active | |
| llm14-proxy | 8214 | qwen2:latest | ✅ active | |
| llm19-proxy | 8219 | vicuna:latest | ✅ active | |
| llm20-proxy | 8220 | llama2:latest | ✅ active | |
| llm21-proxy | 8221 | mistral:latest | ✅ active | |
| llm22-proxy | 8222 | llama3.1:8b | ✅ active | |

**BakLLaVA elimination note (35-C).** BakLLaVA is FULLY ELIMINATED as of the Chapter 33 clean sweep. It is not in the Ollama model registry, not present in source code, and `.pyc` cache has been cleared. Earlier drafts described `llm11-proxy:8211` as "permanently disabled — name-check guard." That language is superseded. The slot is present in the compose file for continuity but the model does not exist in this deployment.

**StarCoder2 status note (35-E).** StarCoder2 at `llm7-proxy:8207` returns HTTP 200 but produces zero-character responses on community queries. It is currently proxied and excluded from consensus scoring on community queries. A routing-layer fix to suppress community query dispatch is tracked as a future work item. This status is harmonized with Chapter 33 §33.3.

### Swarm Execution Model

When a chat request arrives, `ProductionBrain.run()` fires requests to all 22 configured endpoints concurrently, gated by `jarvis-semaphore:8030`. The semaphore limits concurrent Ollama requests to four at a time, preventing serial Ollama scheduler overload while allowing the ensemble to operate in parallel batches.

```python
sem = asyncio.Semaphore(4)  # jarvis-semaphore:8030 max_concurrent: 4

async def guarded(client, m):
    async with sem:
        return await self.query_one(client, m, prompt)

results = await asyncio.gather(*[guarded(client, m) for m in self.models])
```

### Verified Swarm Timing Profile (★ GPU baseline, March 22 – April 4, 2026)

```
[Phi3 Mini]      OK in  ~8–10s    ★ GPU-accelerated
[TinyLlama]      OK in  ~10–12s   ★ GPU-accelerated
[Orca-Mini]      OK in  ~14–18s   ★ GPU-accelerated
[Gemma]          OK in  ~16–20s   ★ GPU-accelerated
[Dolphin-Phi]    OK in  ~18–22s   ★ GPU-accelerated
[MedLlama2]      OK in  ~24–28s   ★ GPU-accelerated
[LLaVA]          OK in  ~24–28s   ★ GPU-accelerated
[Neural-Chat]    OK in  ~24–28s   ★ GPU-accelerated
[StarCoder2]     OK in  ~28–32s   ← HTTP 200, 0-char on community queries
                                    excluded from consensus scoring
[LLaMA 2]        OK in  ~28–32s   ★ GPU-accelerated
[LLaMA 3.1]      OK in  ~28–32s   ★ GPU-accelerated (identity guard active)
[Vicuna]         OK in  ~28–32s   ★ GPU-accelerated
[DeepSeek Coder] OK in  ~30–34s   ★ GPU-accelerated
[SQLCoder]       OK in  ~30–34s   ★ GPU-accelerated
[OpenChat]       OK in  ~32–36s   ★ GPU-accelerated
[MiniCPM-V]      OK in  ~36–40s   ★ GPU-accelerated
[Zephyr]         OK in  ~38–44s   ★ GPU-accelerated
[Starling-LM]    OK in  ~40–46s   ★ GPU-accelerated
[CodeLlama]      OK in  ~40–46s   ★ GPU-accelerated
[Mistral]        OK in  ~42–48s   ★ GPU-accelerated
[Qwen2]          OK in  ~44–50s   ★ GPU-accelerated
[BakLLaVA]       FULLY ELIMINATED (not in Ollama — no resource consumption)
21/22 models contributing consensus
Judge pipeline score: 0.975
★ GPU end-to-end: 99–107s (confirmed runs: 99.6s, 105.9s, 106.5s)
```

---

## 35.4 GBIM Benefit Indexer — Community Resource Swarm Function

The `jarvis-gbim-benefit-indexer` routes queries about benefits, healthcare facilities, emergency services, and geographic knowledge to the correct PostgreSQL or PostGIS data source, then logs conversation beliefs to the local_resources DB for longitudinal community intelligence. All six route modes verified live April 4, 2026.

### What Was Built and Fixed — April 4, 2026

**BELIEFS_DSN corrected.** `BELIEFS_DSN` was added to the `jarvis-gbim-benefit-indexer` environment block. The indexer previously wrote `conversation_beliefs` to `msjarvisgis:5432` (the PostGIS geospatial DB), which has no `conversation_beliefs` table. The correct target is `jarvis-local-resources-db:5435`.

```yaml
# docker-compose.yml — jarvis-gbim-benefit-indexer
environment:
  - BELIEFS_DSN=postgresql://jarvis:${JARVIS_DB_PASSWORD}@jarvis-local-resources-db:5435/local_resources
```

**Fire/EMS column name mismatches corrected:**

| Issue | Before | After |
|:--|:--|:--|
| Owner name column | `name` (missing in schema) | `owner_name AS name` |
| Fire stations table | `wv_fire_stations` | `wv_fire_stations_clean` |
| Row index mapping | Incorrect positions | Correct `r[0]..r[n]` on all three table schemas |

**Log-before-result bug fixed across all 6 branches.** The threading log block referenced `result` before assignment in the `except` path, causing `UnboundLocalError` on any route branch that hit a query exception.

```python
# BEFORE — crashes if exception raised before result is assigned:
except Exception as e:
    log_to_chroma(result, ...)   # UnboundLocalError

# AFTER — safe in all paths:
except Exception as e:
    log_to_chroma([], ...)       # empty list, never unbound
```

Branches fixed: `benefit_lookup`, `hospitals`, `fire_departments`, `ems_stations`, `geo_knowledge` (×2 — both code paths).

### All 6 Route Modes — Verified Live

| Route Mode | Test | Result |
|:--|:--|:--|
| `benefit_lookup` | Kanawha county, `lr=10` | ✅ 10 results |
| `hospitals` | Live query | ✅ 10 results |
| `fire_departments` | Live query | ✅ 20 results |
| `ems_stations` | Live query | ✅ 20 results |
| `geo_knowledge` | Both code paths | ✅ no UnboundLocalError |
| `conversation_beliefs` logging | All 6 modes, correct `user_id` | ✅ confirmed |

### What Is Intentionally Deferred

`lr=0` for Raleigh, Logan, Cabell, and Fayette counties — zero local resource results because Crystal Coyler's next data batch has not yet arrived. Zero code changes needed when the data arrives. Tracked as **data dependency on Crystal Coyler — Chapter 5**.

---

## 35.5 ZCTA Centroids — ZIP-Code Spatial Grounding

829 West Virginia ZCTA centroids were seeded into ChromaDB on April 4, 2026. This collection binds every community query to a physical ZIP-code-level location on the Appalachian landscape — the operational realization of P12 (Intelligence with a ZIP code).

```
Seeding result — April 4, 2026:
Fetched 829 ZCTAs from PostGIS
  Inserted batch ending 24572
  Inserted batch ending 24925
  Inserted batch ending 25140
  Inserted batch ending 25444
  Inserted batch ending 25836
  Inserted batch ending 26150
  Inserted batch ending 26408
  Inserted batch ending 26750
  Inserted final batch
DONE — 829 items in 'zcta_centroids'

Spot-check — Pax, WV (ZCTA 25904):
{
  'ids': ['25904'],
  'metadatas': [{
    'cx': -81.28184535418767,
    'lat': 37.9262719,
    'state': 'WV',
    'zcta5': '25904',
    'lon': -81.2840002,
    'cy': 37.91690967562205
  }],
  'documents': ['West Virginia ZCTA 25904 centroid at 37.9263, -81.2840']
}
```

The `zcta_centroids` collection joins the broader ChromaDB corpus, confirmed at 47 total collections / 6,722,589 vectors / 12 GB at host port 8002 (April 6, 2026 baseline). All scripts targeting ChromaDB must use host port **8002**.

---

## 35.6 Use Cases for Swarm Functions

**Complex community queries.** When a resident of Pax, WV (ZCTA 25904, centroid 37.9263, -81.2840) asks about housing assistance, workforce development, or healthcare access, the ensemble distributes the question across medical (MedLlama2), structured data (SQLCoder), code and technical (CodeLlama, DeepSeek Coder), vision (LLaVA, MiniCPM-V), and general reasoning (Mistral, LLaMA 3.1, Qwen2) models simultaneously. The consensus synthesis integrates domain-specific contributions validated against PostgreSQL GBIM that no single model could provide.

**GBIM benefit routing.** The benefit indexer routes housing, healthcare, and emergency services queries to `local_resources:5435` (101 records, all 55 WV counties) and PostGIS (`gisdb:5432`, 45 GB, 548 tables — Ch. 33 ground truth). `conversation_beliefs` are logged after every interaction, building longitudinal community intelligence that informs future resource recommendations — the operational meaning of P16 (Power accountable to place).

**Robustness verification.** The judge pipeline consistency score measures whether independently prompted models reach similar conclusions. The March 21, 2026 canonical integration test records `consensus_score: 0.975` on the capital of West Virginia query, confirming ensemble stability not attributable to any single model's bias.

**Specialty routing.** SQLCoder handles structured data queries from PostgreSQL. CodeLlama and DeepSeek Coder handle technical implementation. MedLlama2 handles health-related queries. LLaVA and MiniCPM-V handle image and multimodal inputs.

**Redundancy.** With 21 of 22 configured slots contributing consensus, the ensemble tolerates individual model failures. BakLLaVA's full elimination, StarCoder2's 0-char consensus exclusion, and Ollama's occasional memory-related refusals do not prevent the system from producing high-quality responses grounded in PostgreSQL GBIM.

---

## 35.7 Eternal Watchdogs: Continuous Monitoring

### VERIFYANDTEST.sh (★ April 4 changelog applied)

April 4, 2026 seal results (updated to 105 containers April 6):

- Services healthy: 32/32
- LLM proxies healthy: 22/22 (HTTP 200; 21 contributing consensus)
- Docker containers running: **105** (zero exposed ports)
- ChromaDB collections: **47** (host port 8002)
- `psychological_rag` docs: **968**
- `local_resources` records: **101** (all 55 WV counties)
- Address points: **1,115,588**
- Landowner spatial rows: **20,593**
- `gbim_entities` schema: ✅ present (10 records)
- Cloudflare tunnel: ✅ `https://egeria.mountainshares.us`
- Auth: ✅ unauthenticated `/chat` → HTTP 401
- BBB EthicalFilter: ✅ verified (`/filter`, `content_approved`)
- `jarvis-memory:8056`: ✅ healthy
- Judge signing keys: ✅ all 5 present
- Redis ping: ✅ PONG (`docker exec jarvis-redis redis-cli ping` — April 4 fix)
- **`scripts/preflight_gate.sh`: 31 PASS ❌ 0 FAIL ⚠️ 0 WARN**

**Changelog — April 4, 2026.** Check `8060/session-sidecar` replaced dead `/health` REST endpoint with `docker exec jarvis-redis redis-cli ping`. Previous `sed` pattern on URL string caused `command not found`. Redis PONG is now the authoritative session-sidecar health proxy. Change is permanent.

### Ollama Internal Memory Scheduler

| Parameter | Verified Value |
|:--|:--|
| Ollama container memory limit | 20 GB |
| `OLLAMA_NUM_PARALLEL` | 1 |
| `OLLAMA_MAX_LOADED_MODELS` | 1 |
| Host total RAM | 29 GB |
| Host available RAM (production load) | 13 GB |
| GPU | RTX 4070 (active March 22, 2026) |
| GPU-accelerated inference | 99–107s end-to-end |

### Asyncio Semaphore + jarvis-semaphore:8030

`jarvis-semaphore:8030` (`max_concurrent: 4`, `timeout: 600.0`) is the compose-managed semaphore gate. `asyncio.Semaphore(4)` in `ai_server_20llm_PRODUCTION.py` acts in concert with it, preventing more than four simultaneous Ollama requests regardless of concurrent chat sessions.

### MAX_CONCURRENT_CHATS Gate

`MAX_CONCURRENT_CHATS=2` on `jarvis-main-brain` limits simultaneous full chat pipelines. Async jobs (`/chat/async`) use Redis job state (30-minute TTL) and do not consume a slot until active processing begins.

### Redis-backed DynamicPortService

Five NBB containers register health state to Redis using `DynamicPortService`. One Redis container (`jarvis-redis`): container-internal port **6379**, host-facing port **127.0.0.1:6380**.

```bash
# Host-facing verification:
redis-cli -p 6380 ping
# Expected: PONG

# April 4 VERIFYANDTEST.sh method:
docker exec jarvis-redis redis-cli ping
# Expected: PONG
```

---

## 35.8 Watchdog Alert Responses

**Memory exhaustion.** Ollama rejects model loads exceeding available memory. The 20llm-production service logs this as a proxy failure and excludes the model from consensus. GPU acceleration reduces peak memory pressure per inference cycle.

**Timeout.** Models exceeding `jarvis-semaphore:8030` timeout (600.0s) are logged as failures and excluded from consensus. GPU inference completes most model cycles in 28–50s, well within the envelope.

**BakLLaVA — FULLY ELIMINATED.** Not in Ollama model registry. Not in source. `.pyc` cache cleared. Zero resource consumption. No alert path exists — the slot is present in compose for continuity only.

**StarCoder2 0-char exclusion.** HTTP 200 but empty responses on community queries. Excluded from consensus extraction. Routing-layer fix tracked — OI pending. Harmonized with Chapter 33 §33.3.

**Session overload.** `MAX_CONCURRENT_CHATS=2` queues requests beyond the second concurrent session.

**BBB content rejection (port 8016, `/filter`, April 4 confirmed).** When content triggers one of the six filters, it is rejected before reaching the LLM ensemble. `content_approved` is the correct response field. `truth_verification` now uses `rag_grounded_v2` logic (OI-37-C, closed April 3, 2026). All filter events are durably logged at `jarvis-memory:8056`.

**BBB output guard — Phase 4.5 log+passthrough.** Currently log+passthrough (commit 18b8ddac) pending recalibration. `bbb_checked: true` reflects that the BBB received and logged the verdict. Full blocking enforcement not yet active. Fail-open on HTTP 500.

**0.0.0.0 exposure detection.** VERIFYANDTEST.sh includes:

```bash
docker ps --format '{{.Names}} {{.Ports}}' | grep 0.0.0.0
```

Any output is a critical security regression. Zero `0.0.0.0` exposures confirmed across 105 containers April 6, 2026.

**GBIM benefit indexer failures.** If a route branch raises an exception, the log-before-result fix ensures `log_to_chroma([], ...)` is called safely. lr=0 for Raleigh/Logan/Cabell/Fayette is a data gap, not a code failure — result is an empty list, no alert generated.

---

## 35.9 Integration with Barriers, Modes, and Containers

**Blood-brain barrier (primary — port 8016).** Every chat request passes through `jarvis-blood-brain-barrier:8016/filter` via the six-filter input stack at Phase 1.4. EthicalFilter endpoint `/filter`, body `{content, actor_role}`, response field `content_approved` (April 4 verified). `truth_verification` now `rag_grounded_v2` per OI-37-C (closed April 3, 2026). Phase 4.5 output in log+passthrough mode pending recalibration. All gate decisions durably logged at `jarvis-memory:8056`.

**Blood-brain barrier (NBB-internal — port 8301).** Operates on the NBB subconscious pathway. Does not participate in the main `ultimatechat` Phase 1.4 / Phase 4.5 pipeline.

**DGM cascade.** Every ensemble response routed through main-brain (port 8050) is validated by `jarvis-69dgm-bridge` at host port 19000 (internal port 9000). Requests sent directly to port 8008 bypass the DGM gate by design.

**Psychology alignment layer.** `jarvis-psychology-services:8019` runs psychological assessment on every request. `psychological_rag` collection: 968 docs.

**NBB subconscious layer.** Seven of eight NBB containers respond to health probes. `nbb_blood_brain_barrier` (port 8301) is one of these. Pituitary gland registers through Redis DynamicPortService.

**Judge pipeline.** All five judge services (ports 7230–7233, 7239) compose-managed with `restart: unless-stopped`. All 5 judge signing keys confirmed present April 4. Judge verdicts delivered as full dict to `jarvis-blood-brain-barrier:8016/output_guard` at Phase 4.5. All verdicts durably logged at `jarvis-memory:8056`.

**Consciousness bridge and brain orchestrator.** The consciousness bridge (`jarvis-consciousness-bridge`) is mandatory infrastructure through which all swarm and watchdog operations flow. The brain orchestrator (`jarvis-brain-orchestrator`) continuously coordinates ensemble, watchdog feedback loops, and neurobiological layer health.

**ChromaDB memory integration.** 47 active collections / 6,722,589 vectors / 12 GB (host port 8002). Includes `zcta_centroids` (829 WV ZCTAs), `psychological_rag` (968 docs), `local_resources` (101 records), `autonomous_learner` (21,181 records — accumulating), `spiritual_texts` (79,181), `gbim_worldview_entities` (5,416,521), and 41 additional collections. `operations_history` automated ingestion not yet active. All scripts must use host port **8002**.

**PostgreSQL integration.** `msjarvis:5433` (5,416,521 GBIM entities, `confidence_decay` metadata) — primary GBIM ground truth. `gisdb:5432` (**45 GB / 548 tables** — Ch. 33 April 6, 2026 ground truth) — geospatial ground truth. `jarvis-local-resources-db:5435` (101 records, all 55 WV counties) — community resources and `conversation_beliefs` target. All databases monitored by VERIFYANDTEST.sh.

**External access perimeter.** Cloudflare tunnel live at `https://egeria.mountainshares.us`. Caddy reverse proxy + `jarvis-auth` enforce authentication. Unauthenticated `/chat` → HTTP 401. Zero `0.0.0.0` exposed ports across all 105 containers.

**`jarvis-memory:8056` durable audit integration.** Durable BBB gate decisions, ChromaDB `dgm_observations` judge verdicts, and PostgreSQL GBIM validation records together constitute the complete, independently queryable governance record for all swarm and watchdog enforcement actions.

---

## 35.10 Summary

Swarm functions and eternal watchdogs in the April 6, 2026 (FINAL) MountainShares Artificial Learning & Location Intelligence deployment are running, verified, and logged against concrete evidence. The 22-slot LLM ensemble delivers 21/22 consensus participation in 99–107 seconds (GPU baseline: RTX 4070) with judge pipeline consistency score of 0.975. The GBIM benefit indexer routes all six community resource modes live — housing, healthcare, fire/EMS, geographic knowledge — with `conversation_beliefs` logged to `local_resources:5435` after every interaction. 829 ZCTA centroids are seeded into ChromaDB, binding every query to a physical ZIP-code location on the Appalachian landscape.

**105 containers, zero exposed ports. 47 ChromaDB collections / 6,722,589 vectors / 12 GB. 829 `zcta_centroids`. 21,181 `autonomous_learner` records. 101 `local_resources` records (all 55 WV counties). 1,115,588 address points. 20,593 landowner spatial rows. Cloudflare tunnel live. Auth enforced. All 5 judge signing keys present. `jarvis-memory` healthy. `preflight_gate.sh`: 31 PASS ❌ 0 FAIL ⚠️ 0 WARN.**

The dual-BBB architecture remains architecturally authoritative: `jarvis-blood-brain-barrier:8016` is the primary judge pipeline output guard — six-filter input stack at Phase 1.4 (EthicalFilter endpoint `/filter`, field `content_approved`, verified April 4; `truth_verification` now `rag_grounded_v2` per OI-37-C, closed April 3, 2026); BakLLaVA FULLY ELIMINATED; StarCoder2 proxied — 0-char on community queries, excluded from consensus scoring; Phase 4.5 output in log+passthrough mode (commit 18b8ddac) pending recalibration; all gate decisions durably logged at `jarvis-memory:8056`. `nbb_blood_brain_barrier:8301` is the NBB-internal neurobiological variant.

The five-layer watchdog system — VERIFYANDTEST.sh (31 PASS 0 FAIL; 8060 check updated to `docker exec jarvis-redis redis-cli ping`), Ollama memory scheduler, `jarvis-semaphore:8030` (max_concurrent: 4, timeout: 600.0), `MAX_CONCURRENT_CHATS=2`, and Redis DynamicPortService (PONG confirmed) — prevents cascade failures and maintains zero `0.0.0.0` exposures across all 105 containers. PostgreSQL `gisdb:5432` is confirmed at **45 GB / 548 tables** (Ch. 33 April 6 ground truth, corrected from 91 GB / 501 tables). The three-layer governance audit record (`jarvis-memory:8056` durable BBB decisions, ChromaDB `dgm_observations` judge verdicts, PostgreSQL GBIM validation) constitutes a complete, independently queryable accountability substrate for Appalachian community intelligence.

**Chapter 35 is FINAL. Chapter 36 pre-conditions are MET. Crystal Coyler Chapter 5 data dependency tracked for lr=0 county resolution.**

---

## Appendix A — Change Record

**★★★★ April 6, 2026 12:59 PM EDT —** Final rewrite and streamline. Corrections applied:
- **35-A** Container count updated **104 → 105** throughout all stamps, Figure 35.1, and §35.7.
- **35-B / 35-G** `msjarvisgis`/`gisdb:5432` corrected from **91 GB / 501 tables → 45 GB / 548 tables** throughout all sections, Figure 35.1 integration points, §35.2 Introduction, §35.9. Port note added to chapter stamp distinguishing production (`5432 / 45 GB / 548 tables`) from rebuild container (`5435`).
- **35-C** BakLLaVA updated from "permanently disabled — name-check guard" to **FULLY ELIMINATED** throughout all sections, Figure 35.1, §35.3, §35.8, and §35.10. Language is now: not in Ollama, not in source, .pyc cache cleared.
- **35-D** `msjarvis:5433` GBIM 5,416,521 entities confirmed — no change needed.
- **35-E** StarCoder2 (8207) status harmonized with Ch. 33 §33.3: **"Proxied — 0-char on community queries, excluded from consensus scoring"** in chapter stamp, Figure 35.1, model tier table, §35.3, and §35.8.
- **35-F** `autonomous_learner: 21,181 records` added to chapter stamp, Figure 35.1 integration points, and §35.9 ChromaDB section.
- **35-H** `truth_verification` BBB filter updated to **`rag_grounded_v2`** per OI-37-C (closed April 3, 2026), superseding `heuristic_contradiction_v1`. Note added to chapter stamp, §35.2, §35.8, and §35.10.

*★ April 4, 2026 — Original seal. RED TEAM GATE OPEN. All 10 preflight issues closed. 104 containers. 45 ChromaDB collections. 829 zcta_centroids. 101 local_resources all 55 WV counties. BELIEFS_DSN corrected. Fire/EMS mismatches fixed. Log-before-result fixed (6 branches). All 6 GBIM benefit indexer routes verified. EthicalFilter endpoint corrected. VERIFYANDTEST.sh 8060 check updated (Redis ping).*

*★ March 28, 2026 — 96/96 containers Up — all previous updates carried forward.*
