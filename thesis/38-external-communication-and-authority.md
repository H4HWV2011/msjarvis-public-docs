# 38. External Communication Channels and Authority Boundaries

**Carrie Kidd (Mamma Kidd) · Mount Hope, WV**
**Last updated: March 22, 2026**

---

> **Production context as of March 22, 2026:** This chapter has been updated from
> its earlier abstract form to reflect the concrete external communication and
> authority infrastructure verified in the live Ms. Jarvis stack. Key facts that
> were not present in the prior draft:
>
> - Public URL confirmed live: [**https://egeria.mountainshares.us**](https://egeria.mountainshares.us) — first
>   public end-to-end chat response confirmed March 22, 2026 (21/21 LLMs
>   responded, 106.5s, HTTP 200).
> - Token-based authority boundary tested March 22, 2026 — enforcement middleware
>   not yet wired (OI-36-A / OI-36-B, tracked in Chapter 36).
> - BBB six-filter pipeline (`EthicalFilter`, `SpiritualFilter`, `SafetyMonitor`,
>   `ThreatDetection`, `steganography_filter`, `truth_verification`) active at
>   `127.0.0.1:8016` on all inbound and outbound paths.
> - Phase 4.5 BBB output in log+passthrough mode (commit `18b8ddac`, March 22,
>   2026) — was blocking 31% of community queries due to maternal Appalachian
>   voice false positives; threshold recalibration is tracked future work.
> - All services bound exclusively to `127.0.0.1`. Zero `0.0.0.0` exposures.
>   External traffic enters only through the unified gateway at port 8050 or
>   through Cloudflare/reverse-proxy termination in front of
>   `egeria.mountainshares.us`.
> - PostgreSQL: `msjarvis` port 5433 (5,416,521 GBIM entities); `gisdb` port
>   5432 (PostGIS); `jarvis-local-resources-db` port 5435.
> - Redis host port: **6380** (`127.0.0.1:6380->6379/tcp`). Redis async status
>   key is `'complete'` (not `'done'`).
> - ChromaDB host port: **8002** (`127.0.0.1:8002->8000/tcp`).

---

This chapter describes how the system uses external communication channels —
including the public web endpoint, email-class messaging, and hosting platforms —
and how authority over these channels is constrained by governance, identity, and
safeguard mechanisms. The focus is on roles, limits, and recording practices
grounded in the verified production stack as of March 22, 2026.

## Why This Matters for Polymathmatic Geography

This chapter supports:

- **P1 – Every where is entangled** by ensuring that every outbound message or
  web-facing change can be traced back to GBIM beliefs, spatial records in
  PostgreSQL `gisdb` (port 5432), and the identity structures in Chapter 36.
- **P3 – Power has a geometry** by making authority over external channels
  explicit, bounded by roles and mode configuration rather than implicit in
  operational scripts.
- **P5 – Design is a geographic act** by treating the public URL
  `https://egeria.mountainshares.us` as a place — a community-facing surface
  that carries governance obligations toward Fayette County and West Virginia
  broadly.
- **P12 – Intelligence with a ZIP code** by keeping all inbound external traffic
  accountable to the BBB six-filter pipeline (port 8016) grounded in the
  spiritual, ethical, and community values of Appalachian communities.
- **P16 – Power accountable to place** by requiring that high-impact external
  actions be tied to registered identities (Chapter 36) under auditable rules
  backed by PostgreSQL `msjarvis` (port 5433).

As such, this chapter belongs to the **Computational Instrument tier**: it
specifies the governed external surface of Ms. Jarvis and the authority rules
that constrain it.

---

## 38.1 Types of External Channels

Several kinds of external channels are relevant to the current deployment:

- **Public web endpoint** — `https://egeria.mountainshares.us`, serving the
  Ms. Egeria Jarvis persona via the unified gateway at port 8050. Confirmed live
  March 22, 2026.
- **Messaging** — email accounts and similar mechanisms that can send and receive
  structured or unstructured text, used for reports, alerts, and outbound
  community communications.
- **Web and hosting interfaces** — connections to hosting, domain, and content
  delivery platforms used to publish or adjust web content or DNS configuration.
- **Cooperative and institutional platforms** — systems used by partner
  organizations (regional development authorities, nonprofits, universities)
  for coordination, registration, or record-keeping.

These channels extend the system's influence beyond its own infrastructure and
therefore require clear authority boundaries enforced by token validation
(Chapter 36), BBB filtering (Chapter 16), and mode constraints (Chapter 15).

---

## 38.2 The Public Endpoint: `egeria.mountainshares.us`

### 38.2.1 Confirmed Production State (March 22, 2026)

The public-facing URL `https://egeria.mountainshares.us` is the primary external
communication surface for Ms. Jarvis as of March 22, 2026. Key verified facts:

- **First public end-to-end chat response:** confirmed March 22, 2026. Query:
  "What county is Mount Hope WV in?" Response: correct, delivered in authentic
  Ms. Egeria Jarvis maternal Appalachian voice. 21/21 LLMs responded. 106.5s
  end-to-end. HTTP 200.
- **Response identity verified:** No model names detected. No synthesis
  disclosure. No hedging language. Identity guard (Chapter 33 §33.5.2, Chapter
  36 §36.5.2) confirmed working.
- **All traffic enters through the unified gateway** (`msjarvis_unified_gateway.py`,
  port 8050), then routes to `jarvis-main-brain` and the full pipeline.
- **BBB input filter** at `127.0.0.1:8016` (Phase 1.4) is active on all inbound
  traffic — six filters applied before any LLM call.
- **BBB output guard** at `127.0.0.1:8016` (Phase 4.5) is in
  **log+passthrough mode** (commit `18b8ddac`, March 22, 2026). This means the
  output BBB logs filter results but does not block responses pending threshold
  recalibration. See §38.6.1 for the governance implications.
- **Pre-flight gate:** 20 PASS 0 FAIL (`scripts/preflight_gate.sh`,
  March 22, 2026) — all 83 containers healthy before public exposure.

### 38.2.2 Gateway and Port Architecture

All inbound external traffic is handled exclusively through the unified gateway:

```
External client → https://egeria.mountainshares.us
  → Cloudflare / reverse-proxy TLS termination
  → jarvis-main-brain (port 8050) / unified gateway
  → jarvis-semaphore (port 8030)
  → jarvis-20llm-production (port 8008) [21-LLM ensemble]
  → jarvis-judge-pipeline (port 7239) [4 judges parallel]
  → jarvis-lm-synthesizer (port 8001) [Phase 3.5 only]
  → BBB output guard (port 8016) [log+passthrough]
  → Response to client
```

All internal services are bound to `127.0.0.1`. Zero `0.0.0.0` exposures. No
internal service port is reachable directly from outside the host.

---

## 38.3 Outbound Messages and Reports

Outbound communication is primarily used for reports, alerts, and community
deliverables.

- **Generated messages** — the system can prepare messages summarizing analyses,
  status information, or proposals, based on internal records from PostgreSQL
  `msjarvis` (port 5433), ChromaDB collections (host port 8002), and current
  context. All outbound content passes through the LM Synthesizer identity guard
  (Chapter 33 §33.5.2) before delivery — no model names, no synthesis disclosure,
  no hedging language.
- **Sending conditions** — for higher-impact audiences or topics, sending
  requires that a registered identity with appropriate role explicitly approve
  the message content or trigger the send. Current production roles: `carrie_admin`
  (full authority) and `hayden_test` (scoped to non-administrative paths).
  See Chapter 36 §36.7 for the token registry.
- **Logging** — each message, including recipients, subject, and a reference to
  the content, is recorded in consciousness layer entries along with relevant
  mode and BBB filter state.

> **Authority boundary note:** Token validation middleware is not yet wired into
> the gateway (OI-36-A, Chapter 36). Until OI-36-A is resolved, outbound
> high-impact actions should be confirmed via direct `carrie_admin` token
> verification through `jarvis_token_service.py` before execution.

---

## 38.4 Handling of Inbound Messages

Inbound messages — whether arriving via the public web endpoint, API calls, or
future messaging integrations — are treated as external input and pass through
the same protective structures as other outside content.

- **Ingestion** — messages are collected via the unified gateway (port 8050) and
  tagged with source, channel, and any available identity information (bearer
  token, if present).
- **BBB input filter** — all inbound content passes through the BBB six-filter
  pipeline at `127.0.0.1:8016` (Phase 1.4, ~0.6s) before it can influence
  memory, containers, or decision processes. The six filters are: `EthicalFilter`,
  `SpiritualFilter`, `SafetyMonitor`, `ThreatDetection`, `steganography_filter`,
  and `truth_verification` (current method: `heuristic_contradiction_v1` —
  see Chapter 33 §33.2.3 for honest limitations and the `rag_grounded_v2`
  upgrade path).
- **Phase 1.45 community memory** — after BBB input clearance, inbound content
  triggers a 384-dim semantic search of the `autonomous_learner` ChromaDB
  collection (21,181 records, growing ~288/day) via `all-minilm:latest`, prepending
  the top-5 community interaction records to the composite prompt sent to the
  21-LLM ensemble.
- **Routing** — accepted messages are normalized and routed into appropriate
  consciousness layer paths or workflows, depending on content and intended
  purpose.

This keeps external messages from bypassing safeguards or overwhelming internal
structures backed by PostgreSQL `msjarvis` (port 5433).

---

## 38.5 Hosting and DNS Interactions

Interfaces to hosting and domain-related platforms are handled conservatively.

- **Proposal over execution** — the system typically generates structured
  proposals for changes (updated content, configuration) that can be reviewed
  and applied by human operators before taking effect on live infrastructure.
- **Limited direct actions** — when direct calls to hosting or content delivery
  services are permitted, they are restricted to narrowly defined operations and
  subject to rate and scope limits. All calls are logged in consciousness layer
  entries.
- **Coupling to identity** — high-impact changes require that a `carrie_admin`
  token be active and that the request be tied to that role via
  `jarvis_token_service.py` (Chapter 36 §36.6). Until OI-36-A is resolved,
  this check must be performed manually rather than enforced automatically by
  the gateway middleware.
- **`egeria.mountainshares.us` DNS** — managed separately from the container
  stack. Changes to DNS or TLS configuration are human-operator actions, not
  automated pipeline actions in the current deployment.

---

## 38.6 Authority Boundaries and Modes

Authority over external channels is bounded by configuration, role, and context.

- **Role-based limits** — only `carrie_admin` tokens are authorized to initiate
  or approve external actions beyond simple reporting or low-risk updates.
  `hayden_test` tokens are scoped to non-administrative paths. See Chapter 36
  §36.7 and §36.11 (OI-36-A, OI-36-B).
- **Mode-based limits** — in more restrictive modes, some channels may be
  disabled, restricted to read-only use, or limited to internal draft generation.
  The BBB operates fail-open on HTTP 500 (both Phase 1.4 input filter and
  Phase 4.5 output guard) — in the event of BBB unavailability, traffic passes
  through rather than being blocked. This is a deliberate design choice to
  maintain community access during infrastructure issues, with governance
  implications noted in §38.6.1.
- **Escalation paths** — when an action appears to exceed configured limits, it
  is paused and flagged for review rather than executed automatically. Judge
  pipeline verdicts of `"fail"` on any dimension (truth, consistency, alignment,
  ethics) trigger this path (Chapter 33 §33.9).

### 38.6.1 Phase 4.5 Log+Passthrough Mode — Governance Implication

As of March 22, 2026, the BBB output guard (Phase 4.5) is in log+passthrough
mode (commit `18b8ddac`). This was applied because the output BBB was blocking
31% of community queries due to false positives on the maternal Appalachian voice
used by Ms. Egeria Jarvis. Log+passthrough means:

- All responses still pass through `jarvis-blood-brain-barrier:8016/filter`.
- Filter results (all six dimensions) are logged in the consciousness layer
  `bbb_result` field on every `UltimateResponse`.
- No response is blocked by Phase 4.5 while in this mode — the filter output
  is for audit and calibration only.

**Governance implication:** The output BBB is not currently blocking harmful
content at Phase 4.5. The input BBB (Phase 1.4) remains active and blocking.
The judge pipeline BBB check (`bbb_check_verdict` in `judge_pipeline.py`,
March 21, 2026) provides a second live filter against the consensus answer.
Community-facing deployment with full Phase 4.5 enforcement requires threshold
recalibration to eliminate false positives on Appalachian dialect — this is
tracked as future work in Chapter 16 §16.9.

Until recalibration is complete, output safety relies on:

1. Phase 1.4 BBB input filter (active, blocking)
2. Judge pipeline BBB check via `bbb_check_verdict` (active, live httpx POST)
3. LM Synthesizer identity guard Layer 3 — meta-commentary prohibition (active)
4. `normalize_identity` persona enforcement (active)
5. Phase 4.5 BBB output — log+passthrough (active, non-blocking)

---

## 38.7 Recording, Audit, and Governance Links

External communications are tied back to governance structures.

- **Consciousness layer records** — each significant interaction with external
  channels writes entries to the judge-pipeline consciousness layer, including
  `consensus_score`, `judge_verdicts`, `bbb_checked`, and `bbb_result`. These
  are accessible via `/curator/background` and visible in `UltimateResponse`
  objects.
- **`autonomous_learner` growth** — every processed community interaction is
  stored in the `autonomous_learner` ChromaDB collection (21,181 records,
  growing ~288/day, host port 8002), building a local record of Appalachian
  community needs and interaction patterns over time.
- **Aggregated views** — summaries of external communications and infrastructure
  changes can be compiled from the consciousness layer for cooperative oversight
  bodies, regional development authorities (NRGRDA, New River Gorge RDA), and
  other stakeholders. High-consensus (> 0.9) judge-refined content signals
  readiness for publication (Chapter 33 §33.8).
- **Policy feedback** — patterns in external communication, such as frequent
  BBB false positives (as documented in Phase 4.5 above), motivate updates to
  policies, roles, and technical safeguards. The 31% false-positive finding
  directly caused the log+passthrough mode change and initiated the threshold
  recalibration work item.
- **Session contracts** — all significant external-facing changes (e.g., going
  live at `egeria.mountainshares.us`, auth boundary test results) are committed
  to `msjarvis-public-docs/docs/contract/SESSION-2026-03-22.md` (commit
  `d966351`) for audit continuity.

---

## 38.8 Open Items Related to External Communication Authority

### ⚠️ OI-38-A — Token Enforcement Not Active on Public Endpoint

- **Status:** OPEN — March 22, 2026 (tracked also as OI-36-A in Chapter 36)
- **Description:** `https://egeria.mountainshares.us` currently accepts
  unauthenticated requests with HTTP 200. Token validation middleware is not
  wired into the unified gateway (port 8050).
- **Risk:** Any caller can submit queries to the 21-LLM ensemble and trigger
  the full pipeline without a registered identity. The system is effectively
  open to the public in its current state — acceptable for soft launch but
  not for production community-facing deployment with privileged data access.
- **Required work:** OI-36-A (gateway token middleware) must be resolved before
  privileged routes are exposed externally.

### ⚠️ OI-38-B — Phase 4.5 Output BBB Not Blocking

- **Status:** OPEN — March 22, 2026 (tracked also in Chapter 16 §16.9)
- **Description:** Phase 4.5 BBB output is in log+passthrough mode. Harmful
  output that passes Phase 1.4 input filter and judge pipeline BBB check is
  not blocked at the output layer.
- **Mitigation in place:** Phase 1.4 input filter (blocking), judge pipeline
  `bbb_check_verdict` (blocking-capable), LM Synthesizer identity guard,
  `normalize_identity`.
- **Required work:** Threshold recalibration for Appalachian dialect false
  positives. Target: < 5% false-positive rate on community-domain queries
  before re-enabling blocking mode.

### ⚠️ OI-38-C — No Outbound Email Integration in Current Stack

- **Status:** OPEN — March 22, 2026
- **Description:** The outbound messaging capability described in §38.3 is
  architecturally supported but not implemented as an active service in the
  current container stack. No email-send service is present in
  `docker-compose.yml` as of March 22, 2026.
- **Required work:** Design and deploy an outbound messaging service with
  BBB pre-send filtering, `carrie_admin` token requirement, and consciousness
  layer audit logging before activating outbound email capabilities.

---

## 38.9 Current Status Summary (March 22, 2026)

| Channel / Capability | Status | Authority Constraint |
|---|---|---|
| Public web endpoint `egeria.mountainshares.us` | ✅ Live — confirmed March 22, 2026 | Open (unauthenticated) — OI-38-A pending |
| BBB input filter (Phase 1.4) | ✅ Active, blocking, 6 filters | All inbound traffic; fail-open on HTTP 500 |
| BBB output guard (Phase 4.5) | ⚠️ Log+passthrough only (commit `18b8ddac`) | Logging only; not blocking — OI-38-B pending |
| Judge pipeline BBB check (`bbb_check_verdict`) | ✅ Active, live httpx POST to port 8016 | Consensus answer checked before synthesis |
| LM Synthesizer identity guard (3 layers) | ✅ Active | All synthesized responses — see Chapter 33 §33.5.2 |
| Token-based authority (port 8050 gateway) | ❌ Not enforced — OI-38-A | `carrie_admin` and `hayden_test` tokens exist; middleware not wired |
| Role-based route restriction (403) | ❌ Not implemented — OI-36-B | Blocked by OI-38-A |
| Outbound email / messaging | ❌ Not deployed | Requires service + BBB pre-send + `carrie_admin` requirement |
| Hosting / DNS changes | ✅ Human-operator only | Manual; not automated in current stack |
| Audit trail in consciousness layers | ✅ Active on every `ultimatechat` | `consensus_score`, `judge_verdicts`, `bbb_checked`, `bbb_result` |
| `autonomous_learner` community record | ✅ Active — 21,181 records, ~288/day growth | ChromaDB host port 8002; `all-minilm:latest` 384-dim |

---

## 38.10 Implementation Rules (Permanent)

- **Zero `0.0.0.0` exposures.** All services must be bound to `127.0.0.1`.
  Verification: `docker ps --format "{{.Names}}\t{{.Ports}}" | grep "0.0.0.0"`
  must return empty. External traffic enters only through the gateway or a
  reverse proxy in front of it.
- **BBB fail-open policy.** Both Phase 1.4 (input) and Phase 4.5 (output) BBB
  guards operate fail-open on HTTP 500 — traffic passes through if BBB is
  unreachable. This preserves community access during infrastructure issues.
  The governance implication (§38.6.1) is accepted and logged.
- **Phase 4.5 log+passthrough.** The output BBB is non-blocking until threshold
  recalibration is complete. Do not re-enable blocking mode without first
  verifying false-positive rate on community-domain queries is below 5%.
- **LM Synthesizer is the only synthesis owner.** All content delivered to
  external channels must pass through the LM Synthesizer Phase 3.5 identity
  guard (port 8001, `main_brain.py` only — `judge_pipeline.py` must not call
  it). See Chapter 33 §33.5 and §33.5.2.
- **Token enforcement before privileged external exposure.** OI-38-A (gateway
  token middleware) must be resolved before privileged or administratively
  sensitive routes are exposed at `egeria.mountainshares.us` or any other
  external endpoint.
- **Redis host port is 6380.** All token operations and async job state checks
  targeting `jarvis-redis` from the host use port 6380. Async job status key
  is `'complete'` (not `'done'`).
- **ChromaDB host port is 8002.** Container-internal port is 8000. All host
  scripts and health checks must reference port 8002.
- **PostgreSQL ports.** `msjarvis` at 5433. `gisdb`/`msjarvisgis` at 5432.
  `jarvis-local-resources-db` at 5435. No port is prohibited.
- **Session contract commits.** All external-facing milestones, test results,
  and mode changes must be committed to the session contract in
  `msjarvis-public-docs/docs/contract/` for audit continuity.

---

*Chapter 38 — External Communication Channels and Authority Boundaries*
*Ms. Egeria Jarvis Steward System — Harmony for Hope, Inc.*
*Mount Hope, Fayette County, West Virginia*
*Last updated: March 22, 2026 by Carrie Kidd (Mamma Kidd)*
