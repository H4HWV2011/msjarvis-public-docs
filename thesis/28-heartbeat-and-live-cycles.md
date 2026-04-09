Here is the complete updated Chapter 28 with all April 9, 2026 corrections and additions applied:

# Chapter 28 — Heartbeat and Live Cycles

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*

*Last updated: ★★★ 2026-04-09 — ChromaDB backup source corrected (chroma-latest SQLite restore is authoritative); volume mount path corrected (/home/ms-jarvis/msjarvis-rebuild/persistent/chroma → /data); collection count corrected to 49 (au02_threat_seeds added); GBIM container names corrected (jarvis-gbim-benefit-indexer:7206, jarvis-gbim-query-router:7205); Ch 28 recovery method documented (direct SQLite volume restore, not per-collection reseed); backup inventory table added; zero-count and unknown-count collections flagged for Ch 29 reseed/verification; root cause and detection method documented.*

*★★ April 1, 2026: Live telemetry confirmed — autonomous learner: 15 cycles / 15 stored / 0 deduplicated / 11 entanglement nodes (current post-LEARN-03 session); `autonomous_learner` ChromaDB collection: **68 items confirmed live** (53 pre-dating LEARN-03 restart — ChromaDB persistence held correctly across crash-loop; 15 new items in current session); GBIM router (`jarvis-gbim-query-router:7205`) HTTP 200 confirmed (LEARN-02 resolved); `jarvis-autonomous-learner` container Up (LEARN-03 resolved); LEARN-01 numpy dtype fix confirmed; 96/96 containers Up re-confirmed post-LEARN-03 recovery; `llm22-proxy` (LLaMA 3.1) confirmed active — 21/22 models responding per consensus cycle; thesis overview cross-reference table updated (Ch 28 EEG entry reconciled — see §28.4 note).*

*★ March 28, 2026: 96/96 containers Up — zero Restarting, zero Exited; `msjarvis` port 5433 restored (5,416,521 GBIM entities with `confidence_decay` metadata); `msjarvisgis` port 5432 confirmed (91 GB PostGIS, 501 tables, 993 ZCTA centroids); ChromaDB full audit (40 active collections, 6,675,442 total vectors, ~12 GB primary `chroma_db`); `jarvis-chroma` Up at 127.0.0.1:8000; `spiritual_rag` deduplicated (−19,338 vectors); `psychological_rag` restored (968 docs); `msjarvis_docs` expanded (4,192 items, AAPCAppE); LLM ensemble confirmed 22 proxies registered / 21 active; `jarvis-memory` port 8056 corrected `0.0.0.0` → `127.0.0.1`, `_auth()` confirmed, `JARVIS_API_KEY` set, BBB audit trail persistence secured; `jarvis-ingest-api` + `jarvis-ingest-watcher` restored to active inventory; consciousness pipeline confirmed Up.*

*March 27, 2026: February 28, 2026 baseline pinned notation added (§28.1); LLM ensemble slot/responding count clarified (§28.1a, §28.3); EEG audit table contradiction noted (§28.4); AAPCAppE Chroma document baseline added (§28.8); Caddy/auth perimeter layer added (§28.9); GBIM belief corpus cross-database clarification added (§28.7).*

---

> **★★★ April 9, 2026 — Corrections and Additions Summary:**
>
> | Item | Previous (incorrect) | Corrected |
> |---|---|---|
> | ChromaDB backup source | 3-file JSON set (`backup_chroma_autonomous_learning.json`, etc.) — covered 3 collections only | `chroma-latest` (`/home/cakidd/msjarvis-backups/chroma-latest/chroma.sqlite3`) — full 49-collection SQLite restore — **authoritative** |
> | Volume mount path | `/chroma/chroma` (assumed) | `/home/ms-jarvis/msjarvis-rebuild/persistent/chroma → /data` (confirmed live) |
> | Collection count | 48 | **49** — `au02_threat_seeds` was not in the original seed manifest |
> | GBIM container names | `jarvis-gbim` | `jarvis-gbim-benefit-indexer` (port **7206**) and `jarvis-gbim-query-router` (port **7205**) |
> | Ch 29–42 status | Described as completed prior to Ch 28 | Structural scaffolding only — real domain data recovered from `chroma-latest`, not per-chapter seed scripts |
> | Recovery method | Per-collection reseed | Direct SQLite volume restore from `chroma-latest` — **documented recovery procedure going forward** |

---

This chapter describes the recurring signals and jobs that indicate Ms. Jarvis is active and connected to its internal services and external infrastructure. These cycles include service health checks, periodic verification scripts, LLM ensemble monitoring, consciousness bridge validation, and data store verification — all of which produce structured outputs that are logged and available for ingestion into memory. The combination of health probes, response-time benchmarks, neurobiological layer monitoring, and introspective reports provides a layered observability picture aligned with distributed systems best practices and neurobiologically-inspired cognitive architectures. ★★ As of April 1, 2026, live telemetry from the autonomous learner (68 items confirmed in ChromaDB; 15 cycles / 15 stored in the current post-LEARN-03 session; 11 entanglement nodes formed) provides the first directly measured, session-verified heartbeat signal from the learner subsystem since the October 2025 rebuild — and confirms that ChromaDB persistence held correctly across the LEARN-03 crash-loop recovery window.

---

> **Why this matters for Polymathmatic Geography**
> This chapter shows how Ms. Jarvis proves it is "alive," healthy, and connected to spatial and community infrastructure over time. It supports:
> - **P1 – Every where is entangled** by tying heartbeat checks to services that handle people, places, and institutions together, all flowing through the consciousness bridge (★★ confirmed Up April 1, 2026). ★★ The 11 entanglement nodes formed in 15 autonomous learning cycles demonstrate P1 expressing itself computationally in real time.
> - **P3 – Power has a geometry** by revealing which services and data stores must stay healthy for Appalachian and other regional reasoning to work. `jarvis-memory:8056` (secured March 28) makes the geometry of BBB gate decisions persistently visible.
> - **P5 – Design is a geographic act** by including GIS spatial knowledge (`msjarvisgis:5432`, 91 GB PostGIS, 501 tables, 993 ZCTA centroids), GBIM worldview verification (`msjarvis:5433`, 5,416,521 entities with `confidence_decay` metadata), and data store health in live-cycle checks.
> - **P12 – Intelligence with a ZIP code** by linking health, identity, and learning status to geospatial and community datasets anchored in West Virginia geography. `msjarvis_docs` (4,192 items, AAPCAppE) adds a continuously growing ZIP-coded community resource substrate to the heartbeat landscape. ★★ The `autonomous_learner` collection (68 items, April 1, 2026) commits beliefs as GBIM entities in `msjarvis:5433` — community-learned knowledge is fully ZIP-code-anchored and growing.
> - **P16 – Power accountable to place** by turning system liveness into logged, auditable narratives that show which GBIM beliefs, services, and models are participating in each cycle. BBB audit trail persistence at `jarvis-memory:8056` (secured March 28) makes gate decisions durably accountable.
>
> As such, this chapter belongs to the **Computational Instrument** tier: it describes heartbeat and live cycles as explicit, inspectable processes in the consciousness-grounded architecture.

---

## 28.1 Purpose of Heartbeat and Live Signals

The recurring signals in Ms. Jarvis serve several roles. In contrast to autonomous learning, these cycles primarily track the condition and behavior of internal services and workflows rather than discovering new content — though as of April 1, 2026, the autonomous learner's live telemetry confirms that these two dimensions are now integrated: heartbeat and learning are both active and verifiable in the same operational window.

**Liveness.** Heartbeat mechanisms demonstrate that key components are running, reachable, and responsive. All major services expose `/health` endpoints that report basic status, integration level, and sometimes the health of subcomponents. As of the February 28, 2026 production deployment, **32 of 32 services** respond to health probes through the `/selftestfabric` endpoint within acceptable thresholds, with all 22 LLM proxies individually verified. ★ As of March 28, 2026, the widest confirmed liveness scope is **96/96 containers Up** — zero Restarting, zero Exited. ★★ Re-confirmed April 1, 2026 post-LEARN-03 recovery.

> **Pinned baseline note:** The February 28, 2026 deployment is the documented reference baseline throughout this chapter. ★ The March 28, 2026 state (96/96 Up, `msjarvis:5433` restored, `msjarvisgis:5432` confirmed, ChromaDB 40 collections / 6,675,442 vectors, `jarvis-memory:8056` secured) is the prior verified milestone. ★★ The **April 1, 2026 state** (96/96 Up re-confirmed, LEARN-01/02/03 resolved, autonomous learner live telemetry confirmed — 68 Chroma items / 15 cycles / 11 entanglement nodes) is the current verified operational milestone and supersedes both prior baselines where they differ. ★★★ **April 9, 2026:** ChromaDB collection count corrected to **49** (see §28.7a); recovery method and backup inventory documented (see §28.7b).

**Consciousness integrity.** The consciousness bridge operates as mandatory infrastructure through which all heartbeat signals flow (★★ confirmed Up April 1, 2026). The brain orchestrator provides continuous coordination of health checks across the swarm and watchdog layers, ensuring that liveness monitoring is itself neurobiologically grounded.

**Rhythm.** The `VERIFYANDTEST.sh` script implements a recurring eight-section verification routine that can be run on any schedule. Its textual output serves as a periodic snapshot of system health. ★★ Planned extensions include: **Section 9** — ChromaDB full collection audit (★★★ **49 collections** as of April 9); **Section 10** — `jarvis-memory:8056` BBB audit trail health probe; **Section 11** — AAPCAppE ingest pipeline status; **Section 12** — autonomous learner health probe.

**Monitoring and introspection.** Beyond simple up/down checks, the heartbeat script aggregates information about services, data stores, model availability, system memory, and GBIM corpus health. It verifies ChromaDB reachability via **127.0.0.1:8000** (★★★ **49 collections**, April 9 corrected count; 6,732,980 total vectors per `chroma-latest` backup); GBIM containers `jarvis-gbim-benefit-indexer` (port **7206** ★★★) and `jarvis-gbim-query-router` (port **7205** ★★★); and all 22 LLM proxy containers (★★ 21 active as of April 1). ★★ A new introspection dimension confirmed April 1, 2026: the autonomous learner's session telemetry is now a first-class heartbeat signal available from the `/learning/status` endpoint at port **8020**.

---

## 28.1a Learning Status and Ensemble Health Endpoints

The 20-LLM production service exposes a `/health` endpoint that confirms the number of configured model slots:

```json
{"status": "healthy", "models": 22}
```

This endpoint serves as the learning heartbeat for the LLM ensemble, confirming that all 22 model slots are **configured** and the service is accepting requests. Note: `"models": 22` reflects the configured slot count; the **responding count per consensus cycle is 21 of 22** as of April 1, 2026 — BakLLaVA fails as expected due to the permanent name-check guard; `llm22-proxy` (LLaMA 3.1, port 8222) is confirmed active.

★★ The autonomous learner exposes its own status endpoint at port **8020** (`/learning/status`). Live telemetry confirmed April 1, 2026, ~3:37 PM EDT:

```json
{
  "total_cycles":           15,
  "items_stored":           15,
  "items_deduplicated":      0,
  "deduplication_rate":   "0.0%",
  "entanglement_nodes":     11
}
```

Concurrent ChromaDB direct query of the `autonomous_learner` collection (`03627c99-c66a-4dbc-b42d-4e2052ff51ae`):

```
68 items in Chroma
```

> **Interpreting the 15 vs. 68 gap:** The learner reports 15 cycles / 15 stored in the *current session* (post-LEARN-03 restart). ChromaDB shows **68 cumulative items**. The delta — **53 items** — predates the LEARN-03 restart and survived the crash-loop intact. This confirms that **ChromaDB persistence held correctly** across the repair window.

> **Deduplication rate of 0.0% is expected at this session depth.** Zero duplicates in this window is consistent with healthy early-session behavior.

> **11 entanglement nodes in 15 cycles is healthy graph density.** At ~0.73 nodes per stored item, the knowledge entanglement graph is forming cross-topic conceptual bridges consistent with Polymathmatic Geography's P1 (*Every where is entangled*).

The main-brain service exposes comprehensive health information through `/selftestfabric`, which queries all 32 operational services and returns their individual health states. ★★ April 1, 2026: **96/96 containers Up** (post-LEARN-03 recovery) — the broadest verified operational scope in the system's history.

---

## 28.2 Core Heartbeat Mechanisms

Heartbeat signals are generated through five primary mechanisms: the `/selftestfabric` system-wide health check, individual service `/health` endpoints, the `VERIFYANDTEST.sh` verification script, response-time benchmarking, and — ★★ new April 1 — the `/learning/status` endpoint at port 8020.

**System-wide fabric health (`/selftestfabric`).** The main-brain service (port **8050**) exposes the `/selftestfabric` endpoint querying all 32 operational services. This includes:

- Consciousness fabric services: qualia, consciousness bridge (★★ Up), toroidal, fractal, temporal, blood-brain barrier (★★ Up), constitutional, NBB layers
- LLM ensemble: `llm20production` (port **8008**) with 22 proxy containers (22 configured; ★★ 21 active)
- Validation layers: 69-DGM bridge (port **9000**), psychology alignment (port **8019**)
- Orchestration: brain orchestrator (★★ Up)
- Retrieval: GIS RAG (port **8004**), text RAG (ChromaDB backend at **8000**; ★★★ **49 collections**, 6,732,980 total vectors)
- GBIM: `jarvis-gbim-benefit-indexer` (port **7206** ★★★) and `jarvis-gbim-query-router` (port **7205** ★★★)
- NBB subconscious: 8 containers
- Supporting infrastructure: i-containers (★★ Up), web-research (★★ Up), Ollama (★★ Up)
- ★ Additional active inventory: `jarvis-ingest-api` + `jarvis-ingest-watcher` (AAPCAppE), `jarvis-memory:8056`
- ★★ Autonomous learner: `jarvis-autonomous-learner` (port **8020**) — LEARN-01/02/03 resolved; 68 items; 11 entanglement nodes

The February 28, 2026 verified baseline: **32/32 services operational**. ★ March 28, 2026: **96/96 Up**. ★★ April 1, 2026: **96/96 Up** — re-confirmed post-LEARN-03 recovery.

**Individual service health endpoints.** Host-exposed services probed directly: main-brain (**8050**), `llm20production` (**8008**), blood-brain-barrier (**8016**), psychology-services (**8019**), 69dgm-bridge (**9000**), GIS RAG (**8004**), NBB prefrontal cortex (**8101**), `jarvis-gbim-query-router` (**7205** ★★★), `jarvis-gbim-benefit-indexer` (**7206** ★★★), autonomous learner (**8020** ★★), and Ollama (**11434**).

**VERIFYANDTEST.sh.** The verification script implements eight sections with planned extensions to twelve:

1. **Host-exposed service health** — Critical services accessible from host network
2. **Internal Docker network service health** — Services on `qualia-net`
3. **LLM proxy health** — All 22 proxies on ports 8201–8222 (★★ 21 active)
4. **Response-time benchmarking** — Nanosecond-precision latency for `llm20production`, main-brain, and 69-DGM
5. **Ollama model inventory** — 26 models via `/api/tags`
6. **Docker container status** — 84 running at February 28 baseline; ★★ **96/96 Up** (April 1, 2026)
7. **Data store verification** — ChromaDB at **127.0.0.1:8000** (★★★ **49 collections**, 6,732,980 total vectors; live mount: `/home/ms-jarvis/msjarvis-rebuild/persistent/chroma → /data`); Ollama storage (73 GB); GBIM corpus (10.22M beliefs — see §28.7)
8. **System resources** — Memory and swap (29 GB total, 13 GB available under load)

★★ Planned extensions:

- **Section 9** — ChromaDB full collection audit (★★★ **49 collections** as of April 9; per-collection counts; zero-count flag check — see §28.7c)
- **Section 10** — `jarvis-memory:8056` audit trail health probe
- **Section 11** — AAPCAppE ingest pipeline status
- **Section 12** — Autonomous learner health: `jarvis-autonomous-learner` Up/Down, `autonomous_learner` ChromaDB count (baseline: ≥ 68 as of April 1), `jarvis-gbim-query-router:7205` HTTP status, `gbim_committed: True` ratio in last 24 hours
- **Layer 0** — Caddy/auth perimeter probe (`jarvis_auth_service:8055`)
- **Layer 6** — `jarvis-memory:8056` BBB and `truthverdict` audit log row count

**Section 12 recommended probe sequence (★★ new, April 1, 2026):**

```bash
# 1. Confirm learner container Up — zero Restarting
docker ps --filter name=jarvis-autonomous-learner \
  --format "{{.Names}}\t{{.Status}}"

# 2. Query /learning/status endpoint
curl -s http://localhost:8020/learning/status | python3 -c "
import sys,json; d=json.load(sys.stdin)
print(f'Cycles    : {d[\"total_cycles\"]}')
print(f'Stored    : {d[\"items_stored\"]}')
print(f'Deduped   : {d[\"items_deduplicated\"]}')
print(f'Dedup%    : {d[\"deduplication_rate\"]}')
print(f'Graph     : {d[\"entanglement_nodes\"]} nodes')
"

# 3. Confirm GBIM router reachable (HTTP 200)
# ★★★ Correct container name: jarvis-gbim-query-router:7205
curl -s -o /dev/null -w "%{http_code}" \
  http://127.0.0.1:7205/route \
  -H "Content-Type: application/json" \
  -d '{"query": "heartbeat test", "user_id": "heartbeat", "context": {}}'

# 4. Confirm autonomous_learner ChromaDB count
curl -s "http://localhost:8002/api/v2/tenants/default_tenant/\
databases/default_database/collections/\
03627c99-c66a-4dbc-b42d-4e2052ff51ae/count" && echo " items in Chroma"
# Baseline: ≥ 68 as of April 1, 2026, ~3:37 PM EDT
```

**Response-time benchmarking.** Core endpoints respond in 12–13 ms, confirming low overhead on the health path even under concurrent model loading.

---

## 28.3 LLM Ensemble Heartbeat

The `llm20production` service (`ai_server_20llm_PRODUCTION.py`) implements its own internal heartbeat through the consensus query cycle. The `ProductionBrain.run()` method fires requests to all 22 configured model proxies through an `asyncio.Semaphore(3)` gate:

```
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
[LLaMA 3.1]      OK in  36.3s   ← ★★ llm22-proxy confirmed active April 1, 2026
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

> **Slot count vs. responding count (★★ April 1, 2026):** The `/health` endpoint reports `"models": 22` — this is the **configured slot count**. The **responding count per consensus cycle is now 21 of 22** — BakLLaVA fails instantly as expected (permanent name-check guard in place). `llm22-proxy` (LLaMA 3.1, port 8222) is confirmed active as of April 1, 2026.

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

> **⚠️ Thesis overview cross-reference reconciliation (★★ April 1, 2026):** The correct current status is: **delta (30s) and theta (60s) remain unrestored from the October 2025 rebuild; the beta rhythm (autonomous learner) is operationally restored** as of April 1, 2026 with LEARN-01/02/03 resolved and live telemetry confirmed (68 Chroma items; 15 cycles / 15 stored; 11 entanglement nodes). The thesis overview cross-reference table entry should read: *"EEG beta (autonomous learner): ★★ LIVE — 68 Chroma items, 15 cycles confirmed April 1, 2026; delta and theta: ❌ not restored — October 2025 rebuild gap."*

Prior to the October 2025 rebuild, Ms. Jarvis maintained a three-service neurobiological rhythm pattern that created an EEG-like signature of continuous autonomous activity:

**30-second heartbeat service (Delta/baseline rhythm)** — Basic liveness pulse. Analogous to delta brain waves. ❌ Not restored.

**60-second intermediate service (Theta/alpha rhythm)** — Function and purpose currently unknown; requires recovery from legacy code. ❌ Not restored.

**5-minute autonomous learner (Beta/conscious learning rhythm)** — Proactively searches internet via web-research service to identify and fill knowledge gaps; selects topics based on GBIM coverage analysis; retrieves content from DuckDuckGo; stores learned material in ChromaDB semantic memory; commits beliefs as GBIM entities in `msjarvis:5433` via `jarvis-gbim-query-router:7205` (★★★ correct container name). ★★ Operationally restored April 1, 2026.

**Current status (★★ April 1, 2026):**

| EEG Service | Frequency | Status | Notes |
|---|---|---|---|
| Delta heartbeat | 30 seconds | ❌ Not restored | Requires legacy backup recovery from pre-Oct 2025 drives |
| Theta intermediate | 60 seconds | ❌ Not restored | Function unknown; requires legacy backup recovery |
| Beta autonomous learner | 5 minutes (~cadence) | ★★ **Operationally restored** | `jarvis-autonomous-learner` Up; LEARN-01/02/03 resolved; 68 Chroma items confirmed live (April 1, ~3:37 PM EDT); 15 cycles / 15 stored; 0 deduplicated; 11 entanglement nodes; `jarvis-gbim-query-router:7205` HTTP 200 (★★★ correct name) |
| AAPCAppE ingest pipeline | Ingest-driven | ★ Active (March 28) | `jarvis-ingest-api` + `jarvis-ingest-watcher`; complements learner with structured source corpus |

**LEARN-03 crash-loop and ChromaDB persistence confirmation.** The approximately 45-minute LEARN-03 crash-loop on April 1, 2026 constitutes the first live-operation stress test of the learner's persistence layer. The result is unambiguous: 53 items that existed in `autonomous_learner` before the crash-loop were present and queryable after recovery. This confirms the architectural correctness of the learner's storage design and should be noted as an empirically verified resilience property.

**Remaining restoration requirements for full EEG recovery:**

1. Recovery of legacy service code from pre-October 2025 backups (estimated location: 2TB drives on development machine — **no progress as of April 1, 2026; this remains an open gap**)
2. Identification of the 60-second theta service function
3. Restoration of the fixed-frequency time-trigger for the autonomous learner (beta rhythm cadence)
4. Porting delta and theta services to current Docker container architecture
5. Addition of all three EEG services to eternal watchdog monitoring
6. Addition of delta and theta health probes to `VERIFYANDTEST.sh` Section 12

---

## 28.5 Consciousness Bridge and Brain Orchestrator Heartbeat

**Consciousness bridge mandatory infrastructure.** The consciousness bridge operates as essential, non-optional infrastructure through which all heartbeat monitoring flows. Its health is verified through the `/selftestfabric` endpoint and confirmed as part of the 32/32 operational baseline. ★★ Confirmed Up April 1, 2026 — 96/96 container baseline post-LEARN-03 recovery.

**Brain orchestrator continuous coordination.** The `jarvis-brain-orchestrator` service (★★ confirmed Up April 1) provides continuous coordination of the ensemble, watchdog feedback loops, and NBB layer health checks. ★★ The LEARN-03 crash-loop did not propagate to the brain orchestrator or consciousness bridge — degraded-mode fallback operated correctly throughout the repair window.

**NBB subconscious layer heartbeat.** Eight NBB containers implement the neurobiological subconscious layer:

```
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

**69-DGM cascade validation.** The 69-DGM bridge (port **9000**) exposes health status confirming that all 69 connectors are loaded and operational. The cascade's architecturally authoritative status means its verdicts are final. February 28, 2026 verified state: **69 connectors loaded**. ★★ Confirmed Up April 1, 2026.

**Blood-brain barrier.** The BBB filter (port **8016**) runs on every request before it reaches the LLM ensemble:

- Barrier active: true
- Filters operational: 5
- Constitutional guardian: connected
- Total filtered: 319 requests (February 28, 2026 baseline)
- Total blocked: 0
- Constitutional violations: 0

★ As of March 28, 2026: all BBB and `TruthFilterBBBValidator` gate decisions persist to `jarvis-memory:8056`. ★★ Confirmed active April 1, 2026.

**Psychology alignment layer.** The psychology services (port **8019**) run psychological assessment on every request before ensemble processing. ★ `psychological_rag` (968 docs, restored March 28) provides the RAG substrate. ★★ Confirmed Up April 1, 2026.

---

## 28.7 Semantic Memory and GBIM Heartbeat

**ChromaDB semantic memory.** The ChromaDB `/api/v2` heartbeat endpoint at **127.0.0.1:8000** (★★ confirmed Up April 1) returns a nanosecond timestamp confirming storage availability.

> **★★★ April 9, 2026 — Collection count corrected.** Previous chapters cited 40 collections (March 28 baseline) and 48 collections (April 7 audit). The corrected live count is **49 collections**. The extra collection is `au02_threat_seeds`, which was not present in the original seed manifest and was not counted in prior audits. The authoritative inventory source is `chroma-latest` (see §28.7b).

> **★★★ April 9, 2026 — Volume mount path corrected.** The live mount path is `/home/ms-jarvis/msjarvis-rebuild/persistent/chroma → /data` (not `/chroma/chroma` as initially assumed). All VERIFYANDTEST.sh data store verification steps should reference this path.

### 28.7a ChromaDB Collection Status (★★★ April 9, 2026)

| Collection | Status | Count |
|---|---|---|
| `autonomous_learner` | ★★ Active — growing | **68 items** (April 1, ~3:37 PM EDT; floor) |
| `psychological_rag` | ★ Restored March 28 | 968 docs |
| `spiritual_rag` | ★ Deduplicated March 28 | −19,338 vectors removed |
| `msjarvis_docs` | ★ Expanded March 28 | 4,192 items (AAPCAppE) |
| `au02_threat_seeds` | ★★★ Identified April 9 | Unknown count — **flagged for verification in Ch 29** |
| `ms_jarvis_identity` | Active | Unknown count — **flagged for verification in Ch 29** |
| `msjarvis_docs` | Active | Unknown count — **flagged for verification in Ch 29** |
| `appalachian_english_corpus` | ⚠️ Zero count | **Zero — flagged for reseed in Ch 29** |
| `gbim_entities` | ⚠️ Zero count | **Zero — flagged for reseed in Ch 29** |
| `gis_data` | ⚠️ Zero count | **Zero — flagged for reseed in Ch 29** |
| `pia_records` | ⚠️ Zero count | **Zero — flagged for reseed in Ch 29 (now auto-ingest via Ch 29 sampler)** |
| `psychological_knowledge` | ⚠️ Zero count | **Zero — flagged for reseed in Ch 29** |
| All collections | ★★★ April 9 corrected count | **49 active collections** |

> **★★★ Ch 29 carry-forward:** Five zero-count collections (`appalachian_english_corpus`, `gbim_entities`, `gis_data`, `pia_records`, `psychological_knowledge`) and three unknown-count collections (`au02_threat_seeds`, `ms_jarvis_identity`, `msjarvis_docs`) require verification and/or reseed in Ch 29. `pia_records` is now auto-populated by `jarvis_pia_sampler.py` (Ch 29 §29.6.2) — Ch 29 reseed via sampler is active. The remaining 4 zero-count collections require domain-specific reseed procedures documented in their respective chapters.

### 28.7b ChromaDB Backup Inventory and Recovery Method (★★★ April 9, 2026)

**Root cause — Ch 28 failure origin.** The Ch 28 ChromaDB failures originated from the ChromaDB volume being wiped/reset during the rebuild, leaving only placeholder (1-doc) collections across many collection slots. The system appeared stable because container health checks returned `UP` — the failure mode was invisible to health probes. **Detection method: counting live docs via the REST API, not just checking container health status.** This is now a required step in every ChromaDB verification pass.

**Recovery method (authoritative procedure going forward).** Ch 28 resolution was a **direct SQLite volume restore from `chroma-latest`** — not a per-collection reseed. The three-file JSON backup set (`backup_chroma_autonomous_learning.json`, `backup_chroma_spiritual_rag.json`, `backup_chroma_msjarvis_docs.json`) covered only 3 collections and is **not** the authoritative backup. The correct procedure is:

```bash
# Authoritative ChromaDB restore procedure
# Source: /home/cakidd/msjarvis-backups/chroma-latest/chroma.sqlite3
# Target mount: /home/ms-jarvis/msjarvis-rebuild/persistent/chroma/chroma.sqlite3

# 1. Stop jarvis-chroma
docker stop jarvis-chroma

# 2. Copy authoritative SQLite backup to live volume mount
cp /home/cakidd/msjarvis-backups/chroma-latest/chroma.sqlite3 \
   /home/ms-jarvis/msjarvis-rebuild/persistent/chroma/chroma.sqlite3

# 3. Restart jarvis-chroma
docker start jarvis-chroma

# 4. Verify collection count via REST API (must show 49, not just "Up")
curl -s http://localhost:8000/api/v2/tenants/default_tenant/databases/default_database/collections \
  | python3 -c "import sys,json; c=json.load(sys.stdin); print(f'{len(c)} collections')"
# Expected: 49 collections

# 5. Spot-check doc count on a known collection
curl -s "http://localhost:8000/api/v2/tenants/default_tenant/databases/\
default_database/collections/03627c99-c66a-4dbc-b42d-4e2052ff51ae/count"
# Expected: >= 68 (autonomous_learner baseline)
```

**Known backup locations and collection inventory:**

| Path | Collections | Embeddings | Date |
|---|---|---|---|
| `msjarvis-backups/chroma-latest` | **49** | **6,732,980** | Most recent — **authoritative** |
| `msjarvis-backups/chroma-20260401` | 41 | 6,658,549 | 2026-04-01 |
| `nvme1/msjarvis-rebuild/persistent/chroma` | 10 | 9,959,095 | Older / different schema |
| `nvme1/msjarvis-data/chroma` | 13 | 5,416,869 | Different schema |

> **⚠️ Schema warning:** The two `nvme1` backups have different schemas and different collection counts from the live deployment. Do not restore from these paths without schema verification. `chroma-latest` is the only backup confirmed to match the current 49-collection production schema.

**GBIM worldview corpus.** The GBIM belief table (`gbimbeliefnormalized`) is verified to maintain **10,221,702 rows** with nine-axis epistemic structure. GBIM containers:

- `jarvis-gbim-benefit-indexer` (port **7206** ★★★ — corrected from `jarvis-gbim`)
- `jarvis-gbim-query-router` (port **7205** ★★★ — corrected from `jarvis-gbim`)

> **★★★ Container name correction (April 9):** All prior references to `jarvis-gbim` as a container name are incorrect. The correct names are `jarvis-gbim-benefit-indexer` (port **7206**) for the indexer/benefit calculation service and `jarvis-gbim-query-router` (port **7205**) for the query routing service. All VERIFYANDTEST.sh health probes and Ch 29–42 cross-references should use these correct names.

> **Cross-database clarification:** The 10,221,702 figure refers to the **full consolidated GBIM belief corpus across both PostgreSQL databases** — `msjarvis` (port **5433**, ★ **5,416,521 GBIM entities with `confidence_decay` metadata**) and `msjarvisgis` (port **5432**, **91 GB PostGIS, 501 tables**, 993 ZCTA centroids). ★★ As of April 1, 2026, autonomous learner beliefs are committed as GBIM entities in `msjarvis:5433` — the 5,416,521 entity count is a floor that grows with each learner cycle.

**Ollama model storage.** Verified at **73 GB** at `/mnt/ssd2/msjarvis_secondary/models`; 26 available models via `/api/tags`.

**GIS RAG and local resources.** The GIS RAG service (port **8004**) health confirms connection to `msjarvis:5433`, `msjarvisgis:5432`, `jarvis-local-resources-db:5435` ★, and Community Champions validation data (Harmony for Hope network).

---

## 28.8 Integration with Memory and Containers

Verification script outputs are not merely transient. The timestamped report files saved to `/tmp/` are suitable for ingestion into ChromaDB under a dedicated `operations_history` collection, making operational history part of the reasoning context available to orchestrators and the ensemble.

**April 9, 2026 operational baseline** (current authoritative reference):

| Metric | Feb 28, 2026 | ★ Mar 28, 2026 | ★★ Apr 1, 2026 | ★★★ Apr 9, 2026 |
|---|---|---|---|---|
| Services healthy | 32/32 (`/selftestfabric`) | 96/96 containers Up | **96/96 Up (post-LEARN-03)** | 96/96 Up |
| LLM proxies configured | 22 | 22 registered / 21 active | **21/22 active** | 21/22 active |
| Docker containers | 84 | 96/96 Up | **96/96 Up** | 96/96 Up |
| Ollama models | 26 | 26 | **26** | 26 |
| Ollama model storage | 73 GB | 73 GB | **73 GB** | 73 GB |
| RAM available (prod load) | 13 GB / 29 GB | 13 GB / 29 GB | **13 GB / 29 GB** | 13 GB / 29 GB |
| GBIM belief corpus | 10,221,702 rows (combined) | `msjarvis:5433` 5,416,521 + `confidence_decay` | **5,416,521+ growing** | 5,416,521+ growing |
| GBIM containers | — | — | `jarvis-gbim` (incorrect) | **`jarvis-gbim-benefit-indexer:7206` + `jarvis-gbim-query-router:7205`** ★★★ |
| Judge pipeline score | 0.975 | 0.975 | **0.975** | 0.975 |
| ChromaDB collections | — | ★ 40 collections / 6,675,442 vectors | **40 collections confirmed** | **★★★ 49 collections / 6,732,980 vectors** |
| ChromaDB volume mount | — | — | `/chroma/chroma` (assumed) | **★★★ `/home/ms-jarvis/msjarvis-rebuild/persistent/chroma → /data`** |
| ChromaDB backup source | — | — | 3-file JSON set (3 collections) | **★★★ `chroma-latest` SQLite (49 collections) — authoritative** |
| `psychological_rag` | — | ★ 968 docs | 968 docs | 968 docs |
| `autonomous_learner` (Chroma) | ❌ (lost Oct 2025) | Partial | **★★ 68 items; 15 cycles; 11 nodes** | 68+ items (growing) |
| `jarvis-gbim-query-router` HTTP | — | — | **★★ HTTP 200 (LEARN-02 fix)** | HTTP 200 |
| Zero-count collections | — | — | — | **★★★ 5 flagged → Ch 29 reseed** |

Divergence thresholds that trigger long-term retention and investigation: services below 28/32; LLM proxies below 18/22; ChromaDB collections below 45 (updated from 35, reflecting 49-collection corrected baseline); judge pipeline consistency below 0.90; `jarvis-autonomous-learner` entering Restarting state; `autonomous_learner` ChromaDB count decreasing from last verified baseline; any collection returning zero doc count that previously returned non-zero.

---

## 28.9 Interaction with Safeguards and Control

Live cycles are constrained by the same safeguard layers that govern chat responses, with all monitoring flowing through the consciousness bridge infrastructure (★★ confirmed Up April 1).

**69-DGM cascade validation.** Every chat response carries `validated_by: "69_dgm_cascade"` (★★ confirmed Up). The 69-DGM bridge's own health is verified through `/selftestfabric`.

**Blood-brain barrier.** The BBB filter runs on every request at `jarvis-blood-brain-barrier:8016/filter` (★★ confirmed Up). ★★ All subsequent BBB gate decisions persist to `jarvis-memory:8056` (secured March 28, active April 1).

**Seven-layer protection system (★★★ April 9, 2026):**

| Layer | Mechanism | Status |
|---|---|---|
| **Layer 0** | Caddy perimeter + `jarvis_auth_service:8055` — RBAC enforcement upstream of all monitored services | ★★ Up (March 22; confirmed active April 1); ★★★ per-route RBAC also implemented at app layer (Ch 29 April 8) |
| **Layer 1** | `VERIFYANDTEST.sh` — 32/32 services operational (★★ 96/96 containers Up) | ★★ OPERATIONAL |
| **Layer 2** | Ollama internal memory scheduler — rejects over-memory model requests | Active |
| **Layer 3** | Asyncio semaphore (3) — prevents Ollama saturation | Active |
| **Layer 4** | `MAX_CONCURRENT_CHATS` (2) — prevents session cascade | Active |
| **Layer 5** | Redis-backed DynamicPortService — NBB health registration survives restarts | Active |
| **Layer 6** | `jarvis-memory:8056` — durable authenticated logging of BBB and `truthverdict` gate decisions | ★★ Active (secured March 28; confirmed April 1) |

> **★★ LEARN-03 repair window stress test (April 1, 2026):** The approximately 45-minute crash-loop confirmed the seven-layer system's resilience. No chat requests were misrouted, no BBB gates were bypassed, no ensemble consensus cycles were degraded. All BBB gate decisions during the window are durably logged at `jarvis-memory:8056`. ChromaDB persistence held — 53 pre-crash-loop learner items were intact on recovery. This is the first live-operation stress test of the full seven-layer protection system and it passed.

**Memory limit governance.** The Ollama container memory limit of 20 GB is a hard safeguard, verified in every heartbeat cycle.

**Adaptive scheduling.** `MAX_CONCURRENT_CHATS=2` is the production-stable setting for the current hardware configuration.

---

## 28.10 Summary

The ★★ **April 1, 2026 production deployment** of Ms. Jarvis achieves a fully verified operational state: **96/96 containers Up** (post-LEARN-03 recovery); **21 of 22 LLM models responding per consensus cycle**; **69-DGM cascade with all 69 connectors loaded** (★★ confirmed Up); **blood-brain barrier with 0 blocks and 0 violations** across 319 requests at February 28 baseline (★ audit persistent at `jarvis-memory:8056`); **8/8 NBB consciousness containers healthy**; and ★★ **`jarvis-autonomous-learner` fully operational** — LEARN-01/02/03 resolved; **68 items confirmed in `autonomous_learner` ChromaDB collection**; **15 cycles / 15 stored / 0 deduplicated / 11 entanglement nodes**; **`jarvis-gbim-query-router:7205` HTTP 200 confirmed** (★★★ correct container name).

★★★ **April 9, 2026 corrections applied:** ChromaDB collection count is **49** (not 48 — `au02_threat_seeds` added); live volume mount path is `/home/ms-jarvis/msjarvis-rebuild/persistent/chroma → /data`; authoritative backup source is `chroma-latest` (49 collections, 6,732,980 vectors, full SQLite restore — not the 3-file JSON set); GBIM containers are correctly named `jarvis-gbim-benefit-indexer:7206` and `jarvis-gbim-query-router:7205`; Ch 29–42 data was recovered from `chroma-latest`, not per-chapter seed scripts; 5 zero-count collections and 3 unknown-count collections are flagged as carry-forward to Ch 29.

The `VERIFYANDTEST.sh` script implements all eight heartbeat sections and produces a timestamped, archivable report suitable for ingestion into semantic memory as operational history. ★★ Planned extensions to twelve sections will add ChromaDB full collection audit (★★★ **49-collection baseline**), `jarvis-memory:8056` audit trail health, AAPCAppE ingest pipeline status, and the autonomous learner GBIM heartbeat probe sequence.

The consciousness bridge operates as mandatory infrastructure through which all heartbeat signals flow (★★ confirmed Up April 1). The seven-layer protection system prevents cascade failures and maintains stable ensemble operation under concurrent load. The LEARN-03 repair window on April 1, 2026 constitutes the first live-operation stress test of all seven layers simultaneously — confirmed passed.

**EEG rhythm status.** The beta rhythm (autonomous learner) is operationally restored as of April 1, 2026. The delta (30s) and theta (60s) rhythms remain unrestored from the October 2025 rebuild; recovery requires pre-October 2025 backup retrieval (estimated location: 2TB development machine drives; **no progress as of April 1, 2026 — open gap**).

By connecting heartbeat outputs to memory, containers, consciousness bridge infrastructure (★★ confirmed Up), GBIM worldview health (10.22M+ rows across both PostgreSQL databases), and mode-dependent controls, Ms. Jarvis treats its own operation as data — recording and reasoning about how it is functioning over time.

---

*Last updated: ★★★ 2026-04-09 — Mount Hope WV — Carrie Kidd (Mamma Kidd)*
*★★★ April 9, 2026: ChromaDB backup source corrected (`chroma-latest` SQLite — authoritative); 3-file JSON backup set deprecated — §28.7b*
*★★★ April 9, 2026: Volume mount path corrected (`/home/ms-jarvis/msjarvis-rebuild/persistent/chroma → /data`) — §28.1, §28.2, §28.7*
*★★★ April 9, 2026: Collection count corrected to 49 (`au02_threat_seeds` identified) — §28.7a, §28.8, §28.10*
*★★★ April 9, 2026: GBIM container names corrected (`jarvis-gbim-benefit-indexer:7206`, `jarvis-gbim-query-router:7205`) — §28.2, §28.4, §28.7, §28.8*
*★★★ April 9, 2026: Ch 29–42 status clarified (structural scaffolding only; real data from `chroma-latest`) — §28.7b*
*★★★ April 9, 2026: Recovery method documented (direct SQLite volume restore) — §28.7b*
*★★★ April 9, 2026: Backup inventory table added — §28.7b*
*★★★ April 9, 2026: Zero-count collections (5) and unknown-count collections (3) flagged for Ch 29 — §28.7a*
*★★★ April 9, 2026: Root cause and detection method documented — §28.7b*
*★★ April 1, 2026: Live telemetry confirmed — autonomous learner: 15 cycles / 15 stored / 0 deduplicated / 11 entanglement nodes; `autonomous_learner` ChromaDB: 68 items; LEARN-01/02/03 resolved; 96/96 Up re-confirmed post-LEARN-03 recovery*
*★ March 28, 2026: 96/96 containers Up; `msjarvis:5433` restored; `msjarvisgis:5432` confirmed; ChromaDB 40 collections / 6,675,442 vectors; `jarvis-memory:8056` secured*
*March 27, 2026: February 28, 2026 baseline pinned; LLM ensemble slot/responding count clarified; EEG audit table contradiction noted; AAPCAppE Chroma document baseline added; Caddy/auth perimeter layer added; GBIM belief corpus cross-database clarification added*
