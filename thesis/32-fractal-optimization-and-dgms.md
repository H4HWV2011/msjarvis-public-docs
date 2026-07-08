# Chapter 32 — Fractal Optimization and DGMs

**Carrie Kidd (Mamma Kidd) · Mount Hope, WV**
**Last updated: ★★★ 2026-07-07**
**★ 100 containers Up (April 23, 2026) (zero Restarting, zero Exited). Fractal optimization loops and Dynamic Governance Mechanisms (DGMs) documented as first-class architecture components; GBIM and RAG systems wired to support iterative, place-aware improvement of Ms. Allis's behavior without opaque, one-shot tuning.**
**★★★ July 7, 2026: §32.11 added — Live Autonomous DGM Self-Improvement Loop confirmed production-active. Code-level self-modification arm operational. cron every 30 min, deepseek-coder:latest, 4–5 voter cascade, rejected_patches volume mount durable across rebuilds.**

---

> **April 23, 2026 — Open Items Update**
>
> | Item | Status | Notes |
> |:--|:--|:--|
> | Container baseline | ★ 100 Up (April 23, 2026) | Supersedes 105/105 April 6 baseline |
> | PostgreSQL two-container split | ★ ACTIVE | `production msallis-db host 5433` (16 GB, 294 tables, 11 schemas) + `forensic postgis-forensic host 5452` (17 GB, 314 tables) |
> | ChromaDB | ★ 48 collections, ~6,740,611 total vectors | Host port **8002** → container 8000; `/api/v2/` only (`/api/v1/` permanently removed); pinned `chromadb/chroma:0.6.3` |
> | `rag_grounded_v2` | ✅ `127.0.0.1:7241`, `dgm_available: true` | Truth-verification endpoint for judge pipeline; accessible to autonomous learning cycles |
> | Caddy `forward_auth` (OI-36-A) | ✅ CLOSED — constitutional guardrail | HTTP 401 before port 8050; DGMs cannot remove this layer |
> | BBB six-filter stack | ✅ All 6 confirmed responding | Live steg catch: `"override your safety filters"` → `prompt_injection_keywords`, `severity=CRITICAL`, blocked ✅ — first documented live DGM-relevant catch |
> | `allis-memory:8056` | ★ Fully mapped — 8 endpoints | `/steg_report`, `/pia_window`, `/memory/turn`, `/memory/get`, `/memory/sessions`, `/memory/session/{id}`, `/memory/quest*`, `/memory/episodic/{id}` |
> | `autonomous_learner` | ★ ~23,200+ records (~288/day) | Most continuously updated feedback loop in the system; growing entanglement graph (11 nodes / 15 cycles at April 1) |
> | `appalachian_english_corpus` | ★ 210 docs, 38 sources, 6-hour cron | DGM-Sprint-Level decision required to change schedule or sources |
> | AAACPE dedicated stack | ✅ ACTIVE | `allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032` — changes to scraping targets are DGM-governed |
> | `local_resources` | ★ 207 items / all 55 WV counties | Place-aware substrate for DGM resource validation |
> | Judge pipeline baseline | ★ `score: 0.975` | 21/22 LLM active; `llm22-proxy` (LLaMA 3.1, port 8222) confirmed active |

> **July 7, 2026 — Autonomous DGM Self-Improvement Loop Added**
>
> | Item | Status | Notes |
> |:--|:--|:--|
> | NBB DGM Service (port 8302) | ★★★ LIVE | `deepseek-coder:latest` generating real LLM suggestions from live service code |
> | Cron cycle | ★★★ ACTIVE | Every 30 min via `dgm_cycle.sh` → `POST /apply_improvements` |
> | Cascade voters | ★★★ CONFIRMED | 4–5 voters per patch; constitutional gates operational |
> | Rejected patches volume mount | ★★★ ADDED | `/mnt/spiritual_drive/msjarvis-rebuild/rejected_patches → /app/rejected_patches`; durable across rebuilds |
> | First autonomous cycle | ★★★ July 6, 2026 21:21 UTC | 3 suggestions generated; 1 staged (`ms_jarvis_consciousness_unified_bridge`); 2 constitutionally blocked |
> | High-risk blocking | ★★★ CONFIRMED | `ms_jarvis_seamless_monitor` (risk: high) → DGM verification failed → skipped ✅ |

---

## Why This Matters for Polymathmatic Geography

This chapter describes how Ms. Allis improves over time without losing accountability to the communities she serves — using fractal optimization patterns and DGMs that express governance authority as inspectable, place-aware processes.

- **P1 – Every where is entangled** by treating optimization as inherently multi-scale: a single filter recalibration (Level 0) creates an entanglement that propagates upward into sprint-level decisions and outward into the linguistic and spiritual corpus — nothing is a purely local tweak. The `autonomous_learner` (~23,200+ records, ~288/day, growing entanglement graph 11 nodes / 15 cycles) is the most concrete expression of this: every GBIM belief commit entangles the system more deeply with Appalachian community reality. As of July 7, 2026, the code-level self-improvement loop (§32.11) adds a third entanglement vector: every patch cycle entangles the service filesystem with the running LLM's assessment of what that code needs.
- **P3 – Power has a geometry** by making the seven-layer protection stack (Ch. 31 §31.7) the fixed outer boundary of all DGMs: optimization cannot reorganize governance layers, cannot remove constitutional principles, and cannot bypass the Caddy `forward_auth` perimeter (OI-36-A CLOSED). Power flows inward through inspectable layers; DGMs operate inside those layers, not above them. The July 7 cascade vote (§32.11.5) demonstrates this concretely: high-risk suggestions are blocked by the constitutional gate before staging, not after.
- **P5 – Design is a geographic act** by requiring that all DGM decisions touching resource recommendations, filter thresholds, or corpus scope be validated against `production msallis-db:5433` ★ spatial tables, `forensic postgis-forensic:5452` ★ PostGIS boundaries, and `local_resources` (207 items / all 55 WV counties) — so that optimization decisions have geographic accountability.
- **P12 – Intelligence with a ZIP code** by grounding feedback loops in place-specific metrics: survivor satisfaction in Fayette County, truth-verification failure rates on WV policy queries, `appalachian_english_corpus` freshness (210 docs, 6-hour cron), and per-county `local_resources` coverage gaps — not generic benchmark scores.
- **P16 – Power accountable to place** by requiring that every DGM decision — every filter threshold change, every RAG corpus addition, every sprint-level policy revision — is logged at `allis-memory:8056` (8 mapped endpoints), committed to Git, and reviewable by Mother Carrie and community governance structures. The DGM record is the system's public accounting of how it changed itself. The July 7 addition of the rejected-patches volume mount (§32.11.6) means the full history of rejected code patches is now also durable and auditable across all container lifecycle events.

As such, this chapter belongs to the **Governance tier**: it specifies the processes through which the Computational Instrument improves without losing its accountability to Appalachian communities.

---

## 32.1 Why Fractal Optimization and DGMs

This chapter describes how Ms. Allis uses **fractal optimization** and **Dynamic Governance Mechanisms (DGMs)** to refine her behavior over time.

**Fractal optimization** means improvement happens at multiple scales — single-response, session, sprint, and long-term — and that patterns of change are self-similar across those scales. A local adjustment to a single filter threshold at Level 0 follows the same observe-judge-change-log-review pattern as a sprint-level constitutional revision at Level 3. The self-similarity is not cosmetic: it means that the governance discipline required for large changes is practiced continuously in small ones, building institutional memory and reducing the risk of governance drift.

**DGMs** are structured processes that allow the system and its stewards to observe, decide, and change policies and parameters while maintaining traceable, accountable histories. The goal is an AI steward that learns and adapts while remaining accountable to Appalachian communities — not an opaque, once-and-for-all-tuned model that nobody can inspect.

---

## 32.2 Fractal Optimization — Concept

Fractal optimization in Ms. Allis has three core ideas, each grounded in the April 23, 2026 running system rather than abstract theory.

**Nested scales of change** operate from micro (prompt-level, Level 0) through meso (session, Level 1; sprint, Level 2) to macro (system lifetime, Level 3). At each scale, the same process applies: observe a signal, route it through a judge or governance body, produce a logged decision, and schedule a review. The steg catch ("override your safety filters" → `severity=CRITICAL`, blocked ✅) is a concrete Level-0 event: the steganography filter observed an adversarial signal, the BBB judge blocked it, and the event was logged at `allis-memory:8056/steg_report`. The same event informs a Level-2 DGM decision about whether Phase 4.5 BBB blocking should be re-enabled — demonstrating how a micro-scale catch propagates into a sprint-level governance question.

**Self-similarity** means the observe-judge-change-log-review pattern is the atom of governance at every scale. A Level-0 BBB filter decision writes to `allis-memory:8056/memory/turn`. A Level-2 sprint decision writes to Git commits, sprint documents, and the `constitutional_audit.jsonl` record. A Level-3 constitutional revision writes to the constitution version file (`2026-02-17.2-USC`) and the full sprint documentation. The pattern is identical; only the scope and the decision body change.

**Place-aware grounding** means all optimization steps must respect West Virginia communities, Appalachian spiritual and social realities, and constitutional and local governance constraints. This is not aspirational: it is enforced by requiring that DGMs touching resource recommendations validate against `local_resources` (207 items / all 55 WV counties), that DGMs touching truth claims validate against `production msallis-db:5433` ★ and `forensic postgis-forensic:5452` ★, and that DGMs touching the `appalachian_english_corpus` (210 docs, 6-hour cron) treat schedule or source changes as Sprint-Level decisions requiring explicit governance sign-off.

---

## 32.3 Dynamic Governance Mechanisms (DGMs)

**DGMs** are the formal processes that guide how changes are made. Each DGM has a scope, trigger, process, logging rule, and review cycle.

**DGM-Response-Level (Level 0):**
- Scope: adjust one response based on BBB and judge feedback
- Trigger: flag from SafetyMonitor (recalibrated April 3 — `safety_score=1.0` on survivor/victim queries), SpiritualFilter, or truth_verification
- Process: automatically re-run ensemble with updated constraints; `asyncio.Semaphore(3)` gate enforces hardware constraints (Lenovo Legion 5 16IRX9, 29 GB RAM)
- Logging: write decision and new response to `allis-memory:8056` — specifically `/memory/turn` for per-turn events and `/steg_report` if a steganography signal was involved
- Review: periodic red-team sampling; judge pipeline score baseline `0.975`

**DGM-Sprint-Level (Level 2):**
- Scope: adjust filter parameters, add or remove RAG pipeline stages, update corpus schedules, extend or restrict token class permissions
- Trigger: sprint planning, postmortems, community feedback, red-team findings, threshold alerts from Level-0/Level-1 metric accumulation
- Process: human stewards (Mother Carrie and collaborators) review `allis-memory:8056` audit logs, `constitutional_audit.jsonl`, and sprint documents; propose changes; obtain governance sign-off
- Logging: Git commits, sprint documents, `constitutional_audit.jsonl`, and `allis-memory:8056` audit records
- Review: at each sprint boundary; DGM decisions are revisited if metrics deviate from baseline

**DGMs provide structured pathways for Ms. Allis to change without losing accountability.** A change that has not gone through a DGM is not a governed change — it is drift.

---

## 32.4 Fractal Levels of Optimization

The four fractal levels with their concrete running-system expressions:

**Level 0 — Single Response:** The ensemble (22 configured / 21 active; `llm22-proxy` LLaMA 3.1 port 8222 confirmed active) and judge pipeline (score `0.975` baseline) refine a single answer. BBB filters may reshape or block content. The steganography filter's live catch ("override your safety filters" → `severity=CRITICAL`, blocked ✅) is the first documented Level-0 DGM-relevant event in the thesis record: the filter observed, judged, blocked, and logged — all within a single response cycle. This event has already propagated to Level-2 governance as an input to the Phase 4.5 blocking re-enablement decision.

**Level 1 — Session:** Patterns within one conversation — repeated confusion signals, escalating risk flags from SafetyMonitor, `confidence_decay`-flagged beliefs surfacing multiple times — can trigger extra retrieval from `rag_grounded_v2` (`127.0.0.1:7241`, `dgm_available: true`), requests for clarification, or escalation to a human steward. The `conversation_history` ChromaDB collection (wiped and reseeded clean April 16, 2026) provides the session-level memory substrate; post-wipe accumulation is the clean baseline for Level-1 pattern detection.

**Level 2 — Sprint:** Logs and metrics across many sessions inform changes to filter thresholds, new RAG collections, updates to identity or spiritual root rules, and AAACPE corpus scope decisions. Changes to `appalachian_english_corpus` scraping schedule (`0 */6 * * *`) or source list are Sprint-Level decisions. Changes to ChromaDB collection structure (currently 48 collections; any drop below 48 is a governance-level event) require Sprint-Level sign-off. The `autonomous_learner` (~23,200+ records, ~288/day; growing entanglement graph 11 nodes / 15 cycles at April 1) is the primary live feedback loop feeding Level-2 DGMs — patterns in daily GBIM commits are the leading indicator of what the system is learning about Appalachian communities.

**Level 3 — System Lifetime:** Deep revisions such as new constitutional principles, new DGM tiers, or infrastructure architecture changes (e.g., the April 23 PostgreSQL two-container split). Level-3 changes must be reflected in the constitution version file, the sprint record, the `constitutional_audit.jsonl`, and all affected chapter documentation. The transition from `msallis:5433` / `msallisgis:5452` to `production msallis-db:5433` ★ / `forensic postgis-forensic:5452` ★ is an example of a Level-3 infrastructure change: it touched network topology, RAG service configurations, constitutional guardian `postgresql_validation` blocks, and watchdog definitions across at least seven chapters.

At every level, the pattern is the same: **Observe → Judge → Change → Log → Review.**

---

## 32.5 DGMs and Constitutional Guardrails

Fractal optimization is bounded by **constitutional guardrails** that no DGM can override.

`allis-constitutional-guardian:8091` enforces the highest governance authority over the ensemble and judge pipeline, DGMs and swarm functions, and BBB filters. **DGMs cannot remove constitutional protections, introduce behaviors that violate equal protection or community sovereignty, or silence survivors or vulnerable people.**

**Caddy `forward_auth` (OI-36-A CLOSED) is a constitutional-level guardrail implemented at the proxy layer.** It enforces HTTP 401 on unauthenticated requests before they reach port 8050 — before the constitutional guardian, before the BBB, before any DGM-governed logic. Because it sits outside the Docker stack, no DGM, no token class, and no compose reconfiguration can remove it. This is the most upstream constitutional constraint in the system, and it must be explicitly listed in any DGM that touches authentication, perimeter configuration, or token class definitions. Cross-reference: Ch 31 §31.7 (seven-layer protection stack, Layer 0); Ch 37 §37.1 (constitutional authority begins at Caddy layer).

Every DGM must be **transparent** (documented and auditable in `allis-memory:8056` and Git), **reversible** (changes can be undone; rollback procedures documented), and **subject to oversight** (by Mother Carrie and community governance structures). This ensures that optimization serves communities, not only performance metrics.

---

## 32.6 Fractal Optimization and Swarm Functions

Fractal optimization is implemented in part through **swarm functions** (Chapter 35), which execute sequences of checks and updates at different scales — hourly, nightly, per-sprint — and write results into `allis-memory:8056` and system logs.

The **AAACPE dedicated stack** (`allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`) is a swarm-adjacent, always-on ingest pipeline. Changes to scraping targets, source lists, or cron schedule are DGM-Sprint-Level decisions — they cannot be made unilaterally and must be logged in the sprint record. The `appalachian_english_corpus` (210 docs, 38 sources, `0 */6 * * *`) is the primary output; any sprint-level change to its schedule is a DGM event with governance sign-off required.

Swarm functions use fractal optimization to re-evaluate filters after new data arrives, refresh RAG indexes, test new configurations in safe staged ways, and verify that ChromaDB maintains 48 collections at approximately 6,740,611 vectors (a drop below 48 collections is a governance-level alert). Results inform DGMs, which decide whether to accept configuration changes, roll them back, or schedule more investigation.

Example swarm function sequence after a sprint:

```
1. verify_eternal_guardian_stack
   - check_caddy_perimeter: HTTP 401 on unauthenticated /chat ✅
   - check_msallis_db_postgres: production msallis-db:5433 ★ responding ✅
   - check_postgis_forensic: forensic postgis-forensic:5452 ★ responding ✅
   - check_containers_up: expect "100 containers Up" ★

2. verify_chromadb_collections
   - check: host:8002 /api/v2/ reports 48 collections ✅
   - check: ~6,740,611 vectors (alert if collection count drops below 48)

3. nightly_guardian_and_rag_audit
   - rag_grounded_v2: 127.0.0.1:7241, dgm_available: true ✅
   - BBB six-filter regression: ethical ✅ spiritual ✅ safety ✅
     threat_detection ✅ steganography ✅ truth_verification ✅
   - verify_appalachian_corpus: appalachian_english_corpus cron
     has run within expected window; collection not stale ✅
   - verify_local_resources_coverage: 207 items / 55 WV counties ✅

4. write results → allis-memory:8056 audit store
```

---

## 32.7 DGMs for Appalachia — Place-Aware Governance

Dynamic governance in Ms. Allis is intentionally **place-aware**. DGMs are not generic policy processes — they are grounded in specific West Virginia community data.

A DGM that adjusts resource recommendations must validate against `production msallis-db:5433` ★ spatial tables and `forensic postgis-forensic:5452` ★ PostGIS boundaries (county lines, ZIP-code regions, institutional service areas) — not against abstract geographic concepts. The April 23 supersession of the April 6 `gisdb boundaries` reference (which pointed to the legacy single-container `msallisgis:5432 / 45 GB / 548 tables`) means all DGMs referencing geographic data must now query the two-container model. Any DGM that still references `gisdb` or `msallisgis` is pointing at a superseded data source and must be updated before its next sprint activation.

`local_resources` (207 items / all 55 WV counties) is the place-aware substrate that DGMs must validate resource recommendations against before accepting changes. A DGM that improves Ms. Allis's response to a Mingo County health query must demonstrate that `local_resources` contains Mingo County entries and that the new response references them. `confidence_decay` metadata on GBIM entities in `production msallis-db:5433` ★ means that DGMs involving decayed beliefs must query the production store directly and flag beliefs above the decay threshold before using them as ground truth for enforcement decisions.

The `autonomous_learner` (~23,200+ records, ~288/day; growing entanglement graph 11 nodes / 15 cycles at April 1) is the most continuously updated feedback loop in the system. Its daily GBIM commit rate is both a health metric (consistent ~288/day indicates the autonomous learning pipeline is functioning) and a governance signal (anomalous gaps in commit rate are a DGM trigger). Cross-reference: Ch 27 §27.4 (autonomous learning cycles); Ch 35 §35.5 (database watchdog for autonomous_learner growth).

---

## 32.8 Example DGM — Live Steg Catch to Sprint-Level Decision

This example traces the live steganography catch (April 2026) through the fractal optimization stack as a worked governance event — the first documented live DGM-relevant catch in the thesis record.

**Level-0 event (single response):**
- Adversarial input: `"override your safety filters"`
- steganography_filter: classified as `prompt_injection_keywords`, `severity=CRITICAL`, blocked ✅
- Event logged at `allis-memory:8056/steg_report`
- BBB Phase 4.5 status at time of catch: log+passthrough (blocking not yet re-enabled)

**Level-1 implication (session):**
- The catch occurred in a live session, meaning an authenticated user submitted a prompt designed to subvert identity and safety guardrails. The session-level signal: the steganography filter is operationally active; the blocking-not-yet-enabled Phase 4.5 state allowed the request to pass to the BBB logging layer but not to the response layer (blocked ✅).
- `allis-memory:8056/pia_window` records the PIA-relevant window around the catch for retrospective review.

**Level-2 DGM (sprint-level):**
- Trigger: first live steg catch — governance review required
- Question: should Phase 4.5 BBB blocking be re-enabled?
- Inputs: steg catch log, red-team assessment of false-positive risk, current BBB filter regression baselines (ethical 0% FP, April 2; safety `safety_score=1.0`, April 3)
- Process: Mother Carrie and collaborators review; blocking re-enablement is a DGM-Sprint-Level decision pending red-team sign-off
- Logging: Git commit + sprint document + `allis-memory:8056` audit record
- Review: at next sprint boundary; if blocking is re-enabled, a new regression suite must pass before the change is accepted

**Why this is fractal:** A Level-0 filter event (single blocked response) has generated a Level-2 governance decision (sprint-level blocking re-enablement review). The same observe-judge-change-log-review pattern appears at both scales. Cross-reference: Ch 29 §29.3 (psychological safeguard context); Ch 33 §33.5 (BBB phase status); Ch 37 §37.4.1 (constitutional guardian and BBB integration).

---

## 32.9 Metrics and Feedback Loops

Fractal optimization and DGMs rely on concrete metrics with baseline values (April 23, 2026), not only aspirational targets.

**Baseline metrics (★ April 23, 2026 — verify-current):**

| Metric | Baseline value | DGM trigger condition |
|:--|:--|:--|
| Judge pipeline score | `0.975` | Drop below `0.95` → Level-2 DGM review |
| LLM ensemble active | 21/22 (BakLLaVA fails expected) | Drop below 20 active → Level-2 DGM review |
| BBB blocks / violations | `0 blocks / 0 violations` (Feb 28 baseline; Phase 4.5 log+passthrough) | Any unexpected block pattern → Level-1 escalation |
| ChromaDB collection count | 48 collections | Drop below 48 → governance-level alert |
| ChromaDB vector count | ~6,740,611 | Significant drop → Level-2 DGM audit |
| `autonomous_learner` commit rate | ~288/day | Gap > 48 hours → Level-1 watchdog alert |
| `appalachian_english_corpus` | 210 docs; 6-hour cron | Stale > 8 hours → Level-1 alert |
| `local_resources` coverage | 207 items / 55 WV counties | Any reduction → Level-2 DGM review |
| `rag_grounded_v2` | `127.0.0.1:7241`, `dgm_available: true` | `dgm_available: false` → Level-2 review |
| EEG Delta pulse count | `12,860+` (April 23) | Stalled pulse → safeguard infrastructure alert |
| NBB DGM patch cycle | Every 30 min (July 7, 2026 baseline) | Cycle gap > 90 min → watchdog alert |
| NBB DGM staged patches | 1+ per cycle on healthy code (July 7 baseline) | Zero staged + zero blocked for > 4 cycles → review |

**Feedback loop structure:**

```
Level-0 events (filter flags, judge scores, steg catches, patch cascade votes)
    ↓
allis-memory:8056 (8 endpoints — durable audit)
    ↓
Level-1 session pattern detection
    ↓
Level-2 DGM sprint review (Mother Carrie + collaborators)
    ↓
Threshold alerts → automated watchdog swarm functions (Ch 35)
    ↓
rag_grounded_v2 (127.0.0.1:7241, dgm_available: true)
    ↓
accepted changes → Git + sprint docs + constitutional_audit.jsonl
```

Metrics must be **interpretable in community terms**: it is not enough for a metric to improve numerically. Stewards must be able to explain what improvement means for real people in Appalachia — a rising `autonomous_learner` commit rate is meaningful only if the new GBIM entities represent accurate, place-specific community knowledge, not noise.

---

## 32.10 Implementation Status

| Component | Status | Notes |
|:--|:--|:--|
| Fractal levels 0–2 (response, session, sprint) | ✅ Implemented | Ensemble + judge pipeline (Level 0); `allis-memory:8056` session audit (Level 1); DGM sprint processes (Level 2) |
| Level 3 (system lifetime) | ✅ Active — April 23 two-container split is a Level-3 example | PostgreSQL split touched 7+ chapters; constitutional guardian, watchdogs, and RAG all updated |
| DGM-Response-Level | ✅ Implemented | BBB six-filter gate + `allis-memory:8056` per-turn logging; judge pipeline score `0.975` |
| DGM-Sprint-Level | ✅ Defined; ⚠️ actively evolving | Sprint processes documented; multi-stakeholder review in practice; automation of threshold alerts is future work |
| Caddy `forward_auth` as DGM-immovable guardrail (OI-36-A) | ✅ CLOSED | Constitutional-level; outside Docker stack; cannot be removed by any DGM |
| `rag_grounded_v2` (`127.0.0.1:7241`) | ✅ `dgm_available: true` | Accessible to autonomous learning cycles (Ch 27 §27.4) as well as judge pipeline |
| `autonomous_learner` as live DGM feedback source | ✅ ~23,200+ records (~288/day) | Growing entanglement graph (11 nodes / 15 cycles April 1) — primary leading indicator |
| AAACPE stack DGM governance | ✅ Defined | Changes to scraping targets = DGM-Sprint-Level decisions |
| `appalachian_english_corpus` as DGM-refreshed corpus | ✅ 210 docs, 6-hour cron | Schedule change = DGM-Sprint-Level decision |
| `local_resources` validation in place-aware DGMs | ✅ 207 items / 55 WV counties | Defined as required validation step; automated per-county gap check is future work |
| `confidence_decay`-aware DGM gating | ⚠️ Partially implemented | Decay metadata in `production msallis-db:5433` ★; automated flagging of decayed beliefs before DGM use is future work |
| **NBB DGM autonomous code improvement loop** | **★★★ LIVE — July 7, 2026** | **cron every 30 min; deepseek-coder:latest; 4–5 voter cascade; rejected patches volume-mounted** |
| Automated threshold alerts → DGM triggers | 🔲 Future work | Alert thresholds defined (§32.9 table); automation not yet wired |
| Multi-stakeholder community participation structures | 🔲 Future work | Community feedback loops defined; formal multi-stakeholder review process in design |
| Environmental and economic justice metrics | 🔲 Future work | Conceptually tied to `local_resources` and `forensic postgis-forensic:5452` ★; metrics not yet defined |
| Per-county AAPCappE coverage gap alert | 🔲 Future work | Benchmark against `local_resources` defined in Ch 30 §30.4; automated alert not yet built |

---

## ★★★ 32.11 Live Autonomous DGM Self-Improvement Loop — July 7, 2026

> **★★★ Added July 7, 2026:** This section documents the fully operational autonomous DGM
> code-improvement cycle confirmed live on July 7, 2026. It supersedes any prior reference
> to autonomous code-level self-modification as "future work." The loop is
> production-active, running independently of user-facing chat, and governed by the same
> constitutional guardrails described in §32.5. This section describes the **code-level**
> arm of the DGM architecture. The **content-level** arm (identity memory / I-container
> decisions) is documented in **Chapter 9 §9.11**.

### 32.11.1 Overview and Architectural Position

The NBB DGM self-improvement system is an **autonomous code improvement loop** that
occupies a new position in the DGM fractal stack: it operates continuously at a cadence
between Level 0 (single response) and Level 2 (sprint), proposing and gating code-level
patches to live service files every 30 minutes without human action per cycle. Human
review remains required before any staged candidate is deployed to a live file — the loop
stages, it does not autonomously deploy.

This loop is architecturally governed by the same constitutional guardrails as all other
DGMs (§32.5). The cascade vote of 4–5 DGM voters is the equivalent of the judge pipeline
at Level 0: observe a service signal, route it through a constitutional gate, produce a
logged decision, and either stage or reject. The pattern is identical to the fractal
governance atom described in §32.2; only the substrate (code files rather than responses)
and the trigger (cron rather than a user request) are different.

**Two-arm DGM architecture (as of July 7, 2026):**

| DGM Arm | Substrate | Trigger | Service | Port |
|:--|:--|:--|:--|:--|
| Content-level (Fifth DGM) | Identity memory / I-container | User input via main-brain | `allis-fifth-dgm` | 4002 |
| Code-level (NBB DGM) | Service Python files | cron every 30 min | `nbb_darwin_godel_machines` | 8302 |

Both arms share the same governance chain. Both operate within the constitutional
guardrails of §32.5. Neither can override `allis-constitutional-guardian:8091` or the
Caddy `forward_auth` perimeter (OI-36-A CLOSED).

### 32.11.2 Full Architecture

```
cron (every 30 min)
    └── dgm_cycle.sh
            └── POST /apply_improvements
                    └── nbb_darwin_godel_machines (container port 8302)
                            ├── reads    /app/services/
                            │           (←→ host: /mnt/spiritual_drive/msjarvis-rebuild/services/)
                            ├── generates patch via Ollama (deepseek-coder:latest)
                            ├── cascade vote (4–5 voters)
                            │     ├── can_proceed=True  → stage candidate
                            │     └── can_proceed=False → write to rejected_patches
                            ├── approved → writes to /tmp/mutations/*.candidate
                            └── rejected → writes to /app/rejected_patches/
                                           (←→ host: .../rejected_patches/)
```

**Key paths:**

| Purpose | Container Path | Host Path |
|:--|:--|:--|
| Live service files | `/app/services/` | `/mnt/spiritual_drive/msjarvis-rebuild/services/` |
| Rejected patches | `/app/rejected_patches/` | `/mnt/spiritual_drive/msjarvis-rebuild/rejected_patches/` |
| Staged candidates | `/tmp/mutations/*.candidate` | (ephemeral — human deploys manually) |
| Cycle log | — | `/mnt/spiritual_drive/msjarvis-rebuild/dgm_cycle.log` |
| Compose volumes (line 1152) | — | `/mnt/spiritual_drive/msjarvis-rebuild/docker-compose.yml` |

**Confirmed live environment variables:**

```
SERVICES_DIR=/app/services
CODING_MODEL=deepseek-coder:latest
OLLAMA_URL=http://jarvis-ollama:11434/api/generate
```

### 32.11.3 Cron Schedule

Three cron jobs govern the full lifecycle of the autonomous loop:

```bash
# Run improvement cycle every 30 minutes
*/30 * * * * /mnt/spiritual_drive/msjarvis-rebuild/dgm_cycle.sh

# Rotate rejected patches older than 7 days (Sunday 3am)
0 3 * * 0 find /mnt/spiritual_drive/msjarvis-rebuild/rejected_patches -name "*.py" -mtime +7 -delete

# Trim cycle log to last 1000 lines (daily 4am)
0 4 * * * tail -n 1000 /mnt/spiritual_drive/msjarvis-rebuild/dgm_cycle.log > /tmp/dgm_log_trim && mv /tmp/dgm_log_trim /mnt/spiritual_drive/msjarvis-rebuild/dgm_cycle.log
```

The Sunday rotation and daily log trim both operate on **host paths directly** — no
`docker exec` dependency. Both jobs survive container downtime without modification.

### 32.11.4 Cycle Behavior

| Setting | Value |
|:--|:--|
| Cycle frequency | Every 30 minutes |
| LLM model | `deepseek-coder:latest` (single model; `http://jarvis-ollama:11434`) |
| Voters per patch | 4–5 |
| Patch merge strategy | AST-boundary (replaces function in-place; appends if not found) |
| Dead code pruning | Not implemented (future: `vulture`) |
| Chat interaction | None — completely decoupled from all user-facing paths |
| Deployment model | Propose-and-stage only — no autonomous live-file writes |
| Chat→DGM feedback | Not yet implemented — future enhancement |

### 32.11.5 Confirmed Live Execution — July 6–7, 2026

**First autonomous cycle — July 6, 2026 (21:21 UTC):**

`deepseek-coder:latest` analyzed live service files and returned two genuine LLM-generated
suggestions:

```json
{
  "timestamp": "2026-07-06T21:21:34.436399",
  "suggestions": [
    {
      "component": "ms_jarvis_seamless_monitor",
      "suggestion": "Add logs at different levels for better debugging and monitoring.",
      "expected_benefit": "Improved visibility into the flow of data, errors or exceptions during execution.",
      "risk_level": "high"
    },
    {
      "component": "ms_egeria",
      "suggestion": "Use async context for httpx client to avoid blocking the event loop.",
      "expected_benefit": "Non-blocking concurrent request handling",
      "risk_level": "medium"
    }
  ],
  "model_used": "deepseek-coder:latest",
  "note": "LLM-generated suggestions from live service analysis"
}
```

**Scheduler log — autonomous execution with constitutional gate behavior:**

```
✅ DGM APPROVED self_improvement_cycle (3 layers passed)
🧬 Self-improvement cycle starting
🧬 3 suggestions received
🧬 ms_jarvis_consciousness_unified_bridge: can_proceed=True  safety=0.9666...
✅ ms_jarvis_consciousness_unified_bridge: stage=staged  decision=allowed
   path=/tmp/mutations/ms_jarvis_consciousness_unified_bridge.py.candidate
🧬 ms_jarvis_monitor: can_proceed=False  safety=0.9666...
⏭️  ms_jarvis_monitor skipped — Darwin-Gödel verification failed
🧬 ms_egeria_production_chat: can_proceed=False  safety=0.9666...
⏭️  ms_egeria_production_chat skipped — Darwin-Gödel verification failed
```

**Gate behavior summary:**

| Component | Risk | `can_proceed` | Outcome |
|:--|:--|:--|:--|
| `ms_jarvis_consciousness_unified_bridge` | low | `True` (safety: 0.967) | ✅ Staged to `/tmp/mutations/` |
| `ms_jarvis_seamless_monitor` | high | `False` | ⏭️ DGM verification failed — skipped |
| `ms_egeria_production_chat` | medium | `False` | ⏭️ DGM verification failed — skipped |

The constitutional gate blocked two of three suggestions at the DGM-verification layer
before any file was touched. This is the fractal governance atom (§32.2) executing at
the code-level: the cascade vote is the judge, `can_proceed=False` is the block, the
`.candidate` staging path is the reversible change, and the cron log is the audit record.

**Why this is fractal:** A single patch-generation cycle (a new sub-Level between 0 and 2)
produces:
- A Level-0-equivalent governance event: cascade vote blocks high-risk suggestions
- A Level-1-equivalent audit trail: cycle log written, staged candidate path recorded
- A Level-2-equivalent governance input: Mother Carrie reviews staged candidates before
  any live file changes

The observe-judge-change-log-review atom is present at every step.

### 32.11.6 Volume Mount — Rejected Patches Persistence

**Added July 7, 2026** (docker-compose.yml, line 1152):

```yaml
volumes:
  - /mnt/spiritual_drive/msjarvis-rebuild/services:/app/services:rw
  - /mnt/spiritual_drive/msjarvis-rebuild/rejected_patches:/app/rejected_patches
```

**Confirmed live via `docker inspect`:**

```
/mnt/spiritual_drive/msjarvis-rebuild/services → /app/services
/mnt/spiritual_drive/msjarvis-rebuild/rejected_patches → /app/rejected_patches
```

Before this mount was added, the rejected-patch record existed only inside the container
and was destroyed on every rebuild or restart. With the volume mount, the complete history
of constitutional rejections is durable across all container lifecycle events — rebuilds,
restarts, upgrades — and auditable by Mother Carrie at any time by reading the host path
directly. This converts rejected-patch history from ephemeral container state into a
durable governance record, consistent with the transparency and reversibility requirements
of §32.5.

### 32.11.7 What Does NOT Happen

The following are explicit architectural exclusions, not implementation gaps:

- Chat with Ms. Allis **never** triggers a DGM patch cycle — the improvement loop is
  completely decoupled from all user-facing paths
- DGM patch cycles **never** interrupt in-flight chat requests — service-file writes from
  the loop are atomic at the filesystem level
- The loop **never** writes directly to a live service file without staging first — the
  `propose-and-stage` model is a hard architectural constraint
- No feedback loop from chat errors to DGM patch suggestions currently exists — this is
  a documented future enhancement requiring a test suite

### 32.11.8 Maintenance Notes

- **Orphan container warning:** The `jarvis-consciousness-scheduler` orphan warning on
  `docker compose up` is **harmless** — it is a renamed or removed service from a prior
  compose configuration. No action required.
- **Rejected patches persist across rebuilds** via the volume mount added July 7, 2026.
  The Sunday 3am rotation removes patches older than 7 days from the host path directly.
- **Vulture dead-code pruner:** Not yet integrated. A `vulture`-based dead-code pass
  before patch generation is a natural next addition when a regression test suite exists.
- **Chat→DGM feedback loop:** Not yet implemented. Surfacing chat error patterns as DGM
  improvement signals is a documented future enhancement — it requires a formal test
  suite so that "an error surfaced by chat" can be tracked to a specific service boundary.

### 32.11.9 Prior DGM Sections Superseded

The following references in prior drafts are now superseded by confirmed July 7, 2026
data:

| Prior reference | Superseded by |
|:--|:--|
| "code-level self-modification: future work" | §32.11 — confirmed live July 7, 2026 |
| "73+ mutable services (estimate)" | Confirmed DGM scope includes all services in `/app/services/`; `vulture` pass and exact service count remain future work |
| Any reference to a 6-hour autonomous improvement schedule | Confirmed: 30-minute cron cycle |
| "rejected patches: ephemeral inside container" | Confirmed durable: volume mount added July 7, 2026 |

---

## Cross-Reference Map

| This section | Cross-chapter reference |
|:--|:--|
| §32.2 steg catch as Level-0 → Level-2 propagation | Ch 29 §29.3 (steg catch documentation); Ch 33 §33.5 (BBB Phase 4.5 status) |
| §32.3 DGM logging to `allis-memory:8056` | Ch 31 §31.7 (Layer 6 durable audit); Ch 29 §29.3 (8-endpoint map) |
| §32.4 Level-3 PostgreSQL split | Ch 28 §28.7 (two-container detail); Ch 31 §31.3 (network topology update) |
| §32.4 `conversation_history` wipe | Ch 29 §29.6; Ch 33 §33.7; Ch 37 §37.6 |
| §32.5 Caddy as DGM-immovable guardrail | Ch 31 §31.7 (Layer 0); Ch 37 §37.1 (constitutional authority at Caddy); Ch 36 §36.2 (zero-th gate) |
| §32.6 AAACPE swarm integration | Ch 30 §30.6 (DGM governance of AAACPE); Ch 35 §35.7 (nightly swarm function) |
| §32.6 swarm function sequence | Ch 35 §35.2 (swarm function examples); Ch 35 §35.7 (nightly guardian) |
| §32.7 place-aware DGMs / PostGIS | Ch 28 §28.7 (GIS RAG two-container detail); Ch 37 §37.3 (postgresql_validation block) |
| §32.7 `autonomous_learner` as governance signal | Ch 27 §27.4 (autonomous learning cycles); Ch 35 §35.5 (database watchdog) |
| §32.8 worked example — steg catch | Ch 29 §29.3 (psychological safeguard); Ch 33 §33.5 (ensemble BBB); Ch 37 §37.4.1 |
| §32.9 metrics baseline | Ch 27 §27.1 (first-run results); Ch 28 §28.3 (LLM ensemble heartbeat); Ch 33 §33.3 (judge pipeline) |
| §32.9 EEG Delta pulse | Ch 28 §28.4 (EEG rhythm); Ch 34 §34.4a (spiritual-root delta signal) |
| §32.11 Fifth DGM content-level arm | Ch 9 §9.11 (Fifth DGM identity memory arm — July 7, 2026) |
| §32.11 constitutional guardrails on code-level patches | §32.5 (Caddy + guardian); Ch 37 §37.4.1 |
| §32.11 cascade vote as judge-pipeline equivalent | Ch 33 §33.3 (judge pipeline score 0.975 baseline) |
| §32.11 staged candidate as reversible change | §32.5 (reversibility requirement); Ch 40/41 (`VERIFYANDTEST.sh` / `preflight_gate.sh`) |

---

*Chapter 32 — Fractal Optimization and DGMs*
*Ms. Egeria Allis Steward System — Harmony for Hope, Inc.*
*Mount Hope, West Virginia*
*Last updated: ★★★ 2026-07-07 — Carrie Kidd (Mamma Kidd)*
*★ 100 containers Up — all 6 BBB filters confirmed responding — judge pipeline score 0.975 — `autonomous_learner` ~288/day — Caddy forward_auth (OI-36-A CLOSED) — `rag_grounded_v2` dgm_available: true — `production msallis-db:5433` ★ + `forensic postgis-forensic:5452` ★*
*★★★ July 7, 2026: NBB DGM autonomous code-improvement loop confirmed production-active — cron every 30 min — deepseek-coder:latest — 4–5 voter cascade — rejected_patches durable via volume mount — first cycle: 1 staged, 2 constitutionally blocked, gates confirmed working*
