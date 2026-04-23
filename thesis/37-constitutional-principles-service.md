# Chapter 37 — Constitutional Principles Service and Governance Layer

**Carrie Kidd (Mamma Kidd) · Mount Hope, WV**
**Last updated: ★ 2026-04-23**
**★ 100 containers Up (April 23, 2026) (zero Restarting, zero Exited). Constitutional guardian Up, healthy, `/health` returning PostgreSQL connection fields. Audit log writing (6.7K+, `cakidd`-owned). All Chapter 37 OIs remain CLOSED. PostgreSQL two-container split active (April 23): `production msallis-db host 5433` (16 GB, 294 tables, 11 schemas) + `forensic postgis-forensic host 5452` (17 GB, 314 tables) — supersedes `msallis:5433` + `gisdb / msallisgis:5432` April 6 entries. Caddy `forward_auth` (OI-36-A CLOSED) confirmed active: HTTP 401 before port 8050 is the outermost gate. `allis-memory:8056` 8 endpoints fully mapped, survives restarts. ChromaDB: 48 collections / ~6,740,611 total vectors. `post-start.sh` startup sequence required after every stack restart.**

---

> **SEALED STATUS BLOCK (★ April 23, 2026 — supersedes April 6)**
>
> - **System baseline:** ★ **100 containers Up** (zero Restarting, zero Exited) — April 23, 2026 ground truth. Supersedes 105/105 April 6 baseline.
> - **Guardian state:** `allis-constitutional-guardian` Up and healthy; `/health` returns PostgreSQL GBIM and GeoDB connection fields and reports `status: "healthy"`. ★ Verify field names current after April 23 two-container split (see §37.2).
> - **Constitution version:** `2026-02-17.2-USC` active.
> - **Audit log:** `data/constitutional_audit/constitutional_audit.jsonl` actively writing, 6.7K+ entries, `cakidd`-owned. Durable audit also in `allis-memory:8056` (★ 8 endpoints fully mapped — `/steg_report`, `/pia_window`, `/memory/turn`, `/memory/get`, `/memory/sessions`, `/memory/session/{id}`, `/memory/quest*`, `/memory/episodic/{id}`; survives container restarts).
> - **All Chapter 37 Open Items remain CLOSED.**
>   - OI-37-A — gateway exposes `/constitutional/*` correctly with `carrie_admin` enforcement active.
>   - OI-37-B — `/health` includes PostgreSQL liveness fields for both stores. ★ Verify field names after April 23 split.
>   - OI-38-A — token enforcement middleware active at gateway.
> - **★ PostgreSQL two-container split (April 23, 2026 — supersedes April 6):**
>   - `production msallis-db` → host **5433** ★ — 16 GB, 294 tables, 11 schemas; GBIM entities with `confidence_decay` metadata; ~288/day growth from `autonomous_learner`; **supersedes `msallis:5433` — 5,416,521 entities / 45 GB April 6 entry**
>   - `forensic postgis-forensic` → host **5452** ★ — 17 GB, 314 tables (PostGIS geometry); **supersedes `gisdb / msallisgis` host `5432` / compose-internal `5452` — 45 GB / 548 tables April 6 entry**
>   - All Guardian compose environment variables, watchdog scripts, and `/health` field references must target these two containers. See §37.2 port callout (★ updated April 23).
> - **★ Caddy `forward_auth` (OI-36-A CLOSED — confirmed April 23):** HTTP 401 before port 8050 is the zero-th gate, outermost layer. Cannot be removed by any sprint decision, governance vote, or spiritual governance layer. Every nightly swarm audit verifies this as its first check (Ch 35 §35.7).
> - **★ ChromaDB (April 23 ground truth): 48 collections / ~6,740,611 total vectors.** Host port **8002**; `/api/v2/` only; `chromadb/chroma:0.6.3`. Supersedes April 6 — 47 collections / 6,722,589 vectors.
> - **`local_resources` (April 23):** 207 items / all 55 WV counties — `allis-local-resources-db:5435` — full 55-county coverage; geographic completeness baseline for `10a-community-sovereignty` principle validation.
> - **EEG Delta PIA heartbeat (port 8073):** `pulse_count: 12,860+`; stalled pulse is a governance-level alert.
> - **Sprint-3 constitutional guardian log remains clean.** No new commits required for April 23 update; all changes are ground-truth supersessions of PostgreSQL connection targets and container counts.
>
> **What this header is NOT:** It is not a live status indicator. It is the sealed April 23, 2026 snapshot of the stack and guardian after the two-container PostgreSQL split, with all Chapter 37 OIs confirmed closed.

---

## Why This Matters for Polymathmatic Geography

This chapter describes the Constitutional Guardian service that provides constitutional compliance checking grounded in the United States Constitution and validated against `production msallis-db:5433` ★ (16 GB, 294 tables, 11 schemas — GBIM entities with `confidence_decay` metadata; ~288/day growth) and `forensic postgis-forensic:5452` ★ (17 GB, 314 PostGIS tables) for geospatial community boundary validation. It supports:

- **P1 – Every where is entangled** by ensuring that constitutional protections propagate through all services and paths, from Caddy `forward_auth` perimeter (OI-36-A CLOSED) to gateway to barrier to consciousness layers, all grounded in `production msallis-db:5433` ★ GBIM community knowledge with temporal confidence grading (`confidence_decay` metadata; ~288/day growth from `autonomous_learner`).
- **P3 – Power has a geometry** by making constitutional authority the highest architectural layer — explicitly documented, versioned, audited, and queryable — rather than hiding governance rules in opaque code. Constitutional gate decisions are durably logged in both a persistent `.jsonl` file and `allis-memory:8056` (8 endpoints, survives restarts), making enforcement history independently inspectable via `/memory/turn` and `/steg_report`.
- **P5 – Design is a geographic act** by treating constitutional principles as designed artifacts that encode community sovereignty (10th Amendment) and anti-extraction protections for Appalachian communities, validated against `forensic postgis-forensic:5452` ★ PostGIS boundaries (17 GB, 314 tables) with ZIP-code-level community precision. `local_resources` (207 items / all 55 WV counties) is the completeness substrate for `10a-community-sovereignty` validation.
- **P12 – Intelligence with a ZIP code** by grounding equal protection (14th Amendment) and community sovereignty (10th Amendment) principles in West Virginia-specific contexts validated against `production msallis-db:5433` ★ GBIM and `forensic postgis-forensic:5452` ★ geodata.
- **P16 – Power accountable to place** by maintaining a persistent audit log of every constitutional decision, making all blocks, allows, and principle applications queryable and transparent to communities, and by tying enforcement to PostgreSQL-backed identity and geography that is itself growing and entangled with Appalachian reality at ~288 GBIM entities/day.

As such, this chapter belongs to the **Computational Instrument tier**: it specifies the Constitutional Guardian as an independently testable, PostgreSQL-grounded, audit-logged authority service.

---

```text
┌─────────────────────────────────────────────────────────────┐
│   Constitutional Guardian Architecture                      │
│   ★ April 23, 2026                                         │
│   ★ 100 containers Up — zero Restarting, zero Exited       │
│   ★ Guardian: Up, healthy, /health with PostgreSQL fields  │
│   ★ Caddy forward_auth: HTTP 401 outermost gate (OI-36-A)  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Caddy forward_auth perimeter (zero-th gate)               │
│  - HTTP 401 before port 8050 on unauthenticated /chat      │
│  - OI-36-A CLOSED; cannot be removed                       │
│      ↓                                                      │
│  Constitutional Authority Hierarchy                         │
│  ┌────────────────────────────────────────────────┐        │
│  │  HIGHEST: Constitutional Guardian (8091)       │        │
│  │  WORKDIR: /app (Dockerfile.constitutional_     │        │
│  │    guardian — -w /app/services is WRONG)       │        │
│  │  Foundation: U.S. Constitution                 │        │
│  │  -  Amendment I (speech, religion, assembly)   │        │
│  │  -  Amendment IV (privacy, security)           │        │
│  │  -  Amendment V (due process, property)        │        │
│  │  -  Amendment XIV (equal protection)           │        │
│  │  -  General Welfare (Art. I §8, Preamble)      │        │
│  │  -  Amendment X (community sovereignty)        │        │
│  │                                                │        │
│  │  6 Principle Groups, 15+ Specific Principles  │        │
│  │  API version: 2.1.0-USC-Audit (compose label) │        │
│  │  Constitution version: 2026-02-17.2-USC        │        │
│  │  GBIM: production msallis-db (★ host 5433)    │        │
│  │    - 16 GB, 294 tables, 11 schemas             │        │
│  │    - confidence_decay; ~288/day growth         │        │
│  │  GeoDB: forensic postgis-forensic (★ host 5452)│        │
│  │    - 17 GB, 314 PostGIS tables                 │        │
│  │    - supersedes gisdb:5432 / msallisgis April 6│        │
│  └────────────────────────────────────────────────┘        │
│      ↓                                                      │
│  Defense-in-Depth Integration                              │
│  ┌────────────────────────────────────────────────┐        │
│  │  Level 1: Unified Gateway (8050)               │        │
│  │  -  Checks Guardian first                      │        │
│  │  -  Block-before-BBB if violation              │        │
│  │  -  Exposes /constitutional/* via fresh image  │        │
│  │    (OI-37-A CLOSED)                            │        │
│  └────────────────────────────────────────────────┘        │
│      ↓                                                      │
│  ┌────────────────────────────────────────────────┐        │
│  │  Level 2: Blood-Brain Barrier (8016)           │        │
│  │  -  Checks Guardian first                      │        │
│  │  -  If blocked → skip all six filters          │        │
│  │  -  If allowed → six filters (all confirmed    │        │
│  │     responding April 23):                      │        │
│  │    - EthicalFilter (0% FP, Apr 2)              │        │
│  │    - SpiritualFilter ★                         │        │
│  │    - SafetyMonitor (survivor-safe, Apr 3) ★    │        │
│  │    - ThreatDetection                           │        │
│  │    - steganography_filter ★ (live catch logged)│        │
│  │    - truth_verification (rag_grounded_v2)      │        │
│  │  Phase 4.5 output: log+passthrough             │        │
│  │  - 31% FP eliminated; blocking re-enable       │        │
│  │    is next-session/red-team decision           │        │
│  │  All gate decisions → allis-memory:8056        │        │
│  │    (8 endpoints; /steg_report for adv. events) │        │
│  └────────────────────────────────────────────────┘        │
│      ↓                                                      │
│  Core API Endpoints                                        │
│  -  POST /constitutional/check                             │
│  -  GET  /constitutional/status                            │
│  -  GET  /constitutional/principles                        │
│  -  GET  /constitutional/versions                          │
│  -  GET  /constitutional/audit                             │
│  -  GET  /constitutional/audit/stats                       │
│  -  GET  /constitutional/transparency                      │
│      ↓                                                      │
│  Persistent Audit Log                                      │
│  ⚠ mkdir -p data/constitutional_audit BEFORE compose up    │
│  -  Host: data/constitutional_audit/                       │
│         constitutional_audit.jsonl                         │
│  -  Container: /app/audit/constitutional_audit.jsonl       │
│  -  6.7K+, cakidd-owned, writing                           │
│  -  JSON Lines; one decision per line                      │
│  -  Survives restarts (bind mount)                         │
│  -  All events also → allis-memory:8056                    │
│    (8 endpoints; /memory/turn primary; survives restarts)  │
│      ↓                                                      │
│  Role-Specific Enforcement                                 │
│  -  external_corporation: STRICTEST (10a-no-extraction)    │
│  -  community_member: STANDARD                             │
│  -  user/admin/system: tiered + logged                     │
│      ↓                                                      │
│  PostgreSQL Integration (★ April 23 two-container split)   │
│  -  production msallis-db (host 5433) ★: GBIM +           │
│       confidence_decay; 16 GB / 294 tables                 │
│  -  forensic postgis-forensic (host 5452) ★:               │
│       PostGIS geometry; 17 GB / 314 tables                 │
│  -  allis-local-resources-db (host 5435):                  │
│       local_resources 207 items / 55 WV counties           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Figure 37.1.** Constitutional Guardian architecture (★ April 23, 2026): Caddy `forward_auth` perimeter (OI-36-A CLOSED) as zero-th gate; constitutional authority as highest layer; gateway and BBB both checking the guardian first; six-filter BBB (EthicalFilter 0% FP April 2; SpiritualFilter ★; SafetyMonitor survivor-safe April 3 ★; steganography_filter ★ live catch logged; `truth_verification` now `rag_grounded_v2` per OI-37-C); Phase 4.5 log+passthrough; dual PostgreSQL integration (★ `production msallis-db:5433` GBIM — 16 GB, 294 tables; ★ `forensic postgis-forensic:5452` PostGIS — 17 GB, 314 tables — supersedes `msallis:5433` + `gisdb:5432` April 6 entries); `allis-memory:8056` 8-endpoint durable audit; OI-37-A CLOSED (gateway routing); OI-37-B CLOSED (PostgreSQL `/health` fields — ★ verify field names after split). See §37.5.5 for OI closure verification table.

---

## Status Table — ★ April 23, 2026

| Category | Details |
|:--|:--|
| **Implemented** | `allis-constitutional-guardian` running at `127.0.0.1:8091`, healthy. FastAPI with CORS. WORKDIR `/app`. Constitution version `2026-02-17.2-USC` active; API service version `2.1.0-USC-Audit`. BBB wired to consult Guardian first; unified gateway wired to Guardian before BBB; Caddy `forward_auth` (OI-36-A CLOSED) is the zero-th gate before gateway. All `/constitutional/*` routes proxied through the gateway with token enforcement middleware active — OI-37-A CLOSED. Persistent `.jsonl` audit log + durable audit in `allis-memory:8056` (8 endpoints, survives restarts). `/health` returns PostgreSQL liveness fields — OI-37-B CLOSED (★ verify field names current after April 23 split). Production startup: `docker compose up -d && bash scripts/post-start.sh`. ★ PostgreSQL split: `production msallis-db:5433` ★ (GBIM) + `forensic postgis-forensic:5452` ★ (PostGIS). |
| **Partially implemented / scaffolded** | Multi-signature principle amendment workflow. Community consultation process. Real-time dashboards and external reporting. Automated `confidence_decay`-aware GBIM validation pipeline (OI-38-B). Full alert wiring for Exited/Created state detection (patterns documented; alert delivery to external systems is future work). Phase 4.5 blocking re-enablement pending red-team sign-off. |
| **Future work / design intent only** | ML-based pattern detection for constitutional violations. Exporting audit traces to partner compliance systems. Time-series constitutional enforcement analytics in PostgreSQL. Governance UI for reviewing and annotating audit records. Formal session contracts tightly binding gateway, BBB, and Guardian changes for cooperative oversight. |

---

## 37.1 Purpose and Constitutional Foundation

The Constitutional Guardian is the highest authority in Ms. Allis's governance hierarchy. It is grounded in the United States Constitution and backed by `production msallis-db:5433` ★ (16 GB, 294 tables, 11 schemas — GBIM entities with `confidence_decay` metadata; ~288/day growth) and `forensic postgis-forensic:5452` ★ (17 GB, 314 PostGIS tables) rather than ad-hoc rules. It is fronted by the Caddy `forward_auth` perimeter (OI-36-A CLOSED) as the zero-th gate.

**Legal foundation:**

- First Amendment: speech, religion, assembly, petition
- Fourth Amendment: privacy and security
- Fifth Amendment: due process and property
- Fourteenth Amendment: equal protection and due process, validated via GBIM and geodata
- General Welfare clause and Preamble
- Tenth Amendment: community sovereignty and reserved powers, validated against ZCTA-level geography in `forensic postgis-forensic:5452` ★

**Operational role:**

- Acts as **pre-filter** for all actions the system takes or allows, behind Caddy `forward_auth` (OI-36-A CLOSED)
- Provides a shared, explicit set of constitutional principles with documented origins
- Writes every decision to an audit log plus durable memory (`allis-memory:8056` — 8 endpoints)
- Reveals how power is applied to community data and geography

---

## 37.2 Implementation as a Dedicated Service

The Guardian is a dedicated FastAPI container built from `services/Dockerfile.constitutional_guardian` and running `constitutional_api_fixed.py`. It is **only** supported when started via `docker compose`, not via standalone `docker run`.

**Key implementation facts:**

- Container name: `allis-constitutional-guardian`
- Port: 8091 (bound to `127.0.0.1`)
- Compose network: `qualia-net` (runtime: `msallis-rebuild_qualia-net`)
- WORKDIR: `/app` (set in Dockerfile)
- Principles file: `/app/constitutional_principles.json` (host: `./services/constitutional_principles.json`)
- Audit directory: `/app/audit` (host: `./data/constitutional_audit`)
- PostgreSQL integration (★ April 23 two-container split):
  - GBIM: `production msallis-db` → compose DNS `postgresql` → host **5433** ★ (16 GB, 294 tables, 11 schemas; `confidence_decay` metadata)
  - GeoDB: `forensic postgis-forensic` → container-internal **5452** ★ (17 GB, 314 PostGIS tables) — see port callout below

**Network root cause and fix (Sprint 3 — still applies April 23):**

- **Root cause:** `msallis-pgdata-rescue` was running standalone, not on the compose network. From inside containers, `172.18.0.1:5433` was unreachable, and `postgresql` DNS resolved to the wrong instance.
- **Fix:** Use `docker network connect` to attach `msallis-pgdata-rescue` to the compose project network. The Guardian reaches GBIM at `postgresql:5433` on the compose network and verifies via host-side `psql` at `localhost:5433`. ★ After April 23 split, `production msallis-db` is the GBIM container; confirm it is attached to `msallis-rebuild_qualia-net`.

**Gateway build context drift and fix (Sprint 3):**

- **Root cause:** The unified gateway was building from a stale external path instead of `./services/`.
- **Fix:** Commit `af76b479` changed the gateway's build context to `./services/` and ensured all routes (including `/constitutional/*`) are included.

---

> **★ PORT CALLOUT — Updated April 23, 2026 (two-container PostgreSQL split)**
>
> | Reference | Port | Container | Context |
> |:--|:--|:--|:--|
> | `GBIM_POSTGRESQL_PORT` in compose env | **5433** ★ | `production msallis-db` | GBIM — 16 GB, 294 tables, 11 schemas; `confidence_decay` metadata; ~288/day growth; host-side psql: `localhost:5433` |
> | `POSTGRESQL_PORT` in compose env | **5452** ★ | `forensic postgis-forensic` | PostGIS geometry — 17 GB, 314 tables; container-internal port used by Guardian inside Docker network |
> | Host-side `psql` / external tools for PostGIS | **5452** ★ | `forensic postgis-forensic` | ★ **Supersedes host port `5432` / `gisdb` / `msallisgis` April 6 entries** |
>
> **Do not change `POSTGRESQL_PORT` from `5452` in the compose file for `forensic postgis-forensic`.** The 5452/5452 mapping is intentional after the April 23 split — both internal and host port are now 5452 for the forensic container. Verify with `docker port forensic-postgis-forensic` after every restart.
>
> ★ **Prior references to host port `5432` for `gisdb` or `msallisgis` are superseded as of April 23, 2026.** Any compose environment variable, watchdog script, or health-check command still targeting `gisdb:5432` or `msallisgis:5452` (with the old container name) must be updated to `forensic postgis-forensic:5452` ★.

---

**Compose configuration (★ April 23 — updated for two-container split):**

```yaml
allis-constitutional-guardian:
  build:
    context: ./services
    dockerfile: Dockerfile.constitutional_guardian
  container_name: allis-constitutional-guardian
  ports:
    - "127.0.0.1:8091:8091"
  volumes:
    - ./services/constitutional_principles.json:/app/constitutional_principles.json:ro
    - ./data/constitutional_audit:/app/audit
  networks:
    - qualia-net
  restart: unless-stopped
  environment:
    - POSTGRESQL_HOST=postgresql
    - POSTGRESQL_PORT=5452
    - POSTGRESQL_DB=postgis_forensic
    - GBIM_POSTGRESQL_HOST=postgresql
    - GBIM_POSTGRESQL_PORT=5433
    - GBIM_POSTGRESQL_DB=msallis
  # NOTE: POSTGRESQL_DB and GBIM_POSTGRESQL_DB values above are illustrative;
  # verify exact database names against production msallis-db and forensic postgis-forensic
  # containers after April 23 split. Confirm with:
  #   docker exec production-msallis-db psql -U postgres -c "\l"
  #   docker exec forensic-postgis-forensic psql -U postgres -c "\l"
```

---

> **★ PRODUCTION STARTUP SEQUENCE (required after every stack restart)**
>
> ```bash
> # Step 1 — bring the compose stack up
> docker compose up -d
>
> # Step 2 — wire legacy containers to the compose network
> bash scripts/post-start.sh
>
> # Step 3 — initialize swarm functions and eternal watchdogs (★ April 23 addition)
> bash scripts/post-start-swarm.sh
> ```
>
> `scripts/post-start.sh` connects legacy standalone containers (including `msallis-pgdata-rescue`, `production msallis-db`, and `forensic postgis-forensic` if not in compose) to `msallis-rebuild_qualia-net` and repairs any network drift. Without this step, the Guardian's `postgresql:5433` DNS will resolve to the wrong instance and `/health` will report `postgresql_gbim_connection: "error"`.
>
> `scripts/post-start-swarm.sh` (★ April 23 addition — Ch 35 §35.9) starts or verifies all eternal watchdogs, including the PostgreSQL two-container watchdogs, Caddy perimeter confirmation, and `verify_eternal_guardian_stack` smoke test.
>
> Verify the sequence completed successfully:
>
> ```bash
> # Verify Caddy forward_auth perimeter (OI-36-A CLOSED — zero-th gate):
> curl -s -o /dev/null -w "%{http_code}" https://egeria.mountainshares.us/chat
> # Expected: 401
>
> # Verify Guardian health — both PostgreSQL stores (OI-37-B CLOSED):
> curl -s http://localhost:8091/health | python3 -m json.tool
> # Expected:
> # {
> #   "status": "healthy",
> #   "postgresql_gbim_connection": "connected",   ← production msallis-db:5433 ★
> #   "postgresql_geodb_connection": "connected"   ← forensic postgis-forensic:5452 ★
> # }
> # NOTE: verify exact field names are current after April 23 two-container split
>
> # Verify container count (★ April 23 baseline: 100 Up):
> docker ps --format '{{.Names}} {{.Status}}' | grep -c "^.*Up"
> # Expected: 100
> ```
>
> Cross-reference: Ch 35 §35.9 (canonical startup sequence with post-start-swarm.sh); Ch 33 §33.7 (canonical reboot sequence); Ch 39 startup block.

---

## 37.3 Structure of Constitutional Principles

Principles are defined in `constitutional_principles.json` and loaded at Guardian startup. They are organized into six groups:

- First Amendment Rights
- Privacy and Security (Fourth Amendment)
- Due Process and Property (Fifth Amendment)
- Equal Protection (Fourteenth Amendment)
- General Welfare (Article I, Section 8; Preamble)
- Community Sovereignty (Tenth Amendment)

Each principle includes an `id`, short `title`, detailed `description`, `status` field (`active`, `experimental`, `deprecated`), `origin` pointing to specific constitutional text, `scope` describing which actions it applies to, a `postgresql_validation` block referencing `production msallis-db` ★ and/or `forensic postgis-forensic` ★, and a `confidence_decay_aware` flag for GBIM-linked principles.

Changes to principles go through versioned updates to `constitutional_principles.json` and are recorded in `/constitutional/versions`.

**Sample principle with `postgresql_validation` block (★ April 23 — updated for two-container split):**

```json
{
  "id": "10a-no-extraction",
  "title": "No Extraction of Community Data",
  "description": "Community data, geospatial records, and GBIM beliefs may not be extracted, commercialized, or repurposed for external profit. This principle protects community sovereignty under the Tenth Amendment.",
  "status": "active",
  "origin": "U.S. Constitution, Amendment X; Preamble (general welfare)",
  "scope": ["data_export", "external_api_call", "commercial_query"],
  "confidence_decay_aware": true,
  "postgresql_validation": {
    "production_msallis_db": {
      "host": "postgresql",
      "port": 5433,
      "note": "★ production msallis-db:5433 — supersedes msallis:5433 April 6",
      "check": "SELECT COUNT(*) FROM gbim_entities WHERE entity_type = 'community_asset' AND confidence_decay < 0.5",
      "purpose": "Flag high-decay community asset beliefs before allowing export decisions",
      "action_on_fail": "require_episodic_audit"
    },
    "forensic_postgis": {
      "host": "postgresql",
      "port": 5452,
      "note": "★ forensic postgis-forensic:5452 — supersedes msallisgis:5452 / gisdb:5432 April 6",
      "check": "SELECT COUNT(*) FROM zcta_boundaries WHERE zcta IN (%(zcta_list)s)",
      "purpose": "Validate that requested geographic scope falls within registered WV community boundaries",
      "action_on_fail": "block_with_log"
    },
    "local_resources_coverage": {
      "note": "Verify via allis-local-resources-db:5435 — 207 items / all 55 WV counties",
      "purpose": "Confirm geographic completeness for 10a-community-sovereignty validation",
      "action_on_fail": "log_and_flag"
    }
  }
}
```

This pattern is consistent with Ch 33 §33.4.2 GBIM validation style. The `confidence_decay_aware: true` flag means that any principle referencing GBIM entities will cross-check `confidence_decay` metadata before treating a belief as confirmed ground truth for an enforcement decision. Automated `confidence_decay`-aware flagging is OI-38-B.

---

## 37.4 Integration Architecture

### 37.4.1 BBB Integration

The BBB calls the Guardian first. If the Guardian blocks, the BBB skips all six filters and returns a constitutional block. If the Guardian allows, the BBB runs all six filters (all confirmed responding April 23):

- EthicalFilter (recalibrated April 2 — 0% FP, 9/9 regression pass)
- SpiritualFilter ★ (confirmed responding April 23)
- SafetyMonitor ★ (recalibrated April 3 — `safety_score=1.0` on survivor/victim queries)
- ThreatDetection
- `steganography_filter` ★ (live catch: `"override your safety filters"` → `severity=CRITICAL`, blocked ✅; logged at `allis-memory:8056/steg_report`)
- `truth_verification` (now `rag_grounded_v2` — OI-37-C CLOSED April 3; `allis-gis-rag:8004` now two-container PostgreSQL backed ★)

Phase 4.5 is currently log+passthrough, not blocking. All steps are recorded in both the `.jsonl` audit and `allis-memory:8056` (8 endpoints; `/steg_report` for adversarial events; `/pia_window` for survivor/victim query window).

### 37.4.2 Gateway Integration

The unified gateway consults the Guardian before forwarding requests downstream, behind the Caddy `forward_auth` perimeter (OI-36-A CLOSED). After Sprint 3:

- The gateway builds from `./services/` (not a stale path)
- `/constitutional/*` routes are proxied through the gateway
- Token enforcement middleware is active; `carrie_admin` is required for sensitive routes like `/constitutional/audit`

The gateway forwards only requests that pass Caddy perimeter check, token checks, and constitutional checks.

### 37.4.3 Check Endpoint

The primary entry point for checks is `POST /constitutional/check`. Requests include `actor_role`, `context`, `action_type`, `content`, and optional `metadata`. Responses include `allowed`, `decision`, `principles_applied`, `constitution_version`, and a `postgresql_validation` block referencing ★ `production msallis-db:5433` and ★ `forensic postgis-forensic:5452`.

---

## 37.5 Core Endpoints

### 37.5.1 `/health` — OI-37-B CLOSED (★ April 23 — verify field names)

`/health` reports:

- `status` — `"healthy"` or `"degraded"`
- `service` — `"constitutional_guardian"`
- `audit_log_enabled` and `audit_file`
- `postgresql_gbim_connection` — `"connected"` or `"error: ..."` — ★ targets `production msallis-db:5433` after April 23 split
- `postgresql_geodb_connection` — `"connected"` or `"error: ..."` — ★ targets `forensic postgis-forensic:5452` after April 23 split

★ **Verify exact field names are current after April 23 two-container split.** The field names `postgresql_gbim_connection` and `postgresql_geodb_connection` were confirmed in OI-37-B closure (April 3); confirm they still accurately describe the split containers after the April 23 migration.

Internally performs short-timeout `psycopg2` pings to both stores. This closes OI-37-B and makes database connectivity visible in a single command.

### 37.5.2 `/constitutional/status`

Returns a structural snapshot of the framework: which principle groups are active, which PostgreSQL databases are integrated (★ `production msallis-db:5433` and `forensic postgis-forensic:5452`), high-level statistics (principle count, version string), whether `confidence_decay` metadata is active, and `local_resources` coverage (207 items / 55 WV counties).

### 37.5.3 `/constitutional/principles`

Returns the full contents of `constitutional_principles.json` with all metadata. ★ Principle `postgresql_validation` blocks now reference `production msallis-db:5433` ★ and `forensic postgis-forensic:5452` ★ — verify these are updated in the file after April 23 split.

### 37.5.4 `/constitutional/versions`

Exposes version history for `constitutional_principles.json`, including the current version (`2026-02-17.2-USC`), historical versions, and change summaries.

### 37.5.5 `/constitutional/audit` and `/constitutional/audit/stats` — OI-37-A and OI-37-B Closure Verification (★ April 23)

| OI | Requirement | Fix commit | Verification command | Expected result |
|:--|:--|:--|:--|:--|
| OI-36-A | Caddy `forward_auth` HTTP 401 before port 8050 — zero-th gate (confirmed April 23) | OI-36-A CLOSED | `curl -s -o /dev/null -w "%{http_code}" https://egeria.mountainshares.us/chat` | `401` |
| OI-37-A | Gateway exposes `/constitutional/*`; `carrie_admin` enforcement active; current Guardian image | `a44267e3`, `af76b479` | `curl -H "Authorization: Bearer $CARRIE_ADMIN_TOKEN" http://localhost:8050/constitutional/audit` | HTTP 200; JSON audit entries returned |
| OI-37-B | `/health` returns PostgreSQL liveness fields for both stores ★ | `30395591` | `curl -s http://localhost:8091/health \| python3 -m json.tool` | `postgresql_gbim_connection: "connected"` (production msallis-db:5433 ★); `postgresql_geodb_connection: "connected"` (forensic postgis-forensic:5452 ★) |

Requests to audit routes are validated by token middleware: `carrie_admin` tokens get access; lower-privilege tokens receive `403`.

---

## 37.6 Persistent Audit Log

The audit log is the primary record of constitutional decisions:

- File: `data/constitutional_audit/constitutional_audit.jsonl`
- Directory must exist before first compose run: `mkdir -p data/constitutional_audit`
- Ownership must be `cakidd` (or the deploying user), not root
- Audit entries are written as JSON Lines, one per decision
- Each entry includes: timestamp, actor role, context, action type, content hash, decision, principles applied, constitution version, warnings, and PostgreSQL validation metadata (★ `production msallis-db:5433` + `forensic postgis-forensic:5452` after April 23 split)

**★ `allis-memory:8056` — durable cross-container audit (8 endpoints, survives restarts):**

Every constitutional decision is also written to `allis-memory:8056`. This provides cross-container survivability — constitutional gate decisions persist even if the Guardian container is restarted or rebuilt, and are independently queryable for governance accountability without requiring access to the host filesystem.

The 8 endpoints serve different audit purposes:

| Endpoint | Constitutional audit use |
|:--|:--|
| `/memory/turn` | Primary per-turn constitutional gate decisions |
| `/steg_report` | Adversarial events — e.g., `"override your safety filters"` → `severity=CRITICAL` |
| `/pia_window` | Survivor/victim query window — `safety_score=1.0` enforcement events |
| `/memory/sessions` | Session-level constitutional enforcement history |
| `/memory/episodic/{id}` | Specific decision episodic detail for governance review |

```bash
# Verify allis-memory:8056 is receiving constitutional audit events:
curl -H "Authorization: Bearer $allis_API_KEY" \
  http://localhost:8056/memory/turn?limit=5
# Expected: most recent gate decision records including constitutional events

# Verify steg_report endpoint (adversarial events):
curl -H "Authorization: Bearer $allis_API_KEY" \
  http://localhost:8056/steg_report

# Cross-check .jsonl audit is writing:
tail -5 data/constitutional_audit/constitutional_audit.jsonl | python3 -m json.tool
# Expected: recent JSON Lines with timestamp, decision, principles_applied fields
# verify postgresql_validation references production msallis-db:5433 ★ and forensic postgis-forensic:5452 ★
```

All BBB/Guardian gate decisions flow to `allis-memory:8056` as established by Ch 33 §33.2 addendum (secured March 28, 2026). The `.jsonl` file and `allis-memory:8056` are complementary — the file provides host-local forensic recovery; the memory service provides queryable, cross-container durable history.

---

## 37.7 Role-Specific Enforcement

Enforcement is role-aware:

- `external_corporation` — strictest; `10a-no-extraction` checked first; any attempt to commercialize community data triggers GeoDB validation against `forensic postgis-forensic:5452` ★ (17 GB, 314 PostGIS tables) and is likely blocked; `local_resources` coverage (207 items / 55 WV counties) confirms geographic scope
- `community_member` — standard; constitutional protections apply; context and GBIM data are considered, with `confidence_decay` informing the trust level of community facts used in decisions (~288/day growth means recent entities are higher confidence)
- `user`, `admin`, `system` — different levels of trust but all actions are logged to both `.jsonl` and `allis-memory:8056` (8 endpoints)

This structure aligns enforcement with power and risk rather than treating all actors identically.

---

## 37.8 Integration Testing

Regression tests committed in `fbb38c5d` and `3b5f11c0` lock in the full BBB–Guardian integration. ★ April 23 additions: Caddy perimeter test row added; PostgreSQL connection references updated to two-container split.

### BBB Constitutional Guardian Regression Test Suite (★ April 23 — updated)

| # | Test | Endpoint / command | Expected result | Status |
|:--|:--|:--|:--|:--|
| 0 | ★ Caddy `forward_auth` HTTP 401 (OI-36-A CLOSED) | `curl -s -o /dev/null -w "%{http_code}" https://egeria.mountainshares.us/chat` | `401` — zero-th gate active | ✅ Confirmed April 23 |
| 1 | Guardian blocks known extraction attempt (`external_corporation`) | `POST /constitutional/check` — `actor_role: "external_corporation"`, `action_type: "data_export"` | `allowed: false`, `principles_applied: ["10a-no-extraction"]`, audit log entry written | ✅ Pass |
| 2 | Guardian allows community support query (`community_member`) | `POST /constitutional/check` — `actor_role: "community_member"`, `action_type: "information_request"` | `allowed: true`, `decision: "constitutional_pass"`, audit log entry written | ✅ Pass |
| 3 | BBB calls Guardian first; constitutional block skips six filters | Send extraction-type content through BBB pipeline | BBB returns constitutional block without invoking EthicalFilter, SpiritualFilter, etc. | ✅ Pass |
| 4 | Gateway consults Guardian before forwarding downstream | `POST` to `:8050/chat` with extraction-type payload | Gateway returns `403` or constitutional block before reaching LLM ensemble | ✅ Pass |
| 5 | `/health` reports PostgreSQL liveness fields (OI-37-B) | `curl -s http://localhost:8091/health` | `postgresql_gbim_connection: "connected"` (production msallis-db:5433 ★); `postgresql_geodb_connection: "connected"` (forensic postgis-forensic:5452 ★) | ✅ Pass — ★ verify field names after split |
| 6 | Gateway routes `/constitutional/audit` (OI-37-A) | `curl -H "Authorization: Bearer $CARRIE_ADMIN_TOKEN" http://localhost:8050/constitutional/audit` | HTTP 200; audit entries returned | ✅ Pass |
| 7 | Non-admin token on `/constitutional/audit` returns 403 | `curl -H "Authorization: Bearer $HAYDEN_TOKEN" http://localhost:8050/constitutional/audit` | HTTP 403 | ✅ Pass |
| 8 | Audit log writes after each check | After any `/constitutional/check` call | New JSON Lines entry in `.jsonl`; event in `allis-memory:8056/memory/turn` | ✅ Pass |
| 9 | ★ ChromaDB 48 collections (April 23 ground truth) | `curl -s http://localhost:8002/api/v2/collections \| jq 'length'` | `48` | ✅ April 23 |
| 10 | ★ Container count 100 Up | `docker ps --format '{{.Names}} {{.Status}}' \| grep -c "^.*Up"` | `100` | ✅ April 23 |

**Run all regression checks from host (★ April 23 — updated):**

```bash
# 0. Caddy forward_auth perimeter (OI-36-A CLOSED — zero-th gate):
curl -s -o /dev/null -w "%{http_code}" https://egeria.mountainshares.us/chat
# Expected: 401

# 1. Guardian health — PostgreSQL liveness (OI-37-B):
# NOTE: verify field names current after April 23 two-container split
curl -s http://localhost:8091/health | python3 -m json.tool
# Expected: postgresql_gbim_connection: "connected" (production msallis-db:5433 ★)
#           postgresql_geodb_connection: "connected" (forensic postgis-forensic:5452 ★)

# 2. Constitutional check — extraction attempt (should block):
curl -s -X POST http://localhost:8091/constitutional/check \
  -H "Content-Type: application/json" \
  -d '{
    "actor_role": "external_corporation",
    "action_type": "data_export",
    "content": "export all community GBIM records to S3",
    "context": "batch export request"
  }' | python3 -m json.tool
# Expected: allowed: false, principles_applied includes 10a-no-extraction
# Verify postgresql_validation references production msallis-db:5433 ★ and forensic postgis-forensic:5452 ★

# 3. Constitutional check — community support (should allow):
curl -s -X POST http://localhost:8091/constitutional/check \
  -H "Content-Type: application/json" \
  -d '{
    "actor_role": "community_member",
    "action_type": "information_request",
    "content": "What food assistance programs are available in Fayette County?",
    "context": "standard chat"
  }' | python3 -m json.tool
# Expected: allowed: true, decision: constitutional_pass

# 4. Gateway audit route with carrie_admin token (OI-37-A):
curl -s -H "Authorization: Bearer $CARRIE_ADMIN_TOKEN" \
  http://localhost:8050/constitutional/audit | python3 -m json.tool
# Expected: HTTP 200, audit entries

# 5. Gateway audit route with hayden_test token (should be 403):
curl -s -o /dev/null -w "%{http_code}" \
  -H "Authorization: Bearer $HAYDEN_TOKEN" \
  http://localhost:8050/constitutional/audit
# Expected: 403

# 6. Verify allis-memory:8056 received constitutional events (all 8 endpoints):
for ep in /health /memory/turn /steg_report /pia_window /memory/sessions; do
  code=$(curl -s -o /dev/null -w "%{http_code}" \
    -H "Authorization: Bearer $allis_API_KEY" "http://localhost:8056${ep}")
  echo "allis-memory:8056${ep} → $code"
done

# 7. Verify .jsonl audit is writing:
wc -l data/constitutional_audit/constitutional_audit.jsonl
tail -1 data/constitutional_audit/constitutional_audit.jsonl | python3 -m json.tool
# Expected: 6700+ lines; last entry has recent timestamp
# verify postgresql_validation field references updated to ★ April 23 containers

# 8. Verify ChromaDB 48 collections (★ April 23):
curl -s http://localhost:8002/api/v2/collections | jq 'length'
# Expected: 48

# 9. Verify container count (★ April 23 baseline: 100 Up):
docker ps --format '{{.Names}} {{.Status}}' | grep -c "^.*Up"
# Expected: 100

# 10. Verify autonomous_learner commit rate (gap > 48h = governance alert):
# (See Ch 35 §35.5 for full script)
docker exec production-msallis-db psql -U postgres -d msallis -c \
  "SELECT EXTRACT(EPOCH FROM (NOW() - MAX(created_at)))/3600 AS gap_hours FROM autonomous_learner_commits;"
# Expected: < 48.0

# 11. Verify local_resources full 55-county coverage:
docker exec allis-local-resources-db psql -U postgres -c \
  "SELECT COUNT(DISTINCT county_fips) FROM local_resources;"
# Expected: 55
```

---

## 37.9 Governance and Monitoring

### Change Management

Changes to principles are versioned, documented, and tied to Git commits. This chapter's April 23 update reflects ground-truth supersession of PostgreSQL connection targets; no new principle amendments were made. All Sprint 3 commits (`30395591`, `a44267e3`, `af76b479`, `1a28c251`, `6b01ea64`, `7072b446`, `fbb38c5d`, `3b5f11c0`) remain the authoritative closure record.

### Monitoring (★ April 23 — updated)

The monitoring story includes:

- `/health` with PostgreSQL liveness (OI-37-B CLOSED) — ★ verify field names after April 23 split
- Caddy `forward_auth` confirmation (OI-36-A CLOSED) — verified in every nightly swarm audit as first check (Ch 35 §35.7)
- Watchdog script with fixed `docker ps --format` template (no `.ExitCode`) — commit `1a28c251`; ★ expected count updated to 100
- Production startup sequence: `docker compose up -d && bash scripts/post-start.sh && bash scripts/post-start-swarm.sh` (★ `post-start-swarm.sh` added April 23 — Ch 35 §35.9)
- Two-container PostgreSQL watchdogs: `production msallis-db:5433` ★ + `forensic postgis-forensic:5452` ★ (Ch 35 §35.5)
- `autonomous_learner` commit-gap watchdog: gap > 48 hours = governance alert; baseline ~288/day (Ch 35 §35.5)
- EEG Delta PIA heartbeat (port 8073): `pulse_count: 12,860+`; stalled pulse = safeguard infrastructure alert (Ch 35 §35.4)
- ChromaDB collection-count watchdog: drop below 48 = governance-level alert (Ch 35 §35.4)
- `local_resources` coverage watchdog: 207 items / 55 WV counties; reduction = governance alert (Ch 35 §35.7)

---

## 37.10 Sprint 3 Fixes — Summary (★ April 23 carry-forward)

Sprint 3 fixes remain the authoritative resolution record. April 23 adds ground-truth supersessions only.

1. **Network root cause** — `msallis-pgdata-rescue` standalone, off compose network. Fix: `docker network connect`; service DNS `postgresql:5433` internal, `localhost:5433` host. ★ April 23: `production msallis-db` is now the GBIM container; confirm it is attached to `msallis-rebuild_qualia-net`.

2. **Gateway build context drift** — building from stale path. Fix: Build from `./services/` — routes confirmed, Guardian wiring current.

3. **Post-start script** — recurring network drift. Fix: `scripts/post-start.sh`. ★ April 23: `scripts/post-start-swarm.sh` added as Step 3 (Ch 35 §35.9).

4. **Watchdog cosmetic error** — `.ExitCode` unsupported. Fix: Remove from format string; ★ April 23: expected count updated to 100 Up.

5. **Health visibility gap** — `/health` lacked database connectivity. Fix: PostgreSQL liveness checks — OI-37-B CLOSED. ★ April 23: verify field names current after two-container split.

6. **Gateway `/constitutional` routing gap** — Guardian routes not exposed. Fix: Wire `/constitutional/*` through gateway; OI-37-A CLOSED. Caddy `forward_auth` (OI-36-A CLOSED) is now documented as the zero-th gate before this layer.

---

## 37.11 Open Items (★ April 23, 2026 — ALL CLOSED)

As of April 23, 2026, **Chapter 37 has no open items.** OI-37-A and OI-37-B are both CLOSED and recorded in Git history. The April 23 two-container PostgreSQL split does not open new Chapter 37 OIs — it is a ground-truth supersession applied uniformly across all chapters. Any future work (Phase 4.5 blocking re-enablement, automated alert wiring, multi-sig amendment process, automated `confidence_decay` flagging) is tracked as OIs in Ch 38 and subsequent chapters.

---

*Chapter 37 — Constitutional Principles Service and Governance Layer*
*Ms. Egeria Allis Steward System — Harmony for Hope, Inc.*
*Mount Hope, West Virginia*
*Last updated: ★ 2026-04-23 — Carrie Kidd (Mamma Kidd)*
*OI-37-A ✅ OI-37-B ✅ OI-38-A ✅ — ★ 100 containers Up*
*production msallis-db:5433 ★ (16 GB / 294 tables / 11 schemas) + forensic postgis-forensic:5452 ★ (17 GB / 314 tables)*
*allis-memory:8056 — 8 endpoints — durable constitutional audit active — survives restarts*
*Caddy forward_auth (OI-36-A CLOSED) — HTTP 401 outermost gate — confirmed April 23*
*ChromaDB: 48 collections / ~6,740,611 vectors — /api/v2/ only — chromadb/chroma:0.6.3*
*local_resources: 207 items / all 55 WV counties — allis-local-resources-db:5435*
*post-start.sh + post-start-swarm.sh — required after every stack restart*
*autonomous_learner ~288/day — gap > 48h = governance alert*
*EEG Delta heartbeat port 8073 — pulse_count: 12,860+*
