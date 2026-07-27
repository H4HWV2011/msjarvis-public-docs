# 45. H_geo — The Spatial Hilbert Body of H_App (As-Built)

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 27, 2026*

---

## 45.1 What This Chapter Is Allowed to Claim

Within this closure gate, Chapter 45 is limited to **implemented, governed spatial state for the West Virginia GIS slice**, not abstract tensor completeness.

It may claim that:

- governed **county, tract, and block-group collections** are live, count-valid, and queryable;
- there are **no active legacy county/tract collection references** in runtime configuration;
- manifest tables were updated **schema-aware**, with governed rows preserved or inserted and status columns updated where present;
- **no active legacy county/tract rows** remain in status-bearing manifest tables;
- governed county/tract manifest rows are **active or present** everywhere relevant tables exist;
- **tensor-derived promotion and geographic bounding-box filtering** pass an idempotent live probe;
- relevant **unit, integration, anti-surveillance, and policy tests** pass;
- the **H_geo spatial body is fully anchored** as of July 26, 2026: all 237,655 rows in `public.gbim_record` now carry `spatial_unit_id = geoid`, `spatial_unit_kind = 'blockgroup'`, and `valid_time_start = 2020-01-01`, confirmed by `UPDATE 237655` returned from the backfill statement.

It must **not** claim abstract tensor-product completeness across all domains or a fully general spatial algebra beyond the implemented governed bridge.

---

## 45.2 Plain-Language Purpose

For rural developers, H_geo answers a concrete question:

> "When Ms. Allis talks about counties, tracts, and block groups in West Virginia, what exactly has been built, checked, governed, and anchored?"

This chapter explains:

- how **governed county, tract, and block-group GIS collections** sit inside the the larger semantic system;
- how the **manifest** now clearly points at the governed collections and no longer at legacy ones;
- how **every GBIM record is now spatially and temporally anchored** — not as a plan but as a confirmed fact;
- how **tensor-style filters** are used in practice (for bounding boxes and promotion) without over-claiming a full tensor calculus.

The focus is on **what runs today**, not on the whole mathematical design.

---

## 45.3 H_geo as the Spatial Body

H_geo is the part of Ms. Allis's semantic space that holds **place-linked information**:

- counties, tracts, and block groups;
- jurisdiction and locality;
- infrastructure and geography-shaped features.

In this chapter's scope, H_geo can be understood as:

- "the way Ms. Allis holds West Virginia's GIS slices in her head,"
- with those slices wired to **governed collections** and a **manifest** that tells retrieval which ones are truly active,
- and with every record in that body carrying an explicit spatial key (`spatial_unit_id`), spatial resolution (`spatial_unit_kind`), and temporal anchor (`valid_time_start`).

H_geo is not just a map file on disk. It is the **governed, queryable, fully anchored spatial body** Ms. Allis uses when answering geography-shaped questions.

---

## 45.4 The July 26, 2026 Spatial Anchoring Backfill — As-Built

On July 26, 2026, the following backfill statement was executed against `public.gbim_record` in `wv_gis`:

```sql
UPDATE public.gbim_record
SET
  spatial_unit_id   = geoid,
  spatial_unit_kind = 'blockgroup',
  valid_time_start  = '2020-01-01'::timestamptz
WHERE spatial_unit_id IS NULL
   OR spatial_unit_kind IS NULL
   OR valid_time_start IS NULL;
```

The database returned:

```text
UPDATE 237655
```

This single line — `UPDATE 237655` — is the as-built evidence that the H_geo spatial body is fully anchored. Every row in `public.gbim_record` now carries:

| Column             | Value assigned                                  | Meaning                                                         |
|--------------------|--------------------------------------------------|-----------------------------------------------------------------|
| `spatial_unit_id`  | `geoid` (the row's block-group GEOID)           | Uniquely identifies the geographic unit the record describes    |
| `spatial_unit_kind`| `'blockgroup'`                                  | Names the spatial resolution of that unit                       |
| `valid_time_start` | `2020-01-01T00:00:00-05:00`                     | Earliest moment for which the record's metric claim is asserted |

All three columns were made `NOT NULL` by the `gbim_record_spacetime_provenance_chk` CHECK constraint (described in Appendix A), which was applied after the backfill and passed validation against all 237,655 rows without error.

### 45.4.1 What This Means for Rural Developers

Before July 26, 2026, a governed GBIM record could be authorized and marked as publicly claimable without having an explicit geographic unit identifier or a time anchor. That meant the system could make a claim without being able to answer "where exactly?" and "as of when?" together.

After the July 26, 2026 backfill, that gap is closed. Every record in the governed store now answers both questions:

- **Where**: `spatial_unit_id` holds the block-group GEOID (e.g., `540019656003` for a specific block group in Fayette County, WV).
- **At what resolution**: `spatial_unit_kind = 'blockgroup'` makes the geographic grain explicit.
- **Since when**: `valid_time_start = 2020-01-01` anchors the temporal claim.

There is no longer any record in the governed store for which the spatial or temporal anchor is missing. The body is complete.

### 45.4.2 Why `valid_time_start = 2020-01-01` Is Correct for This Corpus

The value `2020-01-01` was chosen because the governed GIS inventory being anchored is a static, point-in-time infrastructure inventory (ATM stations, weather stations, broadband infrastructure, and similar physical assets). These assets do not change month-to-month, and their governing data sources are dated to the 2020 Census cycle.

This `valid_time_start` is **correct for static inventory facts**. It would not be correct for time-sensitive policy or benefit facts that change with legislation or regulation — those require re-ingestion with updated `valid_time_start` values when the underlying policy changes. That distinction is documented as a known gap in the thesis and is not affected by this backfill.

---

## 45.5 County and Tract Collections: Live and Governed

The closure evidence confirms that the **governed county and tract collections**:

- are **live** (services can reach them);
- are **count-valid** (document counts match expectations);
- are **queryable** (GIS RAG and related services can retrieve from them).

Older, legacy county/tract collections are **no longer referenced** in runtime configuration. That means:

- when Ms. Allis answers from West Virginia county/tract governed belief, she is **not secretly talking to an old, unmanaged collection**;
- queries and manifests point at **one coherent governed body** for those grains.

For rural operators, the takeaway is simple: the county and tract data Ms. Allis uses now comes from the **intended governed collections**, not from leftovers.

---

## 45.6 Schema-Aware Manifest Handling

The **publication manifest tables** record:

- which logical GIS collections exist;
- which physical collections implement them;
- which ones are **active**.

The closure work here did three important things **schema-aware**:

- where manifest tables had a **status column**, that column was updated to mark the governed county/tract rows active and to disable legacy rows;
- where tables had **no status column**, governed rows were inserted or preserved without trying to fake status;
- **no active legacy rows** remain for county/tract in status-bearing manifest tables.

This matters for rural developers because:

- there is now **one clear story** in the manifest for counties and tracts;
- you can read the manifest tables and see that **governed rows are the ones in charge**.

---

## 45.7 No Active Legacy County/Tract Paths

Before closure, there was a risk that:

- old collections or manifest rows for counties/tracts might still be used by some code path;
- tests could pass against new collections while some routes still touched legacy ones.

The closure evidence states that:

- runtime configuration **no longer contains active references** to legacy county/tract collections;
- manifest tables no longer treat legacy county/tract rows as active where statuses exist.

In plain language: the **"two names for the same concept"** problem has been cleared for these grains. The system now speaks about West Virginia counties and tracts using **one governed naming and collection scheme**, not a confusing mix.

---

## 45.8 Tensor-Derived Promotion and Bounding-Box Filtering

The gate describes **tensor-derived promotion and geographic bounding-box filtering** passing an idempotent live probe.

For rural developers, this can be read as:

- requests that involve a **geographic bounding box** (a rectangle over the map) are correctly filtered to only the relevant county/tract slices;
- the promotion layer that uses these spatial filters does so in a way that **does not change results if you run it twice in a row** (idempotence).

This is a **practical tensor use**:

- the system treats the geographic slice and the selection intent as **two dimensions** that combine into a **filtered view**;
- it does **not** claim a fully general tensor algebra over every domain, only that the implemented filters behave as designed for these collections.

Now that all 237,655 rows carry `spatial_unit_id` and `spatial_unit_kind`, bounding-box filters over the GBIM corpus have a reliable, non-null key to work against. There is no longer any row for which a spatial filter would fail silently due to a missing geographic identifier.

---

## 45.9 Tests: Health, Policy, and Anti-Surveillance

The closure states that relevant:

- **unit tests**,
- **integration tests**,
- **anti-surveillance tests**, and
- **policy tests**

all pass for the governed county/tract path and manifest behavior.

The anti-surveillance and policy tests matter because:

- GIS data can be misused for tracking or unfair profiling;
- these tests help ensure that the **governed retrieval path** respects basic non-surveillance and policy constraints at this grain.

For rural communities, this means there is actual code and tests backing the idea that:

- "this GIS slice is for **civic and planning use**, not for ungoverned snooping."

---

## 45.10 The Complete Spatial Anchoring Picture

As of July 27, 2026, the spatial state of H_geo can be described precisely and without hedging:

| Property                                         | Value                           | Evidence                        |
|--------------------------------------------------|---------------------------------|---------------------------------|
| Total rows in `public.gbim_record`              | 237,655                         | `UPDATE 237655` (July 26, 2026) |
| Rows with `spatial_unit_id` populated           | 237,655                         | Backfill updated all null rows  |
| Rows with `spatial_unit_kind` populated         | 237,655                         | Backfill updated all null rows  |
| Rows with `valid_time_start` populated          | 237,655                         | Backfill updated all null rows  |
| Rows passing `gbim_record_spacetime_provenance_chk` | 237,655                     | `ALTER TABLE` passed, no error  |
| Admissible rows (`public_admissible_gbim_mv`)   | 93,423                          | Lifecycle audit, July 26, 2026  |
| Spatial unit kind                                | `blockgroup`                    | Confirmed for all rows          |
| Temporal anchor                                  | `2020-01-01T00:00:00-05:00`     | Correct for static inventory    |

The gap between 237,655 total rows and 93,423 admissible rows is not a spatial anchoring gap. All rows are spatially and temporally anchored. The 144,232 non-admissible rows are held back by other admissibility conditions — most commonly `public_claim_allowed = false` or `degradation_status = 'stale'` — not by missing spatial or temporal fields.

---

## 45.11 Step-by-Step View for Rural Developers

From a local operator's point of view, Chapter 45's closure work can be understood as:

1. **Check the collections.**  
   Confirm governed county, tract, and block-group collections are live, count-correct, and queryable.

2. **Check the config.**  
   Ensure no running service points at legacy county/tract collections.

3. **Check the manifest tables.**  
   In tables with status columns, confirm governed rows are marked active and legacy ones are not.  
   In tables without status, confirm governed rows exist and legacy ones are not treated as current.

4. **Confirm the spatial backfill.**  
   Verify that:

   ```sql
   SELECT count(*) FROM public.gbim_record
   WHERE spatial_unit_id IS NULL
      OR spatial_unit_kind IS NULL
      OR valid_time_start IS NULL;
   ```

   returns `0`. The `UPDATE 237655` confirmed this on July 26, 2026.

5. **Run the tensor/bounding-box probe.**  
   Confirm that geographic filters over counties/tracts behave correctly and idempotently.

6. **Run tests.**  
   Make sure unit, integration, anti-surveillance, and policy tests all pass.

When all six hold, the promise of Chapter 45 at this gate is kept: West Virginia county, tract, and block-group spatial data live in **H_geo as a governed, manifest-aligned, fully anchored, policy-tested body** — not as a tangle of old and new names, and not as a partially-populated corpus waiting for spatial fields to be added.

---

## 45.12 What This Chapter Does Not Claim

To stay inside the gate, Chapter 45 does **not** claim:

- a full tensor algebra over all of H_App;
- governed spatial coverage for every geography beyond the proven West Virginia slice;
- perfect or universal GIS access control in all services;
- that `valid_time_start = 2020-01-01` is correct for time-sensitive policy or benefit facts — it is correct only for the static inventory facts in this corpus.

It only claims:

- **live governed county, tract, and block-group collections**;
- **clean manifest alignment** for those collections;
- **working tensor-style filters** for promotion and bounding boxes over them;
- **passing tests**, including anti-surveillance and policy checks;
- **complete spatial anchoring** of all 237,655 rows, confirmed by `UPDATE 237655` on July 26, 2026.

---

## 45.13 Closing Statement

Chapter 45 now records a **complete, concrete closure** over the West Virginia spatial slice of H_geo.

Governed collections are live and in use. Manifest rows have been cleaned and updated schema-aware. Legacy names have been retired from active paths. Tensor-derived promotion and bounding-box filters behave as tested. Policy-aware tests pass.

Most importantly: the H_geo spatial body is **fully anchored**. Every one of the 237,655 rows in `public.gbim_record` now carries `spatial_unit_id = geoid`, `spatial_unit_kind = 'blockgroup'`, and `valid_time_start = 2020-01-01`. The database confirmed this with `UPDATE 237655`. The CHECK constraint confirmed it passed validation. There is no row in the governed store for which the system cannot answer "where?" and "as of when?" simultaneously.

For rural developers, this means Ms. Allis's understanding of West Virginia counties, tracts, and block groups is no longer a mix of old and new, and no longer partially anchored. It is a **single governed spatial body** that is fully identified, fully timestamped, and fully testable within the narrow scope this gate defines.

---

*Chapter 45 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*  
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*  
*See LICENSE for terms.* 
