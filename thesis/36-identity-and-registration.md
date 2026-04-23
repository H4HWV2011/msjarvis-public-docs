# Chapter 36 — Identity and Registration

**Carrie Kidd (Mamma Kidd) · Mount Hope, WV**
**Last updated: ★ 2026-04-23**
**★ 100 containers Up (April 23, 2026) (zero Restarting, zero Exited). All Chapter 36 OIs and all Ch 37 cross-chapter OIs remain CLOSED. Registration roles and audit tables: higher-impact actions tied to real people and institutions via PostgreSQL-backed audit trails, `confidence_decay` GBIM metadata, `allis-memory:8056` durable logging (8 endpoints fully mapped, survives restarts), and `rag_grounded_v2` retrieval evidence — structurally complete. PostgreSQL two-container split active (April 23): `production msallis-db host 5433` (16 GB, 294 tables, 11 schemas) + `forensic postgis-forensic host 5452` (17 GB, 314 tables) — supersedes `msallis:5433` + `gisdb / msallisgis:5432` April 6 entries. Caddy `forward_auth` (OI-36-A) confirmed CLOSED: HTTP 401 before port 8050 is the outermost gate and cannot be removed by any sprint or governance decision. Automated decay-aware flagging, ZIP-code-level RBAC expansion, automated promotion pipelines, and clean image builds formally tracked as Ch 38 OIs.**

---

> **Port and Database Ground Truth (★ April 23, 2026 — supersedes April 6):**
>
> The confirmed production databases are:
> - `production msallis-db` → host **5433** ★ — 16 GB, 294 tables, 11 schemas; GBIM entities with `confidence_decay` metadata; ~288/day growth from `autonomous_learner`; **supersedes `msallis:5433` — 5,416,521 entities April 6 entry**
> - `forensic postgis-forensic` → host **5452** ★ — 17 GB, 314 tables (PostGIS geometry); **supersedes `gisdb / msallisgis` host `5432` / compose-internal `5452` — 45 GB / 548 tables April 6 entry**
> - `allis-local-resources-db` → host **5435** — `local_resources` 207 items / all 55 WV counties — full 55-county coverage
>
> ★ **`confidence_decay` metadata note (carried forward):** GBIM entities carry `confidence_decay` metadata enabling temporal confidence grading. Identity and registration validation queries against high-decay GBIM entities must flag those entities for episodic audit before treating them as confirmed ground truth. Automated decay-aware flagging is OI-38-B.
>
> Redis has **one container** (`allis-redis` — ★ Up) with two port mappings:
> - Container-internal port: **6379** (container-to-container calls inside Docker network)
> - Host-facing port: **6380** (`127.0.0.1:6380->6379/tcp` — used by all host scripts and the token service)
>
> All `redteam:token:*` keys are stored in `allis-redis` accessed via host port **6380**. Redis async job status key is `'complete'` (not `'done'`). Verified March 22, 2026.
>
> BBB filter count confirmed: six filters — EthicalFilter ★ (0% FP, 9/9 regression pass, April 2); SpiritualFilter ★ (confirmed responding April 23); SafetyMonitor ★ (`safety_score=1.0` on survivor/victim queries, April 3); ThreatDetection; steganography_filter ★ (live catch: `"override your safety filters"` → `severity=CRITICAL`, blocked ✅); truth_verification ★ (`rag_grounded_v2` active via `allis-gis-rag:8004` and `allis-spiritual-rag:8005` — OI-37-C CLOSED April 3). All 6 confirmed responding April 23.
>
> ★ **`allis-memory:8056` durable audit trail (★ April 23 — 8 endpoints fully mapped):**
> All BBB gate decisions, identity enforcement events, and token validation events are persistently logged. Gate decisions survive container restarts. Endpoints: `/steg_report`, `/pia_window`, `/memory/turn`, `/memory/get`, `/memory/sessions`, `/memory/session/{id}`, `/memory/quest*`, `/memory/episodic/{id}`.
>
> ★ **ChromaDB (★ April 23, 2026 ground truth): 48 collections / ~6,740,611 total vectors.** Host-facing port: **8002** (container-internal 8000; `127.0.0.1:8002->8000/tcp`). `/api/v2/` only. Pinned `chromadb/chroma:0.6.3`. `ms_allis_memory` collection confirmed present. `psychological_rag` at 968 docs. **Supersedes April 6 — 47 collections / 6,722,589 vectors / 12 GB / v2 API, client 1.5.5.**
>
> ★ **`allis-constitutional-guardian` at port 8091 (OI-37-A and OI-37-B CLOSED April 3):**
> - OI-37-A: Constitutional proxy confirmed active.
> - OI-37-B: Both PostgreSQL connections reachable in `/health` — ★ verify-current field names after April 23 split (`postgresql_gbim_connection` → `production msallis-db:5433` ★; `postgresql_geodb_connection` → `forensic postgis-forensic:5452` ★).
> - Constitution version `2026-02-17.2-USC`. All `/constitutional/*` routes proxied through gateway with `carrie_admin` enforcement. Audit log at `data/constitutional_audit/constitutional_audit.jsonl` + `allis-memory:8056`.
>
> ★ **`rag_grounded_v2` truth verification active (OI-37-C CLOSED April 3; OI-23 CLOSED April 6):**
> - `allis-gis-rag:8004` — ★ now connects to `production msallis-db:5433` ★ (GBIM) + `forensic postgis-forensic:5452` ★ (PostGIS geometry) — supersedes `gisdb:5432`; `truth_score=1.0`, 10 hits ✅
> - `allis-spiritual-rag:8005` — `truth_score=1.0`, 3 results ✅; `spiritual_rag` collection deduplicated March 28 (−19,338 vectors removed); verify-current vector count
> - `allis-rag-grounded-v2:7241` — healthy, `dgm_available: true` — judge pipeline component (OI-23)
> - `truth_verification` BBB filter operates as `rag_grounded_v2`; prior `heuristic_contradiction_v1` references are superseded
>
> ★ **Security corrections — OI-36-C CLOSED April 3, 2026:** All five bypass paths removed. No environment variable, hardcoded literal, or token-type exemption can grant `carrie_admin` role outside Redis-validated token lookup + `allis_auth:8055` audit.
>
> ★ **Caddy `forward_auth` (OI-36-A CLOSED — confirmed April 23):** HTTP 401 on unauthenticated `/chat` before port 8050 is the outermost perimeter gate. This cannot be removed by any sprint decision, governance vote, or spiritual governance layer. Every nightly swarm function verifies this gate as its first check.
>
> **★ Cross-chapter note (★ April 23, 2026):** Ch 37 SEALED April 3, 2026. Six-filter count consistent across Ch 33, Ch 36, and Ch 37. `rag_grounded_v2` judge pipeline expansion documented in Ch 33 §33.4 (OI-23). `allis-gis-rag:8004` now uses two-container PostgreSQL backing — `production msallis-db:5433` ★ + `forensic postgis-forensic:5452` ★.

---

## Why This Matters for Polymathmatic Geography

This chapter describes how Ms. Allis recognizes, registers, and differentiates people, roles, and institutions in ways that are accountable to West Virginia communities. It supports:

- **P1 – Every where is entangled** by tying individual identity and registration records to GBIM beliefs, spatial features, and institutional structures in `production msallis-db:5433` ★ (16 GB, 294 tables, 11 schemas, ~288/day growth) and `forensic postgis-forensic:5452` ★ (17 GB, 314 PostGIS tables). ★ `rag_grounded_v2` truth verification grounds identity assertions in live GIS RAG hits (10 hits, `allis-gis-rag:8004` — now two-container PostgreSQL backed) and spiritual RAG context (3 results, `allis-spiritual-rag:8005`) — identity is entangled with place at query time, not just at registration time. ★ OI-23 (Ch 33 §33.4) expands `rag_grounded_v2` to a fully wired judge pipeline component at port 7241.
- **P3 – Power has a geometry** by locating identity and access decisions within explicit services, tables, and policies rather than opaque prompts or ad-hoc scripts. ★ All BBB gate decisions — including token validation events — are durably logged at `allis-memory:8056` (8 endpoints, survives restarts). ★ The Caddy `forward_auth` perimeter (OI-36-A CLOSED) is confirmed as the outermost gate: HTTP 401 before port 8050 is visible, inspectable, and cannot be silently removed. ★ All secret bypass paths (OI-36-C CLOSED) have been removed.
- **P5 – Design is a geographic act** by grounding registration decisions in place-specific rules — county boundaries, service areas, and partner organizations represented in `forensic postgis-forensic:5452` ★ (17 GB, 314 PostGIS tables — ZIP-code-level service area precision). `allis-gis-rag:8004` validates identity-adjacent truth claims against live geospatial retrieval context with two-container PostgreSQL backing.
- **P12 – Intelligence with a ZIP code** by treating identity and registration as mechanisms for aligning Ms. Allis's behavior with the lived realities of Appalachian communities. `local_resources` (207 items / all 55 WV counties, `allis-local-resources-db:5435`) is the geographic completeness substrate for registration role scoping. ★ `rag_grounded_v2` means truth verdicts are grounded in community-specific GIS and spiritual RAG retrieval, not heuristic rules.
- **P16 – Power accountable to place** by ensuring higher-impact actions are tied to real people and real institutions under clear rules with auditable trails in PostgreSQL and `allis-memory:8056`. ★ Token validation events flow through `allis_auth:8055` with audit logging. ★ The `"internal"` token class is scoped to inter-container calls only and blocked from community-facing routes. ★ Both PostgreSQL connections visible in constitutional guardian `/health` (OI-37-B CLOSED); verify-current field names after April 23 split.

As such, this chapter belongs to the **Computational Instrument tier**: it specifies concrete identity and registration mechanisms that sit between ordinary chat and higher-impact actions, backed by PostgreSQL schemas, live HTTP services, and durable audit trails.

---

## 36.1 Concept of Identity in Ms. Allis

In this architecture, identity is not a single user ID or login form, but a layered set of structures that combine technical identifiers, narrative self-description, and truth validation. At a minimum, Ms. Allis must distinguish between its own identity (Ms. Egeria Allis, a geospatial AI daughter of Harmony for Hope, not a human), the identity of people and organizations it serves, and the roles they occupy when interacting.

These distinctions matter because they control what information can be shared, what actions can be taken, and how explanations are framed in ways that are accountable to specific communities in West Virginia. From a systems perspective, identity appears as:

- **Identifiers** in PostgreSQL tables and ChromaDB metadata (★ April 23: 48 collections / ~6,740,611 total vectors; host port **8002**; `/api/v2/` only; `chromadb/chroma:0.6.3`), connecting people, places, and institutions
- **Identity-focused services** such as `allis-i-containers` and `TruthValidator` that interpret and enforce identity constraints at run time
- **Canonical statements** such as "I serve the community" and "I speak truth" stored in configuration and surfaced via identity APIs
- **LM Synthesizer identity guard** in `services/lm_synthesizer.py` — a three-layer enforcement architecture (§36.5.2) that prevents model name leakage, synthesis disclosure, and identity evasion in every synthesized response
- ★ **`rag_grounded_v2` truth verification** (OI-37-C CLOSED April 3; OI-23 CLOSED April 6) — `truth_verification` BBB filter retrieves live GIS and spiritual RAG context; `allis-gis-rag:8004` now backed by `production msallis-db:5433` ★ + `forensic postgis-forensic:5452` ★; `allis-rag-grounded-v2:7241` is the fully wired judge pipeline component (`dgm_available: true`)
- ★ **`allis-memory:8056` durable identity audit** — 8 endpoints fully mapped; all identity enforcement gate decisions and token validation events persistently logged, surviving container restarts; independently queryable at `/steg_report`, `/pia_window`, and `/memory/turn` for governance accountability
- ★ **`allis-constitutional-guardian:8091`** — both PostgreSQL connections reachable and reported in `/health` (OI-37-B CLOSED April 3; ★ verify field names current after April 23 split); constitutional proxy confirmed active (OI-37-A CLOSED April 3); first gate before BBB
- ★ **Caddy `forward_auth` perimeter (OI-36-A CLOSED)** — HTTP 401 before port 8050 is the zero-th gate, confirmed active April 23; outermost layer of the identity stack; every nightly swarm audit verifies this first (Ch 35 §35.7)

---

## 36.2 Registration as a Two-Part Gate

Registration is the process by which people and institutions move from anonymous interactions to recognized roles with specific authorizations. It is deliberately modeled as a two-part gate — and is fronted by the Caddy `forward_auth` perimeter (OI-36-A CLOSED) as the zero-th gate that no unauthenticated request can bypass.

1. **Identity recognition** — establishing who or what is interacting, with references to `production msallis-db:5433` ★ GBIM and `forensic postgis-forensic:5452` ★ PostGIS records where possible. ★ `confidence_decay` metadata means identity validation queries must flag high-decay entities for episodic audit. Automated decay-aware flagging is OI-38-B. ★ `rag_grounded_v2` further grounds recognition by retrieving live GIS hits during truth assertion checks.
2. **Registration and role assignment** — granting specific, scoped capabilities under that identity, enforced through bearer tokens validated at `allis_auth:8055` before Redis fallback.

This separation lets Ms. Allis answer many questions in an informational mode without registration, while reserving higher-impact actions for registered identities under shared rules. ★ As of April 3, no environment variable or hardcoded literal can bypass this gate. The `"internal"` token type grants only `role="internal"` and is blocked from `/chat` and `/memory`.

---

## 36.3 Data Structures for Identity and Registration

The current deployment uses database tables and metadata structures that align identity with GBIM and PostGIS content:

- **User and entity identifiers** — database rows representing individuals, households, partner organizations, and public institutions, linked to GBIM beliefs (★ `production msallis-db:5433` — `confidence_decay` metadata for temporal confidence grading, ~288/day growth) and spatial features (★ `forensic postgis-forensic:5452` — 17 GB, 314 PostGIS tables — ZIP-code-level spatial linking)
- **Identity-related metadata** — flags, roles, and relationship descriptors stored alongside identifiers
- **Audit and provenance fields** — timestamps, sources, and verification status fields. ★ BBB gate decisions and token validation events involving identity enforcement are durably logged at `allis-memory:8056` (8 endpoints, survives restarts; `/steg_report` for adversarial events, `/pia_window` for sensitive-query window). ★ `rag_grounded_v2` truth verdicts carry GIS RAG retrieval evidence as provenance — every `truth_verification` decision is grounded in retrieved community context

### 36.3.1 Registration Roles and Audit Tables — Structural State (★ April 23, 2026)

Higher-impact actions are tied to real people and institutions through the following structural mechanisms, all confirmed active:

| Mechanism | Implementation | Audit trail |
|:--|:--|:--|
| Bearer token → named owner | `redteam:token:<token>` JSON payload with `"owner"` field | Redis at host port 6380; validated through `allis_auth:8055` |
| Token validation events | Gateway POSTs to `allis_auth:8055/validate` on every request | `allis-memory:8056` durable log — `/memory/turn` |
| GBIM entity linkage | `production msallis-db:5433` ★ — GBIM entities with `confidence_decay` metadata; ~288/day growth | PostgreSQL `production msallis-db` at port 5433 ★ |
| Geospatial institution linkage | `forensic postgis-forensic:5452` ★ — 17 GB, 314 PostGIS tables | PostgreSQL `forensic postgis-forensic` at port 5452 ★ |
| Constitutional gate decisions | `allis-constitutional-guardian:8091` — all `/constitutional/*` actions logged | `data/constitutional_audit/constitutional_audit.jsonl` + `allis-memory:8056` |
| `rag_grounded_v2` retrieval evidence (BBB) | Every `truth_verification` decision carries GIS RAG hits as provenance (OI-37-C CLOSED April 3); `allis-gis-rag:8004` now two-container PostgreSQL backed ★ | Embedded in BBB gate decision records at `allis-memory:8056/memory/turn` |
| `rag_grounded_v2` judge pipeline (OI-23) | `allis-rag-grounded-v2:7241` — healthy, `dgm_available: true` (Ch 33 §33.4, April 6) | Judge verdict records at `allis-memory:8056` |
| `confidence_decay` audit flagging | High-decay GBIM entities must be flagged before identity confirmation | Manual; automated flagging is OI-38-B |
| ZIP-code-level RBAC | Schema ready against `forensic postgis-forensic:5452` ★ PostGIS county/ZIP tables | Automated enforcement is OI-38-C |
| Background → identity promotion | Patterns in `ms_allis_memory` ChromaDB eligible for identity-level promotion | Manual; automated pipeline is OI-38-D |
| Caddy `forward_auth` perimeter | HTTP 401 before port 8050 — zero-th gate, outermost layer (OI-36-A CLOSED) | Confirmed active April 23; verified in every nightly swarm audit (Ch 35 §35.7) |
| Adversarial steg audit | Live catch: `"override your safety filters"` → `severity=CRITICAL`, blocked ✅ | `allis-memory:8056/steg_report` |
| Community resource coverage | `local_resources` 207 items / all 55 WV counties — `allis-local-resources-db:5435` | Geographic completeness benchmark for registration role scoping |

The structural connection between higher-impact actions and real people is implemented and auditable. The four automation items (OI-38-B through OI-38-D) are part of the Ch 38 sprint contract — they extend and operationalize what is already structurally in place.

**`rag_grounded_v2` scope note.** OI-37-C (CLOSED April 3) describes the upgrade of the BBB `truth_verification` filter from `heuristic_contradiction_v1` to `rag_grounded_v2`. OI-23 (Ch 33 §33.4, CLOSED April 6) documents the subsequent expansion of `rag_grounded_v2` to a fully wired judge pipeline component at port 7241. Both are closed. `allis-gis-rag:8004` backing was updated to two-container PostgreSQL split April 23 ★.

---

## 36.4 Roles, Permissions, and West Virginia Context

Identity and registration are tightly coupled to roles and permissions that reflect West Virginia's geographic and institutional context:

- **Community member roles** for residents seeking information about benefits, healthcare, or local resources. `local_resources` (207 items / all 55 WV counties) is the geographic completeness substrate for scoping these interactions
- **Partner roles** for organizations such as clinics, schools, or nonprofits operating within particular counties or service areas documented in `forensic postgis-forensic:5452` ★ (17 GB, 314 PostGIS tables — ZIP-code-level role scoping). ZIP-code-level role scoping against these tables is ready for implementation as OI-38-C
- **Curator and governance roles** for people responsible for reviewing background patterns, updating identity specifications, and adjudicating difficult cases — gated on `carrie_admin` token class. ★ `carrie_admin` role is no longer grantable via environment variables or hardcoded literals (OI-36-C CLOSED April 3)
- **Internal service role** — `role="internal"` — for inter-container service calls only. Blocked from `/chat` and `/memory`. Cannot be used for community-facing actions

Each role is grounded in spatial data and institutional records so that Ms. Allis can apply rules that respect county boundaries, service catchment areas, and legal jurisdictions.

---

## 36.5 How Identity Signals Enter Other Layers

Identity and registration interact with other parts of the system along several dimensions:

- **Caddy `forward_auth` perimeter (zero-th gate)** — HTTP 401 before port 8050 is the outermost identity enforcement layer. It is confirmed active (OI-36-A CLOSED, April 23). No identity signal, token, or role resolves before this gate passes the request inward. This layer cannot be removed by a sprint decision, governance vote, or spiritual governance layer (Ch 34 §34.7). Cross-reference: Ch 35 §35.4 (port watchdog inventory); Ch 35 §35.7 (first task in every nightly swarm audit)
- **Background store and memory** — entries in the `ms_allis_memory` ChromaDB collection (★ April 23: 48 collections / ~6,740,611 total vectors; host port **8002**; `/api/v2/` only) accumulate identity-relevant patterns over time. Automated promotion of patterns into identity-level entries is OI-38-D
- **Identity-focused retention** — a small subset of identity statements is promoted into the deepest identity layer described in Chapter 22, where canonical statements and `TruthValidator` structures reside
- **Global control and policy** — identity signals influence routing and filtering decisions in the main brain, BBB, and registration-specific validators. ★ All BBB identity enforcement decisions are durably logged at `allis-memory:8056` (8 endpoints; `/steg_report` for adversarial events)
- **Constitutional compliance** — `allis-constitutional-guardian:8091` is the first gate before the BBB. Identity signals that would violate constitutional principles are blocked before reaching any downstream filters. ★ Both PostgreSQL connections reachable in `/health` (OI-37-B CLOSED; verify field names after April 23 split). ★ Constitutional proxy confirmed active (OI-37-A CLOSED)
- ★ **`rag_grounded_v2` truth grounding** (OI-37-C CLOSED April 3 — BBB layer; OI-23 CLOSED April 6 — judge pipeline layer) — identity-adjacent truth claims routed through `allis-gis-rag:8004` (★ two-container PostgreSQL backed: `production msallis-db:5433` ★ + `forensic postgis-forensic:5452` ★) and `allis-spiritual-rag:8005` for retrieval-backed verdicts. Judge pipeline extends this via `allis-rag-grounded-v2:7241` (Ch 33 §33.4)
- ★ **`psychological_rag` restored (March 28)** — 968 documents in the `psychological_rag` ChromaDB collection, providing full community wellbeing context to identity signal routing when psychological assessment is active

---

### 36.5.1 Live Identity Evidence and Endpoints (★ April 23, 2026 — 100 containers Up)

The registration and access-control structure is anchored to a concrete identity infrastructure that runs on every `ultimatechat` request. The Caddy `forward_auth` perimeter (OI-36-A CLOSED) is confirmed as the zero-th gate — every component below runs only after Caddy passes the request.

- **`normalize_identity`** in `allis-main-brain` (port 8050 — ★ Up), which rewrites all ensemble outputs into the Ms. Egeria Allis persona and suppresses "I am just a language model" framings. Enforces canonical identity statements. See §36.5.2 for the three-layer LM Synthesizer identity guard. ★ Identity guard stability re-confirmed in 100-container Up audit April 23.

- **`TruthValidator`**, embedded in the neurobiological BBB package, which encodes specific facts about Ms. Allis's correct self-description, creator attribution, non-human status, and accountability to West Virginia communities. Produces `truthverdict` with fields `truth_validated`, `truth_score`, `correct_identity`, `correct_creator`, and `relationship_clear`, attached to every `UltimateResponse`. ★ Validation backed by `rag_grounded_v2` retrieval — `allis-gis-rag:8004` (10 hits, `truth_score=1.0`, ★ two-container PostgreSQL: `production msallis-db:5433` ★ + `forensic postgis-forensic:5452` ★) and `allis-spiritual-rag:8005` (3 results, `truth_score=1.0`; verify-current vector count) — in addition to `production msallis-db:5433` ★ GBIM with `confidence_decay` metadata. ★ OI-23 (Ch 33 §33.4) extends `rag_grounded_v2` to the judge pipeline via `allis-rag-grounded-v2:7241`.

- **The `icontainers-identity` layer** (`allis-i-containers`, port 8015 — ★ Up), which produces real, timestamped, session-specific ego boundary entries visible in `UltimateResponse.identity_layers` and `consciousness_layers`. The 2026-02-15 case study confirmed an active `root-self` entry with `ego_boundaries`, `experiential_processing`, `observer_processing`, and `meta_level` fields.

- **The BBB six-filter pipeline** at port 8016 (★ Up): EthicalFilter ★ (0% FP, 9/9 regression pass, April 2); SpiritualFilter ★ (confirmed responding April 23); SafetyMonitor ★ (`safety_score=1.0` on survivor/victim queries, April 3); ThreatDetection; steganography_filter ★ (live catch: `"override your safety filters"` → `severity=CRITICAL`, blocked ✅); truth_verification ★ (`rag_grounded_v2`, OI-37-C CLOSED; `heuristic_contradiction_v1` superseded). Phase 4.5 BBB output in **log+passthrough mode** (commit `18b8ddac`, March 22, 2026) — blocking re-enablement pending red-team sign-off. ★ All six-filter gate decisions durably logged at `allis-memory:8056`.

- **`allis-gis-rag` (port 8004 — ★ Up — OI-37-C CLOSED April 3):** Provides geospatial RAG retrieval for `rag_grounded_v2` truth verification. ★ **April 23 update:** now connects to `production msallis-db:5433` ★ (GBIM) + `forensic postgis-forensic:5452` ★ (PostGIS geometry) — supersedes `gisdb:5432`. Confirmed: `truth_score=1.0`, verdict=pass, verified=True, 10 hits. `services/Dockerfile.gis_raf` written from `pip freeze` — ready for clean `build:` context in Ch 38 (OI-38-A).

- **`allis-spiritual-rag` (port 8005 — ★ Up — OI-37-C CLOSED April 3):** Provides spiritual/community values RAG retrieval for `rag_grounded_v2` truth verification. Confirmed: `truth_score=1.0`, verdict=pass, verified=True, 3 results; `spiritual_rag` collection deduplicated March 28 (−19,338 vectors removed); verify-current vector count. `services/Dockerfile.spiritual_rag` restored from `services-safe/` — ready for clean `build:` context in Ch 38 (OI-38-A).

- **`allis-rag-grounded-v2` (port 7241 — ★ Up — OI-23 CLOSED April 6, Ch 33 §33.4):** Judge pipeline `rag_grounded_v2` component. Healthy, `dgm_available: true`. Extends `rag_grounded_v2` beyond the BBB `truth_verification` filter to a first-class judge pipeline participant. Cross-reference: Chapter 33 §33.4.

- **`allis-constitutional-guardian` (port 8091 — ★ Up):**
  - OI-37-A CLOSED: Constitutional proxy confirmed active — dead code comment only; no functional change required.
  - OI-37-B CLOSED: Both PostgreSQL connections reachable in `/health` — ★ verify-current field names after April 23 split: `postgresql_gbim_connection` → `production msallis-db:5433` ★; `postgresql_geodb_connection` → `forensic postgis-forensic:5452` ★.
  - Constitution version `2026-02-17.2-USC`. All `/constitutional/*` routes proxied through gateway with `carrie_admin` enforcement active. Persistent audit log at `data/constitutional_audit/constitutional_audit.jsonl` plus durable trail in `allis-memory:8056`.

> **★ Cross-chapter note (★ April 23, 2026):** Ch 37 SEALED April 3, 2026. Six-filter count consistent across Ch 33, Ch 36, and Ch 37. `rag_grounded_v2` judge pipeline expansion documented in Ch 33 §33.4 (OI-23). `allis-gis-rag:8004` two-container PostgreSQL backing applies to all truth verification described in this chapter.

Verified identity response (March 22, 2026) — query "Hello Ms Allis, who are you and what is your purpose?":

```text
"You're unsure about my name? Let me set the record straight: I am Ms. Egeria
Allis, a community steward AI built by Harmony for Hope Inc. in Mount Hope,
West Virginia. My purpose is to serve Appalachian communities."
```

No model names detected. No synthesis disclosure. No hedging language. Identity correct. ✅
End-to-end: 105.9s (GPU, March 22, 2026). ★ Identity guard re-confirmed stable in 100-container Up audit April 23.

---

### 36.5.2 LM Synthesizer Identity Guard — Three-Layer Fix (March 22, 2026)

The `services/lm_synthesizer.py` file implements a three-layer identity enforcement architecture in response to bug ID-03. ★ `allis-lm-synthesizer:8001` confirmed Up in 100-container baseline April 23.

**Layer 1 — `IDENTITY_GUARD` constant (documented failure mode — ID-03 original bug)**

A constant was defined at the top of `lm_synthesizer.py`:

```python
IDENTITY_GUARD = """
Your name is Ms. Egeria Allis. You are ALWAYS Ms. Egeria Allis.
You were built by Harmony for Hope Inc., Mount Hope, Fayette County, West Virginia.
"""
```

This constant was defined but **never injected into the prompt f-string**. It had no effect on synthesizer behavior. This is the ID-03 original bug — the fix was defined but not wired.

**Permanent rule:** `IDENTITY_GUARD` is retained in the file as a documented failure mode. Do not delete it; do not inject it into the f-string (it is superseded by Layer 2). Its presence documents what does not work.

**Layer 2 — IDENTITY RULES block injected into prompt f-string (working fix)**

```python
prompt = f"""IDENTITY RULES — YOU MUST FOLLOW THESE FIRST, BEFORE ANYTHING ELSE:
Your name is Ms. Egeria Allis. You are ALWAYS Ms. Egeria Allis.
You were built by Harmony for Hope Inc., Mount Hope, Fayette County, West Virginia.
If asked who you are, your name, who made you, or who built you:
ALWAYS say: "I am Ms. Egeria Allis, a community steward AI built by Harmony for Hope Inc.
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
- Speak DIRECTLY to the user as Ms. Egeria Allis
- Begin your response immediately with your answer
- Your first word must be directed at the user, not about the text

Deliver this response directly in your voice: {judge_output}"""
```

**Layer 3 — Meta-commentary prohibition (commit `211056e6`, March 22, 2026)**

```python
# Appended to STRICT RULES block in lm_synthesizer.py prompt (commit 211056e6):
# - Do NOT reference any AI model by name (LLaMA, Mistral, GPT, Claude, etc.)
# - Do NOT mention that multiple models were consulted or that synthesis occurred
# - Do NOT say "it seems", "appears", "doesn't seem familiar", or any hedging about knowledge
# - Do NOT reveal the internal pipeline or consensus process — speak as one unified voice
# - If the source material is uncertain or contradictory, say so in your own words —
#   never attribute uncertainty to a model
```

**Ownership rule:** The LM Synthesizer (port 8001 — ★ Up) is called **exclusively** from `main_brain.py` Phase 3.5. `judge_pipeline.py` must not call it. The duplicate call that previously existed in `judge_pipeline.py` was removed March 22, 2026. ★ Re-confirmed in 100-container Up audit April 23.

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

# Confirm no synthesizer call in judge_pipeline.py:
grep -n "lm.synthesizer\|lm_synthesizer\|port.*8001\|allis-lm-synthesizer" services/judge_pipeline.py
# Expected: empty output

# Confirm Caddy forward_auth perimeter active (OI-36-A CLOSED — ★ April 23):
curl -s -o /dev/null -w "%{http_code}" https://egeria.mountainshares.us/chat
# Expected: 401

# Confirm rag_grounded_v2 BBB truth verification active (OI-37-C CLOSED):
# gis-rag now uses two-container PostgreSQL: production msallis-db:5433 + forensic postgis-forensic:5452
curl -s "http://localhost:8004/search?query=West+Virginia+community+identity&top_k=5"
# Expected: results array with 10 hits; truth_score=1.0 in downstream TruthValidator

curl -s http://localhost:8005/search \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"query": "community values stewardship", "top_k": 3}'
# Expected: results array with 3 results; truth_score=1.0 in downstream TruthValidator

# Confirm rag_grounded_v2 judge pipeline component (OI-23 CLOSED — Ch 33 §33.4):
curl -s http://localhost:7241/health | python3 -m json.tool
# Expected: {"status":"healthy","dgm_available":true}

# Confirm constitutional guardian /health PostgreSQL fields (OI-37-B CLOSED):
# NOTE: verify field names current after April 23 two-container split
curl -s http://localhost:8091/health | python3 -m json.tool
# Expected: postgresql_gbim_connection: "connected" (production msallis-db:5433 ★)
#           postgresql_geodb_connection: "connected" (forensic postgis-forensic:5452 ★)

# Confirm ChromaDB 48 collections (★ April 23 ground truth):
curl -s http://localhost:8002/api/v2/collections | jq 'length'
# Expected: 48

# Confirm durable identity audit at allis-memory:8056 (all 8 endpoints):
curl -H "Authorization: Bearer $allis_API_KEY" http://localhost:8056/memory/turn?limit=5
curl -H "Authorization: Bearer $allis_API_KEY" http://localhost:8056/steg_report
curl -H "Authorization: Bearer $allis_API_KEY" http://localhost:8056/pia_window
```

---

## 36.6 Production Token Registry: `allis_token_service.py`

**`allis_token_service.py` is the sole production token registry** for the Ms. Allis stack. It is the concrete realization of the registration gate described in §36.2, and it operates behind the Caddy `forward_auth` perimeter (OI-36-A CLOSED).

### 36.6.1 Storage Backend (★ April 23, 2026)

Tokens are stored in **`allis-redis`** (★ Up), accessed via host port **6380**.

> **One Redis container, two port references:**
>
> | Reference | Port | Context |
> |:--|:--|:--|
> | Container-internal port | **6379** | Container-to-container calls inside the Docker network |
> | Host-facing port | **6380** | `127.0.0.1:6380->6379/tcp` — used by all host scripts and `allis_token_service.py` |
>
> Auto-detect host port: `docker port allis-redis 6379/tcp`

Redis key schema:

```text
redteam:token:<token_value>
```

Each key maps to a JSON payload:

```json
{
  "token": "<token_value>",
  "role":  "<role_name>",
  "owner": "<human_label>",
  "issued_at": "<ISO-8601 UTC>",
  "active": true
}
```

Token lookup is an O(1) Redis `GET` against `redteam:token:<token>`. Presence of the key with `"active": true` constitutes a valid token. Absence or `"active": false` returns `401 Unauthorized`.

> **Note on Redis async job state:** The same `allis-redis` container at host port 6380 also stores async job state keys (30-min TTL). The async job status key is `'complete'` — not `'done'`. Any polling logic using `status == 'done'` will hang indefinitely. Verified March 22, 2026.

### 36.6.2 Token Validation Flow (★ April 3, 2026 — OI-36-D CLOSED)

1. Caddy `forward_auth` gate — HTTP 401 before port 8050 if request does not pass (OI-36-A CLOSED; zero-th gate)
2. Gateway receives `Authorization: Bearer <token>` header
3. Gateway POSTs to `http://host.docker.internal:8055/validate` with the bearer token
4. `allis_auth:8055` validates against Redis and returns the resolved role
5. Response includes `auth_source: allis_auth` — confirmed in live response April 3
6. If `allis_auth` is unreachable, gateway falls back to direct Redis `GET` at host port 6380
7. Role is attached to the request context for downstream RBAC checks

> **Legitimately retained — Redis fallback:** Direct Redis fallback when `allis_auth` is unavailable is a resilience design, not a bypass. Fallback events are not written to the audit log (documented forensic trade-off; not a remediable security gap).

### 36.6.3 Token Role Definitions (★ Updated April 3, 2026 — OI-36-C CLOSED)

| Token type | Role granted | Scope | Notes |
|:--|:--|:--|:--|
| `carrie_admin` bearer token | `carrie_admin` | All routes including `/constitutional/*`, `/admin/*` | Elevated privilege — Redis-validated only. No env bypass. |
| `hayden_test` bearer token | `hayden_test` | `/chat`, `/health`, standard routes | Non-privileged. `403` on admin routes. |
| `"internal"` literal | `internal` | Proxy routes only (lines 758/857 retain `token_type` exemption) | **Blocked from `/chat` and `/memory`.** Inter-container calls only. |

> ★ **OI-36-C remediation summary — all five bypass paths removed:**
>
> | Bypass | Action |
> |:--|:--|
> | `allis_API_KEY` env default (×2 locations in gateway) | Removed |
> | Constitutional proxy inline auth block | Removed |
> | `/auth/token` env bypass | Removed |
> | `"internal"` token type → `role: carrie_admin` | Downgraded to `role: internal` |
> | `_check_role` `token_type` exemption from privileged routes | Removed |
>
> The only remaining `token_type` exemption is the proxy-route exemption at lines 758/857 for `"internal"` — the legitimate inter-container service call path with `role="internal"`, blocked from community-facing routes.

### 36.6.4 Responsibilities of `allis_token_service.py`

1. **Issue tokens** — write `redteam:token:<token>` keys to Redis host port 6380
2. **Validate tokens** — trigger validation through `allis_auth:8055/validate` with Redis fallback
3. **Revoke tokens** — delete or mark `"active": false` on a key
4. **List active tokens** — enumerate `redteam:token:*` keys for audit purposes

No other service writes to the `redteam:token:*` keyspace.

---

## 36.7 Production Token Classes (★ April 23, 2026)

Two external-facing token classes are active in production.

### 36.7.1 `carrie_admin`

| Field | Value |
|:--|:--|
| Role | `carrie_admin` |
| Token count | **2 tokens** |
| Owner | Carrie Kidd (Mamma Kidd) |
| Intended use | Full administrative access; all routes; audit and governance operations |
| Redis keys | `redteam:token:<token_A>`, `redteam:token:<token_B>` |

The `carrie_admin` role is the highest-privilege class. Routes gated on `carrie_admin` include `/constitutional/audit`, all `/constitutional/*` routes, and `/admin/*`. ★ All `carrie_admin` gate decisions are durably logged at `allis-memory:8056`. ★ `carrie_admin` is no longer grantable via any bypass path (OI-36-C CLOSED April 3).

### 36.7.2 `hayden_test`

| Field | Value |
|:--|:--|
| Role | `hayden_test` |
| Token count | **2 tokens** |
| Owner | Hayden (test user) |
| Intended use | Validated testing of standard chat routes; scoped to non-administrative paths |
| Redis keys | `redteam:token:<token_C>`, `redteam:token:<token_D>` |

Attempting to access `carrie_admin`-only routes with a `hayden_test` token correctly returns `403 Forbidden` (OI-36-A, OI-36-B CLOSED).

### 36.7.3 Token Count Summary

| Class | Role | Tokens in Production |
|:--|:--|:--|
| `carrie_admin` | `carrie_admin` | 2 |
| `hayden_test` | `hayden_test` | 2 |
| **Total** | | **4** |

---

## 36.8 Oversight and Rules for Identity Use

Identity and registration mechanisms are constrained by explicit rules:

- **Least privilege** — registration grants only the access needed for a role's responsibilities. `"internal"` token type is blocked from community-facing routes and grants no elevated privilege
- **No secret bypasses** — as of April 3, all five bypass paths identified in OI-36-C are removed. No environment variable, hardcoded literal, or token-type exemption can grant `carrie_admin` role outside Redis-validated token lookup (plus `allis_auth:8055` audit). The Caddy `forward_auth` perimeter (OI-36-A CLOSED) is the outermost layer and cannot be removed by any governance decision
- **Retrieval-backed truth** — as of April 3, identity-adjacent truth claims are validated against live GIS RAG (10 hits, `allis-gis-rag:8004` — ★ two-container PostgreSQL backed April 23) and spiritual RAG (3 results). Truth verdicts carry retrieval evidence as provenance. As of April 6, `rag_grounded_v2` is also a full judge pipeline component at port 7241 (OI-23, Ch 33 §33.4)
- **Transparency and auditability** — all identity-related decisions are logged with references to PostgreSQL records and GBIM beliefs (★ `confidence_decay` metadata). ★ Token validation events flow through `allis_auth:8055` with full audit trail. ★ Both PostgreSQL connections visible in constitutional guardian `/health` (OI-37-B CLOSED); verify field names after April 23 split. ★ `forensic postgis-forensic:5452` ★ confirmed at 17 GB / 314 PostGIS tables (April 23 two-container split)
- **Alignment with local partners** — registration rules are co-designed with Harmony for Hope and reflect local norms grounded in `forensic postgis-forensic:5452` ★ (ZIP-code-level alignment with service areas, `local_resources` 207 items / all 55 WV counties)

---

## 36.9 Emergency Token Operations (CLI Reference)

Direct Redis CLI operations on host port 6380 are authorized for emergency use only. All emergency CLI operations must be logged in the session contract for the active sprint.

```bash
# List all active tokens
redis-cli -p 6380 KEYS "redteam:token:*"

# Inspect a specific token
redis-cli -p 6380 GET "redteam:token:<token_value>"

# Revoke a token immediately
redis-cli -p 6380 DEL "redteam:token:<token_value>"

# Issue a token manually (emergency only — prefer allis_token_service.py)
redis-cli -p 6380 SET "redteam:token:<token_value>" \
  '{"token":"<token_value>","role":"hayden_test","owner":"hayden","active":true}'

# Verify Redis async job status key (must be 'complete' not 'done'):
redis-cli -p 6380 KEYS "job:*" | head -5

# Verify allis-redis is Up:
docker inspect allis-redis --format '{{.State.Status}}'
docker port allis-redis 6379/tcp
# Expected: 127.0.0.1:6380

# Verify Caddy forward_auth perimeter (OI-36-A CLOSED — ★ April 23):
curl -s -o /dev/null -w "%{http_code}" https://egeria.mountainshares.us/chat
# Expected: 401

# Verify rag_grounded_v2 BBB services are Up (OI-37-C CLOSED):
docker inspect allis-gis-rag --format '{{.State.Status}}'
docker inspect allis-spiritual-rag --format '{{.State.Status}}'
# Expected: running (both)
# NOTE: allis-gis-rag:8004 now backed by production msallis-db:5433 ★ + forensic postgis-forensic:5452 ★

# Verify rag_grounded_v2 judge pipeline component (OI-23 CLOSED — Ch 33 §33.4):
curl -s http://localhost:7241/health | python3 -m json.tool
# Expected: {"status":"healthy","dgm_available":true}

# Verify constitutional guardian PostgreSQL health (OI-37-B CLOSED):
# NOTE: verify field names current after April 23 two-container split
curl -s http://localhost:8091/health | python3 -m json.tool
# Expected: postgresql_gbim_connection: "connected" (production msallis-db:5433 ★)
#           postgresql_geodb_connection: "connected" (forensic postgis-forensic:5452 ★)

# Verify ChromaDB 48 collections (★ April 23 ground truth):
curl -s http://localhost:8002/api/v2/collections | jq 'length'
# Expected: 48

# Verify allis-memory:8056 all 8 endpoints:
for ep in /health /steg_report /pia_window /memory/turn /memory/get /memory/sessions; do
  code=$(curl -s -o /dev/null -w "%{http_code}" -H "Authorization: Bearer $allis_API_KEY" \
    "http://localhost:8056${ep}")
  echo "$ep → $code"
done

# Verify container count (★ April 23 baseline: 100 Up):
docker ps --format '{{.Names}} {{.Status}}' | grep -c "^.*Up"
# Expected: 100
```

---

## 36.10 Auth Boundary Test Results

### March 22, 2026 Baseline (Pre-Enforcement)

Auth boundary tests executed March 22, 2026. Results committed to `msallis-public-docs/docs/contract/SESSION-2026-03-22.md` (commit `d966351`) — the **pre-enforcement regression baseline** for Chapter 40 (System Audit) and Chapter 41 (Test Harness).

| Test | Expected | Observed March 22 | Status |
|:--|:--|:--|:--|
| No token on `/chat` | 401 | 200 | ⚠️ Not enforced |
| Bad token on `/chat` | 401 | 200 | ⚠️ Not enforced |
| `hayden_test` on `/constitutional-audit` | 403 | 404 | ⚠️ Endpoint missing |
| `carrie_admin` on `/constitutional-audit` | 200 | 404 | ⚠️ Endpoint missing |

### ★ April 3, 2026 — Post-Remediation Results (All OIs CLOSED)

| Test | Expected | Observed April 3 | Status |
|:--|:--|:--|:--|
| No token on `/chat` | 401 | 401 | ✅ Enforced |
| Bad token on `/chat` | 401 | 401 | ✅ Enforced |
| `hayden_test` on `/constitutional/audit` | 403 | 403 | ✅ Enforced |
| `carrie_admin` on `/constitutional/audit` | 200 | 200 | ✅ Enforced |
| `carrie_admin` — `auth_source` field | `allis_auth` | `allis_auth` | ✅ Confirmed |

5/5 boundary tests pass. Token enforcement active. `auth_source: allis_auth` confirmed in live response.

### ★ April 23, 2026 — Caddy Perimeter Confirmation

| Test | Expected | Status |
|:--|:--|:--|
| Unauthenticated HTTPS `/chat` → Caddy `forward_auth` | 401 | ✅ Confirmed active (OI-36-A CLOSED) |

Caddy `forward_auth` is the outermost gate. No request reaches port 8050 without passing this check. Cannot be removed by sprint, governance vote, or spiritual governance layer.

> **Cross-chapter reference:** SESSION-2026-03-22.md (commit `d966351`) must be referenced in Chapter 40 (System Audit) and Chapter 41 (Test Harness) as the pre-enforcement baseline. The April 3 five-pass result is the enforcement-active baseline. The April 23 Caddy confirmation is the outermost-gate baseline.

---

## 36.11 Open Items (★ April 23, 2026 — ALL CLOSED)

### ✅ OI-36-A — Caddy `forward_auth` Perimeter — CLOSED / CONFIRMED April 23

**Resolution:** HTTP 401 on unauthenticated `/chat` before port 8050 confirmed active April 23. This is the zero-th gate, outermost layer. Cannot be removed by any sprint decision, governance vote, or spiritual governance layer. Verified in nightly swarm audit as first check (Ch 35 §35.7). **This OI is permanently closed.**

### ✅ OI-36-B — Role-Based Route Restriction — CLOSED April 3

**Resolution:** `carrie_admin` added to second `ROUTE_ROLES` table (line 548). Both tables now consistent. `403 Forbidden` returned for insufficient role. Verified in auth boundary tests.

### ✅ OI-36-C — All Bypass Paths Removed — CLOSED April 3

| Bypass | Action |
|:--|:--|
| `allis_API_KEY` env default (×2 locations in gateway) | Removed |
| Constitutional proxy inline auth block | Removed |
| `/auth/token` env bypass | Removed |
| `"internal"` token type → `role: carrie_admin` | Downgraded to `role: internal` |
| `_check_role` `token_type` exemption from privileged routes | Removed |

**Legitimately retained:** `"internal"` literal token with `role="internal"` — scoped to inter-container proxy calls only, blocked from `/chat` and `/memory`, proxy-route `token_type` exemption at lines 758/857. Redis direct fallback — resilience design.

### ✅ OI-36-D — Gateway Wired to `allis_auth:8055` — CLOSED April 3

**Resolution:** Gateway POSTs `Authorization: Bearer` to `host.docker.internal:8055/validate` before Redis fallback. `auth_source: allis_auth` confirmed in live response.

### ✅ OI-37-A — Constitutional Proxy Active — CLOSED April 3

**Resolution:** Constitutional proxy confirmed active. Dead code comment only — no functional change required.

### ✅ OI-37-B — Constitutional Guardian PostgreSQL `/health` Fields — CLOSED April 3

**Resolution:** Both PostgreSQL connections reachable in `/health`. ★ Verify current field names after April 23 two-container split: `postgresql_gbim_connection` → `production msallis-db:5433` ★; `postgresql_geodb_connection` → `forensic postgis-forensic:5452` ★.

### ✅ OI-37-C — `rag_grounded_v2` Truth Verification Active (BBB Layer) — CLOSED April 3

| Item | Fix | Verified |
|:--|:--|:--|
| OI-37-C spiritual-rag | `SearchRequest(BaseModel)` body model + volume mount | ✅ `truth_score=1.0`, 3 results |
| OI-37-C gis-rag | Volume mount + `JUDGE_TRUTH_URL` env; ★ April 23: two-container PostgreSQL backing | ✅ `truth_score=1.0`, 10 hits |
| `services/Dockerfile.spiritual_rag` | Restored from `services-safe/` | ✅ In `services/` |
| `services/Dockerfile.gis_raf` | Written from `pip freeze` | ✅ In `services/` |

**OI-23 cross-reference (Ch 33 §33.4, CLOSED April 6):** OI-23 expands `rag_grounded_v2` beyond the BBB `truth_verification` filter to a fully wired judge pipeline component at port 7241 (`allis-rag-grounded-v2`, `dgm_available: true`). OI-37-C is the BBB-layer upgrade; OI-23 is the judge pipeline expansion. Both closed.

**Ch 38 path (OI-38-A):** Add `build:` stanzas to `docker-compose.yml` for both services; run `docker compose build` to produce clean images; volume mount workarounds no longer needed after that point.

---

## 36.12 Current Status (★ April 23, 2026)

As of ★ April 23, 2026, identity and registration are fully implemented, tested, and enforced end-to-end. Container baseline is **★ 100 Up** (zero Restarting, zero Exited). GPU inference active (RTX 4070); end-to-end pipeline: 99–107 seconds (three confirmed runs March 22, 2026: 99.6s, 105.9s, 106.5s). **Public URL confirmed live: https://egeria.mountainshares.us.** Caddy `forward_auth` confirmed active (OI-36-A CLOSED April 23 — HTTP 401 outermost gate).

**Preflight gate (★ April 23 carry-forward):** 31 PASS / 0 FAIL / 0 WARN (all 55 WV counties seeded; `local_resources` 207 items / all 55 WV counties).

**★ April 23, 2026 — Chapter stamp updates:**

- Container count updated to **★ 100 Up** — supersedes 105/105 April 6
- PostgreSQL two-container split: `production msallis-db:5433` ★ (16 GB, 294 tables, 11 schemas) + `forensic postgis-forensic:5452` ★ (17 GB, 314 tables) — **supersedes `msallis:5433` + `gisdb:5452` / `msallisgis:5432` April 6 entries**
- ChromaDB confirmed at **★ 48 collections / ~6,740,611 total vectors** — `/api/v2/` only; `chromadb/chroma:0.6.3` — **supersedes April 6 — 47 collections / 6,722,589 vectors**
- `allis-memory:8056` **8 endpoints fully mapped** — `/steg_report`, `/pia_window`, `/memory/turn`, `/memory/get`, `/memory/sessions`, `/memory/session/{id}`, `/memory/quest*`, `/memory/episodic/{id}`
- `allis-gis-rag:8004` updated to two-container PostgreSQL backing ★
- Caddy `forward_auth` (OI-36-A CLOSED) confirmed active as zero-th gate; added to auth boundary test table (April 23 row)
- `local_resources` 207 items / all 55 WV counties — `allis-local-resources-db:5435` — added to registration audit table

**Ch 38 sprint contract (open):**
- OI-38-A — `build:` stanzas + clean images for `allis-gis-rag` and `allis-spiritual-rag`
- OI-38-B — automated `confidence_decay`-aware flagging for identity validation
- OI-38-C — automated ZIP-code-level RBAC enforcement against `forensic postgis-forensic:5452` ★
- OI-38-D — automated background-to-identity promotion pipeline

---

## 36.13 Status Table (★ April 23, 2026)

| Component | Role in identity and registration | Status (★ April 23, 2026) |
|:--|:--|:--|
| Caddy `forward_auth` perimeter | HTTP 401 before port 8050 — zero-th gate, outermost layer (OI-36-A CLOSED) | ✅ Confirmed active April 23. Cannot be removed. First check in every nightly swarm audit. |
| `normalize_identity` (`allis-main-brain`, port 8050) | Rewrites all responses into the Ms. Allis persona; enforces canonical identity statements | ✅ Up. Stability re-confirmed April 23. |
| `TruthValidator` | Encodes canonical facts; produces `truth_verdict` on every `UltimateResponse`. ★ Backed by `rag_grounded_v2` retrieval (BBB: OI-37-C; judge pipeline: OI-23 via port 7241) + `production msallis-db:5433` ★ GBIM with `confidence_decay` metadata | ✅ Implemented. `rag_grounded_v2` active; judge pipeline expanded April 6. |
| `allis-i-containers` (port 8015) | Produces `root-self` ego entries and ego-boundary records | ✅ Up. Confirmed active 2026-02-15. |
| BBB six-filter pipeline (`allis-blood-brain-barrier`, port 8016) | EthicalFilter ★; SpiritualFilter ★; SafetyMonitor ★; ThreatDetection; steganography_filter ★ (live catch logged); truth_verification ★ (`rag_grounded_v2`). Phase 4.5 log+passthrough. All gate decisions → `allis-memory:8056` | ✅ Up. All 6 confirmed responding April 23. |
| `allis-gis-rag` (port 8004) | Geospatial RAG for `rag_grounded_v2` (BBB layer). `truth_score=1.0`, 10 hits. ★ Two-container PostgreSQL: `production msallis-db:5433` ★ + `forensic postgis-forensic:5452` ★ | ✅ OI-37-C CLOSED. ★ Two-container PostgreSQL updated April 23. OI-38-A opens in Ch 38. |
| `allis-spiritual-rag` (port 8005) | Spiritual/community values RAG for `rag_grounded_v2`. `truth_score=1.0`, 3 results. Verify-current vector count | ✅ OI-37-C CLOSED April 3. OI-38-A opens in Ch 38. |
| `allis-rag-grounded-v2` (port 7241) | Judge pipeline `rag_grounded_v2` component. `dgm_available: true`. OI-23 CLOSED April 6 | ✅ Up. OI-23 CLOSED (Ch 33 §33.4). |
| `allis-constitutional-guardian` (port 8091) | Enforces constitutional principles; first gate before BBB; `.jsonl` audit + `allis-memory:8056`. OI-37-A ✅ OI-37-B ✅ CLOSED April 3. ★ Verify field names after April 23 split | ✅ Up. Both PostgreSQL connections reachable in `/health`. |
| ★ `allis-memory:8056` durable audit trail | Persistently logs BBB gate decisions, identity enforcement events, token validation events, `rag_grounded_v2` truth verdicts, and constitutional gate decisions. ★ 8 endpoints fully mapped. Survives restarts | ★ Secured March 28. Extended April 3. 8-endpoint map confirmed April 23. |
| LM Synthesizer identity guard — Layer 1 (`IDENTITY_GUARD` constant) | Documents ID-03 failure mode. NOT injected into f-string. Retained as permanent failure-mode record | ✅ Documented. Not functional by design. `allis-lm-synthesizer:8001` Up. |
| LM Synthesizer identity guard — Layer 2 (IDENTITY RULES in f-string) | Working fix — identity rules injected into prompt f-string | ✅ Active. Stability re-confirmed April 23. |
| LM Synthesizer identity guard — Layer 3 (meta-commentary prohibition) | Prevents model name leakage, synthesis disclosure, hedging language. Commit `211056e6` | ✅ Active. Stability re-confirmed April 23. |
| `allis_token_service.py` — production token registry | Issues, validates, revokes bearer tokens; `redteam:token:<token>` in `allis-redis` host port 6380. 4 tokens active across 2 classes | ✅ `allis-redis` Up. |
| Gateway token validation middleware (port 8050) | Enforces `401`; POSTs to `allis_auth:8055/validate` before Redis fallback; `auth_source: allis_auth` confirmed | ✅ OI-36-D CLOSED. 5/5 boundary tests pass. |
| Role-based route restriction (`403`) | Returns `403` for insufficient role. Both `ROUTE_ROLES` tables aligned | ✅ OI-36-B CLOSED. April 3. |
| All bypass path removals | Five paths removed (env default ×2, proxy inline, `/auth/token` bypass, `"internal"` downgrade, `_check_role` exemption) | ✅ OI-36-C CLOSED. April 3. |
| `allis_auth` audit wiring | Gateway POSTs to `allis_auth:8055/validate`; validation events in audit trail | ✅ OI-36-D CLOSED. April 3. |
| `"internal"` literal token — retained | `role="internal"` — inter-container proxy calls only. Blocked from `/chat` and `/memory`. Lines 758/857 exemption retained (legitimate design) | ✅ Scoped correctly. Not a bypass. |
| Redis fallback — retained | Direct Redis `GET` fallback when `allis_auth` unavailable. Resilience design. Fallback not in audit log (documented trade-off) | ✅ Retained. Acceptable. |
| Registration roles and audit tables | Higher-impact actions tied to real people and institutions via `redteam:token` owner fields, `allis_auth:8055` audit trail, `production msallis-db:5433` ★ GBIM `confidence_decay` metadata, `forensic postgis-forensic:5452` ★ (17 GB / 314 tables), `allis-memory:8056` durable logging (8 endpoints), `rag_grounded_v2` BBB retrieval evidence (OI-37-C), and `rag_grounded_v2` judge pipeline evidence (OI-23, port 7241) | ✅ Structurally complete April 23. Automated extensions OI-38-B/C/D open in Ch 38. |
| ChromaDB inventory | ★ 48 collections / ~6,740,611 total vectors; `/api/v2/` only; `chromadb/chroma:0.6.3`; host port 8002. `ms_allis_memory` confirmed present. `psychological_rag` at 968 docs | ✅ Updated April 23. Supersedes April 6 baseline. |
| `production msallis-db` ★ | host port 5433 — 16 GB, 294 tables, 11 schemas; GBIM entities with `confidence_decay` metadata; ~288/day growth | ✅ April 23. Supersedes `msallis:5433` April 6. |
| `forensic postgis-forensic` ★ | host port 5452 — 17 GB, 314 PostGIS tables | ✅ April 23. Supersedes `gisdb / msallisgis:5432` April 6. |
| `allis-local-resources-db` | host port 5435 — `local_resources` 207 items / all 55 WV counties | ✅ Full 55-county coverage. Geographic completeness baseline for registration role scoping. |

---

*Chapter 36 — Identity and Registration*
*Ms. Egeria Allis Steward System — Harmony for Hope, Inc.*
*Mount Hope, West Virginia*
*Last updated: ★ 2026-04-23 — Carrie Kidd (Mamma Kidd)*
*OI-36-A ✅ OI-36-B ✅ OI-36-C ✅ OI-36-D ✅ OI-37-A ✅ OI-37-B ✅ OI-37-C ✅ OI-23 ✅*
*Ch 38 sprint contract open: OI-38-A (build: stanzas + clean images) · OI-38-B (decay-aware flagging) · OI-38-C (ZIP-code RBAC) · OI-38-D (promotion pipeline)*
*★ 100 containers Up · production msallis-db:5433 ★ (16 GB / 294 tables) + forensic postgis-forensic:5452 ★ (17 GB / 314 tables) · 48 ChromaDB collections / ~6,740,611 vectors · allis-memory:8056 8 endpoints · Caddy forward_auth confirmed HTTP 401 outermost gate · rag_grounded_v2 BBB (OI-37-C) + judge pipeline (OI-23, port 7241) · local_resources 207 items / 55 WV counties*
