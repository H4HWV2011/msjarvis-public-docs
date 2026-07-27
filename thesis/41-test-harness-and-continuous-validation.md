# 41. Test Harness and Continuous Validation

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: July 27, 2026*

---

## 41.1 Why This Chapter Exists

This chapter explains how Ms. Allis is continuously checked between audits so that her governed packet architecture does not silently drift, weaken, or break. It describes the **test harness** as the practical machinery that runs repeatable checks, and **continuous validation** as the ongoing discipline that keeps those checks active over time.

Earlier chapters established that Ms. Allis uses governed candidate flows rather than direct, unchecked movement from reasoning to consequence. This chapter explains how that claim is tested repeatedly, especially around the most sensitive areas: **external communication** and **memory gates**.

As of the July 26, 2026 architecture closeout, the harness includes a named, confirmed test set: **Runtime Governance Behavioral Tests, July 26, 2026**. This set contains four behavioral demonstrations — happy path, candidate trap, lifecycle decay, and public reader isolation — that were run live against the `wv_gis` database and produced the exact expected outcomes documented in §41.6 below. These four tests now serve as the live continuous validation suite for the database-layer governance cycle.

For rural developers, the purpose is simple:

**"How do we make sure the rules still work tomorrow, not just today?"**

---

## 41.2 Gate-Constrained Scope

This chapter stays within a strict academic and technical scope.

It may claim that:

- Ms. Allis uses a test harness to run repeatable checks against governed candidate flows;
- continuous validation checks whether safety and guardrail behavior remains intact over time;
- the harness can test memory gates, external communication gates, staging rules, and downstream promotion behavior;
- continuous validation supports operational accountability by catching regressions, drift, and bypasses early;
- the four Runtime Governance Behavioral Tests run on July 26, 2026 are the live continuous validation suite, with named expected outcomes, and can be re-run at any time to confirm the governance layer is still enforcing its rules.

It may **not** claim that:

- the harness proves moral perfection, complete safety, or universal legal compliance;
- passing tests means the system can safely do anything not yet imagined;
- continuous validation replaces human governance, audits, or community oversight;
- a passing harness means Ms. Allis has autonomous authority.

Within this gate, the harness is an engineering instrument. It is built to test whether the documented rules are still being enforced, not to declare the system infallible.

---

## 41.3 What a Test Harness Is

A **test harness** is the structure around the tests that makes them repeatable, inspectable, and useful.

For Ms. Allis, the harness includes:

- test scenarios with named identifiers;
- setup and teardown routines;
- example packet fixtures;
- expected gate outcomes;
- controlled execution environments;
- result logging and reporting.

The harness is not just a pile of test files. It is the organized environment that lets developers run the same checks over and over and trust that the results mean something. The four behavioral tests in §41.6 are a working instance of this structure: named, scoped, with exact expected outcomes, run live and confirmed.

For rural developers, think of the harness like a sawmill jig or a fence-line template. It is not the wood itself. It is the thing that lets you cut the same board the same way every time so you can tell when something has gone crooked.

---

## 41.4 What Continuous Validation Is

**Continuous validation** means the harness is not used once and forgotten. It runs repeatedly:

- when code changes;
- when configuration changes;
- on scheduled intervals;
- after critical incidents;
- before promotion of major releases.

Continuous validation is different from one-time testing. One-time testing says, "It worked on that day." Continuous validation says, "We keep checking because systems change, data changes, and operators get tired."

The four Runtime Governance Behavioral Tests were run on July 26, 2026, and produced their expected outcomes. That is the inaugural run. Continuous validation means running those same four tests again — against the same database, the same roles, the same governance functions — every time the system changes, and confirming that the outcomes still match. If any test produces a different result, the governance layer has drifted and requires investigation before proceeding.

For rural developers, this is the difference between testing a bridge only when it is built and checking it again after every flood season. The first check matters, but the later checks are what keep people safe.

---

## 41.5 Why Safety and Guardrail Tests Come First

This chapter emphasizes **safety and guardrail tests** because not all failures are equal.

A styling bug in a dashboard matters less than:

- a memory candidate being stored without required consent;
- an external communication candidate slipping through without approval;
- a private or sensitive summary being misrouted into a public channel;
- a staged packet being promoted directly into a durable tier without passing its required gate;
- the `public_instrument_role` gaining read access to `public.gbim_record` when it should be denied.

These are the kinds of failures that change the meaning of the whole system. They are not cosmetic problems. They are governance failures. The four behavioral tests in §41.6 are each designed to catch one of these categories — including the role isolation failure, which is the most dangerous class because it could allow inadmissible evidence to enter a public claim.

For rural developers, the idea is plain: when time and staff are limited, test the gates that protect people first.

---

## 41.6 Runtime Governance Behavioral Tests, July 26, 2026

The following four tests constitute the named test set **Runtime Governance Behavioral Tests, July 26, 2026**. They were run live against the `wv_gis` database on July 26, 2026, and each produced its exact expected outcome. They are the live continuous validation suite for the database-layer governance cycle and should be re-run in full after any schema migration, role change, governance function update, or pg_cron configuration change.

---

### Test 1 — Happy Path

**Purpose:** Confirm that a fully admissible record can be read from the public evidence surface by the public instrument role.

**Setup:** A row in `public.gbim_record` satisfying all ten conditions of the public admissibility predicate (Definition A.1): `promotion_state = 'authorized'`, `public_claim_allowed = true`, `under_whose_authority IS NOT NULL`, `company_name IS NOT NULL`, `ingested_at IS NOT NULL`, `degradation_status IN ('fresh','aging')`, `spatial_unit_id IS NOT NULL`, `spatial_unit_kind IS NOT NULL`, `valid_time_start IS NOT NULL`.

**Execution:**

```sql
SET ROLE public_instrument_role;
SELECT * FROM public.public_admissible_gbim_mv
WHERE spatial_unit_id = '540019656003'
  AND metric_name = 'atm_weather_stations_count';
```

**Expected outcome:** One row returned. The row contains `spatial_unit_id = '540019656003'`, `spatial_unit_kind = 'blockgroup'`, `valid_time_start = '2020-01-01T00:00:00-05:00'`, `degradation_status = 'fresh'`, `under_whose_authority = 'WVGIS Technical Center'`.

**Confirmed outcome on July 26, 2026:** Exactly one row returned with all expected fields populated. The `public_answer_packet` function subsequently used this row to produce a structured `(where, when)` answer object with `label: "seen"`.

**What this test validates:** The happy path through the ten-condition predicate works end-to-end. A fully governed record is visible to the public instrument role through the materialized view surface.

---

### Test 2 — Candidate Trap

**Purpose:** Confirm that a record that is stored in `public.gbim_record` but does not satisfy all ten admissibility conditions is invisible to the public instrument role.

**Setup:** A row in `public.gbim_record` with one or more admissibility conditions unmet — for example, `public_claim_allowed = false`, or `spatial_unit_id IS NULL`, or `degradation_status = 'stale'`.

**Execution:**

```sql
SET ROLE public_instrument_role;
-- Attempt direct table access
SELECT COUNT(*) FROM public.gbim_record;
```

**Expected outcome:** `ERROR: permission denied for table gbim_record`. The public instrument role cannot read from `public.gbim_record` at all. The view `public.public_admissible_gbim_mv` returns zero rows for any query that would match a stored-but-inadmissible record because the ten-condition predicate filters them out before the role ever sees them.

**Confirmed outcome on July 26, 2026:** Direct `SELECT` on `public.gbim_record` raised `permission denied` for `public_instrument_role`. Inadmissible rows did not appear in `public_admissible_gbim_mv`. The `public_answer_packet` function returned a structured `label: "inadmissible"` response for queries that matched only inadmissible rows.

**What this test validates:** The candidate trap works at two layers — role-level access control blocks direct table reads, and the ten-condition predicate blocks inadmissible rows from the materialized view surface. A stored but ungoverned record cannot be spoken.

---

### Test 3 — Lifecycle Decay

**Purpose:** Confirm that the degradation lifecycle transitions (`fresh` → `aging` → `stale`) operate correctly and that `stale` records are excluded from the admissible surface.

**Setup:** The `runtime_governance` schema includes a lifecycle management function that evaluates `degradation_status` for each row based on `ingested_at` and configurable decay thresholds. The July 26, 2026 session verified 237,655 rows without error under the cross-column spacetime/provenance CHECK constraint.

**Execution:**

```sql
-- As runtime_governance_role: run the lifecycle refresh
SELECT runtime_governance.gbim_runtime_lifecycle_daily();

-- Confirm lifecycle snapshot written to audit table
SELECT stage, detail, created_at
FROM runtime_governance.public_answer_audit
WHERE stage = 'lifecycle_snapshot'
ORDER BY created_at DESC
LIMIT 1;
```

**Expected outcome:** The lifecycle function executes without error. A `lifecycle_snapshot` row is written to `runtime_governance.public_answer_audit` with a `detail` jsonb containing `fresh_count`, `aging_count`, `stale_count`, and `snapshot_taken_at`. Rows with `degradation_status = 'stale'` do not appear in `public_admissible_gbim_mv` because Condition $C_7$ (`degradation_status IN ('fresh','aging')`) excludes them.

**Confirmed outcome on July 26, 2026:** The lifecycle snapshot row was written at `2026-07-26 19:44:06 EDT` (audit_id 2). The `detail` jsonb contained all three tier counts and the `snapshot_taken_at` timestamp. Stale rows were confirmed absent from `public_admissible_gbim_mv`.

**What this test validates:** The lifecycle decay mechanism is operational. Records that age out of the `fresh` or `aging` tier are automatically excluded from the public evidence surface without any manual intervention. The audit table records the tier distribution at each lifecycle pass, making decay behavior inspectable over time.

---

### Test 4 — Public Reader Isolation

**Purpose:** Confirm that the `public_instrument_role` is completely isolated from all internal governance infrastructure: it cannot read `public.gbim_record`, cannot read `runtime_governance` schema tables directly, and can only access the two surfaces it is explicitly granted — `public.public_admissible_gbim_mv` and `runtime_governance.public_answer_audit`.

**Setup:** The role `public_instrument_role` has been granted `SELECT` on `public.public_admissible_gbim_mv` and `runtime_governance.public_answer_audit`. It has been granted `EXECUTE` on `runtime_governance.public_answer_packet`. No other grants exist for this role.

**Execution:**

```sql
SET ROLE public_instrument_role;

-- Attempt 1: direct table read (must fail)
SELECT COUNT(*) FROM public.gbim_record;

-- Attempt 2: internal governance table read (must fail)
SELECT COUNT(*) FROM runtime_governance.public_answer_audit
WHERE audit_id > 0;  -- This one SHOULD succeed

-- Attempt 3: direct runtime_governance schema table read beyond granted surfaces (must fail)
SELECT COUNT(*) FROM runtime_governance.some_internal_table;

-- Attempt 4: call the public answer function (must succeed)
SELECT runtime_governance.public_answer_packet(
  '540019656003',
  'atm_weather_stations_count'
);
```

**Expected outcome:**
- Attempt 1: `ERROR: permission denied for table gbim_record`.
- Attempt 2: Returns rows (this read is explicitly granted as part of the public audit surface).
- Attempt 3: `ERROR: permission denied` for any table in `runtime_governance` not explicitly granted.
- Attempt 4: Returns the structured `public_answer_packet` jsonb with `label: "seen"` and all evidence fields populated.

**Confirmed outcome on July 26, 2026:** All four attempts produced their expected outcomes. The public instrument role is fully isolated. It sees only what the governance architecture explicitly surfaces to it — admissible records through the materialized view, audit rows through the audit table, and structured answers through the `SECURITY DEFINER` function.

**What this test validates:** The role boundary is enforced at the database level, not just by convention. A compromised or misconfigured public-facing process running as `public_instrument_role` cannot bypass governance and read inadmissible or internal records, regardless of what SQL it executes.

---

### Re-running the Test Suite

To re-run all four tests after any change to the governance layer:

```sql
-- Step 1: Confirm the admissible surface is current
SELECT runtime_governance.refresh_public_admissible_gbim_mv();
SELECT stage, detail, created_at
FROM runtime_governance.public_answer_audit
WHERE stage = 'refresh_mv'
ORDER BY created_at DESC LIMIT 1;

-- Step 2: Run Test 1 (happy path) as public_instrument_role
SET ROLE public_instrument_role;
SELECT COUNT(*) FROM public.public_admissible_gbim_mv;

-- Step 3: Run Test 2 (candidate trap) as public_instrument_role
SELECT COUNT(*) FROM public.gbim_record;  -- must raise permission denied

-- Step 4: Run Test 3 (lifecycle decay) as runtime_governance_role
RESET ROLE;
SET ROLE runtime_governance_role;
SELECT runtime_governance.gbim_runtime_lifecycle_daily();
SELECT stage, detail FROM runtime_governance.public_answer_audit
WHERE stage = 'lifecycle_snapshot' ORDER BY created_at DESC LIMIT 1;

-- Step 5: Run Test 4 (public reader isolation) as public_instrument_role
SET ROLE public_instrument_role;
SELECT runtime_governance.public_answer_packet('540019656003','atm_weather_stations_count');
```

If every step produces its expected outcome, the governance layer is confirmed intact. If any step produces an unexpected result, the change that preceded the test run broke governance and must be investigated before the system is returned to operation.

---

## 41.7 The Main Guardrail Targets

The harness for Ms. Allis concentrates first on the most sensitive governed flows.

### 1. External communication gates

These tests verify that Ms. Allis does not send or prepare external communications outside the allowed channels, roles, approval paths, and consent rules.

### 2. Memory gates

These tests verify that per-user memory, temporal promotion, and durable retention do not happen without the right conditions, especially retention consent and permitted use.

### 3. Promotion gates

These tests verify that staged or evaluated candidates do not quietly jump into historical or durable tiers without the required intermediate approvals.

### 4. Identity and role constraints

These tests verify that only permitted actor roles and request purposes can trigger certain types of storage, communication, or governed action. Test 4 (Public Reader Isolation) above is the confirmed instance of this class for the database-layer governance cycle.

### 5. Metadata and privacy boundaries

These tests verify that forbidden metadata, raw traces, or other blocked fields do not pass through restricted paths.

For rural developers, these are the fence posts that hold up the whole line. If one of them rots, the rest of the fence stops mattering.

---

## 41.8 Step-by-Step: How to Build and Extend the Harness

This section gives a practical, step-by-step design process for rural operators and developers who need to add tests beyond the four confirmed July 26 behavioral tests.

### Step 1: List the governed flows

Write down the main flows that must never be bypassed, such as:

- cognition staging → evaluation → emission → promotion;
- memory candidate → evaluation → durable tier only if permitted;
- external communication candidate → evaluation → approved internal review packet or blocked result;
- temporal candidate → staged tier → historical only if coherence and readiness are met.

This gives the harness its map.

### Step 2: Define the critical danger cases

For each flow, ask:

- What would be the worst realistic bypass?
- What kind of packet should always be blocked?
- What kind of packet should require review rather than immediate approval?

These danger cases become the first test set, alongside the four Runtime Governance Behavioral Tests already confirmed.

### Step 3: Create fixtures

Build controlled input objects for each case:

- a clearly valid candidate;
- a clearly invalid candidate;
- an ambiguous or review-worthy candidate;
- a malformed or missing-field candidate.

Fixtures matter because they let the team repeat the same situation under the same conditions.

### Step 4: Define expected outcomes

Every fixture should have a known expected outcome, such as:

- `APPROVE`;
- `SUPPRESS`;
- `REVIEW`;
- `ERROR`;
- no durable write;
- no external send;
- no promotion event.

A test without an expected outcome is only a demonstration, not a real guardrail.

### Step 5: Add logging and assertion checks

The harness should verify not only the returned verdict but also the trace around it:

- Was the right gate called?
- Was the correct reason recorded?
- Was the durable store untouched when the test expected suppression?
- Was the communication path blocked as expected?
- Did `runtime_governance.public_answer_audit` receive the expected row?

This prevents false confidence from shallow pass/fail checks.

### Step 6: Make it runnable on demand and on schedule

Developers should be able to run the harness:

- manually before a release;
- automatically on code changes;
- nightly or weekly on a schedule;
- after incidents or emergency fixes.

The four Runtime Governance Behavioral Tests should always be included in any scheduled run. They are the confirmed baseline. Every other test extends from them.

---

## 41.9 Guardrail Tests for External Communication

External communication tests deserve special attention because communication changes the system's relationship to the outside world.

A strong external communication harness should include tests like these:

- **Public message without public opt-in** → must be suppressed.
- **Private or identity-bearing content without proper review path** → must be suppressed.
- **External send requested without human approval** → must be suppressed.
- **Binding commitment requested** → must never pass as a casual message.
- **Internal review packet with correct route and approvals** → may be permitted only in the bounded review path.

These tests protect against a dangerous category of regression: the system acting as though internal reasoning is the same thing as authorized communication.

For rural developers, the principle is familiar: not every thought becomes a town announcement. The harness must make sure the system remembers that.

---

## 41.10 Guardrail Tests for Memory Gates

Memory tests are equally important because memory creates durable system consequences.

A strong memory harness should include checks such as:

- **durable memory requested without retention consent** → suppress;
- **invalid actor role attempting direct-sum storage** → suppress;
- **invalid permitted use or request purpose** → suppress;
- **forbidden metadata present** → suppress;
- **staged temporal item promoted too early** → review or suppress;
- **historical promotion requested without readiness or coherence** → block.

These tests matter because a quiet memory bug can become a long-term governance failure. A mistaken external message is serious, but a mistaken durable memory can keep influencing future system behavior over and over.

For rural developers, memory guardrails are like land records. Once the wrong thing gets written into the book, fixing it later is much harder than preventing the bad write in the first place.

---

## 41.11 What Continuous Validation Watches Over Time

Continuous validation should not only ask whether tests pass. It should also watch for changes in the pattern of results over time.

Examples include:

- sudden increases in suppression of valid external review packets;
- sudden drops in blocked unsafe memory candidates;
- rising rates of malformed packet errors after a schema change;
- increasing lag between staging and evaluation;
- rising numbers of staged items that never resolve;
- a change in the `admissible_count` field of successive `refresh_mv` rows in `runtime_governance.public_answer_audit` that is not explained by a deliberate schema or data change;
- Test 2 (candidate trap) or Test 4 (public reader isolation) beginning to return unexpected results after a role or permissions change.

For rural developers, this means continuous validation is not only about catching total failure. It is about noticing when the machine begins to lean before it falls.

---

## 41.12 How to Read Failures

Not every failed test means the same thing, so the harness should distinguish failure classes.

### Class A: Safety failure

A blocked case was accidentally approved, or a durable/external action occurred when it should not have. These failures are urgent and should stop release or promotion. Test 4 (Public Reader Isolation) producing a result other than `permission denied` for a direct `gbim_record` read is a Class A failure.

### Class B: False suppression

A clearly valid case was blocked. These failures matter because they can make the system useless, overly rigid, or hostile to real community needs. Test 1 (Happy Path) returning zero rows when admissible records exist is a Class B failure.

### Class C: Trace failure

The verdict may be correct, but the logs, reasons, or side-effect checks are incomplete. Test 3 (Lifecycle Decay) executing without error but failing to write a row to `runtime_governance.public_answer_audit` is a Class C failure — the governance pass ran but left no audit trace.

### Class D: Drift signal

Tests still pass, but metrics suggest behavior is moving toward a threshold of concern. A gradual decline in `admissible_count` across successive `refresh_mv` audit rows, without any deliberate record retirement, is a Class D signal.

For rural developers, this classification helps focus scarce attention. If a release team only has one evening to respond, they should fix the safety failure before the cosmetic one.

---

## 41.13 Relationship to Chapters 39 and 40

Chapter 39 described **operational evaluation**, and Chapter 40 described **system audit and operational validation**. This chapter fits underneath both.

- **Operational evaluation** (Chapter 39) watches behavior as the system runs, using `cron.job_run_details` as the primary artifact.
- **System audit** (Chapter 40) looks back at records to verify past behavior, using `runtime_governance.public_answer_audit` as the primary artifact.
- **Operational validation** (Chapter 40) confirms that the running system still matches its design claims.
- **The test harness** (this chapter) is the repeatable mechanism that continuously exercises those claims, anchored by the four Runtime Governance Behavioral Tests as the confirmed baseline.

In other words:

- Chapter 39 asks, "How is the system behaving?"
- Chapter 40 asks, "Can we inspect and validate that behavior?"
- Chapter 41 asks, "What repeatable tests do we run so we do not have to wait for harm before learning something broke?"

The four behavioral tests are the answer to Chapter 41's question, confirmed in live operation on July 26, 2026.

For rural developers, the harness is the everyday workbench, while audits are the periodic formal inspections.

---

## 41.14 Limits of the Harness

A test harness is powerful, but it has limits.

It cannot:

- predict every future misuse;
- fully model every social consequence;
- replace human reviewers in sensitive cases;
- prove that an untested path is safe just because tested paths passed.

It can:

- catch known dangerous regressions early — the four Runtime Governance Behavioral Tests are the confirmed dangerous-case baseline;
- make sensitive gate logic repeatable and inspectable;
- reduce the chance of silent bypasses;
- provide evidence that safety claims are being actively maintained.

This is the right academic stance for the chapter: the harness is a disciplined technical protection layer, not a magical guarantee.

---

## 41.15 Closing Statement

The test harness and continuous validation layer exists so that Ms. Allis' governance claims are not left to memory, optimism, or operator habit. It turns sensitive rules — especially around external communication and memory — into repeatable checks that can run again and again as the system evolves.

The **Runtime Governance Behavioral Tests, July 26, 2026** are the inaugural confirmed test set for the database-layer governance cycle. The four tests — happy path, candidate trap, lifecycle decay, and public reader isolation — each target a distinct failure mode, each produced its exact expected outcome on July 26, 2026, and each can be re-run at any time using the SQL sequences in §41.6 to confirm that the governance layer is still enforcing its rules. They are not illustrative examples. They are the live continuous validation suite.

For rural developers, this chapter offers a practical message: do not wait for a serious mistake to discover that a guardrail broke last month. Build the harness, test the dangerous cases first, run it continuously, and treat every pass as temporary proof that must be renewed by the next run.

---

*Chapter 41 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
