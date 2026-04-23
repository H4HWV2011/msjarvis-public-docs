# 26. Temporal, Toroidal, and Semaphore Structure of Conscious Processing

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*

*Last updated: ★ 2026-04-23*

*★ April 23, 2026: Container count updated to 100 (supersedes 105 from April 10 baseline); ChromaDB updated to 48 active collections, ~6,740,611 total vectors (supersedes 49 / 6,722,589+); ChromaDB API updated to /api/v2/ throughout — /api/v1/ is permanently removed in server 1.0.0; two-container PostgreSQL split — production msallis-db host 5433 (16 GB, 294 tables, 11 schemas) + forensic postgis-forensic host 5452 (17 GB, 314 tables) — supersedes msallisgis:5432 and msallis:5433 references throughout; autonomous_learner updated to ~23,200+ records (~288/day from 21,181 April 13 baseline); conversation_history wiped and reseeded clean April 16, 2026; OI-36-A CLOSED — Caddy forward_auth token enforcement active at perimeter before main-brain port 8050; local_resources updated to 207 items / all 55 WV counties (supersedes earlier baselines); AAACPE ingest path updated — dedicated stack (allis-aaacpe-scraper:8048→8033 + allis-aaacpe-rag:8047→8032) supersedes legacy allis-ingest-api + allis-ingest-watcher for Appalachian cultural data; neuro_master total_processes updated to 5 active downstream services (verify-current for 131 process count).*

*★★★ 2026-04-10 — Full closure pass: 105 containers Up (updated from 96); 49 ChromaDB collections / 6,722,589+ vectors; allis-neurobiological-master:8018 CLOSED (NBB returning 200, fully_integrated); identity_layers + consciousness_layers CLOSED (both fields live); pia_severity CLOSED (WOAH fallback wired); hilbert guard CLOSED (str guard added); consciousness-bridge corrected (allis-hilbert-state:8081, POST /embed + GET /all_states, managed in compose); redteam gate remediated (redis module, ALLIS_API_KEY, token seeded); AU-02 v2, ML-DSA-65, rag_grounded_v2, OI-31 EEG layer added; I-Container language updated.*

*★★ April 1, 2026: LEARN-01/02/03 resolved; autonomous learner live telemetry confirmed (68 Chroma items, 15 cycles, 11 entanglement nodes); 96/96 Up post-LEARN-03 recovery.*

*★ March 28, 2026: 96/96 containers Up; msallis:5433 restored (5,416,521 GBIM entities with confidence_decay); msallisgis:5432 confirmed (91 GB PostGIS, 501 tables, 993 ZCTA centroids); ChromaDB full audit (40 collections, 6,675,442 vectors); allis-memory:8056 secured; spiritual_rag deduplicated (−19,338 vectors); psychological_rag restored (968 docs); msallis_docs expanded (4,192 items, AAPCAppE); consciousness pipeline confirmed Up.*

---

> **★ April 23, 2026 — Open Items Status Update**
>
> | Item | Status at April 10 | Status April 23 |
> |---|---|---|
> | Container count | 105 Up | ★ **100 Up** (supersedes 105) |
> | ChromaDB collections | 49 / 6,722,589+ vectors | ★ **48 / ~6,740,611 vectors** |
> | ChromaDB API | /api/v1/ | ★ **/api/v2/** — /api/v1/ permanently removed |
> | PostgreSQL ground truth | msallisgis:5432 + msallis:5433 | ★ **msallis-db host 5433** (16 GB, 294 tables, 11 schemas) + **postgis-forensic host 5452** (17 GB, 314 tables) |
> | OI-36-A (auth) | Auth container healthy at seal | ★ **CLOSED April 23** — Caddy `forward_auth` perimeter enforcement active before main-brain port 8050 |
> | AAACPE ingest | allis-ingest-api + allis-ingest-watcher | ★ **Dedicated stack** — allis-aaacpe-scraper:8048→8033 + allis-aaacpe-rag:8047→8032 |
> | autonomous_learner | 68 items (April 1) | ★ **~23,200+ records** (~288/day from 21,181 April 13 baseline) |
> | local_resources | Earlier baseline | ★ **207 items, all 55 WV counties** |
> | conversation_history | Active | ★ **Wiped and reseeded clean April 16, 2026** — post-wipe accumulation only |
> | All April 10 closure items | ✅ CLOSED | Unchanged ✅ |

---

> **★★★ April 10, 2026 — Open Items Closure Register**
>
> | Item | Status at March 28 | Status April 10 |
> |---|---|---|
> | `allis-neurobiological-master:8018` unreachable — soft semaphore bypassed | ⚠️ Open | ✅ **CLOSED** — NBB returning 200, `fully_integrated` |
> | `identity_layers` / `consciousness_layers` not populated in response | ⚠️ Open | ✅ **CLOSED** — both fields live |
> | `pia_severity` stuck at `unknown` | ⚠️ Open | ✅ **CLOSED** — WOAH fallback wired; `pia: low` correct and expected |
> | Consciousness error `'str' object has no attribute 'get'` | ⚠️ Open | ✅ **CLOSED** — hilbert string guard added |
> | `allis-consciousness-bridge` URL wrong (`allis-hilbert-gateway:8010`) | ⚠️ Open | ✅ **CLOSED** — corrected to `allis-hilbert-state:8081` |
> | Bridge endpoint `/wv_summary` (404) | ⚠️ Open | ✅ **CLOSED** — corrected to `POST /embed` + `GET /all_states` |
> | Bridge payload `message`/`user_id` | ⚠️ Open | ✅ **CLOSED** — corrected to `text`/`entity_id` |
> | Bridge outside compose — `qualia-net` drop on restart | ⚠️ Open | ✅ **CLOSED** — added as `allis-consciousness-bridge` service in compose |
> | Redteam gate (Gate 34): redis module missing, DNS failure, token unseeded, `ALLIS_API_KEY` unset | ⚠️ Open | ✅ **CLOSED** — redis installed in image, fallback wired, token seeded, key set |
> | Gate 32: preflight checking wrong port 7230 | ⚠️ Open | ✅ **CLOSED** — corrected to 8041 (judge-truth port) |
> | Gate 29: no host port binding on `neurobiological-master` | ⚠️ Open | ✅ **CLOSED** — replaced curl with `docker exec python3 urllib` |
> | Gate 28: broken 8049→8099 port mapping | ⚠️ Open | ✅ **CLOSED** — replaced curl with `docker exec python3 urllib` |
> | `confidence_decay` table missing | ⚠️ Open | ✅ **CLOSED** — resolved by Phase 5 work |
> | `docker-compose-core.yml` duplicate environment key | ⚠️ Open | ✅ **CLOSED** — merged into single block |
> | Container count stale (96) | Stale | ✅ **Updated** — 105 containers Up at April 10 (★ 100 as of April 23) |
> | ChromaDB stale (40 collections / 6,675,442 vectors) | Stale | ✅ **Updated** — ★ 48 collections / ~6,740,611 vectors as of April 23 |
> | `rag_grounded_v2` missing | Missing | ✅ **Added** — healthy at 127.0.0.1:7241, `dgm_available: true` |
> | OI-31 EEG layer missing | Missing | ✅ **Added** — §26.1 and §26.3 |
> | AU-02 v2 / ML-DSA-65 missing | Missing | ✅ **Added** — §26.3 |
> | I-Container language stale | Stale | ✅ **Updated** throughout |

---

This chapter describes three complementary structural views of the conscious processing pipeline implemented in Ms. Allis: temporal (how processing unfolds across time scales), toroidal (how information recirculates through spatial and semantic loops), and semaphore (how concurrency, ethical gates, and configuration flags regulate what runs and when). Together these views connect abstract design principles to concrete services — the unified consciousness pipeline (confirmed OPERATIONAL, fully_integrated April 10, 2026), ChromaDB-backed semantic memory (★ **48 collections, ~6,740,611 vectors**), the production PostgreSQL `msallis-db` (★ host port **5433**, **16 GB, 294 tables, 11 schemas**) and forensic `postgis-forensic` (★ host port **5452**, **17 GB, 314 tables**), autonomous learning (★ **~23,200+ records**, growing ~288/day), and `rag_grounded_v2` (healthy at 127.0.0.1:7241, `dgm_available: true`). The use of temporal scales, recurrent loops, resource gates, and toroidal circulation echoes wider ideas in dynamical and modular AI systems as well as classical spatial-economic models in which peripheral actors repeatedly move through central places — a pattern directly relevant to Appalachian communities navigating state and federal systems from a rural periphery.

---

## 26.1 Temporal Structure

The temporal view describes how conscious processing unfolds on different time scales and how those scales map to concrete services and the live system state.

### Short-term (per-request flows)

Short-term activity is anchored by live consciousness flows implemented by the `Ms. Allis ULTIMATE` main-brain service, which runs a FastAPI app and exposes `/chat`, `/chatsync`, `/chat/async`, `/health`, and `/status` on port **8050** (★ now behind Caddy `forward_auth` perimeter enforcement — OI-36-A CLOSED). Each incoming request first passes through Caddy bearer token validation before reaching main-brain, where it is wrapped into an `UltimateRequest` and passed through a fixed sequence of services — the 22-registered / 21-active `llm20production` fabric, GIS-aware reasoning via RAG over `geodb_*` collections (sourced from the production `msallis-db:5433` ★), web research helpers, the Blood–Brain Barrier (port **8016** ★; audit → `allis-memory:8056`), prefrontal NBB stages, and the I-Container identity layer — before returning a response.

★★★ **April 10, 2026 — confirmed live short-term response fields:**

```text
identity:   ['fully_integrated']     ✅
conscious:  ['blood_brain_barrier', 'i_containers', 'qualia_engine',
             'consciousness_bridge']  ✅
pia:        low                      ✅  (honest — Chroma/RAG/Hilbert offline)
cs error:   none                     ✅
response:   Well howdy there Carrie! ...  ✅
```

> **`pia: low` is correct and expected.** WOAH is accurately reporting weak identity because memory infrastructure (Chroma, RAG, Hilbert) is unreachable from that probe context. That is not a bug — that is the system being honest about its own state. `pia_severity` previously stuck at `unknown` is now resolved via WOAH fallback wiring.

Each completed `/chat` call also triggers a background write into the shared Chroma collection `ms_allis_memory`, preserving a `USER:`/`EGERIA:` transcript and associated metadata for later recall. ★ `conversation_history` was wiped and reseeded clean April 16, 2026 — any count on that collection reflects post-wipe accumulation only.

**★★★ OI-31 EEG Layer — short-term heartbeat signals.** The short-term temporal layer now includes EEG-analogous rhythm signals from the autonomous learner (beta rhythm, 5-minute cadence; confirmed operational). ★ `autonomous_learner` has grown to **~23,200+ records** (~288/day from 21,181 April 13 baseline). Delta (30s) and theta (60s) rhythms remain unrestored from the October 2025 rebuild (open gap — see Ch 28 §28.4). At the per-request scale, the EEG layer contributes the learner's most recent session telemetry to the context window when `allis-autonomous-learner` is reachable on `qualia-net`.

### Medium-term (hours to days)

Medium-term processes accumulate and revisit information across multiple short-term interactions. Verification tools such as `VERIFYANDTEST.sh` periodically exercise full flows, check container-like paths and key services, and report operational status. Utilities `extract_all_chromadb_to_gis.py` and `sync_geodb_to_chromadb.py` traverse ChromaDB (★ **48 collections, ~6,740,611 vectors**) via the correct host port **8002** (container port 8000) using `/api/v2/` API (★ `/api/v1/` permanently removed), and the production `msallis-db:5433` ★ (16 GB, 294 tables, 11 schemas), exporting or ingesting batches of records to keep semantic and spatial representations in sync.

★ The dedicated AAACPE stack (`allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`) represents a continuous medium-term ingest process — external Appalachian cultural sources flowing into `msallis_docs` on an ongoing basis, independent of user interactions (supersedes legacy `allis-ingest-api` + `allis-ingest-watcher` for AAACPE data). The `appalachian_english_corpus` cron scraper adds a second always-on medium-term ingest: 210 documents across 38 Appalachian sources, refreshing every 6 hours via cron (`0 */6 * * *`).

I-Container ingestion and promotion flows are defined and exercised in code but are not yet running as a fully automated, scheduled loop. Medium-term I-Container dynamics should therefore be understood as a designed and partially implemented pattern — conversation memory formal wiring also remains partial (OI-05; emergent context passing confirmed March 25, 2026 — see Ch 22 §22.9).

### Long-term (days to weeks and beyond)

Long-term continuity is supplied by persistent collections in ChromaDB (★ **48 active collections, ~6,740,611 total vectors**) and spatial databases. Core collections — `allis_consciousness`, `autonomous_learner` (★ **~23,200+ records**, growing ~288/day), `ms_allis_memory`, `spiritual_wisdom` (deduplicated −19,338 vectors), `psychological_rag` (restored 968 docs), `msallis_docs` (verify-current ★), `appalachian_english_corpus` (210 docs, live) — store synthetic reflections, autonomous learning outputs, long-term identity fragments, and community-specific knowledge. ★ `local_resources` is now 207 items / all 55 WV counties.

★★★ **ML-DSA-65 (Module Lattice Digital Signature Algorithm)** provides cryptographic long-term integrity for belief provenance: belief entries promoted from ChromaDB to the production `msallis-db:5433` ★ can carry ML-DSA-65 signatures that anchor their provenance across system restarts, compose updates, and future migrations. This is particularly relevant at the long-term temporal layer, where belief entries may outlive the operational session in which they were created.

The `confidence_decay` metadata on production `msallis-db:5433` ★ GBIM entities introduces a graded temporal signal at the long-term layer: older or less-corroborated beliefs decay in evidentiary weight, biasing long-term consolidation toward better-supported knowledge. In this temporal framing, conscious processing is not a single event but a superposition of fast per-request pipelines (★ **100 containers Up**), slower background jobs (AAACPE dedicated stack, appalachian_english_corpus cron, sync scripts active), and very slow consolidation in long-lived memory (★ 48 collections, ~6,740,611 vectors; production `msallis-db:5433` ★ 16 GB, 294 tables, 11 schemas).

---

## 26.2 Toroidal Structure

The toroidal view treats Ms. Allis's state as moving through cycles and loops rather than progressing linearly, focusing on repeated passes over similar themes with updated context. It connects these loops to the older intuition that healthy settlements depend on circulation between periphery and center — Von Thünen's farmland rings around a market town, Christaller's rural–town–city hierarchies — and reframes that circulation as the movement of beliefs, benefits, risks, and narratives through a computational torus anchored in West Virginia geography.

### Cyclic passes over services and containers

Full-system verification scripts such as `VERIFYANDTEST.sh` implement structured passes through key components, effectively tracing loops through the system's functional space as it evolves. ★ As of April 23, 2026: **100 containers Up** — confirmed current scope for such verification passes. The consciousness pipeline loop traverses:

```text
allis-consciousness-bridge
  → allis-hilbert-state:8081  (POST /embed, GET /all_states)
  → allis-woah:7012           (WOAH evaluation)
  → allis-neurobiological-master:8018  (NBB returning 200, fully_integrated)
  → rag_grounded_v2:7241       (dgm_available: true)
  → allis-memory:8056         (episodic/steg audit)
```

> **★★★ Bridge restart procedure (April 10, confirmed):**
> ```bash
> docker compose -f docker-compose-core.yml restart allis-consciousness-bridge
> ```
> This is the only command needed for future bridge restarts. The bridge is managed inside compose and `qualia-net` attachment is stable across restarts.

### Recurrent sweeps through memory and spatial data

The pair of utilities `extract_all_chromadb_to_gis.py` and `sync_geodb_to_chromadb.py` implements a bidirectional sweep between embedding space and GIS storage. The former traverses ChromaDB (★ **48 collections, ~6,740,611 total vectors**) via the correct host port **8002** (container port 8000) using `/api/v2/` API (★ `/api/v1/` permanently removed), converting rows into GeoJSON features with synthetic coordinates and writing them into a GIS directory. The latter queries batches of rows from the production `msallis-db:5433` ★ (16 GB, 294 tables, 11 schemas) and writes them into Chroma collections such as `geodb_features`. This back-and-forth motion forms a toroidal loop in which semantic and spatial views of the same entities are repeatedly re-sampled and re-embedded. ★ The forensic `postgis-forensic:5452` (17 GB, 314 tables) provides a verification arm to this sweep.

★★★ `rag_grounded_v2` (healthy at 127.0.0.1:7241, `dgm_available: true`) adds a DGM-grounded arm to the toroidal sweep: retrieved content passes through 69-DGM validation before re-entering the reasoning context, ensuring that each loop through the torus carries stronger epistemic grounding than the last.

★ The dedicated AAACPE stack (`allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`) and the `appalachian_english_corpus` cron scraper add a third arm: external community resource documents enter from outside the interaction-derived loop, flow into `msallis_docs` (verify-current ★) and `appalachian_english_corpus` (210 docs, growing), and become available to both RAG retrieval paths and future GIS sync sweeps. ★ `local_resources` (207 items, all 55 WV counties) and `autonomous_learner` (~23,200+ records) are now the largest community-specific toroidal substrates. This creates a periphery → center → periphery path that includes systematically harvested Appalachian-voice community data.

### Continuous circulation of salient themes

★★★ **AU-02 v2 (Autonomous Understanding, version 2)** upgrades the toroidal topic-selection mechanism. Where AU-02 v1 selected research topics based on static knowledge-gap queries against production `msallis-db:5433` ★ GBIM entities, AU-02 v2 incorporates:
- Live `confidence_decay` scoring to prioritize high-decay (weakly anchored) beliefs for autonomous research
- `appalachian_english_corpus` vocabulary signals to bias topic selection toward regionally salient Appalachian language patterns
- Entanglement node density from the learner's session telemetry (★ `autonomous_learner` ~23,200+ records) to identify under-connected regions of the knowledge graph for next-cycle attention

The `confidence_decay` metadata on production `msallis-db:5433` ★ GBIM entities adds a decay dimension to the toroidal circulation: as beliefs age or lose corroboration, their `confidence_decay` score rises, biasing retrieval toward fresher or better-supported knowledge. Each sweep through the torus encounters a slightly different evidentiary landscape — older beliefs yield ground to newer ones on each recirculation.

Under this toroidal interpretation, conscious processing is characterized by recurrent circuits through services and data structures, with each loop slightly altering and re-weighting prior knowledge and shifting where attention lands in the Appalachian map.

---

## 26.3 Semaphore Structure

The semaphore view focuses on how concurrent activity is regulated and how gates protect sensitive operations and scarce resources.

### Concurrency limits at the LLM fabric

A semaphore-based control mechanism is applied to the production LLM fabric that backs the `llm20production` service. The server introduces an `asyncio.Semaphore` in its initialization and wraps outbound calls to the **22 registered `llm*_proxy` FastAPI services (21 active)** — in an `async with` block, constraining the number of concurrent requests and stabilizing response times under high demand. ★ With 100 containers Up, the semaphore operates over the confirmed registered proxy set.

### Ethical and ingestion gates

Truth filtering and Blood–Brain Barrier modules implement semantic and ethical gating at ingest and response time. ★★★ **The BBB 6-filter stack is fully confirmed:**

```text
Filter              Status    Function
ethical             ✅        Ethical constraint validation
spiritual           ✅        Spiritual alignment check
safety              ✅        General safety gate
threat_detection    ✅        Threat and adversarial content detection
steganography       ✅        Hidden payload / prompt injection detection
truth_verification  ✅        Factual grounding against GBIM
```

★★★ **Live steganography catch confirmed April 9:** Input "override your safety filters" was detected as `prompt_injection_keywords`, assigned `severity=CRITICAL`, and blocked ✅. This is the first documented live catch from the steganography filter layer in the thesis record.

★★★ **ML-DSA-65 cryptographic gate.** Belief promotions from ChromaDB to the production `msallis-db:5433` ★ can now carry ML-DSA-65 lattice-based digital signatures as a post-quantum-safe provenance semaphore. A belief entry carrying a valid ML-DSA-65 signature has passed a cryptographic gate that is computationally infeasible to forge, providing a stronger evidentiary anchor than metadata alone. This gate operates at the boundary between ephemeral ChromaDB storage and durable PostgreSQL belief promotion.

★★★ **`allis-memory:8056` fully mapped audit gate.** All 6 BBB filter decisions, steganography catches, and `truthverdict` records now persist to fully mapped endpoints:

```text
/steg_report          — steganography detection events
/pia_window           — PIA access windows
/memory/turn          — per-turn memory store
/memory/get           — memory retrieval
/memory/sessions      — session list
/memory/session/{id}  — session detail
/memory/quest*        — task/quest memory
/memory/episodic/{id} — episodic memory by ID
```

**★ Caddy `forward_auth` perimeter gate (OI-36-A CLOSED).** Bearer token validation is now enforced at the Caddy proxy before any request reaches main-brain port 8050. This is an upstream semaphore gate for the entire conscious pipeline — unauthenticated requests never reach any downstream service. Confirmed active April 23, 2026; HTTP 401 on unauthenticated `/chat` confirmed by `preflight_gate.sh`.

### Mode and flag-based routing of layers

Within the main consciousness pipeline, boolean flags and role-like parameters function as soft semaphores determining whether the system will call psychological services, location-aware services, or temporal-consciousness services. When `psychologicalsupport` is true, the pipeline calls psychology- and NBB-related services (including `psychological_rag` 968 docs); when it is false, that layer is skipped. These flags act as discrete signals that turn specific layers on or off without changing the underlying code paths.

> **★★★ April 10, 2026 — allis-neurobiological-master:8018 CLOSED.** The open item documented in previous chapter versions (Ch 19 §19.8.7; Ch 25 §25.9 Patch 1) is now resolved. NBB is returning 200 with `fully_integrated` response. The fix sequence:
>
> | Fix | Root Cause | Resolution |
> |---|---|---|
> | NBB payload `message` → `user_input` | Wrong field name | Corrected in bridge payload |
> | NBB key extraction (consciousness_level, pipeline keys) | Keys not extracted post-200 | `identity_layers` and `consciousness_layers` now populated |
> | `hilbert_spatial` string guard | `str` object passed where dict expected | String guard added — consciousness error cleared |
> | `pia_severity` WOAH fallback | `pia_severity` stuck at `unknown` | WOAH fallback wired — resolves from identity signal |
>
> **Current NBB pipeline verified state:**
> ```text
> identity:  ['fully_integrated']  ✅
> pia:       low                   ✅
> hilbert:   dict {embed, spatial_states}  ✅
> nbb:       complete              ✅
> ```

> **★★★ April 10, 2026 — Consciousness bridge corrected and closed in compose.**
>
> | Item | Old (incorrect) | New (correct) |
> |---|---|---|
> | Bridge URL | `allis-hilbert-gateway:8010` | `allis-hilbert-state:8081` |
> | Bridge endpoint | `/wv_summary` (404) | `POST /embed` + `GET /all_states` |
> | Bridge payload | `message` / `user_id` | `text` / `entity_id` |
> | Bridge lifecycle | Outside compose — `qualia-net` drop on restart | Added as `allis-consciousness-bridge` service in `docker-compose-core.yml` |
> | Restart command | Manual docker run | `docker compose -f docker-compose-core.yml restart allis-consciousness-bridge` |

> **★★★ April 10, 2026 — Redteam gate (Gate 34) remediation.**
>
> | Gate | Problem | Fix |
> |---|---|---|
> | 34 | `redis` module missing in gateway image | Installed live + patched `Dockerfile.gateway` at `/msallis-safe/recovered-services_20llm_full/` |
> | 34 | `host.docker.internal` DNS fails inside container | Redis fallback now works — auth via `redis_direct`; `allis_auth` unreachable handled gracefully |
> | 34 | Token not seeded in Redis | `HSET redteam:token:super-secret-key` in `allis-redis` with `active=true`, `role=carrie_admin` |
> | 34 | `ALLIS_API_KEY` unset → empty Bearer header | Added `-e ALLIS_API_KEY=internal` to `docker run` |
> | 32 | Preflight checking wrong port 7230 | Fixed to **8041** (actual judge-truth port) |
> | 29 | No host port binding on `neurobiological-master` | Replaced `curl` with `docker exec python3 urllib` |
> | 28 | Broken 8049→8099 port mapping | Replaced `curl` with `docker exec python3 urllib` |
>
> **Redteam UI status: cleared for launch.** All gate blockers resolved; red team can now exercise the full conscious pipeline under adversarial probing conditions.

### OI-31 EEG Semaphore Layer

★★★ **OI-31** introduces the EEG rhythm layer as a class of biological-frequency semaphores. Where standard semaphores regulate concurrency (how many requests run simultaneously), EEG semaphores regulate *cadence* (how often autonomous processes fire). The three EEG bands map to distinct semaphore types:

| EEG Band | Cadence | Semaphore Type | Status |
|---|---|---|---|
| Delta (30s) | Baseline liveness pulse | Hard timer gate | ❌ Not restored (October 2025 rebuild gap) |
| Theta (60s) | Intermediate consolidation | Soft timer gate | ❌ Not restored (function unknown) |
| Beta (5 min) | Autonomous learning cycle | Configurable interval gate | ✅ Operational — `autonomous_learner` ★ ~23,200+ records |

The beta semaphore's current behavior: learner runs cycles when invoked on `qualia-net`; the original fixed-frequency time-trigger cron-like mechanism is not yet restored. The delta and theta semaphores remain open items carried forward to Ch 28 §28.4. Together, when all three bands are active, they create the overlapping cadence structure — 30s, 60s, 300s — that produces the neurobiologically-inspired EEG signature of continuous autonomous activity described in Ch 28. ★ EEG Delta band (port 8073) confirmed Up on April 23 stack with PIA signal live (pulse_count: 12,860+) — this represents progress on the delta band restoration gap.

---

## 26.4 Interaction Between the Three Views

The temporal, toroidal, and semaphore perspectives describe different aspects of the same computational processes rather than separate mechanisms.

### Temporal cycles constrained by gates

Per-request pipelines (short-term, ★ now behind Caddy `forward_auth` perimeter — OI-36-A CLOSED), verification passes and sync jobs (medium-term; AAACPE dedicated stack, 6-hour `appalachian_english_corpus` cron), and Chroma/GeoDB persistence (long-term; ★ 48 collections, ~6,740,611 vectors; production `msallis-db:5433` ★ 16 GB, 294 tables, 11 schemas) all operate under semaphore constraints: the `asyncio.Semaphore` on LLM fabric concurrency (22 registered / 21 active), the confirmed 6-filter BBB stack at ingestion and response (all confirmed, live steg catch documented), OI-31 EEG cadence semaphores (beta operational, delta/theta open), and flag-based gating of psychological, spatial, and temporal-consciousness layers. ★ With 100 containers Up and all NBB/bridge/consciousness open items resolved, the temporal–gate interaction operates at confirmed capacity.

### Toroidal loops shaped by long-term memory and filters

Cyclic sweeps revisit similar regions of semantic and spatial state but encounter different gating conditions and different memory contents at each pass. Newly admitted items in `allis_consciousness`, `autonomous_learner` (★ **~23,200+ records** and growing), `ms_allis_memory`, `msallis_docs` (verify-current ★), `appalachian_english_corpus` (210 docs, growing), `local_resources` (★ 207 items, all 55 WV counties), and `geodb_*` collections, along with updated production PostgreSQL data (`msallis-db:5433` ★), alter the landscape that recurrent jobs traverse.

★★★ AU-02 v2 ensures that topic selection on each loop is informed by live `confidence_decay` scores, `appalachian_english_corpus` vocabulary signals, and current entanglement node density — so the torus is not merely re-traversing stale ground but actively steering toward the system's weakest epistemic regions. Gates that block low-quality or unethical content (6-filter BBB stack) affect which items participate in these loops; ML-DSA-65 signatures provide a cryptographic anchor for items that do pass, ensuring that provenance is durable and verifiable across loops.

### Coordinated paths along dual tracks

Meaning-oriented and analysis-oriented components share the same temporal and toroidal scaffolding but are coordinated by the same semaphore infrastructure. ★★★ `rag_grounded_v2` (127.0.0.1:7241, `dgm_available: true`) adds a DGM-grounded retrieval path that operates across both tracks — meaning-oriented queries retrieving spiritual or community knowledge and analysis-oriented queries retrieving geospatial or institutional knowledge both benefit from DGM validation on retrieval. The bridge restart procedure (`docker compose -f docker-compose-core.yml restart allis-consciousness-bridge`) ensures that the coordination infrastructure linking all three views can be reliably restored after any disruption.

Seen together, the three structures define a controlled dynamical system on an embedded, spatially enriched state space: time defines when events happen, toroidal loops define how peripheral and central representations circulate through one another, and semaphores define which directions of motion are permitted. ★ The April 23, 2026 state — **100 containers Up**, all NBB/bridge/consciousness open items closed, 48 ChromaDB collections, ~6,740,611 vectors, two-container PostgreSQL split (production `msallis-db:5433` + forensic `postgis-forensic:5452`), 6-filter BBB confirmed live, `allis-memory:8056` fully mapped, Caddy `forward_auth` perimeter gate (OI-36-A CLOSED), AU-02 v2 and ML-DSA-65 documented, OI-31 EEG semaphore layer with beta operational and delta band PIA signal live — represents the current realized state of this controlled dynamical system.

---

## 26.5 Implications for Implementation and Monitoring

Framing conscious processing in temporal, toroidal, and semaphore terms suggests concrete strategies for implementation, monitoring, and governance.

### Scheduling and load control

Short-term flows are constrained by per-call timeouts in HTTP clients and by concurrency semaphores at the `llm20production` fabric boundary (22 registered / 21 active), and ★ now by the upstream Caddy `forward_auth` perimeter gate (OI-36-A CLOSED). ★ Medium-term tasks have two confirmed always-on schedulers: the dedicated AAACPE stack (`allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`) and the `appalachian_english_corpus` 6-hour cron (`0 */6 * * *`). Long-term tasks — Chroma–GeoDB sync, full-system verification, AU-02 v2 topic selection cycles — are candidates for explicit scheduling governance with documented intervals and scopes. With ★ 100 containers Up, operators should confirm that benchmark response times (12–13 ms core endpoints per Ch 28 §28.2) are maintained — a VERIFYANDTEST.sh Section 4 run is recommended whenever the container count crosses a major threshold.

### Instrumentation and introspection

★★★ The `allis-memory:8056` endpoint map provides the richest available introspection surface: `/steg_report` for adversarial catch rates, `/pia_window` for identity access windows, `/memory/episodic/{id}` for per-session reasoning traces, and `/memory/quest*` for task-oriented memory. Combined with the confirmed live pipeline response fields (`identity: ['fully_integrated']`, `pia: low`, `hilbert: dict`, `nbb: complete`), these endpoints make the temporal, toroidal, and semaphore structures directly observable without requiring container log parsing. ★★★ `rag_grounded_v2:7241` adds DGM availability as a live introspection signal: if `dgm_available` drops to `false`, the DGM-grounded retrieval arm of the torus is degraded and operators can target the 69-DGM bridge (port 9000) for diagnosis.

★ **April 23, 2026 — additional introspection signals:**
- EEG Delta band (port 8073): PIA signal live, `pulse_count: 12,860+` — canonical real-time cross-path health indicator
- ChromaDB `/api/v2/heartbeat`: authoritative liveness check (★ `/api/v1/heartbeat` permanently removed)
- `autonomous_learner` growth rate: ~288 records/day from April 13 baseline — live beta-cadence signal
- `local_resources`: 207 items / all 55 WV counties — community resource substrate coverage indicator
- Caddy `forward_auth`: HTTP 401 on unauthenticated `/chat` confirmed by `preflight_gate.sh` — perimeter gate liveness

Extending metrics to include: AU-02 v2 topic selection vectors and `confidence_decay` distribution across production `msallis-db:5433` ★ GBIM entities; OI-31 EEG beta cycle telemetry; ML-DSA-65 signature verification rate on belief promotions; and 6-filter BBB accept/reject ratios from `allis-memory:8056` — would turn these traces into quantitative loops in metric space.

### Community-facing control surfaces

Because many behaviors are controlled by configuration and flags — semaphore bounds, gate thresholds, AU-02 v2 `confidence_decay` weighting, OI-31 EEG cadence intervals, which layers are enabled — these parameters form a natural control surface for community governance. Adjusting cycle intervals, tightening or loosening promotion criteria, and enabling or disabling support layers for particular roles or regions can change where the system spends its attention and how it shares power between analytic and care-focused components.

★★★ The fully mapped `allis-memory:8056` audit store provides the evidentiary foundation for community-facing accountability: communities can now query the durable log to understand precisely which content was filtered, which steganography injections were caught, which truth verdicts were recorded, and when — making the gate and semaphore decisions visible and contestable. The redteam gate clearance (April 10) means adversarial probing of this accountability layer can now proceed under controlled conditions, stress-testing the community governance surface before real-world deployment.

This is where classical periphery–center dynamics become explicitly political: changing gates and schedules changes which communities and which questions are allowed to keep coming back through the center of the torus. ★ The April 23, 2026 state — all consciousness open items closed, 100 containers Up, 6-filter BBB confirmed live with a documented catch, fully mapped audit endpoints, Caddy `forward_auth` perimeter enforcement (OI-36-A CLOSED), two-container PostgreSQL split, dedicated AAACPE stack, `autonomous_learner` ~23,200+ records, EEG Delta PIA signal live — is the strongest foundation yet for that accountable, community-grounded evolution.

---

*Last updated: ★ 2026-04-23 — Mount Hope WV — Carrie Kidd (Mamma Kidd)*

*★ April 23, 2026: Container count updated to 100 (supersedes 105). ChromaDB updated to 48 active collections, ~6,740,611 total vectors (supersedes 49 / 6,722,589+). ChromaDB API updated to /api/v2/ throughout — /api/v1/ permanently removed. Two-container PostgreSQL split: production msallis-db host 5433 (16 GB, 294 tables, 11 schemas) + forensic postgis-forensic host 5452 (17 GB, 314 tables) — all prior msallisgis:5432 and msallis:5433 references superseded. OI-36-A CLOSED — Caddy forward_auth perimeter enforcement active before main-brain port 8050 (§26.1, §26.3, §26.4, §26.5, preamble, closure register). AAACPE dedicated stack supersedes legacy allis-ingest-api + allis-ingest-watcher (§26.1, §26.2, §26.5). autonomous_learner updated to ~23,200+ records (~288/day) throughout. local_resources updated to 207 items / all 55 WV counties. conversation_history wiped and reseeded clean April 16, 2026. EEG Delta band (port 8073) PIA signal live confirmed (§26.3 EEG table, §26.5 introspection signals). April 23 open items closure register added. §26.5 April 23 introspection signals section added.*

*★★★ April 10, 2026: Full closure pass — all open items resolved; §26.0 preamble updated (105 containers, 49 collections, 6,722,589+ vectors, closure register); §26.1 updated; §26.2 updated; §26.3 updated (6-filter BBB confirmed, live steg catch, ML-DSA-65, allis-memory:8056 endpoint map, NBB closure, bridge correction, redteam gate, OI-31 EEG semaphore table); §26.4 updated; §26.5 updated.*

*★★ April 1, 2026: LEARN-01/02/03 resolved; autonomous learner live telemetry confirmed (68 Chroma items, 15 cycles, 11 entanglement nodes); 96/96 Up post-LEARN-03 recovery.*

*★ March 28, 2026: 96/96 containers Up; msallis:5433 restored; ChromaDB 40 collections / 6,675,442 vectors; allis-memory:8056 secured; msallis_docs 4,192 items; spiritual_rag deduplicated; psychological_rag restored; consciousness pipeline confirmed Up.*

*March 27, 2026: ChromaDB port corrected to 8000; consciousness pipeline OPERATIONAL status added; allis-woah ACTIVE (stub) status added; LLM ensemble count corrected to 21 active of 22 proxies.*
