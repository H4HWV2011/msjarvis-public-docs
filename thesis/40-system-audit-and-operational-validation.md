# 40. System Audit and Operational Validation

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: July 27, 2026*

---

## 40.1 Why Audit and Validation Matter

This chapter explains how Ms. Allis is checked from the outside, over time, to see whether she actually behaves the way the architecture says she should. It describes **system audit** and **operational validation** as tools for rural communities and operators, not just for researchers in distant labs.

Audit and validation matter because a system can have beautiful gates on paper and still behave badly in practice. This chapter shows how to look at Ms. Allis as a whole — her packets, pipelines, and platform health — and confirm that the governed design from earlier chapters is truly in force.

As of the July 26, 2026 architecture closeout, the **live system audit artifact** is the `runtime_governance.public_answer_audit` table. It has four columns: `audit_id`, `stage`, `detail jsonb`, and `created_at`. Two confirmed rows were written to this table during the July 26 session — one at 19:44:05 recording the materialized view refresh, and one at 19:44:06 recording the lifecycle snapshot. These are the first entries in the operational audit record and serve as the proof that the audit system is working. They are documented in full in §40.5 below.

For rural developers, this chapter answers a practical question:

**"If we say Ms. Allis is governed, how can someone prove it by looking at records and metrics instead of just trusting us?"**

---

## 40.2 Gate-Constrained Scope

This chapter stays within a strict scope.

It may claim that:

- Ms. Allis exposes enough internal structure — logs, metrics, and audit records — to support technical audit and validation;
- operators can follow clear steps to review how governed candidate flows, gates, and health checks behave;
- system audits can detect mismatches between the intended architecture and actual behavior;
- operational validation can show whether Ms. Allis meets her stated design commitments in real-world operation;
- the `runtime_governance.public_answer_audit` table, with its two confirmed July 26 rows, is the live operational proof that the audit system is functioning.

It may **not** claim that:

- a completed audit proves Ms. Allis is morally right, legally sufficient, or politically legitimate;
- successful operational validation turns Ms. Allis into a certified medical device, financial institution, or public authority;
- audit and validation eliminate the need for human oversight, community governance, or legal review;
- audit automatically grants rights, personhood, or spiritual standing.

Within this gate, audit and operational validation are treated as **technical and procedural** tools that help people understand and manage Ms. Allis. They are instruments of transparency and accountability, not declarations of ultimate correctness.

---

## 40.3 What "System Audit" Means Here

In this context, a **system audit** is a structured review of how Ms. Allis has behaved over some period of time, based on evidence that can be inspected: audit table rows, logs, metrics, configuration, and example packets.

A system audit asks questions such as:

- Did packets actually pass through staging, evaluation, emission, and promotion as described?
- Were constitutional and consent checks applied where they were supposed to be?
- Did external communication, memory, and spatial/temporal subsystems use their governed candidate flows?
- Were emergency checks and cleanup mechanisms triggered when required?
- Does the `runtime_governance.public_answer_audit` table contain rows that match the claimed governance events?

The goal is not to embarrass the system or its operators. The goal is to verify that the **implemented behavior matches the documented architecture**, especially in rural deployments where trust is hard-earned and easily lost.

For rural developers, a system audit is like checking the town's financial records and road usage logs. You are asking:

- Did we spend the money where we said we would?
- Are trucks actually following the posted routes?
- Are weight limits and safety rules being respected?

The `runtime_governance.public_answer_audit` table is the ledger that answers those questions for the database-layer governance cycle.

---

## 40.4 What "Operational Validation" Means Here

**Operational validation** is a form of testing that happens under real or realistic conditions, not just in a lab. It asks whether Ms. Allis, when running normally, still meets her design commitments.

Operational validation asks questions such as:

- Do first-stage evaluation gates behave as expected when real users send messy, varied requests?
- Do packet-level readiness scores and approval rates stay within reasonable ranges?
- Do temporal tiers and memory gates prevent premature or unauthorized promotion?
- Does external communication still respect consent, channel, and content-class rules in actual usage?
- Do governance functions write to `runtime_governance.public_answer_audit` on each execution, as demonstrated by the July 26 session?

The aim is to show that the system is not only structured correctly but also **behaving correctly when used by real people in real places**.

For rural developers, operational validation feels like test-driving a vehicle on the roads it will actually travel. It is not enough for the truck to pass a factory inspection. It must also handle West Virginia hills, weather, and load patterns.

---

## 40.5 The Live Audit Artifact: runtime_governance.public_answer_audit

The `runtime_governance.public_answer_audit` table is the live system audit artifact for the database-layer governance cycle. It was established as part of the July 26, 2026 runtime governance migration and has the following structure:

```sql
CREATE TABLE runtime_governance.public_answer_audit (
    audit_id   serial PRIMARY KEY,
    stage      text        NOT NULL,
    detail     jsonb,
    created_at timestamptz NOT NULL DEFAULT now()
);
```

### The Two Confirmed Audit Rows

On July 26, 2026, two rows were written to this table during the live governance session. These are the first entries in the operational audit record and are the proof that the audit system is working.

**Row 1 — Materialized View Refresh**

| Field | Value |
|---|---|
| `audit_id` | 1 |
| `stage` | `'refresh_mv'` |
| `detail` | `{"admissible_count": 93423, "total_gbim_rows": 237655, "inadmissible_count": 144232}` |
| `created_at` | `2026-07-26 19:44:05 EDT` |

This row was written by `runtime_governance.refresh_public_admissible_gbim_mv()` when it refreshed the `public_admissible_gbim_mv` materialized view. The `detail` jsonb records the three counts that define the state of the public evidence surface at that moment: 237,655 total governed rows in `public.gbim_record`, 93,423 admissible for public claims (all ten conditions of Definition A.1 satisfied), and 144,232 stored but inadmissible.

**Row 2 — Lifecycle Snapshot**

| Field | Value |
|---|---|
| `audit_id` | 2 |
| `stage` | `'lifecycle_snapshot'` |
| `detail` | `{"fresh_count": ..., "aging_count": ..., "stale_count": ..., "snapshot_taken_at": "2026-07-26T19:44:06-04:00"}` |
| `created_at` | `2026-07-26 19:44:06 EDT` |

This row was written one second later by the lifecycle snapshot function as part of the same governance pass. The `detail` jsonb records the degradation tier distribution — how many governed rows were classified as `fresh`, `aging`, and `stale` at the time of the snapshot. The `snapshot_taken_at` field inside the jsonb is the system clock at execution, confirming real-time operation.

### What These Two Rows Prove

These two rows are not illustrative examples. They are the actual rows in the live `runtime_governance.public_answer_audit` table as of the July 26, 2026 architecture closeout. Their existence proves three things:

1. The `runtime_governance` schema and the `public_answer_audit` table were successfully created and are writable.
2. The governance functions `refresh_public_admissible_gbim_mv()` and the lifecycle snapshot function executed successfully and committed their audit records.
3. The `detail jsonb` column carries structured, queryable evidence about the governance state at the time of each operation — this is not a plain text log entry but a structured record that supports programmatic audit queries.

For rural developers, this is the answer to "show me the proof." The proof is in rows 1 and 2 of `runtime_governance.public_answer_audit`.

### Querying the Audit Table

To inspect the current state of the audit record:

```sql
-- View all audit rows in order
SELECT audit_id, stage, detail, created_at
FROM runtime_governance.public_answer_audit
ORDER BY created_at ASC;

-- Inspect the admissibility counts from the most recent refresh
SELECT detail
FROM runtime_governance.public_answer_audit
WHERE stage = 'refresh_mv'
ORDER BY created_at DESC
LIMIT 1;

-- Compare successive lifecycle snapshots for drift
SELECT
  audit_id,
  created_at,
  (detail->>'fresh_count')::int   AS fresh,
  (detail->>'aging_count')::int   AS aging,
  (detail->>'stale_count')::int   AS stale
FROM runtime_governance.public_answer_audit
WHERE stage = 'lifecycle_snapshot'
ORDER BY created_at ASC;
```

As the four pg_cron jobs begin firing on their schedules (jobids 1, 3, 4, 5 registered in `cron.job`), they will write additional rows to this table. The `refresh_mv` stage will accumulate an hourly record of admissibility counts; the `lifecycle_snapshot` stage will accumulate a daily record of degradation tier distribution. Over time, these rows become the continuous audit trail of how the governed evidence surface changes.

---

## 40.6 Foundations: What Must Be Visible to Auditors

For audit and validation to be meaningful, certain things must be visible.

At minimum, auditors and operators must be able to see:

- **Audit table rows** in `runtime_governance.public_answer_audit` that match claimed governance events with timestamps and structured `detail` jsonb;
- **Packet-level traces** that show staging, evaluation, emission, and promotion decisions, with identifiers and timestamps;
- **Gate outcomes** for governed candidate systems (cognition, spatial, temporal, memory, communication), including approval, suppression, and review states;
- **Configuration snapshots** that describe relevant thresholds, allowed roles, permitted uses, and consent requirements at the time of operation;
- **Platform health metrics** that show whether gate services and databases were actually available;
- **Event logs** for emergency cleanup, rejection reasons, and unusual error conditions.

If these data are not available, then audit and validation become guesswork rather than grounded examination.

For rural developers, this means that from day one, Ms. Allis must be deployed with:

- the `runtime_governance.public_answer_audit` table receiving rows from every governance function execution;
- logging;
- metrics;
- configuration versioning;
- time-stamped records of gate decisions.

It is far easier to design for auditability up front than to bolt it on later. The two confirmed July 26 rows demonstrate that this design principle was honored in the initial build.

---

## 40.7 Step-by-Step System Audit for Rural Operators

This section gives a concrete, step-by-step audit procedure that a rural operator or trusted community partner can follow.

### Step 1: Define the audit window and scope

Decide:

- which time period to examine (for example, the last 30 days);
- which subsystems to include (for example, cognition packets and external communication only, or the full stack);
- which questions you want to answer (for example, "Did the governance functions execute and write audit rows during this period?").

Write this down before you start. A clear scope helps avoid confusion later.

### Step 2: Start with runtime_governance.public_answer_audit

Before examining packet traces or gate logs, query the audit table:

```sql
SELECT audit_id, stage, created_at, detail
FROM runtime_governance.public_answer_audit
WHERE created_at BETWEEN '[window_start]' AND '[window_end]'
ORDER BY created_at ASC;
```

The audit table is the authoritative record that governance functions ran and committed their results. If audit rows are missing for a period when the pg_cron jobs should have fired, that absence is itself an audit finding — something prevented the governance cycle from executing or writing its record.

### Step 3: Gather supporting evidence

Collect:

- logs of staging, evaluation, emission, and promotion calls for the chosen window;
- gate decision logs for spatial, temporal, memory, and communication candidates as needed;
- system health logs and metrics;
- configuration files or snapshots that show thresholds and permissions active during the window;
- `cron.job_run_details` rows for the same period (see Chapter 39) to cross-check that pg_cron fired the jobs that produced the audit rows.

### Step 4: Verify packet lifecycle behavior

For a sample of packets in the audit window, check:

- that each packet was staged before evaluation;
- that evaluation logs exist and include status, errors, warnings, and readiness scores;
- that only approved packets proceeded to emission or promotion;
- that no packet was written directly into a durable layer without gate records.

If any packet appears to have bypassed the lifecycle, flag it for deeper investigation.

### Step 5: Check gate consistency

For each governed candidate subsystem in scope, examine:

- the reasons for suppression, review, approval, or promotion;
- whether required consent flags were present when durable or external actions occurred;
- whether forbidden metadata keys or disallowed roles were correctly blocked;
- whether the gate behaved consistently across similar cases.

### Step 6: Cross-check with platform health

Review platform health metrics for the audit window:

- If gate services were down or in degraded mode, did traffic stop or route to safe fallback behavior?
- Were emergency cleanup paths triggered, and if so, were they justified?
- Did operators bypass governance during outages, or did they respect the separation between governed and ungoverned behavior?

The goal is to confirm that governance mechanisms were not quietly sidestepped in the name of "keeping things running."

### Step 7: Document findings and recommended actions

Summarize:

- which checks passed;
- which checks failed or raised concerns;
- what immediate remediation steps are needed (configuration fixes, bug corrections, training updates);
- what structural changes might be needed for future robustness.

Document this in clear language that both technical and non-technical community members can understand.

For rural developers, these seven steps form a workable audit loop. It is a way to answer, with evidence, whether Ms. Allis has acted within her own design discipline. The audit table is the starting point because it is the most direct evidence: if the governance functions ran, there are rows; if there are no rows, investigate why.

---

## 40.8 Step-by-Step Operational Validation

Operational validation uses similar tools but focuses on behavior under normal load and over longer periods.

### Step 1: Define expected behaviors and thresholds

For each subsystem, define what "good behavior" looks like, such as:

- a reasonable range of first-stage approval rates;
- a maximum acceptable rate of gate errors;
- minimum evidence requirements for approvals;
- a maximum acceptable lag between event and temporal promotion;
- a minimum expected row count in `runtime_governance.public_answer_audit` for any given 24-hour period (at least one `refresh_mv` row per hour from jobid 1, at least one `lifecycle_snapshot` row per day from jobid 3).

These expectations should be documented and tied back to the design chapters.

### Step 2: Collect continuous metrics

Configure Ms. Allis to emit continuous metrics about:

- gate decisions (approved, suppressed, review);
- readiness score distributions;
- deduplicated evidence counts;
- promotion rates into durable tiers;
- external communication candidate outcomes;
- system health indicators (uptime, latency, error rates);
- the `admissible_count` trend from successive `refresh_mv` rows in `runtime_governance.public_answer_audit`.

The `admissible_count` trend is especially valuable: if it drops unexpectedly between two hourly audit rows, the governance cycle may have demoted records that should remain admissible, or a schema change may have broken the ten-condition predicate.

### Step 3: Compare actual behavior to expected thresholds

Over a chosen validation period, compare actual metrics to the expectations set in Step 1:

- Are approval rates within the expected band?
- Are error types and rates acceptable?
- Are promotion rates stable and justifiable?
- Are external communication decisions matching the intended pattern of caution?
- Does `runtime_governance.public_answer_audit` show the expected cadence of `refresh_mv` and `lifecycle_snapshot` rows?

If not, identify whether the mismatch is due to misconfigured thresholds, flawed gate logic, unexpected usage patterns in the community, or upstream changes in data or models.

### Step 4: Run scenario-based checks

Design and execute specific scenarios, such as:

- a batch of low-evidence packets;
- a set of consent-missing memory candidates;
- spatial candidates outside the allowed geography;
- external communication candidates with and without public opt-in;
- a manual call to `runtime_governance.refresh_public_admissible_gbim_mv()` followed by a check that a new `refresh_mv` row appears in `runtime_governance.public_answer_audit` within seconds.

The last scenario is the simplest end-to-end validation of the audit system: call the function, confirm the row. If no row appears, the audit path is broken.

### Step 5: Close the loop

Use what you learn from operational validation to:

- adjust thresholds and configurations;
- improve documentation and training for operators;
- refine metrics and logging so future validation is easier.

For rural developers, operational validation is not a one-time ceremony. It is an ongoing discipline of checking, comparing, and adjusting based on actual usage patterns.

---

## 40.9 Relationship Between Audit, Validation, and Governance

Audit and operational validation sit alongside the governance mechanisms described in earlier chapters.

- **Governance** defines what should happen: the gates, candidate schemas, consent rules, and temporal tiers.
- **Operational evaluation** (Chapter 39) watches how those mechanisms behave in day-to-day running, with `cron.job_run_details` as the primary operational artifact.
- **System audit** checks past behavior against governance design and commitments, with `runtime_governance.public_answer_audit` as the primary audit artifact.
- **Operational validation** tests whether the system continues to meet its commitments under real conditions.

Together, they form a loop:

1. Design governed architecture.
2. Operate under that architecture.
3. Observe behavior and metrics.
4. Audit past behavior using `runtime_governance.public_answer_audit`.
5. Validate ongoing operation.
6. Adjust configuration and design where needed.

The two confirmed July 26 audit rows — `refresh_mv` at 19:44:05 and `lifecycle_snapshot` at 19:44:06 — are the first two entries in that loop. They prove that step 4 is not hypothetical: the audit record exists, it is queryable, and it captures structured evidence about governed behavior at a specific moment in time.

For rural developers, that loop is the main protection against quiet drift and unmanaged complexity. It keeps Ms. Allis answerable to both her own design and the communities she serves.

---

## 40.10 Limits and Responsibilities

Even with audit and operational validation in place, some responsibilities remain outside the system.

System audit and operational validation do **not**:

- absolve operators, institutions, or communities of responsibility for how Ms. Allis is used;
- replace legal, ethical, or community review boards;
- provide automatic compliance with any specific regulation without additional work;
- guarantee that no harm can occur;
- make two rows in `runtime_governance.public_answer_audit` a substitute for full external review — they are the starting point, not the conclusion.

They **do**:

- make it easier to see and correct problematic patterns;
- provide evidence for discussions with regulators, communities, and researchers;
- reduce the risk of silent failure modes;
- create a durable, queryable record of how Ms. Allis has behaved over time — starting with the two confirmed rows from July 26, 2026.

For rural communities, the message is clear: the system is built to be **inspectable**. It will not be perfect, but it is designed so that its behavior leaves traces that can be audited and its operation can be validated. The `runtime_governance.public_answer_audit` table is where those traces begin.

---

## 40.11 Closing Statement

System audit and operational validation are the final pillars of Ms. Allis' accountable design. They ensure that staged, evaluated, emitted, and promoted packets can be traced, that gates can be examined, and that platform health is part of the story rather than an invisible assumption.

The `runtime_governance.public_answer_audit` table is the live system audit artifact for the database-layer governance cycle. Its four columns — `audit_id`, `stage`, `detail jsonb`, and `created_at` — capture the what, the when, and the structured evidence of every governance function execution that writes to it. On July 26, 2026, two rows were confirmed in this table: a `refresh_mv` row at 19:44:05 and a `lifecycle_snapshot` row at 19:44:06. These are not examples. They are the actual first entries in the operational audit record, and they prove the audit system is working.

For rural developers, these tools transform Ms. Allis from a black box into an instrument that can be examined, questioned, and improved. Audit and validation do not make her infallible, but they do make her accountable in a concrete, technical way that honors both the architecture and the communities that live with it.

---

*Chapter 40 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
