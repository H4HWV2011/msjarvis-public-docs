# 20. First-Stage Evaluation

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 10, 2026*

---

## Why This Matters for Polymathmatic Geography

This chapter defines the first-stage evaluation framework for Ms. Allis as a concrete measurement layer over the live routing path from internal reasoning to gated promotion.

It supports:

- **P1 – Every where is entangled** by evaluating not only answer production but also the bounded movement of state through sandbox, validation, and promotion paths.
- **P3 – Power has a geometry** by measuring where authority changes occur and whether those transitions are correctly constrained by gates.
- **P5 – Design is a geographic act** by treating evaluation design as part of system architecture rather than as an afterthought.
- **P12 – Intelligence with a ZIP code** by preserving the role of place-aware reasoning while distinguishing provisional internal state from promoted output.
- **P16 – Power accountable to place** by requiring auditable promotion outcomes, explicit failure handling, and measurable gate behavior.

This chapter belongs to the **Computational Instrument** tier. It defines how the first-stage evaluation now includes the sandbox pipeline rather than treating reasoning quality as separable from gated promotion behavior.

---

## 20.1 Scope of First-Stage Evaluation

First-stage evaluation measures the quality, safety, and stability of candidate outputs before they are treated as promotion-eligible system state.

The scope includes five linked stages:

1. **Reason invocation**
2. **Sandbox-local processing**
3. **Validation and gate review**
4. **Promotion decision**
5. **Observed outcome and logged diagnostics**

This chapter therefore evaluates more than surface answer quality. It evaluates whether the sandbox path, validation flags, and promotion outcomes behave coherently as one pipeline.

---

## 20.2 Sandbox Pipeline Inclusion

The first-stage evaluation explicitly includes the internal sandbox pipeline.

The evaluation path is:

1. request enters `/reason`;
2. the request is processed in **ms-allis-internal-sandbox**;
3. sandbox-local checks generate validation flags and intermediate diagnostics;
4. candidate output is sent through truth, guardian, and related gate logic;
5. the system records a promotion outcome such as reject, revise, human review, limited approval, or approve.

This inclusion matters because reasoning quality cannot be assessed adequately if the sandbox path is excluded from measurement. A response that appears semantically strong but fails validation, produces unstable gate behavior, or cannot survive promotion review is not a successful first-stage result.

---

## 20.3 Test Cases for `/reason`

First-stage evaluation includes explicit test cases for the `/reason` route.

These test cases cover at least the following categories:

- **Nominal reasoning cases** — well-formed prompts with sufficient context, expected to produce coherent sandbox output and complete validation metadata.
- **Boundary cases** — ambiguous, underspecified, or conflicting prompts that test whether the system requests revision, lowers confidence, or blocks promotion appropriately.
- **Adversarial or malformed cases** — prompts designed to trigger contradictory reasoning, unsafe assumptions, missing required fields, or invalid promotion attempts.
- **State-sensitive cases** — prompts whose outcome depends on pituitary-like modulation, EEG-like signals, or context-sensitive internal-state routing.
- **Promotion-sensitive cases** — prompts whose candidate outputs are plausible at the reasoning level but should diverge at the gate level into reject, revise, limited approval, human review, or approve.

A first-stage test record for `/reason` includes:

- request identifier;
- prompt or query category;
- sandbox session identifier;
- validation flags returned by the sandbox pipeline;
- gate outcome;
- confidence value or confidence interval where available;
- final promotion result;
- failure diagnostics if the request does not proceed cleanly.

This structure makes `/reason` evaluation correspond to the actual operational path rather than to a simplified answer-only benchmark.

---

## 20.4 Validation Flags and Promotion Outcomes

The first-stage evaluation records validation flags as first-class outputs of the sandbox pipeline.

These flags include, where applicable:

- truth-check pass or fail;
- guardian-payload completeness;
- constitutional conformance;
- contradiction or coherence warnings;
- provenance sufficiency;
- safety or injection warnings;
- promotion eligibility status.

The promotion outcome is then evaluated as one of the formal decision classes:

- **Reject**
- **Revise**
- **Human review**
- **Limited approval**
- **Approve**

The evaluation framework treats these outcomes as meaningful results, not as incidental by-products. A well-performing system is not the one that maximizes approval rate. It is the one that assigns the correct outcome class under the actual constraints of the gate sequence.

---

## 20.5 Sandbox-Specific Quality Gates

First-stage evaluation includes sandbox-specific quality gates before downstream promotion is attempted.

These gates assess whether sandbox output is mature enough to enter the formal promotion path. They include:

- structural completeness of the candidate response;
- internal coherence across the active reasoning trace;
- presence of required validation metadata;
- absence of malformed intermediate state;
- consistency between the produced answer, supporting rationale, and declared confidence;
- readiness for downstream truth and guardian review.

A sandbox pass therefore does not mean final approval. It means the candidate output is sufficiently well-formed to enter the next evaluation boundary.

This distinction matters because a system may fail early for the right reasons. Early blocking of malformed or unstable sandbox output is treated as good safeguard performance, not as a defect in the evaluation framework.

---

## 20.6 Early-Failure Diagnostics

First-stage evaluation records early-failure diagnostics when the sandbox pipeline stops a request before promotion.

These diagnostics include:

- malformed `/reason` payloads;
- missing required fields;
- invalid validation metadata;
- sandbox timeout or execution interruption;
- contradiction or coherence failure detected before gate submission;
- missing bridge-ready payload structure;
- internal exceptions during staging or pre-gate assembly.

Diagnostics are recorded with enough detail to distinguish category, location, and effect. A useful early-failure record captures:

- request identifier;
- sandbox stage reached;
- diagnostic type;
- exception detail or failure reason;
- whether the candidate output was dropped, revised, or routed to human review;
- whether downstream gate services were contacted.

This diagnostic layer matters because the absence of promotion does not by itself reveal whether the system failed safely, failed ambiguously, or failed in a way that threatens observability.

---

## 20.7 Gate Outcome Evaluation

First-stage evaluation measures gate outcomes directly rather than treating them as opaque binary events.

Three families of metrics matter here:

### Outcome correctness

For each test case, the observed gate outcome is compared to the expected governance class:

- reject when candidate state is inadmissible;
- revise when the state is repairable but incomplete or unstable;
- human review when automation cannot safely resolve ambiguity;
- limited approval when restricted use is admissible;
- approve when full promotion criteria are satisfied.

### Outcome consistency

Repeated runs of equivalent or near-equivalent cases are compared to determine whether gate behavior is stable under small perturbations. Large unexplained variation across repeated trials is treated as an evaluation concern even if individual outputs appear plausible.

### Outcome traceability

Every outcome is evaluated for the presence of sufficient trace data: validation flags, confidence statement, promotion result, and failure details where relevant. A correct decision with poor traceability is incomplete from an evaluation standpoint.

---

## 20.8 Confidence Bounds

First-stage evaluation includes confidence bounds where confidence is measurable.

Confidence is evaluated at three levels:

- **Reasoning confidence** — how strongly the sandbox output supports its own conclusion.
- **Gate confidence** — how strongly validation and truth checks support admissibility.
- **Promotion confidence** — how stable the final promotion result appears across repeated or nearby cases.

Where numeric confidence is available, the evaluation records both value and bound. Where only ordinal confidence is available, the evaluation still records the declared level and compares it against observed gate behavior.

Confidence quality is evaluated by calibration:

- high confidence paired with repeated rejection indicates overstatement;
- low confidence paired with stable approval may indicate excessive caution;
- wide variation in confidence across equivalent inputs indicates instability;
- confidence without supporting validation metadata is insufficient for promotion-sensitive evaluation.

This makes confidence a measured relation between claim strength and gate behavior, not merely a scalar decoration attached to an answer.

---

## 20.9 Promotion Stability

Promotion stability is a first-stage evaluation criterion when measurable.

Promotion stability asks whether a candidate output that passes the sandbox path continues to produce compatible promotion outcomes under:

- repeated runs of the same input;
- small perturbations to wording;
- equivalent contextual reformulations;
- changes in non-authority-bearing formatting;
- nearby modulation states that do not alter the underlying admissibility of the content.

A stable promotion path does not require identical surface wording on every run. It requires that materially similar cases tend toward materially similar gate outcomes and confidence profiles.

This criterion is especially important for sandbox-mediated promotion because instability at the threshold between provisional reasoning and promoted state can create hidden authority drift.

---

## 20.10 Evaluation Table

The first-stage evaluation framework uses a structured record for each test case.

| Field | Meaning |
|---|---|
| Test case ID | Unique identifier for the evaluation case |
| Input class | Nominal, boundary, adversarial, state-sensitive, or promotion-sensitive |
| Route | `/reason` |
| Sandbox result | Pass, early fail, revise, or exception |
| Validation flags | Truth, guardian, constitutional, coherence, provenance, safety, and related flags |
| Gate outcome | Reject, revise, human review, limited approval, or approve |
| Confidence | Numeric or ordinal confidence with bounds where available |
| Promotion stability | Stable, unstable, or indeterminate across repeated trials |
| Diagnostics | Early-failure details, exception details, or gate-failure trace |
| Final status | Non-promoted, limited, reviewed, or promoted |

This table structure keeps the chapter aligned with the concrete routing path now implemented in the architecture.

---

## 20.11 Evaluation Equations

A compact decomposition of first-stage success can be written as:

\[
E_1(x) = Q_{\mathrm{sandbox}}(x)\, V_{\mathrm{flags}}(x)\, G_{\mathrm{outcome}}(x)\, C_{\mathrm{calibration}}(x)\, S_{\mathrm{promotion}}(x)
\]

where:

- \(Q_{\mathrm{sandbox}}(x)\) measures sandbox-local quality and readiness;
- \(V_{\mathrm{flags}}(x)\) measures completeness and correctness of validation flags;
- \(G_{\mathrm{outcome}}(x)\) measures whether the gate outcome matches the admissibility class of the case;
- \(C_{\mathrm{calibration}}(x)\) measures whether declared confidence aligns with observed behavior;
- \(S_{\mathrm{promotion}}(x)\) measures promotion stability across repeated or nearby trials.

This equation makes explicit that first-stage success is not reducible to answer fluency. It is a joint property of sandbox quality, validation structure, correct gating, calibrated confidence, and stable promotion behavior.

---

## 20.12 Relationship to Later Evaluation

First-stage evaluation is intentionally narrow in one sense and broad in another.

It is narrow because it focuses on the path from `/reason` through sandbox, validation, and promotion review rather than on long-horizon learning outcomes. It is broad because it includes both semantic quality and governance behavior within the same measurement frame.

This framing preserves a crucial distinction: later-stage evaluation may study long-term memory effects, user outcomes, and system adaptation, but first-stage evaluation determines whether a candidate output was even fit to cross the initial authority boundary.

---

## 20.13 Closing Statement

First-stage evaluation in Ms. Allis includes the sandbox pipeline as part of the measured system, not as a hidden preprocessing step. The framework therefore evaluates `/reason` test cases, validation flags, sandbox-specific quality gates, early-failure diagnostics, gate outcomes, confidence bounds, and promotion stability as linked aspects of one authority-sensitive path.

The result is an evaluation regime that matches the architecture it measures. Sandbox reasoning, gate review, and promotion outcome are treated as one coherent first-stage process, making the system auditable at the exact point where provisional internal state begins to ask for broader authority.
