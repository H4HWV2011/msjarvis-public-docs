# 20. First-Stage Evaluation

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*

*Last updated: 2026-04-23*

*★ April 23, 2026: Container count updated to 100 (supersedes 109 from April 13 baseline); ChromaDB updated to 48 collections, ~6,740,611 vectors (supersedes 49 / 6,722,589+); msallisgis single-container replaced by two-container PostgreSQL split (production msallis-db host 5433, 16 GB, 294 tables, 11 schemas + forensic postgis-forensic host 5452, 17 GB, 314 tables); autonomous_learner gate updated to ≥ 23,200+ (grown ≈288/day from 21,181 April 13 baseline); OI-36-A CLOSED — Caddy forward_auth token enforcement now active at perimeter layer before main-brain port 8050; end-to-end processing_time updated to ~102.58s (GPU RTX 4070 benchmark); AAACPE ingest path updated — dedicated stack (allis-aaacpe-scraper:8048→8033 + allis-aaacpe-rag:8047→8032) supersedes legacy allis-ingest-api + allis-ingest-watcher for Appalachian cultural data.*

---

> **Live Stack Snapshot — April 23, 2026**
>
> All facts in this chapter are anchored to the live verified stack as of April 23, 2026, with **100 running containers** (from `docker ps --filter "status=running" | wc -l`).
>
> | Check | Value | Source |
> |---|---|---|
> | Running containers | 100 | `docker ps --filter "status=running" \| wc -l` |
> | ChromaDB collections | 48 | `preflight_gate.sh` |
> | ChromaDB port binding | host 8002 → container 8000 | `docker port allis-chroma` |
> | `autonomous_learner` records | ≥ 23,200+ | `preflight_gate.sh` |
> | `appalachian_cultural_intelligence` records | verify current | `preflight_gate.sh` |
> | `research_history` records | verify current | `preflight_gate.sh` |
> | `ms_allis_memory` records | verify current | `preflight_gate.sh` |
> | GBIM entities | verify current | `preflight_gate.sh` |
> | msallis-db (production) host port | 5433 | `psql -p 5433 -d msallis` |
> | msallis-db public tables | 294 | `SELECT count(*) FROM pg_tables WHERE schemaname='public'` |
> | msallis-db schemas | 11 | `SELECT count(*) FROM information_schema.schemata` |
> | msallis-db size | 16 GB | `SELECT pg_size_pretty(pg_database_size('msallis'))` |
> | postgis-forensic host port | 5452 | `psql -p 5452` |
> | postgis-forensic tables | 314 | `SELECT count(*) FROM pg_tables` |
> | postgis-forensic size | 17 GB | `SELECT pg_size_pretty(pg_database_size('postgres'))` |
> | BBB service | Up on :8016 | `curl http://localhost:8016/` |
> | allis-memory service | Up on :8056 | `curl -H "Authorization: Bearer $ALLIS_API_KEY" http://localhost:8056/health` |
> | I-Containers service | Up on :8015, dual_awareness: true | `curl http://localhost:8015/health` |
>
> These values are live and must be re-checked with the exact commands listed above for any future audit. Do not substitute hard-coded numbers from prior chapter revisions.

---

This chapter describes the first stage in the container paths — the evaluation layer that decides whether an incoming item is worth retaining at all, and in what initial form. Every user interaction, ingest event, and internal learning signal passes through this stage before anything is written to background storage, identity structures, or belief stores. The first stage does not establish long-term patterns; it filters, scores, and tags. What passes becomes a candidate for the background store described in Chapter 21.

---

## 20.1 Role of First-Stage Evaluation

First-stage evaluation serves as the system's primary admission gate. Its function is not to understand deeply but to decide quickly: is this item worth the cost of retention? The evaluation applies across three input classes:

- **User interactions** — messages arriving at the main-brain `/chat` endpoint (port 8050), routed through the LLM ensemble, BBB, and consciousness layers before a response is returned.
- **Ingest events** — documents arriving through the dedicated AAACPE stack (`allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`) for Appalachian cultural data, and similar external-source feeds. ★ The legacy `allis-ingest-api` + `allis-ingest-watcher` path is superseded for AAACPE ingest as of April 23, 2026.
- **Internal signals** — autonomous learning outputs, EEG band activity, and neurobiological processing results from the I-Container service (port 8015).

For each input class, first-stage evaluation produces a structured verdict that gates all downstream writes. Items that do not pass are dropped or held for human review. Items that pass are written to the background store and tagged for pattern accumulation (see Ch. 21).

First-stage evaluation is considered healthy only when `scripts/preflight_gate.sh` reports all of the following:

- 48 ChromaDB collections ★
- `autonomous_learner` ≥ 23,200+ records ★
- `appalachian_cultural_intelligence` — verify current ★
- `research_history` — verify current ★
- `ms_allis_memory` — verify current ★
- GBIM entities — verify current ★
- `allis-memory:8056` auth confirmed
- BBB `:8016` Up
- ★ Caddy `forward_auth` perimeter token enforcement active (OI-36-A CLOSED — see §20.2)

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

The `Authorization: Bearer $ALLIS_API_KEY` header is required at the service level. Requests without a valid key are rejected before first-stage evaluation begins.

★ **OI-36-A CLOSED — April 23, 2026:** Caddy `forward_auth` token enforcement is now active at the perimeter layer — bearer token validation occurs at the Caddy proxy before any request reaches main-brain port 8050. The `Authorization: Bearer $ALLIS_API_KEY` header requirement at the service level remains correct and unchanged; perimeter enforcement is Caddy-first as an additional layer.

### Ingest Path

External documents arrive through the dedicated AAACPE stack (`allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`) for Appalachian cultural data. ★ This dedicated stack supersedes the legacy `allis-ingest-api` + `allis-ingest-watcher` path for AAACPE ingest as of April 23, 2026. Documents are evaluated for domain relevance and structural quality before being written to `msallis_docs` or `autonomous_learner`. This path bypasses the LLM ensemble — the first-stage gate for ingest events is domain-relevance scoring, not BBB truth filtering.

### Internal Signal Path

Autonomous learning outputs, EEG band activity (ports 8073, 8074, 8075), and Fifth DGM filter results are evaluated against identity coherence thresholds before being surfaced to the background store. The I-Container service (port 8015) provides a live neurobiological processing gate for internal signals — outputs with `within_bounds: false` or `dual_awareness: false` are flagged before downstream writes.

---

## 20.3 The UltimateResponse: Canonical Output Schema

When a user interaction completes the full first-stage evaluation pipeline — routing, LLM ensemble (21 active / 22 registered; BakLLaVA eliminated, StarCoder2 excluded from scoring), BBB filtering, consciousness layers, and identity layers — the result is a structured `UltimateResponse`. The following is the canonical schema as directly observed from a live test call on April 13, 2026, with the `processing_time` field updated to the April 23, 2026 GPU RTX 4070 benchmark:

```json
{
  "response": "What do you need help with today?",
  "services_used": ["<service list>"],
  "consciousness_level": "ultimate_collective",
  "processing_time": 102.58,
  "architecture_layers": 9,
  "truthverdict": null
}
```

**Field notes:**

- `response` — The final text response returned to the user.
- `services_used` — Array of service identifiers that contributed to the response. Populated from the LLM ensemble and routing layer.
- `consciousness_level` — String label reflecting the highest consciousness layer reached. `"ultimate_collective"` is the current production value.
- `processing_time` — Float, seconds. ★ Updated to ~102.58s as of the April 23, 2026 GPU RTX 4070 benchmark (supersedes the April 13 value of 144.02s, which reflected CPU-only full 9-layer processing at prior ensemble scale).
- `architecture_layers` — Integer. Currently 9. Reflects the number of active processing layers traversed.
- `truthverdict` — Present in all `UltimateResponse` objects but **nullable**. Null when the BBB filter did not produce a definitive verdict for the specific interaction. When non-null, carries the BBB truth assessment from `allis-blood-brain-barrier:8016`. Do not treat null as an error — it is a valid and expected value for many interaction types.

Fields such as `validated_by` and `consensus_score` do not appear at the top level of the current `UltimateResponse` schema. Do not reference them as top-level fields in any script or downstream consumer.

---

## 20.4 The Blood-Brain Barrier (BBB)

The BBB service (`allis-blood-brain-barrier`, port 8016) is the primary truth and safety filter in the first-stage evaluation pipeline. It is confirmed Up as of April 13, 2026. Its root endpoint returns:

```json
{
  "service": "Ms. Allis Blood-Brain Barrier",
  "filters": ["<active filter list>"]
}
```

★ **OI-36-A CLOSED — April 23, 2026:** Caddy `forward_auth` token enforcement is active at the perimeter layer before any request reaches main-brain port 8050. The BBB `/filter` and `/truth` pipeline operates unchanged at the service level; perimeter enforcement is Caddy-first as an additional layer. All BBB gate decisions continue to be durably persisted to `allis-memory:8056`.

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

The BBB verdict is attached as `truthverdict` on every `UltimateResponse`. It is nullable (see §20.3). All BBB filtering decisions are durably persisted to `allis-memory:8056` (secured March 28, 2026) — the audit trail is not ephemeral.

---

## 20.5 ChromaDB as First-Stage Write Target

ChromaDB is served via `allis-chroma` on **host port 8002** (mapped to container port 8000). All first-stage background writes go through this binding. Direct references to `localhost:8000` as a host port are stale — the correct host-side address is `localhost:8002`.

★ All **48** active ChromaDB collections (~6,740,611 total vectors) are 384-dim using `all-minilm:latest`. No other embedding model may be used — `nomic-embed-text` produces 768-dim vectors and is incompatible with all existing collections (see Ch. 19 §19.8.8a and Ch. 21 §21.2).

### ChromaDB API

All shell-based commands must use the v2 API path. The v1 path (`/api/v1/`) is permanently removed in Chroma server 1.0.0:

```bash
# CORRECT — Chroma 1.0.0+
curl http://localhost:8002/api/v2/tenants/default_tenant/databases/default_database/collections

# STALE — do not use
curl http://localhost:8002/api/v1/collections
```

The Python `chromadb` client library (version 1.5.5) handles the v1 → v2 migration transparently. Only raw `curl` commands and scripts constructing HTTP requests directly are affected.

When a `/chat` call completes, the `background_rag_store` task writes a new record to `ms_allis_memory` (UUID: `79240788-0828-45f3-b1bc-a9a3593628a6`) via this binding. Every successful interaction produces exactly one new background record. The collection count must be verified by UUID — see Ch. 22 §22.10 for UUID preservation risk.

---

## 20.6 The `allis-memory` Audit Layer

`allis-memory` (port 8056) provides durable, authenticated storage for first-stage filtering decisions. It is secured: `0.0.0.0` corrected to `127.0.0.1`, `_auth()` confirmed on all sensitive routes, `ALLIS_API_KEY` required.

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

★ **April 23, 2026 — Two-Container PostgreSQL Split.** The single-container `msallisgis` on port 5435 has been replaced by a two-container production architecture. All references to `msallisgis:5435` as the authoritative GBIM and GIS store are superseded. The two production containers are:

### msallis-db — Production Instance (host port 5433)

The production PostGIS instance. All live GIS and GBIM production queries route here.

| Metric | Value | Command |
|---|---|---|
| Public tables | 294 | `SELECT count(*) FROM pg_tables WHERE schemaname='public'` |
| Schemas | 11 | `SELECT count(*) FROM information_schema.schemata` |
| Database size | 16 GB | `SELECT pg_size_pretty(pg_database_size('msallis'))` |

These are live values and must be re-checked with the same commands for future audits.

Key GBIM tables (★ row counts are verify-current — GBIM corpus has grown since April 13):

| Table | Rows (April 13 baseline) | Notes |
|---|---|---|
| `gbim_worldview_entity` | ~5,415,896+ | Primary GBIM entity table — verify current ★ |
| `gbim_graph_edges` | ~15,226,626+ | verify current ★ |
| `gbimbeliefnormalized` | ~6,804,671+ | verify current ★ |
| `gbim_attrs` | ~5,491,092+ | verify current ★ |
| `gbim_beliefs` | ~3,747,712+ | verify current ★ |
| `gbim_evidence` | ~2,121,228+ | verify current ★ |
| `gbim_belief_evidence` | ~2,121,130+ | verify current ★ |
| `gbim_full_points_raw` | ~1,389,855+ | verify current ★ |
| `mvw_gbim_landowner_spatial` | ~20,593+ | Landowner beliefs — verify current ★ |
| `memories` | 3 | Promotion/linkage table — see Ch. 21 §21.2 |

The `memories` table carries the full promotion and linkage schema: `gbim_entity_id` (BIGINT, B-tree index), `spatial_ref` (geometry(Point,4326), GIST index), `reviewed` (BOOLEAN, partial index), `promoted` (BOOLEAN, partial index), `source` (TEXT), `chroma_id` (TEXT). These six columns and four indexes were applied cleanly on April 13, 2026.

The `gbim_query_router` (port 7205) landowner path is a fully deterministic PostgreSQL-native path with no ChromaDB interaction.

### postgis-forensic — Forensic Instance (host port 5452)

The forensic PostGIS instance. Used for forensic analysis and verification; not the live GBIM query target.

| Metric | Value | Command |
|---|---|---|
| Total tables | 314 | `SELECT count(*) FROM pg_tables` |
| Database size | 17 GB | `SELECT pg_size_pretty(pg_database_size('postgres'))` |

> **Note on prior §20.7 msallisgis (port 5435):** The single-container `msallisgis:5435` (`allis-local-resources-db`) is retired as the authoritative GBIM/GIS container. The April 13 values (515 public tables, 742 total tables, 95 GB) reflected that single-container state and are superseded by the two-container split above. Do not use port 5435 as the live GBIM query target.

---

## 20.8 I-Containers and Identity Layer Interface

The I-Container service (`ms_allis_i_containers_service.py`, port 8015) is fully operational as of April 13, 2026. It is not future work.

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

One `allis-i-containers` container is confirmed running, mapped `127.0.0.1:8015 → 8015/tcp`.

The service imports all 10 neurobiological modules directly — it is its own NBB backend. The adapter (`allis-i-containers_icontainers_fastapi.py`) proxies to this service; "NBB backend not reachable" in adapter logs is expected and irrelevant.

**Module inventory:**

- I-Container 1 (Self Model): `SelfRecognition`, `IdentityCore`, `PersonalNarrative`, `EgoBoundaries`, `MemorySelf`
- I-Container 2 (Observer/Witness): `WitnessConsciousness`, `ReflectionSystem`, `IntrospectionEngine`, `MetacognitiveAwareness`, `ObserverSelf`

First-stage evaluation feeds into the I-Container layer indirectly: completed interactions are written to `ms_allis_memory`, which the consciousness bridge's `_get_url` read path surfaces across sessions (OI-05 — see Ch. 22 §22.9). This means the I-Container layer is receiving a continuous feed of evaluated, retained interactions and is already contributing to identity trajectory — this is not a future integration milestone.

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

1. **Perimeter authentication** — ★ Caddy `forward_auth` token enforcement (OI-36-A CLOSED) validates the bearer token at the proxy before the request reaches main-brain port 8050.
2. **Service authentication** — `ALLIS_API_KEY` must be present and valid at the service level. No evaluation proceeds without it.
3. **BBB `/filter`** — Content is evaluated against the BBB's active filter list. Items failing the filter are blocked before LLM ensemble processing.
4. **LLM ensemble scoring** — 21 active proxies (22 registered; BakLLaVA eliminated, StarCoder2 excluded from scoring) produce a consensus response. Routing, ensemble weighting, and identity layer processing are applied.
5. **BBB `/truth`** — Truth assessment is applied to the candidate response. The result is attached as `truthverdict` on the `UltimateResponse`. Nullable — a null verdict is valid and does not constitute a failed evaluation.
6. **BBB `/filter_output`** — Output-stage filtering is applied to the final response before delivery.
7. **Background write** — If all stages complete, `background_rag_store` writes one record to `ms_allis_memory` and the BBB audit event is persisted to `allis-memory:8056` via `/memory/turn`.

### Ingest Event

1. **Domain relevance scoring** — Document is evaluated against target domain criteria (community resource relevance, structural quality).
2. **Direct write** — Documents passing relevance scoring are written directly to `msallis_docs` or `autonomous_learner` with metadata `services: ["aappcappe-ingest"]` and `type: "community_resource"`. No LLM ensemble or BBB filtering is applied to ingest events. ★ AAACPE ingest now routes through the dedicated stack (`allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`).

### Internal Signal

1. **I-Container gate** — Signals are processed through the I-Container service (`/process`, port 8015). Outputs with `within_bounds: false` or `dual_awareness: false` are flagged.
2. **Fifth DGM filter** — Internal learning outputs are evaluated against the Fifth DGM criteria before background store candidacy is established.

---

## 20.10 What First-Stage Evaluation Does Not Do

First-stage evaluation explicitly does not:

- Establish long-term patterns or identity-level knowledge — that is the role of Chapters 21 and 22.
- Guarantee deduplication — `ms_allis_memory` accumulates all passing interactions, including near-duplicates. Deduplication is a periodic maintenance operation (see Ch. 21 §21.6).
- Provide session continuity — the BBB and first-stage pipeline are stateless per interaction. Cross-session recall is an emergent behavior of the consciousness bridge `_get_url` read path, not a first-stage design feature (OI-05 — see Ch. 22 §22.9).
- Produce final GBIM updates — first-stage outputs are background store candidates. Promotion to GBIM tables in the production `msallis-db:5433` instance is a human-guided or consolidation-pass operation (see Ch. 21 §21.6 and Ch. 22). ★ Note: prior references to `msallisgis:5435` as the promotion target are superseded by the two-container split (§20.7).

---

## 20.11 Operational Scripts and Verification Commands

### Preflight Gate

```bash
bash scripts/preflight_gate.sh
```

Must pass all 9 checks before any `docker compose up`. Canonical source of truth for collection counts, key collection record counts, GBIM entity counts, and `allis-memory` auth health. ★ Update `preflight_gate.sh` to reflect: 48 ChromaDB collections; `autonomous_learner` ≥ 23,200+; production DB at `msallis-db:5433` (294 tables, 11 schemas) + forensic at `postgis-forensic:5452` (314 tables).

### Live Container Count

```bash
docker ps --filter "status=running" | wc -l
```

Expected: **100** as of April 23, 2026. ★

### ChromaDB Port Binding

```bash
docker port allis-chroma
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
  -H "Authorization: Bearer $ALLIS_API_KEY" \
  -d '{"message":"test","userid":"carrieadmin","role":"carrieadmin","useallservices":false}' \
  | python3 -m json.tool
```

### allis-memory Auth Verification

```bash
curl -s http://localhost:8056/health
curl -s -H "Authorization: Bearer $ALLIS_API_KEY" \
  http://localhost:8056/memory/sessions
```

### Production PostgreSQL Live Counts (★ updated — two-container split)

```bash
# Production instance — msallis-db host 5433
psql -h 127.0.0.1 -p 5433 -U postgres -d msallis \
  -c "SELECT count(*) AS public_tables FROM pg_tables WHERE schemaname='public';"

psql -h 127.0.0.1 -p 5433 -U postgres -d msallis \
  -c "SELECT count(*) AS schemas FROM information_schema.schemata;"

psql -h 127.0.0.1 -p 5433 -U postgres -d msallis \
  -c "SELECT pg_size_pretty(pg_database_size('msallis'));"

# Expected: 294 public tables, 11 schemas, 16 GB

# Forensic instance — postgis-forensic host 5452
psql -h 127.0.0.1 -p 5452 -U postgres \
  -c "SELECT count(*) AS all_tables FROM pg_tables;"

psql -h 127.0.0.1 -p 5452 -U postgres \
  -c "SELECT pg_size_pretty(pg_database_size('postgres'));"

# Expected: 314 tables, 17 GB
```

### I-Containers Health

```bash
curl -s http://localhost:8015/health | python3 -m json.tool
docker ps | grep allis-i-containers
```

Expected: `status: healthy`, `dual_awareness: true`, one container mapped `127.0.0.1:8015->8015/tcp`.

---

## 20.12 Port Reference Table (April 23, 2026)

| Service | Host Port | Container Port | Notes |
|---|---|---|---|
| main-brain (`/chat`) | 8050 | 8050 | Primary user interaction endpoint; ★ Caddy forward_auth active at perimeter (OI-36-A CLOSED) |
| ChromaDB | 8002 | 8000 | `allis-chroma`; `/api/v2/` only; ★ 48 collections |
| BBB | 8016 | 8016 | `allis-blood-brain-barrier` |
| allis-memory | 8056 | 8056 | Secured; `/health` public |
| I-Containers | 8015 | 8015 | `127.0.0.1` binding; fully operational |
| autonomous-learner | 8020 | 8020 | Stale ref: 8425 |
| EEG band services | 8073, 8074, 8075 | — | — |
| gbim_query_router | 7205 | 7205 | PostgreSQL-native, no ChromaDB |
| AAACPE scraper | 8033 | 8033 | `allis-aaacpe-scraper`; host 8048→8033 ★ |
| AAACPE RAG | 8032 | 8032 | `allis-aaacpe-rag`; host 8047→8032 ★ |
| msallis-db (production) | 5433 | 5432 | Production PostGIS; 16 GB, 294 tables, 11 schemas ★ |
| postgis-forensic | 5452 | 5432 | Forensic PostGIS; 17 GB, 314 tables ★ |

> ★ **Retired:** `msallisgis (port 5435)` / `allis-local-resources-db` — superseded by two-container split above. Do not use port 5435 as the live GBIM/GIS query target.

---

*Last updated: 2026-04-23 by Carrie Kidd (Mamma Kidd), Mount Hope WV*

*★ April 23, 2026: Container count updated to 100 (supersedes 109 April 13 baseline). ChromaDB updated to 48 collections, ~6,740,611 vectors (supersedes 49 / 6,722,589+). Two-container PostgreSQL split: production msallis-db host 5433 (16 GB, 294 tables, 11 schemas) + forensic postgis-forensic host 5452 (17 GB, 314 tables) — supersedes single-container msallisgis:5435. autonomous_learner gate updated to ≥ 23,200+ (grown ≈288/day from 21,181 April 13 baseline). GBIM entity counts marked verify-current. OI-36-A CLOSED — Caddy forward_auth token enforcement active at perimeter layer before main-brain port 8050 (§20.2, §20.4, §20.9, §20.12). processing_time updated to ~102.58s GPU RTX 4070 benchmark (§20.3). AAACPE ingest path updated — dedicated stack (allis-aaacpe-scraper:8048→8033 + allis-aaacpe-rag:8047→8032) supersedes legacy allis-ingest-api + allis-ingest-watcher (§20.1, §20.2, §20.9, §20.12). preflight_gate.sh gate conditions updated (§20.1, §20.11). Port reference table updated with AAACPE stack ports and two-container DB split; port 5435 retired (§20.12).*

*April 13, 2026: Chapter anchored to live verified stack. 109 running containers confirmed. All hard-coded March 28 counts replaced with preflight gate references or dated live values. BBB API corrected — /check removed, /filter, /truth, /stats, /filter_output confirmed (§20.4). allis-memory API corrected — /events removed, /memory/turn, /memory/sessions, /memory/episodic, /memory/quest, /steg_report, /pia_window confirmed (§20.6). UltimateResponse canonical schema documented from live test — truthverdict nullable, top-level fields confirmed (§20.3). ChromaDB host port corrected to 8002 throughout (§20.5). msallisgis counts updated to live values: 515 public tables, 742 total tables, 95 GB (§20.7). memories table schema complete — 6 columns, 4 indexes (§20.7). I-Containers confirmed fully operational port 8015, dual_awareness: true — removed "future work" language throughout (§20.8). allis-msallis-db added to compose; msallis-pgdata-rescue retired (§20.7). All /api/v1/ Chroma references marked stale; /api/v2/ canonical (§20.5). preflight_gate.sh established as normative health check for all first-stage evaluation (§20.1, §20.11).*
