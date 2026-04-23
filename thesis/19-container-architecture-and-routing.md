# Chapter 19 — Container Architecture and Routing

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*

*Last updated: April 23, 2026 — container count → 100; ChromaDB → 48 collections /
~6,740,611 vectors; two-container DB split applied throughout: production `msallis-db`
host **5433** (16 GB / 294 tables / 11 schemas); forensic `postgis-forensic` host
**5452** (17 GB / 314 tables / 9 schemas); end-to-end benchmark → **102.58s**;
`autonomous_learner` → **~23,200+** records; OI-36-A CLOSED (auth enforcement
active); §19.13 stale ~95 GB expected value removed; §19.14 April 16 and April 23
rows added; `local_resources` → 207 docs (Ch.17 April 16 baseline); all
`msallisgis:5435 / 45 GB / 515 pub / 742 total` references superseded by two-container
split.*

> **April 23, 2026 UPDATE ★:** Container count → **100 Up** (zero Restarting, zero
> Exited). ChromaDB → **48 active collections, ~6,740,611 vectors** (host port 8002).
> `autonomous_learner` → **~23,200+** records (grown ≈288/day since April 14 baseline
> of 21,181). GPU pipeline → **102.58s** (RTX 4070). Two-container DB split:
> **Production** `msallis-db` host **5433** / container **5432** — `msallisgis`
> **16 GB / 294 tables / 11 schemas** — all production GIS and RAG queries.
> **Forensic** `postgis-forensic` host **5452** — `msallisgis` **17 GB / 314 tables /
> 9 schemas** — forensic auditing only. **OI-36-A CLOSED** — April 23, 2026: Caddy
> `forward_auth` token enforcement is now active at proxy level.
> `conversation_history` wiped and reseeded clean April 16 — count reflects
> post-wipe accumulation only. §19.14 history rows for April 16 and April 23 added.

> **April 14, 2026 update (historical baseline):** 109 running containers confirmed.
> Two new dedicated AAACPE services added: `allis-aaacpe-scraper` (host 8048 →
> container 8033) and `allis-aaacpe-rag` (host 8047 → container 8032). APScheduler
> `run_full_scrape` runs daily at 06:00 UTC and every 6 hours.
> `appalachian_cultural_intelligence` at 1,090 docs. ChromaDB at 49 named collections
> (corrected to 48 as of April 23). `ALLIS_API_KEY` plaintext bypass permanently
> removed as of 2026-04-03. `allis-consciousness-bridge` DNS fix confirmed.
> `allis-neurobiological-master` added to `msallis-rebuild_default` bridge.
> `docker-compose.yml` finalized April 13, 2026 ~21:31. `scripts/preflight_gate.sh`
> validates 64-byte key file before any compose up.

---

## Why This Matters for Polymathmatic Geography

This chapter explains how Ms. Allis's containers receive, sort, and route the flows
of experience that later become memory and decision support. It supports:

- **P1 – Every where is entangled** by treating events from people, places, and
  institutions as a shared stream that must be carefully routed into production
  `msallis-db` (host **5433** ★, 16 GB / 294 tables, 993 ZCTA centroids) and ChromaDB
  memory (**48 collections, ~6,740,611 vectors** ★).
- **P3 – Power has a geometry** by making explicit which services, ports, and stores
  stand between community data and long-term inference, and by naming
  `gbim_query_router` (port 7205) as the service that makes corporate and government
  land ownership queryable by natural language for the first time.
- **P5 – Design is a geographic act** by encoding how Appalachian events move through
  Ms. Allis and into PostgreSQL spatial, semantic, and commons-oriented stores, and
  by treating the routing decision to bypass ChromaDB entirely for landowner queries
  as an explicit architectural choice with geographic and ethical consequences.
- **P12 – Intelligence with a ZIP code** by prioritizing spatial, governance, and
  commons contexts in the way container records are tagged and stored, and by
  recognizing `gbim_query_router` as the service that closes the `who` axis at
  parcel scale. As of April 23, 2026: **100 containers** ★, **48 ChromaDB
  collections** ★, **~6,740,611 total vectors** ★, and a fully operational dedicated
  AAACPE intelligence pipeline — all running on a single Lenovo Legion 5 in Oak
  Hill, West Virginia.
- **P16 – Power accountable to place** by using auditable container flows and
  verification scripts so communities can see where their data goes, and by ensuring
  that corporate and government landholdings are queryable with full assessor
  provenance through `gbim_query_router`.

As such, this chapter belongs to the **Computational Instrument** tier — it describes
the container and routing structures that turn raw events into traceable, place-aware
memory anchored in PostgreSQL.

---

## 19.0 Production State (April 23, 2026 ★)

| Property | Value |
|:--|:--|
| Total containers | **100** ★ (compose-managed + `allis_auth_service` systemd-managed) |
| Compose file | `msallis-rebuild-working/msallis-rebuild/docker-compose.yml` — finalized April 13, 2026 ~21:31 |
| Docker Compose version | v5.1.0 |
| Build directives | Converted to image references for non-judge services — no rebuilds on startup |
| Judge services | Real source files confirmed in `services/` — `--no-cache` rebuild March 22, 2026 |
| Caddy perimeter layer | Port 8443 public-facing — **OI-36-A CLOSED** April 23, 2026 ★ — auth enforcement active |
| `allis_auth_service` | Port 8055, systemd-managed (not Docker-managed) |
| `gbim_query_router` | Port 7205 — HTTP 200 OK stable |
| **Production DB** | `msallis-db` host **5433** ★ — `msallisgis` **16 GB / 294 tables / 11 schemas** |
| **Forensic DB** | `postgis-forensic` host **5452** ★ — `msallisgis` **17 GB / 314 tables / 9 schemas** |
| GBIM corpus (production `msallis-db:5433`) | `gbim_worldview_entity` — verify current; `gbim_graph_edges` — verify current; `gbimbeliefnormalized` — verify current |
| `mvw_gbim_landowner_spatial` | 20,593 landowner beliefs — materialized and spatially indexed |
| ChromaDB | **48 active collections, ~6,740,611 total vectors** ★ (April 23) |
| `appalachian_cultural_intelligence` | Verify current — served by `allis-aaacpe-rag:8047→8032` |
| `spiritual_texts` | 79,181 vectors (primary spiritual corpus) |
| `psychological_rag` | 968 docs (stable since March 28 restoration) |
| `msallis_docs` | Verify current count |
| `ms_allis_memory` | Verify current count — UUID `79240788-0828-45f3-b1bc-a9a3593628a6` confirmed |
| `autonomous_learner` | **~23,200+** ★ records (grown ≈288/day since 21,181 baseline April 14) |
| `local_resources` | **207 docs** ★ (Ch.17 April 16 baseline — verify current) |
| `conversation_history` | Wiped and reseeded clean April 16 ★ — count reflects post-wipe accumulation only |
| Autonomous learner | LEARN-01/02/03 resolved April 1, 2026; dedup gate clean; semantic dedup audit pending |
| `allis-memory` | Port 8056 — `127.0.0.1`; `_auth()` confirmed on 4 sensitive routes; `ALLIS_API_KEY` set |
| AAACPE pipeline | **Dedicated stack** — `allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`; APScheduler `run_full_scrape` daily 06:00 UTC + every 6h |
| Auth security | `ALLIS_API_KEY` plaintext bypass permanently removed from `msallis-unified-gateway.py` as of 2026-04-03; gateway reads only from Docker secret `secrets/allis_api_key.txt` |
| OI-36-A | **CLOSED** April 23, 2026 ★ — Caddy `forward_auth` token enforcement active |
| OI-36-C | CLOSED April 3, 2026 — `ALLIS_API_KEY` plaintext bypass removed |
| Consciousness bridge DNS | `NEUROMASTER_URL` confirmed — `allis-neurobiological-master:8018` on `qualia-net`; `/health` HTTP 200 confirmed |
| Neurobiological master network | On both `qualia-net` and `msallis-rebuild_default` bridge |
| I-Containers | **Fully operational** — port 8015; 10 neurobiological modules; `dual_awareness: true` |
| `memories` table schema | 6 columns, 4 indexes applied to production `msallis-db:5433` |
| preflight gate | `scripts/preflight_gate.sh` — validates 64-byte key file + all system checks before compose up |
| End-to-end benchmark | **102.58s** ★ (GPU RTX 4070 — was 436s / 532s CPU baseline) |
| `services-safe/` sync | `ms_allis_autonomous_learner_optimized.py` and `ms_allis_rag_server.py` synced April 1, 2026 |

---

## 19.1 Position in the Overall System

The container layer sits between external interfaces and the lower-level retrieval,
optimization, and global control mechanisms. It is visible both in the `main-brain`
service that handles `/chat` and `/chat_async` requests and in the autonomous learning
and Fifth DGM pipelines that generate and refine internal content.

Its main responsibilities are to:

- Accept events coming from many sources, including question-handling flows, scheduled
  jobs, and self-improving processes.
- Normalize these events into a common format that can be evaluated and stored
  consistently in production `msallis-db` (host **5433** ★, 16 GB / 294 tables) and
  ChromaDB (**48 collections, ~6,740,611 vectors** ★).
- Dispatch normalized items into successive evaluation stages, while obeying
  system-wide constraints such as safety filters (BBB 6-filter stack with fail-closed
  behavior ★), resource limits, and service health (30s TTL cache, 2s timeout per
  service).

As of April 23, 2026, all external `/chat*` traffic passes through the Caddy perimeter
layer (port 8443) and `allis_auth_service` (port 8055) before reaching any container.
**OI-36-A is CLOSED** ★ — Caddy `forward_auth` token enforcement is active at the
proxy level. OI-36-C is closed: `ALLIS_API_KEY` plaintext bypass permanently removed
from `msallis-unified-gateway.py` as of 2026-04-03.

---

## 19.2 Types of Incoming Events

The intake layer receives several broad categories of events:

- **Direct interactions** — User queries and responses that have already passed through
  Caddy authentication (Tier 1, now enforced ★) and then `bbb-input-filter` (Tier 2).
  These include synchronous requests and asynchronous jobs tracked via job IDs
  persisted in Redis (`allis-redis:6379`, 30-minute TTL).
- **Internal tasks** — Results from scheduled analyses, background maintenance jobs,
  and optimization routines: autonomous learner outputs (**~23,200+** records as of
  April 23 ★, ≈288/day — LEARN-01/02/03 resolved), Fifth DGM optimization steps, and
  WOAH evaluations.
- **External signals** — Notifications or status changes from connected systems. The
  dedicated AAACPE stack (`allis-aaacpe-scraper` + `allis-aaacpe-rag`, operational
  April 14, 2026) is the primary operational external-signal ingest pathway. It
  supersedes the legacy `allis-ingest-api` + `allis-ingest-watcher` path for
  Appalachian cultural intelligence data.
- **Structural changes** — Updates to production `msallis-db` memory (host **5433** ★,
  16 GB / 294 tables), GBIM belief graphs, or spatial layers that may require special
  attention. The March 20, 2026 ingestion of 20,593 landowner belief records and the
  April 13 `memories` table schema completion (6 columns, 4 indexes) are examples.

---

## 19.3 Normalization into Container Records

Before events are passed to deeper stages, they are normalized into container records
with a common structure:

- **Core fields** — Unique identifier, creation and update timestamps, origin (e.g.,
  `user_chat`, `autonomous_learner`, `aaacpe_ingest`, `gbim_landowner_update`, or
  `external_signal`), and a reference to the initiating service or job.
- **Context** — Active role or profile, relevant geographic or institutional context
  from production `msallis-db` (host **5433** ★, 16 GB / 294 tables), and tags
  describing the domain (`governance`, `infrastructure`, `landowner`,
  `community_culture`). For chat records, this includes `user_id` and any declared
  `mode`. For async jobs, the Redis-persisted `job_id` links the normalized record to
  its lifecycle state.
- **Content summary** — Key text, numerical values, or structured data extracted from
  the event. For landowner queries, this includes the routing decision
  (`mode: landowner_gbim`, `route_type: parcel_ownership`) and the SQL aggregation
  result from `mvw_gbim_landowner_spatial`.
- **Links** — References to memory items (ChromaDB embeddings — **48 collections,
  ~6,740,611 vectors** ★, all 384-dim via `all-minilm:latest`), PostgreSQL GBIM
  graph nodes/edges at production `msallis-db:5433` ★, relational records, spatial
  features, and introspective entries. BBB audit trail links route to
  `allis-memory:8056` (secured). `memories` table cross-references route to
  production `msallis-db:5433` ★ via `gbim_entity_id` and `spatial_ref`.
- **Control information** — Flags indicating initial assessments (urgency, sensitivity,
  safety status, BBB-approved or denied with **fail-closed** behavior ★, expected
  resource cost, and whether the item is considered high-value for long-term retention).

---

## 19.4 First-Level Routing Decisions

Once a record is normalized, the intake layer applies initial routing logic:

- **Eligibility checks** — Safety checks (BBB 6-filter stack ★ with `truth_score`
  null guard and **fail-closed** on all failure paths ★), role-based constraints, and
  service availability via health probes (30s TTL cache, 2s timeout per service).
  `scripts/preflight_gate.sh` must pass all checks before any compose up.
- **Phase 1.45 community memory injection** — After BBB input approval, the main
  brain generates a 384-dim embedding via `all-minilm:latest` at
  `allis-ollama:11434/api/embeddings`, queries the `autonomous_learner` ChromaDB
  collection (**~23,200+** records ★), retrieves the 5 most semantically similar
  community interaction records, and prepends them to `enhanced_message` before it
  reaches the 21 active LLMs.
- **Priority assignment** — Assigning a simple priority or track indicator that
  influences ordering and resource allocation.
- **Track assignment** — Deciding whether the record should be sent to specific
  container subsystems (I-Container service port 8015, psychological RAG domains via
  `psychological_rag` 968 docs, production GBIM graph updates at `msallis-db:5433` ★,
  `gbim_query_router` landowner path — HTTP 200 OK stable — or audit logs persisted
  to `allis-memory:8056`).

---

## 19.5 Parallel Paths

The architecture supports multiple parallel paths that share a common structural
pattern (intake → normalization → gating → storage in PostgreSQL or ChromaDB or
discard):

- **Affective and care-oriented paths** — Used when events are framed in terms of
  meaning, care, or psychological support. These involve specialized RAG domains
  (`psychological_rag` 968 docs, stable), therapeutic or community-oriented analysis,
  and services that emphasize ethical interpretation and human impact.
- **Analytical and technical paths** — Used for infrastructure planning (production
  `msallis-db` host **5433** ★), spatial reasoning, optimization over data, and
  structured ownership queries via `gbim_query_router`. These paths emphasize
  quantitative reasoning, model-based analysis, and technical verification against
  production GBIM ground truth.
- **Deterministic relational retrieval path** — The `gbim_query_router` landowner
  path. It does not involve LLM reasoning, ChromaDB vector search, or web research.
  It is the system's only fully deterministic query path. HTTP 200 OK stable.
- **Dedicated AAACPE intelligence path (operational April 14, 2026)** — The
  `allis-aaacpe-scraper` (port 8048→8033) + `allis-aaacpe-rag` (port 8047→8032)
  stack. APScheduler triggers `run_full_scrape` daily at 06:00 UTC and every 6 hours.
  Scraped documents are embedded with `all-minilm:latest` and written to the
  `appalachian_cultural_intelligence` ChromaDB collection. This path supersedes the
  legacy `allis-ingest-api` + `allis-ingest-watcher` path. See §19.8.11 for full
  specification.
- **Autonomous learning path** — `allis-autonomous-learner` stores findings every
  5 minutes into `autonomous_learner` ChromaDB collection (**~23,200+** ★).
  LEARN-01/02/03 resolved April 1, 2026. Dedup gate running cleanly.
  ⚠️ Semantic dedup audit pending.

---

## 19.6 Outputs of the Routing Layer

After routing, the container layer produces:

- **Records marked for immediate evaluation** — Items that pass eligibility checks
  and have sufficient priority are forwarded to downstream evaluators (21-model LLM
  consensus, truth validators, or `gbim_query_router` SQL aggregation). Their
  container records carry all necessary context and links to production PostgreSQL
  tables at `msallis-db:5433` ★.
- **Records held back or dropped** — Events may be queued, delayed, rate-limited, or
  dropped entirely based on policy.
- **Introspective logs and verification entries** — The system records which paths
  were chosen, which services were invoked, what PostgreSQL queries were executed, and
  what the outcomes were. BBB audit events persist to `allis-memory:8056` (secured
  `127.0.0.1`, `_auth()` confirmed, `ALLIS_API_KEY` set). Promotion events are
  tracked in the `memories` table in production `msallis-db:5433` ★ via `reviewed`
  and `promoted` columns.

---

## 19.7 Conceptual Summary

The container architecture provides a structured way to receive, normalize, and direct
events into deeper evaluative paths anchored in production `msallis-db` (host
**5433** ★, 16 GB / 294 tables). It defines how diverse inputs — user interactions,
internal learning results, dedicated AAACPE scraper documents, and structural changes —
enter the system's evaluative core.

The remaining sections ground this abstraction in the current production deployment
topology, focusing on Docker containers, port mappings, compose management, and
service roles as of **April 23, 2026** ★.

---

## 19.8 Operational Container Topology (April 23, 2026 ★)

This section is the authoritative operational state as of April 23, 2026 ★. The
topology is derived from `msallis-rebuild-working/msallis-rebuild/docker-compose.yml`
(finalized April 13, 2026 ~21:31, Docker Compose v5.1.0), runtime `docker ps` output,
`allis_startup.sh`, and verification scripts.

**Compose management baseline — April 23, 2026:**

- All **100** ★ Docker-managed production containers are defined in the canonical
  `docker-compose.yml` — zero Restarting, zero Exited.
- `allis_auth_service` (port 8055) is systemd-managed, not Docker-managed — see
  §19.8.2.
- `gbim_query_router` (port 7205) — HTTP 200 OK stable.
- `allis-memory` (port 8056) — confirmed `127.0.0.1`; `_auth()` confirmed;
  `ALLIS_API_KEY` set.
- `allis-aaacpe-scraper` (8048→8033) and `allis-aaacpe-rag` (8047→8032) — active
  compose inventory; APScheduler `run_full_scrape` daily 06:00 UTC + every 6h.
- Legacy `allis-ingest-api` and `allis-ingest-watcher` — superseded by dedicated
  AAACPE stack. Status in compose: historical reference only.
- `ALLIS_API_KEY` plaintext bypass removed from `msallis-unified-gateway.py` as of
  2026-04-03 (OI-36-C closed).
- **OI-36-A CLOSED** ★ — Caddy `forward_auth` token enforcement now active.
- `scripts/preflight_gate.sh` validates 64-byte key file and all system checks — must
  pass before every `docker compose up`.
- Stale `.bak.*` compose variants in working directory are historical artifacts — do
  not use.
- All build directives remain converted to image references for non-judge services.
- Judge service images were rebuilt with `--no-cache` on March 22, 2026.
- Reboot sequence: `scripts/preflight_gate.sh` (must pass) → `docker compose up -d`
  → `allis_startup.sh`.

---

### 19.8.0 Orphaned Container Warning — Expected Behavior

> **⚠️ Documented March 25, 2026:** Running `docker compose up -d` from the
> `msallis-rebuild` project directory will produce a warning similar to:

```
WARN Found orphan containers (nbb_woah_algorithms, nbb_i_containers,
llm1-proxy, llm2-proxy, ... llm22-proxy) for this project.
If you removed or renamed this service in your compose file, you can run
this command with the --remove-orphans flag to clean it up.
```

**This is expected behavior.** The `nbb_*` containers and `llm*-proxy` containers are
managed by a **separate compose file** in a different project directory.

> **⚠️ CRITICAL: Do NOT use `--remove-orphans`** unless you are intentionally
> decommissioning the NBB stack and all LLM proxy containers. Using
> `--remove-orphans` will stop and remove all `nbb_*` and `llm*-proxy` containers,
> taking down the NBB prefrontal stack (Chapter 12, §12.12), the WOAH algorithms
> service (Chapter 10), and all 22 LLM proxy containers (§19.8.9).

**Safe reboot procedure:**

```bash
# Step 0: Run preflight gate — must pass all checks
bash scripts/preflight_gate.sh

# Step 1: CORRECT — never use --remove-orphans
cd msallis-rebuild-working/msallis-rebuild
docker compose up -d
# Orphan warning will appear — expected and harmless

# WRONG — will decommission NBB stack and LLM proxies
# docker compose up -d --remove-orphans  ← DO NOT USE
```

---

### 19.8.1 Caddy Perimeter Layer

The Caddy reverse proxy is the outermost layer of the routing stack. **OI-36-A is
CLOSED** ★ — auth enforcement is now active at the Caddy perimeter level.

```
┌──────────────────────────────────────────────────────────────────┐
│ Caddy Perimeter Layer — April 23, 2026 ★                        │
├──────────────────────────────────────────────────────────────────┤
│ Port: 8443 (public-facing, HTTPS)                               │
│ Log path: /var/log/caddy/allis_redteam.log                      │
│                                                                  │
│ Route: /chat*                                                    │
│   → 127.0.0.1:8050 (unified gateway)                            │
│   ✅ forward_auth token enforcement ACTIVE (OI-36-A CLOSED ★)   │
│                                                                  │
│ Route: /auth*, /feedback*, /chat/status*                        │
│   → 127.0.0.1:8055 (allis_auth_service)                         │
│                                                                  │
│ Route: /health*, /systems*                                       │
│   → 127.0.0.1:8050 (unified gateway)                            │
│                                                                  │
│ allis-memory:8056 — localhost-bound only, NOT routed through    │
│ Caddy. _auth() confirmed, ALLIS_API_KEY set.                    │
└──────────────────────────────────────────────────────────────────┘
```

---

### 19.8.2 `allis_auth_service` — Port 8055

`allis_auth_service` is the authentication enforcement service. It is
systemd-managed, not Docker-managed, and runs on port 8055 at all times including
during `docker compose down` operations. See Chapter 16, §16.3.2 for full
specification.

| Property | Value |
|:--|:--|
| Port | 8055 |
| Management | systemd (not Docker Compose) |
| Source file | `scripts/allisauthservice.py` |
| Primary endpoint | `POST /auth/token` |
| Secondary endpoint | `GET /health` |
| Token contract | Bootstrap token from `secrets/allis_api_key.txt` — tokens must be registered in the auth service's invite store (OI-36-C closure) |

`allis-memory` (port 8056) is the BBB audit trail store — distinct from
`allis_auth_service`. Docker-managed. Secured March 28, 2026.

---

### 19.8.3 Core Orchestration Layer

```
Container                Port Mapping    Role
─────────────────────────────────────────────────────────────────────
allis-main-brain         8051→8050       External API entry point:
                                         /chat, /chat_async — 30s TTL
                                         health-check cache, Phase 1.45
                                         community memory retrieval
                                         (~23,200+ autonomous_learner
                                         records ★), service
                                         orchestration,
                                         Redis-backed async job mgmt,
                                         RAG queueing to ChromaDB
                                         (48 collections ★,
                                         ~6,740,611 vectors ★)
                                         backed by production
                                         msallis-db host 5433 ★;
                                         routes mode:landowner_gbim
                                         queries to gbim_query_router;
                                         GPU pipeline: 102.58s ★
```

The `allis-main-brain` container hosts the Ms. Allis ULTIMATE main-brain FastAPI
application. It exposes `/health`, `/chat`, `/chat_async`, `/chat_status/{job_id}`,
`/chat_cancel/{job_id}`, and `/chat_cancel_all` endpoints. Health checks use a 30s
TTL cache with 2s per-service timeout. Async job state persists in Redis with
30-minute TTL and survives container restarts.

---

### 19.8.4 Blood-Brain Barrier and Safety Services

> **⚠️ BBB container architecture:** There is **one** BBB container:
> `allis-blood-brain-barrier` at **port 8016** with **6 filters** ★ (was 7 — corrected
> April 16, 2026), all **fail-closed** ★ (exception defaults → `passed=False`, Ch.16).
> Port 8017 (`bbb-output-filter`) does **not exist** as a separate container. Both
> input filtering (Phase 1.4) and output filtering (Phase 4.5) are handled by the
> single service at port 8016. See Chapter 16 for full specification.

**Confirmed BBB API surface:**

| Endpoint | Purpose |
|---|---|
| `/` | Service identity and active filter list |
| `/health` | Health check |
| `/filter` | Primary first-stage filter |
| `/truth` | Truth assessment |
| `/stats` | Aggregate filter statistics |
| `/filter_output` | Output-stage filtering |

There is no `/check` endpoint. Any prior script or documentation referencing `/check`
on port 8016 is stale.

```
Container                Port Mapping    Role
─────────────────────────────────────────────────────────────────────
allis-blood-brain-       8016→8016       Single BBB container.
barrier                                  6 filters ★ (corrected from 7
                                         April 16, 2026).
                                         ALL fail-closed ★ (Ch.16):
                                         exception defaults →
                                         passed=False.
                                         Phase 1.4: constitutional
                                         input filter (BLOCKING) —
                                         /filter and /truth endpoints.
                                         Phase 4.5: output filter
                                         (BBB_OUTPUT_BLOCKING=true ★) —
                                         /filter_output endpoint.
                                         Verdict → allis-memory:8056

allis-memory             8056→8056       BBB audit trail persistence.
                                         Secured: 127.0.0.1
                                         _auth() confirmed on 4 routes
                                         ALLIS_API_KEY set
                                         /health public; /memory/*
                                         protected
                                         Full API: /memory/turn,
                                         /memory/get, /memory/sessions,
                                         /memory/session/{id},
                                         /memory/quest, /memory/quests,
                                         /memory/consolidate,
                                         /memory/episodic,
                                         /steg_report, /pia_window
                                         No /events endpoint — stale ref.

allis-bbb-ethics-proxy  —               Ethics routing shim
```

---

### 19.8.5 LLM Ensemble and Synthesis

```
Container                Port Mapping    Role
─────────────────────────────────────────────────────────────────────
allis-20llm-production   8008→8008       22-proxy LLM ensemble
                                         (22 registered; 21 active;
                                         BakLLaVA eliminated;
                                         StarCoder2 excluded from
                                         scoring)

allis-llm22-proxy        8030→8030       Semaphore proxy for
(semaphore)                              allis-20llm-production;
                                         max_tokens: -1, unlimited
                                         output

allis-lm-synthesizer     8001 internal   LM Synthesizer — calls
                                         allis-ollama:11434/api/
                                         generate with llama3.1:latest;
                                         Ms. Allis persona prompt
                                         merged; Phase 3.5 / 3.75
                                         single pass

allis-web-research       8009→8009       External knowledge retrieval;
                                         excluded for landowner_gbim
                                         mode
```

---

### 19.8.6 Judge Pipeline (compose-managed, all ports bound to 127.0.0.1)

```
Container                  Int. Port  Source File                    Role
───────────────────────────────────────────────────────────────────────────
allis-judge-pipeline       7239       services/judgepipeline.py      Coordinator;
                                                                      POST /evaluate;
                                                                      asyncio.gather
                                                                      aggregation;
                                                                      bbb_check_verdict
                                                                      live httpx POST

allis-judge-truth          7230       services/judgetruthfilter.py   Truth eval;
                                                                      rag_grounded_v2
                                                                      ACTIVE ★ (was
                                                                      heuristic_
                                                                      contradiction_v1
                                                                      — REMOVED
                                                                      April 6, 2026;
                                                                      OI-37-C closed)

allis-judge-consistency    7231       services/judgeconsistency       Internal
                                      engine.py                       coherence;
                                                                      contradiction
                                                                      detection;
                                                                      llm_judge_v3
                                                                      ACTIVE ★

allis-judge-alignment      7232       services/judgealignment         Ms. Allis
                                      filter.py                       identity
                                                                      adherence;
                                                                      community values

allis-judge-ethics         7233       services/judgeethics            Harm screening;
                                      filter.py                       spiritual
                                                                      appropriateness

allis-69dgm-bridge         9000       —                               69-DGM cascade;
                                                                      23-connector
                                                                      3-stage; validates
                                                                      every production
                                                                      response
```

All five judge containers are compose-managed with `restart: unless-stopped`. ML-DSA-65
signing: FULLY ACTIVE — `sprint1_activate_signing.py` ran 19 PASS, 0 FAIL on
March 22, 2026. `rag_grounded_v2` + `llm_judge_v3` active ★ (OI-37-C closed April 6,
2026).

---

### 19.8.7 Memory, Learning, and Optimization Services

```
Container                  Port Mapping   Role
───────────────────────────────────────────────────────────────────
allis-autonomous-learner   8053→8053      Autonomous learning.
                                          LEARN-01/02/03 RESOLVED
                                          April 1, 2026.
                                          ~23,200+ records ★
                                          (≈288/day from 21,181
                                          April 14 baseline).
                                          Canonical collection name:
                                          autonomous_learner
                                          (underscore, ending "er").
                                          autonomous_learning (17,707)
                                          status unconfirmed.
                                          autonomouslearner (no
                                          underscore) is stale.
                                          ⚠️ Semantic dedup audit
                                          pending

allis-i-containers         8015→8015      FULLY OPERATIONAL.
                                          ms_allis_i_containers_
                                          service.py
                                          10 neurobiological modules —
                                          I-Container 1: SelfRecognition,
                                          IdentityCore,
                                          PersonalNarrative,
                                          EgoBoundaries, MemorySelf;
                                          I-Container 2:
                                          WitnessConsciousness,
                                          ReflectionSystem,
                                          IntrospectionEngine,
                                          MetacognitiveAwareness,
                                          ObserverSelf.
                                          dual_awareness: true.
                                          127.0.0.1:8015->8015/tcp

allis-fifth-dgm            4002→4002      Darwin-Gödel-style
                                          optimization and filtering

allis-neurobiological-     8018→8018      Higher-level coordination.
master                                    On both qualia-net AND
                                          msallis-rebuild_default
                                          bridge.
                                          DNS: NEUROMASTER_URL =
                                          allis-neurobiological-
                                          master:8018 on qualia-net.
                                          /health HTTP 200 confirmed.

allis-hippocampus          8011→8011      Hippocampal consolidation;
                                          GBIM beliefs → ChromaDB
                                          (48 collections ★,
                                          ~6,740,611 vectors ★)
                                          pipeline

allis-memory               8056→8056      BBB audit trail persistence.
                                          Secured. 127.0.0.1.
                                          See §19.8.4 for full API.

allis-aaacpe-scraper       8048→8033      AAACPE dedicated scraper.
                                          APScheduler: run_full_scrape
                                          daily 06:00 UTC + every 6h.
                                          Feeds allis-aaacpe-rag.
                                          Supersedes allis-ingest-api
                                          + allis-ingest-watcher for
                                          Appalachian cultural data.

allis-aaacpe-rag           8047→8032      AAACPE dedicated RAG service.
                                          Serves appalachian_cultural_
                                          intelligence collection.
                                          Verify current doc count ★.
                                          EMBED_MODEL: all-minilm:latest
                                          (384-dim).
```

---

### 19.8.8 RAG Domain Services

```
Container                  Port Mapping   Role
───────────────────────────────────────────────────────────────────
allis-rag-server           8003→8016      Text RAG — direct_rag path.
                                          ⚠ Host 8003 maps to container-
                                          internal uvicorn listener on
                                          port 8016. Mapping is
                                          127.0.0.1:8003:8016.
                                          See §19.8.8a for required
                                          env vars.

allis-gis-rag              8004→8004      GIS spatial RAG queries;
                                          geospatialfeatures;
                                          production msallis-db
                                          host 5433 ★

allis-spiritual-rag        8005→8005      Spiritual/cultural RAG.
                                          Note: spiritual_rag as a
                                          single collection does not
                                          exist. Corpus is split:
                                          spiritual_texts (79,181) —
                                          primary; spiritual_wisdom
                                          (135); spiritual_knowledge
                                          (12).

allis-psychology-services  8019→8019      Psychological safety services;
                                          Phase 3 pre-assessment

psychological-rag-domain   8006→8006      Psychological RAG domain;
                                          psychological_rag collection —
                                          968 docs, stable since
                                          March 28 restoration

gbim_query_router          7205→7205      GBIM landowner belief query
                                          router. PostgreSQL-native ONLY.
                                          HTTP 200 OK stable.
                                          Queries mvw_gbim_landowner_
                                          spatial in production
                                          msallis-db:5433 ★
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

### 19.8.8a `allis-rag-server` — Port Correction and Required Environment Variables

> **⚠️ Critical port correction (March 25, 2026):** The `allis-rag-server`
> docker-compose port mapping is `127.0.0.1:8003:8016`. Host port 8003 maps to
> container-internal uvicorn listener on port 8016. All host-side calls use port 8003;
> all container-internal references must use `allis-rag-server:8016`.

```yaml
allis-rag-server:
  image: python:3.11-slim
  container_name: allis-rag-server
  ports:
    - "127.0.0.1:8003:8016"
  environment:
    - OLLAMA_HOST=http://allis-ollama:11434
    - EMBED_MODEL=all-minilm:latest
    - CHROMA_HOST=http://allis-chroma:8000
  networks:
    - qualia-net
```

| Variable | Correct value | Consequence of missing |
|:--|:--|:--|
| `OLLAMA_HOST` | `http://allis-ollama:11434` | All embedding calls fail |
| `EMBED_MODEL` | `all-minilm:latest` | Embedding calls fail — wrong model |
| `CHROMA_HOST` | `http://allis-chroma:8000` | ChromaDB connections fail |

> **⚠️ EMBED_MODEL — canonical value is `all-minilm:latest` (384-dim) across all
> 48 collections ★ (~6,740,611 vectors ★).** Any compose file entry showing
> `EMBED_MODEL=nomic-embed-text` must be corrected before the next restart —
> `nomic-embed-text` produces 768-dim vectors and is incompatible with all existing
> collections.

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

> **⚠️ Orphaned container warning:** All `llm*-proxy` containers are managed by a
> separate compose file. Running `docker compose up -d` from the `msallis-rebuild`
> directory will produce orphan warnings. This is expected. Do NOT use
> `--remove-orphans`. See §19.8.0.

21 models reliably active; BakLLaVA permanently eliminated; StarCoder2 excluded from
scoring. `gbim_query_router` landowner queries do not pass through the LLM ensemble.

---

### 19.8.10 Data Persistence and Semantics

```
Container                  Port Mapping   Role
───────────────────────────────────────────────────────────────────
allis-chroma               8002→8000      Canonical ChromaDB instance.
                                          Host port 8002 (NOT 8000).
                                          chromadata volume at
                                          /home/ms-allis/msallis-rebuild/
                                          persistent/chroma → /data
                                          (authoritative SQLite backup
                                          source).
                                          384-dim all-minilm:latest.
                                          On qualia-net.
                                          Chroma server 1.0.0 /
                                          client chromadb==1.5.5.
                                          /api/v2/ only — /api/v1/
                                          permanently removed.
                                          48 active collections ★,
                                          ~6,740,611 total vectors ★.
                                          LANDOWNER BELIEFS NOT STORED
                                          HERE.

msallis-db                 5433→5432      PRODUCTION PostgreSQL 16 +
(production) ★                           PostGIS.
                                          16 GB ★. 294 tables ★.
                                          11 schemas ★.
                                          993 ZCTA centroids.
                                          gbim_worldview_entity:
                                          verify current.
                                          gbim_graph_edges: verify.
                                          gbimbeliefnormalized: verify.
                                          mvw_gbim_landowner_spatial:
                                          20,593 rows.
                                          memories table: 6 columns,
                                          4 indexes.
                                          building_parcel_county_tax_mv:
                                          verify current.
                                          ALL PRODUCTION GIS AND RAG
                                          QUERIES USE THIS INSTANCE.

postgis-forensic           5452→5432      FORENSIC PostgreSQL 16 +
(forensic) ★                             PostGIS.
                                          17 GB ★. 314 tables ★.
                                          9 schemas ★.
                                          FORENSIC AUDITING ONLY —
                                          not used for live GBIM ops.

allis-redis                6379→6379      Redis; async job state,
                                          30-min TTL; idempotency
                                          TTL 1,800s; health cache

allis-ollama               11434→11434    Ollama LLM backend;
                                          all-minilm:latest 384-dim
                                          embeddings; llama3.1:latest
                                          LM Synthesizer; all 22 model
                                          proxies. On qualia-net.

allis-memory               8056→8056      BBB audit trail persistence.
                                          Secured March 28, 2026.
                                          See §19.8.4 for full API.
```

**Canonical ChromaDB collections — April 23, 2026 ★ (all 384-dim via
`all-minilm:latest`):**

| Collection | Records | Notes |
|:--|:--|:--|
| `gbim_worldview_entities` | verify current | Complete WV GBIM spatial corpus |
| `address_points` | 1,115,588 | — |
| `spiritual_texts` | 79,181 | Primary spiritual corpus |
| `autonomous_learning` | 17,707 | Status unconfirmed — see §19.5 canonicalization note |
| `geospatialfeatures` | 60,875 | — |
| `GBIM_sample_rows` | 5,000 | — |
| `gbim_beliefs_v2` | 5,000 | — |
| `msallis_docs` | verify current | Grown from 4,192 (March 28) |
| `autonomous_learner` | **~23,200+** ★ | Canonical name — confirmed ✅; grown ≈288/day |
| `appalachian_cultural_intelligence` | verify current | Served by `allis-aaacpe-rag:8047→8032` |
| `research_history` | verify current | Grown from 785 |
| `ms_allis_memory` | verify current | UUID `79240788-0828-45f3-b1bc-a9a3593628a6` confirmed ✅ |
| `psychological_rag` | 968 | Stable since March 28 ✅ |
| `gis_wv_benefits` | 4,668 | — |
| `GBIM_Fayette_sample` | 1,535 | — |
| `conversation_history` | post-wipe count ★ | Wiped and reseeded clean April 16 — count reflects post-wipe only |
| `governance_rag` | 643 | — |
| `zcta_centroids` | 829 | — |
| `commons_rag` | 306 | — |
| `appalachian_english_corpus` | 227 | — |
| `local_resources` | **207** ★ | Ch.17 April 16 baseline — verify current |
| `spiritual_wisdom` | 135 | — |
| `spiritual_knowledge` | 12 | — |
| `contracts` | 51 | — |
| `geospatial_features` | 50 | — |
| `au02_threat_seeds` | — | Active |
| `msallis-smoke` | 1 | Smoke test record |

> **Total confirmed April 23, 2026: 48 active collections ★, ~6,740,611 total
> vectors ★.**

> **⚠️ LANDOWNER BELIEFS (`LANDOWNER_CORPORATE`, `LANDOWNER_GOVERNMENT`) are NOT in
> ChromaDB.** Served exclusively by `gbim_query_router` (port 7205) via
> `mvw_gbim_landowner_spatial` in production `msallis-db:5433` ★. 20,593 records.
> PostgreSQL-native path only.

> **⚠️ UUID preservation risk:** `ms_allis_memory` UUID
> `79240788-0828-45f3-b1bc-a9a3593628a6` is hardcoded in the consciousness bridge. If
> ChromaDB is rebuilt, run `scripts/preserve_memory_uuid.sh` before maintenance and
> `scripts/restore_memory_uuid.sh` after if UUID is lost. See Ch. 22 §22.10.

> **⚠️ ChromaDB v2 API:** All shell-based commands must use
> `/api/v2/tenants/default_tenant/databases/default_database/`. The `/api/v1/` path
> is permanently removed. Python `chromadb` client (1.5.5) handles this transparently.

---

### 19.8.11 Dedicated AAACPE Intelligence Pipeline

The AAACPE (Appalachian App Cultural and Community Platform Engine) intelligence
pipeline is served by two dedicated containers added to compose inventory as of April
14, 2026. This replaces the legacy `allis-ingest-api` + `allis-ingest-watcher` path
for Appalachian cultural intelligence data.

| Container | Host Port | Container Port | Role |
|---|---|---|---|
| `allis-aaacpe-scraper` | 8048 | 8033 | Web scraper; APScheduler scheduler |
| `allis-aaacpe-rag` | 8047 | 8032 | RAG query service; serves `appalachian_cultural_intelligence` collection |

**Scheduler configuration:**

- `run_full_scrape` — triggered daily at 06:00 UTC and every 6 hours (APScheduler).
- Scraped documents are embedded with `all-minilm:latest` (384-dim) and written to
  the `appalachian_cultural_intelligence` ChromaDB collection.

**Collection state:** verify current doc count ★ (was 1,090 as of April 14, 2026).

**Open item closed:** The prior open item for the AAACPE pipeline is closed. The
dedicated `allis-aaacpe-scraper` + `allis-aaacpe-rag` stack is the authoritative
ingest and query path for Appalachian cultural intelligence data. Any reference to
`allis-ingest-api` or `allis-ingest-watcher` as the AAACPE ingest mechanism is stale.

---

## 19.9 Auth and Security Updates (April 2026)

### OI-36-C — Closed (2026-04-03)

`ALLIS_API_KEY` plaintext bypass has been permanently removed from
`msallis-unified-gateway.py`. The gateway now reads only from the Docker secret at
`secrets/allis_api_key.txt`.

**`/auth/token` contract change:** Bootstrap tokens derived from the secret file no
longer auto-validate. Tokens must be registered in the auth service's invite store
before they will be accepted.

**Preflight gate key check:** `scripts/preflight_gate.sh` validates that the
`secrets/allis_api_key.txt` file is exactly 64 bytes before any compose up.

### OI-36-A — CLOSED ★ (April 23, 2026)

Auth enforcement at the Caddy perimeter level — `forward_auth` token validation before
routing to `/chat*` — is now **active**. OI-36-A is **closed** as of April 23, 2026.
See §19.8.1 for updated Caddy diagram.

---

## 19.10 Consciousness Bridge and Neurobiological Master (April 2026)

### DNS Resolution Fix (April 14, 2026)

`NEUROMASTER_URL` was briefly mis-routed. Confirmed correct hostname:

```
allis-neurobiological-master:8018
```

on `qualia-net`. Connectivity confirmed via `docker exec` DNS probe and HTTP 200 on
`/health` from the consciousness bridge.

### Network Topology Fix (April 14, 2026)

`allis-neurobiological-master` was previously on `qualia-net` only.
`msallis-rebuild_default` bridge has been added for cross-stack connectivity. Both
networks are now active for this container.

**Updated `allis-consciousness-bridge` services dict:**

```python
services = {
    "unified_gateway": "http://allis-unified-gateway:8011",
    "neuro_master":    "http://allis-neurobiological-master:8018",
    "direct_rag":      "http://allis-rag-server:8016",
    "hilbert":         "http://allis-hilbert:8010",
    "woah":            "http://allis-woah:7012",
    "chroma":          "http://allis-chroma:8000",
}
```

All entries confirmed correct.

---

## 19.11 External Access Points and Network Topology (April 23, 2026 ★)

### qualia-net Topology — Confirmed April 23, 2026

| Service | Container name | Internal port | Status |
|:--|:--|:--|:--|
| WOAH stub | `allis-woah` | 7012 | ✅ Confirmed |
| ChromaDB | `allis-chroma` | 8000 | ✅ Confirmed — 48 collections ★, ~6,740,611 vectors ★ |
| Consciousness Bridge | `allis-consciousness-bridge` | 8018 (actual) | ✅ Confirmed |
| RAG server | `allis-rag-server` | 8016 (internal) | ✅ Confirmed — host maps as 8003→8016 |
| Ollama | `allis-ollama` | 11434 | ✅ Confirmed |
| Neurobiological Master | `allis-neurobiological-master` | 8018 | ✅ Confirmed — DNS fix April 14; /health HTTP 200 |
| AAACPE scraper | `allis-aaacpe-scraper` | 8033 (internal) | ✅ Active — host 8048→8033 |
| AAACPE RAG | `allis-aaacpe-rag` | 8032 (internal) | ✅ Active — host 8047→8032 |
| I-Containers | `allis-i-containers` | 8015 | ✅ Fully operational — dual_awareness: true |

### Host-Exposed Ports (April 23, 2026 ★)

| Port | Service | Notes |
|:--|:--|:--|
| 8443 | Caddy (HTTPS) | Public-facing perimeter; **OI-36-A CLOSED ★** — auth enforcement active |
| 8055 | `allis_auth_service` | systemd-managed; internal only |
| 8051 | `allis-main-brain` (external) | Mapped from internal 8050 |
| 8056 | `allis-memory` | Secured; `127.0.0.1`; `_auth()` confirmed |
| 8048 | `allis-aaacpe-scraper` | → container 8033; APScheduler |
| 8047 | `allis-aaacpe-rag` | → container 8032; appalachian_cultural_intelligence |
| 8015 | `allis-i-containers` | `127.0.0.1` binding; fully operational |
| 8003 | `allis-rag-server` (external) | Maps to container-internal port 8016 |
| 8002 | `allis-chroma` (external) | Maps to container-internal port 8000 |
| 7205 | `gbim_query_router` | Landowner GBIM queries; internal-only hardening pending |
| 11434 | `allis-ollama` | Embeddings and LLM inference |
| **5433** | PostgreSQL `msallis-db` ★ | **Production** — 16 GB / 294 tables / 11 schemas; all live GBIM queries |
| **5452** | PostgreSQL `postgis-forensic` ★ | **Forensic** — 17 GB / 314 tables / 9 schemas; auditing only |
| 6379 | Redis (`allis-redis`) | Async job state; idempotency; health cache |
| 8073, 8074, 8075 | EEG band services | — |

---

## 19.12 Async Job Management API

| Endpoint | Method | Function |
|:--|:--|:--|
| `/chat_async` | POST | Create async job — returns `job_id` immediately |
| `/chat_status/{job_id}` | GET | Poll for progress and result |
| `/chat_cancel/{job_id}` | DELETE | Cancel a specific running job |
| `/chat_cancel_all` | DELETE | Cancel all running jobs |

- Job state persists in Redis (`allis-redis:6379`) with 30-minute TTL.
- State survives `allis-main-brain` container restarts.
- Cancel operations perform true `asyncio.Task` cancellation.
- Idempotency TTL: 1,800s.

---

## 19.13 Verified Reboot Sequence (April 23, 2026 ★)

```bash
# Step 0: Run preflight gate — must pass all checks
bash scripts/preflight_gate.sh
# Validates 64-byte ALLIS_API_KEY file, Chroma collections,
# key collection counts, GBIM entities, allis-memory auth

# Step 1: Confirm allis_auth_service is running under systemd
systemctl status allis-auth-service

# Step 2: Start all compose-managed containers
cd msallis-rebuild-working/msallis-rebuild
docker compose up -d
# ⚠️ Orphan warning for nbb_* and llm*-proxy is EXPECTED
# DO NOT use --remove-orphans

# Step 3: Start and verify the six pipeline containers
./allis_startup.sh
# Go signal: Six green health check marks

# Step 4: Verify qualia-net services
docker exec allis-consciousness-bridge \
  python3 -c "import httpx; r=httpx.get('http://allis-woah:7012/'); print(r.status_code, r.json())"
# Expected: 200

docker exec allis-consciousness-bridge \
  python3 -c "import httpx; r=httpx.get('http://allis-neurobiological-master:8018/health'); print(r.status_code)"
# Expected: 200

# Step 5: Verify ChromaDB v2 API and collection count
curl http://127.0.0.1:8002/api/v2/tenants/default_tenant/databases/default_database/collections
# Expected: 48 collections ★

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

# Step 9: Verify allis-memory auth boundary
curl http://127.0.0.1:8056/health                                        # 200 (intentionally public)
curl http://127.0.0.1:8056/memory/sessions                               # 401 (protected)
curl -H "Authorization: Bearer $ALLIS_API_KEY" \
  http://127.0.0.1:8056/memory/sessions                                  # 200

# Step 10: Verify rag-server env vars
docker exec allis-rag-server env | grep -E "OLLAMA_HOST|EMBED_MODEL|CHROMA_HOST"
# Expected:
# OLLAMA_HOST=http://allis-ollama:11434
# EMBED_MODEL=all-minilm:latest
# CHROMA_HOST=http://allis-chroma:8000

# Step 11: Verify production DB table count ★
psql -h 127.0.0.1 -p 5433 -U postgres -d msallis \
  -c "SELECT COUNT(*) FROM information_schema.tables WHERE table_type='BASE TABLE';"
# Expected: 294 tables ★

# Step 12: Verify forensic DB table count ★
psql -h 127.0.0.1 -p 5452 -U postgres -d postgres \
  -c "SELECT COUNT(*) FROM information_schema.tables WHERE table_type='BASE TABLE';"
# Expected: 314 tables ★

# Step 13: Verify Caddy auth enforcement active ★
curl -s -o /dev/null -w "%{http_code}" https://127.0.0.1:8443/chat \
  -H "Content-Type: application/json" -d '{"message":"test"}' -k
# Expected: 401 (unauthenticated) — confirms OI-36-A CLOSED
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
| March 22, 2026 | 81* | Caddy perimeter (8443) + `allis_auth_service` (8055 systemd); `allis-crypto-policy` removed |
| March 25, 2026 | 81 | `allis-rag-server` port mapping corrected; qualia-net topology confirmed |
| March 28, 2026 | 96 | `allis-memory:8056` corrected; ChromaDB full audit: 40 collections, 6,675,442 vectors; 96/96 Up |
| April 1, 2026 | 96 | LEARN-01/02/03 resolved; autonomous learner repaired; `services-safe` synced |
| April 13, 2026 | 109 | ChromaDB upgraded server 1.0.0 / client 1.5.5; I-Containers fully operational; `memories` table schema complete; `allis-msallis-db` added to compose; `msallis-pgdata-rescue` retired; `preflight_gate.sh` passing all checks; `preserve_memory_uuid.sh` and `restore_memory_uuid.sh` written |
| April 14, 2026 | 109 | `allis-aaacpe-scraper` (8048→8033) + `allis-aaacpe-rag` (8047→8032) added; APScheduler `run_full_scrape` daily 06:00 UTC + every 6h; `appalachian_cultural_intelligence` at 1,090 docs; AAACPE open item closed; OI-36-C closed — `ALLIS_API_KEY` plaintext bypass removed; consciousness bridge DNS fix; neurobiological master added to `msallis-rebuild_default` bridge; 49 ChromaDB collections confirmed |
| **April 16, 2026** ★ | **108** | Neurobiological rebuild; ChromaDB corrupt collection cleanup (3 deleted + recreated); UUID hardcode eliminated; BBB fail-closed hardening applied (Ch.16 ★) — all 6 sub-filter exception defaults → `passed=False`; `BBB_OUTPUT_BLOCKING=true` confirmed; ChromaDB → 48 collections; `conversation_history` wiped and reseeded clean; `bbb-output-filter` (port 8017) confirmed operational |
| **April 23, 2026** ★ | **100** | GPU pipeline optimizations (102.58s RTX 4070); service consolidations; two-container DB split confirmed: production `msallis-db` host 5433 (16 GB / 294 tables / 11 schemas) + forensic `postgis-forensic` host 5452 (17 GB / 314 tables / 9 schemas); ChromaDB ~6,740,611 vectors; `autonomous_learner` ~23,200+; OI-36-A CLOSED — Caddy `forward_auth` enforcement active; `rag_grounded_v2` + `llm_judge_v3` confirmed active (OI-37-C closed April 6) |

*81 = 80 Docker-managed + 1 systemd-managed (`allis_auth_service`).*

---

*Last updated: April 23, 2026 by Carrie Kidd (Mamma Kidd), Mount Hope WV*

*April 14, 2026: `allis-aaacpe-scraper` and `allis-aaacpe-rag` added. APScheduler documented. AAACPE open item closed. OI-36-C closed. Consciousness bridge DNS fix. Neurobiological master added to `msallis-rebuild_default` bridge. ChromaDB 49 collections confirmed (corrected to 48 as of April 23). `all-minilm:latest` (384-dim) confirmed canonical. `allis-memory` `/events` reference removed.*

*April 16, 2026: BBB fail-closed hardening (★ Ch.16) — all 6 sub-filter exception defaults → `passed=False`; `BBB_OUTPUT_BLOCKING=true` confirmed; `bbb-output-filter` port 8017 operational; filter count corrected 7 → 6; ChromaDB corrupt collection cleanup → 48 collections; `conversation_history` wiped and reseeded clean; UUID hardcode eliminated.*

*April 23, 2026 ★: Container count → 100. Two-container DB split applied throughout: production `msallis-db` host 5433 (16 GB / 294 tables / 11 schemas); forensic `postgis-forensic` host 5452 (17 GB / 314 tables / 9 schemas). All `msallisgis:5435 / 45 GB / 515 pub / 742 total` references superseded. ChromaDB → 48 collections / ~6,740,611 vectors throughout. `autonomous_learner` → ~23,200+. End-to-end benchmark → 102.58s (GPU). OI-36-A CLOSED — §19.1, §19.8.1, §19.9 updated; Caddy diagram updated. §19.13 ~95 GB expected value removed entirely. §19.14 April 16 and April 23 rows added. `local_resources` → 207 docs (Ch.17 April 16 baseline). `conversation_history` post-wipe note added. All GBIM row counts marked verify-current. `rag_grounded_v2` + `llm_judge_v3` noted active in §19.8.6. Judge pipeline `heuristic_contradiction_v1` removal noted.*
