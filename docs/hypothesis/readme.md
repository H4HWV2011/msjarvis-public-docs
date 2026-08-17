# Hypothesis Research Program

**Repository:** `H4HWV2011/msjarvis-public-docs`  
**Path:** `docs/hypothesis/`  
**Purpose:** Controlled development, testing, and tracking of the hypotheses underlying the Ms. Allis / Quantarithmia research program.

---

## Purpose

This directory contains the working hypotheses that underlie the broader Ms. Allis, Quantarithmia, governed intelligence, semantic geometry, temporal structure, sovereign memory, and community intelligence research program.

The purpose of this directory is to provide a **controlled research-development layer** between conceptual vision and publication-ready scientific claims.

The existence of a document in this directory does **not** mean that its hypothesis has been demonstrated.

A hypothesis may be:

- newly formulated;
- derived from an existing architectural principle;
- decomposed from a broader hypothesis;
- operationalized into measurable variables;
- awaiting preregistration;
- under experimental investigation;
- awaiting blinded analysis;
- supported by evidence;
- not supported;
- inconclusive;
- replicated; or
- prepared for publication.

The repository therefore distinguishes **what the system is**, **what the research program proposes**, and **what empirical investigation has actually established**.

---

# Relationship to the Rest of the Repository

The research program is intentionally divided into different layers.

```text
docs/
├── thesis/
│   └── As-built architecture, implementation, validation,
│       operational evidence, and system documentation
│
├── vision/
│   └── Conceptual theories, long-range propositions,
│       intellectual lineage, and future research directions
│
└── hypothesis/
    └── Explicit research hypotheses and their
        operationalization, dependencies, experiments,
        evidence, and disposition
````

These layers must not be treated as interchangeable.

### `thesis/`

Documents what has been designed, implemented, tested, validated, or otherwise established as part of the system's development.

### `vision/`

Documents broader intellectual propositions, theoretical ideas, conjectures, and possible future directions.

### `hypothesis/`

Documents propositions that are being treated as **research hypotheses capable of empirical or formal evaluation**.

A statement appearing in `vision/` does not automatically become a hypothesis.

Likewise, an architectural feature documented in `thesis/` does not automatically prove the hypothesis that motivated it.

---

# Core Research Principle

The research program follows a simple distinction:

> **Implementation is not proof.**

A mechanism may be implemented without its associated hypothesis being demonstrated.

Conversely, a hypothesis may receive empirical support without every production mechanism associated with the broader architecture being complete.

Therefore each hypothesis must maintain its own evidence state.

The research program seeks to answer:

1. **What exactly is being claimed?**
2. **What larger proposition does the claim depend upon?**
3. **What observations would support the claim?**
4. **What observations would falsify the claim?**
5. **What experiment or formal analysis can distinguish those outcomes?**
6. **What has actually been demonstrated?**
7. **What remains unresolved?**
8. **Which other hypotheses depend upon the result?**

---

# Hypothesis Registry

The authoritative index for this directory is:

`hypothesis-registry.md`

The registry records the current research program without assuming in advance how many hypotheses ultimately exist.

The program may contain H1–H15, fewer, more, or hierarchical sub-hypotheses.

**Hypothesis numbering must not be assigned merely to fill a predetermined range.**

A new hypothesis receives an identifier only after its independence, relationship to existing hypotheses, and testability have been reviewed.

---

# Hypothesis Hierarchy

The research program may contain multiple levels of claims.

For example:

```text
Foundational proposition
        │
        ├── Derived hypothesis
        │       ├── Experimental hypothesis A
        │       └── Experimental hypothesis B
        │
        └── Derived hypothesis
                └── Experimental hypothesis C
```

This distinction is important.

Two documents may appear to describe different theories while actually representing:

* a parent hypothesis and a child hypothesis;
* a general proposition and a domain-specific test;
* an architectural mechanism and an empirical consequence; or
* separate hypotheses that merely share infrastructure.

The registry therefore records dependencies explicitly.

---

# Research Status

Hypotheses use the following research lifecycle where applicable.

| Status                    | Meaning                                                                                                      |
| ------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Draft**                 | The idea is being formulated and is not yet sufficiently specified for testing.                              |
| **Formulated**            | The proposition has a defined claim but may still require operationalization.                                |
| **Operationalized**       | Variables, conditions, outcomes, and evaluation criteria have been specified sufficiently for investigation. |
| **Preregistered**         | The experimental or formal protocol has been frozen before outcome analysis.                                 |
| **Data Collected**        | Required observations or experimental outputs have been generated.                                           |
| **Blinded**               | Outcome analysis is being performed without access to information that could bias interpretation.            |
| **Analyzed**              | The planned analysis has been completed.                                                                     |
| **Supported**             | The available evidence supports the stated hypothesis under the defined conditions.                          |
| **Not Supported**         | The evidence does not support the hypothesis under the defined conditions.                                   |
| **Inconclusive**          | The evidence does not permit a reliable determination.                                                       |
| **Replicated**            | The result has been independently or appropriately repeated according to the relevant protocol.              |
| **Publication Candidate** | The hypothesis and supporting evidence are sufficiently mature for inclusion in a publication package.       |
| **Published**             | The research has been formally released as part of the applicable publication record.                        |

A status must never be upgraded merely because implementation has advanced.

---

# Evidence States

Each hypothesis should separately record its evidence state.

Suggested evidence categories are:

* **Conceptual** — supported only by reasoning or theoretical argument.
* **Architectural** — represented by an implemented or specified mechanism.
* **Operational** — demonstrated through system operation.
* **Empirical** — evaluated through a defined experiment or observational study.
* **Formal** — supported by mathematical proof or formal derivation.
* **Replicated** — independently or appropriately reproduced.
* **Unresolved** — evidence remains insufficient.

These categories describe the **kind of evidence**, not whether the hypothesis is true.

For example:

> Architectural evidence does not constitute empirical confirmation.

---

# Experimental Discipline

Experiments associated with a hypothesis should be specified before outcome interpretation whenever practical.

A hypothesis experiment should identify:

* research question;
* hypothesis;
* null hypothesis where appropriate;
* independent variable(s);
* dependent variable(s);
* control condition;
* treatment condition;
* dataset or sampling procedure;
* exclusion criteria;
* evaluation metric;
* statistical or analytical method;
* stopping rule;
* reproducibility requirements;
* blinding requirements;
* provenance requirements;
* expected falsification conditions.

Where an experiment has been preregistered, the preregistration becomes part of the evidence chain.

---

# Negative Results

A result that does not support a hypothesis is a valid research outcome.

The repository must not rewrite a hypothesis after observing an unfavorable result merely to preserve the original claim.

If a hypothesis changes materially after experimentation, the revised proposition should receive a new version, and where appropriate, a new hypothesis identifier.

The original hypothesis and its result remain part of the research history.

---

# Relationship to Existing Research

Several existing documents already contain explicit or implicit hypotheses.

Examples include:

* **Does Meaning Require Geometry?**
* **Referential Conditions, Warranted Inference, and Physical Meaning**
* **Does Geographic Meaning Require Geometry?**
* **Kidd's Syncretic Theorem**
* **The Governed Sovereign Intelligence**
* **The Voice of the Commons — Community Intelligence Without Surveillance**
* **IoT Data Commons Corridor**

These documents should not automatically be duplicated here.

Instead, the hypothesis registry should identify:

1. which existing vision documents contain a research hypothesis;
2. which portions constitute independent hypotheses;
3. which propositions are parent theories;
4. which are subsidiary hypotheses;
5. which are architectural principles rather than hypotheses;
6. which remain conjectures;
7. and which have already been converted into experimental protocols.

The `hypothesis/` directory is therefore an **organizational and scientific control layer**, not a wholesale copy of `vision/`.

---

# Current Research Example

The research program already contains an active empirical investigation under:

**Does Meaning Require Geometry?**

Its central proposition concerns whether structured relational constraints contribute measurably to evidence-bounded semantic behavior.

That investigation demonstrates the intended distinction between:

```text
Vision
   ↓
Hypothesis
   ↓
Operationalization
   ↓
Experimental Protocol
   ↓
Data
   ↓
Blinded Analysis
   ↓
Result
   ↓
Interpretation
```

The existence of the architecture that motivated the experiment does not determine its outcome.

The experiment must be allowed to support, weaken, falsify, or leave unresolved the proposition being tested.

---

# Research Dependencies

Hypotheses may depend upon other hypotheses.

Dependencies must be recorded explicitly rather than inferred from chapter numbering.

For example:

```text
H01
Referential Constraint Principle
        │
        ├── H01a
        │   General relational-semantic dependence
        │
        └── H01b
            Geographic referential dependence
```

A dependency means that the interpretation of one hypothesis may rely upon the outcome or validity of another.

It does **not** necessarily mean that the child hypothesis is untestable until the parent is proven.

The registry should explain the precise dependency.

---

# Hypothesis vs. Architecture

The following distinction is mandatory throughout this directory.

### Architecture asks:

> **Can we build the mechanism?**

### Validation asks:

> **Does the mechanism operate as specified?**

### Hypothesis testing asks:

> **Does the observed result support the proposition the mechanism was intended to test?**

These are different questions.

A successful implementation may establish:

> The mechanism exists and behaves according to specification.

It does not automatically establish:

> The underlying scientific proposition is true.

---

# Publication Discipline

Hypotheses in this directory are developed individually, but publication should generally occur as a **coherent research package** rather than through ad hoc release of isolated claims.

Publication readiness should consider:

* maturity of the hypothesis;
* completeness of the experimental protocol;
* availability and provenance of data;
* reproducibility;
* statistical or formal analysis;
* relationship to dependent hypotheses;
* negative and null results;
* competing explanations;
* limitations;
* and consistency with the broader research program.

The purpose is not to delay publication indefinitely.

The purpose is to avoid presenting a partially developed hypothesis as though it were the final conclusion of the research program.

---

# What This Directory Is Not

This directory is not:

* a list of things the system already proves;
* a replacement for the thesis;
* a collection of implementation specifications;
* a collection of untestable aspirations;
* a prediction that every hypothesis will be supported;
* or a predetermined list of exactly fifteen theories.

The number of hypotheses is an empirical organizational result of the research audit.

If one hypothesis decomposes into three independent testable propositions, the registry should reflect that.

If three apparent hypotheses are discovered to be one proposition tested in three domains, the registry should reflect that instead.

---

# Research Integrity Rule

The research program must preserve the distinction between:

> **What we believe.**

> **What we built.**

> **What we measured.**

> **What the evidence supports.**

> **What remains conjectural.**

No hypothesis should be marked supported solely because the architecture was designed around it.

No hypothesis should be marked disproven solely because an implementation is incomplete.

No unresolved question should be silently converted into a demonstrated result.

---

# Intended End State

The completed research program should make it possible to move from the repository to a publication package and answer, for every major claim:

```text
What is the hypothesis?
        ↓
Why does it matter?
        ↓
What does it depend upon?
        ↓
What experiment tests it?
        ↓
What was actually measured?
        ↓
What happened?
        ↓
Was the result reproducible?
        ↓
What conclusion is justified?
        ↓
Which higher-level claims remain unresolved?
```

The goal is not to prove the entire research program at once.

The goal is to make every individual claim **traceable, testable, falsifiable where appropriate, and honest about its evidentiary status**.

---

## Governing Principle

> **A theory becomes a research hypothesis when it can be stated precisely enough that evidence could show us that we are wrong.**

And:

> **A demonstrated mechanism is evidence about the mechanism; it is not automatically evidence for the theory that motivated it.**

This directory exists to preserve that distinction.
