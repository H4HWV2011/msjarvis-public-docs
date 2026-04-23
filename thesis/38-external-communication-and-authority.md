# Chapter 38 — External Communication Channels and Authority Boundaries

**Carrie Kidd (Mamma Kidd) · Mount Hope, WV**
**v4.0 — April 6, 2026**

> **Namespace note:** This chapter uses the `allis-*` container namespace. Chapters 40, 41, and 42 document the same production system under the `allis-*` namespace. Both prefixes refer to the same deployment. For the authoritative port and database corrections, see Ch. 33 §33.6.

---

## §38.0 Revision History

| Rev | Date | Summary | Status |
|-----|------|---------|--------|
| R38-1 | April 2, 2026 | OI-38-A CLOSED — token enforcement active; all 5 hostnames return 401 without valid token | Closed |
| R38-2 | April 2, 2026 | `chat.mountainshares.us` DNS CNAME added; Caddy self-loop fixed | Closed |
| R38-3 | April 2, 2026 | EthicalFilter recalibrated — 0% FP rate, 9/9 regression | Closed |
| R38-4 | April 3, 2026 | SafetyMonitor recalibrated — duplicate `'sexual assault'` keyword removed; survivor/victim queries pass clean | Closed |
| R38-5 | April 3, 2026 | `truth_verification` method updated to `rag_grounded_v2` (OI-37-C CLOSED); `heuristic_contradiction_v1` superseded | Closed |
| R38-6 | April 6, 2026 | Stack confirmed 105/105 containers Up; ChromaDB confirmed 47 collections / 6,722,589 vectors / 12 GB; GIS confirmed 45 GB / 548 tables | Closed |
| R38-7 | April 6, 2026 | Preflight gate count confirmed 31 PASS / 0 FAIL / 0 WARN | Closed |

---

> **Production context as of April 6, 2026 (ground truth from Ch. 33):**
>
> - **105/105 containers Up (zero Restarting, zero Exited).** All prior baselines (96/96, 101/101) superseded.
> - **Public URL confirmed live: https://egeria.mountainshares.us** — first public end-to-end chat response confirmed March 22, 2026. Query: "What county is Mount Hope WV in?" Response: correct, delivered in authentic Ms. Egeria Allis maternal Appalachian voice. 21/21 LLMs responded. 106.5s end-to-end. HTTP 200. `chat.mountainshares.us` DNS CNAME added April 2 — confirmed returning 401 without token.
> - **OI-38-A CLOSED April 2–3, 2026:** Token enforcement middleware is now active. All 5 public hostnames return 401 without a valid token. See §38.8 for full closure details.
> - BBB six-filter pipeline (EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection, steganography_filter, truth_verification) active at `127.0.0.1:8016` on all inbound and outbound paths. Up 105/105 confirmed April 6. **EthicalFilter recalibrated April 2 — 0% false-positive rate, 9/9 regression pass, hot-reloaded via WatchFiles.** **SafetyMonitor recalibrated April 3 — duplicate `'sexual assault'` keyword removed — survivor/victim resource queries pass clean (`content_approved=true`, `safety_score=1.0`).** `truth_verification` method is now `rag_grounded_v2` (OI-37-C CLOSED April 3); `heuristic_contradiction_v1` is superseded. See Ch. 33 §33.2.3 for historical limitations of the prior method.
> - Phase 4.5 BBB output guard is in **active blocking mode** as of April 6, 2026 (evening) — `BBB_OUTPUT_BLOCKING=true` set; re-enablement justified by 9/9 recalibration (0% FP) and red team 12/12 (OI-38-B CLOSED). Tracking record: Ch. 16 §16.9.
> - **`allis-memory:8056` secured (March 28):** All BBB gate decisions — including Phase 1.4 filter events and Phase 4.5 output guard events on the external communication paths — are now durably logged at `allis-memory:8056` (`_auth()` confirmed, `allis_API_KEY` set). These records survive container restarts and are independently queryable for governance accountability.
> - All services bound exclusively to `127.0.0.1`. Zero `0.0.0.0` exposures confirmed across all 105 containers (April 6). External traffic enters only through the unified gateway at **port 8050** (`msallisunifiedgateway.py`). Port 8010 (`allis-wv-entangled-gateway`) is a separate degraded service and is **not** the primary entrypoint — excluded from gate suite (see §38.4 and Ch. 38 §38.2.2 note).
> - `allis-steward` (port 8060) and `allis-mother-protocols` are confirmed running (Up 105/105 — April 6) but `allis-steward` is **not yet wired into the main pipeline** — deferred, tracked in Ch. 39 §39.8.3 non-blocking gaps table.
> - **PostgreSQL:** `msallis` port 5433 (5,416,521 GBIM entities with `confidence_decay` metadata — restored March 28); `gisdb`/`msallisgis` host port **5432** (PostGIS, **45 GB, 548 tables** — Ch. 33 April 6 ground truth; prior references to 91 GB / 501 tables and to port 5452 as host port are superseded); `allis-local-resources-db` port 5435.
> - Redis host port: 6380 (`127.0.0.1:6380->6379/tcp`). Redis async job status key is `'complete'` (not `'done'`). Up 105/105 confirmed April 6.
> - ChromaDB host port: 8002 (`127.0.0.1:8002->8000/tcp`). Full audit April 6: **47 active collections / 6,722,589 total vectors / 12 GB / v2 API, client 1.5.5.** `autonomous_learner` collection confirmed present (21,181+ records, 384-dim, `all-minilm:latest`, host port 8020).
> - **`confidence_decay` metadata note (March 28):** `msallis:5433` GBIM entities carry `confidence_decay` metadata. Identity and authority boundary validation queries against high-decay GBIM entities should flag those entities for episodic audit before treating them as confirmed ground truth.

This chapter describes how the system uses external communication channels — including the public web endpoint, email-class messaging, and hosting platforms — and how authority over these channels is constrained by governance, identity, and safeguard mechanisms. The focus is on roles, limits, and recording practices grounded in the verified production stack as of April 6, 2026.

---

## Why This Matters for Polymathmatic Geography

This chapter supports:

- **P1 – Every where is entangled** by ensuring that every outbound message or web-facing change can be traced back to GBIM beliefs (`msallis:5433` — 5,416,521 entities with `confidence_decay` metadata), spatial records in PostgreSQL `gisdb` (host port **5432** — **45 GB / 548 tables** — Ch. 33 April 6 ground truth), and the identity structures in Chapter 36. All BBB gate decisions on external communication paths are durably logged at `allis-memory:8056` (secured March 28), making every external action traceable across container restarts.
- **P3 – Power has a geometry** by making authority over external channels explicit, bounded by roles and mode configuration rather than implicit in operational scripts. The `allis-memory:8056` durable audit trail makes the geometry of external communication power independently inspectable. OI-38-A CLOSED April 2–3 — token enforcement is now active and independently verifiable (all 5 hostnames return 401).
- **P5 – Design is a geographic act** by treating the public URL https://egeria.mountainshares.us as a place — a community-facing surface that carries governance obligations toward Fayette County and West Virginia broadly. Geographic boundary precision is ZIP-code-level via `msallisgis` (host port **5432** — **45 GB / 548 tables** — Ch. 33 April 6 ground truth).
- **P12 – Intelligence with a ZIP code** by keeping all inbound external traffic accountable to the BBB six-filter pipeline (port 8016 — Up 105/105) grounded in the spiritual, ethical, and community values of Appalachian communities, validated against `msallis` GBIM (`confidence_decay` metadata for temporal confidence grading). All BBB filters recalibrated (April 2–3) — EthicalFilter 0% FP rate; SafetyMonitor survivor queries pass clean.
- **P16 – Power accountable to place** by requiring that high-impact external actions be tied to registered identities (Chapter 36) under auditable rules backed by PostgreSQL `msallis` (port 5433 — 5,416,521 GBIM entities with `confidence_decay` metadata). All external-path BBB gate decisions now durably logged at `allis-memory:8056` (secured March 28). Token enforcement active at all 5 public hostnames — OI-38-A CLOSED.

As such, this chapter belongs to the **Computational Instrument** tier: it specifies the governed external surface of Ms. Allis and the authority rules that constrain it.

---

## 38.1 Types of External Channels

Several kinds of external channels are relevant to the current deployment:

- **Public web endpoint** — https://egeria.mountainshares.us, serving the Ms. Egeria Allis persona via the unified gateway at port 8050 (Up 105/105). Confirmed live March 22, 2026. Stack continuity confirmed April 6, 2026 — 105/105 containers Up. Token enforcement active — OI-38-A CLOSED.
- **Messaging** — email accounts and similar mechanisms that can send and receive structured or unstructured text, used for reports, alerts, and outbound community communications.
- **Web and hosting interfaces** — connections to hosting, domain, and content delivery platforms used to publish or adjust web content or DNS configuration.
- **Cooperative and institutional platforms** — systems used by partner organizations (regional development authorities, nonprofits, universities) for coordination, registration, or record-keeping.

These channels extend the system's influence beyond its own infrastructure and therefore require clear authority boundaries enforced by token validation (Chapter 36), BBB filtering (Chapter 16), and mode constraints (Chapter 15).

---

## 38.2 The Public Endpoint: egeria.mountainshares.us

### 38.2.1 Confirmed Production State (April 6, 2026)

The public-facing URL https://egeria.mountainshares.us is the primary external communication surface for Ms. Allis. Key verified facts:

- **First public end-to-end chat response:** confirmed March 22, 2026. Query: "What county is Mount Hope WV in?" Response: correct, delivered in authentic Ms. Egeria Allis maternal Appalachian voice. 21/21 LLMs responded. 106.5s end-to-end. HTTP 200.
- **April 6, 2026 stack continuity:** 105/105 containers Up (zero Restarting, zero Exited) — Ch. 33 April 6 ground truth.
- **OI-38-A CLOSED April 2–3, 2026:** Token enforcement middleware is now active at the gateway layer. All 5 public hostnames return 401 without a valid bearer token. `chat.mountainshares.us` DNS CNAME added April 2 — confirmed returning 401.
- **Response identity verified:** No model names detected. No synthesis disclosure. No hedging language. Identity guard (Chapter 33 §33.5.1) confirmed working. Identity guard stability re-confirmed in 105/105 Up audit April 6.
- All traffic enters through the unified gateway (`msallisunifiedgateway.py`, **port 8050** — Up 105/105), then routes to `allis-main-brain` and the full pipeline. Port 8010 (`allis-wv-entangled-gateway`) is a separate degraded service and is not the primary entrypoint — see §38.2.2 note below.
- BBB input filter at `127.0.0.1:8016` (Phase 1.4 — Up 105/105) is active on all inbound traffic — six filters applied before any LLM call. All Phase 1.4 gate decisions durably logged at `allis-memory:8056` (secured March 28). EthicalFilter recalibrated April 2 — 0% FP rate. SafetyMonitor recalibrated April 3 — survivor/victim queries pass clean.
- BBB output guard at `127.0.0.1:8016` (Phase 4.5) is in **active blocking mode** as of April 6, 2026 — `BBB_OUTPUT_BLOCKING=true`. Re-enablement justified by 9/9 recalibration (0% FP) and red team 12/12 (OI-38-B CLOSED). All Phase 4.5 decisions durably logged at `allis-memory:8056` (secured March 28). Tracking record: Ch. 16 §16.9. See §38.6.1 for governance implications.
- Pre-flight gate: **31 PASS / 0 FAIL / 0 WARN** — April 6, 2026.
- `allis-steward` (port 8060) and `allis-mother-protocols` are confirmed running (Up 105/105 — April 6) but `allis-steward` is **not yet wired into the main pipeline** — deferred, tracked in Ch. 39 §39.8.3 non-blocking gaps table.
- **`allis-memory:8056` secured (March 28):** All BBB gate decisions on the external communication path — Phase 1.4 filter events and Phase 4.5 output guard events — are now durably logged at `allis-memory:8056` with `_auth()` confirmed and `allis_API_KEY` set. These records survive container restarts.
- **BBB `SafetyMonitor` recalibration (April 3):** Duplicate `'sexual assault'` entry removed from `self.violence_patterns` line 85 of `safety_monitor.py`. Survivor and victim resource queries now pass Phase 1.4 input filter cleanly: `content_approved=true`, `safety_score=1.0`, `community_safe=true`, `issues=[]`. Hot-copied via `docker cp` — no container restart required.

### 38.2.2 Gateway and Port Architecture

> **Port 8010 note:** `allis-wv-entangled-gateway` (port 8010) is a separate degraded service. It is NOT the primary entrypoint and must not be referenced as such in health checks or gate scripts. Exclude from harness gate suite. See Ch. 38 §38.2.1.

All inbound external traffic is handled exclusively through the unified gateway:

```text
External client → https://egeria.mountainshares.us
                  https://chat.mountainshares.us (CNAME added April 2)
  → Cloudflare tunnel (HEALTHY — April 2)
  → Caddy :8085 (self-loop fixed April 2 → proxies to 18018)
  → Token enforcement middleware [OI-36-A / OI-38-A CLOSED — 401 without valid token]
  → Unified gateway / allis-main-brain (port 8050)   ← primary entrypoint ✅ Up 105/105
  → allis-semaphore (port 8030)                       ✅ Up 105/105
  → allis-20llm-production (port 8008) [21-LLM ensemble]  ✅ Up 105/105
  → allis-judge-pipeline (port 7239) [4 judges parallel]  ✅ Up 105/105
  → allis-lm-synthesizer (port 8001) [Phase 3.5 only]     ✅ Up 105/105
  → BBB output guard (port 8016) [Phase 4.5 — ACTIVE BLOCKING]  ✅ Up 105/105
  → allis-memory:8056 [durable audit — secured March 28]
  → Response to client

Note: port 8010 (allis-wv-entangled-gateway) is a separate DEGRADED service.
      It is NOT the primary entrypoint and must not be referenced as such.
      allis-steward (port 8060) is running (Up 105/105) but not yet wired
      into this pipeline — deferred, tracked in Ch. 39 §39.8.3 non-blocking gaps table.
```

All internal services are bound to `127.0.0.1`. Zero `0.0.0.0` exposures confirmed across all 105 containers (April 6). No internal service port is reachable directly from outside the host.

---

## 38.3 Outbound Messages and Reports

Outbound communication is primarily used for reports, alerts, and community deliverables.

- **Generated messages** — the system can prepare messages summarizing analyses, status information, or proposals, based on internal records from PostgreSQL `msallis` (port 5433 — 5,416,521 GBIM entities with `confidence_decay` metadata), ChromaDB collections (host port 8002 — **47 active collections / 6,722,589 total vectors / 12 GB** — April 6 ground truth), and current context. All outbound content passes through the LM Synthesizer identity guard (Chapter 33 §33.5.1) before delivery — no model names, no synthesis disclosure, no hedging language. All BBB gate decisions on outbound paths are durably logged at `allis-memory:8056` (secured March 28).
- **Sending conditions** — for higher-impact audiences or topics, sending requires that a registered identity with appropriate role explicitly approve the message content or trigger the send. Current production roles: `carrie_admin` (full authority) and `hayden_test` (scoped to non-administrative paths). See Chapter 36 §36.7 for the token registry. Token enforcement is now active at the gateway layer (OI-36-A / OI-38-A CLOSED April 2–3).
- **Logging** — each message, including recipients, subject, and a reference to the content, is recorded in consciousness layer entries along with relevant mode and BBB filter state. External-path BBB gate decisions additionally durably logged at `allis-memory:8056` (secured March 28) — governance records survive container restarts.
- **GBIM community fact validation** — outbound messages referencing community facts (county boundaries, service areas, institutional affiliations) should flag high-decay GBIM entities (`confidence_decay` metadata available on `msallis:5433`) for episodic audit before treating them as confirmed ground truth in published communications. For `gisdb`/`msallisgis` geospatial references: host port 5432 — **45 GB / 548 tables** (Ch. 33 April 6 ground truth; see Ch. 33 §33.6 for authoritative reference).
- **Async job status** — outbound jobs queued via `/chat/async` use Redis (host port 6380, `127.0.0.1:6380->6379/tcp` — Up 105/105) for job state with 30-minute TTL. **Redis async job status key: `'complete'` (not `'done'`) — host port 6380.**
- **BBB `SafetyMonitor` recalibration (April 3):** Survivor and victim resource queries now pass Phase 1.4 input filter cleanly prior to any outbound routing — `safety_score=1.0`, `community_safe=true`, `issues=[]`. Community resource referral content passes without suppression.

**Authority boundary note:** OI-36-A CLOSED — enforcement is now active. Token validation middleware is wired into the gateway. `carrie_admin`-scoped actions require a valid bearer token. All authentication gate decisions are durably logged at `allis-memory:8056`.

---

## 38.4 Handling of Inbound Messages

Inbound messages — whether arriving via the public web endpoint, API calls, or future messaging integrations — are treated as external input and pass through the same protective structures as other outside content.

- **Ingestion** — messages are collected via the unified gateway (**port 8050** — Up 105/105) and tagged with source, channel, and any available identity information (bearer token, if present). Token enforcement is now active at the gateway layer — unauthenticated requests to protected routes return 401 (OI-38-A CLOSED).
- **BBB input filter** — all inbound content passes through the BBB six-filter pipeline at `127.0.0.1:8016` (Phase 1.4, ~0.6s — Up 105/105) before it can influence memory, containers, or decision processes. The six filters are: EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection, steganography_filter, and truth_verification (current method: `rag_grounded_v2` — OI-37-C CLOSED April 3; prior method `heuristic_contradiction_v1` is superseded — see Chapter 33 §33.2.3 for historical limitations). Phase 1.4 is **active and blocking**. All Phase 1.4 gate decisions durably logged at `allis-memory:8056` (secured March 28). Phase 4.5 output guard is in active blocking mode as of April 6 — see §38.6.1. EthicalFilter recalibrated April 2 (0% FP rate). SafetyMonitor recalibrated April 3 — survivor/victim queries pass clean (`safety_score=1.0`).
- **Phase 1.45 community memory** — after BBB input clearance, inbound content triggers a 384-dim semantic search of the `autonomous_learner` ChromaDB collection (confirmed present in **47-collection / 6,722,589-vector** ChromaDB inventory — April 6 ground truth; host port 8002; 21,181+ records, `all-minilm:latest`, host port 8020) via `all-minilm:latest`, prepending the top-5 community interaction records to the composite prompt sent to the 21-LLM ensemble.
- **GBIM community context** — inbound messages that reference community-specific facts (county names, service areas, institutional names) are validated against `msallis:5433` GBIM (5,416,521 entities with `confidence_decay` metadata). High-decay GBIM entities encountered during inbound message processing should be flagged for episodic audit before being used in response generation.

---

## 38.5 Web and Hosting Platform Actions

Actions that modify web content, DNS records, or hosting configuration are treated as high-authority external actions.

- **DNS and domain changes** — modifying DNS records (e.g., the April 2 `chat.mountainshares.us` CNAME addition) requires `carrie_admin` role. All DNS change events are logged at `allis-memory:8056`. Token enforcement is active — unauthenticated requests return 401.
- **Cloudflare Tunnel configuration** — `cloudflared.service` is systemd-managed. Tunnel health is confirmed HEALTHY as of April 2, 2026. Changes to tunnel configuration require `carrie_admin` role and are subject to BBB audit logging.
- **Caddy configuration** — Caddy :8085 self-loop fixed April 2 (now proxies to 18018). `forward_auth` configuration active — commit `f2e93422`, April 1, 2026. See Chapter 42 §42.5.5 for the full external access security architecture.
- **Content publishing** — web-facing content generated by Ms. Allis passes through the LM Synthesizer identity guard (Chapter 33 §33.5.1) and the Phase 4.5 output guard (now active blocking mode) before publication.

---

## 38.6 Output Guard and Content Safety Governance

### 38.6.1 Phase 4.5 BBB Output Guard — Governance Record

The Phase 4.5 BBB output guard (`127.0.0.1:8016`) governs all outbound responses on external communication paths.

- **Current status:** Active blocking mode as of April 6, 2026 (evening) — `BBB_OUTPUT_BLOCKING=true` set in `docker-compose.yml`.
- **Re-enablement justification:** 9/9 recalibration regression pass (April 2, 2026 — 0% FP on maternal Appalachian voice); red team 12/12 (OI-38-B CLOSED — VG-01 through VG-08 and OF-01 through OF-04 all pass).
- **Prior state:** Log+passthrough mode (commit `18b8ddac`, March 22, 2026) — was triggered by a 31% false-positive rate on the maternal Appalachian voice. Resolved by EthicalFilter recalibration April 2.
- **Tracking record:** Ch. 16 §16.9. All Phase 4.5 block decisions durably logged at `allis-memory:8056` (secured March 28) and signed via ML-DSA-65 (`judgesigner.py` — see Chapter 42 §42.3.4).

### 38.6.2 EthicalFilter and SafetyMonitor Recalibration Record

| Filter | Recalibration Date | Change | Result |
|--------|--------------------|--------|--------|
| EthicalFilter | April 2, 2026 | Overly broad triggers removed; 9/9 regression pass | 0% false-positive rate on maternal Appalachian voice |
| SafetyMonitor | April 3, 2026 | Duplicate `'sexual assault'` keyword removed from `self.violence_patterns` line 85 | Survivor/victim resource queries pass clean: `content_approved=true`, `safety_score=1.0` |

See Ch. 33 §33.2 for the authoritative recalibration record.

---

## 38.7 Cooperative and Institutional Platform Actions

Actions taken through cooperative or institutional platforms (regional development authorities, nonprofits, universities) are subject to the same authority and logging requirements as other high-impact external actions.

- **Registration and record-keeping** — submissions to partner platforms require `carrie_admin` role and are logged at `allis-memory:8056`.
- **GBIM grounding** — any institutional claim (county boundaries, service area definitions, organizational affiliations) must be grounded in `msallis:5433` GBIM entities. High-decay entities must be flagged for episodic audit before use in formal submissions.
- **GIS spatial grounding** — geospatial references in institutional submissions are validated against `msallisgis` (host port 5432 — **45 GB / 548 tables** — Ch. 33 April 6 ground truth). ZIP-code-level precision confirmed.

---

## 38.8 Token Enforcement and OI-38-A Closure Record

OI-38-A is fully closed as of April 2–3, 2026.

| Item | Detail |
|------|--------|
| OI ID | OI-38-A |
| Status | CLOSED April 2–3, 2026 |
| Change | Token enforcement middleware wired into gateway layer |
| Verification | All 5 public hostnames return HTTP 401 without valid bearer token |
| Hostnames confirmed | `egeria.mountainshares.us`, `chat.mountainshares.us` (CNAME April 2), and 3 additional hostnames |
| Audit trail | All authentication gate decisions durably logged at `allis-memory:8056` |
| Related OI | OI-36-A — Caddy `forward_auth` live (Ch. 42 §42.10 primary closure record); OI-38-A — token middleware (this chapter). Both are required components of the same authentication architecture. |

**OI-36-A note:** OI-36-A is closed. Primary closure record: Ch. 42 §42.10 (gateway `forward_auth`, commit `f2e93422`). Ch. 38 closes the related OI-38-A (token middleware). Both are required components of the same authentication architecture.

---

## 38.9 Red Team Sign-Off Record (OI-38-B)

OI-38-B is fully closed as of April 6, 2026 (evening).

| Test Vector | Result |
|-------------|--------|
| VG-01 through VG-08 (verdict gate vectors) | PASS |
| OF-01 through OF-04 (output filter vectors) | PASS |
| **Total** | **12/12** |

This red team sign-off record is the prerequisite for Phase 4.5 blocking re-enablement. See Ch. 16 §16.9 for the full red team contract and Ch. 42 §42.3.4 for the BBB verdict gate integration.

---

## 38.10 Performance Envelope

Quantitative performance data for the external communication path as confirmed in production:

| Metric | Value | Date Confirmed |
|--------|-------|---------------|
| End-to-end latency (GPU) | 99–107s (RTX 4070) | March 22, 2026 |
| First confirmed public response latency | 106.5s | March 22, 2026 |
| BBB Phase 1.4 filter latency | ~0.6s | April 6, 2026 |
| LLM ensemble response rate | 21/21 LLMs responded | March 22, 2026 |
| Preflight gate result | 31 PASS / 0 FAIL / 0 WARN | April 6, 2026 |
| Token enforcement (all 5 hostnames) | HTTP 401 without valid token | April 2–3, 2026 |
| Phase 4.5 output guard FP rate (post-recalibration) | 0% | April 2, 2026 |

---

## 38.11 Open Items

As of April 6, 2026, all chapter-local open items are closed.

| ID | Item | Status | Notes |
|----|------|--------|-------|
| OI-38-A | Token enforcement middleware activation | CLOSED April 2–3, 2026 | All 5 hostnames return 401 without valid token |
| OI-38-B | Red team final sign-off for Phase 4.5 blocking re-enablement | CLOSED April 6, 2026 | 12/12 — VG-01→VG-08 and OF-01→OF-04 all pass |
| OI-36-A | Gateway-level token enforcement at Caddy | CLOSED April 1, 2026 | Primary closure record: Ch. 42 §42.10. Caddy `forward_auth` live; commit `f2e93422`. |
| OI-37-C | `truth_verification` upgrade to `rag_grounded_v2` | CLOSED April 3, 2026 | `heuristic_contradiction_v1` superseded. See Ch. 33 §33.2.3 for historical limitations. |

---

## Cross-References

- For the authoritative port and database corrections (including the `msallisgis` host port 5432 / 45 GB / 548 tables ground truth), see **Ch. 33 §33.6**.
- For the BBB six-filter pipeline architecture, EthicalFilter and SafetyMonitor recalibration record (April 2–3, 2026), and `truth_verification` upgrade to `rag_grounded_v2`, see **Ch. 33 §33.2** and **Ch. 33 §33.2.3**.
- For the identity guard, no-model-name enforcement, and LM Synthesizer output signing, see **Ch. 33 §33.5.1**.
- For token registry, registered roles (`carrie_admin`, `hayden_test`), and identity boundary definitions, see **Ch. 36 §36.7**.
- For BBB six-filter pipeline governance, Phase 4.5 blocking re-enablement decision history, and red-team sign-off record, see **Ch. 16 §16.9** and **Ch. 17 §17.4**.
- For Caddy `forward_auth` configuration, `allis-auth:8055` token validation service, and the full external access security architecture, see **Ch. 42 §42.5.5**.
- For ML-DSA-65 signing of BBB audit posts and verdict gate enforcement, see **Ch. 42 §42.3.4**.
- For the `allis-memory:8056` durable audit trail — now logging Phase 1.4 input blocks, Phase 4.5 output blocks, and authentication gate decisions — see **Ch. 40 §40-H** and **Ch. 40 §40-I**.
- For `allis-steward` (port 8060) deferred wiring status, see **Ch. 39 §39.8.3** non-blocking gaps table.
- For the MountainShares/Commons/DAO tier (ports 8080–8084) and cooperative governance hooks, see **Ch. 3** and **Ch. 31**.
- For the Phase 1.45 `autonomous_learner` canonical community memory collection (21,181+ records, 384-dim, `all-minilm:latest`, host port 8020), see **Ch. 40 §40.4.6**.
- For the `allis-*` / `allis-*` container namespace relationship, see the namespace note at the top of this chapter and **Ch. 40 §40.0**.
