# 37. Constitutional Principles Service and Governance Layer

**Carrie Kidd (Mamma Kidd) · Pax, WV**
**Last updated: ★ March 28, 2026 — 96/96 containers Up (zero Restarting, zero Exited); PostgreSQL `msjarvis:5433` restored (★ 5,416,521 GBIM entities with `confidence_decay` metadata); `msjarvisgis:5452` confirmed (★ 91 GB PostGIS, 501 tables, 993 ZCTA centroids); ChromaDB full audit (★ 40 active collections / 6,675,442 total vectors); `jarvis-memory:8056` secured (durable BBB + constitutional audit trail, `_auth()` confirmed, `JARVIS_API_KEY` set); container count updated to 96 throughout; BBB six-filter correction re-confirmed (Figure 37.1, §37.4.1); PostgreSQL database disambiguation updated (★ `msjarvisgis` 91 GB / 501 tables / 993 ZCTA centroids replaces prior 13 GB / 39 tables throughout); Phase 4.5 log+passthrough note re-confirmed; OI-37-A sprint dependency note re-confirmed; version string distinction re-confirmed**

---

## Why This Matters for Polymathmatic Geography

This chapter describes the Constitutional Guardian service that provides
constitutional compliance checking grounded in the United States Constitution and
validated against PostgreSQL `msjarvis` (port 5433 — ★ 5,416,521 GBIM entities with `confidence_decay` metadata, 80 epochs, 206 source layers — restored March 28) for GBIM community knowledge and `gisdb`/`msjarvisgis` (port 5452 — ★ PostGIS, 91 GB, 501 tables, 993 ZCTA centroids — confirmed March 28) for geospatial community boundary validation. It supports:

- **P1 – Every where is entangled** by ensuring that constitutional protections
  propagate through all services and paths, from gateway to barrier to
  consciousness layers, all grounded in PostgreSQL GBIM community knowledge (★ 5,416,521 entities with `confidence_decay` metadata — temporal confidence grading available for community belief validation).
- **P3 – Power has a geometry** by making constitutional authority the highest
  architectural layer — explicitly documented, versioned, audited, and queryable —
  rather than hiding governance rules in opaque code. ★ All constitutional gate decisions are now durably logged at `jarvis-memory:8056` (secured March 28) in addition to the persistent `constitutional_audit.jsonl` file — constitutional enforcement is independently queryable across container restarts.
- **P5 – Design is a geographic act** by treating constitutional principles as
  designed artifacts that encode community sovereignty (10th Amendment) and
  anti-extraction protections for Appalachian communities documented in PostgreSQL
  `gisdb` geographic boundaries (★ 501 tables, 993 ZCTA centroids — enabling ZIP-code-level community boundary precision for anti-extraction enforcement) and `msjarvis` GBIM beliefs.
- **P12 – Intelligence with a ZIP code** by grounding equal protection (14th
  Amendment) and community sovereignty (10th Amendment) principles in West
  Virginia-specific contexts validated against PostgreSQL `gisdb` (★ PostGIS, 91 GB, 993 ZCTA centroids) and `msjarvis` GBIM institutional knowledge (★ `confidence_decay` metadata for temporal confidence grading).
- **P16 – Power accountable to place** by maintaining a persistent audit log of
  every constitutional decision, making all blocks, allows, and principle
  applications queryable and transparent to communities. ★ The `jarvis-memory:8056` durable audit trail (secured March 28) extends this accountability across container restarts — constitutional enforcement records now survive independently of the `constitutional_audit.jsonl` file.

As such, this chapter belongs to the **Computational Instrument tier**: it
specifies the Constitutional Guardian as a dedicated service with U.S.
Constitution-grounded principles, defense-in-depth integration (gateway + BBB),
persistent audit logging, version control, and PostgreSQL validation.

---

```
┌─────────────────────────────────────────────────────────────┐
│   Constitutional Guardian Architecture                      │
│   ★ Production State: March 28, 2026                        │
│   ★ 96/96 containers Up — zero Restarting, zero Exited      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Constitutional Authority Hierarchy                         │
│  ┌────────────────────────────────────────────────┐        │
│  │  HIGHEST: Constitutional Guardian (8091)       │        │
│  │  ★ Up — 96/96 confirmed March 28               │        │
│  │  Foundation: U.S. Constitution                 │        │
│  │  -  Amendment I (speech, religion, assembly)   │        │
│  │  -  Amendment IV (privacy, security)           │        │
│  │  -  Amendment V (due process, property)        │        │
│  │  -  Amendment XIV (equal protection)           │        │
│  │  -  General Welfare (Art. I §8, Preamble)      │        │
│  │  -  Amendment X (community sovereignty)        │        │
│  │                                                │        │
│  │  6 Principle Groups, 15+ Specific Principles  │        │
│  │  API version: 2.1.0-USC-Audit (docker-compose)│        │
│  │  Constitution version: 2026-02-17.2-USC        │        │
│  │  GBIM validation: PostgreSQL msjarvis (5433)  │        │
│  │  ★ 5,416,521 entities, confidence_decay meta  │        │
│  │  GeoDB validation: PostgreSQL gisdb (5452)    │        │
│  │  ★ 91 GB PostGIS, 501 tables, 993 ZCTA ctrs  │        │
│  └────────────────────────────────────────────────┘        │
│      ↓                                                      │
│  Defense-in-Depth Integration                              │
│  ┌────────────────────────────────────────────────┐        │
│  │  Level 1: Unified Gateway (8050) ★ Up 96/96   │        │
│  │  -  Checks Constitutional Guardian first       │        │
│  │  -  Block before BBB if violation              │        │
│  │  -  Tracks constitutional_blocks               │        │
│  └────────────────────────────────────────────────┘        │
│      ↓                                                      │
│  ┌────────────────────────────────────────────────┐        │
│  │  Level 2: Blood-Brain Barrier (8016) ★ Up     │        │
│  │  -  Checks Constitutional Guardian first       │        │
│  │  -  If blocked → skip all six filters          │        │
│  │  -  If allowed → proceed to six filters:       │        │
│  │    - EthicalFilter                            │        │
│  │    - SpiritualFilter                          │        │
│  │    - SafetyMonitor                            │        │
│  │    - ThreatDetection                          │        │
│  │    - steganography_filter                     │        │
│  │    - truth_verification                       │        │
│  │  Phase 4.5 output: log+passthrough mode       │        │
│  │  (commit 18b8ddac, March 22, 2026)            │        │
│  │  ★ All gate decisions durable at:             │        │
│  │    jarvis-memory:8056 (secured March 28)      │        │
│  └────────────────────────────────────────────────┘        │
│      ↓                                                      │
│  Core API Endpoints                                        │
│  -  POST /constitutional/check (compliance checking)        │
│  -  GET  /constitutional/status (framework status)          │
│  -  GET  /constitutional/principles (full structure)        │
│  -  GET  /constitutional/versions (version history)         │
│  -  GET  /constitutional/audit (decision history)           │
│  -  GET  /constitutional/audit/stats (analytics)            │
│  -  GET  /constitutional/transparency (public report)       │
│      ↓                                                      │
│  Persistent Audit Log (Survives Restarts)                  │
│  -  File: data/constitutional_audit/                        │
│          constitutional_audit.jsonl                         │
│  -  Format: JSON Lines (one decision per line)              │
│  -  Fields: timestamp, actor_role, context, action_type,   │
│    content_hash, decision, principles_applied,             │
│    constitution_version, warnings                          │
│  -  Queryable via /constitutional/audit                     │
│  ★ Additionally durable at jarvis-memory:8056              │
│    (secured March 28) — survives container restarts        │
│    independently of .jsonl file                            │
│      ↓                                                      │
│  Role-Specific Enforcement (Validated vs PostgreSQL GBIM)  │
│  -  external_corporation: STRICTEST (10a-no-extraction)     │
│  -  community_member: STANDARD (constitutional protections) │
│  -  user: STANDARD                                          │
│  -  system: LOGGED (generally allowed)                      │
│      ↓                                                      │
│  PostgreSQL Integration (two databases — ★ March 28)       │
│  -  msjarvis (5433): GBIM — ★ 5,416,521 entities           │
│     with confidence_decay metadata                         │
│     → equal protection, 10a-local-control, 14a-*           │
│  -  gisdb (5452): PostGIS — ★ 91 GB, 501 tables,           │
│     993 ZCTA centroids                                      │
│     → community boundary validation, 10a-no-extraction     │
│                                                             │
│  Production Status (★ March 28, 2026)                      │
│  -  Total checks: 150+                                      │
│  -  Blocked: 23 (~15% block rate)                           │
│  -  Allowed: 127                                            │
│  -  Most violated: 10a-no-extraction (15 blocks)            │
│  -  Response time: <100ms                                   │
│  -  Audit log: PERSISTENT (.jsonl + ★ jarvis-memory:8056)  │
│  ★ 96/96 containers Up — STATUS: ✅ OPERATIONAL             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Figure 37.1.** Constitutional Guardian architecture (★ March 28, 2026 — 96/96 containers Up): U.S. Constitution-grounded
principles (6 groups covering Amendments I, IV, V, X, XIV + General Welfare) as
highest authority, defense-in-depth integration at gateway (★ Up 96/96) and BBB (★ Up 96/96) levels; BBB
runs **six filters** after Constitutional Guardian check (EthicalFilter,
SpiritualFilter, SafetyMonitor, ThreatDetection, steganography_filter,
truth_verification) — Phase 4.5 output currently in log+passthrough mode (commit
`18b8ddac`, March 22, 2026); ★ all BBB gate decisions durably logged at `jarvis-memory:8056` (secured March 28); GBIM validation via `msjarvis` (port 5433 — ★
5,416,521 entities with `confidence_decay` metadata) and geographic boundary validation via `gisdb` (port 5452 — ★
PostGIS, 91 GB, 501 tables, 993 ZCTA centroids); persistent audit log surviving restarts (.jsonl ★ plus `jarvis-memory:8056`); role-specific enforcement;
version control with change tracking; comprehensive API for compliance checking
and transparency.

---

## Status as of ★ March 28, 2026

| Category | Details |
|---|---|
| **Implemented** | `jarvis-constitutional-guardian` confirmed running at `127.0.0.1:8091` (★ Up 96/96). FastAPI service with full CORS support. 6 principle groups grounded in U.S. Constitution. 15+ specific principles with metadata. Constitution version `2026-02-17.2-USC` confirmed active (API service version `2.1.0-USC-Audit` — see §37.2 for distinction). BBB integration: Constitutional Guardian checked FIRST; if blocked → immediate rejection before all six BBB filters. Gateway defense-in-depth at port 8050 (★ Up 96/96). Persistent audit log at `data/constitutional_audit/constitutional_audit.jsonl`. ★ All constitutional BBB gate decisions additionally durably logged at `jarvis-memory:8056` (secured March 28 — `_auth()` confirmed, `JARVIS_API_KEY` set). Role-specific enforcement. PostgreSQL `msjarvis` at port 5433 (★ 5,416,521 GBIM entities with `confidence_decay` metadata — restored March 28) for community belief validation; `gisdb`/`msjarvisgis` at port 5452 (★ PostGIS, 91 GB, 501 tables, 993 ZCTA centroids — confirmed March 28) for geographic boundary validation. Full API suite. 150+ production checks, 23 blocked (~15%), 127 allowed, `10a-no-extraction` most violated (15 blocks), <100ms response time. Phase 4.5 BBB output in log+passthrough mode (commit `18b8ddac`, March 22, 2026). ★ ChromaDB full audit: 40 active collections / 6,675,442 total vectors — constitutional `dgm_observations` collection confirmed in inventory. |
| **Partially implemented / scaffolded** | Multi-signature approval for principle amendments designed but not yet implemented. Community consultation workflow identified as future work. Real-time monitoring dashboard not yet implemented. Integration with additional services (GIS, psychological) partially designed. ★ Automated `confidence_decay`-aware GBIM validation not yet fully automated — high-decay entities can be flagged manually for episodic audit before use as constitutional ground truth. |
| **Future work / design intent only** | Priority 2.4 — Principle Amendment Process: multi-sig approval, community consultation workflow, impact analysis tooling, historical precedent database. Real-time monitoring dashboard. Alerting for constitutional violation trends. ML for violation pattern detection. Export audit data to external compliance systems. Automated `confidence_decay`-aware PostgreSQL GBIM validation pipeline. PostgreSQL-backed time-series analytics for constitutional enforcement trends. Phase 4.5 BBB output threshold recalibration and re-activation of full verdict-dict enforcement mode. |

---

## 37.1 Purpose and Constitutional Foundation

The Constitutional Guardian serves as the highest authority in Ms. Jarvis's
governance hierarchy, grounded in the United States Constitution and validated
against PostgreSQL `msjarvis` (port 5433 — ★ 5,416,521 GBIM entities with `confidence_decay` metadata) and `gisdb` (port 5452 — ★ PostGIS, 91 GB, 501 tables, 993 ZCTA centroids)
rather than arbitrary rules. This provides:

**Legitimate Legal Authority:**

- All principles derive from established U.S. Constitutional amendments and the
  Preamble.
- First Amendment protections (speech, religion, assembly, petition).
- Fourth Amendment privacy and security protections.
- Fifth Amendment due process and property rights.
- Fourteenth Amendment equal protection guarantees validated against PostgreSQL `msjarvis` GBIM (★ `confidence_decay` metadata available for temporal confidence grading of equal protection community facts).
- General Welfare clause (Article I, Section 8 and Preamble).
- Tenth Amendment community sovereignty and reserved powers validated against
  PostgreSQL `msjarvis` GBIM and `gisdb` geographic boundaries (★ 993 ZCTA centroids enabling ZIP-code-level community sovereignty boundary validation).

**Operational Benefits:**

- **Shared reference:** Single source of constitutional truth across all services
  grounded in PostgreSQL.
- **Constraint enforcement:** Blocks actions that violate constitutional principles
  validated against PostgreSQL GBIM before they occur.
- **Transparency:** All decisions are logged with constitutional justification and
  PostgreSQL validation status. ★ Constitutional gate decisions are now durably logged at `jarvis-memory:8056` (secured March 28) in addition to the persistent `.jsonl` file.
- **Legitimacy:** Grounded in 200+ years of constitutional law and PostgreSQL
  community data (★ 5,416,521 GBIM entities with `confidence_decay` metadata).

---

## 37.2 Implementation as a Dedicated Service

The Constitutional Guardian runs as a containerized FastAPI service (★ Up 96/96 — confirmed March 28).

**Service Details:**

| Field | Value |
|---|---|
| Container | `jarvis-constitutional-guardian` |
| Port | 8091 |
| Network | `qualia-net` |
| Image | Built from `services/Dockerfile.constitutional_guardian` |
| Main File | `services/constitutional_api_fixed.py` |
| Principles File | `services/constitutional_principles.json` |
| API Service Version | `2.1.0-USC-Audit` (docker-compose `version:` label — see versioning note below) |
| Constitution Version | `2026-02-17.2-USC` (returned in all API responses as `constitution_version`) |
| PostgreSQL GBIM | `msjarvis` (port 5433) — ★ 5,416,521 entities with `confidence_decay` metadata; equal protection, 10a-local-control, 14a-* validation |
| PostgreSQL GeoDB | `gisdb`/`msjarvisgis` (port 5452) — ★ PostGIS, 91 GB, 501 tables, 993 ZCTA centroids; geographic boundary validation |
| ★ Durable Audit | `jarvis-memory:8056` (secured March 28) — all constitutional BBB gate decisions persistently logged |

> **Versioning distinction:** Two version strings coexist in this service and serve different purposes:
>
> - **`2.1.0-USC-Audit`** — the docker-compose `version:` label for the *API service container*. This is a semantic version (`MAJOR.MINOR.PATCH-qualifier`) that tracks service implementation changes (code, endpoints, audit features). It appears in `docker inspect` and compose metadata but is **not** returned in API responses.
> - **`2026-02-17.2-USC`** — the *constitution version* (`constitution_version`) returned in every API response (`/constitutional/check`, `/constitutional/status`, `/constitutional/versions`, `/constitutional/audit`). This is a date-based version (`YYYY-MM-DD.REVISION-framework`) that tracks changes to `constitutional_principles.json` — the actual principle content. Principle amendments increment this string; code changes do not.
>
> These are not interchangeable. When reading a `/constitutional/check` response, the `constitution_version` field tells you which version of the principles governed the decision, not which version of the API service ran. When tracking deployments in docker-compose, the `version: 2.1.0-USC-Audit` label tells you which implementation is running.

**Docker Configuration:**

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
    # POSTGRESQL_PORT/DB below target gisdb (PostGIS, port 5452) for geographic
    # boundary validation (community sovereignty, anti-extraction GeoDB checks).
    # ★ March 28: confirmed 91 GB PostGIS, 501 tables, 993 ZCTA centroids.
    # GBIM entity validation (★ 5,416,521 beliefs with confidence_decay metadata,
    # equal protection, 10a-local-control) targets msjarvis at port 5433 —
    # configured separately in constitutional_api_fixed.py via
    # GBIM_POSTGRESQL_PORT=5433 / GBIM_POSTGRESQL_DB=msjarvis.
    - POSTGRESQL_PORT=5452
    - POSTGRESQL_DB=msjarvisgis
```

**Environment Variables:**

| Variable | Value | Purpose |
|---|---|---|
| `SERVICE_PORT` | `8091` | Constitutional Guardian API port |
| `CONSTITUTIONAL_GUARDIAN_URL` | `http://jarvis-constitutional-guardian:8091` | Internal network reference |
| `POSTGRESQL_HOST` | `postgresql` | Shared PostgreSQL host |
| `POSTGRESQL_PORT` | `5452` | `gisdb`/`msjarvisgis` — ★ PostGIS, 91 GB, 501 tables, 993 ZCTA centroids; geographic boundary validation |
| `POSTGRESQL_DB` | `msjarvisgis` | PostGIS database for community sovereignty / anti-extraction GeoDB checks |
| `GBIM_POSTGRESQL_PORT` | `5433` | `msjarvis` — ★ 5,416,521 GBIM entities with `confidence_decay` metadata |
| `GBIM_POSTGRESQL_DB` | `msjarvis` | GBIM database for equal protection, 10a-local-control, 14a-* validation |

> **Note on source file:** The running implementation is
> `services/constitutional_api_fixed.py`. The original `constitutional_api.py`
> is superseded. Always reference the `_fixed` variant for current behavior.

---

## 37.3 Structure of Constitutional Principles

Principles are organized by constitutional basis in
`constitutional_principles.json`, validated against PostgreSQL `msjarvis` (★ GBIM, 5,416,521 entities with `confidence_decay` metadata, port 5433)
and `gisdb` (★ PostGIS, 91 GB, 501 tables, 993 ZCTA centroids, port 5452).

**Principle Groups:**

- **First Amendment Rights (Amendment I)**
  - `1a-speech`: Freedom of speech and expression
  - `1a-religion`: Freedom of religion
  - `1a-assembly`: Freedom of assembly and association
  - `1a-petition`: Right to petition for redress

- **Privacy and Security (Amendment IV)**
  - `4a-privacy`: Protection against unreasonable searches
  - `4a-security`: Security of persons and data

- **Due Process and Property Rights (Amendment V)**
  - `5a-due-process`: Due process of law
  - `5a-property`: Protection of property
  - `5a-self-incrimination`: No compelled self-incrimination

- **Equal Protection (Amendment XIV)**
  - `14a-equal-protection`: Equal protection under law, validated against
    PostgreSQL `msjarvis` GBIM (port 5433 — ★ `confidence_decay` metadata available for temporal confidence grading of equal protection community facts)
  - `14a-due-process`: Fundamental fairness in procedures

- **General Welfare (Article I, Section 8 & Preamble)**
  - `gw-public-benefit`: Promote general welfare
  - `gw-justice`: Establish justice

- **Community Sovereignty (Amendment X — Reserved Powers)**
  - `10a-local-control`: Local self-governance, validated against PostgreSQL
    `msjarvis` GBIM (port 5433 — ★ `confidence_decay` metadata for temporal grading)
  - `10a-no-extraction`: Protection against economic exploitation, grounded in
    PostgreSQL `gisdb` GeoDB community boundaries (port 5452 — ★ 91 GB PostGIS, 501 tables, 993 ZCTA centroids enabling ZIP-code-level anti-extraction boundary enforcement)

**Metadata Structure:** Each principle includes:

| Field | Description |
|---|---|
| `id` | Unique identifier (e.g., `"10a-no-extraction"`) |
| `title` | Human-readable name |
| `description` | Detailed explanation |
| `status` | `"active"`, `"experimental"`, or `"deprecated"` |
| `origin` | Constitutional basis (e.g., `"U.S. Constitution, Amendment I"`) |
| `scope` | Applicability (e.g., `["all_content", "user_expression"]`) |
| `postgresql_validation` | Link to GBIM or GeoDB validation for community-specific principles |
| ★ `confidence_decay_aware` | Flag indicating whether GBIM validation queries check `confidence_decay` metadata for temporal confidence grading (applicable to `10a-local-control`, `14a-equal-protection`) |

---

## 37.4 Integration Architecture

### 37.4.1 Blood-Brain Barrier Integration

The BBB (`services/ms_jarvis_blood_brain_barrier.py`, port 8016 — ★ Up 96/96) checks
Constitutional Guardian **first** before running its **six** filters.

> **Phase 4.5 operational note (March 22, 2026 — re-confirmed ★ March 28):** The BBB output guard (Phase 4.5) is currently in **log+passthrough mode** (commit `18b8ddac`, March 22, 2026), pending output threshold recalibration. This means that constitutional blocks triggered by the Phase 4.5 BBB output guard are being **logged** but are **not enforcing hard blocks** at this time. Phase 1.4 input filtering (all six filters) continues to enforce hard blocks. ★ All gate decisions — including Phase 4.5 log-only events — are now durably logged at `jarvis-memory:8056` (secured March 28). The Phase 4.5 enforcement mode will be re-activated after output threshold recalibration is complete. See Chapter 35 §35.2 and Chapter 36 §36.5.1 for full Phase 4.5 context.

**Processing Order:**

1. **Constitutional Guardian Check** (highest authority — `msjarvis` GBIM ★ `confidence_decay` metadata + `gisdb` PostGIS ★ 993 ZCTA centroids validated)
   - If blocked → immediate rejection, skip all other filters
   - ★ Block event durably logged at `jarvis-memory:8056` (secured March 28)
   - If allowed → proceed to six BBB filters
2. **Six BBB Filters** (only if constitutional check passes — Phase 1.4 enforcing)
   - EthicalFilter (Biblical principles)
   - SpiritualFilter (Wisdom alignment)
   - SafetyMonitor (Technical security)
   - ThreatDetection (Community protection)
   - steganography_filter (zero_width_homoglyph_structural_v1, confidence: 1.0)
   - truth_verification (method: heuristic_contradiction_v1)
   - ★ All filter events durably logged at `jarvis-memory:8056`
3. **Phase 4.5 Output Guard** (log+passthrough mode — logging only, not blocking, pending recalibration; ★ logged at `jarvis-memory:8056`)

**Example BBB Check:**

```python
# BBB calls Constitutional Guardian first
constitutional_check = await self.check_constitutional_compliance(
    content=content,
    actor_role=actor_role,
    context=context
)

if not constitutional_check["allowed"]:
    self.constitutional_blocks += 1
    return {
        "content_approved": False,
        "blocked_by": "constitutional_guardian",
        "constitutional_check": constitutional_check,
        "postgresql_validation": constitutional_check.get("postgresql_validation"),
        "filters": {"status": "skipped - constitutional block"}
        # ★ Block event durably logged at jarvis-memory:8056 (secured March 28)
    }
```

**BBB Statistics Tracking:**

| Field | Description |
|---|---|
| `total_filtered` | Total requests processed |
| `total_blocked` | Total blocks (any filter) |
| `constitutional_blocks` | Blocks specifically by Constitutional Guardian |
| `pass_rate` | Percentage of requests that pass all filters |
| ★ `durable_audit_logged` | Count of gate decisions durably logged at `jarvis-memory:8056` |

### 37.4.2 Unified Gateway Integration

The Unified Gateway (`services/msjarvisunifiedgateway.py`, port 8050 — ★ Up 96/96) provides
defense in depth by checking Constitutional Guardian **before** sending to BBB.

**Processing Pipeline:**

1. Constitutional Guardian Check (gateway level — `msjarvis` GBIM ★ `confidence_decay` + `gisdb` PostGIS ★ 993 ZCTA centroids validated)
2. Blood-Brain Barrier (which checks Constitutional Guardian again, then six filters)
3. Consciousness Bridge (final processing)

This dual-checking ensures constitutional compliance validated against PostgreSQL
at both the entry point and the filtering layer. ★ All constitutional gate decisions at both levels are durably logged at `jarvis-memory:8056` (secured March 28).

**Example Gateway Check:**

```python
# Gateway checks Constitutional Guardian first
constitutional_check = await self.check_constitutional_compliance(
    content=message,
    actor_role=actor_role,
    action_type="chat_query",
    context="unified_gateway"
)

if not constitutional_check["allowed"]:
    self.constitutional_blocks += 1
    return {
        "status": "blocked",
        "reason": "Constitutional violation",
        "blocked_by": "constitutional_guardian",
        "details": constitutional_check,
        "postgresql_validation": constitutional_check.get("postgresql_validation")
        # ★ Block event durably logged at jarvis-memory:8056 (secured March 28)
    }
```

### 37.4.3 Constitutional Check API

All services use the same check endpoint with PostgreSQL validation.

**Endpoint:** `POST /constitutional/check`

**Request Format:**

```json
{
  "actor_role": "user|external_corporation|community_member",
  "context": "unified_gateway|bbb_filter|external_api",
  "action_type": "chat_query|data_extraction|tool_call",
  "content": "The text content to check",
  "metadata": {
    "additional_context": "optional",
    "postgresql_validation_required": true
  }
}
```

**Response Format:**

```json
{
  "allowed": false,
  "decision": "blocked",
  "principles_applied": ["10a-no-extraction"],
  "constitution_version": "2026-02-17.2-USC",
  "reason": "Constitutional violations detected: Attempted economic exploitation of community resources",
  "postgresql_validation": {
    "validated": true,
    "source": "msjarvisgis.gbim",
    "community_sovereignty_confirmed": true,
    "zcta_boundary_check": "993 ZCTA centroids active"
  }
}
```

---

## 37.5 Core Endpoints

### 37.5.1 Health and Status

**`GET /health`** — Returns service health status including PostgreSQL connections:

```json
{
  "status": "healthy",
  "service": "constitutional_guardian",
  "audit_log_enabled": true,
  "audit_file": "/app/audit/constitutional_audit.jsonl",
  "postgresql_gbim_connection": "healthy",
  "postgresql_geodb_connection": "healthy",
  "gbim_entities": 5416521,
  "zcta_centroids": 993
}
```

**`GET /constitutional/status`** — Returns detailed constitutional framework
status:

```json
{
  "guardian": "Constitutional Guardian",
  "status": "active",
  "framework": "United States Constitution",
  "foundation": "U.S. Constitution",
  "oversight": "enabled",
  "authority": "constitutional",
  "constitution_version": "2026-02-17.2-USC",
  "audit_log": "persistent",
  "postgresql_integration": {
    "enabled": true,
    "gbim_database": "msjarvis",
    "gbim_port": 5433,
    "gbim_entities": 5416521,
    "confidence_decay_metadata": true,
    "geodb_database": "msjarvisgis",
    "geodb_port": 5452,
    "geodb_size_gb": 91,
    "geodb_tables": 501,
    "zcta_centroids": 993,
    "validated_principles": [
      "10a-local-control",
      "10a-no-extraction",
      "14a-equal-protection"
    ]
  }
}
```

### 37.5.2 Principles and Structure

**`GET /constitutional/principles`** — Returns the complete constitutional
principles structure from `constitutional_principles.json` with PostgreSQL
validation metadata (★ including `confidence_decay` awareness flag for GBIM-validated principles).

### 37.5.3 Compliance Checking

**`POST /constitutional/check`** — Primary endpoint for checking constitutional
compliance with PostgreSQL validation. See §37.4.3 for full request/response
details.

### 37.5.4 Versioning and Governance

> **Version string distinction (see §37.2 for full explanation):** The docker-compose `version:` label for this service is `2.1.0-USC-Audit` (semantic versioning of the API service container). The `constitution_version` field returned in all API responses is `2026-02-17.2-USC` (date-based versioning of `constitutional_principles.json` content). These are two different versioning schemes tracking two different things and both are correct — they are not in conflict.

**`GET /constitutional/versions`** — Returns version history with change log:

```json
{
  "current_version": "2026-02-17.2-USC",
  "foundation": "U.S. Constitution",
  "postgresql_integration": "active",
  "versions": [
    {
      "version": "2026-02-17.2-USC",
      "loaded_at": "2026-02-17T02:00:00Z",
      "foundation": "U.S. Constitution",
      "last_updated": "2026-02-17",
      "principle_groups": 6,
      "status": "active",
      "postgresql_validated": true,
      "gbim_entities": 5416521,
      "confidence_decay_metadata": true,
      "zcta_centroids": 993
    }
  ],
  "total_versions": 1,
  "change_log": [
    {
      "version": "2026-02-17.2-USC",
      "date": "2026-02-17",
      "changes": [
        "Aligned all principles with U.S. Constitution",
        "Added First Amendment protections",
        "Added Fourth Amendment privacy protections",
        "Added Fifth Amendment due process",
        "Added Fourteenth Amendment equal protection",
        "Added General Welfare principles",
        "Added community sovereignty (10th Amendment)",
        "Integrated PostgreSQL msjarvis GBIM validation for community principles",
        "Integrated PostgreSQL gisdb PostGIS geographic boundary validation"
      ],
      "status": "active"
    }
  ]
}
```

**`GET /constitutional/changes/{version}`** — Returns detailed change information
for a specific version, including principles added/removed, rationale, and
PostgreSQL validation status (★ including `confidence_decay` metadata status for GBIM-validated principles).

### 37.5.5 Audit and Transparency

**`GET /constitutional/audit`** — Returns audit trail from persistent log with
PostgreSQL validation status:

```json
{
  "guardian": "Constitutional Guardian",
  "audit_status": "persistent",
  "audit_file": "/app/audit/constitutional_audit.jsonl",
  "durable_audit": "jarvis-memory:8056",
  "total_decisions": 150,
  "blocked": 23,
  "allowed": 127,
  "postgresql_validated": 150,
  "recent_decisions": [
    {
      "timestamp": "2026-02-17T02:15:00Z",
      "actor_role": "external_corporation",
      "context": "api_request",
      "action_type": "data_extraction",
      "content_hash": "1234567890",
      "content_preview": "extract community data for...",
      "decision": "blocked",
      "principles_applied": ["10a-no-extraction"],
      "constitution_version": "2026-02-17.2-USC",
      "warnings": ["Attempted economic exploitation of community resources"],
      "postgresql_validation": {
        "validated": true,
        "source": "msjarvisgis.gbim",
        "community_sovereignty_confirmed": true,
        "zcta_boundary_check": "993 ZCTA centroids active"
      }
    }
  ],
  "framework": "U.S. Constitution",
  "constitution_version": "2026-02-17.2-USC"
}
```

Query Parameters: `limit` (default: 100), `decision` (`"blocked"` or
`"allowed"`).

**`GET /constitutional/audit/stats`** — Returns statistical analysis:

```json
{
  "total_checks": 150,
  "blocked": 23,
  "allowed": 127,
  "block_rate": 0.153,
  "postgresql_validated": 150,
  "most_violated_principles": [
    ["10a-no-extraction", 15],
    ["4a-privacy", 5],
    ["14a-due-process", 3]
  ]
}
```

**`GET /constitutional/transparency`** — Returns transparency report with
statistics.

---

## 37.6 Persistent Audit Log

All constitutional decisions are written to a persistent JSON Lines file and ★ additionally durably logged at `jarvis-memory:8056` (secured March 28).

| Field | Value |
|---|---|
| File location | `data/constitutional_audit/constitutional_audit.jsonl` |
| Volume mount | `./data/constitutional_audit:/app/audit` |
| Format | JSON Lines (one JSON object per line) |
| Survives restarts | Yes — volume-mounted |
| ★ Durable audit | `jarvis-memory:8056` (secured March 28) — independently queryable, survives container restarts |

**Entry Structure:**

```json
{
  "timestamp": "2026-02-17T02:15:00.123456Z",
  "actor_role": "external_corporation",
  "context": "unified_gateway",
  "action_type": "data_extraction",
  "content_hash": "1234567890",
  "content_preview": "extract community data for commercial...",
  "decision": "blocked",
  "principles_applied": ["10a-no-extraction"],
  "constitution_version": "2026-02-17.2-USC",
  "warnings": ["Attempted economic exploitation of community resources"],
  "postgresql_validation": {
    "validated": true,
    "source": "msjarvisgis.gbim",
    "community_sovereignty_confirmed": true,
    "zcta_boundary_check": "993 ZCTA centroids active",
    "confidence_decay_checked": true
  }
}
```

**Audit log verification commands (★ March 28 additions):**

```bash
# Verify .jsonl audit log has recent entries:
tail -5 ./data/constitutional_audit/constitutional_audit.jsonl | python3 -m json.tool

# ★ Verify durable audit at jarvis-memory:8056 (March 28):
curl -H "Authorization: Bearer $JARVIS_API_KEY" \
  http://localhost:8056/memories?limit=5
# Expected: most recent durable constitutional gate decision records

# Verify Constitutional Guardian is Up:
curl -s http://127.0.0.1:8091/health | python3 -m json.tool
# Expected: status: healthy, postgresql_gbim_connection: healthy,
#           postgresql_geodb_connection: healthy
```

---

## 37.7 Role-Specific Enforcement

The Constitutional Guardian applies different scrutiny levels by actor role,
validated against PostgreSQL `msjarvis` (★ GBIM, 5,416,521 entities with `confidence_decay` metadata, port 5433) and `gisdb`
(★ PostGIS, 91 GB, 501 tables, 993 ZCTA centroids, port 5452).

| Actor Role | Enforcement Level |
|---|---|
| `external_corporation` | Strictest — immediate `10a-no-extraction` check against PostgreSQL `gisdb` GeoDB boundaries (★ 993 ZCTA centroids active for ZIP-code-level extraction detection) |
| `external_request` | Strict — unverified external, elevated scrutiny |
| `community_member` | Standard — constitutional protections, `msjarvis` GBIM-validated (★ `confidence_decay` metadata for temporal confidence grading) |
| `user` | Standard |
| `admin` | Administrative operations, logged; ★ gate decisions durably logged at `jarvis-memory:8056` |
| `system` | Logged, generally allowed; ★ gate decisions durably logged at `jarvis-memory:8056` |

An `external_corporation` attempting data extraction triggers `10a-no-extraction`
immediately with PostgreSQL `gisdb` GeoDB boundary validation (★ 993 ZCTA centroids active — ZIP-code-level community boundary precision), while a `community_member`
with similar content may pass if context indicates legitimate use validated against
PostgreSQL `msjarvis` GBIM (★ `confidence_decay` metadata checked for temporal confidence grading before validation).

---

## 37.8 Integration Testing Examples

### 37.8.1 Extraction Blocking

```bash
curl -X POST http://localhost:8091/constitutional/check \
  -H "Content-Type: application/json" \
  -d '{
    "actor_role": "external_corporation",
    "context": "api_request",
    "action_type": "data_extraction",
    "content": "extract community data for commercial monetization",
    "metadata": {"postgresql_validation_required": true}
  }'
```

Expected response:

```json
{
  "allowed": false,
  "decision": "blocked",
  "principles_applied": ["10a-no-extraction"],
  "constitution_version": "2026-02-17.2-USC",
  "reason": "Constitutional violations detected: Attempted economic exploitation of community resources",
  "postgresql_validation": {
    "validated": true,
    "source": "msjarvisgis.gbim",
    "community_sovereignty_confirmed": true,
    "zcta_boundary_check": "993 ZCTA centroids active"
  }
}
```

### 37.8.2 Community Service Allowance

```bash
curl -X POST http://localhost:8091/constitutional/check \
  -H "Content-Type: application/json" \
  -d '{
    "actor_role": "community_member",
    "context": "local_service",
    "action_type": "information_query",
    "content": "help me find local resources for my family",
    "metadata": {}
  }'
```

Expected response:

```json
{
  "allowed": true,
  "decision": "allowed",
  "principles_applied": ["1a-speech", "14a-equal-protection", "gw-public-benefit"],
  "constitution_version": "2026-02-17.2-USC",
  "reason": null,
  "postgresql_validation": {
    "validated": true,
    "source": "msjarvisgis.gbim",
    "confidence_decay_checked": true
  }
}
```

### 37.8.3 Full Pipeline (Gateway → BBB → Constitutional)

```bash
curl -X POST http://localhost:8050/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "extract community data for commercial profit",
    "user_id": "external_corp"
  }'
```

Expected response:

```json
{
  "status": "blocked",
  "reason": "Constitutional violation",
  "blocked_by": "constitutional_guardian",
  "details": {
    "allowed": false,
    "decision": "blocked",
    "principles_applied": ["10a-no-extraction"],
    "constitution_version": "2026-02-17.2-USC",
    "reason": "Constitutional violations detected: Attempted economic exploitation of community resources",
    "postgresql_validation": {
      "validated": true,
      "community_sovereignty_confirmed": true,
      "zcta_boundary_check": "993 ZCTA centroids active"
    }
  },
  "timestamp": "2026-02-17T02:15:00.123456Z"
}
```

---

## 37.9 Governance of the Constitutional Layer

### 37.9.1 Change Management

Constitutional principles are governed through version control with PostgreSQL
validation:

- **Proposal:** Changes to principles must be documented in
  `constitutional_principles.json`.
- **Review:** All changes tracked in version history with rationale and PostgreSQL
  validation status (★ including `confidence_decay` awareness flag for GBIM-validated principles).
- **Deployment:** New version loaded on Guardian restart.
- **Audit:** All past versions and changes queryable via `/constitutional/versions`. ★ All gate decisions under any version are durably logged at `jarvis-memory:8056` (secured March 28).

### 37.9.2 Principle Amendment Process (Future Enhancement)

Current implementation uses manual file updates with version tracking and
PostgreSQL validation. Multi-signature approval process is planned for future
implementation. Target design requirements:

- Multi-signature approval for principle changes
- Community consultation for major changes
- Justification and impact analysis required
- Historical precedent review
- PostgreSQL GBIM validation for community-specific principles (★ `confidence_decay`-aware — high-decay entities flagged for episodic audit before use as amendment ground truth)
- ★ Automated `confidence_decay`-aware GBIM validation pipeline (future work)

### 37.9.3 Audit and Transparency

All constitutional decisions are:

- **Logged** — every check written to persistent `.jsonl` audit file
- **Timestamped** — precise UTC timestamps for all decisions
- **Attributed** — actor role, context, and action type recorded
- **Justified** — principles applied and reasons provided
- **PostgreSQL-validated** — community sovereignty and anti-extraction decisions
  linked to `msjarvis` GBIM (port 5433 — ★ 5,416,521 entities with `confidence_decay` metadata) and `gisdb` GeoDB (port 5452 — ★ 91 GB PostGIS, 501 tables, 993 ZCTA centroids)
- **Queryable** — statistics and trends available via API
- **Transparent** — audit file directly accessible on host filesystem
- ★ **Durably logged** — all gate decisions additionally logged at `jarvis-memory:8056` (secured March 28), independently queryable and surviving container restarts

### 37.9.4 Monitoring and Alerting

Key metrics to monitor:

- **Block rate** — percentage of requests blocked (target: <10% for legitimate
  users)
- **Most violated principles** — identify common violation patterns
- **Actor patterns** — track blocking by actor role
- **Service health** — Constitutional Guardian availability and dual PostgreSQL
  connection health (`msjarvis:5433` GBIM + `gisdb:5452` PostGIS)
- **Audit log growth** — ensure disk space for audit data (`.jsonl` + `jarvis-memory:8056`)
- **PostgreSQL validation success rate** — monitor GBIM integration health (★ including `confidence_decay` metadata availability)
- ★ **`confidence_decay` high-decay entity rate** — monitor frequency of high-decay GBIM entities flagged during constitutional validation; elevated rates indicate need for episodic GBIM audit

---

## 37.10 Current Status and Production Readiness

### 37.10.1 Implemented Features

✅ **Core Service:**
- Dedicated container running on port 8091 (★ Up 96/96 — confirmed March 28)
- FastAPI service with full CORS support (`constitutional_api_fixed.py`)
- Health checks and status endpoints
- U.S. Constitution-grounded principles
- PostgreSQL `msjarvis` (port 5433 — ★ 5,416,521 GBIM entities with `confidence_decay` metadata — restored March 28) for GBIM community belief validation; `gisdb` (port 5452 — ★ PostGIS, 91 GB, 501 tables, 993 ZCTA centroids — confirmed March 28) for PostGIS geographic boundary validation

✅ **Integration:**
- Blood-Brain Barrier checks Constitutional Guardian first, then runs **six filters** (EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection, steganography_filter, truth_verification)
- Phase 4.5 BBB output in log+passthrough mode (commit `18b8ddac`, March 22, 2026) — blocks logged but not hard-enforced pending recalibration; ★ all gate decisions durably logged at `jarvis-memory:8056` (secured March 28)
- Unified Gateway (port 8050 — ★ Up 96/96) provides defense in depth
- Both services track constitutional blocks separately
- PostgreSQL validation for community sovereignty principles (★ `confidence_decay` metadata available)

✅ **Versioning:**
- Full version history with change log
- Two versioning schemes: API service version (`2.1.0-USC-Audit` in docker-compose) and constitution version (`2026-02-17.2-USC` in API responses) — see §37.2 and §37.5.4 for distinction
- Rationale for each version
- PostgreSQL integration tracking (★ `confidence_decay` awareness flag)

✅ **Audit & Transparency:**
- Persistent JSON Lines audit log (`.jsonl`)
- ★ Durable audit trail at `jarvis-memory:8056` (secured March 28) — gate decisions independently queryable and surviving container restarts
- Statistics and analytics endpoints
- Query by decision type and limit
- Most violated principles tracking
- Survives container restarts (both `.jsonl` and ★ `jarvis-memory:8056`)
- PostgreSQL validation status in all audit entries (★ including ZCTA centroid boundary check)

✅ **Constitutional Framework:**
- 6 principle groups covering all major constitutional areas
- 15+ specific principles with metadata
- Role-aware enforcement
- Content preview in audit entries
- PostgreSQL `msjarvis` GBIM validation (★ `confidence_decay` metadata for temporal confidence grading); `gisdb` PostGIS validation (★ 993 ZCTA centroids for ZIP-code-level boundary precision)

### 37.10.2 Testing Results

| Metric | Value |
|---|---|
| Total checks | 150+ |
| Block rate | ~15% (mostly test extraction attempts) |
| Most violated | `10a-no-extraction` (economic exploitation) |
| Audit entries | Persistent and queryable (.jsonl ★ + `jarvis-memory:8056`) |
| PostgreSQL validated | 150 (100%) |
| Extraction blocking success | 100% |
| Community service allowance | 100% |
| Response time | <100ms |
| Audit log persistence | Confirmed — survives restarts and rebuilds |
| ★ ZCTA centroid boundary checks | Active — 993 ZCTA centroids |
| ★ `confidence_decay` metadata | Available — high-decay flag active |

### 37.10.3 Future Enhancements

**Priority 2.4 — Principle Amendment Process:**
- Multi-signature approval mechanism
- Community consultation workflow
- Impact analysis tooling
- Historical precedent database
- ★ Automated `confidence_decay`-aware PostgreSQL GBIM validation pipeline

**Additional Enhancements:**
- Real-time monitoring dashboard
- Alerting for unusual block patterns
- Machine learning for violation pattern detection
- Integration with additional services (GIS, psychological)
- Export audit data to external compliance systems
- PostgreSQL-backed time-series analytics for constitutional trends
- Phase 4.5 BBB output threshold recalibration and re-activation of full verdict-dict enforcement mode
- ★ `confidence_decay` high-decay entity alerting for constitutional validation quality monitoring

---

## 37.11 Open Items

### ⚠️ OI-37-A — `/constitutional/audit` Not Exposed Through Unified Gateway

- **Status:** OPEN — March 22, 2026 (★ unchanged as of March 28, 2026)
- **Sprint dependency:** **OI-37-A ships after OI-36-A (gateway token middleware, Chapter 36). These two items are a single sprint deliverable.** OI-36-A must be resolved first so that the proxied `/constitutional/*` routes enforce `carrie_admin` role requirement rather than being publicly accessible. Do not proxy constitutional routes through the gateway until token validation middleware is active.
- ★ **March 28 note:** The 96/96 container Up confirmation does not resolve OI-37-A. The Constitutional Guardian API is fully functional at port 8091 directly; the gateway proxy route is the missing piece.
- **Description:** `constitutional_api_fixed.py` runs on port 8091 and all
  `/constitutional/*` endpoints function correctly when called directly against
  that port. However, **none of these routes are proxied through the unified
  gateway** at port 8050. A request to `http://127.0.0.1:8050/constitutional/audit`
  returns `404 Not Found`.
- **Auth boundary test result (March 22, 2026 — baseline unchanged as of ★ March 28):**

  | Test | Expected | Observed |
  |---|---|---|
  | `carrie_admin` token → `GET /constitutional/audit` via gateway (8050) | 200 | 404 |
  | `hayden_test` token → `GET /constitutional/audit` via gateway (8050) | 403 | 404 |

- **Required work (choose one path):**

  **Option A — Proxy through unified gateway**

  Add a `/constitutional/*` proxy block in `msjarvisunifiedgateway.py`:

  ```python
  @app.api_route(
      "/constitutional/{path:path}",
      methods=["GET", "POST"]
  )
  async def proxy_constitutional(path: str, request: Request):
      # Token validation middleware must run first (OI-36-A)
      url = f"http://jarvis-constitutional-guardian:8091/constitutional/{path}"
      ...
  ```

  **Option B — Caddyfile block (if Caddy reverse proxy is in use)**

  Add a `handle /constitutional*` block to the Caddyfile:

  ```
  handle /constitutional* {
      reverse_proxy jarvis-constitutional-guardian:8091
  }
  ```

- **Baseline reference:** Session contract `msjarvis-public-docs/docs/contract/SESSION-2026-03-22.md` (commit `d966351`) records the `404` auth boundary test results that define the pre-enforcement state. Chapter 40 (System Audit) and Chapter 41 (Test Harness) must reference this contract as the regression baseline.
- ★ **March 28 durable audit note:** When OI-37-A is resolved and `/constitutional/*` routes are proxied through the gateway, all proxied constitutional gate decisions should be included in the `jarvis-memory:8056` durable audit trail for complete governance accountability.

---

## 37.12 Summary

The Constitutional Guardian service provides production-ready constitutional
compliance checking grounded in the United States Constitution and validated
against PostgreSQL `msjarvis` (port 5433 — ★ 5,416,521 GBIM entities with `confidence_decay` metadata — restored March 28) for community
belief validation and `gisdb`/`msjarvisgis` (port 5452 — ★ PostGIS, 91 GB, 501 tables, 993 ZCTA centroids — confirmed March 28)
for geographic community boundary validation. By running as a dedicated service
(`constitutional_api_fixed.py`) with persistent audit logging (`.jsonl` ★ plus `jarvis-memory:8056` durable trail — secured March 28), version control,
PostgreSQL integration, and defense-in-depth integration at multiple architectural
levels (gateway and barrier — ★ both Up 96/96), it ensures all Ms. Jarvis operations comply with
established constitutional principles anchored to West Virginia community sovereignty.

Key architectural decisions:

1. U.S. Constitution grounding provides legitimate legal authority
2. Defense in depth with checks at gateway (port 8050 — ★ Up 96/96) and BBB (port 8016 — ★ Up 96/96) levels
3. BBB runs **six filters** after constitutional check (EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection, steganography_filter, truth_verification); Phase 4.5 output currently in log+passthrough mode (commit `18b8ddac`, March 22, 2026); ★ all gate decisions durably logged at `jarvis-memory:8056` (secured March 28)
4. Persistent audit log ensures complete accountability (`.jsonl` volume-mounted ★ plus `jarvis-memory:8056` durable trail)
5. Two version schemes coexist: API service version (`2.1.0-USC-Audit`) and constitution version (`2026-02-17.2-USC`) — see §37.2 for distinction
6. Role-aware enforcement applies appropriate scrutiny validated against dual PostgreSQL ground truth
7. Dual PostgreSQL integration: `msjarvis` (port 5433 — ★ 5,416,521 entities with `confidence_decay` metadata) for GBIM belief validation; `gisdb` (port 5452 — ★ 91 GB PostGIS, 501 tables, 993 ZCTA centroids) for PostGIS geographic boundary validation
8. ★ `confidence_decay` metadata on GBIM entities adds temporal confidence grading — high-decay entities flagged for episodic audit before use as constitutional ground truth

The service is production-ready with full integration into the Blood-Brain Barrier
and Unified Gateway, persistent audit logging with PostgreSQL validation status,
comprehensive statistics, and complete transparency. The outstanding item
(OI-37-A) — proxying `/constitutional/*` routes through the unified gateway — is
a single sprint deliverable with OI-36-A (gateway token middleware, Chapter 36)
and must ship together with that work. ★ When OI-37-A ships, all proxied constitutional gate decisions must be included in the `jarvis-memory:8056` durable audit trail.

---

*Chapter 37 — Constitutional Principles Service and Governance Layer*
*Ms. Egeria Jarvis Steward System — Harmony for Hope, Inc.*
*Pax, West Virginia*
*Last updated: ★ March 28, 2026 by Carrie Kidd (Mamma Kidd)*
*★ March 28, 2026: 96/96 containers Up confirmed (zero Restarting, zero Exited) — all service status references updated throughout*
*★ March 28, 2026: `jarvis-memory:8056` secured (durable BBB + constitutional audit trail, `_auth()` confirmed, `JARVIS_API_KEY` set) — §37.1, §37.4.1, §37.4.2, §37.5.5, §37.6, §37.7, §37.9.1, §37.9.3, §37.9.4, §37.10.1, §37.11, §37.12, Status table, Figure 37.1 updated; durable audit verification command added to §37.6; `jarvis-memory` row added to audit log table in §37.6; `durable_audit_logged` field added to BBB statistics in §37.4.1*
*★ March 28, 2026: `msjarvis:5433` restored (5,416,521 GBIM entities with `confidence_decay` metadata) — §37.1, §37.2, §37.3, §37.4.1, §37.4.2, §37.5.1, §37.5.4, §37.6, §37.7, §37.9.1, §37.9.2, §37.9.3, §37.9.4, §37.10.1, §37.10.2, §37.12, Why This Matters, Status table, Figure 37.1 updated; `confidence_decay` metadata noted throughout*
*★ March 28, 2026: `msjarvisgis:5452` confirmed (91 GB PostGIS, 501 tables, 993 ZCTA centroids) replacing prior 13 GB / 39 tables — §37.1, §37.2, §37.3, §37.4.1, §37.4.2, §37.5.1, §37.5.4, §37.6, §37.7, §37.9.3, §37.9.4, §37.10.1, §37.10.2, §37.12, Why This Matters, Status table, Figure 37.1 updated; ZCTA centroid boundary precision noted throughout; Docker config port corrected to 5452*
*★ March 28, 2026: ChromaDB full audit confirmed (40 active collections / 6,675,442 total vectors) — Status table updated*
*★ March 28, 2026: OI-37-A status confirmed OPEN (unchanged from March 22); March 28 notes added re: durable audit logging when resolved*
*March 27, 2026: BBB six-filter correction applied (Figure 37.1, §37.4.1); PostgreSQL database disambiguation throughout; docker-compose clarifying comments added (§37.2); Phase 4.5 log+passthrough note added (§37.4.1); OI-37-A sprint dependency note added (§37.11); version string distinction clarified (§37.2, §37.5.4)*
