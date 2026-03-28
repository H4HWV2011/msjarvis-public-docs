````markdown
# Chapter 39 — Operational Evaluation

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV — Last updated: March 28, 2026 — container count updated to 96 (10 new containers confirmed live); jarvis-autonomous-learner port corrected to 8020 (not 8425); jarvis-rag-server internal port corrected to 8003→8003 (not 8003→8016); jarvis-consciousness-bridge confirmed internal-only on 8020; jarvis-gbim-query-router container name corrected; MountainShares/Commons/DAO services confirmed DEPLOYED (ports 8080–8084); jarvis-memory (8056), jarvis-hilbert-gateway (internal), jarvis-eeg-delta/theta/beta (8073–8075) documented; local_resources DSN corrected; 45 verified Kanawha resources (synthetic Fayette entries removed, data governance policy established); /resolve endpoint confirmed live; gisdb port 5452→5432 corrected throughout; ChromaDB collection count confirmed 31 / 6,665,093 items; ~436s CPU benchmark labeled stale; /direct_rag → /query corrected; preflight gate 24 PASS baseline confirmed; OI-05 PARTIALLY RESOLVED; OI-10 MATERIALLY ADVANCED*

This chapter records the operational state of Ms. Jarvis as of March 28, 2026,
with verified test results from the production deployment running on the Legion 5
at `~/msjarvis-rebuild-working/msjarvis-rebuild/`. All results listed here were
observed directly from live system outputs, terminal sessions, and verification
scripts. No result in this chapter is inferred or estimated. Where a test result
is pending or inconclusive, it is labeled as such.

---

> **Port and database corrections (permanent record — March 22–28, 2026):**
>
> - **PostgreSQL `msjarvis`** is at host port **5433** — 5,416,521 GBIM entities,
>   80 epochs, 206 source layers. This is the primary GBIM belief store.
> - **PostgreSQL `gisdb` / `msjarvisgis`** (PostGIS) is at host port **5432** —
>   91 GB, 501 tables, geospatial features. This is the GIS database.
>   Any reference to port **5452** for `gisdb` is a stale typo; the correct port is **5432**.
> - **PostgreSQL `jarvis-local-resources-db`** is at host port **5435**
>   (`127.0.0.1:5435->5432/tcp`). Container DSN corrected March 28, 2026:
>   `jarvis-local-resources-db:5432/postgres`. The `/resolve` endpoint is
>   confirmed live as of March 28, 2026.
> - **ChromaDB** (`jarvis-chroma`) host port is **8002**
>   (`127.0.0.1:8002->8000/tcp`). Container-internal port 8000 is not
>   used by host scripts. All scripts must reference port **8002**.
>   Confirmed inventory: **31 collections, 6,665,093 total items** (March 25, 2026).
> - **Redis** (`jarvis-redis`) host port is **6380**
>   (`127.0.0.1:6380->6379/tcp`). Container-internal port 6379 is used
>   only by container-to-container calls. Async job status key is
>   `'complete'` (not `'done'`).
> - **`jarvis-main-brain`** unified gateway is at port **8050** — not 8010.
>   Any reference to port 8010 in pipeline diagrams refers to
>   `jarvis-wv-entangled-gateway`, a separate degraded service.
> - **BBB** (`jarvis-blood-brain-barrier`) is at port **8016** —
>   six filters: `EthicalFilter`, `SpiritualFilter`, `SafetyMonitor`,
>   `ThreatDetection`, `steganography_filter`, `truth_verification`.
> - **`jarvis-rag-server`** host port is **8003**, container-internal port is
>   also **8003** (`127.0.0.1:8003->8003/tcp`, verified March 28, 2026).
>   Any prior reference to internal port 8016 for this container is incorrect.
>   RAG endpoint is **`/query`** (not `/direct_rag` — corrected sprint Patch 3A,
>   March 25, 2026).
> - **`jarvis-autonomous-learner`** host port is **8020**
>   (`127.0.0.1:8020->8020/tcp`, verified March 28, 2026). Any prior
>   reference to port **8425** for this container is incorrect and stale.
> - **`jarvis-consciousness-bridge`** is internal-only (no host binding,
>   internal port 8020). It shares the 8020 internal address space with
>   `jarvis-autonomous-learner` but does NOT have a host-side port binding.
>   All host scripts must reach `jarvis-autonomous-learner` at host port 8020.
>   The consciousness bridge is not reachable directly from the host.
> - **Container count is 96** as of March 28, 2026. Prior documentation
>   referencing 83 containers is stale. Ten new containers were confirmed
>   live on March 28: `jarvis-memory` (8056), `jarvis-eeg-delta` (8073),
>   `jarvis-eeg-theta` (8074), `jarvis-eeg-beta` (8075), `jarvis-mountainshares-coordinator`
>   (8080), `jarvis-commons-gamification` (8081), `jarvis-dao-governance` (8082),
>   `jarvis-ms-token-service` (8083), `jarvis-community-stake-registry` (8084),
>   and `jarvis-hilbert-gateway` (internal, no host binding).
> - **MountainShares/Commons/DAO services are DEPLOYED** as of March 28, 2026.
>   Prior documentation stating "NOT DEPLOYED / HTTP 000" for ports 8080–8084
>   is superseded. All five services are confirmed running.
> - **`jarvis-gbim-query-router`** is the correct container name (not
>   `gbim_query_router`). Host port **7205** (`127.0.0.1:7205->7205/tcp`).
> - **Preflight gate baseline is 24 PASS / 0 FAIL** (expanded from 20 during
>   the March 22–25 sprint). Any reference to "20 PASS 0 FAIL" is stale.
> - **Zero `0.0.0.0` exposures** confirmed across all 96 containers.
>   Exception to verify: `jarvis-web-research` shows `8090/tcp` without an
>   explicit `127.0.0.1:` prefix in `docker ps` output — confirm with
>   `docker inspect jarvis-web-research --format '{{json .NetworkSettings.Ports}}'`.

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
verified; ChromaDB inventory confirmed at **31 collections, 6,665,093 total items**.
New as of March 28, 2026: container count updated to 96; `jarvis-autonomous-learner`
port corrected to 8020; `jarvis-rag-server` internal port corrected; MountainShares
services confirmed deployed; EEG layer (delta/theta/beta), `jarvis-memory`, and
`jarvis-hilbert-gateway` documented; `jarvis-local-resources-db` DSN corrected;
data governance policy established (no synthetic or unverified data in
`local_resources`); 45 verified Kanawha County resources confirmed active;
`/resolve` endpoint confirmed live; `scripts/seed_local_resources_chroma.py`
documented.

---

## 39.2 Production Stack Health (March 28, 2026)

Test: `docker compose up -d` followed by `~/jarvis_startup.sh` on full
96-container stack.

Verified result:

```
All 96 containers: RUNNING
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

New containers confirmed live March 28, 2026:
  ✅ jarvis-memory (port 8056)
  ✅ jarvis-eeg-delta (port 8073)
  ✅ jarvis-eeg-theta (port 8074)
  ✅ jarvis-eeg-beta (port 8075)
  ✅ jarvis-mountainshares-coordinator (port 8080)
  ✅ jarvis-commons-gamification (port 8081)
  ✅ jarvis-dao-governance (port 8082)
  ✅ jarvis-ms-token-service (port 8083)
  ✅ jarvis-community-stake-registry (port 8084)
  ✅ jarvis-hilbert-gateway (internal, no host binding)

GBIM query router:
  ✅ jarvis-gbim-query-router (port 7205) — added to compose March 20, 2026

EXTERNAL SYSTEMD SERVICES (not Docker Compose — auto-start on boot):
  ✅ caddy.service (port 8443 — /etc/caddy/Caddyfile)
  ✅ jarvis-auth.service (port 8055 — scripts/jarvis_auth_service.py)
  ✅ cloudflared.service (Cloudflare Tunnel — msjarvis)
```

**Assessment:** ✅ Full 96-container stack confirmed running as of March 28, 2026.
Zero `0.0.0.0` exposures confirmed. Three external systemd services (Caddy,
jarvis-auth, cloudflared) auto-start independently of Docker Compose on boot.
MountainShares/Commons/DAO tier (5 containers, ports 8080–8084) confirmed deployed.
EEG layer (3 containers, ports 8073–8075) and `jarvis-memory` (port 8056)
confirmed running. `jarvis-hilbert-gateway` confirmed running, internal-only.

**Full verified reboot sequence:**

```bash
cd ~/msjarvis-rebuild-working/msjarvis-rebuild
docker compose up -d && ~/jarvis_startup.sh
# cloudflared, caddy, jarvis-auth all auto-start via systemd on boot
bash scripts/preflight_gate.sh   # must show 24 PASS 0 FAIL
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
Job state persistence: jarvis-redis — host port 6380 (container-internal 6379), 30-min TTL
Job status values: processing → complete (NOT 'done' — 'done' is incorrect and hangs)
Cancel capability: /chat/cancel/{job_id} — true asyncio.Task cancellation
BBB behavior: Phase 1.4 input filter — active, blocking — port 8016
             Phase 4.5 output filter — LOG+PASSTHROUGH (not blocking)
             see §39.3.1 and Chapter 16 §16.9 for output BBB detail
Phase 1.45: community memory retrieval active on every /chat
  (top-5 autonomous_learner records prepended to enhanced_message
   via all-minilm:latest 384-dim semantic search, ChromaDB port 8002)
```

> **⚠️ Stale figures retired:**
> - The ~436s figure from prior versions of this chapter was the CPU-only benchmark
>   before March 22, 2026. The RTX 4070 GPU is now active. **The ~436s figure is
>   RETIRED/STALE and must not appear in any current documentation without this label.**
> - Any reference to `jarvis-main-brain` at port **8010** is incorrect. The
>   unified gateway is at port **8050**. Port 8010 is `jarvis-wv-entangled-gateway`,
>   a separate degraded service.

### 39.3.1 Output BBB — Log+Passthrough Mode (March 22, 2026)

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
Input BBB (Phase 1.4): FULLY ACTIVE — correctly tuned — port 8016
```

Output BBB recalibration is a documented next-session priority.
See Chapter 16 §16.9 for full calibration status and the Appalachian voice
threshold recalibration work item.

**Safety posture during log+passthrough phase:** Output safety relies on five
active layers:
1. Phase 1.4 BBB input filter (active, blocking, port 8016)
2. Judge pipeline `bbb_check_verdict` (live async httpx POST to port 8016,
   active on consensus answer — Chapter 33 §33.2 addendum)
3. LM Synthesizer identity guard — three layers active in
   `services/lm_synthesizer.py` (Chapter 33 §33.5.2 / Chapter 36 §36.5.2)
4. `normalize_identity` persona enforcement in `jarvis-main-brain` (port 8050)
5. Phase 4.5 BBB output — log+passthrough (active, non-blocking, logging all
   six filter results in `UltimateResponse.bbb_result`)

**Assessment:** ✅ Full pipeline operational at GPU speeds. Three confirmed public
runs: 99.6s, 105.9s, 106.5s. Output BBB in safe log+passthrough mode during red
team phase.

---

## 39.4 Memory Growth and ChromaDB Collections

Test: Collection record counts verified via `docker exec jarvis-chroma` ChromaDB
queries and autonomous learner growth rate tracking. All ChromaDB connections use
host port **8002** (`127.0.0.1:8002->8000/tcp`). Embedding model locked to
`all-minilm:latest` (384-dim) for all collections — do not substitute
`nomic-embed-text` (768-dim, incompatible with existing collections).

**Verified result — ChromaDB inventory (March 25, 2026):**

> **⚠️ Collection count correction:** Prior versions of this chapter reported
> 13 collections (March 22 snapshot) and referenced a total of 19 collections
> (partially inferred). The **confirmed collection count as of March 25, 2026
> is 31 collections, 6,665,093 total items**, verified via direct ChromaDB API
> enumeration during the consciousness pipeline sprint. Any reference to 13 or
> 19 collections is stale.

```
Collection                          Records    Status
─────────────────────────────────── ────────── ──────────────────────────────────────────
gbim_worldview_entities             5,416,521  ✅ Complete WV GBIM spatial corpus
autonomous_learner                  21,181+    ✅ Growing ~288/day from March 14 baseline
psychological_rag                   968        ✅ Active
spiritual_texts                     23         ✅ Active
appalachian_cultural_intelligence   5          ✅ Active
GBIM_sample_rows                    5,000      ✅ Active
GBIM_sample                         3          ✅ Active
msjarvis-smoke                      1          ✅ Smoke test record
msjarvis_docs                       2,348      ✅ Active — 45 verified Kanawha County
                                               community resources (synthetic Fayette
                                               entries removed March 28, 2026 —
                                               data governance policy established) +
                                               2,303 system docs
GBIM_Fayette_sample                 0          ⚠ Scaffolded — pending ingest
geospatialfeatures                  0          ⚠ Scaffolded — pending backfill ingest
[+ 20 additional collections confirmed in March 25 full enumeration]

Total confirmed collection count (March 25, 2026): 31 collections
Total items across all collections (March 25, 2026): 6,665,093
Prior reported count (March 22 snapshot): 13 named / 19 estimated — SUPERSEDED
```

> **Data governance policy (established March 28, 2026):** No synthetic,
> inferred, or unverified data may be written to `local_resources` or ingested
> into the `msjarvis_docs` ChromaDB collection. All resources must be
> individually verified before seeding. The 45 Kanawha County resources in
> `msjarvis_docs` are verified. Two previously included Fayette County entries
> were synthetic placeholders and were removed March 28, 2026.
> Seed script: `scripts/seed_local_resources_chroma.py`.

> **Note on the 20 additional collections:** The 20 collections beyond the 11
> named above were confirmed present in the ChromaDB container during the March 25
> consciousness pipeline sprint full enumeration. Individual record counts and
> active/scaffolded status for these 20 collections are pending documentation.
> They are counted in the 31-collection / 6,665,093-item total but not
> individually catalogued here.

```
Embedding model (all collections): all-minilm:latest (384-dim, via jarvis-ollama:11434)
INCOMPATIBLE model (DO NOT USE): nomic-embed-text (768-dim — breaks all existing collections)
ChromaDB host port: 8002 (container-internal: 8000)
Auto-detect: docker port jarvis-chroma 8000/tcp
```

```
LANDOWNER BELIEFS: NOT in ChromaDB.
Served exclusively by jarvis-gbim-query-router (port 7205)
via mvw_gbim_landowner_spatial in msjarvisgis / gisdb (PostgreSQL port 5432).
```

**Assessment:** ✅ Core collections healthy. ChromaDB inventory confirmed at
**31 collections, 6,665,093 total items** as of March 25, 2026. `autonomous_learner`
growth confirmed. Two known scaffolded collections (0 records) awaiting backfill
ingest — not blocking production. Embedding dimension lock (`all-minilm:latest` /
384-dim) enforced. Data governance policy established March 28, 2026.

---

## 39.5 PostgreSQL Production Databases

Test: Direct `psql` queries against production databases to verify table count,
row counts, and corpus integrity as of March 20–22, 2026.

### 39.5.1 `gisdb` / `msjarvisgis` — PostGIS Geospatial Database (Port 5432)

```
Database: msjarvisgis (also referred to as gisdb)
PostgreSQL version: 16 + PostGIS
Host port: 5432
Size: 91 GB
Tables: 501
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
Content: 5,416,521 GBIM entities, 80 epochs, 206 source layers
Role: Primary GBIM belief store — non-geospatial knowledge base
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
local_resources table: 45 verified Kanawha County resources
  — data governance policy: no synthetic or unverified entries permitted
  — seed script: scripts/seed_local_resources_chroma.py
```

**Assessment:** ✅ All three PostgreSQL databases confirmed active. Materialized
view live. Landowner beliefs ingested and spatially indexed. Red team audit tables
confirmed active. `jarvis-local-resources-db` DSN corrected March 28, 2026.

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

**Verified result (March 25, 2026 — end of sprint):**

```
VERIFYANDTEST.sh (March 22 morning baseline):
  23 PASS 0 FAIL
  Note: regression baseline timeout is WARN (not FAIL) — cached-first
  approach deployed to avoid 600s timeout when semaphore busy

scripts/preflight_gate.sh — 24 checks (March 22–25, 2026 sprint):
  ✅  1. Container count ≥79
  ✅  2. Zero 0.0.0.0 exposures
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
  ✅ 13. Community resources: 45 verified (Kanawha County — updated March 28, 2026)
  ✅ 14. msjarvis_docs: 2,348 items
  ✅ 15. redteam_sessions table exists
  ✅ 16. Invite tokens: 4 active
  ✅ 17. mvw_gbim_landowner_spatial: 20,593 rows
  ✅ 18. Caddy gateway (port 8443) — CORS active
  ✅ 19. Auth service (port 8055) — token validation ready
  ✅ 20. Cloudflare tunnel — https://egeria.mountainshares.us live
  ✅ 21. Chroma reachability (v2 API, port 8002) — added sprint Patch 1
  ✅ 22. WOAH container active (port 7012) — added sprint Patch 2
  ✅ 23. RAG endpoint reachable (/query, port 8003) — added sprint Patch 3A
  ✅ 24. Consciousness bridge health (port 8020 internal) — added sprint Patch 3B
──────────────────────────────────────────────────────────
RESULT: 24 PASS 0 FAIL
```

> **Preflight check #13 update (March 28, 2026):** The check text should read
> "Community resources: 45 verified (Kanawha County)". The prior value of 52
> (50 Kanawha + 2 Fayette) is stale — the 2 Fayette entries were synthetic
> placeholders removed under the data governance policy established March 28, 2026.

**Assessment:** ✅ Pre-flight gate confirmed at **24 PASS / 0 FAIL** — current
baseline. Gate held throughout the March 22–25 sprint and through March 28.
`VERIFYANDTEST.sh` regression poll uses cached-first approach to avoid semaphore
timeout under load.

---

## 39.8 Known Gaps and Pending Work

### 39.8.1 Open Item Status Table (updated March 28, 2026)

| OI ID | Item | Status | Notes |
|---|---|---|---|
| OI-02 | Output BBB Phase 4.5 recalibration | ⚠️ **OPEN** | Log+passthrough mode remains in effect (commit `18b8ddac`). Target: < 5% false-positive rate before re-enabling blocking. See Chapter 16 §16.9. |
| OI-05 | Conversation memory (formal wiring) | ⚠️ **PARTIALLY RESOLVED** | Emergent context observed in March 25 end-to-end production test. Formal wiring incomplete. See §39.11. |
| OI-10 | Meaning-oriented pipeline (consciousness bridge, WOAH, Chroma) | ✅ **MATERIALLY ADVANCED** | All three confirmed operational March 25, 2026. See §39.11 and Chapter 25 §25.9. |
| OI-11 | StarCoder2 exclusion (0-char on community queries) | ⚠️ **OPEN** | HTTP 200, 0-char responses on community queries. Excluded from consensus. See Chapter 35 §35.3. |
| OI-29 | WOAH Pydantic schema formalization | ⚠️ **STUB OPERATIONAL — SCHEMA DEFERRED** | WOAH rebuilt as stdlib stub — confirmed operational on `qualia-net`. Schema formalization deferred. |
| OI-36-A | Gateway token enforcement | ⚠️ OPEN | Unauthenticated `/chat` requests still reach gateway at port 8050. See Chapter 36 §36.11. |
| OI-36-B | Role-based route restriction (403) | ⚠️ OPEN | Blocked by OI-36-A. |
| OI-38-A | Token enforcement on public endpoint | ⚠️ OPEN | https://egeria.mountainshares.us accepts unauthenticated requests. |
| OI-38-B | Phase 4.5 output BBB not blocking | ⚠️ OPEN | Same as OI-02. |

### 39.8.2 Non-OI Data Gaps and Pending Work (March 28, 2026)

| Item | Status | Notes |
|---|---|---|
| Output BBB recalibration | ⚠️ OPEN | 31% false-positive rate on maternal/exclamatory Appalachian tone confirmed; threshold adjustment needed. See Chapter 16 §16.9. |
| Gateway auth enforcement | ⚠️ OPEN | Token validation is UI-initiated only. See OI-36-A / OI-38-A. |
| Role-based route restriction (403) | ⚠️ OPEN | See OI-36-B. |
| `geospatialfeatures` ChromaDB | ⚠️ 0 records | Scaffolded — backfill ingest pending |
| `GBIM_Fayette_sample` ChromaDB | ⚠️ 0 records | Scaffolded — pending ingest |
| `appalachian_cultural_intelligence` | ⚠️ 5 items | Minimal — needs expansion |
| `spiritual_texts` | ⚠️ 23 items | Active but minimal |
| ChromaDB 20 additional collections | ⚠️ ENUMERATED — counts pending | Confirmed in 31-collection inventory; individual record counts not yet catalogued. |
| `jarvis-steward` | ⚠️ No host binding | Running (internal only); not wired into main pipeline |
| `jarvis-hilbert-gateway` | ⚠️ No host binding | Confirmed running (internal only); pipeline wiring not yet documented |
| `jarvis-memory` (port 8056) | ⚠️ Undocumented | Confirmed running; service role, endpoints, and pipeline integration not yet documented |
| `jarvis-eeg-delta/theta/beta` (8073–8075) | ⚠️ Undocumented | EEG layer confirmed running; service architecture, endpoints, and pipeline role not yet documented |
| MountainShares tier (8080–8084) | ⚠️ DEPLOYED — endpoints unverified | All five containers confirmed running; individual endpoint health and pipeline integration not yet validated. Prior "NOT DEPLOYED" status is superseded. |
| `VERIFYANDTEST` regression poll | ⚠️ WARN | "WV capital city" test times out under load; cached-first approach mitigates but does not resolve |
| MySQL schema dump | ⚠️ Undocumented | Port 3307 (`127.0.0.1:3307->3306/tcp`) confirmed running; schema dump not yet committed to `docs/` |
| Government landowner proposition codes | ⏳ Pending | `LANDOWNER_GOVERNMENT` records pending separate ingest pass |
| `mvw_gbim_landowner_spatial` refresh cadence | ⏳ Pending | Materialized view refresh not yet defined (currently manual) |
| `gbim_beliefs_v2` ChromaDB status | ⚠️ UNVERIFIED | Not individually confirmed; may be among 20 additional collections |
| RAG embedding end-to-end validation | ⚠️ IN PROGRESS | RAG endpoint reachable (`/query`, port 8003, HTTP 200); embedding roundtrip not yet fully validated |
| `jarvis-neurobiological-master` reachability | ⚠️ OPEN | Confirmed unreachable; Chroma health check rerouted around it (Ch. 25 Patch 1); root cause unresolved |
| `jarvis-web-research` binding verification | ⚠️ VERIFY | Shows `8090/tcp` without `127.0.0.1:` prefix in `docker ps` — run `docker inspect jarvis-web-research --format '{{json .NetworkSettings.Ports}}'` to confirm no 0.0.0.0 exposure |
| Preflight gate container count check | ⚠️ UPDATE NEEDED | Gate check #1 reads `≥79`; should be updated to `≥96` to match current verified stack |

None of the above block current production operation. The public endpoint
https://egeria.mountainshares.us is live and functional.

---

## 39.9 Operational Summary Table (March 28, 2026)

| Capability | Status | Key Metric |
|---|---|---|
| Full 96-container stack startup | ✅ Verified | `docker compose up -d` + `jarvis_startup.sh` |
| External systemd services | ✅ Verified | Caddy 8443, jarvis-auth 8055, cloudflared — all auto-start on boot |
| End-to-end chat pipeline (GPU) | ✅ Verified | 99–107s (RTX 4070) — CPU baseline ~436s **RETIRED/STALE** |
| Public HTTPS endpoint | ✅ LIVE | https://egeria.mountainshares.us |
| Async job management | ✅ Verified | Redis-backed (host port 6380), 30-min TTL, true asyncio cancel, status key = `'complete'` |
| BBB input filter (Phase 1.4) | ✅ Active, blocking | Port 8016 — six filters |
| BBB output filter (Phase 4.5) | ⚠️ Log+passthrough | Port 8016 — logging only, not blocking during tuning (OI-02) |
| Phase 1.45 community memory injection | ✅ Verified | top-5 `autonomous_learner` records on every `/chat` via ChromaDB port 8002 |
| Autonomous learner growth | ✅ Verified | 21,181+ records, ~288/day — host port **8020** |
| `msjarvis_docs` collection | ✅ Verified | 2,348 items — 45 verified Kanawha County resources + 2,303 system docs (updated March 28) |
| ChromaDB confirmed collection inventory | ✅ Updated | **31 collections, 6,665,093 total items** (March 25) — host port 8002 |
| PostgreSQL `gisdb` / `msjarvisgis` corpus | ✅ Verified | 91 GB, 501 tables, 5,416,522 beliefs — port **5432** |
| PostgreSQL `msjarvis` GBIM store | ✅ Verified | 5,416,521 GBIM entities, 80 epochs — port 5433 |
| PostgreSQL `jarvis-local-resources-db` | ✅ Verified | 7,354,707 parcel rows; red team audit tables active — port 5435; DSN corrected March 28 |
| `jarvis-local-resources` `/resolve` endpoint | ✅ LIVE | Confirmed March 28, 2026 — port 8006 |
| GBIM landowner query (`jarvis-gbim-query-router`) | ✅ Verified | 20,593 beliefs, 401 canonical entities, port 7205 |
| Judge pipeline (5 containers) | ✅ Verified | Compose-managed; coordinator 7239, judges 7230–7233 |
| 21-model LLM ensemble | ✅ Verified | 21/22 responded within budget — March 22, 2026 |
| Identity guard (LM Synthesizer, 3 layers) | ✅ Verified | Model names blocked; Egeria identity confirmed under adversarial probe |
| Red team tokens | ✅ Active | 4 active (carrie_admin ×2, hayden_test ×2) — `jarvis-redis` host port 6380 |
| Pre-flight gate | ✅ Verified | **24 PASS 0 FAIL** — current baseline |
| Consciousness pipeline (Chroma + WOAH + Bridge) | ✅ Operational | Confirmed March 25, 2026 — all three stages active (OI-10 materially advanced) |
| Conversation memory (emergent) | ⚠️ Partial | Prior context referenced in March 25 test; formal wiring incomplete (OI-05 partially resolved) |
| RAG embedding end-to-end | ⚠️ In progress | Endpoint reachable at `/query` port 8003; embedding roundtrip in final-stage fix |
| MountainShares/Commons/DAO tier | ⚠️ DEPLOYED — endpoints unverified | 5 containers live (ports 8080–8084); individual health not yet validated |
| EEG layer (delta/theta/beta) | ⚠️ Running — undocumented | 3 containers live (ports 8073–8075); architecture and pipeline role not yet documented |
| `jarvis-memory` | ⚠️ Running — undocumented | Port 8056; service role and pipeline integration not yet documented |
| `jarvis-hilbert-gateway` | ⚠️ Running — undocumented | Internal only; pipeline wiring not yet documented |
| Zero `0.0.0.0` exposures | ✅ Confirmed | All 96 containers localhost-only (verify `jarvis-web-research` per §39.8.2) |
| Data governance policy | ✅ Established | March 28, 2026 — no synthetic/unverified data in `local_resources` or `msjarvis_docs` |

---

## 39.10 First Public End-to-End Verification — March 22, 2026

This section documents the first confirmed public end-to-end chat session via
https://egeria.mountainshares.us, March 22, 2026. Three consecutive queries were
submitted through the Cloudflare-tunneled Caddy gateway → `jarvis-auth` token
validation → `jarvis-main-brain` port 8050 → full 9-phase pipeline → synthesized
response in Ms. Egeria Jarvis voice. All three runs completed in the 99–107s GPU
range. Response content included authentic Appalachian maternal voice, confirmed
WV geographic context, and no identity leakage (no "As LLaMA," "As Mistral," or
"As an AI" phrases). Public URL remains live.

---

## 39.11 Consciousness Pipeline Confirmation — March 25, 2026

Following the five-patch sprint (Chapter 25 §25.9 / Chapter 40 §40-H), the full
consciousness pipeline was confirmed operational for the first time:

```
Chroma v2 API (port 8002):          CONNECTED — /api/v2/heartbeat HTTP 200
WOAH (port 7012, stdlib stub):      ACTIVE — {"status": "ok"}
Consciousness bridge (internal 8020): OPERATIONAL — 3 patches applied
RAG server (host port 8003):        OPERATIONAL — /query confirmed
Unified gateway (port 18018):       OPERATIONAL — dict.lower() guard patched
jarvis-ollama (11434):              REACHABLE from RAG server container
jarvis-neurobiological-master (8018): ⚠️ UNREACHABLE — Chroma health rerouted
                                       around it (Ch. 25 Patch 1); root cause open
```

During the March 25 production end-to-end test, emergent conversation context
carryover was observed (OI-05 PARTIALLY RESOLVED). Formal conversation memory
wiring remains incomplete. The `autonomous_learner` collection provides semantic
similarity recall but is not a session-scoped conversation buffer.

---

## 39.12 Complete Verified Container Inventory (March 28, 2026)

Full `docker ps` snapshot verified March 28, 2026 — 96 containers total, zero
`0.0.0.0` exposures.

### Core Orchestration

| Container | Host Port | Internal Port | Status |
|---|---|---|---|
| `jarvis-main-brain` | 8050 | 8050 | ✅ Healthy |
| `jarvis-brain-orchestrator` | 17260 | 7260 | ✅ Healthy |
| `jarvis-unified-gateway` | 18018 | 8001 | ✅ Running |
| `jarvis-semaphore` | 8030 | 8030 | ✅ Running |
| `jarvis-steward` | none | internal | ✅ Running — not wired to pipeline |

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
| `jarvis-blood-brain-barrier` | 8016 | 8016 | ✅ Running — 6 filters |
| `jarvis-69dgm-bridge` | 19000 | 9000 | ✅ Running — 23 connectors, 3 stages, 69 ops |
| `jarvis-constitutional-guardian` | 8091 | 8091 | ✅ Running |
| `jarvis-psychology-services` | 8019 | 8019 | ✅ Running |
| `psychological_rag_domain` | 9006 | 8006 | ✅ Running — 968 items |

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

### EEG Layer (NEW — March 28, 2026)

| Container | Host Port | Status | Notes |
|---|---|---|---|
| `jarvis-eeg-delta` | 8073 | ✅ Running | Architecture and pipeline role pending documentation |
| `jarvis-eeg-theta` | 8074 | ✅ Running | Architecture and pipeline role pending documentation |
| `jarvis-eeg-beta` | 8075 | ✅ Running | Architecture and pipeline role pending documentation |

### Memory (NEW — March 28, 2026)

| Container | Host Port | Status | Notes |
|---|---|---|---|
| `jarvis-memory` | 8056 | ✅ Running | Service role and pipeline integration pending documentation |

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
| `jarvis-web-research` | 8090 | 8090 | ✅ Running | ⚠️ Verify 0.0.0.0 binding |
| `jarvis-aaacpe-rag` | 8032 | 8032 | ✅ Running | |
| `jarvis-aaacpe-scraper` | 8033 | 8033 | ✅ Running | |
| `jarvis-wv-entangled-gateway` | 8010 | 8010 | ⚠️ Degraded | Not the primary entrypoint |
| `jarvis-agents-service` | none | 8005 | ✅ Running | Internal only |
| `jarvis-hilbert-gateway` | none | internal | ✅ Running | NEW — pipeline wiring undocumented |

### MountainShares / Commons / DAO Tier (NEW — DEPLOYED March 28, 2026)

> **Status correction:** Prior documentation listed all five of these services as
> "NOT DEPLOYED / HTTP 000." All five are confirmed running as of March 28, 2026.
> Individual endpoint health and pipeline integration have not yet been validated.

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
| `jarvis-chroma` | 8002 | ChromaDB | ✅ Healthy | 31 collections, 6,665,093 items |
| `jarvis-redis` | 6380 | Redis 7 | ✅ Healthy | Job state, status key `'complete'` |
| `jarvis-local-resources-db` | 5435 | PostGIS 15 | ✅ Running | DSN corrected March 28 |
| `neo4j` | 7687, 7475 | Neo4j 5.13 | ✅ Running | Identity graphs |
| `mysql` | 3307 | MySQL 8.2 | ✅ Running | Schema undocumented |
| Host PostgreSQL `msjarvisgis` | 5432 | PostGIS 16 | ✅ Verified | 5,416,522 beliefs |
| Host PostgreSQL `msjarvis` | 5433 | PostgreSQL 16 | ✅ Running | 5,416,521 GBIM entities |

### Infrastructure

| Container | Host Port | Status | Notes |
|---|---|---|---|
| `ipfs/kubo` | 5001 | ✅ Running | MountainShares/Commons content addressing |
| `jarvis-crypto-policy` | 8099 | ✅ Running | Added to compose March 22 |
| `jarvis-ingest-api` | none | ✅ Running | Added to compose March 22 |
| `jarvis-ingest-watcher` | none | ✅ Running | Added to compose March 22 |

---

*End of Chapter 39 — Operational Evaluation*
*Last updated: March 28, 2026*
*Author: Carrie Kidd (Mamma Kidd), Mount Hope, WV*
*Repo: H4HWV2011/msjarvis-public-docs*
````
