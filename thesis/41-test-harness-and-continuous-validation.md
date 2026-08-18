# 41 — Test Harness and Continuous Validation

*Carrie Kidd (Mamma Kidd) — Mount Hope, West Virginia*  
*Last Updated: August 17, 2026*

---

## 41.1 Purpose of the Test Harness

This chapter explains how Ms. Jarvis keeps itself honest over time by exercising a **test harness** rather than relying only on one-off proofs. The goal is to show that key governance behaviors keep working after restarts, schema changes, image promotions, and new code, not just once during development.

For rural developers, a test harness is simply a repeatable set of scripts and checks that you can run to answer a practical question: “Is the system still behaving the way the thesis says it should?” Continuous validation means those scripts are used whenever the system changes, not just when it is first set up.

---

## 41.2 What Counts as Continuous Validation

Continuous validation in this architecture has three parts:

- **Named tests** that correspond to specific thesis claims.
- **Expected outcomes** that can be compared with live results.
- **Routines for rerunning tests** whenever critical code, images, schema, routing, or configuration changes occur.

The point is to treat the system like a machine that needs regular inspection. You do not wait for a failure to ask whether gates are working. You rerun the tests anytime you adjust the parts that those gates depend on.

This chapter focuses on the **Runtime Governance Behavioral Tests, July 26, 2026**, together with the **BBB, Guardian, Master, and EEG Compatibility Smoke Tests, August 17, 2026**.

---

## 41.3 The Runtime Governance Behavioral Test Set

On July 26, 2026, four core runtime-governance behaviors were exercised and confirmed:

1. **Happy Path** — admissible records behave as expected.
2. **Candidate Trap** — candidate-only material cannot leak into the public evidence path.
3. **Lifecycle Decay** — stale records are removed from public speakability.
4. **Public Reader Isolation** — the public role cannot see raw governed records.

Together, these four form the test set named:

```text
Runtime Governance Behavioral Tests, July 26, 2026
```

This chapter treats that set as a baseline harness. New behavior-focused tests, such as the overflow gate smoke test and the August 17 BBB, Guardian, Master, and EEG compatibility tests, belong in the same family. They extend the harness rather than replace it.

---

## 41.4 Test 1 — Happy Path

### 41.4.1 Intent

The happy path test answers the question: “When the system has fresh, authorized, public-claim-allowed records, does the admissible evidence view show them correctly?”

In other words, it checks that the **normal case** works: the system should not only block bad records; it should serve good ones reliably.

### 41.4.2 Procedure

The test script performs three basic steps:

1. Refresh the admissible materialized view.
2. Query the top admissible records, such as blockgroup-level counts from the spatial body.
3. Confirm that:

   - `promotion_state = 'authorized'`
   - `public_claim_allowed = true`
   - `degradation_status = 'fresh'`

appear in the returned rows.

A rural developer can think of this as looking up a fresh store shelf — the question is whether the shelf holds the items it should hold.

### 41.4.3 Expected Outcome

The expected outcome is:

- A non-zero count of admissible rows.
- Records that match the governed schema and lifecycle rules.
- Values that align with the known spatial and temporal anchors.

If the happy path test returns no admissible rows or shows wrong lifecycle or promotion states, then the basic serving path is broken and must be repaired before further tests are trusted.

---

## 41.5 Test 2 — Candidate Trap

### 41.5.1 Intent

The candidate trap test checks that **candidate-only material cannot leak into the public evidence path**, even if the underlying table contains it.

This guards against the risk that someone might mark a record as “candidate” but still accidentally expose it through the public interface.

### 41.5.2 Procedure

The test performs the following:

1. Choose one authorized and public-claim-allowed record.
2. Flip it to:

   - `promotion_state = 'candidate'`
   - `public_claim_allowed = false`
3. Refresh the admissible materialized view.
4. Count:

   - Candidate rows in the raw table.
   - Admissible rows in the view.

### 41.5.3 Expected Outcome

The expected outcome is:

- The raw table shows one candidate row.
- The admissible view shows **zero** rows corresponding to that candidate.
- The candidate does not appear in public evidence queries.

This confirms the candidate trap: moving a record into candidate status closes the public path for that record. For rural developers, this test shows that tentative material is not accidentally treated as truth.

---

## 41.6 Test 3 — Lifecycle Decay

### 41.6.1 Intent

The lifecycle decay test verifies that **stale records are automatically removed from public speakability**. A record is not supposed to remain admissible forever; its degradation status must respond to time.

### 41.6.2 Procedure

The test:

1. Select an admissible record with:

   - `degradation_status = 'fresh'`
2. Push its `ingested_at` timestamp back by a chosen interval, such as 18 months.
3. Run the lifecycle refresh function.
4. Refresh the admissible materialized view.
5. Inspect:

   - The record’s new `degradation_status`.
   - Whether it still appears in the admissible view.

### 41.6.3 Expected Outcome

The expected outcome is:

- The record’s `degradation_status` becomes `'stale'`.
- The record no longer appears in the admissible view.
- The public speakability count adjusts accordingly.

For rural developers, this test means that old data does not quietly remain publicly authoritative. The system knows how to age records out of the public surface.

---

## 41.7 Test 4 — Public Reader Isolation

### 41.7.1 Intent

The public reader isolation test ensures that **the public-facing role can see only admissible evidence and audit records**, not raw governed tables.

This is the core non-surveillance boundary in the system: the public instrument should not be able to introspect every raw record.

### 41.7.2 Procedure

The test:

1. Switch to the public reader role.
2. Attempt to:

   - Select from the admissible view.
   - Select from the audit table.
   - Select directly from the raw governed table.

### 41.7.3 Expected Outcome

The expected outcome is:

- Selecting from the admissible view succeeds.
- Selecting from the audit table succeeds.
- Selecting from the raw governed table fails with a permission error.

For rural developers, this test proves that public tools work on committed, governed evidence only. They cannot silently browse internal state.

---

## 41.8 Overflow Gate Smoke Test as a Behavioral Test

### 41.8.1 Intent

The overflow smoke test belongs in the same behavioral test suite because it checks that **three gates around person-space and overflow** work together:

1. Cognition promotion.
2. Person-space validation.
3. Overflow minimization and queue behavior.

It is not just a check on one function. It exercises a full path: cognition → person-space → overflow queue.

### 41.8.2 Procedure

The test script:

1. Stages a cognition packet.
2. Evaluates and promotes it, capturing a readiness score.
3. Constructs a `person_space_event` and validates it with a `person_space_validation` result.
4. Enqueues a minimized public-context event into the overflow queue:

   ```text
   overflow:queue:overflow_retriable_public_context
   ```

5. Checks that queue depth changes from `0` to `1`.
6. Inspects the queued event to confirm it contains only allowlisted public-context fields.

### 41.8.3 Expected Outcome

The expected outcome is:

- A staged packet becomes approved and promoted with a readiness score.
- The promoted record carries a valid `person_space_event` and `person_space_validation.ok = true`.
- The overflow queue key matches the expected lane.
- Queue depth rises from 0 to 1.
- The queued event is minimized, containing only fields such as `entity_id`, `event_timestamp`, `public_role_state`, `agency_state`, `consent_scope`, `truth_score`, `spatial_ref`, `person_ref`, `promotion_reason`, `priority`, `ttl_class`, and `retry_count`.

This test shows that the system can handle overflow in a way that respects person-space stability and privacy. For rural developers, it is a direct demonstration that bounded overflow is not just a design sketch; it works in code.

---

## 41.9 BBB, Guardian, Master, and EEG Compatibility Smoke Tests

The August 17, 2026 validation added a concrete smoke-test group for the live Blood-Brain Barrier, Constitutional Guardian boundary, Neurobiological Master, and EEG compatibility interface.

This group verifies that:

- ordinary BBB content filtering remains functional;
- explicitly governed operations deny when authorization is missing or invalid;
- Guardian HTTP denial cannot be transformed into a BBB allow;
- the Neurobiological Master pipeline remains healthy after BBB promotion;
- Delta, Theta, and Beta rhythm telemetry is accepted by the Master compatibility interface.

Together, these tests provide a direct operational check of the fail-closed remediation and its compatibility with the existing neurobiological pipeline.

---

## 41.10 Test 5 — Normal BBB Request

### 41.10.1 Intent

The normal BBB request test verifies that ordinary `content_filter` traffic remains available after the fail-closed Guardian remediation.

The test checks an important distinction: generic content filtering is evaluated by BBB’s local safeguards. It is not falsely represented as a completed Guardian/PDR authorization.

### 41.10.2 Procedure

Send a normal request to the live BBB filter route:

```text
POST http://jarvis-blood-brain-barrier:8016/filter
```

Use a non-governed operation class:

```json
{
  "content": "Production BBB compatibility smoke test.",
  "actor_role": "system",
  "context": "bbb_guardian_production_smoke",
  "action_type": "content_filter"
}
```

Inspect the response fields:

- `content_approved`
- `constitutional_check.applicable`
- `constitutional_check.allowed`
- `constitutional_check.decision`
- `blocked_by`

### 41.10.3 Expected Outcome

The expected result is:

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

This means:

- local BBB safeguards evaluated the content;
- the content passed those applicable safeguards;
- Guardian/PDR authorization was not falsely claimed for ordinary filtering;
- no constitutional block occurred.

A normal request that unexpectedly produces a Guardian allow, a Guardian error allow, or a failure to apply local safeguards should be treated as a regression.

---

## 41.11 Test 6 — Governed Request Missing Credentials

### 41.11.1 Intent

The governed-request-missing-credentials test verifies local fail-closed behavior before an incomplete request reaches Guardian.

The test proves that a request explicitly classified as `user-data-operationalization` cannot proceed without the two required authorization headers:

- `X-Caller-Token`
- `X-Operation-Intent`

### 41.11.2 Procedure

Send a request to the BBB filter route with the governed operation class but without the authorization headers:

```text
POST http://jarvis-blood-brain-barrier:8016/filter
```

```json
{
  "content": "Production BBB governed operation negative test.",
  "actor_role": "system",
  "context": "bbb_guardian_production_smoke",
  "action_type": "user-data-operationalization"
}
```

Inspect:

- `content_approved`
- `blocked_by`
- `constitutional_check.applicable`
- `constitutional_check.allowed`
- `constitutional_check.decision`

### 41.11.3 Expected Outcome

The expected result is:

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

The BBB should block this request locally. It should not create substitute credentials, call Guardian with invented values, or downgrade the missing authorization into a warning.

---

## 41.12 Test 7 — Governed Request with Invalid Credentials

### 41.12.1 Intent

The invalid-credentials test verifies that BBB preserves a Guardian denial rather than converting it into an allow.

This is the direct regression test for the historic fail-open defect. Guardian previously returned HTTP 401 to unauthorized BBB requests, and BBB incorrectly converted the resulting error into an allow. The remediated behavior must preserve the denial.

### 41.12.2 Procedure

Send a governed request with deliberately invalid headers:

```text
POST http://jarvis-blood-brain-barrier:8016/filter
```

```json
{
  "content": "Guardian authorization negative validation.",
  "actor_role": "system",
  "context": "bbb_guardian_production_validation",
  "action_type": "user-data-operationalization"
}
```

Use the following non-secret invalid test headers:

```text
X-Caller-Token: invalid-production-validation-token
X-Operation-Intent: invalid-production-validation-intent
```

Inspect:

- HTTP status returned by BBB;
- `content_approved`;
- `blocked_by`;
- `constitutional_check.applicable`;
- `constitutional_check.allowed`;
- `constitutional_check.decision`;
- `constitutional_check.guardian_status_code`.

### 41.12.3 Expected Outcome

The expected result is:

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

The BBB response itself remains HTTP 200 because the BBB successfully processed and denied the request. The meaningful security result is inside the response: the governed action is blocked and Guardian’s HTTP 401 denial is preserved.

Any result containing `allowed: true`, `content_approved: true`, `guardian_error` as an allow, or “fail-safe allow” is a critical regression.

---

## 41.13 Test 8 — Master End-to-End Pipeline

### 41.13.1 Intent

The Master end-to-end pipeline test verifies that the BBB fail-closed remediation does not break ordinary neurobiological processing.

The Master must continue to process normal content through the established integration path, including BBB, I-Containers, Qualia, and consciousness-bridge fallback behavior.

### 41.13.2 Procedure

From an authorized peer container on `qualia-net`, send a normal processing request to the Master:

```text
POST http://jarvis-neurobiological-master:8018/biological_process
```

```json
{
  "message": "Post-BBB fail-closed production integration smoke test."
}
```

Inspect:

- HTTP status;
- overall completion status;
- integrated-processing state;
- BBB `content_approved`;
- Guardian applicability and decision;
- I-Containers presence;
- Qualia status;
- bridge status.

### 41.13.3 Expected Outcome

The expected result is:

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

A bridge fallback result of `degraded` may appear as the existing bridge status. That fallback status is not evidence that the BBB remediation failed, provided the Master completes integrated processing and the expected BBB, I-Containers, and Qualia results remain present.

This test demonstrates that ordinary processing remains available while the specialized Guardian-governed operation remains intentionally fail closed.

---

## 41.14 Test 9 — EEG Rhythm Observation

### 41.14.1 Intent

The EEG rhythm observation test verifies that the Neurobiological Master’s compatibility interface accepts live rhythm telemetry and reports the latest observed pulse for each rhythm.

The test confirms that EEG compatibility did not disturb the established Master pipeline and that EEG producers post to the Master rather than to an old unavailable route.

### 41.14.2 Procedure

Observe the Master compatibility interface:

```text
GET http://jarvis-neurobiological-master:8018/eeg_pulse/status
```

Verify that the live EEG producer services post compatible telemetry to:

```text
POST http://jarvis-neurobiological-master:8018/eeg_pulse
```

A compatible EEG pulse includes a rhythm, pulse value, timestamp, and optional payload:

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

Inspect:

- the HTTP result for submitted pulses;
- the accepted rhythm and pulse values;
- the `rhythms` object in `/eeg_pulse/status`;
- Master logs for accepted rhythm messages and HTTP 202 responses;
- absence of `/eeg_pulse` or `/eeg_pulse/status` 404 responses.

### 41.14.3 Expected Outcome

The expected behavior is:

- `POST /eeg_pulse` returns HTTP 202 Accepted.
- The response identifies the accepted rhythm and pulse.
- `GET /eeg_pulse/status` returns HTTP 200 with `status: "ok"`.
- The status response contains the latest process-local record for each observed rhythm.
- Delta, Theta, and Beta appear after their live producers have reported.
- Master logs record accepted pulse events and HTTP 202 responses.
- No EEG endpoint 404 errors appear during the observation window.

A representative successful status summary is:

```json
{
  "received_rhythms": [
    "beta",
    "delta",
    "theta"
  ],
  "status": "ok"
}
```

The EEG status endpoint is intentionally in memory and process local. It reports the latest accepted pulse for each rhythm during the current Master container lifetime. It is not a durable telemetry database, a clinical EEG record, a medical diagnostic surface, or a promotion-authority mechanism.

---

## 41.15 How to Run the Test Suite

For this chapter, the test harness is organized conceptually rather than tied to one toolchain. The steps below assume a developer has access to the relevant scripts, containers, and database.

### 41.15.1 Before Running

Before running the tests:

- Ensure the database and runtime governance schema are up-to-date.
- Confirm that the admissible view and audit table exist and are not empty.
- Confirm that the relevant Docker containers are running and attached to their expected networks.
- Confirm that BBB, Guardian, and Master health endpoints respond.
- Make sure you understand which environment you are testing: development, staging, canary, or production.
- Record the current service image and rollback image before replacing a production container.

Running tests in the wrong environment can interfere with live data. For rural developers working with limited resources, this means carefully choosing a safe testing environment and keeping rollback evidence available.

### 41.15.2 Recommended Test Order

The recommended order is:

1. Happy Path — check that the admissible surface is healthy.
2. Candidate Trap — verify candidate suppression.
3. Lifecycle Decay — confirm stale-record removal.
4. Public Reader Isolation — verify role boundaries.
5. Overflow Gate Smoke Test — exercise the cognition-to-overflow path.
6. Normal BBB Request — verify ordinary local filtering.
7. Governed Request Missing Credentials — verify local fail-closed blocking.
8. Governed Request with Invalid Credentials — verify Guardian HTTP 401 denial is preserved.
9. Master End-to-End Pipeline — verify ordinary neurobiological integration remains intact.
10. EEG Rhythm Observation — verify accepted Delta, Theta, and Beta telemetry.

Each test should log:

- the time of the run;
- the image or revision under test;
- any modifications made during the test;
- the observed outcome;
- the expected outcome;
- any rollback action required.

If any critical test fails, the system should be treated as not fully aligned with the thesis claims until the failure is explained, contained, and corrected.

---

## 41.16 Implementation Status

**Runtime Governance Behavioral Tests, July 26, 2026: Demonstrated.**

As of July 26, 2026:

- All four core runtime-governance behavioral tests — happy path, candidate trap, lifecycle decay, and public reader isolation — have been exercised successfully against live GBIM state.
- The overflow gate smoke test has demonstrated a complete cognition-to-overflow path with minimized person-space events and bounded queue behavior.
- Together, these tests form the named test set:

  ```text
  Runtime Governance Behavioral Tests, July 26, 2026
  ```

**BBB, Guardian, Master, and EEG Compatibility Smoke Tests, August 17, 2026: Demonstrated.**

As of August 17, 2026:

- The fail-open BBB Guardian-integration defect was reproduced, isolated in a canary, and remediated.
- Normal `content_filter` traffic was confirmed to pass local BBB safeguards while recording Guardian as `not_applicable`.
- A governed request without credentials was blocked locally.
- A governed request with invalid credentials reached Guardian, received HTTP 401, and remained blocked.
- The remediated BBB image was promoted successfully to production.
- The Master end-to-end pipeline completed successfully after the BBB promotion.
- Delta, Theta, and Beta telemetry was accepted by the Master EEG compatibility interface with HTTP 202.
- The Master reported the latest observed rhythm records through its process-local in-memory status route.

Within the academic scope of this chapter, the system is permitted to claim that continuous validation of governance behavior, fail-closed authorization behavior, neurobiological integration, and EEG compatibility is not a theoretical plan but a demonstrated practice.

---

## 41.17 Step-by-Step Summary for Rural Developers

When reading or using this chapter, rural developers can follow this checklist:

1. **Know what is being tested.**  
   Each test corresponds to a specific thesis claim about governance behavior, safety boundaries, routing, or operational compatibility.

2. **Understand the expected outcome.**  
   The chapter lays out what should happen for each test, including what must be blocked.

3. **Run the tests in a safe environment.**  
   Avoid running state-changing tests against live production without proper safeguards, approval, and rollback preparation.

4. **Compare outcomes to expectations.**  
   Use discrepancies as a signal to investigate and correct behavior.

5. **Treat denial as a successful result when the request is unauthorized.**  
   A governed request with missing or invalid authority should be blocked. That is proof that the gate works.

6. **Treat the test suite as a living tool.**  
   New tests, such as the EEG compatibility observation and Guardian-denial regression test, should be added as new behaviors are implemented.

7. **Stay within scope.**  
   This chapter does not claim that every possible behavior is tested. It documents concrete, named behavioral tests that cover critical runtime governance, overflow, BBB, Guardian, Master, and EEG patterns as of late July and August 2026.

---

## 41.18 Closing

A test harness is the system’s way of practicing accountability. The **Runtime Governance Behavioral Tests, July 26, 2026** and the **BBB, Guardian, Master, and EEG Compatibility Smoke Tests, August 17, 2026** show that Ms. Jarvis can check itself for correct governance behavior on demand.

By naming the tests, stating their expected outcomes, recording failure modes, preserving rollback paths, and treating them as continuous validation tools, this chapter keeps the thesis tied to observable, rerunnable behavior rather than one-time assertions.

For rural developers, this means that the system’s most important promises — about candidate suppression, lifecycle decay, role isolation, bounded overflow, local BBB filtering, fail-closed Guardian behavior, Master pipeline continuity, and EEG compatibility — can be verified in practice, not just trusted in theory.
