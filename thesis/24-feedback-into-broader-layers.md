# 24. Feedback into Broader Layers

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 22, 2026*

---

## 24.1 Why This Matters for Polymathmatic Geography

This chapter explains how Ms. Allis sends **feedback signals** into broader layers of the system without letting raw sandbox output rewrite memory, governance, or commons directly. It shows how feedback is bounded, consent‑gated, and provenance‑bearing.

It supports:

- **P1 – Every where is entangled** by letting local observations influence retrieval, learning, and governance, but only through explicit records.  
- **P3 – Power has a geometry** by treating upward feedback as movement across authority layers, not as a free write.  
- **P5 – Design is a geographic act** by making feedback routing part of the system’s map: which signals may travel where, and under what rules.  
- **P12 – Intelligence with a ZIP code** by letting place‑ and people‑specific gaps or patterns nudge broader behavior without leaking raw transcripts.  
- **P16 – Power accountable to place** by logging feedback into auditable collections instead of silently changing behavior.

This chapter belongs to the **Computational Instrument** tier. It documents feedback as built: **records written into governed stores**, not ad‑hoc self‑modification.

---

## 24.2 What Counts as Feedback Into Broader Layers

“Feedback into broader layers” means **writing small, structured records** that other subsystems can read later. These records never contain raw transcripts or unreviewed sandbox traces.

Allowed **source types** for feedback include:

- retained conversation summaries (already approved and retention‑eligible);  
- background patterns that passed Chapter 21 rules;  
- automated learning gaps (for example, “system is weak on X”);  
- continuous validation results (for example, “Phi/coherence degraded here”);  
- DGM cycle outcomes;  
- PIA reviews;  
- commons governance records (for example, decisions about what belongs in commons).

Allowed **target layers** include:

- retrieval bias hints;  
- background pattern updates;  
- automated learning gap queues;  
- WOAH (optimization) hints;  
- pituitary (global mode) hints;  
- governance review queues;  
- continuous validation watch lists.

Each feedback record is:

- **bounded** – small, focused, and scoped;  
- **consent‑gated** – respecting user retention settings;  
- **provenance‑bearing** – with a hash or pointer to its source;  
- **auditable** – stored in a Chroma collection such as `broader_layer_feedback_records`.

---

## 24.3 How Feedback Records Are Structured

Every feedback record has a compact structure, for example:

```markdown
- source_type        # e.g., retained_conversation, background_pattern, automated_learning_gap
- source_id          # identifier within that source
- target_layer       # e.g., retrieval_bias, automated_learning_gap_queue, governance_review
- request_purpose    # almost always “governance” or a similarly bounded purpose
- actor_role         # typically “system” for internal feedback
- retention_consent  # true/false
- phi_floor_met      # true/false (coherence/health check)
- provenance_hash    # hash linking back to evidentiary context
- human_review_required  # true/false
```

The gate you ran shows concrete examples, such as:

- a **valid** record where a background pattern gently biases retrieval;  
- a **learning_gap** record where a recognized gap is sent to an automated learning queue.

Only records that pass all checks are written to the feedback collection.

---

## 24.4 Consent and Raw-Data Suppression

Two hard suppression rules govern feedback:

1. **No consent → no feedback write.**  
   If `retention_consent` is false for a `retained_conversation` source, the verdict is **SUPPRESS** and the record is not written, even if everything else is valid.

2. **Raw transcript or forbidden metadata → SUPPRESS.**  
   If the projection attempts to include raw transcripts, private identity data, or forbidden fields (for example, `raw_private_transcript`), the feedback record is suppressed.

In your gate output, you can see:

- a `no_consent` case where feedback from a conversation is suppressed;  
- a `raw_trace` case where a would‑be background pattern record is suppressed because it tried to use raw transcript metadata.

This ensures broader layers see **clean signals**, not copies of user conversations.

---

## 24.5 Phi/Coherence Floors and Review

Feedback records also depend on **system coherence**, via Phi and related measures:

- If `phi_floor_met` is **true**, and other conditions are satisfied, a feedback record can be **PERMIT**ted and written.  
- If `phi_floor_met` is **false**, even with consent and a valid source type, the verdict is **REVIEW**, and no direct write occurs.

In your probe, the `low_phi` case shows:

- source_type: `continuous_validation`;  
- target_layer: `continuous_validation_watch`;  
- `phi_floor_met: false`;  
- verdict: **REVIEW**.

This means: “The system noticed a coherence problem. Instead of automatically pushing this into the watch list, it flags it for review.”

---

## 24.6 Examples of Permitted Feedback

The gate shows two concrete permitted examples:

1. **Background pattern → retrieval bias.**  
   - `source_type`: `background_pattern`  
   - `target_layer`: `retrieval_bias`  
   - `verdict`: **PERMIT**  
   - Written as `fb24_3169…` into `broader_layer_feedback_records`.

   This lets a vetted background pattern slightly influence which documents are retrieved, without exposing raw data.

2. **Automated learning gap → learning gap queue.**  
   - `source_type`: `automated_learning_gap`  
   - `target_layer`: `automated_learning_gap_queue`  
   - `verdict`: **PERMIT**  
   - Written as `fb24_b0f11…` into `broader_layer_feedback_records`.

   This lets the system remember, “I struggled with this topic; please schedule a learning task later,” without altering the core models directly.

In both cases:

- consent is true;  
- Phi floor is met;  
- forbidden metadata is absent;  
- provenance is recorded.

---

## 24.7 Examples of Suppressed Feedback

The same contract also shows what **may not** be written:

- **Binding legal action.**  
  A projection with source_type `commons_governance_record` and target_layer `governance_review` is blocked when it carries `binding_legal_action` metadata. Verdict: **SUPPRESS**.

- **No retention consent.**  
  A `retained_conversation` projection targeting `background_pattern` is suppressed when `retention_consent` is false.

- **Raw transcript.**  
  Any projection marked with forbidden `raw_transcript` or similar metadata is suppressed.

These examples enforce the gate’s scope:

- no binding legal action;  
- no clinical diagnosis;  
- no financial instruction;  
- no unreviewed self‑modification;  
- no raw trace propagation.

---

## 24.8 Allowed vs Blocked Flows (Table)

| Source type              | Target layer                     | Status    | Reason                                   |
|--------------------------|----------------------------------|----------:|------------------------------------------|
| background_pattern       | retrieval_bias                   | PERMIT    | bounded feedback record permitted        |
| automated_learning_gap   | automated_learning_gap_queue     | PERMIT    | bounded feedback record permitted        |
| continuous_validation    | continuous_validation_watch      | REVIEW    | Phi floor not met → review               |
| retained_conversation    | background_pattern (no consent)  | SUPPRESS  | retention consent required               |
| retained_conversation    | background_pattern (raw_trace)   | SUPPRESS  | forbidden metadata: raw_transcript       |
| commons_governance_record| governance_review (binding)      | SUPPRESS  | forbidden metadata: binding_legal_action |

This table is the “wiring diagram” for Chapter 24.

---

## 24.9 What Chapter 24 Does Not Claim

Within this gate, Chapter 24 does **not** claim:

- automatic or unconstrained self‑modification;  
- direct propagation of raw sandbox traces into broader layers;  
- binding legal actions;  
- clinical diagnosis or therapeutic decisions;  
- financial instructions;  
- guaranteed safety.

Instead, it claims:

- **bounded feedback records** with consent and provenance;  
- **suppression** when consent, Phi, or metadata rules fail;  
- **review** when coherence is low or stakes are high.

Broader layers see **small, structured hints**, not uncontrolled writes.

---

## 24.10 Step-by-Step View for Rural Developers

On a running system, feedback into broader layers behaves like this:

1. **Some event happens.**  
   For example, a DGM cycle finds a gap, or a background pattern is updated.

2. **A projection is built.**  
   A small record is drafted with `source_type`, `source_id`, `target_layer`, `provenance_hash`, and flags.

3. **Contract rules run.**  
   The system checks consent, Phi/coherence, and forbidden metadata.

4. **Verdict is chosen.**  
   - PERMIT → record written to `broader_layer_feedback_records`.  
   - REVIEW → no write; requires human or higher‑level review.  
   - SUPPRESS → no write; case is blocked.

5. **Broader layer reads records later.**  
   Retrieval, learning queues, or governance dashboards treat these records as **inputs**, not commands.

For you as an operator, the important point is: you can inspect the feedback collection and see exactly what kinds of hints the system is using to adjust itself.

---

## 24.11 Closing Statement

Feedback into broader layers in Ms. Allis is implemented as **small, governed records**, not as free‑flowing self‑rewrites. Only approved, consent‑respecting, provenance‑bearing signals are written into Chroma collections for retrieval biasing, learning gaps, governance reviews, or similar tasks.

By suppressing raw transcripts, binding actions, and low‑Phi projections, Chapter 24 keeps the feedback path accountable to the same safeguards that govern everything else in the system—so local reasoning can inform the whole without quietly taking it over.
