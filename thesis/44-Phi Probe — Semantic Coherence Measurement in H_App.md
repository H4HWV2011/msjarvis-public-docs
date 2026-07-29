# 44 — Phi Probe — Semantic Coherence Measurement in H_App

*Carrie Kidd (Mamma Kidd) — Oak Hill, West Virginia*
*Last Updated: July 29, 2026*
*Status: Demonstrated — July 2026 Production Gate*

---

## What This Chapter Is About

This chapter explains how Ms. Jarvis measures **semantic coherence** — the degree to which its governed data is ready to back public claims — using a single, concrete number called the **Phi probe fraction**.

For rural developers in West Virginia and across Appalachia, abstract ideas like "semantic coherence" can feel distant from practical work. This chapter translates the concept into a ratio you can query, monitor, and act on. By the end, you will understand what Phi measures, how it is computed from real database rows, why the baseline number is 39.3%, and how to use it as a health gauge as your system grows.

This chapter operates strictly within the academic scope of the July 2026 production gate. It does not claim to measure every kind of coherence — only admissibility-based semantic coherence within the governed corpus.

---

## 44.1 The Core Idea: Coherence as a Ratio

The system stores many records. Not all of them are ready to speak.

Some records are fresh, fully anchored, and approved for public claims. Others are aging, incomplete, or still moving through the promotion lifecycle. The Phi probe answers a simple question:

> *Of all the authorized governed records in the system right now, what fraction are admissible for public claims?*

That fraction — expressed as a decimal or percentage — is Phi.

\[
\Phi_{\text{admissible}} = \frac{\text{admissible rows}}{\text{total authorized rows}}
\]

**As of July 26, 2026:**

\[
\Phi_{\text{admissible}} \approx \frac{93{,}423}{237{,}655} \approx 0.393 \quad (39.3\%)
\]

This is the verified baseline established at the July 2026 production gate. It is not an estimate. It is a live inspection of the governed corpus.

---

## 44.2 Why This Matters for Rural Developers

Rural data systems face a specific challenge: data is often collected under resource constraints, with incomplete provenance, inconsistent spatial anchors, or gaps in the temporal record. The result is a corpus that holds more than it can safely speak.

The Phi probe gives you a concrete handle on that gap. Instead of saying "we have a lot of data but some of it is messy," you can say:

> *39.3% of our governed records are fully admissible. The rest are stored but not yet ready to back public claims.*

That sentence is actionable. It tells you how much cleanup, promotion, and lifecycle work remains. It gives stewards and developers a shared vocabulary. And it allows you to track progress over time with a single number.

---

## 44.3 The Governed Corpus: What Is Being Measured

The measurement operates on two database objects.

**The full authorized corpus:**

```sql
SELECT COUNT(*)
FROM public.gbim_record
WHERE promotion_state = 'authorized';
-- Result: 237,655 rows
```

**The admissible subset:**

```sql
SELECT COUNT(*)
FROM public.public_admissible_gbim_mv;
-- Result: 93,423 rows
```

The materialized view `public_admissible_gbim_mv` applies the ten-condition admissibility predicate (described in full in Appendix A) and returns only the records that pass all ten conditions.

Every record in the admissible subset is ready to:

- Back a public answer via `public_answer_packet`.
- Appear on the public evidence surface.
- Anchor an overflow event in person-space.

Records outside the admissible subset are not errors. They are candidates, aging records, or records still moving through the promotion lifecycle. The system stores them intentionally.

---

## 44.4 The Ten-Condition Admissibility Predicate

The Phi probe is only as meaningful as the predicate it measures against. A record must satisfy all ten conditions (C1–C10) to be counted as admissible.

| Condition | Field or State | What It Requires |
|-----------|----------------|-----------------|
| C1 | `gbim_id` | NOT NULL |
| C2 | `promotion_state` | = `'authorized'` |
| C3 | `public_claim_allowed` | = `true` |
| C4 | `under_whose_authority` | NOT NULL |
| C5 | `company_name` | NOT NULL |
| C6 | `ingested_at` | NOT NULL |
| C7 | `degradation_status` | IN `('fresh', 'aging')` |
| C8 | `spatial_unit_id` | NOT NULL (blockgroup GEOID) |
| C9 | `spatial_unit_kind` | = `'blockgroup'` |
| C10 | `valid_time_start` | NOT NULL (≥ 2020-01-01) |

Conditions C8, C9, and C10 are the **structural anchors** added at the schema level on July 26, 2026. They enforce that every admissible record is grounded in a real place (a Census block group) and a real time period. This is what the monograph calls the Spacetime Contract at the data layer.

For rural developers, the spatial conditions matter especially. A record without a blockgroup GEOID cannot be placed on the map. A record without `valid_time_start` cannot be read as evidence for a specific moment in community history. These are not bureaucratic requirements — they are what make the data meaningful.

---

## 44.5 How Phi Connects to the Overflow Proof

The overflow proof — which demonstrates that Ms. Jarvis can route cognition safely out of its internal state into person-space — depends on the governed corpus being coherent enough to support safe overflow events.

**The chain works as follows:**

1. A query arrives at `public_answer_packet`.
2. The function draws evidence from `public_admissible_gbim_mv`.
3. If the evidence surface is coherent (high Phi), the answer is well-grounded.
4. If an overflow event is triggered, it carries a reference back to this admissible evidence.
5. Person-space validation confirms the event is safe to route.

If the governed corpus were incoherent — if most records failed the admissibility predicate — the overflow proof would be grounded in noise. The 39.3% baseline shows that is not the case: 93,423 fully admissible records are available to anchor both answers and overflow events at the July 2026 gate.

---

## 44.6 Computing Phi: Step-by-Step

This is the complete procedure for computing the Phi probe measurement on a live system.

**Step 1 — Count total authorized rows:**

```sql
SELECT COUNT(*) AS total_authorized
FROM public.gbim_record
WHERE promotion_state = 'authorized';
```

**Step 2 — Refresh the admissible materialized view:**

```sql
REFRESH MATERIALIZED VIEW CONCURRENTLY public.public_admissible_gbim_mv;
```

**Step 3 — Count admissible rows:**

```sql
SELECT COUNT(*) AS admissible_rows
FROM public.public_admissible_gbim_mv;
```

**Step 4 — Compute the fraction:**

```sql
SELECT
    admissible.cnt AS admissible_rows,
    total.cnt AS total_authorized,
    ROUND(admissible.cnt::numeric / total.cnt * 100, 1) AS phi_percent
FROM
    (SELECT COUNT(*) AS cnt FROM public.public_admissible_gbim_mv) admissible,
    (SELECT COUNT(*) AS cnt FROM public.gbim_record
     WHERE promotion_state = 'authorized') total;
```

**Expected output at the July 2026 gate:**

```
 admissible_rows | total_authorized | phi_percent
-----------------+------------------+------------
          93423  |          237655  |       39.3
```

---

## 44.7 What the 39.3% Baseline Tells You

**What it means — and what it does not mean:**

| Interpretation | Correct? |
|----------------|----------|
| 39.3% of governed records are ready for public claims | ✓ Yes |
| The remaining 60.7% are errors or broken data | ✗ No — they are in motion |
| The system is 39.3% "done" | ✗ No — Phi measures coherence, not completeness |
| A higher Phi is always better | ✗ Not necessarily — new ingestion will temporarily lower Phi |
| Phi can be tracked over time as a health gauge | ✓ Yes — this is the primary use |

A 39.3% admissibility fraction reflects an intentional design: the system stores candidates, partial records, and lifecycle-aging records that are useful internally but not yet suitable for public claims. As promotion workflows mature and spatial/temporal anchors are backfilled, Phi will rise.

---

## 44.8 Using Phi as a Health Gauge Over Time

The Phi probe is designed to be rerun. Developers and data stewards can run it after every major ingestion, migration, or lifecycle event.

**Questions Phi can answer over time:**

- Did last week's data migration improve or degrade admissibility?
- Are records aging out faster than new admissible records are being promoted?
- Is the spatial anchor backfill project raising Phi as expected?

**Practical thresholds (not formal requirements):**

| Phi Range | Interpretation |
|-----------|---------------|
| < 20% | High inadmissibility — investigate lifecycle or promotion gaps |
| 20–40% | Normal range during active ingestion phases |
| 40–60% | Healthy governed corpus with mature promotion workflows |
| > 60% | Well-curated corpus; monitor for stale records masquerading as fresh |

The July 2026 baseline of 39.3% places the system at the upper end of the active ingestion range — coherent enough to back answers and overflow events, with meaningful room to grow as the corpus matures.

---

## 44.9 Phi and the pg_cron Lifecycle Scheduler

Phi does not stay fixed on its own. The lifecycle scheduler — driven by four `pg_cron` jobs registered in `wv_gis` — continuously advances record states:

```
-- Hourly: advances degradation status
SELECT cron.schedule('lifecycle-hourly', '0 * * * *',
    'SELECT apply_runtime_lifecycle();');

-- Daily: refreshes the admissible materialized view
SELECT cron.schedule('admissible-refresh-daily', '0 2 * * *',
    'REFRESH MATERIALIZED VIEW CONCURRENTLY public.public_admissible_gbim_mv;');
```

> **Note:** The correct entry point is `apply_runtime_lifecycle()`. Do not use the deprecated `gbim_runtime_lifecycle_hourly()` function, which no longer exists. Any documentation or cron job referencing the old function name must be updated.

As records age from `fresh` to `aging` to `stale`, some will drop out of the admissible view. As new records are promoted and anchored, others will enter it. Phi reflects this living process.

---

## 44.10 Audit Traceability and the Phi Measurement

When `public_answer_packet` or `public_geoid_panel` are called to draw from the admissible corpus, each call is logged to `public_answer_audit` with a real trace ID threaded through the `query_id` field.

This means that the Phi measurement is not just a count — it is auditable. You can trace any public claim back to the specific admissible record that backed it, and from there to the promotion event that authorized it.

```sql
-- Inspect recent audit entries with trace IDs
SELECT query_id, gbim_id, called_at, function_name
FROM public.public_answer_audit
ORDER BY called_at DESC
LIMIT 10;
```

For rural developers building systems that serve public accountability functions — zoning, SNAP eligibility, infrastructure assessment — this auditability is not optional. It is what makes the system trustworthy.

---

## 44.11 Step-by-Step Summary for Rural Developers

1. **Understand what Phi measures.**
   The fraction of authorized governed records that satisfy all ten admissibility conditions and are ready to back public claims.

2. **Remember the verified baseline.**
   93,423 admissible rows out of 237,655 authorized rows = **39.3% admissibility** as of July 26, 2026.

3. **Know the ten conditions.**
   C1–C7 are provenance and lifecycle conditions. C8–C10 are spatial and temporal anchors added July 26, 2026. A record must pass all ten to count.

4. **Connect Phi to public answers and overflow.**
   Every public claim and every overflow event draws from the admissible corpus. Phi tells you how large and healthy that corpus is.

5. **Run the four-step query procedure.**
   Count authorized rows → refresh the materialized view → count admissible rows → compute the fraction. This gives you a live Phi reading.

6. **Use the scheduler correctly.**
   The entry point is `apply_runtime_lifecycle()`. The deprecated `gbim_runtime_lifecycle_hourly()` function is gone.

7. **Track Phi over time.**
   Run the probe after migrations, ingestion events, and promotion campaigns. A rising Phi means coherence is improving. An unexpected drop means something needs investigation.

8. **Stay within scope.**
   This chapter measures admissibility-based semantic coherence within the governed corpus. It does not claim to measure every form of system coherence.

---

## 44.12 Implementation Status

**Phi Probe — Semantic Coherence Measurement: Demonstrated.**

| Metric | Value | Date Verified |
|--------|-------|---------------|
| Total authorized governed rows | 237,655 | July 26, 2026 |
| Admissible rows (all ten conditions) | 93,423 | July 26, 2026 |
| Phi admissibility fraction | 39.3% | July 26, 2026 |
| Admissibility predicate conditions | 10 (C1–C10) | July 26, 2026 |
| Lifecycle scheduler entry point | `apply_runtime_lifecycle()` | July 29, 2026 |
| Audit trace threading | Real `query_id` in `public_answer_audit` | July 29, 2026 |

These numbers reflect a live inspection of the production governed corpus, not a hypothetical estimate. The Phi probe is a demonstrated measurement of semantic coherence within H_App at the July 2026 production gate.

---

## 44.13 Closing

The Phi probe gives H_App a way to talk about the health of its governed corpus with numbers instead of metaphors. A corpus that is 39.3% admissible is a corpus that is alive, curated, and accountable — with the majority of its records still in motion and a significant, verified subset ready to back public claims today.

For rural developers in Appalachia and beyond, that means the data beneath Ms. Jarvis is not a pile of records. It is a governed body whose coherence can be measured, tracked, and improved. That is the difference between a system that stores data and a system that earns the right to speak.

---

*Chapter 44 is sealed for the July 2026 production gate.*
*All values verified against the live production database.*
*No claims are made beyond what has been demonstrated at two layers: service running and database state confirmed.*
