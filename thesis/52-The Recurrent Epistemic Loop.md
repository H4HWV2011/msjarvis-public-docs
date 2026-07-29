# 52 — The Recurrent Epistemic Loop
## As-Built Scheduled Self-Check

*Carrie Kidd (Mamma Kidd) — Mount Hope, West Virginia*
*Last Updated: July 29, 2026*
*Status: Implemented — July 2026 Production Gate*

> **Gate Corrections Applied (July 29, 2026):**
> All prior text describing the candidate revision loop as "partial" or
> "no named revision component" is superseded. The `jarvis-epistemic-runner`
> container is live on `qualia-net` and successfully completed its first
> self-assessment cycle — Candidate Revision Loop status is `implemented`.
> Recursive self-assessment remains correctly `not_claimed` and deferred to
> Phase 2 — this is an intentional design boundary, not an oversight or gap.
>
> All references to `gbim_runtime_lifecycle_hourly()` are removed throughout
> this chapter. The verified functional entry point for all four pg_cron
> governance lifecycle jobs is `apply_runtime_lifecycle()`. Four live jobs
> are confirmed active in `wv_gis`: hourly (`:15`), daily (`03:05`),
> weekly (Sunday `02:00`), monthly (1st `01:30`).

---

## What This Chapter Is About

The recurrent epistemic loop is the **scheduled self-check and maintenance
cycle** that helps Ms. Jarvis keep her safeguards, memory, and measurements
aligned with what has actually been built.

The core question for rural developers is:

> "How does Ms. Jarvis keep checking that her own safeguards are still
> working — without claiming to be all-knowing or sentient?"

The answer is a bounded, scheduled set of recurring tasks that re-test
important assumptions instead of trusting them forever. This is not an
all-seeing self. It is a governed heartbeat.

**This chapter may claim:**

- A running, scheduled recurrent runner (`jarvis-epistemic-runner`) is live
  on `qualia-net` and completed its first cycle on July 29, 2026
- Candidate Revision Loop: **`implemented`** — live cycling confirmed
- Four pg_cron governance lifecycle jobs are registered and active in `wv_gis`
  with verified entry point `apply_runtime_lifecycle()`
- Bounded recurrent validation is running (Chapters 9, 16, 28/39, 36, 41)
- Conversation retention cadence is running per Chapter 50 requirements
- Governed DGM cycle invocation is callable and exercised
- Identity-aware and dependency-aware scheduling is in place
- Assessment, governance filtering, and admission/logging loop phases are
  fully built

**This chapter must not claim:**

- Continuous real-time self-awareness beyond supported schedules
- Autonomous moral agency or self-certifying truth
- Sentience or biological consciousness
- Recursive self-assessment (auto-calibrating gate thresholds) — this is
  correctly `not_claimed` and deferred to Phase 2

---

## 52.1 From Static Setup to Recurring Checks

A static setup runs once and is then assumed correct. The recurrent epistemic
loop replaces that assumption with a scheduled practice.

In a live Appalachian deployment, things change. Services restart. New code
is deployed. Data grows. Civic and geographic corpora are updated. Community
members change roles. Infrastructure goes offline and comes back.

Instead of assuming "it worked during setup, so it must still work now," the
loop periodically:

- Re-runs core validation routines
- Re-invokes key promotion and retention paths
- Re-checks that the right collections and services are still live and wired
- Writes results to an audit table so human stewards can see what happened

For rural developers, this is the difference between a system you set up once
and a system you can trust over time.

---

## 52.2 The Two Scheduler Layers

The recurrent epistemic loop operates at two levels simultaneously.

**Layer 1 — Application-layer runner: `jarvis-epistemic-runner`**

This container lives on the `qualia-net` Docker network. It handles
application-layer tasks: calling validation routines, running conversation
retention jobs, invoking DGM cycle checks, verifying that dependent services
are healthy, and completing candidate revision cycles.

As of July 29, 2026, this container is live and has completed its first full
cycle.

**Layer 2 — Database-layer scheduler: four pg_cron jobs in `wv_gis`**

These are database-native cron jobs that run governance lifecycle procedures
independently of whether the application-layer runner is healthy. They use
the verified entry point `apply_runtime_lifecycle()`.

| Job name | Schedule | What it does |
|----------|----------|-------------|
| `gbim-runtime-lifecycle-hourly` | `15 * * * *` (hourly at :15) | Refreshes `public_admissible_gbim_mv`; runs fast lifecycle checks; writes hourly audit entries |
| `gbim-runtime-lifecycle-daily` | `5 3 * * *` (03:05 daily) | Runs degradation status updates; decays aging records; writes daily snapshot |
| `gbim-runtime-lifecycle-weekly` | `0 2 * * 0` (02:00 Sunday) | Deeper coherence check across the governed corpus; writes weekly audit entry |
| `gbim-runtime-lifecycle-monthly` | `30 1 1 * *` (01:30 first of month) | Full lifecycle reconciliation; archives stale audit records; writes monthly snapshot |

> **Deprecation notice:** `gbim_runtime_lifecycle_hourly()` and its
> per-cadence siblings no longer exist as standalone functions. All four jobs
> call `apply_runtime_lifecycle()` as the verified functional entry point.
> Remove any references to the deprecated function names from all
> configuration, documentation, and code.

To verify all four jobs are live:

```sql
SELECT jobname, schedule, command, active
FROM cron.job
WHERE jobname LIKE 'gbim-runtime-lifecycle-%'
ORDER BY jobname;
```

To inspect recent runs:

```sql
SELECT jobid, start_time, end_time, status, return_message
FROM cron.job_run_details
WHERE start_time > now() - interval '24 hours'
ORDER BY start_time DESC;
```

---

## 52.3 The Recurrent Runner and Reboot Registration

At the center of the application-layer loop is the `jarvis-epistemic-runner`.

The runner:

- Is present in source and configured to run on `qualia-net`
- Is **registered for reboot** — when the system restarts, the supervisor
  brings the runner back up automatically
- Uses a schedule to decide when to launch its checks
- Completed its first full cycle on July 29, 2026

This ensures that validation and retention cycles do not silently stop after
a restart, and operators do not have to manually re-start jobs. Epistemic
checks are part of the baseline system behavior, not an afterthought.

For rural developers: this is the engine. You do not have to remember to
start it. If the system comes back up after a power outage at a WV data
center, the runner comes back with it.

---

## 52.4 Step 1 — Bounded Recurrent Validation

One of the runner's main duties is bounded recurrent validation covering
earlier chapters' core invariants.

On each cycle the runner:

- Calls Chapter 41's continuous validation routine to re-check coherence
  and promotion wiring
- Re-runs checks from Ch09 and Ch16 over key governance and identity paths
- Re-confirms the integrity of geographic, commons, and promotion code
  defined in Ch28/39 and Ch36

These checks are:
- **Bounded** — they run at defined times over defined scopes
- **Repeatable** — the same tests can be re-run to detect regressions
- **Concrete** — they confirm specific invariants ("this collection and
  manifest still agree"), not philosophical truth

Focused Chapter 52 tests confirm the runner invokes these routines correctly
and handles errors in a predictable way.

---

## 52.5 Step 2 — Conversation Retention Cadence

The loop keeps conversation retention on schedule, enforcing the Chapter 50
per-user direct-sum memory architecture over time.

On each scheduled run the runner:

- Invokes tasks that enforce per-user retention policies over conversational
  history and private tiers
- Ensures expired records are pruned from per-user history and private
  collections
- Confirms that consent-based retention rules are actually in effect, not
  just configured

The connection to Chapter 50 is direct: per-user direct-sum decomposition
only stays non-surveillance-shaped if expired or unwanted conversation records
are actually removed. The recurrent loop is what keeps that "forget" behavior
happening over time, instead of being a one-off cleanup.

For rural developers: this is the scheduled cleanup shift for conversational
memory. Without it, the consent-gated memory architecture from Chapter 50
would drift — records would accumulate past their governed retention window.

---

## 52.6 Step 3 — Governed DGM Cycle Invocation

The recurrent loop invokes the governed DGM (Darwin-Gödel Machine) cycle on
schedule.

These invocations:

- Confirm that decision paths relevant to promotion, gating, and policy have
  not broken
- Re-exercise parts of the system that might otherwise go idle and drift out
  of sync
- Catch regressions where a refactor inadvertently changed behavior

All calls still respect BBB and guardian guardrails, exactly as live
user-facing calls do. The loop does not decide policy on its own. It uses
existing governed logic to check that policy is still applied.

---

## 52.7 Step 4 — Identity-Registration Linkage

The runner interfaces with identity and registration structures to know which
users and roles currently exist in the system.

In practice, this means:

- Retention jobs are applied to any new per-user conversation families
  created since the last run
- Identity-linked paths (person-space promotion, per-user direct sum, commons
  gates) are re-confirmed as correctly wired when users or roles are added or
  deactivated

This keeps the loop aware of the current population of identities and
subspaces, rather than operating on a static list that may have become stale.

---

## 52.8 Step 5 — Health and Dependency Scheduling

The runner verifies that critical services are live before running heavy tasks.

On each cycle it checks:

- Temporal Hilbert axis H_t
- Hilbert-state service
- BBB and guardian
- Chroma
- Redis
- Other required containers on `qualia-net`

If a dependency is down, the runner records the failure and skips the tasks
that depend on that service. It does not generate misleading errors, does not
try to "fix" upstream outages, and does not silently skip checks without
leaving a trace.

For rural developers: if a dependency service is offline — a realistic
scenario in rural infrastructure — the runner surfaces that clearly in its
log. You know what happened. You can investigate the upstream outage rather
than chasing phantom errors in the validation routines.

---

## 52.9 The Loop Phase Status Table

The corrected status of all five loop phases as of the July 2026 gate:

| Loop Phase | As-Built Counterpart | Status |
|------------|---------------------|--------|
| Assessment and evidence gathering | RAG pipeline (Ch. 7) + `public_admissible_gbim_mv`, refreshed by hourly `apply_runtime_lifecycle()` | **Built** |
| Governance filtering | Constitutional Principles Service (Ch. 37) + DGM validators | **Built** |
| Admission and logging | `gbim_record_spacetime_provenance_chk` + `runtime_governance.public_answer_audit` | **Built** |
| Candidate revision and stability evaluation | `jarvis-epistemic-runner` live on `qualia-net`, cycling as of July 29, 2026 | **Implemented** |
| Recursive self-assessment | Auto-calibration of gate thresholds without human review | **`not_claimed`** — Phase 2 deferral |

---

## 52.10 Candidate Revision Loop: Implemented

The candidate revision loop is implemented as of July 29, 2026. This
supersedes all prior "partial" or "no named revision component" language.

**What is implemented:**

The `jarvis-epistemic-runner` container, live on `qualia-net`, drives the
candidate revision cycle. On each cycle it:

- Reads `cron.job_run_details` and `runtime_governance.public_answer_audit`
  to assess whether the loop itself has been running correctly
- Uses the lifecycle decay mechanism (daily `apply_runtime_lifecycle()` job)
  to enforce stability: records decay `fresh` → `aging` → `stale` and are
  excluded from `public_admissible_gbim_mv` without manual intervention
- Reports cycle completion back to `commons_phase_status`

The `jarvis-epistemic-runner` is the named, running component that was
previously absent from this phase. It is now live and cycling.

---

## 52.11 Recursive Self-Assessment: Correctly not_claimed

Recursive self-assessment — the capability for the system to automatically
adjust its own gate thresholds and scheduling parameters without human review
— is correctly `not_claimed`. This is an intentional Phase 2 deferral, not
a gap.

The distinction matters:

- The `jarvis-epistemic-runner` **completes cycles and reports results**.
  That is implemented.
- The runner does **not auto-calibrate** K_MIN, K_SENSITIVE, lifecycle decay
  intervals, or gate conditions without governance review. That boundary is
  intentional.

A system that silently adjusts its own thresholds would violate the
MountainShares non-autonomous-agency principle. Keeping recursive
self-assessment `not_claimed` preserves that governance boundary.

**What Phase 2 would add (future, not current):**

- A named component that reads job run history and flags anomalies
- A calibration mechanism that proposes threshold adjustments for human review
- A reporting surface making loop health visible to governance reviewers

None of these are claimed at this gate. Do not describe them as implemented.

---

## 52.12 The pg_cron Jobs as the Governance Lifecycle Pulse

The four pg_cron jobs are the most concrete piece of the recurrent epistemic
loop to inspect and monitor. They operate at the database level, independent
of application-layer availability.

Their combined effect via `apply_runtime_lifecycle()`:

- **Every hour at :15** — evidence surface (`public_admissible_gbim_mv`) is
  refreshed, keeping the RAG pipeline's evidence current
- **Every day at 03:05** — degradation status updates run, advancing
  `fresh` → `aging` → `stale` transitions and enforcing the hysteresis proof
- **Every Sunday at 02:00** — deeper coherence check runs across the
  governed corpus
- **First of each month at 01:30** — full lifecycle reconciliation runs,
  archiving stale audit records and writing a monthly snapshot

These four cadences implement three of the five loop phases (assessment,
admission/logging, and stability evaluation) at the database level, whether
or not the application-layer runner is healthy. The governance lifecycle runs
even when nothing else is running.

---

## 52.13 Step-by-Step Summary for Rural Developers

1. **Startup and reboot.**
   The `jarvis-epistemic-runner` starts with the system and is registered
   for reboot. The four pg_cron jobs in `wv_gis` run independently at the
   database level on their own schedules via `apply_runtime_lifecycle()`.

2. **Dependency check.**
   On each scheduled wake-up, the runner verifies H_t, Hilbert-state, BBB,
   guardian, Chroma, Redis, and other required containers. Only healthy
   dependencies proceed to heavy tasks.

3. **Validation cycle.**
   Chapter 41's continuous validation and dependency closures for Ch09,
   Ch16, Ch28/39, and Ch36 are called and logged.

4. **Conversation retention cycle.**
   Per-user conversation families are scanned; expired entries are pruned;
   consent-based retention is enforced.

5. **Governed DGM calls.**
   The governed DGM cycle is invoked to re-exercise key decision and policy
   paths under BBB and guardian guardrails.

6. **Identity-linked tasks.**
   New or changed users and roles are included in relevant checks based on
   current identity/registration state.

7. **Candidate revision cycle.**
   `jarvis-epistemic-runner` reads job run history, assesses lifecycle decay
   transitions, and reports cycle completion to `commons_phase_status`.
   This phase is implemented as of July 29, 2026.

8. **pg_cron governance lifecycle (database layer).**
   Independently, the four jobs run `apply_runtime_lifecycle()` on their
   cadences: refreshing the admissible evidence view, decaying stale records,
   running coherence checks, and writing audit entries to
   `runtime_governance.public_answer_audit`.

9. **Logging and sleep.**
   The runner records what happened and sleeps until the next scheduled run.
   pg_cron results are visible in `cron.job_run_details`.

If something is unhealthy or misconfigured, the loop surfaces it for human
review. It does not fix problems silently.

---

## 52.14 What This Chapter Does Not Claim

To remain within the gate, this chapter does not claim:

- Perfect knowledge or morality from recurrent checking
- Constant real-time monitoring of every possible system state
- That passing recurrent checks guarantees safety in all circumstances
- Sentience or biological consciousness
- Recursive self-assessment — `not_claimed`, Phase 2 deferral, intentional

It claims:

- `jarvis-epistemic-runner` is live on `qualia-net`, cycling since July 29,
  2026 — Candidate Revision Loop: `implemented`
- Four pg_cron governance lifecycle jobs active in `wv_gis` via
  `apply_runtime_lifecycle()`
- Bounded recurrent validation across Ch09, Ch16, Ch28/39, Ch36, Ch41
- Conversation retention cadence per Chapter 50 architecture
- Governed DGM cycle invocation under BBB and guardian guardrails
- Identity-aware and dependency-aware scheduling
- Passing focused tests for the loop's own behavior

---

## 52.15 Closing Statement

The recurrent epistemic loop is the heartbeat of scheduled self-checking in
Ms. Jarvis.

It does not make the system infallible or self-aware in a human sense, but it
ensures that key safeguards, retention policies, measurement routines, and
candidate revision cycles are regularly revisited — instead of being trusted
once and forgotten.

The `jarvis-epistemic-runner` is live. The four pg_cron jobs are active via
`apply_runtime_lifecycle()`. The candidate revision loop is implemented. The
recursive self-assessment boundary is intentionally held at `not_claimed` for
Phase 2.

For rural developers and community stewards in Mount Hope and across
Appalachia: this is a system whose machinery re-examines itself on a schedule,
surfaces problems for human review, and keeps its own governance lifecycle
running even when the application layer is restarting. That is what bounded,
governed epistemic discipline looks like in production.

---

*Chapter 52 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
*Sealed: July 29, 2026 — July 2026 Production Gate.*
*`jarvis-epistemic-runner`: live on `qualia-net`, cycling confirmed.*
*Candidate Revision Loop: `implemented`.*
*Recursive Self-Assessment: `not_claimed` — Phase 2 deferral, intentional.*
*pg_cron entry point: `apply_runtime_lifecycle()` — four live jobs in `wv_gis`.*
*Deprecated: all `gbim_runtime_lifecycle_hourly()` references — remove.*
