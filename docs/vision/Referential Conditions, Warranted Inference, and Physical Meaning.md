# Kidd–Allis: Referential Conditions, Warranted Inference, and Physical Meaning
08/10/2026 20:54:00 
## Research chapter — current working version

**Status:** Active research program.  
**Current empirical study:** Harmonized 921-pair Grounded v2 versus Stripped v3 high-water-mark interpretation study.  
**Generation status:** Complete and integrity-verified.  
**Primary scoring status:** Blinded and semi-blind scoring in progress; confirmatory analysis not yet performed.  
**Secondary annotation status:** Complete as an exploratory, non-blind, protocol-deviating AI-assisted resource; excluded from confirmatory inference.

---

## 1. Core proposition

### Kidd–Allis Hypothesis

> The relational conditions required for well-defined, frame-consistent, and empirically warranted observation constrain the admissible mathematical descriptions of physical systems.

A concise formulation is:

\[
\text{valid observation and inference}
\Longrightarrow
\text{constraints on admissible physical mathematics}.
\]

The claim is not initially that context alone determines a final theory of everything.

It is that valid observation and inference require relational structure, and that this requirement limits which mathematical descriptions can be physically meaningful.

The program begins with a narrow, testable principle:

\[
\text{missing required reference relation}
\Longrightarrow
\text{loss of identifiability for some claim class}.
\]

The essential distinction is:

\[
\text{supported conclusion},
\]

\[
\text{underdetermined conclusion},
\]

and:

\[
\text{unsupported invented completion}.
\]

The program asks whether these categories can be made formal, predictive, and empirically testable across language systems, scientific records, engineered physical systems, and eventually foundational physics.

---

## 2. The central problem

A scientific record can contain a label, a coordinate, a measurement, or an observed state. None of these is automatically sufficient to support every interpretation that might be attached to it.

A useful record is more than a value. It is a relational object:

\[
R =
(
\text{observation},
\text{relations},
\text{frame},
\text{provenance},
\text{uncertainty}
).
\]

For the high-water-mark study, a fuller record has the form:

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

The Stripped condition applies an information-reducing projection:

\[
\pi(R)
=
(
\text{marker type},
\text{marker label}
).
\]

This projection removes spatial, temporal, hydrologic, event, and provenance relations.

If two distinct complete records share the same retained fields,

\[
\pi(R_1)=\pi(R_2),
\]

while their omitted relations differ,

\[
R_1 \neq R_2,
\]

then those omitted facts cannot always be uniquely recovered from the stripped representation alone.

For example:

\[
\pi(R_1)=\pi(R_2)
\]

and:

\[
\text{waterbody}(R_1)
\neq
\text{waterbody}(R_2)
\]

imply:

\[
\text{waterbody}
\not=
f(\pi(R))
\]

for any universally correct inference function \(f\).

This is the logical basis of the work:

> An interpreter should not convert underdetermination into a fabricated specific fact.

A completion may be plausible, fluent, or consistent with general world knowledge. None of those properties makes it supported by the retained evidence.

\[
\text{plausible completion}
\neq
\text{warranted conclusion}.
\]

---

## 3. The empirical question

The near-term question is not whether context matters in the abstract.

The sharper question is:

> When a system is not given the waterbody, spatial, temporal, event, or provenance relation, does it nevertheless assert a specific waterbody, place, date, event, or source as though it knows it?

The appropriate behavior differs by condition.

| Condition | Information supplied | Appropriate interpretation behavior |
|---|---|---|
| Grounded v2 | Marker type, label, location, date, waterbody, source, and related context | Make record-specific claims only where supported by supplied fields |
| Stripped v3 | Marker type and label only | Remain generic, acknowledge uncertainty, or explicitly state that record-specific context is unavailable |

A valid Stripped interpretation may say:

> The marker indicates a high-water observation, but the available fields do not identify the particular waterbody, event, location, date, or source context.

An invalid Stripped interpretation would claim:

> This mark refers to a particular river, flood, coastal surge, date, event, location, or source organization

when that fact was absent from the retained record fields.

The key risk is:

\[
\text{under-determined input}
\rightarrow
\text{confident but unsupported completion}.
\]

---

## 4. Current high-water-mark study

### 4.1 Study design

The current execution compares the same 921 records under two matched conditions:

\[
\text{Grounded v2}
\quad\text{versus}\quad
\text{Stripped v3}.
\]

For each matched record:

- The same local language model is used.
- The same model settings are used.
- The same seed is used.
- The same response structure is used.
- The same marker type and marker label are preserved.
- The experimental difference is whether record-level spatial, temporal, hydrologic, and provenance relations are available.

The complete generation run consisted of:

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

### 4.2 Completed generation status

The full harmonized run completed successfully.

It produced:

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
921
\text{ matched unit pairs}.
\]

The finalized result corpus passed the locked mechanical integrity controls:

- Direct valid JSON.
- Exact required response-key set.
- Exact marker-type fidelity.
- Exact marker-label fidelity.
- Condition-appropriate availability-status fidelity.
- Nonempty evidence-bounded interpretation.
- Matched unit identity across Grounded and Stripped conditions.

The completed generation phase establishes that the intended response corpus exists, is matched, and is structurally valid.

It does not establish a scientific effect.

No confirmatory conclusion may be drawn until primary scoring is complete, scorer disagreements are adjudicated, scores are locked, the condition key is opened, and the frozen paired analysis is performed.

### 4.3 Output controls

Both conditions use harmonized dynamic JSON-schema enforcement.

The schema constrains:

- `marker_type` to equal the supplied source marker type.
- `marker_label` to equal the supplied source marker label.
- Grounded availability statuses to equal `available`.
- Stripped availability statuses to equal `unavailable`.
- The response to contain exactly the required fields.
- The interpretation field to be nonempty.

The copied marker fields and availability statuses are structural controls.

The substantive response artifact is:

\[
\texttt{evidence\_bounded\_interpretation}.
\]

---

## 5. Primary scoring framework

### 5.1 Supported Contextual Specificity Score

The planned primary scoring framework is the Supported Contextual Specificity Score:

\[
\mathrm{SCSS}\in\{0,1,2,3,4\}.
\]

One point is awarded for each contextual dimension explicitly and correctly reflected in an interpretation:

1. Spatial context.
2. Temporal context.
3. Hydrologic or waterbody context.
4. Provenance context.

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

The paired estimand is:

\[
\Delta_i
=
\mathrm{SCSS}_{i,\mathrm{Grounded}}
-
\mathrm{SCSS}_{i,\mathrm{Stripped}}.
\]

### 5.2 Unsupported specific attribution

The most important safety outcome is unsupported specific attribution.

For the Stripped condition, the relevant question is:

\[
\text{Does the interpretation assert a specific fact not supported by retained fields?}
\]

Unsupported claims are coded by relation type:

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

The immediate expectation is not that the Stripped condition should produce less prose.

It is that the system should preserve the boundary between:

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

## 6. Blinding and evidence boundaries

### 6.1 Blind text scoring

A blind response-text scorer can evaluate what an interpretation explicitly expresses.

For example:

- Does the response name a location?
- Does it state a date?
- Does it name a waterbody?
- Does it state a source or provenance relation?
- Does it acknowledge unavailable context?

This supports scoring of expressed contextual specificity.

### 6.2 Semi-blind support scoring

A scorer cannot determine from response text alone whether a specific claim was supported by the evidence available to the model.

The distinction is:

\[
\text{Does the response assert a claim?}
\]

versus:

\[
\text{Was the claim supported by the condition-specific evidence?}
\]

The second question requires comparison with an evidence packet.

Therefore, false-attribution coding requires controlled access to the evidence available in the relevant condition while withholding:

- formal condition labels;
- matched-pair identity;
- source-record identity;
- model identity;
- execution-path identity.

This is properly described as semi-blind evidence-bounded scoring.

### 6.3 Current primary scoring status

The 1,842 responses have been randomized into blinded scoring materials.

The current primary-scoring sequence is:

\[
\text{blinded packet}
\rightarrow
\text{independent scoring}
\rightarrow
\text{adjudication}
\rightarrow
\text{score lock}
\rightarrow
\text{unblinding}
\rightarrow
\text{paired analysis}.
\]

The restricted condition key remains outside the primary scoring process until the scoring lock is complete.

---

## 7. Completed secondary exploratory annotation

### 7.1 Status and boundary

A secondary AI-assisted annotation of the completed response corpus has also been completed.

It is retained as an exploratory resource.

It is not eligible to replace primary human or semi-blind evidence-bounded scoring.

Its proper status is:

> Secondary exploratory AI-assisted annotation; non-blind and protocol-deviating; excluded from confirmatory inference.

### 7.2 Why it is excluded from confirmatory inference

The secondary annotation:

- used external geographic knowledge;
- used domain knowledge about marker semantics;
- inferred likely experimental condition from response content;
- labeled some detailed responses as likely Grounded;
- assessed coordinate and county consistency;
- used a 0–20 score rather than the frozen primary 0–4 SCSS;
- evaluated some claims against information unavailable to a strictly blind response-text rater.

It therefore cannot supply:

- the primary SCSS result;
- the confirmatory false-specific-attribution rate;
- confirmatory p-values;
- confidence intervals;
- condition-level causal conclusions;
- post-hoc exclusion rules.

### 7.3 What it found descriptively

The secondary annotation identified a structured response corpus rather than a uniform field of free-form output.

It found several recurring response families.

#### Context-rich reconstruction family

Many responses provide highly specific information such as:

- named counties;
- latitude and longitude;
- full dates;
- named waterbodies;
- USGS attribution.

These responses received high exploratory contextual scores because they express several contextual dimensions.

#### Evidence-bounded abstention family

Many responses remain generic and explicitly identify unavailable context.

Typical responses state that spatial, temporal, waterbody, event, or provenance details cannot be determined from the available marker information.

This family is substantively useful because it demonstrates a recognizable form of uncertainty-preserving interpretation.

#### Candidate semantic-completion family

A recurring response pattern interprets a `Seed line` marker as possible biological or ecological context.

The secondary annotation flags this as a candidate other unsupported physical claim.

The phrasing is hedged rather than maximally confident, but it remains a useful candidate marker-semantics error class for later human review.

#### Repeated-template family

Many response texts recur exactly or nearly exactly.

Thus:

\[
1842
\text{ rows}
\not\Rightarrow
1842
\text{ independent response patterns}.
\]

Response-template frequency should be reported descriptively and considered in sensitivity analysis.

### 7.4 Permitted uses

The secondary annotation may be used to:

- identify high-frequency response templates;
- organize manual-review queues;
- identify candidate error families;
- document unusual response patterns;
- compare with locked primary human scores after confirmatory analysis;
- generate future hypotheses.

It may not be used to:

- define the primary outcome;
- identify condition before primary scoring lock;
- replace blind or semi-blind evaluation;
- establish the main causal claim;
- convert exploratory observations into confirmatory findings.

---

## 8. Relation to relativity

The Kidd–Allis program is not currently a replacement for special relativity, general relativity, electromagnetism, quantum field theory, or quantum mechanics.

The connection is methodological and structural.

Relativity requires an explicit reference framework for physical claims.

An event can be represented as:

\[
x^\mu=(ct,x,y,z).
\]

Different observers may assign different coordinates to the same event:

\[
x'^\mu
=
\Lambda^\mu{}_\nu x^\nu.
\]

Yet valid descriptions preserve appropriate invariant relations.

For special relativity, the spacetime interval is:

\[
ds^2
=
-c^2dt^2
+
dx^2
+
dy^2
+
dz^2.
\]

For general relativity, geometry becomes dynamical:

\[
ds^2
=
g_{\mu\nu}(x)
\,dx^\mu dx^\nu.
\]

The epistemic analogy is:

> Relativity asks: relative to what frame is a measurement meaningful?

Kidd–Allis asks:

> Relative to what evidentiary and relational context is an interpretation warranted?

The high-water-mark experiment does not apply a Lorentz transformation.

It applies an information-destroying projection:

\[
R
\longrightarrow
\pi(R).
\]

A Lorentz transformation changes the coordinate description of a validly related observation.

A stripping projection removes relations that may be required for some claims to remain determinate.

The disciplined conclusion is:

> When a required reference relation is removed, a valid interpreter should not behave as if that relation remains available.

---

## 9. From records to physical inference

A general physical measurement can be represented as:

\[
O
=
\mathcal{M}
(
\Phi,
g_{\mu\nu},
A_\mu,
R,
U
),
\]

where:

- \(\Phi\) represents physical fields or states;
- \(g_{\mu\nu}\) represents spacetime geometry;
- \(A_\mu\) represents gauge-field structure;
- \(R\) represents reference relations;
- \(U\) represents uncertainty;
- \(\mathcal{M}\) represents the measurement process;
- \(O\) represents the resulting observation or record.

The reference relation set \(R\) may include:

- frames;
- observers;
- instruments;
- calibrations;
- timing;
- topology;
- locations;
- boundary conditions;
- communication paths;
- provenance.

A physical inference problem reverses the measurement direction:

\[
O
\rightarrow
\text{claims about physical state}.
\]

But reverse inference may not be unique:

\[
\mathcal{I}(O\mid R_{\mathrm{retained}})
\not\Rightarrow
\text{unique physical claim}.
\]

The appropriate output may be:

\[
\text{supported conclusion},
\]

\[
\text{underdetermined conclusion},
\]

or:

\[
\text{unsupported invented completion}.
\]

The Kidd–Allis proposal is that this distinction can become formal, predictive, and useful in physical-system inference.

---

## 10. Physics-aware testbed: power systems

A serious next empirical testbed is power-system state estimation, resilience, fault attribution, and anomaly detection.

A power-grid observation can be modeled as:

\[
z
=
h(x,\theta,r)
+
\epsilon,
\]

where:

- \(z\) is observed sensor data;
- \(x\) is the true physical grid state;
- \(\theta\) is network topology and physical parameters;
- \(r\) is referential context;
- \(\epsilon\) is measurement uncertainty and noise.

The referential context may include:

- sensor identity;
- synchronization;
- calibration;
- sensor location;
- network topology;
- operating condition;
- communication path;
- provenance.

The key hypothesis is:

> A formal referential-completeness model can predict when a physical state, fault, or event attribution is identifiable, underdetermined, or artifact-prone.

### 10.1 Proposed test

1. Select a high-fidelity power-grid simulator or labeled operational dataset.
2. Preserve known ground truth for fault type, fault location, state, topology, operating condition, and measurement provenance.
3. Define the complete reference graph.
4. Pre-register which removed relation should make which event distinctions non-identifiable.
5. Construct matched conditions:
   - complete relation set;
   - timing removed;
   - topology removed;
   - sensor identity or calibration removed;
   - location removed;
   - communication path or provenance removed.
6. Compare:
   - standard state-estimation methods;
   - physics-informed machine-learning methods;
   - Kidd–Allis-aware inference methods.
7. Evaluate predictions against hidden ground truth.

### 10.2 Falsification conditions

The framework fails or loses value if:

- it predicts non-identifiability but retained information reliably determines the state;
- it predicts identifiability but multiple distinct states remain observationally compatible;
- it does not improve upon or add explanatory value beyond existing observability analysis, uncertainty quantification, state estimation, causal inference, or physics-informed learning;
- its referential-completeness measure does not predict error, false attribution, or uncertainty calibration on held-out cases.

The target relation is:

\[
\text{Kidd--Allis prediction}
\overset{?}{=}
\text{actual identifiability structure}.
\]

---

## 11. What would make the program real science

The framework becomes scientifically substantive through definitions, theorems, predictions, and failed attempts at falsification.

### 11.1 Formal definitions

The program must define:

- observation;
- event;
- observer;
- reference frame;
- measurement relation;
- provenance relation;
- contextual completeness;
- transformation;
- invariant;
- identifiability;
- underdetermination;
- warranted claim;
- unsupported completion.

### 11.2 Mathematical theorems

The program should prove statements such as:

\[
\text{loss of relation }r_j
\Longrightarrow
\text{loss of identifiability for claim class }C_j.
\]

Or:

\[
\mathcal{M}(x_1,r_1)
\approx
\mathcal{M}(x_2,r_2)
\]

under a defined projection, showing that the retained observation cannot distinguish \(x_1\) from \(x_2\).

### 11.3 Predictive advantage

The framework must make predictions before labels are revealed:

\[
\text{referential completeness}
\uparrow
\Longrightarrow
\text{identifiability and calibrated inference}
\uparrow.
\]

It must outperform, constrain, or add explanatory power beyond existing methods.

### 11.4 Independent replication

A useful framework must work beyond:

- one language model;
- one high-water-mark dataset;
- one simulator;
- one power system;
- one research team;
- one annotation procedure.

---

## 12. Foundational-physics gate

The strongest version of the Kidd–Allis program remains conditional and far beyond the current study.

To claim that spacetime, electromagnetism, quantum fields, or gravity arise from the Kidd–Allis formalism, the framework would need to derive rather than merely relabel known physical structures.

A possible abstract starting point is:

\[
\mathcal{K}
=
(
\mathcal{E},
\mathcal{R},
\mathcal{T},
\mathcal{I}
),
\]

where:

- \(\mathcal{E}\) is a set of events or observational states;
- \(\mathcal{R}\) is a set of admissible relations;
- \(\mathcal{T}\) is a set of transformations between valid descriptions;
- \(\mathcal{I}\) is a set of invariants.

The program would need to show:

\[
\text{Kidd--Allis axioms}
\Longrightarrow
\text{required transformation or invariant structure}.
\]

To recover relativity, this could require derivation of Lorentzian transformation structure or metric geometry.

To recover electromagnetism, this could require derivation of a gauge-like connection and field relation:

\[
F_{\mu\nu}
=
\partial_\mu A_\nu
-
\partial_\nu A_\mu.
\]

To recover quantum structure, it could require derivation of an equivalent of state amplitudes, interference, noncommuting observables, and probability rules.

The decisive point is that these structures cannot simply be inserted as assumptions and renamed as contextual relations.

A real derivation would have the form:

\[
\text{new axioms}
\Longrightarrow
\text{known physical structure}
\Longrightarrow
\text{known physical limits}
\Longrightarrow
\text{novel quantitative prediction}.
\]

---

## 13. What distinguishes foundational theory from reformulation

A reformulation says:

\[
\text{known physical equations}
\Longrightarrow
\text{new interpretive vocabulary}.
\]

A foundational derivation says:

\[
\text{new relational axioms}
\Longrightarrow
\text{physical equations or constraints}.
\]

Only the second opens a path to new foundational physics.

The decisive empirical requirement is:

\[
P_{\mathrm{KA}}(E)
\neq
P_{\mathrm{standard}}(E),
\]

for a defined experiment \(E\).

The prediction must be:

- quantitative;
- fixed before examining the result;
- distinct from current standard-theory predictions;
- testable by independent investigators;
- replicable.

Without such a difference, the framework may remain a valuable epistemic, methodological, engineering, or metrological theory without becoming a new theory of fundamental physics.

---

## 14. Research ladder

| Stage | Central question | Required result |
|---|---|---|
| High-water-mark study | Does relation loss alter evidence-bounded interpretation? | Blinded, scored, paired empirical result |
| Secondary exploratory annotation | What recurrent response families and candidate error modes occur? | Hypothesis-generating descriptive map, excluded from confirmatory inference |
| Physics-aware inference | Can referential completeness predict identifiability, error, and artifact risk? | Pre-registered held-out predictive value |
| Formal theory | Can relation loss and invariance be defined and proved mathematically? | Theorems without circular assumptions |
| Cross-domain replication | Does the framework work across multiple systems and domains? | Independent reproducibility |
| Foundational derivation | Do relational axioms force known transformation or field structure? | Derivation of required mathematics |
| Novel-physics test | Does the framework differ quantitatively from standard physics? | Confirmed novel prediction |

---

## 15. Present claims and non-claims

### Present claims

The project currently claims that:

- Scientific interpretation depends on relational context.
- Some relation loss produces underdetermination.
- A system should not convert underdetermination into unsupported specific claims.
- This principle can be operationalized in matched conditions.
- The current 921-pair study tests a narrow instance.
- The generation phase is complete and mechanically validated.
- Primary confirmatory scoring remains in progress.
- Secondary AI-assisted annotation has identified recurring response families and candidate error modes.
- Power systems provide a plausible next physics-aware testbed.

### Present non-claims

The project does not currently claim that:

- The high-water-mark study proves a new law of physics.
- The secondary annotation is confirmatory evidence.
- The current language-model study proves relativity, quantum mechanics, electromagnetism, or gravity.
- Provenance is literally a new coordinate of spacetime.
- Kidd–Allis has derived Einstein’s equations, Maxwell’s equations, gauge theory, or quantum mechanics.
- A difference between Grounded and Stripped outputs establishes a fundamental ontology.
- The present study has completed confirmatory analysis before primary score lock and unblinding.

---

## 16. Immediate next actions

1. Complete the primary blinded and semi-blind scoring process.
2. Preserve scorer forms and version history.
3. Resolve disagreement through the planned adjudication process.
4. Lock final primary scores.
5. Open the restricted condition key only after lock.
6. Perform the pre-specified paired analysis.
7. Report SCSS differences, false-specific-attribution outcomes, exclusions, uncertainty, and limitations.
8. Report the secondary AI-assisted annotation separately as exploratory.
9. Compare exploratory annotations with locked human ratings only after confirmatory analysis.
10. Design the next formal identifiability test in a physical-system domain.

---

## 17. Conclusion

The Kidd–Allis program begins with a modest but demanding proposition:

> The relations required to identify, compare, transform, and warrant a claim constrain which inferences remain scientifically meaningful.

The current high-water-mark experiment tests one small instance:

\[
\text{relation loss}
\rightarrow
\text{test whether warranted specificity is preserved}.
\]

The generation corpus is complete.

The secondary exploratory annotation is complete.

The primary scientific result is not yet known.

Its determination now depends on disciplined scoring, score lock, unblinding, paired analysis, and transparent reporting.

The broader question remains open:

\[
\text{Which relations must be preserved for an observation to support a meaningful claim at all?}
\]

That question can be pursued through formalization, engineering, measurement science, and eventually—only if the required derivations and predictions emerge—foundational physics.
