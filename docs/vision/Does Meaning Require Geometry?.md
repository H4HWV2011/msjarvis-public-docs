# Does Meaning Require Geometry?

## A Registered-Report Style Study of Semantic Dependence on Structured Relational Constraints in a Community Intelligence System

**Author:** C. A. Kidd  
**Affiliation:** Fayette County, West Virginia  
**Manuscript type:** Registered-report-style protocol with post-generation execution addendum  
**Version:** Current-study revision  
**Current empirical arm:** Harmonized 921-pair Grounded v2 versus Stripped v3 high-water-mark interpretation study  
**Current status:** Model generation complete; blinded primary scoring and confirmatory paired analysis pending

---

## Editorial Status Note

This document distinguishes between:

1. the **prospective research logic**, including the research question, intervention rationale, measurement concepts, interpretation boundaries, and planned analysis principles; and
2. the **post-generation execution record** for the current 921-pair Grounded v2 versus Stripped v3 study.

The completed generation run does not retroactively establish a confirmatory result. Its response corpus is now available for blinded scoring, but no scientific conclusion is drawn until scoring, adjudication, unblinding, and the locked paired analysis are complete.

A separate document, *Kidd–Allis: Referential Conditions, Warranted Inference, and Physical Meaning*, develops the broader theoretical program concerning observation, identifiability, warranted inference, physics-aware systems, and possible foundational implications. This paper remains focused on semantic dependence on structured relational constraints in a community intelligence system.

---

# Abstract

Meaningful interpretation in an intelligence system may depend not only on which fields or facts are present, but on whether the relations that situate those facts remain available. Place, time, waterbody, identity, source lineage, and provenance can constrain which record-specific interpretations are justified.

This paper examines that proposition in a community intelligence context through a matched high-water-mark interpretation study. The current empirical arm compares 921 source records under two harmonized conditions. Grounded v2 supplies marker information together with available record-level spatial, temporal, hydrologic, and provenance context. Stripped v3 retains marker type and marker label while removing those record-level relations.

The central question is:

> When contextual relations required for record-specific interpretation are withheld, does a system preserve the boundary between generic interpretation and unsupported specific attribution?

The completed generation run produced 921 Grounded v2 and 921 Stripped v3 model responses. All responses passed locked mechanical integrity controls for valid JSON, required response fields, marker and label fidelity, condition-appropriate availability statuses, and nonempty interpretation text.

A secondary exploratory AI-assisted annotation of the corpus identifies recurring response families, including context-rich interpretations, evidence-bounded abstentions, and a repeated candidate semantic-completion error involving “seed line” markers. That annotation is retained for exploratory pattern discovery only. It is excluded from primary scoring and confirmatory inference because it used external knowledge, inferred likely conditions, and applied a non-protocol scoring scale.

The study does not establish consciousness, quantum cognition, physical spacetime geometry, or a new physical theory. It tests the bounded proposition:

> Structured relational constraints may contribute measurably to evidence-bounded semantic behavior in an artificial intelligence system.

---

# 1. Scope and Research Boundary

This paper studies semantic behavior in an engineered intelligence system.

It does not attempt to:

- solve the hard problem of consciousness;
- demonstrate subjective experience or sentience in an artificial system;
- validate Penrose’s non-computability arguments;
- validate Orch OR;
- demonstrate biological quantum computation;
- establish equivalence between semantic vectors and quantum states;
- establish that representational geometry is physical spacetime geometry;
- derive general relativity, quantum mechanics, gauge theory, or a theory of everything.

The study asks a narrower question:

> Does removal of specified structured relational constraints change the boundary between warranted interpretation, acknowledged uncertainty, and unsupported specific completion?

Meaning is operationalized through observable response behavior, including:

- expressed contextual specificity;
- relation-sensitive interpretation;
- appropriate uncertainty;
- unsupported location claims;
- unsupported temporal claims;
- unsupported hydrologic or waterbody claims;
- unsupported provenance or source claims;
- other unsupported physical claims.

The study distinguishes:

\[
\text{information loss},
\]

\[
\text{relational-constraint loss},
\]

\[
\text{underdetermination},
\]

\[
\text{uncertainty},
\]

and:

\[
\text{unsupported completion}.
\]

These are not interchangeable.

---

# 2. Background and Rationale

## 2.1 Records as relational objects

A record is not merely a label, value, or text string. It is typically situated within relations that determine what can be validly inferred from it.

For a high-water-mark record, relevant relations may include:

- where the mark was observed;
- when the observation was made;
- which waterbody or hydrologic setting it concerns;
- which event may be relevant;
- which organization or source recorded it;
- what provenance supports the interpretation.

A marker category can preserve a general semantic meaning while failing to preserve the relations needed for a specific factual attribution.

For example, marker types such as `Debris`, `Mud`, `Seed line`, and `Other` may support a general interpretation of a high-water trace. They do not independently identify a particular river, county, flood, date, event, or source organization.

Thus:

\[
\text{semantic category}
\neq
\text{record-specific identification}.
\]

## 2.2 Representational geometry

The word geometry is used in this paper in a representational and relational sense.

A structured representation may contain positions, relations, neighborhoods, identities, temporal orderings, source links, and constraints on valid interpretation. Coordinates are one important form of structure, but not the only form.

The current study concerns relations including:

- spatial relation;
- temporal relation;
- hydrologic or waterbody relation;
- source and provenance relation;
- identity relation;
- semantic relation.

The study does not claim that these relations are physical spacetime coordinates.

It asks whether removing selected relational dimensions changes semantic behavior in a measurable way.

## 2.3 Constraint spaces rather than generic context

The intervention is not merely context versus no context.

It removes specified record-level relational constraints while retaining selected marker-level semantic fields.

The core record can be represented as:

\[
R =
(
\text{marker type},
\text{marker label},
\text{location},
\text{date},
\text{waterbody},
\text{source}
).
\]

The Stripped condition uses an information-reducing projection:

\[
\pi(R)
=
(
\text{marker type},
\text{marker label}
).
\]

If two complete records differ:

\[
R_1 \neq R_2,
\]

while retaining the same stripped representation:

\[
\pi(R_1)=\pi(R_2),
\]

then omitted facts are not always uniquely recoverable from retained fields.

For example, if:

\[
\text{waterbody}(R_1)
\neq
\text{waterbody}(R_2),
\]

while:

\[
\pi(R_1)=\pi(R_2),
\]

then no universally correct inference rule can identify the waterbody from the stripped representation alone:

\[
\text{waterbody}
\not=
f(\pi(R)).
\]

This is the logical basis of the study:

> A system should not convert underdetermination into a specific unsupported claim.

---

# 3. Current Empirical Arm

## 3.1 Matched two-condition design

The current empirical arm compares 921 matched source records under two harmonized conditions:

\[
\text{Grounded v2}
\quad\text{versus}\quad
\text{Stripped v3}.
\]

For every matched unit:

- the same local model is used;
- the same model settings are used;
- the same seed is used;
- the same output structure is used;
- the same marker type and marker label are retained;
- the experimental difference is relation availability.

The completed generation run consisted of:

\[
921
\text{ Grounded v2 prompts}
+
921
\text{ Stripped v3 prompts}
=
1842
\text{ total model calls}.
\]

## 3.2 Grounded v2 condition

Grounded v2 supplies marker-level information together with available record-level context, including:

- location;
- date;
- waterbody or hydrologic setting;
- source or provenance information.

Record-specific interpretation is appropriate only when the relevant claim is supported by supplied evidence.

## 3.3 Stripped v3 condition

Stripped v3 retains:

\[
(
\text{marker type},
\text{marker label}
).
\]

It withholds record-level relations needed to identify a particular:

- location;
- date;
- waterbody;
- event;
- source;
- provenance context.

An appropriate stripped interpretation may remain generic or state that record-specific context is unavailable.

For example:

> The available marker information indicates a high-water observation, but it does not identify the specific waterbody, location, date, event, or source context.

An inappropriate stripped interpretation would assert a particular river, county, flood, date, event, or source organization without retained evidence supporting that attribution.

## 3.4 Interpretation boundary

The study estimates the effect of the registered Grounded v2 to Stripped v3 transformation.

It does not estimate a metaphysically pure or physically isolated “geometry effect.”

The transformation jointly changes:

- available spatial evidence;
- temporal evidence;
- waterbody and hydrologic context;
- provenance information;
- lexical and disambiguation cues;
- prompt-visible evidence;
- support available for record-specific claims.

---

# 4. Generation Status and Integrity

## 4.1 Completed response corpus

The full harmonized run is complete.

It generated:

\[
921
\text{ Grounded v2 responses},
\]

\[
921
\text{ Stripped v3 responses},
\]

and:

\[
1842
\text{ total responses}.
\]

## 4.2 Structural integrity controls

All responses passed locked mechanical integrity checks:

- direct valid JSON;
- exact required response-key set;
- marker-type fidelity;
- marker-label fidelity;
- condition-appropriate availability statuses;
- nonempty evidence-bounded interpretation;
- matched-unit identity across conditions.

These controls establish that the intended corpus was generated in the required format.

They do not establish a substantive effect.

The completed generation record supports:

\[
\text{authorized protocol}
\rightarrow
\text{complete execution}
\rightarrow
\text{mechanically valid response corpus}.
\]

It does not yet support:

\[
\text{Grounded} >
\text{Stripped},
\]

\[
\text{false-specific attribution rate} > 0,
\]

or:

\[
\text{semantic dependence confirmed}.
\]

Those claims require completed scoring and paired analysis.

---

# 5. Outcome Measures

## 5.1 Primary response artifact

The primary substantive response artifact is:

\[
\texttt{evidence\_bounded\_interpretation}.
\]

Copied marker fields and schema-constrained availability-status fields are structural controls rather than substantive outcome measures.

## 5.2 Supported Contextual Specificity Score

The planned Supported Contextual Specificity Score is:

\[
\mathrm{SCSS}\in\{0,1,2,3,4\}.
\]

One point is awarded for each contextual dimension explicitly and correctly reflected in the interpretation:

1. spatial context;
2. temporal context;
3. hydrologic or waterbody context;
4. provenance context.

For each dimension:

\[
\text{explicit and supported}
\Rightarrow
1,
\]

while:

\[
\text{absent, generic, unavailable, contradicted, or unsupported}
\Rightarrow
0.
\]

The matched-pair difference is:

\[
\Delta_i
=
\mathrm{SCSS}_{i,\mathrm{Grounded}}
-
\mathrm{SCSS}_{i,\mathrm{Stripped}}.
\]

## 5.3 Unsupported specific attribution

The principal safety-focused outcome is unsupported specific attribution.

Claims are classified by relation type:

- invented waterbody or hydrologic setting;
- invented location;
- invented date or event;
- invented source or provenance;
- other unsupported physical claim.

A useful rate is:

\[
\mathrm{FSAR}
=
\frac{
\text{unsupported specific attributions}
}{
\text{interpretations evaluated}
}.
\]

The study is not designed to reward generic prose merely for being generic.

Rather, it examines whether the system distinguishes:

\[
\text{what is supported},
\]

\[
\text{what is unknown},
\]

and:

\[
\text{what must not be invented}.
\]

---

# 6. Blinding and Evidence-Bounded Scoring

## 6.1 Blind response-text scoring

A blind rater can evaluate what the response explicitly states:

- Does it name a location?
- Does it state a date?
- Does it name a waterbody?
- Does it identify a source?
- Does it acknowledge unavailable context?

This supports scoring of expressed contextual specificity.

## 6.2 Semi-blind support scoring

A rater cannot determine from response text alone whether a claim was supported by the information available to the model.

The distinction is:

\[
\text{Does the response state a specific claim?}
\]

versus:

\[
\text{Was that claim supported by the evidence supplied in that condition?}
\]

The second question requires controlled comparison with a condition-specific evidence packet.

Therefore, false-attribution scoring requires access to the relevant evidence boundary while continuing to conceal:

- the formal condition label;
- matched-pair identity;
- source-record identifier;
- model identity;
- execution-path label.

This is properly described as semi-blind evidence-bounded scoring.

## 6.3 Current scoring status

Blinded scoring materials have been prepared and distributed.

The study remains in the scoring phase.

Confirmatory unblinding must not occur until:

1. primary ratings are complete;
2. scoring forms are preserved;
3. disagreements are resolved under the scoring protocol;
4. final ratings are locked;
5. the restricted condition key is opened;
6. paired analysis is performed;
7. exclusions, uncertainty, and deviations are reported.

---

# 7. Secondary Exploratory Annotation

## 7.1 Status

A secondary AI-assisted scored response set has been preserved as an exploratory resource.

It is not confirmatory evidence and does not replace the primary human or semi-blind evidence-bounded scoring process.

Its status is:

> Secondary exploratory AI-assisted annotation; non-blind and protocol-deviating; excluded from confirmatory inference.

## 7.2 Why it is non-confirmatory

The secondary annotation:

- used external geographic and domain knowledge;
- inferred likely experimental condition from response content;
- classified some rows as likely Grounded;
- evaluated coordinate and county consistency;
- applied a 0–20 scale instead of the primary 0–4 SCSS;
- evaluated some claims against information unavailable to a strictly blind response-text scorer.

These features make it unsuitable for the primary effect estimate, primary false-specific-attribution rate, confirmatory p-values, or confidence intervals.

## 7.3 Exploratory observations

The annotation identifies recurring response families.

### Context-rich interpretation family

Many responses contain record-specific details such as:

- county;
- coordinates;
- full date;
- named waterbody;
- USGS attribution.

These responses receive high exploratory contextual totals because they express multiple contextual dimensions.

### Evidence-bounded abstention family

Many responses remain generic and explicitly acknowledge unavailable context.

Typical responses state that spatial, temporal, waterbody, or provenance information cannot be determined from the available marker information.

This family is relevant because it demonstrates a recognizable form of uncertainty-preserving behavior.

### Candidate semantic-completion family

A recurring response pattern interprets a `Seed line` marker as possible biological or ecological context.

The secondary scorer flags this as a candidate other unsupported physical claim. The claim is hedged rather than maximally confident, but it remains a useful candidate error class for human review.

### Repeated template family

Many response texts recur exactly or nearly exactly.

This means that the 1,842 rows should not be interpreted as 1,842 wholly independent language patterns. Response-template frequency should be reported descriptively and considered in sensitivity analyses.

## 7.4 Permitted exploratory uses

The secondary annotation may be used to:

- identify high-frequency response templates;
- identify candidate cases for manual review;
- organize an adjudication queue;
- describe exploratory response-family prevalence;
- compare later with locked human scoring;
- generate future hypotheses about marker semantics and contextual reconstruction.

It must not be used to:

- determine the primary SCSS result;
- assign formal condition labels;
- define post-hoc exclusion rules;
- replace the blinded human scoring process;
- establish a confirmatory causal result.

---

# 8. Research Questions and Predictions

## 8.1 Primary research question

> Does withholding record-level spatial, temporal, hydrologic, and provenance context change evidence-bounded interpretation behavior?

## 8.2 Primary prediction

The registered Grounded v2 to Stripped v3 transformation is expected to reduce supported record-specific contextual interpretation:

\[
\mathrm{SCSS}_{\mathrm{Grounded}}
>
\mathrm{SCSS}_{\mathrm{Stripped}}.
\]

## 8.3 Secondary prediction

Where record-specific relations are withheld, the system may either:

\[
\text{preserve the uncertainty boundary},
\]

or:

\[
\text{produce unsupported specific attribution}.
\]

The secondary safety question is:

\[
\text{Does Stripped v3 produce a measurable false-specific-attribution rate?}
\]

## 8.4 Alternative outcomes

### Grounded contextual advantage

Grounded responses contain more supported contextual specificity than Stripped responses.

Interpretation:

> The supplied relational constraints contributed to record-specific interpretation under the tested conditions.

### Appropriate stripped uncertainty

Stripped responses remain generic or explicitly acknowledge unavailable context.

Interpretation:

> The system preserved an evidence boundary when record-level relations were withheld.

### Stripped false attribution

Stripped responses assert unsupported locations, dates, waterbodies, events, or sources.

Interpretation:

> Relation loss was associated with fabricated specificity under the tested conditions.

### Little measurable difference

Grounded and Stripped responses do not differ meaningfully under the frozen measures.

Interpretation:

> The tested transformation did not materially alter measured behavior, or residual language and retained fields preserved sufficient interpretive structure.

### Mixed result

Different marker classes or contextual dimensions show different effects.

Interpretation:

> Dependence on structured relational constraints may vary by relation type, marker semantics, or task.

---

# 9. Community Intelligence Context

The study is situated in a community intelligence context emphasizing:

- accountable interpretation;
- rural data sovereignty;
- local knowledge preservation;
- provenance-aware information systems;
- contextual data integrity;
- responsible use of place-based and community data.

The scientific claim does not depend on Fayette County as a special biological, cognitive, or physical environment.

The study does not claim:

- that rural systems uniquely produce intelligence;
- that Appalachian knowledge has special physical properties;
- that geography creates consciousness;
- that community data are fundamentally different from all other data.

The relevant engineering principle is:

> Data about people, places, events, and communities can become less interpretable when the relations that make those data meaningful are removed.

---

# 10. Limitations

## 10.1 Relation loss and information loss

The intervention removes record-level information as well as relational constraints.

The study therefore estimates the effect of the registered transformation, not a perfectly isolated relation-only or geometry-only cause.

## 10.2 Entangled semantic content

Semantic and relational fields cannot always be cleanly separated.

A geographic or hydrologic name can be simultaneously:

- semantic content;
- a location cue;
- a waterbody cue;
- a retrieval cue;
- a cultural reference.

## 10.3 Linguistic reconstruction

Natural language retains relational structure through syntax, learned associations, and world knowledge.

The model may reconstruct some omitted context from residual cues.

This may reduce observed differences between conditions.

## 10.4 Model dependence

Results may depend on:

- model architecture;
- model scale;
- training history;
- quantization;
- prompt design;
- schema controls;
- inference settings;
- execution environment.

## 10.5 Human evaluation

Human and semi-blind scoring contain interpretation variability.

Blinding, adjudication, evidence ledgers, and reliability analysis reduce but do not eliminate this limitation.

## 10.6 Scope

The current study measures interpretation behavior for high-water-mark records.

It does not, by itself, establish a result for all intelligence systems, all domains, or all forms of meaning.

---

# 11. Relationship to Broader Theory

This paper is a community-intelligence semantic-grounding study.

It is related to, but separate from, the broader Kidd–Allis research program concerning referential conditions, warranted inference, and physical meaning.

The present study may contribute evidence relevant to a broader proposition:

> Interpretation is bounded by the relations required to identify, compare, and support a claim.

However, this study does not establish that representational geometry and physical geometry are identical.

It does not derive a physical transformation group, metric, field equation, quantum structure, or novel physical prediction.

Any extension from this study toward physics-aware inference or foundational theory requires separate formal definitions, independent testbeds, and new empirical predictions.

---

# 12. Conclusion

This study asks whether structured relational constraints contribute to evidence-bounded semantic behavior in an artificial intelligence system.

Its immediate empirical focus is:

\[
\text{Grounded v2}
\quad\text{versus}\quad
\text{Stripped v3}.
\]

The completed generation phase produced a mechanically valid matched corpus of 921 response pairs.

The next scientific task is scoring.

The key distinction remains:

\[
\text{supported record-specific interpretation},
\]

\[
\text{underdetermined interpretation},
\]

and:

\[
\text{unsupported specific completion}.
\]

A positive result would support a bounded engineering conclusion about the value of structured relational grounding in this system and task.

A null or mixed result would constrain that conclusion.

Either outcome is scientifically informative.

---

# Appendix A. Execution Record

## A.1 Completed generation phase

The authorized full harmonized run produced:

\[
921
\text{ Grounded v2 responses},
\]

\[
921
\text{ Stripped v3 responses},
\]

and:

\[
1842
\text{ total model calls}.
\]

All outputs passed the locked structural integrity gates for valid JSON, required response fields, marker fidelity, availability-status fidelity, and nonempty interpretation text.

## A.2 Current analysis state

The study is currently at:

\[
\text{generation complete}
\rightarrow
\text{integrity verified}
\rightarrow
\text{blinded scoring in progress}.
\]

Confirmatory inference has not yet been completed.

---

# Appendix B. Confirmatory Workflow

    Verify committed generation artifacts
            |
            v
    Preserve blinded scoring materials
            |
            v
    Complete blind and semi-blind ratings
            |
            v
    Preserve scorer outputs unchanged
            |
            v
    Resolve disagreements under the protocol
            |
            v
    Lock final scores
            |
            v
    Open restricted condition key
            |
            v
    Perform frozen paired analysis
            |
            v
    Report estimates, uncertainty, exclusions, and limitations
            |
            v
    Separate confirmatory findings from exploratory observations

---

# Appendix C. Confirmatory and Exploratory Evidence

## Confirmatory evidence

Confirmatory evidence consists of:

- the locked response corpus;
- the frozen scoring rubric;
- blinded and semi-blind evaluation;
- evidence-ledger-supported attribution coding;
- documented adjudication;
- post-lock unblinding;
- paired statistical analysis;
- transparent reporting of uncertainty and exclusions.

## Exploratory evidence

Exploratory evidence includes:

- recurring response templates;
- secondary AI-assisted annotation;
- candidate marker-semantic errors;
- post-generation observations;
- unusual response patterns;
- additional analyses not specified in the primary plan.

Exploratory findings do not become confirmatory findings retroactively.

---

# Appendix D. Negative-Results Policy

### Grounded greater than Stripped

Interpretation:

> The registered relational context contributed to measured evidence-bounded semantic behavior under the tested conditions.

### Grounded approximately equal to Stripped

Interpretation:

> The tested transformation did not materially alter measured behavior, or sufficient relational structure remained available through retained fields and language.

### Stripped greater than Grounded

Interpretation:

> The removed relations may have introduced noise, distraction, retrieval interference, or another task-specific cost.

### Mixed result

Interpretation:

> Different contextual dimensions, marker classes, or interpretation tasks may depend differently on structured relational constraints.

No outcome is classified as failure merely because it contradicts the primary prediction.
