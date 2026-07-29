# 53 — The Spacetime Contract

*Carrie Kidd (Mamma Kidd) — Mount Hope, West Virginia*
*Last Updated: July 29, 2026*
*Status: As-Built — Both Halves Fully Enforced — July 2026 Production Gate*

> **Gate Corrections Applied (July 29, 2026):**
> The heading "The Half Not Yet Enforced: Time-Sensitive Civic Facts" is
> removed and superseded. The `civic_policy_fact` table is live with dual
> temporal axes (`recorded_at` vs. `valid_time_start`). The function
> `commons_current_policy()` is returning verified PY2026 SNAP eligibility
> rules. Both halves of the spacetime contract — **where** and **when** —
> are fully enforced in production as of July 29, 2026.

---

## What This Chapter Is About

This chapter explains how Ms. Jarvis is prevented from inventing geography,
committing hallucinated places to permanent memory, or making civic policy
claims that are not anchored to a specific time.

The core question for rural developers is:

> "How does the system know *where* a question is about, what it does when
> it does not know, and how does that same discipline protect the system's
> permanent memory and its time-sensitive civic facts?"

The answer is the **spacetime contract**: a rule that no grounded civic claim
may be made or committed to memory unless the system can produce a
trustworthy `(where, when)` coordinate pair it actually retrieved.

**This chapter may claim:**

- A three-layer geographic guard (distance ceiling, lexical scope check,
  authoritative place list) is live and tested in production
- The `gbim_record_spacetime_provenance_chk` CHECK constraint enforces the
  full spacetime contract at the database schema level
- `public_admissible_gbim_mv` enforces a ten-condition admissibility
  predicate, and the public instrument role reads only from this view
- `runtime_governance.public_answer_packet()` returns fully provenanced
  `(where, when)` answer objects at runtime
- The `civic_policy_fact` table is live with dual temporal axes:
  `recorded_at` (ingestion timestamp) and `valid_time_start` (policy
  effective date)
- `commons_current_policy()` is returning verified PY2026 SNAP eligibility
  rules
- Both halves of the spacetime contract are fully enforced in production

**This chapter must not claim:**

- That the geographic guard catches every possible out-of-scope query
  (the out-of-state city list is finite; vague paraphrases can evade lexical
  checks)
- Clinical, legal, or universal safety guarantees
- That the spacetime contract governs private per-user memory (it does not —
  that pipeline is governed by Chapter 50)

---

## 53.1 Why This Is Called a Spacetime Contract

The title is intentionally metaphorical but disciplined. In physics, spacetime
provides the coordinate structure within which events can be located. In the
same engineered sense, Ms. Jarvis is not allowed to make a grounded civic
claim unless it can be placed at an explicit **where** and a specific **when**.

The contract is a rule for system behavior, not a claim about physics:

- **Where:** a canonical geographic identifier drawn from the matched record
  (a county ID, a tract ID, or a county-plus-tract-plus-block-group key)
- **When:** a version or snapshot identifier showing which dated dataset
  the claim comes from — specifically `valid_time_start`, the effective date
  of the underlying fact

If no trustworthy coordinate pair can be produced, the system must refuse
rather than improvise. That refusal protects not only what the system says,
but what it commits to permanent memory.

---

## 53.2 The Problem: Retrieval Always Answers

A vector database always returns the nearest match. It does not know when
the correct answer should be "this question is out of scope." This creates
a predictable failure mode in rural civic systems:

```
query: "Cook County Illinois"     -> resolved to Taylor County, WV
query: "the surface of the moon"  -> resolved to Putnam County, WV
query: "how do I bake sourdough"  -> resolved to Cabell County, WV
```

These are not edge cases. They are the ordinary consequence of how vector
retrieval works. Without a guard, all three produce an apparently geographic
answer. A confident wrong county is more dangerous than an explicit refusal —
it gives the appearance of geographic authority without the substance of
geographic truth.

For rural developers, the first practical lesson is this: a vector database
does not know your program boundary. It knows only relative similarity inside
the corpus it was given.

---

## 53.3 Why a Simple Threshold Fails

The obvious solution — accept close matches, reject far ones — is incomplete.
When measured on the live system:

```
Mount Hope West Virginia     distance 0.5783   <- in-scope
King County Washington       distance 0.5180   <- out-of-scope
```

A genuine West Virginia place (Mount Hope, 0.5783) scores *farther* than
an out-of-state query (King County Washington, 0.5180). The overlap measured
0.0603. No single threshold can perfectly separate belonging from non-belonging.

Embedding distance captures how much a phrase *looks like a place*, not
whether it belongs to your service region. Distance measures placeness more
reliably than belonging. That is why the threshold can only be one layer of
the guard, not the whole guard.

---

## 53.4 Step 1 — The Three-Layer Geographic Guard

The production guard uses three layers working together.

### Layer 1: A Loose Distance Ceiling for Nonsense

A ceiling of 0.75 catches only the obviously absurd tail — queries that are
not really place questions:

```
what is the capital of France   distance 0.9069   rejected
how tall is Mount Everest       distance 0.9027   rejected
the surface of the moon         distance 0.8020   rejected
recipe for cornbread            distance 0.8438   rejected
```

The ceiling is intentionally loose — set above the farthest valid West
Virginia query so no legitimate local place is ever rejected. It is
evidence-based, calibrated against roughly 28 out-of-scope queries.

### Layer 2: A Lexical Scope Check on the Query

This layer reads the question text directly and is what actually separates
in-region from out-of-region place questions:

- If the question names another US state → refuse
- If the question names a major out-of-state city → refuse
- If the question says "West Virginia" or "WV" → preserve as in-scope

The critical implementation detail: the check reads the **query**, not the
retrieved record. Every record in a West Virginia-only corpus is already a
West Virginia place, so checking the record proves nothing. "Cook County
Illinois" resolves to Taylor County, WV — but the *query* names Illinois.
Only reading the user's stated scope catches this correctly.

### Layer 3: An Authoritative In-Region Place List

The guard carries 493 names baked directly into the guard code: every West
Virginia county and incorporated place, drawn from the Census TIGER/Line 2023
places file plus all 55 county names.

This list was baked in — not referenced from an external file — because it
was tested directly: after source shapefiles were deleted from the machine,
the guard still loaded all 493 names and still accepted Mount Hope. A rural
system runs on fragile hardware and temporary directories. If the guard
depends on a live external file to know that Mount Hope or Thurmond is real,
it is not robust enough for production.

---

## 53.5 Step 2 — Handling Name Collisions

Name collisions are where otherwise sensible guards fail. West Virginia has
many:

- **Charleston** — WV state capital, and also a South Carolina city
- **Raleigh** — WV county, and also a major North Carolina city
- **Wyoming** and **Ohio** — both US state names and WV county names

The guard resolves these by context:

- `"Raleigh county"` is accepted because "county" form matches the WV county
- `"Wyoming county"` is accepted as the WV county; bare "Wyoming" is read
  as the state and refused
- Any name on the authoritative WV place list is excluded from the
  out-of-state reject list

Every collision case was caught during testing, not in production. A guard
that rejects one real county or misplaces one local town will be remembered
for that mistake long after the larger architecture is forgotten.

---

## 53.6 Step 3 — Refusing Explicitly

A guard does not finish its job when it rejects a query internally. It
finishes when the user receives a clear refusal message.

The system returns a structured refusal: a flag, a machine reason, and a
human message explaining that the requested location appears to be outside
the West Virginia civic dataset or is not specific enough to ground safely.

Implementation detail: the answer layer must actually read and speak the
refusal. If it only checks whether any records came back, a refusal looks
identical to "found nothing" and the system falls silent instead of
explaining. Making the refusal visible is a deliberate wiring step.

---

## 53.7 Step 4 — The Spacetime Contract in the Database

Both halves of the spacetime contract are enforced at the database schema
level as of July 29, 2026.

### The CHECK Constraint

```sql
CONSTRAINT gbim_record_spacetime_provenance_chk CHECK (
  NOT (promotion_state = 'authorized' AND public_claim_allowed = true)
  OR (
    spatial_unit_id     IS NOT NULL
    AND spatial_unit_kind   IS NOT NULL
    AND valid_time_start    IS NOT NULL
    AND under_whose_authority IS NOT NULL
    AND company_name         IS NOT NULL
    AND ingested_at          IS NOT NULL
  )
)
```

Any row marked `authorized` and `public_claim_allowed = true` must carry all
six fields. If it cannot, it cannot be authorized. Hallucinated geography
cannot be written into permanent memory — not because a later step catches
it, but because it was never authorized to cross the boundary.

### The Ten-Condition Admissibility Predicate

For a row to appear in `public_admissible_gbim_mv` and be readable by the
public instrument, it must satisfy all ten conditions:

1. `gbim_id IS NOT NULL`
2. `promotion_state = 'authorized'`
3. `public_claim_allowed = true`
4. `under_whose_authority IS NOT NULL`
5. `company_name IS NOT NULL`
6. `ingested_at IS NOT NULL`
7. `degradation_status IN ('fresh', 'aging')`
8. `spatial_unit_id IS NOT NULL`
9. `spatial_unit_kind IS NOT NULL`
10. `valid_time_start IS NOT NULL`

Conditions 8–10 enforce the spacetime contract directly. Any row failing
any condition is stored for governance audit but invisible to the public
instrument.

### Verified Admissibility Counts (July 26, 2026)

```json
{
  "fresh": 237655,
  "aging": 0,
  "stale": 0,
  "authorized": 237655,
  "admissible_public": 93423,
  "inadmissible_public": 144232,
  "public_claim_allowed": 93423
}
```

The split — 93,423 admissible, 144,232 stored-but-inadmissible — is by
design. Many records are held internally for governance but not authorized
for public claim emission.

---

## 53.8 Step 5 — The civic_policy_fact Table and commons_current_policy()

The heading "The Half Not Yet Enforced" no longer applies. Both halves of
the spacetime contract are fully enforced in production.

### What Changed

The `civic_policy_fact` table is now live. It implements dual temporal axes
that distinguish two different kinds of time:

- **`recorded_at`** — when the fact was ingested into the system (the
  memory event timestamp)
- **`valid_time_start`** — the effective date of the policy rule itself
  (when the rule became legally operative)

This distinction matters: "this rule was recorded at this moment" is not
"this rule is effective for this program year." The system previously had
only `ingested_at`. It now has both.

### Verified Policy Output

`commons_current_policy()` is returning verified PY2026 SNAP eligibility
rules. For rural developers, this means the system can now make time-anchored
civic policy claims:

- The claim is grounded to a specific policy effective date
  (`valid_time_start`)
- The claim carries the ingestion record (`recorded_at`) separately
- Both temporal coordinates are machine-checkable against the admissibility
  predicate
- The claim cannot enter the public evidence layer without carrying both

This is the temporal half of the spacetime contract applied to the category
that most matters in rural Appalachian civic use: benefit eligibility and
program-year policy rules.

### Why This Matters for Rural Developers

A system that answers "am I eligible for SNAP?" must know which program year
it is speaking from. A benefit threshold that was valid from October 2024 to
September 2025 must not be returned as if it applies in PY2026. Without
`valid_time_start` on the fact itself — not just on the ingestion event —
that distinction cannot be enforced.

The `civic_policy_fact` table and `commons_current_policy()` close that gap.
When a community member in Fayette County asks about SNAP eligibility, the
system's answer is anchored to PY2026 rules specifically, and the temporal
anchor is part of the stored fact, not an assumption made at query time.

---

## 53.9 Step 6 — The public_answer_packet Function

The function `runtime_governance.public_answer_packet(p_geoid, p_metric_name)`
is the first component to return a structured, fully provenanced `(where,
when)` answer object at runtime. Verified output from July 26, 2026:

```json
{
  "query": {
    "geoid": "540019656003",
    "metric_name": "atm_weather_stations_count"
  },
  "generated_at": "2026-07-26T20:45:58.110893-04:00",
  "answer_blocks": [
    {
      "text": "atm_weather_stations_count for geoid 540019656003 is 1 count.",
      "label": "seen",
      "evidence": {
        "bg_table": "public.wv_bg_atm_weather_stations",
        "ingested_at": "2026-07-26T18:37:29.43012-04:00",
        "company_name": "WVGIS Technical Center",
        "source_table": "public.wv_atm_weather_stations",
        "valid_time_end": null,
        "spatial_unit_id": "540019656003",
        "valid_time_start": "2020-01-01T00:00:00-05:00",
        "spatial_unit_kind": "blockgroup",
        "degradation_status": "fresh",
        "under_whose_authority": "WVGIS Technical Center"
      },
      "evidence_ids": ["24e12e70-8c3d-4f27-8ee2-bc2011bb15a5"]
    }
  ],
  "admissibility_summary": {
    "seen_count": 1,
    "inferred_count": 0,
    "inadmissible_count": 0
  }
}
```

Every answer object contains:

- **Where:** `spatial_unit_id` (census block group GEOID), `spatial_unit_kind`
- **When:** `valid_time_start` (effective date of dataset), `ingested_at`
  (memory event timestamp)
- **Provenance:** `company_name`, `under_whose_authority`, `source_table`,
  `bg_table`, `evidence_ids` (UUID trace to specific `gbim_record` row)
- **Label:** `"seen"` — drawn from direct admissible evidence, not inferred
- **Admissibility summary:** counts of seen, inferred, and inadmissible
  blocks, enabling downstream layers to reason about answer quality

Two explicit refusal cases are handled without hallucination: `"inadmissible"`
when evidence exists but fails the admissibility gate; `"no_data"` when no
records exist at all for that combination. Every invocation is logged to
`runtime_governance.public_answer_audit`.

---

## 53.10 Step 7 — The Role Hierarchy

The separation between governance visibility and public instrument visibility
is enforced at the database role level:

- **`runtime_governance_role`** — full `SELECT / INSERT / UPDATE / DELETE`
  on `public.gbim_record`; RLS policy permits full read access. For internal
  governance and lifecycle accounting only.
- **`public_instrument_role`** — read-only, scoped to
  `public_admissible_gbim_mv` and `runtime_governance.public_answer_audit`.
  Has no direct access to `public.gbim_record`.

This boundary was verified directly: as `gbim_public_reader`, `SELECT` from
`public_admissible_gbim_mv` succeeds; direct `SELECT` from
`public.gbim_record` returns `ERROR: permission denied for table gbim_record`.
The role-level boundary is real and enforced, not just configured.

---

## 53.11 Step 8 — The pg_cron Lifecycle Scheduler

The spacetime contract requires not only that records be correctly classified
at ingestion, but that their lifecycle state is maintained over time. Four
pg_cron jobs in `wv_gis` handle this via `apply_runtime_lifecycle()`:

| Job | Schedule | Cadence |
|-----|----------|---------|
| `gbim-runtime-lifecycle-hourly` | `15 * * * *` | Refreshes `public_admissible_gbim_mv`; fast lifecycle checks |
| `gbim-runtime-lifecycle-daily` | `5 3 * * *` | Full degradation status updates; `fresh` → `aging` → `stale` |
| `gbim-runtime-lifecycle-weekly` | `0 2 * * 0` | Deeper coherence check across governed corpus |
| `gbim-runtime-lifecycle-monthly` | `30 1 1 * *` | Full lifecycle reconciliation; archives stale audit records |

These jobs ensure that a record admitted as `fresh` eventually transitions to
`stale` and falls out of `public_admissible_gbim_mv` automatically — without
manual intervention. Stale policy facts cannot linger in the public evidence
surface past their governed lifecycle window.

---

## 53.12 The Four Behavioral Proofs

Four behavioral proofs were run against the live database:

1. **Happy path** — querying `public_admissible_gbim_mv` returned real
   admissible rows with `promotion_state = 'authorized'`,
   `public_claim_allowed = true`, and `degradation_status = 'fresh'`.

2. **Candidate trap** — one authorized row was flipped to
   `promotion_state = 'candidate'` and `public_claim_allowed = false`. After
   refresh, `public_mv_rows = 0`. Candidate material cannot leak into the
   public evidence path.

3. **Lifecycle decay** — one admissible row's `ingested_at` was pushed back
   18 months. After running `refresh_gbim_degradation_status()` and refreshing
   the view, the row became `degradation_status = 'stale'` and
   `still_public = false`. Degraded records are automatically removed from
   public speakability.

4. **Public reader isolation** — as `gbim_public_reader`, `SELECT` from
   `public_admissible_gbim_mv` succeeds; direct `SELECT` from
   `public.gbim_record` returns permission denied. The role boundary is real.

All four proofs used `ROLLBACK` to leave production state clean.

---

## 53.13 What This Guard Does Not Do

An honest chapter names the boundary of its claims:

- The out-of-state city list is finite (~90 cities after collision removal).
  A bare out-of-state town name with no state attached can slip through.
- The distance ceiling was calibrated on a modest evaluation set. It is
  evidence-based, not mathematically universal.
- Vague references, paraphrases, and misspellings can evade lexical checks.

These limitations do not invalidate the method. They define the next
increment of work. A useful guard is allowed to be incomplete, provided its
incompleteness is named and testable.

---

## 53.14 Scope Boundary: Civic Geography vs. Private Memory

This chapter governs one path: answers about public civic geography. It does
**not** govern the system's private per-user memory, which follows the
opposite rule.

Civic geography is meant to range across counties and tracts inside the
public regional corpus. Private memory must never range across people.
Confusing the two pipelines would turn a public geography rule into a privacy
violation. Chapter 50 governs private per-user memory separately and by
different rules. Do not conflate them.

---

## 53.15 Step-by-Step Summary for Rural Developers

1. **Define the geographic scope plainly.** Decide exactly what region the
   system serves. Write it down. Make it explicit.

2. **Build a canonical civic geography corpus.** Store counties, tracts,
   block groups, and towns with canonical identifiers. This is the retrieval
   layer's answer space.

3. **Measure retrieval before adding a guard.** Run known in-scope and
   out-of-scope queries and record the distances. Find the overlap. The
   overlap proves a threshold alone is not enough.

4. **Set a loose nonsense ceiling.** High enough to preserve all valid
   in-region queries; low enough to reject clearly non-geographic queries.
   This is the nonsense filter, not the geography filter.

5. **Add lexical scope checks.** Reject queries that name other states or
   out-of-scope cities. Read the query, not the retrieved record.

6. **Bake an authoritative local place list into the guard.** Test that it
   works with the source file removed.

7. **Test collisions deliberately.** Shared names, ambiguous names,
   county-versus-city forms, small local places. None of these work
   automatically.

8. **Refuse explicitly.** Return a visible refusal message. Wire the answer
   layer to actually speak it.

9. **Enforce the spacetime contract at the write boundary.** Use a CHECK
   constraint that blocks any authorized public claim missing a
   `spatial_unit_id`, `spatial_unit_kind`, or `valid_time_start`.

10. **Use dual temporal axes for civic policy facts.** Separate
    `recorded_at` (ingestion timestamp) from `valid_time_start` (policy
    effective date). These are not the same thing. A PY2026 SNAP rule
    must carry the program year effective date, not just when it was
    ingested.

11. **Build a role hierarchy.** Governance role sees everything. Public
    instrument role reads only the admissible view. Test the boundary.

12. **Wire a lifecycle scheduler.** Use pg_cron or equivalent so lifecycle
    state is maintained automatically. Stale records must fall out of the
    public evidence surface without manual intervention.

13. **Every public answer should carry its evidence.** Label, source table,
    authority, temporal anchor, and a UUID trace. Downstream layers must
    be able to reason about answer quality programmatically.

14. **Keep the guard scoped.** Apply it only to the civic geography retrieval
    path. Do not reuse it for private user memory.

---

## 53.16 Closing Statement

A rural civic AI does not become trustworthy by sounding confident. It
becomes trustworthy by refusing to cross the boundary of what it can ground.

The spacetime contract enforces that discipline at every level: in the
geographic guard that refuses out-of-scope queries, in the CHECK constraint
that blocks hallucinated geography from entering permanent memory, in the
ten-condition admissibility predicate that keeps the public evidence surface
clean, in the `civic_policy_fact` table that anchors policy claims to their
actual effective dates, and in `commons_current_policy()` returning verified
PY2026 SNAP eligibility rules.

Both halves of the contract — **where** and **when** — are fully enforced
in production as of July 29, 2026.

For community members in Mount Hope and across Fayette County: when Ms.
Jarvis makes a civic claim, she can tell you where the fact comes from,
which geographic unit it applies to, and which program year's rules it
reflects. If she cannot produce those coordinates, she refuses rather than
guesses. That is what the spacetime contract means in practice.

---

*Chapter 53 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
*Sealed: July 29, 2026 — July 2026 Production Gate.*
*Status: As-Built — Both Halves Fully Enforced.*
*`civic_policy_fact` table: live with dual temporal axes (`recorded_at`,
`valid_time_start`).*
*`commons_current_policy()`: returning verified PY2026 SNAP eligibility rules.*
