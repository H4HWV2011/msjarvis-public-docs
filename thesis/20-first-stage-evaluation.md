# 20. First-Stage Evaluation

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*

*Last updated: 2026-04-13*

---

> **Live Stack Snapshot — April 13, 2026**
>
> All facts in this chapter are anchored to the live verified stack as of April 13, 2026, with **109 running containers** (from `docker ps --filter "status=running" | wc -l`).
>
> | Check | Value | Source |
> |---|---|---|
> | Running containers | 109 | `docker ps --filter "status=running" \| wc -l` |
> | ChromaDB collections | 49 | `preflight_gate.sh` |
> | ChromaDB port binding | host 8002 → container 8000 | `docker port jarvis-chroma` |
> | `autonomous_learner` records | ≥ 21,181 | `preflight_gate.sh` |
> | `appalachian_cultural_intelligence` records | ≥ 1,084 | `preflight_gate.sh` |
> | `research_history` records | ≥ 785 | `preflight_gate.sh` |
> | `ms_jarvis_memory` records | ≥ 296 | `preflight_gate.sh` |
> | GBIM entities | ≥ 5,416,521 | `preflight_gate.sh` |
> | msjarvisgis public tables | 515 | `SELECT count(*) FROM pg_tables WHERE schemaname='public'` |
> | msjarvisgis total tables | 742 | `SELECT count(*) FROM pg_tables` |
> | msjarvisgis size | 95 GB | `SELECT pg_size_pretty(pg_database_size('msjarvisgis'))` |
> | BBB service | Up on :8016 | `curl http://localhost:8016/` |
> | jarvis-memory service | Up on :8056 | `curl -H "Authorization: Bearer $JARVIS_API_KEY" http://localhost:8056/health` |
> | I-Containers service | Up on :8015, dual_awareness: true | `curl http://localhost:8015/health` |
>
> These values are live and must be re-checked with the exact commands listed above for any future audit. Do not substitute hard-coded numbers from prior chapter revisions.

---

This chapter describes the first stage in the container paths — the evaluation layer that decides whether an incoming item is worth retaining at all, and in what initial form. Every user interaction, ingest event, and internal learning signal passes through this stage before anything is written to background storage, identity structures, or belief stores. The first stage does not establish long-term patterns; it filters, scores, and tags. What passes becomes a candidate for the background store described in Chapter 21.

---

## 20.1 Role of First-Stage Evaluation

First-stage evaluation serves as the system's primary admission gate. Its function is not to understand deeply but to decide quickly: is this item worth the cost of retention? The evaluation applies across three input classes:

- **User interactions** — messages arriving at the main-brain `/chat` endpoint (port 8050), routed through the LLM ensemble, BBB, and consciousness layers before a response is returned.
- **Ingest events** — documents arriving through `jarvis-ingest-api` and `jarvis-ingest-watcher` (AAPCAppE pipeline and similar external-source feeds).
- **Internal signals** — autonomous learning outputs, EEG band activity, and neurobiological processing results from the I-Container service (port 8015).

For each input class, first-stage evaluation produces a structured verdict that gates all downstream writes. Items that do not pass are dropped or held for human review. Items that pass are written to the background store and tagged for pattern accumulation (see Ch. 21).

First-stage evaluation is considered healthy only when `scripts/preflight_gate.sh` reports all of the following:

- 49 ChromaDB collections
- `autonomous_learner` ≥ 21,181 records
- `appalachian_cultural_intelligence` ≥ 1,084 records
- `research_history` ≥ 785 records
- `ms_jarvis_memory` ≥ 296 records
- GBIM entities ≥ 5,416,521
- `jarvis-memory:8056` auth confirmed
- BBB `:8016` Up

If `preflight_gate.sh` does not pass all 9 checks, first-stage evaluation must be treated as degraded regardless of container `Up` status.

---

## 20.2 Inputs and Triggering Conditions

### User Interaction Path

User messages arrive at main-brain port 8050 via authenticated POST to `/chat`. The minimum required fields are:

```json
{
  "message": "<user text>",
  "userid": "<user id>",
  "role": "<role>",
  "useallservices": false
}
```

The `Authorization: Bearer $JARVIS_API_KEY` header is required. Requests without a valid key are rejected before first-stage evaluation begins.

### Ingest Path

External documents arrive through `jarvis-ingest-api` and `jarvis-ingest-watcher`. These are evaluated for domain relevance and structural quality before being written to `msjarvis_docs` or `autonomous_learner`. This path bypasses the LLM ensemble — the first-stage gate for ingest events is domain-relevance scoring, not BBB truth filtering.

### Internal Signal Path

Autonomous learning outputs, EEG band activity (ports 8073, 8074, 8075), and Fifth DGM filter results are evaluated against identity coherence thresholds before being surfaced to the background store. The I-Container service (port 8015) now provides a live neurobiological processing gate for internal signals — outputs with `within_bounds: false` or `dual_awareness: false` are flagged before downstream writes.

---

## 20.3 The UltimateResponse: Canonical Output Schema

When a user interaction completes the full first-stage evaluation pipeline — routing, LLM ensemble (21 active / 22 registered; BakLLaVA eliminated, StarCoder2 excluded from scoring), BBB filtering, consciousness layers, and identity layers — the result is a structured `UltimateResponse`. The following is the canonical schema as directly observed from a live test call on April 13, 2026:

```json
{
  "response": "What do you need help with today?",
  "services_used": ["<service list>"],
  "consciousness_level": "ultimate_collective",
  "processing_time": 144.02,
  "architecture_layers": 9,
  "truthverdict": null
}
```

**Field notes:**

- `response` — The final text response returned to the user.
- `services_used` — Array of service identifiers that contributed to the response. Populated from the LLM ensemble and routing layer.
- `consciousness_level` — String label reflecting the highest consciousness layer reached. `"ultimate_collective"` is the current production value.
- `processing_time` — Float, seconds. The April 13 test recorded 144.02 seconds — this reflects full 9-layer processing and is expected at current ensemble scale.
- `architecture_layers` — Integer. Currently 9. Reflects the number of active processing layers traversed.
- `truthverdict` — Present in all `UltimateResponse` objects but **nullable**. Null when the BBB filter did not produce a definitive verdict for the specific interaction. When non-null, carries the BBB truth assessment from `jarvis-blood-brain-barrier:8016`. Do not treat null as an error — it is a valid and expected value for many interaction types.

Fields such as `validated_by` and `consensus_score` do not appear at the top level of the current `UltimateResponse` schema. Do not reference them as top-level fields in any script or downstream consumer.

---

## 20.4 The Blood-Brain Barrier (BBB)

The BBB service (`jarvis-blood-brain-barrier`, port 8016) is the primary truth and safety filter in the first-stage evaluation pipeline. It is confirmed Up as of April 13, 2026. Its root endpoint returns:

```json
{
  "service": "Ms. Jarvis Blood-Brain Barrier",
  "filters": ["<active filter list>"]
}
```

### Confirmed API Surface (April 13, 2026)

| Endpoint | Purpose |
|---|---|
| `/` | Service identity and active filter list |
| `/health` | Health check — Up/degraded status |
| `/filter` | Primary first-stage filter — evaluates incoming content |
| `/truth` | Truth assessment — evaluates factual claims |
| `/stats` | Aggregate filter statistics |
| `/filter_output` | Output-stage filtering — applied before response delivery |

**There is no `/check` endpoint.** Any prior documentation or script referencing `/check` on port 8016 is stale and must be corrected.

First-stage evaluation consults the BBB via `/filter` and `/truth`. Health and aggregate metrics are available at `/health` and `/stats`. Output-stage filtering uses `/filter_output`.

The BBB verdict is attached as `truthverdict` on every `UltimateResponse`. It is nullable (see §20.3). All BBB filtering decisions are durably persisted to `jarvis-memory:8056` (secured March 28, 2026) — the audit trail is not ephemeral.

---

## 20.5 ChromaDB as First-Stage Write Target

ChromaDB is served via `jarvis-chroma` on **host port 8002** (mapped to container port 8000). All first-stage background writes go through this binding. Direct references to `localhost:8000` as a host port are stale — the correct host-side address is `localhost:8002`.

All 49 active ChromaDB collections (6,722,589+ total vectors) are 384-dim using `all-minilm:latest`. No other embedding model may be used — `nomic-embed-text` produces 768-dim vectors and is incompatible with all existing collections (see Ch. 19 §19.8.8a and Ch. 21 §21.2).

### ChromaDB API

All shell-based commands must use the v2 API path. The v1 path (`/api/v1/`) is permanently removed in Chroma server 1.0.0:

```bash
# CORRECT — Chroma 1.0.0+
curl http://localhost:8002/api/v2/tenants/default_tenant/databases/default_database/collections

# STALE — do not use
curl http://localhost:8002/api/v1/collections
```

The Python `chromadb` client library (version 1.5.5) handles the v1 → v2 migration transparently. Only raw `curl` commands and scripts constructing HTTP requests directly are affected.

When a `/chat` call completes, the `background_rag_store` task writes a new record to `ms_jarvis_memory` (UUID: `79240788-0828-45f3-b1bc-a9a3593628a6`) via this binding. Every successful interaction produces exactly one new background record. The collection currently holds 296 records and must be verified by UUID — see Ch. 22 §22.10 for UUID preservation risk.

---

## 20.6 The `jarvis-memory` Audit Layer

`jarvis-memory` (port 8056) provides durable, authenticated storage for first-stage filtering decisions. It is secured: `0.0.0.0` corrected to `127.0.0.1`, `_auth()` confirmed on all sensitive routes, `JARVIS_API_KEY` required.

### Confirmed API Surface (April 13, 2026)

| Endpoint | Auth Required | Purpose |
|---|---|---|
| `/health` | No | Health check — intentionally public (standard monitoring exemption) |
| `/memory/turn` | Yes | Record a conversation turn |
| `/memory/get` | Yes | Retrieve memory record |
| `/memory/sessions` | Yes | List sessions |
| `/memory/session/{session_id}` | Yes | Get session detail |
| `/memory/quest` | Yes | Quest memory operations |
| `/memory/quest/{user_id}/{quest_id}` | Yes | Get specific quest |
| `/memory/quests/{user_id}` | Yes | List user quests |
| `/memory/consolidate/{user_id}` | Yes | Trigger memory consolidation |
| `/memory/episodic/{user_id}` | Yes | Episodic memory for user |
| `/steg_report` | Yes | Steganography report |
| `/pia_window` | Yes | PIA window |

**There is no `/events` endpoint.** Any prior documentation or script referencing `/events` on port 8056 is stale and must be corrected.

First-stage decisions are durably recorded via `/memory/turn` and related episodic and quest endpoints. Steganography and PIA windows are available at `/steg_report` and `/pia_window`. The `/health` endpoint is intentionally public and must not be treated as an auth breach.

Auth verification (confirmed April 13, 2026):

| Route | Authed (200) | Unauthed (401) | Status |
|---|---|---|---|
| `/health` | 200 | 200 | ✅ Intentionally open |
| `/memory/sessions` | 200 | 401 | ✅ Protected |
| `/memory/turn` | 405 (needs POST) | 405 | ✅ Protected — 405 = wrong method, auth passed |

---

## 20.7 PostgreSQL Substrates

### msjarvisgis (port 5435)

The authoritative GBIM and GIS store. All GBIM data is in `msjarvisgis` on port 5435 — not on port 5433. As of April 13, 2026:

| Metric | Value | Command |
|---|---|---|
| Public tables | 515 | `SELECT count(*) FROM pg_tables WHERE schemaname='public'` |
| Total tables | 742 | `SELECT count(*) FROM pg_tables` |
| Database size | 95 GB | `SELECT pg_size_pretty(pg_database_size('msjarvisgis'))` |

These are live values and must be re-checked with the same commands for future audits. Do not substitute the prior hard-coded values (501 tables, 91 GB) anywhere in this documentation.

Key GBIM tables:

| Table | Rows | Notes |
|---|---|---|
| `gbim_worldview_entity` | 5,415,896 | Primary GBIM entity table |
| `gbim_graph_edges` | 15,226,626 | — |
| `gbimbeliefnormalized` | 6,804,671 | — |
| `gbim_attrs` | 5,491,092 | — |
| `gbim_beliefs` | 3,747,712 | — |
| `gbim_evidence` | 2,121,228 | — |
| `gbim_belief_evidence` | 2,121,130 | — |
| `gbim_full_points_raw` | 1,389,855 | — |
| `mvw_gbim_landowner_spatial` | 20,593 | Landowner beliefs |
| `memories` | 3 | Promotion/linkage table — see Ch. 21 §21.2 |

The `memories` table carries the full promotion and linkage schema: `gbim_entity_id` (BIGINT, B-tree index), `spatial_ref` (geometry(Point,4326), GIST index), `reviewed` (BOOLEAN, partial index), `promoted` (BOOLEAN, partial index), `source` (TEXT), `chroma_id` (TEXT). These six columns and four indexes were applied cleanly on April 13, 2026.

The `gbim_query_router` (port 7205) landowner path is a fully deterministic PostgreSQL-native path with no ChromaDB interaction.

### jarvis-msjarvis-db (port 5433)

Added to `docker-compose.yml` on April 13, 2026 with `external: true` volume declaration for `msjarvis_pgdata`. Container is confirmed healthy. The prior `msjarvis-pgdata-rescue` container (wrong volume, 37 rows only, `gbim_entities` schema present with 0 live rows) is retired. The `msjarvis` database on port 5433 is currently offline for live GBIM operations — all live GBIM data is in `msjarvisgis` on port 5435.

---

## 20.8 I-Containers and Identity Layer Interface

The I-Container service (`ms_jarvis_i_containers_service.py`, port 8015) is fully operational as of April 13, 2026. It is not future work.

Confirmed live status:

```json
{
  "status": "healthy",
  "i_container_1": "active",
  "i_container_2": "active",
  "integration_layer": "active",
  "dual_awareness": true
}
```

One `jarvis-i-containers` container is confirmed running, mapped `127.0.0.1:8015 → 8015/tcp`.

The service imports all 10 neurobiological modules directly — it is its own NBB backend. The adapter (`jarvis-i-containers_icontainers_fastapi.py`) proxies to this service; "NBB backend not reachable" in adapter logs is expected and irrelevant.

**Module inventory:**

- I-Container 1 (Self Model): `SelfRecognition`, `IdentityCore`, `PersonalNarrative`, `EgoBoundaries`, `MemorySelf`
- I-Container 2 (Observer/Witness): `WitnessConsciousness`, `ReflectionSystem`, `IntrospectionEngine`, `MetacognitiveAwareness`, `ObserverSelf`

First-stage evaluation feeds into the I-Container layer indirectly: completed interactions are written to `ms_jarvis_memory`, which the consciousness bridge's `_get_url` read path surfaces across sessions (OI-05 — see Ch. 22 §22.9). This means the I-Container layer is receiving a continuous feed of evaluated, retained interactions and is already contributing to identity trajectory — this is not a future integration milestone.

The April 13, 2026 production baseline for identity metrics:

| Metric | Value |
|---|---|
| `identity_coherence` | 0.6 |
| `confidence` | 0.7 |
| `core_stability` | 0.9 |
| `core_values` | care, learning, integrity |
| `ego_check.within_bounds` | true |
| `boundary_mode` | healthy |
| `dual_awareness` | true |

Deviations from these baseline values on subsequent `/process` calls constitute a detectable identity drift pattern (see Ch. 21 §21.5).

---

## 20.9 Evaluation Criteria and Scoring

First-stage evaluation applies the following criteria, depending on input class:

### User Interaction

1. **Authentication** — `JARVIS_API_KEY` must be present and valid. No evaluation proceeds without it.
2. **BBB `/filter`** — Content is evaluated against the BBB's active filter list. Items failing the filter are blocked before LLM ensemble processing.
3. **LLM ensemble scoring** — 21 active proxies (22 registered; BakLLaVA eliminated, StarCoder2 excluded from scoring) produce a consensus response. Routing, ensemble weighting, and identity layer processing are applied.
4. **BBB `/truth`** — Truth assessment is applied to the candidate response. The result is attached as `truthverdict` on the `UltimateResponse`. Nullable — a null verdict is valid and does not constitute a failed evaluation.
5. **BBB `/filter_output`** — Output-stage filtering is applied to the final response before delivery.
6. **Background write** — If all stages complete, `background_rag_store` writes one record to `ms_jarvis_memory` and the BBB audit event is persisted to `jarvis-memory:8056` via `/memory/turn`.

### Ingest Event

1. **Domain relevance scoring** — Document is evaluated against target domain criteria (community resource relevance, structural quality).
2. **Direct write** — Documents passing relevance scoring are written directly to `msjarvis_docs` or `autonomous_learner` with metadata `services: ["aappcappe-ingest"]` and `type: "community_resource"`. No LLM ensemble or BBB filtering is applied to ingest events.

### Internal Signal

1. **I-Container gate** — Signals are processed through the I-Container service (`/process`, port 8015). Outputs with `within_bounds: false` or `dual_awareness: false` are flagged.
2. **Fifth DGM filter** — Internal learning outputs are evaluated against the Fifth DGM criteria before background store candidacy is established.

---

## 20.10 What First-Stage Evaluation Does Not Do

First-stage evaluation explicitly does not:

- Establish long-term patterns or identity-level knowledge — that is the role of Chapters 21 and 22.
- Guarantee deduplication — `ms_jarvis_memory` accumulates all passing interactions, including near-duplicates. Deduplication is a periodic maintenance operation (see Ch. 21 §21.6).
- Provide session continuity — the BBB and first-stage pipeline are stateless per interaction. Cross-session recall is an emergent behavior of the consciousness bridge `_get_url` read path, not a first-stage design feature (OI-05 — see Ch. 22 §22.9).
- Produce final GBIM updates — first-stage outputs are background store candidates. Promotion to GBIM tables in `msjarvisgis:5435` is a human-guided or consolidation-pass operation (see Ch. 21 §21.6 and Ch. 22).

---

## 20.11 Operational Scripts and Verification Commands

### Preflight Gate

```bash
bash scripts/preflight_gate.sh
```

Must pass all 9 checks before any `docker compose up`. Canonical source of truth for collection counts, key collection record counts, GBIM entity counts, and `jarvis-memory` auth health.

### Live Container Count

```bash
docker ps --filter "status=running" | wc -l
```

Expected: 109 as of April 13, 2026.

### ChromaDB Port Binding

```bash
docker port jarvis-chroma
```

Expected: `8000/tcp -> 0.0.0.0:8002`

### BBB Health and API

```bash
curl -s http://localhost:8016/ | python3 -m json.tool
curl -s http://localhost:8016/health
curl -s http://localhost:8016/stats
```

### Live Chat Schema

```bash
curl -s http://localhost:8050/chat \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $JARVIS_API_KEY" \
  -d '{"message":"test","userid":"carrieadmin","role":"carrieadmin","useallservices":false}' \
  | python3 -m json.tool
```

### jarvis-memory Auth Verification

```bash
curl -s http://localhost:8056/health
curl -s -H "Authorization: Bearer $JARVIS_API_KEY" \
  http://localhost:8056/memory/sessions
```

### msjarvisgis Live Counts

```bash
psql -h 127.0.0.1 -p 5435 -U postgres -d msjarvisgis \
  -c "SELECT count(*) AS public_tables FROM pg_tables WHERE schemaname='public';"

psql -h 127.0.0.1 -p 5435 -U postgres -d msjarvisgis \
  -c "SELECT count(*) AS all_tables FROM pg_tables;"

psql -h 127.0.0.1 -p 5435 -U postgres -d msjarvisgis \
  -c "SELECT pg_size_pretty(pg_database_size('msjarvisgis'));"
```

Expected as of April 13, 2026: 515 public tables, 742 total tables, 95 GB.

### I-Containers Health

```bash
curl -s http://localhost:8015/health | python3 -m json.tool
docker ps | grep jarvis-i-containers
```

Expected: `status: healthy`, `dual_awareness: true`, one container mapped `127.0.0.1:8015->8015/tcp`.

---

## 20.12 Port Reference Table (April 13, 2026)

| Service | Host Port | Container Port | Notes |
|---|---|---|---|
| main-brain (`/chat`) | 8050 | 8050 | Primary user interaction endpoint |
| ChromaDB | 8002 | 8000 | `jarvis-chroma`; `/api/v2/` only |
| BBB | 8016 | 8016 | `jarvis-blood-brain-barrier` |
| jarvis-memory | 8056 | 8056 | Secured; `/health` public |
| I-Containers | 8015 | 8015 | `127.0.0.1` binding; fully operational |
| autonomous-learner | 8020 | 8020 | Stale ref: 8425 |
| EEG band services | 8073, 8074, 8075 | — | — |
| gbim_query_router | 7205 | 7205 | PostgreSQL-native, no ChromaDB |
| msjarvisgis (GBIM + GIS) | 5435 | 5432 | `jarvis-local-resources-db`; authoritative GBIM |
| jarvis-msjarvis-db | 5433 | 5432 | External volume `msjarvis_pgdata`; offline for live GBIM |

---

*Last updated: 2026-04-13 by Carrie Kidd (Mamma Kidd), Mount Hope WV*

*April 13, 2026: Chapter anchored to live verified stack. 109 running containers confirmed. All hard-coded March 28 counts replaced with preflight gate references or dated live values. BBB API corrected — /check removed, /filter, /truth, /stats, /filter_output confirmed (§20.4). jarvis-memory API corrected — /events removed, /memory/turn, /memory/sessions, /memory/episodic, /memory/quest, /steg_report, /pia_window confirmed (§20.6). UltimateResponse canonical schema documented from live test — truthverdict nullable, top-level fields confirmed (§20.3). ChromaDB host port corrected to 8002 throughout (§20.5). msjarvisgis counts updated to live values: 515 public tables, 742 total tables, 95 GB (§20.7). memories table schema complete — 6 columns, 4 indexes (§20.7). I-Containers confirmed fully operational port 8015, dual_awareness: true — removed "future work" language throughout (§20.8). jarvis-msjarvis-db added to compose; msjarvis-pgdata-rescue retired (§20.7). All /api/v1/ Chroma references marked stale; /api/v2/ canonical (§20.5). preflight_gate.sh established as normative health check for all first-stage evaluation (§20.1, §20.11).*
