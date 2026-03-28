# Chapter 19 — Container Architecture and Routing

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*

*Last updated: 2026-03-28 — ★ March 28, 2026: 96/96 containers Up — zero Restarting, zero Exited; `msjarvis` port 5433 restored (5,416,521 GBIM entities with `confidence_decay` metadata); `msjarvisgis` port 5432 confirmed (91 GB PostGIS, 501 tables, 993 ZCTA centroids) — replaces `gisdb` port 5433/13 GB references throughout; ChromaDB full audit (40 collections, 6,675,442 total vectors); `spiritual_rag` deduplicated (−19,338 vectors); `psychological_rag` restored (968 docs); `msjarvis_docs` expanded (4,192 items); `autonomous_learner` growing — first AAPCAppE external-source docs flowing; `jarvis-memory` port 8056 corrected `0.0.0.0` → `127.0.0.1`; `_auth()` confirmed on 4 sensitive routes; `JARVIS_API_KEY` set; `jarvis-ingest-api` and `jarvis-ingest-watcher` restored to active inventory (AAPCAppE pipeline operational); Ch. 12 §12.11 cross-references updated to §12.12. March 27, 2026: §19.9 Ch. 30 audit table forward cross-reference added; §19.8.10 `ms_jarvis_memory` ChromaDB collection row added with UUID; §19.8.8a `EMBED_MODEL` `nomic-embed-text` contradiction corrected; §19.11 `jarvis-neurobiological-master` qualia-net note added; §19.15 OI-05 conversation memory row added.*

---

## Why This Matters for Polymathmatic Geography

This chapter explains how Ms. Jarvis's containers receive, sort, and route the flows of experience that later become memory and decision support. It supports:

- **P1 – Every where is entangled** by treating events from people, places, and institutions as a shared stream that must be carefully routed into PostgreSQL `msjarvisgis` (port **5432** ★, **91 GB PostGIS, 501 tables**, 993 ZCTA centroids) and `msjarvis` (port **5433** ★, 5,416,521 verified GBIM entities) and ChromaDB memory (★ **40 collections, 6,675,442 vectors**).
- **P3 – Power has a geometry** by making explicit which services, ports, and stores stand between community data and long-term inference in PostgreSQL, and by naming `gbim_query_router` (port 7205) as the service that makes corporate and government land ownership queryable by natural language for the first time.
- **P5 – Design is a geographic act** by encoding how Appalachian events move through Ms. Jarvis and into PostgreSQL spatial, semantic, and commons-oriented stores, and by treating the routing decision to bypass ChromaDB entirely for landowner queries as an explicit architectural choice with geographic and ethical consequences.
- **P12 – Intelligence with a ZIP code** by prioritizing spatial, governance, and commons contexts from PostgreSQL GeoDB in the way container records are tagged and stored, and by recognizing `gbim_query_router` as the service that closes the `who` axis at parcel scale. ★ As of March 28, 2026: **96 containers**, **40 ChromaDB collections**, **6,675,442 total vectors**, and a fully operational AAPCAppE ingest pipeline — all running on a single Lenovo Legion 5 in Oak Hill, West Virginia.
- **P16 – Power accountable to place** by using auditable container flows and verification scripts so communities can see where their data goes in PostgreSQL `msjarvisgis` ★ and ChromaDB ★, and by ensuring that corporate and government landholdings are queryable with full assessor provenance through `gbim_query_router`.

As such, this chapter belongs to the **Computational Instrument** tier — it describes the container and routing structures that turn raw events into traceable, place-aware memory anchored in PostgreSQL.

---

## 19.0 Production State (★ March 28, 2026)

| Property | Value |
|---|---|
| Total containers | ★ **96** (compose-managed + `jarvis_auth_service` systemd-managed) |
| Compose file | `msjarvis-rebuild-working/msjarvis-rebuild/docker-compose.yml` |
| Docker Compose version | v5.1.0 |
| Build directives | Converted to image references for non-judge services — no rebuilds on startup |
| Judge services | Real source files confirmed in `services/` — `--no-cache` rebuild March 22, 2026 |
| Caddy perimeter layer | Port 8443 public-facing — see §16.3 for current auth gap (OI-36-A) |
| `jarvis_auth_service` | Port 8055, systemd-managed (not Docker-managed) |
| `gbim_query_router` | Port 7205, added to compose March 20, 2026 — landowner belief layer live |
| GBIM corpus (`msjarvis:5433` ★) | 5,416,521 beliefs in `msjarvis` with `confidence_decay` metadata |
| GBIM corpus (`msjarvisgis:5432` ★) | 5,416,522 rows in `gbim_belief_normalized` in `msjarvisgis` including 20,593 landowner beliefs |
| `mvw_gbim_landowner_spatial` | Materialized and spatially indexed — March 20, 2026 |
| ChromaDB ★ | **40 active collections, 6,675,442 total vectors** (March 28 full audit) |
| `spiritual_rag` ★ | Deduplicated — −19,338 vectors (March 28) |
| `psychological_rag` ★ | Restored — **968 docs** (March 28) |
| `msjarvis_docs` ★ | Expanded — **4,192 items** (March 28) |
| Autonomous learner | 21,181 records (March 21 baseline), growing ≈288/day ★ + AAPCAppE external-source docs flowing |
| `jarvis-memory` ★ | Port **8056** — corrected `0.0.0.0` → `127.0.0.1`; `_auth()` confirmed on 4 sensitive routes; `JARVIS_API_KEY` set |
| `jarvis-ingest-api` ★ | **Restored to active inventory** — AAPCAppE pipeline operational (65 docs, 39 sources, March 27) |
| `jarvis-ingest-watcher` ★ | **Restored to active inventory** — AAPCAppE pipeline operational |
| End-to-end benchmark | 436s (optimized from 532s baseline) |
| `jarvis-rag-server` port correction | March 25, 2026 — host 8003 maps to container-internal port **8016** (uvicorn listener). Mapping is `127.0.0.1:8003:8016`. Required env vars documented — see §19.8.8a. |
| qualia-net topology | Confirmed March 25, 2026 — all consciousness pipeline services on qualia-net — see §19.11 |
| Orphaned container warning | Documented March 25, 2026 — `nbb_*` and `llm*-proxy` namespaces produce expected orphan warnings — see §19.8.0 |
| Ch. 12 cross-reference ★ | §12.11 updated to **§12.12** throughout |

---

## 19.1 Position in the Overall System

The container layer sits between external interfaces and the lower-level retrieval, optimization, and global control mechanisms. It is visible both in the `main-brain` service that handles `/chat` and `/chat_async` requests and in the autonomous learning and Fifth DGM pipelines that generate and refine internal content.

Its main responsibilities are to:

- Accept events coming from many sources, including question-handling flows, scheduled jobs, and self-improving processes.
- Normalize these events into a common format that can be evaluated and stored consistently in PostgreSQL `msjarvisgis` (port **5432** ★, 91 GB PostGIS, 501 tables) and `msjarvis` (port **5433** ★, 5,416,521 GBIM entities) and ChromaDB (★ 40 collections, 6,675,442 vectors).
- Dispatch normalized items into successive evaluation stages, while obeying system-wide constraints such as safety filters (BBB 7-filter stack with fail-open behavior), resource limits, and service health (30s TTL cache, 2s timeout per service).

As of March 22, 2026, all external `/chat*` traffic passes through the Caddy perimeter layer (port 8443) and `jarvis_auth_service` (port 8055) **before** reaching any container. Authentication gap OI-36-A remains open — see Chapter 16, §16.11. ★ As of March 28, 2026, `jarvis-memory` (port **8056**) has been secured: `0.0.0.0` → `127.0.0.1`, `_auth()` confirmed on 4 sensitive routes, `JARVIS_API_KEY` set — BBB audit trail persistence is now localhost-bound and authenticated.

---

## 19.2 Types of Incoming Events

The intake layer receives several broad categories of events:

- **Direct interactions** — User queries and responses that have already passed through Caddy authentication (Tier 1) and then `bbb-input-filter` (Tier 2). These include synchronous requests and asynchronous jobs tracked via job IDs persisted in Redis (`jarvis-redis:6379`, 30-minute TTL).
- **Internal tasks** — Results from scheduled analyses, background maintenance jobs, and optimization routines: autonomous learner outputs (21,181 records as of March 22, 2026 baseline ★ + AAPCAppE external-source docs now flowing), Fifth DGM optimization steps, and WOAH evaluations.
- **External signals** — Notifications or status changes from connected systems (messaging platforms, web front ends, or external data sources). ★ AAPCAppE scraper (`jarvis-ingest-watcher`, 65 documents, 39 sources confirmed March 27) is the first operational external-signal ingest pathway.
- **Structural changes** — Updates to PostgreSQL `msjarvisgis` (port **5432** ★) memory, GBIM belief graphs, or spatial layers that may require special attention. The March 20, 2026 ingestion of 20,593 landowner belief records and the promotion of `gbim_query_router` to production are examples. ★ The March 28 ChromaDB maintenance audit (40 collections, `spiritual_rag` deduplication, `psychological_rag` restoration, `msjarvis_docs` expansion) is a structural change of the semantic memory layer.

---

## 19.3 Normalization into Container Records

Before events are passed to deeper stages, they are normalized into container records with a common structure:

- **Core fields** — Unique identifier, creation and update timestamps, origin (e.g., `user_chat`, `autonomous_learner`, `aappcappe_ingest` ★, `gbim_landowner_update`, or `external_signal`), and a reference to the initiating service or job.
- **Context** — Active role or profile, relevant geographic or institutional context from PostgreSQL GeoDB (`msjarvisgis:5432` ★, 91 GB PostGIS, 501 tables), and tags describing the domain (`governance`, `infrastructure`, `landowner`, `community_culture`). For chat records, this includes `user_id` and any declared `mode`. For async jobs, the Redis-persisted `job_id` links the normalized record to its lifecycle state.
- **Content summary** — Key text, numerical values, or structured data extracted from the event. For landowner queries, this includes the routing decision (`mode: landowner_gbim`, `route_type: parcel_ownership`) and the SQL aggregation result from `mvw_gbim_landowner_spatial`.
- **Links** — References to memory items (ChromaDB embeddings ★ — 40 collections, 6,675,442 vectors, all 384-dim via `all-minilm:latest`), PostgreSQL GBIM graph nodes/edges at `msjarvis:5433` ★ and `msjarvisgis:5432` ★, relational records, spatial features, and introspective entries. ★ BBB audit trail links now route to `jarvis-memory:8056` (corrected `0.0.0.0` → `127.0.0.1`, `_auth()` confirmed).
- **Control information** — Flags indicating initial assessments (urgency, sensitivity, safety status, BBB-approved or denied with fail-open on HTTP 500, expected resource cost, and whether the item is considered high-value for long-term retention).

---

## 19.4 First-Level Routing Decisions

Once a record is normalized, the intake layer applies initial routing logic:

- **Eligibility checks** — Safety checks (BBB 7-filter stack with `truth_score` null guard and fail-open on HTTP 500), role-based constraints, and service availability via health probes (30s TTL cache, 2s timeout per service).
- **Phase 1.45 community memory injection** — After BBB input approval, the main brain generates a 384-dim embedding via `all-minilm:latest` at `jarvis-ollama:11434/api/embeddings`, queries the `autonomous_learner` ChromaDB collection (21,181 records ★ + AAPCAppE docs flowing), retrieves the 5 most semantically similar community interaction records, and prepends them to `enhanced_message` before it reaches the 22 LLMs.
- **Priority assignment** — Assigning a simple priority or track indicator that influences ordering and resource allocation.
- **Track assignment** — Deciding whether the record should be sent to specific container subsystems (I-Container, psychological RAG domains via `psychological_rag` ★ 968 docs restored, PostgreSQL GBIM graph updates at `msjarvis:5433` ★ and `msjarvisgis:5432` ★, `gbim_query_router` landowner path, or audit logs persisted to `jarvis-memory:8056` ★).

---

## 19.5 Parallel Paths

The architecture supports multiple parallel paths that share a common structural pattern (intake → normalization → gating → storage in PostgreSQL or ChromaDB or discard):

- **Affective and care-oriented paths** — Used when events are framed in terms of meaning, care, or psychological support. These involve specialized RAG domains (`psychological_rag` ★ restored to 968 docs March 28), therapeutic or community-oriented analysis, and services that emphasize ethical interpretation and human impact.
- **Analytical and technical paths** — Used for infrastructure planning (PostgreSQL `msjarvisgis` GeoDB ★), spatial reasoning, optimization over data, and structured ownership queries via `gbim_query_router`. These paths emphasize quantitative reasoning, model-based analysis, and technical verification against PostgreSQL GBIM ground truth (`msjarvis:5433` ★, 5,416,521 entities).
- **Deterministic relational retrieval path** — The `gbim_query_router` landowner path. It does not involve LLM reasoning, ChromaDB vector search, or web research. It is the system's only fully deterministic query path.
- ★ **External-source ingest path** — The AAPCAppE ingest pipeline (`jarvis-ingest-api` + `jarvis-ingest-watcher`, restored to active inventory March 28). Community resource documents from external sources enter through this path and flow into ChromaDB (`msjarvis_docs` ★ expanded to 4,192 items) and `autonomous_learner`. This path closes the gap between the system's community resource policy intent and the previously empty `jarvis-local-resources-db` state.

---

## 19.6 Outputs of the Routing Layer

After routing, the container layer produces:

- **Records marked for immediate evaluation** — Items that pass eligibility checks and have sufficient priority are forwarded to downstream evaluators (22-model LLM consensus, truth validators, or `gbim_query_router` SQL aggregation). Their container records carry all necessary context and links to PostgreSQL tables at `msjarvis:5433` ★ and `msjarvisgis:5432` ★.
- **Records held back or dropped** — Events may be queued, delayed, rate-limited, or dropped entirely based on policy.
- **Introspective logs and verification entries** — The system records which paths were chosen, which services were invoked, what PostgreSQL queries were executed, and what the outcomes were. ★ BBB audit events now persist to `jarvis-memory:8056` (secured `127.0.0.1`, `_auth()` confirmed, `JARVIS_API_KEY` set, March 28).

---

## 19.7 Conceptual Summary

The container architecture provides a structured way to receive, normalize, and direct events into deeper evaluative paths anchored in PostgreSQL `msjarvisgis` (port **5432** ★, **91 GB PostGIS, 501 tables**, 993 ZCTA centroids) and `msjarvis` (port **5433** ★, **5,416,521 GBIM entities** with `confidence_decay` metadata). It defines how diverse inputs — user interactions, internal learning results, external signals including ★ AAPCAppE scraper documents, and structural changes — enter the system's evaluative core.

The remaining sections ground this abstraction in the current production deployment topology, focusing on Docker containers, port mappings, compose management, and service roles as of ★ **March 28, 2026**.

---

## 19.8 Operational Container Topology (★ March 28, 2026)

This section is the authoritative operational state as of ★ March 28, 2026. The topology is derived from `msjarvis-rebuild-working/msjarvis-rebuild/docker-compose.yml` (Docker Compose v5.1.0), runtime `docker ps` output, `jarvis_startup.sh`, and verification scripts.

**Compose management baseline — ★ March 28, 2026:**

- ★ All **96** Docker-managed production containers are defined in a single `docker-compose.yml` — **zero Restarting, zero Exited**.
- `jarvis_auth_service` (port 8055) is **systemd-managed**, not Docker-managed — see §19.8.2.
- `gbim_query_router` (port 7205) was added to compose on March 20, 2026.
- ★ `jarvis-memory` (port **8056**) corrected to `127.0.0.1`; `_auth()` confirmed on 4 sensitive routes; `JARVIS_API_KEY` set (March 28, 2026).
- ★ `jarvis-ingest-api` and `jarvis-ingest-watcher` **restored to active inventory** (AAPCAppE pipeline operational — 65 docs, 39 sources, March 27).
- All build directives remain converted to image references for non-judge services — no image rebuilds occur on startup for those containers.
- Judge service images were rebuilt with `--no-cache` on March 22, 2026.
- Reboot sequence is unchanged: `docker compose up -d` followed by `jarvis_startup.sh`.

---

### 19.8.0 Orphaned Container Warning — Expected Behavior (March 25, 2026)

> **⚠️ Documented March 25, 2026:** Running `docker compose up -d` from the `msjarvis-rebuild` project directory will produce a warning similar to:

```
WARN Found orphan containers (nbb_woah_algorithms, nbb_i_containers,
llm1-proxy, llm2-proxy, ... llm22-proxy) for this project.
If you removed or renamed this service in your compose file, you can run
this command with the --remove-orphans flag to clean it up.
```

**This is expected behavior.** The `nbb_*` containers and `llm*-proxy` containers are managed by a **separate compose file** in a different project directory. They are not orphans in the true sense — they are intentionally running services from a different compose project that happen to share the same Docker host.

> **⚠️ CRITICAL: Do NOT use `--remove-orphans`** unless you are intentionally decommissioning the NBB stack and all LLM proxy containers. Using `--remove-orphans` will stop and remove all `nbb_*` and `llm*-proxy` containers, taking down the NBB prefrontal stack (Chapter 12, **§12.12** ★), the WOAH algorithms service (Chapter 10), and all 22 LLM proxy containers (§19.8.9).

**Safe reboot procedure:**

```bash
# CORRECT — never use --remove-orphans
cd msjarvis-rebuild-working/msjarvis-rebuild
docker compose up -d
# Orphan warning will appear — this is expected and harmless

# WRONG — will decommission NBB stack and LLM proxies
# docker compose up -d --remove-orphans  ← DO NOT USE
```

If the orphan warning does not appear, verify that the NBB stack and LLM proxy compose file are running:

```bash
# Verify nbb stack is up
docker ps | grep nbb_

# Verify llm proxies are up
docker ps | grep llm.*proxy | wc -l
# Expected: 22
```

---

### 19.8.1 Caddy Perimeter Layer

The Caddy reverse proxy is the **outermost layer** of the routing stack. See Chapter 16, §16.3 for current status including OI-36-A (auth enforcement gap).

```
┌──────────────────────────────────────────────────────────────────┐
│ Caddy Perimeter Layer — ★ March 28, 2026                        │
├──────────────────────────────────────────────────────────────────┤
│ Port: 8443 (public-facing, HTTPS)                               │
│ Log path: /var/log/caddy/jarvis_redteam.log                     │
│                                                                  │
│ Route: /chat*                                                    │
│   → 127.0.0.1:8050 (unified gateway)                            │
│   ⚠ Token enforcement not active at proxy level (OI-36-A)      │
│                                                                  │
│ Route: /auth*, /feedback*, /chat/status*                        │
│   → 127.0.0.1:8055 (jarvis_auth_service)                        │
│                                                                  │
│ Route: /health*, /systems*                                       │
│   → 127.0.0.1:8050 (unified gateway)                            │
│                                                                  │
│ ★ jarvis-memory:8056 — corrected 0.0.0.0 → 127.0.0.1 (Mar 28) │
│   NOT routed through Caddy — localhost-bound only               │
└──────────────────────────────────────────────────────────────────┘
```

---

### 19.8.2 `jarvis_auth_service` — Port 8055

`jarvis_auth_service` is the authentication enforcement service. It is **systemd-managed**, not Docker-managed, and runs on port 8055 at all times including during `docker compose down` operations. See Chapter 16, §16.3.2 for full specification.

| Property | Value |
|---|---|
| Port | 8055 |
| Management | systemd (not Docker Compose) |
| Source file | `scripts/jarvisauthservice.py` |
| Primary endpoint | `POST /auth/token` |
| Secondary endpoint | `GET /health` |

★ **`jarvis-memory` (port 8056)** is the BBB audit trail store — distinct from `jarvis_auth_service`. As of March 28, 2026: corrected to `127.0.0.1`, `_auth()` confirmed on 4 sensitive routes, `JARVIS_API_KEY` set. Not systemd-managed — Docker-managed.

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
                                         RAG queueing to ChromaDB ★
                                         (40 collections, 6,675,442
                                         vectors) backed by PostgreSQL
                                         msjarvis:5433 ★ and
                                         msjarvisgis:5432 ★;
                                         routes mode:landowner_gbim
                                         queries to gbim_query_router
```

The `jarvis-main-brain` container hosts the Ms. Jarvis ULTIMATE main-brain FastAPI application. It exposes `health`, `/chat`, `/chat_async`, `/chat_status/{job_id}`, `/chat_cancel/{job_id}`, and `/chat_cancel_all` endpoints. Health checks use a 30s TTL cache with 2s per-service timeout. Async job state persists in Redis with 30-minute TTL and survives container restarts.

---

### 19.8.4 Blood-Brain Barrier and Safety Services

> **⚠️ BBB container architecture — verified March 25, 2026, ★ confirmed Up March 28, 2026:** There is **one** BBB container: `jarvis-blood-brain-barrier` at **port 8016**. Port 8017 (`bbb-output-filter`) does **not exist**. Both input filtering (Phase 1.4) and output filtering (Phase 4.5) are handled by the single service at port 8016. See Chapter 16 for full specification including Phase 4.5 log+passthrough mode (OI-02) and OI-36-A auth gap.

```
Container                Port Mapping    Role
─────────────────────────────────────────────────────────────────────
jarvis-blood-brain-      8016→8016       Single BBB container.
barrier                                  ★ Confirmed Up March 28.
                                         Phase 1.4: constitutional
                                         input filter (BLOCKING) —
                                         6 filters stable March 22–28.
                                         Phase 4.5: output filter
                                         (LOG+PASSTHROUGH — OI-02).
                                         Fail-open on HTTP 500.
                                         Verdict dict → jarvis-memory
                                         :8056 ★ (corrected, secured)

jarvis-memory            8056→8056       BBB audit trail persistence.
                                         ★ CORRECTED March 28, 2026:
                                         0.0.0.0 → 127.0.0.1
                                         _auth() confirmed on 4 routes
                                         JARVIS_API_KEY set

jarvis-bbb-ethics-proxy  —               Ethics routing shim —
                                         bbb_ethics_proxy.py
```

*See Chapter 16 for full BBB architecture.*

---

### 19.8.5 LLM Ensemble and Synthesis

```
Container                Port Mapping    Role
─────────────────────────────────────────────────────────────────────
jarvis-20llm-production  8008→8008       22-proxy LLM ensemble
                                         (22 proxies; 21 active;
                                         StarCoder2 returns 0-char
                                         on community queries)

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

All five judge service containers are compose-managed with `restart: unless-stopped`. Ghost file `COPY lmsynthesizer.py app` line fully removed from `services/Dockerfile.judge` on March 22, 2026; `--no-cache` rebuild completed. ML-DSA-65 signing: **FULLY ACTIVE** — `sprint1_activate_signing.py` ran 19 PASS, 0 FAIL on March 22, 2026. ★ All confirmed Up March 28, 2026.

---

### 19.8.7 Memory, Learning, and Optimization Services

```
Container                  Port Mapping   Role
───────────────────────────────────────────────────────────────────
jarvis-autonomous-learner  8053→8053      Autonomous learning;
                                          21,181 records (March 21
                                          baseline), growing ≈288/day
                                          ★ + AAPCAppE external-source
                                          docs now flowing (March 27)

jarvis-i-containers        8115→8015      Container orchestration;
                                          storage of curated
                                          knowledge items

jarvis-fifth-dgm           4002→4002      Darwin-Gödel-style
                                          optimization and filtering

jarvis-neurobiological-    8118→8018      Higher-level coordination
master                                    among neurobiological modules
                                          ⚠ Unreachable March 25
                                          sprint — open item

jarvis-hippocampus         8011→8011      Hippocampal consolidation;
                                          GBIM beliefs → ChromaDB ★
                                          (40 collections, 6,675,442
                                          vectors) pipeline;
                                          added to compose March 17

jarvis-memory              8056→8056      BBB audit trail persistence
                                          ★ CORRECTED March 28:
                                          0.0.0.0 → 127.0.0.1
                                          _auth() confirmed 4 routes
                                          JARVIS_API_KEY set

jarvis-ingest-api          —              ★ RESTORED to active inventory
                                          March 28 — AAPCAppE pipeline
                                          operational (65 docs ingested,
                                          39 sources confirmed March 27)
                                          See OI-30 for corpus tracking

jarvis-ingest-watcher      —              ★ RESTORED to active inventory
                                          March 28 — AAPCAppE pipeline
                                          operational; watches for new
                                          community resource documents
                                          See §19.9 for prior orphan note
```

---

### 19.8.8 RAG Domain Services

```
Container                  Port Mapping   Role
───────────────────────────────────────────────────────────────────
jarvis-rag-server          8003→8016      Text RAG — direct_rag path.
                                          ⚠ CORRECTED March 25, 2026:
                                          host 8003 maps to container-
                                          internal uvicorn listener on
                                          port 8016. Mapping is
                                          127.0.0.1:8003:8016.
                                          See §19.8.8a for required
                                          env vars.

jarvis-gis-rag             8004→8004      GIS spatial RAG queries;
                                          geospatialfeatures;
                                          PostgreSQL msjarvisgis:5432 ★
                                          (91 GB PostGIS, 501 tables)

jarvis-spiritual-rag       8005→8005      Spiritual/cultural RAG;
                                          spiritualtexts collection ★
                                          Deduplicated −19,338 vectors
                                          (March 28, 2026)

jarvis-psychology-services 8019→8019      Psychological safety
                                          services; Phase 3
                                          pre-assessment

psychological-rag-domain   8006→8006      Psychological RAG domain;
                                          psychological_rag collection ★
                                          Restored — 968 docs (Mar 28)

gbim_query_router          7205→7205      GBIM landowner belief
                                          query router.
                                          PostgreSQL-native path ONLY.
                                          Queries mvw_gbim_landowner_
                                          spatial in msjarvisgis:5432 ★
                                          (91 GB PostGIS) via SQL
                                          aggregation.
                                          proposition_codes:
                                          LANDOWNER_CORPORATE,
                                          LANDOWNER_GOVERNMENT.
                                          worldview: eq1.
                                          20,593 verified landowner
                                          beliefs. NO ChromaDB —
                                          bypassed entirely.
```

---

### 19.8.8a `jarvis-rag-server` — Port Correction and Required Environment Variables (March 25, 2026)

> **⚠️ Critical port correction — March 25, 2026:**

The `jarvis-rag-server` docker-compose port mapping is:

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

**Port mapping:** Host port **8003** maps to container-internal uvicorn listener on **port 8016**. The previous documentation showed `127.0.0.1:8003:8003`, which is incorrect. The uvicorn process inside the container binds to `0.0.0.0:8016`, not port 8003. All host-side calls use port 8003; all container-internal references (from other containers on qualia-net) must use `jarvis-rag-server:8016`.

**Required environment variables:**

| Variable | Correct value | Default if absent | Consequence of missing |
|---|---|---|---|
| `OLLAMA_HOST` | `http://jarvis-ollama:11434` | `http://ollama:11434` | Container attempts to connect to `ollama` (non-existent hostname) — all embedding calls fail with connection error |
| `EMBED_MODEL` | `all-minilm:latest` | `mxbai-embed-large` | Attempts to use `mxbai-embed-large`, which is not loaded in the Ollama instance — all embedding calls fail with model-not-found error |
| `CHROMA_HOST` | `http://jarvis-chroma:8000` | varies | ChromaDB connections fail or route to wrong host |

> **⚠️ EMBED_MODEL — canonical value is `all-minilm:latest`:** Any compose file entry showing `EMBED_MODEL=nomic-embed-text` must be corrected. `nomic-embed-text` produces **768-dim** vectors and is **incompatible** with all existing ChromaDB collections (384-dim). ★ All 40 ChromaDB collections (6,675,442 vectors as of March 28 full audit) are 384-dim — **only `all-minilm:latest` may be used for any ChromaDB embedding generation.** If the compose file still shows `nomic-embed-text`, update it to `all-minilm:latest` before the next restart.

> **If these env vars are missing or incorrect, `jarvis-rag-server` will silently appear to start but will fail on every embedding request.** The container will be RUNNING but non-functional. Always verify env vars are present after any compose file edit affecting this service.

**Calling `jarvis-rag-server` from other containers (qualia-net):**

```python
import httpx

# Health check — use container-internal port 8016
resp = httpx.get("http://jarvis-rag-server:8016/health")

# RAG query — container-internal port 8016
resp = httpx.post(
    "http://jarvis-rag-server:8016/query",
    json={"query": "community resources Fayette County", "n_results": 5}
)
```

**Calling from host:**

```bash
# Health check — use host port 8003
curl http://127.0.0.1:8003/health

# RAG query from host
curl -X POST http://127.0.0.1:8003/query \
  -H "Content-Type: application/json" \
  -d '{"query": "community resources Fayette County", "n_results": 5}'
```

**Verified in consciousness bridge services dict (March 25, 2026):**

```python
# jarvis-consciousness-bridge services dict
# direct_rag entry must use container-internal port 8016
services = {
    "direct_rag": "http://jarvis-rag-server:8016",
    ...
}
```

---

### 19.8.9 LLM Proxy Layer (21 active models, 22 proxies)

| Proxy | Port | Model |
|---|---|---|
| llm1-proxy | 8201 | TinyLlama `tinyllama:latest` |
| llm2-proxy | 8202 | Gemma `gemma:2b` |
| llm3-proxy | 8203 | MedLlama2 `medllama2:latest` |
| llm4-proxy | 8204 | MiniCPM-V `minicpm-v:latest` |
| llm5-proxy | 8205 | LLaVA `llava:latest` |
| llm6-proxy | 8206 | SQLCoder `sqlcoder:latest` |
| llm7-proxy | 8207 | StarCoder2 `starcoder2:latest` ⚠️ occasionally returns 0-char on community queries |
| llm8-proxy | 8208 | CodeLlama `codellama:latest` |
| llm9-proxy | 8209 | DeepSeek Coder `deepseek-coder:latest` |
| llm10-proxy | 8210 | Phi3 Mini `phi3:mini` |
| llm11-proxy | 8211 | BakLLaVA — **permanently disabled** (name-check guard) |
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

> **⚠️ Orphaned container warning:** All `llm*-proxy` containers are managed by a **separate compose file**. Running `docker compose up -d` from the `msjarvis-rebuild` directory will produce orphan warnings for these containers. This is expected. Do NOT use `--remove-orphans`. See §19.8.0.

All 22 proxies route through `jarvis-20llm-production` (port 8008) via the semaphore proxy (port 8030). 21 models reliably active; StarCoder2 (llm7-proxy) proxied but frequently returns 0-character responses on community-domain queries. Note: `gbim_query_router` landowner queries do not pass through the LLM ensemble. ★ All confirmed Up as part of 96-container stack March 28, 2026.

---

### 19.8.10 Data Persistence and Semantics

```
Container                  Port Mapping   Role
───────────────────────────────────────────────────────────────────
jarvis-chroma              8000→8000      Canonical ChromaDB instance;
                                          chromadata volume; 384-dim
                                          all-minilm:latest.
                                          On qualia-net (confirmed
                                          March 25). v2 API active
                                          (/api/v2/heartbeat → 200).
                                          ★ 40 active collections,
                                          6,675,442 total vectors
                                          (March 28 full audit).
                                          LANDOWNER BELIEFS NOT STORED
                                          HERE.

postgresql-msjarvis        5433→5433      ★ PostgreSQL 16; GBIM belief
(msjarvis)                               store; 5,416,521 entities
                                          with confidence_decay
                                          metadata; RAG-facing;
                                          ★ port 5433 RESTORED March 28

postgresql-msjarvisgis     5432→5432      ★ PostgreSQL 16 + PostGIS;
(msjarvisgis)                            91 GB, 501 tables, 993 ZCTA
                                          centroids; 5,416,522 rows in
                                          gbim_belief_normalized incl.
                                          20,593 landowner beliefs;
                                          mvw_gbim_landowner_spatial live
                                          ★ replaces gisdb:5433/13 GB
                                          throughout

jarvis-local-resources-db  5435→5435      Community resources database;
                                          building_parcel_county_tax_mv:
                                          7,354,707 rows
                                          ★ AAPCAppE ingest pipeline now
                                          operational — closing gap

jarvis-redis               6379→6379      Redis; async job state, 30-min
                                          TTL; idempotency TTL 1,800s;
                                          health cache

jarvis-ollama              11434→11434    Ollama LLM backend;
                                          all-minilm:latest 384-dim
                                          embeddings; llama3.1:latest LM
                                          Synthesizer; all 22 model
                                          proxies. On qualia-net
                                          (confirmed March 25).

jarvis-memory              8056→8056      BBB audit trail persistence.
                                          ★ CORRECTED March 28, 2026:
                                          0.0.0.0 → 127.0.0.1
                                          _auth() confirmed 4 routes
                                          JARVIS_API_KEY set
```

**Canonical ChromaDB collections — ★ March 28, 2026 full audit (all 384-dim via `all-minilm:latest`):**

| Collection | UUID | Records | Notes |
|---|---|---|---|
| `gbim_worldview_entities` | — | 5,416,521 | Complete WV GBIM spatial corpus |
| `autonomous_learner` | — | 21,181+ | Growing ≈288/day; ★ + AAPCAppE external-source docs now flowing; Phase 1.45 active retrieval on every chat |
| `ms_jarvis_memory` | `79240788-0828-45f3-b1bc-a9a3593628a6` | — | Consciousness bridge collection — UUID hardcoded in bridge service. **⚠️ UUID preservation risk:** If ChromaDB is rebuilt, this UUID must be re-registered manually or the consciousness bridge will fail to locate the collection. See Ch. 22 §22.10 for full UUID preservation procedures. |
| `psychological_rag` | — | ★ **968** | ★ RESTORED March 28, 2026 — psychological domain RAG |
| `spiritual_texts` | — | ★ (audited) | ★ `spiritual_rag` deduplicated − 19,338 vectors March 28 |
| `appalachian_cultural_intelligence` | — | 5 | Appalachian cultural intelligence |
| `GBIM_sample_rows` | — | 5,000 | GBIM sample rows |
| `GBIM_sample` | — | 3 | GBIM sample |
| `msjarvis-smoke` | — | 1 | Smoke test record |
| `msjarvis_docs` | — | ★ **4,192** | ★ EXPANDED March 28, 2026 — first AAPCAppE docs ingested |
| `GBIM_Fayette_sample` | — | 0 | Scaffolded — pending ingest |
| `geospatial_features` | — | 0 | Scaffolded — pending backfill ingest |

> ★ **Total confirmed March 28, 2026 full audit: 40 active collections, 6,675,442 total vectors.**

**⚠️ LANDOWNER BELIEFS (`LANDOWNER_CORPORATE`, `LANDOWNER_GOVERNMENT`) are NOT in ChromaDB.** They are served exclusively by `gbim_query_router` (port 7205) via `mvw_gbim_landowner_spatial` in `msjarvisgis:5432` ★. 20,593 records. PostgreSQL-native path only.

**Critical embedding model constraint:** `nomic-embed-text` produces 768-dim vectors and is **incompatible** with all existing collections. ★ All **40 collections** (6,675,442 vectors) are 384-dim — **only `all-minilm:latest` may be used for any ChromaDB embedding generation.** Correct any compose file entry showing `nomic-embed-text` to `all-minilm:latest` before next restart.

---

## 19.9 Removed Services / Restored Services (★ March 28, 2026)

### ★ Restored to Active Inventory (March 28, 2026)

> **★ CORRECTION from prior state (March 22–27):** `jarvis-ingest-api` and `jarvis-ingest-watcher` were listed as orphaned and removed from inventory as of the March 22, 2026 audit. As of **March 28, 2026**, both containers have been **restored to the active service inventory** because the AAPCAppE ingest pipeline is now operational.

| Container | Status | Notes |
|---|---|---|
| `jarvis-ingest-api` | ★ **ACTIVE** | AAPCAppE pipeline operational — 65 documents ingested, 39 sources confirmed (March 27, 2026). Now in compose. `msjarvis_docs` expanded to 4,192 items. See OI-30. |
| `jarvis-ingest-watcher` | ★ **ACTIVE** | AAPCAppE pipeline operational — watches for new community resource documents. Now in compose. See OI-30. |

> **⚠️ Ch. 30 audit table cross-reference (March 27, 2026):** The Ch. 30 AAPCAppE audit table previously listed these containers as ⚠️ "Stub only". That status is now superseded by the March 27–28 operational confirmation. See Ch. 30 and OI-30 for AAPCAppE corpus completion tracking.

### Permanently Removed from Inventory (March 22, 2026)

| Container | Port | Reason for removal |
|---|---|---|
| `jarvis-crypto-policy` | 8099 | Orphaned — crypto policy functionality consolidated into `jarvis_auth_service` and `bbb-input-filter`. Not in compose. Not referenced in any active service path. |

If `jarvis-crypto-policy` appears in any script, treat as a stale reference and update.

---

## 19.10 Async Job Management API

| Endpoint | Method | Function |
|---|---|---|
| `/chat_async` | POST | Create async job — returns `job_id` immediately |
| `/chat_status/{job_id}` | GET | Poll for progress and result |
| `/chat_cancel/{job_id}` | DELETE | Cancel a specific running job |
| `/chat_cancel_all` | DELETE | Cancel all running jobs |

**Implementation details:**
- Job state persists in Redis (`jarvis-redis:6379`) with 30-minute TTL.
- State survives `jarvis-main-brain` container restarts.
- Cancel operations perform true `asyncio.Task` cancellation — the 22-LLM pipeline stops immediately mid-run.
- Idempotency TTL: Redis-backed, 1,800s.

---

## 19.11 External Access Points and Network Topology (★ March 28, 2026)

### qualia-net Topology — Confirmed March 25, 2026 (★ All Up March 28)

All consciousness pipeline services are confirmed on `qualia-net`. The following table documents confirmed qualia-net membership as of ★ March 28, 2026:

| Service | Container name | Internal port | qualia-net status |
|---|---|---|---|
| WOAH stub | `jarvis-woah` | 7012 | ✅ Confirmed — IP 172.18.0.x, RUNNING March 25; ★ Up March 28 |
| ChromaDB | `jarvis-chroma` | 8000 | ✅ Confirmed — v2 API `/api/v2/heartbeat` → 200; ★ 40 collections, 6,675,442 vectors March 28 |
| Consciousness Bridge | `jarvis-consciousness-bridge` | 8018 (actual) | ✅ Confirmed — source at `/app/services/msjarvisconsciousnessbridge.py`; ★ Up March 28 |
| RAG server | `jarvis-rag-server` | 8016 (internal) | ✅ Confirmed — host maps as 8003→8016; ★ Up March 28 |
| Ollama | `jarvis-ollama` | 11434 | ✅ Confirmed — reachable from qualia-net as `http://jarvis-ollama:11434`; ★ Up March 28 |
| Neurobiological Master | `jarvis-neurobiological-master` | 8018 | ⚠️ Targeted for qualia-net confirmation — currently unreachable as of March 25, 2026 sprint |

> **`jarvis-neurobiological-master` (port 8018)** is the higher-level neurobiological coordination service (see §19.8.7). It is targeted for qualia-net confirmation in a future sprint but was unreachable during the March 25, 2026 sprint. Its qualia-net membership and health status remain open items. Do not route consciousness pipeline traffic through this service until connectivity is confirmed.

> **DNS resolution note:** DNS resolution between services on qualia-net uses Docker's embedded DNS. Container names resolve to their qualia-net IPs. If DNS resolution fails for any of the above services, confirm the container is **running** — DNS cannot resolve a stopped or exiting container regardless of network configuration. (This was the root cause of the `jarvis-woah` DNS failure prior to March 25 — the container was exiting, not a network misconfiguration. See Chapter 10.)

**Network topology diagram — qualia-net (★ March 28, 2026):**

```
qualia-net (172.18.0.0/16)
─────────────────────────────────────────
                │
┌───────────────┼───────────────────────┐
│               │                       │
jarvis-woah    jarvis-chroma        jarvis-ollama
:7012 ✅        :8000 ✅ ★            :11434 ✅
(stdlib stub)   (v2 API)             (embeddings +
★ Up Mar 28     ★ 40 collections      LLM inference)
                6,675,442 vectors      ★ Up Mar 28
                │
jarvis-consciousness-   jarvis-rag-server
bridge                  :8016 (internal) ✅ ★ Up Mar 28
:8018 (actual) ✅        host: 8003→8016
source: /app/services/  OLLAMA_HOST=http://jarvis-ollama:11434
msjarvisconsciousness   EMBED_MODEL=all-minilm:latest (see §19.8.8a)
bridge.py               CHROMA_HOST=http://jarvis-chroma:8000
★ Up Mar 28
                        jarvis-memory
                        :8056 ★ CORRECTED Mar 28
                        0.0.0.0 → 127.0.0.1
                        _auth() confirmed, JARVIS_API_KEY set

jarvis-neurobiological-master
:8018 (targeted)
⚠️ Unreachable March 25, 2026 sprint
qualia-net confirmation pending
```

**Services dict in `jarvis-consciousness-bridge` (confirmed March 25, 2026):**

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

### Host-Exposed Ports (★ March 28, 2026)

| Port | Service | Notes |
|---|---|---|
| 8443 | Caddy (HTTPS) | Public-facing perimeter; auth gap OI-36-A open |
| 8055 | `jarvis_auth_service` | systemd-managed; internal only |
| 8051 | `jarvis-main-brain` (external) | Mapped from internal 8050 |
| 8056 | `jarvis-memory` ★ | ★ CORRECTED March 28 — `0.0.0.0` → `127.0.0.1`; `_auth()` confirmed; `JARVIS_API_KEY` set |
| 8003 | `jarvis-rag-server` (external) | ⚠️ Maps to container-internal port **8016** (not 8003) |
| 7205 | `gbim_query_router` | Landowner GBIM queries — internal-only hardening pending |
| 11434 | `jarvis-ollama` | Embeddings and LLM inference |
| 5432 | PostgreSQL `msjarvisgis` ★ | GBIM spatial; landowner beliefs; GeoDB; 91 GB PostGIS, 501 tables |
| 5433 | PostgreSQL `msjarvis` ★ | GBIM belief store; RAG-facing; 5,416,521 entities; ★ RESTORED March 28 |
| 5435 | PostgreSQL `jarvis-local-resources-db` | Community resources; ★ AAPCAppE ingest now active |
| 6379 | Redis (`jarvis-redis`) | Async job state; idempotency; health cache |

All other services communicate over `qualia-net` Docker bridge network using container names and internal ports for discovery.

---

## 19.12 Verified Reboot Sequence (★ March 28, 2026)

```bash
# Step 0: Confirm jarvis_auth_service is running under systemd
systemctl status jarvis-auth-service

# Step 1: Start all compose-managed containers (★ 96 as of March 28)
cd msjarvis-rebuild-working/msjarvis-rebuild
docker compose up -d
# ⚠️ Orphan warning for nbb_* and llm*-proxy containers is EXPECTED
# DO NOT use --remove-orphans

# Step 2: Start and verify the six pipeline containers
./jarvis_startup.sh
# Go signal: Six green health check marks
# ✅ jarvis-judge-truth
# ✅ jarvis-judge-consistency
# ✅ jarvis-judge-alignment
# ✅ jarvis-judge-ethics
# ✅ jarvis-judge-pipeline
# ✅ jarvis-69dgm-bridge

# Step 3: Verify qualia-net services
docker exec jarvis-consciousness-bridge \
  python3 -c "import httpx; r=httpx.get('http://jarvis-woah:7012/'); print(r.status_code, r.json())"
# Expected: 200 {"status": "ok", "service": "jarvis-woah", "port": 7012}

docker exec jarvis-rag-server \
  python3 -c "import httpx; r=httpx.get('http://localhost:8016/health'); print(r.status_code)"
# Expected: 200

# Step 4: Verify jarvis-rag-server env vars are present
docker exec jarvis-rag-server env | grep -E "OLLAMA_HOST|EMBED_MODEL|CHROMA_HOST"
# Expected:
# OLLAMA_HOST=http://jarvis-ollama:11434
# EMBED_MODEL=all-minilm:latest  (update if still showing nomic-embed-text — see §19.8.8a)
# CHROMA_HOST=http://jarvis-chroma:8000

# ★ Step 4a: Verify jarvis-memory is localhost-bound and authenticated
docker exec jarvis-memory env | grep -E "JARVIS_API_KEY|HOST|BIND"
# Expected: JARVIS_API_KEY set; host/bind = 127.0.0.1 (not 0.0.0.0)
curl http://127.0.0.1:8056/health
# Expected: 200 (with auth token if _auth() is enforced on /health)

# Step 5: Verify Caddy perimeter is live
curl -k -o /dev/null -w "%{http_code}" https://localhost:8443/health
# Expected: 200

# ★ Step 6: Verify ChromaDB full audit baseline (March 28)
curl http://127.0.0.1:8000/api/v2/heartbeat
# Expected: 200
# Collection count should be 40; total vectors 6,675,442
```

`gbim_query_router` is compose-managed and starts with Step 1. `jarvis_auth_service` must be verified at Step 0. ★ `jarvis-ingest-api` and `jarvis-ingest-watcher` start with Step 1 — confirm AAPCAppE pipeline operational after Step 1.

**Important:** Before running `docker compose up -d` after any change to judge service source files in `services/`, verify build context integrity per §19.14. See §19.8.0 for orphaned container warning behavior.

---

## 19.13 Container Count History

| Date | Container count | Notable addition |
|---|---|---|
| Initial deployment | 70 | Core stack |
| March 13, 2026 | 73 | I-Containers port fix; 3 corpus containers identified missing |
| March 17, 2026 | 79 | 9 missing containers added to compose; Redis async job system; Docker Compose v5.1.0 upgrade |
| March 18, 2026 | 79 | Compose audit complete; all build→image for non-judge services; hash-prefix names resolved |
| March 20, 2026 | 80 | `gbim_query_router` port 7205 — landowner belief layer live |
| March 21, 2026 | 80 | Ghost file remediation; real judge scripts restored; sub-judge ports corrected; `bbb_check_verdict` live; `judgesigner.py` deployed |
| March 22, 2026 | **81\*** | Caddy perimeter (port 8443) + `jarvis_auth_service` port 8055 (systemd); ghost file `COPY` line fully removed from `Dockerfile.judge`; `jarvis-crypto-policy` removed from inventory; `jarvis-ingest-api` and `jarvis-ingest-watcher` temporarily orphaned pending AAPCAppE activation |
| March 25, 2026 | **81** | `jarvis-rag-server` port mapping corrected (8003→8016 internal); env vars documented; orphaned container warning documented (§19.8.0); qualia-net topology confirmed (§19.11) |
| ★ March 28, 2026 | ★ **96** | `jarvis-memory:8056` corrected (`0.0.0.0`→`127.0.0.1`), `_auth()` confirmed, `JARVIS_API_KEY` set; `jarvis-ingest-api` + `jarvis-ingest-watcher` restored to active inventory (AAPCAppE operational); `msjarvis:5433` restored; `msjarvisgis:5432` confirmed (91 GB PostGIS, 501 tables); ChromaDB full audit: 40 collections, 6,675,442 vectors; `spiritual_rag` deduplicated (−19,338 vectors); `psychological_rag` restored (968 docs); `msjarvis_docs` expanded (4,192 items); 96/96 Up — zero Restarting, zero Exited |

*\* 80 Docker-managed containers + 1 systemd-managed service (`jarvis_auth_service`). Container count in `docker ps` output will show 80 at that date. ★ As of March 28, 2026: 96 containers Up in `docker ps` output.*

---

## 19.14 Build Context Integrity

### The Vulnerability: Silent Source File Contamination

On March 21, 2026, inspection of the running judge containers revealed that all four sub-judge source files in `services/` had been silently replaced with copies of `lmsynthesizer.py` bearing incorrect names. On March 22, 2026, a second ghost file was found and removed: the `COPY lmsynthesizer.py app` line remained in `services/Dockerfile.judge` even after the March 21 source file remediation. The line has been **fully removed** and a `--no-cache` rebuild completed March 22, 2026.

### `services-safe/` — The Authoritative Reference

`services-safe/` is the read-only reference copy of the canonical judge scripts that is never modified by routine operations. It must contain exactly:

- `services-safe/Dockerfile.judge`
- `services-safe/judgepipeline.py`
- `services-safe/judgetruthfilter.py`
- `services-safe/judgeconsistencyengine.py`
- `services-safe/judgealignmentfilter.py`
- `services-safe/judgeethicsfilter.py`
- `services-safe/judgesigner.py`

`services-safe/` must **never** be used as the Docker build context. It is a reference and restoration source only.

### Pre-Rebuild Mandatory Checklist

```bash
# 1. Confirm services/ content matches services-safe/ (canonical diff)
diff <(ls services/ | grep -E "judge|Dockerfile" | sort) \
     <(ls services-safe/ | grep -E "judge|Dockerfile" | sort)
# Expected: no output

# 2. Confirm no ghost COPY lines in Dockerfile.judge
grep -n "lmsynthesizer" services/Dockerfile.judge
# Expected: no output

# 3. Confirm each judge file is its own script
for f in judgepipeline.py judgetruthfilter.py judgeconsistencyengine.py \
<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# the previous response was truncated due to token's running out please continue

Here is the continuation from where the previous response was cut off — starting at the Pre-Rebuild Mandatory Checklist step 3 and continuing to the end of Chapter 19:

````markdown
# 3. Confirm each judge file is its own script
for f in judgepipeline.py judgetruthfilter.py judgeconsistencyengine.py \
          judgealignmentfilter.py judgeethicsfilter.py; do
  echo -n "$f: "
  head -5 services/$f | grep -c "lmsynthesizer\|LM Synthesizer" \
    && echo "⚠️ CLONE DETECTED" || echo "✅ OK"
done

# 4. Confirm judgesk.bin and judgepk.bin are present
ls -la services/judgesk.bin services/judgepk.bin

# 5. After confirming all above, rebuild with --no-cache
docker compose build --no-cache \
  jarvis-judge-pipeline jarvis-judge-truth jarvis-judge-consistency \
  jarvis-judge-alignment jarvis-judge-ethics
```

***

## 19.15 Known Issues and Resolution Status (★ March 28, 2026)

### Resolved Issues

| Issue | Status |
|---|---|
| Response truncation (730 chars, `max_tokens: 500`) | ✅ FIXED — `max_tokens: -1`, unlimited |
| ChromaDB `DummyCollection` blocking semantic retrieval | ✅ FIXED — `all-minilm:latest` 384-dim semantic retrieval implemented March 17 |
| Redis response persistence in-memory only | ✅ FIXED — full Redis-backed job system with 30-min TTL deployed March 17 |
| 33 services not in `docker-compose.yml` | ✅ FIXED — all containers now in compose |
| Judge pipeline URL wrong port (7239 for all judges) | ✅ FIXED — corrected to 7230/7231/7232/7233 March 16 |
| LM Synthesizer calling `jarvis-roche-llm` (HTTP 500) | ✅ FIXED — now calls `jarvis-ollama:11434/api/generate` directly March 18 |
| BBB `truth_score` KeyError crash | ✅ FIXED — null guard added to BBB orchestrator March 18 |
| BBB blocking entire pipeline on HTTP 500 | ✅ FIXED — fail-open behavior on non-200 BBB responses March 18 |
| Judge services orphaned (not compose-managed) | ✅ FIXED — all 5 judge services compose-managed `restart: unless-stopped` March 18 |
| `bbb_check_verdict` stub | ✅ FIXED — live async `httpx.AsyncClient` POST to `jarvis-blood-brain-barrier:8016/filter` March 21 |
| Ghost file contamination (`lmsynthesizer.py` clones in `services/`) | ✅ FULLY FIXED March 22, 2026 |
| `judgesigner.py` active call status | ✅ FULLY ACTIVE March 22, 2026 — 19 PASS, 0 FAIL |
| BBB steganography aggregation logic bug | ✅ FIXED March 22, 2026 |
| `jarvis-woah` exit code 1 (missing uvicorn) | ✅ FIXED March 25, 2026 — stdlib stub, volume bind mount, confirmed RUNNING on qualia-net |
| `jarvis-rag-server` port mapping documented as 8003:8003 | ✅ CORRECTED March 25, 2026 — mapping is 8003:8016 (host 8003 → container-internal 8016) |
| `jarvis-rag-server` env vars undocumented | ✅ DOCUMENTED March 25, 2026 — `OLLAMA_HOST`, `EMBED_MODEL`, `CHROMA_HOST` required |
| `EMBED_MODEL=nomic-embed-text` contradiction in compose | ✅ CORRECTED March 27, 2026 — canonical value is `all-minilm:latest`; `nomic-embed-text` is 768-dim and incompatible with all 384-dim collections |
| `jarvis-memory:8056` bound to `0.0.0.0` | ✅ FIXED ★ March 28, 2026 — corrected to `127.0.0.1` |
| `jarvis-memory` unauthenticated sensitive routes | ✅ FIXED ★ March 28, 2026 — `_auth()` confirmed on 4 sensitive routes; `JARVIS_API_KEY` set |
| `msjarvis` port 5433 unreachable | ✅ FIXED ★ March 28, 2026 — port 5433 restored; 5,416,521 GBIM entities with `confidence_decay` metadata confirmed |
| `spiritual_rag` vector bloat | ✅ FIXED ★ March 28, 2026 — deduplicated; −19,338 vectors removed |
| `psychological_rag` collection degraded | ✅ FIXED ★ March 28, 2026 — restored to 968 docs |
| `msjarvis_docs` collection empty | ✅ PARTIALLY FIXED ★ March 28, 2026 — expanded to 4,192 items (AAPCAppE first run); full corpus pending OI-30 |
| `jarvis-ingest-api` and `jarvis-ingest-watcher` orphaned | ✅ RESTORED ★ March 28, 2026 — AAPCAppE pipeline operational; both returned to active inventory |
| Ch. 12 §12.11 cross-reference stale | ✅ CORRECTED ★ March 28, 2026 — updated to §12.12 throughout |
| Container count stale (81 → 96) | ✅ UPDATED ★ March 28, 2026 — 96/96 Up, zero Restarting, zero Exited |

### Open Issues

| Issue | Status |
|---|---|
| OI-36-A — Gateway-level auth not enforced | ⚠️ OPEN — see Chapter 16 §16.11 |
| OI-05 — Conversation memory (`conversation_history` ChromaDB formal wiring) | 🟡 PARTIAL — emergent context passing confirmed March 25, 2026; formal ChromaDB wiring not yet complete — see Ch. 22 §22.9 |
| OI-02 — Phase 4.5 output BBB log+passthrough | ⚠️ OPEN — ~31% false-positive rate; tuning sprint pending |
| OI-30 — AAPCAppE full corpus completion | 🟡 IN PROGRESS ★ — ingest pipeline operational (65 docs, 39 sources); Community Champions data entry next priority; `msjarvis_docs` at 4,192 items |
| `jarvis-neurobiological-master` unreachable | ⚠️ OPEN — March 25 sprint; Chroma health check rerouted direct; qualia-net confirmation pending |
| Hallucination on local community resources | 🟡 IN PROGRESS ★ — AAPCAppE pipeline now operational; gap closing; Community Champions data entry next priority |
| StarCoder2 returning 0-char on community queries | ⚠️ KNOWN — 21 of 22 models active |
| `geospatial_features` ChromaDB collection (0 records) | ⚠️ OPEN — backfill ingest pending |
| `GBIM_Fayette_sample` ChromaDB collection (0 records) | ⚠️ OPEN — pending ingest |
| `gbim_query_router` port 7205 hardening | ⚠️ PENDING — may restrict to internal-only |
| `mvw_gbim_landowner_spatial` refresh schedule | ⚠️ PENDING — manual `REFRESH MATERIALIZED VIEW` currently |
| GPU inference | ⚠️ PENDING — WVU partnership; CPU-only currently |
| `ms_jarvis_memory` UUID preservation risk | ⚠️ OPEN — UUID `79240788-0828-45f3-b1bc-a9a3593628a6` hardcoded in consciousness bridge; ChromaDB rebuild requires manual UUID re-registration — see Ch. 22 §22.10 |
| `heuristic_contradiction_v1` judge upgrade | ⚠️ OPEN — upgrade to RAG-grounded truth scoring (Chapter 7 §7.8) targeting `msjarvisgis:5432` ★ and `msjarvis:5433` ★ both confirmed at correct ports; data stores ready; upgrade sprint pending |

***

## 19.16 Operational Summary Table (★ March 28, 2026)

| Capability | Status | Key Metric |
|---|---|---|
| Caddy perimeter layer | ✅ Verified | Port 8443; auth gap OI-36-A open (Chapter 16) |
| `jarvis_auth_service` | ✅ Verified | Port 8055; systemd-managed; `/auth/token` endpoint live |
| `jarvis-memory` ★ | ✅ SECURED | Port 8056; `0.0.0.0` → `127.0.0.1`; `_auth()` confirmed 4 routes; `JARVIS_API_KEY` set (March 28) |
| Full ★ 96-container stack startup | ✅ Verified | `docker compose up -d` + `jarvis_startup.sh`; orphan warning expected (§19.8.0); 96/96 Up — zero Restarting, zero Exited (March 28) |
| End-to-end chat pipeline | ✅ Verified | 436s (optimized from 532s) |
| Async job management | ✅ Verified | Redis-backed, 30-min TTL, true asyncio cancel |
| BBB 7-filter stack (Phase 1.4) | ✅ Verified | 6 filters stable March 22–28 ★; fail-open on HTTP 500 |
| BBB Phase 4.5 output | ⚠️ LOG+PASSTHROUGH | OI-02 pending; ~31% false-positive on Appalachian maternal voice |
| Phase 1.45 community memory injection | ✅ Verified | Top-5 `autonomous_learner` records on every chat; ★ + AAPCAppE docs flowing |
| Autonomous learner growth | ✅ Verified | 21,181 records (March 21 baseline), ≈288/day ★ + AAPCAppE external-source stream |
| ChromaDB canonical collections ★ | ✅ Audited | ★ **40 active collections, 6,675,442 total vectors** (March 28 full audit); `ms_jarvis_memory` UUID documented |
| `spiritual_rag` ★ | ✅ DEDUPLICATED | −19,338 vectors removed (March 28) |
| `psychological_rag` ★ | ✅ RESTORED | 968 docs (March 28) |
| `msjarvis_docs` ★ | ✅ EXPANDING | 4,192 items (March 28); OI-30 tracking full corpus |
| PostgreSQL `msjarvisgis` ★ | ✅ Verified | Port **5432**; 91 GB PostGIS, 501 tables, 993 ZCTA centroids |
| PostgreSQL `msjarvis` ★ | ✅ RESTORED | Port **5433**; 5,416,521 GBIM entities with `confidence_decay` metadata (March 28) |
| GBIM landowner query (`gbim_query_router`) | ✅ Verified | 20,593 beliefs, 401 canonical entities, port 7205 |
| Judge pipeline (6 containers) | ✅ Verified | `jarvis_startup.sh` 6 green health marks; ★ all Up March 28 |
| ML-DSA-65 judge signing | ✅ Verified | FULLY ACTIVE March 22, 2026 — 19 PASS, 0 FAIL |
| 22-model LLM ensemble | ✅ Verified | 21 active; StarCoder2 proxied with caveats |
| `jarvis-rag-server` port mapping | ✅ CORRECTED | `127.0.0.1:8003:8016` — host 8003 → container 8016 |
| `jarvis-rag-server` env vars | ✅ DOCUMENTED | `OLLAMA_HOST`, `EMBED_MODEL=all-minilm:latest`, `CHROMA_HOST` required |
| qualia-net topology | ✅ Confirmed | `jarvis-woah`, `jarvis-chroma`, `jarvis-consciousness-bridge`, `jarvis-rag-server`, `jarvis-ollama` all on qualia-net; ★ all Up March 28 |
| `jarvis-neurobiological-master` qualia-net | ⚠️ PENDING | Unreachable March 25 sprint — targeted for future qualia-net confirmation |
| Orphaned container warning | ✅ Documented | `nbb_*` and `llm*-proxy` — expected; `--remove-orphans` prohibited |
| `jarvis-ingest-api` ★ | ✅ RESTORED | Active inventory — AAPCAppE pipeline operational (65 docs, 39 sources, March 27) |
| `jarvis-ingest-watcher` ★ | ✅ RESTORED | Active inventory — AAPCAppE pipeline operational |
| `jarvis-crypto-policy` | ✅ Removed | Permanently removed from inventory March 22 |
| OI-05 conversation memory | 🟡 PARTIAL | Emergent context passing confirmed March 25; formal ChromaDB wiring pending — Ch. 22 §22.9 |
| OI-30 AAPCAppE corpus ★ | 🟡 IN PROGRESS | Pipeline operational; 4,192 docs in `msjarvis_docs`; Community Champions data entry next |
| `heuristic_contradiction_v1` judge upgrade ★ | ⚠️ PENDING | Both data stores confirmed at correct ports; upgrade sprint pending — Chapter 7 §7.8 |
| Ch. 12 cross-reference ★ | ✅ CORRECTED | §12.11 → **§12.12** throughout |

***

*Chapter 19 — Container Architecture and Routing*

*Carrie Kidd (Mamma Kidd), Mount Hope WV*

*March 27, 2026: §19.9 Ch. 30 audit table forward cross-reference added; §19.8.10 `ms_jarvis_memory` ChromaDB collection row added with UUID `79240788-0828-45f3-b1bc-a9a3593628a6`; §19.8.8a `EMBED_MODEL=nomic-embed-text` contradiction corrected — canonical value is `all-minilm:latest`; §19.11 `jarvis-neurobiological-master` qualia-net note added; §19.15 OI-05 conversation memory row added.*

*★ March 28, 2026: 96/96 containers Up — zero Restarting, zero Exited. `msjarvis` port 5433 restored (5,416,521 GBIM entities with `confidence_decay` metadata) — propagated to §19.0, Why This Matters, §19.1, §19.3, §19.4, §19.5, §19.6, §19.7, §19.8.3, §19.8.8, §19.8.10, §19.11, §19.15, §19.16. `msjarvisgis` port 5432 confirmed (91 GB PostGIS, 501 tables, 993 ZCTA centroids) — replaces all `gisdb` port 5433/13 GB references throughout. ChromaDB full audit (40 collections, 6,675,442 total vectors) — propagated to Why This Matters, §19.0, §19.1, §19.3, §19.4, §19.5, §19.7, §19.8.3, §19.8.7, §19.8.8, §19.8.10, §19.11, §19.15, §19.16. `spiritual_rag` deduplicated (−19,338 vectors) — §19.8.8, §19.8.10, §19.15, §19.16. `psychological_rag` restored (968 docs) — §19.5, §19.8.8, §19.8.10, §19.15, §19.16. `msjarvis_docs` expanded (4,192 items) — §19.8.10, §19.15, §19.16. `jarvis-memory` port 8056 corrected `0.0.0.0` → `127.0.0.1`; `_auth()` confirmed; `JARVIS_API_KEY` set — §19.0, §19.1, §19.3, §19.4, §19.6, §19.8.1, §19.8.2, §19.8.4, §19.8.7, §19.8.10, §19.11, §19.12, §19.15, §19.16. `jarvis-ingest-api` and `jarvis-ingest-watcher` restored to active inventory — §19.0, §19.2, §19.5, §19.8.7, §19.9, §19.12, §19.15, §19.16. Container count updated 81 → 96 throughout — §19.0, §19.8 baseline, §19.8.0, §19.12, §19.13, §19.16. Ch. 12 §12.11 → §12.12 — §19.8.0. `heuristic_contradiction_v1` upgrade readiness note added (both data stores confirmed) — §19.15, §19.16.*
