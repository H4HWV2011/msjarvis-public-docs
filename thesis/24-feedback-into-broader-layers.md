# 24. Feedback into Broader Layers

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: July 27, 2026*

---

## 24.1 Why This Matters for Polymathmatic Geography

This chapter explains how Ms. Allis sends **feedback signals** into broader layers of the system without letting raw sandbox output rewrite memory, governance, or commons directly. It shows how feedback is bounded, consent-gated, and provenance-bearing — and how every invocation of the public civic claim function leaves a durable, inspectable audit trail in `runtime_governance.public_answer_audit`.

It supports:

- **P1 – Every where is entangled** by letting local observations influence retrieval, learning, and governance, but only through explicit records.
- **P3 – Power has a geometry** by treating upward feedback as movement across authority layers, not as a free write.
- **P5 – Design is a geographic act** by making feedback routing part of the system's map: which signals may travel where, and under what rules.
- **P12 – Intelligence with a ZIP code** by letting place- and people-specific gaps or patterns nudge broader behavior without leaking raw transcripts.
- **P16 – Power accountable to place** by logging feedback into auditable collections and tables instead of silently changing behavior.

This chapter belongs to the **Computational Instrument** tier. It documents feedback as built: **records written into governed stores**, not ad-hoc self-modification.

---

## 24.2 What Counts as Feedback into Broader Layers

"Feedback into broader layers" means **writing small, structured records** that other subsystems can read later. These records never contain raw transcripts or unreviewed sandbox traces.

Allowed **source types** for feedback include:

- retained conversation summaries (already approved and retention-eligible);
- background patterns that passed Chapter 21 rules;
- automated learning gaps (for example, "system is weak on X");
- continuous validation results (for example, "Phi/coherence degraded here");
- DGM cycle outcomes;
- PIA reviews;
- commons governance records (for example, decisions about what belongs in commons);
- civic claim invocations logged by `runtime_governance.public_answer_packet`.

Allowed **target layers** include:

- retrieval bias hints;
- background pattern updates;
- automated learning gap queues;
- WOAH (optimization) hints;
- pituitary (global mode) hints;
- governance review queues;
- continuous validation watch lists;
- the durable civic claim audit trail in `runtime_governance.public_answer_audit`.

Each feedback record is:

- **bounded** — small, focused, and scoped;
- **consent-gated** — respecting user retention settings;
- **provenance-bearing** — with a hash or pointer to its source;
- **auditable** — stored in a Chroma collection such as `broader_layer_feedback_records` or, for civic claim feedback, in the PostgreSQL table `runtime_governance.public_answer_audit`.

---

## 24.3 The Civic Claim Audit Trail: runtime_governance.public_answer_audit

Every invocation of `runtime_governance.public_answer_packet` — the function that produces structured public civic claims — is logged as a feedback record in `runtime_governance.public_answer_audit`. This table is the durable audit trail for civic claim feedback: it records what was asked, when it was asked, what the admissibility state of the evidence was at the time, and how many rows passed or failed the ten-condition predicate.

For rural developers, this means that the civic claim layer is not a black box. Every time the system answers a question about a community — "How many weather stations are in this blockgroup?" — a row is written to `runtime_governance.public_answer_audit` that documents the governance state behind that answer. The table is readable by the governance runtime, inspectable by operators, and persistent across restarts.

The July 26, 2026 lifecycle snapshot — the concrete background store illustration introduced in Chapter 21 — was itself written to `runtime_governance.public_answer_audit` as a `lifecycle_snapshot` stage entry. That entry is a feedback record from the governed data layer into the governance audit layer, carrying the counts of fresh, aging, stale, authorized, admissible, and inadmissible rows at that moment in time.

### Structure of the audit table

```sql
CREATE TABLE IF NOT EXISTS runtime_governance.public_answer_audit (
  audit_id   bigserial PRIMARY KEY,
  query_id   text        NOT NULL,
  stage      text        NOT NULL,
  detail     jsonb       NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT now()
);
```

The `stage` column names what kind of feedback entry this row represents. Observed stage values include:

| Stage value | What it records |
|---|---|
| `refresh_public_admissible_gbim_mv` | Materialized view refresh: row count and timestamp |
| `lifecycle_snapshot` | Full admissibility count breakdown at a point in time |
| `public_answer_packet` | Individual civic claim invocation: geoid, metric, answer blocks, admissibility summary |

For rural developers, reading this table is the first step in auditing what the civic claim layer has been doing:

```sql
SELECT audit_id, stage, detail, created_at
FROM runtime_governance.public_answer_audit
ORDER BY audit_id DESC
LIMIT 20;
```

---

## 24.4 How Feedback Records Are Structured (General)

Every general feedback record has a compact structure:

```markdown
- source_type        # e.g., retained_conversation, background_pattern, automated_learning_gap
- source_id          # identifier within that source
- target_layer       # e.g., retrieval_bias, automated_learning_gap_queue, governance_review
- request_purpose    # almost always "governance" or a similarly bounded purpose
- actor_role         # typically "system" for internal feedback
- retention_consent  # true/false
- phi_floor_met      # true/false (coherence/health check)
- provenance_hash    # hash linking back to evidentiary context
- human_review_required  # true/false
```

Civic claim feedback records written to `runtime_governance.public_answer_audit` use the `detail` jsonb column to carry the same information in a structured form: query parameters, answer blocks with evidence fields, and the admissibility summary showing how many records were seen, inferred, or inadmissible at the time of the claim.

Only records that pass all checks are written to the feedback collection. For civic claim records, the check is the ten-condition admissibility predicate: only admissible evidence enters the `answer_blocks` field of the logged claim.

---

## 24.5 Consent and Raw-Data Suppression

Two hard suppression rules govern feedback:

1. **No consent → no feedback write.** If `retention_consent` is false for a `retained_conversation` source, the verdict is **SUPPRESS** and the record is not written, even if everything else is valid.

2. **Raw transcript or forbidden metadata → SUPPRESS.** If the projection attempts to include raw transcripts, private identity data, or forbidden fields, the feedback record is suppressed.

These rules apply to the general feedback path. The civic claim path through `runtime_governance.public_answer_packet` applies an equivalent constraint: no record enters the `answer_blocks` of a logged claim unless it passes all ten admissibility conditions. A claim that finds no admissible evidence returns a structured refusal — logged to `runtime_governance.public_answer_audit` with an `inadmissible_count` rather than a fabricated answer.

This ensures broader layers see **clean signals**, not copies of user conversations or inadmissible records.

---

## 24.6 Phi/Coherence Floors and Review

Feedback records also depend on **system coherence**, via Phi and related measures:

- If `phi_floor_met` is **true**, and other conditions are satisfied, a feedback record can be **PERMIT**ted and written.
- If `phi_floor_met` is **false**, even with consent and a valid source type, the verdict is **REVIEW**, and no direct write occurs.

The `low_phi` case shows:

- source_type: `continuous_validation`;
- target_layer: `continuous_validation_watch`;
- `phi_floor_met: false`;
- verdict: **REVIEW**.

This means: "The system noticed a coherence problem. Instead of automatically pushing this into the watch list, it flags it for review." The civic claim path has an analogous behavior: if the governance runtime detects that the materialized view has not been recently refreshed or that lifecycle counts show an unexpected degradation, the `runtime_governance.public_answer_audit` record for that invocation will reflect the stale state rather than silently serving outdated evidence.

---

## 24.7 Examples of Permitted Feedback

Two concrete permitted examples from the gate:

1. **Background pattern → retrieval bias.**
   - `source_type`: `background_pattern`
   - `target_layer`: `retrieval_bias`
   - `verdict`: **PERMIT**
   - Written into `broader_layer_feedback_records`.

   This lets a vetted background pattern slightly influence which documents are retrieved, without exposing raw data.

2. **Automated learning gap → learning gap queue.**
   - `source_type`: `automated_learning_gap`
   - `target_layer`: `automated_learning_gap_queue`
   - `verdict`: **PERMIT**
   - Written into `broader_layer_feedback_records`.

   This lets the system remember "I struggled with this topic; please schedule a learning task later," without altering the core models directly.

A third class of permitted feedback is the civic claim audit record:

3. **Civic claim invocation → runtime_governance.public_answer_audit.**
   - `source_type`: civic claim via `runtime_governance.public_answer_packet`
   - `target_layer`: `runtime_governance.public_answer_audit`
   - `verdict`: **PERMIT** (written on every invocation, regardless of whether admissible evidence was found)
   - Carries: query parameters, evidence blocks with `spatial_unit_id`, `spatial_unit_kind`, `valid_time_start`, and the full admissibility summary.

   In all three cases: consent, provenance, and admissibility rules are satisfied before anything is written.

---

## 24.8 Examples of Suppressed Feedback

The same contract also shows what **may not** be written:

- **Binding legal action.** A projection with source_type `commons_governance_record` and target_layer `governance_review` is blocked when it carries `binding_legal_action` metadata. Verdict: **SUPPRESS**.
- **No retention consent.** A `retained_conversation` projection targeting `background_pattern` is suppressed when `retention_consent` is false.
- **Raw transcript.** Any projection marked with forbidden `raw_transcript` or similar metadata is suppressed.

These examples enforce the gate's scope: no binding legal action, no clinical diagnosis, no financial instruction, no unreviewed self-modification, no raw trace propagation.

---

## 24.9 Allowed vs Blocked Flows

| Source type | Target layer | Status | Reason |
|---|---|---|---|
| background_pattern | retrieval_bias | PERMIT | Bounded feedback record permitted |
| automated_learning_gap | automated_learning_gap_queue | PERMIT | Bounded feedback record permitted |
| public_answer_packet invocation | runtime_governance.public_answer_audit | PERMIT | Durable civic claim audit trail; written on every invocation |
| continuous_validation | continuous_validation_watch | REVIEW | Phi floor not met → review required |
| retained_conversation | background_pattern (no consent) | SUPPRESS | Retention consent required |
| retained_conversation | background_pattern (raw_trace) | SUPPRESS | Forbidden metadata: raw_transcript |
| commons_governance_record | governance_review (binding) | SUPPRESS | Forbidden metadata: binding_legal_action |

This table is the wiring diagram for Chapter 24. The civic claim audit row is new as of July 26, 2026 and represents the feedback path from the governed data layer back into the governance audit layer.

---

## 24.10 What Chapter 24 Does Not Claim

Within this gate, Chapter 24 does **not** claim:

- automatic or unconstrained self-modification;
- direct propagation of raw sandbox traces into broader layers;
- binding legal actions;
- clinical diagnosis or therapeutic decisions;
- financial instructions;
- guaranteed safety;
- that every row in `runtime_governance.public_answer_audit` represents a successful civic claim — some rows represent structured refusals when no admissible evidence was found.

Instead, it claims:

- **bounded feedback records** with consent and provenance;
- **suppression** when consent, Phi, or metadata rules fail;
- **review** when coherence is low or stakes are high;
- **a durable audit trail** in `runtime_governance.public_answer_audit` for every invocation of the civic claim function, whether that invocation produced evidence or a structured refusal.

Broader layers see **small, structured hints and audit records**, not uncontrolled writes.

---

## 24.11 Step-by-Step View for Rural Developers

On a running system, feedback into broader layers behaves like this:

1. **Some event happens.** For example, a DGM cycle finds a gap, a background pattern is updated, or a community member's query invokes `runtime_governance.public_answer_packet`.

2. **A projection or invocation record is built.** A small record is drafted with source type, source identifier, target layer, provenance, and flags. For civic claim invocations, the record includes the query parameters, evidence blocks, and admissibility summary.

3. **Contract rules run.** The system checks consent, Phi/coherence, and forbidden metadata. For civic claims, the ten-condition predicate runs against `public_admissible_gbim_mv`.

4. **Verdict is chosen.**
   - PERMIT → record written to `broader_layer_feedback_records` or to `runtime_governance.public_answer_audit`.
   - REVIEW → no write; requires human or higher-level review.
   - SUPPRESS → no write; case is blocked.

5. **Broader layer reads records later.** Retrieval, learning queues, governance dashboards, and the civic claim audit trail treat these records as **inputs**, not commands.

For operators, the civic claim audit trail is the most directly inspectable feedback path. You can query `runtime_governance.public_answer_audit` at any time to see which claims were made, what evidence backed them, and what the admissibility state of the system was at the moment each claim was produced. That is the feedback mechanism from the civic layer back into governance — durable, structured, and always available without rerunning any query.

---

## 24.12 Closing Statement

Feedback into broader layers in Ms. Allis is implemented as **small, governed records**, not as free-flowing self-rewrites. Only approved, consent-respecting, provenance-bearing signals are written into Chroma collections for retrieval biasing, learning gaps, governance reviews, or similar tasks.

The table `runtime_governance.public_answer_audit` is the durable audit trail for civic claim feedback. Every invocation of `runtime_governance.public_answer_packet` writes a row to this table, recording the query, the evidence, and the admissibility summary at the moment the claim was produced. That row is the system's commitment that the claim was governed — that it carried spatial, temporal, and provenance anchors, or that it refused to answer rather than guess.

By suppressing raw transcripts, binding actions, and low-Phi projections, and by logging every civic claim invocation to a persistent audit table, Chapter 24 keeps the feedback path accountable to the same safeguards that govern everything else in the system — so local reasoning can inform the whole without quietly taking it over.

---

*Chapter 24 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
