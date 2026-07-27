# 20. First-Stage Evaluation

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: July 27, 2026*

---

## 20.1 Why This Matters for Polymathmatic Geography

This chapter explains the first-stage evaluation framework used by Ms. Allis to determine whether a candidate reasoning packet or a governed data record is fit to move beyond provisional internal handling. It matters because the system must not leap from retrieval, synthesis, or sandbox reasoning directly into memory, policy, or outward consequence.

It supports:

- **P3 – Power has a geometry** by making evaluation a visible gate between candidate reasoning and consequence.
- **P5 – Design is a geographic act** by treating evaluation rules as part of the architecture that shapes how place-aware reasoning becomes durable action.
- **P12 – Intelligence with a ZIP code** by requiring that local evidence, routing discipline, and policy checks be present before a packet is treated as ready.
- **P16 – Power accountable to place** by ensuring that candidate packets are scored, checked, and either held, emitted, or promoted under explicit governance rather than hidden model confidence.

This chapter belongs to the **Computational Instrument** tier. It describes first-stage evaluation as an implemented governance step for both candidate cognition packets and governed GBIM records, not as a metaphor or purely theoretical abstraction.

As of the July 26, 2026 architecture closeout, the first-stage admissibility standard for governed data records was formalized as a ten-condition predicate enforced by the `public_admissible_gbim` view and the `gbim_record_spacetime_provenance_chk` CHECK constraint. Any section of this chapter listing evaluation conditions for governed records uses that exact ten-condition list.

---

## 20.2 Gate-Constrained Scope

The academic scope of this chapter is intentionally narrow.

This chapter may claim that:

- candidate cognition packets are staged before evaluation;
- first-stage evaluation inspects structured packet fields;
- evaluation returns explicit status, error, warning, and readiness information;
- approved packets may proceed to governed emission and later promotion;
- unapproved packets remain staged, are suppressed, or do not move forward;
- governed GBIM data records must satisfy the ten-condition admissibility predicate before they may enter the public evidence surface.

This chapter may **not** claim that:

- first-stage evaluation proves truth in an absolute sense;
- evaluation creates private thought, consciousness, or autonomous authority;
- a packet becomes durable memory or external authority merely because it was evaluated;
- readiness scores are equivalent to correctness, legality, or moral legitimacy;
- passing the ten-condition predicate guarantees factual accuracy of the underlying record.

Under this gate, first-stage evaluation is documented as a bounded operational review stage. It is an implemented governance filter, not a final arbiter of truth or personhood.

---

## 20.3 Two Kinds of First-Stage Evaluation

First-stage evaluation in this system refers to two related but distinct governance steps that share the same underlying philosophy.

**Kind 1 — Cognition packet evaluation.** A candidate reasoning packet is staged, then reviewed for structural integrity, coherence, routing alignment, policy state, and readiness before it may be emitted or promoted. This is described in §§20.4–20.11.

**Kind 2 — Governed data record admissibility.** A record in `public.gbim_record` must satisfy ten explicit conditions before it may enter the public evidence surface `public_admissible_gbim_mv` and back a public civic claim. This is described in §§20.12–20.15.

Both kinds follow the same governance pattern: create a candidate, hold it in a staged or bounded tier, evaluate it under explicit rules, and promote it only if later gates permit. Rural developers can treat them as two applications of one principle.

---

## 20.4 What First-Stage Evaluation Is (Cognition Packets)

First-stage evaluation of a cognition packet is the first formal review step applied to a staged cognition packet.

In plain language, it answers a practical question:

**"Is this packet structured, governed, and coherent enough to continue?"**

That means first-stage evaluation checks whether a staged packet has enough integrity to move from provisional internal handling toward later governed uses such as emitted packet formation or promotion into a temporal tier.

For rural developers, the easiest way to understand it is this:

1. A request or internal trigger produces a candidate packet.
2. That packet is staged, not yet trusted.
3. First-stage evaluation reviews it under known rules.
4. Only then can it move to the next governed step.

The first-stage evaluator is not "the mind" of the system. It is the first gatekeeper for candidate reasoning products.

---

## 20.5 The Packet That Gets Evaluated

First-stage evaluation does not inspect a vague cloud of reasoning. It evaluates a **staged cognition packet**.

That staged packet is built from structured fields such as:

- request context;
- intent assessment;
- cognitive stage summaries;
- retrieval evidence;
- spatial or temporal context where relevant;
- routing decisions;
- risk and policy state;
- identity mode;
- optional metadata.

This matters because evaluation is not supposed to judge only a final answer string. It is supposed to judge the packet as a governed object with traceable structure.

For rural developers, that means the system is easier to inspect and debug. Instead of asking "Why did the model say that?", the operator can ask:

- What context was staged?
- What service was selected?
- What evidence was included?
- What policy state was attached?
- What identity mode was active?

That is a better engineering surface than opaque chat output.

---

## 20.6 Step-by-Step Lifecycle (Cognition Packets)

The first-stage evaluation framework should be understood as part of a larger governed packet lifecycle.

### Step 1: Stage the packet

A candidate cognition packet is first sent into the cognition sandbox and staged. At this moment it is not yet approved, emitted, or promoted. It is simply held as a candidate object for review.

### Step 2: Assign packet identity

The staging service returns a system-generated packet identifier. This matters because later evaluation does not operate only on the interaction identifier. It operates on the specific staged packet that the sandbox created.

### Step 3: Evaluate the staged packet

The evaluator receives the interaction identifier and the packet identifier and checks the staged packet for readiness, warnings, errors, and approval status.

### Step 4: Decide whether it may proceed

If the packet is approved, it can move to governed emission. If it is not approved, it stays out of downstream promotion paths.

### Step 5: Emit a governed packet

An approved packet may then be emitted as a governed `llm_packet`, which packages the selected reasoning context, policy state, routing rationale, and evidence in a controlled form.

### Step 6: Promote only after approval

Only after the packet has passed first-stage evaluation and later governed steps may it be promoted to a higher tier such as historical memory.

For rural developers, the key lesson is simple: **stage first, evaluate second, emit third, promote last.** Skipping that order is out of scope for the architecture described here.

---

## 20.7 What the Evaluator Returns (Cognition Packets)

The first-stage evaluator returns a structured result rather than a vague pass/fail impression.

A typical first-stage evaluation result includes:

- the packet identifier;
- the interaction identifier;
- a status such as `approved`;
- a list of errors;
- a list of warnings;
- a readiness score;
- a deduplicated evidence count;
- an evaluation timestamp.

For rural developers, each field has a plain meaning:

- **status** tells whether the packet may proceed;
- **errors** describe blocking problems;
- **warnings** describe non-blocking concerns;
- **readiness score** expresses overall preparedness for the next governed step;
- **deduplicated evidence count** tells how much distinct evidence survived review rather than being counted twice.

This design helps administrators explain what happened without claiming the evaluator is infallible.

---

## 20.8 What "Approved" Means

An approved first-stage packet is not the same thing as a final truth claim.

"Approved" means the packet has passed the first governance check strongly enough to continue through the controlled pipeline. It does **not** mean:

- the packet is permanently admitted to memory;
- the packet is publicly authorized;
- the packet is beyond constitutional review;
- the packet is beyond later bridge, temporal, or promotion checks.

For rural developers, "approved" should be read as:

**"This packet is fit to go to the next controlled step."**

That is all. It is an operational verdict, not a metaphysical one.

---

## 20.9 Relationship to Emission and Promotion (Cognition Packets)

Once a packet has passed first-stage evaluation, it may be emitted as a governed packet.

Emission transforms the staged and evaluated candidate into a structured packet that downstream services can consume without re-reading a raw, unstable reasoning trace. The emitted packet may include:

- interaction identifier;
- user identifier;
- original message;
- intent assessment;
- identity mode;
- risk and policy state;
- routing decisions;
- stage summaries;
- retrieval evidence;
- packet readiness score;
- an `emit_ready` flag.

A packet may be:

- staged but not yet evaluated;
- evaluated but not yet emitted;
- emitted but not yet promoted;
- promoted only after the preceding conditions are met.

For rural developers, that separation prevents a common systems mistake: assuming that because a candidate looks good, it should be written directly into durable state. In this architecture, durable change requires more than "it looked good once."

---

## 20.10 The Ten-Condition Admissibility Predicate (Governed Data Records)

The second kind of first-stage evaluation applies to records in `public.gbim_record`. A record is *publicly admissible* — meaning it may enter the public evidence surface and back a civic claim — if and only if all ten of the following conditions hold simultaneously.

This list was formalized on July 26, 2026 as the `public_admissible_gbim` view predicate and enforced by the `gbim_record_spacetime_provenance_chk` CHECK constraint. Any prior version of this chapter listing fewer than ten conditions should be read as superseded by this list.

| Condition | Column | What it enforces |
|---|---|---|
| C1 | `gbim_id IS NOT NULL` | Record identity — every admissible record must have a non-null primary key. |
| C2 | `promotion_state = 'authorized'` | Authorization — the record has passed the GBIM promotion gate. |
| C3 | `public_claim_allowed = true` | Explicit public flag — separately set from authorization; both must be true. |
| C4 | `under_whose_authority IS NOT NULL` | Legal provenance — the authorizing body must be named. |
| C5 | `company_name IS NOT NULL` | Organizational provenance — the originating organization must be named. |
| C6 | `ingested_at IS NOT NULL` | Ingestion timestamp — the moment of record acceptance must be documented. |
| C7 | `degradation_status IN ('fresh', 'aging')` | Lifecycle state — stale records are excluded even if authorized. |
| C8 | `spatial_unit_id IS NOT NULL` | Spatial anchor — added July 26, 2026; no record admitted without its geographic unit. |
| C9 | `spatial_unit_kind IS NOT NULL` | Spatial resolution — blockgroup, tract, county, or equivalent must be specified. |
| C10 | `valid_time_start IS NOT NULL` | Temporal anchor — added July 26, 2026; earliest moment of validity must be specified. |

The predicate is a **conjunction**: any single false condition renders the entire record inadmissible regardless of the status of the remaining nine conditions.

Conditions C1 through C7 were present before July 26, 2026. Conditions C8, C9, and C10 were added on July 26, 2026, closing the spatial and temporal halves of the Spacetime Contract. The admissibility predicate was verified against 237,655 rows without error; 93,423 rows satisfied all ten conditions and entered the public evidence surface.

### Implementation in SQL

The predicate is directly instantiated as the `WHERE` clause of `public.public_admissible_gbim`:

```sql
CREATE VIEW public.public_admissible_gbim AS
SELECT g.*
FROM public.gbim_record g
WHERE g.gbim_id IS NOT NULL                         -- C1
  AND g.promotion_state = 'authorized'             -- C2
  AND g.public_claim_allowed = true                -- C3
  AND g.under_whose_authority IS NOT NULL          -- C4
  AND g.company_name IS NOT NULL                   -- C5
  AND g.ingested_at IS NOT NULL                    -- C6
  AND g.degradation_status IN ('fresh','aging')    -- C7
  AND g.spatial_unit_id IS NOT NULL                -- C8
  AND g.spatial_unit_kind IS NOT NULL              -- C9
  AND g.valid_time_start IS NOT NULL;              -- C10
```

`public.public_admissible_gbim_mv` is the materialized version, refreshed by `runtime_governance.refresh_public_admissible_gbim_mv()`.

---

## 20.11 What the Ten Conditions Mean for Rural Developers

Each condition in the ten-condition predicate has a plain operational meaning that matters to rural developers working with or extending this system.

**C1 — gbim_id IS NOT NULL.** Every record the system will speak publicly must have a unique, non-null identifier. If the primary key is missing, the record does not exist in a governable sense.

**C2 — promotion_state = 'authorized'.** The record has been reviewed and formally authorized through the GBIM promotion gate. A record can be stored without being authorized; stored is not the same as speakable.

**C3 — public_claim_allowed = true.** Authorization alone is not enough. There is a separate, affirmative flag that must be set before a record may back a public claim. This two-step requirement prevents accidental public disclosure of records that were authorized for internal use only.

**C4 — under_whose_authority IS NOT NULL.** The system must name who authorized the record. Anonymous authority is not governance.

**C5 — company_name IS NOT NULL.** The originating organization must be named. This is the organizational accountability anchor.

**C6 — ingested_at IS NOT NULL.** The system must record when the data entered the governed store. Without an ingestion timestamp, the provenance chain is incomplete.

**C7 — degradation_status IN ('fresh', 'aging').** Records have a lifecycle. A record that has gone stale is excluded from public claims even if it remains authorized. This prevents the system from citing outdated data as current evidence.

**C8 — spatial_unit_id IS NOT NULL.** The geographic unit the record describes must be identified by its normalized key (for example, a Census blockgroup GEOID). A record without a spatial anchor cannot answer *where*.

**C9 — spatial_unit_kind IS NOT NULL.** The resolution of the spatial unit — whether it is a blockgroup, tract, county, or equivalent — must be stated. This prevents ambiguity about what geographic level the record describes.

**C10 — valid_time_start IS NOT NULL.** The earliest moment for which the record's metric claim is valid must be stated. A record without a temporal anchor cannot answer *when*.

The three conditions added July 26, 2026 — C8, C9, and C10 — close the spatial and temporal halves of the Spacetime Contract. Before that date, a record could be authorized for public claims without specifying *where exactly* or *as of when*. That gap is now closed at the schema level.

---

## 20.12 The Separation of Stored from Speakable

A key consequence of the ten-condition predicate is that the system maintains a strict boundary between records it stores and records it will speak publicly.

**Stored state** is everything in `public.gbim_record`. The governance runtime has full access to all stored records, including those that fail one or more of the ten conditions. This broad access is intentional: governance requires visibility into inadmissible records to understand why they are inadmissible, to backfill missing fields, and to promote or demote records over time.

**Speakable state** is only what passes all ten conditions and appears in `public_admissible_gbim_mv`. The public instrument role can only read from this materialized view. A direct `SELECT` on `public.gbim_record` returns `permission denied` for the public role.

At the July 26, 2026 gate:

| Measure | Count |
|---|---|
| Total authorized rows | 237,655 |
| Admissible for public claims (all ten conditions) | 93,423 |
| Stored but inadmissible | 144,232 |

The 144,232 inadmissible rows are not errors. They represent records held in the governed store that do not yet meet all ten conditions. The system stores them; it does not speak them.

---

## 20.13 Step-by-Step Guide for Rural Developers (Both Kinds)

A rural developer can work with first-stage evaluation using the following sequences.

### For cognition packet evaluation:

1. Gather the request context, evidence, intent, routing information, and risk state that belong in the staged packet.
2. Send the full candidate packet to the staging endpoint; record the returned packet identifier.
3. Do not substitute the interaction identifier for the packet identifier.
4. Submit the interaction identifier and the staged packet identifier to the evaluation step.
5. Read status, errors, warnings, readiness score, and evidence count before moving any further.
6. Proceed only if the packet is approved; otherwise hold it outside downstream authority paths.
7. Emit the governed packet only after approval.
8. Promote only under later gates — promotion belongs to later governance, memory, and temporal tiers.

### For governed data record admissibility:

1. Identify the record in `public.gbim_record` that is intended for public use.
2. Confirm that all ten conditions in §20.10 are satisfied — run a query against `public.public_admissible_gbim` and verify the record appears.
3. If any condition fails, determine which field is missing or incorrect: check `promotion_state`, `public_claim_allowed`, `under_whose_authority`, `company_name`, `ingested_at`, `degradation_status`, `spatial_unit_id`, `spatial_unit_kind`, and `valid_time_start` in sequence.
4. Backfill or correct the failing field through the appropriate governance path — do not bypass the predicate by direct write.
5. Re-run the admissibility check after backfilling to confirm the record now appears in `public_admissible_gbim`.
6. Refresh the materialized view `public_admissible_gbim_mv` by calling `runtime_governance.refresh_public_admissible_gbim_mv()`.
7. Verify the updated count in `runtime_governance.public_answer_audit` before allowing any downstream system to cite the record as public evidence.

In both cases, the same principle applies: evaluate explicitly, do not assume, and hold anything that fails any single condition until the failure is corrected.

---

## 20.14 Relationship to Other Governed Candidate Systems

First-stage evaluation belongs to a broader family of governed candidate workflows inside Ms. Allis.

Other governed candidate flows include:

- spatial candidate staging and evaluation;
- temporal staged tiers prior to historical admission;
- per-user staged conversational memory;
- governed feedback and external communication candidates;
- GBIM record admissibility through the ten-condition predicate.

The common pattern is consistent:

- create a candidate;
- hold it in a staged or bounded tier;
- evaluate it under explicit rules;
- promote it only if later gates permit.

This pattern matters academically because it shows that first-stage evaluation is not an isolated trick. It is one expression of a broader architecture in which provisional states are deliberately separated from authoritative ones. Rural developers who understand this pattern in the cognition-packet context will recognize it immediately in the GBIM admissibility context, and vice versa.

---

## 20.15 Metrics and Audit Meaning

The first-stage framework includes metrics because operators need more than narrative description.

For cognition packet evaluation, relevant metrics include:

- whether a packet was approved;
- readiness score;
- number of warnings and errors;
- number of deduplicated evidence items;
- evaluation timestamps;
- whether emission and promotion occurred afterward.

For governed data record admissibility, relevant metrics include:

- count of records satisfying all ten conditions (`admissible_public` in the lifecycle snapshot);
- count of authorized records that do not satisfy all ten conditions (`inadmissible_public`);
- which specific condition is most commonly the blocking factor;
- lifecycle snapshot timestamps in `runtime_governance.public_answer_audit`.

These metrics make both evaluation paths auditable. They help operators detect weak evidence, missing spatial or temporal anchors, and premature promotion attempts. They provide a stable record for later system validation.

---

## 20.16 Distinguishing Evaluation from Truth, Memory, and Action

First-stage evaluation must be kept distinct from three other things.

**Evaluation is not truth.** The evaluator checks structure, readiness, and governed fit. It does not guarantee absolute correctness of the underlying data.

**Evaluation is not memory.** A packet can be evaluated — or a record can pass the ten conditions — and still never become durable memory or a permanent public fact. Promotion rules, temporal tiers, retention conditions, and consent rules still apply.

**Evaluation is not action.** An evaluated packet or admissible record does not automatically create public communication, legal commitment, or civic action. External communication and binding acts require additional gates.

For rural developers, this distinction protects against overreach. It keeps the system from treating a well-formed packet or a ten-condition-passing record as though it were automatically a fact, a memory, or a decision.

---

## 20.17 Limits of the Chapter

This chapter stays within strict academic and implementation limits.

It does not claim that:

- readiness scores are consciousness scores;
- evaluation proves the ontology of mind;
- packet approval overrides constitutional or legal review;
- first-stage evaluation alone authorizes publication, retention, or action;
- the cognition sandbox is a self-governing intelligence;
- passing the ten-condition predicate guarantees the factual accuracy or legal authority of the underlying data record.

Instead, the chapter documents two limited and concrete facts:

1. Ms. Allis uses a governed first-stage evaluation step to review staged cognition packets before they may proceed to emitted or promoted forms.

2. Ms. Allis uses a ten-condition admissibility predicate — enforced structurally as of July 26, 2026 — to determine which governed data records may enter the public evidence surface and back a civic claim.

Both claims are appropriately bounded, technically meaningful, and operationally useful.

---

## 20.18 Closing Statement

First-stage evaluation is the first formal governance step for candidate cognition packets and governed data records in Ms. Allis. It stands between staged reasoning and downstream consequence, checking whether a packet or record is sufficiently structured, governed, and policy-aligned to continue.

For governed data records, that standard was formalized on July 26, 2026 as the ten-condition admissibility predicate: `gbim_id`, `promotion_state`, `public_claim_allowed`, `under_whose_authority`, `company_name`, `ingested_at`, `degradation_status IN ('fresh', 'aging')`, `spatial_unit_id`, `spatial_unit_kind`, and `valid_time_start`. All ten conditions must hold simultaneously. Any single failure closes the gate.

For rural developers, the lesson is practical and direct: do not trust candidate reasoning or governed data merely because it exists. Stage it, evaluate it against the explicit conditions, read the returned fields, and only then allow it to move forward under the next gates. In this architecture, first-stage evaluation is the first visible proof that reasoning and data have entered governance rather than bypassed it.

---

*Chapter 20 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
