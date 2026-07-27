# Chapter 53 — The Spacetime Contract

**Author:** C. A. Kidd
**Last Updated:** July 26, 2026
**Status:** As-built — both halves of the spacetime contract are enforced in production

---

## How a rural civic AI is prevented from inventing geography

---

### 1. What this chapter is for

If you are building an AI system that answers questions about real places — counties, towns, census tracts, service areas, or neighborhoods — you will run into a problem that is easy to miss until it fails in front of the people you serve. This chapter explains that problem, describes a tested solution now running in production, and shows how to reproduce the same guard in a small rural civic setting.

It is written step by step for rural developers, especially those working in small nonprofits, local government, health access networks, mutual aid systems, or community technology projects. The system described here was built under tight resource constraints, calibrated on a live laptop deployment, and tested against real place queries. No research lab is required. What is required is a discipline of measurement, a refusal to guess, and a willingness to define the boundary of the system honestly.

The scope of this chapter is deliberately narrow. It covers one question: how the system decides whether it knows *where* a user's question is about, what it does when it does not know, and how that same decision protects the system's permanent memory, not only its spoken answers. It does not cover answer phrasing, document ingestion, model selection, or private conversation history. Those belong to other chapters. This narrow scope is not a limitation of the method; it is part of the method. A guard that tries to solve every problem at once is too broad to test and too vague to trust.

---

### 2. Why this is called a spacetime contract

The title is intentionally metaphorical, but the metaphor is disciplined rather than decorative. In physics, spacetime provides the coordinate structure within which events can be located. A statement about an event is meaningful only if it can be placed somewhere and somewhen. In the same engineered sense, this civic AI is not allowed to make a grounded geographic claim unless it can place that claim within an explicit coordinate system of civic data.

That is why the chapter uses the phrase **spacetime contract**. The contract is not a claim about physics or relativity. It is a rule for system behavior. Every grounded civic claim must be attachable to a specific **where** and a specific **when**. If no trustworthy coordinate can be produced, the system must refuse rather than improvise.

One note on language, because this chapter later borrows more physics vocabulary. When it speaks of an "authorized coordinate set" or a "basis" of allowed places, those are architecture terms for authorization scope, not literal claims of formal vector-space structure. The enforceable content of this chapter is a lexical scope check and a calibrated distance ceiling, both measured below. The physics analogy is a way to think clearly, not a proof.

---

### 3. The system context: what is being guarded

Before describing the guard, it is important to name the exact path it governs.

The system holds West Virginia civic geography in a retrieval layer. Place records such as counties, tracts, and block groups are embedded into vectors and stored in a vector database. When a user asks a question involving a place, the system embeds the query and retrieves the nearest geographic records from that index.

That retrieval step is useful, but it is not self-validating. It tells the system which stored record is *closest* to the query, not whether the query is actually about a place the system should answer for. The guard exists to decide whether retrieval has found a place the system is entitled to treat as real, in-scope, and trustworthy.

In this chapter, the guarded path is the **public civic geography path** only — the path used to resolve counties, towns, census tracts, and related regional geography. It does **not** apply to private user memory, conversation history, or person-specific data. Those paths require different rules and must not be conflated with broad civic retrieval.

---

### 4. The problem: retrieval always answers, even when it should refuse

A vector database always returns the nearest match from what it has. That is its job. It does not know when the correct answer should be "this question is out of scope" or "this is not a place at all."

This creates a predictable failure mode. If the system is asked about a place it does not cover, or about something that is not a place, the database still returns the nearest stored West Virginia record. The result contains a distance value, but by itself that value does not say "this is invalid." It only says "this is the least wrong thing I found."

In a rural civic system, this matters because the answer may look specific even when it is wrong. A confident wrong county is more dangerous than an explicit refusal. It gives the appearance of geographic authority without the substance of geographic truth.

The goal is not to make retrieval more eloquent. The goal is to stop the system from turning nearest-neighbor behavior into false geographic certainty.

---

### 5. The measured failure: nearest does not mean correct

This failure is easiest to understand through direct examples. In the live system, queries clearly outside the intended West Virginia civic scope still resolved to specific West Virginia counties because the vector database returned the nearest available match.

```
query: "Cook County Illinois"        -> resolved to Taylor County, WV
query: "the surface of the moon"     -> resolved to Putnam County, WV
query: "how do I bake sourdough"     -> resolved to Cabell County, WV
```

These are not abstract edge cases. They are the ordinary consequence of how vector retrieval works. Cook County is real, but outside the system's regional scope. The moon is not in West Virginia. A sourdough recipe is not a place. Yet without a guard, all three still produce an apparently geographic answer.

For rural developers, this is the first practical lesson: a vector database does not know your program boundary. It knows only relative similarity inside the corpus it was given. If you do not add a separate scope guard, retrieval alone will confidently map the world into your region.

---

### 6. The contract: no grounded claim without a where and a when

The system therefore needs a rule stronger than "take the nearest hit." It can be stated in one sentence:

**The system may not state a geographic fact unless it can attach that fact to a trustworthy `(where, when)` tuple that it actually retrieved.**

The two parts of that tuple are:

- **Where**: a canonical geographic identifier drawn from the matched record — a county ID, a tract ID, or a county-plus-tract-plus-block-group key.
- **When**: a version or snapshot identifier showing which dated dataset the claim comes from.

As of July 26, 2026, both halves of this contract are enforced in production. The **where** half has been live since the initial implementation described below. The **when** half was completed on July 26, 2026 through the full spacetime/provenance schema migration and the `public_answer_packet` function described in sections 14 through 16.

The central difficulty is that retrieval always produces *some* candidate where. The guard's job is to determine whether that where is trustworthy enough to authorize a claim.

---

### 7. Why a simple threshold does not solve the problem

The obvious solution is a distance threshold: accept close matches, reject far ones. It is simple, measurable, and incomplete.

To test whether a clean threshold existed, the system was evaluated on two groups of queries — real West Virginia places that should be accepted, and places elsewhere or non-places that should be refused.

In-scope results:

```
Kanawha county West Virginia    distance 0.2517
McDowell county                 distance 0.2769
Fayette county West Virginia    distance 0.2971
Raleigh county                  distance 0.3302
Monongalia county Morgantown    distance 0.3710
census tract 54019020101        distance 0.5067
Mount Hope West Virginia        distance 0.5783
```

Out-of-scope results:

```
King County Washington          distance 0.5180
Cook County Illinois            distance 0.5960
Harris County Texas             distance 0.6102
Los Angeles California          distance 0.6298
Toronto Ontario Canada          distance 0.7982
the surface of the moon         distance 0.8216
how do I bake sourdough bread   distance 0.8638
```

The overlap is the critical finding. A genuine West Virginia place such as Mount Hope (0.5783) can score *farther* than an out-of-state query such as King County Washington (0.5180). The overlap measured 0.0603. No single threshold can perfectly separate "belongs in West Virginia" from "does not belong."

For rural developers, this is the second practical lesson: embedding distance captures how much a phrase *looks like a place*, not whether it belongs to your service region. Texts shaped like county names remain close to other county names even when they refer to the wrong state. Distance measures placeness more reliably than belonging. That is why the threshold can only be one layer of the guard, not the whole guard.

---

### 8. The design principle: separate kinds of error

Once the threshold is shown to be insufficient alone, the design principle becomes clear. Different error types need different checks. There are at least three distinct failure modes:

1. The query is not about a place at all.
2. The query is about a real place, but outside the region.
3. The query names a place that collides with a place elsewhere.

A single distance threshold cannot reliably solve all three. The guard therefore uses multiple signals, each doing one job and no more.

This is a useful habit for small teams. Instead of searching for one perfect score, ask which kinds of mistake the system makes, then assign a specific check to each. The result is easier to test and easier to explain.

---

### 9. The guard: three signals working together

The production guard uses three layers.

#### 9.1 A loose distance ceiling for nonsense

The first layer is a high distance ceiling. In this system it is 0.75. Anything beyond it is treated as too far away to authorize a geographic claim. This layer does **not** try to distinguish West Virginia from other states. It catches only the obviously absurd tail — questions that are not really place questions.

```
what is the capital of France   distance 0.9069   rejected
how tall is Mount Everest       distance 0.9027   rejected
the surface of the moon         distance 0.8020   rejected
recipe for cornbread            distance 0.8438   rejected
```

The ceiling is intentionally loose. It sits above the farthest measured valid West Virginia query, so it never rejects a legitimate in-region place. Its purpose is modest and important: remove pure nonsense before it can be canonicalized into a fake county. The value 0.75 is evidence-based, calibrated against roughly twenty-eight out-of-scope queries; nothing legitimate approached it.

#### 9.2 A lexical scope check on the question itself

The second layer reads the question text directly. This is the layer that actually separates in-region from out-of-region place questions.

The rule is simple:

- If the question names another US state, refuse it.
- If the question names a major out-of-state city, refuse it.
- If the question explicitly says "West Virginia" or "WV," preserve it as in-scope unless a stronger contradiction appears.

There is a subtlety worth stating precisely, because it is easy to describe wrongly. The check reads the **query**, not the retrieved record. Every record in a West Virginia-only corpus is already a West Virginia place, so checking the record proves nothing — "Cook County Illinois" resolves to Taylor County, WV, which *is* in the region. What catches it is that the *query* names Illinois. The scope check refuses when the question declares a coordinate outside the region, regardless of what the nearest record happens to be. Distance cannot do this; only reading the user's stated scope can.

#### 9.3 An authoritative in-region place list

The third layer protects small towns and name collisions by carrying an authoritative list of the region's own places.

In the West Virginia deployment, that list holds 493 names — every county and every incorporated place, drawn from the Census TIGER/Line 2023 places file plus the 55 county names. The list was baked directly into the guard code so that it survives deletion of the source shapefile or other staging artifacts. This was tested directly: after the source shapefiles were deleted from the machine, the guard still loaded all 493 names and still accepted Mount Hope.

That matters operationally. A rural system often runs on fragile hardware, temporary directories, hand-built pipelines, and imperfect storage. If the guard depends on a live external file to know that Mount Hope or Thurmond is a real West Virginia place, it is not robust enough for production. Baking the place universe into the guard turns a data dependency into a tested invariant.

---

### 10. Handling collisions: where rural systems get embarrassed

Name collisions are where many otherwise sensible guards fail. A system that merely blocks out-of-state names will still make mistakes if it does not account for names shared across the country. West Virginia has many:

- **Charleston** — a West Virginia city, and the state capital, but also a city in South Carolina.
- **Raleigh** — a West Virginia county, but also a major city in North Carolina.
- **Wyoming** and **Ohio** — names of both US states and West Virginia counties.

The solution is not to guess from the name alone. The solution is context.

- "Raleigh county" is accepted, because the county form matches the West Virginia county — even though "Raleigh" alone appears on out-of-state city lists.
- "Wyoming county" is accepted as the West Virginia county; bare "Wyoming" is read as the state and refused. The disambiguating rule is simple and reliable: no US state has the word "county" in its name, so "`<name>` county" for a shared name means the West Virginia county.
- Any name on the authoritative West Virginia place list is protected from naive rejection. Charleston, Huntington, and every small town are excluded from the out-of-state reject list because they appear on the region's own place list.

Every one of these collisions was caught during testing, not in production. The combined guard was validated against every calibration query plus the collision cases and both directions of the shared-name ambiguity, and answered all of them correctly.

For rural developers, this is the third practical lesson: local credibility is often lost on small, obvious errors. A guard that rejects one real county or misplaces one local town will be remembered for that mistake long after the larger architecture is forgotten.

---

### 11. The operational rule: refuse out loud

A guard does not finish its job when it rejects a query internally. It finishes its job when the user receives a clear refusal message.

In this system, a rejected query yields a plain explanation: the requested location appears to be outside the West Virginia civic dataset, or the query is not specific enough to ground safely, so the system declines rather than guess.

This matters for user trust. Silent failure feels arbitrary. Wrong confidence feels deceptive. Explicit refusal teaches the user the system's boundary and shows that the boundary is intentional rather than broken. For civic use this is not cosmetic; it is part of accountability.

There is an implementation detail behind that plainness. The retrieval service returns a structured refusal — a flag saying the query was refused, a machine reason, and a human message. The layer that assembles the AI's answer must actually read that refusal and speak it. If the answer layer only checks whether any records came back, a refusal looks identical to "found nothing," and the system falls silent instead of explaining. Making the refusal visible to the person is a deliberate wiring step, not an automatic consequence of the guard.

---

### 12. Step-by-step implementation path for a rural developer

A developer reproducing this method in another region can follow the same order.

**Step 1: Define the geographic scope plainly.**
Decide exactly what region the system serves. A state, a county network, a set of tribal lands, a metro area, or a service catchment are all valid. What matters is that the scope is explicit.

**Step 2: Build a canonical civic geography corpus.**
Store the region's counties, tracts, block groups, towns, or other units in a structured corpus with canonical identifiers. This becomes the retrieval layer's answer space.

**Step 3: Measure retrieval before adding a guard.**
Run known in-scope and known out-of-scope queries and record the top-hit distances. Do not guess where the threshold belongs. Measure it.

**Step 4: Find the overlap.**
Look for whether real in-scope places and out-of-scope places overlap in distance. In most cases they will. That overlap is the proof that distance alone is not enough.

**Step 5: Set a loose nonsense ceiling.**
Choose a ceiling high enough to preserve all valid in-region queries but low enough to reject clearly non-geographic queries. This is your nonsense filter, not your geography filter.

**Step 6: Add lexical scope checks.**
Reject queries that explicitly name other states, other countries, or out-of-scope major cities. Respect the user's language about place. Remember to read the query, not the retrieved record.

**Step 7: Bake an authoritative local place list into the guard.**
Carry your region's own towns and counties inside the guard logic so real local places are protected and the guard survives missing source files. Test that it still works with the source file removed.

**Step 8: Test collisions deliberately.**
Create tests for shared names, ambiguous names, county-versus-city forms, and small local places. Do not assume these will work automatically.

**Step 9: Refuse explicitly.**
Return a visible refusal message when the system cannot ground the place safely, and make sure the answer layer reads and speaks that refusal.

**Step 10: Keep the guard scoped.**
Apply this guard only to the civic geography retrieval path. Do not reuse it for private user memory or other pipelines with different governance rules.

---

### 13. Proof of behavior in production

After the layers were combined and wired into the live retrieval service, the system behaved correctly on the tested cases. These are results from the running production service:

```
Kanawha county West Virginia   -> answered normally
Cook County Illinois           -> refused: names another state
the surface of the moon        -> refused: beyond the distance ceiling
Mount Hope West Virginia       -> answered normally
```

The significance is not just that examples worked. It is that the layered guard succeeded exactly where the simple threshold failed. The overlapping case — Mount Hope — remained answerable, while clearly out-of-scope queries were refused for explicit, distinct reasons: one caught by the lexical scope check, one by the distance ceiling. That is the practical success criterion for the chapter: preserve real local places, reject outside geography, reject non-places, and explain the refusal.

---

### 14. The deeper role: refusal as a defense of permanent memory

The chapter to this point has treated the guard as protecting the system's *answers*. There is a second, deeper role that connects this contract to how the system stores what it believes over time.

The system does not commit every thought to permanent memory immediately. A candidate finding first enters a staging area. It becomes committed memory only after passing a promotion gate — an evaluation step that checks the candidate against several conditions and promotes it only if all of them pass. A candidate that fails is not committed; it remains a staged record, visible for audit, but never crossing into the system's durable state.

**As of July 26, 2026, this gate is implemented at the database level.** The `gbim_record_spacetime_provenance_chk` CHECK constraint on `public.gbim_record` enforces that any row marked `promotion_state = 'authorized'` and `public_claim_allowed = true` must carry a non-null `spatial_unit_id`, `spatial_unit_kind`, `valid_time_start`, `under_whose_authority`, `company_name`, and `ingested_at`. The `public_admissible_gbim_mv` materialized view is the only surface readable by the `public_instrument_role`; it additionally requires `degradation_status IN ('fresh', 'aging')`. Any row that fails these conditions is stored but inadmissible — it cannot cross into the public evidence layer at all.

This is where the spacetime contract does more than shape an answer. A geographic claim the guard would refuse also fails the promotion gate. Hallucinated geography cannot be written into permanent memory — not because a later step catches it, but because it was never authorized to cross the boundary. The refusal is a defense of the system's memory, not only its speech.

For rural developers, the lesson generalizes beyond geography. The strongest place to enforce a scope rule is not at the moment of speaking, but at the moment of committing to memory. An answer can be regenerated; a corrupted belief persists and compounds. If your system has any notion of durable state — a knowledge base, a belief store, a learned profile — the scope guard belongs at the write boundary as much as at the read boundary.

---

### 15. Runtime governance layer: as-built implementation

The following describes the production runtime governance layer installed in `wv_gis` on the Ms. Allis deployment machine on July 26, 2026. These are verified outputs from live `psql` sessions, not hypothetical specifications.

#### 15.1 Schema and role structure

- `runtime_governance` schema holds all governance functions and audit tables.
- `public_answer_audit` table logs every invocation of the answer function with stage, detail JSON, and timestamp.
- `runtime_governance_role` is a login role with full `SELECT / INSERT / UPDATE / DELETE` on `public.gbim_record` and an RLS policy permitting full read access. This role is for internal governance and lifecycle accounting only.
- `public_instrument_role` is a read-only role scoped to `public_admissible_gbim_mv` and `runtime_governance.public_answer_audit`. It has no direct access to `public.gbim_record`. This role backs the public-facing instrument.

The separation of these roles is the architectural boundary between "internal governance can see everything" and "public instrument may only speak from admissible evidence."

#### 15.2 Spacetime/provenance schema migration

On July 26, 2026, `public.gbim_record` was extended with the following columns, backfilled, and locked down:

```sql
-- Added columns
spatial_unit_id     text        NOT NULL  -- equals geoid for blockgroup records
spatial_unit_kind   text        NOT NULL  -- 'blockgroup' for all current records
valid_time_start    timestamptz NOT NULL  -- 2020-01-01 for static inventories
valid_time_end      timestamptz          -- NULL for open-ended validity

-- CHECK constraint (enforces full spacetime contract on public claims)
CONSTRAINT gbim_record_spacetime_provenance_chk CHECK (
  NOT (promotion_state = 'authorized' AND public_claim_allowed = true)
  OR (
    spatial_unit_id IS NOT NULL
    AND spatial_unit_kind IS NOT NULL
    AND valid_time_start IS NOT NULL
    AND under_whose_authority IS NOT NULL
    AND company_name IS NOT NULL
    AND ingested_at IS NOT NULL
  )
)
```

All 237,655 rows passed the backfill. The NOT NULL alterations succeeded, which confirms every row was covered before the constraint was locked. The current admissible row count is 93,423 — the subset of total rows that carry authorized status, a public claim flag, fresh/aging lifecycle, and all required spacetime and provenance fields.

#### 15.3 Verified admissibility lifecycle output

The lifecycle audit function `runtime_governance.log_lifecycle_counts()` records a snapshot to `public_answer_audit` on every call. The verified snapshot from July 26, 2026 reads:

```json
{
  "aging": 0,
  "fresh": 237655,
  "stale": 0,
  "logged_at": "2026-07-26T19:44:06.530415-04:00",
  "authorized": 237655,
  "admissible_public": 93423,
  "inadmissible_public": 144232,
  "public_claim_allowed": 93423
}
```

The split — 93,423 admissible, 144,232 stored-but-inadmissible — reflects the intended design: many records are held internally for governance purposes but not authorized for public claim emission.

#### 15.4 Lifecycle demos verified

Four behavioral proofs were run against the live database:

1. **Happy path** — querying `public_admissible_gbim_mv` returned real admissible rows with `promotion_state = 'authorized'`, `public_claim_allowed = true`, and `degradation_status = 'fresh'`.

2. **Candidate trap** — one authorized and public row was flipped to `promotion_state = 'candidate'` and `public_claim_allowed = false`. After refresh, the raw table showed `raw_candidate_rows = 1` and the materialized view showed `public_mv_rows = 0`. Candidate material cannot leak into the public evidence path.

3. **Lifecycle decay** — one admissible row's `ingested_at` was pushed back 18 months. After running `refresh_gbim_degradation_status()` and refreshing the materialized view, the row became `degradation_status = 'stale'` and `still_public = false`. Degraded records are automatically removed from public speakability.

4. **Public reader isolation** — as `gbim_public_reader`, `SELECT` from `public_admissible_gbim_mv` succeeds; direct `SELECT` from `public.gbim_record` returns `ERROR: permission denied for table gbim_record`. The role-level boundary is real and enforced.

All four demos used `ROLLBACK` to leave production state clean.

---

### 16. The public_answer_packet function: proof of the full spacetime contract

The function `runtime_governance.public_answer_packet(p_geoid text, p_metric_name text)` is a `SECURITY DEFINER` PL/pgSQL function with `search_path` pinned to `public, runtime_governance, pg_temp`. It is the first component in this system to return a structured, fully provenanced `(where, when)` answer object at runtime, satisfying both halves of the spacetime contract simultaneously.

The following is the verified output from a live invocation on July 26, 2026, as `public_instrument_role`:

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
            "evidence_ids": [
                "24e12e70-8c3d-4f27-8ee2-bc2011bb15a5"
            ]
        }
    ],
    "admissibility_summary": {
        "seen_count": 1,
        "inferred_count": 0,
        "inadmissible_count": 0
    }
}
```

This answer object contains:

- **Where**: `spatial_unit_id = "540019656003"` (census block group GEOID), `spatial_unit_kind = "blockgroup"`.
- **When**: `valid_time_start = "2020-01-01T00:00:00-05:00"`, the effective date of the underlying Census/ATM dataset; `ingested_at` records when the record entered the system.
- **Provenance**: `company_name` and `under_whose_authority` both identify WVGIS Technical Center; `source_table` and `bg_table` name the exact database objects; `evidence_ids` provides a UUID trace back to the specific `gbim_record` row.
- **Label**: `"seen"` — the answer is drawn from direct admissible evidence, not inferred.
- **Admissibility summary**: counts of seen, inferred, and inadmissible evidence blocks, enabling any downstream layer to reason about answer quality programmatically.

The function handles two refusal cases without hallucinating a value: when admissible evidence exists for the geoid and metric combination but zero rows pass the admissibility gate, it returns an `"inadmissible"` block; when no records exist at all for that combination, it returns a distinct `"no_data"` block. The distinction between "stored but inadmissible" and "never stored" is part of the contract.

Every invocation is logged to `runtime_governance.public_answer_audit`, creating a durable audit trail of every public claim the system was asked to support.

---

### 17. The runtime scheduler: pg_cron lifecycle jobs

The spacetime contract requires not only that records be correctly classified at the moment of ingestion, but that their lifecycle state be maintained over time. A record that was `fresh` at ingestion should become `aging` and eventually `stale` as the underlying dataset ages. Stale records must automatically fall out of the admissible set without requiring manual intervention.

This is accomplished through four `pg_cron` jobs registered in `wv_gis` on July 26, 2026:

```
jobid | schedule    | jobname                          | function
------+-------------+----------------------------------+--------------------------------------------
1     | 5 3 * * *   | gbim-runtime-lifecycle-daily     | runtime_governance.gbim_runtime_lifecycle_daily()
3     | 15 * * * *  | gbim-runtime-lifecycle-hourly    | runtime_governance.gbim_runtime_lifecycle_hourly()
4     | 0 2 * * 0   | gbim-runtime-lifecycle-weekly    | runtime_governance.gbim_runtime_lifecycle_weekly()
5     | 30 1 $ * *  | gbim-runtime-lifecycle-monthly   | runtime_governance.gbim_runtime_lifecycle_monthly()
```

All four jobs are `active = true`. The hourly job handles degradation status refreshes and fast-path anomaly detection. The daily job runs the full lifecycle snapshot and audit log. The weekly job handles slower structural checks. The monthly job — scheduled for the last day of each month — handles heavier revalidation.

`cron.job_run_details` was empty at the time of installation, as expected; no jobs had fired yet. Once executions begin, the run history will provide a machine-readable audit trail of the system's lifecycle health over time.

This scheduler is the implementation of what Chapter 52 describes as the Recurrent Epistemic Loop: a scheduled, automated process that continuously checks the system's own evidence against its admissibility criteria and adjusts lifecycle state accordingly.

---

### 18. The full predicate for public admissibility: as-built

The enforced public admissibility rule as of July 26, 2026 is as follows. Any row in `public.gbim_record` must satisfy **all** of the following conditions to appear in `public_admissible_gbim_mv` and be accessible to the public instrument:

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

Condition 1 ensures record identity. Conditions 2 and 3 enforce the governance gate. Conditions 4 through 6 enforce provenance. Condition 7 enforces lifecycle freshness. Conditions 8 through 10 enforce the spacetime contract — the where (spatial unit identity and kind) and the when (temporal anchor).

Any row failing one or more conditions is stored in `gbim_record` — visible to the governance role for audit and repair — but invisible to the public instrument. The `public_answer_packet` function labels such cases explicitly as `"inadmissible"` rather than returning a value or remaining silent.

---

### 19. What this guard does not do

An honest chapter should name the boundary of its claims. This guard does **not** solve every geographic grounding problem. At least three gaps remain.

First, the out-of-state city list is finite. It catches the cities most likely to appear — roughly ninety after collision removal — but not every small municipality elsewhere. A bare out-of-state town name with no state attached, and no absurd distance, can still slip through.

Second, the distance ceiling was set from a modest evaluation set. It is evidence-based, but not mathematically universal.

Third, vague references, paraphrases, and misspellings can evade lexical checks and fall through to the ceiling logic only.

On the temporal side, `valid_time_start` for static inventories is currently anchored to `2020-01-01` — the canonical Census snapshot date — rather than to a per-dataset observed date. This is correct for the ATM weather station data and similar static inventories. For time-sensitive policy and benefit facts, the temporal anchor must come from the underlying effective date of the fact itself, not from the ingestion event. Those facts are not yet in the corpus. The anchor `2020-01-01` is honest for what is currently stored; it would not be honest for benefit eligibility rules, program year thresholds, or similarly time-varying civic data.

These limitations do not invalidate the method. They define the next increment of work. A useful guard is allowed to be incomplete, provided its incompleteness is named and testable.

---

### 20. The boundary of this chapter

This chapter governs one path: answers about public civic geography. It does **not** govern the system's private per-person memory, which follows the opposite rule. Civic geography is meant to range across counties and tracts inside the public regional corpus. Private memory must never range across people. Confusing the two would turn a public geography rule into a privacy violation.

That boundary is part of the academic scope of this chapter. The chapter is about geographic grounding and — in sections 15 through 18 — the point at which geographic grounding meets the memory-commit boundary and the runtime governance layer. It is not about memory sovereignty, user identity, or cross-user data isolation, which are governed elsewhere and by different rules.

---

### 21. The half not yet enforced: time-sensitive civic facts

The spacetime contract requires both a **where** and a **when**. For the current corpus — ATM weather stations, geographic inventories, and Census-derived block group attributes — the **when** is fully enforceable because the facts are static: they reflect a specific dated snapshot, and that date is now carried as `valid_time_start` in every admissible row.

What is not yet in the corpus is a different category of civic fact: **policy facts, eligibility rules, benefit thresholds, program year conditions.** An audit of the current databases found that those tables do not exist — not that they lack a date column, but that the facts have not yet been re-added. This is a more useful finding than a missing column, because it locates the decision at the right moment: re-ingestion.

When those facts return, they must land in structured, dated tables carrying a `valid_time_start` and `valid_time_end` that reflect the effective period of the rule, not the ingestion timestamp. A benefit threshold that was valid from October 2024 to September 2025 must carry those dates explicitly. If benefit facts return as unstructured document text, the temporal half of the contract will remain unenforceable for that category, because a paragraph pulled from an undated manual has no `when` to check against.

The memory system already timestamps when a belief was committed (`ingested_at`). That is a real temporal coordinate, but it is the time of the memory event, not the time the underlying fact is effective. "This rule was recorded at this moment" is not "this rule is effective for this program year." The system has the first; civic truth needs the second.

This chapter therefore carries forward one design instruction: time-sensitive civic facts must be stored in dated, structured form from the moment they are re-added, or their **when** anchor cannot be checked by the spacetime contract. The contract, written before the data returns, is what makes that instruction actionable rather than a regret.

---

### 22. What rural developers should take away

A rural civic AI does not become trustworthy by sounding confident. It becomes trustworthy by refusing to cross the boundary of what it can ground.

The practical lessons of this chapter:

1. Retrieval will always return something. That is not the same as knowing.
2. Distance alone does not tell you whether a place belongs to your region.
3. A layered guard is more honest than a magical threshold.
4. Read the query, not just the retrieved record, when checking scope.
5. Your region needs an authoritative place list, and the guard should survive losing the source file.
6. Name collisions must be handled deliberately.
7. Refusals should be visible and plain, and the answer layer must actually speak them.
8. The strongest place to enforce a scope rule is the memory-commit boundary, not only the answer.
9. Geographic grounding and private memory are different pipelines and need different rules.
10. If the system will ever make time-sensitive civic claims, the data must be stored with explicit temporal keys from the moment it is re-added.
11. Build a role hierarchy that separates governance visibility from public instrument visibility. The governance role needs full table access; the public role needs only the admissible view.
12. Wire a scheduler to your lifecycle functions so lifecycle state is maintained automatically over time, not only at ingestion.
13. Every public answer should carry its evidence explicitly — label, source table, authority, temporal anchor, and a UUID trace — so downstream layers can reason about answer quality programmatically.

The deepest point is simple: when the system does not know where or when a question is about, it must say so — and it must not quietly remember a guess as if it were true. Everything else in this chapter is machinery built to make that sentence true, measurable, and defensible.
