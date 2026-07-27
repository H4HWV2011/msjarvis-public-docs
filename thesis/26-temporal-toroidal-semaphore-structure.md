# 26. Temporal Toroidal Semaphore Structure

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: July 27, 2026*

---

## 26.1 Why This Matters for Polymathmatic Geography

This chapter explains how Ms. Allis regulates **time and cycles** so that reasoning, validation, promotion, and retention happen in **bounded intervals** instead of as instant, fire-and-forget writes. It shows how temporal structure acts as part of governance, not just plumbing — and names the four live pg_cron jobs that are the clock-driven heartbeat of that governance cycle as of July 26, 2026.

It supports:

- **P1 – Every where is entangled** by tying time, reasoning, gating, and memory into one coupled system instead of treating them as separate.
- **P3 – Power has a geometry** by giving authority transitions a temporal shape: whether something may advance depends on *when* and *for how long* it stays stable.
- **P5 – Design is a geographic act** by treating timing layers — semaphores, windows, retries, and hysteresis — as part of the system's map.
- **P12 – Intelligence with a ZIP code** by letting local reasoning unfold inside bounded sessions without forcing immediate system-wide consequences.
- **P16 – Power accountable to place** by making temporal promotion observable and bounded rather than letting state jump straight from thought to lasting effect.

This chapter belongs to the **Computational Instrument** tier. It describes the **as-built temporal governance layer** over Ms. Allis.

---

## 26.2 The Four Live pg_cron Jobs: The Clock-Driven Governance Cycle

The most concrete expression of the temporal toroidal semaphore in the running system is the four pg_cron jobs registered in `wv_gis` as of July 26, 2026. These jobs are the **clock-driven governance cycle**: they are not aspirational cron entries, they are running schedules that advance the GBIM lifecycle, refresh the public evidence surface, and write audit records to `runtime_governance.public_answer_audit` on a repeating cadence.

| Job name | Schedule (cron) | Plain-English cadence | Procedure |
|---|---|---|---|
| `gbim-runtime-lifecycle-hourly` | `15 * * * *` | Every hour at :15 past | `runtime_governance.gbim_runtime_lifecycle_hourly()` |
| `gbim-runtime-lifecycle-daily` | `5 3 * * *` | Every day at 03:05 | `runtime_governance.gbim_runtime_lifecycle_daily()` |
| `gbim-runtime-lifecycle-weekly` | `0 2 * * 0` | Every Sunday at 02:00 | `runtime_governance.gbim_runtime_lifecycle_weekly()` |
| `gbim-runtime-lifecycle-monthly` | `30 1 $ * *` | Last day of each month at 01:30 | `runtime_governance.gbim_runtime_lifecycle_monthly()` |

These four schedules are the **toroidal** part of the temporal semaphore: the system continuously cycles through hourly, daily, weekly, and monthly governance passes, each one layered on top of the others. No governance decision happens in a single instant — it happens inside a mesh of repeating intervals. For rural developers, you can verify these jobs are registered by querying:

```sql
SELECT jobname, schedule, command, active
FROM cron.job
WHERE jobname LIKE 'gbim-runtime-lifecycle-%'
ORDER BY jobname;
```

And you can inspect their recent execution history with:

```sql
SELECT jobid, start_time, end_time, status, return_message
FROM cron.job_run_details
ORDER BY start_time DESC
LIMIT 20;
```

---

## 26.3 What Each Job Does in the Governance Cycle

Each of the four jobs advances a different layer of the temporal governance cycle. Their granularity is deliberate: fine-grained hourly passes catch rapid admissibility changes; daily passes handle degradation and backfill; weekly and monthly passes perform deeper lifecycle audits.

**Hourly (`15 * * * *`):** Refreshes the `public_admissible_gbim_mv` materialized view, writes a `refresh_public_admissible_gbim_mv` stage record to `runtime_governance.public_answer_audit`, and advances the degradation clock on fresh records that are aging toward stale. This is the shortest semaphore interval: it ensures the public evidence surface is never more than one hour out of date.

**Daily (`5 3 * * *):** Runs at 03:05 each morning. Performs deeper lifecycle transitions — marking records as stale when they have passed the freshness window, triggering backfill checks for records with missing `spatial_unit_id`, `spatial_unit_kind`, or `valid_time_start`, and writing a `lifecycle_snapshot` audit record capturing the full admissibility count breakdown at that point in time.

**Weekly (`0 2 * * 0`):** Runs at 02:00 every Sunday. Performs cohort-level review across the entire governed store — identifying records that are authorized but blocked from public claims, records with provenance gaps, and records that have been stale long enough to warrant governance review. Writes a weekly audit summary to `runtime_governance.public_answer_audit`.

**Monthly (`30 1 $ * *`):** Runs at 01:30 on the last day of each month. Performs the deepest lifecycle audit: full admissibility counts, degradation trend analysis, promotion gate statistics, and a summary record written to `runtime_governance.public_answer_audit` for that month's governance state.

---

## 26.4 What the Temporal Semaphore Does (General)

The **temporal toroidal semaphore structure** is the timing framework that controls when:

- a sandbox session can run;
- validation checks happen;
- promotion windows open or stay closed;
- retries or holds are allowed;
- a candidate must expire or roll back.

You can think of it as a **traffic light plus calendar** for internal reasoning:

- green: you may proceed to the next gate;
- yellow: hold or retry;
- red: stop or roll back;
- clock: these lights change on a schedule tied to system heartbeat and Hilbert-time.

The four pg_cron jobs are the clock. Without them, the temporal semaphore has no heartbeat — governance checks would be one-time events rather than the repeating cycle that gives the toroidal structure its name.

It is **not** a promise of perfect monitoring or real-time determinism. It is a practical timing mesh that keeps important steps from collapsing into one instant.

---

## 26.5 Live Time and State Services

Chapter 26 builds on live services that are already running:

- **Hilbert-time service** on a dedicated port with:
  - ephemeral Redis for short-term slices;
  - staged Redis for near-term windows;
  - historical Postgres for longer records.

- **Hilbert-state service** with Redis attached, tracking current state snapshots and coordination flags.

These services give the semaphore layer:

- a notion of **"now"** and **"then"**;
- a way to tell **ephemeral** from **staged** from **historical** data;
- a way to check whether a candidate has stayed stable across an interval instead of just at one instant.

They are part of the "toroidal" idea: the system cycles through time slices, but keeps enough memory of the loop to reason about stability. The four pg_cron jobs in §26.2 are what drive the Postgres side of this loop — the durable, auditable half of the temporal mesh.

---

## 26.6 Sandbox Sessions as Timed Intervals

A **sandbox session** is a **timed interval** of internal reasoning.

For each session, the temporal layer tracks:

- when it **starts**;
- how long active deliberation runs;
- when **validation checkpoints** occur;
- whether a **retry window** is open;
- when a **promotion window** opens (if at all);
- when the session must **expire** or roll back.

Step-by-step, a typical session looks like:

1. A task is routed into the sandbox and gets a time-stamped session ID.
2. The session runs reasoning steps inside a bounded interval.
3. Validation checks fire at planned times — for example, at the end of a reasoning phase.
4. If checks fail but the state is promising, a **retry/hold** period is opened.
5. If checks pass and the state stays stable, a **promotion window** can open.
6. If windows close or time runs out, the session either finishes without promotion or rolls back.

The hourly pg_cron job is the fastest external clock the sandbox respects: within a given hour, a session may run and validate; the next hourly tick will find its effects reflected in the refreshed materialized view.

---

## 26.7 Gating Cycles Over Time

A **gating cycle** is the timed sequence a candidate goes through on its way to possible promotion.

One cycle can be sketched as:

1. **Acquire a semaphore slot** for a given candidate or session.
2. Run internal reasoning for that slot's active interval.
3. Hit a **validation checkpoint** (truth, guardian, coherence, etc.).
4. Decide whether to:
   - **proceed** toward promotion;
   - **hold** and inspect again later;
   - **retry** with more context;
   - **terminate** or roll back.
5. If strong enough and within timing constraints, enter a **promotion window**.
6. Either commit to a broader layer or let the window close.

The "toroidal" part is that cycles can repeat: a candidate may circle back through more than one pass, but always under timing rules instead of looping freely. The four pg_cron schedules define the walls of those cycles: hourly for fast feedback, daily for degradation, weekly for cohort review, monthly for deep audit.

---

## 26.8 Hysteresis and Stability (Preventing Flapping)

The temporal structure includes **hysteresis**: the system does not change its mind too quickly on small perturbations.

Applied here:

- a candidate is not allowed to bounce rapidly between "ready" and "not ready" just because of very small perturbations;
- once a candidate crosses into an admissible state, it must stay acceptable long enough — across at least one hourly cycle — before a promotion window fully opens;
- once it is judged unstable, it may need to re-earn admissibility across a meaningful interval.

This prevents **flapping**, where the system would otherwise:

- promote a candidate on one tick;
- retract or overturn it on the next;
- promote again on the third.

Hysteresis requires **stability over time**, not just a single lucky check. In practice, this means a record's `degradation_status` must remain `fresh` or `aging` across at least one full hourly pass before it enters the publicly admissible surface — a property enforced by the interaction between the hourly job and the ten-condition predicate in Appendix A.

---

## 26.9 Recurrent Epistemic Runner

A **recurrent epistemic runner** is registered and live. It is responsible for:

- regularly polling health and gate-state surfaces;
- triggering **recurrent checks** on DGM cycles, BBB, guardian, and other components;
- feeding its findings back into continuous validation and timing decisions.

In practical terms, the runner:

- makes sure checks happen **again and again** at safe intervals;
- ensures that temporal windows are driven by current information instead of stale status;
- writes logs so operators can see a history of how gates and health looked over time.

The recurrent epistemic runner operates at the application layer; the four pg_cron jobs in §26.2 operate at the database layer. Together they are the two-layer heartbeat of the system: application-level polling and database-level scheduled governance, synchronized through `runtime_governance.public_answer_audit` as the shared audit surface.

---

## 26.10 Links to DGM and Continuous Validation

Chapter 26 leans on two important prior closures:

- **Chapter 09 DGM closure.** Shows that DGM self-modification is bounded: immutable targets and low-score proposals are rejected, and rollbacks are verified.
- **Chapter 41 continuous validation closure.** Shows that core health, sandbox dependencies, guardian schemas, DGM run cycles, and classification invariants are watched over time.

The temporal semaphore layer **hooks into these** by:

- scheduling or pacing DGM cycles within the daily and weekly pg_cron windows;
- ensuring DGM changes are considered only within defined temporal boundaries;
- coordinating continuous validation checks so they occur at predictable times aligned with the four-cadence governance cycle;
- reflecting validation outcomes in whether promotion windows stay open or close before the next scheduled tick.

Time, here, is part of the guardrail: DGM and validation don't fire arbitrarily; they are woven into the timing mesh defined by `15 * * * *`, `5 3 * * *`, `0 2 * * 0`, and `30 1 $ * *`.

---

## 26.11 What the Temporal Layer Does Not Claim

Within this gate, Chapter 26 does **not** claim:

- perfect monitoring;
- real-time determinism;
- a mathematical proof of all future states;
- total absence of stale containers;
- universal safety;
- legal or clinical guarantees;
- sentience or biological consciousness;
- that the four pg_cron jobs are sufficient on their own — they drive governance cadence, but the admissibility decisions they invoke are enforced by the ten-condition predicate in Appendix A, not by the scheduler alone.

It only claims:

- **implemented timing structure** over gate cycles and promotion windows;
- **four named, verified pg_cron schedules** that are the live clock-driven governance cycle;
- **bounded state transition checks** driven by Hilbert-time/state, DGM closure, and continuous validation;
- **monitorable behavior** via `runtime_governance.public_answer_audit`, health endpoints, and `cron.job_run_details`.

The temporal semaphore is a strong safety scaffold — not a guarantee.

---

## 26.12 Step-by-Step View for Rural Developers

From a rural developer's perspective, the temporal layer works like this:

1. **The four pg_cron jobs are the clock.** They fire at `15 * * * *` (hourly), `5 3 * * *` (daily), `0 2 * * 0` (weekly), and `30 1 $ * *` (monthly last-day). You can verify they are active in `cron.job` and inspect their run history in `cron.job_run_details`.

2. **Hilbert-time and Hilbert-state** keep track of the finer-grained "when" and "what's going on now" at the Redis layer, inside each hourly window.

3. **The recurrent epistemic runner** wakes up on its own application-layer schedule, checks health, DGM, guardian, and other components, and feeds findings into the same governance surfaces the pg_cron jobs write to.

4. **Sandbox sessions** run only inside time-bounded slots. Their effects are not visible in the public evidence surface until the next hourly pg_cron tick refreshes `public_admissible_gbim_mv`.

5. **Validation checkpoints** happen at specific times aligned with the governance cadence, not randomly.

6. **Promotion windows** open only when a candidate has stayed coherent and admissible long enough to survive at least one full hourly cycle.

7. **Hysteresis** makes sure the system doesn't flicker between promote and rollback on small wobbles across consecutive hourly ticks.

8. **`runtime_governance.public_answer_audit`** gives you a durable trail of what each pg_cron job found and did when it ran. You can read the `lifecycle_snapshot` stage rows to see exactly how the admissibility counts changed from one governance pass to the next.

For day-to-day operations in a rural deployment, the most important thing to verify is that all four pg_cron jobs show recent `succeeded` rows in `cron.job_run_details`. A gap in the hourly job means the public evidence surface may be stale; a gap in the daily job means degradation transitions have not advanced; a gap in the weekly or monthly jobs means cohort and deep audit records are not accumulating.

---

## 26.13 Closing Statement

The temporal toroidal semaphore structure gives Ms. Allis a **time-aware backbone** for safe decision-making. Sandbox sessions, gate cycles, retries, promotion windows, hysteresis, and recurrent checks all work together so that internal reasoning cannot instantly become lasting consequence without surviving **time-based scrutiny**.

The four pg_cron jobs — firing at `15 * * * *`, `5 3 * * *`, `0 2 * * 0`, and `30 1 $ * *` — are the live, clock-driven governance cycle that makes this backbone operational. They are not background plumbing: they are the temporal semaphore in motion, advancing the GBIM lifecycle, refreshing the public evidence surface, and writing the audit trail that makes every governance decision traceable to a specific moment in time.

This chapter therefore seals time itself as part of the governance architecture: not a passive backdrop, but an active set of semaphores with verified schedules that say when the system may think, when it must wait, and when it is finally allowed to act.

---

*Chapter 26 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
