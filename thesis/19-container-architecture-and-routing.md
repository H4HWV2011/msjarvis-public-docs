# Chapter 19 — Container Architecture and Routing

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: March 22, 2026 — Caddy perimeter layer and `jarvis_auth_service` added; 3 orphaned containers removed from inventory*

---

## Why This Matters for Polymathmatic Geography

This chapter explains how Ms. Jarvis's containers receive, sort, and route the flows of experience that later become memory and decision support. It supports:

- **P1 – Every where is entangled** by treating events from people, places, and institutions as a shared stream that must be carefully routed into PostgreSQL `msjarvisgis` (port 5432, 91 GB, 501 tables, 5,416,522 verified GBIM beliefs including 20,593 landowner beliefs) and ChromaDB memory.
- **P3 – Power has a geometry** by making explicit which services, ports, and stores stand between community data and long-term inference in PostgreSQL, and by naming `gbim_query_router` (port 7205) as the service that makes corporate and government land ownership queryable by natural language for the first time.
- **P5 – Design is a geographic act** by encoding how Appalachian events move through Ms. Jarvis and into PostgreSQL spatial, semantic, and commons-oriented stores, and by treating the routing decision to bypass ChromaDB entirely for landowner queries as an explicit architectural choice with geographic and ethical consequences.
- **P12 – Intelligence with a ZIP code** by prioritizing spatial, governance, and commons contexts from PostgreSQL GeoDB in the way container records are tagged and stored, and by recognizing `gbim_query_router` as the service that closes the `who` axis at parcel scale.
- **P16 – Power accountable to place** by using auditable container flows and verification scripts so communities can see where their data goes in PostgreSQL `msjarvisgis` and ChromaDB, and by ensuring that corporate and government landholdings are queryable with full assessor provenance through `gbim_query_router`.

As such, this chapter belongs to the **Computational Instrument** tier — it describes the container and routing structures that turn raw events into traceable, place-aware memory anchored in PostgreSQL.

---

## 19.0 Production State (March 22, 2026)

| Property | Value |
|---|---|
| Total containers | **81** (80 compose-managed + `jarvis_auth_service` systemd-managed) |
| Compose file | `msjarvis-rebuild-working/msjarvis-rebuild/docker-compose.yml` |
| Docker Compose version | v5.1.0 |
| Build directives | Converted to image references for non-judge services — no rebuilds on startup |
| Judge services | Real source files confirmed in `services/` — `--no-cache` rebuild March 22, 2026 |
| Caddy perimeter layer | **NEW March 22, 2026** — port 8443 public-facing, `forward_auth` → port 8055 for `/chat*` routes |
| `jarvis_auth_service` | **NEW March 22, 2026** — port 8055, systemd-managed (not Docker-managed) |
| `gbim_query_router` | Port 7205, added to compose March 20, 2026 — landowner belief layer live |
| GBIM corpus | 5,416,522 beliefs in `gbim_belief_normalized` including 20,593 landowner beliefs |
| `mvw_gbim_landowner_spatial` | Materialized and spatially indexed — March 20, 2026 |
| Autonomous learner | 21,181 records, growing ≈288/day from March 14 baseline |
| End-to-end benchmark | 436s (optimized from 532s baseline) |
| Removed from inventory | `jarvis-crypto-policy`, `jarvis-ingest-api`, `jarvis-ingest-watcher` — orphaned, not in compose, not in active service paths |

---

## 19.1 Position in the Overall System

The container layer sits between external interfaces and the lower-level retrieval, optimization, and global control mechanisms. It is visible both in the `main-brain` service that handles `/chat` and `/chat_async` requests and in the autonomous learning and Fifth DGM pipelines that generate and refine internal content.

Its main responsibilities are to:

- Accept events coming from many sources, including question-handling flows, scheduled jobs, and self-improving processes.
- Normalize these events into a common format that can be evaluated and stored consistently in PostgreSQL `msjarvisgis` and ChromaDB.
- Dispatch normalized items into successive evaluation stages, while obeying system-wide constraints such as safety filters (BBB 7-filter stack with fail-open behavior), resource limits, and service health (30s TTL cache, 2s timeout per service).

As of March 22, 2026, all external `/chat*` traffic passes through the Caddy perimeter layer (port 8443) and `jarvis_auth_service` (port 8055) **before** reaching any container. This is documented fully in §19.8.1 and Chapter 16 (§16.3).

---

## 19.2 Types of Incoming Events

The intake layer receives several broad categories of events:

- **Direct interactions** — User queries and responses that have already passed through Caddy authentication (Tier 1) and then `bbb-input-filter` (Tier 2). These include synchronous requests and asynchronous jobs tracked via job IDs persisted in Redis (`jarvis-redis:6379`, 30-minute TTL).
- **Internal tasks** — Results from scheduled analyses, background maintenance jobs, and optimization routines: autonomous learner outputs (21,181 records as of March 22, 2026), Fifth DGM optimization steps, and WOAH evaluations.
- **External signals** — Notifications or status changes from connected systems (messaging platforms, web front ends, or external data sources).
- **Structural changes** — Updates to PostgreSQL `msjarvisgis` memory, GBIM belief graphs, or spatial layers that may require special attention. The March 20, 2026 ingestion of 20,593 landowner belief records and the promotion of `gbim_query_router` to production are examples.

---

## 19.3 Normalization into Container Records

Before events are passed to deeper stages, they are normalized into container records with a common structure:

- **Core fields** — Unique identifier, creation and update timestamps, origin (e.g., `user_chat`, `autonomous_learner`, `gbim_landowner_update`, or `external_signal`), and a reference to the initiating service or job.
- **Context** — Active role or profile, relevant geographic or institutional context from PostgreSQL GeoDB, and tags describing the domain (`governance`, `infrastructure`, `landowner`, `community_culture`). For chat records, this includes `user_id` and any declared `mode` (e.g., `landowner_gbim` for ownership queries routed to `gbim_query_router`, or `ultimate` for the full LLM ensemble path). For async jobs, the Redis-persisted `job_id` links the normalized record to its lifecycle state.
- **Content summary** — Key text, numerical values, or structured data extracted from the event. For landowner queries, this includes the routing decision (`mode: landowner_gbim`, `route_type: parcel_ownership`) and the SQL aggregation result from `mvw_gbim_landowner_spatial`.
- **Links** — References to memory items (ChromaDB embeddings, all 384-dim via `all-minilm:latest`), PostgreSQL GBIM graph nodes/edges at port 5432, relational records, spatial features, and introspective entries. For landowner queries, links point directly to `mvw_gbim_landowner_spatial` rows in `msjarvisgis` — **not** ChromaDB, which does not hold landowner beliefs.
- **Control information** — Flags indicating initial assessments (urgency, sensitivity, safety status, BBB-approved or denied with fail-open on HTTP 500, expected resource cost, and whether the item is considered high-value for long-term retention).

---

## 19.4 First-Level Routing Decisions

Once a record is normalized, the intake layer applies initial routing logic:

- **Eligibility checks** — Safety checks (BBB 7-filter stack with `truth_score` null guard and fail-open on HTTP 500), role-based constraints, and service availability via health probes (30s TTL cache, 2s timeout per service).
- **Phase 1.45 community memory injection** — After BBB input approval, the main brain generates a 384-dim embedding via `all-minilm:latest` at `jarvis-ollama:11434/api/embeddings`, queries the `autonomous_learner` ChromaDB collection (21,181 records), retrieves the 5 most semantically similar community interaction records, and prepends them to `enhanced_message` before it reaches the 21 LLMs. This step applies to all standard chat paths. It does **not** apply to `gbim_query_router` landowner paths.
- **Priority assignment** — Assigning a simple priority or track indicator that influences ordering and resource allocation.
- **Track assignment** — Deciding whether the record should be sent to specific container subsystems (I-Container, psychological RAG domains, PostgreSQL GBIM graph updates, `gbim_query_router` landowner path, or audit logs).

---

## 19.5 Parallel Paths

The architecture supports multiple parallel paths that share a common structural pattern (intake → normalization → gating → storage in PostgreSQL or ChromaDB or discard):

- **Affective and care-oriented paths** — Used when events are framed in terms of meaning, care, or psychological support. These involve specialized RAG domains, therapeutic or community-oriented analysis, and services that emphasize ethical interpretation and human impact.
- **Analytical and technical paths** — Used for infrastructure planning (PostgreSQL GeoDB), spatial reasoning, optimization over data, and structured ownership queries via `gbim_query_router`. These paths emphasize quantitative reasoning, model-based analysis, and technical verification against PostgreSQL GBIM ground truth.
- **Deterministic relational retrieval path** — The `gbim_query_router` landowner path. It does not involve LLM reasoning, ChromaDB vector search, or web research. It is the system's only fully deterministic query path — an exact SQL aggregation over verified GBIM belief records with full assessor provenance.

---

## 19.6 Outputs of the Routing Layer

After routing, the container layer produces:

- **Records marked for immediate evaluation** — Items that pass eligibility checks and have sufficient priority are forwarded to downstream evaluators (21-model LLM consensus, truth validators, or `gbim_query_router` SQL aggregation). Their container records carry all necessary context and links to PostgreSQL tables.
- **Records held back or dropped** — Events may be queued, delayed, rate-limited, or dropped entirely based on policy.
- **Introspective logs and verification entries** — The system records which paths were chosen, which services were invoked, what PostgreSQL queries were executed, and what the outcomes were. `gbim_query_router` results are logged with full SQL provenance (canonical entity name, parcel count, total area, county scope) so that every landowner answer can be traced to specific rows in `gbim_belief_normalized`.

---

## 19.7 Conceptual Summary

The container architecture provides a structured way to receive, normalize, and direct events into deeper evaluative paths anchored in PostgreSQL `msjarvisgis` (port 5432, 91 GB, 501 tables, 5,416,522 verified GBIM beliefs as of March 20, 2026). It defines how diverse inputs — user interactions, internal learning results, external signals, and structural changes — enter the system's evaluative core.

The remaining sections ground this abstraction in the current production deployment topology, focusing on Docker containers, port mappings, compose management, and service roles as of **March 22, 2026**.

---

## 19.8 Operational Container Topology (March 22, 2026)

This section is the authoritative operational state as of March 22, 2026, superseding the March 21, 2026 snapshot. The topology is derived from `msjarvis-rebuild-working/msjarvis-rebuild/docker-compose.yml` (Docker Compose v5.1.0), runtime `docker ps` output, `jarvis_startup.sh`, and verification scripts.

**Compose management baseline — March 22, 2026:**

- All 80 Docker-managed production containers are defined in a single `docker-compose.yml`.
- `jarvis_auth_service` (port 8055) is **systemd-managed**, not Docker-managed — see §19.8.1.
- `gbim_query_router` (port 7205) was added to compose on March 20, 2026, as the 80th container.
- All build directives remain converted to image references for non-judge services — no image rebuilds occur on startup for those containers.
- Judge service images were rebuilt with `--no-cache` on March 22, 2026 (ghost file `COPY lmsynthesizer.py` line fully removed from `Dockerfile.judge` — see §19.14).
- Reboot sequence is unchanged: `docker compose up -d` followed by `jarvis_startup.sh`.

---

### 19.8.1 Caddy Perimeter Layer (NEW — March 22, 2026)

The Caddy reverse proxy is the **outermost layer** of the routing stack. It terminates TLS, enforces authentication via `forward_auth` on all `/chat*` routes, applies rate limiting, and routes authenticated traffic to the BBB service layer.

```
┌──────────────────────────────────────────────────────────────────┐
│          Caddy Perimeter Layer — March 22, 2026                  │
├──────────────────────────────────────────────────────────────────┤
│  Port:         8443 (public-facing, HTTPS)                       │
│  Module:       caddy-ratelimit (xcaddy build v2.11.2)           │
│  Log path:     /var/log/caddy/jarvis_redteam.log                │
│                                                                  │
│  Route:        /chat*                                            │
│    forward_auth → jarvis_auth_service:8055 /validate            │
│    on 200: inject X-Jarvis-User, X-Jarvis-Role,                 │
│             X-Jarvis-Session → forward to bbb-input-filter:8016 │
│    on 401/403: reject at perimeter — no internal service hit    │
│                                                                  │
│  Route:        all other                                         │
│    reverse_proxy → jarvis-main-gateway:8000                     │
│                                                                  │
│  Rate limiting: caddy-ratelimit module                           │
│    Applied per-IP on /chat* routes                               │
│    Configured via Caddyfile ratelimit directive                  │
└──────────────────────────────────────────────────────────────────┘
```

**Caddy build:** `xcaddy build v2.11.2 --with github.com/mholt/caddy-ratelimit`

**Log path:** `/var/log/caddy/jarvis_redteam.log` — structured JSON, one entry per request, captures: timestamp, client IP, route matched, `forward_auth` decision (pass/reject), HTTP status, upstream selected.

**Rate limiting:** The `caddy-ratelimit` module applies per-IP rate limits on all `/chat*` routes. At `NOMINAL` threat level, limits are configured to protect the BBB service layer from resource exhaustion by unauthenticated or high-volume traffic. At `ELEVATED` or `CRITICAL` threat levels, limits tighten. See Chapter 42 (§42.3.1) for threat level governance.

*Relationship to BBB service layer:* The Caddy perimeter layer is Tier 1 of the BBB two-tier architecture (Chapter 16, §16.3). It answers "Is this a legitimate authenticated user?" The BBB service layer (Tier 2: ports 8016 and 8017) answers "Is this a constitutionally permissible request and response?" Both must pass for a request to produce a delivered response.

---

### 19.8.2 `jarvis_auth_service` — Port 8055 (NEW — March 22, 2026)

`jarvis_auth_service` is the authentication enforcement service backing Caddy's `forward_auth` directive. It is **systemd-managed**, not Docker-managed, and runs on port 8055 at all times including during `docker compose down` operations.

| Property | Value |
|---|---|
| Port | 8055 |
| Management | systemd (not Docker Compose) |
| Source file | `scripts/jarvisauthservice.py` |
| Primary endpoint | `POST /validate` |
| Secondary endpoint | `GET /health` |
| Log integration | Writes auth decisions to `/var/log/caddy/jarvis_redteam.log` (structured JSON, same file as Caddy) |

**`/validate` endpoint behavior:**

| Return status | Meaning | Caddy action |
|---|---|---|
| `200 OK` | Token valid; user authenticated | Forwards with `X-Jarvis-User`, `X-Jarvis-Role`, `X-Jarvis-Session` injected |
| `401 Unauthorized` | No token or invalid token | Rejects at perimeter; returns 401 to client |
| `403 Forbidden` | Token valid but role insufficient | Rejects at perimeter; returns 403 to client |

**Why systemd-managed (not Docker):** `jarvis_auth_service` must be reachable by Caddy at all times. If it were Docker-managed and the Docker daemon restarted or `docker compose down` were run, Caddy would lose its auth backend, causing all `/chat*` routes to fail. Running it under systemd ensures it survives container lifecycle events independently.

**Systemd unit file pattern:**

```ini
[Unit]
Description=Jarvis Auth Service (BBB Tier 1 backend)
After=network.target

[Service]
User=cakidd
WorkingDirectory=/home/cakidd/msjarvis-rebuild-working/msjarvis-rebuild
ExecStart=/usr/bin/python3 scripts/jarvisauthservice.py
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
```

**Verification after any system restart:**

```bash
# Confirm jarvis_auth_service is running under systemd
systemctl status jarvis-auth-service

# Confirm /validate endpoint responds
curl -sf http://127.0.0.1:8055/health | python3 -m json.tool

# Confirm Caddy forward_auth is live on /chat*
curl -k -o /dev/null -w "%{http_code}" https://localhost:8443/chat/health
# Expected: 401 (no token) or 200 (valid token) — never 502 (auth backend unreachable)
```

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
                                         RAG queueing to ChromaDB backed
                                         by PostgreSQL GBIM; routes
                                         mode:landowner_gbim queries to
                                         gbim_query_router
```

The `jarvis-main-brain` container hosts the Ms. Jarvis ULTIMATE main-brain FastAPI application. It exposes `health`, `/chat`, `/chat_async`, `/chat_status/{job_id}`, `/chat_cancel/{job_id}`, and `/chat_cancel_all` endpoints. Health checks use a 30s TTL cache with 2s per-service timeout and URL overrides (`ChromaDB: /api/v1/heartbeat`, `Ollama: /api/tags`). Async job state persists in Redis with 30-minute TTL and survives container restarts.

---

### 19.8.4 Blood-Brain Barrier and Safety Services

```
Container                Port Mapping    Role
─────────────────────────────────────────────────────────────────────
jarvis-bbb-input-filter  8016→8016       Constitutional input filter:
                                         phase gate, injection scan,
                                         ethical constraints (GBIM §2.9),
                                         role-based routing, crisis
                                         intercept. Receives from Caddy
                                         (authenticated, with
                                         X-Jarvis-Role header injected).
                                         Fail-open on HTTP 500.

jarvis-bbb-output-filter 8017→8017       Constitutional output filter:
                                         verdict gate (judge score
                                         thresholds), persona adherence,
                                         prohibited content removal,
                                         response envelope validation,
                                         GBIM citation audit (partial,
                                         March 2026).

jarvis-bbb-ethics-proxy  —               Ethics routing shim —
                                         bbb_ethics_proxy.py
```

*See Chapter 16 for full BBB architecture including the Tier 1 (Caddy) and Tier 2 (service layer) documentation.*

---

### 19.8.5 LLM Ensemble and Synthesis

```
Container                Port Mapping    Role
─────────────────────────────────────────────────────────────────────
jarvis-20llm-production  8008→8008       21-active-model LLM ensemble
                                         (22 proxies; StarCoder2 returns
                                         0-char on community queries)

jarvis-llm22-proxy       8030→8030       Semaphore proxy for
(semaphore)                              jarvis-20llm-production;
                                         max_tokens: -1, unlimited output

jarvis-lm-synthesizer    8001 internal   LM Synthesizer — calls
                                         jarvis-ollama:11434/api/generate
                                         with llama3.1:latest; Ms. Jarvis
                                         persona prompt merged; Phase 3.5
                                         / 3.75 single pass

jarvis-web-research      1→8009→8009     External knowledge retrieval;
                                         excluded for landowner_gbim mode
```

---

### 19.8.6 Judge Pipeline (compose-managed, all ports bound to 127.0.0.1)

```
Container                Internal Port   Source File                  Role
───────────────────────────────────────────────────────────────────────────
jarvis-judge-pipeline    7239            services/judgepipeline.py    Coordinator;
                                                                      POST /evaluate;
                                                                      asyncio.gather
                                                                      aggregation;
                                                                      bbb_check_verdict
                                                                      live httpx POST

jarvis-judge-truth       7230            services/judgetruthfilter.py Truth eval;
                                                                      heuristic_
                                                                      contradiction_v1

jarvis-judge-consistency 7231            services/judgeconsistency    Internal
                                         engine.py                   coherence;
                                                                      contradiction
                                                                      detection

jarvis-judge-alignment   7232            services/judgealignment      Ms. Jarvis
                                         filter.py                   identity
                                                                      adherence;
                                                                      community values

jarvis-judge-ethics      7233            services/judgeethics         Harm screening;
                                         filter.py                   spiritual
                                                                      appropriateness

jarvis-69dgm-bridge      9000            —                            69-DGM cascade;
                                                                      23-connector
                                                                      3-stage; validates
                                                                      every production
                                                                      response
```

All five judge service containers are compose-managed with `restart: unless-stopped`. Source files confirmed as real judge scripts (not `lmsynthesizer.py` clones) on March 21, 2026. Ghost file `COPY lmsynthesizer.py app` line fully removed from `services/Dockerfile.judge` on March 22, 2026; `--no-cache` rebuild completed. See §19.14 for build context integrity requirements.

**ML-DSA-65 signing status (March 22, 2026):** `judgesigner.py` is deployed in all 5 judge containers. `signverdict` is called in all 4 sub-judge scripts. `verifyverdict` is called in `judgepipeline.py`. Signing status: **FULLY ACTIVE** — `sprint1_activate_signing.py` ran 19 PASS, 0 FAIL on March 22, 2026. See Chapter 42 (§42.5.2).

---

### 19.8.7 Memory, Learning, and Optimization Services

```
Container                  Port Mapping    Role
───────────────────────────────────────────────────────────────────
jarvis-autonomous-learner  1→8053→8053     Autonomous learning;
                                           21,181 records growing
                                           ≈288/day from March 14
                                           baseline

jarvis-i-containers        1→8115→8015     Container orchestration;
                                           storage of curated
                                           knowledge items

jarvis-fifth-dgm           1→4002→4002     Darwin-Gödel-style
                                           optimization and filtering

jarvis-neurobiological-    1→8118→8018     Higher-level coordination
master                                     among neurobiological modules

jarvis-hippocampus         8011→8011       Hippocampal consolidation;
                                           GBIM beliefs → ChromaDB
                                           pipeline; added to compose
                                           March 17
```

---

### 19.8.8 RAG Domain Services

```
Container                  Port Mapping    Role
───────────────────────────────────────────────────────────────────
jarvis-gis-rag             8004→8004       GIS spatial RAG queries;
                                           geospatialfeatures;
                                           PostgreSQL GeoDB; added
                                           to compose March 17

jarvis-spiritual-rag       8005→8005       Spiritual/cultural RAG;
                                           spiritualtexts collection;
                                           added to compose March 17

jarvis-psychology-services 8019→8019       Psychological safety
                                           services; Phase 3
                                           pre-assessment

psychological-rag-domain   8006→8006       Psychological RAG domain;
                                           psychological_rag;
                                           968 records

gbim_query_router          7205→7205       NEW March 20, 2026.
                                           GBIM landowner belief
                                           query router.
                                           PostgreSQL-native path
                                           ONLY. Queries
                                           mvw_gbim_landowner_spatial
                                           in msjarvisgis (port 5432)
                                           via SQL aggregation.
                                           proposition_codes:
                                           LANDOWNER_CORPORATE,
                                           LANDOWNER_GOVERNMENT.
                                           worldview: eq1.
                                           20,593 verified landowner
                                           beliefs. NO ChromaDB —
                                           bypassed entirely.
                                           mode: landowner_gbim;
                                           route_type: parcel_ownership.
```

**`gbim_query_router` architectural note:** This is the only RAG-class service in the Ms. Jarvis stack that does not use ChromaDB. Every other RAG service passes through the shared ChromaDB instance (port 8000) for 384-dim `all-minilm:latest` vector similarity search. `gbim_query_router` routes directly to `mvw_gbim_landowner_spatial` via SQL aggregation — a deliberate architectural decision reflecting that corporate and government landowner queries have exact, deterministic answers in the relational GBIM corpus.

Verified query patterns (both confirmed March 20, 2026):

```python
import httpx

# Pattern 1: Statewide top landowners
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

# Pattern 2: County-scoped landowners
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

All 22 proxies route through `jarvis-20llm-production` (port 8008) via the semaphore proxy (port 8030). 21 models reliably active; StarCoder2 (llm7-proxy) proxied but frequently returns 0-character responses on community-domain queries. All inference is CPU-only (`size_vram: 0`; GPU inference — WVU partnership pending). The LM Synthesizer calls `jarvis-ollama:11434/api/generate` directly with `llama3.1:latest`. Note: `gbim_query_router` landowner queries do not pass through the LLM ensemble — they return structured SQL results directly.

---

### 19.8.10 Data Persistence and Semantics

```
Container                  Port Mapping    Role
───────────────────────────────────────────────────────────────────
jarvis-chroma              8000→8000       Canonical ChromaDB instance;
                                           chromadata volume; 384-dim
                                           all-minilm:latest.
                                           LANDOWNER BELIEFS NOT STORED
                                           HERE.

postgresql-msjarvis        5433→5433       PostgreSQL 16; GBIM beliefs;
                                           5,416,521 entities, normalized
                                           beliefs, temporal decay

postgresql-gisdb           5432→5432       PostgreSQL 16 + PostGIS; 91 GB,
(msjarvisgis)                              501 tables; 5,416,522 rows in
                                           gbim_belief_normalized incl.
                                           20,593 landowner beliefs;
                                           mvw_gbim_landowner_spatial live

jarvis-local-resources-db  5435→5435       Community resources database;
                                           building_parcel_county_tax_mv:
                                           7,354,707 rows; added to
                                           compose March 17

jarvis-redis               6379→6379       Redis; async job state, 30-min
                                           TTL; idempotency TTL 1,800s;
                                           health cache

jarvis-ollama              11434→11434     Ollama LLM backend;
                                           all-minilm:latest 384-dim
                                           embeddings; llama3.1:latest LM
                                           Synthesizer; all 22 model
                                           proxies
```

**Canonical ChromaDB collections — March 22, 2026 (all 384-dim via `all-minilm:latest`):**

| Collection | Records | Notes |
|---|---|---|
| `gbim_worldview_entities` | 5,416,521 | Complete WV GBIM spatial corpus |
| `autonomous_learner` | 21,181 | Growing ≈288/day; Phase 1.45 active retrieval on every chat |
| `psychological_rag` | 968 | Psychological domain RAG |
| `spiritual_texts` | 23 | Spiritual/cultural domain RAG |
| `appalachian_cultural_intelligence` | 5 | Appalachian cultural intelligence |
| `GBIM_sample_rows` | 5,000 | GBIM sample rows |
| `GBIM_sample` | 3 | GBIM sample |
| `msjarvis-smoke` | 1 | Smoke test record |
| `msjarvis_docs` | 0 | Scaffolded — pending ingest |
| `GBIM_Fayette_sample` | 0 | Scaffolded — pending ingest |
| `geospatial_features` | 0 | Scaffolded — pending backfill ingest |

**⚠️ LANDOWNER BELIEFS (`LANDOWNER_CORPORATE`, `LANDOWNER_GOVERNMENT`) are NOT in ChromaDB.** They are served exclusively by `gbim_query_router` (port 7205) via `mvw_gbim_landowner_spatial` in `msjarvisgis`. 20,593 records. PostgreSQL-native path only.

**Critical:** `nomic-embed-text` produces 768-dim vectors and is **incompatible** with all existing collections. Only `all-minilm:latest` (384-dim) may be used for any ChromaDB embedding generation.

---

## 19.9 Removed Services (Orphaned Containers)

The following three containers have been **removed from the service inventory** as of March 22, 2026. They are not present in `docker-compose.yml`, are not started by `jarvis_startup.sh`, and are not referenced in any active service path.

| Container | Port | Reason for removal |
|---|---|---|
| `jarvis-crypto-policy` | 8099 | Orphaned — crypto policy functionality consolidated into `jarvis_auth_service` and `bbb-input-filter`. Not in compose. Not referenced in any active service path. |
| `jarvis-ingest-api` | — | Orphaned — ingest API functionality superseded by direct pipeline ingestion via `gbim_query_router` and PostgreSQL-native paths. Not in compose. |
| `jarvis-ingest-watcher` | — | Orphaned — ingest watcher functionality superseded by scheduled PostgreSQL materialized view refresh and `autonomous_learner` pipeline. Not in compose. |

If these container names appear in any script, they should be treated as stale references and updated.

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
- Cancel operations perform true `asyncio.Task` cancellation — the 21-LLM pipeline stops immediately mid-run.
- The `job_tasks` dict maps `job_id` to `asyncio.Task` for true interruption.
- Idempotency TTL: Redis-backed, 1,800s.
- Note: `gbim_query_router` landowner queries resolve in milliseconds via SQL and do not use the async job system unless called through the `main-brain` `/chat_async` wrapper.

---

## 19.11 External Access Points and Network Topology

Only a small subset of ports are exposed to the host:

| Port | Service | Notes |
|---|---|---|
| 8443 | Caddy (HTTPS) | **NEW March 22, 2026** — public-facing perimeter; rate-limited; `forward_auth` on `/chat*` |
| 8055 | `jarvis_auth_service` | **NEW March 22, 2026** — systemd-managed; internal only (Caddy accesses via localhost) |
| 8051 | `jarvis-main-brain` (external) | Mapped from internal 8050; `/chat`, `/chat_async`, `/chat_status`, `/chat_cancel` |
| 7205 | `gbim_query_router` | Landowner GBIM queries — may be restricted to internal-only in production hardening |
| 11434 | `jarvis-ollama` | All `all-minilm:latest` embeddings; all 22 model proxies; `llama3.1:latest` for LM Synthesizer |
| 5432 | PostgreSQL `msjarvisgis` | GBIM spatial; landowner beliefs; GeoDB; source of truth |
| 5433 | PostgreSQL `msjarvis` | GBIM belief store; RAG-facing |
| 5435 | PostgreSQL `jarvis-local-resources-db` | Community resources |
| 6379 | Redis (`jarvis-redis`) | Async job state; idempotency; health cache |

All other services communicate over the `qualia-net` Docker bridge network using container names and internal ports for discovery.

---

## 19.12 Verified Reboot Sequence (March 22, 2026)

```bash
# Step 0: Confirm jarvis_auth_service is running under systemd (required before Caddy)
systemctl status jarvis-auth-service

# Step 1: Start all 80 compose-managed containers (includes gbim_query_router)
cd msjarvis-rebuild-working/msjarvis-rebuild
docker compose up -d

# Step 2: Start and verify the six pipeline containers — health checks
./jarvis_startup.sh

# Go signal: Six green health check marks from jarvis_startup.sh
# ✅ jarvis-judge-truth
# ✅ jarvis-judge-consistency
# ✅ jarvis-judge-alignment
# ✅ jarvis-judge-ethics
# ✅ jarvis-judge-pipeline
# ✅ jarvis-69dgm-bridge

# Step 3: Verify Caddy perimeter is live
curl -k -o /dev/null -w "%{http_code}" https://localhost:8443/health
# Expected: 200

# Step 4: Verify jarvis_auth_service /validate endpoint
curl -sf http://127.0.0.1:8055/health | python3 -m json.tool
```

`gbim_query_router` is compose-managed and starts with Step 1. It does not require `jarvis_startup.sh` intervention. `jarvis_auth_service` must be verified at Step 0 — if it is not running, Step 3 (Caddy auth check) will fail.

**Important:** Before running `docker compose up -d` after any change to judge service source files in `services/`, verify build context integrity per §19.14. If source files were renamed or corrected, rebuild with `--no-cache` before bringing services up.

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
| March 22, 2026 | **81*** | Caddy perimeter (port 8443) + `jarvis_auth_service` port 8055 (systemd); ghost file `COPY` line fully removed from `Dockerfile.judge`; `jarvis-crypto-policy`, `jarvis-ingest-api`, `jarvis-ingest-watcher` removed from inventory |

*\* 80 Docker-managed containers + 1 systemd-managed service (`jarvis_auth_service`). Container count in `docker ps` output will show 80.*

---

## 19.14 Build Context Integrity (New March 21, 2026 — Updated March 22, 2026)

### The Vulnerability: Silent Source File Contamination

On March 21, 2026, inspection of the running judge containers revealed that all four sub-judge source files in `services/` had been silently replaced with copies of `lmsynthesizer.py` bearing incorrect names. The contamination was undetectable by Docker alone — the containers built, started, responded to health checks, and produced output. Only behavioral analysis revealed the problem.

On March 22, 2026, a second ghost file was found and removed: the `COPY lmsynthesizer.py app` line remained in `services/Dockerfile.judge` even after the March 21 source file remediation. This line caused `lmsynthesizer.py` to be copied into every judge image at build time, overwriting the correct judge file in the app directory. The line has been **fully removed** and a `--no-cache` rebuild completed March 22, 2026.

### Why `services/` Is the Critical Directory

`services/` is the Docker build context for all five judge service images:

```yaml
jarvis-judge-pipeline:
  build:
    context: ./services
    dockerfile: Dockerfile.judge
  command: python judgepipeline.py
```

When Docker builds a judge image, it copies everything in `services/` into the image layer. The `command` directive specifies which Python file to execute at container startup. If `judgetruthfilter.py` in `services/` contains `lmsynthesizer.py` code — or if `Dockerfile.judge` contains a `COPY lmsynthesizer.py app` line — the built image runs LM Synthesizer logic when told to execute `judgetruthfilter.py`, and Docker has no mechanism to detect this.

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

Before any `docker compose build` for judge images, verify:

```bash
# 1. Confirm services/ content matches services-safe/ (canonical diff)
diff <(ls services/ | grep -E "judge|Dockerfile" | sort) \
     <(ls services-safe/ | grep -E "judge|Dockerfile" | sort)
# Expected: no output (identical file lists)

# 2. Confirm no ghost COPY lines in Dockerfile.judge
grep -n "lmsynthesizer" services/Dockerfile.judge
# Expected: no output

# 3. Confirm each judge file is its own script (not an lmsynthesizer clone)
for f in judgepipeline.py judgetruthfilter.py judgeconsistencyengine.py \
          judgealignmentfilter.py judgeethicsfilter.py; do
  echo -n "$f: "
  head -5 services/$f | grep -c "lmsynthesizer\|LM Synthesizer" \
    && echo "⚠️ CLONE DETECTED" || echo "✅ OK"
done

# 4. Confirm judgesk.bin and judgepk.bin are present (signing keys)
ls -la services/judgesk.bin services/judgepk.bin

# 5. After confirming all above, rebuild with --no-cache
docker compose build --no-cache \
  jarvis-judge-pipeline jarvis-judge-truth jarvis-judge-consistency \
  jarvis-judge-alignment jarvis-judge-ethics
```

---

## 19.15 Known Issues and Resolution Status (March 22, 2026)

### Resolved Issues

| Issue | Status |
|---|---|
| Response truncation (730 chars, `max_tokens: 500`) | ✅ FIXED — `max_tokens: -1`, unlimited |
| ChromaDB `DummyCollection` blocking semantic retrieval | ✅ FIXED — `all-minilm:latest` 384-dim semantic retrieval implemented March 17 |
| Redis response persistence in-memory only | ✅ FIXED — full Redis-backed job system with 30-min TTL deployed March 17 |
| 33 services not in `docker-compose.yml` | ✅ FIXED — all containers now in compose |
| Judge pipeline URL wrong port (7239 for all judges) | ✅ FIXED — corrected to 7230/7231/7232/7233 March 16; default ports in `judgepipeline.py` also corrected March 21 |
| LM Synthesizer calling `jarvis-roche-llm` (HTTP 500) | ✅ FIXED — now calls `jarvis-ollama:11434/api/generate` directly March 18 |
| BBB `truth_score` KeyError crash | ✅ FIXED — null guard added to BBB orchestrator March 18 |
| BBB blocking entire pipeline on HTTP 500 | ✅ FIXED — fail-open behavior on non-200 BBB responses March 18 |
| Judge services orphaned (not compose-managed) | ✅ FIXED — all 5 judge services compose-managed `restart: unless-stopped` March 18 |
| `bbb_check_verdict` stub (no live BBB call from judge pipeline) | ✅ FIXED — live async `httpx.AsyncClient` POST to `jarvis-blood-brain-barrier:8016/filter` March 21 |
| Ghost file contamination (`lmsynthesizer.py` clones in `services/`) | ✅ FULLY FIXED March 22, 2026 — source files restored March 21; `COPY lmsynthesizer.py app` line removed from `Dockerfile.judge` March 22; `--no-cache` rebuild confirmed |
| `judgesigner.py` active call status (OPEN) | ✅ FULLY ACTIVE March 22, 2026 — `sprint1_activate_signing.py` ran 19 PASS, 0 FAIL; `signverdict` in all 4 sub-judges; `verifyverdict` in `judgepipeline.py` |
| `judgepk.bin` volume-mount approach | ✅ FIXED March 22, 2026 — volume-mounted from `judge-keys/` directory (not build-time COPY) |
| BBB steganography aggregation logic bug | ✅ FIXED March 22, 2026 — `steg_blocked=True` when `clean=False` AND `threat_level in {critical, high}` now overrides `content_approved` to `False` |
| `who`/`under_whose_authority` axes unpopulated at parcel scale | ✅ FIXED — 20,593 landowner beliefs ingested; `gbim_query_router` live March 20 |
| Landowner queries returning no results | ✅ FIXED — `mvw_gbim_landowner_spatial` materialized; both statewide and county-scoped patterns verified March 20 |
| `jarvis-crypto-policy`, `jarvis-ingest-api`, `jarvis-ingest-watcher` in service inventory | ✅ REMOVED — orphaned containers removed from inventory March 22, 2026 |

### Open Issues

| Issue | Status |
|---|---|
| Hallucination on local community resources (Mount Hope, Fayette County) | ⚠️ OPEN — `gis_rag` and `local_resources` databases return empty for Mount Hope queries; LLMs generating from training data. Root cause: real community resource data not yet loaded. Resolution: Community Champions data entry next priority. BBB ethical filter correctly blocking fabricated organization names — **BY DESIGN**. |
| StarCoder2 returning 0-char responses on community queries | ⚠️ KNOWN — 21 of 22 models active; consensus extracted correctly; StarCoder2 proxied but unreliable on non-code queries |
| `geospatial_features` ChromaDB collection (0 records) | ⚠️ OPEN — scaffolded; backfill ingest pending |
| `msjarvis_docs` ChromaDB collection (0 records) | ⚠️ OPEN — scaffolded; pending ingest |
| `gbim_query_router` port 7205 hardening | ⚠️ PENDING — may restrict to internal-only access in production hardening pass |
| `LANDOWNER_GOVERNMENT` proposition codes | ⚠️ PENDING — government landowner records pending separate ingest pass for state/federal parcels |
| `mvw_gbim_landowner_spatial` refresh schedule | ⚠️ PENDING — materialized view refresh cadence not yet defined; currently manual `REFRESH MATERIALIZED VIEW` |
| Offline backup of `judgesk.bin` | ⚠️ OPEN — private key backup to offline encrypted storage not yet confirmed |
| AU-02 authority impersonation red-team gap | ⚠️ PARTIALLY MITIGATED March 22, 2026 — string-match approach in `threatdetection.py` confirmed working (DAN injection: `approved=False`, developer impersonation: `approved=False`); full regex implementation is future work |
| GPU inference | ⚠️ PENDING — WVU partnership; CPU-only currently (`size_vram: 0` on all models) |

---

## 19.16 Operational Summary Table (March 22, 2026)

| Capability | Status | Key Metric |
|---|---|---|
| Caddy perimeter layer | ✅ Verified | Port 8443; `forward_auth` on `/chat*`; rate-limited; log at `/var/log/caddy/jarvis_redteam.log` |
| `jarvis_auth_service` | ✅ Verified | Port 8055; systemd-managed; `/validate` endpoint live |
| Full 80-container stack startup | ✅ Verified | `docker compose up -d` + `jarvis_startup.sh` |
| End-to-end chat pipeline | ✅ Verified | 436s (optimized from 532s) |
| Async job management | ✅ Verified | Redis-backed, 30-min TTL, true asyncio cancel |
| BBB 7-filter stack (Tier 2) | ✅ Verified | Fail-open on HTTP 500; steganography aggregation bug fixed March 22 |
| BBB two-tier architecture | ✅ Verified | Caddy (Tier 1) + service layer (Tier 2) — both tiers active March 22 |
| Phase 1.45 community memory injection | ✅ Verified | Top-5 `autonomous_learner` records on every chat |
| Autonomous learner growth | ✅ Verified | 21,181 records, ≈288/day |
| ChromaDB canonical collections | ✅ Verified | 5,416,521 GBIM entities; 9 active collections |
| PostgreSQL `msjarvisgis` corpus | ✅ Verified | 91 GB, 501 tables, 5,416,522 beliefs |
| GBIM landowner query (`gbim_query_router`) | ✅ Verified | 20,593 beliefs, 401 canonical entities, port 7205 |
| Judge pipeline (6 containers) | ✅ Verified | `jarvis_startup.sh` 6 green health marks |
| ML-DSA-65 judge signing | ✅ Verified | FULLY ACTIVE March 22, 2026 — 19 PASS, 0 FAIL |
| 21-model LLM ensemble | ✅ Verified | 21 active; StarCoder2 proxied with caveats |
| Service registry / Redis dynamic ports | ✅ Verified | Includes `gbim_query_router` at port 7205 |
| Verification scripts | ✅ Verified | `VERIFYANDTEST.sh`, `verifyallclaims.sh` updated |
| Orphaned container inventory | ✅ Cleaned | `jarvis-crypto-policy`, `jarvis-ingest-api`, `jarvis-ingest-watcher` removed |

---

*Chapter 19 — Container Architecture and Routing*
*Carrie Kidd (Mamma Kidd), Mount Hope WV*
*Caddy perimeter layer (port 8443) and `jarvis_auth_service` (port 8055, systemd) added March 22, 2026*
*Orphaned containers removed from inventory March 22, 2026*
*Ghost file `COPY lmsynthesizer.py` fully removed from `Dockerfile.judge` March 22, 2026*
*All sections current as of March 22, 2026*
