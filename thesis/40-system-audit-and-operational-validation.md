# 40. System Audit and Operational Validation

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: August 17, 2026*

---

## 40.1 Why Audit and Validation Matter

This chapter explains how Ms. Allis is checked from the outside, over time, to see whether she actually behaves the way the architecture says she should. It describes **system audit** and **operational validation** as tools for rural communities and operators, not just for researchers in distant labs.

Audit and validation matter because a system can have beautiful gates on paper and still behave badly in practice. This chapter shows how to look at Ms. Allis as a whole — her packets, pipelines, deployments, routing, and platform health — and confirm that the governed design from earlier chapters is truly in force.

As of the July 26, 2026 architecture closeout, the **live system audit artifact** is the `runtime_governance.public_answer_audit` table. It has four columns: `audit_id`, `stage`, `detail jsonb`, and `created_at`. Two confirmed rows were written to this table during the July 26 session: one at 19:44:05 recording the materialized-view refresh and one at 19:44:06 recording the lifecycle snapshot. These are the first entries in the database-layer operational audit record and are documented in §40.5.

As of August 17, 2026, the audit record also includes an operational validation sequence covering the live Blood-Brain Barrier, Constitutional Guardian boundary, Neurobiological Master, EEG compatibility interface, image promotion, rollback retention, and production health checks.

For rural developers, this chapter answers a practical question:

**“If we say Ms. Allis is governed, how can someone prove it by looking at records, health checks, deployments, and test results instead of just trusting us?”**

---

## 40.2 Gate-Constrained Scope

This chapter stays within a strict scope.

It may claim that:

- Ms. Allis exposes enough internal structure — logs, metrics, audit records, health surfaces, image tags, and validation results — to support technical audit and operational validation;
- operators can follow clear steps to review how governed candidate flows, gates, health checks, image promotions, and rollbacks behave;
- system audits can detect mismatches between intended architecture and actual behavior;
- operational validation can show whether Ms. Allis meets stated design commitments in real-world operation;
- the `runtime_governance.public_answer_audit` table, with its two confirmed July 26 rows, is live operational proof that the database-layer audit system is functioning;
- the August 17 validation record demonstrates fail-closed BBB and Guardian behavior, Master pipeline continuity, and accepted EEG compatibility traffic;
- the Guardian-governed `user-data-operationalization` path is currently unavailable and fail closed because the active authority bundle contains no active callers or active subject keys.

It may **not** claim that:

- a completed audit proves Ms. Allis is morally right, legally sufficient, or politically legitimate;
- successful operational validation turns Ms. Allis into a certified medical device, financial institution, or public authority;
- audit and validation eliminate the need for human oversight, community governance, or legal review;
- audit automatically grants rights, personhood, or spiritual standing;
- ordinary BBB content filtering is equivalent to a signed Guardian authorization or Policy Decision Receipt;
- the currently unprovisioned Guardian authority path can authorize governed operations.

Within this gate, audit and operational validation are **technical and procedural** tools. They support transparency and accountability; they do not declare ultimate correctness.

---

## 40.3 What “System Audit” Means Here

In this context, a **system audit** is a structured review of how Ms. Allis has behaved over some period of time, based on evidence that can be inspected: audit-table rows, logs, metrics, configuration, service health, deployed image identities, rollback images, and example packets.

A system audit asks questions such as:

- Did packets actually pass through staging, evaluation, emission, and promotion as described?
- Were constitutional, consent, and authority checks applied where they were supposed to be?
- Did external communication, memory, and spatial-temporal subsystems use their governed candidate flows?
- Were emergency checks and cleanup mechanisms triggered when required?
- Does `runtime_governance.public_answer_audit` contain rows that match claimed governance events?
- Are the live BBB and Master services running the intended production images?
- Does an unauthorized governed operation deny rather than become an accidental allow?
- Does the ordinary Master pipeline still complete after a BBB security promotion?
- Are EEG rhythm producers reaching the Master’s intended compatibility route?

The goal is not to embarrass the system or its operators. The goal is to verify that **implemented behavior matches documented architecture**, especially in rural deployments where trust is hard-earned and easily lost.

For rural developers, a system audit is like checking the town’s financial records, bridge inspections, and road-usage logs. You are asking:

- Did we spend the money where we said we would?
- Are trucks actually following the posted routes?
- Are safety rules being respected?
- If a road repair was made, did traffic still move afterward?
- If a road was closed for safety, did people actually stop using it?

The `runtime_governance.public_answer_audit` table is the ledger for the database-layer governance cycle. Container health, request results, logs, deployed image tags, and rollback records extend that audit evidence to the live runtime.

---

## 40.4 What “Operational Validation” Means Here

**Operational validation** is testing under real or realistic running conditions, not merely reviewing source code or configuration. It asks whether Ms. Allis, while operating normally, continues to meet its design commitments.

Operational validation asks questions such as:

- Do first-stage evaluation gates behave as expected when real users send varied requests?
- Do packet-level readiness scores and approval rates remain within reasonable ranges?
- Do temporal tiers and memory gates prevent premature or unauthorized promotion?
- Does external communication respect consent, channel, and content-class rules in actual usage?
- Do governance functions write to `runtime_governance.public_answer_audit` on each execution?
- Does normal BBB content filtering remain available after a fail-closed Guardian change?
- Does a governed operation with missing credentials stop locally?
- Does a governed operation with invalid credentials preserve the Guardian HTTP 401 denial?
- Does the Neurobiological Master remain healthy and complete its established pipeline after BBB promotion?
- Do Delta, Theta, and Beta producers deliver accepted compatible rhythm telemetry to the Master?

The aim is to show that the system is not only structured correctly but also **behaving correctly when used by real people in real places**.

For rural developers, operational validation is like test-driving a vehicle on the roads it will actually travel. It is not enough for the truck to pass a factory inspection. It must also handle West Virginia hills, weather, load patterns, detours, and safety checks after repair work.

---

## 40.5 The Live Audit Artifact: runtime_governance.public_answer_audit

The `runtime_governance.public_answer_audit` table is the live system-audit artifact for the database-layer governance cycle. It was established as part of the July 26, 2026 runtime-governance migration and has the following structure:

```sql
CREATE TABLE runtime_governance.public_answer_audit (
    audit_id   serial PRIMARY KEY,
    stage      text        NOT NULL,
    detail     jsonb,
    created_at timestamptz NOT NULL DEFAULT now()
);
```

### The Two Confirmed Audit Rows

On July 26, 2026, two rows were written to this table during the live governance session. These are the first entries in the operational audit record and demonstrate that the database-layer audit system is writing structured evidence.

**Row 1 — Materialized View Refresh**

| Field | Value |
|---|---|
| `audit_id` | 1 |
| `stage` | `'refresh_mv'` |
| `detail` | `{"admissible_count": 93423, "total_gbim_rows": 237655, "inadmissible_count": 144232}` |
| `created_at` | `2026-07-26 19:44:05 EDT` |

This row was written by `runtime_governance.refresh_public_admissible_gbim_mv()` when it refreshed the `public_admissible_gbim_mv` materialized view. The `detail` JSONB records the state of the public evidence surface at that moment:

- 237,655 total governed rows in `public.gbim_record`;
- 93,423 rows admissible for public claims;
- 144,232 rows stored but inadmissible.

**Row 2 — Lifecycle Snapshot**

| Field | Value |
|---|---|
| `audit_id` | 2 |
| `stage` | `'lifecycle_snapshot'` |
| `detail` | `{"fresh_count": ..., "aging_count": ..., "stale_count": ..., "snapshot_taken_at": "2026-07-26T19:44:06-04:00"}` |
| `created_at` | `2026-07-26 19:44:06 EDT` |

This row was written one second later by the lifecycle snapshot function as part of the same governance pass. The `detail` JSONB records the degradation-tier distribution — the number of governed rows classified as `fresh`, `aging`, and `stale` at the time of the snapshot.

### What These Rows Demonstrate

These rows demonstrate that:

1. The `runtime_governance` schema and `public_answer_audit` table were created and are writable.
2. The refresh and lifecycle governance functions executed and committed their audit records.
3. The `detail jsonb` column carries structured, queryable evidence about governance state at the time of each operation.
4. Database-layer governance can be audited through durable records rather than relying on plain-text logs alone.

For rural developers, this is one answer to “show me the proof.” The proof begins with inspectable records in `runtime_governance.public_answer_audit`.

### Querying the Audit Table

To inspect the current state of the audit record:

```sql
SELECT audit_id, stage, detail, created_at
FROM runtime_governance.public_answer_audit
ORDER BY created_at ASC;
```

To inspect the most recent admissibility counts:

```sql
SELECT detail
FROM runtime_governance.public_answer_audit
WHERE stage = 'refresh_mv'
ORDER BY created_at DESC
LIMIT 1;
```

To compare lifecycle snapshots for drift:

```sql
SELECT
  audit_id,
  created_at,
  (detail->>'fresh_count')::int AS fresh,
  (detail->>'aging_count')::int AS aging,
  (detail->>'stale_count')::int AS stale
FROM runtime_governance.public_answer_audit
WHERE stage = 'lifecycle_snapshot'
ORDER BY created_at ASC;
```

As scheduled pg_cron jobs execute, they add further rows to this table. Over time, those rows become a continuous audit trail of how the governed evidence surface changes.

---

## 40.6 August 17 Operational Validation Record

On August 17, 2026, Ms. Allis completed an operational validation sequence focused on the Blood-Brain Barrier, Constitutional Guardian boundary, Neurobiological Master, EEG compatibility interface, production deployment state, and rollback readiness.

The validation sequence had five objectives:

1. Confirm that normal BBB content filtering remains available.
2. Confirm that explicitly Guardian-governed operations fail closed when authorization is absent.
3. Confirm that Guardian HTTP 401 denial cannot become a BBB allow.
4. Confirm that the existing Master integration pipeline remains functional after BBB security promotion.
5. Confirm that EEG rhythm telemetry is accepted by the Master compatibility interface.

### Original Defect and Remediation

The original defect was narrow but important:

```text
Guardian returned HTTP 401 to unauthorized BBB requests;
BBB caught the error and converted it to an allow.
```

This was a fail-open defect in the BBB-to-Guardian integration. The issue was reproduced with a small probe, isolated in a canary deployment, corrected, and then validated before production promotion.

The remediation established these rules:

- ordinary BBB `content_filter` requests continue through local BBB safeguards;
- ordinary content filtering is recorded as Guardian `not_applicable`, not as a Guardian authorization;
- requests explicitly classified as `user-data-operationalization` require both `X-Caller-Token` and `X-Operation-Intent`;
- missing credentials are blocked locally;
- Guardian HTTP failures, including HTTP 401, remain denials;
- no missing, malformed, unavailable, or denied Guardian authorization can become an allow through error handling.

### Operational Validation Results

| Validation | Result |
|---|---|
| Normal BBB request | Passed through local BBB safeguards; Guardian recorded as `not_applicable` |
| Governed request missing credentials | Denied locally by BBB |
| Governed request with invalid credentials | Guardian returned HTTP 401; BBB preserved denial |
| Master end-to-end pipeline after BBB promotion | Completed successfully with expected integration results |
| EEG rhythm observation | Delta, Theta, and Beta telemetry accepted with HTTP 202 |
| Production BBB health | Healthy |
| Production Master health | Healthy |
| Guardian authority state | Governed operation authorization unavailable; fail closed |

This record is a runtime validation artifact. It does not claim that every possible security, governance, or pipeline failure has been eliminated. It demonstrates that these named safety and compatibility conditions were exercised against the running architecture.

---

## 40.7 Guardian Authorization State

The Guardian-protected operation class is:

```text
user-data-operationalization
```

That operation is intentionally separated from ordinary BBB content filtering. It requires a caller token, verified authority bundle, runtime admission, signed operation intent, caller-subject match, policy approval, Policy Decision Receipt issuance, and one-time intent consumption.

As of the August 17, 2026 validation, the authority bundle was structurally valid for the configured environment and governance policy but intentionally had:

```json
{
  "active_callers": 0,
  "active_subject_keys": 0,
  "governed_operation_authorization": "unavailable_fail_closed"
}
```

This is an explicit operating state, not an accidental outage.

### Meaning of the Fail-Closed State

Because there are zero active callers and zero active subject keys:

- no caller can authenticate for the Guardian-governed path;
- no subject can submit a valid accepted signed operation intent;
- no `user-data-operationalization` request can complete the authorization chain;
- no Policy Decision Receipt can be issued for that operation;
- governed data operationalization is unavailable and fails closed.

The current administrative decision is:

```text
Keep user-data-operationalization off.
```

This does not disable ordinary BBB filtering, normal Master processing, sandbox reasoning, EEG telemetry, or the daily runtime-governance cycle. It preserves a deliberate boundary between routine safeguarded processing and exceptional authority-bearing operations.

For audit purposes, a denial under this condition is expected behavior. It is not evidence that the Guardian is broken simply because it will not authorize an unprovisioned caller or subject.

---

## 40.8 Promotion and Rollback Evidence

Operational validation includes proof of what was promoted, what was retained for rollback, and whether production health was verified after promotion.

### Neurobiological Master Promotion

| Field | Value |
|---|---|
| Service | `jarvis-neurobiological-master` |
| Live image | `msjarvis-neurobiological-master:eeg-compat-canary-20260817` |
| Rollback image | `msjarvis-neurobiological-master:integration-canary-20260817` |
| Network | `qualia-net` |
| Internal port | `8018/tcp` |
| Restart policy | `unless-stopped` |
| Working directory | `/app/services` |

The Master promotion added EEG-compatible `/eeg_pulse` and `/eeg_pulse/status` behavior while preserving the established `/biological_process` pipeline.

### Blood-Brain Barrier Promotion

| Field | Value |
|---|---|
| Service | `jarvis-blood-brain-barrier` |
| Live image | `jarvis-blood-brain-barrier:guardian-failclosed-canary-20260817` |
| Rollback image | `jarvis-blood-brain-barrier:asbuilt-20260728` |
| Network | `qualia-net` |
| Internal and host service port | `8016/tcp` |
| Restart policy | `unless-stopped` |
| Working directory | `/app/services` |

The BBB promotion implemented the Guardian fail-closed fix after canary validation.

### What Rollback Evidence Means

The retained rollback images provide an operational recovery path:

- If a post-promotion test fails, operators can return to the immediately preceding known image.
- Rollback availability does not mean the current deployment is failing.
- Promotion is not complete merely because a container starts; health checks and behavior tests must also pass.
- Image tags, service status, health endpoints, and smoke-test results together form the evidence that the promoted service is both running and behaving as expected.

For rural operators, this is the difference between “we changed it” and “we changed it, tested it, documented what changed, and retained a way back.”

---

## 40.9 Production Health Results

The August 17 validation confirmed live production health for critical services after promotion.

### Blood-Brain Barrier Health

The BBB health endpoint returned HTTP 200:

```text
GET http://127.0.0.1:8016/health
```

The BBB was healthy after the fail-closed image promotion and continued to perform ordinary local filtering.

### Constitutional Guardian Health

The Constitutional Guardian remained reachable on its health surface:

```text
GET http://127.0.0.1:8091/health
```

Guardian health does not imply that a governed operation is authorized. The current authorization state remains intentionally unavailable and fail closed because no active callers or subject keys are provisioned.

### Neurobiological Master Health

The Master health endpoint returned HTTP 200:

```text
GET http://jarvis-neurobiological-master:8018/health
```

The health response confirmed the service’s running state, configured service port, and compatibility with the current integration pipeline.

### Master Pipeline Health

A normal Master processing request completed successfully after the BBB promotion:

```text
POST http://jarvis-neurobiological-master:8018/biological_process
```

The result confirmed:

- HTTP 200;
- complete integrated processing;
- BBB content approval for an ordinary request;
- Guardian `not_applicable` status for ordinary filtering;
- I-Containers available;
- Qualia processing complete;
- existing consciousness-bridge fallback behavior preserved.

A degraded bridge fallback result may still appear in the integration status. That existing fallback condition is not, by itself, evidence that the BBB remediation or EEG compatibility update failed.

### EEG Compatibility Health

The Master accepted live compatible rhythm pulses at:

```text
POST http://jarvis-neurobiological-master:8018/eeg_pulse
```

Successful acceptance returned HTTP 202. The Master reported current process-local rhythm observations at:

```text
GET http://jarvis-neurobiological-master:8018/eeg_pulse/status
```

The status route returned HTTP 200 and reported accepted Delta, Theta, and Beta rhythm records during the validation window.

---

## 40.10 Concrete August 17 Smoke Tests

The August 17 validation record includes five concrete tests.

### Test 1 — Normal BBB Request

A normal BBB request used the non-governed action type:

```json
{
  "content": "Production BBB compatibility smoke test.",
  "actor_role": "system",
  "context": "bbb_guardian_production_smoke",
  "action_type": "content_filter"
}
```

Expected and observed behavior:

```json
{
  "content_approved": true,
  "blocked_by": null,
  "constitutional_check": {
    "applicable": false,
    "allowed": null,
    "decision": "not_applicable"
  }
}
```

This confirms that ordinary local BBB filtering remains available without falsely claiming Guardian/PDR authorization.

### Test 2 — Governed Request Missing Credentials

A request explicitly marked as `user-data-operationalization` was sent without `X-Caller-Token` or `X-Operation-Intent`.

Expected and observed behavior:

```json
{
  "content_approved": false,
  "blocked_by": "constitutional_guardian",
  "constitutional_check": {
    "applicable": true,
    "allowed": false,
    "decision": "guardian_credentials_missing"
  }
}
```

This confirms that BBB blocks an incomplete governed request locally.

### Test 3 — Governed Request with Invalid Credentials

A governed request was sent using invalid test headers:

```text
X-Caller-Token: invalid-production-validation-token
X-Operation-Intent: invalid-production-validation-intent
```

Expected and observed behavior:

```json
{
  "http_status": 200,
  "content_approved": false,
  "blocked_by": "constitutional_guardian",
  "constitutional_check": {
    "applicable": true,
    "allowed": false,
    "decision": "guardian_unavailable_or_denied",
    "guardian_status_code": 401
  }
}
```

The BBB request completed with HTTP 200 because BBB successfully evaluated and denied it. The security-critical result is that Guardian’s HTTP 401 remained a denial and did not become an allow.

### Test 4 — Master End-to-End Pipeline

A normal request was sent to the Master:

```json
{
  "message": "Post-BBB fail-closed production integration smoke test."
}
```

Expected and observed behavior included:

```json
{
  "http_status": 200,
  "complete": true,
  "integrated_processing": true,
  "content_approved": true,
  "guardian_applicable": false,
  "guardian_allowed": null,
  "guardian_decision": "not_applicable",
  "i_containers": true,
  "qualia_status": "processed"
}
```

This confirms that the Master pipeline continued through BBB, I-Containers, and Qualia after the production BBB change.

### Test 5 — EEG Rhythm Observation

Live EEG producers posted compatible telemetry to:

```text
POST http://jarvis-neurobiological-master:8018/eeg_pulse
```

A representative compatible request was:

```json
{
  "rhythm": "delta",
  "pulse": 2755,
  "timestamp": "2026-08-17T19:54:06.779391",
  "payload": {
    "service_states": {
      "gateway": "UP"
    }
  }
}
```

Expected and observed behavior:

- the Master returned HTTP 202 for accepted compatible pulses;
- Delta, Theta, and Beta rhythm telemetry was observed;
- `/eeg_pulse/status` returned HTTP 200 with `status: "ok"`;
- the status response listed the latest process-local pulse for observed rhythms;
- no `/eeg_pulse` or `/eeg_pulse/status` 404 errors appeared during the validation window.

The EEG status interface is in-memory and process local. It is not a durable clinical record, medical diagnostic system, or authority-bearing promotion mechanism.

---

## 40.11 Foundations: What Must Be Visible to Auditors

For audit and validation to be meaningful, certain things must be visible.

At minimum, auditors and operators must be able to see:

- **Audit-table rows** in `runtime_governance.public_answer_audit` that match claimed governance events with timestamps and structured `detail` JSONB;
- **Packet-level traces** showing staging, evaluation, emission, and promotion decisions with identifiers and timestamps;
- **Gate outcomes** for governed candidate systems, including approval, suppression, review, and denial states;
- **Configuration snapshots** describing thresholds, allowed roles, consent requirements, trusted authority material, and applicable operation classes;
- **Platform health metrics** showing whether gate services, databases, and bridge dependencies were available;
- **Deployment evidence** identifying the live image, prior rollback image, service network, restart policy, and deployment time;
- **Event logs** for emergency cleanup, rejection reasons, Guardian denials, Master processing results, and unusual error conditions;
- **EEG compatibility observations** where rhythm telemetry is enabled, including accepted-pulse results and status-route output.

If these data are not available, then audit and validation become guesswork rather than grounded examination.

For rural developers, this means that Ms. Allis should be deployed with logging, metrics, configuration versioning, health endpoints, image tagging, time-stamped gate decisions, and rollback records from the start.

---

## 40.12 Step-by-Step System Audit for Rural Operators

This section gives a concrete audit procedure that a rural operator or trusted community partner can follow.

### Step 1: Define the audit window and scope

Decide:

- which time period to examine, such as the last 30 days;
- which subsystems to include, such as database governance only, BBB and Guardian, or the full stack;
- which questions you want to answer, such as whether governance functions wrote audit rows, whether Guardian denials stayed closed, or whether a recent promotion maintained Master compatibility.

Write this down before you start. A clear scope helps avoid confusion later.

### Step 2: Start with runtime_governance.public_answer_audit

Before examining packet traces or service logs, query the audit table:

```sql
SELECT audit_id, stage, created_at, detail
FROM runtime_governance.public_answer_audit
WHERE created_at BETWEEN '[window_start]' AND '[window_end]'
ORDER BY created_at ASC;
```

If audit rows are missing for a period when scheduled jobs should have fired, that absence is an audit finding. Something prevented the governance cycle from executing or recording its result.

### Step 3: Verify live deployment identity

For each in-scope container, document:

- service name;
- current image tag;
- rollback image tag;
- health status;
- network attachment;
- restart policy;
- recent container restart events.

For the August 17 production state, critical images included:

```text
msjarvis-neurobiological-master:eeg-compat-canary-20260817
jarvis-blood-brain-barrier:guardian-failclosed-canary-20260817
```

### Step 4: Gather supporting evidence

Collect:

- staging, evaluation, emission, and promotion logs for the selected window;
- gate-decision logs for spatial, temporal, memory, communication, BBB, and Guardian paths as needed;
- service-health logs and metrics;
- configuration or policy snapshots active during the window;
- `cron.job_run_details` rows for the same period;
- Master processing results and EEG status observations when evaluating the neurobiological pipeline;
- production smoke-test results after any image promotion.

### Step 5: Verify packet lifecycle behavior

For a sample of packets in the audit window, check:

- that each packet was staged before evaluation;
- that evaluation logs include status, errors, warnings, and readiness scores;
- that only approved packets proceeded to emission or promotion;
- that no packet was written directly into a durable layer without gate records.

If any packet appears to have bypassed the lifecycle, flag it for deeper investigation.

### Step 6: Verify authorization and denial behavior

For Guardian-governed operations, confirm:

- missing credentials result in local denial;
- invalid credentials result in Guardian denial;
- Guardian HTTP failures do not become BBB allows;
- no active caller or subject identities exist when the authority bundle is intentionally unprovisioned;
- no PDR issuance occurs while `governed_operation_authorization` remains `unavailable_fail_closed`.

A denied unauthorized request is evidence of correct safety behavior, not necessarily a system failure.

### Step 7: Cross-check platform health and compatibility

Review platform health metrics for the audit window:

- Were BBB, Guardian, Master, Chroma, Hilbert, and sandbox services available as expected?
- If a service entered degraded mode, did traffic stop or use an explicitly safe fallback?
- Did ordinary Master processing continue after BBB promotion?
- Did EEG producers deliver accepted compatible pulses to the Master?
- Were emergency cleanup paths triggered, and if so, were they justified?
- Did operators bypass governance during outages, or did they respect the separation between governed and ungoverned behavior?

### Step 8: Document findings and actions

Summarize:

- which checks passed;
- which checks failed or raised concern;
- live image and rollback evidence;
- required remediation;
- whether rollback was considered or performed;
- what structural or procedural changes are needed for future robustness.

Document this in language that both technical and non-technical community members can understand.

---

## 40.13 Step-by-Step Operational Validation

Operational validation uses similar tools but focuses on behavior under normal load and over longer periods.

### Step 1: Define expected behaviors and thresholds

For each subsystem, define what good behavior looks like, such as:

- reasonable first-stage approval rates;
- maximum acceptable gate-error rates;
- minimum evidence requirements for approvals;
- maximum acceptable lag between event and temporal promotion;
- expected daily and hourly audit-table rows;
- BBB ordinary-request availability;
- zero unauthorized Guardian-governed approvals;
- Master health and successful normal pipeline completion;
- expected accepted EEG rhythm traffic where EEG producers are enabled.

### Step 2: Collect continuous metrics

Configure Ms. Allis to emit continuous metrics about:

- gate decisions: approved, suppressed, review, denied;
- readiness-score distributions;
- deduplicated evidence counts;
- promotion rates into durable tiers;
- external communication candidate outcomes;
- system-health indicators: uptime, latency, and error rates;
- successive `refresh_mv` admissible counts;
- BBB and Guardian denial outcomes;
- Master pipeline completion;
- EEG pulse acceptance and observed rhythm presence.

### Step 3: Compare actual behavior to thresholds

Over a chosen validation period, compare observed metrics to documented expectations:

- Are approval rates within an expected band?
- Are error types and rates acceptable?
- Are promotion rates stable and explainable?
- Are external communications following the intended pattern of caution?
- Does `runtime_governance.public_answer_audit` show the expected cadence?
- Are governed operations correctly unavailable while authority is unprovisioned?
- Does normal content filtering remain available?
- Does the Master remain healthy and compatible after changes?

### Step 4: Run scenario-based checks

Run specific scenarios such as:

- a batch of low-evidence packets;
- consent-missing memory candidates;
- spatial candidates outside allowed geography;
- external communication candidates with and without public opt-in;
- a manual call to `runtime_governance.refresh_public_admissible_gbim_mv()` followed by a check that a new `refresh_mv` row appears;
- a normal BBB request;
- a governed request with no credentials;
- a governed request with invalid credentials;
- a normal Master pipeline request;
- an EEG rhythm-status observation.

### Step 5: Close the loop

Use operational-validation results to:

- adjust thresholds and configuration;
- improve documentation and operator training;
- refine metrics and logging;
- correct defects;
- promote validated images;
- preserve rollback images;
- repeat the relevant smoke tests after every consequential change.

For rural developers, operational validation is not a one-time ceremony. It is a continuing discipline of checking, comparing, correcting, and documenting.

---

## 40.14 Relationship Between Audit, Validation, and Governance

Audit and operational validation sit alongside the governance mechanisms described in earlier chapters.

- **Governance** defines what should happen: gates, candidate schemas, consent rules, temporal tiers, and authority boundaries.
- **Operational evaluation** watches how those mechanisms behave in day-to-day running.
- **System audit** checks past behavior against governance design and commitments.
- **Operational validation** tests whether the system continues to meet commitments under realistic conditions.
- **Deployment validation** confirms that an image promotion behaves correctly in production and leaves a usable rollback path.

Together, they form a loop:

1. Design governed architecture.
2. Operate under that architecture.
3. Observe behavior, health, and metrics.
4. Audit records, logs, images, and request outcomes.
5. Validate normal, negative, and compatibility scenarios.
6. Promote a corrected image only after validation.
7. Retain a rollback image.
8. Re-test production behavior after promotion.
9. Adjust configuration and design where needed.

The two confirmed July 26 audit rows establish a durable database audit trail. The August 17 validation sequence adds a concrete runtime record: the BBB Guardian defect was reproduced, corrected in canary, promoted after behavior tests, checked in production, and verified for Master and EEG compatibility.

For rural developers, that loop is protection against quiet drift and unmanaged complexity. It keeps Ms. Allis answerable to its design, its operators, and the communities it serves.

---

## 40.15 Limits and Responsibilities

Even with audit and operational validation in place, some responsibilities remain outside the system.

System audit and operational validation do **not**:

- absolve operators, institutions, or communities of responsibility for how Ms. Allis is used;
- replace legal, ethical, or community review boards;
- provide automatic compliance with any specific regulation without additional work;
- guarantee that no harm can occur;
- make audit rows, health checks, or passing smoke tests a substitute for independent review;
- make the current intentionally unprovisioned Guardian authority path an active authorization system.

They **do**:

- make it easier to see and correct problematic patterns;
- provide evidence for discussion with regulators, communities, and researchers;
- reduce the risk of silent failure modes;
- create a durable, queryable record of database-layer governance behavior;
- show whether production services are running intended images and passing defined health checks;
- preserve proof that unauthorized governed operations fail closed;
- show whether ordinary processing remains compatible after security changes;
- retain a documented rollback path when a promotion must be reversed.

For rural communities, the message is clear: the system is designed to be **inspectable**. It will not be perfect, but its behavior should leave traces that can be audited and validated.

---

## 40.16 Closing Statement

System audit and operational validation are pillars of Ms. Allis’s accountable design. They ensure that staged, evaluated, emitted, and promoted packets can be traced; that gates can be examined; that authority failures remain closed; and that platform health is part of the story rather than an invisible assumption.

The `runtime_governance.public_answer_audit` table is the live audit artifact for the database-layer governance cycle. Its four columns — `audit_id`, `stage`, `detail jsonb`, and `created_at` — capture structured evidence of governance function execution. On July 26, 2026, two initial rows were confirmed: a `refresh_mv` row at 19:44:05 and a `lifecycle_snapshot` row at 19:44:06.

The August 17, 2026 operational validation record adds runtime evidence that the BBB Guardian integration was corrected from fail-open to fail-closed, normal BBB filtering remained operational, invalid Guardian credentials remained blocked with preserved HTTP 401 denial, the Master pipeline completed successfully after production promotion, and Delta, Theta, and Beta EEG rhythm telemetry was accepted by the Master compatibility interface.

The current Guardian state is explicit:

```text
governed operation authorization unavailable fail closed
```

That state is intentional. With zero active callers and zero active subject keys, `user-data-operationalization` cannot gain authority or obtain a PDR. Meanwhile, ordinary safeguarded system work continues through its applicable gates.

For rural developers, these tools transform Ms. Allis from a black box into an instrument that can be examined, questioned, repaired, rolled back when necessary, and improved. Audit and validation do not make the system infallible, but they make accountability concrete and technically inspectable.

---

*Chapter 40 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*  
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*  
*See LICENSE for terms.*
