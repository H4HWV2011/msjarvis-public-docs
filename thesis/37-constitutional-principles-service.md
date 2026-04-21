# Chapter 37 — Constitutional Principles Service and Governance Layer

**Carrie Kidd (Mamma Kidd) · Mount Hope, WV**  
**Last updated: ★★★★ April 6, 2026 — FINAL REWRITE**  
**105/105 containers Up (zero Restarting, zero Exited); constitutional guardian Up, healthy, `/health` returning PostgreSQL connection fields; audit log writing (6.7K+, `cakidd`-owned); watchdog template fix committed; gateway build context corrected; standalone `msallis-pgdata-rescue` wired into compose network; `scripts/post-start.sh` created and in use; OI-37-A CLOSED (gateway exposing `/constitutional/*` correctly with fresh image); OI-37-B CLOSED (`/health` includes PostgreSQL liveness fields); OI-38-A CLOSED (token enforcement active on all public hostnames); preflight gate 31 PASS / 0 FAIL / 0 WARN; EthicalFilter recalibrated April 2 (0% FP); SafetyMonitor recalibrated April 3 (`safety_score=1.0` on survivor/victim queries); Phase 4.5 BBB output guard in log+passthrough mode — blocking re-enablement is a next-session decision pending red team sign-off. BBB Constitutional Guardian regression tests committed (3b5f11c0). post-start.sh startup sequence required after every stack restart.**

---

> **SEALED STATUS BLOCK — WHAT THIS HEADER DOES AND DOES NOT MEAN**
>
> - **System baseline:** 105/105 containers Up (zero Restarting, zero Exited) — April 6, 2026 ground truth. This count supersedes all earlier baselines.
> - **Guardian state:** `allis-constitutional-guardian` is Up and healthy; `/health` returns PostgreSQL GBIM and GeoDB connection fields and reports `status: "healthy"`.
> - **Constitution version:** `2026-02-17.2-USC` active.
> - **Audit log:** `data/constitutional_audit/constitutional_audit.jsonl` is actively writing, 6.7K+ entries, `cakidd`-owned; durable audit also in `allis-memory:8056`.
> - **All Chapter 37 Open Items are CLOSED:**
>   - OI-37-A — gateway now builds from `./services/`, runs current image, and exposes `/constitutional/*` correctly, enforcing `carrie_admin` token requirements.
>   - OI-37-B — `/health` now includes PostgreSQL connection liveness fields for `msallis` and `msallisgis`.
>   - OI-38-A — previously open, now CLOSED (token enforcement middleware active at gateway).
> - **Sprint-3 constitutional guardian log is clean:** final commits for this chapter:
>   - `30395591` — `fix(constitutional-guardian): close OI-37-B`
>   - `a44267e3` — `docs(ch37): close OI-37-A`
>   - `af76b479` — `fix(gateway): correct build context from ./services/`
>   - `1a28c251` — `fix(watchdog): remove .ExitCode template field`
>   - `6b01ea64` — `docs(ch37): add chapter file + OI-37-B gap`
>   - `7072b446` — `docs(ch37): April 3 gap audit`
>   - `fbb38c5d` — `test: Constitutional Guardian + BBB regression tests`
>   - `3b5f11c0` — `fix: wire Constitutional Guardian as BBB first gate`
>
> **What this header is NOT:** It is not a live status indicator. It is a sealed snapshot of the stack and guardian as of April 6, 2026 final rewrite, after Sprint 3 fixes, regression tests, and Ch. 33 April 6 ground truth corrections, with all Chapter 37 OIs fully closed.

---

## Why This Matters for Polymathmatic Geography

This chapter describes the Constitutional Guardian service that provides constitutional compliance checking grounded in the United States Constitution and validated against PostgreSQL `msallis` (port 5433 — 5,416,521 GBIM entities with `confidence_decay` metadata, 80 epochs, 206 source layers) and `gisdb`/`msallisgis` (host port 5432 / compose-internal 5452 — PostGIS, **45 GB, 548 tables** — Ch. 33 April 6, 2026 ground truth) for geospatial community boundary validation. It supports:

- **P1 – Every where is entangled** by ensuring that constitutional protections propagate through all services and paths, from gateway to barrier to consciousness layers, all grounded in PostgreSQL GBIM community knowledge with temporal confidence grading (`confidence_decay` metadata).
- **P3 – Power has a geometry** by making constitutional authority the highest architectural layer — explicitly documented, versioned, audited, and queryable — rather than hiding governance rules in opaque code. Constitutional gate decisions are durably logged in both a persistent `.jsonl` file and `allis-memory:8056`, making enforcement history independently inspectable.
- **P5 – Design is a geographic act** by treating constitutional principles as designed artifacts that encode community sovereignty (10th Amendment) and anti-extraction protections for Appalachian communities, validated against `gisdb`'s PostGIS boundaries (**45 GB, 548 tables** — Ch. 33 April 6 ground truth) with ZIP-code-level community precision.
- **P12 – Intelligence with a ZIP code** by grounding equal protection (14th Amendment) and community sovereignty (10th Amendment) principles in West Virginia-specific contexts validated against `msallis` GBIM and `msallisgis` geodata.
- **P16 – Power accountable to place** by maintaining a persistent audit log of every constitutional decision, making all blocks, allows, and principle applications queryable and transparent to communities, and by tying enforcement to PostgreSQL-backed identity and geography.

As such, this chapter belongs to the **Computational Instrument tier**: it specifies the Constitutional Guardian as an independently testable, PostgreSQL-grounded, audit-logged authority service.

---

```text
┌─────────────────────────────────────────────────────────────┐
│   Constitutional Guardian Architecture                      │
│   ★★★★ FINAL: April 6, 2026                                │
│   ★ 105/105 containers Up — zero Restarting, zero Exited   │
│   ★ Guardian: Up, healthy, /health with Postgres fields    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
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
│  │  GBIM: msallis (5433)                          │        │
│  │    - 5,416,521 entities, confidence_decay      │        │
│  │  GeoDB: msallisgis                             │        │
│  │    - host:5432 / container-internal:5452       │        │
│  │    - 45 GB / 548 tables (Ch.33 Apr 6)         │        │
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
│  │  -  If allowed → six filters:                  │        │
│  │    - EthicalFilter (0% FP, Apr 2)              │        │
│  │    - SpiritualFilter                           │        │
│  │    - SafetyMonitor (survivor-safe, Apr 3)      │        │
│  │    - ThreatDetection                           │        │
│  │    - steganography_filter                      │        │
│  │    - truth_verification (rag_grounded_v2)      │        │
│  │  Phase 4.5 output: log+passthrough             │        │
│  │  - 31% FP eliminated; blocking re-enable       │        │
│  │    is next-session/red-team decision           │        │
│  │  All gate decisions → allis-memory:8056        │        │
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
│      ↓                                                      │
│  Role-Specific Enforcement                                 │
│  -  external_corporation: STRICTEST (10a-no-extraction)    │
│  -  community_member: STANDARD                             │
│  -  user/admin/system: tiered + logged                     │
│      ↓                                                      │
│  PostgreSQL Integration                                    │
│  -  msallis (5433): GBIM + confidence_decay                │
│  -  msallisgis: host:5432 / container-internal:5452        │
│    - 45 GB / 548 tables (Ch. 33 April 6 ground truth)      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Figure 37.1.** Constitutional Guardian architecture (★★★★ FINAL April 6, 2026): constitutional authority as highest layer; gateway and BBB both checking the guardian first; six-filter BBB (EthicalFilter 0% FP April 2; SafetyMonitor survivor-safe April 3; `truth_verification` now `rag_grounded_v2` per OI-37-C); Phase 4.5 log+passthrough; dual PostgreSQL integration (`msallis:5433` GBIM 5,416,521 entities with `confidence_decay`; `msallisgis` host:5432 / internal:5452 — **45 GB / 548 tables** Ch. 33 April 6 ground truth); persistent `.jsonl` plus durable `allis-memory:8056` audit; OI-37-A CLOSED (gateway routing); OI-37-B CLOSED (PostgreSQL `/health` fields). See §37.5.5 for OI closure verification table.

---

## Status Table — ★★★★ April 6, 2026 FINAL

| Category | Details |
|:--|:--|
| **Implemented** | `allis-constitutional-guardian` running at `127.0.0.1:8091`, healthy. FastAPI with CORS. WORKDIR `/app` (Dockerfile-set; no `-w` flag needed or allowed). Constitution version `2026-02-17.2-USC` active; API service version `2.1.0-USC-Audit` in compose labels. BBB wired to consult Guardian first; unified gateway wired to Guardian before BBB. All `/constitutional/*` routes proxied through the gateway using the current Guardian image (build context fixed to `./services/`) with token enforcement middleware active — OI-37-A CLOSED. Persistent `.jsonl` audit log on host with `cakidd` ownership, plus durable audit in `allis-memory:8056`. `/health` returns PostgreSQL liveness fields — OI-37-B CLOSED. Production startup sequence: `docker compose up -d && bash scripts/post-start.sh`. |
| **Partially implemented / scaffolded** | Multi-signature principle amendment workflow. Community consultation process. Real-time dashboards and external reporting. Automated `confidence_decay`-aware GBIM validation pipeline. Full alert wiring for Exited/Created state detection (pattern documented in this chapter; alert delivery to external systems is future work). Phase 4.5 blocking re-enablement pending red team sign-off. |
| **Future work / design intent only** | ML-based pattern detection for constitutional violations. Exporting audit traces to partner compliance systems. Time-series constitutional enforcement analytics in PostgreSQL. Governance UI for reviewing and annotating audit records. Formal session contracts tightly binding gateway, BBB, and Guardian changes for cooperative oversight. |

---

## 37.1 Purpose and Constitutional Foundation

The Constitutional Guardian is the highest authority in Ms. Allis's governance hierarchy. It is grounded in the United States Constitution and backed by PostgreSQL `msallis` (port 5433 — GBIM entities with `confidence_decay` metadata) and `msallisgis` (host 5432 / container-internal 5452 — PostGIS, **45 GB, 548 tables** — Ch. 33 April 6, 2026 ground truth) rather than ad-hoc rules.

**Legal foundation:**

- First Amendment: speech, religion, assembly, petition.
- Fourth Amendment: privacy and security.
- Fifth Amendment: due process and property.
- Fourteenth Amendment: equal protection and due process, validated via GBIM and geodata.
- General Welfare clause and Preamble.
- Tenth Amendment: community sovereignty and reserved powers, validated against ZCTA-level geography.

**Operational role:**

- Acts as **pre-filter** for all actions the system takes or allows.
- Provides a shared, explicit set of constitutional principles with documented origins.
- Writes every decision to an audit log plus durable memory.
- Reveals how power is applied to community data and geography.

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
- PostgreSQL integration:
  - GBIM: `postgresql:5433` on the compose network; verified host-side at `localhost:5433`.
  - GeoDB: `msallisgis` — see compose environment and port callout below.

**Network root cause and fix (Sprint 3):**

- **Root cause:** `msallis-pgdata-rescue` was running standalone, not on the compose network. From inside containers, `172.18.0.1:5433` was unreachable, and `postgresql` DNS resolved to the wrong instance.
- **Fix:** Use `docker network connect` to attach `msallis-pgdata-rescue` to the compose project network. The Guardian now reaches GBIM at `postgresql:5433` on the compose network and verifies via host-side `psql` at `localhost:5433`.

**Gateway build context drift and fix (Sprint 3):**

- **Root cause:** The unified gateway was building from a stale external path instead of `./services/`, leaving it with an outdated route set and stale Guardian wiring.
- **Fix:** Commit `af76b479` changed the gateway's build context to `./services/` and ensured all 86 routes (including `/constitutional/*`) are included.

---

> **★ PORT CALLOUT — `POSTGRESQL_PORT=5452` (container-internal) vs. host port 5432**
>
> The compose environment sets `POSTGRESQL_PORT=5452`. This is the **container-internal** port mapping for the `msallisgis` GeoDB connection inside the Guardian container. It is **not** the host port.
>
> | Reference | Port | Context |
> |:--|:--|:--|
> | `POSTGRESQL_PORT` in compose env | **5452** | Container-internal — used by the Guardian to reach `msallisgis` inside the Docker network |
> | Host-side `psql` / external tools | **5432** | Host port — Ch. 33 April 6 ground truth: `gisdb:5432` = **45 GB / 548 tables** |
>
> **Do not change `POSTGRESQL_PORT` from `5452` in the compose file.** Host-side access always uses 5432. The 5452/5432 split is the correct, intentional mapping — not an error.

---

**Compose configuration (simplified):**

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
    - POSTGRESQL_DB=msallisgis
    - GBIM_POSTGRESQL_PORT=5433
    - GBIM_POSTGRESQL_DB=msallis
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
> ```
>
> `scripts/post-start.sh` connects legacy standalone containers (e.g., `msallis-pgdata-rescue`) to the compose project network (`msallis-rebuild_qualia-net`) and repairs any network drift introduced by bare `docker run` commands. Without this step, the Guardian's `postgresql:5433` DNS will resolve to the wrong instance and `/health` will report `postgresql_gbim_connection: "error"`.
>
> Verify the sequence completed successfully:
>
> ```bash
> curl -s http://localhost:8091/health | python3 -m json.tool
> # Expected:
> # {
> #   "status": "healthy",
> #   "postgresql_gbim_connection": "connected",
> #   "postgresql_geodb_connection": "connected"
> # }
> ```
>
> Cross-reference: Ch. 33 §33.7 (canonical reboot sequence); Ch. 39 startup block.

---

## 37.3 Structure of Constitutional Principles

Principles are defined in `constitutional_principles.json` and loaded at Guardian startup. They are organized into six groups:

- First Amendment Rights
- Privacy and Security (Fourth Amendment)
- Due Process and Property (Fifth Amendment)
- Equal Protection (Fourteenth Amendment)
- General Welfare (Article I, Section 8; Preamble)
- Community Sovereignty (Tenth Amendment)

Each principle includes:

- An `id` (e.g., `10a-no-extraction`)
- A short `title`
- A detailed `description`
- A `status` field (`active`, `experimental`, `deprecated`)
- An `origin` pointing to specific constitutional text
- A `scope` describing which actions it applies to
- A `postgresql_validation` block referencing `msallis` and/or `msallisgis`
- A `confidence_decay_aware` flag for GBIM-linked principles (e.g., `10a-local-control`)

Changes to principles go through versioned updates to `constitutional_principles.json` and are recorded in `/constitutional/versions`.

**Sample principle with `postgresql_validation` block (redacted — `10a-no-extraction`):**

The following is a representative example of how the `postgresql_validation` block is populated for an anti-extraction principle. Field values are illustrative; authoritative values are in `constitutional_principles.json`.

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
    "msallis": {
      "check": "SELECT COUNT(*) FROM gbim_entities WHERE entity_type = 'community_asset' AND confidence_decay < 0.5",
      "purpose": "Flag high-decay community asset beliefs before allowing export decisions",
      "action_on_fail": "require_episodic_audit"
    },
    "msallisgis": {
      "check": "SELECT COUNT(*) FROM zcta_boundaries WHERE zcta IN (%(zcta_list)s)",
      "purpose": "Validate that requested geographic scope falls within registered WV community boundaries",
      "action_on_fail": "block_with_log"
    }
  }
}
```

This pattern is consistent with Ch. 33 §33.4.2 GBIM validation style. The `confidence_decay_aware: true` flag means that any principle referencing GBIM entities will cross-check `confidence_decay` metadata before treating a belief as confirmed ground truth for an enforcement decision.

---

## 37.4 Integration Architecture

### 37.4.1 BBB Integration

The BBB calls the Guardian first. If the Guardian blocks, the BBB skips all six filters and returns a constitutional block. If the Guardian allows, the BBB runs:

- EthicalFilter (recalibrated April 2 — 0% FP, 9/9 regression pass)
- SpiritualFilter
- SafetyMonitor (recalibrated April 3 — `safety_score=1.0` on survivor/victim queries)
- ThreatDetection
- `steganography_filter`
- `truth_verification` (now `rag_grounded_v2` — OI-37-C CLOSED April 3)

Phase 4.5 is currently log+passthrough, not blocking. All steps are recorded in both the `.jsonl` audit and `allis-memory:8056`.

### 37.4.2 Gateway Integration

The unified gateway consults the Guardian before forwarding requests downstream. After Sprint 3:

- The gateway builds from `./services/` (not a stale path).
- `/constitutional/*` routes are proxied through the gateway.
- Token enforcement middleware is active; `carrie_admin` is required for sensitive routes like `/constitutional/audit`.

The gateway forwards only requests that pass both token checks and constitutional checks.

### 37.4.3 Check Endpoint

The primary entry point for checks is `POST /constitutional/check`. Requests include `actor_role`, `context`, `action_type`, `content`, and optional `metadata`. Responses include `allowed`, `decision`, `principles_applied`, `constitution_version`, and a `postgresql_validation` block.

---

## 37.5 Core Endpoints

### 37.5.1 `/health` — OI-37-B CLOSED

Before Sprint 3, `/health` only returned simple service status. After commit `30395591`, `/health` now reports:

- `status` — `"healthy"` or `"degraded"`
- `service` — `"constitutional_guardian"`
- `audit_log_enabled` and `audit_file`
- `postgresql_gbim_connection` — `"connected"` or `"error: ..."`
- `postgresql_geodb_connection` — `"connected"` or `"error: ..."`

Internally, it performs short-timeout `psycopg2` pings to `msallis` and `msallisgis`. This closes OI-37-B and makes database connectivity visible in a single command.

### 37.5.2 `/constitutional/status`

Returns a structural snapshot of the framework: which principle groups are active, which PostgreSQL databases are integrated, high-level statistics (principle count, version string), and whether `confidence_decay` metadata is active.

### 37.5.3 `/constitutional/principles`

Returns the full contents of `constitutional_principles.json` with all metadata.

### 37.5.4 `/constitutional/versions`

Exposes version history for `constitutional_principles.json`, including the current version (`2026-02-17.2-USC`), historical versions, and change summaries.

### 37.5.5 `/constitutional/audit` and `/constitutional/audit/stats` — OI-37-A and OI-37-B Closure Verification

Before Sprint 3, the gateway did not expose `/constitutional/audit` at all — calling through `:8050/constitutional/audit` gave `404`. Both OIs are now closed and the following verification table confirms their status:

| OI | Requirement | Fix commit | Verification command | Expected result |
|:--|:--|:--|:--|:--|
| OI-37-A | Gateway exposes `/constitutional/*`; `carrie_admin` enforcement active; current Guardian image in use | `a44267e3`, `af76b479` | `curl -H "Authorization: Bearer $CARRIE_ADMIN_TOKEN" http://localhost:8050/constitutional/audit` | HTTP 200; JSON audit entries returned |
| OI-37-B | `/health` returns `postgresql_gbim_connection` and `postgresql_geodb_connection` liveness fields | `30395591` | `curl -s http://localhost:8091/health \\| python3 -m json.tool` | `postgresql_gbim_connection: "connected"`, `postgresql_geodb_connection: "connected"` |

Requests to audit routes are validated by token middleware: `carrie_admin` tokens get access; lower-privilege tokens receive `403`.

---

## 37.6 Persistent Audit Log

The audit log is the primary record of constitutional decisions:

- File: `data/constitutional_audit/constitutional_audit.jsonl`
- Directory must exist before first compose run:

```bash
mkdir -p data/constitutional_audit
```

- Ownership must be `cakidd` (or the deploying user), not root.
- Audit entries are written as JSON Lines, one per decision.
- Each entry includes: timestamp, actor role, context, action type, content hash, decision, principles applied, constitution version, warnings, and PostgreSQL validation metadata.

**★ `allis-memory:8056` — durable cross-container audit (secured March 28, 2026):**

In addition to the `.jsonl` file, **every constitutional decision is also written to `allis-memory:8056`**. This provides cross-container survivability: constitutional gate decisions persist even if the Guardian container is restarted or rebuilt, and are independently queryable for governance accountability without requiring access to the host filesystem.

```bash
# Verify allis-memory:8056 is receiving constitutional audit events:
curl -H "Authorization: Bearer $JARVIS_API_KEY" \
  http://localhost:8056/memories?limit=5
# Expected: most recent gate decision records including constitutional events

# Cross-check .jsonl audit is writing:
tail -5 data/constitutional_audit/constitutional_audit.jsonl | python3 -m json.tool
# Expected: recent JSON Lines with timestamp, decision, principles_applied fields
```

All BBB/Guardian gate decisions flow to `allis-memory:8056` as established by Ch. 33 §33.2 addendum (secured March 28, 2026). The `.jsonl` file and `allis-memory:8056` are complementary — the file provides host-local forensic recovery; the memory service provides queryable, cross-container durable history.

---

## 37.7 Role-Specific Enforcement

Enforcement is role-aware:

- `external_corporation` — strictest; `10a-no-extraction` checked first; any attempt to commercialize community data triggers GeoDB validation against `msallisgis` (45 GB / 548 tables — Ch. 33 April 6 ground truth) and is likely blocked.
- `community_member` — standard; constitutional protections apply; context and GBIM data are considered, with `confidence_decay` informing the trust level of community facts used in decisions.
- `user`, `admin`, `system` — different levels of trust but all actions are logged to both `.jsonl` and `allis-memory:8056`.

This structure aligns enforcement with power and risk rather than treating all actors identically.

---

## 37.8 Integration Testing

Regression tests committed in `fbb38c5d` (`test: Constitutional Guardian + BBB regression tests`) and `3b5f11c0` (`fix: wire Constitutional Guardian as BBB first gate`) lock in the full BBB–Guardian integration. The table below mirrors the regression test format from Ch. 33 §33.6.

### BBB Constitutional Guardian Regression Test Suite (commit `fbb38c5d` / `3b5f11c0`)

| # | Test | Endpoint / command | Expected result | Status |
|:--|:--|:--|:--|:--|
| 1 | Guardian blocks known extraction attempt (`external_corporation`) | `POST /constitutional/check` — `actor_role: "external_corporation"`, `action_type: "data_export"` | `allowed: false`, `principles_applied: ["10a-no-extraction"]`, audit log entry written | ✅ Pass |
| 2 | Guardian allows community support query (`community_member`) | `POST /constitutional/check` — `actor_role: "community_member"`, `action_type: "information_request"` | `allowed: true`, `decision: "constitutional_pass"`, audit log entry written | ✅ Pass |
| 3 | BBB calls Guardian first; constitutional block skips six filters | Send extraction-type content through BBB pipeline | BBB returns constitutional block without invoking EthicalFilter, SpiritualFilter, etc. | ✅ Pass |
| 4 | Gateway consults Guardian before forwarding downstream | `POST` to `:8050/chat` with extraction-type payload | Gateway returns `403` or constitutional block before reaching LLM ensemble | ✅ Pass |
| 5 | `/health` reports PostgreSQL liveness fields (OI-37-B) | `curl -s http://localhost:8091/health` | `postgresql_gbim_connection: "connected"`, `postgresql_geodb_connection: "connected"` | ✅ Pass |
| 6 | Gateway routes `/constitutional/audit` (OI-37-A) | `curl -H "Authorization: Bearer $CARRIE_ADMIN_TOKEN" http://localhost:8050/constitutional/audit` | HTTP 200; audit entries returned | ✅ Pass |
| 7 | Non-admin token on `/constitutional/audit` returns 403 | `curl -H "Authorization: Bearer $HAYDEN_TOKEN" http://localhost:8050/constitutional/audit` | HTTP 403 | ✅ Pass |
| 8 | Audit log writes after each check | After any `/constitutional/check` call | New JSON Lines entry in `data/constitutional_audit/constitutional_audit.jsonl`; event in `allis-memory:8056` | ✅ Pass |

**Run all regression checks from host:**

```bash
# 1. Guardian health — PostgreSQL liveness (OI-37-B):
curl -s http://localhost:8091/health | python3 -m json.tool

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

# 6. Verify allis-memory:8056 received constitutional events:
curl -H "Authorization: Bearer $JARVIS_API_KEY" \
  http://localhost:8056/memories?limit=3 | python3 -m json.tool
# Expected: recent records including constitutional gate decisions

# 7. Verify .jsonl audit is writing:
wc -l data/constitutional_audit/constitutional_audit.jsonl
tail -1 data/constitutional_audit/constitutional_audit.jsonl | python3 -m json.tool
# Expected: 6700+ lines; last entry has recent timestamp
```

---

## 37.9 Governance and Monitoring

### Change Management

Changes to principles are versioned, documented, and tied to Git commits. This chapter's April 6 final state is anchored by:

- `30395591` (closing OI-37-B)
- `a44267e3` (closing OI-37-A)
- Earlier documentation and test commits in the Sprint 3 sequence

### Monitoring

The monitoring story now includes:

- `/health` with PostgreSQL liveness (OI-37-B CLOSED)
- Watchdog script with fixed `docker ps --format` template (no `.ExitCode`) — commit `1a28c251`
- Production startup sequence: `docker compose up -d && bash scripts/post-start.sh` (required after every restart — see §37.2)
- Recommended cron/watchdog patterns for detecting:
  - Exited (0) Guardian containers
  - Created-but-never-started Guardian containers

These patterns are documented and will be wired to alerts in a future sprint.

---

## 37.10 Sprint 3 Fixes — Summary

What Sprint 3 fixed for this chapter:

1. **Network root cause** — `msallis-pgdata-rescue` was standalone, off the compose network.  
   - Fix: Attach to compose network; use service DNS `postgresql:5433` internal, `localhost:5433` for host verification.

2. **Gateway build context drift** — gateway was building from a stale path.  
   - Fix: Build from `./services/` — 86 routes confirmed, Guardian wiring current.

3. **Post-start script** — recurring configuration drift between compose and standalone containers.  
   - Fix: `scripts/post-start.sh` created. Run after every stack restart (see §37.2 Production Startup Sequence).

4. **Watchdog cosmetic error** — `.ExitCode` template field unsupported on this Docker version.  
   - Fix: Remove `.ExitCode` from `watchdog-containers.sh` format string — commit `1a28c251`.

5. **Health visibility gap** — `/health` lacked database connectivity information.  
   - Fix: Add PostgreSQL liveness checks to `/health` — OI-37-B CLOSED, commit `30395591`.

6. **Gateway `/constitutional` routing gap** — Guardian routes not exposed or running under stale image.  
   - Fix: Wire `/constitutional/*` through gateway using current image and enforce token roles — OI-37-A CLOSED, commit `a44267e3`.

With these fixes, **all Chapter 37 OIs are closed** and the sprint log is clean.

---

## 37.11 Open Items

As of April 6, 2026, **Chapter 37 has no open items.** OI-37-A and OI-37-B are both CLOSED and recorded in Git history. Any future work (Phase 4.5 blocking re-enablement, automated alert wiring, multi-sig amendment process) will be tracked as new OIs in subsequent chapters or sprints.

---

## 37.12 Summary

Chapter 37 describes a fully integrated, PostgreSQL-backed Constitutional Guardian service:

- Running as its own container, built from current code, on the compose network.
- Exposed through the unified gateway with token enforcement, as the first gate before the BBB.
- Backed by dual PostgreSQL databases (`msallis:5433` GBIM with `confidence_decay`; `msallisgis` host:5432 / internal:5452 — **45 GB / 548 tables**, Ch. 33 April 6 ground truth).
- Logging every decision to both a persistent `.jsonl` file (`cakidd`-owned, 6.7K+ entries) and `allis-memory:8056` for durable cross-container survivability.
- Tested and verified via regression tests committed in `fbb38c5d` and `3b5f11c0`.
- Production startup sequence documented and required: `docker compose up -d && bash scripts/post-start.sh`.
- All known gaps — routing, health visibility, watcher noise, network wiring, principle documentation — addressed and recorded in Git.

---

*Chapter 37 — Constitutional Principles Service and Governance Layer*  
*Ms. Egeria Allis Steward System — Harmony for Hope, Inc.*  
*Mount Hope, West Virginia*  
*FINAL: ★★★★ April 6, 2026 — Sprint 3 Constitutional Guardian Complete*  
*OI-37-A ✅ OI-37-B ✅ OI-38-A ✅ — 105/105 containers Up*  
*gisdb:5432 — 45 GB / 548 tables (Ch. 33 April 6 ground truth)*  
*allis-memory:8056 — durable constitutional audit active*  
*post-start.sh — required after every stack restart*  
