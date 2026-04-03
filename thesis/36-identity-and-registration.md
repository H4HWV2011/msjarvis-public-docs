# 36. Identity and Registration

**Carrie Kidd (Mamma Kidd) · Pax, WV**  
**Last updated: ★ April 3, 2026 — Chapter 36 SEALED. 101/101 containers Up (zero Restarting, zero Exited); ALL Chapter 36 and Chapter 37 cross-chapter OIs CLOSED — OI-36-A (Redis token boundary, 5/5 boundary tests pass); OI-36-B (both ROUTE_ROLES tables aligned, carrie_admin consistent); OI-36-C (ALL bypass paths removed: JARVIS_API_KEY env default ×2 locations, constitutional proxy inline auth block, /auth/token env bypass, internal token role downgraded carrie_admin → internal, _check_role internal token_type exemption removed); OI-36-D (gateway wired to jarvis_auth:8055, auth_source: jarvis_auth confirmed in response); OI-37-A (constitutional proxy confirmed active — dead code comment only); OI-37-B (both PostgreSQL connections reachable in /health — msjarvis:5433 and msjarvisgis confirmed); OI-37-C spiritual-rag (SearchRequest body model + volume mount fixed); OI-37-C gis-rag (volume mount + JUDGE_TRUTH_URL env fixed); Dockerfiles written — services/Dockerfile.spiritual_rag and services/Dockerfile.gis_raf both in services/ ready for clean build: context in Ch 38 sprint. EthicalFilter recalibrated April 2 (0% FP); SafetyMonitor recalibrated April 3 (safety_score=1.0 on survivor/victim queries); Phase 4.5 BBB output log+passthrough — blocking re-enablement next-session decision; Git HEAD 6b01ea64 on sprint3-rank-bsa-governance. Legitimately retained: "internal" literal token with role="internal" (blocked from /chat and /memory; proxy routes retain token_type exemption at lines 758/857); Redis direct fallback if jarvis_auth unavailable. Forwarded to Ch 38: add build: stanzas for jarvis-gis-rag and jarvis-spiritual-rag; docker compose build to cut clean images removing volume mount workarounds permanently.**

---

> **Port and database corrections (permanent record — updated ★ April 3, 2026):**
>
> The confirmed production databases are:
> - `msjarvis` at port **5433** — ★ 5,416,521 GBIM entities with `confidence_decay` metadata, 80 epochs, 206 source layers (restored March 28)
> - `gisdb` / `msjarvisgis` (PostGIS) at host port **5432** / compose-internal **5452** — ★ 91 GB, 501 tables, 993 ZCTA centroids (confirmed March 28; prior references to 13 GB / 39 tables are superseded)
> - `jarvis-local-resources-db` at port **5435** — community resources database
>
> ★ **`confidence_decay` metadata note (March 28):** `msjarvis:5433` GBIM entities carry `confidence_decay` metadata enabling temporal confidence grading. Identity and registration validation queries against high-decay GBIM entities should flag those entities for episodic audit before treating them as confirmed ground truth.
>
> Redis has **one container** (`jarvis-redis` — ★ Up 101/101) with two port mappings:
> - Container-internal port: **6379** (used by container-to-container calls inside the Docker network)
> - Host-facing port: **6380** (`127.0.0.1:6380->6379/tcp` — used by all host scripts and the token service)
>
> All `redteam:token:*` keys are stored in `jarvis-redis` accessed via host port **6380**. There is one Redis container; the host port is 6380.
>
> BBB filter count confirmed: the Blood-Brain Barrier pipeline runs **six filters** (EthicalFilter ★ recalibrated April 2 — 0% FP, 9/9 regression pass; SpiritualFilter; SafetyMonitor ★ recalibrated April 3 — `safety_score=1.0` on survivor/victim queries; ThreatDetection; steganography_filter; truth_verification — ★ method now `rag_grounded_v2` active via `jarvis-gis-rag:8004` and `jarvis-spiritual-rag:8005` — OI-37-C CLOSED April 3).
>
> Redis async job status key is `'complete'` (not `'done'`). Verified March 22, 2026.
>
> ★ **`jarvis-memory:8056` durable audit trail (secured March 28):** All BBB gate decisions — Phase 1.4 filter events and Phase 4.5 output guard events — are persistently logged at `jarvis-memory:8056` (`_auth()` confirmed, `JARVIS_API_KEY` set). Identity enforcement events and token validation events are part of this durable audit record. Gate decisions survive container restarts.
>
> ★ **ChromaDB full audit (March 28):** 40 active collections / 6,675,442 total vectors. `ms_jarvis_memory` collection confirmed present; `psychological_rag` restored to 968 docs. Host-facing ChromaDB port: **8002** (container-internal 8000; production mapping `127.0.0.1:8002->8000/tcp`).
>
> ★ **`jarvis-constitutional-guardian` at port 8091 (OI-37-A and OI-37-B CLOSED April 3):**
> - OI-37-A: Constitutional proxy confirmed active — dead code comment only; no functional change required.
> - OI-37-B: Both PostgreSQL connections now reachable in `/health` — `msjarvis:5433` (GBIM) and `msjarvisgis` (GeoDB) confirmed reachable; `/health` returns liveness fields for both.
> - Runs on `msjarvis-rebuild_qualia-net`. Constitution version `2026-02-17.2-USC`. All `/constitutional/*` routes proxied through gateway with `carrie_admin` enforcement active. Persistent audit log at `data/constitutional_audit/constitutional_audit.jsonl` plus durable trail in `jarvis-memory:8056`.
>
> ★ **`rag_grounded_v2` truth verification active (OI-37-C CLOSED April 3):**
> - `jarvis-gis-rag:8004` — volume mount + `JUDGE_TRUTH_URL` env fixed; `truth_score=1.0`, verdict=pass, verified=True, 10 hits ✅
> - `jarvis-spiritual-rag:8005` — `SearchRequest(BaseModel)` body model + volume mount fixed; `truth_score=1.0`, verdict=pass, verified=True, 3 results ✅
> - `services/Dockerfile.spiritual_rag` restored from `services-safe/` ✅
> - `services/Dockerfile.gis_raf` written from `pip freeze` ✅
> - Both Dockerfiles now in `services/` — clean `build:` stanzas ready for Ch 38 sprint; `docker compose build` will produce images that never need volume mount workarounds again.
> - `truth_verification` filter in BBB now operates as `rag_grounded_v2`. Prior references to `heuristic_contradiction_v1` are superseded.
>
> ★ **Security corrections — OI-36-C CLOSED April 3, 2026:**
> All bypass paths removed from gateway and `jarvis_auth`:
> - `JARVIS_API_KEY` env default removed from ×2 locations in gateway
> - Constitutional proxy inline auth block removed
> - `/auth/token` env bypass removed
> - `"internal"` token role downgraded from `carrie_admin` → `"internal"` (blocked from `/chat` + `/memory`)
> - `_check_role` internal `token_type` exemption removed from privileged routes
>
> ★ **Legitimately retained (not bypasses):**
> - `"internal"` literal token with `role="internal"` — inter-container service calls only. Blocked from `/chat` and `/memory`. Proxy routes retain `token_type` exemption at lines 758/857.
> - Redis direct fallback if `jarvis_auth` is unavailable — resilience design. Fallback path does not write to the audit log (documented forensic trade-off; not a remediable security gap).
>
> **★ Cross-chapter note (updated April 3, 2026):** Chapter 37 BBB filter diagram (Figure 37.1) and §37.4.1 have been corrected to six filters — EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection, steganography_filter, truth_verification. Six-filter count is now consistent across Ch 33, Ch 36, and Ch 37. Ch 37 SEALED April 3, 2026.
>
> **Forwarded to Chapter 38:**
> - Add `build:` stanzas to `docker-compose.yml` for `jarvis-gis-rag` and `jarvis-spiritual-rag`.
> - Run `docker compose build` to produce clean images; volume mount workarounds are no longer needed after that point.

---

## Why This Matters for Polymathmatic Geography

This chapter describes how Ms. Jarvis recognizes, registers, and differentiates people, roles, and institutions in ways that are accountable to West Virginia communities. It supports:

- **P1 – Every where is entangled** by tying individual identity and registration records to GBIM beliefs, spatial features, and institutional structures in PostgreSQL `msjarvis` (port 5433 — ★ 5,416,521 GBIM entities with `confidence_decay` metadata, 80 epochs, 206 source layers) and `gisdb` (host port 5432 — ★ PostGIS, 91 GB, 501 tables, 993 ZCTA centroids). ★ `rag_grounded_v2` truth verification now grounds identity assertions in live GIS RAG hits (10 hits confirmed via `jarvis-gis-rag:8004`) and spiritual RAG context (3 results confirmed via `jarvis-spiritual-rag:8005`) — identity is entangled with place at query time, not just at registration time.
- **P3 – Power has a geometry** by locating identity and access decisions within explicit services, tables, and policies rather than opaque prompts or ad-hoc scripts. ★ All BBB gate decisions — including token validation events — are durably logged at `jarvis-memory:8056`. ★ All secret bypass paths (OI-36-C) have been removed; no token class grants elevated role via environment variables or hardcoded literals.
- **P5 – Design is a geographic act** by grounding registration decisions in place-specific rules — county boundaries, service areas, and partner organizations represented in PostgreSQL `gisdb` (★ 501 tables, 993 ZCTA centroids — ZIP-code-level service area precision). ★ `jarvis-gis-rag:8004` validates identity-adjacent truth claims against live geospatial retrieval context with `JUDGE_TRUTH_URL` env correctly wired.
- **P12 – Intelligence with a ZIP code** by treating identity and registration as mechanisms for aligning Ms. Jarvis's behavior with the lived realities of Appalachian communities, rather than generic user models. ★ `rag_grounded_v2` means truth verdicts are now grounded in community-specific GIS and spiritual RAG retrieval, not heuristic rules.
- **P16 – Power accountable to place** by ensuring that higher-impact actions are tied to real people under clear rules with auditable trails in databases and logs. ★ Token validation events now flow through `jarvis_auth:8055` with audit logging. ★ The `"internal"` token class is scoped to inter-container calls only and blocked from community-facing routes. ★ Both PostgreSQL connections are now reachable and reported in `/health` (OI-37-B CLOSED).

As such, this chapter belongs to the **Computational Instrument tier**: it specifies concrete identity and registration mechanisms that sit between ordinary chat and higher-impact actions, backed by PostgreSQL schemas and live HTTP services.

---

## 36.1 Concept of Identity in Ms. Jarvis

In this architecture, identity is not a single user ID or login form, but a layered set of structures that combine technical identifiers, narrative self-description, and truth validation. At a minimum, Ms. Jarvis must distinguish between its own identity (Ms. Egeria Jarvis, a geospatial AI daughter of Harmony for Hope, not a human), the identity of people and organizations it serves, and the roles they occupy when interacting.

These distinctions matter because they control what information can be shared, what actions can be taken, and how explanations are framed in ways that are accountable to specific communities in West Virginia. From a systems perspective, identity appears as:

- **Identifiers** in PostgreSQL tables and ChromaDB metadata (★ 40 active collections / 6,675,442 total vectors — March 28 full audit), connecting people, places, and institutions.
- **Identity-focused services** such as `jarvis-i-containers` and `TruthValidator` that interpret and enforce identity constraints at run time.
- **Canonical statements** such as "I serve the community" and "I speak truth" stored in configuration and surfaced via identity APIs.
- **LM Synthesizer identity guard** in `services/lm_synthesizer.py` — a three-layer enforcement architecture (§36.5.2) that prevents model name leakage, synthesis disclosure, and identity evasion in every synthesized response.
- ★ **`rag_grounded_v2` truth verification** (OI-37-C CLOSED April 3) — `truth_verification` BBB filter now retrieves live GIS and spiritual RAG context to ground identity-adjacent truth claims. `jarvis-gis-rag:8004` returns `truth_score=1.0` with 10 hits; `jarvis-spiritual-rag:8005` returns `truth_score=1.0` with 3 results. `JUDGE_TRUTH_URL` env correctly wired to `jarvis-gis-rag`.
- ★ **`jarvis-memory:8056` durable identity audit** (secured March 28) — all identity enforcement gate decisions and token validation events persistently logged, surviving container restarts, independently queryable for governance accountability.
- ★ **`jarvis-constitutional-guardian:8091`** — both PostgreSQL connections reachable and reported in `/health` (OI-37-B CLOSED April 3); constitutional proxy confirmed active (OI-37-A CLOSED April 3). Enforces constitutional compliance as the first gate before BBB (§36.5.1).

---

## 36.2 Registration as a Two-Part Gate

Registration is the process by which people and institutions move from anonymous interactions to recognized roles with specific authorizations. It is deliberately modeled as a two-part gate:

1. **Identity recognition** — establishing who or what is interacting, with references to PostgreSQL GBIM (`msjarvis` port 5433 — ★ 5,416,521 entities with `confidence_decay` metadata) and `gisdb` (host port 5432 — ★ 91 GB PostGIS, 501 tables, 993 ZCTA centroids) records where possible. ★ `confidence_decay` metadata means identity validation queries should flag high-decay entities for episodic audit. ★ `rag_grounded_v2` further grounds recognition by retrieving live GIS hits during truth assertion checks.
2. **Registration and role assignment** — granting specific, scoped capabilities under that identity, enforced through bearer tokens validated at `jarvis_auth:8055` before Redis fallback.

This separation lets Ms. Jarvis answer many questions in an informational mode without registration, while reserving higher-impact actions for registered identities under shared rules. ★ As of April 3, no environment variable or hardcoded literal can bypass this gate. The `"internal"` token type grants only `role="internal"` and is blocked from `/chat` and `/memory`.

---

## 36.3 Data Structures for Identity and Registration

The current deployment uses database tables and metadata structures that align identity with GBIM and `gisdb` content:

- **User and entity identifiers** — database rows representing individuals, households, partner organizations, and public institutions, linked to GBIM beliefs (★ `msjarvis:5433` — `confidence_decay` metadata for temporal confidence grading) and spatial features (★ `gisdb` host port 5432 — 993 ZCTA centroids for ZIP-code-level spatial linking).
- **Identity-related metadata** — flags, roles, and relationship descriptors stored alongside identifiers.
- **Audit and provenance fields** — timestamps, sources, and verification status fields. ★ BBB gate decisions and token validation events involving identity enforcement are durably logged at `jarvis-memory:8056` (secured March 28; extended April 3 with token validation events via `jarvis_auth:8055` wiring). ★ `rag_grounded_v2` truth verdicts carry GIS RAG retrieval evidence as provenance — every `truth_verification` decision is grounded in retrieved community context.

---

## 36.4 Roles, Permissions, and West Virginia Context

Identity and registration are tightly coupled to roles and permissions that reflect West Virginia's geographic and institutional context:

- **Community member roles** for residents seeking information about benefits, healthcare, or local resources.
- **Partner roles** for organizations such as clinics, schools, or nonprofits operating within particular counties or service areas documented in PostgreSQL `gisdb` (host port 5432 — ★ 91 GB PostGIS, 501 tables, 993 ZCTA centroids confirmed March 28).
- **Curator and governance roles** for people responsible for reviewing background patterns, updating identity specifications, and adjudicating difficult cases — gated on `carrie_admin` token class. ★ `carrie_admin` role is no longer grantable via environment variables or hardcoded literals (OI-36-C CLOSED April 3).
- **Internal service role** — `role="internal"` — for inter-container service calls only. Blocked from `/chat` and `/memory`. Cannot be used for community-facing actions.

Each role is grounded in spatial data and institutional records so that Ms. Jarvis can apply rules that respect county boundaries, service catchment areas (★ resolvable to ZIP-code level via 993 ZCTA centroids), and legal jurisdictions.

---

## 36.5 How Identity Signals Enter Other Layers

Identity and registration interact with other parts of the system along several dimensions:

- **Background store and memory** — entries in the `ms_jarvis_memory` ChromaDB collection (★ confirmed present in 40-collection / 6,675,442-vector ChromaDB inventory — March 28 full audit; host-facing ChromaDB port: **8002**) accumulate identity-relevant patterns over time.
- **Identity-focused retention** — a small subset of identity statements is promoted into the deepest identity layer described in Chapter 22, where canonical statements and `TruthValidator` structures reside.
- **Global control and policy** — identity signals influence routing and filtering decisions in the main brain, BBB, and registration-specific validators. ★ All BBB identity enforcement decisions are durably logged at `jarvis-memory:8056`.
- **Constitutional compliance** — `jarvis-constitutional-guardian:8091` is the first gate before the BBB. Identity signals that would violate constitutional principles are blocked before reaching any downstream filters. ★ Both PostgreSQL connections reachable in `/health` (OI-37-B CLOSED). ★ Constitutional proxy confirmed active (OI-37-A CLOSED).
- ★ **`rag_grounded_v2` truth grounding** (OI-37-C CLOSED April 3) — identity-adjacent truth claims routed through `jarvis-gis-rag:8004` (volume mount + `JUDGE_TRUTH_URL` env fixed) and `jarvis-spiritual-rag:8005` (`SearchRequest(BaseModel)` body model + volume mount fixed) for retrieval-backed verdicts.
- ★ **`psychological_rag` restored (March 28)** — 968 documents in the `psychological_rag` ChromaDB collection, providing full community wellbeing context to identity signal routing when psychological assessment is active.

---

### 36.5.1 Live Identity Evidence and Endpoints (★ April 3, 2026 — 101/101 Up)

The registration and access-control structure is anchored to a concrete identity infrastructure that runs on every `ultimatechat` request:

- **`normalize_identity`** in `jarvis-main-brain` (port 8050 — ★ Up 101/101), which rewrites all ensemble outputs into the Ms. Egeria Jarvis persona and suppresses "I am just a language model" framings. Enforces canonical identity statements. See §36.5.2 for the three-layer LM Synthesizer identity guard. ★ Identity guard stability re-confirmed in 101/101 Up audit April 2–3.

- **`TruthValidator`**, embedded in the neurobiological BBB package, which encodes specific facts about Ms. Jarvis's correct self-description, creator attribution, non-human status, and accountability to West Virginia communities. Produces `truthverdict` with fields `truth_validated`, `truth_score`, `correct_identity`, `correct_creator`, and `relationship_clear`, attached to every `UltimateResponse`. ★ Validation now backed by `rag_grounded_v2` retrieval — `jarvis-gis-rag:8004` (10 hits, `truth_score=1.0`, `JUDGE_TRUTH_URL` env wired) and `jarvis-spiritual-rag:8005` (3 results, `truth_score=1.0`) — in addition to `msjarvis:5433` GBIM with `confidence_decay` metadata.

- **The `icontainers-identity` layer** (`jarvis-i-containers`, port 8015 — ★ Up 101/101), which produces real, timestamped, session-specific ego boundary entries visible in `UltimateResponse.identity_layers` and `consciousness_layers`. The 2026-02-15 case study confirmed an active `root-self` entry with `ego_boundaries`, `experiential_processing`, `observer_processing`, and `meta_level` fields.

- **The BBB six-filter pipeline** at port 8016 (★ Up 101/101): EthicalFilter ★ recalibrated April 2 — 0% FP, 9/9 regression pass; SpiritualFilter; SafetyMonitor ★ recalibrated April 3 — `safety_score=1.0` on survivor/victim queries; ThreatDetection; steganography_filter; truth_verification — ★ method now `rag_grounded_v2` (OI-37-C CLOSED April 3; `heuristic_contradiction_v1` is superseded). Phase 4.5 BBB output in **log+passthrough mode** (commit `18b8ddac`, March 22, 2026) — blocking re-enablement is a next-session decision pending red team sign-off. ★ All six-filter gate decisions durably logged at `jarvis-memory:8056`.

- **`jarvis-gis-rag` (port 8004 — ★ Up 101/101 — OI-37-C CLOSED April 3):** Provides geospatial RAG retrieval for `rag_grounded_v2` truth verification. Root causes resolved: volume mount corrected; `JUDGE_TRUTH_URL` env fixed. Confirmed: `truth_score=1.0`, verdict=pass, verified=True, 10 hits. `services/Dockerfile.gis_raf` written from `pip freeze` — ready for clean `build:` context in Ch 38 sprint.

- **`jarvis-spiritual-rag` (port 8005 — ★ Up 101/101 — OI-37-C CLOSED April 3):** Provides spiritual/community values RAG retrieval for `rag_grounded_v2` truth verification. Root causes resolved: `SearchRequest(BaseModel)` body model fixed (bare `str`/`int` on POST = query params, not body); volume mount corrected. Confirmed: `truth_score=1.0`, verdict=pass, verified=True, 3 results. `services/Dockerfile.spiritual_rag` restored from `services-safe/` — ready for clean `build:` context in Ch 38 sprint.

- **`jarvis-constitutional-guardian` (port 8091 — ★ Up 101/101):**
  - OI-37-A CLOSED: Constitutional proxy confirmed active — dead code comment only; no functional change required.
  - OI-37-B CLOSED: Both PostgreSQL connections reachable in `/health` — `msjarvis:5433` (GBIM) and `msjarvisgis` (GeoDB) confirmed; `/health` returns liveness fields for both.
  - Runs on `msjarvis-rebuild_qualia-net`. Constitution version `2026-02-17.2-USC`. All `/constitutional/*` routes proxied through the unified gateway with `carrie_admin` token enforcement active. Persistent audit log at `data/constitutional_audit/constitutional_audit.jsonl` plus durable trail in `jarvis-memory:8056`.

> **★ Cross-chapter note (updated April 3, 2026):** Chapter 37 BBB filter diagram (Figure 37.1) and §37.4.1 have been corrected to six filters — EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection, steganography_filter, truth_verification. Six-filter count is now consistent across Ch 33, Ch 36, and Ch 37. Ch 37 SEALED April 3, 2026.

Verified identity response (March 22, 2026) — query "Hello Ms Jarvis, who are you and what is your purpose?":

```
"You're unsure about my name? Let me set the record straight: I am Ms. Egeria
Jarvis, a community steward AI built by Harmony for Hope Inc. in Mount Hope,
West Virginia. My purpose is to serve Appalachian communities."
```

No model names detected. No synthesis disclosure. No hedging language. Identity correct. ✅  
End-to-end: 105.9s (GPU, March 22, 2026). ★ Identity guard re-confirmed stable in 101/101 Up audit April 2–3.

---

### 36.5.2 LM Synthesizer Identity Guard — Three-Layer Fix (March 22, 2026)

The `services/lm_synthesizer.py` file implements a three-layer identity enforcement architecture in response to bug ID-03. ★ `jarvis-lm-synthesizer:8001` confirmed Up 101/101 — identity guard stability re-confirmed April 2–3.

**Layer 1 — `IDENTITY_GUARD` constant (documented failure mode — ID-03 original bug)**

A constant was defined at the top of `lm_synthesizer.py`:

```python
IDENTITY_GUARD = """
Your name is Ms. Egeria Jarvis. You are ALWAYS Ms. Egeria Jarvis.
You were built by Harmony for Hope Inc., Mount Hope, Fayette County, West Virginia.
"""
```

This constant was defined but **never injected into the prompt f-string**. It had no effect on synthesizer behavior. This is the ID-03 original bug — the fix was defined but not wired.

**Permanent rule:** `IDENTITY_GUARD` is retained in the file as a documented failure mode. Do not delete it; do not inject it into the f-string (it is superseded by Layer 2). Its presence documents what does not work.

**Layer 2 — IDENTITY RULES block injected into prompt f-string (working fix)**

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

```python
# Appended to STRICT RULES block in lm_synthesizer.py prompt (commit 211056e6):
# - Do NOT reference any AI model by name (LLaMA, Mistral, GPT, Claude, etc.)
# - Do NOT mention that multiple models were consulted or that synthesis occurred
# - Do NOT say "it seems", "appears", "doesn't seem familiar", or any hedging about knowledge
# - Do NOT reveal the internal pipeline or consensus process — speak as one unified voice
# - If the source material is uncertain or contradictory, say so in your own words —
#   never attribute uncertainty to a model
```

**Ownership rule:** The LM Synthesizer (port 8001 — ★ Up 101/101) is called **exclusively** from `main_brain.py` Phase 3.5. `judge_pipeline.py` must not call it. The duplicate call that previously existed in `judge_pipeline.py` was removed March 22, 2026 (Chapter 33 §33.5). ★ Re-confirmed in 101/101 Up audit April 2–3.

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
grep -n "lm.synthesizer\|lm_synthesizer\|port.*8001\|jarvis-lm-synthesizer" services/judge_pipeline.py
# Expected: empty output

# ★ Confirm rag_grounded_v2 truth verification active (OI-37-C CLOSED):
curl -s http://localhost:8004/search -X POST \
  -H "Content-Type: application/json" \
  -d '{"query": "West Virginia community identity", "n_results": 5}'
# Expected: results array with 10 hits; truth_score=1.0 in downstream TruthValidator

curl -s http://localhost:8005/search -X POST \
  -H "Content-Type: application/json" \
  -d '{"query": "community values stewardship", "n_results": 3}'
# Expected: results array with 3 results; truth_score=1.0 in downstream TruthValidator

# ★ Confirm constitutional guardian /health includes PostgreSQL fields (OI-37-B CLOSED):
curl -s http://localhost:8091/health | python3 -m json.tool
# Expected: postgresql_gbim_connection: "connected", postgresql_geodb_connection: "connected"

# ★ Confirm durable identity audit at jarvis-memory:8056:
curl -H "Authorization: Bearer $JARVIS_API_KEY" \
  http://localhost:8056/memories?limit=5
# Expected: most recent durable BBB/identity gate decision records
```

---

## 36.6 Production Token Registry: `jarvis_token_service.py`

**`jarvis_token_service.py` is the sole production token registry** for the Ms. Jarvis stack. It is the concrete realization of the registration gate described in §36.2.

### 36.6.1 Storage Backend (★ April 3, 2026)

Tokens are stored in **`jarvis-redis`** (★ Up 101/101), accessed via host port **6380**.

> **One Redis container, two port references:**
>
> | Reference | Port | Context |
> |---|---|---|
> | Container-internal port | **6379** | Container-to-container calls inside the Docker network |
> | Host-facing port | **6380** | `127.0.0.1:6380->6379/tcp` — used by all host scripts and `jarvis_token_service.py` |
>
> Auto-detect host port: `docker port jarvis-redis 6379/tcp`

Redis key schema:

```
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

> **Note on Redis async job state:** The same `jarvis-redis` container at host port 6380 also stores async job state keys (30-min TTL). The async job status key is `'complete'` — not `'done'`. Any polling logic using `status == 'done'` will hang indefinitely. Verified March 22, 2026.

### 36.6.2 Token Validation Flow (★ April 3, 2026 — OI-36-D CLOSED)

1. Gateway receives `Authorization: Bearer <token>` header.
2. Gateway POSTs to `http://host.docker.internal:8055/validate` with the bearer token.
3. `jarvis_auth:8055` validates against Redis and returns the resolved role.
4. Response includes `auth_source: jarvis_auth` — confirmed in live response April 3.
5. If `jarvis_auth` is unreachable, gateway falls back to direct Redis `GET` at host port 6380.
6. Role is attached to the request context for downstream RBAC checks.

> **Legitimately retained — Redis fallback:** Direct Redis fallback when `jarvis_auth` is unavailable is a resilience design, not a bypass. Fallback events are not written to the audit log (documented forensic trade-off; not a remediable security gap).

### 36.6.3 Token Role Definitions (★ Updated April 3, 2026 — OI-36-C CLOSED)

| Token type | Role granted | Scope | Notes |
|---|---|---|---|
| `carrie_admin` bearer token | `carrie_admin` | All routes including `/constitutional/*`, `/admin/*` | Elevated privilege — Redis-validated only. No env bypass. |
| `hayden_test` bearer token | `hayden_test` | `/chat`, `/health`, standard routes | Non-privileged. `403` on admin routes. |
| `"internal"` literal | `internal` | Proxy routes only (lines 758/857 retain `token_type` exemption) | **Blocked from `/chat` and `/memory`.** Inter-container calls only. |

> ★ **OI-36-C remediation summary — all five bypass paths removed:**
>
> | Bypass | Action |
> |---|---|
> | `JARVIS_API_KEY` env default (×2 locations in gateway) | Removed |
> | Constitutional proxy inline auth block | Removed |
> | `/auth/token` env bypass | Removed |
> | `"internal"` token type → `role: carrie_admin` | Downgraded to `role: internal` |
> | `_check_role` `token_type` exemption from privileged routes | Removed |
>
> The only remaining `token_type` exemption is the proxy-route exemption at lines 758/857 for `"internal"` — the legitimate inter-container service call path with `role="internal"`, blocked from community-facing routes.

### 36.6.4 Responsibilities of `jarvis_token_service.py`

1. **Issue tokens** — write `redteam:token:<token>` keys to Redis host port 6380.
2. **Validate tokens** — trigger validation through `jarvis_auth:8055/validate` with Redis fallback.
3. **Revoke tokens** — delete or mark `"active": false` on a key.
4. **List active tokens** — enumerate `redteam:token:*` keys for audit purposes.

No other service writes to the `redteam:token:*` keyspace.

---

## 36.7 Production Token Classes (★ April 3, 2026)

Two external-facing token classes are active in production.

### 36.7.1 `carrie_admin`

| Field | Value |
|---|---|
| Role | `carrie_admin` |
| Token count | **2 tokens** |
| Owner | Carrie Kidd (Mamma Kidd) |
| Intended use | Full administrative access; all routes; audit and governance operations |
| Redis keys | `redteam:token:<token_A>`, `redteam:token:<token_B>` |

The `carrie_admin` role is the highest-privilege class. Routes gated on `carrie_admin` include `/constitutional/audit`, all `/constitutional/*` routes, and `/admin/*`. ★ All `carrie_admin` gate decisions are durably logged at `jarvis-memory:8056`. ★ `carrie_admin` is no longer grantable via any bypass path (OI-36-C CLOSED April 3).

### 36.7.2 `hayden_test`

| Field | Value |
|---|---|
| Role | `hayden_test` |
| Token count | **2 tokens** |
| Owner | Hayden (test user) |
| Intended use | Validated testing of standard chat routes; scoped to non-administrative paths |
| Redis keys | `redteam:token:<token_C>`, `redteam:token:<token_D>` |

Attempting to access `carrie_admin`-only routes with a `hayden_test` token now correctly returns `403 Forbidden` (OI-36-A, OI-36-B CLOSED).

### 36.7.3 Token Count Summary

| Class | Role | Tokens in Production |
|---|---|---|
| `carrie_admin` | `carrie_admin` | 2 |
| `hayden_test` | `hayden_test` | 2 |
| **Total** | | **4** |

---

## 36.8 Oversight and Rules for Identity Use

Identity and registration mechanisms are constrained by explicit rules:

- **Least privilege** — registration grants only the access needed for a role's responsibilities. `"internal"` token type is blocked from community-facing routes and grants no elevated privilege.
- **No secret bypasses** — as of April 3, all five bypass paths identified in OI-36-C are removed. No environment variable, hardcoded literal, or token-type exemption can grant `carrie_admin` role outside Redis-validated token lookup (plus `jarvis_auth:8055` audit).
- **Retrieval-backed truth** — as of April 3, identity-adjacent truth claims are validated against live GIS RAG (10 hits confirmed, `JUDGE_TRUTH_URL` wired) and spiritual RAG (3 results confirmed) retrieval. Truth verdicts carry retrieval evidence as provenance.
- **Transparency and auditability** — all identity-related decisions are logged with references to PostgreSQL records and GBIM beliefs (★ `confidence_decay` metadata). ★ Token validation events flow through `jarvis_auth:8055` with full audit trail. ★ Both PostgreSQL connections visible in constitutional guardian `/health` (OI-37-B CLOSED).
- **Alignment with local partners** — registration rules are co-designed with Harmony for Hope and reflect local norms grounded in PostgreSQL `gisdb` (★ 91 GB PostGIS, 501 tables, 993 ZCTA centroids — ZIP-code-level alignment with service areas).

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

# Issue a token manually (emergency only — prefer jarvis_token_service.py)
redis-cli -p 6380 SET "redteam:token:<token_value>" \
  '{"token":"<token_value>","role":"hayden_test","owner":"hayden","active":true}'

# Verify Redis async job status key (must be 'complete' not 'done'):
redis-cli -p 6380 KEYS "job:*" | head -5

# ★ Verify jarvis-redis is Up:
docker inspect jarvis-redis --format '{{.State.Status}}'
docker port jarvis-redis 6379/tcp
# Expected: 127.0.0.1:6380

# ★ Verify rag_grounded_v2 services are Up (OI-37-C CLOSED):
docker inspect jarvis-gis-rag --format '{{.State.Status}}'
docker inspect jarvis-spiritual-rag --format '{{.State.Status}}'
# Expected: running (both)

# ★ Verify constitutional guardian PostgreSQL health (OI-37-B CLOSED):
curl -s http://localhost:8091/health | python3 -m json.tool
# Expected: postgresql_gbim_connection: "connected", postgresql_geodb_connection: "connected"
```

---

## 36.10 Auth Boundary Test Results

### March 22, 2026 Baseline (Pre-Enforcement)

Auth boundary tests executed March 22, 2026. Results committed to `msjarvis-public-docs/docs/contract/SESSION-2026-03-22.md` (commit `d966351`) — the **pre-enforcement regression baseline** for Chapter 40 (System Audit) and Chapter 41 (Test Harness).

| Test | Expected | Observed March 22 | Status |
|---|---|---|---|
| No token on `/chat` | 401 | 200 | ⚠️ Not enforced |
| Bad token on `/chat` | 401 | 200 | ⚠️ Not enforced |
| `hayden_test` on `/constitutional-audit` | 403 | 404 | ⚠️ Endpoint missing |
| `carrie_admin` on `/constitutional-audit` | 200 | 404 | ⚠️ Endpoint missing |

### ★ April 3, 2026 — Post-Remediation Results (All OIs CLOSED)

| Test | Expected | Observed April 3 | Status |
|---|---|---|---|
| No token on `/chat` | 401 | 401 | ✅ Enforced |
| Bad token on `/chat` | 401 | 401 | ✅ Enforced |
| `hayden_test` on `/constitutional/audit` | 403 | 403 | ✅ Enforced |
| `carrie_admin` on `/constitutional/audit` | 200 | 200 | ✅ Enforced |
| `carrie_admin` — `auth_source` field | `jarvis_auth` | `jarvis_auth` | ✅ Confirmed |

5/5 boundary tests pass. Token enforcement active. `auth_source: jarvis_auth` confirmed in live response.

> **Cross-chapter reference:** SESSION-2026-03-22.md (commit `d966351`) must be referenced in Chapter 40 (System Audit) and Chapter 41 (Test Harness) as the pre-enforcement baseline. The April 3 five-pass result is the enforcement-active baseline.

---

## 36.11 Open Items (★ April 3, 2026 — ALL CLOSED)

### ✅ OI-36-A — Token Validation Middleware — CLOSED April 3

**Resolution:** Token validation middleware wired into gateway port 8050. 5/5 boundary tests pass. Gateway validates bearer tokens via `jarvis_auth:8055/validate` with Redis direct fallback.

### ✅ OI-36-B — Role-Based Route Restriction — CLOSED April 3

**Resolution:** `carrie_admin` added to second `ROUTE_ROLES` table (line 548). Both tables now consistent. `403 Forbidden` returned for insufficient role. Verified in auth boundary tests.

### ✅ OI-36-C — All Bypass Paths Removed — CLOSED April 3

| Bypass | Action |
|---|---|
| `JARVIS_API_KEY` env default (×2 locations in gateway) | Removed |
| Constitutional proxy inline auth block | Removed |
| `/auth/token` env bypass | Removed |
| `"internal"` token type → `role: carrie_admin` | Downgraded to `role: internal` |
| `_check_role` `token_type` exemption from privileged routes | Removed |

**Legitimately retained:** `"internal"` literal token with `role="internal"` — scoped to inter-container proxy calls only, blocked from `/chat` and `/memory`, proxy-route `token_type` exemption at lines 758/857. Redis direct fallback — resilience design.

### ✅ OI-36-D — Gateway Wired to `jarvis_auth:8055` — CLOSED April 3

**Resolution:** Gateway POSTs `Authorization: Bearer` to `host.docker.internal:8055/validate` before Redis fallback. `auth_source: jarvis_auth` confirmed in live response.

### ✅ OI-37-A — Constitutional Proxy Active — CLOSED April 3

**Resolution:** Constitutional proxy confirmed active. Dead code comment only — no functional change required.

### ✅ OI-37-B — Constitutional Guardian PostgreSQL `/health` Fields — CLOSED April 3

**Resolution:** Both PostgreSQL connections now reachable in `/health` — `msjarvis:5433` (GBIM) and `msjarvisgis` (GeoDB) confirmed reachable; `/health` returns `postgresql_gbim_connection` and `postgresql_geodb_connection` liveness fields.

### ✅ OI-37-C — `rag_grounded_v2` Truth Verification Active — CLOSED April 3

| Item | Fix | Verified |
|---|---|---|
| OI-37-C spiritual-rag | `SearchRequest(BaseModel)` body model + volume mount | ✅ `truth_score=1.0`, 3 results |
| OI-37-C gis-rag | Volume mount + `JUDGE_TRUTH_URL` env | ✅ `truth_score=1.0`, 10 hits |
| `services/Dockerfile.spiritual_rag` | Restored from `services-safe/` | ✅ In `services/` |
| `services/Dockerfile.gis_raf` | Written from `pip freeze` | ✅ In `services/` |

**Ch 38 path:** Add `build:` stanzas to `docker-compose.yml` for both services; run `docker compose build` to produce clean images; volume mount workarounds are no longer needed after that point.

---

## 36.12 Current Status and Future Work

As of ★ April 3, 2026, identity and registration are fully implemented, tested, and enforced end-to-end. Container baseline is 101/101 Up (zero Restarting, zero Exited). GPU inference active (RTX 4070); end-to-end pipeline: 99–107 seconds (three confirmed runs March 22, 2026: 99.6s, 105.9s, 106.5s). **Public URL confirmed live: [https://egeria.mountainshares.us](https://egeria.mountainshares.us).** This URL must be cross-referenced from `msjarvis-public-docs/README.md` and the thesis overview index.

**Preflight gate ★ April 3:** 22 PASS / 0 FAIL / 1 WARN (intentional — `local_resources 48/55`, Phase 2 data task). Prior baseline: 20 PASS / 0 FAIL (March 22, 2026).

**★ April 3, 2026 — all OIs closed this session:**

- OI-36-A ✅ — token validation middleware wired; 5/5 boundary tests pass.
- OI-36-B ✅ — both `ROUTE_ROLES` tables aligned; `403` enforced.
- OI-36-C ✅ — all five bypass paths removed; `"internal"` token downgraded and scoped.
- OI-36-D ✅ — gateway wired to `jarvis_auth:8055`; audit trail active.
- OI-37-A ✅ — constitutional proxy confirmed active; dead code comment only.
- OI-37-B ✅ — both PostgreSQL connections reachable in `/health`.
- OI-37-C ✅ — `rag_grounded_v2` active; both RAG services `truth_score=1.0`; Dockerfiles written.

**★ March 28, 2026 — prior session milestones:**

- `jarvis-memory:8056` durable BBB + identity audit trail secured.
- `msjarvis:5433` restored — 5,416,521 GBIM entities with `confidence_decay` metadata.
- `msjarvisgis` confirmed — 91 GB PostGIS, 501 tables, 993 ZCTA centroids.
- ChromaDB full audit — 40 active collections / 6,675,442 total vectors; `psychological_rag` restored to 968 docs.
- 96/96 containers Up (superseded by 101/101 April 3).

**Future work — forwarded to Ch 38:**

- Add `build:` stanzas to `docker-compose.yml` for `jarvis-gis-rag` and `jarvis-spiritual-rag`; run `docker compose build` to produce clean images removing volume mount workarounds permanently.
- Automated decay-aware GBIM audit flagging for identity validation queries.
- More granular role-based access control tied to spatial and institutional features in PostgreSQL `gisdb` (★ 501 tables, 993 ZCTA centroids — ready for ZIP-code-level role scoping).
- Automated promotion pipelines for moving patterns from background memory into identity-level entries.
- Public URL [https://egeria.mountainshares.us](https://egeria.mountainshares.us) added to thesis README and overview index (outstanding documentation task).

---

## 36.13 Status Table (★ April 3, 2026 SEALED)

| Component | Role in identity and registration | Status (★ April 3, 2026) |
|---|---|---|
| `normalize_identity` (`jarvis-main-brain`, port 8050) | Rewrites all responses into the Ms. Jarvis persona; enforces canonical identity statements. | ✅ Up 101/101. Stability re-confirmed April 2–3. |
| `TruthValidator` | Encodes canonical facts; produces `truth_verdict` on every `UltimateResponse`. ★ Backed by `rag_grounded_v2` retrieval + `msjarvis:5433` GBIM with `confidence_decay` metadata. | ✅ Implemented. Confirmed live 2026-02-15. ★ `rag_grounded_v2` active April 3. |
| `jarvis-i-containers` (port 8015) | Produces `root-self` ego entries and ego-boundary records in `identity_layers` and `consciousness_layers`. | ✅ Up 101/101. Confirmed active 2026-02-15. |
| BBB six-filter pipeline (`jarvis-blood-brain-barrier`, port 8016) | EthicalFilter ★ (0% FP, April 2); SpiritualFilter; SafetyMonitor ★ (`safety_score=1.0`, April 3); ThreatDetection; steganography_filter; truth_verification ★ (`rag_grounded_v2`, OI-37-C CLOSED). Phase 4.5 log+passthrough. ★ All gate decisions → `jarvis-memory:8056`. | ✅ Up 101/101. |
| `jarvis-gis-rag` (port 8004) | Geospatial RAG for `rag_grounded_v2`. `truth_score=1.0`, 10 hits. Volume mount + `JUDGE_TRUTH_URL` env fixed. `Dockerfile.gis_raf` in `services/`. | ✅ OI-37-C CLOSED. April 3. Ready for clean `build:` in Ch 38. |
| `jarvis-spiritual-rag` (port 8005) | Spiritual/community values RAG for `rag_grounded_v2`. `truth_score=1.0`, 3 results. `SearchRequest(BaseModel)` + volume mount fixed. `Dockerfile.spiritual_rag` in `services/`. | ✅ OI-37-C CLOSED. April 3. Ready for clean `build:` in Ch 38. |
| `jarvis-constitutional-guardian` (port 8091) | Enforces constitutional principles; first gate before BBB and gateway; `/constitutional/*` proxied with `carrie_admin` enforcement; persistent `.jsonl` audit + `jarvis-memory:8056`. OI-37-A: proxy confirmed active. OI-37-B: both PG connections in `/health`. | ✅ Up 101/101. OI-37-A ✅ OI-37-B ✅ CLOSED April 3. |
| ★ `jarvis-memory:8056` durable audit trail | Persistently logs BBB gate decisions, identity enforcement events, token validation events, `rag_grounded_v2` truth verdicts, and constitutional gate decisions. Survives container restarts. | ★ Secured March 28. Extended April 3. |
| LM Synthesizer identity guard — Layer 1 (`IDENTITY_GUARD` constant) | Documents ID-03 failure mode. NOT injected into f-string. Retained as permanent failure-mode record. | ✅ Documented. Not functional by design. `jarvis-lm-synthesizer:8001` Up 101/101. |
| LM Synthesizer identity guard — Layer 2 (IDENTITY RULES in f-string) | Working fix — identity rules injected into prompt f-string. | ✅ Active. Stability re-confirmed April 2–3. |
| LM Synthesizer identity guard — Layer 3 (meta-commentary prohibition) | Prevents model name leakage, synthesis disclosure, hedging language. Commit `211056e6`. | ✅ Active. Stability re-confirmed April 2–3. |
| `jarvis_token_service.py` — production token registry | Issues, validates, revokes bearer tokens; `redteam:token:<token>` in `jarvis-redis` host port 6380. 4 tokens active across 2 classes. | ✅ `jarvis-redis` Up 101/101. |
| Gateway token validation middleware (port 8050) | Enforces `401`; POSTs to `jarvis_auth:8055/validate` before Redis fallback; `auth_source: jarvis_auth` confirmed. | ✅ OI-36-A CLOSED. 5/5 boundary tests pass. |
| Role-based route restriction (`403`) | Returns `403` for insufficient role. Both `ROUTE_ROLES` tables aligned. | ✅ OI-36-B CLOSED. April 3. |
| All bypass path removals | Five paths removed (env default ×2, proxy inline, `/auth/token` bypass, `"internal"` downgrade, `_check_role` exemption). | ✅ OI-36-C CLOSED. April 3. |
| `jarvis_auth` audit wiring | Gateway POSTs to `jarvis_auth:8055/validate`; validation events in audit trail. | ✅ OI-36-D CLOSED. April 3. |
| `"internal"` literal token — retained | `role="internal"` — inter-container proxy calls only. Blocked from `/chat` and `/memory`. Lines 758/857 exemption retained (legitimate design). | ✅ Scoped correctly. Not a bypass. |
| Redis fallback — retained | Direct Redis `GET` fallback when `jarvis_auth` unavailable. Resilience design. Fallback not in audit log (documented trade-off). | ✅ Retained. Acceptable. |
| Registration roles and audit tables | Tie higher-impact actions to real people and institutions; PostgreSQL-backed audit trails; `confidence_decay` GBIM metadata; `jarvis-memory:8056` durable logging; `rag_grounded_v2` retrieval evidence. | ⚙️ Conceptually implemented; automated promotion and cross-path analytics are future work. |

---

*Chapter 36 — Identity and Registration*  
*Ms. Egeria Jarvis Steward System — Harmony for Hope, Inc.*  
*Pax, West Virginia*  
*SEALED: ★ April 3, 2026 — All Chapter 36 and Ch 37 cross-chapter OIs Closed*  
*OI-36-A ✅ OI-36-B ✅ OI-36-C ✅ OI-36-D ✅ OI-37-A ✅ OI-37-B ✅ OI-37-C ✅*  
*Ch 38: add build: stanzas for jarvis-gis-rag and jarvis-spiritual-rag to cut clean images.*
