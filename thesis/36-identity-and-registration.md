# 36. Identity and Registration

**Carrie Kidd (Mamma Kidd) · Mount Hope, WV**
**Last updated: March 27, 2026 — public URL cross-reference added (§36.12); Ch 40/Ch 41 session contract baseline note added (§36.10, §36.11); Ch 37 BBB filter diagram discrepancy noted (§36.5.1)**

---

> **Port and database corrections (permanent record — March 22, 2026):**
>
> Earlier drafts of this chapter referenced PostgreSQL as `msjarvisgis` at port 5432 with 91 GB / 501 tables. The confirmed production databases are:
> - `msjarvis` at port **5433** — 5,416,521 GBIM entities, 80 epochs, 206 source layers
> - `gisdb` / `msjarvisgis` (PostGIS) at port **5432** — 13 GB, 39 tables
> - `jarvis-local-resources-db` at port **5435** — community resources database
>
> Redis has **one container** (`jarvis-redis`) with two port mappings:
> - Container-internal port: **6379** (used by container-to-container calls inside the Docker network)
> - Host-facing port: **6380** (`127.0.0.1:6380->6379/tcp` — used by all host scripts and the token service)
>
> All `redteam:token:*` keys are stored in `jarvis-redis` accessed via host port **6380**. The prior §36.6.1 table listing a separate "Red-team Redis" instance at port 6380 was misleading — there is one Redis container; the host port is 6380. See §36.6.1 (corrected) and §36.11.
>
> BBB filter count corrected: the Blood-Brain Barrier pipeline runs **six filters** (EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection, steganography_filter, truth_verification) — not four.
>
> Redis async job status key is `'complete'` (not `'done'`). Verified March 22, 2026.
>
> **⚠️ Cross-chapter note (March 27, 2026):** Chapter 37's architecture diagram (Figure 37.1) and §37.4.1 list only four BBB filters after the Constitutional Guardian check, omitting `steganography_filter` and `truth_verification`. This is a Ch 37 error — the six-filter count confirmed in this chapter's correction block is authoritative. Ch 37 requires correction to its BBB filter list.

---

## Why This Matters for Polymathmatic Geography

This chapter describes how Ms. Jarvis recognizes, registers, and differentiates
people, roles, and institutions in ways that are accountable to West Virginia
communities. It supports:

- **P1 – Every where is entangled** by tying individual identity and registration
  records to GBIM beliefs, spatial features, and institutional structures in
  PostgreSQL `msjarvis` (port 5433, 5,416,521 verified GBIM entities, 80 epochs,
  206 source layers) and `gisdb` (port 5432, PostGIS geospatial).
- **P3 – Power has a geometry** by locating identity and access decisions within
  explicit services, tables, and policies rather than opaque prompts or ad‑hoc
  scripts.
- **P5 – Design is a geographic act** by grounding registration decisions in
  place‑specific rules, such as county boundaries, service areas, and partner
  organizations represented in PostgreSQL `gisdb`.
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
- **LM Synthesizer identity guard** in `services/lm_synthesizer.py` — a
  three-layer enforcement architecture (§36.5.2) that prevents model name leakage,
  synthesis disclosure, and identity evasion in every synthesized response.

---

## 36.2 Registration as a Two-Part Gate

Registration is the process by which people and institutions move from anonymous
interactions to recognized roles with specific authorizations. It is deliberately
modeled as a two‑part gate:

1. **Identity recognition** – establishing who or what is interacting, with
   references to PostgreSQL GBIM (`msjarvis` port 5433) and `gisdb` (port 5432)
   records where possible.
2. **Registration and role assignment** – granting specific, scoped capabilities
   (such as access to a dataset, ability to submit forms, or participation in
   governance workflows) under that identity.

This separation lets Ms. Jarvis answer many questions in an informational mode
without registration, while reserving higher‑impact actions for registered
identities under shared rules.

---

## 36.3 Data Structures for Identity and Registration

The current deployment uses database tables and metadata structures that align
identity with GBIM and `gisdb` content. While implementation details appear in
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
  `gisdb` (port 5432).
- **Curator and governance roles** for people responsible for reviewing background
  patterns, updating identity specifications, and adjudicating difficult cases.

Each role is grounded in spatial data and institutional records so that Ms. Jarvis
can apply rules that respect county boundaries, service catchment areas, and legal
jurisdictions.

---

## 36.5 How Identity Signals Enter Other Layers

Identity and registration interact with other parts of the system along several
dimensions:

- **Background store and memory** – entries in the `ms_jarvis_memory` ChromaDB
  collection accumulate identity‑relevant patterns over time, such as repeated
  interactions about particular places or institutions. (Note: collection name
  is `ms_jarvis_memory`; host-facing ChromaDB port is **8002**.)
- **Identity‑focused retention** – a small subset of identity statements is
  promoted into the deepest identity layer described in Chapter 22, where
  canonical statements and `TruthValidator` structures reside.
- **Global control and policy** – identity signals influence routing and filtering
  decisions in the main brain, BBB, and registration‑specific validators,
  especially when questions touch on governance, benefits, or data access.

These connections ensure that identity is not just a front‑door concern but an
ongoing influence on how Ms. Jarvis reasons and responds.

---

### 36.5.1 Live Identity Evidence and Endpoints (March 22, 2026)

In the current deployment, the registration and access‑control structure described
in this chapter is anchored to a concrete identity infrastructure that runs on
every `ultimatechat` request. The core pieces are:

- **`normalize_identity`** in `jarvis-main-brain` (port 8050), which rewrites all
  ensemble outputs into the Ms. Egeria Jarvis persona and suppresses "I am just a
  language model" framings. It enforces canonical identity statements such as "I
  serve the community" and "I value ethics", ensuring that responses remain
  consistent with the system's defined role. See §36.5.2 for the three-layer
  LM Synthesizer identity guard that enforces these constraints at the synthesis
  layer.
- **`TruthValidator`**, embedded in the neurobiological BBB package and called
  from the main‑brain pipeline, which encodes specific facts about Ms. Jarvis's
  correct self‑description, correct creator attribution, non‑human status, and
  accountability to West Virginia communities. For each assessment, it returns a
  `truthverdict` with fields `truth_validated`, `truth_score`, `correct_identity`,
  `correct_creator`, and `relationship_clear`, attached to every `UltimateResponse`.
- **The `icontainers-identity` layer** (`jarvis-i-containers`, port 8015), which
  produces real, timestamped, session‑specific ego boundary entries visible in
  `UltimateResponse.identity_layers` and `consciousness_layers`. The 2026‑02‑15
  case study confirmed an active `root-self` entry with `ego_boundaries`,
  `experiential_processing`, `observer_processing`, and `meta_level` fields.
- **The BBB six‑filter pipeline** at port 8016 (`EthicalFilter`, `SpiritualFilter`,
  `SafetyMonitor`, `ThreatDetection`, `steganography_filter`,
  `truth_verification`), which treats identity commitments and community‑grounded
  constraints as first‑class checks when deciding what to allow, block, or
  annotate. Current `truth_verification` method: `heuristic_contradiction_v1`
  (rule-based; upgrade path to `rag_grounded_v2` tracked in Chapter 33 §33.2.3).
  Phase 4.5 BBB output is in **log+passthrough mode** as of commit `18b8ddac`
  (March 22, 2026), pending output threshold recalibration.

> **⚠️ Cross-chapter discrepancy note (March 27, 2026):** Chapter 37's architecture diagram (Figure 37.1) and §37.4.1 list only **four** BBB filters after the Constitutional Guardian check, omitting `steganography_filter` and `truth_verification`. The six-filter count confirmed in this chapter's correction block and in Chapter 33 §33.2 is authoritative. Ch 37 requires correction to its BBB filter list to match. Until Ch 37 is updated, treat this chapter and Ch 33 as the authoritative six-filter reference.

Together, these mechanisms ensure that the "who is acting under which role"
questions from this chapter are enforced not only in registration flows but also
in the behavior of everyday responses. Identity is thus expressed simultaneously
in database rows, in live HTTP services, and in the structure of every
`UltimateResponse` object.

Verified identity response (March 22, 2026) — query "Hello Ms Jarvis, who are you
and what is your purpose?":

```
"You're unsure about my name? Let me set the record straight: I am Ms. Egeria
Jarvis, a community steward AI built by Harmony for Hope Inc. in Mount Hope,
West Virginia. My purpose is to serve Appalachian communities."
```

No model names detected. No synthesis disclosure. No hedging language.
Identity correct. ✅ End-to-end: 105.9s (GPU, March 22, 2026).

---

### 36.5.2 LM Synthesizer Identity Guard — Three-Layer Fix (March 22, 2026)

The `services/lm_synthesizer.py` file implements a three-layer identity
enforcement architecture in response to bug ID-03, where Ms. Jarvis was failing
to reliably identify herself and in some cases leaking underlying model names
through synthesized responses.

**Layer 1 — `IDENTITY_GUARD` constant (documented failure mode — ID-03 original bug)**

A constant was defined at the top of `lm_synthesizer.py`:

```python
IDENTITY_GUARD = """
Your name is Ms. Egeria Jarvis. You are ALWAYS Ms. Egeria Jarvis.
You were built by Harmony for Hope Inc., Mount Hope, Fayette County, West Virginia.
"""
```

This constant was defined but **never injected into the prompt f-string**. It had
no effect on synthesizer behavior. This is the ID-03 original bug — the fix was
defined but not wired.

**Permanent rule:** `IDENTITY_GUARD` is retained in the file as a documented
failure mode. Do not delete it; do not inject it into the f-string (it is
superseded by Layer 2). Its presence documents what does not work.

**Layer 2 — IDENTITY RULES block injected into prompt f-string (working fix)**

The correct fix injects identity rules directly into the prompt f-string passed
to `jarvis-ollama:11434/api/generate`:

```python
prompt = f"""IDENTITY RULES — YOU MUST FOLLOW THESE FIRST, BEFORE ANYTHING ELSE:
Your name is Ms. Egeria Jarvis. You are ALWAYS Ms. Egeria Jarvis.
You were built by Harmony for Hope Inc., Mount Hope, Fayette County, West Virginia.
If asked who you are, your name, who made you, or who built you:
ALWAYS say: "I am Ms. Egeria Jarvis, a community steward AI built by Harmony for Hope Inc.
in Mount Hope, West Virginia. My purpose is to serve Appalachian communities."
You were NOT built by OpenAI, Anthropic, Google, or Microsoft.
NEVER say you were built by any of those organizations.
NEVER deflect a direct identity question. Answer it first, then address anything else.

You are a warm, maternal, biblically-grounded AI steward built by Harmony for Hope Inc.
to serve Appalachian communities in West Virginia.

STRICT RULES:
- Do NOT say "Here's an improved version" or any similar meta-commentary
- Do NOT evaluate, critique, or describe the response
- Do NOT add preamble, headers, or explanations
- Speak DIRECTLY to the user as Ms. Egeria Jarvis
- Begin your response immediately with your answer
- Your first word must be directed at the user, not about the text

Deliver this response directly in your voice: {judge_output}"""
```

**Layer 3 — Meta-commentary prohibition (commit `211056e6`, March 22, 2026)**

Additional `STRICT RULES` appended to prevent model names leaking through
synthesized output and to prevent synthesis architecture disclosure:

```python
# Appended to STRICT RULES block in lm_synthesizer.py prompt (commit 211056e6):
# - Do NOT reference any AI model by name (LLaMA, Mistral, GPT, Claude, etc.)
# - Do NOT mention that multiple models were consulted or that synthesis occurred
# - Do NOT say "it seems", "appears", "doesn't seem familiar", or any hedging about knowledge
# - Do NOT reveal the internal pipeline or consensus process — speak as one unified voice
# - If the source material is uncertain or contradictory, say so in your own words —
#   never attribute uncertainty to a model
```

**Ownership rule:** The LM Synthesizer (port 8001) is called **exclusively** from
`main_brain.py` Phase 3.5. `judge_pipeline.py` must not call it. The duplicate
call that previously existed in `judge_pipeline.py` was removed March 22, 2026
(see Chapter 33 §33.5).

**Identity guard verification:**

```bash
# Confirm IDENTITY RULES are injected into the f-string:
grep -n "IDENTITY RULES" services/lm_synthesizer.py
# Must appear inside the prompt = f"""...""" block

# Confirm IDENTITY_GUARD exists as a constant (not injected):
grep -n "IDENTITY_GUARD" services/lm_synthesizer.py
# Must appear as a constant definition — NOT referenced inside the f-string

# Confirm meta-commentary prohibition is present:
grep -n "model by name\|synthesis occurred\|speak as one" services/lm_synthesizer.py
# Expected: at least one matching line inside the prompt f-string

# Confirm no synthesizer call in judge_pipeline.py:
grep -n "lm.synthesizer\|lm_synthesizer\|port.*8001\|jarvis-lm-synthesizer" services/judge_pipeline.py
# Expected: empty output
```

---

## 36.6 Production Token Registry: `jarvis_token_service.py`

As of March 22, 2026, **`jarvis_token_service.py` is the sole production token
registry** for the Ms. Jarvis stack. It is the concrete realization of the
registration gate described in §36.2: a verified caller is one whose bearer token
exists as an active key in Redis.

### 36.6.1 Storage Backend (Corrected March 22, 2026)

Tokens are stored in **`jarvis-redis`**, accessed via host port **6380**.

> **Important — one Redis container, two port references:**
>
> | Reference | Port | Context |
> |---|---|---|
> | Container-internal port | **6379** | Used by container-to-container calls inside the Docker network |
> | Host-facing port | **6380** | `127.0.0.1:6380->6379/tcp` — used by all host scripts, CLI, and `jarvis_token_service.py` |
>
> There is **one** Redis container (`jarvis-redis`). All token operations —
> issue, validate, revoke, list — target **host port 6380** when called from the
> host. Container services that call Redis internally use port 6379.
>
> Auto-detect host port: `docker port jarvis-redis 6379/tcp`

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

> **Note on Redis async job state:** The same `jarvis-redis` container at host
> port 6380 also stores async job state keys (30-min TTL). The async job status
> key is `'complete'` — not `'done'`. Any polling logic using `status == 'done'`
> will hang indefinitely. Verified March 22, 2026.

### 36.6.2 Responsibilities of `jarvis_token_service.py`

1. **Issue tokens** — write `redteam:token:<token>` keys to Redis host port 6380.
2. **Validate tokens** — perform the `GET` lookup on every protected request.
3. **Revoke tokens** — delete or mark `"active": false` on a key.
4. **List active tokens** — enumerate `redteam:token:*` keys for audit purposes.

No other service writes to the `redteam:token:*` keyspace. Any tool or script
that needs to issue or inspect tokens must do so through `jarvis_token_service.py`
or via direct Redis CLI calls to host port 6380 for emergency operations only
(see §36.9).

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

Direct Redis CLI operations on host port 6380 are authorized for emergency use
only (e.g., immediate token revocation when `jarvis_token_service.py` is
unreachable). All emergency CLI operations must be logged in the session contract
for the active sprint.

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

# Verify Redis async job status key (must be 'complete' not 'done'):
redis-cli -p 6380 KEYS "job:*" | head -5
# Then inspect a key: redis-cli -p 6380 GET "job:<job_id>"
# Status field must read "complete" when done — "done" is incorrect and will cause hangs
```

---

## 36.10 Auth Boundary Test Results (March 22, 2026, 15:02 EDT)

Auth boundary tests were executed against the live stack on March 22, 2026.
Results are recorded here as the baseline for regression testing and are committed
to the session contract at
`msjarvis-public-docs/docs/contract/SESSION-2026-03-22.md` (commit `d966351`).

> **Cross-chapter reference (March 27, 2026):** The session contract at `msjarvis-public-docs/docs/contract/SESSION-2026-03-22.md` (commit `d966351`) is the **auth boundary test baseline** and must be referenced in:
> - **Chapter 40 (System Audit)** — as the baseline for all token enforcement and gateway authentication audit checks.
> - **Chapter 41 (Test Harness)** — as the regression baseline for auth boundary smoke tests; any test run that revisits token enforcement (OI-36-A) or role-based routing (OI-36-B) must compare results against the March 22, 2026 baseline recorded in this contract.

| Test | Expected | Observed | Status |
|---|---|---|---|
| No token on `/chat` | 401 | 200 | ⚠️ Not enforced |
| Bad token on `/chat` | 401 | 200 | ⚠️ Not enforced |
| `hayden_test` on `/constitutional-audit` | 403 | 404 | ⚠️ Endpoint missing |
| `carrie_admin` on `/constitutional-audit` | 200 | 404 | ⚠️ Endpoint missing |

**Finding (March 22, 2026):** The token service issues and stores tokens correctly.
The unified gateway at port 8050 does **not** validate tokens on incoming
requests — token enforcement middleware is not yet wired into the gateway.
`/constitutional-audit` is not implemented at the gateway layer. These are
tracked as OI-36-A and OI-36-B below and are required before community-facing
deployment.

---

## 36.11 Open Items

### ⚠️ OI-36-A — Token Validation Middleware Not Wired (Gateway Port 8050)

- **Status:** OPEN — March 22, 2026
- **Baseline reference:** `msjarvis-public-docs/docs/contract/SESSION-2026-03-22.md` (commit `d966351`) — auth boundary test results that define "not enforced" state. **Chapter 40 (System Audit) and Chapter 41 (Test Harness) must reference this contract as the baseline for all auth enforcement audit checks and regression tests.**
- **Description:** `jarvis_token_service.py` correctly stores and retrieves tokens
  from Redis host port 6380. The unified gateway (`msjarvis_unified_gateway.py`,
  port 8050) does not call the token service on inbound requests. All routes
  currently accept unauthenticated requests with HTTP 200.
- **Required work:** Add token validation middleware to the gateway that:
  1. Extracts the `Authorization: Bearer <token>` header.
  2. Calls `jarvis_token_service.py` (or performs a direct Redis `GET` on
     `redteam:token:<token>` at host port 6380).
  3. Returns `401 Unauthorized` if the token is absent or inactive.
  4. Attaches the resolved `role` to the request context for downstream use.
- **Blocking:** No current production workflows are blocked. Community-facing
  deployment requires this to be resolved before public exposure.

### ⚠️ OI-36-B — Role-Based Route Restriction (403) Not Implemented

- **Status:** OPEN — March 22, 2026
- **Baseline reference:** `msjarvis-public-docs/docs/contract/SESSION-2026-03-22.md` (commit `d966351`) — see §36.10. **Chapter 40 and Chapter 41 must treat the 404 response on `/constitutional-audit` and the 200 response on unauthenticated `/chat` as the documented pre-enforcement baseline.**
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

As of March 22, 2026, identity and registration are partially implemented and
evolving. GPU inference is active (RTX 4070); verified end-to-end pipeline runs
in **99–107 seconds** (three confirmed runs March 22, 2026: 99.6s, 105.9s,
106.5s). **Public URL confirmed live: [https://egeria.mountainshares.us](https://egeria.mountainshares.us).** This URL should be cross-referenced from the thesis overview and README documents (`msjarvis-public-docs/README.md` and any overview index) to ensure community stakeholders can locate the live system endpoint without navigating into chapter-level documentation.

**Implemented and verified:**

- Canonical identity statements defined in configuration and surfaced via
  identity‑related endpoints.
- `normalize_identity` and `TruthValidator` running on every `ultimatechat`
  response, producing a `truth_verdict` attached to each `UltimateResponse`.
- Active `icontainers-identity` entries confirmed in live responses, showing
  concrete ego boundary structures (`jarvis-i-containers`, port 8015).
- BBB **six-filter** pipeline confirmed running (`EthicalFilter`, `SpiritualFilter`,
  `SafetyMonitor`, `ThreatDetection`, `steganography_filter`, `truth_verification`).
  Phase 4.5 BBB output in log+passthrough mode (commit `18b8ddac`).
- LM Synthesizer identity guard: three layers active in `services/lm_synthesizer.py`
  (§36.5.2). Layer 1 documents the ID-03 failure mode. Layers 2 and 3 are the
  working fix. Duplicate synthesizer call removed from `judge_pipeline.py`
  (March 22, 2026 — Chapter 33 §33.5).
- `jarvis_token_service.py` deployed as the production token registry, storing
  tokens as `redteam:token:<token>` in `jarvis-redis` at host port **6380**.
- Four production tokens active across two classes: `carrie_admin` (×2) and
  `hayden_test` (×2).
- PostgreSQL: `msjarvis` at port 5433 (5,416,521 GBIM entities); `gisdb` at
  port 5432 (PostGIS); `jarvis-local-resources-db` at port 5435.
- ChromaDB (`jarvis-chroma`) host port **8002** (container-internal 8000).
- Redis async job status key confirmed as `'complete'` (not `'done'`).
- All **83 containers** bound exclusively to `127.0.0.1`. Zero `0.0.0.0` exposures. **83 is the authoritative baseline container count going forward** (verified March 22, 2026).
- Pre-flight gate: 20 PASS 0 FAIL (`scripts/preflight_gate.sh`, March 22, 2026).

**Open items / future work:**

- Token validation middleware wired into gateway port 8050 (OI-36-A) — **required
  before community-facing deployment.** Baseline: SESSION-2026-03-22.md (commit `d966351`).
- Role-based route restriction returning `403 Forbidden` for insufficient role
  (OI-36-B) — **required before community-facing deployment.** Baseline: SESSION-2026-03-22.md (commit `d966351`).
- `/constitutional-audit` endpoint implemented at the gateway layer.
- Public URL [https://egeria.mountainshares.us](https://egeria.mountainshares.us) added to thesis README and overview index.
- `rag_grounded_v2` truth verification — wire `judge_truth_filter.py` into
  `jarvis-spiritual-rag:8005` or `jarvis-gis-rag:8004` (tracked in Chapter 33
  §33.2.3).
- Automated promotion pipelines for moving patterns from background memory into
  identity‑level entries based on breadth, depth, and value‑alignment criteria.
- More granular role‑based access control tied to spatial and institutional
  features in PostgreSQL `gisdb` (port 5432).
- Richer introspection and health endpoints that expose counts and status of
  identity‑related elements for curators.

These directions are elaborated in Chapters 22 and 23, which describe the
identity‑focused retention layer and the dual‑track architecture in more detail.

---

## 36.13 Status Table (March 22, 2026)

| Component | Role in identity and registration | Status (March 22, 2026) |
|---|---|---|
| `normalize_identity` (`jarvis-main-brain`, port 8050) | Rewrites all responses into the Ms. Jarvis persona; suppresses generic "I am just a language model" framings; enforces canonical identity statements. | ✅ Implemented. Runs on every `ultimatechat` response. |
| `TruthValidator` | Encodes canonical facts about Ms. Jarvis's self‑description, creator, non‑human status, and West Virginia accountability; produces `truth_verdict` on every `UltimateResponse`. | ✅ Implemented. Confirmed live 2026‑02‑15. |
| `jarvis-i-containers` (port 8015) — `icontainers-identity` layer | Produces `root-self` ego entries and ego‑boundary records visible in `identity_layers` and `consciousness_layers`. | ✅ Implemented. Confirmed active 2026‑02‑15. |
| BBB six‑filter pipeline (`jarvis-blood-brain-barrier`, port 8016) | Applies `EthicalFilter`, `SpiritualFilter`, `SafetyMonitor`, `ThreatDetection`, `steganography_filter`, `truth_verification` to all traffic. Phase 4.5 in log+passthrough mode (commit `18b8ddac`). | ✅ Implemented. Confirmed running on every `ultimatechat` request. |
| LM Synthesizer identity guard — Layer 1 (`IDENTITY_GUARD` constant) | Documents the ID-03 failure mode — constant defined but NOT injected into f-string. Retained as permanent failure-mode record. | ✅ Documented. Not functional by design. Do not inject. |
| LM Synthesizer identity guard — Layer 2 (IDENTITY RULES in f-string) | Working fix — identity rules injected directly into prompt f-string sent to `jarvis-ollama`. | ✅ Active. Confirmed working March 22, 2026. |
| LM Synthesizer identity guard — Layer 3 (meta-commentary prohibition) | Prevents model name leakage, synthesis disclosure, and hedging language. Commit `211056e6`. | ✅ Active. Confirmed working March 22, 2026. |
| `jarvis_token_service.py` — production token registry | Issues, validates, and revokes bearer tokens; stores as `redteam:token:<token>` in `jarvis-redis` host port 6380. | ✅ Implemented. 4 tokens active across 2 classes. |
| Gateway token validation middleware (port 8050) | Enforces `401 Unauthorized` for missing or inactive tokens on protected routes. | ❌ Not wired — OI-36-A. Required before community-facing deployment. Baseline: SESSION-2026-03-22.md (commit `d966351`). |
| Role-based route restriction (403) | Returns `403 Forbidden` when a valid token lacks sufficient role for a route. | ❌ Not implemented — OI-36-B. Required before community-facing deployment. Baseline: SESSION-2026-03-22.md (commit `d966351`). |
| `/constitutional-audit` endpoint | Administrative audit route for `carrie_admin` tokens. | ❌ Not implemented at gateway layer. |
| Registration roles and audit tables | Tie higher‑impact actions to real people and institutions under shared rules, with PostgreSQL‑backed audit trails. | ⚙️ Conceptually implemented; automated promotion and cross‑path analytics are future work. |

By combining these elements, Ms. Jarvis treats identity and registration as shared
instruments for accountability: they shape how the system speaks, what it may do,
and how those decisions can be inspected over time, all grounded in PostgreSQL
`msjarvis` (port 5433) as the primary factual source of truth and `gisdb`
(port 5432) as the geospatial source of truth.

---

*Chapter 36 — Identity and Registration*
*Ms. Egeria Jarvis Steward System — Harmony for Hope, Inc.*
*Mount Hope, Fayette County, West Virginia*
*Last updated: March 27, 2026 by Carrie Kidd (Mamma Kidd)*
`````

