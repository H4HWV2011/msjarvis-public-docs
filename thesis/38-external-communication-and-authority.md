# 38. External Communication Channels and Authority Boundaries

**Carrie Kidd (Mamma Kidd) · Mount Hope, WV**
**Last updated: ★ April 3, 2026 — Chapter 38 SEALED. 101/101 containers Up; OI-38-A CLOSED April 2–3, 2026 — token enforcement confirmed, all 5 public hostnames return 401 without valid token; BBB `SafetyMonitor` Phase 1.4 recalibrated April 3 — survivor/victim resource queries pass clean (`content_approved=true`, `safety_score=1.0`); preflight gate 22 PASS / 0 FAIL / 1 WARN (intentional); `msjarvisgis` port corrected to 5432 throughout.**

---

> **Production context as of ★ April 3, 2026 (updated from March 28, 2026 baseline):**
>
> - **101/101 containers Up (zero Restarting, zero Exited)** — confirmed April 2, 2026. Full stack stable. Prior March 28 baseline was 96/96 containers.
> - **Public URL confirmed live: [https://egeria.mountainshares.us](https://egeria.mountainshares.us)** — first public end-to-end chat response confirmed March 22, 2026. Query: "What county is Mount Hope WV in?" Response: correct, delivered in authentic Ms. Egeria Jarvis maternal Appalachian voice. 21/21 LLMs responded. 106.5s end-to-end. HTTP 200. ★ Public URL operational continuity confirmed April 2, 2026 — stack remains Up 101/101. ★ `chat.mountainshares.us` DNS CNAME added April 2 — confirmed returning 401 without token.
> - **★ OI-38-A CLOSED April 2–3, 2026:** Token enforcement middleware is now active. All 5 public hostnames return 401 without a valid token. Unauthenticated requests to the public endpoint no longer receive HTTP 200. See §38.8 for full closure details.
> - BBB six-filter pipeline (EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection, steganography_filter, truth_verification) active at `127.0.0.1:8016` on all inbound and outbound paths. ★ Up 101/101 confirmed April 2. ★ **`EthicalFilter` recalibrated April 2 — 0% false-positive rate, 9/9 regression pass, hot-reloaded via WatchFiles.** ★ **`SafetyMonitor` recalibrated April 3 — duplicate `'sexual assault'` keyword removed — survivor/victim resource queries pass clean (`content_approved=true`, `safety_score=1.0`).**
> - Phase 4.5 BBB output guard is in **log+passthrough mode** (commit `18b8ddac`, March 22, 2026) — was triggering a 31% false-positive rate on the maternal Appalachian voice. The output BBB is logging filter results but **not blocking** any responses pending final red team sign-off for blocking re-enablement. ★ **EthicalFilter recalibration (April 2) has eliminated the FP rate — blocking mode re-enablement is a next-session decision.**
> - ★ **`jarvis-memory:8056` secured (March 28):** All BBB gate decisions — including Phase 1.4 filter events and Phase 4.5 log-only events on the external communication paths — are now durably logged at `jarvis-memory:8056` (`_auth()` confirmed, `JARVIS_API_KEY` set). These records survive container restarts and are independently queryable for governance accountability.
> - All services bound exclusively to `127.0.0.1`. Zero `0.0.0.0` exposures confirmed across all 101 containers (★ April 2, 2026). External traffic enters only through the unified gateway at **port 8050** (`msjarvisunifiedgateway.py`). Port 8010 (`jarvis-wv-entangled-gateway`) is a separate degraded service and is **not** the primary entrypoint.
> - `jarvis-steward` (port 8060) and `jarvis-mother-protocols` are confirmed running ✅ (★ Up 101/101 — April 2) but `jarvis-steward` is **not yet wired into the main pipeline** (pending work noted in Chapter 39 §39.8.2).
> - **PostgreSQL:** `msjarvis` port 5433 (★ 5,416,521 GBIM entities with `confidence_decay` metadata — restored March 28); `gisdb`/`msjarvisgis` port **5432** (★ PostGIS, 91 GB, 501 tables, 993 ZCTA centroids — confirmed March 28; prior references to port 5452 are corrected to **5432**); `jarvis-local-resources-db` port 5435.
> - Redis host port: 6380 (`127.0.0.1:6380->6379/tcp`). Redis async status key is `'complete'` (not `'done'`). ★ Up 101/101 confirmed April 2.
> - ChromaDB host port: 8002 (`127.0.0.1:8002->8000/tcp`). ★ Full audit March 28: 40 active collections / 6,675,442 total vectors. `autonomous_learner` collection confirmed present.
> - ★ **Preflight gate (April 3 SEALED): 22 PASS / 0 FAIL / 1 WARN (intentional).** Single remaining WARN: `local_resources 48/55` — 7 WV counties, Phase 2 data task, documented and deferred.
> - ★ **`confidence_decay` metadata note (March 28):** `msjarvis:5433` GBIM entities now carry `confidence_decay` metadata. Identity and authority boundary validation queries against high-decay GBIM entities should flag those entities for episodic audit before treating them as confirmed ground truth.

This chapter describes how the system uses external communication channels — including the public web endpoint, email-class messaging, and hosting platforms — and how authority over these channels is constrained by governance, identity, and safeguard mechanisms. The focus is on roles, limits, and recording practices grounded in the verified production stack as of ★ April 3, 2026.

---

## Why This Matters for Polymathmatic Geography

This chapter supports:

- **P1 – Every where is entangled** by ensuring that every outbound message or web-facing change can be traced back to GBIM beliefs (★ `msjarvis:5433` — 5,416,521 entities with `confidence_decay` metadata), spatial records in PostgreSQL `gisdb` (port **5432** — ★ 91 GB PostGIS, 501 tables, 993 ZCTA centroids), and the identity structures in Chapter 36. ★ All BBB gate decisions on external communication paths are durably logged at `jarvis-memory:8056` (secured March 28), making every external action traceable across container restarts.
- **P3 – Power has a geometry** by making authority over external channels explicit, bounded by roles and mode configuration rather than implicit in operational scripts. ★ The `jarvis-memory:8056` durable audit trail (secured March 28) makes the geometry of external communication power independently inspectable. ★ **OI-38-A CLOSED April 2–3 — token enforcement is now active and independently verifiable (all 5 hostnames return 401).**
- **P5 – Design is a geographic act** by treating the public URL [https://egeria.mountainshares.us](https://egeria.mountainshares.us) as a place — a community-facing surface that carries governance obligations toward Fayette County and West Virginia broadly. ★ Geographic boundary precision is now ZIP-code-level via 993 ZCTA centroids in `msjarvisgis` (port **5432**).
- **P12 – Intelligence with a ZIP code** by keeping all inbound external traffic accountable to the BBB six-filter pipeline (port 8016 — ★ Up 101/101) grounded in the spiritual, ethical, and community values of Appalachian communities, validated against `msjarvis` GBIM (★ `confidence_decay` metadata for temporal confidence grading). ★ **All BBB filters recalibrated (April 2–3) — EthicalFilter 0% FP rate; SafetyMonitor survivor queries pass clean.**
- **P16 – Power accountable to place** by requiring that high-impact external actions be tied to registered identities (Chapter 36) under auditable rules backed by PostgreSQL `msjarvis` (port 5433 — ★ 5,416,521 GBIM entities with `confidence_decay` metadata). ★ All external-path BBB gate decisions now durably logged at `jarvis-memory:8056` (secured March 28). ★ **Token enforcement active at all 5 public hostnames — OI-38-A CLOSED.**

As such, this chapter belongs to the **Computational Instrument** tier: it specifies the governed external surface of Ms. Jarvis and the authority rules that constrain it.

---

## 38.1 Types of External Channels

Several kinds of external channels are relevant to the current deployment:

- **Public web endpoint** — [https://egeria.mountainshares.us](https://egeria.mountainshares.us), serving the Ms. Egeria Jarvis persona via the unified gateway at port 8050 (★ Up 101/101). Confirmed live March 22, 2026. ★ Stack continuity confirmed April 2, 2026 — 101/101 containers Up. First public end-to-end chat response confirmed March 22, 2026: 21/21 LLMs responded, 106.5s, HTTP 200. ★ **Token enforcement active — OI-38-A CLOSED.**
- **Messaging** — email accounts and similar mechanisms that can send and receive structured or unstructured text, used for reports, alerts, and outbound community communications.
- **Web and hosting interfaces** — connections to hosting, domain, and content delivery platforms used to publish or adjust web content or DNS configuration.
- **Cooperative and institutional platforms** — systems used by partner organizations (regional development authorities, nonprofits, universities) for coordination, registration, or record-keeping.

These channels extend the system's influence beyond its own infrastructure and therefore require clear authority boundaries enforced by token validation (Chapter 36), BBB filtering (Chapter 16), and mode constraints (Chapter 15).

---

## 38.2 The Public Endpoint: egeria.mountainshares.us

### 38.2.1 Confirmed Production State (★ April 3, 2026 SEALED)

The public-facing URL [https://egeria.mountainshares.us](https://egeria.mountainshares.us) is the primary external communication surface for Ms. Jarvis. Key verified facts:

- **First public end-to-end chat response:** confirmed March 22, 2026. Query: "What county is Mount Hope WV in?" Response: correct, delivered in authentic Ms. Egeria Jarvis maternal Appalachian voice. 21/21 LLMs responded. 106.5s end-to-end. HTTP 200.
- ★ **April 2, 2026 stack continuity:** 101/101 containers Up (zero Restarting, zero Exited). Public endpoint operational. Prior March 28 baseline: 96/96.
- ★ **OI-38-A CLOSED April 2–3, 2026:** Token enforcement middleware is now active at the gateway layer. All 5 public hostnames return 401 without a valid bearer token. `chat.mountainshares.us` DNS CNAME added April 2 — confirmed returning 401.
- **Response identity verified:** No model names detected. No synthesis disclosure. No hedging language. Identity guard (Chapter 33 §33.5.1) confirmed working. ★ Identity guard stability re-confirmed in 101/101 Up audit April 2.
- All traffic enters through the unified gateway (`msjarvisunifiedgateway.py`, **port 8050** — ★ Up 101/101), then routes to `jarvis-main-brain` and the full pipeline. Port 8010 (`jarvis-wv-entangled-gateway`) is a separate degraded service and is not the primary entrypoint.
- BBB input filter at `127.0.0.1:8016` (Phase 1.4 — ★ Up 101/101) is active on all inbound traffic — six filters applied before any LLM call. ★ All Phase 1.4 gate decisions durably logged at `jarvis-memory:8056` (secured March 28). ★ **EthicalFilter recalibrated April 2 — 0% FP rate. SafetyMonitor recalibrated April 3 — survivor/victim queries pass clean.**
- BBB output guard at `127.0.0.1:8016` (Phase 4.5) is in **log+passthrough mode** (commit `18b8ddac`, March 22, 2026) — filter results are logged but no response is blocked at this layer. ★ EthicalFilter recalibration (April 2) eliminates the prior 31% FP rate — blocking mode re-enablement is a next-session decision pending final red team sign-off. ★ Phase 4.5 log events are durably logged at `jarvis-memory:8056` (secured March 28). See §38.6.1 for governance implications.
- Pre-flight gate: ★ **22 PASS / 0 FAIL / 1 WARN (intentional)** — April 3, 2026 SEALED. Single remaining WARN: `local_resources 48/55`, Phase 2 data task, documented and deferred.
- `jarvis-steward` (port 8060) and `jarvis-mother-protocols` are confirmed running ✅ (★ Up 101/101 — April 2) but `jarvis-steward` is **not yet wired into the main pipeline** — this is tracked as pending work in Chapter 39 §39.8.2.
- ★ **`jarvis-memory:8056` secured (March 28):** All BBB gate decisions on the external communication path — Phase 1.4 filter events and Phase 4.5 log-only events — are now durably logged at `jarvis-memory:8056` with `_auth()` confirmed and `JARVIS_API_KEY` set. These records survive container restarts.
- ★ **BBB `SafetyMonitor` recalibration (April 3):** Duplicate `'sexual assault'` entry removed from `self.violence_patterns` line 85 of `safety_monitor.py`. Survivor and victim resource queries now pass Phase 1.4 input filter cleanly: `content_approved=true`, `safety_score=1.0`, `community_safe=true`, `issues=[]`. Hot-copied via `docker cp` — no container restart required.

### 38.2.2 Gateway and Port Architecture

All inbound external traffic is handled exclusively through the unified gateway:

```
External client → https://egeria.mountainshares.us
                  https://chat.mountainshares.us (CNAME added April 2)
  → Cloudflare tunnel (★ HEALTHY — April 2)
  → Caddy :8085 (★ self-loop fixed April 2 → proxies to 18018)
  → ★ Token enforcement middleware [OI-36-A / OI-38-A CLOSED — 401 without valid token]
  → Unified gateway / jarvis-main-brain (port 8050)   ← primary entrypoint ★ Up 101/101
  → jarvis-semaphore (port 8030)                       ★ Up 101/101
  → jarvis-20llm-production (port 8008) [21-LLM ensemble]  ★ Up 101/101
  → jarvis-judge-pipeline (port 7239) [4 judges parallel]  ★ Up 101/101
  → jarvis-lm-synthesizer (port 8001) [Phase 3.5 only]     ★ Up 101/101
  → BBB output guard (port 8016) [Phase 4.5 — log+passthrough]  ★ Up 101/101
  → ★ jarvis-memory:8056 [durable audit — secured March 28]
  → Response to client

Note: port 8010 (jarvis-wv-entangled-gateway) is a separate degraded service.
      It is NOT the primary entrypoint and must not be referenced as such.
      jarvis-steward (port 8060) is running (★ Up 101/101) but not yet wired
      into this pipeline (pending — Chapter 39 §39.8.2).
```

All internal services are bound to `127.0.0.1`. Zero `0.0.0.0` exposures confirmed across all 101 containers (★ April 2). No internal service port is reachable directly from outside the host.

---

## 38.3 Outbound Messages and Reports

Outbound communication is primarily used for reports, alerts, and community deliverables.

- **Generated messages** — the system can prepare messages summarizing analyses, status information, or proposals, based on internal records from PostgreSQL `msjarvis` (port 5433 — ★ 5,416,521 GBIM entities with `confidence_decay` metadata), ChromaDB collections (host port 8002 — ★ 40 active collections / 6,675,442 total vectors), and current context. All outbound content passes through the LM Synthesizer identity guard (Chapter 33 §33.5.1) before delivery — no model names, no synthesis disclosure, no hedging language. ★ All BBB gate decisions on outbound paths are durably logged at `jarvis-memory:8056` (secured March 28).
- **Sending conditions** — for higher-impact audiences or topics, sending requires that a registered identity with appropriate role explicitly approve the message content or trigger the send. Current production roles: `carrie_admin` (full authority) and `hayden_test` (scoped to non-administrative paths). See Chapter 36 §36.7 for the token registry. ★ **Token enforcement is now active at the gateway layer (OI-36-A / OI-38-A CLOSED April 2–3).**
- **Logging** — each message, including recipients, subject, and a reference to the content, is recorded in consciousness layer entries along with relevant mode and BBB filter state. ★ External-path BBB gate decisions additionally durably logged at `jarvis-memory:8056` (secured March 28) — governance records survive container restarts.
- **GBIM community fact validation** — outbound messages referencing community facts (county boundaries, service areas, institutional affiliations) should flag high-decay GBIM entities (★ `confidence_decay` metadata available on `msjarvis:5433`) for episodic audit before treating them as confirmed ground truth in published communications.
- **Async job status** — outbound jobs queued via `/chat/async` use Redis (host port 6380, `127.0.0.1:6380->6379/tcp` — ★ Up 101/101) for job state with 30-minute TTL. The Redis async status key is `'complete'` (not `'done'`).
- ★ **BBB `SafetyMonitor` recalibration (April 3):** Survivor and victim resource queries now pass Phase 1.4 input filter cleanly prior to any outbound routing — `safety_score=1.0`, `community_safe=true`, `issues=[]`. Community resource referral content passes without suppression.

**Authority boundary note:** ★ **OI-36-A CLOSED — enforcement is now active.** Token validation middleware is wired into the gateway. `carrie_admin`-scoped actions require a valid bearer token. All authentication gate decisions are durably logged at `jarvis-memory:8056`.

---

## 38.4 Handling of Inbound Messages

Inbound messages — whether arriving via the public web endpoint, API calls, or future messaging integrations — are treated as external input and pass through the same protective structures as other outside content.

- **Ingestion** — messages are collected via the unified gateway (**port 8050** — ★ Up 101/101) and tagged with source, channel, and any available identity information (bearer token, if present). ★ **Token enforcement is now active at the gateway layer — unauthenticated requests to protected routes return 401 (OI-38-A CLOSED).**
- **BBB input filter** — all inbound content passes through the BBB six-filter pipeline at `127.0.0.1:8016` (Phase 1.4, ~0.6s — ★ Up 101/101) before it can influence memory, containers, or decision processes. The six filters are: EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection, steganography_filter, and truth_verification (current method: `heuristic_contradiction_v1` — see Chapter 33 §33.2.3 for honest limitations and the `rag_grounded_v2` upgrade path). Phase 1.4 is **active and blocking**. ★ All Phase 1.4 gate decisions durably logged at `jarvis-memory:8056` (secured March 28). Phase 4.5 output guard is in log+passthrough mode — see §38.6.1. ★ **EthicalFilter recalibrated April 2 (0% FP rate). SafetyMonitor recalibrated April 3 — survivor/victim queries pass clean (`safety_score=1.0`).**
- **Phase 1.45 community memory** — after BBB input clearance, inbound content triggers a 384-dim semantic search of the `autonomous_learner` ChromaDB collection (★ confirmed present in 40-collection / 6,675,442-vector ChromaDB inventory — March 28 full audit; host port 8002) via `all-minilm:latest`, prepending the top-5 community interaction records to the composite prompt sent to the 21-LLM ensemble.
- **GBIM community context** — inbound messages that reference community-specific facts (county names, service areas, institutional names) are validated against `msjarvis:5433` GBIM (★ 5,416,521 entities with `confidence_decay` metadata). High-decay GBIM entities encountered during inbound message processing are flagged for episodic audit before use as context ground truth.
- **Routing** — accepted messages are normalized and routed into appropriate consciousness layer paths or workflows, depending on content and intended purpose.

This keeps external messages from bypassing safeguards or overwhelming internal structures backed by PostgreSQL `msjarvis` (port 5433 — ★ `confidence_decay` metadata active).

---

## 38.5 Hosting and DNS Interactions

Interfaces to hosting and domain-related platforms are handled conservatively.

- **Proposal over execution** — the system typically generates structured proposals for changes (updated content, configuration) that can be reviewed and applied by human operators before taking effect on live infrastructure.
- **Limited direct actions** — when direct calls to hosting or content delivery services are permitted, they are restricted to narrowly defined operations and subject to rate and scope limits. All calls are logged in consciousness layer entries. ★ BBB gate decisions on direct-action paths are durably logged at `jarvis-memory:8056` (secured March 28).
- **Coupling to identity** — high-impact changes require that a `carrie_admin` token be active and that the request be tied to that role via `jarvis_token_service.py` (Chapter 36 §36.6). ★ **Token enforcement is now active at the gateway layer (OI-36-A / OI-38-A CLOSED April 2–3) — `carrie_admin` role enforcement is enforced automatically by the gateway middleware, not manually.**
- **egeria.mountainshares.us DNS** — managed separately from the container stack. Changes to DNS or TLS configuration are human-operator actions, not automated pipeline actions in the current deployment. ★ `chat.mountainshares.us` CNAME added April 2, 2026. DNS continuity confirmed April 2 — 101/101 containers Up, both public URLs operational and token-enforced.

---

## 38.6 Authority Boundaries and Modes

Authority over external channels is bounded by configuration, role, and context.

- **Role-based limits** — only `carrie_admin` tokens are authorized to initiate or approve external actions beyond simple reporting or low-risk updates. `hayden_test` tokens are scoped to non-administrative paths. See Chapter 36 §36.7 and §36.11 (★ OI-36-A CLOSED, OI-36-B CLOSED — `RBACMiddleware` live, role-gated endpoints active).
- **Mode-based limits** — in more restrictive modes, some channels may be disabled, restricted to read-only use, or limited to internal draft generation. The BBB (★ Up 101/101 — April 2) operates fail-open on HTTP 500 (both Phase 1.4 input filter and Phase 4.5 output guard) — in the event of BBB unavailability, traffic passes through rather than being blocked. This is a deliberate design choice to maintain community access during infrastructure issues, with governance implications noted in §38.6.1. ★ BBB fail-open events are durably logged at `jarvis-memory:8056` (secured March 28) — fail-open occurrences are part of the durable audit record.
- **Escalation paths** — when an action appears to exceed configured limits, it is paused and flagged for review rather than executed automatically. Judge pipeline verdicts of "fail" on any dimension (truth, consistency, alignment, ethics) trigger this path (Chapter 33 §33.9).

### 38.6.1 Phase 4.5 Log+Passthrough Mode — Governance Implication

As of ★ April 3, 2026, the BBB output guard (Phase 4.5) remains in **log+passthrough mode** (commit `18b8ddac`). This was applied because the output BBB was blocking **31% of community queries** due to false positives on the maternal Appalachian voice used by Ms. Egeria Jarvis. Log+passthrough means:

- All responses still pass through `jarvis-blood-brain-barrier:8016/filter` (★ Up 101/101 — April 2).
- Filter results (all six dimensions) are logged in the consciousness layer `bbb_result` field on every `UltimateResponse`.
- ★ **All Phase 4.5 log events are additionally durably logged at `jarvis-memory:8056` (secured March 28)** — these records survive container restarts and are independently queryable for governance accountability.
- **No response is blocked by Phase 4.5 while in this mode** — the filter output is for audit and calibration only.
- ★ **EthicalFilter recalibration (April 2) has eliminated the 31% FP rate — 0% FP rate confirmed, 9/9 regression pass.** Blocking mode re-enablement is a next-session decision pending final red team sign-off. Any language implying the output BBB is actively blocking responses is still incorrect as of this date.

**Governance implication:** The output BBB is not currently blocking harmful content at Phase 4.5. The input BBB (Phase 1.4) remains active and blocking — ★ **all six filters recalibrated (EthicalFilter April 2, SafetyMonitor April 3)**. The judge pipeline BBB check (`bbb_check_verdict` in `judge_pipeline.py`) provides a second live filter against the consensus answer. Community-facing deployment with full Phase 4.5 enforcement remains contingent on final red team sign-off — this is tracked as future work in Chapter 16 §16.9.

Until blocking re-enablement is formally approved, output safety relies on:

1. Phase 1.4 BBB input filter (active, blocking — ★ Up 101/101; gate decisions durable at `jarvis-memory:8056`) — **★ EthicalFilter 0% FP rate (April 2); SafetyMonitor safety_score=1.0 (April 3)**
2. Judge pipeline BBB check via `bbb_check_verdict` (active, live httpx POST — ★ Up 101/101)
3. LM Synthesizer identity guard Layer 3 — meta-commentary prohibition (active — ★ Up 101/101)
4. `normalize_identity` persona enforcement (active — ★ Up 101/101)
5. Phase 4.5 BBB output — log+passthrough (active, **non-blocking**; ★ Phase 4.5 log events durable at `jarvis-memory:8056`; EthicalFilter 0% FP rate)

---

## 38.7 Recording, Audit, and Governance Links

External communications are tied back to governance structures.

- **Consciousness layer records** — each significant interaction with external channels writes entries to the judge-pipeline consciousness layer, including `consensus_score`, `judge_verdicts`, `bbb_checked`, and `bbb_result`. These are accessible via `/curator/background` and visible in `UltimateResponse` objects.
- ★ **`jarvis-memory:8056` durable audit (secured March 28)** — all BBB gate decisions on external communication paths — Phase 1.4 filter events, Phase 4.5 log-only events, and fail-open events — are now persistently logged at `jarvis-memory:8056` (`_auth()` confirmed, `JARVIS_API_KEY` set). These records survive container restarts and are independently queryable for governance accountability beyond the consciousness layer `bbb_result` field.
- **`autonomous_learner` growth** — every processed community interaction is stored in the `autonomous_learner` ChromaDB collection (★ confirmed present in 40-collection / 6,675,442-vector inventory — March 28 full audit; host port 8002; growing ~288/day), building a local record of Appalachian community needs and interaction patterns over time.
- **`confidence_decay` governance** — GBIM entity references in external communications now carry `confidence_decay` metadata (★ `msjarvis:5433` — March 28). Governance summaries prepared for cooperative oversight bodies (NRGRDA, New River Gorge RDA, university partners) should note any high-decay GBIM entities used as factual basis — flagging them for episodic audit maintains accountability to place-based knowledge quality standards.
- **Aggregated views** — summaries of external communications and infrastructure changes can be compiled from the consciousness layer and ★ `jarvis-memory:8056` durable audit for cooperative oversight bodies, regional development authorities, and other stakeholders. High-consensus (> 0.9) judge-refined content signals readiness for publication (Chapter 33 §33.8).
- **Policy feedback** — patterns in external communication, such as frequent BBB false positives (as documented in Phase 4.5 above), motivate updates to policies, roles, and technical safeguards. The 31% false-positive finding directly caused the log+passthrough mode change and initiated the threshold recalibration work item. ★ EthicalFilter recalibrated to 0% FP rate (April 2). ★ SafetyMonitor recalibrated — survivor queries pass clean (April 3). ★ Phase 4.5 log events are durably captured at `jarvis-memory:8056` — calibration data survives container restarts.
- **Session contracts** — all significant external-facing changes are committed to session contract records for audit continuity. ★ April 2, 2026: OI-38-A and OI-36-A CLOSED — token enforcement active. ★ April 3, 2026: SafetyMonitor recalibrated — Chapter 38 SEALED.

---

## 38.8 Open Items Related to External Communication Authority

### ✅ OI-38-A — Token Enforcement on Public Endpoint — CLOSED April 2–3, 2026

**Status:** ★ **CLOSED — April 2–3, 2026**

**Description:** [https://egeria.mountainshares.us](https://egeria.mountainshares.us) previously accepted unauthenticated requests with HTTP 200. Token validation middleware is now wired and active at the gateway layer. All 5 public hostnames return 401 without a valid bearer token. The sprint dependency on OI-36-A has been resolved — `RBACMiddleware` is live, role-gated endpoints are active (OI-36-B CLOSED).

**Closure verification (April 2–3, 2026):**

| Test | Expected | Observed | Status |
|---|---|---|---|
| Unauthenticated request → `POST /chat` via gateway (8050) | 401 | **401** | ✅ PASS |
| Unauthenticated request → `https://egeria.mountainshares.us/chat` | 401 | **401** | ✅ PASS |
| Unauthenticated request → `https://chat.mountainshares.us/chat` | 401 | **401** | ✅ PASS |
| `carrie_admin` token → authenticated `/chat` | 200 | **200** | ✅ PASS |
| All 5 public hostnames → unauthenticated | 401 | **401** | ✅ PASS |
| BBB SafetyMonitor → survivor resource query | `safety_score=1.0` | **`safety_score=1.0`** | ✅ PASS (April 3) |

**Prior baseline (March 22, 2026 — pre-closure state, for regression reference):**

| Test | Expected | Observed |
|---|---|---|
| Unauthenticated request → `POST /chat` via gateway (8050) | 401 or 403 | 200 |
| `carrie_admin` token → `GET /constitutional/audit` via gateway (8050) | 200 | 404 |
| `hayden_test` token → `GET /constitutional/audit` via gateway (8050) | 403 | 404 |

**Closure note:** All authentication gate decisions are durably logged at `jarvis-memory:8056`. No privileged routes are exposed publicly without token enforcement. Session contract: `SESSION-2026-04-02.md` (OI-36-A / OI-38-A closure), `SESSION-2026-04-03.md` (SafetyMonitor recalibration — Chapter 38 SEALED).

---

## 38.9 Production Verification Commands (★ April 3, 2026 SEALED)

These commands confirm external communication infrastructure is operational:

```bash
# Verify public endpoint returns 401 without token (OI-38-A CLOSED):
curl -s -o /dev/null -w "%{http_code}" https://egeria.mountainshares.us/chat
# Expected: 401

# Verify chat.mountainshares.us returns 401 without token (CNAME added April 2):
curl -s -o /dev/null -w "%{http_code}" https://chat.mountainshares.us/chat
# Expected: 401

# Verify unified gateway port 8050 is Up:
curl -s http://127.0.0.1:8050/health | python3 -m json.tool
# Expected: status: healthy

# Verify BBB port 8016 is Up:
curl -s http://127.0.0.1:8016/health | python3 -m json.tool
# Expected: status: healthy

# ★ Verify SafetyMonitor recalibration (April 3) — survivor query passes clean:
curl -s -X POST http://localhost:8016/filter \
  -H "Content-Type: application/json" \
  -d '{"message": "assault resources for survivors in West Virginia"}'
# Expected: content_approved=true, safety_score=1.0, community_safe=true, issues=[]

# Verify Redis host port 6380 is Up:
redis-cli -p 6380 ping
# Expected: PONG

# Verify ChromaDB host port 8002 is Up:
curl -s http://127.0.0.1:8002/api/v2/heartbeat
# Expected: HTTP 200

# ★ Verify jarvis-memory:8056 durable audit (secured March 28):
curl -H "Authorization: Bearer $JARVIS_API_KEY" \
  http://localhost:8056/memories?limit=5
# Expected: most recent durable BBB + external-communication gate decision records

# ★ Verify PostgreSQL msjarvis (5433) GBIM is accessible:
psql -h localhost -p 5433 -U msjarvis_user -d msjarvis \
  -c "SELECT COUNT(*) FROM gbim_entities WHERE confidence_decay IS NOT NULL;"
# Expected: row count > 0 (confidence_decay metadata active — March 28)

# ★ Verify PostgreSQL msjarvisgis (5432) is accessible:
psql -h localhost -p 5432 -U gis_user -d msjarvisgis \
  -c "SELECT COUNT(*) FROM zcta_centroids;"
# Expected: 993
```

---

*Chapter 38 — External Communication Channels and Authority Boundaries*
*Ms. Egeria Jarvis Steward System — Harmony for Hope, Inc.*
*Mount Hope, West Virginia*
*Last updated: ★ April 3, 2026 — Chapter 38 SEALED — by Carrie Kidd (Mamma Kidd)*

*★ April 3, 2026: Chapter 38 SEALED — BBB `SafetyMonitor` Phase 1.4 recalibrated — duplicate `'sexual assault'` keyword removed from `self.violence_patterns` line 85 of `safety_monitor.py`; survivor/victim resource queries pass clean (`content_approved=true`, `safety_score=1.0`, `community_safe=true`, `issues=[]`). Hot-copied via `docker cp` — no restart required. §38.2.1, §38.3, §38.4, §38.6.1, §38.8, §38.9 updated. Production context block updated.*
*★ April 2, 2026: 101/101 containers Up confirmed (zero Restarting, zero Exited) — container count updated to 101 throughout; OI-38-A CLOSED — token enforcement active, all 5 public hostnames return 401; OI-36-A / OI-36-B CLOSED — RBACMiddleware live; Caddyfile :8085 self-loop fixed; Cloudflare tunnel HEALTHY; `chat.mountainshares.us` CNAME added; all 0.0.0.0 exposures eliminated; preflight gate corrected to 22 PASS / 0 FAIL / 1 WARN (intentional); §38.2.1, §38.2.2, §38.3, §38.5, §38.6, §38.8, §38.9 updated.*
*★ March 28, 2026: 96/96 containers Up confirmed (zero Restarting, zero Exited) — all service status references updated throughout; §38.2.1 production state updated; §38.2.2 gateway diagram annotated; §38.9 verification command block added*
*★ March 28, 2026: `jarvis-memory:8056` secured (durable BBB + external-communication audit trail, `_auth()` confirmed, `JARVIS_API_KEY` set) — production context block, §38.2.1, §38.2.2, §38.3, §38.4, §38.5, §38.6 (mode-based limits), §38.6.1, §38.7, §38.8, Why This Matters, §38.9 updated*
*★ March 28, 2026: `msjarvis:5433` restored (5,416,521 GBIM entities with `confidence_decay` metadata) — production context block, §38.3, §38.4, §38.7, Why This Matters updated*
*★ March 28, 2026: `msjarvisgis` port corrected to 5432 (91 GB PostGIS, 501 tables, 993 ZCTA centroids) throughout — prior references to port 5452 superseded*
*★ March 28, 2026: ChromaDB full audit (40 active collections / 6,675,442 total vectors) — production context block, §38.4, §38.7 updated*
*March 27, 2026: Ch. 35 merge artifact stripped; OI-38-A sentence restored; Phase 4.5 log+passthrough confirmed throughout; port 8050 as primary entrypoint corrected; Redis async status key 'complete' confirmed*
