# Appendix A: Admissibility Predicate
## The Ten-Condition Conjunction — As-Built, July 29, 2026

**Author:** C. A. Kidd — Mount Hope, West Virginia
**Last Updated:** July 29, 2026
**Status:** As-Built — Both Halves Fully Enforced — July 2026 Production Gate

> **Gate Corrections Applied (July 29, 2026):**
> The prior seven-condition conjunction has been superseded by the
> ten-condition conjunction (C1–C10). Three new conditions — C8, C9, C10 —
> were added on July 26, 2026 as part of the full spacetime/provenance
> schema migration. The Verification Discipline rule is now in force.
> All infrastructure corrections listed below are applied and sealed.

---

## What This Appendix Is About

This appendix defines the full admissibility predicate governing which rows
in `public.gbim_record` are visible to the public instrument. It is written
step by step for rural developers who need to understand, reproduce, or
extend the governed state model described in the main thesis.

The predicate is not aspirational. Every condition listed here is enforced
in production as of July 29, 2026 — at the database schema level, the
materialized view level, and the role access level. The Verification
Discipline rule below explains exactly what "enforced in production" must
mean before any claim may be retired from the "Not Yet Demonstrated"
register.

---

## A.1 The Ten-Condition Admissibility Conjunction (C1–C10)

For a row in `public.gbim_record` to appear in `public_admissible_gbim_mv`
and be accessible to `public_instrument_role`, it must satisfy **all ten**
of the following conditions simultaneously. Failure of any single condition
makes the row stored-but-inadmissible: visible to the governance role for
audit and repair, but invisible to the public instrument.

| Condition | Predicate | Notes |
|-----------|-----------|-------|
| C1 | `gbim_id IS NOT NULL` | Record identity — unchanged from prior version |
| C2 | `promotion_state = 'authorized'` | Governance gate — unchanged from prior version |
| C3 | `public_claim_allowed = true` | Public emission flag — unchanged from prior version |
| C4 | `under_whose_authority IS NOT NULL` | Provenance authority — unchanged from prior version |
| C5 | `company_name IS NOT NULL` | Provenance organization — unchanged from prior version |
| C6 | `ingested_at IS NOT NULL` | Memory event timestamp — unchanged from prior version |
| C7 | `degradation_status IN ('fresh', 'aging')` | Lifecycle freshness — unchanged from prior version |
| C8 | `spatial_unit_id IS NOT NULL` | Blockgroup GEOID — **added July 26, 2026** |
| C9 | `spatial_unit_kind IS NOT NULL` | Spatial kind anchor (`'blockgroup'` for all current records) — **added July 26, 2026** |
| C10 | `valid_time_start IS NOT NULL` | Temporal anchor (≥ 2020-01-01) — **added July 26, 2026** |

Conditions C1–C7 are unchanged from the prior seven-condition version.
Conditions C8–C10 are the spacetime extension: they enforce the **where**
(C8, C9) and the **when** (C10) of the spacetime contract defined in
Chapter 53.

### The Enforcing CHECK Constraint

C8–C10 are enforced at write time by the following database constraint on
`public.gbim_record`:

```sql
CONSTRAINT gbim_record_spacetime_provenance_chk CHECK (
  NOT (promotion_state = 'authorized' AND public_claim_allowed = true)
  OR (
    spatial_unit_id       IS NOT NULL
    AND spatial_unit_kind IS NOT NULL
    AND valid_time_start  IS NOT NULL
    AND under_whose_authority IS NOT NULL
    AND company_name      IS NOT NULL
    AND ingested_at       IS NOT NULL
  )
)
```

Any attempt to mark a row `authorized` and `public_claim_allowed = true`
without satisfying all six fields is rejected at the database level. The
predicate is not a post-hoc filter — it is a write barrier. Hallucinated
geography and unanchored temporal claims cannot enter the public evidence
surface because they are blocked before they can be committed.

### Step-by-Step for Rural Developers

1. **Start with your governance gate (C2, C3).** Every row must be
   explicitly promoted to `authorized` and flagged for public emission.
   Nothing becomes public by default.

2. **Require provenance (C4, C5, C6).** Every public row must name who
   authorized it, which organization it comes from, and when it was
   ingested. These are not metadata — they are admissibility conditions.

3. **Enforce lifecycle (C7).** A row that was `fresh` at ingestion becomes
   `aging` and then `stale` over time. Stale rows automatically fall out
   of the admissible set. Build a scheduler (see A.4) to maintain this
   automatically.

4. **Add the spacetime anchor (C8, C9, C10).** Every public civic claim
   must carry a geographic unit identity (`spatial_unit_id`), a geographic
   kind (`spatial_unit_kind`), and a policy effective date
   (`valid_time_start`). Without all three, the row cannot be public.

5. **Enforce at the write boundary, not only the read boundary.** Use a
   CHECK constraint so the predicate is checked when the row is written,
   not only when it is queried. An answer can be regenerated; a corrupted
   belief persists.

---

## A.2 The Verification Discipline Rule

**Any claim of live behavior must be demonstrated at two layers before it
may be removed from the "Not Yet Demonstrated" register:**

**Layer 1 — Service Running:** The relevant service, container, or function
must be confirmed healthy at runtime. This means an observed HTTP response,
a successful function invocation, or a verified container status — not a
configuration file asserting the service is intended to run.

**Layer 2 — Database State Confirmed:** The underlying database state that
the service depends on must be independently confirmed via a live `psql`
session or equivalent direct query. Service health alone does not confirm
that the evidence the service reads is admissible, current, or correctly
structured.

A claim satisfies the Verification Discipline rule only when **both** layers
have been observed and recorded. A claim that satisfies Layer 1 but not
Layer 2 remains on the "Not Yet Demonstrated" register with a note that
service health is confirmed but database state is pending.

### Why Two Layers Are Required

A service can be running and healthy while the database it reads from holds
stale, inadmissible, or incorrectly structured rows. Conversely, the
database can hold correctly structured admissible rows while the service
that reads them is down or misconfigured. Neither layer alone constitutes
proof of live civic behavior.

For rural developers running systems on laptops, shared machines, or
intermittent infrastructure: this rule protects you from the commonest
class of false confidence — "I can see the container is up" without
checking whether the data it serves is actually admissible.

---

## A.3 Infrastructure Corrections (Cross-Cutting)

The following items were corrected as part of the July 29, 2026 production
gate. Prior descriptions are removed and replaced with verified as-built
status.

### A.3.1 Audit Trace IDs

| Item | Prior Description (Removed) | Verified As-Built Status |
|------|------------------------------|--------------------------|
| Audit trace IDs | `query_id` hardcoded as a placeholder | Real trace IDs threaded through `public_answer_packet` and `public_geoid_panel` into `public_answer_audit`; every public claim invocation produces a durable UUID audit record |

The `public_answer_audit` table in the `runtime_governance` schema receives
a logged row on every invocation of `public_answer_packet`. The trace ID
is a real UUID drawn from the `gbim_record.gbim_id` of the evidence row
used to construct the answer, not a hardcoded placeholder. Downstream
systems may query `public_answer_audit` to reconstruct the provenance chain
for any answer the system has produced.

### A.3.2 pg_cron Target

| Item | Prior Description (Removed) | Verified As-Built Status |
|------|------------------------------|--------------------------|
| pg_cron lifecycle target | `gbim_runtime_lifecycle_hourly()` named as the cron target | `apply_runtime_lifecycle` is the correct function name called by all four scheduled jobs |

The four registered pg_cron jobs (`gbim-runtime-lifecycle-hourly`,
`gbim-runtime-lifecycle-daily`, `gbim-runtime-lifecycle-weekly`,
`gbim-runtime-lifecycle-monthly`) all invoke `apply_runtime_lifecycle` —
not the previously documented `gbim_runtime_lifecycle_hourly()`. Any
documentation, monitoring configuration, or operational runbook that
references the old function name must be updated to `apply_runtime_lifecycle`.

### A.3.3 Policy Service

| Item | Prior Description (Removed) | Verified As-Built Status |
|------|------------------------------|--------------------------|
| Policy service | "Not Yet Demonstrated" | `jarvis-crypto-policy` is healthy on port 8099; HMAC-SHA256 verified; secrets rotated as of July 29, 2026 |

`jarvis-crypto-policy` satisfies the Verification Discipline rule at both
layers: the service is confirmed running and responding on port 8099
(Layer 1), and the `civic_policy_fact` table it reads from carries verified
PY2026 SNAP eligibility rules with dual temporal axes — `recorded_at` and
`valid_time_start` — confirmed via live `psql` session (Layer 2). HMAC-SHA256
message authentication is in force; secrets have been rotated.

### A.3.4 geoguard_city

| Item | Prior Description (Removed) | Verified As-Built Status |
|------|------------------------------|--------------------------|
| `geoguard_city` | "Planned / empty" | Populated with verified data as of July 29, 2026 |

The `geoguard_city` table is no longer empty or planned. It holds the
verified city-level entries used by the geographic guard's lexical scope
check layer (described in Chapter 53, Section 9.2). The table was
populated as part of the July 29, 2026 production gate. Rural developers
extending the guard to a new region should populate this table from the
Census TIGER/Line places file for their region, following the same pattern
used for the West Virginia deployment.

### A.3.5 Contracts Container

| Item | Prior Description (Removed) | Verified As-Built Status |
|------|------------------------------|--------------------------|
| `jarvis-contracts` container | "Failing / ExitCode non-zero" | `jarvis-contracts` running (ExitCode 0); compiled artifacts confirmed |

The `jarvis-contracts` container previously failed to reach a healthy state.
As of July 29, 2026, the container is running with ExitCode 0 and compiled
artifacts have been confirmed present and loadable. The Verification
Discipline rule is satisfied at both layers: container status verified
(Layer 1) and contract artifact integrity confirmed (Layer 2).

---

## A.4 The Admissibility Lifecycle: Step-by-Step for Rural Developers

The admissibility predicate is a snapshot. What keeps it honest over time
is the lifecycle scheduler. The following steps describe how to reproduce
the full governed lifecycle in another rural deployment.

**Step 1: Define your admissibility conditions explicitly.**
Write them down as a numbered list. Every condition must be testable with
a SQL query. If you cannot write the SQL, the condition is not enforceable.

**Step 2: Encode the conditions in a CHECK constraint and a materialized
view.**
The CHECK constraint enforces conditions at write time. The materialized
view enforces them at read time. Both are required. One without the other
leaves a gap.

**Step 3: Create the role hierarchy.**
`runtime_governance_role` sees everything. `public_instrument_role` reads
only `public_admissible_gbim_mv`. Test the boundary directly: attempt a
direct SELECT from `public.gbim_record` as the public role and confirm
it returns a permission denied error.

**Step 4: Wire the four lifecycle jobs.**
Register hourly, daily, weekly, and monthly pg_cron jobs all calling
`apply_runtime_lifecycle`. Do not name the jobs after the function; name
them after the cadence (`gbim-runtime-lifecycle-hourly`, etc.) so
monitoring is readable without knowing the implementation.

**Step 5: Verify the scheduler at both layers.**
Confirm the cron jobs appear in `cron.job` with `active = true` (Layer 1).
Confirm that running the lifecycle function directly produces the expected
degradation state transitions in `public.gbim_record` (Layer 2).

**Step 6: Add the Verification Discipline rule to your project's definition
of done.**
Any feature, migration, or infrastructure change that claims to be "live"
must satisfy both layers before the claim is recorded in any document,
chapter, or audit log. A two-row table — "Layer 1: service confirmed" and
"Layer 2: database state confirmed" — is a sufficient record format.

**Step 7: Maintain the "Not Yet Demonstrated" register.**
Keep a running list of any behavior that has been designed but not yet
verified at both layers. Remove items only when both layers are confirmed.
This register is not a shame list — it is an honest inventory of the gap
between architecture and evidence.

---

## A.5 Verified Admissibility Counts (July 26, 2026)

The following snapshot was captured from a live
`runtime_governance.log_lifecycle_counts()` invocation on July 26, 2026:

```json
{
  "fresh": 237655,
  "aging": 0,
  "stale": 0,
  "authorized": 237655,
  "admissible_public": 93423,
  "inadmissible_public": 144232,
  "public_claim_allowed": 93423,
  "logged_at": "2026-07-26T19:44:06.530415-04:00"
}
```

The split — 93,423 admissible, 144,232 stored-but-inadmissible — is
correct by design. Many rows are held internally for governance and repair
purposes but are not authorized for public claim emission. The 144,232
inadmissible rows are not errors; they are rows that correctly fail one or
more of C1–C10 and are therefore correctly excluded from the public
evidence surface.

---

## A.6 The civic_policy_fact Table and PY2026 SNAP Eligibility

The `civic_policy_fact` table is live with dual temporal axes:

- **`recorded_at`** — when the fact was ingested (the memory event timestamp,
  equivalent to `ingested_at` in `gbim_record`)
- **`valid_time_start`** — the effective date of the policy rule itself
  (when the rule became legally operative under its governing program year)

These two timestamps are not the same and must not be conflated. A PY2026
SNAP income threshold was legally effective on October 1, 2025. It was
ingested into the system on a later date. The `valid_time_start` carries
the legal effective date; `recorded_at` carries the ingestion date. Both
are required by C6 and C10 respectively.

`commons_current_policy()` is returning verified PY2026 SNAP eligibility
rules as of July 29, 2026. This function satisfies the Verification
Discipline rule: the service (`jarvis-crypto-policy`, port 8099) is
confirmed healthy at Layer 1, and the `civic_policy_fact` rows it reads
carry both `recorded_at` and `valid_time_start` confirmed at Layer 2.

For rural developers: any civic policy claim your system makes — benefit
eligibility, income thresholds, application deadlines, program rules —
must carry a `valid_time_start` anchored to the governing program year.
Ingestion date is not a substitute for policy effective date. A system that
confuses the two will serve last year's rules as if they are current.

---

## A.7 Scope of This Appendix

This appendix governs one surface: the public civic evidence layer defined
by `public_admissible_gbim_mv` and enforced by `gbim_record_spacetime_provenance_chk`.

It does **not** govern:

- Private per-user conversational memory (Chapter 50)
- The geographic guard's runtime query evaluation (Chapter 53)
- The LLM ensemble or answer-phrasing layer (Chapter 33)
- Any clinical, legal, or safety-critical claim beyond civic benefit eligibility

The scope is narrow by design. A predicate that tries to govern every
surface at once is too broad to test and too vague to trust.

---

## A.8 Closing Statement

The ten-condition admissibility conjunction is not a checklist for idealized
future behavior. It is a description of what the production database enforces
today, confirmed at both layers required by the Verification Discipline rule.

Every infrastructure correction in A.3 was applied and sealed on July 29,
2026. Prior descriptions of failing containers, empty tables, placeholder
trace IDs, and undemonstrated services are removed and replaced with
verified as-built status.

For community members in Mount Hope and across West Virginia: the rows that
power Ms. Jarvis's civic answers have all passed ten independent checks
before they are allowed to reach you. If a row fails any one of those ten
checks, it stays in the internal governance layer — visible for repair, but
silent to the public instrument. That is what it means for admissibility to
be enforced rather than declared.

---

*Appendix A authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
*Sealed: July 29, 2026 — July 2026 Production Gate.*
*Prior seven-condition conjunction superseded by ten-condition conjunction (C1–C10).*
*Verification Discipline rule: in force.*
*Infrastructure corrections: applied and sealed.*
*`jarvis-crypto-policy`: healthy, port 8099, HMAC-SHA256, secrets rotated.*
*`geoguard_city`: populated as of July 29, 2026.*
*`jarvis-contracts`: ExitCode 0, compiled artifacts confirmed.*
