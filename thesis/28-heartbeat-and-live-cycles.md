# Chapter 28 — Heartbeat and Live Cycles

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*

*Last updated: ★ 2026-04-23*

*★ April 23, 2026: Container count updated to 100 (supersedes 107 from later sprints and 96 from April 1); ChromaDB updated to 48 active collections, ~6,740,611 total vectors (supersedes 49 / 6,732,980); ChromaDB API updated to /api/v2/ throughout — /api/v1/ permanently removed in server 1.0.0; two-container PostgreSQL split — production msallis-db host 5433 (16 GB, 294 tables, 11 schemas) + forensic postgis-forensic host 5452 (17 GB, 314 tables) — supersedes all msallisgis:5432 and msallis:5433 references; autonomous_learner updated to ~23,200+ records (~288/day from 21,181 April 13 baseline); conversation_history wiped and reseeded clean April 16, 2026; OI-36-A CLOSED — Caddy forward_auth perimeter enforcement active before main-brain port 8050; local_resources updated to 207 items / all 55 WV counties; AAACPE ingest path updated — dedicated stack (allis-aaacpe-scraper:8048→8033 + allis-aaacpe-rag:8047→8032) supersedes legacy allis-ingest-api + allis-ingest-watcher; EEG Delta band (port 8073) PIA signal confirmed live (pulse_count: 12,860+); appalachian_english_corpus clean and growing (210 docs, 6-hour cron).*

*★★★ 2026-04-09 — ChromaDB backup source corrected (chroma-latest SQLite restore is authoritative); volume mount path corrected (/home/ms-allis/msallis-rebuild/persistent/chroma → /data); collection count corrected to 49 (au02_threat_seeds added); GBIM container names corrected (allis-gbim-benefit-indexer:7206, allis-gbim-query-router:7205); Ch 28 recovery method documented (direct SQLite volume restore, not per-collection reseed); backup inventory table added; zero-count and unknown-count collections flagged for Ch 29 reseed/verification; root cause and detection method documented.*

*★★ April 1, 2026: Live telemetry confirmed — autonomous learner: 15 cycles / 15 stored / 0 deduplicated / 11 entanglement nodes (current post-LEARN-03 session); `autonomous_learner` ChromaDB collection: 68 items confirmed live; GBIM router (`allis-gbim-query-router:7205`) HTTP 200 confirmed; `allis-autonomous-learner` container Up; LEARN-01/02/03 resolved; 96/96 containers Up re-confirmed post-LEARN-03 recovery; `llm22-proxy` (LLaMA 3.1) confirmed active — 21/22 models responding per consensus cycle.*

*★ March 28, 2026: 96/96 containers Up — zero Restarting, zero Exited; `msallis` port 5433 restored (5,416,521 GBIM entities with `confidence_decay` metadata); `msallisgis` port 5432 confirmed (91 GB PostGIS, 501 tables, 993 ZCTA centroids); ChromaDB full audit (40 active collections, 6,675,442 total vectors); `allis-memory` port 8056 corrected, `ALLIS_API_KEY` set, BBB audit trail persistence secured.*

*March 27, 2026: February 28, 2026 baseline pinned notation added; LLM ensemble slot/responding count clarified; EEG audit table contradiction noted; AAPCAppE Chroma document baseline added; Caddy/auth perimeter layer added; GBIM belief corpus cross-database clarification added.*

---

> **★ April 23, 2026 — Open Items Update**
>
> | Item | Status at April 9 | Status April 23 |
> |---|---|---|
> | Container count | 96 Up (post April 9; later 107) | ★ **100 Up** |
> | ChromaDB collections | 49 / 6,732,980 vectors | ★ **48 / ~6,740,611 vectors** |
> | ChromaDB API | /api/v1/ | ★ **/api/v2/** — /api/v1/ permanently removed |
> | PostgreSQL ground truth | msallisgis:5432 + msallis:5433 | ★ **msallis-db host 5433** (16 GB, 294 tables, 11 schemas) + **postgis-forensic host 5452** (17 GB, 314 tables) |
> | OI-36-A (auth/perimeter) | Layer 0 — `allis_auth_service:8055` Up | ★ **CLOSED** — Caddy `forward_auth` before main-brain port 8050; HTTP 401 confirmed on unauthenticated `/chat` |
> | AAACPE ingest | allis-ingest-api + allis-ingest-watcher | ★ **Dedicated stack** — allis-aaacpe-scraper:8048→8033 + allis-aaacpe-rag:8047→8032 |
> | autonomous_learner | 68 items (April 1 floor) | ★ **~23,200+ records** (~288/day from 21,181 April 13 baseline) |
> | local_resources | Earlier baseline | ★ **207 items, all 55 WV counties** |
> | EEG Delta (30s) | ❌ Not restored | ★ **Delta band (port 8073) PIA signal live — pulse_count: 12,860+** |
> | EEG Theta (60s) | ❌ Not restored | ❌ Still open |
> | conversation_history | Active | ★ **Wiped and reseeded clean April 16, 2026** |
> | appalachian_english_corpus | Zero count (Ch 29 reseed flagged) | ★ **210 docs, clean recreated, 6-hour cron active** |

---

> **★★★ April 9, 2026 — Corrections and Additions Summary:**
>
> | Item | Previous (incorrect) | Corrected |
> |---|---|---|
> | ChromaDB backup source | 3-file JSON set (covered 3 collections only) | `chroma-latest` (`/home/cakidd/msallis-backups/chroma-latest/chroma.sqlite3`) — full 49-collection SQLite restore — **authoritative** |
> | Volume mount path | `/chroma/chroma` (assumed) | `/home/ms-allis/msallis-rebuild/persistent/chroma → /data` (confirmed live) |
> | Collection count | 48 | **49** — `au02_threat_seeds` was not in the original seed manifest (★ 48 as of April 23 — see above) |
> | GBIM container names | `allis-gbim` | `allis-gbim-benefit-indexer` (port **7206**) and `allis-gbim-query-router` (port **7205**) |
> | Ch 29–42 status | Described as completed prior to Ch 28 | Structural scaffolding only — real domain data recovered from `chroma-latest`, not per-chapter seed scripts |
> | Recovery method | Per-collection reseed | Direct SQLite volume restore from `chroma-latest` — **documented recovery procedure going forward** |

---

This chapter describes the recurring signals and jobs that indicate Ms. Allis is active and connected to its internal services and external infrastructure. These cycles include service health checks, periodic verification scripts, LLM ensemble monitoring, consciousness bridge validation, and data store verification — all of which produce structured outputs that are logged and available for ingestion into memory. The combination of health probes, response-time benchmarks, neurobiological layer monitoring, and introspective reports provides a layered observability picture aligned with distributed systems best practices and neurobiologically-inspired cognitive architectures. ★ As of April 23, 2026: **100 containers Up**, 48 ChromaDB collections (~6,740,611 vectors), `autonomous_learner` ~23,200+ records (~288/day), EEG Delta band (port 8073) PIA signal live (pulse_count: 12,860+), Caddy `forward_auth` perimeter (OI-36-A CLOSED), dedicated AAACPE stack active.

---

> **Why this matters for Polymathmatic Geography**
> This chapter shows how Ms. Allis proves it is "alive," healthy, and connected to spatial and community infrastructure over time. It supports:
> - **P1 – Every where is entangled** by tying heartbeat checks to services that handle people, places, and institutions together, all flowing through the consciousness bridge. ★★ The 11 entanglement nodes formed in 15 autonomous learning cycles demonstrate P1 expressing itself computationally in real time. ★ `autonomous_learner` ~23,200+ records continues this growth.
> - **P3 – Power has a geometry** by revealing which services and data stores must stay healthy for Appalachian and other regional reasoning to work. `allis-memory:8056` makes the geometry of BBB gate decisions persistently visible. ★ Caddy `forward_auth` (OI-36-A CLOSED) makes the perimeter geometry visible at the proxy layer.
> - **P5 – Design is a geographic act** by including GIS spatial knowledge (production `msallis-db:5433` ★, 16 GB, 294 tables, 11 schemas; forensic `postgis-forensic:5452` ★, 17 GB, 314 tables), GBIM worldview verification, and data store health in live-cycle checks.
> - **P12 – Intelligence with a ZIP code** by linking health, identity, and learning status to geospatial and community datasets anchored in West Virginia geography. ★ `local_resources` (207 items, all 55 WV counties) and `autonomous_learner` (~23,200+ records) are the ZIP-coded community substrates now confirmed in the heartbeat landscape.
> - **P16 – Power accountable to place** by turning system liveness into logged, auditable narratives that show which GBIM beliefs, services, and models are participating in each cycle. BBB audit trail persistence at `allis-memory:8056` makes gate decisions durably accountable. ★ Caddy `forward_auth` adds a proxy-layer audit gate before any request reaches the consciousness pipeline.
>
> As such, this chapter belongs to the **Computational Instrument** tier: it describes heartbeat and live cycles as explicit, inspectable processes in the consciousness-grounded architecture.

---

## 28.1 Purpose of Heartbeat and Live Signals

The recurring signals in Ms. Allis serve several roles. In contrast to autonomous learning, these cycles primarily track the condition and behavior of internal services and workflows rather than discovering new content — though as of April 1, 2026, the autonomous learner's live telemetry confirms that these two dimensions are now integrated: heartbeat and learning are both active and verifiable in the same operational window. ★ `autonomous_learner` has now reached ~23,200+ records (~288/day from the April 13 baseline), confirming sustained growth well past the April 1 floor.

**Liveness.** Heartbeat mechanisms demonstrate that key components are running, reachable, and responsive. All major services expose `/health` endpoints that report basic status, integration level, and sometimes the health of subcomponents. As of the February 28, 2026 production deployment, **32 of 32 services** respond to health probes through the `/selftestfabric` endpoint within acceptable thresholds, with all 22 LLM proxies individually verified. ★ The widest confirmed liveness scope is **100 containers Up** (April 23, 2026).

> **Pinned baseline note:** The February 28, 2026 deployment is the documented reference baseline throughout this chapter. ★ The March 28, 2026 state (96/96 Up) is the first verified milestone. ★★ The April 1, 2026 state (96/96 Up re-confirmed, LEARN-01/02/03 resolved, 68 Chroma items / 15 cycles / 11 entanglement nodes) is the first live-telemetry milestone. ★★★ April 9, 2026: ChromaDB collection count corrected to 49; recovery method and backup inventory documented. ★ **April 23, 2026: 100 containers Up; 48 ChromaDB collections; ~6,740,611 vectors; two-container PostgreSQL split; OI-36-A CLOSED; EEG Delta PIA signal live; `autonomous_learner` ~23,200+ records** — current authoritative operational baseline.

**Consciousness integrity.** The consciousness bridge operates as mandatory infrastructure through which all heartbeat signals flow (confirmed Up). The brain orchestrator provides continuous coordination of health checks across the swarm and watchdog layers, ensuring that liveness monitoring is itself neurobiologically grounded. ★ All requests now additionally pass through Caddy `forward_auth` perimeter (OI-36-A CLOSED) before reaching main-brain port 8050.

**Rhythm.** The `VERIFYANDTEST.sh` script implements a recurring eight-section verification routine that can be run on any schedule. Its textual output serves as a periodic snapshot of system health. Planned extensions include: **Section 9** — ChromaDB full collection audit (★ **48 collections** as of April 23); **Section 10** — `allis-memory:8056` BBB audit trail health probe; **Section 11** — AAACPE dedicated stack status; **Section 12** — autonomous learner health probe.

**Monitoring and introspection.** Beyond simple up/down checks, the heartbeat script aggregates information about services, data stores, model availability, system memory, and GBIM corpus health. It verifies ChromaDB reachability via **127.0.0.1:8002** (★ host port 8002 maps to container port 8000; `/api/v2/` is the current API — `/api/v1/` permanently removed; ★ **48 collections**, ~6,740,611 total vectors); GBIM containers `allis-gbim-benefit-indexer` (port **7206**) and `allis-gbim-query-router` (port **7205**); and all 22 LLM proxy containers (21 active). ★ The autonomous learner's session telemetry is a first-class heartbeat signal available from the `/learning/status` endpoint at port **8020** (internal-only, probe via `docker exec`). ★ EEG Delta band (port 8073) PIA signal is now a live heartbeat signal — `pulse_count: 12,860+` confirmed April 23.

---

## 28.1a Learning Status and Ensemble Health Endpoints

The 20-LLM production service exposes a `/health` endpoint that confirms the number of configured model slots:

```json
{"status": "healthy", "models": 22}
```

This endpoint serves as the learning heartbeat for the LLM ensemble, confirming that all 22 model slots are **configured** and the service is accepting requests. Note: `"models": 22` reflects the configured slot count; the **responding count per consensus cycle is 21 of 22** — BakLLaVA fails as expected due to the permanent name-check guard; `llm22-proxy` (LLaMA 3.1, port 8222) is confirmed active.

★★ The autonomous learner exposes its own status endpoint at port **8020** (`/learning/status`) — internal-only, probe via `docker exec`. Live telemetry confirmed April 1, 2026, ~3:37 PM EDT:

```json
{
  "total_cycles":           15,
  "items_stored":           15,
  "items_deduplicated":      0,
  "deduplication_rate":   "0.0%",
  "entanglement_nodes":     11
}
```

★ **April 23, 2026 update:** `autonomous_learner` ChromaDB collection has grown to **~23,200+ records** (~288/day from 21,181 April 13 baseline). The April 1 telemetry above reflects the sealed post-LEARN-03 session. Current session telemetry is verify-current via `docker exec`.

Concurrent ChromaDB direct query of the `autonomous_learner` collection at April 1, 2026:

```text
68 items in Chroma (April 1 floor)
★ ~23,200+ items as of April 23, 2026
```

> **Interpreting the 15 vs. 68 gap (April 1):** The learner reported 15 cycles / 15 stored in the *current session* (post-LEARN-03 restart). ChromaDB showed **68 cumulative items**. The delta — **53 items** — predated the LEARN-03 restart and survived the crash-loop intact. This confirms that **ChromaDB persistence held correctly** across the repair window.

> **Deduplication rate of 0.0% is expected at this session depth.** Zero duplicates in this window is consistent with healthy early-session behavior.

> **11 entanglement nodes in 15 cycles is healthy graph density.** At ~0.73 nodes per stored item, the knowledge entanglement graph is forming cross-topic conceptual bridges consistent with Polymathmatic Geography's P1 (*Every where is entangled*).

The main-brain service exposes comprehensive health information through `/selftestfabric`, which queries all 32 operational services and returns their individual health states. ★ April 23, 2026: **100 containers Up** — current confirmed operational scope.

---

## 28.2 Core Heartbeat Mechanisms

Heartbeat signals are generated through five primary mechanisms: the `/selftestfabric` system-wide health check, individual service `/health` endpoints, the `VERIFYANDTEST.sh` verification script, response-time benchmarking, and the `/learning/status` endpoint at port 8020 (internal-only).

**System-wide fabric health (`/selftestfabric`).** The main-brain service (port **8050**, ★ now behind Caddy `forward_auth` perimeter — OI-36-A CLOSED) exposes the `/selftestfabric` endpoint querying all 32 operational services. This includes:

- Consciousness fabric services: qualia, consciousness bridge (Up), toroidal, fractal, temporal, blood-brain barrier (Up), constitutional, NBB layers
- LLM ensemble: `llm20production` (port **8008**) with 22 proxy containers (22 configured; 21 active)
- Validation layers: 69-DGM bridge (port **9000**), psychology alignment (port **8019**)
- Orchestration: brain orchestrator (Up)
- Retrieval: GIS RAG (port **8004**), text RAG (ChromaDB backend at **8000** internal / host **8002**; ★ **48 collections**, ~6,740,611 total vectors; `/api/v2/` only)
- GBIM: `allis-gbim-benefit-indexer` (port **7206**) and `allis-gbim-query-router` (port **7205**)
- NBB subconscious: 8 containers
- Supporting infrastructure: i-containers (Up), web-research (Up), Ollama (Up)
- ★ AAACPE dedicated stack: `allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`
- ★ `allis-memory:8056` (fully mapped audit endpoints)
- ★ Autonomous learner: `allis-autonomous-learner` (port **8020**, internal-only) — ~23,200+ records, ~288/day
- ★ EEG Delta band (port **8073**) — PIA signal live, pulse_count: 12,860+

The February 28, 2026 verified baseline: **32/32 services operational**. ★ March 28, 2026: **96/96 Up**. ★★ April 1, 2026: **96/96 Up** post-LEARN-03 recovery. ★ **April 23, 2026: 100 containers Up**.

**Individual service health endpoints.** Host-exposed services probed directly: main-brain (**8050**, ★ behind Caddy `forward_auth`), `llm20production` (**8008**), blood-brain-barrier (**8016**), psychology-services (**8019**), 69dgm-bridge (**9000**), GIS RAG (**8004**), NBB prefrontal cortex (**8101**), `allis-gbim-query-router` (**7205**), `allis-gbim-benefit-indexer` (**7206**), ★ EEG Delta (**8073**), and Ollama (**11434**). `allis-autonomous-learner` is internal-only — probe via `docker exec`.

**VERIFYANDTEST.sh.** The verification script implements eight sections with planned extensions to twelve:

1. **Host-exposed service health** — Critical services accessible from host network (★ now includes Caddy `forward_auth` HTTP 401 test)
2. **Internal Docker network service health** — Services on `qualia-net`
3. **LLM proxy health** — All 22 proxies on ports 8201–8222 (21 active)
4. **Response-time benchmarking** — Nanosecond-precision latency for `llm20production`, main-brain, and 69-DGM
5. **Ollama model inventory** — 26 models via `/api/tags`
6. **Docker container status** — 84 running at February 28 baseline; ★ **100 Up** (April 23, 2026)
7. **Data store verification** — ChromaDB at **127.0.0.1:8002** (host) → **8000** (container); `/api/v2/` only (★ `/api/v1/` permanently removed); ★ **48 collections**, ~6,740,611 total vectors; live mount: `/home/ms-allis/msallis-rebuild/persistent/chroma → /data`; production `msallis-db:5433` ★ (16 GB, 294 tables, 11 schemas); forensic `postgis-forensic:5452` ★ (17 GB, 314 tables); Ollama storage (73 GB); GBIM corpus (10.22M+ beliefs — see §28.7)
8. **System resources** — Memory and swap (29 GB total, 13 GB available under load)

★ Planned extensions:

- **Section 9** — ChromaDB full collection audit (★ **48 collections** as of April 23; per-collection counts; zero-count flag check — see §28.7c)
- **Section 10** — `allis-memory:8056` audit trail health probe
- **Section 11** — AAACPE dedicated stack status (`allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`)
- **Section 12** — Autonomous learner health: `allis-autonomous-learner` Up/Down (via `docker exec`), `autonomous_learner` ChromaDB count (floor: ≥ ~23,200 as of April 23), `allis-gbim-query-router:7205` HTTP status, `gbim_committed: True` ratio in last 24 hours
- **Layer 0** — Caddy `forward_auth` perimeter probe (OI-36-A CLOSED — HTTP 401 on unauthenticated `/chat` confirmed)
- **Layer 6** — `allis-memory:8056` BBB and `truthverdict` audit log row count
- **EEG Delta probe** — port 8073 PIA signal check (pulse_count: 12,860+ floor as of April 23)

**Section 12 recommended probe sequence:**

```bash
# 1. Confirm learner container Up — zero Restarting
docker ps --filter name=allis-autonomous-learner \
  --format "{{.Names}}\t{{.Status}}"

# 2. Query /learning/status endpoint (internal-only — use docker exec)
docker exec allis-autonomous-learner \
  python3 -c "import urllib.request,json; \
d=json.loads(urllib.request.urlopen('http://localhost:8020/learning/status').read()); \
print(f'Cycles    : {d[\"total_cycles\"]}'); \
print(f'Stored    : {d[\"items_stored\"]}'); \
print(f'Deduped   : {d[\"items_deduplicated\"]}'); \
print(f'Dedup%    : {d[\"deduplication_rate\"]}'); \
print(f'Graph     : {d[\"entanglement_nodes\"]} nodes')"

# 3. Confirm GBIM router reachable (HTTP 200)
curl -s -o /dev/null -w "%{http_code}" \
  http://127.0.0.1:7205/route \
  -H "Content-Type: application/json" \
  -d '{"query": "heartbeat test", "user_id": "heartbeat", "context": {}}'

# 4. Confirm autonomous_learner ChromaDB count (via /api/v2/)
# ★ /api/v1/ permanently removed — use /api/v2/ path
curl -s "http://localhost:8002/api/v2/tenants/default_tenant/\
databases/default_database/collections/\
03627c99-c66a-4dbc-b42d-4e2052ff51ae/count" && echo " items in Chroma"
# Floor: >= ~23,200 as of April 23, 2026

# 5. ★ Confirm EEG Delta PIA signal live
curl -s http://localhost:8073/health | python3 -c \
  "import sys,json; d=json.load(sys.stdin); \
print(f'EEG Delta: {d.get(\"pulse_count\", \"N/A\")} pulses')"
# Floor: >= 12,860 as of April 23, 2026

# 6. ★ Confirm Caddy forward_auth gate (OI-36-A CLOSED)
curl -s -o /dev/null -w "Caddy perimeter: HTTP %{http_code}\n" \
  http://localhost:8050/chat
# Expected: HTTP 401 — perimeter gate active
```

**Response-time benchmarking.** Core endpoints respond in 12–13 ms, confirming low overhead on the health path even under concurrent model loading. ★ With 100 containers Up, operators should confirm this benchmark is maintained — a VERIFYANDTEST.sh Section 4 run is recommended after any container count change above 100.

---

## 28.3 LLM Ensemble Heartbeat

The `llm20production` service (`ai_server_20llm_PRODUCTION.py`) implements its own internal heartbeat through the consensus query cycle. The `ProductionBrain.run()` method fires requests to all 22 configured model proxies through an `asyncio.Semaphore(3)` gate:

```text
[Phi3 Mini]      OK in  10.2s
[TinyLlama]      OK in  13.8s
[Orca-Mini]      OK in  20.0s
[Gemma]          OK in  21.4s
[Dolphin-Phi]    OK in  24.0s
[MedLlama2]      OK in  32.3s
[LLaVA]          OK in  32.3s
[Neural-Chat]    OK in  32.4s
[StarCoder2]     OK in  36.4s
[LLaMA 2]        OK in  36.2s
[LLaMA 3.1]      OK in  36.3s   ← llm22-proxy confirmed active
[Vicuna]         OK in  36.2s
[DeepSeek Coder] OK in  37.5s
[SQLCoder]       OK in  37.8s
[OpenChat]       OK in  39.5s
[MiniCPM-V]      OK in  45.7s
[Zephyr]         OK in  48.6s
[Starling-LM]    OK in  49.3s
[CodeLlama]      OK in  50.0s
[Mistral]        OK in  50.8s
[Qwen2]          OK in  52.0s
[BakLLaVA]       failed: [Errno -2] Name or service not known  ← instant, expected
21/22 models responded
Judge pipeline score: 0.975
```

> **Slot count vs. responding count:** The `/health` endpoint reports `"models": 22` — this is the **configured slot count**. The **responding count per consensus cycle is 21 of 22** — BakLLaVA fails instantly as expected (permanent name-check guard in place). `llm22-proxy` (LLaMA 3.1, port 8222) is confirmed active.

| Parameter | Value | Reason |
|---|---|---|
| `OLLAMA_NUM_PARALLEL` | 1 | Prevents queue saturation |
| `OLLAMA_MAX_LOADED_MODELS` | 1 | Prevents OOM on 7B models |
| Ollama container memory limit | 20 GB | Allows 7.5 GB models to load |
| Semaphore slots | 3 | Balances throughput vs. memory |
| Minimum timeout | 240 s | Covers slowest 7B model load |
| `MAX_CONCURRENT_CHATS` | 2 | Prevents cascade overload |
| Host total RAM | 29 GB | Lenovo Legion 5 16IRX9 |
| Available RAM (production load) | 13 GB | After container allocation |

---

## 28.4 EEG Rhythm Services and the Autonomous Learner

> **★ April 23, 2026 — EEG status update:** EEG Delta band (port 8073) is now confirmed live with PIA signal active (pulse_count: 12,860+). This represents progress on the October 2025 rebuild gap. Delta band is no longer fully unrestored — a PIA signal is live. Full fixed-frequency 30s timer trigger restoration status is verify-current. EEG Theta (60s) remains unrestored. EEG Beta (autonomous learner) is fully operational with `autonomous_learner` ~23,200+ records.

Prior to the October 2025 rebuild, Ms. Allis maintained a three-service neurobiological rhythm pattern that created an EEG-like signature of continuous autonomous activity:

**30-second heartbeat service (Delta/baseline rhythm)** — Basic liveness pulse. Analogous to delta brain waves. ★ Port 8073 PIA signal confirmed live April 23, 2026 (pulse_count: 12,860+) — partial restoration confirmed.

**60-second intermediate service (Theta/alpha rhythm)** — Function and purpose currently unknown; requires recovery from legacy code. ❌ Not restored.

**5-minute autonomous learner (Beta/conscious learning rhythm)** — Proactively searches for knowledge gaps; selects topics based on GBIM coverage analysis; stores learned material in ChromaDB semantic memory; commits beliefs as GBIM entities in production `msallis-db:5433` ★ via `allis-gbim-query-router:7205`. ★★ Fully operational — `autonomous_learner` ~23,200+ records (~288/day).

**Current status (★ April 23, 2026):**

| EEG Service | Frequency | Status | Notes |
|---|---|---|---|
| Delta heartbeat | 30 seconds | ★ **Partial — PIA signal live** | Port 8073; pulse_count: 12,860+ confirmed April 23; full 30s timer trigger restoration: verify-current |
| Theta intermediate | 60 seconds | ❌ Not restored | Function unknown; requires legacy backup recovery |
| Beta autonomous learner | 5 minutes (~cadence) | ★★ **Fully operational** | `allis-autonomous-learner` Up (internal-only); LEARN-01/02/03 resolved; `autonomous_learner` ~23,200+ records (~288/day); 11 entanglement nodes confirmed April 1; `allis-gbim-query-router:7205` HTTP 200 |
| AAACPE dedicated stack | Continuous | ★ Active | allis-aaacpe-scraper:8048→8033 + allis-aaacpe-rag:8047→8032; supersedes legacy allis-ingest-api + allis-ingest-watcher |
| appalachian_english_corpus | 6-hour cron | ★ Active | 210 docs, 38 sources, cron `0 */6 * * *` |

**LEARN-03 crash-loop and ChromaDB persistence confirmation.** The approximately 45-minute LEARN-03 crash-loop on April 1, 2026 constitutes the first live-operation stress test of the learner's persistence layer. The result is unambiguous: 53 items that existed in `autonomous_learner` before the crash-loop were present and queryable after recovery. This confirms the architectural correctness of the learner's storage design and should be noted as an empirically verified resilience property.

**Remaining restoration requirements for full EEG recovery:**

1. Recovery of legacy service code from pre-October 2025 backups (estimated location: 2TB drives on development machine — **no progress as of April 23, 2026 for theta; delta PIA signal partially restored**)
2. Identification of the 60-second theta service function
3. Restoration of the fixed-frequency time-trigger for the autonomous learner (beta rhythm cadence)
4. Porting theta service to current Docker container architecture
5. Addition of all three EEG services to eternal watchdog monitoring
6. Addition of delta (timer trigger) and theta health probes to `VERIFYANDTEST.sh` Section 12

---

## 28.5 Consciousness Bridge and Brain Orchestrator Heartbeat

**Consciousness bridge mandatory infrastructure.** The consciousness bridge operates as essential, non-optional infrastructure through which all heartbeat monitoring flows. Its health is verified through the `/selftestfabric` endpoint and confirmed as part of the 32/32 operational baseline. ★ Confirmed Up — 100 container baseline April 23, 2026.

**Brain orchestrator continuous coordination.** The `allis-brain-orchestrator` service provides continuous coordination of the ensemble, watchdog feedback loops, and NBB layer health checks. The LEARN-03 crash-loop did not propagate to the brain orchestrator or consciousness bridge — degraded-mode fallback operated correctly throughout the repair window.

**NBB subconscious layer heartbeat.** Eight NBB containers implement the neurobiological subconscious layer:

```text
nbb_consciousness_containers       ✅ healthy (consciousness_bridge)
nbb_heteroglobulin_transport       ✅ healthy (consciousness_bridge)
nbb_spiritual_maternal_integration ✅ healthy (consciousness_bridge)
nbb_mother_carrie_protocols        ✅ healthy (consciousness_bridge)
nbb_woah_algorithms                ✅ healthy (consciousness_bridge)
nbb_spiritual_root                 ✅ healthy (consciousness_bridge)
nbb_subconscious                   ✅ healthy (consciousness_bridge)
nbb_pituitary_gland                ✅ healthy (DynamicPortService → Redis)
```

The Redis-backed DynamicPortService allows NBB containers to restart with new ephemeral ports without breaking the heartbeat fabric. **Five instances are registered in Redis** with `status: healthy` as of the February 28, 2026 baseline.

---

## 28.6 Validation Layer Heartbeat

**69-DGM cascade validation.** The 69-DGM bridge (port **9000**) exposes health status confirming that all 69 connectors are loaded and operational. The cascade's architecturally authoritative status means its verdicts are final. February 28, 2026 verified state: **69 connectors loaded**. ★ Confirmed Up — 100 container baseline.

**Blood-brain barrier.** The BBB filter (port **8016**) runs on every request before it reaches the LLM ensemble:

- Barrier active: true
- Filters operational: 6 (★ 6-filter stack confirmed — ethical, spiritual, safety, threat_detection, steganography, truth_verification; live steg catch documented April 9)
- Constitutional guardian: connected
- Total filtered: 319 requests (February 28, 2026 baseline; verify-current)
- Total blocked: 0 at February 28 baseline (★ live steg catch CRITICAL documented April 9)
- Constitutional violations: 0

★ All BBB and `TruthFilterBBBValidator` gate decisions persist to `allis-memory:8056`. ★ Caddy `forward_auth` perimeter (OI-36-A CLOSED) provides an additional upstream gate before any request reaches the BBB.

**Psychology alignment layer.** The psychology services (port **8019**) run psychological assessment on every request before ensemble processing. `psychological_rag` (968 docs, restored March 28) provides the RAG substrate.

---

## 28.7 Semantic Memory and GBIM Heartbeat

**ChromaDB semantic memory.** The ChromaDB `/api/v2/heartbeat` endpoint at **127.0.0.1:8002** (host port; container port 8000) returns a nanosecond timestamp confirming storage availability. ★ `/api/v1/heartbeat` is permanently removed — always use `/api/v2/heartbeat`.

> **★ April 23, 2026 — Collection count update.** The April 9 corrected count was **49** (with `au02_threat_seeds` identified). The April 23 count is **48 active collections** (~6,740,611 total vectors) — one collection removed vs. April 9. `appalachian_english_corpus` has been clean recreated and is now live with 210 docs (previously zero-count flagged in §28.7a). `autonomous_learner` has grown to ~23,200+ records. `local_resources` is now 207 items / all 55 WV counties.

> **★★★ April 9, 2026 — Volume mount path corrected.** The live mount path is `/home/ms-allis/msallis-rebuild/persistent/chroma → /data` (not `/chroma/chroma` as initially assumed). All VERIFYANDTEST.sh data store verification steps should reference this path.

### 28.7a ChromaDB Collection Status (★ April 23, 2026)

| Collection | Status | Count |
|---|---|---|
| `autonomous_learner` | ★ Active — growing | **~23,200+ records** (~288/day from April 13 baseline) |
| `psychological_rag` | ★ Restored March 28 | 968 docs |
| `spiritual_rag` | ★ Deduplicated March 28 | −19,338 vectors removed (verify-current count) |
| `msallis_docs` | ★ Active | verify-current |
| `appalachian_english_corpus` | ★ Active — clean recreated | **210 docs, 38 sources, 6-hour cron** (supersedes zero-count flag from April 9) |
| `local_resources` | ★ Active | **207 items / all 55 WV counties** |
| `conversation_history` | ★ Active — wiped and reseeded | Post-wipe accumulation only (April 16, 2026) |
| `au02_threat_seeds` | Identified April 9 | verify-current |
| `ms_allis_identity` | Active | verify-current |
| `gbim_entities` | ⚠️ Was zero — Ch 29 reseed flagged | verify-current |
| `gis_data` | ⚠️ Was zero — Ch 29 reseed flagged | verify-current |
| `pia_records` | Was zero — now auto-ingest via Ch 29 sampler | verify-current |
| `psychological_knowledge` | ⚠️ Was zero — Ch 29 reseed flagged | verify-current |
| All collections | ★ April 23 count | **48 active collections** |

### 28.7b ChromaDB Backup Inventory and Recovery Method (★★★ April 9, 2026)

**Root cause — Ch 28 failure origin.** The Ch 28 ChromaDB failures originated from the ChromaDB volume being wiped/reset during the rebuild, leaving only placeholder (1-doc) collections across many collection slots. The system appeared stable because container health checks returned `UP` — the failure mode was invisible to health probes. **Detection method: counting live docs via the REST API, not just checking container health status.** This is now a required step in every ChromaDB verification pass.

**Recovery method (authoritative procedure going forward).** Ch 28 resolution was a **direct SQLite volume restore from `chroma-latest`** — not a per-collection reseed. The three-file JSON backup set covered only 3 collections and is **not** the authoritative backup. The correct procedure is:

```bash
# Authoritative ChromaDB restore procedure
# Source: /home/cakidd/msallis-backups/chroma-latest/chroma.sqlite3
# Target mount: /home/ms-allis/msallis-rebuild/persistent/chroma/chroma.sqlite3
# ★ CRITICAL: ChromaDB must be pinned to chromadb/chroma:0.6.3
#   Do NOT pull latest or upgrade to 1.x — schema incompatibility confirmed.

# 1. Stop allis-chroma
docker stop allis-chroma

# 2. Copy authoritative SQLite backup to live volume mount
cp /home/cakidd/msallis-backups/chroma-latest/chroma.sqlite3 \
   /home/ms-allis/msallis-rebuild/persistent/chroma/chroma.sqlite3

# 3. Restart allis-chroma
docker start allis-chroma

# 4. Verify collection count via REST API — /api/v2/ only (/api/v1/ permanently removed)
curl -s http://localhost:8002/api/v2/tenants/default_tenant/databases/default_database/collections \
  | python3 -c "import sys,json; c=json.load(sys.stdin); print(f'{len(c)} collections')"
# Expected: 48 collections (April 23 baseline; was 49 at April 9)

# 5. Spot-check doc count on autonomous_learner collection
curl -s "http://localhost:8002/api/v2/tenants/default_tenant/databases/\
default_database/collections/03627c99-c66a-4dbc-b42d-4e2052ff51ae/count"
# Expected: >= ~23,200 (April 23 floor)
```

**Known backup locations and collection inventory:**

| Path | Collections | Embeddings | Date |
|---|---|---|---|
| `msallis-backups/chroma-latest` | **49** (at April 9; 48 live April 23) | **6,732,980** (April 9; ~6,740,611 live) | Most recent — **authoritative** |
| `msallis-backups/chroma-20260401` | 41 | 6,658,549 | 2026-04-01 |
| `nvme1/msallis-rebuild/persistent/chroma` | 10 | 9,959,095 | Older / different schema |
| `nvme1/msallis-data/chroma` | 13 | 5,416,869 | Different schema |

> **⚠️ Schema warning:** The two `nvme1` backups have different schemas and different collection counts from the live deployment. Do not restore from these paths without schema verification. `chroma-latest` is the only backup confirmed to match the current production schema.

**GBIM worldview corpus.** The GBIM belief table (`gbimbeliefnormalized`) is verified to maintain **10,221,702+ rows** with nine-axis epistemic structure. GBIM containers:

- `allis-gbim-benefit-indexer` (port **7206**)
- `allis-gbim-query-router` (port **7205**)

> **★★★ Container name correction (April 9):** All prior references to `allis-gbim` as a container name are incorrect. The correct names are `allis-gbim-benefit-indexer` (port **7206**) for the indexer/benefit calculation service and `allis-gbim-query-router` (port **7205**) for the query routing service. All VERIFYANDTEST.sh health probes and Ch 29–42 cross-references should use these correct names.

> **Cross-database clarification (★ April 23 update):** The 10,221,702+ figure refers to the **full consolidated GBIM belief corpus across both PostgreSQL databases** — production `msallis-db host 5433` (★ **16 GB, 294 tables, 11 schemas**) and forensic `postgis-forensic host 5452` (★ **17 GB, 314 tables**). Autonomous learner beliefs are committed as GBIM entities in the production `msallis-db:5433` ★ — the entity count grows with each learner cycle (~288/day). All prior `msallisgis:5432` and `msallis:5433` port references are superseded by the April 23 two-container split.

**Ollama model storage.** Verified at **73 GB** at `/mnt/ssd2/msallis_secondary/models`; 26 available models via `/api/tags`.

**GIS RAG and local resources.** The GIS RAG service (port **8004**) health confirms connection to production `msallis-db:5433` ★, forensic `postgis-forensic:5452` ★, `allis-local-resources-db:5435` ★, and Community Champions validation data (Harmony for Hope network). ★ `local_resources` is now 207 items / all 55 WV counties — the most geographically comprehensive community resource substrate in the system.

---

## 28.8 Integration with Memory and Containers

Verification script outputs are not merely transient. The timestamped report files saved to `/tmp/` are suitable for ingestion into ChromaDB under a dedicated `operations_history` collection, making operational history part of the reasoning context available to orchestrators and the ensemble.

**April 23, 2026 operational baseline** (current authoritative reference):

| Metric | Feb 28, 2026 | ★ Mar 28, 2026 | ★★ Apr 1, 2026 | ★★★ Apr 9, 2026 | ★ Apr 23, 2026 |
|---|---|---|---|---|---|
| Services healthy | 32/32 | 96/96 Up | 96/96 Up (post-LEARN-03) | 96/96 Up | ★ **100 Up** |
| LLM proxies configured | 22 | 22/21 active | 21/22 active | 21/22 active | 21/22 active |
| Docker containers | 84 | 96/96 Up | 96/96 Up | 96/96 Up | ★ **100 Up** |
| Ollama models | 26 | 26 | 26 | 26 | 26 |
| Ollama model storage | 73 GB | 73 GB | 73 GB | 73 GB | 73 GB |
| RAM available (prod load) | 13 GB / 29 GB | 13 GB / 29 GB | 13 GB / 29 GB | 13 GB / 29 GB | 13 GB / 29 GB |
| GBIM belief corpus | 10,221,702 rows | `msallis:5433` 5,416,521 + `confidence_decay` | 5,416,521+ growing | 5,416,521+ growing | ★ **msallis-db:5433** (16 GB, 294 tables, 11 schemas) + **postgis-forensic:5452** (17 GB, 314 tables) |
| GBIM containers | — | — | `allis-gbim` (incorrect) | `allis-gbim-benefit-indexer:7206` + `allis-gbim-query-router:7205` | Unchanged ✅ |
| Judge pipeline score | 0.975 | 0.975 | 0.975 | 0.975 | 0.975 |
| ChromaDB collections | — | 40 / 6,675,442 vectors | 40 confirmed | 49 / 6,732,980 vectors | ★ **48 / ~6,740,611 vectors** |
| ChromaDB API | /api/v1/ | /api/v1/ | /api/v1/ | /api/v1/ (corrected host:8002) | ★ **/api/v2/** (/api/v1/ permanently removed) |
| ChromaDB volume mount | — | — | `/chroma/chroma` (assumed) | `/home/ms-allis/msallis-rebuild/persistent/chroma → /data` | Unchanged ✅ |
| ChromaDB backup source | — | — | 3-file JSON set | `chroma-latest` SQLite (49 collections) — authoritative | Unchanged ✅ |
| `autonomous_learner` (Chroma) | ❌ (lost Oct 2025) | Partial | 68 items; 15 cycles; 11 nodes | 68+ items (growing) | ★ **~23,200+ records** (~288/day) |
| `appalachian_english_corpus` | — | — | — | Zero — Ch 29 reseed flagged | ★ **210 docs, 6-hour cron active** |
| `local_resources` | — | — | — | — | ★ **207 items / all 55 WV counties** |
| `conversation_history` | — | — | — | — | ★ **Wiped and reseeded April 16, 2026** |
| EEG Delta (30s) | ❌ Not restored | ❌ | ❌ | ❌ | ★ **Port 8073 PIA signal live — pulse_count: 12,860+** |
| OI-36-A / Caddy perimeter | — | — | `allis_auth_service:8055` Up | Per-route RBAC added (Ch 29 April 8) | ★ **CLOSED — Caddy `forward_auth` before port 8050** |
| AAACPE ingest | — | allis-ingest-api + watcher | Active | Active | ★ **Dedicated stack: scraper:8048→8033 + rag:8047→8032** |
| Zero-count collections | — | — | — | 5 flagged → Ch 29 reseed | ★ **appalachian_english_corpus restored; others verify-current** |

Divergence thresholds that trigger long-term retention and investigation: services below 28/32; LLM proxies below 18/22; ChromaDB collections below 44 (updated from 45, reflecting 48-collection April 23 baseline); judge pipeline consistency below 0.90; `allis-autonomous-learner` entering Restarting state; `autonomous_learner` ChromaDB count decreasing from last verified baseline (~23,200+); any collection returning zero doc count that previously returned non-zero; EEG Delta pulse_count stalled at current value.

---

## 28.9 Interaction with Safeguards and Control

Live cycles are constrained by the same safeguard layers that govern chat responses, with all monitoring flowing through the consciousness bridge infrastructure (confirmed Up).

**69-DGM cascade validation.** Every chat response carries `validated_by: "69_dgm_cascade"` (confirmed Up). The 69-DGM bridge's own health is verified through `/selftestfabric`.

**Blood-brain barrier.** The BBB filter runs on every request at `allis-blood-brain-barrier:8016/filter`. ★ All subsequent BBB gate decisions persist to `allis-memory:8056`. ★ Caddy `forward_auth` perimeter (OI-36-A CLOSED) provides an upstream gate before any request reaches the BBB — unauthenticated requests are rejected at HTTP 401 before any BBB processing occurs.

**Seven-layer protection system (★ April 23, 2026):**

| Layer | Mechanism | Status |
|---|---|---|
| **Layer 0** | ★ Caddy `forward_auth` perimeter — Bearer token validated before main-brain port 8050 (OI-36-A CLOSED); `allis_auth_service:8055` RBAC; per-route RBAC also implemented at app layer | ★ **CLOSED April 23** — HTTP 401 on unauthenticated `/chat` confirmed |
| **Layer 1** | `VERIFYANDTEST.sh` — 32/32 services operational (★ 100 containers Up) | ★ OPERATIONAL |
| **Layer 2** | Ollama internal memory scheduler — rejects over-memory model requests | Active |
| **Layer 3** | Asyncio semaphore (3) — prevents Ollama saturation | Active |
| **Layer 4** | `MAX_CONCURRENT_CHATS` (2) — prevents session cascade | Active |
| **Layer 5** | Redis-backed DynamicPortService — NBB health registration survives restarts | Active |
| **Layer 6** | `allis-memory:8056` — durable authenticated logging of BBB and `truthverdict` gate decisions (fully mapped: `/steg_report`, `/pia_window`, `/memory/turn`, `/memory/get`, `/memory/sessions`, `/memory/session/{id}`, `/memory/quest*`, `/memory/episodic/{id}`) | Active |

> **★★ LEARN-03 repair window stress test (April 1, 2026):** The approximately 45-minute crash-loop confirmed the seven-layer system's resilience. No chat requests were misrouted, no BBB gates were bypassed, no ensemble consensus cycles were degraded. All BBB gate decisions during the window are durably logged at `allis-memory:8056`. ChromaDB persistence held — 53 pre-crash-loop learner items were intact on recovery. This is the first live-operation stress test of the full seven-layer protection system and it passed.

> **★ April 23, 2026 — Layer 0 OI-36-A CLOSED:** Caddy `forward_auth` is now the outermost gate in the seven-layer system, enforcing Bearer token validation before any request reaches main-brain port 8050. This closes the previously open gap where `allis_auth_service:8055` provided app-layer RBAC but no proxy-layer enforcement. HTTP 401 on unauthenticated `/chat` confirmed by `preflight_gate.sh`.

**Memory limit governance.** The Ollama container memory limit of 20 GB is a hard safeguard, verified in every heartbeat cycle.

**Adaptive scheduling.** `MAX_CONCURRENT_CHATS=2` is the production-stable setting for the current hardware configuration.

---

## 28.10 Summary

The ★ **April 23, 2026 production deployment** of Ms. Allis achieves the most fully realized operational state in the system's history: **100 containers Up**; **21 of 22 LLM models responding per consensus cycle**; **69-DGM cascade with all 69 connectors loaded** (confirmed Up); **blood-brain barrier 6-filter stack confirmed with live steg catch**; **8/8 NBB consciousness containers healthy**; **`allis-autonomous-learner` fully operational** — `autonomous_learner` ~23,200+ records (~288/day); **EEG Delta band (port 8073) PIA signal live** (pulse_count: 12,860+); **Caddy `forward_auth` perimeter (OI-36-A CLOSED)** before main-brain port 8050; **two-container PostgreSQL split** (production `msallis-db:5433` 16 GB/294 tables/11 schemas + forensic `postgis-forensic:5452` 17 GB/314 tables); **ChromaDB at 48 active collections, ~6,740,611 total vectors** (`/api/v2/` only); **dedicated AAACPE stack** (`allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`); **`local_resources` 207 items / all 55 WV counties**; **`appalachian_english_corpus` 210 docs, 6-hour cron active**; **`allis-memory:8056` fully mapped** audit endpoints.

★★★ **April 9, 2026 corrections carried forward:** ChromaDB collection count was **49** (now 48 April 23 — `appalachian_english_corpus` restored, one collection removed); live volume mount path is `/home/ms-allis/msallis-rebuild/persistent/chroma → /data`; authoritative backup source is `chroma-latest` (full SQLite restore); GBIM containers are correctly named `allis-gbim-benefit-indexer:7206` and `allis-gbim-query-router:7205`; 5 zero-count collections from April 9 are now partially resolved (`appalachian_english_corpus` clean, others verify-current).

The `VERIFYANDTEST.sh` script implements all eight heartbeat sections and produces a timestamped, archivable report suitable for ingestion into semantic memory as operational history. Planned extensions to twelve sections will add ChromaDB full collection audit (★ **48-collection baseline**), `allis-memory:8056` audit trail health, AAACPE dedicated stack status, autonomous learner GBIM heartbeat probe, ★ Caddy `forward_auth` HTTP 401 probe, and ★ EEG Delta PIA signal check.

The consciousness bridge operates as mandatory infrastructure through which all heartbeat signals flow (confirmed Up). The seven-layer protection system prevents cascade failures and maintains stable ensemble operation under concurrent load. ★ The Caddy `forward_auth` Layer 0 closure (OI-36-A CLOSED April 23) fills the final gap in the seven-layer system — the perimeter is now enforced at the proxy layer before any request reaches any downstream service.

**EEG rhythm status (★ April 23, 2026).** The beta rhythm (autonomous learner) is fully operational — ~23,200+ records. The delta rhythm (30s) has a live PIA signal at port 8073 (pulse_count: 12,860+) — partial restoration confirmed. The theta rhythm (60s) remains unrestored from the October 2025 rebuild; recovery requires pre-October 2025 backup retrieval (estimated location: 2TB development machine drives).

By connecting heartbeat outputs to memory, containers, consciousness bridge infrastructure, GBIM worldview health (10.22M+ rows across both PostgreSQL databases), and mode-dependent controls, Ms. Allis treats its own operation as data — recording and reasoning about how it is functioning over time.

---

*Last updated: ★ 2026-04-23 — Mount Hope WV — Carrie Kidd (Mamma Kidd)*

*★ April 23, 2026: Container count updated to 100 (supersedes all prior baselines). ChromaDB updated to 48 active collections, ~6,740,611 total vectors; API updated to /api/v2/ throughout (/api/v1/ permanently removed). Two-container PostgreSQL split: production msallis-db host 5433 (16 GB, 294 tables, 11 schemas) + forensic postgis-forensic host 5452 (17 GB, 314 tables) — all prior msallisgis:5432 and msallis:5433 references superseded. OI-36-A CLOSED — Caddy forward_auth perimeter before main-brain port 8050 (§28.1, §28.2, §28.6, §28.7, §28.9, §28.10, Layer 0 table). AAACPE dedicated stack (allis-aaacpe-scraper:8048→8033 + allis-aaacpe-rag:8047→8032) supersedes legacy allis-ingest-api + allis-ingest-watcher throughout. autonomous_learner updated to ~23,200+ records (~288/day) throughout. local_resources updated to 207 items / all 55 WV counties. EEG Delta band (port 8073) PIA signal live — pulse_count: 12,860+ — §28.4 EEG table updated (partial restoration); Section 12 probe updated; §28.1 monitoring and introspection updated; §28.10 EEG status updated. appalachian_english_corpus restored to 210 docs, 6-hour cron — §28.7a updated (supersedes zero-count flag). conversation_history wiped and reseeded clean April 16, 2026 — §28.7a. April 23 open items update table added. April 23 column added to §28.8 operational baseline table. Divergence thresholds updated (ChromaDB floor now 44 from 45). ChromaDB host port corrected to 8002 throughout (container port 8000 internal). Section 12 probe sequence updated with /api/v2/ paths, docker exec for internal-only learner, EEG Delta probe, Caddy perimeter test.*

*★★★ April 9, 2026: ChromaDB backup source corrected; volume mount path corrected; collection count corrected to 49; GBIM container names corrected; Ch 29–42 status clarified; recovery method documented; backup inventory table added; zero-count collections (5) and unknown-count collections (3) flagged for Ch 29.*

*★★ April 1, 2026: Live telemetry confirmed — autonomous learner: 15 cycles / 15 stored / 0 deduplicated / 11 entanglement nodes; `autonomous_learner` ChromaDB: 68 items; LEARN-01/02/03 resolved; 96/96 Up re-confirmed post-LEARN-03 recovery.*

*★ March 28, 2026: 96/96 containers Up; `msallis:5433` restored; `msallisgis:5432` confirmed; ChromaDB 40 collections / 6,675,442 vectors; `allis-memory:8056` secured.*

*March 27, 2026: February 28, 2026 baseline pinned; LLM ensemble slot/responding count clarified; EEG audit table contradiction noted; AAPCAppE Chroma document baseline added; Caddy/auth perimeter layer added; GBIM belief corpus cross-database clarification added.*
