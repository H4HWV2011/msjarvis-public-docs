# 39. Operational Evaluation

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: July 27, 2026*

---

## 39.1 Why Operational Evaluation Matters

This chapter explains how Ms. Allis evaluates her behavior as a whole system in day-to-day operation. Operational evaluation watches the gates, not just the packets that pass through them.

It connects directly to the Polymathmatic Geography principles that say power has a geometry, intelligence must be accountable to place, and systems must not quietly slide from experiment to authority. Operational evaluation is the layer where those principles are measured in practice.

As of the July 26, 2026 architecture closeout, the **primary operational evaluation artifact** for the database-layer governance cycle is the `cron.job_run_details` table in `wv_gis`. This table accumulates a `succeeded` or `failed` row for every firing of the four pg_cron jobs (jobids 1, 3, 4, 5). It was empty as of July 26, 2026 — no executions had yet occurred — but it is the designated record of automated learning and operational behavior once the jobs begin firing on their scheduled cadences. That table and its role are detailed in §39.5 below.

For rural developers, this chapter answers a simple question:

**"Once all these governed packets and gates exist, how do we tell if the whole machine is behaving the way it should?"**

---

## 39.2 Gate-Constrained Scope

This chapter stays within a narrow and concrete academic scope.

This chapter may claim that:

- operational evaluation measures how often governed candidate flows behave as designed;
- operational evaluation uses packet-level metrics (like approval rates and deduplicated evidence), higher-level platform metrics (like system health and uptime), and the pg_cron execution history in `cron.job_run_details` as the automated operational record;
- operational evaluation treats the system as something that must be audited, not simply trusted;
- operational evaluation is itself bounded and does not override constitutional or legal limits.

This chapter may **not** claim that:

- operational evaluation proves absolute correctness, morality, or legality;
- operational evaluation makes Ms. Allis self-governing in a political or metaphysical sense;
- operational evaluation on its own authorizes external commitments, public speech, or durable memory;
- operational evaluation replaces human judgment, community governance, or law.

Within this gate, operational evaluation is documented as an **instrumental, technical layer** for monitoring and improving a governed AI system. It is a tool for accountability, not a claim of perfection or autonomy.

---

## 39.3 From Packet Evaluation to Operational Evaluation

Earlier chapters describe how individual cognition packets are staged, evaluated, emitted, and later promoted under explicit governance.

Operational evaluation takes a step back from the single packet and asks:

- Over many packets, are the gates being used correctly?
- Are they blocking the right things and allowing the right things?
- Are there patterns of failure that point to design problems or misalignment with local needs?

This shift matters academically because it moves from **micro governance** (one packet at a time) to **macro governance** (how the whole pipeline behaves in the wild). It matters practically because rural deployments must be able to notice trends and not just individual mistakes.

For rural developers, the difference is simple:

- **Packet evaluation**: "Should this packet move forward?"
- **Operational evaluation**: "Are we happy with how packets move forward in general?"

Both are necessary.

---

## 39.4 Layers of Operational Evaluation

Operational evaluation in Ms. Allis has at least three layers.

1. **Packet-Level Gate Metrics** — Measures how individual packets interact with staging, evaluation, emission, and promotion.

2. **Service- and Pipeline-Level Metrics** — Measures how the various governed candidate systems (cognition, spatial, temporal, memory, communication) behave as coordinated pipelines.

3. **Platform-Level Health and Accountability Metrics** — Measures how the overall system performs across uptime, error rates, capacity, and exposure of internal state to operators and communities. As of July 26, 2026, the primary automated record at this layer is `cron.job_run_details`.

Each layer tells a different part of the story, but all three must be read together to understand how Ms. Allis behaves in the real world.

---

## 39.5 cron.job_run_details: The Primary Operational Evaluation Artifact

The `cron.job_run_details` table in `wv_gis` is the **primary operational evaluation artifact** for the database-layer governance cycle. Every time one of the four registered pg_cron jobs fires, this table receives a row recording whether that execution succeeded or failed, when it started, when it ended, and what it returned.

### As-Built State on July 26, 2026

As of July 26, 2026, `cron.job_run_details` was **empty**. No executions had yet occurred. The four jobs (jobids 1, 3, 4, 5) had been registered and verified as active in `cron.job`, but none had fired on their scheduled cadences at the time of the architecture closeout. This is an honest, accurate statement of the as-built state: the governance heartbeat was installed and ready; the execution history had not yet begun to accumulate.

This is the verification discipline of Appendix A applied to operational evaluation: a table that exists and is designated as the artifact is documented as such, with an accurate note about its state at the time of the gate. The table will accumulate `succeeded` and `failed` run history as the jobs fire on their schedules going forward.

### Structure and Queries

The `cron.job_run_details` table has the following relevant columns:

```sql
SELECT
  jobid,
  runid,
  job_pid,
  database,
  username,
  command,
  status,          -- 'succeeded' or 'failed'
  return_message,
  start_time,
  end_time
FROM cron.job_run_details
ORDER BY start_time DESC;
```

For rural developers, the operational evaluation queries you will run most often are:

```sql
-- Most recent run for each job
SELECT DISTINCT ON (jobid)
  jobid, status, return_message, start_time, end_time
FROM cron.job_run_details
ORDER BY jobid, start_time DESC;

-- All failed runs (the anomaly log)
SELECT jobid, status, return_message, start_time
FROM cron.job_run_details
WHERE status = 'failed'
ORDER BY start_time DESC;

-- Run count and success rate per job
SELECT
  jobid,
  COUNT(*) AS total_runs,
  SUM(CASE WHEN status = 'succeeded' THEN 1 ELSE 0 END) AS succeeded,
  SUM(CASE WHEN status = 'failed' THEN 1 ELSE 0 END) AS failed
FROM cron.job_run_details
GROUP BY jobid
ORDER BY jobid;
```

### What cron.job_run_details Records Over Time

As the four jobs begin firing, `cron.job_run_details` will accumulate the execution history that makes operational evaluation possible:

| jobid | Job name | What a succeeded row confirms |
|---|---|---|
| 1 | `gbim-runtime-lifecycle-hourly` | Materialized view refreshed; admissibility counts advanced; `refresh_public_admissible_gbim_mv` audit record written |
| 3 | `gbim-runtime-lifecycle-daily` | Degradation transitions run; `lifecycle_snapshot` written; governance filtering pass executed (Chapter 52 Recurrent Epistemic Loop) |
| 4 | `gbim-runtime-lifecycle-weekly` | Cohort review completed; weekly audit record written |
| 5 | `gbim-runtime-lifecycle-monthly` | Deep lifecycle audit completed; monthly governance state record written |

A `failed` row for jobid 1 means the public evidence surface was not refreshed during that hour. A `failed` row for jobid 3 means the daily governance filtering pass — including constitutional review via the Constitutional Principles Service (Chapter 37) — did not execute that morning. Both are operationally significant and should be treated as governance degradation events, not routine noise.

### cron.job_run_details as Automated Learning Record

Once executions accumulate, `cron.job_run_details` becomes more than a run log. It becomes the **automated learning record** for the governance cycle:

- Patterns of `failed` rows for a specific job identify systematic problems — misconfigured procedures, schema migrations that broke a dependent function, or infrastructure failures that interrupted database access.
- Patterns of unusually long `end_time - start_time` durations identify governance passes that are growing more expensive as the governed store grows, signaling that indexing or partitioning adjustments may be needed.
- The absence of any rows for a job that should have fired (gap in the hourly record, for example) identifies a pg_cron daemon restart or a `cron.job` deactivation that was not intentional.

For rural developers with limited monitoring infrastructure, `cron.job_run_details` is the single table that answers the question: "Did the governance cycle actually run today?" It is not a substitute for full observability, but it is the durable, queryable record that replaces the need to read log files after the fact.

---

## 39.6 Packet-Level Operational Metrics

Packet-level operational evaluation is built on top of the governed packet lifecycle.

For the cognition sandbox, typical packet-level metrics include:

- number of packets staged;
- number and proportion of packets approved at first-stage evaluation;
- number and proportion of packets rejected or held with warnings;
- readiness score distributions;
- deduplicated evidence counts;
- latency from staging to evaluation, and from evaluation to emission.

For rural developers, these metrics can be read in plain terms:

- If **too many packets are blocked**, the gates may be too strict, misconfigured, or misaligned with local use.
- If **too few packets are blocked**, the gates may be too loose or not catching problematic cases.
- If **readiness scores cluster at the extremes**, something may be wrong with either the scoring logic or the upstream candidate generation.

Packet-level operational evaluation does not ask whether a single packet is right. It asks whether the gate is behaving reasonably across many packets.

---

## 39.7 Deduplication and Evidence Quality

Deduplicated evidence counts are an important part of operational evaluation for Ms. Allis.

At the packet level, deduplicated evidence metrics tell operators whether:

- the retrieval system is feeding the evaluator many copies of the same thing;
- the evaluation layer is correctly collapsing repeated evidence;
- packets are being approved with thin or repetitive support.

At the operational level, these metrics are used to:

- adjust retrieval routing and filters;
- tighten or relax minimum evidence standards;
- identify sources that produce noisy or redundant material;
- ensure that local evidence from rural geographies is not drowned out by generic web patterns.

For rural developers, deduplication metrics are a way of asking:

**"Is this system really listening to our place, or just repeating the same loud voices over and over?"**

The operational evaluator cannot answer that question perfectly, but it can show when duplication or thin evidence becomes a pattern.

---

## 39.8 Operational Evaluation of Governed Pipelines

Operational evaluation also looks at how the different governed candidate systems behave as pipelines.

Examples include:

- **Cognition pipeline**: staging → first-stage evaluation → governed emission → promotion;
- **Spatial pipeline**: spatial candidates staged, evaluated, and possibly promoted into historical spatial memory;
- **Temporal pipeline**: ephemeral, staged, and historical temporal tiers;
- **Per-user memory pipeline**: conversational candidates evaluated for direct sum memory only under allowed roles, purposes, and consent;
- **External communication pipeline**: external communication candidates evaluated and only permitted under strict roles, channels, and consent conditions.
- **Database governance pipeline**: pg_cron jobs fire on schedule → `cron.job_run_details` records the outcome → `runtime_governance.public_answer_audit` records the governance effect.

Operational evaluation at this level asks:

- Are packets flowing through the intended sequence of gates?
- Are any services bypassing governance layers?
- Do we see unexpected concentrations of traffic in certain tiers?
- Are the four pg_cron jobs firing on schedule and accumulating `succeeded` rows?
- Are there patterns of failure that suggest design flaws in the candidate schemas or gate rules?

For rural developers, this is like looking at a map of traffic through a town: Are trucks avoiding the weight-limited bridge? Are ambulances able to reach the hospital? Are dangerous shortcuts being taken around the edges? Operational evaluation maps and monitors the traffic of packets through Ms. Allis' internal roads — including the scheduled governance roads that the pg_cron jobs travel.

---

## 39.9 Platform-Level Health and Accountability

Operational evaluation also covers platform-level health metrics, which tell whether Ms. Allis is able to do her work reliably.

Examples include:

- **Uptime and health checks** for critical services (gateways, cognition sandbox, spatial sandbox, temporal memory, RAG services, databases);
- **Latency and throughput** for evaluation and routing endpoints;
- **Error and failure rates**, including emergency cleanup triggers;
- **Queue depths and backlog counts** for staged candidates awaiting review;
- **Capacity limits** for rural deployments (network quality, hardware limits, local database constraints);
- **pg_cron execution history** in `cron.job_run_details` — whether the governance heartbeat is firing and succeeding on its four scheduled cadences.

These metrics matter because a theoretically perfect governance system is useless if the services that enforce it are down, overloaded, or misconfigured.

For rural developers, platform-level operational evaluation has a straightforward meaning:

**"Is Ms. Allis awake, healthy, and able to apply her gates?"**

If not, the right response is not to bypass governance but to restore health and only then restart governed traffic. Checking `cron.job_run_details` for recent `succeeded` rows is the first step in that diagnosis.

---

## 39.10 Step-by-Step Operational Evaluation Process

This section offers a simple step-by-step process for rural operators and developers to interpret operational evaluation in practice.

### Step 1: Confirm platform health

Before worrying about packets, check that the core services are up and reporting healthy status. If the foundation is unstable, fix that first.

### Step 2: Check cron.job_run_details

Query `cron.job_run_details` for the four pg_cron jobs. Confirm that jobid 1 shows a `succeeded` row within the last hour, jobid 3 within the last day, jobid 4 within the last week, and jobid 5 within the last month. If any job shows a `failed` row or an unexplained gap, treat that as a governance degradation event and investigate before proceeding to packet-level review.

As of July 26, 2026, this table was empty — no executions had yet occurred. The first `succeeded` rows will begin appearing as the jobs fire on their schedules. Once they do, this step becomes the fastest operational check available.

### Step 3: Inspect packet-level gate metrics

Look at approval rates, rejection rates, warnings, readiness score distributions, and deduplicated evidence counts.

- If everything is being approved with high scores and few warnings, the gates may be too lenient.
- If almost nothing is being approved, the gates or schemas may be too strict.
- If deduplicated evidence counts are low, retrieval and evidence aggregation may need adjustment.

### Step 4: Check pipeline integrity

Verify that packets are actually flowing through staging, evaluation, emission, and promotion rather than bypassing gates.

- Look for unexpected direct writes into durable tiers.
- Look for services that attempt to emit or promote without passing evaluation.
- Ensure that external communication routes still go through their governed candidate flows.

### Step 5: Evaluate trends over time

Operational evaluation is less about single incidents and more about patterns. Track:

- changes in approval rates;
- shifts in error categories;
- growth in staged-but-never-promoted packets;
- drops or spikes in external communication candidates;
- failure rate trends in `cron.job_run_details` for each jobid.

### Step 6: Adjust configuration, not principles

When metrics suggest a problem, the first response is usually to adjust thresholds, schemas, routing hints, or retrieval parameters. The underlying principles of consent, constitutional alignment, and place-aware responsibility remain fixed.

### Step 7: Document and review

Record notable operational shifts and the corrective actions taken. This documentation supports community and academic review without exposing private user content or confidential operational keys. For the database-layer governance cycle, the `cron.job_run_details` table is itself part of this documentation — it is a durable, queryable record of what the governance heartbeat did and when.

For rural developers, this seven-step loop is the practical rhythm of operational evaluation. It is a recurring practice, not a one-time audit.

---

## 39.11 Operational Evaluation as Guardrail Against Drift

One of the main dangers in long-running systems is **drift**: slow movement away from the original design intent.

Operational evaluation is a guardrail against that drift because:

- it notices when the proportion of packets in different tiers changes dramatically;
- it reveals when certain gates are barely being used or are being overwhelmed;
- it shows when external communication candidates increase or start failing in new ways;
- it highlights when error types shift from setup mistakes toward deeper misalignment;
- it records when the governance heartbeat begins missing scheduled firings — detectable in `cron.job_run_details` as gaps in the jobid 1 hourly record or absent jobid 3 daily rows.

This is especially important in rural contexts, where the temptation to "just make it work" can be strong under resource constraints. Operational evaluation makes it easier to see when shortcuts are undermining the architecture.

For rural developers, this means Ms. Allis is built to complain about her own drift. The system is supposed to tell on itself when it starts straying from the intended pattern of staged, evaluated, emitted, and promoted flows — and `cron.job_run_details` is the place where the governance layer's own drift becomes visible.

---

## 39.12 Limits of Operational Evaluation

Operational evaluation has clear limits, which must be respected.

It does not:

- guarantee that every approved packet is right, just, or fair;
- guarantee that every rejected packet is wrong, harmful, or unhelpful;
- replace legal, ethical, or human oversight;
- convert Ms. Allis into a self-judging person;
- make `cron.job_run_details` a complete substitute for full observability — it records whether the jobs fired and whether they succeeded, not the internal details of every governance decision made during a run.

It does:

- provide structured measurements of how often governance mechanisms are used and how they behave;
- support tuning, debugging, and validation of the governed architecture;
- provide evidence that the system stays within its own design commitments;
- give rural communities a way to ask informed questions about how the system has been behaving;
- accumulate in `cron.job_run_details` a durable, queryable record of governance heartbeat execution that grows more informative with every passing day.

In academic terms, operational evaluation is an internal instrument of **system reflexivity**. It is a way the system looks at its own behavior under a fixed constitution, not a way it changes that constitution.

---

## 39.13 Relationship to Polymathmatic Geography

Operational evaluation supports key Polymathmatic Geography principles.

- **P3 – Power has a geometry**: Operational evaluation shows how power actually flows through the internal routes and gates of Ms. Allis. The `cron.job_run_details` table is the geometric record of how the governance heartbeat moves through time.
- **P12 – Intelligence with a ZIP code**: Operational evaluation can be shaped to pay attention to local traffic, local evidence, and local gate behavior rather than only global metrics.
- **P16 – Power accountable to place**: Operational evaluation provides the logs and metrics needed for local overseers to hold the system accountable. `cron.job_run_details` and `runtime_governance.public_answer_audit` together form the durable accountability record for the communities Ms. Allis serves.

For rural developers, this means that operational evaluation is not just a technical performance feature. It is a core part of how the system remains answerable to the communities it serves.

---

## 39.14 Closing Statement

Operational evaluation is Ms. Allis' way of watching herself operate, in a constrained, technical sense. It tracks packet-level gate behavior, pipeline integrity, and platform health so that rural deployments can see whether the system is behaving as designed.

The **primary operational evaluation artifact** for the database-layer governance cycle is `cron.job_run_details`. As of July 26, 2026, this table was empty — the four pg_cron jobs had been registered and verified as active, but no executions had yet occurred. Going forward, every firing of jobids 1, 3, 4, and 5 will write a `succeeded` or `failed` row to this table, accumulating the automated learning and operational evaluation record that makes governance behavior auditable over time.

It does not grant the system any special moral authority, legal standing, or personhood. Instead, it keeps the system grounded in its commitments: staged before evaluated, evaluated before emitted, emitted before promoted, and always under rules that reflect the needs and rights of the communities where it is deployed.

---

*Chapter 39 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
