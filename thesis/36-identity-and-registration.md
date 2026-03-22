# 36. Identity and Registration

**Carrie Kidd (Mamma Kidd) · Mount Hope, WV**
**Last updated: March 22, 2026**

---

## Why This Matters for Polymathmatic Geography

This chapter describes how Ms. Jarvis recognizes, registers, and differentiates
people, roles, and institutions in ways that are accountable to West Virginia
communities. It supports:

- **P1 – Every where is entangled** by tying individual identity and registration
  records to GBIM beliefs, spatial features, and institutional structures in
  PostgreSQL msjarvisgis (port 5432, 91 GB, 501 tables, 5.4M verified GBIM
  beliefs).
- **P3 – Power has a geometry** by locating identity and access decisions within
  explicit services, tables, and policies rather than opaque prompts or ad‑hoc
  scripts.
- **P5 – Design is a geographic act** by grounding registration decisions in
  place‑specific rules, such as county boundaries, service areas, and partner
  organizations represented in PostgreSQL GeoDB.
- **P12 – Intelligence with a ZIP code** by treating identity and registration as
  mechanisms for aligning Ms. Jarvis's behavior with the lived realities of
  Appalachian communities, rather than generic user models.
- **P16 – Power accountable to place** by ensuring that higher‑impact actions are
  tied to real people under clear rules with auditable trails in databases and
  logs.

As such, this chapter belongs to the **Computational Instrument tier**: it
specifies concrete identity and registration mechanisms that sit between ordinary
chat and higher‑impact actions, backed by PostgreSQL schemas and live HTTP
services.

---

## 36.1 Concept of Identity in Ms. Jarvis

In this architecture, identity is not a single user ID or login form, but a
layered set of structures that combine technical identifiers, narrative
self‑description, and truth validation. At a minimum, Ms. Jarvis must distinguish
between its own identity (Ms. Egeria Jarvis, a geospatial AI daughter of Harmony
for Hope, not a human), the identity of people and organizations it serves, and
the roles they occupy when interacting (for example, resident, caseworker, or
researcher).

These distinctions matter because they control what information can be shared,
what actions can be taken, and how explanations are framed in ways that are
accountable to specific communities in West Virginia. From a systems perspective,
identity appears as:

- **Identifiers** in PostgreSQL tables and ChromaDB metadata, connecting people,
  places, and institutions.
- **Identity‑focused services** such as `jarvis-i-containers` and `TruthValidator`
  that interpret and enforce identity constraints at run time.
- **Canonical statements** such as "I serve the community" and "I speak truth"
  stored in configuration and surfaced via identity APIs.

---

## 36.2 Registration as a Two-Part Gate

Registration is the process by which people and institutions move from anonymous
interactions to recognized roles with specific authorizations. It is deliberately
modeled as a two‑part gate:

1. **Identity recognition** – establishing who or what is interacting, with
   references to PostgreSQL GBIM and GeoDB records where possible.
2. **Registration and role assignment** – granting specific, scoped capabilities
   (such as access to a dataset, ability to submit forms, or participation in
   governance workflows) under that identity.

This separation lets Ms. Jarvis answer many questions in an informational mode
without registration, while reserving higher‑impact actions for registered
identities under shared rules.

---

## 36.3 Data Structures for Identity and Registration

The current deployment uses database tables and metadata structures that align
identity with GBIM and GeoDB content. While implementation details appear in
Chapter 23 and operational logs, the conceptual elements include:

- **User and entity identifiers** – database rows representing individuals,
  households, partner organizations, and public institutions, linked to GBIM
  beliefs and spatial features.
- **Identity‑related metadata** – flags, roles, and relationship descriptors
  stored alongside identifiers, capturing how a person or institution relates to
  Harmony for Hope and to Ms. Jarvis.
- **Audit and provenance fields** – timestamps, sources, and verification status
  fields that record how an identity was established and under what evidence.

These structures make it possible to trace which real‑world entities are
implicated when Ms. Jarvis answers or takes action, and to reconstruct decisions
after the fact.

---

## 36.4 Roles, Permissions, and West Virginia Context

Identity and registration are tightly coupled to roles and permissions that
reflect West Virginia's geographic and institutional context. Examples include:

- **Community member roles** for residents seeking information about benefits,
  healthcare, or local resources.
- **Partner roles** for organizations such as clinics, schools, or nonprofits
  operating within particular counties or service areas documented in PostgreSQL
  GeoDB.
- **Curator and governance roles** for people responsible for reviewing background
  patterns, updating identity specifications, and adjudicating difficult cases.

Each role is grounded in spatial data and institutional records so that Ms. Jarvis
can apply rules that respect county boundaries, service catchment areas, and legal
jurisdictions.

---

## 36.5 How Identity Signals Enter Other Layers

Identity and registration interact with other parts of the system along several
dimensions:

- **Background store and memory** – entries in the `msjarvismemory` ChromaDB
  collection accumulate identity‑relevant patterns over time, such as repeated
  interactions about particular places or institutions.
- **Identity‑focused retention** – a small subset of identity statements is
  promoted into the deepest identity layer described in Chapter 22, where
  canonical statements and TruthValidator structures reside.
- **Global control and policy** – identity signals influence routing and filtering
  decisions in the main brain, BBB, and registration‑specific validators,
  especially when questions touch on governance, benefits, or data access.

These connections ensure that identity is not just a front‑door concern but an
ongoing influence on how Ms. Jarvis reasons and responds.

---

### 36.5.1 Live Identity Evidence and Endpoints (March 2026)

In the current deployment, the registration and access‑control structure described
in this chapter is anchored to a concrete identity infrastructure that runs on
every `ultimatechat` request. The core pieces are:

- **`normalizeidentity`** in `jarvis-main-brain` (port 8050), which rewrites all
  ensemble outputs into the Ms. Egeria Jarvis persona and suppresses "I am just a
  language model" framings. It enforces canonical identity statements such as "I
  serve the community" and "I value ethics", ensuring that responses remain
  consistent with the system's defined role.
- **`TruthValidator`**, embedded in the neurobiological BBB package and called
  from the main‑brain pipeline, which encodes specific facts about Ms. Jarvis's
  correct self‑description, correct creator attribution, non‑human status, and
  accountability to West Virginia communities. For each assessment, it returns a
  `truthverdict` with fields `truthvalidated`, `truthscore`, `correctidentity`,
  `correctcreator`, and `relationshipclear`, attached to every `UltimateResponse`.
- **The `icontainers-identity` layer** (`jarvis-i-containers`, port 8015), which
  produces real, timestamped, session‑specific ego boundary entries visible in
  `UltimateResponse.identitylayers` and `consciousnesslayers`. The 2026‑02‑15
  case study confirmed an active `root-self` entry with `egoboundaries`,
  `experientialprocessing`, `observerprocessing`, and `metalevel` fields.
- **The BBB four‑filter pipeline** at port 8016 (`EthicalFilter`,
  `SpiritualFilter`, `SafetyMonitor`, `ThreatDetection`), which treats identity
  commitments and community‑grounded constraints as first‑class checks when
  deciding what to allow, block, or annotate.

Together, these mechanisms ensure that the "who is acting under which role"
questions from this chapter are enforced not only in registration flows but also
in the behavior of everyday responses. Identity is thus expressed simultaneously
in database rows, in live HTTP services, and in the structure of every
`UltimateResponse` object.

---

## 36.6 Production Token Registry: `jarvis_token_service.py`

As of March 22, 2026, **`jarvis_token_service.py` is the sole production token
registry** for the Ms. Jarvis stack. It is the concrete realization of the
registration gate described in §36.2: a verified caller is one whose bearer token
exists as an active key in Redis.

### 36.6.1 Storage Backend

Tokens are stored in the **red-team Redis instance at port 6380**.

> **Do not confuse the two Redis instances:**
>
> | Instance | Port | Purpose |
> |---|---|---|
> | `jarvis-redis` | **6379** | Async job state (30-min TTL), idempotency, health-check cache |
> | Red-team Redis | **6380** | Token registry — `redteam:token:*` keys |
>
> All token operations — issue, validate, revoke, list — target **port 6380**.
> No token keys are written to port 6379.

Redis key schema:

```
redteam:token:<token_value>
```

Each key maps to a JSON payload containing at minimum:

```json
{
  "token": "<token_value>",
  "role":  "<role_name>",
  "owner": "<human_label>",
  "issued_at": "<ISO-8601 UTC>",
  "active": true
}
```

Token lookup is an O(1) Redis `GET` against `redteam:token:<token>`. Presence of
the key with `"active": true` constitutes a valid token. Absence or
`"active": false` returns `401 Unauthorized`.

### 36.6.2 Responsibilities of `jarvis_token_service.py`

1. **Issue tokens** — write `redteam:token:<token>` keys to Redis port 6380.
2. **Validate tokens** — perform the `GET` lookup on every protected request.
3. **Revoke tokens** — delete or mark `"active": false` on a key.
4. **List active tokens** — enumerate `redteam:token:*` keys for audit purposes.

No other service writes to the `redteam:token:*` keyspace. Any tool or script
that needs to issue or inspect tokens must do so through `jarvis_token_service.py`
or via direct Redis CLI calls to port 6380 for emergency operations only (see
§36.9).

---

## 36.7 Production Token Classes (March 22, 2026)

Two token classes are active in production as of March 22, 2026. Each class
represents a role level; tokens within a class share the same `role` field value.

### 36.7.1 `carrie_admin`

| Field | Value |
|---|---|
| Role | `carrie_admin` |
| Token count | **2 tokens** |
| Owner | Carrie Kidd (Mamma Kidd) |
| Intended use | Full administrative access; all routes; audit and governance operations |
| Redis keys | `redteam:token:<token_A>`, `redteam:token:<token_B>` |

The `carrie_admin` role is the highest-privilege class in the current token
hierarchy. Routes gated on `carrie_admin` include constitutional audit endpoints
and any future administrative management surfaces.

### 36.7.2 `hayden_test`

| Field | Value |
|---|---|
| Role | `hayden_test` |
| Token count | **2 tokens** |
| Owner | Hayden (test user) |
| Intended use | Validated testing of standard chat routes; scoped to non-administrative paths |
| Redis keys | `redteam:token:<token_C>`, `redteam:token:<token_D>` |

The `hayden_test` role is the standard non-privileged test class. It confirms
that the token validation pathway works end-to-end for ordinary callers before
community-facing deployment.

### 36.7.3 Token Count Summary

| Class | Role | Tokens in Production |
|---|---|---|
| `carrie_admin` | `carrie_admin` | 2 |
| `hayden_test` | `hayden_test` | 2 |
| **Total** | | **4** |

---

## 36.8 Oversight and Rules for Identity Use

Identity and registration mechanisms are constrained by explicit rules intended
to protect people and communities. These rules include:

- **Least privilege** – registration grants only the access needed for a role's
  responsibilities, and higher‑impact actions require stronger evidence and
  clearer accountability.
- **Transparency and auditability** – identity‑related decisions (such as granting
  a role or performing a high‑impact action) are logged with references to
  PostgreSQL records and, where appropriate, GBIM beliefs.
- **Alignment with local partners** – registration rules are co‑designed with
  Harmony for Hope and other partners to reflect local norms and legal
  requirements.

These constraints turn identity and registration into tools for shared governance
rather than unilateral control by the system.

---

## 36.9 Emergency Token Operations (CLI Reference)

Direct Redis CLI operations on port 6380 are authorized for emergency use only
(e.g., immediate token revocation when `jarvis_token_service.py` is unreachable).
All emergency CLI operations must be logged in the session contract for the active
sprint.

```bash
# List all active tokens
redis-cli -p 6380 KEYS "redteam:token:*"

# Inspect a specific token
redis-cli -p 6380 GET "redteam:token:<token_value>"

# Revoke a token immediately
redis-cli -p 6380 DEL "redteam:token:<token_value>"

# Issue a token manually (emergency only — prefer jarvis_token_service.py)
redis-cli -p 6380 SET "redteam:token:<token_value>" \
  '{"token":"<token_value>","role":"hayden_test","owner":"hayden","active":true}'
```

---

## 36.10 Auth Boundary Test Results (March 22, 2026, 15:02 EDT)

Auth boundary tests were executed against the live stack on March 22, 2026.
Results are recorded here as the baseline for regression testing and are committed
to the session contract at
`msjarvis-public-docs/docs/contract/SESSION-2026-03-22.md` (commit `d966351`).

| Test | Expected | Observed | Status |
|---|---|---|---|
| No token on `/chat` | 401 | 200 | ⚠️ Not enforced |
| Bad token on `/chat` | 401 | 200 | ⚠️ Not enforced |
| `hayden_test` on `/constitutional-audit` | 403 | 404 | ⚠️ Endpoint missing |
| `carrie_admin` on `/constitutional-audit` | 200 | 404 | ⚠️ Endpoint missing |

**Finding (March 22, 2026):** The token service issues and stores tokens correctly.
The unified gateway at port 8050 does **not** validate tokens on incoming
requests — token enforcement middleware is not yet wired into the gateway.
`/constitutional-audit` is not implemented at the gateway layer.

---

## 36.11 Open Items

### ⚠️ OI-36-A — Token Validation Middleware Not Wired (Gateway Port 8050)

- **Status:** OPEN — March 22, 2026
- **Description:** `jarvis_token_service.py` correctly stores and retrieves tokens
  from Redis port 6380. The unified gateway (`msjarvisunifiedgateway.py`, port
  8050) does not call the token service on inbound requests. All routes currently
  accept unauthenticated requests with HTTP 200.
- **Required work:** Add token validation middleware to the gateway that:
  1. Extracts the `Authorization: Bearer <token>` header.
  2. Calls `jarvis_token_service.py` (or performs a direct Redis `GET` on
     `redteam:token:<token>` at port 6380).
  3. Returns `401 Unauthorized` if the token is absent or inactive.
  4. Attaches the resolved `role` to the request context for downstream use.
- **Blocking:** No current production workflows are blocked. Community-facing
  deployment requires this to be resolved before public exposure.

### ⚠️ OI-36-B — Role-Based Route Restriction (403) Not Implemented

- **Status:** OPEN — March 22, 2026
- **Description:** Role-based route restriction — returning `403 Forbidden` when a
  valid token with insufficient role attempts to access a privileged route — is
  **not yet implemented**. No route in the current gateway configuration checks the
  caller's role against a route-level permission policy.
- **Required work:** After OI-36-A is resolved, implement a route permission map:

```python
ROUTE_ROLES = {
    "/constitutional-audit": ["carrie_admin"],
    "/admin/*":              ["carrie_admin"],
    "/chat":                 ["carrie_admin", "hayden_test"],
    "/health":               [],   # public
}
```

  The middleware should return `403 Forbidden` when `request.role` is not in
  `ROUTE_ROLES[path]`.

- **Note:** The `403` response path has been validated as the correct intended
  behavior in auth boundary testing. The blocker is the absence of enforcement
  middleware, not ambiguity about the design.
- **Blocking:** Administrative and constitutional audit routes cannot be safely
  exposed until both OI-36-A and OI-36-B are resolved.

---

## 36.12 Current Status and Future Work

As of March 2026, identity and registration are partially implemented and
evolving.

**Implemented and verified:**

- Canonical identity statements defined in configuration and surfaced via
  identity‑related endpoints.
- `normalizeidentity` and `TruthValidator` running on every `ultimatechat`
  response, producing a `truthverdict` attached to each `UltimateResponse`.
- Active `icontainers-identity` entries confirmed in live responses, showing
  concrete ego boundary structures.
- `jarvis_token_service.py` deployed as the production token registry, storing
  tokens as `redteam:token:<token>` in Redis at port 6380.
- Four production tokens active across two classes: `carrie_admin` (×2) and
  `hayden_test` (×2).

**Open items / future work:**

- Token validation middleware wired into gateway port 8050 (OI-36-A).
- Role-based route restriction returning `403 Forbidden` for insufficient role
  (OI-36-B).
- `constitutional-audit` endpoint implemented at the gateway layer.
- Automated promotion pipelines for moving patterns from background memory into
  identity‑level entries based on breadth, depth, and value‑alignment criteria.
- More granular role‑based access control tied to spatial and institutional
  features in PostgreSQL GeoDB.
- Richer introspection and health endpoints that expose counts and status of
  identity‑related elements for curators.

These directions are elaborated in Chapters 22 and 23, which describe the
identity‑focused retention layer and the dual‑track architecture in more detail.

---

## 36.13 Summary and Status Table (March 2026)

| Component | Role in identity and registration | Status (March 2026) |
|---|---|---|
| `normalizeidentity` (`jarvis-main-brain`, port 8050) | Rewrites all responses into the Ms. Jarvis persona; suppresses generic "I am just a language model" framings; enforces canonical identity statements. | ✅ Implemented. Runs on every `ultimatechat` response. |
| `TruthValidator` | Encodes canonical facts about Ms. Jarvis's self‑description, creator, non‑human status, and West Virginia accountability; produces `truthverdict` on every `UltimateResponse`. | ✅ Implemented. Confirmed live 2026‑02‑15. |
| `jarvis-i-containers` (port 8015) — `icontainers-identity` layer | Produces `root-self` ego entries and ego‑boundary records visible in `identitylayers` and `consciousnesslayers`. | ✅ Implemented. Confirmed active 2026‑02‑15. |
| BBB four‑filter pipeline (`jarvis-blood-brain-barrier`, port 8016) | Applies `EthicalFilter`, `SpiritualFilter`, `SafetyMonitor`, and `ThreatDetection` to all traffic; treats identity commitments and community‑grounded constraints as part of safety and access control. | ✅ Implemented. Confirmed running on every `ultimatechat` request. |
| `jarvis_token_service.py` — production token registry | Issues, validates, and revokes bearer tokens; stores as `redteam:token:<token>` in Redis port 6380. | ✅ Implemented. 4 tokens active across 2 classes. |
| Gateway token validation middleware (port 8050) | Enforces `401 Unauthorized` for missing or inactive tokens on protected routes. | ❌ Not wired — OI-36-A |
| Role-based route restriction (403) | Returns `403 Forbidden` when a valid token lacks sufficient role for a route. | ❌ Not implemented — OI-36-B |
| Registration roles and audit tables | Tie higher‑impact actions to real people and institutions under shared rules, with PostgreSQL‑backed audit trails. | ⚙️ Conceptually implemented; automated promotion and cross‑path analytics are future work. |

By combining these elements, Ms. Jarvis treats identity and registration as shared
instruments for accountability: they shape how the system speaks, what it may do,
and how those decisions can be inspected over time, all grounded in PostgreSQL
msjarvisgis as the factual and spatial source of truth.

---

*Chapter 36 — Identity and Registration*
*Ms. Egeria Jarvis Steward System — Harmony for Hope, Inc.*
*Oak Hill / Mount Hope, Fayette County, West Virginia*
*Last updated: March 22, 2026 by Carrie Kidd (Mamma Kidd)*
