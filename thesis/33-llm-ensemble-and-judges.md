# 33. LLM Ensemble and Judges

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 10, 2026*

---

## 33.1 Role of the Ensemble

The LLM ensemble in Ms. Allis provides plurality of generation, evaluation, and comparison rather than a single monolithic decision source. Different model instances and routing paths can contribute candidate answers, critiques, summaries, or evaluations, allowing the system to compare outputs instead of treating the first generation as authoritative.

The ensemble therefore serves two linked purposes. First, it expands the system’s ability to produce diverse candidate interpretations. Second, it supports internal checking by making disagreement, corroboration, and comparative scoring observable within the reasoning path.

This chapter concerns the ensemble as part of a governed architecture. Ensemble outputs are useful precisely because they remain provisional until they pass through the sandbox validation path and any later promotion gates.

---

## 33.2 Judges as Distinct Roles

Judges are specialized evaluative components within the ensemble architecture. Their function is not to generate the primary candidate content, but to assess candidate content according to defined criteria.

These criteria may include:

- truth or truth-likeness;
- consistency with available context;
- contradiction detection;
- coherence across reasoning steps;
- policy or constitutional fit;
- risk or safety concerns;
- confidence calibration.

A judge is therefore not simply another voice in the ensemble. It is an evaluative role with an authority-order function. It helps determine whether a candidate output should remain merely provisional, become corroborated within the sandbox, or be considered eligible for later approval by downstream gates.

---

## 33.3 Judges Inside the Sandbox Pipeline

The judges belong inside the actual sandbox pipeline.

They are not best understood as detached evaluators that appear only after reasoning is already complete. Instead, they operate as explicit validation steps in the bounded path between candidate generation and any possibility of promotion. Their outputs feed sandbox validation results, which in turn shape whether the current reasoning state is rejected, revised, corroborated, limited, or forwarded for later gate review.

A simplified sandbox pipeline can be described as:

1. retrieval and context assembly;
2. provisional ensemble generation;
3. judge evaluation inside the sandbox;
4. sandbox validation result;
5. candidate state outcome;
6. downstream gating and promotion review if eligible.

This placement matters because it keeps judgment close to the provisional reasoning state it is evaluating. The sandbox is where reversibility still exists, so that is where judge outputs have their most useful effect.

---

## 33.4 Explicit Judge Steps

Judge roles such as truth and consistency filters should be treated as explicit steps in the pipeline rather than background qualities of the ensemble.

A typical internal sequence may include:

- a **truth judge** that tests whether a candidate claim is sufficiently grounded in retrieved or available evidence;
- a **consistency judge** that checks whether the candidate contradicts prior steps, parallel outputs, or governing context;
- a **coherence judge** that examines whether the reasoning path holds together structurally;
- a **safety or policy judge** that tests whether the candidate remains within allowed boundaries.

The results of these judge passes feed the sandbox validation result. They do not themselves authorize production consequence. Instead, they help classify the candidate state and determine whether it should remain provisional, become corroborated, be sent back for revision, or be blocked from further movement.

This explicit step structure also clarifies how the chapter relates to the sandbox, BBB, and DGM chapters. Judges are part of the bounded validation interior, not a substitute for later promotion governance.

---

## 33.5 Provisional Ensemble Outputs

Ensemble outputs remain provisional until gated and promoted.

This is one of the most important authority-order statements in the chapter. A candidate answer produced by one or several models may be high quality, strongly worded, or internally persuasive. None of those properties makes it authorized. Inside the architecture, ensemble generation produces candidate states, not final states.

That means even a strongly corroborated ensemble result is still provisional while it remains inside the sandbox. It may gain a higher standing through judge agreement or evidentiary support, but it does not become approved merely by scoring well internally.

The ensemble therefore contributes to internal epistemic quality, while the downstream governance path determines whether any candidate result may carry broader authority.

---

## 33.6 Authority Order

The chapter benefits from a clear authority-order vocabulary for judge and ensemble outputs.

A useful sequence is:

\[
S_{\mathrm{prov}} \rightarrow S_{\mathrm{corr}} \rightarrow S_{\mathrm{elig}} \rightarrow S_{\mathrm{app}}
\]

where \(S_{\mathrm{prov}}\) is a provisional state, \(S_{\mathrm{corr}}\) is a corroborated state, \(S_{\mathrm{elig}}\) is a state judged eligible for promotion review, and \(S_{\mathrm{app}}\) is an approved state after downstream gating succeeds.

This terminology clarifies the function of judges:

- generation creates **provisional** candidate states;
- judge results may raise a candidate to **corroborated** status within the sandbox;
- sandbox validation may mark a corroborated state as **eligible** for downstream review;
- only later gating can create an **approved** state.

By using authority-order language, the system distinguishes internal confidence from authorized consequence.

---

## 33.7 Sandbox Validation Results

Judge outputs feed into sandbox validation results rather than acting as isolated verdicts.

A single truth score or consistency verdict is informative, but the sandbox needs a composite interpretation of what those results mean for the candidate state. Sandbox validation is therefore the step where judge findings are aggregated into a usable internal outcome.

Possible internal outcomes include:

- reject as unsupported or contradictory;
- revise because the candidate is promising but incomplete or unstable;
- corroborate because multiple judge paths support it sufficiently inside the sandbox;
- hold for additional evidence;
- mark as eligible for downstream review.

This composite result is important because different judges may disagree. One judge may find a candidate coherent while another finds it weakly grounded. Sandbox validation is the place where those tensions are interpreted while the reasoning state is still reversible.

---

## 33.8 Truth and Consistency as Filters

Truth and consistency are especially important judge roles because they sit near the center of the authority transition.

A truth-oriented judge helps test whether the candidate output is adequately tied to sources, retrieval context, or other evidentiary support. A consistency-oriented judge tests whether the candidate coheres with other parts of the active reasoning state, previously accepted constraints, or the current problem framing.

These should be understood as filtering functions inside the sandbox pipeline. They do not simply “score” the answer for interest or elegance. They determine whether the candidate state has enough internal integrity to move from provisional generation toward corroborated status.

When these filters fail, the sandbox should not treat the candidate as merely low-ranked. It should treat it as structurally blocked, revise-required, or non-eligible for further promotion.

---

## 33.9 Judge Disagreement

Judge disagreement is not noise to be hidden. It is often a meaningful signal.

When one judge finds a candidate strongly grounded and another finds it inconsistent, the disagreement reveals that the candidate occupies an unstable place in the current reasoning state. That instability should remain visible inside sandbox validation rather than being averaged away too early.

In practice, disagreement may lead to:

- revision of the candidate state;
- request for additional retrieval or evidence;
- downgrade from corroborated to still-provisional;
- escalation to human review in especially sensitive contexts;
- refusal to mark the state as eligible for downstream approval.

This is one reason the ensemble-and-judges architecture is valuable. It allows the system to represent uncertainty and conflict before consequence, instead of pretending unanimity where none exists.

---

## 33.10 Relationship to Downstream Gates

Judges are not the final authority in the architecture.

Their outputs operate inside the sandbox and contribute to authority-order transitions from provisional to corroborated and from corroborated to eligible. But the final move from eligible to approved belongs to downstream gating, including whatever truth, guardian, constitutional, BBB, or other promotion requirements apply in the relevant path.

This distinction keeps the chapter aligned with the surrounding architecture:

- the ensemble generates candidate outputs;
- judges evaluate those outputs inside the sandbox;
- sandbox validation classifies the candidate state;
- downstream gates decide whether an eligible state becomes approved.

Thus the judges are neither ornamental nor sovereign. They are interior validators in a larger governed promotion path.

---

## 33.11 Relationship to Corpus, Infrastructure, and Fractal Optimization

The ensemble-and-judges chapter now sits more clearly in relation to the surrounding chapters.

With the scraper and corpus chapter, the relationship is that corpus-derived material enters as reasoning context and may be assessed by judges for grounding, consistency, and adequacy of support. With the MountainShares and infrastructure chapter, judge behavior helps determine whether operationally meaningful outputs are sufficiently corroborated before any broader use. With the fractal optimization chapter, optimization loops may tune judge thresholds, ordering, or evaluation behavior, but the resulting outputs remain provisional until the sandbox and downstream gates classify them appropriately.

This means judges are part of a governed chain rather than a free-standing scoring layer. Their role is to shape transitions in authority order, not to collapse those transitions into one internal score.

---

## 33.12 Closing Statement

The LLM ensemble provides diverse candidate outputs, while judges act as explicit evaluative steps inside the sandbox pipeline. Truth, consistency, coherence, and related judge roles feed sandbox validation results that determine whether a candidate state remains provisional, becomes corroborated, or is marked eligible for downstream review.

Ensemble outputs therefore remain provisional until gated and promoted. By using authority-order terminology that distinguishes provisional, corroborated, eligible, and approved states, this chapter clarifies how judge outputs contribute to governed transitions without replacing the later approval path.
