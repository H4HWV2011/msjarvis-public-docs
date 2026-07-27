# 21. Background Store and Patterns

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: July 27, 2026*

---

## 21.1 Why This Matters for Polymathmatic Geography

This chapter explains how Ms. Allis keeps **background understanding** without sliding into surveillance, unlimited memory, or raw transcript hoarding. It shows how recurring patterns are formed only after passing through gates, not directly from whatever the system happened to "think." It also explains how the background store connects to the governed data layer: the 144,232 rows held internally in `public.gbim_record` as of the July 26, 2026 lifecycle snapshot are the concrete, operational example of this principle at the data layer — real records kept for governance but not yet speakable publicly.

It supports:

- **P1 – Every where is entangled** by letting patterns emerge across conversations, geography, and governance, while still respecting strict retention rules.
- **P3 – Power has a geometry** by placing pattern formation downstream of BBB, guardian, and retention gates rather than inside raw sandbox traces.
- **P5 – Design is a geographic act** by making decisions about "what may become a pattern" part of system design, not an accident of logging.
- **P12 – Intelligence with a ZIP code** by allowing place-aware regularities to persist only when they have crossed the right consent and retention paths.
- **P16 – Power accountable to place** by requiring patterns to carry provenance and consent, so their lineage can be inspected later.

This chapter belongs to the **Computational Instrument** tier. It describes the as-built background store and pattern system, not an unlimited or automatic memory.

---

## 21.2 Background Store Role

The background store is where Ms. Allis keeps **summaries and regularities**, not raw conversations.

Its job is to:

- hold **bounded pattern summaries** that help future reasoning;
- keep those summaries tied to **consent, provenance, and retention rules**;
- stay separate from internal working notes and raw transcripts.

You can think of it as a small notebook of "things Ms. Allis is allowed to remember in general," built only from content that already passed through gates and retention checks.

At the governed data layer, this same principle applies directly to `public.gbim_record`. Every row in that table is part of the background store: it is held for governance, lifecycle management, backfill, and promotion review. Not every row is speakable. The ones that are not yet speakable are the operational background — real, valued data that the governance runtime needs but that has not yet earned the right to back a public claim.

---

## 21.3 The Concrete Illustration: 144,232 Stored-but-Inadmissible Rows

The July 26, 2026 lifecycle snapshot — recorded in `runtime_governance.public_answer_audit` as the `lifecycle_snapshot` audit entry — produced the following counts:

| Measure | Count | Source |
|---|---|---|
| Total authorized rows in `public.gbim_record` | 237,655 | Lifecycle snapshot, July 26, 2026 |
| Admissible for public claims (all ten conditions) | 93,423 | Lifecycle snapshot, July 26, 2026 |
| Stored but inadmissible | 144,232 | Lifecycle snapshot, July 26, 2026 |

The 144,232 stored-but-inadmissible rows are the background store in concrete form. These are not errors, corrupt data, or records scheduled for deletion. They are real governed records that the system holds internally — authorized, provenanced, and maintained — but that do not yet satisfy all ten conditions of the public admissibility predicate.

Common reasons a row is in this category include:

- `public_claim_allowed` has not yet been affirmatively set to `true`, even though `promotion_state = 'authorized'`;
- `spatial_unit_id`, `spatial_unit_kind`, or `valid_time_start` has not yet been backfilled, meaning the record predates the July 26, 2026 Spacetime Contract columns;
- `degradation_status` has moved to `'stale'`, excluding the record from the current public surface even though it was previously admissible.

For rural developers, the lesson is direct: **the background store is real data doing real governance work.** The 144,232 rows are the proof. They are not a gap or a failure — they represent the system's honest accounting of what it holds versus what it will speak. The governance runtime (`runtime_governance_role`) can read and maintain all 237,655 rows. The public instrument (`public_instrument_role`) can only read the 93,423 that pass all ten conditions.

This stored/speakable boundary is the defining structural property of the background store.

---

## 21.4 Separation from Raw Transcripts and Profiling

Several kinds of data are **explicitly not** stored as background patterns:

- full raw chat transcripts by default;
- detailed identity metadata such as exact names, addresses, or identifiers that could rebuild a person's dossier;
- per-user psychological profiles built automatically from behavior.

Instead:

- only **pattern summaries** are eligible (for example, "this user prefers step-by-step explanations");
- those summaries must respect **retention consent** and **provenance requirements**;
- identity-heavy details are suppressed or anonymized before anything can become background.

This keeps the system from turning everyday use into a hidden profile or an unlimited recall of past conversations. The governed data layer applies the same principle differently: the 144,232 inadmissible rows are held for governance, not for profiling, and the governance runtime's access to them is bounded by the role structure described in Chapter 20.

---

## 21.5 Consent, Provenance, and Commons Eligibility

The system distinguishes between three ideas that sound similar but are very different in practice:

- **Background retention.** Whether a pattern summary may be kept for future use in this environment at all.
- **Per-user people-space memory.** Consent-gated, deletable per-user memories that never become general background unless explicitly allowed.
- **Commons eligibility.** Whether a pattern or artifact may be turned into a public "commons" resource, which requires **a separate, explicit opt-in.**

For a pattern to enter the background store, it must:

1. Come from **approved, gated outcomes** — not from a raw working note or provisional reasoning trace.
2. Respect the user's retention and deletion settings.
3. Carry enough **provenance** to explain what it came from.
4. Stay **separate from commons** unless there is a clear public-opt-in path.

Background storage is therefore **opt-in and bounded**, not automatic and unlimited.

For governed data records, provenance is enforced structurally: `under_whose_authority` and `company_name` are required fields in the ten-condition admissibility predicate. A record without a named authorizing body and a named originating organization cannot become publicly speakable — it remains in the background store until those fields are populated and verified.

---

## 21.6 Memory Families You Can See at Runtime

The background design uses several **runtime-visible memory families**:

- **Conversation collections** — per-session or per-thread traces that support short-term continuity.
- **People-space collections** — per-user memory areas, consent-controlled and prunable.
- **Commons collections** — publicly shareable patterns or resources, populated only with explicit consent and curation.
- **Background pattern collections** — bounded summaries that help with regularities like "this community cares about emergency resources first" or "rural users often have poor connectivity."
- **Governed data background store** — the full `public.gbim_record` table, including the 144,232 stored-but-inadmissible rows, maintained by the governance runtime for lifecycle management, backfill, promotion review, and degradation tracking.

All of these families are visible as **separate collections or tables** in the backing stores. System operators can inspect which family a given summary or record lives in and what rules apply to it.

---

## 21.7 How Patterns Are Formed (High Level)

A background pattern is not a copy of a conversation. It is a **small summary** extracted from content that already cleared the relevant gates.

The pipeline looks like this:

1. A conversation or reasoning episode produces a **promoted conclusion** (for example, "this user prefers code with comments").
2. That conclusion passes BBB, guardian, and retention checks.
3. A summarizer creates a **compact pattern** from it (for example, "preference: explained steps").
4. The pattern is stored in the appropriate collection, with **provenance links** back to its source.
5. Later, Ms. Allis may consult that pattern to shape responses, always subject to updated consent and deletion.

If consent is revoked or a user requests deletion, entries in the relevant people-space or background collections are removed or pruned, and future patterns must be rebuilt from remaining data.

The governed data layer follows the same sequence in a different register: a raw data record enters `public.gbim_record`, passes through the promotion gate to `authorization_state = 'authorized'`, is evaluated against the ten-condition admissibility predicate, and only then may back a public claim. The 144,232 stored-but-inadmissible rows are at various stages of that journey — held, valid, and maintained, but not yet at the end of it.

---

## 21.8 What Background Patterns Are *Not*

Within this gate, background patterns must **not** be described as:

- unlimited memory of everything ever said;
- automatic psychological profiles;
- raw transcript storage;
- automatic "commons" publication of user content;
- clinical or legal guarantees.

Instead, patterns are:

- bounded summaries;
- consent-gated;
- provenance-carrying;
- distinct from transcripts and logs;
- subject to deletion and pruning.

The 144,232 stored-but-inadmissible rows are the data-layer analogue of this discipline. They are not publicly accessible, not cited in answers, and not treated as authoritative public evidence. They are held in the background, subject to governance maintenance, and eligible for promotion if and when the remaining admissibility conditions are met.

---

## 21.9 Interaction with BBB, Guardian, Chroma, and Hilbert-State

Several live services back the background store:

- The **BBB** and **constitutional guardian** decide which conclusions are even eligible to become long-term knowledge.
- **Chroma** or equivalent vector stores hold pattern embeddings and collection families.
- **Hilbert-state** services track the system's current state and time frame, allowing pattern evaluation to factor in when and under what conditions a summary was formed.
- **`runtime_governance`** schema functions — including `runtime_governance.refresh_public_admissible_gbim_mv()` and `runtime_governance.log_lifecycle_counts()` — maintain the governed data background store, tracking which rows are admissible, which are not, and why.

For rural developers, the important idea is that **background store management is routed through the same safety, time/state, and governance layers** as other authority-bearing decisions, not left as ad-hoc file writes or unreviewed database inserts.

---

## 21.10 The Lifecycle Snapshot as the Audit Record

The July 26, 2026 lifecycle snapshot is the concrete audit record for the background store at that point in time. It was logged automatically by `runtime_governance.log_lifecycle_counts()` and is readable from `runtime_governance.public_answer_audit`:

```sql
SELECT audit_id, stage, detail, created_at
FROM runtime_governance.public_answer_audit
WHERE stage = 'lifecycle_snapshot'
ORDER BY audit_id DESC
LIMIT 1;
```

The detail field of that record contains:

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

This JSON is the background store's balance sheet at July 26, 2026:

- **237,655** — total authorized records held in the background store.
- **93,423** — records that have crossed from background to speakable by satisfying all ten admissibility conditions.
- **144,232** — records that remain in the background store: real, authorized, maintained, and not yet speakable.

For rural developers, this audit record is how you verify the state of the background store at any point in time. Running `log_lifecycle_counts()` on a schedule (the system does this via pg_cron) means the audit history grows over time, and operators can observe how the 144,232 figure changes as backfill work proceeds and new records are ingested, promoted, or degraded.

---

## 21.11 Practical View for Rural Developers

If you are running Ms. Allis on your own machine, you can think of the background store at two levels.

**At the pattern level:**

- There is a **small shelf** where allowed summaries live.
- Every card on the shelf has: what it says (the pattern), where it came from (provenance), which user or space it belongs to, and whether it is allowed to stay or must be deleted on request.
- You can adjust retention policies, clear people-space and background collections for a user, and review which families are active (conversation, people-space, commons, background).
- You cannot make the system silently keep unlimited transcripts or automatically convert private conversations into commons content.

**At the governed data level:**

- The background store is `public.gbim_record` — all 237,655 authorized rows as of July 26, 2026.
- The speakable surface is `public_admissible_gbim_mv` — the 93,423 rows that pass all ten conditions.
- The background is the difference: 144,232 rows held internally for governance, lifecycle, and backfill.
- You can inspect the background store by querying `public.gbim_record` as `runtime_governance_role`.
- You can inspect the speakable surface by querying `public_admissible_gbim_mv` as `public_instrument_role`.
- You can audit the balance by reading `runtime_governance.public_answer_audit`.

The two levels share one discipline: **what is stored is not automatically what is spoken.** Governance is the gap between them.

---

## 21.12 Limits of the Chapter

This chapter stays within strict academic and implementation limits.

It does not claim that:

- the background store is consciousness or memory in a human sense;
- the 144,232 inadmissible rows are errors or corrupt data;
- stored-but-inadmissible records are permanently excluded from public claims;
- background patterns are equivalent to facts, commitments, or legal records;
- the background store is beyond deletion, pruning, or governance review.

Instead, the chapter documents two bounded and concrete facts:

1. Ms. Allis maintains a background store of pattern summaries drawn from gated, consented, provenanced outcomes — distinct from raw transcripts and automatic profiling.
2. The governed data layer of the background store contained 144,232 stored-but-inadmissible rows as of the July 26, 2026 lifecycle snapshot, representing real authorized records held for governance that have not yet satisfied all ten conditions for public admission.

Both facts are operationally verifiable and appropriately bounded.

---

## 21.13 Closing Statement

Chapter 21 describes a **bounded, consent-gated background store** that holds pattern summaries and governed data records — not raw transcripts, not automatic profiles, not unlimited recall.

The 144,232 stored-but-inadmissible rows from the July 26, 2026 lifecycle snapshot are the system's clearest illustration of this principle in practice. They are real data, held honestly, maintained by the governance runtime, and waiting for the conditions that will allow them to cross from background into the speakable public evidence surface. They are not a gap in the system — they are the system working as designed.

This keeps Ms. Allis's long-term sense of place, community, and evidence useful and trustworthy, while staying accountable to consent, provenance, and the ten-condition admissibility standard rather than quietly speaking everything it holds.

---

*Chapter 21 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
