# 37. Constitutional Principles Service and Governance Layer

**Carrie Kidd (Mamma Kidd) · Pax, WV**  
**Last updated: ★ April 3, 2026 — Chapter 37 SEALED. 101/101 containers Up (zero Restarting, zero Exited); constitutional guardian Up, healthy, `/health` returning PostgreSQL connection fields; audit log writing (6.7K+, `cakidd`-owned); watchdog template fix committed; gateway build context corrected; standalone `msjarvis-pgdata-rescue` wired into compose network; `scripts/post-start.sh` created and in use; OI-37-A CLOSED (gateway exposing `/constitutional/*` correctly with fresh image); OI-37-B CLOSED (`/health` includes PostgreSQL liveness fields); OI-38-A CLOSED (token enforcement active on all public hostnames); preflight gate 22 PASS / 0 FAIL / 1 WARN (intentional); EthicalFilter recalibrated April 2 (0% FP); SafetyMonitor recalibrated April 3 (`safety_score=1.0` on survivor/victim queries); Phase 4.5 BBB output guard in log+passthrough mode — blocking re-enablement is a next-session decision pending red team sign-off.**

---

> **SEALED STATUS BLOCK — WHAT THIS HEADER DOES AND DOES NOT MEAN**
>
> - **System baseline:** 101/101 containers Up (zero Restarting, zero Exited) — confirmed April 2–3, 2026. This count supersedes the earlier 96/96 baseline.  
> - **Guardian state:** `jarvis-constitutional-guardian` is Up and healthy; `/health` returns PostgreSQL GBIM and GeoDB connection fields and reports `status: "healthy"`.  
> - **Constitution version:** `2026-02-17.2-USC` active.  
> - **Audit log:** `data/constitutional_audit/constitutional_audit.jsonl` is actively writing, 6.7K+ entries, `cakidd`-owned; durable audit in `jarvis-memory:8056`.  
> - **All Chapter 37 Open Items are CLOSED:**  
>   - OI-37-A — gateway now builds from `./services/`, runs current image, and exposes `/constitutional/*` correctly, enforcing `carrie_admin` token requirements.  
>   - OI-37-B — `/health` now includes PostgreSQL connection liveness fields for `msjarvis` and `msjarvisgis`.  
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
> **What this header is NOT:** It is not a live status indicator. It is a sealed snapshot of the stack and guardian as of April 3, 2026, after Sprint 3 fixes and regression tests, with Chapter 37 OIs fully closed.

---

## Why This Matters for Polymathmatic Geography

This chapter describes the Constitutional Guardian service that provides constitutional compliance checking grounded in the United States Constitution and validated against PostgreSQL `msjarvis` (port 5433 — 5,416,521 GBIM entities with `confidence_decay` metadata, 80 epochs, 206 source layers) for GBIM community knowledge and `gisdb`/`msjarvisgis` (host port 5432 / compose-internal 5452 — PostGIS, 91 GB, 501 tables, 993 ZCTA centroids) for geospatial community boundary validation. It supports:

- **P1 – Every where is entangled** by ensuring that constitutional protections propagate through all services and paths, from gateway to barrier to consciousness layers, all grounded in PostgreSQL GBIM community knowledge with temporal confidence grading (`confidence_decay` metadata).
- **P3 – Power has a geometry** by making constitutional authority the highest architectural layer — explicitly documented, versioned, audited, and queryable — rather than hiding governance rules in opaque code. Constitutional gate decisions are durably logged in both a persistent `.jsonl` file and `jarvis-memory:8056`, making enforcement history independently inspectable.
- **P5 – Design is a geographic act** by treating constitutional principles as designed artifacts that encode community sovereignty (10th Amendment) and anti-extraction protections for Appalachian communities, validated against `gisdb`’s PostGIS boundaries (91 GB, 501 tables, 993 ZCTA centroids) with ZIP-code-level community precision.
- **P12 – Intelligence with a ZIP code** by grounding equal protection (14th Amendment) and community sovereignty (10th Amendment) principles in West Virginia-specific contexts validated against `msjarvis` GBIM and `msjarvisgis` geodata.
- **P16 – Power accountable to place** by maintaining a persistent audit log of every constitutional decision, making all blocks, allows, and principle applications queryable and transparent to communities, and by tying enforcement to PostgreSQL-backed identity and geography.

As such, this chapter belongs to the **Computational Instrument tier**: it specifies the Constitutional Guardian as an independently testable, PostgreSQL-grounded, audit-logged authority service.

---

```
┌─────────────────────────────────────────────────────────────┐
│   Constitutional Guardian Architecture                      │
│   ★ SEALED: April 3, 2026                                  │
│   ★ 101/101 containers Up — zero Restarting, zero Exited   │
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
│  │  GBIM: msjarvis (5433)                         │        │
│  │    - 5,416,521 entities, confidence_decay      │        │
│  │  GeoDB: msjarvisgis                            │        │
│  │    - host:5432 / internal:5452                │        │
│  │    - 91 GB, 501 tables, 993 ZCTA centroids    │        │
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
│  │    - truth_verification                        │        │
│  │  Phase 4.5 output: log+passthrough             │        │
│  │  - 31% FP eliminated; blocking re-enable       │        │
│  │    is next-session/red-team decision           │        │
│  │  All gate decisions → jarvis-memory:8056       │        │
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
│  -  All events also → jarvis-memory:8056                   │
│      ↓                                                      │
│  Role-Specific Enforcement                                 │
│  -  external_corporation: STRICTEST (10a-no-extraction)     │
│  -  community_member: STANDARD                             │
│  -  user/admin/system: tiered + logged                     │
│      ↓                                                      │
│  PostgreSQL Integration                                    │
│  -  msjarvis (5433): GBIM + confidence_decay               │
│  -  msjarvisgis: host:5432 / internal:5452                 │
│    - 91 GB PostGIS, 501 tables, 993 ZCTA centroids         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Figure 37.1.** Constitutional Guardian architecture (SEALED April 3, 2026): constitutional authority as highest layer; gateway and BBB both checking the guardian first; six-filter BBB with recalibrated EthicalFilter and SafetyMonitor; Phase 4.5 log+passthrough; dual PostgreSQL integration; persistent `.jsonl` plus durable `jarvis-memory:8056` audit; all Chapter 37 OIs closed.

---

## Status Table — ★ April 3, 2026 SEALED

| Category | Details |
|---|---|
| **Implemented** | `jarvis-constitutional-guardian` running at `127.0.0.1:8091`, healthy. FastAPI with CORS. WORKDIR `/app` (Dockerfile-set; no `-w` flag needed or allowed). Constitution version `2026-02-17.2-USC` active; API service version `2.1.0-USC-Audit` in compose labels. BBB wired to consult Guardian first; unified gateway wired to Guardian before BBB. All `/constitutional/*` routes proxied through the gateway using the **current** Guardian image (build context fixed to `./services/`) with token enforcement middleware active — OI-37-A CLOSED. Persistent `.jsonl` audit log on host with `cakidd` ownership, plus durable audit in `jarvis-memory:8056`. `/health` returns PostgreSQL liveness fields — OI-37-B CLOSED. |
| **Partially implemented / scaffolded** | Multi-signature principle amendment workflow. Community consultation process. Real-time dashboards and external reporting. Automated `confidence_decay`-aware GBIM validation pipeline. Full alert wiring for Exited/Created state detection (pattern documented in this chapter; alert delivery to external systems is future work). Phase 4.5 blocking re-enablement pending red team sign-off. |
| **Future work / design intent only** | ML-based pattern detection for constitutional violations. Exporting audit traces to partner compliance systems. Time-series constitutional enforcement analytics in PostgreSQL. Governance UI for reviewing and annotating audit records. Formal session contracts tightly binding gateway, BBB, and Guardian changes for cooperative oversight. |

---

## 37.1 Purpose and Constitutional Foundation

The Constitutional Guardian is the highest authority in Ms. Jarvis’s governance hierarchy. It is grounded in the United States Constitution and backed by PostgreSQL `msjarvis` (port 5433 — GBIM entities with `confidence_decay` metadata) and `msjarvisgis` (host 5432 / internal 5452 — PostGIS, 91 GB, 501 tables, 993 ZCTA centroids) rather than ad-hoc rules.

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

- Container name: `jarvis-constitutional-guardian`
- Port: 8091 (bound to `127.0.0.1`)
- Compose network: `qualia-net` (runtime: `msjarvis-rebuild_qualia-net`)
- WORKDIR: `/app` (set in Dockerfile)
- Principles file: `/app/constitutional_principles.json` (host: `./services/constitutional_principles.json`)
- Audit directory: `/app/audit` (host: `./data/constitutional_audit`)
- PostgreSQL integration:
  - GBIM: host `msjarvis-pgdata-rescue` on compose network, port 5433; inside Guardian, host `postgresql`, port 5433.
  - GeoDB: `msjarvisgis` exposed on host 5432, but internal service uses `POSTGRESQL_PORT=5452`.

**Network root cause and fix (Sprint 3):**

- **Root cause:** `msjarvis-pgdata-rescue` was running standalone, not on the compose network. From inside containers, `172.18.0.1:5433` was unreachable, and `postgresql` DNS resolved to the wrong instance.
- **Fix:** Use `docker network connect` to attach `msjarvis-pgdata-rescue` to the compose project network and configure compose to reach it by service DNS, not by host bridge IP. The Guardian now reaches GBIM at `postgresql:5433` on the compose network and verifies via host-side `psql` at `localhost:5433`.

**Gateway build context drift and fix (Sprint 3):**

- **Root cause:** The unified gateway was building from a stale external path instead of `./services/`, leaving it with an outdated route set and stale Guardian wiring.
- **Fix:** Commit `af76b479` changed the gateway’s build context to `./services/` and ensured all 86 routes (including `/constitutional/*`) are included. The gateway now proxies to the current Guardian image and returns the correct status and audit routes for `carrie_admin` tokens.

> **Post-start wiring script:**  
> To keep the compose and legacy standalone containers wired correctly, run:
>
> ```bash
> docker compose up -d
> bash scripts/post-start.sh
> ```
>
> `scripts/post-start.sh` connects legacy containers (e.g., `msjarvis-pgdata-rescue`) to the compose network and repairs any network drift introduced by bare `docker run` commands.

**Compose configuration (simplified):**

```yaml
jarvis-constitutional-guardian:
  build:
    context: ./services
    dockerfile: Dockerfile.constitutional_guardian
  container_name: jarvis-constitutional-guardian
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
    - POSTGRESQL_DB=msjarvisgis
    - GBIM_POSTGRESQL_PORT=5433
    - GBIM_POSTGRESQL_DB=msjarvis
```

**Operator rule:** Do not change `POSTGRESQL_HOST` from `postgresql`, and do not change `POSTGRESQL_PORT` from `5452` inside the compose file. Host-side `psql` uses 5432 for `msjarvisgis`, but the container uses 5452.

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
- A `postgresql_validation` block referencing `msjarvis` and/or `msjarvisgis`
- A `confidence_decay_aware` flag for GBIM-linked principles (e.g., `10a-local-control`)

Changes to principles go through versioned updates to `constitutional_principles.json` and are recorded in `/constitutional/versions`.

---

## 37.4 Integration Architecture

### 37.4.1 BBB Integration

The BBB calls the Guardian first. If the Guardian blocks, the BBB skips all six filters and returns a constitutional block. If the Guardian allows, the BBB runs:

- EthicalFilter
- SpiritualFilter
- SafetyMonitor
- ThreatDetection
- `steganography_filter`
- `truth_verification`

Phase 4.5 is currently log+passthrough, not blocking. All these steps are recorded in both the `.jsonl` audit and `jarvis-memory:8056`.

### 37.4.2 Gateway Integration

The unified gateway consults the Guardian before forwarding requests downstream. After Sprint 3:

- The gateway builds from `./services/` (not a stale path).
- `/constitutional/*` routes are proxied through the gateway.
- Token enforcement middleware is active; `carrie_admin` is required for sensitive routes like `/constitutional/audit`.

The gateway forwards only requests that pass both token checks and constitutional checks.

### 37.4.3 Check Endpoint

The primary entry point for checks is:

- `POST /constitutional/check`

Requests include `actor_role`, `context`, `action_type`, `content`, and optional `metadata`. Responses include `allowed`, `decision`, `principles_applied`, `constitution_version`, and a `postgresql_validation` block.

---

## 37.5 Core Endpoints

### 37.5.1 `/health` — OI-37-B CLOSED

Before today, `/health` only returned simple service status. OI-37-B required adding PostgreSQL liveness information. After commit `30395591`, `/health` now reports:

- `status` — `"healthy"` or `"degraded"`
- `service` — `"constitutional_guardian"`
- `audit_log_enabled` and `audit_file`
- `postgresql_gbim_connection` — `"connected"` or `"error: ..."`
- `postgresql_geodb_connection` — `"connected"` or `"error: ..."`

Internally, it performs short-timeout `psycopg2` pings to `msjarvis` and `msjarvisgis`. This closes OI-37-B and makes database connectivity visible in a single command.

### 37.5.2 `/constitutional/status`

Returns a structural snapshot of the framework:

- Which principle groups are active
- Which PostgreSQL databases are integrated
- High-level statistics (principle count, version string)
- Whether `confidence_decay` metadata is active

### 37.5.3 `/constitutional/principles`

Returns the full contents of `constitutional_principles.json` with all metadata.

### 37.5.4 `/constitutional/versions`

Exposes version history for `constitutional_principles.json`, including:

- Current version (`2026-02-17.2-USC`)
- Historical versions
- Change summaries

### 37.5.5 `/constitutional/audit` and `/constitutional/audit/stats` — OI-37-A CLOSED

Before Sprint 3, the gateway did not expose `/constitutional/audit` at all — calling through `:8050/constitutional/audit` gave `404`. OI-37-A is now closed:

- The gateway now proxies `/constitutional/*` to the Guardian.
- Requests are validated by token middleware:
  - `carrie_admin` tokens get access to audit routes.
  - Lower-privilege tokens receive `403` as appropriate.
- The gateway builds from the current Guardian image (`./services/` context), so routes and behavior are in sync.

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

In addition to the file, all decisions are recorded in `jarvis-memory:8056` for durable, queryable audit independent of container lifecycle.

---

## 37.7 Role-Specific Enforcement

Enforcement is role-aware:

- `external_corporation` — strictest; `10a-no-extraction` checked first; any attempt to commercialize community data triggers GeoDB validation and is likely blocked.
- `community_member` — standard; constitutional protections apply; context and GBIM data are considered, with `confidence_decay` informing the trust level of community facts used in decisions.
- `user`, `admin`, `system` — different levels of trust but all actions are logged.

This structure aligns enforcement with power and risk rather than treating all actors identically.

---

## 37.8 Integration Testing

Regression tests (`fbb38c5d`) ensure:

- The Guardian blocks known extraction attempts from `external_corporation`.
- The Guardian allows community support queries.
- The BBB and gateway consult the Guardian first.
- `/health` reports PostgreSQL connectivity correctly.
- Gateway routing to `/constitutional/*` is wired to the current Guardian image.

These tests lock in the intended behavior and guard against regressions.

---

## 37.9 Governance and Monitoring

### Change Management

Changes to principles are versioned, documented, and tied to Git commits. This chapter’s April 3 sealing state is anchored by:

- `30395591` (closing OI-37-B)
- `a44267e3` (closing OI-37-A)
- Earlier documentation and test commits in the Sprint 3 sequence

### Monitoring

The monitoring story now includes:

- `/health` with PostgreSQL liveness
- Watchdog script with fixed `docker ps --format` template (no `.ExitCode`)
- Recommended cron/watchdog patterns for detecting:

  - Exited (0) Guardian containers
  - Created-but-never-started Guardian containers

These patterns are documented here and will be wired to alerts in a future sprint.

---

## 37.10 Sprint 3 Fixes — Summary

What Sprint 3 fixed for this chapter:

1. **Network root cause** — `msjarvis-pgdata-rescue` was standalone, off the compose network.  
   - Fix: Attach it to the compose network, use service DNS and proper ports (`postgresql:5433` internal, `localhost:5433` for host verification).

2. **Gateway build context drift** — gateway was building from a stale path and not seeing current Guardian code or routes.  
   - Fix: Build from `./services/`, confirming 86 routes and proper Guardian wiring.

3. **Post-start script** — recurring configuration drift between compose and standalone containers.  
   - Fix: `scripts/post-start.sh` created. Run after every stack restart:

     ```bash
     docker compose up -d
     bash scripts/post-start.sh
     ```

4. **Watchdog cosmetic error** — `.ExitCode` template field unsupported on this Docker version.  
   - Fix: Remove `.ExitCode` from `watchdog-containers.sh` format string; script now runs cleanly.

5. **Health visibility gap** — `/health` lacked database connectivity information (OI-37-B).  
   - Fix: Add PostgreSQL liveness checks and fields to `/health`.

6. **Gateway /constitutional routing gap** — Guardian routes not exposed or running under stale image (OI-37-A).  
   - Fix: Wire `/constitutional/*` through gateway using current image and enforce token roles.

With these fixes, **all Chapter 37 OIs are closed** and the sprint log is clean.

---

## 37.11 Open Items

As of April 3, 2026, **Chapter 37 has no open items.** OI-37-A and OI-37-B are both CLOSED and recorded in Git history. Any future work (e.g., Phase 4.5 blocking re-enablement, automated alert wiring, multi-sig amendment process) will be tracked as new OIs in subsequent chapters or sprints, not as residual debt in this chapter.

---

## 37.12 Summary

Chapter 37 now describes a fully integrated, PostgreSQL-backed Constitutional Guardian service:

- Running as its own container, built from current code, on the compose network.
- Exposed through the unified gateway with token enforcement, as the first gate before the BBB.
- Backed by dual PostgreSQL databases (`msjarvis` GBIM with `confidence_decay`, `msjarvisgis` GeoDB).
- Logging every decision to both a persistent `.jsonl` file and a durable memory service.
- Tested and verified via regression tests and production commands.
- With all known gaps — routing, health visibility, watcher noise, network wiring, principle documentation — addressed and recorded in Git.

*Chapter 37 — Constitutional Principles Service and Governance Layer*  
*Ms. Egeria Jarvis Steward System — Harmony for Hope, Inc.*  
*Mount Hope, West Virginia*  
*SEALED: ★ April 3, 2026 — Sprint 3 Constitutional Guardian Complete*
