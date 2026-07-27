# 28. Heartbeat and Live Cycles

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: July 27, 2026*

---

## 28.1 What Chapter 28 Means by "Heartbeat"

In Ms. Allis, **heartbeat** means the repeated live cycle that shows the system is not merely installed, but actively supporting governed reasoning at runtime.

As of the July 26, 2026 architecture closeout, the live heartbeat has two layers:

- The **application-layer heartbeat**: the recurrent epistemic runner that wakes up, checks health across H_t, H_state, Phi, BBB, and the constitutional guardian, and logs what it finds.
- The **database-layer heartbeat**: four pg_cron jobs registered in `wv_gis` that advance the GBIM lifecycle, refresh the public evidence surface, and write audit records to `runtime_governance.public_answer_audit` on a verified, scheduled cadence.

This chapter may claim that the live cycle is operational because both layers are verified as running. The pg_cron job table output from July 26, 2026 is the as-built heartbeat specification for the database layer, and it is reproduced in §28.2.

---

## 28.2 As-Built Heartbeat Specification: The cron.job Table (July 26, 2026)

The following is the actual output from the `cron.job` table in `wv_gis` as of July 26, 2026. These four rows are the live, clock-driven governance cycle. They are not aspirational; they are registered and active.

```
 jobid |       schedule        |                          command                           | nodename  | nodeport | database | username | active | jobname
-------+-----------------------+------------------------------------------------------------+-----------+----------+----------+----------+--------+---------------------------------------------
     1 | 15 * * * *            | SELECT runtime_governance.gbim_runtime_lifecycle_hourly()  | localhost |     5432 | wv_gis   | postgres | t      | gbim-runtime-lifecycle-hourly
     3 | 5 3 * * *             | SELECT runtime_governance.gbim_runtime_lifecycle_daily()   | localhost |     5432 | wv_gis   | postgres | t      | gbim-runtime-lifecycle-daily
     4 | 0 2 * * 0             | SELECT runtime_governance.gbim_runtime_lifecycle_weekly()  | localhost |     5432 | wv_gis   | postgres | t      | gbim-runtime-lifecycle-weekly
     5 | 30 1 $ * *            | SELECT runtime_governance.gbim_runtime_lifecycle_monthly() | localhost |     5432 | wv_gis   | postgres | t      | gbim-runtime-lifecycle-monthly
```

Every field in this output is the as-built specification:

| Field | Meaning |
|---|---|
| `jobid` | Permanent identifier in `cron.job`. IDs 1, 3, 4, 5 confirm these jobs survived any earlier registration gaps (jobid 2 is absent, indicating a prior job was removed). |
| `schedule` | The cron expression that controls when the job fires. |
| `command` | The exact SQL statement executed at each firing. |
| `nodename` / `nodeport` / `database` | Confirms these jobs run on `localhost:5432` in the `wv_gis` database. |
| `username` | Jobs execute as `postgres`, giving them access to `runtime_governance` procedures. |
| `active = t` | All four jobs are active as of July 26, 2026. |
| `jobname` | Human-readable label used in logs and monitoring queries. |

For rural developers, you can re-verify this output at any time with:

```sql
SELECT jobid, schedule, command, active, jobname
FROM cron.job
ORDER BY jobid;
```

If any row shows `active = f`, or if a row is missing, the database-layer heartbeat is degraded and the governance cadence is interrupted.

---

## 28.3 What Each Heartbeat Job Does

Each job advances a different layer of the governance cycle. Their cadence is deliberate and nested: hourly passes catch fast changes, daily passes handle degradation, weekly and monthly passes perform deeper audits.

**Job 1 — Hourly (`15 * * * *`)**
Fires every hour at 15 minutes past the hour. Calls `runtime_governance.gbim_runtime_lifecycle_hourly()`. At each firing it:
- refreshes the `public_admissible_gbim_mv` materialized view so the public evidence surface is never more than one hour stale;
- writes a `refresh_public_admissible_gbim_mv` stage record to `runtime_governance.public_answer_audit` with the current admissible row count and timestamp;
- advances the degradation clock, moving records that have exceeded their freshness window from `fresh` toward `aging`.

**Job 3 — Daily (`5 3 * * *`)**
Fires every day at 03:05. Calls `runtime_governance.gbim_runtime_lifecycle_daily()`. At each firing it:
- marks records as `stale` when they have exceeded the aging window;
- checks for records with missing `spatial_unit_id`, `spatial_unit_kind`, or `valid_time_start` and queues them for backfill;
- writes a `lifecycle_snapshot` stage record to `runtime_governance.public_answer_audit` capturing the full admissibility count breakdown — authorized, admissible, stored-but-inadmissible — at that moment in time.

**Job 4 — Weekly (`0 2 * * 0`)**
Fires every Sunday at 02:00. Calls `runtime_governance.gbim_runtime_lifecycle_weekly()`. At each firing it:
- performs cohort-level review across the governed store, identifying authorized records blocked from public claims, records with provenance gaps, and records stale long enough to warrant governance review;
- writes a weekly audit summary to `runtime_governance.public_answer_audit`.

**Job 5 — Monthly (`30 1 $ * *`)**
Fires at 01:30 on the last day of each month. Calls `runtime_governance.gbim_runtime_lifecycle_monthly()`. At each firing it:
- performs the deepest lifecycle audit: full admissibility counts, degradation trend analysis, promotion gate statistics;
- writes a monthly governance state record to `runtime_governance.public_answer_audit`.

---

## 28.4 Verifying the Heartbeat is Running

For rural developers, the most important operational check is confirming that the four jobs are actually firing on schedule. The `cron.job_run_details` table holds the execution history:

```sql
SELECT jobid, start_time, end_time, status, return_message
FROM cron.job_run_details
ORDER BY start_time DESC
LIMIT 20;
```

A healthy system shows recent `succeeded` rows for jobid 1 (within the last hour), jobid 3 (within the last day), jobid 4 (within the last week), and jobid 5 (within the last month). The significance of each gap:

| Job | Max acceptable gap | What a gap means |
|---|---|---|
| jobid 1 (hourly) | 1 hour | Public evidence surface is stale; admissibility counts have not advanced |
| jobid 3 (daily) | 24 hours | Degradation transitions have not run; `lifecycle_snapshot` audit records are missing |
| jobid 4 (weekly) | 7 days | Cohort review has not run; provenance gap detection is behind |
| jobid 5 (monthly) | ~1 month | Deep audit records are not accumulating; trend analysis is unavailable |

---

## 28.5 The Application-Layer Heartbeat: Recurrent Epistemic Runner

The second layer of the heartbeat is the **recurrent epistemic runner** — the application-level worker that wakes up, checks whether key governance and state services are healthy, and logs what it finds.

In plain terms, one heartbeat pass through the runner is a short route:

1. The recurrent runner wakes up.
2. It checks whether **Hilbert time (H_t)** is healthy.
3. It checks whether **Hilbert state (H_state)** is healthy.
4. It checks whether the **Phi probe** is reachable at the real deployed host mapping.
5. It checks whether **BBB** and the **constitutional guardian** are healthy.
6. It records the result so the system has an audit trail of liveness over time.

If that route is healthy, the live cycle is considered available at the verified scope. If key dependencies fail, the system treats the governed path as degraded.

The recurrent epistemic runner and the four pg_cron jobs are synchronized through `runtime_governance.public_answer_audit` as the shared audit surface: both layers write to it, and both layers can be inspected there.

---

## 28.6 H_t and H_state

Two verified dependencies in this chapter are **H_t** and **H_state**.

- **H_t** is the time-aware layer that helps the system keep track of temporal continuity. It provides the notion of "now" and "then" that the hourly pg_cron job uses to advance the degradation clock.
- **H_state** is the state layer that helps the system retain and expose current runtime condition. It tracks coordination flags and current state snapshots between pg_cron firings.

Heartbeat matters because the runner is not just checking "is one Python file alive?" It is checking whether the **time and state backbone** needed for orderly cycles is healthy between database-layer governance passes.

---

## 28.7 Phi at the Real Port

The closure evidence corrected a stale assumption that Phi lived at an old 8100 address. Chapter 28 claims that the **Phi probe is healthy at its actual deployed host mapping**, not at a superseded port.

For rural developers, the lesson is direct: heartbeat only counts if you verify the service where it **really runs**. A cron job that calls a procedure at the right schedule but depends on a service at a stale address is not a complete heartbeat — it is a scheduled call to a broken path.

---

## 28.8 BBB and Constitutional Guardian

The heartbeat path depends on the governance barrier being alive. The verified runtime scope includes:

- a healthy **BBB**;
- a healthy **constitutional guardian**.

This does not mean every promotion decision is always correct. It only means the governance-facing services that belong in the live cycle were verified as healthy, so the runner's heartbeat can legitimately include them as part of the operational chain.

---

## 28.9 EEG Containers and Runtime Context

The July 26, 2026 closeout confirms that **EEG containers are present**. That supports the runtime picture by showing that the broader live environment around recurring epistemic activity is actually deployed, rather than being described only on paper.

For Chapter 28, that evidence supports the claim of a live-cycle ecosystem without turning the chapter into a claim about clinical cognition, sentience, or unrestricted autonomy. The system has supporting runtime pieces present; the chapter stays limited to **verified live-cycle support**.

---

## 28.10 What Heartbeat Does for Governance

Heartbeat in this chapter is important because it ties system governance to actual runtime availability.

A candidate path that depends on time, state, Phi, BBB, and the constitutional guardian should not be described as fully alive if those services are unavailable. The four pg_cron jobs add a second dimension to this check: a candidate path that depends on the public evidence surface being current should not be described as fully alive if jobid 1 has not fired within the last hour.

Chapter 28 therefore treats heartbeat as a **two-layer runtime honesty check**:

- If the recurrent runner is live and its dependencies are healthy, the application-layer cycle may be described as live.
- If the four pg_cron jobs are active and showing recent `succeeded` rows, the database-layer governance cycle may be described as live.
- If either layer is degraded, the system should be treated as degraded at the governed scope.

This keeps the thesis from confusing "the code exists" with "the live cycle is operational."

---

## 28.11 Checklist for Rural Developers

If you are checking Chapter 28 in the field, use this checklist:

1. Query `SELECT jobid, schedule, active, jobname FROM cron.job ORDER BY jobid` — do you see jobids 1, 3, 4, 5 with `active = t`?
2. Query `cron.job_run_details` — do all four jobs show recent `succeeded` rows within their acceptable gaps (§28.4)?
3. Is the **recurrent epistemic runner** actually running as a process?
4. Does the runner have **reboot/cron registration** so it comes back after restart?
5. Is **H_t** healthy?
6. Is **H_state** healthy?
7. Is the **Phi probe** healthy at the **real deployed port mapping**?
8. Are **BBB** and the **constitutional guardian** healthy?
9. Does `runtime_governance.public_answer_audit` show recent rows from both pg_cron jobs and the runner?

If those answers stay yes, the chapter's verified heartbeat claim is on solid ground.

---

## 28.12 What This Chapter Does Not Claim

Within this gate, Chapter 28 does **not** claim:

- universal safety;
- perfect monitoring;
- unrestricted autonomous authority;
- biological or clinical consciousness;
- that every downstream judgment is correct;
- that the four pg_cron jobs guarantee admissibility — they advance the lifecycle, but admissibility is enforced by the ten-condition predicate in Appendix A, not by the scheduler.

It only claims the verified runtime scope: **a two-layer heartbeat consisting of four registered pg_cron jobs (jobids 1, 3, 4, 5) and a live recurrent epistemic runner, together with their dependent health chain verified on July 26, 2026**.

---

## 28.13 Closing Statement

Chapter 28 presents heartbeat as the system's **repeatable live check** for governed runtime continuity. At the verified July 26, 2026 scope, that means two layers working together:

The **database-layer heartbeat** is the four pg_cron jobs registered in `cron.job` as jobids 1, 3, 4, and 5 — firing at `15 * * * *`, `5 3 * * *`, `0 2 * * 0`, and `30 1 $ * *` — which advance the GBIM lifecycle and write the governance audit trail on a continuous, observable cadence.

The **application-layer heartbeat** is the recurrent epistemic runner with reboot persistence, checking H_t, H_state, Phi at the real deployed host mapping, BBB, and the constitutional guardian on its own repeating schedule.

Both layers write to `runtime_governance.public_answer_audit`. Both layers are verifiable by any operator with access to `cron.job`, `cron.job_run_details`, and the runtime_governance schema.

For rural developers, the core idea is simple: the chapter is about proving that the **live path is actually up and cycling** — with jobids in the database and a runner on the host — not about claiming more intelligence, authority, or certainty than the July 26, 2026 gate verified.

---

*Chapter 28 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
