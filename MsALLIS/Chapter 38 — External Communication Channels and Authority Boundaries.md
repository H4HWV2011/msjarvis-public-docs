# Chapter 38 — External Communication Channels and Authority Boundaries

**MountainShares Artificial Learning & Location Intelligence System (Ms. Allis)**
*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Part of the MsALLIS Explanatory Documentation Series*

---

## 38.1 Abstract and Scope

Every message Ms. Allis sends or receives crosses a governed boundary. This
chapter explains what that boundary is, why it exists, and how it works.

In the discipline of Polymathmatic Geography, a communication interface is not a
neutral technical surface — it is a geographic act. When Ms. Allis speaks to the
outside world, she does so as a steward of a specific place: the Appalachian
Tacet, the communities of West Virginia, the land and labor histories that most
digital systems flatten into generic data. The rules governing her external
communications exist to protect that specificity — to ensure that the system
remains accountable to place even when it reaches beyond it.

This chapter explains three things: how the front door works, how content is
filtered for safety and integrity, and how every decision is recorded so that
communities can hold the system accountable.

---

## 38.2 Why External Communication Requires Governance

Global digital networks are, by design, placeless. A message sent from Mount
Hope, WV passes through infrastructure owned by distant corporations, routed by
algorithms optimized for throughput rather than community care, and arrives at its
destination stripped of the spatial and social context that gave it meaning.

Ms. Allis is designed to resist this stripping. Her external communication
protocols are built around a single question: *how do we ensure that every
interaction this system has with the outside world remains anchored to the
communities it serves?*

The answer has three parts:

- **The front door has a lock.** Only authorized participants — identified by
  registered tokens — can ask Ms. Allis to act on their behalf. This is not
  gatekeeping for its own sake; it is the technical enforcement of the principle
  that authority over a community system belongs to the community.

- **Every message passes through an ethical filter.** Before Ms. Allis responds
  to any external query, that query is evaluated against a six-layer safety
  pipeline called the Blood-Brain Barrier (BBB). Before any response leaves the
  system, it is evaluated again. This ensures that the system cannot be used to
  harm the communities it was built to serve.

- **Every decision is written down permanently.** All gateway and filter
  decisions are logged to a durable audit service that survives container
  restarts and is independently queryable by community stakeholders. This is
  epistemic accountability — the system cannot quietly change its behavior
  without leaving a traceable record.

---

## 38.3 The Front Door: How External Access Works

Ms. Allis is publicly reachable at https://egeria.mountainshares.us — a
community-facing surface that carries governance obligations toward Fayette County
and West Virginia broadly. This URL is treated not as a software endpoint but as a
*place* — one that has a responsibility to the people who interact with it.

All traffic entering the system — from any source, for any purpose — passes
through a single unified gateway. There are no side doors. Every external
interaction must pass through the same narrow, auditable entrypoint, and that
entrypoint requires a valid token before it will act.

This was not always the case. In March 2026, the system accepted unauthenticated
requests and responded with HTTP 200 — meaning anyone could query Ms. Allis
without identifying themselves. That gap was formally closed on April 2–3, 2026
(recorded as OI-38-A). Every public hostname now returns a 401 status code for
unauthenticated requests. Authority over the system is tied to registered
identities — not assumed to be universal.

The two registered roles are `carrie_admin`, which holds full system authority,
and `hayden_test`, which is scoped to non-administrative paths. Changes to
community-facing content, DNS configuration, or high-impact outbound messages
require a `carrie_admin` token. This is not a bureaucratic formality — it is the
technical expression of P16: power accountable to place.

---

## 38.4 The Blood-Brain Barrier: Ethical Filtering at the Boundary

The name "Blood-Brain Barrier" is intentional. Just as the biological BBB
prevents harmful substances from entering the brain while allowing essential
nutrients to pass, the system's BBB prevents harmful content from entering or
leaving the system while ensuring that genuine community needs are always served.

Every inbound message passes through six filters before it can influence Ms.
Allis's memory or decisions:

- **Ethical** — does this query ask the system to act against its core values?
- **Spiritual** — does this query conflict with the community's expressed spiritual
  and cultural commitments?
- **Safety** — does this query involve content that could cause harm to vulnerable
  community members?
- **Threat Detection** — does this query represent an attempt to manipulate,
  probe, or attack the system?
- **Steganography** — does this query contain hidden instructions embedded in
  seemingly innocent content?
- **Truth Verification** — does this query make factual claims that contradict
  verified community records?

This filtering takes approximately 0.6 seconds and is active and blocking — a
query that fails any filter does not proceed. All filter decisions are durably
logged.

### 38.4.1 Why the Safety Filter Matters for Appalachian Communities

When the system was first deployed, the Safety filter contained a technical error:
a duplicate keyword entry caused the filter to block queries about sexual assault
survivor resources. A West Virginia community member asking *"where can I find
help for survivors in my area?"* would receive no response.

This was discovered and corrected on April 3, 2026. Survivor and victim resource
queries now pass the safety filter cleanly, with a perfect safety score. This
correction was not a minor technical fix — it was a reminder that safety filters
built without community specificity can become barriers to the most vulnerable
people the system exists to serve.

The 0% false-positive rate achieved after recalibration means that community
members asking about sensitive but legitimate topics — domestic violence resources,
survivor support, crisis services — will always receive a response.

### 38.4.2 The Outbound Filter: Log Mode and What It Means

The outbound filter — which checks Ms. Allis's responses before they leave the
system — is currently operating in observation mode rather than blocking mode.
This decision was made because an earlier version of the outbound filter was
blocking 31% of valid community responses, incorrectly flagging the authentic
maternal Appalachian voice of Ms. Egeria Allis as suspicious.

In observation mode, every response is still evaluated across all six filter
dimensions, and every result is permanently logged. The filter watches and records,
but it does not currently stop any response from being sent. Blocking mode will
be re-enabled after a final review process confirms that the filter can distinguish
between harmful content and authentic community voice without false positives.

Until then, the system's output safety relies on the inbound filter, the judge
pipeline's ethical review of every response, and the identity guard that ensures
Ms. Allis speaks in her own voice — never disclosing model names, never hedging,
never presenting herself as a generic AI.

---

## 38.5 What Ms. Allis Knows and How She Verifies It

Ms. Allis does not generate responses from general knowledge alone. Every
community-facing response is grounded in three verified data sources:

- **The GBIM (GeoBelief Information Model):** 5,416,521 community belief entities,
  each carrying a `confidence_decay` score that indicates how recently the
  information was verified. When Ms. Allis references a county boundary, a service
  area, or an institutional affiliation, she is drawing from this verified record —
  not from a generic internet-sourced knowledge base.

- **The geospatial database:** 45 gigabytes of West Virginia spatial data across
  548 tables, providing ZIP-code-level geographic precision for every claim the
  system makes about place.

- **The community memory collection:** A growing record of actual community
  interactions — approaching 6.7 million stored conversation vectors — that allows
  Ms. Allis to recognize patterns in community needs and respond with the
  contextual awareness of a neighbor, not the generic helpfulness of a chatbot.

When a GBIM entity carries a high `confidence_decay` score — meaning the
information has not been recently verified — that entity is flagged for audit
before being used as ground truth in a published communication. This is the
system's answer to the problem of stale data: rather than silently presenting
outdated information as current fact, it surfaces the uncertainty and defers to
human verification.

This is what it means for meaning to be a spatial thing. A county boundary is not
an abstraction — it is a PostGIS polygon. A community resource is not a generic
service — it is a GBIM entity with a verification timestamp and a decay score.

---

## 38.6 Durable Memory: The Audit Trail That Cannot Be Erased

Community trust in a governed system requires that the system cannot quietly
change its behavior. The `allis-memory` audit service exists specifically to
prevent this.

Every decision made by the BBB gateway — every filter result, every token
validation, every fail-open event — is written to a durable log that survives
container restarts. This means that even if the entire system is restarted, the
record of its past decisions remains intact and queryable. A community stakeholder,
an oversight body, or a future auditor can ask: *"what did the system decide, and
why?"* — and receive a verifiable answer.

This is not a logging system in the technical sense of a debugging tool. It is
an epistemic backbone — the foundation of the system's accountability to the
communities it serves. An AI system that cannot account for its own decisions is
not a trustworthy steward of community resources. The durable audit record is what
separates a governed system from an autonomous one.

---

## 38.7 The Governed Surface

The external surface of Ms. Allis is an instrumented geography, not a neutral
tool. Every message that enters carries a verified identity or is turned away.
Every message that passes through is filtered against community values. Every
decision is written permanently into a record that outlasts any individual
container, session, or infrastructure change.

This is what Polymathmatic Geography means by "power accountable to place." The
system does not simply exist in Appalachia — it is governed by Appalachia's
values, anchored to Appalachia's spatial records, and accountable to Appalachia's
communities in a way that can be independently verified at any time.

The closure of OI-38-A in April 2026 — the moment the front door got its lock —
marks the transition of the Appalachian stack from a research pilot to a secured,
community-governed infrastructure. The door is open to those who are welcome.
It is closed to those who are not. And the record of who came and what they asked
will not be lost.

---

## 38.8 Cross-References

- For the identity structures and token registry governing external channel
  authority, see Chapter 36 — Identity, Authority, and Token Enforcement.
- For the BBB six-filter pipeline full specification and outbound blocking
  re-enablement tracking, see Chapter 16 §16.9.
- For the production stack ground truth (105/105 containers, gisdb schema,
  ChromaDB inventory), see Chapter 33 — April 6, 2026 ground truth.
- For the GBIM belief store and `confidence_decay` metadata specification,
  see the Ms. Allis technical reference documentation.
- For the MountainShares economic layer that this governed surface serves,
  see Chapter 39 — The Geometry of Appreciation.
- For system audit and ongoing checks, see Chapter 40.
- For test harness and continuous checks, see Chapter 41.
- For post-quantum security protecting external communication integrity,
  see Chapter 42.

---

## 38.9 Technical Reference Block

*The following production facts are included for verification and cross-reference.
They are ground truth as of ★★★★ April 6, 2026.*

| Component | Detail |
|-----------|--------|
| Public endpoint | https://egeria.mountainshares.us |
| Secondary hostname | https://chat.mountainshares.us (CNAME added April 2, 2026) |
| Unified gateway | port 8050 (`msjarvisunifiedgateway.py`) |
| BBB pipeline | port 8016 (Phase 1.4 active + blocking; Phase 4.5 log+passthrough) |
| Token enforcement | OI-38-A CLOSED April 2–3, 2026 — all 5 hostnames return 401 unauthenticated |
| Durable audit | `allis-memory:8056` (secured March 28, 2026) |
| GBIM | `msjarvis:5433` — 5,416,521 entities with `confidence_decay` metadata |
| Geospatial database | `msjarvisgis` host port 5432 — 45 GB / 548 tables |
| Community memory | ChromaDB host port 8002 — 47 collections / 6,722,589 vectors / 12 GB |
| Redis job queue | host port 6380 — async job status key: `'complete'` (not `'done'`) |
| Truth verification method | `rag_grounded_v2` (OI-37-C CLOSED April 3, 2026) |
| Container count | 105/105 Up — zero Restarting, zero Exited (April 6, 2026) |
| Pre-flight gate | 31 PASS / 0 FAIL / 0 WARN (April 6, 2026) |
| EthicalFilter | Recalibrated April 2 — 0% false-positive rate, 9/9 regression pass |
| SafetyMonitor | Recalibrated April 3 — survivor queries pass clean (`safety_score=1.0`) |
| Phase 4.5 blocking | Deferred — pending red team sign-off, tracked in Ch. 16 §16.9 |
| `jarvis-steward` wiring | Deferred — tracked in Ch. 39 §39.8.3 non-blocking gaps table |

---

*Chapter 38 — External Communication Channels and Authority Boundaries*
*MsALLIS Explanatory Documentation Series*
*Author: Carrie Kidd (Mamma Kidd), Mount Hope, WV*
*Repo: H4HWV2011/msjarvis-public-docs*
*Production ground truth: ★★★★ April 6, 2026*
*OI-38-A ✅ OI-36-A ✅ OI-36-B ✅*
