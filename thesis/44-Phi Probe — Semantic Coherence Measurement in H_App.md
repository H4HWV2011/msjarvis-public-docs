# 44 — Phi Probe — Semantic Coherence Measurement in H_App

*Carrie Kidd (Mamma Kidd) — Mount Hope, West Virginia*  
*Last Updated: July 27, 2026*

---

## 44.1 Purpose of the Phi Probe

This chapter explains how Ms. Jarvis measures the **semantic coherence of governed state** inside H_App using a concrete probe: the fraction of governed records that are admissible for public claims.

The name “Phi probe” here refers to a measurement of how much of the stored governed corpus is ready to be spoken as evidence, not just stored as data. It is a way of asking: “How coherent is our governed state today?” and answering that question with a real number rather than a feeling.

For rural developers, this provides a practical handle on an abstract idea. Instead of saying “the system is pretty coherent,” the system can say “39.3% of governed rows are admissible as of July 26, 2026.”

---

## 44.2 What Semantic Coherence Means Here

Semantic coherence, in the context of H_App, means that a governed record:

- Has all required spatial and temporal anchors.
- Has clear provenance and lifecycle state.
- Satisfies the ten-condition admissibility predicate.
- Is ready to back a public answer without further qualification.

A corpus with high semantic coherence has many records that meet these conditions. A corpus with low coherence has many records that are stored but not yet ready to speak.

The Phi probe is the measurement that tells us where we stand.

---

## 44.3 The Governed Corpus Under Measurement

The corpus under measurement is:

- The set of rows in `public.gbim_record` that represent governed state from the spatial body.
- The admissible subset of those rows in `public.public_admissible_gbim_mv`, defined by the ten-condition predicate described in earlier chapters.

This corpus includes:

- Spatial anchors such as blockgroup GEOIDs.
- Temporal anchors such as `valid_time_start`.
- Provenance fields such as `company_name` and `under_whose_authority`.
- Lifecycle fields such as `degradation_status`.

It is the same corpus from which the overflow proof and public answer paths draw their evidence.

---

## 44.4 Concrete Phi Probe Measurement — July 26, 2026

As of the July 26, 2026 gate, the Phi probe measurement is:

- **Total authorized governed rows:** 237,655.
- **Admissible for public claims (all ten conditions):** 93,423.
- **Admissibility fraction:** approximately 39.3%.

### 44.4.1 How the Fraction Is Computed

The Phi probe fraction is:

\[
\Phi_{\text{admissible}} = \frac{\text{admissible rows}}{\text{total authorized rows}} \approx \frac{93{,}423}{237{,}655} \approx 0.393
\]

Expressed as a percentage, this is about **39.3% admissibility**.

### 44.4.2 What the Numbers Mean

These numbers mean:

- Out of all governed records that have passed authorization, only a subset (93,423) currently satisfy all ten admissibility conditions and are allowed to back public claims.
- The remaining records (144,232) are stored but inadmissible — for example, because they are not yet marked `public_claim_allowed`, or because their lifecycle status is `stale`, or because other conditions are not met.

The Phi probe does not treat inadmissible records as errors. It treats them as part of the stored corpus that is still in motion: records that may be promoted, corrected, or aged out over time.

---

## 44.5 Why Phi Probe Matters for Coherence

### 44.5.1 Coherence as a Ratio, Not a Guess

By defining semantic coherence as a ratio of admissible to total governed records, the system:

- Anchors coherence in the same governed corpus that powers answers and overflow.
- Avoids vague statements like “the system is mostly coherent.”
- Provides a concrete, repeatable measurement that can be compared over time.

For rural developers, this is useful because it turns a high-level concept into something that can be monitored like a gauge.

### 44.5.2 What 39.3% Admissibility Tells Us

A 39.3% admissibility fraction tells us:

- The system is storing more records than it speaks.
- Almost two out of five authorized records are fully admissible.
- The corpus has room to grow in coherence as more records are promoted and lifecycle conditions are met.

This is not a failure. It reflects an intentional design choice: the system stores candidates, partial records, and aging records that are useful internally but not suitable for public claims.

---

## 44.6 Ten-Condition Admissibility and Phi

The Phi probe is tied directly to the ten-condition admissibility predicate defined elsewhere.

### 44.6.1 Conditions Recap

To be admissible, a record must satisfy ten conditions, including:

- Having a non-null `gbim_id`.
- Being in `promotion_state = 'authorized'`.
- Having `public_claim_allowed = true`.
- Having non-null provenance fields (`under_whose_authority`, `company_name`, `ingested_at`).
- Having `degradation_status` in `('fresh', 'aging')`.
- Having non-null `spatial_unit_id`, `spatial_unit_kind`, and `valid_time_start`.

The admissible view filters records according to these conditions. The Phi probe then measures how many authorized records pass the filter.

### 44.6.2 Phi as a Coherence Lens

Because the predicate is strict, Phi serves as a coherence lens:

- When more records meet all ten conditions, Phi increases.
- When records shift into `stale` status or lose public claim flags, Phi decreases.
- When new records are ingested but not yet promoted, they enter the corpus without changing Phi until they pass the predicate.

For rural developers, this means that improving Phi is not about generating more data alone; it is about improving the completeness and lifecycle quality of existing data.

---

## 44.7 Overflow Proof Inside the Governed Corpus

The overflow proof — showing cognition-to-overflow behavior — lives inside the same governed corpus measured by the Phi probe.

### 44.7.1 Overflow Events and Admissible Evidence

Overflow events are constructed from:

- Person-space validation results.
- Minimized public-context fields.
- Governed evidence that passes through admissible surfaces.

These events are not arbitrary logs. They are structured records that rely on the governed state being coherent enough to support safe overflow.

### 44.7.2 Why Coherence Matters for Overflow

If governed state were incoherent:

- Overflow events might carry incomplete or misleading context.
- Person-space validation might be unable to determine whether an event is safe to route.
- Queued events might not map cleanly back to governed evidence.

The Phi probe’s 39.3% admissibility measurement shows that:

- A significant subset of governed records are coherent enough to back both answers and overflow events.
- The overflow proof is grounded in real, admissible data, not just conceptual sketches.

For rural developers, this is a reassurance: the overflow mechanisms are not attached to a random or broken corpus; they attach to a corpus with measurable coherence.

---

## 44.8 Using Phi Probe Over Time

The Phi probe is not a one-time measurement. It is designed to be rerun as the system evolves.

### 44.8.1 Tracking Changes

Over time, developers and stewards can track:

- How the admissibility fraction changes as new data is ingested.
- How lifecycle decay affects the fraction.
- How improvements in promotion processes and provenance capture raise coherence.

This allows the system to answer questions like:

- “Did our recent migration increase or decrease admissibility?”
- “Are we improving how we capture spatial and temporal anchors?”

### 44.8.2 Practical Use for Rural Developers

Rural developers can use Phi as a simple health indicator:

- If Phi rises, more governed records are ready to speak.
- If Phi falls unexpectedly, something may be wrong in lifecycle handling or promotion logic.
- If Phi remains steady while the corpus grows, it may be time to invest in promotion and cleanup work.

The measurement is practical: it is a ratio of counts, not an obscure statistic.

---

## 44.9 Implementation Status

**Phi Probe — Semantic Coherence Measurement: Demonstrated.**

As of July 26, 2026:

- Total authorized governed rows: 237,655.
- Admissible rows for public claims: 93,423.
- Admissibility fraction: approximately 39.3%.

These numbers reflect a live inspection of the governed corpus, not a hypothetical estimate. The Phi probe is therefore a demonstrated measurement of semantic coherence within H_App at that time.

Within the academic scope of this chapter, the system is allowed to claim that:

- Coherence is measurable.
- The current coherence level is known.
- Overflow behavior is grounded in this measured corpus.

---

## 44.10 Step-by-Step Summary for Rural Developers

To understand and use this chapter:

1. **Know what Phi measures.**  
   It measures the fraction of governed records that are admissible for public claims.

2. **Remember the concrete numbers.**  
   93,423 admissible rows out of 237,655 total give about 39.3% admissibility as of July 26, 2026.

3. **Connect Phi to the ten conditions.**  
   Only records that meet all ten admissibility conditions count as coherent for public claims.

4. **See the link to overflow.**  
   Overflow events depend on coherent governed state; the Phi measurement shows that such coherence is present.

5. **Use Phi as a health gauge.**  
   Track Phi over time to see whether coherence is improving or degrading.

6. **Stay within scope.**  
   This chapter does not claim to measure every kind of coherence. It focuses on admissibility-based semantic coherence within the governed corpus.

---

## 44.11 Closing

The Phi probe gives H_App a way to talk about semantic coherence with numbers instead of metaphors. By tying coherence to the fraction of governed records that are admissible for public claims, and by reporting 39.3% admissibility as of July 26, 2026, the system shows that its governed corpus is both measurable and meaningfully constrained.

For rural developers, that means they can look at the corpus not just as a pile of data, but as a living, governed body whose coherence can be monitored, improved, and trusted.
