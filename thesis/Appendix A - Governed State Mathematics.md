# Appendix A — Governed State Mathematics (As‑Built)

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 26, 2026*

---

## A.0 Overview and Purpose

Appendix A defines the mathematical structure of governed state in the Ms. Jarvis / Ms. Allis system and maintains the **verification discipline** that keeps the thesis honest about what is running versus what is planned.

After the July 26, 2026 architecture closeout, governed state gained three new structural columns — `spatial_unit_id`, `spatial_unit_kind`, and `valid_time_start` — that close the spatial and temporal halves of the Spacetime Contract (Chapter 53). This appendix now contains the formal admissibility predicate derived from those changes, the verification discipline rules, all demonstrated paths through the stack, and guidance for rural developers who need to audit or extend this system.

If a chapter claims a mechanism is live, it must be able to point back here to evidence that meets the standard defined in §A.1.

---

## A.1 Demonstrated vs. Not‑Yet‑Demonstrated

Every mechanism in the thesis must live in one of two registers.

**Demonstrated** — A claim is demonstrated only when a real path has been exercised and confirmed across at least two layers:
- A service or script is running on the expected port or schedule.
- An endpoint or worker produces live behavior.
- Database, Chroma, or Redis state shows the expected effect.
- Logs or test probes confirm the result.

**Not Yet Demonstrated** — A claim is not yet demonstrated when it is:
- Only described architecturally in text.
- Implemented in code but never exercised end‑to‑end.
- Visible only in tests or prototypes, not in the live services layer.
- Dependent on tables, routes, or keys that do not yet exist.

No chapter may quietly promote an architectural idea to "live behavior" without this kind of evidence. Appendix A's job is to keep that line clear.

---

## A.2 The Governed State Definition

A *governed state record* in this system is a row in `public.gbim_record` that has been promoted to `authorized` status and satisfies all structural constraints. As of July 26, 2026, the governed state definition includes three new structural columns that were not present in earlier versions of the schema.

### A.2.1 Structural Columns Added July 26, 2026

The following columns were added to `public.gbim_record` and made `NOT NULL`:

| Column | Type | Role in Governed State |
|---|---|---|
| `spatial_unit_id` | `text NOT NULL` | Normalized spatial key (e.g., blockgroup GEOID). Anchors the record to a specific geographic unit in the authoritative WV spatial domain. |
| `spatial_unit_kind` | `text NOT NULL` | Classification of the spatial unit: `'blockgroup'`, `'tract'`, `'county'`, or equivalent. Makes the spatial anchor self‑describing. |
| `valid_time_start` | `timestamptz NOT NULL` | The earliest moment for which the record's metric claim is asserted. Closes the temporal half of the Spacetime Contract. |

These three columns are **structural requirements**, not runtime filters. Every row in `public.gbim_record` must have them populated; the system will reject an insert or update that would leave them null on a row where `promotion_state = 'authorized'` and `public_claim_allowed = true`, due to the cross‑column CHECK constraint described in §A.3.

### A.2.2 What This Means for Rural Developers

Before July 26, 2026, a record could be marked as authorized for public claims without having an explicit spatial unit identifier or a time anchor. That gap meant the system could make a claim without being able to answer "where exactly?" and "as of when?" simultaneously.

Adding these three columns closes that gap. Now every public claim the system emits is tied to a named spatial unit at a specific resolution (`spatial_unit_kind`) with a specific key (`spatial_unit_id`) that is valid starting from a specific point in time (`valid_time_start`). If those fields are missing, the record is stored but inadmissible.

---

## A.3 The Cross‑Column Spacetime/Provenance CHECK Constraint

The following CHECK constraint was added to `public.gbim_record` on July 26, 2026 and was verified against 237,655 rows without error:

```sql
ALTER TABLE public.gbim_record
ADD CONSTRAINT gbim_record_spacetime_provenance_chk
CHECK (
  NOT (promotion_state = 'authorized' AND public_claim_allowed = true)
  OR (
    spatial_unit_id IS NOT NULL
    AND spatial_unit_kind IS NOT NULL
    AND valid_time_start IS NOT NULL
    AND under_whose_authority IS NOT NULL
    AND company_name IS NOT NULL
    AND ingested_at IS NOT NULL
  )
);
```

This constraint is evaluated at the table level on every insert and update. Its logic reads: *if a row is both authorized and flagged as publicly claimable, then all spatial, temporal, and provenance fields must be populated; otherwise the row is rejected*. Rows that are stored but not yet authorized, or that have `public_claim_allowed = false`, are not subject to these requirements and may be held in an incomplete state during ingestion or review.

The constraint passed `ALTER TABLE` cleanly, which confirms that all existing rows satisfied these requirements at the time of the gate.

---

## A.4 Formal Definition — The Ten‑Condition Public Admissibility Predicate

**Definition A.1 (Public Admissibility).**  
Let $r$ denote a row in `public.gbim_record`. The row $r$ is *publicly admissible* — meaning it may enter the public evidence surface `public_admissible_gbim_mv` and back a public claim — if and only if all ten of the following conditions hold simultaneously:

$$\text{admissible}(r) \iff C_1(r) \wedge C_2(r) \wedge C_3(r) \wedge C_4(r) \wedge C_5(r) \wedge C_6(r) \wedge C_7(r) \wedge C_8(r) \wedge C_9(r) \wedge C_{10}(r)$$

where the ten conditions are:

| Condition | SQL predicate | What it enforces |
|---|---|---|
| $C_1$ | `g.gbim_id IS NOT NULL` | Record identity — every admissible record must have a non‑null primary key. |
| $C_2$ | `g.promotion_state = 'authorized'` | Authorization — the record has passed the GBIM promotion gate and is not merely a candidate or provisional entry. |
| $C_3$ | `g.public_claim_allowed = true` | Explicit public flag — a separate column that must be affirmatively set, independent of authorization. |
| $C_4$ | `g.under_whose_authority IS NOT NULL` | Legal provenance — the authorizing body for the record must be named. |
| $C_5$ | `g.company_name IS NOT NULL` | Organizational provenance — the originating organization must be named. |
| $C_6$ | `g.ingested_at IS NOT NULL` | Ingestion timestamp — the moment of record acceptance into the governed store must be documented. |
| $C_7$ | `g.degradation_status IN ('fresh', 'aging')` | Lifecycle state — only records that are fresh or aging are admissible; stale records are excluded from public claims even if authorized. |
| $C_8$ | `g.spatial_unit_id IS NOT NULL` | Spatial anchor — added July 26, 2026; no record may be publicly admitted without identifying its geographic unit. |
| $C_9$ | `g.spatial_unit_kind IS NOT NULL` | Spatial resolution — the kind of spatial unit (blockgroup, tract, county) must be specified. |
| $C_{10}$ | `g.valid_time_start IS NOT NULL` | Temporal anchor — the earliest moment of validity for the claim must be specified. |

**Remark.** Conditions $C_1$ through $C_7$ were present in the pre‑July 26 architecture. Conditions $C_8$, $C_9$, and $C_{10}$ were added on July 26, 2026, closing the spatial and temporal halves of the Spacetime Contract. The admissibility predicate is a conjunction: any single false condition renders the entire row inadmissible regardless of the status of the other nine.

### A.4.1 Implementation in SQL

The predicate above is directly instantiated as the `WHERE` clause of `public.public_admissible_gbim`:

```sql
CREATE VIEW public.public_admissible_gbim AS
SELECT g.*
FROM public.gbim_record g
WHERE g.gbim_id IS NOT NULL                           -- C1
  AND g.promotion_state = 'authorized'               -- C2
  AND g.public_claim_allowed = true                  -- C3
  AND g.under_whose_authority IS NOT NULL            -- C4
  AND g.company_name IS NOT NULL                     -- C5
  AND g.ingested_at IS NOT NULL                      -- C6
  AND g.degradation_status IN ('fresh','aging')      -- C7
  AND g.spatial_unit_id IS NOT NULL                  -- C8
  AND g.spatial_unit_kind IS NOT NULL                -- C9
  AND g.valid_time_start IS NOT NULL;                -- C10
```

`public.public_admissible_gbim_mv` is a materialized version of this view, refreshed by `runtime_governance.refresh_public_admissible_gbim_mv()`.

### A.4.2 Verified Row Counts (July 26, 2026 Gate)

The lifecycle audit at the July 26 gate produced the following counts, recorded in `runtime_governance.public_answer_audit`:

| Metric | Count |
|---|---|
| Total authorized rows | 237,655 |
| Admissible for public claims (all ten conditions) | 93,423 |
| Stored but inadmissible | 144,232 |

The 144,232 inadmissible rows are not errors. They represent records held in the governed store that do not meet all ten conditions — for example, records with `public_claim_allowed = false` or with lifecycle status `stale`. The system stores them; it does not speak them.

---

## A.5 The Separation of Stored State from Speakable State

A key principle of this architecture is that *stored* and *speakable* are different registers.

**Stored state** is everything in `public.gbim_record`. The governance runtime (`runtime_governance_role`) can read, write, and audit all stored state. This broad access is intentional: governance and lifecycle maintenance require visibility into inadmissible records to understand why they are inadmissible, to backfill missing fields, and to promote or demote records over time.

**Speakable state** is only what passes the ten‑condition predicate and appears in `public_admissible_gbim_mv`. The public instrument (`public_instrument_role`) can only read from this materialized view and from `runtime_governance.public_answer_audit`. A direct `SELECT` on `public.gbim_record` returns `permission denied` for the public role — confirmed at the July 26 gate.

This separation means the system can evolve its internal state freely without risking premature public disclosure. Records ingested today may not be publicly admissible until they complete their promotion and lifecycle journey. That journey is tracked; the destination is enforced.

---

## A.6 The Runtime Governance Role Structure

Two roles were established on July 26, 2026 to enforce the stored/speakable boundary:

**`runtime_governance_role`**  
- Full `SELECT`, `INSERT`, `UPDATE`, `DELETE` on `public.gbim_record`.  
- Row‑Level Security policy `gbim_read_policy` with `USING (true)` — sees all rows.  
- Responsible for running lifecycle refresh functions, backfilling spacetime columns, and promoting records.  
- This is an internal governance role, not exposed to the public instrument surface.

**`public_instrument_role`**  
- `SELECT` only on `public.public_admissible_gbim_mv` and `runtime_governance.public_answer_audit`.  
- No access to `public.gbim_record` — any attempt raises `permission denied`.  
- This role backs the public‑facing answer function `runtime_governance.public_answer_packet(geoid, metric_name)`.  
- Only admissible evidence may enter a public claim through this role.

---

## A.7 The public_answer_packet Function

The function `runtime_governance.public_answer_packet(p_geoid text, p_metric_name text)` is the primary public evidence surface. It is a `SECURITY DEFINER` PL/pgSQL function with `search_path` pinned to `public, runtime_governance, pg_temp`.

When called as `public_instrument_role`, it returns a `jsonb` document with the following structure, shown here from the July 26, 2026 live run against geoid `540019656003`:

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

The `label` field distinguishes three answer states:
- **`"seen"`** — Direct admissible evidence exists for the requested geoid and metric.
- **`"inferred"`** — Multiple admissible evidence rows exist and a summary is produced.
- **`"inadmissible"`** — No admissible evidence exists; the answer is a structured refusal, not a guess.

This is the Spacetime Contract at runtime: every answer carries `spatial_unit_id`, `spatial_unit_kind`, and `valid_time_start` in its evidence block, or it does not answer at all.

---

## A.8 AAPCAppE → Chroma → GBIM Corpus Path

At the corpus level, the as‑built architecture includes a specific Appalachian pipeline:

1. **AAPCAppE scraper (port 8033)** — Service `jarvis-aaacpe-scraper`. Scrapes Appalachian linguistic information and related texts. Output: corpus chunks ready for vectorization.
2. **Chroma corpus storage (port 8002)** — Service `jarvis-chroma`. Stores vectors and metadata for scraped documents; the inspected Chroma collections include the one receiving AAPCAppE output.
3. **GBIM intake path** — GBIM queries Chroma via the standard retrieval pipeline: $M_{\text{corpus}} \rightarrow C_{\text{retrieved}} \rightarrow S_{\text{sandbox}} \rightarrow F_{\text{candidate}}$. Appalachian corpus evidence flows AAPCAppE → Chroma → GBIM.

This entire path has been exercised and is treated as **demonstrated**.

---

## A.9 The GBIM Promotion Contract

GBIM provides the canonical demonstrated example of a governed promotion contract in the system. The contract has three key pieces:

1. **Trigger (guardrail)** — A BEFORE trigger on insert/update checks that the target manifest row is coherence‑approved and in the correct status. It rejects activation if `coherence_ok` is false.
2. **Evaluator (`coherence_ok`)** — Populates a `coherence_ok` flag on the manifest row. Runs as part of the GBIM build/validate pipeline, not as a manual toggle.
3. **Procedure (`promote_gbim_collection`)** — The single sanctioned promotion path. Verifies `coherence_ok == true`, sets `active` status, and updates `gbim_active_collection`. The trigger aborts if the guard is violated.

This triad — trigger, evaluator, procedure — is **demonstrated**: it has been run on real manifests including negative tests that attempted to activate non‑coherent or superseded manifests.

---

## A.10 Live Scheduled Runners and the Epistemic Loop

As of July 26, 2026, the following pg_cron jobs are registered and active in `wv_gis`:

| Job name | Schedule | Procedure |
|---|---|---|
| `gbim-runtime-lifecycle-daily` | `5 3 * * *` | `runtime_governance.gbim_runtime_lifecycle_daily()` |
| `gbim-runtime-lifecycle-hourly` | `15 * * * *` | `runtime_governance.gbim_runtime_lifecycle_hourly()` |
| `gbim-runtime-lifecycle-weekly` | `0 2 * * 0` | `runtime_governance.gbim_runtime_lifecycle_weekly()` |
| `gbim-runtime-lifecycle-monthly` | `30 1 $ * *` | `runtime_governance.gbim_runtime_lifecycle_monthly()` |

These jobs implement the recurrent epistemic loop described in Chapter 52. In addition, the following application‑layer workers contribute:

| Worker | Schedule | Role |
|---|---|---|
| `conversation_retention_worker.py` | Hourly | Enforces per‑user conversational retention policies over Chroma. |
| `identity_promotion.py` | Daily at 03:00 | Moves identities between provisional and confirmed states. |
| `recurrent_epistemic_runner.py` | On reboot (crypto-venv) | Coordinates Chapter 41 continuous validation and service health checks. |

The `dgm_cycle.sh` runner is **paused**, replaced by the recurrent epistemic runner; it is retained here as a historical reference.

---

## A.11 Redis `hilbert:time:*` Keys and Temporal Verification

The July 2026 temporal probes revealed a family of Redis keys under `hilbert:time:*`, including:

- `hilbert:time:asbuilt_ch49`, `hilbert:time:asbuilt_ch49_clean`
- `hilbert:time:ch04_ch44_probe_...` (multiple probe keys)
- `hilbert:time:commons_coherence`, `hilbert:time:commons_coherence_probe`
- `hilbert:time:ingest:blockgroup:540019655001`
- `hilbert:time:test:naive-fix`, `hilbert:time:test:utc-fix`

These confirm a live Hilbert‑time service is running with named port binding and that temporal operations can read/write these keys and observe TTL/decay behavior.

The `/policy/set` endpoint at port 8099 (`services/policy_set_service.py`) is under construction but has not yet passed end‑to‑end verification. It remains **Not Yet Demonstrated** and its cron entry remains commented out until the endpoint is reachable, honors its request/response contract, and fails closed on missing authorization.

---

## A.12 Live Chroma Collections

The July 2026 inspection confirmed the following Chroma collections are in active use:

- **AAPCAppE / corpus collections** — receiving Appalachian linguistic corpus material from `jarvis-aaacpe-scraper`; GBIM's retrieval path reads from these via $M_{\text{corpus}} \rightarrow C_{\text{retrieved}}$.
- **Per‑user conversation collections** — `conversation_history_user_<slug>`, `conversation_private_user_<slug>`, `conversation_staged_user_<slug>`. No cross‑user record leak between alpha and beta users was observed.
- **Community Hilbert Commons** — `community_hilbert_commons` on port 8055; stores centroid + provenance records for k‑thresholded, public‑opt‑in community vectors; suppresses under‑threshold groups.

---

## A.13 How to Read This Appendix as a Rural Developer

For developers operating or auditing this stack from communities like Mount Hope, WV, Appendix A is a practical checklist with five questions:

1. **Is there a live service or worker?** Check the named port or the scheduled script in §A.10.
2. **Can you exercise it?** Call `runtime_governance.public_answer_packet` or let a pg_cron job fire and observe `cron.job_run_details`.
3. **Does a store or keyspace confirm the effect?** Inspect the admissible row count in `public_admissible_gbim_mv`, or check `runtime_governance.public_answer_audit` for lifecycle snapshots.
4. **Is the path governed?** Look for the ten‑condition predicate (§A.4), the spacetime/provenance CHECK constraint (§A.3), and the role boundary (§A.6). The proof that candidate material cannot leak into the public evidence surface is in §A.5.
5. **Is the chapter honest about status?** Does it use "Demonstrated" only where evidence of the kind described in §A.1 exists? Does it mark architectural ideas as "Not Yet Demonstrated" where appropriate?

If the answer to any of these questions is "no," Appendix A expects the claim to be narrowed, the discrepancy to be logged, or the path to be strengthened.

---

## A.14 Closing Statement

Appendix A turns governed state mathematics into a lived verification discipline.

The ten‑condition public admissibility predicate in §A.4 is the formal heart of this appendix. It states precisely what it means for a GBIM record to be speakable: authorized, publicly flagged, provenanced, fresh or aging in its lifecycle, spatially anchored by `spatial_unit_id` and `spatial_unit_kind`, and temporally anchored by `valid_time_start`. All ten conditions must hold simultaneously. Any single failure closes the gate.

The three structural columns added on July 26, 2026 — `spatial_unit_id`, `spatial_unit_kind`, and `valid_time_start` — closed the spatial and temporal halves of the Spacetime Contract at the schema level. Their addition, backfill, and promotion to `NOT NULL` were verified against 237,655 rows without error. The resulting admissible surface of 93,423 rows represents the current public claim inventory.

The ledger of what is actually true in the code and services today lives here. The procedure for updating that ledger as the system grows lives here too: demonstrate at two layers, then promote. Anything less stays in the Not Yet Demonstrated register until it earns its place.
