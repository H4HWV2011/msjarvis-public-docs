# 41 — Test Harness and Continuous Validation

*Carrie Kidd (Mamma Kidd) — Mount Hope, West Virginia*  
*Last Updated: July 27, 2026*

---

## 41.1 Purpose of the Test Harness

This chapter explains how Ms. Jarvis keeps itself honest over time by exercising a **test harness** rather than relying only on one-off proofs. The goal is to show that key governance behaviors keep working after restarts, schema changes, and new code, not just once during development.

For rural developers, a test harness is simply a repeatable set of scripts and checks that you can run to answer a practical question: “Is the system still behaving the way the thesis says it should?” Continuous validation means those scripts are used whenever the system changes, not just when it is first set up.

---

## 41.2 What Counts as Continuous Validation

Continuous validation in this architecture has three parts:

- **Named tests** that correspond to specific thesis claims.
- **Expected outcomes** that can be compared with live results.
- **Routines for rerunning tests** whenever critical code or schema changes occur.

The point is to treat the system like a machine that needs regular inspection. You do not wait for a failure to ask whether gates are working. You rerun the tests anytime you adjust the parts that those gates depend on.

This chapter focuses on one named set of tests: the **Runtime Governance Behavioral Tests, July 26, 2026**.

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

This chapter treats that set as a baseline harness. New behavior-focused tests, such as the overflow gate smoke test, belong in the same family. They extend the harness rather than replace it.

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
2. Push its `ingested_at` timestamp back by a chosen interval (for example, 18 months).
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

## 41.9 How to Run the Test Suite

For this chapter, the test harness is organized conceptually rather than tied to a particular toolchain. The steps below assume a developer has access to the relevant scripts and database.

### 41.9.1 Before Running

Before running the tests:

- Ensure the database and runtime governance schema are up-to-date.
- Confirm that the admissible view and audit table exist and are not empty.
- Make sure you understand which environment you are testing (development, staging, or production).

Running tests in the wrong environment can interfere with live data. For rural developers working with limited resources, this means carefully choosing a safe testing environment.

### 41.9.2 Running the Tests

The recommended order is:

1. Happy Path — check that the admissible surface is healthy.
2. Candidate Trap — verify candidate suppression.
3. Lifecycle Decay — confirm stale record removal.
4. Public Reader Isolation — verify role boundaries.
5. Overflow Gate Smoke Test — exercise the cognition-to-overflow path.

Each test should log:

- The time of the run.
- Any modifications made during the test.
- The observed outcomes.

If any test fails, the system should be treated as not fully aligned with the thesis claims until the failure is explained and corrected.

---

## 41.10 Implementation Status

**Runtime Governance Behavioral Tests, July 26, 2026: Demonstrated.**

As of July 26, 2026:

- All four core runtime-governance behavioral tests — happy path, candidate trap, lifecycle decay, and public reader isolation — have been exercised successfully against live GBIM state.
- The overflow gate smoke test has demonstrated a complete cognition-to-overflow path with minimized person-space events and bounded queue behavior.
- Together, these tests form the named test set:

  ```text
  Runtime Governance Behavioral Tests, July 26, 2026
  ```

Within the academic scope of this chapter, the system is permitted to claim that continuous validation of governance behavior is not a theoretical plan but a demonstrated practice.

---

## 41.11 Step-by-Step Summary for Rural Developers

When reading or using this chapter, rural developers can follow this checklist:

1. **Know what is being tested.**  
   Each test corresponds to a specific thesis claim about governance behavior.

2. **Understand the expected outcome.**  
   The chapter lays out what should happen for each test.

3. **Run the tests in a safe environment.**  
   Avoid running them against live production without proper safeguards.

4. **Compare outcomes to expectations.**  
   Use discrepancies as a signal to investigate and correct behavior.

5. **Treat the test suite as a living tool.**  
   New tests, like the overflow smoke test, should be added as new behaviors are implemented.

6. **Stay within scope.**  
   This chapter does not claim that every possible behavior is tested. It documents a concrete, named set of behavioral tests that cover the most critical runtime governance and overflow patterns as of late July 2026.

---

## 41.12 Closing

A test harness is the system’s way of practicing accountability. The **Runtime Governance Behavioral Tests, July 26, 2026** show that Ms. Jarvis can check itself for correct governance behavior on demand. By naming the tests, stating their expected outcomes, and treating them as a continuous validation tool, this chapter keeps the thesis tied to observable, rerunnable behavior rather than one-time assertions.

For rural developers, this means that the system’s most important promises — about candidate suppression, lifecycle decay, role isolation, and bounded overflow — can be verified in practice, not just trusted in theory.
