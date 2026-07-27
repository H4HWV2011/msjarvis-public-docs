# 52. The Recurrent Epistemic Loop — As-Built Scheduled Self-Check

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: July 27, 2026*

---

## 52.0 Overview

The recurrent epistemic loop is the **scheduled self-check and maintenance cycle** that helps Ms. Allis keep her safeguards, memory, and measurements aligned with what has actually been built.

It describes how the system, on a schedule, re-runs key validations, retention jobs, and governed decision cycles while remaining accountable to constitutional limits, identity and locality rules, and the per-user and commons architectures defined in earlier chapters. This is **not** an all-seeing, all-knowing self; it is a bounded set of recurring tasks that re-test important assumptions instead of trusting them forever.

As of July 27, 2026, the recurrent epistemic loop has a second scheduler layer: **four pg_cron jobs** registered in `wv_gis` that run governance lifecycle procedures on hourly, daily, weekly, and monthly cadences. The Implementation Status Addendum in §52.14 maps each theoretical loop phase to its as-built counterpart and gives an honest accounting of what is built, what is partial, and what remains future work.

---

## 52.1 From Static Setup to Recurring Checks

A static setup runs once and then is assumed correct. The recurrent epistemic loop replaces that with **recurring checks**.

In a live deployment, things change:

- services are restarted;
- new code is deployed;
- data grows and evolves;
- civic and geographic corpora are updated.

Instead of assuming that "it worked once, so it must still work," Ms. Allis uses a small runner that periodically:

- re-runs core validation routines;
- re-invokes key promotion/retention paths;
- re-checks that the right collections and services are still live and correctly wired.

This turns epistemic discipline into a **scheduled practice**, not a one-time event.

---

## 52.2 Components of the As-Built Loop

The as-built recurrent loop has several concrete pieces:

- **Recurrent runner process**
  A long-lived worker that wakes up on a schedule to run checks.

- **pg_cron governance lifecycle jobs**
  Four database-level cron jobs registered in `wv_gis` (hourly, daily, weekly, monthly) that run `runtime_governance` procedures. These are the database-layer scheduler complement to the application-layer runner.

- **Validation jobs**
  Tasks such as Chapter 41's continuous validation and other chapter-specific checks.

- **Conversation retention jobs**
  Scheduled runs that enforce per-user retention and pruning for conversational memory.

- **Governed DGM cycle invocation**
  Calling the governed decision-making cycle to confirm that gates still operate correctly.

- **Dependency health checks**
  Verifying that \(H_t\), Hilbert-state, BBB, guardian, Chroma, Redis, and required containers are live.

- **Dependency closures**
  Bundled routines that know how to re-exercise Ch09, Ch16, Ch28/39, Ch36, and Ch41 in a controlled way.

Focused tests for this loop are also present and passing, so the runner itself has been checked.

---

## 52.3 The Recurrent Runner and Reboot Registration

At the center of the loop is a **recurrent epistemic runner**.

The runner:

- is present in source and configured to run;
- is **registered for reboot**, meaning that when the system restarts, the runner is brought back up by the supervisor;
- uses a schedule (think cron-like intervals) to decide when to launch its checks.

This ensures that:

- validation and retention cycles do **not silently stop** after a restart;
- operators do not have to remember to re-start each job manually;
- epistemic checks are part of the **baseline system behavior**, not an afterthought.

For rural developers, this is the "engine" that keeps all the periodic testing and cleanup tasks actually happening.

---

## 52.4 Bounded Recurrent Validation (Ch41 and Others)

One of the runner's main duties is **bounded recurrent validation**.

Evidence for this includes:

- Chapter 41's continuous validation is scheduled;
- dependency closures for Ch09, Ch16, Ch28/39, Ch36, and Ch41 are present;
- focused tests confirm the runner can call these routines.

In practice, on each cycle the runner may:

- call the Chapter 41 validation routine to re-check things like coherence and promotion wiring;
- re-run checks from Ch09 and Ch16 over key governance and identity paths;
- re-confirm the integrity of geographic, commons, and promotion code defined in Ch28/39 and Ch36.

These checks are:

- **bounded** — they run at defined times, over defined scopes;
- **repeatable** — the same tests can be re-run to see if anything has regressed.

Rather than certifying "truth" in the philosophical sense, these jobs confirm that **concrete invariants** (like "this collection and manifest still agree") hold over time.

---

## 52.5 Conversation Retention Cadence

The loop also keeps **conversation retention** on schedule.

The gate confirms that conversation retention is "scheduled or running," which in practice means that the runner:

- periodically invokes tasks that enforce **per-user retention policies** over conversational history and private tiers;
- ensures expired records are pruned from per-user history/private collections;
- confirms that **consent-based retention** rules (from the direct-sum memory chapter) are actually in effect, not just configured.

This connects directly to Chapter 50:

- per-user direct-sum decomposition only stays non-surveillance-shaped if expired or unwanted conversation records are **really removed**;
- the recurrent loop is what keeps that "forget" behavior happening over time, instead of being a one-off cleanup.

For rural developers, this is the scheduled "cleanup shift" for conversational memory.

---

## 52.6 DGM Governed Cycle Invocation

The recurrent loop can also **invoke the governed DGM cycle**.

The gate states that the DGM cycle contract "remains callable," which implies:

- the runner has access to a **governed decision-making routine** described in earlier chapters;
- on schedule, it can call that routine in a controlled way;
- any calls still respect **BBB and guardian guardrails**, just like live user-facing calls.

These invocations are used to:

- confirm that decision paths relevant to promotion, gating, and policy have not broken;
- re-exercise parts of the system that might otherwise go idle and drift out of sync;
- catch regressions where a refactor inadvertently changed behavior.

The loop does **not** decide policy on its own. It uses existing governed logic to **check** that policy is still applied.

---

## 52.7 Identity-Registration Linkage

The recurrent loop interfaces with identity and registration structures to know **which users and roles exist**.

In practice, the runner:

- uses that information to decide which per-user subspaces need retention or validation;
- ensures that new or changed identities are included in the next round of relevant checks.

Examples include:

- applying retention jobs to any new per-user conversation families created since the last run;
- ensuring that identity-linked paths (such as person-space promotion, per-user direct sum, and commons gates) are still wired correctly when users or roles are added or deactivated.

This keeps the loop aware of the **current population** of identities and subspaces, rather than operating on a static list.

---

## 52.8 Health and Dependency Scheduling

The runner relies on a set of **critical services** and verifies that they are live before running heavy tasks.

The gate lists:

- temporal Hilbert axis \(H_t\);
- Hilbert-state service;
- BBB and guardian;
- Chroma;
- Redis;
- other required containers.

On each scheduled cycle, the runner:

- checks that these services are reachable and responsive;
- only proceeds with validations or retention runs if dependencies are healthy;
- records failures when any dependency is down so operators can investigate.

This prevents the loop from:

- generating misleading errors because a base service was offline;
- trying to "fix" problems that are actually **upstream outages**;
- silently skipping checks without leaving a trace.

---

## 52.9 Focused Tests for the Loop Itself

The gate confirms that **focused Chapter 52 tests pass**.

These tests focus on:

- whether the runner **starts correctly**;
- whether it **invokes the intended tasks** (validation, retention, DGM calls) when scheduled;
- whether it respects dependency checks (for example, does not run certain tasks if a required service is down);
- whether it **handles errors and logging** in a predictable way.

This is important: the self-check loop itself must be tested, or else it could fail silently. Passing tests indicate that the basic scheduling and dispatch behavior is working as designed at this gate.

---

## 52.10 Bounded, Not Always-On, Self-Checking

The recurrent epistemic loop at this gate is explicitly **bounded and scheduled**, not an always-on self-awareness layer.

The scope explicitly does **not** include:

- continuous real-time execution beyond supported schedules;
- fully autonomous moral agency;
- self-certifying truth or universal safety;
- sentience or biological consciousness.

In concrete terms:

- the runner wakes at defined times, runs its list of tasks, then sleeps;
- it operates within **well-defined intervals and scopes**;
- human operators and community governance remain responsible for higher-level oversight.

The loop is better understood as **periodic maintenance and validation**, not as a mind constantly inspecting itself.

---

## 52.11 Step-by-Step View for Rural Developers

Putting it all together, the as-built recurrent epistemic loop runs like this:

1. **Startup and reboot.**
   - The runner process starts with the system and is registered to come back after a reboot.
   - The four pg_cron jobs are registered in `wv_gis` and run independently of the application-layer runner on their own database-level schedules.

2. **Dependency check.**
   - On each scheduled wake-up, the runner verifies that temporal Hilbert, Hilbert-state, BBB, guardian, Chroma, Redis, and other required containers are live.

3. **Validation cycle.**
   - It calls Chapter 41's continuous validation and other bound validation routines (Ch09, Ch16, Ch28/39, Ch36), logging any failures.

4. **Conversation retention cycle.**
   - It runs retention jobs over per-user conversation families, pruning expired entries and enforcing consent-based retention.

5. **Governed DGM calls.**
   - It may invoke the governed DGM cycle to re-exercise key decision and policy paths.

6. **Identity-linked tasks.**
   - It uses identity/registration linkage to ensure new or changed users and roles are included in relevant checks.

7. **pg_cron governance lifecycle jobs (database layer).**
   - Independently, on their own schedules, the four pg_cron jobs run `runtime_governance` lifecycle procedures: refreshing the admissible materialized view, decaying stale records, and writing lifecycle snapshots to `runtime_governance.public_answer_audit`.

8. **Logging and sleep.**
   - The runner records what happened, then sleeps until the next scheduled run.
   - pg_cron results are visible in `cron.job_run_details`.

If something is unhealthy or misconfigured, the loop's purpose is not to fix it silently, but to **surface it regularly** so humans can see and address it.

---

## 52.12 What This Chapter Does Not Claim

To stay within the gate, this chapter does **not** claim that:

- the loop can guarantee perfect knowledge or morality;
- the system constantly monitors every possible state in real time;
- passing recurrent checks guarantees safety in all circumstances;
- the system is conscious or sentient;
- candidate revision/stability evaluation and recursive self-assessment are fully implemented (see §52.14).

It only claims:

- a running, scheduled recurrent runner;
- **four pg_cron governance lifecycle jobs** at database level;
- **bounded recurrent validation**;
- **conversation retention cadence**;
- governed **DGM cycle invocation**;
- **identity-aware and dependency-aware scheduling**;
- passing tests for the loop's own behavior at this gate.

---

## 52.13 Closing Statement

The recurrent epistemic loop, as built today, is the **heartbeat of scheduled self-checking** in Ms. Allis.

It does not make the system infallible or self-aware in a human sense, but it does ensure that key safeguards, retention policies, and measurement routines are regularly revisited instead of being trusted once and forgotten. For rural developers and community stewards, this provides a clear, inspectable structure for how the system keeps **re-examining its own machinery** over time, within carefully bounded and governed limits.

The pg_cron jobs add a second, database-native layer to this heartbeat. They run whether or not the application-layer runner is healthy, providing an independent governance lifecycle pulse that keeps the admissible evidence surface fresh and the audit trail current.

---

## 52.14 Implementation Status Addendum — Loop Phases As-Built (July 27, 2026)

This addendum maps each theoretical phase of the recurrent epistemic loop to its as-built counterpart in the live system. It uses the two-register discipline from Appendix A: **built** means a real path has been exercised and confirmed; **partial** means some components are running but a named gap remains; **future** means the design is understood but end-to-end implementation has not begun.

---

### 52.14.1 The Four pg_cron Jobs — The Live Scheduler

The database-level scheduler for the recurrent epistemic loop consists of four pg_cron jobs registered in `wv_gis`. These jobs run `runtime_governance` procedures on independent schedules and do not depend on the application-layer runner being healthy.

| Job name | Schedule | Procedure | What it does |
|---|---|---|---|
| `gbim-runtime-lifecycle-hourly` | `15 * * * *` (hourly, at :15) | `runtime_governance.gbim_runtime_lifecycle_hourly()` | Refreshes `public_admissible_gbim_mv`; runs fast lifecycle checks; writes hourly audit entries to `runtime_governance.public_answer_audit` |
| `gbim-runtime-lifecycle-daily` | `5 3 * * *` (03:05 daily) | `runtime_governance.gbim_runtime_lifecycle_daily()` | Runs full degradation status updates; decays aging records; promotes or demotes rows based on lifecycle rules; writes daily snapshot |
| `gbim-runtime-lifecycle-weekly` | `0 2 * * 0` (02:00 Sunday) | `runtime_governance.gbim_runtime_lifecycle_weekly()` | Runs deeper coherence checks across the governed corpus; writes weekly audit entry |
| `gbim-runtime-lifecycle-monthly` | `30 1 1 * *` (01:30 first of month) | `runtime_governance.gbim_runtime_lifecycle_monthly()` | Runs full lifecycle reconciliation; archives stale audit records; writes monthly snapshot |

These four jobs are the **live scheduler** for the governance lifecycle layer of the recurrent epistemic loop. They operate at the database level, independent of application-layer services. A rural developer can verify they are registered by running:

```sql
SELECT jobname, schedule, command, active
FROM cron.job
WHERE jobname LIKE 'gbim-runtime-lifecycle-%'
ORDER BY jobname;
```

And can inspect recent runs via:

```sql
SELECT jobid, start_time, end_time, status, return_message
FROM cron.job_run_details
WHERE start_time > now() - interval '24 hours'
ORDER BY start_time DESC;
```

---

### 52.14.2 Loop Phase: Assessment and Evidence Gathering — **Built**

**Theoretical role:** The loop's first phase is to gather current evidence about the state of the governed epistemic corpus — what records exist, which are admissible, and what the current governed state looks like.

**As-built counterpart:**

- **RAG pipeline (Chapter 7)** provides the retrieval-augmented generation layer: evidence is retrieved from the governed corpus before any answer is generated. The pipeline queries `public_admissible_gbim_mv` as its authoritative evidence source.
- **`public_admissible_gbim_mv`** (93,423 rows, `degradation_status = 'fresh'`) is the materialized view that is refreshed by `gbim-runtime-lifecycle-hourly` on each cycle, keeping the evidence surface current.
- The hourly pg_cron job is the scheduled assessment trigger: every hour at :15, it re-evaluates which rows pass the ten-condition admissibility predicate and refreshes the view accordingly.

**Status: Built.** Both the RAG pipeline and the admissible evidence view are live. The hourly pg_cron job is the scheduled driver of evidence freshness.

---

### 52.14.3 Loop Phase: Governance Filtering — **Built**

**Theoretical role:** Before any candidate answer or promoted record is admitted, it must pass governance filters that enforce constitutional principles and policy constraints.

**As-built counterpart:**

- **Constitutional Principles Service (Chapter 37)** is the live governance filter. It enforces the constitutional constraints that no answer, promotion, or commons output may violate. It is called as part of the governance pathway before candidates are admitted.
- **DGM validators** are the governed decision-making validators that enforce promotion gates, coherence checks, and policy constraints at the candidate level. They implement the formal promotion contract (trigger → evaluator → procedure) described in Appendix A §A.9.

**Status: Built.** The Constitutional Principles Service is live. DGM validators are running and have been exercised on real manifests including negative tests.

---

### 52.14.4 Loop Phase: Admission and Logging — **Built**

**Theoretical role:** Once a candidate passes assessment and governance filtering, it must be admitted into the governed store and its admission must be logged for audit purposes.

**As-built counterpart:**

- **`runtime_governance.public_answer_audit`** is the live audit table. Every lifecycle snapshot, public answer packet, and governance lifecycle job result is written here. The four pg_cron jobs write their run results to this table on each scheduled execution.
- The `gbim_record_spacetime_provenance_chk` CHECK constraint (Appendix A §A.3) enforces admission conditions at the schema level: a row cannot be admitted as authorized and publicly claimable without satisfying all spatial, temporal, and provenance requirements.
- Admission is logged both at the row level (via `ingested_at`, `promotion_state`, and `degradation_status` columns on `gbim_record`) and at the audit level (via `runtime_governance.public_answer_audit`).

**Status: Built.** Admission and logging are running. `runtime_governance.public_answer_audit` is populated by each pg_cron job run and by `runtime_governance.public_answer_packet` calls.

---

### 52.14.5 Loop Phase: Candidate Revision and Stability Evaluation — **Partial**

**Theoretical role:** The loop should evaluate whether candidate records are stable over time — whether a record that was admitted last week still deserves to be admitted today, whether its evidence basis has changed, and whether it should be revised or demoted.

**As-built counterpart:**

- **DGM gates handle the promotion and demotion decision logic.** The lifecycle decay mechanism (degradation from `fresh` to `aging` to `stale` via the daily pg_cron job) is the primary stability enforcement mechanism. A record that was once fresh and admissible will eventually decay to `stale` and be excluded from `public_admissible_gbim_mv` without requiring a manual intervention.
- The daily and weekly pg_cron jobs run degradation status updates, which implement a form of scheduled stability evaluation: every 24 hours, the system re-evaluates which records remain in a stable enough state to be publicly admissible.

**Gap — hysteresis needs a named component:** The lifecycle decay implements hysteresis at the row level (a record cannot jump directly from `fresh` to `stale`; it must pass through `aging`). However, there is no currently named component that performs **candidate-level revision** — that is, no component that looks at a set of candidate records, compares them against new evidence, and decides whether a previously admitted record should be revised in light of updated information. The DGM gates handle the gate (admit or don't), and lifecycle decay handles the expiry (how long a record stays admissible), but the loop phase of "examine this previously admitted record in light of new evidence and decide if it needs to change" does not yet have a named, running component.

**Status: Partial.** Lifecycle decay (daily pg_cron job) and DGM gates provide stability enforcement and expiry. A named candidate revision component that re-evaluates previously admitted records against updated evidence is not yet implemented.

---

### 52.14.6 Loop Phase: Recursive Self-Assessment — **Future Phase 2**

**Theoretical role:** In its most ambitious form, the recurrent epistemic loop would include a phase where the system assesses its own loop — examining whether the loop itself is functioning correctly, whether its schedules are appropriate, and whether its gate conditions are still calibrated to current deployment needs.

**As-built status:** This phase is **Future Phase 2**. The current loop performs self-checking in a bounded sense: focused Chapter 52 tests verify that the runner starts, invokes tasks, and handles errors. The pg_cron jobs write to `cron.job_run_details` so failures are visible. But there is no component that examines the loop's own behavior over time and recommends adjustments to schedules, thresholds, or gate conditions based on observed patterns.

**What Phase 2 would add:**

- a named component that reads `cron.job_run_details` and `runtime_governance.public_answer_audit` over time and flags anomalies (for example, a job that consistently takes longer than expected, or a phase that is consistently producing zero admissions);
- a calibration mechanism that could propose adjustments to lifecycle decay intervals or k-threshold values based on observed corpus behavior;
- a reporting surface that makes the loop's own health visible to human governance reviewers.

**Status: Future Phase 2.** This is understood architecturally but has not been scoped for implementation. It will be opened after the candidate revision component (§52.14.5) is named and built.

---

### 52.14.7 Loop Phase Status Summary

| Loop Phase | Theoretical Role | As-Built Counterpart | Status |
|---|---|---|---|
| Assessment and evidence gathering | Gather current evidence about governed corpus state | RAG pipeline (Ch. 7) + `public_admissible_gbim_mv`, refreshed by hourly pg_cron job | **Built** |
| Governance filtering | Enforce constitutional and policy constraints on candidates | Constitutional Principles Service (Ch. 37) + DGM validators | **Built** |
| Admission and logging | Admit passing candidates and write audit record | `gbim_record_spacetime_provenance_chk` + `runtime_governance.public_answer_audit` | **Built** |
| Candidate revision and stability evaluation | Re-evaluate admitted records against updated evidence | Lifecycle decay (daily pg_cron) + DGM gates (expiry and demotion); **no named revision component** | **Partial** |
| Recursive self-assessment | Loop examines its own behavior and calibrates | Not yet implemented | **Future Phase 2** |

---

### 52.14.8 The pg_cron Jobs as the Governance Lifecycle Pulse

For rural developers, the four pg_cron jobs are the most concrete piece of the recurrent epistemic loop to inspect and monitor. They do not require the application-layer runner to be healthy; they run at the database level on their own schedules.

Their combined effect is:

- **every hour**: the evidence surface (`public_admissible_gbim_mv`) is refreshed, keeping the RAG pipeline's evidence current;
- **every day at 03:05**: degradation status updates run, advancing `fresh` → `aging` → `stale` transitions and enforcing the hysteresis proof;
- **every Sunday at 02:00**: a deeper coherence check runs across the governed corpus;
- **on the first of each month at 01:30**: a full lifecycle reconciliation runs, archiving stale audit records and writing a monthly snapshot.

These four cadences implement three of the five loop phases (assessment, admission/logging, and stability evaluation) at the database level, independent of application-layer availability. The governance lifecycle runs even when nothing else is running.

---

*Chapter 52 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
