# Chapter 19 — Container Architecture and Routing

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*

*Last updated: 2026-04-14*

> **April 14, 2026 update:** 109 running containers confirmed. Two new dedicated AAACPE services added to compose: `jarvis-aaacpe-scraper` (host 8048 → container 8033) and `jarvis-aaacpe-rag` (host 8047 → container 8032). APScheduler `run_full_scrape` runs daily at 06:00 UTC and every 6 hours. `appalachian_cultural_intelligence` collection at 1,090 docs (2 scrape runs completed; last_run_new_docs: 123). AAACPE ingest pipeline open item closed — legacy `jarvis-ingest-api` + `jarvis-ingest-watcher` path superseded by dedicated AAACPE stack. ChromaDB now at 49 named collections (previously 40). `EMBED_MODEL=all-minilm:latest` (384-dim) confirmed canonical across all 49 collections. `JARVIS_API_KEY` plaintext bypass permanently removed from `msjarvis-unified-gateway.py` as of 2026-04-03 — gateway now reads only from Docker secret `secrets/jarvis_api_key.txt`; `/auth/token` bootstrap tokens must be registered in the auth service's invite store. `jarvis-consciousness-bridge` DNS fix confirmed — `NEUROMASTER_URL` correctly resolves to `jarvis-neurobiological-master:8018` on `qualia-net`; `/health` endpoint returning HTTP 200. `jarvis-neurobiological-master` network fix — container now on both `qualia-net` and `msjarvis-rebuild_default` bridge for cross-stack connectivity. `docker-compose.yml` finalized April 13, 2026 ~21:31; stale `.bak.*` variants in working directory are historical artifacts only — do not use. `scripts/preflight_gate.sh` validates 64-byte key file before any compose up.

---

## Why This Matters for Polymathmatic Geography

This chapter explains how Ms. Jarvis's containers receive, sort, and route the flows of experience that later become memory and decision support. It supports:

- **P1 – Every where is entangled** by treating events from people, places, and institutions as a shared stream that must be carefully routed into PostgreSQL `msjarvisgis` (port 5435, 45 GB PostGIS, 515 public tables / 742 total tables) and ChromaDB memory (49 collections, 6,722,589+ vectors).
- **P3 – Power has a geometry** by making explicit which services, ports, and stores stand between community data and long-term inference in PostgreSQL, and by naming `gbim_query_router` (port 7205) as the service that makes corporate and government land ownership queryable by natural language for the first time.
- **P5 – Design is a geographic act** by encoding how Appalachian events move through Ms. Jarvis and into PostgreSQL spatial, semantic, and commons-oriented stores, and by treating the routing decision to bypass ChromaDB entirely for landowner queries as an explicit architectural choice with geographic and ethical consequences.
- **P12 – Intelligence with a ZIP code** by prioritizing spatial, governance, and commons contexts in the way container records are tagged and stored, and by recognizing `gbim_query_router` as the service that closes the `who` axis at parcel scale. As of April 14, 2026: **109 containers**, **49 ChromaDB collections**, **6,722,589+ total vectors**, and a fully operational dedicated AAACPE intelligence pipeline — all running on a single Lenovo Legion 5 in Oak Hill, West Virginia.
- **P16 – Power accountable to place** by using auditable container flows and verification scripts so communities can see where their data goes in PostgreSQL `msjarvisgis` and ChromaDB, and by ensuring that corporate and government landholdings are queryable with full assessor provenance through `gbim_query_router`.

As such, this chapter belongs to the **Computational Instrument** tier — it describes the container and routing structures that turn raw events into traceable, place-aware memory anchored in PostgreSQL.

---

## 19.0 Production State (April 14, 2026)

| Property | Value |
|:--|:--|
| Total containers | **109** (compose-managed + `jarvis_auth_service` systemd-managed) |
| Compose file | `msjarvis-rebuild-working/msjarvis-rebuild/docker-compose.yml` — finalized April 13, 2026 ~21:31 |
| Docker Compose version | v5.1.0 |
| Build directives | Converted to image references for non-judge services — no rebuilds on startup |
| Judge services | Real source files confirmed in `services/` — `--no-cache` rebuild March 22, 2026 |
| Caddy perimeter layer | Port 8443 public-facing — see §16.3 for current auth gap (OI-36-A) |
| `jarvis_auth_service` | Port 8055, systemd-managed (not Docker-managed) |
| `gbim_query_router` | Port 7205 — HTTP 200 OK stable |
| GBIM corpus (`msjarvisgis:5435`) | `gbim_worldview_entity` — 5,415,896 rows; `gbim_graph_edges` — 15,226,626 rows; `gbimbeliefnormalized` — 6,804,671 rows |
| `mvw_gbim_landowner_spatial` | 20,593 landowner beliefs — materialized and spatially indexed |
| ChromaDB | **49 active collections, 6,722,589+ total vectors** (April 13 full audit) |
| `appalachian_cultural_intelligence` | **1,090 docs** — 2 scrape runs completed; last_run_new_docs: 123 — served by `jarvis-aaacpe-rag:8047→8032` |
| `spiritual_texts` | 79,181 vectors (primary spiritual corpus) |
| `psychological_rag` | 968 docs (stable since March 28 restoration) |
| `msjarvis_docs` | 7,465 items (grown from 4,192 March 28) |
| `ms_jarvis_memory` | 296 records — UUID `79240788-0828-45f3-b1bc-a9a3593628a6` confirmed |
| `autonomous_learner` | 21,181 records (canonical collection name — growing ≈288/day) |
| Autonomous learner | LEARN-01/02/03 resolved April 1, 2026; dedup gate clean; semantic dedup audit pending |
| `jarvis-memory` | Port 8056 — `0.0.0.0` → `127.0.0.1` corrected; `_auth()` confirmed on 4 sensitive routes; `JARVIS_API_KEY` set |
| AAACPE pipeline | **Dedicated stack** — `jarvis-aaacpe-scraper:8048→8033` + `jarvis-aaacpe-rag:8047→8032`; APScheduler `run_full_scrape` daily 06:00 UTC + every 6h; supersedes legacy `jarvis-ingest-api` + `jarvis-ingest-watcher` path |
| Auth security | `JARVIS_API_KEY` plaintext bypass permanently removed from `msjarvis-unified-gateway.py` as of 2026-04-03; gateway reads only from Docker secret `secrets/jarvis_api_key.txt`; `/auth/token` bootstrap tokens must be registered in auth service invite store |
| Consciousness bridge DNS | `NEUROMASTER_URL` confirmed correct — `jarvis-neurobiological-master:8018` on `qualia-net`; `/health` HTTP 200 confirmed |
| Neurobiological master network | Added to both `qualia-net` and `msjarvis-rebuild_default` bridge for cross-stack connectivity |
| I-Containers | **Fully operational** — port 8015; 10 neurobiological modules; `dual_awareness: true` |
| `memories` table schema | 6 columns, 4 indexes applied to `msjarvisgis:5435` — `gbim_entity_id`, `spatial_ref`, `reviewed`, `promoted`, `source`, `chroma_id` |
| preflight gate | `scripts/preflight_gate.sh` — validates 64-byte key file + all 9 system checks before compose up |
| Compose `.bak.*` files | Stale historical artifacts in working directory — do not use; canonical compose finalized April 13, 2026 ~21:31 |
| End-to-end benchmark | 436s (optimized from 532s baseline) |
| `services-safe/` sync | `ms_jarvis_autonomous_learner_optimized.py` and `ms_jarvis_rag_server.py` synced April 1, 2026 |

---

## 19.1 Position in the Overall System

The container layer sits between external interfaces and the lower-level retrieval, optimization, and global control mechanisms. It is visible both in the `main-brain` service that handles `/chat` and `/chat_async` requests and in the autonomous learning and Fifth DGM pipelines that generate and refine internal content.

Its main responsibilities are to:

- Accept events coming from many sources, including question-handling flows, scheduled jobs, and self-improving processes.
- Normalize these events into a common format that can be evaluated and stored consistently in PostgreSQL `msjarvisgis` (port 5435, 45 GB PostGIS, 515 public / 742 total tables) and ChromaDB (49 collections, 6,722,589+ vectors).
- Dispatch normalized items into successive evaluation stages, while obeying system-wide constraints such as safety filters (BBB 7-filter stack with fail-open behavior), resource limits, and service health (30s TTL cache, 2s timeout per service).

As of April 14, 2026, all external `/chat*` traffic passes through the Caddy perimeter layer (port 8443) and `jarvis_auth_service` (port 8055) before reaching any container. Authentication gap OI-36-A remains open — see Chapter 16, §16.11. OI-36-C is closed: `JARVIS_API_KEY` plaintext bypass permanently removed from `msjarvis-unified-gateway.py` as of 2026-04-03.

---

## 19.2 Types of Incoming Events

The intake layer receives several broad categories of events:

- **Direct interactions** — User queries and responses that have already passed through Caddy authentication (Tier 1) and then `bbb-input-filter` (Tier 2). These include synchronous requests and asynchronous jobs tracked via job IDs persisted in Redis (`jarvis-redis:6379`, 30-minute TTL).
- **Internal tasks** — Results from scheduled analyses, background maintenance jobs, and optimization routines: autonomous learner outputs (21,181 records as of March 21, 2026 baseline, ≈288/day — LEARN-01/02/03 resolved), Fifth DGM optimization steps, and WOAH evaluations.
- **External signals** — Notifications or status changes from connected systems. The dedicated AAACPE stack (`jarvis-aaacpe-scraper` + `jarvis-aaacpe-rag`, operational April 14, 2026) is the primary operational external-signal ingest pathway. It supersedes the legacy `jarvis-ingest-api` + `jarvis-ingest-watcher` path for Appalachian cultural intelligence data.
- **Structural changes** — Updates to PostgreSQL `msjarvisgis` memory, GBIM belief graphs, or spatial layers that may require special attention. The March 20, 2026 ingestion of 20,593 landowner belief records and the April 13 `memories` table schema completion (6 columns, 4 indexes) are examples.

---

## 19.3 Normalization into Container Records

Before events are passed to deeper stages, they are normalized into container records with a common structure:

- **Core fields** — Unique identifier, creation and update timestamps, origin (e.g., `user_chat`, `autonomous_learner`, `aaacpe_ingest`, `gbim_landowner_update`, or `external_signal`), and a reference to the initiating service or job.
- **Context** — Active role or profile, relevant geographic or institutional context from PostgreSQL `msjarvisgis:5435` (45 GB PostGIS, 515 public tables), and tags describing the domain (`governance`, `infrastructure`, `landowner`, `community_culture`). For chat records, this includes `user_id` and any declared `mode`. For async jobs, the Redis-persisted `job_id` links the normalized record to its lifecycle state.
- **Content summary** — Key text, numerical values, or structured data extracted from the event. For landowner queries, this includes the routing decision (`mode: landowner_gbim`, `route_type: parcel_ownership`) and the SQL aggregation result from `mvw_gbim_landowner_spatial`.
- **Links** — References to memory items (ChromaDB embeddings — 49 collections, 6,722,589+ vectors, all 384-dim via `all-minilm:latest`), PostgreSQL GBIM graph nodes/edges at `msjarvisgis:5435`, relational records, spatial features, and introspective entries. BBB audit trail links route to `jarvis-memory:8056` (corrected, secured). `memories` table cross-references route to `msjarvisgis:5435` via `gbim_entity_id` and `spatial_ref`.
- **Control information** — Flags indicating initial assessments (urgency, sensitivity, safety status, BBB-approved or denied with fail-open on HTTP 500, expected resource cost, and whether the item is considered high-value for long-term retention).

---

## 19.4 First-Level Routing Decisions

Once a record is normalized, the intake layer applies initial routing logic:

- **Eligibility checks** — Safety checks (BBB 7-filter stack with `truth_score` null guard and fail-open on HTTP 500), role-based constraints, and service availability via health probes (30s TTL cache, 2s timeout per service). `scripts/preflight_gate.sh` must pass all 9 checks before any compose up.
- **Phase 1.45 community memory injection** — After BBB input approval, the main brain generates a 384-dim embedding via `all-minilm:latest` at `jarvis-ollama:11434/api/embeddings`, queries the `autonomous_learner` ChromaDB collection (21,181 records baseline, ≈288/day), retrieves the 5 most semantically similar community interaction records, and prepends them to `enhanced_message` before it reaches the 21 active LLMs.
- **Priority assignment** — Assigning a simple priority or track indicator that influences ordering and resource allocation.
- **Track assignment** — Deciding whether the record should be sent to specific container subsystems (I-Container service port 8015, psychological RAG domains via `psychological_rag` 968 docs, PostgreSQL GBIM graph updates at `msjarvisgis:5435`, `gbim_query_router` landowner path — HTTP 200 OK stable — or audit logs persisted to `jarvis-memory:8056`).

---

## 19.5 Parallel Paths

The architecture supports multiple parallel paths that share a common structural pattern (intake → normalization → gating → storage in PostgreSQL or ChromaDB or discard):

- **Affective and care-oriented paths** — Used when events are framed in terms of meaning, care, or psychological support. These involve specialized RAG domains (`psychological_rag` 968 docs, stable), therapeutic or community-oriented analysis, and services that emphasize ethical interpretation and human impact.
- **Analytical and technical paths** — Used for infrastructure planning (PostgreSQL `msjarvisgis`), spatial reasoning, optimization over data, and structured ownership queries via `gbim_query_router`. These paths emphasize quantitative reasoning, model-based analysis, and technical verification against PostgreSQL GBIM ground truth (`msjarvisgis:5435`, `gbim_worldview_entity` 5,415,896 rows).
- **Deterministic relational retrieval path** — The `gbim_query_router` landowner path. It does not involve LLM reasoning, ChromaDB vector search, or web research. It is the system's only fully deterministic query path. HTTP 200 OK stable.
- **Dedicated AAACPE intelligence path (operational April 14, 2026)** — The `jarvis-aaacpe-scraper` (port 8048→8033) + `jarvis-aaacpe-rag` (port 8047→8032) stack. APScheduler triggers `run_full_scrape` daily at 06:00 UTC and every 6 hours. Scraped documents are embedded with `all-minilm:latest` and written to the `appalachian_cultural_intelligence` ChromaDB collection (1,090 docs as of April 14 — 2 scrape runs completed, last_run_new_docs: 123). This path supersedes the legacy `jarvis-ingest-api` + `jarvis-ingest-watcher` path for Appalachian cultural intelligence data. See §19.8.11 for full specification.
- **Autonomous learning path** — `jarvis-autonomous-learner` stores findings every 5 minutes into `autonomous_learner` ChromaDB collection. LEARN-01/02/03 resolved April 1, 2026. Dedup gate running cleanly. ⚠️ Semantic dedup audit pending.

---

## 19.6 Outputs of the Routing Layer

After routing, the container layer produces:

- **Records marked for immediate evaluation** — Items that pass eligibility checks and have sufficient priority are forwarded to downstream evaluators (21-model LLM consensus, truth validators, or `gbim_query_router` SQL aggregation). Their container records carry all necessary context and links to PostgreSQL tables at `msjarvisgis:5435`.
- **Records held back or dropped** — Events may be queued, delayed, rate-limited, or dropped entirely based on policy.
- **Introspective logs and verification entries** — The system records which paths were chosen, which services were invoked, what PostgreSQL queries were executed, and what the outcomes were. BBB audit events persist to `jarvis-memory:8056` (secured `127.0.0.1`, `_auth()` confirmed, `JARVIS_API_KEY` set). Promotion events are tracked in the `memories` table in `msjarvisgis:5435` via `reviewed` and `promoted` columns.

---

## 19.7 Conceptual Summary

The container architecture provides a structured way to receive, normalize, and direct events into deeper evaluative paths anchored in PostgreSQL `msjarvisgis` (port 5435, 45 GB PostGIS, 515 public tables / 742 total tables). It defines how diverse inputs — user interactions, internal learning results, dedicated AAACPE scraper documents, and structural changes — enter the system's evaluative core.

The remaining sections ground this abstraction in the current production deployment topology, focusing on Docker containers, port mappings, compose management, and service roles as of **April 14, 2026**.

---

## 19.8 Operational Container Topology (April 14, 2026)

This section is the authoritative operational state as of April 14, 2026. The topology is derived from `msjarvis-rebuild-working/msjarvis-rebuild/docker-compose.yml` (finalized April 13, 2026 ~21:31, Docker Compose v5.1.0), runtime `docker ps` output, `jarvis_startup.sh`, and verification scripts.

**Compose management baseline — April 14, 2026:**

- All **109** Docker-managed production containers are defined in the canonical `docker-compose.yml` — zero Restarting, zero Exited.
- `jarvis_auth_service` (port 8055) is systemd-managed, not Docker-managed — see §19.8.2.
- `gbim_query_router` (port 7205) — HTTP 200 OK stable.
- `jarvis-memory` (port 8056) — confirmed `127.0.0.1`; `_auth()` confirmed; `JARVIS_API_KEY` set.
- `jarvis-aaacpe-scraper` (8048→8033) and `jarvis-aaacpe-rag` (8047→8032) — active compose inventory; APScheduler `run_full_scrape` daily 06:00 UTC + every 6h.
- Legacy `jarvis-ingest-api` and `jarvis-ingest-watcher` — superseded by dedicated AAACPE stack for Appalachian cultural intelligence ingest. Status in compose: historical reference only.
- `JARVIS_API_KEY` plaintext bypass removed from `msjarvis-unified-gateway.py` as of 2026-04-03 (OI-36-C closed). Gateway reads only from Docker secret `secrets/jarvis_api_key.txt`.
- `scripts/preflight_gate.sh` validates 64-byte key file and all 9 system checks — must pass before every `docker compose up`.
- Stale `.bak.*` compose variants in working directory are historical artifacts — do not use for any operational purpose.
- All build directives remain converted to image references for non-judge services.
- Judge service images were rebuilt with `--no-cache` on March 22, 2026.
- Reboot sequence: `scripts/preflight_gate.sh` (must pass) → `docker compose up -d` → `jarvis_startup.sh`.

---

### 19.8.0 Orphaned Container Warning — Expected Behavior

> **⚠️ Documented March 25, 2026:** Running `docker compose up -d` from the `msjarvis-rebuild` project directory will produce a warning similar to:

```
WARN Found orphan containers (nbb_woah_algorithms, nbb_i_containers,
llm1-proxy, llm2-proxy, ... llm22-proxy) for this project.
If you removed or renamed this service in your compose file, you can run
this command with the --remove-orphans flag to clean it up.
```

**This is expected behavior.** The `nbb_*` containers and `llm*-proxy` containers are managed by a **separate compose file** in a different project directory.

> **⚠️ CRITICAL: Do NOT use `--remove-orphans`** unless you are intentionally decommissioning the NBB stack and all LLM proxy containers. Using `--remove-orphans` will stop and remove all `nbb_*` and `llm*-proxy` containers, taking down the NBB prefrontal stack (Chapter 12, §12.12), the WOAH algorithms service (Chapter 10), and all 22 LLM proxy containers (§19.8.9).

**Safe reboot procedure:**

```bash
# Step 0: Run preflight gate — must pass all 9 checks
bash scripts/preflight_gate.sh

# Step 1: CORRECT — never use --remove-orphans
cd msjarvis-rebuild-working/msjarvis-rebuild
docker compose up -d
# Orphan warning will appear — expected and harmless

# WRONG — will decommission NBB stack and LLM proxies
# docker compose up -d --remove-orphans  ← DO NOT USE
```

---

### 19.8.1 Caddy Perimeter Layer

The Caddy reverse proxy is the outermost layer of the routing stack. See Chapter 16, §16.3 for current status including OI-36-A (auth enforcement gap). OI-36-C is closed — see §19.0.

```
┌──────────────────────────────────────────────────────────────────┐
│ Caddy Perimeter Layer — April 14, 2026                          │
├──────────────────────────────────────────────────────────────────┤
│ Port: 8443 (public-facing, HTTPS)                               │
│ Log path: /var/log/caddy/jarvis_redteam.log                     │
│                                                                  │
│ Route: /chat*                                                    │
│   → 127.0.0.1:8050 (unified gateway)                            │
│   ⚠ Token enforcement not active at proxy level (OI-36-A open) │
│                                                                  │
│ Route: /auth*, /feedback*, /chat/status*                        │
│   → 127.0.0.1:8055 (jarvis_auth_service)                        │
│                                                                  │
│ Route: /health*, /systems*                                       │
│   → 127.0.0.1:8050 (unified gateway)                            │
│                                                                  │
│ jarvis-memory:8056 — localhost-bound only, NOT routed through   │
│ Caddy. _auth() confirmed, JARVIS_API_KEY set.                   │
└──────────────────────────────────────────────────────────────────┘
```

---

### 19.8.2 `jarvis_auth_service` — Port 8055

`jarvis_auth_service` is the authentication enforcement service. It is systemd-managed, not Docker-managed, and runs on port 8055 at all times including during `docker compose down` operations. See Chapter 16, §16.3.2 for full specification.

| Property | Value |
|:--|:--|
| Port | 8055 |
| Management | systemd (not Docker Compose) |
| Source file | `scripts/jarvisauthservice.py` |
| Primary endpoint | `POST /auth/token` |
| Secondary endpoint | `GET /health` |
| Token contract | Bootstrap token from `secrets/jarvis_api_key.txt` — does **not** auto-validate; tokens must be registered in the auth service's invite store (OI-36-C closure) |

`jarvis-memory` (port 8056) is the BBB audit trail store — distinct from `jarvis_auth_service`. Docker-managed. Secured March 28, 2026.

---

### 19.8.3 Core Orchestration Layer

```
Container                Port Mapping    Role
─────────────────────────────────────────────────────────────────────
jarvis-main-brain        8051→8050       External API entry point:
                                         /chat, /chat_async — 30s TTL
                                         health-check cache, Phase 1.45
                                         community memory retrieval,
                                         service orchestration,
                                         Redis-backed async job mgmt,
                                         RAG queueing to ChromaDB
                                         (49 collections, 6,722,589+
                                         vectors) backed by PostgreSQL
                                         msjarvisgis:5435;
                                         routes mode:landowner_gbim
                                         queries to gbim_query_router
```

The `jarvis-main-brain` container hosts the Ms. Jarvis ULTIMATE main-brain FastAPI application. It exposes `/health`, `/chat`, `/chat_async`, `/chat_status/{job_id}`, `/chat_cancel/{job_id}`, and `/chat_cancel_all` endpoints. Health checks use a 30s TTL cache with 2s per-service timeout. Async job state persists in Redis with 30-minute TTL and survives container restarts.

---

### 19.8.4 Blood-Brain Barrier and Safety Services

> **⚠️ BBB container architecture:** There is **one** BBB container: `jarvis-blood-brain-barrier` at **port 8016**. Port 8017 (`bbb-output-filter`) does **not exist**. Both input filtering (Phase 1.4) and output filtering (Phase 4.5) are handled by the single service at port 8016. See Chapter 16 for full specification.

**Confirmed BBB API surface (April 13, 2026):**

| Endpoint | Purpose |
|---|---|
| `/` | Service identity and active filter list |
| `/health` | Health check |
| `/filter` | Primary first-stage filter |
| `/truth` | Truth assessment |
| `/stats` | Aggregate filter statistics |
| `/filter_output` | Output-stage filtering |

There is no `/check` endpoint. Any prior script or documentation referencing `/check` on port 8016 is stale.

```
Container                Port Mapping    Role
─────────────────────────────────────────────────────────────────────
jarvis-blood-brain-      8016→8016       Single BBB container.
barrier                                  Phase 1.4: constitutional
                                         input filter (BLOCKING) —
                                         /filter and /truth endpoints.
                                         Phase 4.5: output filter
                                         (LOG+PASSTHROUGH — OI-02) —
                                         /filter_output endpoint.
                                         Fail-open on HTTP 500.
                                         Verdict → jarvis-memory:8056

jarvis-memory            8056→8056       BBB audit trail persistence.
                                         Corrected: 0.0.0.0 → 127.0.0.1
                                         _auth() confirmed on 4 routes
                                         JARVIS_API_KEY set
                                         /health public; /memory/* protected
                                         Full API: /memory/turn,
                                         /memory/get, /memory/sessions,
                                         /memory/session/{id},
                                         /memory/quest, /memory/quests,
                                         /memory/consolidate,
                                         /memory/episodic,
                                         /steg_report, /pia_window
                                         No /events endpoint — stale ref.

jarvis-bbb-ethics-proxy  —               Ethics routing shim
```

---

### 19.8.5 LLM Ensemble and Synthesis

```
Container                Port Mapping    Role
─────────────────────────────────────────────────────────────────────
jarvis-20llm-production  8008→8008       22-proxy LLM ensemble
                                         (22 registered; 21 active;
                                         BakLLaVA eliminated;
                                         StarCoder2 excluded from
                                         scoring)

jarvis-llm22-proxy       8030→8030       Semaphore proxy for
(semaphore)                              jarvis-20llm-production;
                                         max_tokens: -1, unlimited output

jarvis-lm-synthesizer    8001 internal   LM Synthesizer — calls
                                         jarvis-ollama:11434/api/generate
                                         with llama3.1:latest; Ms. Jarvis
                                         persona prompt merged; Phase 3.5
                                         / 3.75 single pass

jarvis-web-research      8009→8009       External knowledge retrieval;
                                         excluded for landowner_gbim mode
```

---

### 19.8.6 Judge Pipeline (compose-managed, all ports bound to 127.0.0.1)

```
Container                  Internal Port  Source File                    Role
───────────────────────────────────────────────────────────────────────────
jarvis-judge-pipeline      7239           services/judgepipeline.py      Coordinator;
                                                                          POST /evaluate;
                                                                          asyncio.gather
                                                                          aggregation;
                                                                          bbb_check_verdict
                                                                          live httpx POST

jarvis-judge-truth         7230           services/judgetruthfilter.py   Truth eval;
                                                                          heuristic_
                                                                          contradiction_v1

jarvis-judge-consistency   7231           services/judgeconsistency       Internal
                                          engine.py                       coherence;
                                                                          contradiction
                                                                          detection

jarvis-judge-alignment     7232           services/judgealignment         Ms. Jarvis
                                          filter.py                       identity
                                                                          adherence;
                                                                          community values

jarvis-judge-ethics        7233           services/judgeethics            Harm screening;
                                          filter.py                       spiritual
                                                                          appropriateness

jarvis-69dgm-bridge        9000           —                               69-DGM cascade;
                                                                          23-connector
                                                                          3-stage; validates
                                                                          every production
                                                                          response
```

All five judge containers are compose-managed with `restart: unless-stopped`. ML-DSA-65 signing: FULLY ACTIVE — `sprint1_activate_signing.py` ran 19 PASS, 0 FAIL on March 22, 2026.

---

### 19.8.7 Memory, Learning, and Optimization Services

```
Container                  Port Mapping   Role
───────────────────────────────────────────────────────────────────
jarvis-autonomous-learner  8053→8053      Autonomous learning.
                                          LEARN-01/02/03 RESOLVED
                                          April 1, 2026.
                                          21,181 records baseline
                                          (March 21, 2026);
                                          accumulation ≈288/day.
                                          Canonical collection name:
                                          autonomous_learner
                                          (underscore, ending "er").
                                          autonomous_learning (17,707)
                                          status unconfirmed.
                                          autonomouslearner (no
                                          underscore) is stale.
                                          ⚠️ Semantic dedup audit pending

jarvis-i-containers        8015→8015      FULLY OPERATIONAL April 13.
                                          ms_jarvis_i_containers_service.py
                                          10 neurobiological modules —
                                          I-Container 1: SelfRecognition,
                                          IdentityCore, PersonalNarrative,
                                          EgoBoundaries, MemorySelf;
                                          I-Container 2:
                                          WitnessConsciousness,
                                          ReflectionSystem,
                                          IntrospectionEngine,
                                          MetacognitiveAwareness,
                                          ObserverSelf.
                                          dual_awareness: true confirmed.
                                          127.0.0.1:8015->8015/tcp

jarvis-fifth-dgm           4002→4002      Darwin-Gödel-style
                                          optimization and filtering

jarvis-neurobiological-    8018→8018      Higher-level coordination.
master                                    Network fix April 14:
                                          added to qualia-net AND
                                          msjarvis-rebuild_default bridge
                                          for cross-stack connectivity.
                                          DNS fix: NEUROMASTER_URL =
                                          jarvis-neurobiological-master:8018
                                          on qualia-net confirmed correct.
                                          /health HTTP 200 confirmed from
                                          consciousness bridge.

jarvis-hippocampus         8011→8011      Hippocampal consolidation;
                                          GBIM beliefs → ChromaDB
                                          (49 collections, 6,722,589+
                                          vectors) pipeline

jarvis-memory              8056→8056      BBB audit trail persistence.
                                          Secured March 28, 2026.
                                          0.0.0.0 → 127.0.0.1 corrected.
                                          See §19.8.4 for full API surface.

jarvis-aaacpe-scraper      8048→8033      AAACPE dedicated scraper.
                                          APScheduler: run_full_scrape
                                          daily 06:00 UTC + every 6h.
                                          Feeds jarvis-aaacpe-rag.
                                          Supersedes jarvis-ingest-api
                                          + jarvis-ingest-watcher for
                                          Appalachian cultural data.

jarvis-aaacpe-rag          8047→8032      AAACPE dedicated RAG service.
                                          Serves appalachian_cultural_
                                          intelligence collection.
                                          1,090 docs as of April 14
                                          (2 scrape runs; last_run_
                                          new_docs: 123).
                                          EMBED_MODEL: all-minilm:latest
                                          (384-dim).
```

---

### 19.8.8 RAG Domain Services

```
Container                  Port Mapping   Role
───────────────────────────────────────────────────────────────────
jarvis-rag-server          8003→8016      Text RAG — direct_rag path.
                                          ⚠ Host 8003 maps to container-
                                          internal uvicorn listener on
                                          port 8016. Mapping is
                                          127.0.0.1:8003:8016.
                                          See §19.8.8a for required
                                          env vars.

jarvis-gis-rag             8004→8004      GIS spatial RAG queries;
                                          geospatialfeatures;
                                          PostgreSQL msjarvisgis:5435

jarvis-spiritual-rag       8005→8005      Spiritual/cultural RAG.
                                          Note: spiritual_rag as a
                                          single collection does not
                                          exist. Corpus is split:
                                          spiritual_texts (79,181) —
                                          primary; spiritual_wisdom (135);
                                          spiritual_knowledge (12).

jarvis-psychology-services 8019→8019      Psychological safety services;
                                          Phase 3 pre-assessment

psychological-rag-domain   8006→8006      Psychological RAG domain;
                                          psychological_rag collection —
                                          968 docs, stable since
                                          March 28 restoration

gbim_query_router          7205→7205      GBIM landowner belief query
                                          router. PostgreSQL-native ONLY.
                                          HTTP 200 OK stable.
                                          Queries mvw_gbim_landowner_
                                          spatial in msjarvisgis:5435
                                          via SQL aggregation.
                                          proposition_codes:
                                          LANDOWNER_CORPORATE,
                                          LANDOWNER_GOVERNMENT.
                                          worldview: eq1.
                                          20,593 verified landowner
                                          beliefs. NO ChromaDB —
                                          bypassed entirely.
```

---

### 19.8.8a `jarvis-rag-server` — Port Correction and Required Environment Variables

> **⚠️ Critical port correction (March 25, 2026):** The `jarvis-rag-server` docker-compose port mapping is `127.0.0.1:8003:8016`. Host port 8003 maps to container-internal uvicorn listener on port 8016. All host-side calls use port 8003; all container-internal references must use `jarvis-rag-server:8016`.

```yaml
jarvis-rag-server:
  image: python:3.11-slim
  container_name: jarvis-rag-server
  ports:
    - "127.0.0.1:8003:8016"
  environment:
    - OLLAMA_HOST=http://jarvis-ollama:11434
    - EMBED_MODEL=all-minilm:latest
    - CHROMA_HOST=http://jarvis-chroma:8000
  networks:
    - qualia-net
```

| Variable | Correct value | Consequence of missing |
|:--|:--|:--|
| `OLLAMA_HOST` | `http://jarvis-ollama:11434` | All embedding calls fail |
| `EMBED_MODEL` | `all-minilm:latest` | Embedding calls fail — wrong model |
| `CHROMA_HOST` | `http://jarvis-chroma:8000` | ChromaDB connections fail |

> **⚠️ EMBED_MODEL — canonical value is `all-minilm:latest` (384-dim) across all 49 ChromaDB collections (6,722,589+ vectors).** Any compose file entry showing `EMBED_MODEL=nomic-embed-text` must be corrected before the next restart — `nomic-embed-text` produces 768-dim vectors and is incompatible with all existing collections. This applies to `jarvis-aaacpe-rag` and any other service with an `EMBED_MODEL` environment variable.

---

### 19.8.9 LLM Proxy Layer (21 active models, 22 registered proxies)

| Proxy | Port | Model |
|:--|:--|:--|
| llm1-proxy | 8201 | TinyLlama `tinyllama:latest` |
| llm2-proxy | 8202 | Gemma `gemma:2b` |
| llm3-proxy | 8203 | MedLlama2 `medllama2:latest` |
| llm4-proxy | 8204 | MiniCPM-V `minicpm-v:latest` |
| llm5-proxy | 8205 | LLaVA `llava:latest` |
| llm6-proxy | 8206 | SQLCoder `sqlcoder:latest` |
| llm7-proxy | 8207 | StarCoder2 `starcoder2:latest` — excluded from scoring |
| llm8-proxy | 8208 | CodeLlama `codellama:latest` |
| llm9-proxy | 8209 | DeepSeek Coder `deepseek-coder:latest` |
| llm10-proxy | 8210 | Phi3 Mini `phi3:mini` |
| llm11-proxy | 8211 | BakLLaVA — **permanently eliminated** |
| llm12-proxy | 8212 | Dolphin-Phi `dolphin-phi:latest` |
| llm13-proxy | 8213 | Orca-Mini `orca-mini:latest` |
| llm14-proxy | 8214 | Qwen2 `qwen2:latest` |
| llm15-proxy | 8215 | Zephyr `zephyr:latest` |
| llm16-proxy | 8216 | Starling-LM `starling-lm:latest` |
| llm17-proxy | 8217 | Neural-Chat `neural-chat:latest` |
| llm18-proxy | 8218 | OpenChat `openchat:latest` |
| llm19-proxy | 8219 | Vicuna `vicuna:latest` |
| llm20-proxy | 8220 | LLaMA 2 `llama2:latest` |
| llm21-proxy | 8221 | Mistral `mistral:latest` |
| llm22-proxy | 8222 | LLaMA 3.1 `llama3:latest` |

> **⚠️ Orphaned container warning:** All `llm*-proxy` containers are managed by a separate compose file. Running `docker compose up -d` from the `msjarvis-rebuild` directory will produce orphan warnings. This is expected. Do NOT use `--remove-orphans`. See §19.8.0.

21 models reliably active; BakLLaVA permanently eliminated; StarCoder2 excluded from scoring. `gbim_query_router` landowner queries do not pass through the LLM ensemble.

---

### 19.8.10 Data Persistence and Semantics

```
Container                  Port Mapping   Role
───────────────────────────────────────────────────────────────────
jarvis-chroma              8002→8000      Canonical ChromaDB instance.
                                          Host port 8002 (NOT 8000).
                                          chromadata volume at
                                          /home/ms-jarvis/msjarvis-rebuild/
                                          persistent/chroma → /data
                                          (authoritative SQLite backup
                                          source — not 3-file JSON set).
                                          384-dim all-minilm:latest.
                                          On qualia-net.
                                          Chroma server 1.0.0 /
                                          client chromadb==1.5.5.
                                          /api/v2/ only — /api/v1/
                                          permanently removed.
                                          49 active collections,
                                          6,722,589+ total vectors.
                                          LANDOWNER BELIEFS NOT STORED
                                          HERE.

jarvis-local-resources-db  5435→5432      PostgreSQL 16 + PostGIS.
(msjarvisgis)                            45 GB. 515 public tables,
                                          742 total tables.
                                          993 ZCTA centroids.
                                          gbim_worldview_entity:
                                          5,415,896 rows.
                                          gbim_graph_edges:
                                          15,226,626 rows.
                                          gbimbeliefnormalized:
                                          6,804,671 rows.
                                          mvw_gbim_landowner_spatial:
                                          20,593 rows.
                                          memories table: 6 columns,
                                          4 indexes (April 13, 2026).
                                          building_parcel_county_tax_mv:
                                          7,354,707 rows.

jarvis-msjarvis-db         5433→5432      Added to compose April 13,
                                          2026. external: true volume
                                          for msjarvis_pgdata.
                                          Container healthy.
                                          msjarvis database: offline
                                          for live GBIM ops.
                                          All live GBIM data in
                                          msjarvisgis on 5435.
                                          Prior msjarvis-pgdata-rescue
                                          container retired.

jarvis-redis               6379→6379      Redis; async job state,
                                          30-min TTL; idempotency
                                          TTL 1,800s; health cache

jarvis-ollama              11434→11434    Ollama LLM backend;
                                          all-minilm:latest 384-dim
                                          embeddings; llama3.1:latest
                                          LM Synthesizer; all 22 model
                                          proxies. On qualia-net.

jarvis-memory              8056→8056      BBB audit trail persistence.
                                          Secured March 28, 2026.
                                          See §19.8.4 for full API.
```

**Canonical ChromaDB collections — April 14, 2026 (all 384-dim via `all-minilm:latest`):**

| Collection | Records | Notes |
|:--|:--|:--|
| `gbim_worldview_entities` | 5,416,521 | Complete WV GBIM spatial corpus |
| `address_points` | 1,115,588 | — |
| `spiritual_texts` | 79,181 | Primary spiritual corpus — `spiritual_rag` as unified collection does not exist |
| `autonomous_learning` | 17,707 | Status unconfirmed — see §19.5 canonicalization note |
| `geospatialfeatures` | 60,875 | — |
| `GBIM_sample_rows` | 5,000 | — |
| `gbim_beliefs_v2` | 5,000 | — |
| `msjarvis_docs` | 7,465 | Grown from 4,192 (March 28) |
| `autonomous_learner` | 21,181 | **Canonical name** — confirmed ✅ |
| `appalachian_cultural_intelligence` | 1,090 | Served by `jarvis-aaacpe-rag:8047→8032`; 2 scrape runs; last_run_new_docs: 123 |
| `research_history` | 785 | Grown from 16 ✅ |
| `ms_jarvis_memory` | 296 | UUID `79240788-0828-45f3-b1bc-a9a3593628a6` confirmed ✅ |
| `psychological_rag` | 968 | Stable since March 28 ✅ |
| `gis_wv_benefits` | 4,668 | — |
| `GBIM_Fayette_sample` | 1,535 | — |
| `conversation_history` | 564 | — |
| `governance_rag` | 643 | — |
| `zcta_centroids` | 829 | — |
| `commons_rag` | 306 | — |
| `appalachian_english_corpus` | 227 | — |
| `local_resources` | 101 | — |
| `spiritual_wisdom` | 135 | — |
| `spiritual_knowledge` | 12 | — |
| `contracts` | 51 | — |
| `geospatial_features` | 50 | — |
| `au02_threat_seeds` | — | Active — added since March 28 |
| `msjarvis-smoke` | 1 | Smoke test record |

> **Total confirmed April 13, 2026 full audit: 49 active collections, 6,722,589+ total vectors.**

> **⚠️ LANDOWNER BELIEFS (`LANDOWNER_CORPORATE`, `LANDOWNER_GOVERNMENT`) are NOT in ChromaDB.** Served exclusively by `gbim_query_router` (port 7205) via `mvw_gbim_landowner_spatial` in `msjarvisgis:5435`. 20,593 records. PostgreSQL-native path only.

> **⚠️ UUID preservation risk:** `ms_jarvis_memory` UUID `79240788-0828-45f3-b1bc-a9a3593628a6` is hardcoded in the consciousness bridge. If ChromaDB is rebuilt, run `scripts/preserve_memory_uuid.sh` before maintenance and `scripts/restore_memory_uuid.sh` after if UUID is lost. See Ch. 22 §22.10.

> **⚠️ ChromaDB v2 API:** All shell-based commands must use `/api/v2/tenants/default_tenant/databases/default_database/`. The `/api/v1/` path is permanently removed. Python `chromadb` client (1.5.5) handles this transparently.

---

### 19.8.11 Dedicated AAACPE Intelligence Pipeline (new, April 14, 2026)

The AAACPE (Appalachian App Cultural and Community Platform Engine) intelligence pipeline is now served by two dedicated containers added to compose inventory as of April 14, 2026. This replaces the legacy `jarvis-ingest-api` + `jarvis-ingest-watcher` path for Appalachian cultural intelligence data.

| Container | Host Port | Container Port | Role |
|---|---|---|---|
| `jarvis-aaacpe-scraper` | 8048 | 8033 | Web scraper; APScheduler scheduler |
| `jarvis-aaacpe-rag` | 8047 | 8032 | RAG query service; serves `appalachian_cultural_intelligence` collection |

**Scheduler configuration:**

- `run_full_scrape` — triggered daily at 06:00 UTC and every 6 hours (APScheduler).
- Scraped documents are embedded with `all-minilm:latest` (384-dim) and written to the `appalachian_cultural_intelligence` ChromaDB collection.

**Collection state as of April 14, 2026:**

- `appalachian_cultural_intelligence` — 1,090 documents
- 2 scrape runs completed
- `last_run_new_docs`: 123

**Open item closed:** The prior open item for the AAACPE pipeline (previously relying on `jarvis-ingest-api` + `jarvis-ingest-watcher`) is closed. The dedicated `jarvis-aaacpe-scraper` + `jarvis-aaacpe-rag` stack is the authoritative ingest and query path for Appalachian cultural intelligence data. Any reference to `jarvis-ingest-api` or `jarvis-ingest-watcher` as the AAACPE ingest mechanism is stale.

---

## 19.9 Auth and Security Updates (April 2026)

### OI-36-C — Closed (2026-04-03)

`JARVIS_API_KEY` plaintext bypass has been permanently removed from `msjarvis-unified-gateway.py`. The gateway now reads only from the Docker secret at `secrets/jarvis_api_key.txt`.

**`/auth/token` contract change:** Bootstrap tokens derived from the secret file no longer auto-validate. Tokens must be registered in the auth service's invite store before they will be accepted.

**Preflight gate key check:** `scripts/preflight_gate.sh` validates that the `secrets/jarvis_api_key.txt` file is exactly 64 bytes before any compose up. If the file is missing, truncated, or contains placeholder content, the gate fails and compose up must not proceed.

### OI-36-A — Still Open

Auth enforcement at the Caddy perimeter level (token validation before routing to `/chat*`) remains open. See Chapter 16, §16.11.

---

## 19.10 Consciousness Bridge and Neurobiological Master (April 2026)

### DNS Resolution Fix (April 14, 2026)

`NEUROMASTER_URL` was briefly mis-routed. Confirmed correct hostname:

```
jarvis-neurobiological-master:8018
```

on `qualia-net`. Connectivity confirmed via `docker exec` DNS probe and HTTP 200 on `/health` from the consciousness bridge.

### Network Topology Fix (April 14, 2026)

`jarvis-neurobiological-master` was previously on `qualia-net` only. `msjarvis-rebuild_default` bridge has been added for cross-stack connectivity. Both networks are now active for this container.

**Updated `jarvis-consciousness-bridge` services dict (April 14, 2026):**

```python
services = {
    "unified_gateway": "http://jarvis-unified-gateway:8011",
    "neuro_master":    "http://jarvis-neurobiological-master:8018",
    "direct_rag":      "http://jarvis-rag-server:8016",
    "hilbert":         "http://jarvis-hilbert:8010",
    "woah":            "http://jarvis-woah:7012",
    "chroma":          "http://jarvis-chroma:8000",
}
```

All entries confirmed correct. `neuro_master` entry was previously the source of the DNS mis-routing — now resolved.

---

## 19.11 External Access Points and Network Topology (April 14, 2026)

### qualia-net Topology — Confirmed April 14, 2026

| Service | Container name | Internal port | Status |
|:--|:--|:--|:--|
| WOAH stub | `jarvis-woah` | 7012 | ✅ Confirmed |
| ChromaDB | `jarvis-chroma` | 8000 | ✅ Confirmed — 49 collections, 6,722,589+ vectors |
| Consciousness Bridge | `jarvis-consciousness-bridge` | 8018 (actual) | ✅ Confirmed |
| RAG server | `jarvis-rag-server` | 8016 (internal) | ✅ Confirmed — host maps as 8003→8016 |
| Ollama | `jarvis-ollama` | 11434 | ✅ Confirmed |
| Neurobiological Master | `jarvis-neurobiological-master` | 8018 | ✅ Confirmed — DNS fix April 14; /health HTTP 200 |
| AAACPE scraper | `jarvis-aaacpe-scraper` | 8033 (internal) | ✅ Active — host 8048→8033 |
| AAACPE RAG | `jarvis-aaacpe-rag` | 8032 (internal) | ✅ Active — host 8047→8032 |
| I-Containers | `jarvis-i-containers` | 8015 | ✅ Fully operational — dual_awareness: true |

### Host-Exposed Ports (April 14, 2026)

| Port | Service | Notes |
|:--|:--|:--|
| 8443 | Caddy (HTTPS) | Public-facing perimeter; OI-36-A open |
| 8055 | `jarvis_auth_service` | systemd-managed; internal only |
| 8051 | `jarvis-main-brain` (external) | Mapped from internal 8050 |
| 8056 | `jarvis-memory` | Secured; `127.0.0.1`; `_auth()` confirmed |
| 8048 | `jarvis-aaacpe-scraper` | → container 8033; APScheduler |
| 8047 | `jarvis-aaacpe-rag` | → container 8032; appalachian_cultural_intelligence |
| 8015 | `jarvis-i-containers` | `127.0.0.1` binding; fully operational |
| 8020 | `jarvis-autonomous-learner` | Stale ref: 8425 |
| 8003 | `jarvis-rag-server` (external) | Maps to container-internal port 8016 |
| 8002 | `jarvis-chroma` (external) | Maps to container-internal port 8000 |
| 7205 | `gbim_query_router` | Landowner GBIM queries; internal-only hardening pending |
| 11434 | `jarvis-ollama` | Embeddings and LLM inference |
| 5435 | PostgreSQL `msjarvisgis` | `jarvis-local-resources-db`; 45 GB; 515 pub / 742 total tables; authoritative GBIM |
| 5433 | PostgreSQL `jarvis-msjarvis-db` | External volume `msjarvis_pgdata`; offline for live GBIM |
| 6379 | Redis (`jarvis-redis`) | Async job state; idempotency; health cache |
| 8073, 8074, 8075 | EEG band services | — |

---

## 19.12 Async Job Management API

| Endpoint | Method | Function |
|:--|:--|:--|
| `/chat_async` | POST | Create async job — returns `job_id` immediately |
| `/chat_status/{job_id}` | GET | Poll for progress and result |
| `/chat_cancel/{job_id}` | DELETE | Cancel a specific running job |
| `/chat_cancel_all` | DELETE | Cancel all running jobs |

- Job state persists in Redis (`jarvis-redis:6379`) with 30-minute TTL.
- State survives `jarvis-main-brain` container restarts.
- Cancel operations perform true `asyncio.Task` cancellation.
- Idempotency TTL: 1,800s.

---

## 19.13 Verified Reboot Sequence (April 14, 2026)

```bash
# Step 0: Run preflight gate — must pass all 9 checks
bash scripts/preflight_gate.sh
# Validates 64-byte JARVIS_API_KEY file, Chroma collections,
# key collection counts, GBIM entities, jarvis-memory auth

# Step 1: Confirm jarvis_auth_service is running under systemd
systemctl status jarvis-auth-service

# Step 2: Start all compose-managed containers
cd msjarvis-rebuild-working/msjarvis-rebuild
docker compose up -d
# ⚠️ Orphan warning for nbb_* and llm*-proxy is EXPECTED
# DO NOT use --remove-orphans

# Step 3: Start and verify the six pipeline containers
./jarvis_startup.sh
# Go signal: Six green health check marks

# Step 4: Verify qualia-net services
docker exec jarvis-consciousness-bridge \
  python3 -c "import httpx; r=httpx.get('http://jarvis-woah:7012/'); print(r.status_code, r.json())"
# Expected: 200

docker exec jarvis-consciousness-bridge \
  python3 -c "import httpx; r=httpx.get('http://jarvis-neurobiological-master:8018/health'); print(r.status_code)"
# Expected: 200

# Step 5: Verify ChromaDB v2 API and collection count
curl http://127.0.0.1:8002/api/v2/tenants/default_tenant/databases/default_database/collections
# Expected: 49 collections

# Step 6: Verify AAACPE stack
curl http://127.0.0.1:8048/health
curl http://127.0.0.1:8047/health
# Both expected: 200

# Step 7: Verify I-Containers
curl -s http://127.0.0.1:8015/health | python3 -m json.tool
# Expected: status healthy, dual_awareness: true

# Step 8: Verify gbim_query_router
curl -X POST http://127.0.0.1:7205/query \
  -H "Content-Type: application/json" \
  -d '{"query": "corporate landowners Fayette County"}'
# Expected: HTTP 200 OK

# Step 9: Verify jarvis-memory auth boundary
curl http://127.0.0.1:8056/health                                        # 200 (intentionally public)
curl http://127.0.0.1:8056/memory/sessions                               # 401 (protected)
curl -H "Authorization: Bearer $JARVIS_API_KEY" \
  http://127.0.0.1:8056/memory/sessions                                  # 200

# Step 10: Verify rag-server env vars
docker exec jarvis-rag-server env | grep -E "OLLAMA_HOST|EMBED_MODEL|CHROMA_HOST"
# Expected:
# OLLAMA_HOST=http://jarvis-ollama:11434
# EMBED_MODEL=all-minilm:latest
# CHROMA_HOST=http://jarvis-chroma:8000

# Step 11: Verify msjarvisgis live counts
psql -h 127.0.0.1 -p 5435 -U postgres -d msjarvisgis \
  -c "SELECT count(*) AS public_tables FROM pg_tables WHERE schemaname='public';"
# Expected: 515

psql -h 127.0.0.1 -p 5435 -U postgres -d msjarvisgis \
  -c "SELECT pg_size_pretty(pg_database_size('msjarvisgis'));"
# Expected: ~95 GB
```

---

## 19.14 Container Count History

| Date | Container count | Notable addition |
|:--|:--|:--|
| Initial deployment | 70 | Core stack |
| March 13, 2026 | 73 | I-Containers port fix; 3 corpus containers identified missing |
| March 17, 2026 | 79 | 9 missing containers added; Redis async job system; Docker Compose v5.1.0 |
| March 18, 2026 | 79 | Compose audit complete; all build→image for non-judge services |
| March 20, 2026 | 80 | `gbim_query_router` port 7205 — landowner belief layer live |
| March 21, 2026 | 80 | Ghost file remediation; judge scripts restored; `bbb_check_verdict` live |
| March 22, 2026 | 81* | Caddy perimeter (8443) + `jarvis_auth_service` (8055 systemd); `jarvis-crypto-policy` removed |
| March 25, 2026 | 81 | `jarvis-rag-server` port mapping corrected; qualia-net topology confirmed |
| March 28, 2026 | 96 | `jarvis-memory:8056` corrected; `jarvis-ingest-api` + `jarvis-ingest-watcher` restored; ChromaDB full audit: 40 collections, 6,675,442 vectors; 96/96 Up |
| April 1, 2026 | 96 | LEARN-01/02/03 resolved; autonomous learner repaired; `services-safe` synced |
| April 13, 2026 | 109 | ChromaDB upgraded to server 1.0.0 / client 1.5.5; I-Containers fully operational; `memories` table schema complete; `jarvis-msjarvis-db` added to compose; `msjarvis-pgdata-rescue` retired; `preflight_gate.sh` passing all 9 checks; `preserve_memory_uuid.sh` and `restore_memory_uuid.sh` written |
| April 14, 2026 | 109 | `jarvis-aaacpe-scraper` (8048→8033) + `jarvis-aaacpe-rag` (8047→8032) added; APScheduler `run_full_scrape` daily 06:00 UTC + every 6h; `appalachian_cultural_intelligence` at 1,090 docs; AAACPE open item closed; OI-36-C closed — `JARVIS_API_KEY` plaintext bypass removed; consciousness bridge DNS fix; neurobiological master added to `msjarvis-rebuild_default` bridge; 49 ChromaDB collections confirmed |

*81 = 80 Docker-managed + 1 systemd-managed (`jarvis_auth_service`).*

---

*Last updated: 2026-04-14 by Carrie Kidd (Mamma Kidd), Mount Hope WV*

*April 14, 2026: jarvis-aaacpe-scraper (8048→8033) and jarvis-aaacpe-rag (8047→8032) added to compose and port registry (§19.8.7, §19.8.11, §19.11, §19.14). APScheduler run_full_scrape daily 06:00 UTC + every 6h documented (§19.8.11). appalachian_cultural_intelligence at 1,090 docs, last_run_new_docs: 123 (§19.8.10, §19.8.11). AAACPE open item closed — legacy jarvis-ingest-api + jarvis-ingest-watcher path superseded (§19.5, §19.8.7, §19.8.11). ChromaDB collection count updated to 49 throughout (§19.0, §19.1, §19.3, §19.4, §19.8.10). all-minilm:latest (384-dim) confirmed canonical across all 49 collections (§19.8.8a, §19.8.10). OI-36-C closed — JARVIS_API_KEY plaintext bypass permanently removed from msjarvis-unified-gateway.py as of 2026-04-03; gateway reads only from Docker secret secrets/jarvis_api_key.txt; /auth/token bootstrap tokens must be registered in invite store (§19.0, §19.8.2, §19.9). scripts/preflight_gate.sh validates 64-byte key file before compose up (§19.8.0, §19.9, §19.13). jarvis-consciousness-bridge DNS fix — NEUROMASTER_URL confirmed jarvis-neurobiological-master:8018 on qualia-net; /health HTTP 200 confirmed (§19.10, §19.11). jarvis-neurobiological-master added to msjarvis-rebuild_default bridge for cross-stack connectivity (§19.8.7, §19.10). docker-compose.yml finalized April 13, 2026 ~21:31 — stale .bak.* variants are historical artifacts only (§19.0, §19.8). msjarvisgis port corrected to 5435 throughout (all sections). ChromaDB host port corrected to 8002 throughout (§19.8.10, §19.11, §19.12, §19.13). msjarvisgis live counts updated — 515 public tables, 742 total tables, 45 GB, 5,415,896 gbim_worldview_entity rows (§19.0, §19.8.10). jarvis-msjarvis-db added to compose; msjarvis-pgdata-rescue retired (§19.8.10). memories table schema complete — 6 columns, 4 indexes (§19.0, §19.8.10). I-Containers confirmed fully operational port 8015, dual_awareness: true — future-work language removed (§19.8.7, §19.11). BBB /check endpoint reference removed; /filter, /truth, /stats, /filter_output confirmed (§19.8.4). jarvis-memory /events reference removed; full confirmed API surface documented (§19.8.4). UltimateResponse canonical schema noted — truthverdict present but nullable; top-level fields confirmed (see Ch. 20 §20.3). ms_jarvis_memory UUID preservation risk documented (§19.8.10). Chroma v2 API canonical — /api/v1/ permanently removed (§19.8.10, §19.13). All hard-coded March 28 table/size counts replaced with live April 13/14 values or preflight gate references.*
