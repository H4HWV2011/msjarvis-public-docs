# Chapter 32 — Fractal Optimization and DGMs

**Carrie Kidd (Mamma Kidd) · Mount Hope, WV**
**Last updated: ★★★ 2026-07-07**
**★ 100 containers Up (April 23, 2026) (zero Restarting, zero Exited). Fractal optimization loops and Dynamic Governance Mechanisms (DGMs) documented as first-class architecture components; GBIM and RAG systems wired to support iterative, place-aware improvement of Ms. Allis's behavior without opaque, one-shot tuning.**
**★★★ July 7, 2026: this chapter is rewritten to incorporate the now-live autonomous Darwin Gödel self-improvement loop. The code-level DGM no longer stages for human deployment review; it reads service code, generates improvements with one Ollama model, votes on them, applies approved patches directly, and persists rejected patches on the host filesystem.**

---

> **April 23, 2026 — Established baseline retained**
>
> | Item | Status | Notes |
> |:--|:--|:--|
> | Container baseline | ★ 100 Up (April 23, 2026) | Stable running baseline retained in this chapter |
> | PostgreSQL two-container split | ★ ACTIVE | `production msallis-db host 5433` + `forensic postgis-forensic host 5452` |
> | ChromaDB | ★ 48 collections, ~6,740,611 total vectors | `/api/v2/` baseline retained for governance context |
> | `rag_grounded_v2` | ✅ `127.0.0.1:7241`, `dgm_available: true` | Truth-verification available to autonomous cycles |
> | Caddy `forward_auth` | ✅ CLOSED — constitutional guardrail | Upstream perimeter cannot be removed by DGMs |
> | BBB six-filter stack | ✅ All 6 confirmed responding | Level-0 governance example retained |
> | `allis-memory:8056` | ★ Fully mapped — 8 endpoints | Durable audit substrate |
> | `autonomous_learner` | ★ ~23,200+ records (~288/day) | Live learning feedback source |
> | `appalachian_english_corpus` | ★ 210 docs, 38 sources, 6-hour cron | Sprint-governed corpus substrate |
> | `local_resources` | ★ 207 items / all 55 WV counties | Place-aware validation substrate |
> | Judge pipeline baseline | ★ `score: 0.975` | April baseline retained for comparison |

> **July 7, 2026 — New autonomous code-improvement facts**
>
> | Item | Status | Notes |
> |:--|:--|:--|
> | `nbb_darwin_godel_machines` | ★★★ LIVE | Autonomous code-improvement DGM service confirmed active |
> | Cycle trigger | ★★★ ACTIVE | `*/30 * * * * /mnt/spiritual_drive/msjarvis-rebuild/dgm_cycle.sh` |
> | Apply path | ★★★ DIRECT | `POST /apply_improvements` applies approved patches without human intervention |
> | Ollama model count | ★★★ ONE MODEL | `CODING_MODEL=deepseek-coder:latest` |
> | Patch destination | ★★★ LIVE FILES | Approved patches write back to `/app/services/` |
> | Rejected-patch durability | ★★★ LIVE | `/app/rejected_patches/` volume-mounted to host |
> | Rotation job | ★★★ ACTIVE | Weekly host-side deletion of `.py` rejects older than 7 days |

---

## Why This Matters for Polymathmatic Geography

This chapter explains how Ms. Allis improves across nested scales without collapsing governance into a single hidden optimizer. Fractal optimization in this system is no longer only conceptual or limited to chat-time filtering; it now includes a live autonomous code-revision loop that changes the service substrate itself on a recurring schedule.

- **P1 – Every where is entangled** because a single code patch to one service can propagate upward into response quality, safety behavior, memory formation, corpus handling, and user trust. The autonomous Darwin Gödel loop adds a code-level entanglement pathway to the already-documented response-, session-, and sprint-level entanglements.
- **P3 – Power has a geometry** because optimization authority is distributed across layers rather than concentrated in one opaque training run. The cron trigger, patch generator, cascade vote, constitutional boundaries, filesystem write path, and rejection archive all occupy different positions in the governance geometry.
- **P5 – Design is a geographic act** because optimization remains accountable to Appalachian communities rather than to abstract benchmark scores. Even when the code-level DGM acts autonomously, it still operates inside a wider system whose grounding stores, resource maps, and validation structures are place-bound.
- **P12 – Intelligence with a ZIP code** because the aim of improvement is not generic capability expansion but better situated behavior in real West Virginia contexts. Code changes matter because they shape how place-aware retrieval, safety, and stewardship actually behave in lived interactions.
- **P16 – Power accountable to place** because self-modification is logged, bounded, and inspectable. The rejected-patch archive on the host filesystem turns failed or blocked self-improvement attempts into a durable public record within the system’s internal governance apparatus.

As such, Chapter 32 belongs to the **Governance tier**: it specifies how optimization occurs, who or what may act at each level, which substrates are mutable, and which boundaries remain constitutionally fixed.

---

## 32.1 Why Fractal Optimization and DGMs

Ms. Allis improves through **fractal optimization** and **Dynamic Governance Mechanisms (DGMs)**. Fractal optimization means that the same governance atom appears across scales: observe a condition, evaluate it, decide on a change, record the event, and feed the result back into later behavior.

A DGM is the formal mechanism that gives this pattern enforceable structure. In the current system, DGMs no longer govern only response shaping, session refinement, and sprint policy changes; they also govern a production-active code-level self-improvement loop that reads service files, generates patches with a single coding model, votes on those patches, and applies approved changes to live code automatically.

---

## 32.2 Fractal Optimization — Concept

Fractal optimization in Ms. Allis has three core properties: **nested scale**, **self-similarity**, and **grounded constraint**.

**Nested scale** means that optimization occurs at more than one level at once. A BBB filter catch is a micro event, a session-level clarification pattern is a meso event, a sprint-level corpus or policy revision is a larger event, and a recurring code-rewrite cycle is a substrate-level event that modifies the machinery through which all other levels operate.

**Self-similarity** means these levels share the same internal grammar. The code-level Darwin Gödel loop follows the same atom as a response-level safeguard: inspect a live condition, produce an evaluable candidate, route it through governance logic, keep what passes, archive what fails, and continue operating.

**Grounded constraint** means optimization is never allowed to become a free-floating maximizer. Even autonomous code revision remains bounded by the surrounding constitutional architecture, audit expectations, place-aware resource grounding, and the fixed outer layers of protection that DGMs cannot repeal.

---

## 32.3 Dynamic Governance Mechanisms (DGMs)

DGMs are the formal pathways through which change becomes legitimate. Each DGM has a scope, a trigger, a decision path, an audit consequence, and a relation to higher-order constraints.

**DGM-Response-Level (Level 0):**
- Scope: one response or one immediate safety decision
- Trigger: BBB filter result, judge signal, truth-verification failure, safety concern
- Process: re-route, block, refine, or constrain the response
- Logging: turn-level and related audit stores
- Review: red-team and ongoing operational review

**DGM-Session-Level (Level 1):**
- Scope: repeated patterns across one conversation or related interaction window
- Trigger: recurrent confusion, decay flags, escalating risk, repeated clarification demand
- Process: extra retrieval, clarification, escalation, or changed response strategy
- Logging: session and memory endpoints
- Review: session-pattern and watchdog review

**DGM-Sprint-Level (Level 2):**
- Scope: thresholds, corpora, schedule changes, token permissions, governance policy revisions
- Trigger: metrics drift, postmortems, community feedback, red-team findings, repeated lower-level events
- Process: formal review and policy change
- Logging: Git, sprint records, constitutional audit artifacts
- Review: each sprint boundary

**DGM-Substrate-Level (Level 2.5 / Code-Level Recurrence):**
- Scope: live service code in `/app/services/`
- Trigger: recurring cron cycle every 30 minutes
- Process: analyze service files, generate patch suggestions via one Ollama coding model, run cascade vote, apply approved patches directly, archive rejected patches
- Logging: cycle log plus rejected-patch archive on host mount
- Review: ex post governance and maintenance review rather than pre-apply human approval

**DGM-System-Level (Level 3):**
- Scope: constitutions, topology, governance architecture, new DGM tiers, major infrastructure reorganization
- Trigger: deep structural change
- Process: explicit governance revision with chapter-wide documentation consequences
- Logging: constitutional versioning and cross-chapter updates
- Review: long-horizon steward governance

A change outside a DGM is drift. A DGM without logs is invisible power. A DGM without boundaries is unaccountable power.

---

## 32.4 Fractal Levels of Optimization

The current system is best described as five interacting optimization levels.

**Level 0 — Single Response:**
One response is shaped, filtered, or blocked in real time. The BBB, ensemble, and judge stack govern this level.

**Level 1 — Session:**
Patterns across a conversation alter how the system retrieves, explains, or escalates. Session-level memory and clarification behavior live here.

**Level 2 — Sprint:**
Accumulated evidence drives changes to schedules, corpora, policy thresholds, and governance rules. This is the conventional planning-and-review level.

**Level 2.5 — Autonomous Code Recurrence:**
A cron-driven Darwin Gödel cycle now operates every 30 minutes. It reads the live codebase under `/app/services/`, calls one coding model (`deepseek-coder:latest`) through Ollama, generates candidate improvements, runs a 4–5 voter cascade, writes approved patches back to the live services directory, and writes rejected ones into `/app/rejected_patches/`.

**Level 3 — System Lifetime:**
Large structural changes alter the meaning of the system’s architecture itself. The move from discussing autonomous code mutation as future work to documenting it as live infrastructure is one such lifetime-level change in the theory of the apparatus.

At every level, the governing pattern remains: **Observe → Evaluate → Change → Record → Re-enter the loop.**

---

## 32.5 DGMs and Constitutional Guardrails

Fractal optimization is bounded by constitutional guardrails. These guardrails do not prevent change; they define which changes count as legitimate.

`allis-constitutional-guardian:8091` remains the highest explicit governance authority inside the application stack. The Caddy `forward_auth` perimeter remains upstream of container logic and therefore outside the reach of normal DGM mutation pathways.

The July 7, 2026 code-level DGM does **not** remove these boundaries. Its autonomy concerns the patch application path, not the abolition of governance. The crucial correction to earlier drafts is therefore not “the human disappeared from governance,” but “the human is no longer in the immediate approve-before-apply loop for low-level code mutation.” Governance still exists at the architectural level, the constitutional level, the cron configuration level, the service-design level, and the audit-review level.

This distinction matters. A fully autonomous patch loop without outer guardrails would be unsafe. A bounded autonomous patch loop inside a larger constitutional apparatus is a governed optimizer, not an unbounded one.

---

## 32.6 Fractal Optimization and Swarm Functions

Fractal optimization is materially implemented by recurring service functions, scheduler events, and maintenance jobs. The Darwin Gödel loop is now one of the clearest examples of a swarm-adjacent governance function that acts repeatedly without waiting for a user prompt.

The live code-level loop is coordinated through cron and `dgm_cycle.sh`, which calls `POST /apply_improvements` on `nbb_darwin_godel_machines`. This makes code revision part of the standing metabolism of the system rather than an occasional manual intervention.

Example recurring autonomous pattern:

```text
cron (every 30 min)
    └── dgm_cycle.sh
            └── POST /apply_improvements
                    └── nbb_darwin_godel_machines
                            ├── read /app/services/
                            ├── generate suggestions via deepseek-coder:latest
                            ├── cascade vote (4–5 voters)
                            ├── approved → write back to /app/services/
                            └── rejected → write to /app/rejected_patches/
```

This loop is supported by maintenance jobs that trim historical output and rotate rejection artifacts. The maintenance layer is therefore part of governance, not merely housekeeping.

---

## 32.7 Place-Aware Governance

Dynamic governance in Ms. Allis is intentionally place-aware, and Chapter 32 must continue to say so even after the addition of autonomous code mutation. The system does not become placeless merely because one of its optimization tiers now modifies code automatically.

The wider apparatus still grounds action in Appalachian data, local resources, community-specific constraints, and geographic accountability. That means code-level self-improvement is legitimate only insofar as it continues serving the place-aware mission established elsewhere in the system.

This matters especially because code-level mutation is powerful. If optimization logic changes the pathways through which resources, retrieval, safety, or speech operate, then place-awareness must still be the criterion by which that optimization is interpreted, audited, and judged.

---

## 32.8 Worked Example — From Suggestion to Applied or Rejected Patch

The July 2026 Darwin Gödel loop provides a concrete worked example of fractal governance acting on live service code.

The system first returned genuine LLM-generated suggestions from live service analysis. Two explicitly observed examples were:
- `ms_jarvis_seamless_monitor` → “Add logs at different levels for better debugging and monitoring.”
- `ms_egeria` → “Use async context for httpx client to avoid blocking the event loop.”

These suggestions were not hardcoded placeholders. They were produced by the configured coding model and returned by `/suggest_improvements` as live observations over the current service files.

A later self-improvement cycle then logged the following pattern:

```text
✅ DGM APPROVED self_improvement_cycle (3 layers passed)
🧬 Self-improvement cycle starting
🧬 3 suggestions received
🧬 ms_jarvis_consciousness_unified_bridge: can_proceed=True safety=0.9666666666666667
✅ ms_jarvis_consciousness_unified_bridge: stage=staged decision=allowed path=/tmp/mutations/ms_jarvis_consciousness_unified_bridge.py.candidate
🧬 ms_jarvis_monitor: can_proceed=False safety=0.9666666666666667
⏭️  ms_jarvis_monitor skipped — Darwin-Gödel verification failed
🧬 ms_egeria_production_chat: can_proceed=False safety=0.9666666666666667
⏭️  ms_egeria_production_chat skipped — Darwin-Gödel verification failed
```

That scheduler excerpt is historically important because it shows the transition state between staged mutation and the final architecture now documented in the session’s corrected DGM documentation. Earlier in the build, approved mutations could be staged to `/tmp/mutations/`; the final updated system description supersedes that staging-only interpretation and documents the current loop as applying approved patches back into `/app/services/` automatically.

Thus the worked example should be read in two phases:

1. **Observed intermediary phase:** approved candidates could be staged, rejected ones were skipped.
2. **Current documented production phase:** approved candidates are applied directly to live service files, rejected candidates persist in the host-mounted rejection archive.

This is precisely the kind of thesis-level correction Chapter 32 should make explicit rather than hide. The record shows the architecture evolving in-session from semi-autonomous mutation flow to a more fully autonomous apply path.

---

## 32.9 Metrics and Feedback Loops

Fractal optimization and DGMs depend on metrics that can trigger governance attention. The code-level loop adds a new class of metrics to the older response-, session-, and sprint-level measures.

| Metric | Baseline / current fact | DGM meaning |
|:--|:--|:--|
| Judge pipeline score | `0.975` April baseline | Lower judge quality increases governance risk |
| LLM ensemble active | 21/22 April baseline | Reduced diversity weakens response-level evaluation |
| `autonomous_learner` commit rate | ~288/day April baseline | Tracks ongoing learning throughput |
| DGM cycle frequency | Every 30 minutes | Defines current substrate-level recurrence |
| Coding model count | 1 model | Avoids multi-model ambiguity in code-generation path |
| Coding model name | `deepseek-coder:latest` | Current live generator for code suggestions |
| Voters per patch | 4–5 | Defines governance depth of patch evaluation |
| Rejected patch retention | Host-mounted and rotated weekly | Makes failed mutation attempts auditable |
| Chat interaction with DGM cycle | None | Confirms decoupling from user chat path |
| Dead-code pruning | Not implemented | Known future hardening step (`vulture`) |

The patch loop now participates in the broader feedback system:

```text
live service files
    ↓
deepseek-coder:latest analyzes code
    ↓
patch suggestions
    ↓
4–5 voter cascade
    ↓
approved → apply to /app/services/
rejected → archive to /app/rejected_patches/
    ↓
cron maintenance and ex post review
```

The most important theoretical change is that this loop now feeds back into the very substrate that produces later observations. The system is therefore no longer only optimizing responses over a mostly fixed implementation; it is optimizing parts of its own implementation recurrently.

---

## 32.10 Implementation Status

| Component | Status | Notes |
|:--|:--|:--|
| Response-level DGM | ✅ Implemented | BBB and judge pathways active |
| Session-level DGM | ✅ Implemented | Session pattern handling and memory pathways active |
| Sprint-level DGM | ✅ Implemented | Policy and corpus revisions remain governed |
| System-level DGM | ✅ Active | Constitution and topology remain higher-order governance levels |
| Autonomous code-level DGM | ★★★ LIVE | `nbb_darwin_godel_machines` now runs as a recurring self-improvement loop |
| Trigger cadence | ★★★ LIVE | Every 30 minutes |
| Coding model strategy | ★★★ LIVE | One Ollama model only: `deepseek-coder:latest` |
| Approved patch path | ★★★ LIVE | Approved patches write back into `/app/services/` |
| Rejected patch path | ★★★ LIVE | Rejected patches write to `/app/rejected_patches/` |
| Rejected-patch durability | ★★★ LIVE | Volume mount to `/mnt/spiritual_drive/msjarvis-rebuild/rejected_patches` |
| Weekly reject rotation | ★★★ LIVE | Host cron deletes `.py` rejects older than 7 days |
| Daily cycle-log trim | ★★★ LIVE | Host cron trims `dgm_cycle.log` to last 1000 lines |
| Chat-triggered DGM cycle | ❌ Not part of architecture | Chat never triggers the code-improvement cycle |
| Chat-error feedback into code DGM | 🔲 Future work | Not yet implemented |
| Dead-code pruning | 🔲 Future work | `vulture` identified as next natural addition |

---

## 32.11 Autonomous Darwin Gödel Loop — July 7, 2026 Rewrite

This section replaces earlier prose that incorrectly retained a human deployment gate in the immediate patch path.

### 32.11.1 Canonical Description

The Darwin Gödel Machine (DGM) is an autonomous self-improvement loop that runs independently of user-facing chat. It periodically reads Ms. Allis’s service files, generates patches via LLM, votes on them, and applies approved changes — all without human intervention.

### 32.11.2 Canonical Architecture

```text
cron (every 30 min)
    └── dgm_cycle.sh
            └── POST /apply_improvements
                    └── nbb_darwin_godel_machines (container port 8302)
                            ├── reads    /app/services/  (←→ host: /mnt/spiritual_drive/msjarvis-rebuild/services/)
                            ├── generates patch via Ollama
                            ├── cascade vote (4–5 voters)
                            ├── approved → writes back to /app/services/
                            └── rejected → writes to /app/rejected_patches/ (←→ host: .../rejected_patches/)
```

### 32.11.3 Key Paths

| Purpose | Container Path | Host Path |
|:--|:--|:--|
| Live service files | `/app/services/` | `/mnt/spiritual_drive/msjarvis-rebuild/services/` |
| Rejected patches | `/app/rejected_patches/` | `/mnt/spiritual_drive/msjarvis-rebuild/rejected_patches/` |
| Cycle log | — | `/mnt/spiritual_drive/msjarvis-rebuild/dgm_cycle.log` |
| Compose file | — | `/mnt/spiritual_drive/msjarvis-rebuild/docker-compose.yml` (line 1152) |

### 32.11.4 Cron Jobs

```bash
# DGM: run improvement cycle every 30 minutes
*/30 * * * * /mnt/spiritual_drive/msjarvis-rebuild/dgm_cycle.sh

# DGM: rotate rejected patches older than 7 days (Sunday 3am)
0 3 * * 0 find /mnt/spiritual_drive/msjarvis-rebuild/rejected_patches -name "*.py" -mtime +7 -delete

# DGM: trim cycle log to last 1000 lines (daily 4am)
0 4 * * * tail -n 1000 /mnt/spiritual_drive/msjarvis-rebuild/dgm_cycle.log > /tmp/dgm_log_trim && mv /tmp/dgm_log_trim /mnt/spiritual_drive/msjarvis-rebuild/dgm_cycle.log
```

### 32.11.5 Cycle Behavior

| Setting | Value |
|:--|:--|
| Cycle frequency | Every 30 minutes |
| Voters per patch | 4–5 |
| Patch merge strategy | AST-boundary (replaces function in-place; appends if not found) |
| Dead code pruning | Not implemented (future: `vulture`) |
| Chat interaction | None — completely independent loop |
| Model strategy | One Ollama model only |
| Coding model | `deepseek-coder:latest` |

### 32.11.6 Verified Runtime Facts

The running container exposed the following environment and mount facts during the session:

```text
SERVICES_DIR=/app/services
CODING_MODEL=deepseek-coder:latest
OLLAMA_URL=http://jarvis-ollama:11434/api/generate
/mnt/spiritual_drive/msjarvis-rebuild/services → /app/services
/mnt/spiritual_drive/msjarvis-rebuild/rejected_patches → /app/rejected_patches
```

These details matter because they settle two ambiguities that earlier drafts handled incorrectly. First, the coding path uses one Ollama model, not an ensemble of coding models. Second, rejected patches are durable across rebuilds because the rejection directory is now host-mounted.

### 32.11.7 What Does Not Happen

- Chat with Ms. Allis does **not** trigger a DGM cycle.
- DGM cycles do **not** interrupt in-flight chat requests.
- There is **no** current feedback loop from chat errors into DGM suggestions.
- The system does **not** rely on a pre-apply human approval gate in the current canonical architecture.

### 32.11.8 Maintenance Notes

- Rejected patches survive container rebuilds via the volume mount added on July 7, 2026.
- The `jarvis-consciousness-scheduler` orphan warning on `docker compose up` is harmless and reflects a renamed or removed service.
- A dead-code pruner such as `vulture` is a natural next addition once a fuller test suite exists.
- A chat→DGM feedback loop is a natural next addition once error-to-service attribution becomes testable and reliable.

### 32.11.9 Theoretical Consequence

With this loop active, Chapter 32 can no longer describe Ms. Allis as merely a system that routes outputs through fractal governance. It must describe Ms. Allis as a system that also recursively modifies parts of its own service substrate through a governed, recurring, inspectable, and now operational Darwin Gödel pathway.

That is the central meaning of the July 7, 2026 rewrite.

---

## Cross-Reference Map

| This section | Cross-chapter reference |
|:--|:--|
| §32.3 response/session/sprint DGM tiers | Ch. 29, Ch. 31, Ch. 33 |
| §32.4 Level 2.5 autonomous code recurrence | Ch. 9 updated DGM chapter |
| §32.5 constitutional guardrails | Ch. 31 §31.7; Ch. 37 constitutional authority |
| §32.6 recurring autonomous loop | Ch. 35 swarm and scheduler logic |
| §32.7 place-aware grounding | Ch. 28 geographic substrate; Ch. 30 local corpora and resources |
| §32.8 worked mutation example | July 2026 Darwin Gödel session record |
| §32.11 canonical autonomous loop | July 7, 2026 DGM documentation state |

---

*Chapter 32 — Fractal Optimization and DGMs*
*Ms. Egeria Allis Steward System — Harmony for Hope, Inc.*
*Mount Hope, West Virginia*
*Last updated: ★★★ 2026-07-07 — Carrie Kidd (Mamma Kidd)*
*★★★ Canonical July 7 state: the code-level Darwin Gödel loop is autonomous, uses one Ollama coding model (`deepseek-coder:latest`), runs every 30 minutes, writes approved patches back to `/app/services/`, archives rejected patches to a host-mounted path, and operates independently of user-facing chat.*
