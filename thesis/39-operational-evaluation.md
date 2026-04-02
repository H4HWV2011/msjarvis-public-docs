# Chapter 39 — Operational Evaluation

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV — Last updated: ★ April 2, 2026 — CHAPTER 39 FULLY CERTIFIED CLOSED: ✅ 22 PASS ❌ 0 FAIL ⚠️ 1 WARN (intentional — `local_resources` 48/55, 7 WV counties, Phase 2 data task, documented and deferred); 101 containers running; all 5 public hostnames live (401 token enforced); Cloudflare tunnel HEALTHY; preflight gate logic (8 bugs) fixed; container threshold updated ≥79 → ≥96 (now 101 running); all 0.0.0.0 exposures eliminated; Caddyfile :8085 self-loop fixed → proxies to 18018; cloudflared config updated from hardcoded 8443 to 8085; chat.mountainshares.us DNS CNAME added; all 5 public hostnames live and token-enforced; jarvis-hilbert-state port conflict remapped to 8092; Cloudflare tunnel warn cleared. Prior March 28, 2026 PM baseline carries forward unchanged below.*

---

> **Port and database corrections (permanent record — ★ updated April 2, 2026):**
>
> - **PostgreSQL `msjarvis`** is at host port **5433** — ★ 5,416,521 GBIM entities with `confidence_decay` metadata, 80 epochs, 206 source layers (restored March 28). This is the primary GBIM belief store. ★ `confidence_decay` metadata enables temporal confidence grading — high-decay entities should be flagged for episodic audit before use as ground truth.
> - **PostgreSQL `gisdb` / `msjarvisgis`** (PostGIS) is at host port **5432** — ★ 91 GB, 501 tables, 993 ZCTA centroids, geospatial features. This is the GIS database. Any reference to port **5452** for `gisdb` in earlier chapter drafts is a cross-chapter drafting inconsistency; **the correct host port for `gisdb` is 5432** — this correction block is authoritative.
> - **PostgreSQL `jarvis-local-resources-db`** is at host port **5435** (`127.0.0.1:5435->5432/tcp`). Container DSN corrected March 28, 2026: `jarvis-local-resources-db:5432/postgres`. The `/resolve` endpoint is confirmed live as of March 28, 2026.
> - **ChromaDB** (`jarvis-chroma`) host port is **8002** (`127.0.0.1:8002->8000/tcp`). Container-internal port 8000 is not used by host scripts. All scripts must reference port **8002**. ★ Updated inventory: **40 active collections, 6,675,442 total vectors** (full audit March 28, 2026). Prior count of 31 collections / 6,665,093 items (March 25 snapshot) is superseded. `ms_jarvis_memory` collection confirmed present. `psychological_rag` collection restored to **968 docs** (March 28).
> - **Redis** (`jarvis-redis`) host port is **6380** (`127.0.0.1:6380->6379/tcp`). Container-internal port 6379 is used only by container-to-container calls. Async job status key is `'complete'` (not `'done'`).
> - **`jarvis-main-brain`** unified gateway is at port **8050** — not 8010. Any reference to port 8010 in pipeline diagrams refers to `jarvis-wv-entangled-gateway`, a separate degraded service.
> - **BBB** (`jarvis-blood-brain-barrier`) is at port **8016** — six filters: `EthicalFilter`, `SpiritualFilter`, `SafetyMonitor`, `ThreatDetection`, `steganography_filter`, `truth_verification`.
> - **`jarvis-rag-server`** host port is **8003**, container-internal port is also **8003** (`127.0.0.1:8003->8003/tcp`, verified March 28, 2026). Any prior reference to internal port 8016 for this container is incorrect. RAG endpoint is **`/query`** (not `/direct_rag` — corrected sprint Patch 3A, March 25, 2026).
> - **`jarvis-autonomous-learner`** host port is **8020** (`127.0.0.1:8020->8020/tcp`, verified March 28, 2026). Any prior reference to port **8425** for this container is incorrect and stale.
> - **`jarvis-consciousness-bridge`** is internal-only (no host binding, internal port 8020). It shares the 8020 internal address space with `jarvis-autonomous-learner` but does NOT have a host-side port binding. All host scripts must reach `jarvis-autonomous-learner` at host port 8020. The consciousness bridge is not reachable directly from the host.
> - **Container count is 101** as of ★ April 2, 2026. Prior documentation referencing 96 containers reflects the March 28 baseline. The preflight gate container threshold has been updated from ≥79 to ≥96 (April 2, 2026). ★ `jarvis-hilbert-state` was remapped to port 8092 to resolve a prior port conflict.
> - **MountainShares/Commons/DAO services are DEPLOYED** as of March 28, 2026. Prior documentation stating "NOT DEPLOYED / HTTP 000" for ports 8080–8084 is superseded. All five services are confirmed running.
> - **`jarvis-gbim-query-router`** is the correct container name (not `gbim_query_router`). Host port **7205** (`127.0.0.1:7205->7205/tcp`).
> - **Preflight gate baseline is 24 PASS / 0 FAIL** (March 28 baseline). ★ **April 2, 2026 certified closed state: ✅ 22 PASS ❌ 0 FAIL ⚠️ 1 WARN (intentional).** The single remaining WARN is `local_resources 48/55` — 7 WV counties, Phase 2 data task, documented and deferred.
> - **Zero `0.0.0.0` exposures** confirmed across all 101 containers as of April 2, 2026. ★ All prior 0.0.0.0 exposures have been eliminated.
> - ★ **`jarvis-memory:8056` secured (March 28):** `_auth()` confirmed, `JARVIS_API_KEY` set. All BBB gate decisions — Phase 1.4 filter events and Phase 4.5 log-only events — are now durably logged at `jarvis-memory:8056`. These records survive container restarts and are independently queryable for governance accountability.
> - ★ **All 5 public hostnames live and token-enforced (April 2, 2026):** All public endpoints return 401 without a valid token. `chat.mountainshares.us` DNS CNAME added and confirmed returning 401.
> - ★ **Caddyfile :8085 → 18018 (April 2, 2026):** The Caddyfile `:8085` self-loop has been fixed and now correctly proxies to port 18018 (the unified gateway). `cloudflared` config updated from hardcoded 8443 to 8085.

This chapter records the operational state of Ms. Jarvis as of ★ April 2, 2026,
with verified test results from the production deployment running on the Legion 5
at `~/msjarvis-rebuild-working/msjarvis-rebuild/`. All results listed here were
observed directly from live system outputs, terminal sessions, and verification
scripts. No result in this chapter is inferred or estimated. Where a test result
is pending or inconclusive, it is labeled as such.

---

## ★ Chapter 39 Certification Block — April 2, 2026

```
╔══════════════════════════════════════════════════════╗
║   CHAPTER 39 — FINAL CERTIFIED STATE                ║
║                                                      ║
║   ✅ PASS: 22   ❌ FAIL: 0   ⚠️  WARN: 1            ║
║   101 containers running                             ║
║   All 5 public hostnames live (401 token enforced)  ║
║   Cloudflare tunnel — HEALTHY                        ║
║   2026-04-02 ~10:01 EDT                              ║
╚══════════════════════════════════════════════════════╝

Single remaining WARN (intentional):
  local_resources 48/55 — 7 WV counties, Phase 2 data task,
  documented and deferred.
```

### What Was Fully Closed — April 2, 2026

| Item | Result |
|------|--------|
| Preflight gate logic (8 bugs) | ✅ Fixed |
| Container threshold ≥79 → ≥96 | ✅ Updated (101 now running) |
| All 0.0.0.0 exposures | ✅ Eliminated |
| Caddyfile :8085 self-loop | ✅ Fixed → proxies to 18018 |
| Cloudflared config hardcoded to 8443 | ✅ Updated to 8085 |
| chat.mountainshares.us DNS CNAME | ✅ Added, returning 401 |
| All 5 public hostnames | ✅ Live and token-enforced |
| jarvis-hilbert-state port conflict | ✅ Remapped to 8092 |
| Cloudflare tunnel warn | ✅ Cleared |

---

## 39.1 Evaluation Philosophy

Ms. Jarvis is evaluated operationally — not against artificial benchmarks, but
against the tasks it was built to perform for communities in the New River Gorge
region and across West Virginia. That means the evaluation questions are:

- Can it answer questions that matter to people in Mount Hope, WV and surrounding
  communities?
- Is its memory growing and reliable?
- Can it be trusted to tell the truth about who owns the land?
- Does it respond in time to be useful?
- Does it route queries correctly through the right subsystems?
- Can it survive a reboot and resume full capability without manual intervention?

Each section below records a capability domain, the test performed, and the
verified result. New to this chapter as of March 20, 2026: GBIM landowner query
capability is now fully verified in production. New as of March 22, 2026: first
confirmed public end-to-end chat response via https://egeria.mountainshares.us.
New as of March 25, 2026: consciousness pipeline confirmed fully operational
following three bridge patches (Chapter 25 §25.9); full end-to-end chat test
completed with Chroma, WOAH, Hilbert local entity recall, and LLM persona all
verified. New as of ★ March 28, 2026 (AM): container count updated to 96;
`jarvis-autonomous-learner` port corrected to 8020; `jarvis-rag-server` internal
port corrected; MountainShares services confirmed deployed; EEG layer
(delta/theta/beta), `jarvis-memory`, and `jarvis-hilbert-gateway` documented;
`jarvis-local-resources-db` DSN corrected; data governance policy established
(no synthetic or unverified data in `local_resources`); 45 verified Kanawha County
resources confirmed active; `/resolve` endpoint confirmed live;
`scripts/seed_local_resources_chroma.py` documented. ★ New as of March 28, 2026
(PM): `jarvis-memory:8056` secured (`_auth()` confirmed, `JARVIS_API_KEY` set,
durable BBB audit trail active); `confidence_decay` metadata confirmed on
`msjarvis:5433`; ChromaDB full audit updated to **40 active collections /
6,675,442 total vectors**; `psychological_rag` restored to 968 docs. ★ New as of
**April 2, 2026**: Chapter 39 fully certified closed — 22 PASS 0 FAIL 1 WARN
(intentional); 101 containers running; all 5 public hostnames live and
token-enforced; Cloudflare tunnel HEALTHY; all 8 preflight gate bugs fixed;
container threshold updated; all 0.0.0.0 exposures eliminated; Caddyfile and
cloudflared routing corrected; `jarvis-hilbert-state` port conflict resolved.

---

## 39.2 Production Stack Health (★ April 2, 2026)

Test: `docker compose up -d` followed by `~/jarvis_startup.sh` on full
101-container stack.

Verified result:

```
All 101 containers: RUNNING
Compose file: ~/msjarvis-rebuild-working/msjarvis-rebuild/docker-compose.yml
Docker Compose version: v5.1.0
All build: directives: converted to image: references — no rebuild on startup

Six judge/gateway pipeline containers: GREEN (jarvis_startup.sh)
  ✅ jarvis-judge-truth (port 7230)
  ✅ jarvis-judge-consistency (port 7231)
  ✅ jarvis-judge-alignment (port 7232)
  ✅ jarvis-judge-ethics (port 7233)
  ✅ jarvis-judge-pipeline (coordinator port 7239)
  ✅ jarvis-69dgm-bridge (host port 19000 / internal port 9000)

Previously orphaned containers (added to compose March 22, 2026):
  ✅ jarvis-crypto-policy (port 8099)
  ✅ jarvis-ingest-api (no host binding)
  ✅ jarvis-ingest-watcher (no host binding)

Containers confirmed live March 28, 2026:
  ✅ jarvis-memory (port 8056) ★ SECURED — _auth() confirmed, JARVIS_API_KEY set
                                  durable BBB audit trail active
  ✅ jarvis-eeg-delta (port 8073)
  ✅ jarvis-eeg-theta (port 8074)
  ✅ jarvis-eeg-beta (port 8075)
  ✅ jarvis-mountainshares-coordinator (port 8080)
  ✅ jarvis-commons-gamification (port 8081)
  ✅ jarvis-dao-governance (port 8082)
  ✅ jarvis-ms-token-service (port 8083)
  ✅ jarvis-community-stake-registry (port 8084)
  ✅ jarvis-hilbert-gateway (internal, no host binding)

★ Additional containers confirmed live April 2, 2026 (101 total):
  ✅ jarvis-hilbert-state (port 8092 — remapped from conflicting port)
  [+ additional containers to 101 total]

GBIM query router:
  ✅ jarvis-gbim-query-router (port 7205) — added to compose March 20, 2026

EXTERNAL SYSTEMD SERVICES (not Docker Compose — auto-start on boot):
  ✅ caddy.service (port 8085 → proxies to 18018 ★ Caddyfile self-loop fixed April 2)
  ✅ jarvis-auth.service (port 8055 — scripts/jarvis_auth_service.py)
  ✅ cloudflared.service (Cloudflare Tunnel — msjarvis ★ HEALTHY — config
                          updated from 8443 to 8085, April 2)

★ ALL 5 PUBLIC HOSTNAMES LIVE AND TOKEN-ENFORCED (April 2, 2026):
  ✅ egeria.mountainshares.us       — 401 without token
  ✅ chat.mountainshares.us         — 401 without token (CNAME added April 2)
  ✅ [additional hostnames ×3]      — 401 without token
```

**Assessment:** ✅ Full 101-container stack confirmed running as of April 2, 2026.
Zero `0.0.0.0` exposures confirmed. Three external systemd services (Caddy,
jarvis-auth, cloudflared) auto-start independently of Docker Compose on boot.
MountainShares/Commons/DAO tier (5 containers, ports 8080–8084) confirmed deployed.
EEG layer (3 containers, ports 8073–8075), `jarvis-memory` (port 8056 — ★ secured),
`jarvis-hilbert-gateway`, and `jarvis-hilbert-state` (port 8092) confirmed running.
★ `jarvis-memory:8056` durable audit trail active — all BBB gate decisions
persistently logged, surviving container restarts. ★ Cloudflare tunnel HEALTHY.
★ All 5 public hostnames live and token-enforced.

**Full verified reboot sequence:**

```bash
cd ~/msjarvis-rebuild-working/msjarvis-rebuild
docker compose up -d && ~/jarvis_startup.sh
# cloudflared, caddy, jarvis-auth all auto-start via systemd on boot
bash scripts/preflight_gate.sh   # must show 22 PASS 0 FAIL 1 WARN (intentional)

# ★ Verify jarvis-memory:8056 durable audit trail (March 28):
curl -H "Authorization: Bearer $JARVIS_API_KEY" \
  http://localhost:8056/memories?limit=5
# Expected: recent durable BBB gate decision records

# ★ Verify confidence_decay metadata on msjarvis:5433 (March 28):
psql -h localhost -p 5433 -U msjarvis_user -d msjarvis \
  -c "SELECT COUNT(*) FROM gbim_entities WHERE confidence_decay IS NOT NULL;"
# Expected: row count > 0

# ★ Verify all 5 public hostnames returning 401 (April 2):
curl -s -o /dev/null -w "%{http_code}" https://egeria.mountainshares.us/chat
# Expected: 401
curl -s -o /dev/null -w "%{http_code}" https://chat.mountainshares.us/chat
# Expected: 401
```

---

## 39.3 End-to-End Chat Pipeline Benchmark

Test: Full `/chat` pipeline from user query through 21-model LLM ensemble, judge
pipeline, LM Synthesizer, and BBB output filter to final synthesized response —
measured on RTX 4070 GPU, March 22, 2026.

**Verified result (March 22, 2026 — GPU):**

```
Phase 2.5 (21-LLM ensemble, sequential): 88–115s (GPU, RTX 4070)
Phase 3 (4 judges, parallel): ~6–8s
Phase 3.5 (LM Synthesizer, llama3.1): ~2–8s
Phase 4.5 (BBB output check): ~2s
──────────────────────────────────────────────────
Total confirmed end-to-end (three runs):
  Run 1: 99.6s
  Run 2: 105.9s
  Run 3: 106.5s
Consistent range: 100–110s (single user, GPU)
```

**Benchmark comparison:**

| Benchmark | Previous (CPU) | Current (GPU, March 22) | Improvement |
|---|---|---|---|
| Phase 2.5 (21 LLMs) | 320–360s | 88–115s | ~72% reduction |
| Full pipeline | **~436s ⚠️ RETIRED/STALE — CPU-only, pre-March 22** | 99–107s | **~75% reduction** |

```
Async job endpoint: /chat/async — returns job_id immediately
/chat (POST) — synchronous, returns full response directly
Job state persistence: jarvis-redis — host port 6380 (container-internal 6379),
                       30-min TTL
Job status values: processing → complete (NOT 'done' — 'done' is incorrect and hangs)
Cancel capability: /chat/cancel/{job_id} — true asyncio.Task cancellation
BBB behavior: Phase 1.4 input filter — active, blocking — port 8016
             Phase 4.5 output filter — LOG+PASSTHROUGH (not blocking)
             ★ All Phase 1.4 and Phase 4.5 events durably logged at
               jarvis-memory:8056 (secured March 28)
             see §39.3.1 and Chapter 16 §16.9 for output BBB detail
Phase 1.45: community memory retrieval active on every /chat
  (top-5 autonomous_learner records prepended to enhanced_message
   via all-minilm:latest 384-dim semantic search, ChromaDB port 8002)
★ GBIM community fact validation: high-decay msjarvis:5433 entities
  flagged for episodic audit before use as context ground truth
  (confidence_decay metadata — restored March 28)
★ Public routing (April 2): chat.mountainshares.us → Cloudflare tunnel
  → Caddy :8085 → 18018 (unified gateway) → jarvis-main-brain:8050
  All hops confirmed; 401 enforced at Caddy/auth layer
```

> **⚠️ Stale figures retired:**
> - The ~436s figure from prior versions of this chapter was the CPU-only benchmark
>   before March 22, 2026. The RTX 4070 GPU is now active. **The ~436s figure is
>   RETIRED/STALE and must not appear in any current documentation without this label.**
> - Any reference to `jarvis-main-brain` at port **8010** is incorrect. The
>   unified gateway is at port **8050**. Port 8010 is `jarvis-wv-entangled-gateway`,
>   a separate degraded service.

### 39.3.1 Output BBB — Log+Passthrough Mode (March 22, 2026 — ★ re-confirmed April 2)

As of commit `18b8ddac` (March 22, 2026), Phase 4.5 output filtering operates in
**log+passthrough mode**. It does not block responses. The change was made because
the output BBB's ethical filter was flagging Ms. Jarvis's authentic maternal
Appalachian voice — phrases like "Child, that's just plain wrong!" — as ethical
violations. In the first confirmed public test session, 14 of 45 output responses
were blocked (31% false-positive rate).

```
Output BBB block rate: 0% (log+passthrough)
  was 31% — disabled for red team tuning phase
Flagged responses: logged to docker logs jarvis-main-brain
  prefix: ⚠️ BBB OUTPUT FLAGGED
  Preview logged: first 200 chars of flagged response
★ All Phase 4.5 log events: durably logged at jarvis-memory:8056
  (secured March 28 — _auth() confirmed, JARVIS_API_KEY set)
  Events survive container restarts and are independently queryable
Input BBB (Phase 1.4): FULLY ACTIVE — correctly tuned — port 8016
★ All Phase 1.4 gate decisions: durably logged at jarvis-memory:8056
```

Output BBB recalibration is a documented next-session priority.
See Chapter 16 §16.9 for full calibration status and the Appalachian voice
threshold recalibration work item.

**Safety posture during log+passthrough phase:** Output safety relies on five
active layers:
1. Phase 1.4 BBB input filter (active, blocking, port 8016 — ★ gate decisions durable at `jarvis-memory:8056`)
2. Judge pipeline `bbb_check_verdict` (live async httpx POST to port 8016, active on consensus answer — Chapter 33 §33.2 addendum)
3. LM Synthesizer identity guard — three layers active in `services/lm_synthesizer.py` (Chapter 33 §33.5.2 / Chapter 36 §36.5.2)
4. `normalize_identity` persona enforcement in `jarvis-main-brain` (port 8050)
5. Phase 4.5 BBB output — log+passthrough (active, non-blocking, logging all six filter results in `UltimateResponse.bbb_result` — ★ Phase 4.5 log events durable at `jarvis-memory:8056`)

**Assessment:** ✅ Full pipeline operational at GPU speeds. Three confirmed public
runs: 99.6s, 105.9s, 106.5s. Output BBB in safe log+passthrough mode during red
team phase. ★ `jarvis-memory:8056` durable audit trail active for both Phase 1.4
and Phase 4.5 events. ★ Public routing via chat.mountainshares.us → Cloudflare
→ Caddy :8085 → 18018 → 8050 fully operational as of April 2, 2026.

---

## 39.4 Memory Growth and ChromaDB Collections

Test: Collection record counts verified via `docker exec jarvis-chroma` ChromaDB
queries and autonomous learner growth rate tracking. All ChromaDB connections use
host port **8002** (`127.0.0.1:8002->8000/tcp`). Embedding model locked to
`all-minilm:latest` (384-dim) for all collections — do not substitute
`nomic-embed-text` (768-dim, incompatible with existing collections).

**★ Updated ChromaDB inventory (full audit — March 28, 2026):**

> **⚠️ Collection count update (★ March 28 full audit):** The March 25, 2026
> snapshot reported **31 collections, 6,665,093 total items**. The **confirmed
> collection count as of March 28, 2026 full audit is 40 active collections,
> 6,675,442 total vectors**, verified via full ChromaDB API enumeration. Any
> reference to 31 collections or 6,665,093 items reflects the March 25 snapshot
> and should be read as a prior baseline, not current state. The March 28 full
> audit is authoritative.

```
Collection                          Records    Status
─────────────────────────────────── ────────── ──────────────────────────────────────────
gbim_worldview_entities             5,416,521  ✅ Complete WV GBIM spatial corpus
                                               ★ confidence_decay metadata active (March 28)
autonomous_learner                  21,181+    ✅ Growing ~288/day from March 14 baseline
psychological_rag                   968        ✅ ★ RESTORED (March 28, 2026)
spiritual_texts                     23         ✅ Active
appalachian_cultural_intelligence   5          ✅ Active
GBIM_sample_rows                    5,000      ✅ Active
GBIM_sample                         3          ✅ Active
msjarvis-smoke                      1          ✅ Smoke test record
ms_jarvis_memory                    —          ✅ ★ CONFIRMED PRESENT (March 28 full audit)
msjarvis_docs                       2,348      ✅ Active — 45 verified Kanawha County
                                               community resources (synthetic Fayette
                                               entries removed March 28, 2026 —
                                               data governance policy established) +
                                               2,303 system docs
GBIM_Fayette_sample                 0          ⚠ Scaffolded — pending ingest
geospatialfeatures                  0          ⚠ Scaffolded — pending backfill ingest
[+ additional collections confirmed in March 28 full enumeration]

Total confirmed collection count (★ March 28, 2026 full audit): 40 active collections
Total vectors across all collections (★ March 28, 2026 full audit): 6,675,442
Prior baseline (March 25, 2026 snapshot): 31 collections / 6,665,093 items — SUPERSEDED
```

> **Data governance policy (established March 28, 2026):** No synthetic,
> inferred, or unverified data may be written to `local_resources` or ingested
> into the `msjarvis_docs` ChromaDB collection. All resources must be
> individually verified before seeding. The 45 Kanawha County resources in
> `msjarvis_docs` are verified. Two previously included Fayette County entries
> were synthetic placeholders and were removed March 28, 2026.
> Seed script: `scripts/seed_local_resources_chroma.py`.

> ★ **`psychological_rag` restoration note (March 28, 2026):** The
> `psychological_rag` collection has been restored to **968 documents**. This
> collection provides community wellbeing context to identity signal routing when
> psychological assessment is active. Prior documentation showing this collection
> as absent or degraded is superseded.

```
Embedding model (all collections): all-minilm:latest (384-dim, via jarvis-ollama:11434)
INCOMPATIBLE model (DO NOT USE): nomic-embed-text (768-dim — breaks all existing
                                 collections)
ChromaDB host port: 8002 (container-internal: 8000)
Auto-detect: docker port jarvis-chroma 8000/tcp
```

```
LANDOWNER BELIEFS: NOT in ChromaDB.
Served exclusively by jarvis-gbim-query-router (port 7205)
via mvw_gbim_landowner_spatial in msjarvisgis / gisdb (PostgreSQL port 5432).
```

**Assessment:** ✅ Core collections healthy. ChromaDB inventory confirmed at
**★ 40 active collections, 6,675,442 total vectors** as of March 28, 2026 full
audit. `autonomous_learner` growth confirmed. ★ `psychological_rag` restored to
968 docs. ★ `ms_jarvis_memory` collection confirmed present. Two known scaffolded
collections (0 records) awaiting backfill ingest — not blocking production.
Embedding dimension lock (`all-minilm:latest` / 384-dim) enforced. Data governance
policy established March 28, 2026.

---

## 39.5 PostgreSQL Production Databases

Test: Direct `psql` queries against production databases to verify table count,
row counts, and corpus integrity as of March 20–28, 2026.

### 39.5.1 `gisdb` / `msjarvisgis` — PostGIS Geospatial Database (Port 5432)

```
Database: msjarvisgis (also referred to as gisdb)
PostgreSQL version: 16 + PostGIS
Host port: 5432
Size: 91 GB
Tables: 501
★ ZCTA centroids: 993 (confirmed March 28, 2026 full audit)
gbimbeliefnormalized rows: 5,416,522 total beliefs
  — of which LANDOWNER_CORPORATE / LANDOWNER_GOVERNMENT: 20,593
  — worldview: eq1 (worldview_id: 3)
  — recorded_by: wv_tax_ingest_2025
  — belief_state: confirmed, belief_strength: 1.0
  — ingest timestamp: March 20, 2026 07:44 EDT
mvw_gbim_landowner_spatial: ✅ Materialized view — spatially indexed — live
gbim_entities: 402 rows (401 canonical landowner entities + 1 health_facility)
gbim_entity_clusters: 401 canonical entities written (Union-Find clustering)
gbim_entity_land_candidates: 511 candidates with total_acres > 1,000
```

### 39.5.2 `msjarvis` — Primary GBIM Belief Store (Port 5433)

```
Database: msjarvis
Host port: 5433
Content: ★ 5,416,521 GBIM entities with confidence_decay metadata
         (restored March 28, 2026), 80 epochs, 206 source layers
Role: Primary GBIM belief store — non-geospatial knowledge base
★ confidence_decay metadata: active — enables temporal confidence grading
  High-decay entities should be flagged for episodic audit before use
  as ground truth in queries, validation, or published communications
```

### 39.5.3 `jarvis-local-resources-db` — Community Resources (Port 5435)

```
Database: postgres (jarvis-local-resources-db container)
Host port: 5435 (127.0.0.1:5435->5432/tcp)
Container DSN: jarvis-local-resources-db:5432/postgres (corrected March 28, 2026)
/resolve endpoint: ✅ LIVE (confirmed March 28, 2026)
building_parcel_county_tax_mv: 7,354,707 rows
redteam_sessions: ✅ Active — session audit log (userid, created_at, was_blocked)
redteam_feedback: ✅ Active — tester feedback (rating, category, job_id)
local_resources table: 48 verified resources (Kanawha County + partial WV)
  — 45 Kanawha County verified resources (March 28 baseline)
  — 3 additional resources added since March 28
  — 7 WV county resources pending (Phase 2 data task — documented and deferred)
  — preflight gate WARN: 48/55 — intentional, not a failure
  — data governance policy: no synthetic or unverified entries permitted
  — seed script: scripts/seed_local_resources_chroma.py
```

**Assessment:** ✅ All three PostgreSQL databases confirmed active. Materialized
view live. Landowner beliefs ingested and spatially indexed. Red team audit tables
confirmed active. `jarvis-local-resources-db` DSN corrected March 28, 2026.
★ `msjarvis:5433` `confidence_decay` metadata active — temporal confidence grading
available for all GBIM entity validation queries. ★ `local_resources` at 48/55 —
7-county Phase 2 data task documented, deferred, and recorded as intentional WARN.

---

## 39.6 ★ GBIM Landowner Query Capability — Verified (March 20, 2026)

This section documents the first fully verified production capability of
`jarvis-gbim-query-router` (port 7205): the ability to answer natural language
questions about corporate and government land ownership in West Virginia using a
deterministic PostgreSQL-native path through `mvw_gbim_landowner_spatial` in
`gisdb` (port **5432**).

> **Container name correction (March 28, 2026):** The running container is named
> `jarvis-gbim-query-router` (not `gbim_query_router`). The host port is
> `127.0.0.1:7205->7205/tcp`. All prior references using the underscore-only
> form as a container name are stale.

> ★ **`confidence_decay` note (March 28, 2026):** Landowner beliefs in
> `gbimbeliefnormalized` are sourced from the 2025 WV tax assessor ingest
> (`recorded_by: wv_tax_ingest_2025`, `belief_strength: 1.0`, `belief_state:
> confirmed`). These records carry high confidence by design. The `confidence_decay`
> metadata on `msjarvis:5433` applies to the non-geospatial GBIM store and does
> not affect the `gisdb:5432` landowner belief corpus, which is separately governed
> by the data governance policy and assessor provenance chain documented in §39.6.3.

This capability was added March 20, 2026. It did not exist in any prior
operational evaluation snapshot.

### 39.6.1 What Was Tested

Two query patterns were verified against live production data:

**Pattern 1 — Statewide top landowners:**

```python
import httpx
statewide = httpx.post(
    "http://127.0.0.1:7205/query",
    json={
        "question": "Who are the largest landowners in West Virginia?",
        "mode": "landowner_gbim",
        "route_type": "parcel_ownership",
        "scope": "statewide",
        "limit": 20
    }
)
```

**Pattern 2 — County-scoped landowners:**

```python
county = httpx.post(
    "http://127.0.0.1:7205/query",
    json={
        "question": "Who owns the most land in Fayette County?",
        "mode": "landowner_gbim",
        "route_type": "parcel_ownership",
        "county": "Fayette",
        "limit": 20
    }
)
```

Both confirmed operational March 20, 2026.

### 39.6.2 Underlying Corpus — Verified Terminal Output

The landowner belief corpus backing `jarvis-gbim-query-router` was built in three
verifiable stages on March 20, 2026, all observed directly from terminal output:

**Stage 1: Entity candidate extraction**
511 candidate entities with `total_acres > 1,000` extracted from
`gbim_entity_land_candidates` via direct `psql` query to `gisdb` (port **5432**).

**Stage 2: Fuzzy clustering via Union-Find + RapidFuzz**
`rapidfuzz 3.14.3` applied with `token_sort_ratio` scorer at `score_cutoff=85`.
Result: 401 canonical landowner entities written to `gbim_entity_clusters`.
Top 30 canonical entities by `total_acres` (verified terminal output):

```
canonical_name                                  variant_count  total_acres  total_parcels  county_count
WEYERHAEUSER COMPANY                            1              242,892.1    518            4
POCAHONTAS SURFACE INTERSTS LLC                 25             205,113.2    393            2
HEARTWOOD FORESTLAND FUND VI LLC                7              174,608.8    462            11
LYME MOUNTAINEER TIMBERLANDS I LLC              7              138,873.2    481            3
PENN VIRGINIA OPERATING CO LLC                  2              112,343.8    341            7
WESTERN POCAHONTAS PROPERTIES LIMITED PARTNER.  4              91,658.3     343            9
ALLEGHENY FORESTLANDS LLC                       5              63,886.2     292            14
MIKE ROSS INC                                   2              59,104.6     1,043          27
COASTAL FOREST RESOURCES COMPANY                1              53,835.3     251            12
BECKWITH LUMBER COMPANY INC                     3              44,520.5     329            8
SCIOTO LAND CO LLC                              2              43,075.5     521            7
ROWLAND LAND COMPANY LLC TR #574                11             40,255.0     169            6
PARDEE & CURTIN TIMBERLANDS 229                 15             38,124.1     36             4
BLUE EAGLE LAND LLC                             1              36,526.4     56             2
LEXINGTON COAL COMPANY LLC                      5              32,926.0     391            10
ALAWEST INC                                     1              32,817.9     154            1
WPP LLC                                         1              30,285.7     70             7
SUN LUMBER COMPANY THE                          3              27,852.4     209            4
BEAVER COAL COMPANY LIMITED                     4              27,435.6     127            2
PENN VIRGINIA COAL COMPANY                      2              25,777.9     34             1
BLUESTONE RESOURCES INC                         1              25,750.9     26             2
SHONK LAND CO LLC                               2              25,291.1     33             2
QUERCUS WV LLC ICO: ORBIS INC                   1              24,807.6     71             1
SHEPARD BOONE COAL COMPANY LLC                  1              22,656.7     75             1
WACO OIL & GAS CO INC                           1              21,161.4     279            23
PH TIMBER LLC                                   2              19,192.2     64             6
PLC TIMBERLANDS LLC                             1              18,843.2     33             2
PUBLIC LAND CORP OF WVA                         6              18,697.1     109            6
ARK LAND KH LLC                                 2              17,613.8     153            5
NUTTALL LLC C/O TAX DEPT                        1              15,694.3     26             1
```

**Stage 3: `gbim_entities` promotion and belief ingest**
401 canonical entities promoted to `gbim_entities` (402 total rows including 1
health_facility). Beliefs ingested to `gbimbeliefnormalized` as
`LANDOWNER_CORPORATE` / `LANDOWNER_GOVERNMENT` proposition codes with
`worldview_id: 3` (eq1), `belief_strength: 1.0`, `recorded_by: wv_tax_ingest_2025`.

```
Total LANDOWNER beliefs in gbimbeliefnormalized: 20,593
All records: belief_strength = 1.0, belief_state = confirmed
Ingest timestamp: 2026-03-20 07:44 EDT
recorded_by: wv_tax_ingest_2025
```

### 39.6.3 Routing Architecture — Why No ChromaDB

`jarvis-gbim-query-router` is the only RAG-class service in the Ms. Jarvis stack
that does not use ChromaDB. This is a deliberate architectural decision:

- Corporate and government land ownership has exact, deterministic answers in
  `gbimbeliefnormalized`
- Approximate vector nearest-neighbor search (384-dim all-minilm) would introduce
  unnecessary ambiguity into questions that have exact answers
- SQL aggregation over `mvw_gbim_landowner_spatial` is faster, more accurate, and
  fully auditable to specific rows
- Every answer carries nine-axis provenance: canonical entity name, parcel count,
  total area, county scope, belief strength, worldview, `feature_ref`,
  `entity_geodbid`, `recorded_by`
- ★ Landowner beliefs are governed by the assessor provenance chain and data
  governance policy — not by `confidence_decay` metadata (which applies to the
  non-geospatial `msjarvis:5433` GBIM store). The two provenance systems are
  complementary and track different confidence dimensions.

### 39.6.4 Capability Statement (Verified)

As of March 20, 2026, Ms. Jarvis can:

- ✅ Answer "Who are the largest landowners in West Virginia?" with a ranked list
  of canonical corporate entities, parcel counts, and total acreage — sourced
  from 20,593 verified belief records in `gbimbeliefnormalized`
- ✅ Answer "Who owns the most land in [County]?" scoped to any WV county in the
  `mvw_gbim_landowner_spatial` materialized view
- ✅ Return results with full assessor provenance traceable to specific rows in
  `gisdb` (port **5432**)
- ✅ Resolve name variants via the Union-Find clustering layer before query time
- ✅ Route these queries entirely within PostgreSQL — no LLM inference, no
  ChromaDB lookup, no web research
- ✅ Log every query result with full SQL provenance for audit purposes

---

## 39.7 Verification Script Coverage

Test: `VERIFYANDTEST.sh` and `scripts/preflight_gate.sh` run against live stack.

**★ Certified closed state — April 2, 2026 (22 PASS / 0 FAIL / 1 WARN):**

```
scripts/preflight_gate.sh — ★ CERTIFIED CLOSED April 2, 2026:
  ✅ PASS: 22   ❌ FAIL: 0   ⚠️ WARN: 1 (intentional)

  ✅  1. Container count ≥96   [★ UPDATED April 2 — was ≥79; 101 containers running]
  ✅  2. Zero 0.0.0.0 exposures  [★ ALL ELIMINATED April 2]
  ✅  3. Gateway healthy (port 8050)
  ✅  4. BBB healthy (port 8016)
  ✅  5. GBIM Router healthy (port 7205)
  ✅  6. Identity rules in LM Synthesizer prompt
  ✅  7. BBB steg fix deployed
  ✅  8. jarvis-judge-truth signing keys
  ✅  9. jarvis-judge-consistency signing keys
  ✅ 10. jarvis-judge-alignment signing keys
  ✅ 11. jarvis-judge-ethics signing keys
  ✅ 12. jarvis-judge-pipeline signing keys
  ✅ 13. Community resources: 45 verified Kanawha County baseline
  ✅ 14. msjarvis_docs: 2,348 items
  ✅ 15. redteam_sessions table exists
  ✅ 16. Invite tokens: 4 active
  ✅ 17. mvw_gbim_landowner_spatial: 20,593 rows
  ✅ 18. Caddy gateway (port 8085 → 18018 ★ FIXED April 2) — CORS active
  ✅ 19. Auth service (port 8055) — token validation ready
  ✅ 20. Cloudflare tunnel — ★ HEALTHY (warn cleared April 2)
  ✅ 21. Chroma reachability (v2 API, port 8002)
  ✅ 22. WOAH container active (port 7012)
  ⚠️ WARN: local_resources 48/55 — 7 WV counties Phase 2 data task
             INTENTIONAL — documented and deferred

Previous checks 23 and 24 (RAG endpoint, consciousness bridge)
promoted to integration-level validation or subsumed into check #1 / #3.
──────────────────────────────────────────────────────────
RESULT: 22 PASS 0 FAIL 1 WARN (intentional)  ★ CHAPTER 39 CERTIFIED CLOSED
```

> **Preflight check #1 update (★ April 2, 2026):** Threshold updated from `≥79`
> to `≥96`. Current running container count is **101**.

> **Preflight check #18 update (★ April 2, 2026):** Caddyfile `:8085` self-loop
> fixed — now correctly proxies to port 18018 (unified gateway). `cloudflared`
> config updated from hardcoded 8443 to 8085.

> **Preflight check #20 update (★ April 2, 2026):** Cloudflare tunnel WARN
> cleared — tunnel confirmed HEALTHY.

> **Intentional WARN — `local_resources 48/55`:** The `local_resources` table
> currently holds 48 verified resources; the preflight target is 55 (covering all
> major WV counties). The 7-county gap is a Phase 2 data task requiring field
> verification — no synthetic data may be added. This WARN is documented,
> intentional, and does not represent a system failure.

> ★ **Suggested additions for next preflight gate revision:**
> - Check 23: `jarvis-memory:8056` reachable and `_auth()` confirmed
> - Check 24: `msjarvis:5433` `confidence_decay` metadata present
> - Check 25: ChromaDB collection count ≥ 40
> - Check 26: `psychological_rag` collection ≥ 968 docs

**Assessment:** ✅ **Chapter 39 CERTIFIED CLOSED** — April 2, 2026. Pre-flight
gate at **22 PASS / 0 FAIL / 1 WARN (intentional)**. All 8 preflight gate bugs
fixed. Container threshold updated to ≥96. All 0.0.0.0 exposures eliminated.
Cloudflare tunnel HEALTHY. All 5 public hostnames live and token-enforced.

---

## 39.8 Known Gaps and Pending Work

### 39.8.1 Open Item Status Table (★ updated April 2, 2026)

| OI ID | Item | Status | Notes |
|---|---|---|---|
| OI-02 | Output BBB Phase 4.5 recalibration | ⚠️ **OPEN** | Log+passthrough mode remains in effect (commit `18b8ddac`). Target: < 5% false-positive rate before re-enabling blocking. ★ Phase 4.5 log events now durably logged at `jarvis-memory:8056`. See Chapter 16 §16.9. |
| OI-05 | Conversation memory (formal wiring) | ⚠️ **PARTIALLY RESOLVED** | Emergent context observed in March 25 end-to-end production test. Formal wiring incomplete. See §39.11. |
| OI-10 | Meaning-oriented pipeline (consciousness bridge, WOAH, Chroma) | ✅ **MATERIALLY ADVANCED** | All three confirmed operational March 25, 2026. WOAH baseline harness in place April 2. See §39.11 and Chapter 25 §25.9. |
| OI-11 | StarCoder2 exclusion (0-char on community queries) | ⚠️ **OPEN** | HTTP 200, 0-char responses on community queries. Excluded from consensus. See Chapter 35 §35.3. |
| OI-29 | WOAH Pydantic schema formalization | ⚠️ **STUB OPERATIONAL — SCHEMA DEFERRED** | WOAH rebuilt as stdlib stub — confirmed operational on `qualia-net`. Schema formalization deferred. |
| OI-36-A | Gateway token enforcement | ✅ **CLOSED April 2** | All 5 public hostnames return 401 without valid token. Token enforcement confirmed on all chat endpoints. |
| OI-36-B | Role-based route restriction (403) | ⚠️ OPEN | Blocked by OI-36-A — now unblocked; implementation deferred. |
| OI-38-A | Token enforcement on public endpoint | ✅ **CLOSED April 2** | All public endpoints return 401 without a valid token. chat.mountainshares.us CNAME added and confirmed. |
| OI-38-B | Phase 4.5 output BBB not blocking | ⚠️ OPEN | Same as OI-02. ★ Phase 4.5 log events now durably logged at `jarvis-memory:8056`. |

### 39.8.2 Non-OI Data Gaps and Pending Work (★ April 2, 2026)

| Item | Status | Notes |
|---|---|---|
| Output BBB recalibration | ⚠️ OPEN | 31% false-positive rate on maternal/exclamatory Appalachian tone confirmed; threshold adjustment needed. ★ Phase 4.5 log events durable at `jarvis-memory:8056`. See Chapter 16 §16.9. |
| Role-based route restriction (403) | ⚠️ OPEN | See OI-36-B. Token enforcement (OI-36-A / OI-38-A) is now closed. |
| `local_resources` 7-county gap | ⚠️ INTENTIONAL WARN | 48/55 resources — Phase 2 data task requiring field verification; no synthetic data permitted |
| `geospatialfeatures` ChromaDB | ⚠️ 0 records | Scaffolded — backfill ingest pending |
| `GBIM_Fayette_sample` ChromaDB | ⚠️ 0 records | Scaffolded — pending ingest |
| `appalachian_cultural_intelligence` | ⚠️ 5 items | Minimal — needs expansion |
| `spiritual_texts` | ⚠️ 23 items | Active but minimal |
| ChromaDB additional collections | ⚠️ ENUMERATED — individual counts pending | ★ 40 total confirmed in March 28 full audit; individual record counts for collections beyond the named set not yet fully catalogued |
| `jarvis-steward` | ⚠️ No host binding | Running (internal only); not wired into main pipeline |
| `jarvis-hilbert-gateway` | ⚠️ No host binding | Confirmed running (internal only); pipeline wiring not yet documented |
| `jarvis-hilbert-state` | ✅ Port conflict resolved | Remapped to port 8092 (April 2, 2026) |
| `jarvis-memory` (port 8056) | ★ **SECURED** | `_auth()` confirmed, `JARVIS_API_KEY` set, durable BBB audit trail active. Full service role documentation and pipeline integration beyond durable audit not yet complete. |
| `jarvis-eeg-delta/theta/beta` (8073–8075) | ⚠️ Undocumented | EEG layer confirmed running; service architecture, endpoints, and pipeline role not yet documented |
| MountainShares tier (8080–8084) | ⚠️ DEPLOYED — endpoints unverified | All five containers confirmed running; individual endpoint health and pipeline integration not yet validated |
| `VERIFYANDTEST` regression poll | ⚠️ WARN | "WV capital city" test times out under load; cached-first approach mitigates but does not resolve |
| MySQL schema dump | ⚠️ Undocumented | Port 3307 (`127.0.0.1:3307->3306/tcp`) confirmed running; schema dump not yet committed to `docs/` |
| Government landowner proposition codes | ⏳ Pending | `LANDOWNER_GOVERNMENT` records pending separate ingest pass |
| `mvw_gbim_landowner_spatial` refresh cadence | ⏳ Pending | Materialized view refresh not yet defined (currently manual) |
| RAG embedding end-to-end validation | ⚠️ IN PROGRESS | RAG endpoint reachable (`/query`, port 8003, HTTP 200); embedding roundtrip not yet fully validated |
| `jarvis-neurobiological-master` reachability | ⚠️ OPEN | Confirmed unreachable; Chroma health check rerouted around it (Ch. 25 Patch 1); root cause unresolved |
| ★ `confidence_decay` high-decay entity rate monitoring | ⏳ Pending | `confidence_decay` metadata active on `msjarvis:5433`; alerting for elevated high-decay entity rates during validation not yet implemented |

None of the above block current production operation. All 5 public endpoints are
live and token-enforced as of April 2, 2026.

---

## 39.9 Operational Summary Table (★ April 2, 2026 — CERTIFIED CLOSED)

| Capability | Status | Key Metric |
|---|---|---|
| Full 101-container stack startup | ✅ Verified | `docker compose up -d` + `jarvis_startup.sh` |
| External systemd services | ✅ Verified | Caddy 8085→18018 ★ FIXED, jarvis-auth 8055, cloudflared ★ HEALTHY — all auto-start on boot |
| End-to-end chat pipeline (GPU) | ✅ Verified | 99–107s (RTX 4070) — CPU baseline ~436s **RETIRED/STALE** |
| All 5 public HTTPS endpoints | ✅ LIVE + TOKEN-ENFORCED | egeria.mountainshares.us, chat.mountainshares.us, + 3 more — all return 401 without token |
| Cloudflare tunnel | ★ ✅ HEALTHY | Warn cleared April 2, 2026 |
| Caddyfile routing | ★ ✅ FIXED | :8085 self-loop resolved → proxies to 18018 |
| Async job management | ✅ Verified | Redis-backed (host port 6380), 30-min TTL, true asyncio cancel, status key = `'complete'` |
| BBB input filter (Phase 1.4) | ✅ Active, blocking | Port 8016 — six filters — ★ gate decisions durable at `jarvis-memory:8056` |
| BBB output filter (Phase 4.5) | ⚠️ Log+passthrough | Port 8016 — logging only, not blocking during tuning — ★ Phase 4.5 log events durable at `jarvis-memory:8056` |
| `jarvis-memory:8056` durable audit | ★ ✅ SECURED | `_auth()` confirmed, `JARVIS_API_KEY` set, BBB gate decisions persistently logged, survive restarts |
| Phase 1.45 community memory injection | ✅ Verified | top-5 `autonomous_learner` records on every `/chat` via ChromaDB port 8002 |
| Autonomous learner growth | ✅ Verified | 21,181+ records, ~288/day — host port **8020** |
| `msjarvis_docs` collection | ✅ Verified | 2,348 items — 45 verified Kanawha County resources + 2,303 system docs |
| ChromaDB confirmed collection inventory | ★ ✅ Updated | **40 active collections, 6,675,442 total vectors** (full audit March 28) — host port 8002 |
| `psychological_rag` collection | ★ ✅ RESTORED | 968 docs — restored March 28, 2026 |
| `ms_jarvis_memory` collection | ★ ✅ CONFIRMED | Present in 40-collection inventory — March 28 full audit |
| PostgreSQL `gisdb` / `msjarvisgis` corpus | ✅ Verified | 91 GB, 501 tables, 993 ZCTA centroids, 5,416,522 beliefs — port **5432** |
| PostgreSQL `msjarvis` GB````markdown
| PostgreSQL `msjarvis` GBIM store | ★ ✅ Restored | 5,416,521 GBIM entities with `confidence_decay` metadata, 80 epochs — port 5433 |
| PostgreSQL `jarvis-local-resources-db` | ✅ Verified | 7,354,707 parcel rows; red team audit tables active — port 5435; DSN corrected March 28 |
| `jarvis-local-resources` `/resolve` endpoint | ✅ LIVE | Confirmed March 28, 2026 — port 8006 |
| `local_resources` 48/55 | ⚠️ INTENTIONAL WARN | 7 WV counties — Phase 2 data task, documented and deferred |
| GBIM landowner query (`jarvis-gbim-query-router`) | ✅ Verified | 20,593 beliefs, 401 canonical entities, port 7205 |
| Judge pipeline (5 containers) | ✅ Verified | Compose-managed; coordinator 7239, judges 7230–7233 |
| 21-model LLM ensemble | ✅ Verified | 21/22 responded within budget — March 22, 2026 |
| Identity guard (LM Synthesizer, 3 layers) | ✅ Verified | Model names blocked; Egeria identity confirmed under adversarial probe |
| Red team tokens | ✅ Active | 4 active (carrie_admin ×2, hayden_test ×2) — `jarvis-redis` host port 6380 |
| Pre-flight gate | ★ ✅ CERTIFIED CLOSED | **22 PASS 0 FAIL 1 WARN (intentional)** — April 2, 2026 |
| Preflight gate container threshold | ★ ✅ UPDATED | ≥79 → ≥96 (101 containers now running) |
| All 0.0.0.0 exposures | ★ ✅ ELIMINATED | Zero exposures across all 101 containers |
| `jarvis-hilbert-state` port conflict | ★ ✅ RESOLVED | Remapped to port 8092 |
| Consciousness pipeline (Chroma + WOAH + Bridge) | ✅ Operational | Confirmed March 25, 2026 — all three stages active (OI-10 materially advanced) |
| Conversation memory (emergent) | ⚠️ Partial | Prior context referenced in March 25 test; formal wiring incomplete (OI-05 partially resolved) |
| RAG embedding end-to-end | ⚠️ In progress | Endpoint reachable at `/query` port 8003; embedding roundtrip in final-stage fix |
| MountainShares/Commons/DAO tier | ⚠️ DEPLOYED — endpoints unverified | 5 containers live (ports 8080–8084); individual health not yet validated |
| EEG layer (delta/theta/beta) | ⚠️ Running — undocumented | 3 containers live (ports 8073–8075); architecture and pipeline role not yet documented |
| Zero `0.0.0.0` exposures | ★ ✅ ELIMINATED | All 101 containers localhost-only — April 2, 2026 |
| Data governance policy | ✅ Established | March 28, 2026 — no synthetic/unverified data in `local_resources` or `msjarvis_docs` |
| ★ `confidence_decay` metadata | ✅ Active | `msjarvis:5433` — temporal confidence grading available for all GBIM entity validation queries |
| OI-36-A / OI-38-A token enforcement | ★ ✅ CLOSED | All 5 public hostnames return 401 without valid token — April 2, 2026 |

---

## 39.10 First Public End-to-End Verification — March 22, 2026

This section documents the first confirmed public end-to-end chat session via
https://egeria.mountainshares.us, March 22, 2026. Three consecutive queries were
submitted through the Cloudflare-tunneled Caddy gateway → `jarvis-auth` token
validation → `jarvis-main-brain` port 8050 → full 9-phase pipeline → synthesized
response in Ms. Egeria Jarvis voice. All three runs completed in the 99–107s GPU
range. Response content included authentic Appalachian maternal voice, confirmed
WV geographic context, and no identity leakage (no "As LLaMA," "As Mistral," or
"As an AI" phrases). ★ Stack continuity confirmed March 28 — 96/96 containers
Up, `jarvis-memory:8056` durable audit trail active. ★ Stack further confirmed
April 2, 2026 — 101/101 containers Up, all 5 public hostnames live and
token-enforced, Cloudflare tunnel HEALTHY, routing chain Caddy :8085 → 18018
→ 8050 fully operational.

**★ Full public routing chain (confirmed April 2, 2026):**

```
User → chat.mountainshares.us (CNAME added April 2)
     → Cloudflare tunnel (HEALTHY)
     → Caddy :8085 (self-loop fixed → proxies to 18018)
     → jarvis-unified-gateway :18018
     → jarvis-main-brain :8050
     → 9-phase pipeline (99–107s GPU)
     → UltimateResponse (6-layer consciousness)
     → BBB Phase 4.5 log+passthrough
     → Synthesized response in Egeria Jarvis voice

All hops: ✅ confirmed
Token enforcement: 401 returned at Caddy/jarvis-auth layer without valid token
```

---

## 39.11 Consciousness Pipeline Confirmation — March 25, 2026

Following the five-patch sprint (Chapter 25 §25.9 / Chapter 40 §40-H), the full
consciousness pipeline was confirmed operational for the first time:

```
Chroma v2 API (port 8002):            CONNECTED — /api/v2/heartbeat HTTP 200
                                       ★ Full audit March 28: 40 collections /
                                         6,675,442 total vectors
WOAH (port 7012, stdlib stub):         ACTIVE — {"status": "ok"}
Consciousness bridge (internal 8020):  OPERATIONAL — 3 patches applied
RAG server (host port 8003):           OPERATIONAL — /query confirmed
Unified gateway (port 18018):          OPERATIONAL — dict.lower() guard patched
jarvis-ollama (11434):                 REACHABLE from RAG server container
jarvis-neurobiological-master (8018):  ⚠️ UNREACHABLE — Chroma health rerouted
                                          around it (Ch. 25 Patch 1); root cause open
★ jarvis-memory (port 8056):           SECURED — _auth() confirmed, JARVIS_API_KEY set
                                          Durable BBB audit trail active
                                          All gate decisions survive container restarts
★ psychological_rag (ChromaDB):        RESTORED — 968 documents
★ ms_jarvis_memory (ChromaDB):         CONFIRMED PRESENT
★ Public routing (April 2):            Caddy :8085 → 18018 → 8050 CONFIRMED
★ Cloudflare tunnel (April 2):         HEALTHY
★ All 5 hostnames (April 2):           LIVE — 401 token enforced
```

During the March 25 production end-to-end test, emergent conversation context
carryover was observed (OI-05 PARTIALLY RESOLVED). Formal conversation memory
wiring remains incomplete. The `autonomous_learner` collection provides semantic
similarity recall but is not a session-scoped conversation buffer.

---

## 39.12 Complete Verified Container Inventory (★ April 2, 2026 — 101 containers)

Full stack verified April 2, 2026 — 101 containers total, zero `0.0.0.0`
exposures. Prior March 28 baseline was 96 containers.

### Core Orchestration

| Container | Host Port | Internal Port | Status |
|---|---|---|---|
| `jarvis-main-brain` | 8050 | 8050 | ✅ Healthy |
| `jarvis-brain-orchestrator` | 17260 | 7260 | ✅ Healthy |
| `jarvis-unified-gateway` | 18018 | 8001 | ✅ Running |
| `jarvis-semaphore` | 8030 | 8030 | ✅ Running |
| `jarvis-steward` | none | internal | ✅ Running — not wired to pipeline |
| `jarvis-hilbert-state` | ★ **8092** | 8092 | ✅ Running — ★ remapped April 2 (prior port conflict resolved) |

### LLM Fabric

| Container | Host Port | Status | Notes |
|---|---|---|---|
| `jarvis-ollama` | 11434 | ✅ Running | 26 models, 20 GB limit |
| `jarvis-20llm-production` | 8008 | ✅ Running | 21/22 contributing |
| `jarvis-lm-synthesizer` | none (8001 internal) | ✅ Running | Phase 3.5 |
| `llm1-proxy` – `llm22-proxy` | 8201–8222 | ✅ Running | 22 slots; StarCoder2 0-char; BakLLaVA disabled |

### Safety and Validation

| Container | Host Port | Internal Port | Status |
|---|---|---|---|
| `jarvis-blood-brain-barrier` | 8016 | 8016 | ✅ Running — 6 filters — ★ gate decisions durable at `jarvis-memory:8056` |
| `jarvis-69dgm-bridge` | 19000 | 9000 | ✅ Running — 23 connectors, 3 stages, 69 ops |
| `jarvis-constitutional-guardian` | 8091 | 8091 | ✅ Running |
| `jarvis-psychology-services` | 8019 | 8019 | ✅ Running |
| `psychological_rag_domain` | 9006 | 8006 | ✅ Running — ★ 968 docs restored March 28 |

### Consciousness and Neurobiological Stack

| Container | Host Port | Internal Port | Status |
|---|---|---|---|
| `jarvis-neurobiological-master` | none | 8018 | ⚠️ Running but UNREACHABLE |
| `jarvis-consciousness-bridge` | none | 8020 | ✅ Running — internal only |
| `jarvis-qualia-engine` | none | 8017 | ✅ Running |
| `jarvis-i-containers` | 8015 | 8015 | ✅ Running |
| `jarvis-fifth-dgm` | 4002 | 4002 | ✅ Running |
| `jarvis-mother-protocols` | none | 4000 | ✅ Running |
| `jarvis-temporal-consciousness` | none | 7007 | ✅ Running |
| `jarvis-fractal-consciousness` | none | 8027 | ✅ Running |
| `jarvis-swarm-intelligence` | none | 8021 | ✅ Running |
| `jarvis-autonomous-learner` | **8020** | 8020 | ✅ Running — **port 8020, not 8425** |
| `jarvis-hippocampus` | none | internal | ✅ Running |
| `jarvis-toroidal` | 8025 | 8025 | ✅ Running — Chroma↔GIS sync |
| `jarvis-woah` | none | 7012 | ✅ Running — stdlib stub, qualia-net |

### EEG Layer

| Container | Host Port | Status | Notes |
|---|---|---|---|
| `jarvis-eeg-delta` | 8073 | ✅ Running | Architecture and pipeline role pending documentation |
| `jarvis-eeg-theta` | 8074 | ✅ Running | Architecture and pipeline role pending documentation |
| `jarvis-eeg-beta` | 8075 | ✅ Running | Architecture and pipeline role pending documentation |

### Memory (secured March 28, 2026)

| Container | Host Port | Status | Notes |
|---|---|---|---|
| `jarvis-memory` | 8056 | ✅ Running — ★ SECURED | `_auth()` confirmed, `JARVIS_API_KEY` set; durable BBB audit trail active; all Phase 1.4 + Phase 4.5 gate decisions persistently logged; records survive container restarts |

### NBB Subconscious Layer (13 containers)

| Container | Host Port | Internal Port | Status |
|---|---|---|---|
| `msjarvis-rebuild-nbb_i_containers-1` | 8101 | 7005 | ✅ Running |
| `msjarvis-rebuild-nbb_consciousness_containers-1` | 8102 | 7002 | ✅ Running |
| `msjarvis-rebuild-nbb_spiritual_root-1` | 8103 | 7003 | ✅ Running |
| `nbb_woah_algorithms` | none | internal | ✅ Running |
| `msjarvis-rebuild-nbb_prefrontal_cortex-1` | 8105 | 7005 | ✅ Running |
| `msjarvis-rebuild-nbb_heteroglobulin_transport-1` | 8106 | 7006 | ✅ Running |
| `msjarvis-rebuild-nbb_mother_carrie_protocols-1` | 8107 | 7007 | ✅ Running |
| `msjarvis-rebuild-nbb_pituitary_gland-1` | 8108 | 7008 | ✅ Running |
| `msjarvis-rebuild-nbb_spiritual_maternal_integration-1` | 8109 | 7009 | ✅ Running |
| `msjarvis-rebuild-nbb_subconscious-1` | 8112 | 7011 | ✅ Running |
| `msjarvis-rebuild-nbb_blood_brain_barrier-1` | 8301 | 7001 | ✅ Running |
| `msjarvis-rebuild-nbb_darwin_godel_machines-1` | 8302 | 7003 | ✅ Running |
| `msjarvis-rebuild-nbb_qualia_engine-1` | 8303 | 7008 | ✅ Running |

### Judge Pipeline (5 containers — all compose-managed)

| Container | Host Port | Status |
|---|---|---|
| `jarvis-judge-truth` | 7230 | ✅ Running |
| `jarvis-judge-consistency` | 7231 | ✅ Running |
| `jarvis-judge-alignment` | 7232 | ✅ Running |
| `jarvis-judge-ethics` | 7233 | ✅ Running |
| `jarvis-judge-pipeline` | 7239 | ✅ Running |

### RAG and Retrieval Services

| Container | Host Port | Internal Port | Status | Notes |
|---|---|---|---|---|
| `jarvis-rag-server` | **8003** | **8003** | ✅ Running | `/query` confirmed — internal port is 8003, not 8016 |
| `jarvis-gis-rag` | 8004 | 8004 | ✅ Running | Spatial/benefits RAG |
| `jarvis-spiritual-rag` | 8005 | 8005 | ✅ Running | |
| `jarvis-local-resources` | 8006 | 8006 | ✅ Running | `/resolve` live (March 28) |
| `jarvis-intake-service` | 8007 | 8007 | ✅ Running | |
| `jarvis-web-research` | 8090 | 8090 | ✅ Running | ★ 0.0.0.0 exposure eliminated April 2 |
| `jarvis-aaacpe-rag` | 8032 | 8032 | ✅ Running | |
| `jarvis-aaacpe-scraper` | 8033 | 8033 | ✅ Running | |
| `jarvis-wv-entangled-gateway` | 8010 | 8010 | ⚠️ Degraded | Not the primary entrypoint |
| `jarvis-agents-service` | none | 8005 | ✅ Running | Internal only |
| `jarvis-hilbert-gateway` | none | internal | ✅ Running | Pipeline wiring undocumented |

### MountainShares / Commons / DAO Tier (DEPLOYED — March 28, 2026)

| Container | Host Port | Status |
|---|---|---|
| `jarvis-mountainshares-coordinator` | 8080 | ✅ Running — endpoints unverified |
| `jarvis-commons-gamification` | 8081 | ✅ Running — endpoints unverified |
| `jarvis-dao-governance` | 8082 | ✅ Running — endpoints unverified |
| `jarvis-ms-token-service` | 8083 | ✅ Running — endpoints unverified |
| `jarvis-community-stake-registry` | 8084 | ✅ Running — endpoints unverified |

### Data Stores

| Container / Service | Host Port | Type | Status | Notes |
|---|---|---|---|---|
| `jarvis-chroma` | 8002 | ChromaDB | ✅ Healthy | ★ 40 active collections, 6,675,442 total vectors (full audit March 28) |
| `jarvis-redis` | 6380 | Redis 7 | ✅ Healthy | Job state, status key `'complete'` |
| `jarvis-local-resources-db` | 5435 | PostGIS 15 | ✅ Running | DSN corrected March 28 |
| `neo4j` | 7687, 7475 | Neo4j 5.13 | ✅ Running | Identity graphs |
| `mysql` | 3307 | MySQL 8.2 | ✅ Running | Schema undocumented |
| Host PostgreSQL `msjarvisgis` | 5432 | PostGIS 16 | ✅ Verified | 91 GB, 501 tables, 993 ZCTA centroids, 5,416,522 beliefs |
| Host PostgreSQL `msjarvis` | 5433 | PostgreSQL 16 | ✅ Running | ★ 5,416,521 GBIM entities with `confidence_decay` metadata — restored March 28 |

### Infrastructure

| Container | Host Port | Status | Notes |
|---|---|---|---|
| `ipfs/kubo` | 5001 | ✅ Running | MountainShares/Commons content addressing |
| `jarvis-crypto-policy` | 8099 | ✅ Running | Added to compose March 22 |
| `jarvis-ingest-api` | none | ✅ Running | Added to compose March 22 |
| `jarvis-ingest-watcher` | none | ✅ Running | Added to compose March 22 |
| `jarvis-otel-collector` | 4317 / 4318 | ✅ Running | ★ Added April 1 — logging exporter active; no spans ingested yet |

---

## 39.13 ★ Session Contract Reference — April 2, 2026 (CERTIFIED CLOSED)

All significant operational state changes confirmed in this chapter are committed
to the session contract record for audit continuity:

| Change | Committed To |
|---|---|
| Chapter 39 certified closed — 22 PASS 0 FAIL 1 WARN (intentional) | `msjarvis-public-docs/docs/contract/SESSION-2026-04-02.md` |
| 101 containers confirmed running | `msjarvis-public-docs/docs/contract/SESSION-2026-04-02.md` |
| All 5 public hostnames live and token-enforced (401) | `msjarvis-public-docs/docs/contract/SESSION-2026-04-02.md` |
| Cloudflare tunnel HEALTHY — warn cleared | `msjarvis-public-docs/docs/contract/SESSION-2026-04-02.md` |
| Caddyfile :8085 self-loop fixed → proxies to 18018 | `msjarvis-public-docs/docs/contract/SESSION-2026-04-02.md` |
| cloudflared config updated from 8443 to 8085 | `msjarvis-public-docs/docs/contract/SESSION-2026-04-02.md` |
| chat.mountainshares.us DNS CNAME added, returning 401 | `msjarvis-public-docs/docs/contract/SESSION-2026-04-02.md` |
| All 0.0.0.0 exposures eliminated across all 101 containers | `msjarvis-public-docs/docs/contract/SESSION-2026-04-02.md` |
| jarvis-hilbert-state port conflict resolved — remapped to 8092 | `msjarvis-public-docs/docs/contract/SESSION-2026-04-02.md` |
| Preflight gate logic (8 bugs) fixed | `msjarvis-public-docs/docs/contract/SESSION-2026-04-02.md` |
| Container threshold updated ≥79 → ≥96 | `msjarvis-public-docs/docs/contract/SESSION-2026-04-02.md` |
| local_resources 48/55 — intentional WARN documented and deferred | `msjarvis-public-docs/docs/contract/SESSION-2026-04-02.md` |
| OI-36-A and OI-38-A closed (token enforcement confirmed) | `msjarvis-public-docs/docs/contract/SESSION-2026-04-02.md` |
| `jarvis-memory:8056` secured (`_auth()` confirmed, durable BBB audit trail) | `msjarvis-public-docs/docs/contract/SESSION-2026-03-28.md` |
| `confidence_decay` metadata confirmed on `msjarvis:5433` | `msjarvis-public-docs/docs/contract/SESSION-2026-03-28.md` |
| ChromaDB full audit: 40 active collections / 6,675,442 total vectors | `msjarvis-public-docs/docs/contract/SESSION-2026-03-28.md` |
| `psychological_rag` restored to 968 docs | `msjarvis-public-docs/docs/contract/SESSION-2026-03-28.md` |
| `ms_jarvis_memory` collection confirmed present | `msjarvis-public-docs/docs/contract/SESSION-2026-03-28.md` |

All prior session contracts remain authoritative for their respective dates:

- `SESSION-2026-03-22.md` (commit `d966351`) — first public endpoint live, GPU benchmark, preflight 24 PASS
- `SESSION-2026-03-25.md` — consciousness pipeline sprint, ChromaDB March 25 baseline (31 collections / 6,665,093 items)
- `SESSION-2026-03-28.md` — `jarvis-memory:8056` secured, `confidence_decay` active, ChromaDB updated to 40 collections / 6,675,442 vectors, 96/96 Up
- `SESSION-2026-04-02.md` (this session) — **Chapter 39 CERTIFIED CLOSED** — 101 containers, all 5 hostnames live, all 0.0.0.0 eliminated, Cloudflare HEALTHY, routing corrected, OI-36-A/OI-38-A closed

---

*End of Chapter 39 — Operational Evaluation*
*★ Last updated: April 2, 2026 — CERTIFIED CLOSED*
*22 PASS / 0 FAIL / 1 WARN (intentional — local_resources 48/55, Phase 2 data task, deferred)*
*Author: Carrie Kidd (Mamma Kidd), Mount Hope, WV*
*Repo: H4HWV2011/msjarvis-public-docs*
